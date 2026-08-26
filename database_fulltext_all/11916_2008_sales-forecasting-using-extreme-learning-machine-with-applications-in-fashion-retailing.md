---
otero_id: 11916
otero_key: "BHFPNN3K"
title: "Sales forecasting using extreme learning machine with applications in fashion retailing"
authors: "Zhan-Li Sun; Tsan-Ming Choi; Kin-Fan Au; Yong Yu"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.07.009"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Sales forecasting using extreme learning machine with applications in fashion retailing

Zhan-Li Sun, Tsan-Ming Choi ⁎, Kin-Fan Au, Yong Yu

Institute of Textiles and Clothing, The Hong Kong Polytechnic University, Hung Hom, Kowloon, Hong Kong

## a r t i c l e i n f o

Article history: Received 10 August 2007 Received in revised form 22 July 2008 Accepted 31 July 2008 Available online 13 August 2008

Keywords: Fashion sales forecasting Extreme learning machine Arti<sup>fi</sup>cial neural network Backpropagation neural networks Decision support system

## a b s t r a c t

Sales forecasting is a challenging problem owing to the volatility of demand which depends on many factors. This is especially prominent in fashion retailing where a versatile sales forecasting system is crucial. This study applies a novel neural network technique called extreme learning machine (ELM) to investigate the relationship between sales amount and some signi<sup>fi</sup>cant factors which affect demand (such as design factors). Performances of our models are evaluated by using real data from a fashion retailer in Hong Kong. The experimental results demonstrate that our proposed methods outperform several sales forecasting methods which are based on backpropagation neural networks.

© 2008 Elsevier B.V. All rights reserved.

## 1. Introduction

Sales forecasting refers to the prediction of future sales based on past historical data. Owing to competition [41,42] and globalization, sales forecasting plays a more and more prominent role in a decision support system [26] of a commercial enterprise. An effective sales forecasting can help the decision-maker calculate the production and material costs and determine the sales price. This will result in lower inventory levels, quick response and achieve the objective of just-in-time (JIT) delivery [2,5–7,12]. However, sales forecasting is usually a highly complex problem due to the in<sup>fl</sup>uence of internal and external environments, especially for the fashion and textiles industry [25–27]. Thus, nowadays, how to develop more accurate and timely sales forecasting methods becomes an important research topic. Some retailers improve their stocking decisions by acquiring market information and revising their forecast in multiple stages [8–10]. A good forecasting method can help retailers reduce over-stocking and under-stocking costs [12]. Thus sales forecasting becomes one crucial task in supply chain management under uncertainty and it greatly affects the retailers and other channel members in various ways [31,43]. In this paper, we propose a new method which employs extreme learning machine (ELM) for sales forecasting in fashion retailing [32].

Recently, arti<sup>fi</sup>cial neural networks (ANNs) have been applied extensively for sales forecasting [4,13,34,35,44–46] because they have very promising performance in the areas of control, prediction, and pattern recognition [15,21,22,30,33,38,40]. Many studies conclude that ANN is better than various conventional methods [1,3,28,29,39]. In [13], the statistical time-series model and the ANN based model were investigated for forecasting women's apparel sales. Chakraborty et al. [3] presented an ANN approach based on multivariate time-series analysis, which can accurately predict the <sup>fl</sup>our prices in three cities in USA. Lachtermacher and Fuller [28] developed a calibrated ANN model. In the model, the Box–Jenkins methods are used to determine the lag components of the input data. Moreover, it employed a heuristics method to choose the number of hidden units. In Kuo and Xue [27], the authors reported that the ANNs are better than many conventional statistical forecasting methods (see [3,16] for more details). However, most ANN based sales forecasting methods use gradient-based learning algorithms, such as the backpropagation neural network (BPNN), and problems such as over-tuning and long computation time still arise. A relatively novel learning algorithm for single-hidden-layer feedforward neural networks (SLFN) called extreme learning machine (ELM) has been proposed in [20,47] recently. In ELM, the input weights (linking the input layer to the hidden layer) and hidden biases are randomly chosen, and the output weights (linking the hidden layer to the output layer) are analytically determined by using the Moore– Penrose (MP) generalized inverse. ELM not only learns much faster with a higher generalization performance than the traditional gradient-based learning algorithms but it also avoids many dif<sup>fi</sup>culties faced by gradient-based learning methods such as stopping criteria, learning rate, learning epochs, local minima, and the over-tuned problems [16–18,36].

To the best of our knowledge, the application of ELM for fashion sales forecasting has not been studied in the literature. In this paper, the ELM is selected to analyze fashion sales forecasting on the data provided by a Hong Kong fashion retailer. In this method, some design factors (size, color, etc.) and sales factors (price, etc.) of the fashion apparels are chosen as the input variables of the ELM. Although ELM has many advantages compared to those traditional gradient-based learning algorithms, a shortcoming is that its solution is usually different from time to time because the input weights and hidden biases are randomly chosen, which is also a common existing problem in ANNs that parameters are initialized randomly. As a result, we don't know exactly on which time the initiation will give a good result when we want to predict a future sales amount. Considering the randomness for the selection of weights and hidden biases [24], we propose to predict the future sales amount by an integration of ELMs. For this method, the average series of multiple ELMs' outputs is used as the <sup>fi</sup>nally predicted sales amount. Our <sup>fi</sup>ndings indicate that this extension usually has a smaller predicting error when the <sup>fl</sup>uctuation of ELM outputs is larger.

In addition, the data sets are usually normalized before training so that they fall in a speci<sup>fi</sup>cally given interval. This measure considerably accelerates weight learning and avoids saturation or over<sup>fl</sup>ow of the hidden and output neurons whose activation values generally fall in the [0,1] or [1,1] interval. Finally, for the outputs of ELM, an unnormalization step is necessary to convert the data back into unnormalized units.

Based on the above analyses, we propose a sales forecasting method using ELM for fashion retailing in this paper. The rest of the paper is organized as follows. The fundamental principle of our proposed method is introduced in Section 2. Experimental results and related discussions are presented in Sections 3 and 4, respectively.

## 2. Methodology

In this section, we present the model for the fashion sales forecasting using extreme learning machine (ELM) algorithm. For this method, we <sup>fi</sup>rst extract the sales data of one kind of fashion clothes from the raw data, which include all factors affecting the sales amount. Then the most signi<sup>fi</sup>cant factors are selected to be the inputs of the ELM. The output of the ELM is the sales amount. Subsequently, the data composed of these input/output pairs are divided into training, testing, and predicting sets. Before training, the training data and testing data are normalized respectively so that the inputs fall into a speci<sup>fi</sup>c range. After training, the unnormalization step converts the data back into unnormalized units. Based on the input and output weights obtained by training data and testing data, the predicted sales series for the predicting data can be computed directly through the established ELM. We will give a speci<sup>fi</sup>c example on how each step is implemented in the model in the experiment section. In the following, we give a concise review of ELM [20,37,47], and the normalization and unnormalization procedures [11,23].

## 2.1. Extreme learning machine

