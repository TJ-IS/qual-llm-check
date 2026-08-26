---
otero_id: 376
otero_key: "TGWXM44Y"
title: "Prediction of movement direction in crude oil prices based on semi-supervised learning"
authors: "Hyunjung Shin; Tianya Hou; Kanghee Park; Chan-Kyoo Park; Sunghee Choi"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.11.009"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Prediction of movement direction in crude oil prices based on semi-supervised learning

Hyunjung Shin <sup>a,</sup>⁎<sup>,1</sup>, Tianya Hou <sup>b,1</sup>, Kanghee Park <sup>a</sup>, Chan-Kyoo Park <sup>c</sup>, Sunghee Choi <sup>d</sup>

<sup>a</sup> Department of Industrial Engineering, Ajou University, San 5 Wonchun-dong, Yeongtong-gu, Suwon, 443-749, Republic of Korea

<sup>b</sup> Department of Building and Real Estate, Hong Kong Polytechnic University, Hung Hom, Kowloon, Hong Kong

<sup>c</sup> Department of Management, Dongguk University-Seoul Campus, 3-26 Pildong, Chung-gu, Seoul, 100-715, Republic of Korea

<sup>d</sup> Department of International Commerce, Keimyung University, 2800 Dalgubeoldaero, Dalseo-gu, Daegu, 704-701, Republic of Korea

## a r t i c l e i n f o

Article history: Received 21 May 2011 Received in revised form 21 March 2012 Accepted 4 November 2012 Available online 12 November 2012

Keywords: Oil price prediction Semi-supervised learning (SSL) Technical indicators Feature extraction (PCA/NLPCA) Machine learning

## a b s t r a c t

Oil price prediction has long been an important determinant in the management of most sectors of industry across the world, and has therefore consistently required detailed research. However, existing approaches to oil price prediction have sometimes made it rather dif<sup>fi</sup>cult to implement the complex interconnected relationship between the price of oil and other global/domestic economic factors. This has been complicated by the in<sup>fl</sup>uence of the irregular impact caused by the economic factors that affect the oil price. Recently, a machine learning algorithm, known as semi-supervised learning (SSL) has emerged, whose strength is the ease it can bring to the network representation of entities and the explicitness of inference which is expressed through relations between different entities. Since an awareness of the network representation of complicated relations between economic factors including the oil price is natural in SSL, this method allows the effects of the impact of economic factors on the oil price to be assessed with improved accuracy. SSL has so far been exploited in dealing with the non timeseries types of entity, but not for the time-series types. Therefore, the proposed study is to exploit the method of representing the network between these time-series entities, and to then employ SSL to forecast the upward and downward movement of oil prices. The proposed SSL approach will be tested using one-month-ahead monthly crude oil price predictions between January 1992 and June 2008.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

For many years, the price of crude oil price has been an important determinant of global or national economic performance. An increase or decrease in the oil price will have a marked economic effect on all countries in the world. Thus the state of oil prices is a consistent preoccupation of economic experts in most industries, as well as many politicians. A change in the crude oil price can lead to a transfer of income between importing and exporting countries through a shift in the terms of trade [7], since oil is the world's most actively traded commodity accounting for over 10% of total world trade [27]. For net oil-importing countries, higher oil prices can lead to a drop in real national income caused by increased input costs, along with reduced non-oil demand, higher in<sup>fl</sup>ation, lower investment, upward pressure on wage levels, higher unemployment, reduced tax revenues, increases in budget de<sup>fi</sup>cits, higher interest rates, and downward pressure on exchange rates. Net oil-exporting countries may experience those economic phenomena in the opposite way. An increase in the oil price can directly boost the real national income of net oil-exporting countries because of the higher earnings they will get from exports, which may eventually lead to greater concentration of international assets. Over the longer term, part of this gain may be later offset by losses from the lower demand for exports due to the economic recession propagated by trading partners. The bigger the crude oil price increase and the longer higher prices are sustained, the bigger the impact on the global economy.

The overall mechanism by which the oil price affects most global or national economic factors is generally well understood, and therefore forecasting the oil price has been perceived as an important research topic. One of the most commonly used approaches to oil price prediction is the statistical time-series method [20,28], which characterizes the oil price as consisting of a time trend, a seasonal factor, a cyclical element and an error term. Many techniques are available to break up a series of oil prices into these components. They include Akarca and Andrianacos' autoregressive integrated moving average (ARIMA) model [2], Lanza et al.'s error correction model (ECM) [21], and Mirmirani and Li's vector auto-regression (VAR) model [24]. Other kinds of approach assume that stochastically quantifying the relationship between the oil price and the latent economic factors may provide more relevant prediction than attempting to uncover the underlying structure of the series itself. Such methods include the stochastic, semi-parametric, and wavelet-based methods. Cortazar and Schwartz implemented a stochastic model for oil futures prices [11], Morana suggested a semi-parametric statistical method for short-term forecasting based on the GARCH properties of crude oil price [25], and Youse<sup>fi</sup> et al. applied a wavelet-based technique to predict crude oil prices [39]. Other approaches using data mining or machine learning algorithms have also been applied to oil price prediction problem. Yu et al.'s ensemble learning method, which is based on arti<sup>fi</sup>cial neural network (ANN) [40] and Xie et al.'s support vector machines (SVM) [37].

Despite such attempts, oil price prediction has remained a dif<sup>fi</sup>cult problem due to its complexity and irregularity. The complexity is mainly due the complex interactions of many global and national economic factors. Such in<sup>fl</sup>uences are certainly signi<sup>fi</sup>cant but their magnitude is dif<sup>fi</sup>cult to quantify because the relationship between the oil price and external factors is a complicated network structure which is affected by direct/indirect and repetitive/cyclic in<sup>fl</sup>uences. As regards the approaches mentioned above, most techniques are dif-<sup>fi</sup>cult to use in implementing the network structure. On the other hand, the irregularity is caused by the sudden movement of the oil price as a number of sharp price increases/decreases have occurred in the past. There have been several oil price shocks in 1973, 1978 and 2008, including drastic price collapses in 1986 and 1998 [1]. The price of oil is basically determined by balancing the amount of oil the net oil-exporting countries can supply with the demands of the net importing countries, but the irregularity is caused more by the shocks on the supply-side, which may be political disputes or sudden changes in external economic factors [3,6,12,16,17,34]. In such cases, a precise prediction of the values of the oil price will be dif<sup>fi</sup>cult to obtain. However, a rough prediction of the upward and downward changes of the price can still be helpful for decision making. Some of the approaches mentioned above can predict a binary estimate for the changes. But the prediction will inevitably be incomplete, as a propagation pathway of the irregular impact of the source factor on the oil price is dif<sup>fi</sup>cult to illustrate without explicit network representation on the relationship.

Most recently, a category of machine learning algorithms, known as semi-supervised learning (SSL) has emerged, the main strength of which is that it allows taking advantage of the strengths of both supervised learning and unsupervised learning[10,44]. The primary goal of supervised learning is to build accurate classi<sup>fi</sup>ers or regressors using labeled data. On the other hand, unsupervised learning is usually employed to discover data structure from unlabeled data. In semi-supervised learning, meaningful representation of complicatedly structured data is identi<sup>fi</sup>ed from unlabeled data, and then the decision or regression function is achieved on both labeled and the unlabeled, which is smooth with respect to the underlying geometry. SSL is regarded as a more pragmatic learning scheme since many practical domains are in such situation that there is a large supply of unlabeled data but limited labeled data which can be expensive, dif<sup>fi</sup>cult, and time-consuming to generate. Many related researches have shown validity of SSL in a number of application domains such as spam <sup>fi</sup>ltering[43], document categorization [30], video surveillance [31], text classi<sup>fi</sup>cation [35], text chunking [4], gene expression data classi<sup>fi</sup>cation [5,13], and webpage classi<sup>fi</sup>cation [22], etc. In those literatures, SSL is often compared with the representative models of supervised learning, and shows its superiority over them thanks to its capability of learning from only a few labeled data utilizing a large amount of unlabeled data. There has been a whole spectrum of interesting ideas on how to learn from both labeled and unlabeled data, $\mathrm { e . g . , }$ the expectation-maximization based approach [26], self– training [38], co-training [9], Transductive support vector machines [18], and the graph-based approaches such as graph mincuts [8], harmonic approach [45], and local and global consistency [41], etc. Among several types of SSL algorithms, a graph-based SSL is employed in our study [32,33]. In graph-based SSL, the entities are connected via the similarities between them, and prediction about an entity is made by assessing the propagated in<sup>fl</sup>uence of its neighboring entities through the connections that exist within them.

