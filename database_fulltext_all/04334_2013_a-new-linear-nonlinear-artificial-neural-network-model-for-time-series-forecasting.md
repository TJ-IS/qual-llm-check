---
otero_id: 4334
otero_key: "J6CWWA9Y"
title: "A new linear & nonlinear artificial neural network model for time series forecasting"
authors: "Ufuk Yolcu; Erol Egrioglu; Cagdas H. Aladag"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.12.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A new linear & nonlinear arti<sup>fi</sup>cial neural network model for time series forecasting

Ufuk Yolcu <sup>a,</sup>⁎, Erol Egrioglu <sup>b</sup>, Cagdas H. Aladag <sup>c</sup>

<sup>a</sup> Department of Statistics, Giresun University, Giresun 28000, Turkey

<sup>b</sup> Department of Statistics, Ondokuz Mayis University, Samsun 55139, Turkey

<sup>c</sup> Department of Statistics, Hacettepe University, Ankara 06800, Turkey

## a r t i c l e i n f o

Article history: Received 28 September 2011 Received in revised form 25 July 2012 Accepted 4 December 2012 Available online 12 December 2012

Keywords: Arti<sup>fi</sup>cial neural networks Forecasting Multiplicative neuron model Particle swarm optimization

## a b s t r a c t

Arti<sup>fi</sup>cial neural network approach is a well-known method that is a useful tool for time series forecasting. Since real life time series can generally contain both linear and nonlinear components, hybrid approaches which can model both these two components have also been proposed in the literature. The hybrid approaches suggested in the literature generally have two phases. In the <sup>fi</sup>rst phase, linear component of time series is modeled with a linear model. Then, nonlinear component is modeled by utilizing a nonlinear model in the second phase. In two-phase methods, it is assumed that time series has only a linear structure in the <sup>fi</sup>rst phase. Also, it is assumed that time series has only a nonlinear structure in the second phase. Therefore, this causes model speci<sup>fi</sup>cation error. In order to overcome this problem, a novel neural network model, which consists of both linear and nonlinear structures, is proposed in this study. The proposed model considers that time series has both linear and nonlinear components. Multiplicative and Mc Culloch–Pitts neuron structures are employed for nonlinear and linear parts of the proposed model, respectively. In addition, the modi<sup>fi</sup>ed particle swarm optimization method is used to train the proposed neural network model. In order to show the performance of the proposed approach, it is applied to three real life time series and obtained results are compared to those obtained from other approaches available in the literature. It is observed that the proposed model gives the best forecasts for these three time series.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

In the literature, while linear models such as autoregressive integrated moving average (ARIMA; [2]) have been used for linear time series, nonlinear models such as arti<sup>fi</sup>cial neural networks (ANN), bilinear, and threshold autoregressive (TAR; [19]) have been preferred for nonlinear time series. It is a well-known fact that real life time series can generally contain both trend and seasonal variations. It is almost impossible that a time series is pure linear or pure nonlinear.

For some time series, linear models can produce satisfactory results when the linear part of the time series is superior to the nonlinear part. In a similar way, when the nonlinear part of the time series is superior to the linear part, nonlinear models can give satisfactory results. However, in both cases, one of these parts is not taken into consideration. Thus, it can lead to deceptive results. To deal with this problem, various hybrid approaches have been suggested in the literature. Tseng et al. [20] proposed a hybrid forecasting model, which combines the seasonal ARIMA (SARIMA) and ANN. Zhang [24] improved a hybrid model based on ARIMA and ANN. In Zhang's [24] method, it is assumed that time series is composed of sum of linear and nonlinear parts. In the method proposed by Zhang [24], while the linear part is being analyzed by

ARIMA, the residuals obtained from ARIMA are modeled by feed forward ANN. In the literature, there have been some hybrid methods similar to Zhang's method [24]. Khashei and Bijari [12,13] combined ARIMA and probabilistic neural network (PNN), Chen and Wang [4] combined SARIMA and SVM, Aladag et al. [1] combined ARIMA and Elman neural networks, and Lee and Tong [14] combined ARIMA and genetic algorithms. Besides, Ince and Trafalis [7] proposed a hybrid model which incorporates parametric techniques such as ARIMA, vector autoregressive (VAR) and co-integration techniques, and nonparametric techniques such as support vector regression (SVR) and ANN. Wang et al. [22] introduced some hybrid approaches which are called threshold ANN, cluster based ANN, and periodic ANN. BuHamra et al. [3] and Jain and Kumar [8] suggested hybrid approaches in which the inputs of ANN are determined by Box-Jenkins' [2] procedure. In addition to these studies, hybrid approaches combining SARIMA and ANN were also proposed to analyze fuzzy time series (Egrioglu et al. [5]; Uslu et al. [21]).

The hybrid approaches which can model both these two components have been proposed in the literature in order to forecast real life time series containing both linear and nonlinear components. These hybrid approaches generally consist of two phases. After linear the component of the time series is modeled with a linear model in the <sup>fi</sup>rst phase, the nonlinear component is modeled by utilizing a nonlinear model in the next phase. In two-phase methods, it is assumed that time series has only a linear structure in the <sup>fi</sup>rst phase and it is assumed that time series has only a nonlinear structure in the second phase.

Therefore, this causes model speci<sup>fi</sup>cation error. In this study, a new ANN model composed of both linear and nonlinear structures is proposed to deal with this problem and to increase forecasting accuracy. The proposed model considers that time series has both linear and nonlinear components. Therefore, this method has the ability to model both linear and nonlinear parts in the time series at the same time. In the proposed model, Multiplicative and Mc Culloch–Pitts neuron structures are used for the nonlinear and linear parts, respectively. In addition, the modi<sup>fi</sup>ed particle swarm optimization (MPSO) method is used to train the proposed neural network model. To show the applicability of the proposed method, it is applied to three real life time series in the implementation. For the aim of comparison, the obtained results are compared to those calculated from other approaches available in the literature. As a result of the implementation, it is seen that the proposed method has the best forecasting accuracy.

In the next section, the MPSO method is presented. The proposed neural network model is introduced in Section 3. The implementation is given in Section 4. Finally, the last section concludes the paper.

## 2. The modi<sup>fi</sup>ed particle swarm optimization

