---
otero_id: 26568
otero_key: "73B4SXUB"
title: "Measuring Brand Favorability Using Large-Scale Social Media Data"
authors: "Kunpeng Zhang; Wendy Moe"
year: "2021"
journal: "Information Systems Research"
doi: "10.1287/isre.2021.1030"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Measuring Brand Favorability Using Large-Scale Social Media Data

Kunpeng Zhang,<sup>a</sup> Wendy Moe<sup>b</sup>

<sup>a</sup> Department of Decision, Operations & Information Technologies, Robert H. Smith School of Business, University of Maryland, College Park, Maryland 20740; <sup>b</sup> Department of Marketing, Robert H. Smith School of Business, University of Maryland, College Park, Maryland 20740 Contact: kpzhang@umd.edu, https://orcid.org/0000-0002-1474-3169 (KZ); wmoe@umd.edu (WM)

Received: February 3, 2019 Revised: November 1, 2019; June 2, 2020; January 8, 2021 Accepted: March 1, 202 Published Online in Articles in Advance: October 25, 2021

https://doi.org/10.1287/isre.2021.1030

Copyright: © 2021 INFORMS

Abstract. For decades, brand managers have monitored brand health with the use of consumer surveys, which have been re<sup>fi</sup>ned to address issues related to sampling bias, response bias, leading questions, etc. However, with the advance of Web 2.0 and the internet, consumers have turned to social media to express their opinions on a variety of topics and, subsequently, have generated an extremely large amount of interaction data with brands. Analyzing these publicly available data to measure brand health has attracted great research attention. In this study, we focus on developing a method to measure brand favorability while accounting for the measure biases exhibited by social media posters. Speci<sup>fi</sup>cally, we propose a probabilistic graphical model–based collective inference framework and implement a block-based Markov chain Monte Carlo sampling technique to obtain an adjusted brand favorability measure that is correlated with traditional surveybased measures used by brands. For analysis, we collect and examine Facebook data for more than 3,300 brands and about 205 million unique users that interact with those brands via their Facebook brand pages. Our data set is large and contains 6.68 billion likes and full text for 1.01 billion user comments, creating challenges for any modeling efforts. We evaluate the effectiveness of our model via out-of-sample prediction, external ground truth testing, and simulation. All demonstrate that our model performs very well, providing brand managers with a new method to more accurately measure consumer opinions toward the brand using social media data.

History: Ravi Bapna, Senior Editor; Wenjing Duan, Associate Editor. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2021.1030.

Keywords: social media brand measurement large scale probabilistic model block-based MCMC

## 1. Introduction

For decades, brand managers have monitored brand health with the use of consumer surveys. Survey methodologies have been re<sup>fi</sup>ned to address issues related to sampling bias, response bias, leading questions, etc. Recently, with consumers turning to social media, brand managers have shifted their focus to monitoring social media with the assumption that what is said on social media represents the voice of the customer (Surico 2018). Compared with traditional surveys, using social media data can be less expensive and conducted more frequently (if not in real time). As a result, the marketing research industry based on traditional surveys has been steadily losing market share to social media monitoring platforms and research <sup>fi</sup>rms (Denis 2019).

Listening platforms (e.g., BrandWatch) provide social media metrics to represent the voice of the consumer and inform on brand health (Kulkarni 2018). Academic researchers have investigated a vast collection of social media metrics that measure the volume, variance, and valence of online word-of-mouth (see Table 1 for an overview of the various social media metrics examined in the extant research). Volume measures, such as the number of posts, reviews, tweets, etc., are used to re<sup>fl</sup>ect the degree of “chatter” in the marketplace. Valence measures, such as average sentiment or percentage of positive posts, are used to re<sup>fl</sup>ect consumer sentiment toward the brand. So, at a time when social media data are becoming easier and less expensive to access, many brands have adopted social media listening and scaled back on their traditional survey-based marketing research.

However, brands have been slow to adopt social media listening for the purposes of brand monitoring (Sterling 2019) in part because social media monitoring has not lived up to its potential, and the accuracy of commonly used social media metrics, such as average sentiment, has been put into question (Schweidel and Moe 2014). For example, several papers show how average sentiment metrics do not necessarily re<sup>fl</sup>ect the underlying opinion of the underlying customer base (Li and Hitt 2008, Godes and Silva 2011, Moe and Trusov 2011, Moe and Schweidel 2012). Researchers have identi<sup>fi</sup>ed several sources of this measurement bias, ranging from behavioral biases (Schlosser 2005, Hu et al. 2017) to reporting biases (Dellarocas and Wood 2008, Chen et al. 2015) to social dynamics (Moe and Schweidel 2012) to the role of motivation (Toubia and Stephen 2013) to context or venue effects (Schweidel and Moe 2014).

Table 1. Summary of Various Research Literatures on Social Media Metrics

<table><tr><td>Paper</td><td>Model used for the objective</td><td>Data for analysis</td><td>Metrics used or developed</td></tr><tr><td>Schweidel and Moe (2014)</td><td>Jointly model both posted sentiment and venue format choice as two separate but related processes</td><td>7,565 comments from on Enterprise Software Brand (provided by Converseon) from June 2009 to August 2010</td><td>Average sentiment, proposed latent measure</td></tr><tr><td>Moe and Trusov (2011)</td><td>Explicitly model the arrival of posted product ratings and separate the effects of social dynamics on ratings from the underlying baseline ratings</td><td>A sample of 500 products rated and sold on a website of a national retailer of bath, fragrance, and beauty from December 2006 to December 2007</td><td>Average sentiment, variance, and volume</td></tr><tr><td>Ma, Sun and Kekre (2015)</td><td>Dynamic choice model to account for the evolutions of both customers&#x27; voicing decisions and their relationships with firms</td><td>The messages relevant to the firm posted by customers on Twitter from February 2010 to December 2010</td><td>Volume, valence and composite</td></tr><tr><td>Stephen and Galak (2012)</td><td>Multivariate autoregressive time-series model</td><td>Daily loan sales from January 1, 2007 to March 2, 2008, combined with 23,863 Kiva-related forum posts</td><td>Number of posts</td></tr><tr><td>Chevalier and Mayzlin (2006)</td><td>Econometric analysis to construct measures of each firm&#x27;s sales of individual books</td><td>Sales of 3,587 books from Global Books and 2,818 titles that appeared in Publishers Weekly best-seller on Amazon.com and bn.com during 3 periods</td><td>Valence, volume and composite</td></tr><tr><td>Borah and Tellis (2016)</td><td>Individual and panel vector autoregressive model</td><td>48 nameplates from four brands from January 1, 2009 to April 15, 2010</td><td>Number of negative posts (composite valence-volume)</td></tr><tr><td>Moe and Schweidel (2012)</td><td>Probit/ordered probit process to model individual&#x27;s online posting behavior</td><td>A total of 10,460 ratings across 1,811 products posted by 4,974 unique individuals on BazaarVoice</td><td>Volume, variance, valence, and composite</td></tr><tr><td>Godes and Silva (2011)</td><td>Econometric regression analysis</td><td>Book reviews for each of the top 350 selling titles as of noon, October 27, 2005 on Amazon.com.</td><td>Average sentiment</td></tr><tr><td>Li and Hitt (2008)</td><td>A theoretical model of buyers&#x27; self-selection in reviews over time</td><td>Book review from Amazon.com</td><td>Average sentiment</td></tr><tr><td>Tirunillai and Tellis (2014)</td><td>Use EGARCH process to identify which metric of UGC is related to stock market performance</td><td>347,628 product reviews across 15 firms in five markets between June 2005 and January 2010.</td><td>Volume, valence and composite</td></tr><tr><td>Chintagunta, Gopinath, and Venkataraman (2010)</td><td>Regression analysis</td><td>Daily box office ticket sales data on all movies released from November 2003 to February 2005.</td><td>Valence, volume and variance</td></tr><tr><td>Luo, Zhang, and Duan (2013)</td><td>Vector autoregressive model</td><td>Daily data from multiple sources for social media during the period of August 1, 2007 to July 31, 2009</td><td>Volume and valence</td></tr><tr><td>Yang, Ren, and Adomavicius (2019)</td><td>Econometric regression analysis</td><td>Facebook posts, comments, and likes of 41 companies in six industries in 2012</td><td>Volume, valence and composite</td></tr><tr><td>Bapna, Benner, and Qiu (2019)</td><td>Econometric regression analysis</td><td>Facebook profile pages of 23 firms from the flash sales segment of the retail industry</td><td>Volume, valence and composite</td></tr><tr><td>Ho, Wu, and Tan (2017)</td><td>Hierarchical Bayesian model to understand individual&#x27;s decisions of whether to post a rating and what rating to post</td><td>Purchase histories and review entries by 1,000 randomly selected individuals on products of 10 categories from March 2006 to November 2011</td><td>Volume, variance and composite</td></tr></table>

