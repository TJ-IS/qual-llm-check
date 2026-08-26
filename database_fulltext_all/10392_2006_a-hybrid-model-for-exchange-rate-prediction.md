---
otero_id: 10392
otero_key: "77S53DG7"
title: "A hybrid model for exchange rate prediction"
authors: "Huseyin Ince; Theodore B. Trafalis"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.09.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A hybrid model for exchange rate prediction

Huseyin Ince <sup>a</sup>, Theodore B. Trafalis <sup>b,\*</sup>

<sup>a</sup> School of Business Administration, Gebze Institute of Technology, Cay rova Fab. Yolu No:101 P.K:141 41400, Gebze, Kocaeli, Turkey <sup>b</sup> School of Industrial Engineering, University of Oklahoma, 202 West Boyd, Room 124, Norman, OK 73019, United States

Received 21 July 2004; received in revised form 30 August 2005; accepted 11 September 2005 Available online 20 October 2005

## Abstract

Exchange rate forecasting is an important problem. Several forecasting techniques have been proposed in order to gain some advantages. Most of them are either as good as random walk forecasting models or slightly worse. Some researchers argued that this shows the efficiency of the exchange market. We propose a two stage forecasting model which incorporates parametric techniques such as autoregressive integrated moving average (ARIMA), vector autoregressive (VAR) and co-integration techniques, and nonparametric techniques such as support vector regression (SVR) and artificial neural networks (ANN). Comparison of these models showed that input selection is very important. Furthermore, our findings show that the SVR technique outperforms the ANN for two input selection methods. <sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Exchange rate prediction; Neural networks; Support vector regression; Time series

## 1. Introduction

Exchange rate forecasting is an important problem that has been studied by researchers and practitioners extensively. It is argued that exchange rate market is very efficient. Therefore, it is difficult to make short term and long term forecasting efficiently [2,13,25,38]. Several techniques have been proposed and applied to exchange rate forecasting and estimation of the volatility in order to beat the random walk model. These techniques can be put into the following categories.

The first group of techniques uses the economic theory to understand the structural relations between exchange rate and other variables and also statistical methods which try to identify the structure of the serial correlation and nonlinearity in time series. They are in the family of parametric models. Econometric and time series models are widely applied to foreign exchange market. Several researchers criticized the forecasting performance of these techniques and some of them have found that the random walk model outperforms the econometric and time series techniques [18,25,38]. The reason is that most of the econometric models are linear and used under specific assumptions. For example, ARIMA models assume a linear relationship between the current value of the underlying variables and previous values of the variable and error terms. Time series models are highly nonlinear and the mean and variance of the series can change overtime. In order to overcome this difficulty, an autoregressive conditional heteroscedasticty (ARCH) model is introduced by Engle [16] and this model is generalized by Bollerslev [1]. Different implementation of GARCH models has been proposed in order to overcome some difficulties such as nonlinearities and long term memory [15,14].

Fernandes tested whether the conditional heteroscedasticty models (CHM) capture the nonlinearities in the data. Nine out of twelve currencies, CHM models are good approximations. This suggests that CHM captures substantially but not completely the nonlinearities in the data [18]. Furthermore, instead of using GARCH models, their extension such as FIGARCH and IGARCH models are used for forecasting the market exchange rate. In a recent paper, Vilasuso [43] showed that the FIGARCH model is better than IGARCH and GARCH models for capturing the salient feature of the exchange rate volatility. The FIGARCH model generates superior out of sample volatility forecasting. Some researchers argued that CHM type models are better than random walk model and others showed that the random walk model is as good as CHMs or better than CHM [2,13]. The smooth transition autoregressive model (STAR) and exponential smooth transition autoregressive model (ESTAR) have been used to discover the dynamics of exchange rate forecasting. The ESTAR model shows strong predictability at horizons of 2 to 3 years. However, it does not have this predictability for shorter horizons [25].

Nonparametric models have been used extensively the last decade. The reason is the development of new techniques in artificial intelligence and increasing power of computers. These techniques have been applied to several areas such as stock price prediction, option pricing, and credit risk scoring [5– 7,19,22,23,26,30,36,37,39]. Most widely used techniques are the multilayer perceptron (MLP), radial basis function (RBF) networks and recurrent networks. Because of the efficiency of the foreign exchange market it is difficult to use statistical methods to forecast the dynamic behavior of the time series. Therefore, it is not wise to use linear models. RBF networks were applied to \$US/\$NZ exchange rate forecasting and showed that RBF network outperforms the linear autoregressive (LAR) models [44]. In their paper, Yao and Tan compared the neural network model with technical forecasting for Swiss Franc and American Dollar and they concluded that it is not easy to forecast if the market is efficient [45]. In addition to this, ANN and chaotic models were compared with random walk model. Lisi and Schiavo [29] indicated that ANN and chaotic models outperform the random walk model. In the exchange rate market forecasting literature, neural networks have been used and argued by several researchers (for examples see Refs. [6,7,11,12,26,29,30,44,45]).

Recently, in classification and regression, a novel method which is called support vector machine (SVM)

has been developed by Vapnik and is used successfully in several classification and regression problems [9,42]. SVM uses the structural risk minimization theory [3,9,34] unlike other methods such as ANN and ARIMA that employ the empirical risk minimization theory. It has been shown that the SVM problem is a convex optimization problem which means that the optimal solution is global. On the other hand, an ANN model uses the backpropagation or its variant algorithm to find the optimal weights. The problem is nonconvex and it’s solution is in one of the local minima. Because of this, theoretically, the SVM algorithm is superior to the ANN model. This has also been proven experimentally [33,35]. Support vector regression (SVR) has been used to predict stock market indices such as NASDAQ and Dow Jones, and short term stock prices [23,36,37].

