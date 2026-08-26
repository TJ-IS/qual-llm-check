---
otero_id: 19798
otero_key: "GBHTHZV6"
title: "New algorithms for automatic modelling and forecasting of decision support systems"
authors: "Diego J. Pedregal"
year: "2021"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2021.113585"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# New algorithms for automatic modelling and forecasting of decision support systems

Diego J. Pedregal

ETSI Industriales de Ciudad Real & Institute of Applied Mathematics in Science and Engineering (IMACI), Universidad de Castilla-La Mancha, 13071 Ciudad Real, Spain

## A R T I C L E I N F O

Keywords: Decision support system Unobserved components model State space systems Kalman filter Forecasting Maximum likelihood

## A B S T R A C T

Decision support systems often rely on time series forecasting, making the accuracy of such systems of paramount importance for their efficiency. Since most systems nowadays require the processing of massive amount of data, automatic identification of time series models has become inevitable. This automatism is inherent in artificial intelligence methods, but it often goes unnoticed that forecasting ‘classical’ methods have also been developing their own automatic methods for a long time. The radical novelty of this paper is the development of a brand new algorithm for identification of structural Unobserved Components models from which decision support systems may benefit. A second point is that combination of forecasts is more fruitful than competition or method selection in some cases. Both points are illustrated in two examples that show the effectiveness of the identification procedure and the forecasting gains when fairly different methods are combined.

## 1. Introduction

The fact that decision support systems (DSS) often rely on time series forecasting makes the accuracy of forecasting methods a key issue in improving the efficiency of such systems. To achieve that end many different forecasting methods have been tried in the past. Undoubtedly, the two forecasting methods with the longest tradition are ExponenTial Smoothing (ETS) and ARIMA models, both with accompanying auto matic identification procedures [5,12,20,22]. Other methods, like Theta [3], have become widespread after participation in M-# forecasting competitions [28,29,31].

More recently, the irruption of Deep Learning (DL) methods in the area of time series forecasting is producing several types of reactions. On the one hand. some researchers see marked differences between statistical’, ‘classical’ or ‘traditional’ methods versus ‘modern’ or ‘new ones, to the point of proposing the need to choose one and reject the others. On the other hand, others develop hybrid methods, taking advantage of and combining ‘statistical’ and ‘modern’ techniques as building blocks of an overall complex system, (see e.g., [2,29–31,35]).

Be that as it may, such is the need to generate fast and reliable forecasts from these huge amounts of data that manual identification of models is unfeasible. This is the case for many DSS that are based on time series forecasting (see e.g., [1,6,10,13,27,37]).

In this scenario, there is one methodology that has been systemati cally overlooked for several reasons, namely, Unobserved Component (UC) models ([9,16,38], and many others). Of all the reasons that can be cited for this omission, the most relevant for this work is the lack of an automatic identification algorithm that would make the use of UCs as flexible as its natural competitors. In fact, having such an identification procedure would allow to claim UC models not only as a useful fore casting tool (such as ETS, ARIMA or Theta), but also as an automatic formal signal extraction method to perform important tasks, such as seasonal adjustment, de-trending, cycle analysis, etc. This is important to overcome the limitations of ad-hoc methods, like the widespread use of moving averages and others.

Putting together everything said so far, the objective of this paper is twofold, from which DSS can benefit. First, to develop automatic iden tification algorithms for structural UC models (UCA hereafter) and to test them on both intensive-individual time series and large sales data sets. Second, to demonstrate that forecast combinations of different methods improve forecasting accuracy in sales datasets typical of many DSS, implying that, at least in some cases, a reconciliation strategy such as method combination outperforms method selection.

The remainder of the paper is organized as follows. Section 2 provide a general overview of UC models. Sections 3 presents UCA and the complexity of setting it up. Section 4 shows UCA working on two real examples. Finally, Section 5 offers some final remarks and conclusions.

## 2. Unobserved components models

The UC models aims at decomposing a time series into meaningful components. A common decomposition is shown in Eq. (1), where $T _ { t } , C _ { t }$ $S _ { t } ,$ and I stand for a trend, cycle, seasonal, irregular components, respectively. The model allows also for linear relationships with k exogenous variables $x _ { i , \ t }$ affected by a set of parameters $\beta _ { i } , ( i = 1 , . . . , k )$

$$
z _ {t} = T _ {t} + C _ {t} + S _ {t} + I _ {t} + \sum_ {i = 1} ^ {k} \beta_ {i} x _ {i, t}\tag{1}
$$

Structural methods take Eq. (1) as the base model (it is actually the observation equation of a State Space (SS) system, see below) and directly specify the dynamic models for each of the components, for which there is a wide range of possibilities.

Once a model is chosen for each component listed in the previous Section, a complete SS model is assembled by block concatenation of the individual SS models. The well-known Kalman filter and associated smoothing algorithms provide the basis for a wide range of operations, like parameter estimation $ { \mathbf { b } } \mathbf { y }$ Maximum Likelihood, estimation of state and their covariance matrices, interpolation, signal extraction, etc. The particular approach in this paper stem from a long tradition, see e.g., Harrison and Stevens [15]; Harvey [16]; de Jong [23]; Young et al. [40]; Durbin and Koopman [9].

The following subsections show the particular models of each type of component used in this paper.

## 2.1. Trend components

All trends considered are particular cases of the Generalised Random Walk model (or Damped Trend, DT) shown in Eq. (2), where $T _ { t } { ^ { * } }$ is usually referred to as the trend ‘slope’, $0 \leq \alpha \leq 1 , \eta _ { T , }$ and $\eta _ { T , \ t } { ^ { * } }$ are independent Gaussian white noise sequences with variances $\sigma _ { \eta T } ^ { 2 }$ and $\sigma _ { \eta T } \dot { \ast } ^ { \bar { 2 } }$ , respectively.

$$
\left[ \begin{array}{c} T _ {t + 1} \\ T _ {t + 1} ^ {*} \end{array} \right] = \left[ \begin{array}{c c} 1 & 1 \\ 0 & \alpha \end{array} \right] \left[ \begin{array}{c} T _ {t} \\ T _ {t} ^ {*} \end{array} \right] + \left[ \begin{array}{c} \eta_ {T, t} \\ \eta_ {T, t} ^ {*} \end{array} \right]\tag{2}
$$

