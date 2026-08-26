---
otero_id: 4178
otero_key: "KZREWN4Q"
title: "Forecasting and trading the EUR/USD exchange rate with stochastic Neural Network combination and time-varying leverage"
authors: "Georgios Sermpinis; Christian Dunis; Jason Laws; Charalampos Stasinakis"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.05.039"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Forecasting and trading the EUR/USD exchange rate with stochastic Neural Network combination and time-varying leverage

Georgios Sermpinis <sup>a,</sup>⁎, Christian Dunis <sup>b</sup>, Jason Laws <sup>c</sup>, Charalampos Stasinakis <sup>a</sup>

<sup>a</sup> University of Glasgow Business School, University of Glasgow, Gilbert Scott Building, Glasgow, G12 8QQ, United Kingdom

<sup>b</sup> Liverpool Business School, JMU, John Foster Building, 98 Mount Pleasant, Liverpool L3 5UZ, United Kingdom

<sup>c</sup> University of Liverpool Management School, The University of Liverpool, Chatham Street, Liverpool, L69 7ZH, United Kingdom

## a r t i c l e i n f o

Article history: Received 18 September 2011 Received in revised form 1 May 2012 Accepted 21 May 2012 Available online 30 May 2012

Keywords: Psi Sigma network Recurrent Network Forecast combinations Kalman Filter LASSO Leverage

## a b s t r a c t

The motivation of this paper is to investigate the use of a Neural Network (NN) architecture, the Psi Sigma Neural Network (PSN), when applied to the task of forecasting and trading the Euro/Dollar (EUR/USD) exchange rate using the European Central Bank (ECB) <sup>fi</sup>xing series and to explore the utility of Kalman Filters in combining NN forecasts. This is done by benchmarking the statistical and trading performance of PSN with a Naive Strategy, an Autoregressive Moving Average (ARMA) model and two different NN architectures, a Multi-Layer Perceptron (MLP) and a Recurrent Network (RNN). We combine our NN forecasts with Kalman Filter, a traditional Simple Average, the Bayesian Average, the Granger–Ramanathan's Regression Approach (GRR) and the Least Absolute Shrinkage and Selection Operator (LASSO). Finally, we apply a time-varying leverage strategy based on RiskMetrics volatility forecasts in order to further improve the forecasting performance of our models and combinations. The statistical and trading performance of our models is estimated throughout the period of 2002–2010, using the last two years for out-of-sample testing. In terms of our results, the PSN outperforms all models' individual performances in terms of statistical accuracy and trading performance. The forecast combinations also present improved empirical evidence, with Kalman Filters outperforming by far its benchmarks. We also note that after the application of the time varying leverage, all models except ARMA show a substantial increase in their trading performance.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

The term of Neural Network (NN) originates from the biological neuron connections of human brain. The arti<sup>fi</sup>cial NNs are computation models that embody data-adaptive learning and clustering abilities, deriving from parallel processing procedures [34]. The NNs are considered a relatively new technology in Finance, but with high potential and an increasing number of applications. However, their practical limitations and contradictory empirical evidence lead to skepticism on whether they can outperform existing traditional models.

The motivation for this paper is to investigate the trading performance of a novel Neural Network (NN) architecture, the Psi Sigma Neural Network (PSN), and explore the utility of Kalman Filters in combining NN forecasts. Firstly, we apply the EUR/USD European Central Bank (ECB) <sup>fi</sup>xing series to a Naive Strategy, an Autoregressive Moving Average (ARMA) model and three NNs, namely a Multi-Layer Perceptron (MLP), a Recurrent Network (RNN) and a PSN. Secondly, we compare the Kalman Filter with four forecast combination methods. That is the traditional Simple Average, the Bayesian Average, Granger–Ramanathan's Regression Approach (GRR) and the Least Absolute Shrinkage and Selection Operator (LASSO). The models' performance is estimated using the EUR/USD ECB <sup>fi</sup>xing series of the period of 2002–2010, using the last two years for out-ofsample testing. We also introduce a time-varying leverage strategy based on RiskMetrics volatility forecasts.

Our results show, PSN outperforms its NN and statistical benchmarks in terms of annualized returns and information ratios. The NN forecast combinations, excluding the Bayesian Average model, present improved annualized returns and information ratios and in almost all cases outperform every individual NN performance. More speci<sup>fi</sup>cally, the Kalman Filter outperforms all individual models and combination forecasts. We also note that the Kalman Filter forecasts are statistically different from their benchmarks under the Diebold–Marino test [11]. Finally we note that, after applying the time-varying leverage strategy, all models except ARMA show substantial increase in their trading performance.

Section 2 is a literature review of previous research on PSNs and combination forecasts, especially Kalman Filters. Section 3 follows the detailed description of the EUR/USD ECB <sup>fi</sup>xing series, used as our dataset. Section 4 gives an overview of the benchmark models and the architectures of the NNs selected, while Section 5 describes the forecast combination methods we implemented. The statistical and trading performance of our models is presented in Sections 6 and 7. Finally, some concluding remarks are summarized in Section 8.

## 2. Literature review

The most common NN architecture is the MLP and seems to perform well at time-series <sup>fi</sup>nancial forecasting [38], although the empirical evidence can be contradictory in many cases. For example, Tsaih et al. [53] attempt to forecast the S&P 500 stock index futures and in their application Reasoning Neural Networks perform better than MLPs. Lam [35] also examines the <sup>fi</sup>nancial forecasting performance of feed-forward NNs and concludes that they fail to outperform the maximum benchmarks in all cases. Ince and Trafalis [31] forecast the EUR/USD, GBP/USD, JPY/USD and AUD/USD exchange rates with MLP and Support Vector Regression and their results show that MLP achieves less accurate forecasts. Finally, according to Alfaro et al. [2] the AdaBoost algorithm is superior to MPLs, when applied to the task of forecasting bankruptcy of European <sup>fi</sup>rms. On the other hand, Tenti [49] and Dunis and Huang [15] achieved encouraging results also by using RNNs to forecast the exchange rates. But the PSN architecture presents remarkable empirical evidence compared to both MLP and RNN. PSNs were <sup>fi</sup>rst introduced by Ghosh and Shin [23] as architectures able to capture high-order correlations. Ghosh and Shin [23,24] also present results on their forecasting superiority in function approximation, when compared with a MLP network and a Higher Order Neural Network (HONN). Ghazali et al. [22] compare PSN with HONN and MLP in terms of forecasting and trading the IBM common stock closing price and the US 10-year government bond series. PSN presented improved statistical accuracy and annualized return compared with both benchmarks. Satisfactory forecasting results of PSN were presented by Hussain et al. [30] on the EUR/USD, the EUR/GBP and the EUR/JPY exchange rates using univariate series as inputs in their networks. On the other hand, Dunis et al. [16] also study the EUR/USD series with PSN and fail to outperform MLP, RNN and HONN in a simple trading application.

Bates and Granger [4] and Newbold and Granger [39] suggested combining rules based on variances–covariances of the individual forecasts, while Granger and Ramanathan [26] presented a regression combination forecast framework with encouraging results. According to Palm and Zellner [40], it is sensible to use Simple Average for combination forecasting, while Deutsch et al. [10] achieved substantially smaller squared forecast errors combining forecasts with changing weights. The regression framework, presented in the 90s, performs poorly though in many cases, which leads the research to turn to more sophisticated methods. For example, Chan et al. [8] suggested the use of Ridge Regression, while Swanson and Zeng [48] use Bayesian Information Criteria. However, in real applications there are also contradictory results regarding both these models (see Stock and Watson [46] and Rapach and Strauss [42]). Finally, Leigh et al. [36] presented novel experiments of combining pattern recognition, NNs and genetic algorithms, in order to forecast price changes for the NYSE Composite Index. From their approach stock market purchasing opportunities are identi<sup>fi</sup>ed and encouraging decision-making results are achieved.

Time-series analysis is often based on the assumption that the parameters are <sup>fi</sup>xed. However, in reality <sup>fi</sup>nancial data and the correlation structure between <sup>fi</sup>nancial variables are time-varying. Harvey [28] and Hamilton [27] both suggest using state space modeling, such as Kalman Filter, for representing dynamic systems where unobserved variables (so-called ‘state’ variables) can be integrated within an ‘observable’ model. According to Goh and Mandic [25] the recursive Kalman Filter is suitable for processing complex-valued nonlinear, non-stationary signals and bivariate signals with strong component correlations. Kalman Filter is also considered an optimal time-varying <sup>fi</sup>nancial forecast for <sup>fi</sup>nancial markets [19]. Anandalingam and Chen [3] compare Kalman Filter with Bayesian combination forecast model, while Sessions and Chatterjee [44] conclude that recursive methods are found to be very effective. LeSage and Magura [37] extend the Granger–Ramanathan combination method by allowing time-varying weights and their methodology outperforms traditional and other forecast combinations. Terui and van Dijk [50] also suggest that the combined forecasts perform well, especially with time varying coef<sup>fi</sup>cients. Finally, Stock and Watson [46] try to forecast the output growth of seven countries and note that time-varying combination forecasts can lack in robustness, despite performing well in many cases.

## 3. The EUR/USD exchange rate and related <sup>fi</sup>nancial data

The European Central Bank (ECB) publishes a daily <sup>fi</sup>xing for selected EUR exchange rates: these reference mid-rates are based on a daily concentration procedure between central banks within and outside the European System of Central Banks, which normally takes place at 2.15 p.m. ECB time. The reference exchange rates are published both by electronic market information providers and on the ECB's website shortly after the concentration procedure has been completed. Although only a reference rate, many <sup>fi</sup>nancial institutions are ready to trade at the EUR <sup>fi</sup>xing and it is therefore possible to leave orders with a bank for business to be transacted at this level.

In this paper, we examine the EUR/USD over period 2002–2010, using the last two years for out-of-sample. In order to train our Neural Networks we further divided our in-sample dataset in two subperiods (see more in Section 4.2) (Table 1).

The graph below shows the total dataset for the EUR/USD and its volatile trend since early 2008 (Fig. 1).

The EUR/USD time series, shown above, is non-normal and nonstationary. Jarque–Bera statistics con<sup>fi</sup>rm its non-normality at the 99% con<sup>fi</sup>dence interval with slight skewness and low kurtosis. To overcome the non-stationary issue, the EUR/USD series is transformed into a daily series of rate returns. So given the price level $P _ { 1 } ,$ $P _ { 2 } , . . . , P _ { t } ,$ the return at time t is calculated as:

$$
R _ {t} = \left(\frac {P _ {t}}{P _ {t - 1}}\right) - 1.\tag{1}
$$

The stationary property of the EUR/USD return series is con<sup>fi</sup>rmed at the 1% signi<sup>fi</sup>cance level (ADF and PP test statistics) and its summary statistics are shown in Fig. 2. From those it is obvious that the slight skewness and low kurtosis remain. The Jarque–Bera statistic con<sup>fi</sup>rms again that the EUR/USD series is non-normal at the 99% con<sup>fi</sup>dence interval. For more details on Jarque–Bera statistics see Jarque and Bera [32].

In the absence of any formal theory behind the selection of the inputs of a Neural Network, we conduct some Neural Network experiments and a sensitivity analysis on a pool of potential inputs in the training dataset in order to help our decision. Our aim is to select the set of inputs for each network which is the more likely to lead to the best trading performance in the out-of-sample dataset. In our application, we select as inputs the set of variables that provide the higher trading performance for each network in the test sub-period. To our surprise this set of inputs is identical for all Neural Network models. These sets of inputs for each network are presented in Table 2 below.<sup>1</sup>

Table 1  
The EUR/USD dataset–Neural Networks' training datasets.

