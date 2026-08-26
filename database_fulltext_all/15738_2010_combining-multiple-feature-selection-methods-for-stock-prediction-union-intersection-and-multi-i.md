---
otero_id: 15738
otero_key: "JTAEW9CW"
title: "Combining multiple feature selection methods for stock prediction: Union, intersection, and multi-intersection approaches"
authors: "Chih-Fong Tsai; Yu-Chieh Hsiao"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.08.028"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Combining multiple feature selection methods for stock prediction: Union, intersection, and multi-intersection approaches

Chih-Fong Tsai ⁎, Yu-Chieh Hsiao

Department of Information Management, National Central University, Taiwan

## a r t i c l e i n f o

Article history: Received 10 May 2009 Received in revised form 4 August 2010 Accepted 17 August 2010 Available online 21 August 2010

Keywords: Stock prediction Feature selection Data mining Principal Component Analysis Genetic algorithm Decision trees

## a b s t r a c t

To effectively predict stock price for investors is a very important research problem. In literature, data mining techniques have been applied to stock (market) prediction. Feature selection, a pre-processing step of data mining, aims at <sup>fi</sup>ltering out unrepresentative variables from a given dataset for effective prediction. As using different feature selection methods will lead to different features selected and thus affect the prediction performance, the purpose of this paper is to combine multiple feature selection methods to identify more representative variables for better prediction. In particular, three well-known feature selection methods, which are Principal Component Analysis (PCA), Genetic Algorithms (GA) and decision trees (CART), are used. The combination methods to <sup>fi</sup>lter out unrepresentative variables are based on union, intersection, and multi-intersection strategies. For the prediction model, the back-propagation neural network is developed. Experimental results show that the intersection between PCA and GA and the multi-intersection of PCA, GA, and CART perform the best, which are of 79% and 78.98% accuracy respectively. In addition, these two combined feature selection methods <sup>fi</sup>lter out near 80% unrepresentative features from 85 original variables, resulting in 14 and 17 important features respectively. These variables are the important factors for stock prediction and can be used for future investment decisions.

© 2010 Elsevier B.V. All rights reserved

## 1. Introduction

Stock investments are a very popular investment activity around the world. However, the stock market is always dif<sup>fi</sup>cult to accurately predict due to many reasons, such as the political situation (for some speci<sup>fi</sup>c countries), the global economy, etc. Without the good ability of predicting stock price, successful investments are very dif<sup>fi</sup>cult to make.

In literature, some basic important factors, such as <sup>fi</sup>nancial ratios, technical indexes, and macroeconomic indexes have been proved as the important factors of affecting stocks' rise and fall. However, different studies select their factors (i.e. input variables) differently for their prediction models [3]. That is, the opinion of the important factors for stock prediction is somewhat different in related work since there is no exact answer to the question of what are the most representative variables. On the other hand, it is the fact that using different input variables can make the same prediction model performs differently. Therefore, constructing the optimal stock prediction model for investors is very challenging.

In general, some related work considers a feature selection step to examine the usefulness of their chosen variables for effective stock prediction, e.g. [5,15,53]. This is because not all of the pre-chosen features are informative or can provide high discrimination power. This can be called as the curse of dimensionality problem [33]. As a result, feature selection can be used to <sup>fi</sup>lter out redundant and/or irrelevant features from a chosen dataset resulting in more representative features for better prediction performances [50].

Related work which considers feature selection is usually based on one chosen method only (c.f. Table 1). That is, the chosen feature selection method is supposed to select usable features for stock prediction. However, using different feature selection methods is likely to produce different results (i.e. different variables selected). Therefore, if we could apply a number of different feature selection methods and then combine the selection results, we can not only understand the most important and representative variables that all the feature selection methods ‘agree’, but also further improve prediction performances over using one single feature selection methods.

The idea of combining multiple feature selection methods is derived from classi<sup>fi</sup>er ensembles (or multiple classi<sup>fi</sup>ers) [26]. The aim of classi<sup>fi</sup>er ensembles is to obtain highly accurate classi<sup>fi</sup>ers by combining less accurate ones. They are intended to improve the classi<sup>fi</sup>cation performance of a single classi<sup>fi</sup>er. That is, the combination is able to complement the errors made by the individual classi<sup>fi</sup>ers on different parts of the input space. Therefore, the performance of classi<sup>fi</sup>er ensembles is likely better than one of the best single classi<sup>fi</sup>ers used in isolation.

Table 1 Comparisons of related work.

<table><tr><td>Work</td><td>Dataset</td><td>Prediction model</td><td>Input variables</td><td>Feature selection</td></tr><tr><td>Huang and Tsai (2009) [15]</td><td>Taiwan index futures (FITX)</td><td>A hybrid SOM $^{a}$ -SVR $^{b}$ model</td><td>13 Technical indexes</td><td>Filter-based feature selection</td></tr><tr><td>Lai et al., (2009) [28]</td><td>Taiwan Stock Exchange Corporation</td><td>K-means, GA-based fuzzy decision tree</td><td>7 Technical indexes</td><td>Step-wise regression</td></tr><tr><td>Lin et al., (2009) [36]</td><td>S&amp;P 500</td><td>ESN $^{c}$ , BPNN $^{d}$ , RNN $^{e}$ </td><td>Technical indexes</td><td>PCA</td></tr><tr><td>Zarandi et al., (2009) [54]</td><td>An automotive manufactory in Asia</td><td>A type-2 fuzzy logic system</td><td>Fundamental &amp; Technical indexes</td><td>Regularity Criterion (RC)</td></tr><tr><td>Li and Kuo (2008) [34]</td><td>Taiwan Weighted Stock Index</td><td>SOM + BPNN</td><td>Technical indexes</td><td>Discrete wavelet transform (DWT)</td></tr><tr><td>Chang and Liu (2008) [5]</td><td>TSE index and MediaTek</td><td>A TSK type fuzzy rule based system</td><td>8 Technical indexes</td><td>Step-wise regression</td></tr><tr><td>Yu et al., (2005) [53]</td><td>S&amp;P 500 index data</td><td>GA-based SVM $^{f}$ </td><td>18 Technical indexes</td><td>GA</td></tr><tr><td>Enke and Thawornwong (2005) [10]</td><td>S&amp;P 500 stock index</td><td>Linear regression model, BPNN, GRNN $^{g}$ , PNN $^{h}$ </td><td>31 Financial and economic variables</td><td>Information gain</td></tr><tr><td>Ince and Trafalis (2004) [19]</td><td>NASDAQ</td><td>BPNN and SVM</td><td>Technical indexes</td><td>PCA and FA $^{i}$ </td></tr><tr><td>Lam (2004) [29]</td><td>364 S&amp;P companies</td><td>BPNN</td><td>16 Financial &amp; 11 macroeconomic indexes</td><td>-</td></tr><tr><td>Abraham et al., (2001) [1]</td><td>NASDAQ</td><td>BPNN, neuro-fuzzy system</td><td>Fundamental indexes</td><td>PCA</td></tr><tr><td>Hulme and Xu (2001) [17]</td><td>Australian Stock Exchange (ASX)</td><td>GA-based NN</td><td>Fundamental indexes</td><td>-</td></tr><tr><td>Kim and Han (2000) [24]</td><td>Daily Korea stock price index (KOSPI)</td><td>A hybrid model of BPNN and GA</td><td>12 Technical indexes</td><td>GA</td></tr></table>

<sup>a</sup> SOFM Self-organizing feature map.  
<sup>b</sup> SVR Support vector regression.  
<sup>c</sup> ESN: Echo state network.  
<sup>d</sup> BPNN: Back-propagation neural network.  
<sup>e</sup> RNN: Recurrent neural network.  
<sup>f</sup> SVM: Support vector machine.  
<sup>g</sup> GRNN: Generalized regression neural network  
<sup>h</sup> PNN: Probabilistic neural network.  
<sup>i</sup> FA: Factor analysis.

As a result, the major research objective of this paper is to examine whether the prediction model using the selected features (i.e. variables) by the combination of multiple feature selection methods can provide better performances (higher accuracy and lower errors) than using single feature selection methods. In particular, three combination strategies to combine multiple selection results are assessed, which are the union, intersection, and multi-intersection approaches. Moreover, the combination of multiple feature selection methods is able to allow us to identify much better representative variables for stock prediction.

The rest of this paper is organized as follows. Section 2 reviews related literature, including stock price theory and analysis methods and feature selection methods used in this paper which are Principal Component Analysis, genetic algorithm, and decision trees. In addition, related work is compared in terms of their datasets used, prediction models constructed, feature selection methods applied, etc. Section 3 presents the experimental setup, including the chosen dataset, the combination approaches to combine multiple feature selection methods, the process of constructing the prediction model based on arti<sup>fi</sup>cial neural networks, and the evaluation methods. Section 4 shows the experimental results and a conclusion is provided in Section 5.

