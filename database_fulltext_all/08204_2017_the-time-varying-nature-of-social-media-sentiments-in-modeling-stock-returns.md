---
otero_id: 8204
otero_key: "6SMBQ8JF"
title: "The time-varying nature of social media sentiments in modeling stock returns"
authors: "Chi-San Ho; Paul Damien; Bin Gu; Prabhudev Konana"
year: "2017"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2017.06.001"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

The Time-Varying Nature of Social Media Sentiments in Modeling Stock Returns

Chi-San Ho, Paul Damien, Bin Gu, Prabhudev Konana

PII: S0167-9236(17)30102-1

DOI: doi:10.1016/j.dss.2017.06.001

![](/api/attachments/6SMBQ8JF/fulltext/images/14362b406f81d0d50d23aff256aa5bca1527903ce44815e66df928683e24772c.jpg)

Reference: DECSUP 12852

To appear in: Decision Support Systems

Received date: 13 January 2017

Revised date: 3 June 2017

Accepted date: 16 June 2017

Please cite this article as: Chi-San Ho, Paul Damien, Bin Gu, Prabhudev Konana, The Time-Varying Nature of Social Media Sentiments in Modeling Stock Returns, Decision Support Systems (2017), doi:10.1016/j.dss.2017.06.001

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# The Time-Varying Nature of Social Media Sentiments in Modeling Stock Returns

Chi-San Ho $^{a}$ , Paul Damien $^{a,*}$ , Bin Gu $^{b}$ , Prabhudev Konana $^{a}$

$^{a}$ McCombs School of Business, University of Texas at Austin, 2100 Speedway Stop B6500, Austin, TX 78712, USA

$^{b}$ W. P. Carey School of Business, Arizona State University, Main Campus PO BOX 874606, Tempe, AZ 85287, USA

## Abstract

The broad aim of this paper is to answer the following related queries: is the relationship between social media sentiments and stock returns time-varying? To provide a satisfactory response, a novel methodology—a symbiosis of Bayesian Dynamic Linear Models and Seemingly Unrelated Regressions—is introduced. Two sets of Dow Jones Industrial Average stock data and corresponding social media data from Yahoo! Finance stock message boards are used in a comprehensive empirical study. Some key findings are: (a) Affirmative response to the above question; (b) Models with only social media sentiments and market returns perform at least as well as models that include Fama-French and Momentum factors; (c) There are significant correlations between stocks, ranging from -0.8 to 0.6 in both data sets.

Keywords: Bayesian Inference; Seemingly Unrelated Regressions; Social Media Sentiments; Dynamic Linear Models; Markov Chain Monte Carlo

\*Corresponding Author:

Paul Damien, B.M. (Mack) Rankin, Jr., Professor of Business Administration

McCombs School of Business, University of Texas at Austin

2100 Speedway Stop B6500

## 1 Introduction

To better motivate this paper's contributions to the literature on social media sentiments vis-a-vis their relationship to stock returns, the introduction comprises two subsections wherein the first one offers a comparative literature review, followed by an overview of this study.

## 1.1 Motivation and Related Literature

Opinions about stocks, products, businesses etc., on social media sites such as social networks, virtual communities, and microblogging services (e.g., Twitter) are ubiquitous. Numerous methodologies have been proposed for mining opinions and emotions usually referred to as social media sentiments. These sentiments have applications in a variety of market services and investment settings; see, as examples, [7], [20], [21], and [27]. Importantly, social media facilitate interactions among members who find relevant information and make decisions. Several commercial products (e.g., SAS Social Media Analytics, Radian6, Socialmention) incorporate tools to extract sentiments. The ability to use social media sentiments for stock prediction has attracted significant interest in academia and industry. As one example, TDAmeritrade, an online stock broker, allows investors to post and view sentiments of stocks and trade directly from this interface. In this regard, the growing consensus was best captured by PredictWallStreet on their website:

"The idea is simple. You share your opinion on whether you think a stock or index will go up or down. PredictWallStreet combines all the predictions it receives and provides information about the community sentiment, accuracy of the community predictions as well as forecasts for individual stocks, ETFs and indices. Since the stock market moves based on the collective thinking of thousands of individuals, the more people who make predictions on PredictWallStreet, the more potentially useful the information becomes."

This “wisdom of the crowd” provides market sentiments that can be a proxy for the market mood. For instance, one of the largest social media sites for stock related activity is Yahoo! Finance. In January 2014, ComScore Media Metrix reports that Yahoo! Finance received 39.6 million unique visitors while AOL's Money and Finance had 19.8 Million visitors. Some stocks attract over 1000 messages per day on Yahoo! Finance alone; see, [14].

There is substantial literature on the theoretical pros and cons of social media sentiments and their relationship to modeling stock returns and other metrics; as examples [2, 3, 12, 19, 21, 23, 28]. Recently, Sul et al. [25] study the predictability of returns, based on sentiments expressed on Twitter. Using a multiple linear regression model, they conclude that “sentiment in tweets about a specific firm from users with less than 171 followers...had a significant impact on the stock’s returns on the next trading day, the next 10 days, and the next 20 days.” Similarly, He et al. [15] find that negative sentiments on Tweets could predict a firm’s future stock prices.

Another theoretical argument to study social media sentiments is often described as follows: First, given the magnitude of investor attention in these forums, social media sentiments from these forums capture retail investors' sentiments on individual stocks which are known to influence short-term stock performance ([4], [10]). Second, users on social media may have access to insider information. Postings by insiders could reveal information beyond what is publicly disclosed which influence future stock performance ([3], [13]).

Thus, social media may reveal private information or market imperfections that can be exploited for prediction of stock prices. The efficient market hypothesis (EMH) argues that prices fully reflect all known information, and that it is difficult to seek excess returns; see [22]. Hirshleifer [16] provides an overview of psychological and behavioral arguments for mis-pricing; see, also, [18] and [26]. Bounded rationality also suggests that individuals may fail to account for repeated information and are subjected to greater bias ([11]). However, discussions in social media may reflect investors' perceptions, emotions, and heuristics. These sentiments may lead stock prices rather than lag; if so, there are opportunities for at least short-term predictions of stock returns.

Three aspects of social media have been closely studied: sentiments, activity, and agreement. Sentiments capture bullishness or bearishness of online postings. Activity measures the overall level of interests in discussing a stock. Finally, agreement assesses convergence of opinion among posts. Sentiments such as bullish, bearish, neutral and agreement are often difficult to extract from messages because of the volume and noise ([2], [9]). Antweiler et al. [2] found that the effect of message board sentiments on stock returns was negative and statistically insignificant. However, they show that activity (i.e., number of messages) and agreement have significant predictability of stock volatility.

## 1.2 Aims of this Research

Our main focus is to examine a possible dynamic relationship between social media sentiments and future stock returns. This is worthy of study, since models of behavioral finance suggest that investor sentiments could both underreact and overreact to underlying fundamentals; indeed, it is this uncertainty that creates risks for arbitrageurs ([4], [10]). This gap between the empirical literature and analytic models highlights the need to develop a method that allows for a dynamic relationship between sentiments and future stock returns. Here we tackle this issue via a combination of Bayesian Dynamic Linear Models (DLMs) and Seemingly Unrelated Regressions (SURs); see, [29] and [30].

Unlike traditional regression models, our first methodological innovation, via DLMs, allows sentiment regression coefficients to vary over time. This enables us to capture both over-reaction and under-reaction by investors. DLMs differ from traditional random coefficients models; the latter allows regression parameters to be stochastic but not time-varying. The second methodological contribution is the introduction of the SUR approach within a DLM framework. The traditional linear regression model and DLM assumes no cross-correlation between stock returns. The SUR approach allows us to investigate multiple stocks as systems of equations by explicitly modeling the cross-correlations between returns, leading to statistically better estimates of the variances of regression parameters. Thus, the DLM and SUR approaches serve different and useful purposes. By exploiting the merits of both, we model stock returns data as a dynamic function of social media sentiments.

At the outset, it is worth mentioning other models different than our approach, and which have been used in the stock returns literature. ARIMA models, such as GARCH and EGARCH, are primarily used to address volatility, hence they are broadly classified as stochastic volatility models. We do not model volatility. Rather, our focus is on understanding the time-varying behavior of social media regression parameters and their impact on prediction. If the aim were to model stochastic volatility, then GARCH or its variants would be viable choices.

Our SUR-DLM framework is quite different than the approach taken in, for example, [17]. In their model, “beta” refers to a firm’s beta in a CAPM model. The authors then model that beta as a stochastic process, resulting in a Bayesian formulation via MCMC. This is very different than the

# ACCEPTED MANUSCRIPT

research agenda for our paper.

At times, data mining has been used to formulate new regressors (labeled “mood trends”) before executing a standard multiple linear regression to assess if these regressors are statistically significant ([5]). We do not mine new regressors.

Finally, methodologically, many of the above references (such as [5] and [25]) use multiple linear regression which is a (static) special case of the SUR model used in our paper. Importantly, our focus is to use social media sentiments gathered from message boards on Yahoo! Finance, and study their relevance in predicting stock returns when such sentiments are treated as time-varying. Note that even though our focus is not on Twitter-based sentiments, the mathematical approach taken here would readily apply to such data, and related ones, as well.

Saving the details for later, here we briefly highlight some of the key findings from this study. First, the impact of social media sentiments on future stock returns vary over time. Second, there is considerable correlation between stocks. Third, the time-varying social media sentiments coefficients are more stable in 2011 when compared to 2009; the latter was a period of high turbulence due to recession. Fourth, adding Fama-French or Momentum factors ([6]) underperforms a model with just social media sentiments and market returns; that is, the prediction errors are significantly larger compared to a model with just social media sentiments and market returns.

Section 2 details the methodology and Section 3 describes the data. Section 4 provides a comprehensive empirical study, followed by conclusions in Section 5.

## 2 Methodology

The intuition underlying a DLM is simple yet powerful. At any time t, the observed data $y_{t}$ is perturbed by noise (or error), $u_{t}$ . The expected value of $y_{t}$ is modeled via the regression term $X\beta$ . The thrust of the DLM is to allow the $\beta$ vector to evolve over time, which in turn would affect the expected value to evolve as well. The OLS estimation is a special case when $\beta$ is fixed. Likewise, the DLM is more general than the traditional random coefficients model where the coefficient is random with a fixed mean. The evolutionary dynamics of $\beta$ , typically, is modeled as an autoregressive process with additional noise (or error) over time, say $v_{t}$ . The error $u_{t}$ is called the observation error, while $v_{t}$ is called the system error, leading to two inter-related equations, namely the Observation and

