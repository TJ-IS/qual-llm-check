---
otero_id: 9320
otero_key: "BF8VDYHC"
title: "An Extensive Examination of Regression Models with a Binary Outcome Variable"
authors: "Suneel Chatla; Galit Shmueli"
year: "2017"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00455"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Volume 18 Issue 4

Article 1

4-28-2017

# An Extensive Examination of Regression Models with a Binary Outcome Variable

Suneel Babu Chatla , suneel.chatla@iss.nthu.edu.tw

Galit Shmueli

, galit.shmueli@iss.nthu.edu.tw

Follow this and additional works at: https://aisel.aisnet.org/jais

Research Paper

ISSN: 1536-9323

# An Extensive Examination of Regression Models with a Binary Outcome Variable

Suneel Babu Chatla

Institute of Service Science

Galit Shmueli

Institute of Service Science

National Tsing Hua University, Taiwan

suneel.chatla@iss.nthu.edu.tw

National Tsing Hua University, Taiwan

galit.shmueli@iss.nthu.edu.tw

## Abstract:

Linear regression is among the most popular statistical models in social sciences research, and researchers in various disciplines use linear probability models (LPMs)—linear regression models applied to a binary outcome. Surprisingly, LPMs are rare in the IS literature, where researchers typically use logit and probit models for binary outcomes. Researchers have examined specific aspects of LPMs’ but not thoroughly evaluated their practical pros and cons for different research goals under different scenarios. We perform an extensive simulation study to evaluate the advantages and dangers of LPMs, especially with respect to big data, which is now common in IS research. We evaluate LPMs for three common uses of binary outcome models: inference and estimation, prediction and classification, and selection bias. We compare its performance to logit and probit under different sample sizes, error distributions, and more. We find that coefficient directions, statistical significance, and marginal effects yield results similar to logit and probit. In addition, LPM estimators are consistent for the true parameters up to a multiplicative scalar. This scalar, although rarely required, can be estimated assuming an appropriate error distribution. For classification and selection bias, LPMs are on par with logit and probit models in terms of class separation and ranking and is a viable alternative in selection models. LPMs are lacking when the predicted probabilities are of interest because predicted probabilities can exceed the unit interval. We illustrate some of these results by modeling price in online auctions using data from eBay.

Keywords: Linear Regression, Linear Probability Model, Binary Outcome, Selection Bias, Estimation, Inference, Prediction, Big Data, Logit, Probit.

"Entities should not be multiplied unnecessarily.” (Occam’s razor)

## 1 Introduction and Motivation

Binary outcomes are common in the information systems (IS) literature. Among models for a binary dependent variable, logistic and probit regression models are the most commonly used in IS. These models are used for three main purposes:

1. Inference and estimation: estimating and testing the effect of covariates of interest on a binary outcome.

2. Classification: predicting the class or probability for new records.

3. Selection bias: estimating the selection model in propensity score matching and in the first stage of 2SLS models.

Among the many empirical IS studies that model binary dependent variables, the great majority use logistic regression for inference (e.g., Susarla, Subramanyam, and Kargade’s (2010) model renewal of outsourcing contracts (yes/no); Rishika, Kumar, Janakiraman, and Bezawada’s (2013) model social media participation; Asvanund, Clay, Krishnan, and Smith’s (2004) model song availability in P2P networks (available/unavailable); and Hui, Teo, and Lee’s (2007) model disclosure of private information by online users (yes/no)), logistic regression for selection bias using propensity score matching (e.g., Mithas & Krishnan, 2009; Rishika et al., 2013), and probit regression for selection bias using 2SLS (e.g., Kuan, Hui, Prasarnphanich, & Lai, 2015; Gopal & Koka., 2012; Kwon & Johnson., 2014; Liu, Brass, & Chen, 2014).

A linear probability model (LPM)—linear regression model applied to a binary dependent variable—is an alternative to logistic and probit regression models.

Notation: assume that we have ?? observations and ?? independent variables. We define the dependent variable $Z _ { n \times 1 } = { \left[ \begin{array} { l } { Z _ { 1 } } \\ { Z _ { 2 } } \\ { \vdots } \\ { Z _ { n } } \end{array} \right] } ,$ where $z _ { i } \in \{ 0 , 1 \}$ ; design matrix $X _ { n \times ( p + 1 ) } = { \left[ \begin{array} { l } { x _ { 1 } ^ { T } } \\ { x _ { 2 } ^ { T } } \\ { \vdots } \\ { x _ { n } ^ { T } } \end{array} \right] }$ , where $x _ { i } ^ { T } = \left[ \mathbb { 1 } x _ { i 1 } x _ { i 1 } \dots x _ { i p } \right] , i =$

$1 , 2 , \ldots , n ;$ parameter vector $\beta _ { ( p + 1 ) \times 1 } ;$ and error term $\varepsilon _ { n \times 1 } = { \left[ \begin{array} { l } { \varepsilon _ { 1 } } \\ { \varepsilon _ { 2 } } \\ { \vdots } \\ { \varepsilon _ { n } } \end{array} \right] } .$ . The LPM model is given by:

$$
Z = X \beta + \varepsilon ,\tag{1}
$$

or, using observation specific notation, $z _ { i } = x _ { i } ^ { T } \pmb { \beta } + \varepsilon _ { i }$ . The model is estimated using ordinary least squares (OLS).

LPMs are common in disciplines such as economics and political science for each of the three goals mentioned earlier: inference (e.g., McGarry, 2000; Fairlie & Sundstrom, 1998; Betts & Fairlie, 2001; Klaassen & Magnus, 2001; Lukashin, 2000), classification (e.g., Heckman & Snyder, 1996), and selection bias (Olsen, 1980). Yet, LPMs are rare in the IS literature.

## 1.1 LPMs in the Information Systems Literature

We conducted a full-text search<sup>1</sup> of binary dependent variable models in the journals Information Systems Research (1990 to September 2016), MIS Quarterly (1977 to September 2016), Journal of the Association for Information Systems (2003 to September 2016), and the IS section of Management Science (1954 to September 2016). We found 92 papers that modeled a binary dependent variable, but only eight of them used a LPM.

For example, Burtch, Ghose, and Wattal (2016) used a LPM to avoid the incidental parameter problem that the logit models have. Schlereth and Skiera (2017) considered a LPM to obtain the rankings for the choice probabilities as quickly as possible and because LPMs are very fast. Miller and Tucker (2009) used a LPM to study the diffusion of EMR technology using data from 2910 hospitals. Forman, Ghose, and Wiesenfeld (2008) used a LPM to model the presence of identity-disclosure information in online reviews present/absent) applied to over 160,000 book reviews on Amazon.com. Forman, Ghose, and Goldfarb (2009) used a LPM to model data from Amazon.com on the top-selling books for 1,497 unique locations in the United States for 10 months in order to evaluate the effect of customers’ locations on their online/offline shopping choice. Adjerid, Acquisti, Teland, Padman, and Adler-Milstein (2015) used a LPM for both cross sectional (survey) and panel (6 years) datasets. Ceccagnoli, Forman, Huang, and Wu (2012) used a LPM to model a panel dataset on 1,210 small independent software vendors (ISV) over the 1996-2004 period to study how participation in an ecosystem partnership improves the business performance of the small ISVs. These five papers used LPMs for inference. Table 1 summarizes our literature search results, and Table A1 presents them in more detail.

Table 1. Summary of IS Literature Survey of Binary Outcome Models

<table><tr><td>Modeling goal</td><td>Number of papers</td></tr><tr><td>Inference/estimation</td><td>54</td></tr><tr><td>Selection bias (2SLS + PSM)</td><td>27</td></tr><tr><td>Classification/prediction</td><td>3</td></tr><tr><td>Inference/estimation + classification/prediction</td><td>2</td></tr><tr><td>Inference/estimation + selection bias</td><td>4</td></tr><tr><td>Endogeneity (2SLS)</td><td>1</td></tr><tr><td>Inference + endogeneity (2SLS)</td><td>1</td></tr><tr><td>Total</td><td>92</td></tr></table>

## 1.2 LPM in Big Data

In the realm of big data where large samples are available, researchers have claimed that LPMs produce qualitatively similar results to both logistic and probit regression models (Gordon, Lin, Osberg, & Phipps, 1994; Betts & Fairlie, 2001). Large samples are now becoming popular in IS studies, and many IS researchers have begun to focus on working with big data. Thought leaders and editors of leading IS journals see much reason for optimism regarding big data’s impact on the IS discipline (Abbasi, Sarker, & Chiang, 2016; Agarwal & Dhar, 2014). Advances in technology have brought us the ability to collect, transfer, and store large data sets. Thanks to this, a growing number of empirical studies published in information systems and related disciplines now rely on very large samples (Lin, Lucas, & Shmueli, 2013). Among those studies, some have a binary outcome. For example, Özpolat, Gao, Jank, and Viswanathan (2013) used a logit model to study the presence/absence of online trust seals using over 9000 online shopping sessions; Overby and Jap (2009) analyzed over 100,000 used vehicles in the wholesale automotive market using probit models to study virtual versus physical vehicle presentation by the seller and physical versus virtual presence of the buyer. Asvanund et al. (2004) use a probit regression to model song availability in a P2P network for over 160,000 songs. Only a single large-sample binary-outcome paper used a LPM (Forman et al., 2008). Therefore, we are interested in evaluating the performance of a LPM against its alternatives also in the case of large samples.

## 1.3 Goal of This Study

In this paper, we examine the performance of LPMs with respect to large samples. We start by describing the advantages and weaknesses of LPMs based on examining the literature on them in different areas. Since the literature is inconclusive, we examine and evaluate LPMs’ strengths and weaknesses through an extensive simulation study.

We consider and examine LPMs’ components that one uses for inference and estimation, classification and prediction, and selection bias: coefficients (in terms of bias and consistency) and fitted/predicted values. We then examine how these components affect the three goals. In doing so, we provide researchers and practitioners with an understanding of when LPMs are useful, when they are not, and what they should expect under different scenarios.

The paper proceeds as follows: in Section 2, we describe the criticisms, controversies, and justifications surrounding using LPMs as they appear in the extant literature. In Section 3, we provide theoretical results regarding consistency of the estimators, marginal effects, predicted values, and classification. In Section 4, we describe the simulation study (in which we compared LPMs with logit and probit models in terms of coefficient estimation, significance, prediction, and selection models) and its results. In Section 5, we illustrate some of these results using a real dataset on online auctions. In Section 6, we summarize our results, offer directions for future research, and conclude the paper.

## 2 Criticism of, Controversy about, and Justification for LPMs in the Literature

## 2.1 Criticisms of LPMs

Estimating LPMs using ordinary least squares (OLS) has four main problems (Maddala, 1986):

1. Non-normal error term: for a binary dependent variable, the error term $\varepsilon _ { \mathrm { i } }$ can only take two values: $\varepsilon _ { \mathrm { i } } = 1 - \mathrm { x _ { i } ^ { T } } \beta \mathrm { i } \mathrm { f } \mathrm { z _ { i } } = 1$ and $\boldsymbol { \mathfrak { \varepsilon } } _ { \mathrm { i } } = - \mathbf {  { x } } _ { \mathrm { i } } ^ { \mathrm { T } } \boldsymbol { \beta } \mathrm { \ i f \ } \mathbf { z } _ { \mathrm { i } } = 0$ . Hence the normality assumption cannot be valid.

2. Non-constant error variance: the variance for a binary outcome is given by $\sigma _ { \mathrm { i } } ^ { 2 } = \mathrm { E [ z _ { \mathrm { i } } ] ( 1 - E [ z _ { \mathrm { i } } ] ) }$ . Since E[z ] is a function of ${ \mathrm { X i , } }$ the variance varies for different levels of X and, thus, the homoscedasticity assumption is violated.

3. Constraints on the response function: since E[z<sub>i</sub>] represents probabilities, they should be constrained between 0 and $1 ( \mathsf { i . e . , 0 } \leq \mathrm { E [ z _ { i } ] } \leq 1 )$ . However, the LPM does not institute this constraint.

4. Functional form: since the model is linear, a unit increase in one of the covariates of ?? (say, $x _ { k } )$ is interpreted as a constant change of $\beta _ { k }$ in the probability of an event while holding the remaining covariates constant. The magnitude change should be constant regardless of the current value of $x _ { k }$ . In many applications, however, this is unrealistic. In general, when the outcome is a probability, it is reasonable that the effects of covariates will diminish as the predicted probability approaches 0 or 1. Long and Freese (2006) states that this problem is the most serious one with LPMs.

Given these four issues, conventional advice (Gordon et al., 1994) suggests using generalized linear models (GLMs) with logit or probit link functions to overcome all four issues. By choosing a sigmoidal curve or an inverse normal cumulative distribution function (ICDF) as a functional form, one overcomes all of the above limitations. The logit and probit links are symmetric and can produce diminishing effects as the probability approaches 0 or 1, and they mostly differ from each other at the tails. For small samples, both techniques produce similar results, but, as the sample size increases, the differences are more evident (Gordon et al., 1994). For an asymmetric link function, the literature suggests using a complementary log-log function.

Since one does not encounter the above four problems with logit or probit models, the latter have become the common choice for modeling binary outcomes. While there is an additional cost of computational complexity when using logit/probit models, that cost is practically negligible due to the advancements in computational power.

## 2.2 Debate about the Criticism in the Literature

The statistical arguments against using linear regression with a binary dependent variable are not as decisive as research has often claimed (Hellevik, 2009). Several papers discuss the impact of each of the four issues in Section 2.1 on inference and prediction, which makes the criticism of LPMs a more debatable issue.

