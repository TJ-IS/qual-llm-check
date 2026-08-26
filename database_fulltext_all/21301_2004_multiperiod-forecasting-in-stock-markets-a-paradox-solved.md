---
otero_id: 21301
otero_key: "PE4K287F"
title: "Multiperiod forecasting in stock markets: a paradox solved"
authors: "Hans-Martin Krolzig; Juan Toro"
year: "2004"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(03)00085-x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Multiperiod forecasting in stock markets: a paradox solved

Hans-Martin Krolzig<sup>a</sup>, Juan Toro<sup>b,c,</sup>\*

<sup>a</sup> Economics Department, Nuffield College, Oxford, UK

<sup>b</sup> Economics Department, Oxford University, Oxford, UK

<sup>c</sup> CentrA, Sevilla, Spain

Available online 16 July 2003

## Abstract

One of the most striking results on asset pricing in the last 20 years is the better forecastability of long-horizon returns over one-step return forecasts. This could seem a paradox, given that the further our forecast horizon the greater the uncertainty we are bound to face. This point can been found in Campbell and Shiller [Journal of Finance 43 (1988) 661; Journal of Finance 40 (1985) 793; American Economic Review 76 (1986) 1142] among others. In this paper, we offer an alternative explanation to this ‘‘forecast paradox ’’ that is in agreement with Kim et al. [Review of Economic Studies 30 (1992) 25], who found that the negative serial correlation in long-horizon returns depends very much on the sample choice. Our explanation is based on the existence of simultaneous shifts in the time series of the equilibrium stock price and dividends. This explanation relies on the concept of co-breaking [D.F. Hendry, A theory of co-breaking, Mimeo, Nuffield College, Oxford, 1995.]. We put forward a stochastic present value model, in which we are able to show how shifts in the process for dividends lead to shifts in the equilibrium stock price.

This has important implications for multiperiod forecasting, as we demonstrate in this paper. An empirical application supports our results. In our empirical application, we model earning, dividends, stock prices, and the risk-free interest in the United States from 1926 to 1985. We can distinguish three different historical periods where the process for dividends and the equilibrium stock prices are characterized by different properties in terms of their means and variances. Our empirical model i extended to a forecasting exercise where the ‘‘forecast paradox’’ is solved. <sup>D</sup> 2003 Elsevier B.V. All rights reserved.

JEL classification: G12; C32; C52; C53 JEL classification: G12; C32; C52; C53

Keywords: Stock prices; Asset pricing; Returns behaviour; Markov switching; Structural breaks; Forecasting

## 1. Introduction

The time-series behavior of stock prices has been characterized as forecastable when conditioning on past values of returns. Although the forecastability is small when conditioning on past returns, the forecast improves greatly when the information set is extended and the conditioning set widens to include other variables.

One of the most striking results on asset pricing in the last 20 years is the better forecastability of longhorizon returns over one-step return forecast. This could seem a paradox given that the further our forecast horizon the greater the uncertainty we are bound to face. This point can be found in Refs. [2,4,20], among others. A common conclusion in these works is that between 20% and 30% of the variance of 4 or 5 years return can be accounted for by lagged multiperiod returns, dividend – price ratio, or price–earning ratio. Campbell and Shiller [2] argue that when the dividend–price ratio is used as conditioning variable, the latter can stand for a good proxy for future discounted return if we consider a present value model with time varying returns. Fama [8] considers a decomposition of the prices of stocks into a permanent and a transitory component. When the stationary component is highly persistent, multiperiod returns would show a strong negative correlation. The variance of multiperiod returns would thus be well explained just by past returns.

Theoretically, the long horizon forecastability of returns had been given two different explanations. The first refers to irrational markets where the price deviates temporarily from its equilibrium price as given by fundamentals. DeBondt and Thaler [4] argue that individuals do not use Bayesian rules at the time of updating new incoming information. On the contrary, individuals tend to overweight the most recent information. This overreaction bias allows analysts to predict future returns based only on past returns. An alternative theory suggests the existence of timevarying expected equilibrium returns that come from rational behavior in efficient markets.

In this paper we, offer an alternative explanation to this ‘‘forecast paradox ’’ that is in agreement with Kim et al. [18], who found that the negative serial correlation in long-horizon returns depends very much on the sample choice. More particularly, they show that when the first 10 years from the 1926–1985 sample are omitted, previous results are reversed. Our explanation is based on the existence of simultaneous shifts in the time series of the equilibrium stock price and dividends. This explanation relies on the concept of co-breaking [16]. The concept of co-breaking has recently been introduced by Hendry [16]. In Section 2, we define the concept of co-breaking. We introduce a present value model and show how this type of models implies co-breaking. In Section 3, we propose a strategy for modelling co-breaking vectors with a Markov switching autoregressive model and implement this strategy with the Campbell and Shiller dataset [2]. Section 4 analyzes the forecasting implications of deterministic shifts and how the forecast can be improved by modelling the common shifts (cobreaks). Section 5 concludes.

## 2. Co-breaking in asset markets

## 2.1. The concept of co-breaking

Engle and Kozicki [7] have recently proposed the idea of common features in time series. This idea is inspired by the concept of cointegration introduced in Refs. [6,11]. Engle and Kozicki [7] show that a feature is common to a set of time series if a linear combination of them do not have the feature though each of the series individually have it. Some particular examples of this concept are the idea of common cycle introduced by Engle and Kozicki [7] and co-breaking introduced by Hendry [16]. Consider an n-dimensional vector stochastic process {x<sub>t</sub>} with $t { = } 1 , . . . . T$ with $E [ { \boldsymbol { x } } _ { t } ] = \mu _ { t } .$

Definition 1. The $n \times r$ matrix % of rank r(n>r>0) is said to be contemporaneous mean co-breaking of order r for $\{ x _ { t } \}$ if $\phi ^ { \prime } \mu _ { t } = 0$ for any $t { \in } T .$

## 2.2. Present value theory of stock prices

According to the efficient market hypothesis, stock prices incorporates the market’s best forecast of the present value of future dividends. In the basic present value theory (PVT) model of stock prices, the stock price $( Q _ { t } )$ is given by the present value of the dividends associated with the stock:

$$
Q _ {t} = \mathrm{E} _ {t} \left\{\sum_ {j = 0} ^ {\infty} R _ {t, j} ^ {- j - 1} D _ {t + j} \right\} = \sum_ {j = 0} ^ {\infty} R _ {t, j} ^ {- j - 1} \mathrm{E} _ {t} D _ {t + j},\tag{1}
$$

