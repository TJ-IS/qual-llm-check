---
otero_id: 14336
otero_key: "ZPH8QHPY"
title: "A demand forecast model using a combination of surrogate data analysis and optimal neural network approach"
authors: "H.C.W. Lau; G.T.S. Ho; Yi Zhao"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.12.008"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A demand forecast model using a combination of surrogate data analysis and optimal neural network approach

H.C.W. Lau <sup>a,</sup>⁎, G.T.S. Ho <sup>b</sup>, Yi Zhao b

<sup>a</sup> CInIS & School of Management, University of Western Sydney, Australia

<sup>b</sup> Department of Industrial and System Engineering, The Hong Kong Polytechnic University, Kowloon, Hong Kong

## a r t i c l e i n f o

Article history: Received 2 June 2010 Received in revised form 8 August 2012 Accepted 6 December 2012 Available online 14 December 2012

Keywords: Demand forecast Minimum description length (MDL) Optimal neural network Stochastic factors Surrogate data

## a b s t r a c t

As rough or inaccurate estimation of demands is one of the main causes of the bullwhip effect harming the entire supply chain, we have developed a mathematical approach, the minimum description length (MDL), to determine the optimal arti<sup>fi</sup>cial neural network (ANN) that can provide accurate demand forecasts. Two types of simulated customer and one practical demand are employed to validate the capability of the MDL method. Since stochastic factors hidden in the demand data disturb the prediction, the surrogate data method is proposed for identifying the characteristics of the demand data. This method excludes demands that are totally stochastic when forecasting. We demonstrate how optimal models estimated by MDL are consistent with the dynamics of demand data identi<sup>fi</sup>ed by the surrogate data method. The complementary approach of the surrogate data method and neural network constitutes a comprehensive framework for making various demand predictions. This framework is applicable to a wide variety of real-world data.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

The operation of the supply chain has undergone signi<sup>fi</sup>cant changes during the past decade [3]. Within the supply chain, enterprises usually adopt a strategy of having low inventories at all levels, including the end sale retailers, in order to reduce the their costs [22,27]. Meanwhile, the retailer sectors have to face uncertainties emerging in their supply chains. Customer demands depend on uncertain, stochastic factors, which make it dif<sup>fi</sup>cult for supply chain participants to give an accurate estimation of future demands. This issue would be further extended by variation ampli<sup>fi</sup>cation, known as bullwhip effect, and make the parties involved getting lost in inventory management by receiving faulted noti<sup>fi</sup>cation. Obviously, the extra stock keeping results in excess production at the upstream levels, since the producer aims to ful<sup>fi</sup>ll the over-estimated demand. Likewise, underestimated demand causes upstream players not producing enough quantity ful<sup>fi</sup>lling actual demand. Both scenarios lead to inef<sup>fi</sup>ciency in supply chain management. Thus, the challenge for a participant in the supply chain is to determine the appropriate quantity in terms of accurate demand forecast.

As the bullwhip effect has been recognized as a forecast-driven problem through supply chains, it is necessary to develop advanced techniques for forecasting customer demand and extend the visibility of customer demands as far as possible. However, doing an accurate and truthful demand forecasting is not straightforward and its dif<sup>fi</sup>- culty is that customer demands depend on many environmental factors while the pattern hidden in those demands is unknown or is too complicated for managers along supply chain to understand.

In this paper, an intelligent system based on the MDL-optimal neural network for “learning” the underlying pattern and predicting future demands is developed. Neural networks are considered as the primary and most popular technique for demand forecasting in supply chain management, and in particular the multi-layer feed-forward neural network is able to approximate any nonlinear or linear function under certain conditions [2,13,20]. Moreover, the high-degree of freedom in the neural network architecture provides the potential to model any function but, unfortunately, also results in a very high probability of over<sup>fi</sup>tting [38]. So the crucial issue in developing a neural network is the generalization of the network; however, being ignored in published works. An alternative novel approach is taken to determine the optimal neural network considering generalization and de<sup>fi</sup>ned as the MDL-optimal neural network for demand forecasting.

Furthermore, there is little in the literature that focuses on studying the nature of customer demand. Most articles about demand forecasting usually maintain that the given data should be predicted by using their approaches no matter whether the data is stochastic, linear or nonlinear and no matter whether the forecasting techniques are suitable for modeling the data or not. Actual demands depend on a lot of stochastic elements, which very probably result in the demands becoming completely stochastic. Meanwhile, some kinds of demand data in which deterministic patterns dominate appear to be random, and then people are very likely to ignore investigation of those demands. To address this issue, we employ the surrogate data method and examine the dynamics of the speci<sup>fi</sup>c simulated customer demands. We notice that the results of the surrogate data method are also con<sup>fi</sup>rmed by the MDL-optimal model. We, therefore, attempt to make use of the hypothesis testing with surrogated data method con<sup>fi</sup>rming the modeling technique so as to provide a comprehensive solution to problems of customer demand prediction in terms of identifying data feature, and selecting optimal network setting from one to another model. The contribution of the proposed techniques is also validated according to the performance in accuracy and <sup>fl</sup>exibility in comparison with commonly used mathematical approaches in experiments.

The rest of the paper is organized as follows: Section 2 contains a brief review of techniques of demand forecasting. This is followed by a description of the developed optimal neural network, as well as the surrogate data method for identifying data characteristics. In Section 4 the application of proposed technique is described and benchmarked with existing approaches through simulated models and a practical study. In the last section a conclusion on the approaches that have been developed is given and suggestions for future research are provided.

## 2. Literature review

Uncertainty in a supply chain can be de<sup>fi</sup>ned as unpredictable events that affect its planned performance [24]. Demand uncertainty, caused by inaccurate forecasting, feeds into the information exchange network, which in turn results in the bullwhip effect [30]. Such an effect may decrease the ability of the chain to meet the expected target for the delivery of products and services.

