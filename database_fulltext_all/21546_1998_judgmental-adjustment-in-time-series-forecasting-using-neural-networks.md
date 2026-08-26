---
otero_id: 21546
otero_key: "MWZVRA6P"
title: "Judgmental adjustment in time series forecasting using neural networks"
authors: "Jae Kyu Lee; Chang Seon Yum"
year: "1998"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(97)00050-x"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Judgmental adjustment in time series forecasting using neural networks

Jae Kyu Lee <sup>)</sup>, Chang Seon Yum

Graduate School of Management, Korea AdÕanced Institute of Science and Technology, 207-43, Cheongryang, Seoul, 130-012, South Korea

## Abstract

Time series models are a highly useful forecasting method, but are deficient in the sense that they merely extrapolate past patterns in the data without taking into account the expected irregular future events. To overcome this limitation, forecasting experts in practice judgmentally adjust the statistical forecasts. Typical judgmental factors may be treated as outliers in statistical analysis. To automate the judgmental adjustment process, neural network models are developed in this study. To collect the data for judgmental events, judgmental effects are filtered out of raw data. The main trend is captured by a neural network model using the filtered data, while judgmental effects are modeled by another neural network. Then the judgmental effects are additively adjusted. Performance of this architecture is tested in comparison with five other architectures. According to the experiments, the architecture of neural network based additive judgmental adjustment significantl improves the forecasting performance. q 1998 Elsevier Science B.V.

Keywords: Time series forecasting; Judgmental factor; Neural network; Neural network based additive judgmental adjustmen

## 1. Introduction

The rationale behind time series models, whether they are based on statistical analysis or neural networks, is that past patterns will continue for the coming periods. When this assumption is not true, the time series model has an inherent limitation because extrapolating the time series model cannot effectively reflect the impact of expected irregular and infrequent future events 3,16,18 .<sup>w</sup> <sup>x</sup>

A method to overcome this limitation can be observed from the forecasting experts practice of judgmental adjustment on the time series models. A set of research supports the paradigm of such human expert’s judgmental adjustments. Georgoff and Murdick 8 claimed that the forecaster should incorpo- <sup>w</sup> <sup>x</sup> rate subjective judgments in dynamic situations when the statistical models can not reflect significant internal and external changes. Edmundson et al. 4 commented that the well-structured judgmental process can consistently outperform the statistical modelbased extrapolation. Wolfe and Flores 26 have<sup>w</sup> <sup>x</sup> shown that the ARIMA AutoRegressive IntegratedŽ Moving Average model based forecasts can be en-. hanced by adopting the Analytical Hierarchy Process Ž . AHP of Satty for the judgmental adjustment. They argued that the accuracy of unadjusted statistical forecasts can be improved by the judgmental adjustment. Flores et al. 6 have compared the perfor- <sup>w</sup> <sup>x</sup> mance of two methods: AHP and centroid based methods. They have shown that the AHP method produced larger absolute adjustments to the objective forecast than the centroid method, although the difference is not significant.

Lee et al. 16 have also empirically shown the<sup>w</sup> <sup>x</sup> superiority of post-judgmental adjustment forecasts with the data of refinery products demand. In their study, the histories of judgments are captured as cases, and a nonmonotonic case based reasoning Ž . CBR scheme is proposed to evaluate the effects of similar new events. A system named UNIK-FCST is developed according to this approach and is currently semi-automatically operational. However, they pointed out the unresolved difficulties of a CBR approach: 1 accommodation of inconsistency Ž . among same situations, 2 generalization of similarŽ . cases, 3 measuring the impact of judgmental events, Ž . and 4 handling the correlation effects among theŽ . judgmental factors.

To overcome these difficulties, this study adopts a neural network approach for modelling judgmental adjustment processes. Since the data points of the historical judgmental adjustments are usually not sufficient for statistical analysis, the neural network is more suitable 9,14,17,19,25 .<sup>w</sup> <sup>x</sup>

The architecture that we propose is denoted as the model MAIN NN Filtered( <sup><</sup> ) ( )<sup>q</sup>JUDGMENTAL NN .

## 1 .1 . M o d e l 1 : M A IN N N F ilte re d( <sup><</sup> ) <sup>q</sup> JUDGMENTAL NN( )

In this architecture, the main trend is forecasted by a neural network model using filtered data. Judgmental effects are estimated by the neural network model, and the effect is additively adjusted.

To validate the proposed architecture, we compared the performance with the following five other architectures.

## 1.2. Model 2: MAIN NN Filtered( <sup><</sup> )

This forecast is only made by a neural network based main trend forecasting model that uses filtered data. This comparison can validate the effectiveness of judgmental adjustments.

## 1.3. Model 3: MAIN NN Raw( <sup><</sup> )

This forecast is made by a single neural network that uses the raw data without filtering the judgmental effects. This comparison can validate the adequacy of the additive adjustment architecture.

## 1.4. Model 4: MAIN NN Filtered and JUDGMEN( <sup><</sup> - TAL)

This neural network is constructed by appending the judgmental factors as inputs to the MAIN NN Filtered ( <sup><</sup> ) model. This comparison can validate the adequacy of the adjustment process with a different architecture.

## 1.5. M odel 5: M AIN ARIM A Filtered( <sup><</sup> ) <sup>q</sup> JUDGMENTAL NN( )

This model has replaced the neural network model for main trend forecasting with the ARIMA model. This comparison can validate the performance of neural network model when compared to the ARIMA model.

## 1.6. Model 6: MAIN ARIMA Raw( <sup><</sup> )

This model uses the ARIMA model using the raw data. It can validate the performance of the neural network model by comparing with MAIN NN Raw( <sup><</sup> ).

The 118 time series data points for January 1984–October 1993 were collected for this research. The 96 data points for January 1984–December 1991 were used for training. The remaining 22 data points for January 1992–October 1993 were used for prediction. We have forecasted for two time points, one-month ahead for the operational schedule and three-months ahead for the crude oil purchase planning. The evaluation criteria adopted were Mean Squared Errors MSE , Mean Absolute Errors MAEŽ . Ž . and Mean Absolute Percentage Errors MAPE .Ž .

The neural network software package used for this experiment was UNIK-NN developed by the Intelligent Information Systems Laboratory in the Korea Advanced Institute of Science and Technology. For the learning algorithm, the standard backpropagation algorithm with a momentum term was used. For the time series analysis, SAS package was used.

The remaining sections of this paper are organized as follows. In Section 2, the judgmental adjustment process and relevant terminologies are formally defined and illustrated with a refinery example. In Section 3, the procedure of the neural network based adjustment is explained step by step. In Section 4, various comparative performance evaluations are described. Section 5 concludes this paper.

## 2. Judgmental adjustment in time series forecasting

This section formally defines the terminologies and notations for judgmental adjustment.

## 2.1. Judgmental adjustment process

The traditional time series process can be defined as Eq. 1 : Ž .

$$
\hat {Y} (t) = f \bigl (Y (t - 1), Y (t - 2), \ldots \bigr)\tag{1}
$$

where Y tŽ .<sup>y</sup>k <sup>s</sup>actual data for the period $t - k$ Ž k is a time lag , and. $\hat { Y } ( t ) =$ forecast for the period t. In contrast, the judgmentally adjusted time series process can be formally defined as Eqs. 2 and 3 :Ž . Ž .

$$
\hat {Y} _ {\mathrm{o}} (t) = f \left(Y _ {\mathrm{o}} (t - 1), Y _ {\mathrm{o}} (t - 2), \dots\right) \text { and }\tag{2}
$$

$$
\hat {Y} _ {\mathrm{a}} (t) = \hat {Y} _ {\mathrm{o}} (t) + \Delta Y (t)\tag{3}
$$

where $Y _ { \mathrm { o } } ( t - k ) = \mathrm { f i l t e r e d }$ data by eliminating the judgmental effects for the period $t - k , \hat { Y _ { \mathrm { o } } } ( t ) = \mathrm { m a i n }$ 1 trend forecast for the period t by a time series model, $\Delta \hat { Y } ( t ) =$ estimated magnitude of judgmental adjustment for the period t, and $\hat { Y } _ { \mathrm { a } } ( t ) = \mathrm { a d j u s t e d }$ forecast for the period t.

Let’s formally define the terminologies judgmental factor, judgmental eÕent, monthly judgmental instance and judgmental case.

## 2.2. Judgmental factors

Judgmental factor is defined as ‘‘a factor that cannot be fully incorporated into the time series models, and thus cannot be effectively identified by the extrapolation of past patterns in the data set’’ <sup>w</sup> <sup>x</sup> 16 .

![](/api/attachments/MWZVRA6P/fulltext/images/33e8c050c5dc9e4c465d255d242829ed2b9ae7716172f86963968277daa07f10.jpg)

The concept of judgmental factor is comparable with the notion of causality of Granger 10 . Accord-<sup>w</sup> <sup>x</sup> ing to his notion, ‘‘although a variable may affect a dependent variable, if the effect is subsumed by the past data series, the causality cannot be explicitly grasped’’. In this sense, the judgmental factors can be regarded as the factors whose effects cannot be subsumed by the past data series.

Common characteristics of judgmental factors are:

1. The factors occur irregularly and infrequently. Thus the number of data point is usually too small for statistical modelling.

2. Nevertheless, the impact is too significant to neglect.

3. The effect is transient.

4. The occurrence of coming events can be recognized in advance although it is not easy to judge their impact precisely.

For example, in the Korean refinery, whose market is under the control of governmental regulation, the demand forecasting experts judgmentally adjust the forecast from the time series model. Four typical judgmental factors that influence the gasoline demand forecasts are: 1 governmental energy saving Ž . regulations, 2 strikes of energy intensive industries,Ž . Ž . Ž . 3 special holidays, and 4 advanced price change announcements. Attributes of these judgmental factors are explained in Table 1. The impacts of the first three factors are transient as depicted in Fig. 1a. The impact of the last factor advanced price change Ž announcements transfers the demands between. be-