where $R _ { t , j } ^ { - j }$ is the discount factor for cash flows j periods ahead, and $D _ { t + j }$ are the dividends in period $t { + } j .$ The logic behind Eq. (1) is that a lower (higher) stock price provides an incentive to buy (sell) stocks, which drives prices up (down). For the sake of simplification, it is usually assumed that the discount rate is constant over different time horizons

$$
R _ {t, j} ^ {- j} = \mathrm{e} ^ {-} \int_ {0} ^ {j} r (i) \mathrm{d} i = \mathrm{e} ^ {- r _ {t} j} = R _ {t} ^ {- j},\tag{2}
$$

where $r _ { t } = \mathrm { l n } R _ { t } = \mathrm { l n } ( 1 + i _ { t } )$ is the log of the risk-free rate. Thus, no risk-adjustment to the discount rate is made, and we assume risk-neutral investors. The stock price is postulated to depend on expected fundamentals. If we further assume that dividends are expected to grow with rate $\mu ^ { * }$ , we get the seminal model [10].

$$
Q _ {t} = \frac {D _ {t}}{i _ {t} - \mu^ {*}}.\tag{3}
$$

In contrast to the original deterministic approach, we propose a joint stochastic model of stock valuation and dividends growth subject to shifts in regime. We show that shifts in the mean growth of dividends imply contemporaneous shifts in the equilibrium mean of relative stock prices (co-breaking).

## 2.3. A simple model

Let us consider, as an example to the analysis above, the random-walk model of dividends subject to shifts in the mean-growth parameter $\mu _ { t }$

$$
\Delta d _ {t} = \mu_ {t} + u _ {t},\tag{4}
$$

where $u _ { t }$ is a martingale difference sequence (MDS) and the mean $\mu _ { t } = \mathrm E _ { t } [ \Delta d _ { t } ] = \mathrm E _ { t } [ \ln ( D _ { t } ) / ( D _ { t - 1 } ) ]$ is time varying. For our purpose here, assume that $\mu _ { t }$ is deterministic and, hence, perfectly predictable. Suppose that the mean growth rate of the dividends is equal to $\mu _ { t + j } = \mu ^ { \mathrm { e } }$ for all $j \geq 0$ , we then get the following representation in levels:

$$
d _ {t + h} = d _ {t} + h \mu^ {\mathrm{e}} + \sum_ {i = 1} ^ {h} u _ {t + i},
$$

which leads to the following stock price evaluation

$$
\begin{array}{l} Q _ {t} = \mathrm{E} _ {t} \left[ R _ {t} ^ {- 1} \sum_ {h = 0} ^ {\infty} \mathrm{e} ^ {- (r _ {t} - \mu^ {\mathrm{e}}) ^ {h}} \exp \left\{d _ {t} + \sum_ {i = 1} ^ {h} u _ {t + i} \right\} \right] \\ = D _ {t} \left\{R _ {t} ^ {- 1} \sum_ {h = 0} ^ {\infty} \mathrm{e} ^ {- (r _ {t} - \mu^ {\mathrm{e}}) ^ {h}} \mathrm{E} _ {t} \left[ \exp \left(\sum_ {i = 1} ^ {h} u _ {t + i}\right) \right] \right\}. \end{array}
$$

Under the normality of $u _ { t } ,$ we have

$$
\begin{array}{c} \mathrm{E} _ {t} \left[ \exp \left(\sum_ {i = 1} ^ {h} u _ {t + i}\right) \right] = \exp \left\{\frac {1}{2} \operatorname{Var} _ {t} \left(\sum_ {i = 1} ^ {h} u _ {t + i}\right) \right\} \\ = \exp \left\{\frac {1}{2} \sigma_ {u} ^ {2} h \right\}. \end{array}
$$

For $r _ { t } > \mu ^ { \mathrm { e } } + 1 / 2 \sigma _ { u } ^ { 2 } ,$ we define $\tilde { R } ^ { - 1 } = \mathrm { e } ^ { - ( r _ { t } - \mu ^ { \mathrm { e } } - 1 / 2 \sigma _ { u } ^ { 2 } ) } =$ $( 1 + i _ { t } ) ^ { - 1 } ( 1 + \mu ^ { * } )$ , where $\mu ^ { * } = 1 - \exp \{ \mu ^ { \mathrm { e } } + 1 / 2 \sigma _ { u } ^ { 2 } \}$ is the mean growth rate of $D _ { t }$ . Thus, we get

$$
Q _ {t} = R ^ {- 1} \sum_ {h = 0} ^ {\infty} \tilde {R} ^ {- h} D _ {t} = R ^ {- 1} (1 - \tilde {R} ^ {- 1}) ^ {- 1} D _ {t}.\tag{5}
$$

First, note that Eq. (5) is identical to the deterministic Gordon model

$$
Q _ {t} = \frac {D _ {t}}{i _ {t} - \mu^ {*}}
$$

Taking logs of Eq. (5) reveals that the PVT requires co-breaking in a non-linear fashion:

$$
q _ {t} = d _ {t} - \ln (1 - \mathrm{e} ^ {- (r _ {t} - \mu^ {\mathrm{e}} - \frac {1}{2} \sigma_ {u} ^ {2})}).\tag{6}
$$

Now, consider the log-linear approximation of $q _ { t } - d _ { t } = \psi ( r _ { t } , \mu ^ { \mathrm { e } } , \sigma _ { u } ^ { 2 } )$ in Eq. (5), which is $q _ { t } - d _ { t } = \psi$ $( r _ { t } , \mu ^ { \mathrm { { e } } } , \sigma _ { u } ^ { 2 } ) + \psi _ { 1 } r _ { t } + \psi _ { 2 } \mu ^ { \mathrm { { e } } } + \psi _ { 3 } \sigma _ { u } ^ { 2 } .$ It can be shown that $\psi _ { 1 } \mathrm { = - } ( \overbrace { 1 } - \mathrm { e } ^ { - \mathrm { e } ^ { - \mathrm { e } ^ { - \mathrm { e } ^ { - \mathrm { e } ^ { - \mathrm { \Lambda } } } } \left( r _ { t } - \mathrm { \Lambda } ^ { \ast } - 1 / 2 \sigma _ { u } ^ { 2 } \right) } } ) ^ { - 1 } \mathrm { e } ^  - \mathrm { e } ^ { - \mathrm { e } ^ { \mathrm { e } ^ { - \mathrm { \Lambda } } - 1 / 2 \sigma _ { u } ^ { 2 } } } \mathrm { = - \Gamma } \left( Q / \mathrm { e } ^ { \mathrm { e } ^ { \mathrm { e } ^ { - \mathrm { e } ^ { - \mathrm { \Lambda } } - 1 / 2 \sigma _ { u } ^ { 2 } } } \right) } \mathrm { = - \Gamma } \left( Q / \mathrm { e } ^  \mathrm { e } ^  \mathrm { e } ^ { - \mathrm { e } ^ { - \mathrm { e } ^ { - \mathrm { \Lambda } } - 1 / 2 \sigma _ { u } ^ { 2 } } } \mathrm { = - \Gamma } \left( r _ { t } - \mathrm { e } ^ { \mathrm { e } ^ { - \mathrm { e } ^ { - \mathrm { e } ^ { - \mathrm { \Lambda } } - 1 / 2 \sigma _ { u } ^ { 2 } } } \right) } \right) .$ $D ) ( 1 - D / Q ) = - \left( Q / D - 1 \right) = - \left( e ^ { \psi _ { 0 } } - 1 \right)$ , where $\psi _ { 0 } =$ $D _ { 0 } / Q _ { 0 }$ and $\psi _ { 2 } { = } \psi _ { 3 } { = } - \psi _ { 1 } ,$ and we thus have:

