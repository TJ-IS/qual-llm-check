---
otero_id: 6038
otero_key: "A2CRCR8Y"
title: "Modeling daily patient arrivals at Emergency Department and quantifying the relative importance of contributing variables using artificial neural network"
authors: "M. Xu; T.C. Wong; K.S. Chin"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.12.019"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Modeling daily patient arrivals at Emergency Department and quantifying the relative importance of contributing variables using arti<sup>fi</sup>cial neural network

M. Xu <sup>1</sup>, T.C. Wong ⁎, K.S. Chin <sup>2</sup>

Dept. of Systems Engineering and Engineering Management, City University of Hong Kong, 83 Tat Chee Avenue, Kowloon Tong, Hong Kong

## a r t i c l e i n f o

Article history: Received 26 April 2012 Received in revised form 8 October 2012 Accepted 23 December 2012 Available online 29 December 2012

Keywords: Patient arrival Emergency Department Relative importance Arti<sup>fi</sup>cial neural network Multiple linear regression

## a b s t r a c t

Emergency Department (ED) plays a critical role in healthcare systems by providing emergency care to patients in need. The quality of ED services, measured by waiting time and length of stay, is signi<sup>fi</sup>cantly affected by patient arrivals. Increased patient arrivals could undermine service timeliness, thus putting patients in severe conditions at risk. These factors lead to the following research questions that have rarely been studied before: What are the variables directly associated with patient arrivals in the ED? What is the nature of association between these variables and patient arrivals? Which variable is the most in<sup>fl</sup>uential and why? To address the above questions, we proposed a three-stage method in this paper. First, a data-driven method is used to identify contributing variables directly correlated with the daily arrivals of Categories 3 and 4 patients (i.e., non-critica patients). Second, the association between contributing variables and daily patient arrival is modeled by using arti<sup>fi</sup>cial neural network (ANN), and the modeling ability is compared with that of nonlinear least square regression (NLLSR) and multiple linear regression (MLR) in terms of mean average percentage error (MAPE). Third, four types of relative importance (RI) of input variables based on ANN are compared, and their statistical reliability is tested by the MLR-based RI. We applied this three-stage method to one year of data of patient arrivals at a local ED. The contribution of this paper is twofold. Theoretically, this paper emphasizes the importance of using data-driven selection of variables for complex system modeling, and then provides a comprehensive comparison of RI using different computational methods. Practically, this work is a novel attempt of applying ANN to model patient arrivals, and the result can be used to aid in strategic decision-making on ED resource planning in response to predictable arrival variations.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

The Emergency Department (ED) is the busiest department in a hospital and its primary purpose is to provide timely emergency care to patients in need. Amid scarce resources and rising public scrutiny, the quality of ED services is strictly measured and monitored. Recently, performance indicators, such as maximum waiting time of patients (hereafter denoted as waiting time), are used increasingly to measure the ED service quality [28]. Prolonged waiting time is attributed to a variety of variables and has long been a major cause of ED crowding, which is a key symptom of supply–demand mismatch. A conceptual model depicting ED crowding illustrates that patient arrivals directly affect throughput measures of ED, such as waiting time [4]. According to the Hong Kong Hospital Authority, waiting time is one of the key performance indicators (KPIs) for assessing EDs. The target service level is different for patients of different categories (Appendix A). Staff members in local EDs tend to express the dif<sup>fi</sup>culty in meeting the service target of Categories 3 and 4 patients, that is, 90% of the Category 3 patients are seen by a doctor within 30 min, and 75% of the Category 4 patients are seen within 120 min. Violations of the service target are frequently observed when the patient volume shows a surge. This <sup>fi</sup>nding can be clearly illustrated from the sensitive change in waiting time against arrival variations of Categories 3 and 4 patients in two random days during the study period (Fig. 1). Thus, a better match between supply (ED resource) and demand (patient arrivals) can enhance ED service quality, which in turn, will improve the patient experiences and staff morale [51]. A reliable arrival prediction model needs to be developed to achieve the foregoing; such a model should take a number of contributing variables into account. Empirical knowledge indicates that the potential variables of arrival <sup>fl</sup>uctuation could be temporal (weekdays, weekends, holidays, and others), climatic (temperature, rain, and others), or dictated by in<sup>fl</sup>uenza outbreaks [7,30,50]. With the developed arrival model, ED decision-makers can predict patient arrivals on a future day by keying in all contributing variables to the model. The predicted result will provide managerial insights on staf<sup>fi</sup>ng and operational practices so that the ED can be better prepared for the coming arrival variations.

![](/api/attachments/A2CRCR8Y/fulltext/images/bcaccde6cfad5ab94411cd731dfa7ae01c1e29ab0a2012842694184a85e2bdce.jpg)

![](/api/attachments/A2CRCR8Y/fulltext/images/e150ef2cb6600aaa32303b18d6d22846fceaac7d4774ac4131583588f9cfdf78.jpg)

![](/api/attachments/A2CRCR8Y/fulltext/images/5fdf36f44e044f5d324c664d836159d57c10f7a71da58d0b169c87e06339f890.jpg)

![](/api/attachments/A2CRCR8Y/fulltext/images/85292bd513e04881dca6ea593fd473d5c923d4c6b693544665c893cc5b3cd61d.jpg)  
Fig. 1. The vertical green lines in (a) and (b) represent waiting time of individual patients. The red line (a) and blue line (b) represent hourly arrivals of Categories 3 and 4 patients, respectively. The black bars in (a) and (b) indicate the waiting time limit of Categories 3 and 4 patients, respectively.

From a theoretical standpoint, promoting a new understanding of a modeling technique itself would be another research topic. In the present study, this new understanding can be achieved by looking into the different computation methods for the relative importance (RI) of contributing variables. Although many nonlinear models, such as ANN, are labeled as “black box”, useful yet hidden information can be extracted from these models to provide explanatory insight on the RI of contributing variables toward the subject of interest or model output, that is, patient arrival. The reliability of ANN-based RI is not proven because ANN itself lacks statistical soundness [11]. Previous studies argued that the ANN-based RI is not arithmetically comparable within variables, and hence, decision-makers cannot extract any statistical insights from RI [37]. Wong et al. [56] developed an ANN model to identify determinants of organizational innovation and veri<sup>fi</sup>ed the RI by consulting human experts. However, the subjective opinion of human experts cannot statistically validate the ANN-based RI without a comparison with its counterpart computed from a pure statistical model, such as MLR.

The organization of this paper is as follows. Section 2 reviews various modeling techniques on arrival and customer demand problems, as well as several ANN-based methods of computing the RI of contributing variables. Section 3 presents the details of the proposed three-stage method and its application to the modeling of daily patient arrival at a local ED. Section 4 presents the analysis results and Section 5 discusses the <sup>fi</sup>ndings. The conclusion, limitations, and the direction of our future work are given in Section 6.

## 2. Literature review

## 2.1. Customer demands

A more comprehensive understanding of the patient arrival problem can be achieved by relating it to the larger topic of customer demand forecast. Generally, the forecasting and modeling techniques can be classi<sup>fi</sup>ed into two main streams, namely, linear and nonlinear. Linear methods are less demanding, technically, and include time series decomposition, Holt–Winters exponential smoothing, MLR, and average autoregressive integrated moving average (ARIMA). Nonlinear methods are more capable of modeling the input–output relationship in any complex and dynamic system [11]. The most common nonlinear forecasting methods include ANN, support vector regression (SVR), and fuzzy time series. The sophisticated nature of these methods allows researchers to handle more complex input–output relations. The superiority of nonlinear over linear methods has been demonstrated through real applications. Table 1 summarizes previous work in four typical areas of service industry where a variety of forecasting techniques were applied.

Table 1  
Summary of forecasting models applied in areas of service industry.

<table><tr><td>Applications</td><td>References</td><td>Methods</td></tr><tr><td rowspan="4">Call center</td><td>[3,24,45,52]</td><td>Inhomogeneous Poisson process</td></tr><tr><td>[44]</td><td>ANN</td></tr><tr><td>[10,13,50,57]</td><td>ARIMA</td></tr><tr><td>[13,47]</td><td>Averaging and harmonic regression, ARIMA</td></tr><tr><td rowspan="3">Tourism</td><td>[15]</td><td>Exponential smoothing, ARIMA, SVR, ANN</td></tr><tr><td>[16]</td><td>Adaptive network-based fuzzy inference system (ANFIS), fuzzy time series, grey forecasting, Markov residual modified model</td></tr><tr><td>[32]</td><td>Grey forecasting, Fourier series, Markov chain</td></tr><tr><td rowspan="5">Sales, retail, trade</td><td>[6]</td><td>Evolutionary neuron network, ARIMA</td></tr><tr><td>[18]</td><td>ANN, ARIMA</td></tr><tr><td>[19]</td><td>ANN, exponential smoothing, ARIMA</td></tr><tr><td>[34]</td><td>SVR</td></tr><tr><td>[36]</td><td>Autoregressive techniques and decision tree algorithm</td></tr><tr><td rowspan="3">Energy</td><td>[1]</td><td>ANN, naive forecast, multiple abductive modeling, MLR, ARIMA</td></tr><tr><td>[23]</td><td>ANN</td></tr><tr><td>[48]</td><td>ANN, exponential smoothing, ARIMA</td></tr></table>

