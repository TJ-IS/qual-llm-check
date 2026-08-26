---
otero_id: 14970
otero_key: "DD3JTA7K"
title: "Can online user reviews be more helpful? Evaluating and improving ranking approaches"
authors: "Jying-Nan Wang; Jiangze Du; Ya-Ling Chiu"
year: "2020"
journal: "Information & Management"
doi: "10.1016/j.im.2020.103281"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Can online user reviews be more helpful? Evaluating and improving ranking approaches

Jying-Nan Wang<sup>a,b</sup>, Jiangze $\mathrm { D } \mathfrak { u } ^ { \mathrm { c } , \mathrm { d } , \ast }$ , Ya-Ling Chiu<sup>e,b</sup>

<sup>a</sup> College of International Finance and Trade, Zhejiang Yuexiu University of Foreign Languages, Shaoxing, China

<sup>b</sup> Digital Technology and Management Innovation Research Center, Zhejiang Yuexiu University of Foreign Languages, Shaoxing, China

<sup>c</sup> School of Finance, Jiangxi University of Finance and Economics, Nanchang, China

<sup>d</sup> Research Centre of Financial Management and Risk Prevention, Jiangxi University of Finance and Economics, Nanchang, China

<sup>e</sup> College of International Business, Zhejiang Yuexiu University of Foreign Languages, Shaoxing, China

## A R T I C L E I N F O

Keywords. Online user reviews Helpfulness Ranking Bayesian statistics

## A B S T R A C T

Given the sharply increasing number of online reviews, the selection of strategies by review-hosting firms to help users access more helpful reviews is an intriguing but insuficiently studied issue. We first propose a model to help us understand how reviews receive helpful votes (HV) and non-helpful votes. According to this model, the performances of diferent ranking approaches are compared using several simulated datasets with empirical features. In addition to three well-known ranking approaches, we develop a novel approach based on Bayesian statistics that is easy to implement in existing websites and can be combined with other content recommendation techniques to determine the prior belief in online reviews. More importantly, we suggest two simple ways to enhance existing ranking approaches. The numerical evidence demonstrates the advantages of two enhanced approaches, as indicated by higher helpful ratios and a reduced Matthew efect. These findings have important practical implications for consumers, online retailers, and review-hosting firms

## 1. Introduction

The rapid growth of the Internet has allowed consumers to express their opinions about products through quantitative ratings and/or qualitative text content. Consumers are increasingly relying on these online user reviews to make purchasing decisions, and consequently online user reviews have attracted much attention in the literature [1–3]. Formally, online user reviews can be defined as peer-generated product evaluations posted on company or third-party websites [4]. Online user reviews are regarded as a powerful marketing communication tool with a critical impact on consumers’ willingness to pay [5,6], product sales [7–13], and even the market value of a company [14–16]. As users generally have limited time or patience to read all reviews, firms that host reviews, such as IMDB or Amazon, should be committed to manage the large volume of reviews and attempt to provide consumers more useful information. To provide suggestions to review-hosting firms, this study uses numerical analysis to explore review management.

Here, a review is considered helpful only if users think it provide useful information. However, the helpfulness of reviews is a complex construct that is usually not easy to assess in practice. A common approach to evaluate review helpfulness is through users’ voting information. Specifically, the review-hosting firm can allow users to vote on each review. If a user thinks a review provides useful information, he/she will cast a HV; otherwise, he/she will cast a non-HV. Fig. 1 presents a typical example on IMDB. Users see a simple question such as “Was the above review useful to you?” and then vote by choosing one of two options: Yes or No. Thus, each review contains not only the corresponding film's rating and text content but also the number of votes and HV; e.g., IMDB provides helpfulness annotations such as “683 out of 1047 people found the following review useful.” The helpful ratio, which is calculated by dividing the number of HV by the number of total votes (TV), can be used to measure the helpfulness of reviews. Many empirical studies apply this kind of voting information as an operational evaluation criterion for review helpfulness [4,17–19]. If review-hosting firms can eficiently verify the helpfulness of reviews, they can give users more helpful recommendations and ultimately afect purchasing decisions [20]. In this study, a virtual world is constructed based on the characteristics of real online reviews. From the perspective of review-hosting firms, we attempt to evaluate and improve various ranking approaches.

Prior research has mainly focused on methods to predict whether a single new review will be judged as helpful, in terms of the number of

![](/api/attachments/DD3JTA7K/fulltext/images/0af6029894a00ff9ec2941738e966bca541148bfedda883e5e245083e79c4b6b.jpg)  
Fig. 1. A typical review on IMDB.

HV it receives, or its helpful ratio. For example, reviews with extreme ratings may receive more HV, and product type significantly moderates this respect [4,17]. Reviewer characteristics, such as expertise and reputation, are also taken into account in determining which review is helpful [21,22]. Several studies have applied text-mining techniques to analyze text content, such as number of words [4], readability [13,23,24], and sentiment [25–28]. These determinants can be used to predict the helpfulness of reviews through machine learning [29]. In short, past studies have mainly focused on examining the determinants of helpfulness or developing a model based on these determinants to forecast the helpfulness of reviews. Our work departs fundamentally from prior literature. First, rather than considering a single review, we consider the set of reviews that a user is shown. A user encounters a set of reviews, not a single review. Diferent ranking methods determine which ranked list of reviews a user sees. We address the following re search questions about the ranked list of reviews that is shown to a user: (1) How can we define and measure the performance of a reviewranking method? (2) What factors afect the performance of the ranking methods? (3) How can the existing ranking methods be improved?

To address these questions, our work introduces the following novel elements: (1) We define overall outcome measures as a function of the ranked list or set of reviews as a whole. (2) We evaluate the performance of three well-known ranking approaches and also propose a novel ranking method. (3) We hypothesize a latent “true quality” construct; helpfulness votes that are used as the ultimate measure (for a single review) in prior work, is considered in our model as an indirect measure of true quality. This novel feature allows new kinds of analysis (see next). (4) We model the entire setting, including the processes through which reviews are written, ranked for presentation to future users, and possibly read and voted upon. (5) Using the model in a simulation study, we investigate how the ranking method and other factors of the setting afect overall outcomes for users. These elements, taken together, comprise a very diferent approach to the question of review helpfulness.

Besides reporting how well the ranking approaches perform, we investigate how to improve them. Specifically, we use the simulation to show how to address the Matthew or “rich get richer" effect [30–32]. In this context, the Matthew efect refers to the phenomenon that a new review may be assigned a low rank, and never has the chance to receive any votes at all. Otherwise, it may get an undeserved “unhelpful” vote at the beginning and may never recover. Besides harming performance, these efects may discourage the review writer from writing reviews in the future, because reviewers seek social interaction [33]. Using the simulation, we trace the proportions of reviews that never get voted on, or that get an unlucky initial vote, under diferent conditions, and we propose simple adjustments to the ranking algorithms to improve performance by overcoming these rich-get-richer efects.

The contributions of our paper reflect its novel elements outlined above. On a practical level, we propose a new ranking method, and we show how various ranking methods can be easily improved. Second – this is needed to compare ranking methods – we propose outcome measures for measuring the goodness of a ranked list of reviews. A third contribution is the simulation model itself. The model is validated against a real IMDB dataset of 412 films, 92,005 reviews, and more than two million helpfulness votes. We view the model as an organizing framework for research on review behaviors. It has modeling elements for the processes of writing reviews, ranking reviews, seeing and reading reviews, voting on reviews, etc. The delineation of these distinct processes, as well as the ways they interact, organizes the field and facilitates the framing of research questions. Fourth, the model includes the hypothesized latent “true quality,” which opens new possibilities for analytical and computational investigations.

The remainder of the text is organized as follows. The next section introduces the general model of online user reviews and voting behavior. The related empirical features are also presented. In Section 3, we describe the ranking approaches and the criteria for evaluation. The numerical analysis procedure and corresponding results are shown in Section 4. In Section $^ { 5 , }$ we first explore the efects of reviews with zero and few votes. Then, we propose simple ways to improve ranking approaches. Finally, we conclude with a discussion of implications, limitations, and future research.

## 2. Model descriptions

## 2.1. About reviews

We define $\Re _ { t }$ as the set of online user reviews at time t where $t = 1$ , $2 , . . . ,$ T and $\Re _ { 0 }$ is an empty set at the initial time. Suppose the number of new reviews appearing in a time interval $I _ { t } = ( t - 1 _ { : }$ , t] follows a Poisson distribution; the probability of the arrival of a new review (adds into R ) in $I _ { t }$ is

$$
P (\mathrm{anewreviewarrivalin} I _ {t}) = \lambda_ {t} ^ {r} e ^ {- \lambda_ {t} ^ {r}},\tag{1}
$$

where $\lambda _ { t } ^ { r }$ is the average number of new reviews in $I _ { t ^ { \star } }$ . If the length of I is suficiently small, we can ignore the possibility of equivalent or more than two review arrivals. For example, if the length of I is one minute and $\lambda _ { t } ^ { r } = 0 . 0 5 ;$ there are 72 new reviews per day on average. In this case, the probability of more than one review arrival in I is only 0.12%. In addition, newer products usually receive more attention, and thus $\lambda _ { t } ^ { r }$ should decline with time intuitively. To comply with this reality, $\lambda _ { t } ^ { r }$ is given by the following function:

$$
\lambda_ {t} ^ {r} = \frac {\eta}{T} \delta e ^ {- \delta t / T}, \quad t = 1, 2, \dots , T,\tag{2}
$$

where η accounts for the expected number of reviews, which is determined by the popularity of a specific product, and δ is the decaying rate parameter.

More importantly, each review has its own specific quality, which is measured by the possibility that users regard its content as helpful. In other words, when users view a higher quality review, they have a higher likelihood of giving HV. Specifically, we denote the quality of the ith review as $q ^ { i } .$ When the ith review is viewed by a user, it represents a probabilistic experiment in which there are only two outcomes: receiving either a HV with probability $q ^ { i }$ or a non-HV with probability $1 - q ^ { i } .$ To generate each review's quality in our numerical analysis, we assume $q ^ { i }$ follows a Beta distribution for two reasons. First, a Beta distribution represents a distribution of probabilities, and $q ^ { i }$ is exactly a kind of probability. Second, as the Beta distribution is the conjugate prior to the binomial distribution, this feature is consistent with the concept of the BLB ranking approach and increases the convenience of the calculation. Formally, q<sup>i</sup> follows a Beta distribution with two shape parameters $\beta _ { 1 }$ and $\beta _ { 2 } ,$ and its probability density function is expressed as

$$
f _ {q} (x) = \frac {\Gamma (\beta_ {1} + \beta_ {2})}{\Gamma (\beta_ {1}) \Gamma (\beta_ {2})} x ^ {\beta_ {1} - 1} (1 - x) ^ {\beta_ {2} - 1}, \quad 0 \leq x \leq 1,\tag{3}
$$

where Γ(·) is the gamma function and $\beta _ { 1 } , \beta _ { 2 } > 0$ . When $\cdot \beta _ { 1 }$ is equal to $\beta _ { 2 } ,$ the Beta distribution is symmetric, and its mean is 0.5. When $\beta _ { 1 } < \beta _ { 2 }$ $\begin{array} { r } { ( \beta _ { 1 } > \beta _ { 2 } ) , } \end{array}$ the quality distribution is positively (negatively) skewed. In addition, given $\beta _ { 1 } = \beta _ { 2 } = \beta ,$ a larger $\beta$ indicates that $q ^ { i }$ has a smaller variance.<sup>1</sup>Given $\beta _ { 1 } = \beta _ { 2 } = \beta ;$ , the variance is equal to ${ \frac { 1 } { 4 ( 2 \beta + 1 ) } } .$ . Thus, a larger $\beta$ is associated with a smaller variance.Therefore, the distribution of $q ^ { i }$ is highly flexible to represent the characteristics of review quality.

In summary, if we generate $n _ { t }$ reviews until time t, the set of reviews is denoted as $\mathfrak { R } _ { t } = \{ R _ { t } ^ { 1 } , R _ { t } ^ { 2 } , . . . , R _ { t } ^ { n _ { t } } \}$ , where $R _ { t } ^ { i }$ is the ith review with quality $q ^ { i } .$ Note that $q ^ { i }$ is exogenous and time-invariant in our model, but several characteristics, $\mathbf { e . g . }$ ., the number of HV, change over time. For convenience, we denote $n _ { T } = N ,$ , which is the number of reviews at time $T ,$ and hence $\mathfrak { R } _ { T } = \{ R _ { t } ^ { 1 } , R _ { t } ^ { 2 } , . . . , R _ { T } ^ { N } \}$ at the end of the period. If the time interval $I _ { t }$ is suficiently small, according to Eqs. (1) and (2), we can find the approximate expected value of N from

$$
E (N) \simeq \eta (1 - e ^ {- \delta}).\tag{4}
$$

In practical simulations, because of the restriction of computation time, setting an extremely small length of I is inappropriate. The possibility that more than one new review may occur in a very small proportion of $I _ { t }$ is ignored in our simulation. Therefore, our average simulated number of reviews is always slightly smaller than E(N).

## 2.2. About voters

Another important element in this model is how votes, including helpful and non-HV, originate. We focus on those users who are willing to evaluate reviews and share with the public. These users are hereafter referred to as voters.² When a voter glances over a review. he/she

$$
E [ X ] = \frac {\beta_ {1}}{\beta_ {1} + \beta_ {2}}
$$

always gives it a helpful or a non-HV. We assume the number of voter arrivals in $I _ { t }$ also follows a Poisson distribution. Thus, the probability of a voter arrival in I is

$$
P \text {(a voter arrival in} I _ {t}) = \lambda_ {t} ^ {v} e ^ {- \lambda_ {t} ^ {v}},\tag{5}
$$

where $\lambda _ { t } ^ { \nu }$ is the average number of voter arrivals in I . We directly assume $\lambda _ { t } ^ { \nu } = \kappa \lambda _ { t } ^ { r }$ , which implies that more reviews always come with more voters naturally.<sup>3</sup> For instance, given $\kappa = 5 ,$ , the number of voters will be five times the number of reviews on average. Furthermore, for convenience, if a new review and a voter appear in the same $I _ { v }$ we assume that the voter can find this review immediately.

When the number of reviews is large, it is impossible for voters to view all online reviews. In reality, if reviews are sorted by time (with the most recent at the top), more recent reviews are reached by voters more easily. Therefore, the default ranking approach for reviews, e.g., most helpful first ranking (MHF) or chronological ranking, indeed affects the probability of reviews being viewed. We denote Rank(R <sup>i</sup>) as the rank of $R _ { t } ^ { i }$ in $\Re _ { t }$ conditional on a specific ranking approach. For example, based on the MHF ranking approach, if $R _ { t } ^ { i }$ has the greatest number of HV among $\Re _ { t } ,$ , then Rank(R <sup>i</sup>) is equal to one. In particular, the probability of $R _ { t } ^ { i }$ being viewed declines with Rank(R <sup>i</sup>). Hence, we assume that the probability of $R _ { t } ^ { i }$ being viewed is given by the following reverse Sigmoid function<sup>4</sup> :

$$
P (R _ {t} ^ {i} \text {being found}) = (1 + e ^ {\frac {\mathrm{Rank} (R _ {t} ^ {i}) - m}{\varphi}}) ^ {- 1}\tag{6}
$$

where the shape parameters m, $\varphi > 0$ . If Rank(R <sup>i</sup>) is smaller (larger) than $m ,$ the probability of $R _ { t } ^ { i }$ being found is larger (smaller) than 0.5. In addition, φ controls the changes in the declining rate of probability. For instance, given $m = 2 0$ and $\varphi = 1 0$ , if Rank(R <sup>i</sup>) = 1, 10, 20, and 30, the probabilities of $R _ { t } ^ { i }$ being viewed are 0.87, 0.73, 0.5, and 0.27, respectively. Fig. 2 shows the changes in probability with $m = 2 0$ and $\varphi = 5 ,$ 10, and 20.