This paper further contributes to the aforementioned stream of research. Our goal is to provide a methodology for brand managers to more accurately measure consumer sentiment toward their brand using social media data. Although many of the papers mentioned investigate the behavioral underpinnings of social media behavior, few have provided a measurement tool that directly addresses and accounts for these biases. One exception is Schweidel and Moe (2014) in which the authors provide a model that accounts for venue bias and provides a latent brand health measure that accurately tracks changes in sentiment for a single brand over time. Although the ability to track a brand over time is important, brand managers still face the challenge of how to compare their brand to others using social media data, an application not addressed by Schweidel and Moe (2014). This is the gap we aim to <sup>fi</sup>ll with this paper and our proposed methodology.

In this paper, we consider how a commonly used social media metric, average sentiment, is subject to user positivity bias and may not accurately represent differences across brands (see Baumgartner and Steenkamp 2001, Paulhus 1991 for a review of various response biases). Although the extant literature has identi<sup>fi</sup>ed a variety of different biases when consumers respond to surveys, we focus on one speci<sup>fi</sup>c bias that may be present on social media as a starting point. Speci<sup>fi</sup>cally, we consider how heterogeneity in a user’s tendency to be positive (or negative) can bias average sentiment metrics and propose a method that accommodates these user differences in an effort to provide a more accurate brand sentiment measure. Moreover, various computational methods have been implemented to address information systems problems, in particular understanding social media content using text mining (Abbasi et al. 2018, Adamopoulos et al. 2018, Lee et al. 2018) and enhancing social media analysis via visual analytics (Liu et al. 2020, Shin et al. 2020). Similarly, our data-driven analysis is based on large-scale social media activities and makes the following contributions.

We propose a novel framework for measuring brand favorability using probabilistic graphical models that capture interactions between users and brands, including both likes and textual comments.

We use a very large (approximately 2.2 TB) realworld online data set to test and demonstrate the effectiveness of our proposed inference algorithm on measuring off-line brand favorability.

To deal with large-scale data, we investigate conditional independence among variables in the graphical model and propose a parallelized block-based Markov chain Monte Carlo (MCMC) algorithm for ef<sup>fi</sup>cient inference.

Finally, we design different ways to test the performance of our brand favorability measure method: (1) we perform simulations and validate our algorithm and assumptions; (2) we compare our proposed brand favorability measure with an external ground truth brand favorability ranking from Kantar Millward Brown’s brand valuation ranking, BrandZ; and (3) we assess out-of-sample model <sup>fi</sup>t for multiple time periods. All tests perform signi<sup>fi</sup>cantly well.

The resulting method provides a measure of brand favorability that tracks established survey-based methods (i.e., BrandZ) using social media data. The use of social media data provides more timely and accessible data for market researchers and provides a signi<sup>fi</sup>cant methodological improvement for brand managers.

The rest of this paper is organized as follows. We <sup>fi</sup>rst describe our framework for measuring brand favorability (and user positivity) before discussing the speci<sup>fi</sup>cs of our data collection, data processing and cleansing, senti ment coding, and estimation procedure. From there, we discuss the empirical results pertaining to our proposed brand favorability measure. We then evaluate our proposed algorithm using simulation, out-of-sample <sup>fi</sup>t, and external ground truth data and conclude with a discussion of practical implications for social media brands.

## 2. Research Methodology

Easily observable to each brand is the sentiment expressed by the many users engaged with its brand page. This sentiment can be expressed as a like or in the text of a posted comment. However, this sentiment is also subject to directional bias depending on the positivity/negativity of the user providing the opinion (see Baumgartner and Steenkamp 2001, Paulhus 1991 for a review of various response biases).<sup>1</sup> From a single brand’s perspective, it is impossible to gauge the positivity/negativity of the individuals engaged with its page. Additional data on the positivity/negativity of its users on other brand pages is necessary to estimate each individual’s general tendency to be positive or negative in order to arrive at an adjusted brand favorability measure.

Previous researchers also propose methods to accommodate consumer heterogeneity, distinguishing between heterogeneity in brand preferences versus heterogeneity in how consumers express themselves online. For example, research on product recommendation systems (Adomavicius et al. 2019) focus on the consumer heterogeneity seen across brands, by which variation in consumer brand preferences results in different brands appealing to different consumer segments. In contrast, research on social media behavior focuses on heterogeneity across consumers in terms of the bias present in expressed consumer sentiment (Schweidel and Moe 2014). Here, we provide a larger framework that accommodates both heterogeneity across consumers in terms of the potential positivity bias present in their social media activity as well as heterogeneity across brands with the goal of providing a measure of brand favorability that is comparable across brands regardless any user heterogeneity that may be present in the data.

Figure 1 illustrates the collective inference framework we use to estimate brand favorability and user positivity based on the observed sentiment expressed by users across multiple brand pages. Although the sentiment of the user–brand interaction is observed, we estimate user positivity and brand favorability as latent constructs and assume that both drive sentiment. Speci<sup>fi</sup>cally, we model the latent favorability of brand $j ~ ( F _ { j } )$ , the positivity property of user $\textit { i } ( P _ { i } )$ , and the sentiment of user $i ^ { \prime } \mathrm { s }$ activity on brand $j ^ { \prime } \mathbf { s }$ Facebook page $( S _ { i j } )$ as random variables. The sentiment of the engagement activity, $S _ { i j } ,$ is dependent on both the favorability of brand j and the general positivity of user i. For simplicity, we assume all random variables are binary. That is, user positivity can take a high value (meaning a positive person) or a low value (meaning a nonpositive person), similarly to brand favorability. The sentiment of the user–brand interac tion is either positive (P) or nonpositive (NP).<sup>2</sup>

Figure 1. Collective Inference Framework  
![](/api/attachments/73B4SXUB/fulltext/images/bfbb63f26e4ac63a45fe6317a4c7680b51da673fc40e30c276082a0a22d5a169.jpg)