## 2. Literature review

## 2.1. Stock price theory and analysis methods

## 2.1.1. Stock price theory

Stock prices mean the actual transaction price through the buyers and sellers in the market. Stock prices are determined by the laws of supply and demand [6]. In theory, whether the price of a stock is high or low, it is decided by the buyers and sellers' transactions in the open market. When supply and demand change, the stock price must be changed. That is, if the supply exceeds the demand, the stock price must fall; if the demand exceeds the supply, the stock price must rise. Therefore, we can see that the supply and demand factors directly affect stock prices.

However, there are many other factors affecting stock prices. In past decades, the academic community has developed many related theories about stock prices. The most common one is the Ef<sup>fi</sup>cient Market Hypothesis (EMH) proposed by Fama [11].

Fama's Ef<sup>fi</sup>cient Market Hypothesis supposes that the investment activity is a “Fair-Game Market”. It means all information has disclosed in the stock market, and re<sup>fl</sup>ects on stock prices. According to the difference of disclosed information, there are three kinds of Ef<sup>fi</sup>cient Market Hypothesis as follows.

• The Weak Form Ef<sup>fi</sup>cient Market: the variations of price, volume of trade and other historical information have fully re<sup>fl</sup>ected in stock prices. Hence, using past information to analyze stock situations cannot get excess returns. Because of this reason, technical analysis is not applied under this situation.

• The Semi-strong Form Ef<sup>fi</sup>cient Market: all readily-available public information including the variation of price, volume of trade, <sup>fi</sup>nancial statements and other information have fully re<sup>fl</sup>ected in stock prices. Therefore, it cannot acquire excess returns by using the information that everyone knows. For this reason, fundamental analysis is not applied under this situation.

![](/api/attachments/JTAEW9CW/fulltext/images/2c988299b16822b9335e94cb6c03cb6167322e2a60516308d4add2372c6e8877.jpg)  
Fig. 1. The procedure of searching the instance space by GA.

![](/api/attachments/JTAEW9CW/fulltext/images/ec00db8e8ba27e76f11bd2f139372ab9cdee80ea27fe414dbcdd812902be0d22.jpg)  
Fig. 2. The <sup>fi</sup>rst stage experiment.

• The Strong Form Ef<sup>fi</sup>cient Market: all information includes public and privileged information is fully re<sup>fl</sup>ected in prices. Privileged information involves knowledge available to a market marker, insider information available to corporate managers, etc. Therefore, both of public and privileged information cannot predict the market situation.

## 2.1.2. Stock price analysis methods

In literature, the most common analytical approaches are fundamental analysis and technical analysis described below.

• Fundamental analysis. Fundamental analysis believes that every stock has its intrinsic value. If the share prices lower than the intrinsic value, it means the stock is undervalued. In this case, we should buy this stock, and vice versa. Hence, a fundamental analysis is the process of analyzing information contained in <sup>fi</sup>nancial statements, such as the company's annual report, balance sheets, and income statements [41]. Some commonly used <sup>fi</sup>nancial ratio for stock price forecasting are current ratio, return on assets, liabilities ratio, etc.

In addition, economic factors also belong to this category. It depends on the statistics of the macroeconomics data and they have a signi<sup>fi</sup>cant in<sup>fl</sup>uence on the returns of individual stocks as well as stock index in general as they possess a signi<sup>fi</sup>cant impact on the growth and earnings' prospects of the underlying companies. Moreover, economic variables also affect the liquidity of the stock market. Some examples of the economic variables are in<sup>fl</sup>ation rates, employment <sup>fi</sup>gures and producers' price index, etc. After taking all these factors into account, the analyst can make a decision about whether to sell or buy a stock [29].

• Technical analysis. Technical analysis, also known as “charting”, has been a part of <sup>fi</sup>nancial practice for many decades [32,37]. It studies the historical price and volume movements of a stock by using charts as the primary tool to forecast future price movements [39]. This theory believes that the trends and patterns of an investment instrument's price, volume, breadth, and the trading activities re<sup>fl</sup>ect most of the relevant market information that a decision maker can utilize to determine its value [29]. Other technical indexes, which have been used for stock price prediction are such as moving average (MA) [29,37], moving average convergence and divergence (MACD) [9], psychological line (PSY) [9], relative strength index (RSI) [29], commodity channel index (CCI) [21], etc. For detailed descriptions, please refer to Achelis [2] and Jobman [21].

## 2.2. Feature selection

In many research problems, such as pattern recognition, it is important to choose a group of set of attributions with more prediction information. That is, if the number of irrelevant or redundant features is reduced drastically, the running time of a learning algorithm is also reduced. Moreover, a more general concept can be yielded. Performing feature selection can lead to many potential bene<sup>fi</sup>ts, which are facilitating data visualization and data understanding, reducing the measurement and storage requirements, reducing training and utilization times, defying the curse of dimensionality to improve prediction performances, etc. [13,25,38].

The following describe three well-known feature selection methods, which are Principal Component Analysis, genetic algorithm, and decision trees.

## 2.2.1. Principal Component Analysis

Principal Component Analysis (PCA) is a multivariate statistical technique. It aims at reducing the dimensionality of a dataset with a large number of interrelated variables. In particular, it extracts a small set of factors or components that are constituted of highly correlated elements, while retaining their original characters. After performing PCA, the uncorrelated variables which are called components, will replace the original variables. The total variability of a dataset produced by the complete set of m variables can often be accounted for primarily by a smaller set of k components of these variables (kbm). Therefore, the new dataset consists of n records on k components rather than n records on m variables as the original one. Speci<sup>fi</sup>cally, eigenvalues and eigenvetors of the principal components are computed in order to <sup>fi</sup>nd a linear combination of the original variables that makes the greatest variance. The <sup>fi</sup>rst principal component accounts for as much of the variability in the data, and the second principal component accounts for the remaining variability and so on. Particularly, the level of the variability for each feature lies in the range [0,1], in which the feature with 1 represents the highest variability. Therefore, if we need the components (i.e. features) which can explain 90% (i.e. 0.9) of the variability, features with 90% of the variability or higher can be selected [22].

## 2.2.2. Genetic algorithm

The main idea of Genetic Algorithms (GA) is from Darwin's theory of evolution from natural selection in the survival of the <sup>fi</sup>ttest. GA attempts to computationally mimic the processes by which natural selection operates. It works with a set of candidate solutions called population and generates successive populations of alternate solutions that are represented by a chromosome [14]. Associated with the characteristics of exploitation and exploration search, GA can deal with large search spaces ef<sup>fi</sup>ciently, and hence has less chance to get a local optimal solution than other algorithms [16].

In Siedlecki and Sklansky [46], a given feature subset is represented as a binary string (a ‘chromosome’) of length n (the total number of features), with a zero or one in position i denoting the absence (‘0’) or presence (‘1’) of feature i in the set. Then, each chromosome is evaluated to determine its <sup>fi</sup>tness, which determines how likely the chromosome is to survive and breed into the next generation. New chromosomes are created from old chromosomes by the process of crossover and mutation. In addition, doing these operators over and over again until some termination criterion is satis<sup>fi</sup>ed, we can <sup>fi</sup>nd the evolution of the optimal solution in a complex space.

(a) Intersection of two feature selection methods

![](/api/attachments/JTAEW9CW/fulltext/images/724dce9344e1aee6238b4fd0a63b54a6d838ba3eab57da29e5fc9c7bfb9984c0.jpg)

(b) Combination methods of the three feature selection methods  
![](/api/attachments/JTAEW9CW/fulltext/images/02b53484bb6c721c5f7461f8a0842968e2c39ec0a95c5e97e799f194d464e4d6.jpg)  
Fig. 3. The second stage experiment.

Fig. 1 shows the procedure for searching the instance space by GA [47]. That is, each member of the population in the GA is a single disjunct and the GA tries to <sup>fi</sup>nd the best possible disjunct at each generation. Then, the best disjunct replaces the rest through the operators. After GA converges, the best disjunct found is retained and the positive examples it covers are removed. This process is repeated until all the positive instances are covered. The <sup>fi</sup>nal rule or concept is then the disjunct of all the disjuncts found.

