---
otero_id: 15636
otero_key: "9WR7QEAA"
title: "Levy process-driven mean-reverting electricity price model: the marginal distribution analysis"
authors: "Shi-Jie Deng; Wenjiang Jiang"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.05.010"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Levy process-driven mean-reverting electricity price model: the marginal distribution analysis

Shi-Jie Deng<sup>a,\*</sup>, Wenjiang Jiang<sup>b</sup>

<sup>a</sup>School of ISyE, Georgia Institute of Technology, Atlanta, GA 30332-0205, USA <sup>b</sup>School of Mathematical Science, Yunnan Normal University, Yunnan, China

Available online 10 July 2004

## Abstract

We propose a class of stochastic mean-reverting models for electricity prices with Levy process-driven Ornstein–Uhlenbeck (OU) processes being the building blocks. We first fit marginal distributions of power price series to two special classes of distributions defined by quantile functions (termed Class I and Class II distributions). A theoretical correlation structure is then used to fit the empirical autocorrelation structure. Lastly, based on results from the first two steps, we construct a stochastic process by superposing two OU processes. The focus of this paper is on fitting the marginal distribution. A Class I distribution has closed-form formulas for probability density, cumulative distribution function, and quantile function, while a Class II distribution may have extremely unbalanced tails. Both classes of distributions admit realistic modelling of the marginal distribution of electricity prices. This approach effectively captures not only the anomalous tail behaviors but also the correlation structure present in the electricity price series. © 2004 Elsevier B V All rights reserved

Keywords: Electricity market signals; Electricity option pricing; Levy process; Ornstein–Uhlenbeck type process; Heavy-tail; Unbalanced-tail; Correlation structure; Risk management

## 1. Introduction

In seeking mid-term and long-term economic efficiency, many countries including the United Kingdom, Australia, Chile, Argentina, New Zealand, Norway and the United States have been, or are currently undertaking efforts to restructure their electricity supply industries (see Refs. [10,15]). This global trend of restructuring leads to the emergence and the rapid growth of electric power markets starting in the early 1990s. In the United States, an electricity wholesale market known as the Power Exchange, where day-ahead and hour-ahead electricity is traded, started its operation in California On March 31, 1998. Electricity is also traded in the realtime market managed by the California Independent System Operator (ISO). In the Pennsylvania–New Jersey–Maryland (PJM) interconnection, there is one single market for electricity, managed by the PJM

ISO, which began to operate in April 1998. Following the moves by California and PJM, the New England Power Pool started on May 1, 1999 while the electricity market in New York, called the New York Power Pool, came on-line on November 18, 1999.

Ever since the moment that electricity became a traded commodity, its price has been displaying the highest level of volatility and the most complex features among all commodity prices.

Fig. 1 plots the historical price paths of electricity in two regions of the U.S., Northern California and PJM, during the time period from April 1, 1998 to August 31, 2000. The historical price data shows that power prices exhibit salient features such as meanreverting, jumps, and spikes, which reflect the commodity nature of electricity and the unique characteristics of electricity such as non-storability, heavy reliance on the transmission networks, and characteristic steepness of the electricity supply function at high production levels in almost all regions of the U.S. Such erratic price behaviors could create dramatic market risks and operational risks. In risk management jargon, market risk refers to the financial impact of an adverse move in financial or commodity markets; and operational risk refers to the impact of a firm’s lack of preparation for market volatility. The market and operational risks associated with remarkably volatile electricity prices make it an indispensable task to accurately model the power price dynamics for the purpose of risk management.

Our main objective is to identify a power price model that is both realistic for option pricing and risk management purposes and feasible for parameter estimation given limited available market data. Enlightened by the facts that an Ornstein–Uhlenbeck (OU) type process (to be described in the next section) can be conveniently characterized by its marginal distribution and correlation structure, and the superposition of OU type processes can model not only short-range dependence but also quasi-long-range dependence (QLRD), we propose to model electricity prices using the superposition of OU type processes. Specifically, we first fit the marginal distributions of power price return series to two special classes of distributions (termed Class I and Class II distributions) by matching the quantiles of an empirical distribution with that of a theoretical distribution. While both distribution classes have rich tail behaviors, they have advantages in different aspects. The Class I distributions have closed-form formulas for probability densities, probability distribution functions and quantile functions, and the Class II distributions have a great potential in modelling data sets with extremely unbalanced tails. We then fit the correlation structure of the empirical data to a simple functional form generated by superposing two or more OU processes. This correlation structure can effectively explain the QLRD phenomena and determine the weights of the superposition. Finally, we construct a stochastic electricity price model based on the fitted marginal distribution and the correlation structure.

![](/api/attachments/9WR7QEAA/fulltext/images/e3d924d4e299258ff554d6f034aa0bfd49a1120202b123018411480fdc06e4dd.jpg)  
Fig. 1. Historical electricity daily spot prices.

The organization of the rest of our paper is as follows. A brief review on other approaches to electricity price modelling is given in Section 2. We then describe our approach in Section 3 and present some results on parameter estimation using electricity daily spot prices in Section 4. Some applications in electricity option pricing and risk management are highlighted in Section 5. We conclude with pointing out future research direction in Section 6.

## 2. Literature review

Electricity prices cannot be adequately represented by the classic financial asset pricing models such as the geometric Brownian motion (GBM) model that underlies the Black–Scholes option pricing formula. Fig. 1 clearly demonstrates this point. Mean-reversion is a common feature in almost all commodity prices (e.g. Ref. [14]). In a realistic electricity price model, mean-reversion, jump, and stochastic volatility are among the key characteristics that need to be captured (see Ref. [7,12]). Ref. [5] offers a one-factor price model that combines a mean-reverting process with a single jump process. Ref. [6] presents three meanreversion jump-diffusion models including multifactor affine jump-diffusion models that can incorporate regime-switching jumps as well as stochastic volatility. By introducing jumps into the continuoustime mean-reverting spot price models, one can better capture the abrupt market changes caused by unpredictable scenarios such as abnormal weather conditions and forced capacity outages. Power prices simulated from each of the three models in Ref. [6], as plotted in Fig. 2, reveal a strong similarity to historical power price curves shown in Fig. 1.