We assume that each variable has its own probability distribution (or a probability mass function in this discrete case) that explains the variation in the positivity property across users and the difference in favorability across brands. For instance, a positive sentiment (positive comment or like) is more likely to be expressed by a positively inclined user for a favorable brand. If a brand has a low favorability, it obviously attracts more nonpositive comments. In this case, we observe some weakly negative comments made by easygoing users who usually write positive comments. If a brand has a lower favorability and most of the comments came from tough users who usually write negative comments, then those comments are construct a probabilistic graphical model that is depicted in Figure 1. A graphical model has been successfully and widely used in many business domains, such as predicting bank failure based on historical data (Sarkar and Sriram 2001) and examining belief revision for the modi<sup>fi</sup>cation of existing data in a probabilistic relational database (Dey and Sarkar 2000).

The goal of our task is to infer brand favorability (F) for m brands and user positivity (P) for n users from the sentiment expressed (S) by the K observed user engagement activities with the brands. To this end, we infer the probability of Fs and Ps from all observed Ss as represented by the following Equation (1).

$$
\begin{array}{r l} & {P r (F _ {\mathrm{j}} \mid S _ {1 1}, S _ {1 2}, \ldots , S _ {\mathrm{ij}}, \ldots , S _ {\mathrm{K}})} \\ & {\quad = \sum_ {F _ {- j}, P} P r (F _ {1}, F _ {2}, \ldots , F _ {m}, P _ {1}, P _ {2}, \ldots , P _ {n}} \\ & {\qquad \mid S _ {1 1}, S _ {1 2}, \ldots , S _ {i j}, \ldots , S _ {K})} \\ & {\qquad \qquad P r (F _ {1}, F _ {2}, \ldots , F _ {m}, P _ {1}, P _ {2}, \ldots , P _ {n},} \\ & {\quad = \sum_ {F _ {- j}, P} \frac {S _ {1 1} , S _ {1 2} , \ldots , S _ {i j} , \ldots , S _ {K})}{\sum_ {i , j} S _ {i j}},} \\ & {P r (P _ {\mathrm{i}} \mid S _ {1 1}, S _ {1 2}, \ldots , S _ {\mathrm{ij}}, \ldots , S _ {\mathrm{K}})} \\ & {\quad = \sum_ {P _ {- i}, F} P r (F _ {1}, F _ {2}, \ldots , F _ {m}, P _ {1}, P _ {2}, \ldots , P _ {n}} \\ & {\qquad \mid S _ {1 1}, S _ {1 2}, \ldots , S _ {i j}, \ldots , S _ {K})} \\ & {\qquad \qquad P r (F _ {1}, f _ {2}, \ldots , F _ {m}, P _ {1}, P _ {2}, \ldots , P _ {n}, S _ {1 1},} \\ & {\quad = \sum_ {P _ {- i}, F} \frac {S _ {1 2} , \ldots , S _ {i j} , \ldots , S _ {K})}{\sum_ {i , j} S _ {i j}},} \end{array}\tag{1}
$$

where $1 \ \leq \ i \ \leq \ n , \ 1 \ \leq \ j \ \leq \ m , \ S _ { i j }$ is the sentiment expressed by user i’s engagement activity with brand $j , F _ { - j }$ denotes all brand favorability values excluding $F _ { j } ,$ and $P _ { - i }$ denotes all user positivity values excluding $P _ { i } .$ As each user might have multiple engagement activities with the same brand, we specify the sentiment score as the ratio of the number of positive activities (comments or likes) to the number of total activities. This represents the fraction of user–brand interactions that are positive. Furthermore, we treat sentiment scores as binary: positive for scores larger than a threshold (τ) and nonpositive otherwise.

Table 2. Conditional Probability Distribution for $F _ { j } , P _ { i } , S _ { i j } .$ ${ S _ { i j } } ^ { P } { : }$ Sentiment Is Positive, $S _ { i j } ^ { \phantom { N } N } \colon$ Sentiment Is Non-positive

<table><tr><td> $F_j$ </td><td> $P_i$ </td><td> $S_{ij}^P$ </td><td> $S_{ij}^N$ </td></tr><tr><td>L</td><td>L</td><td>δ</td><td>1-δ</td></tr><tr><td>L</td><td>H</td><td>α</td><td>1-α</td></tr><tr><td>H</td><td>L</td><td>β</td><td>1-β</td></tr><tr><td>H</td><td>H</td><td>γ</td><td>1-γ</td></tr></table>

In order to calculate the probability represented in Equation (1), we begin by specifying the conditional probability distribution, $\overline { { P r ( \bar { S } _ { i j } \mid \bar { F } _ { j } , \bar { P } _ { i } ) } }$ according to Table 2. The probability that expressed sentiment is positive given that the brand is highly favorable and the user is strongly positive is denoted as $\gamma ,$ and δ represents the probability that the expressed sentiment is positive when the brand is less favorable and the user is nonpositive. The parameter α represents the probability that expressed sentiment is positive when the brand is less favorable and the user is very positive, and $\beta$ represents the probability that the expressed sentiment is positive when brand favorability is high and user positivity is low. To facilitate more ef<sup>fi</sup>cient estimation, we constrain $\alpha < \beta .$ . This constraint assumes that users with lower positivity are more likely to engage in a positive way with brands of higher favorability than users with higher positivity would with brands of lower favorability. Theoretically, α and $\beta$ should not change the brand favorability and user positivity that much because this constraint is equivalently similar to giving more weights to the brand favorability estimation component as compared with the user positivity estimation component in the model.

From the probability statement in Equation (1), we can obtain the probability of $P _ { i }$ and $F _ { j }$ by summing out other variables. However, the denominator (also known as partition function) can be cumbersome to compute because of a large discrete state space. For our data, we have billions of comments generated by millions of users on thousands of brands. Although each sentiment variable $S _ { i j }$ is binary, the state space of the denominator is exponentially huge. Thus, we apply MCMC methods.

To estimate the model using MCMC methods, a Markov chain is constructed to converge to a target distribution, and then samples are taken from the Markov chain. The state of each chain is assigned to the variables being sampled, and the transitions between states follow a rule based on MCMC methods. The rule asserts that the next state of a chain is reached by sequentially sampling all variables based on their distribution when conditioned on the current values of all other variables and the data. To apply this algorithm, we de<sup>fi</sup>ne the full conditional marginal distribution $P r ( F _ { j } \mid F _ { - j } , P , S )$ for brands and $P r ( P _ { i } \mid P _ { - i } ,$ $F , S )$ for users. The distribution uses the probabilistic arguments from Table 2 by canceling out some terms because of the properties of Bayesian theory, which yields

$$
\begin{array}{c} P r (F _ {j} | F _ {- j}, P, S) = \frac {P r (F , P , S)}{P r (F _ {- j} , P , S)} \\ = \frac {P r (F , P , S)}{\sum_ {F _ {j}} P r (F , P , S)} \\ = \frac {P r (F _ {1}) \cdots P r (F _ {m}) \cdot P r (P _ {1}) \cdots P r (P _ {n}) \cdot \prod_ {i , j} P r (S _ {i j} | P _ {I} , F _ {j})}{\sum_ {F _ {j}} P r (F _ {1}) \cdots P r (F _ {m}) \cdot P r (P _ {1}) \cdots P r (P _ {n}) \cdot \prod_ {i , j} P r (S _ {i j} | P _ {I} , F _ {j})} \\ = \frac {P r (F _ {j}) \prod_ {i} P r (S _ {i j} | P _ {i} , F _ {j})}{\sum_ {F _ {j}} P r (F _ {j}) \prod_ {i} P r (S _ {i j} | P _ {i} , F _ {j})} \end{array} ,\tag{2}
$$

