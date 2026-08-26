---
otero_id: 19239
otero_key: "JNCHHPQX"
title: "A neural network approach to forecasting model selection"
authors: "Jeffrey E. Sohl; A.R. Venkatachalam"
year: "1995"
journal: "Information & Management"
doi: "10.1016/0378-7206(95)00033-4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# A neural network approach to forecasting model selection

Jeffrey E. Sohl \*, A.R. Venkatachalam

Department of Decision Sciences, Whittemore School of Business and Economics, University of New Hampshire, Durham, New Hampshire
NH 03824, USA

## Abstract

The literature has shown that no one model provides the most accurate forecasts. The focus has instead shifted to identifying the characteristics of the time series in order to provide guidelines for choosing the most appropriate extrapolation model. In this paper we test the feasibility of employing the neural network structure for model selection. To accomplish this objective, a set of time series characteristics, representing the domain knowledge, is established. A back propagation neural network is then constructed with eleven input nodes representing six time series characteristics. The output nodes of the neural network represent nine time series forecasting methods grouped into three categories. The results indicate that the neural network approach can assist the practitioner in the selection of the appropriate forecast model.

Keywords: Neural networks; Model selection; Forecasting; Intelligent systems

## 1. Introduction

Interest in extrapolation model selection research was initially provided by the M-competition of Makridakis et al. [20]. Following this, Schnaars [25] compared the results of five extrapolation models and a random-walk model for forecasting across nearly one hundred sales series and several forecasting horizons. His result was a set of empirically based boundary conditions. Using an alternative approach, Dalrymple [10] provided a summary of current sales forecasting practices, as a means of deciding what methods are most commonly used. Fliedner and Mabert [15] considered the effect of product group size and group criteria on forecasting performance and Gross and Sohl [18] assessed the impact of proration criteria on total product line forecast accuracy. In judgmental time series forecasting, O'Conner and Lawrence [22] examined the properties of time series and their influence on the widths of judgmental confidence intervals. Danaker and Brodie [11] also assessed both forecast horizon and the length of the time series as indicators of forecast accuracy.

The need to incorporate time series characteristics directly into the forecast model selection has recently been addressed by Collopy and Armstrong. As an initial stage for identifying key features for use in selecting extrapolation methods, they $[8]$ report the results of a survey that asked forecasting experts to identify criteria they would use to select forecasting models. The results of this initial survey were combined with information on model selection from five forecasting experts, and the results provided the basis for the development of a rule-based forecasting procedure $[9]$ .

Neural networks technology has been applied successfully for a number of forecasting problem domains, such as bankruptcy prediction $[14]$ , thrift failure prediction $[24]$ , bond rating prediction $[12,27]$ , and risk assessment $[21]$ . A number of researchers have also focused on the use of neural networks as an alternative methodology for time series forecasting $[5–7,16,17,19,26,28]$ . Such a review suggests that a study of Neural Network use as a forecasting model selection tool has not been attempted.

This paper relies on the results of research on forecast model selection criteria to test the utility of neural network methodology in the model selection process. To accomplish this, a reasonable set of time series characteristics, representing the domain knowledge is established. It is not suggested that the time series characteristics and associated metrics are exhaustive.

## 2. Time series characteristics

The criteria for selecting data characteristics require that any input be measurable and repeatable. The feature should also be available from the normal collection of data. In addition, the forecasting literature guides the development of the criteria. Lastly, the set of time series characteristics should be manageable in size. Based on the above criteria, a set of six distinguishing features was used.

Length of the time series: measured by the number of observations used to estimate the parameters of the model. This does not include the ex-ante sample size that is used for assessing forecast accuracy.

Time period between observations: one of three time periods: monthly, quarterly, or yearly.

Type of time series data: the source of the data and its level of aggregation, represented by one of four categories (micro level, macro level, industry specific, and demographic data).

Basic trend: measured by the slope of the time series regression model.

Recent trend: the trend of the time series for the latest observations, indicated by the slope of the time series regression model fitted to the last one third of the data series.

Variability of the series: the stability of the series, measured by the value of R-squared from the fitted regression model.

Each of the data series is identified by these seven distinguishing features, available and calculated directly from the historical data series.

## 2.1. Measure of forecast accuracy