This model subsumes the following particular cases: i) Random Walk (RW), setting $\alpha = 0 , \sigma _ { \eta _ { T } } \ast { } ^ { 2 } = 0$ and $T _ { 1 } { ^ * } = 0 ;$ ii) RW with drift, same as previous, but with $T _ { 1 } { ^ * } \neq$ 0; iii) Integrated Random Walk (IRW) with $\alpha =$ 1 and ${ \sigma _ { \eta _ { T } } } ^ { 2 } = 0 .$ , (it is equivalent to the well-known Hodrick-Prescott filter, $[ 1 9 , 4 0 ] ) ;$ iv) Local Linear Trend (LLT) with $\alpha = 1 ,$ , (see $\mathbf { e } .  g . , \ [ 9 , 1 6 , 3 6 ] )$ .

## 2.2. Cyclical components

Cycles are taken from Harvey [16] and obey Eq. (3). Here, $C _ { t } { } ^ { * }$ is an additional state necessary to define the model; $\rho$ is a damping factor taking values between 0 and 1; ω is the frequency of the cycle, namely ω $= 2 \pi / P ,$ , where P is the period (the number of observations per one full oscillation); and $\eta _ { t }$ and ${ { \eta } _ { t } } ^ { * }$ are mutually independent Gaussian white noises with common variance $\sigma _ { \eta } ^ { 2 } .$

$$
\left[ \begin{array}{c} C _ {t + 1} \\ C _ {t + 1} ^ {*} \end{array} \right] = \rho \left[ \begin{array}{c c} \cos \omega & \sin \omega \\ - \sin \omega & \cos \omega \end{array} \right] \left[ \begin{array}{c} C _ {t} \\ C _ {t} ^ {*} \end{array} \right] + \left[ \begin{array}{c} \eta_ {t} \\ \eta_ {t} ^ {*} \end{array} \right]\tag{3}
$$

## 2.3. Seasonal components

Seasonal components considered in this paper are of the trigono metric class proposed by Harvey [16]. The formulation is essentially the same as the cycle with $\rho = 1$ and adding all the harmonics of the fundamental frequency/period. Calling s the known seasonal period (the number of observations per year), the number of harmonics in general is $[ s / 2 ] = s / 2$ for even s numbers, and $[ s / 2 ] = ( s - 1 ) / 2$ for uneven s numbers.

The overall seasonal component is then the sum of all the sinusoidal harmonics $s _ { j , \textit { t } }$ in Eq. $^ { ( 4 ) }$ where $\omega _ { j } = 2 \pi j / s$ is the frequency of each harmonic, $S _ { j , t } { ^ { * } }$ is an additional state necessary for the specification, and $\eta _ { j , \mathrm { ~ } }$ <sub>t</sub> and $\eta _ { j , \ t } { } ^ { * }$ are independent white noises with common variance $\sigma _ { j } ^ { 2 } .$

$$
\begin{array}{c} S _ {t} = \sum_ {j = 1} ^ {[ s / 2 ]} S _ {j, t} \\ \left[ \begin{array}{l} S _ {j, t + 1} \\ S _ {j, t + 1} ^ {*} \end{array} \right] = \left[ \begin{array}{c c} \cos \omega_ {j} & \sin \omega_ {j} \\ - \sin \omega_ {j} & \cos \omega_ {j} \end{array} \right] \left[ \begin{array}{l} S _ {j, t} \\ S _ {j, t} ^ {*} \end{array} \right] + \left[ \begin{array}{l} \eta_ {j, t} \\ \eta_ {j, t} ^ {*} \end{array} \right] \end{array}\tag{4}
$$

It is common to consider two simplifying assumptions when dealing with seasonal components, like are the cases of the popular Basic Structural Model with trigonometric seasonality (BSM) from Harvey [16] or the exponential smoothing models, such us Hyndman et al. [22]. The first constraint is that all harmonics are present in every seasonal component. The second is that one single variance represents the sea sonal component, which implies that all harmonics are constrained to have one common variance or the same power in spectral terms $( \mathrm { i . e . , } \sigma _ { j } ^ { 2 }$ $= \sigma ^ { 2 } , j = 1 , 2 , . . . , [ s / 2 ] \big )$ ). This assumption was relaxed by Young et al. [40] and is also relaxed here.

## 2.4. Irregular components

The irregular component is usually considered as a residual component obtained after the extraction of the rest of components. Very often, it is just serially independent white noise with constant variance $\sigma _ { I } ^ { 2 } .$ But sometimes it exhibits some remaining autocorrelation. In such cases, coloured irregular components may be considered in the form of $\mathbf { A R M A } ( p , q )$ processes that should be both stationary and invertible in order to avoid identification problems with the rest of components.

## 2.5. Input-output relations

The UC model may include relations with exogenous variables naturally. But this should be done with care, since identification prob lems may appear especially in cases where the inputs themselves are affected by trend or seasonality. Such problems usually do not appear when the inputs are stationary (i.e., they do not mingle with the trend component) and non-seasonal $( \mathrm { i . e . , }$ there is no confusion with the sea sonal component). Typically, deterministic variables, such as calendar variables, moving festivals. or general intervention variables to deal with outlying observations are ideal candidates to consider.

## 3. An automatic identification algorithm for UC

The automatic algorithm proposed below, UCA, is based on infor mation criteria and performs remarkably well in practice, as will be shown in later worked examples. It adopts three possible versions, one full that involves estimation of all possible models, a stepwise with unit root tests and stepwise without unit root tests. The stepwise versions try to reduce the number of models to estimate in order to improve iden tification speed without a loss of efficiency for situations where computing time is important. To the author knowledge this is the first time that an algorithm of this nature is proposed in the UC literature.

A critical issue is the selection of the model population for each of the components from the whole universe of possibilities. It should be large enough to be able to represent as many different types of time series as possible, although irrelevant choices should be kept out to avoid an unmanageable increase in computing times.

The specific options considered in this paper are listed in Section 2 and summarized here: i) trends may be either none, RW, DT or LLT; ii) cycles may be none, one or several cycles and the user should decide whether the periods are known or should be estimated jointly with the rest of parameters; iii) seasonal components may be either none, trigo nometric with one single variance for all harmonics, or with a different variance for each of them; iv) irregular may be none or white noise.