<table><tr><td>Periods</td><td>Trading days</td><td>Start date</td><td>End date</td></tr><tr><td>Total dataset</td><td>2295</td><td>3/01/2002</td><td>31/12/2010</td></tr><tr><td>Training dataset (in-sample)</td><td>1270</td><td>3/01/2002</td><td>29/12/2006</td></tr><tr><td>Test dataset (in-sample)</td><td>511</td><td>02/01/2007</td><td>31/12/2008</td></tr><tr><td>Validation dataset (out-of-sample)</td><td>514</td><td>02/01/2009</td><td>31/12/2010</td></tr></table>

## 4. Forecasting models

## 4.1. Benchmark forecasting models

In this paper we use two traditional forecasting strategies, the Naive Strategy and the Auto-Regressive Moving Average (ARMA) model, in order to benchmark the ef<sup>fi</sup>ciency of the NNs' trading performance.

## 4.1.1. Naive Strategy

The Naive Strategy is considered to be the simplest strategy to predict the future. That is to accept as a forecast for time $t + 1 ,$ , the value of time t, assuming that the best prediction is the most recent period change. Thus, the model takes the form:

$$
\hat {Y} _ {t + 1} = Y _ {t}\tag{2}
$$

where $Y _ { t }$ is the actual rate of return at time t and $\hat { Y } _ { t + 1 }$ is the forecast rate of return at time t + 1. In order to evaluate the Naive trading performance, a simulated strategy is used.

## 4.1.2. Auto-Regressive Moving Average Model (ARMA)

The ARMA model is based on the assumption that the current value of a time-series is a linear combination of its previous values plus a combination of current and previous values of the residuals [6]. Thus, the ARMA model embodies autoregressive and moving average components and can be speci<sup>fi</sup>ed as below:

$$
\begin{array}{r} Y _ {t} = \varphi_ {0} + \varphi_ {1} Y _ {t - 1} + \varphi_ {2} Y _ {t - 2} + \ldots + \varphi_ {p} Y _ {t - p} \\ + \varepsilon_ {t} - w _ {1} \varepsilon_ {t - 1} - w _ {2} \varepsilon_ {t - 2} - \ldots - w _ {q} \varepsilon_ {t - q} \end{array}\tag{3}
$$

Where:

• $Y _ { t }$ is the dependent variable at time t

$Y _ { t - 1 } , Y _ { t - 2 , \cdots } Y _ { t - p }$ are the lagged dependent variables

$\varphi _ { 0 } , \varphi _ { 1 } , . . . , \varphi _ { p }$ are the regression coef<sup>fi</sup>cients

• $\varepsilon _ { t }$ is the residual term

$\boldsymbol { \varepsilon } _ { t - 1 } , \boldsymbol { \varepsilon } _ { t - 2 } , . . . , \boldsymbol { \varepsilon } _ { t - q }$ are the previous values of the residual terms

$w _ { 1 } , w _ { 2 } , . . . , w _ { q }$ are the residual weights.

Based on the In-Sample correlogram (Training and Test subsets), a restricted ARMA (13,13) model was chosen as the best for an out-ofsample estimation (See Appendix A). The ARMA model, used in this paper, can be speci<sup>fi</sup>ed as follows:

$$
\begin{array}{l} Y _ {t} = 0. 0 2 8 8 - 0. 2 6 8 9 Y _ {t - 3} + 0. 6 0 2 8 Y _ {t - 4} - 0. 3 9 2 1 Y _ {t - 6} - 0. 6 8 8 4 Y _ {t - 9} \\ \quad + 0. 3 6 4 1 Y _ {t - 1 3} + 0. 2 6 3 8 \varepsilon_ {t - 3} - 0. 5 9 \varepsilon_ {t - 4} + 0. 3 9 1 6 \varepsilon_ {t - 6} \\ \quad + 0. 6 2 2 7 \varepsilon_ {t - 9} - 0. 3 1 6 5 \varepsilon_ {t - 1 3}. \end{array} \tag {4}
$$

The evaluation of the ARMA model selected comes in terms of trading performance.

## 4.2. Neural Networks (NNs)

Neural Networks exist in several forms in the literature. The most popular architecture is the Multi-Layer Perceptron (MLP). A standard Neural Network has at least three layers. The <sup>fi</sup>rst layer is called the input layer (the number of its nodes corresponds to the number of explanatory variables). The last layer is called the output layer (the number of its nodes corresponds to the number of response variables). An intermediary layer of nodes, the hidden layer, separates the input from the output layer. Its number of nodes de<sup>fi</sup>nes the amount of complexity the model is capable of <sup>fi</sup>tting. In addition, the input and hidden layers contain an extra node called the bias node. This node has a <sup>fi</sup>xed value of one and has the same function as the intercept in traditional regression models. Normally, each node of one layer has connections to all the other nodes of the next layer.

The network processes information as follows: the input nodes contain the value of the explanatory variables. Since each node connection represents a weight factor, the information reaches a single hidden layer node as the weighted sum of its inputs. Each node of the hidden layer passes the information through a nonlinear activation function and passes it on to the output layer if the calculated value is above a threshold.

The training of the network (which is the adjustment of its weights in the way that the network maps the input value of the training data to the corresponding output value) starts with randomly chosen weights and proceeds by applying a learning algorithm called backpropagation of errors<sup>2</sup> [45]. The learning algorithm simply tries to <sup>fi</sup>nd those weights which minimize an Error Function (normally the sum of all squared differences between target and actual values). Since networks with suf<sup>fi</sup>- cient hidden nodes are able to learn the training data (as well as their outliers and their noise) by heart, it is crucial to stop the training procedure at the right time to prevent over<sup>fi</sup>tting (this is called ‘early stopping’). This can be achieved by dividing the dataset into 3 subsets respectively called the training and test sets used for simulating the data currently available to <sup>fi</sup>t and tune the model and the validation set used for simulating future values. The training of a network is stopped when the mean squared forecasted error is at minimum in the test-sub period. The network parameters are then estimated by <sup>fi</sup>tting the training data using the above mentioned iterative procedure (backpropagation of errors). The iteration length is optimized by maximizing the forecasting accuracy for the test dataset. Then the predictive value of the model is evaluated applying it to the validation dataset (out-of-sample dataset).

Since the starting point for each network is a set of random weights, forecasts can differ between networks. In order to eliminate any variance between our NN forecasts and to add robustness to our results, we used the Simple Average of a committee of 10 NNs, which presented the highest pro<sup>fi</sup>t in the training sub-period. This was necessary in order to eliminate any outlier network that could jeopardize our conclusions. The characteristics of the NNs used in this paper are presented in Appendix B.

## 4.2.1. The Multi-Layer Perceptron Model (MLP)

MLPs are feed-forward layered NN, trained with a back-propagation algorithm. According to Kaastra and Boyd [34], they are the most commonly used types of arti<sup>fi</sup>cial networks in <sup>fi</sup>nancial time-series forecasting. The training of the MLP network is processed on a threelayered architecture, as described above. A typical MLP model is shown in Fig. 3.

Where:

$x _ { t } ^ { [ n ] } ( n = 1 , 2 , \cdots , k + 1 ) Z$ are the inputs (including the input bias node) at time t

$h _ { t } ^ { [ m ] } ( m { = } 1 , 2 , . . . , j { + } 1 ) Z$ are the hidden nodes outputs (including the hidden bias node) at time t

$\hat { Y } _ { t } Z$ is the MLP output

• u , w are the network weights

![](/api/attachments/KZREWN4Q/fulltext/images/51c6dfbe23492fb0640ff2031f062e6d6ffa7c14c51297edc8b28cda7bf370e9.jpg)  
Fig. 1. EUR/USD Frankfurt daily <sup>fi</sup>xing prices.

$\textcircled{5}$ is the transfer sigmoid function

$$
S (x) = \frac {1}{1 + e ^ {- x}}\tag{5}
$$

$\bigcirc$ is a linear function

$$
F (x) = \sum_ {i} x _ {i}.\tag{6}
$$

The Error Function to be minimized is

$$
E \Big (c, w _ {j} \Big) = \frac {1}{T} \sum_ {t = 1} ^ {T} \big (y _ {t} - \tilde {y} _ {t} (w _ {k}, c) \big) ^ {2}\tag{7}
$$

with y being the target value. The evaluation of the MLP model selected comes in terms of trading performance.

## 4.2.2. The Recurrent Neural Network (RNN)

The next model is the recurrent Neural Network. While a complete explanation of RNN models is beyond the scope of this paper, we present below a brief explanation of the signi<sup>fi</sup>cant differences between RNN and MLP architectures. For an exact speci<sup>fi</sup>cation of Recurrent Networks, see Elman [21].

A simple Recurrent Network has an activation feedback which embodies short-term memory. The advantages of using Recurrent Networks over feed-forward networks for modeling non-linear time series have been well documented in the past. However, as mentioned by Tenti [49], “the main disadvantage of RNNs is that they require substantially more connections, and more memory in simulation than the standard back-propagation networks” (p. 569), thus resulting in a substantial increase in computational time. However, having said this, RNNs can yield better results in comparison with simple MLPs due to the additional memory inputs. A simple illustration of the architecture of an Elman RNN is presented below (Fig. 4).

Where:

$x _ { t } ^ { [ n ] } ( n = 1 , 2 , . . . , k + 1 ) , u _ { t } ^ { [ 1 ] } , u _ { t } ^ { [ 2 ] } Z$ are the RNN inputs at time t (including bias node)

• $\tilde { y } _ { t }$ is the output of the RNN

$d _ { t } ^ { [ f ] } ( f = 1 , 2 )$ and $w _ { t } ^ { [ n ] } ( n = 1 , 2 , . . . , k + 1 )$ are the weights of the network

$U _ { t } ^ { [ f ] } , f = ( 1 , 2 )$ is the output of the hidden nodes at time t

$\textcircled{5}$ is the transfer sigmoid function: $\begin{array} { r } { S ( x ) = \frac { 1 } { 1 + e ^ { - x } } } \end{array}$

is a linear function: $F ( x ) = \sum _ { i } x _ { i } .$

The Error Function to be minimized is

$$
E (d _ {t}, w _ {t}) = \frac {1}{T} \sum_ {t = 1} ^ {T} \left(y _ {t} - \tilde {y} _ {t} (d _ {t}, w _ {t})\right) ^ {2}\tag{8}
$$

In short, the RNN architecture can provide more accurate outputs because the inputs are (potentially) taken from all previous values (see inputs $U _ { j - 1 } ^ { [ \hat { 1 } ] } .$ and $U _ { j - 1 } ^ { \left[ 2 \right] }$ in the <sup>fi</sup>gure above). The evaluation of the RNN model selected comes in terms of trading performance.

## 4.2.3. The Psi-Sigma Neural Network (PSN)

The PSNs are a class of Higher Order Neural Networks with a fully connected feed-forward structure. Ghosh and Shin [23] were the <sup>fi</sup>rst to introduce the PSN, trying to reduce the numbers of weights and connections of a Higher Order Neural Network. Their goal was to combine the fast learning property of single-layer networks with the mapping ability of Higher Order Neural Networks and avoid increasing the required number of weights. The training process is again three-layered. The PSN architecture of a one-output layer is shown in Fig. 5.

Where:

$x _ { t } \ ( n { = } 1 , 2 , { \ldots } , k { + } 1 )$ are the model inputs (including the input bias node)

![](/api/attachments/KZREWN4Q/fulltext/images/25baf8e69e3e558b5ef606166d6396f9fe39fca737241509c3c5a65adebea50e.jpg)  
Fig. 2. EUR/USD returns summary statistics.