Unfortunately, all of these models, which adopt certain types of stochastic processes to model power prices, require a relatively large amount of market price data, in particular options prices, for carrying out rigorous parameter estimation. However, in the newly developed power markets, neither quality nor quantity of options price data can be guaranteed. In a discretetime setup, [13] examines a Markov regime-switching model with a mean-reverting stochastic process model as an alternative power price model. Using data from four electricity markets, they estimate the model by applying the method of maximum likelihood. Ref. [1] utilizes a frequency-domain method to separate out periodic price variations from random variations and then estimate the volatility and mean-reversion parameters associated with the random variation of power prices. Neither of the two models is not fully calibrated with market prices of electricity derivatives.

![](/api/attachments/9WR7QEAA/fulltext/images/898a308f47992cb6120f0d54585ff819f6981af8c029a757fef10188e66343ce.jpg)  
Fig. 2. Simulated spot prices from mean-reversion jump-diffusion models.

With respect to the marginal distributions and the quasi-long-range dependent structure, some financial time series are investigated in Refs. [3,4,11]. Some of their conclusions are:

<sup>!</sup> The marginal distributions of those time series have tails that are heavier than the tail of a normal distribution but lighter than that of a Cauchy distribution. Furthermore, their tails are often unbalanced, by which we mean that one side is heavier than the other side.

<sup>!</sup> The quasi-long-range dependent structure in those time series can be fitted very well by the following correlation structure

$$
r (u) = w \rho_ {0} ^ {u} + (1 - w) \rho_ {1} ^ {u},\tag{1}
$$

where r(u) is the autocorrelation function, w, $\rho _ { 0 } ,$ $\rho _ { 1 } , \in ( 0 , 1 )$

<sup>!</sup> The correlation structure of Eq. (1) can be obtained by just using the superposition two OU processes which will be described in the next section.

## 3. Model description

An Ornstein–Uhlenbeck type process, or for short an OU process, is a stationary stochastic process x(t) that satisfies a stochastic differential equation of the form

$$
\mathrm{d} x (t) = - \lambda x (t) \mathrm{d} t + \mathrm{d} z (\lambda t)\tag{2}
$$

where $z ( \lambda t )$ is a Levy process and k is a positive constant. $z ( \lambda t )$ may depend on k and it is referred to as the background driving Levy process, abbreviated BDLP.

Let P(t) denote the price of electricity at time t. $X _ { \varDelta } ( t )$ represents the logarithmic difference of electricity prices over time interval of length D, namely,

$$
X _ {\varDelta} (t) = \log (P (t + \varDelta)) - \log (P (t)).\tag{3}
$$

As D becomes irrelevant once fixed, we denote $X _ { \varDelta } ( t )$ by $X ( t )$ hereon. We propose to model $X ( t )$ and its serial correlation structure by the superposition of two independent OU processes. Specifically,

$$
\begin{array}{l} X (t) = X _ {1} (t) + X _ {2} (t) \\ \mathrm{d} X _ {j} (t) = - \lambda_ {j} X _ {j} (t) + \mathrm{d} Z _ {j} (t) \text {   for   } j = 1, 2 \end{array}\tag{4}
$$

where $X _ { 1 } ( t )$ and $X _ { 2 } ( t )$ are two independent OU processes, $Z _ { 1 } ( t )$ and $Z _ { 2 } ( t )$ are two independent Levy processes (the BDLP’s), and $\lambda _ { j } \mathbf { \bar { s } }$ are positive constants. Should a stronger series dependence structure be encountered in power price data, we can easily extend our model (4) to capture it by superposing more than two independent OU processes.

One important fact is that the autocorrelation function of $X ( t )$ has the exact form of Eq. (1), with

$$
\begin{array}{l} \rho_ {i} = \exp (- \lambda_ {i}), i = 1, 2; \\ w = \frac {\operatorname{Var} (X _ {1} (t))}{\operatorname{Var} (X _ {1} (t) + X _ {2} (t))}. \end{array}\tag{5}
$$

To estimate the parameters in Eq. (4), one can simply employ the least-squares estimation (LSE) or $\bar { \boldsymbol { L } ^ { 1 } }$ method to match the function $r ( u )$ defined by Eq. (1) to the empirical cumulative autocorrelation functions, which can be obtained using SAS or other standard mathematical software.

Remark 1. A special case of our model is where the Levy processes in Eq. (4) are replaced by two standard Brownian motions (possibly correlated with correlation coefficient $\rho )$ . Let $\varphi ( \nu , t )$ denote the characteristic function of $X _ { T }$ conditional on $X _ { t } ,$ namely,

$$
\varphi (v, t) \equiv E \left[ e ^ {i \cdot v \cdot X (T)} | X (t) \right]
$$

where $\nu { \in } \mathcal { R }$ . Then we know that $\varphi ( \nu , t )$ is of the following form.

$$
\varphi (v, t) = e ^ {\alpha (v \cdot i, t) + v \cdot i \left(X _ {1} (t) e ^ {- \lambda_ {1} (T - t)} + X _ {2} (t) e ^ {- \lambda_ {2} (T - t)}\right)}
$$

where $\alpha ( \nu \cdot i , t )$ is an explicit function of time t (but a little tedious to fully specify here). With this characteristic function, we can apply a Generalized Method of Moments to estimate the parameters $\lambda _ { j } ,$ ${ j = } 1 , 2$ and $\rho .$