The total number of possible combinations in this module are 23 when no cycle is required $( 4 \times 3 \times 2 - 1$ , minus one because no trend, no seasonal and no irregular is not a model) or 47 with cycles included. These numbers may be reduced considerably if any of the components is fixed when additional information is available. It is the case when the data is non-seasonal (then the search reduces to non-seasonal models), and/or stationary (trends are removed from the search).

The algorithm proceeds sequentially in modules explained in the next subsections.

## 3.1. Module 1: pre-testing

At this initial stage one compulsory seasonality test and one optional unit root-test are run. The former is to discard seasonal harmonics not present in the seasonal component, while the latter discerns whether the time series is stationary or not.

The seasonal test is based on the standard t-statistic values in a harmonic regression with a third order polynomial trend, see Eq. (5), where $\alpha _ { i } , ( i = 0 , 1 , 2 , 3 )$ , a<sub>j</sub> and $b _ { j } , ( j = 1 , 2 , . . . , [ s / 2 ] )$ ) are parameters to estimate (with $b _ { [ s / 2 ] } = 0$ since $s i n ( \pi ) = 0 )$ and $\epsilon _ { t }$ is assumed white noise with mean zero and constant variance.

$$
z _ {t} = \sum_ {i = 0} ^ {3} \alpha_ {i} t ^ {i} + \sum_ {j = 1} ^ {[ s / 2 ]} \left[ a _ {j} \cos (2 \pi j t / s) + b _ {j} \sin (2 \pi j t / s) \right] + \epsilon_ {t}\tag{5}
$$

A harmonic j is included in the subsequent seasonal component if any of the parameters a and b or both have a t-statistic greater than 1.645 in absolute value, corresponding to a two sided t-test at an approximately 10% significance, assuming Gaussianity.

The outcome of this test is used in different ways, depending on the type of algorithm selected, $\mathrm { i . e . , i }$

• Full algorithm: the test implied by Eq. (5) is run only to discard irrelevant harmonics in the seasonal component, but the next mod ules proceed with all possible combinations of components.

• Stepwise without unit root test: same as full, but a conclusive har monic test is used to decide whether a seasonal component is present in the data or not and proceed accordingly in next modules. The seasonal component is considered present in the data if at least one ttest is greater than 3 (therefore, non-seasonal models are discarded in later modules); no seasonal component is included if all the t-tests are smaller than 1.645 (seasonal models are discarded); and the test is considered inconclusive if at least one of the tests fall in the range 1.645 to 3 and none is greater than 3 (both seasonal and nonseasonal models are included in later modules). Mind that, when seasonality is detected, the seasonal model in subsequent module may have all or just part of the harmonics.

• Stepwise with unit root tests: the harmonic regression in Eq. (5) is applied in the same terms as in the previous stepwise version. In addition, an augmented Dickey-Fuller test with the number of output lags identified by BIC determines the trend models to include in next modules. The series is classified as stationary if the t-test corre sponding to the first lag of the series is lower than − 5 (discarding trend models in next modules); non-stationary if test values greater than − 2 (stationary models are discarded); or undetermined if the ttest is between − 5 and − 2 (models with and without trends are included in next modules).

## 3.2. Module 2: model selection

A battery of models are estimated and the best is chosen according to the minimization of an information criterion, either Akaike's (AIC), corrected Akaike's (AICc), or Bayesian's (BIC), i.e.,

$$
A I C = N ^ {- 1} \left[ - 2 \ln \left(L ^ {*}\right) + 2 k \right]
$$

$$
A I C c = A I C + \frac {2 k ^ {2} + 2 k}{N (N - k - 1)}
$$

$$
B I C = N ^ {- 1} \left[ - 2 \ln (L ^ {*}) + \ln (N) k \right]
$$

where $L ^ { * }$ is the likelihood value at the optimum, N is the length of the time series and k the number of parameters plus nonstationary states in the model.

The full version for this module is rather simple and consists of running all the models possible and selecting the best according to the information criterion chosen. This module may be run with or without simultaneous automatic detection of outliers.

The stepwise algorithm avoiding unit root testing involves the following steps:

• Step 1: all possible models are estimated combining the models for the components but with only two possible types of trends, namely none and RW. This is in fact an empirical way of testing for a unit root by means of information criteria alternative to the augmented Dickey-Fuller in Module 1. Two outcomes are possible: i) the best model is one with no trend, then the algorithm goes to Step 2; or ii) the best model includes a RW trend, in which case the algorithm proceeds to Step 3.

• Step 2: models with DT and combinations of the rest of components are estimated, selecting the best overall. Go to Module 3.

• Step 3: there is at least one unit root in the data. A second unit root is tested by running all the combinations of components with a LLT trend.

• Step 4: the models for the components already selected in steps 1 and 3 are combined with a DT trend. The overall best model is chosen. Go to Module 3.

The logic of this algorithm is clear, it keeps selecting the best trend at each step increasing the number of unit root in trend models. Steps 2 and 4 regarding DT trends are necessary, because in many real situations the DT came out as the best, regardless of the outcome of immediate pre vious steps.

If the unit root test option is chosen in Module 1 and the test is not conclusive, then Module 2 applies as is. On the contrary, if the unit root test is conclusive the stepwise procedure takes advantage of this infor mation. Two cases are possible: i) the series is stationary, then all possible combinations of components are tested with no trend; and ii) the series has at least one unit root, then Step 1 above runs only with models with RW trends, and Step 2 is skipped.

## 3.3. Module 3: ARMA model selection

Further improvements are possible by testing for any correlation left in the model innovations. This may be tracked by an identification procedure based on ARMA models. The orders must be limited to be smaller than the seasonal period to avoid identification problems with the seasonal component.

The algorithm used is a simplified version of Hyndman and Khan dakar [20] consisting on searching exclusively on stationary and nonseasonal models, since both non-stationarity and seasonality are assumed already captured by the trend and seasonal components. The procedure uses standard regression to increase speed by taking advan tage of the linear approximation proposed by Hannan and Rissanen [14], by which an initial noise estimation is obtained by fitting a long autoregressive model to the innovations identified by BIC.

## 3.4. Module 4: joint final estimation

If an ARMA model is detected as a result of the previous module, then the joint UC model with the ARMA irregular component embedded is

