---
otero_id: 17651
otero_key: "NT7MMSCX"
title: "Neural network system for forecasting method selection"
authors: "Chao-Hsien Chu; Djohan Widjaja"
year: "1994"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)90071-x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Neural network system for forecasting method selection

Chao-Hsien Chu $^{1}$

Iowa State University, Ames, Iowa 50011, USA

Djohan Widjaja

Price Waterhouse, Chicago, Illinois 60603, USA

Choosing an appropriate forecasting method is a crucial decision for most organizations, as the company's success is highly dependent on the accurate prediction of future. The decision, however, is not easy because many forecasting methods are available and the selection often requires extensive statistical knowledge, experience, and personal judgment. In this paper, we illustrate how can a neural network approach be used to ease this task. We first examine the general technical issues (decisions) involved in designing neural network applications. A backpropagation-based forecasting prototype is then used to demonstrate how these decisions be determined in practice.

Keywords: Neural networks; Forecasting method selection; Backpropagation; Exponential smoothing; Forecasting

![](/api/attachments/NT7MMSCX/fulltext/images/f211c977075b49f81252a5545586379419ffec7e586080a779306c8249a4aa16.jpg)

Chao-Hsien Chu is an associate professor of management at the College of Business, Iowa State University, USA. He received his BE in Industrial Engineering and MBA, both from Taiwan. His Ph.D. in Business Administration was from the Pennsylvania State University. Dr. Chu's research interests include applied artificial intelligence (expert systems, fuzzy methodology, and neural networks), manufacturing information systems, analytical modeling of JIT systems,

and cellular manufacturing/group technology. He has published articles in OMEGA, Journal of Information Systems Management, Computers and Industrial Engineering, International Journal of Production Research, Journal of Operations Management, International Journal of Operations and Production Management, among others. Dr. Chu is in the Editorial Review Board of Journal of End User Computing and the Production and Operations Management Society Journal.

## 1. Introduction

In today's competitive world, the better an organization can predict its future, the better chance it can survive. Forecasting analysis deals with the prediction of future. During the past decades, a variety of forecasting methods and computerized systems have been developed either to improve forecasting accuracy or to increase computational efficiency [2,23], forecasting yet remain as a difficult and challenging task for the following reasons: (1) the environment under which forecasting to be performed is dynamically change; therefore, the future may follow the same trend as the past but unexpected events or outliers may be arisen to disturb our logical reasoning. (2) data available for forecasting are often volatile, uncertain and incomplete, depending on the sources and how they were collected. For instance, data may be collected annually, quarterly, or monthly. Also they may be collected as was or aggregated. (3) different time horizons and thus different forecasting methods may be needed. Some decisions, for instance, new product development, capacity planning, financial planning, manpower planning etc., require a longer horizon; for others, such as material acquisition, inventory management, scheduling etc., a short horizon is normally sufficient.

Choosing an appropriate forecasting method is a complicated decision, as there are many forecasting methods available and each method dif-

![](/api/attachments/NT7MMSCX/fulltext/images/2bec76aaa6aeab27ec51570c399045ae21ca9ab1b037e6fcda6876202a384ac2.jpg)

Correspondence to: Professor Chao-Hsien Chu, College of Business, Iowa State University, 300 Carver Hall, Ames, Iowa 50011, USA. Tel.: (515) 294-9693. Fax: (515) 294-6060. E-mail: chu.c@iastate.edu.

fers in complexity, data requirements, cost and accuracy. In addition, some methods perform better in the short-term forecasting; while others do better in the long-run [22]. The decision depends not only on the items to be forecasted, sources of data, the person in charge of forecasting, and nature of forecasting methods but also on the measuring criterion to which the performance is to be evaluated [22]. Although a number of approaches, for instance, examining the autocorrelation function (ACF) and partial autocorrelation function (PAC) [3,21], automated procedures [8,13,20], and pattern recognition [19], have been suggested, extensive statistical knowledge, experience, and subjective judgments are still needed for obtaining a good performance.

Over the past years, expert systems have been introduced to aid the decision $[7,27,33]$ . One major difficulty with expert system methodology is to acquire, represent, and build a good knowledge base (i.e., knowledge acquisition and representation). Since human knowledge is often implicit in nature and sometimes conflicts to each other, it is very difficult to verify and formalize them in an explicit manner using production rule and frame etc.. Besides, other than being a time consuming and labor intensive task, formalizing implicit to explicit knowledge may result in losses of critical information due to the incomplete, vague, and fuzzy nature of data $[35]$ .

Neural networks have recently been proposed to possibly remove these deficiencies. Neural networks can automatically learn previous experience from examples without going through tedious acquisition and representation procedures. Because of this, it has attracted much attention from both industry and academics. Many successful applications have been reported in the literature $[4,9,24,25,28,30,32,35]$ , but little effort has been put into exploring the technical details towards developing such applications; thus, many critical decisions yet remain state-of-the-art and require numerous experiments or trial and error $[17]$ . Moreover, though neural networks can solve many problems conventional systems have found intractable, it is still deficient at solving problems which involve complex computations $[5,6,26]$ . The purposes of this paper are two fold: (1) to examine the technical issues involved in designing neural network applications and (2) to illustrate through a prototype of neural system, NNFS, how these critical decisions be determined in practice.

## 2. Neural network approaches to forecasting