Our objective is to develop a two stage forecasting model. In the first stage, we propose an input selection process by using time series models such as autoregressive integrated moving average (ARIMA) and co-integration analysis. After determining the number of inputs in the first stage, we apply state of the art techniques, namely ANN and SVR. In this way, powerful side of time series models and artificial intelligence model are discovered. Since the ANN and SVR technique are data-driven, it is very crucial to determine the right inputs. In the estimation process, ANN, and SVR do not use any assumption regarding the distribution of the data. On the other hand, time series techniques use several assumptions about the data. Therefore, estimation and forecasting are based on these assumptions. This is a very important drawback. In order to overcome these difficulties, we propose a two stage algorithm.

The remainder of this paper is organized as follows. In Section 2, we explain the methodology. Section 3 gives experimental results. Finally, Section 4 concludes the paper.

## 2. Methodology

In this section, co-integration method, SVR and ANN models will be explained briefly. The first method is used to identify the relationship between dependent and independent variables which can be the lagged values of dependent variables or exogenous variables. Then, two machine learning techniques, multilayer perceptron (MLP), which uses the backpropagation algorithm [21] as a training algorithm and SVR will be applied to the model that we specified in the first stage.

## 2.1. Time series analysis

Two techniques can be adopted to determine the inputs of a forecasting model. One of them is to use the autoregressive integrated moving average (ARIMA) model which tries to find the optimal number of previous values of the dependent variable and random shocks. The second one is a vector autoregressive(VAR) model and co-integration analysis. Next we briefly explain these two methods.

The general autoregressive moving average (ARMA) model of a time series Y can be written as

$$
\begin{array}{c} y _ {t} = \delta + \phi_ {1} y _ {t - 1} + \phi_ {2} y _ {t - 2} + \ldots + \phi_ {p} y _ {t - p} + \varepsilon_ {t} \\ + \theta_ {1} \varepsilon_ {t - 1} + \theta_ {2} \varepsilon_ {t - 2} + \ldots + \theta_ {q} \varepsilon_ {t - q} \end{array}\tag{1}
$$

where $\varepsilon _ { t }$ is independent and identically distributed with mean 0 and variance $\sigma ^ { 2 }$ . This means there is a linear relationship among the past values and future values of Y and random shocks. In order to determine the order of ARIMA model, ACF and partial ACF are used in conjunction with the Akaike information (AIC) or Schwarz Bayes information (BIC) criterion. Augmented Dickey Fuller (ADF) test can be conducted to test the stationarity. The ARIMA model follows an iterative process of model identification, parameter estimation and diagnostic checking. More information in ARIMA models can be found in Ref. [20].

Co-integration analysis, introduced by Granger, is the determination of long run relationships in economics. The basic idea behind the co-integration is that, if two or more series move closely together, even though the series themselves are trended, the difference between them is constant [15].

Consider the following vector error correction model of order $p \colon$

$$
\Delta \mathbf {y} _ {t} = \alpha \beta^ {\prime} \mathbf {y} _ {t - 1} + \sum_ {j 0 1} ^ {p - 1} \Gamma_ {j} \Delta \mathbf {y} _ {t - 1} + \varepsilon_ {t}\tag{2}
$$

where $\boldsymbol { y } _ { t }$ is an $( n \times 1 )$ vector of I(1) variables, $\mathbf { \alpha } \mathbf { \alpha } \mathbf { \beta } _ { \mathbf { \alpha } } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha \alpha } \mathbf \mathbf { \alpha } \mathbf { \alpha \alpha } \mathbf \mathbf { \alpha } \mathbf { \alpha \alpha } \mathbf \mathbf { \alpha \alpha } \mathbf \mathbf { \alpha \alpha } \mathbf \alpha \mathbf \alpha \mathbf  \alpha \alpha \alpha \alpha \alpha \alpha \alpha \mathbf \alpha \alpha \alpha \alpha \beta \alpha \alpha \alpha \mathbf \alpha \alpha \alpha \alpha \alpha \mathbf \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \mathbf \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha $ is an $( n \times n )$ matrix such that the $( n \times r )$ matrices have rank $r , \ : \Gamma _ { j } , j = 1 , 2 , . . . , p - 1$ , are $( n \times n )$ parameter matrices, and $\mathbf { \delta } _ { \mathcal { E } _ { t } }$ is an $( n \times 1 )$ vector of white noise with a positive definite covariance matrix. If $\scriptstyle \partial < r < n$ , the variables in $\boldsymbol { y } _ { \mathrm { t } }$ are co-integrated with r co-integrating relationships $\boldsymbol { \beta } \mathbf { \check { y } } _ { t }$

In order to test the null hypothesis of no co-integration between the set of I(1) variables, the ordinary least squares (OLS) method can be used to estimate the parameters and then, the unit root test can be applied to residuals. Rejecting the null hypothesis of a unit root test is evidence in favor of co-integration. Johansen [24] proposed the maximum likelihood method to estimate the $\beta$ which can be derived as the solution of a generalized eigenvalue problem. Likelihood ratio tests of hypotheses about the number of co-integrating vectors can be based on these eigenvalues.

Our goal is to use the co-integration analysis to determine the order of the integration between variables if the co-integration exists. The major advantage of the time series models would be the identification of the independent variables in our models which will be explained next. We will employ the parametric models to choose the influential variables or previous values of the dependent variables.

## 2.2. Support vector regression

SVMs for classification and regression based on structural risk minimization are developed by Vapnik [42]. In the e-insensitive SVR, our goal is to find a function f(x) that has an e deviation from the actually obtained target $y _ { i }$ for all training data and at the same time is as flat as possible. Suppose f(x) takes the following form:

$$
f (x) = w x + b \quad \mathbf {w} \in X, b \in \Re .\tag{3}
$$

In the case where the constraints are infeasible, we introduce slack variables $\xi _ { i } , \xi _ { i } *$ . This case is called the soft margin formulation, and is described by the following problem.