Both the numbers of total TV and HV are important indicators for measuring review quality. For each $R _ { t } ^ { i } ,$ , the corresponding $\mathrm { T V } _ { t } ^ { i }$ and HV<sup>i</sup> are generated in our model. Specifically, initially, $\mathrm { T V } _ { 0 } ^ { i } = 0 ;$ , and $\mathrm { H V } _ { 0 } ^ { i } = 0$ . Then, we let $\mathrm { T V } _ { t } ^ { i } = \mathrm { T V } _ { t - 1 } ^ { i } + Y _ { t } ^ { i }$ and $\mathrm { H } \mathbf { V } _ { t } ^ { i } = \mathrm { H } \mathbf { V } _ { t - 1 } ^ { i } + W _ { t } ^ { i } , t = 1 ;$ $2 , . . . , T ,$ , where ${ \boldsymbol { Y } } _ { t } ^ { i } ,$ and $\boldsymbol { W } _ { t } ^ { i }$ are random variables with Bernoulli distributions. The probability of $Y _ { t } ^ { i } = 1$ is equal to the probability ${ \sf o f } ^ { \mathrm { ~ \tiny ~ \omega ~ } } R _ { t } ^ { i }$ being viewed” conditional on “voter arrivals in $I _ { t ^ { \star } } \stackrel { \triangledown } { ^ { \wedge } }$ Suppose the above two events are independent; according to Eqs. (5) and (6), the probability of $Y _ { t } ^ { i } = 1$ is

$$
P (Y _ {t} ^ {i} = 1) = \frac {\lambda_ {t} ^ {\nu} e ^ {- \lambda_ {t} ^ {\nu}}}{1 + e ^ {\frac {\mathrm{Rank} (R _ {t} ^ {i}) - m}{\varphi}}}.\tag{7}
$$

We then investigate the probability of $W _ { t } ^ { i } = 1 _ { : }$ , which is equal to the probability of “the voter chooses a helpful vote” conditional on $Y _ { t } ^ { i } = 1$ Recall that the probability of voters choosing helpfulness of $R _ { t } ^ { i }$ depends on its quality $q ^ { i } .$ Thus, given the independence assumption,<sup>5</sup> intuitively we can find

![](/api/attachments/DD3JTA7K/fulltext/images/cf861feeea3c862fff4b96c2a32b9952dffda623daff4403e9cb95f40c7e271e.jpg)  
Fig. 2. Review ranks and the probability of being viewed.

$$
P (W _ {t} ^ {i} = 1) = q ^ {i} \times P (Y _ {t} ^ {i} = 1),\tag{8}
$$