Particle swarm optimization, which is a population based heuristic algorithm, was <sup>fi</sup>rstly proposed by Kennedy and Eberhart [11]. A distinguishing feature of this heuristic algorithm is that it simultaneously examines different points in different regions of the solution space to <sup>fi</sup>nd the global optimum solution. Local optimum traps can be avoided because of this feature. In this study, MPSO is used to train the proposed neural network model. The MPSO algorithm has a time varying inertia weight like in Shi and Eberhart [17]. In a similar way, this algorithm also has a time varying acceleration coef<sup>fi</sup>cient like in Ma et al. [15].

## Algorithm 1. The MPSO

Step 1 Positions of each kth $( k = 1 , 2 , . . . , p n )$ particles' positions are randomly determined and kept in a vector X given as follows:

$$
X _ {k} = \left\{x _ {k, 1}, x _ {k, 2}, \dots , x _ {k, d} \right\}, k = 1, 2, \dots , p n\tag{1}
$$

where $\iota _ { i } ^ { k } ( i { = } 1 , 2 { , } . . . , d )$ represents ith position of kth particle. pn and d represents the number of particles in a swarm and positions, respectively.

Step 2 Velocities are randomly determined and stored in a vector $V _ { k }$ given below.

$$
V _ {k} = \left\{v _ {k, 1}, v _ {k, 2}, \dots , v _ {k, d} \right\}, k = 1, 2, \dots , p n\tag{2}
$$

Step 3 According to the evaluation function, Pbest and Gbest particles given in Eqs. (3) and (4), respectively, are determined.

$$
P b e s t _ {k} = \left(p _ {k, 1}, p _ {k, 2},..., p _ {k, d}\right), k = 1, 2,..., p n\tag{3}
$$

$$
G b e s t = \left(p _ {g, 1}, p _ {g, 2}, \dots , p _ {g, d}\right)\tag{4}
$$

where Pbest is a vector that stores the positions corresponding to the kth particle's best individual performance, and Gbest represents the best particle, which has the best evaluation function value, found so far.

Step 4 Let $c _ { 1 }$ and $c _ { 2 }$ represent cognitive and social coef<sup>fi</sup>cients, respectively, and w is the inertia parameter. Let $\left( \boldsymbol { c } _ { 1 i } , \ \boldsymbol { c } _ { 1 f } \right)$ $( c _ { 2 i } , c _ { 2 f } ) ,$ , and $( w _ { 1 } , w _ { 2 } )$ be the intervals which include possible values for $c _ { 1 } , c _ { 2 }$ and w, respectively. At each iteration, these parameters are calculated by using the formulas given in Eqs. (5), (6) and (7).

$$
c _ {1} = \left(c _ {1 f} = c _ {1 i}\right) \frac {t}{m a x t} + c _ {1 i}\tag{5}
$$

$$
c _ {2} = \left(c _ {2 f} = c _ {2 i}\right) \frac {t}{m a x t} + c _ {2 i}\tag{6}
$$

$$
w = (w _ {2} - w _ {1}) \frac {\max t - t}{\max t} + w _ {1}\tag{7}
$$

where maxt and t represent maximum iteration number and current iteration number, respectively.

Step 5 Values of velocities and positions are updated by using the formulas given in Eqs. (8) and (9), respectively.

$$
\begin{array}{c} v _ {i, d} ^ {t + 1} = \left[ w \times v _ {i, d} ^ {t} + c _ {1} \times r a n d _ {1} \times \left(p _ {i, d} - x _ {i, d}\right) + c _ {2} \times r a n d _ {2} \right. \\ \times \left(p _ {g, d} - x _ {i, d}\right) \biggr ] \end{array}\tag{8}
$$

$$
x _ {i, d} ^ {t + 1} = x _ {i, d} + v _ {i, d} ^ {t + 1}\tag{9}
$$

where rand and rand are random values from the interval [0 1].

Step 6 Steps 3 to 5 are repeated until a predetermined maximum iteration number (maxt) is reached.

## 3. The proposed method

In the literature, there have been various linear models to analyze time series. Since most of real time series also contain nonlinear structure, linear models cannot produce satisfactory results when such time series are analyzed. To forecast this kind of time series, nonlinear models such as TAR, SVM, SVR, and feed forward and recurrent ANN have been used in the literature. However, nonlinear models are not suf<sup>fi</sup>cient by themselves since real life time series have both linear and nonlinear structures. Therefore, hybrid models which include the advantages of both linear and nonlinear models have also been proposed in the literature. In the hybrid approaches, it is assumed that the time series is composed of the sum of the linear and nonlinear parts and can be de<sup>fi</sup>ned by

$$
y _ {t} = L _ {t} + N _ {t}\tag{10}
$$

where $y _ { t } , L _ { t } ,$ and $N _ { t }$ represent the time series, the linear part and the nonlinear part of the time series, respectively.

In the literature, Zhang [24], Chen and Wang [4], Aladag et al. [1], and Lee and Tong [14] employed two-phase hybrid approaches. After the linear part of time series is modeled in the <sup>fi</sup>rst phase, by assuming that residuals obtained in the <sup>fi</sup>rst phase contain the nonlinear part, these residuals are analyzed with nonlinear models in the second phase. Employing a linear model in the <sup>fi</sup>rst phase means that nonlinear relations are not taken into consideration. This situation causes model speci<sup>fi</sup>cation error. To overcome this problem, a one-phase method which can simultaneously analyze both linear and nonlinear structures is needed when time series given in Eq. (10) are analyzed. Therefore, a novel linear & nonlinear arti<sup>fi</sup>cial neural network (L&NL-ANN) model is proposed in this study. The broad structure of the proposed model is illustrated in Fig. 1.

In Fig. 1, $\scriptstyle \sum$ and ∏ represent neuron models of McCulloch and Pitts [16], and multiplicative neuron models (Yadav et al. [23]), respectively. The functions f and $f _ { 2 }$ are given in Eqs. (11) and (12), respectively.

$$
f _ {1} (x) = x\tag{11}
$$

$$
f _ {2} (x) = \frac {1}{1 + e ^ {- x}}\tag{12}
$$