![](/api/attachments/GBHTHZV6/fulltext/images/409190cd5e5b768c97dfdf0b4f7364cdbd39df0be112302057173d9348d5725d.jpg)  
Fig. 1. Monthly Spanish Industrial Production Index from 2000 to 2019.

estimated.

This module applies whenever an ARMA structure is found for the model innovations. The joint estimation of UC models with ARMA in novations should be exercised with care to avoid identification problems among components. Indeed, ARMA components should be estimated imposing stationarity and invertibility constraints to avoid identification problems with the trend component or unit root cancellations with the rest of components.

One approach to deal with this problem was proposed by Monahan [32], that allows to transform any set of p unconstrained real values into an appropriate AR polynomial with all its roots outside the unit circle. This is done in two steps: i) the unconstrained parameter values are mapped into the interval (− 1, 1) individually, and ii) such values are considered the first p coefficients of a partial autocorrelation function of an AR(p) model and are converted into the polynomial coefficients by reversing the recursive solution to the Yule-Walker equations for pure AR models.

## 3.5. Module 5: final model selection

The best final model is selected between those of modules 2 and 4, depending on which one exhibits the smallest information criterion.

## 3.6. Further issues

Any of the UCA versions (full or either stepwise) may be run including additional features: i) Exogenous inputs that are concentrated out of the likelihood by the augmented Kalman filter [23]; ii) one or several cycles Harvey [16]; and iii) automatic outliers detection, based on the procedure by Havey and Koopman [17] for additive outliers, slope changes and level shifts.

Implementing a fully automatic algorithm for general UCs like UCA is a complex road full of pitfalls, because there are many details on which the success of such a complex system depends. There are many technicalities that make the procedure faster and more robust, and they may only be found in a long list of papers and books. The following can be considered a non-exhaustive list included in the particular imple mentation used in this paper [34]: use of augmented recursive algo rithms in the case of models with inputs; exact initialisation of recursive algorithms; use of profile diffuse log likelihood objective function that reduces the parameter space in one element in univariate models and k + 1 elements in models with inputs; use of analytical likelihood gradi ents whenever possible; constrained estimation of unconstrained pa rameters by appropriate transformations (variances are positive, some parameters must be between 0 and 1, ARMA models should be sta tionary and invertible, etc.); development of a Quasi-Newton algorithm for likelihood maximization that allows to impose constraints on pa rameters on the fly when they reach the boundaries or to switch the concentrated variance parameter when it turns out to be zero; careful selection of initial conditions for parameter search, etc.

## 4. Worked examples

The examples in this Section illustrate UCA described in previous sections working on real data. Forecasting comparisons with other standard and well-established methodologies are included, namely ARIMA, ETS and Theta. For these cases, forecast package in R and ECOTOOL toolbox in MATLAB are used [20,33].

Comparisons among methods are based on usual error metrics, some of them absolute, like the Mean Error (ME), Root Mean Squared Error (RMSE) and Mean Absolute Error (MAE), and some other metrics rela tive to actual values in different ways, namely the Mean Absolute Scaled Error (MASE) [21] and symmetric Mean Absolute Percentage Error (sMAPE) [28]. Formulae for the last two metrics is shown in Eqs. (6) and (7), where ${ \boldsymbol { z } } _ { t }$ and $\widehat { \boldsymbol { z } } _ { t }$ are the actual and forecast values at time t, respectively; N is the forecast origin and the number of observations in the fitting sample; s is the seasonal period; and h is the forecasting horizon.

$$
M A S E _ {h} = h ^ {- 1} \sum_ {i = 1} ^ {h} \frac {\left| z _ {T + i} - \widehat {z} _ {T + i} \right|}{(N - 1) ^ {- 1} \sum_ {r = s + 1} ^ {N} \left| z _ {r} - z _ {r - s} \right|}\tag{6}
$$

$$
s M A P E _ {h} = h ^ {- 1} \sum_ {i = 1} ^ {h} \frac {2 \left| z _ {T + i} - \widehat {z} _ {T + i} \right|}{\left| z _ {T + i} \right| + \left| \widehat {z} _ {T + i} \right|} \times 1 0 0\tag{7}
$$

## 4.1. Spanish Industrial Production Index (IPI)

UCA is shown working at full on the monthly Spanish Industrial Production Index (IPI) from January 2000 to December 2019, shown in Fig. 1. The data exhibit a typical strong seasonal pattern together with sharp changes in 2008 as a consequence of the previous recession.

Typical inputs to this sort of data are calendar effects, mainly moving Easter festival and trading days. Many different definitions may be provided for these two variables, the ones used here are:

• Easter effect measured as the proportion of public holidays, from Thursday to Easter Sunday, that falls in March and April each year.

• Trading days effect corrects for different proportions of working days and weekends in each month. The variable is the number of working days minus the number of Saturdays and Sundays multiplied by 5/2.

To illustrate UCA working with different settings, it is run four times with different levels of complexity: i) as is; ii) including Easter and trading effects as exogenous inputs; iii) including automatic detection of outliers; iv) including both inputs effects and outliers.

Summary of statistics for four runs of the identification algorithm. Q(12) stand for the Ljung-Box autocorrelation statistic on innovations for 12 lags and H(78) is the variance ratio between the first and the third thirds of the sample.

<table><tr><td rowspan="2"></td><td rowspan="2">Univariate</td><td>Model</td><td>Model</td><td>Model</td></tr><tr><td>with inputs</td><td>with outliers</td><td>with both</td></tr><tr><td>Log-Lik</td><td>374.922</td><td>484.339</td><td>387.355</td><td>501.195</td></tr><tr><td>AIC</td><td>-2.966</td><td>-3.903</td><td>-3.061</td><td>-3.985</td></tr><tr><td>AICc</td><td>-2.954</td><td>-3.895</td><td>-3.049</td><td>-3.964</td></tr><tr><td>BIC</td><td>-2.691</td><td>-3.671</td><td>-2.770</td><td>-3.651</td></tr><tr><td>Q(12)</td><td>22.163</td><td>16.188</td><td>18.480</td><td>6.964</td></tr><tr><td>H(78)</td><td>0.690</td><td>0.851</td><td>0.696</td><td>0.821</td></tr></table>