where $q ^ { i }$ is determined by Eq. (3). Although we could directly estimate the expected W <sup>i</sup> and $\boldsymbol { Y } _ { t } ^ { i }$ at time t using Eqs. (7) and (8), it is not an easy task to calculate the expected TV<sup>i</sup> and HV<sup>i</sup> due to the dynamic value of Rank( $[ R _ { t } ^ { i } )$ . In other words, diferent ranking approaches afect TV<sup>i</sup> and $\mathrm { H V } _ { t } ^ { i }$ significantly. In Section $^ { 3 , }$ we will introduce not only several well known approaches but also the new Bayesian ranking approach.

To further understand all parts of the mentioned model, we provide an example to demonstrate it. As shown in Fig. 3, suppose one product, such as a cell phone, appears on a certain online platform, people can then start writing reviews depending on their user experience and can also vote on these reviews. In particular, reviews and voters appear randomly at diferent times according to Eqs. (1) and (5), respectively. Fig. 3 indicates that there are 5 reviews of this product, with 22 voters providing relevant votes on the reviews. Moreover, each review has a specific quality, determined by Eq. (3), which is always time-invariant and unobservable. Higher quality implies that a review is more likely to be viewed as helpful by voters. The key aspect of this model is how the ranking approach afects the values of TV and HV for each review. Clearly, TV or HV is zero for a new review. Over time, voters may view the review and decide whether to give it a HV. Accordingly, the numbers of votes (TV and HV) are never greater than the total number of voters, because a voter only votes on reviews he/she sees and whether he/she sees a review depends on its rank. We assume a voter appears in a specific time interval as indicated in Fig. 3. At the beginning of this interval, the initial review set includes 5 reviews with corresponding TV and HV; for instance, for review 1, TV = 15 and HV = 12. These reviews can then be sorted using the most recent first ranking approach (MRF)- or MHF-ranking approach. It should be noted that TV of a review increases by one only when it is viewed by the voter, so this voter does not read and vote on all reviews in both cases. Based on Eq. (6), a review with a smaller rank is more likely to be viewed by this voter. In addition, according to Eq. (8), a viewed review with better quality is more likely to receive a HV. Therefore, the two ranking approaches result in diferent values of TV and HV for these reviews. In summary, the above steps are repeated whenever a voter appears. Diferent ranking approaches will lead to diferent results for TV and HV for each review.

## 2.3. Empirical features of reviews from IMDB

We provide some empirical evidence to support the rationality of our model. Massive reviews are collected from IMDB, one of the most popular online film communities in the world. The top 100 box ofice films in the US over the period 2010–2015 are considered. From September 27, 2016, to September 30, 2016, we applied web crawler technology to collect data related to each film's reviews posted within 8 weeks after the release date. If a film had less than 50 reviews, all data for this film were excluded. Finally, 412 films with 92,005 reviews remained. with a total of 2.318.475 votes and 1.153.538 HV Table 1presents the descriptive statistics for our sample. On average, each film has 233 reviews for which 5627 voters provide 2800 HV. We are also aware that when a voter views a review, he/she probably has a 50% chance of reporting it as helpful.

The IMDB data can be used to illustrate that the model assumptions do not violate the actual situation. However, due to the limitations of empirical data availability, we can only obtain the voting information of each review on the data collection date. This means that we have no way to verify when voters appear or how they vote. Therefore, we can only apply the IMDB data to investigate two characteristics of the review: the number of reviews over time and the review's quality distribution. First, because newer products receive more attention, the number of reviews should decline with time, and this phenomenon is modeled by Eqs. (1) and (2). Fig. 4 shows the number of total reviews in the first 8 weeks. The declining trend is indeed obvious and is consistent with our model assumptions. Second, we explore the review's quality distribution. As it is impossible to obtain the true quality, we use the review's helpful ratio as a proxy of quality. To avoid small sample biases, we retain reviews with 30 votes or more to measure their quality. Consequently, 16,222 reviews are used to estimate quality, and the related histogram is shown in Fig. 5. The histogram indicates that the quality exhibits a roughly symmetric bell-shaped distribution, and to be consistent with this empirical feature, we always se $\beta _ { 1 } = \beta _ { 2 }$ in Eq. (3). In Section 4.1, according to the above model setups, we show that the simulated data present the same patterns as in Figs. 4 and 5.

![](/api/attachments/DD3JTA7K/fulltext/images/ebb142ffc2a058e04a6b22e4ab1d877f4c6c33e73063597a4beca8c54640cd63.jpg)  
Fig. 3. An example for illustrating the model.  
Table 1

Basic descriptions in IMDB reviews.

<table><tr><td></td><td>Mean</td><td>Standard deviation</td><td>Maximum</td><td>Minimum</td></tr><tr><td>Total reviews per film</td><td>223.313</td><td>258.606</td><td>2973.000</td><td>50.000</td></tr><tr><td>Total votes per film</td><td>5627.367</td><td>10,543.860</td><td>168,517.000</td><td>317.000</td></tr><tr><td>Total helpful votes per film</td><td>2799.850</td><td>5326.584</td><td>88,153.000</td><td>116.000</td></tr><tr><td>Total helpful votes/total votes</td><td>0.519</td><td>0.064</td><td>0.776</td><td>0.256</td></tr></table>

investigate whether diferent ranking approaches can help reviewhosting firms to detect helpful reviews using only TV and HV. Even if MRF does not perform as well in finding helpful reviews as ranking approaches that apply voting information, it is still the most common ranking approach in online communities. Therefore, we retain its related outcomes in this paper for the reader's reference. In addition to MRF, we intuitively consider three other ranking approaches: the MHF, the best helpful ratio first ranking (HRF),<sup>6</sup> and the Bayesian lower bound ranking (BLB). Specifically, we first evaluate the ranking score of $R _ { t } ^ { i } ,$ and then Rank(R <sup>i</sup>) is determined by the largest first order of scores.

![](/api/attachments/DD3JTA7K/fulltext/images/1c956d6ad4d98fa73d1d7a1350ccdb22f9f5832706375057f05232532e8fa84d.jpg)  
Fig. 4. Empirical feature: the frequency of reviews appear.

## 3. Ranking approaches and evaluations

## 3.1. Three simple ranking approaches

Review-hosting firms usually adopt several ranking approaches for sorting reviews. In addition to the MRF, which is always one of the options, they may provide some mystic ranking approaches based on users’ historical behavior or review content analysis. In this study, we $\zeta _ { t } ^ { i } ( \cdot )$ represents the ranking score from a certain approach. The ranking scores of MRF and MHF are defined as

![](/api/attachments/DD3JTA7K/fulltext/images/8ccd266e845ce4c15489c1bc506fb9cfa34e1ada16fb76270ac4ade4330ee152.jpg)  
Fig. 5. Empirical feature: the distribution of reviews’ quality.

$$
\zeta_ {t} ^ {i} (\mathrm{MRF}) = \text { the   posted   time   of   the   ith   review; }\tag{9}
$$

$$
\zeta_ {t} ^ {i} (\mathrm{MHF}) = \mathrm{HV} _ {t} ^ {i}.\tag{10}
$$

As it is impossible to observe the true review quality, the helpful ratio, which is calculated by $\mathrm { H V } _ { t } ^ { i } / \mathrm { T V } _ { t } ^ { i }$ , can be intuitively considered as a good proxy variable for review quality. Accordingly, if the websitehosting manager sorts reviews based on relevant helpful ratios, reviews with higher quality could be listed in a more conspicuous place on the website. However, at the moment a review appears, the total number of votes is naturally zero, which leads to a problem in calculation. To compensate for this defect, we can set a default value for the initial helpful ratio. Formally, the ranking score of HRF can be defined as

$$
\zeta_ {t} ^ {i} (\mathrm{HRF}) = \left\{ \begin{array}{l l} \mathrm{HV} _ {t} ^ {i} / \mathrm{TV} _ {t} ^ {i}, & \text {if TV_{t} ^{i} >0}, \\ \xi , & \text {if TV_{t} ^{i} = 0}, \end{array} \right.\tag{11}
$$

where $\xi$ is the default value of the helpful ratio. In general, we set the quality of a review that has not received any votes as $0 . 5 , \mathrm { i . e . , } \xi = 0 . 5 .$ We will further explore the influence of diferent default values on HRF performance in Section 5.2.

## 3.2. Bayesian lower bound ranking approach

We follow the concept of Bayesian statistics to propose BLB, which updates the beliefs of people using evidence from new data. The main motivation of BLB is that if review-hosting firms know the true quality of each review, they will be able to place higher quality reviews where they can be easily seen. However, the true quality is never observable. In practice, review-hosting firms have their own prior or subjective beliefs about the quality of reviews and can continue to observe users’ behavior to update these beliefs. In our approach, we assume that before the firm evaluates a review's quality, the prior belief of $q ^ { i }$ is identical and follows a symmetric Beta distribution. Note that the prior belief distribution does not need to be the same as in Eq. (3). To clearly distinguish these two distributions, we define the probability density function of quality prior belief as follows:

$$
B (x; \beta_ {H}, \beta_ {N}) = \frac {\Gamma (\beta_ {H} + \beta_ {N})}{\Gamma (\beta_ {H}) \Gamma (\beta_ {N})} x ^ {\beta_ {H} - 1} (1 - x) ^ {\beta_ {N} - 1}, \quad 0 \leq x \leq 1,\tag{12}
$$

where Γ(·) is a gamma function and the shape parameters $\beta _ { H } = \beta _ { N } > 0$ imply that the expected quality is 0.5.

The value of the shape parameters indicates that a review-hosting firm could have diferent levels of confidence about review quality. In ${ \mathrm { F i g . ~ } } 6 ,$ for example, if the prior belief is $B ( x ; 2 0 , 2 0 )$ , the company ha greater confidence in its prior beliefs than if the prior belief is B(x;3, 3). Greater confidence means the probability that the firm will use new information to adjust the level of belief is relatively small. Thus, the prior belief is more stable if $\beta _ { H }$ and $\beta _ { N }$ have larger values. We then investigate how firms update their beliefs. Suppose the prior belief of reviews is $B ( x ; \beta _ { H } , \beta _ { N } )$ and people have observed $\mathrm { H V } _ { t } ^ { i }$ and $\mathsf { \bar { \tau } } _ { \mathrm { T V } _ { t } ^ { i } }$ at time t. The posterior belief $B _ { t } ^ { i } ( x ; \beta _ { H } ^ { * } , \beta _ { N } ^ { * } )$ is defined as

$$
B _ {t} ^ {i} (x; \beta_ {H} ^ {*}, \beta_ {N} ^ {*}) = B (x; \beta_ {H} + \mathrm{HV} _ {t} ^ {i}, \beta_ {N} + \mathrm{NV} _ {t} ^ {i}),\tag{13}
$$

where $\mathbf { N V } _ { t } ^ { i } = \mathbf { T V } _ { t } ^ { i } - \mathbf { H V } _ { t } ^ { i }$ . We use the above example to show how helpful and non-HV update the prior belief. Given a more stable prior belief distribution $( \beta _ { H } = \beta _ { N } = 2 0 )$ , if there are more HV than non-HV $( \mathrm { H V } _ { t } ^ { i } = 1 0 , \mathrm { N V } _ { t } ^ { i } = 5 )$ , the posterior belief becomes B x( ; 30, 25)<sup>i</sup> ; however, if the number of non-HV is greater $( \mathrm { H V } _ { t } ^ { i } = 5 , \mathrm { N V } _ { t } ^ { i } = 1 0 )$ , the posterior belief becomes $B _ { t } ^ { i } ( x ; 2 5 , 3 0 )$ . The changes in beliefs are shown in $\mathrm { F i g . } 7 ( \mathbf { a } )$ and (b). Similar examples of a less stable prior belief distribution $( \beta _ { H } = \beta _ { N } = 3 )$ are presented in Fig. 7 (c) and (d). When $H V ^ { i }$ is larger, firms believe that the quality of $R _ { t } ^ { i }$ is higher. If the prior belief is less stable, the same number of votes induces a greater change in the posterior belief.

Based on the posterior belief distribution $B _ { t } ^ { i } ( x ; \beta _ { H } ^ { * } , \beta _ { N } ^ { * } )$ , BLB adapts a conservative critical value to determine Rank $( R _ { t } ^ { i } )$ . Formally, we define

$$
\zeta_ {t} ^ {i} (\mathrm{BLB}) = Q (B _ {t} ^ {i} (x; \beta_ {H} ^ {*}, \beta_ {N} ^ {*}), 0. 0 5),\tag{14}
$$

where $Q ( B _ { t } ^ { i } ( x ; \beta _ { H } ^ { * } , \beta _ { N } ^ { * } ) , 0 . 0 5 )$ is the 5% quantile of the posterior belief distribution. The value of $\zeta _ { t } ^ { i } ( \mathrm { B L B } )$ is afected by the mean of $B _ { t } ^ { i } ( x ; \beta _ { H } ^ { * } , \beta _ { N } ^ { * } )$ and its variance. The first efect makes $\zeta _ { t } ^ { i } ( \mathrm { B L B } )$ larger (smaller) if $\mathrm { H V } _ { t } ^ { i }$ is larger (smaller) than $\mathrm { N V } _ { t } ^ { i }$ . The second efect shows that more votes can reduce the uncertainty of belief; consequently, less variance induces higher $\zeta _ { t } ^ { i } ( \mathrm { B L B } )$ . For instance, in Fig. $^ { 7 , }$ we also show the changes in $\zeta _ { t } ^ { i } ( \mathrm { B L B } )$ in each case. In cases (a) and (c), both efects make $\zeta _ { t } ^ { i } ( \mathrm { B L B } )$ larger. Nevertheless, in cases (b) and (c), as the mean and variance efects are opposite, the directions of change in (BLB)<sup>i</sup> are not consistent. In summary, BLB, adjusts the small sample bias when

$$
B _ {t} ^ {i} (x; \beta_ {H} ^ {*}, \beta_ {N} ^ {*}) = B (x; \beta_ {H} + \gamma \mathrm{HV} _ {t} ^ {i}, \beta_ {N} + \gamma \mathrm{NV} _ {t} ^ {i}),
$$

![](/api/attachments/DD3JTA7K/fulltext/images/9fde121d294c84401078f04bdf418afd6e02e363f29ee6f2ec0c65d4e8697f99.jpg)  
Fig. 6. Prior beliefs of review's quality.

measuring review quality. In addition, BLB, incorporates firms’ prior beliefs into the model, which makes the sorting process more realistic and flexible.

## 3.3. Criteria for evaluation

Criteria are needed for measuring which of the four ranking approaches has better performance from a certain perspective. For simplicity, in this paper, we only evaluate the performance of ranking approaches at the end of period T. The first criterion is the Aggregated Helpful Ratio (AHR), which is calculated by

(a) Updating more stable beliefs with HV=10 and NV=5  
![](/api/attachments/DD3JTA7K/fulltext/images/af1e98b4f7bafd0f391123155417f74056c7bf182cd1f9f601d339bce6781ab4.jpg)

(c) Updating less stable beliefs with HV=10 and NV=5  
![](/api/attachments/DD3JTA7K/fulltext/images/4b75424466a6b1efa15848eeb73a2ff0ed51a1825aa2f7aa85f0a5634747fb57.jpg)

$$
\mathrm{AHR} = \frac {\sum_ {i = 1} ^ {N} \mathrm{HV} _ {T} ^ {i}}{\sum_ {i = 1} ^ {N} \mathrm{TV} _ {T} ^ {i}}.\tag{15}
$$

AHR provides an intuitive means of estimating the percentage of voters who think the reviews are helpful.

To investigate another criterion, we first define the individual helpful ratio HR<sup>i</sup> , i.e.,

$$
\mathrm{HR} _ {t} ^ {i} = \frac {\mathrm{HV} _ {t} ^ {i}}{\mathrm{TV} _ {t} ^ {i}},\tag{16}
$$

where TV<sup>i</sup> should be larger than zero. The second criterion uses the correlation of $\mathrm { T V } _ { T } ^ { i }$ with $\mathrm { H R } _ { T } ^ { i }$ , denoted ρ. If the action of a review-hosting firm in sorting or recommending reviews is correct, ρ should be positive, implying that higher quality reviews are seen more frequently. The IMDB dataset introduced in Section 2.3 provides some empirical evi dence to support this point, as ρ for 90,753 reviews with positive TV is 0.225 (p-value = 0). We further use Pearson's correlation test for 412 films and find that approximately 93% have significantly positive correlations (p-value < 0.01).

(b) Updating more stable beliefs with HV=5 and NV=10  
![](/api/attachments/DD3JTA7K/fulltext/images/802dcb67145baaa10e0b70035d7896a5cd2eddb6af6fae299c57b2dadc2d1ffe.jpg)

(d) Updating less stable beliefs with HV=5 and NV=10  
![](/api/attachments/DD3JTA7K/fulltext/images/b508a9430072a9fc3a4bcab88410c5de4e8686424eace17472193ee15382be92.jpg)  
Fig. 7. Update the prior beliefs in four cases.

Table 2  
Examples about criteria for evaluation.

<table><tr><td rowspan="2">Reviews</td><td rowspan="2">Quality</td><td colspan="2">Case 1</td><td colspan="2">Case 2</td></tr><tr><td>TV</td><td>HV</td><td>TV</td><td>HV</td></tr><tr><td>1</td><td>0.8</td><td>30</td><td>24</td><td>50</td><td>40</td></tr><tr><td>2</td><td>0.6</td><td>20</td><td>12</td><td>5</td><td>3</td></tr><tr><td>3</td><td>0.5</td><td>20</td><td>10</td><td>10</td><td>5</td></tr><tr><td>4</td><td>0.4</td><td>20</td><td>8</td><td>5</td><td>2</td></tr><tr><td>5</td><td>0.2</td><td>10</td><td>2</td><td>30</td><td>6</td></tr></table>

AHR and $\boldsymbol { \rho }$ are both reasonable criteria but have some diferences. Suppose two diferent ranking approaches are adopted for 5 reviews, the voting results are presented in Table 2. In this example, it is fortuitous that each HR<sup>i</sup> is equal to the corresponding true quality. In both cases, AHR is equal to 0.56, but ρ is 0.949 and 0.341 for cases 1 and 2, respectively. Given the same AHR, a lower $\boldsymbol { \rho }$ indicates that more relatively high-quality reviews are not taken seriously; in addition, more relatively low-quality reviews are read too many times. However, in reality, we can only use HR as a proxy of true quality, but the small sample bias will cause HR to be far from the true value. Unless the number of samples used in the calculation of HR is suficiently large, the comparison of $\rho$ is relatively meaningless. Thus, we suggest calculating both criteria but employing the value of AHR as the main cri terion.<sup>8</sup>

As early posted reviews have a greater opportunity to receive more votes, inappropriate ranking approaches may result in later reviews going unseen. Some better reviews are always recommended by the system, and most other reviews are not seen. A user whose reviews always receive no feedback may feel discouraged and disinterested in sharing on the platform. However, AHR and $\rho$ do not take the efects of zero-vote reviews into account. Because we want to see how to help the ranking algorithms to overcome/avoid the Matthew efect, which is partly driven by reviews that get zero votes, we also define and measure the proportion of reviews with zero votes (PRZ). More importantly, using a simulation, we will be comparing diferent ranking approaches according to these outcome measures, AHR and $\rho .$ One might think that obviously the HRF, which ranks according to each review's HV/TV, will be the best method when judged according to AHR, which is defined as the average HV/TV. The benefit of the simulation study is that it will show the conditions under which AHR enjoys this advantage, and also how and when we can improve HRF (and other methods) to overcome rich-get-richer efects and perform even better.

## 4. Numerical analysis

In this section, we first illustrate how to conduct related simulation according to the model descriptions in Section 2. Then we can compare ranking approaches, shed light on the factors that make each ranking approach perform well or not, and understand how the ranking approaches can be improved.

<sup>8</sup> The true quality for each review is not observable in practical applications, so this study uses AHR and $\rho ,$ which are not directly related to $q ^ { i } .$ However, in the simulation experiment, we can obtain the true quality level of each review. Accordingly, we also provide two similar criteria using true quality for re ference. The corresponding results are shown in Appendix A.2.

## 4.1. Simulation procedures and characteristics

From t = 1 to T, we can simulate whether a new review appears by using Eq. ((1)), whether a voter arrives by using Eq. ((5)), and the numbers of TV and HV for the ith review by using Eqs. (7) and (8) under diferent ranking approaches. The detailed procedure is shown in Algorithm 1. We denote the experiment ReSim $( S _ { j }$ , ranking approach) to indicate the use of diferent scenarios, where $S _ { j } = \{ T , \eta , \delta , \beta _ { 1 } , \beta _ { 2 } , \kappa , m ,$ $\varphi \}$ . Table 3 shows the meaning of each simulation parameter and which equation uses it. Because several parameters involved in the model can change the characteristics of reviews and voters; we consider various parameter sets to demonstrate certain real-world scenarios. The different scenarios also help us to confirm the robustness of relevant findings. In Table $^ { 4 , }$ , we organize eight $S _ { j }$ to investigate the perfor mances of the diferent ranking approaches. For example, ReSim $( S _ { 1 } ,$ MHF) indicates the use of MHF and the model parameters given by $S _ { 1 }$ Furthermore, we must explain the meaning of $T = 8 0 , 6 4 0$ . The sample period is focused on the first 8 weeks after the release of a new film (product). To generate simulated data, we convert the 8 weeks of continuous time to discrete times with a length of one minute, i.e., $T = 8 \times 7 \times 2 4 \times 6 0$

Table 4 warrants further discussion. As it is usually not easy to find a real-world scenario that completely meets a certain case, we regard $S _ { 1 }$ as the benchmark and take the film industry as our example to explain the practical meaning of diferent scenarios. First, in $S _ { 1 } { } _ { i }$ , we assume that most reviews or votes appear within 8 weeks of the release of a film. so we only observe the sample during the first 8 weeks. In scenario $S _ { 2 } ,$ , the total number of reviews or votes is almost the same as in $s _ { \mathrm { 1 } } ,$ but the time that they appear is mainly concentrated in the first 4 weeks. This means that the film received widespread attention from the market in the short term, but the craze quickly receded. For example, some mo vies rely on high marketing budgets to increase the box ofice at the beginning of release. but if the film's reputation is not good, the box ofice will decline rapidly. In general, the box ofice is positively correlated with the number of reviews [34]. In $S _ { 3 } ,$ the smaller $\eta$ reflects relatively fewer reviews or voters for this film compared to $S _ { 1 }$ In other words, this film is less popular than our benchmark. In addition, we change the decline rate of the average number of new reviews in $S _ { 4 } .$ Fig. 8 displays the number of new reviews according to ReSim $( S _ { 1 } ,$ , MRF) and ReSim(S₄. MRF) in each week. The declining trend is similar to that in Fig. 4. Moreover, a larger δ implies that more reviews appear in the first few weeks, but the rate of decline is very fast. Therefore, thi scenario also implies that the film's box ofice decline rate is faster than in $S _ { 1 }$ In $S _ { 5 } ,$ the distribution of review quality is controlled by the parameters of the Beta distribution. When $\beta _ { 1 }$ and $\beta _ { 2 }$ are larger, the distribution of review quality is more concentrated. In Fig. 9, we verify this property based on ReSim $( S _ { 1 }$ , MRF) and ReSim $( S _ { 5 } ,$ , MRF). In the context of the film industry. for instance. if the content of a film is relatively easy to understand, the diference in the quality of its reviews may be smaller than that of some dificult films. In the next scenario, ${ \cal S } _ { 6 } ,$ because our model assumes that the ratio of the number of voters to the number of reviews is a constant by Eq. (5). the number of voters dou. bles compared to $S _ { 1 }$ when we change κ from 5 to 10. Finally, both $S _ { 7 }$ and $S _ { 8 }$ change the review's probability of being viewed as shown in Fig. 2. Specifically, a smaller m implies that voters are less willing to take the time to view more reviews. In addition. the probability that a review is seen by a voter will always decrease as the review rank in creases, while a greater $\varphi$ indicates that the rate of decline is slower. Overall, eight diferent scenarios are considered in our discussions, and we investigate the performance of each of the diferent ranking ap proaches. In the following numerical analysis, to ensure a fair evalua tion, each case is repeated 1000 times, and the mean and standard deviation of every evaluated criterion are reported.

Before investigating the performance of the ranking approaches, we first examine some characteristics of our simulations. As shown in Table $^ { 5 , }$ the expected number of reviews can be estimated by Eq. (4).

Table 3  
Summary of simulation parameters.

<table><tr><td>Parameters</td><td>Meaning</td><td>Which equations use it</td></tr><tr><td>T</td><td>The number of periods in each simulation</td><td>(1), (2), (4)</td></tr><tr><td>η</td><td>The parameter of the expected number of reviews</td><td>(1), (2), (4)</td></tr><tr><td>δ</td><td>The decaying rate of new reviews appearing</td><td>(1), (2), (4)</td></tr><tr><td>β1, β2</td><td>The shape parameters of the quality&#x27;s probability density function</td><td>(3), (8)</td></tr><tr><td>κ</td><td>A parameter equals to the expected number of voter arrivals divided by the expected number of reviews</td><td>(5), (7), (8)</td></tr><tr><td>m, φ</td><td>The shape parameters of the probability of reviews being viewed</td><td>(6), (7), (8)</td></tr></table>

Table 4  
Parameters settings in eight scenarios.

<table><tr><td></td><td>T</td><td> $\eta$ </td><td> $\delta$ </td><td> $\beta_1$ </td><td> $\beta_2$ </td><td> $\kappa$ </td><td>m</td><td> $\varphi$ </td></tr><tr><td> $S_1$ </td><td>80,640</td><td>500</td><td>2</td><td>3</td><td>3</td><td>5</td><td>20</td><td>5</td></tr><tr><td> $S_2$ </td><td>40,320</td><td>500</td><td>2</td><td>3</td><td>3</td><td>5</td><td>20</td><td>5</td></tr><tr><td> $S_3$ </td><td>80,640</td><td>300</td><td>2</td><td>3</td><td>3</td><td>5</td><td>20</td><td>5</td></tr><tr><td> $S_4$ </td><td>80,640</td><td>500</td><td>5</td><td>3</td><td>3</td><td>5</td><td>20</td><td>5</td></tr><tr><td> $S_5$ </td><td>80,640</td><td>500</td><td>2</td><td>10</td><td>10</td><td>5</td><td>20</td><td>5</td></tr><tr><td> $S_6$ </td><td>80,640</td><td>500</td><td>2</td><td>3</td><td>3</td><td>10</td><td>20</td><td>5</td></tr><tr><td> $S_7$ </td><td>80,640</td><td>500</td><td>2</td><td>3</td><td>3</td><td>5</td><td>10</td><td>5</td></tr><tr><td> $S_8$ </td><td>80,640</td><td>500</td><td>2</td><td>3</td><td>3</td><td>5</td><td>20</td><td>20</td></tr></table>

The bold numbers in the table indicate that the parameters are diferent from those of other scenarios.

instance, given $m = 2 0 , \varphi = 5 ,$ , and $N = 4 3 0 { \mathrm { ; } }$ , a voter would browse an average of 19.6 reviews. The simulated ratio of total voters and TTV in ReSim(S , MRF), i.e., 39,750/2081 = 19.1, is smaller than 19.6 because there are not enough reviews in the beginning. As discussed in Eq. (6), m and φ control the changes in the declining rate of the probability of being found. ReSim(S , MRF) and ReSim $( S _ { 8 } ,$ MRF) display diferent declining rates and indicate that a voter browses an average of 10.0 and 24.3 reviews, respectively. A recent study by Brightlocal.com [35] suggests that approximately 10% of consumers spend time reading more than 10 reviews (vs. 13% in 2015). Accordingly, in this study, voters are considered to be usually willing to spend more time to read more reviews.

![](/api/attachments/DD3JTA7K/fulltext/images/f65645cec380658dca59a819e5946e93fadfb31a9cafc1040aaad4eb54c72f52.jpg)  
Fig. 8. Simulated data feature: the frequency of reviews appear.

For example, given $\eta = 5 0 0$ and $\delta = 2 ,$ , the expected number of reviews is approximately 432. However, because the maximum number of re views in $I _ { t }$ is one, our simulated expected outcome represents a slight underestimate. For ReSim(S , MRF) and ${ \mathrm { R e S i m } } ( S _ { 2 } , { \mathrm { M R F } } )$ , the mean of N is 429.8 and 426 $^ { . 5 , }$ respectively. As the latter has a higher possibility of producing more than one review in $I _ { t } ,$ it would miss more reviews than the former. This numerical bias can be overcome by decreasing the length of $I _ { t s } \ \in . g .$ ., changing the one-minute length to a one-second length, but this will greatly increase the computation time. As the above bias does not afect the evaluation of the ranking approaches, we do not change the length of $I _ { t } .$ The third column represents the number of voters and is almost κ times N. Similarly, some voters are ignored because of the simulated bias. The fourth column in Table 5 reports the means and standard deviations of TTV, which is the summation of TV for all reviews at time T. According to $\operatorname { E q . } \left( 6 \right)$ , if there are N reviews, the $\begin{array} { r } { \sum _ { j = 1 } ^ { N } \left( 1 + e ^ { \frac { j - m } { \varphi } } \right) ^ { - } } \end{array}$ 1 expected number of found reviews is equal to . For

## 4.2. Numerical results

The simulation is run from two diferent perspectives. First, we use the simulation to see how AHR and ρ are afected by various features of the setting, regardless of the ranking method. Then, we use the simulation to gain insights into how the diferent ranking methods behave.

When we focus on how AHR or PRZ depends on the scenario settings, there are three interesting findings based on the results in Table 5. First, comparing $S _ { 1 }$ and $S _ { 3 }$ shows that when the number of reviews is smaller, AHR decreases. The reason is that there is a smaller pool of good reviews. Second, comparing $S _ { 1 }$ and $S _ { 5 }$ shows that when the distribution of review quality is more concentrated. both AHR and PRZ will decrease. The reason is that the helpfulness votes are a stochastic function of review quality, and a smaller variance reduces the ability of helpfulness votes to separate better reviews from worse. Third, comparing $S _ { 1 }$ and $S _ { 8 }$ shows that when voters are more willing to read more comments, the extent of PRZ reduction is highly obvious. However, a smaller PRZ indicates that more high-quality articles can be found, which helps to improve AHR. By contrast, when people read more reviews, it becomes easier to read some poor-quality reviews, which causes AHR to decline. Accordingly, the rise or fall of AHR depends on the strength of these two efects. In the cases in Table 5, AHR is slightly reduced.

![](/api/attachments/DD3JTA7K/fulltext/images/1b03ba247d761c390ef2214f06aedc08d1df2523dafb903d208e7b0e08775258.jpg)  
Fig. 9. Simulated data feature: the distribution of reviews’ quality.

Compared to the benchmark $s _ { 1 } ,$ only $S _ { 3 }$ (small number of reviews), $S _ { 5 }$ (small diference in review quality), and $S _ { 8 }$ (more browsed reviews per voter) result in diferent ranking performances. Therefore, in the following discussions, we only retain these four scenarios. We also add BLB in the discussions. BLB is based on quality prior belief as shown in Eq. (12) and updates the belief according to $\operatorname { E q . }$ (14). We first need to determine the parameters $\beta _ { H }$ and $\beta _ { N } .$ Suppose there is no further information about review quality; $\beta _ { H } = \beta _ { N }$ is reasonable to maintain a mean quality of 0.5. In addition, a larger $\beta _ { H } ( \beta _ { N } )$ indicates that the prior belief is more confident or that new information, TV<sup>i</sup> and $\mathrm { N V } _ { t } ^ { i } ,$ is less influential. In this study, four parameter settings, i.e., 3, 10, 20, and 50, are denoted as BLB3, BLB10, BLB20, and BLB50, respectively, and the corresponding results are reported in Table 6. These results also support previous findings.

From the other perspective, we focus on comparing the performance of diferent ranking approaches. MRF undoubtedly has the worst performance in terms of AHR or ρ. Specifically, ether AHR = 0.5 or ρ = 0 indicates that MRF does not allow voters to more easily find helpful reviews. However, PRZ = 0 indicates that almost no review has zero votes. In other words, users will be motivated to post because they know that their reviews have been read by someone. For MHF, the average AHR is approximately 0.58, except for ReSim(S , MHF). Because MHF allows early published reviews to be viewed more easily, the HV of these reviews will naturally be higher, regardless of the quality of the reviews. When enough reviews have many votes, they will always be in front [31], and new reviews will be dificult to find. This results in a large PRZ,<sup>9</sup> highlighting a disadvantage of MHF because users may lose the motivation to continue to share their thoughts on the website. In cases of HRF with $\xi = 0 . 5 ,$ , we find that both AHR and $\boldsymbol { \rho }$ have obviously improved in all scenarios compared to MRF or MHF. Moreover, the values of PRZ are also reduced. Finally, we investigate the performance of BLB with various $\beta _ { H }$ and $\beta _ { N }$ in Table 6. In terms of AHR and PRZ, BLB is much better than MRF and MHF but is slightly worse than HRF. In terms of $\rho ,$ BLB is the best of all ranking approaches. Incidentally, if new information is less influential, e.g., $\beta _ { H } = \beta _ { N } = 5 0$ , reviews have more opportunity to be viewed by at least one voter, resulting in a smaller PRZ. However, when more no-zero-TV reviews are used to calculate $\rho ,$ a reduction of ρ may occur.

The main purpose of this study is not to discover or build the bestranking approach, but to gain some new insights through this controlled simulated world. The discussions of diferent scenarios mentioned above have established that when there are fewer reviews, the review quality variation is smaller, and voters are willing to read more reviews, which will cause AHR to decline. Moreover, although using HRF or BLB can provide better performance, numerical simulations are inadequate to prove which is the best-ranking approach. In other words, solely emphasizing which approach is better is less meaningful than further improving existing approaches, which will help managers optimize their ranking systems. Next, we propose two simple ways to enhance HRF and BLB.

## 5. Enhancing ranking approaches

## 5.1. Problems of reviews with zero or few votes

We first explain why, regardless of which ranking approach is used, reviews with zero or few votes hinder the improvement of AHR. This kind of issue is called the “cold start” problem in computer science literature, particularly in studies of recommending systems [36–38]. Three types of cold start problems can be distinguished: new commu nity, new user, and new item [39]. The common strategy for tackling these problems is to consider more characteristics of items and users in recommending systems, such as content-based filtering, demographic filtering, and collaborative filtering [40,41]. Our problem of review with zero or few votes is similar to a new-item problem. Using our model, we can gain insights into how the cold-start problem applies to review rankings.

Table 5  
Evaluations for three ranking approaches.

<table><tr><td rowspan="2">Experiments</td><td colspan="4">Basic information</td><td colspan="3">Evaluation criteria</td></tr><tr><td>N</td><td>Voters</td><td>TTV</td><td>THV</td><td>AHR</td><td> $\rho$ </td><td>PRZ</td></tr><tr><td colspan="8">Panel A: The most recent first ranking approach (MRF)</td></tr><tr><td>ReSim(S1, MRF)</td><td>429.8(21.1)</td><td>2081.7(44.7)</td><td>39,750.3(897.2)</td><td>19,911.6(583.0)</td><td>0.5009(0.0098)</td><td>0.0007(0.0519)</td><td>0.0005(0.0012)</td></tr><tr><td>ReSim(S2, MRF)</td><td>426.5(20.5)</td><td>2011.1(44.6)</td><td>38,416.2(882.5)</td><td>19,210.8(569.2)</td><td>0.5001(0.0095)</td><td>-0.0008(0.0510)</td><td>0.0005(0.0011)</td></tr><tr><td>ReSim(S3, MRF)</td><td>257.5(15.9)</td><td>1264.0(34.7)</td><td>23,696.4(696.2)</td><td>11,848.4(444.3)</td><td>0.5000(0.0121)</td><td>-0.0007(0.0693)</td><td>0.0007(0.0018)</td></tr><tr><td>ReSim(S4, MRF)</td><td>489.4(21.6)</td><td>2295.0(46.4)</td><td>44,008.8(922.2)</td><td>22,006.5(583.3)</td><td>0.5001(0.0091)</td><td>-0.0004(0.0480)</td><td>0.0005(0.0010)</td></tr><tr><td>ReSim(S5, MRF)</td><td>429.4(20.0)</td><td>2082.4(45.3)</td><td>39,765.8(899.6)</td><td>19,876.5(494.8)</td><td>0.4998(0.0057)</td><td>0.0016(0.0573)</td><td>0.0005(0.0011)</td></tr><tr><td>ReSim(S6, MRF)</td><td>429.0(20.9)</td><td>4024.8(61.6)</td><td>76,907.5(1270.8)</td><td>38,451.0(953.7)</td><td>0.5000(0.0096)</td><td>-0.0012(0.0516)</td><td>0.0003(0.0008)</td></tr><tr><td>ReSim(S7, MRF)</td><td>429.0(20.9)</td><td>2081.8(46.6)</td><td>20,861.7(487.3)</td><td>10,433.6(319.1)</td><td>0.5001(0.0098)</td><td>0.0019(0.0486)</td><td>0.0006(0.0013)</td></tr><tr><td>ReSim(S8, MRF)</td><td>429.7(21.2)</td><td>2081.6(45.0)</td><td>50,559.4(1245.8)</td><td>25,259.8(777.3)</td><td>0.4996(0.0097)</td><td>-0.0009(0.0535)</td><td>0.0008(0.0015)</td></tr><tr><td colspan="8">Panel B: The most helpful first ranking approach (MHF)</td></tr><tr><td>ReSim(S1, MHF)</td><td>428.9(20.3)</td><td>2082.9(44.3)</td><td>39,765.5(886.6)</td><td>23,090.6(1405.7)</td><td>0.5806(0.0323)</td><td>0.3968(0.1061)</td><td>0.8629(0.0076)</td></tr><tr><td>ReSim(S2, MHF)</td><td>426.0(21.4)</td><td>2011.1(44.5)</td><td>38,401.5(896.3)</td><td>22,297.6(1360.7)</td><td>0.5807(0.0328)</td><td>0.3991(0.1101)</td><td>0.8621(0.0080)</td></tr><tr><td>ReSim(S3, MHF)</td><td>258.4(16.4)</td><td>1264.2(35.5)</td><td>23,713.3(706.7)</td><td>13,512.4(867.2)</td><td>0.5698(0.0328)</td><td>0.3654(0.1184)</td><td>0.7833(0.0147)</td></tr><tr><td>ReSim(S4, MHF)</td><td>489.4(22.7)</td><td>2294.3(48.0)</td><td>43,989.5(959.6)</td><td>25,619.6(1551.5)</td><td>0.5824(0.0331)</td><td>0.4019(0.1050)</td><td>0.8786(0.0066)</td></tr><tr><td>ReSim(S5, MHF)</td><td>428.8(19.7)</td><td>2083.3(46.0)</td><td>39,771.7(915.8)</td><td>20,998.6(931.3)</td><td>0.5280(0.0198)</td><td>0.2588(0.1093)</td><td>0.8630(0.0074)</td></tr><tr><td>ReSim(S6, MHF)</td><td>428.2(20.8)</td><td>4021.9(63.1)</td><td>76,807.4(1303.1)</td><td>44,475.4(2652.8)</td><td>0.5790(0.0326)</td><td>0.3759(0.1069)</td><td>0.8550(0.0082)</td></tr><tr><td>ReSim(S7, MHF)</td><td>428.5(20.1)</td><td>2083.2(44.3)</td><td>20,869.6(466.9)</td><td>12,426.4(873.3)</td><td>0.5954(0.0385)</td><td>0.3862(0.1126)</td><td>0.8856(0.0069)</td></tr><tr><td>ReSim(S8, MHF)</td><td>428.8(21.4)</td><td>2082.9(45.5)</td><td>50,633.0(1226.2)</td><td>29,354.6(1313.1)</td><td>0.5797(0.0216)</td><td>0.3054(0.0597)</td><td>0.6035(0.0204)</td></tr><tr><td colspan="8">Panel C: The best helpful ratio first ranking approach (HRF) with  $\xi = 0.5$ </td></tr><tr><td>ReSim(S1, HRF)</td><td>428.4(20.7)</td><td>2082.5(45.5)</td><td>39,762.9(931.3)</td><td>29,157.4(1040.9)</td><td>0.7333(0.0200)</td><td>0.7203(0.0193)</td><td>0.6317(0.0474)</td></tr><tr><td>ReSim(S2, HRF)</td><td>427.0(22.0)</td><td>2011.4(46.1)</td><td>38,438.7(921.2)</td><td>28,198.7(1022.6)</td><td>0.7336(0.0201)</td><td>0.7217(0.0189)</td><td>0.6313(0.0477)</td></tr><tr><td>ReSim(S3, HRF)</td><td>258.1(16.4)</td><td>1265.7(35.6)</td><td>23,729.0(728.8)</td><td>16,803.1(749.8)</td><td>0.7081(0.0215)</td><td>0.7392(0.0213)</td><td>0.4491(0.0708)</td></tr><tr><td>ReSim(S4, HRF)</td><td>488.8(22.4)</td><td>2296.7(47.0)</td><td>44,044.6(949.6)</td><td>32,564.3(1092.0)</td><td>0.7394(0.0192)</td><td>0.7151(0.0188)</td><td>0.6701(0.0410)</td></tr><tr><td>ReSim(S5, HRF)</td><td>428.8(20.4)</td><td>2079.5(44.1)</td><td>39,692.3(905.2)</td><td>24,917.4(782.9)</td><td>0.6278(0.0134)</td><td>0.6220(0.0237)</td><td>0.5280(0.0639)</td></tr><tr><td>ReSim(S6, HRF)</td><td>429.9(20.2)</td><td>4022.3(61.6)</td><td>76,865.6(1262.4)</td><td>56,968.6(1737.3)</td><td>0.7411(0.0192)</td><td>0.7087(0.0184)</td><td>0.6119(0.0471)</td></tr><tr><td>ReSim(S7, HRF)</td><td>428.5(21.2)</td><td>2082.0(45.5)</td><td>20,855.6(480.8)</td><td>15,669.5(602.1)</td><td>0.7513(0.0222)</td><td>0.6764(0.0205)</td><td>0.6961(0.0407)</td></tr><tr><td>ReSim(S8, HRF)</td><td>428.1(20.8)</td><td>2083.9(45.4)</td><td>50,665.1(1235.8)</td><td>35,688.0(1245.8)</td><td>0.7043(0.0155)</td><td>0.6766(0.0138)</td><td>0.1627(0.0438)</td></tr></table>

Note: This table shows the averages of the number of reviews, the number of voters, TTV, THV, AHR, ρ, and PRZ based on simulations. The standard deviations are displayed in corresponding parentheses.

First, we explore the problem of reviews with zero votes. Intuitively, if a large number of reviews have no chance to be viewed, that is, PRZ is high, high-quality reviews may be directly ignored. Of course, lowquality reviews will also be ignored. But this does not “cancel out.” The intuition is that votes convey information; they are a noisy signal, but they do reflect the quality and they allow ranking methods to show increasingly good reviews. Therefore, all else being equal, the more reviews about which we can collect votes, the higher will be the AHR. A specific example can help us illustrate the influence of PRZ more clearly. Suppose, at a certain time point, there are 400 reviews whose quality follows a Beta distribution with $\beta _ { 1 } = \beta _ { 2 } = 3$ as shown in Eq. (3). Whether reviews receive at least one vote follows a Bernoulli distribution in which the expected proportion of zero-vote reviews is equal to PRZ. The unknown quality of zero-vote reviews is regarded as 0.5. We then assume that there is a best-ranking approach that can obtain the reviews’ true quality once they have been voted on by anyone, and thus can exactly sort all reviews depending on quality. In this way, the average quality of the first 20, 30, and 40 reviews can be calculated, and these values might be regarded as the upper bounds of average quality among all ranking approaches. Fig. 10 displays how PRZ afects these upper bounds through 5000 simulations based on the mentioned settings. For example, if there are no zero-vote reviews (PRZ = 0), the mean of the average quality of the first 20 reviews is 0.860; but if only

Table 6  
Evaluations for the Bayesian lower bound ranking approach.

<table><tr><td rowspan="2">Experiments</td><td colspan="4">Basic information</td><td colspan="3">Evaluation criteria</td></tr><tr><td>N</td><td>Voters</td><td>TTV</td><td>THV</td><td>AHR</td><td> $\rho$ </td><td>PRZ</td></tr><tr><td colspan="8">Panel A: BLB with  ${\beta }_{H} = {\beta }_{N} = 3$ </td></tr><tr><td>ReSim(S1, BLB3)</td><td>429.9(20.2)</td><td>2081.5(44.8)</td><td>39,734.8(898.9)</td><td>27,249.5(1189.1)</td><td>0.6858(0.0252)</td><td>0.7555(0.0432)</td><td>0.7891(0.0215)</td></tr><tr><td>ReSim(S3, BLB3)</td><td>258.0(16.3)</td><td>1264.3(36.3)</td><td>23,706.4(725.2)</td><td>15,797.9(811.8)</td><td>0.6663(0.0259)</td><td>0.7520(0.0488)</td><td>0.6783(0.0335)</td></tr><tr><td>ReSim(S5, BLB3)</td><td>429.4(20.3)</td><td>2085.8(46.0)</td><td>39,837.3(926.8)</td><td>23,462.1(898.1)</td><td>0.5889(0.0177)</td><td>0.6837(0.0557)</td><td>0.8007(0.0190)</td></tr><tr><td>ReSim(S8, BLB3)</td><td>428.8(21.4)</td><td>2083.0(45.3)</td><td>50,618.0(1236.2)</td><td>34,377.4(1250.0)</td><td>0.6791(0.0172)</td><td>0.6507(0.0320)</td><td>0.4456(0.0327)</td></tr><tr><td colspan="8">Panel B: BLB with  ${\beta }_{H} = {\beta }_{N} = {10}$ </td></tr><tr><td>ReSim(S1, BLB10)</td><td>429.0(19.7)</td><td>2081.8(45.8)</td><td>39,768.0(916.7)</td><td>27,901.8(1124.1)</td><td>0.7016(0.0229)</td><td>0.6912(0.0397)</td><td>0.7382(0.0299)</td></tr><tr><td>ReSim(S3, BLB10)</td><td>258.4(16.3)</td><td>1264.9(36.9)</td><td>23,713.5(745.4)</td><td>16,131.6(771.3)</td><td>0.6802(0.0238)</td><td>0.6851(0.0473)</td><td>0.6056(0.0454)</td></tr><tr><td>ReSim(S5, BLB10)</td><td>429.2(20.1)</td><td>2081.6(44.6)</td><td>39,752.2(908.6)</td><td>23,898.7(854.7)</td><td>0.6012(0.0160)</td><td>0.6243(0.0447)</td><td>0.7352(0.0303)</td></tr><tr><td>ReSim(S8, BLB10)</td><td>428.2(21.3)</td><td>2083.6(44.9)</td><td>50,629.6(1211.4)</td><td>34,715.6(1172.1)</td><td>0.6856(0.0150)</td><td>0.5843(0.0286)</td><td>0.3449(0.0390)</td></tr><tr><td colspan="8">Panel C: BLB with  ${\beta }_{H} = {\beta }_{N} = {20}$ </td></tr><tr><td>ReSim(S1, BLB20)</td><td>429.2(20.2)</td><td>2083.5(45.9)</td><td>39,770.9(944.3)</td><td>28,031.6(1120.2)</td><td>0.7048(0.0225)</td><td>0.6594(0.0392)</td><td>0.7177(0.0323)</td></tr><tr><td>ReSim(S3, BLB20)</td><td>258.5(15.9)</td><td>1265.9(34.8)</td><td>23,751.1(713.6)</td><td>16,278.0(740.8)</td><td>0.6853(0.0222)</td><td>0.6526(0.0435)</td><td>0.5749(0.0498)</td></tr><tr><td>ReSim(S5, BLB20)</td><td>428.7(20.8)</td><td>2080.4(43.0)</td><td>39,722.8(853.9)</td><td>24,085.3(816.7)</td><td>0.6063(0.0157)</td><td>0.5903(0.0404)</td><td>0.6992(0.0368)</td></tr><tr><td>ReSim(S8, BLB20)</td><td>429.8(21.4)</td><td>2082.8(44.6)</td><td>50,624.9(1218.5)</td><td>34,805.5(1209.3)</td><td>0.6875(0.0153)</td><td>0.5540(0.0266)</td><td>0.3096(0.0413)</td></tr><tr><td colspan="8">Panel D: BLB with  ${\beta }_{H} = {\beta }_{N} = {50}$ </td></tr><tr><td>ReSim(S1, BLB50)</td><td>429.6(21.0)</td><td>2083.5(45.5)</td><td>39,789.3(915.7)</td><td>28,216.2(1066.5)</td><td>0.7091(0.0209)</td><td>0.6277(0.0356)</td><td>0.6975(0.0354)</td></tr><tr><td>ReSim(S3, BLB50)</td><td>258.3(15.8)</td><td>1264.2(35.2)</td><td>23,712.3(710.9)</td><td>16,295.6(733.2)</td><td>0.6872(0.0215)</td><td>0.6207(0.0391)</td><td>0.5459(0.0516)</td></tr><tr><td>ReSim(S5, BLB50)</td><td>430.1(20.9)</td><td>2082.2(45.0)</td><td>39,758.4(905.0)</td><td>24,327.6(820.6)</td><td>0.6119(0.0146)</td><td>0.5555(0.0368)</td><td>0.6633(0.0422)</td></tr><tr><td>ReSim(S8, BLB50)</td><td>429.2(20.8)</td><td>2082.3(45.8)</td><td>50,601.8(1218.2)</td><td>34,772.1(1157.9)</td><td>0.6871(0.0146)</td><td>0.5211(0.0263)</td><td>0.2760(0.0420)</td></tr></table>

Note: This table shows the averages of the number of reviews, the number of voters, TTV, THV, AHR, ρ, and PRZ based on simulations. The standard deviations are displayed in corresponding parentheses.

![](/api/attachments/DD3JTA7K/fulltext/images/3a8eb9d953da52bc57a6979b9fd112da9cb61f555bc32c043ec5ca4f93464f5d.jpg)  
Fig. 10. Efects of reviews with zero votes on average quality.

![](/api/attachments/DD3JTA7K/fulltext/images/92db965aeb2356c2db76595502fe34805836f3bf1c5f9f45bdd3f18ca18ecac6.jpg)  
Fig. 11. Survival analysis of reviews with few votes.

Table 7  
Survival probability of reviews with few votes.

<table><tr><td rowspan="2"># Votes</td><td colspan="9">True quality of the review</td></tr><tr><td>0.9</td><td>0.8</td><td>0.7</td><td>0.6</td><td>0.5</td><td>0.4</td><td>0.3</td><td>0.2</td><td>0.1</td></tr><tr><td colspan="10">Panel A: The default quality of zero-vote review is 0.5</td></tr><tr><td>2</td><td>0.900</td><td>0.800</td><td>0.700</td><td>0.600</td><td>0.500</td><td>0.400</td><td>0.300</td><td>0.200</td><td>0.100</td></tr><tr><td>3</td><td>0.891</td><td>0.768</td><td>0.637</td><td>0.504</td><td>0.375</td><td>0.256</td><td>0.153</td><td>0.072</td><td>0.019</td></tr><tr><td>4</td><td>0.891</td><td>0.768</td><td>0.637</td><td>0.504</td><td>0.375</td><td>0.256</td><td>0.153</td><td>0.072</td><td>0.019</td></tr><tr><td>5</td><td>0.889</td><td>0.758</td><td>0.611</td><td>0.458</td><td>0.313</td><td>0.187</td><td>0.091</td><td>0.031</td><td>0.004</td></tr><tr><td>6</td><td>0.889</td><td>0.758</td><td>0.611</td><td>0.458</td><td>0.313</td><td>0.187</td><td>0.091</td><td>0.031</td><td>0.004</td></tr><tr><td>7</td><td>0.889</td><td>0.754</td><td>0.597</td><td>0.430</td><td>0.273</td><td>0.145</td><td>0.059</td><td>0.015</td><td>0.001</td></tr><tr><td>8</td><td>0.889</td><td>0.754</td><td>0.597</td><td>0.430</td><td>0.273</td><td>0.145</td><td>0.059</td><td>0.015</td><td>0.001</td></tr><tr><td>9</td><td>0.889</td><td>0.752</td><td>0.588</td><td>0.412</td><td>0.246</td><td>0.118</td><td>0.040</td><td>0.007</td><td>0.000</td></tr><tr><td>10</td><td>0.889</td><td>0.752</td><td>0.588</td><td>0.412</td><td>0.246</td><td>0.118</td><td>0.040</td><td>0.007</td><td>0.000</td></tr><tr><td>11</td><td>0.889</td><td>0.751</td><td>0.583</td><td>0.398</td><td>0.226</td><td>0.097</td><td>0.028</td><td>0.004</td><td>0.000</td></tr><tr><td>12</td><td>0.889</td><td>0.751</td><td>0.583</td><td>0.398</td><td>0.226</td><td>0.097</td><td>0.028</td><td>0.004</td><td>0.000</td></tr><tr><td>13</td><td>0.889</td><td>0.751</td><td>0.580</td><td>0.388</td><td>0.209</td><td>0.082</td><td>0.020</td><td>0.002</td><td>0.000</td></tr><tr><td>14</td><td>0.889</td><td>0.751</td><td>0.580</td><td>0.388</td><td>0.209</td><td>0.082</td><td>0.020</td><td>0.002</td><td>0.000</td></tr><tr><td>15</td><td>0.889</td><td>0.750</td><td>0.578</td><td>0.380</td><td>0.196</td><td>0.071</td><td>0.014</td><td>0.001</td><td>0.000</td></tr><tr><td colspan="10">Panel B: The default quality of zero-vote review is 0.6</td></tr><tr><td>2</td><td>0.810</td><td>0.640</td><td>0.490</td><td>0.360</td><td>0.250</td><td>0.160</td><td>0.090</td><td>0.040</td><td>0.010</td></tr><tr><td>3</td><td>0.810</td><td>0.640</td><td>0.490</td><td>0.360</td><td>0.250</td><td>0.160</td><td>0.090</td><td>0.040</td><td>0.010</td></tr><tr><td>4</td><td>0.802</td><td>0.614</td><td>0.446</td><td>0.302</td><td>0.188</td><td>0.102</td><td>0.046</td><td>0.014</td><td>0.002</td></tr><tr><td>5</td><td>0.802</td><td>0.614</td><td>0.446</td><td>0.302</td><td>0.188</td><td>0.102</td><td>0.046</td><td>0.014</td><td>0.002</td></tr><tr><td>6</td><td>0.800</td><td>0.606</td><td>0.427</td><td>0.275</td><td>0.156</td><td>0.075</td><td>0.027</td><td>0.006</td><td>0.000</td></tr><tr><td>7</td><td>0.797</td><td>0.590</td><td>0.395</td><td>0.233</td><td>0.117</td><td>0.047</td><td>0.013</td><td>0.002</td><td>0.000</td></tr><tr><td>8</td><td>0.797</td><td>0.590</td><td>0.395</td><td>0.233</td><td>0.117</td><td>0.047</td><td>0.013</td><td>0.002</td><td>0.000</td></tr><tr><td>9</td><td>0.797</td><td>0.585</td><td>0.383</td><td>0.215</td><td>0.100</td><td>0.035</td><td>0.008</td><td>0.001</td><td>0.000</td></tr><tr><td>10</td><td>0.797</td><td>0.585</td><td>0.383</td><td>0.215</td><td>0.100</td><td>0.035</td><td>0.008</td><td>0.001</td><td>0.000</td></tr><tr><td>11</td><td>0.797</td><td>0.583</td><td>0.376</td><td>0.204</td><td>0.088</td><td>0.028</td><td>0.005</td><td>0.000</td><td>0.000</td></tr><tr><td>12</td><td>0.796</td><td>0.579</td><td>0.363</td><td>0.185</td><td>0.072</td><td>0.019</td><td>0.003</td><td>0.000</td><td>0.000</td></tr><tr><td>13</td><td>0.796</td><td>0.579</td><td>0.363</td><td>0.185</td><td>0.072</td><td>0.019</td><td>0.003</td><td>0.000</td><td>0.000</td></tr><tr><td>14</td><td>0.796</td><td>0.577</td><td>0.357</td><td>0.176</td><td>0.064</td><td>0.015</td><td>0.002</td><td>0.000</td><td>0.000</td></tr><tr><td>15</td><td>0.796</td><td>0.577</td><td>0.357</td><td>0.176</td><td>0.064</td><td>0.015</td><td>0.002</td><td>0.000</td><td>0.000</td></tr></table>

10% of reviews receive at least one vote (PRZ = 0.9), the mean of average quality is reduced to 0.653. In short, a higher PRZ causes the upper bound of the viewed reviews’ average quality to be lower, so we can attempt to reduce PRZ to improve AHR.

In addition to the problem of reviews with zero votes, some high quality reviews may be judged as low-quality ones because of the stochastic nature of votes as shown in Eq. (8). Once a review's quality is judged as lower than the default quality of the zero-vote reviews, this review nearly loses the opportunity to be seen. For example, 400 reviews with a PRZ of 0.3 imply that there are 120 zero-vote reviews. Once a review's quality is judged to be below the default quality, it will be ranked after all the 120 zero-vote reviews. To analyze this phe nomenon, we define the survival probability given a review receives n votes as the probability that its judged quality is always higher than or equal to the default quality when this review receives x votes. $x = 1 ,$ , 2, …, n. Suppose the default quality is 0.5, Fig. 11 displays the survival analysis of one review with true quality q. It should be noted that this is not a standard binomial distribution due to its path dependence. Consequently, when a review receives the first 3 votes, its survival probability is $q ^ { 3 } + 2 q ^ { 2 } ( 1 - q )$ . Considering the true quality of the reviews as between 0.1 and 0.9, Table 7 summarizes their survival probabilities when receiving $2 , 3 , . . . ,$ 15 votes. In this table, panels A and B represent the cases of default quality of 0.5 and 0.6, representatively. For example, given a default quality of 0.5 and true quality of 0.8, the survival probability of reviews with 10 votes is 0.752. It indicates that approximately 24.8% of reviews with $q = 0 . 8$ are incorrectly ranked behind the zero-vote reviews. Although the survival probability of highquality reviews decreases when the default quality is increased to 0.6, this setting can also exclude more low-quality ones. Therefore, giving these previously ignored high-quality reviews another chance to be ranked in front will prevent them from becoming buried in a large number of reviews.

According to the mentioned findings, we can attempt to enhance the ranking approach from two aspects. The first way is to give higher ranking scores to reviews of unknown quality, which ensures that more reviews are evaluated at least once. The second way is to allow reviews with a low number of votes additional chances to be evaluated again. Next, we further explain how to implement these improvements in HRF and BLB.

## 5.2. Adjustments to HRF

Adjustments to HRF are focused on reducing the number of zerovote reviews by adjusting its default setting. Specifically, as shown in Eq. (11), the ranking score of HRF has a predetermined parameter of ξ, which is always set as 0.5 in the previous analysis. When all reviews of unknown quality are regarded as higher quality ones, we can investigate whether the performance of HRF really improves. According to this concept, we increase the value of ξ to 0.6 and 0.7, and we also test whether reducing the value of ξ has a reverse efect. Following the same simulation procedures, the related outcomes are displayed in Table 8. Consistent with our expectation, when ξ is larger than the default value of 0.5, AHR is better than the original result in various scenarios; however, when $\xi = 0 . 4 ,$ , AHR becomes worse. In addition, a greater ξ always induces a lower PRZ. We briefly explain this result. Given $\xi = 0 . 5 ,$ , if there are enough reviews whose helpful ratios are greater than 0.5, all zero-vote reviews will no longer be easily seen, even if their true quality is greater than 0.5. However, given $\xi = 0 . 6$ or 0.7, reviews can be ranked before the zero-vote ones only if their quality is above 0.6 or 0.7. Accordingly, only reviews of suficiently high quality can be placed in front of zero-vote reviews, which ensures that people see high-quality reviews or assist in evaluating some zerovote reviews. In other words, zero-vote reviews have a better chance of being seen, which contributes to finding more high-quality reviews.

Table 8  
Evaluations for the best helpful ratio first ranking approach with diferent ξ.

<table><tr><td rowspan="2">Experiments</td><td colspan="4">Basic information</td><td colspan="3">Evaluation criteria</td></tr><tr><td>N</td><td>Voters</td><td>TTV</td><td>THV</td><td>AHR</td><td> $\rho$ </td><td>PRZ</td></tr><tr><td colspan="8">Panel A: HRF with  $\xi = 0.4$ </td></tr><tr><td>ReSim(S1, HRF)</td><td>430.0(20.3)</td><td>2083.6(43.6)</td><td>39,764.5(895.2)</td><td>28,517.4(1107.7)</td><td>0.7171(0.0222)</td><td>0.7704(0.0190)</td><td>0.7179(0.0334)</td></tr><tr><td>ReSim(S3, HRF)</td><td>258.1(15.9)</td><td>1266.1(35.2)</td><td>23,755.5(718.1)</td><td>16,474.5(771.7)</td><td>0.6934(0.0229)</td><td>0.7848(0.0218)</td><td>0.5696(0.0508)</td></tr><tr><td>ReSim(S5, HRF)</td><td>429.0(19.9)</td><td>2080.8(44.6)</td><td>39,733.9(900.7)</td><td>24,269.5(802.8)</td><td>0.6108(0.0153)</td><td>0.7101(0.0188)</td><td>0.7144(0.0351)</td></tr><tr><td>ReSim(S8, HRF)</td><td>429.0(20.2)</td><td>2084.5(47.6)</td><td>50,700.5(1285.8)</td><td>35,449.2(1300.2)</td><td>0.6991(0.0160)</td><td>0.7149(0.0147)</td><td>0.3002(0.0430)</td></tr><tr><td colspan="8">Panel B: HRF with  $\xi = 0.6$ </td></tr><tr><td>ReSim(S1, HRF)</td><td>430.1(20.7)</td><td>2086.0(46.8)</td><td>39,838.1(938.5)</td><td>30,035.6(1004.3)</td><td>0.7539(0.0176)</td><td>0.6025(0.0284)</td><td>0.3905(0.0767)</td></tr><tr><td>ReSim(S3, HRF)</td><td>258.8(15.5)</td><td>1265.7(35.0)</td><td>23,749.7(705.3)</td><td>17,144.9(735.1)</td><td>0.7219(0.0213)</td><td>0.6318(0.0286)</td><td>0.1686(0.0826)</td></tr><tr><td>ReSim(S5, HRF)</td><td>429.7(20.1)</td><td>2083.2(45.4)</td><td>39,779.5(917.7)</td><td>25,364.8(798.2)</td><td>0.6376(0.0132)</td><td>0.4475(0.0204)</td><td>0.0212(0.0277)</td></tr><tr><td>ReSim(S8, HRF)</td><td>428.4(22.2)</td><td>2082.4(43.9)</td><td>50,605.2(1192.5)</td><td>35,829.4(1223.6)</td><td>0.7080(0.0156)</td><td>0.6362(0.0177)</td><td>0.0254(0.0134)</td></tr><tr><td colspan="8">Panel C: HRF with  $\xi = 0.7$ </td></tr><tr><td>ReSim(S1, HRF)</td><td>429.9(20.6)</td><td>2080.1(43.4)</td><td>39,728.4(864.4)</td><td>30,242.2(983.7)</td><td>0.7612(0.0178)</td><td>0.5063(0.0225)</td><td>0.0657(0.0549)</td></tr><tr><td>ReSim(S3, HRF)</td><td>257.8(15.8)</td><td>1265.0(35.7)</td><td>23,719.4(727.8)</td><td>17,127.7(773.5)</td><td>0.7220(0.0221)</td><td>0.5889(0.0249)</td><td>0.0095(0.0127)</td></tr><tr><td>ReSim(S5, HRF)</td><td>429.9(21.2)</td><td>2081.9(44.7)</td><td>39,752.0(901.3)</td><td>25,346.0(825.6)</td><td>0.6376(0.0139)</td><td>0.4449(0.0200)</td><td>0.0005(0.0012)</td></tr><tr><td>ReSim(S8, HRF)</td><td>429.5(20.4)</td><td>2082.7(46.7)</td><td>50,606.9(1260.2)</td><td>35,831.0(1251.4)</td><td>0.7080(0.0151)</td><td>0.6316(0.0183)</td><td>0.0035(0.0032)</td></tr></table>

Note: This table shows the averages of the number of reviews, the number of voters, TTV, THV, AHR, $\rho ,$ and PRZ based on simulations. The standard deviations are displayed in corresponding parentheses.

## 5.3. Adjustments to BLB

Adjustments to BLB are focused on not only reducing the number of zero-vote reviews but also giving an additional chance to be viewed again for few-vote reviews. First, we allow reviews that only receive a small number of votes another chance of being viewed to increase opportunities to detect high-quality reviews. Following this idea, we propose an adjusted Bayesian lower bound ranking approach (ABLB). As for the other approaches, we first define the ranking score as

$$
\zeta_ {t} ^ {i} (\mathrm{ABLB}) = \zeta_ {t} ^ {i} (\mathrm{BLB}) + \gamma (p) \times 2 \sqrt {\frac {\beta_ {H} ^ {*} \beta_ {N} ^ {*}}{(\beta_ {H} ^ {*} + \beta_ {N} ^ {*}) ^ {2} (\beta_ {H} ^ {*} + \beta_ {N} ^ {*} + 1)}},\tag{17}
$$

where $\zeta _ { t } ^ { i } ( \mathrm { B L B } )$ is defined in Eq. (14) and $\gamma$ follows a Bernoulli distribution with a change rate p. When $p = 0 . 1$ , every review has a 10% chance to increase its ranking score by 2 times the standard deviation of the corresponding posterior belief distribution as specified in Eq. (13).

Therefore, every review has an opportunity to increase its score and improve its ranking. Although initially the probability of receiving extra scores is the same for each review, the number of extra scores will be afected by HV<sup>i</sup> and $\mathrm { N V } _ { t } ^ { i } .$ . In general, more votes result in less extra scores, ensuring that the review still has an opportunity to be sorted to its previous position before its quality is confirmed. By contrast, if a low-quality review has been evaluated by many voters, the extra score is not suficient to significantly increase its rank. More technical discussions of the relationship between the number of votes and extra scores can be found in Appendix A.3.

To evaluate the performance of ABLB. we consider three levels of change rates: 0.1, 0.2, and 0.3. Because the scenarios $S _ { 3 } , S _ { 5 } ,$ and $S _ { 8 }$ have the same characteristics as $S _ { 1 } ,$ we only report the related results for the benchmark scenario $S _ { 1 }$ in Table 9. The PRZ in $S _ { 1 }$ is at least $0 . 7 ,$ as shown in Table 6. The original intent of ABLB is to reduce PRZ, and indeed, ABLB works well; in 12 experiments, the maximum PRZ is only $_ { 0 . 4 9 0 }$ and the minimum is 0.248. Furthermore, ABLB also produces higher AHR than BLB. For example, in ${ \mathrm { R e S i m } } ( S _ { 1 } ,$ ABLB10), AHR is approximately 0.74, compared to 0.7 in ${ \mathrm { R e S i m } } ( S _ { 1 }$ , BLB10). However, because many more non-zero-vote reviews are considered in computing $\rho ,$ ABLB yields smaller ρ than BLB. Our results indicate that giving reviews more extra opportunities indeed improves the performance of BLB. Moreover, we improve ABLB through reducing the number of zero-vote reviews. Specifically, for convenience, we set $\beta _ { H } = 2 \times \beta _ { N }$ in Eq. (12), which means we assume zero-vote reviews have a higher default quality. In the following discussions, we add the symbol \* to ABLB to represent the modified approach. For example, the parameters of quality prior belief in ABLB10 are $\beta _ { H } = 1 0$ and $\beta _ { N } = 1 0$ , but in ABLB10\*, they are $\beta _ { H } = 2 \times 1 0$ and $\beta _ { N } = 1 0$ . Then, we repeat the simulations and show the corresponding results in Table 10. Obviously, ABLB\* performs better than ABLB.

Finally, we further explore how the performance changes through time for each ranking approach. Given scenario $S _ { 1 } ,$ we conduct the same simulated procedure for MRF, MHF, BLB3, and HRF with $\xi = 0 . 5 ,$ , ABLB3 with $p = 0 . 1$ , HRF with $\xi = 0 . 6 ,$ and ABLB3\* with $p = 0 . 1$ . We can then record the numbers of TV and HV in each day, and thus the daily AHR can be determined. Based on 1000 simulations, the average daily AHR for each approach can be calculated, as shown in Fig. 12. We summarize three findings through this figure. First, with the exception of MRF, AHR increases over time for all approaches, but the rate of increase gradually slows, in dicating that people can find high-quality reviews more easily over time. Second, without using the two rules to enhance the original method, at all time points, HRF exhibits the best performance in terms of the average daily AHR. Third, incorporating Rule 1 (Rule 2), although the initial improve ment of HRF (BLB) is not obvious, its average daily AHR is clearly better than that of the original approach after approximately 7 (5) days. In addi tion, it is interesting to compare the performance changes of ABLB3\* and HRF with $\xi = 0 . 6$ . Initially, the latter's AHR is better than that of the former, but $\mathtt { A B L B 3 ^ { * } }$ can continue to improve AHR for a longer period of time. After approximately two weeks, ABLB3\* starts to gain an advantage and remains ahead thereafter. Therefore, appropriate PRZ reductions according to our rules do allow more high-quality reviews to be detected, increasing the usefulness of information delivered to users of the website.

Table 9  
Evaluations for ABLB.

<table><tr><td rowspan="2">Experiments</td><td colspan="4">Basic information</td><td colspan="3">Evaluation criteria</td></tr><tr><td>N</td><td>Voters</td><td>TTV</td><td>THV</td><td>AHR</td><td> $\rho$ </td><td>PRZ</td></tr><tr><td colspan="8">Panel A: Adjusted BLB with change rate = 0.1</td></tr><tr><td>ReSim(S1, ABLB3)</td><td>429.9(20.6)</td><td>2082.7(43.7)</td><td>39,757.7(881.5)</td><td>29,624.8(975.0)</td><td>0.7451(0.0173)</td><td>0.4948(0.0290)</td><td>0.3679(0.0606)</td></tr><tr><td>ReSim(S1, ABLB10)</td><td>429.5(20.0)</td><td>2085.1(46.2)</td><td>39,805.7(935.7)</td><td>29,238.4(967.2)</td><td>0.7345(0.0171)</td><td>0.4095(0.0317)</td><td>0.3614(0.0582)</td></tr><tr><td>ReSim(S1, ABLB20)</td><td>429.7(20.1)</td><td>2081.9(43.7)</td><td>39,755.4(888.3)</td><td>28,953.5(986.0)</td><td>0.7283(0.0177)</td><td>0.3588(0.0273)</td><td>0.3201(0.0570)</td></tr><tr><td>ReSim(S1, ABLB50)</td><td>429.6(20.5)</td><td>2082.6(44.5)</td><td>39,766.4(885.1)</td><td>28,495.2(972.7)</td><td>0.7166(0.0180)</td><td>0.3123(0.0235)</td><td>0.2483(0.0526)</td></tr><tr><td colspan="8">Panel B: Adjusted BLB with change rate = 0.2</td></tr><tr><td>ReSim(S1, ABLB3)</td><td>429.1(20.9)</td><td>2084.2(44.7)</td><td>39,800.8(894.7)</td><td>29,771.8(996.3)</td><td>0.7480(0.0173)</td><td>0.5463(0.0260)</td><td>0.4172(0.0603)</td></tr><tr><td>ReSim(S1, ABLB10)</td><td>428.9(20.6)</td><td>2083.7(44.4)</td><td>39,777.1(883.7)</td><td>29,418.2(988.4)</td><td>0.7395(0.0175)</td><td>0.4846(0.0305)</td><td>0.4432(0.0551)</td></tr><tr><td>ReSim(S1, ABLB20)</td><td>427.7(20.8)</td><td>2082.7(44.0)</td><td>39,747.1(892.2)</td><td>29,136.8(977.5)</td><td>0.7330(0.0178)</td><td>0.4416(0.0284)</td><td>0.4305(0.0547)</td></tr><tr><td>ReSim(S1, ABLB50)</td><td>428.1(20.5)</td><td>2081.6(46.1)</td><td>39,744.2(911.2)</td><td>28,767.6(948.4)</td><td>0.7238(0.0179)</td><td>0.3982(0.0275)</td><td>0.4001(0.0554)</td></tr><tr><td colspan="8">Panel C: Adjusted BLB with change rate = 0.3</td></tr><tr><td>ReSim(S1, ABLB3)</td><td>429.5(20.8)</td><td>2081.6(45.6)</td><td>39,724.1(924.1)</td><td>29,733.9(1007.1)</td><td>0.7485(0.0174)</td><td>0.5738(0.0246)</td><td>0.4465(0.0590)</td></tr><tr><td>ReSim(S1, ABLB10)</td><td>428.4(20.5)</td><td>2083.1(42.9)</td><td>39,777.2(863.5)</td><td>29,441.9(973.3)</td><td>0.7402(0.0178)</td><td>0.5280(0.0281)</td><td>0.4877(0.0506)</td></tr><tr><td>ReSim(S1, ABLB20)</td><td>429.8(20.1)</td><td>2081.9(45.9)</td><td>39,760.4(911.5)</td><td>29,222.1(1016.5)</td><td>0.7349(0.0177)</td><td>0.4897(0.0280)</td><td>0.4899(0.0498)</td></tr><tr><td>ReSim(S1, ABLB50)</td><td>429.8(20.9)</td><td>2083.3(44.1)</td><td>39,787.5(877.0)</td><td>28,900.6(977.5)</td><td>0.7264(0.0182)</td><td>0.4511(0.0278)</td><td>0.4764(0.0510)</td></tr></table>

Note: This table shows the averages of the number of reviews, the number of voters, TTV, THV, AHR, ρ, and PRZ based on simulations. The standard deviations are displayed in corresponding parentheses.

Table 10  
Evaluations for ABLB\*

<table><tr><td rowspan="2">Experiments</td><td colspan="4">Basic information</td><td colspan="3">Evaluation criteria</td></tr><tr><td>N</td><td>Voters</td><td>TTV</td><td>THV</td><td>AHR</td><td> $\rho$ </td><td>PRZ</td></tr><tr><td colspan="8">Panel A:  $ABLB^*$  with change rate = 0.1</td></tr><tr><td>ReSim(S1, ABLB3*)</td><td>429.5(20.5)</td><td>2080.1(46.3)</td><td>39,716.7(917.1)</td><td>30,065.0(995.3)</td><td>0.7570(0.0171)</td><td>0.4285(0.0180)</td><td>0.0677(0.0341)</td></tr><tr><td>ReSim(S1, ABLB10*)</td><td>428.3(20.8)</td><td>2080.3(44.6)</td><td>39,718.1(900.6)</td><td>29,771.8(981.2)</td><td>0.7496(0.0173)</td><td>0.3834(0.0190)</td><td>0.0617(0.0284)</td></tr><tr><td>ReSim(S1, ABLB20*)</td><td>428.9(21.0)</td><td>2083.2(46.0)</td><td>39,784.0(929.3)</td><td>29,600.4(1024.5)</td><td>0.7440(0.0175)</td><td>0.3610(0.0188)</td><td>0.0521(0.0249)</td></tr><tr><td>ReSim(S1, ABLB50*)</td><td>429.9(20.5)</td><td>2081.2(44.7)</td><td>39,737.0(885.6)</td><td>29,092.4(1017.3)</td><td>0.7321(0.0179)</td><td>0.3399(0.0190)</td><td>0.0358(0.0160)</td></tr><tr><td colspan="8">Panel B:  $ABLB^*$  with change rate = 0.2</td></tr><tr><td>ReSim(S1, ABLB3*)</td><td>429.1(20.0)</td><td>2082.2(44.9)</td><td>39,769.3(896.0)</td><td>30,202.4(970.6)</td><td>0.7594(0.0167)</td><td>0.4555(0.0182)</td><td>0.0748(0.0406)</td></tr><tr><td>ReSim(S1, ABLB10*)</td><td>428.1(20.7)</td><td>2081.2(43.1)</td><td>39,744.0(876.3)</td><td>29,939.0(994.9)</td><td>0.7533(0.0173)</td><td>0.4172(0.0178)</td><td>0.0840(0.0413)</td></tr><tr><td>ReSim(S1, ABLB20*)</td><td>428.9(20.1)</td><td>2081.3(45.7)</td><td>39,747.2(914.1)</td><td>29,722.2(1020.4)</td><td>0.7477(0.0172)</td><td>0.3955(0.0184)</td><td>0.0824(0.0399)</td></tr><tr><td>ReSim(S1, ABLB50*)</td><td>429.7(20.1)</td><td>2085.1(46.6)</td><td>39,809.9(932.3)</td><td>29,397.3(1023.7)</td><td>0.7384(0.0179)</td><td>0.3726(0.0178)</td><td>0.0654(0.0328)</td></tr><tr><td colspan="8">Panel C:  $ABLB^*$  with change rate = 0.3</td></tr><tr><td>ReSim(S1, ABLB3*)</td><td>428.5(20.8)</td><td>2080.6(44.7)</td><td>39,721.0(896.0)</td><td>30,208.2(972.8)</td><td>0.7605(0.0169)</td><td>0.4714(0.0178)</td><td>0.0874(0.0498)</td></tr><tr><td>ReSim(S1, ABLB10*)</td><td>428.4(20.8)</td><td>2080.9(46.0)</td><td>39,729.8(931.4)</td><td>30,044.0(1012.9)</td><td>0.7562(0.0170)</td><td>0.4376(0.0185)</td><td>0.1073(0.0518)</td></tr><tr><td>ReSim(S1, ABLB20*)</td><td>429.1(20.8)</td><td>2083.5(42.6)</td><td>39,780.5(870.4)</td><td>29,922.1(954.9)</td><td>0.7522(0.0166)</td><td>0.4197(0.0187)</td><td>0.1133(0.0515)</td></tr><tr><td>ReSim(S1, ABLB50*)</td><td>430.2(20.9)</td><td>2084.1(43.9)</td><td>39,797.2(880.5)</td><td>29,565.7(962.4)</td><td>0.7429(0.0170)</td><td>0.3980(0.0176)</td><td>0.1045(0.0484)</td></tr></table>

Note: This table shows the averages of the number of reviews, the number of voters. TTV. THV. AHR. o, and PRZ based on simulations. The standard deviations are displayed in corresponding parentheses.

![](/api/attachments/DD3JTA7K/fulltext/images/2cffc16bd7107f12bafff56f88499bf4d704b7aa936ae6f0d4b91adbc58a8a4f.jpg)  
Fig. 12. Comparisons of dynamic average AHR in diferent approaches.

## 6. Conclusions, implications, and limitations

As a major form of user-generated content, online reviews play a vital role in electronic commerce. To address the problem faced by reviewhosting firms of detecting the helpfulness of reviews, we construct a complete conceptual framework to further understand the review system and compare the performance of ranking approaches. We also propose a new Bayesian-based ranking approach, BLB, which is competitive with other ranking approaches in terms of AHR and PRZ. This approach can be combined with other content recommendation techniques to determine the prior belief in online reviews. Moreover, we find that some existing ranking approaches can be enhanced through mitigating the Matthew efect. Based on this idea, we propose two ways to improve HRF and BLB. The main limitation of this study is that empirical data related to review helpfulness under diferent ranking approaches are not avail able. Consequently, the discussions are based on numerical simulations. For future studies, researchers could seek the cooperation of reviewhosting firms to obtain relevant data. Below, we introduce three im plications for review-hosting firms or online retailers.

First, our results indicate that no matter which ranking approach i used, the average helpfulness for users who obtain information from reviews will decline in three cases: there are fewer reviews, the distribution of review quality is more concentrated, or users read more reviews. Based on the first two cases, review-hosting firms should find ways to make more users willing to write reviews on the platform. In particular, if the average quality of the article is fixed, increasing the quality variation of reviews will help the various ranking approaches find high-quality reviews, thus making it easier for users to obtain useful information. The specific practice may be to increase the diversity of platform participants to enhance the variability of reviews. For the third case, the decrease in average helpfulness arising from users’ willingness to read more reviews is usually regarded as beneficial by review-hosting firms.

The second practical implication concerns the extension of BLB (or ABLB). Although our model assumes that prior beliefs of review quality are identical, as specified by $\operatorname { E q . }$ (12), users could determine each corresponding prior belief according to other helpfulness-predicting models. For example, some review-hosting firms may have their own existing review-recommending models, which may be constructed based on review content, reviewer characteristics, or any other observable factors. When a new review appears, firms can assess its quality based on their model without any voting information. Suppose their model can estimate the expected value and variance of the review quality, denoted $E [ \widehat { q } ^ { i } ]$ and var[ ]ˆq i , we can then determine the prior belief of this review. Specifically, as shown in footnote 1, if both the expected value and variance of a Beta distribution random variable are estimated, we can find two shape parameters $\beta _ { H }$ and $\beta _ { N }$ to construct the distribution of quality prior belief according to $\mathrm { E q . ( 1 2 ) . } ^ { 1 0 }$ In this way, if the review-hosting firm manager trusts $E [ \widehat { q } ^ { i } ] = 0 . 8$ and $\mathrm { v a r } [ \widehat { q } ^ { i } ] = 0 . 0 1$ for review i, he/she can set $\beta _ { H } = 1 2$ and $\beta _ { N } = 3$ as his/her prior belief. This review then has a better initial ranking. Thus, the flexibility of BLB allows it to be combined with other review-recommending methods, e.g., sentiment or content analysis. Such a combination represents another possible extension of BLB to be explored in future studies.

$$
\beta_ {H} = \left(\frac {1 - \mu}{\sigma^ {2}} - \frac {1}{\mu}\right) \mu^ {2}
$$

Third, the Matthew efect may result in zero votes for most reviews. In the short run, a large proportion of reviews are never evaluated by anyone, which is not conducive to the discovery of high-quality reviews. In the long run, people who write reviews do not receive any feedback, and they may lose their enthusiasm and stop participating in platform activities. This can even lead to a decline in the number of reviews. Therefore, recent studies also recommend that online retailers adopt dif ferent ranking strategies to mitigate the Matthew efect [31]. Two ways are proposed in Section 5 to mitigate the Matthew efect, and both can be implemented in existing approaches. When a review's quality is unknown, review-hosting firms can first assume that its quality is better than the average value, which can help more reviews be seen at least once. In addition, review-hosting firms can attempt to give a review with a small number of votes an opportunity to be seen by voters again, even if its quality is currently judged as worse. In fact, we think these two ways also apply to the treatment of people or things around us in everyday life. Being kinder to those we don’t know or are unfamiliar with and willing to give others more opportunities will make the world a better place.

## Algorithm 1. ReSim(T, η, δ, β<sub>1</sub>, β<sub>2</sub>, κ, m, φ)

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
1: procedure
2: # Initial Setting:
3:  $\Re_{0}\leftarrow\{\phi\}$ 
4: # Generate simulated data:
5: for t = 1 to T do:
6:  $n_{t}\leftarrow$  the number of elements in  $R_{t-1}$ 
7: # About reviews
8: if a new review appears then # Refer to Eq. (1)
</div>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
9:  $n_{t} \longleftarrow n_{t} + 1$ 
10:  $q^{n_{t}}$  is determined by Eq. (3)
11:  $R_{t} \longleftarrow \{R_{t-1}, R_{t}^{n_{t}}\}$ 
12:  $TV_{t-1}^{nt} \longleftarrow 0$ 
13:  $HV_{t-1}^{nt} \longleftarrow 0$ 
14: else
15:  $R_{t} \longleftarrow R_{t-1}$ 
16: # About voters
17: if a voter arrivals then # Refer to Eq. (5)
18: Calculate the each Rank( $R_{t}^{i}$ ) depended on a specific ranking approach
19: for for i = 1 to  $n_{t}$  do:
20:  $TV_{t}^{i} \longleftarrow TV_{t-1}^{i} + Y_{t}^{i}$  # Refer to Eq. (7)
21:  $HV_{t}^{i} \longleftarrow HV_{t-1}^{i} + W_{t}^{i}$  # Refer to Eq. (8)
22: else
23: for for i = 1 to  $n_{t}$  do:
24:  $TV_{t}^{i} \longleftarrow TV_{t-1}^{i}$ 
25:  $HV_{t}^{i} \longleftarrow HV_{t-1}^{i}$
</div>

## Acknowledgments

The authors would like to sincerely appreciate the helpful and valuable suggestions from the editor, associate editor and the other three reviewers. This work was supported by the National Natural Science Foundation of China (NSFC No. 71961007,71801117 and71973056). It was also supported in part by the Humanities and Social Sciences Project in Jiangxi Province of China (JJ18207 andJD19028) and Science and Technology Project of Education Department in Jiangxi Province of China (GJJ180278).

## Appendix A

## A.1. Wilson lower bound ranking approach

We introduce the Wilson lower bound ranking (WLB) approach briefly. This measure functions acceptably if TV is very large. Suppose one review has 5 HV and 0 unhelpful votes, whereas another has 100 HV and 1 non-HV. Directly adapting helpful ratio sorting will give a higher score to the former, even though the latter seems more reliable. Therefore, we should balance the helpful ratio with the uncertainty of a small TV. The well known solution was suggested by Wilson [42]. The key idea is to identify a conservative value that has a very small possibility of being larger thar the real helpful ratio. Specifically, we make the score equal to the lower bound of the real helpful ratio based on the observed TV and HV. Given a confidence level of 100(1 − α)%, <sup>i</sup>(WLB) is determined by the lower bound of the Wilson score interval [42], i.e.,

$$
\zeta_ {t} ^ {i} (\mathrm{WLB}) = \left\{ \begin{array}{l l} \frac {\mathrm{TV} _ {t} ^ {i}}{\mathrm{TV} _ {t} ^ {i} + z _ {\alpha} ^ {2}} \Bigg (\widehat {p} _ {t} ^ {i} + \frac {z _ {\alpha} ^ {2}}{2 \mathrm{TV} _ {t} ^ {i}} - z _ {\alpha} \sqrt {\frac {\widehat {p} _ {t} ^ {i} (1 - \widehat {p} _ {t} ^ {i})}{\mathrm{TV} _ {t} ^ {i}} + (\frac {z _ {\alpha}}{2 \mathrm{TV} _ {t} ^ {i}}) ^ {2}} \Bigg), & \text {if TV_{t} ^{i} >0}, \\ 0, & \text {if TV_{t} ^{i} = 0}, \end{array} \right.\tag{18}
$$

where $\widehat { \boldsymbol { p } } _ { t } ^ { i }$ is equal to $\mathrm { H V } _ { t } ^ { i } / \mathrm { T V } _ { t } ^ { i }$ and ${ z } _ { \alpha }$ is the (1 − α/2) quantile of a standard normal distribution.

According to Eq. (18), WLB suggests applying the observable TV and HV to estimate the true quality. Table Table A1 shows the results for WLB at both 90% and 95% confidence levels, which are denoted as WLB90 and WLB95, respectively. There are three notable features of WLB. First, the level of confidence does not afect the performance of WLB. Second, in terms of AHR or ρ, WLB is much better than MHF. For example, compared to ReSim $( S _ { 1 } , \mathrm { M H F } )$ , using WLB can improve AHR from 0.58 to approximately 0.65, while enhancing o from 0.40 to approximately 0.82. Third, although WLE

## Table A1

Evaluations for the Wilson lower bound ranking approach.

<table><tr><td rowspan="2">Experiments</td><td colspan="4">Basic information</td><td colspan="3">Evaluation criteria</td></tr><tr><td>N</td><td>Voters</td><td>TTV</td><td>THV</td><td>AHR</td><td> $\rho$ </td><td>PRZ</td></tr><tr><td colspan="8">Panel A: WLB with 90% confidence level</td></tr><tr><td>ReSim(S1, WLB90)</td><td>429.4(20.5)</td><td>2083.8(46.2)</td><td>39,795.1(938.0)</td><td>25,942.8(1325.0)</td><td>0.6519(0.0289)</td><td>0.8286(0.0462)</td><td>0.8658(0.0073)</td></tr><tr><td>ReSim(S3, WLB90)</td><td>258.5(15.8)</td><td>1264.6(35.8)</td><td>23,714.3(726.6)</td><td>15,096.8(886.2)</td><td>0.6366(0.0310)</td><td>0.8171(0.0493)</td><td>0.7878(0.0141)</td></tr><tr><td>ReSim(S5, WLB90)</td><td>428.9(20.3)</td><td>2084.5(44.6)</td><td>39,797.5(897.0)</td><td>23,041.5(908.2)</td><td>0.5790(0.0184)</td><td>0.7267(0.0604)</td><td>0.8659(0.0072)</td></tr><tr><td>ReSim(S8, WLB90)</td><td>430.0(20.1)</td><td>2081.6(48.2)</td><td>50,608.8(1258.4)</td><td>33,609.3(1278.0)</td><td>0.6641(0.0189)</td><td>0.7376(0.0313)</td><td>0.6131(0.0186)</td></tr><tr><td colspan="8">Panel B: WLB with 95% confidence level</td></tr><tr><td>ReSim(S1, WLB95)</td><td>428.5(21.1)</td><td>2081.9(44.5)</td><td>39,755.5(901.2)</td><td>25,920.5(1355.2)</td><td>0.6520(0.0302)</td><td>0.8139(0.0526)</td><td>0.8653(0.0076)</td></tr><tr><td>ReSim( $S_3$ , WLB95)</td><td>258.0(15.7)</td><td>1264.8(35.7)</td><td>23,705.7(718.8)</td><td>15,104.8(859.2)</td><td>0.6372(0.0303)</td><td>0.8060(0.0547)</td><td>0.7872(0.0142)</td></tr><tr><td>ReSim( $S_5$ , WLB95)</td><td>429.0(20.2)</td><td>2081.1(44.6)</td><td>39,734.9(907.1)</td><td>22,911.5(931.8)</td><td>0.5766(0.0192)</td><td>0.7038(0.0730)</td><td>0.8657(0.0074)</td></tr><tr><td>ReSim( $S_8$ , WLB95)</td><td>428.8(20.8)</td><td>2079.5(44.9)</td><td>50,555.5(1199.8)</td><td>33,451.1(1273.8)</td><td>0.6616(0.0189)</td><td>0.7229(0.0332)</td><td>0.6127(0.0191)</td></tr></table>

Note: This table shows the averages of the number of reviews, the number of voters, TTV, THV, AHR, $\rho ,$ and PRZ based on simulations. The standard deviations are displayed in corresponding parentheses.

succeeds in improving both AHR and $\boldsymbol { \rho }$ to a greater extent, it cannot reduce PRZ compared with MHF. Thus, we further consider BLB to ameliorate this defect.

## A.2. Using the criteria based on true quality

The true quality level is not observable in practical applications, so in our consideration, neither AHR nor ρ is related to $q ^ { i } .$ However, based on our simulation experiment, the true quality level of each review can be available in this artificial world. Therefore, we can define AHR\* as

$$
\mathrm{AHR} ^ {*} = \frac {\sum_ {i = 1} ^ {N} \mathrm{TV} _ {T} ^ {i} \times q ^ {i}}{\sum_ {i = 1} ^ {N} \mathrm{TV} _ {T} ^ {i}}.\tag{19}
$$

This criterion based on $q ^ { i }$ can be regarded as a kind of vote-weighted average of quality for all reviews. In addition, compared to $\rho ,$ we define $\rho ^ { * }$ as the correlation of $\mathrm { T V } _ { T } ^ { i }$ and $q ^ { i } .$ . Both criteria, AHR\* and $\rho ^ { * } ,$ can be used to evaluate performance in our experiments. We conclude that all results are similar to the corresponding results for AHR and $\rho ,$ and thus we do not provide further discussions but report them in Table Table A2. These result provide further evidence of the eligibility of adopting AHR and $\rho$ as our criteria.

Table A2  
Evaluations for all ranking approaches based on true quality.

<table><tr><td>Experiments</td><td>AHR*</td><td> $\rho^*$ </td></tr><tr><td colspan="3">MRF ranking approach (Table 4)</td></tr><tr><td>ReSim(S1, MRF)</td><td>0.5009 (0.0094)</td><td>0.0003 (0.0497)</td></tr><tr><td>ReSim(S2, MRF)</td><td>0.5002 (0.0093)</td><td>-0.0017 (0.0478)</td></tr><tr><td>ReSim(S3, MRF)</td><td>0.4999 (0.0117)</td><td>-0.0013 (0.0632)</td></tr><tr><td>ReSim(S4, MRF)</td><td>0.5002 (0.0088)</td><td>-0.0004 (0.0459)</td></tr><tr><td>ReSim(S5, MRF)</td><td>0.4998 (0.0053)</td><td>-0.0001 (0.0474)</td></tr><tr><td>ReSim(S6, MRF)</td><td>0.4999 (0.0094)</td><td>-0.0006 (0.0496)</td></tr><tr><td>ReSim(S7, MRF)</td><td>0.5003 (0.0092)</td><td>0.0020 (0.0478)</td></tr><tr><td>ReSim(S8, MRF)</td><td>0.4996 (0.0095)</td><td>-0.0003 (0.0476)</td></tr><tr><td colspan="3">MHF ranking approach (Table 4)</td></tr><tr><td>ReSim(S1, MRH)</td><td>0.5806 (0.0320)</td><td>0.3837 (0.1061)</td></tr><tr><td>ReSim(S2, MRH)</td><td>0.5806 (0.0327)</td><td>0.3835 (0.1069)</td></tr><tr><td>ReSim(S3, MRH)</td><td>0.5699 (0.0328)</td><td>0.3438 (0.1176)</td></tr><tr><td>ReSim(S4, MRH)</td><td>0.5823 (0.0331)</td><td>0.3920 (0.1048)</td></tr><tr><td>ReSim(S5, MRH)</td><td>0.5280 (0.0196)</td><td>0.2359 (0.1200)</td></tr><tr><td>ReSim(S6, MRH)</td><td>0.5789 (0.0327)</td><td>0.3648 (0.1077)</td></tr><tr><td>ReSim(S7, MRH)</td><td>0.5954 (0.0384)</td><td>0.3886 (0.1116)</td></tr><tr><td>ReSim(S8, MRH)</td><td>0.5798 (0.0216)</td><td>0.3043 (0.0627)</td></tr><tr><td colspan="3">HRF ranking approach (Table 4)</td></tr><tr><td>ReSim(S1, HRF)</td><td>0.7334 (0.0199)</td><td>0.6389 (0.0405)</td></tr><tr><td>ReSim(S2, HRF)</td><td>0.7335 (0.0201)</td><td>0.6401 (0.0408)</td></tr><tr><td>ReSim(S3, HRF)</td><td>0.7080 (0.0214)</td><td>0.6333 (0.0465)</td></tr><tr><td>ReSim(S4, HRF)</td><td>0.7394 (0.0192)</td><td>0.6413 (0.0399)</td></tr><tr><td>ReSim(S5, HRF)</td><td>0.6278 (0.0132)</td><td>0.5334 (0.0498)</td></tr><tr><td>ReSim(S6, HRF)</td><td>0.7413 (0.0192)</td><td>0.6394 (0.0383)</td></tr><tr><td>ReSim(S7, HRF)</td><td>0.7514 (0.0221)</td><td>0.6130 (0.0441)</td></tr><tr><td>ReSim(S8, HRF)</td><td>0.7044 (0.0155)</td><td>0.5929 (0.0265)</td></tr><tr><td colspan="3">BLB with  $\beta_H = \beta_N = 3$  (Table 5)</td></tr><tr><td>ReSim(S1, BLB3)</td><td>0.6858 (0.0251)</td><td>0.6836 (0.0549)</td></tr><tr><td>ReSim(S3, BLB3)</td><td>0.6665 (0.0256)</td><td>0.6651 (0.0588)</td></tr><tr><td>ReSim(S5, BLB3)</td><td>0.5890 (0.0174)</td><td>0.5923 (0.0750)</td></tr><tr><td>ReSim(S8, BLB3)</td><td>0.6791 (0.0172)</td><td>0.6141 (0.0332)</td></tr></table>

BLB with $\beta _ { H } = \beta _ { N } = 1 0$ (Table 5)  
(continued on next page)

Table A2 (continued)

<table><tr><td>Experiments</td><td>AHR*</td><td> $\rho^*$ </td></tr><tr><td>ReSim(S1, BLB10)</td><td>0.7016 (0.0227)</td><td>0.6455 (0.0498)</td></tr><tr><td>ReSim(S3, BLB10)</td><td>0.6801 (0.0237)</td><td>0.6307 (0.0555)</td></tr><tr><td>ReSim(S5, BLB10)</td><td>0.6013 (0.0159)</td><td>0.5544 (0.0635)</td></tr><tr><td>ReSim(S8, BLB10)</td><td>0.6857 (0.0150)</td><td>0.5711 (0.0289)</td></tr><tr><td colspan="3">BLB with  $\beta_H = \beta_N = 20$  (Table 5)</td></tr><tr><td>ReSim(S1, BLB20)</td><td>0.7048 (0.0224)</td><td>0.6267 (0.0477)</td></tr><tr><td>ReSim(S3, BLB20)</td><td>0.6851 (0.0221)</td><td>0.6121 (0.0524)</td></tr><tr><td>ReSim(S5, BLB20)</td><td>0.6063 (0.0156)</td><td>0.5379 (0.0592)</td></tr><tr><td>ReSim(S8, BLB20)</td><td>0.6874 (0.0152)</td><td>0.5507 (0.0290)</td></tr><tr><td colspan="3">BLB with  $\beta_H = \beta_N = 50$  (Table 5)</td></tr><tr><td>ReSim(S1, BLB50)</td><td>0.7091 (0.0208)</td><td>0.6055 (0.0450)</td></tr><tr><td>ReSim(S3, BLB50)</td><td>0.6871 (0.0215)</td><td>0.5909 (0.0471)</td></tr><tr><td>ReSim(S5, BLB50)</td><td>0.6118 (0.0146)</td><td>0.5246 (0.0563)</td></tr><tr><td>ReSim(S8, BLB50)</td><td>0.6872 (0.0146)</td><td>0.5276 (0.0271)</td></tr></table>

Note: This table shows the averages of AHR\* and $\rho ^ { * }$ based on simulations. The standard deviations are displayed in corresponding parentheses.

(a) HV = 1 and NV = 1  
![](/api/attachments/DD3JTA7K/fulltext/images/365283f24f1abf0904a793e83d39abd09c234443da9583c7f68da9a5de822c1d.jpg)

(b) $H V = 3 0 { \mathrm { ~ a n d ~ } } N V = 2 0$  
![](/api/attachments/DD3JTA7K/fulltext/images/558f54b4aa05ef29ff225b2071967b3bf069a8b1320f104c1fd80e0f742c02d6.jpg)  
Fig. A1. Plots of the ranking score.

## A.3. Examples of how ABLB works

We illustrate how ABLB works through the example of ReSim(S , ABLB3), where ABLB3 denotes ABLB with $\beta _ { H } = \beta _ { N } = 3$ . Fig. A1 shows the values of the ranking scores with diferent HV and NV. In panel (a), when R <sup>i</sup> has one HV and one non-HV $( \mathrm { H V } _ { t } ^ { i } = \mathrm { N V } _ { t } ^ { i } = 1 )$ , the ranking score is 0.225; whereas in panel (b), when $\mathrm { H V } _ { t } ^ { i } = 3 0 \mathrm { a n d N V } _ { t } ^ { i } = 2 0$ , the ranking score is 0.480. This figure obviously illustrates that larger HV and smaller NV result in a higher ranking score. Fig. A2 shows how HV and NV afect the extra scores. For $\mathrm { H } \mathbf { V } _ { t } ^ { i } = \mathbf { N } \mathbf { V } _ { t } ^ { i } = 1$ , the extra score is 0.333, as shown in panel (a). In panel (b), the extra score is only 0.130 when $\mathrm { H V } _ { t } ^ { i } = 2 0$ and $\mathrm { N V } _ { t } ^ { i } = 3 0$ . Therefore, when more votes appear, the extra score becomes smaller. Now we focus on two reviews, i.e., $R _ { t } ^ { 1 }$ and $R _ { t } ^ { 2 } .$ . Suppose $R _ { t } ^ { 1 }$ receives $\mathrm { H V } _ { t } ^ { i } = 3 0 , \mathrm { N V } _ { t } ^ { i } = 2 0$ , and $R _ { t } ^ { 2 }$ receives $\mathbf { H } \mathbf { V } _ { t } ^ { i } = \mathbf { N } \mathbf { V } _ { t } ^ { i } = 1$ , their ranking scores are 0.480 and 0.225, respectively. In other words, Rank(R<sup>1</sup>) < Rank(R <sup>2</sup>). However, based on ABLB, $R _ { t } ^ { 2 }$ has a certain possibility of obtaining an extra score of 0.333. If only $R _ { t } ^ { 2 }$ receives the extra score, its ranking score becomes 0.558, and $R _ { t } ^ { 2 }$ is sorted above $R _ { t } ^ { 1 }$

(a) HV = 1 and NV = 1  
![](/api/attachments/DD3JTA7K/fulltext/images/66ab897d1b32d717f3478650d959c10f3b2549c0b7b2090152f05fa0223f298b.jpg)

(b) HV = 20 and NV = 30  
![](/api/attachments/DD3JTA7K/fulltext/images/662c1b5d9c34bbc1f1048042a2a903f52e1d8789edf3f2727eeccfeea3cd37eb.jpg)  
Fig. A2. Plots of the extra score.

## References

[1] W. Duan. B. Gu. A.B. Whinston. Do online reviews matter? An empirical in: vestigation of panel data. Decis. Support Syst, 45 (2008) 1007–1016.

[2] C. Forman, A. Ghose, B. Wiesenfeld, Examining the relationship between reviews and sales: the role of reviewer identity disclosure in electronic markets, Inf. Syst. Res. 19 (2008) 291–313.

[3] X. Li. LM. Hitt, Self-selection and information role of online product reviews, Inf. Syst. Res, 19 (2008) 456–474.

[4] S.M. Mudambi, D. Schuff, What makes a helpful review? A study of customer re. views on amazon.com, MIS Q. 34 (2010) 185–200.

[5] J. Wu, Y. Wu, J. Sun, Z. Yang, User reviews and uncertainty assessment: a two stage model of consumers' willingness-to-pay in online markets, Decis, Support Syst. 55 (2013) 175–185.

[6] J. Wu, E.A.A. Gaytán, The role of online seller reviews and product price on buyers willingness-to-pay: a risk perspective, Eur. J. Inf. Syst. 22 (2013) 416–433.

[7] S. Basuroy, S. Chatterjee, S.A. Ravid, How critical are critical reviews? The box office effects of film critics, star power, and budgets, J. Mark, 67 (2003) 103–117.

[8] J.A. Chevalier, D. Mayzlin, The efect of word of mouth on sales: online book

reviews, J. Mark. Res. 43 (2006) 345–354.

[9] E.K. Clemons, G.G. Gao, L.M. Hitt, When online reviews meet hyperdiferentiation: a study of the craft beer industry, J. Manage. Inf. Syst. 23 (2006) 149–171.

[10] C. Dellarocas, X.M. Zhang, N.F. Awad, Exploring the value of online product reviews in forecasting sales: the case of motion pictures, J. Interact. Mark. 21 (2007) 23–45.

[11] V. Dhar, E.A. Chang, Does chatter matter? The impact of user-generated content on music sales, J. Interact. Mark. 23 (2009) 300–307.

[12] P.K. Chintagunta, S. Gopinath, S. Venkataraman, The efects of online user reviews on movie box ofice performance: accounting for sequential rollout and aggregation across local markets, Mark. Sci. 29 (2010) 944–957.

[13] A. Ghose, P.G. Ipeirotis, Estimating the helpfulness and economic impact of product reviews: mining text and reviewer characteristics, IEEE Trans. Knowl. Data Eng. 23 (2011).1498–1512

[14] X. Luo, J. Zhang, W. Duan, Social media and firm equity value, Inf. Syst. Res. 24 (2013)146–163.

[15] X. Luo, J. Zhang, How do consumer buzz and trafic in social media marketing predict the value of the firm? J. Manage. Inf, Syst. 30 (2013) 213–238.

[16] X. Luo, S. Raithel, M.A. Wiles, The impact of brand rating dispersion on firm value, J. Mark, Res, 50 (2013) 399–415

[17] D. Yin, S.D. Bond, H. Zhang, Anxious or angry? Efects of discrete emotions on the perceived helpfulness of online reviews, MIS Q. 38 (2014) 539–560.

[18] D. Weathers, S.D. Swain, V. Grover, Can online product reviews be more helpful?. examining characteristics of information content by product type, Decis. Support Syst, 79 (2015) 12–23.

[19] J. Wu, Review popularity and review helpfulness: a model for user review effectiveness, Decis, Support Syst, 97 (2017) 92–103.

[20] B.A. Sparks, V. Browning, The impact of online reviews on hotel booking intentions and perception of trust, Tour. Manage. 32 (2011) 1310–1323.

[21] P. Racherla, W. Friske, Perceived ‘usefulness’ of online consumer reviews: an exploratory investigation across three services categories, Electron. Commer. Res. Appl. 11 (2012) 548–559

[22] Z. Liu, S. Park, What makes a useful online review? Implication for travel product websites, Tour. Manage. 47 (2015) 140–151.

[23] N. Korfiatis, E. GarcíA-Bariocanal, S. Sánchez-Alonso, Evaluating content quality and helpfulness of online product reviews: the interplay of review helpfulness vs. review content, Electron. Commer. Res. Appl. 11 (2012) 205–217.

[24] A. Agnihotri, S. Bhattacharya, Online review helpfulness: role of qualitative factors, Psychol, Mark, 33 (2016) 1006–1017

[25] H. Baek, J. Ahn. Y. Choi, Helpfulness of online consumer reviews: readers' obiec: tives and review cues Int J Flectron Commer, 17 (2012) 99–126

[26] M. Salehan, D.J. Kim, Predicting the performance of online consumer reviews: a sentiment mining approach to big data analytics, Decis. Support Syst. 81 (2016) 30–40.

[27] A.Y. Chua, S. Banerjee, Helpfulness of user-generated reviews as a function of review sentiment, product type and information quality, Comput. Hum. Behav. 54 (2016) 547–554.

[28] M. Malik, A. Hussain, Helpfulness of product reviews as a function of discrete positive and negative emotions, Comput. Hum. Behav. 73 (2017) 290–302.

[29] J.P. Singh, S. Irani, N.P. Rana, Y.K. Dwivedi, S. Saumya, P.K. Roy, Predicting the “helpfulness” of online consumer reviews, J. Bus, Res, 70 (2017) 346–355.

[30] R.K. Merton, et al., The Matthew effect in science, Science 159 (1968) 56–63.

[31] Y. Wan, The Matthew effect in social commerce, Electron, Mark, 25 (2015)

313–324.

[32] A.Y. Chua, S. Banerjee, Analyzing review eficacy on amazon.com: does the rich grow richer? Comput. Hum. Behav. 75 (2017) 501–509.

[33] T. Hennig-Thurau, K.P. Gwinner, G. Walsh, D.D. Gremler, Electronic word-of-mouth via consumer-opinion platforms: what motivates consumers to articulate them: selves on the internet? J. Interact. Mark. 18 (2004) 38–52

[34] Y. Liu, Word of mouth for movies: its dynamics and impact on box ofice revenue, J. Mark. 70 (2006) 74–89.

[35] BrightLocal, Local Consumer Review Survey, (2016) accessed from www.brightlo cal.com/learn/local-consumer-review-survey.

[36] A.I. Schein, A. Popescul, L.H. Ungar, D.M. Pennock, Methods and metrics for coldstart recommendations, Proceedings of the 25th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, ACM, 2002, pp. 253–260.

[37] J. Bobadilla, F. Ortega, A. Hernando, J. Bernal, A collaborative filtering approach to mitigate the new user cold start problem, Knowl. Based Syst. 26 (2012) 225–238.

[38] Z. Chen, N.H. Lurie, Temporal contiguity and negativity bias in the impact of online word of mouth, J. Mark. Res. 50 (2013) 463–476.

[39] J. Bobadilla, F. Ortega, A. Hernando, A. Gutiérrez, Recommender systems survey, Knowl, Based Syst, 46 (2013) 109–132.

[40] B. Lika, K. Kolomvatsos, S. Hadjiefthymiades, Facing the cold start problem in re commender systems, Expert Syst. Appl. 41 (2014) 2065–2073.

[41] A.L.V. Pereira, E.R. Hruschka, Simultaneous co-clustering and learning to address the cold start problem in recommender systems, Knowl. Based Syst. 82 (2015) 11–19.

[42] E.B. Wilson, Probable inference, the law of succession, and statistical inference, J Am, Stat, Assoc. 22 (1927) 209–212.

Jying-Nan Wang is currently a professor in the faculty of College of International Finance and Trade, Zhejiang Yuexiu University of Foreign Languages, China. Dr. Wang received his Ph.D. in College of Management from Yuan Ze University. His research focuses on Business Intelligence Analysis, Market Microstructure, Risk Management, and Programming Trading. He has published a number of research papers in high quality refereed academic journals, including the Journal of Banking and Finance; the Journal of Empirical Finance; Econometric Reviews; Quantitative Finance; the Journal of Medical Internet Research; Electronic Commerce Research and Applications.

Jiangze Du is currently an associate professor in the School of Finance, Jiangxi University of Finance and Economics in China. Dr. Du obtained his Ph.D. degree in the Department of Management Sciences from the City University of Hong Kong. His current research interests include: Decision Support Systems, Online Data Analysis, and Financial Risk Management. His research has appeared in journals such as the Journal of Empirical Finance, Electronic Commerce Research and Applications, Economic Modelling.

Ya-Ling Chiu is currently an associate professor in the faculty of the College of International Business, Zhejiang Yuexiu University of Foreign Languages, China. Dr. Chiu received her Ph.D. in the College of Management from Yuan Ze University. Her research examines Online Word-of-Mouth Behavior and Online Community Behavior. She has published a number of research papers in high quality refereed academic journals, including the Journal of Business Research, International Marketing Review, the Journal of Business & Industrial Marketing, the Journal of Medical Internet Research, Electronic Commerce Research and Applications, and Assessment & Evaluation in Higher Education