As seen in Fig. 1, the L&NL-ANN model includes two components linear and nonlinear. $W _ { 1 }$ is a vector that includes the weights between the inputs of the linear component and neurons in the hidden layer corresponding to the linear part of the model. Similarly, the vector $W _ { 2 }$ contains the weights between the inputs of the nonlinear component and neurons in the hidden layer corresponding to the nonlinear part of the model. Each component has m inputs so both $W _ { 1 }$ and $W _ { 2 }$ are m×1. The vector $W _ { 3 } ,$ , which is $2 \times 1$ , consists of two weights which are used to combine outputs calculated from linear and nonlinear components. Thus, calculation of the output of L&NL-ANN model is given in three stages.

![](/api/attachments/J6CWWA9Y/fulltext/images/3e744aafa2b71b4ae43aef2b518646f2860ce47cf93c8d48dd37121d8bb27426.jpg)  
Fig. 1. The architecture of L&NL-ANN model.

Stage 1 The output value of the neuron in the hidden layer corresponding to the linear component $\left( \boldsymbol { o } _ { 1 } \right)$ is calculated. Firstly, the activation value net for the neuron is obtained by using the formula given as follows:

$$
n e t _ {1} = \left[ \sum_ {j = 1} ^ {m} w _ {1 j} y _ {t - j} + b _ {1} \right]\tag{13}
$$

where $w _ { 1 j } \ ( j = 1 , 2 , . . . , m )$ are elements of $W _ { 1 }$ , and $b _ { 1 }$ is bias weight for the linear part. The activation function used in this neuron is $f _ { 1 }$ given in Eq. (11) so the output value $o _ { 1 }$ is calculated by

$$
o _ {1} = f _ {1} (n e t _ {1}) = n e t _ {1}\tag{14}
$$

Thus, the output $o _ { 1 }$ is equivalent to an output obtained from mth order autoregressive model.

Stage 2 The output value of the neuron in the hidden layer corresponding to the nonlinear component $\left( { { o _ { 2 } } } \right)$ is calculated. Before calculating $^ { 0 _ { 2 } , }$ the activation value ne $t _ { 2 }$ for the neuron is computed by using the formula given in Eq. (15).

$$
n e t _ {2} = \left[ \prod_ {j = 1} ^ {m} \left(w _ {2 j} y _ {t - j} + b _ {2 j}\right) \right]\tag{15}
$$

where $w _ { 2 j } ,$ and $b _ { 2 j } ( j = 1 , 2 , . . . , m )$ are elements of $W _ { 2 } ,$ and bias weight values for the nonlinear part. The activation function used in this neuron is $f _ { 2 }$ given in Eq. (12) so the output value $o _ { 2 }$ is calculated by

$$
o _ {2} = f _ {2} \left(n e t _ {2}\right) = \frac {1}{1 + \exp \left(- n e t _ {2}\right)}\tag{16}
$$

Thus, the output o is equivalent to an output obtained from mth order nonlinear autoregressive model.

Stage 3 The output value $( \hat { y } _ { t } )$ of the model is calculated. First of all, the activation value net<sub>3</sub> for the neuron in the output layer is obtained bay using the formula given in Eq. (17).

$$
n e t _ {3} = \left[ w _ {3 1} n e t _ {1} + w _ {3 2} n e t _ {2} + b _ {3} \right]\tag{17}
$$

In Eq. (17), $b _ { 3 }$ is bias weight. Then, the output $\hat { y } _ { t }$ is computed as follows:

$$
\hat {y} _ {t} = f _ {1} (n e t _ {3}) = n e t _ {3}\tag{18}
$$

![](/api/attachments/J6CWWA9Y/fulltext/images/6452918fa3329e601deba8127da039f9e8595fd941f6ba29877eb2f6d3160962.jpg)  
Fig. 2. Structure of a particle

![](/api/attachments/J6CWWA9Y/fulltext/images/5f81e2a85f2a241f712b1a76c327704d747b05295b7052eb1a3f95a45c6719df.jpg)  
Fig. 3. The time series data of the amount of SO in Ankara.

As seen from Eq. (18), the output value is obtained from the weighted sum of linear and nonlinear autoregressive models. Unlike the model given in Eq. (10), L&NL-ANN model can be expressed as in Eq. (19).

$$
y _ {t} = w _ {3 1} L _ {t} + w _ {3 2} N _ {t} + b _ {3}\tag{19}
$$

It should be noted in here that in the model given in Eq. (10), weights of linear and nonlinear components are equal. However, in L&NL-ANN model, these weights are determined during the optimization process of ANN due to the structure of the data.

In the proposed approach, L&NL-ANN model, which is also de<sup>fi</sup>ned in this study, is trained using MPSO method. In the MPSO, positions of a particle are weights of L&NL-ANN model. Hence, a particle has 3m + 4 positions. The structure of a particle is illustrated in Fig. 2.

Mean square error (MSE), which is a well-known forecasting performance criterion, is used as evaluation function. MSE can be calculated using the formula given in Eq. (20).

$$
\mathrm{MSE} = \frac {1}{n} \sum_ {t = 1} ^ {n} \left(\text { output } _ {t} - \text { target } _ {t}\right) ^ {2}\tag{20}
$$

where n represents the number of learning sample. The algorithm for calculation of the output value of the proposed MSANN model is presented below.

Algorithm 2. The algorithm for calculation of the output value of the proposed L&NL-ANN model.

Step 1 The parameters of MPSO are determined.

In the <sup>fi</sup>rst step, the parameters which direct the MPSO algorithm are determined. These parameters are pn, vm, c , c , $c _ { 2 i } , c _ { 2 f } , w _ { 1 } ,$ and $w _ { 2 }$ that were given in the previous section.

Step 2 Initial values of positions and velocities are determined.

The initial positions and velocities of each particle in a swarm are randomly generated from uniform distribution (0,1) and (−vm,vm), respectively.

Step 3 Evaluation function values are computed.

Evaluation function values for each particle are calculated. MSE given in Eq. (20) is used as evaluation function.

Step 4 Pbest<sub>k</sub> $( k = 1 , 2 , . . . , p n )$ and Gbest are determined due to the evaluation function values calculated in the previous step. $P b e s t _ { k }$ is a vector that stores the positions corresponding to the kth particle's best individual performance, and Gbest is the best particle, which has the best evaluation function value, found so far