Note that the <sup>fi</sup>tness function looks at the number of positive and negative examples covered by the rule, and it also assigns partial credit for the number of attribute intervals on that rule that match the corresponding attribute values on a positive training example. For instance, a chromosome is an n dimensional binary vector, where n is the total number of features. If the i-th bit of the vector is 1, then the i-th feature is included in the subset. On the contrary, if the i-th is 0, the feature is not included. The <sup>fi</sup>tness function is determined for each chromosome in the population.

<table><tr><td colspan="4">2000</td><td colspan="4">2001</td><td colspan="4">2002</td><td colspan="4">2003</td><td colspan="4">2004</td><td colspan="4">2005</td><td colspan="4">2006</td><td colspan="2">2007</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>1</td><td>2</td><td>3</td><td>4</td><td>1</td><td>2</td><td>3</td><td>4</td><td>1</td><td>2</td><td>3</td><td>4</td><td>1</td><td>2</td><td>3</td><td>4</td><td>1</td><td>2</td><td>3</td><td>4</td><td>1</td><td>2</td><td>3</td><td>4</td><td>1</td><td>2</td></tr><tr><td colspan="24">Training 1</td><td>T</td><td colspan="5"></td></tr><tr><td></td><td colspan="24">Training 2</td><td>T</td><td colspan="4"></td></tr><tr><td colspan="2"></td><td colspan="24">Training 3</td><td>T</td><td colspan="3"></td></tr><tr><td colspan="3"></td><td colspan="24">Training 4</td><td>T</td><td colspan="2"></td></tr><tr><td colspan="3"></td><td colspan="25">Training 5</td><td>T</td><td></td></tr><tr><td colspan="4"></td><td colspan="25">Training 6</td><td>T</td></tr><tr><td colspan="24">Training 1</td><td colspan="6">T</td></tr><tr><td></td><td colspan="24">Training 2</td><td colspan="5">T</td></tr><tr><td colspan="3"></td><td colspan="23">Training 3</td><td colspan="4">T</td></tr><tr><td colspan="4"></td><td colspan="23">Training 4</td><td colspan="3">T</td></tr><tr><td colspan="4"></td><td colspan="24">Training 5</td><td colspan="2">T</td></tr></table>

Fig. 4. Sliding window by one quarter based testing data.

Fig.5. Sliding window by other-quarter based testing data.

## 2.2.3. Decision trees

The construction of a decision tree involves a collection of decision nodes, connected by branches, extending downward from the root node until terminating in leaf nodes. The leaf nodes of a decision tree means a result and the path from the root node to the leaf nodes constitute the required combination of conditions [30].

The Classi<sup>fi</sup>cation and Regression Trees (CART) [4] is a statistical technique that can select from a large number of explanatory variables those that are most important in determining the response variable to be explained [13]. The decision trees produced by CART are strictly binary, containing exactly two branches for each decision tree. The root node t is separated into two samples based on some condition. The samples that <sup>fi</sup>t the condition will be separated into the left nodes (t ), and the others will be separated into the right nodes (t ). P and P are the path that the node t goes through t and t . In particular, a decision tree is based on the entropy theory that the attribute (or feature) with the highest information gain (or greatest entropy reduction) is chosen as the test attribute for the non-leaf node. As a result, the decision nodes (t, t , and t ) can be regarded as representative features over a given dataset [7].

## 2.3. Related work

This section compares related work in terms of their datasets used, prediction models constructed, feature selection methods considered, etc. Table 1 shows the comparative result.

Regarding Table 1, we can see that much related work only considers one speci<sup>fi</sup>c index, i.e. either technical indexes or fundamental indexes (including economic factors). However, only Zarandi et al., [54] use both fundamental and technical indexes for stock prediction. Even related work uses the same index; the number of input variables used in these studies is different [3]. Therefore, currently there are no generally agreed representative variables for stock prediction. In addition, in the current stage there is no ‘best feature selection method for stock prediction. Consequently, related work only applies one chosen feature selection method to <sup>fi</sup>lter out irrelevant variables. This motivates us to collect all relevant variables used for stock prediction in literature and then combining multiple feature selection methods to identify more representative variables for improving prediction performances.

The fundamental and macroeconomic indexes.

<table><tr><td colspan="3">Fundamental indexes</td></tr><tr><td>ROA(A): EBI%</td><td>Gross margin growth</td><td>Quick ratio</td></tr><tr><td>Gross margin%</td><td>Operation income growth</td><td>Liabilities ratio</td></tr><tr><td>Operating income%</td><td>Net income growth</td><td>Total asset turnover</td></tr><tr><td>Net income%</td><td>Ordinary income growth</td><td>Account receivable turnover</td></tr><tr><td>Continued net income%</td><td>Continued income growth</td><td>Inventory turnover</td></tr><tr><td>Cash flow ratio</td><td>Total asset growth</td><td>Fixed asset turnover</td></tr><tr><td>Sales Growth ratio</td><td>Return on total asset</td><td>Days payables outstanding</td></tr><tr><td>Current ratio</td><td></td><td></td></tr><tr><td colspan="3">Macroeconomic indexes</td></tr><tr><td>US gross national product</td><td>Monitoring indicator</td><td>Export foreign exchange volume</td></tr><tr><td>US gross domestic product</td><td>Leading indicators</td><td>Government purchase</td></tr><tr><td>US unemployment rate</td><td>WPI increase rate</td><td>Government revenue</td></tr><tr><td>US Industrial Production</td><td>CCI Increase Rate</td><td>Taiwan Consumer Price Index (CPI)</td></tr><tr><td>US export trade amount</td><td>Import price index increase rate</td><td>Taiwan wholesale price index WPI</td></tr><tr><td>US import trade amount</td><td>Export price index increase rate</td><td>GNP deflator</td></tr><tr><td>US consumer price index CPI</td><td>US lagging indicator</td><td>Industrial production</td></tr><tr><td>US producer price index PPI</td><td>Foreign investment approval</td><td>Electric product export order</td></tr><tr><td>US real GDP</td><td>Taiwan unemployment rate</td><td>Machinery product export order</td></tr><tr><td>US real economic growth rate</td><td>Narrow monetary supply M1A</td><td>Electric machinery product export order</td></tr><tr><td>US CCI increase rate</td><td>Narrow monetary supply M1B</td><td>Information and communication product export order</td></tr><tr><td>US customer confident index CCI</td><td>Monetary supply M1B increase ratio</td><td>Taiwan total trading volume</td></tr><tr><td>US personal expenditure</td><td>Broad monetary supply M2</td><td>US total trading volume</td></tr><tr><td>US personal income (Quarter)</td><td>Broad monetary supply M2 increase rate</td><td>Import volume in dollar</td></tr><tr><td>US monetary amount (M1)</td><td>Narrow monetary supply M1A Increase Rate</td><td>Export amount to US</td></tr><tr><td>US monetary supply (M2)</td><td>Taiwan rediscount rate</td><td>Import amount from US</td></tr><tr><td>US industrial production increase rate</td><td>Foreign exchange rate</td><td>Export volume index</td></tr><tr><td>US current account of GDP in ratio</td><td>Foreign exchange reserves</td><td>Import volume index</td></tr><tr><td>Taiwan export volume in NT</td><td>Merchandise trade volume</td><td>Export growth rate</td></tr><tr><td>Taiwan import volume in NT</td><td>Merchandise export (F.O.B)</td><td>Import growth rate</td></tr><tr><td>Total import volume change rate in NT</td><td>Merchandise import (F.O.B)</td><td>Quasi money</td></tr></table>

Table 3 Parameter settings of GA.

<table><tr><td>Work</td><td>Population size</td><td>Crossover rate</td><td>Mutation rate</td></tr><tr><td>De Jong and Spears [8]</td><td>50</td><td>0.6</td><td>0.001</td></tr><tr><td>Grefenstette [12]</td><td>30</td><td>0.9</td><td>0.01</td></tr><tr><td>Kim and Han [24]</td><td>20</td><td>0.6</td><td>0.033</td></tr></table>

## 3. Experimental design

## 3.1. The experimental process

## 3.1.1. The first experimental stage

The experiment contains two stages. For the <sup>fi</sup>rst stage, this paper considers fundamental indexes as the input variables including <sup>fi</sup>nancial and macroeconomic variables from the Taiwan Economic Journal (TEJ) database. That is, <sup>fi</sup>nancial and macroeconomic variables are concatenated. In addition, the stock price information (i.e. the output variable) corresponding to the fundamental indexes is collected to be the dataset for later experiments. In particular, this is the original dataset without feature selection for training and testing the arti<sup>fi</sup>cial neural network (ANN) as the prediction model (c.f. Section 3.5).