Table 2 Explanatory variables.

<table><tr><td>Number</td><td>Explanatory variables</td><td>Lag $^{a}$ </td></tr><tr><td>1</td><td>EUR/USD exchange rate return</td><td>1</td></tr><tr><td>2</td><td>EUR/USD exchange rate return</td><td>2</td></tr><tr><td>3</td><td>EUR/USD exchange rate return</td><td>4</td></tr><tr><td>4</td><td>EUR/USD exchange rate return</td><td>5</td></tr><tr><td>5</td><td>EUR/USD exchange rate return</td><td>8</td></tr><tr><td>6</td><td>EUR/USD exchange rate return</td><td>10</td></tr><tr><td>7</td><td>EUR/GBP exchange rate return</td><td>1</td></tr><tr><td>8</td><td>EUR/GBP exchange rate return</td><td>2</td></tr><tr><td>9</td><td>EUR/JPY exchange rate return</td><td>1</td></tr></table>

<sup>a</sup> In our application the term ‘Lag 1’ means that today's closing price is used to forecast the tomorrow's one.

$\tilde { y } _ { t } Z$ is the PSN output

• w<sub>j</sub> $( j = 1 , 2 . . , k )$ are the adjustable weights (K is the desired order of the network)

$h ( x ) = \sum _ { i } x _ { i } { \mathrm { i } } { \mathrm { : } }$ the hidden layer activation function

ð<sup>9</sup>Þ

$\bullet \ \sigma ( x ) = { \frac { 1 } { 1 + e ^ { - x c } } }$ is the output sigmoid activation function

<sub>ð</sub><sup>10</sup><sub>Þ</sub>

c the adjustable term

The Error Function minimized is

$$
E \Big (c, w _ {j} \Big) = \frac {1}{T} \sum_ {t = 1} ^ {T} \left(y _ {t} - \tilde {y} _ {t} (w _ {k}, c)\right) ^ {2}\tag{11}
$$

with $y _ { t }$ being the target value. The training of the PSN is achieved also with the backpropagation and the ‘early-stopping’ procedure, as described in Section 4.2. The structure of the PSN and the sigmoid output function require the normalization of the inputs and the de-normalization of the outputs. Based on Ghazali et.al [22], our inputs are normalized between the values of 0.2 and 0.8 and at the end the outputs of the network are de-normalized back.

For example let us consider a Psi Sigma network which is fed with a N+1 dimensional input vector $x = ( 1 , x _ { 1 } , . . . , x _ { N } ) ^ { T } .$ . These inputs are weighted by K weight factors $\nu _ { j } = ( w _ { 0 j } , w _ { 1 j } , . . . , w _ { N j } ) ^ { T } , j = 1 , 2 , . . K$ and summed by a layer of K summing units, where K is the desired order of the network. So the output of the j-th summing unit,h in the hidden layer, is given by: $h _ { j } = w _ { j } ^ { T } x = \sum _ { k = 1 } ^ { N } w _ { k j } x _ { k } + w _ { o j } , \mathsf { j } = 1 , 2 , . . .$ , K while the output y\~ of the network is given by $\begin{array} { r } { \tilde { y } = \sigma \big ( \prod _ { j = 1 } ^ { K } h _ { j } \big ) } \end{array}$ . Note that by using products in the output layer we directly incorporate the capabilities of higher order networks with a smaller number of weights and processing units. For example, a k-th degree higher order Neural Network with d inputs needs $\sum _ { i = 0 } ^ { k } { \frac { ( d { + } i { - } 1 ) ! } { i ! ( d { + } 1 ) ! } }$ weights if all products of up to k components

are to be incorporated while a similar Psi Sigma network needs only $( \mathsf { d } + 1 ) _ { * } \mathsf { k }$ weights. Also note that the sigmoid function is neuron

![](/api/attachments/KZREWN4Q/fulltext/images/9ec8b87bdb59df8a2c977c6e239ccced53839f75a392506ffc883c34d665ad7e.jpg)  
Fig. 3. A single output, fully connected MLP model (bias nodes are not shown for simplicity).

Input Layer

![](/api/attachments/KZREWN4Q/fulltext/images/b77a2831728007cf8c4ea470c046e073ad8dc100c299e83fa08c97910ef075de.jpg)  
Fig. 4. Elman RNN with two nodes in the hidden layer.

adaptive. As the network is trained not only the weights but also c in Eq. (10) is adjusted. This strategy seems to provide better <sup>fi</sup>tting properties and increases the approximation capability of a Neural Network by introducing an extra variable in the estimation, compared to classical architectures with sigmoidal neurons [54].

The price for the <sup>fl</sup>exibility and speed of Psi Sigma networks is that they are not universal approximators. We need to choose a suitable order of approximation (or else the number of hidden units) by considering the estimated function complexity, amount of data and amount of noise present. To overcome this, our code runs simulations for orders two to six and then it presents the best network. The evaluation of the PSN model selected comes in terms of trading performance.

## 5. Forecasting combination techniques

In this section we present the <sup>fi</sup>ve techniques that we used to combine our NN forecasts. It is important to outline that a forecast combination targets either to follow the trend of the best individual forecast (‘combining for adaptation’) or to signi<sup>fi</sup>cantly outperform each one of them (‘combining for improvement’) [57]. Consequently, we decided to exclude the ARMA and the naive strategy from our combination techniques. Both strategies present a considerably worse trading performance than their NNs' counterparts both in-sample and out-of-sample. Therefore, their inclusion in our combination techniques will deteriorate their performance rather than improve it.

![](/api/attachments/KZREWN4Q/fulltext/images/cc33bc8d1f857d1d3187d12ffca3db322a0d30fd64f60d364d1d40bb63526a3b.jpg)  
Fig. 5. A PSN with one output layer.

Table 3 Summary of in-sample statistical performance.

<table><tr><td rowspan="2"></td><td colspan="2">Traditional techniques</td><td colspan="3">Neural Networks</td><td colspan="5">Forecast combinations</td></tr><tr><td>NAIVE</td><td>ARMA</td><td>MLP</td><td>RNN</td><td>PSN</td><td>Simple Average</td><td>Bayesian Average</td><td>GRR</td><td>LASSO</td><td>Kalman Filter</td></tr><tr><td>MAE</td><td>0.0065</td><td>0.0045</td><td>0.0044</td><td>0.0042</td><td>0.0039</td><td>0.0037</td><td>0.0037</td><td>0.0035</td><td>0.0038</td><td>0.0033</td></tr><tr><td>MAPE</td><td>399.44%</td><td>122.20%</td><td>97.13%</td><td>93.35%</td><td>89.43%</td><td>84.98%</td><td>85.13%</td><td>82.78%</td><td>87.63%</td><td>71.51%</td></tr><tr><td>RMSE</td><td>0.0086</td><td>0.0060</td><td>0.0053</td><td>0.0050</td><td>0.0041</td><td>0.0036</td><td>0.0036</td><td>0.0032</td><td>0.0037</td><td>0.0023</td></tr><tr><td>Theil-U</td><td>0.7021</td><td>0.6948</td><td>0.6686</td><td>0.5087</td><td>0.4292</td><td>0.4522</td><td>0.4625</td><td>0.4245</td><td>0.4613</td><td>0.2713</td></tr></table>

## 5.1. Simple Average

The <sup>fi</sup>rst forecasting combination technique used in this paper is Simple Average, which can be considered a benchmark forecast combination model. Given the three NNs' forecasts f <sup>t</sup> ,f <sup>t</sup> ,f <sup>t</sup> at time t, the combination forecast at time t is calculated as:

$$
f _ {c _ {N N s}} ^ {t} = \left(f _ {M L P} ^ {t} + f _ {R N N} ^ {t} + f _ {P S N} ^ {t}\right) / 3.\tag{12}
$$

## 5.2. Bayesian averaging

A Bayesian Average model speci<sup>fi</sup>es optimal weights for the combination forecast based on the Akaike Information Criterion (AIC) and Schwarz Bayesian Information Criterion (SIC). According to Buckland et al. [7] the Bayesian weights using AIC, can be estimated as:

$$
w _ {A I C, i} = \frac {e ^ {- 0 . 5 \Delta A I C _ {i}}}{\sum_ {j = 1} ^ {3} e ^ {- 0 . 5 \Delta A I C _ {j}}}\tag{13}
$$

Where:

• i = 1,2,3 for f<sub>MLP</sub>, f<sub>RNN</sub>, f<sub>PSN</sub>respectively

$$
\Delta A I C _ {i} = A I C _ {i} - A I C _ {i, m i n}.\tag{14}
$$

Based on the above, the combination forecast at time t is $f _ { c _ { N N s } } ^ { t } = \left( \sum _ { i = 1 } ^ { 3 } w _ { A I C , i } f _ { i } ^ { t } \right) ,$ =3 and in our case the AIC Bayesian models take the following form:

$$
f _ {c _ {A I C}} ^ {t} = \left(0. 3 3 4 2 0 9 9 8 8 f _ {M L P} ^ {t} + 0. 3 3 0 8 3 1 0 5 9 f _ {R N N} ^ {t} + 0. 3 3 4 9 5 8 9 5 3 f _ {P S N} ^ {t}\right) / 3.\tag{15}
$$

The Bayesian Average weights for SIC are de<sup>fi</sup>ned similarly and in our case the SIC Bayesian model is speci<sup>fi</sup>ed as follows:

$$
f _ {c _ {S I C}} ^ {t} = \left(0. 3 3 4 2 1 0 0 0 9 f _ {M L P} ^ {t} + 0. 3 3 0 8 3 1 0 8 1 f _ {R N N} ^ {t} + 0. 3 3 4 9 5 8 9 1 f _ {P S N} ^ {t}\right) / 3.\tag{16}
$$

Eqs. (15) and (16) are similar as the AIC and SIC criteria for our NNs in the in-sample period are very close. For that reason we will present only the Bayesian Average based on the AIC criterion, the one that presented a marginally better trading performance in-sample.

Nonetheless, the weights are in favor (maximized) of PSN, namely the model with the minimum AIC and SIC respectively. For details on the exact calculation of the AIC and SIC and their Bayesian Average weights see Appendix C.

## 5.3. Granger and Ramanathan Regression Approach (GRR)

According to Bates and Granger [4], a combining set of forecasts outperforms the individual forecasts that the set consists of. Taking this basic idea one step further, Granger and Ramanathan [26] suggested three regression models as follows:

$$
f _ {c 1} = a _ {0} + \sum_ {i = 1} ^ {n} a _ {i} f _ {i} + \varepsilon_ {1}\tag{[GRR - 1]}
$$

$$
f _ {c 2} = \sum_ {i = 1} ^ {n} a _ {i} f _ {i} + \varepsilon_ {2}\tag{[GRR - 2]}
$$

$$
f _ {c 3} = \sum_ {i = 1} ^ {n} a _ {i} f _ {i} + \varepsilon_ {3}, \quad w h e r e \quad \sum_ {i = 1} ^ {n} a _ {i} = 1\tag{[GRR - 3]}
$$

Where

$f _ { i } , i { = } 1 , . . . , n$ are the individual one-step-ahead forecasts,

$f _ { c l } , f _ { c 2 } , f _ { c 3 }$ are the combination forecast of each model,

• $\alpha _ { 0 }$ is the constant term of the regression

• α are the regression coef<sup>fi</sup>cients of each model

$\varepsilon _ { 1 } , \varepsilon _ { 2 } , \varepsilon _ { 3 }$ are the error terms of each regression model.

The GRR-1 model, which was selected for our case, is usually preferred in order to avoid forecast errors correlated with the individual forecasts f [48]. Thus, the GRR model at time t used in this paper is speci<sup>fi</sup>ed as shown below:

$$
f _ {c _ {N N s}} ^ {t} = 0. 0 4 2 2 + 3 5. 0 2 3 f _ {M L P} ^ {t} + 1 3. 4 6 1 f _ {R N N} ^ {t} + 5 6. 1 3 2 f _ {P S N} ^ {t} + \varepsilon_ {t}.\tag{17}
$$

However, the variety of data and the biased and correlated forecasts raise questions on GRR model selection or modi<sup>fi</sup>cation, which are further discussed in the literature [9,12].

## 5.4. Least Absolute Shrinkage and Selection Operator (LASSO)

The LASSO Regression is a class of Shrinkage or Regularization Regressions, which applies when multicollinearity exists among the regressors [47]. The main difference between this technique and the Ordinary Least Squares (OLS) Regression is that LASSO method also minimizes the residual squared error, by adding a coef<sup>fi</sup>cient constraint (similarly to Ridge Regression [8]).

Summary of out-of-sample statistical performance

<table><tr><td rowspan="2"></td><td colspan="2">Traditional techniques</td><td colspan="3">Neural Networks</td><td colspan="5">Forecast combinations</td></tr><tr><td>NAIVE</td><td>ARMA</td><td>MLP</td><td>RNN</td><td>PSN</td><td>Simple Average</td><td>Bayesian Average</td><td>GRR</td><td>LASSO</td><td>Kalman Filter</td></tr><tr><td>MAE</td><td>0.0084</td><td>0.0059</td><td>0.0058</td><td>0.0056</td><td>0.0048</td><td>0.0048</td><td>0.0048</td><td>0.0047</td><td>0.0046</td><td>0.0044</td></tr><tr><td>MAPE</td><td>405.62%</td><td>131.20%</td><td>112.37%</td><td>105.97%</td><td>97.88%</td><td>94.07%</td><td>93.76%</td><td>92.83%</td><td>92.05%</td><td>88.37%</td></tr><tr><td>RMSE</td><td>0.0107</td><td>0.0077</td><td>0.0061</td><td>0.0060</td><td>0.0054</td><td>0.0053</td><td>0.0051</td><td>0.0049</td><td>0.0053</td><td>0.0043</td></tr><tr><td>Theil-U</td><td>0.7958</td><td>0.8749</td><td>0.7301</td><td>0.6001</td><td>0.4770</td><td>0.5672</td><td>0.5598</td><td>0.5297</td><td>0.6142</td><td>0.5212</td></tr></table>

Table 5  
Summary results of Diebold–Mariano statistic for MSE and MAS loss functions.

<table><tr><td></td><td>NAIVE</td><td>ARMA</td><td>MLP</td><td>RNN</td><td>PSN</td><td>Simple Average</td><td>Bayesian Average</td><td>GRR</td><td>LASSO</td></tr><tr><td> $s_{MSE}$ </td><td>-9.307</td><td>-9.321</td><td>-6.244</td><td>-5.698</td><td>-5.184</td><td>-4.869</td><td>-4.896</td><td>-4.351</td><td>-4.112</td></tr><tr><td> $s_{MAE}$ </td><td>-9.845</td><td>-9.832</td><td>-9.189</td><td>-8.881</td><td>-8.159</td><td>-7.851</td><td>-7.873</td><td>-7.679</td><td>-7.352</td></tr></table>

Compared to Ridge Regression, LASSO best applies in samples of few variables with medium/large effect such in our case [29]. For more details on the mathematical speci<sup>fi</sup>cations of LASSO see Wang et al. [55]. Given the vectors of independent and dependent variables:

$$
\left( \begin{array}{c} X _ {1} ^ {T} \\ \vdots \\ X _ {N} ^ {T} \end{array} \right) = \left( \begin{array}{c c c} x _ {1 1} & ... & x _ {1 N} \\ \vdots & \ddots & \vdots \\ x _ {N 1} & ... & x _ {N N} \end{array} \right), \quad Y = (y _ {1},..., y _ {N}) ^ {T}\tag{18}
$$

and the training data $\{ ( X _ { 1 } , y _ { 1 } ) , . . . , ( X _ { N } , y _ { N } ) \}$ , the LASSO coef<sup>fi</sup>cients are estimated based on the following argument:

$$
\hat {\beta} _ {l a s s o} = \arg \min _ {\beta} \left\{\sum_ {i = 1} ^ {N} \left(y _ {i} - \beta_ {0} - \sum_ {j = 1} ^ {d} \beta_ {i} x _ {i j}\right) ^ {2} \right\} \quad s u b j e c t t o \quad \sum_ {j = 1} ^ {d} \left| \beta_ {j} \right| \leq k, k > 0.\tag{19}
$$

The argument (19) is based on Breiman's non-negative garrote minimization process [58]. Here k stands for the ‘tuning parameter’, because it controls the amount of shrinkage applied to the coef<sup>fi</sup>cients [52]. In our case, we experimented with various values of k in the in-sample period and we concluded that the best results in terms of trading performance are acquired when the constraint takes the following form:

$$
| \beta_ {M L P} | + | \beta_ {R N N} | + | \beta_ {P S N} | \leq 1 0. 6.\tag{20}
$$

Subject to this constraint our model takes the form:

$$
f _ {c _ {N N s}} ^ {t} = 3. 2 8 4 f _ {M L P} ^ {t} + 1. 5 9 1 f _ {R N N} ^ {t} + 5. 6 2 3 f _ {P S N} ^ {t} + \varepsilon_ {t}.\tag{21}
$$

This LASSO constraint makes the model adaptive, since it creates a penalization balance on each estimate, by leading some coef<sup>fi</sup>cients to zero or close to zero (see the unconstrained regression of GGR (17) compared to LASSO (21)).

## 5.5. Kalman Filter

Kalman Filter is an ef<sup>fi</sup>cient recursive <sup>fi</sup>lter that estimates the state of a dynamic system from a series of incomplete and noisy measurements.

The time-varying coef<sup>fi</sup>cient combination forecast suggested in this paper is shown below:

Measurement equation:

$$
f _ {c _ {N N s}} ^ {t} = \sum_ {i = 1} ^ {3} a _ {i} ^ {t} f _ {i} ^ {t} + \varepsilon_ {t}, \quad \varepsilon_ {t} \sim N I D (0, \sigma_ {\varepsilon} ^ {2})\tag{22}
$$

State equation:

$$
a _ {i} ^ {t} = a _ {i} ^ {t - 1} + n _ {t}, \quad n _ {t} \sim N I D \left(0, \sigma_ {n} ^ {2}\right)\tag{23}
$$

Where:

$f _ { _ { c N N s } } ^ { t }$ is the dependent variable (combination forecast) at time t $\stackrel { \triangledown } { f _ { i } ^ { t } } ( i = 1 , 2 , 3 )$ are the independent variables (individual forecasts) at time t

$a _ { i } ^ { t } ( i = 1 , 2 , 3 )$ are the time-varying coef<sup>fi</sup>cients at time t for each NN $\mathbf { } \varepsilon _ { t } , n _ { t }$ are the uncorrelated error terms (noise).

When Kalman Filter is applied, all a<sup>t</sup>are estimated in time, along with the log-likelihood of the model based on the observations up to time t. Then the likelihood function is maximized with a numerical optimization algorithm, based onσ<sup>2</sup>. The updated alphas for the state equation are estimated at time t based on the new observations at time t and then the state estimates are propagated in time t+1. Thus, the Kalman Filter update can be considered as the best unbiased linear estimate of the individual forecastsf<sup>t</sup>, given $\textbf { \textit { f } } _ { c N N s } ^ { t }$ and the prior information. After Kalman Filter and the numerical optimization algorithm, a Kalman smoothing algorithm should be applied, because the accuracy is increased to the end of the sample. This algorithm ‘smoothes’ the estimates by running backwards in time and using information acquired after time t and allows our model to compute forecasts, which use all available measurement data over the forecast sample.

Following Welch and Bishop [53] and Dunis et al. [14], in our study the alphas are calculated by a simple random walk and we initialized $\varepsilon _ { 1 } = 0 .$ . Based on the above, our Kalman Filter model has as a <sup>fi</sup>nal state the following:

$$
f _ {c _ {N N s}} ^ {t} = 5. 8 0 f _ {M L P} ^ {t} + 1. 1 6 f _ {R N N} ^ {t} + 7 5. 8 9 f _ {P S N} ^ {t} + \varepsilon_ {t}\tag{24}
$$

Summary of in-sample trading performance.

<table><tr><td rowspan="2"></td><td colspan="2">Traditional techniques</td><td colspan="3">Neural Networks</td><td colspan="5">Forecast combinations</td></tr><tr><td>NAIVE</td><td>ARMA</td><td>MLP</td><td>RNN</td><td>PSN</td><td>Simple Average</td><td>Bayesian Average</td><td>GRR</td><td>LASSO</td><td>Kalman Filter</td></tr><tr><td>Annualized return (excluding costs)</td><td>1.49%</td><td>13.87%</td><td>23.19%</td><td>26.14%</td><td>28.10%</td><td>32.74%</td><td>32.39%</td><td>33.99%</td><td>30.57%</td><td>42.63%</td></tr><tr><td>Annualized volatility</td><td>9.68%</td><td>9.70%</td><td>9.38%</td><td>9.59%</td><td>9.23%</td><td>9.51%</td><td>9.52%</td><td>9.49%</td><td>9.54%</td><td>9.35%</td></tr><tr><td>Information ratio (excluding costs)</td><td>0.15</td><td>1.43</td><td>2.47</td><td>2.73</td><td>3.05</td><td>3.44</td><td>3.4</td><td>3.58</td><td>3.21</td><td>4.56</td></tr><tr><td>Maximum drawdown</td><td>-8.59%</td><td>-6.52%</td><td>-5.91%</td><td>-6.55%</td><td>-6.55%</td><td>-6.55%</td><td>-6.55%</td><td>-6.55%</td><td>-6.55%</td><td>-6.66%</td></tr><tr><td>Annualized transactions</td><td>130</td><td>100</td><td>121</td><td>136</td><td>74</td><td>107</td><td>106</td><td>104</td><td>106</td><td>121</td></tr><tr><td>Transaction costs</td><td>0.91%</td><td>0.70%</td><td>0.85%</td><td>0.95%</td><td>0.52%</td><td>0.75%</td><td>0.74%</td><td>0.73%</td><td>0.74%</td><td>0.85%</td></tr><tr><td>Annualized return (including costs)</td><td>0.58%</td><td>13.17%</td><td>22.34%</td><td>25.19%</td><td>27.58%</td><td>31.99%</td><td>31.65%</td><td>33.26%</td><td>29.83%</td><td>41.78%</td></tr><tr><td>Information ratio (including costs)</td><td>0.06</td><td>1.36</td><td>2.38</td><td>2.63</td><td>2.99</td><td>3.36</td><td>3.32</td><td>3.50</td><td>3.13</td><td>4.47</td></tr></table>

Table Summary of out-of-sample trading performance.