$$
\begin{array}{l} \min \frac {1}{2} \left\| \mathbf {w} \right\| ^ {2} + C \sum_ {i = 1} ^ {l} (\xi_ {i} + \xi_ {i} *) \\ \text { Subject   to } \\ y _ {i} - \mathbf {w x} _ {i} - b \leq \varepsilon + \xi_ {i} \\ \mathbf {w x} _ {i} + b - y _ {i} \leq \varepsilon + \xi_ {i} * \\ \xi_ {i}, \xi_ {i} ^ {*} \geq 0 \\ C \succ 0 \end{array}\tag{4}
$$

where, C determines the trade-off between the flatness of the $f ( x )$ and the amount up to which deviations larger than e are tolerated. Note that, $\xi _ { i } , \xi _ { i } *$ are called slack variables.

In order to solve problem (4), we formulate the dual problem by constructing the Lagrange function. The dual problem of Eq. (4) becomes:

$$
\begin{array}{l} \max - \frac {1}{2} \sum_ {i = 1} ^ {l} \sum_ {j = 1} ^ {l} \left(\lambda_ {i} - \lambda_ {i} ^ {*}\right) \left(\lambda_ {j} - \lambda_ {j} ^ {*}\right) \mathbf {x} _ {i} \mathbf {x} _ {j} - \varepsilon \sum_ {i = 1} ^ {l} \left(\lambda_ {i} + \lambda_ {i} ^ {*}\right) + \sum_ {i = 1} ^ {l} y _ {i} \left(\lambda_ {i} - \lambda_ {i} ^ {*}\right) \\ \text { Subject   to } \sum \left(\lambda_ {i} - \lambda_ {i} ^ {*}\right) = 0 \\ \lambda_ {i}, \lambda_ {i} ^ {*} \in (0, C). \end{array}\tag{5}
$$

Solving for w, we have

$$
\begin{array}{l} \mathbf {w} ^ {*} = \sum_ {i = 1} ^ {l} \bigl (\lambda_ {i} - \lambda_ {i} ^ {*} \bigr) \boldsymbol {x} _ {i}, \\ f (x) = \sum_ {i = 1} ^ {l} \bigl (\lambda_ {i} - \lambda_ {i} ^ {*} \bigr) \boldsymbol {x} _ {i} \boldsymbol {x} + b ^ {*}. \end{array}\tag{6}
$$

So far, we have explained the linear SVR. Let us look at the nonlinear case briefly. First of all, we need to map the input space into the feature space and try to find a linear regression hyperplane in the feature space. Using the trick of kernel functions [3,9,33,34], we have the following QP problem

$$
\begin{array}{l} \max - \frac {1}{2} \sum_ {i = 1} ^ {l} \sum_ {j = 1} ^ {l} \left(\lambda_ {i} - \lambda_ {i} ^ {*}\right) \left(\lambda_ {j} - \lambda_ {j} ^ {*}\right) K \left(\boldsymbol {x} _ {i} \boldsymbol {x} _ {j}\right) - \varepsilon \sum_ {i = 1} ^ {l} \left(\lambda_ {i} + \lambda_ {i} ^ {*}\right) + \sum_ {i = 1} ^ {l} y _ {i} \left(\lambda_ {i} - \lambda_ {i} ^ {*}\right) \\ \text { Subject   to } \sum \left(\lambda_ {i} - \lambda_ {i} ^ {*}\right) = 0 \\ \lambda_ {i}, \lambda_ {i} ^ {*} \in (0, C) \end{array}\tag{7}
$$

At the optimal solution, we obtain

$$
\begin{array}{l} \mathbf {w} ^ {*} = \sum_ {i = 1} ^ {l} \bigl (\lambda_ {i} - \lambda_ {i} ^ {*} \bigr) K (\boldsymbol {x}, \boldsymbol {x} _ {i}), \text { and } \\ f (x) = \sum_ {i = 1} ^ {l} \bigl (\lambda_ {i} - \lambda_ {i} ^ {*} \bigr) K (\boldsymbol {x}, \boldsymbol {x} _ {i}) + b, \end{array}\tag{8}
$$

where K(.,.) is a kernel function.

According to Refs. [3,9,42], any symmetric positive semi-definite function, which satisfies Mercer’s conditions, can be used as a kernel function in the SVMs context. Usually we have more than one kernel to map the input space into the feature space. The question is which kernel functions provide good generalization for a particular problem. We could not say that one kernel outperforms the others. Therefore, one has to use more than one kernel function for a particular problem. Some validation techniques such as bootstrapping and crossvalidation can be used to determine a good kernel [4,10]. Even when we decide for a kernel function, we have to decide what are the parameters of the kernel. For instance, RBF kernel has a parameter r and one has to decide the value of r before the experiment. Selection of this parameter is very important. Many algorithms are proposed to solve the SVM optimization problem [8,10,27,31,32,34]. We can divide these algorithms into two groups: (1) classical nonlinear algorithms such as gradient descent/ascent algorithms, and Zoutendijk’s methods [3,34]; and (2) state of the art interior point algorithms such as the primal dual path following algorithm [40,41]. One can solve moderate sizes of problems with these algorithms. In order to achieve the expected efficiency with a large-scale problem, decomposition techniques must be applied [8,31,32].

## 2.3. Artificial neural networks

Neural networks have recently gained popularity to explore the dynamics of a variety of financial applications [11,19,22,26,28,30,44,45]. Since the exchange markets are highly volatile, complex with noise market conditions, several neural network models such as multilayer perceptron (MLP), radial basis function networks (RBF) and recurrent networks have been applied to exchange rate forecasting [11,30,45].

MLP networks have the capability of a complex mapping between input and output that enables the network to approximate nonlinear functions. Consider a two-layer MLP network consisting of n input, and a hidden layer of s hidden neurons and a layer of m output neurons. MLP networks operate as follows: input units receive a pattern vector, $\pmb { x } = ( x _ { 1 } , x _ { 2 } , \dots x _ { n } )$ from an external world, which is propagated to all units in the hidden layer. Every hidden neuron j first computes the net input $\begin{array} { r } { h _ { j } = \sum _ { i } w _ { i j } x _ { i } } \end{array}$ and then produces as output $\begin{array} { r } { V _ { j } = f \big ( h _ { j } \big ) = \overline { { f } } \big ( \sum _ { i } w _ { i j } x _ { i } \big ) } \end{array}$ where f is a differentiable transfer function [21]. Each output unit k receives as input the output of the hidden layer and, repeating all the operations just described, we have