$$
q _ {t} - d _ {t} \simeq \psi_ {0} + \left(\mathrm{e} ^ {\psi_ {0}} - 1\right) \left\{- r _ {t} + \mu^ {\mathrm{e}} + \frac {1}{2} \sigma_ {u} ^ {2} \right\}.\tag{7}
$$

We get a linear relationship between the price-perdividends, the free-risk interest rate, and the expected dividends growth.

## 2.4. The general model

2.4.1. The stochastic process determining dividends growth

Consider an $\operatorname { A R } ( 1 )$ model of dividends subject to shifts in the mean,

$$
\Delta d _ {t} = \mu_ {t} + \alpha (\Delta d _ {t - 1} - \mu_ {t - 1}) + u _ {t},\tag{8}
$$

where $u _ { t }$ is an MDS and the mean $\mu _ { t } { = } \mathrm { E } _ { t } [ \Delta d _ { t } ] =$ $\mathrm { E } _ { t } [ \ln ( D _ { t } ) / ( D _ { t - 1 } ) ]$ is time varying. For our purpose here, assume that $\mu _ { t }$ is deterministic and, hence, perfectly predictable. Given Eq. (8), the dividend expectations are based on the moving-average representation

$$
\Delta d _ {t + h} = \mu_ {t + h} + \alpha^ {h} (\Delta d _ {t} - \mu_ {t}) + \sum_ {i = 1} ^ {h} \alpha^ {h - i} u _ {t + i}.\tag{9}
$$

Suppose that the mean growth rate of the dividends is equal to $\mu _ { t + j } = \mu ^ { \mathrm { e } }$ for all $j \geq 0$ , we get the following representation in levels:

$$
\begin{array}{l} d _ {t + h} = d _ {t} + \mu^ {\mathrm{e}} h + \left(\sum_ {i = 1} ^ {h} \alpha^ {i}\right) (\Delta d _ {t} - \mu^ {\mathrm{e}}) \\ \qquad + \left(\sum_ {j = 1} ^ {h} \sum_ {i = 1} ^ {j} \alpha^ {h - i}\right) u _ {t + i}. \end{array}\tag{10}
$$

Then the expectation of $d _ { t + h }$ conditional on the information set at time t is given by

$$
\begin{array}{l} d _ {t + h \cdot t} = \mathrm{E} _ {t} d _ {t + h} = d _ {t} + \mu^ {\mathrm{e}} h + \frac {\alpha (1 - \alpha^ {h})}{1 - \alpha} \\ \times (d _ {t} - d _ {t - 1} - \mu_ {t - 1}), \end{array}\tag{11}
$$

where we used $\textstyle \sum _ { i = 1 } ^ { h } \alpha ^ { i } = [ \alpha / ( 1 - \alpha ) ] ( 1 - \alpha ^ { h } )$

In the following, we show how shifts in the mean growth of dividends are translated into stock price changes due to the reevaluation of stocks.

## 2.4.2. Stock price process

Inserting Eq. (10) into Eq. (1) gives for $R _ { t } { > } M { = } \mathsf { e } ^ { \mu ^ { \mathrm { e } } }$