$$
\begin{array}{c} P r (P _ {i} | P _ {- i}, F, S) = \frac {P r (P , F , S)}{P r (P _ {- i} , F , S)} \\ = \frac {P r (P , F , S)}{\sum_ {P _ {i}} P r (P , F , S)} \\ = \frac {P r (F _ {1}) \cdots P r (F _ {m}) \cdot P r (P _ {1}) \cdots P r (P _ {n}) \cdot \prod_ {i , j} P r (S _ {i j} | P _ {i} , F _ {j})}{\sum_ {P _ {i}} P r (F _ {1}) \cdots P r (F _ {m}) \cdot P r (P _ {1}) \cdots P r (P _ {n}) \cdot \prod_ {i , j} P r (S _ {i j} | P _ {i} , F _ {j})}, \\ = \frac {P r (P _ {i}) \prod_ {j} P r (S _ {i j} | P _ {i} , F _ {j})}{\sum_ {P _ {i}} P r (P _ {i}) \prod_ {j} P r (S _ {i j} | P _ {i} , F _ {j})} \end{array}\tag{3}
$$

where $P _ { - i }$ represents $\{ P _ { 1 } , P _ { 2 } , . . . , P _ { i - 1 } , P _ { i + 1 } , . . . , P _ { n } \}$ and $F _ { - j }$ represents $\{ F _ { 1 } , F _ { 2 } , . . . , F _ { j - 1 } , F _ { j + 1 } , . . . , F _ { m } \}$ . Additionally, $S$ represents all $S _ { i j } { \bf s } , \ F$ represents all $F _ { j } \mathbf { s } ,$ , and $P$ represents all $P _ { i } \mathbf { s }$

Because we have millions of users and thousands of brands, sampling users and brands sequentially is computationally burdensome and can be slow. With further investigation of our model, we realize that there are several conditional independencies that can make the inference calculation more ef<sup>fi</sup>cient. First, $F _ { 1 } ,$ $F _ { 2 } , \dots , F _ { j } , \dots , F _ { m }$ are independent of each other given all $P _ { 1 } , P _ { 2 } , \ldots , P _ { i } , \ldots , P _ { n }$ and all observed variables $S _ { i j } .$ Similarly, $P _ { 1 } , \ P _ { 2 } , \ \ldots , \ P _ { i } , \ \ldots , \ P _ { n }$ are independent of each other given all $F _ { 1 } , F _ { 2 } , \ \dots , F _ { j } , \ \dots , F _ { m }$ and all $S _ { i j } .$ The following two cases show the conditional independence of $F _ { x }$ and $F _ { y }$ given all $P$ and S, similar cases for P.

![](/api/attachments/73B4SXUB/fulltext/images/5569d65d0c56dcf64d44e13d341b71e9f5af69baa2cb3048116dddc07770efa1.jpg)  
Figure 2. Illustration of Conditional Independence  
Note. Shaded variables mean that they are known.

Brands $F _ { x }$ and $F _ { y }$ do not have any common users as shown in Figure 2(a). It is obviously that $F _ { x }$ and $F _ { y }$ are independent given all $P _ { 1 } , P _ { 2 } , \dots , P _ { a } , \dots , P _ { b } , \dots , P _ { n }$ and $S _ { i j } .$

Brands $F _ { x }$ and $F _ { y }$ have common users $P _ { c }$ as shown in Figure 2(b). They are still conditional independent because $P _ { c }$ blocks the path from $F _ { x }$ to $F _ { y }$ given $S _ { c x }$ and $S _ { c y }$ are known.

These conditional independencies allow us to sample brands and users in parallel. Thus, we implement a block-based MCMC method that processes users and brands as two separate blocks. We alternately sample all $P _ { i } s$ and $F _ { j } s$ in each sampling round. The algorithm converges fast after we collect sampled values for approximately 150\~200 rounds in parallel. The sketch of the algorithm is outlined as follows. The detailed performance evaluation is depicted in Online Appendix C.

## <sub>Algorithm 1</sub> (Parallelized Block-Based MCMC)

Input: $\begin{array} { r } { 1 \leq i \leq n , 1 \leq j \leq m ; } \end{array}$ noise factor δ; conditional probability distribution parameters α and β; sentiment threshold $\gamma ~ ( \mathrm { e . g . } , ~ \alpha = \bar { 0 } . 3 , ~ \beta = 0 . 6 , ~ \delta = 0 . 1 , ~ \gamma = 0 . 9 ,$ τ 0.7)

1. Initialize brand favorability and user positivity: $P r ( F _ { j } )$ and $P r ( P _ { i } )$ ;

2. Obtain sentiment $\mathrm { S } _ { i j }$ for each comment;

3. repeat:

4. For the kth round:

5. Sampling all $F _ { j } s$ based on Equation (2) in parallel;

6. Sampling all $P _ { i } s$ based on Equation (3) in parallel;

7. calculate $\begin{array} { r } { P r ( F _ { j } ) = \frac { \sum _ { t = 1 } ^ { k } F _ { j } ^ { ( k ) } } { k } , P r ( P _ { i } ) = \frac { \sum _ { t = 1 } ^ { k } P _ { i } ^ { ( k ) } } { k } ; } \end{array}$

8. until the target distributions (Pr P and $P r ( F _ { j } ) )$ converge

9. Output: brand favorability and user positivity: $P r ( F _ { j } )$ <sup>'</sup>s and $P r ( P _ { i } ) ` { : }$ s.

## 2.1. Facebook Data Collection and Cleansing

Before detailing our methodology, we describe the nature of our data to provide context for our method discussion. We collected a large data set from Facebook, focusing on brand pages from Englishspeaking countries (i.e., the brands from the United

States, the United Kingdom, India, Australia, etc.). These brand pages represent a variety of different types of brands, including but not limited to commercial brands, celebrities, sports teams, nonpro<sup>fi</sup>t organizations, etc. We use the Facebook Graph $\mathrm { A P I ^ { 4 } }$ to download all available activities made by a brand on its Facebook page (i.e., posts) and all available activities made by users on the brand’s Facebook page (i.e., comments on posts and likes on posts).<sup>5</sup> The data set used for this study includes all activity starting from the day the brand page was created on Facebook<sup>6</sup> through January 1, 2018.

To create our <sup>fi</sup>nal data set, we cleanse the data of any users who made very few comments $( \mathrm { i . e . , }$ fewer than <sup>fi</sup>ve across all brands).<sup>7</sup> We also identify and remove fake accounts (Vlasselaer et al. 2016) and fraudulent activities using an approach similar to that used in Zhang et al. (2016) by removing the following:

1. Users who commented on more than 100 brand pages or liked posts on more than 150 brand pages (the average user comments on four to <sup>fi</sup>ve pages and likes posts on seven to eight different pages).

2. Users who liked more than 90% of the posts on a brand page (the average user liked 0.094% posts).

3. Users who posted duplicate comments containing URL links, which often direct to phishing sites (e.g., CNN’s brand page contained 237,101 duplicate user comments out of a total of 12,468,286 posted user comments).

The <sup>fi</sup>nal data set contains data from 3,355 brand pages and approximately 205 million users.<sup>8</sup> Table 3 describes the resulting data set and Online Appendix B shows the distribution of data.

Table 3. Dataset Description and Statistics After Cleansing

<table><tr><td>Description</td><td>Volume</td></tr><tr><td>Number of brands</td><td>3,355</td></tr><tr><td>Number of brand posts</td><td>11,253,623</td></tr><tr><td>Number of unique users</td><td>205,528,593</td></tr><tr><td>Number of user comments</td><td>1,011,588,619</td></tr><tr><td>Number of likes</td><td>6,681,320,439</td></tr></table>