$$
O _ {k} = f \left(\sum_ {j = 1} ^ {s} V _ {j} w _ {j k}\right) = f \left(\sum_ {j = 1} ^ {s} f \left(\sum_ {i = 1} ^ {n} x _ {i} w _ {i j}\right) w _ {j k}\right).\tag{9}
$$

Several optimization algorithms can be used to train the MLP network. One of the most widely used training algorithms is the backpropagation algorithm (BP). The BP algorithm minimizes the total square error by using the general delta rule [21].

The challenging task is to determine the number of hidden layers, number of neurons in each layer, learning and momentum parameter. These parameters can be determined with trial and error or genetic algorithms can be used to find the optimal architecture of the network. Extensive information can be found in Refs. [30,35].

MLP networks can be used stand alone for exchange forecasting. The difficulty is to determine the right input and input size. This can be achieved by using the underlying economics theory to identify the influential variables. In addition to this, statistical techniques such as autoregressive models or co-integration can help us to determine the input variables for MLP networks.

Table 1  
ARIMA models for each exchange rate

<table><tr><td>Exchange rates</td><td>ARIMA models</td></tr><tr><td>Euro/Dollar</td><td>ARIMA(3,1,0)</td></tr><tr><td>Pound/Dollar</td><td>ARIMA(4,1,0)</td></tr><tr><td>JPY/Dollar</td><td>ARIMA(3,1,0)</td></tr><tr><td>AUD/Dollar</td><td>ARIMA(2,1,0)</td></tr></table>

## 3. Experiments

Exchange rate forecasting is a difficult task due to changing dynamics of its driving factors. There is a large number of factors that influence the daily value of the exchange rates. They can be identified by using time series models such as ARIMA and VAR techniques.

Daily values of exchange rates for Euro/Dollar, Pound/Dollar, JPY/Dollar and AUD/Dollar were used —from January 1, 2000 to May 26, 2004. The data set was randomly divided into three groups, training, crossvalidation, and testing set. The number of examples in each set is 1544, 100, and 60, respectively. Our analysis consists of two parts. First, we conduct a time series analysis to determine the number of inputs by using ARIMA method, VAR and co-integration analysis for Euro/Dollar and GBP/Dollar rates.

Two time series models have been used to identify the inputs. These techniques can be put in two categories, univariate time series, which are ARIMA models, and multivariate time series, VAR and co-integration techniques. After determining the number of inputs with these methods, SVR and MLP networks are applied. The performances of SVR and MLP networks are compared with each other in terms of mean square error (MSE) and mean absolute error (MAE). Furthermore, we compare the performance of the input selection method, namely ARIMA vs. VAR and co-integration techniques. The testing set, which is not seen by the learning algorithms before, is used for comparison. In the next two subsections, performance of learning algorithms (SVR and MLP networks) is given for input selection techniques.

Table 2  
Mean square error and mean absolute error of MLP network for testing set

<table><tr><td></td><td>EURO</td><td>GBP</td><td>JPY</td><td>AUD</td></tr><tr><td>MSE</td><td>0.0000294</td><td>0.0000115</td><td>0.0535000</td><td>0.0000017</td></tr><tr><td>MAE</td><td>0.0033000</td><td>0.0025000</td><td>0.1300000</td><td>0.0009735</td></tr></table>

Table 3  
Mean square error and mean absolute error of SVR for testing set

<table><tr><td></td><td>EURO</td><td>GBP</td><td>JPY</td><td>AUD</td></tr><tr><td>MSE</td><td>0.0000037</td><td>0.0000021</td><td>0.0106000</td><td>0.0000009</td></tr><tr><td>MAE</td><td>0.001400</td><td>0.001100</td><td>0.070900</td><td>0.000654</td></tr></table>

## 3.1. ARIMA method for input selection

The ADF unit root test revealed that Euro/Dollar, Pound/Dollar, JPY/Dollar and AUD/Dollar time series are not stationary. Based on autocorrelation and partial autocorrelation, the following models are selected for each exchange rate datasets (see Table 1).

Table 1 shows that the following functions give us the relationship between input and output for each time series.

$$
\begin{array}{l} x _ {t} = f (x _ {t - 1}, x _ {t - 2}, x _ {t - 3}), \\ y _ {t} = f (y _ {t - 1}, y _ {t - 2}, y _ {t - 3}, y _ {t - 4}), \\ z _ {t} = f (z _ {t - 1}, z _ {t - 2}, z _ {t - 3}), \\ v _ {t} = f (v _ {t - 1}, v _ {t - 2}). \end{array}\tag{10}
$$

where x = Euro/Dollar, y = Pound/Dollar, z = JPY/Dollar and v = AUD/Dollar.

MLP networks with the backpropagation algorithm have been applied for each series. Several studies showed that one hidden layer provides good generalization capability for financial forecasting problems. The number of hidden units influences the performance of the network. It is important not to over-fit the MLP networks with a large number of hidden units than can memorize the data. In order to avoid this problem, a 10- fold cross-validation technique is used to select the MLP architecture in terms of the validation error. MSE and MAE for the testing set are shown in Table 2 for Euro/Dollar, GBP/Dollar, JPY/Dollar and AUD/ Dollar exchange rates.

Furthermore, the SVR technique was also used as an alternative forecasting method. Since SVR has some free parameters such as the kernel function and its parameters, we need to specify them before running the algorithm. Free parameters of the SVR method have been determined by using a 10-fold cross-validation technique. Optimal parameters are shown in Table 3 with MSE and MAE of the testing set for each exchange rate.