$$
\begin{array}{l} Q _ {t} = \mathrm{E} _ {t} \left[ R _ {t} ^ {- 1} \sum_ {h = 0} ^ {\infty} \tilde {R} _ {t} ^ {- h} \exp \left\{d _ {t} + \left(\sum_ {i = 1} ^ {h} \alpha^ {i}\right) \left(\Delta d _ {t} - \mu_ {t - 1}\right) \right. \right. \\ \left. + \left(\sum_ {j = 1} ^ {h} \sum_ {i = 1} ^ {j} \alpha^ {h - i} u _ {t + i}\right) \right\} \\ = D _ {t} \left\{R _ {t} ^ {- 1} \sum_ {h = 0} ^ {\infty} \tilde {R} _ {t} ^ {- h} \tilde {M} _ {t} ^ {[ \alpha / (1 - \alpha) ] (1 - \alpha^ {h})} \mathrm{E} _ {t} \right. \\ \times \left[ \exp \left(\sum_ {j = 1} ^ {h} \sum_ {i = 1} ^ {j} \alpha^ {h - i} u _ {t + i}\right) \right] \Bigg \} \end{array} \tag {12}
$$

where,

$$
\tilde {R} _ {t} ^ {- 1} = R _ {t} ^ {- 1} M,
$$

$$
\begin{array}{l} \tilde {M} _ {t} = \left(\frac {D _ {t}}{M _ {t - 1} D _ {t - 1}}\right), \\ \text { and } \end{array}
$$

$$
\sum_ {h = 0} ^ {\infty} R _ {t} ^ {- h} M ^ {h} = \left(1 - R _ {t} ^ {- 1} M\right) ^ {- 1}.
$$

Under normality of $u _ { t } ,$ we have

$$
\begin{array}{l} \mathrm{E} _ {t} \left[ \exp \left(\sum_ {j = 1} ^ {h} \sum_ {i = 1} ^ {j} \alpha^ {h - i} u _ {t + i}\right) \right] \\ = \exp \left\{\frac {1}{2} \operatorname{Var} _ {t} \left(\sum_ {j = 1} ^ {h} \sum_ {i = 1} ^ {j} \alpha^ {h - i} u _ {t + i}\right) \right\} = \omega_ {h} (\alpha , \sigma_ {u} ^ {2}). \end{array}
$$

and we can then obtain,

$$
Q _ {t} = R _ {t} ^ {- 1} D _ {t}
$$

$$
\times \left\{\sum_ {h = 0} ^ {\infty} \mathrm{e} ^ {- (r _ {t} - \mu^ {\mathrm{e}}) h + \frac {1}{2} \omega_ {h} (\alpha , \sigma_ {u} ^ {2}) + [ \alpha / (1 - \alpha) ] (1 - \alpha^ {h}) (\Delta d _ {t} - \mu)} \right\}\tag{13}
$$

$$
\begin{array}{l} Q _ {t} = R _ {t} ^ {- 1} D _ {t} \mathrm{e} ^ {[ \alpha / (1 - \alpha) ] (\Delta d _ {t - \mu})} \\ \times \left\{\sum_ {h = 0} ^ {\infty} \mathrm{e} ^ {- (r _ {t} - \mu^ {\mathrm{e}}) h + \frac {1}{2} \omega_ {h} (\alpha , \sigma_ {u} ^ {2}) - [ \alpha / (1 - \alpha) ] \alpha^ {h} (\Delta d _ {t} - \mu)} \right\}. \end{array}\tag{14}
$$

Taking logs in the above expression, we get to

$$
\begin{array}{l} q _ {t} = d _ {t} + \frac {\alpha}{(1 - \alpha)} (\Delta d _ {t} - \mu) \\ \quad + \ln \left[ \sum_ {h = 0} ^ {\infty} \mathrm{e} ^ {- r _ {t} h + \mu^ {\mathrm{c}} h + \frac {1}{2} \omega_ {h} (\alpha , \sigma_ {u} ^ {2}) - [ \alpha / (1 - \alpha) ] \alpha^ {h} (\Delta d _ {t} - \mu)} \right], \end{array}\tag{15}
$$

which reveals that the PVT requires co-breaking.

$$
q _ {t} \simeq d _ {t} - r _ {t} + \mu^ {\mathrm{e}} + \kappa (\Delta d _ {t} - \mu^ {\mathrm{e}}),\tag{16}
$$

where j depends on a. Thus, we get a linear relationship between the interest rate adjusted price-per-dividends and the expected dividend growth:

$$
(q _ {t} - d _ {t} - r) \simeq (1 - \kappa) \mu^ {\mathrm{e}} + \kappa \Delta d _ {t}.
$$

Note that this approach is quite general and not restricted to stocks. Bond prices (term structure models) and house prices are other examples that might be interesting to look at. The model could also be extended for observed variables that are leading indicators for dividends.

## 3. Modelling co-breaking with the MS-VAR

## 3.1. The co-breaking VAR

The log-linear correspondent to our model is given by

$$
\Delta d _ {t} = \mu_ {t} ^ {\mathrm{e}} + \alpha (\Delta d _ {t - 1} - \mu_ {t - 1} ^ {\mathrm{e}}) + u _ {t}\tag{17}
$$

$$
z _ {t} = (1 - \kappa) \mu_ {t} ^ {\mathrm{e}} + \kappa \Delta d _ {t} + \varepsilon_ {t}\tag{18}
$$

where $z _ { t } = q _ { t } - d _ { t } - \ln i _ { t } = \log ( i _ { t } \mathcal { Q } _ { t } ) / ( D _ { t } )$ is the log of the ratio of price-per-dividends and the free-risk interest rate measuring the under or overvaluation of stocks in terms of the observables. Note that $u _ { t } \sim \mathrm { N I D } ( 0 , \sigma _ { u } ^ { 2 } )$ denotes the innovation to (expected) dividends growth, and $\varepsilon _ { t } \sim \mathrm { N I D } ( 0 , \sigma _ { \varepsilon } ^ { 2 } )$ represents the under- or overvaluation of stocks, such that $\mathrm { E } _ { t - 1 } ( q _ { t } - p \nu _ { t } ) { = } 0$ . Eqs. (17) and (18) can be considered as the structural form

$$
\left[ \begin{array}{c} \Delta d _ {t} \\ z _ {t} \end{array} \right] = \left[ \begin{array}{c} 1 \\ 1 \end{array} \right] \mu_ {t} ^ {\mathrm{e}} + \left[ \begin{array}{c} \alpha \\ \alpha \kappa \end{array} \right] (\Delta d _ {t - 1} - \mu_ {t - 1} ^ {\mathrm{e}})) + \left[ \begin{array}{c c} 1 & 0 \\ \kappa & 1 \end{array} \right] \left[ \begin{array}{c} u _ {t} \\ \varepsilon_ {t} \end{array} \right]\tag{19}
$$

of a Markov switching in mean vector autoregression of order 1(MSM-VAR(1)):<sup>1</sup>

$$
\boldsymbol {x} _ {t} = \mu (s _ {t}) + A (\boldsymbol {x} _ {t} - \mu (s _ {t - 1})) + \omega_ {t}\tag{20}
$$

where:

$$
\boldsymbol {x} _ {t} = \left[ \begin{array}{c} \Delta d _ {t} \\ z _ {t} \end{array} \right],
$$

$$
\mu (s _ {t}) = \left[ \begin{array}{c} \mu_ {s _ {t}} ^ {\mathrm{e}} \\ \mu_ {s _ {t}} ^ {\mathrm{e}} \end{array} \right],
$$

$$
A = \left[ \begin{array}{c c} \alpha & 0 \\ \alpha \kappa & 0 \end{array} \right],
$$

and

$$
w _ {t} = \left[ \begin{array}{c} u _ {t} \\ \varepsilon_ {t} + \kappa u _ {t} \end{array} \right] \text {   is   NID   } \left(0, \left[ \begin{array}{c c} \sigma_ {u} ^ {2} & \kappa \sigma_ {u} ^ {2} \\ \kappa \sigma_ {u} ^ {2} & \sigma_ {\varepsilon} ^ {2} + \kappa^ {2} \sigma_ {u} ^ {2} \end{array} \right]\right).
$$

3.2. Modelling stock pricing and dividend growth with the MS-VAR

So far, we have assumed that PVT describes stock prices perfectly. We now allow for temporary deviation from PVT. As our statistical model, we could consider a three-regime Markov-switching vector autoregression with changing intercept and regime-dependent covariances of order one (MSIH(3) –VAR(1)):

$$
y _ {t} = v (s _ {t}) + A _ {1} y _ {t - 1} + u _ {t}, \quad u _ {t} \mid s _ {t} \sim \mathrm{NID} (0, \Sigma (s _ {t})),
$$

where $y _ { t } { = } ( z _ { t } , \Delta d _ { t } ) ^ { \prime }$

The stationarity of the system was confirmed by Johansen’s cointegration tests (see Ref. [17]). Three vectors, $\nu _ { 1 } , \nu _ { 2 } , \nu _ { 3 } ,$ , of regime-conditional means of $y _ { t }$ are distinguished. The general idea behind this class of regime-switching models is that the parameters of a VAR depend upon a stochastic, unobservable regime variable $s _ { t } { \in } \{ 1 , . . . . , M \}$ . The stochastic process for generating the unobservable regimes is an ergodic Markov chain defined by the transition probabilities:

$$
\begin{array}{l} p _ {i j} = \operatorname * {P r} (s _ {t + 1} = j \mid s _ {t} = i), \quad \sum_ {j = 1} ^ {M} p _ {i j} = 1 \\ \forall i, j \in \{1, \ldots , M \}. \end{array}\tag{21}
$$

By inferring in the probabilities of the unobserved regimes conditional on an available information set, it is then possible to reconstruct the regimes.<sup>2,3</sup>

The maximum likelihood (ML) estimates of the MSIH(3)–VAR(1) for the period 1873–1995 are given in Table 1. There is evidence for an overreaction of markets: for a given regime, overvaluation of stocks is corrected by partial adjustment of stock prices and not by higher dividends in the future. This can be seen in the magnitude of the coefficients of $( q - d - i ) _ { t - 1 }$ in the first and second equations. The response of $\Delta d _ { t }$ is small and hardly significant. The lower part of Table 1 includes different measures of goodness-of-fit of the non-linear model, and these are compared with the same measures for the linear model (a vector autoregression of order one). These measures include the log-likelihood value of the model, the Akaike Information Criterion (AIC), the Hannan–Quinn Criterion (HQ) and the Schwarz Criterion (SC). They all seem to favour the non-linear model.<sup>4</sup> In the right hand side of Table 1, we report the measures of persistence for each of the regimes: the expected number of years that prevails (duration) in each regime and the unconditional (ergodic) probability of each of the regimes.

The dating of the regime shifts is visualized in Fig. 1 which gives the filtered, smoothed, and predicted probabilities of being in Regime 1, 2 or $3 . ^ { 5 }$ The filtered probabilities are depicted with a continuous thin line, the filtered probabilities are printed with a dashed continuous line, and the smoothed probabilities are given by the thick-dotted line. The regime probabilities indicate the presence of structural breaks: Regime 2 is associated with the period lasting from 1873 to 1923. Regime 1 is effective from 1929 to 1951, showing negative dividend growth and low pricing of stocks. The post-World War II period (since 1952) is captured by Regime 3, which is consistent with the ‘‘Golden Twenties’’ (1924–1929): strong dividend growth is associated with high stock prices. The effects of the regime shifts on the two variables are depicted in Fig. 2. The continuous and dashed lines plot the original modeled variable and its fitted value, respectively. The upper panel contains the plot for the equilibrium stock price and the lower panel contains the plot for the dividend growth. Fig. 2 shows also the good fit of our model, which confirms the values recorded in the lower part of Table 1. Major changes to the mean growth rate and the volatility of the data (see Fig. 3) are evident. Changes in the correlation structure can also be observed. While in the pre-WWI period (Regime 2), the errors in the dividend and the stock price equation are uncorrelated, we found a negative contemporaneously correlation in regime 1, i.e. $\Delta d \uparrow \Rightarrow \Delta q < \Delta d ,$ and a positive contemporaneous correlation in the post-WWII Regime 3: $\Delta d \uparrow \Rightarrow \Delta q > \Delta d .$

We found that this model gives a good statistical representation of the data and all coefficients are significant. Fig. 3 plots the smoothed, predicted, and standard residuals of our fitted model, and offers a graphical evidence on the good fit of the model. Due to the existence of a nuisance parameter under the null hypothesis, the likelihood ratio test statistic for testing the number of regimes does not posses an asymptotic $\chi ^ { 2 }$ distribution. However, the presence of regime shifts confirmed unanimously by the information criteria and the likelihood ratio test statistic $\mathrm { L R } = 1 1 7 . 4 5$ for 10 restricted parameters and nuisance parameters suggests a rejection of linearity if we based our inference on $\bar { \chi } ^ { 2 } ( 1 6 )$ as a good approximation to Ref. [15] and the upper bound of Ref. [3].

Our findings are in line with the theoretical model developed in Section 3: Under the presence of breaks in the mean of the stochastic process of dividends growth, the equilibrium price of assets changes as well. Stock prices reflect high mean growth: a high mean growth of dividends corresponds with a high stock valuation (‘‘glamour stock markets’’).

Table 1  
Estimation results for the MSIH(3) – VAR(1) model, 1873 (1) – 1995 (1)

<table><tr><td></td><td> $(q-d-i)_t$ </td><td> $\Delta d_t$ </td><td colspan="4">Transition probabilities</td></tr><tr><td colspan="3">Regime-dependent intercepts</td><td colspan="2"> $p_{1i}$ </td><td> $p_{2i}$ </td><td> $p_{3i}$ </td></tr><tr><td rowspan="2">Regime 1</td><td>-0.474</td><td>-0.048</td><td>Regime 1</td><td>0.918</td><td> $1.274 \times 10^{-5}$ </td><td>0.022</td></tr><tr><td>0.096</td><td>0.069</td><td>Regime 2</td><td>0.082</td><td>0.967</td><td> $1.954 \times 10^{-5}$ </td></tr><tr><td rowspan="2">Regime 2</td><td>-0.054</td><td>0.008</td><td>Regime 3</td><td> $4.779 \times 10^{-6}$ </td><td>0.033</td><td>0.978</td></tr><tr><td>0.039</td><td>0.017</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="3">Regime 3</td><td>0.092</td><td>0.038</td><td colspan="4">Persistence of Regimes</td></tr><tr><td>0.046</td><td>0.007</td><td></td><td>Ergodic prob.</td><td>Duration</td><td> $n_{Obs}$ </td></tr><tr><td></td><td></td><td>Regime 1</td><td>0.138</td><td>12.2</td><td>13.6</td></tr><tr><td colspan="3">Autoregressive parameters</td><td>Regime 2</td><td>0.339</td><td>30.0</td><td>60.2</td></tr><tr><td rowspan="2"> $(q-d-i)_{t-1}$ </td><td>0.801</td><td>-0.017</td><td>Regime 3</td><td>0.523</td><td>46.4</td><td>49.1</td></tr><tr><td>0.049</td><td>0.008</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2"> $\Delta d_{t-1}$ </td><td>0.226</td><td>0.430</td><td></td><td></td><td></td><td></td></tr><tr><td>0.205</td><td>0.084</td><td></td><td></td><td></td><td></td></tr><tr><td colspan="7">Variance-covariances  $(\times 10^{-2})$ </td></tr><tr><td rowspan="2">Regime 1</td><td>6.961</td><td>-3.082</td><td></td><td></td><td></td><td></td></tr><tr><td>-0.476</td><td>6.022</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2">Regime 2</td><td>8.135</td><td>-0.007</td><td></td><td></td><td></td><td></td></tr><tr><td>-0.002</td><td>1.656</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2">Regime 3</td><td>7.952</td><td>0.303</td><td></td><td></td><td></td><td></td></tr><tr><td>0.346</td><td>0.096</td><td></td><td></td><td></td><td></td></tr><tr><td>Fitting</td><td>MS-VAR</td><td>Linear VAR</td><td></td><td></td><td></td><td></td></tr><tr><td>LogLik</td><td>112.35</td><td>53.63</td><td></td><td></td><td></td><td></td></tr><tr><td>AIC</td><td>-1.42</td><td>-0.73</td><td></td><td></td><td></td><td></td></tr><tr><td>HQ</td><td>-1.19</td><td>-0.64</td><td></td><td></td><td></td><td></td></tr><tr><td>SC</td><td>-0.85</td><td>-0.52</td><td></td><td></td><td></td><td></td></tr></table>