## 2.2. Sentiment Coding

In our context, user interactions with the brand page can be in the form of likes or comments. We treat all likes as a positive engagement activity.<sup>9</sup> However, classifying the textual content of comments as positive, negative, or neutral requires more complex analysis. To codify the sentiment of posted comments, we use sentiment analysis that leverages natural language processing, text analysis, and computational linguistics. Recently, there has been a wide range of research done on sentiment analysis from rule-based, corpusbased approaches to machine learning techniques (Zhang et al. 2018). In this paper, we develop a sentiment identi<sup>fi</sup>cation algorithm that integrates three components (details can be found in Online Appendix A):

1. A linguistic rule-based method extended from basic compositional semantic rules (Choi and Cardie 2008).

2. A numeric sentiment identi<sup>fi</sup>cation to classify sentiment as a continuous numerical score to re<sup>fl</sup>ect sentiment strength (Xie et al. 2014).

3. A dictionary-based method to consider special characters used in social media text (e.g., emoticons).

## 2.3. Estimation Procedure

Our estimation procedure consists of two stages. In the <sup>fi</sup>rst stage, we apply our model to all nine years of data (all comments and likes posted by all users across all brands) and obtain user positivity scores for each of the 205.53 million users and brand favorability scores for each of the 3,355 brands in our data. These user positivity and brand favorability scores refer to the posterior estimate of each user’s probability of being high positivity and each brand’s probability of being high favorability, respectively.

In the second stage of our estimation, we assume that user positivity is a user trait and, therefore, is relatively static but acknowledge that brand favorability can change over time. Thus, we recalculate brand favorability probabilities (all $F _ { j } \mathbf { s } )$ for each year based on the user positivity scores obtained from the <sup>fi</sup>rst stage and the sentiment of user engagements $( S _ { i j } \mathsf { s } )$ observed in that year.<sup>10</sup>

It is important to note that this is a very large data set that poses some serious challenges for estimation. Beyond just the issue of computing power (we estimated the model on a machine with 256 GB memory and 24 cores), we also made some simplifying assumptions regarding the conditional probability distribution presented in Table 2. Our model contains four parameters as shown in Table 2 and one sentiment threshold parameter τ. Given the size of the data, it is infeasible to use traditional Bayesian methods to estimate these parameters. Instead, we estimated the resulting brand favorability and user positivity measures using each of 2,304 possible parameter combinations, assuming that each parameter potentially has nine discrete values with a range (0.1, 0.9) subject to the following simplifying constraints: (1) $\alpha < \beta$ (see explanations in Section 2); (2) δ $< 0 . 5 \ ( \mathrm { i . e . } ,$ , the case in which both user positivity and brand favorability are low), $\gamma > 0 . 5 \ ( \mathrm { i . e . } $ , the case in which both user positivity and brand favorability are high), $\tau > 0 . 5$ (the threshold for positive sentiment). For each parameter setting, we calculate the log-likelihood of the model. These log-likelihoods ranged from $- 9 . 1 2 \times 1 0 ^ { 8 } \mathrm { { t o } \ - 4 . 0 8 \times 1 0 ^ { 8 } }$ . The parameter combination with the maximum log-likelihood $( \alpha = 0 . 3 , \beta = 0 . 6 , \delta = 0 . 1 , \gamma = 0 . 9 , \tau = 0 . 7 , \mathrm { { L L } } = - 4 . 0 8 \times$ $1 0 ^ { 8 } )$ was chosen to generate the results we present next.

## 3. Brand Favorability Results

We obtain brand favorability scores across all brands in 2015 and user positivity scores for all individuals. The distribution of user positivity scores indicates signi<sup>fi</sup>cant differentiation across users in terms of their innate tendencies to be positive (see Figure 3). This provides empirical evidence that scale usage heterogeneity exists. Not surprisingly, we also observe dispersion in brand favorability scores (see Figure 4).

Figure 3. (Color online) Distribution of User Positivity Scores (up to December 31, 2015)  
![](/api/attachments/73B4SXUB/fulltext/images/7f2f75821e5b706c816002d4ac1723bcb7f7afe63901db471ff1aa7aff746663.jpg)

Figure 4. (Color online) Distribution of 2015 Brand Favorability Scores  
![](/api/attachments/73B4SXUB/fulltext/images/6199ac1c0d5a32a8bfba72e112a9ed47cba0c126a3922db16e01ac5358b63561.jpg)  
Brand Favorability

Similar results are also found for 2016 and 2017 (see Online Appendix D). The distribution of brand favorability scores shows a clear positive skew. This positive skew is not surprising given that brands can only persist if consumers have a positive opinion of it. This is not to say that all brands are favorably perceived. In fact, in our data, 17.9% of the brands are extremely favorable (i.e., brand favorability > 0.9) and less than 1% have favorability scores below 0.5.

To reiterate, the brand favorability and user positivity scores presented are associated with the parameter combination $\alpha = 0 . 3 , \beta = 0 . 6 , \delta = 0 . 1 , \gamma = 0 . 9 , \tau = 0 . 7 .$ This is the parameter setting that yielded the largest log-likelihood. This parameter combination is the same for years 2016 and 2017 based on the similar procedure of maximizing log-likelihood. To test how sensitive our results are to the parameter settings, we compute brand favorability scores associated with each of the 2,304 parameter combinations and examine the variance in estimates across different parameter settings. The results show that there is very little variation in brand favorability across parameter settings. For example, the average standard deviation in brand favorability scores across parameter settings for the 20 top and 20 bottom brands (as de<sup>fi</sup>ned by the 2015 BrandZ Top 100 rankings) are 0.0035 and 0.0032, respectively. Thus, brand favorability scores resulting from our model are not very sensitive to the parameter combination selected to initiate the model. This gives us con<sup>fi</sup>dence in our methodology and in the robustness of the brand favorability scores that result.

## 4. Evaluation of the Method

To evaluate the performance of our proposed model, we (1) assess model <sup>fi</sup>t using out-of-sample testing; (2) validate our model-based brand favorability measures by comparing them with external, off-line, brandtracking, survey-based data provided by Kantar Millward Brown’s BrandZ ranking; and (3) validate the model via simulation. In addition, we make several assumptions when building the model, such as the static property of user positivity over time. We describe the procedure of testing this assumption using our real data at the end of this section.

## 4.1. Model Fit

We divide our data into training and testing sets in the following way. For each brand, we randomly select 70% of the activities (i.e., user–brand commenting and liking) for the training set. The remaining 30% are used for the testing set.<sup>11</sup> We then estimate our model on the training set to obtain brand favorability for all brands and user positivity for all individuals. We use these brand favorability and user positivity estimates to predict the binary sentiment (positive versus nonpositive) of activities in the testing set, using the same threshold (τ) as in the model estimation.

Table 4 presents the results of our model <sup>fi</sup>t testing. Our model has a high accuracy rate and correctly classi<sup>fi</sup>es 88.1% of the activities as positive or nonpositive in the 2015 testing set, 87.4% in 2016, and 89.1% in 2017. Turning to our measure of precision, of the activities that we predicted to be positive, 86.9% were actually observed to be positive in 2015, 87.1% in 2016, and 88.2% in 2017. In terms of recall, 89.1% of the observed positive activities were also predicted to be positive by our model in 2015, 85.7% in 2016, and 87.7% in 2017. Overall, these measures indicate that our model of brand favorability and user positivity <sup>fi</sup>ts the observed data well.

Table 4. Model Fit