Table 4  
Comparison of MLP and SVR method performance with t-test for testing set

<table><tr><td>Exchange rates</td><td>t-statistics</td><td>t-crit. value (0.05)</td><td>p-value</td></tr><tr><td>EURO/Dollar</td><td>3.8185</td><td>1.6626</td><td>0.0001</td></tr><tr><td>GBP/Dollar</td><td>4.5297</td><td>1.6626</td><td>0.0000</td></tr><tr><td>JPY/Dollar</td><td>2.5530</td><td>1.6626</td><td>0.0062</td></tr><tr><td>AUD/Dollar</td><td>2.6761</td><td>1.6626</td><td>0.0044</td></tr></table>

Table 6 Granger causality tests  
Table 5  
Trace and maximum eigenvalue test statistics for various values of the co-integration rank r with critical values for a 1%

<table><tr><td></td><td>Variables</td><td>Trace</td><td>Critical value</td><td> $\lambda_{\text{max}}$ </td><td>Critical value</td></tr><tr><td>r≤0</td><td>GBP/Dollar</td><td>60.699</td><td>62.520</td><td>28.653</td><td>36.193</td></tr><tr><td>r≤1</td><td>EURO/Dollar</td><td>58.921</td><td>41.081</td><td>35.845</td><td>29.263</td></tr><tr><td>r≤2</td><td>JPY/Dollar</td><td>38.076</td><td>16.162</td><td>26.432</td><td>21.747</td></tr><tr><td>r≤3</td><td>AUD/Dollar</td><td>7.571</td><td>6.635</td><td>7.571</td><td>6.635</td></tr></table>

We have conducted a t-test to see if there is a significant difference between MLP and SVR methods in the testing period. Null hypothesis is stated that there is no difference between the performance of MLP network and SVR method in terms of MSE when ARIMA input selection technique is used. For each series, we have concluded that the SVR method outperforms the MLP network based on t-test results (see Table 4).

## 3.2. Vector autoregression and co-integration method for input selection

We found that time series are I(1) by using Augmented Dickey Fuller(ADF) test. We select the time lag length using the likelihood ratio test and Akaike information criteria (AIC). These tests yield the optimal time lag length of k = 4 for each exchange rate. A model with a linear trend was assumed. The results of trace and maximum eigenvalue test statistics are given in Table 5. According to Table 5, there is no co-integration between the exchange rates. Because of this, we could not use cointegration analysis for the input selection process.

Because of the co-integration analysis results, we turn our attention to vector autoregressive models in order to determine the inputs. We chose the time lag length as k = 4 using the likelihood ratio test and AIC.

Table 7  
Mean square error (MSE) and mean absolute error (MAE) of MLP network for testing set by using VAR method for input selection

<table><tr><td></td><td>EURO</td><td>GBP</td><td>JPY</td><td>AUD</td></tr><tr><td>MSE</td><td>0.0000049</td><td>0.0000091</td><td>0.0323000</td><td>0.0000056</td></tr><tr><td>MAE</td><td>0.0018000</td><td>0.0025000</td><td>0.1437000</td><td>0.0020000</td></tr></table>

Then a VAR model was assumed and the parameters of the model were estimated. Investigation of residuals by the Granger causality test [17] shows that the Euro/ Dollar rate has a significant Granger-Causal impact on the GBP/Dollar rate and vice versa (see Table 6).

From these results, the relationship between the exchange rates can be explained by the following equations.

$$
x _ {t} = f (x _ {t - 1}, \ldots , x _ {t - 4}, y _ {t - 1}, \ldots , y _ {t - 4})\tag{11a}
$$

$$
y _ {t} = f (y _ {t - 1}, \ldots , y _ {t - 4}, x _ {t - 1}, \ldots , x _ {t - 4})\tag{11b}
$$

$$
z _ {t} = f (z _ {t - 1}, \dots , z _ {t - 4}, x _ {t - 1}, \dots , x _ {t - 4}, y _ {t - 1}, \dots , y _ {t - 4})\tag{11c}
$$

$$
v _ {t} = f (v _ {t - 1}, \ldots , v _ {t - 4}, y _ {t - 1}, \ldots , y _ {t - 4})\tag{11d}
$$

$$
x _ {t}: (\text { Euro / Dollar }) _ {t}
$$

$$
y _ {t}: (\mathrm{GBP/Dollar}) _ {t}
$$

$$
z _ {t}: \left(\mathrm{JPY} / \text {Dollar}\right) _ {t}
$$

$$
v _ {t}: (\mathrm{AUD} / \text { Dollar }) _ {t}.
$$

From Table 6 and Eqs. (11a) (11b) (11c) (11d), we draw the following results: EURO/Dollar exchange rate depends on its previous values and GBP/Dollar rate’s on four previous values. GBP/Dollar exchange rate can be determined by its previous values and EURO/Dollar rate’s by its four previous values. JPY/Dollar rates can be determined by its four previous values, similarly EURO/Dollar and GBP/Dollar rates by its four previous values. We need four previous values of AUD/Dollar and GBP/Dollar to determine the AUD/Dollar exchange rate.

<table><tr><td></td><td>F-value</td><td>F-probability</td><td></td><td>F-value</td><td>F-probability</td></tr><tr><td>Equation 1: (11a)</td><td></td><td></td><td>Equation 3: (11c)</td><td></td><td></td></tr><tr><td>GBP</td><td>2.4601</td><td>0.0420</td><td>GBP</td><td>3.4281</td><td>0.0085</td></tr><tr><td>EUR</td><td>10,482.2311</td><td>0.0000</td><td>EUR</td><td>0.6336</td><td>0.6386</td></tr><tr><td>USD/JPY</td><td>1.2071</td><td>0.3059</td><td>USD/JPY</td><td>27,977.3069</td><td>0.0000</td></tr><tr><td>USD/AUD</td><td>0.7783</td><td>0.5392</td><td>USD/AUD</td><td>3.063</td><td>0.0158</td></tr><tr><td>Equation 2: (11b)</td><td></td><td></td><td>Equation 4: (11d)</td><td></td><td></td></tr><tr><td>GBP</td><td>7622.7929</td><td>0.0000</td><td>GBP</td><td>1.4386</td><td>0.2188</td></tr><tr><td>EUR</td><td>2.5388</td><td>0.0383</td><td>EUR</td><td>2.3721</td><td>0.0499</td></tr><tr><td>USD/JPY</td><td>1.1301</td><td>0.3406</td><td>USD/JPY</td><td>0.5233</td><td>0.7186</td></tr><tr><td>USD/AUD</td><td>0.7348</td><td>0.5682</td><td>USD/AUD</td><td>11,456.0016</td><td>0.0000</td></tr></table>