In terms of non-normal error terms (challenge #1), OLS provides estimators that are asymptotically normal under quite general conditions even if the distribution of the error terms is far from normal. With a large sample, this challenge is, therefore, mute (Aldrich & Nelson, 1984; Long & Freese (2006).

The non-constant error variance (challenge #2) is of no consequence for the regression coefficient, but the uncertainty estimate for the coefficient and, thus, the test of significance is affected (Hellevik, 2009). In studies interested in inference, the literature suggests substituting OLS estimation with weighted least squares (WLS) to estimate the model. This two-stage procedure first produces fitted values $\hat { \boldsymbol { z } } _ { i } = x _ { i } ^ { T } \hat { \boldsymbol { \beta } }$ $( \mathsf { i } \mathsf { = } 1 , \ldots , \mathsf { n } )$ from the OLS estimation and then re-estimates the model using WLS with weights $w _ { i } =$ $1 / \sqrt { \hat { z } _ { i } \left( 1 - \hat { z } _ { i } \right) }$ (Goldberger, 1964).

The implication of the unconstrained response function (challenge #3) is that predicted values, which reflect probabilities, are not constrained to the unit interval. Friedman et al. (2009, p. 103) comment about an unconstrained response function’s impact on classification as follows: “these violations themselves do not guarantee that this approach will not work, and in fact on many problems it gives similar results to more standard linear methods for classification”. In other words, when one uses the probabilities for classification, one is interested only in comparing $\mathsf { P } ( z _ { i } = 1 )$ to $\mathsf { P } ( z _ { i } { = } 0 )$ and classifying the observation to the class with the higher probability.

When one focuses on the probability itself, then values beyond the unit interval are problematic. The ad hoc solution to this problem is simply replacing values above 1 with 1 and values below 0 with 0 (Mukras, 1993). As Figure A5 shows, whenever LPMs produce unbounded predictions, both logistic and probit models produce predictions equal exactly to 1 or 0. Hence, it is indeed reasonable to replace the unbounded predictions with either 0 or 1. Unbounded predictions can also cause problems while calculating weights for WLS (for addressing challenge #2). To solve the problem of calculating weights for WLS, researchers suggest replacing predictions above 1 with 0.999 and predictions below 0 with 0.001 (Aldrich & Nelson, 1984), which guarantees positive weights as WLS requires. In general, the percentage of unbounded predictions produced by LPMs is small, and they mainly happen due to outliers in the data (high leverage and influential observations). Hence, rounding off predictions would actually improve the LPM standard errors, which both logistic and probit models do by default.

When LPMs produce many unbounded predictions, it might indicate either an underspecified model (Friedman et al. 2009) or LPMs’ inadequacy. Unbounded predictions will affect both inference and prediction. The functional form issue (challenge #4), which is based on the claim that the effect of covariates on the probability more realistically diminishes near 0 or 1 rather than behaves linearly, relates more directly to LPMs’ inadequacy. One can base these claims on either theoretical considerations or empirical tests. For example, if there are many unbounded predictions, then a linear specification may not be appropriate. However, there is no empirical evidence on what percentage of unbounded predictions one can use to decide about whether to use a LPM.

## 2.3 Justification for the LPM

In their book Mostly Harmless Econometrics, Angrist and Pischke (2008) discuss LPMs’ theoretical and practical advantages compared to GLMs such as logistic and probit models in terms of linking inference with causality and causally interpreting regression coefficients. They conclude (p. 107):

While nonlinear models may fit the [conditional expectation function] more closely than a linear model, when it comes to marginal effect this probably matters little…. Nonlinear models require a number of decisions along the way (e.g., the weighting scheme, derivatives vs. finite differences), while OLS is standardized. Nonlinear life also gets considerably more complicated when we work with instrumental variables and panel data. Finally, extra complexity comes into the inference step as well, since we need standard errors for marginal effects.

Hellevik (2009) further notes that one cannot apply loglinear measures in causal analyses since they do not accurately describe (multivariate) associations.

Because typically one does not know the underlying true model, one can choose a model—whether logistic, probit, or linear probability model—based only on an approximation. Thus, one might ask how choosing the “wrong” model harms the results. Angrist and Pischke (2012, July 09) state:

The LPM won’t give the true marginal effects from the right nonlinear model. But then, the same is true for the wrong nonlinear model! The fact that we have a probit, a logit, and the LPM is just a statement to the fact that we don’t know what the “right model is. Hence, there is a lot to be said for sticking to a linear regression function as compared to a fairly arbitrary choice of a non-linear one!

Li and Duan (1989) show that one can still obtain consistent estimators for the regression parameters even under link violation as long as the covariates are spherically distributed (e.g., follow a normal distribution) along with some other conditions. However, when the data are far from normally distributed (e.g., heavily skewed), the coefficients estimated from either probit or logit models will differ from the true values.

In some cases, only LPMs allow model estimation. Specifically, one can estimate coefficients of some dummy variables in a LPM but not in a logistic or probit regression model (Anderson, 1987; Caudill, 1987).

For example, one cannot estimate observation-specific dummies and group-specific dummies, where all members of the group belong to the same class, with either logit or probit models. While this phenomenon is rare in cross sectional studies, it is quite common in panel data studies. This phenomenon is also probably one of the reasons behind why many panel studies choose LPM over either logit or probit models (Forman et al, 2008; Adjerid et al., 2015); with a LPM, one can estimate these effects quite comfortably. Similarly, both logit and probit run into problems when a complete or quasi-separation exists in the data.

Multiple authors point to LPMs’ interpretational advantage over non-linear models, especially when the model includes interaction terms. McGarry (2000) appeals to the ease of interpreting estimated marginal effects. Fairlie and Sundstrom (1998) prefer LPMs due to the ease with which one can interpret coefficients.

Wooldridge (2010, p. 455) also advocates using a LPM when one seeks estimation or inference:

If the main purpose is to estimate the partial effect of [the covariate] on the response probability, averaged across the distribution of [the covariates], then the fact that some predicted values are outside the unit interval may not be very important.

With a large sample, researchers have claimed LPMs to produce qualitatively similar results to both logistic and probit regression models (Gordon et al., 1994; Betts & Fairlie, 2001). Existing research on selection bias showcases the successful use of LPM. The two-stage least squares (2SLS) approach for selection bias comprises the following two models:

1. Selection model: $S ^ { * } { } _ { n \times 1 } = W _ { n \times ( k + 1 ) } \gamma + \omega _ { n \times 1 }$ , where $S ^ { * }$ is latent and we observe $S = 1 \mathrm { \ i f \ } S ^ { * } \geq$ 0and $S = 0$ otherwise. We assume there are only $m < n$ observations with ?? = 1.

2. Outcome model: $Y _ { m \times 1 } = X _ { m \times ( p + 1 ) } \beta + \varepsilon _ { m \times 1 }$ , where ?? is observed only if ?? = 1. While it is not uncommon to use the same set of covariates in both the models $( \mathsf { i . e . , } W = X )$ , it is preferable to use at least one different covariate than the covariates in outcome model.

If we assume both errors $( \omega , \varepsilon )$ follow a bivariate normal distribution, then we can estimate the above model using ordinary likelihood based methods that require solving an iterative algorithm. Heckman (1979) paved the way for the prevalence of methods for correcting sample selection bias. Heckman simplified the above complex Maximum likelihood (ML)-based estimation procedure into two simple steps: 1) estimate the selection model with a probit model and calculate the inverse Mills ratio $\begin{array} { r } { ( { \mathsf { I M R } } = \frac { \emptyset ( \mathbf { W } \widehat { \gamma } ) } { \Phi ( \mathbf { W } \widehat { \gamma } ) } , } \end{array}$ where Φ is the standard normal density and Φ is the standard normal CDF); and 2) estimate the outcome model, which includes the IMR as an extra covariate to control for selection bias. Olsen (1980) further simplified the estimation by replacing the probit selection model with a LPM and using the fitted values (Wγ̂ − 1)) directly in the outcome model as an extra predictor. Olsen’s LPM approach requires that the conditional expectation of ??|?? is linear in ?? , and this assumption is more flexible than the bivariate normality required for Heckman’s approach. While some researchers have criticized Olsen’s approach for using a LPM, others have showed that the two approaches yield identical results (Wooldridge, 2010; Olsen, 1980; Angrist & Pischke, 2008).

In the context of endogeneity, when one uses 2SLS for handling a binary endogenous variable, the advantage of using LPM in the first stage is that plugging the first-stage fitted values into the second stage regression results in consistent 2SLS estimates. Using a nonlinear model in the first stage to increase the 2SLS estimate efficiency requires special care to avoid “forbidden regressions” (typically done by treating the first-stage fitted values as instruments). Angrist and Pischke (2008, p. 191) conclude: “Use of a nonlinear plug-in first-stage may not do too much damage in practice—a probit first-stage can be pretty close to linear—but why take a chance when you don’t have $\mathbf { t o } { \dot { ? } } "$

Lastly, another advantage of LPMs is computational: least squares estimation is computationally cheaper than the ML method used for estimating logistic or probit regression models. ML relies on an iterative algorithm that is sequential in nature and, therefore, difficult to parallelize (Yahav, Shmueli, & Mani, 2016). This computational advantage is not a big concern given today’s computing power. However, there are situations where even a small gain in time is meaningful.

## 3 LPMs for Estimation and Inference vs. Fitted and Predicted Values

Proponents and critics of LPMs typically rest their claims on theoretical or practical arguments that affect statistical inference, parameter estimation, and prediction. Statistical significance and parameter estimation are relevant to the goals of inference, while prediction is relevant to the goals of classification and selection bias. Therefore, we distinguish between the scenarios of explanatory modeling where one focuses on parameter estimation and statistical inference and predictive modeling where one focuses on predicted values (Shmueli, 2010; Shmueli & Koppius, 2011). For example, some studies show that, in large samples, LPMs produce results “similar” to logistic and probit regression models. Researchers sometimes measure similarity in terms of prediction accuracy (Gordon et al., 1994) and, at other times, in terms of statistical significance (Hellevik, 2009).

Given the two different contexts and the different uses of binary outcome models, we examine and summarize results regarding the following quantities: coefficient bias, marginal effects, fitted/predicted probabilities, and classifications.

## 3.1 Formulation of the Binary Outcome Scenario

Coefficient bias and interpretation are major concerns when one seeks parameter estimation. In the statistics literature, one possible way to motivate binary variable models is to assume that there exists an underlying latent continuous variable that has been discretized so that one only observes the discretized (binary) version.

Assume the true underlying model with continuous dependent variable is as follows:

$$
Y _ {n \times 1} = X _ {n \times (p + 1)} \beta_ {(p + 1) \times 1} + \varepsilon_ {n \times 1}, \quad \varepsilon_ {i} \sim f (0, \sigma^ {2}),\tag{2}
$$

where $f \ ( . ) = \mathsf { a n y }$ symmetric continuous density and Y is a latent continuous variable, we observe only:

$$
Z = \left\{ \begin{array}{l l} 1, & \text {if} Y > 0 \\ 0, & \text {if} Y <   0 \end{array} \right.\tag{3}
$$

Based on the error distribution $\boldsymbol { \mathfrak { f } } ( . )$ , we select the model to estimate the parameters of interest. For simplicity, let us consider f = {uniform, logistic, normal}. Figure 1 illustrates the similarity of these three distributions when they have mean zero and variance equal to one. Ideally, one would fit a probit model if the errors arise from a standard normal distribution and a logistic regression if the errors arise from a standard logistic distribution. Although not as popular, one would fit a linear probability model if the errors arise from a standard uniform distribution. From Equations 2 and 3, we can write:

$$
E [ Z | X ] = \mathcal {F} (X \beta),\tag{4}
$$

where $\mathcal { F } \left( . \right)$ is the cumulative distribution function (CDF) for the density $f \left( . \right)$ in Equation 2. Both logistic (logit) and probit models assume the random variable ?? follows a Bernoulli distribution with the probability defined in Equation 4, and we estimate parameters using MLE. It is well known that, under some regularity conditions, the ML estimators are consistent $( { \widehat { \beta } } \ { \overset { p } {  } } \beta )$ . However, although we estimate Equation 4 to retrieve the estimates for the original model in Equation 2, one has to interpret the resulting coefficients completely differently from how one should interpret the original coefficients due to $Y ^ { \prime } { \sf s }$ unobserved nature and the fact that one draws interpretations with respect to the observed binary ??.

![](/api/attachments/BF8VDYHC/fulltext/images/04310450270fd7e7de188bccebbecacab03032e6004eabc3e5adbc78353fa305.jpg)

![](/api/attachments/BF8VDYHC/fulltext/images/894cc6fffc183cd3da59501a4e9a379f1ddea01b93c4da94e4921bd6caba1687.jpg)  
Figure 1. Density (Left) and CDF (Right) for Three Distributions: N(0,1), logistic(0, ${ \frac { \sqrt { 3 } } { \pi } } )$ ), and $\mathsf { U } ( - \sqrt { 3 } ,$ √3)

In contrast, a LPM is simply a linear model that regresses ?? on ?? as follows:

$$
Z = X \beta_ {b} + \varepsilon_ {b},\tag{5}
$$

with the least squares estimator for $\beta _ { b }$ obtained as $\widehat { \beta } _ { b } = \left( X ^ { T } X \right) ^ { - 1 } X ^ { T } Z .$

## 3.2 Relationship with the true coefficients

Let us consider the bias of the least squares LPM estimator ${ \widehat { \beta } } _ { b }$ :

$$
\begin{array}{c} E \big [ \hat {\beta} _ {b} - \beta | X \big ] = (X ^ {T} X) ^ {- 1} X ^ {T} E [ Z | X ] - \beta \\ = \big (X ^ {T} X \big) ^ {- 1} X ^ {T} \mathcal {F} \big (X \beta \big) - \beta \end{array}\tag{6}
$$

The above bias will become zero if the errors (??) in Equation 2 arise from a standard uniform distribution. In practice, one does not often encounter errors from a standard uniform distribution with small samples. Therefore, LPM estimates are typically biased in a small sample. However, research has proven that the LPM estimators are consistent (in proportion), which means that the estimator converges to the true value (in proportion) as sample size increases.

Applying linear regression to a binary dependent variable is not new. Fisher (1936) showed that the coefficients from a discriminant analysis are proportional to the coefficients obtained by fitting a LPM to the binary dependent variable that denotes the class membership for the observations (see also Duda, Hart, & Stork, 2012, Section 5.8.2). Continuing this line of research, Haggstrom (1983) provided the relationships between the LPM and logistic regression coefficients and between the two models’ standard errors for the special case when the independent variables follow a multivariate normal distribution. Billinger (2012) showed that, under some regularity conditions, the LPM estimators are strongly consistent for the true parameters up to a multiplicative scalar ((??)) $( \mathbf { \sigma } ( \beta _ { b } \propto \beta \mathbf { \sigma } \implies \beta _ { b } = k \beta ) )$ . While the strong consistency property requires the covariates to be normality distributed, research has shown that the result holds even under weak conditions (e.g., Duan & Li, 1991). In addition, Li and Duan (1989) showed that the directions of the LPM estimators are consistent with the directions of the parameters from the true model.

We now describe methods for calculating the multiplicative scalar (k) for LPM estimates under some assumptions on the error distributions in Equation 2.

Case 1: uniformly distributed errors:

Let us assume that $\varepsilon \sim f ( . ) = U ( - \sigma \sqrt { 3 } , \sigma \sqrt { 3 } )$ , which means the errors have mean 0 and variance $\sigma ^ { 2 }$ . This assumption is consistent with other standard models such as probit $( N ( \mu = 0 , \sigma ^ { 2 } = 1 ) )$ .

From Equation 6, we can see that:

$$
E \big [ \hat {\beta} _ {b} | X \big ] = \beta_ {b} = (X ^ {T} X) ^ {- 1} X ^ {T} \left(\frac {X \beta + \sigma \sqrt {3}}{2 \sigma \sqrt {3}}\right)\tag{7}
$$

The LPM parameters are, therefore, linearly related to the true parameters. Since both sets of parameters $( \beta _ { b }$ and $\beta )$ are linear in $\mathsf { X } ,$ we can recover the true parameters $( \beta )$ in a straightforward manner.

## Case 2: normally distributed errors:

Let us assume that $\varepsilon \sim f ( . ) = N ( 0 , \sigma ^ { 2 } )$ and it follows that $Y | X \sim N ( X \beta , \sigma ^ { 2 } )$ . Again, from Equation 6, we can get:

$$
E \big [ \hat {\beta} _ {b} \big | X \big ] = \beta_ {b} = (X ^ {T} X) ^ {- 1} X ^ {T} \Phi \left(\frac {X \beta}{\sigma}\right),\tag{8}
$$

where $\Phi ( . )$ is the standard normal CDF. Since $\Phi ( . )$ is a non-linear function, we cannot recover the true parameters $( \beta )$ as simply as from Equation 7. However, we can find an approximation by exploiting the normality assumption. The correlation between a standard normal variable and its standard dichotomized version is $\sqrt { \frac { 2 } { \pi } }$ (Vargha, Rudas, & Delaney, 1996), which implies that the LPM parameters $\beta _ { b }$ are discounted by this scalar when the variables are standardized. One can extend this correction to nonstandardized variables as follows:

$$
\beta_ {b} = \sqrt {\frac {2}{\pi}} \frac {\sigma_ {b}}{\sigma} \beta ,\tag{9}
$$

where $\sigma _ { b }$ is the standard deviation for ??.

Case 3: logistic distributed errors:

We can approximate the standard logistic distribution with $\begin{array} { r } { \mathcal { F } ( \varepsilon ) \approx \Phi \left( \frac { \varepsilon } { 1 . 7 } \right) } \end{array}$ (Johnson & Kotz, 1970). Hence, we can use the same correction that Equation 9 uses. However, to be more precise, we follow the same approach used to derive the correction factor for normally distributed errors and derive the correction factor for logistic errors<sup>2</sup> as:

$$
\beta_ {b} = 0. 7 6 2 \frac {\sigma_ {b}}{\sigma} \beta ,\tag{10}
$$

where $\sigma _ { b }$ is the standard deviation for ??.

In summary, the LPM estimators are consistent for the true parameters up to a multiplicative scalar(??), and one can calculate the scalar if one has a reasonable estimate of ??. By assuming the appropriate error distribution, one can apply the above corrections to retrieve the coefficients from the underlying continuous outcome model. Based on our empirical analysis, we observed that the normal correction (case 2) works well most of the time. While the three corrections produce similar results, they might differ if the data has many outliers and is highly skewed.

## 3.3 Marginal Effects

The point estimates for the coefficients are important for drawing inferences. However, researchers who use nonlinear binary variable models (e.g., logit/probit) often do not interpret the coefficients because one cannot interpret their coefficients as straightforwardly as OLS coefficients. The marginal effects (the amount of relative change in the dependent variable due to a unit change in a covariate) and the probabilities are key to understanding the relationships of interest in the population. Since both probit and logit models are nonlinear, the size of the effect of a change in the independent variable of interest depends on the values of other independent variables. While the least squares estimates from Equation 5 are directly the marginal effects for LPM, one calculates the marginal effects for logit models as:

$$
\mathsf {M E f o r} x _ {i k} = \frac {\partial E [ z _ {i} ]}{\partial x _ {k}} = \frac {e ^ {x _ {i} ^ {T} \beta}}{(1 + e ^ {x _ {i} ^ {T} \beta}) ^ {2}} \beta_ {\mathrm{k}}\tag{11}
$$

And for probit models as:

$$
\mathsf {M E f o r} x _ {i k} = \frac {\partial E [ z _ {i} ]}{\partial x _ {k}} = \phi (x _ {i} ^ {T} \beta) \beta_ {\mathrm{k}},\tag{12}
$$

where ∅ (.) is the density for a standard normal distribution.

In practice, one can approximate the effects in Equations 11 and 12 using their sample estimates as Equations 13 and 14, respectively, show:

$$
\widehat {M E} _ {i k} \approx A v e r a g e \left[ \frac {e ^ {x _ {i} ^ {T}} \widehat {\beta}}{(1 + e ^ {x _ {i} ^ {T} \widehat {\beta}}) ^ {2}} \right] \widehat {\beta} _ {k}\tag{13}
$$

$$
\widehat {M E} _ {i k} \approx A v e r a g e [ \phi (x _ {i} ^ {T} \hat {\beta}) ] \widehat {\beta} _ {k}\tag{14}
$$

Although the marginal effects from the above three models look different in form, numerically, they are practically the same (e.g., Angrist & Pischke, 2008, p.107), which is one reason that we use a LPM despite its drawbacks.

## 3.4 Fitted/Predicted Values and Classification

As we mention earlier, predicted probabilities from a LPM might exceed the unit interval; while not a concern when one seeks to estimate and test parameters, it is important when one is interested in the estimated or predicted probability. Therefore, the biggest concern is the functional form for which it might be inappropriate to assume a linear effect of covariates on $P ( z _ { i } = 1 )$ ). The linear form might also pose challenges to generating accurate predictions for values near 0 or 1. In theory, one can extend the model (in terms of predictors) in such a way that the fitted values or predicted probabilities will remain between zero and one (Friedman, Hastie, & Tibshirani, 2009).

As Table 1 shows, research in the IS literature has mostly used fitted values from binary outcome models to account for selection bias. While studies that estimate selection models and instrumental variable models in 2SLS models often use probit models, studies that use propensity score matching tend to use logit models (in PSM with a binary treatment variable, researchers such as Caliendo (2006) have established that logit and probit models lead to similar results). Although rare in IS studies, we note that LPMs are a viable alternative to probit models in selection models (Wooldridge, 2010; Olsen, 1980; Angrist & Pischke, 2008).

As Westin (1974) points out, LPM generally does not provide much help for predicting probabilities because it yields unbounded predictions. Yet, if one uses the predictions as an intermediary step where what matters is their ordering, then LPM is a viable alternative to logit and probit models. Two such cases include 1) the classification of new observations, where one converts the probability into a binary classification depending whether $P ( z _ { i } = 1 )$ or $P ( z _ { i } = 0 )$ is larger; and 2) selection models, where one uses the fitted probabilities for matching treatment and control observations (in PSM) or as a covariate in the outcome model (2SLS). We investigate these cases, which are useful in many empirical studies.

