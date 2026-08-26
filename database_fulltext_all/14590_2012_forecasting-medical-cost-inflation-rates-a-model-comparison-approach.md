---
otero_id: 14590
otero_key: "MUNDD4XJ"
title: "Forecasting medical cost inflation rates: A model comparison approach"
authors: "Qing Cao; Bradley T. Ewing; Mark A. Thompson"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.12.012"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Forecasting medical cost in<sup>fl</sup>ation rates: A model comparison approach

Qing Cao ⁎, Bradley T. Ewing, Mark A. Thompson

Area of Information Systems and Quantitative Sciences, Rawls College of Business, Texas Tech University, Lubbock, TX 79409-2101, United State

## a r t i c l e i n f o

Article history: Received 19 February 2011 Received in revised form 25 December 2011 Accepted 27 December 2011 Available online 4 January 2012

Keywords: Medical care In<sup>fl</sup>ation Forecasting Neural networks ARIMA

## a b s t r a c t

Due to healthcare costs rising faster than overall cost of living, decision makers (i.e., households, businesses, and governments) must cut back on healthcare utilization or spending elsewhere to be <sup>fi</sup>scally responsible. Accurate forecasts of future medical costs are critical for ef<sup>fi</sup>cient planning, budgeting and operating decisions at all levels. This research compares the accuracy of the linear autoregressive moving average (ARMA) model and the nonlinear neural network model in producing forecasts of medical cost in<sup>fl</sup>ation rates. The analysis focuses on twelve monthly measures of medical costs including the overall medical care price index and eleven (disaggregated) subsectors of medical costs. In addition to standard symmetric measures of forecast accuracy, we utilize two asymmetric error measures designed to capture and penalize preferences for under- and overprediction in model selection. The <sup>fi</sup>ndings indicate that the neural network model outperforms the univariate ARMA in both 1-step and 12-step ahead forecasts. A number of important practical implications are discussed, such as the use of accurate forecasts in contract negotiations, budgeting and planning.

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

Health care spending continues to grow faster than the economy. According to the Centers for Medicare and Medicaid Services, national health expenditures accounts for 16.2% of gross domestic product in 2008. Increases in demand for healthcare products and services from a growing population, consumer price insensitivity, and technology are just some of the factors that continue to put an upward pressure on prices. Rising prices often make operating and budgetary decisions more dif<sup>fi</sup>cult as the share of these health expenditures relative to the rest of the budget increases. As such, decision makers (i.e., households, businesses, and governments) must cut back on healthcare utilization or spending on other products or services elsewhere. Hence, accurate forecasts of future medical costs are critical for ef<sup>fi</sup>cient planning, budgeting and operating decisions at all levels (i.e., household, <sup>fi</sup>rm, and government). For instance, while many consumers at the household level have some form of insurance, a substantial amount of medical payments are made out-of-pocket. Consequently, many households participate in health savings accounts (HSA). Knowledge about future changes in medical costs would assist households in optimally determining the amount to allocate to their respective HSAs.<sup>1</sup>

Budget analysts and <sup>fi</sup>nancial managers require accurate forecasts of the rate of medical price increases. Medical cost in<sup>fl</sup>ation plays a major role in planning future budget obligations or liabilities such as pension plans. In addition, understanding the time series behavior of medical costs provides nonhealth-related <sup>fi</sup>rms as well as healthcare providers with information to negotiate with insurance companies on health plans. Financial managers and health care administrators use forecasts to prepare and evaluate their budget positions, premiums, and capitation rates [13]. Payors and providers may also negotiate multi-year contracts. In doing so, both parties may arrange fee schedules to some cost of living adjustment. Likewise, payors may be more inclined to underpredict medical cost in<sup>fl</sup>ation whereas providers may be more inclined to overpredict. The prices for different medical sectors or specialties may behave differently, thus understanding and modeling price changes disaggregated by medical sector could be bene<sup>fi</sup>cial for use in business valuations, industry benchmarking, planning and budgeting, and negotiating insurance contracts.