<table><tr><td>Metric</td><td>2015</td><td>2016</td><td>2017</td></tr><tr><td> $Accuracy^a$ </td><td>0.881</td><td>0.874</td><td>0.891</td></tr><tr><td> $Precision^b$ </td><td>0.869</td><td>0.871</td><td>0.882</td></tr><tr><td> $Recall^c$ </td><td>0.891</td><td>0.857</td><td>0.877</td></tr><tr><td> $RMSE^d$ </td><td>0.203</td><td>0.223</td><td>0.210</td></tr></table>

<sup>a</sup>Accuracy is de<sup>fi</sup>ned as the proportion of activities in the testing set that were correctly classi<sup>fi</sup>ed as positive versus non-positive using model predictions.  
<sup>b</sup>Precision is the proportion of activities predicted to be positive which were observed to be positive.  
<sup>c</sup>Recall is the proportion of positive activities that were correctly identi<sup>fi</sup>ed by the model.  
<sup>d</sup>Root mean squared error. It is calculated based on the predicted values before applying the threshold τ.

## 4.2. Validation of Brand Favorability Scores

To validate our brand favorability scores, we compare our social media–based measure of brand favorability against the BrandZ ranking of the top 100 most valuable global brands. This ranking is a standard in marketing research (Lehmann et al. 2008) and is based on both the brand’s <sup>fi</sup>nancial performance and traditional brand tracking surveys. Kantar Millward Brown publishes both the rank and estimated <sup>fi</sup>nancial value for each brand on an annual basis.<sup>12</sup>

As an initial test, we compare the model-based brand favorability scores of the brands in the top of the BrandZ ranking to those in the bottom. On average, the top 20 brands according to BrandZ had a mean favorability score of 0.793, and the bottom 20 brands had a favorability score of 0.702. This difference is signi<sup>fi</sup>cant with p-value < 0.001. Similarly, the top 10 and 30 brands had mean favorability scores of 0.774 and 0.807, and the bottom 10 and 30 brands had mean favorability scores of 0.712 and 0.721, respectively. Note that the predicted favorability scores are not monotonically decreasing for top brands in BrandZ. The difference is signi<sup>fi</sup>cant with p-values < 0.05 and < 0.001, respectively, providing initial con<sup>fi</sup>- dence in our ability to predict BrandZ outcomes with our proposed brand favorability score.

We next examine the relationship between our method and BrandZ’s by calculating the Pearson correlation between the BrandZ value against our social media–based brand favorability score and the Spearman correlation between the BrandZ rank and our estimated brand favorability rank (see Table 5). Because the variation among values of these top BrandZ brands is large, we take “log” to make the distribution well behaved, which is more likely to result in a robust model. For comparison purposes, we also consider the effectiveness of a model-free social media–based measure, average sentiment, a machine learning–based predictive model, and a matrix factorization–based model in predicting BrandZ rank and value (also presented in Table 5).

For the machine learning approach, we predict the favorability scores of top brands in the BrandZ ranking. We use the number of posts, comments, fans, positive comments, negative comments, and likes and the Google trend as features and <sup>fi</sup>t our data in a deep neural network model. We implement a two-layer, fully connected feedforward network with dropout and batch normalization. Note that the results of deep neural networks in Table 5 are reported on the test set. Please refer to Online Appendix E for the details of the network architecture, training/validation, and hyperparameter tuning.

Table 5. Comparison Between Social Media-Based Brand Measures and BrandZ

<table><tr><td>log(BrandZ Value) vs.</td><td>2015</td><td>2016</td><td>2017</td></tr><tr><td>Average sentiment score</td><td>-0.175(p = 0.112)</td><td>-1.205(p = 0.154)</td><td>-1.361(p = 0.144)</td></tr><tr><td>Deep neural network predicted score</td><td>0.114(p = 0.071)</td><td>0.117(p = 0.059)</td><td>-0.109(p = 0.065)</td></tr><tr><td>NMF estimated score</td><td>0.074(p = 0.94)</td><td>0.086(p = 0.952)</td><td>0.091(p = 0.84)</td></tr><tr><td>Favorability score (ours)</td><td>0.326(p = 0.0025)</td><td>0.405(p = 0.0018)</td><td>0.412(p = 0.002)</td></tr><tr><td>BrandZ Rank vs.</td><td>2015</td><td>2016</td><td>2017</td></tr><tr><td>Average sentiment rank</td><td>0(p = 1)</td><td>0(p = 1)</td><td>0(p = 1)</td></tr><tr><td>Deep neural network predicted rank</td><td>0.120(p = 0.07)</td><td>0.131(p = 0.057)</td><td>0.124(p = 0.065)</td></tr><tr><td>NMF estimated rank</td><td>0.083(p = 0.82)</td><td>0.106(p = 0.737)</td><td>0.117(p = 0.905)</td></tr><tr><td>Favorability rank (ours)</td><td>0.437(p &lt; 0.001)</td><td>0.514(p &lt; 0.001)</td><td>0.528(p &lt; 0.001)</td></tr></table>

Note. Values in the upper half of the table are Pearson correlation while those in the lower half are Spearman’s rank correlations.

For the matrix factorization method, we chose the biased nonnegative matrix factorization (NMF) mod el. We <sup>fi</sup>rst form a user–brand matrix in which each cell is the sentiment of comments made by a user on that brand. We then perform NMF to obtain the user factors U and the brand factors V as well as the user–brand biases. Finally, the favorability of each brand is predicted as the average predicted ratings (i.e., each $r _ { i j }$ of brand j by user i is the dot product of $U _ { i }$ and $V _ { j \prime }$ plus the overall average rating of user i) by all users on that brand.

The results show that our proposed brand favorability measure signi<sup>fi</sup>cantly predicts BrandZ rank and value (which are based on both <sup>fi</sup>nancial performance metrics and brand tracking surveys) although the baseline metrics do not. This provides validation that our brand favorability score, which accounts for directional response bias, is a more accurate measure of the brand than baseline metrics, which do not.<sup>13</sup>

## 4.3. Model Validation Using Simulation

We also perform model validation using simulation. Our simulated data are generated based on distributions that are close to reality (i.e., what we observe in the data). The empirical results related to brand favorability and user positivity in our data reveal that both approximately follow a normal distribution. The statistics of our data after cleansing also tell us that each user interacts with seven to eight brands (public fan pages) on average. Thus, we generate our simulated data using the following procedure: (1) We randomly generate 1,000,000 users, and their positivity scores follow a normal distribution with a mean of 0.55 and a variance of 0.1. (2) Similarly, we randomly generate 1,000 brands, and their brand favorability scores follow a normal distribution with mean and variance being 0.55 and 0.1, respectively. (3) We generate the binary sentiment (positive or nonpositive) for a user–brand pair. Each brand interacts with 8,000 randomly selected users, and each sentiment is generated based on the conditional probability set in Table 2. All parameters are <sup>fi</sup>xed using the optimal ones with the largest log-likelihood value on the real data (see details in Section 2.3).

Table 6. Model Comparison to the Ground Truth on the Simulation Data

<table><tr><td>Method</td><td>Brand favorability</td><td>User positivity</td></tr><tr><td rowspan="2">Our method (block-based MCMC)</td><td>0.6334</td><td>0.288</td></tr><tr><td>(p = 0.000)</td><td>(p = 0.000)</td></tr><tr><td rowspan="2">Baseline-1 (average sentiment)</td><td>0.133</td><td>0.181</td></tr><tr><td>(p = 0.504)</td><td>(p = 0.000)</td></tr><tr><td rowspan="2">Baseline-2 (NMF)</td><td>0.128</td><td>0.205</td></tr><tr><td>(p = 0.107)</td><td>(p = 0.000)</td></tr></table>