The bullwhip effect, also known as the Forrester or whiplash effect is one of the key areas of research in supply chain management (SCM) applications and its' typical cases could be found in the commercial operation of Campbell's Soup [15], HP and Proctor & Gamble [25], and a garment supply chain [12]. High inventory levels and poor customer services along the supply chain constitute symptoms of the bullwhip effect [9].

In terms of management science techniques, Yao, [39] Paik, and SeungKuk [31] identi<sup>fi</sup>ed demand forecasting as one of the signi<sup>fi</sup>cant variables for the bullwhip control, and Miyaoka found that improved forecasting could reduce <sup>fl</sup>uctuations in manufacturing production levels [29]. It is of vital importance as it has close relationship with reordering system [6], inventory cost [26], decision making [28], pro<sup>fi</sup>t maximization [18], etc. Gurnani et al. [18] found that retailers have to strike a balance between an accurate demand forecast and unit cost uncertainty before selling season starts. Different situations require different forecast models or methods. Sani and Kingsman [34] compared <sup>fi</sup>ve forecasting methods in terms of cost, service level and then both of them and found that they perform slightly different form each other. To forecast telephone demand in Australia and Chile, different techniques were also adopted by Bhattacharyya and Wellenius respectively [5]. Referring to above works, it can be concluded that optimal forecasting methods have to be designed or selected carefully [14].

To address this far-reaching factor, the moving average and the single exponential smoothing methods have been used by Graves [17] and Chen et al. [7,8]. Multiple correlations and a regression equation with weights can also be applied for optimal prediction [10]. It is a conventional technique in demand forecasting [33]. According to a comparative study, ANN can produce better predictions than with the Multiple Regression method [16].

As neural networks have been developed rapidly and are used widely in operations management [23,32,35]. Demand forecasting problems deploying this arti<sup>fi</sup>cial intelligent technique are studied following classi<sup>fi</sup>cation, simulation, and decision making. Hill et al. [21] stated that neural networks can perform signi<sup>fi</sup>cantly well in forecasting tasks. Possible reasons for poor forecast of classical decomposition are indenti<sup>fi</sup>ed and Hansen and Nelson [19] concluded that use of neural networks is a way out. More studies in comparing and combining traditional and neural network based forecasting methodology suggest that neural network can offer some improvement in performance and its feasibility of cooperation [11]. In this paper, we focus on how MDL-optimal neural networks approach for tackling linear and nonlinear simulated customer demand forecasting.

## 3. Framework of the MDL-optimal neural network model

Simulation logic, along with a <sup>fl</sup>owchart, is shown in Fig. 1. To verify that the program does actually perform as intended, the conceptual model is divided into three parts: demand generation, forecasting and calculation of prediction accuracy. The neural network used in this paper is the three-layer feedforward neural network, with a single hidden layer, sigmoid activation functions, and one linear output, as illustrated in Fig. 1. Given the input vector $\left( \boldsymbol { x } _ { t - 1 } , \boldsymbol { x } _ { t } \right.$ $\scriptstyle { 2 \cdots , X _ { t - d } } )$ the transfer function of the neural network, f can be mathematically expressed as

$$
f \left(x _ {t - 1}, x _ {t - 2}, \dots , x _ {t - d}\right) = b _ {0} + \sum_ {i = 1} ^ {k} v _ {i} \phi \left(\sum_ {j = 1} ^ {d} \omega_ {i, j} x _ {t - j} + b _ {i}\right)\tag{1}
$$

where $\{ \nu _ { i } , \omega _ { i , j } , b _ { i } \}$ are weights and biases respectively, ϕ is the tan-sigmoid transfer function, k is the number of neurons, and d is the number of inputs. The Levenberg–Marquardt algorithm is used to train the neural network.

Over<sup>fi</sup>tting has long been recognized as an endemic problem to neural networks having a number of parameters. The biological nature for ANN (i.e. a massive highly connected array of nonlinear excitatory “neurons”) promotes the construction of neural networks with a large number of neurons. Correspondingly the resulting models easily become over<sup>fi</sup>tting. Therefore, the adequate generalization of ANN for a speci<sup>fi</sup>c application is a primary element to ensure successful application in practice. We, therefore, utilize a novel approach, MDL, to directly determine the optimal neural network (i.e. the number of neurons in the neural network) with the focus on prediction accuracy.

## 3.1. The minimum description length

The MDL principle is based on the trade-off strategy to estimate the optimal model according to the minimum of total description length. The description length of a model is composed of two parts: the cost describing both the model parameters, and its prediction errors.

De<sup>fi</sup>nition 1. N(s) is the description length of parameters of a neural network, whose neuron number is s.

De<sup>fi</sup>nition 2. E(s) is the description length of the prediction error of the same model.

The total description length with respect to this model, denoted by $D ( s ) ,$ , is then given by the sum of both parts. The MDL principle states that the optimal model is the one that minimize D(s).

Let $\{ d _ { i } \} _ { i = 1 } ^ { N }$ be customer demands of N time units (for example weeks) and $f ( d _ { i - 1 } , d _ { i - 2 } , . . . , d _ { i - k } ; \Lambda _ { s } )$ be a prediction of the neural network given of the previous k inputs and neural network parameters Λ with respect to s neurons. The prediction error at the ith time unit is then given by $e _ { i } { = } f ( d _ { i - 1 } , d _ { i - 2 } , { \ldots } , d _ { i - k } ; \Lambda _ { s } ) - d _ { i } .$ . So the description length of the neural network $f ( { \bf \cdots } , \Lambda _ { s } )$ is given by the description length of all the parameters Λ [40]:

$$
N (s) = L (\Lambda_ {s}) = \sum_ {j = 1} ^ {s} \ln \frac {\gamma}{\delta_ {j}}\tag{2}
$$

![](/api/attachments/ZPH8QHPY/fulltext/images/ae87a0ac0aea6cf17abf73388fa463d5e66694db2dbe58a8809c3231ad88f8f8.jpg)  
Fig. 1. Flowchart of simulation model.

where γ is a constant. $\big ( \delta _ { 0 } , \delta _ { 1 } , . . . , \delta _ { s } \big )$ are de<sup>fi</sup>ned as the solution of