With respect to state and federal governments, the sustainability of public programs (e.g., Medicare and Medicaid) requires accurate forecasts of medical cost in<sup>fl</sup>ation. Budget and legislative analysts use forecasts to impose premium caps, payment rates, and global expenditure limits. In fact, accurate forecasts are vital to the legislative process when future public programs are being proposed for policy evaluation and comparison of various health-related programs. For example, the Congressional Budget Of<sup>fi</sup>ce provides cost estimates on proposed legislation while state budget agencies often provide cost estimates for state-level legislation. Accurate forecasts are critical for determining the costs and bene<sup>fi</sup>ts of health-related programs when taxpayers will be responsible for meeting future government obligations. However, it is possible that taxpayers as well as budget analysts may prefer that changes in medical costs be overpredicted as opposed to underpredicted if the costs of making a forecast mistake are higher for the latter. This might be the case if budget de<sup>fi</sup>cits are more costly than the equivalent surplus to the taxpayer, especially if there is an increase in taxes to make up the budget shortfall from underpredicting changes in medical costs. Alternatively, budget analysts may have a similar view with respect to de<sup>fi</sup>cits and making spending cuts due to underpredicting changes in medical costs relative to the case of overpredicting and an accompanying surplus. Thus, while having the most accurate forecast is certainly preferred, the loss associated with the forecasting errors may actually be asymmetric. Along with traditional symmetric error measures, our paper evaluates the medical cost forecasting models using asymmetric error measures that penalize the respective model for over- or underpredicting the actual rate of medical cost in<sup>fl</sup>ation.

Improved forecasts of medical cost in<sup>fl</sup>ation can yield better decisions for individuals, businesses, and government. While speci<sup>fi</sup>c industry models are proprietary, insurers, actuaries and other health care analysts typically utilize variations of autoregressive (AR) and moving average (MA) methods to conduct stochastic trend analysis; thus, our comparator method is the general class of autoregressivemoving average (ARMA) models. However, the use of traditional time series forecasting models that assume linear relationships between past observations and subsequent forecasts may be problematic and lead to poor forecasts if the data actually exhibit nonlinear patterns as evident in Fig. 1. Seeking to achieve greater levels of accuracy, forecasters are always looking for new quantitative forecasting methods to compare to those they currently use. Since there are few studies that have speci<sup>fi</sup>cally forecasted medical cost in<sup>fl</sup>ation rates [11,26], we choose to compare the traditional linear time series model (e.g., ARMA models) against an arti<sup>fi</sup>cial neural network (NN) model. NN models are based on previous research that indicates the human brain relies on dense connections between information nodes and a nonlinear, parallel structure to process information [15]. NN models then attempt to replicate these characteristics through mathematical formulas that link input and output variables. Furthermore, NN models have an amazing ability to recognize patterns. Thus, NN-type models tend to outperform other nonlinear approaches [17,22,27,33,34].

![](/api/attachments/MUNDD4XJ/fulltext/images/e5dce94bfad2c9526b80a4d28c59641354075924ad1ae5bc582e61df3ba1ab6e.jpg)  
Fig. 1. Medical cost in<sup>fl</sup>ation rates.

![](/api/attachments/MUNDD4XJ/fulltext/images/3ab6419a7251c5f4f0c122846a2776862574653900410cc5e497360eaf90edfa.jpg)  
Fig. 1. (continued)

While successful forecasting applications of neural network models have been reported in a number of business <sup>fi</sup>elds, including accounting [33], <sup>fi</sup>nance [6], management information systems [33], marketing [29], production management [9], and energy consumption [1], to our knowledge there has been no application of NN models to medical cost in<sup>fl</sup>ation rates. However, Swanson and White [28] applied neural network models to macroeconomic forecasting and found that linear models actually performed better. In terms of speci<sup>fi</sup>cally forecasting in<sup>fl</sup>ation, Moshiri and Cameron [19] found neural network models did as well and in some cases better than traditional econometric models. Furthermore, Nakamura [20] examined in<sup>fl</sup>ation using the U.S. GDP de<sup>fl</sup>ator and found that neural network models outperformed univariate autoregressive models over short horizons. As such, this paper <sup>fi</sup>lls a void in the literature by providing evidence on whether NN models can be an effective alternative to forecasting medical cost in<sup>fl</sup>ation rates.

In this paper, we use a NN model to generate forecasts of various measures of medical cost in<sup>fl</sup>ation. We then compare the NN forecasts with those produced by the linear alternative based on the best <sup>fi</sup>tting