## 2.2. Patient arrivals

Most studies on patient arrivals found below were published in medical journals. Overall, linear methods are overwhelmingly adopted. Linear methods can be generally classi<sup>fi</sup>ed into multivariate and univariate models. A typical example of the former is MLR, which associates patient arrivals with temporal variables (hour, weekday, and month) [5,7,30,51], holidays [30,51], weather variables, and the effects of their interaction [30]. By contrast, the latter depends solely on the lagged value of real arrivals, such as ARIMA. Nearly all the studies included here indicated that temporal variables are more in<sup>fl</sup>uential to patient arrival than the effect of holiday and weather. Many of them also showed that although advanced univariate models [5,12,20,31,43] such as ARIMA can produce more accurate results compared with MLR models, using such models entails dif<sup>fi</sup>culty in identifying and interpreting the model structure.

## 2.3. ANN and computation of RI of input variables

ANN enables modeling complex nonlinear relations and providing decision support. ANN is inspired by the structure of biological neural networks, and it starts by assigning random weights to included variables and then adjusting these weights in a feed-forward, backpropagation style to minimize the difference between the actual and predicted outputs. The neurons in the hidden layer transfer the weighted input data to the output using nonlinear transfer function [11]. Fig. 2 illustrates the structure of a typical three-layer ANN.

![](/api/attachments/A2CRCR8Y/fulltext/images/9839b8dc3466dce536e6d4db7e9e9ecd0bbffecc057fde63049d5c0c4fcfe831.jpg)  
Fig. 2. A three-layer ANN with N input neurons, P hidden neurons, and M output neurons.

From the <sup>fi</sup>gure, the lines connecting two neurons assign weights to the incoming data before transferring them to the next neuron. The weight values re<sup>fl</sup>ect the strength of that connection. Regardless of the risk of over-<sup>fi</sup>t and long training time, ANN is capable of approximating output arbitrarily well given suf<sup>fi</sup>cient neurons in the hidden layers. By comparison, linear methods such as MLR cannot capture the complex nonlinear input–output relations in real systems. The negative side of ANN is that it is considered a “black box” system, and several statisticians have pointed out the absence of widely accepted procedures to determine ANN architecture. Thus, the structure of ANN is problem-speci<sup>fi</sup>c. Thus far, ANN has appeared in many healthcare studies, such as diagnosing speci<sup>fi</sup>c diseases by taking clinically relevant variables into account [8,9,26,27].

The “black box” characteristic of ANN gives rise to dif<sup>fi</sup>culty in quantifying the RI of input variables into output variables. The possible solutions can be divided into two groups. The <sup>fi</sup>rst is the explicit computation of the connection weights between neurons (e.g., Garson [21], Yoon et al. [59], and Tsaur et al. [49]). Howes and Crook [29] criticized Garson's method by pointing out that it does not include the bias effect. Yoon's method could cause weight cancellation and thus lead to a zero denominator. However, these methods are nevertheless reliable in real applications. In a recent study, Wong et al. [54] compared the above three methods in calculating the importance of determinants to the performance of supply chain operation. He found that Tsaur's method produces different factor rankings as compared with Garson's and Yoon's methods. The second method features by a before-and-after comparison of the output variations after the deletion or adjustment of the value of input variables. The change of mean square error (COE) method [46] and sensitivity analysis are the two most popular methods in the second group [37,39]. The COE method measures the change of MSE after deleting the input variable of interest from the original ANN. This technique is analogous to the stepwise method of identifying independent variables in MLR. COE has been applied to the analysis of different industrial engineering problems [46,54–56] with promising results. Alternatively, sensitivity analysis works by varying each input variable over either the entire or a partial range of possible values while holding all other input variables constant at a speci<sup>fi</sup>ed percentile, so that the RI of variables of interest can be assessed by the induced variation of output variables. Sung [46] compared COE and sensitivity analysis in a real engineering problem, and found that both methods generated comparable results. Thus far, consensus has not been reached on which group of methods outperforms the other [22,38].

## 2.4. Research gaps

We have observed several potential research gaps that this paper can bridge. First, previous medical papers that studied patient arrivals contained debatable issues that may undermine the analysis results. For example, most of them focused on total patient arrivals only, without revealing if patients in different severity levels could be modeled by the same set of predictors. For example, Category 3 patients are less likely to be deterred from visiting the ED by bad weather, but Category 4 patients may consider not visiting the ED as most of them are not in critical condition. Second, the contributing variables are often selected by human judgment or experience. However, we believe that reliance on empirical knowledge may cause biased results because some seemingly important variables may not statistically correlate with the patient arrivals. Third, although nonlinear methods have shown better performance than linear methods in the service industry, few applications are found in patient arrival problems where linear methods, such as MLR, continue to prevail. This paper can also offer theoretical contributions toward the lack of comprehensive comparison among different types of ANN-based RI, the statistical reliability of which is rarely investigated.

## 3. Proposed methodology

A three-stage method is proposed to bridge the research gap. A quick overview of the method is as follows. First, key contributing variables to patient arrivals are addressed. The process of variable screening is completely data-driven and not guided by any empirical knowledge such that subjective judgment is omitted. Second, ANN models are constructed to depict the association between key variables identi<sup>fi</sup>ed in the <sup>fi</sup>rst stage and patient arrivals. The ANN-based models are then trained and validated before being compared with the two benchmarking methods. Third, with respect to the trained ANN models, the RI of the contributing variables is calculated by four different methods. The RI's statistical reliability is checked with its counterpart calculated by an MLR-based method. The details of each stage can be found in the following subsections.

## 3.1. Output measures: daily patient arrival

This paper focuses on the daily arrivals of Categories 3 and 4 patients only because they account for over 90% of the total daily visits to the ED. The patients making up each of the <sup>fi</sup>ve triage categories are introduced in Appendix A. As patient arrivals are count numbers, the daily arrival distribution of Categories 3 and 4 patients are rightward skewed. A common solution to this problem is log-transferring the arrival data [41]. However, the raw arrival data are kept as output variables after con<sup>fi</sup>rming normality using the Chi-squared test (pb0.05).

## 3.2. Stage one: identification of key contributing variables

In selecting the contributing variables, three aspects are considered: previous research on patient arrivals, data availability, and interviews with ED staff. Literature in Subsection 2.2 points out that the common variables associated with daily patient arrivals are temporal, holidays, weather variables and their interaction effects [5,7,30,31,35,51]. Regarding data availability, only temporal data can be retrieved from the ED information system, and the weather data need to be collected from the Hong Kong Observatory. The ED staff suggested another important variable, namely, in<sup>fl</sup>uenza, by referring to the sharp increase of arrivals during the outbreak of human swine <sup>fl</sup>u in Hong Kong. The <sup>fi</sup>nal candidate variables are weekday, holiday, weather (rainfall, wind speed, temperature, humidity), and in<sup>fl</sup>uenza (human swine <sup>fl</sup>u) outbreak level. In treating these contributing variables as inputs and the daily arrivals of Categories 3 and 4 patients as outputs, correlation analysis is conducted to examine the association among all the variables. Because linearity among variables is unknown, Spearman's rank correlation coef<sup>fi</sup>cients are calculated. In brief, the Spearman's coef<sup>fi</sup>cient is another version of the Pearson's correlation coef<sup>fi</sup>cient for ranked variables. The coef<sup>fi</sup>cient is denoted by $\rho ,$ and for a sample of size n, the value of coef<sup>fi</sup>cient is as follows:

$$
\rho = \frac {\sum_ {i = 1} ^ {n} (x _ {i} - \overline {{x}}) (y _ {i} - \overline {{y}})}{\sqrt {\sum_ {i = 1} ^ {n} (x _ {i} - \overline {{x}}) ^ {2} \sum_ {i = 1} ^ {n} (y _ {i} - \overline {{y}}) ^ {2}}}\tag{1}
$$

where $x _ { i }$ and $y _ { i }$ are ranks converted from the raw value of $X _ { i }$ and $Y _ { i \cdot }$ The range of Spearman's coef<sup>fi</sup>cient falls into [−1, 1], and a correlation of $+ 1 \ 0 \Gamma - 1$ occurs when each of the variables is a perfect monotone function of the other. Based on the Spearman's coef<sup>fi</sup>cients, two relation diagrams are constructed to denote the association between contributing variables and the daily arrivals of Categories 3 and 4 patients, respectively. In this research, our aim is to identify all the direct associations between contributing variables and daily arrivals; connections that are indirect to the daily arrivals are ignored. Next, partial correlation analysis is performed to re-examine the direct connections between each of the contributing variables and daily arrivals. Partial correlation coef<sup>fi</sup>cients are used to measure the degree of association between two random variables while controlling a third one. First-order partial correlation refers to the degree of association by keeping a third variable constant. It is calculated by

$$
r _ {x y. z} \frac {r _ {x y} - r _ {x z} r _ {y z}}{\sqrt {\left(1 - r _ {x z} ^ {2}\right) \left(1 - r _ {y z} ^ {2}\right)}}\tag{2}
$$