In practice, there are different approaches for specifying an OU process. One approach is called the BDLP modelling, which first specifies the BDLP of an OU process and then determines the stationary distribution of the OU process. Another approach is called the stationary distribution modelling, which starts with the stationary distribution models. In both approaches, the likelihood functions based on discretely observed data are usually not explicitly available except for certain special cases of the stable OU process. Therefore, the parameter estimation often resorts to simulation-based methods such as the partner approach or the Quantile–Quantile (Q–Q) estimation approach proposed by Ref. [11]. In these simulation-based procedures, the most time-consuming part is to simulate the stochastic integral:

$$
\int_ {0} ^ {\varDelta} f (t) \mathrm{d} Z (t)\tag{6}
$$

where $f ( t )$ is a deterministic function and $Z ( t )$ is a properly defined Levy process.

Several approaches are available for evaluating the stochastic integral (6). One approach is to use the path-wise approximation, provided that $Z ( t )$ can be conveniently simulated for any $t { > } 0 .$ . Another approach is to utilize the series representation, which is based on the following results. Let U(dx) be the Levy measure of a non-decreasing Levy process $Z ( t )$ . The upper tail of $U$ is defined by $Q ^ { + } ( x ) =$ $U ( [ x , + \infty ) ) . \stackrel { \textstyle \top } { Q } ^ { - 1 }$ denotes the inverse of $\mathrm { Q } ^ { + }$ , namely, $Q ^ { - 1 } ( x ) { = } \operatorname* { i n f } \{ y { > } 0 , ~ Q ^ { + } ( y ) { \leq } x \}$ . Then Eq. (6) has the following representation.

$$
\left\{\int_ {0} ^ {t} f (s) \mathrm{d} Z (s): t > 0 \right\} \stackrel {{\mathcal {L}}} {{=}} \left\{\sum_ {i = 1} ^ {\infty} f \left(t r _ {i}\right) Q ^ {- 1} \left(a _ {i} / t\right): t > 0 \right\}\tag{7}
$$

where $\big \{ w _ { i } \big \} , \big \{ a _ { i } \big \}$ , and $\left\{ \boldsymbol { r } _ { i } \right\}$ are three independent series of independent random variables with $w _ { i } \mathrm { ^ { * } s }$ being standard normal, $r _ { i } \mathrm { { ^ { * } s } }$ being uniform on [0,1], and $a _ { 1 } { < } a _ { 2 } { < } \cdot \cdot \cdot { < } a _ { i } { < } \cdot \cdot \cdot$ being the sequence of arrival times of an independent Poisson process with intensity 1. However, to evaluate $\boldsymbol { Q } ^ { - 1 }$ in Eq. (7) is usually a rather time-consuming task. To achieve a fast simulation of Eq. (6), Ref. [11] proposes an inverse upper tail Levy measure modelling (IUTLMM) approach whose main ideas are to avoid the inverse evaluation of $\boldsymbol { Q } ^ { - 1 }$ and make the terms in Eq. (7) decay as fast as possible. In parameter inference through IUTLMM, a key step to reduce the computational workload is to suitably determine the range of the tail thickness of the BDLP. As shown in Ref. [11] that the tail thickness of the BDLP of an OU process is exactly the same as that of its stationary (i.e. marginal) distribution, one only needs to know the tail thickness of the stationary distribution for the purpose of fixing the parameter range for the tail index of the BDLP. Therefore, determining the marginal distribution of the electricity price model (4) is a major step in fully specifying the process X(t) in Eq. (4).

Empirical examinations have revealed a wide spectrum of tail behaviors in the marginal distributions of electric prices. To fit the stationary distribution of power price well, we need to investigate the distributions with versatile tail behaviors.

## 3.1. Marginal distribution of X(t)

In this section, we introduce two new classes of distributions, termed as Class I and Class II distributions (see also Ref. [11]). These distributions are defined by quantile functions. We illustrate their properties and versatile tail behaviors which make them suitable candidates for the marginal distribution of an OU process concerned in model (4).

A Class I distribution is denoted by $\mathcal { Q } _ { \mathrm { I } } ( \alpha , \beta , \delta , \mu )$ and defined by the quantile function $q ( y ; \alpha , \beta , \delta , \mu )$ given below. For $y { \in } ( - 1 , 1 )$ ,

$$
q (y; \alpha , \beta , \delta , \mu) = \delta^ {\frac {1}{\alpha}} \left\{\log \frac {y ^ {\beta}}{1 - y ^ {\beta}} \right\} ^ {\left(\frac {1}{\alpha}\right) + \mu}\tag{8}
$$

where model parameters $\alpha , \beta , \delta { \in } R _ { + }$ and $\mu { \in } R$ . The superscript $^ { \circ } ( \alpha ) ^ { \prime }$ for $\alpha { > } 0$ represents the operation:

$$
x ^ {(\alpha)} = \left\{ \begin{array}{l l} x ^ {\alpha} & \text { if } x > 0 \\ 0 & \text { if } x = 0 \\ - (- x) ^ {\alpha} & \text { if } x <   0 \end{array} \right.
$$

All parameters in Eq. (8) have intuitive interpretations: $\mu$ is a location parameter; d functions as a scaling parameter; $\beta$ acts like a tail balance adjuster: $\beta { = } 1$ means a balanced tail, and $\beta { < } ( > ) 1$ means the left (right) tail is fatter than the right (left) tail; and a indicates the tail order—the smaller the $\alpha ,$ the fatter the tail of the distribution.

The cumulative distribution function and the probability density function (PDF) of $\mathcal { Q } _ { \mathrm { I } } ( \alpha , \beta , \delta , \mu )$

are also in closed-form. Specifically, the PDF is given by:

$$
p (x; \alpha , \beta , \delta , \mu) = \frac {\alpha \cdot \frac {(x - \mu) ^ {(\alpha)}}{(x - \mu)} e ^ {- \frac {1}{\delta} (x - \mu) ^ {(\alpha)}}}{\delta \beta \cdot \left(1 + e ^ {- \frac {1}{\delta} (x - \mu) ^ {(\alpha)}}\right) ^ {1 + \frac {1}{\beta}}}\tag{9}
$$

for $x { \in } ( - \infty , \mu ) \cup ( \mu , + \infty )$ . We note that since a Class I distribution has a closed-form probability density function, a straightforward maximum likelihood estimation procedure can be employed to obtain the parameters $\alpha , \beta , \delta$ and $\mu$ in Eq. (8).

The Class II distributions are constructed to fit the extremely unbalanced tails of empirical data. We denote a Class II distribution by $Q _ { \mathrm { I I } } ( \alpha _ { - } , \alpha _ { + } , \delta _ { - } , \delta _ { + } , \mu )$

Its quantile function $q ( y ; \alpha _ { - } , \alpha _ { + } , \delta _ { - } , \delta _ { + } , \mu )$ is specified as follows. For $y { \in } ( - 1 , 1 )$ ,

$$
\begin{array}{l} q (y; \alpha_ {-}, \alpha_ {+}, \delta_ {-}, \delta_ {+}, \mu) \\ = - \delta_ {-} ^ {\frac {1}{\alpha_ {-}}} \left(\log \frac {1}{y}\right) ^ {\frac {1}{\alpha_ {-}}} + \delta_ {+} ^ {\frac {1}{\alpha_ {+}}} \left(\log \frac {1}{1 - y}\right) ^ {\frac {1}{\alpha_ {+}}} + \mu \end{array}\tag{10}
$$

where model parameters $\alpha _ { - } , \ \alpha _ { + } , \ \delta _ { - } , \ \delta _ { + } \in R .$ and $\mu { \in } R . \ \alpha$ and $a _ { + }$ measure the fatness of the respective left and right tails of a Class II distribution while $\delta _ { - }$ and $\delta _ { + }$ act as scaling factors at the two sides of the distribution. $\mu$ is again a location parameter. We are mainly interested in the cases where $\smash { \alpha _ { - } \le 1 }$ and $\mathsf { \alpha } _ { \mathsf { + } } \mathsf { \leq } 1$

![](/api/attachments/9WR7QEAA/fulltext/images/37692bdd8c508bdd78039a2d71e94c3af2ff773dc59228de1fd82148233687cc.jpg)

![](/api/attachments/9WR7QEAA/fulltext/images/c1130dbb0483311efbeb324d987d7d50d1a9a0ec2978bd5578f5841585330e74.jpg)

![](/api/attachments/9WR7QEAA/fulltext/images/ab75c19aef28b81ed192f306b3513f55589a29b14b9b968d21b4f2a74760d21e.jpg)

![](/api/attachments/9WR7QEAA/fulltext/images/dd90b966245595af42febc661de46f3d33f23e071109618399e79863c4f11514.jpg)

![](/api/attachments/9WR7QEAA/fulltext/images/dac4246568633d7a4227f508de051c2b227a2f8c4b6649422826abeb54483c78.jpg)

![](/api/attachments/9WR7QEAA/fulltext/images/3c6243fb8ab5ea015b942340a52081a98c492142ea93f2ec402025875ec7fc0c.jpg)

![](/api/attachments/9WR7QEAA/fulltext/images/df1515230cf3c3fdafc0e229c32f0891f9a82c09fa3b97d4d689d93e9e6d120f.jpg)

![](/api/attachments/9WR7QEAA/fulltext/images/1d178dc9cd98c80ef78c83c22cbecacf83602736e3ec1f13d5bbf64d244ae6dd.jpg)

![](/api/attachments/9WR7QEAA/fulltext/images/9edce3009d1ee8516ae33d8975ad10916984fd26121c50bb0b15aa0063f90480.jpg)

![](/api/attachments/9WR7QEAA/fulltext/images/c5f9ce2d293344ca5b612c4988392e87a48023569e32ced66f294845b2a914f0.jpg)

![](/api/attachments/9WR7QEAA/fulltext/images/732c05e07f9129567a43bdd52a6ba1f2fb811e893d37bcc154dee23407000114.jpg)  
Fig. 3. Probability density function: different Class I distributions.

![](/api/attachments/9WR7QEAA/fulltext/images/728644b17b2608fb05acc4bce81460a9b207d26f72c3c4119ac52e1d57786e52.jpg)

A remarkable feature of a Class II distribution is its tremendous flexibility in having different tail orders at the two sides of the PDF: a for the lefthand side and $\mathsf { \Omega } \mathsf { \Omega } \partial _ { \mathsf { \Gamma } } \left( \mathsf { \Omega } \right)$ for the right-hand side. Moreover, the skewness of the distribution is jointly determined by ${ \alpha - / + }$ and $\delta _ { - / + }$ at both sides in the sense that if $\delta _ { - } \geq \delta .$ and further $a _ { 1 } \leq x _ { + }$ , then the distribution will skew to the left; but if $a _ { 1 } \leq a _ { + }$ , then it cannot be concluded that the distribution will skew to the right. Instead, we can fix $\delta _ { - }$ and $\delta _ { + }$ (namely let $\delta _ { - } { = } \delta _ { + } )$ and then estimate other parameters. After doing so, $a _ { - } \leq x _ { + }$ will then imply that the distribution is skewed to the left.

## 3.2. Properties of Class I and Class II distributions

We first illustrate the flexible shapes of the PDFs that Class I and II distributions can have in two figures. Figs. 3 and 4 plot the density functions of a set of Class I and II distributions for different parameter settings (we set $\mu { = } 0$ in all cases). We see a broad range of tail behaviors exhibited by these Class I and II distributions from the density plots.

For arbitrary constants c and d, the following facts about Class I and II distributions are straightforward to verify.

<sup>!</sup> If $X { \sim } \mathcal { Q } _ { \mathrm { I } } ( \alpha , \beta , \delta , \mu ) \ \Lambda ^ { \cdots }$ means <sup>b</sup>is distributed as<sup>Q</sup>), then $c X ^ { + } d { \sim } Q _ { \mathrm { I } } ( \alpha , \beta , c ^ { \alpha } \delta , c \mu { + } d )$