ARMA model. In particular, we compare accuracy for 1-step and 12- step ahead forecasts for the aggregate or overall medical care in<sup>fl</sup>ation rate and for the eleven disaggregated (by sector or type) medical in-<sup>fl</sup>ation rates. Forecasts are compared using standard measures of mean squared error (MSE) and mean absolute error (MAE). A unique feature of our study, and one that is important given user preferences for over- or underprediction of medical cost in<sup>fl</sup>ation is the use of two asymmetric error measures that speci<sup>fi</sup>cally penalize for over- and underpredicting the actual medical cost in<sup>fl</sup>ation rate. For example, consider the case for both payors and providers. Both groups want the most accurate forecast of changes in medical costs. However, the loss associated with forecasting errors may fundamentally differ by group. Moreover, the loss may not only be asymmetric but in terms of assessing model performance it may be better to penalize for overpredicting in some cases (e.g., such as for payors) and for underpredicting in other cases (e.g., for providers). This naturally leads to the following question: Is the selection criteria for the medical cost in<sup>fl</sup>ation forecasting model sensitive to the error measure used (i.e., symmetric or asymmetric)? Our results indicate that the neural network model outperforms the linear alternative when forecasting changes in medical care prices and may be a viable alternative to the traditional time series approach. Moreover, results hold regardless of the error measure used.

## 2. Methods

The most widely used aggregate measure of medical prices in the U.S. is the Bureau of Labor Statistics’ consumer price index (CPI), which is designed to capture price changes for out-of-pocket expenditures.<sup>2</sup> Government agencies use the medical CPI for its budget estimates and policy simulations as it pertains to health care legislation. Employers tend to use the medical CPI as a benchmark for medical costs and to adjust their insurance premiums. Likewise, medical <sup>fi</sup>rms tend to use these medical indexes as a benchmark as oppose to their actual costs, which may be dif<sup>fi</sup>cult to obtain when negotiating contracts with payors, providers, or even purchasers. While several studies develop <sup>fi</sup>rm-level decision support tools using neural networks or arti<sup>fi</sup>cial intelligence [18,30–32], we are interested in using aggregate medical cost measures that can provide insurers, consultants, analysts, and employers with industry-level cost in<sup>fl</sup>ation benchmarks as well as provide forecasts of medical cost trends. As such, we obtained monthly CPI data for the broad category of medical care as well as the different medical subsectors. Medical care is one of the major groups in the CPI and is subdivided into two components: medical care commodities and medical care services.

Medical care commodities include prescription and nonprescription drugs as well as medical equipment and supplies. Medical care services, the larger of the two components, includes professional medical services, hospital services, nursing home services, and health insurance. Professional medical services consist of physicians’ services, dental services, eyeglasses and eye care, and other medical services. Hospital and related services consist of services provided to inpatients and outpatients as well as emergency room visits, nursing home care, and adult day care. The data span the common sample period of January 1996 to July 2010. Each index was seasonally adjusted using the Census X-11 method. Since unit root tests indicated that each medical CPI series (i.e., price level index) is nonstationary, we transformed each price series into a year-over-year in<sup>fl</sup>ation rate adjusting the sample period to start January 1997 for a total of 168 monthly observations.<sup>3</sup> The in<sup>fl</sup>ation rates are stationary and it is appropriate to use them in the univariate modeling framework described below.

## 2.1. Linear ARMA models

The in<sup>fl</sup>ation rate for each medical cost in<sup>fl</sup>ation rate is modeled as an ARMA process:

$$
\varphi (L) I N F _ {t} ^ {j} = \theta (L) \varepsilon_ {t} + \mu\tag{1}
$$

where $I N F _ { t } ^ { j }$ represents the in<sup>fl</sup>ation rate in the respective medical sector j (e.g., physician services, hospital services, etc.), ϕ and θ are polynomials in the lag operator L, and μ is a constant term. The best-<sup>fi</sup>tting ARMA model for each in<sup>fl</sup>ation rate was determined by examination of the autocorrelation functions and standard Box–Jenkins techniques.<sup>4</sup> The majority were ARMA(1,0) or AR(1) although as many as three AR and three MA terms were included in the various model speci<sup>fi</sup>cations.<sup>5</sup> Diagnostic tests indicated that the models were free of autocorrelation.

## 2.2. NN models

There are many different kinds of neural networks. For example, a single-layer feedforward network does not contain any neurons that are connected to themselves or any others earlier in the system. While this makes it easy to train, there are certain problems that cannot be solved without another layer of neurons. The solution to this was a multilayer-network with two or more layers. Another type of NN architecture is called the recurrent network, which differs from the feedforward networks since neurons transport a signal back through the network. However, feedforward network models are proven to be effective in forecasting or prediction, whereas recurrent network models are more effective in classi<sup>fi</sup>cations.

As such, we apply a multilayer network approach to predict medical cost in<sup>fl</sup>ation rates. In a feedforward neural network model, input and output variables are linked through one or more hidden layers, each consisting of processing units that are referred to as hidden nodes. Following Zhang, Cao, and Schniederjans [33], we assume a single hidden layer. Each node in the hidden layer has a weighted connection to each independent variable and each output variable. Because we focus on medical cost in<sup>fl</sup>ation, the model examined here has a single output variable.