where $r _ { x y } , r _ { x z } ,$ and $r _ { y z }$ are rank correlations. Partial correlation analysis is applied under the assumption that one variable is not signi<sup>fi</sup>cantly correlated to another variable unless through a third one. Thus, partial correlation coef<sup>fi</sup>cient is calculated for each of the connections. The connection is removed only if its partial coef<sup>fi</sup>cient is not signi<sup>fi</sup>- cant. This procedure is repeated for the rest of the connections, and the resultant relation diagram can be developed by incorporating all connections that are deemed as the most direct and signi<sup>fi</sup>cant. A key contributing variable must be the one with the most direct and signi<sup>fi</sup>cant connection to the daily arrival of Categories 3 and 4 patients.

## 3.3. Stage two: development of ANN

The key contributing variables identi<sup>fi</sup>ed in the <sup>fi</sup>rst stage are regarded as input to a feed-forward back-propagation neural network with three layers. The transfer functions in the hidden and output layer are logistic-sigmoid and purely linear respectively. Each of the two ANN models (one for Category 3 patients and another for Category 4 patients) is trained and evaluated via a tenfold cross validation process, whereby the data are split into 10 divisions such that, in each validation process, 90% of the data are used for training whereas the remaining 10% are for validation. In this study, the data comprise 365 days of patient arrival information. Hence, the size of training and validation set are 328 and $^ { 3 7 , }$ respectively. The modeling accuracy of the ANN model is measured by MAPE which is a scaleinvariant statistic that expresses forecast error as a percentage. For a series of forecast values $( { \hat { y } } _ { 1 } , { \hat { y } } _ { 2 } , \dots { \hat { y } } _ { n } )$ and the corresponding series of observed values $( y _ { 1 } , y _ { 2 } , \dots y _ { n } )$

$$
M A P E = \frac {1}{n} \sum_ {t = 1} ^ {n} \left| \left(y _ {t} - \hat {y} _ {t}\right) / y _ {t} \right|\tag{3}
$$

where n is the number of validation sets. The average, standard deviation, and the minimum and maximum values of MAPE are calculated across the tenfold cross the tenfold cross-validation process. The optimal number of hidden neurons in each ANN model is determined by trial-and-error until the minimum average and standard deviation of MAPE are obtained. In judging the performance of ANN-based models, two statistical models, MLR and NLLSR, are regarded as the benchmarks. In MLR, the input variables are assumed to be linearly related with output variable, and their strengths are measured by regression coef<sup>fi</sup>cient β. A disturbance term ε is added to the model to explain the noise of the linear relationship between input and output variables. The MLR model involves n input variables, and one output variable is given as

$$
\begin{array}{l} y = X \beta + \varepsilon \text {where} X = (x _ {1} x _ {2} x _ {3}... x _ {n}) ^ {T}, \\ \beta = (\beta_ {1} \beta_ {2} \beta_ {3}... \beta_ {n}) ^ {T}, \text {and} \varepsilon = (\varepsilon_ {1} \varepsilon_ {2} \varepsilon_ {3} \varepsilon_ {n}) ^ {T}. \end{array}\tag{4}
$$

NLLSR is used to <sup>fi</sup>t m observations with n unknown parameters in a nonlinear model (m>n) (Eq. (5)). The coef<sup>fi</sup>cients β are determined in such way that the sum of squares could be minimized (Eq. (6)). $r _ { i }$ is the residual between the ith output in the training set and the estimated output from $f ( x _ { 1 } , \beta )$ (Eq. (7)). Newton's and Gauss–Newton's method are two major algorithms for minimizing the sum of squares. The former possesses the advantage of quicker convergence, whereas the later is superior in the sense that calculating the second derivative of $r _ { i }$ is not necessary. In this study, the Gauss–Newton method is used. Tenfold cross-validation is also performed in the two statistical models, and the summary statistics of MAPE is compared with that of the ANN-based models.

Spearman's rank correlation coef<sup>fi</sup>cients between variables. The left side is the output– input coef<sup>fi</sup>cients while the right side is the input–input coef<sup>fi</sup>cients.

<table><tr><td rowspan="2"></td><td colspan="2">Outputs</td><td colspan="7">Inputs</td></tr><tr><td>C3</td><td>C4</td><td>WK</td><td>IF</td><td>HL</td><td>RF</td><td>TP</td><td>WD</td><td>HM</td></tr><tr><td>WK</td><td>-0.31**</td><td>-0.23**</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>IF</td><td>0.17**</td><td>0.48**</td><td>0.00</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>HL</td><td>0.03</td><td>0.01</td><td>-0.08</td><td>-0.01</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>RF</td><td>-0.12*</td><td>0.01</td><td>-0.08</td><td>0.08</td><td>-0.01</td><td>1</td><td></td><td></td><td></td></tr><tr><td>TP</td><td>0.02</td><td>0.40*</td><td>0.04</td><td>0.04</td><td>-0.03</td><td>0.11*</td><td>1</td><td></td><td></td></tr><tr><td>WD</td><td>-0.15**</td><td>-0.14**</td><td>-0.11</td><td>0.00</td><td>-0.03</td><td>0.16**</td><td>-0.16**</td><td>1</td><td></td></tr><tr><td>HM</td><td>-0.01</td><td>-0.15**</td><td>-0.03</td><td>-0.01</td><td>0.06</td><td>0.43**</td><td>-0.02</td><td>0.12*</td><td>1</td></tr></table>

C3 = Category 3; C4 = Category 4; WK = Weekday; IF = In<sup>fl</sup>uenza Level; HL = Holiday; RF = Rainfall; TP = Temperature; and WD = Wind Speed. Signi<sup>fi</sup>cance code: 0.01 ‘\*\*’and 0.05 ‘\*’.

$$
Y = f (X, \beta)\tag{5}
$$

$$
S = \sum_ {i = 1} ^ {m} r _ {i} ^ {2}\tag{6}
$$

$$
r _ {i} = y _ {i} - f (x _ {i}, \beta) \quad \forall i = 1, \dots , m.\tag{7}
$$

3.4. Stage three: computation of RI of contributing variables using ANN

Several methods of computing RI for contributing variables of ANN have been described in Subsection 2.3, and their pros and cons are discussed. In this study, Garson's method [21], Yoon's method [59], the COE method, and sensitivity analysis [46] are implemented to compute the RI of contributing variables. The RI by Garson's and Yoon's methods are obtained, as shown in Eqs. (8) and (9), respectively.

$$
\mathrm{RI} _ {i k} = \frac {\sum_ {j = 1} ^ {P} \frac {\left| W _ {i j} \right| \left| W _ {j k} \right|}{\sum_ {i = 1} ^ {N} \left| W _ {i j} \right|}}{\sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {P} \frac {\left| W _ {i j} \right| \left| W _ {j k} \right|}{\sum_ {i = 1} ^ {N} \left| W _ {i j} \right|}}\tag{8}
$$

$$
\mathrm{RI} _ {i k} = \frac {\sum_ {j = 1} ^ {P} W _ {i j} W _ {j k}}{\sum_ {i = 1} ^ {N} \left| \sum_ {j = 1} ^ {P} W _ {i j} W _ {j k} \right|}.\tag{9}
$$

$W _ { i j }$ denotes the connection weight between the ith input variable and the jth hidden neuron, and $W _ { j k }$ denotes the connection weight between the jth hidden neuron to the kth output variables. The value of RI falls into the [0, 1] interval. By contrast, the COE is a more statistically rooted approach that measures the increase of forecast MSE of ANN after an input variable has been deleted. The MSE of a single input variable is determined by Eq. (10).

$$
\mathrm{MSE} = \sum_ {d = 1} ^ {D} \frac {(A _ {d} - E _ {d}) ^ {2}}{D}\tag{10}
$$

where $A _ { d }$ and $E _ { d }$ are the dth actual value and the estimated value, respectively, and D is the size of the validation set. The change in MSE is computed after having one input variable deleted from the original ANN model. Obviously, the largest change in MSE would indicate that the deleted input variable is the most important one. In sensitivity analysis, each of the input variables is varied at 12 “scale” values that are evenly delimited over the entire range and other input variables are held constant at their minimum, 1st quartile, median, 3rd quartile, and maximum. For each input variable, <sup>fi</sup>ve output values on <sup>fi</sup>ve summary statistics are calculated and then reduced to a median value. Finally, 12 median output values for each input variable are obtained, and the RI of that input variable is computed by the max–min range (as detailed in [22]). All the RIs calculated by COE and sensitivity analy sis are also normalized to [0, 1].

## 3.5. Computation of RI of contributing variables using MLR

Given that ANN is not statistically rooted technique, four types of RI based on ANN need to be compared with that based on a pure statistical model to avoid undermining the reliability of the computed RI. In this study, we adopted the MLR-based method of computing the RI proposed by Lindeman et al., known as LMG [33]. An R package “relaimpo” was developed by Grömping [25] to address computational intensiveness. Similar to the previous practice, the RI of the contributing variables is normalized into [0, 1]. The details of this method can be found in Appendix B.