![](/api/attachments/MWZVRA6P/fulltext/images/b72ae46d846a31919d021ea50d87a80fc6204bec5ad1df2bfc78a26676c47c88.jpg)  
Fig. 1. The categories of judgmental factors.

T<sub>a</sub>bl<sub>e</sub> 1  
Attributes of judgmental factors for the gasoline demand forecast

<table><tr><td colspan="2">Judgmental factors</td><td rowspan="2">Attributes of judgmental factors</td><td rowspan="2">Categories of judgmental factors</td></tr><tr><td>Name</td><td>Notation</td></tr><tr><td>Regulation</td><td> $R_m(k, i, d)$ </td><td>k: regulation type, i: intensity of regulation, d: impacted duration (days)</td><td>Transient factor</td></tr><tr><td>Strike</td><td> $S_m(k, i, d)$ </td><td>k: industry type, i: intensity of strike, d: impacted duration (days)</td><td>Transient factor</td></tr><tr><td>Holiday</td><td> $H_m(k, d)$ </td><td>k: holiday type, d: impacted duration (days)</td><td>Transient factor</td></tr><tr><td>Advanced announcement</td><td> $A_m(p, t_a, t_e)$ </td><td>p: percentage of price change,  $t_a$ : announced date,  $t_e$ : effective date</td><td>Transferring factor</td></tr></table>

S<sub>u</sub>b<sub>scr</sub>i<sub>p</sub>t <sub>m</sub> d<sub>eno</sub>t<sub>es</sub> th<sub>e</sub> <sub>occurr</sub>i<sub>ng</sub> <sub>mon</sub>th.

T<sub>a</sub>bl<sub>e</sub> 2  
Illustration of judgmental events <sub>,</sub> monthly instances <sub>,</sub> and cases

<table><tr><td>Month, year</td><td>Monthly time tag</td><td>Judgmental events</td><td>Monthly judgmental instances</td><td>Judgmental cases</td><td>Judgmental case no.</td></tr><tr><td>Jul., 1988</td><td>55</td><td></td><td></td><td></td><td></td></tr><tr><td>Aug.</td><td>56</td><td></td><td></td><td></td><td></td></tr><tr><td>Sep.</td><td>57</td><td> $R_{57}(1,0.2,23), H_{57}(2,1)$ </td><td> $r_{57}(1,0.2,16), h_{57}(2,1)$ </td><td> $\{r_{57}(1,0.2,16), h_{57}(2,1), -106\}$ </td><td>Case 20</td></tr><tr><td>Oct.</td><td>58</td><td> $A_{58}(-4.7, Oct. 1, Oct. 21)$ </td><td> $r_{58}(1,0.2,7), a_{58}(4.7,9)$ </td><td> $r_{58}(1,0.2,7), a_{58}(4.7,9), -150\}$ </td><td>Case 21</td></tr><tr><td>Nov.</td><td>59</td><td></td><td> $a_{59}(-4.7,9)$ </td><td> $\{a_{59}(-4.7,9), 99\}$ </td><td>Case 22</td></tr><tr><td>Dec.</td><td>60</td><td></td><td></td><td></td><td></td></tr><tr><td>Jan., 1989</td><td>61</td><td></td><td></td><td></td><td></td></tr><tr><td>Feb.</td><td>62</td><td> $H_{62}(1,2)$ </td><td> $h_{62}(1,2)$ </td><td> $\{h_{62}(1,2), 64\}$ </td><td>Case 23</td></tr><tr><td>Mar.</td><td>63</td><td></td><td></td><td></td><td></td></tr><tr><td>Apr.</td><td>64</td><td></td><td></td><td></td><td></td></tr><tr><td>May</td><td>65</td><td></td><td></td><td></td><td></td></tr><tr><td>Jun.</td><td>66</td><td></td><td></td><td></td><td></td></tr></table>

fore and after the effective date as depicted in Fig. 1b. The magnitude of area A and B may not be precisely the same if the structural change of the main trend line is shifted significantly. However, the difference between the magnitudes is usually negligible in the refinery case.

![](/api/attachments/MWZVRA6P/fulltext/images/b9c75b0615707784df58c53058d55c9ac491af301cad66c18845b1881732dc76.jpg)  
(e) Case 5  
Fig. 2. Monthly impacted duration of transferring factor.

## 2.3. Judgmental eÕents and monthly instances

The realization of judgmental factors is judgmental eÕents. Thus a judgmental event is accompanied by its impact. In the refinery case as most monthlyŽ demand forecasting does , the duration of judgmental . factors is measured by days, while the impact should be measured by the month. When an impact encompasses more than a month, we need to partition the impact to consecutive monthly instances.

For the transient factors, the impact for a month is proportional to the effective days within the month. So the monthly instances that encompass two consecutive months can be computed by the following formula:

$$
R _ {m} (k, i, d) = r _ {m} (k, i, d _ {m}) + r _ {m + 1} (k, i, d _ {m + 1})\tag{4}
$$

$$
S _ {m} (k, i, d) = s _ {m} (k, i, d _ {m}) + s _ {m + 1} (k, i, d _ {m + 1})\tag{5}
$$

$$
H _ {m} (k, d) = h _ {m} (k, d _ {m}) + h _ {m + 1} (k, d _ {m + 1})\tag{6}
$$

where $d = d _ { m } + d _ { m + 1 } , ~ d _ { m }$ and $d _ { m + 1 }$ are the impacted duration in the months m and $m + 1$ respectively.

However, computing the monthly impact of the transferring factor needs to consider the compensation effect as depicted in Fig. 2. In the refinery case, the rough effectuated days after the effective date is similar to the interval between the announced date and effective date, and the impact of transferring event lasts at most three consecutive months: the announced month Ž . m and the following two months Ž . m<sup>q</sup>1, m<sup>q</sup>2 . The monthly impacted duration can be calculated for the following five possible situations.

Let us define the necessary notations.

p: Announced percentage of price change

$p _ { m } \colon$ Percentage of price change in the month m

$d _ { m } \colon$ Impacted duration number of days in Ž .

the month m

$t _ { \mathrm { a } } \mathrm { : }$ Announced date

$t _ { \mathrm { e } } \colon$ Effective date

lastŽ .t : Last day of the month to which the day t belongs

Case 1: The announced date, effective date and completing date of the impact are placed in the same month See Fig. 2a . In this case, the impact is fully Ž . compensated within the month without affecting the following months. So the impacted duration for each month $m , m + 1$ , and $m + 2$ is all zero.

Case 2: The announced date and effective date are placed in the month m, while the completing date of the impact is placed in the next month $m + 1$ SeeŽ Fig. 2b . In this case, the transferred impacts in the. opposite directions within the announced month can be compensated each other. The impacted duration in the months m and $m + 1$ are the same except the opposite sign of price change percentage.

Case 3: The announced date is placed in the month m while the effective date and completing date are placed in the month $m + 1$ See Fig. 2c . InŽ . this case, the transferred impacts in the opposite directions in the month $m + l$ can be compensated each other. Again, the impacted duration in the months m and $m + 1$ are the same although the impacted direction is opposite.

Case 4: The announced date occurs in the month $m ;$ the effective date occurs in the first half of the month $m + 1$ ; the completing date occurs in the month $m + 2$ See Fig. 2d . In this case, the trans- Ž . ferred impacts in the opposite directions occur in the month $m + 1$ . So the impacted duration in month m is partitioned to the months $m + 1$ and $m + 2$

Case 5: The announced date occurs in the month m; the effective date occurs in the second half of the month $m + 1 ;$ the completing the occurs in the month $m + 2$ See Fig. 2e . In this case, the transferredŽ . impacts in the opposite directions occur in the month $m + 1$ . So the impacted duration in the month $m + 2$ is partitioned to the months m and $m + 1$

The above five cases can be notationally denoted as Eqs. 7 – 12 :Ž . Ž ..

$$
\begin{array}{r l} A _ {m} (p, t _ {\mathrm{a}}, t _ {\mathrm{e}}) & = a _ {m} (p _ {m}, d _ {m}) + a _ {m + 1} (p _ {m + 1}, d _ {m + 1}) \\ & \quad + a _ {m + 2} (p _ {m + 2}, d _ {m + 2}) \end{array} \tag {7}
$$

$$
[ \text { Case   1 } ] \text { IF } (t _ {\mathrm{a}} + 2 (t _ {\mathrm{e}} - t _ {\mathrm{a}}) - 1) \leq \operatorname{last} (t _ {\mathrm{a}}),
$$

$$
\text { THEN } p _ {m} = p _ {m + 1} = p _ {m + 2} = 0,
$$

$$
d _ {m} = d _ {m + 1} = d _ {m + 2} = 0\tag{8}
$$

$$
[ \text { Case   2 } ] \text { IF } (t _ {\mathrm{a}} + 2 (t _ {\mathrm{e}} - t _ {\mathrm{a}}) - 1) > \text { last } (t _ {\mathrm{a}}),
$$

$$
\text { and } t _ {\mathrm{e}} \leq \operatorname{last} \left(t _ {\mathrm{a}}\right), \text { THEN } p _ {m} = - p, p _ {m + 1} = p,
$$

$$
p _ {m + 2} = 0,
$$

$$
\begin{array}{c} d _ {m} = d _ {m + 1} = \bigl (\text { last } (t _ {\mathrm{a}}) - t _ {\mathrm{a}} + 1 \bigr) \\ - 2 \bigl (\text { last } (t _ {\mathrm{a}}) - t _ {\mathrm{e}} + 1 \bigr), \end{array}
$$