To formally describe our feedforward model, let $Y _ { t }$ denote the single output of the neural network model and let x and $z _ { j }$ denote, respectively, the $i ^ { t h }$ input variable $( i = 1 , . . . , k )$ and the $j ^ { t h }$ middle layer variable. Following common practice in the neural network literature [21], we assume that (1) logistic functions link the input variables to the middle layer nodes, and (2) the neural network output is simply the weighted sum of the hidden nodes. Given these assumptions, the three-layer neural network model can be written succinctly as:

$$
(Y _ {t}) = f (X, \alpha , \beta) = \sum_ {j = 1} ^ {n} \alpha_ {j} z _ {j} = \sum_ {j = 1} ^ {n} \alpha_ {j} \log \operatorname{sig} \left(\sum_ {i = 1} ^ {k} \beta_ {i j} x _ {i} + \beta_ {0 j}\right)\tag{2}
$$

where:

$\alpha _ { j }$ = is the weight attached to the $j ^ { t h }$ hidden layer variable in the output variable;

$\beta _ { i j }$ = is the weight attached to input i in the $j ^ { t h }$ hidden layer variable;

$$
\begin{array}{l l} \beta_ {0 j} & = \text { is   the   bias   weight   of   the   } j ^ {t h} \text {   hidden   layer   variable;   and } \\ \log \text { sig } & = \text { the   logistic   transfer   function   log   sig   (a) } \\ & = 1 / [ (1 + \exp (- a)) ]. \end{array}
$$

The network weights were estimated using least squares with regularization parameters, $\lambda _ { 1 }$ and $\lambda _ { 2 } ,$ included to penalize complexity and thus avoid over<sup>fi</sup>tting (see Bishop [4], Section 9.2). To estimate these parameters, we employed a backward propagation (BP) algorithm, which involves the iterative adjustment of an initial set of parameters in order to improve model <sup>fi</sup>t or increase forecast accuracy. The popularity of BP algorithms re<sup>fl</sup>ects their ease of implementation and demonstrated success in <sup>fi</sup>nding “effective solutions to large and dif<sup>fi</sup>cult problems” (Haykin [15], p. 172).

## 2.3. Forecasting accuracy procedure

We used monthly medical cost in<sup>fl</sup>ation rates for January 1997 to July 2008 for a total of 139 monthly observations to estimate the two types of models. Thus, there are 24 monthly observations for the hold-out sample. We used a rolling estimation method to generate h-step-ahead forecasts and then evaluated the forecasting models using several different error measures. The traditional mean squared error (MSE) and mean absolute error (MAE) measures are as follows:

$$
M S E = \frac {1}{T} \sum_ {t = 1} ^ {T} \left(Y _ {t} - \hat {Y} _ {t}\right) ^ {2}\tag{3}
$$

$$
M A E = \frac {1}{T} \sum_ {t = 1} ^ {T} \left| Y _ {t} - \hat {Y} _ {t} \right|\tag{4}
$$

where T is the number of predictions. $Y _ { t }$ is the actual in<sup>fl</sup>ation rate and <sup>^</sup>Y is the forecasted in<sup>fl</sup>ation rate for period t. However, the MSE and MAE treat over- and underpredictions the same.

As previously mentioned, individuals, businesses, or governments may have a preference for over- or underpredicting the respective medical cost in<sup>fl</sup>ation rate. In developing a decision support tool for forecasting model selection, it is bene<sup>fi</sup>cial to have an error measure that takes into account the asymmetric preferences of users. One such measure has been proposed by Brailsford and Faff [5] known as the mean mixed error (MME) that allows one to penalize for underpredicting (MME(U)) or overpredicting (MME(O)):

$$
M M E (U) = \frac {1}{T} \left(\sum_ {t = 1} ^ {T} \sqrt {\left| Y _ {t} - \hat {Y} _ {t} \right| * (1 - I)} + \sum_ {t = 1} ^ {T} \left| Y _ {t} - \hat {Y} _ {t} \right| * (I)\right)\tag{5}
$$

$$
M M E (O) = \frac {1}{T} \left(\sum_ {t = 1} ^ {T} \left| Y _ {t} - \hat {Y} _ {t} \right| * (1 - I) + \sum_ {t = 1} ^ {T} \sqrt {\left| Y _ {t} - \hat {Y} _ {t} \right| * (I)}\right)\tag{6}
$$