3.6. Comparison between ANN- and MLR-based RI of contributing variables

The average RI by Garson's, Yoon's, COE, and sensitivity analysis methods are compared with that obtained by the LMG method over a tenfold cross-validation process to validate the statistical reliability of the ANN-based RI. Moreover, Spearman's rank correlation coef<sup>fi</sup>- cients are calculated to measure the similarity of the ranking of contributing variables by four ANN-based methods and that by LMG method. All the analyses in this section are conducted in R, version 2.12.3 (available at http://www.r-project.org/) and MATLAB version 2008a (The MathWorks, Inc.)

![](/api/attachments/A2CRCR8Y/fulltext/images/d3f64dd4709baf145ccf555a5204098a3f008b8b3e66524e6fc894e98a35ef9c.jpg)  
Fig. 3. Relation diagram of input and output variables

Spearman's rank partial correlation coef<sup>fi</sup>cients between input and output variables

<table><tr><td>Output variable</td><td>Controlling variables</td><td colspan="5">Input variables</td></tr><tr><td rowspan="5">C3</td><td></td><td>WD</td><td>RF</td><td>IF</td><td>WK</td><td></td></tr><tr><td>WD</td><td>-</td><td> $-0.10^{*}$ </td><td> $0.17^{**}$ </td><td> $-0.33^{**}$ </td><td></td></tr><tr><td>RF</td><td> $-0.13^{*}$ </td><td>-</td><td> $0.18^{**}$ </td><td> $-0.32^{**}$ </td><td></td></tr><tr><td>IF</td><td> $-0.15^{**}$ </td><td> $-0.14^{**}$ </td><td>-</td><td> $-0.31^{**}$ </td><td></td></tr><tr><td>WK</td><td> $-0.19^{**}$ </td><td> $-0.15^{**}$ </td><td> $0.18^{**}$ </td><td>-</td><td></td></tr><tr><td rowspan="6">C4</td><td></td><td>WD</td><td>HM</td><td>TP</td><td>IF</td><td>WK</td></tr><tr><td>WD</td><td>-</td><td> $-0.14^{**}$ </td><td> $0.38^{**}$ </td><td> $0.49^{**}$ </td><td> $-0.25^{**}$ </td></tr><tr><td>HM</td><td> $-0.13^{*}$ </td><td>-</td><td> $0.40^{**}$ </td><td> $0.47^{**}$ </td><td> $-0.24^{**}$ </td></tr><tr><td>TP</td><td> $-0.09^{*}$ </td><td> $-0.16^{**}$ </td><td>-</td><td> $0.40^{**}$ </td><td> $-0.27^{**}$ </td></tr><tr><td>IF</td><td> $-0.16^{**}$ </td><td> $-0.09^{*}$ </td><td> $0.29^{**}$ </td><td>-</td><td> $-0.27^{**}$ </td></tr><tr><td>WK</td><td> $-0.18^{**}$ </td><td> $-0.16^{**}$ </td><td> $0.42^{**}$ </td><td> $0.50^{**}$ </td><td>-</td></tr></table>

Signi<sup>fi</sup>cance code: 0.01\*\*and 0.05 \*.

## 4. Results

## 4.1. Development of relation diagram

Table 2 shows the Spearman's rank correlation coef<sup>fi</sup>cients (r) between all variables. The left side shows the output–input coef<sup>fi</sup>cients whereas the right side presents the input–input coef<sup>fi</sup>cients. The abbreviations used in this table are C3 (daily arrival of Category 3 patients), C4 (daily arrival of Category 4 patients), WK (weekday), IF (in<sup>fl</sup>uenza), HL (holiday), RF (rainfall), TP (temperature), WD (wind speed), and HM (humidity). In general, the results reported in Table 2 are aligned with real-life observations. For example, patient arrivals decrease from Mondays to Sundays, and increase signi<sup>fi</sup>cantly during in<sup>fl</sup>uenza outbreaks. Among climatic variables, windy days (i.e. RF>0) deter patients from visiting the ED $( \mathrm { r } = - 0 . 1 4 , p { < } 0 . 0 1 ; \mathrm { ~ r } = - 0 . 1 5 ,$ pb0.01). TP affects C4 positively $( \Gamma = 0 . 4 0 , p { < } 0 . 0 5 )$ whereas HM affects C4 negatively $( \Gamma = - 0 . 1 5 , p { < } 0 . 0 1 )$ , but both impose little impact on C3 $( \mathrm { r } = 0 . 0 2 , p > 0 . 0 5 ; \mathrm { r } = - 0 . 0 1 , p > 0 . 0 5 )$ ). An exceptional <sup>fi</sup>nding is that RF reduced C3 (r=−0.12, pb0.05) but it makes no impact on C4 (r= 0.01, p>0.05). Not surprisingly, neither WK nor IF is associated with climatic variables.

Based on the results reported in Table 2, two relation diagrams can be constructed for C3 and C4, as shown in Fig. 3a and b, respectively, where circles represent all variables and solid lines represent signi<sup>fi</sup>cant correlations. Following the procedures mentioned in Subsection 3.2, TP and HM in Fig. 3a and RF in Fig. 3b are omitted due to the missing direct link to C3 or C4. Two relation diagrams are then revised into Fig. 3c and d, where the dotted lines are the connections that need to be re-examined by partial correlation analysis. The signi<sup>fi</sup>cant partial coef<sup>fi</sup>cients reported in Table 3 suggest that all connections should be maintained. Although interactions can be observed between climatic variables as shown in Fig. 3c and d, those interactions are not consid ered as climatic interaction terms due to their low contribution to the modeling accuracy [35]. In short, input variables of ANN-based models for C3 and C4 are the following: WK, IF, RF, WD (Fig. 3c), and WK, IF, WD, HM, TP (Fig. 3d), respectively.

## 4.2. Comparison between ANN, MLR and NLLSR

Table 4 shows the performance of ANN with varying numbers of hidden neurons (P). ANN with the smallest average and standard deviation of MAPE are considered as the best predictor for modeling patient arrival. In general, MAPE may become smaller as P increases and larger when over-<sup>fi</sup>tting occurs. Thus, trained ANN cannot be generalized in the validation dataset. However, this trend is occasionally unstable due to the various sources of randomness during data processing. Therefore, instead of the best ANN model, two ANN models that possess similarly smaller average values and standard deviations of MAPE, compared with their counterparts, are selected. Based on the results in Table 4, the optimal ANN with P=15 and 16 are the best for C3, and whereas those with P=13 and 14 are the best for C4. Table 5 shows the comparison among the ANN models, MLR and NLLSR over the tenfold cross-validation process. The ANN models are shown to outperform NLLSR and MLR in terms of MAPE. The outperformance of ANN is con<sup>fi</sup>rmed by two-sample t-test. The four null hypotheses H1 to H4 for C3 are as follows:

H1. The performance of ANN (P=15) is NOT signi<sup>fi</sup>cantly different from that of NLLSR.

H2. The performance of ANN (P=15) is NOT signi<sup>fi</sup>cantly different from that of MLR.

H3. The performance of ANN (P= 16) is NOT signi<sup>fi</sup>cantly different from that of NLLSR.

H4. The performance of ANN (P=16) is NOT signi<sup>fi</sup>cantly different from that of MLR.

The other four hypotheses H5 to H8 for C4 are constructed in the same manner, except for P=13 and 14. The t-test results are shown in Table 6. At the con<sup>fi</sup>dence level of 95%, all null hypotheses H1 to H8 are rejected, indicating that ANN can outperform NLLSR and MLR signi<sup>fi</sup>cantly.

## 4.3. Validation of ANN-based RI

4.3.1. Comparison of average value of ANN- and MLR-based RI

Fig. 4 shows the average value of RI using four ANN-based methods (i.e. Garson, Yoon, COE, sensitivity analysis) and the MLR-based method (i.e., LMG) across the tenfold cross-validation process. Statistically, weekday (WK) and in<sup>fl</sup>uenza outbreak level (IF) are found to be the two major contributing variables to C3 and C4. However, some differences in the ranking of contributing variables generated by various methods can be observed. For C3, weekday (WK) and in<sup>fl</sup>uenza (IF) rank the <sup>fi</sup>rst and second, respectively, by all methods, except sensitivity analysis, and followed by rainfall (RF) and wind (WD), as shown in Fig. 4a. For C4, as presented in Fig. 4b, in<sup>fl</sup>uenza (IF) is deemed to be the most predominant variable. Weekday (WK), which is the most important variable for C3, is only the second most important variable to C4. Moreover, the three climatic variables (HM, TP, and WD) are found to share the same degree of in<sup>fl</sup>uence on C4. Overall, all methods can generate a similar ranking of contributing variables to patient arrivals except for the minor disagreement on the importance of climatic variables. Except for the sensitivity analysis, Garson's, Yoon's, and COE methods compute a similar RI for all contributing variables, compared with the LMG method.

Summary statistics of MAPE of ANN across the 10-fold cross-validation with varying hidden neurons.