<table><tr><td rowspan="2"></td><td colspan="2">Traditional techniques</td><td colspan="3">Neural Networks</td><td colspan="5">Forecast combinations</td></tr><tr><td>NAIVE</td><td>ARMA</td><td>MLP</td><td>RNN</td><td>PSN</td><td>Simple Average</td><td>Bayesian Average</td><td>GRR</td><td>LASSO</td><td>Kalman Filter</td></tr><tr><td>Annualized return (excluding costs)</td><td>-4.80%</td><td>10.60%</td><td>14.80%</td><td>16.07%</td><td>18.37%</td><td>16.37%</td><td>16.59%</td><td>16.99%</td><td>20.23%</td><td>28.79%</td></tr><tr><td>Annualized volatility</td><td>12.03%</td><td>11.07%</td><td>11.83%</td><td>11.02%</td><td>10.89%</td><td>10.85%</td><td>10.85%</td><td>11.02%</td><td>10.99%</td><td>10.92%</td></tr><tr><td>Information ratio (excluding costs)</td><td>-0.4</td><td>0.96</td><td>1.25</td><td>1.46</td><td>1.69</td><td>1.51</td><td>1.53</td><td>1.54</td><td>1.84</td><td>2.64</td></tr><tr><td>Maximum drawdown</td><td>-6.41%</td><td>-6.23%</td><td>-6.23%</td><td>-6.23%</td><td>-6.31%</td><td>-6.31%</td><td>-6.31%</td><td>-6.31%</td><td>-6.31%</td><td>-6.31%</td></tr><tr><td>Annualized transactions</td><td>77</td><td>54</td><td>71</td><td>71</td><td>76</td><td>70</td><td>71</td><td>63</td><td>69</td><td>73</td></tr><tr><td>Transaction costs</td><td>0.54%</td><td>0.38%</td><td>0.50%</td><td>0.50%</td><td>0.53%</td><td>0.49%</td><td>0.50%</td><td>0.44%</td><td>0.48%</td><td>0.51%</td></tr><tr><td>Annualized return (including costs)</td><td>-5.34%</td><td>10.22%</td><td>14.30%</td><td>15.57%</td><td>17.84%</td><td>15.88%</td><td>16.09%</td><td>16.55%</td><td>19.75%</td><td>28.28%</td></tr><tr><td>Information ratio (including costs)</td><td>-0.44</td><td>0.92</td><td>1.21</td><td>1.41</td><td>1.64</td><td>1.46</td><td>1.48</td><td>1.50</td><td>1.80</td><td>2.59</td></tr></table>

From the above equation we note that the Kalman <sup>fi</sup>ltering process favors the PSN model. This is what one would expect, since it is the model that performs best individually.

In order to achieve optimal Kalman Filter estimation, it is important though to introduce a noise ratio.

$$
n _ {r} = \sigma_ {\varepsilon} ^ {2} / \sigma_ {n} ^ {2}\tag{25}
$$

The results are becoming more adaptive when the noise ratio rises [14]. When $\begin{array} { r } { r _ { n } ^ { 2 } = 0 , } \end{array}$ , the model transforms to the typical OLS model. Appendix D describes the Kalman <sup>fi</sup>ltering and smoothing process.

## 6. Statistical performance

As it is standard in the literature, in order to evaluate statistically our forecasts, the RMSE, the MAE, the MAPE and the Theil-U statistics are computed (see among others Dunis and Williams [20] and Dunis and Chen [13]). The statistical analysis will provide some information regarding the accuracy of our forecasts and strengthen our conclusions. The RMSE and MAE statistics are scale-dependent measures but give a basis to compare volatility forecasts with the realized volatility while the MAPE and the Theil-U statistics are independent of the scale of the variables. In particular, the Theil-U statistic is constructed in such a way that it necessarily lies between zero and one, with zero indicating a perfect <sup>fi</sup>t. A more detailed description of these measures can be found on Pindyck and Rubinfeld [41] and Theil [51], while their mathematical formulas are presented in Appendix E. For all four of the error statistics retained (RMSE, MAE, MAPE and Theil-U) the lower the output, the better the forecasting accuracy of the model concerned. In Tables 3 and 4 we present the in-sample period and out-of-sample periods respectively.

We note that from our individual forecasts, the PSN outperformed all other models in both the in-sample and out-of-sample periods. Similarly, for our forecast combination methodologies the Kalman Filter beat its benchmarks for the four statistical criteria retained in both estimation periods. Adding to the above statistical performance of the Kalman Filter, the Diebold–Mariano [11] statistic for predictive accuracy is also computed for both MSE and MAE loss functions (for more details on the Diebold–Mariano statistic see Appendix F). The results of the Diebold–Mariano statistic, comparing Kalman <sup>fi</sup>lter with each other method, are summarized in Table 5.

## Table 8

Classi<sup>fi</sup>cation of leverage in sub-periods.

<table><tr><td></td><td>Extremely low vol.</td><td>Medium low vol.</td><td>Lower high vol.</td><td>Upper high vol.</td><td>Medium high vol.</td><td>Extremely high vol.</td></tr><tr><td>Leverage</td><td>2.5</td><td>2</td><td>1.5</td><td>1</td><td>0.5</td><td>0</td></tr></table>

From the above table we note that the null hypothesis of equal predictive accuracy is rejected for all comparisons and for both loss functions at 5% con<sup>fi</sup>dence interval, since the test results |s |>1.96 and $| s _ { M A E } | > 1 . 9 6 .$ . Moreover, the statistical superiority of the Kalman Filter forecasts is con<sup>fi</sup>rmed as for both loss functions the realizations of the Diebold–Mariano [11] statistic are negative.<sup>3</sup> We also note that our second best model in statistical terms, the LASSO regression, has the closest forecasts with Kalman Filter.

## 7. Trading performance

## 7.1. Trading strategy and transaction costs

The trading strategy applied in this paper is to go or stay ‘long’ when the forecast return is above zero and go or stay ‘short’ when the forecast return is below zero. The ‘long’ and ‘short’ EUR/USD positions are de<sup>fi</sup>ned as buying and selling Euros at the current price respectively. The transaction costs for a tradable amount, say USD 5–10 million, are about 1 pip (0.0001 EUR/USD) per trade (one way) between market makers. But since we consider the EUR/USD time series as a series of middle rates, the transaction costs are one spread per round trip. With an average exchange rate of EUR/USD of 1.369 for the out-of-sample period, a cost of 1 pip is equivalent to an average cost of 0.007% per position.

## 7.2. Trading performance before leverage

The trading performance measures and their calculation description are presented in Appendix E. In Table 6 we present the in-sample trading performance of our models and forecast combinations before and after transaction cost.

We note that all our models present a positive trading performance after transaction costs. From our single forecasts the PSN outperforms each NN and statistical benchmark in terms of annualized return and information ratio. Our other two arti<sup>fi</sup>cial intelligence models, the RNN and the MLP, present the second and third best trading performance respectively. Concerning our forecast combinations we observe that the Kalman Filter presents the best trading performance with an annualized return of 41.78% and an information ratio of 4.47 after transaction costs. It is also worth noting that all our forecast combinations outperform our best single forecast, the PSN in terms of trading performance. In Table 7 below we present the out-of-sample performance of our models before and after transaction costs.

![](/api/attachments/KZREWN4Q/fulltext/images/2e39d559882668f2c5a37ac74f9f7eda207587ce8e7117dcd73dbb7f983754fc.jpg)  
Fig. 6. Leverages assigned in the out-of-sample period.

From the last two rows of Table 7, we note that the PSN continues to outperform all other single forecasts in terms of trading performance. From our forecast combinations, only the Kalman Filter and the LASSO methods seem to beat our best single forecast. The Simple Average, Bayesian Average and GRR methods who demonstrated a better performance in the in-sample period seem unable to maintain this superiority in the out-of-sample period. Moreover, we note that the trading performance of the Bayesian Average and Simple Average strategies is very close. This was expected as the AIC and the BIC information criteria for our 3 NNs are very close in the in-sample period. On the other hand, the GRR strategy still outperforms the MLP and the RNN models in terms of annualized return and information ratio. That could be thought as a trend to adapt to the best individual performance (‘combining for adaptation’ [57]). We also note that the Kalman Filter achieves a 10% higher annualized return than our second best methodology, the LASSO regression. It seems that the ability of Kalman Filter to provide ef<sup>fi</sup>cient computational recursive means to estimate the state of our process gives it a considerable advantage compared to our <sup>fi</sup>xed parameters combination models.

## 7.3. Leverage to exploit high information ratios

In order to further improve the trading performance of our models we introduce a leverage based on RiskMetrics one day ahead volatility forecasts<sup>4</sup> (for more details on RiskMetrics model see Appendix G). The intuition of the strategy is to avoid trading when volatility is very high while at the same time exploiting days when the volatility is relatively low. As mentioned by Bertolini [5], there are few papers on market-timing techniques for foreign exchange, with the notable exception of Dunis and Miao [17,18]. The opposition between market-timing techniques and time-varying leverage is only apparent as time-varying leverage can also be easily achieved by scaling position sizes inversely to recent risk measures behavior.

Firstly, we forecast with RiskMetrics the one day ahead realized volatility of the EUR/USD exchange rate in the test and validation sub-periods. Then, following Dunis and Miao [17,18] we split these two periods into six sub-periods, ranging from periods with extremely low volatility to periods experiencing extremely high volatility. Periods with different volatility levels are classi<sup>fi</sup>ed in the following way: <sup>fi</sup>rst the average (μ) difference between the actual volatility in day t and the forecasted for day t+1 and its ‘volatility’ (measured in terms of standard deviation σ) are calculated; those periods where the difference is between μ plus one σ are classi<sup>fi</sup>ed as ‘Lower high vol. periods’. Similarly, ‘Medium high vol.’ (between μ+σ and μ+2σ) and ‘Extremely high vol.’ (above μ+2σ) periods can be de<sup>fi</sup>ned. Periods with low volatility are also de<sup>fi</sup>ned following the same 1σ and 2σ approach, but with a minus sign.

For each sub-period a leverage is assigned starting with 0 for periods of extremely high volatility to a leverage of 2.5 for periods of extremely low volatility (see for leverage factors [17,18]). Table 8 below presents the sub-periods and their relevant leverages.

The parameters of our strategy (μ and σ) are updated every three months by rolling forward the estimation period. So for example, for the <sup>fi</sup>rst three months of our validation period, μ and σ are computed based on the eighteen months of the test sub-period. For the following three months, the two parameters are computed based on the last <sup>fi</sup>fteen months of our test sub-period and the <sup>fi</sup>rst three of the validation sub-period. The leverages assigned in the days of the out-of-sample period, based on the above strategy are summarized in the following <sup>fi</sup>gure (Fig. 6).

The cost of leverage (interest payments for the additional capital) is calculated at 1.75%p.a. (that is 0.0069% per trading day<sup>5</sup>). Our <sup>fi</sup>nal results are presented in Table 9 below.

The most striking performance achieved by the time-varying leverage strategy is the signi<sup>fi</sup>cant reduction in the maximum drawdown, the essence of risk for an investor in <sup>fi</sup>nancial markets. Not only do all models, except ARMA, experience a higher performance in terms of return or risk-adjusted return, but maximum drawdowns are reduced by as much as 50%, from 6.31% to 3.38% in the case of the Kalman Filter combination! Even the naive strategy seems to try to invert its previous discouraging performance (see Table 9). The PSN still outperforms every NN and increases its annualized pro<sup>fi</sup>t over 3%. Similarly our Bayesian Average and Simple Average combination methods present a 3% increase of annualized return, but they still cannot outperform the PSN and RNN individual performance. Our other two forecast combination techniques, the GGR and the LASSO, also present an increased annualized return and information ratio. Finally, the Kalman Filter continues to present a remarkable trading performance with the highest information ratio and a 5.67% increase in terms of annualized return. When transaction and leverage costs are included, the pro<sup>fi</sup>t decreases, but the trend of the results is not affected. That allows us to conclude, that in all cases the Kalman Filter

Summary of out-of-sample trading performance — <sup>fi</sup>nal results<sup>6</sup>

<sup>6</sup> Not taken into account the interest that could be earned during times where the capital is not traded (non-trading days) or not fully invested and could therefore be invested.