Table 8  
Mean square error (MSE) and mean absolute error (MAE) of SVR for testing set by using VAR method for input selection

<table><tr><td></td><td>EURO</td><td>GBP</td><td>JPY</td><td>AUD</td></tr><tr><td>MSE</td><td>0.0000028</td><td>0.0000122</td><td>0.0159000</td><td>0.0000040</td></tr><tr><td>MAE</td><td>0.001400</td><td>0.003200</td><td>0.098700</td><td>0.001600</td></tr></table>

Next, we will use this information on SVR and MLP methods. We have used the same experimental design as we used for univariate analysis. An MLP network with one hidden layer is used for each series. The number of hidden units and other parameters are determined by using a 10-fold cross-validation. Performance of the MLP networks is shown in Table 7.

As we stated in Section 3.1, selection of the free parameters for the SVR method is very important. SVR is very sensitive to these parameters. For this reason, a 10-fold cross-validation technique is employed in order to determine the right parameters. After determining these, an optimal solution is found by solving the problem. The performance of the SVR method with the VAR input selection process is given in Table 8 for each exchange rate in terms of MSE and MAE.

If we compare the MSEs of MLP and SVR method, we see that SVR outperforms the MLP networks for VAR input selection method for all series except the GBP/Dollar exchange rate. We have also performed a t-test to check if SVR outperforms the MLP methods for Euro/Dollar, GBP/Dollar, JPY/Dollar and AUD/ Dollar exchange rates. We test the null hypothesis that the performances of SVR and MLP methods are the same for each exchange rate. Test results show that we accept the alternative hypothesis which is, SVR method outperforms the MLP methods for Euro/Dollar, JPY/Dollar and AUD/Dollar except GBP/Dollar (see Table 9). The performance of SVR and MLP network is the same for GBP/Dollar. All individual t-tests are performed at 5% significance level. This means that the SVR method outperforms the MLP networks for exchange rate forecasting.

Table 9  
Comparison of MLP and SVR method performance with t-test for testing set

<table><tr><td>Exchange rates</td><td>t-statistics</td><td>t-critical value (0.05)</td><td>p-value</td></tr><tr><td>EURO/Dollar</td><td>2.0085</td><td>1.6672</td><td>0.0243</td></tr><tr><td>GBP/Dollar</td><td>-1.0043</td><td>1.6672</td><td>0.1594</td></tr><tr><td>JPY/Dollar</td><td>2.3954</td><td>1.6672</td><td>0.0097</td></tr><tr><td>AUD/Dollar</td><td>2.2953</td><td>1.6672</td><td>0.0124</td></tr></table>

Table 10  
MSE of ARIMA and VAR input selection procedure for testing set

<table><tr><td rowspan="2">Exchange rates</td><td colspan="2">MLP network</td><td colspan="2">SVR method</td></tr><tr><td>ARIMA</td><td>VAR</td><td>ARIMA</td><td>VAR</td></tr><tr><td>EURO/Dollar</td><td>0.000029</td><td>0.000005</td><td>0.000004</td><td>0.000003</td></tr><tr><td>GBP/Dollar</td><td>0.000012</td><td>0.000009</td><td>0.000002</td><td>0.000012</td></tr><tr><td>JPY/Dollar</td><td>0.053500</td><td>0.032300</td><td>0.010600</td><td>0.015900</td></tr><tr><td>AUD/Dollar</td><td>0.000002</td><td>0.000006</td><td>0.000001</td><td>0.000004</td></tr></table>

## 3.3. Comparison of input selection techniques

Until this point, we have compared the SVR and MLP network. Comparison of the input selection process, namely ARIMA vs. VAR, would reveal some information. The following design is used for the comparison of input selection. Since we employ two methods after the input selection procedure, MSE and MAE of input selection process are given in the following table.

Table 10 shows the MSE of ARIMA and VAR technique for MLP network and SVR method. It is wise to use VAR technique in order to determine the input of the MLP networks for three exchange rates; EURO/Dollar, GBP/Dollar and JPY/Dollar. On the other hand, ARIMA outperforms the VAR technique to determine the input of the SVR method for the three exchange rates, GBP/Dollar, JPY/Dollar, and AUD/ Dollar. As we know from Sections 3.1 and 3.2, SVR outperforms the MLP networks. Therefore, ARIMA input selection procedure can be used to determine the inputs.

Finally, we have compared the proposed hybrid methods with pure forecasting techniques, ARIMA and VAR. Model specifications of these two methods have been done in Sections 3.1 and 3.2. The following table (Table 11) shows the MSE of the pure techniques.

Comparison of the hybrid methods with pure techniques reveals that the hybrid method outperforms the pure ARIMA and VAR models in terms of MSE error (see Tables 10 and 11). By using hybrid forecasting techniques, we try to avoid the weakness of pure techniques.

Table 11  
MSE of pure forecasting techniques (ARIMA and VAR) for testing set

<table><tr><td>Exchange rates</td><td>ARIMA</td><td>VAR</td></tr><tr><td>EURO/Dollar</td><td>0.001874</td><td>0.000039</td></tr><tr><td>GBP/Dollar</td><td>0.004072</td><td>0.000081</td></tr><tr><td>JPY/Dollar</td><td>6.853610</td><td>0.361648</td></tr><tr><td>AUD/Dollar</td><td>0.001108</td><td>0.000071</td></tr></table>