<sup>!</sup> If $X { \sim } \mathcal { Q } _ { \mathrm { I I } } ( \alpha _ { - } , \alpha _ { + } , \delta _ { -- } , \delta _ { + } , \mu )$ , then $c X + d - Q _ { \mathrm { I I } } ( \alpha \_ , \alpha _ { + } ,$ $c ^ { \alpha } { - } \delta _ { - } , c ^ { \alpha + } \delta _ { + , c \mu + d ) }$

Several other interesting properties pertaining to Class I distributions are as follows:

<sup>!</sup> Multimodality: when $\alpha { > } 1$ , the probability density function of a Class I distribution is bimodal.

<sup>!</sup> Closed under powering: let $\mathcal { Q } _ { \mathrm { I } } ( \alpha , \beta , \delta )$ denote $\mathcal { Q } _ { 1 } ( \alpha , \beta , \delta , 0 )$ , then the following holds true for $n { > } 0 .$

If $X \sim \mathcal { Q } _ { \mathrm { I } } ( \alpha , \beta , \delta )$ ; then $X ^ { n } Q _ { \mathrm { I } } \Big ( \frac { \alpha } { n } , \beta , \delta \Big )$

![](/api/attachments/9WR7QEAA/fulltext/images/06c33c6c3765c866d343f4436ddb35a00753485592eda4d7de568e38cc87f265.jpg)

![](/api/attachments/9WR7QEAA/fulltext/images/e25b832c6da9d2e2adf616b2c6c44aa17f03a29ebe9d2f4ffec204a16cb59d43.jpg)

![](/api/attachments/9WR7QEAA/fulltext/images/3f20c7c33aca47288be3b3c6d938eae24ceca310ec8ec09589f5cdea2cdb0762.jpg)

![](/api/attachments/9WR7QEAA/fulltext/images/2a91aa9ab9cc89b86fc3978e1c7f6d55ccac77ea9ed0115f32dcd14715ec22ad.jpg)

![](/api/attachments/9WR7QEAA/fulltext/images/c05f48437e45eb27407a261c40645b069ab587c8246d0c2bbddb46e6e6d01f91.jpg)

![](/api/attachments/9WR7QEAA/fulltext/images/48ef8964008c0fc13a4a512b33a7f7ccb96ac92db8be7b289fd2ce1462a8a6f1.jpg)

![](/api/attachments/9WR7QEAA/fulltext/images/1821e51af1e9335e128b7440d372c319e494d1b11310b46d9ad4832c86598695.jpg)

![](/api/attachments/9WR7QEAA/fulltext/images/c422b46e6dc347e12fd13fc98d99b0dd997edc74e76c576c909705dbc32048f4.jpg)  
Fig. 4. Probability density function: different Class II distributions.

In general, if $n$ is an integer and $X { \sim } Q _ { \mathrm { I } } ( \alpha , \beta , \delta , \mu )$ 4 then $X ^ { n }$ is just a linear combination of random variables in form $\mathcal { Q } _ { \mathrm { I } } ( \alpha , \beta , \delta )$

<sup>!</sup> The moments formulae: let $X { \sim } Q _ { \mathrm { I } } ( \alpha , \beta , \delta , \mu )$ and $\alpha ( \alpha , \beta , \delta ) { \equiv } \mathrm { E } [ \mathcal { Q } _ { \mathrm { I } } ( \alpha , \beta , \delta ) ]$ , then the nth moment of X is given by:

$$
\begin{array}{l} \operatorname{E} [ X ^ {n} ] = \mu^ {n} + \mathrm{C} _ {n} ^ {1} \mu^ {n - 1} \mathrm{a} (\alpha , \beta , \delta) + \dots \\ \qquad + \mathrm{C} _ {n} ^ {\mathrm{k}} \mu^ {n - \mathrm{k}} \mathrm{a} \Big (\frac {\alpha}{\mathrm{k}}, \beta , \delta \Big) + \dots + \mathrm{a} \Big (\frac {\alpha}{n}, \beta , \delta \Big). \end{array}
$$

In particular,

$$
\operatorname{E} [ X ] = \mu + a (\alpha , \beta , \delta)
$$

$$
\operatorname{Var} [ X ] = a \left(\frac {\alpha}{2}, \beta , \delta\right) - a ^ {2} (\alpha , \beta , \delta).
$$

Note that the variance does not depend on $\mu .$

## 4. Parameter estimation and calibration

To infer the model parameters in a Class I or Class II distribution, we take the Quantile–Quantile (Q–Q) estimation approach proposed by Ref. [11]. The Q–Q approach is based on directly matching the quantile function. Suppose a distribution class is defined by a quantile function which is parameterized by a vector h in the parameter space $\Theta \subseteq R ^ { n }$ . We fit empirical data to the distribution class by searching for the $\operatorname { \mathrm { ~ } } ^ { \mathsf { \tiny ~ \mathscr { ~ } } } \mathsf { b e s t } ^ { \mathsf { \tiny ~ \mathfrak { ~ } } } \theta$ that minimizes the <sup>b</sup>distance<sup>Q</sup> (e.g. in $L _ { \mathrm { 1 } } \mathrm { - n o r m }$ sense)

![](/api/attachments/9WR7QEAA/fulltext/images/c332efde55a9abfd179901582c7f49443f783b835187f0bf686848102fd89fd8.jpg)  
Fig. 5. Historical log-price differences: Cal-PX (left) vs. PJM (right).

