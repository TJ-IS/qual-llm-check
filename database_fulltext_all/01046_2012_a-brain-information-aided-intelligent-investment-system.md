---
otero_id: 1046
otero_key: "M82RXSMS"
title: "A brain information-aided intelligent investment system"
authors: "Tetsuya Shimokawa; Kanta Kinoshita; Kazuhiro Miyagawa; Tadanobu Misawa"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.05.041"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A brain information-aided intelligent investment system

Tetsuya Shimokawa <sup>a,</sup>⁎, Kanta Kinoshita <sup>b</sup>, Kazuhiro Miyagawa <sup>c</sup>, Tadanobu Misawa d

<sup>a</sup> The School of Management, Tokyo University of Science, 500, Shimokiyoku Kuki-shi Saitama, Japan

<sup>b</sup> Graduate School of Economics, Waseda University, 1-6-1, Nishiwaseda, Shinjuku-ku, Tokyo, Japan

<sup>c</sup> Graduate School of Economics, Hitotsubashi University, 2‐1, Naka, Kunitachi-shi, Tokyo, Japan

<sup>d</sup> Graduate School of Science and Engineering, University of Toyama 3190 Gofuku, Toyama 930‐8555, Japan

## a r t i c l e i n f o

Article history: Received 1 November 2010 Received in revised form 10 May 2012 Accepted 21 May 2012 Available online 30 May 2012

Keywords: Self-managed investment system Brain computer interfac Bayesian three-layer perceptron ABIC Neuroeconomics

## a b s t r a c t

Recent advancements in neuroeconomics have revealed that speci<sup>fi</sup>c sites of brain activity provide bene<sup>fi</sup>cial information regarding future risks and expected rewards. Given such advances in neuroscience, this paper studies the use of brain information in the <sup>fi</sup>nancial system. This study explores the extent to which investment performance can be improved by using brain information in investment decision making. To examine this question, we developed a self-managed investment system that selectively employs useful brain information obtained from multiple individuals. The <sup>fi</sup>ndings show the validity of brain information. Our system accomplishes superior performances of the investments based on a typical portfolio selection model and <sup>fi</sup>- nancial time-series models. The results of this study indicate the possibility of applying brain information to the <sup>fi</sup>eld of <sup>fi</sup>nance.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Recent advancements in neuroeconomics have revealed that specific sites of brain activity provide bene<sup>fi</sup>cial information regarding future risks and expected rewards. In light of these developments in neuroeconomics, this paper explores the possibility of improving an investment system with brain information regarding investment behavior. In general, good traders may have better awareness of crises in markets than poor traders. Lo and Repin [13] reported <sup>fi</sup>nding a disparity between experienced and inexperienced traders in their physiological responses to market conditions. According to their study, experienced traders were able to selectively react to market events that carry risk, such as the increased volatility of market prices and changes in trends, while inexperienced traders were unable to do so.

Lohrenz et al. [15] examined the relationship between changes in market prices and brain responses and found that <sup>fi</sup>ctive learning signals (<sup>fi</sup>ctive error) are closely associated with investment behavior and functional imaging of the dopaminergic system using fMRI. In addition, Shimokawa et al. [20,21] found that brain information from investors (changes in the Hb concentration in cerebral blood in the dorsolateral prefrontal area and the medial and lateral orbital frontal cortices) corresponded to the investors' market price forecasts, such as trends and risks. The precision of predicting investment behavior would be substantially improved using the aforementioned brain information as a factor. These studies have provided the following <sup>fi</sup>ndings. First, there are individual differences, but some traders react better to market conditions. Second, that response may be apparent in the form of brain information.

These <sup>fi</sup>ndings naturally lead to the following question: can the investment performance of a system be improved dramatically by selectively incorporating only brain information from investors who have appropriate expectations regarding market prices, i.e. good traders, in that system? This study intends to investigate that question.<sup>2</sup>

<sup>1</sup> We would observe emotional aspects or intuitions of traders, which are expected to somewhat affect market behavior and therefore might be useful for predicting future market price, The reason why we focus on brain data is that it is considered to better reflect on emotional aspects: for example. the activity of the orbital cortex would express some kind of stress, and the activity of the dorsolateral prefrontal cortex would represent reward expectations. Our system sequentially compares market price and brain data observed from each portion of the brain of each trader and statistically detects which brain data is useful for future price prediction and optimal investment strategy. The brain data that provides useful data is used as a factor for modeling optimal investment strategy, and a pattern recognition technique <sup>fi</sup>nds an optimal relationship between brain data and future market price

2 Developments of behavioral economics and neuro-economics during the past two decades have offered new insights into the cognitive and psychological aspects of economic decision-making. In response to this trend, there are some attempts to develop decision support systems which take the psychological aspects into account [7,8,12,22]. In this study, we intend to apply <sup>fi</sup>ndings in neuro-economics to decision support system.

![](/api/attachments/M82RXSMS/fulltext/images/1c43f2262348e885bbe8588493e29588d6d74af4ecd3349c28f83d05ec52f7f4.jpg)  
Fig. 1. The system overview. Our system consists of ‘the brain measurement and the real-time processing component’, ‘the return prediction component’ and ‘the investment determine model component’. The brain measurement and real-time processing component measures brain information and its real-time noise processing; the return prediction component conducts market forecasts that follow past price data; and the investment determine model component determines the most appropriate investment rate using brain information and market forecast data obtained from the brain measurement and real-time processing component and the return prediction component.

## 2. Method

## 2.1. System overview

To resolve this question, this study developed a self-managed investment system to predict by using brain information in real‐time.

In this system, subsequent market price forecasts and investment rates are optimized by learning, and brain information is used to determine the optimal investment rate. If, for example, an investor's extreme alarm at the future of the market could be observed based on brain information, then the system could automatically lower his or her investment rate (Fig. 1).

By improving accuracy in the predicting system, the collected brain information can be used as supporting data for each investor. In addition, sharing brain information of speci<sup>fi</sup>c traders who belong to an investment group/company with interested parties can improve the performance of the investment group. For example, procuring brain information regarding a competent trader's ability to discern market conditions could provide valid data for price forecasts.