## 4. Conclusions

We try to combine parametric and nonparametric techniques in order to obtain a better performance for exchange rate forecasting. In addition to this, comparison of two nonparametric models, ANN and SVR, is given with two input selection techniques, ARIMA and VAR, respectively. Parametric and nonparametric techniques have some advantages and disadvantages. For example, parametric techniques are based on specific assumptions and these assumptions are not satisfied or partially satisfied in real world problems. Because of this, we use parametric techniques to identify the number of previous values of dependent and independent variables. On the other hand, nonparametric techniques do not have any restricted assumption like parametric techniques. For this reason, they are applied to estimate the parameters of the mathematical models.

Experiments showed that SVR method outperforms the MLP networks for each input selection algorithm. This can be explained by the formulation of the SVR and MLP networks. SVR method uses a quadratic programming problem which is convex and has a global optimum solution. On the other hand, MLP networks use the backpropagation algorithm to minimize the network error. The problem is nonconvex and it is hard to find the global optimum.

Comparison of the input selection process reveals different results. The best selection procedure depends on the training algorithms. If we want to use an MLP network, it is better to use VAR technique to determine the inputs. On the other hand, ARIMA input selection technique gives the best results if SVR method is employed for training. All the comparisons are made by using MSE and MAE error of the testing set.

A different approach has been applied to exchange rate forecasting. This hybrid technique provides very promising results. The next step would be to develop trading strategies. Our goal is to show that combination of parametric and nonparametric techniques is as good as pure techniques.

## References

[1] T. Bollerslev, Generalized autoregressive conditional heteroskedasticity, Journal of Econometrics 31 (1986) 307 – 327.

[2] C. Brooks, Linear and non-linear (non-)forecastability of high frequency exchange rates, Journal of Forecasting 15 (1997) 125– 145.

[3] C.J.C. Burges, A tutorial on support vector machines for pattern classification, Data Mining and Knowledge Discovery 2 (2) (1998) 121–167.

[4] O. Chapelle, V. Vapnik, O. Bousquet, S. Mukherjee, Choosing multiple parameters for support vector machines, Machine Learning 46 (13) (2002) 131– 159.

[5] A. Chen, M.T. Leung, H. Daouk, Application of neural networks to an emerging financial market: forecasting and trading the Taiwan stock index, Computers Operations Research 30 (2003) 901–923.

[6] A.-S. Chen, M.T. Leung, Regression neural network for error correction in foreign exchange forecasting and trading, Computers and Operations Research 31 (2004) 1049– 1068.

[7] S.-H. Chun, S.H. Kim, Impact of momentum bias on forecasting through knowledge discovery techniques in the foreign exchange market, Expert Systems with Applications 24 (2003) 115–122.

[8] R. Collobert, S. Bengio, Svmtorch: support vector machines for largescale regression problems, Journal of Machine Learning Research 1 (2001) 143–160.

[9] C. Cortes, V. Vapnik, Support vector networks, Machine Learning 20 (1995) 273 – 297.

[10] N. Cristianini, C. Campbell, J. ShaweTaylor, Dynamically adapting kernels in support vector machines, NIPS 1998 (1998) 204 – 210.

[11] J.T. Davis, A. Episcopos, S. Wettimuny, Predicting direction shifts on Canadian–US exchange rates with artificial neural networks, International Journal of Intelligient Systems in Accounting 10 (2001) 83 – 96.

[12] S., Demirbas, Cointegration Analysis—Causality Testing and Wagner’s Law: The Case of Turkey, 1950–1990, Annual Meeting of the European Public Choice Society (April 7–10, 1999).

[13] F.X. Diabold, J. Gardeazabal, K. Yilmaz, On cointegration and exchange rate dynamics, Journal of Finance 49 (1994) 727– 735.

[14] Z. Ding, C.W.J. Granger, Modeling volatility persistence of speculative returns: a new approach, Journal of Econometrics 73 (1996) 185–215.

[15] Z. Ding, C.W.J. Granger, R.F. Engle, A long memory property of stock market returns and a new model, Journal of Empirical Finance 1 (1993) 83–106.

[16] R.F. Engle, Autoregressive conditional heteroscedasticity with estimates of the variance of the United Kingdom inflation, Econometrica 50 (1982) 987– 1008.

[17] R.F. Engle, C.W. Granger, Co-integration and error correction: representation, estimation and testing, Econometrica 55 (1987) 251 – 276.

[18] M. Fernandes, Non-linearity and exchange rates, Journal of Forecasting 17 (1998) 497 – 514.

[19] J. Galindo, A framework for comperative analysis of statistical and machine learning methods: an application to the black scholes option pricing equations, Technical Report, Banco de Mexico, Mexico, DF, 1998 (04930).

[20] J.D. Hamilton, Time Series Analysis, Princeton Univ. Press, 1994.

[21] S. Haykin, Neural Networks: A Comprehensive Foundation, MacMillan Publishing Company, New York, 1994.

[22] J.M. Hutchinson, A.W. Lo, T. Poggio, A nonparametic approach to pricing and hedging derivative securities via learning networks, The Journal of Finance XLIX (3) (1994) 851 – 889.

[23] H. Ince, B. Trafalis, Short term forecasting with support vector machines and application to stock price prediction, in: Dagli, Buczak, Ghosh, Embrechts, Ersoy (Eds.), Smart Engineering

System Design: Neural Networks, Fuzzy Logic, Evolutionary Programming, Data Mining and Complex Systems, ASME Press, 2003, pp. 737– 746.

[24] S. Johansen, Estimation and hypothesis of cointegration vectors in Gaussian vector autoregressive models, Econometrica 59 (1991) 1551–1580.