$$
d _ {m + 2} = 0\tag{9}
$$

$$
\begin{array}{r l} & \text {[Case 3] IF last(t_{a} <  (t_{a} + 2(t_{e} - t_{a}) - 1)} \\ & \qquad \leq \text {last(t_{a})}, \text {and t_{e} >last(t_{a})}, \\ & \text {THEN p_{m} = -p, p_{m+ 1} = p, p_{m+ 2} = 0,} \\ & d _ {m} = d _ {m + 1} = \text {last(t_{a}) - t_{a} + 1, d_{m+ 2} = 0} \\ & \text {[Case 4] IF (t_{a} + 2(t_{e} - t_{a}) - 1) > last(t_{e}),} \\ & \text {and last(t_{a}) <  t_{e} \leq last(t_{a}) + 1 / 2(last(t_{e})} \\ & \qquad - \text {last(t_{a})}), \\ & \text {THEN p_{m} = -p, p_{m+ 1} = p, p_{m+ 2} = p,} \\ & d _ {m} = \text {last(t_{a}) - t_{a} + 1}, \\ & d _ {m + 1} = \text {last(t_{e}) - last(t_{a}) - 2(t_{e} - last(t_{a}) - 1)}, \\ & d _ {m + 2} = d _ {m} - d _ {m + 1} \\ & \text {[Case 5] IF (t_{a} + 2(t_{e} - t_{a}) - 1) > last(t_{e}),} \\ & \text {and (t_{e}) > last(t_{a}) + 1 / 2(last(t_{e}) - last(t_{a}))}, \\ & \text {THEN p_{m} = -p, p_{m+ 1} = -p, p_{m+ 2} = p,} \\ & d _ {m} = \text {last(t_{a}) - t_{a} + 1}, \\ & d _ {m + 1} = \text {last(t_{e}) - last(t_{a}) - 2(last(t_{e}) - t_{e} + 1)}, \\ & d _ {m + 2} = d _ {m} + d _ {m + 1} \end{array} \tag {12}
$$

Four judgmental events and six monthly judgmental instances are illustrated in the third and fourth columns of Table 2. The second column, Monthly Time Tag, is the serial number of the months that correspond to the periods July 1988–June 1989. For instance, $R _ { 5 7 } ( 1 , 0 . 2 , 2 3 )$ at September 1988 is the restriction of driving either odd or even number plated cars within Seoul during the Olympic games. This kind of regulation is classified as type 1. The intensity 0.2 is measured by multiplying the per- Ž . centage of restricted cars 0.5 by the fraction of carŽ . holding regions in the country 0.4 , and the durationŽ . is 23 days from September 15 to October 7, 1988. Since the event is overlaid over the 57th month and the 58th month, it should be partitioned into two monthly judgmental instances: $r _ { 5 7 } ( 1 , \ 0 . 2 ,$ . , 16 and $r _ { 5 8 } ( 1 , 0 . 2 , 7 )$

Another example of an event was the governmental announcement of price change Ž . <sup>y</sup>4.7% on October 1st 1988, which was supposed to be effective from October 21st. Since people expected the price to drop, they delayed buying until after October 21st. The portion of demand for October 1–20 was transferred to after October 21st as much as they can. The effect of price elasticity per se is assumed to be absorbed into the main trend for the short-term transferring period. So $A _ { 5 8 } ( - 4 . 7$ . , Oct. 1, Oct. 21 is partitioned into $a _ { 5 8 } ( 4 . 7 , 9 )$ and $a _ { 5 9 } ( - 4 . 7 , 9 )$ according to Eq. 9 . Note that the price effect for the 58thŽ . month is up by 4.7%, while for the 59th month is down by 4.7%.

## 2.4. Judgmental cases

In September 1988, a special holiday event $H _ { 5 7 } ( 2 \AA$ 1 occurred whose. $\mathrm { t y p e } = 2$ represents Thanksgiving Day. Since the impact lasted only a day, $H _ { 5 7 } ( 2$ $\begin{array} { r } { 1 ) = h _ { 5 7 } ( 2 , } \end{array}$ ., 1 . Since $r _ { 5 7 } ( 1 , \ 0 . 2$ . , 16 had happened simultaneously with $h _ { 5 7 } ( 2 , \ 1 )$ , the impact <sup>y</sup>106 is measured as the composite effect of two instances. The judgmental case is the pair of occurrences of judgmental monthly eÕents and their impact. For instance, Case 20 is the defined $\mathrm { a s } \{ r _ { 5 7 } ( 1 , ~ 0 . 2 , ~ 1 6 )$ $h _ { 5 7 } ( 2 , \ 1 ) , \ - 1 0 6 \}$ in the sixth column of Table 2. Likewise the Cases 21–23 are defined. In this manner, we have identified 37 judgmental cases for the training period from January 1984 to December 1991.

## 3. Procedure of the neural network based adjustment

In this section, a neural network based judgmental adjustment procedure for MAIN NN Filtered( <sup><</sup> ) <sup>q</sup> JUDGMENTAL NN ( ) is proposed to supplement human adjustments of forecasts. The overall procedure for the judgmental adjustment is depicted in Fig. 3. Key steps in the procedure are the following:

1. Identification of historical judgmental events.

2. Generation of monthly judgmental instances.

3. Generation of judgmental cases.

4. Generalization of judgmental cases using a neural network model.

5. Main trend forecasting using a neural network model.

6. Estimation of the effect of expected monthly judgmental instances and additive adjustment.

## 3.1. Identification of historical judgmental eÕents

Historical judgmental events can usually be identified by examining their historical records. But, when there is a risk of missing some historical judgmental events, we may examine the outliers. Outliers may be detected by the 2 or 3 criterion when the distribution is known. Otherwise, the Chebyshev inequality may be used 7 .<sup>w</sup> <sup>x</sup>

## 3.2. Generation of monthly judgmental instances

A judgmental event may affect the demand more than a time unit such as a month . However, be-Ž .

![](/api/attachments/MWZVRA6P/fulltext/images/e94e96122e7f75e5a34a33928907f2cbbc3be32a93031aeabc306aed2ebf14c8.jpg)  
Fig. 3. Neural network based main trend forecasting with a neural network based judgmental adjustment.

cause the demand is managed and predicted by the time unit, the effect of the judgmental event should be evaluated for each time unit. So the judgmental event needs to be split into relevant monthly judg mental instances as was shown in Table 2.

## 3.3. Generation of judgmental cases

To construct the judgmental cases from the monthly judgmental instances, we need to keep the monthly time tag of instances. This is because the same event at a different time may have different impact. If the impact can be computed by an external formula, the impact can be supplied accordingly. For instance, if a forecaster could obtain the information necessary to compute the impact of car regulation Žthe total number of cars affected and average daily gasoline consumption per car , she or he could com- . pute the expected amount of decreased consumption quite precisely by the following formula:

Effect<sup>s</sup>number of affected cars

)average daily gasoline consumption per car

)impacted duration.

However if such a formula is not available, the effect should be automatically computed by delineating the difference between the forecast by the main trend model and its actual value. In this case, we cannot avoid imposing the random errors of the raw data to the judgmental events. So, we had better compute the impact of judgmental event using the external formula as much as possible. Anyway once the impact is identified, the magnitude is smoothed out of the raw data generating the filtered data set. Fig. 4 shows time series plots of actual sales and filtered sales from January 1984 to December 1991 for refinery case.

## 3.4. Generalization of judgmental cases using a neural network model

The relationship between the monthly judgmental instances in a period and their impact can be generalized by adopting a neural network model as depicted in Fig. 5. The input of a neural network model corresponds to the monthly judgmental instances along with a monthly time tag, and the output corresponds to the monthly impact.

In the refinery case, we had 11 input variables and one output variable. We limited the number of hidden nodes according to the Hecht–Nielsen theorem which guaranties that the number of hidden nodes does not need to exceed $2 n + I \left( 2 * 1 1 + 1 = \right.$ 23 where. n is the number of input nodes 5 . We<sup>w</sup> <sup>x</sup> had selected even numbers of hidden nodes between one and 23 constructing the following neural net-

![](/api/attachments/MWZVRA6P/fulltext/images/e9f8c8ab37003fe77ea0da404614d4d8c1ee3b4f3abc6ac6377dab188ea1e1c4.jpg)  
Fig. 4. Time series plots of actual sales and filtered sales.

![](/api/attachments/MWZVRA6P/fulltext/images/eb920c12f8d451e96babfe1c3ee1dae8b5b0f3b90eeedb48afbb0aac993f708c.jpg)  
Fig. 5. Generalization of judgmental cases by a neural network.

work architectures of NNŽa of input nodes-a of hidden nodes-a of output nodes : NN 11-2-1 ,. Ž . NN 11-4-1 , NN 11-6-1 , NN 11-8-1 , NN 11-10-1 ,Ž . Ž . Ž . Ž . NN 11-12-1 , NN 11-14-1 , NN 11-16-1 , NN 11-Ž . Ž . Ž . Ž 18-1 , NN 11-20-1 , and NN 11-22-1 . We had tested. Ž . Ž . each neural network architecture with 300, 600, 900, and 1200 epochs in order to determine the best one. 37 judgmental cases were divided into two sets. 25 cases were used for training and 12 cases were used for testing. Sample judgmental cases for training are shown in Table 3. Through the test, the NN 11-8-Ž 1 epochs <sup><</sup> <sup>s</sup>600 had the minimum Mean Squared . Error MSE , and was therefore selected as the bestŽ . model. The model was then trained with all of 37 judgmental cases for 600 epochs. In this manner, the g e n e r a liz in g n e u r a l n e tw o r k m o d e l JUDGMENTAL NN( ) was constructed.

3.5. Main trend forecasting using a neural network model

As demonstrated in Fig. 3, the main trend can be forecasted by a neural network model using the time series data, which has filtered the impacts of the monthly judgmental instances. It is denoted as MAIN NN Filtered( )<sup><</sup> ). In the refinery case, we designed several neural network architectures to determine the best one. As input variables, we selected three input variables demands at m-1, m-2 to reflectŽ recency, and m-12 to reflect the seasonal cycle. along with the optional ones from m-3, m-4, m-5, m-6, m-7 and m-8. For the hidden nodes, we again selected even numbers of hidden nodes between 1 and 2 n<sup>q</sup>1. The designed neural network architectures and their test order are shown in Table 4.

We trained all of the neural network for 300, 600, 900, and 1200 epochs with 64 out of 96 filtered data points. Table 5 illustrates the sample data set for training. The trained neural network models were tested with the remaining 32 filtered data points. Each row of Table 6 shows the best model among the ones with the same input variables. Among the best ones, the NN 7-4-1 epochs Ž <sup><</sup> <sup>s</sup>600 was selected . as the main trend model because it had the minimum MSE. The model is retrained with the 96 filtered data points from the whole learning period. This trained model was used as MAIN NN Filtered( <sup><</sup> ) to predict the main trend forecasts.

Table 3  
Sample judgmental cases for training

<table><tr><td rowspan="2">Judgmental Cases</td><td colspan="5">Inputs</td><td>Output</td></tr><tr><td>m.</td><td>rm(k, i, dm).</td><td>sm(k, i, dm).</td><td>hm(k, dm).</td><td>am(pm, dm)</td><td>Monthly Impact</td></tr><tr><td>Case 20</td><td>(57)</td><td>(1, 0.2, 16)</td><td>(0, 0, 0)</td><td>(2, 1)</td><td>(0, 0)</td><td>-106</td></tr><tr><td>Case 21</td><td>(58)</td><td>(1, 0.2, 7)</td><td>(0, 0, 0)</td><td>(0, 0)</td><td>(4.7, 9)</td><td>-150</td></tr><tr><td>Case 22</td><td>(59)</td><td>(0, 0, 0)</td><td>(0, 0, 0)</td><td>(0, 0)</td><td>(-4.7, 9)</td><td>99</td></tr><tr><td>Case 23</td><td>(60)</td><td>(0, 0, 0)</td><td>(0, 0, 0)</td><td>(1, 2)</td><td>(0, 0)</td><td>64</td></tr></table>

Subscript m denotes monthly time tag.

Table 5 Sample data set for training  
Table 4  
Designed neural network architectures and their test order

<table><tr><td colspan="2">Input nodes</td><td rowspan="2">No. of hidden nodes</td></tr><tr><td>Number</td><td>Node&#x27;s time tag</td></tr><tr><td>3</td><td>m-1, m-2, m-12</td><td>2, 4, 6</td></tr><tr><td>4</td><td>m-1, m-2, m-3, m-12</td><td>2, 4, 6, 8</td></tr><tr><td>5</td><td>m-1, m-2, m-3, m-4, m-12</td><td>2, 4, 6, 8, 10</td></tr><tr><td>6</td><td>m-1, m-2, m-3, m-4, m-5, m-12</td><td>2, 4, 6, 8, 10, 12</td></tr><tr><td>7</td><td>m-1, m-2, m-3, m-4, m-5, m-6, m-12</td><td>2, 4, 6, 8, 10, 12, 14</td></tr><tr><td>8</td><td>m-1, m-2, m-3, m-4, m-5, m-6, m-7, m-12</td><td>2, 4, 6, 8, 10, 12, 14, 16</td></tr><tr><td>9</td><td>m-1, m-2, m-3, m-4, m-5, m-6, m-7, m-8, m-12</td><td>2, 4, 6, 8, 10, 12, 14, 16, 18</td></tr></table>

## 3.6. Estimation of the effect of expected monthly judgmental instances and additiÕe adjustment

A forecaster should identify the expected judgmental events and monthly judgmental instances to estimate their impacts on the prediction periods. Upcoming judgmental events can usually be identified through internal<sup>r</sup>external information such as news, government announcements and management policies before the event occurs. To enhance the identification of the expected judgmental events and monthly judgmental instances, a forecaster should effectively dialogue with sales staff, as well as collect and analyze relevant information. In the refinery case, for the one-month ahead prediction, there were six judgmental events as shown in Table 7 during the prediction period: $H _ { 9 8 } ( 1 , 4 ) , \ A _ { 1 0 2 } ( 2 2 . 7 ,$ , Jun. 7, Jun. 25 ,. Ž . Ž . Ž .S 1, 0.8, 21 , H 2, 4 , H 1, 3 , $H _ { 1 1 7 } ( 2 .$

<table><tr><td rowspan="2">Patterns</td><td>Inputs</td><td>Output</td></tr><tr><td>Filtered Data Set at (m-12, m-6, m-5, m-4, m-3, m-2, m-1)</td><td>Filtered Data at (m)</td></tr><tr><td></td><td></td><td></td></tr><tr><td>Pattern 55</td><td>(885, 872, 902, 1039, 1031, 1176, 1088)</td><td>1,174</td></tr><tr><td>Pattern 56</td><td>(917, 902, 1039, 1031, 1176, 1088, 1174)</td><td>1,306</td></tr><tr><td>Pattern 57</td><td>(953, 1039, 1031, 1176, 1088, 1174, 1306)</td><td>1,259</td></tr><tr><td>Pattern 58</td><td>(928, 1031, 1176, 1088, 1174, 1306, 1259)</td><td>1,257</td></tr><tr><td>Pattern 59</td><td>(908, 1176, 1088, 1174, 1306, 1259, 1257)</td><td>1,182</td></tr><tr><td>Pattern 60</td><td>(1018, 1088, 1174, 1306, 1259, 1257, 1182)</td><td>1,326</td></tr><tr><td>Pattern 61</td><td>(872, 1174, 1306, 1259, 1257, 1182, 1326)</td><td>1,204</td></tr><tr><td>Pattern 62</td><td>(902, 1306, 1259, 1257, 1182, 1326, 1204)</td><td>1,097</td></tr><tr><td>Pattern 63</td><td>(1039, 1259, 1257, 1182, 1326, 1204, 1097)</td><td>1,408</td></tr><tr><td>Pattern 64</td><td>(1301, 1257, 1182, 1326, 1204, 1097, 1408)</td><td>1,419</td></tr><tr><td>Pattern 65</td><td>(1176, 1182, 1326, 1204, 1097, 1408, 1419)</td><td>1,529</td></tr><tr><td>Pattern 66</td><td>(1088, 1326, 1204, 1097, 1408, 1419, 1529)</td><td>1,499</td></tr></table>

3 . The six judgmental events are split into seven. monthly judgmental instances: $( \boldsymbol { h } _ { 9 6 } ( 1 , \mathrm {  ~ \Omega ~ } 4 )$ $a _ { 1 0 2 } ( - 2 2 . 7 , ~ 1 2 ) , ~ a _ { 1 0 3 } ( 2 2 . 7 , ~ 1 2 ) , ~ s _ { 1 0 5 } ( 1 , ~ 0 . 8 , ~ 2 1 )$ $h _ { 1 0 5 } ( 2 , 4 ) , h _ { 1 0 9 } 1 , 3 ) , h _ { 1 1 7 } ( 2 , 3 ) )$ . Because the forecaster predicted demand for June at the end of May 1992, he could not have known the announcement of price changes that occurred on June 7, 1992. Therefore, $a _ { 1 0 2 } ( - 2 2 . 7 , 1 2 )$ on June 1992 was not considered. On the other hand for the three-months ahead prediction, as shown in Table 8, two judgmental events, $A _ { 1 0 2 } ( 2 2 . 7 ,$ ., Jun. 7, Jun. 25 and $S _ { 1 0 5 } ( 1 , 0 . 8 ,$ 21 , could not be considered because the forecaster. could not acquire information about them threemonth in advance. In other words, only the judgmental events of special holiday could have been acquired. This implies that the far advanced forecasting is more difficult in considering the judgmental events.

The effect of upcoming monthly judgmental instances can be estimated simply by inputting monthly judgmental instances and their monthly time tag into the neural network JUDGMENTAL NN( ). Such judgmental impacts are added to the main trend forecast computed by MAIN NN Filtered( <sup><</sup> ). One- and threemonths ahead forecasts by MAIN NN Filtered( <sup><</sup> ) are shown in the fifth columns of Tables 7 and 8 respectively. One- and three-months ahead forecasts by MAIN NN Filtered( <sup><</sup> ) ( ) <sup>q</sup>JUDGMENTAL NN are also shown in the seventh columns of Tables 7 and 8 respectively. Fig. 6 shows their graphical presentat i o n s r e s p e c t i v e l y . T h e e f f e c t s o f JUDGMENTAL NN( ) are summarized in Table 9. We can see that the forecasts after the adjustment have less errors in all aspects of error measurement. Note the reduced MSE by the additive judgment are 20.3% and 21.5% in one- and three-months ahead prediction models respectively.

Table 6  
The best neural network model among the ones with the same input variables

<table><tr><td>Models</td><td>MSE</td></tr><tr><td>NN(3-2-1|epochs = 300)</td><td>14,217</td></tr><tr><td>NN(4-2-1|epochs = 300)</td><td>11,631</td></tr><tr><td>NN(5-4-1|epochs = 600)</td><td>8378</td></tr><tr><td>NN(6-6-1|epochs = 600)</td><td>8102</td></tr><tr><td>NN(7-4-1|epochs = 600)</td><td>7961</td></tr><tr><td>NN(8-6-1|epochs = 600)</td><td>10,232</td></tr><tr><td>NN(9-6-1|epochs = 900)</td><td>11,529</td></tr></table>

Table 10 shows the effect of an individual judgm ental factor in M A IN N N F iltered( <sup><</sup> ) <sup>q</sup> JUDGMENTAL NN( ). For instance, when the regulation factor is eliminated from the set of the judgmental factors, the MSE for one-month ahead forecasting is increased to 7701. This means that the regulation factor’s contribution in reducing MSE was $\Delta \mathrm { M S E } =$ $7 7 0 1 - 7 4 1 8 = 2 3 8$ . In this manner, we can see that holiday effect for one-month and three-months ahead forecastings are 3535 and 5329 respectively. According to this analysis, we can notice that the holiday effect and advanced price change announcement are most critical judgmental factors in refinery case.

![](/api/attachments/MWZVRA6P/fulltext/images/3bfc7abaee65f2e0a2ab611bdb3d950070986669b70ee9d79cbf240d5f120c0c.jpg)  
Fig. 6. Actual sales and one- and three-months ahead forecasts by MAIN NN Filtered ( <sup><</sup> ) ( ) <sup>q</sup>JUDGMENTAL NN .

T<sub>a</sub>bl<sub>e</sub> 7  
One-month ahead forecasts made b<sub>y</sub> MAIN NN Filt<sub>e</sub>r<sub>e</sub>d( < ) ( ) q JUDGMENTAL NN . Prediction <sub>p</sub>eriod: Jan. 1 992–Oct. 1 993 Unit: thousand barrelsŽ .

<table><tr><td>Months</td><td>Judgmental events</td><td>Monthly judgmental instances</td><td>Raw data</td><td>Forecasts by MAIN(NN|Filtered)</td><td>Estimates by JUDGMENTAL(NN)</td><td>Forecasts by MAIN(NN|Filtered) + JUDGMENTAL(NN)</td></tr><tr><td>Jan., 1992</td><td></td><td></td><td>2609</td><td>2566</td><td></td><td>2566</td></tr><tr><td>Feb.</td><td> $H_{98}(1,4)$ </td><td> $h_{98}(1,4)$ </td><td>2479</td><td>2410</td><td>105</td><td>2515</td></tr><tr><td>Mar.</td><td></td><td></td><td>2706</td><td>2723</td><td></td><td>2723</td></tr><tr><td>Apr.</td><td></td><td></td><td>2799</td><td>2731</td><td></td><td>2731</td></tr><tr><td>May</td><td></td><td></td><td>2900</td><td>2823</td><td></td><td>2823</td></tr><tr><td>Jun.</td><td> $A_{102}(22.7,\text{ Jun. }7,\text{ Jun. }25)$ </td><td>*</td><td>3088</td><td>2950</td><td></td><td>2950</td></tr><tr><td>Jul.</td><td></td><td> $a_{103}(22.7,12)$ </td><td>2951</td><td>3044</td><td>-173</td><td>2871</td></tr><tr><td>Aug.</td><td></td><td></td><td>3205</td><td>3135</td><td></td><td>3135</td></tr><tr><td>Sep.</td><td> $S_{105}(1,0.8,21), H_{105}(2,4)$ </td><td> $s_{105}(1,0.8,21), h_{105}(2,4)$ </td><td>3095</td><td>3137</td><td>-66</td><td>3071</td></tr><tr><td>Oct.</td><td></td><td></td><td>3107</td><td>3152</td><td></td><td>3152</td></tr><tr><td>Nov.</td><td></td><td></td><td>3076</td><td>3139</td><td></td><td>3139</td></tr><tr><td>Dec.</td><td></td><td></td><td>3233</td><td>3124</td><td></td><td>3124</td></tr><tr><td>Jan., 1993</td><td> $H_{109}(1,3)$ </td><td> $h_{109}(1,3)$ </td><td>3240</td><td>3175</td><td>117</td><td>3292</td></tr><tr><td>Feb.</td><td></td><td></td><td>2920</td><td>2999</td><td></td><td>2999</td></tr><tr><td>Mar.</td><td></td><td></td><td>3295</td><td>3144</td><td></td><td>3144</td></tr><tr><td>Apr.</td><td></td><td></td><td>3314</td><td>3205</td><td></td><td>3205</td></tr><tr><td>May</td><td></td><td></td><td>3527</td><td>3378</td><td></td><td>3378</td></tr><tr><td>Jun.</td><td></td><td></td><td>3345</td><td>3426</td><td></td><td>3426</td></tr><tr><td>Jul.</td><td></td><td></td><td>3562</td><td>3587</td><td></td><td>3587</td></tr><tr><td>Aug.</td><td></td><td></td><td>3784</td><td>3655</td><td></td><td>3655</td></tr><tr><td>Sep.</td><td> $H_{117}(2,3)$ </td><td> $h_{117}(2,3)$ </td><td>3786</td><td>3587</td><td>120</td><td>3707</td></tr><tr><td>Oct.</td><td></td><td></td><td>3662</td><td>3729</td><td></td><td>3729</td></tr></table>

T<sub>a</sub>bl<sub>e</sub> 8  
Three-months ahead forecasts made b MAIN NN Filt<sub>e</sub>r<sub>e</sub>d( < ) ( )q JUDGMENTAL NN Prediction eriod: Jan 1 992–Oct 1 993 Unit: thousand barrelsŽ .

<table><tr><td>Months</td><td>Judgmental events</td><td>Monthly judgmental instances</td><td>Raw data</td><td>Forecasts by MAIN(NN|Filtered)</td><td>Estimates by JUDGMENTAL(NN)</td><td>Forecasts by MAIN(NN|Filtered) + JUDGMENTAL(NN)</td></tr><tr><td>Jan., 1992</td><td></td><td></td><td>2609</td><td>2549</td><td></td><td>2549</td></tr><tr><td>Feb.</td><td> $H_{98}(1,4)$ </td><td> $h_{98}(1,4)$ </td><td>2479</td><td>2319</td><td>105</td><td>2424</td></tr><tr><td>Mar.</td><td></td><td></td><td>2706</td><td>2585</td><td></td><td>2585</td></tr><tr><td>Apr.</td><td></td><td></td><td>2799</td><td>2742</td><td></td><td>2742</td></tr><tr><td>May</td><td></td><td></td><td>2900</td><td>2800</td><td></td><td>2800</td></tr><tr><td>Jun.</td><td>*</td><td>*</td><td>3088</td><td>2925</td><td></td><td>2925</td></tr><tr><td>Jul.</td><td></td><td>*</td><td>2951</td><td>3041</td><td></td><td>3041</td></tr><tr><td>Aug.</td><td></td><td></td><td>3205</td><td>3189</td><td></td><td>3189</td></tr><tr><td>Sep.</td><td>*,  $H_{105}(2,4)$ </td><td>*,  $h_{105}(2,4)$ </td><td>3095</td><td>3111</td><td>101</td><td>3212</td></tr><tr><td>Oct.</td><td></td><td></td><td>3107</td><td>3156</td><td></td><td>3156</td></tr><tr><td>Nov.</td><td></td><td></td><td>3076</td><td>3165</td><td></td><td>3165</td></tr><tr><td>Dec.</td><td></td><td></td><td>3233</td><td>3124</td><td></td><td>3124</td></tr><tr><td>Jan., 1993</td><td> $H_{109}(1,3)$ </td><td> $h_{109}(1,3)$ </td><td>3240</td><td>3101</td><td>117</td><td>3218</td></tr><tr><td>Feb.</td><td></td><td></td><td>2920</td><td>3005</td><td></td><td>3005</td></tr><tr><td>Mar.</td><td></td><td></td><td>3295</td><td>3118</td><td></td><td>3118</td></tr><tr><td>Apr.</td><td></td><td></td><td>3314</td><td>3229</td><td></td><td>3229</td></tr><tr><td>May</td><td></td><td></td><td>3527</td><td>3414</td><td></td><td>3414</td></tr><tr><td>Jun.</td><td></td><td></td><td>3345</td><td>3393</td><td></td><td>3393</td></tr><tr><td>Jul.</td><td></td><td></td><td>3562</td><td>3443</td><td></td><td>3443</td></tr><tr><td>Aug.</td><td></td><td></td><td>3784</td><td>3675</td><td></td><td>3675</td></tr><tr><td>Sep.</td><td> $H_{117}(2,3)$ </td><td> $h_{117}(2,3)$ </td><td>3786</td><td>3603</td><td>120</td><td>3723</td></tr><tr><td>Oct.</td><td></td><td></td><td>3662</td><td>3776</td><td></td><td>3776</td></tr></table>

## 4. Comparative performance evaluation

Now let us evaluate the performance of MAIN NN Filtered( <sup><</sup> ) ( )<sup>q</sup>JUDGMENTAL NN in comparison with other neural network architectures in Model 2–4 described in Section 1. We will also evaluate the performance of neural network models in comparison with ARIMA models of Model 5–6.

## 4.1. Comparison of neural network architectures

## 4.1.1. Hypotheses for the effects of judgmental factors

Our first concern was whether the judgmental adjustment contributed to the accuracy of forecasting. So we attempted to test the Hypothesis 1.

Hypothesis 1: Judgmental adjustment can significantly enhance forecasting accuracy.

This hypothesis can be validated by t-testing the perform ances of M A IN N N F iltered( <sup><</sup> ) <sup>q</sup> JUDGMENTAL NN( ) (vs. MAIN NN Filtered<sup><</sup> ).

Our second concern was whether the explicitly distinguished two neural networks in an additive relationship can outperform a single neural network which implicitly incorporated both the effects of the main trend and judgmental adjustment. So we tested the Hypothesis 2.

Hypothesis 2: The main trend forecasting neural network with additive adjustment of judgmental neural network outperforms the neural network trained by raw data.

This hypothesis can be validated by t-testing the perform ances of M A IN N N F iltered( <sup><</sup> ) <sup>q</sup> JUDGMENTAL NN( ) ( vs. MAIN NN Raw<sup><</sup> ).

Our next question was whether the explicitly distinguished two neural networks in an additive relationship can outperform a single neural network which explicitly incorporated both the effects of main trend and judgmental adjustment. This question is formalized as the Hypothesis 3.

Hypothesis 3: Delineating idiosyncratic patterns out of the main trend with additive adjustment outperforms the explicitly amalgamated single model.

This hypothesis was validated by the t-test of MAIN NN Filtered( <sup><</sup> ) ( ) <sup>q</sup> JUDGMENTAL NN vs. MAIN NN Filtered and Judgmental( <sup><</sup> ).

4.1.2. Additional neural networks to test the hypotheses

For testing these above hypotheses, the best models with the architectures MAIN NN Raw( <sup><</sup> ) and MAIN NN Filtered and Judgmental( <sup><</sup> ) were generated respectively.

MAIN NN Raw( <sup><</sup> ): A single neural network model using the raw data. In the refinery case, the best model for MAIN NN Raw( <sup><</sup> ) was determined by the same procedure taken for MAIN NN Filtered( <sup><</sup> ) as described in Section 3.5, except that 1000, 3000, 5000 and 7000 epochs were used. The best MAIN NN Raw( <sup><</sup> ) model has 7 input nodes m-1, m-2,Ž m-3, m-4, m-5, m-6, m-12 , 6 hidden nodes, and 1. output node with 5000 epochs of training.

MAIN NN Filtered and Judgmental( <sup><</sup> ): As noted earlier, this neural network was constructed by appending the judgmental factor as inputs to the MAIN NN Filtered ( <sup><</sup> ) model. Like the refinery case, the best model of MAIN NN Filtered and Judgmen ( <sup><</sup> - tal) is found when there are 17 input nodes, 12 hidden nodes, and one output node with 900 epochs of training.

Table 9  
Effect of judgmental model

<table><tr><td>Forecasting time</td><td>Criteria</td><td>MAIN(NN|Filtered)</td><td>MAIN(NN|Filtered) + JUDGMENTAL(NN)</td><td>Effect of JUDGMENTAL(NN)</td></tr><tr><td rowspan="3">One-month ahead</td><td>MSE</td><td>9315</td><td>7418</td><td>-1897 (-20.3%)</td></tr><tr><td>MAE</td><td>85.8</td><td>76.9</td><td>-8.9 (-10.4%)</td></tr><tr><td>MAPE</td><td>2.66</td><td>2.41</td><td>-0.25 (-9.4%)</td></tr><tr><td rowspan="3">Three-months ahead</td><td>MSE</td><td>12144</td><td>9527</td><td>-2617 (-21.5%)</td></tr><tr><td>MAE</td><td>100.1</td><td>89.1</td><td>-11.0 (-10.9%)</td></tr><tr><td>MAPE</td><td>3.17</td><td>2.82</td><td>-0.35 (-11.0%)</td></tr></table>

MSE: mean squared errors, MAE: mean absolute errors, MAPE: mean absolute percentage errors.

Table 10  
Effect of an individual judgmental factor in MAIN NN Filtered( <sup><</sup> ) ( ) <sup>q</sup>JUDGMENTAL NN

<table><tr><td rowspan="2">Eliminated judgmental factor</td><td rowspan="2">Considered judgmental factors</td><td colspan="2">One-month ahead</td><td colspan="2">Three-months ahead</td></tr><tr><td>MSE</td><td>Difference on MSE</td><td>MSE</td><td>Difference on MSE</td></tr><tr><td>Regulation</td><td>Strike, Holiday, Advanced announcement</td><td>7701 (A)</td><td>(E) - (A) = 238</td><td>9981 (a)</td><td>(e) - (a) = 454</td></tr><tr><td>Strike</td><td>Regulation, Holiday, Advanced announcement</td><td>7731 (B)</td><td>(E) - (B) = 313</td><td>10059 (b)</td><td>(e) - (b) = 532</td></tr><tr><td>Holiday</td><td>Regulation, Strike, Advanced announcement</td><td>10953 (C)</td><td>(E) - (C) = 3535</td><td>14856 (c)</td><td>(e) - (c) = 5329</td></tr><tr><td>Advanced announcement</td><td>Regulation, Strike, Holiday</td><td>8201 (D)</td><td>(E) - (D) = 783</td><td>10760 (d)</td><td>(e) - (d) = 1233</td></tr><tr><td>None</td><td>Regulation, Strike, Holiday, Advanced announcement</td><td>7418 (E)</td><td></td><td>9527 (e)</td><td></td></tr></table>

MSE: mean squared errors.

## 4.1.3. Test results

The performances of four compared models are summarized in Table 11. First of all, the ANOVA test rejected the premise that the four models are equal for one- and three-months ahead forecasts with the significance of 0.1 Ž p-values for MSE, MAE and MAPE are 0.08, 0.04 and 0.04 respectively for onemonth ahead forecasting, and 0.03, 0.03 and 0.05 respectively for three-months ahead forecasting . As . a next step to test the Hypotheses 1–3, the t-tests for one- and three-months ahead forecasts were performed. The results are shown in Tables 12 and 13, respectively. Each t-test was performed with the null hypothesis of Ho: $u _ { \mathrm { r } } \leq u _ { \mathrm { c } }$ where $u _ { \mathrm { r } }$ is true mean squared errors of the model in the row head while $u _ { \textup { c } }$ is true mean squared errors of the model in the column head of Tables 12 and 13. For example, t-test of MAIN NN Filtered( <sup><</sup> ) ( )<sup>q</sup>JUDGMENTAL NN and MAIN NN Filtered( <sup><</sup> ) on MSE was performed with the following test statistics 11,22,24 :<sup>w</sup> <sup>x</sup> t Cˆ y R.

$- ~ ( u _ { \mathrm { c } } - u _ { \mathrm { r } } ) \} / \{ S _ { \mathrm { p } } \sqrt { 1 / n _ { 1 } + 1 / n _ { 2 } } ) _ { \mathrm { m } }$ and degree of freedom $= n _ { 1 } + n _ { 2 } - 2$ where $\overline { { S _ { \mathrm { p } } ^ { 2 } } } = \{ \left( n _ { 1 } - 1 \right) \ S _ { 1 } ^ { 2 } +$ $( n _ { 2 } \mathrm { ~ - ~ } 1 ) \quad S _ { 2 } ^ { 2 } \} / ( n _ { 1 } + n _ { 2 } \mathrm { ~ - ~ } 2 ) , \overline { { \mathbb { C } } } = \mathbf { M S E }$ of MAIN NN Filtered( <sup><</sup> ) ( ) <sup>q</sup>JUDGMENTAL NN for prediction period, R<sup>s</sup>MSE of MAIN NN Filtered( <sup><</sup> ) for prediction period, $S _ { 1 }$ and $S _ { 2 }$ are standard deviations of squared errors for prediction period in MAIN NN Filtered( <sup><</sup> ) ( ) <sup>q</sup> JUDGMENTAL NN and MAIN NN Filtered ( <sup><</sup> ) respectively, and $n _ { 1 }$ and $n _ { 2 }$ are numbers of the prediction of points of MAIN NN Filtered( <sup><</sup> ) ( ) <sup>q</sup> JUDGMENTAL NN and MAIN NN Filtered( <sup><</sup> ) respectively.

According to the tests, we concluded as follows.

4.1.3.1. Judgmental adjustment can enhance forecasting accuracy. As we can see from Tables 12 and 13, p-values for MSE, MAE and MAPE are 0.22, 0.25 and 0.24 respectively for one-month ahead forecasting, 0.15, 0.21 and 0.19 respectively for threemonths ahead forecasting. According to this result, we cannot accept the Hypothesis 1 with 10% of significance, but we could find strong evidence that the judgmental adjustment is beneficial by all error measures. Even though the adjustment effect is weakly significant from the t-test’s point of view, we observed eight positive performance enhancement by adjustment out of the nine monthly judgmental adjustment. This implies that judgmental adjustment can contribute to performance enhancement of the neural network using filtered data.

Performances of MAIN NN Filtered ( <sup><</sup> ) ( ) ( <sup>q</sup> JUDGMENTAL NN , MAIN NN Filtered <sup><</sup> ) ( , MAIN NN Raw <sup><</sup> ) ( and MAIN NN Filtered and Judgmen <sup><</sup> - tal)

<table><tr><td>Forecasting time</td><td>Criteria</td><td>MAIN(NN|Filtered) + JUDGMENTAL(NN)</td><td>MAIN(NN|Filtered)</td><td>MAIN(NN|Raw)</td><td>MAIN(NN|Filtered) and Judgmental)</td></tr><tr><td rowspan="3">One-month ahead</td><td>MSE</td><td>7418</td><td>9315</td><td>12121</td><td>12592</td></tr><tr><td>MAE</td><td>76.9</td><td>85.8</td><td>102.9</td><td>105.3</td></tr><tr><td>MAPE</td><td>2.41</td><td>2.66</td><td>3.34</td><td>3.33</td></tr><tr><td rowspan="3">Three-months ahead</td><td>MSE</td><td>9527</td><td>12144</td><td>17101</td><td>17596</td></tr><tr><td>MAE</td><td>89.1</td><td>100.1</td><td>119.6</td><td>124.1</td></tr><tr><td>MAPE</td><td>2.82</td><td>3.17</td><td>3.81</td><td>3.95</td></tr></table>

Table 12  
p-Values for t-test one-month ahead Ž .

<table><tr><td></td><td>Criteria</td><td>MAIN(NN|Filtered)</td><td>MAIN(NN|Raw)</td><td>MAIN(NN|Filtered and Judgmental)</td></tr><tr><td rowspan="3">MAIN(NN|Filtered) + JUDGMENTAL(NN)</td><td>MSE</td><td>0.22</td><td>0.03**</td><td>0.01**</td></tr><tr><td>MAE</td><td>0.25</td><td>0.02**</td><td>0.01**</td></tr><tr><td>MAPE</td><td>0.24</td><td>0.01**</td><td>0.005**</td></tr><tr><td rowspan="3">MAIN(NN|Filtered)</td><td>MSE</td><td></td><td>0.17</td><td>0.11</td></tr><tr><td>MAE</td><td></td><td>0.08*</td><td>0.10*</td></tr><tr><td>MAPE</td><td></td><td>0.06*</td><td>0.04**</td></tr><tr><td rowspan="3">MAIN(NN|Raw)</td><td>MSE</td><td></td><td></td><td>0.43</td></tr><tr><td>MAE</td><td></td><td></td><td>0.44</td></tr><tr><td>MAPE</td><td></td><td></td><td>0.48</td></tr></table>

<sup>)</sup> <sup>)</sup> 5% significance level, <sup>)</sup>10% significance level.

4.1.3.2. The main trend forecasting neural network with additiÕe adjustment of judgmental neural network outperforms the neural network trained by raw data. According to the results in Tables 12 and 13, the Hypothesis 2 can be accepted with a significance of 0.05 for all criteria for two forecasting time points. Note the p-values for MSE, MAE and MAPE for one-month ahead forecasting are 0.03, 0.02 and

0.01, and those for three-months ahead forecasting are 0.01, 0.01 and 0.01.

4.1.3.3. Delineating idiosyncratic patterns out of the main trend with additiÕe adjustment outperforms the explicitly amalgamated single model. It turned out that MAIN NN Filtered( <sup><</sup> ) ( )<sup>q</sup> JUDGMENTAL NN outperforms MAIN NN Filtered and Judgmental( <sup><</sup> ) with the significance of 0.01. p-values for MSE, MAE and MAPE for one-month ahead forecasting are 0.01, 0.01 and 0.005 respectively, while 0.004, 0.005 and 0.005 respectively for three-months ahead forecasting. According to the results of experiments, we can conclude that the heterogeneous judgmental patterns should be filtered out first from the main trend. The judgmental patterns can then be grasped by another neural network and can be used for additive adjustment beneficially.

It is interesting to note that the MAIN NN Raw( <sup><</sup> )

Table 13  
p-Values for t-test three-months aheadŽ .

<table><tr><td></td><td>Criteria</td><td>MAIN(NN|Filtered)</td><td>MAIN(NN|Raw)</td><td>MAIN(NN|Filtered and Judgmental)</td></tr><tr><td rowspan="3">MAIN(NN|Filtered) + JUDGMENTAL(NN)</td><td>MSE</td><td>0.15</td><td>0.01**</td><td>0.004**</td></tr><tr><td>MAE</td><td>0.21</td><td>0.01**</td><td>0.005**</td></tr><tr><td>MAPE</td><td>0.19</td><td>0.01**</td><td>0.005**</td></tr><tr><td rowspan="3">MAIN(NN|Filtered)</td><td>MSE</td><td></td><td>0.09*</td><td>0.04**</td></tr><tr><td>MAE</td><td></td><td>0.09*</td><td>0.04**</td></tr><tr><td>MAPE</td><td></td><td>0.08*</td><td>0.04**</td></tr><tr><td rowspan="3">MAIN(NN|Raw)</td><td>MSE</td><td></td><td></td><td>0.44</td></tr><tr><td>MAE</td><td></td><td></td><td>0.39</td></tr><tr><td>MAPE</td><td></td><td></td><td>0.39</td></tr></table>

) <sup>)</sup>5% significance level, <sup>)</sup>10% significance level.

