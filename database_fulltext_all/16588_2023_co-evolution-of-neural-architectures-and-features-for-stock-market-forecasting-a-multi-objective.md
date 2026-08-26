---
otero_id: 16588
otero_key: "57C6VREY"
title: "Co-evolution of neural architectures and features for stock market forecasting: A multi-objective decision perspective"
authors: "Faizal Hafiz; Jan Broekaert; Davide La Torre; Akshya Swain"
year: "2023"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2023.114015"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Co-evolution of Neural Architectures and Features for Stock Market Forecasting: A Multi-objective Decision Perspective

Faizal Hafiz<sup>a,∗</sup>, Jan Broekaert<sup>a</sup>, Davide La Torre<sup>a</sup>, Akshya Swain<sup>b</sup>

<sup>a</sup>SKEMA Business School, Universit´e Cˆote d’Azur, Sophia Antipolis, France <sup>b</sup>Department of Electrical, Computer & Software Engineering, The University of Auckland, New Zealand

## Abstract

In a multi-objective setting, a portfolio manager’s highly consequential decisions can benefit from assessing alternative forecasting models of stock index movement. The present investigation proposes a new approach to identify a set of non-dominated neural network models for further selection by the decision-maker. A new co-evolution approac is proposed to simultaneously select the features and topology of neural networks (collectively referred to as neural architecture), where the features are viewed from a topological perspective as input neurons. Further, the co-evolution is posed as a multi-criteria problem to evolve sparse and eficacious neural architectures. The well-known dominance and decomposition based multi-objective evolutionary algorithms are augmented with a non-geometric crossover operator to diversify and balance the search for neural architectures across conflicting criteria. Moreover, the co-evolutio is augmented to accommodate the data-based implications of distinct market behaviors prior to and during the ongo ing COVID-19 pandemic. A detailed comparative evaluation is carried out with the conventional sequential approach of feature selection followed by neural topology design, as well as a scalarized co-evolution approach. The results on the NASDAQ index in pre- and peri-COVID time windows convincingly demonstrate that the proposed co-evolution approach can evolve a set of non-dominated neural forecasting models with better generalization capabilities.

Keywords: Feature Selection, Financial Forecasting, Neural Architecture Search, Multi-Criteria Decision Making

## 1. Introduction

In a complex multi-objective setting involving near-stochastic input data and disparate trade market behaviors stemming from the COVID-19 pandemic, a decision-maker (DM) looks to mitigate the efect of uncertain factors in portfolio decisions. Structured information and oversight from forecasting models are essential supporting tools in such circumstances. This study, therefore, aims to obtain a set of Pareto-optimal forecasting models for stock index movement, which balance multiple criteria of model complexity with prediction performance over distinct market behaviors separated by the outbreak of the COVID-19 pandemic.

This investigation, in particular, focuses on the design of neural forecasting models with input features derived from the technical analysis, which essentially aggregate the information contained in the historical time-series of basic trading data (e.g., daily open and close index values). The motivation for this research direction is two-fold: (1) technical analysis is well-suited for short-term forecasting as it depends only on regularly available basic trading information and is arguably the most common among the existing approaches [1–3]. (2) Artificial Neural Networks (ANN) remained a benchmark technique since the early adoption of machine learning models in stock market forecasting [2, 4]. Further, while the flexible topology of ANN can capture possibly non-linear information in stock forecasting data, several issues related to eficient network design, such as optimal selection of topology and input features, still warrant attention, e.g., see [5–8], which demonstrate that such selection is likely to improve forecasting performance.

The forecasting performance of any neural model is critically dependent on its topological design, which encompasses depth (number of hidden layers), size (number of neurons in each hidden layer), and the choice of the activation function. The optimal topology for a given application and dataset requires an adjusted network complexity that bal ances the bias-variance trade-of [9, 10], e.g., an overly sparse network may lead to high bias errors, whereas an over-complex network may over-fit and thus lead to increased generalization errors. Therefore, an empirical topological design based on a trial-and-error or a rule-of-thumb, which is often employed in existing stock market forecasting models (see Section 2.2 for details), is likely to yield a suboptimal performance. The other crucial design factor is feature selection which aims to identify and remove irrelevant and redundant input features ( see [11] for the details on feature relevance), to reduce the input dimensionality, and often to improve the forecasting performance [11–13], as many technical indicators tend to provide overlapping information and may become redundant [3, 14]. While recent stock forecasting literature focuses on feature selection (see Section 2.1), most depend either on feature selection filters [11, 12] or on dimensionality reduction through principle component analysis, which often neglects non-linear interactions among features. To bridge this gap and to simultaneously address the selection of features and topology, this study pursues a new topological perspective where the selection of features is viewed, ab initio, as the selection of input neurons. Such integration can yield better results for both feature and topology selection as follows: the reduction in input dimensionality associated with feature selection encourages the exploration of relatively parsimonious topologies. Similarly, topological selection aids the search for feature subsets by providing direct access to classification performance; such direct estimates of feature subset eficacy are often more accurate than indirect statistical estimates; see feature selection filters and wrappers in [11–13]. It is worth emphasizing that, despite these advantages, most forecasting models focus on a conventional disjoint or sequential neural design, where feature selection is followed by an empirical selection of neural topology [14–18], which is likely to yield sub-optimal models.

We approach neural architecture as a combination of a feature subset and a neural topology based on the aforementioned topological perspective. This allows us to formulate the multi-objective co-evolution problem, which aims to identify the Pareto optimal set of eficacious and parsimonious neural architectures. Further, it is easy to follow that the search space for the multi-objective co-evolution problem contains all the possible combinations of feature subsets as well as neural topologies (discussed later in Section 4). This search space is known to be multi-modal, deceptive, and noisy [9, 12]. To this end, a combination of Multi-objective Evolutionary Algorithms (MOEAs) and an a posteriori decision making tool is proposed as the overall search framework. In particular, MOEA identifies a set of non-dominated neural architectures first, which represent a diferent degree of trade-of over parsimony and forecasting performance. Next, a combination of multiplicative preference relations [19] and a multi-criteria tournament [20] is proposed as the a posteriori decision support tool to select a particular neural architecture as per the preferences of the Decision Maker (DM).

To summarize, with the motivations for improved neural forecasting models for stock market movement, the core contributions of this investigation are as follows:

• Simultaneous optimization of features and neural topology is proposed under the co-evolution framework. The architectural complexity/parsimony is pursued under a multi-objective setting to evolve parsimonious neural archi tectures with better generalization capabilities.

• Forecasting of the NASDAQ index is being considered during the COVID-19 pandemic. It is shown that the optimal architectural design for disparate market behaviors prior to and within the pandemic can be inconsistent to some degree and is addressed by balancing forecasting performances over pre- and within-COVID periods.

• A search framework consisting of MOEA and a posteriori decision support tool is proposed to identify neural architectures under the proposed co-evolution environment. The impact of search algorithms is investigated by consid ering two well-known MOEAs based on distinct search philosophies: dominance based NSGA-II [21] and hybrid decomposition-dominance based EAGD [22]. Further, NSGA-II is augmented by introducing a non-geometric crossover operator [23] to encourage diversity of the identified neural architectures.

The eficacy of the proposed co-evolution is demonstrated by considering a total of 21 diferent neural architecture design approaches, which are broadly categorized into three comparative neural design baselines (see Section 6). The results of the comparative evaluation demonstrate a statistically significant improvement in the forecasting performance with the proposed co-evolution approach.

To develop our forecasting model and arguments, the rest of this article is organized as follows: In Section 2, the related developments in the literature are screened. Section 3 outlines the forecasting model, classification performance metrics, and COVID-19 related data segmentation. This is followed by the formulation of the proposed co-evolution problem in Section 4. The search framework consisting of Multi-objective Evolutionary Algorithms (MOEAs) and the a posteriori decision support tool is discussed next in Section 5. Section 6 details three distinct neural design baselines, which are considered for comparative evaluation purposes. The results of this investigation are discussed in Section 7. Finally, Section 8 provides a brief discussion and conclusions about the proposed co-evolution approach and the corresponding search framework.

## 2. Background and Related Works

## 2.1. Feature Selection

Feature selection is one of the fundamental problems of machine learning, and it involves a sparse selection of relevant features from the given set of input features [11–13]. Most feature selection approaches can be categorized into either filters or wrappers. This distinction arises mainly from the estimation used to evaluate the classification performance; filters typically rely on indirect statistical or information theory based estimates, whereas wrappers depend directly on the performance of an underlying classifier. While wrappers are computationally expensive, they tend to be more accurate. We refer to [11, 12] for a detailed discussion on feature relevance, redundancy as well as filters and wrappers.

Most of the existing stock forecasting models rely on filters to indirectly estimate feature relevance and/or redundancy, which include but are not limited to correlation criteria [15, 24–28], mutual information [29] and information gain [30]. In comparison, feature selection wrappers have received relatively less attention [14, 31–34]. Peng et al. [14] considered two wrappers, sequential forward floating search and tournament selection, with logistic regression as the underlying classifier for a day ahead movement prediction of seven stock indices. Lee [31] proposed a hybrid filter-wrapper feature selection for a day-ahead movement prediction of the NASDAQ index. In particular, an F-score based filter is used first to prune the feature set, which is followed by a greedy sequential forward search (wrapper) with SVM as the underlying classifier. In [32], a combination of recursive feature elimination wrapper and SVM is used to reduce a full feature set derived from technical analysis as well as other exogenous sources. In [33, 34], a genetic algorithm based wrapper with ANN as the underlying classifier was proposed. Another popular approach among the existing forecasting models is feature extraction using Principal Component Analysis (PCA) [17, 18, 35, 36], where the dimensionality reduction is achieved by retaining a few linear combinations of features (principals) that account for maximal data variance. The transformation of data from a higher to a lower dimensional space is, however, associated with a loss of interpretability and may not be desirable. Further, diferent ensembles of feature selection techniques have also been explored [18, 37, 38]. The objective of such ensembles is to complement individual feature selection techniques. For instance, Tsai and Hsiao [18] derived diferent ensembles through the union and intersection of reduced subsets identified using genetic algorithm (wrapper), information entropy (decision trees) and PCA.

To summarize, while feature selection is receiving increasingly more attention in stock market forecasting, the focus is primarily either on filters or PCA, which tend to neglect nonlinear feature interactions. Further, feature selection is mostly approached as a uni-objective problem focusing primarily on classification performance. However, it is essentially a multi-objective problem as its two key objectives, subset sparsity and improved classification performance, are at least partially conflicting. Consequently, an optimal feature subset which minimizes both objectives simultaneously may not exist; instead, there may exist a set of non-dominated feature subsets which represent a diferent degree of trade-of among these objectives.

## 2.2. Neural Architecture Search

Before we review the existing neural architecture designs, it is pertinent to discuss the implications of neural network depth briefly. While shallow and deep neural architectures have been pursued to forecast stock index movement [1, 2, 4, 39, 40], the selection of the optimal architectural complexity depends on the information in the data [9, 41]. When a network architecture is excessively deep with respect to the statistical information in the data, the initial few network layers will optimally capture the relation while the remaining layers simulate the identity function [41]. Following this perspective and accommodating the fact that the dynamic information contained within technical indicators is often considered weak owing to the adaptive market hypothesis [1, 2, 4, 42], this study pursues shallow neural architectures with a few hidden layers for stock index forecasting. We refer to [1, 2, 39, 40] for a detailed treatment of deep neural network-based forecasting.

The neural architecture can be approached as a set of design choices for the hidden layers, $e . g .$ ., the number of neurons (size) and layers (depth). The selection of an appropriate topology has been the focus of active research since the early stages of neural network development [9, 43]. Over the years, several rules-of-thumb have been proposed which determine the size of hidden layers as a function of the number of inputs/features, outputs and training samples [43, 44], see Section 6.1. Network pruning is another common approach wherein the topological complexity is gradually reduced by identifying and pruning redundant neurons, e.g. see [9]. The selection of the optimal topolog is, however, often application-dependent, and an empirical design following a rule-of-thumb or trial-and-error is likely to yield suboptimal results [9, 43, 44].

It is interesting to note that most stock market forecasting models based on neural networks rely on empirical approaches for topological design [7, 14, 15, 17, 18, 30, 33–35, 37, 45, 46]. Typically, the size of the hidden layer is adjusted by limited trial-and-error and cross-validation [7, 14, 15, 17, 18, 30, 35, 37, 45, 46]. The other empirical approach uses rules of thumb to determine the number and size of hidden layers [25, 27, 31, 47]. A few existing approaches focus on meta-heuristics, such as genetic algorithm, to determine optimal network weights [16, 48, 49]; however, the topology is still selected empirically. In [50], a rule of thumb determines the initial topological design for a wavelet neural network, which is subsequently pruned using a rough set-based approach. In comparison, the optimization of neural topology has received relatively less attention, e.g., see [8, 51–53]. Versace et al. [8] focused on optimizing the number of components in PCA along with the size of the hidden layer using genetic algorithm (GA). In [51, 52], GA was used to select features as well as the size of hidden the layer for a single hidden layer neural network. Similarly, Kim and Shin [53] focused on optimizing input delays and the hidden layer size of time-delayed neural networks.

The selection of neural topology is still under-explored in the stock forecasting models; while a few investigations in [8, 51–53] focus on selecting a part of neural architecture, such as features and hidden layer size, the other aspects, such as the number of hidden layers and selection of activation function, have not been considered. Further the complexity of neural architectures is neither explicitly defined nor pursued in any of these investigations. Our earlier investigation in [44] demonstrated that such explicit formulation of neural complexity is key to balancing th parsimony and eficacy of the neural architectures.