Step 5 The parameters are updated.

The updated values of cognitive coef<sup>fi</sup>cient $c _ { 1 } ,$ social coef<sup>fi</sup>- cient $c _ { 2 } ,$ and inertia parameter w are calculated using the formulas given in Eqs. (5), (6), and (7).

Step 6 New values of positions and velocities are calculated. New values of positions and velocities for each particle are computed by using the formulas given in Eqs. (8) and (9). If the maximum iteration number is reached, the algorithm goes to Step 3; otherwise, it goes to Step 7.

Step 7 The optimal solution is determined.

The elements of Gbest are taken as the optimal weight values of the L&NL-ANN.

## 4. Application of the proposed L&NL-ANN model

In order to evaluate the performance of the proposed approach based on the L&NL-ANN model, which also de<sup>fi</sup>ned in this study, and the MPSO algorithm, the proposed approach is applied to three real time series in the implementation. These time series are also analyzed by using other alternative methods such as ANN, fuzzy time series, hybrid methods, and linear and nonlinear conventional approaches.

Table 1  
The obtained forecasting results for ANSO data.

<table><tr><td>Test Data</td><td>SARIMA</td><td>WMES</td><td>Song [18]</td><td>Egrioglu et al. [5]</td><td>Uslu et. al. [21]</td><td>FFANN</td><td>RBFNN</td><td>L&amp;NL-ANN</td></tr><tr><td>21</td><td>22.93</td><td>15.40</td><td>41.66</td><td>20</td><td>22.75</td><td>24.09</td><td>30.53</td><td>21.70</td></tr><tr><td>27</td><td>22.35</td><td>16.11</td><td>27.50</td><td>30</td><td>22.75</td><td>24.17</td><td>36.96</td><td>21.56</td></tr><tr><td>25</td><td>23.61</td><td>17.77</td><td>41.66</td><td>20</td><td>22.75</td><td>24.62</td><td>43.72</td><td>25.54</td></tr><tr><td>28</td><td>28.81</td><td>25.12</td><td>41.66</td><td>30</td><td>22.75</td><td>25.90</td><td>45.72</td><td>31.08</td></tr><tr><td>38</td><td>46.97</td><td>41.11</td><td>41.66</td><td>30</td><td>42.05</td><td>47.07</td><td>46.19</td><td>37.47</td></tr><tr><td>45</td><td>54.62</td><td>46.12</td><td>46.78</td><td>50</td><td>42.05</td><td>44.20</td><td>45.74</td><td>46.64</td></tr><tr><td>38</td><td>58.13</td><td>49.80</td><td>45.00</td><td>40</td><td>42.05</td><td>38.46</td><td>43.1</td><td>41.97</td></tr><tr><td>36</td><td>46.99</td><td>44.24</td><td>46.78</td><td>30</td><td>42.05</td><td>34.73</td><td>36.49</td><td>35.22</td></tr><tr><td>24</td><td>37.85</td><td>31.96</td><td>46.78</td><td>30</td><td>22.75</td><td>28.51</td><td>31.75</td><td>32.13</td></tr><tr><td>22</td><td>24.76</td><td>18.39</td><td>27.50</td><td>20</td><td>22.75</td><td>25.53</td><td>29.51</td><td>23.35</td></tr><tr><td>RMSE</td><td>9.6249</td><td>7.1062</td><td>12.7410</td><td>4.5607</td><td>3.6611</td><td>3.7402</td><td>10.3189</td><td>3.5674</td></tr><tr><td>MAPE</td><td>0.2336</td><td>0.2204</td><td>0.3977</td><td>0.1312</td><td>0.1051</td><td>0.0995</td><td>0.3248</td><td>0.0944</td></tr><tr><td>MdAPE</td><td>0.1931</td><td>0.2478</td><td>0.2748</td><td>0.1111</td><td>0.0983</td><td>0.0898</td><td>0.3321</td><td>0.0491</td></tr><tr><td>DA</td><td>0.5556</td><td>0.6667</td><td>0.6667</td><td>1.0000</td><td>0.7778</td><td>0.8889</td><td>0.7778</td><td>1.0000</td></tr></table>

Table 2  
The optimal weights of L&NL-ANN model.

<table><tr><td> $W_1$ </td><td> $b_1$ </td><td> $W_2$ </td><td> $b_2$ </td><td> $W_3$ </td><td> $b_3$ </td></tr><tr><td>3.2493640953</td><td>1.1763445404</td><td>1.5214729257</td><td>-1.3700203060</td><td>1.1324621049</td><td>-0.6524088177</td></tr><tr><td>0.4632453173</td><td></td><td>0.1068945512</td><td>-1.0517058203</td><td>0.1249808216</td><td></td></tr><tr><td>-0.3644501379</td><td></td><td>-0.3095323299</td><td>1.2115469437</td><td></td><td></td></tr><tr><td>0.2622086689</td><td></td><td>0.0426492273</td><td>0.7264541204</td><td></td><td></td></tr><tr><td>-0.3578923341</td><td></td><td>0.0596581488</td><td>1.4538253515</td><td></td><td></td></tr><tr><td>-0.0183806813</td><td></td><td>2.2159505332</td><td>0.5183546715</td><td></td><td></td></tr><tr><td>-1.2641464956</td><td></td><td>1.6641947716</td><td>-0.6089078254</td><td></td><td></td></tr><tr><td>-0.0626257989</td><td></td><td>0.3210090179</td><td>1.3204980257</td><td></td><td></td></tr><tr><td>0.4618536402</td><td></td><td>-0.1126251483</td><td>-0.7093258240</td><td></td><td></td></tr><tr><td>0.3997984385</td><td></td><td>0.4363950911</td><td>2.0129471641</td><td></td><td></td></tr><tr><td>1.2998003058</td><td></td><td>0.4555531477</td><td>-0.1217494950</td><td></td><td></td></tr><tr><td>1.1886041719</td><td></td><td>1.4455141945</td><td>0.8223344211</td><td></td><td></td></tr></table>