where I is the indicator function such that $I { = } 1 \mathrm { i f } Y _ { t } – \hat { Y }$ (underpredictions) and $I { = } 0$ (overpredictions) otherwise.<sup>6</sup> Thus, this measure will identify if model selection is sensitive to users’ preferences for overor underpredicting medical cost in<sup>fl</sup>ation rates.

## 2.4. Hypothesis testing procedure

To formally demonstrate the accuracy of the models in this study, the following hypotheses were developed:

H1. There is no forecasting accuracy difference between forecasts produced by linear ARMA models and those produced by nonlinear NN models.

For purposes of statistical testing, this hypothesis is subdivided into two parts:

H1a. There will be no forecasting accuracy difference in 1-step ahead forecasts produced by ARMA models and those produced by nonlinear NN models.

H1b. There will be no forecasting accuracy difference in 12-step ahead forecasts produced by ARMA models and those produced by nonlinear NN models.

To evaluate the hypotheses, we assessed the differences in the forecast accuracy statistics computed for each model. In particular, we used a paired sample t-test [7] to evaluate the relative predictive accuracy between models of the 1-step ahead forecasts (H1a) and 12-steps ahead forecasts (H1b) for each medical in<sup>fl</sup>ation rate. Based on prior research, we expect that nonlinear NN models will yield smaller forecasting errors (i.e., improve forecasting accuracy) than the linear alternative ARMA models, resulting in rejection of the null hypotheses.

## 3. Results and discussion

The descriptive statistics for each medical cost in<sup>fl</sup>ation series over the entire sample are reported in Table 1. As can be seen, there is some variation across the different medical cost in<sup>fl</sup>ation rates. Overall medical care in<sup>fl</sup>ation averaged 3.89% over the entire sample. However, in<sup>fl</sup>ation rates differed substantially between the two major components of medical care commodities (2.93%) and medical care services (4.19%). There was some variation in in<sup>fl</sup>ation rates among medical services. For example, the annual in<sup>fl</sup>ation rate for physician services averaged 3.08% compared to 4.51% for dental services and eyeglasses and 1.75% for eye care. Hospital services annual rate of in<sup>fl</sup>ation was 5.96% with outpatient services averaging 6.57%. Examination of the standard deviation of various measures of medical cost in<sup>fl</sup>ation reveals similar disparities ranging from a high of 2.03 (outpatient hospital services) to a low of 0.48 (professional services). In addition, the variability within and across the different medical cost in<sup>fl</sup>ation rates can be seen in Fig. 1. Interestingly, the graphs illustrate the effect of the recent recession that started December 2007 with several in<sup>fl</sup>ation rates making steep downward adjustments. This observation of severe and steep adjustments in in<sup>fl</sup>ation rates is consistent with previous <sup>fi</sup>ndings of macroeconomic time series exhibiting asymmetric or nonlinear adjustments over the business cycle [12,23,25]. According to Sichel [25] “steep adjustments” represents one type of nonlinearity. This evidence of nonlinearity is problematic as ARMA models may be misspeci<sup>fi</sup>ed and lead to poor out-of-sample forecasts. In fact, Zhang et al. [33] <sup>fi</sup>nd that NN models outperform linear models in cases where there is nonlinearity. As such, in these nonlinear cases, NN models may be better suited for forecasting medical cost in<sup>fl</sup>ation rates over the traditional linear alternative. Since there is considerable variability across the different medical cost in<sup>fl</sup>ation rates, it is important to model and forecast each measure of medical cost in<sup>fl</sup>ation separately.

The paired sample t-test is used to test the hypotheses. In order to test H1, we consider the forecasting performance of the NN and ARMA models for each medical cost in<sup>fl</sup>ation rate listed in Table 1 by examining the errors for 1-step (H1a) and 12-step (H1b) ahead forecasts. Tables 2 and 3 present a summary of the forecasting results and respective comparisons. Regardless of the error measure used, the results from the 1-step ahead forecasts indicate that the NN model outperforms the best in-sample ARMA model. Furthermore, the differences in forecast errors were signi<sup>fi</sup>cant at the 5% level or less rejecting H1a (i.e., no forecasting accuracy difference in 1-step ahead forecasts between ARMA and NN models). The same can be said for the 12-step ahead forecasts with three exceptions: Professional Services, Eyeglasses and Eye Care, and Other Services. That is, the differences in forecast errors were signi<sup>fi</sup>cant at the 5% level or less rejecting H1b (i.e., no forecasting accuracy difference in 12-step ahead forecasts between ARMA and NN models). For these three cases, the use of MSE shows their respective signi<sup>fi</sup>cance levels to be 0.08, 0.16, and 0.08, which may be interpreted as only marginally signi<sup>fi</sup>cant at best. Our <sup>fi</sup>ndings provide additional support to previous work where NN models consistently outperform other linear methods [3,8,16].