## 4 Simulation Study

To evaluate LPM for the three types of study goals (inference and estimation, classification, and selection bias), we created two simulation setups: one focuses on the estimated model and the other on fitted/predicted values. We used the first setup to evaluate inference and estimation and the second setup to evaluate classification and selection bias.

In addition, we also evaluated the effect of sample size so that our results are useful for today’s big data studies. To do so, we generated three sample sizes for each of the scenarios: a small sample, a medium sample, and a very large sample.

## 4.1 Inference and Estimation

## 4.1.1 Simulation Design

We generate a population of total sample size $\mathsf { n } = 1 , 0 0 0 , 0 0 0$ . The simulation process is:

Step 1: generate 4 covariates, simulated as follows: $x _ { 1 } \sim U { \left( - 1 , 1 \right) } , x _ { 2 } \sim N ( 0 , 0 . 1 ^ { 2 } )$ , and $x _ { 3 } , x _ { 4 }$ from a bivariate normal distribution with means zeros and covariance matrix $\begin{array} { r l } { \binom { 0 . 5 } { - 0 . 3 } } & { { } - 0 . 3 } \\ { \qquad - 0 . 3 } & { { } 0 . 5 } \end{array}$

Step 2: generate error variables from each of the following three standard error distributions: $\varepsilon _ { 1 } { \sim } N \big ( 0 , 1 \big ) , \varepsilon _ { 2 } { \sim } L o g i s t i c ( 0 , 1 )$ , and $\varepsilon _ { 3 } \sim U ( 0 , 1 )$ .

Step 3: calculate three latent (dependent) variables that correspond to the three error distributions and use the fixed parameter values ${ \boldsymbol { \beta } } _ { 0 } = 0 , { \boldsymbol { \beta } } _ { 1 } = 1 , { \boldsymbol { \beta } } _ { 2 } = - 1 , { \boldsymbol { \beta } } _ { 3 } = 0 . 5 , { \boldsymbol { \beta } } _ { 4 } = - 0 . 5 ;$

$$
\begin{array}{r l} & {Y _ {1} = \beta_ {0} + \beta_ {1} x _ {1} + \beta_ {2} x _ {2} + \beta_ {3} x _ {3} + \beta_ {4} x _ {4} + \varepsilon_ {1}} \\ & {Y _ {2} = \beta_ {0} + \beta_ {1} x _ {1} + \beta_ {2} x _ {2} + \beta_ {3} x _ {3} + \beta_ {4} x _ {4} + \varepsilon_ {2}} \\ & {Y _ {3} = \beta_ {0} + \beta_ {1} x _ {1} + \beta_ {2} x _ {2} + \beta_ {3} x _ {3} + \beta_ {4} x _ {4} + \varepsilon_ {3}} \end{array}\tag{15}
$$

Step 4: calculate the observed binary variable for each latent dependent variable by using the mean as the cut-off threshold. Using the indicator functionΙ(. ), which results in a dummy variable with value 1 if the condition is true and 0 if it is false, we calculate $Z _ { 1 } = \mathrm { ~ I ~ } \big ( Y _ { 1 } \geq m e a n ( Y _ { 1 } ) \big ) , Z _ { 2 } = \mathrm { I } \big ( Y _ { 2 } \geq m e a n ( Y _ { 2 } ) \big )$ $Z _ { 3 } = \operatorname { I } \left( Y _ { 3 } \geq m e a n \left( Y _ { 3 } \right) \right)$

From this population data, we sample three datasets with different sample sizes $( \mathsf { n } = 5 0 , \mathsf { n } = 5 0 0 , \mathsf { n } =$ 50,000). Figure 2 summarizes the study design.

<table><tr><td></td><td>Normal</td><td>Logistic</td><td>Uniform</td></tr><tr><td> $x_1$ </td><td> $U(-1,1)$ </td><td> $U(-1,1)$ </td><td> $U(-1,1)$ </td></tr><tr><td> $x_2$ </td><td> $N(0,0.1^2)$ </td><td> $N(0,0.1^2)$ </td><td> $N(0,0.1^2)$ </td></tr><tr><td> $(x_3,x_4)$ </td><td> $BN(\begin{bmatrix}0\\ 0\end{bmatrix},\begin{bmatrix}0.5 & -0.3\\ -0.3 & 0.5\end{bmatrix})$ </td><td> $BN(\begin{bmatrix}0\\ 0\end{bmatrix},\begin{bmatrix}0.5 & -0.3\\ -0.3 & 0.5\end{bmatrix})$ </td><td> $BN(\begin{bmatrix}0\\ 0\end{bmatrix},\begin{bmatrix}0.5 & -0.3\\ -0.3 & 0.5\end{ bmatrix})$ </td></tr><tr><td> $\epsilon$ </td><td> $\epsilon_1 \sim N(0,1)$ </td><td> $\epsilon_2 \sim Logistic(0,1)$ </td><td> $\epsilon_3 \sim U(0,1)$ </td></tr><tr><td>Regression Coefficients</td><td> $\beta_1=1,\beta_2=-1,$  $\beta_3=0.5,\beta_4=-0.5$ </td><td> $\beta_1=1,\beta_2=-1,$  $\beta_3=0.5,\beta_4=-0.5$ </td><td> $\beta_1=1,\beta_2=-1,$  $\beta_3=0.5,\beta_4=-0.5$ </td></tr><tr><td>Latent continuous variable</td><td> $y_1=\sum_{i=1}^{4}x_i\beta_i+\epsilon_1$ </td><td> $y_2=\sum_{i=1}^{4}x_i\beta_i+\epsilon_2$ </td><td> $y_3=\sum_{i=1}^{4}x_i\beta_i+\epsilon_3$ </td></tr><tr><td>Observed binary variable</td><td> $z_1=I(y_1\geq mean(y_1))$ </td><td> $z_2=I(y_2\geq mean(y_2))$ </td><td> $z_3=I(y_3\geq mean(y_3))$ </td></tr><tr><td>Sample size</td><td>(50,500,50000)</td><td>(50,500,50000)</td><td>(50,500,50000)</td></tr><tr><td>Bootstrap replications</td><td>100</td><td>100</td><td>100</td></tr></table>