[25] L. Kilian, M.P. Taylor, Why is it so difficult to beat random walk forecast of exchange rates? Journal of International Economics 60 (2003) 85– 107.

[26] V. Kodogiannis, A. Lolis, Forecasting financial time series using neural network and fuzzy system-based techniques, Neural Computing and Applications 11 (2002) 90–102.

[27] Y.J. Lee, O.L. Mangasarian, Rsvm: reduced support vector machines, CD Proceedings of the First SIAM International Conference on Data Mining, 2001.

[28] X. Li, C.-L. Ang, R. Gray, An intelligent business forecaster for strategic business planning, Journal of Forecasting 18 (1999) 181–204.

[29] F. Lisi, R.A. Schiavo, A comparison between neural networks and chaotic models for exchange rate prediction, Computational Statistics and Data Analysis 30 (1999) 87 – 102.

[30] A.K. Nag, A. Mitra, Forecasting daily foreign exchange rates using genetically optimized neural networks, Journal of Forecasting 21 (2002) 501 – 511.

[31] E. Osuna, R. Freund, F. Girosi, Training support vector machines: an application to face detection, Proc. Computer Vision and Pattern Recognition ’97, 1997, pp. 130 – 136.

[32] J. Platt, Fast training of support vector machines using sequential minimal optimization, in: B. Sch<sup>¨</sup> olkopf, C.J.C. Burges, A.J. Smola (Eds.), Advances in Kernel Methods: Support Vector Learning, MIT Press, 1999, pp. 185 – 208.

[33] M. Pontil, A. Verri, Properties of support vector machines, Technical Report, Massachusetts Institute of Technology, Artificial Intelligence Laboratory, 1997.

[34] B. Scho¨lkopf, A.J. Smola, Learning with Kernels: Support Vector Machines, Regularization, Optimization, and Beyond, The MIT Press, Cambridge, Massachusetts, 2002.

[35] T.B. Trafalis, Artificial neural networks applied to financial forecasting, in: C.J.C. Dagli, Buczak, Ghosh, Embrechts, Ersoy (Eds.), Smart Engineering System Design: Neural Networks, Fuzzy Logic, Evolutionary Programming, data Mining and Complex Systems, ASME Press, 1999, pp. 1049– 1054.

[36] T.B. Trafalis, H. Ince, Support vector machine for regression and applications to financial forecasting, Neural Networks, 2000. IJCNN 2000, Proceedings of the IEEEINNSENNS International Joint Conference, vol. 6, IEEE, 2000, pp. 348 – 353.

[37] T.B. Trafalis, H. Ince, T. Mishina, Support vector regression in option pricing, Proceedings of Conference on Computational Intelligence and Financial Engineering (CIFer 2003), 2003 (March 20–23) Hong Kong, 2003.

[38] A. Trapletti, A. Geyer, F. Leisch, Forecasting exchange rates using cointegration models and intra-day data, Journal of Forecasting 21 (2002) 151 – 166.

[39] R. Tsaih, Sensitivity Analysis, Neural Networks and, the Finance, 1999, pp. 3830 – 3835.

[40] R.J. Vanderbei, Interior point methods: algorithms and formulations, ORSA Journal on Computing 6 (1) (1995) 32 – 34.

[41] R.J. Vanderbei, LOQO an interior point code for quadratic programming, Technical Report, Statistics and Operations Research, Princeton University, 1998 (SOQ-94-15).

[42] V. Vapnik, The Nature of Statistical Learning Theory, Springer Verlag, 1995.

[43] J. Vilasuso, Forecasting exchange rate volatility, Economic Letters 76 (2002) 59–64.

[44] Z. Vojinovic, V. Kecman, R. Seidel, A data mining approach to financial time series modeling and forecasting, International Journal of Intelligent Systems, Finance & Management 10 (2001) 225– 239.

[45] J. Yao, C.H. Tan, A case study on using neural networks to perform technical forecasting of forex, Neurocomputing 34 (2000) 79– 98.

Huseyin Ince is an Assistant Professor in the School of Business Administration at Gebze Institute of Technology in Turkey. He received his BS degree in Econometrics from Uludag University, Turkey, MS degree in Operations Research from Case Western Reserve University–Ohio, USA and PhD degree in Industrial Engineering from University of Oklahoma, USA. His teaching and research interests are in machine learning and its applications, kernel methods, data mining techniques, optimization, and financial time series analysis.

Theodore B. Trafalis, PhD, is a Professor in the School of Industrial Engineering at the University of Oklahoma. He earned his BS in mathematics from the University of Athens, Greece, his MS in Applied Mathematics, MSIE, and PhD in Operations Research from Purdue University. He is a member of INFORMS, SIAM, Hellenic Operational Society, International Society of Multiple Criteria Decision Making, and the International Society of Neural Networks. He has been listed in several Who’s Who biographies such as in the 1993–1994 edition of Who’s Who in the World. He was a visiting Assistant Professor at Purdue University (1989–1990), an invited Research Fellow at Delft University of Technology, Netherlands (1996), and a visiting Associate Professor at Blaise Pascal University, France, and at the Technical University of Crete (1998). He was also an invited visiting Associate Professor at Akita Prefectural University, Japan (2001). His research interests include operations research/management science, mathematical programming, interior point methods, multiobjective optimization, control theory, artificial neural networks, kernel methods, evolutionary programming data mining and global optimization. He has published more than 100 articles in journals, conference proceedings, edited books, made over 100 technical presentations and received several awards for his papers. In 2004, he received the Regents Award at the University of Oklahoma for his research activities. He has been continuously funded through National Science Foundation (NSF) and received the NSF research initiation award in 1991. He currently serves as a PI on an interdisciplinary grant related to real time mining of integrated weather data funded from the NSF. He is currently editing a special issue in Support Vector Machines for the journal of Computational Management Science. He is also an associate editor of Computational Management Science and The Journal of Heuristics and has been on the Program Committee of several international conferences in the field of intelligent systems and optimization.