between the theoretical quantile function as a function of $\theta$ and the empirical quantile function. This estimation method is a simulation-based scheme (similar to the one used in [8]) and it takes full advantage of the closed-form quantile function.

Specifically, let $\{ F ( x ; \theta ) , \theta { \in } \Theta \subseteq R ^ { n } \}$ be a distribution class parameterized by h. A member of $F ( x ; \theta )$ with unknown $\theta$ generates a series of observations $Y _ { 1 } , Y _ { 2 } ; \cdots , Y _ { n }$ . Further assume that $F ( x ; \theta )$ can be simulated for any given h. The $\mathrm { Q - Q }$ estimation method infers $\theta$ from $Y _ { 1 } , Y _ { 2 } ; \cdots , Y _ { n }$ by solving the minimization problem (Eq. (11)).

$$
\min _ {\theta \in \Theta} f (R _ {1} (Y), \dots , R _ {l} (Y); \theta , T _ {1} (X), \dots , T _ {l} (X))\tag{11}
$$

where $f ( \cdot )$ is an appropriately chosen score function, with the most common choice being the $L _ { 1 }$ or $L _ { 2 }$ norm. $\{ R _ { 1 } ( Y ) , \cdot \cdot \cdot , R _ { l } ( Y ) \}$ and $\{ T _ { 1 } ( X ( \theta ) ) , \cdot \cdot \cdot , T _ { l } ( X ( \theta ) ) \}$ are empirical quantiles of $Y { = } ( \ Y _ { 1 } ; \cdots , Y _ { n } )$ and $X ( \theta ) =$ $( X _ { 1 } , \cdot \cdot \cdot , x _ { n ^ { \prime } } )$ , respectively, meaning that $R _ { i } ( Y ) =$ $F _ { n } ^ { - 1 } ( p _ { i } ; Y )$ and $T _ { i } ( X ) { = } F _ { n ^ { \prime } } ^ { - 1 } ( p _ { i } , X )$ . X(h) is simply a set of simulated samples of $F ( x ; \theta )$ for a given $\theta ;$ $F _ { n } ( \cdot , Y )$ denotes the empirical distribution function based on $Y$ with sample size $n ;$ and $( p _ { 1 } , p _ { 2 } ; \cdots , p _ { l } )$ denotes the set of probabilities for which the quantiles are obtained.

Since the theoretical quantiles are explicitly specified as $q ( u ; \theta )$ for the Class I and II distributions, Eq. (11) can be rewritten as:

$$
\min _ {\theta \in \Theta} f (R _ {1} (Y), \dots , R _ {l} (Y); \theta , q (p _ {1}; \theta), \dots , q (p _ {l}; \theta))\tag{12}
$$

![](/api/attachments/9WR7QEAA/fulltext/images/40516590b4707a8fb4c9a7a5d592a22e4609393ffef7c2b3f310a867bd68021d.jpg)

with f (<sup>d</sup> ) taking the form of

$$
\min _ {\theta \in \Theta} \sum_ {i = 1} ^ {l} w _ {i} | R _ {i} (Y) - F ^ {- 1} (p _ {i}) |
$$

or

$$
\min _ {\theta \in \Theta} \sum_ {i = 1} ^ {l} w _ {i} \left[ R _ {i} (Y) - F ^ {- 1} \left(p _ {i}\right) \right] ^ {2}
$$

where $w _ { 1 } ; \cdot \cdot , w _ { l }$ are suitably chosen weights.

For the empirical analysis of fitting Class I and II distributions to the marginal distribution of electricity price, we use two data sets: the daily average prices at the California Power Exchange (Cal-PX) market and the Pennsylvania–New Jersey–Maryland (PJM) market from April 1, 1998, to August 31, 2000. We take D=1 day in Eq. (3) and examine the marginal distribution of $X ( t ) { = } \log ( P ( t ) ) { - } \log ( P ( t { - } 1 ) )$ (namely, X(t) is the log-price difference between the day-t and the day-(t1) prices). The two panels of Fig. 5 plot the time series of the log-price difference at Cal-PX and PJM.

Applying the Q–Q estimation method, we obtain the parameters for the Class I distributions that fit the Cal-PX and PJM prices the best. Fig. 6 illustrates the Quantile–Quantile plots (Q–Q plots) of the empirical quantiles of the Cal-PX and PJM price distributions versus their respective theoretical quantiles (the estimated parameters are shown in the two panels as well), where the theoretical quantiles are plotted on the x-axis and the empirical quantiles on the y-axis.

![](/api/attachments/9WR7QEAA/fulltext/images/6db58f074a24b10df1a003fb27296e0c848c6c135d4bb63332752896ae40f7f5.jpg)

Table 1  
Estimated parameters of Class I distributions

<table><tr><td></td><td> $\alpha$ </td><td> $\beta$ </td><td> $\delta$ </td><td> $\mu$ </td></tr><tr><td>Cal-PX</td><td>0.6124</td><td>0.8819</td><td>0.1901</td><td>-0.0226</td></tr><tr><td>PJM</td><td>0.7789</td><td>0.9765</td><td>0.2291</td><td>-0.0059</td></tr></table>

Each of the two Q–Q plots in Fig. 6 forms a relatively straight line, which indicates a good fit between the empirical quantile function and the theoretical quantile function, except for several outliers. The parameters for Class I distributions obtained using Cal-PX and PJM price data sets are reported in Table 1.