Generally speaking, there are considerable improvements in forecasting medical cost in<sup>fl</sup>ation rates by employing NN models over the standard linear alternative models. These results are robust across the different error measures, including the asymmetric error measures. For example, healthcare providers such as physicians, hospitals, ophthalmologists, and dentists in negotiations with third-party payors over reimbursement rates and fees will <sup>fi</sup>nd having accurate forecasts to be bene<sup>fi</sup>cial, especially considering the substantial time costs of negotiations which may encourage the use of multi-year contracts. Once rates and fees are agreed upon, benchmarking these rates to a cost of living measure may be appropriate. For example, physicians may want to use the in<sup>fl</sup>ation forecast associated with physician services. The latter case also illustrates the incentive for physicians to overpredict future in<sup>fl</sup>ation, whereas payors may prefer to underpredict. Optimally, both parties would want access to the most accurate forecasts. However, if model selection was sensitive to the respective error measure, then this result could add to the negotiation costs. In any event, we found that the NN models outperformed the linear alternative even when the forecasting evaluation was performed using asymmetric error measures.

Government agencies and policymakers also prefer accurate forecasts of medical cost in<sup>fl</sup>ation rates. In particular, forecasts of the various categories of medical care services and medical commodities are used for budgeting, public policy, and program evaluation. For example, current programs often benchmark reimbursement rates, premiums, and fees against some medical cost index. More accurate forecasts of medical cost in<sup>fl</sup>ation rates also provide budget analyst more con<sup>fi</sup>dence in forecasts of program-level health expenditures. The Medicare Part D prescription program is one such example. This particular program puts future cost obligations on the budget. As such, accurate forecasts are important, but underpredicting the cost of the program could be detrimental to taxpayers who eventually foot the bill. Again, our results indicate that the NN model outperformed the ARMA model for prescription drugs as well as medical care commodities regardless of the error measure used to assess forecast accuracy. Likewise, future healthcare legislation or programs need accurate forecasts of medical costs for budget impact analysis. Depending on the type of healthcare program or the speci<sup>fi</sup>c healthcare sector the program is targeting (e.g., physicians or inpatient care), our results provide budget analysts with support on model selection.

Overall, these results highlight the usefulness of NN models in providing better forecasts of medical cost in<sup>fl</sup>ation rates over the traditional linear alternative. Of the 96 different model comparisons, the NN model had signi<sup>fi</sup>cantly lower forecasting errors than the ARMA model and only three comparisons that were not signi<sup>fi</sup>cantly lower. In most cases, the NN model reduced the forecasting error by more than half relative to the ARMA model. This evidence clearly indicates that NN models are better able to capture the data characteristics of medical cost in<sup>fl</sup>ation rates over ARMA models (e.g., nonlinearity). More accurate forecasts can greatly assist in negotiations of reimbursement rates, improve the decision making within the practice, and lead to better resource allocation and utilization of healthcare services.

## 4. Conclusion

We compared the forecast accuracy of a standard NN model to that of the traditional linear ARMA model for medical cost in<sup>fl</sup>ation rates. Our results indicate that the NN model outperforms the best <sup>fi</sup>tting ARMA model for each medical cost in<sup>fl</sup>ation rate examined at both 1- and 12-months ahead. The results can be used to support the decisions of various stakeholders in both the private and public sectors by providing valuable information on model selection for forecasting various forms of medical cost in<sup>fl</sup>ation.

While this research suggests using NN-type models for better forecasts, a concern exists with regards to the likelihood of physicians, hospital administrators, third-party payors, policymakers, etc.

to utilize NN-type models in actual practice. This concern is valid given the relative complexity and degree of technical sophistication needed to estimate and interpret nonlinear models. Moreover, in some cases, data limitations and cost constraints may inhibit the use of NN models. However, recent advancements in estimation techniques have led to commercially-available software packages that allow users to analyze the weights assigned to various variables and evaluate their impact on the predictive power of NN-type models. We believe the results presented here will encourage further investigation into the use of NN-type models to predict medical cost in<sup>fl</sup>ation. Finally, it is becoming easier for healthcare practitioners to adopt this methodology with minimal knowledge of neural networks and programming knowledge. In terms of implementation, practitioners can purchase off-the-shelf neural network application software to enhance their forecasting tools (e.g., NeuroShell©).