Several ways of assessing forecast accuracy are discussed extensively in the literature $[1,13]$ . The focus of the research is to utilize one measure of forecast accuracy on the basis of consistency and to eliminate inconsistent results that are inherent when several measures are employed. Specifically, one measure of forecast accuracy is used for each of the forecasting models acting on the time series. That method resulting in the minimum error is considered the appropriate model; this model becomes one of the output neurons. Another criteria is ease of implementation and intuitive appeal to the practitioner. Additional criteria included measures that are unaffected by outliers, independent of scale, and widely used. Therefore, the Mean Absolute Percentage Error (MAPE) is used to determine forecast accuracy.

## 3. Neural networks

A number of applications involving pattern recognition are amenable to a neural network approach. Common applications include character recognition, forecasting, signal processing, robot control, and process monitoring. Bailey and Thompson [2,3] have identified a number of criteria for selecting this application:

1. conventional computer technology is not adequate,

2. problem requires qualitative or complex quantitative reasoning,

3. solution is derived from highly-interdependent parameters with no precise quantification,

4. data is readily available but multivariate and noisy or error-prone, and

5. project development time is short; though, sufficient “training time” is needed.

Although there are a number of learning algorithms to train a neural network, the back propagation (back-prop) paradigm has become the most popular for prediction and classification problems. A three-layer back-prop neural network is shown in Fig. 1. When the relationship between the input and output variables is nonlinear, a hidden layer helps in extracting higher level features and facilitates generalization of outputs. Connections between neurons have numerical weights; these are adjusted in the training process.

![](/api/attachments/JNCHHPQX/fulltext/images/f239b924ac4521b05546c01e51582a4f9e2870a8dd921cd97d5f5ebf3707a714.jpg)  
Fig. 1. A three-layer back propagation network

Each neuron has an activation level, specified by continuous or discrete values. The value for a neuron in the hidden or output layers is typically the sum of each incoming activation level times its respective connection weight. For the neurons in the input layer, the activation levels are determined in response to the input signals received from the environment. The internal activation is then modified by a transfer function and becomes an output, which in turn may become an input to one or more neurons. For classification problems, a sigmoid transfer function is typically used to transform the input signals into output signals. It is represented by

$$
F (I) = 1 / \left(1 + e ^ {- I}\right),
$$

where / represents the internal activation.

In the back-prop network paradigm, all the connection weights are assumed to be responsible for an output error, defined as the difference between a network's estimated output or predicted value and the corresponding observed output value. The error values are calculated at the output layer, propagated to previous layers, and used for adjusting the connection weights. The training process consists of repeatedly feeding input and output data from empirical observations, propagating the error values, and adjusting the connection weights until the error values fall below a user-specified tolerance level.

The following equations describe how the error values are computed and the connection weights are updated: $^{1}$

Net input to a hidden neuron, $j = I_{j} = \sum_{i}w_{ji}O_{i}$

Output of a hidden neuron, $j = O_{j} = \frac{1}{(1 + e^{-I_j})}$

Net input to an output neuron, $l = I_{i} = \sum_{j}w_{lj}O_{j}$

Output of an output neuron, $l = O_{1} = \frac{1}{(1 + e^{-I_{i}})}$

The equation for updating the connection weights between the hidden and output layers is:

$$
w _ {l j} (\text { new }) = w _ {l j} (\text { old }) + \alpha \delta_ {l} O _ {j} + \beta [ \Delta w _ {l j} (\text { old }) ],
$$

where $\delta_{1}$ is called the error signal and computed as $\delta_{l}=F^{\prime}(I_{l})(A_{l}-O_{l})$ ; and $F^{\prime}(I_{l})=O_{l}(1-O_{l})$ for Sigmoid transfer function. $A_{1}$ and $O_{1}$ represent actual and estimated output signals. The term $\alpha$ represents the learning rate and $\beta$ represents the momentum.

The equation for updating the connection weights between the input and hidden layers is:

$$
w _ {j i} (\text { new }) = w _ {j i} (\text { old }) + \alpha \delta_ {j} O _ {i} + \beta [ \Delta w _ {j i} (\text { old }) ],
$$

where $\delta_{j}$ is defined as

$$
O _ {j} \left(1 - O _ {j}\right) \sum_ {l} w _ {j i} \delta_ {l}.
$$

## 4. A neural network for forecasting model selection