For the Cal-PX data, $\beta { = } 0 . 8 8 1 9$ suggests that the left tail of the Cal-PX log-return distribution is fatter than the right tail. For the PJM data, although acceptable, the fit of PJM log-return is not as good as that of the Cal-PX log-return. The Q–Q plot of the empirical quantiles of PJM data versus the theoretical quantiles deviates slightly from the $4 5 ^ { \circ }$ line (see the right panel of Fig. 6). Similar to the Cal-PX data, the PJM price data also yields a less-than-one $\beta$ value (b=0.9765) indicating a fatter left tail of the logreturn distribution in the PJM market.

![](/api/attachments/9WR7QEAA/fulltext/images/7803c5a2e46006d48b411805118789f6279c16bfb882b8a6a002c02c825e367d.jpg)  
Fig. 6. The Q–Q plots for fitted Class I distributions: Cal-PX (left) vs. PJM prices (right).

α-left=0.63864α-right=0.83561 δ-Ieft=0.20889 δ-right=0.24231 μ=-0.080405

Estimated parameters of Class II distributions

<table><tr><td></td><td> $\alpha_{-}$ </td><td> $\alpha_{+}$ </td><td> $\delta_{-}$ </td><td> $\delta_{+}$ </td><td> $\mu$ </td></tr><tr><td>Cal-PX</td><td>0.5264</td><td>0.5907</td><td>0.1833</td><td>0.1833</td><td>0.0164</td></tr><tr><td>PJM</td><td>0.6386</td><td>0.8356</td><td>0.2089</td><td>0.2423</td><td>0.0804</td></tr></table>

We next use the Q–Q method to fit Class II distributions to Cal-PX and PJM daily log-price differences. The estimated parameters are reported in Table 2.

The Q–Q plot of the fitted Class II distribution on the PJM price data appears to be better than that of the Class I distribution (Fig. 7). Moreover, $\alpha _ { - }$ is less than $\alpha _ { + }$ for the PJM price data implying a fatter left tail than the right tail. This is consistent with the observation made from the PJM fitting results in the Class I distribution case.

For the Cal-PX data, we restrict $\delta _ { + }$ to be identical with $\delta _ { - } .$ The fitted Class II distribution generates a reasonably good Q–Q plot as well. The estimated $\alpha _ { + }$ is greater than $\alpha _ { - }$ (see Table 2), which is again consistent with the observation of a fatter right tail than the left tail in the distribution of Cal-PX log-returns (as implied by the Cal-PX fitting results in the Class I distribution case).

![](/api/attachments/9WR7QEAA/fulltext/images/ef694c57d7505341b096c62bfaad79c4978f9daf97c28b8c8dcd937bbc230103.jpg)

## 5. Options pricing and risk management applications

The marginal distribution of the price process $X ( t )$ is a key component in pricing European-style electricity options and calculating risk management metrics.

## 5.1. Pricing of European-style options

Suppose the electricity price is x at time 0. Let $C ( x , T )$ denote the value of an European option with a terminal payoff of f( P(T)) at maturity time $T$ where $P ( T )$ is the electricity price at time $T$ and $f ( \cdot )$ is a real-valued measurable function. Assuming there is no arbitrage opportunities, then by the risk-neutral options pricing theorem of Ref. [9], there exists a risk-neutral probability distribution $\boldsymbol { Q }$ over all possible realizations of P(T) so that

$$
C (x, T) = E ^ {Q} \left[ e ^ {- r T} f (P (T)) \right] = e ^ {- r T} \int_ {- \infty} ^ {+ \infty} f (s) d Q (s)\tag{13}
$$

where $r$ is the constant risk-free interest rate. Recall that $X ( t )$ denote log( P(t+T))log( P(t)). Let Q<sup>˜</sup> (s)

![](/api/attachments/9WR7QEAA/fulltext/images/f96bcb39fb6d989375e21339c494d6491e7a68092a05a330d7c530612630d292.jpg)  
Fig. 7. The Q–Q plots for fitted Class II distributions: Cal-PX (left) vs. PJM prices (right).

denote the marginal distribution function of $X ( t )$ under the risk-neutral measure. Then

$$
P (T) \stackrel {{\mathcal {L}}} {{=}} P (0) \exp (X (0))
$$

(L means the probability law) and Eq. (13) becomes

$$
\begin{array}{l} C (x, T) = E ^ {Q} \big [ e ^ {- r T} f (P (T)) \big ] \\ \qquad = E ^ {\tilde {Q}} \big [ e ^ {- r T} f (P (0) \exp (X (0))) \big ] \\ \qquad = e ^ {- r T} \int_ {- \infty} ^ {+ \infty} f (x \mathrm{e} ^ {\mathrm{s}}) \mathrm{d} \tilde {\mathbf {Q}} (\mathrm{s}). \end{array}\tag{14}
$$

Thus we can value any European-style option with payoff being a function of the terminal price $P ( T )$ based on the marginal distribution of X(0) under the risk-neutral probability measure.

## 5.2. Value-at-risk and expected shortfall

Let $X ( t )$ denote the return of a portfolio X over some fixed time interval D at time t. As one important risk management metric, Value-at-Risk (VaR) has long been utilized in practice. The VaR of a portfolio X at level a (for $0 { < } \alpha { < } 1 )$ over time horizon D, denoted by $\operatorname { V a R } ^ { ( \alpha ) } ( X )$ , is a quantity that equals the worst possible loss of the portfolio X at the $1 0 0 \times ( 1 - \alpha ) \%$ confidence level. Namely,

$$
x ^ {\alpha} (X) = \sup _ {x} \{x: P [ X \leq x ] \leq \alpha \}
$$

$$
\operatorname{VaR} ^ {(\alpha)} (X) = - x ^ {(\alpha)} (X)
$$

Note that

$$
\operatorname{VaR} ^ {(\alpha)} (X) = - q (\alpha)\tag{15}
$$

where $q ( u )$ is the quantile function of X.