## 4. Implications for forecasting multiperiod returns using the MS-VAR

One of the most striking results on asset pricing in the last 20 years is the better forecastability of longhorizon returns over one-step return forecast. This could seem a paradox, given that the further our forecast horizon the greater the uncertainty we are bound to face.

To assess the contribution of the MS-VAR model in order to solve this puzzle, we examine the outcome of in-sample forecast experiments with the VARs associated with Regime 2 (pre-WWI) and Regime 3 (post-WWII), and compare it to a linear time-invariant VAR over the full sample. The estimates of the linear time-invariant vector autoregression over the full sample are given in Table 2. While an attractive feature of MS-VAR models is the ease with which forecasts can be obtained [19], the structural-break character of our model makes an out-of-sample forecast experiment with the dataset complicated until 1923, where only one regime can be observed.

This does not allow operators to judge the out-ofsample forecasting abilities of the models, but allows them to understand the importance of structural breaks in the intercept for forecasting dividends and relative stock prices. The forecast exercise is implemented to resolve the forecast paradox. We propose an alternative explanation of this ‘‘forecast paradox ’’ that considers the relationship between structural shifts and multiperiod forecasting and how modelling cobreaking resolves the ‘‘forecast paradox.’’

We will measure the forecast performance with the mean squared prediction error criterion, such that for a given information set $X _ { t } ,$ the optimal predictor is given by the conditional mean $\hat { x _ { t + h | t } } { = } \mathrm { E } [ x _ { t + h } | X _ { t } ]$ . For the $\mathrm { M S } ( M ) { \mathrm { - V A R } } ( p )$ model, the conditional expectation involved by the optimal predictor, ${ \hat { x } } _ { T ^ { + } h | T _ { 3 } }$ is given by

![](/api/attachments/PE4K287F/fulltext/images/ad9df12c01fb699ca53f64edd56d2f8c03bedb93a6fd4cfe1e881533cbcf1fc5.jpg)  
Fig. 1. Regime probabilities.

$$
\mathrm{E} \left[ x _ {T + h} \mid X _ {T} \right] = \sum_ {s _ {T + h = 1}} ^ {M} \mathrm{E} \left[ x _ {T + h} \mid X _ {T}, s _ {T + h} \right] \operatorname * {P r} \left(s _ {T + h} \mid X _ {t}\right),\tag{22}
$$

where $X _ { T }$ is the full-sample information and the predicted regime probabilities,

$$
\begin{array}{l} \operatorname * {P r} (s _ {T + h} = j \mid X _ {T}) \\ = \sum_ {i = 1} ^ {M} \operatorname * {P r} (s _ {T + h} = j | s _ {T} = i) \operatorname * {P r} (s _ {T} = i \mid X _ {T}), \end{array}
$$

only depend on the transition probabilities, $\operatorname* { P r } ( s _ { t } =$ $j | s _ { t - 1 } = i ) = p _ { i j } , \ i , j = 1 , . \ . \ . ,$ , M and the filtered regime probability $\mathrm { P r } ( s _ { T } = i | X _ { T } )$

The optimal predictor of the MS–AR model is linear in the last $p$ observations and the last regime inference, but there exists no purely linear representation of the optimal predictor in the information set.

Note, however, that the optimal forecasting rule becomes linear in the limit as the regimes become completely unpredictable, defined by $\operatorname* { P r } ( s _ { t + 1 } | s _ { t } ) =$ $\mathrm { P r } ( s _ { t + 1 } )$ , or if the regimes are absorbing states, $\mathrm { P r } ( s _ { t + 1 } | s _ { t } ) = \mathrm { P r } ( s _ { t } )$ . In the latter case, we have $\hat { \nu } _ { T + h } = \nu _ { T }$ for all $h \geq 0 .$ . As ${ \tilde { p } } _ { 2 2 } = 0 . 9 6 7$ and ${ \tilde { p } } _ { 3 3 } = 0 . 9 7 8$ , forecasts based on the recent regime-dependent VAR are good approximations to the optimal predictor.

We define as the multiperiod-return forecast

$$
\hat {R} _ {T + h \cdot T} = \frac {1}{h} (\hat {x} _ {T + h} - x _ {T}) = \frac {1}{h} \sum_ {i = 1} ^ {h} \Delta \hat {x} _ {T + i}\tag{23}
$$

and as the multiperiod-return forecast error

$$
\begin{array}{c} R _ {T + h \cdot T} - \hat {R} _ {T + h \cdot T} = \frac {1}{h} (\hat {x} _ {T + h} - x _ {T + h}) \\ = \frac {1}{h} \sum_ {i = 1} ^ {h} (\Delta \hat {x} _ {T + i} - \Delta x _ {T + i}). \end{array}\tag{24}
$$

Fig. 4 gives the multiperiod-return forecast errors for stock prices. We have plotted the multiperiod-

![](/api/attachments/PE4K287F/fulltext/images/ed5aef83c9900adec581da2136d68a905f6236ac69d29a8bdfe439efa1a04670.jpg)  
Fig. 2. Actual and fitted values.

return forecast errors one period ahead and four periods ahead. The top panel shows the forecast errors obtained using the linear time-invariant VAR, the middle panel shows the forecast error obtained using the parameter estimates associated with Regime 2 (pre-WWI) and the lower panel plots the error forecasts calculated with the parameters estimates associated with Regime 3 (post-WWII). As one can see from the top panel, the one-step ahead forecast errors are greater that the four-step ahead forecast errors for a wide set of the sample size. The middle panel shows that for the periods when Regime 2 was active (see middle panel of Fig. 1), the one-step ahead forecast errors are always lower that the fourstep ahead forecast errors. Last, the lower panel shows that when Regime 3 prevailed (see lower panel of Fig. 1), the one-step ahead forecast errors are always lower that the four-step ahead forecast errors. This evidence shows how the forecasting paradox that we documented earlier can be solved by using a model that takes into account the shift in the process of the equilibrium stock prices and the dividend growth.