Figure 2. Simulation Design for the Goal of Inference and Estimation

## 4.1.2 Analyses and Results

Based on the above design, our study was a $3 \times 3 \times 3$ factorial design: three sample sizes $( \mathsf { n } = 5 0 , \mathsf { n } = 5 0 0 .$ , n = 50,000), three standard error distributions (normal, logistic, and uniform), and three estimated models (Probit, Logit, and LPM). In addition, to evaluate sampling variability, we simulated 100 replications in each cell (for each of the 27 combinations of sample size, error distribution, and estimated model).

Before performing the analyses, we estimated all the models using the population data. Figure 3 shows the results. The first column gives the output for the estimated model with the continuous dependent variable $Y _ { 1 }$ , which serves as a baseline model. The other columns in Figure 3 show the results from probit, logit, and linear probability models with the dependent variables $Z _ { 1 } , Z _ { 2 } ,$ and $Z _ { 3 }$ , respectively. We estimated each model using the data generated from the appropriate distribution—the ideal scenario (i.e., we estimated a logistic model using the data simulated from a logistic error distribution, etc.).

<table><tr><td></td><td>OLS</td><td>Probit</td><td>Logit</td><td>LPM</td></tr><tr><td>(Intercept)</td><td>-0.00(0.00)</td><td>-0.00(0.00)</td><td>-0.00(0.00)</td><td>0.50***(0.00)</td></tr><tr><td> $x_1$ </td><td>1.00***(0.00)</td><td>1.00***(0.00)</td><td>0.99***(0.00)</td><td>0.47***(0.00)</td></tr><tr><td> $x_2$ </td><td>-1.02***(0.01)</td><td>-1.01***(0.01)</td><td>-1.00***(0.02)</td><td>-0.43***(0.00)</td></tr><tr><td> $x_3$ </td><td>0.50***(0.00)</td><td>0.50***(0.00)</td><td>0.50***(0.00)</td><td>0.21***(0.00)</td></tr><tr><td> $x_4$ </td><td>-0.50***(0.00)</td><td>-0.50***(0.00)</td><td>-0.50***(0.00)</td><td>-0.21***(0.00)</td></tr><tr><td> $R^2$ </td><td>0.43</td><td></td><td></td><td>0.59</td></tr><tr><td>Adj.  $R^2$ </td><td>0.43</td><td></td><td></td><td>0.59</td></tr><tr><td>Num. obs.</td><td>1000000</td><td>1000000</td><td>1000000</td><td>1000000</td></tr><tr><td>RMSE</td><td>1.00</td><td></td><td></td><td>0.32</td></tr><tr><td>AIC</td><td></td><td>1063039.43</td><td>1237124.17</td><td></td></tr><tr><td>BIC</td><td></td><td>1063098.51</td><td>1237183.25</td><td></td></tr><tr><td>Log Likelihood</td><td></td><td>-531514.72</td><td>-618557.09</td><td></td></tr><tr><td>Deviance</td><td></td><td>1063029.43</td><td>1237114.17</td><td></td></tr></table>

Figure 3. Estimated Models on Total Data (“Population”)<sup>3</sup>

From Figure 3, we see that the estimates from the LPM were proportional to and directionally consistent with the estimates from the baseline (continuous $Y _ { 1 } )$ model.

We first examined inference: we evaluated the coefficient significance levels in each of the 27 combinations. Figure 4 describes the results for each of the three sample sizes. The x-axis represents common significance levels, and the y-axis is the frequency (or percentage) out of 100 replications. Rows represent different error distributions and columns represent the regression coefficients $( \widehat { \beta } _ { } _ { 1 } , \widehat { \beta } _ { } _ { 2 } , \widehat { \beta } _ { } _ { 3 } , \widehat { \beta } _ { } _ { 4 } )$ . We can observe that the coefficient significance levels were similar for the three models across all the coefficients and for the given three sample sizes. Although we can observe a small discrepancy for the uniform errors for n = 50, the bars for the non-significant (n.s) level were very similar. The violation of distributional assumptions matters for small samples such as n = 50 but, with large samples, these differences disappear.

Figure 5 shows the marginal effects for the estimated models for each sample size. The three subplots in each row are for different error distributions. We plotted the estimated marginal effects for the 100 replications as a boxplot to show their distribution. We can observe that the distribution of marginal effects for each of the three models and for all the coefficients were nearly identical. Since $x _ { 2 }$ had very small variance, ${ \widehat { \boldsymbol { \beta } } } _ { 2 }$ exhibited larger variance compared to other coefficients. With large samples, marginal effects were very precise and also similar across all three models.

Sample Size = 50  
![](/api/attachments/BF8VDYHC/fulltext/images/404a77155b4a0d6bdbebc60dcbd9a37c3666e9fd2f3c9e50efb62218a69f0d8e.jpg)

Sample Size = 500  
![](/api/attachments/BF8VDYHC/fulltext/images/3bc4b230ac9ffe634f4039bce1c608680728c3e4a5e9e51d9f610ade372c9b55.jpg)

Sample Size = 50,000  
![](/api/attachments/BF8VDYHC/fulltext/images/5f9a5d2b687ba5797494cf297e7de2a0de001df4b3c6d0800ef2cf888aba8cb9.jpg)  
Figure 4. Comparing the Three Models in Terms of Frequency of Coefficient Significance by Sample Size; Results Based on 100 Replications for Each of the Sample Data Sets

Sample Size = 50  
![](/api/attachments/BF8VDYHC/fulltext/images/b5de64425baf86f14620a79c1ce95c7342fb700676c10029aa115d600e06318c.jpg)

![](/api/attachments/BF8VDYHC/fulltext/images/a0256ab0fbea448797302fce372b7e3d67f9aa23bd87d880e7370ad3bd823bd9.jpg)

![](/api/attachments/BF8VDYHC/fulltext/images/56edc821f87facfd9f602ac38b75513f046f2129a731c9a96fa0cfa955a23cfd.jpg)  
Figure 5. Comparing the Three Models in Terms of the Marginal Effects Distribution Across 100 Replications for Each Sample Size

## 4.2 Prediction and Selection Bias

## 4.2.1 Simulation Design

We based the simulation for the prediction analyses on the models we describe in Section 2.1. We simulated a dataset of size $\mathsf { n } ~ = ~ 1 , 0 0 0 , 0 0 0$ and set initial parameters to the following values: $\gamma _ { _ 0 } =$ $- 0 . 5 , \gamma _ { 1 } = 0 . 5 , \gamma _ { 2 } = - 0 . 5 , \gamma _ { 3 } = 1 . 5 , \gamma _ { 4 } = - 1 , \beta _ { 0 } = 0 . 5 , \beta _ { 1 } = - 1 . 5 , \beta _ { 2 } = 0 . 5 , \beta _ { 3 } = 1$

Step 1: generate (??, ??) from a bivariate normal distribution with means 0 and covariance $\binom { 0 . 5 } { - 0 . 4 } \quad \begin{array} { l } { { - 0 . 4 } } \\ { { 0 . 5 } } \end{array}$

Step 2: generate $x _ { 1 } { \sim } U ( 0 , 1 ) , x _ { 2 } { \sim } N ( 0 , 1 )$ , and $x _ { 3 } , x _ { 4 }$ from a bivariate normal distribution with means 0.5 and covariance $\binom { 0 . 5 } { 0 . 3 } \quad 0 . 3 )$

Step 3: selection model: compute $\mathsf { S } ^ { \star }$ using the formula $S ^ { * } = \gamma _ { _ 0 } + \gamma _ { _ 1 } x _ { 1 } + \gamma _ { _ 2 } x _ { 2 } + \gamma _ { _ 3 } x _ { 3 } + \gamma _ { _ 4 } x _ { 4 } + \omega$ and ?? = $\mathrm { ~ I ~ } ( S ^ { * } \geq m e a n ( S ^ { * } ) )$ .

Step 4: outcome model: for S = 1, compute Y using the formula: $Y = \beta _ { 0 } + \beta _ { 1 } x _ { 1 } + \beta _ { 2 } x _ { 2 } + \beta _ { 3 } x _ { 3 } + \varepsilon .$

We used the data from the above design to estimate the outcome model under selection bias.

## 4.2.2 Analyses and Results

Similar to the inference and estimation case, we sampled three datasets with sizes $\mathsf { n } = 5 0 0 , \mathsf { n } = 5 0 0 0$ , and n = 50,000. Again, we simulated 100 replications for each combination of sample size and for each model. Figure 6 plots the results in terms of the outcome model coefficients’ distribution.

In addition to comparing the outcome model coefficients, which are of interest in selection bias scenarios, we also compared the predictions of the probit, logit and linear probability models on a holdout set. Such predictions are of interest in predictive studies. Figure A1 shows the results. We can see that the prediction distributions from all three models were identical except for the LPM’s unbounded predictions. This finding also corroborates the selection bias results.

Figure 7 provides the summary statistics for the variables, and one can see that they are severely skewed with possibly extreme outliers. To be able to evaluate the LPM against benchmarks, we dichotomized the price variable using a median split, so that prices above the median were set to ?? = 1 and otherwise to ?? = 0. We estimated all the four models we describe in Section 5.1. We used a holdout sample of size n = 5,000 to evaluate the predictions from the above models. First, we compared the LPM coefficients and their significance with probit, logit, and OLS regression using the continuous price after a logtransformation (ln(Price)) to account for skewness in price<sup>7</sup> (Figure A2<sup>8</sup>).

![](/api/attachments/BF8VDYHC/fulltext/images/581139dad098bc42f6136f39e96484ebd22b3ee77896d96e0b0d85da2466e9a6.jpg)  
Figure 6. Comparing the Coefficient Distribution in a 2SLS Outcome Model after Correcting for Selection Bias with Three Methods; Results by Sample Size based on 100 Bootstrap Replications

## 5 An Application to Online Auctions

Online auction websites produce large amounts of data that one can use to provide services to buyers and sellers, for market research, and for product development. Therefore, academic research that uses online auction data has thrived in various disciplines, including information systems, marketing, computer science, statistics, and economics. Early studies looked at determinants of auction price to identify and quantify factors that affect an auction’s final price (Lucking-Reiley, Bryan, Prasad, & Reeves, 2007); other studies have looked at price dynamics; the development of models for forecasting auction prices and for studying bidder and seller relationships; and more (see Jank & Shmueli, 2010).

To illustrate and evaluate the use of LPMs in the context of a real dataset, we used a large sample (n = 300,384) of eBay (www.ebay.com) auctions for digital cameras that transacted between August 2007 and January 2008. Lin et al. (2013) used the same dataset. We sought to: 1) quantify the relationship between auction price (the outcome) and four covariates of interest: auction duration, minimum bid<sup>5</sup>, and whether the seller set a reserve price<sup>6</sup> or not (the covariates in the model that Lin et al. (2013) used); and 2) predict the price of new auctions given these four predictors.

<table><tr><td>Variable</td><td>N</td><td>Mean</td><td>Std</td><td>Min</td><td>Max</td></tr><tr><td>price ($)</td><td>300,384</td><td>106.900</td><td>102.700</td><td>0.010</td><td>10,099</td></tr><tr><td>minimum bid ($)</td><td>300,384</td><td>38.000</td><td>79.050</td><td>0.010</td><td>8,999</td></tr><tr><td>duration (days)</td><td>300,384</td><td>4.638</td><td>7.655</td><td>0.0004</td><td>641.4</td></tr><tr><td>seller feedback</td><td>300,384</td><td>35,766</td><td>83,574</td><td>999</td><td>365,762</td></tr><tr><td>reserve price (1=yes)</td><td>300,384</td><td>0.0275</td><td>0.1637</td><td>0</td><td>1</td></tr></table>

Figure 7. Summary Statistics for the eBay Auction Variables

Figure 8 describes the results. Both logit and probit models suffered quasi-separation issues (discussed in previous sections) due to severe skewness in the covariates. Figure A6 provides the residual diagnostic plots for the logit model. One can see from the plot that the data contained serious outliers that caused both the logit and probit models to suffer from quasi-separation warnings, while the LPM had no such estimation problems. To avoid this problem, for the inference purpose, we log transformed the three continuous covariates. Column 1 presents the results from OLS regression on the continuous price variables, which we can use as a benchmark. The remaining three models (logit, probit and LPM) used binary price as the dependent variable.

We can immediately see that estimates for both probit and logit look different, which contrasts with what we observed in the simulation results. This issue is not specific to the current data and is not rare in practice. As we mention earlier, we need to scale the logit coefficients by 1.7 to obtain the probit coefficients. Similarly, the coefficients from the LPM are proportional to the true coefficients<sup>9</sup>. One can see that the direction and the significance results across all the models are identical. We compared coefficient significance and marginal analysis as in the simulation. The results (Figure A3) are consistent with both theory and what we observed in the simulation study.