SARIMA and Winters' multiplicative exponential smoothing (WMES) approaches are the linear conventional methods used in the implementation. Feed forward arti<sup>fi</sup>cial neural network (FFANN) type and Radial basis function based arti<sup>fi</sup>cial neural networks (RBF) which are ANN approaches are preferred in the application. Also, we would like to note that FFANN model used in this study is a multilayer perceptron (MLP) model. Song's method [18], and hybrid fuzzy time series method proposed by Egrioglu et al. [5] and Uslu et al. [21] are also employed. Hybrid approaches combine ARIMA and ANN proposed by Zhang [24] and Aladag et al. [1] are utilized. Self-exciting threshold autoregressive (SETAR) is a method that is used in the implementation as a nonlinear forecasting approach. Then, the results calculated from the proposed approach are compared to those produced by the other methods. In all computations, Matlab version 7.12.0 (R2011a) computer package was used.

To compare all obtained forecasting results, some performance measures such as root mean square error (RMSE), mean absolute percentage error (MAPE), median absolute percentage error (MdAPE), and direction accuracy (DA) were employed. The related formulas are presented below.

$$
R M S E = \left(\frac {\sum_ {i = 1} ^ {T} (y _ {i} - \hat {y} _ {i}) ^ {2}}{T}\right) ^ {1 / 2}\tag{21}
$$

$$
M A P E = \frac {1}{T} \sum_ {i = 1} ^ {T} \left| \frac {y _ {i} - \hat {y} _ {i}}{y _ {i}} \right|\tag{22}
$$

$$
M d A P E = \text { Median } \left(\left| \frac {y _ {i} - \hat {y} _ {i}}{y _ {i}} \right|\right)\tag{23}
$$