In this paper, we propose a graph-based SSL approach for predicting upward and downward changes in a series of oil prices. The representation of complicated relations between entities is natural in the SSL learning framework and the propagation of a change in an entity is explicitly elucidated via network structure. By treating the economic factors, including the oil price, as entities of the network, these features of SSL will contribute to resolving the complexity and irregularity of the oil price prediction problem. SSL has been exploited to some extent for assessing the non time-series types of entity, but not for timeseries types. Therefore, the intention here is to exploit this method of representing the relationship between time-series type entities and to then employ SSL to forecast the upward and downward movement of oil prices. The proposed SSL approach will be applied to the crude oil price prediction of West Texas Intermediate (WTI) from January 1992 to June 2008, and will be validated through comparison with an autoregression model, a logistic regression model, an ANN model and an SVM model.

The rest of this paper is organized as follows. Section 2 brie<sup>fl</sup>y introduces the SSL algorithm. Section 3 presents the proposed SSL model for time series prediction. Section 4 provides the experimental results as evaluated with regard to the WTI crude oil prices and compares the proposed model with <sup>fi</sup>ve other representative models. Finally, in Section 5, conclusions will be drawn.

## 2. Semi-supervised learning

In graph-based SSL algorithm, a data point (or entity) $x _ { i } \in R ^ { M } ( i = 1 , \ldots ,$ n) is represented as a node i in a graph (or network), and the relationship between data points is represented by an edge where the connection strength from each node j to each other node i is encoded as $w _ { i j }$ of a similarity matrix W [42]. Fig. 1 presents a graphical representation of SSL.

A weight $w _ { i j }$ can take a binary value (0 or 1) in the simplest case. Often, a Gaussian function of Euclidean distance between points with length scale σ is used to specify connection strength:

$$
\mathrm{w} _ {\mathrm{ij}} = \left\{ \begin{array}{c c} \exp \left(- \frac {\left(\mathrm{x} _ {\mathrm{i}} - \mathrm{x} _ {\mathrm{j}}\right) ^ {\mathrm{T}} \left(\mathrm{x} _ {\mathrm{i}} - \mathrm{x} _ {\mathrm{j}}\right)}{\sigma^ {2}}\right) & \text { if } \mathrm{i} \sim \mathrm{j} \left(^ {\prime} \mathrm{k} ^ {\prime} \text { nearest   neighbors }\right), \\ 0 & \text { otherwise } \end{array} \right.\tag{1}
$$

Usually, an edge i\~j is established when node i is one of k-nearest neighbors of node j or node i is within a certain Euclidean distance $r ,$ $\lVert x _ { i } - x _ { j } \rVert < r .$ . The labeled nodes have labels $y _ { l } { \in } \{ - 1 , 1 \} ( 1 { = } 1 , { \ldots } , L )$ , while the unlabeled nodes have zeros $y _ { u } = 0 ( u = L + 1 , . . . , L + U )$ . The algorithm will output an n-dimensional real-valued vector $f = [ f _ { l } ^ { T } f _ { u } ^ { T } ] ^ { T } = ( f _ { 1 } , \dots , f _ { L } , f _ { L + 1 } ,$ $\ldots f _ { L + U } ) ^ { T }$ which can be thresholded to make label predictions on $f _ { L + 1 } , . . . ,$ $f _ { L + U }$ after learning. It is assumed that (a) f should be close to the given label $\mathrm { y _ { i } }$ in labeled nodes and (b) overall, f should not be too different from its adjacent nodes $f _ { j } .$ One can obtain f by minimizing the following quadratic functional:

![](/api/attachments/TGWXM44Y/fulltext/images/5e5bf45aac89d86d946454f66a60618969b366d2b6b662777748161256ecb4a4.jpg)  
Fig. 1. Graph-based semi-supervised learning (SSL).

$$
\operatorname{Min} _ {\mathrm{f}} (\mathbf {f} - \mathbf {y}) ^ {\mathrm{T}} (\mathbf {f} - \mathbf {y}) + \mu \mathbf {f} ^ {\mathrm{T}} \mathbf {L} \mathbf {f},\tag{2}
$$

where $\mathbf { y } { = } ( \mathbf { y } _ { 1 } { , } . . . , \mathbf { y } _ { 1 } { , } 0 . . . , 0 ) ^ { \mathrm { T } }$ , and the matrix L, called the graph Laplacian, is de<sup>fi</sup>ned as $\mathrm { L } { = } \mathrm { D } { \mathrm { - } } \mathrm { W } , \mathrm { D } { = } \mathrm { d i a g ( d _ { i } ) }$ , and $\begin{array} { r } { \mathsf { d } _ { \mathrm { i } } { = } \sum _ { j } \omega _ { i j } . } \end{array}$ . The <sup>fi</sup>rst term corresponds to the loss function in terms of condition (a), and the second term represents the smoothness of the predicted outputs in terms of condition (b). The parameter μ represents trades between loss and smoothness. The solution to Eq. (2) is obtained as

$$
\mathbf {f} = (\mathrm{I} + \mu \mathrm{L}) ^ {- 1} \mathbf {y},\tag{3}
$$

where I is the identity matrix. The formulation of Eq. (2) and its closedform solution (Eq. (3)) present the SSL classi<sup>fi</sup>cation framework, hence the resulting thresholded value of f is ideally suited to capture the movement of oil prices.

## 3. Proposed method

To apply the graph-based SSL to time series prediction, we propose a method of graph representation for time series data, and a procedure for obtaining predicted values from the graph. For instance, assume that multiple time series are given as the input for the prediction problem of the WTI intermediate oil price of this month: the total amount of Saudi oil production (SAUDI), the surplus ability of OPEC production (OPEC surplus), NYMEX oil future price (NIMEX\_OI), etc. To apply SSL to this problem, the proposed method begins with a re-designed graph as in Fig. 2.

The nodes in the graph represent the time series variables that in-<sup>fl</sup>uence WTI, e.g., demand- and supply-related variables and other external economic indicators (factors). Then the edge between any two nodes i \~ j stands for the similarity of the two sets of time series, represented as $\cdot w _ { i j } \in W$ . The label $\cdot y _ { t } ^ { \cdot }$ on each node presents either ‘up’ $( + 1 )$ ) or ‘down’ (−1) of the time series at time point t. In the graph of Fig. 2, the labels of WTI and SAUDI are not known yet at time point t, and hence are unlabeled. To estimate the label $y _ { t } ,$ the similarity matrix of SSL was calculated at time point t-1, W . Based on this set-up, we explain how to measure the similarity ‘w ’ of a similarity matrix W and how to set the value for label $\mathbf { \dot { y } } .$

## 3.1. Similarity matrix

The design of the similarity matrix W plays a critical part in the aspect of performance when using SSL [10], [44]. In the matrix $W ,$ each element represents how strongly the two nodes are related, with larger elemental value being associated with greater nodal similarity. In the proposed method, the time-series data are transformed into vectors by building technical indicators (TIs) and employing feature extraction techniques to build the similarity matrix. The general process of constructing the similarity matrix is described in Fig. 3.

![](/api/attachments/TGWXM44Y/fulltext/images/10a76d85fc7bf07fe56217532093140b3926aa5399b6e1097dee59e317915e78.jpg)  
Fig. 2. Graph SSL representation for time series prediction.

## 3.1.1. Technical indicator (TI) transformation

TIs are frequently used in <sup>fi</sup>nancial forecasting as they offer the advantages of removing the noise (oscillatory noise) inherent in time series and illustrating the underlying structure, $\mathrm { i . e . , }$ the tendencies and structural factors affecting variation. Oil prices and other economic factors exist as time series data by the nature of the variables, and each of them is de<sup>fi</sup>ned as a sequence as