Brain information from multiple investors in the market would be measured simultaneously. The measured brain information would be transferred to the system almost in real-time, i.e. every 0.17 s, and then <sup>fi</sup>ltered to remove periodic <sup>fl</sup>uctuations speci<sup>fi</sup>c to the body. Useful brain information from all of the brain information sent to the system would be successively selected and re<sup>fl</sup>ected to an extent in the determination of investment rates (Section 2.2).<sup>3</sup>

Three-layer perceptrons were used as a basis function to represent a model for determining investment rates. Potential factors were the predicted rate of return and data on the Hb concentration in blood at individual sites from individual subjects (Sections 2.3 and 2.4). Individual parameters for the three-layer perceptrons were successively estimated by hierarchical Bayesian estimation, and Akaike's Bayesian Information Criterion (ABIC) was used to select brain information of use in determining the optimal amount of investing. Use of this criterion allows selection of an optimal model that also takes into account the potential for over-<sup>fi</sup>tting due to an increase in the number of factors. The teaching signal used in supervised learning is, in this instance, the optimal amount of investing. If a portfolio's actual rate of return is positive, the investment rate is 2, and if that rate is negative, then the investment rate is −2. That said, the computation space for this work was limited, so the number of hidden units in the three-layer perceptron was set to three.

Functional near-infrared spectroscopy (fNIRS) was used to measure brain information. fNIRS has several advantages in that the equipment used is compact and less restrictive to subjects, it is noninvasive since it uses light, and it provides good temporal resolution (on the order of several dozen ms) [11]. These attributes represent not simply the major bene<sup>fi</sup>ts of using fNIRS in practice but are also crucial to the veri<sup>fi</sup>cation work done in this study. In other words, the equipment is compact, allowing simultaneous measurement of information from multiple traders in realtime. The equipment also allows the speci<sup>fi</sup>c selection of useful information from a large-scale sample of brain information. From these advantages, some researches that use fNIRS to analyze economic decision makings have been published recently ([21] in <sup>fi</sup>nancial decision making under uncertainty, and [16,19] in preference decision making). This study intends to apply the <sup>fi</sup>ndings in [21] to fNIRSbased <sup>fi</sup>nancial decision support system.

Table 1 Factor candidates in price prediction.

<table><tr><td>Factor</td></tr><tr><td>Rate of return 1 period prior</td></tr><tr><td>Rate of return 2 period prior</td></tr><tr><td>Moving average of prior returns (10 terms)</td></tr><tr><td>TOPIX return 1 period prior</td></tr><tr><td>Exchange rate (dollar-yen) 1 period prior</td></tr><tr><td>S&amp;P 500 return 1 period prior</td></tr></table>

![](/api/attachments/M82RXSMS/fulltext/images/8184e5f4be42b4a3622b6be3090de8cfb8d696f47861441de072c8ea0d9af17e.jpg)  
Fig. 2. Optimal investment model. Any decision regarding the most appropriate investment rate is based on brain information and market price forecasts using the market price sequence The three-layer perceptron is used as a basis function to represent a model for determining investments. Data used in this study are selected by the hyperparameter marginal likelihood

## 2.2. Brain measurement and real-time processing

This experiment measured changes in the concentrations of oxygenated hemoglobin (oxyHb) and deoxygenated hemoglobin (deoxyHb) during task performance using the fNIRStation from Shimadzu Corporation.<sup>4</sup> The 10–20 system was used for electrode placement. In light of previous studies, the following analysis focused on 2 areas: the dorsolateral prefrontal cortex (DLPFC), which is believed to better re<sup>fl</sup>ect the activity of the reward system [4,10]; the orbital frontal cortex (OFC) [6,17,18].

Brain information measured by fNIRS was transferred in the system in real-time and <sup>fi</sup>ltered in order to remove periodic <sup>fl</sup>uctuations speci<sup>fi</sup>c to the body. The <sup>fi</sup>ltering technique used was a low-pass <sup>fi</sup>lter that <sup>fi</sup>lters high-frequency signals via a Fourier transform. A <sup>fi</sup>lter via a fast Fourier transform was sequentially applied. For most subjects, the frequency that served as the threshold value was 0.6 Hz. This corresponds to the frequency of noise due to blood circulation.

## 2.3. Prediction of the rate of return

Factors thought to be related to market price formation served as factors for prediction of the subsequent rate of return. Prediction was done with a portfolio of top ten stocks in terms of the Sharpe ratio selected from the Nikkei 225 stocks. Such a portfolio was considered in order to provide consistent system operations with increased predictability. Table 1 shows the potential predictive factors of the portfolio's rate of return that were taken into account in this study. These factors are frequently focused upon in the <sup>fi</sup>eld of asset price predictability. Three-layer perceptrons served as a basis function for a predictive model, and model parameters and the optimal weights of stocks incorporated in the portfolio were speci<sup>fi</sup>ed by hierarchical Bayesian estimation. Moreover, factors that signi<sup>fi</sup>cantly affect prediction of the rate of return were identi<sup>fi</sup>ed using ABIC.

![](/api/attachments/M82RXSMS/fulltext/images/8718bc33e3f55c7db0ae336221488f38aaab227e147b8f41dcb0e5407bb59a85.jpg)  
Fig. 3. The three-layer perceptron. The three-layer perceptron is used as a basis function to represent a model for determining investment; n represents predictive variables, and h indicates the number of hidden units. In theory, increasing the number of h can approximate all types of continuous functions. The most appropriate decision making regarding investment is thought to depend on the complex relations between the explanatory variables. However, using the three-layer perceptron as a basis function makes it possible to capture such a nonlinear relationship. Model parameters are determined by Bayesian learning

## 2.4. Determination of the amount of investment

To provide a model for determining the amount of investment, a model to determine the optimal amount of investing was created with Bayesian three-layer perceptrons using the portfolio's predicted rate of return and brain information mentioned above as factors (Figs. 2 and 3). Tables 2 and 3 show the potential factors. Refer to the Appendix for details about the three-layer perceptron and hierarchical Bayesian estimation relating to the parameter and model selection.<sup>5</sup>

## 3. Experiment