## 3. Forecasting Procedure

## 3.1. Neural Forecasting using Technical Indicators

This study uses technical indicators to forecast a day-ahead stock index movement. Technical indicators are designed as functions of fundamental daily trading quantities (i.e., trading volume, open, close, intra-day high and low) to identify trends or turning points in historical index data, which would subsequently support trading decisions [1, 14, 25, 28, 44]. In particular, the neural forecasting model aims to capture relations between technical indicators and the movement of the index. In particular, a total of 24 distinct technical indicators shown in Table 1 are considered in this study to capture various trends and turning points in the historical index data. These indicators have been selected on the basis of earlier investigations in [1, 2, 14, 25, 28, 44]. The selected indicators include both trend indicators and oscillators. The trend indicators like Moving Average and Momentum (see Table 1) have been developed to identif the direction of movement. In contrast, the oscillators have been developed to recognize turning points by identifying over-bought and over-sold, e.g., Relative Strength Index and William’s oscillator in Table 1. We refer to [1] for a detailed discussion on technical indicators. It is worth noting that each indicator essentially summarizes the index behavior over a period of the past few days, which is denoted by in Table 1. While the maximum value of is <sup>τ τ</sup>typically limited to 30 days, the exact value of is often set empirically [1, 14, 25, 28]. Given that the selection of <sup>τ</sup>is likely to afect forecasting performance (see [54]), and there is no consensus on its optimum value, most of the <sup>τ</sup>indicators in this study are determined over diferent values of $\tau ,$ as shown in Table 1. Hence, multiple features are obtained from most technical indicators.

The features extracted from technical indicators are subsequently used as the inputs to a feed-forward neural network (see Section 4). The neural network is trained via supervised learning to predict a day-ahead index movement, y(t + 1), which is encoded as a binary classifier:

$$
y (t + 1) = \left\{ \begin{array}{l l} 1, & \text { if } \quad C (t + 1) - C (t) > 0, \\ 0, & \text { otherwise } \end{array} \right.\tag{1}
$$

Table 1: Technical Indicators<sup>††</sup>

<table><tr><td>Financial Indicator</td><td>Parameters</td><td>Expression</td></tr><tr><td>Opening, Highest Intra-day, Lowest Intra-day, &amp; Closing Price</td><td>-</td><td> $[O(t), H(t), L(t), C(t)]$ </td></tr><tr><td>Moving Average</td><td> $\tau = [5, 10, 15, 20]$ </td><td> $MA_{\tau}(t) = \sum_{j=t-\tau+1}^{t} \frac{C(j)}{\tau}$ </td></tr><tr><td>Exponential Moving Average</td><td> $\tau = [5, 10, 15, 20], \alpha = \frac{2}{\tau+1}$ </td><td> $EMA_{\tau}(t) = \alpha C(t) + (1 - \alpha)EMA_{\tau}(t-1), EMA_{\tau}(1) = C(1)$ </td></tr><tr><td>Relative Strength Index</td><td> $\tau = [5, 10, 15, 20]$ </td><td> $RSI_{\tau}(t) = 100 \times \frac{UPC_{\tau}(t)/UD_{\tau}(t)}{UPC_{\tau}(t)/UD_{\tau}(t) + DPC_{\tau}(t)/DD_{\tau}(t)}$ </td></tr><tr><td>Stochastic Index, K</td><td> $\tau = [5, 9]$ </td><td> $K_{\tau}(t) = \frac{2}{3}K_{\tau}(t-1) + \frac{1}{3}\frac{C(t) - HH_{\tau}(t)}{HH_{\tau}(t) - LL_{\tau}(t)}$ </td></tr><tr><td>Stochastic Index, D</td><td> $\tau = [5, 9]$ </td><td> $D_{\tau}(t) = \frac{2}{3}D_{\tau}(t-1) + \frac{1}{3}K_{\tau}(t)$ </td></tr><tr><td>Moving Average Convergence-Divergence</td><td> $\tau = 9, \alpha = \frac{2}{\tau+1}$ </td><td> $MACD_{\tau}(t) = (1 - \alpha)MACD_{\tau}(t-1) + \alpha(EMA_{12}(t) - EMA_{26}(t))$ </td></tr><tr><td>Larry Williams&#x27; Oscillator</td><td> $\tau = [5, 10, 15, 20]$ </td><td> $WR_{\tau}(t) = 100 \times \frac{HH_{\tau}(t) - C(t)}{HH_{\tau}(t) - LL_{\tau}(t)}$ </td></tr><tr><td>Psychological Line</td><td> $\tau = [5, 10, 15, 20]$ </td><td> $PSY_{\tau}(t) = 100 \times \frac{UD_{\tau}(t)}{\tau}$ </td></tr><tr><td>Price Oscillator</td><td> $x = [5, 10, 15], y = [10, 15, 20]$ </td><td> $OSCP_{x,y}(t) = \frac{MA_x(t) - MA_y(t)}{MA_x(t)}$ </td></tr><tr><td> $^{\dagger}$ Directional Indicator Up</td><td> $\tau = [5, 10, 15, 20]$ </td><td> $+DIS_{\tau}(t) = (+DM_{\tau}(t)/TRS_{\tau}(t)) \times 100$ </td></tr><tr><td> $^{\dagger}$ Directional Indicator Down</td><td> $\tau = [5, 10, 15, 20]$ </td><td> $-DIS_{\tau}(t) = (-DM_{\tau}(t)/TRS_{\tau}(t)) \times 100$ </td></tr><tr><td>Bias</td><td> $\tau = [5, 10, 15, 20]$ </td><td> $BIAS_{\tau}(t) = 100 \times \frac{C(t) - MA_{\tau}(t)}{MA_{\tau}(t)}$ </td></tr><tr><td>Volume Ratio</td><td> $\tau = 10$ </td><td> $VR_{\tau}(t) = UV_{\tau}(t)/\left(UV_{\tau}(t) + DV_{\tau}(t)\right)$ </td></tr><tr><td>A ratio</td><td> $\tau = 20$ </td><td> $AR_{\tau}(t) = \sum_{j=t-(\tau-1)}^{t} H(j) - O(j) / \sum_{j=t-(\tau-1)}^{t} O(j) - L(j)$ </td></tr><tr><td>B ratio</td><td> $\tau = 20$ </td><td> $BR_{\tau}(t) = \sum_{j=t-(\tau-1)}^{t} /H(j) - C(j) / \sum_{j=t-(\tau-1)}^{t} C(j) - L(j)$ </td></tr><tr><td>Lowest Low</td><td> $\tau = 10$ </td><td> $LL_{\tau}(t) = \min \left\{L(t-\tau), \cdots, L(t-1)\right\}$ </td></tr><tr><td>Highest High</td><td> $\tau = 10$ </td><td> $HH_{\tau}(t) = \max \left\{H(t-\tau), \cdots, H(t-1)\right\}$ </td></tr><tr><td>Median Price</td><td> $\tau = 10$ </td><td> $MP_{\tau}(t) = \text{med}\left\{C(t-\tau), \cdots, C(t-1)\right\}$ </td></tr><tr><td>Average True Range</td><td> $\tau = 10$ </td><td> $ATR_{\tau}(t) = \left(ATR_{\tau}(t) \cdot (\tau-1) + TR(t)\right)/\tau$ </td></tr><tr><td>Relative Difference in Percentage</td><td> $\tau = [5, 10, 15, 20]$ </td><td> $RDP_{\tau}(t) = 100 \times \frac{C(t) - C(t-\tau)}{C(t-\tau)}$ </td></tr><tr><td>Momentum</td><td> $\tau = [5, 10, 15, 20]$ </td><td> $MTM_{\tau}(t) = C(t) - C(t-\tau)$ </td></tr><tr><td>Price Rate of Change</td><td> $\tau = [5, 10, 15, 20]$ </td><td> $ROC_{\tau}(t) = 100 \times \frac{C(t)}{C(t-\tau)}$ </td></tr><tr><td> $^{\ddagger}$ Ultimate Oscillator</td><td> $(x, y, z) = [10, 20, 30]$ </td><td> $UO_{x,y,z}(t) = \frac{100}{4 + 2 + 1} \left(4AVG(x) + 2AVG(y) + AVG(z)\right)$ </td></tr><tr><td>Ulcer Index</td><td> $\tau = 14$ </td><td> $Ulcer_{\tau}(t) = \sqrt{\sum_{k=1}^{T} R_k(t)^2/\tau}, R_k(t) = \frac{100}{HH(t-k)} \left(C(t) - HH(t-k)\right)$ </td></tr></table>

$$
{ } ^ { \ddagger } A V G ( t ) = \frac { \sum _ { j = 1 } ^ { t } C ( j ) - \operatorname* { m i n } \left\{ L ( j ) , C ( j - 1 ) \right\} } { \sum _ { j = 1 } ^ { t } \operatorname* { m a x } \left\{ H ( j ) , C ( j ) \right\} - \operatorname* { m i n } \left\{ L ( j ) , C ( j ) \right\} } ; { } ^ { \dagger } + D M _ { \tau } ( t ) = \sum _ { j = t - \tau + 1 } ^ { t } \frac { H ( j ) - H ( j - 1 ) } { \tau } ; - D M _ { \tau } ( t ) = \sum _ { j = t - \tau + 1 } ^ { t } \frac { L ( j ) - L ( j - 1 ) } { \tau }
$$

$$
{ } ^ { \dagger } T R S _ { \tau } ( t ) = \frac { 1 } { \tau } \sum _ { j = t - \tau + 1 } ^ { t } T R ( j ) , \quad w i t h , \quad T R ( j ) = \operatorname * { m a x } \left\{ H ( j ) - L ( j ) ,   H ( j ) - C ( j - 1 ) ,   L ( j ) - C ( j - 1 ) \right\}
$$

${ } ^ { \dagger \dagger } C ( j ) , H ( j )$ and L( j) respectively give the closing, the highest and the lowest price of day− j; HH (t) ← the highest high price in the previous $( t - \tau )$ days; $L L _ { \tau } ( t ) \gets { \mathrm { t h e } }$ <sup>τ</sup> lowest low price in the previous (t − ) days; UD (t) ← upward days during (t − ) days; DD (t) ← downward <sup>τ</sup>days in during $( t - \tau ) ; U P C _ { \tau } ( t ) \gets$ <sup>τ τ</sup>cumulative closing values on upward days during $( t - \tau ) ; D P C _ { \tau } ( t ) \gets 1$ <sup>τ τ</sup>the cumulative closing values on <sup>τ</sup>downward days during $( t - \tau ) ; T V _ { \tau } ( t )$ ← the volume summation over $( t - \tau ) ; U V _ { \tau } ( t ) \gets$ <sup>τ τ</sup>cumulative volume restricted to upward days; $D V _ { \tau } ( t ) \gets$ <sup>τ τ</sup>cumulative volume on downward days

For the sake of simplicity, let x denote the $i ^ { t h } .$ −feature, which is determined from a particular technical indicator

in Table 1; then the labeled learning data D can be represented as:

$$
\mathcal {D} = \left\{\left(x _ {1}, x _ {2}, \dots , x _ {n _ {f}}, y\right) ^ {(k)} \mid y \in \{0, 1 \} \right\}, \quad k = 1, 2, \dots \mathcal {N}\tag{2}
$$

where, $n _ { f }$ and N respectively denote the total number of features and patterns. A total of 68 features are obtained by evaluating the technical indicator expressions in Table 1, of which some are parameterized over diferent time periods $\tau , i . e . , n _ { f } = 6 8$ . A sliding window of size $w = ( \tau + 1 )$ ) is used on the daily time series of fundamental trading quantities to extract each pattern in D. For any given day−t, the features $( x _ { 1 } , \ldots , x _ { n _ { f } } )$ are evaluated using the trading information over the period of $[ t - \tau , t ]$ days, and the corresponding day-ahead prediction label is generated using the <sup>τ</sup>closing value of the next day (t + 1), see (1). Accordingly, each pattern corresponds to a particular frame of sliding window $( t - \tau + 1 )$ , where $t = 1 , 2 , \ldots , N _ { d a y s }$ and $N _ { d a y s }$ denotes a number of trading days. It is emphasized that the prediction is truly ex-ante as any information from the prediction day, say (t + 1), is not used to extract input features.

## 3.2. Dataset: Pre- and Peri-COVID Stock Index Movements

This study focuses on the historical stock index time-series data over four years starting from January, 2017 to May, 2021. The motivation behind the selection of this timeline lies in the fact that it includes stock market behavior approximately two years prior to and after the breakout of the COVID-19 pandemic. The profound impact of the COVID-19 epidemic on the world economy has exacted measures and eforts by policymakers, managers, and academics, and has sufused the stock markets with high volatility trends, as analyzed in [55–58]. The risk-laden repercussion for financial institutions and investors motivate the development of forecasting models under the changed market behavior. Earlier investigation [44, 59] on this time period indicated that training data reflecting distinct market behavior prior to the COVID-19 pandemic could have a detrimental efect on the forecasting performance in within-COVID 19 time period. This period, hence, can be thought of as a real-life benchmark to design forecasting models in an environment following a market disruption, with possible inconsistencies in market behaviors prior to and after the disruption. In particular, the historical data in this study is segmented into pre- and within-COVID time periods as follows: Pre-COVID data $( \mathcal { D } _ { p r } ) \mathrm { : }$ : from January, 2017 to December, 2018; Within-COVID training data $( \mathcal { D } _ { t r a i n } ) \colon$ from January, 2019 to August, 2020; Within-COVID testing data $( \mathcal { D } _ { t e s t } ) \mathrm { : }$ from August, 2020 to January, 2021; Within-COVID hold-out data $( \mathcal { D } _ { h o l d } )$ : from January, 2021 to May, 2021.