Mean of MASE metrics for 1 to 12 steps ahead forecasts of Spanish IPI data based on forecasts run at moving forecasting origins starting on January 2015. B&J stands for ARIMA models and B&J\* for ARIMA models identified with ECOTOOL

<table><tr><td>h</td><td>B&amp;J</td><td>Theta</td><td>ETS</td><td>UCA</td><td>BSM</td><td>B&amp;J*</td><td>B&amp;J</td><td>UCA</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td colspan="2">with outliers</td></tr><tr><td>1</td><td>0.556</td><td>0.597</td><td>0.614</td><td>0.517</td><td>0.584</td><td>0.573</td><td>0.288</td><td>0.281</td></tr><tr><td>2</td><td>0.551</td><td>0.580</td><td>0.583</td><td>0.508</td><td>0.558</td><td>0.558</td><td>0.319</td><td>0.302</td></tr><tr><td>3</td><td>0.551</td><td>0.569</td><td>0.573</td><td>0.508</td><td>0.546</td><td>0.563</td><td>0.347</td><td>0.322</td></tr><tr><td>4</td><td>0.564</td><td>0.570</td><td>0.576</td><td>0.521</td><td>0.546</td><td>0.565</td><td>0.368</td><td>0.338</td></tr><tr><td>5</td><td>0.578</td><td>0.570</td><td>0.581</td><td>0.528</td><td>0.545</td><td>0.568</td><td>0.381</td><td>0.348</td></tr><tr><td>6</td><td>0.593</td><td>0.576</td><td>0.591</td><td>0.536</td><td>0.549</td><td>0.579</td><td>0.393</td><td>0.358</td></tr><tr><td>7</td><td>0.601</td><td>0.580</td><td>0.599</td><td>0.536</td><td>0.550</td><td>0.580</td><td>0.399</td><td>0.360</td></tr><tr><td>8</td><td>0.610</td><td>0.586</td><td>0.600</td><td>0.537</td><td>0.552</td><td>0.584</td><td>0.407</td><td>0.363</td></tr><tr><td>9</td><td>0.612</td><td>0.584</td><td>0.598</td><td>0.533</td><td>0.546</td><td>0.576</td><td>0.410</td><td>0.366</td></tr><tr><td>10</td><td>0.626</td><td>0.596</td><td>0.615</td><td>0.544</td><td>0.553</td><td>0.585</td><td>0.411</td><td>0.370</td></tr><tr><td>11</td><td>0.635</td><td>0.605</td><td>0.627</td><td>0.549</td><td>0.555</td><td>0.590</td><td>0.415</td><td>0.375</td></tr><tr><td>12</td><td>0.647</td><td>0.611</td><td>0.629</td><td>0.554</td><td>0.556</td><td>0.598</td><td>0.418</td><td>0.378</td></tr></table>

The properties of the estimated models are similar: all the harmonics are included in the models according to the output of the harmonic regression in Module 1; the trend follows a RW in all cases; the seasonal component has different variances for all harmonics except in the model including the inputs effects; the irregular is white noise. A summary of statistics for these four models is shown in Table 1. Both stepwise procedures produced the same output than the full algorithm in all cases with an approximate computing time reduction of 30%.

Table 1 illustrates how model complexity is rewarded in terms of objective functions, costs and diagnostic statistics. All models outper form the univariate one consisting on a raw application without any aid of inputs or outliers detection. The biggest improvement is when the Easter and trading effects are included in the model, actually this is the best according to BIC. However, according to AIC and AICc the best of all is clearly the one on the last column that is preferred mainly because all the inputs effects and outliers are highly significant (the smallest t-test of all is 4.58).

Forecasting performance is tested based on a rolling experiment for 12 months ahead forecasts, starting on January 2015 and moving one month at a time with re-identification of all models at each single step. The central section of Table 1 shows the mean of all the MASE metric for ARIMA (shown as B&J), Theta and ETS, UCA, BSM (with a RW trend) and ARIMA using the particular implementation of the identification algorithm of Hyndman and Khandakar [20] in ECOTOOL (B&J\*, [33], available at https://github.com/djpedregal/ECOTOOL). The right sec tion of the table shows additional results for ARIMA (also implemented in ECOTOOL) and UCA with automatic modelling of outliers. Results according to other error metrics provided the same results and are not shown to save space.

Results show clearly several facts: i) the methods classification in the central section of Table 2 are in favour of UCA, followed by BSM, and the rest with varying performance depending on the forecasting horizon; ii) the ARIMA implementation in ECOTOOL (B&J\*) is better than the same implementation in B&J for horizons longer than 4 months; iii) any model including outlier detection improve forecasting performance drastically and UCA with outliers outperforms B&J still further.

## 4.2. Retailer sales

This example includes the daily sales of all categories sold by a department store in Spain along 15 full weeks (878 items). Fig. 2 shows some typical examples.

All time series are forecast the last 14 days available in the sample with the same methods as in the previous example, adding a recurrent neural network of the Long-Short Term Memory (LSTM) class, usually considered as a good predictor in multivariate contexts

![](/api/attachments/GBHTHZV6/fulltext/images/c126b5dc3f776ece828a3e62047621d3bdcce4a84f9841564de5a87b4f3855da.jpg)  
Fig. 2. Some examples of retailer sales.

Table 3  
Hyperparameter search space and optimum values selected

<table><tr><td>Hyperparameter</td><td>Search space</td><td>Optimum</td></tr><tr><td>Output lags</td><td>1, 2, 3, 7, 14, 15</td><td>14</td></tr><tr><td>Number of layers</td><td>2, 3, 4, 5</td><td>4</td></tr><tr><td>Number of neurons per layer</td><td>10, 30, 50, 75, 100</td><td>50</td></tr><tr><td>Drop out rate</td><td>0, 0.05, 0.1, 0.15</td><td>0.05</td></tr><tr><td>Epochs</td><td>200, 300, 400, 500</td><td>400</td></tr><tr><td>Learning rate</td><td>0.0005, 0.001, 0.005, 0.01</td><td>0.005</td></tr></table>

[4,7,18,26,31,35,41].

This type of recurrent neural network has ‘hidden’ and ‘cell’ states, which help in retaining short-term and long-term dependencies, respectively. In addition, several gates are introduced, namely a forget, input and output gates. The first two control which part of the infor mation is to be removed or retained and the last one generates the output as a function of the information. The typical architecture of LSTM networks is already a classic and is omitted here, see details in Hochreiter and Schmidhuber [18] and Yunpeng et al. [41].