$$
\left(Q \left[ \begin{array}{c} \delta_ {0} \\ \delta_ {1} \\ \delta_ {2} \\ \vdots \\ \delta_ {k} \end{array} \right]\right) _ {j} = \frac {1}{\delta_ {j - 1}}\tag{3}
$$

where Q is the second derivative of E(s) and (⋅) denotes the jth element of the vector (⋅) [40].

E(s) is the negative logarithm of the likelihood of the errors $e =$ $\{ e _ { i } \} _ { i = 1 } ^ { N }$ under the given probability distribution of those errors. With the assumption that these errors follow the standard Gaussian distribution the description length of model prediction errors is approximated by [40]

$$
E (s) = \frac {N}{2} + \ln \left(\frac {2 \pi}{N}\right) ^ {N / 2} + \ln \left(\sum_ {i = 1} ^ {N} e _ {i} ^ {2}\right) ^ {N / 2}.\tag{4}
$$

In this paper we further study the prediction of customer demands by using the related environmental processes. Since the end customer demand is related to many environmental factors the end customer demand can be regarded as an unknown function with respect to those factors. Given the time series of K environment factors at the jth time unit as the inputs, $\lbrace p _ { i j } \rbrace _ { i = 1 } ^ { K } ,$ the neural network gives its prediction, $f ( p _ { 1 } ^ { j } , p _ { 2 } ^ { j } , . . . , p _ { K } ^ { j } ; \varLambda _ { s } )$ and correspondingly the prediction error at the jth time unit $e _ { i } { = } f ( p _ { 1 } ^ { j } , p _ { 2 } ^ { j } , { \ldots } , p _ { K } ^ { j } ; \Lambda _ { s } ) - d _ { i }$ . We then employ equations for M(s) and E(s) to compute the description length of the neural network in this scenario.

## 3.2. Surrogate data method

The surrogate data method was suggested and standardized by Theiler [37]. The rationale for surrogate data hypothesis testing is to generate an ensemble of surrogate data (surrogates in short) that preserve certain properties of the original data (i.e. consistent with some null hypotheses) [36].

There are three typical null hypotheses, NH0 (the data is random noise), NH1 (the data is linearly <sup>fi</sup>ltered noise) and NH2 (the data is a static monotonic nonlinear transformation of linearly <sup>fi</sup>ltered noise) [42]. Correspondingly, Algorithm 0, Algorithm 1, and Algorithm 2 produce surrogates that are consistent with these hypotheses. One then applies some test statistic to both the surrogates and the original data. If the test statistic value for the data is out of the distribution formed by values estimated for the surrogates, the given hypotheses is rejected as being the likely origin of the data. If the statistical value for the data is in the distribution formed from surrogates, this suggests that the data is consistent with the given hypotheses.

For example, we test the demand data against the hypothesis of NH1. That is, we wish to examine whether the demand data we are interested in originates from the linear process. If so, the linear model is more suitable to model such data. So the surrogate data method acts as a guide to the next modeling technique. We then notice whether the optimal neural network selected by the MDL is equivalent to a linear model so as to further validate the capability of our model selection technique. If the given data is consistent with the nonlinear process nonlinear modeling techniques, like neural networks should outperform the linear counterparts. However, nonlinear models are sensitive to data sets and more easily become over<sup>fi</sup>tted than do linear models. We then observe whether the MDL-optimal model can avoid over<sup>fi</sup>tting and can provide an accurate prediction. This is discussed at length in the next section.

## 4. Experimental results

First of all, the customers follow a linear demand process with seasonal swings. The customer demands in the simulation model are generated using the following formula [41],