As shown in Fig. 1, ELM is a single hidden-layer feedforward neural network (SLFN). It randomly chooses the input weight matrix W and analytically determines the output weight matrix β of SLFN. Suppose that we are training a SLFN with K hidden neurons and an activation function vector $\pmb { \mathrm { g } } ( x ) \pmb { = } ( g _ { 1 } ( x ) , g _ { 2 } ( x ) , . . . , g _ { K } ( x ) )$ to learn N distinct samples $( x _ { \mathrm { i } } , t _ { \mathrm { i } } ) ,$ , where $\boldsymbol { x } _ { \mathrm { i } } = [ x _ { i 1 } , x _ { i 2 } , . . . , x _ { i n } ] ^ { T } \in R _ { n }$ and $t _ { \mathrm { i } } \mathrm { = } [ t _ { i 1 } , t _ { i 2 } , \mathrm { , . . . , } t _ { i n } ] ^ { T } \in R _ { m } .$ . If the SLFNs can approximate these N samples with a zero error, then we have

![](/api/attachments/BHFPNN3K/fulltext/images/18c017ca9c2157251f1e9ac5db4a6007efa1bbccf7bae25961a99aca696823c6.jpg)  
Fig. 1. The structure of ELM model.

![](/api/attachments/BHFPNN3K/fulltext/images/74d5176b1d240f4bf26098f935bd9cd18b82ba646e7a717849989ddcb3888447.jpg)  
Fig. 2. The scheme of the ELM integration system.

$$
\sum_ {j = 1} ^ {N} | | \mathbf {y} _ {j} - \mathbf {t} _ {j} | | = 0,\tag{1}
$$

where $\mathbf { y }$ is the actual output value of the SLFN. There also exist parameters $\beta _ { i } , w _ { \mathrm { i } }$ and $\mathbf { b } _ { i }$ such that

$$
\sum_ {i = 1} ^ {K} \beta_ {i} g _ {i} \left(\boldsymbol {w} _ {i} \cdot \mathbf {x} _ {j} + b _ {i}\right) = \mathbf {t} _ {j}, j = 1, \dots , N,\tag{2}
$$

where $\pmb { w } _ { i } \mathrm { = } [ w _ { i 1 } , . . . , w _ { m } ] ^ { T }$ is the weight vector connecting the ith hidden neuron and the input neurons, $\beta _ { i } \mathopen { } \mathclose \bgroup \left[ \beta _ { i 1 } , . . . , \beta _ { m } \aftergroup \egroup \right] ^ { T } , i \mathop { = } 1 , . . . , K$ is the weight vector connecting the ith hidden neuron and the output neurons, and $b _ { i }$ is the threshold of the ith hidden neuron. The operation ${ \pmb w } _ { i } { \bf \cdot x } _ { j }$ in Eq. (2) denotes the inner product of ${ \pmb w } _ { i ^ { \ast } }$ and $\mathbf { x } _ { j } .$ The above N equations can be written compactly as:

$$
\mathbf {H} \boldsymbol {\beta} = \mathbf {T},\tag{3}
$$

where ${ \bf H } = \{ h _ { i j } \} ~ ( i = 1 , . . . , N$ and $j = 1 , . . . , K )$ is the hidden-layer output matrix, $h _ { i j } { = } g ( w _ { j } { \cdot } x _ { i } { + } b _ { j } )$ denotes the output of the jth hidden neuron with respect to $\mathbf { \bar { x } } _ { \mathrm { i } } , \mathsf { \beta } = \left[ \mathsf { \beta } _ { 1 } , \ldots , \mathsf { \beta } _ { K } \right]$ is the matrix of output weights, $\mathbf { T } = [ \mathbf { t } _ { 1 } ,$ $\mathbf { t } _ { 2 } , . . . , \mathbf { t } _ { N } ] ^ { T }$ is the matrix of targets.

In ELM, the input weights and hidden biases are randomly generated instead of tuned. Thus, the determination of the output weights (linking the hidden layer to the output layer) is as simple as <sup>fi</sup>nding the least-square solution to the given linear system. The minimum norm least-square (LS) solution to the linear system (3) is

$$
\hat {\boldsymbol {\beta}} = \mathbf {H} ^ {\dagger} \mathbf {T},\tag{4}
$$

where $\mathbf { H } ^ { \dagger }$ is the MP generalized inverse of the matrix H. The minimum norm LS solution is unique and has the smallest norm among all the LS solutions. As analyzed by [10], ELM tends to obtain a good generalization performance with a dramatically increased learning speed by using this MP inverse method.

## 2.2. Normalization and unnormalization

The normalization method for the input variables and output variables can be described as follows [13,17]:

$$
\begin{array}{l} x n _ {p i} = 2 \times (x _ {p i} - \min \left\{x _ {p i} \right\}) / (\max \left\{x _ {p i} \right\} - \min \left\{x _ {p i} \right\}), i = 1, 2, \dots , n, p \\ = 1, \ldots , N, \end{array}\tag{5}
$$

$$
y n _ {p} = 2 \times \left(y _ {p} - \min \left\{y _ {p} \right\}\right) / \left(\max \left\{y _ {p} \right\} - \min \left\{y _ {p} \right\}\right), p = 1, \dots , N.\tag{6}
$$

A part of raw data provided by a Hong Kong fashion retailer

<table><tr><td>Month</td><td>Date</td><td>Code number</td><td>Color</td><td>Size</td><td>Price</td><td>Sales amount</td></tr><tr><td>11/2005</td><td>25</td><td>424101160</td><td>54</td><td>026</td><td>445</td><td>5</td></tr><tr><td>11/2005</td><td>26</td><td>424101160</td><td>54</td><td>029</td><td>89</td><td>1</td></tr><tr><td>11/2005</td><td>27</td><td>424101160</td><td>99</td><td>026</td><td>267</td><td>3</td></tr><tr><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr></table>

The unnormalization method for the normalized data is given as follows:

$$
x u n _ {p i} = 0. 5 \times x n _ {p i} \times \left(\max \left\{x n _ {p i} \right\} - \min \left\{x n _ {p i} \right\}\right) + \min \left\{x n _ {p i} \right\},
$$

$$
i = 1, 2, \dots , n, p = 1, \dots , N,\tag{7}
$$

$$
y u n _ {p} = 0. 5 \times y n _ {p} \times \left(\max \left\{y _ {p} \right\} - \min \left\{y _ {p} \right\}\right) + \min \left\{y _ {p} \right\}.\tag{8}
$$

The operators min{·} and max{·} in Eqs. (5) to (8) are used to select the minimum and maximum values from the given data series, respectively.

## 2.3. Steps of fashion sales forecasting using extreme learning algorithm

Assume that the dimension of the input variables is n and the number of the samples is N. De<sup>fi</sup>ne the input variables as $x _ { i } { = } ( x _ { i 1 } , x _ { i 2 }$ $\scriptstyle \ldots , x _ { i n } ) ,$ , the observed values as $t _ { i } , i = 1 , 2 , . . . , N .$ In the following, we give the speci<sup>fi</sup>c steps of the fashion sales forecasting method using ELM.

Step 1 Extract the sales data of one kind of fashion clothes from the raw data according to its code number;