An analytical proof of the above result goes as follows. Consider again the AR(1) model:

$$
\Delta x _ {t} = \mu_ {t} + \alpha (\Delta x _ {t - 1} - \mu_ {t - 1}) + u _ {t},\tag{25}
$$

exhibiting the moving-average representation

$$
\Delta x _ {t + h} = \mu_ {t + h} + \alpha^ {h} (\Delta x _ {t} - \mu_ {t}) + \sum_ {i = 1} ^ {h} \alpha^ {h - i} u _ {t + i}.\tag{26}
$$

Thus, the optimal predictor is given by

$$
\Delta \hat {x} _ {t + h \cdot t} = \hat {\mu} _ {t + h \cdot t} + \alpha^ {h} (\Delta x _ {t} - \mu_ {t})\tag{27}
$$

and the h-step prediction error is

$$
\Delta x _ {t + h} - \Delta \hat {x} _ {t + h \cdot t} = (\mu_ {t + h} - \hat {\mu} _ {t + h \cdot t}) + \sum_ {i = 1} ^ {h} \alpha^ {h - i} u _ {t + i}.\tag{28}
$$

Table 2  
![](/api/attachments/PE4K287F/fulltext/images/485d3c59e514677bb2f67c844b3656f696a8899ae1db0e801f1204faeb2dd813.jpg)  
Dd - Errors in the MSIH(3)-VAR(1)

Lqdi - StdResids in the MSIH(3)-VAR(1)  
![](/api/attachments/PE4K287F/fulltext/images/a52c17a2e6457cdb44327754735d618d2b3cd9a607bf4d0308a4d00406cb3084.jpg)

![](/api/attachments/PE4K287F/fulltext/images/c2e58e387ef9920d1965fa992a9a9fb9668baa66a45db63a9921af69d3918bd3.jpg)

Dd - StdResids in the MSIH(3)-VAR(1)  
![](/api/attachments/PE4K287F/fulltext/images/f50be2f555e60750b4e6e226f2f13d08bffb7341e3f705592ba1e2ed8aff3203.jpg)  
Fig. 3. Smoothed, predicted, and standard residuals from our fitted model.

Assuming that consistent estimators a˜ and $\tilde { \sigma } _ { u } ^ { 2 }$ of $\alpha ,$ $\sigma _ { u } ^ { 2 }$ are available, such that for a large number of observations, $\alpha _ { u } ^ { 2 } = \alpha , \ \tilde { \sigma } _ { u } ^ { 2 } = \sigma _ { u } ^ { 2 }$ . Suppose, furthermore, that the changes to the mean are unpredictable, such that the estimator of $\mu _ { t + h }$ is given by $\hat { \mu } _ { t + h \cdot t } \overset { } { = } \hat { \mu } _ { t } =$ $\textstyle \sum _ { j = 0 } ^ { t } \Delta x _ { t - j } .$ . Then the mean square prediction error at h-step is:

Estimation results for the VAR(1) model, 1873 (1) – 1995 (1)

<table><tr><td></td><td> $(q-d-i)_t$ </td><td> $\Delta d_t$ </td></tr><tr><td colspan="3">Intercept</td></tr><tr><td></td><td>-0.025</td><td>0.022</td></tr><tr><td></td><td>0.030</td><td>0.012</td></tr><tr><td colspan="3">Autoregressive parameters</td></tr><tr><td> $(q-d-i)_{t-1}$ </td><td>0.930</td><td>-0.006</td></tr><tr><td></td><td>0.034</td><td>0.014</td></tr><tr><td> $\Delta d_{t-1}$ </td><td>0.493</td><td>0.248</td></tr><tr><td></td><td>0.220</td><td>0.088</td></tr><tr><td colspan="3">Variance-covariances ( $\times 10^{-2}$ )</td></tr><tr><td> $(q-d-i)_t$ </td><td>9.684</td><td>0.189</td></tr><tr><td> $\Delta d_t$ </td><td>0.048</td><td>1.559</td></tr></table>

$$
\begin{array}{l} \mathrm{E} _ {t} [ \Delta x _ {t + h} - \Delta \hat {x} _ {t + h \cdot t} ] = \mathrm{E} _ {t} [ (\mu_ {t + h} - \hat {\mu} _ {t}) ^ {2} ] \\ \qquad + \mathrm{E} _ {t} \left[ \left(\sum_ {i = 1} ^ {h} \alpha^ {h - i} u _ {t + i}\right) ^ {2} \right] \\ \qquad = \mathrm{E} _ {t} [ (\mu_ {t + h} - \hat {\mu} _ {t}) ^ {2} ] \\ \qquad + \frac {\alpha^ {2} (1 - \alpha^ {2 h})}{1 - \alpha^ {2}} \sigma_ {u} ^ {2} \end{array}\tag{29}
$$

ð30Þ

The multiperiod forecast error $R _ { t + h \cdot t } - \hat { R } _ { t + h t } = 1 /$ $h \textstyle \sum _ { i = 1 } ^ { h } ( \Delta \hat { x } _ { t + i } - \Delta x _ { t + i } )$ can be expressed as:

ð31Þ

$$
\begin{array}{l}\lim _ {h \rightarrow \infty} (R _ {t + h \cdot t} - \hat {R} _ {t + h \cdot t}) = \lim _ {h \rightarrow \infty} \frac {1}{h} \sum_ {i = 1} ^ {h} (\Delta \hat {x} _ {t + i} - \Delta x _ {t + i})\\= \lim _ {h \rightarrow \infty} \frac {1}{h} \sum_ {i = 1} ^ {h} (\mu_ {t + i} - \hat {\mu} _ {t})\\+ \lim _ {h \rightarrow \infty} \frac {1}{h} \left(\sum_ {i = 1} ^ {h} \sum_ {j = 1} ^ {i} \alpha^ {i - j} u _ {t + i}\right)\end{array}\tag {3}\tag{32}
$$

![](/api/attachments/PE4K287F/fulltext/images/69a9bec0fe074da5d83faeec07c43e331974dcf57720b37a8985c746a3772d23.jpg)

![](/api/attachments/PE4K287F/fulltext/images/f46c576187a718a79268d96428e71cac10f180fc29f01c55547f358f3047dc20.jpg)

![](/api/attachments/PE4K287F/fulltext/images/ff0e8c98fc18b3fda902601faf36ccf98a1f9ee89689bb897b500f92c4e13555.jpg)  
Fig. 4. The in-sample forecasting experiment.

And one can observe from the above equation, that what matters in the long run are the unpredictable shifts of the mean growth rate