<table><tr><td rowspan="2"></td><td colspan="2">Traditional techniques</td><td colspan="3">Neural Networks</td><td colspan="5">Forecast combinations</td></tr><tr><td>NAIVE</td><td>ARMA</td><td>MLP</td><td>RNN</td><td>PSN</td><td>Simple Average</td><td>Bayesian Average</td><td>GRR</td><td>LASSO</td><td>Kalman Filter</td></tr><tr><td>Annualized return (excluding costs)</td><td>-2.34%</td><td>7.28%</td><td>18.13%</td><td>19.44%</td><td>22.28%</td><td>19.12%</td><td>19.36%</td><td>22.37%</td><td>25.08%</td><td>34.46%</td></tr><tr><td>Annualized volatility</td><td>10.14%</td><td>10.44%</td><td>9.90%</td><td>9.04%</td><td>9.85%</td><td>9.09%</td><td>9.13%</td><td>9.38%</td><td>9.20%</td><td>9.32%</td></tr><tr><td>Information ratio (excluding costs)</td><td>-0.23</td><td>0.7</td><td>1.83</td><td>2.15</td><td>2.26</td><td>2.1</td><td>2.12</td><td>2.38</td><td>2.73</td><td>3.7</td></tr><tr><td>Maximum drawdown</td><td>-3.50%</td><td>-3.20%</td><td>-3.66%</td><td>-3.14%</td><td>-3.66%</td><td>-2.98%</td><td>-3.21%</td><td>-2.83%</td><td>-2.94%</td><td>-3.38%</td></tr><tr><td>Annualized transactions</td><td>122</td><td>90</td><td>115</td><td>117</td><td>122</td><td>111</td><td>113</td><td>97</td><td>110</td><td>114</td></tr><tr><td>Average leverage factor (ex post) $^a$ </td><td>n.a.</td><td>n.a.</td><td>1.13</td><td>1.19</td><td>1.12</td><td>1.09</td><td>1.09</td><td>1.26</td><td>1.18</td><td>1.15</td></tr><tr><td>Transaction and leverage costs</td><td>1.79%</td><td>1.57%</td><td>1.74%</td><td>1.75%</td><td>1.79%</td><td>1.72%</td><td>1.73%</td><td>1.62%</td><td>1.71%</td><td>1.73%</td></tr><tr><td>Annualized return (including costs)</td><td>-4.13%</td><td>5.71%</td><td>16.39%</td><td>17.69%</td><td>20.49%</td><td>17.40%</td><td>17.63%</td><td>20.75%</td><td>23.37%</td><td>32.73%</td></tr><tr><td>Information ratio (including costs)</td><td>-0.41</td><td>0.55</td><td>1.66</td><td>1.96</td><td>2.08</td><td>1.91</td><td>1.93</td><td>2.21</td><td>2.54</td><td>3.51</td></tr></table>

<sup>a</sup> The average leverage factor ex post is computed as the ratio of the annualized returns after costs of Tables 7 and 9 for those models which achieved an in-sample information ratio of at least 2 and, as such, would have been candidates for leveraging out-of-sample.

can be considered by far the optimal forecast combination for our dataset and the models under study.

## 8. Concluding remarks

In this paper we investigate the trading and statistical performance of a Neural Network (NN) architecture, the Psi Sigma Neural Network (PSN), and explore the utility of Kalman Filters in combining NN forecasts. Firstly, we apply the EUR/USD European Central Bank (ECB) <sup>fi</sup>xing series to a Naive Strategy, an Autoregressive Moving Average (ARMA) model and three NNs, namely a Multi-Layer Perceptron (MLP), a Recurrent Network (RNN) and a PSN. Secondly, we compare a Kalman <sup>fi</sup>lterbased combination with four other forecast combination methods. That is the traditional Simple Average, the Bayesian Average, Granger–Ramanathan's Regression Approach (GRR) and the Least Absolute Shrinkage and Selection Operator (LASSO). The models' performance is estimated through the EUR/USD ECB <sup>fi</sup>xing series of the period of 2002–2010, using the last two years for out-of-sample testing. We also introduce a time-varying leverage strategy based on RiskMetrics volatility forecasts.

As it turns out, the PSN outperforms its benchmark models in terms of statistical accuracy and trading performance. It is also shown that all the forecast combinations, outperform out-of-sample all our single models except the PSN for the statistical and trading terms retained. It is interesting that the ‘combining for improvement’ pattern that all combination forecasts showed in the in-sample period pattern, changes regarding the out-of-sample combination forecasts. Simple Average, Bayesian Average and GRR do not continue to outperform PSNs' best individual performance but are better than MLP and RNN, while LASSO and Kalman Filter present the best results. It seems that the ability of Kalman Filter to provide ef<sup>fi</sup>cient computational recursive means to estimate the state of our process gives it a considerable advantage compared to our <sup>fi</sup>xed parameters combination models. Finally, all models except ARMA show a substantial increase in their trading performance and a striking reduction in maximum drawdowns after applying timevarying leverage with Kalman Filter still being the best approach. The remarkable trading performance of Kalman Filter allows us to conclude that it can be considered as an optimal forecast combination for the models and time-series under study.

Our results should go some way towards convincing a growing number of quantitative fund managers to experiment beyond the bounds of the more traditional models and trading strategies. The results in Table 9, with an information ratio in excess of 3, should also provide motivation for the use of Kalman Filter in combining model based forecasts.

## Appendix A. The ARMA model

Fig. A.1 shows the output of the ARMA model selected. The null hypothesis that all the coef<sup>fi</sup>cients are not signi<sup>fi</sup>cantly different from zero is rejected at 95% con<sup>fi</sup>dence interval.

Dependent Variable: SAMPLE Method: Least Squares Date: 06/03/11 Time: 02:59 Sample (adjusted): 14 1781 Included observations: 1768 after adjustments Convergence achieved after 47 iterations MA Backcast: 1 13

<table><tr><td>Variable</td><td>Coefficient</td><td>Std. Error</td><td>t-Statistic</td><td>Prob.</td></tr><tr><td>C</td><td>0.028801</td><td>0.014372</td><td>2.004036</td><td>0.0452</td></tr><tr><td>AR(3)</td><td>-0.268915</td><td>0.089710</td><td>-2.997613</td><td>0.0028</td></tr><tr><td>AR(4)</td><td>0.602842</td><td>0.030519</td><td>19.75272</td><td>0.0000</td></tr><tr><td>AR(6)</td><td>-0.392114</td><td>0.033178</td><td>-11.81842</td><td>0.0000</td></tr><tr><td>AR(9)</td><td>-0.688370</td><td>0.069511</td><td>-9.903014</td><td>0.0000</td></tr><tr><td>AR(13)</td><td>0.364073</td><td>0.045366</td><td>8.025222</td><td>0.0000</td></tr><tr><td>MA(3)</td><td>0.263776</td><td>0.098488</td><td>2.678264</td><td>0.0075</td></tr><tr><td>MA(4)</td><td>-0.589976</td><td>0.033434</td><td>-17.64616</td><td>0.0000</td></tr><tr><td>MA(6)</td><td>0.391560</td><td>0.035648</td><td>10.98413</td><td>0.0000</td></tr><tr><td>MA(9)</td><td>0.622728</td><td>0.074974</td><td>8.305911</td><td>0.0000</td></tr><tr><td>MA(13)</td><td>-0.316544</td><td>0.049824</td><td>-6.353206</td><td>0.0000</td></tr><tr><td>R-squared</td><td>0.017546</td><td colspan="2">Mean dependent var</td><td>0.028818</td></tr><tr><td>Adjusted R-squared</td><td>0.011955</td><td colspan="2">S.D. dependent var</td><td>0.612764</td></tr><tr><td>S.E. of regression</td><td>0.609090</td><td colspan="2">Akaike info criterion</td><td>1.852501</td></tr><tr><td>Sum squared resid</td><td>651.8306</td><td colspan="2">Schwarz criterion</td><td>1.886581</td></tr><tr><td>Log likelihood</td><td>-1626.611</td><td colspan="2">Hannan-Quinn criter.</td><td>1.865093</td></tr><tr><td>F-statistic</td><td>3.137972</td><td colspan="2">Durbin-Watson stat</td><td>1.991296</td></tr><tr><td>Prob(F-statistic)</td><td>0.000549</td><td colspan="2"></td><td></td></tr><tr><td rowspan="4">Inverted AR Roots</td><td>.92+.38i</td><td>.92-.38i</td><td>.80</td><td>.47-.81i</td></tr><tr><td>.47+.81i</td><td>-.01+1.00i</td><td>-.01-1.00i</td><td>-.10-.82i</td></tr><tr><td>-.10+.82i</td><td>-.76-.58i</td><td>-.76+.58i</td><td>-.92+.04i</td></tr><tr><td>-.92-.04i</td><td colspan="2"></td><td></td></tr><tr><td rowspan="5">Inverted MA Roots</td><td colspan="4">Estimated AR process is nonstationary</td></tr><tr><td>.91-.38i</td><td>.91+.38i</td><td>.79</td><td>.47-.80i</td></tr><tr><td>.47+.80i</td><td>-.01-1.00i</td><td>-.01+1.00i</td><td>-.10-.81i</td></tr><tr><td>-.10+.81i</td><td>-.75+.57i</td><td>-.75-.57i</td><td>-.91+.05i</td></tr><tr><td>-.91-.05i</td><td colspan="2"></td><td></td></tr></table>

Fig. A.1. The ARMA model detailed output.

## Appendix B. NNs' training characteristics

In Table B.1 we present the characteristics of the Neural Networks with the best trading performance in the test sub-period which we used in our committees. The choice of these parameters is based on an extensive experimentation in the in-sample sub-period and on the relevant literature [13,22,49]. For example for the number of iterations, we started our experimentation from 10.000 iterations and we stopped at the 200.000 iterations, increasing in each experiment the number of iterations by 5.000.

Table B.1  
The NNs' training characteristics.

<table><tr><td>Parameters</td><td>MLP</td><td>RNN</td><td>PSN</td></tr><tr><td>Learning algorithm</td><td>Gradient descent</td><td>Gradient descent</td><td>Gradient descent</td></tr><tr><td>Learning rate</td><td>0.001</td><td>0.001</td><td>0.5</td></tr><tr><td>Momentum</td><td>0.003</td><td>0.004</td><td>0.5</td></tr><tr><td>Iteration steps</td><td>100,000</td><td>60,000</td><td>40,000</td></tr><tr><td>Initialisation of weights</td><td>N(0,1)</td><td>N(0,1)</td><td>N(0,1)</td></tr><tr><td>Input nodes</td><td>9</td><td>9</td><td>9</td></tr><tr><td>Hidden nodes</td><td>7</td><td>5</td><td>4</td></tr><tr><td>Output node</td><td>1</td><td>1</td><td>1</td></tr></table>

## Appendix C. Bayesian Information Criteria

AIC measures the relative goodness of <sup>fi</sup>t of a statistical model, as introduced by Akaike [1]. On the other hand, SIC (also known as BIC or SBIC [43]) is considered a criterion to select the best model among models with different numbers of parameters. If N is the sample size of the dataset, k the total number of parameters in the equation of interest and $s ^ { 2 }$ the maximum likelihood estimate of the error variance, then AIC and BIC are calculated as shown below:

$$
A I C = N \log \left(s ^ {2}\right) + 2 k, S I C = N \log \left(s ^ {2}\right) + k \log (N)\tag{C.1}
$$

Table C.1  
Calculation of weights for the AIC and SIC Bayesian Averaging model.