Step 2 Observe the sales amount in a given time interval, select the factors that have a signi<sup>fi</sup>cant effect on the sales as the inputs of ELM;

Step 3 Divide the input/output data $\left( \mathbf { x } _ { i } , t _ { i } \right)$ into training data (TRD of $N _ { t } ) _ { \ast }$ , testing data $( T E D \ o \mathsf { f } N _ { c } ) ,$ , and predicting data (PRD of $N _ { p } )$ randomly, where $N { = } N _ { i } { + } N _ { e } { + } N _ { p } ;$

Step 4 Normalize the training data and testing data using Eqs. (5) and (6), respectively;

Step 5 Select the activation function of hidden neuron and the neuron number of hidden layer of ELM;

Step 6 Input training data and testing data, compute the outputs of ELM, unnormalized the outputs, then obtain the predicted sales series $y _ { i } , \ i = 1 , . . . , N$ of training data and testing data;

Step 7 Based on the input and output weights obtained by Steps 5 and 6, compute the predicted sales series of predicting data and the corresponding predicting error.

Step 8 Repeat Steps 6 and 7 for P times for the same data, then obtain P predicting sales series y<sup>j</sup>, $i = 1 , 2 , . . . , N , \ j = 1 , 2 , . . . , P ;$ compute the average predicting sales series $\begin{array} { r } { \overline { { y } } _ { i } = \frac { 1 } { P } \sum _ { j = 1 } ^ { P } \mathbf { y } _ { i } ^ { j } , } \end{array}$ $i { = } 1 , 2 , . . . , N$ and its predicting error.

As shown in Step 8 and Fig. 2, in order to obtain a higher prediction accuracy, a regression integration method is proposed in this paper as an extension of ELM (ELME) model. To compute the average predicting sales series $\begin{array} { r } { \overline { { y } } _ { i } = \frac { 1 } { P } \sum _ { i = 1 } ^ { P } y _ { i } ^ { j } , i = 1 , 2 , \cdot \cdot \cdot , N , } \end{array}$ we must <sup>fi</sup>rst repeatedly run the ELM for P times with the same data set. It is well known that the mean value is closer to the expectation when the parameter P becomes larger. Since the expectation is a single value, the results obtained by the ELME will become more stable when the parameter P becomes larger. Unfortunately, the computation time also increases when the parameter P becomes larger. Considering both the computation time and the stability of ELME, the parameter P is selected from the interval [100, 1000].

As a remark, for the P trials, the structure of ELM, including the number of layers and the input, are all the same. The input weight matrices of P trials are different from each other because of the random initialization. The P predicted sales series are obtained by using ELM with the P input weight matrices. So the P predicted sales series are different from each other. The <sup>fi</sup>nal predicted sales series are only the mean of the P predicted sales series. It should be pointed out that the structure and parameters of each ELM in the integration system should be retained when the trained system is used to predict a new sales series in real application.

![](/api/attachments/BHFPNN3K/fulltext/images/ef43e146c1e60f157be63cda2959831fe9a5dbea312822cbc37a3caadf4b0e91.jpg)  
(a) The sales amounts of Jeans with different colors

![](/api/attachments/BHFPNN3K/fulltext/images/f1058726c5757807dc357fcad0da479af43296e44adbe49f14a28e1262e8e079.jpg)  
(b) The sales amounts of Jeans with different sizes

![](/api/attachments/BHFPNN3K/fulltext/images/2d6bfae7b817add753d398b565c37e37944a129f3b17911dd4dd4eb8657c9083.jpg)  
(c) The sales amounts of Jeans with different prices  
Fig. 3. The sales amount of Jeans in a month for different colors, sizes, and prices (the x-axes of panels (a), (b) and (c) denote the number of color, the number of size, and the number of price for the corresponding series, respectively. The y-axes denote the respective sales amounts).

Table 2  
The sales mean (μ) and standard deviation (σ) of Jeans in one month for different colors, sizes and prices

<table><tr><td>Cases</td><td>Number</td><td> $\mu$ </td><td> $\sigma$ </td></tr><tr><td>Case 1 (size code: 27; price: 356)</td><td>12 (colors)</td><td>28.1667</td><td>16.1461</td></tr><tr><td>Case 2 (color code: 54; price: 356)</td><td>51 (sizes)</td><td>7.6863</td><td>5.2096</td></tr><tr><td>Case 3 (color code: 54; size code: 27)</td><td>182 (prices)</td><td>52.8516</td><td>29.2236</td></tr></table>

Table 3  
The coef<sup>fi</sup>cients of variation (cvs) of the three cases in Table 2

<table><tr><td>Cases</td><td>cv</td></tr><tr><td>1</td><td>0.5732</td></tr><tr><td>2</td><td>0.6778</td></tr><tr><td>3</td><td>0.5529</td></tr></table>

## 3. Simulation studies

In order to test the validity and performance of the proposed algorithm, we present in this section three experimental results on three sets of real fashion sales data provided by a Hong Kong fashion retailer. Speci<sup>fi</sup>cally, as an example, we give a concise explanation for each step in Section 2.3 combining with the data processed in experiment 1. These explanations are not repeated in experiments 2 and 3 since they are all similar. The batch steepest descent backpropagation algorithm with an adaptive learning rate (GDA), and the gradient descent momentum and adaptive learning ratio backpropagation (GDX) are two typical backpropagation algorithms [15]. As a comparison, we also give the experimental results obtained by the GDA and GDX algorithms on the same data set.

Table 4  
The comparisons of GDA, GDX, ELM and ELME in experiment 1

<table><tr><td></td><td>GDA</td><td>GDX</td><td>ELM</td><td>ELME</td></tr><tr><td> $\mu_{\text{mse}}^{\text{tr}}$ </td><td>1.1450</td><td>2.8538</td><td>0.0001</td><td>2.1124e-005</td></tr><tr><td> $\text{std}_{\text{mse}}^{\text{tr}}$ </td><td>0.5296</td><td>0.44053</td><td>0.0001</td><td></td></tr><tr><td> $\mu_{\text{mse}}^{\text{te}}$ </td><td>1.6903</td><td>2.138</td><td>2.0640</td><td>2.0629</td></tr><tr><td> $\text{std}_{\text{mse}}^{\text{te}}$ </td><td>0.4527</td><td>0.45464</td><td>0.0228</td><td></td></tr><tr><td> $\mu_{\text{mse}}^{\text{pr}}$ </td><td>1.0710</td><td>2.6304</td><td>0.0002</td><td>4.9872e-005</td></tr><tr><td> $\text{std}_{\text{mse}}^{\text{pr}}$ </td><td>0.5034</td><td>0.39369</td><td>0.0002</td><td></td></tr></table>

All simulations are conducted in MATLAB running on an ordinary personal computer with a dual core CPU (1.73 GHZ and 0.97 GHZ) and 1 G memory. In the following experiments, the activation function is the sigmoidal function:

$$
g (x) = \frac {1}{1 + e ^ {- x}}.\tag{9}
$$

The performance index is the mean squared error (mse) between the predicted sales amount and actual sales amount:

$$
\mathrm{mse} = \frac {1}{N} \sum_ {i = 1} ^ {N} (y _ {i} - t _ {i}) ^ {2},\tag{10}
$$