Next, the original dataset is processed by Principal Component Analysis (PCA), Genetic Algorithms (GA), and decision trees (CART) respectively, in order to <sup>fi</sup>lter out unrepresentative variables. As a result, three processed datasets from the three feature selection methods can be obtained respectively. Then, each of the three processed datasets is divided into the training and testing datasets to construct the prediction model based on Arti<sup>fi</sup>cial Neural Networks (ANN) for stock prediction. Therefore, the aim of the <sup>fi</sup>rst stage is to <sup>fi</sup>nd out whether using one of these three feature selection methods can allow ANN to provide better performances than the model without feature selection. Fig. 2 shows the <sup>fi</sup>rst stage experiment.

## 3.1.2. The second experimental stage

For the second stage, the three feature selection methods are combined by the union, intersection, and multi-intersection methods (c.f. Section 3.6) in order to predict stock prices more effectively and <sup>fi</sup>nd out more representative variables. Fig. 3 shows the second stage experiment.

## 3.2. The dataset

The data source of this paper is based on the Taiwan Economic Journal (TEJ) database. In addition, the listed electronic corporations which are published by the Taiwan Stock Exchange (TSE)<sup>1</sup> are considered. This is because the government has invested a lot of efforts and resources in the electronic industry and many investors invest much money on this industry. Therefore, the electronic industry has become the mainstream in the stock market and it is the most competitive industry in Taiwan. In particular, its transactions contain over 70% of the Taiwan stock market.

![](/api/attachments/JTAEW9CW/fulltext/images/5802c8fc92dd1648d67111a496273ee4ebefaba574c1143d5c1eb564d72e81f0.jpg)  
(a)

![](/api/attachments/JTAEW9CW/fulltext/images/34936e456dd93c6d3888c367d2304dce398012f40303f0b3df74683ecc09fdcf.jpg)  
(b)

![](/api/attachments/JTAEW9CW/fulltext/images/987848c6dc8a505ecc5bf9c9c6a001ab6cd592ff5f9acd14319d177a711984f5.jpg)

![](/api/attachments/JTAEW9CW/fulltext/images/5222f424494741df2e4e9955eb28e658c7cee101442ab6b812c1be6392b85d48.jpg)  
(d)

(c)  
![](/api/attachments/JTAEW9CW/fulltext/images/f89580d14c5191425e9892087c20f680f77e96b7e590747ebf7cd0d8ef90c4d3.jpg)  
(e)

![](/api/attachments/JTAEW9CW/fulltext/images/d9da22a113bd030f0352f5deccef1dd27de1348a277f1c819b6c46f7d3475bb2.jpg)  
Fig. 6. The combination methods.  
(f)

Table 4  
Confusion matrix.

<table><tr><td>↓Actual\predicted→</td><td>Rise</td><td>Fall</td></tr><tr><td>Rise</td><td>a</td><td>b</td></tr><tr><td>Fall</td><td>c</td><td>d</td></tr></table>

Average accurac $\scriptstyle { \prime = { \frac { a + d } { a + b + c + d } } } .$  
Error rates for stocks ${ \mathrm { r i s e } } = { \frac { b } { a + b } } .$  
Error rates for stocks ${ \mathrm { f a l l } } = { \frac { c } { c + d } } .$

Table 5  
Prediction accuracy of by one quarter based testing data.

<table><tr><td></td><td>MLP (%)</td><td>PCA + MLP (%)</td><td>CART + MLP (%)</td><td>GA + MLP (%)</td></tr><tr><td>TEST1</td><td>72.46</td><td>73.16</td><td>71.74</td><td>73.19</td></tr><tr><td>TEST2</td><td>74.64</td><td>75.36</td><td>75.36</td><td>73.19</td></tr><tr><td>TEST3</td><td>74.64</td><td>73.91</td><td>75.36</td><td>74.64</td></tr><tr><td>TEST4</td><td>93.48</td><td>93.48</td><td>93.48</td><td>93.48</td></tr><tr><td>TEST5</td><td>64.49</td><td>62.32</td><td>62.32</td><td>62.32</td></tr><tr><td>TEST6</td><td>51.45</td><td>93.48</td><td>94.2</td><td>93.48</td></tr><tr><td>Avg. accuracy</td><td>71.86</td><td>78.62</td><td>78.74</td><td>78.38</td></tr></table>

Table 6  
Prediction accuracy by other-quarter based testing data.

<table><tr><td></td><td>MLP (%)</td><td>PCA + MLP (%)</td><td>CART + MLP (%)</td><td>GA + MLP (%)</td></tr><tr><td>TEST1</td><td>73.19</td><td>78.14</td><td>78.26</td><td>77.78</td></tr><tr><td>TEST2</td><td>79.86</td><td>78.7</td><td>79.28</td><td>72.61</td></tr><tr><td>TEST3</td><td>79.89</td><td>57.61</td><td>79.35</td><td>80.98</td></tr><tr><td>TEST4</td><td>56.76</td><td>82.61</td><td>54.11</td><td>79.71</td></tr><tr><td>TEST5</td><td>53.26</td><td>77.9</td><td>77.9</td><td>77.9</td></tr><tr><td>Avg. accuracy</td><td>68.59</td><td>74.99</td><td>73.78</td><td>77.8</td></tr></table>

This study chooses the data from the <sup>fi</sup>rst quarter of 2000 to the second quarter of 2007. Seasonal data are considered because of the volatility of stock prices. Moreover, there will be insuf<sup>fi</sup>cient samples if the research adopts the annual <sup>fi</sup>nancial report. Therefore, in order to cooperate with the data of <sup>fi</sup>nancial reports in seasons, the selected index will mainly be based on the months of 3, 6, 9, and 12. In total, there are 4140 data samples (i.e. case companies) composed of 2117 and 2023 samples for stocks' rise and fall respectively. Therefore, on average each quarter contains 159 data samples.

Furthermore, the sliding window method [34,41] is used to divide the sample data into different groups of training and testing data. The sliding window strategy is widely used in many frequent data mining, including stock market prediction [49]. In this paper, there are two testing strategies based on the sliding window. The <sup>fi</sup>rst one is to predict the single quarter of the stock price shown in Fig. 4. That is, for example, the training data of the <sup>fi</sup>rst group is from the <sup>fi</sup>rst quarter of 2000 to the fourth quarter of 2005. Then, the testing data (T) is based on the next quarter (i.e. the <sup>fi</sup>rst quarter of 2006). Therefore, the model is trained and tested for six times. As a result, there are six different rates of accuracy of the prediction model. Particularly, the proportion of training and testing data is 24:1.

The second strategy of using the sliding window is to predict the other quarters except the training ones shown in Fig. 5. That is, the training data is the same as the <sup>fi</sup>rst strategy. However, the testing data (T) are based on the other quarters except the training ones. For example, the <sup>fi</sup>rst group of the training data is based on the <sup>fi</sup>rst quarter of 2000 to the fourth quarter of 2005. For the testing data, it is from the <sup>fi</sup>rst quarter of 2006 to the second quarter of 2007. This is the situation when one only uses a model trained by ‘Training 1’ for stock prediction in any periods from 2006 to 2007. As a result, there are <sup>fi</sup>ve different models developed which provide <sup>fi</sup>ve different prediction results respectively. Speci<sup>fi</sup>cally, the proportions of training and testing data are 4:1 (24:6), 24:5, 6:1 (24:4), 8:1 (24:3), and 12:1 (24:2) respectively.

Table 7  
Prediction accuracy of multiple feature selections by one quarter based testing data.

<table><tr><td></td><td>Union (%)</td><td>Multi-intersection (%)</td><td> $PCA \cap GA$ (%)</td><td> $PCA \cap CART$ (%)</td><td> $GA \cap CART$ (%)</td></tr><tr><td>TEST1</td><td>71.74</td><td>73.91</td><td>71.74</td><td>27.54</td><td>27.54</td></tr><tr><td>TEST2</td><td>71.01</td><td>71.74</td><td>75.36</td><td>75.36</td><td>24.64</td></tr><tr><td>TEST3</td><td>75.36</td><td>74.64</td><td>74.64</td><td>74.64</td><td>74.64</td></tr><tr><td>TEST4</td><td>93.48</td><td>93.48</td><td>93.48</td><td>93.48</td><td>93.48</td></tr><tr><td>TEST5</td><td>62.32</td><td>62.32</td><td>62.32</td><td>62.32</td><td>62.32</td></tr><tr><td>TEST6</td><td>43.48</td><td>93.48</td><td>93.48</td><td>93.48</td><td>93.48</td></tr><tr><td>Avg. accuracy</td><td>69.57</td><td>78.262</td><td>78.50</td><td>71.14</td><td>62.68</td></tr></table>