Note. Values are Spearman’s rank correlations.

We now turn toward applying our method to estimate the brand favorability scores and user positivity scores and compare them with the ground truth in steps 1 and 2. Results are shown in Table 6 in which each cell provides the Spearman rank correlation between the ground truth measure of brand favorability or user positivity and the model-based measure provided by our proposed method (row 2), a simple average sentiment (row 3), or an NMF (row 4) as a baseline comparison. Numbers in the parentheses are p-values. Note that we do not include the machine learning baseline here because we do not have aforementioned features for each brand. From the results, we see that our block-based MCMC algorithm provides a more accurate brand favorability measure as our proposed measure is signi<sup>fi</sup>cantly correlated with the true underlying favorability scores used to generate the data.

## 4.4. Assumption Testing

One assumption in our model is that user positivity is static over time. To test the validity of this assumption, we divide our data into three years: 2015, 2016, and 2017. Within each year, we use our method to estimate user positivity. We then calculate the overlapping percentage of users in the top 25%, 25%–50%, 50%–75%, and bottom 25% across two consecutive years (e.g., 2015–2016 and 2016–2017). The results are provided in Table 7 and show that highly positive users tend to be positive across the years. That is, user positivity is relatively stable, providing con<sup>fi</sup>dence in our assumption that user positivity is relatively static over time.

Table 7. Overlapping Percentage of Users in Different Percentages Regarding Their Positivity Across Two Consecutive Years

<table><tr><td rowspan="2"></td><td rowspan="2">Quartiles</td><td colspan="4">2016</td></tr><tr><td>Top 25%</td><td>25–50%</td><td>50–75%</td><td>75–100%</td></tr><tr><td rowspan="4">2015</td><td>0–25%</td><td>0.750</td><td>0.173</td><td>0.077</td><td>0.0</td></tr><tr><td>25–50%</td><td>0.237</td><td>0.733</td><td>0.03</td><td>0.0</td></tr><tr><td>50–75%</td><td>0.018</td><td>0.083</td><td>0.841</td><td>0.058</td></tr><tr><td>75–100%</td><td>0.027</td><td>0.032</td><td>0.075</td><td>0.866</td></tr><tr><td rowspan="2"></td><td rowspan="2">Quartiles</td><td colspan="4">2017</td></tr><tr><td>Top 25%</td><td>25–50%</td><td>50–75%</td><td>75–100%</td></tr><tr><td rowspan="4">2016</td><td>0–25%</td><td>0.762</td><td>0.144</td><td>0.084</td><td>0.0</td></tr><tr><td>25–50%</td><td>0.132</td><td>0.743</td><td>0.101</td><td>0.024</td></tr><tr><td>50–75%</td><td>0.095</td><td>0.065</td><td>0.685</td><td>0.155</td></tr><tr><td>75–100%</td><td>0.011</td><td>0.049</td><td>0.128</td><td>0.812</td></tr></table>

## 5. Conclusion

Existing research shows that average sentiment metrics often misstate the underlying consumer opinion toward a brand. Our validation exercise corroborates that argument by showing no relationship between observed average sentiment and BrandZ, which employs trusted methods based on <sup>fi</sup>nancial performance metrics and traditional surveys. In contrast, we show that our proposed brand favorability score, using only social media data, is predictive of BrandZ, providing what we argue is a more accurate measure of consumer opinion toward the brand.

In this paper, we argue that directional bias exists on social media brand pages and propose a method that provides a brand favorability measure that accounts for individual differences in providing positive (or nonpositive: neutral or negative) opinions on social media. This research contributes to a growing stream of social media research that examines the effects of behavioral bias in online opinion. It also contributes to a growing body of methodological research focused on providing methods that go beyond simple summary metrics to use social media for more accurate insights. However, modeling the role of directional or positivity bias accounts for only one type of response bias. Survey-based researchers have identi<sup>fi</sup>ed several types of response biases beyond just directional bias, and we encourage future research of these biases in the context of social media.

Overall, social media has the potential to be a valuable source of insights for marketers. However, the data are generated by users who are subject to a number of behavioral biases, compromising the integrity of the data. As a <sup>fi</sup>eld, information systems researchers have only just begun exploring ways to leverage social media data for insights. We hope this paper contributes to that effort and provides some answers as well as motivates some new questions for marketing managers and information systems researchers.

## Endnotes

<sup>1</sup> Directional bias refers to an individual’s tendency to be more positive or negative when expressing opinions. For example, when presented with a response scale, some respondents may favor the higher end of the scale.

<sup>2</sup> The sentiment of activities is coded as positive, negative, and neutral. For simplicity, we model the positivity property of a user as a binary variable. The strength of positivity can be adjusted via the threshold parameter discussed later in detail.

<sup>3</sup> The assumptions we make for the model in this paper might have some limitations; for example, we don’t consider the sentiment of comments from one user to be possibly affected by others. The focus of this paper is to measure off-line brand favorability using large-scale online social media data with some simple and feasible graphical models. Our empirical results show that it can effectively and efficiently achieve this goal.

Please see https://developers.facebook.com/docs/graph-api.

<sup>5</sup> Note that the “share” button was launched in late 2011; hence, we do not use it in this work because of lack of data consistency over the entire time period of analysis.

<sup>6</sup> The first observed brand posts in our data were from January 2009.

<sup>7</sup> We vary this threshold to 3 and 10 and find a relatively consistent result for the year of 2015 (e.g., 0.432 and 0.415 for the correlation between our favorability rank and the BrandZ rank; see details in Section 4.2).

<sup>8</sup> The complete database contains more than 20,000 brand pages. In addition to screening out non-English brand pages, we limited our sample to include only those brand pages with sufficient activity in terms of brand posts, user likes, and posted comments. Each brand in our final data set of 3,355 has at least one brand post, one user like, and one posted comment in each year.

<sup>9</sup> Facebook introduced different emotional response emoticons to their platform on February 24, 2016. After that, the Facebook API still returns different emotions as.“like."

<sup>10</sup> We also estimated the model using only data from 2015 to estimate both user positivity and brand favorability. The results were very similar with brand favorability scores correlated 0.91 across the two methods. Furthermore, no significant differences were observed in any of the subsequent analyses.

<sup>11</sup> Activities in the testing set made by those users who do not exist in the training set are ignored because their positivity scores were unknown when testing.