where $y _ { i }$ and $t _ { i }$ are the predicted sales amount and actual sales amount, respectively

![](/api/attachments/BHFPNN3K/fulltext/images/6cb436a04d13f2fa28f48fec970b1751756fc6202eac26f69f61d24dc93d7ed2.jpg)  
(a) The fashion sales series in the training data

![](/api/attachments/BHFPNN3K/fulltext/images/909f739ca96ceed01fe10d3d478a2199afc6b8f432fb31707e68c5cd2ef53bdf.jpg)

(b) The fashion sales series in the testing data  
![](/api/attachments/BHFPNN3K/fulltext/images/f5ab41102aac477d13f7d2529877ae660115c8aabe4cd284f724b023dd3181d9.jpg)  
Fig. 4. The fashion sales series in the training, testing, and predicting sets in experiment 1 (The x-axes of panels (a), (b), and (c) denote the number of samples of the corresponding series; the y-axes denote the sales amounts).

Table 5  
The performance index ratios in experiment 1

<table><tr><td></td><td>GDAELM</td><td>GDXELM</td><td>ELMEELM</td></tr><tr><td> $\mu_{mse}^{tr}$ </td><td>11,450</td><td>28,538</td><td>0.1604</td></tr><tr><td> $std_{mse}^{tr}$ </td><td>5296</td><td>4405.3</td><td></td></tr><tr><td> $\mu_{mse}^{te}$ </td><td>0.81894</td><td>1.0359</td><td>0.9994</td></tr><tr><td> $std_{mse}^{te}$ </td><td>19.855</td><td>19.94</td><td></td></tr><tr><td> $\mu_{mse}^{pr}$ </td><td>5355</td><td>13,152</td><td>0.2296</td></tr><tr><td> $std_{mse}^{pr}$ </td><td>2517</td><td>1968.4</td><td></td></tr></table>

Table 6  
The ratios between st $\mathrm { l } _ { \mathrm { m s e } }$ and $\mu _ { \mathrm { m s e } }$ for ELM

<table><tr><td></td><td>Training data</td><td>Testing data</td><td>Predicting data</td></tr><tr><td> $\text{std}_{\text{mse}}$ </td><td>1.0388</td><td>0.0111</td><td>1.1075</td></tr><tr><td> $\mu_{\text{mse}}$ </td><td></td><td></td><td></td></tr></table>

To measure the stability of the algorithms, we de<sup>fi</sup>ne the coef<sup>fi</sup>cient of variation cv as the ratio between standard deviation (σ) and mean (μ):

$$
\mathrm{CV} = \frac {\sigma}{\mu}.\tag{11}
$$

The standard deviation std $\mathsf { I } _ { \mathrm { m s e } }$ of P trials is de<sup>fi</sup>ned as:

$$
\operatorname{std} _ {\text { mse }} = \sqrt {\frac {1}{P} \sum_ {i = 1} ^ {P} \left(\operatorname{mse} _ {i} - \mu\right) ^ {2}},\tag{12}
$$

where ms $\underline { { \circ } } _ { i } , i = 1 , 2 , . . . , P$ is the mean squared error obtained when we run the algorithm for the ith time with the same data set, $\mu _ { \mathrm { m s e } }$ is the mean value of mse :

$$
\mu_ {\mathrm{mse}} = \frac {1}{P} \sum_ {j = 1} ^ {P} \mathrm{mse} _ {j}.\tag{13}
$$

## 3.1. Experiment 1

According to the code number of the commodity, the Jeans data is extracted from the raw data in Table 1 and used as the experimental data. There are 7 attributes for this kind of clothes: month, date, code number, color, size, price, sales amount. Since the goal of this study is to investigate the relationship between the fashion sales amount and the most signi<sup>fi</sup>cant factors affecting the sales amount, and owing to the features of the data sets, the attributes of month, date and code number are not selected.

Table 7  
The comparisons of GDA, GDX, ELM and ELME in experiment 2

<table><tr><td></td><td>GDA</td><td>GDX</td><td>ELM</td><td>ELME</td></tr><tr><td> $\mu_{\text{mse}}^{\text{tr}}$ </td><td>0.9859</td><td>2.1254</td><td>0.1556</td><td>0.1548</td></tr><tr><td> $\text{std}_{\text{mse}}^{\text{tr}}$ </td><td>0.2817</td><td>1.8719</td><td>0.0010</td><td></td></tr><tr><td> $\mu_{\text{mse}}^{\text{te}}$ </td><td>0.6015</td><td>1.5050</td><td>1.4094</td><td>1.4077</td></tr><tr><td> $\text{std}_{\text{mse}}^{\text{te}}$ </td><td>0.1665</td><td>1.3556</td><td>0.0425</td><td></td></tr><tr><td> $\mu_{\text{mse}}^{\text{pr}}$ </td><td>0.7810</td><td>1.6818</td><td>0.6515</td><td>0.649</td></tr><tr><td> $\text{std}_{\text{mse}}^{\text{pr}}$ </td><td>0.2978</td><td>1.0578</td><td>0.0366</td><td></td></tr></table>

According to the expert knowledge, the remaining factors, color, size, and price, have a signi<sup>fi</sup>cant impact on the sales amount. To analyze their impacts further, as shown in Fig. 3, we give the sales amount of Jeans with different colors, sizes and prices in March, 1999. As shown in Table 2, there are 12, 51, 182 kinds of colors, sizes, and prices, respectively for the Jeans in March. Fig. 3(a) shows the sales amount of Jeans with the same size (size number: 027) and price (356). Each point represents the sales amount in a month for one color. Fig. 3(b) shows the sales amount of Jeans with same color (color number: 54) and price (356) but with different sizes. The sales amount of Jeans with the same color (color number: 54) and size (size number: 027) but with different prices is shown in Fig. 3(c).

For the three cases in Fig. 3, the mean (μ) and standard deviation (σ) of the sales amount are given in Table 2. The coef<sup>fi</sup>cients of variation (cvs) are given in Table 3. From Fig. 3 and Tables 2–3, we can see that the factors of color, size, and price have signi<sup>fi</sup>cant impacts on the sales amount. We use the coef<sup>fi</sup>cients of variation (cvs) to measure the signi<sup>fi</sup>cance of factors. As shown in Table 3, three factors color, size, and price have similar cvs so they are all selected. Therefore, they are used as the inputs of the ELM. If more factors are available, we can sort them according to the criterion cvs and then select the factors with the large cvs. The sales amount is the output of the ELM. The data processed are composed of these input/output pairs.

![](/api/attachments/BHFPNN3K/fulltext/images/00fdae352d8b61b46b07232de59a99cea3b5a9d2561a49fb90cf50c2b9c740b9.jpg)

(a) The fashion sales series in the training data  
![](/api/attachments/BHFPNN3K/fulltext/images/3eb1a83a0046b8ab4b75ddb1ef73969d32df77c127fe6390fbd544c8860176e6.jpg)