Table 14  
Performances of MAIN NN Filtered( <sup><</sup> ) ( ) ( <sup>q</sup> JUDGMENTAL NN , MAIN ARIMA Filtered<sup><</sup> ) ( ) ( <sup>q</sup> JUDGMENTAL NN , MAIN NN Raw<sup><</sup> ) and MAIN ARIMA Raw( <sup><</sup> )

<table><tr><td rowspan="2">Forecasting time</td><td rowspan="2">Criteria</td><td colspan="4">Models</td></tr><tr><td>MAIN(NN|Filtered) + JUDGMENTAL(NN)</td><td>MAIN(ARIMA|Filtered) + JUDGMENTAL(NN)</td><td>MAIN(NN|Raw)</td><td>MAIN(ARIMA|Raw)</td></tr><tr><td rowspan="3">One-month ahead</td><td>MSE</td><td>7418</td><td>9308</td><td>12121</td><td>15136</td></tr><tr><td>MAE</td><td>76.9</td><td>84.9</td><td>102.9</td><td>109.1</td></tr><tr><td>MAPE</td><td>2.41</td><td>2.74</td><td>3.34</td><td>3.54</td></tr><tr><td rowspan="3">Three-months ahead</td><td>MSE</td><td>9527</td><td>12239</td><td>17101</td><td>21237</td></tr><tr><td>MAE</td><td>89.1</td><td>98.7</td><td>119.6</td><td>126.81</td></tr><tr><td>MAPE</td><td>2.82</td><td>3.17</td><td>3.81</td><td>4.03</td></tr></table>