<table><tr><td></td><td>OLS</td><td>Logit</td><td>Probit</td><td>LPM</td></tr><tr><td>(Intercept)</td><td>4.0049***(0.0067)</td><td>-0.3543***(0.0144)</td><td>-0.2332***(0.0087)</td><td>0.4086***(0.0032)</td></tr><tr><td>minimum.bid</td><td>0.1110***(0.0008)</td><td>0.1583***(0.0017)</td><td>0.0957***(0.0010)</td><td>0.0357***(0.0004)</td></tr><tr><td>Seller.Feedback</td><td>0.0422***(0.0006)</td><td>0.0784***(0.0013)</td><td>0.0490***(0.0008)</td><td>0.0185***(0.0003)</td></tr><tr><td>duration</td><td>-0.1798***(0.0022)</td><td>-0.4189***(0.0049)</td><td>-0.2472***(0.0030)</td><td>-0.0915***(0.0010)</td></tr><tr><td>reserve.priceYes</td><td>0.8198***(0.0115)</td><td>1.5687***(0.0270)</td><td>0.9528***(0.0159)</td><td>0.3417***(0.0054)</td></tr><tr><td> $R^2$ </td><td>0.1040</td><td></td><td></td><td>0.0763</td></tr><tr><td>Adj.  $R^2$ </td><td>0.1040</td><td></td><td></td><td>0.0763</td></tr><tr><td>Num. obs.</td><td>295324</td><td>295324</td><td>295324</td><td>295324</td></tr><tr><td>RMSE</td><td>1.0130</td><td></td><td></td><td>0.4805</td></tr><tr><td>AIC</td><td></td><td>385571.7672</td><td>385850.5969</td><td></td></tr><tr><td>BIC</td><td></td><td>385624.7463</td><td>385903.5760</td><td></td></tr><tr><td>Log Likelihood</td><td></td><td>-192780.8836</td><td>-192920.2984</td><td></td></tr><tr><td>Deviance</td><td></td><td>385561.7672</td><td>385840.5969</td><td></td></tr></table>

\*\*\*p < 0.001, \*\* p < 0.01, \*p < 0.05

Figure 8. Estimated OLS and LPM Models for Price of Online Auctions

In terms of predictive power, we compared the out-of-sample predictions and classifications from the LPM to those from a logit and probit models for the holdout sample. While variable transformations are good for coefficient estimation (explanatory modeling), sometimes modeling the raw data leads to higher predictive performance. Therefore, we compared predictions from models with unstandardized covariates (Figure 9) to predictions from models without log transformed covariates (Figure A4 in Appendix). Figure 9 shows good class separation by all models, while Figure A4 shows less class separation. And, indeed, we see that the predictive power of the models that used binary price on raw data (or covariates) was much better than the models using binary price on log transformed data (or covariates). Note that some LPM predictions exceeded the unit interval.

In the boxplots, the LPM predictions appear to have slightly lower variance within each class but closer class medians. We also note that the area under the curve (AUC) values for the three models are identical. Thus, for a predictive purpose, if one seeks class separation alone, then the LPM is as good as the logit and probit models. However, since the predicted probabilities exceeded the unit interval, LPMs are not a good choice if one seeks the predicted probabilities themselves.

![](/api/attachments/BF8VDYHC/fulltext/images/8e1ee66b77499db86a49b6e63875809aeede497d29bbe8c18989519de1632589.jpg)

![](/api/attachments/BF8VDYHC/fulltext/images/7bd99e4e39b239629c4052a30049b9d5fd563957609b641d8e597f24dab0073a.jpg)  
False positive rate  
Figure 9. Predictions (Left) and ROC Curves (Right) for the Holdout Price Data for Logit, Probit, and Linear Probability Models (Unstandardized Covariates)

## 6 Summary and Conclusions

The results from both the simulation study and eBay analysis indicate that LPMs perform similar to logistic and probit models in terms of coefficient significance, effect size (marginal effect), classification, and ranking. LPM coefficients have the added advantage of easier interpretation, but LPMs are inferior to logit and probit models if predicted probabilities are of interest.

Revisiting our literature survey, we note that, in almost all of the studies, the authors could have considered using a LPM in place of the logit or probit model they used. Specifically, in all of the selection model cases except for the paper that used Tobit due to truncation, the authors could have used a LPM. Using a LPM in place of a probit model in the first stage of 2SLS is simpler than using a probit model because it does not require computing the Mills ratio. For papers that performed classification, LPM would have been a reasonable model in place of the logistic regression: in Kohli and Devaraj (2003) and in Bardhan, Oh, Zheng, and Kirksey (2015). In contrast, Hui et al. (2007) report both predicted classes and probabilities, and, therefore, a LPM would not have been a good choice. Lastly, for the inference and estimation studies, in all cases where the authors used the binary outcome model for obtaining statistical significance, coefficient sign, or marginal effects, a LPM would have again been a reasonable alternative. For marginal effects, LPMs are especially useful because they do not require extra calculations (as is the case in linear regression for a continuous outcome). For example, Bloom, Garicano, Sadun, and Van Reenen (2014) compared the effect size of different independent variables on several outcomes of interest (some of which were continuous and some binary). They fitted OLS to the numerical outcome models and probit to the binary outcome models. For interpreting the effects, they relied on the OLS coefficients directly but had to perform and report marginal effects for the probit models. Had they used a LPM, they would have simplified the exposition and been able to straightforwardly compare and interpret the different models of interest.

Our results illustrate that LPMs have advantages and disadvantages when compared to GLMs for a binary outcome variable. We see that whether one should use a LPM closely depends on one’s analysis goal. For inference and parameter estimation, LPMs are mainly useful due to their simplicity and ease of interpretation. For generating predicted or fitted values from selection models or for classification, LPMs are as good as logit and probit models in terms of class separation and ranking. LMPs are inappropriate only when the predicted probabilities themselves are the quantities of interest. We also show that LPMs perform equally to other selection bias models. Finally, in terms of inference, LPMs provide a superior alternative for data where the logit and probit models do not converge or issue quasi-separation warnings (e.g., our eBay example). We summarize the advantages and weaknesses of LPM in Table 2.

Table 2. Summary of the LPM Results: Advantages and Shortcomings of LPM for Different Study Goals

<table><tr><td>Inference and estimation</td><td>Predicting new records</td><td>Selection bias</td></tr><tr><td>1. LPMs do not have convergence issues such as quasi-separation that logit and probit models have.2. Coefficient signs are consistent and the estimators are consistent for the true parameters up to a multiplicative scalar.3. LPMs allows one to more easily interpret of coefficients and to not need to calculate marginal effects.4. LPMs suffer from heteroscedasticity and non-normality. If the sample size is too small, then LPMs might not be a good choice.</td><td>1. For classification, in terms of class separation and ranking, LPMs&#x27; performance is as good as logit and probit models.2. When one is directly interested in the predicted probabilities, LPMs are not a good choice due to values that exceed the unit interval. Logit and probit models are better choices.3. LPMs produce unbounded predicted probabilities (beyond [0,1]). Obtaining too many unbounded predictions can indicate an inadequate model: one needs to either include more predictors or else use a GLM</td><td>1. Unlike the probit selection model in 2SLS that requires computing the Mills ratio, one can insert LPM fitted values as-is into the outcome model.2. More easily interpret marginal effects when the selection and outcome models use the same covariates.3. Outcome model inference results using LPM fitted values are the same as logit and probit.</td></tr><tr><td>Recommendations:</td><td>Recommendations:</td><td>Recommendations:</td></tr><tr><td>1. Use LPM if the sample size is large, otherwise use a GLM.2. If using a LPM with a small sample, correct the standard errors using WLS.3. Before performing WLS, trim predicted probabilities to avoid losing many observations.</td><td>1. Use LPMs if one seeks classification or ranking.2. If one seeks to obtain predicted probabilities, then use GLM.3. If using LPM to obtain predicted probabilities, then round off probabilities exceeding [0,1].4. With many unbounded predictions, then a LPM might not be a good choice. Use a GLM.</td><td>1. Use LPM if the sample size is large.2. If both selection model and outcome model have the same predictors, then LPMs might not be a good choice because they suffer from multicollinearity more than probit models.</td></tr></table>

As Table 2 shows, and consistent with the literature, the LPM estimators are consistent for the true parameters up to a multiplicative scalar. One can calculate the scalar if one has a reasonable estimate of $\sigma _ { y }$ However, we reiterate that one needs the standard deviation only to retrieve the underlying true (OLS) coefficient, which is often not a researcher’s primary interest. When really needed, however, one could obtain an estimate of the standard deviation based on subject knowledge (similar to Bayesian priors) or by using previous studies that use a continuous outcome variable. One could also take a small sample of the continuous outcome variable when it is expensive to collect it for the entire study sample. In addition to the coefficient proportionality property, the coefficient significance and direction are consistent with logit and probit models.

Our simulation results on coefficient significance agree with the results that Hellevik (2009) reports. However, our study differs from Hellevik (2009) in terms of objectives and contributions. They are similar only to Hellevik’s (2009) results that compared the significance probabilities of linear probability and logit models. While Hellevik (2009) focuses only on the coefficients’ statistical significance, we also examine prediction and selection bias issues. Our simulation settings are more comprehensive. We used four covariates both in the simulation and in a real dataset (eBay) with different types of variable distributions, while Hellevik (2009) used only two covariates (one continuous, one binary). We also used varying sample sizes (n = 50, 500, and 50000) to observe the consistent behavior of the estimators. Lastly, we also included the probit model in our comparisons, whereas Helevik (2009) only compared LPMs with logit models. Hence, our approach and results provide a more comprehensive picture about LPMs’ performance compared to logit and probit models. As we move into the realm of big data, we need to consider analyses’ computational costs. With the advances in computing power, logit and probit models estimation is typically sufficiently fast despite the iterative nature of the estimation algorithm. LPMs produce results in a single iteration and are computationally cheaper. Hence, when one seeks to obtain real time predictions or where one needs to update the model frequently (e.g., every minute), LPMs might be advantageous. Table A2 describes the computation times for our simulation study in Section 4.1 (model with four predictors).

One question for future research involves using LPMs with multi-category outcome variables. For example, in propensity score matching, research has shown that logit and probit selection models have negligible differences with a binary outcome but that they do have different strengths in the multi-class case (Caliendo, 2006, p.73). Second, our simulation study was limited to the manipulated variables we chose. One could extend our study by expanding the simulation models to a large number of predictors and non-linear relationships such as interaction terms. Our initial findings from exploring nonlinear models indicate that the results remain unchanged as long as no severe multicollinearity affects LPM estimation. Finally, another direction of interest is LPMs’ performance compared to logit or probit models in the case of highly unbalanced data, where the number of 1s is very small or very large.

## Acknowledgments

We thank Ravi Bapna and Nishtha Langer for emphasizing the importance of studying LPMs for selection bias and Wolfgang Jank for sharing the eBay data. We are grateful to the AE and the three reviewers for their helpful comments and suggestions that helped improve this paper. This research was partially funded by grant 105-2410-H-007-034-MY3 from the Ministry of Science and Technology in Taiwan.

## References

Abbasi, A., Sarker, S., & Chiang, R. H. (2016). Big data research in information systems: Toward an inclusive research agenda. Journal of the Association for Information Systems, 17(2), i-xxxii.

Adjerid, I., Acquisti, A., Telang, R., Padman, R., & Adler-Milstein, J. (2015). The impact of privacy regulation and technology incentives: The case of health information exchanges. Management Science, 62(4), 1042-1063.

Agarwal, R., & Dhar, V. (2014). Big data, data science, and analytics: The opportunity and challenge for IS research. Information Systems Research, 25(3), 443-448.

Aggarwal, R., Gopal, R., Gupta, A., & Singh, H. (2012). Putting money where the mouths are: The relation between venture financing and electronic word-of-mouth. Information Systems Research, 23(3), 976-992.

Aggarwal, R., Kryscynski, D., Midha, V., & Singh, H. (2015). Early to adopt and early to discontinue: The impact of self-perceived and actual IT knowledge on technology use behaviors of end users. Information Systems Research, 26(1), 127-144.

Aggarwal, R., & Singh, H. (2013). Differential influence of blogs across different stages of decision making: The case of venture capitalists. MIS Quarterly, 37(4), 1093-1112.

Aldrich, J. H., & Nelson, F. D. (1984). Linear probability, logit, and probit models (vol. 45). Thousand Oaks, CA: Sage.

Anderson, G. J. (1987). Prediction tests in limited dependent variable models. Journal of Econometrics, 34(1), 253-261.

Angrist, J. D., & Pischke, J. S. (2008). Mostly harmless econometrics: An empiricist's companion. Princeton, NJ: Princeton University Press.

Angrist, J. D., & Pischke, J. S. (2012). Probit better than LPM? MostlyHarmlessEconometrics. Retrieved from http://www.mostlyharmlesseconometrics.com/2012/07/probit-better-than-lpm/

Aral, S., Brynjolfsson, E., & Wu, L. (2012). Three-way complementarities: Performance pay, human resource analytics, and information technology. Management Science, 58(5), 913-931.

Asvanund, A., Clay, K., Krishnan, R., & Smith, M. D. (2004). An empirical analysis of network externalities in peer-to-peer music-sharing networks. Information Systems Research, 15(2), 155-174.

Banker, R. D., Hu, N., Pavlou, P. A., & Luftman, J. (2011). CIO reporting structure, strategic positioning, and firm performance. MIS Quarterly, 35(2), 487-504.

Bapna, R., Goes, P., Wei, K. K., & Zhang, Z. (2011). A finite mixture logit model to segment and predict electronic payments system adoption. Information Systems Research, 22(1), 118-133.