The experimental setup and sites for measurement of brain information are shown in Fig. 4. Based on <sup>fi</sup>ndings from previous studies and given the constraints of fNIRS, the brain information measurement sites were the dorsolateral prefrontal cortex (DLPFC) and the orbital frontal cortex (OFC) [4,6,10,17,18,21]. Details on the investment experiment conducted here are as follows. Subjects (market participants) were a maximum of four healthy adults in each session; adults were of both sexes and ages 18 to 24. In all of the sessions, there were 80 participants. Of the subjects, 33 had investment experience (28 males, 5 females).

Table 2  
Factor candidates of the three-layer perceptron model. This is a combination of factors representing potentially predictive variables for the optimal investment model explored by this study.

<table><tr><td>Factor</td></tr><tr><td>Previous explained variable (auto-correlation term)</td></tr><tr><td>oxyHb at DLPFC (subject 1)</td></tr><tr><td>oxyHb at DLPFC (subject 2)</td></tr><tr><td>oxyHb at DLPFC (subject 3)</td></tr><tr><td>oxyHb at DLPFC (subject 4)</td></tr><tr><td>oxyHb at DLPFC (average for subjects)</td></tr><tr><td>oxyHb at OFC (subject 1)</td></tr><tr><td>oxyHb at OFC (subject 2)</td></tr><tr><td>oxyHb at OFC (subject 3)</td></tr><tr><td>oxyHb at OFC (subject 4)</td></tr><tr><td>oxyHb at OFC (average for subjects)</td></tr></table>

Table 3  
The factor set candidates.

<table><tr><td>ID</td><td>Factor set</td></tr><tr><td>FS1</td><td>Auto-correlation term (the benchmark)</td></tr><tr><td>FS2</td><td>Auto-correlation term, oxyHb at DLPFC (subject 1)</td></tr><tr><td>FS3</td><td>Auto-correlation term, oxyHb at DLPFC (subject 2)</td></tr><tr><td>FS4</td><td>Auto-correlation term, oxyHb at DLPFC (subject 3)</td></tr><tr><td>FS5</td><td>Auto-correlation term, oxyHb at DLPFC (subject 4)</td></tr><tr><td>FS6</td><td>Auto-correlation term, oxyHb at OFC (subject 1)</td></tr><tr><td>FS7</td><td>Auto-correlation term, oxyHb at OFC (subject 2)</td></tr><tr><td>FS8</td><td>Auto-correlation term, oxyHb at OFC (subject 3)</td></tr><tr><td>FS9</td><td>Auto-correlation term, oxyHb at OFC (subject 4)</td></tr><tr><td>FS10</td><td>Auto-correlation term, oxyHb at DLPFC (average for subjects)</td></tr><tr><td>FS11</td><td>Auto-correlation term, oxyHb at OFC (average for subjects)</td></tr><tr><td>FS12</td><td>Auto-correlation term, oxyHb at DLPFC (subjects 1, 2, 3, 4)</td></tr><tr><td>FS13</td><td>Auto-correlation term, oxyHb at OFC (subjects 1, 2, 3, 4)</td></tr><tr><td>FS14</td><td>Auto-correlation term, oxyHb at DLPFC and OFC (subjects 1, 2, 3, 4)</td></tr><tr><td>FS15</td><td>Auto-correlation term, oxyHb at DLPFC and OFC (average for subjects)</td></tr></table>

Subjects (market participants) were shown a chart of their portfolio value, their current investment rate, and a chart indicating the market index (here, TOPIX and the US dollar–yen exchange rate).

To give an incentive, the subjects participate in a virtual investment. The investment can specify the limit price and the size of order. However, the market price isn't formed endogenously from their order. The market price sequence is exogenously given from the actual market data.

The screen was updated 100 times in 1-second intervals. These steps constituted 1 session, and a total of 20 sessions provided a total sample size of 8000 (20 sessions×4 individuals×100 periods). The data on the series of prices used were daily data on the Nikkei 225 stocks from July 1, 2008 to June 30, 2009. Batches of 10 of the Nikkei 225 stocks were randomly selected for use in each session. Table 4 shows the stock data.

## 4. Market price prediction and brain information

To start with, whether measured brain information really provides useful information with regard to the prediction of market prices, or at least if there are some individuals who could provide such brain information, was determined. fNIRS has the advantages of using compact and non-restrictive equipment, but compared to fMRI it has dif<sup>fi</sup>culty measuring areas deep inside the brain (less than 30 mm from the surface of the scalp) and low spatial resolution (about 25 mm while fMRI offers resolution of several mm), so the issue of whether brain information associated with prediction and risk can be correctly collected must be meticulously examined.