The main contribution of this study is the improved forecasting accuracy of a NN model over the traditional linear alternative (i.e., ARMA model). In addition, our results are robust to the standard error measures MSE and MAE, but also to asymmetric error measures that penalize the respective forecasting model for over- or underpredicting the (true) medical cost in<sup>fl</sup>ation rate. However, there are some limitations of this study that could be examined in future work. One avenue for future work could be to examine the robustness of our forecasting results to other medical cost measures as well as other models. With respect to other cost measures, some of these are proprietary in nature or limiting in scope. However, this work could be extended by examining the producer equivalent to the medical CPI that is published by the Bureau of Labor Statistics (i.e., producer price index). Regarding other models, there are a variety of alternative forecasting methods including hybrid approaches that combine NN with various statistical techniques that could be explored in future work. In addition, the univariate nature of this study could be extended to a multivariate setting. Of course, this paper provided evidence on the applicability of NN models as a better decision support tool over the linear alternative to forecast medical cost in<sup>fl</sup>ation rates.

## References

[1] R. Abdel-Aal, Univariate modeling and forecasting of monthly energy demand time series using adductive and neural networks, Computers and Industrial Engineering 54 (2008) 903–917.

[2] E. Berndt, D. Cutler, R. Frank, Z. Griliches, J. Newhouse, Price indexes for medical care goods and services: an overview of measurement issues, NBER Working paper, 1998, No. W6817.

[3] S. Bhattacharyya, P. Pendharkar, Inductive, evolutionary, and neural computing techniques for discrimination: a comparative study, Decision Sciences 29 (1998) 871-893.

[4] C. Bishop, Neural networks for pattern recognition, Oxford University Press, Oxford, 1997.

[5] T. Brailsford, R. Faff, An evaluation of volatility forecasting techniques, Journal of Banking and Finance 20 (1996) 419–438.

[6] Q. Cao, M. Parry, Neural network earnings per share forecasting models: a comparison of backward propagation and the genetic algorithm, Decision Support Systems 47 (2009) 32–41.

[7] W. Conover, Practical Nonparametric Statistics, second ed. John Wiley & Sons, New York, 1980.

[8] V. Desai, R. Bharati, The ef<sup>fi</sup>cacy of neural networks in predicting returns on stock and bond indices, Decision Sciences 29 (1998) 405–421.

[9] P. Doganis, E. Aggelogiannaki, H. Sarimveis, A combined model predictive control and time series forecasting framework for production-inventory systems, International Journal of Production Research 46 (2008) 6841–6853

[10] W. Enders, Applied Econometric Time Series, John Wiley & Sons, New York, 1995.

[11] B. Ewing, M. Piette, J. Payne, Forecasting medical net discount rates, The Journal of Risk and Insurance 70 (2003) 85–95.

[12] B. Ewing, M. Thompson, A state-level analysis of business cycle asymmetry, Bulletin of Economic Research, in press.

[13] P. Grimaldi, New healthcare price indexes aid <sup>fi</sup>nancial analysis, Healthcare Financial Management 48 (1994) 68–70 64, 66,.

[14] A. Harvey, Time Series Models, second ed. MIT Press, Cambridge, 1994.

[15] S. Haykin, Neural Networks: A Comprehensive Foundation, second ed. Prentice-Hall Englewood Cliffs 1999.

[16] J. Jiang, M. Zhong, G. Klein, Marketing category forecasting: an alternative of BVAR-artificial neural networks, Decision Sciences 31 (2000) 789–807

[17] E. Kim, W. Kim, Y. Lee, Combination of multiple classi<sup>fi</sup>ers for customer's purchase behavior prediction, Decision Support Systems 34 (2003) 167–175.

[18] N. Menon, B. Lee, Cost control and production performance enhancement by IT investment and regulation changes: evidence from the healthcare industry, Decision Support Systems 30 (2000) 153–169.

[19] S. Moshiri, N. Cameron, Neural network versus econometric models in forecasting in<sup>fl</sup>ation, Journal of Forecasting 19 (2000) 201–217.

[20] E. Nakamura, In<sup>fl</sup>ation forecasting using a neural network, Economics Letters 86 (2005) 373–378.

[21] M. Qi, Nonlinear predictability of stock returns using <sup>fi</sup>nancial and economic variables, Journal of Business & Economic Statistics 17 (1999) 419–429.

[22] M. Qi, Predicting US recessions with leading indicators via neural network model, International Journal of Forecasting 17 (2001) 383–401.