<table><tr><td>P</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td></tr><tr><td colspan="16">Category 3 patient arrivals</td></tr><tr><td>Mean</td><td>8.73</td><td>8.69</td><td>8.46</td><td>8.63</td><td>8.29</td><td>8.39</td><td>8.26</td><td>8.14</td><td>8.05</td><td>7.96</td><td>7.31</td><td>7.77</td><td>8.2</td><td>8.09</td><td>8.22</td></tr><tr><td>SD</td><td>1.48</td><td>1.62</td><td>2.80</td><td>2.39</td><td>1.43</td><td>1.91</td><td>1.39</td><td>1.74</td><td>1.58</td><td>2.14</td><td>1.13</td><td>1.22</td><td>1.01</td><td>1.03</td><td>1.68</td></tr><tr><td>Min</td><td>7.40</td><td>6.37</td><td>5.86</td><td>5.15</td><td>6.22</td><td>5.68</td><td>6.50</td><td>5.74</td><td>5.47</td><td>5.32</td><td>5.61</td><td>5.77</td><td>6.06</td><td>6.15</td><td>6.31</td></tr><tr><td>Max</td><td>12.06</td><td>12.22</td><td>14.97</td><td>13.04</td><td>10.87</td><td>11.10</td><td>10.93</td><td>10.29</td><td>10.73</td><td>11.98</td><td>8.95</td><td>9.96</td><td>9.43</td><td>9.45</td><td>12.39</td></tr><tr><td colspan="16">Category 4 patient arrivals</td></tr><tr><td>Mean</td><td>7.42</td><td>7.52</td><td>7.23</td><td>7.02</td><td>6.81</td><td>6.96</td><td>6.99</td><td>6.71</td><td>6.43</td><td>6.38</td><td>6.77</td><td>6.83</td><td>7.19</td><td>7.24</td><td>7.34</td></tr><tr><td>SD</td><td>1.21</td><td>1.10</td><td>1.33</td><td>1.25</td><td>0.82</td><td>1.76</td><td>1.11</td><td>1.00</td><td>1.09</td><td>0.86</td><td>1.05</td><td>1.04</td><td>0.86</td><td>1.45</td><td>1.53</td></tr><tr><td>Min</td><td>6.02</td><td>6.03</td><td>5.86</td><td>5.53</td><td>5.61</td><td>5.39</td><td>5.71</td><td>5.21</td><td>5.13</td><td>5.10</td><td>5.80</td><td>5.77</td><td>6.17</td><td>5.78</td><td>5.60</td></tr><tr><td>Max</td><td>10.38</td><td>9.07</td><td>9.83</td><td>9.33</td><td>8.08</td><td>11.24</td><td>8.89</td><td>8.55</td><td>8.18</td><td>7.92</td><td>8.89</td><td>9.07</td><td>8.58</td><td>9.97</td><td>9.57</td></tr></table>

P: number of neuron in the hidden layer.  
SD: standard deviation.

Table 5  
Comparison of modeling accuracy between ANN and two statistical models using the same set of input variables.

<table><tr><td rowspan="2">Test no.</td><td colspan="4">Category 3 patient arrivals</td><td colspan="4">Category 4 patient arrivals</td></tr><tr><td>ANN (P=15)</td><td>ANN (P=16)</td><td>NLLSR</td><td>MLR</td><td>ANN (P=13)</td><td>ANN (P=14)</td><td>NLLSR</td><td>MLR</td></tr><tr><td>1</td><td>8.02</td><td>7.96</td><td>8.50</td><td>7.45</td><td>5.13</td><td>6.60</td><td>7.30</td><td>8.54</td></tr><tr><td>2</td><td>5.80</td><td>8.74</td><td>7.52</td><td>10.12</td><td>6.06</td><td>6.84</td><td>7.02</td><td>7.97</td></tr><tr><td>3</td><td>7.39</td><td>7.59</td><td>8.51</td><td>10.40</td><td>7.95</td><td>5.88</td><td>9.97</td><td>7.77</td></tr><tr><td>4</td><td>7.42</td><td>9.53</td><td>9.43</td><td>9.73</td><td>5.87</td><td>5.10</td><td>5.65</td><td>6.60</td></tr><tr><td>5</td><td>7.40</td><td>6.03</td><td>10.15</td><td>10.80</td><td>5.30</td><td>5.72</td><td>8.35</td><td>7.05</td></tr><tr><td>6</td><td>7.85</td><td>9.29</td><td>10.72</td><td>10.13</td><td>5.76</td><td>5.56</td><td>8.01</td><td>8.33</td></tr><tr><td>7</td><td>5.93</td><td>7.47</td><td>9.97</td><td>9.06</td><td>6.16</td><td>7.92</td><td>7.07</td><td>10.47</td></tr><tr><td>8</td><td>7.00</td><td>7.47</td><td>8.49</td><td>8.71</td><td>7.96</td><td>7.64</td><td>7.73</td><td>6.90</td></tr><tr><td>9</td><td>9.92</td><td>8.12</td><td>10.54</td><td>11.38</td><td>5.93</td><td>6.52</td><td>8.63</td><td>8.69</td></tr><tr><td>10</td><td>6.38</td><td>5.50</td><td>6.36</td><td>7.32</td><td>8.18</td><td>6.03</td><td>5.66</td><td>6.27</td></tr><tr><td>Mean</td><td>7.31</td><td>7.77</td><td>9.02</td><td>9.51</td><td>6.43</td><td>6.38</td><td>7.54</td><td>7.86</td></tr><tr><td>SD</td><td>1.13</td><td>1.22</td><td>1.33</td><td>1.29</td><td>1.09</td><td>0.86</td><td>1.25</td><td>1.18</td></tr><tr><td>Min</td><td>5.80</td><td>5.50</td><td>6.36</td><td>6.64</td><td>5.13</td><td>5.10</td><td>5.66</td><td>5.27</td></tr><tr><td>Max</td><td>9.92</td><td>9.53</td><td>10.72</td><td>11.49</td><td>8.18</td><td>7.92</td><td>9.97</td><td>10.47</td></tr></table>

MLR: multiple linear regression

## 4.3.2. Ranking similarity between ANN- and MLR-based RI

Table 7 shows the Spearman's coef<sup>fi</sup>cients between the rankings generated by ANN-based methods and those by the LMG method over the tenfold cross validation process. The coef<sup>fi</sup>cients (r=0.65– 0.70, pb0.01) suggest that Garson's, Yoon's, and COE methods are generally consistent with the LMG method in obtaining the RI of contributing variables to C3. The same observation can be made for C4. Speci<sup>fi</sup>cally, sensitivity analysis is less consistent with the LMG method for both C3 and C4 (r=0.44, r=0.35, pb0.01).

In summary, the results reported in Subsections 4.3.1 and 4.3.2 suggest that ANN-based methods of computing variables' RI are statistically comparable to the MLR-based method (i.e., LMG). Hence, ANN-based RI is validated as reliable or “genuine”.

## 5. Discussion

In contrast to the use of empirical knowledge in previous studies, the <sup>fi</sup>rst stage of our method adopts correlation and partial correlation analysis to screen out input variables that are directly correlated

## Table 6

Two-sample t-test for average MAPE under ANN, NLLSR, and MLR

<table><tr><td colspan="2">Category 3 patient arrivals</td><td colspan="2">Category 4 patient arrivals</td></tr><tr><td>Hypothesis</td><td>p-value</td><td>Hypothesis</td><td>p-value</td></tr><tr><td>H1</td><td>0.005</td><td>H5</td><td>0.030</td></tr><tr><td>H2</td><td>0.001</td><td>H6</td><td>0.008</td></tr><tr><td>H3</td><td>0.026</td><td>H7</td><td>0.018</td></tr><tr><td>H4</td><td>0.004</td><td>H8</td><td>0.004</td></tr></table>