$$
\pmb {X} _ {t} = \{\pmb {x} _ {1}, \pmb {x} _ {2}, \dots , \pmb {x} _ {i}, \dots , \pmb {x} _ {t} \},\tag{4}
$$

where t represents the current time point, and $x _ { t }$ is the corresponding value. The existence o $\mathrm { \ddot { X } _ { t } }$ as time series data induces several problems in the direct application of SSL to the data. As shown in Fig. 2, each of the nodes on the graph has its own time series, as shown in (4). For instance, the WTI node has $\mathsf { X } _ { \mathrm { t } } ^ { \mathsf { W T I } }$ and the SAUDI node also has $\mathrm { \dot { X } _ { t } ^ { \dot { S } A U D I } }$

The problem is that it is dif<sup>fi</sup>cult to draw the similarity between them directly from the two sets of time-series data. Therefore, individual time series are transformed into structural characteristics of time point t, i.e., $S _ { t } ^ { W T I }$ and $S _ { t } ^ { S A U D I }$ , representing the trends and variations of individual series. Table 1 summarizes the TIs used in this study. The similarity between the two nodes is measured by using the seven-tuple vector $S _ { t } { = } \{ s _ { 1 } { , } s _ { 2 } { , } s _ { 3 } { , } s _ { 4 } { , } s _ { 5 } { , } s _ { 6 } { , } s _ { 7 } \}$ composed of MA, BIAS, OSC, ROC, K, D, and RSI.

Using the TIs enables the time-series data to be transformed into vector-type data, while maintaining the time associations of the series, and thus eases their application to SSL. Each indicator has parameters, denoted as p or q as shown in Table 1, which must be decided by the user. However, since there is no rule for deciding appropriate parameter values, the decisions are generally made through trial-and-error. Another alternative is to consider all the diverse values of the parameters. In such a case, however, one indicator will be increased to as many variables as the number of combinations of the parameters, $p { = } 1 , . . . , m$ and $q = 1 , . . . , r ,$ so that the resulting vector will be represented as $S _ { t } = \{ s _ { 1 } ^ { 1 } , . . . , s _ { 1 } ^ { \mathrm { m } } , s _ { 2 } ^ { 1 } , . . . , s _ { 2 } ^ { \mathrm { m } } , s _ { 3 } ^ { 1 , 1 } , . . . , s _ { 3 } ^ { \mathrm { m , r } } , . . . , s _ { 7 } ^ { 1 } , . . . , s _ { 7 } ^ { \mathrm { m } } \}$ This may increase the dimensions of input variables, thereby inducing the curse of dimensionality and possibly causing model over-<sup>fi</sup>tting. Therefore, the next section introduces a method that uses all the diverse parameter values while reducing the unnecessary dimensions derived from the TI parameters.

## 3.1.2. Feature extraction

Feature extraction refers to the process of determining a mapping procedure that reduces the dimensionality and removes the noise effect from the data. Among the various methods for feature extraction, the linear method of principal component analysis (PCA) is the most common. By calculating the eigenvectors of the covariance matrix of original data, PCA transforms a high-dimensional input vector into a low-dimensional one whose components (extracted features) are uncorrelated. On the other hand, among the several kinds of nonlinear PCA (NLPCA), auto-associative neural network (AANN) is one of the well known nonlinear transformation methods. In AANN, the network is trained to perform identity mapping where the values of input features are approximated at the output layer, and the nonlinear principal components can be obtained from the hidden nodes in the bottleneck layer.

![](/api/attachments/TGWXM44Y/fulltext/images/62d8239a492cb6a111e4b3bc637f462b9aa64ede6f1fcdca95d31697fe7b3f96.jpg)  
Fig. 3. Constructing the similarity matrix.

The de<sup>fi</sup>nition of technical indicators (TIs).

<table><tr><td></td><td>TIs</td><td>Meaning</td></tr><tr><td> $s_1$ </td><td> $MA_p(X_t) = \frac{1}{p}(X_t) + \frac{p-1}{p}MA_p(X_{t-1})$ </td><td>p-moving average (exponential smoothing)</td></tr><tr><td> $s_2$ </td><td> $BIAS_p(X_t) = \frac{x_t - MA_p(X_t)}{MA_p(X_t)}$ </td><td>The change rate of  $x_t$  relative to  $MA_p(X_t)$ </td></tr><tr><td> $s_3$ </td><td> $OSC_{p,q}(X_t) = \frac{MA_p(X_t) - MA_q(X_t)}{MA_p(X_t)}$ </td><td>The change rate of  $MA_q(X_t)$  relative to  $MA_p(X_t)$ </td></tr><tr><td> $s_4$ </td><td> $ROC_p(X_t) = \frac{x_t - x_{t-p}}{x_t}$ </td><td>The relative rate of change for  $X_t$  between p consecutive time points</td></tr><tr><td> $s_5$ </td><td> $K_t^p = \frac{x_t - Min_{i=t-p-1}^t(x_i)}{Max_{i=t-p-1}^t(x_i) - Min_{i=t-p-t}^t(x_i)}$ </td><td>Standardization of  $x_t$ </td></tr><tr><td> $s_6$ </td><td> $D_t^p = MA_3(K_t^p)$ </td><td>3-moving average of  $K_t^p$ </td></tr><tr><td> $s_7$ </td><td> $RSI_t^p = \frac{\sum_{i=t-p-1}^t (x_i - x_{i-1})}{\sum_{i=t-p-t}^t (x_i - x_{i-1})},$ </td><td>The relative strength index.</td></tr></table>

3.1.2.1. Principal component analysis (PCA). PCA can be used for dimensionality reduction in a data set by extracting important hidden features that provide the greatest contribution to its variance. Technically, PCA attempts to <sup>fi</sup>nd orthonormal axes which maximally decorrelate the original features of data. Given the data points $\mathsf { s } _ { \mathrm { i } } \in \mathsf { R } ^ { \mathrm { m } } ( \mathrm { i } = 1 , . . . , \mathsf { n }$ and $\Sigma _ { \mathrm { i } = 1 } ^ { \mathrm { n } } \ s _ { \mathrm { i } } { = } 1$ 1,usually mbn), PCA carries out linear transformation of each s<sub>i</sub> into a new one $Z _ { \mathrm { i } }$ by

$$
\underbrace {Z _ {i}} _ {m \times 1} = \underbrace {U ^ {T}} _ {m \times m} \underbrace {s _ {i}} _ {m \times 1}, i = 1, \dots , n,\tag{5}
$$

where U is the m×m orthogonal matrix whose $k ^ { \mathrm { { t h } } }$ column $\mathrm { u _ { k } }$ is the $k ^ { \mathrm { { f h } } }$ eigenvector of the covariance matrix $\begin{array} { r } { C = \frac { 1 } { n } \sum _ { i = 1 } ^ { n } s _ { i } s _ { i } ^ { T } } \end{array}$ . The matrix U can <sup>¼ ¼</sup>be obtained by solving the eigenvalue problem with respect to C,

$$
\lambda_ {k} u _ {k} = C u _ {k}, \quad k = 1, \dots , m,\tag{6}
$$

where $\lambda _ { k }$ is an eigenvalue of C and $\mathrm { u _ { k } }$ is the corresponding eigenvector. The magnitude of an eigenvalue stands for the proportion of variance that can be explained by the corresponding eigenvector. Therefore, by taking the <sup>fi</sup>rst $p$ largest eigenvectors $\tilde { U } ^ { T } { = } \{ u _ { 1 } , u _ { 2 } { , } { \ldots } , u _ { p } \}$ we can <sup>fi</sup>nd “lower” dimensional orthonormal space while still retaining most important aspects of the data. A projected data point onto the lower dimensional space, ${ \tilde { s } } _ { i } ,$ is calculated as the orthogonal transformations of $S _ { \mathrm { i } } ,$

$$
\underbrace {\tilde {s} _ {i}} _ {p \times 1} = \underbrace {\tilde {U} ^ {T}} _ {p \times m} \underbrace {s _ {i}} _ {m \times 1}, i = 1, \dots , n.\tag{7}
$$