[23] J. Ramsey, P. Rothman, Time irreversibility and business cycle asymmetry, Journal of Money, Credit, and Banking 28 (1996) 1–21.

[24] D. Remler, S. Glied, How much more cost sharing will health savings accounts bring? Health Affairs 25 (2006) 1070–1078.

[25] D. Sichel, Business cycle asymmetry: a deeper look, Economic Inquiry 31 (1993) 224–236.

[26] F. Slesnick, Forecasting medical costs in tort cases: the role of the economist, Journal of Forensic Economics 4 (1990) 83–99.

[27] W. Spangler, J. May, L. Vargas, Choosing data-mining methods for multiple classi-<sup>fi</sup>cation: representational and performance measurement implications for decision support, Journal of Management Information Systems 16 (1999) 37–62.

[28] N. Swanson, H. White, A model selection approach to real-time macroeconomic forecasting using linear models and arti<sup>fi</sup>cial neural networks, The Review of Economics and Statistics 79 (1997) 540–550.

[29] R. Thieme, M. Song, R. Calantone, Arti<sup>fi</sup>cial neural network decision support systems for new product development project selection, Journal of Marketing Research 37 (2000) 499–506.

[30] S. Walczak, J. Scharf, Reducing surgical patient costs through use of an arti<sup>fi</sup>cial neural network to predict transfusion requirements, Decision Support Systems 30 (2000) 125–138.

[31] C.-S. Yang, C.-P. Wei, C.-C. Yuan, J.-Y. Schoung, Predicting the length of hospital stay of burn patients: comparisons of prediction accuracy among different clinical stages, Decision Support Systems 50 (2010) 325–335.

[32] J.-Y. Yeh, T.-H. Wu, C.-W. Tsao, Using data mining techniques to predict hospitalization of hemodialysis patients, Decision Support Systems 50 (2011) 439–448.

[33] W. Zhang, Q. Cao, M. Schniederjans, Neural network earnings per share forecasting models: a comparative analysis of alternative methods, Decision Sciences 35 (2004) 205–237.

[34] D. Zhu, G. Premkumar, X. Zhang, C. Chu, Data mining for network intrusion detection: a comparison of alternative methods, Decision Sciences 32 (2001) 635–653.

![](/api/attachments/MUNDD4XJ/fulltext/images/10dcab1c5890739a55946322f50a01007690b52c90b2c80caa505a50b99184fe.jpg)

Qing Cao is the Jerry Rawls Professor of Management Information Systems at the Rawls College of Business, Texas Tech University. His research interests include IT governance, IT diffusion and adoption, supply chain information management, strategic alignment and arti<sup>fi</sup>cial intelligence applications. He has published more than 40 research papers in top business journals such as Journal of Operations Management, Decision Sciences, Decision Support Systems, Communications of ACM, Journal of AIS, International Journal of Production Research, Information and Management, European Journal of Operational Research, Computers and Operations Research, Annals of Operations Research, Journal of Production and Innovation Management, International Journal of Project Manage-

ment, Journal of Database Management, International Journal of Production Economics, and among others. Dr. Cao also served as the Associate Program Chair at the Decision Sciences Institute Annual Meeting (2008).

![](/api/attachments/MUNDD4XJ/fulltext/images/37789a3aa01218bd536b35b50660088d95e7262760c10700740228f9cd5854a4.jpg)

Bradley T. Ewing is the Rawls Professor in Operations Management in the Rawls College of Business at Texa Tech University. Professor Ewing received his Ph.D. from Purdue University's Krannert School of Management. He regularly teaches courses in operations management and statistics. He has published over 100 articles and is the recipient of several research grants. He is currently working on projects related to life-cycle cost analysis, the modeling of wind characteristics for energy use and risk management, and energy.

![](/api/attachments/MUNDD4XJ/fulltext/images/7eea871bb7112edbf6ce5b3c6944b9591566803dc1104bd9b553313580dc8c93.jpg)

Mark A. Thompson is an Associate Professor of Operations Management and Associate Director of the Health Organization Management program at Texas Tech University, He joined the faculty in 2009 and has worked in the <sup>fi</sup>elds of operations management, risk analysis, energy, and health care. Currently, he serves as the co-editor of International Journal of Information and Operations Management Education and on the editorial board of another journal. Professor Thompson has previously held positions as the Cree-Walker Chair of Business Administration at Augusta State University, as State Economic Forecaster at the University of Arkansas—Little Rock, and as Assistant Professor at Stephen F. Austin State University.