to daily patient arrivals. This data-driven method is particularly useful in a case that involves a large set of interdependent variables. Although ANN can model the complex association among those variables, they must be reduced to their simplest form for the sake of clarity and conciseness, especially when extracting hints from its structure to provide explanatory information. On the other hand, the results of correlation analysis can help ED decision-makers under stand and capture the complex relationship among variables. Most of the signi<sup>fi</sup>cant correlations reported in Table 2 are consistent with empirical knowledge and real observations. For example, patient arrivals of both categories are deemed sensitive to weekday (WK) factors. This observation can be described by the general psycholog of people: most people visit EDs on weekdays because doing so allows them to take a day-off and claim medical reimbursement. This logic also explains the higher number of arrivals on Mondays in the target ED, and the same observation has been reported in previ ous studies [5,7,30,31,35,51]. The effect of in<sup>fl</sup>uenza (IF) on patient arrivals is also found prominent by referring to the sharp increase of ED attendance during the human swine <sup>fl</sup>u outbreak. During that period, most of the patients claiming <sup>fl</sup>u infection were triaged to C4. Thus, IF is deemed as more determinant than WK for C4 patients, whereas the opposite is true for C3 patients. The results likewise imply that undesirable weather conditions, such as typhoons and rain storms that cause drastic change to rainfall (RF) and wind speed (WD), would discourage C3 and C4 patient arrivals. Interestingly, temperature (TP) alone barely affects C3 patient arrivals. This <sup>fi</sup>nding is because the deci sion of C3 patients to go to an ED is made mainly based on their severity, regardless of undesirably high or low temperature. However, for C4 patients, whose conditions are less serious, TP is a factor in deciding or planning a visit to the ED, and C4 patients usually prefer to visit the ED on warm days. Meanwhile, the vulnerability to common ailments on hot days, such as heat stroke, cold, diarrhea, arthritis, and others also increases C4 patient arrivals. Nevertheless, some results are found to be against common knowledge. For example, holiday variables are not found to affect patient arrivals, and rainy days are not observed to reduce C4 arrivals $( \Gamma = 0 . 0 1 , p { > } 0 . 0 5 )$ . The former coincides with ED staff's opinion that signi<sup>fi</sup>cant <sup>fl</sup>uctuation of patient arrivals are only observed during long holidays such as Easter, Christmas and Chinese New Year, whereas in other shorter holidays, the <sup>fl</sup>uctuation is not obvious. Thus, the model can be improved by only including the vari able of long holidays. For the latter, the possible explanation would be that the deterrent effect of rainy weather on C4 arrivals is offset by the increased colds and minor injuries under rainy weather condi tion [42,60]. Overall, although the <sup>fi</sup>nal relation diagrams are no perfectly adherent to our empirical knowledge, they are nevertheless trustworthy from a statistical point of view because subjective judg ment has been omitted.

The second stage is motivated by the presence of nonlinearity in real systems. Linear methods have been commonly utilized in modern health care research [14], such as in diagnoses of diseases and calculation of performance metrics. However, a pure linear relation among variables hardly exists in reality. Moreover, the normality of output variables is always assumed in patient arrival studies. In this regard, using linear regression to model non-normally distributed output variables could lead to poor <sup>fi</sup>t and tendency of committing type II error, i.e., the model fails to detect the signi<sup>fi</sup>cant effect of an input variable when one truly exists [41]. In this study, the patient arrivals are proved to be normally distributed such so that the log-transfer of output data is not necessary [35]. Moreover, using linear regression to model patient arrivals may lead to multicolinearity, which occurs when input variables are correlated. This issue is another infringement to the basic assumption of linear models. Hence, linear regression may not be appropriate for modeling patient arrivals because all climatic variables linked to C3 and C4 are correlated, as shown in Fig. 3c and d. For the result of this stage, the number of hidden neurons constituting the optimal ANN models for C3 and C4 patient arrivals is largely data-dependent due to the lack of analytical procedures for identifying the optimal number of hidden neurons. Different numbers may be generated given a different set of training and test data. The cross-validation in Table 4 is therefore important because it selects the optimal number of hidden neuron by testing on 10 different combinations of training and test data. As a result, the numbers of hidden neurons selected in Table 5 are statistically meaningful. This data-dependent characteristic of ANN does not favor model generalization, but it is encouraging in a sense that the model user can improve the modeling accuracy to the maximum extent by tuning the structures and parameters of the model. Linear methods such as MLR do not have this <sup>fl</sup>exibility. Testing is not done on more than one hidden layer for ANN models because most of the input–output relations can be appropriately described by a model with a single hidden layer [8,9]. Overall, the use of ANN frees up decision-makers from preprocessing input and output data to meet the linear regression prerequisites. Although ANN has also been criticized for lacking statistical ground, and the determination of optimal ANN structure is contentious in terms of the learning algorithm, the number of hidden layers and neurons, and other issues, these disadvantages should not override its strong ability of modeling complex input–output relations.

Table 7  
![](/api/attachments/A2CRCR8Y/fulltext/images/402a8a97d6dbd448480aa9a9144c4952674704145b7941c6e258f2c0cc5e7898.jpg)  
Fig. 4. Average relative importance of input variables across 10-fold cross-validation.

The third stage investigates the statistical reliability of different types of ANN-based RI. Fig. 4 and Table 7 indicate that the RIs computed by four ANN-based methods are statistically comparable to the results of the LMG method. This <sup>fi</sup>nding is important because it allows model users to extract statistically reliable RI from a nonstatistical yet sophisticated model such as ANN. The result of this stage is consistent with empirical knowledge, which dictates that in-<sup>fl</sup>uenza and weekdays carry more importance than weather factors in modeling daily patient arrivals of C3 and C4 patients. The result also answers the research questions raised in the abstract.

In practice, this ANN model provides a logical basis for better planning of ED operations. The ED decision-maker can predict patient arrivals for speci<sup>fi</sup>c days by feeding the corresponding values of the input factors to the ANN model. Accurate predictions for the days when the patient arrivals is likely to deviate from the normal, such as Mondays, weekends, extreme weather conditions, in<sup>fl</sup>uenza outbreak, and others, are particularly important for the timely adjustment of resource allocation and care delivery process for C3 and C4 patients. The available options for such adjustment may include 1) differentiating the staf<sup>fi</sup>ng level from Mondays to Sundays, 2) increasing/reducing the number of nurses and doctors dedicated to C3 or C4 patients, 3) designating an area within the observation room to accommodate the impending over<sup>fl</sup>ow of C3 patients, and 4) opening up a fast-track lane for C4 patients with unbearable pain and minor injuries. All the above adjustments are critical for the improvement of service quality and experience of ED patients. For example, when a C4 patient surge is predicted, changing the patient <sup>fl</sup>ow to fast-track mode for patients with pain and injuries would signi<sup>fi</sup>cantly shorten the overall waiting time of C4 patients.

Spearman's rank correlation coef<sup>fi</sup>cients of RI rankings of input variables

<table><tr><td></td><td></td><td>Garson</td><td>Yoon</td><td>COE</td><td>SA</td></tr><tr><td>Category 3 arrivals</td><td>LMG</td><td>0.70**</td><td>0.65**</td><td>0.68**</td><td>0.44**</td></tr><tr><td>Category 4 arrivals</td><td>LMG</td><td>0.65**</td><td>0.56**</td><td>0.61**</td><td>0.35**</td></tr></table>

SA: sensitivity analysis. Signi<sup>fi</sup>cance code: 0.01\*\*.

The contribution of this paper is twofold. Theoretically, this paper stresses the usefulness of data-driven approach to variable selection for complex system modeling, and then provides a comprehensive comparison of several RI computation methods. Practically, this is a novel attempt of applying ANN to model patient arrivals whereby the results are critical to ED management strategy, including resource planning and allocation, care delivery <sup>fl</sup>ow changes, and staff scheduling ahead of predicted arrival variations. In a broad sense, this study resonates the recent trend of using industrial engineering techniques to improve ED performance. Similar studies have been noted. For example, Cheng et al. [17] applied a new fuzzy time-series based on weighted-transitional matrix to forecast outpatient visits. Williams et al. [53] reported the association between patient arrivals and waiting time using a quantitative modeling technique. Ahmed and Alkhamis [2] identi<sup>fi</sup>ed the optimal staff level using discrete-event simulation. Yeh and Lin [58] and Puente et al. [40] applied genetic algorithms to resolve the scheduling problem of nurses and doctors. The current study is the <sup>fi</sup>rst step towards the ultimate target of building a simulation-based decision support system to guide ED operations in response to the fast and varying patient arrivals.

## 6. Conclusions

In this paper, correlation analysis was applied to identify key variables that contribute to the daily patient arrival based on one year data from a local ED. Then, we used ANN to model the association between these contributing variables and daily patient arrivals. Its superiority over two benchmarking methods in terms of modeling accuracy was also con<sup>fi</sup>rmed. The model will be helpful for ED decision-making on resource planning and <sup>fl</sup>ow adjustment in the process of achieving excellent service. Moreover, four ANN-based methods of computing RI of input variables were compared, and their statistically reliability was tested with an MLR-based method, namely, LMG. Except for the sensitivity analysis, three other methods (Garson's, Yoon's, and COE) were con<sup>fi</sup>rmed reliable. Although computing RI was not the primary purpose when the ANN was originally invented, it is an important supplement to the ANN theory, particularly in real applications where RI carries considerable amount of weight in the exercise of decision-making.

This study has three distinctive features. First, we adopted a datadriven approach rather than empirical knowledge to select key contributing variables to ensure the statistical correlation between all the selected variables and the daily patient arrivals. Second, we used ANN to model daily patient arrivals as opposed to the linear methods widely used in the literature. Third, we con<sup>fi</sup>rmed that the reliability of ANN-based RI is statistically comparable to that from a pure statistical model, such as MLR. This <sup>fi</sup>nding is very important because the user of ANN can extract the explanatory information from its hidden and complex structure.

The results of this study need to be interpreted with caution due to two limitations. First, this paper did not compare ANN with other nonlinear techniques aside from NLLSR. Therefore, the results are inconclusive with regard to the superiority of ANN for modeling patient arrivals over other approaches. Second, this work did not take into account data on patients who left without being seen, which accounted for less than 3% of the total patients. Data integrity was further undermined by the missing data of return patients who need followup treatments. Finally, the optimal ANN models determined by the contributing variables and number of hidden neurons may be subject to the particular ED context where this study was conducted, thereby limiting generalizability.