(b) The fashion sales series in the testing data  
![](/api/attachments/BHFPNN3K/fulltext/images/d9b27fdd67b8eacbdb3d6001ac09718e73fc7a1e1c5c8408c1e50055d91d7d18.jpg)  
(c) The fashion sales series in the predicting data  
Fig. 5. The fashion sales series in the training, testing, and predicting sets in experiment 2 (The x-axes of panels (a), (b), and (c) denote the number of samples of the respective series; the y-axes denote the sales amounts).

Table 8  
The performance index ratios in experiment 2

<table><tr><td></td><td>GDAELM</td><td>GDXELM</td><td>ELMEELM</td></tr><tr><td> $\mu_{mse}^{tr}$ </td><td>6.3361</td><td>13.659</td><td>0.9951</td></tr><tr><td> $std_{mse}^{tr}$ </td><td>281.7000</td><td>1871.9</td><td></td></tr><tr><td> $\mu_{mse}^{te}$ </td><td>0.4268</td><td>1.0678</td><td>0.9988</td></tr><tr><td> $std_{mse}^{te}$ </td><td>3.9176</td><td>31.896</td><td></td></tr><tr><td> $\mu_{mse}^{pr}$ </td><td>1.1988</td><td>2.5814</td><td>0.9962</td></tr><tr><td> $std_{mse}^{pr}$ </td><td>8.1366</td><td>28.902</td><td></td></tr></table>

Table 9  
The ratios between ${ \sf s t d } _ { \mathrm { m s e } }$ and $\mu _ { \mathrm { m s e } }$ for ELM

<table><tr><td></td><td>Training data</td><td>Testing data</td><td>Predicting data</td></tr><tr><td> $\text{std}_{\text{mse}}$ </td><td rowspan="2">0.0066</td><td rowspan="2">0.0301</td><td rowspan="2">0.0561</td></tr><tr><td> $\mu_{\text{mse}}$ </td></tr></table>

Here, 200 input/output pairs are used as the experimental data, in which 60% of the data points are used for the training set, 20% for the testing set, and 20% for the predicting set. The sales amounts in the training, testing, and predicting sets are shown in Fig. 4(a), (b), and (c), respectively. The training data and testing data are <sup>fi</sup>rst normalized by using Eqs. (5) and (6). As a result, the training data and testing data all fall into the interval [−1,1]. Then we perform the experiment on training and testing data according to steps 3–7 depicted in Section 2.3. As done in [19], the average mse $\left( \mu _ { \mathrm { m s e } } \right)$ and standard deviation $( \mathsf { s t d } _ { \mathrm { m s e } } )$ of 100 trials are used to evaluate the performance of the algorithms. For simplicity, the symbols tr, te, and pr are added into $\mu _ { \mathrm { m s e } }$ and $\mathsf { s t d } _ { \mathrm { m s e } }$ as superscripts to denote the experimental results for training, testing, and predicting data, respectively.

When the number of hidden neurons is increased from 1 to 30, the number that gives the smallest validation error is chosen for the ELM and the two backpropogation algorithms. The experimental comparisons for the batch steepest descent backpropagation algorithm with an adaptive learning rate (GDA), gradient descent momentum and adaptive learning ratio backpropagation (GDX), extreme learning algorithm (ELM) and its extension (ELME) are given in Table 4.

Table 10  
The comparisons of GDA, GDX, ELM and ELME in experiment 3

<table><tr><td></td><td>GDA</td><td>GDX</td><td>ELM</td><td>ELME</td></tr><tr><td> $\mu_{\text{mse}}^{\text{tr}}$ </td><td>0.3368</td><td>0.4213</td><td>0.4930</td><td>0.4046</td></tr><tr><td> $std_{\text{mse}}^{\text{tr}}$ </td><td>0.1346</td><td>0.1530</td><td>0.0979</td><td></td></tr><tr><td> $\mu_{\text{mse}}^{\text{te}}$ </td><td>0.4893</td><td>0.3534</td><td>0.4297</td><td>0.2795</td></tr><tr><td> $std_{\text{mse}}^{\text{te}}$ </td><td>0.2538</td><td>0.1982</td><td>0.1337</td><td></td></tr><tr><td> $\mu_{\text{mse}}^{\text{pr}}$ </td><td>0.7308</td><td>0.6100</td><td>0.4952</td><td>0.3888</td></tr><tr><td> $std_{\text{mse}}^{\text{pr}}$ </td><td>0.3336</td><td>0.2327</td><td>0.1493</td><td></td></tr></table>

Table 11  
The performance index ratios in experiment 3

<table><tr><td></td><td>GDAELM</td><td>GDXELM</td><td>ELMEELM</td></tr><tr><td> $\mu_{\text{mse}}^{\text{tr}}$ </td><td>0.67172</td><td>0.8546</td><td>0.82069</td></tr><tr><td> $std_{\text{mse}}^{\text{tr}}$ </td><td>1.0338</td><td>1.5628</td><td></td></tr><tr><td> $\mu_{\text{mse}}^{\text{te}}$ </td><td>1.0464</td><td>0.8224</td><td>0.65045</td></tr><tr><td> $std_{\text{mse}}^{\text{te}}$ </td><td>1.2202</td><td>1.4824</td><td></td></tr><tr><td> $\mu_{\text{mse}}^{\text{pr}}$ </td><td>1.4561</td><td>1.2318</td><td>0.78514</td></tr><tr><td> $std_{\text{mse}}^{\text{pr}}$ </td><td>1.4625</td><td>1.5586</td><td></td></tr></table>

The performance index ratios between GDA, GDX, ELME and ELM are given in Table 5. It should be pointed out that the performance index std of the ELME is not <sup>fi</sup>lled in Tables 4 and 5 because there is only one result after the 100 trials of ELM. (For the stability of the ELME, we have given a discussion in Section 2.3.) From Tables 4 and 5, it can be seen that ELM and ELME generally have smaller training, testing, and predicting errors than GDA and GDX. In Table 5, the training, testing, and predicting errors of ELME are only 16.04%, 99.94% and 22.96% of the corresponding performance indices of ELM, respectively.

![](/api/attachments/BHFPNN3K/fulltext/images/7e3967596bdd8a17d4c8fbc9ba45b775ea8a2359b80fbc81a77dfbbcb033301b.jpg)  
(a) The fashion sales series in the training data

![](/api/attachments/BHFPNN3K/fulltext/images/b57ca4dd5363aa62290b8d3174aebaeefd721dc5316d9c9eddcab15020aede72.jpg)

(b) The fashion sales series in the testing data  
![](/api/attachments/BHFPNN3K/fulltext/images/1cfce74bcaacbdc9aba2b11ad3fe5b126d1ca0df8b31aaa9170f25da64aad0f1.jpg)  
(c) The fashion sales series in the predicting data  
Fig. 6. The fashion sales series in the training, testing, and predicting sets in experiment 3 (The x-axes of panels (a), (b), and (c) denote the number of samples of the corresponding series; the y-axes denote the sales amounts).

Table 12  
The ratios between std $\mathrm { m s e }$ and $\mu _ { \mathrm { m s e } }$ for ELM

<table><tr><td></td><td>Training data</td><td>Testing data</td><td>Predicting data</td></tr><tr><td> $\frac{\text{std}_{\text{mse}}}{\mu_{\text{mse}}}$ </td><td>0.1985</td><td>0.3112</td><td>0.3016</td></tr></table>