$$
\mu^ {\mathrm{e}} := \lim _ {h \rightarrow \infty} \frac {1}{h} \sum_ {i = 1} ^ {h} \mathrm{E} (\Delta x _ {t + i} \mid x _ {t}).\tag{33}
$$

## 5. Conclusion

This paper departs from a well-known puzzle in finance: ‘‘the forecast paradox.’’ An important literature in finance postulate the paradoxical result that long-horizon returns could be forecasted better than one-step returns (see Refs. [2,4,20] among others). In this paper, we have shown how this result is reversed when the specific time varying process for stocks prices and dividends are considered in a present value model for stocks. We find evidence for the United States of the time varying process for stocks prices and dividends in a dataset that goes as far as 1873. A forecasting exercise based on our estimated model solves the ‘‘forecast paradox,’’ and we are able to show that the forecasting puzzle presented in the finance literature is just and artifact induced by parameter non-constancy.

A natural extension of our approach proposed in this paper would be to model the system of stock prices, dividends, and interest rates, where the candidate for the co-integrating space would be $( q _ { t - 1 } -$ $d _ { t - 1 } - r + \mu ^ { \mathrm { e } } + \kappa ( \Delta d _ { t } - \mu ^ { \mathrm { e } } ) )$ . However, strong and persistent deviations from the equilibrium (bubbles) might not be adequately represented by linear vector error correction models (VECMs). Hence, one might allow for regime shifts in the error-correction mechanism. There may exist a regime with mean-reversion and regime with an inactive equilibrium correction mechanism, thus exhibiting bubbles and stock prices, which are just martingales:

$$
\begin{array}{r l} \Delta q _ {t} & = - \alpha (s _ {t}) (q _ {t - 1} - d _ {t - 1} - r + \mu^ {\mathrm{e}} + \kappa (\Delta d _ {t} - \mu^ {\mathrm{e}})) \\ & + \dots + u _ {t} \end{array} \tag {34}
$$

where $s _ { t }$ is the regime variable. In the system approach, one might model earning growth as an MS-AR

$$
\Delta d _ {t} = \mu (s _ {t} ^ {\mathrm{e}}) + \alpha (\Delta d _ {t - 1} - \mu (s _ {t - 1} ^ {\mathrm{e}})) + u _ {t} ^ {\mathrm{e}}.\tag{35}
$$

Furthermore, it would be interesting to compare the expected growth rate of dividends coming from MS-AR model-based forecasts for dividends (cobreaking):

$$
\hat {\mu} _ {t} = \lim _ {h \rightarrow \infty} \frac {1}{h} \sum_ {i = 1} ^ {h} \mathrm{E} (\Delta d _ {t + i} \mid d _ {t}) = \mu^ {\mathrm{e}}\tag{36}
$$

with data on market expectations as well as the implicit rate (in equilibrium)

$$
\mu_ {t} ^ {\mathrm{e}} = \ln i _ {t} - \ln \frac {D _ {t}}{Q _ {t}}.
$$

Unfortunately, it is illusionary to hope for such data for the period under consideration.

## Acknowledgements

We are grateful to David Hendry, Søren Johansen, Grayham E. Mizon, Rocco Mosconi, Natalia Fabra, and Bent Nielsen, for useful comments and discussions. Financial support from the UK Economic and Social Research Council under grant L116251015 is gratefully acknowledged by the first author. The research of the second author was supported through a European Community Marie Curie Fellowship, contract HPMF-CT-2000-00761.

## References

[1] A. Ang, G. Bekaert, Regime switches in interest rates, Working Paper, Stanford University, 1995.

[2] J.Y. Campbell, R.J. Shiller, Stock prices, earning, and expected dividends, Journal of Finance 43 (1988) 661– 676.

[3] R.B. Davies, Hypothesis testing when a nuisance parameter is present only under the alternative, Biometrika 64 (1977) 247– 254.

[4] W. DeBondt, R. Thaler, Does the stock market over react? Journal of Finance 40 (1985) 793–805.

[5] J.A. Doornik, Ox: an object-oriented matrix programming language, Technical report, www.nuff.ox.ac.uk/Users/Doornik, Oxford, 1996.

[6] R.F. Engle, C.W.J. Granger, Co-integration and error correction: representation, estimation and testing, Econometrica 55 (1987) 251–276.

[7] R.F. Engle, S. Kozicki, Testing for common features, Journal of Business Economic and Statistics 11 (1993) 369– 395.

[8] E. Fama, The cross section of expected stock returns, Journal of Finance 47 (1992) 427– 465.

[9] R. Garcia, Asymptotic null distribution of the likelihood ratio test in Markov switching models, Working Paper (1993) (Universite´ de Montre´al).

[10] M. Gordon, The Investment, Financing, and Valuation of the Corporation, Irwin, Homewood, IL, 1956.

[11] C.W.J. Granger, Developments in the study of cointegrated economic variables, Oxford Bulletin of Economics & Statistics 48 (1986) 213– 228.

[12] J.D. Hamilton, Analysis of time series subject to changes in regime, Journal of Econometrics 45 (1990) 39 – 70.

[13] J.D. Hamilton, Time Series Analysis, Princeton Univ. Press, Princeton, 1994.

[14] B.E. Hansen, The likelihood ratio test under non-standard conditions: testing the Markov switching model of GNP, Journal of Applied Econometrics 7 (1992) S61– S82.

[15] B.E. Hansen, Erratum: the likelihood ratio test under nonstandard conditions: testing the Markov switching model of GNP, Journal of Applied Econometrics 11 (1996) 195 – 199.

[16] D.F. Hendry, A theory of co-breaking, Mimeo, Nuffield College, Oxford, 1995.

[17] S. Johansen, Likelihood-Based Inference in Cointegrated Vector Autoregressive Models, Oxford Univ. Press, Oxford, 1995.

[18] M.C. Kim, C. Nelson, R. Startz, Mean reversion in stock prices? A reappraisal of the empirical evidence, Review of Economic Studies 30 (1992) 25– 46.

[19] H.-M. Krolzig, Forecasting Markov-switching vector autoregressive processes, Mimeo, Department of Economics, Oxford University, 1997.

[20] J. Poterba, L. Summers, The persistence of volatility and stock market fluctuations, American Economic Review 76 (1986) 1142– 1151.

Hans-Martin Krolzig is a research fellow at Nuffield College (Oxford). His area of expertise is time-series econometrics, with special emphasis in automatic model selection in econometrics and the study of general-to-specific model selection procedures.

Juan Toro is a senior research economist at centrA (Sevilla), and has held previous positions at the European University Institute (Florence) and at the Economics Department in Oxford. His area of expertise is time-series econometrics with special interest in Markov switching models and cointegration issues.