<table><tr><td></td><td>AIC</td><td>SIC</td><td> $\Delta_{AIC}$ </td><td> $\Delta_{SIC}$ </td><td> $W_{AIC}$ </td><td> $W_{SIC}$ </td></tr><tr><td>MLP</td><td>1.825879871</td><td>1.832039254</td><td>0.004476988</td><td>0.004476604</td><td>0.334209988</td><td>0.334210009</td></tr><tr><td>RNN</td><td>1.846203174</td><td>1.852362557</td><td>0.024800291</td><td>0.024799907</td><td>0.330831059</td><td>0.330831081</td></tr><tr><td>PSN</td><td>1.821402883</td><td>1.827562265</td><td>0</td><td>0</td><td>0.334958953</td><td>0.33495891</td></tr></table>

Table C.1 describes the estimation of the Bayesian Information Criteria for the cases of MLP, RNN and PSN forecasts, based on Eq. (13).

## Appendix D. Kalman Filter and smoothing process

A generalized linear state space model of the nx1 vector $y _ { t }$ is de<sup>fi</sup>ned as:

$$
y _ {t} = c _ {t} + Z _ {t} a _ {t} + \varepsilon_ {t}, \varepsilon_ {t} \sim N I D (0, \sigma_ {\varepsilon} ^ {2}) a n d a _ {t + 1} = d _ {t} + T _ {t} a _ {t} + n _ {t}, n _ {t} \sim N I D (0, \sigma_ {n} ^ {2})\tag{D.1}
$$

where $\alpha _ { t }$ is a mx1 vector of possible state variables and $c _ { t } , Z _ { t } , d _ { t }$ and $T _ { t }$ are conformable vectors and matrixes.

The $\varepsilon _ { t }$ and $n _ { t }$ vectors are assumed to be serially independent, with contemporaneous variance structure:

$$
\Omega_ {t} = \operatorname{var} _ {t} \left[ \begin{array}{c} \varepsilon_ {t} \\ n _ {t} \end{array} \right] = \left[ \begin{array}{c c} H _ {t} & G _ {t} \\ G _ {t} ^ {\prime} & Q _ {t} \end{array} \right]\tag{D.2}
$$

where $H _ { t }$ is a nxn symmetric variance matrix, $Q _ { t }$ is a mxm symmetric variance matrix and $G _ { t }$ is a nxm matrix of covariances [56].

If now we consider the conditional distribution of the state vector $\alpha _ { t } ,$ given information available at time t-1, we can de<sup>fi</sup>ne with the Kalman Filter the mean and variance matrix of the conditional distribution as:

$$
a _ {t | t - 1} = E _ {t - 1} (a _ {t})\tag{D.3}
$$

$$
P _ {t | t - 1} = E _ {t - 1} \left[ \left(a _ {t} - a _ {t | t - 1}\right) \left(a _ {t} - a _ {t | t - 1}\right) ^ {\prime} \right].\tag{D.4}
$$

Thus, the recursive algorithm of the Kalman <sup>fi</sup>lter calculates the following three:

1. The one-step ahead mean $\alpha _ { t | t - 1 }$ and one-step ahead variance $P _ { t \vert t - 1 }$ of the states. Under the Gaussian error assumption, $\alpha _ { t \vert t - 1 }$ is the minimum mean square error estimator of $\dot { } \alpha _ { t }$ and $P _ { t \vert t - \cdot }$ is the mean square error (MSE) of $\alpha _ { t \vert t - 1 }$

2. The one-step ahead estimate of $y _ { t }$ as:

$$
\hat {y} _ {t} = y _ {t | t - 1} = E _ {t - 1} (y _ {t}) = E (y _ {t} | a _ {t | t - 1}) = c _ {t} + Z _ {t} a _ {t | t - 1}.\tag{D.5}
$$

3. The one-step ahead prediction errors and their variances respectively as:

$$
\hat {\varepsilon} _ {t} = \varepsilon_ {t | t - 1} = y _ {t} - \hat {y} _ {t | t - 1}, \quad \hat {F} _ {t} = F _ {t | t - 1} = \mathrm{var} \Big (\varepsilon_ {t | t - 1} \Big) = Z _ {t} P _ {t | t - 1} Z _ {t} ^ {\prime} + H _ {t}.\tag{D.6}
$$

In our case, we set $\hat { y } _ { 0 } = 0$ and $\mathrm { P } _ { 0 } = 1$ . If $\mathrm { P } _ { 0 }$ was also set equal to zero, that would mean that there is no noise, so all the estimates would be equal to the initial state. Then, the next step is to embody a smoothing algorithm to our process. The smoothing algorithm, which uses all the information observed, in other words the whole sample T, to form expectations at any period until T, is known as <sup>fi</sup>xed-interval smoothing. In this way it is possible to estimate the smooth estimates of the states and the variances:

$$
\hat {\alpha} _ {t} = a _ {t | T = E _ {T} (a _ {t}) a n d V _ {t} = \mathrm{var} _ {T} (a _ {t})}\tag{D.7}
$$

Additionally, not only the smoothed estimates of y and their variances can be calculated based on Eqs. (D.5) and (D.6) respectively, but als the smoothed estimates of the $\varepsilon _ { t }$ and $n _ { t }$ vectors and their corresponding smoothed variance matrix:

$$
\hat {\varepsilon} _ {t} = \varepsilon_ {t | T} = E _ {T} (\varepsilon_ {t}), \hat {n} _ {t} = n _ {t | T} = E _ {T} (n _ {t}) a n d \hat {\Omega} _ {t} = \operatorname{var} _ {t} \left[ \begin{array}{c} \hat {\varepsilon} _ {t} \\ \hat {n} _ {t} \end{array} \right] = \left[ \begin{array}{c c} \hat {H} _ {t}, & \hat {G} _ {t} \\ \hat {G} _ {t}, & \hat {Q} _ {t} \end{array} \right].\tag{D.8}
$$

## Appendix E. The statistical and trading performance measures

The statistical and trading performance measures are calculated as shown in Tables E.1 and TE.2 respectively:

Table E.1  
The statistical performance measures and their calculation description.

<table><tr><td>Performance measures</td><td>Description</td></tr><tr><td>Mean absolute error</td><td> $MAE = \left( \frac{1}{n} \right) \sum_{\tau=t+1}^{t+n} |\hat{\sigma}_{\tau}-\sigma_{\tau}|$ with  $\sigma_{\tau}$  being the actual volatility and  $\hat{\sigma}_{\tau}$  the forecasted value</td></tr><tr><td>Mean absolute percentage error</td><td> $MAPE = \frac{1}{n} \sum_{\tau=t+1}^{t+n} \left| \frac{\sigma_{\tau}-\hat{\sigma}_{\tau}}{\sigma_{\tau}} \right|$ </td></tr><tr><td>Root mean squared error</td><td> $RMSE = \sqrt{\frac{1}{n} \sum_{\tau=t+1}^{t+n} (\hat{\sigma}_{\tau}-\sigma_{\tau})^2}$ </td></tr><tr><td>Theil-U</td><td> $Theil-U = \sqrt{ \left( \frac{ \frac{1}{n} \sum_{\tau=t+1}^{t+n} (\hat{\sigma}_{\tau}-\sigma_{\tau})^2 }{ \sqrt{ \frac{1}{n} \sum_{\tau=t+1}^{t+n} \hat{\sigma}_{\tau}^2 } + \sqrt{ \frac{1}{n} \sum_{\tau=t+1}^{t+n} \sigma_{\tau}^2 } } \right) }$ </td></tr></table>

Table E.2  
The trading performance measures and their calculation description.

<table><tr><td>Performance measures</td><td>Description</td></tr><tr><td>Annualized return</td><td> $R^{A} = 252 * \frac{1}{N} * \left( \sum_{t=1}^{N} R_{t} \right)$  where  $R_{t}$  the daily return</td></tr><tr><td>Cumulative return</td><td> $R^{C} = \sum_{t=1}^{N} R_{t}$ </td></tr><tr><td>Annualized volatility</td><td> $\sigma^{A} = \sqrt{252} * \sqrt{\frac{1}{N-1} * \sum_{t=1}^{N} (R_{t} - \bar{R})^{2}}$ </td></tr><tr><td>information ratio</td><td> $SR = \frac{R^{A}}{\sigma^{A}}$ </td></tr><tr><td>Maximum drawdown</td><td>Maximum negative value of  $\sum (R_{t})$  over the period  $MD = Min_{i=1,\cdots,t:t=1,\cdots,N} \left( \sum_{j=i}^{t} R_{j} \right)$ </td></tr></table>

## Appendix F. Diebold–Mariano statistic for predictive accuracy

The Diebold–Mariano [11] statistic tests the null hypothesis of equal predictive accuracy. If n is the sample size and $e _ { i } ^ { 1 } , e _ { i } ^ { 2 } ( \mathrm { i } = 1 , 2 . . . \mathrm { n } )$ are the forecast errors of the two competing forecasts, then the loss functions are estimated as:

$$
L _ {1} ^ {M S E} \left(e _ {i} ^ {1}\right) = \left(e _ {i} ^ {1}\right) ^ {2}, L _ {2} ^ {M S E} \left(e _ {i} ^ {2}\right) = \left(e _ {i} ^ {2}\right) ^ {2}\tag{F.1}
$$

$$
L _ {1} ^ {M A E} \left(e _ {i} ^ {1}\right) = \left| e _ {i} ^ {1} \right|, L _ {2} ^ {M A E} \left(e _ {i} ^ {2}\right) = \left| e _ {i} ^ {2} \right|.\tag{F.2}
$$

The Diebold–Mariano statistic is based on the loss differentials:

$$
d _ {i} ^ {M S E} = L _ {1} ^ {M S E} \left(e _ {i} ^ {1}\right) - L _ {2} ^ {M S E} \left(e _ {i} ^ {2}\right)\tag{F.3}
$$

$$
d _ {i} ^ {M A E} = L _ {1} ^ {M A E} \left(e _ {i} ^ {1}\right) - L _ {2} ^ {M A E} \left(e _ {i} ^ {2}\right).\tag{F.4}
$$

The null hypotheses tested based on the s<sub>MSE</sub> and s<sub>MAE</sub> are:

$H _ { 0 } : E ( d _ { i } ^ { M S E } ) = 0 \mathrm { Z }$ against the alternative $H _ { 1 } : E ( d _ { i } ^ { M S E } ) \neq 0$

$\bullet \ H _ { 0 } : E ( d _ { i } ^ { M A E } ) = 0 Z$ against the alternative $H _ { 1 } : E ( d _ { i } ^ { M A E } ) \neq 0$

The Diebold–Mariano test statistic s is estimated as:

$$
s = \frac {\bar {d} _ {i}}{\sqrt {\hat {V} (\bar {d} _ {i})}} \quad \xrightarrow {d} N (0, 1)\tag{F.5}
$$

where

$$
V (\bar {d} _ {i}) = n ^ {- 1} \left[ \hat {\gamma} _ {0} + 2 \sum_ {k = 1} ^ {n - 1} \hat {\gamma} _ {k} \right] a n d \gamma_ {k} = n ^ {- 1} \sum_ {i = k + 1} ^ {n} (d _ {i} - \bar {d} _ {i}) (d _ {i - k} - \bar {d} _ {i})\tag{F.6}
$$

## Appendix G. RiskMetrics Volatility Model

The RiskMetrics Volatility Model is a special case of the general Exponential Weighted Moving Average Model (EWMA). The EWMA suggests that the variance of a <sup>fi</sup>nancial asset can be calculated using the formula:

$$
\sigma_ {t} ^ {2} = \lambda \sigma_ {t - 1} ^ {2} + (1 - \lambda) r _ {t - 1} ^ {2}\tag{G.1}
$$

