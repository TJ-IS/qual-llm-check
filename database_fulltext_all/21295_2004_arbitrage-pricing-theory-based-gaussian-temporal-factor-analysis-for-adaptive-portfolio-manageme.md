---
otero_id: 21295
otero_key: "EE5TEUCA"
title: "Arbitrage pricing theory-based Gaussian temporal factor analysis for adaptive portfolio management"
authors: "Kai-Chun Chiu; Lei Xu"
year: "2004"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(03)00082-4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# Arbitrage pricing theory-based Gaussian temporal factor analysis for adaptive portfolio management

Kai-Chun Chiu\*, Lei Xu

Department of Computer Science and Engineering, The Chinese University of Hong Kong, Shatin, New Territories, Hong Kong, PR China Available online 17 July 2003

## Abstract

Ever since the inception of Markowitz’s modern portfolio theory, static portfolio optimization techniques were gradually phased out by dynamic portfolio management due to the growth of popularity in automated trading. In view of the intensive computational needs, it is common to use machine learning approaches on Sharpe ratio maximization for implementing dynamic portfolio optimization. In the literature, return-based approaches which directly used security prices or returns to control portfolio weights were often used. Inspired by the arbitrage pricing theory (APT), some other efforts concentrate on indirect modelling using hidden factors. On the other hand, with regard to the proper risk measure in the Sharpe ratio, downside risk was considered a better substitute for variance. In this paper, we investigate how the Gaussian temporal factor analysis (TFA) technique can be used for portfolio optimization. Since TFA is based on the classical APT model and has the benefit of removing rotation indeterminacy via temporal modelling, using TFA for portfolio management allows portfolio weights to be indirectly controlled by several hidden factors. Moreover, we extend the approach to some other variants tailored for investors according to their investment objectives and degree of risk tolerance.

Keywords: Temporal factor analysis; Arbitrage pricing theory; Portfolio optimization; Sharpe ratio; Downside risk; Upside volatility

## 1. Introduction

Portfolio management has evolved as a core decision-making activity for investors and practitioners in the financial market nowadays. Prior to the inception of Markowitz’s modern portfolio theory [11], theoretical research on investments has concentrated on modelling expected returns [2].

During the early stage of its development, portfolio optimization was often constrained by its static implementation. Unlike dynamic portfolio optimization by which the optimal portfolio weights were tracked over time based on updated market information, the weights determined using static optimization techniques could not adapt to market changes within the investment horizon.

Despite dynamic portfolio optimization being powerful, it turned out to be a problem that required intensive computation. Recall that the most natural technique for solving dynamic portfolio optimization problems was stochastic dynamic programming. However, this approach was often compromised by several factors such as the curse of dimensionality when too many state variables were involved [7]. In general, practical considerations such as taxes and transactions costs also increased the number of state variables in the objective function.

In fact, this problem could be better solved via some popular machine learning approaches [3,12,13, 21] which required the optimal parameters to be adaptively learned over time, and consequently, we have the term adaptive portfolio management. Among the various methodologies suggested, the most popular one is based on maximizing the well-known Sharpe ratio [17]. In implementation, trading could be based on training a trading system on labelled data [12] or directly maximizing the expected profit via the socalled adaptive supervised learning decision networks [8,21]. In this paper, these approaches were generally referred to as return-based portfolio management because they either explicitly treated the weights as constants or depend directly on the security price or returns.

Inspired by the arbitrage pricing theory (APT) in finance, which assumes that the cross-sectional expected returns of securities is linearly related to k hidden economic factors, typical statistical techniques such as principal component analysis (PCA), independent component analysis (ICA) [1,22] and maximum likelihood factor analysis [10] have been used. However, should we adopt either PCA or ICA for estimating the hidden factors, we have to compromise on the terms of zero noise. Likewise, we have to make a compromise on rotation indeterminacy if we use conventional factor analytic techniques.

In fact, many researchers also realized that variance was not appropriate for quantifying risk in the Sharpe ratio because it counted positive returns as risk. For instance, Fishburn used the lower partial moment (LPM) [5] of returns called downside risk to replace the traditional variance measure. Moreover, similar ideas were adopted for implementing portfolios optimization [8,9].

In this paper, we aim to investigate using the technique temporal factor analysis (TFA) [18] for portfolio optimization. Since TFA is based on the classical APT model and has the benefit of removing rotation indeterminacy via temporal modelling, using TFA for portfolio management allows portfolio weights to be indirectly controlled by several hidden factors. Moreover, we can extend the approach to some other variants tailored for investors according to their risk and return objectives.

The rest of the paper is organized in the following way. Sections 2 and 3 briefly review the APT and the Gaussian TFA models, respectively. Section 4 illustrates how the APT-based adaptive portfolio management can be effected with algorithms proposed in this paper. Three variants of the APT-based Sharpe ratio maximization technique are studied in Section 5. Section 6 concludes the paper.

## 2. Review on arbitrage pricing theory

The APT begins with the assumption that the $n \times 1$ vector of asset returns, $R _ { t } ,$ is generated by a linear stochastic process with k factors [14–16]:

$$
R _ {t} = \bar {R} + A f _ {t} + e _ {t}\tag{1}
$$

where $f _ { t }$ is the $k \times 1$ vector of realizations of k common factors, A is the $n \times k$ matrix of factor weights or loadings and $e _ { t }$ is an $n \times 1$ vector of asset-specific risks. It is assumed that $f _ { t }$ and $e _ { t }$ have zero expected values so that R¯ is the $n \times 1$ vector of mean returns. The model addresses how expected returns behave in a market with no arbitrage opportunities and predicts that an asset’s expected return is linearly related to the factor loadings or

$$
\bar {R} = R _ {f} + A p\tag{2}
$$

where $R _ { f }$ is an $n \times 1$ vector of constants representing the risk-free return, and $p$ is $k \times 1$ vector of risk premiums. Similar to the derivation of CAPM, Eq. (2) is based on the rationale that unsystematic risk is diversifiable and therefore should have a zero price in the market with no arbitrage opportunities.

## 3. Overview of temporal factor analysis

Suppose the relationship between a state $y _ { t } \in \mathbb { R } ^ { k }$ and an observation $x _ { t } { \in } \mathbb { R } ^ { d }$ is described by the first-order state-space equations as follows [18,19]:

$$
y _ {t} = B y _ {t - 1} + \varepsilon_ {t},\tag{3}
$$

$$
x _ {t} = A y _ {t} + e _ {t}, \quad t = 1, 2, \dots , N\tag{4}
$$

where $\varepsilon _ { t }$ and $e _ { t }$ are mutually independent zeromean white noises with $E ( \varepsilon _ { i } \varepsilon _ { j } ^ { T } ) \stackrel { \cdot \cdot } { = } \textstyle \sum _ { \varepsilon } \delta _ { i j } , \stackrel { \cdot } { E } ( e _ { i } e _ { j } ^ { T } ) = \textstyle \sum _ { e } \delta _ { i j } ,$

$E ( \varepsilon _ { i } e _ { j } ^ { T } ) = 0 , \Sigma _ { s }$ and $\Sigma _ { e }$ are diagonal matrices and $\delta _ { i j }$ is the Kronecker delta function:

$$
\delta_ {i j} = \left\{ \begin{array}{l l} 1, & \text { if   } i = j, \\ 0, & \text { otherwise } \end{array} \right..\tag{5}
$$

We call $\boldsymbol { \varepsilon } _ { t }$ the driving noise upon the fact that it drives the source process over time. Similarly, $e _ { t }$ is called measurement noise because it happens to be there during measurement. The above model is generally referred to as the TFA model.

In the context of APT analysis, Eq. (1) can be obtained from Eq. (4) by substituting $( \tilde { \mathbb { R } } _ { t } - \bar { R } )$ for $x _ { t }$ and $f _ { t }$ for $y _ { t }$ . The only difference between the $\mathrm { A P T }$ model and the TFA model is the added Eq. (3) for modelling temporal relation of each factor. The added equation represents the factor series $\scriptstyle y = \{ y _ { t } \} _ { t = 1 } ^ { T }$ in a multichannel autoregressive process, driven by an i.i.d. noise series $\left\{ \varepsilon _ { t } \right\} _ { t = 1 } ^ { \bar { T } }$ that are independent of both $y _ { t - 1 }$ and $e _ { t } .$ Specifically, it is assumed that $\mathbf { \delta } _ { \mathcal { E } _ { t } }$ is Gaussian distributed. Moreover, TFA is defined such that the $k$ sources $y _ { t } ^ { ( 1 ) } , y _ { t } ^ { ( 2 ) } , . . . , y _ { t } ^ { ( k ) }$ in this state-space model are statistically independent. The objective of TFA is to estimate the sequence of $\boldsymbol { y _ { t } } ^ { * } \mathbf { s }$ with unknown model parameters $\scriptstyle \Theta = \{ A , B , \Sigma _ { \varepsilon } , \Sigma _ { e } \}$ through available observations.

## 3.1. A learning algorithm

In implementation, an adaptive algorithm has been suggested. At each time unit, factor loadings are estimated by cross-sectional regression, and factor scores are estimated by maximum likelihood learning. Xu proposed an algorithm in Ref. [19] as shown below.

Step 1: Fix $A , B , \Sigma _ { \varepsilon }$ and $\Sigma _ { e } ,$ estimate the hidden factors $y _ { t }$ by

$$
\begin{array}{l} \hat {y} _ {t} = (\Sigma_ {\varepsilon} ^ {- 1} + A ^ {T} \Sigma_ {e} ^ {- 1} A) ^ {- 1} (A ^ {T} \Sigma_ {e} ^ {- 1} x _ {t} + \Sigma_ {\varepsilon} ^ {- 1} B \hat {y} _ {t - 1}), \\ \varepsilon_ {t} = y _ {t} - B \hat {y} _ {t - 1}, \\ e _ {t} = x _ {t} - A \hat {y} _ {t}. \end{array}
$$

Step 2: Fix $y _ { t } ,$ update A, B, $\textstyle \sum _ { \varepsilon }$ and $\Sigma _ { e }$ by the gradient ascent approach as follows:

$$
\begin{array}{l} B ^ {\text {new}} = B ^ {\text {old}} + \eta_ {0} \text {diag} [ \varepsilon_ {t} y _ {t - 1} ^ {T} ], \\ A ^ {\text {new}} = A ^ {\text {old}} + \eta_ {0} e _ {t} y _ {t} ^ {T}, \\ \Sigma_ {\varepsilon} ^ {\text {new}} = (1 - \eta) \Sigma_ {\varepsilon} ^ {\text {old}} + \eta_ {0} \text {diag} [ \varepsilon_ {t} \varepsilon_ {t} ^ {T} ], \\ \Sigma_ {e} ^ {\text {new}} = (1 - \eta) \Sigma_ {e} ^ {\text {old}} + \eta_ {0} \text {diag} [ e _ {t} e _ {t} ^ {T} ]. \end{array}
$$

where $\eta _ { 0 }$ denotes the learning rate.

## 3.2. TFA driven by ARCH( p) process

In the finance literature, effects of autoregressive conditional heteroscedasticity (ARCH) were considered in modelling unobserved components [6] as well as hidden factors [4]. In fact, the TFA model can be directly extended so as to explicitly consider the presence of ARCH effect. For example, we may just assume that each factor series has ARCH( p) effect. Mathematically, we have

$$
\begin{array}{l} \varepsilon_ {t} ^ {(j)} = v _ {t} ^ {(j)} \psi_ {t} ^ {(j)}, \quad v _ {t} ^ {(j)} \sim N (0, 1) \\ \psi_ {t} ^ {(j) ^ {2}} = a _ {0} ^ {(j) ^ {2}} + \sum_ {\tau = 1} ^ {p} a _ {\tau} ^ {(j) ^ {2}} \varepsilon_ {t - \tau} ^ {(j) ^ {2}} \end{array}
$$

To accommodate for the learning of ARCH effect, updating of $\textstyle \sum _ { \varepsilon }$ at time t can be alternatively done via updating $a _ { 0 } ^ { ( j ) }$ and $\{ a _ { \tau } ^ { ( j ) } \} _ { \tau = 1 } ^ { p }$ as shown below:

$$
\begin{array}{l} a _ {0} ^ {(j) \text {new}} = a _ {0} ^ {(j) \text {old}} + \frac {\eta a _ {0} ^ {(j)}}{a _ {0} ^ {(j) ^ {2}} + \sum_ {\tau = 1} ^ {p} a _ {\tau} ^ {(j) ^ {2}} \varepsilon_ {t - \tau} ^ {(j) ^ {2}}} \\ \times \left(\frac {\varepsilon_ {t} ^ {(j) ^ {2}}}{a _ {0} ^ {(j) ^ {2}} + \sum_ {\tau = 1} ^ {p} a _ {\tau} ^ {(j) ^ {2}} \varepsilon_ {t - \tau} ^ {(j) ^ {2}}} - 1\right) \end{array}\tag{6}
$$

$$
\begin{array}{l} a _ {\tau} ^ {(j) \text {new}} = a _ {\tau} ^ {(j) \text {old}} + \frac {\eta a _ {\tau} ^ {(j)} \varepsilon_ {t - \tau} ^ {(j) ^ {2}}}{a _ {0} ^ {(j) ^ {2}} + \sum_ {\tau = 1} ^ {p} a _ {\tau} ^ {(j) ^ {2}} \varepsilon_ {t - \tau} ^ {(j) ^ {2}}} \\ \times \left(\frac {\varepsilon_ {t} ^ {(j) ^ {2}}}{a _ {0} ^ {(j) ^ {2}} + \sum_ {\tau = 1} ^ {p} a _ {\tau} ^ {(j) ^ {2}} \varepsilon_ {t - \tau} ^ {(j) ^ {2}}} - 1\right) \end{array}\tag{7}
$$

$$
\Sigma_ {\varepsilon} = \left( \begin{array}{c c c c} \psi^ {(1) ^ {2}} & 0 & \dots & 0 \\ 0 & \psi^ {(2) ^ {2}} & \dots & 0 \\ \vdots & \ddots & \dots & 0 \\ 0 & \dots & 0 & \psi^ {(k) ^ {2}} \end{array} \right)
$$

$$
\psi^ {(j) ^ {2}} = a _ {0} ^ {(j) ^ {2}} + \sum_ {\tau = 1} ^ {p} a _ {\tau} ^ {(j) ^ {2}} \varepsilon_ {t - \tau} ^ {(j) ^ {2}}, \qquad j = 1, 2, \dots , k
$$

## 4. Gaussian TFA for adaptive portfolio management

When the APT-based Gaussian TFA model is adopted for portfolio management, portfolio weights adjustment can be made under the control of independent hidden factors that affect the portfolio. In the sequel, we illustrate how this can be achieved under the following four scenarios:

<table><tr><td></td><td>Transaction cost</td><td>Short sale permission</td></tr><tr><td>Scenario I</td><td>no</td><td>no</td></tr><tr><td>Scenario II</td><td>yes</td><td>no</td></tr><tr><td>Scenario III</td><td>no</td><td>yes</td></tr><tr><td>Scenario IV</td><td>yes</td><td>yes</td></tr></table>

4.1. Scenario I: No transaction cost and short sale not permitted

The assumptions underlying this scenario are no transaction cost and short sale not permitted. Consequently, we consider the return of a typical portfolio which is given by Ref. [19]

$$
R _ {t} = (1 - \alpha_ {t}) r ^ {f} + \alpha_ {t} \sum_ {j = 1} ^ {m} \beta_ {t} ^ {(j)} x _ {t} ^ {(j)},
$$

$$
\text { subject   to } \left\{ \begin{array}{l} \alpha_ {t} > 0, \\ 0 \leq \beta_ {t} \leq 1, \\ \sum_ {j = 1} ^ {m} \beta_ {t} ^ {(j)} = 1 \end{array} . \right.\tag{8}
$$

where $r ^ { f }$ denotes the risk-free rate of return, $x _ { t }$ denotes returns of risky securities, $\alpha _ { t }$ the proportion of total capital to be invested in risky securities and $\beta _ { t } ^ { ( j ) }$ the proportion of $\alpha _ { t }$ to be invested in the jth risky asset.

Instead of focussing on the mean variance efficient frontier, we seek to optimize the portfolio Sharpe ratio $( S _ { \mathrm { p } } )$ [8] with $S _ { \mathrm { p } } = M ( R _ { T } ) / \sqrt { V ( R _ { T } ) }$ given by Ref. [19]. In other words, the objective function to maximize is:

$$
\max _ {\psi , \phi} S _ {\mathrm{p}} = \frac {M (R _ {T})}{\sqrt {V (R _ {T})}}
$$

$$
\text { subject   to } \left\{ \begin{array}{l} \alpha_ {t} = \exp (\zeta_ {t}), \\ \zeta_ {t} = g (y _ {t}, \psi), \\ \beta_ {t} ^ {(j)} = \exp \Big (\xi_ {t} ^ {(j)} \Big) / \sum_ {r = 1} ^ {m} \exp \Big (\xi_ {t} ^ {(r)} \Big), \\ \xi_ {t} = f (y _ {t}, \phi). \end{array} \right.\tag{9}
$$

where $\begin{array} { r } { M ( R _ { T } ) = \frac { 1 } { T } \sum _ { t = 1 } ^ { T } R _ { t } } \end{array}$ is the conditional expected return and $\begin{array} { r } { V ( R _ { T } ) \stackrel { = } { = } \frac { 1 } { T } \sum _ { t = 1 } ^ { T } \left[ R _ { t } - M ( R _ { T } ) \right] ^ { 2 } } \end{array}$ is a measure of risk or volatility, $\{ y _ { t } \} _ { t = 1 } ^ { N }$ is the time series of independent hidden factors that drives the observed return series $\{ x _ { t } \} _ { t = 1 } ^ { N } , \ g ( y _ { t } , \psi )$ and $f ( y _ { t } , \phi )$ are some nonlinear functions that map $y _ { t } \mathrm { t o } ,$ , respectively, $\zeta _ { t }$ and $\xi _ { t }$ which, in turn, adjusts the portfolio weights $\alpha _ { t }$ and $\beta _ { t } ^ { ( j ) }$ , respectively.

Maximizing the portfolio Sharpe ratio in effect balances the trade-off between maximizing the expected return and at the same time minimizing the risk. In implementation, we can simply use the gradient ascent approach. The time series $\ \dot { \{ \boldsymbol y } _ { t }  \dot { \boldsymbol \xi } _ { t = 1 } ^ { N }$ can be estimated via the Gaussian TFA algorithm in Ref. [19]. Although the functions $g ( \boldsymbol { y } _ { t } , \boldsymbol { \psi } )$ and $f ( y _ { t } , \phi )$ are not known a priori, it may be approximated via the adaptive extended normalized radial basis function (ENRBF) algorithm in Ref. [20].

Like radial basis function (RBF) network, ENRBF is one of the popular models adopted for function approximation. The general form of RBF is

$$
f _ {k} (x) = \sum_ {j = 1} ^ {k} w _ {j} \varphi ([ x - \mu_ {j} ] ^ {T} \Sigma_ {j} ^ {- 1} [ x - \mu_ {j} ])\tag{10}
$$

ENRBF is an improved modification of RBF by replacing $w _ { j }$ with a linear vector function $W _ { j } ^ { T } x + c _ { j }$ and dividing the term $\varphi ( [ x - \mu _ { j } ] ^ { T } \Sigma _ { j } ^ { - 1 } [ x - \mu _ { j } ] )$ over the aggregate of all terms to arrive at

$$
f _ {k} (x) = \frac {\sum_ {j = 1} ^ {k} \left(W _ {j} ^ {T} x + c _ {j}\right) \varphi \left(\left[ x - \mu_ {j} \right] ^ {T} \Sigma_ {j} ^ {- 1} \left[ x - \mu_ {j} \right]\right)}{\sum_ {j = 1} ^ {k} \varphi \left(\left[ x - \mu_ {j} \right] ^ {T} \Sigma_ {j} ^ {- 1} \left[ x - \mu_ {j} \right]\right)}\tag{11}
$$

where $W _ { j }$ is a parameter matrix.

Basically, each $W _ { j } ^ { T } x + c _ { j }$ represents a local linear segment. The ENRBF network approximates a globally nonlinear function by joining all piecewise linear segments weighted by probability. The set of parameters to be estimated is $\scriptstyle \Theta = \{ \mu _ { j } , \sum _ { j } , \ W _ { j } , c _ { j } \} _ { j = 1 } ^ { k }$

Specifically, $g ( \boldsymbol { y } _ { t } , \boldsymbol { \psi } )$ and $f ( y _ { t } , \phi )$ can be modelled by the ENRBF shown below.

$$
g (y _ {t}, \psi) = \sum_ {p = 1} ^ {k} (W _ {p} ^ {T} y _ {t} + c _ {p}) \varphi (\mu_ {p}, \Sigma_ {p}, k)\tag{12}
$$

$$
f (y _ {t}, \phi) = \sum_ {p = 1} ^ {\hat {k}} (\hat {W} _ {p} ^ {T} y _ {t} + \hat {c} _ {p}) \varphi (\hat {\mu} _ {p}, \hat {\Sigma} _ {p}, \hat {k})\tag{13}
$$

where

$$
\varphi (\mu_ {p}, \Sigma_ {p}, k) = \frac {\exp (- 0 . 5 (y _ {t} - \mu_ {p}) ^ {T} \Sigma_ {p} ^ {- 1} (y _ {t} - \mu_ {p}))}{\sum_ {r = 1} ^ {k} \exp (- 0 . 5 (y _ {t} - \mu_ {r}) ^ {T} \Sigma_ {p} ^ {- 1} (y _ {t} - \mu_ {r}))}.
$$

The set of parameters in Eqs. (12) and (13) to be estimated is H where $\Theta = \psi \cup \phi , \psi { = } \{ \mu _ { p } , { \cal { L } } _ { p } , W _ { p } , c _ { p } \} _ { p } ^ { k } = 1$ and $\boldsymbol { \phi } { = } \{ \hat { \mu } _ { p } , \hat { \boldsymbol { { \Sigma } } } _ { p } , \hat { W } _ { p } , \hat { \mathbf { c } } _ { p } \} _ { p } ^ { \hat { \mathbf { k } } } = \mathbf { 1 } { . }$ In general, for each $\theta { \in } \Theta$ updating takes place adaptively in the following form:

$$
\theta^ {\text { new }} = \theta^ {\text { old }} + \eta_ {0} \nabla_ {\theta} S _ {\mathrm{p}}\tag{14}
$$

where $\eta _ { 0 }$ is the learning step size, $\nabla _ { \theta } S _ { \mathbf { p } }$ denotes the gradient with respect to h in the ascent direction of $S _ { \mathrm { p } } .$ . Typically, the adaptive algorithm shown in Table 1 can be adopted for implementation.

## 4.2. Simulation

## 4.2.1. Data considerations

All simulations in this paper are based on the past average fixed deposit interest rate, stock and index data of Hong Kong. Daily closing prices of the 1-week bank average interest rate, 3 major stock indices as well as 86 actively trading stocks covering the period from January 1, 1998 to December 31, 1999 are used. The number of trading days throughout this period is 522. The three major stock indices are, respectively, Hang Seng Index (HSI), Hang Seng China-Affiliated Corporations Index (HSCCI) and Hang Seng China Enterprises Index (HSCEI). Of the 86 equities, 30 of them are HSI constituents, 32 are HSCCI constituents and the remaining 24 are HSCEI constituents. The index data are directly used for adaptive portfolio management while the stock prices are used by Gaussian TFA for recovering independent hidden factors $y _ { t } .$

## 4.2.2. Methodology

We consider the task of managing a portfolio which consists of four securities, the average fixed deposit interest rate and the three major stock indices in Hong Kong. The fixed deposit interest rate is used as the proxy for the risk-free rate of return $r ^ { f } .$ The first 400 samples are used for training and the last 121 samples for testing. In the test phase, we first make prediction on $\hat { y } _ { t }$ and $\hat { x } _ { t }$ with $\hat { y } _ { t } \approx B y _ { t - 1 }$ and $\hat { x } _ { t } \approx A \hat { y } _ { t }$ . Moreover, learning is carried out in an adaptive fashion such that the actual value of $x _ { t }$ at time t is used to extract $y _ { t }$ and modify the parameters once it is known $( \mathrm { i . e . , }$ once the current time t is passed into t + 1). The APTbased algorithm in Table 1 is adopted that uses hidden independent factors extracted by TFA for controlling portfolio weights. We refer to this approach APT-based portfolio management. Both TFA algorithms with or without ARCH effect consideration could be used for this purpose. For simplicity, in the following experiments, we only adopt the one

Table 1  
An adaptive algorithm for implementation of the APT-based portfolio managemen

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Updating rules for the parameter set $\psi$ $\mu_{\mathrm{p}}^{\mathrm{new}} = \mu_{\mathrm{p}}^{\mathrm{old}} + \eta (\nabla_{\zeta_T} S_{\mathrm{p}}) \varphi (\mu_{\mathrm{p}}, \Sigma_{\mathrm{p}}, k) \tau (\mu_{\mathrm{p}}, \Sigma_{\mathrm{p}}, W_{\mathrm{p}}, c_{\mathrm{p}}, k) (y_T - \mu_{\mathrm{p}})$ $\Sigma_{\mathrm{p}}^{\mathrm{new}} = \Sigma_{\mathrm{p}}^{\mathrm{old}} + \eta (\nabla_{\zeta_T} S_{\mathrm{p}}) \varphi (\mu_{\mathrm{p}}, \Sigma_{\mathrm{p}}, k) \tau (\mu_{\mathrm{p}}, \Sigma_{\mathrm{p}}, W_{\mathrm{p}}, c_{\mathrm{p}}, k) \kappa (\mu_{\mathrm{p}}, \Sigma_{\mathrm{p}})$ $W_{\mathrm{p}}^{\mathrm{new}} = W_{\mathrm{p}}^{\mathrm{old}} + \eta (\nabla_{\zeta_T} S_{\mathrm{p}}) y_T \varphi (\mu_{\mathrm{p}}, \Sigma_{\mathrm{p}}, k)$ $c_{\mathrm{p}}^{\mathrm{new}} = c_{\mathrm{p}}^{\mathrm{old}} + \eta (\nabla_{\zeta_T} S_{\mathrm{p}}) \varphi (\mu_{\mathrm{p}}, \Sigma_{\mathrm{p}}, k)$

Updating rules for the parameter set $\phi$ $\hat{\mu}_{\mathrm{p}}^{\mathrm{new}} = \hat{\mu}_{\mathrm{p}}^{\mathrm{old}} + \hat{\eta} (\nabla_{\xi_T^{(j)}} S_{\mathrm{p}}) (y_T - \hat{\mu}_{\mathrm{p}}) \varphi (\hat{\mu}_{\mathrm{p}}, \hat{\Sigma}_{\mathrm{p}}, \hat{k}) \chi (\hat{\mu}_{\mathrm{p}}, \hat{\Sigma}_{\mathrm{p}}, \hat{W}_{p,q}, \hat{c}_{p,q}, \hat{k})$ $\hat{\Sigma}_{\mathrm{p}}^{\mathrm{new}} = \hat{\Sigma}_{\mathrm{p}}^{\mathrm{old}} + \hat{\eta} (\nabla_{\xi_T^{(j)}} S_{\mathrm{p}}) \kappa (\hat{\mu}_{\mathrm{p}}, \hat{\Sigma}_{\mathrm{p}}) \varphi (\hat{\mu}_{\mathrm{p}}, \hat{\Sigma}_{\mathrm{p}}, \hat{k}) \chi (\hat{\mu}_{\mathrm{p}}, \hat{\Sigma}_{\mathrm{p}}, \hat{W}_{p,q}, \hat{c}_{p,q}, \hat{k})$ $\hat{W}_{p,q}^{\mathrm{new}} = \hat{W}_{p,q}^{\mathrm{old}} + \hat{\eta} (\nabla_{\xi_T^{(j)}} S_{\mathrm{p}}) y_T \varphi (\hat{\mu}_{\mathrm{p}}, \hat{\Sigma}_{\mathrm{p}}, \hat{k})$ $\hat{c}_{p,r}^{\mathrm{new}} = \hat{c}_{p,r}^{\mathrm{old}} + \hat{\eta} (\nabla_{\xi_T^{(j)}} S_{\mathrm{p}}) \varphi (\hat{\mu}_{\mathrm{p}}, \hat{\Sigma}_{\mathrm{p}}, \hat{k})$ where $\eta$ and $\hat{\eta}$ are learning rates,

$M(R_T) = 1/T\Sigma_{t=1}^T R_t, V(R_T) = 1/T\Sigma_{t=1}^T [R_t - M(R_T)]^2$ $\nabla_{\zeta_T} S_{\mathrm{p}} = \frac{\left[V(R_T) - M(R_T)\left(R_T - M(R_T) - \frac{1}{T} \sum_{t=1}^T (R_T - M(R_t))\right)\right]}{T \sqrt {[V(R_T)]^3}} \left(\frac{\sum_{r=1}^{m} \exp(\xi_T^{(r)}) x_T^{(r)}}{\sum_{r=1}^{m} \exp(\xi_T^{(r)})} - r^f\right) \exp(\zeta_T),$ $\nabla_{\xi_T^{(j)}} S_{\mathrm{p}} = \frac{\left[V(R_T) - M(R_T)\left(R_T - M(R_T) - \frac{1}{T} \sum_{t=1}^T (R_t - M(R_t))\right)\right] \exp(\zeta_T) x_T^{(j)} \left(\sum_{r=1}^{m} \exp(\xi_T^{(r)}) - \exp(\xi_T^{(j)})\right) \exp(\xi_T^{(j)})}{T \sqrt {[V(R_T)]^3} \left(\sum_{r=1}^{m} \exp(\xi_T^{(r)})\right)^2}$,

$\varphi(\mu_{\mathrm{p}}, \Sigma_{\mathrm{p}}, k) = \frac{\exp(-0.5(y_T - \mu_{\mathrm{p}})^T\Sigma_{\mathrm{p}}^{-1}(y_T - \mu_{\mathrm{p}}))}{\sum_{r=1}^{k} \exp(-0.5(y_T - \mu_r)^T\Sigma_r^{-1}(y_T - \mu_r))}$,

$\kappa(\mu_{\mathrm{p}}, \Sigma_{\mathrm{p}}) = \Sigma_{\mathrm{p}}^{-1}(y_T - \mu_{\mathrm{p}})(y_T - \mu_{\mathrm{p}})^T\Sigma_{\mathrm{p}}^{-1} - 0.5 \text {diag } [\Sigma_{\mathrm{p}}^{-1}(y_T - \mu_{\mathrm{p}})(y_T - \mu_{\mathrm{p}})^T\Sigma_{\mathrm{p}}^{-1}],$ $\tau(\mu_{\mathrm{p}}, \Sigma_{\mathrm{p}}, W_{\mathrm{p}}, c_{\mathrm{p}}, k) = \frac{(W_p^T y_T + c_p) - \sum_{r=1}^{k} (W_r^T y_T + c_r) \varphi(\mu_r, \Sigma_r, k)}{\sum_{r=1}^{k} \exp(-0.5(y_T - \mu_r)^T\Sigma_r^{-1}(y_T - \mu_r))}$,

$\chi(\mu_{\mathrm{p}}, \Sigma_{\mathrm{p}}, W_{p,q}, c_{p,q}, k) = \frac{(W_p^T y_T + c_p,q) - \sum_{r=1}^{k} (W_p^T y_T + c_r) \varphi(\mu_r, \Sigma_r, k)}{\sum_{r=1}^{k} \exp(-0.5(y_T - \mu_r)^T\Sigma_r^{-1}(y_T - \mu_r))}$,
</div>

$W _ { p , q }$ denotes the pth column of the qth matrix, diag[M] denotes a diagonal matrix that takes the diagonal part of a matrix M, $\zeta _ { T } { = } g ( y _ { T } , \psi )$ as defined in Eq. (6) and $\xi _ { T } ^ { ( j ) }$ is the $j \mathrm { t h }$ output of $f ( y _ { T } , \phi )$ as defined in Eq. (7).

without ARCH consideration. For each $y _ { t }$ under test, we can adaptively get $\zeta _ { t } { = } g ( y _ { t } , \psi )$ and $\xi _ { t } { = } f ( y _ { t } , \ \phi _ { t } ) ,$ and then the portfolio weights $\alpha _ { t } { = } \exp \ ( \zeta _ { t } )$ and $\dot { \boldsymbol { \beta } } _ { t } ^ { ( j ) }$ $= \exp ( \xi _ { t } ^ { ( j ) } ) / \sum _ { r = 1 } ^ { m }$ exp (n<sub>t</sub><sup>(r)</sup>). Finally, returns can be computed via Eq. (8). For the sake of comparison, we also implement a traditional approach that directly uses stock returns $x _ { t }$ instead of hidden factors $y _ { t }$ [8]. We refer to this approach return-based portfolio management.

## 4.2.3. Results

Fig. 1 shows the returns of individual securities that make up the portfolio during the test phase, with relevant risk-return statistics given in Table 2. Graphical comparison of profit gain between the two approaches using test data is shown in Fig. 2. Daily risk-return statistics of the portfolios are given in Table 3.

![](/api/attachments/EE5TEUCA/fulltext/images/590ecc8e345f9c2aee348e5bbbe2281e6dff4035cef3cfad951a39872dd84f24.jpg)

![](/api/attachments/EE5TEUCA/fulltext/images/c137fef012dd909c1f16c9318654740b1e7488a0805ae8bf89463fe070c24009.jpg)

![](/api/attachments/EE5TEUCA/fulltext/images/85bcd2d6ef75cbdf5d82c4d71c279edd8ab45683ac57eae8703e1163d50b875c.jpg)  
(c) Daily return of HSCCI

![](/api/attachments/EE5TEUCA/fulltext/images/f2b9218dcbfacfb96fb4c3630938c3b9b3f528a8f2cd87a59d16b04cd66c7fe7.jpg)  
Fig. 1. Returns of individual securities in the portfolio.

## 4.3. Scenario II: has transaction cost but short sale not permitted

Scenario II differs from Scenario I in taking into account the effect of transaction cost. Since any change on $\beta _ { t } ^ { ( j ) }$ leads to a transaction that incurs a cost on return $c _ { t }$ given by

Table 2  
Daily risk-return statistics of constituents of portfolios

<table><tr><td>Component name</td><td>Mean return (%)</td><td>Risk (%)</td></tr><tr><td>Average interest rate</td><td>0.0148</td><td>0.00</td></tr><tr><td>HSI</td><td>0.18</td><td>1.48</td></tr><tr><td>HSCCI</td><td>0.03</td><td>2.51</td></tr><tr><td>HSCEI</td><td>-0.20</td><td>2.55</td></tr></table>

![](/api/attachments/EE5TEUCA/fulltext/images/cb44f1ed7e15fac4ae3fa39f93d61bd917b7694f8dc1480b644e9ec0ff36ef08.jpg)  
Fig. 2. Comparative profit gain of APT-based and return-based portfolios for Scenario I.

Table 3  
Daily risk-return statistics of the portfolio for Scenario I

<table><tr><td></td><td>Return-based portfolio</td><td>APT-based portfolio</td><td>Change in Sharpe ratio  $\Delta S_{p}$ </td></tr><tr><td>Mean return</td><td>0.06%</td><td>0.14%</td><td>-</td></tr><tr><td>Risk</td><td>0.48%</td><td>0.81%</td><td>-</td></tr><tr><td>Sharpe ratio</td><td>0.1250</td><td>0.1728</td><td> $\uparrow$  38.24%</td></tr></table>

$$
\begin{array}{l} c _ {t} = - \alpha_ {t} \sum_ {j = 1} ^ {m} r _ {c} | \beta_ {t} ^ {(j)} - \beta_ {t - 1} ^ {(j)} | p _ {t} ^ {(j)} / p _ {t - 1} ^ {(j)} \\ = - \alpha_ {t} \sum_ {j = 1} ^ {m} r _ {c} | \beta_ {t} ^ {(j)} - \beta_ {t - 1} ^ {(j)} | (1 + x _ {t} ^ {(j)}) \end{array}\tag{15}
$$

where $r _ { c }$ is a constant denoting the rate of transaction cost. Consequently, we consider the portfolio return adjusted for transaction cost given by Ref. [19] n

$$
\begin{array}{l} R _ {t} = (1 - \alpha_ {t}) r ^ {f} + \alpha_ {t} \sum_ {j = 1} ^ {m} [ \beta_ {t} ^ {(j)} x _ {t} ^ {(j)} - r _ {c} | \beta_ {t} ^ {(j)} \\ \quad - \beta_ {t - 1} ^ {(j)} | (1 + x _ {t} ^ {(j)}) ], \\ \text { subject   to } \left\{ \begin{array}{l} \alpha_ {t} > 0, \\ 0 \leq \beta_ {t} \leq 1, \\ \sum_ {j = 1} ^ {m} \beta_ {t} ^ {(j)} = 1 \end{array} . \right. \end{array}\tag{16}
$$

The APT-based algorithm in Table 1 could still be adopted in this case, except that the two terms $\nabla _ { \zeta } S _ { \mathrm { p } }$ and $\nabla _ { \xi _ { T } ^ { ( j ) } } S _ { \mathrm { p } }$ become, respectively,

$$
\begin{array}{l}\nabla_ {\zeta_ {T}} S _ {\mathfrak {p}} = \frac {\left[ V (R _ {T}) - M (R _ {T}) \left(R _ {T} - M (R _ {T}) - \frac {1}{T} \sum_ {t = 1} ^ {T} (R _ {t} - M (R _ {t}))\right) \right]}{T \sqrt {[ V (R _ {T}) ] ^ {3}}}\\\times \left(\sum_ {j = 1} ^ {m} \left[ \frac {\exp (\xi_ {T} ^ {(j)}) x _ {T} ^ {(j)}}{\sum_ {r = 1} ^ {m} \exp (\xi_ {T} ^ {(r)})} - r _ {c} \middle | \frac {\exp (\xi_ {T} ^ {(j)})}{\sum_ {r = 1} ^ {m} \exp (\xi_ {T} ^ {(r)})} \right. \right.\\\left. - \frac {\exp (\xi_ {T - 1} ^ {(j)})}{\sum_ {r = 1} ^ {m} \exp (\xi_ {T - 1} ^ {(r)})} \middle | (1 + x _ {T} ^ {(j)}) \right] - r ^ {f}\left. \right) \exp (\zeta_ {T}),\end{array}
$$

$$
\begin{array}{l} \nabla_ {\xi_ {T} ^ {(j)}} S _ {\mathrm{p}} = \left[ V (R _ {T}) - M (R _ {T}) \Bigg (R _ {T} - M (R _ {T}) \right. \\ \left. - \frac {1}{T} \sum_ {t = 1} ^ {T} (R _ {t} - M (R _ {t})) \Bigg) \right] \exp (\zeta_ {T}) \\ \times \left[ x _ {T} ^ {(j)} - r _ {c} \operatorname{sign} \Big (\exp (\xi_ {T} ^ {(j)}) - \exp (\xi_ {T} ^ {(j - 1)}) \Big) \right] \\ \times \left[ \sum_ {r = 1} ^ {m} \exp (\xi_ {T} ^ {(r)}) - \exp (\xi_ {T} ^ {(j)}) \right] \exp (\xi_ {T} ^ {(j)}) \\ \Bigg / \left[ T \sqrt {[ V (R _ {T}) ] ^ {3}} \left(\sum_ {r = 1} ^ {m} \exp (\xi_ {T} ^ {(r)})\right) ^ {2} \right] \end{array}
$$

## 4.3.1. Simulation

For the purpose of simulation, we fix the rate of transaction cost at $r _ { c } { = } 0 . 1 \%$ . Graphical comparison of profit gain between the two approaches using test data is shown in Fig. 3, while daily risk-return statistics of the portfolios are given in Table 4.

4.4. Scenario III: no transaction cost but short sale is permitted

Scenario III differs from Scenario I in that short sale is now permitted. By removing the nonnegative constraints on $\alpha _ { t }$ and $\beta _ { t }$ in Eq. (8), we get

![](/api/attachments/EE5TEUCA/fulltext/images/392c48727cdcb4c95cf1a9b68c4dea57785f35035e96b27ad4b3e846f2c53940.jpg)  
Fig. 3. Comparative profit gain of APT-based and return-based portfolios for Scenario II.

Table 4  
Risk-return statistics of the portfolio for Scenario II

<table><tr><td></td><td>Return-based portfolio</td><td>APT-based portfolio</td><td>Change in Sharpe ratio  $\Delta S_{p}$ </td></tr><tr><td>Mean return</td><td>0.04%</td><td>0.12%</td><td>-</td></tr><tr><td>Risk</td><td>0.42%</td><td>0.73%</td><td>-</td></tr><tr><td>Sharpe ratio</td><td>0.0952</td><td>0.1644</td><td> $\uparrow$  72.69%</td></tr></table>

$$
\begin{array}{c} R _ {t} = (1 - \alpha_ {t}) r ^ {f} + \alpha_ {t} \sum_ {j - 1} ^ {m} \beta_ {t} ^ {(j)} x _ {t} ^ {(j)} \\ - r _ {c} | \beta_ {t} ^ {(j)} - \beta_ {t - 1} ^ {(j)} | (1 + x _ {t} ^ {(j)}) \end{array}
$$

$$
\text { subject   to } \sum_ {j = 1} ^ {m} \beta_ {t} ^ {(j)} = 1\tag{17}
$$

and the new objective function

$$
\begin{array}{l} \max _ {\psi , \phi} S _ {p} = \frac {M (R _ {T})}{\sqrt {V (R _ {T})}} \\ \text { subject   to } \left\{ \begin{array}{l} \alpha_ {t} = \zeta_ {t} = g (y _ {t}, \psi), \\ \beta_ {t} ^ {(j)} = \xi_ {t} ^ {(j)} / \sum_ {r = 1} ^ {m} \xi_ {t} ^ {(r)}, \\ \xi_ {t} = f (y _ {t}, \phi) \end{array} \right. \end{array}\tag{18}
$$

In implementation, the algorithm in Table 1 could be adopted, except the two terms $\nabla _ { \zeta } S _ { \mathrm { p } }$ and $\nabla _ { \xi _ { T ( j ) } } S _ { \mathrm { p } }$ become, respectively,

$$
\begin{array}{l} \nabla_ {\zeta_ {T}} S _ {\mathfrak {p}} = \frac {\left[ V (R _ {T}) - M (R _ {T}) \left(R _ {T} - M (R _ {T}) - \frac {1}{T} \sum_ {t = 1} ^ {T} (R _ {t} - M (R _ {t}))\right) \right]}{T \sqrt {[ V (R _ {T}) ] ^ {3}}} \\ \times \left(\sum_ {j = 1} ^ {m} \left[ \frac {\xi_ {T} ^ {(j)} x _ {T} ^ {(j)}}{\sum_ {r = 1} ^ {m} \xi_ {T} ^ {(r)}} - r _ {c} \left| \frac {\xi_ {T} ^ {(j)}}{\sum_ {r = 1} ^ {m} \xi_ {T} ^ {(r)}} - \frac {\xi_ {T - 1} ^ {(j)}}{\sum_ {r = 1} ^ {m} \xi_ {T - 1} ^ {(r)}} \right| (1 + x _ {T} ^ {(j)}) \right] - r ^ {f}\right) \\ \nabla_ {\frac {\varepsilon^ {(j)}}{\xi_ {T}}} S _ {\mathfrak {p}} = \frac {\left[ V (R _ {T}) - M (R _ {T}) \left(R _ {T} - M (R _ {T}) - \frac {1}{T} \sum_ {t = 1} ^ {T} (R _ {t} - M (R _ {t}))\right) \right] \zeta_ {T} x _ {T} ^ {(j)} \left(\sum_ {r = 1} ^ {m} \xi_ {T} ^ {(r)} - \xi_ {T} ^ {(j)}\right)}{T \sqrt {[ V (R _ {T}) ] ^ {3}} \left(\sum_ {r = 1} ^ {m} \xi_ {T} ^ {(r)}\right) ^ {2}} \end{array}
$$

## 4.4.1. Simulation

For the purpose of simulation, short selling is not applicable to the return-based approach. Graphical comparison of profit gain between the two approaches using test data is shown in Fig. 4, while daily risk-return statistics of the portfolios are given in Table 5.

4.5. Scenario IV: has transaction cost and short sale is permitted

Scenario IV differs from Scenario I in that the effects of both transaction cost and short sale on portfolio selection have to be treated appropriately. As a result, we have

$$
\begin{array}{c} R _ {t} = (1 - \alpha_ {t}) r ^ {f} + \alpha_ {t} \sum_ {j = 1} ^ {m} [ \beta_ {t} ^ {(j)} x _ {t} ^ {(j)} - r _ {c} | \beta_ {t} ^ {(j)} \\ - \beta_ {t - 1} ^ {(j)} | (1 + x _ {t} ^ {(j)}) ], \end{array}
$$

$$
\text { subject   to } \sum_ {j = 1} ^ {m} \beta_ {t} ^ {(j)} = 1\tag{19}
$$

Here, we have the objective function the same as Eq. (18). The APT-based algorithm in Table 1 could still be adopted in this case, except that the two terms $\nabla _ { \zeta } S _ { \mathrm { p } }$ and $\nabla _ { \xi _ { T } ^ { ( j ) } } S _ { \mathrm { p } }$ become, respectively,

![](/api/attachments/EE5TEUCA/fulltext/images/98f43dae268dde342a23e330218ea00ab4dad128b6479613574db07a4ed0fec5.jpg)  
Fig. 4. Comparative profit gain of APT-based and return-based portfolios for Scenario III.

Table 5  
Risk-return statistics of the portfolio for Scenario III

<table><tr><td></td><td>Return-based portfolio</td><td>APT-based portfolio</td><td>Change in Sharpe ratio  $\Delta S_{p}$ </td></tr><tr><td>Mean return</td><td>0.06%</td><td>0.19%</td><td>-</td></tr><tr><td>Risk</td><td>0.48%</td><td>0.92%</td><td>-</td></tr><tr><td>Sharpe ratio</td><td>0.1250</td><td>0.2065</td><td> $\uparrow$  65.20%</td></tr></table>

$$
\begin{array}{l} \nabla_ {\zeta_ {T}} S _ {\mathrm{p}} = \frac {\left[ V (R _ {T}) - M (R _ {T}) \left(R _ {T} - M (R _ {T}) - \frac {1}{T} \sum_ {t = 1} ^ {T} (R _ {t} - M (R _ {t}))\right) \right]}{T \sqrt {[ V (R _ {T}) ] ^ {3}}} \\ \times \left(\frac {\sum_ {j = 1} ^ {m} \xi_ {T} ^ {(j)} x _ {T} ^ {(j)}}{\sum_ {j = 1} ^ {m} \xi_ {T} ^ {(j)}} - r ^ {f}\right), \end{array}
$$

$$
\begin{array}{l} \nabla_ {\xi_ {T} ^ {(j)}} S _ {\mathfrak {p}} = \left[ V (R _ {T}) - M (R _ {T}) \left(R _ {T} - M (R _ {T}) \right. \right. \\ \left. \left. - \frac {1}{T} \sum_ {t = 1} ^ {T} (R _ {t} - M (R _ {t}))\right) \right] \zeta_ {T} \\ \times \left[ x _ {T} ^ {(j)} - r _ {c} \mathrm{sign} \left(\xi_ {T} ^ {(j)} - \xi_ {T} ^ {(j - 1)}\right) \right] \\ \times \left[ \sum_ {r = 1} ^ {m} \xi_ {T} ^ {(r)} - \xi_ {T} ^ {(j)} \right] \\ / \left[ T \sqrt {[ V (R _ {T}) ] ^ {3}} \left(\sum_ {r = 1} ^ {m} \xi_ {T} ^ {(r)}\right) ^ {2} \right] \end{array}
$$

## 4.5.1. Simulation

In simulation, we fix the rate of transaction cost at $\begin{array} { r } { r _ { c } = 0 . 1 \% } \end{array}$ , and short selling is not applicable to the return-based approach. Graphical comparison of profit gain between the two approaches using test data is shown in Fig. 5, while daily risk-return statistics of the portfolios are given in Table 6.

## 4.6. Performance evaluation

To summarize the experimental results of the above four scenarios, we have noted the following two phenomena. First, the APT-based portfolio in general performs better than the return-based portfolio if the scope of comparison is limited to within each scenario, as evidenced by higher $S _ { \mathrm { p } }$ attained in Tables 3–6. It should be noted that higher $S _ { \mathrm { p } }$ may arise as a consequence of one of the following situations: (i) higher expected return, lower overall volatility; (ii) higher expected return, same overall volatility; (iii) same expected return, lower overall volatility; (iv) both expected return increase or decrease, with expected return increases (decreases) at a faster (lower) rate than overall volatility. Second, if we compare the performance of APT-based portfolios across all the four scenarios, especially the portfolio Sharpe ratio of scenario III against I (z19.50%) and scenario IV against II (z10.58%), we may conclude that performance may be further improved whenever short sale is permitted.

The first phenomenon reveals the fact that independent hidden factors may be more effective in controlling portfolio weights. Possible rationales include dimensionality reduction, as there are usually only a few hidden factors for a large number of securities. What seems to be a more important revelation is that the classical APT [16] model is still helpful here.

![](/api/attachments/EE5TEUCA/fulltext/images/7e3b1a42d2684b4dfe9003b6d7623758f131519c67d9f16805a7a2c21d4259fd.jpg)  
Fig. 5. Comparative profit gain of APT-based and return-based portfolios for Scenario IV.

Table 6  
Risk-return statistics of the portfolio for Scenario IV

<table><tr><td></td><td>Return-based portfolio</td><td>APT-based portfolio</td><td>Change in Sharpe ratio  $\Delta S_{p}$ </td></tr><tr><td>Mean return</td><td>0.04%</td><td>0.16%</td><td>-</td></tr><tr><td>Risk</td><td>0.42%</td><td>0.88%</td><td>-</td></tr><tr><td>Sharpe ratio</td><td>0.0952</td><td>0.1818</td><td> $\uparrow$  90.97%</td></tr></table>

Although short selling is expensive for individual investors and not generally permissible for most institutional investors [2] in many markets, relevant experimental results reveal the hypothetical potential benefit such facility might add to the portfolio returns. The benefit mainly arises from the exploitation of downside trend in market price in addition to upward movement. This, in turn, reduces the chance that the fund is left idle due to declining stock prices for most stocks, which is more or less a phenomenon when the general market atmosphere is gloomy.

## 5. APT-based portfolio management by modified portfolio Sharpe ratio

In this section, we consider three variants of the portfolio Sharpe ratio. Specifically, we consider portfolio expected downside risk $V _ { T } ^ { - }$ which is represented by

$$
V _ {T} ^ {-} = \frac {1}{T} \sum_ {t = 1} ^ {T} \sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {m} \beta_ {t} ^ {(i)} \beta_ {t} ^ {(j)} \int_ {- \infty} ^ {0} \int_ {- \infty} ^ {0} x _ {t} ^ {(i)} x _ {t} ^ {(j)} p
$$

$$
(x _ {t} ^ {(i)}, x _ {t} ^ {(j)}) \mathrm{d} x _ {t} ^ {(i)} \mathrm{d} x _ {t} ^ {(j)}
$$

$$
= \frac {1}{T} \sum_ {t = 1} ^ {T} \sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {m} \beta_ {t} ^ {(i)} \beta_ {t} ^ {(j)} D _ {t} ^ {(i, j)}\tag{20}
$$

where $\beta _ { i }$ and $x _ { i }$ denote the portfolio weight and return of the ith risky security, respectively, and $D _ { t } ^ { ( i , j ) }$ is a constant.

In addition to considering the downside risk, the so-called portfolio expected upside volatility $V _ { T } ^ { + }$ can be defined similarly as

$$
V _ {T} ^ {+} = \frac {1}{T} \sum_ {t = 1} ^ {T} \sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {m} \beta_ {t} ^ {(i)} \beta_ {t} ^ {(j)} \int_ {0} ^ {\infty} \int_ {0} ^ {\infty} x _ {t} ^ {(i)} x _ {t} ^ {(j)} p
$$

$$
(x _ {t} ^ {(i)}, x _ {t} ^ {(j)}) \mathbf {d} x _ {t} ^ {(i)} \mathbf {d} x _ {t} ^ {(j)}
$$

$$
= \frac {1}{T} \sum_ {t = 1} ^ {T} \sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {m} \beta_ {t} ^ {(i)} \beta_ {t} ^ {(j)} U _ {t} ^ {(i, j)}\tag{21}
$$

where $\beta _ { i }$ and $x _ { i }$ denote the portfolio weight and return of the ith risky security, respectively, and $U _ { t } ^ { ( i , j ) }$ is a constant.

5.1. Modified Sharpe ratio with minimum downside risk and maximum upside volatility

Given that portfolio variance can be broken down into portfolio downside risk and upside volatility, it is desirable to consider the maximization of the upside volatility and minimization of the downside risk at the same time in calculating the optimal portfolio. In other words, we can consider maximization of the following improved Sharpe ratio $S _ { \mathrm { p } } ^ { \prime }$

$$
\max _ {\psi , \phi} S _ {\mathrm{p}} ^ {\prime} = \frac {M (R _ {T}) + V _ {T} ^ {+}}{V _ {T} ^ {-}}
$$

$$
\text { subject   to } \left\{ \begin{array}{l} \alpha_ {t} = \exp (\zeta_ {t}), \\ \zeta_ {t} = g (y _ {t}, \psi), \\ \beta_ {t} ^ {(j)} = \exp (\xi_ {t} ^ {(j)}) / \sum_ {r = 1} ^ {m} \exp (\xi_ {t} ^ {(r)}), \\ \xi_ {t} = f (y _ {t}, \phi) \end{array} . \right.\tag{22}
$$

In implementation, the algorithm in Table 1 could be adopted, except the two terms $\nabla _ { \zeta } S _ { \mathrm { p } }$ and $\nabla _ { \xi _ { T } ^ { ( j ) } } S _ { p }$ become, respectively,

$$
\nabla_ {\zeta_ {T}} S _ {\mathrm{p}} ^ {\prime} = \frac {\sum_ {j = 1} ^ {m} \exp (\xi_ {T} ^ {(j)}) \left(\sum_ {j = 1} ^ {m} \exp (\xi_ {T} ^ {(j)}) x _ {T} ^ {(j)} - r ^ {f} \sum_ {j = 1} ^ {m} \exp (\xi_ {T} ^ {(j)})\right) \exp (\zeta_ {T})}{\sum_ {t = 1} ^ {T} \sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {m} \exp (\xi_ {T} ^ {(i)}) \exp (\xi_ {T} ^ {(j)}) D _ {t} ^ {(i , j)}},
$$

$$
\begin{array}{l} \nabla_ {\xi_ {T} ^ {(j)}} S _ {\mathrm{p}} ^ {\prime} = \left[ \sum_ {t = 1} ^ {T} \sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {m} \exp (\xi_ {T} ^ {(i)}) \exp (\xi_ {T} ^ {(j)}) D _ {t} ^ {(i, j)} \right. \\ \times \left(\exp (\zeta_ {T}) x _ {T} ^ {(j)} + \frac {\sum_ {i = 1} ^ {m} \exp (\xi_ {T} ^ {(i)}) U _ {T} ^ {(i , j)}}{\sum_ {r = 1} ^ {m} \exp (\xi_ {T} ^ {(r)})}\right) \\ - \left(\sum_ {t = 1} ^ {T} R _ {t} + \sum_ {t = 1} ^ {T} \sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {m} \exp (\xi_ {T} ^ {(i)}) \exp (\xi_ {T} ^ {(j)}) \right. \\ \left. \times U _ {t} ^ {(i, j)})\right) \frac {\sum_ {i = 1} ^ {m} \exp (\xi_ {T} ^ {(i)}) D _ {T} ^ {(i , j)}}{\sum_ {r = 1} ^ {m} \exp (\xi_ {T} ^ {(r)})} \\ \times \left[ \left(\sum_ {r = 1} ^ {m} \exp (\xi_ {T} ^ {(r)}) - \exp (\xi_ {T} ^ {(j)})\right) \exp (\xi_ {T} ^ {(j)}) \right] \\ \Bigg / \left(\sum_ {t = 1} ^ {T} \sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {m} \exp (\xi_ {T} ^ {(i)}) \exp (\xi_ {T} ^ {(j)}) D _ {t} ^ {(i, j)}\right) \\ \times \left(\sum_ {r = 1} ^ {m} \exp (\xi_ {T} ^ {(r)})\right) ] ^ {2} \end{array}
$$

## 5.1.1. Simulation

We implement the modified Sharpe ratio simulation using the same set of data described before and the APT-based approach in Scenario I as benchmark for comparison. Graphical comparison of profit gain between the two approaches using test data is shown in Fig. 6, while daily risk-return statistics of the portfolios are given in Table 7.

![](/api/attachments/EE5TEUCA/fulltext/images/4975394a58335ec0e999321c216274d8208006875a90c5062029fde29b28d4c6.jpg)  
Fig. 6. Comparative profit gain under original and modified Sharpe ratio.

## 5.2. Risk minimization with control of expected return

Some conservative investors are more concerned about risk than return. Therefore, a more appropriate investment strategy may be to minimize risk while controlling the expected return. Particularly, this can be achieved by setting the expected return in $\operatorname { E q . }$ (30) to be a constant specified by the investor, and the optimization essentially becomes a minimization of downside risk and a maximization of upside volatility.

$$
\max _ {\psi , \phi} S _ {\mathrm{p}} ^ {\prime} = \frac {r + V _ {T} ^ {+}}{V _ {T} ^ {-}}
$$

$$
\text { subject   to } \left\{ \begin{array}{l} \alpha_ {t} = \exp (\zeta_ {t}), \\ \zeta_ {t} = g (y _ {t}, \psi), \\ \beta_ {t} ^ {(j)} = \exp (\xi_ {t} ^ {(j)}) / \sum_ {r = 1} ^ {m} \exp (\xi_ {t} ^ {(r)}), \\ \xi_ {t} = f (y _ {t}, \phi), \\ M (R _ {T}) = r \end{array} . \right.\tag{23}
$$

To solve the above optimization problem with equality constraints, we adopt the augmented Lagrangian method. Specifically, for the equality constrained problem,

Daily Risk-return statistics of portfolio under original and modified Sharpe ratio

<table><tr><td></td><td>Original Sharpe ratio</td><td>Modified Sharpe ratio</td></tr><tr><td>Mean return</td><td>0.14%</td><td>0.24%</td></tr><tr><td>Risk</td><td>0.81%</td><td>1.13%</td></tr><tr><td>Upside volatility</td><td>-</td><td>0.43%</td></tr><tr><td>Downside risk</td><td>-</td><td>0.35%</td></tr><tr><td>Sharpe ratio  $S_p$ </td><td>0.1728</td><td>1.9143</td></tr></table>

maximize f ðxÞ with respect to x

ð24Þ

subject to hðxÞ ¼ 0;

the augmented Lagrangian function can be written as

$$
L (x, \lambda) = f (x) - \lambda h (x) - \frac {1}{2} c [ h (x) ] ^ {2}\tag{25}
$$

where k is the Lagrange multiplier, c is the penalty parameter. Then, a sequence of minimizations of the form

maximize $L _ { c _ { k } } ( x , \lambda _ { k } )$ with respect to x

ð26Þ

subject to $x { \in } \mathbb { R } ^ { n }$

is performed, where $\{ c _ { k } \}$ is a sequence of positive penalty parameters sequence satisfying

$$
\begin{array}{l l} 0 <   c _ {k} <   c _ {k + 1} & \forall k \\ c _ {k} \to \infty & \text { as } k \to \infty \end{array} .\tag{27}
$$

The multiplier sequence $\{ \lambda _ { k } \}$ is generated by the iteration

$$
\lambda_ {k + 1} = \lambda_ {k} + c _ {k} h (\hat {x})\tag{28}
$$

where xˆ is the solution of Eq. (26).

Here, the augmented Lagrangian is given by

$$
\begin{array}{l} r + \frac {1}{T} \sum_ {t = 1} ^ {T} \sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {m} \beta_ {t} ^ {(i)} \beta_ {t} ^ {(j)} U _ {t} ^ {(i, j)} \\ L = \frac {\frac {1}{T} \sum_ {t = 1} ^ {T} \sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {m} \beta_ {t} ^ {(i)} \beta_ {t} ^ {(j)} D _ {t} ^ {(i , j)}}{- \lambda \left(\frac {1}{T} \sum_ {t = 1} ^ {T} R _ {t} - r\right) - \frac {c}{2} \left(\frac {1}{T} \sum_ {t = 1} ^ {T} R _ {t} - r\right) ^ {2}} \end{array}\tag{29}
$$

In implementation, the algorithm in Table 1 could be adopted, except the two terms $\nabla _ { \zeta } S _ { \mathrm { p } }$ and $\nabla _ { \xi _ { T } ^ { ( j ) } } S _ { \mathrm { p } }$ are replaced by $\nabla _ { \zeta _ { T } } L$ and $\nabla _ { \xi _ { T } ^ { ( j ) } } L$ , respectively, where

$$
\begin{array}{l} \nabla_ {\zeta_ {T}} L = \frac {\exp (\zeta_ {T})}{T} \left(r ^ {f} - \frac {\sum_ {r = 1} ^ {m} \exp (\xi_ {T} ^ {(r)}) x _ {T} ^ {(r)}}{\sum_ {r = 1} ^ {m} \exp (\xi_ {T} ^ {(r)})}\right) \\ \times (\lambda + c (M (R _ {T}) - r)) \end{array}
$$

$$
\begin{array}{l} \nabla_ {\xi_ {T} ^ {(j)}} L = \left[ \left(\sum_ {t = 1} ^ {T} \sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {m} \exp (\xi_ {T} ^ {(i)}) \exp (\xi_ {T} ^ {(j)}) D _ {t} ^ {(i, j)} \right. \right. \\ \times \left(\frac {\sum_ {i = 1} ^ {m} \exp (\xi_ {T} ^ {(i)}) U _ {T} ^ {(i , j)}}{\sum_ {r = 1} ^ {m} \exp (\xi_ {T} ^ {(r)})}\right) \\ - \left(\sum_ {t = 1} ^ {T} \sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {m} \exp (\xi_ {T} ^ {(i)}) \exp (\xi_ {T} ^ {(j)}) U _ {t} ^ {(i, j)}\right) \\ \times \left. \frac {\sum_ {i = 1} ^ {m} \exp (\xi_ {T} ^ {(i)}) D _ {T} ^ {(i , j)}}{\sum_ {r = 1} ^ {m} \exp (\xi_ {T} ^ {(r)})}\right) \\ / \left(\sum_ {t = 1} ^ {T} \sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {m} \exp (\xi_ {T} ^ {(i)}) \exp (\xi_ {T} ^ {(j)}) D _ {t} ^ {(i, j)}\right) ^ {2} \end{array}
$$

$$
\left. \begin{array}{l} - \frac {\exp (\zeta_ {T}) x _ {T} ^ {(j)}}{T} (\lambda + c (M (R _ {T}) - r)) \\ \times \frac {\left(\sum_ {r = 1} ^ {m} \exp (\xi_ {T} ^ {(r)}) - \exp (\xi_ {T} ^ {(j)})\right) \exp (\xi_ {T} ^ {(j)})}{\left[ \sum_ {r = 1} ^ {m} \exp (\xi_ {T} ^ {(r)}) \right] ^ {2}} \end{array} \right]
$$

## 5.2.1. Simulation

We simulate the modified Sharpe ratio with control of expected return approach and use the modified Sharpe ratio approach in the previous subsection as benchmark. The predetermined expected return used for the simulation is $r = ~ 0 . 1 5 \%$ Graphical comparison of profit gain between the two approaches using test data is shown in Fig. 7, while daily risk-return statistics of the portfolios are given in Table 8.

## 5.3. Return maximization with control of expected downside risk

Some aggressive investors are more concerned about return than risk. Therefore, a strategy that may better serve them is to maximize the expected return while controlling the expected downside risk. In particular, this can be achieved by setting the expected downside risk in Eq. (30) to be a constant specified by the investor, and the optimization essentially becomes a maximization of expected return and upside volatility.

![](/api/attachments/EE5TEUCA/fulltext/images/ef180ad6eb0fdb3f90417bcc0ce57087ba8aa1683c9d24c7d8a0f0bbd4a961a8.jpg)  
Fig. 7. Comparative profit gain of portfolio with control of expected return.

Table 8  
Risk-return statistics of portfolio with control of expected return

<table><tr><td></td><td>Modified Sharpe ratio</td><td>Modified Sharpe ratio with control of expected return</td></tr><tr><td>Mean return</td><td>0.24%</td><td>0.17%</td></tr><tr><td>Risk</td><td>1.13%</td><td>0.79%</td></tr><tr><td>Upside volatility</td><td>0.43%</td><td>0.30%</td></tr><tr><td>Downside risk</td><td>0.35%</td><td>0.23%</td></tr><tr><td>Sharpe ratio  $S_p$ </td><td>1.9143</td><td>2.0435</td></tr></table>

$$
\begin{array}{l} \max _ {\psi , \phi} S _ {\mathrm{p}} ^ {\prime} = \frac {M (R _ {T}) + V _ {T} ^ {+}}{v} \\ \text { subject   to } \left\{ \begin{array}{l} \alpha_ {t} = \exp (\zeta_ {t}), \\ \zeta_ {t} = g (y _ {t}, \psi), \\ \beta_ {t} ^ {(j)} = \exp (\xi_ {t} ^ {(j)}) / \sum_ {r = 1} ^ {m} \exp (\xi_ {t} ^ {(r)}), \\ \zeta_ {t} = f (y _ {t}, \phi), \\ V _ {T} ^ {-} = v \end{array} \right. \end{array}\tag{30}
$$

Here, the augmented Lagrangian is given by

$$
\begin{array}{l} L = \frac {1}{T v} \left(\sum_ {t = 1} ^ {T} R _ {t} + \sum_ {t = 1} ^ {T} \sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {m} \beta_ {t} ^ {(i)} \beta_ {t} ^ {(j)} U _ {t} ^ {(i, j)}\right) \\ - \lambda \left(\frac {1}{T} \sum_ {t = 1} ^ {T} \sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {m} \beta_ {t} ^ {(i)} \beta_ {t} ^ {(j)} D _ {t} ^ {(i, j)} - v\right) \\ - \frac {c}{2} \left(\frac {1}{T} \sum_ {t = 1} ^ {T} \sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {m} \beta_ {t} ^ {(i)} \beta_ {t} ^ {(j)} D _ {t} ^ {(i, j)} - v\right) ^ {2} \end{array}\tag{31}
$$

In implementation, the algorithm in Table 1 could be adopted, except the two terms $\nabla _ { \zeta } S _ { \mathrm { p } }$ and $\nabla _ { \xi _ { T } ^ { ( j ) } } S _ { \mathrm { p } }$ are replaced by $\nabla _ { \zeta _ { T } } L$ and $\nabla _ { \xi _ { T } ^ { ( j ) } L }$ , respectively, where

$$
\nabla_ {\zeta_ {T}} L = \frac {\exp (\zeta_ {T})}{T v} \left(\frac {\sum_ {r = 1} ^ {m} \exp (\xi_ {T} ^ {(r)}) x _ {T} ^ {(r)}}{\sum_ {r = 1} ^ {m} \exp (\xi_ {T} ^ {(r)})} - r _ {f}\right)
$$

$$
\begin{array}{l} \nabla_ {\xi_ {T} ^ {(j)}} L = \left[ \frac {\exp (\zeta_ {T}) T v \sum_ {r = 1} ^ {m} \exp (\xi_ {T} ^ {(r)}) x _ {T} ^ {(j)} + \sum_ {i = 1} ^ {m} \exp (\xi_ {T} ^ {(i)}) U _ {T} ^ {(i , j)}}{T v \sum_ {r = 1} ^ {m} \exp (\xi_ {T} ^ {(r)})} \right. \\ - \frac {\sum_ {i = 1} ^ {m} \exp (\xi_ {T} ^ {(i)}) D _ {T} ^ {(i , j)}}{T \sum_ {r = 1} ^ {m} \exp (\xi_ {T} ^ {(r)})} (\lambda + c (V _ {T} ^ {-} - v)) \\ \times \frac {\left(\sum_ {r = 1} ^ {m} \exp (\xi_ {T} ^ {(r)}) - \exp (\xi_ {T} ^ {(j)})\right) \exp (\xi_ {T} ^ {(j)})}{\left[ \sum_ {r = 1} ^ {m} \exp (\xi_ {T} ^ {(r)}) \right] ^ {2}} \end{array}
$$

## 5.3.1. Simulation

We simulate the modified Sharpe ratio with control of expected downside risk approach and use the modified Sharpe ratio approach in the previous subsection as benchmark. The predetermined expected downside risk used for the simulation is v = 0.20%.

![](/api/attachments/EE5TEUCA/fulltext/images/460a6c877e3a134985187fc0d6ab7a06534ffa79b6919242e9da7fd6298d231e.jpg)  
Fig. 8. Comparative profit gain of portfolio with control of expected downside risk.

Risk-return statistics of portfolio with control of expected downside risk

<table><tr><td></td><td>Modified Sharpe ratio</td><td>Modified Sharpe ratio with control of downside risk</td></tr><tr><td>Mean return</td><td>0.24%</td><td>0.15%</td></tr><tr><td>Risk</td><td>1.13%</td><td>0.71%</td></tr><tr><td>Upside volatility</td><td>0.43%</td><td>0.23%</td></tr><tr><td>Downside risk</td><td>0.35%</td><td>0.19%</td></tr><tr><td>Sharpe ratio  $S_p$ </td><td>1.9143</td><td>0.2000</td></tr></table>

Graphical comparison of profit gain between the two approaches using test data is shown in Fig. 8, while daily risk-return statistics of the portfolios are given in Table 9.

## 5.4. Performance evaluation

The investment strategy with control of expected return is well suited for risk-averse investors. By comparing the statistics shown in Table 8 with that of Table 7, we can see that not only is the expected return under control, but also is risk lowered. As a result, $S _ { \mathrm { p } }$ remains more or less constant. This observation agrees with the tenet in finance that risk and return go hand in hand with each other. Similar reasoning could also be extended to include the case of aggressive profit-seeking investors by comparing the statistics shown in Table 9 with that of Table 7.

## 6. Conclusion

In this paper, we introduce how to utilize the APTbased Gaussian TFA model for adaptive portfolio management. Since TFA is based on the classical APT model and has the benefit of removing rotation indeterminacy via temporal modelling, using TFA for portfolio management would allow portfolio weights to be indirectly controlled by several hidden factors. Moreover, the approach is extended to tailor for investors according to their risk and return objectives. Simulation results reveal that APT-based portfolio management in general excels return-based portfolio management and portfolio returns may be somehow enhanced by short selling, especially when the general market climate is not that favorable.

## Acknowledgements

We would like to express our gratitude to the anonymous reviewers for their comments and suggestions that improved the original manuscript. The work described in this paper was fully supported by a grant from the Research Grant Council of the Hong Kong SAR (Project No. CUHK 4297/98E).

## References

[1] A.D. Back, A.S. Weigend, A first application of independent component analysis to extracting structure from stock returns, International Journal of Neural Systems 8 (4) (1997) 473 – 484.

[2] L. Chan, J. Karceski, J. Lakonishok, On portfolio optimization: forecasting covariances and choosing the risk model, The Review of Financial Studies 12 (5) (1999) 937 – 974.

[3] M. Choey, A.S. Weigend, Nonlinear trading models through Sharpe ratio optimization, International Journal of Neural Systems 8 (3) (1997) 417–431.

[4] M. Dungey, V. Martin, A. Pagan, A multivariate latent factor decomposition of international bond yield spreads, Journal of Applied Econometrics 15 (2000) 697– 715.

[5] P.C. Fishburn, Mean-risk analysis with risk associated with below target returns, The American Economic Review 67 (2) (1977) 116 – 126.

[6] A. Harvey, E. Ruiz, E. Sentana, Unobserved component time series models with ARCH disturbances, Journal of Econometrics 52 (1992) 129–157.

[7] M. Haugh, A. Lo, Computational challenges in portfolio management, Computing in Science and Engineering 3 (3) (2001) 54– 59.

[8] K.K. Hung, C.C. Cheung, L. Xu, New Sharpe-ratio-related methods for portfolio selection, Proceedings of Computational Intelligence for Financial Engineering (CIFEr 2000) (2000) 34– 37.

[9] K.K. Hung, L. Xu, Further improvement of adaptive supervised learning decision (ASLD) network in stock market, Proceedings of the International Joint Conference on Neural Networks (IJCNN’99) 6 (1999) 3860 – 3865.

[10] K.G. Jo¨ reskog, A.S. Goldberger, Factor analysis by general ized least squares, Psychometrika 37 (1972) 243 – 260.

[11] H. Markowitz, Portfolio Selection: Efficient Diversification of Investments, Wiley, New York, 1959.

[12] J. Moody, L. Wu, Y. Liao, M. Saffell, Performance functions and reinforcement learning for trading systems and portfolios, Journal of Forecasting 17 (1998) 441–470.

[13] R. Neuneier, Optimal asset allocation using adaptive dynamic programming, Advances in Neural Information Processing Systems 8 (1996) 952–958.

[14] R. Roll, S. Ross, An empirical investigation of the arbitrage pricing theory, Journal of Finance 35 (1980) 1073 – 1103.

[15] R. Roll, S. Ross, The arbitrage pricing theory approach to strategic portfolio planning, Financial Analysts Journal 40 (1984) 14– 26.

[16] S. Ross, The arbitrage theory of capital asset pricing, Journal of Economic Theory 13 (1976) 341–360.

[17] W.F. Sharpe, Mutual fund performance, Journal of Business 39 (1966) 119– 138.

[18] L. Xu, Temporal BYY learning for state space approach, hidden markov model and blind source separation, IEEE Transactions on Signal Processing 48 (2000) 2132– 2144.

[19] L. Xu, BYY harmony learning, independent state space and generalized APT financial analyses, IEEE Transactions on Neural Networks 12 (4) (2001) 822–849.

[20] L. Xu, RBF nets, mixture experts, and Bayesian Ying – Yang learning, Neurocomputing 19 (1998) 223 – 257.

[21] L. Xu, Y.M. Cheung, Adaptive supervised learning decision networks for traders and portfolios, Journal of Computational Intelligence in Finance 5 (6) (1997) 11 – 15.

[22] F. Yip, L. Xu, An application of independent component analysis in the arbitrage pricing theory, Proceedings of the International Joint Conference on Neural Networks (IJCNN’2000) 5 (2000) 279– 284.

Kai-Chun Chiu received his BBA (Hon.) in accountancy from the Chinese University of Hong Kong in 2000. He is a member of Beta Gamma Sigma. He is currently a PhD student of the Department of Computer Science and Engineering, the Chinese University of Hong Kong.

Lei Xu is a chair professor in the Department of Computer Science and Engineering of the Chinese University of Hong Kong. He has been concurrently a full professor at Peking University since 1992, and guest professor at three other universities in China and the United Kingdom. After completing his PhD thesis in Tsinghua University by the end of 1986, he joined Peking University in 1987 first as a postdoc and then became one of a few exceptionally promoted young associate professors of the university in 1988. During 1989 – 1993, he worked as postdoc or senior research associate in several universities in Europe and North America, including Harvard and MIT. Prof. Xu is a governor of the International Neural Network Society, the chair of the Computational Finance Technical Committee of the IEEE Neural Networks Society, a past president of Asia – Pacific Neural Networks Assembly, and an associate editor for six international journals on neural networks, including Neural Networks and IEEE Transactions on Neural Networks. He has published more than more than 240 papers in refereed journals, edited books and international conferences, with a number of them being well-cited contributions. He has received several Chinese national prestigious academic awards, including 1994 Chinese National Nature Science Award, and 1988 Chinese State Education Council Fok Ying Tung Award, and international awards (including an 1995 INNS Leadership Award). In addition, he has given over 40 keynote/plenary/invited/tutorial talks in international major neural networks conferences, such as ICONIP, WCNN, IEEE-ICNN, IJCNN, etc. He was an ICONIP’96 Program Committee Chair, a Joint-ICANN-ICONIP03 Program Committee co-chair and a general chair of IDEAL’98, IDEAL’00, IEEE CIFER’03 and IEEE FE04. Prof. Xu is an IEEE fellow, a fellow of the International Association for Pattern Recognition and a member of the European Academy of Sciences.