Table 13  
The mean (μ) and standard deviation (σ) of sales amounts for three products in one year

<table><tr><td>Product</td><td>1</td><td>2</td><td>3</td></tr><tr><td> $\mu$ </td><td>1.8907</td><td>2.8979</td><td>1.4040</td></tr><tr><td> $\sigma$ </td><td>1.3476</td><td>1.4040</td><td>0.8969</td></tr></table>

To analyze the <sup>fl</sup>uctuation of ELM, the ratios between ${ \mathsf { s t d } } _ { \mathrm { m s e } }$ and μ are given in Table 6. The standard deviation std is about one time of the average error $\mu _ { \mathrm { m s e } }$ in Table 6. Therefore, the training and predicting errors of ELM have a large variation from time to time due to the random initiation of input weights and hidden bias. That is to say, the <sup>fl</sup>uctuation of ELM is large in experiment 1.

Based on the above analyses, we can conclude that ELM and its extension ELME are better than the other two methods for fashion sales forecasting. And the ELME is better than ELM when the <sup>fl</sup>uctuation of ELM is large.

## 3.2. Experiment 2

In experiment 2, the sales data of sock are selected as the experimental data. In the data, there is only one kind of size for the sock. Thus the size factor is not selected as an important factor (cvs=0). Only the color and sales price of the clothes are selected as the signi<sup>fi</sup>cant factors. Here, 200 samples are used as the experimental data, in which 60% of the data points are used for the training set, 20% for the testing set, and 20% for the predicting set. The sales amounts in the training, testing, and predicting sets are shown in Fig. 5(a), (b) and (c), respectively.

To compare ELM and ELME with the other two methods, the same data and inputs are used for the four methods. The experimental comparisons for GDA, GDX, ELM and ELME are given in Table 7. The performance index ratios between GDA, GDX, ELME and ELM are given in Table 8. From Tables 7 and 8, we can conclude that the ELM and ELME are better than the GDA and GDX algorithms when we consider the training, testing, predicting errors, and the standard deviations.

To analyze the <sup>fl</sup>uctuation of ELM, the ratios between std and msē are given in Table 9. From Table 9, we can see that the <sup>fl</sup>uctuation of the training, testing and predicting errors in experiment 2 is much less than the corresponding results in experiment 1. In Table 8, the training, testing, and predicting errors of ELME are 99.51%, 99.88%, and 99.62% of the corresponding performance indices of ELM, respectively. The extent that the errors are decreased by the ELME is not as large as the result in experiment 1.

## Table 14

The cvs of sales amounts for three products in one year

<table><tr><td>Product</td><td>1</td><td>2</td><td>3</td></tr><tr><td>cvs</td><td>0.7128</td><td>0.4845</td><td>0.6388</td></tr></table>

Table 15  
The three experimental results for ELM

<table><tr><td></td><td>1</td><td>2</td><td>3</td></tr><tr><td> $\mu_{\text{mse}}^{\text{tr}}$ </td><td>0.0001</td><td>0.1556</td><td>0.4930</td></tr><tr><td> $\text{std}_{\text{mse}}^{\text{tr}}$ </td><td>0.0001</td><td>0.0010</td><td>0.0979</td></tr><tr><td> $\mu_{\text{mse}}^{\text{te}}$ </td><td>2.0640</td><td>1.4094</td><td>0.4297</td></tr><tr><td> $\text{std}_{\text{mse}}^{\text{te}}$ </td><td>0.0228</td><td>0.0425</td><td>0.1337</td></tr><tr><td> $\mu_{\text{mse}}^{\text{pr}}$ </td><td>0.0002</td><td>0.6515</td><td>0.4952</td></tr><tr><td> $\text{std}_{\text{mse}}^{\text{pr}}$ </td><td>0.0002</td><td>0.0366</td><td>0.1493</td></tr></table>

Table 16  
The training time of four methods with different number of samples

<table><tr><td>NS</td><td>Δt(GDA)</td><td>Δt(GDX)</td><td>Δt(ELM)</td><td>Δt(ELME)</td></tr><tr><td>200</td><td>0.5934</td><td>0.5353</td><td>0.0122</td><td>1.2190</td></tr><tr><td>1000</td><td>0.8814</td><td>0.6414</td><td>0.0195</td><td>1.9530</td></tr><tr><td>5000</td><td>3.2447</td><td>2.2552</td><td>0.0786</td><td>7.8590</td></tr><tr><td>10,000</td><td>9.9348</td><td>6.4550</td><td>0.1528</td><td>15.2820</td></tr></table>

## 3.3. Experiment 3

In this experiment, the Jacket data is used as the experimental data. The color, size and price of the clothes are selected as the signi<sup>fi</sup>cant factors. 200 samples are used as the experimental data, in which 60% of the data points are used for the training set, 20% for the testing set, and 20% for the predicting set, and the respective sales amounts are shown in Fig. 6(a), (b), and (c).

The experimental comparisons for GDA, GDX, ELM and ELME are given in Table 10. The performance index ratios between GDA, GDX, ELME and ELM are given in Table 11. From Tables 10 and 11, the ELM and ELME are better than the GDA and GDX algorithms when we consider the training, testing, predicting errors, and the standard deviations.

In Table 11, the training, testing, and predicting errors of ELME are 82.07%, 65.05% and 78.51% of the corresponding performance indices of ELM, respectively. The ratios between std and μ are given in Table 12.

In general, considering the predicting accuracy and stability, ELM and its extension ELME are better than GDA and GDX. From the above simulation results, we can see that ELME can have a higher accuracy than ELM especially when the experimental results of ELM have a larger <sup>fl</sup>uctuation.

## 4. Further discussions

The forecasting accuracy of an approach is often in<sup>fl</sup>uenced by the inherent nature of a product and its sales pattern. In this section, the effect of sales amount <sup>fl</sup>uctuation on the prediction's accuracy of ELM is investigated. The sales amount <sup>fl</sup>uctuations are measured by the coef<sup>fi</sup>cients of variation (cvs). Sales data of three products are studied, each with a different sales feature. Table 13 shows the mean (μ) and standard deviation (σ) of sales amounts for three products in one year.

The cvs of sales amounts for three products in one year is given in Table 14. Table 15 shows three experimental results for ELM.