Although PCA is a well established dimensionality reduction method, its applicability is limited by the assumption that the data is a linear combination of certain features. Therefore, if the data set shows non-linear relationship among features, there is no guarantee that the extracted features by PCA will contain all important features.

3.1.2.2. Nonlinear principal component analysis (NLPCA): auto-associative neural network (AANN). Another approach to dimensionality reduction is through the use of an AANN, a special kind of feed-forward neural network [19]. AANN attempts to <sup>fi</sup>nd and eliminate nonlinear correlations in the data. Similar to PCA, it can be used to reduce the dimensionality of data by removing redundant features. The general structure of AANN, as shown in $\mathrm { F i g . }$ . 4, consists of an input layer, an output layer, and multiple hidden layers. Both the number of input nodes and that of output nodes are equally set to m. Among the hidden layers, the mapping layer models the mapping function (F1) and the demapping layer models the demapping function (F2). The number of nodes, $p ,$ in a particular hidden layer, the so called “bottleneck layer”, is set to be less than the number of nodes in the input/output layer $\scriptstyle ( p < m )$ . In auto-associative mapping, the target data is set to be identical to the input data. This “identity mapping” creates a global reduction of the data dimensionality while the input data goes through the bottleneck layer before appearing at the output layer. Let F denote the auto-associative mapping learnt by the network. $\operatorname { I f } { \biggl \{ } { \tilde { \mathsf { s } } } _ { 1 } , { \tilde { \mathsf { s } } } _ { 2 } , . . . , { \tilde { \mathsf { s } } } _ { \mathrm { n } } { \biggr \} }$ is the set of output data produced by the AANN when the input data set $\{ s _ { 1 } , s _ { 2 } , . . . , s _ { \mathrm { n } } \}$ is given, then F can be found which minimizes the mean square error,

$$
E = \sum_ {i = 1} ^ {n} \left(s _ {i} - \tilde {s} _ {i}\right) ^ {T} \left(s _ {i} - \tilde {s} _ {i}\right) = \sum_ {i = 1} ^ {n} \left(s _ {i} - F (s _ {i})\right) ^ {T} \left(x _ {i} - F (s _ {i})\right).\tag{8}
$$

The mapping function F can be separated into $F _ { 1 }$ and $F _ { 2 } ,$ so that $\operatorname { F } ( . ) =$ $F _ { 2 } ( F _ { 1 } ( . ) )$ , where $F _ { 1 }$ is the transformation in the network from the input layer into the dimension compressing the hidden layer (the bottleneck layer), and $F _ { 2 }$ is the transformation from the bottleneck layer into the output layer. To summarize, the data are <sup>fi</sup>rst compressed to lower the dimensionality and then reconstructed. The mapping from the input layer to the bottleneck layer can be regarded as a “nonlinear” projection onto the lower dimensional space $( \mathsf { m } \to \mathsf { p } )$ , and each node in the bottleneck can be considered as an extracted feature retaining signi<sup>fi</sup>cant information of the data. New data $\tilde { \mathsf { s } } _ { \mathrm { i } }$ is then calculated as

$$
\underbrace {\tilde {s} _ {i}} _ {p \times 1} = F _ {1} \underbrace {(s _ {i})} _ {m \times 1}.\tag{9}
$$

AANN is a good model to extract the variables that can well express the nonlinear relationship of data if its structure is well established. However, since AANN is not a method in which the number of the nodes of the bottleneck layer is determined from the beginning, its need to be determined by the users in accordance with the situation introduces signi<sup>fi</sup>cant dif<sup>fi</sup>culty.

## 3.2. Label

The label on the node in the SSL graph in Fig. 2 is designed to explain whether the predicted value of the corresponding variable is up or down. It can be formulated as follows:

$$
\mathrm{y} _ {\mathrm{t}} = \operatorname{sign} \left(\mathrm{x} _ {\mathrm{t}} - \mathrm{MA} _ {3} \left(\mathrm{x} _ {\mathrm{t}}\right)\right).\tag{10}
$$

For instance, if the total amount of SAUDI oil production of this month (t) exceeds its three-month moving average, Eq. (10) will give a $\mathbf { \dot { y } _ { t } } = + \mathbf { \boldsymbol { 1 } } \mathbf { \dot { \xi } }$ ’ label. On the contrary, the node is labeled as $\mathsf { y } _ { \mathrm { t } } = - 1 ^ { \prime }$ for the opposite case. And $\mathsf { y } _ { \mathrm { t } } = 0 ^ { \prime }$ if there is no information about the movement of the corresponding time-series value at time point t; the label is to be predicted. In the proposed method, we set the label of the target variable, WTI spot prices, to ‘0’. Also note that some of input variables may not be able to be labeled, for instance, SAUDI in Fig. 2, but SSL produces a prediction even for such a node.

Given label $\mathrm { y } _ { \mathrm { t } } ,$ Eq. (3) provides the predicted value $\mathrm { f _ { t } }$ for every node, which can take on a real number unlike the values of label $\mathrm { y } _ { \mathrm { t } } .$ The following interpretation can be put on the predicted value. At time point t, if the predicted value f is an arbitrary positive number, then it is equivalent in sign with the value of $\left( \mathbf { X } _ { \mathrm { t } } - \mathbf { M } \mathbf { A } _ { 3 } ( \mathbf { x } _ { \mathrm { t } } ) \right)$ . This means that $\mathbf { X _ { t } } ,$ i.e., the WTI oil price for time point t will exceed the price of the past three-month moving average. To rephrase this

![](/api/attachments/TGWXM44Y/fulltext/images/285b3e9e3cd83c001567b7cdfcaca5bf6a074cca1e47f94514362376d19eae25.jpg)  
Fig. 4. Architecture of AANN

$$
\operatorname{sign} \left(\mathrm{f} _ {\mathrm{t}}\right) > 0 \Longleftrightarrow \operatorname{sign} \left(\mathrm{x} _ {\mathrm{t}} - \mathrm{MA} _ {3} \left(\mathrm{x} _ {\mathrm{t}}\right)\right) > 0\tag{11}
$$

and thus, the following inequality holds:

$$
\mathrm{x} _ {\mathrm{t}} > \mathrm{MA} _ {3} (\mathrm{x} _ {\mathrm{t}}).\tag{12}
$$

To substitute the right-hand side of the inequality with the de<sup>fi</sup>nition of the moving average equation in Table 1, the following inequality is derived

$$
\mathrm{x} _ {\mathrm{t}} > \frac {1}{3} \mathrm{x} _ {\mathrm{t}} + \frac {3 - 1}{3} \mathrm{MA} _ {3} (\mathrm{x} _ {\mathrm{t} - 1}),
$$

and summarized as the <sup>fi</sup>nal form below.

$$
\mathrm{x} _ {\mathrm{t}} > \mathrm{MA} _ {3} (\mathrm{x} _ {\mathrm{t-1}})\tag{13}
$$

That is, since $\mathbf { \sigma } \cdot \mathbf { f } _ { \mathrm { t } } > 0 ^ { \prime }$ actually means ${ \bf X } _ { \mathrm { t } } { > } \mathrm { M A } _ { 3 } ( { \bf X } _ { \mathrm { t } - 1 } ) ,$ , this implies that ‘one-time-point-ahead prediction’ is available with the predicted value $\mathrm { f _ { t } }$ and $\mathrm { M A } _ { 3 } ( \mathbf { X } _ { \mathrm { f } - 1 } )$ at time point t-1. This procedure is schematized as shown in Fig. 5.

## 4. Experiment

In this section, we implement the proposed method on the prediction of price movement of West Texas Intermediate crude oil. As aforementioned in the earlier sections, a set of multiple time series data is described using a network (or a graph) to capture the multiple interactions included and prediction is made using SSL. Since the construction procedure of the network employs TI transformation which increases dimensionality, feature extraction is implemented through alternative approaches of PCA and NLPCA. Depending on the number of extracted features, many models are possible, and therefore the best model is determined by performance comparison using a measure known as the area under the ROC curve (AUC). Finally, comparison with other representative data mining models is made of the best SSL model determined previously.