Bardhan, I., Oh, J. H., Zheng, Z., & Kirksey, K. (2015). Predictive analytics for readmission of patients with congestive heart failure. Information Systems Research, 26(1), 19-39.

Benaroch, M., Lichtenstein, Y., & Robinson, K. (2006). Real options in information technology risk management: An empirical validation of risk-option relationships. MIS Quarterly, 30(4), 827-864.

Betts, J. R., & Fairlie, R. W. (2001). Explaining ethnic, racial, and immigrant differences in private school attendance. Journal of Urban Economics, 50(1), 26-51.

Bloom, N., Garicano, L., Sadun, R., & Van Reenen, J. (2014). The distinct effects of information technology and communication technology on firm organization. Management Science, 60(12), 2859-2885.

Brillinger, D. R. (2012). A generalized linear model with “Gaussian” regressor variables. In D. R. Brillinger (Ed.), Selected works of David Brillinger (pp. 589-606). Berlin: Springer.

Burtch, G., Ghose, A., & Wattal, S. (2016). Secret admirers: An empirical examination of information hiding and contribution dynamics in online crowdfunding. Information Systems Research, 27(3), 478-496.

Caliendo, M., Clement, M., Papies, D., & Scheel-Kopeinig, S. (2012). The cost impact of spam filters: Measuring the effect of information system technologies in organizations. Information Systems Research, 23(3), 1068-1080.

Caudill, S. B. (1987). Dichotomous choice models and dummy variables. The Statistician, 36, 381-383.

Caliendo, M. (2006). Microeconometric evaluation of labour market policies (vol. 568). Berlin: Springer.

Ceccagnoli, M., Forman, C., Huang, P., & Wu, D. J. (2011). Co-creation of value in a platform ecosystem: The case of enterprise software. MIS Quarterly, 36(1), 263-290.

Chan, J., & Ghose, A. (2013). Internet’s dirty secret: Assessing the impact of online intermediaries on HIV transmission. MIS Quarterly, 38(4), 955-976.

Chang, Y. B., & Gurbaxani, V. (2012). Information technology outsourcing, knowledge transfer, and firm productivity: An empirical analysis. MIS Quarterly, 36(4), 1043-1053.

Chau, P. Y., & Tam, K. Y. (1997). Factors affecting the adoption of open systems: An exploratory study. MIS Quarterly, 21(1), 1-24.

Chen, P. Y., & Forman, C. (2006). Can vendors influence switching costs and compatibility in an environment with open standards? MIS Quarterly, 30(SI), 541-562.

Chen, P. Y., & Hitt, L. M. (2002). Measuring switching costs and the determinants of customer retention in Internet-enabled businesses: A study of the online brokerage industry. Information Systems Research, 13(3), 255-274.

Chen, Y., & Bharadwaj, A. (2009). An empirical analysis of contract structures in IT outsourcing. Information Systems Research, 20(4), 484-506.

De, P., Hu, Y., & Rahman, M. S. (2013). Product-oriented Web technologies and product returns: An exploratory study. Information Systems Research, 24(4), 998-1010.

Duan, N., & Li, K. C. (1991). A bias bound for least squares linear regression. Statistica Sinica, 1(1991), 127-136.

Duda, R. O., Hart, P. E., & Stork, D. G. (2012). Pattern classification. New York: John Wiley & Sons.

Fairlie, R. W., & Sundstrom, W. A. (1999). The emergence, persistence, and recent widening of the racial unemployment gap. Industrial & Labor Relations Review, 52(2), 252-270.

Fang, Z., Gu, B., Luo, X., & Xu, Y. (2015). Contemporaneous and delayed sales impact of location-based mobile promotions. Information Systems Research, 26(3), 552-564.

Fisher, R. A. (1936). The use of multiple measurements in taxonomic problems. Annals of Eugenics, 7(2), 179-188.

Fitoussi, D., & Gurbaxani, V. (2012). IT outsourcing contracts and performance measurement. Information Systems Research, 23(1), 129-143.

Forman, C., Ghose, A., & Wiesenfeld, B. (2008). Examining the relationship between reviews and sales: The role of reviewer identity disclosure in electronic markets. Information Systems Research, 19(3), 291-313.

Forman, C., Ghose, A., & Goldfarb, A. (2009). Competition between local and electronic markets: How the benefit of buying online depends on where you live. Management Science, 55(1), 47-57.

Friedman, J., Hastie, T., & Tibshirani, R. (2009). The elements of statistical learning (2<sup>nd</sup> ed.). Berlin: Springer.

Gefen, D., & Carmel, E. (2008). Is the world really flat? A look at offshoring at an online programming marketplace. MIS Quarterly, 32(2), 367-384.

Gao, G., Greenwood, B. N., Agarwal, R., & Jeffrey, S. (2015). Vocal minority and silent majority: How do online ratings reflect population perceptions of quality? MIS Quarterly, 39(3), 565-589.

Godinho de Matos, M., Ferreira, P., & Krackhardt, D. (2014). Peer influence in the diffusion of the iPhone 3G over a large social network. Management Information Systems Quarterly, 38(4), 1103-1133.

Goes, P. B., Lin, M., & Au Yeung, C. M. (2014). “Popularity effect” in user-generated content: Evidence from online product reviews. Information Systems Research, 25(2), 222-238.

Goh, K. Y., Heng, C. S., & Lin, Z. (2013). Social media brand community and consumer behavior: Quantifying the relative impact of user-and marketer-generated content. Information Systems Research, 24(1), 88-107.

Goldberger, A. S. (1964). Econometric theory. New York: Wiley.

Gopal, A., & Koka, B. R. (2012). The asymmetric benefits of relational flexibility: evidence from software development outsourcing. MIS Quarterly, 36(2), 553-576.

Gopal, A., & Sivaramakrishnan, K. (2008). On vendor preferences for contract types in offshore software projects: The case of fixed price vs. time and materials contracts. Information Systems Research, 19(2), 202-220.

Gordon, D. V., Lin, Z., Osberg, L., & Phipps, S. (1994). Predicting probabilities: Inherent and sampling variability in the estimation of discrete-choice models. Oxford Bulletin of Economics and Statistics, 56(1), 13-31.

Gordon, L. A., Loeb, M. P., & Sohail, T. (2010). Market value of voluntary disclosures concerning information security. MIS Quarterly, 34(3), 567-594.

Gray, J. V., Siemsen, E., & Vasudeva, G. (2015). Colocation still matters: Conformance quality and the interdependence of R&D and manufacturing in the pharmaceutical industry. Management Science, 61(11), 2760-2781.

Griffith, T. L., & Northcraft, G. B. (1996). Cognitive elements in the implementation of new technology: Can less information provide more benefits? MIS Quarterly, 20(1), 99-110.

Gu, B., Konana, P., Raghunathan, R., & Chen, H. M. (2014). The allure of homophily in social media: Evidence from investor responses on virtual communities. Information Systems Research, 25(3), 604-617.

Haggstrom, G. W. (1983). Logistic regression and discriminant analysis by ordinary least squares. Journal of Business & Economic Statistics, 1(3), 229-238.

Hahn, J., Moon, J. Y., & Zhang, C. (2008). Emergence of new project teams from open source software developer networks: Impact of prior collaboration ties. Information Systems Research, 19(3), 369- 391.

Han, W., Ada, S., Sharman, R., & Rao, H. R. (2015). Campus emergency notification systems: an examination of factors affecting compliance with alerts. MIS Quarterly, 39 (4), 909-929.

Hansen, J. M., & Walden, E. (2013). The role of restrictiveness of use in determining ethical and legal awareness of unauthorized file sharing. Journal of the Association for Information Systems, 14(9), 521-549.

Hargittai, E. (2006). Hurdles to information seeking: Spelling and typographical mistakes during users online behavior. Journal of the Association for Information Systems, 7(1), 52-67.

Heckman, J. J. (1979). Sample selection bias as a specification error. Econometrica, 47(1), 153-161.

Heckman, J. J., & Snyder, J. M., Jr. (1996). Linear probability models of the demand for attributes with an empirical application to estimating the preferences of legislators (no. w5785). National Bureau of Economic Research.

Hellevik, O. (2009). Linear versus logistic regression when the dependent variable is a dichotomy. Quality & Quantity, 43(1), 59-74.

Hinz, O., Spann, M., & Hann, I. H. (2015). Can’t buy me love… or can I? Social capital attainment through conspicuous consumption in virtual environments. Information Systems Research, 26(4), 859-870.

Hong, Y., & Pavlou, P. A. (2014). Product fit uncertainty in online markets: Nature, effects, and antecedents. Information Systems Research, 25(2), 328-344.

Hong, Y., Wang, C., & Pavlou, P. A. (2015). Comparing open and sealed bid auctions: Evidence from online labor markets. Information Systems Research.

Hui, K. L., Teo, H. H., & Lee, S. Y. T. (2007). The value of privacy assurance: An exploratory field experiment. MIS Quarterly, 31(1), 19-33.

Hyun Kim, S., Mukhopadhyay, T., & Kraut, R. E. (2016). When does repository KMS use lift performance? the role of alternative knowledge sources and task environments. MIS Quarterly, 40(1), 133-156.

Jank, W., & Shmueli, G. (2010). Modeling online auctions (vol. 91). New York: John Wiley & Sons.

Johnson, N. L., Kotz, S., & Balakrishnan, N. (1997). Discrete multivariate distributions. New York: John Wiley & Sons.

Kalaignanam, K., Kushwaha, T., Steenkamp, J. B. E., & Tuli, K. R. (2013). The effect of CRM outsourcing on shareholder value: A contingency perspective. Management Science, 59(3), 748-769.

Klaassen, F. J., & Magnus, J. R. (2001). Are points in tennis independent and identically distributed? Evidence from a dynamic binary panel data model. Journal of the American Statistical Association, 96(454), 500-509.

Kohli, R., & Devaraj, S. (2003). Measuring information technology payoff: A meta-analysis of structural variables in firm-level empirical research. Information systems research, 14(2), 127-145.

Kohli, R., Devaraj, S., & Ow, T. T. (2012). Does information technology investment influence a firm's market value? A case of non-publicly traded healthcare firms. MIS Quarterly, 36(4), 1145-1163.

Kuan, K. K., Hui, K. L., Prasarnphanich, P., & Lai, H. Y. (2015). What makes a review voted? An empirical investigation of review voting in online review systems. Journal of the Association for Information Systems, 16(1), 48-71.

Kudaravalli, S., & Faraj, S. (2008). The structure of collaboration in electronic networks\*. Journal of the Association for Information Systems, 9(10/11), 706-726.

Kuruzovich, J., Viswanathan, S., Agarwal, R., Gosain, S., & Weitzman, S. (2008). Marketspace or marketplace? Online information search and channel outcomes in auto retailing. Information Systems Research, 19(2), 182-201.

Kwon, J., & Johnson, M. E. (2014). Proactive versus reactive security investments in the healthcare sector. MIS Quarterly, 38(2), 451-471.

Langer, N., Forman, C., Kekre, S., & Sun, B. (2012). Ushering buyers into electronic channels: An empirical analysis. Information Systems Research, 23(4), 1212-1231.

Li, K. C., & Duan, N. (1989). Regression analysis under link violation. The Annals of Statistics, 17(3), 1009-1052.

Lin, M., Lucas, H. C., Jr., & Shmueli, G. (2013). Too big to fail: Large samples and the p-value problem. Information Systems Research, 24(4), 906-917.

Liu, D., Brass, D., Lu, Y., & Chen, D. (2015). Friendships in online peer-to-peer lending: Pipes, prisms, and relational herding. MIS Quarterly, 39(3), 729-742.

Long, J. S., & Freese, J. (2006). Regression models for categorical dependent variables using Stata. College Station, TX: Stata Press.

Luca, M., & Zervas, G. (2016). Fake it till you make it: Reputation, competition, and Yelp review fraud. Management Science, 62(12), 3412-3427

Lucking-Reiley, D., Bryan, D., Prasad, N., & Reeves, D. (2007). Pennies from eBay: The determinants of price in online auctions. The Journal of Industrial Economics, 55(2), 223-233.

Lukashin, Y. P. (2000). Econometric analysis of managers' judgements on the determinants of the financial situation in Russia. Economics of Planning, 33(1-2), 85-101.

Ma, L., Montgomery, A. L., Singh, P. V., & Smith, M. D. (2014). An empirical analysis of the impact of prerelease movie piracy on box office revenue. Information Systems Research, 25(3), 590-603.

Maddala, G. S. (1986). Limited-dependent and qualitative variables in econometrics. Cambridge: Cambridge University Press.

Mani, D., Barua, A., & Whinston, A. (2010). An empirical analysis of the impact of information capabilities design on business process outsourcing performance. MIS Quarterly, 34(1), 39-62.

Mani, D., Barua, A., & Whinston, A. B. (2012). An empirical analysis of the contractual and information structures of business process outsourcing relationships. Information Systems Research, 23(3), 618-634.

Mani, D., Barua, A., & Whinston, A. B. (2013). Outsourcing contracts and equity prices. Information Systems Research, 24(4), 1028-1049.

McElheran, K. (2015). Do market leaders lead in business process innovation? The case (s) of e-business adoption. Management Science, 61(6), 1197-1216.

McGarry, K. (2000). Testing parental altruism: Implications of a dynamic model (no. w7593). National Bureau of Economic Research.

Mendelson, H., & Pillai, R. R. (1998). Clockspeed and informational response: Evidence from the information technology industry. Information Systems Research, 9(4), 415-433.

Meservy, T. O., Jensen, M. L., & Fadel, K. J. (2013). Evaluation of competing candidate solutions in electronic networks of practice. Information Systems Research, 25(1), 15-34.