The dataset is divided into three splits as training, validation and testing sets. The testing split is the same as the rest of models (last 14 days) and the validation set is just the previous 14 days. Then, after a normalization of data between 0 and 1 using min-max scaling, the network is optimized by minimizing the mean squared error in the validation set, with a grid search of hyperparameters along the values shown in Table 3 (that also shows the optimal values of the hyper parameters). Only the lagged values of the time series are introduced as features to the network so that the network plays with the same set of information than the rest of methods. The search space comprises 7680 models and where conducted entirely in keras on top of Google Ten sorFlow in the Python environment [8].

As for the UC models. 18.7% of the cases where identified as stationary series with no trend, 20.2% with RW trends, and 61.1% with DT. The surprising fact is that none were identified as LLT, implying that the series do not exhibit big changes in the mean. As for seasonality, in 17.1% of the series no seasonality was detected, while 69.9% of the cases were modeled with the same variance for all harmonics and 13.0% with all variances different. As for the irregular components, the usual case is just white noise, with 93.2% of the cases, only one case with no irregular component, and the rest with some sort of AR process, most of them AR (1) (5.3%) and the rest AR(2) (1.5%).

The forecast results are reported in Table 4 for all the methods considered, including the LSTM, and the median of all of them, which is usually reported in the literature as an efficient way of combining forecasts coming from different sources [25]. These tables show the median values of the error metrics across all time series and several forecasting horizons, up to 14 days. Note that tables for MAE, and sMAPE are not presented to save space, as the conclusions are the same. Such information is available from the author upon request.

The ME metric is useful for testing forecasting bias, see the top panel of Table 4. Although it is difficult to draw any clear conclusion from this evidence, since all values are small with respect to the units of the variables, it can be said that all methods perform adequately and not systematic big bias is detected. There is no clear winning method for all forecasting horizons.

The variance of the errors can be investigated through the RMSE (middle panel of Table 4), and the evidence is clear, as UCA is the ab solute winner followed closely by Theta, Median and ETS depending on the forecasting horizon.

Regarding MASE, the best method is Median for several forecasting horizons. Median is also the second best, very close to the winner, in those cases where it is not the best. UCA is the second best for horizons longer than 4.

In contrast to some of the literature, LSTM does not perform particularly well on this dataset, even though some factors play in principle in favour of LSTM, such as the multivariate context, high volatility and short time series. However, the time series may be linear in general or not complex enough to take full advantage of LSTM models [39].

Testing for significant differences in forecasting performance is usually advocated [11]. In this paper rank tests are used, that have become a standard after the M3 forecasting competition (see e.g., [24,31], and references therein). Starting from a formal global test under the null hypothesis that all the methods are indistinguishable using a given error metric, it is also possible to test significance differ ences for pairs of methods. These pairwise comparisons are actually implemented graphically by plotting the mean and confidence band for each method. Methods with overlapping confidence bands are consid ered to have equal accuracy, whereas significant differences arise when the intervals do not overlap. In the same spirit, multiple tests against the mean rank may be displayed graphically by a control chart in which a center line and a confidence band are plotted, and the mean rank of individual methods performing significantly differently than the average fall outside that band (see [24], for details).

Median of different error metrics for the retailer data. Bold numbers indicate the best method for each forecasting horizon.

<table><tr><td>h</td><td>1</td><td>2</td><td>3</td><td>4</td><td>7</td><td>10</td><td>14</td></tr><tr><td>ARIMA</td><td>-0.674</td><td>0.345</td><td>-0.130</td><td>-0.695</td><td>0.118</td><td>-0.193</td><td>-0.254</td></tr><tr><td>Theta</td><td>-0.329</td><td>0.818</td><td>0.315</td><td>-0.356</td><td>-0.022</td><td>-0.147</td><td>-0.274</td></tr><tr><td>ETS</td><td>-0.189</td><td>0.919</td><td>0.476</td><td>-0.141</td><td>0.141</td><td>0.043</td><td>-0.283</td></tr><tr><td>UCA</td><td>-0.432</td><td>0.698</td><td>0.173</td><td>-0.052</td><td>0.102</td><td>0.035</td><td>-0.127</td></tr><tr><td>LSTM</td><td>0.073</td><td>0.858</td><td>0.314</td><td>-0.258</td><td>0.087</td><td>-0.015</td><td>-0.413</td></tr><tr><td>Median</td><td>-0.224</td><td>0.765</td><td>0.112</td><td>-0.374</td><td>-0.025</td><td>-0.086</td><td>-0.407</td></tr><tr><td colspan="8">Median of RMSE</td></tr><tr><td>ARIMA</td><td>7.283</td><td>10.296</td><td>10.501</td><td>10.658</td><td>11.855</td><td>12.379</td><td>12.585</td></tr><tr><td>Theta</td><td>6.690</td><td>9.394</td><td>9.943</td><td>10.362</td><td>11.234</td><td>11.943</td><td>12.062</td></tr><tr><td>ETS</td><td>7.123</td><td>9.532</td><td>10.379</td><td>10.518</td><td>11.117</td><td>11.830</td><td>12.315</td></tr><tr><td>UCA</td><td>6.426</td><td>9.384</td><td>9.890</td><td>9.783</td><td>10.126</td><td>11.173</td><td>11.382</td></tr><tr><td>LSTM</td><td>7.523</td><td>10.690</td><td>11.198</td><td>11.374</td><td>11.701</td><td>12.210</td><td>12.193</td></tr><tr><td>Median</td><td>6.821</td><td>9.502</td><td>10.119</td><td>10.226</td><td>11.086</td><td>11.706</td><td>11.779</td></tr><tr><td colspan="8">Median of MASE</td></tr><tr><td>ARIMA</td><td>0.704</td><td>0.757</td><td>0.789</td><td>0.795</td><td>0.791</td><td>0.800</td><td>0.817</td></tr><tr><td>Theta</td><td>0.642</td><td>0.775</td><td>0.758</td><td>0.780</td><td>0.758</td><td>0.789</td><td>0.788</td></tr><tr><td>ETS</td><td>0.661</td><td>0.751</td><td>0.764</td><td>0.776</td><td>0.750</td><td>0.786</td><td>0.772</td></tr><tr><td>UCA</td><td>0.668</td><td>0.771</td><td>0.757</td><td>0.760</td><td>0.743</td><td>0.772</td><td>0.766</td></tr><tr><td>LSTM</td><td>0.713</td><td>0.803</td><td>0.809</td><td>0.813</td><td>0.778</td><td>0.811</td><td>0.786</td></tr><tr><td>Median</td><td>0.655</td><td>0.753</td><td>0.745</td><td>0.763</td><td>0.733</td><td>0.757</td><td>0.756</td></tr></table>