In criticizing VaR for not having a natural subadditive property (see Ref. [2]), several other alternative risk measures such as Tail Conditional Expectation (TCE), Conditional VaR (CVaR), and Expected Shortfall (ES) have also been proposed. Among these measures, Expected Shortfall, defined as the expected loss incurred within the $\%$ worst cases of the portfolio/asset return, is the most popular quantity. The ES of X at level a can be calculated as

$$
\mathrm{ES} ^ {(\alpha)} = - \frac {1}{\alpha} \int_ {0} ^ {\alpha} q (u) d u\tag{16}
$$

where $q ( u )$ is the quantile function of X.

Regardless which risk management measure to be used, it is clear from Eqs. (15) and (16) that the two important risk metrics, VaR and ES, can be easily calculated if the underlying price or return process follows model (4) with the marginal distribution given by the quantile function defined in Eqs. (8) or (10).

## 6. Conclusion

In summary, we propose a mean-reverting Levy process driving stochastic model, which is a superposition of two OU type processes, for modelling the electricity price. The model has the potential of capturing the autocorrelation structure of the electricity price return series and it enables the parameter inference based on its marginal distribution. By obtaining the tail index of the marginal distribution of the proposed price model, we can pin down the tail index of the background driving Levy process for the OU processes, which is a major step in fully determining the proposed model. We examine two classes of quantile-defined distributions for fitting the marginal distribution of electricity price series and obtain satisfactory fitting results in two power markets. These distributions effectively model the heavy and unbalanced tail behaviors of the electricity price caused by jumps and stochastic volatility since they accommodate rich tail behaviors by design. The fitted marginal distribution of the underlying process (Eq. (4)) can be directly applied to the options pricing and risk measurement calculation problems. In future research, we will report results on inferring the other essential parameters, $\lambda _ { j } \mathbf { \bar { s } } ,$ of the underlying process (Eq. (4)) based on marginal distributions for the purposes of dynamic hedging and other risk management applications.

## Acknowledgements

This research is supported in part by NSF Grant ECS-0134210 and a research grant from the Power System Engineering Research Center (PSerc). The usual disclaimers apply.

## References

[1] F.L. Alvarado, R. Rajaraman, Understanding price volatility in electricity markets, Proceedings of the 33rd Hawaii International Conference on System Sciences, Hawaii, 2000.

[2] P. Artzner, F. Delbaen, J. Eber, D. Heath, Coherent measures of risk, Mathematical Finance 9 (1999) 203 – 228.

[3] O.E. Barndorff-Nielsen, Processes of normal inverse Gaussian type, Finance and Stochastics 2 (1998) 41 – 68.

[4] O.E. Barndorff-Nielsen, W. Jiang, An initial analysis of some German stock prices, Working Papers No. 15 (1998) (CAF).

[5] G. Barz, B. Johnson, Modeling the prices of commodities that are costly to store: the case of electricity, Proceedings of the Chicago Risk Management Conference (May 1998), Chicago, IL, 1998.

[6] S.J. Deng, Stochastic models of energy commodity prices and their applications: mean-reversion with jumps and spikes, Working Paper, University of California, Berkeley, 1999.

[7] S.J. Deng, B. Johnson, A. Sogomonian, Exotic electricity options and the valuation of electricity generation and transmission assets, Decision Support Systems 3 (30) (2001) 383–392.

[8] P.J. Diggle, R.J. Gratton, Monte Carlo methods of inference for implicit statistical models, Journal of the Royal Statistical Society. Series B, Statistical Methodology 46 (1984) 193–227 (with discussion).

[9] M. Harrison, D. Kreps, Martingales and arbitrage in multiperiod securities markets, Journal of Economic Theory 20 (1979) 381–408.

[10] R. Gilbert, E. Kahn (Eds.), International Comparisons of Electricity Regulation, Cambridge University Press, Cambridge, UK, 1996, pp. 1 – 55.

[11] W. Jiang, Some Simulation-based Models Towards Mathematical Finance, PhD Dissertation, University of Aarhus, 2000.

[12] Vincent Kaminski, The challenge of pricing and risk managing electricity derivatives, The US Power Market, Risk Publications, London, UK, 1997, pp. 149– 171.

[13] T. Mount, R. Ethier, Estimating the volatility of spot prices in restructured electricity markets and the implications for option values, PSerc Working Paper, Cornell University, 1998.

[14] Eduardo S. Schwartz, The stochastic behavior of commodity prices: implications for valuation and hedging, Journal of Finance (1997 July) 923– 973.

[15] Frank Wolak, Market Design and Price Behavior in Restructured Electricity Markets: An International Comparison, mimeo, Stanford University, 1997.

Dr. Shi-Jie Deng is Assistant Professor of Industrial and Systems Engineering at Georgia Institute of Technology. Dr. Deng’s research interests include financial asset pricing and real options valuation, financial engineering applications in energy commodity markets, transmission pricing in electric power systems, stochastic modelling and simulation. He received the CAREER Award from the National Science Foundation in 2002. Dr. Deng has served as a consultant to several private and public organizations on issues of risk management and asset valuation in the deregulated electricity industry. Dr. Deng holds a BSc degree in Applied Mathematics from Peking University in China, a master of science in Mathematics from the University of Minnesota at Twin Cities, and MS and PhD in Industrial Engineering and Operations Research from the University of California at Berkeley.

Dr. Wenjiang Jiang is Professor of Financial Mathematics and Mathematical Statistics at Yunnan Normal University. Dr. Jiang’s research interests include stochastic models towards finance (Stochastic Volatility Models, OU processes, Processes of the Generalized Hyperbolic type, Processes with quasi-long-range dependence), financial asset pricing, VaR type models, computational stochastic, estimation via simulation in complex models, Heavy-tailed distributions and their applications.

Dr. Jiang holds a BSc degree in Mathematics and a master of science in Statistics from Peking Normal University in China, and PhD in Mathematical Finance from Aarhus University, Denmark.