## 4.1. Data

The data employed in this study are the time-series data of the prices of the WTI crude oil which consist of 198 monthly spot prices ranging from January 1992 to June 2008 as shown in Fig. 6.

For the same span, the Korea Energy Economics Institute (KEEI) made available the 25 diverse external economic factors (time series variables) that are strongly related to the WTI oil price screened by the domain experts, e.g., demand- and supply-related variables and other external economic indicators. The demand-related variables include the amount of overall international oil production, the amount of OPEC oil production, and the amount of SAUDI oil production. The supply-related variables include the amount of overall international demand, the amount of OECD countries' oil demand, and the amount of non-OECD countries' oil demand. Other economic indicators include the producer price indices and the US dollar exchange rates. We tested the association of those 25 input variables with the WTI oil price in the continuous scale with R<sup>2</sup> improvement values at the signi<sup>fi</sup>cance level of $\alpha = 0 . 0 1$ in order to reject the insigni<sup>fi</sup>cant ones [29]. But all of the given 25 variables showed statistical signi<sup>fi</sup>cance, and hence employed all as input variables in our study. The variables are tabulated in Table 2. Among them, WTI is the target variable and so regarded as unlabeled. Fig. 7 shows how the 25 external economic factors used as input variables affect WTI. Notably, input variables not only affect WTI but also affect each other in a very complicated manner.

![](/api/attachments/TGWXM44Y/fulltext/images/a0859bad319923e3dcfbabffc457e42f1ef04f774937fad40e655546ba02d359.jpg)  
Fig. 5. Schematic description of interpreting forecasted values (when f >0).

Table 2  
![](/api/attachments/TGWXM44Y/fulltext/images/8dc5cd76686d6b494643073c14759672e87edd334e1b1751d03a7c335ec7bccc.jpg)  
Fig. 6. The monthly WTI crude oil prices from Jan. 1992 to Jun. 2008.

The data set used in the experiment was set up as follows. The <sup>fi</sup>rst 100 monthly data values for January 1993 through April 2001 were used as a training data set. The remaining 86 monthly data values for May 2001 through June 2008 were used as a test set (of the 198 time points in total, 12 time points necessary to create TIs were excluded) for performance comparison with competing models.

The 26 sets of time-series data from January 1992 to June 2008.

<table><tr><td colspan="2">Target variable</td><td colspan="2">West Texas intermediate crude oil prices (WTI)</td></tr><tr><td rowspan="2" colspan="2">Input variables</td><td colspan="2">Association with target variable</td></tr><tr><td> $R^2$ </td><td>p-value</td></tr><tr><td rowspan="5">Demand-side</td><td>Overall amount of world oil demand</td><td>0.941</td><td> $1.12×10^{-41}$ </td></tr><tr><td>Amount of OECD demand</td><td>0.373</td><td> $1.22×10^{-12}$ </td></tr><tr><td>Non-OECD demand</td><td>0.605</td><td> $3.86×10^{-65}$ </td></tr><tr><td>China demand</td><td>0.227</td><td> $6.83×10^{-59}$ </td></tr><tr><td>USA demand</td><td>0.365</td><td> $3.32×10^{-21}$ </td></tr><tr><td rowspan="9">Supply-side</td><td>OPEC production</td><td>0.773</td><td> $3.49×10^{-59}$ </td></tr><tr><td>Saudi production</td><td>0.736</td><td> $1.67×10^{-39}$ </td></tr><tr><td>Iran production</td><td>0.630</td><td> $2.33×10^{-40}$ </td></tr><tr><td>Iraq production</td><td>0.738</td><td> $1.02×10^{-8}$ </td></tr><tr><td>Kuwait production</td><td>0.585</td><td> $2.32×10^{-30}$ </td></tr><tr><td>Non-OPEC production</td><td>0.593</td><td> $6.57×10^{-29}$ </td></tr><tr><td>USA production</td><td>0.554</td><td> $5.57×10^{-5}$ </td></tr><tr><td>Russia production</td><td>0.487</td><td> $2.67×10^{-48}$ </td></tr><tr><td>World production</td><td>0.469</td><td> $2.23×10^{-44}$ </td></tr><tr><td rowspan="11">Other economic indicators</td><td>Producer price index</td><td>0.259</td><td> $2.98×10^{-12}$ </td></tr><tr><td>U.S. exchange rate</td><td>0.663</td><td> $8.64×10^{-22}$ </td></tr><tr><td>OECD commercial stockpiles</td><td>0.669</td><td> $4.83×10^{-15}$ </td></tr><tr><td>U.S. commercial stockpiles for crude oil</td><td>0.326</td><td> $5.44×10^{-5}$ </td></tr><tr><td>U.S. commercial stockpiles for oil</td><td>0.319</td><td> $2.29×10^{-5}$ </td></tr><tr><td>OPEC surplus production ability</td><td>0.206</td><td> $1.66×10^{-11}$ </td></tr><tr><td>NYMEX oil futures price</td><td>0.824</td><td> $2.37×10^{-76}$ </td></tr><tr><td>Non-commercial real purchase (short)</td><td>0.133</td><td> $1.03×10^{-4}$ </td></tr><tr><td>Non-commercial real purchase (long)</td><td>0.194</td><td> $7.48×10^{-11}$ </td></tr><tr><td>Commercial volume (short)</td><td>0.048</td><td> $1.91×10^{-4}$ </td></tr><tr><td>Commercial volume (long)</td><td>0.031</td><td> $1.30×10^{-4}$ </td></tr></table>

## 4.2. Performance measure (AUC)

To measure the prediction performance, the area under the curve (AUC), which is de<sup>fi</sup>ned as the area under the receiver operating characteristic (ROC) curve, is used [14,15]. The ROC curve plots true positive rate as a function of false positive rate for differing classi<sup>fi</sup>cation thresholds as shown in Fig. 8. The AUC measures the overall quality of the ranking induced by model rather than the quality of a single value of threshold in that ranking. The closer the curve follows the left-hand border and then the top-border of the ROC space, the larger value of AUC the model produces; i.e., the more accurate the model is.

## 4.3. SSL parameter selection

The parameter values of the SSL model, k and μ, the number of k-nearest neighbors in (1) and the loss-smoothness tradeoff in (3) were selected from $\{ \mathrm { k } , \mu \} \in \{ 2 , 3 , 4 , 5 \} \times \{ 0 . 0 1 , 0 . 1 , 0 . 3 , 0 . 5 , 0 . 7 , 1 , 1 0 , 1 0 0 \}$ as optimum combinations through cross-validations. Fig. 9 illustrates a typical pattern of how the AUC performance of an SSL model would vary depending on the combinations of parameters k and μ. Every SSL model in this study found its model-parameters at its best AUC, for instance, the model in Fig. 9 set the values of (k, μ) to (2, 0.1).

## 4.4. Results on TI transformation and feature extraction

As shown in Section 3.1.1, each of the 26 variables is transformed into the seven TIs: MA, BIAS, OSC, ROC, K, D or RSI. The parameters for each TI are set as $\mathfrak { p } \in \{ 3 , 4 , 6 , 8 , 9 , 1 2 \}$ . Since a single variable is transformed to 7 TIs, and each of which has 6 dependent sub-variables, then the total number of the sub-variables per variable, or simply input dimensionality, becomes 42 (=7 TIs×6 parameter dependent sub-variables). Even though the use of TI facilitates the consideration of the trends and the structure of the data, there is, on the other hand, the drawback that one variable turns into a set of an increased number of sub-variables. The increased number of input variables means an increase in dimensionality, which degrades the performance of the prediction model. Thus, as mentioned in Section 3.1.2, feature extraction techniques are employed: PCA and NLPCA. If we extract a single feature per TI, then the 6 parameter dependent sub-variables are reduced to one dimensional feature. For PCA, this implies that we use only the <sup>fi</sup>rst principal component from the covariance matrix of the 6 parameter dependent sub-variables. For NLPCA, the network con<sup>fi</sup>guration is composed of 6 input nodes in the input layer, 1 hidden node in the bottleneck layer, and 6 output nodes in the output layer (See the architecture of AANN in Fig. 4). During the network training, the values of the 6 parameter dependent sub-variables are fed to the network as both input and target.