System (or State) equations. Following West and Harrison [29], the observation equation is given by

$$
y _ {t} = X _ {t} ^ {\prime} \beta_ {t} + u _ {t} u _ {t} \sim N _ {p} (0, U _ {t}), t = 1, \dots , n,\tag{1}
$$

and the system regression equation

$$
\beta_ {t} = G _ {t} \beta_ {t - 1} + v _ {t} v _ {t} \sim N _ {q} (0, V _ {t}).\tag{2}
$$

Note that one obtains the standard multiple linear regression model if the systems equation is ignored. We assume that the $u_{t}$ and $v_{t}$ are mutually independent; the matrix $G$ is assumed known. Also, the system equation above is an autoregression of order one. In general, one could include higher order terms. For our application, we found a first order systems equation model was sufficient since adding more terms may lead to over-fitting; [29] also caution the use of these models in the direction of parsimony.

For both estimation and prediction, the first goal is to find the posterior distributions of $\beta_{t}$ , $t = 1, \cdots, n$ . With prior distributions for the vector of these slopes, $U_{t}$ , $V_{t}$ (or the ratio $V_{t}/U_{t}$ ), it is possible to obtain the posterior distributions of all the random variables in the model. This would correspond to the Estimation Phase of the DLM. One could then derive the predictive distribution of stock returns in the Prediction Phase. Details are provided in the Appendix.

## 2.1 Seemingly Unrelated Regression (SUR) Model

In a traditional linear regression model for stock returns, in matrix notation, one would have,

$$
y = X \beta + u,\tag{3}
$$

where y is the vector of stock returns, X is the matrix of regressors (social media sentiments, market returns, Fama-French, Momentum Factors, etc.), $\beta$ is a vector of unknown but fixed parameters and u is random error, which is typically assumed to be normally distributed with zero mean and unknown variance-covariance matrix, $\Sigma$ . The parameter vector $\beta$ is estimated via OLS. The above model assumes no correlations between various stock returns.

In contrast, the SUR approach ([1], [30]) explicitly models the correlations between stock returns.

# ACCEPTED MANUSCRIPT

For the moment, assume the regression parameter vector $\beta$ to be fixed in time, but unknown; later, we will make it time-varying, random and unknown. Let j denote the return on the jth stock and M denote the total number of stocks. Let n be the total number of observations (in days) for each stock. We have:

$$
\begin{array}{l} y _ {j} = X _ {j} \beta_ {j} + u _ {j}, j = 1, \ldots , M, \\ \text { with } E [ u _ {i} u _ {j} ^ {\prime} ] = \left\{ \begin{array}{l l} \omega_ {i j} I, & (i \neq j) \\ \omega_ {i} ^ {2} I, & (i = j); \end{array} \right. \end{array}\tag{4}
$$

$y_{j}$ and $u_{j}$ are $n \times 1$ vectors, $X_{j}$ is an $n \times p_{j}$ matrix of rank $p_{j}$ of observations, and $\beta_{j}$ is a $p_{j}$ -dimensional coefficient vector. The domain of parameter values are given as follows: $\beta_{j} \in \mathbb{R}^{p_{j}}$ , $(j = 1, \ldots, M)$ , $\omega_{ij} \in \mathbb{R}$ , $(i, j = 1, \ldots, M, i \neq j)$ and $\omega_{j} \in \mathbb{R}_{>0}$ , $(j = 1, \ldots, M)$ . This system of equations extends the traditional multiple linear regression model to include two critical and practically useful features:

\- The error terms in each equation are allowed to be correlated. Since each equation represents a particular stock's returns, this assumption implies that the model accounts for correlations between these stock returns. Clearly this is a useful feature to impose: businesses competing in the same market would likely have negative correlations in their returns, while those participating in the same ecosystem might have positive correlations.

\- Each equation in the system could have different independent variables (or regressors) and variances. This is also a reasonable assumption, for there is no a priori reason to suppose that each of the stocks in the Dow Jones Industrial Average (DJIA) require the same set of regressors to explain and predict it. The same argument could also apply to the volatilities in these stock returns.

It is convenient to express the SUR model using matrix notation:

$$
y = X \beta + u,\tag{5}
$$

$u \sim N(0, \Omega \otimes I)$ , where $N(\mu, \Sigma)$ denotes the normal distribution; $\otimes$ is the tensor product; $\Omega$ is an $M \times M$ symmetric matrix with diagonal elements $\omega_1^2, \ldots, \omega_M^2$ , and the off-diagonal $ij$ th elements are $\omega_{ij}; y' = (y_1', \ldots, y_M')$ ; $X = \mathrm{diag}(X_1, \ldots X_M)$ ; $\beta' = (\beta_1', \ldots, \beta_M')$ ; and $u' = (u_1', \ldots, u_M')$ .

The normal likelihood function for the above model is given by:

$$
L (y \mid \beta , \Omega) = \frac {1}{(2 \pi) ^ {n M / 2} \mid \Omega \mid^ {n / 2}} \exp \left[ - \frac {1}{2} \mathrm{tr} \left\{R \Omega^ {- 1} \right\} \right],\tag{6}
$$

where “tr” denotes the trace of a matrix; $|\Omega|=\det(\Omega)$ is the determinant of $\Omega$ ; and the ijth element of the $M\times M$ matrix R is $r_{ij}$ and $r_{ij}=(y_{i}-X_{i}\beta_{i})^{\prime}(y_{j}-X_{j}\beta_{j})$ .

It is possible to estimate the parameters of the SUR model using a non-Bayesian approach. But later we imbed the SUR into a DLM framework to allow the regression vector, $\beta$ , to vary over time, thus requiring a Bayesian approach to estimation and prediction ([29]). Also, Zellner [30] offers compelling reasons why a Bayesian approach to the SUR model is preferred over standard estimation methods.

To complete the Bayesian specification, following Zellner [30], consider Jeffrey's invariant prior for $(\beta, \Omega)$ , where $\pi(.)$ denotes a prior distribution:

$$
\pi (\beta , \Omega) = \pi (\beta) \pi (\Omega) \propto | \Omega | ^ {- \frac {M + 1}{2}},\tag{7}
$$

where the last term above is the square root of the determinant of the Fisher information matrix. Jeffery's prior is invariant under any one-to-one re-parametrization of the model and, as a result, is frequently used in the literature. The theoretical notion of invariance is somewhat involved. Intuitively, Jeffrey's prior is appealing when used with scale parameters. That is, it does not matter, for instance, if one characterizes the model, say using the variance or standard deviation; the prior is valid under both of these scale parametrizations.

The posterior joint density function, by Bayes' theorem, is given by:

$$
g (\beta , \Omega \mid Y, X) \propto | \Omega | ^ {- (n + M + 1) / 2} \exp \left[ - \frac {1}{2} \mathrm{tr} \left\{R \Omega^ {- 1} \right\} \right].\tag{8}
$$

From the above, given that one assumes prior distributions on $\beta$ and $\Omega$ , these quantities are random and unknown. This is in sharp contrast to standard linear regressions where they are fixed and unknown. Also, $\beta$ is not time-varying in the above SUR model: later, when we include the SUR into a DLM, the $\beta$ vector will also become time-varying.

In regression, the two goals of any statistical inference procedure are to explain the impact of the regressors on the dependent variable and to predict future values of the dependent variable. For

# ACCEPTED MANUSCRIPT

the above model, it is relatively straightforward to construct a Markov chain Monte Carlo (MCMC) method, namely a Gibbs Sampler to accomplish both these goals; see, [1] and [8]. To implement a Gibbs sampler, we first need to derive the conditional distributions of the unknown, random parameters; these distributions need to be known only up to proportionality.

\- ESTIMATION PHASE: The posterior conditional distributions $g(\beta \mid \Omega, Y, X)$ and $g(\Omega \mid \beta, Y, X)$ are:

$$
g (\beta \mid \Omega , Y, X) = N (\hat {\beta}, \hat {\Omega} _ {\beta}),
$$

$$
\text { and } \quad g (\Omega \mid \beta , Y, X) = I W (R, n)\tag{9}
$$

where $IW(\cdot,\cdot)$ denotes the inverse Wishart distribution, and

$$
\hat {\beta} = \left\{X ^ {\prime} (\Omega^ {- 1} \otimes I) X \right\} ^ {- 1} X ^ {\prime} (\Omega^ {- 1} \otimes I) \cdot y,
$$

$$
\hat {\Omega} _ {\beta} = (X ^ {\prime} (\Omega^ {- 1} \otimes I) X) ^ {- 1}
$$

Note that the estimation of $\hat{\beta}$ has the same form as the classical method; see [30]. As a result of using Jeffery's prior, the estimated regression coefficients will be very close to those from the classical method. However, unlike the classical method, in this Bayesian model one can obtain the complete predictive distribution of the stock returns vector $y$ , to which we now turn.

\- PREDICTION PHASE: The predictive distribution for a future vector of stock returns, $y$ , given $x$ , $\beta$ and $\Omega$ is derived as follows. With $y_j$ denoting the $j$ th stock's return, let $y_j$ be an $n \times 1$ vector. At time, say $n + 1$ , what is the distribution of $y_j^{n+1}$ given $\beta$ , $\Omega$ and the $(n + 1)$ th row in each of the regressor matrices $X_j$ ? To answer this, first stack all the $y$ values we want to predict at time $n + 1$ ; that is, the $y_j^{n+1}$ are stacked and denoted as $Y_{n+1}$ ; likewise the augmented $X$ matrix is $\text{diag}\{X_1^{n+1}, \ldots, X_M^{n+1}\}$ . To directly sample from $Y_{n+1}$ is difficult. However, we can achieve this easily via the Gibbs sampler from the Estimation Phase ([24]). We have:

$$
f (Y _ {n + 1} \mid X, \beta , \Omega) = N (X \beta , \Omega)\tag{10}
$$

$$
f (\beta \mid \Omega , Y _ {n + 1}, X) = N (\hat {\beta}, \hat {\Omega} _ {\beta})
$$

$$
\text { and } f (\Omega \mid \beta , Y _ {n + 1}, X) = I W (R, n + 1).\tag{11}
$$

Let us recap the value of the Bayesian SUR model: it explicitly models the cross-correlations between the $M$ stock returns via the system of equations. Second, the regression parameter vector $\beta$ is random; hence we are able to obtain its posterior distribution rather than a point estimate. Hence, the regression coefficient on social media sentiments could evolve each day due to market dynamics or system noise: this is in addition to the noise one observes in stock returns data which is conventionally called observation error. To allow the regression coefficient vector $\beta$ in the Bayesian SUR model to evolve over time, we will embed the SUR component into a DLM. Finally, one can obtain the entire predictive distribution for each stock at any future point in time.

## 2.2 SUR model with dynamic coefficients

Since one of the main aims of the paper is to assess the impact of social media sentiments on future stock returns, we use the DLM for the regression parameters corresponding to social media sentiments; that is, we allow its regression coefficients to be time-varying in all the equations in the SUR model. The remaining regression parameters are assumed to be non time-varying but still random. We have:

$$
\begin{array}{c} y _ {j t} = \alpha_ {j} + X _ {j t} \beta_ {j t} + Z _ {j t} \gamma_ {j} + u _ {j t} \\ \beta_ {j t} = \beta_ {j t - 1} + v _ {j t} \\ \text {for j = 1,\ldots,M,}\quad t = 1, \ldots , n, \end{array}\tag{12}
$$

where $y_{jt}$ , $\alpha_{j}$ , $X_{jt}$ , $\beta_{jt}, u_{jt}$ , $v_{jt}$ are scalars and in particular, $X_{jt}$ corresponds to the time-varying regressors, namely social media sentiments. The $Z_{jt}$ are $1 \times p_{j}$ vectors and $\gamma_{j}$ are $p_{j} \times 1$ vectors, corresponding to non-time-varying (or static) regressors and coefficients which may include Fama-French factors and market returns. A listing of these static regressors for each model in our study is provided in the next section.

Let $u_{t} = (u_{1t},\dots,u_{Mt})^{T}$ and $v_{t} = (v_{1t},\dots,v_{Mt})^{T}$ , then

$$
u _ {t} \sim i. i. d. N _ {M} (0, \Omega) \text {   and   } v _ {t} \sim i. i. d. N _ {M} (0, \Sigma),
$$

where $\Sigma = A\Omega A$ . $A$ is a diagonal matrix, $\{A\}_{jj} = ((1 - \delta_j) / \delta_j)^{\frac{1}{2}}$ , where $0 < \delta_j < 1$ specifies the signal to noise ratio.

What is the role of $\delta_j$ ? Note that when $\delta_j \to 1$ , the contribution of the error or noise from the system equation to the observation equation (via $\Omega$ ) declines. In practice, the $\delta_j$ s are assumed known, typically 0.9 to 0.99 ([29]). On the other hand, it is also possible to allow $\delta_j$ to be random. In the Appendix we develop the mathematics in its most general form where we let the $\delta_j$ s be random. The key point is the $\delta_j$ s specify the strength of the relationship between $\Omega$ and $\Sigma$ , namely the covariances in the observation and system equations, respectively. Thus, as the $\delta_j$ s approach one, the estimation of the regression parameters are less dependent on the noise from the system equations. In our context, this would mean that as the $\delta_j$ s approach one, the time volatility in the slopes of the social media sentiment coefficients are more impacted by the observation error in the stock returns data than the dynamics stemming from the system error.

Given $\delta_{j}$ , the random, unknown parameters in our DLM-SUR model are collected together in the vector $\Theta = \{\alpha_{j}, \beta_{j,1:n}, \gamma_{j}, \Omega\}$ ; in this vector, the only component that is time-varying is the collection of regression slopes, generically denoted as $\beta$ . The data are collected together in the vector $D_{n} = \{y_{j,1:n}, X_{j,1:n}, Z_{j,1:n}\}$ , where the first, second and third components correspond, respectively, to the stock returns, the regressors whose coefficients vary in time, and the regressors whose coefficients are fixed in time. Combining Jeffery's prior for the SUR model parameters with the prior distribution for the DLM parameters, the prior joint distribution for $\Theta$ is given by:

$$
\pi (\Theta) \propto \pi (\Omega) \pi (\beta_ {0}) \propto | \Omega | ^ {- \frac {M + 1}{2}} \cdot N _ {M} (m _ {0}, C _ {0}).\tag{13}
$$

In the above, all parameters with a subscript 0 correspond to those from the DLM component of the model. Since the posterior distribution of $\Theta$ will not have a closed form solution, we would have to use MCMC methods for the estimation and prediction phases of the analysis. To this end, like before, a Gibbs sampler algorithm is derived. Saving the details for the Appendix, to execute a Gibbs sampler for the combined DLM-SUR system of equations, we need the following conditional distributions to sample the various components in $\Theta$ and the predictive distribution of $Y_{n + 1}$ .

$$
f (\alpha_ {1: M} | D _ {n}, \Theta / \{\alpha_ {1: M} \}) \sim N _ {M} (\mu_ {\alpha}, \Sigma_ {\alpha})\tag{14}
$$

$$
f (\gamma | D _ {n}, \Theta / \{\gamma_ {1: M} \}) \sim N _ {P} (\mu_ {\gamma}, \Sigma_ {\gamma})\tag{15}
$$

$$
f (\beta_ {j, 1: n} | D _ {t}, \Theta / \{\beta_ {j, 1: n} \}) \sim F F B S\tag{16}
$$

$$
f (\Omega | D _ {n}, \Theta / \{\Omega \}) \sim I W (R, T),\tag{17}
$$

$$
f (Y _ {n + 1} | D _ {n + 1}, \Theta) \sim N _ {M} (\mu_ {p}, \Sigma_ {p}),\tag{18}
$$

where $FFBS$ stands for Filter Forward Backward Sampling algorithm, $N$ denotes the normal distribution and $IW$ denotes the inverse-Wishart distribution. In the above, the notation $f(\alpha_{1:M}|D,\Theta/\{\alpha_{1:M}\})$ means the posterior conditional distributions of $\alpha_{1:M}$ given the data, $D$ , and all the other parameters in the vector $\Theta$ excluding the $\alpha_{1:M}$ parameters; likewise for all the other conditional distributions shown above. Thus, the Gibbs sampler will generate samples from the posterior distributions of all the random parameters in the model. This is the estimation phase. The equations for the prediction phase are detailed in the Appendix. Basically, for the latter phase, one uses the samples from the estimation phase to approximate the integrals corresponding to the predictive densities of each stock return at each time point.

## 3 Data Description

The datasets consist of message posts collected from Yahoo! Finance from January 2009 to June 2009 and from June 2011 to June 2012. Given the large number of stock message boards and the amount of time it takes to collect posts, for our analysis, we chose stocks from a well-known market index, the Dow Jones Industrial Average (DJIA) $^{1}$ , as a representative set of large-cap stocks. The choice of data is similar to Antweiler and Frank (2004) who considered 45 stocks drawn from two stock indices, namely DJIA and Dow Jones Internet Commerce Index (XLK). The descriptive statistics for the data are in Tables 1 and 2.

The data on social media sentiment measures range from -2 to 2, where -2 represents a strong sell signal, +2 represents a strong buy signal, and 0 represents a hold signal. Note that these values do not represent agreement, bearishness, and bullishness. The sentiment posts are self-declared sentiments. Where appropriate, standard averaging was used to encapsulate these data. Messages without self-declared sentiments were excluded. If there were no self-declared messages for a stock on a given day, we imputed it to represent a “hold”. This may be debatable but it is a reasonable assumption, especially in conjunction with the large number of messages. Importantly, if one brings in the fact that most investors are risk averse, then neutrality, in our context, could be far more difficult to justify than “hold”. Table 2 shows the maximum messages for each of the stocks in the 2011 dataset. Due to copious changes on the Yahoo! Finance website, we could not retrieve similar data for 2009.

## 4 Analysis

The following abbreviations are used throughout the discussion of the analysis. SR: stock returns; MR: market returns; CS: weighted social media sentiment; SMB: Fama-French small market capitalization minus big market capitalization factor; HML: Fama-French high book-to-market ratio minus low book-to-market ratio factor; UMD: momentum factor. All the independent variables are lagged one time period. This is because we are interested in stock returns at time t given the independent regressor values at time t-1. That is, we are interested in forecasting one-step ahead since investment decisions (such as buy, hold or sell) are made ex ante. However, in CAPM, market returns and other factors are usually treated contemporaneously.

## 4.1 Modeling and Parameter Estimation

For each data set, we construct three models to compare the predictability of CS versus the full-factor Fama-French/momentum models. Model 1 includes the dynamic CS regressor and the static Market Return factor; the second is the SUR model with the static Fama-French and momentum factors; and the third is the DLM-SUR model with CS, Fama-French and momentum factors. Table

Table 1: Descriptive statistics for 2009 data set

<table><tr><td colspan="2"></td><td colspan="2">Daily Returns</td><td colspan="2">Daily Sentiment</td></tr><tr><td>Company</td><td>Ticket</td><td>Mean</td><td>SD</td><td>Mean</td><td>SD</td></tr><tr><td>Alcoa</td><td>AA</td><td>0.40%</td><td>0.27%</td><td>1.00</td><td>0.07</td></tr><tr><td>American Express</td><td>AXP</td><td>0.47%</td><td>0.22%</td><td>-0.47</td><td>0.10</td></tr><tr><td>Boeing</td><td>BA</td><td>0.22%</td><td>0.16%</td><td>0.20</td><td>0.09</td></tr><tr><td>Bank of America</td><td>BAC</td><td>0.14%</td><td>0.24%</td><td>0.91</td><td>0.03</td></tr><tr><td>Citigroup</td><td>C</td><td>0.16%</td><td>0.34%</td><td>1.03</td><td>0.04</td></tr><tr><td>Caterpillar</td><td>CAT</td><td>0.47%</td><td>0.22%</td><td>0.16</td><td>0.09</td></tr><tr><td>Chevron</td><td>CVX</td><td>0.14%</td><td>0.11%</td><td>0.66</td><td>0.09</td></tr><tr><td>DuPont</td><td>DD</td><td>0.25%</td><td>0.18%</td><td>0.67</td><td>0.08</td></tr><tr><td>Walt Disney</td><td>DIS</td><td>0.28%</td><td>0.15%</td><td>0.69</td><td>0.10</td></tr><tr><td>General Electric</td><td>GE</td><td>0.24%</td><td>0.20%</td><td>0.61</td><td>0.05</td></tr><tr><td>Home Depot</td><td>HD</td><td>0.18%</td><td>0.13%</td><td>0.15</td><td>0.10</td></tr><tr><td>Hewlett-Packard</td><td>HPQ</td><td>0.24%</td><td>0.11%</td><td>-0.13</td><td>0.06</td></tr><tr><td>IBM</td><td>IBM</td><td>0.19%</td><td>0.10%</td><td>0.30</td><td>0.08</td></tr><tr><td>Intel</td><td>INTC</td><td>0.19%</td><td>0.14%</td><td>0.99</td><td>0.05</td></tr><tr><td>Johnson &amp; Johnson</td><td>JNJ</td><td>0.11%</td><td>0.07%</td><td>0.91</td><td>0.08</td></tr><tr><td>JP Morgan Chase</td><td>JPM</td><td>0.18%</td><td>0.19%</td><td>-1.43</td><td>0.04</td></tr><tr><td>Kraft</td><td>KFT</td><td>0.08%</td><td>0.11%</td><td>0.31</td><td>0.08</td></tr><tr><td>Coca-Cola</td><td>KO</td><td>0.15%</td><td>0.08%</td><td>0.59</td><td>0.08</td></tr><tr><td>McDonald&#x27;s</td><td>MCD</td><td>0.08%</td><td>0.09%</td><td>0.82</td><td>0.09</td></tr><tr><td>3M</td><td>MMM</td><td>0.27%</td><td>0.12%</td><td>0.29</td><td>0.07</td></tr><tr><td>Merck</td><td>MRK</td><td>0.24%</td><td>0.14%</td><td>0.47</td><td>0.11</td></tr><tr><td>Microsoft</td><td>MSFT</td><td>0.21%</td><td>0.14%</td><td>0.79</td><td>0.06</td></tr><tr><td>Pfizer</td><td>PFE</td><td>0.18%</td><td>0.12%</td><td>1.48</td><td>0.05</td></tr><tr><td>Procter &amp; Gamble</td><td>PG</td><td>0.15%</td><td>0.10%</td><td>0.90</td><td>0.08</td></tr><tr><td>AT&amp;T</td><td>T</td><td>0.13%</td><td>0.10%</td><td>0.77</td><td>0.07</td></tr><tr><td>United Technologies</td><td>UTX</td><td>0.25%</td><td>0.12%</td><td>0.26</td><td>0.06</td></tr><tr><td>Verizon Communications</td><td>VZ</td><td>0.09%</td><td>0.10%</td><td>0.79</td><td>0.09</td></tr><tr><td>Wal-Mart</td><td>WMT</td><td>0.09%</td><td>0.07%</td><td>1.22</td><td>0.05</td></tr><tr><td>Exxon Mobil</td><td>XOM</td><td>0.00%</td><td>0.11%</td><td>0.57</td><td>0.08</td></tr><tr><td>Market return (S&amp;P 500)</td><td>^GSPC</td><td>0.17%</td><td>0.10%</td><td></td><td></td></tr></table>

SD : standard deviation

Table 2: Descriptive statistics for 2011 data set

<table><tr><td rowspan="2">Company</td><td rowspan="2">Ticket</td><td colspan="2">Daily Return</td><td colspan="2">Daily Sentiment</td><td rowspan="2">Maximum# of Messages</td></tr><tr><td>Mean</td><td>SD</td><td>Mean</td><td>SD</td></tr><tr><td>Alcoa</td><td>AA</td><td>-0.20%</td><td>0.17%</td><td>0.69</td><td>0.05</td><td>89</td></tr><tr><td>American Express</td><td>AXP</td><td>0.06%</td><td>0.12%</td><td>0.00</td><td>0.07</td><td>4</td></tr><tr><td>Boeing</td><td>BA</td><td>-0.01%</td><td>0.12%</td><td>0.49</td><td>0.07</td><td>10</td></tr><tr><td>Bank of America</td><td>BAC</td><td>-0.09%</td><td>0.25%</td><td>0.60</td><td>0.03</td><td>374</td></tr><tr><td>Caterpillar</td><td>CAT</td><td>-0.03%</td><td>0.15%</td><td>1.02</td><td>0.04</td><td>48</td></tr><tr><td>Cisco</td><td>CSCO</td><td>0.03%</td><td>0.13%</td><td>1.01</td><td>0.04</td><td>116</td></tr><tr><td>Chevron</td><td>CVX</td><td>0.01%</td><td>0.11%</td><td>1.01</td><td>0.05</td><td>12</td></tr><tr><td>DuPont</td><td>DD</td><td>0.01%</td><td>0.12%</td><td>0.16</td><td>0.05</td><td>4</td></tr><tr><td>Walt Disney</td><td>DIS</td><td>0.08%</td><td>0.12%</td><td>0.49</td><td>0.06</td><td>18</td></tr><tr><td>General Electric</td><td>GE</td><td>0.03%</td><td>0.12%</td><td>0.15</td><td>0.04</td><td>46</td></tr><tr><td>Home Depot</td><td>HD</td><td>0.17%</td><td>0.10%</td><td>0.14</td><td>0.07</td><td>8</td></tr><tr><td>Hewlett-Packard</td><td>HPQ</td><td>-0.16%</td><td>0.16%</td><td>0.41</td><td>0.05</td><td>97</td></tr><tr><td>IBM</td><td>IBM</td><td>0.07%</td><td>0.09%</td><td>0.67</td><td>0.07</td><td>54</td></tr><tr><td>Intel</td><td>INTC</td><td>0.09%</td><td>0.10%</td><td>1.59</td><td>0.02</td><td>64</td></tr><tr><td>Johnson &amp; Johnson</td><td>JNJ</td><td>0.00%</td><td>0.06%</td><td>0.58</td><td>0.06</td><td>10</td></tr><tr><td>JP Morgan Chase</td><td>JPM</td><td>-0.04%</td><td>0.17%</td><td>-0.49</td><td>0.06</td><td>216</td></tr><tr><td>Kraft</td><td>KFT</td><td>0.06%</td><td>0.06%</td><td>0.42</td><td>0.05</td><td>6</td></tr><tr><td>Coca-Cola</td><td>KO</td><td>0.06%</td><td>0.07%</td><td>0.49</td><td>0.05</td><td>7</td></tr><tr><td>McDonald&#x27;s</td><td>MCD</td><td>0.05%</td><td>0.07%</td><td>0.73</td><td>0.06</td><td>20</td></tr><tr><td>3M</td><td>MMM</td><td>-0.01%</td><td>0.11%</td><td>0.29</td><td>0.04</td><td>4</td></tr><tr><td>Merck</td><td>MRK</td><td>0.05%</td><td>0.08%</td><td>0.24</td><td>0.06</td><td>6</td></tr><tr><td>Microsoft</td><td>MSFT</td><td>0.09%</td><td>0.10%</td><td>0.90</td><td>0.03</td><td>36</td></tr><tr><td>Pfizer</td><td>PE</td><td>0.04%</td><td>0.09%</td><td>0.86</td><td>0.06</td><td>15</td></tr><tr><td>Procter &amp; Gamble</td><td>PG</td><td>-0.01%</td><td>0.06%</td><td>0.60</td><td>0.06</td><td>11</td></tr><tr><td>AT&amp;T</td><td>T</td><td>0.07%</td><td>0.07%</td><td>0.38</td><td>0.05</td><td>42</td></tr><tr><td>Travelers Companies</td><td>TRV</td><td>0.03%</td><td>0.11%</td><td>0.15</td><td>0.04</td><td>2</td></tr><tr><td>United Technologies</td><td>UTX</td><td>-0.04%</td><td>0.11%</td><td>0.50</td><td>0.06</td><td>6</td></tr><tr><td>Verizon Communications</td><td>VZ</td><td>0.09%</td><td>0.07%</td><td>0.71</td><td>0.06</td><td>34</td></tr><tr><td>Wal-Mart</td><td>WMT</td><td>0.10%</td><td>0.07%</td><td>0.04</td><td>0.04</td><td>38</td></tr><tr><td>Exxon Mobil</td><td>XOM</td><td>0.76%</td><td>0.09%</td><td>0.91</td><td>0.05</td><td>28</td></tr><tr><td>Market return (S&amp;P 500)</td><td>^GSPC</td><td>0.00%</td><td>0.09%</td><td></td><td></td><td></td></tr></table>

SD : standard deviation

Table 3: The list of regressors in the three models

<table><tr><td>Model</td><td>Dynamic Regressors (β)</td><td>Static Regressors (Z)</td></tr><tr><td>1</td><td>CS</td><td>MR</td></tr><tr><td>2</td><td></td><td>MR, SMB, HML, UMD</td></tr><tr><td>3</td><td>CS</td><td>MR, SMB, HML, UMD</td></tr></table>

3 provides the regressors in the three models. These three models allow us to isolate the effect of CS from the other factors on stock returns. For each of the two datasets, one MCMC chain per model was run for 12,000 iterations with a burn-in of 2,000 and a thinning of every 5 iterations. In canonical notation, with $SR_{j,t}$ denoting the $j$ th stock's returns at time $t$ , all three models can be written as following.

$$
\begin{array}{c} S R _ {j t} = \alpha_ {j} + C S _ {j t} \beta_ {j t} + Z _ {j t} \gamma_ {j} + u _ {j t}, \\ C S _ {j t} = C S _ {j t - 1} + v _ {j t}, \\ j = 1, \ldots , M, t = 1, \ldots , n, \\ u _ {j t} \sim i. i. d. N _ {M} (0, \Omega) v _ {j t} \sim i. i. d. N _ {M} (0, \Sigma), \end{array}\tag{19}
$$

where $\Sigma = A\Omega A$ ; the $Z_{jt}$ contain the static regressors. Recall from the methodology section, $A$ is a diagonal matrix such that $\{A\}_{jj} = ((1 - \delta_j) / \delta_j)^{\frac{1}{2}}$ , where $\delta_j$ specifies the signal to noise ratio for each stock. We tried different fixed values for $\delta_j$ and settled for 0.99 for all our models, since the results were similar even if we reduced them to, say 0.9. In other words, we allowed the signal in the observation equation to capture more of the uncertainty in the parameter estimates, as well as the predictions.

## 4.2 Estimation Phase

The estimation phase serves two purposes. First, to validate the claim that the slopes of the regression parameters for the CS coefficients are time-varying; this validation is accomplished using the DLM approach. Second, to demonstrate, via the posterior distributions of the variance-covariance matrix of the SUR model, the importance of considering cross-correlations between stocks in the datasets. In practical terms, a positive CS on a given stock not only affects the focal stock but also other stocks that are positively correlated with the focal stock. Hence modeling these correlations is important in both the estimation and prediction phases.

## 4.2.1 The estimated regression coefficients for the time-varying CS variable

To better focus the discussion, we pick six stocks to report. These stocks are American Express (AXP), Bank of America (BAC), Walt Disney (DIS), General Electrics (GE), JP Morgan Chase (JPM) and Microsoft (MSFT). In the interests of space, we do not report the results of all the other stocks. They are available upon request.

Validating the time-varying aspect of the CS regression slopes: the CS coefficients $(\beta_{t})$ from Model 1 for these six stocks are shown in Figures 1 and 2. The solid and dotted curves are the CS time-varying posterior means and their $90\%$ uncertainty bands, respectively, obtained by implementing the algorithm detailed in the Appendix. Note that the AXP CS coefficients in both data sets change considerably, as does JPM's. In contrast, the time-varying CS coefficients for MSFT and DIS are fairly stable over time in both data sets. For all four stocks, the estimated coefficients vary over time, taking on both positive and negative values at different time periods. Similar inferences were noted for the remaining stocks in the data sets. The results suggest that it would be inappropriate to assume that the CS regression coefficients are fixed in time for all these stocks when the analysis clearly points to meaningful time-varying evolution in some stocks. Put differently, assuming these slopes and intercepts to be fixed would mean there is just one unique line for each stock, implying (erroneously) a fixed rate of change in that stock's returns for a unit change in CS across all time periods.

To elaborate on the last point above, consider Table 4. For the six stocks, for each of the two data sets, 2009 and 2011, the first, second, and third rows correspond, respectively, to the posterior means, the fifth, and 95th percentiles. For the sake of illustration, these numeric values correspond to the last point shown in Figures 1 and 2. The last row in the table for each of the two datasets is the value of the slope coefficients for the six stocks obtained from running six static multiple linear regression models, one for each stock, with CS and MR. The estimated slope coefficients are markedly different from the DLM-SUM approach since the forecast, both in-sample and out-of-sample, use the same value for the coefficient. In reality, Figures 1 and 2 demonstrate how these six coefficients adapt to both the observation and system noise, evolving from one day to the next, starting with day one. Also, Table 4 provides rich summaries like the 5th and 95th percentiles of the posterior distributions of the CS coefficients, allowing researchers and practitioners to quantify the uncertainty. It is possible to construct confidence intervals for the static regression coefficients. However, like the mean estimates, these intervals will be the same for each day, whereas the Bayesian intervals will change each day, based on evolving observation and system noises.

The upshot of the above discussion is this: the impact of social media sentiments on future stock returns is time-varying. This was one of the primary hypotheses that this paper sought to examine.

Table 4: The comparison of CS coefficients from Model 1 and the static multiple linear regression model

<table><tr><td>2009</td><td>AXP</td><td>BAC</td><td>DIS</td><td>GE</td><td>JPM</td><td>MSFT</td></tr><tr><td>Bayesian Posterior Means</td><td>-0.044</td><td>-0.776</td><td>0.612</td><td>-0.035</td><td>0.155</td><td>0.071</td></tr><tr><td>5th Percentiles of Posterior Distributions</td><td>-0.971</td><td>-1.568</td><td>-0.064</td><td>-0.913</td><td>-1.370</td><td>-0.546</td></tr><tr><td>95th Percentiles of Posterior Distributions</td><td>0.789</td><td>0.066</td><td>1.400</td><td>0.734</td><td>1.375</td><td>0.675</td></tr><tr><td>CS Coefficients from Static Regression 2011</td><td>-0.248</td><td>-0.939</td><td>0.190</td><td>0.274</td><td>-0.127</td><td>0.103</td></tr><tr><td>Bayesian Posterior Means</td><td>0.392</td><td>-0.086</td><td>-0.031</td><td>0.141</td><td>0.642</td><td>0.031</td></tr><tr><td>5th Percentiles of Posterior Distributions</td><td>-0.531</td><td>-0.703</td><td>-0.816</td><td>-0.343</td><td>-0.265</td><td>-0.759</td></tr><tr><td>95th Percentiles of Posterior Distributions</td><td>1.354</td><td>0.559</td><td>0.691</td><td>0.612</td><td>1.567</td><td>0.812</td></tr><tr><td>CS Coefficients from Static Regression</td><td>-0.178</td><td>0.533</td><td>0.085</td><td>0.057</td><td>-0.134</td><td>0.401</td></tr></table>

## 4.2.2 The posterior distributions of the correlations of the system residual matrix $\Omega$ using the model with CS and MR

We now consider the cross-correlation between stock returns. Recall that $\Omega$ is the cross-sectional correlation matrix between the contemporaneous returns of different stocks. The elements in this matrix range from roughly -0.8 to 0.6 in both data sets. In 2009, the largest negative correlation is -0.74 (between PFE and JPM) and the largest positive correlation is 0.53 (between JPM and AXP). In 2011, the minimum correlation is -0.65 (between AA and JPM) and the maximum correlation is 0.56 (between AA and INTC). In both data sets, about 10% of the correlations are greater than 0.3 in absolute value. Explicitly modeling these correlations is clearly important. For instance, the large negative correlation between PFE and JPM suggests an inverse relationship in the way

2009 CS coefficient of AXP  
Figure 1: Selected time-series plots of the CS coefficients for the 2009 and 2011 data sets under Model 1  
![](/api/attachments/6SMBQ8JF/fulltext/images/34ea07ffc11b9bfd239acf9ac7d7437bb1d3a59ba8e0e6c8a990a831e6c4b17a.jpg)  
2009 CS coefficient of BAC

2011 CS coefficient of AXP  
![](/api/attachments/6SMBQ8JF/fulltext/images/49a7b45b0278f8562a4ab71c311310e991279ec05a0e98568fea760b69d0fe36.jpg)  
2011 CS coefficient of BAC

![](/api/attachments/6SMBQ8JF/fulltext/images/fc4bebe2fd21163250aa63ed1a1999a892f4eaec929f227ef864f6cc00e89d54.jpg)

![](/api/attachments/6SMBQ8JF/fulltext/images/1210e8dac5ad164caef93c325350a3a6b93aab35ce7f4bae719402363861f9ee.jpg)

![](/api/attachments/6SMBQ8JF/fulltext/images/66c62a63d6e08bbd0789140be3bd03a5bb8d160202b8bdfe5eaa0c90d67fe84b.jpg)

![](/api/attachments/6SMBQ8JF/fulltext/images/76fa02bb487b1918df8cccc08770e21c2349aa1921a7fc8a2c2d0151b46bbb6c.jpg)  
Solid curves are the posterior means and the dotted curves are the 90% uncertainty bands.

2009 CS coefficient of GE  
Figure 2: Selected time-series plots of the CS coefficients for the 2009 and 2011 data sets under Model 1  
![](/api/attachments/6SMBQ8JF/fulltext/images/f3b3078a66371c4f2271815ce53200d92b79c89e0fe7453f28e4a5def21d4fdd.jpg)  
2009 CS coefficient of JPM

2011 CS coefficient of GE  
![](/api/attachments/6SMBQ8JF/fulltext/images/60526533a7ed61d519f27554be16585af7f8d443fc5371f1d181910035047aa2.jpg)  
2011 CS coefficient of JPM

![](/api/attachments/6SMBQ8JF/fulltext/images/26a437534a094e5f28358edf49ab2c433dfd5ca1ecaaf891273386716f43a38e.jpg)

![](/api/attachments/6SMBQ8JF/fulltext/images/78ce5bae09b83475942b4365a6b8f2a4f8c59e7005cbca5dfa3b716f4f81bee6.jpg)

![](/api/attachments/6SMBQ8JF/fulltext/images/36aa738b23574f05d76b1f6e1fdb5fec12ff4738556a91e0c255ba08761d9e3c.jpg)

2011 CS coefficient of MSFT  
![](/api/attachments/6SMBQ8JF/fulltext/images/2be9c3d47fbac011d135c4521e9c63bc861d7d46c61410b212746016ebebe8a7.jpg)  
Solid curves are the posterior means and the dotted curves are the 90% uncertainty bands.

# ACCEPTED MANUSCRIPT

in which their respective returns evolve. These then influence the corresponding CS time-varying coefficients through the DLM's systems equations. The upshot of this dynamic relationship is that future forecasts of PFE and JPM stocks will be influenced by these correlations. Importantly, the correlations themselves are not static, since they are draws from the posterior distribution of $\Omega$ .

## 4.3 Prediction Phase

The Bayesian approach allows us to test for out-of-sample validation since it produces the predictive distributions, not just a point prediction, at each time period for each of the stocks in the data sets. To this end, we use the first 126 observations in 2009 and 251 observations in 2011 in the estimation phase, and predict one-day ahead for the six stocks described in the estimation phase above. We can then compare our predictions with the actual observed data for that day. Note our modeling approach can easily provide predictions k steps ahead for any k; here, for illustration, we set k = 1.

## 4.3.1 Inferences from predictive densities

Table 5: Summary of the predictive densities, OLS estimates and realized returns for six selected stocks: 2009 data using Model 1— only dynamic CS factors and Market Returns

<table><tr><td>Stock</td><td>Realized Return</td><td>OLS Estimate</td><td>DLM-SUR Mean</td><td>SD</td><td>Kurtosis</td></tr><tr><td>AXP</td><td>-0.69</td><td>0.877</td><td>0.67</td><td>3.89</td><td>3.66</td></tr><tr><td>BAC</td><td>-0.07</td><td>-0.222</td><td>-0.43</td><td>2.19</td><td>4.48</td></tr><tr><td>DIS</td><td>-0.10</td><td>0.018</td><td>-0.15</td><td>2.28</td><td>4.58</td></tr><tr><td>GE</td><td>-1.43</td><td>0.069</td><td>-0.16</td><td>1.74</td><td>3.86</td></tr><tr><td>JPM</td><td>0.34</td><td>0.162</td><td>-0.02</td><td>6.21</td><td>4.04</td></tr><tr><td>MSFT</td><td>-1.55</td><td>0.202</td><td>0.06</td><td>1.62</td><td>5.14</td></tr></table>

Table 6: Summary of the predictive densities, OLS estimates and realized returns for six selected stocks: 2011 data using Model 1— only dynamic CS factors and Market Returns

<table><tr><td>Stock</td><td>Realized Return</td><td>OLS Estimate</td><td>DLM-SUR Mean</td><td>St. Dev.</td><td>Kurtosis</td></tr><tr><td>AXP</td><td>0.88</td><td>0.062</td><td>0.05</td><td>2.03</td><td>3.87</td></tr><tr><td>BAC</td><td>2.90</td><td>-0.49</td><td>-0.31</td><td>0.84</td><td>4.04</td></tr><tr><td>DIS</td><td>0.97</td><td>0.202</td><td>-0.04</td><td>1.54</td><td>4.36</td></tr><tr><td>GE</td><td>0.50</td><td>0.043</td><td>0.87</td><td>0.77</td><td>3.43</td></tr><tr><td>JPM</td><td>3.22</td><td>0.052</td><td>-0.89</td><td>2.29</td><td>3.65</td></tr><tr><td>MSFT</td><td>-0.14</td><td>-0.144</td><td>0.00</td><td>0.99</td><td>3.71</td></tr></table>

For the 2009 and 2011 data sets, the actual realized returns for all the stocks are within two standard errors from the means of the respective predictive densities. Our SUR-DLM approach not only models the covariance between stocks (as discussed in section 4.2.2) but note that the predictive densities feature higher levels of kurtosis than the normal distribution for some of the predictive distributions of stock returns. In other words, the predictive distributions for many of these returns could be heavy-tailed. The Bayesian SUR-DLM captures such features appropriately. The primary benefit of higher order moments is they influence the estimates of the lower order ones. For example, if the true underlying density is, say unimodal and leptokurtic, the probability mass at the peak will be significantly influenced by the model used to describe the data. Here, we have shown that the parameters are time-varying which suggests that all the moments of the evolving probability densities will change and influence the future moments. The kurtosis for many of the predictive distributions clearly show that the data are leptokurtic. Treating this explicitly (like we do) leads to better predictions.

A striking feature from Tables 5 and 6 is that the standard deviations of the predictive densities for all the stocks are substantially smaller in 2011 when compared to 2009. But this is not surprising. Earlier from figures 1 and 2 we saw that the plots of the time-varying CS coefficients are far more stable in 2011 when compared to 2009, which was a crisis phase in the economy. Since the predictive distributions are a function of these coefficients, their standard deviations are appropriately influenced by the estimates of these coefficients.

Another interesting feature is that the realized returns for the six stocks fluctuate considerably in the two data sets, implying that the Bayesian predictive time-varying approach is better suited to model the stock returns, rather than a fixed, static approach.

For comparison, we also include the predicted values from a standard OLS procedure for the six stocks. It is important to emphasize how misguided decisions could be if one merely focused on the Mean values, be it OLS or from our model. For one, the kurtosis of the predictive densities are much larger than that of a normal distribution. In other words, it would be important to account for the volatility and higher order moments of the data distribution. Point estimates, like the mean, are largely data centric. Even here, this is evident when one compares the 2009 versus 2011 estimates for the exact same six stocks. What our research shows is that it is better to have a methodology that will consistently capture all the key moments of the predictive density, regardless of the particular data set with which one may be confronted. Since no model is “perfect”, the best one could hope for is to try and account for as many sources of variability as possible. Our SUR-DLM model for social media sentiments is a step in that direction.

<table><tr><td colspan="4">Table 7: MAE and MSE Means and Standard Errors for 15 observations</td></tr><tr><td>MAE</td><td>Model 1</td><td>Model 2</td><td>Model 3</td></tr><tr><td>2009 data set</td><td>26.00(10.40)</td><td>46.06(16.32)</td><td>26.49(8.51)</td></tr><tr><td>2011 data set</td><td>31.85(13.54)</td><td>44.93(28.18)</td><td>35.05(16.10)</td></tr><tr><td>pooled data set</td><td>28.93(12.23)</td><td>45.50(22.63)</td><td>30.77(13.38)</td></tr><tr><td>MSE</td><td>Model 1</td><td>Model 2</td><td>Model 3</td></tr><tr><td>2009 data set</td><td>52.03(39.17)</td><td>127.41(84.59)</td><td>51.51(34.91)</td></tr><tr><td>2011 data set</td><td>63.83(48.27)</td><td>134.64(158.70)</td><td>78.56(65.66)</td></tr><tr><td>pooled data set</td><td>57.93(43.61)</td><td>131.03(125.01)</td><td>65.04(53.47)</td></tr></table>

Note: Standard errors are in parenthesis

## 4.3.2 Forecast errors

Recall from earlier (Table 3) that there are three models we are evaluating. Model 1: This includes the dynamic CS regressor and static Market Return factor. Model 2: This is the SUR model with static Fama-French and momentum factors. Model 3: This is the DLM-SUR model with CS, Fama-French and momentum factors.

To further analyze the differences between the above models, we calculate both the Mean Absolute Errors (MAE) and the Mean Square Errors (MSE) between the actual realized returns and the mean of predictive returns for 15 consecutive days for the three models using both datasets. Furthermore, we pool the 2009 and 2011 results to see if the inferences hold using a larger dataset. A paired two-sample t-test was performed leading to the following conclusions. Consider Table 7 and Table 8.

First, for the 2009 data, Model 1 and Model 3 outperforms Model 2 significantly with two-tailed p-value less than 1% for both MAE and MSE metrics. That is, there is strong evidence that adding CS improves predictions of stock returns.

Second, there is no significant difference between Model 2 and Model 3 which implies that adding lag Fama-French/ Momentum factors do not offer any significant benefit for predicting stock returns.

Table 8: MAE and MSE predictive comparisons

<table><tr><td></td><td colspan="2">Model 1 - Model 2</td><td colspan="2">Model 1 - Model 3</td><td colspan="2">Model 2 - Model 3</td></tr><tr><td>MAE</td><td>t stats.</td><td>p-value</td><td>t stats.</td><td>p-value</td><td>t stats.</td><td>p-value</td></tr><tr><td>2009 data set</td><td>-4.50</td><td>0.0004</td><td>-0.66</td><td>0.5199</td><td>4.40</td><td>0.0006</td></tr><tr><td>2011 data set</td><td>-1.55</td><td>0.1441</td><td>-2.17</td><td>0.0473</td><td>1.06</td><td>0.3046</td></tr><tr><td>pooled data set</td><td>-3.50</td><td>0.0015</td><td>-2.18</td><td>0.0379</td><td>2.87</td><td>0.0076</td></tr><tr><td colspan="3"></td><td colspan="2"></td><td colspan="2"></td></tr><tr><td>MSE</td><td>t stats.</td><td>p-value</td><td>t stats.</td><td>p-value</td><td>t stats.</td><td>p-value</td></tr><tr><td>2009 data set</td><td>-3.20</td><td>0.0060</td><td>0.23</td><td>0.8195</td><td>3.20</td><td>0.0060</td></tr><tr><td>2011 data set</td><td>-1.62</td><td>0.1280</td><td>-2.30</td><td>0.0370</td><td>1.18</td><td>0.2581</td></tr><tr><td>pooled data set</td><td>-2.99</td><td>0.0056</td><td>-0.96</td><td>0.0592</td><td>2.52</td><td>0.0175</td></tr></table>

Third, for the 2011 data, there is a statistically significant difference between Model 1 and Model 3 with two-tailed p-value less than $5\%$ under both MAE and MSE metrics. This indicates that adding the extra lagged Fama-French/ Momentum factors worsen the predictions.

Fourth, there is weaker evidence that suggests Model 1 outperforms Model 2 with two-tailed p-value less than $15\%$ for both MAE and MSE metrics.

Fifth, there is no statistically significant difference for the prediction errors between Model 2 and Model 3 but note that Model 3 has meaningfully lower prediction errors than Model 2. This is consistent with the 2009 data wherein Model 2 had the worst performance.

Sixth, Table 8 shows that when the 2009 and 2011 data are pooled, Model 1 outperforms Model 2 and Model 3 significantly with two-tailed p-value lass than $5\%$ under the MAE metric. With the MSE metric, Model 1 outperforms Model 2 and 3 at the $1\%$ significance level. Thus, when data sets with different levels of volatility are combined, Model 1 (the one with dynamic CS and static Market Return) better predicts returns compared to models with additional static factors in them. In conclusion, it is crucial to emphasize the upshot of Tables 7 and 8: modeling parameter uncertainty via SUR/DLMs goes a long way in better understanding the importance of social media sentiments and their role in predicting stock returns, rather than adding Fama-French and momentum factors. This is because the rich structure of the SUR-DLM approach, along with CS and MR, are enough to describe the underlying dynamics of stock returns. Adding more factors, even if they are statistically different from zero, do not improve prediction; this is the principle of parsimony at work. That is, it emphasizes a key statistical point: models that fit the data well do not necessarily predict well. The methodological intent of our research is not to look for a “best-fit” model, rather it is to study the impact of time-varying nature of the sentiment parameters.

## 5 Conclusion

A novel Bayesian method to assess the relationship between social media sentiments and future stock returns was considered. Methodologically, the model integrated two mathematical notions: Dynamic Linear Models (DLMs) allow us to explicitly model the time-varying relationship between social media sentiments and future stock returns; and Seemingly Unrelated Regressions (SURs) allow us to model the stock returns as a system of inter-related equations that explicitly factor cross-correlations between the returns.

The empirical analysis of the stocks in the DJIA in 2009 and 2011 provides compelling evidence to support both the time-varying and cross-correlation hypotheses. Further, the one-day ahead predictive distributions for many of the stocks in the DJIA have tails that are heavier than the normal distribution. This means extreme values in the observed data play a crucial role in forecasting stock returns. Here, we exemplified the methodology by predicting one-day ahead. In principle, the model could be adapted for multi-steps ahead forecasting.

Another critical finding is that models with just social media sentiments and market returns perform at least as well as models that also include Fama-French and Momentum Factors. We argue that this is because of the DLM-SUR modeling approach taken in this paper. Capturing system dynamics via the DLM component and the inter-related nature of stock returns in the DJIA via the SUR component provides new insight into the role of social media sentiments on stock performance in financial markets.

It is worthy to note that traditional serial correlation (or autocorrelation) time-series regressions are special cases of DLMs. This is readily seen if one simply removes the state equation and proceeds to model the observation equation as an autoregressive model. A main difference between the two types of models is that in a DLM, the relationship between the independent and dependent variable varies over time and could be negative/positive over different time periods. Interestingly, He et al. [15] found that negative sentiments on Tweets could predict a firm's future stock prices. It is possible that even positive Twitter sentiments might influence predictability if the corresponding

# ACCEPTED MANUSCRIPT

regressors were allowed to be time-varying. This may be worthy of future research. Approaches like Fama-Macbeth only address issues related to autocorrelated dependent variables but do not handle dynamic relationships between independent and dependent variables.

It may be tempting to step away from a daily DLM model for each company like we did in this paper. This is not viable for three reasons. One, aggregating data could likely hide underlying variation in the data. Two, aggregation will hide sudden spikes in the data which clearly exists in the stock returns data. Three, the Bayesian estimates will be much improved, since “learning” and “updating” day-to-day will better capture the local fluctuations, such as spikes, in the data. Working with daily data increases computation time, but this is hardly a daunting issue in this age of high-speed computing. Indeed, it is for this reason models like DLMs could prove useful in the burgeoning field of “big data” analytics.

One of the difficulties in dealing with social media sentiments is the changing nature of the online databases and missing data. Handling missing covariate data requires data augmentation steps in the Markov chain Monte Carlo algorithms. In the present context, we are unsure how one would augment missing self-declared sentiments on a given day since they are not missing data in the usual statistical sense. In other words, we are led to the tough question: what probability model should one assume for such sentiments so one could augment missing values from it within an MCMC routine? This is a difficult question to tackle satisfactorily. It has some similarities to modeling management skill in mutual fund performance. To our knowledge, no one has provided a satisfactory way to tackle that problem in the financial economics literature.

While we have used a Gibbs sampler to do the MCMC analysis, there are other simulation methods one could try, like Sequential Monte Carlo. We note that there is no single universal MCMC method that works in every setting since every method has it pros and cons. For our purposes, the Gibbs sampler works well, since the conditional distributions are of known type; hence sampling them is somewhat straightforward.

## Acknowledgements

We thank the editor and reviewers for their patience and encouragement while revising this paper. Many thanks to Professor Alvin Leung for his help in acquiring some of the data used in this paper.

## References

[1] T. Ando, A. Zellner, Hierarchical Bayesian analysis of the seemingly unrelated regression and simultaneous equations models using a combination of direct Monte Carlo and importance sampling techniques, Bayesian Analysis 5 (1) (2010) 65–96.

[2] W. Antweiler, M. Z. Frank, Is all that talk just noise? The information content of internet stock message boards, Journal of Finance 59 (3) (2004) 1259–1294.

[3] M. Bagnoli, M. D. Beneish, S. G. Watts, Whisper forecasts of quarterly earnings per share, Journal of Accounting and Economics 28 (1) (1999) 27–50.

[4] N. Barberis, A. Shleifer, R. Vishny, A model of investor sentiment, Journal of Financial Economics 49 (3) (1998) 307–343.

[5] J. Bollen, H. Mao, X. Zeng, Twitter mood predicts the stock market, Journal of Computational Science 2 (1) (2011) 1–8.

[6] M. M. Carhart, On persistence in mutual fund performance, The Journal of Finance 52 (1) (1997) 57–82.

[7] J. A. Chevalier, D. Mayzlin, The effect of word of mouth on sales: Online book reviews, Journal of Marketing Research 43 (3) (2006) 345–354.

[8] S. Chib, Markov Chain Monte Carlo methods., in: P. Damien, P. Dellaportas, N. Polson, D. Stephens (eds.), Bayesian Theory and Applications, Oxford University Press, Clarendon, England, 2013, pp. 87–103.

[9] S. Das, M. Chen, Yahoo! for Amazon: Sentiment extraction from small talk on the Web, Management Science 53 (9) (2007) 1375–1388.

[10] J. DeLong, A. Shleifer, L. Summers, R. Waldmann, Noise trader risk in financial markets, Journal of Political Economy 98 (4) (1990) 703–738.

[11] P. M. DeMarzo, D. Vayanos, J. Zwiebel, Persuasion bias, social influence, and unidimensional opinions, The Quarterly Journal of Economics 118 (3) (2003) 909–968.

[12] M. Dewally, Internet investment advice: Investing with a rock of salt, Financial Analysts Journal 59 (4) (2003) 65–77.

[13] J. Felton, J. Kim, Warnings from the Enron message board, Journal of Investing 11 (3) (2002) 29–52.

[14] B. Gu, P. Konana, M. Chen, Competition among virtual communities and user valuation: the case of investor communities, Information Systems Research 18 (1) (2007) 68–85.

[15] W. He, L. Guo, J. Shen, V. Akula, Social media-based forecasting: A case study of tweets and stock prices in the financial services industry, Journal of Organizational and End User Computing 28 (2) (2016) 74–91.

[16] D. Hirshleifer, Investor psychology and asset pricing, The Journal of Finance 56 (4) (2001) 1533–1597.

[17] G. Jostova, A. Philipov, Bayesian analysis of stochastic betas, Journal of Financial and Quantitative Analysis 40 (04) (2005) 747–778.

[18] D. Kahneman, A. Tversky, On the reality of cognitive illusions, Psychological review 103 (3) (1996) 582–91.

[19] Q. Li, T. Wang, Q. Gong, Y. Chen, Z. Lin, S.-k. Song, Media-aware quantitative trading based on public web information, Decision Support Systems 61 (2014) 93–105.

[20] A. Lugmayr, G. Gossen, Evaluation of methods and techniques for language based sentiment analysis for DAX 30 stock exchange a first concept of a "LUGO" sentiment indicator, International SERIES on Information Systems and Management in Creative eMedia (1) (2013) 69–76.

[21] X. Luo, J. Zhang, W. Duan, Social media and firm equity value, Information Systems Research 24 (1) (2013) 146–163.

[22] B. G. Malkiel, The efficient market hypothesis and its critics, Journal of Economic Perspectives (2003) 59–82.

[23] C. Oh, O. Sheng, Investigating predictive power of stock micro blog sentiment in forecasting future stock price directional movement, Proceedings of the International Conference on Information Systems (ICIS), December 6, 2011 (Page 17).

[24] D. F. Percy, Prediction for seemingly unrelated regressions, 1992. Journal of the Royal Statistical Society. Series B (Methodological) 54 (1) (1992) 243–252.

[25] H. K. Sul, A. R. Dennis, L. I. Yuan, Trading on Twitter: Using social media sentiment to predict stock returns, Decision Sciences (2016) 1–31.
URL http://dx.doi.org/10.1111/deci.12229

[26] R. Thaler, Mental accounting and consumer choice, Marketing Science 4 (3) (1985) 199–214.

[27] S. Tirunillai, G. J. Tellis, Does chatter really matter? Dynamics of user-generated content and stock performance, Marketing Science 31 (2) (2012) 198–215.

[28] R. Tumarkin, R. F. Whitelaw, News or noise? Internet postings and stock prices, Financial Analysts Journal 57 (3) (2001) 41–51.

[29] M. West, J. Harrison, Bayesian Forecasting and Dynamic Models, Springer-Verlag, New York, 1997.

[30] A. Zellner, An Introduction to Bayesian Inference in Econometrics, Willey, New York, 1971.

## Appendix

Gibbs sampler for SUR-DLM model

The model

$$
y _ {j t} = \alpha_ {j} + X _ {j t} \beta_ {j t} + Z _ {j t} \gamma_ {j} + u _ {j t},
$$

$$
\beta_ {j t} = \beta_ {j t - 1} + v _ {j t},\tag{20}
$$

$$
j = 1, \dots , M, t = 1, \dots , n,
$$

$y_{jt}, \alpha_j, X_{jt}, \beta_{jt}, u_{jt}, v_{jt}$ are scalers, $Z_{jt}$ are $1 \times p_j$ vectors, $\gamma_j$ are $p_j \times 1$ vectors, and $P = \sum p_j$ . Let $u_t = (u_{1t}, ..., u_{Mt})'$ and $v_t = (v_{1t}, ..., v_{Mt})'$ , then

$$
u _ {t} \sim i. i. d. N _ {M} (0, \Omega) v _ {t} \sim i. i. d. N _ {M} (0, \Sigma)
$$

where $\Sigma = A\Omega A$ and $A$ is a diagonal matrix, $\{A\}_{jj} = ((1 - \delta_j) / \delta_j)^{\frac{1}{2}}$ .

## Sampling $\alpha$

To sample $\alpha |y,X\beta ,Z\gamma ,\Omega$ , let $\epsilon_{jt} = y_{jt} - X_{jt}\beta_{jt} - Z_{jt}\gamma_j$ . Let $\epsilon$ be a $M\times n$ matrix, $\{\epsilon \}_{jt} = \epsilon_{jt}$ $C_M$ be a $n\times M$ matrix and $C_1$ be a $1\times M$ matrix where all entries in $C_M$ and $C_1$ are 1.

$$
f (\alpha_ {1: M} | D, \Theta / \{\alpha_ {1: M} \}) \sim N _ {M} (\mu_ {\alpha}, \Sigma_ {\alpha})
$$

where

$$
\mu_ {\alpha} = \Sigma_ {\alpha} \left(\Omega^ {- 1} \odot C _ {M} ^ {T} \epsilon^ {T}\right) C _ {1}
$$

$$
\Sigma_ {\alpha} = \left(\Omega^ {- 1} \odot C _ {M} ^ {T} C _ {M}\right) ^ {- 1}
$$

## Sampling $\gamma$

To sample $\gamma |y,\alpha X\beta ,Z,\Omega$ , let $\epsilon_{jt} = y_{jt} - \alpha_j - X_{jt}\beta_{jt}$ . Then we can stack $\epsilon_{jt}$ to be $nM\times 1$ matrix $\epsilon$ and stack $Z_{jt}$ to be a $nM\times P$ matrix $Z$ and $\gamma_{j}$ to be a $P\times 1$ matrix $\gamma$

$$
f (\gamma | D, \Theta / \{\gamma_ {1: M} \}) \sim N _ {P} (\mu_ {\gamma}, \Sigma_ {\gamma})
$$

where

$$
\mu_ {\gamma} = \left\{Z ^ {\prime} (\Omega^ {- 1} \otimes I) Z \right\} ^ {- 1} Z ^ {\prime} (\Omega^ {- 1} \otimes I) \cdot \epsilon
$$

$$
\Sigma_ {\alpha} = (Z ^ {\prime} (\Omega^ {- 1} \otimes I) Z) ^ {- 1}
$$

## Sampling $\beta$

To sample $\beta|\Sigma$ . Let $\xi_t = y_t - \alpha - Z_t\gamma$ , $F_t$ is a diagonal matrix and $\{F_t\}_{jj} = X_{tj}$ .

The forward filtration starts with the posterior at time 0, $\beta_0 \sim N(m_0, C_0)$ . Given the posterior distribution at $t - 1$

$$
(\beta_ {t - 1} | D _ {t - 1}) \sim N _ {M} (m _ {t - 1}, C _ {t - 1})
$$

and the priors at t,

$$
(\beta_ {t} | D _ {t - 1}) \sim N _ {M} (a _ {t}, R _ {t}) (y _ {t} | D _ {t - 1}) \sim N _ {M} (f _ {t}, Q _ {t}),
$$

where

$$
a _ {t} = m _ {t - 1} R _ {t} = C _ {t} + \Sigma , f _ {t} = a _ {t}, Q _ {t} = F _ {t} R _ {t} F _ {t} ^ {\prime} + \Omega ,
$$

the posterior distribution at $t$ is

$$
(\beta_ {t} | D _ {t}) \sim N _ {M} (m _ {t}, C _ {t}),
$$

where

$$
m _ {t} = a _ {t} + R _ {t} F _ {t} ^ {\prime} Q _ {t} ^ {- 1} e _ {t}, C _ {t} = R _ {t} - R _ {t} F _ {t} ^ {\prime} Q _ {t} ^ {- 1} F _ {t} R _ {t}, e _ {t} = \xi_ {t} - f _ {t}.
$$

The backward sampling starts with the posterior distribution at time T; first, sample $\beta_{n}$ from

$N_{M}(m_{n},C_{n})$ . Let $h_n = m_n$ ， $B_{n} = C_{n}$ and

$$
(\beta_ {t + 1} | D _ {n}) \sim N _ {M} (h _ {t + 1}, B _ {t + 1});
$$

then

$$
\left(\beta_ {t} \mid \beta_ {t + 1}, D _ {n}\right) \sim N _ {M} \left(h _ {t}, B _ {t}\right),
$$

where

$$
h _ {t} = m _ {t} + C _ {t} R _ {t + 1} ^ {- 1} (\beta_ {t + 1} - a _ {t + 1}) B _ {t} = C _ {t} - C _ {t} R _ {t + 1} ^ {- 1} C _ {t}.
$$

## Sampling Ω

Given all the other information from the DLM components above, the SUR system is given by:

$$
\begin{array}{c} u _ {t} = y _ {t} - \alpha + X _ {t} \beta_ {t} + Z _ {t} \gamma , t = 1, \dots , n \\ v _ {t} = \beta_ {t} - \beta_ {t - 1}, t = 2, \dots (n - 1) \\ u _ {t} \sim N (0, \Omega) v _ {t} \sim N (0, \Sigma) \end{array}
$$

where $\{\Omega\}_{ij} = \omega_{ij}$ .

The likelihood of $\Omega$ can be expressed as

$$
L (\Omega) = \propto | \Omega | ^ {- \frac {(n - 1)}{2}} | \Sigma | ^ {- \frac {(n - 1)}{2}} \exp \left\{- \frac {1}{2} \sum_ {t = 1} ^ {n} \left((u _ {t}) ^ {\prime} \Omega^ {- 1} (u _ {t})\right) - \frac {1}{2} \sum_ {t = 1} ^ {n - 1} \left((v _ {t}) ^ {\prime} \Sigma^ {- 1} (v _ {t})\right) \right\}
$$

and the posterior density can be expressed as

$$
f (\Omega | D, \Theta / \{\Omega \}) \propto | \Omega | ^ {- \frac {(n + 1)}{2}} | \Sigma | ^ {- \frac {(n - 1)}{2}} \exp \left\{- \frac {1}{2} \sum_ {t = 1} ^ {n} \left((u _ {t}) ^ {\prime} \Omega^ {- 1} (u _ {t})\right) - \frac {1}{2} \sum_ {t = 1} ^ {n - 1} \left((v _ {t}) ^ {\prime} \Sigma^ {- 1} (v _ {t})\right) \right\}
$$

Let $\delta^{*} = \frac{1 - \delta}{\delta}$ and $A$ be a diagonal matrix were $\{A\}_{jj} = (\delta_j^*)^{\frac{1}{2}}$ . Define $\Sigma = A\Omega A$ , then

$$
\{\Sigma \} _ {j k} = \left\{ \begin{array}{l l} \sqrt {\delta_ {j} ^ {*} \delta_ {k} ^ {*}} \omega_ {j k} & (j \neq k) \\ \delta_ {j} ^ {*} \omega_ {j} ^ {2}, & (j = k) \end{array} \right.
$$

$$
f (\Omega | D, \Theta / \{\Omega \}) \propto | \Omega | ^ {- \frac {1}{2}} | \Omega | ^ {- \frac {(n)}{2}} | A \Omega A | ^ {- \frac {(n - 1)}{2}} \exp \left\{- \frac {1}{2} \sum_ {t = 1} ^ {n} \left((u _ {t}) ^ {\prime} \Omega^ {- 1} (u _ {t})\right) - \frac {1}{2} \sum_ {t = 1} ^ {n - 1} \left((v _ {t}) ^ {\prime} (A \Omega A) ^ {- 1} (v _ {t})\right) \right\}
$$

$$
\propto | \Omega | ^ {- n} \exp \left\{- \frac {1}{2} \sum_ {t = 1} ^ {n} \left((u _ {t}) ^ {\prime} \Omega^ {- 1} (u _ {t})\right) - \frac {1}{2} \sum_ {t = 1} ^ {n - 1} \left((v _ {t}) ^ {\prime} (A) ^ {- 1} \Omega^ {- 1} (A) ^ {- 1} (v _ {t})\right) \right\}
$$

Thus, the posterior distribution of $\Omega \sim$ Inverse Wishart $(\nu ,\Psi)$ where,

$$
\nu = n + (n - 1) + 1 = 2 n
$$

$$
\Psi = \sum_ {t = 1} ^ {n} (u _ {t}) (u _ {t}) ^ {\prime} + \sum_ {t = 1} ^ {n - 1} \left((A) ^ {- 1} (v _ {t}) (v _ {t}) ^ {\prime} (A) ^ {- 1}\right).
$$

## Sampling $\delta$

For each $j$ , we can either fix the signal to noise ratio $\delta$ or make it random variable. If we want to learn about $\delta$ through the data, we can use Beta priors on the $\delta$ 's and use Metropolis-Hastings within Gibbs to generate from its conditional distribution. Here we provide details on independent Metropolis-Hastings where the candidate draws for $\delta$ come from independent Beta distributions. The likelihood function for $\delta$ is

$$
L (\delta) = \propto | A \Omega A | ^ {- \frac {(n - 1)}{2}} \exp \left\{- \frac {1}{2} \sum_ {t = 1} ^ {n - 1} \left((v _ {t}) ^ {\prime} (A \Omega A) ^ {- 1} (v _ {t})\right) \right\}
$$

The posterior density of $\delta$ is

$$
f (\delta | D, \Theta / \{\delta \}) \propto \pi (\delta) \cdot | A \Omega A | ^ {- \frac {(n - 1)}{2}} \exp \left\{- \frac {1}{2} \sum_ {t = 1} ^ {n - 1} \left((v _ {t}) ^ {\prime} (A \Omega A) ^ {- 1} (v _ {t})\right) \right\}
$$

Given $\delta_{0}$ and candidate density $g(\delta)$ , the candidate $\delta^{*}$ of the independent Metropolis-Hastings algorithm has acceptance rate

$$
\alpha = \min (1, \frac {f (\delta^ {*}) \cdot g (\delta_ {0})}{f (\delta_ {0}) \cdot g (\delta^ {*})})
$$

If we let $g(x)$ be the prior of $\delta$ , then the acceptance rate can be calculated with the likelihood of $\delta$ alone.

## Sampling Predictive distribution of Y

In each Gibbs iteration after the sampling of $\beta$ , we can sample the predictive distribution $Y_{n + 1}|D_n,X_{n + 1},Z_{n + 1},\Theta$ within the FFBS loop.

$$
f (Y _ {n + 1} | D _ {n + 1}, X _ {n + 1}, Z _ {n + 1}, \Theta) \sim N _ {M} (\mu_ {p}, \Sigma_ {p})
$$

$$
\mu_ {p} = \alpha + X _ {n + 1} m _ {t} + Z _ {n + 1} \gamma
$$

$$
\Sigma_ {p} = D _ {X} \cdot (C _ {n} + \Sigma) \cdot D _ {X} + \Omega ,
$$

where $D_{X}$ is the diagonal matrix of $X_{n+1}$ .

## Biographical Note

• Chi-San Ho, Senior Data Scientist, Capital One Bank, Dallas, Texas

\- Paul Damien, Professor of Information, Risk and Operations Management, Elected fellow of the Royal Statistical Society of England, Chair of the Graduate Studies Committee (2004-2009, IROM Department) McCombs School of Business, University of Texas in Austin

\- Bin Gu, Professor of Business, W. P. Carey School of Business, Arizona State University, Main Campus: Senior Editor, MIS Quarterly 2015-2017 Associate Editor, Information Systems Research 2012-2016 Associate Editor, MIS Quarterly 2012-2014 Associate Editor, Information Systems Research – Special Issue on Social Media and Business Transformation Associate Editor, Decision Support Systems, 2014-2016

\- Prabhudev Konana, Professor of Information, Risk and Operations Management, McCombs School of Business, University of Texas in Austin: Associate Editor, Decision Science, 2010 – current; Associate Editor, Information Systems Research, 2005 – 2008; Associate Editor, Management Information Systems Quarterly, 2003 – 2007; Senior Editor (Guest), Management Information Systems Quarterly, 2005/2006/2011; Editorial Review Board – Journal of AIS, 2002 – present; Editorial Review Board – Information Technology and Management, 2002 – present; Editorial Review Board – Journal of Database Management (2000-2001)

# ACCEPTED MANUSCRIPT

## Highlights

\- Is the relationship between social media sentiments and stock returns time-varying? How does one capture the inherent cross-correlation between stocks to better model the time-varying relationship?

\- Answers to the above queries are tackled via a novel methodology: Bayesian Dynamic Linear Models and Seemingly Unrelated Regressions.

\- The impact of social media sentiments on future stock returns vary over time. Thus, both positive and negative sentiments could meaningfully impact the prediction of stock returns.

\- Modeling cross-correlations among stock returns meaningfully impacts their estimation and prediction. The posterior distributions of correlations range from -0.8 to +0.6.

\- The time-varying social media sentiments coefficients are more stable in 2011 when compared to 2009; the latter was a period of high turbulence due to recession.