and MAIN NN Filtered and Judgmental( <sup><</sup> ) did not make a significant difference at all. This is because the MAIN NN Filtered and Judgmental( <sup><</sup> ) has simply distinguished the judgmental factors explicitly, while the model MAIN NN Raw( <sup><</sup> ) has implicitly kept the judgmental factors.

## 4.2. Comparison between neural network and ARIMA

Many studies have reported the superiority of neural network models over the traditional time series models 2,12,13,15,21,23 . Let us confirm<sup>w</sup> <sup>x</sup> whether this is true in the refinery case that we have worked on by comparing the neural network models with ARIMA, because ARIMA model is another useful tool for the time series forecasting See Refs.Ž <sup>w</sup> <sup>x</sup> 1,20 and further information ..

## 4.2.1. Hypothesis

Hypothesis 4: Neural network models outperform the ARIMA models.

This hypothesis can be validated by the two t-tests: MAIN NN Filtered( <sup><</sup> ) ( ) <sup>q</sup> JUDGMENTAL NN vs. MAIN ARIMA Filtered( <sup><</sup> ) ( )<sup>q</sup>JUDGMENTAL NN and MAIN NN Raw( <sup><</sup> ) (vs. MAIN ARIMA Raw<sup><</sup> ).

## 4.2.2. ARIMA model used to test the hypothesis