![](/api/attachments/GBHTHZV6/fulltext/images/9332d3ef74001664e73169f38606dea14e26c893dcc2e97085cd21eef755c0c0.jpg)  
Fig. 3. Average ranks tests. Pairwise comparisons in top panel and comparisons against the mean in bottom panel.

Taking the MASE as the error metric, the overall test for all methods included in Table 4 is 154.62, the critical value at a significance level of 5% is calculated according to a Chi-squared with K − 1 degrees of freedom, where K is the number of methods. That value is 11.07 in this case, so the methods are significantly different overall. Repeating the tests for each forecasting horizon produces statistics with a minimum in 37.25, implying that the null is rejected in all cases, even applying Bonferroni corrections for multiple testing.

Multiple comparisons among methods are also depicted in Fig. 3, both against each other (top panel) and against the mean rank (bottom panel). In this figure, an additional method is added that consists of calculating the median of the forecasts excluding the ARIMA method (labeled M-ARIMA). Several facts emerge from this figure:

• The ARIMA model is significantly worse than the rest.

• The rank of the remaining individual methods from best to worse is UCA, LSTM, ETS, Theta. But, strictly speaking, the differences observed between these methods are not statistically significant or are not different to the mean rank.

• The best method is M-ARIMA, followed by Median. Both are un doubtedly significantly different from the rest, although they do not differ from each other.

These graphs show in essence that improving forecast performance significantly in contexts where many time series are available is a difficult task. Even the most complex and flexible methods, such as LSTM, are not able to improve upon them. Only the combination of all of them improves upon all of them separately, mainly because combining is a way do the forecasting exercise more robust. Therefore, rather than emphasizing the differences among methods of any kind, cooperation among them seems a better way forward, at least in this dataset.

One last point worth mentioning that is usually overlooked when it comes to deep learning models has to do with computation times. While individual methods, such as UCA, take about 3 min to compute forecasts for the 878 time series in this dataset, LSTM takes about 36 h on the same computer.

## 5. Conclusions

The efficiency of DSS in most business and industrial sectors depends on the accuracy of forecasting methods. There are many solutions available to achieve that end, some of them purely statistical, others based on machine or deep learning techniques, and even others that mix features of all of them in so-called hybrid methods.

This paper contributes to improve the efficiency of DSS in several ways. Firstly, by introducing for the first time in the literature an automatic identification algorithm for univariate structural UC models, UCA, based on statistical criteria, which is ready to be applied to any dataset of any size. The proposal is richer than many UC approaches considered in the literature. For example, the variety of models for in dividual components is wider and more flexible, one or several cycles can be included in the models, input-output relations are also allowed, the method may include automatic outlier detection, stepwise proced ures are implemented to make the identification faster, etc.

Secondly, the paper shows that all the algorithms embedded in UCA are able to produce an efficient and deep detailed analysis of a single time series with several peculiarities, such as outliers, input variables (e. g., Easter effect and other calendar effects), different variances for each harmonic in the seasonal component, etc.

A final take-away of this paper, which is often not sufficiently recognized in the literature, is that simple combinations of methods are more important than they appear at first glance. The last example in the paper shows how methods with similar accuracy on large datasets can easily be combined into a new method that outperforms all of them separately. Such a combination actually works as a mean to make forecasts much more robust.

Certainly, the research and examples in this paper show that DSS practitioners and researchers can improve the efficiency of their ana lyses by adopting UCA as another tool in their toolbox alongside othe well-established methods. They can also improve their results by testing whether combinations of different forecasting methods improve upon individual ones, especially when dealing with big datasets typical of DSS.

## Acknowledgements