Further, one of the major concerns in financial forecasting is the issue of inadvertent data snooping [4, 60], which can lead to irregularly inflated estimation of generalization capabilities. The issue of data snooping is addressed by sequestering data over four time windows, as discussed earlier. Each dataset is kept strictly separate, and their roles are defined as follows: (1) $\mathcal { D } _ { t r a i n } \mathbf { : }$ : serves as the training dataset and is used for estimation of neural network weights (2) ${ \mathcal { D } } _ { p r }$ and $\mathcal { D } _ { t e s t } \colon$ serve as test datasets to evaluate performance over pre- and within-COVID periods during the optimization of neural architecture. (3) $\mathcal { D } _ { h o l d } \mathrm { : }$ serves as the hold-out dataset. This is a truly out-of-sample dataset as it is not used in any step of model development, including neural architecture optimization and weight estimation. Accordingly, this dataset is used to assess the generalization capabilities of the identified models.

## 3.3. Performance Metrics

Given that the movement forecasting model is essentially a binary classifier, the overall classification accuracy is equivalent to the well-known financial metric ‘Hit-Rate’, which also evaluates the ratio of correct predictions over total predictions [54]. Note that performance assessment using only overall accuracy may be misleading as a long-term drift in the historical trading data may lead to a brute classifier (predicting only majority movement in a dataset) [37, 44]. This study, therefore, considers additional metrics for a balanced assessment of classification performance over both upwards and downwards movements: the Matthews Correlation Coeficient (MCC), the Balanced Accuracy (BA), and Balanced Error = (1 - BA), see [61] for details.

## 4. Multi-objective Co-evolution of Neural Architecture and Features

This study pursues the neural topology as a set of choices for the design of hidden layers $( i . e .$ , size and depth). In addition, the selection of activation function is also being considered. The motivation for this inclusion lies in the earlier investigations of [62] which showed that an independent selection of the activation function for each neuror can lead to relatively sparse topologies. Accordingly, a candidate neural topology $( \mathcal { T } )$ can be represented by a set of tuples,

$$
\mathcal {T} \leftarrow \left\{ \begin{array}{c} (s ^ {1}, f ^ {1}), (s ^ {2}, f ^ {2}), \ldots , (s ^ {n _ {\ell}}, f ^ {n _ {\ell}})   \Big | \\ s ^ {k} \in [ 0, s ^ {m a x} ], \quad f ^ {k} \in \mathcal {F}, \quad \forall k \in [ 1, n _ {\ell} ] \end{array} \right\}\tag{3}
$$

where, the $i ^ { t h } \mathrm { - t u p l e } , ( s ^ { i } , f ^ { i } )$ , represents the design choices for the $i ^ { t h }$ hidden layer; s gives the size or the number of hidden neurons; $f$ denotes a particular activation function which is selected from the set of activation functions, $\mathcal { F }$ , for each hidden layer; $s ^ { m a x }$ and $n _ { \ell }$ respectively give the maximum number of hidden neurons and layers, which are user-defined parameters. Such topologies can be categorized as a semi-heterogeneous, see Hagg et al. [62].

Further, from the topological perspective, the selection of features can be viewed as the selection of input neurons. The removal of irrelevant and redundant features through feature selection can, therefore, be considered a part of the neural design. Before we discuss the co-evolution of features with neural topology, consider the feature selection process in the context of a given set of full features, $X _ { \mathrm { f u l l } } \colon$

$$
X ^ {\star} = \left\{X \subset X _ {\text {full}} \mid J (X) = \min _ {\forall X _ {i} \subset X _ {\text {full}}} J (X _ {i}) \right\}, \quad \text {where,} \quad X _ {\text {full}} = \left\{x _ {1}, x _ {2}, \dots , x _ {n _ {f}} \right\}\tag{4}
$$

where, $x _ { i }$ and $n _ { f }$ denote the $i ^ { t h }$ feature and the total number of features, respectively; $X \subset X _ { \mathrm { f u l l } }$ is a candidate feature subset; and $J ( \cdot )$ is a suitable criterion function which measures the utility of feature subsets, $e . g .$ , classification error. Feature selection is a combinatorial problem due to feature correlations, which becomes NP-Hard even for a moderate number of features [12, 13]. Usually, the selection of features and the design of neural topology are carried out independently, as discussed in Section 2. This study, in contrast, proposes a co-evolution of feature selection with the neural topology, as follows:

$$
\mathcal {A} ^ {\star} = \underset {\mathcal {A} _ {i} \in \Omega} {\arg \min} \left\{ \begin{array}{l} \mathcal {E} (\mathcal {A} _ {i}, \mathcal {D} _ {t e s t}) \\ C (\mathcal {A} _ {i}) \end{array} \right., \text {   where,   } \mathcal {A} _ {i} = \left\{\mathcal {T} _ {i}, X _ {i} \right\}\tag{5}
$$

A denotes an extended neural architecture which is a combination of feature subset X and hidden layer topology $\mathcal { T } ;$ $\mathcal { D } _ { t e s t }$ denotes a test data; and $\varepsilon ( \cdot )$ and $C ( \cdot )$ respectively denote the criteria to measure the classification performance and complexity of a candidate extended architectures (discussed later in Section 5.1.2). Ω denotes the search space of the co-evolution problem, and it is given by,

$$
\Omega = \Omega_ {\mathcal {T}} \times \Omega_ {F}, \quad \text { where, } \quad \Omega_ {\mathcal {T}} = \left([ 0, s ^ {m a x} ] \times \mathcal {F}\right) ^ {n _ {\ell}}, \quad \Omega_ {F} = \left\{X \mid X \subset X _ {\text { full }} \wedge X \neq \emptyset \right\}\tag{6}
$$

$\Omega _ { \mathcal { T } }$ and $\Omega _ { F }$ denote the search space of neural architectures and features, respectively. It is worth noting that the co evolution is formulated as a bi-objective problem to balance the complexity of neural architectures with their eficacy, as seen in (5).

Further, this study, in particular, focuses on the neural design for forecasting stock index movement over the past four years, which includes two distinct market behaviors stemming from the ongoing COVID-19 pandemic, as discussed in Section 3.2. The previous investigations [44, 59] showed that these behavioral changes may be contradictory. The co-evolution problem is, therefore, re-formulated as a multi-objective problem to accommodate distinct market behaviors prior to and during the COVID-19 pandemic, as follows:

$$
\mathcal {A} ^ {\star} = \underset {\mathcal {A} _ {i} \in \Omega} {\arg \min} \left\{ \begin{array}{l} \mathcal {E} _ {c v} (\mathcal {A} _ {i}) \\ \mathcal {C} (\mathcal {A} _ {i}) \\ \mathcal {E} _ {p r} (\mathcal {A} _ {i}) \end{array} \right.\tag{7}
$$

where, $\mathcal { E } _ { p r } ( \mathcal { R } _ { i } )$ and $\mathcal { E } _ { c \nu } ( \mathcal { R } _ { i } )$ respectively denote the values of balanced error obtained with the architecture $\mathcal { A } _ { i }$ over $p r e - C O V I D \left( \mathcal { D } _ { p r } \right)$ and $w i t h i n - C O V I D \left( \mathcal { D } _ { t e s t } \right)$ datasets, see Section 3.2.

![](/api/attachments/57C6VREY/fulltext/images/dc3322905d5229417dd49aa5bf4ba9ae6d6e037b46c9f7e9c66b2b1b2343eca6.jpg)  
Figure 1: Proposed multi-objective co-evolution framework for simultaneous optimization of features and neural topology. APS denotes the set of non-dominated neural architectures identified by the search algorithm.

## 5. Search Framework for Co-evolution Approach

Fig. 1 shows the overall framework of the proposed co-evolution approach to identify neural architectures under the multi-dataset learning scenario involving pre- and within-COVID stock market behaviors. This framework can broadly be categorized into two steps: (1) the search for non-dominated neural architectures and (2) the selection of final architecture as per the preferences of a Decision Maker (DM). These steps are discussed briefly in the following:

An efective search strategy is crucial to identifying promising combinations of feature subset and neural topology in the extended search space (Ω). To this end, this study considers the two well-known Multi-Objective Evolutionar Algorithms (MOEAs). In essence, MOEAs sample the search space (Ω) to generate and evaluate candidate neural architectures (A) throughout the search process, as seen in Fig. 1. A set of non-dominated neural architectures is identified at the end of this search process. The details associated with the search process will be discussed in Section 5.1.

It is worth noting that non-dominated architectures identified by MOEAs are directly incomparable as they represent a varying degree of trade-ofs across the search objectives (i.e., architecture complexity, pre- and within-COVID classification performance). From the perspective of the DM, such non-dominated architectures represent a set of forecasting models with distinct capabilities. Accordingly, preferences of DM about search objectives can be used to compare and, thus, select from the identified architectures. The second step (see Fig. 1) of the proposed framework is designed following these notions, see Section 5.2.

## 5.1. Multi-objective Evolutionary Search Algorithms

Multi-Objective Evolutionary Algorithms (MOEAs) aim to approximate the true Pareto front (PF) of the given problem as accurately as possible. This requires that the Approximated Pareto Front (APF) includes non-dominated solutions which are not only close to the PF (i.e., convergence) but are also well distributed over the entire PF (i.e., diversity). The balance of convergence with the diversity of the APF is crucial for well-informed a posteriori de cision making. The diversity preserving mechanisms in most MOEAs can be categorized into dominance-based or decomposition-based perspectives, see [22] for details. To accommodate both perspectives, two distinct MOEAs are considered: (1) an augmented version of the classical dominance-based algorithm, NSGA-II [21, 23] (2) External Archive Guided MOEA Based on Decomposition (EAGD) [22].

This study selects the classical NSGA-II [21] from dominance-based MOEAs due to its popularity. It is worth noting that while the NSGA-II includes the crowding distance operator to improve the solution diversity, it has been shown that the diversity can further be improved by replacing the conventional recombination operators in NSGA-II (e.g., single-point or uniform crossover) with a non-geometric crossover operator [23, 63], which is adopted here. The design of the non-geometric operator, its parameter settings, and their impacts have been investigated in detail by Ishibuchi et al. in [23] and, therefore, are not discussed here. The other implementation details, such as non-dominated sorting and crowding tournament selection operator, are implemented following the original proposal of Deb et al. [21]. Further, the decomposition-based MOEAs often under-perform on non-continuous Pareto fronts, which are typically associated with combinatorial problems similar to feature selection [22, 63]. EAGD [22] overcomes this issue by a hybrid dominance-decomposition based approach for multi-objective combinatorial problems and, therefore, is considered as the second search algorithm.

As discussed earlier, both NSGA-II and EAGD generate and evaluate candidate neural architectures by sampling the search space Ω. To this end, both algorithms encode candidate neural architectures as an n−dimensional binary string, which will be discussed in Section 5.1.1. The eficacy of each candidate architecture is evaluated across all the search objectives, i.e., architectural complexity, and classification performance over pre- and within-COVID datasets. This evaluation procedure will be discussed in Section 5.1.2.

## 5.1.1. Binary Encoding

Each candidate neural architecture, ${ \mathcal { A } } = \{ X , ~ { \mathcal { T } } \}$ , is encoded by an n−dimensional binary string, where, $n \_ =$ $n _ { f } + \ ( n _ { \ell } \cdot n _ { b i t s } )$ . The first $n _ { f } .$ −bits of such string encode the feature subset $( X )$ , whereas the remaining bits of the string <sup>ℓ</sup>encode the neural topology (T ). A typical binary encoding (denoted as B) is given by,

$$
\mathcal {B} = \left[ \overbrace {\beta_ {1} , \quad \cdots \quad \beta_ {n _ {f}}} ^ {\text { features }} \overbrace {\beta_ {n _ {f} + 1} , \quad \cdots \beta_ {n _ {f} + n _ {b i t s}} , \quad \beta_ {n _ {f} + (n _ {b i t s} + 1)} , \quad \cdots , \beta_ {n}} ^ {\text { topology }} \right], \qquad \text { where }, \quad n = (n _ {b i t s} \cdot n _ {\ell}) + n _ {f}\tag{8}
$$

The feature subset X is encoded by a binary substring of length $n _ { f }$ . Each bit (denoted by $\beta )$ of such a substring encodes whether the corresponding feature is included in $X , e . g . , \beta _ { j } = 1$ <sup>β</sup> indicates that the j<sup>th</sup>−feature is included in $X ,$ $x _ { j } \in X$ . Further, each hidden layer of $\cdot \mathcal { T }$ is encoded by an $n _ { b i t s } \mathrm { - t u p l e }$ . The first $( n _ { b i t s } - 1 )$ bits of such tuple encode the size (number of hidden neurons, s), whereas the last bit encodes the selection of an activation function, $f \in { \mathcal { F } }$ . The set of possible activation functions is given by, $\mathcal { F } = \left\{ s i g m o i d , \right.$ tanh<sup>o</sup>. A total of $( \boldsymbol { n } _ { \ell } \cdot \boldsymbol { n } _ { b i t s } )$ bits is required to encode $\mathcal { T } ,$ , as the maximum number of hidden layers is limited to $n _ { \ell }$

## 5.1.2. Criteria Evaluation

Throughout the search process, each candidate neural architecture is evaluated following the steps outlined in Algorithm 1. The process begins by decoding a binary string $\mathcal { B } _ { i } .$ , which represents an $i ^ { t h } .$ −candidate architecture in both NSGA-II and EAGD, following the steps in Line 7 - 15, Algorithm 1. Its performance is determined next in terms of the main three search objectives, as outlined in Line 16 - 22, Algorithm 1, and discussed in detail in the following:

In this study, the complexity of neural architectures is defined directly as a function of diferent topological components as well as features,

$$
\mathcal {C} (\mathcal {A} _ {i}) = \frac {1}{3} \left\{\frac {\left| X _ {i} \right|}{n _ {f}} + \frac {\left| \left\{(s ^ {k} , f ^ {k}) \mid s ^ {k} \neq 0 , \quad \forall k \in [ 1 , n _ {\ell} ] \right\} \right|}{n _ {\ell}} + \sum_ {k = 1} ^ {n _ {\ell}} \frac {s ^ {k}}{s ^ {m a x}} \right\}\tag{9}
$$

where, $\mathcal { A } _ { i }$ denotes a candidate architecture; | · | determines the cardinality of the given set; $X _ { i }$ denotes the feature subset encoded by $\mathcal { A } _ { i } ; n _ { f }$ gives the total number of features; $n _ { \ell }$ and $s ^ { m a x }$ respectively give the maximum number of hidden layers and neurons, respectively. The function, ${ \mathit { C } } ,$ is bounded in [0, 1] and will attain the maximum value for the mother architecture, $i . e .$ , the architecture which includes all features, the maximum allowable neurons, and layers. C thus measures the complexity of any given architecture relative to the mother architecture. It is easy to follow that a lower value of this function is desirable.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 1: Criteria Evaluation, $J(\cdot)$

Input : Search Agent, $\mathcal{B}_i = \{\beta_{i,1}, \ldots, \beta_{i,n}\}$

Output: Criterion Function, $\vec{J}(\mathcal{A}_i) \leftarrow [\mathcal{E}_{\text{cv}}(\mathcal{A}_i), \mathcal{C}(\mathcal{A}_i), \mathcal{E}_{\text{pr}}(\mathcal{A}_i)]^T$

*/ Decode the feature subset, $X_i$

1 $X_i \leftarrow \emptyset$

2 for $j = 1$ to $n_f$ do

3 if $\beta_{i,j} = 1$ then

4 $X_i \leftarrow \{X_i \cup x_j\} * / \text{add the } j^{th}$ feature

5 end

6 $\mathcal{B}_i \leftarrow \mathcal{B}_i \setminus \{\beta_{i,1}, \beta_{i,2}, \ldots, \beta_{i,n_f}\}$

*/ Decode the neural topology, $\mathcal{T}_i$

7 $\mathcal{T}_i \leftarrow \emptyset$

8 for $j = 1$ to $n_\ell$ do

9 */ Layer Size

$s_j \leftarrow \sum_{p=1}^{(n_{bits}-1)} \beta_{i,p} \times 2^{(n_{bits}-p-1)}$

*/ Activation Function

10 if $\beta_{i,n_{bits}} = 1$ then $f^j \leftarrow \text{sigmoid}$;

11 else $f^j \leftarrow \text{tanh}$;

12 $\mathcal{T}_i \leftarrow \{\mathcal{T}_i \cup (s^j, f^j)\}$

13 $\mathcal{B}_i \leftarrow \mathcal{B}_i \setminus \{\beta_{i,1}, \ldots, \beta_{i,n_{bits}}\}$

14 end

15 $\mathcal{A}_i \leftarrow \{\mathcal{T}_i, X_i\} * / \text{Candidate Architecture}$

*/ Architecture Complexity

16 $C(\mathcal{A}_i) \leftarrow \frac{1}{3} \left\{ \frac{|x_i|}{n_f} + \frac{|[(s^k, f^k) | s^k \neq 0, \forall k \in [1, n_\ell])|}{n_\ell} + \sum_{k=1}^{n_\ell} \frac{s^{k}}{s^{max}} \right\}$

*/ Estimation of Network Performance

17 for $k = 1$ to cycles do

18 */ Weight Estimation, see [64]

19 $W_{i,k}^* \leftarrow \arg\min_{W} L(\mathcal{A}_i, W, D_{train})$

20 Determine balanced errors: $E_k(\mathcal{A}_i, W_{i,k}^*, D_{pr})$ and $E_k(\mathcal{A}_i, W_{i,k}^*, D_{test})$

21 end

22 */ Efficacy over COVID-period

23 $E_{cv}(\mathcal{A}_i) \leftarrow \frac{1}{cycles} \sum_{k=1}^{cycles} E_k(\mathcal{A}_i, W_{i,k}^*, D_{test})$

24 */ Efficacy over Pre-COVID period

25 $E_{pr}(\mathcal{A}_i) \leftarrow \frac{1}{cycles} \sum_{k=1}^{cycles} E_k(\mathcal{A}_i, W_{i,k}^*, D_{pr})$

L(-) denotes loss function for the weight estimation [64]
</div>

Next, we focus on the criteria functions that determine the classification performance. This process begins by estimating the network weights (W) for the candidate architecture using the scaled-conjugate gradient descent algorithm [64]. It is worth emphasizing that the weight estimation is often influenced by various factors including but not limited to local minima and weight initialization, which may translate into an incorrect estimation of the architecture’s eficacy [9]. To minimize such efects, for the given architecture, the weight estimation is repeated over multiple learning cycles, as outlined in Line 17 - 22, Algorithm 1. The subsequent average values of balanced error over preand within-COVID datasets, $\mathcal { E } _ { c \nu } ( \mathcal { R } _ { i } )$ and $\mathcal { E } _ { p r } ( \mathcal { R } _ { i } )$ , serve as two search objectives in addition to the aforementioned architectural complexity, C.

## 5.2. Preference Articulation

The non-dominated architectures identified for the co-evolution problem in (7) by MOEAs are incomparable. Hence, the a posteriori selection of the final architecture depends on the stated preferences of the decision maker (DM), i.e., the relative importance of the three diferent objectives from the perspective of the DM. This procedure is outlined in Algorithm 2 and is discussed in detail in the following: Let Γ denote the Approximate Pareto Set (APS), which represents a set of non-dominated extended architectures identified by a particular MOEA for the co-evolution problem in (7), i.e.,

$$
\Gamma = \left\{\mathcal {A} _ {1}, \quad \mathcal {A} _ {2}, \quad \ldots \right\}, \qquad \Lambda = \left\{\vec {J} (\mathcal {A} _ {1}), \quad \vec {J} (\mathcal {A} _ {2}), \quad \ldots \right\}\tag{10}
$$

where, $\vec { J } ( \mathcal { R } _ { i } ) = \left[ \mathcal { E } _ { c \nu } ( \mathcal { A } _ { i } ) , \quad C ( \mathcal { A } _ { i } ) , \quad \mathcal { E } _ { p r } ( \mathcal { A } _ { i } ) \right] ^ { T }$ , with $i = 1 , 2 , \ldots , | \Gamma | ;$ Λ denotes the Approximate Pareto Front (APF) cor-<sup>.</sup> <sup>.</sup> <sup>.</sup>responding to Γ. Each identified non-dominated architecture $\mathcal { A } _ { i } \in \Gamma$ represents a distinct degree of trade-of across complexity and forecasting performance in pre- and within-COVID periods.

The crucial first step is to quantify often abstract and partial preferences of the DM. This study relies on the multiplicative preference relations [19] for this purpose, which translates preferences into quantifiable weights (denoted by ) for each objective. To this end, the quantification process starts by obtaining the preferences from the DM in terms of an ordered ranking (O) for each objective, in the decreasing order of their importance. In the next step, the intensity of the objective ranking (denoted by I) is selected on a scale from ‘1’ (indiference) to ‘9’ (extreme prejudice). To understand this further, let the objective rankings and the preference intensity specified by the DM be given by:

$$
O = \left[ \begin{array}{c c c} O _ {c v} & O _ {C} & O _ {p r} \end{array} \right] = \left[ \begin{array}{c c c} 1 & 2 & 3 \end{array} \right], \text {and} \mathcal {I} = 9\tag{11}
$$

where, $O _ { c \nu } , O _ { C } .$ , and $O _ { p r }$ respectively denote ranking for within-COVID performance, complexity and pre-COVID performance. This objective ranking indicates that the highest preference is given to within-COVID performance, followed by complexity and pre-COVID performance. For these specifications, the preference relations ( ) between <sup>π</sup>the objectives and, ultimately, the preference weights ( ) are determined by following the steps outlined in Line 1 - 8, Algorithm 2, as follows:

$$
\left[ \begin{array}{c c c} \pi_ {1, 1} & \pi_ {1, 2} & \pi_ {1, 3} \\ \pi_ {2, 1} & \pi_ {2, 2} & \pi_ {2, 3} \\ \pi_ {3, 1} & \pi_ {3, 2} & \pi_ {3, 3} \end{array} \right] = \left[ \begin{array}{c c c} 1 & \sqrt {9} & 9 \\ \frac {1}{\sqrt {9}} & 1 & \sqrt {9} \\ \frac {1}{9} & \frac {1}{\sqrt {9}} & 1 \end{array} \right], \quad \text { which   yields },\tag{12}
$$

$$
\vec {\theta} = \frac {\left[ \begin{array}{l l l} \theta_ {1} & \theta_ {2} & \theta_ {3} \end{array} \right]}{\sum \theta} = \frac {\left[ \begin{array}{l l l} 3 & 1 & 0 . 3 3 \end{array} \right]}{4 . 3 3} = \left[ \begin{array}{l l l} 0. 6 9 & 0. 2 3 & 0. 0 7 \end{array} \right]
$$

In the last step of the a posteriori selection, the preference weights are used to select the final architecture using the Multi-Criteria Tournament Decision (MTD) [20]. The rationale of this approach is to rank each architecture, $\mathcal { A } _ { i } \in \Gamma$ , over a particular objective−p through a tournament comparison with the set of remaining non-dominated architectures, $i . e . , \{ \Gamma \backslash \mathcal { A } _ { i } \}$ . This process is shown in Line 10 - 16, Algorithm 2. In particular, the tournament wins ( ) and tournament function (Φ) over all search objectives are determined first. This is followed by the evaluation <sup>τ</sup>of the global rank (R) which is a function of the tournament wins (Φ) and the preference weight ( ), see Line 17, <sup>θ</sup>Algorithm 2. Finally, the architecture with the maximum global rank is selected as the final architecture, see Line 19, Algorithm 2.

To understand this procedure, consider an Approximate Pareto front (APF, Λ) containing four non-dominated architectures $( \mathcal { A } _ { 1 } , \mathcal { A } _ { 2 } , \ldots , \mathcal { A } _ { 4 } )$ with the objective values given by (13). For each architecture in this APF, tournament wins ( ) and tournament function (Φ) are determined as follows (see Lines 10 - 16, Algorithm 2):

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 2: A posteriori selection

Input : Pareto set, $\Gamma^{*} = \{\mathcal{A}_{1}, \mathcal{A}_{2}, \ldots\}$; Pareto front, $\Lambda^{*} = \{\vec{J}(\mathcal{A}_{1}), \vec{J}(\mathcal{A}_{2}), \ldots\}$

Output: Selected Structure, $\mathcal{A}^{*}$

*/ Preference formulation

1 Specify the preference intensity, $I \in [1,9]$; and the objective rankings, $O = \begin{bmatrix} O_{cv} &amp; O_{C} &amp; O_{pr} \end{bmatrix}$

2 for $i = 1$ to $n_{obj}$ do

3    for $j = 1$ to $n_{obj}$ do

4    $\pi_{i,j} = I^{\left(\frac{O_{j}-O_{i}}{n_{obj}-1}\right)}$ */ pref. relations

5    end

6    $\theta_{i} = \left( \prod_{j=1}^{n_{obj}} \pi_{i,j} \right)^{1/n_{obj}}$

7 end

8 $\vec{\theta} = \begin{bmatrix} \theta_{1} &amp; \theta_{2} &amp; \ldots &amp; \theta_{n_{obj}} \end{bmatrix} / \sum_{p=1}^{n_{obj}} \theta_{p} * / \text{weights}$

*/ Tournament function

9 for $i = 1$ to $|\Lambda^{*}|$ do

10    for $p = 1$ to $n_{obj}$ do

11    $\tau_{i,p} \leftarrow 0$

12    for $j = 1$ to $|\Lambda^{*}|$ do

13    if $J_{p}(\mathcal{A}_{j}) &gt; J_{p}(\mathcal{A}_{i})$ then $\tau_{i,p} \leftarrow \tau_{i,p} + 1$ */ tournament wins;

14    end

15    $\Phi_{p}(\mathcal{A}_{i}) \leftarrow \frac{\tau_{i,p}}{|\Lambda^{*}| - 1}$ */ tournament function

16    end

17    $\mathcal{R}(\mathcal{A}_{i}) \leftarrow \left( \prod_{p=1}^{n_{obj}} \Phi_{p}(\mathcal{A}_{i})^{\theta_{p}} \right)^{\frac{1}{n_{obj}}} * / \text{global rank}$

18 end

19 Select the architecture with the maximum $\mathcal{R}(\cdot)$, i.e., $\mathcal{A}^{*} \leftarrow \{\mathcal{A}_{i} | \mathcal{R}(\mathcal{A}_{i}) = \arg\max\mathcal{R}(\mathcal{A}_{k}), \forall\mathcal{A}_{k} \in \Gamma^{*}\}$ $n_{obj} = 3$ denotes total number of objectives; Criteria Function: $\vec{J}(\mathcal{A}_{i}) = \begin{bmatrix} J_{1}(\mathcal{A}_{i}), J_{2}(\mathcal{A}_{i}), J_{3}(\mathcal{A}_{i}) \end{bmatrix}^{T}$, where, $J_{1}(\mathcal{A}_{i}) \leftarrow \mathcal{E}(\mathcal{A}_{i},\mathcal{D}_{test}), J_{2}(\mathcal{A}_{i}) \leftarrow C(\mathcal{A}_{i})$ and $J_{3}(\mathcal{A}_{i}) \leftarrow \mathcal{E}(\mathcal{A}_{i},\mathcal{D}_{pr})$.
</div>

$$
\Lambda = \left[ \begin{array}{c c c} \mathcal {E} _ {c v} & C & \mathcal {E} _ {p r} \\ 0. 4 3 & 0. 2 7 & 0. 4 6 \\ 0. 4 2 & 0. 3 0 & 0. 4 8 \\ 0. 4 1 & 0. 3 6 & 0. 4 7 \\ 0. 4 5 & 0. 6 5 & 0. 4 5 \end{array} \right] \vec {J} (\mathcal {A} _ {1}) \quad \text {gives}, \quad \tau = \left[ \begin{array}{c c c} \mathcal {E} _ {c v} & C & \mathcal {E} _ {p r} \\ 1 & 3 & 2 \\ 2 & 2 & 0 \\ 3 & 1 & 1 \\ 0 & 0 & 3 \end{array} \right] \mathcal {A} _ {1} \quad \text {and,} \quad \Phi = \frac {\tau}{| \Lambda^ {*} | - 1} = \left[ \begin{array}{c c c} \mathcal {E} _ {c v} & C & \mathcal {E} _ {p r} \\ 0. 3 3 & 1 & 0. 6 7 \\ 0. 6 7 & 0. 6 7 & 0 \\ 1 & 0. 3 3 & 0. 3 3 \\ 0 & 0 & 1 \end{array} \right] \mathcal {A} _ {2}\tag{13}
$$

Next, the global rank for each architecture in Λ is determined by considering the objective rankings, O in (11) and the

consequent preference weights, $\vec { \theta }$ in (12) as follows:

$$
\mathcal {R} = \left[ \begin{array}{c} 0. 7 7 \\ 0 \\ 0. 8 9 \\ 0 \end{array} \right] \begin{array}{c} \mathcal {A} _ {1} \\ \mathcal {A} _ {2} \\ \mathcal {A} _ {3} \\ \mathcal {A} _ {4} \end{array}\tag{14}
$$

Here, $\mathcal { A } _ { 3 }$ is selected as the preferred architecture since it has the maximum value of R.

## 6. Comparative Evaluation: Baseline Neural Design Approaches

This study considers a total of 21 diferent neural architecture design approaches, which are broadly categorized into three baseline approaches for comparative evaluation purposes. These baselines represent prevailing neural design approaches in most of the existing stock index movement investigations (see Section 2), as will be discussed in the following subsections.

## 6.1. Baseline-1: a priori Feature Selection and Rule of Thumbs

The first baseline is designed to reflect most neural forecasting models for stock movement, which are designed in two sequential steps: the input dimensionality of the neural network is reduced first through either pre-processing step such as PCA or feature selection filters, see Section 2.1. Next, the neural topology is selected either following a rule-of-thumb or via trial-and-error (see Section 2.2). In particular, the following three input dimensionality reduction methods are being considered for this baseline: PCA, minimum redundancy-maximum relevancy (mRmR) [65] and correlation-based feature selection (CFS) [66]. Following the investigations in [17, 35], a classical PCA variant is applied to the full feature set containing 68 features. The resultant top 44 principal components explain 99.99% of data variance. Hence, the subsequently transformed datasets with 44 components are used for neural network training and testing. Further, both feature selection filters (mRmR and CFS) essentially focus on identifying a feature subset that reduces feature-to-feature interaction (redundancy) while increasing feature-to-class interaction (relevance). We refer to [65, 66] for implementation details of mRmR and CFS. Both filters use a greedy search approach (best-first search) and identified subsets with 17 (mRmR) and 29 (CFS) features.

In the next step of this baseline, the reduced feature subsets are combined with distinct neural topologies, which are designed with six rules-of-thumb given in Appendix A. We refer to these rules-of-thumb for a systematic design of neural topology to replace empirical trial-and-error topological designs, which is often encountered in the existing studies, e.g., see [7, 14, 15, 17, 18, 30, 33–35, 37, 45, 46].

## 6.2. Baseline-2: a priori Feature Selection and Topology Optimization

The empirical design of neural topology via trial-and-error or rules-of-thumb (similar to baseline-1) may not lead to an optimal topology. Therefore, for sake of fair comparison, the second baseline optimizes neural topology after the dimensionality reduction step. The key distinction here, with respect to the proposed co-evolution problem in (7), is that the reduced feature subset (and therefore the subset of input neurons) remains fixed during the subsequent neural topology search. The optimization of only topology can be formulated as follows:

$$
\mathcal {T} ^ {*} = \underset {\mathcal {T} _ {i} \in \Omega_ {\mathcal {T}}} {\arg \min} \left\{ \begin{array}{l} \mathcal {E} (\mathcal {T} _ {i}, X _ {\mathrm{d}} ^ {*}, \mathcal {D} _ {\text { test }}) \\ \mathcal {C} (\mathcal {T} _ {i}, X _ {\mathrm{d}} ^ {*}) \\ \mathcal {E} (\mathcal {T} _ {i}, X _ {\mathrm{d}} ^ {*}, \mathcal {D} _ {\text { pr }}) \end{array} \right.\tag{15}
$$

where, $\mathrm { X _ { d } ^ { \ast } }$ denotes the subset of d−features which is identified through a priori dimensionality reduction step. The procedure for the baseline topology optimization is similar to the overall process outlined in Section 5, except for one key diference: Given that the features have been selected a priori, the candidate solutions in the baseline neural archi-

tecture search encode only the design of hidden layers (see Section 5.1.1), as follows: $\mathcal { B } = \overbrace { \left[ \beta _ { 1 } , \beta _ { 2 } , \ldots , \beta _ { \left( n _ { b i t s } \cdot n _ { \ell } \right) } \right] } ^ { \mathcal { B } }$

Note that the search space for the neural topology selection reduces to $\Omega _ { \mathcal { T } }$ . The caveat, however, is the loss of the degree of freedom to adjust the design of downstream hidden layers according to the feature subset unde consideration. A possible trade-of in the performance of the evolved neural topologies thus may be expected.

## 6.3. Baseline-3: Scalarized Co-evolution Approach

This study considers the scalarized multi-criteria approach to co-evolve the feature subset and the neural topology proposed in [44] as the third baseline search approach, as follows:

$$
\mathcal {A} ^ {\star} = \underset {\mathcal {A} _ {i} \in \Omega} {\arg \min} \mathcal {J} (\mathcal {A} _ {i}), \qquad w h e r e, \qquad \mathcal {J} (\mathcal {A} _ {i}) = \theta_ {\mathrm{E}} \times \mathrm{E} (\mathcal {A} _ {i}, \mathcal {D} _ {t e s t}) + \theta_ {\mathcal {C}} \times \mathcal {C} (\mathcal {A} _ {i}) + \mathcal {P} (\mathcal {A} _ {i})\tag{16}
$$

where, E(·) and C(·) respectively give the overall classification error and the complexity of the architecture under consideration; $\theta _ { \mathrm { E } }$ and $\theta _ { C }$ denote the preferences of the DM; and P denotes a penalty function which is defined as an −constraint over both $\mathrm { C O V I D } \left( \mathcal { D } _ { t e s t } \right)$ and pre-COVID data $( \mathcal { D } _ { p r } )$ , as follows:

$$
\mathcal {P} (\mathcal {A} _ {i}) = 5 \times \left[ \max \left\{0, \epsilon_ {1} - \Phi (\mathcal {A} _ {i}, \mathcal {D} _ {\text {test}}) \right\} + \max \left\{0, \epsilon_ {2} - \Phi (\mathcal {A} _ {i}, \mathcal {D} _ {\text {pr}}) \right\} + \max \left\{0, \mathrm{E} (\mathcal {A} _ {i}, \mathcal {D} _ {\text {pr}}) - \epsilon_ {3} \right\} \right]\tag{17}
$$

where, Φ(·) denotes Matthews correlation coeficient; $\epsilon _ { 1 } , \epsilon _ { 2 }$ and $\epsilon _ { 3 }$ represent the pre-specified thresholds. A detailed discussion on the rationale behind the penalty function as well as the selection of the thresholds can be found in [44]. It is worth emphasizing that the goal of both the proposed and scalarized approach is to co-evolve the feature subset and the neural topology, i.e., they operate in the common problem search space, Ω. However, the search objectives of these approaches difer, especially in terms of how the pre-COVID data, ${ \mathcal { D } } _ { p r } ,$ is being used. In the proposed approach, the classification performance over ${ \mathcal { D } } _ { p r }$ is one of the main search objectives; see (7) and Section 4. In contrast, in the scalarized approach, the classification performance over ${ \mathcal { D } } _ { p r }$ serves as the secondary search objective. This is apparent from the penalty function in (17), wherein the search is ‘guided’ to keep the error over ${ \mathcal { D } } _ { p r }$ below a pre-fixed threshold ( ), and there is no incentive for further reduction, $i . e .$ , all neural architectures with $\mathrm { E } ( X _ { \mathrm { i } } , \mathcal { D } _ { \mathrm { p r } } ) \leq \epsilon _ { 3 }$ are considered to be equally acceptable when only the performance over $\mathcal { D } _ { p r }$ is considered.

## 7. Results

## 7.1. Experimental Setup

The neural architectures are identified for the NASDAQ data over the four years (see Section 3.2) using both the proposed approach (Section 4 and 5) and the baseline search approaches (Section 6). The search framework outlined in Section 5 is used for the proposed and baseline-2 search environments. A total of 40 independent runs of MOEAs (NSGA-II and EAGD) are carried out, where each run is set to terminate after 15,000 Function Evaluations (FEs). At the end of each run, the identified non-dominated neural architectures and the corresponding approximate Pareto front are recorded. The dominance of such recorded neural architectures is again determined after 40 independent runs, and only non-dominated architectures are considered for further analysis. The search space of neural architectures is determined as follows: A total of 68 features are considered, which are derived from the technical indicators given in Table 1, $i . e . , n _ { f } = 6 8 .$ . The maximum number of hidden layers is set to 2, $i . e . , n _ { \ell } = 2$ . Each layer can have the maximum of 128 neurons, $i . e . , s ^ { m a x } = 1 2 8$ <sup>ℓ</sup>. The mother or the most complex neural architecture (C = 1) for this search space contains all 68-features as inputs and two hidden layers with 128 neurons.

Further, the search parameters of MOEAs are selected empirically and based on earlier investigations in [22, 23, 63]. In particular, the following settings are used for both NSGA-II and EAGD: population size→ 50; mutation $r a t e \to 1 / n .$ , where n is the total number of search variables (see Section 5.1.1). The other algorithm-specific parameters <sup>/</sup>are selected as follows: (1) NSGA-II: crossover rate→ 0.9; probability of non-geometric crossover→ 0.8; probability $o f b i t \ – f i i p \substack { \longrightarrow 1 / n }$ . (2) EAGD: crossover rate→ 1.0; learning generations:→ 8; neighbors:→ 10% of population size.

![](/api/attachments/57C6VREY/fulltext/images/ace5ed31ff407a966da2abdf834f38fcc93304f8f46cc12dd9754ded0008e2d1.jpg)

![](/api/attachments/57C6VREY/fulltext/images/2e508ae6874d37390ac9e6f01a033908b4756160236fbc75bb9bbff61d3735fd.jpg)  
Figure 2: Trade-of in complexity (C) and forecasting performances, COVID balanced error $( \mathcal { E } _ { c \nu } ) ,$ and Pre-COVID balanced error $( \mathcal { E } _ { p r } ) .$ Each circle represents a particular nondominated architecture identified under the coevolution search scenario for the NASDAQ index. The values C are denoted by the radius and the color of circles; a larger radius and bright yellow color of a circle denotes a higher value of architectural complexity, whereas a smaller radius and dark blue color indicates the otherwise.

## 7.2. Co-evolution: Efects of search algorithm

The search for non-dominated neural architectures involves navigating through a typically multi-model, deceptive, and noisy search space associated with the co-evolution problem [9, 12]. Accordingly, an efective search strategy is crucial to converge to the true Pareto front with diverse non-dominated neural architectures. To investigate the efects of diferent search strategies on the identified architectures, we compare the performance of NSGA-II and EAGD. Fig. 2 shows the identified approximate Pareto fronts for the NASDAQ index. It is observed that the algorithms have been equally efective in reducing COVID balance error $( { \mathcal E _ { c \nu } } )$ . Further, the results indicate a clear trade-of in complexity (C) and pre-COVID balanced error $( \mathcal { E } _ { p r } ) _ { \ V }$ ; EAGD tends to select less complex architectures at the expense of higher values of $\mathcal { E } _ { p r } .$ see Fig. 2(b). In contrast, the inclusion of non-geometric crossover [23] in NSGA-II encourages the discovery of a relatively diverse set of architectures, as seen in Fig. 2(a). In particular, NSGA-II identified architectures with lower values of both ${ \mathcal E } _ { c \nu }$ and $\mathcal { E } _ { p r }$ ; albeit with increased complexity as a trade-of. Given that the prediction performance is often preferred over the architectural complexity, we recommend NSGA-II with non-geometric crossover for the co-evolution problem.

## 7.3. Co-evolution: Accommodating diferent decision perspectives through a posteriori selection

Most MOEAs, including NSGA-II and EAGD, are designed to obtain a diverse set of non-dominated solutions Given that such non-dominated solutions are incomparable directly, the perspective of the DM is crucial to select the final solution through the a posteriori selection from the identified Approximate Pareto Set, Γ. To this end, the combination of multiplicative preference relations [19] and the Multi-criteria Tournament Decision (MTD) [20, 63] is used, as discussed in Section 5.2, and shown in Fig. 1. In particular, five distinct objective rankings (O) are being considered to highlight distinct preference perspectives of the DM. Each ranking is defined as an order of preference over COVID-era performance $( O _ { c \nu } )$ , architecture complexity $( O _ { C } )$ and $p r e - C O V I D - e r a$ performance $( O _ { p r } )$ i.e., $\begin{array} { r l } { O = \lceil O _ { c \nu }  } & { { } O _ { C } \quad O _ { p r } \rceil } \end{array}$ . Further, the intensity of preferences is set to strength $^ { \circ } 9 ^ { \prime } \ ( i . e . , \ : J \ : = \ : 9 )$ for all objective rankings. Both, the ranking scenarios (O) and the intensities (I) at which such prioritization is supported, are then used to select an appropriate neural architecture from the approximated Pareto set, e.g. Section 5.2.

Table 2 lists the objective rankings being considered along with the corresponding selected non-dominated architectures from the Pareto set identified by NSGA-II for the NASDAQ index. It provides the details about the selected neural topologies, their complexity (C), as well as classification performances in COVID and Pre-COVID time periods. The classification performance is measured in terms of overall accuracy as well as using MCC (see Section 3.3). Given that the forecasting model is essentially a binary classifier, the overall accuracy is equivalent to the well-known financial prediction metric $\cdot { H i t } { - } R a t e ^ { 3 }$ . In the following, the result corresponding to each decision perspective is discussed individually for ease of interpretation

• Perspective-1: Indiference, $O _ { c \nu } \sim O _ { C } \sim O _ { p r } ;$ In the first decision perspective, the DM is indiferent, i.e., all objectives have equal preference. This is reflected by $O _ { 1 } = \left\lceil 1 \quad 1 \quad 1 \right\rceil \mathrm { i n }$ Table 2. A comparatively sparse neural architecture, $\mathcal { A } _ { 1 }$ , is selected in this scenario; 11 features and a single hidden layer with 18 neurons. A relatively lower pre-COVID classification performance (MCC = 0.06) is obtained with this architecture. This scenario serves as a baseline for the comparison with the other perspectives.

Table 2: Efects of preferences on a posteriori architecture selection for NASDAQ: NSGA-II

<table><tr><td> $^{\dagger}$ Rankings &amp; Selected Architecture</td><td>Selected Features |X|</td><td>Hidden Layer-1 ( $s^{1},f^{1}$ )</td><td>Hidden Layer-2 ( $s^{2},f^{2}$ )</td><td>Complexity, C</td><td> $^{\dagger\dagger}$ COVID Data,  $\mathcal{D}_{test}$ </td><td> $^{\dagger\dagger}$ COVID Data,  $\mathcal{D}_{hold}$ </td><td> $^{\dagger\dagger}$ Pre-COVID Data,  $\mathcal{D}_{pr}$ </td></tr><tr><td rowspan="2"> $O_{1},\mathcal{A}_{1}$ </td><td rowspan="2">11</td><td>18</td><td>-</td><td rowspan="2">0.27</td><td rowspan="2">61.84(0.16)</td><td rowspan="2">55.93(0.13)</td><td rowspan="2">55.47(0.06)</td></tr><tr><td>tansig</td><td>-</td></tr><tr><td rowspan="2"> $O_{2},\mathcal{A}_{2}$ </td><td rowspan="2">11</td><td>32</td><td>-</td><td rowspan="2">0.30</td><td rowspan="2">63.17(0.20)</td><td rowspan="2">56.18(0.14)</td><td rowspan="2">56.34(0.06)</td></tr><tr><td>tansig</td><td>-</td></tr><tr><td rowspan="2"> $O_{3},\mathcal{A}_{3}$ </td><td rowspan="2">10</td><td>35</td><td>32</td><td rowspan="2">0.47</td><td rowspan="2">60(0.13)</td><td rowspan="2">56.26(0.13)</td><td rowspan="2">56.41(0.08)</td></tr><tr><td>tansig</td><td>logsig</td></tr><tr><td rowspan="2"> $O_{4},\mathcal{A}_{4}$ </td><td rowspan="2">14</td><td>123</td><td>64</td><td rowspan="2">0.65</td><td rowspan="2">58.76(0.11)</td><td rowspan="2">56.09(0.13)</td><td rowspan="2">58.33(0.12)</td></tr><tr><td>tansig</td><td>logsig</td></tr><tr><td rowspan="2"> $O_{5},\mathcal{A}_{5}$ </td><td rowspan="2">13</td><td>48</td><td>-</td><td rowspan="2">0.36</td><td rowspan="2">63.32(0.21)</td><td rowspan="2">56.35(0.14)</td><td rowspan="2">56.36(0.07)</td></tr><tr><td>tansig</td><td>-</td></tr></table>

<sup>†</sup> - ranking denotes DM’s preference towards search objectives, i.e., COVID performance, complexity and $P r e \ – C O V I D$ performance and it is denoted by ${ \cal O } = \big [ O _ { c \nu } ~ O _ { C } ~ O _ { p r } \big ] ; O _ { 1 } , O _ { 2 } , \ldots O _ { 5 }$ denote diferent objective rankings and are given as follows: $O _ { 1 } = \big [ 1 \mathrm { ~  ~ \xi ~ } 1 \mathrm { ~  ~ \xi ~ } 1 \big ] , O _ { 2 } = \big [ 1 \mathrm { ~  ~ \xi ~ } 2 \mathrm { ~  ~ \xi ~ } 3 \big ] , O _ { 3 } ^ { ' } = \big [ 1 \mathrm { ~  ~ \xi ~ } 2 \mathrm { ~  ~ \xi ~ } 1 \big ] , O _ { 4 } = \big [ 2 \mathrm { ~  ~ \xi ~ } 3 \mathrm { ~  ~ \xi ~ } 1 \big ] , \mathrm { a n d ~ } O _ { 5 } = \big [ 1 \mathrm { ~  ~ \xi ~ } 3 \mathrm { ~  ~ \xi ~ } 3 \big ]$ $^ { \dagger \dagger }$ - forecasting performance in terms of overall accuracy/hit-rate (in percentage) and Matthews Correlation Coeficien (MCC); a higher value is desirable for both metrics. The values of MCC are shown inside parentheses.

• Perspective-2, $O _ { c \nu } \succ O _ { C } \succ O _ { p r } ;$ The DM emphasizes COVID performance and secondly complexity, which is reflected by $O _ { 2 } \ = \ \left\lceil 1 \quad 2 \quad 3 \right\rceil$ . The efects of these preferences are clearly visible in the selected architecture, $\mathcal { A } _ { 2 } .$ , which is relatively more complex than $\mathcal { A } _ { 1 } , i . e . , C ( A _ { 2 } ) > C ( \mathcal { A } _ { 1 } )$ ), albeit with comparatively better COVID classification performance.

• Perspective-3, $O _ { c \nu } \sim O _ { p r } \succ O _ { C } $ : Here the DM prefers the classification performance in both time-periods over complexity, $i . e . , O _ { 3 } = \left\lceil 1 \quad 2 \quad 1 \right\rceil$ . While the selected architecture $\mathcal { A } _ { 3 }$ is more complex than the baseline $\mathcal { A } _ { 1 }$ , the corresponding classification performance is better than $\mathcal { A } _ { 1 }$ in both pre- and within-COVID periods. Note that $\mathcal { A } _ { 3 }$ is semi-heterogeneous with diferent activation functions in each hidden layer.

• Perspective-4, $O _ { p r } { > } O _ { c \nu } { > } O _ { C }$ : The DM emphasizes most on the performance over the $p r e { \mathrm { - } } C O V I D$ period and the least on complexity, i.e., $O _ { 4 } = { \left[ 2 \begin{array} { l l l } { 3 } & { 1 } \end{array} \right] }$ . As expected, the selected architecture in this scenario, $\mathcal { A } _ { 4 }$ , improves pre-COVID performance at the expense of higher complexity; $\mathcal { A } _ { 4 }$ is the most complex architecture among all scenarios with two dense hidden layers, see Table 2. $\mathcal { A } _ { 4 }$ is also semi-heterogeneous.

• Perspective-5, $O _ { c \nu } \succ O _ { C } \sim O _ { p r } ;$ In the final perspective, the DM prefers a better within-COVID performance, whereas they are indiferent to the complexity and $p r e { \mathrm { - } } C O V I D$ performance, i.e., $O _ { 5 } = { \Big [ } 1 \quad 3 \quad 3 { \Big ] } .$ . The architecture ${ \mathcal { A } } _ { 5 }$ has better classification performances in pre- and within-COVID periods with a trade-of in complexity compared to $\mathcal { A } _ { 1 }$

The comparative evaluation of these scenarios further underlines a trade-of in architecture complexity and $p r e \cdot$ COVID performance in the identified architectures. Nevertheless, all selected architectures $( \mathcal { A } _ { 1 } , \mathcal { A } _ { 2 } , \ldots , \mathcal { A } _ { 5 }$ , Table 2) provide similar performance on out-of-sample COVID dataset $( \mathcal { D } _ { h o l d } )$ , i.e., overall classification accuracy (hit rate) ≈ 56% and MCC≈ 0.14.

## 7.4. Comparative Evaluation with Baseline Approaches

The details of neural forecasting models for the NASDAQ index, which are designed following the first baseline approach, are shown in Table 3. In particular, the input dimensionality of the neural network models is reduced first via either PCA or filter-based feature selection (mRmR or CFS), as discussed in Section 6.1. Next, the neural topologies are determined using various rules-of-thumb in Appendix A. The results show that most neural architectures designed using this baseline have very low values of MCC ( 0.01, highlighted by underlining in Table 3). This behavior can be explained by the tendency of neural networks to be a ‘brute’ classifier, i.e., predict only index rises. Similar behavior has also been identified in the earlier investigations (e.g., see [25]), and is highly undesirable. Note that CFS is not considered for further analysis as it led to ‘brute’ classifiers with all rules-of-thumb; see MCC values with CFS for $\mathcal { D } _ { t e s t }$ in Table 3.

Table 3: Results of baseline neural design: a priori feature selection with rules of thumb for neural topology selection

<table><tr><td rowspan="2">Scenario</td><td rowspan="2"> $^{\ddagger}$ Topology Rule</td><td rowspan="2">Layer Size  $(s^{1})$ </td><td rowspan="2">Layer Size  $(s^{2})$ </td><td rowspan="2">Complexity  $C(\cdot)$ </td><td colspan="3"> $^{\dagger\dagger}$  Classification Performance</td></tr><tr><td>COVID $\mathcal{D}_{test}$ </td><td>COVID $\mathcal{D}_{hold}$ </td><td>Pre-COVID $\mathcal{D}_{pr}$ </td></tr><tr><td rowspan="6">PCA + RoT 44 principals (99.99% of Variance Explained)</td><td>Kolmogorov</td><td>89</td><td>-</td><td>0.3597</td><td>55.90(0.02)</td><td>52.35(0.05)</td><td>53.44(0)</td></tr><tr><td>Hush</td><td>48</td><td>-</td><td>0.3995</td><td>55.61(0)</td><td>51.63(0.03)</td><td>54.16(0)</td></tr><tr><td>Wang</td><td>29</td><td>-</td><td>0.3323</td><td>56.87(0.04)</td><td>51.56(0.03)</td><td>53.85(0)</td></tr><tr><td>Ripley</td><td>23</td><td>-</td><td>0.3297</td><td>56.37(0.01)</td><td>51.74(0.03)</td><td>54.30(0)</td></tr><tr><td>Fletcher-Goss</td><td>15</td><td>-</td><td>0.3271</td><td>57.53(0.05)</td><td>51.12(0.02)</td><td>54.55(0)</td></tr><tr><td>Huang</td><td>57</td><td>19</td><td>0.5101</td><td>57.36(0.01)</td><td>51.93(0.03)</td><td>54.38(0)</td></tr><tr><td rowspan="5">mRmR + RoT 17 features</td><td>Kolmogorov</td><td>35</td><td>-</td><td>0.3419</td><td>57.48(0.01)</td><td>51.10(0.02)</td><td>54.57(0.02)</td></tr><tr><td>Hush</td><td>68</td><td>-</td><td>0.4285</td><td>57.53(0.01)</td><td>50.44(0)</td><td>54.22(0.01)</td></tr><tr><td>Wang</td><td>11</td><td>-</td><td>0.2789</td><td>56.95(0.01)</td><td>51.41(0.02)</td><td>54.95(0.01)</td></tr><tr><td>Ripley &amp; Fletcher-Goss</td><td>10</td><td>-</td><td>0.2762</td><td>56.06(0)</td><td>51.54(0.03)</td><td>54.90(0.02)</td></tr><tr><td>Huang</td><td>57</td><td>19</td><td>0.5164</td><td>55.24(0)</td><td>50.51(0)</td><td>55.35(0.02)</td></tr><tr><td rowspan="6">CFS + RoT 29 features</td><td>Kolmogorov</td><td>59</td><td>-</td><td>0.4637</td><td>56.72(-0.04)</td><td>50.70(0)</td><td>53.27(0.01)</td></tr><tr><td>Hush</td><td>116</td><td>-</td><td>0.6133</td><td>57.18(-0.03)</td><td>51.03(0.02)</td><td>52.29(0)</td></tr><tr><td>Wang</td><td>19</td><td>-</td><td>0.3587</td><td>55.71(-0.02)</td><td>51.01(0.01)</td><td>53.96(0.02)</td></tr><tr><td>Ripley</td><td>16</td><td>-</td><td>0.3508</td><td>56.16(-0.02)</td><td>51.71(0.04)</td><td>53.84(0.02)</td></tr><tr><td>Fletcher-Goss</td><td>13</td><td>-</td><td>0.3429</td><td>55.53(-0.04)</td><td>52.09(0.05)</td><td>53.70(0.02)</td></tr><tr><td>Huang</td><td>57</td><td>19</td><td>0.5752</td><td>55.98(-0.01)</td><td>50.81(0.02)</td><td>53.36(0.01)</td></tr></table>

<sup>‡</sup> See Appendix A for the details about rules of thumb; <sup>†</sup> ‘tanh’ is selected as the activation function for hidden layer/s; <sup>††</sup> forecasting performance in terms of overall classification accuracy/hit-rate (in percentage) and Matthews Correlation Coeficient (MCC). The values of MCC are shown inside parentheses. The underlined MCC values indicate biased prediction behavior towards index rise

Next step of the comparative evaluation focuses on the performance of the second (Section 6.2) and third (Section 6.3) baselines on the NASDAQ index. The second baseline optimizes neural topologies after the dimensionality reduction using either PCA or mRmR. In contrast, the third baseline is essentially a scalarized version of the proposed multi-objective co-evolution. Note that the second baseline, only topology optimization, identified a large number of neural topologies, so we omit the detailed description of neural architectures (similar to Table 3) for sake of brevity. Instead, we compare the performance of the identified neural models following these baselines using the two-dimensional Pareto front plots shown in Fig. 3. Note that the scalarized approach requires the a priori specification of the preference weights, $[ \theta _ { \mathrm { E } } , \theta _ { C } ] ,$ , from the DM. The results obtained using the following three distinct <sup>θ θ</sup>preference scenarios are shown in Fig. 3 to highlight the diferent preferences of the DM: (1) Eficacy over Complexity: [ , ] = [0.75, 0.25], (2) Balanced Scenario: [ , $\theta _ { C } ] = [ 0 . 5 0 , \ 0 . 5 0 ]$ , and (3) Complexity over Eficacy: $[ \theta _ { \mathrm { E } } , \theta _ { C } ] = [ 0 . 2 5 , 0 . 7 5 ]$

![](/api/attachments/57C6VREY/fulltext/images/a2273feff37f7a6b41d167b8c743c8b106c603fb700fe7ba1e16c7b902ae1957.jpg)  
(a)

![](/api/attachments/57C6VREY/fulltext/images/7503e2b6d06474ec75b183832cb1fbb9fbfad50844cd63287b6915095b8966b4.jpg)  
(b)

![](/api/attachments/57C6VREY/fulltext/images/1a49295055b8e453e1c6be65bcb6653f8a8d4cf1d511750d5cd28bbca3d5a7cd.jpg)  
(c)

Figure 3: Comparative evaluation of neural design approaches. Legends: NSGA-II (co-evolution); EAGD (co-evolution); 2DS (scalerized coevolution); PCA+Top (PCA and Topology Optimization); PCA+RoT (PCA and Rule of Thumbs); mRmR+Top (mRmR and Topology Optimization); mRmR+RoT (mRmR and Rule of Thumbs); CFS+RoT (CFS and Rule of Thumbs).  
![](/api/attachments/57C6VREY/fulltext/images/b7fda1c11520b1aaefaf6dc9d5e9e78e0787b86a4c6e0c2b8763316ac394100e.jpg)  
Figure 4: Comparative evaluation of neural design approaches on the out-of-sample data, ${ \mathcal { D } } _ { h o l d } .$ Each circle represents a neural architecture for the NASDAQ index. The MCC values associated with each architecture are reflected by the circle size, i.e., a larger circle denotes a higher value of MCC. Legends: NSGA-II (co-evolution); EAGD (co-evolution); 2DS (scalerized co-evolution); PCA+Top (PCA and Topology Optimization); PCA+RoT (PCA and Rule of Thumbs); mRmR+Top (mRmR and Topology Optimization); mRmR+RoT (mRmR and Rule of Thumbs); CFS+RoT (CFS and Rule of Thumbs).

The results in Fig. 3 indicate that most of the architectures identified by the second baseline (optimization of only topologies) are dominated by the proposed and scalarized approach. It is, therefore, safe to infer that the co-evolution of the feature subset and the neural topology can yield comparatively better results. Further, it is interesting to see that the architectures identified following the scalarized approach are comparable to the proposed approach and lie in the knee-point region of the Pareto front when only the COVID error $( { \mathcal E _ { c \nu } } )$ and the complexity (C) are considered, see Fig. 3(b). However, the scalarized architectures tend to have higher pre-COVID errors $( \mathcal { E } _ { p r } )$ than the proposed approach, as seen in Fig. 3(a) and (c). This is expected and can be explained as follows: the scalarized approach was designed to attain only a pre-specified threshold for $\mathcal { E } _ { p r } ,$ as discussed earlier. In contrast, the proposed approach can better balance performance over both COVID and pre-COVID data owing to the latter’s inclusion in the multi objective formulation.

For sake of convenience, overall classification accuracy (hit rate) and MCC on the out-of-sample dataset $( \mathcal { D } _ { h o l d } )$ of the neural models designed using all comparative baselines and the proposed co-evolution approach are depicted in Fig. 4. It is clear that both co-evolution approaches, scalerized (baseline-3) and proposed multi-objective formulation, outperform baselines-1 and 2. The significant improvement in MCC with the co-evolution approaches is especially noteworthy. The limitations of decoupled neural design approaches (baseline-1 and 2) can primarily be attributed to the input dimensionality reduction approaches (PCA, mRmR, CFS), which are often unsuccessful in accounting for nonlinear feature interactions.

Table 4: Outcomes of Hommel’s post-hoc procedure on out-of-sample datase $( \mathcal { D } _ { h o l d } )$

<table><tr><td rowspan="2">Scenario</td><td rowspan="2">Approach</td><td colspan="3">Accuracy</td><td colspan="3">MCC</td></tr><tr><td>Mean ± SD</td><td>p-value</td><td>‡Adjusted p-value</td><td>Mean ± SD</td><td>p-value</td><td>‡Adjusted p-value</td></tr><tr><td rowspan="2">Naïve</td><td>Random</td><td>49.38 ± 4.6</td><td>1.0E-18</td><td>6.3E-03**</td><td>-0.01 ± 0.09</td><td>5.7E-20</td><td>6.3E-03**</td></tr><tr><td>Brute</td><td>49.45</td><td>3.8E-22</td><td>5.6E-03**</td><td>0</td><td>4.4E-22</td><td>5.6E-03**</td></tr><tr><td rowspan="3">Baseline-1</td><td>PCA + Kolmogorov</td><td>52.35 ± 2.9</td><td>2.5E-10</td><td>1.3E-02**</td><td>0.05 ± 0.07</td><td>4.6E-09</td><td>1.7E-02**</td></tr><tr><td>mRmR + Fletcher-Goss</td><td>51.54 ± 2.9</td><td>2.3E-13</td><td>7.1E-03**</td><td>0.03 ± 0.08</td><td>9.5E-14</td><td>7.1E-03**</td></tr><tr><td>CFS + Fletcher-Goss</td><td>52.09 ± 2.6</td><td>3.1E-10</td><td>1.7E-02**</td><td>0.05 ± 0.07</td><td>4.3E-10</td><td>1.3E-02**</td></tr><tr><td rowspan="2">Baseline-2</td><td>PCA + Top</td><td>52.20 ± 2.4</td><td>1.6E-10</td><td>1.0E-02**</td><td>0.05 ± 0.06</td><td>1.3E-10</td><td>8.3E-03**</td></tr><tr><td>mRmR + Top</td><td>52.18 ± 3.4</td><td>3.5E-11</td><td>8.3E-03**</td><td>0.05 ± 0.09</td><td>4.3E-10</td><td>1.0E-02**</td></tr><tr><td>Baseline-3</td><td>Scalerized (2DS)</td><td>56.62 ± 3.1</td><td>4.6E-01</td><td>2.5E-02**</td><td>0.13 ± 0.08</td><td>3.1E-01</td><td>2.5E-02**</td></tr><tr><td rowspan="2">Co-evolution</td><td>EAGD</td><td>57.93 ± 2.6</td><td>8.9E-01</td><td>5.0E-02</td><td>0.19 ± 0.07</td><td>8.8E-01</td><td>5.0E-02</td></tr><tr><td>NSGA-II</td><td>58.07 ± 3.0</td><td>-</td><td>-</td><td>0.19 ± 0.07</td><td>-</td><td>-</td></tr></table>

<sup>‡</sup> null hypothesis states that a particular approach is better than the Co-evolution (NSGA-II); Hommel’s posthoc procedure suggests that all null-hypotheses (H ) with APV≤ 0.025 should be rejected at = 0.05 level (95% confidence interval); <sup>∗∗</sup> denotes that nullhypothesis is rejected

The statistical significance of the results is determined through non-parametric statistical tests, following the guidelines in [67]. To this end, the neural architecture with the best performance on $\mathcal { D } _ { h o l d }$ is selected first for each baseline as well as the proposed co-evolution approach. Table 4 shows the classification performance of these architectures, both in terms of overall accuracy and MCC. Note that for this part of the analysis, two na¨ıve classifiers are also being considered: na¨ıve random which randomly predicts up or down label for each test instance; and na¨ıve brute which always predicts up movement irrespective of the test instance

The results of Friedmann’s two-way analysis by ranks support the rejection of the null-hypothesis that all the architectures have equal performance with the following p−values: 1.08E-10 (overall accuracy), 1.12E-10 (MCC). Further, the top three neural architectures identified as per Friedman rankings are from the following approaches: Coevolution (NSGA-II), Co-evolution (EAGD), and Scalerized (2DS). Based on these rankings, Co-evolution (NSGA-II) serves as the control approach in the subsequent post-hoc analysis, in which the control approach is compared with the remaining approaches using a set of null hypotheses. Each hypothesis states that the approach being compared identifies significantly better architecture than co-evolution (NSGA-II). The adjusted p−values (APV) for this test are determined using Hommel’s post-hoc analysis [67]. The results of this analysis clearly show that all null-hypotheses, except with co-evolution (EAGD), can safely be rejected at the significance level $\alpha = 0 . 0 5$ , see Table 4.

## 8. Discussion & Conclusions

The development of forecasting models is a critical supporting tool that helps the decision-maker minimize the risk arising from intrinsic and COVID-19 induced uncertainties in stock markets. Neural networks are among the most performant forecasting models for this task, provided their architecture is carefully designed. The design of neural architecture is a multi-criteria problem that requires a careful balance of parsimony (selection of features and topology) with eficacy (forecasting performance over pre- and within-COVID data). This study proposed a new coevolution approach that simultaneously targets feature selection, topological complexity, and multi-dataset learning to address these issues. In addition, a search framework consisting of diversity-focused MOEAs and an a posteriori architecture selection was proposed. It was shown that the introduction of the non-geometric recombination operator allows for the identification of a set of diverse neural architectures in terms of complexity as well as the forecasting performance over multiple datasets. This gives the Decision Maker (DM) a higher degree of selection freedom fo a preferred criterion. Further, a combination of multiplicative preference relations and a tournament decision was used to select architecture a posteriori from the identified Approximate Pareto Set (APS). It was shown that this combination could embed the preferences of the DM into the final neural architecture selection.

The eficacy of the proposed co-evolution was demonstrated by considering a total of 21 diferent neural architecture design approaches, which were broadly categorized into three comparative neural design baselines. These comparative baselines represent neural forecasting models in most existing investigations, as discussed in Section 6. The comparative evaluation demonstrated a statistically significant improvement with the co-evolution.

Further, this investigation provided yet another empirical result supporting market ineficiency. However, more importantly, the results of comparative evaluations could, in part, explain the disparity in conclusions about the forecasting performance of shallow neural networks in the existing research. In particular, the results show that it is possible to obtain insuficient forecasting models which conform to market eficiency or are brute in nature with an improper selection of features and neural topology. The proposed co-evolution approach can overcome such problem by identifying optimal combinations of features and neural topology, which results in balanced forecasting models.

This investigation focused on the forecasting of stock indices, the co-evolution framework proposed here is generic and can be used for any dataset with a moderate number of features. Further, the forecasting performance was evaluated only in terms of classification metrics; the construction trading strategies using the model prediction is left as a future exercise. However, the co-evolution of neural architecture can further be improved by considering other metrics which are closer to profitability, e.g., see mean profit rate in [34].

## Appendix A. Empirical Rules for Neural Design

Kolmogorov’s Theorem: $( s ^ { 1 } , s ^ { 2 } )  \Big ( 2 n _ { f } + 1 , 0 \Big )$ ; Hush’s Rule: $( s ^ { 1 } , \ s ^ { 2 } ) \to \Big ( \lceil c _ { 1 } \times n _ { f } \rceil , \ \lceil c _ { 2 } \times m \rceil \Big )$ , where, $c _ { 1 } \in [ 2 , 4 ]$ $c _ { 2 } \in [ 2 , 3 ]$ ; Wang’s Rule : $( s ^ { 1 } , s ^ { 2 } )  \biggl ( \lceil \frac { 2 \times n _ { f } } { 3 } \rceil , 0 \biggr )$ ; Ripley’s Rule : $( s ^ { 1 } , s ^ { 2 } )  \biggl ( \Biggl | \frac { n _ { f } + m } 2 \Biggl | , 0 \biggr ) ;$ ; Fletcher-Goss’s Rule : $( s ^ { 1 } , \ s ^ { 2 } )  ( \lceil 2 \sqrt { n _ { f } } + m \rceil , \ 0 )$ ; Huang’s Rule : $( s ^ { 1 } , s ^ { 2 } )  ( \lceil \sqrt { ( m + 2 ) N } + ( 2 \sqrt { \frac { N } { m + 2 } } ) \rceil , \lceil m \sqrt { \frac { N } { m + 2 } } \rceil )$

where $n _ { f } , m ,$ , and N respectively denote the number of features, number of output classes/labels, and the total number of training samples.

## References

[1] O. Bustos, A. Pomares-Quimbaya, Stock market movement forecast: A systematic review, Expert Systems with Applications 156 (2020) 113464.

[2] M. M. Kumbure C. Lohrmann. P Luukka I. Porras Machine learning techniques and data for stock market forecasting: A literature review Expert Systems with Applications 197 (2022) 116659.

[3] H. H. Htun, M. Biehl, N. Petkov, Survey of feature selection and extraction techniques for stock market prediction, Financial Innovation 9 (1) (2023) 26.

[4] B. M. Henrique, V. A. Sobreiro, H. Kimura, Literature review: Machine learning techniques applied to financial market prediction, Expert Systems with Applications 124 (2019) 226–251.

[5] G. S. Atsalakis, K. P. Valavanis, Surveying stock market forecasting techniques – Part II: Soft computing methods, Expert Systems with Applications 36 (3, Part 2) (2009) 5932–5941.

[6] A. J. Hussain, A. Knowles, P. J. Lisboa, W. El-Deredy, Financial time series prediction using polynomial pipelined neural networks, Expert Systems with Applications 35 (3) (2008) 1186–1199.

[7] M. Lam, Neural network techniques for financial performance prediction: integrating fundamental and technical analysis, Decision Support Systems 37 (4) (2004) 567–581.

[8] M. Versace, R. Bhatt, O. Hinds, M. Shifer, Predicting the exchange traded fund DIA with a combination of genetic algorithms and neural networks, Expert Systems with Applications 27 (3) (2004) 417–425.

[9] X. Yao, Evolving artificial neural networks, Proceedings of the IEEE 87 (9) (1999) 1423–1447.

[10] J. Wang, C. Xu, X. Yang, J. M. Zurada, A novel pruning algorithm for smoothing feedforward neural networks based on group lasso method, IEEE Transactions on Neural Networks and Learning Systems 29 (5) (2018) 2012–2024.

[11] R. Kohavi, G. H. John, Wrappers for feature subset selection, Artificial intelligence 97 (1) (1997) 273–324.

[12] I. Guyon, A. Elisseef, An introduction to variable and feature selection, Journal of Machine Learning Research 3 (Mar) (2003) 1157–1182

[13] F. Hafiz, A. Swain, N. Patel, C. Naik, A two-dimensional (2D) learning framework for particle swarm based feature selection, Pattern Recognition 76 (2018) 416–433.

[14] Y. Peng, P. H. M. Albuquerque, H. Kimura, C. A. P. B. Saavedra, Feature selection and deep neural networks for stock price direction forecasting using technical analysis indicators, Machine Learning with Applications 5 (2021) 100060.

[15] S. Asadi, E. Hadavandi, F. Mehmanpazir, M. M. Nakhostin, Hybridization of evolutionary levenberg–marquardt neural networks and data pre-processing for stock market prediction, Knowledge-Based Systems 35 (2012) 245–258.

[16] M. Qiu, Y. Song, F. Akagi, Application of artificial neural network for the prediction of stock market returns: The case of the japanese stock market, Chaos, Solitons & Fractals 85 (2016) 1–7.

[17] X. Zhong, D. Enke, Forecasting daily stock market return using dimensionality reduction, Expert Systems with Applications 67 (2017) 126–139.

[18] C.-F. Tsai, Y.-C. Hsiao, Combining multiple feature selection methods for stock prediction: Union, intersection, and multi-intersection approaches, Decision Support Systems 50 (1) (2010) 258–269.

[19] Q. Zhang, J. C. Chen, P. P. Chong, Decision consolidation: criteria weight determination using multiple preference formats, Decision Support Systems 38 (2) (2004) 247–258.

[20] R. Parreiras, J. Vasconcelos, Decision making in multiobjective optimization aided by the multicriteria tournament decision method, Nonlinear Analysis: Theory, Methods & Applications 71 (12) (2009) e191–e198.

[21] K. Deb, A. Pratap, S. Agarwal, T. Meyarivan, A fast and elitist multiobjective genetic algorithm: NSGA-II, IEEE Transactions on Evolutionary Computation 6 (2) (2002) 182–197.

[22] X. Cai, Y. Li, Z. Fan, Q. Zhang, An external archive guided multiobjective evolutionary algorithm based on decomposition for combinatorial optimization, IEEE Transactions on Evolutionary Computation 19 (4) (2015) 508–523.

[23] H. Ishibuchi, N. Tsukamoto, Y. Nojima, Diversity improvement by non-geometric binary crossover in evolutionary multiobjective optimization, IEEE Transactions on Evolutionary Computation 14 (6) (2010) 985–998.

[24] G. Li, A. Zhang, Q. Zhang, D. Wu, C. Zhan, Pearson correlation coeficient-based performance enhancement of broad learning system for stock price prediction, IEEE Transactions on Circuits and Systems II: Express Briefs 69 (5) (2022) 2413–2417.

[25] D. Kumar, S. S. Meghwani, M. Thakur, Proximal support vector machine based hybrid prediction models for trend forecasting in financial markets, Journal of Computational Science 17 (2016) 1–13.

[26] K. Zbikowski, Using volume weighted support vector machines with walk forward testing and feature selection for the purpose of creating<sup>˙</sup> stock trading strategy, Expert Systems with Applications 42 (4) (2015) 1797–1805.

[27] F. A. de Oliveira, C. N. Nobre, L. E. Zarate, Applying artificial neural networks to prediction of stock price and improvement of the directional´ prediction index – case study of petr4, petrobras, brazil, Expert Systems with Applications 40 (18) (2013) 7596–7606.

[28] C.-L. Huang, C.-Y. Tsai, A hybrid sofm-svr with a filter-based feature selection for stock market forecasting, Expert Systems with Applications 36 (2, Part 1) (2009) 1529–1539.

[29] J. Sun, K. Xiao, C. Liu, W. Zhou, H. Xiong, Exploiting intra-day patterns for market shock prediction: A machine learning approach, Expert Systems with Applications 127 (2019) 272–281.

[30] S. Thawornwong, D. Enke, The adaptive selection of financial and economic variables for use with artificial neural networks, Neurocomputing 56 (2004) 205–232.

[31] M.-C. Lee, Using support vector machine with a hybrid feature selection method to the stock trend prediction, Expert Systems with Applica tions 36 (8) (2009) 10896–10904.

[32] B. Weng, M. A. Ahmed, F. M. Megahed, Stock market one-day ahead movement prediction using disparate data sources, Expert Systems with Applications 79 (2017) 153–163.

[33] M. Inthachot, V. Boonjing, S. Intakosum, et al., Artificial neural network and genetic algorithm hybrid intelligence for predicting Thai stock price index trend, Computational intelligence and neuroscience 2016 (2016).

[34] G. Liu, X. Wang, A new metric for individual stock trend prediction, Engineering Applications of Artificial Intelligence 82 (2019) 1–12.

[35] X. Zhong, D. Enke, A comprehensive cluster and classification mining procedure for daily stock market return forecasting, Neurocomputing 267 (2017) 152–168.

[36] L. Di Persio, O. Honchar, Artificial neural networks architectures for stock price prediction: Comparisons and applications, Internationa journal of circuits, systems and signal processing 10 (2016) (2016) 403–413.

[37] A. U. Haq, A. Zeb, Z. Lei, D. Zhang, Forecasting daily stock trend using multi-filter feature selection and deep learning, Expert Systems with Applications 168 (2021) 114444.

[38] Y. Alsubaie, K. El Hindi, H. Alsalman, Cost-sensitive prediction of stock price direction: Selection of technical indicators, IEEE Access 7 (2019) 146876–146892.

[39] O. B. Sezer, M. U. Gudelek, A. M. Ozbayoglu, Financial time series forecasting with deep learning: A systematic literature review: 2005– 2019, Applied soft computing 90 (2020) 106181.

[40] F. Rundo, F. Trenta, A. L. di Stallo, S. Battiato, Machine learning for quantitative finance applications: A survey, Applied Sciences 9 (24) (2019) 5574.

[41] K. He, X. Zhang, S. Ren, J. Sun, Deep residual learning for image recognition, in: Proceedings of the IEEE conference on computer vision and pattern recognition, 2016, pp. 770–778.

[42] E. F. Fama, Random walks in stock market prices, Financial Analysts Journal 21 (5) (1965) 55–59.

[43] D. Stathakis, How many hidden layers and nodes?, International Journal of Remote Sensing 30 (8) (2009) 2133–2147

[44] F. Hafiz, J. Broekaert, D. La Torre, A. Swain, A multi-criteria approach to evolve sparse neural architectures for stock market forecasting, Annals of Operations Research (Accepted), Available online: arXiv eprint:2111.08060 (2021).

[45] K. Kim, Financial time series forecasting using support vector machines, Neurocomputing 55 (1) (2003) 307–319.

[46] L.-J. Cao, F. E. H. Tay, Support vector machine with adaptive parameters in financial time series forecasting, IEEE Transactions on Neural Networks 14 (6) (2003) 1506–1518.

[47] D. Olson, C. Mossman, Neural network forecasts of canadian stock returns using accounting ratios, International Journal of Forecasting 19 (3) (2003) 453–465.

[48] H. Hu, L. Tang, S. Zhang, H. Wang, Predicting the direction of stock markets using optimized neural networks with google trends, Neuro computing 285 (2018) 188–195.

[49] P.-C. Chang, D. di Wang, C. le Zhou, A novel model by evolving partially connected neural network for stock price trend forecasting, Expert

Systems with Applications 39 (1) (2012) 611–620.

[50] L. Lei, Wavelet neural network prediction method of stock price trend based on rough set attribute reduction, Applied Soft Computing 62 (2018) 923–932.

[51] M. Shahvaroughi Farahani, S. H. Razavi Hajiagha, Forecasting stock price using integrated artificial neural network and metaheuristic algo rithms compared to time series models, Soft computing 25 (13) (2021) 8483–8513.

[52] M. Goc¸ken, M.¨ Ozc¸alıcı, A. Boru, A. T. Dosdo<sup>¨</sup> gru, Integrating metaheuristics and artificial neural networks for improved stock price predic-˘ tion, Expert Systems with Applications 44 (2016) 320–331.

[53] H. jung Kim, K. shik Shin, A hybrid approach based on neural networks and genetic algorithms for detecting temporal patterns in stock markets, Applied Soft Computing 7 (2) (2007) 569–576.

[54] Y. Shynkevich, T. McGinnity, S. Coleman, A. Belatreche, Y. Li, Forecasting price movements using technical indicators: Investigating the impact of varying input window length, Neurocomputing 264 (2017) 71–88.

[55] X. Gao, Y. Ren, M. Umar, To what extent does COVID-19 drive stock market volatility? a comparison between the U.S. and china, Economic Research 35 (1) (2022) 1686–1706.

[56] M. M. Rahman, C. Guotai, A. D. Gupta, M. Hossain, M. Z. Abedin, Impact of early COVID-19 pandemic on the US and european stock markets and volatility forecasting, Economic Research 35 (1) (2022) 3591–3608.

[57] W. Li, F. Chien, H. W. Kamran, T. M. Aldeehani, M. Sadiq, V. C. Nguyen, F. Taghizadeh-Hesary, The nexus between COVID-19 fear and stock market volatility, Economic Research 35 (1) (2022) 1765–1785.

[58] M. Buszko, W. Orzeszko, M. Stawarz, COVID-19 pandemic and stability of stock market—a sectoral approach, PLOS ONE 16 (5) (2021) 1–26.

[59] R. Chandra, Y. He, Bayesian neural networks for stock price forecasting before and during COVID-19 pandemic, PLOS ONE 16 (7) (2021) 1–32.

[60] R. Sullivan, A. Timmermann, H. White, Data-snooping, technical trading rule performance, and the bootstrap, The Journal of Finance 54 (5) (1999) 1647–1691.

[61] M. Grandini, E. Bagli, G. Visani, Metrics for multi-class classification: an overview (2020). doi:10.48550/ARXIV.2008.05756.

[62] A. Hagg, M. Mensing, A. Asteroth, Evolving parsimonious networks by mixing activation functions, in: Proceedings of the Genetic and Evolutionary Computation Conference, 2017, pp. 425–432.

[63] F. Hafiz, A. Swain, E. Mendes, Multi-objective evolutionary framework for non-linear system identification: A comprehensive investigation, Neurocomputing 386 (2020) 257 – 280.

[64] M. F. Møller, A scaled conjugate gradient algorithm for fast supervised learning, Neural Networks 6 (4) (1993) 525–533.

[65] H. Peng, F. Long, C. Ding, Feature selection based on mutual information criteria of max-dependency, max-relevance, and min-redundancy, IEEE Transactions on Pattern Analysis and Machine Intelligence 27 (8) (2005) 1226–1238.

[66] M. A. Hall, L. A. Smith, Feature selection for machine learning: comparing a correlation-based filter approach to the wrapper., in: FLAIRS conference, Vol. 1999, 1999, pp. 235–239.

[67] S. Garc´ıa, A. Fernandez, J. Luengo, F. Herrera, Advanced nonparametric tests for multiple comparisons in the design of experiments in´ computational intelligence and data mining: Experimental analysis of power, Information Sciences 180 (10) (2010) 2044–2064.