Panel 1 in Fig. 5 shows changes in the Hb concentration in blood and value changes (observed changes in the value of the subjects' portfolios) for 3 subjects when plotted over time. What is apparent from the <sup>fi</sup>gure is the similarity between changes in the Hb concentration in blood in the dorsolateral prefrontal area and value changes; also apparent is the negative response to risk (and particularly a major market event like a crash) as indicated by changes in the Hb concentration in blood in the lateral orbital frontal cortex. What can be ascertained from the <sup>fi</sup>gure is that changes in the dorsolateral prefrontal area follow the expected utility hypothesis, and changes in the lateral orbital frontal cortex also appear to be in response to large <sup>fl</sup>uctuations. An extremely interesting fact is that the Hb concentration in blood frequently changes prior to a major <sup>fl</sup>uctuation. This may be because subjects anticipate trends and risks. If this information is used appropriately, then the ef<sup>fi</sup>ciency of the investment system can probably be improved.

Panel 2 in Fig. 5 shows the correlations over time between market price changes and changes in the Hb concentration in blood in the dorsolateral prefrontal area of two representative subjects. As expected, there is a positive correlation with trends. These <sup>fi</sup>gures indicate that in situations like a rise or crash in volatility or changes in trends, there are users who can predict and react to those situations to an extent. The <sup>fi</sup>gures also indicate that this behavior can be observed as changes in the Hb concentration in blood.

![](/api/attachments/M82RXSMS/fulltext/images/2ae22b0ff440e35135c280aef175fc1e3cbe0410c54dfbe450862947dbaad93b.jpg)  
Fig. 4. Experimental setup (panel 1) and probe (panel 2). Panel 1 shows the experimental setup that simultaneously measures four individuals. Panel 2 indicates the brain regions on which this study focuses. The upper section represents the dorsolateral prefrontal cortex (DLPFC) and the lower section shows the orbital frontal cortex (OFC).

Table 4 Stock data.

<table><tr><td>Session</td><td>Start</td><td>End</td></tr><tr><td>1</td><td>November 22, 2006</td><td>April 19, 2007</td></tr><tr><td>2</td><td>July 10, 2008</td><td>December 4, 2008</td></tr><tr><td>3</td><td>February 15, 2008</td><td>July 9, 2008</td></tr><tr><td>4</td><td>July 10, 2008</td><td>December 4, 2008</td></tr><tr><td>5</td><td>November 22, 2006</td><td>April 19, 2007</td></tr><tr><td>6</td><td>July 10, 2008</td><td>December 4, 2008</td></tr><tr><td>7</td><td>July 10, 2008</td><td>December 4, 2008</td></tr><tr><td>8</td><td>February 15, 2008</td><td>July 9, 2008</td></tr><tr><td>9</td><td>November 22, 2006</td><td>April 19, 2007</td></tr><tr><td>10</td><td>February 15, 2008</td><td>July 9, 2008</td></tr><tr><td>11</td><td>February 15, 2008</td><td>July 9, 2008</td></tr><tr><td>12</td><td>February 15, 2008</td><td>July 9, 2008</td></tr><tr><td>13</td><td>February 15, 2008</td><td>July 9, 2008</td></tr><tr><td>14</td><td>November 22, 2006</td><td>April 19, 2007</td></tr><tr><td>15</td><td>November 22, 2006</td><td>April 19, 2007</td></tr><tr><td>16</td><td>November 22, 2006</td><td>April 19, 2007</td></tr><tr><td>17</td><td>July 10, 2008</td><td>December 4, 2008</td></tr><tr><td>18</td><td>July 10, 2008</td><td>December 4, 2008</td></tr><tr><td>19</td><td>December 5, 2008</td><td>May 8, 2009</td></tr><tr><td>20</td><td>July 10, 2008</td><td>December 4, 2008</td></tr></table>

Panel 3 in Fig. 5 shows a histogram of the extent of improvement based on predictions using an autocorrelation term alone in increments of ABIC when changes in the Hb concentration in blood are added as a predictive variable to price forecasts. Thus, statistical veri<sup>fi</sup>cation using

ABIC indicates that in almost all of the sessions, using some form of brain information, results in signi<sup>fi</sup>cantly better price prediction than the use of an autocorrelation term alone.

## 5. Main results: optimal investment system using brain information

Taking these <sup>fi</sup>ndings in Section 4 into account, this study next constructed an optimal investment model using subjects' brain data and determined whether or not brain information could improve the performance of the investment system. Twenty sessions were randomly chosen; in each session, the <sup>fi</sup>rst 80 periods served as a learning stage. Signi<sup>fi</sup>cant factors were selected and parameters were learned. The remaining 20 periods served as the veri<sup>fi</sup>cation stage; in this stage, factors were <sup>fi</sup>xed and parameters were sequentially learned. In the selection of useful factors, potential factors were from a set of 11 types of factors consisting of the portfolio's anticipated rate of return and brain responses from individual subjects. Tables 2 and 3 show the potential factors of the investment models. This selection process included instances where no brain information whatsoever was used, i.e. the only factor was the portfolio's anticipated rate of return.

## 5.1. Optimal model selected by ABIC

If cerebral blood <sup>fl</sup>ow fails to provide some form of information to help determine the optimal investment rate, the factor set selected with the information criterion in many instances will be the predicted rate of return. If there are subjects (or sites) that provide some form of information, then these subjects/sites may be chosen as signi<sup>fi</sup>cant factors.

![](/api/attachments/M82RXSMS/fulltext/images/7009d75d734742143d1939477bc1089e01eb4f9dfb6e5aee41c01714ea9122f7.jpg)

![](/api/attachments/M82RXSMS/fulltext/images/aa039734023427a063f0660a9c62663067ad0e723ccbace28e9cd7bd38778c7f.jpg)  
Fig. 5. Panel 1: market event. The top <sup>fi</sup>gure shows price changes, the middle <sup>fi</sup>gure shows the Hb concentration in blood in the dorsolateral prefrontal area, and the bottom <sup>fi</sup>gure shows changes in the Hb concentration in blood in the lateral orbital frontal cortex, The horizontal axis indicates periods. It is especially apparent that changes in the DLPFC activation have a close correlation with changes in the price sequence. In addition, the OFC tends to respond inversely to changes in the price sequence. This can be interpreted as in vestors' caution or stress, Panel 2: Time-correlations. The vertical axis indicates the coefficient of correlation over time and the horizontal axis indicates the time lag. A greater positive time lag indicates a lag prior to changes in the Hb concentration in blood. The <sup>fi</sup>gure indicates the correlation between the deviation from the moving average (10 periods) as represented by price trends and changes in the Hb concentration in blood in the dorsolateral prefrontal area. Therefore, the DLPFC activation of these individuals could provid useful information for market fluctuation forecasts. Panel 3: ABIC in price prediction The vertical axis indicates the pumber of sessions, and the horizontal axis indicates the extent of improvement in the predictive model in relation to differences in ABIC. The predicted variable was the market price after 1 period. In addition to the autocorrelation term for th market price, changes in the Hb concentration in cerebral blood at individual sites of individual subiects served as predictive variables. An optimal model was selected on the basis of ABIC The percent improvement was calculated as the difference of ABIC in the optimal predictive model and ABiC in the predictive model using only an autocorrelation term fot the market price, A larger ABIC indicates better price prediction accuracy, In other words, this finding indicates that brain information contains information for price prediction

The histgram of ABIC improvement (Investment model)  
![](/api/attachments/M82RXSMS/fulltext/images/74c34c13428d1f061f8271cdbfe60c2478114133afff617b98be741ee0bb91fc.jpg)  
Fig. 6. ABIC of the three-layer perceptron model. This <sup>fi</sup>gure is a histogram of the extent of improvement in ABIC by the optimal investment model. Use of the forecast rate of return as a predictive variable and no use of brain information whatsoever served as a benchmark. Speci<sup>fi</sup>cally, the values in column 3 of Table 5 minus those in column 4 were graphed. A larger ABIC indicates a better <sup>fi</sup>t with investment models. This suggests that brain information contains some kind of information for price prediction. (Tables 5 and 3 show the types of brain information that are useful at each experimental session).

As a result of model selection based on ABIC using the learning stage data (80 periods), a factor set that included some form of brain information was chosen for 19 of 20 sessions. In other words, in many of the sessions brain information from at least one investor was found to provide information of use in optimal investing. Fig. 6 and Table 5 provide the result.

## 5.2. Comparison with the portfolio selection model

Fig. 7 indicates the investment performance of the system. The ef-<sup>fi</sup>cient frontier, indicated by the blue line, was derived by a traditional form of the Markowitzian process based on the top 10 stocks used in the portfolio during the session, in which the expected rate of return and covariance of the rate of return were derived from historical data on the series of stock prices.

As is apparent from these <sup>fi</sup>gures in Fig. 7, a combination of the expected rate of return and risk provided by the investment system using brain information resulted in a frontier positioned to the upper left of the ef<sup>fi</sup>cient frontier derived from past price information alone, indicating that our model was clearly better than the typical portfolio selection model. In actuality, the system's rate of return was positioned to the upper left of the capital market line when the risk-free interest rate was 0 in more than 14 of 20 sessions.<sup>6,7</sup>

## 5.3. Predictive test: comparison with financial time-series models

Fixing the selected factor set and performing sequential forecasting for the remaining 20 periods, were found to result in a system performance that was clearly better than that with several benchmarks. Respective results are shown in Fig. 8 (left, center, and right) and Table 6.

## 5.3.1. Portfolio selection model

The historical average rate of return (daily, in units of basis points) was used as bases to measure performance. To start with, comparing the forecast rate of return alone as a factor to benchmarks revealed an improvement of 5.28 basis points (per daily) in the average rate of return in sessions on-average. Improvement in the rate of return was noted in 20 of 20 sessions.

## 5.3.2. ARMA–GARCH model

In addition, comparison of investment performance was also done using an ARMA–GARCH model, a model typically used in the <sup>fi</sup>eld of <sup>fi</sup>- nancial statistics, as a benchmark. This comparison revealed an improvement of 33.67 basis points (per daily) in the average rate of return in sessions on-average. Improvement in the rate of return was noted in 17 of 20 sessions where the ARMA–GARCH model here was an optimal model chosen with Akaike's Information Criteria (AIC) based on maximum likelihood estimation determined with the learning stage sample. In addition, investment in the ARMA–GARCH model was done using the forecast rate of return according to the ARMA–GARCH model. If the anticipated rate of return were positive, the investment rate would be 1, and if it were negative that rate would be 0.<sup>8</sup>

## 5.3.3. Market index

Moreover, comparison using TOPIX's rate of return as a benchmark also indicated an improvement of 4.22 basis points in the average rate of return in sessions on-average. Improvement in the rate of return was noted in 16 of 20 sessions.

## 6. Discussion

Why did the inclusion of brain information allow improved investment performance? According to the ef<sup>fi</sup>cient market hypothesis in <sup>fi</sup>nancial theory, investment performance above the market average cannot be expected without some form of prioritizing of information. The current results indicate that selective use of brain information provides risk information compared with information provided from the market only.<sup>9</sup> There are several possible reasons for this.

Table 5  
ABIC of the three-layer perceptron model. This table indicates the set of predictive variables chosen for each session on the basis of ABIC in an optimal investment model (column 2) as well as ABIC in the optimal model (column 3) and ABIC when only the forecast rate of return served as a predictive variable and no brain information whatsoever was used (column 4). The number of the set of predictive variables (column 2) is shown in Table 3.

<table><tr><td>Session</td><td>Factor set</td><td>ABIC</td><td>ABIC (FS1)</td><td>ABIC improvement</td></tr><tr><td>1</td><td>FS 12</td><td>-169.82</td><td>-170.99</td><td>1.17</td></tr><tr><td>2</td><td>FS 10</td><td>-169.86</td><td>-170.71</td><td>0.85</td></tr><tr><td>3</td><td>FS 3</td><td>-168.77</td><td>-169.15</td><td>0.39</td></tr><tr><td>4</td><td>FS 14</td><td>-170.59</td><td>-173.67</td><td>3.08</td></tr><tr><td>5</td><td>FS 13</td><td>-169.14</td><td>-170.74</td><td>1.59</td></tr><tr><td>6</td><td>FS 13</td><td>-169.69</td><td>-170.05</td><td>0.36</td></tr><tr><td>7</td><td>FS 8</td><td>-168.49</td><td>-169.33</td><td>0.84</td></tr><tr><td>8</td><td>FS 10</td><td>-166.34</td><td>-174.07</td><td>7.73</td></tr><tr><td>9</td><td>FS 13</td><td>-169.99</td><td>-171.78</td><td>1.79</td></tr><tr><td>10</td><td>FS 10</td><td>-169.76</td><td>-169.96</td><td>0.20</td></tr><tr><td>11</td><td>FS 1</td><td>-168.81</td><td>-168.81</td><td>0.00</td></tr><tr><td>12</td><td>FS 11</td><td>-169.09</td><td>-171.01</td><td>1.92</td></tr><tr><td>13</td><td>FS 7</td><td>-168.62</td><td>-168.73</td><td>0.12</td></tr><tr><td>14</td><td>FS 9</td><td>-169.34</td><td>-176.88</td><td>7.54</td></tr><tr><td>15</td><td>FS 5</td><td>-169.08</td><td>-170.51</td><td>1.43</td></tr><tr><td>16</td><td>FS 13</td><td>-169.28</td><td>-184.93</td><td>15.65</td></tr><tr><td>17</td><td>FS 5</td><td>-167.33</td><td>-169.26</td><td>1.93</td></tr><tr><td>18</td><td>FS 11</td><td>-166.93</td><td>-169.41</td><td>2.48</td></tr><tr><td>19</td><td>FS 5</td><td>-169.28</td><td>-170.24</td><td>0.96</td></tr><tr><td>20</td><td>FS 5</td><td>-167.95</td><td>-168.79</td><td>0.84</td></tr></table>

First, it is because of the system's selectivity. The current system does not use all brain information. Activation of several sites in the brain in numerous traders connected to the system provides information. Moreover, only information which improves investment rate was selected statistically. Thus, if there were a trader with reasonable expectations of prices, even if it were only one individual, using that individual's brain information can improve investment ef<sup>fi</sup>ciency. Human decision-making obviously has substantial bias [1,5,13], so brain information is anticipated to include a great deal of unhelpful information. If a trader's decision-making bias is systematic, then that bias could conversely serve as useful information.

Second, brain information has previously been noted to potentially allow re<sup>fi</sup>nement of the indices related to the predictability of given market prices. Market prices are known to be predictable in certain circumstances. Examples include mean-reverting market prices and the existence of autocorrelation as a result of the disposition effect, but in general these circumstances are measured by indices like price deviation from the moving average and paper pro<sup>fi</sup>t and loss of investors. Nevertheless, if that predictability is the result of decisionmaking bias due to investor psychology, then using brain information together with these indices is sure to allow more accurate discernment of predictable circumstances. As an example, if a trader fears the risk of a crash due to deviation of market prices from the moving average or he feels stressed by a greater paper loss, then these emotions may be evidenced by brain information. Lo and Repin [13] reported changes in a trader's biological responses with deviation from the moving average and changes in trends.

Third, brain information may include information that is dif<sup>fi</sup>cult to quantify and thus dif<sup>fi</sup>cult to adequately take into account in a system, such as the atmosphere of a situation, experience, or fear of an impending crash. If seasoned traders in particular used such a system, this tendency (to include hard-to-quantify information) would probably be even more pronounced.

![](/api/attachments/M82RXSMS/fulltext/images/7780ed077c05ed9cc2d5577bda5193ff4f91225463cdc220010474a40b82bbc4.jpg)

![](/api/attachments/M82RXSMS/fulltext/images/7f81b2cd4fc5d8d140c6e1760cad3bd09c940751b721be7895afd70172a0490f.jpg)

![](/api/attachments/M82RXSMS/fulltext/images/83fbc7a671235c1d9b37f39bab851f3730a9c8f9c3af181c703f6af78682052e.jpg)

![](/api/attachments/M82RXSMS/fulltext/images/b06757c20287779b634581759bacfb3b41641ae50e33bf3ff72a02be2ce47452.jpg)

![](/api/attachments/M82RXSMS/fulltext/images/15098b53cd2e50451d5914e2e88d6e67ea65f7dab1526508be6121fda5c74d7a.jpg)

![](/api/attachments/M82RXSMS/fulltext/images/3768b15a416a83e9aa272a51c61166813d8ddd3bb37d4cad874ae676054b4086.jpg)

![](/api/attachments/M82RXSMS/fulltext/images/a673922ad95f691d58ba2cbaafc7bd1d38386ecb2f8c16cc70f302ef2fa85f7a.jpg)

![](/api/attachments/M82RXSMS/fulltext/images/fd086a10be484f59b5645d2bdacb916ccd693715c8f5e6809829729e35e89e61.jpg)

![](/api/attachments/M82RXSMS/fulltext/images/7a090fb9c20c5324b6474ec4f7121fbae29b473e98681d5cdb66e2d0e80a412f.jpg)

![](/api/attachments/M82RXSMS/fulltext/images/4b5914e934aafce4265e42c8b43db2cd2eceff69b7b458f824c17fc823291873.jpg)

![](/api/attachments/M82RXSMS/fulltext/images/780183a46f89f06b61fa4814437e30bad0e5acc49d31f032535b508248238081.jpg)

![](/api/attachments/M82RXSMS/fulltext/images/580a35d3a4c4f803cbb80c311b461b4ec1f98671fec2aa417a25177dcd42939e.jpg)

![](/api/attachments/M82RXSMS/fulltext/images/ff0a4a9dee646cb4f92093f70ce85625da0eb0b065ec78fc2659615bfa503186.jpg)

![](/api/attachments/M82RXSMS/fulltext/images/4f104d7417e5b8c3289e99b54351c6771ac485d3ef2d6bd5b9b0b09e2c17f03c.jpg)

![](/api/attachments/M82RXSMS/fulltext/images/74c6485423cc8137f52d1c0bbdec12f812735553c9c8ba9203ad7092feed0348.jpg)

![](/api/attachments/M82RXSMS/fulltext/images/2554fac224e66f35ad64e9b02cc0efa762ba8b98d15b59358f8a2f3a482957f5.jpg)

![](/api/attachments/M82RXSMS/fulltext/images/8edf70c9de988de29efdd974c9d2cbfaf8469103b3495ab024c86cb5c369b286.jpg)

![](/api/attachments/M82RXSMS/fulltext/images/3fc40d6d7050e081ac44daea4a8c648df1c8d8041f6add40e643a2a6f20edd0a.jpg)

![](/api/attachments/M82RXSMS/fulltext/images/292f1f0ae13b4e150a6faba3efb4229d2b66bda7a246b9fd187cfcec5c0618c5.jpg)

![](/api/attachments/M82RXSMS/fulltext/images/16ac0b93f3b2eee5ba043532983cff66f2963e7627f0b3f958cb75f71f45f6ec.jpg)  
Fig. 7. Ef<sup>fi</sup>cient frontiers. This <sup>fi</sup>gure shows the relationship between the ef<sup>fi</sup>cient frontier and the rate of return achieved by the system in twenty sessions. The ef<sup>fi</sup>cient frontier for the ten stocks used in the experiment is derived by a traditional form of the Markowitzian process The performance of our system is shown as O in the figures, Red O pertains to the case when the system's performance positions to the upper left of the ef<sup>fi</sup>cient frontier. Being positioned at the upper-left of the ef<sup>fi</sup>cient frontier is evidence that the rate of return for our investment model is superior to that of the typical portfolio selection model. Fourteen out of twenty sessions con<sup>fi</sup>rm the plots in the upper-left section. The case with no brain information has been indicated by blue squares. Many of these are scattered near the ef<sup>fi</sup>cient frontier. Their positioning con<sup>fi</sup>rms that many sessions show declined performances as compared to those with brain information

![](/api/attachments/M82RXSMS/fulltext/images/20a0ab2d893fdbba7981009bd7a19e26c0fd1e710c16be4c93828eedff32af96.jpg)

Table 6  
![](/api/attachments/M82RXSMS/fulltext/images/bb555b54c6ed175d233700d5262c273e71589ec8ec7c28db7b6e50a0de8bf0e9.jpg)

![](/api/attachments/M82RXSMS/fulltext/images/6ac19a0bdd42d19249e6945d5a18c7a1ab7558d2a507e18ce20e1483865cc7a8.jpg)  
Fig. 8. The performance improvement. The vertical axis indicates the number of sessions. The horizontal axis indicates the extent of the improvement in the rate of return provided by an investment system using brain information. This improvement is in comparison to respective benchmarks and is indicated by the difference in the average rate of return with regard to a series of rates of return. On the left is a system using only the forecast rate of return and no brain information. In the middle is a system using TOPIX's rate of return for the same period. On the right is a system using forecasts derived from an ARMA–GARCH model. Introducing brain information helps improve investment performance. In addition, in many cases, our models show superior investment performance in comparison to the market index (TOPIX) and the ARMA–GARCH model.

The reader may consider a consistency between our results and the ef-<sup>fi</sup>cient market hypothesis. Our conclusion pertains to predictability, and this is contrary to the concept of the ef<sup>fi</sup>cient market hypothesis, which denies predictability by using the market ef<sup>fi</sup>ciency argument. However, recent advances in behavioral <sup>fi</sup>nance and neuroeconomics show that the presence of human decision-making bias from rationality is caused. This often brings about the distortion of price formation in markets and, as a result, provides room for predictability (Barberis et al. [2], Grinblatt and Han [9], Barberis and Thaler [3]). Our analysis also touches on these studies. In other words, human decision-making bias lowers market ef<sup>fi</sup>- ciency and as a result, predictability exists. It is our belief that human brain information is useful data that can help us understand such decision-making bias.

Transaction costs are not explicitly considered here since we compare the performance of our model to that of the portfolio theory and other <sup>fi</sup>- nancial time-series models including the GARCH. The simulation allows for a change in the rate of investment of each term without transaction costs both in our model and in the models based on the portfolio theory and the GARCH. However, it is imperative to consider transaction costs from a practical perspective. Speci<sup>fi</sup>cally, an average of 8.7 basis points of return (daily) is obtained in our model. This means that no pro<sup>fi</sup>ts will be yielded if transaction costs that exceed the rate of return are present.

Prediction accuracy of the three-layer perceptron model.

<table><tr><td rowspan="2">Session</td><td colspan="3">Return improvement</td></tr><tr><td>Portfolio return</td><td>TOPIX return</td><td>ARMA-GARCH model</td></tr><tr><td>1</td><td>0.00255</td><td>-0.00128</td><td>-0.16857</td></tr><tr><td>2</td><td>0.00406</td><td>0.00701</td><td>0.48001</td></tr><tr><td>3</td><td>0.00619</td><td>0.00504</td><td>0.60290</td></tr><tr><td>4</td><td>0.00127</td><td>0.00540</td><td>-0.08186</td></tr><tr><td>5</td><td>0.00336</td><td>-0.00047</td><td>0.02472</td></tr><tr><td>6</td><td>0.00297</td><td>0.00554</td><td>0.07266</td></tr><tr><td>7</td><td>0.00473</td><td>0.00769</td><td>0.53645</td></tr><tr><td>8</td><td>0.00734</td><td>0.00619</td><td>0.68465</td></tr><tr><td>9</td><td>0.00817</td><td>0.00161</td><td>0.28171</td></tr><tr><td>10</td><td>0.00628</td><td>0.00513</td><td>0.65893</td></tr><tr><td>11</td><td>0.00610</td><td>0.00441</td><td>0.45198</td></tr><tr><td>12</td><td>0.00829</td><td>0.00661</td><td>0.82571</td></tr><tr><td>13</td><td>0.00752</td><td>0.00584</td><td>0.62302</td></tr><tr><td>14</td><td>0.00944</td><td>0.00328</td><td>0.38325</td></tr><tr><td>15</td><td>0.00752</td><td>0.00137</td><td>0.11545</td></tr><tr><td>16</td><td>0.00119</td><td>-0.00264</td><td>-0.29909</td></tr><tr><td>17</td><td>0.00316</td><td>0.00573</td><td>0.14786</td></tr><tr><td>18</td><td>0.00684</td><td>0.00980</td><td>0.58758</td></tr><tr><td>19</td><td>0.00318</td><td>-0.00018</td><td>0.24936</td></tr><tr><td>20</td><td>0.00535</td><td>0.00831</td><td>0.55811</td></tr><tr><td>Average</td><td>0.00528</td><td>0.00422</td><td>0.33674</td></tr></table>

Performing a more accurate analysis and evaluation requires relearning investment models that explicitly incorporate transaction costs. Here we reduced the number of investments and calculated the performance for the case when transaction costs were reduced. This was accomplished by imposing a new condition, stating, “investments will not be made when the absolute values of the most appropriate rate of investment predicted by the model are below a certain threshold level.”

Table 7 shows the relationship between the number of investment times and system performance. The threshold level in the table means that the system takes investments if the optimal investment rate forecasted by our system exceeds the threshold level; otherwise, the system does not take investments. The number of times in the table shows the number of times of investment among all sessions under the threshold level. Evaluating this result indicates that a reduction in the number of transactions has no negative impact on investment performance. As the threshold level increases, the number of investment times decreases, but the average return of investment increases. A decrease of the number of investment times means transaction cost reduction; hence, we believe that the transaction cost problem will be under control.

Finally, we point out a remaining question. In the long term, it is important to consider two types of learning by users. One includes the mastery of investment techniques through market experience, and the other entails the learning effects by using the system. As Lo and Repin [14] indicate, the learning through market experience is expected to result in more selective biological responses. Moreover, the learning effect by using the system implies interactive learning. It includes learning by the system side, which accompanies diachronic changes in human biological responses, and investment learning by the human side through feedback regarding the most appropriate investment information from the system. To what extent these learning effects impact investment performances is an interesting topic for long-term system use.

Table 7  
Relationship between the number of investment times and system performance.

<table><tr><td>Threshold level</td><td>Number of times</td><td>Average of return</td><td>Standard deviation of return</td><td>Sharp ratio of return</td></tr><tr><td>0.00</td><td>400</td><td>0.00087</td><td>0.0044</td><td>0.1968</td></tr><tr><td>0.05</td><td>334</td><td>0.0010</td><td>0.0048</td><td>0.2162</td></tr><tr><td>0.10</td><td>275</td><td>0.0012</td><td>0.0053</td><td>0.2305</td></tr><tr><td>0.15</td><td>207</td><td>0.0016</td><td>0.0059</td><td>0.2709</td></tr><tr><td>0.20</td><td>161</td><td>0.0020</td><td>0.0065</td><td>0.3055</td></tr><tr><td>0.25</td><td>114</td><td>0.0032</td><td>0.0070</td><td>0.4599</td></tr><tr><td>0.30</td><td>85</td><td>0.0040</td><td>0.0076</td><td>0.5276</td></tr></table>

## Appendix A. Supplementary data

Supplementary data to this article can be found online at http://dx.doi. org/10.1016/j.dss.2012.05.041.

## References

[1] N. Barberis, M. Huang, T. Santos, Prospect theory and asset prices, Quarterly Journal of Economics 116 (2001) 1–53.

[2] N. Barberis, A. Shleifer, R. Vishny, A model of investor sentiment, Journal of Financial Economics 49 (3) (1998) 307–343.

[3] N. Barberis, R. Thaler, A survey of behavioral <sup>fi</sup>nance, in: G. Constantinides, M. Harris, R.M. Stulz (Eds.), Handbook of the Economics of Finance, Elsevier, 2003, pp. 1053–1128.

[4] D. Barraclough, M. Conroy, D. Lee, Prefrontal cortex and decision making in a mixed-strategy game, Nature Neuroscience 7 (2005) 404–410.

[5] C. Camerer, G. Loewenstein, D. Prelec, Neuroeconomics: how neuroscience can inform economics, Journal of Economic Literature 43 (2005) 9–64.

[6] N. Camille, G. Coricelli, J. Sallet, P. Pradat-Diehl, J. Duhamel, A. Sirigu, The involvement of the orbitofrontal cortex in the experience of regret, Science 304 (2004) 1167–1170.

[7] J. Chen, S. Lee, An exploratory cognitive DSS for strategic decision making, Decision Support Systems 36 (2003) 147–160.

[8] J. George, K. Duffy, M. Ahuja, Countering the anchoring and adjustment bias with decision support systems, Decision Support Systems 29 (2000) 195–206.

[9] M. Grinblatt, B. Han, Prospect theory, mental accounting, and momentum, Journal of Financial Economics 78 (2005) 311–339.

[10] K. Hikosaka, M. Watanabe, Delay activity of orbital and lateral prefrontal neurons of the monkey varying with different rewards, Cerebral Cortex 10 (2000) 263–271.

[11] Y. Hoshi, Functional near-infrared optical imaging: utility and limitations in human brain mapping, Psychophysiology 40 (2003) 511–520.

[12] F. Kuo, C. Hsu, R. Day, An exploratory study of cognitive effort involved in decision under framing—an application of the eye-tracking technology, Decision Support Systems 48 (2009) 81–91.

[13] A. Lo, D. Repin, The psychophysiology of real-time <sup>fi</sup>nancial risk processing, Journal of Cognitive Neuroscience 14 (2002) 323–339.

[14] A. Lo, D. Repin, B. Steenbarger, Fear and greed in <sup>fi</sup>nancial markets: a clinical study of day-traders, NBER Working Paper (2005) No. 11243.

[15] T. Lohrenz, K. McCabe, C. Camerer, P. Montague, Neural signature of <sup>fi</sup>ctive learning signals in a sequential investment task, Proceedings of the National Academy of Sciences 104 (2007) 9493–9498

[16] S. Luu, T. Chau, Neural representation of degree of preference in the medial prefrontal cortex, NeuroReport 20 (2009) 1581.

[17] J. O'Doherty, Reward representations and reward-related learning in the human brain: insights from neuroimaging, Current Opinion in Neurobiology 14 (2004) 769–776.

[18] J. O'Doherty, M. Kringelbach, E. Rolls, J. Hornak, C. Andrews, Abstract reward and punishment representations in the human orbitofrontal cortex, Nature Neuroscience 4 (2001) 95–102.

[19] T. Shimokawa, T. Misawa, K. Suzuki, Neural representation of preference relation ships, NeuroReport 19 (2008) 1557–1561.

[20] T. Shimokawa, K. Suzuki, T. Misawa, Augmented reinforcement learning and investment decision making, Neurocomputing 72 (2009) 3447–3461.

[21] T. Shimokawa, K. Suzuki, T. Misawa, K. Miyagawa, Predictability of investment behavior from brain information measured by functional near-infrared spectroscopy: a Bayesian neural network model, Neuroscience 161 (2009) 347–358.

[22] W. Tan, C. Tan, H. Teo, Consumer-based decision aid that explains which to buy decision con<sup>fi</sup>rmation or overcon<sup>fi</sup>dence bias? Decision Support Systems 53 (1) (2012) 127–141.

Tetsuya Shimokawa is an Associate Professor at the School of Management at Tokyo University of Science, Japan, and has reserved Ph.D. in Economics from the University of Tokyo. He was a research fellow (DC) of the Japan Society for the Promotion of Science in 1997; research fellow of the Center for International Research on the Japanese Economy, the University of Tokyo in 1999; and was a research fellow (PD) of the Japan Society for the Promotion of Science in 2000. His research interests include computational economics, pattern recognition, neuroeconomics, and behavioral <sup>fi</sup>nance.

Kanta Kinoshita is a student at the Graduate School of Economics, Waseda University, Japan. His research interests include the <sup>fi</sup>nancial time-series analysis, behavioral <sup>fi</sup>- nance, and neuroeconomics

Kazuhiro Miyagawa is a student at the Graduate School of Economics, Hitotsubashi University, Japan. His research interests include the arti<sup>fi</sup>cial intelligence, game theory, and neuroeconomics

Tadanobu Misawa (member) is a lecturer at the Graduate School of Science and Engineer ing, University of Toyama. He received his B.E., M.E., and Ph.D. degrees from Kanazawa University in 1999, 2001, and 2004. He was a doctoral fellow of Kanazawa Institute of Technology in 2004. He was an assistant professor at the School of Management, Tokyo University of Science, in 2005. He is interested in arti<sup>fi</sup>cial intelligence, especially reinforcement learning and multiagent system