## 3.3. Variables

As Huang and Tsai [15] and Kim [23] pointed out that technical indexes are applied to daily price change in the stock price, this paper considers fundamental indexes and macroeconomic indexes as the input variables except technical indexes for predicting the quarter based dataset. This is because the Taiwan stock market is the Weak Form Ef<sup>fi</sup>cient Market, which does not re<sup>fl</sup>ect all public information in stock prices [35].

Regarding literature review, all of the fundamental and macroeconomic indexes considered in related work are selected. In total, there are 85 variables selected for each data sample which are listed in Table 2.

Note that as the United States is an important trade partner of Taiwan, the economy of United States greatly in<sup>fl</sup>uences the Taiwan stock market. For example, for the year 2003, the share of Taiwan export to US was 18% and the share of Taiwan imports from US was 13.2%. Therefore, a great deal of United States macroeconomic indexes are considered in this paper. In addition, the experimental results show that most of the representative features selected by combining multiple feature selection methods (which can provide the highest accuracy rate and are important factors for Taiwan stock prediction) are United States macroeconomic indexes (c.f. Section 4.3.3).

For the output variables (i.e. class labels for the prediction model), since it is hard to de<sup>fi</sup>ne the degree of stocks' rise and decline, i.e. different investors may have different de<sup>fi</sup>nitions about stock price rising and declining, the <sup>fi</sup>rst attempt of this paper is to simply de<sup>fi</sup>ne two class labels, which are “1” and “−1”. For the output class labels of “1”, it means the stock price is higher than the previous quarter and “−1” means that the stock price is lower than the previous quarter. That is, the output (or classi<sup>fi</sup>cation) variable for each data sample is based on comparing its stock price between the i + 1-th quarter and the i-th quarter. For example, for a speci<sup>fi</sup>c case company if its stock price of the second quarter in 2006 is higher than the one of the <sup>fi</sup>rst quarter in 2006, then the output (or classi<sup>fi</sup>cation) variable of the second quarter in 2006 is “1”.

Table 8  
Prediction accuracy of multiple feature selections by other-quarter based testing data.

<table><tr><td></td><td>Union (%)</td><td>Multi-intersection (%)</td><td>PCANGA (%)</td><td>PCANCART (%)</td><td>GANCART (%)</td></tr><tr><td>TEST1</td><td>77.17</td><td>77.54</td><td>75.72</td><td>62.68</td><td>58.57</td></tr><tr><td>TEST2</td><td>77.39</td><td>78.99</td><td>79.57</td><td>79.86</td><td>69.71</td></tr><tr><td>TEST3</td><td>59.64</td><td>80.98</td><td>81.16</td><td>59.24</td><td>59.24</td></tr><tr><td>TEST4</td><td>55.56</td><td>83.09</td><td>83.09</td><td>74.88</td><td>83.09</td></tr><tr><td>TEST5</td><td>51.09</td><td>77.9</td><td>77.9</td><td>34.42</td><td>77.9</td></tr><tr><td>Avg. accuracy</td><td>64.17</td><td>79.7</td><td>79.49</td><td>62.22</td><td>69.7</td></tr></table>

![](/api/attachments/JTAEW9CW/fulltext/images/6f2892cd1ee59df0ae6138975b496e63dff71cef1c0a20781845f0192b4206b6.jpg)  
Fig. 7. Prediction accuracy of the MLP models by the one quarter based testing dataset.

Note that it can cause the problem of ‘predicting’ the known stock price movement since the quarterly data are only available after that quarter is over. Therefore, to test the prediction model over a speci<sup>fi</sup>c quarter, the input variables are based on its previous quarter. For example, given a constructed prediction model trained by ‘Training 1 shown in Fig. 4, the input variables of the <sup>fi</sup>rst quarter in 2006 (T) are based on the fourth quarter in 2005 and so on.

## 3.4. Feature selection

## 3.4.1. Principal Component Analysis

To perform PCA, the factors accounting for greater than 10% of the variance (eiqenvaluesN1) are kept in the analysis and the factor loading 0.5 are used as informative variables [45]. Speci<sup>fi</sup>cally, we set the factor loading equals to or greater than 0.5 to extract the important variables from the dataset. To enhance these factors' interpretability, we consider the varimax factor rotation method to minimize the number of variables that have high loading on a factor. That is, varimax rotation maximizes the sum of the variance of the squared loadings. Speci<sup>fi</sup>cally, for each factor, high loadings (i.e. correlations) will result in a few variables, and the rest will be near zero [22].

In addition, the selection of the important principal component is based on the requirement that the percentage of the total variance is 95% [52]. Note that after the factor loading which is lower than 0.5 is deleted from the original dataset, the total variance of the processed dataset has attained to 95.45%.

![](/api/attachments/JTAEW9CW/fulltext/images/c12a37e2bf2808cea2777effee20fb46dffa08592ad32a0214e4dc0493786fcf.jpg)  
Fig. 8. Prediction accuracy of the MLP models by the other-quarter based testing dataset.

![](/api/attachments/JTAEW9CW/fulltext/images/e54865ea8872eae30eccd88645186f58a626a908f72fada8bf9a468af50bf7f7.jpg)  
Fig. 9. Error rates of the MLP models by one quarter based testing dataset.

![](/api/attachments/JTAEW9CW/fulltext/images/5cbc0d5988501167917db5b0a7a8b314b723aa51ce6863eba8079b765d87738e.jpg)  
Fig. 10. Error rates of the MLP models by the other-quarter based testing dataset.

## 3.4.2. Genetic Algorithm

In this study, the second feature selection method we used is based on Genetic Algorithms (GA). There are several different parameter settings for GA shown in Table 3. According to the prediction performance, the parameters used in this paper for later comparisons are as follows: the population size is set to 20, the crossover rate is set to 0.6 and the mutation rate is set to 0.033.

## 3.4.3. Decision trees

The CART (Classi<sup>fi</sup>cation and Regression Trees) is used as the third feature selection method. The default value<sup>2</sup> is used to establish the initial decision tree (based on a given training set) and then pruning the least related variables in order to select the explanatory variables and split point with the highest reduction of impurity.

To prune the initial decision tree, the minimum support and the score method are considered to create the tree branches. In particular, we set the minimum support for 100 (i.e. to delete the rules which contain less than 100), and the result does not make the prediction performance different. In addition, entropy and Bayesian methods can be used to create the tree branches, and we found that the entropy method can provide the best prediction performance over the given dataset.

## 3.5. Artificial neural network

In this paper, we used multi-layer perceptron (MLP) arti<sup>fi</sup>cial neural networks with the back-propagation learning algorithm as the baseline prediction model. This is because approximately 95% of business application studies utilize MLP [48]. In addition, the most popular learning method is back-propagation [18,40]. Since the focus of this paper is not on developing a novel prediction model, it is feasible to construct the widely applied model, i.e. MLP, as the baseline prediction model for comparisons. The following parameters of constructing a MLP network are as follows:

• Learning rate. The learning rate is the parameter in the learning rule that aids the convergence of errors. In the general case, a learning rate of 0.9 is recommended. However, if the learning rate is too high, it will cause the error to oscillate and thus prevent the converging process [43].

• Hidden layer. Regarding prior studies [33,42,51], it is found that using one hidden layer of MLP in the area of stock price prediction can have better performances. Therefore, in this paper, we consider one hidden layer to construct the MLP model.

• Hidden layer node. In literature [42,51], there is no precise number to the node of the hidden layer. If there are too few nodes, the network cannot re<sup>fl</sup>ect the relationship between input variables, which may result in the under-<sup>fi</sup>tting problem. On the other hand, too many nodes will cause the over-<sup>fi</sup>tting problem easily. Hence, we use 6, 12, and 18 respectively in order to <sup>fi</sup>nd the optimal number of the hidden layer node.

• Training epoch. The linking value will gradually be adjusted when the MLP model is trained continuously. In order to make the error of the target value and the output of the neural network become closer, it will become convergent when two of the values do not change. In this paper, we consider the training epoch of 100, 300, 500, and 1000 respectively to <sup>fi</sup>nd the best training epoch.

As a result, there will be 72 and 60 models for each feature selection method over the one quarter and other-quarter based testing datasets respectively. That is, for the example of the one quarter based testing dataset, it contains six testing subsets based on the sliding window and every sample is used for training for 12 times (i.e. three different hidden layer nodes and four different training epochs).

Table 10  
The selected variables by PCA∩GA and the multi-intersection approach.