![](/api/attachments/TGWXM44Y/fulltext/images/74b9fdc4243f846cdc49df46cb31c76cfdb6f40afb79f8d3afd6d5fa0c71333f.jpg)  
Fig. 7. The SSL graph for the 26 sets of time-series variables: WTI is the target variable and the remaining economic factors are input variables. The edge between two nodes represents the similarity between them.

After training, the output value of the bottleneck node is used as the extracted feature. Fig. 10 shows the procedure of feature extraction following TI transformation from a variable, SAUDI.

This process is similarly applied to all of the 26 variables. Then a node in the graph which corresponds to a variable is represented as a vector of 7 tuples, e.g., $\mathsf { S } ^ { \mathsf { S A U D I } } = ( s _ { 1 } ^ { \mathsf { S A U D I } } , s _ { 2 } ^ { \mathsf { S A U D I } } , s _ { 3 } ^ { \mathsf { S A U D I } } , s _ { 4 } ^ { \mathsf { S A U D I } } , s _ { 5 } ^ { \mathsf { S A U D I } } ,$ $s _ { 6 } ^ { \mathrm { S A U D I } } , s _ { 7 } ^ { \mathrm { S A U D I } } )$ . The similarity (edge-connection) between the nodes is built from (1). Fig. 11 exempli<sup>fi</sup>es how the connections between the 26 variables are made from 7-tuple vector-representation. The size of vector can vary depending on how many features are extracted. If we set the number of extracted features to three, then a variable is represented as a vector of 21 tuples, ${ \sf S } = ( { \sf s } _ { 1 1 } , { \sf s } _ { 1 2 } , { \sf s } _ { 1 3 } ,$ s<sub>21</sub>, $\begin{array} { r } { { 5 _ { 2 2 } } , \dotsc , { 5 _ { 2 3 } } , \dotsc , { 5 _ { 5 1 } } , \dotsc , { 5 _ { 5 3 } } , \dotsc , { 5 _ { 7 1 } } , { 5 _ { 7 2 } } , { 5 _ { 7 3 } } \dotsc } \end{array}$ . However, it is dif<sup>fi</sup>cult to determine the number of extracted features when the intrinsic dimension is unknown. In the experiment, we attempted to <sup>fi</sup>nd the optimum number of extracted features among 1, 3 and $6 ,$ which respectively led to 7, 21 and 42 input dimensionality per variable (=7 TIs×{1, 3, 6} features extracted from 6 parameter dependent sub-variables).

![](/api/attachments/TGWXM44Y/fulltext/images/7d70bb6ec3f80065bc6e99fa69c63be2e0f82f1251775b7ac941a5e2457ed902.jpg)  
Fig. 8. ROC curve.

In the following Fig. 12 and Table 3, the AUC values of the seven SSL models are compared: $\mathrm { S S L _ { 0 } , S S L _ { P 1 } , S S L _ { P 3 } , S S L _ { P 6 } , S S L _ { N 1 } , S S L _ { N 3 } }$ and ${ \mathsf { S S L } } _ { \mathrm { N 6 } } .$ The designations were determined based on whether PCA or NLPCA was used and the number of extracted features. For instance, ${ \sf S S L _ { P 3 } }$ means a model made by extracting three features per TI through PCA and then applying SSL. The input dimensionality is 21 (=7 TIs×1 extracted feature). Likewise, ${ \mathsf { S S L } } _ { \mathrm { N 3 } }$ is a model made by extracting three features through NLPCA. The model designated as ${ \mathsf { S S L } } _ { 0 }$ refers to a model without the feature extraction procedure, therefore 6 sub-variables per TI are all used. The input dimensionality of SSL is $4 2 ~ ( = 7 ~ \mathrm { T I s } \times 6$ parameter dependent sub-variables).

The average AUC of SSL using 42 sub-variables is 0.84. A notable fact is that ${ \mathrm { S S L } } _ { \mathrm { P 1 } }$ almost reproduces the performance ${ \tt o f S S L } _ { 0 }$ with only 7 features with the average AUC of 0.83. Overall, the performances of the ${ \mathrm { S S L } } _ { \mathrm { P } }$ models are similar to the performance of the ${ \mathsf { S S L } } _ { 0 }$ models. The performances of the $\mathrm { { S S L } _ { N } }$ tend to be somewhat inferior. The results that the ${ \mathrm { S S L } } _ { \mathrm { P } }$ models are better performed than the $\mathrm { S S L _ { N } }$ models give us a hint that the 6 parameter dependent variables would be rather linearly correlated since they are derived from an identical TI formula, e.g. $\mathsf { M A } ( \mathsf { p } )$ where $\mathsf { p } = \{ 3 , 4 , 6 , 8 , 9 , 1 2 \}$ , and also see Fig. 10. Among the SSL models, ${ \sf S S L } _ { \mathrm { P 3 } }$ shows the best performance with an average AUC of 0.86. The optimum number of extracted features is usually determined by a trial-and-error fashion. However, related to our experimental setting for the number of extracted features {1, 3, 6}, we may conjecture that a single feature would not be suf<sup>fi</sup>cient to explain the variability among the 6 parameter dependent variables whereas 6 features would just reconstruct the original input space into the feature space without the effect of dimensionality reduction and thus no effect of noise reduction. Using 3 extracted features would be a compromise between both ends. To summarize, if feature extraction is used, performances similar or superior to the original performance can be expected even with smaller numbers of variables and, in particular, PCA was more effective than NLPCA in our experiment.

![](/api/attachments/TGWXM44Y/fulltext/images/53aa06598448a7d2bb1efc076f279acc6f62f8465b16a06741c78963298ea6f8.jpg)  
Fig. 9. The AUC over model-parameters variation (k and μ) using the SSL model.

![](/api/attachments/TGWXM44Y/fulltext/images/881e836af0fe8e7b358720b1f4d33f0767f7c3ad31eedb3dcdd6a5fc99dbce3a.jpg)  
Fig. 10. The procedure of feature extraction following TI transformation

## 4.5. Results of the comparison: SSL vs. other models

In this experiment, ${ \sf S S L } _ { \mathbb { P } 3 }$ was compared with <sup>fi</sup>ve well known representative models: an auto-regression (AR) model, a logistic regression (LR) model, an ANN model, and two SVM models, $\mathsf { S V M \_ R B F }$ and $\mathrm { S V M \_ p o L Y }$ using RBF kernel function and polynomial kernel function, respectively.

The optimum model parameters were selected for each of the <sup>fi</sup>ve models in Section 4.2 in a similar way to that done for SSL. The resultant AUC values of the six models are summarized in Table 4 and Fig. 13. First, AR and LR showed average AUC values of 0.53 and 0.55, respectively, which are much smaller than the AUC average of 0.86 for the proposed $\mathrm { S S L } _ { \mathrm { P 3 } } .$ This indicates that the time-series models, based on existing linear models, have limitations in explaining the irregular patterns of oil price movement. Although ANN and SVM showed average AUC values of 0.74 and 0.66, respectively, which indicated their superior accuracy compared to that of AR and the LR, they showed relatively poor results compared to ${ \mathrm { S S L } } _ { \mathrm { P 3 } } .$ The superior generalization ability of SSL compared to that of ANN and SVM was attributed to the fact that SSL uses not only one-to-one relationships between the target variable WTI and the input variables (demands, supplies and other external economic factors) but also the intrinsic inter-relationships between the input variables. This enabled the SSL to perform more accurately than others. Fig. 14 presents how ${ \mathrm { S S L } } _ { \mathrm { P 3 } }$ <sup>fi</sup>ts the ups and downs of the WTI oil prices during the test period of May 2001 through June 2008. The thicker line indicates the WTI oil prices and the thinner line its three-month moving average, i.e., $\mathrm { M A } _ { 3 } ( \mathrm { W I I } )$ . The <sup>fi</sup>gure shows that the predicted value <sup>fi</sup>ts the ups and downs of the price movement reasonably well.

## 5. Conclusions

This paper has proposed a novel method for oil price prediction using the SSL algorithm. The proposed method modi<sup>fi</sup>es the existing

![](/api/attachments/TGWXM44Y/fulltext/images/6dbfaa57634e8e4fe9c5633d277cf6599a0a91c6eecc62a9734cdec2158bdc1c.jpg)  
Fig. 11. Similarity (edge-connection) calculation from 7-tuple vector-representation.

SSL algorithm for application to time-series prediction, including measuring the similarity between different sets of time-series data and the labels of pricing ups and downs, and the advanced techniques using TI transformation and feature extraction. The advantages of the proposed method can be summarized as follows. First, the modi<sup>fi</sup>ed SSL considers not only the in<sup>fl</sup>uence of input variables on the target variable but also the mutual in<sup>fl</sup>uences among the input variables. For our oil price prediction problem, the WTI crude oil prices were predicted by taking into account the in<sup>fl</sup>uence of external economic factors such as demand-side factors, supply-side factors, and various types of international economic index. The economic factors including the oil price were represented as nodes in a network, and connected via similarities between them. Then prediction on the WTI crude oil price was made by the propagated in<sup>fl</sup>uence of its neighboring economic factors through the connections. This enables to resolve the complexity and irregularity of oil price prediction problem caused by its intrinsic dynamics interacting with many global or national economic factors, and results in more accurate prediction than that offered by the existing representative prediction models. Second, by transforming time-series data into TIs, the noise in the data was removed and the underlying tendencies and structural factors for the variations were revealed. Third, by using feature extraction, only the few features that are commonly intrinsic among input variables were used in the modeling, which avoided any unnecessary increases of the input dimensionality. The synergy effect of these three advantages were harmonized in our SSL model-based oil price prediction, and afforded an AUC accuracy of 0.86, which is an unprecedented performance. The proposed method is expected to be applied to any domain that requires time-series prediction, i.e., the prediction of international oil prices, domestic/foreign stock price indices, price variability, national growth rates and currency exchange rates. Technically, the proposed method can be more sophisticated with respect to feature extraction procedure. PCA/NLPCA can be replaced with independent component analysis (ICA) as in [23], and a combining approach of multiple features can be an alternative of choosing one of them [36]. Applying and adapting our method to diverse domains and techniques will be well worth further research.

![](/api/attachments/TGWXM44Y/fulltext/images/80efbb8b90aff81e10dc2b62a32dae09500a58c9f029b3e5e02bb8aab8d63ad3.jpg)  
Fig. 12. Comparison of AUC for seven different SSL models. The numbers under the graph stand for the number of the extracted features through PCA or NLPCA. The squares indicate the best AUC after repetition of experiments under every combination of parameters {k,μ}, the circles indicate the average AUC and the triangles indicate the minimum AUC.

Table 3  
AUCs summary for seven different SSL models

<table><tr><td>AUC</td><td>Max</td><td>Avg</td><td>Min</td></tr><tr><td> $SSL_0$ </td><td>0.86</td><td>0.84</td><td>0.76</td></tr><tr><td> $SSL_{P1}$ </td><td>0.85</td><td>0.83</td><td>0.77</td></tr><tr><td> $SSL_{P3}$ </td><td>0.88</td><td>0.86</td><td>0.77</td></tr><tr><td> $SSL_{P6}$ </td><td>0.86</td><td>0.85</td><td>0.77</td></tr><tr><td> $SSL_{N1}$ </td><td>0.84</td><td>0.83</td><td>0.81</td></tr><tr><td> $SSL_{N3}$ </td><td>0.82</td><td>0.80</td><td>0.77</td></tr><tr><td> $SSL_{N6}$ </td><td>0.75</td><td>0.74</td><td>0.72</td></tr></table>

Table 4  
AUCs comparison of SSL vs. the <sup>fi</sup>ve competing models.

<table><tr><td>AUC</td><td>Max</td><td>Avg</td><td>Min</td><td>Rank</td></tr><tr><td> $SSL_{P3}$ </td><td>0.88</td><td>0.86</td><td>0.77</td><td>1</td></tr><tr><td>AR</td><td>0.54</td><td>0.53</td><td>0.52</td><td>6</td></tr><tr><td>LR</td><td>0.64</td><td>0.55</td><td>0.49</td><td>5</td></tr><tr><td>ANN</td><td>0.82</td><td>0.74</td><td>0.55</td><td>2</td></tr><tr><td>SVM_RBF</td><td>0.78</td><td>0.73</td><td>0.67</td><td>3</td></tr><tr><td>SVM_POLY</td><td>0.74</td><td>0.58</td><td>0.50</td><td>4</td></tr></table>

![](/api/attachments/TGWXM44Y/fulltext/images/d311bffb4ae2ca5fe427645d67edfe9571baff0308ff193d91d59f465c81a0d3.jpg)  
Fig. 13. Comparison in AUC: SSL versus the <sup>fi</sup>ve competing models.

## Acknowledgment

The authors would like to gratefully acknowledge support from Post Brain Korea 21 and the research grant from National Research Foundation of the Korean Government (2010-0007804/2012-0000994).

![](/api/attachments/TGWXM44Y/fulltext/images/8041b9d47f529ada03f47a69d31698de26a59e5bcb9f2a35e0e28b685c74a062.jpg)  
Fig. 14. SSL for the test period of May 2001 through Jun 2008.

## References

[1] S. Abosedra, H. Baghestani, On the predictive accuracy of crude oil futures prices, Energy Policy 32 (2004) 1389–1393.

[2] A.T. Akarca, D. Andrianacos, Detecting break in oil price series using the Box–Tiao method, International Advances in Economic Research 3 (1997) 217–224.

[3] R.A. Amano, S.V. Norden, Exchange rates and oil prices, Review of International Economics 6 (1998) 683–694.

[4] R.K. Ando, T. Zhang, A High-Performance Semi-Supervised Learning Method for Text Chunking, in: ACL '05 Proceedings of the 43rd Annual Meeting on Association for Computational Linguistics Ann Arbor, Michigan, 2005, pp. 1–9.

[5] E. Bair, R. Tibshirani, Semi-supervised methods to predict patient survival from gene expression data, PLoS Biology 2 (2004) 511–522.

[6] S.A. Basher, P. Sadorsky, Oil price risk and emerging stock markets, Global Finance Journal 17 (2004) 224–251

[7] F. Birol, Analysis of the Impact of High Oil Price on the Global Economy, International Energy Agency, 2004

[8] A. Blum, S. Chawla, Learning from labeled and unlabeled data using graph mincuts, in: ICML '01 Proceedings of the Eighteenth International Conference on Machine Learning San Francisco, 2001, pp. 19–26.

[9] A. Blum, T. Mitchell, Combining labeled and unlabeled data with co-training, in: COLT' 98 Proceedings of the eleventh annual conference on Computational learn ing theory New York, 1998, pp. 92–100.

[10] O. Chapelle, B. Scholkopf, A. Zien, Semi-Supervised Learning Cambridge, MIT Press, England, 2006.

[11] G. Cortazar, E.S. Schwartz, Implementing a stochastic model for oil futures prices, Energy Economics 25 (2003) 215–238.

[12] L. Feng, J. Li, X. Pang, China's oil reserve forecast and analysis based on peak oil models, Energy Policy 36 (2008) 4149–4153.

[13] Y.-C. Gong, C.-L. Chen, Semi-supervised method for gene expression data classi<sup>fi</sup>- cation with Gaussian <sup>fi</sup>elds and harmonic functions, in: 19th International Conference on Pattern Recognition (ICPR 2008), Tampa, FL, 2008, pp. 1–4.

[14] M. Gribskov, N.L. Robinson, The use of receiver operating characteristic (ROC) analysis to evaluate sequence matching, Computers and Chemistry 20 (1996) 25–33.

[15] J.A. Hanley, B.J. McNeil, The meaning and use of the area under a receiver operating characteristic. Radiology 143 (1982) 29–36

[16] L.-Y. He, Y. Fan, Y.-M. Wei, Impact of speculator's expectations of returns and time scales of investment on crude oil price behaviors, Energy Economics 31 (2009) 77–84.

[17] D. Huang, B. Yu, F.J. Fabozzi, M. Fukushima, CAViaR-based forecast for oil price risk, Energy Economics 31 (2009) 511–518.

[18] T. Joachims, Transductive inference for text classi<sup>fi</sup>cation using support vector machines, in: International Conference on Machine Learning, San Francisco, 1999, pp. 200–209.

[19] R.T. Kamimura, S. Bicciato, H. Shimizu, J. Alford, G.N. Stephanopoulos, Mining of multivariate temporal biological data: a framework for the rational design of data-driven models, in: Presented at the BioKDD, 2001: Workshop on Data Mining in Bioinformatics, San Francisco, CA(US), 2001.

[20] T.A. Knetsch, Forecasting the price of crude oil via convenience yield predictions, Journal of Forecasting 26 (2007) 527–549.

[21] A. Lanza, M. Manera, M. Giovannini, Modeling and forecasting cointegrated relationships among heavy oil and product prices, Energy Economics 27 (2005) 831–848.

[22] R. Liu, J. Zhou, M. Liu, A graph-based semi-supervised learning algorithm for web page classi<sup>fi</sup>cation, in: International Conference on Intelligent Systems Design and Applications, China, 2006, pp. 856–860.

[23] C.-J. Lu, T.-S. Lee, C.-C. Chiu, Financial time series forecasting using independent component analysis and support vector regression, Decision Support Systems 47 (2009) 115–125.

[24] S. Mirmirani, H.C. Li, A comparison of VAR and neural networks with genetic algorithm in forecasting price of oil, Applications of Arti<sup>fi</sup>cial Intelligence in Finance and Economics 19 (2004) 203-223.

[25] C. Morana, A semiparametric approach to short-term oil price forecasting, Energy Economics 23 (2001) 325–338

[26] K. Nigam, A.K. Mccallum, S. Thrun, T. Mitchell, Text classication from labeled and unlabeled documents using EM, Machine Learning 39 (1999) 1–34.

[27] J. Philip, K. Verleger, Adjusting to Volatile Energy Prices, Policy Analyses in International Economics Series vol. 39 Peterson Institute, 1994. (ISBN: 0881320692 9780881320695)

[28] SajalGhosh, Import demand of crude oil and economic growth: evidence from India, Energy Policy 37 (2009) 699–702.

[29] K.S. Sarma, Variable selection node, in: Predictive modeling with SAS Enterprise Miner: practical solutions for business, ed Cary, NC, USA: SAS Institute Inc, 2007, pp. 48-50.

[30] H. Shin, K. Tsuda, Prediction of protein function from networks, in: O. Chapelle, et al., (Eds.), Semi-Supervised Learning, MIT Press, 2006, pp. 339–352.

[31] H. Shin, A.M. Lisewski, O. Lichtarge, Graph sharpening plus graph integration: a synergy that improves protein functional classi<sup>fi</sup>cation, Bioinformatics 23 (2007) 3217–3224.

[32] H. Shin, K. Tsuda, B. Schoelkopf, Protein functional class prediction with a combined graph, Expert Systems with Applications 36 (2) (November 2009) 3284–3292.

[33] H. Shin, N.J. Hill, A.M. Lisewski, J.-S. Park, Graph sharpening, Expert Systems with Applications 37 (2010) 7870–7879.

[34] P. Stevens, The determination of oil prices 1945–1995: a diagrammatic interpretation, Energy Policy 23 (1995) 861–870

[35] A. Subramanya, J. Bilmes, Soft-supervised learning for text classi<sup>fi</sup>cation, in: EMNLP '08 Proceedings of the Conference on Empirical Methods in Natural Language Processing Honolulu, Hawaii, 2008, pp. 1090–1099.

[36] C.-F. Tsai, Y.-C. Hsiao, Combining multiple feature selection methods for stock prediction: union, intersection, and multi-intersection approaches, Decision Support Systems 50 (2010) 258–269.

[37] W. Xie, L. Yu, S. Xu, S. Wang, A new method for crude oil price forecasting based on support vector machines, in: Presented at the International Conference on Computational Science, 2006.

[38] D. Yarowsky, Unsupervised word sense disambiguation rivaling supervised methods, in: ACL '95 Proceedings of the 33rd Annual Meeting on Association for Computational Linguistics Stroudsburg, 1995, pp. 189–196.

[39] S. Youse<sup>fi</sup>, I. Weinreich, D. Reinarz, Wavelet-based prediction of oil prices, Chaos, Solitions and Fractals 25 (2005) 265–275

[40] L. Yu, S. Wang, K.K. Lai, Forecasting crude oil price with an EMD-based neural network ensemble learning paradigm, Energy Economics 30 (2008) 2623–2635.

[41] D. Zhou, O. Bousquet, T.N. Lal, J. Weston, B. Schölkopf, Learning with local and global consistency, in: Advances in Neural Information Processing Systems 16(NIPS), Whistler, Britishi Columbia, 2004, pp. 321–328.

[42] D. Zhou, O. Bousquet, T.N. Lal, J. Weston, B. Schölkopf, Learning with local and global consistency, Advances in Neural Information Processing Systems 16 (2004) 321–328.

[43] X. Zhu, Semi-supervised learning with graphs, PhD thesis, Carnegie Mellon University, CMU-LTI-05–192, 2005.

[44] X. Zhu, Semi-supervised learning literature survey, Technical Report 1530, Computer Science, University of Wisconsin-Madison, 2005.

![](/api/attachments/TGWXM44Y/fulltext/images/995a0eafd2cb66be5a550d76d54a422f2f44abefae358a5a88a7f8843cc88628.jpg)

[45] X. Zhu, Z. Ghahramani, J. Lafferty, Semi-supervised learning using Gaussian <sup>fi</sup>elds and harmonic functions, in: International Conference on Machine Learning (ICML2003), Washington DC, 2003, pp. 912–919.

![](/api/attachments/TGWXM44Y/fulltext/images/806d89470f16d139f3ce869e55672766ed116e94004deb44098ceccdf0a653e2.jpg)

![](/api/attachments/TGWXM44Y/fulltext/images/7008885d41ca0adedff466b4f4697c941be767d9cfecfc1954010b07173dc644.jpg)  
Hyunjung (Helen) Shin received the Ph.D. degree in Data Mining from Seoul National University, and further majored in Machine Learning during her Post-Doc at Max Planck Institute in Germany. Since 2006, she joined Ajou University as a faculty member of the Department of Industrial and Information Systems Engineering. Theory interest of her is more focused on Data Mining algorithms including Machine Learning. Her research activities on application range across areas as different as hospital fraud detection, direct marketing in CRM, Oil/Stock price prediction, bio-medical informatics, etc.

Chan-Kyoo Park is an Associate Professor of School of Business at Dongguk University in Seoul. He earned his Ph.D. in Operations Research from Department of Industrial Engineering at Seoul National University. His current research interests are in the areas of management science and data mining. His research has been published in severa journals including European Journal of Operational Research, Computers and Operations Research and Asia-Pacific Opera: tions Research.

![](/api/attachments/TGWXM44Y/fulltext/images/8b227665f7207645bb874ad8e20e6375e65d2ecc42af39b50e5f39c21b144403.jpg)

![](/api/attachments/TGWXM44Y/fulltext/images/d9c1cbb04d0ddb736f3d81fc57b468a1b54c7b85bd75b317852440eea9bc6c08.jpg)

Tianya Hou received her B.E. degree from Tsinghua university in China and further majored Data Mining as her M.S. degree in Ajou University in South Korea. Her current research topic is oil price prediction using neural network and semi-supervised learning.

Kanghee Park received B.E. degree from Ajou University in 2008, and is currently pursuing his Ph.D. degree at Graduate School of Industrial Engineering, Ajou University, South Korea. His research interest is on <sup>fi</sup>nancial time-series prediction using various techniques of machine learning algorithms.

Sunghee Choi earned his Ph.D. in Economics at the Claremont Graduate University of Claremont Colleges, USA. He is an assistant professor of International Commerce at the Keimyung University, Rep. of Korea.