From Tables 14 and 15, it can be observed that there is a relationship between the cvs and the forecasting errors. When the cv is larger (i.e., the <sup>fl</sup>uctuation of the product's demand is larger), the training, testing, and predicting errors of ELM are generally lower, and vice versa. This result shows that the <sup>fl</sup>uctuation in demands of product has a great impact on the forecasting accuracy, and the ELM is especially accurate when forecasting for products with a large cv. The reason is that the neural network tends to be biased with data of relatively small variance (small cv) [14], and the bias will decrease the forecasting accuracy. Intuitively, the ANN is a soft computing method. It learns the pattern (sale amount) by training samples and remembering the knowledge using its structure. When the patterns are too close (with a small cv), the ANN can't remember and distinguish these patterns. On the contrary, when the pattern has a larger cv, it is easier to be learned by the ANN.

## Table 17

The training time ratios between GDA, GDX and ELM

<table><tr><td>NS</td><td> $\frac{\Delta t(GDA)}{\Delta t(ELM)}$ </td><td> $\frac{\Delta t(GDA)}{\Delta t(ELM)}$ </td></tr><tr><td>200</td><td>48.639</td><td>43.877</td></tr><tr><td>1000</td><td>45.2</td><td>32.892</td></tr><tr><td>5000</td><td>41.281</td><td>28.692</td></tr><tr><td>10,000</td><td>65.018</td><td>42.245</td></tr></table>

To compare the computation ef<sup>fi</sup>ciency of the four methods, Table 16 gives the training time of four methods (Δt) with different number of samples (NS). It should be pointed out that the training time of ELME is the sum of training time that is consumed in 100 trials of ELM.

The training time ratios between GDA, GDX and ELM are given in Table 17. From Tables 16 and 17, we can see that ELM has a very shorter training time than GDA and GDX.

## 5. Conclusion

Owing to market competition and globalization, sales forecasting plays a more and more prominent role in a decision support system of a commercial enterprise. It is especially true in fashion business. How to develop more accurate and timely sales forecasting methods becomes an important research topic. In this paper, we apply a relatively novel neural network technique, extreme learning machine (ELM) and its extension, to fashion sales forecasting. It is known that ELM not only has a higher generalization performance than the traditional gradient-based learning algorithms but it also avoids many dif<sup>fi</sup>culties faced by gradient-based learning methods such as stopping criteria, learning rate, learning epochs, local minima, and the over-tuned problem. Therefore, ELM is selected to analyze fashion sales forecasting on the data provided by a Hong Kong fashion retailer in this paper. Using this method, the most signi<sup>fi</sup>cant factors affecting the sales amount are selected as the inputs of ELM. As an extension, the arithmetic mean value of multiple trials is used as the <sup>fi</sup>nal predicted sales forecasting amount. Our experiments have successfully demonstrated that both ELM and its extension can be employed in sales forecasting for fashion retailing and they can produce smaller predicting errors than some other sales forecasting methods based on two well-established backpropagation neural networks (BPNN). The ELM is thus a promising tool in sales forecasting for fashion retailers. Moreover, in our approach, by using the statistical mean value of multiple trials as the <sup>fi</sup>nal forecasting result, the ELM forecasting result is more stable than the BPNN algorithms. This makes the ELM approach a better choice when employing to the practical forecasting of fashion sales, in which the BPNN result can be very unstable. This study also provides a guide for the selection of the important sales forecasting factors such as design factors (size, color, etc.) and the price factor.

## Acknowledgments

We sincerely thank the editor, and the anonymous reviewers for their many helpful suggestions and kind advice. Tsan-Ming Choi's research is partially supported by the Research Grants Council of Hong Kong, grant's number PolyU5145/06E, and the research funding by The Hong Kong Polytechnic University. Kin-Fan Au’s research is partially supported by the Research Grants Council of Hong Kong, Grant’s number PolyU5101/05E. Thanks are given to Tiaojun Xiao, Chun-Hung Chiu, Hye Kyung Im, Danqin Yang for their comments on the earlier draft of this paper.

## References

[1] E. Alfaro, N. García, M. Gámez, D. Elizondo, Bankruptcy forecasting: an empirical comparison of AdaBoost and neural networks, Decision Support Systems 45 (1) (2008) 110–122.

[2] K.F. Au, N.Y. Chan, Quick response for Hong Kong clothing suppliers: a total system approach, Proceedings of the 13th Annual Conference of the Production and Operations Management Society (San Francisco, USA, 2002.

[3] K. Chakraborty, K. Mehrotra, C.K. Mohan, Forecasting the behavior of multivariate time series using neural networks, Neural Networks 5 (1992) 961–970.

[4] P.C. Chang, Y.W. Wang, Fuzzy Delphi and back-propagation model for sales forecasting in PCB industry, Expert Systems with Applications 30 (4) (2006) 715–726.

[5] T.M. Choi, Quick response in fashion supply chains with dual information updating, Journal of Industrial and Management Optimization 2 (2006) 255–268

[6] T.M. Choi, Pre-season stocking and pricing decisions for fashion retailers with multiple information updating, International Journal of Production Economics 106 (2007) 146–170.

[7] T.M. Choi, P.S. Chow, Mean-variance analysis of quick response program, International Journal of Production Economics 114 (2) (2008) 456–475.

[8] T.M. Choi, D. Li, H. Yan, Optimal two-stage ordering policy with Bayesian information updating, Journal of the Operational Research Society 54 (2003) 846–859.

[9] T.M. Choi, D. Li, H. Yan, Optimal single ordering policy with multiple delivery modes and Bayesian information updates, Computers and Operations Research 31 (2004) 1965–1984.

[10] T.M. Choi, D. Li, H. Yan, Quick response policy with Bayesian information updates, European Journal of Operational Research 170 (2006) 788–808.

[11] H. Demuth, M. Beale, M. Hagan, Neural Network Toolbox for Use with MATLAB, The Mathworks, Inc., Natick, MA, 2006.

[12] G.D. Eppen, A.V. Iyer, Improved fashion buying with Bayesian updates, Operations Research 45 (1997) 805–819.

[13] C. Frank, A. Garg, L. Sztandera, A. Raheja, Forecasting women's apparel sales using mathematical modeling, International Journal of Clothing Science and Technology 15 (2) (2003) 107–125.

[14] S. Geman, E. Bienenstock, R. Doursat, Neural networks and the nias/variance dilemma, Neural Computation 4 (1) (1992) 1–58.

[15] D.S. Huang, Systematic Theory of Neural Networks for Pattern Recognition, Publishing House of Electronic Industry of China, Beijing, 1996.

[16] G.B. Huang, Learning capability and storage capacity of two-hidden-layer feedforward networks, IEEE Transactions on Neural Networks 14 (2) (2003) 274–281.

[17] G.B. Huang, H.A. Babri, Upper bounds on the number of hidden neurons in feedforward networks with arbitrary bounded nonlinear activation functions, IEEE Transactions on Neural Networks 9 (1) (1998) 224–229.

[18] G.B. Huang, L. Chen, C.K. Siew, Universal approximation using incremental constructive feedforward networks with random hidden nodes, IEEE Transactions on Neural Networks 17 (4) (2006) 879–892.

[19] G.B. Huang, Q.Y. Zhu, C.K. Siew, Extreme learning machine: a new learning scheme of feedforward neural networks, Proceedings of the International Joint Conference on Neural Networks (IJCNN2004) (Budapest, Hungary, July 2004, pp. 985–990.

[20] G.B. Huang, Q.Y. Zhu, C.K. Siew, Extreme learning machine: theory and applications, Neurocomputing 70 (2006) 489–501.

[21] C.L. Hui, T.W. Lau, S.F. Ng, K.C.C. Chan, Neural network prediction of human psychological perception of fabric hand, Textile Research Journal, 74 (2004) 375–383.

[22] C.L. Hui, S.F. Ng, A new approach for prediction of sewing performance of fabrics in apparel manufacturing using arti<sup>fi</sup>cial neural networks, Journal of the Textile Institute 96 (2005) 401–406.

[23] J.S.R. Jang, N. Gulley, Fuzzy Logic Toolbox for Use with MATLAB, The Mathworks, Inc., Natick, MA, 2006.

[24] J. Kittler, M. Hatef, P.W. Duin, J. Matas, On combining classi<sup>fi</sup>ers, IEEE Transactions on Pattern Analysis and Machine Intelligence 20 (3) (1998) 226–239.

[25] R.J. Kuo, A sales forecasting system based on fuzzy neural network with initial weights generated by genetic algorithm, European Journal of Operational Research 129 (2001) 496–517.

[26] R.J. Kuo, K.C. Xue, A decision support system for sales forecasting through fuzzy neural networks with asymmetric fuzzy weights, Decision Support Systems 24 (2) (1998) 105–126.

[27] R.J. Kuo, K.C. Xue, Fuzzy neural networks with application to sales forecasting, Fuzzy Sets and Systems 108 (1999) 123–143.

[28] G. Lachtermacher, J.D. Fuller, Backpropagation in time-series forecasting, Journal of Forecasting 14 (1995) 381–393.

[29] M. Lam, Neural network techniques for <sup>fi</sup>nancial performance prediction: integrating fundamental and technical analysis, Decision Support Systems 37 (4) (2004) 567-581.

[30] W. Leigh, R. Purvis, J.M. Ragusa, Forecasting the NYSE composite index with technical analysis, pattern recognizer, neural network, and genetic algorithm: a case study in romantic decision support, Decision Support Systems 32 (4) (2002) 361–377.

[31] W.Y. Liang, C.C. Huang, Agent-based demand forecast in multi-echelon supply chain, Decision Support Systems 42 (2006) 390–407.

[32] Z.L. Sun, K.F. Au, T.M. Choi, A hybrid neuron-fuzzy inference system through integration of fuzzy logic and extreme learning machines, IEEE Transactions on Systems, Man and Cybernetics-Part B: Cybernetics 37 (5) (2007) 1321–1331

[33] Z.L. Sun, D.S. Huang, C.H. Zheng, L. Shang, Optimal selection of time lags for temporal blind source separation based on genetic algorithm, Neurocomputing 69 (7–9) (2006) 884–887.

[34] L.M. Sztandera, C. Frank, B. Vemulapali, Predicting women's apparel sales by soft computing, Lecture Notes in Arti<sup>fi</sup>cial Intelligence 3070 (2004) 1193–1198.

[35] L.M. Sztandera, C. Frank, B. Vemulapali, Prediction of women's apparel sales using soft computing methods, Lecture Notes in Arti<sup>fi</sup>cial Intelligence 3215 (2004) 506–512.

[36] S. Tamura, M. Tateishi, Capabilities of a four-layered feedforward neural network: four layers versus three, IEEE Transactions on Neural Networks 8 (2) (1997) 251–255.

[37] S. Thomassey, A. Fiordaliso, A hybrid sales forecasting system based on clustering and decision trees, Decision Support Systems 42 (2006) 408–421.

[38] P.D. Wasserman, Neural Computing: Theory and Practice, Van Nostrand Reinhold, New York, USA, 1989.

[39] A.S. Weigend, D.E. Rumelhart, B.A. Huberman, Generalization by weight-elimination with application to forecasting, Advance Neural Information Processing System 3 (1990) 875–882.

[40] H. White, Arti<sup>fi</sup>cial Neural Networks: Approximations and Learning Theory, Blackwell Oxford UK 1992

[41] T.J. Xiao, X.T. Qi, Price competition, cost and demand disruptions and coordination of a supply chain with one manufacturer and two competing retailers, Omega 36 (2008) 741–753.

[42] T.J. Xiao, X.T. Qi, G. Yu, Coordination of supply chain after demand disruptions retailers compete, International Journal of Production Economics 109 (2007) 162–179.

[43] T.J. Xiao, D.Q. Yang, Price and service competition of supply chains with risk-averse retailers under demand uncertainty, International Journal of Production Economics 114 (2008) 187–200.

[44] H. Yoo, R.L. Pimmel, Short-term load forecasting using a self-supervised adaptive neural network, IEEE transactions on Power Systems 14 (2) (1999) 779–784.

[45] Y. Yu, T.M. Choi and K.F. Au, Web-based Sales Forecasting System with Applications in Fashion Business, Forthcoming in Research Journal of Textile and Apparel. in press.

![](/api/attachments/BHFPNN3K/fulltext/images/6ca36019ec07871c43087b63daaabf63941c12b66a67f5b6a5d4d3a0dee60219.jpg)

[46] G.Q. Zhang, B.E. Patuwo, M.Y. Hu, Forecasting with arti<sup>fi</sup>cial neural networks: the state of the art, International Journal of Forecasting 14 (1998) 35-62

[47] Q.Y. Zhu, A.K. Qin, P.N. Suganthan, G.B. Huang, Evolutionary extreme learning machine. Pattern Recognition 38 (2005) 1759–1763.

Kin-Fan AU is an associate professor in the Institute of Textiles and Clothing of The Hong Kong Polytechnic University. His research interest is in the business aspects of fashion and textiles, particularly in the area of global trading of fashion and textile products. Dr. Au has published many papers in textiles and related journals on topics of world trading, offshore production and modelling of textiles and apparel trade

![](/api/attachments/BHFPNN3K/fulltext/images/5a6602cfd07194ea52cfcbfc9066e76ff57698d496343c79456017f82f8c45ab.jpg)  
Zhan-Li Sun received his PhD degree from the University of Science & Technology of China in 2005. He worked as a Research Associate at The Hong Kong Polytechnic University in 2006–2007 and Research Fellow at Nanyang Technological University in 2007-2008, He is currently with the National University of Singapore. His research interests include machine learning, signal and image processing.

![](/api/attachments/BHFPNN3K/fulltext/images/c5a5283d72d3dcc446cfbb8bf9b994ea6c42a6eb7ff5a9b9197740e3f11444ef.jpg)

Yong Yu is currently a research associate at The Hong Kong Polytechnic University. He received his PhD from the Hong Kong Polytechnic University. His research interests are computer simulation, cluster computing, and arti<sup>fi</sup>cial intelligence in business forecasting.

![](/api/attachments/BHFPNN3K/fulltext/images/454e085cb9741d249159ecec4b6491e024ee57f051f10d3b57260e8d32fc3a68.jpg)

Operational Research Society, Omega, etc. He is a member of IEEE and INFORMS.

Tsan-Ming Choi (Jason) received his PhD in supply chain management from The Chinese University of Hong Kong. He is currently an assistant professor at The Hong Kong Polytechnic University. His current research interests mainly focus on supply chain management. Over the past few years, he has actively participated in a variety of research and consultancy projects in supply chain management. He has consulted companies such as Bossini, First Glory, and Sun-Hing Ltd. He has published in journals such as Computers and Operations Research, Decision Support Systems, European Journal of Operational Research, IEEE Transactions (various), International Journal of Production Economics, Journal of Industrial and Management Optimization, Journal of the