To test the hypothesis, MAIN ARIMA Filtered ( <sup><</sup> ) <sup>q</sup> JUDGMENTAL NN( ) ( and MAIN ARIMA Raw<sup><</sup> ) models required additional specification.

MAIN ARIMA( ) ( ) <sup>\_</sup> filtered <sup>q</sup> JUDGMENTAL NN : Since the ARIMA model is one of the most popular model for time series forecasting, we adopted it to produce main trend forecasts. This model is therefore denoted MAIN ARIMA Filtered( <sup><</sup> ). If the main trend forecasts produced by the MAIN ARIMA Filtered( <sup><</sup> ) was additively adjusted by the neural network model JUDGMENTAL NN( ), this model was denoted MAIN ARIMA Filtered( <sup><</sup> ) ( ) <sup>q</sup> JUDGMENTAL NN . Note that the JUDGMENTAL NN( ) was trained using the monthly judgmental instances filtered out by MAIN ARIMA Filtered( <sup><</sup> ). In the refinery case, the identified model MAIN ARIMA Filtered( <sup><</sup> ) with a logarithmic value of filtered data is ARIMA $( 4 , 1 , 1 ) * \left( 0 , 1 , 1 \right) _ { 1 2 }$ The best JUDGMENTAL NN( ) model had 11 input nodes, 8 hidden nodes, and one output node with 600 epochs of training.