In our research, a back propagation neural network was constructed with eleven input nodes and three output nodes. A back propagation learning design was used.

The input nodes representing the six distinguishing features of time series data were:

1. Length of the time series

2. Time between observations

3. Type of data

4. Basic trend

5. Recent trend

6. Variability

The length, basic trend, recent trend, and variability are numeric values and have one input neuron each. The time between observations has three nodes (for monthly, quarterly, or yearly values). The type of data has four neurons (for micro level, macro level, industry specific, or demographic data).

The output layer has three neurons representing the three categories of time series forecasting methods. They were chosen because they were well established and extensively studied, readily available and commonly used, require little user intervention in parameter selection and estimation, and represent a robust cross section of forecasting procedures. Nine forecasting methods were selected, and they were grouped into three categories.

## 4.1. Category I

This has relatively simple models that are used in practice but are not necessarily best for business and economic data.

Naive 1. The forecast at time period $t + 1$ is equal to the actual value at time period t.

Simple moving average. The forecast is the average of the last N values of the time series, where N is chosen to minimize the sum of the squared error (error = actual-forecast).

Single exponential smoothing. One parameter simple exponential smoothing.

## 4.2. Category II

These are responsive to linear trends.

Brown's one parameter linear exponential smoothing. Double exponential smoothing with one smoothing parameter.

Linear regression trend fitting. Time series regression with t as the independent variable.

Adaptive response rate exponential smoothing. The same as single exponential smoothing, except that the smoothing constant is allowed to vary over time.

## 4.3. Category III

These are flexible models that are adaptive to a variety of trends.

Holt's two parameter linear exponential smoothing. Holt's linear model with the value of the two smoothing parameters chosen so as to minimize the mean square error.

Brown's one parameter quadratic exponential smoothing. Triple exponential smoothing with one smoothing parameter.

Winter's three parameter exponential smoothing. Winter's linear model with the three parameters chosen so as to minimize the mean square error.

The selection of the number of nodes in the hidden layer is often heuristic. Examples include: $(2n+1)$ , where n represents the number of input nodes, $0.5*(sum\ of\ input\ and\ output\ neurons)$ , square root of the sum of input and out neurons, 0.1N, where N represents the number of training inputs, etc. After experimenting with a number of heuristics, a 23-neuron hidden layer was found to give good results.

## 4.4. The data set, training, and testing

The M-competition data was used to train and test the neural network. A subset of the 1001 series, consisting of 180, was obtained by a stratified random sample to assure an adequate cross-section and was used to train the neural net. The time series characteristics were calculated using SAS and thus form the input vectors. The measure of forecast accuracy (MAPE) was determined for each of the sub-series using the same forecast horizons used in the M-competition (6,8 and 18 periods for yearly, quarterly and monthly time series, respectively). The accuracy measure was calculated for each of the nine forecast methods available for all 180 series. The forecasting method resulting in the minimum MAPE (for the thirteen methods) was identified for and labelled as one of the three categories for each of the sub-series and it represents the output vector for the training set. The results are shown in Table 1.

The trained neural network was then tested with two sets of time series data, each containing 86 series. The test sets were chosen randomly from the original 1001 series but excluding the 180 series used in the training session. The test results are shown in Table 2.

<table><tr><td colspan="2">Table 1Training statistics</td></tr><tr><td>Number of data sets:</td><td>180</td></tr><tr><td>Training tolerance:</td><td>0.5</td></tr><tr><td>Number of good * classification achieved:</td><td>153</td></tr><tr><td>Percentage of good classification achieved:</td><td>85%</td></tr><tr><td>Total number of iterations:</td><td>3,215,200</td></tr><tr><td>Learning rate used:</td><td>0.9 (starting), 0.02 (ending)</td></tr><tr><td>Number of hidden neurons:</td><td>23</td></tr></table>

A classification is considered good if the output neuron representing the correct category has a value $> = 0.5$ and the other output neurons have values $< 0.5$ .

Table 2
Testing results

<table><tr><td></td><td>Testing Set 1</td><td>Testing Set 2</td></tr><tr><td>Size of data set</td><td>86</td><td>86</td></tr><tr><td>Number of good classifications</td><td>59</td><td>62</td></tr><tr><td>Percentage of good classifications achieved</td><td>68.6%</td><td>72.1%</td></tr><tr><td>Testing tolerance</td><td>0.5</td><td>0.5</td></tr></table>