<table><tr><td>PCANGA</td><td></td><td colspan="2">The multi-intersection approach</td></tr><tr><td>1</td><td>US gross national income</td><td>1</td><td>US gross national income</td></tr><tr><td>2</td><td>US producer price index</td><td>2</td><td>US Producer Price Index</td></tr><tr><td>3</td><td>US annual changes in consumer price index</td><td>3</td><td>US annual changes in consumer price index</td></tr><tr><td>4</td><td>US personal consumption expenditures</td><td>4</td><td>US personal consumption expenditures</td></tr><tr><td>5</td><td>US annual changes in industrial production index</td><td>5</td><td>US annual changes in industrial production index</td></tr><tr><td>6</td><td>US current account to GDP ratio</td><td>6</td><td>US current account to GDP ratio</td></tr><tr><td>7</td><td>Taiwan unemployment rate</td><td>7</td><td>Taiwan unemployment rate</td></tr><tr><td>8</td><td>Quasi money</td><td>8</td><td>Quasi money</td></tr><tr><td>9</td><td>Export amount to US</td><td>9</td><td>Export amount to US</td></tr><tr><td>10</td><td>US merchandise trade volume</td><td>10</td><td>US merchandise trade volume</td></tr><tr><td>11</td><td>The export order for electric products</td><td>11</td><td>The export order for electric products</td></tr><tr><td>12</td><td>GNP deflator</td><td>12</td><td>GNP deflator</td></tr><tr><td>13</td><td>US monetary supply</td><td>13</td><td>US monetary supply</td></tr><tr><td>14</td><td>Narrow monetary supply</td><td>14</td><td>Narrow monetary supply</td></tr><tr><td></td><td></td><td>15</td><td>Import quantum index</td></tr><tr><td></td><td></td><td>16</td><td>Annual changes in export price index</td></tr><tr><td></td><td></td><td>17</td><td>Industrial production index</td></tr></table>

## 3.6. Combination methods

Regarding Fig. 3, there are six different methods of combining the chosen three feature selection methods. Fig. 6 shows the concept diagram of these combination methods. That is, Fig. 6(a), (b), and (c) are the intersections of two feature selection methods and the result of the intersection method is based on the repeated variables selected by two of the combined feature selection methods. Fig. 6(d) is the intersection of the three feature selection methods.

On the other hand, the result of using the union combination method is based on all variables that have been selected by each of the three feature selection methods shown in Fig. 6(e).

Finally, for the multi-intersection method, the repeated variables of PCA and GA, PCA and CART, GA and CART are selected as shown in Fig. 6 (f).

## 3.7. Evaluation strategies

To assess the performance of the developed prediction models, accuracy and error rates are examined. They can be measured by a confusion matrix shown in Table 4.

## 4. Results

## 4.1. Single feature selection methods

Tables 5 and 6 show the rate of prediction accuracy of the four different MLP models based on the one quarter and other-quarter based testing datasets respectively. As we can see, the results are slightly different if different testing datasets are considered. In particular, larger testing dataset could degrade the prediction performance of the models. Note that the prediction accuracy rate for each test set is based on the best parameter setting of MLP (c.f. Section 3.5). That is, for each test set (‘T’ in Figs. 4 and 5) there are 12 MLP models constructed and only the best MLP, which provides the highest rate of accuracy, is listed here.

Based on the one quarter based testing dataset, the MLP models followed by PCA, CART, and GA performs similarly, which can provide about 78% accuracy. This may be because the testing data are only based on one quarter, i.e. the testing data size is relatively small, which cannot make these MLP models perform signi<sup>fi</sup>cantly different. On the other hand, for the other-quarter based testing dataset, GA+MLP performs the best (77.8% on average). Moreover, only the model of GA+MLP degrades the least accuracy rate from the one quarter to other-quarter based testing datasets. This implies that feature selection using GA could make the prediction model more stable than the other feature selection methods.

It is interesting that for ‘TEST5’ of one quarter based testing data (Table 5), all of the models do not perform well, which means that the <sup>fi</sup>rst quarter of 2007 is dif<sup>fi</sup>cult to forecast. However, for ‘TEST6’ the baseline MLP model performs even worse than ‘TEST5’, but the other three models followed by feature selection provide relative good performances. This is similar to ‘TEST4’ and ‘TEST5’ of other-quarter based testing data (Table 6). Therefore, it implies that the baseline MLP model is not suitable and unstable for predicting newer testing data.

## 4.2. Multiple feature selection methods

Tables 7 and 8 show the prediction performances of the MLP models by combining multiple feature selection methods over the one quarter and other-quarter based testing datasets respectively. Note that the feature selection result of GA CART is the same as the intersection between PCA, GA, and CART (PCA∩GA∩CART).

The results indicate that the intersection between PCA and GA outperforms the other combination approaches over the one quarter based testing dataset. On the other hand, combining multiple feature selection methods by the multi-intersection approach performs the best based on the other-quarter based testing dataset. However, the rates of prediction accuracy by both combination approaches over the two testing datasets do not have a big difference, i.e. less than 0.3%.

Table 11  
T-test of prediction accuracy (p value) by the one quarter based testing dataset.

<table><tr><td></td><td>Baseline</td><td>PCA</td><td>CART</td><td>GA</td><td>Union</td><td>Multi-intersection</td><td> $PCA \cap GA$ </td><td> $PCA \cap CART$ </td><td> $GA \cap CART$ </td></tr><tr><td>Baseline</td><td></td><td>0.139</td><td>0.193</td><td>0.001</td><td>0.311</td><td>0.000</td><td>0.000</td><td>0.973</td><td>0.009</td></tr><tr><td>PCA</td><td></td><td></td><td>0.792</td><td>0.375</td><td>0.040</td><td>0.005</td><td>0.001</td><td>0.143</td><td>0.000</td></tr><tr><td>CART</td><td></td><td></td><td></td><td>0.287</td><td>0.081</td><td>0.012</td><td>0.000</td><td>0.300</td><td>0.004</td></tr><tr><td>GA</td><td></td><td></td><td></td><td></td><td>0.000</td><td>0.015</td><td>0.001</td><td>0.004</td><td>0.000</td></tr><tr><td>Union</td><td></td><td></td><td></td><td></td><td></td><td>0.000</td><td>0.000</td><td>0.609</td><td>0.026</td></tr><tr><td>Multi-intersection</td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.110</td><td>0.000</td><td>0.000</td></tr><tr><td> $PCA \cap GA$ </td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.000</td><td>0.000</td></tr><tr><td> $PCA \cap CART$ </td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.001</td></tr><tr><td> $GA \cap CART$ </td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Table 9  
Numbers of features selected vs. accuracy rates.

<table><tr><td></td><td>PCA</td><td>CART</td><td>GA</td><td>Union</td><td>Multi-intersection</td><td> $PCA \cap GA$ </td><td> $PCA \cap CART$ </td><td> $GA \cap CART$ </td></tr><tr><td>No. features selected</td><td>64</td><td>11</td><td>17</td><td>72</td><td>17</td><td>14</td><td>5</td><td>2</td></tr><tr><td>Accuracy (one quarter)</td><td>78.66% (2)</td><td>78.743% (1)</td><td>78.38% (4)</td><td>69.57% (7)</td><td>78.262% (5)</td><td>78.50% (3)</td><td>71.14% (6)</td><td>62.68% (8)</td></tr><tr><td>Accuracy (other quarters)</td><td>74.99% (4)</td><td>72.62% (5)</td><td>77.8% (3)</td><td>64.17% (7)</td><td>79.7% (1)</td><td>79.49% (2)</td><td>62.22% (8)</td><td>69.7% (6)</td></tr><tr><td>Avg. accuracy</td><td>76.83% (4)</td><td>75.68% (5)</td><td>78.09% (3)</td><td>66.87% (6)</td><td>78.98% (2)</td><td>79.00% (1)</td><td>66.68% (7)</td><td>66.19% (8)</td></tr></table>

## 4.3. Further comparisons

## 4.3.1. Prediction accuracy

Figs. 7 and 8 further compare average prediction accuracy of the MLP models using different feature selection methods over the one quarter and other-quarter based testing datasets respectively.

For prediction accuracy, as we can see that the MLP model followed by each of the three single feature selection methods performs better than the baseline MLP model over the two different testing datasets. On the other hand, combining multiple feature selection methods by the PCA∩GA and multi-intersection approaches also perform better than the baseline MLP model.

Although the prediction performances of using single feature selection methods (i.e. PCA, CART, and GA) and combining multiple feature selection methods (i.e. PCA GA and multi-intersection) do not have a big difference, the later methods can provide much higher accuracy than the single feature selection methods over the otherquarter based testing dataset.