Miller, A. R., & Tucker, C. (2009). Privacy protection and technology diffusion: The case of electronic medical records. Management Science, 55(7), 1077-1093.

Miller, A. R., & Tucker, C. (2013). Active social media management: The case of health care. Information Systems Research, 24(1), 52-70.

Mithas, S., & Krishnan, M. S. (2009). From association to causation via a potential outcomes approach. Information Systems Research, 20(2), 295-313.

Moreno, A., & Terwiesch, C. (2014). Doing business with strangers: Reputation in online service marketplaces. Information Systems Research, 25(4), 865-886.

Mukras, M. S. (1993). Elementary econometrics: Theory, application and policy. Nairobi: East African Publishers.

Oestreicher-Singer, G., & Zalmanson, L. (2013). Content or community? A digital business strategy for content providers in the social age. MIS Quarterly, 37(2), 591-616.

Oh, O., Agrawal, M., & Rao, H. R. (2013). Community intelligence and social media services: A rumor theoretic analysis of tweets during social crises. MIS Quarterly, 37(2), 407-426.

Olsen, R. J. (1980). A least squares correction for selectivity bias. Econometrica: Journal of the Econometric Society, 48(7), 1815-1820.

Overby, E., & Jap, S. (2009). Electronic and physical market channels: A multiyear investigation in a market for products of uncertain quality. Management Science, 55(6), 940-957.

Overby, E., & Clarke, J. (2012). A transaction-level analysis of spatial arbitrage: The role of habit, attention, and electronic trading. Management Science, 58(2), 394-412.

Özpolat, K., Gao, G., Jank, W., & Viswanathan, S. (2013). The value of third-party assurance seals in online retailing: An empirical investigation. Information Systems Research, 24(4), 1100-1111.

Thirumalai, S., & Sinha, K. K. (2013). To personalize or not to personalize online purchase interactions: Implications of self-selection by retailers. Information Systems Research, 24(3), 683-708.

Raghu, T. S., Sinha, R., Vinze, A., & Burton, O. (2009). Willingness to pay in an open source software environment. Information Systems Research, 20(2), 218-236.

Ransbotham, S., & Mitra, S. (2009). Choice and chance: A conceptual model of paths to information security compromise. Information Systems Research, 20(1), 121-139.

Rice, S. C. (2012). Reputation and uncertainty in online markets: An experimental study. Information Systems Research, 23(2), 436-452.

Rishika, R., Kumar, A., Janakiraman, R., & Bezawada, R. (2013). The effect of customers’ social media participation on customer visit frequency and profitability: An empirical investigation. Information Systems Research, 24(1), 108-127.

Ruckman, K., Saraf, N., & Sambamurthy, V. (2015). Market positioning by IT service vendors through imitation. Information Systems Research, 26(1), 100-126.

Schlereth, C., & Skiera, B. (2017). Two new features in discrete choice experiments to improve willingness-to-pay estimation that result in SDR and SADR: Separated (adaptive) dual response. Management Science, 63(3), 829-842

Shmueli, G., & Koppius, O. (2011). Predictive analytics in information systems research. MIS Quarterly, 35(3), 553-572.

Shmueli, G. (2010). To explain or to predict? Statistical Science, 25(3), 289-310.

Singh, H., Aggarwal, R., & Cojuharenco, I. (2015). Strike a happy medium: The effect of IT knowledge on venture capitalists’ overconfidence in it investments. MIS Quarterly, 39(4), 887-908.

Smith, M. D., & Telang, R. (2009). Competing with free: The impact of movie broadcasts on DVD sales and internet piracy. MIS Quarterly, 33(2), 321-338.

Susarla, A., & Barua, A. (2011). Contracting efficiency and new firm survival in markets enabled by information technology. Information Systems Research, 22(2), 306-324.

Susarla, A., Subramanyam, R., & Karhade, P. (2010). Contractual provisions to mitigate holdup: Evidence from information technology outsourcing. Information Systems Research, 21(1), 37-55.

Tafti, A., Mithas, S., & Krishnan, M. S. (2013). The effect of information technology-enabled flexibility on formation and market value of alliances. Management Science, 59(1), 207-225.

Tam, K. Y., & Ho, S. Y. (2005). Web personalization as a persuasion strategy: An elaboration likelihood model perspective. Information Systems Research, 16(3), 271-291.

Tambe, P., & Hitt, L. M. (2012). Now IT's personal: Offshoring and the shifting skill composition of the US information technology workforce. Management Science, 58(4), 678-695.

Tian, F., & Xu, S. X. (2015). How do enterprise resource planning systems affect firm risk? Postimplementation impact. MIS Quarterly, 39(1), 39-60.

Vargha, A., Rudas, T., Delaney, H. D., & Maxwell, S. E. (1996). Dichotomization, partial correlation, and conditional independence. Journal of Educational and Behavioral statistics, 21(3), 264-282.

Wang, T., Kannan, K. N., & Ulmer, J. R. (2013). The association between the disclosure and the realization of information security risk factors. Information Systems Research, 24(2), 201-218.

Westin, R. B. (1974). Predictions from binary choice models. Journal of Econometrics, 2(1), 1-16.

Wooldridge, J. M. (2010). Econometric analysis of cross section and panel data (2<sup>nd</sup> ed.). Cambridge, MA: MIT Press.

Wu, L. (2013). Social network effects on productivity and job security: Evidence from the adoption of a social networking tool. Information Systems Research, 24(1), 30-51.

Xue, L., Ray, G., & Gu, B. (2011). Environmental uncertainty and IT infrastructure governance: A curvilinear relationship. Information Systems Research, 22(2), 389-399.

Yahav, I., Shmueli, G., & Mani, D. (2016). A tree-based approach for addressing self-selection in impact studies with big data, MIS Quarterly, 40(4), 819-848.

Ye, S., Gao, G., & Viswanathan, S. (2014). Strategic behavior in online reputation systems: Evidence from revoking on eBay. MIS Quarterly, 38(4), 1033-1056.

Yin, D., Bond, S., & Zhang, H. (2014). Anxious or angry? Effects of discrete emotions on the perceived helpfulness of online reviews. MIS Quarterly, 38(2), 539-560.

Zeileis, A. (2004). Econometric computing with HC and HAC covariance matrix estimators. Journal of Statistical Software, 11(10), 1-17.

## Appendix

Table A1. Results from Search of IS Literature for Regression Models for a Binary Dependent Variable (JAIS, ISR, MISQ, Management Science’s IS Section)

<table><tr><td>Authors, journal and year</td><td>Dependent variable</td><td>Use of model</td><td>Hybrid</td></tr><tr><td>Hansen &amp; Walden (2013), JAIS</td><td>Ethical; legal</td><td>Inference &amp; estimation</td><td>Logit</td></tr><tr><td>Kudaravalli &amp; Faraj (2008), JAIS</td><td>Issue resolution</td><td>Inference &amp; estimation</td><td>Logit</td></tr><tr><td>Hargittai (2006), JAIS</td><td>mistake(s)</td><td>Inference &amp; estimation</td><td>Logit</td></tr><tr><td>Susarla &amp; Barua (2010), ISR</td><td>Contract renewal</td><td>Inference &amp; estimation</td><td>Logit</td></tr><tr><td>Hahn, Moon, &amp; Zhang (2008), ISR</td><td>Developer joining</td><td>Inference &amp; estimation</td><td>Logit</td></tr><tr><td>Chen &amp; Hitt (2002), ISR</td><td>Switch, attrition</td><td>Inference &amp; estimation</td><td>Logit</td></tr><tr><td>Tam &amp; Ho (2005), ISR</td><td>Choice</td><td>Inference &amp; estimation</td><td>Logit</td></tr><tr><td>Fang, Gu, Luo, &amp; Xu (2015), ISR</td><td>Purchase or not</td><td>Inference &amp; estimation</td><td>Logit</td></tr><tr><td>Aggarwal, Kryscynski, Midha, &amp; Singh (2015), ISR</td><td>Adopt decision</td><td>Inference &amp; estimation</td><td>Logit</td></tr><tr><td>Moreno &amp; Terwiesch (2014), ISR</td><td>Success of bid</td><td>Inference &amp; estimation</td><td>Logit</td></tr><tr><td>Gu, Konana, Raghunathan, &amp; Chen (2014), ISR</td><td>Selected a thread or not</td><td>Inference &amp; estimation</td><td>Logit</td></tr><tr><td>Goes, Lin, &amp; Au Yeung (2014), ISR</td><td>Provided rating or not</td><td>Inference &amp; estimation</td><td>Logit</td></tr><tr><td>Hong &amp; Pavlou (2014), ISR</td><td>Product return</td><td>Inference &amp; estimation</td><td>Logit</td></tr><tr><td>Langer, Forman, Kekre, &amp; Sun (2012), ISR</td><td>Channel choice</td><td>Inference &amp; estimation</td><td>Logit</td></tr><tr><td>Rice (2012), ISR</td><td>To transact</td><td>Inference &amp; estimation</td><td>Logit</td></tr><tr><td>Fitoussi &amp; Gurbaxani (2012), ISR</td><td>Reduction in IT cost</td><td>Inference &amp; estimation</td><td>Logit</td></tr><tr><td>Xue, Ray, &amp; Gu (2011), ISR</td><td>Centralization, uncertainty</td><td>Inference &amp; estimation</td><td>Logit</td></tr><tr><td>Raghu, Sinha, Vinze, &amp; Burton (2009), ISR</td><td>Willingness to pay</td><td>Inference &amp; estimation</td><td>Logit</td></tr><tr><td>Ransbotham &amp; Mitra (2009), ISR</td><td>Target</td><td>Inference &amp; estimation</td><td>Logit</td></tr><tr><td>Asvanund et al. (2004), ISR</td><td>Availability</td><td>Inference &amp; estimation</td><td>Logit</td></tr><tr><td>Özpolat et al. (2013), ISR</td><td>Purchase conversion</td><td>Inference &amp; estimation</td><td>Logit &amp; probit</td></tr><tr><td>Forman et al. (2008), ISR</td><td>Disclosure</td><td>Inference &amp; estimation</td><td>LPM</td></tr><tr><td>Burtch et al. (2016), ISR Mendelson &amp; Pillai (1998), ISR</td><td>Concealment Availability of time shifted communication technologies</td><td>Inference &amp; estimation Inference &amp; estimation</td><td>LPM Probit</td></tr><tr><td>Ruckman, Saraf, &amp; Sambamurthy (2015), ISR</td><td>Service change</td><td>Inference &amp; estimation</td><td>Probit</td></tr><tr><td>Mani, Barya, &amp; Whinston (2013), ISR</td><td>Contract choice</td><td>Inference &amp; estimation</td><td>Probit</td></tr><tr><td>Wu (2013), ISR</td><td>Retention</td><td>Inference &amp; estimation</td><td>Probit</td></tr><tr><td>Miller &amp; Tucker (2013), ISR</td><td>Active social media</td><td>Inference &amp; estimation</td><td>Probit</td></tr><tr><td>Kuruzovich, Viswanathan, Agarwal, Gosain, &amp; Weitzman (2008), ISR</td><td>Information retrieval</td><td>Inference &amp; estimation</td><td>Probit</td></tr><tr><td>Han, Ada, Sharman, &amp; Rao (2015), MISQ</td><td>Intention to comply</td><td>Inference &amp; estimation</td><td>Logit</td></tr><tr><td>Chan &amp; Ghose (2013), MISQ</td><td>Entry into the states</td><td>Inference &amp; estimation</td><td>Logit</td></tr><tr><td>Banker, Hu, Pavlou, &amp; Luftman (2011), MISQ</td><td>CIO reporting structure</td><td>Inference &amp; estimation</td><td>Logit</td></tr></table>

Table A1. Results from Search of IS Literature for Regression Models for a Binary Dependent Variable (JAIS, ISR, MISQ, Management Science’s IS Section)