Our future work intends to focus on three directions. First, the results of current research can be re<sup>fi</sup>ned by extending data collection beyond one year so that monthly pattern can be studied. The weather variables ahead of the predicting day can likewise be included to the ANN model given the widely accepted experience that weather changes take a while before causing common ailments on patients. Second, a similar ANN model can be developed for real-time prediction of remaining waiting time before the <sup>fi</sup>rst doctor consultation. When excessive waiting for consecutive patients is predicted, the model will indicate increasing patient demands, and the ED decisionmaker will be prompted to revise manpower allocation and make other adjustments to expedite the ED operation. This waiting time prediction model will supplement the patient arrival model reported in this paper so that both real-time and long-term demands can be estimated for ED resource planning. Finally, our three-stage method can be extended to other healthcare related topics characterized by complex input–output relations and the desirability of estimating RI of contributing variables, such as in identifying contributing factors to a speci<sup>fi</sup>c disease and computing the RI.

## Acknowledgement

The work described in this paper was partially supported by a grant from the City University of Hong Kong SRG project no. 7002773. The authors would like to thank several anonymous reviewers for their helpful comments and suggestions on this paper.

Appendix A. Triage system in Hong Kong accident and Emergency Departments

<table><tr><td>Triage category</td><td>Patient conditions</td><td>Actions of staff</td><td>Target response time</td></tr><tr><td>1 (Critical)</td><td>Suffers from a life-threatening condition(s) caused by a major eventWith unstable vital signs requiring immediate resuscitation</td><td>Direct patient to resuscitation roomAttend to patient immediately by a team comprising medical and nursing staff</td><td>Immediate100% of cases within the target response time</td></tr><tr><td>2 (Emergency)</td><td>Suffers from a potentially life-threatening conditionBorderline vital signs but with potential risk of rapid deteriorationRequire emergency treatment and immediate continuous close monitoring</td><td>Direct patient to resuscitation room/treatment cubicleOffer medical attention and immediate continuous close monitoring within 15 min.</td><td>&lt;15 min95% of cases within the target response time</td></tr><tr><td>3 (Urgent)</td><td>Suffers from a major condition with potential risk of deteriorationStable vital signs</td><td>Direct patient to cubicle</td><td>&lt;30 min90% of cases within the target response time</td></tr><tr><td>4 (Semi-urgent)</td><td>Suffers from acute but stable condition(s)Stable vital signsCan afford to wait some time without serious complications</td><td>Direct patient to cubicle/walk-in clinic</td><td></td></tr><tr><td>5 (Non-urgent)</td><td>Suffers from minor and stable condition(s) (including acute and non-acute conditions)Stable vital signsCan afford to wait without deterioration</td><td>Direct patient to cubicle/walk-in clinic</td><td></td></tr></table>

## Appendix B. LMG method of computing RI based on an MLR model

The $R ^ { 2 }$ for a MLR model with input variables in set S is de<sup>fi</sup>ned by Eq. (11).

$$
R ^ {2} (S) = \frac {\text { Model   SS } (\text { model   with   explanatory   variables   in   S })}{\text { Total   SS }},\tag{11}
$$

and the additional $R ^ { 2 }$ after adding the input variables in set M to the original model with input variables in set S is de<sup>fi</sup>ned by Eq. (12).

$$
\operatorname{seq} R ^ {2} (M | S) = R ^ {2} (M \cup S) - R ^ {2} (S).\tag{12}
$$

The order in which input variables enter into the model is denoted by the index array $r = ( r _ { 1 } , . . . , r _ { n } )$ , which is a permutation of the input variables' index $\{ 1 , . . . , p \}$ . Let $S _ { k } ( r )$ denotes the set of input variables entering the model before input variable $x _ { k }$ in the order r, then the portion of $R ^ { 2 }$ accounted by $x _ { k }$ is

$$
\operatorname{seq} R ^ {2} \left(\left\{x _ {k} \right\} \mid S _ {k} (r)\right) = R ^ {2} \left(\left\{x _ {k} \right\} \cup S _ {k} (r)\right) - R ^ {2} \left(S _ {k} (r)\right).\tag{13}
$$

Based on Eq. (13), the RI of contributing variables by LMG method can be written as

$$
L M G (x _ {k}) = \frac {1}{p !} _ {r} \sum_ {\text { permutation }} \operatorname{seq} R ^ {2} (\{x _ {k} \} | r).\tag{14}
$$

Similar to previous practice, the RI of contributing variables are normalized into [0, 1].

## References

[1] R.E. Abdel-Aal, Univariate modeling and forecasting of monthly energy demand time series using abductive and neural networks, Computers and Industrial Engineering 54 (2008) 903–917.

[2] M.A. Ahmed, T.M. Alkhamis, Simulation optimization for an emergency department healthcare unit in Kuwait, European Journal of Operational Research 198 (2009) 936–942.

[3] S. Aldor-Noiman, P.D. Feigin, A. Mandelbaum, Workload forecasting for a call center: methodology and a case study, The Annals of Applied Statistics 3 (2009) 1403–1447

[4] B.R. Asplin, D.J. Magid, K.V. Rhodes, L.I. Solberg, N. Lurie, C.A. Camargo Jr., A conceptual model of emergency department crowding, Annals of Emergency Medicine 42 (2003) 173–180.

[5] B.R. Asplin, T.J. Flottemesch, B.D. Gordon, Developing models for patient <sup>fl</sup>ow and daily surge capacity research, Academic Emergency Medicine 13 (2006) 1109–1113.

[6] K.F. Au, T.M. Choi, Y. Yu, Fashion retail forecasting by evolutionary neural networks, International Journal of Production Economics 114 (2008) 615–630.

[7] H. Batal, J. Tench, S. McMillan, J. Adams, P.S. Mehler, Predicting patient visits to an urgent care clinic using calendar variables, Academic Emergency Medicine 8 (2001) 45–53.

[8] W.G. Baxt, F.S. Shofer, F.D. Sites, J.E. Hollander, A neural network aid for the early diagnosis of cardiac ischemia in patients presenting to the emergency department with chest pain, Annals of Emergency Medicine 40 (2002) 575–583.

[9] W.G. Baxt, F.S. Shofer, F.D. Sites, J.E. Hollander, A neural computational aid to the diagnosis of acute myocardial infarction, Annals of Emergency Medicine 39 (2002) 366–373.

[10] L. Bianchi, J. Jarrett, R. Choudary Hanumara, Improving forecasting for telemarketing centers by ARIMA modeling with intervention, International Journal of Forecasting 14 (1998) 497–504.

[11] C.M. Bishop, Neural Networks for Pattern Recognition, Clarendon Press, Oxford, 1995.

[12] R. Champion, L.D. Kinsman, G.A. Lee, K.A. Masman, E.A. May, M.D. Taylor, P.R. Thomas, R.J. Williams, Forecasting emergency department presentations, Austrian Health Review 31 (2007) 83–90.

[13] N. Channouf, P. L'Ecuyer, A. Ingolfsson, A. Avramidis, The application of forecasting techniques to modeling emergency medicine system calls in Calgary, Alberta, Health Care Management Science 10 (2007) 25–45

[14] Y.C. Chao, Y. Zhao, L.L. Kupper, L.A. Nylander-French, Quantifying the relative importance of predictors in multiple linear regression analyses for public health studies, Journal of Occupational and Environmental Hygiene 5 (2008) 519–529.

[15] K.Y. Chen, Combining linear and nonlinear model in forecasting tourism demand, Expert Systems with Applications 38 (2011) 10368–10376.

[16] M.S. Chen, L.C. Ying, M.C. Pan, Forecasting tourist arrivals by using the adaptive network-based fuzzy inference system, Expert Systems with Applications 37 (2010) 1185–1191.

[17] C.H. Cheng, J.W. Wang, C.H. Li, Forecasting the number of outpatient visits using a new fuzzy time series based on weighted-transitional matrix, Expert Systems with Applications 34 (2008) 2568–2575.

[18] C.W. Chu, G.P. Zhang, A comparative study of linear and nonlinear models for aggregate retail sales forecasting, International Journal of Production Economics 86 (2003) 217–231.

[19] H.C. Co, R. Boosarawongse, Forecasting Thailand's rice export: statistical techniques vs. arti<sup>fi</sup>cial neural networks, Computers and Industrial Engineering 53 (2007) 610–627.

[20] T.J. Flottemesch, B.D. Gordon, S.S. Jones, Advanced statistics: developing a formal model of emergency department census and de<sup>fi</sup>ning operational ef<sup>fi</sup>ciency, Academic Emergency Medicine 14 (2007) 799–809

[21] G.D. Garson, Interpreting neural-network connection weights, AI Expert 6 (1991) 47–51.

[22] M. Gevrey, I. Dimopoulos, S. Lek, Review and comparison of methods to study the contribution of variables in arti<sup>fi</sup>cial neural network models, Ecological Modelling 160 (2003) 249–264.

[23] E. González-Romera, M.A. Jaramillo-Morán, D. Carmona-Fernández, Forecasting of the electric energy demand trend and monthly <sup>fl</sup>uctuation with neural networks, Computers and Industrial Engineering 52 (2007) 336–343.