where $\sigma _ { t - 1 } ^ { 2 } \mathrm { i } s$ the EWMA variance at time $t - 1 , \ r _ { t - 1 } ^ { 2 }$ the squared returns at time $t - 1$ and λ a weight between 0 and 1. The RiskMetrics Volatility Model assumes that the weight $\lambda { = } 0 . 9 4$ . So in our case, we estimate the daily volatility with the formula below:

RiskMetricsVol $= \sqrt { 0 . 9 4 \sigma _ { t - 1 } ^ { 2 } + 0 . 0 6 r _ { t - 1 } ^ { 2 } } .$

<sub>ð</sub>G:2<sub>Þ</sub>

## References

[1] H. Akaike, A new look at the statistical model identi<sup>fi</sup>cation, IEEE Transactions on Automatic Control 19 (6) (1974) 716–723.

[2] E. Alfaro, N. García, M. Gamez, D. Elizondo, Bankruptcy forecasting: an empirical comparison of AdaBoost and neural networks, Decision Support Systems 45 (1) (2008) 110–122.

[3] G. Anandalingam, L. Chen, Linear combination of forecasts: a general Bayesian model, Journal of Forecasting 8 (3) (1989) 199–214.

[4] J.M. Bates, C.W.J. Granger, The combination of forecasts, Operational Research Society 20 (4) (1969) 451–468.

[5] L. Bertolini, Trading Foreign Exchange Carry Portfolios, PhD Thesis, Cass Business School, City University London, 2010.

[6] C. Brooks, Introductory Econometrics for Finance, second revised ed, Cambridge University Press, Cambridge, 2008.

[7] S.T. Buckland, K.P. Burnham, N.H. Augustin, Model selection: an integral part of inference, Biometrics 53 (2) (1997) 603–618.

[8] Y.L. Chan, J.H. Stock, M.W. Watson, A dynamic factor model framework for forecast combination, Spanish Economic Review 1 (2) (1999) 91–121.

[9] N.E. Coulson, R.P. Robins, Forecast combination in a dynamic setting, Journal of Forecasting 12 (1) (1993) 63–67.

[10] M. Deutsch, C.W.J. Granger, T. Teräsvirta, The combination of forecasts using changing weights, International Journal of Forecasting 10 (1) (1994) 47–57.

[11] F.X. Diebold, R.S. Mariano, Comparing predictive accuracy, Journal of Business and Economic Statistics 13 (3) (1995) 253–263.

[12] F.X. Diebold, P. Pauly, Structural change and the combination of forecasts, Journal of Forecasting 6 (1) (1987) 21–40.

[13] C.L. Dunis, Y.X. Chen, Alternative volatility models for risk management and trading: application to the EUR/USD and USD/JPY rates, Derivatives Use, Trading and Regulation, 11, 2005, pp. 126–156.

[14] C.L. Dunis, G. Giorgioni, J. Laws, J. Rudy, Statistical Arbitrage and High-Frequency Data with an Application to Eurostoxx 50 Equities, Working Paper, Liverpool Business School, 2010.

[15] C.L. Dunis, X. Huang, Forecasting and trading currency volatility: an application of recurrent neural regression and model combination, Journal of Forecasting 21 (5) (2002) 317–354

[16] C.L. Dunis, J. Laws, G. Sermpinis, Higher order and recurrent neural architectures for trading the EUR/USD exchange rate, Quantitative Finance 11 (4) (2011) 615–629.

[17] C.L. Dunis, J. Miao, Optimal trading frequency for active asset management: evidence from technical trading rules, Journal of Asset Management 5 (5) (2005) 305–326

[18] C.L. Dunis, J. Miao, Volatility <sup>fi</sup>lters for asset management: an application to managed futures, Journal of Asset Management 7 (3) (2006) 179–189.

[19] C.L. Dunis, G. Shannon, Emerging markets of South-East and Central Asia: do they still offer a diversi<sup>fi</sup>cation bene<sup>fi</sup>t? Journal of Asset Management 6 (3) (2005) 168–190.

[20] C.L. Dunis, M. Williams, Modelling and trading the EUR/USD exchange rate: do neural network models perform better? Derivatives Use, Trading and Regulation 8 (2002) 211–239.

[21] J.L. Elman, Finding structure in time, Cognitive Science 14 (2) (1990) 179–211.

[22] R. Ghazali, A.J. Hussain, M. Merabti, Higher order neural networks for <sup>fi</sup>nancial time series prediction, The 10th IASTED International Conference on Arti<sup>fi</sup>cial Intelligence and Soft Computing, Palma de Mallorca, Spain, (2006), 2006, pp. 119–124.

[23] J. Ghosh, Y. Shin, The Pi-sigma network: an ef<sup>fi</sup>cient higher-order neural networks for pattern classi<sup>fi</sup>cation and function approximation, Proceedings of International Joint Conference of Neural Networks 1 (1991) 13–18.

[24] J. Ghosh, Y. Shin, Ef<sup>fi</sup>cient higher-order neural networks for classi<sup>fi</sup>cation and function approximation, International Journal of Neural Systems 3 (4) (1992) 323–350.

[25] S.L. Goh, D.P. Mandic, An augmented extended Kalman Filter algorithm for complex-valued recurrent neural networks, Neural Computation 19 (4) (2007) 1039–1055.

[26] C.W.J. Granger, R. Ramanathan, Improved methods of combining forecasts, Journal of Forecasting 3 (2) (1984) 197–204.

[27] J.D. Hamilton, Time Series Analysis, Princeton University Press, Princeton, N.J., 1994

[28] A.C. Harvey, Forecasting, Structural Time Series Models and the Kalman Filter, Cambridge University Press Cambridge UK. 1990

[29] T. Hastie, R. Tibshirani, J.H. Friedman, The Elements of Statistical Learning: Data Mining, Inference, and Prediction, second ed. Springer, New York, 2009.

[30] A.I. Hussain, R. Ghazali, D. Al-Jumeily, M. Merabti, Dynamic ridge polynomial neural network for financial time series prediction JEEE International conference on Innovation in Information Technology, Dubai 2006 (2006) 1–5.

[31] H. Ince, T.B. Trafalis, A hybrid model for exchange rate prediction, Decision Support Systems 42 (2) (2006) 1054–1062.

[32] C.M. Jarque, A.K. Bera, Ef<sup>fi</sup>cient tests for normality, homoscedasticity and serial independence of regression residuals, Economics Letters 6 (3) (1980) 255–259.

[33] I. Kaastra, M. Boyd, Designing a neural network for forecasting <sup>fi</sup>nancial and economic time series, Neurocomputing 10 (3) (1996) 215–236.

[34] B. Krose, P.V.D. Smagt, An Introduction to Neural Networks, eighth ed, University of Amsterdam, 1996

[35] M. Lam, Neural network techniques for <sup>fi</sup>nancial performance prediction: integrating fundamental and technical analysis, Decision Support Systems 37 (4) (2004) 567–581.

[36] W. Leigh, R. Purvis, J.M. Ragusa, Forecasting the NYSE composite index with technical analysis, pattern recognizer, neural network, and genetic algorithm: a case study in romantic decision support, Decision Support Systems 32 (4) (2002) 361–377.

[37] J. Lesage, M. Magura, A Mixture-Model Approach to Combining Forecasts, Journal of Business & Economic Statistics 10 (4) (1992) 445–452.

[38] S. Makridakis, A. Andersen, R. Carbone, R. Fildes, M. Hibon, R. Lewandowski, J. Newton, E. Parzen, R. Winkler, The accuracy of extrapolation (time series) methods: results of a forecasting competition, Journal of Forecasting 1 (2) (1982) 111–153.

[39] P. Newbold, C.W.J. Granger, Experience with forecasting univariate time series and the combination of forecasts, Journal of the Royal Statistical Society 137 (2) (1974) 131–165.

[40] F.C. Palm, A. Zellner, To combine or not to combine? Issues of combining forecasts, Journal of Forecasting 11 (8) (1992) 687–701.

[41] R.S. Pindyck, D.L. Rubinfeld, Econometric Models and Economic Forecasts, forth ed. Irwin/McGraw-Hill Boston. 1998

[42] D.E. Rapach, J.K. Strauss, Forecasting US employment growth using forecast combining methods, Journal of Forecasting 27 (1) (2008) 75–93.

[43] G. Schwarz, Estimating the dimension of a model, The Annals of Statistics 6 (2) (1978) 461–464.

[44] D.N. Sessions, S. Chatterjee, The combining of forecasts using recursive techniques with non-stationary weights, Journal of Forecasting 8 (3) (1989) 239–251.

[45] A.F. Shapiro, A Hitchhiker's guide to the techniques of adaptive nonlinear models Insurance: Mathematics and Economics 26 (2–3) (2000) 119–132.

[46] J.H. Stock, M.W. Watson, Combination forecasts of output growth in a seven-country data set, Journal of Forecasting 23 (6) (2004) 405–430.

[47] R. Sundberg, Shrinkage regression, in: A.H. El-Shaarawi, W.W. Piegorsch (Eds.), Encyclopedia of Environmetrics, John Wiley & Sons, Ltd., Chichester, 2002, pp. 1994–1998.

[48] N.R. Swanson, T. Zeng, Choosing among competing econometric forecasts: regression-based forecast combination using model selection, Journal of Forecasting 20 (6) (2001) 425–440.

[49] P. Tenti, Forecasting foreign exchange rates using recurrent neural networks Applied Artificial Intelligence 10 (6) (1996) 567–581

[50] N. Terui, H.K. Van Dijk, Combined forecasts from linear and nonlinear time series models, International Journal of Forecasting 18 (3) (2002) 421–438.

[51] H. Theil, Applied Economic Forecasting, North-Holland Pub. Co., Amsterdam and Rand McNally, Chicago, 1966

[52] R. Tibshirani, Regression shrinkage and selection via the lasso: a retrospective, Journal of the Royal Statistical Society: Series B (Statistical Methodology) 73 (3) (2011) 273–282.

[53] R. Tsaih, Y. Hsu, C.C. Lai, Forecasting S&P 500 stock index futures with a hybrid AI system, Decision Support Systems 23 (2) (1998) 161–174.

[54] L. Vecci, F. Piazza, A. Uncini, Learning and approximation capabilities of adaptive spline activation function neural networks, Neural Networks 11 (2) (1998) 259–270.

[55] H. Wang, G. Li, G. Jiang, Robust regression shrinkage and consistent variable selection through the LAD–Lasso, Journal of Business and Economic Statistics 25 (3) (2007) 347–355.

[56] G. Welch, G. Bishop, An introduction to the Kalman Filter, Design 7 (1) (2001) 1–16.

[57] Y. Yang, Combining forecasting procedures: some theoretical results, Econometric Theory 20 (1) (2004) 176–222.

[58] M. Yuan, Y. Lin, On the non-negative garrotte estimator, Journal of the Royal Statistical Society: Series B (Statistical Methodology) 69 (2) (2007) 143–161.

Dr Georgios Sermpinis is lecturer in Economics at the University of Glasgow. His research interests lie in <sup>fi</sup>nancial forecasting and the utility of decision support systems in <sup>fi</sup>nancial problems.

Professor Christian Dunis is Emeritus Professor of Banking and Finance at Liverpool Business School, JMU. Currently he is Joint General Manager, Horus Partners Wealth Management Group.

Dr Jason Laws is senior lecturer in Finance at the University of Liverpool. His research interests lie in <sup>fi</sup>nancial risk management and <sup>fi</sup>nancial derivatives.

Mr Charalampos Stasinakis is a PhD student at the University of Glasgow.