Table 15  
p-Values for t-test one-month ahead Ž .

<table><tr><td></td><td>Criteria</td><td>MAIN(ARIMA|Filtered)+JUDGMENTAL(NN)</td><td>MAIN(NN|Raw)</td><td>MAIN(ARIMA|Raw)</td></tr><tr><td rowspan="3">MAIN(NN|Filtered)+JUDGMENTAL(NN)</td><td>MSE</td><td>0.16</td><td>0.03**</td><td>0.02**</td></tr><tr><td>MAE</td><td>0.21</td><td>0.01**</td><td>0.01**</td></tr><tr><td>MAPE</td><td>0.19</td><td>0.02**</td><td>0.01**</td></tr><tr><td rowspan="3">MAIN(ARIMA|Filtered)+JUDGMENTAL(NN)</td><td>MSE</td><td></td><td>0.15</td><td>0.06*</td></tr><tr><td>MAE</td><td></td><td>0.07*</td><td>0.06*</td></tr><tr><td>MAPE</td><td></td><td>0.11</td><td>0.06*</td></tr><tr><td rowspan="3">MAIN(NN|Raw)</td><td>MSE</td><td></td><td></td><td>0.22</td></tr><tr><td>MAE</td><td></td><td></td><td>0.32</td></tr><tr><td>MAPE</td><td></td><td></td><td>0.28</td></tr></table>

) <sup>)</sup>5% significance level, <sup>)</sup>10% significance level.

MAIN ARIMA( ) <sup>\_</sup>raw : A single ARIMA model using the raw demand series. The identified model MAIN ARIMA( ) <sup>\_</sup> Raw with logarithmic value of the ra w d a ta in th e re fin e ry c a se w a s $\mathrm { A R I M A } ( 6 , 1 , 1 ) * ( 0 , 1 , 1 ) _ { 1 2 }$

## 4.2.3. Test results