$$
D _ {t} = (b a s e (t) + s l o p e (t)) * \left(\left[ \frac {\text { season } (t) + \text { period } (2 \pi / 5 2 * t)}{\text { season } (t)}\right) + \text { noise } * \text { rand\_normal } (\cdot), \right.\tag{5}
$$

where $D _ { t }$ is the demand at the tth week, rand \_normal(⋅) is a standard normal random generator between zero and one, noise represents the amplitude of the contaminated normal random noise, and base, slope, period and season are variable coef<sup>fi</sup>cients concerned with the time, a week.

The same form is also used by Bayraktar et al. [4] but they set base, slope and season with constants. The underlying tendency in their simulated data is easy to follow so we replace them with timevariant coef<sup>fi</sup>cients and add stochastic factors into the generation of these coef<sup>fi</sup>cients. The <sup>fl</sup>uctuation of base and peaks of slope randomly appear, and the variable, season, is added with strong random noise, all of which are tried to re<sup>fl</sup>ect the practical factors. Finally, the generated customer demand is more dif<sup>fi</sup>cult to forecast.

Base, slope, season and period are speci<sup>fi</sup>ed by the simulated data, as shown in Fig. 2. These four data sets contaminated with observational noise simulate practical environmental factors related to the customer demand. Then the demand data per week is generated using the given formula above. In order to examine the suitability of MDL approach to forecast demand, some forecasting techniques, MSE-optimal neural network, exponential smoothing and multiple regressions, would be taken as comparison.

## 4.1. Identification of stochastic customer demands

Prior to the prediction of the simulated customer demands, it is necessary to determine whether the given data is predictable or not. It is not signi<sup>fi</sup>cant to make a prediction of customer demands which are consistent with stochastic noise. The surrogate data method with the hypotheses of NH0 and NH1 is used to test the dynamic property of the given demand data (i.e. predictability and linear property). The results are presented in Fig. 3.

100 surrogates of the original customer demand are generated, which are consistent with NH0 and NH1. One popular statistical criterion, complexity [42], is applied to the given simulated data. Green bars in Fig. 3 show the probability distribution of statistical values for all the surrogates; and the red star is the complexity of the original demand. Note that the complexity of the original time series is not shown in the top panel of Fig. 3, as its value is far away from the range of the surrogates' results (i.e. 0.99–1.10).

Gaussian distribution is employed to <sup>fi</sup>t the distribution of statistical values for surrogate data. With this known distribution, we can determine the con<sup>fi</sup>dence level of rejecting the given hypothesis. The central limit theorem proves that a large number of independent surrogates are distributed approximately normally. The normal distribution is appropriate for modeling the distribution of statistical values of surrogates as 100 surrogates are generated independently.

We observe that the complexity of the original demand data is even larger than the mean of the <sup>fi</sup>tted Gaussian distribution plus its three-time standard deviation. It, therefore, suggests that the given customer demand is inconsistent with random noise, with almost 100% con<sup>fi</sup>dence probability. Furthermore, in the bottom panel the statistical value of the original demand data is in the center of the distribution of the surrogates. This result indicates that the given customer demand is consistent with linear dynamics. Thus both conclusions indicate that the given data itself is not of a stochastic character and is suitable for prediction by linear modeling techniques.

![](/api/attachments/ZPH8QHPY/fulltext/images/8147e87604d9430f02aea62c0c7c69aa32102720d45958aab44694c93e41a5a6.jpg)

![](/api/attachments/ZPH8QHPY/fulltext/images/92998778187f4b0516b7688749269e13a123901813a952c22e9bee9cd02f28cb.jpg)

c  
![](/api/attachments/ZPH8QHPY/fulltext/images/b49061491c2d99dab66f0a615fc817d2925b61d1b1952355237898e419d1c70e.jpg)

d  
![](/api/attachments/ZPH8QHPY/fulltext/images/eca535c4501c6c7096f40377a8ac93ad40e24dc46c6b0729248db371eb2ca18f.jpg)  
Fig. 2. Time series of environmental factors, base (a), slope (b), season (c) and period (d).

![](/api/attachments/ZPH8QHPY/fulltext/images/c46dd589d74cdf059cd95da88a49555c029a2a5bc8083e1720488f13cc544af3.jpg)

![](/api/attachments/ZPH8QHPY/fulltext/images/044c1a96b40a595ac1bb31a2b191488b33d716e8e32148b07822456f14103aa0.jpg)  
Fig. 3. Application of the surrogate data method with hypotheses of NH0 (top panel) and NH1 (bottom panel) to the simulated demand data.

## 4.2. Prediction of customer demands with historical demands

Various neural networks are employed with one to twenty neurons to forecast the demand data generated by the formula above, of which the <sup>fi</sup>rst 400 points are selected to train the network, and the rest are the test data. Typical predictions obtained by the neural networks with one, <sup>fi</sup>ve, seven, ten, sixteen, and nineteen neurons are listed in Fig. 4, where the red curves are the prediction and the blue curves are the original demand. The neural network with only one neuron predicts exactly the future customer demand. Note that some predicted values are negative, as shown in Fig. 4(c) and (d) since they are obtained automatically by the given neural network. The negative values indicate that the neural network has become over<sup>fi</sup>tted. The description length curve of all twenty neural networks is shown in Fig. 5. The neural network candidate with one neuron minimizes the description length and thereby this neural network is the MDL-optimal model. The neural network with one neuron is equivalent to a linear model. It conforms to the previous conclusion taken by the surrogate data method that the linear model is suitable for predicting the given simulated demand.

![](/api/attachments/ZPH8QHPY/fulltext/images/b631d9e2f9b57f6e64a13845b5170d6c2eb78453e5abdaae1de93991f2044d31.jpg)

![](/api/attachments/ZPH8QHPY/fulltext/images/dfb2c7afae320988523803ba46ab2f9a9003a4e36afd9cd60427fedc34cf6ee1.jpg)

![](/api/attachments/ZPH8QHPY/fulltext/images/0eedffe1d42d3d321fcf9563e7f6ddf769fea3d95fab38ac333354cbf86b1cf6.jpg)

![](/api/attachments/ZPH8QHPY/fulltext/images/395ee240268e7e1f598c8c09091609fe45927bd43b9b54a255ee0ac2d5ecbecb.jpg)

![](/api/attachments/ZPH8QHPY/fulltext/images/9f9585ba51061a3606f2446bded8a0500fb6a2539570d3a39e3c3c8fc98995dc.jpg)

![](/api/attachments/ZPH8QHPY/fulltext/images/6736475003b4d0c4954e7ae004892af1ac9e332e4fd69f1c654322541b2ec42f.jpg)  
Fig. 4. Prediction of various neural networks of the customer demands by using historical demand data.

Here the standard deviation of the test data is set as the threshold for assessing the accuracy of the prediction. It means that if the deviation between the original data and its prediction is lower than the threshold, this prediction is regarded as an accurate one; otherwise, it is an inaccurate prediction. Finally, a curve of the prediction accuracy for all twenty models is achieved, as shown in the bottom panel of Fig. 5. Again, the MDL-optimal model gives the most accurate prediction.

As a comparison, we illustrate the mean square errors of the training and test data, as presented in Fig. 6. The mean square errors of the training data keep decreasing while the mean square errors of the test data keep increasing, with <sup>fl</sup>uctuations. The presence of mean square errors indicates that the neural networks with more neurons are inclined to become over<sup>fi</sup>tted but it cannot estimate the optimal neural network. The mean square errors in the test data can be regarded as evidence of over<sup>fi</sup>tting, rather than a criterion for model selection.

The performance among selected forecasting techniques is given in Table 1, with negligible mean-square errors for the four methods, it is found that neural network approach got slightly better prediction comparing to those of exponential smoothing and multiple regression with overall accuracy about 0.8.

## 4.3. Prediction of customer demands with environmental factors

The records of base, slope, season and period are fed to the neural network to give the corresponding demand data. Obviously, the generation of demand data is a simple linear function with respect to these parameters. Using the environmental factors related to the practical customer demand is the best way to forecast such demand.

![](/api/attachments/ZPH8QHPY/fulltext/images/b92611b1f605892b26fcbb7b95b74909bb3ad354d7ef2b552c34627aca6cc3ec.jpg)

![](/api/attachments/ZPH8QHPY/fulltext/images/acb3c6775c70eee35c97a69fbe9dbde7f64b2738436e803ae5be46042bc05df3.jpg)  
Fig. 5. Description length and prediction accuracy of the twenty neural networks when employing historical demand data

![](/api/attachments/ZPH8QHPY/fulltext/images/fcf34a9ee10ca8d88e30da27cf47b57b592f21869b4c640abb3f7df01f5cb330.jpg)

![](/api/attachments/ZPH8QHPY/fulltext/images/99d826b6950eb3b4f2fe55d26bca7659e337ca06d7359ce2f3e7e47827814fc8.jpg)  
Fig. 6. Mean square errors of both the training (the top panel) and test data (the bottom panel) for all the twenty neural networks.

Fig. 7 gives the description length curve of twenty neural networks and their prediction accuracy.

The description length curve shows that for the same type of simulated demand data, the MDL-optimal neural network is also the neural network candidate with one neuron, which achieves the highest prediction accuracy. The curve expression in Fig. 7 and calculated mean square error also show that over<sup>fi</sup>tting occurs in the network models with more than one neuron. Hence, the MDL-optimal model can provide an accurate prediction for the linear demand data in both scenarios.

Under the effect of environmental factors, computations, again, Table 2 shows that MDL-optimal neural network performed the best among the four speci<sup>fi</sup>ed demand forecasting methods. It is deserved to mention that prediction accuracy with environmental factors of

Table 1  
Prediction accuracy of customer demands with historical demands.

<table><tr><td></td><td>MDL-optimal NN</td><td>MSE-optimal NN</td><td>Exponential smoothing</td><td>Multiple regression</td></tr><tr><td>MSE</td><td> $1.75 \times 10^{-3}$ </td><td> $1.51 \times 10^{-3}$ </td><td> $3.46 \times 10^{-3}$ </td><td> $4.31 \times 10^{-3}$ </td></tr><tr><td>Prediction accuracy</td><td>0.88</td><td>0.84</td><td>0.77</td><td>0.78</td></tr></table>

MDL-optimal neural network is about 37% and 20% higher than those of exponential smoothing and multiple regressions respectively.

## 4.4. Prediction of nonlinear customer demands

We now introduce a chaotic time series, the Ikeda map, which appears to be periodic. The equation of the Ikeda map is given by

$$
\left\{ \begin{array}{c} x _ {n + 1} = 1 + \mu (x _ {n} \cos t _ {n} - y _ {n} \sin t _ {n}) \\ y _ {n + 1} = \mu (x _ {n} \sin t _ {n} + y _ {n} \cos t _ {n}) \end{array} \right.,\tag{6}
$$

where $\mu { = } 0 . 7$ and $t _ { n } { = } 0 . 4 { - } 6 / ( 1 + x _ { n } ^ { 2 } + y _ { n } ^ { 2 } ) .$

It is known that with the parameters above, the data generated is nonlinear. Certainly, other known nonlinear data can also be used. Here we choose the x-component data of the Ikeda map denoted by Ikeda\_x. We, therefore, simulate the nonlinear demand by using the formula, $D _ { t } =$ base+slope+season+Ikeda \_x.

The base, slope and season are the same as those of the previous function, and are contaminated with stochastic noise. The demand that is generated is also a linear function with respect to these four coef<sup>fi</sup>cients, but the data itself is nonlinear. The simulated nonlinear demand data is tested by the surrogate data method, as shown in Fig. 8. The dashed curves are a Gaussian distribution <sup>fi</sup>tted to the distribution of two kinds of surrogates. In the <sup>fi</sup>gure, the statistical value of the original simulated demand data is 0.721, which is lower than the mean of complexity of surrogates minus their standard deviation. We, therefore, conclude that the given demand data is not random noise, and not suitable for linear models.

![](/api/attachments/ZPH8QHPY/fulltext/images/f518ef5e5a199d245ab81f6467f91144b2699198f5ecf4989151fcdf618e6298.jpg)

![](/api/attachments/ZPH8QHPY/fulltext/images/aff2e5adcabd398d6d183699d3e82f81b24c5fcb7740f481fd03b23c0ab88758.jpg)  
Fig. 7. Description length and prediction accuracy of the twenty neural network candidates, using environmental factors.

We also generate 500 points of this system, of which 400 points are selected as training data and the rest are used as testing data. Typical predictions obtained by neural networks with one, <sup>fi</sup>ve, nine, thirteen, sixteen, and twenty neurons are presented in Fig. 9, where the denotation of curves is the same as that in Fig. 4. The description length of these twenty neural network candidates is plotted in the top panel of Fig. 10 and the bottom panel shows the accuracy of the predictions.

Table 2  
Prediction accuracy of customer demands with environmental factors

<table><tr><td></td><td>MDL-optimal NN</td><td>MSE-optimal NN</td><td>Exponential smoothing</td><td>Multiple regression</td></tr><tr><td>MSE</td><td> $3.33 \times 10^{-3}$ </td><td> $3.18 \times 10^{-3}$ </td><td> $7.56 \times 10^{-3}$ </td><td> $7.40 \times 10^{-3}$ </td></tr><tr><td>Prediction accuracy</td><td>0.85</td><td>0.84</td><td>0.62</td><td>0.71</td></tr></table>

Referring to Fig. 10, the MDL-optimal neural network is the neural network candidate with <sup>fi</sup>ve neurons, which achieves the highest prediction accuracy of all. From Fig. 9, we observe that the MDL-optimal neural network accurately predicts the demand of the next customer. The neural network with one neuron cannot capture the underlying dynamics of this demand data although the amplitude of prediction is lower than the original one (i.e. the variance of the prediction is also lower than that of the original).

While comparing all results of prediction accuracies, the accuracy of MDL-optimal neural network is as high as 0.92 which is also approximately 1.4 times of those of exponential smoothing and multiple regressions as shown in Table 3.

We also implement the prediction for this nonlinear demand data by using the four coef<sup>fi</sup>cients. As we expected, the description length curve shows the neural network with one neuron is the optimal model in this case. For the sake of brevity, we do not show these <sup>fi</sup>gures. In addition, we replace the time series of the Ikeda map with the periodic data and then repeat the prediction in the same way. We notice that the MDL-optimal model as well as the other models fails to follow the future tendency of the demand data. This suggests that one should be cautious when using environmental factors which are possibly related to customer demands when making predictions. It is quite dif<sup>fi</sup>cult to identify the environmental factors that affect customer demands, and wrong employment of irrelevant environmental records would result in poor predictions. In contrast, prediction using historical demand data is preferable but it is suggested that the data characteristics be investigated prior to the prediction by using the surrogate data method, as discussed in this section.

![](/api/attachments/ZPH8QHPY/fulltext/images/e4c95492d6a9cf58a3cfbb9ca3dc44c2938505e96985da262023f47597cb67ba.jpg)

![](/api/attachments/ZPH8QHPY/fulltext/images/51bda6a8abd70f2d3bd5471502f6e9d7c5c13f4a793db30adaad0331fcadad52.jpg)  
Fig. 8. Application of the surrogate data method with hypotheses of NH0 (the top panel) and NH1 (the bottom panel) to the nonlinear demand data.

## 4.5. Prediction of practical demand data

Here we employ the practical demand data, Monthly gasoline demand Ontario gallons in millions from 1960 to 1975, to validate the proposed modeling technique and the framework [1]. We follow the same procedure as in previous cases. The surrogate data method,

![](/api/attachments/ZPH8QHPY/fulltext/images/732644ea5f14e1a973d81e2186759bb59c0d76f41d5ef1de492604d7d03010d0.jpg)

![](/api/attachments/ZPH8QHPY/fulltext/images/de673f5ea426c89a484ed3b506c2ede08bc996cc582ae96d9af31e1ce0d468c7.jpg)

![](/api/attachments/ZPH8QHPY/fulltext/images/f7e57d08661f583e25902c5784df6000d2952addf2346f5171c1668625551aa8.jpg)

![](/api/attachments/ZPH8QHPY/fulltext/images/5675238d7553789b24a0c5f44495b26f0960c0e7fca998b3ead00b6fa9a02698.jpg)

![](/api/attachments/ZPH8QHPY/fulltext/images/25ecabbd0c6bb8b9cfd30434f5fb43c776bb08051e48e2a834425f8ea42138c2.jpg)

![](/api/attachments/ZPH8QHPY/fulltext/images/5817f56e611bf2d1339cbc7b5bc42eb1b9886b9288357e9a3f6ad58e26de275c.jpg)  
Fig. 9. Prediction of various neural networks of nonlinear customer demands by using historical demand data

![](/api/attachments/ZPH8QHPY/fulltext/images/8eecdd071cdf17534a63f01381d1f5e45d36f6528435a3845a26647987aaa18a.jpg)

![](/api/attachments/ZPH8QHPY/fulltext/images/f4fc73bbd6d60d5a327542acf0447827145503d2902c2964301c0aab0ccac66a.jpg)  
Fig. 10. Description length of twenty neural networks and their prediction accuracy.

as shown in Fig. 11, suggests, with a weak con<sup>fi</sup>dence level that the practical demand data is consistent with the linear process.

There are 192 data points, of which 102 points are selected to train neural networks and the rest are used as testing data. Typical predictions obtained by various neural networks including the MDL-optimal one are presented in Fig. 12. We observe that the MDL-optimal neural network overwhelms the other candidates. Fig. 13 exhibits the description length of these twenty neural network candidates and their prediction accuracy which suggests that MDL is the optimal model.

Table 3  
Prediction accuracy of nonlinear customer demands.

<table><tr><td></td><td>MDL-optimal NN</td><td>MSE-optimal NN</td><td>Exponential smoothing</td><td>Multiple regression</td></tr><tr><td>MSE</td><td>10.10</td><td>7.69</td><td>13.02</td><td>9.62</td></tr><tr><td>Prediction accuracy</td><td>0.92</td><td>0.85</td><td>0.64</td><td>0.69</td></tr></table>

According to Table 4, we can <sup>fi</sup>nd that MDL-optimal neural network, still, performed the best with prediction accuracy 0.84. It is of 31%, 50% and 55.6% higher correspondingly. It is noticed that the large scale historical demand causes relatively large MSEs. In conclusion, MDL-optimal neural network shows its high accuracy and adoptability in different perspectives mentioned.

## 5. Conclusion

This study has provided an analysis of the impact of the neural network forecasting technique when dealing with a linear demand structure with seasonal swings, and also with a non-linear demand structure. Although earlier researchers examined analytically a similar demand forecasting problem [4] they did not consider the dynamic properties of the demand data in their prediction. The complementary approach developed here examines the characteristics of several demand processes by using statistical hypothesis testing in order to exclude totally stochastic demands from being used for the purpose of prediction.

![](/api/attachments/ZPH8QHPY/fulltext/images/ee79debf34d6fe0cdbf99702357bd507da16d3ae76a1101ce94576f50d13ba3e.jpg)  
Fig. 11. Application of the surrogate data method with hypotheses of NH1 to the practical monthly gasoline demand (the star represents the complexity of the original demand).

Based on the simulation analysis, this study notes a highly signi<sup>fi</sup>- cant <sup>fi</sup>nding that the method of description length can be adapted so that it can be used to select the optimal neural network that is consistent with the demand structure identi<sup>fi</sup>ed by the surrogate data method. The MDL-optimal neural networks give accurate predictions for typical demand data outperforming its counterparts. The surrogate data method and the MDL method con<sup>fi</sup>rm each other by their <sup>fi</sup>ndings. The proposed framework of both methods gives an insight into various demand predictions. Here we do not consider the ordering policy in the supply chain. Neither has an up-to replenishment policy been considered, that is, one in which the stocks in the retail sectors are kept “up to” a certain level by replenishing products consumed by customers (i.e. their demands). Obviously, the MDL method that has been developed, as well as the MDL-optimal neural network are also applicable to other replenishment policies in those scenarios by ensuring that predictions are accurate.

This study may further be extended as a way of assessing the impact of the bullwhip effect on the performance measures of the supply chain (e.g., total inventory cost and service level of the chain). Given the fact that bullwhip effect has a deteriorating impact

![](/api/attachments/ZPH8QHPY/fulltext/images/46667f7ed51fca865d26b7ee4fc57da6ded9331bc78c7c867a5e95fbb448b8b7.jpg)

![](/api/attachments/ZPH8QHPY/fulltext/images/ce17710be4158727eaf3fd8f0e0ddafd3bdfea6e8c0124fea6cdf0dcf197937f.jpg)

![](/api/attachments/ZPH8QHPY/fulltext/images/80e6244d1f588c4c3a11b44f37acaa6967d7003fa6eb25522b571aedda5a06b2.jpg)

d  
![](/api/attachments/ZPH8QHPY/fulltext/images/3b37e1fb84fd1724b81ee6f2d263dd1489f267e48ace0d7bb577f645f4436c84.jpg)

![](/api/attachments/ZPH8QHPY/fulltext/images/4c8e136acca4dc1434057a1c3f0ef2502003eee64d8c61816cea32bf441c54ad.jpg)

![](/api/attachments/ZPH8QHPY/fulltext/images/81a0372e41c74fc33fe0f0c580fd3bbc7bbc530cd2e4ab2ab509690fd111e2d0.jpg)  
Fig. 12. Prediction of various neural networks on the practical demands by using historical demand data

![](/api/attachments/ZPH8QHPY/fulltext/images/602eeb4d7ecb927438bb466a98798af3aa34b15ed0201ae1f29fb2b34a9d5fb5.jpg)

![](/api/attachments/ZPH8QHPY/fulltext/images/72f7d7430e93faabe748d3b5b434c7c7f7a71e327d58206779a55b6ef5cb6ca2.jpg)  
Fig. 13. Description length of twenty neural networks and their prediction accuracy.

on the operation cost of the whole chain, the direct relationship between the bullwhip effect and the performance of the proposed prediction techniques is an interesting area for future research. In addition, the structural con<sup>fi</sup>guration of the prediction system is suggested as a way to integrate various modules/techniques so as to enhance the ef<sup>fi</sup>ciency of the whole system.

## Acknowledgment

The authors wish to thank the Research Committee of the Hong Kong Polytechnic University and the CInIS research group of University of Western Sydney for their support of this project.

Table 4  
Prediction accuracy of practical demand data

<table><tr><td></td><td>MDL-optimal NN</td><td>MSE-optimal NN</td><td>Exponential smoothing</td><td>Multiple regression</td></tr><tr><td>MSE</td><td> $1.48 \times 10^{4}$ </td><td> $1.03 \times 10^{4}$ </td><td> $4.76 \times 10^{4}$ </td><td> $6.02 \times 10^{4}$ </td></tr><tr><td>Prediction accuracy</td><td>0.84</td><td>0.64</td><td>0.56</td><td>0.54</td></tr></table>

## References

[1] B. Abraham, J. Ledolter, Statistical Methods for Forecasting, John Wiley, New York, 1983.

[2] L. Aburto, R. Webber, Demand forecast in a supermarket using a hybrid intelligent system, in: Design and application of hybrid intelligent systems, IOS, Berlin, 2003.

[3] L. Aburto, R. Webber, Improved supply chain management based on hybrid demand forecasts, Applied Soft Computing 7 (Jan. 2007) 136–144.

[4] E. Bayraktar, S. Kohb, A. Gunasekaran, K. Sari, E. Tatoglu, The role of forecasting on bullwhip effect for E-SCM applications, International Journal of Production Economics 113 (2008) 193–204

[5] M.N. Bhattacharyya, Forecasting the demand for telephones in Australia, Journal of the Royal Statistical Society: Series C: Applied Statistics 23 (1) (1974) 1–10.

[6] M. Caputo, V. Mininno, Internal, vertical and horizontal logistics integration in Italian grocery distribution International Journal of Physical Distribution and Logistics Management 26 (9) (1996) 64–90.

[7] F. Chen, J.K. Ryan, D. Simchi-Levi, The impact of exponent trial smoothing forecasts on the bullwhip effect, Naval Research Logistics 47 (2000) 269–286.

[8] F. Chen, Z. Drezner, J.K. Ryan, D. Simchi-Levi, Quantifying the bullwhip effect in a simple supply chain: the impact of forecasting, lead times, and information, Management Science 46 (3) (2000) 436–443.

[9] S. Chopra, P. Meindl, Supply Chain Management, Prentice-Hall, Englewood Cliffs, NJ, 2001.

[10] J. Cohen, Multiple regression as a general data-analytic system, Psychologica Bulletin 70 (6) (1968) 426–443.

[11] M.C.M. de Carvalho, M.S. Dougherty, A.S. Fowkes, M.R. Wardman, Forecasting travel demand: a comparison of logit and arti<sup>fi</sup>cial neural network methods, The Journal of the Operational Research Society 49 (7) (1998) 717–722.

[12] S.M. Disney, D.R. Towill, The effect of vendor managed inventory (VMI) dynamics on the bullwhip effect in supply chains, International of Production Economics 85 (2003) 199–215.

[13] J. Faraway, C. Chat<sup>fi</sup>eld, Time series forecasting with neural networks: a comparative study using the airline data, Applied Statistics 47 (2) (1998) 231–250.

[14] R. Fildes, Evaluation of aggregate and individual forecast method selection rules, Management Science 35 (9) (1989) 1056–1065.

[15] M. Fisher, J. Hammond, W. Obermeyer, A. Raman, Con<sup>fi</sup>guring a supply chain to reduce the cost of demand uncertainty, Production and Operations Management 6 (1997) 211–225.

[16] I. Flood, A neural network appraoch to the sequencing of construction tasks, in: Proceedings of the 6th International Symposium on Automation and Robotics in Construction, Construction Industry Institute, Austin, TX, 1989, pp. 204–211.

[17] S.C. Graves, A single-item inventory model for a non-stationary demand process, Manufacturing and Service Operations Management 1 (1) (1999) 50–61.

[18] H. Gurnani, C.S. Tang, Optimal ordering decisions with uncertain cost and demand forecast updating, Management Science 45 (10) (1999) 1456–1462.

[19] J.V. Hansen, R.D. Nelson, Forecasting and recombining time-series components by using neural networks, The Journal of the Operational Research Society 54 (3) (2003) 307–317.

[20] T. Hill, M. O'Connor, W. Remus, Neural networks for time series forecasts, Management Science 42 (7) (1996) 1082–1092.

[21] T. Hill, M. O'Connor, W. Remus, Neural networks models for time series forecasts, Management Science 42 (7) (1996) 1082–1092.

[22] R.H. Hollier, K.L. Mak, K.K. Lai, Computing optimal (s, S) policies for Inventory systems with a cut-off transaction size and the option of joint replenishment, International Journal of Production Research 40 (14) (2002) 3375–3389.

[23] H. James, Software for studying and developing applications of arti<sup>fi</sup>cial neural networks, The Economic Journal 104 (422) (1994) 181–196.

[24] S. Koh, A. Gunasekaran, A knowledge management approach for managing uncertainty in manufacturing, Industrial Management and Data Systems 106 (2006) 439–459.

[25] H. Lee, V. Padmanabhan, W. Seungjin, The bullwhip effect in supply chains, Sloan Management Review 38 (1997) 93–102.

[26] W. Liang, C. Huang, Agent-based demand forecast in multi-echelon supply chain, Decision Support Systems 42 (1) (2006) 390–407.

[27] J.M. Masters, Determination of near optimal stock levels for multi-echelon distribution inventories, Journal of Business Logistics 14 (2) (1993) 165–195.

[28] R. Metters, Quantifying the bullwhip effect in supply chains, Journal of Operations Management 15 (2) (1997) 89–100.

[29] J. Miyaoka, W. Hausman, How a base stock policy using ‘stale’ forecasts provides supply chain bene<sup>fi</sup>ts, Manufacturing and Service Operations Management 6 (2) (2004) 149–162.

[30] T. Moyaux, B. Chaib-draa, S. D'Amours, Information sharing as a coordination mechanism for reducing the bullwhip effect in a supply chain, IEEE Transactions on Systems, Man, and Cybernetics Part C 37 (3) (2007) 396–409.

[31] S.K. Paik, Analysis of the causes of ‘bullwhip’ effect in a supply chain: A simulation approach, Ph.D. Dissertation, The George Washington University, 2003.

[32] N.C. Proudlove, Intelligent management systems in operations: a review, The Journal of the Operational Research Society 49 (7) (1998) 682–699.

[33] M. Ranasinghe, G.B. Hua, T. Barathithaasan, A Comparative Study of Arti<sup>fi</sup>cial Neural Networks and Multiple Regression Analysis in Estimating Willingness

to Pay for Urban Water Supply, Department of Civil Engineering, University of Moratuwa, Sri Lanka, 2001.

[34] B. Sani, B.G. Kingsman, Selecting the best periodic inventory control and demand forecasting methods for low demand items, The Journal of the Operational Research Society 48 (7) (1997) 700–713.

[35] S. Schocken, G. Ariav, Neural networks for decision support: problems and oppor tunities, Decision Support Systems 11 (5) (1994) 393–414.

[36] M. Small, C.K. Tse, Detecting determinism in time series: the method of surrogate data, IEEE Transactions on Circuits and Systems I 50 (2003) 663–672.

[37] J. Theiler, S. Eubank, A. Longtin, B. Galdrikian, J.D. Farmer, Testing for nonlinearity in time series: the method of surrogate data, Physica D: Nonlinear Phenomena 58 (1–4) (1992) 77–94.

[38] J.M. Twomey, A.E. Smith, Bias and variance of validation methods for function approximation neural networks under conditions of sparse data, IEEE Transactions on Systems, Man, and Cybernetics Part C 28 (3) (1998) 417–430.

[39] D.Q. Yao, Study of bullwhip effect and channel design in supply chains, Ph.D. Dissertation, the University of Wisconsin-Milwaukee, 2001.

[40] Y. Zhao, M. Small, Minimum description length criterion for modeling of chaotic attractors with multilayer perception networks, IEEE Transactions on Circuits and Systems I 53 (3) (2006) 722–732.

[41] X. Zhao, J. Xie, J. Leung, The impact of forecasting model selection on the value of information sharing in a supply chain, European Journal of Operational Research 142 (2002) 321–344.

[42] Y. Zhao, J.F. Sun, M. Small, Evidence consistent with deterministic chaos in human cardiac data: surrogate and nonlinear dynamical modeling, International Journal of Bifurcation and Chaos 18 (2) (2008) 141–160

H.C.W. Lau received his M.Sc. degree from Aston University, Birmingham U.K., in 1981 and the Ph.D. degree from the University of Adelaide, Adelaide, Australia, in 1995. He is currentl an Associate Professor with the Department of Industrial and Systems Engineering Hong Kong Polytechnic University, involved in research and teaching activities. His current research areas cover manufacturing, data management, work<sup>fl</sup>ow automation, and arti<sup>fi</sup>cial intelligence applications.

G.T.S. Ho received his Bachelor degree and PhD at the Hong Kong Polytechnic University. He is currently a lecturer in the Department of Industrial and Systems Engineering at the Hong Kong Polytechnic University. His research interests include supply chain management, integrated quality enhancement systems and arti<sup>fi</sup>cial intelligence appli cations.

Yi Zhao received his M.Eng. degree from Zhajiang University, Hangzhou, China, in 2003 and the Ph.D. degree from Hong Kong Polytechnic University, Hong Kong, China, in 2007. He is currently a Postdoctoral Fellow at Hong Kong Polytechnic University. His research interests include time series analysis, nonlinear system modeling, and neural networks.