The network is implemented using the software package BrainMaker [4] running on a microcomputer.

## 5. Conclusions

The primary focus of the work reported here was to explore the utility of neural network methodology in the selection of forecasting models. The result has been positive and encouraging. While a number of studies in the past have explored the use of neural network methodology as an alternative to traditional forecasting methods, this research focuses on the selection of an appropriate forecasting method for a given data series using neural networks. A neural network was trained using a set of 180 time series. Even with a relatively small training size, we achieved a reasonable level of accuracy (about seventy percent with two sets of test data).

## 6. For further reading

[23]

## Acknowledgements

The authors would like to thank Steve Ruta for his assistance in the data collection phase of this research. This research was partially supported by a grant from the Whittemore School of Business and Economics at the University of New Hampshire.

## References

[1] Armstrong, J.S. and F. Collopy, 1992, “Error Measures for Generalizing about Forecasting Methods: Empirical Comparisons,” International Journal of Forecasting, Vol. 8, No. 1, pp. 69–80.

[2] Bailey, D. and D. Thompson, 1990a, “How to Develop Neural Network Applications,” AI Expert, June 1990, pp. 38–47.

[3] Bailey, D. and D. Thompson, 1990b, “Developing Neural Network Applications,” AI Expert, September 1990, pp. 34–41.

[4] California Scientific Software, 1993, “BrainMaker: User’s Guide and Reference Manual,” Nevada City, California.

[5] Caporaletti, L.E., E.L. Gillenwater and J.D. Johnson, 1991, "Feedforward Neural Networks as Linear and Nonlinear Weighted Average Time-Series Forecasting Techniques," in: Proceedings of Decision Sciences Institute, Miami Beach, FL, pp. 494–496.

[6] Chakraborty, K., K. Mehrotra and C.K. Mohan, 1992, "Forecasting the Behavior of Multivariate Time Series using Neural Networks," Neural Networks, Vol. 5, November/December 1992, pp. 961–970.

[7] Chang, I., S. Rapiraju, M. Whiteside and G. Hwang, 1991, "A Neural Network to Time Series Forecasting," in: Proceedings of Decision Sciences Institute, Miami Beach, FL, pp. 1716–1718.

[8] Collopy, F. and J.S. Armstrong, 1992a, “Expert Opinions about Extrapolation and the Mystery of the Overlooked Discontinuities,” International Journal of Forecasting, Vol. 8, No. 4, pp. 575–582.

[9] Collopy, F. and J.S. Armstrong, 1992b, “Rule-Based Forecasting; Development and Validation of an Expert System Approach to Combining Time Series Extrapolations,” Management Science, Vol. 38, No. 10, pp. 1394–1414.

[10] Dalrymple, D.J., 1987, “Sales Forecasting Practices,” International Journal of Forecasting, Vol. 3, pp. 379–391.

[11] Danaker, P.J. and R.J. Brodie, 1992, “Predictive Accuracy of Simple Versus Complex Econometric Market Share Models. Theoretical and Empirical Results,” International Journal of Forecasting, Vol. 8, No. 4, pp. 613–626.

[12] Dutta, S. and S. Hekhar, 1988, “Bond-Rating: A Non-Conservative Application of Neural Networks,” in: Proceedings of the IEEE International Conference on Neural Networks, Vol. II, San Diego, CA, pp. 443–450.

[13] Fildes, R., 1992, “The Evaluation of Extrapolative Forecasting Methods,” International Journal of Forecasting, Vol. 8, No. 1, pp. 81–98.

[14] Fletcher, D. and E. Goss, 1993, “Forecasting with Neural

Networks – An Application Using Bankruptcy Data," Information & Management, Vol. 24, No. 3, pp. 159–167.

[15] Fliedner, E. and V. Mabert, 1992, “Constrained Forecasting: Some Implementation Guidelines,” Decision Sciences, Vol. 23, No. 5, 1143–1161.

[16] Foster, W.R., F. Collopy, and L.H. Ungar, 1992, “Neural Network Forecasting of Short, Noisy Time Series,” Computers & Chemical Engineering, Vol. 16, April 1992, pp. 293–297.