The performance of each model is summarized in Table 14. Through the t-tests of MAIN NN Filtered( <sup><</sup> ) <sup>q</sup>JUDGMENTAL NN( ) (vs. MAIN ARIMA Filtered<sup><</sup> ) <sup>q</sup> JUDGMENTAL NN( ) (and MAIN NN Raw<sup><</sup> ) vs. MAIN ARIMA Raw( <sup><</sup> ), it turned out that the neural network outperformed ARIMA as expected. As we can see from Tables 15 and 16, MAIN NN Filtered( <sup><</sup> ) <sup>q</sup> J U D G M E N T A L N N( ) o u tp e r f o r m s MAIN ARIMA Filtered( <sup><</sup> ) ( ) <sup>q</sup> JUDGMENTAL NN . p-Values for MSE, MAE and MAPE for one-month ahead forecasting were 0.16, 0.21 and 0.19 respectively, while 0.17, 0.22 and 0.21 were the p-values for three-months ahead forecasting. MAIN NN Raw( <sup><</sup> )

also outperformed MAIN ARIMA Raw( <sup><</sup> ). p-Values for MSE, MAE and MAPE for one-month ahead forecasting were 0.22, 0.32 and 0.28 respectively, while 0.22, 0.35 and 0.36 were the values for three-months ahead forecasting. The p-values were not significantly low. This implies that the key factor that influences the performance of forecasting is the architecture rather than the estimation method at least in the refinery case.

## 5. Conclusion and remarks

We have empirically validated the superiority of neural network based additive adjustment for demand forecasting. For this validation, we have compared the performance of this model with five other alternative architectures and estimation methods. At least in the refinery case, we have shown that the additive adjustment of judgmental effects on the neural network based main trend forecast could provide the best forecasts. It seems that this finding can be effective in other domains as well. We have also argued that the effect of architecture is more crucial than the estimation method.

## Acknowledgements

We would like to thank Jeong Su Hong in Yukong Company for having provided the historical data and knowledge for Korean refinery case study.

Table 16  
p-Values for t-test three-months aheadŽ .

<table><tr><td></td><td>Criteria</td><td>MAIN(ARIMA|Filtered) + JUDGMENTAL(NN)</td><td>MAIN(NN|Raw)</td><td>MAIN(ARIMA|Raw)</td></tr><tr><td rowspan="3">MAIN(NN|Filtered) + JUDGMENTAL(NN)</td><td>MSE</td><td>0.17</td><td>0.02**</td><td>0.01**</td></tr><tr><td>MAE</td><td>0.22</td><td>0.02**</td><td>0.01**</td></tr><tr><td>MAPE</td><td>0.21</td><td>0.02**</td><td>0.02**</td></tr><tr><td rowspan="3">MAIN(ARIMA|Filtered) + JUDGMENTAL(NN)</td><td>MSE</td><td></td><td>0.11</td><td>0.04**</td></tr><tr><td>MAE</td><td></td><td>0.08*</td><td>0.07*</td></tr><tr><td>MAPE</td><td></td><td>0.08*</td><td>0.08**</td></tr><tr><td rowspan="3">MAIN(NN|Raw)</td><td>MSE</td><td></td><td></td><td>0.22</td></tr><tr><td>MAE</td><td></td><td></td><td>0.35</td></tr><tr><td>MAPE</td><td></td><td></td><td>0.36</td></tr></table>

## References

<sup>w</sup> <sup>x</sup> 1 B. Box, G. Jenkins, Time Series Analysis, Forecasting and Control, Holden-Day, San Francisco, CA, 1976.

<sup>w</sup> <sup>x</sup> 2 P. Caire, G. Hatabian, C. Muller, Progress in forecasting by neural networks, IEEE Conf. Neural Networks 2 1992 .Ž .

<sup>w</sup> <sup>x</sup> 3 R.B. Chase, N.J. Aquilano, Production and Operations Management, Richard D. Irwin, 1977.

<sup>w</sup> <sup>x</sup> 4 R.H. Edmundson, M. Lawrence, M.J. O’Connor, The use of nontime series information in sales forecasting: a case study, J. Forecasting 7 1988 .Ž .

<sup>w</sup> <sup>x</sup> 5 L. Fausett, Fundamentals of Neural Networks, Prentice-Hall, 1994.

<sup>w</sup> <sup>x</sup> 6 B.E. Flores, D.L. Olson, C. Wolfe, Judgmental adjustment of forecasts: a comparison of methods, Int. J. Forecasting 7 Ž . 1991 .

<sup>w</sup> <sup>x</sup> 7 E.S. Gardner Jr., A simple method of computing prediction intervals for time series forecasts, Manage. Sci. 34 1988 . Ž .

8 D.M. Georgoff, R.G. Murdick, Manager’s Guide to Forecasting, Harvard Business Review, January–February, 1986.

<sup>w</sup> <sup>x</sup> 9 W.L. Gorr, D. Nagin, J. Szczypula, Comparative study of artificial neural network and statistical models for predicting student grade point averages, Int. J. Forecasting 10 1994 .Ž .

<sup>w</sup> <sup>x</sup> 10 C.W.J. Granger, Investigating causal relations by econometric and cross-spectral models, Econometrica 37 1969 .Ž .

<sup>w</sup> <sup>x</sup> 11 R.V. Hogg, T.C. Allen, Introduction to Mathematical Statistics, Macmillan, London, 1978.

<sup>w</sup> <sup>x</sup> 12 W.C. Jhee, J.K. Lee, Performance of Neural Networks in Managerial Forecasting, Intelligent Systems in Accounting, Finance and Management, Vol. 2 1993 .Ž .

<sup>w</sup> <sup>x</sup> 13 W.C. Jhee, K.C. Lee, J.K. Lee, A neural network approach for the identification of the box jenkins model, Network: Computation Neural Syst. 3 1992 .Ž .

<sup>w</sup> <sup>x</sup> 14 J.K. Lee, Integration and competition of AI with quantitative methods for decision support, Expert Syst. Appl. 1 4Ž . Ž . 1990 .

<sup>w</sup> <sup>x</sup> 15 J.K. Lee, W.C. Jhee, A two-stage neural network approach for ARMA model identification with ESACF, Decision Support Syst. 11 1994 . Ž .

<sup>w</sup> <sup>x</sup> 16 J.K. Lee, S.B. Oh, J.C. Shin, UNIK-FCST: Knowledge-assisted adjustment of statistical forecasts, Expert Syst. Appl.: An Int. J. 1 1990Ž .

<sup>w</sup> <sup>x</sup> 17 J.K. Lee, C.S. Yum, W.J. Kim, Neural Network Based Judgmental Adjustment for Time Series Forecasting, Proceedings of the International Conference EANN ’95 August,Ž 1995 ..

<sup>w</sup> <sup>x</sup> 18 J.S. Lim, M. O’Connor, Judgmental Adjustment of Initial Forecasts, Proceedings of the 2nd International Meeting by Decision Sciences Institute June, 1993 .Ž .

<sup>w</sup> <sup>x</sup> 19 C.N. Lu, N.T. Wu, S. Vemuri, Neural network based short term load forecasting, IEEE Trans. Power Syst. 81 1993 .Ž .

<sup>w</sup> <sup>x</sup> 20 S. Makridakis, S.C. Wheelwright, The Handbook of Forecasting: A Manager’s Guide, Wiley, Chichester, 1982.

<sup>w</sup> <sup>x</sup> 21 D.C. Park, M.A. El-Sharkawi, R.J. Marks II, Electric load forecasting using an artificial neural network, IEEE Trans. Power Syst. 6 2 1991 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 22 V.K. Rohatgi, An Introduction to Probability Theory and Mathematical Statistics, Wiley, Chichester, 1976.

<sup>w</sup> <sup>x</sup> 23 R. Sharda, R.B. Patil, A connectionist approach to time series prediction: an empirical test, J. Intelligent Manufacturing 2 1992 .Ž .

<sup>w</sup> <sup>x</sup> 24 R.E. Walpole, R.H. Myers, Probability and Statistics for Engineers and Scientists, Macmillan, London, 1978.

<sup>w</sup> <sup>x</sup> 25 R. Wilson, R. Sharda, Neural Networks, OR<sup>r</sup>MS Today Ž . August, 1992 .

<sup>w</sup> <sup>x</sup> 26 C. Wolfe, B. Flores, Judgmental adjustment of earnings forecasts, J. Forecasting 9 1990 .Ž .

![](/api/attachments/MWZVRA6P/fulltext/images/d5b4c067e2063592a47569315baf31c162fdec7b97e7570768bca0ce2713f1f2.jpg)

Jae Kyu Lee is a Professor of Management Information Systems at Korea Advanced Institute of Science and Technology. He received a B.A. from Seoul National University, an M.S. from the Korea Advanced Institute of Science and Technology and a Ph.D. from the Wharton School, University of Pennsylvania. He has authored several books on expert systems, and published numerous papers in the following journals: Management Science, Decision Support Systems, Ex-

pert Systems with Applications, Expert Systems, Decision Sciences, Fuzzy Sets and Systems, and International Journal of Man–Machine Studies. Currently, he is an editorial member of the following journals: Decision Support Systems, Expert Systems with Applications, International journal of Intelligent Systems in Accounting, Finance and Management, New Review of Applied Expert Systems, and International Journal of Information Technology.

![](/api/attachments/MWZVRA6P/fulltext/images/dcc5ea2e37df8bb1b9db43fb41f3b85c38160c71829988ea004aad7994870333.jpg)

Chang Seon Yum is a Managing Consultant of James Martin Korea, Korea. He received a B.S. from Korea University, an M.S. and Ph. D. from the Korea Advanced Institute of Science and Technology KAIST . His research interests Ž . include Expert Systems, Neural Networks, Decision Support Systems, Database Design and Artificial Intelligence applications in business.