<sup>12</sup> BrandZ measures financial value by using both corporate earnings data and a brand multiple based on stock price (https://www. brandz.com/articlenew/brandz-brand-valuation-methodology).

Corporate earnings data reflects the brand’s success in the consumer market and thus should also reflect consumer sentiment, The brand multiple, however, may reflect investor sentiment. However, investor sentiment should, in theory, also reflect the potential success in the consumer market (Gupta et al. 2003). This is

evidenced by research showing how social media sentiment is predictive of stock price performance (Bollen et al. 2011).

<sup>13</sup> We also considered other social media metrics, such as the number of likes and the number of followers. Neither were correlated with BrandZ rank or value.

## References

Abbasi A, Zhou Y, Deng S, Zhang P (2018) Text analytics to support sense-making in social media: A language-action perspective. Management Inform. Systems Quart. 42(2):427–464.

Adomavicius G, Bockstedt J, Curley S, Zhang J (2019) Reducing recommender systems biases: An investigation of rating display designs. Management Inform. Systems Quart. 43(4):1321–1341.

Adamopoulos P, Ghose A, Todri V (2018) The impact of user personality traits on word of mouth: Text-mining social media platforms. Inform. Systems Res. 29(3):612–630.

Bapna S, Benner M, Qiu L (2019) Nurturing online communities: An empirical investigation. Management Inform. Systems Quart. 43(2):425–452.

Baumgartner H, Steenkamp J-B (2001) Response styles in marketing research: A cross-national investigation. J. Marketing Res. 38(2): 143–156.

Bollen J, Mao H, Zeng X (2011) Twitter mood predicts the stock market. J. Comput. Sci. 2(1):1–8.

Borah A, Tellis GJ (2016) Halo (spillover) effects in social media: Do product recalls of one brand hurt or help rival brands? J. Marketing Res. 53(2):143–160.

Chen H, Zheng Z, Ceran Y (2015) De-biasing the reporting bias in social media analytics. Production Oper. Management. 25(5):849– 865.

Chevalier J, Mayzlin D (2006) The effect of word of mouth on sales: Online book reviews. J. Marketing Res. 43(3):345–354.

Chintagunta PK, Gopinath S, Venkataraman S (2010) The effects of online user reviews on movie box of<sup>fi</sup>ce performance: Accounting for sequential rollout and aggregation across local markets. Marketing Sci. 29(5):944–957.

Choi Y, Cardie C (2008) Learning with compositional semantics as structural inference for subsentential sentiment analysis. Proc. Conf. Empirical Methods Natl. Language Processing. (Association for Computational Linguistics), 793–801.

Dellarocas C, Wood C (2008) The sound of silence in online feedback: Estimating trading risks in the presence of reporting bias. Management Sci. 54(3):460–476.

Denis S (2019) Social media analytics market expands at 15% CAGR by 201-26 thriving worldwide by top players Salesforce, Oracle Corporation, SAS Institute, Adobe Systems, IBM. Market Report Gazette Online (September 19), https://www.marketreportgazette com/2019/09/social-media-analytics-market-expands-at-15-cagrby-2019-26-thriving-worldwide-by-top-players-salesforce-oraclecorporation-sas-institute-adobe-systems-ibm/.

Dey D, Sarkar S (2000) Modi<sup>fi</sup>cations of uncertain data: A Bayesian framework for belief revision. Inform. Systems Res. 11(1):1–16.

Godes D, Silva JC (2011) Sequential and temporal dynamics of online opinion. Marketing Sci. 31(3):448–473.

Gupta S, Lehmann D, Stuart J (2003) Valuing customers. J. Marketing Res. 41(1):7–18.

Ho Y-C, Wu J, Tan Y (2017) Discon<sup>fi</sup>rmation effect on online rating behavior: A structural model. Inform. Systems Res. 28(3):626–642.

Hu N, Pavlou P, Zhang J (2017) Self-selection biases in online product reviews. Management Inform. Systems Quart. 41(2):449– 471.

Kulkarni C (2018) How to make the most of your social data. ADWEEK Online (October 26), https://www.adweek.com/ digital/how-to-make-the-most-of-your-social-data/.

Lee D, Hosanagar K, Nair HS (2018) Advertising content and consumer engagement on social media: Evidence from Facebook. Management Sci. 64(11):5105–5131.

Lehmann D, Farley J (2008) The structure of survey-based brand metrics. J. Int. Marketing 16(4):29–56.

Li X, Hitt LM (2008) Self-selection and information role of online product reviews. Inform. Systems Res. 19(4):456–474.

Liu J, Seneff S (2009) Review sentiment scoring via a parse-andparaphrase paradigm. Proc. 2009 Conf. Empirical Methods Natl. Language Processing, vol. 1 (Association for Computational Linguistics), 161–169.

Liu X, Zhang B, Susarla A, Padman R (2020) Go to YouTube and call me in the morning: Use of social media for chronic conditions. Management Inform. Systems Quart. 44(1b):257–283.

Luo X, Zhang J, Duan W (2013) Social media and <sup>fi</sup>rm equity value. Inform. Systems Res. 24(1):146–163.

Luo X, Zhang J, Gu B, Phang CW (2017) Expert blogs and genera consumer perceptions of competing brands. Management Inform. Systems Quart. 41(2):371–395.

Ma L, Sun B, Kekre S (2015) The squeaky wheel gets the grease— An empirical analysis of customer voice and <sup>fi</sup>rm intervention on Twitter. Marketing Sci. 34(5):627–645.

Moe WW, Schweidel DA (2012) Online product opinions: Incidence, evaluation, and evolution. Marketing Sci. 31(3):372–386.

Moe WW, Trusov M (2011) The value of social dynamics in online product ratings forums. J. Marketing Res. 48(3):444–456.

Paulhus DL (1991) Measurement and control of response bias. Robinson JP, Shaver PR, Wrightsman LS, eds. Measures of Personality and Social Psychological Attitudes, (Academic Press, California), 17–59.

Shin D, He S, Lee GM, Whinston AB, Centitas S, Lee K-C (2020) Enhancing social media analysis with visual data analytics: A deep learning approach. Management Inform. Systems Quart. 44(4):1459–1492.

Sarkar S, Sriram RS (2001) Bayesian models for early warning of bank failures. Management Sci. 47(11):1457–1475.

Schlosser AE (2005) Posting versus lurking: Communicating in a multiple audience context. J. Consumer Res. 32(2):260–265.

Schweidel DA, Moe WW (2014) Listening in on social media: A joint model of sentiment and venue format choice. J. Marketin Res. 51(4):387–402.

Sterling G (2019) Report: There’s almost no correlation between online and of<sup>fl</sup>ine consumer conversations. Marketing Land Online (August 28), https://marketingland.com/report-theres-almost-nocorrelation-between-online-and-of<sup>fl</sup>ine-consumer-conversations-266325.

Stephen AT, Galak J (2012) The effects of traditional and social earned media on sales: A study of a microlending marketplace. J. Marketing Res. 49(5):624–639.

Surico K (2018) How social listening voice of the customer data power unbeatable customer experience analytics. NETBASE Online (June 4) https://www.netbase.com/blog/how-sociallistening-voice-of-the-customer-data-power-unbeatable-customerexperience-analytics/.

Tirunillai S, Tellis GJ (2014) Mining marketing meaning from online chatter: Strategic brand analysis of big data using latent dirichlet allocation. J. Marketing Res. 51(4):463–479

Toubia O, Stephen AT (2013) Intrinsic vs. image-related utility in social media: Why do people contribute content to Twitter? Marketing Sci. 32(3):368–392.

Van Vlasselaer V, Eliassi-Rad T, Akoglu L, Snoeck M, Baesens B (2016) GOTCHA! Network-based fraud detection for social security fraud. Management Sci. 63(9):3090–3110.

Xie Y, Chen ZZ, Zhang K, Cheng Y, Honbo D, Agrawal A, Choudhary A (2014) MuSES: Multilingual sentiment elicitation system for social media. IEEE Intelligent Systems 29(4):34–42

Yang M, Ren Y, Adomavicius G (2019) Understanding usergenerated content and customer engagement on Facebook business pages. Inform. Systems Res. 30(3):839–855.

Zhang K, Bhattacharyya S, Ram S (2016) Large-scale network analysis for online social brand advertising. Management Inform. Systems Quart. 40(4):849–868.

Zhang L, Wang S, Liu B (2018) Deep learning for sentiment analysis. Survey (London) Preprint submitted January 24, https://arxiv. org/abs/1801.07883.