[17] Gent, C.R. and C.P. Sheppard, 1992, “Predicting Time Series by a Fully Connected Neural Network Trained by Back Propagation,” Computing & Control Engineering Journal, Vol. 3, No. 3, May, pp. 109–112.

[18] Gross, C. and J. Sohl, 1990, “Disaggregation Methods to Expedite Product Line Forecasting,” Journal of Forecasting, Vol. 9, No. 3, pp. 233–254.

[19] Kohers, G., 1992, “The Use of Modular Neural Networks in Time Series Forecasting,” in: Proceedings of Decision Sciences Institute, San Francisco, CA, pp. 759–761.

[20] Makridakis, S., A. Andersen, R. Carbone, R. Fildes, M. Hibon, R. Lewandowski, J. Newton, E. Parzen and R. Winkler, 1982, “The Accuracy of Extrapolation (Time Series) Methods: Results of a Forecasting Competition,” Journal of Forecasting, Vol. 1, pp. 111–153.

[21] Marose, R., 1990, “A Financial Neural-Network Application,” AI Expert, May (1990), pp. 50–53.

[22] O'Conner, M. and M. Lawrence, 1992, "Time Series Characteristics and the Widths of Judgmental Confidence Intervals," International Journal of Forecasting, Vol. 7, No. 4, pp. 413–420.

[23] Rumelhart, D.E., G.E. Hinton, and R.J. Williams, 1986, "Learning Internal Representations by Error Propagation," in: Parallel Distributed Processing: Explorations in the Microstructures of Cognition (Vol. 1), D.E. Rumelhart and J.L. McClelland (Eds.), Cambridge, MA: MIT Press.

[24] Salchenberger, L.M., E.M. Cinar and N.A. Lash, 1992, "Neural Networks: A New Tool for Predicting Thrift Failures," Decision Sciences, Vol. 23, No. 4, July/August, pp. 899–916.

[25] Schnaars, S.P., 1984, “Situational Factors Affecting Forecast Accuracy,” Journal of Marketing Research, Vol. 21, pp. 290–297.

[26] Tang, Z., C. Almeida, and P.A. Fishwick, 1991, “Time Series Forecasting Using Neural Networks vs Box-Jenkins Methodology,” Simulation, Vol. 57, November 1991, pp. 303–310.

[27] Utans, J. and J. Moody, 1991, “Selecting Neural Network Architectures via the Prediction Risk: Application to Corporate Bond Rating Prediction,” in: Proceedings: First International Conference on Artificial Intelligence Applications on Wall Street, IEEE Computer Society Press, Los Alamitos, CA.

[28] Weigend, A.S. and N.A. Gershenfeld, 1993, “Results of the Time Series Prediction Competition at the Santa Fe Institute,” in: Proceedings of the 1993 International Conference on Neural Networks, San Francisco, CA, pp. 1786–1793.

![](/api/attachments/JNCHHPQX/fulltext/images/ad9d0c80995efaebf400856a1d7001508988e432e6b0900c8ab68be78164c7c4.jpg)

Jeffrey E. Sohl is an Associate Professor of Management Science in the Department of Decision Sciences and Director of the Center for Venture Research at the Whittemore School of Business and Economics at the University of New Hampshire. He received his MBA and Ph.D. from the University of Maryland. His current research has focused on equity financing for technology based entrepreneurial ventures and forecasting model selection. He has pre-

sented his research at both national and international forums. He has written several articles which have been published in academic and business journals, including the Social Science Journal, the Journal of Business Forecasting, Frontiers of Entrepreneurship Research, the Journal of Forecasting, and the Journal of Business Venturing.

![](/api/attachments/JNCHHPQX/fulltext/images/113a76bf8b9580278976c77ead3ac5925fc0200fccf94601b9a0de600de034c4.jpg)

A.R. “Venky” Venkatachalam obtained a Ph.D. in Management Science from The University of Alabama and is currently Assistant Professor of Information Systems in the Whittemore School of Business and Economics at the University of New Hampshire. His research interests include cross-cultural studies in information systems management, global information systems, knowledge-based systems, and neural networks. He has published in Simula-

tion, Industrial Management, Journal of Intelligent Manufacturing, Computers and Operations Research, Information & Management, Journal of Global Information Management, and Expert Systems with Applications. Dr. Venkatachalam is a member of the Decision Sciences Institute and Information Resources Management Association.