Neural networks, sometimes called connectionist systems, artificial neural systems, or neurocomputers, are computing systems that process information by their dynamic state in response to the external inputs [6]. A neural network normally consists of several components: (1) A set of neurons. Neurons are simple processing units that send and receive signals from outside environment or other neurons in the network. (2) Pattern of connectivity. Neurons form a network by linking to each other; these links can be fully or partially connected. (3) Propagation rule. A propagation rule is used to aggregate input signals from other neurons. (4) Activation rule. Once input signals are aggregated, the neuron applies an activation rule to convert the weighted input with its previous level of activation into a new level of activation. (5) Transfer function. A transfer function then maps the activation value of a neuron into an output signal to be sent to other neurons. (6) Learning rule. Learning in a neural network involves a process of changing the pattern and strength of connectivity among neurons [28].

Neural networks have been proven to be an effective approach for a broad spectrum of applications. For example, they have been successfully used in many business domains such as economic prediction, financial analysis, mortgage loan evaluation, credit approval, bankruptcy prediction, stock market prediction etc. [9,16,31,32,34]. Neural networks can be designed to assist forecasting analysis in two ways:

## 2.1. Direct forecasting

This approach uses a neural network to approximate the original time series or some transformed version of the series. It uses the explicit logic of a neural network to express the future value in terms of previous values; that is,

$$
\tilde {X} (t + 1) = \mathcal {R} (X (t), X (t - 1), \dots , X (t - n))\tag{1}
$$

According to [10], the method can only be used to predict the future value one at a time. In order to predict more than one value into the future, the predictions must be fed back into the network as if they were data; that is,