$$
D A = \frac {1}{T} \sum_ {i = 1} ^ {T} a _ {i}, a _ {i} = \left\{ \begin{array}{l l} 1 & \text { if } (y _ {i + 1} - y _ {i}) (\hat {y} _ {i + 1} - y _ {i}) > 0 \\ 0 & \text { otherwise. } \end{array} \right.\tag{24}
$$

where $y _ { i }$ is the actual value; $\hat { y } _ { i }$ is the predicted value; T is the number of data.

## 4.1. Data set 1

The <sup>fi</sup>rst time series is the amount of carbon dioxide measured monthly in Ankara capitol of Turkey (ANSO) between March 1995 and April 2006. The graph of ANSO time series is presented in Fig. 3.

This time series has both trend and seasonal components and its period is 12. The <sup>fi</sup>rst 124 observations were used for training and the last 10 observations are used for test set. In addition to the proposed approach, seasonal autoregressive integrated moving average (SARIMA), winter's multiplicative exponential smoothing (WMES), feed forward neural network (FFANN) methods and the fuzzy time series forecasting methods proposed by Song [18], Egrioglu et al. [5] and Uslu et al. [21] were used to analyze ANSO data. For the test set, the forecasts and values of the performance measures produced by all methods are summarized in Table 1.

The results of the methods SARIMA, WMES, Song [18], Egrioglu et al. [5], and Uslu et al. [21] were taken from Uslu et al. [21]. The best SARIMA model was found as SARIMA(1,1,0)(0,1,1)12. When WMES was applied to ANSO, linear trend component was employed. When the method proposed by Song [18] was utilized, length of interval was taken as 50. For the approach introduced in Egrioglu et al. [5], length of intervals for ANSO and errors were taken as 10 and 0.2, respectively. Also, eight neurons were used in the hidden layer of the feed forward neural network model that was utilized to de<sup>fi</sup>ne fuzzy relationships in the method proposed by Egrioglu et al. [5]. When the forecasting approach proposed by Uslu et al. [21] was employed, number of fuzzy cluster was taken as 10 for both ANSO and errors. Besides, two neurons were used in the hidden layer of the feed forward neural network model that was used to determine fuzzy relationships in the method introduced in Uslu et al. [21]. When FFANN and RBF were applied to the data, the numbers of neurons in both the hidden and input layers are changed from 1 to 12 and one output neuron is employed. Therefore, 144 architectures are totally examined for each type. The best FFANN architecture among them was found as the architecture 12-1-1 that means the best architecture contains 12 neurons in the input layer and 1 neuron in the hidden. And, the best architecture for RBF was found as the architecture 12-2-1. Thus, Thus, the inputs of the best FFANN and RBF model are the lagged variables $X _ { t - 1 } , X _ { t - 2 } , . . . , X _ { t - 1 2 } .$ Inputs of L&NL-ANN model are taken as $X _ { t - 1 } , X _ { t - 2 } , . . . , X _ { t - 1 2 }$ like in the FFANN model. And, in the training process of L&NL-ANN model, the parameters of the modi<sup>fi</sup>ed particle swarm optimization are determined as follows: $( c _ { 1 i } , c _ { 1 f } ) = ( 2 , 3 ) , ( c _ { 2 i } , c _ { 2 f } ) = ( 2 , 3 ) , ( w _ { 1 } , w _ { 2 } ) = ( 1 , 2 ) , p n =$ 30, and maxt=1000. The optimal weight values of the L&NL-ANN model are presented in Table 2.

![](/api/attachments/J6CWWA9Y/fulltext/images/f066ed5d9a9ebf834b6c36914ac83a26f0b8d1b93d0135833b7592fa361d4c32.jpg)  
Fig. 4. The graph of observations and forecasts obtained from all methods for the test set

![](/api/attachments/J6CWWA9Y/fulltext/images/424fa3aafc1b921a511d0abcc3d63611ec9a6c2c0b2d8b3fae5cf8681db7b7b5.jpg)  
Fig. 5. Australian beer consumption data.

According to Table 1, the proposed approach has the best forecasting accuracy for ANSO data in terms of RMSE, MAPE, MdAPE, and DA. To examine the results visually, the graph of the real observations and the forecasts produced by all approaches for the test set is given in Fig. 4. As clearly seen from this graph, the proposed approach produces very accurate forecasts for ANSO data.

## 4.2. Data set 2

The second time series is quarterly Australian beer consumption (Janacek [9], pp.84) between 1956 Q1 and 1994 Q1 whose graph is given in Fig. 5. The last 16 observations of the time series were used for test set. Australian beer consumption was forecasted by using SARIMA, WMES, FFANN, and the proposed L&NL-ANN method. The fuzzy time series forecasting methods proposed by Song [18], Egrioglu et al. [5], and Uslu et al. [21] were not used for this data because of the characteristic of the data. In other words, Australian beer consumption does not contain uncertainty so it is not proper to use fuzzy time series methods for this data. All obtained forecasting results for Australian beer consumption are summarized in Table 3.

Table 3  
The obtained forecasting results for Australian beer consumption.

<table><tr><td>Test data</td><td>SARIMA</td><td>WMES</td><td>FFANN</td><td>RBF</td><td>L&amp;NL-ANN</td></tr><tr><td>430.50</td><td>452.72</td><td>453.91</td><td>453.8838</td><td>430.54</td><td>449.92</td></tr><tr><td>600.00</td><td>578.29</td><td>575.22</td><td>557.8151</td><td>509.26</td><td>574.28</td></tr><tr><td>464.50</td><td>487.70</td><td>502.32</td><td>497.5159</td><td>525.50</td><td>481.47</td></tr><tr><td>423.60</td><td>446.28</td><td>444.73</td><td>437.393</td><td>426.63</td><td>442.79</td></tr><tr><td>437.00</td><td>456.77</td><td>459.66</td><td>449.0035</td><td>426.45</td><td>445.12</td></tr><tr><td>574.00</td><td>583.51</td><td>582.48</td><td>569.0025</td><td>523.35</td><td>571.97</td></tr><tr><td>443.00</td><td>492.13</td><td>508.64</td><td>471.0758</td><td>511.80</td><td>472.76</td></tr><tr><td>410.00</td><td>450.36</td><td>450.31</td><td>424.3307</td><td>426.60</td><td>416.36</td></tr><tr><td>420.00</td><td>461.01</td><td>465.4</td><td>448.8667</td><td>427.71</td><td>428.63</td></tr><tr><td>532.00</td><td>588.96</td><td>589.74</td><td>560.0436</td><td>508.68</td><td>559.89</td></tr><tr><td>432.00</td><td>496.77</td><td>514.96</td><td>447.0135</td><td>489.67</td><td>445.75</td></tr><tr><td>420.00</td><td>454.64</td><td>455.89</td><td>408.6362</td><td>427.31</td><td>390.25</td></tr><tr><td>411.00</td><td>465.46</td><td>471.15</td><td>428.1073</td><td>430.14</td><td>412.38</td></tr><tr><td>512.00</td><td>594.71</td><td>597.00</td><td>537.6988</td><td>486.54</td><td>533.19</td></tr><tr><td>449.00</td><td>501.67</td><td>521.28</td><td>438.433</td><td>476.30</td><td>442.13</td></tr><tr><td>382.00</td><td>459.17</td><td>461.46</td><td>420.5827</td><td>431.40</td><td>405.08</td></tr><tr><td>RMSE</td><td>47.0367</td><td>53.3295</td><td>24.1052</td><td>41.7000</td><td>18.7888</td></tr><tr><td>MAPE</td><td>0.0949</td><td>0.1072</td><td>0.0476</td><td>0.0686</td><td>0.0357</td></tr><tr><td>MdAPE</td><td>0.0980</td><td>0.1032</td><td>0.0459</td><td>0.0481</td><td>0.0390</td></tr><tr><td>DA</td><td>0.7333</td><td>0.6667</td><td>0.9333</td><td>0.9333</td><td>1.0000</td></tr></table>

The best model for SARIMA was obtained as SARIMA(0,1,1)(0,1,1) . Linear trend component was utilized when WMES was applied to Australian beer consumption. When the data was forecasted using FFANN and RBF, the numbers of neurons in both the hidden and input layers are changed from 1 to 8 and one output neuron is employed so 64 architectures are totally examined for each type. For both neural network models, the best architecture was found as 4-3-1 that means the best architecture has 3 and 4 neurons in the input and hidden layers, respectively. When the proposed method was used, the order of the L&NL-ANN model was m=8. It is clearly seen that the proposed method has the best forecasting accuracy in terms of all performance measures when Table 3 is examined. Also, the forecasting performance of the proposed L&NL-ANN model is examined visually. The graph of the real observations and the forecasts obtained from all methods for the test set is given in Fig. 6. According to this graph, the forecasts obtained from the proposed approach are very accurate.

![](/api/attachments/J6CWWA9Y/fulltext/images/9308d4a098c0c6e1fb64814ae803412d4c2393a18e3fb43d282ad5ffa3c0a9e9.jpg)  
Fig. 6. The forecasting results computed over the test set for Data set 2.

![](/api/attachments/J6CWWA9Y/fulltext/images/dcad5c3fca9c09b31fb08e63472fd02e334fdb839f0133acde44072372fb4a01.jpg)  
Fig. 7. Logarithmic Canadian lynx data series (1821–1934).

## 4.3. Data set 3

L&NL-ANN model was also applied to Canadian lynx data consisting of the set of annual numbers of lynx trappings in the Mackenzie River District of North-West Canada for the period from 1821 to 1934. The last 14 observations were used for test set and the rest of the data were used for training. This data has also been extensively analyzed in the time series literature. We used the logarithm (to the base 10) of the data in the analysis. In addition to the proposed approach, logarithm of Canada lynx data, which is shown in Fig. 7, is examined by using the methods proposed by Zhang [24], Kajitani et al. [10], Khashei and Bijari [12,13], Gan and Peng [6], Aladag et al. [1]. When the proposed method was used, the order of the L&NL-ANN model was m=3. Mean square error (MSE) values obtained from all methods for the test set are presented in Table 4. MSE values included in Table 4 were taken from corresponding studies such as Aladag et al. [1], Zhang [24], Kajitani et al. [10], Khashei and Bijari [12,13] and Gan and Peng [6]. In addition, the results obtained from ARIMA and FFANN methods (Table 5) were also taken from Aladag et al. [1]. Detailed information about applications of these methods can be found in these studies.

As seen from Table 4, the best forecasts are obtained when the proposed L&NL-ANN model is used in terms of MSE criterion. The graph of the real observations and the forecasts obtained from the proposed approach for test set is given in Fig. 8. It is clearly seen from the graph that the forecasts produced by the proposed approach are very accurate.

## 5. Conclusions

It is a well-known fact that real life time series can contain both linear and nonlinear structures. In the literature, various hybrid approaches, which are generally two-phase methods, have been proposed to deal with such time series. After linear component of time series is modeled with a linear model in the <sup>fi</sup>rst phase, nonlinear component is modeled by utilizing a nonlinear model in the next phase. In two-phase methods, it is assumed that time series has only linear structure in the <sup>fi</sup>rst phase and it is assumed that time series has only a nonlinear structure in the second phase. Therefore, this causes model speci<sup>fi</sup>cation error. To overcome this problem and to reach high forecasting accuracy level, a new ANN model which can simultaneously analyze both linear and nonlinear structures is introduced in this study. This model can be considered as one-phase hybrid approach. In the other hybrid approaches available in the literature, weights of linear and nonlinear components are equal. Unlike the other hybrid approaches suggested in the literature, in the proposed neural network model, weights of linear and nonlinear components are determined during the optimization process of ANN due to the structure of the data. In the proposed model, Multiplicative and Mc Culloch–Pitts neuron structures are used for nonlinear and linear parts, respectively. In addition, the modi<sup>fi</sup>ed particle swarm optimization method is used to train the proposed neural network model.

The MSE values calculated over the test set for Logarithmic Canadian Lynx Data.

<table><tr><td>ARIMA</td><td>FFANN</td><td>Zhang [24]</td><td>Kajitani [10]</td><td>Aladag et al. [1]</td><td>Khashei [12]</td><td>Khashei [13]</td><td>Gan [6]</td><td>L&amp;NL-ANN</td></tr><tr><td>0.015</td><td>0.020</td><td>0.017</td><td>0.014</td><td>0.009</td><td>0.013</td><td>0.011</td><td>0.007</td><td>0.006</td></tr></table>

To show forecasting performance of the proposed method, it is applied to three real life time series in the implementation. For the aim of comparison, these time series are also analyzed by using other alternative methods such as ANN, fuzzy time series, hybrid methods, and linear and nonlinear conventional approaches. Then, the obtained results are compared to those calculated from the other approaches available in the literature. As a result of the implementation, it is clearly observed that the proposed method produced the best forecasts for these three real time series.

The forecasting results obtained from the proposed method for Logarithmic Canadian Lynx Data.

<table><tr><td>Test Data</td><td>ARIMA</td><td>WMES</td><td>FFANN</td><td>RBF</td><td>Zhang [24]</td><td>Aladag et al. [1]</td><td>L&amp;NL-ANN</td></tr><tr><td>2.3600</td><td>2.3200</td><td>2.0300</td><td>2.4808</td><td>2.5100</td><td>2.2093</td><td>2.2906</td><td>2.3582</td></tr><tr><td>2.6000</td><td>2.8100</td><td>2.4100</td><td>2.7236</td><td>2.4100</td><td>2.8282</td><td>2.7804</td><td>2.7557</td></tr><tr><td>3.0500</td><td>2.9900</td><td>2.9000</td><td>2.9587</td><td>3.2600</td><td>3.0082</td><td>2.9664</td><td>2.9643</td></tr><tr><td>3.3900</td><td>3.3700</td><td>3.3000</td><td>3.3206</td><td>3.2600</td><td>3.3882</td><td>3.3404</td><td>3.4386</td></tr><tr><td>3.5500</td><td>3.6000</td><td>3.5700</td><td>3.6178</td><td>3.2600</td><td>3.6185</td><td>3.5976</td><td>3.6735</td></tr><tr><td>3.4700</td><td>3.5700</td><td>3.6600</td><td>3.4537</td><td>3.1900</td><td>3.5882</td><td>3.5037</td><td>3.4434</td></tr><tr><td>3.1900</td><td>2.8800</td><td>3.2100</td><td>3.0282</td><td>3.1900</td><td>2.8982</td><td>3.1257</td><td>3.1070</td></tr><tr><td>2.7200</td><td>2.5100</td><td>2.7700</td><td>2.7276</td><td>2.5100</td><td>2.4987</td><td>2.4804</td><td>2.8125</td></tr><tr><td>2.6900</td><td>2.7100</td><td>2.5400</td><td>2.3325</td><td>2.5100</td><td>2.7373</td><td>2.6804</td><td>2.5369</td></tr><tr><td>2.8200</td><td>2.7400</td><td>2.6600</td><td>2.6023</td><td>2.5100</td><td>2.7582</td><td>2.7104</td><td>2.8116</td></tr><tr><td>3.0000</td><td>2.9200</td><td>2.8200</td><td>2.9641</td><td>3.1900</td><td>2.9383</td><td>2.9909</td><td>3.0594</td></tr><tr><td>3.2000</td><td>3.1200</td><td>3.0500</td><td>3.1861</td><td>3.1900</td><td>3.1383</td><td>3.2860</td><td>3.2561</td></tr><tr><td>3.4200</td><td>3.4400</td><td>3.5000</td><td>3.2937</td><td>3.1900</td><td>3.4582</td><td>3.4104</td><td>3.4202</td></tr><tr><td>3.5300</td><td>3.5400</td><td>3.6700</td><td>3.4005</td><td>3.1900</td><td>3.5582</td><td>3.5156</td><td>3.5272</td></tr><tr><td>RMSE</td><td>0.1261</td><td>0.1568</td><td>0.1423</td><td>0.2170</td><td>0.1324</td><td>0.0970</td><td>0.0826</td></tr><tr><td>MAPE</td><td>0.0312</td><td>0.0469</td><td>0.0376</td><td>0.0636</td><td>0.0350</td><td>0.0251</td><td>0.0217</td></tr><tr><td>MdAPE</td><td>0.0223</td><td>0.0480</td><td>0.0333</td><td>0.0681</td><td>0.0199</td><td>0.0194</td><td>0.0187</td></tr><tr><td>DA</td><td>0.9231</td><td>0.7692</td><td>0.8462</td><td>0.6923</td><td>0.8462</td><td>1.0000</td><td>1.0000</td></tr></table>

![](/api/attachments/J6CWWA9Y/fulltext/images/188911f1a662386ec017c3d7e937af92e4feb501a6e3a31e37b7a8aa1d55447a.jpg)  
Fig. 8. The graph of observations and forecasts produced by the proposed L&NL-ANN for Data set 3.

## References

[1] C.H. Aladag, E. Egrioglu, C. Kadilar, Forecasting nonlinear time series with a hybrid methodology, Applied Mathematics Letters 22 (2009) 1467–1470.

[2] G.E.P. Box, G.M. Jenkins, Time Series Analysis: Forecasting and Control, Holdan-Day, San Francisco, CA, 1976.

[3] S. BuHamra, N. Smaoui, M. Gabr, The Box–Jenkins analysis and neural networks: prediction and time series modeling, Applied Mathematical Modelling 27 (2003) 805–815.

[4] K.Y. Chen, C.H. Wang, A Hybrid SARIMA and support vector machines in forecast ing the production values of the machinery industry in Taiwan, Expert System with Applications 32 (1) (2007) 254–264

[5] E. Egrioglu, C.H. Aladag, U. Yolcu, M.A. Basaran, V.R. Uslu, A new hybrid approach based on SARIMA and partial high order bivariate fuzzy time series forecasting model. Expert Systems with Applications 36 (2009) 7424-7434.

[6] M. Gan, H. Peng, Stability analysis of RBF network-based state-dependent autoregressive model for nonlinear time series, Applied Soft Computing 12 (2012) 174–181.

[7] H. Ince, T.B. Traffalis, A hybrid model for exchange rate prediction, Decision Support Systems 42 (2005) 1054–1062.

[8] A. Jain, A.M. Kumar, Hybrid neural network models for hydrological time series forecasting, Applied Soft Computing 7 (2007) 585–592

[9] G. Janacek, Practical Time Series, in: Oxford University Press Inc., Newyork, 2001 p. 156.

[10] Y. Kajitani, W.K. Hipel, A.I. Mcleod, Forecasting nonlinear time series with feed forward neural networks: a case study of Canadian Lynx Data, Journal of Forecasting 24 (2005) 105–117.

[11] J. Kennedy, R. Eberhart, Particle swarm optimization, in: Proceedings of IEEE International Conference on Neural Networks, Piscataway, IEEE Press, NJ, USA, 1995, pp. 1942–1948.

[12] M. Khashei, M. Bijari, An arti<sup>fi</sup>cial network (p, d, q) model for time series forecasting, Expert Systems with Applications 37 (2010) 479–489.

[13] M. Khashei, M. Bijari, A new class of hybrid models for time series forecasting, Expert Systems with Applications 39 (2012) 4344–4357.

[14] Y.S. Lee, L.I. Tong, Forecasting time series using a methodology based on autoregressive integrated moving average and genetic programming, Knowledge-Based Systems 24 (2011) 66–72.

[15] Y. Ma, C. Jiang, Z. Hou, C. Wang, The formulation of the optimal strategies for the electricity producers based on the particle swarm optimization algorithm, IEEE Transactions on Power Systems 21 (4) (2006) 1663–1671

[16] W.S. McCulloch, W. Pitts, A logical calculus of the ideas immanent in nervous activity, Bulletin of Mathematical Biophysics 5 (1943) 115–133.

[17] Y. Shi, R.C. Eberhart, Empirical study of particle swarm optimization, Proceedings of IEEE International Congress on Evolutionary Computation 3 (1999) 101–106.

[18] Q. Song, Seasonal forecasting in fuzzy time series, Fuzzy Sets and Systems 107 (1999) 235–236.

[19] H. Tong, Non-linear Time Series: a Dynamical System Approach, Oxford University Press, New York, 1990.

[20] F.M. Tseng, H.C. Yu, G.H. Tzeng, Combining neural network model with seasonal time series ARIMA model, Technological Forecasting and Social Change 69 (2002) 71–87.

[21] V.R. Uslu, C.H. Aladag, U. Yolcu, E. Egrioglu, A new hybrid approach for forecasting a seasonal fuzzy time series, in: International Symposium Computing Science and Engineering Proceeding Book, 2010, pp. 1152–1158.

[22] W. Wang, P.H.A.J.M. Van Gelder, J.K. Vrijling, J. Ma, Forecasting daily stream <sup>fl</sup>ow using hybrid ANN models, Journal of Hydrology 324 (2006) 383–399.

[23] R.N. Yadav, P.K. Kalra, J. John, Time series prediction with single multiplicative neuron model, Applied Soft Computing 7 (2007) 1157–1163.

[24] G. Zhang, Time series forecasting using a hybrid ARIMA and neural network model. Neurocomputing 50 (2003) 159–175.

Ufuk Yolcu is assistant professor at the Giresun University Turkey. He received the B.Sc., the M.Sc. (M.Sc. thesis title: High order fuzzy time series forecasting model based on arti<sup>fi</sup>cial neural networks) and the Ph.D. (Ph. D. thesis title: Multivariate analysis in fuzzy time series) degrees in statistics from the University of Ondokuz Mayis, Turkey, in 2003, 2008 and 2011, respectively. His research interests include fuzzy time series, arti<sup>fi</sup>cial neural networks, heuristic and evolutionary algorithms

Erol Egrioglu is associate professor at the University of Ondokuz Mayis, Turkey. He received the B.Sc. degree in statistics from the University of Ondokuz Mayis, Turkey, in 1998. He received the M.Sc. degree (M.Sc. thesis title: Bayesian analysis of ARMA model and an application) in statistics at the Faculty of Science and Arts of the University of Ondokuz Mayis, Turkey, in 2002 and the Ph.D. degree in statistics at the Faculty of Science, of the University of Hacettepe, Turkey, in 2006. His research interests include time series analysis, bayesian approaches, fuzzy time series and arti<sup>fi</sup>cial neural networks, heuristic and evolutionary algorithms.

Cagdas H. Aladag is associate professor at the Hacettepe University, Turkey. He received the B.Sc., the M.Sc. (M.Sc. thesis title: Solving a course timetabling problem by using tabu search algorithm) and the Ph.D. (Ph. D. thesis title: Using tabu search algorithm in the selection of architecture for arti<sup>fi</sup>cial neural network) degrees in statistics from the University of Hacettepe, Turkey, in 2001, 2004 and 2009, respectively His research interests include time series analysis, fuzzy time series, arti<sup>fi</sup>cial neural network, heuristic and evolutionary algorithms.