## 4.3.2. Prediction errors

Figs. 9 and 10 show the error rates of the MLP models using different feature selection methods over the one quarter and otherquarter based testing datasets respectively. It is interesting that all of these prediction models do not perform well for predicting stocks' fall. We believe that this is because we did not exclude the data which may be dif<sup>fi</sup>cult to forecast, such as the president election in the <sup>fi</sup>rst quarters of 2000 and 2004 and the 9/11 and SARS events from 2000 to the <sup>fi</sup>rst quarter of 2001.

However, the error rate of predicting stocks' rise is relatively lower. Particularly, the MLP models by PCA GA and the multiintersection approach outperform the others. This implies that given a new stock, investors who would like to make successful investments can only rely on the decision of the prediction model for the stock rises. If investors follow the output of the prediction model for the case of stocks' fall, then investors are very likely to make incorrect decisions. In other words, these models can help investors make decisions for buying ‘rising’ stocks, rather than selling ‘falling’ stocks if they have held.

## 4.3.3. Selected features vs. prediction accuracy

Table 9 compares these feature selection methods in terms of the number of features selected and their corresponding accuracy rates.

Regarding Table 9, very few input variables still have a high discriminate power for stock prediction. For example, the 11 features (out of 85) selected by CART allow the MLP model to produce 78.743% accuracy over the one quarter based testing dataset and 17 features selected by the multi-intersection approach for 79.7% accuracy over the other-quarter based testing dataset. In other words, these variables can be regarded as the important factors of affecting stocks rise and fall.

On average, combining PCA and GA by the intersection approach provides the highest accuracy rate (79%) and the multi-intersection approach performs the second (78.98%). For single feature selection methods, GA performs the best (78.09%). On the other hand, the union combination approach, PCA∩CART and GA∩CART performs the worst (i.e. below 70%). Therefore, we can conclude that combining multiple speci<sup>fi</sup>c feature selection methods is able to allow the stock prediction model to perform better than using single feature selection methods. However, the combination methods used need to be carefully considered.

Table 10 lists the variables selected by PCA∩GA and the multiintersection approach. Both approaches select the same 14 variables, in which the later one selects three more variables. This indicates that the U.S. stock market has a leading effect to the Taiwan stock market. Therefore, for future stock prediction and investments, these 14 variables can be considered.

## 4.3.4. Statistical analysis

To analyze the level of signi<sup>fi</sup>cant difference of prediction accuracy by using different feature selection methods, t-test is used. Tables 11 and 12 show the t-test result over the one and other-quarter based testing datasets respectively.

Regarding above analyses, we can see that considering single feature selection methods, PCA, CART, and GA do not make MLP perform signi<sup>fi</sup>cantly different over the two testing datasets. However, only the model of GA+MLP provides a high level of signi<sup>fi</sup>cant difference from the baseline MLP. For combining multiple feature selection methods, the prediction results of the MLP models using the PCA∩GA and multiintersection approaches over the two testing datasets are signi<sup>fi</sup>cantly different from the ones using single and other combined multiple feature selection methods.

## 5. Conclusion

In stock prediction, fundamental and technical indexes composed of different variables have been widely used in literature. As feature selection aiming at selecting more representative features for better prediction results, most of the related studies only use one chosen feature selection method for stock prediction. This paper compares three different feature selection methods, i.e. Principal Component Analysis (PCA), Genetic Algorithms (GA), and decision trees (CART) and combines them based on union, intersection, and multiintersection approaches to examine their prediction accuracy and errors.

The experimental results show that combining multiple feature selection methods can provide better prediction performances than using single feature selection methods. In particular, the intersection between PCA and GA and the multi-intersection of PCA, GA, and CART perform the best, which provide the highest rate of prediction accuracy and the lowest error rate of predicting stocks' rise. This <sup>fi</sup>nding directly corresponds to the success of classi<sup>fi</sup>er ensembles, which is based on the diversity of individual classi<sup>fi</sup>ers [26]. That is, the ways of selecting features by PCA, GA, and CART individually are different, which can make the selected features by these three methods much diversi<sup>fi</sup>ed (see Table 9)<sup>3</sup>. Therefore, the multiintersection of PCA, GA, and CART can provide the best performance. For the intersection between PCA and GA, they select 14 features, which are the same as the 14 features out of 17 by the multiintersection approach. This approach of course also performs very well, which is similar to multi-intersection of PCA, GA, and CART.

Table 12  
T-test of prediction accuracy (p value) by the other-quarter based testing dataset.

<table><tr><td></td><td>Baseline</td><td>PCA</td><td>CART</td><td>GA</td><td>Union</td><td>Multi-intersection</td><td>PCANGA</td><td>PCANCART</td><td>GANCART</td></tr><tr><td>Baseline</td><td></td><td>0.859</td><td>0.068</td><td>0.015</td><td>0.384</td><td>0.000</td><td>0.000</td><td>0.356</td><td>0.800</td></tr><tr><td>PCA</td><td></td><td></td><td>0.359</td><td>0.031</td><td>0.573</td><td>0.000</td><td>0.000</td><td>0.612</td><td>0.664</td></tr><tr><td>CART</td><td></td><td></td><td></td><td>0.391</td><td>0.036</td><td>0.001</td><td>0.000</td><td>0.022</td><td>0.198</td></tr><tr><td>GA</td><td></td><td></td><td></td><td></td><td>0.001</td><td>0.000</td><td>0.000</td><td>0.003</td><td>0.020</td></tr><tr><td>Union</td><td></td><td></td><td></td><td></td><td></td><td>0.000</td><td>0.000</td><td>0.967</td><td>0.841</td></tr><tr><td>Multi-intersection</td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.007</td><td>0.000</td><td>0.000</td></tr><tr><td>PCANGA</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.000</td><td>0.000</td></tr><tr><td>PCANCART</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.830</td></tr><tr><td>GANCART</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Moreover, these two combined approaches select 14 and 17 important variables respectively from the 85 original variables, which <sup>fi</sup>lter out many unrepresentative variables. These variables can be used not only for practical investment decisions, but also for future research as the ‘standard’ input variables to construct novel prediction models for comparisons.

It should be noted that although this paper considers three popular feature selection methods, there are other methods available in literature, for example, information gain [31], independent component analysis [27], and other variants of PCA, such as kernel PCA [44], asymmetric PCA [20], etc. However, from the practical standpoint, it is dif<sup>fi</sup>cult to conduct a comprehensive study on all existing feature selection methods. In addition, currently it is hard to de<sup>fi</sup>ne the most representative method in the stock prediction domain, and there is no comparative study based on these methods, which can be regarded as one of the future research issues.

## References

[1] A. Abraham, N. Baikunth, P.K. Mahanti, Hybrid intelligent systems for stock market analysis, Lecture Notes in Computer Science 2074 (2001) 337–345.

[2] S.B. Achelis, Technical Analysis from A to Z, McGraw-Hill, New York, 2000.

[3] G.S. Atsalakis, K.P. Valavanis, Surveying stock market forecasting techniques — part II: soft computing methods, Expert Systems with Applications 36 (3) (2009) 5932–5941.

[4] L. Breiman, J. Friedman, R. Olshen, S. Stone, Classi<sup>fi</sup>cation and Regression Trees, Chapman & Hall/CRC Press, Florida, 1984.

[5] P.C. Chang, C.H. Liu, A TSK type fuzzy rule based system for stock price prediction, Expert Systems with Application 34 (1) (2008) 135–144

[6] G. Cordinly, Guide to the Stock Exchange, 2nd EdRichard D., Irwin, Inc, 1907.

[7] M. Dash, H. Liu, Feature selection for classi<sup>fi</sup>cation, Intelligent Data Analysis 1 (1997) 131–156.

[8] K.A. De Jong, W.M. Spears, An analysis of the interacting roles of population size and crossover in genetic algorithms, Proceedings of the First Workshop on Parallel Problem Solving from Nature, 1990, pp. 38–47.

[9] J.L. Du, Know-how of Applications of Technical Indices in Taiwan Stock Market, Wealth Press, 2003.

[10] D. Enke, S. Thawornwong, The use of data mining and neural networks for forecasting stock market returns Expert System with Applications 29 (4) (2005) 927–940

[11] E.F. Fama, Random walks in stock market prices, Financial Analysis Journal 21 (1965) 55–59.

[12] J.J. Grefenstette, Optimization of control parameters for genetic algorithms, IEEE Transactions on Systems, Man, and Cybernetics 16 (1) (1986) 122–128.

[13] I. Guyon, A. Elisseeff, An introduction to variable and feature selection, Journal of Machine Learning Research 3 (2003) 1157–1182.