This work was supported by the European Regional Development Fund and Junta de Comunidades de Castilla-La Mancha (JCCM/FEDER, UE) under the project with reference SBPLY/19/180501/000151 and by the Vicerrectorado de Investigacion ´ y Política Científica from UCLM through the research group fund program (PREDILAB; DOCM 26/02/ 2020 [2020-GRIN-28770].

## References

[1] A. Aksoy, N. Ozturk, E. Sucky, A decision support system for demand forecasting in the clothing industry, Int. J. Cloth. Sci. Technol. 24 (2012) 221–236.

[2] D. Arnott, S. Gao, Behavioral economics for decision support systems researchers, Decis, Support. Syst, 122 (2019) 113063

[3] V. Assimakopoulos, K. Nikolopoulos, The theta model: a decomposition approach to forecasting, Int. J. Forecast. 16 (2000) 521–530.

[4] K. Bandara, P. Shi, C. Bergmeir, H. Hewamalage, Q. Tran, B. Seaman, Sale Demand Forecast in E-Commerce using a Long Short-Term Memory Neural Network Methodology, 2019. CoRR abs/1901.04028. URL: http://arxiv.org/abs/1 901.04028, arXiv:1901.04028.

[5] G.E.P. Box, G.M. Jenkins, G.C. Reinsel, G. Ljung, Time Series Analysis: Forecasting and Control, John Wiley & Sons, 2015.

[6] C. Ching-Chin, A.I.K. Ieng, W. Ling-Ling, K. Ling-Chieh, Designing a decisionsupport system for new product sales forecasting, Expert Syst. Appl. 37 (2010) 1654–1665.

[7] G. Chniti, H. Bakir, H. Zaher, E-commerce time series forecasting using lstm neural network and support vector regression, in: Proceedings of the International Conference on Big Data and Internet of Thing, Association for Computing Machinery, New York, NY, USA, 2017, pp. 80–84.

[8] F. Chollet, et al., Keras, GitHub, 2015. URL, https://github.com/fchollet/keras.

[9] J. Durbin, S.J. Koopman, Time Series Analysis by State Space Methods, Oxford University Press. 2012.

[10] R. Fildes, P. Goodwin, M. Lawrence, The design features of forecasting support systems and their effectiveness. Decis, Support, Syst, 42 (2006) 351–361.

[11] T. Fischer, C. Krauss, Deep learning with long short-term memory networks for financial market predictions. Eur. J. Oper. Res, 270 (2018) 654–669.

[12] V. Gomez, ´ A. Maravall, Automatic modeling methods for univariate series, in: A Course in Time Series, John Wiley & Sons, Inc, 2001, pp. 171–201.

[13] Z. Guo, W. Wong, M. Li, A multivariate intelligent decision-making model for retail sales forecasting, Decis. Support. Syst. 55 (2013) 247–255

[14] E.J. Hannan, J. Rissanen, Recursive estimation of mixed autoregressive-moving average order, Biometrika 69 (1982) 81–94.

[15] P.J. Harrison, C.F. Stevens, Bayesian forecasting, J. R. Stat. Soc. Ser. B Methodol. 38 (1976) 205–247.

[16] A.C. Harvey, Forecasting, Structural Time Series Models and the Kalman Filter Cambridge University Press, 1989.

[17] A.C. Havey, S.J. Koopman, Diagnostic checking of unobserved components time

[18] S. Hochreiter, J. Schmidhuber, Long short-term memory, Neural Comput. 9 (1997) 1735–1780, https://doi.org/10.1162/neco.1997.9.8.1735.

[19] R.J. Hodrick, E.C. Prescott, Postwar u.s. business cycles: an empirical investigation, J. Money Credit Bank. 29 (1997) 1–16.

[20] R.J. Hyndman, Y. Khandakar, Automatic time series forecasting: the forecast package for r, J. Stat. Softw. 27 (2008) 1–22.

[21] R.J. Hyndman, A.B. Koehler, Another look at measures of forecast accuracy, Int. J. Forecast. 22 (2006) 679–688.

[22] R.J. Hyndman, A.B. Koehler, J.K. Ord, R.D. Snyder, Forecasting with Exponentia Smoothing: The State Space Approach, Springer Science and Business Media, 2008.

[23] P. de Jong, The diffuse kalman filter, Ann. Stat. 19 (1991) 1073–1083.

[24] A. Koning, P. Franses, M. Higon, H. Stekler, The m3 competition: statistical tests of the results, Int. J. Forecast. 21 (2005) 397–409.

[25] N. Kourentzes, D. Barrow, F. Petropoulos, Another look at forecast selection and combination: evidence from forecast pooling, Int. J. Prod. Econ. 209 (2019) 226–235. The Proceedings of the 19th International Symposium on Inventories.

[26] B. Lakshmanan, P.S.N. Vivek Raja, V. Kalathiappan, Sales demand forecasting using lstm network, in: S.S. Dash, C. Lakshmi, S. Das, B.K. Panigrahi (Eds.), Artificial Intelligence and Evolutionary Computations in Engineering Systems, Springer Singapore, Singapore, 2020, pp. 125–132.

[27] A. Loureiro, V. Migu´eis, L.F. da Silva, Exploring the use of deep neural networks for sales forecasting in fashion retail, Decis. Support. Syst. 114 (2018) 81–93.

[28] S. Makridakis, M. Hibon, The m3-competition: results, conclusions and implications, Int. J. Forecast. 16 (2000) 451–476.

[29] S. Makridakis, F. Petropoulos, Special issue: M4 competition, Int. J. Forecast. 36 (2020).

[30] S. Makridakis, E. Spiliotis, V. Assimakopoulos, The m4 competition: results, findings, conclusion and way forward, Int. J. Forecast. 34 (2018) 802–808.

[31] S. Makridakis, E. Spiliotis, V. Assimakopoulos, The M5 Accuracy Competition: Results, Findings and Conclusions, 2020.

[32] J.F. Monahan, A note on enforcing stationarity in Arma models, Biometrika 71 (1984) 403–404.

[33] D.J. Pedregal, Time series analysis and forecasting with ECOTOOL, PLoS One 14 (2019), https://doi.org/10.1371/journal. pone.0221238.

[34] D.J. Pedregal, UComp: Automatic Unobserved Components Models. R Package Version 1.1, 2020.

[35] S. Punia, S.P. Singh, J.K. Madaan, From predictive to prescriptive analytics: a datadriven multi-item newsvendor model. Decis, Support, Syst. 136 (2020) 113340

[36] C.J. Taylor, D.J. Pedregal, P.C. Young, W. Tych, Environmental time series analysis and forecasting with the captain toolbox, Environ. Model. Softw. 22 (2007) 797–814.

[37] M.A. Villegas, D.J. Pedregal, Supply chain decision support systems based on a novel hierarchical forecasting approach, Decis. Support. Syst. 114 (2018) 29–36.

[38] M.A. Villegas, D.J. Pedregal, Automatic selection of unobserved components models for supply chain forecasting, Int. J. Forecast. 35 (2019) 157–169. Specia Section: Supply Chain Forecasting.

[39] G. Xie, N. Zhang, S. Wang, Data characteristic analysis and model selection for container throughput forecasting within a decomposition-ensemble methodology, Transport. Res. Part E: LogisticsTransport. Rey. 108 (2017) 160–178.

[40] P.C. Young, D.J. Pedregal, W. Tych, Dynamic harmonic regression, J. Forecast. 18 (1999) 369–394.

[41] L. Yunpeng, H. Di, B. Junpeng, Q. Yong, Multi-step ahead time series forecasting for different data patterns based on lstm recurrent neural network. in: 14th Web Information Systems and Applications Conference, 2017, pp. 305–310.

Diego J. Pedregal is a Professor at the Business Administration Department of Uni versidad de Castilla-La Mancha (Spain). He received his first degree in Economics (Econometrics and Time series analysis) in June 1991 from the Universidad Autónoma de Madrid (UAM, Spain); his M.A. in Public Finance in June 1992 from the Institute for Fiscal Studies (Spain): his Ph.D. in March 1995 from the UAM: and enjoved a post-doc position at Lancaster University (UK). His research interests include the identification and estimation of linear and non-linear systems, state space methods applied to time series and fore casting, with applications to Economics and Engineering.