<table><tr><td>Benaroch, Lichtenstein, &amp; Robinson (2006), MISQ</td><td>Risk option associations</td><td>Inference &amp; estimation</td><td>Logit</td></tr><tr><td>Chau &amp; Tam (1997), MISQ</td><td>Adopter or non-adopter</td><td>Inference &amp; estimation</td><td>Logit</td></tr><tr><td>Gefen &amp; Carmel (2008), MISQ</td><td>Identifying the winning bid</td><td>Inference &amp; estimation</td><td>Logit</td></tr><tr><td>Oh, Agarwal, &amp; Rao (2013), MISQ</td><td>Rumor</td><td>Inference &amp; estimation</td><td>Logit</td></tr><tr><td>Ye, Gao, &amp; Viswanathan (2014), MISQ</td><td>If strike</td><td>Inference &amp; estimation</td><td>Logit</td></tr><tr><td>Gao, Greenwood, Agarwal, &amp; Jeffrey (2015), MISQ</td><td>Online rating</td><td>Inference &amp; estimation</td><td>Logit</td></tr><tr><td>Chau &amp; Tam (1997), MISQ</td><td>Open systems adoption</td><td>Inference &amp; estimation</td><td>Logit</td></tr><tr><td>Ceccagnoli et al. (2012), MISQ</td><td>IPO</td><td>Inference &amp; estimation</td><td>LPM</td></tr><tr><td>Godinho de Matos, Ferreira, &amp; Krackhardt (2014), MISQ</td><td>Adopted</td><td>Inference &amp; estimation</td><td>Probit</td></tr><tr><td>Gopal &amp; Koka (2012), MISQ</td><td>Contract choice</td><td>Inference &amp; estimation</td><td>Probit</td></tr><tr><td>Overby &amp; Clarke (2012), MS</td><td>Choice</td><td>Inference &amp; estimation</td><td>Logit</td></tr><tr><td>Aral, Brynjolfsson, &amp; wu (2012), MS</td><td>HCM</td><td>Inference &amp; estimation</td><td>Logit</td></tr><tr><td>Miller &amp; Tucker (2009), MS</td><td>EMR productivity</td><td>Inference &amp; estimation</td><td>LPM</td></tr><tr><td>Adjerid et al. (2015), MS</td><td>HIE creation</td><td>Inference &amp; estimation</td><td>LPM</td></tr><tr><td>Forman et al. (2009), MS</td><td>Local Top</td><td>Inference &amp; estimation</td><td>LPM</td></tr><tr><td>Luca &amp; Zervas (2016), MS</td><td>Filtered reviews</td><td>Inference &amp; estimation</td><td>LPM</td></tr><tr><td>Bloom et al. (2014), MS</td><td>Plant manager autonomy</td><td>Inference &amp; estimation</td><td>Probit</td></tr><tr><td>Gray, Siemsen, &amp; Vasudeva (2015), MS</td><td>Inspection</td><td>Inference &amp; estimation</td><td>Probit</td></tr><tr><td>McElheran (2015), MS</td><td>E-buy, e-sell</td><td>Inference &amp; estimation</td><td>Probit</td></tr><tr><td>Griffith &amp; Northcraft (1996), MISQ</td><td>File</td><td>Inference &amp; estimation</td><td>Logit</td></tr><tr><td>Chen &amp; Forman (2006), MISQ</td><td>Adoption</td><td>Inference &amp; estimation</td><td>Probit</td></tr><tr><td>Meservy, Jensen, &amp; Fadel (2013), ISR</td><td>Choice</td><td>Inference &amp; estimation</td><td>Logit</td></tr><tr><td>Kuan et al. (2015), JAIS</td><td>Voting</td><td>Selection bias (2SLS)</td><td>Probit</td></tr><tr><td>Wang, Kannan, &amp; Ulmer (2013), ISR</td><td>Breach announcement</td><td>Selection bias (2SLS)</td><td>Logit</td></tr><tr><td>Gopal &amp; Sivaramakrishnan (2008), ISR</td><td>Contract choice</td><td>Selection bias (2SLS)</td><td>Probit</td></tr><tr><td>Goh, Heng, &amp; Lin (2013), ISR</td><td>Selection decision</td><td>Selection bias (2SLS)</td><td>Probit</td></tr><tr><td>Thirumalai &amp; Sinha (2013), ISR</td><td>Personalization</td><td>Selection bias (2SLS)</td><td>Probit</td></tr><tr><td>Kwon &amp; Johnson (2014), MISQ</td><td>Proactive</td><td>Selection bias (2SLS)</td><td>Probit</td></tr><tr><td>Mani, Barua, &amp; Whinston (2010), MISQ</td><td>IC choice</td><td>Selection bias (2SLS)</td><td>Probit</td></tr><tr><td>Chang &amp; Gurbaxani (2012), MISQ</td><td>Outsourcing</td><td>Selection bias (2SLS)</td><td>Probit</td></tr><tr><td>Gordon, Loeb, &amp; Sohail (2010), MISQ</td><td>Disclosure</td><td>Selection bias (2SLS)</td><td>Probit</td></tr><tr><td>Tafti, Mithas, &amp; Krishnan (2013), MS</td><td>Industry characteristics</td><td>Selection bias (2SLS)</td><td>Probit</td></tr><tr><td>Kalaignanam, Kushwaha, Steenkamp, &amp; Tuli (2013), MS</td><td>Private information</td><td>Selection bias (2SLS)</td><td>Probit</td></tr><tr><td>Chen &amp; Bharadwaj (2009), ISR</td><td>Process interdependence</td><td>Selection bias (2SLS)</td><td>Probit</td></tr></table>

Table A1. Results from Search of IS Literature for Regression Models for a Binary Dependent Variable (JAIS, ISR, MISQ, Management Science’s IS Section)

<table><tr><td>Tian &amp; Xu (2015), MISQ</td><td>Firm risk</td><td>Selection bias (2SLS)</td><td>Probit</td></tr><tr><td>Yin, Bond, &amp; Zhang (2014), MISQ</td><td>Helpful vote</td><td>Selection bias (2SLS)</td><td>Probit</td></tr><tr><td>Aggarwal, Gopal, Gupta, &amp; Singh (2012), ISR</td><td>Venture</td><td>Selection bias (2SLS)</td><td>Probit</td></tr><tr><td>Mani, Barua, &amp; Whinston (2012), ISR</td><td>Contract choice</td><td>Selection bias (2SLS)</td><td>Probit</td></tr><tr><td>Singh, Aggarwal, &amp; Cojuharenco (2015), MISQ</td><td>Funding decision</td><td>Selection bias (2SLS)</td><td>Probit</td></tr><tr><td>Susarla &amp; Barua (2011), ISR</td><td>Contract Choice</td><td>Selection bias (2SLS)</td><td>Probit</td></tr><tr><td>Mithas &amp; Krishnan (2009), ISR</td><td>MBA or non-MBA</td><td>Selection bias (PSM)</td><td>Logit</td></tr><tr><td>Rishika et al. (2013), ISR</td><td>Social media participation</td><td>Selection bias (PSM)</td><td>Logit</td></tr><tr><td>Ma, Montgomery, Singh, &amp; Smith (2014), ISR</td><td>Pirated or not</td><td>Selection bias (PSM)</td><td>Logit</td></tr><tr><td>Caliendo, Clement, Papies, &amp; Scheel-Kopeinig (2012), ISR</td><td>Installed spam filter</td><td>Selection bias (PSM)</td><td>Logit</td></tr><tr><td>Hinz, Spann, &amp; Hann (2015), ISR</td><td>Purchase</td><td>Selection bias (PSM)</td><td>Probit</td></tr><tr><td>Oestreicher-Singer &amp; Zalmanson (2013), MISQ</td><td>Subscribing decision</td><td>Selection bias (PSM)</td><td>Logit</td></tr><tr><td>Hyun Kim, Mukhopadhyay, &amp; Kraut (2016), MISQ</td><td>KMS</td><td>Selection bias (PSM)</td><td>Logit</td></tr><tr><td>Kohli, Devaraj, &amp; Ow (2012), MISQ</td><td>IT investment</td><td>Selection bias (PSM)</td><td>Logit</td></tr><tr><td>Smith &amp; Teland (2009), MISQ</td><td>Availability of bittorrent</td><td>Selection bias (PSM)</td><td>Probit</td></tr><tr><td>Kohli &amp; Devarah (2003), ISR</td><td>Positive vs. non-positive IT pay off studies</td><td>Classification and prediction</td><td>Logit</td></tr><tr><td>Hui et al. (2007), MISQ</td><td>To disclose or not to disclose</td><td>Classification and prediction</td><td>Logit</td></tr><tr><td>Schlereth &amp; Skiera (2017), MS</td><td>Choice probability</td><td>Classification and prediction</td><td>LPM</td></tr><tr><td>Bardhan et al. (2015), ISR</td><td>30 day readmission</td><td>Inference and prediction</td><td>Logit</td></tr><tr><td>Bapna, Goes, Wei, &amp; Zhang (2011), ISR</td><td>EPS adoption</td><td>Inference and prediction</td><td>Logit</td></tr><tr><td>Oestreicher-Singer &amp; Zalmanson (2012), MISQ</td><td>Subscribing decision</td><td>Inference and selection bias (PSM)</td><td>Logit</td></tr><tr><td>De, Hu, &amp; Rahman (2013), ISR</td><td>Returns</td><td>Inference and selection bias (PSM)</td><td>Logit &amp; probit</td></tr><tr><td>Hong, Wang, &amp; Pavlou (2015), ISR</td><td>Selection or contract</td><td>Inference and selection bias (PSM)</td><td>Logit</td></tr><tr><td>Liu et al. (2015), MISQ</td><td>Lending</td><td>Inference and selection bias (2SLS)</td><td>Logit &amp; probit</td></tr><tr><td>Tambe &amp; Hitt (2012), MS</td><td>Offshoring</td><td>Endogeneity (2SLS)</td><td>Probit</td></tr><tr><td>Aggarwal &amp; Singh (2013), MISQ</td><td>Choice decision</td><td>Inference and endogeneity (2SLS)</td><td>Logit &amp; probit</td></tr></table>

Table A2. Computation Times (in milliseconds) for the Simulated Model in Section 4.1 with Three Different Sample Sizes (50, 500, 50000); Estimated Timings Based on 100 Evaluations of Each Model

<table><tr><td>R function</td><td>N = 50</td><td>N = 500</td><td>N = 50000</td></tr><tr><td>Lm()</td><td>1.4</td><td>2</td><td>69</td></tr><tr><td>Glm(logit)</td><td>2.1</td><td>3.9</td><td>283</td></tr><tr><td>Glm(probit)</td><td>4.1</td><td>7.5</td><td>554</td></tr><tr><td>Brglm(logit)</td><td>11</td><td>18</td><td>1102</td></tr><tr><td>Brglm(probit)</td><td>53</td><td>61</td><td>2100</td></tr></table>

![](/api/attachments/BF8VDYHC/fulltext/images/5f106fd037c74c6c021d1de5d7ce9590139dc4ea1d7d12b4bf510e5fd36accf6.jpg)  
False positive rate

![](/api/attachments/BF8VDYHC/fulltext/images/ee9c0a84342bcc459789b438b474d95b5103c2370c276f85fec22f33b97a5536.jpg)

Figure A1. Comparison ROC and Distribution of Predicted Values for the Three Models (Logit, Probit and Linear Probability) on a Simulated Dataset  
![](/api/attachments/BF8VDYHC/fulltext/images/dd21a86ac5f522faf4bcbd943184936272d281254ce818ce9cab61df81f13c6d.jpg)  
Figure A2. Comparison of the Distribution of Auction Price Before and After Log and Box-Cox Transformations

![](/api/attachments/BF8VDYHC/fulltext/images/73da7ec2b3b6252c3658f031c59f1b659d5e6a953e9ec44332dd24d51a12849c.jpg)

![](/api/attachments/BF8VDYHC/fulltext/images/e370eeeb0c321b5b254c0eff1dfcc661a6cd1b9dca8485bfcdd3e2b0fc108016.jpg)  
Figure A3. Coefficient Significance<sup>10</sup> and Marginal Analysis for the Three Models (Logit, Probit and Linear Probability) on eBay Data Based on 100 Bootstrap Replications with Different Sample Sizes (n = {500, 5000, 50000}).

![](/api/attachments/BF8VDYHC/fulltext/images/b00e0a61ce2f890fc1d4fc0d7383cf6c87f6451706ca806df9a532b223ff051b.jpg)

![](/api/attachments/BF8VDYHC/fulltext/images/a970149c4fbba2d1417ebbd2e3e7a5e339f09d17b8a80208cbd09b4bc67e1027.jpg)  
Figure A4. Predicted Values (Left) and ROC Curves (Right) for the Three Models (Logit, Probit and Linear Probability) on Holdout eBay Data; The Continuous Covariates are Log Transformed

LPM Predictions  
![](/api/attachments/BF8VDYHC/fulltext/images/86a034487878d4f9163ce11e9df025dde52edb5b79117db1b80fa0abf7376f35.jpg)  
LPM Predictions

![](/api/attachments/BF8VDYHC/fulltext/images/5ff75d2f1ec3c31bbc5de4fb94ac0baaeb499719d2a8d40cc9ce085ce265b52c.jpg)  
Figure A5. Comparison of Predicted Values for Both Logistic Regression and a LPM for Two Datasets that Produce Bounded and Unbounded Predictions Respectively for a LPM

![](/api/attachments/BF8VDYHC/fulltext/images/8ecc8d327884660d1872c33b6afb0b0268cee7628662b123e83d6d0382072b12.jpg)

![](/api/attachments/BF8VDYHC/fulltext/images/bdb4582e588df0e6e76999d7c147bfebb2648f9d9b91bef8b0b6892d4b355f84.jpg)

![](/api/attachments/BF8VDYHC/fulltext/images/1475f4293bfe9b62169ea99c6b6c7db9bed3c5fcb0009f96b20bde54830d94fe.jpg)

![](/api/attachments/BF8VDYHC/fulltext/images/612274e75333ccee529b567542a88dfda67235c76c202e1d5ccc6fd191039654.jpg)  
Figure A6. Residual Diagnostics for the Logit Model on eBay Data Without Log Transforming the Three Continuous Covariates

## About the Authors

Suneel Babu Chatla is a doctoral student at the Institute of Service Science, National Tsing Hua University, Taiwan. He completed his Masters in Statistics from the University of Hyderabad, India.

Galit Shmueli is the Tsing Hua Distinguished Professor at the Institute of Service Science, National Tsing Hua University, Taiwan. She is also Director of the Center for Service Innovation & Analytics at NTHU's College of Technology Management. She earned her Masters and PhD in Statistics from the Technion – Israel Institute of Technology, and her BA in Psychology and Statistics from Haifa University. Her research focuses on statistical and data mining methodology with applications in information systems and healthcare. She authors multiple books and over 80 publications in peer-reviewed journals and books, including Management Science, Journal of the American Statistical Association, Journal of the Royal Statistical Society, Information Systems Research, MIS Quarterly, Journal of Business and Economic Statistics, Marketing Science, Statistical Science, Technometrics, and Proceedings of the National Academies of Science.

Copyright © 2017 by the Association for Information Systems. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and full citation on the first page. Copyright for components of this work owned by others than the Association for Information Systems must be honored. Abstracting with credit is permitted. To copy otherwise, to republish, to post on servers, or to redistribute to lists requires prior specific permission and/or fee. Request permission to publish from: AIS Administrative Office, P.O. Box 2712 Atlanta, GA, 30301-2712 Attn: Reprints or via email from publications@aisnet.org.