[14] J. Holland, Adaptation in Natural and Arti<sup>fi</sup>cial Systems, University of Michigan Press. 1975

[15] C.L. Huang, C.Y. Tsai, A hybrid SOFM-SVR with a <sup>fi</sup>lter-based feature selection for stock market forecasting, Expert System with Applications 36 (2) (2009) 1529–1539.

[16] C.L. Huang, C.J. Wang, A GA-based feature selection and parameters optimization for support vector machines, Expert Systems with Applications 31 (2006) 231–240.

[17] D. Hulme, S. Xu, Application of genetic algorithm to the optimisation of neural network con<sup>fi</sup>guration for stock market forecasting, Lecture Notes in Arti<sup>fi</sup>cial Intelligence 2256 (2001).285–296

[18] H. Ince, T.B. Tradalis, A hybrid model for exchange rate prediction, Decision Support Systems 42 (2) (2006) 1054–1062.

[19] H. Ince, T.B. Tradalis, Kernel principal component analysis and support vector machines for stock price prediction, IEEE International Joint Conference on Neural Networks, 2004, pp. 2053–2058.

[20] X. Jiang, Asymmetric principal component and discriminant analyses for pattern classi<sup>fi</sup>cation, IEEE Transactions on Pattern Analysis and Machine Intelligence 31 (5) (2009) 931–937.

[21] D.R. Jobman, The Handbook of Technical Analysis: A Comprehensive Guide to Analytical Methods, Trading Systems and Technical Indicators, McGraw-Hill, New York, 1994.

[22] I.T. Jolliffe, Principal Component Analysis, Springer Verlag, New York, 1986.

[23] K.J. Kim, Financial time series forecasting using support vector machines, Neurocomputing 55 (2003) 307–319.

[24] K.J. Kim, I. Han, Genetic algorithm approach to feature discretization in arti<sup>fi</sup>cial neural network for the prediction of stock price index, Expert Systems with Applications 19 (2) (2000) 125–132.

[25] Y. Kim, Toward a successful CRM: variable selection, sampling, and ensemble, Decision Support Systems 41 (2) (2006) 542–553.

[26] J. Kittler, M. Hatef, R.P.W. Duin, J. Matas, J. On, Combining classi<sup>fi</sup>ers, IEEE Transactions on Pattern Analysis and Machine Intelligence 20 (3) (1998) 226–239.

[27] N. Kwak, C. Kim, H. Kim, H. Dimensionality, Reduction based on ICA for regression problems, Neurocomputing 71 (2008) 2596–2603.

[28] R.K. Lai, C.Y. Fan, W.H. Huang, P.C. Chang, Evolving and clustering fuzzy decision tree for <sup>fi</sup>nancial time series data forecasting, Expert Systems with Applications 36 (2) (2009) 3761–3773.

[29] M. Lam, Neural network techniques for <sup>fi</sup>nancial performance prediction: integrating fundamental and technical analysis, Decision Support System 37 (4) (2004) 567–581.

[30] D.T. Larose, Data Mining Method and Models, John Wiley & Sons, Inc., New Jersey, 2006.

[31] C. Lee, G.G. Lee, Information gain and divergence-based feature selection for machine learning-based text categorization, Information Processing and Management 42 (1) (2006) 155–165.

[32] W. Leigh, N. Modani, R. Hightower, A computational implementation of stock charting: abrupt volume increase as signal for movement in New York stock exchange composite index, Decision Support Systems 37 (4) (2004) 515–530.

[33] J. Li, M.T. Manry, P.L. Narasimha, C. Yu, Feature selection using a piecewise linear network, IEEE Transactions on Neural Networks 17 (5) (2006) 1101–1115.

[34] S.T. Li, S.C. Kuo, Knowledge discovery in <sup>fi</sup>nancial investment for forecasting and trading strategy through wavelet-based SOM networks, Expert Systems with Applications 34 (2) (2008) 935–951.

[35] K.P. Lim, R.D. Brooks, M.J. Hinich, Nonlinear serial dependence and the weak-form ef<sup>fi</sup>ciency of Asian emerging stock markets, Journal of International Financial Markets, Institutions and Money 18 (5) (2008) 527–544.

[36] X. Lin, Z. Yang, Y. Song, Short-term stock price prediction based on echo state networks, Expert Systems with Applications 36 (3) (2009) 7313–7317.

[37] A.W. Lo, H. Mamaysky, J. Wang, Foundation of technical analysis: computations, algorithm, statistical inference, and empirical implementation, Journal of Finance 55 (4) (2000) 1705–1765.

[38] D. Mladenic´, M. Grobelnik, Feature selection on hierarchy of web documents, Decision Support Systems 35 (1) (2003) 45–87.

[39] J.J. Murphy, Technical Analysis of the Financial Markets: A Comprehensive Guide to Trading Methods and Applications, New York Institute of Finance, 1999.

[40] S. Olafsson, X. Li, S. Wu, Operations research and data mining, European Journal of Operational Research 187 (3) (2008) 1429–1448.

[41] D. Olson, C. Mossman, Neural network forecasts of Canadian stock returns using accounting ratios International Journal of Forecasting 19 (3) (2003) 453–465

[42] M. Paliwal, U.A. Kumar, Neural networks and statistical techniques: a review of applications, Expert Systems with Applications 36 (1) (2009) 2–17.

[43] T.S. Quah, B. Srinvasan, Improving returns on stock investment through neural network selection, Expert Systems with Applications 17 (4) (1999) 295–301.

[45] V. Shih, Q. Zhang, M. Liu, Comparing the performance of Chinese banks: a principal component approach, China Economic Review 18 (2007) 15–34.

[46] W. Siedlecki, J. Sklansky, A note on genetic algorithms for large-scale feature selection, Pattern Recognition Letters 10 (5) (1989) 335–347.

[47] R. Sikora, S. Piramuthu, Framework for ef<sup>fi</sup>cient feature selection in genetic algorithm based data mining, European Journal of Operational Research 180 (2) (2007) 723–737.

[48] K.A. Smith, J.N.D. Gupta, Neural networks in business: techniques and applications for the operations researcher, Computers & Operations Research 27 (11–12) (2000) 1023–1044.

[49] S.K. Tanbeer, C.F. Ahmed, B.-S. Jeong, Y.-K. Lee, Sliding window-based frequent pattern mining over data streams, Information Sciences 179 (22) (2009) 3843–3865.

[50] C.-F. Tsai, Feature selection in bankruptcy prediction, Knowledge-Based Systems 22 (2) (2009) 120–127.

[51] P.M. Tsang, P. Kwok, S.O. Choy, R. Kwan, S.C. Ng., J. Mak, J. Tsang, K. Koong, T.L Wong, Design and implementation of NN5 for Hong Kong stock price forecasting, Engineering Applications of Arti<sup>fi</sup>cial Intelligence 20 (4) (2007) 453–461.

[52] N.K. Vitanov, K. Sakai, Z.I. Dimitrova, SSA, PCA, TDPSC, ACFA: useful combination of methods for analysis of short and nonstationary time series, Chaos, Solitions and Fractals 37 (1) (2008) 187–202.

[53] L. Yu, S. Wang, K.K. Lai, Mining stock market tendency using GA-based support vector machines, Lecture Notes in Computer Science 3828 (2005) 336–345.

[54] F.M.H. Zarandi, B. Rezaee, I.B. Turksen, E. Neshat, A type-2 fuzzy rule-based expert system model for stock price analysis, Expert Systems with Applications 36 (1) (2009) 139–154.

Dr. Chih-Fong Tsai obtained a PhD at School of Computing and Technology from the University of Sunderland, UK in 2005 for the thesis entitled “Automatically Annotating Images with Keywords”. He is now an associate professor at the Department of Information Management, National Central University, Taiwan. He has published over 20 refereed journal papers including ACM Transactions on Information Systems, Pattern Recognition, Information Processing & Management, Applied Soft Computing, Neurocomputing, Knowledge-Based Systems, Expert Systems with Applications, Expert Systems, Online Information Review, International Journal on Artificial Intelligence Tools, Journal of Systems and Software, etc. In 2008, he received the ‘Highly Commended Award’ (Emerald Literati Network 2008 Awards for Excellence) for a paper published in Online Information Review (“A Review of Image Retrieval Methods for Digital Cultural Heritage Resources”). His current research focuses on multimedia information retrieval and data mining applications.

Miss Yu-Chieh Hsiao received the Master's degree from the Department of Accounting and Information Technology, National Chung Cheng University, Taiwan. Her research interest focuses on data mining applications.