[24] L.V. Green, P.J. Kolesar, W. Whitt, Coping with time-varying demand when setting staf<sup>fi</sup>ng requirements for a service system, Production and Operations Management 16 (2007) 13–39.

[25] U. Grömping, Relative importance for linear regression in R: the package relaimpo, Journal of Statistical Software 17 (2006).

[26] R.F. Harrison, R.L. Kennedy, Arti<sup>fi</sup>cial neural network models for prediction of acute coronary syndromes using clinical data from the time of presentation, Annals of Emergency Medicine 46 (2005) 431–439.

[27] J.E. Hollander, K.L. Sease, D.M. Sparano, F.D. Sites, F.S. Shofer, W.G. Baxt, Effects of neural network feedback to physicians on admit/discharge decision for emergency department patients with chest pain, Annals of Emergency Medicine 44 (2004) 199–205.

[28] L.I. Horwitz, J. Green, E.H. Bradley, US emergency department performance on waiting time and length of visit, Annals of Emergency Medicine 55 (2010) 133–141.

[29] R. Howes, N. Crook, Using input parameter in<sup>fl</sup>uences to support the decisions of feedforward neural networks, Neurocomputing 24 (1999) 191–206.

[30] S.S. Jones, A. Thomas, R.S. Evans, S.J. Welch, P.J. Haug, G.L. Snow, Forecasting daily patient volumes in the emergency department, Academic Emergency Medicine 15 (2008) 159–170.

[31] S.S. Jones, R.S. Evans, T.L. Allen, A. Thomas, P.J. Haug, S.J. Welch, G.L. Snow, A multivariate time series approach to modeling and forecasting demand in the emergency department, Journal of Biomedical Informatics 42 (2009) 123–139.

[32] C.T. Lin, I.F. Lee, Arti<sup>fi</sup>cial intelligence diagnosis algorithm for expanding a precision expert forecasting system, Expert Systems with Applications 36 (2009) 8385–8390.

[33] R.H. Lindeman, P.F. Merenda, R.Z. Gold, Introduction to Bivariate and Multivariate analysis, Scott, Foresman, Glenview, IL, 1980.

[34] C.J. Lu, Y.W. Wang, Combining independent component analysis and growing hierarchical self-organizing maps with support vector regression in product demand forecasting, International Journal of Production Economics 128 (2010) 603–613.

[35] M.L. McCarthy, S.L. Zeger, R. Ding, D. Aronsky, N.R. Hoot, G.D. Kelen, The challenge of predicting demand for emergency department services, Academic Emergency Medicine 15 (2008) 337–346

[36] Y. Ni, F. Fan, A two-stage dynamic sales forecasting model for the fashion retail, Expert Systems with Applications 38 (2011) 1529–1536.

[37] J.D. Olden, D.A. Jackson, Illuminating the “black box”: a randomization approach for understanding variable contributions in arti<sup>fi</sup>cial neural networks, Ecological Modelling 154 (2002) 135–150

[38] J.D. Olden, M.K. Joy, R.G. Death, An accurate comparison of methods for quantifying variable importance in arti<sup>fi</sup>cial neural networks using simulated data, Ecological Modelling 178 (2004) 389–397.

[39] S.L. Özesmi, U. Özesmi, An arti<sup>fi</sup>cial neural network approach to spatial habitat modeling with interspeci<sup>fi</sup>c interaction, Ecological Modelling 116 (1999) 15–31.

[40] J. Puente, A. Gómez, I. Fernández, P. Priore, Medical doctor rostering problem in a hospital emergency department by means of genetic algorithms, Computers and Industrial Engineering 56 (2009) 1232–1242.

[41] M. Qualls, D.J. Pallin, J.D. Schuur, Parametric versus nonparametric statistical tests: the length of stay example, Academic Emergency Medicine 17 (2010) 1113-1121

[42] W.R. Rising, I.A. O'Daniel. C.S. Roberts, Correlating weather and trauma admissions at a level I trauma center, The Journal of Trauma 60 (2006) 1096–1100.

[43] L.M. Schweigler, J.S. Desmond, M.L. McCarthy, K.J. Bukowski, E.L. Ionides, J.G. Younger, Forecasting models of emergency department crowding, Academic Emergency Medicine 16 (2009) 301–308.

[44] H. Setzler, C. Saydam, S. Park, EMS call volume predictions: a comparative study, Computers and Operations Research 36 (2009) 1843–1851.

[45] H. Shen, J.Z. Huang, Interday forecasting and intraday updating of call center arrivals, Manufacturing & Service Operations Management 10 (2008) 391–410.

[46] A.H. Sung, Ranking importance of input parameters of neural networks, Expert Systems with Applications 15 (1998) 405–411.

[47] J.W. Taylor, A comparison of univariate time series methods for forecasting intraday arrivals at a call center, Management Science 54 (2008) 253–265.

[48] J.W. Taylor, Triple seasonal methods for short-term electricity demand forecasting, European Journal of Operational Research 204 (2010) 139–152.

[49] S.H. Tsaur, Y.C. Chiu, C.H. Huang, Determinants of guest loyalty to international tourist hotels — a neural network approach, Tourism Management 23 (2002) 397–405.

[50] W. Tych, D.J. Pedregal, P.C. Young, J. Davies, An unobserved component model for multi-rate forecasting of telephone call demand: the design of a forecasting support system, International Journal of Forecasting 18 (2002) 673–695.

[51] M. Wargon, E. Casalino, B. Guidet, From model to forecasting: a multicenter study in emergency departments, Academic Emergency Medicine 17 (2010) 970–978.

[52] J. Weinberg, L.D. Brown, J.R. Stroud, Bayesian forecasting of an inhomogeneous Poisson process with applications to call center data, Journal of the American Statistical Association 102 (2007).1185-1198

[53] P. Williams, G. Tai, Y. Lei, Simulation based analysis of patient arrival to health care systems and evaluation of an operations improvement scheme, Annals of Operations Research 178 (2010) 263-279

[54] T.C. Wong, K.M.Y. Law, H.K. Yau, S.C. Ngan, Analyzing supply chain operation models with the PC-algorithm and the neural network, Expert Systems with Applications 38 (2011) 7526–7534.

[55] T.C. Wong, S.Y. Wong, K.S. Chin, A neural network-based approach of quantifying relative importance among various determinants toward organizational innovation, Expert Systems with Applications 38 (2011) 13064–13072.

[56] T.C. Wong, S.C. Ngan, F.T.S. Chan, A.Y.L. Chong, A two-stage analysis of the in<sup>fl</sup>uences of employee alignment on effecting business-IT alignment, Decision Support Systems 53 (2012) 490–498.

[57] W. Xu, Long range planning for call centers at Fedex, The Journal of Business Forecasting Methods and Systems 18 (2000) 7–11.

[58] J.Y. Yeh, W.S. Lin, Using simulation technique and genetic algorithm to improve the quality of a hospital emergency department, Expert Systems with Applications 32 (2007) 1073–1083.

[59] Y. Yoon, T. Guimaraes, G. Swales, Integrating arti<sup>fi</sup>cial neural networks with rule-based expert systems, Decision Support Systems 11 (1994) 497–507.

[60] L.M. Zibners, B.K. Bonsu, J.R. Hayes, D.M. Cohen, Local weather effects on emergency department visits, Pediatric Emergency Care 22 (2006) 104–106.

M. Xu received his B. Eng. degree in Industrial Engineering and Engineering Management from the City University of Hong Kong and he is currently a PhD student in the Department of Systems Engineering and Engineering Management. His current research interests include simulation and staff scheduling for healthcare systems such as hospital and emergency departments.

Dr. T. C. Wong received his B. Eng. degree in Industrial Engineering and the M. Phil. and PhD degrees in Operations Research from the University of Hong Kong, Pokfulam, Hong Kong, in 2002, 2005, and 2008, respectively. He is currently with the Department of Systems Engineering and Engineering Management, City University of Hong Kong. His current research interests include operations research, computation optimization and modeling, supply chain management, and evolutionary algorithms.

Dr. Kwai-Sang Chin is an associate professor at the Department of Systems Engineering and Engineering Management, City University of Hong Kong. He is a Charter Engineer in U.K., a Registered Professional Engineer in Hong Kong, and Fellow Member of the American Society for Quality, Hong Kong Society for Quality and Hong Kong Quality Management Association. He is also the Programme Leader of B. Eng. Total Quality Engineering in the Department. He maintains intensive collaboration with industries through various consultancy work, training courses and industrial projects. His current research interests are Quality Systems and Management, New Product Design and Development, and Decision Support Systems. He has published a signi<sup>fi</sup>cant number of papers in peer reviewed journals such as IEEE Transactions on Engineering Management, IEEE Transactions on Fuzzy Systems, European Journal of Operational Research, Decision Support Systems, Information Sciences, Expert Systems with Applications, International Journal of Production Research, International Journal of Quality and Reliability Management, Industrial Management and Data Systems, International Journal of Advanced Manufacturing Technology, and the like.