$$
\begin{array}{c} \tilde {X} (t + 2) = \mathcal {R} \big (\tilde {X} (t + 1), X (t), X (t - 1), \dots , \\ X (t - (n - 1)) \end{array}\tag{2}
$$

Although direct forecasting via neural networks has been successfully used in deterministic time series, it has not performed as well as traditional forecasting methods for the short-term and noisy time series $[10,14]$ . The task of designing neural networks for direct forecasting is also quite complicated, as the required number of hidden layers and the number of processing units in each hidden layer must be carefully selected to match the complication of the problem. If the logic behind the time series is very complicated, it may need more than one hidden layer and the number of neurons in each layer must be increased $[25]$ .

## 2.2. Indirect forecasting

Neural network also can be designed to assist in (1) selecting weights for combining forecast or (2) selecting an appropriate forecasting method:

(1) Combining weights selection. Foster etc. [10] proposed a backpropagation network to select appropriate weights for combining six exponential smoothing methods. The network takes input data as well as features embedded in the data, such as the existence of consistent long and short term trends, a consistent increase or decrease in the series over several time steps, the amount of variation about the mean, and the goodness of the least squares fit of data, to produce output weights, $\omega_{k}$ , which are then used to combine traditional forecasts, $f_{k}(t+1)$ ; thus, one can obtain an aggregated forecast as:

$$
\tilde {X} (t + 1) = \sum_ {k = 1} ^ {K} \omega_ {k} f _ {k} (t + 1)\tag{3}
$$

This approach is based upon an observation that combining forecasts could lead to improve forecasting performance [22]. According to [10], the neural network approach performs better than the traditional equal-weight approach. The method also performs better than direct neural network forecasting for short-term and noisy time series.

(2) Forecasting method selection. This approach relies on the pattern recognition capability of a neural network to select an appropriate forecasting method. One can then use the proposed method to compute the forecasting values.

## 3. Technical design issues

Developing a successful neural application involves several stages and critical decisions $[1]$ . In this section, we will discuss the design issues in details and illustrate how a prototype of forecasting system, NNFS, was built and trained to assist in selecting an appropriate exponential smoothing method.

## 3.1. Conceptual framework

One of the major issues towards designing a neural system is to determine its logical structure. Figure 1 depicts the major modules and framework used in designing NNFS. The major part of system was written in BASIC language, while the demand pattern recognition and forecasting method selection networks were built and simulated using the BrainMaker software [4]. Please refer to sections 3.4, 3.13, and 3.14 and Figure 5 for related technical details.

![](/api/attachments/NT7MMSCX/fulltext/images/3198f5e1645ebb366732a65ec1942b57373db52373e96dd99f648019bbc067ce.jpg)  
Fig. 1. The conceptual framework of NNFS.

(1) Data entry and updating. This module provides three major functions – data entry, data updating, and graphic display. A user can either enter data from the keyboard or retrieve data from a file that was stored in an ASCII format. The user also can update the data file and display the time series in graphic mode, under which the demand pattern can be visually examined.

(2) Data representation. NNFS uses three type of autocorrelation analyses to represent demand patterns. See section 3.2 for a detailed discussion on the data representation scheme.

(3) Demand pattern recognition (DPR). This module allows users to recall the trained DPR network to identify the demand pattern embedded in a time series. DPR has been designed and trained to recognize six demand patterns: stationary, stationary plus seasonal, linear trend, linear trend plus seasonal, quadratic trend, and quadratic trend plus seasonal.

(4) Forecasting model selection (FMS). The system then asks the user to enter the number of periods to be forecasted, the forecasting horizon (short, medium, or long term), and the industry type to which the data belong. These information together with the identified demand pattern from previous stage are fed into another trained network, FMS, for selecting an appropriate forecasting method. Please note that demand pattern is the major input to FMS network. We include the other two inputs for demonstrating the network's capability in taking other factors into consideration. Currently, the FMS has been trained to select one among six exponential smoothing methods for three types of industries – food and beverages, electrical machinery, and paper and pulp. The system is flexible and can be trained to recognize data from other industries.

![](/api/attachments/NT7MMSCX/fulltext/images/e0e076d7177ecf5206f846b824fadd7e68865f2e9076148f904d5a6861767266.jpg)  
Fig. 2. Representing knowledge for demand patterns.

(5) Forecasting. The user can use the recommended method or any other forecasting method available in the system for forecasting analysis. Also, the system can summarize the performance in terms of mean square error (MSE) and mean absolute percent error (MAPE) for all the models specified. NNFS contains six smoothing models: (1) single exponential smoothing; (2) Brown's linear exponential smoothing; (3) Brown's quadratic exponential smoothing; (4) Holt's two parameter linear exponential smoothing; (5) adaptive-response-rate single exponential smoothing; and (6) Winters' seasonal method. A theoretical examination of the smoothing models can be found in [11,12]. The selection of smoothing models for this system is due to several practical considerations [12]: (1) smoothing models are relatively simple; (2) components of the models, for example, trend and seasonality, have intuitive meaning to the user; (3) only limited data storage and moderate computational effort are required; (4) tracking signal tests for monitoring forecast can be easily applied; (4) empirical studies have shown that smoothing model is quite accurate compared with more complex forecasting methods such as Box-Jenkins; and (5) smoothing methods are robustic to particular data patterns or outliers.

## 3.2. Data representation

Representing input data in a format that a computer can uniquely identify their embedded features is a major bottleneck towards designing a neural system $[26]$ . For forecasting purpose, one can directly use the historical data as inputs or to perform a preprocessing such as autocorrelation analysis etc.. The first approach is normally used by direct forecasting $[10,14]$ . We used the latter approach in representing data. Figure 2 shows the six popular demand patterns considered in the DPR network and their corresponding autocorrelation results. As can be seen from the figure, one needs to perform three types of autocorrelation analyses in order to correctly represent and distinguish these patterns. The first autocorrelation, which uses actual data, can only separate the stationary and pure seasonal patterns from others. However, if the stationary pattern is noisy or the seasonal pattern is not strong enough, we will have difficulty in distinguishing the stationary pattern from pure seasonal pattern. The second autocorrelation, which uses the first-difference of actual data, will eliminate the linear trend from the data; thus, with results from the first two autocorrelation analyses, one can then separate the linear trend pattern from quadratic trend pattern and the stationary pattern from pure seasonal pattern. The third autocorrelation, which uses the second-difference of actual data, will eliminate the quadratic trend from the data. Therefore, with results from all three types of autocorrelation, one can further separate the quadratic trend pattern from quadratic trend plus seasonal pattern. A detailed discussion of autocorrelation analysis can be found in [3,21,23].

## 3.3. Selection of network paradigm

Neural network is a fast growing subject in which more than 50 paradigms have been proposed over the past years [25,30]. Each topology has unique features and may be only appropriate for a few specific applications [1]. Selecting a suitable topology for a particular application yet remains an art. Among the available paradigms, backpropagation model has the largest number of successful applications. In fact, it has almost become the standard for modeling, forecasting, and classification domains. Because of its popularity, successful record, and several canned software are available for public use [4,24,25], we selected it for study.

The backpropagation model involves a forward- followed by a backward- propagating step. Many parameters and decisions involved in developing a backpropagation network (See Table 1). We illustrate some of those decisions below. An extensive review of the backpropagation neural model can be found in [25,28].

<table><tr><td>·Determine the number of training and test data sets.</td></tr><tr><td>·How to create training and test data sets?</td></tr><tr><td>·Select the method of transferring data into suitable input values.</td></tr><tr><td>·Determine the number of hidden layers.</td></tr><tr><td>·Determine the pattern of connectivity.</td></tr><tr><td>·Determine the network size:</td></tr><tr><td>– Number of processing units (PE) in the input layer.</td></tr><tr><td>– Number of processing units (PE) in the hidden layers.</td></tr><tr><td>– Number of processing units (PE) in the output layer.</td></tr><tr><td>·Determine the initial input weights.</td></tr><tr><td>·Select a propagation rule:</td></tr><tr><td>Weighted sum, cumulative weighted sum, maximum, minimum, majority, or product.</td></tr><tr><td>·Select an activation rule:</td></tr><tr><td>Identity or threshold functions.</td></tr><tr><td>·Select a transfer function:</td></tr><tr><td>Identity, linear, sigmoid, sine, or hyperbolic tangent function.</td></tr><tr><td>·Select a learning rule:</td></tr><tr><td>Delta rule, cumulative delta rule, or generalized delta rule.</td></tr><tr><td>·Determine the learning parameters:</td></tr><tr><td>– Learning rate ( $\beta$ ).</td></tr><tr><td>– Momentum term ( $\alpha$ ).</td></tr><tr><td>·Select diagnostic tools:</td></tr><tr><td>Root-Mean-Squared error, confusion matrix, or histogram.</td></tr><tr><td>·How to reduce the training time?</td></tr></table>

## 3.4. Selection of development tool

Selecting a programming tool for developing and testing neural networks is a much simple task, as there are only few options opened for the selection. Some researchers prefer using high-level programming languages, such as C, PASCAL, or BASIC, because they are more flexible and can be easily interfaced or incorporated with conventional applications. But it takes much time to design and test the system, as every technical details must be programmed from the scratch. Other people like to use development tools or environment, such as BrainMaker or Neuralworks Professional II, because these tools are much easier to use and can save much programming time. However, most of them suffer from inflexibility because only one or a few network paradigms are provided. Also, they cannot be used to test new learning rules and parameters. We used BASIC to design the main program and user-interface and to perform all the computational analyses. In addition, we used the Brain-Maker software to build, train and test the neural networks.

## 3.5. Determination on the number of hidden layers

The major purpose of a hidden layer is to serve as a feature detector or filter, which perform a mapping between input units and output units. One major limitation of single-layer neural networks is that they can only classify linearly separable patterns. For more complicated problems or non-linearly separable patterns, a multilayer networks is normally needed. Backpropagation networks may contain more than one hidden layer with each layer fully connected to the layers below and above it. According to [17], although most problems can be solved effectively with a single hidden layer, determining the number of hidden layers for a complicated problem is tricky and normally requires tedious experiments or trial-and-error. For example, the neural network for stock market prediction requires two hidden layers, each layer with different transfer functions [25]. Since most time series include noises and exhibit a non-linear structure, a simple backpropagation model (without hidden layers) is theoretically incapable. A network with one or more hidden layer has to be considered. Computational experience from previous studies [10,14] has shown that the three-layer networks are sufficient for obtaining reasonable forecasting results.

## 3.6. Determination on the network size

Determining an appropriate network size for a complex problem is a very difficult and time consuming task. Many designers either follow a rule of thumb or copy the design specifications from previous successful applications $[1,4,5]$ . Figures 3 and 4 show the two networks – DPR and FMS – involved in NNFS with detailed discussion follows:

(1) Input layer. The required number of input neurons is often determined by the number of unique features embedded in the data $[1,35]$ . In the DPR network, it depends on the number of periods of autocorrelation data. Since the input data allows for 36 data periods, we have 35 values on the regular autocorrelation, 34 values on the first-difference autocorrelation, and 33 values on the second-difference autocorrelation, a total of 105 neurons with three as dummy (due to a limitation of the BrainMaker software) is included in the input layer. In the FMS network, as only three factors – demand pattern, forecasting horizon, and type of industry – are considered in the prototype, the number of input neurons is three.

![](/api/attachments/NT7MMSCX/fulltext/images/4f7917437e55bd30e888f2e6f9cf2ede379430b7abd65bfc17ca0dd39798543d.jpg)  
Fig. 3. Demand Pattern Recognition (DPR) neural network.

(2) Output layer. The required number of neurons for output layer is often determined by the number of expected output patterns $[1,4]$ .

![](/api/attachments/NT7MMSCX/fulltext/images/8facbc36b4d4905f1062ee5d86aff571e0dba5ae40249e7589461f4035ddea6d.jpg)

FH: Forecasting Horizon    BQ: Brown's Quadratic Exp.

TI: Type of Industry HE: Holt's Exponential

DP: Demand Pattern AD: Adaptive Response Exp.

SE: Simple Exponential WI: Winters' Exponential

Fig. 4. Forecasting Method Selection (FMS) neural network.

Since we intend to recognize six demand patterns, the output layer for the DPR network consists of six neurons, with each neuron representing a pattern. The number of output neurons for the FMS network is also six because six exponential smoothing models are under consideration.

(3) Hidden layers. The decision for hidden layers is much more complicated. Several principles have been proposed: (1) the size of a hidden layer should not be the smallest nor the largest among layers [1]; (2) a good guess for the size of a hidden layer is between 50% to 75% of the total number of input and output neurons [4]; (3) the theoretical upper bound for the number of hidden units is limited by the number of training data [17]. In our trial test, we followed the second principle and used 75% and 60% of the total input and output neurons for the DPR and FMS networks. These numbers seem to work fine though they may not necessitate the optimal choice.

## 3.7. Selection of propagation and activation functions

Propagation function is used to compute the aggregated input of a processing element. Although several options, such as weighted sum, cumulative sum, maximum, minimum, majority, and product [25], are available for a backpropagation network, weighted sum method has been popularly used in most applications. We select it due for its popularity. In fact, it is the only option available in the BrainMaker software. Activation function is used to calculate the activation value of a processing unit. Although several options, for example, identity and threshold functions, are available for a backpropagation network, we used identity function due for its popularity.

Table 2  
Formulae for generating training and test data

<table><tr><td>Demand Pattern</td><td>Mathematical Expression</td></tr><tr><td>Stationary</td><td>A + RND (SEED)</td></tr><tr><td>Linear Trend</td><td>A + T * RND (SEED)</td></tr><tr><td>Quadratic Trend</td><td>A +  $T^{2}$  * RND (SEED)</td></tr><tr><td>Seasonality</td><td>A * SIN (2 * B/C * T)</td></tr><tr><td>A:</td><td>Leveling (average) parameter</td></tr><tr><td>RND (SEED):</td><td>Random number generator</td></tr><tr><td>T:</td><td>Time period</td></tr><tr><td>B:</td><td>Seasonal parameter</td></tr><tr><td>C:</td><td>Number of seasons</td></tr></table>

Table 3  
Summary of demand pattern recognition and forecasting results

<table><tr><td rowspan="2">Data Set</td><td rowspan="2">Demand Pattern</td><td rowspan="2">Identified pattern</td><td rowspan="2">Source</td><td rowspan="2">Measures</td><td colspan="6">Available Forecasting Methods *</td><td colspan="2">Recommended</td></tr><tr><td>SE</td><td>BL</td><td>BQ</td><td>HE</td><td>AD</td><td>WI</td><td>Method</td><td>Rank</td></tr><tr><td></td><td></td><td></td><td></td><td>MSE</td><td>610.83</td><td>638.47</td><td>661.88</td><td>1382.42</td><td>573.26</td><td>1127.05</td><td></td><td>1</td></tr><tr><td>1</td><td>LT+S</td><td>LT+S</td><td>[23]</td><td>MAPE</td><td>9.62</td><td>10.16</td><td>9.84</td><td>15.76</td><td>9.95</td><td>13.57</td><td>AD</td><td>3</td></tr><tr><td></td><td></td><td></td><td></td><td>MSE $^{\dagger}$ </td><td>6.67</td><td>4.49</td><td>3.62</td><td>12.04</td><td>3.20</td><td>17.62</td><td></td><td>2</td></tr><tr><td>2</td><td>QT+S</td><td>QT</td><td>[23]</td><td>MAPE</td><td>16.55</td><td>13.06</td><td>11.38</td><td>22.21</td><td>11.28</td><td>39.12</td><td>BQ</td><td>2</td></tr><tr><td></td><td></td><td></td><td></td><td>MSE</td><td>58.86</td><td>61.18</td><td>65.54</td><td>66.40</td><td>52.36</td><td>105.94</td><td></td><td>1</td></tr><tr><td>3</td><td>LT+S</td><td>LT+S</td><td>[15]</td><td>MAPE</td><td>27.28</td><td>29.30</td><td>28.46</td><td>31.50</td><td>25.76</td><td>38.18</td><td>AD</td><td>1</td></tr><tr><td></td><td></td><td></td><td></td><td>MSE</td><td>53.14</td><td>59.11</td><td>66.43</td><td>70.58</td><td>51.23</td><td>125.49</td><td></td><td>1</td></tr><tr><td>4</td><td>ST+S</td><td>ST+S</td><td>[15]</td><td>MAPE</td><td>7.80</td><td>8.52</td><td>9.05</td><td>9.47</td><td>7.86</td><td>12.66</td><td>AD</td><td>2</td></tr><tr><td></td><td></td><td></td><td></td><td>MSE</td><td>95.12</td><td>69.83</td><td>81.33</td><td>468.27</td><td>104.30</td><td>122.41</td><td></td><td>1</td></tr><tr><td>5</td><td>LT+S</td><td>LT+S</td><td>[15]</td><td>MAPE</td><td>14.17</td><td>13.19</td><td>13.79</td><td>38.31</td><td>15.95</td><td>15.55</td><td>BL</td><td>1</td></tr><tr><td></td><td></td><td></td><td></td><td>MSE</td><td>1.54</td><td>0.52</td><td>0.47</td><td>2.14</td><td>0.82</td><td>1.13</td><td></td><td>2</td></tr><tr><td>6</td><td>LT</td><td>LT</td><td>[18]</td><td>MAPE</td><td>6.72</td><td>3.92</td><td>3.40</td><td>7.75</td><td>4.97</td><td>5.16</td><td>BL</td><td>2</td></tr><tr><td></td><td></td><td></td><td></td><td>MSE $^{\ddagger}$ </td><td>4.45</td><td>5.24</td><td>6.02</td><td>16.39</td><td>5.49</td><td>6.26</td><td></td><td>1</td></tr><tr><td>7</td><td>ST</td><td>ST</td><td>[29]</td><td>MAPE</td><td>7.95</td><td>9.43</td><td>10.40</td><td>20.28</td><td>9.57</td><td>10.88</td><td>SE</td><td>1</td></tr><tr><td></td><td></td><td></td><td></td><td>MSE $^{\dagger}$ </td><td>2.89</td><td>3.21</td><td>3.67</td><td>4.91</td><td>3.31</td><td>6.72</td><td></td><td>1</td></tr><tr><td>8</td><td>QT</td><td>QT</td><td>[21]</td><td>MAPE</td><td>14.86</td><td>15.29</td><td>16.22</td><td>19.46</td><td>15.40</td><td>25.16</td><td>SE</td><td>1</td></tr><tr><td></td><td></td><td></td><td></td><td>MSE</td><td>127.29</td><td>114.15</td><td>133.02</td><td>143.79</td><td>157.32</td><td>95.60</td><td></td><td>1</td></tr><tr><td>9</td><td>LT+S</td><td>LT+S</td><td>[23]</td><td>MAPE</td><td>6.46</td><td>6.41</td><td>6.92</td><td>7.04</td><td>7.14</td><td>6.11</td><td>WI</td><td>1</td></tr><tr><td></td><td></td><td></td><td></td><td>MSE</td><td>5.01</td><td>5.58</td><td>5.89</td><td>36.87</td><td>5.07</td><td>10.39</td><td></td><td></td></tr><tr><td>10</td><td>ST+S</td><td>ST+S</td><td>[23]</td><td>MAPE</td><td>1.93</td><td>2.13</td><td>2.17</td><td>5.02</td><td>2.05</td><td>2.44</td><td>SE</td><td>1</td></tr></table>

\* See Figures 3 and 4 for the abbreviation of notations  
$^{\dagger}$ In the scale of $10^{7}$  
$^{\ddagger}$ In the scale of $10^{4}$

## 3.8. Selection of transfer function

Several options of transfer function, such as identity, linear, sigmoid, hyperbolic tangent (TanH), and sine functions [25], are available for a backpropagation network. The selection mainly depends on the nature of input data and what the network is trying to learn. As a rule of thumb, if the problem is to pick up an exceptional structure such as bankruptcy prediction and stock picking, hyperbolic tangent function works better; on the other hand, if the problem is to classify an object from the others, sigmoid function is a better choice [17]. In our cases we select sigmoid function because both problems belong to classification domain.

## 3.9. Selection of learning rule

Backpropagation network can use either delta rule, cumulative delta rule, or generalized delta rule for learning purpose. Generally speaking, the delta rule works fine for deterministic data, but if the data are noisy, the generalized delta rule works better [17]. Since most time series are noisy, we elected to use the generalized delta rule for both networks. The rule can be expressed as:

$$
\Delta W _ {j i} (t + 1) = \beta E | X | | X | + \alpha \Delta W _ {j i} (t)\tag{4}
$$

Where, $W_{ji}$ is a weight vector; $\beta$ represents the learning rate; E is the error from output; X is an input vector; and $\alpha$ is a momentum term.

## 3.10. Determination on the learning parameters

Two parameters, $\beta$ and $\alpha$ , involved in the generalized delta rule. $\beta$ , which measures the speed of convergence, is a constant between 0 and 1. If a larger value was used, the learning will be faster, but it will cause the network to oscillate around the minimum. On the other hand, if a smaller value was used, though it can prevent the network from oscillating, it will take a very long time to arrive at the minimum. $\alpha$ is the momentum term that often makes the next weight change in more or less the same direction. The $\alpha$ value also can keep the network from falling into a local minimum. There is no exact rule for determining the $\beta$ and $\alpha$ values. In general, the default values provided by the software vendors work fine [17]. We used the default values provided in BrainMaker; that is, 1.0 and 0.9 for $\beta$ and $\alpha$ respectively. Our experiments show that these values are appropriate for our application.

## 3.11. Preparation of training data

Selecting appropriate training data sets is another key decision for an effective and successful implementation of neural systems. Both quantity and quality of the data are important. As a rule of thumb, the more training data sets provided for the system, the longer it takes to train the network. The training data for this study contains 120 data sets (20 sets, with different parameters and noises, from each demand pattern) generated from mathematical equations. Table 2 summarizes the equations used to generate the training and test data sets. Where, the A parameter is used to control the average level of a time series and the random number, RND (SEED), is used to add noises to the series. We repeatedly used these data sets (for DPR network) and the corresponding simulated forecasting results (for FMS network) to train the networks until the root-mean-squared (RMS) error lower than an acceptable level (normally 0.1).

## 3.12. Reduction of training time

How to reduce training time is another critical issue many researchers have been worked for years. Several methodologies, for example, adding a momentum term, varying the learning rate by starting a larger value and progressing to smaller values, adding a bias units, using a second derivatives to produce a more accurate estimate of the correct weight change etc., have been proposed in the literature $[9,28,25,32]$ . There has no research done to study their relative performance. We used the strategy suggested in the BrainMaker; that is, we first increased the tolerance and then reduced it gradually. This strategy allows us to reduce the training time from two hours to less than one hour in an IBM PC/AT with 8 MHZ speed.

```txt
- MAIN PROGRAM:
GOSUB MENU    »* Call System Menu Module **
GOSUB ENTRY    »* Call Data Entry Module **
GOSUB UPDATE    »* Call Data Updating Module **
GOSUB GRAPHIC »* Call Graphic Display Module **

- AUTOCORRELATION ANALYSIS:
GOSUB AUTO    »* Call Autocorrelation Module **
OPEN "FCT\BRAINRTS.IN" FOR OUTPUT AS #1
REM    ** Save information for using by DPR network **
- DEMAND PATTERN RECOGNITION:
CHDIR "FCT"
REM    ** Change to sub-directory of BrainMaker **
SHELL "brainmak -batch"
REM    ** Activate BrainMaker in batch mode **
CHDIR “..”
REM    ** Switch back to NNFS directory **
- FORECASTING METHOD SELECTION:
OPEN "FCT\BRAINRTS.OUT" FOR OUTPUT AS #2
REM    ** Retrieve simulated results from BrainMaker **
REM    ** Other parts are the same as DPR network **
- FORECASTING AND PERFORMANCE EVALUATION:
GOSUB FCC    »* Call Forecasting Module **
END
```

## 3.13. User-interface design

The major weakness with most neural network tools is the lack of facility for developing friendly user-interface and the lack of computational power for computationally intensive applications. To solve these deficiencies, we used the BASIC programming language to develop the user-interface (such as menu selection and graphic display) and to perform the necessary numeric computations (such as autocorrelation and forecasting analyses). NNFS is a menu-driven system, in which the user can select options from menus. Inside each menu, question/answer dialogues are used to inquire additional data/information. NNFS also allows the user to review the graph of the input data, the data contents, and the identified demand pattern in one screen.

## 3.14. System integration and maintenance

Although BrainMaker allows users to built, train, and test networks in either interactive or batch modes. The current version of BrainMaker does not provide adequate interface with conventional programming languages. We used the "SHELL" facility of DOS to integrate neural networks with the major programs, written in BASIC. Figure 5 illustrates how the interface work, in which only those statements for demand pattern recognition are actually displayed in BASIC commands. Shell facility allows one to load and execute the neural network program without stopping the execution. Since all of the data are stored in the ASCII format, the system can be easily maintained by using a professional editor, Lotus-123, or word processor.

## 4. Performance evaluation

We have tested the performance of the demand pattern recognition (DPR) network using two groups of data sets. In the first group, we used a random number generator to generate 180 different data sets (30 data sets, with different parameters and noises, for each demand pattern). Please refer to Table 2 for mathematical expressions used to generate these test data sets. Despite different parameters and noises are presented in the data, the DPR network successfully

Fig. 5. Illustration of system integration.

recognized 173 data sets (i.e., 96.11% successful rate). This indicates that the DPR network is quite robust to different environment.

We further tested the DPR network with 10 data sets collected from the open literature [15,18,21,23,29]. Table 3 summarizes the results of demand pattern recognition. As can be seen from the table, the network again performed quite well on the real-world data. It successfully recognized 9 data sets with a $90\%$ success rate. The only data set missed has a quadratic trend plus seasonality but was recognized as having a quadratic trend only. The possible reason for the failure could be due to insufficient number of observations for identifying the seasonal factor.

We then used the same data sets from the literature to evaluate the performance of the FMS network. We first ran the system to recommend an appropriate method and then computed the forecasting using all six exponential smoothing methods. The results are then evaluated in terms of mean square error (MSE) and mean absolute percent error (MAPE). Table 3 also summarizes the forecasting results in terms of MSE and MAPE. Among the 10 data sets tested, the FMS correctly recommended the best method for 8 data sets, according to the MSE criterion and 6 data sets, according to the MAPE criterion. The success rate is 80% and 60% respectively. For those cases by which the system did not recommend the best method, the second or the third ranked method was normally recommended. Considering the facts that some of these data sets are noisy and in fact there has no single forecasting method performed well under different measuring criteria [22], the results of FMS network are fairly good and stable. Worth noting is that the FMS network tends to recommend the adaptive response-rate smoothing method over the winters' method if the seasonal pattern of the data is not strong enough. Again, this may be due to the insufficient data periods for identifying the seasonality.

## 5. Conclusions

In this study, we have examined the critical issues in general and illustrated in specific how these decisions are made towards developing backpropagation networks for forecasting method selection. Though a few guidelines can be followed, most decisions are still problem dependent. A considerable amount of research is now under way centering around: (1) optimizing the number of neurons in the hidden layers, (2) improving the speed of learning, (3) generalizing the pattern of connectivity, (4) analyzing the scaling, generalization, and fault tolerance properties, and (5) employing higher order correlations and arbitrary threshold functions [30]. We have also tested and evaluated the systems using both simulated and actual data from the literature. As shown from the evaluations, the system has a very high success rate of identifying correct demand patterns (over 90%) and recommending an appropriate smoothing forecasting method (70% in average). In this regard, using neural networks for forecasting method selection can be claimed as a success.

Neural-based forecasting systems have several advantages over rule-based systems: First, because the development process needs not to involve those time consuming tasks such as acquisition and formalization, they take shorter time to develop. Second, since the systems only perform simple calculations, their processing time is shorter; on the contrary, expert systems involve extensive and time consuming searches. Third, neural systems can update knowledge over time as long as more training data sets are provided; while, a knowledge engineer must present to reconstruct and extend the knowledge base for the expert systems. Fourth, the systems can learn new patterns that are not previously available in the training data sets; while, new rules must be acquired for the expert systems. Fifth, neural systems are more robust than expert systems: they can be trained and thus recognize data that contains noises but it is very difficult (if not impossible) to represent noisy information in production rules. Finally, a human expert needs not be presented when one developing the neural systems; thus, one can reduce the difficulty of finding appropriate experts and verifying the possible conflict among experts.

However, neural systems still have some shortcomings which deserve further improvement. First, unlike expert systems, they cannot explain “why” and “how” the decision making was made. One possible solution is to integrate neural networks approach with expert systems technology. Second, accuracy of the neural systems is highly dependent on the quality and quantity of the training data; therefore, the selection of training data sets should be with care. Finally, as there is no standard procedure available for developing neural network applications, the development process yet requires tedious experiments and try-and-error.

## References

[1] D. Bailey and D. Thompson, How to Develop Neural Network, AI Expert (June 1990) 38–47.

[2] C.E. Beaumont, E. Mahmoud and V.E. McGee, Microcomputer Forecasting Software: A Survey, Journal of Forecasting 4, No. 3 (1985) 305–311.

[3] G.E.P. Box and G.M. Jenkins, Time Series Analysis Forecasting and Control (Holden-Day, San Francisco, CA., Revised Edition, 1976).

[4] BrainMaker, User Guide and Reference Manual (California Scientific Software, California, 1989).

[5] C. Butler and M. Caudill, Naturally Intelligent Systems (The MIT Press, Boston, MA., 1990).

[6] M. Caudill, Neural Network Primer (Miller Freeman Publications, San Francisco, CA, 1989).

[7] C.-H. Chu and K.-Y. Tsang, On the Design of a Forecasting Expert System, Proceedings of National Decision Science Conference (November 1989).

[8] L.W. Coopersmith, Automatic Forecasting Using the FLEXICAST System, TIMS Studies in the Management Science, 12 (1979) 265–278.

[9] J. Dayhoff, Neural Network Architecture (Van Nostrand Reinhold, New York, 1990).

[10] B. Foster, F. Collopy, and L. Ungar, Neural Network Forecasting of Short, Noisy Time Series, a paper presented at National TIMS/ORSA Meeting, Nashville, TN., (May 1991).

[11] E.S. Gardner, Jr., Exponential Smoothing: The State of the Art, Journal of Forecasting 4, No. 1 (1985) 1–28.

[12] E.S. Gardner, Jr., Smoothing Methods for Short-Term Planning and Control, in: S. Makridakis and S.C. Wheelwright, Eds., The Handbook of Forecasting (John Wiley & Sons, New York).

[13] G.W. Hill and D. Woodworth, Automatic Box-Jenkins Forecasting, J. Opl Res. Soc. 31 (1980) 413–422.

[14] B.J. Huffman and T.R. Hoffmann, Application of Neural Networks in Time Series Forecasting, Proceedings of MIDWEST Decision Science Conference (1989) 162–164.

[15] D. Johnson and M. King, Basic Forecasting Techniques (Butterworth & Co., Ltd., London, 1988).

[16] C.C. Klimasauskas, Applying Neural Networks, Part 2: A Walk Through the Application Process, PC AI (March/April 1991) 27–34.

[17] C.C. Klimasauskas, Applying Neural Networks, Part 3: Training a Neural Network, PC AI (May/June 1991) 20–24.

[18] G. Kress, G., Practical Techniques of Business Forecasting: Fundamentals and Applications for Marketing, Production, and Financial Managers (Quorum Books Greenwood Press, Westport, Connecticut, 1985).

[19] K.C. Lee and S.J. Park, Decision Support in Time Series Modeling by Pattern Recognition, Decision Support Systems 4 (1988) 199–207.

[20] G. Libert, An Automatic Procedure for Box-Jenkins Model Building, European J. of Operations Research 17 (1984) 95–103.

[21] V.A. Mabert, An Introduction to Short Term Forecasting Using the Box-Jenkins Methodology (American Institute of Industrial Engineers, Norcross, Georgia, 1975).

[22] S. Makridakis, A. Andersen, R. Carbone, R. Filder, M.

Hibon, Lewandowski, J. Newton, E. Parzen and R. Winkler, The Accuracy of Extrapolation Methods: Results of a Forecasting Competition, Journal of Forecasting 1, No. 2 (1982) 111–152.

[23] S. Makridakis, S. Wheelwright and V. McGee, Forecasting: Methods and Applications 2nd Ed. (John Wiley & Son, New York, 1983).

[24] J.L. McClelland and D.E. Rumelhart, Explorations in Parallel Distributed Processing: A Handbook of Models, Programs, and Exercises (The MIT Press, MA., 1988).

[25] Neuralware Inc., Neuralworks Professional II: User Guide (Neuralware Inc., Pittsburgh, PA., 1989).

[26] Y.-H. Pao, Adaptive Pattern Recognition and Neural Networks (Addison-Wesley Publishing Company, Inc., MA., 1989).

[27] S. Rahman, Formulate and Analysis of a Rule-Based Short-Term Load Forecasting Algorithm, Proceedings of IEEE 78 (1990) 805–816.

[28] D.E. Rumelhart, J.L. McClelland and the PDP Research Group, Parallel Distributed Processing: Exploration in the Microstructure of Cognition Vol. 1 (The MIT Press, MA., 1989).

[29] N. Seitz, Business Forecasting: On Your Personal Computer, (Reston Publishing Company, Inc., Reston, VA., 1984).

[30] P.K. Simpson, Artificial Neural Networks: Foundations, Paradigms, Applications, and Implementations (Pergamar Press, New York, 1990).

[31] K.Y. Tam, Neural Network Models and the Prediction of Bank Bankruptcy, OMEGA: The International Journal of Management Science 19, No. 5 (1991) 429–445.

[32] P.D. Wasserman, Neural Computing: Theory and Practice (Van Nostrand Reinhold, New York, 1989).

[33] R.R. Weitz, NOSTRADAMUS: A Knowledge-Based Forecasting Advisor, International Journal of Forecasting 2, (1986) 273–282.

[34] H. White, Economic Prediction Using Neural Networks: The Case of IBM Daily Stock Returns, Working Paper (Department of Economic, University of California, San Diego, 1989).

[35] Y.O. Yoon, R.W. Brobst, P.R. Bergstresser and L.L. Peterson, A Connectionist Expert System for Dermatology Diagnosis, Expert System: Planning, Implementation, Integration 1, No. 4 (1990) 22–31.
