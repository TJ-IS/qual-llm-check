---
otero_id: 5800
otero_key: "MSXYGJZC"
title: "A multivariate intelligent decision-making model for retail sales forecasting"
authors: "Z.X. Guo; W.K. Wong; Min Li"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.01.026"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A multivariate intelligent decision-making model for retail sales forecasting

Z.X. Guo <sup>a,</sup>⁎, W.K. Wong <sup>b</sup>, Min Li <sup>b</sup>

<sup>a</sup> Business School, Sichuan University, Chengdu 610065, PR China

<sup>b</sup> Institute of Textiles and Clothing, The Hong Kong Polytechnic University, Hunghom, Kowloon, Hong Kong, China

## a r t i c l e i n f o

Article history: Received 11 August 2011 Received in revised form 28 August 2012 Accepted 21 January 2013 Available online 12 February 2013

Keywords: Retail industry Early sales Sales forecasting Multivariate forecasting

## a b s t r a c t

A sales forecasting problem in the retail industry is addressed based on early sales. An effective multivariate intelligent decision-making (MID) model is developed to provide effective forecasts for this problem by integrating a data preparation and preprocessing module, a harmony search-wrapper-based variable selection (HWVS) module and a multivariate intelligent forecaster (MIF) module. The HWVS module selects out the optimal input variable subset from given candidate inputs as the inputs of MIF. The MIF is established to model the relationship between the selected input variables and the sales volumes of retail products, and then utilized to forecast the sales volumes of retail products. Extensive experiments were conducted to validate the proposed MID model in terms of extensive typical sales datasets from real-world retail industry. Experimental results show that it is statistically signi<sup>fi</sup>cant that the proposed MID model can generate much better forecasts than extreme learning machine-based model and generalized linear model do.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

Retail sales forecasting is estimating the future demand of a retail product, which is essential to sound business planning [1] and is playing a more and more prominent role in dynamic supply chain facing the ever-intensifying global competition [33]. Sales forecasting is the foundation on which company plans are built [20], which is essential to improve a retail company's competition capacity [11]. This paper addresses a multivariate sales forecasting problem, which forecasts the overall sales of a retail product based on its early sales volume.

## 1.1. Sales forecasting

The history of sales forecasting can be traced back to more than 50 years ago [1,32]. Since then a large number of sales forecasting papers have been published [4,5,21,24,32,33], which involves a wide variety of applications in real-world industries, such as print circuit board industry [4], food industry [5] and apparel industry [14].

Some researchers investigated the sales forecasting problem by considering it as univariate time series forecasting problems [23,33]. Their studies utilized input data directly from the historical sales data of time series being forecasted, which are usually based on a basic assumption that the underlying data-generating process of the time series is constant. This assumption is usually invalid in real world since a variety of factors in<sup>fl</sup>uencing product sales, called in<sup>fl</sup>uencing factors, may cause the uncertain change of data pattern, particularly in a dynamic and quick response business environment such as apparel and footwear industry. As a result, the univariate forecasting model cannot handle sudden changes caused by various in<sup>fl</sup>uencing factors such as product attributes and economic environment.

To handle this, some researchers integrated the sales forecasting problem by using multivariate inputs including historical sales and related in<sup>fl</sup>uencing factors [4,5]. Chang et al. [4] addressed the monthly sales forecasting problem to help printed circuit board companies generate effective customer demand forecasts by considering indexes from 4 different domains such as macroeconomic and industry production ones. Chen and Ou [5] investigated a perishable food forecasting problem with the consideration of sales data of target store and neighboring stores as well as weather data. In the multivariate sales forecasting literature, a limited number of in<sup>fl</sup>uencing factors are considered due to reasons such as data unavailability, which perhaps omits important factors and thus weakens forecasting performance.

Although the multivariate forecasting model has potential and advantage to effectively model the relation between sales data and various in<sup>fl</sup>uencing factors, its real-world application is constrained by some issues: (1) a large number of in<sup>fl</sup>uencing factors can in<sup>fl</sup>uence sales, however it is hard to identify the relationships between these factors and <sup>fi</sup>nal sales and (2) it is usual that there are not suf<sup>fi</sup>cient historical data especially when lots of in<sup>fl</sup>uencing factors are considered or the sales of a new product is forecasted.

In the existing literature, most studies dealt with sales forecasting on the basis of historical sales data of products to be forecasted. To forecast the overall sales of new retail products without directly available historical sales data, previous studies usually considered the historical sales of their similar products [7,30,31]. Thomassey and Fiordaliso [30] also investigated the effects of 3 variables (item price, the starting time of the sales and the life span of items) on <sup>fi</sup>nal sales. However, it is hard to identify which past products are similar in forecasting process in industries with large product variety and frequent product changes. These studies also cannot handle future sudden changes caused by in<sup>fl</sup>uencing factors.

It is commonly accepted among retailers that the early sales of a retail product is an excellent indicator of its overall sales [12]. However, little attention has been paid in utilizing early sales to forecast overall sales of retail products so far. The only one work found was conducted by Tanaka [27], which performed long-term sales forecasting based on the early sales and the correlations between short- and long-term accumulated sales within similar products groups. In his work, the forecasting accuracy largely relied on the selection of reference group, which were determined by expert knowledge and thus subjective and probably unreliable. In addition, Tanaka's work has not considered the effects of various in<sup>fl</sup>uencing factors on overall sales, which thus could not handle sales changes caused by these factors such as production attributes and promotion strategy.

In this research, we will aim at addressing a sales forecasting problem for retail products based on their early sales, called early salesbased sales forecasting problem, which forecast the overall sales volume of a retail product in a selling season in terms of its early sales with the consideration of a variety of in<sup>fl</sup>uencing factors instead of using the historical sales data of its similar products. The in<sup>fl</sup>uencing factors include promotion strategy, product attributes (such as selling price, product type and material type), early sales volumes, various economic indices, climate index, etc. The effects of economic factors can be re<sup>fl</sup>ected by various economic indices such as consumer con<sup>fi</sup>dence index (CCI), consumer price index (CPI) and gross domestic product (GDP). However, it keeps unknown if and how these factors in<sup>fl</sup>uence the overall sales volumes of retail products. Among these in<sup>fl</sup>uencing factors, some may be redundant or even irrelevant to the overall sales, which will detract the accuracy of forecasting model and increase its complexity and computational burden. To the best of our knowledge, it is the <sup>fi</sup>rst paper that investigates the effects of various in<sup>fl</sup>uencing factors on overall sales of retail products, and the relations between these factors and overall sales. This research can forecast overall sales of a retail product no matter whether the product has available historical sales data of its similar products.

## 1.2. Techniques for sales forecasting

Techniques for time series forecasting have been widely applied to sales forecasting since most of existing sales forecasting studies were based on the concept of time series. Existing techniques for time series forecasting are generally divided into two groups: classical techniques based on mathematical and statistical models and arti<sup>fi</sup>cial intelligence techniques. Classical techniques used include exponential smoothing [13,29], autoregressive moving average (ARIMA) methods [8,23], Kalman <sup>fi</sup>lter methods [17,35], and so on. Arti<sup>fi</sup>cial intelligence techniques used include expert systems [21,25], fuzzy systems [24], neural network (NN) models [3–5], and hybrid models integrating multiple intelligent techniques [30,33].

These classical techniques cannot be used for the modeling of nontime series. However, the sales forecasting problem investigated in this paper does not use time series of historical sales. The classical techniques thus cannot be used for the investigated problem. Among arti<sup>fi</sup>- cial intelligence techniques, the NN model was the most commonly used one, which has been proved to be universal approximators and can effectively model various time series and non-time series. A number of studies also demonstrate that the NN approach outperforms the classical models due to its capacity of nonlinearity, generalization and universal function approximation [2,8,28].

In recent years, a novel NN, extreme learning machine (ELM), has attracted more and more attentions from forecasting researchers due to its feature of easy to use and fast learning speed [6,26]. The ELM can avoid many dif<sup>fi</sup>culties faced by traditional NN learning algorithms, such as the selections of stopping criteria, learning rate, and learning epochs because of its distinct learning mechanism. On the basis of ELM, Wong and Guo [33] recently developed an effective hybrid intelligence model to provide effective and reliable forecasts for fashion sales series characterized by nonlinearity, seasonality or irregularity, which utilized harmony search (HS) to improve the generalization and forecasting performance of the ELM, and utilized a <sup>fi</sup>netuning process to further improve forecasting accuracy. Their model can outperform ARIMA models and an evolving NN-based forecasting model and an ELM-based model proposed by Sun et al. [26].

In this research, a multivariate intelligent decision-making (MID) model is developed to deal with the investigated sales forecasting problem based on the hybrid intelligence model proposed by Wong and Guo [33]. To decrease the side effects of irrelevant and redundant inputs and the large computational complexity caused by too many input variables, a novel variable selection method, HS-wrapper-based variable selection, is developed in the MID model to select out an appropriate input variable subset from a large number of input variables and explore the relations between overall sales of a retail product and its early sales as well as various in<sup>fl</sup>uencing factors.

The remainder of this paper is organized as follows. In Section 2, the proposed MID model for the investigated sales forecasting problem is presented. Experimental design and results are presented in Section 3. Section 4 further analyzes and discusses the experimental results and the performance and effectiveness of the proposed model. Finally, conclusions and future work are described in Section 5.

## 2. Multivariate intelligent decision-making model for sales forecasting

This research considers the early sales of a retail product and various in<sup>fl</sup>uencing factors as candidate input variables and assumes that there are m input variables in total and n pairs of multi-input– single-output (MISO) samples data are given. Let $( \mathsf { X } _ { \mathrm { i } } , \mathsf { y } _ { \mathrm { i } } )$ denotes the ith input/output data pair (1≤i≤n).

To forecast the overall sales of a retail product in a selling season on the basis of its early sales, this research <sup>fi</sup>rstly identi<sup>fi</sup>es the relationships between m input variables $\left( x _ { i 1 } , x _ { i 2 } , \cdots , x _ { i m } \right)$ of $\mathrm { X _ { i } }$ and the overall sales volume $\mathrm { y _ { i } }$ and selecting out an appropriate subset of input variables from $\mathrm { X _ { i } }$ as the valid inputs, and then establishes an effective model to approximate these relationships in terms of n given samples data. Lastly, the established model is utilized to forecast the sales volumes of other retail products on the basis of their early sales and related input variables. A multivariate intelligent decision-making (MID) model is developed to implement the said processes.

Fig. 1 shows the architecture of the proposed MID model, which is composed of 3 modules, including a data preparation and preprocessing (DPP) module, a HS-wrapper-based variable selection (HWVS) module and a multivariate intelligent forecaster (MIF) module. The DPP module extracts sales data of past products from the point-of-sales database of retailers, and then preprocesses these data for the development and validation of the MID model. The HWVS module selects out the optimal input variable subset from given candidate input variables for pruning redundant and irrelevant ones and providing a better understanding on the inherent characteristic of sales data. The selected input variable subset is then used to establish the MIF for modeling the relationship between the selected input variables and the sales volumes of retail products. Lastly, the established MIF is utilized to forecast the overall sales volumes of retail products.

![](/api/attachments/MSXYGJZC/fulltext/images/81693081be88d7e3b3fb990adef347cc7c7f02f4a982f6433db717bb3283032e.jpg)  
Fig. 1. Architecture of the MID model

## 2.1. Data preparation and preprocessing

A large variety of in<sup>fl</sup>uencing factors can affect the overall sales volume of a retail product in a selling season. The following in<sup>fl</sup>uencing factors are considered as candidate input variables for further extracting the optimal input variable subset.

1) Original selling price: It represents the original selling price of the retail product.

2) Style type: It indicates the type of styles of retail products, such as trouser, T-shirt and coat.

3) Material type: It indicates the type of materials for retail products, such as leather, nylon and polyester.

4) Promotion strategy: Different promotion strategies have effects on sales volumes of retail products. This research classi<sup>fi</sup>es these strategies into A, B, and C categories, which represent the very high, high, and medium degrees respectively at which the strategies can improve sales volumes.

5) Shop quantity: It indicates the number of retail shops that sell the forecasted product.

6) Release date: It indicates which date a retail product starts to be sold in the market. Its value indicates which day it is in a year.

7) Life span: It indicates how many days a retail product is sold in the market.

8) Early sales volumes: It is unclear that how the early sales volume affects the overall sales so far. This research regards the accumulated sales volumes within the <sup>fi</sup>rst 3, 7, 10 and 14 days as 4 candidate input variables.

9) Climate index: It indicates the average temperature of the coming next selling season counting from the release date. Retail products with different release dates have different climate indices.

10) Economic indices: Various available indices re<sup>fl</sup>ecting economic performances, including CCI, CPI, GDP, producer price index (PPI), total retail sales index and price index for ‘clothing and footwear’, are considered as candidate input variables. The value of each economic index takes the average of the index values from its latest 6 months.

To forecast the sales volume of a retail product in a whole selling season, the training samples used need to satisfy the conditions: (1) the life span of each selected retail product should be around a whole selling season; and (2) the average selling prices of retail products could not be much lower than their original selling prices.

Among the candidate input variables described above, some are qualitative ones, including style type, material type and promotion strategy, which need to be changed <sup>fi</sup>rstly to numeric variables for the development of forecasting model. This research uses numeric values to replace the values of each qualitative variable. For example, we use 0, 1 and 2 to replace the 3 categories of promotion strategies, A, B and C.

Data preprocessing has signi<sup>fi</sup>cant effects on the performance of supervised learning models [19] because unreliable training samples probably lead to wrong model parameters. Incomplete data is an inevitable problem in handling most real-world data sources. The missing data need to be interpolated to keep the completeness and the change trend of time series. The missing observation is <sup>fi</sup>lled in by using the mean of its latest two neighboring data in its time series. In addition, data normalization can speed up the training time of NNs by starting the training process for each feature within the same scale. The z-score normalization method [19] is adopted to normalize the input and output variables. The preprocessed data are used as training and test samples of variable selection and MIF modules.

## 2.2. HS-Wrapper-based variable selection

It is crucial to <sup>fi</sup>nd out the optimal variable subset from all candidate input variables because redundant or even irrelevant input variables probably decrease the accuracy of forecasting model and increase its complexity and computational burden. A variety of variable selection approaches have been developed [15], mainly including <sup>fi</sup>lter approach, embedded approach and wrapper approach. The wrapper approach [18] is employed to develop the HWVS module for selecting out the optimal input variable subset because the wrapper approach utilizes learning machine as a black box to score different variable subsets according to their modeling performance, which is regardless of the chosen learning machine. To implement the wrapper approach, 3 issues need to be de<sup>fi</sup>ned, including (1) how to search the space of all possible variable subsets; (2) how to evaluate the forecasting performance of a learning machine (forecaster) and (3) which forecaster to be used. The HWVS module utilizes HS to search the space of all possible variable subsets. The K-fold cross-validation method is utilized to perform performance evaluation. An NN-based forecaster, called MIF that will be described in detail in Section 2.3, is developed to model the mathematical relationships between selected input variables and sales volumes of retail products.

Fig. 2 shows the work<sup>fl</sup>ow of the HWVS module. The steps involved are the same as the corresponding ones of the improved HS algorithm proposed by Mahdavi et al. [22], except for steps 2 and 3, which are detailed as follows.

Step 2: Initialize the harmony memory.

The HM is generated randomly, in which each HM member (called a harmony, an solution individual), s, represents a feasible input variable subset. s is denoted by a binary string, $\mathsf { S } = [ s _ { 1 } , s _ { 2 } , . . . , s _ { C } ] .$ s is a binary value, which indicates that the ith input variable is selected if ${ \bf \dot { \boldsymbol { s } } } _ { i } = 1 ;$ ; otherwise it is not.

Step 3: Calculate objective function value of each harmony in terms of cross-validation.

Minimizing the forecasting error is the most important objective of forecasting. The objective function value OF of a harmony is represented by a function of forecasting error. Based on the K-fold cross-validation method, the objective function value OF is calculated by evaluating the forecasting performance generated by the corresponding input variable subset. The detailed procedures to obtain OF are described below:

![](/api/attachments/MSXYGJZC/fulltext/images/efd70d365eb8f6b59460e00a891ed2c6d8dadac289b6f257f769eddf67a8a716.jpg)  
Fig. 2. Flowchart of the HWVS module.

(1) The normalized training samples, generated in Section $2 . 1$ are randomly partitioned into K sample subsets, numbered 1 to K. Set $i = 1$

(2) The ith sample subset is used as validation data for testing the forecaster, and the remaining $K - 1$ subsample sets are used as training data to train and establish the forecaster (Section 2.3 will describe how the forecaster is implemented in detail). The mean squared error of forecasting outputs of these validation data is denoted by $M _ { i }$ (3) $i = i + 1$ . Go to (4) if $i > K ,$ otherwise go to (2).

(4) $O F = \left( \sum _ { i = 1 } ^ { K } M _ { i } \right) / K .$

The less the objective function value, the better solution the harmony represents.

## 2.3. Multivariate intelligent forecaster

The output of the MIF is the <sup>fi</sup>nal forecast of overall sales volume of a retail product. The input variable subset, generated by the HWVS module, is adopted as the input variables of the MIF. The hybrid intelligent forecaster, developed by Wong and Guo [33], is modi<sup>fi</sup>ed to implement the MIF module. Fig. 3 shows the <sup>fl</sup>owchart of the MIF.

The MIF generates the <sup>fi</sup>nal forecast on the basis of the forecasting outputs generated by an HS-ELM-based NN. The NN is run repeatedly $N _ { \mathrm { m a x } \ h l }$ times so as to decrease the randomicity of NN outputs. In each run, the NN has a speci<sup>fi</sup>ed number (i) of hidden neurons, which increases successively from 1 $\mathrm { t o } N _ { \mathrm { m a x } h l } .$ The NN is used to approximate the relationship between the selected input variables and the sales volumes of retail products. The output of the NN needs to be de-normalized to get the initial forecasts of sales volumes because the input and output of the HS-ELM-based NN are normalized values. These initial forecasts, generated by HS-ELM-based NNs with different number of hidden neurons, can be unreasonable because NNs may be over<sup>fi</sup>tted. They are thus input into the heuristic <sup>fi</sup>ne-tuning process for generating the <sup>fi</sup>nal forecast of sales volume.

The heuristic <sup>fi</sup>ne-tuning process is <sup>fi</sup>rstly utilized to identify and eliminate unreasonable initial forecasts generated by over<sup>fi</sup>tted NNs. The mean of remaining reasonable initial forecasts is the <sup>fi</sup>nal sales forecast. The processes to identify unreasonable forecasts are described as follows. Let outNN denote the denormalized NN output. MinOutS and MaxOutS denote the minimal and maximal values of actual outputs of training samples. The initial forecast is considered as unreasonable if one of the following conditions is met:

![](/api/attachments/MSXYGJZC/fulltext/images/9dccb8f5119587830a4cd86dd01085662df4ca7d53c3855f27836e4f1a80a8e2.jpg)  
Fig. 3. Flowchart of the MIF.

(1) $o u t N N { > } k _ { 1 } \cdot M a x O u t S ,$

(2) outNNbMinOutS/k<sub>2</sub>

where $k _ { 1 } ,$ k are pre-given constants greater than 1 and less than 2. The greater the standard deviation of the training samples' outputs is, the greater the values of $k _ { 1 }$ and $k _ { 2 }$ are. We set both $k _ { 1 }$ and $k _ { 2 }$ are equal to 2. The remaining forecasts except unreasonable ones are then averaged as the <sup>fi</sup>nal sales forecasts.

## 3. Numerical experiments

Extensive experiments were conducted to evaluate the forecasting performance of the proposed MID model in terms of real-world sales data of apparel products, which forecasted the overall sales volumes of various retail products based on their early sales. This section presents how these experiments were conducted and the results of 4 experiments using typical sample data. To validate the general forecasting performance of the MID model, these experiments investigate sales forecasting tasks in different regions with a large number of retail shops and products. Each of the <sup>fi</sup>rst 3 experiments considers different in<sup>fl</sup>uencing factors and candidate input variables, in which 10 sets of different datasets are utilized respectively to evaluate and compare the forecasting performances generated by the proposed model and several compared models. Each dataset consists of a speci<sup>fi</sup>ed number of sample pairs, in which the last 3 input–output sample pairs are utilized for out-of-sample test whereas the others are training samples. In experiment 4, 3 sets of datasets with more sample pairs are investigated, which are formed by combining the datasets in experiments 1–3 respectively. In each of the 3 datasets, the last 10 input–output samples are utilized for out-of-sample test. The 33 sets of datasets used in the 4 experiments contain a large amount of samples. Due to page limit, these datasets are placed on Internet (http://myweb.polyu.edu.hk/\~tcguozx/ datasets/).

## 3.1. Experimental design

Real sales data were collected from one of the largest fashion retail companies in Hong Kong and Mainland China, which include sales data of fashion products from different retail shops and cities from 01/2007 through 12/2009. The life span of each selected retail product is greater than 160 days and less than 200 days. Data of available economic indices of each city can be collected from the Municipal Statistics Bureau of this city. The average selling prices of selected product is greater than 80% of its original price. Experiments have not considered the effects of 3 in<sup>fl</sup>uencing factors, including style type, material type and promotion strategy due to their data unavailability and incompleteness.

## 3.1.1. Forecasting models used for comparison

This research conducted experiments from two aspects: (1) the forecasting performance of the proposed model was compared with 2 multivariate models, including the improved ELM (IELM) model and the generalized linear model [10]; (2) to observe the bene<sup>fi</sup>ts brought by the HWVS module, this research also compared the performances of the 3 models using all candidate input variables as the inputs of the MIF module and using only the selected input variables, generated by the HWVS module, as inputs.

The IELM model is developed based on the ELME model proposed by Sun et al. [26]. Wong and Guo [33] have demonstrated that the forecasting performance of the ELME model is inferior to that of the HS-ELM-based model. It is one of the main reasons that the ELME model lacks of effective mechanism to determine appropriate input weights of NNs and the number of appropriate hidden neurons. It is well-known that the number of hidden neurons has large effects on NN performances [36]. To decrease the randomicity of NN outputs generated by the ELME model with a speci<sup>fi</sup>ed number of hidden neurons, in the IELM model, we <sup>fi</sup>rstly obtain $N _ { \mathrm { m a x } \ h l }$ forecasting outputs by repeatedly running the ELME models with different number of hidden neurons from 1 to $N _ { \mathrm { m a x } \ h l } ;$ these forecasting outputs are then input into the heuristic <sup>fi</sup>ne-tuning process for generating the <sup>fi</sup>nal forecasting output of the IELM model.

The generalized linear model (GLM) was developed by Nelder and Wedderburn [10], which is a <sup>fl</sup>exible generalization of various least squares regression models, including linear regression, logistic regression and Poisson regression. To use generalized linear models, we assume that the observations (sales volumes of retail products) obey a normal distribution.

## 3.1.2. Accuracy measures

No accuracy measure is generally applicable to all forecasting tasks due to various forecasting objectives as well as data scales and patterns [9,16]. To reduce possible bias generated by one single accuracy measure, this research utilized three measures of forecast accuracy, including root mean square error (RMSE), mean absolute percentage error (MAPE) and mean absolute error (MAE), to evaluate the performance of each forecasting result generated by the MIF.

Let $Y _ { t }$ denote the observation at time t and $F _ { t }$ denote the forecast of $Y _ { t } .$ Then de<sup>fi</sup>ne the forecast error $e _ { t } { = } Y _ { t } { - } F _ { t }$ . The three accuracy measures are formulated as follows:

$$
\begin{array}{l} (1) R M S E = \sqrt {\text {mean} (e ^ {2})} \\ (2) M A P E = \text {mean} \left(\left| e _ {t} / Y _ {t} \right|\right) \times 100 \% \\ (3) M A E = \text {mean} (\left| e \right|). \end{array}
$$

## 3.2. Experiment 1

In this experiment, each dataset consists of 41 sample pairs. The output of each sample is the actual overall sales volume of a fashion product in all retail shops of the investigated company in city A. Each sample has 14 candidate inputs, including original selling price, shop quantity, release date, life span, 4 early sales volumes, climate index and 5 economic indexes. The economic indexes include CPI, GDP, PPI, total retail sales index and price index for ‘clothing and footwear’. On the basis of available training samples, the subset of input variables, generated by the HWVS module, comprises 3 variables, including shop quantity, accumulated sales volume in the <sup>fi</sup>rst 10 days and climate index.

The comparisons of actual and forecasted outputs are shown in Figs. 4–6, each of which shows the forecasting outputs, generated by different models, of a test sample in each dataset. The solid line plots the actual sales volumes of different fashion products in all retail shops of the investigated company. The forecasts generated by different models are represented by different signs. The signs ‘∗’, ‘x’, ‘□’, ‘+’, ‘○’ and ‘·’ represent, respectively, the forecasts generated by the GLM with all candidate inputs (GLM1), the GLM with selected inputs (GLM2), the IELM model with all candidate inputs (IELM1), the IELM model with selected inputs (IELM2), the MIF with all candidate inputs (MID1) and the MIF with selected inputs (MID model, MID2). It can be clearly found from Figs. 4 to 6 that the proposed MID model generates forecasts of sales volumes closer to the actual values.

On the basis of the forecasting outputs shown in Figs. 4–6, we further evaluate the performance change generated by the selected input variable subset and compare the forecasting results generated by the GLM, the IELM model and the MID model. Fig. 7 shows the summary comparison result, in which sub<sup>fi</sup>gures (a)–(c) represent the results respectively under accuracy measures MAE, MAPE and RMSE. Each sub<sup>fi</sup>gure contains 6 bars named B1–B6. The upper and lower parts of the <sup>fi</sup>rst 5 bars, B1–B5, show the number of datasets getting better forecasting performances, generated respectively by GLM2 and GLM1, IELM2 and IELM1, MID2 and MID1, MID1 and IELM1, MID2 and IELM2. The 6th bar shows the results generated by MID2, IELM2 and GLM2, which shows, from top to bottom, the number of datasets for which the 3 models generate best performances respectively. For identi<sup>fi</sup>cation purpose, we use a very small part in a bar to indicate 0.

![](/api/attachments/MSXYGJZC/fulltext/images/dc2ad145102b6f568cd25a977abcd8a73064a2be4247202eebdfd9caaa1e859c.jpg)  
Fig. 4. Output comparison of the 1st test sample in each dataset

It can be clearly found from bars B1–B3 that the three models with the selected variable inputs (GLM2, IELM2 and MID2) can generate superior performances to their corresponding models with all candidate inputs whichever accuracy measures are used. For example, if MAE is used as the accuracy measure, GLM2, IELM2 and MID2 generate better forecasting performances for 6, 9 and 8 datasets whereas GLM1, IELM1 and MID1 generate better forecasting performances for 4, 1 and 2 datasets. Bars B4 and B5 indicate that the MID1 and MID2 generate better forecasts than IELM and IELM2. The results of B6 indicate that MID2 usually generates better forecasting results than IELM2 and GLM2 whichever accuracy measure is used except for generating an inferior MAPE result for one dataset to IELM2, which shows that the proposed MID model (MID2) exhibits much superior performance to IELM2 and GLM2 in this experiment.

![](/api/attachments/MSXYGJZC/fulltext/images/d11fbbd2e0d638bbc198d9149940d52a2c42e1ac4338b9cc6c70e734dc2c4e2b.jpg)  
Fig. 5. Output comparison of the 2nd test sample in each dataset

![](/api/attachments/MSXYGJZC/fulltext/images/38296b32e0685b5a4d870e33b902e7a59523fdd0fd1e163d38210a9333addfbe.jpg)  
Fig. 6. Output comparison of the 3rd test sample in each dataset.

## 3.3. Experiment 2

Each dataset consists of 35 sample pairs in this experiment. The output of each sample is the actual sales volume of a fashion product in a retail shop of the investigated company in city A. Each sample includes 13 candidate input variables, which are the same to variables in experiment 1 except for excluding the input ‘shop quantity’. The HWVS module generates the subset of 7 input variables from these 13 candidate variables, which include life span, sales volumes in the <sup>fi</sup>rst 3, 7 and 10 days, climate index, total retail sales index and price index for ‘clothing and footwear’.

Due to the page limit, this paper does not present the comparison results of actual and forecasted outputs in experiments 2–4. Similar to Fig. 7, Fig. 8 shows the further summary result of this experiment by further comparing the forecasting results generated by different models. The results from bars B1–B3 show that GLM2 and IELM2 can generate slightly better forecasting performances than GLM1 and IELM1 while MID2 generates much better performance than MID does since MID2 generates superior forecasting results for 8, 8 and 9 datasets, respectively, in terms of 3 different accuracy measures. The results from bars B4–B6 show that (1) MID1 generates better forecasting results than IELM for at least 7 datasets in terms of different accuracy measures; (2) MID2 always generates better forecasting results than IELM2 and GLM2 for all 10 datasets whichever accuracy measure is used. These results show that the proposed MID model exhibits much better forecasting performance than other models do in this experiment.

## 3.4. Experiment 3

Each dataset consists of 32 sample pairs in this experiment. The output of each sample is the actual sales volume of a fashion product in a retail shop of the investigated company in city B. Each sample includes 9 candidate input variables, including original selling price, release date, life span, 4 early sales volumes in a retail shop, climate index and total retail sales index. In experiments 1–2, 5 economic indexes were included. However, this experiment used another factor because the values of the 5 factors could not be obtained effectively due to incomplete information released by relevant government department and organization. On the basis of available training samples, the subset of input variables, generated by the HWVS module, contains original selling price, life span, sales volume in the <sup>fi</sup>rst 14 days and total retail sales index.

Fig. 9 shows the summary result of this experiment. The results from bars B1–B3 demonstrate that GLM2, IELM2 and MID2 can generate obviously better forecasting performance than their corresponding models with all candidate inputs. For instance, GLM2 and IELM2 generate superior forecasting results for 8 and 9 datasets respectively whichever accuracy measure is used. Bars B4 indicate that the MID1 generate better forecasting results than IELM1 for 9 datasets. In addition, bars B5 and B6 indicate that MID2 generate superior forecasting results to IELM2 and GLM2 for at least 9 datasets whichever accuracy measure is used. These results also show that the proposed MID model exhibits much superior forecasting performance to other models in this experiment.

## 3.5. Experiment 4

3 sets of datasets with more observations are utilized to evaluate the forecasting performances of different models. The 3 datasets consists of 76, 65 and 60 observations respectively. The last 10 observations of each dataset are used for out-of-sample test. Table 1 shows the forecasting results for the 3 datasets in terms of different accuracy measures. It is clear that, in this experiment, MID2 generates the best forecasting performances (out-of-sample test) and the second best <sup>fi</sup>tting performances (in-sample test, only inferior to MID1).

The experimental results above were obtained based on the following setting: the values of parameters of HS algorithms were shown in Table 2, in which $P A R _ { \mathrm { m i n } }$ and $P A R _ { \mathrm { { m a x } } }$ denote the minimum and the maximum of PAR, and $b w _ { \mathrm { m i n } }$ and $b w _ { \mathrm { m a x } }$ denote the minimum and the maximum of bw. In addition, the maximum number $N _ { \operatorname* { m a x } h l }$ of hidden neurons is equal to 5. The activation function $g ( x )$ of NN is the sigmoidal function, i.e., $\begin{array} { r } { g ( x ) = \frac { 1 } { 1 + e ^ { - x } } } \end{array}$ . 10-fold cross-validation method was used in the HS-wrapper module.

![](/api/attachments/MSXYGJZC/fulltext/images/a927a85100b6f055510d1684ef42e4d937ef033eb23c3ee462e45cceba8d1980.jpg)

![](/api/attachments/MSXYGJZC/fulltext/images/7139d0527d0fcd9b107d9fb704aae17b11897a9811e4abd971b318e4a542cd84.jpg)  
Fig. 7. Comparison of forecasting results (Experiment 1).

![](/api/attachments/MSXYGJZC/fulltext/images/ef36e5fcc20eba6faf7a7f90d602434134bd1b50f059f2276223fabdc91dc629.jpg)

![](/api/attachments/MSXYGJZC/fulltext/images/89b68df197fd41f1d329916ca50312369c9e2c034b01f7535085f00443fe3502.jpg)

![](/api/attachments/MSXYGJZC/fulltext/images/fa8630e88feb449a7f984b57c4d98f8520e8bc40892853141c118bc27f2fe53a.jpg)

![](/api/attachments/MSXYGJZC/fulltext/images/5f11e63d09b974dadcb5d4ac545736d76309b5c09bc6551b74a4de15827acf44.jpg)  
C) RMSE  
Fig. 8. Comparison of forecasting results (Experiment 2).

## 4. Discussion

This section presents an in-depth discussion on the forecasting performance of the proposed MID model. Further analysis is <sup>fi</sup>rstly conducted to validate the superiority of the proposed model over other models based on the experimental results presented in Section 3. The performance of HWVS model and its effects on <sup>fi</sup>nal forecasting results are then discussed.

## 4.1. Further performance comparison and analysis

Extensive experiments were presented to validate the forecasting performance of the proposed MID model in Section 3, in which 33 different datasets were investigated. These datasets involve different cities and a large variety of retail shops and retail products, and can re<sup>fl</sup>ect typical sales patterns in retailing.

On the basis of the experimental results described in Section 3, Table 3 shows a summary comparison between the proposed MID model (MID2) and 5 other compared models. In this table, the <sup>fi</sup>rst column shows the number of datasets for which MID2 generates best forecasting performance compared with other 5 models, and the second to <sup>fi</sup>fth columns show the comparison results between MID2 with MID1, IELM2, IELM1, GLM2 and GLM1 respectively. In this table, the <sup>fi</sup>rst value of each cell represents the results of out-of-sample test while the value in the bracket represents the result of in-sample test. Taking MAE as an example, MID2 generates best forecasts in all 6 models for 20 datasets in terms of out-of-sample test, and for 15 datasets in terms of in-sample test. It can be found from this table, MID2 generates much higher training accuracies than IELM2, IELM1, GLM2 and GLM1. However, it can only outperform MID1 for 13 datasets in terms of in-sample test. It is because MID1 has more inputs and more complicated network connections, which can bring higher <sup>fi</sup>tting (training) accuracy although they are prone to over<sup>fi</sup>tting and generating poor forecasts.

We further used p-values to measure the forecasting results generated by different models. This research uses $A \equiv ( o r \mathrm { \succsim } ) B$ to represent that A generates better forecasting accuracies for $p \%$ (or more than $p \% , p { \geq } 5 0 )$ of datasets than B does. For example, $M I D 2 \equiv O t h e r M o d e l s$ represents that MID2 generates higher forecasting accuracies for $p \%$ of datasets than other compared models do. To further analyze the superiority of MID2 over other models, we de<sup>fi</sup>ne four null hypotheses $( \mathrm { H A } _ { 0 } , \mathrm { H B } _ { 0 } , \mathrm { H C } _ { 0 }$ and $\mathrm { H D } _ { 0 } )$ and their corresponding alternative hypoth eses below:

![](/api/attachments/MSXYGJZC/fulltext/images/76f2b799dbe03af80cb08c4168f63b62c9ed12e880b72ce44586c38f13edb5d0.jpg)

$$
\mathrm{HA} _ {0}: \text { MID2 } \equiv \text { OtherModels }; \mathrm{HA} _ {1}: \text { MID2 } \succ \text { OtherModels }; p = 5 5.
$$

$$
\mathrm{HB} _ {0}: M I D 2 \equiv M I D 1; \mathrm{HB} _ {1}: M I D 2 \succ M I D 1; p = 6 5.
$$

$$
\mathrm{HC} _ {0}: M I D 2 \equiv I E L M 1; \mathrm{HC} _ {1}: M I D 2 \succ I E L M 1; p = 8 0.
$$

$$
\mathrm{HD} _ {0} \colon M I D 2 \equiv G L M 2; \mathrm{HD} _ {1} \colon M I D 2 \succ G L M 2; p = 9 0.
$$

To validate if the proposed model is signi<sup>fi</sup>cantly superior to other models whichever accuracy measure is employed, we calculate the p-value of each hypothesis by using the minimal number of datasets shown in the corresponding column of Table 3. That is, we take numbers 23, 26, 31 and 33 to calculate the p-values of the four null hypotheses respectively. The four p-values are 0.045, 0.048, 0.023 and 0.028 respectively, which are all less than 0.05. We thus reject these hypotheses at the 5% signi<sup>fi</sup>cance level. Take null hypotheses $\mathrm { H A } _ { 0 }$ as an example. There is a 95% chance of accepting the alternative hypothesis $\mathrm { H A } _ { 1 }$ That is, for more than 55% of datasets, MID2 generate the best forecasting accuracies among 6 compared models at the 5% signi<sup>fi</sup>cance level. In addition, the results of rejecting hypotheses $\mathrm { H B } _ { 0 } – \mathrm { H D } _ { 0 }$ show that, for more than 65%, 80% and 90% of datasets, MID2 generate higher forecasting accuracies than MID1, IELM1 (IELM2), and GLM1 (GLM2) models at the 5% signi<sup>fi</sup>cance level. The results of statistical tests indicate that it is statistically signi<sup>fi</sup>cant that the proposed MID model (MID2) can generate much better forecasting performances than IELM models and GLMs do in terms of three accuracy measures (MAE, MAPE and RMSE).

![](/api/attachments/MSXYGJZC/fulltext/images/fb0b154a8ec310028e760526507432ab36ff033a8a76351b8fa808086374d462.jpg)  
Fig. 9. Comparison of forecasting results (Experiment 3).

![](/api/attachments/MSXYGJZC/fulltext/images/b37a38b9cba9e8f9e87a0b2417eea532c405671b84d924cc7a577f64e4fa5096.jpg)

Table 1  
Performance comparison of different models for larger-size samples

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">MID2</td><td colspan="2">MID1</td><td colspan="2">IELM2</td><td colspan="2">IELM1</td><td colspan="2">GLM2</td><td colspan="2">GLM1</td></tr><tr><td>In sample</td><td>Out of sample</td><td>In sample</td><td>Out of sample</td><td>In sample</td><td>Out of sample</td><td>In sample</td><td>Out of sample</td><td>In sample</td><td>Out of sample</td><td>In sample</td><td>Out of sample</td></tr><tr><td rowspan="3">Data of Exp. 1</td><td>MAE</td><td>304.2</td><td>782.4</td><td>231.7</td><td>889.1</td><td>730.7</td><td>825.0</td><td>909.8</td><td>529.0</td><td>1158.8</td><td>1421.7</td><td>809.8</td><td>365.3</td></tr><tr><td>MAPE</td><td>23.8%</td><td>24.3%</td><td>27.3%</td><td>33.6%</td><td>69.4%</td><td>30.4%</td><td>98.4%</td><td>42.4%</td><td>39.3%</td><td>333.7%</td><td>27.5%</td><td>85.8%</td></tr><tr><td>RMSE</td><td>637.8</td><td>1372.3</td><td>325.8</td><td>1512.3</td><td>1318.3</td><td>1300.7</td><td>1623.3</td><td>691.8</td><td>1981.7</td><td>2019.3</td><td>1316.5</td><td>566.1</td></tr><tr><td rowspan="3">Data of Exp. 2</td><td>MAE</td><td>39.8</td><td>35.1</td><td>44.0</td><td>60.4</td><td>49.9</td><td>126.3</td><td>127.6</td><td>70.3</td><td>126.9</td><td>119.3</td><td>101.0</td><td>145.2</td></tr><tr><td>MAPE</td><td>18.3%</td><td>14.0%</td><td>21.3%</td><td>27.8%</td><td>19.5%</td><td>46.0%</td><td>45.8%</td><td>28.8%</td><td>80.8%</td><td>75.0%</td><td>64.4%</td><td>91.3%</td></tr><tr><td>RMSE</td><td>53.7</td><td>46.5</td><td>56.6</td><td>73.3</td><td>70.3</td><td>214.6</td><td>226.2</td><td>77.7</td><td>178.7</td><td>143.9</td><td>145.4</td><td>228.5</td></tr><tr><td rowspan="3">Data of Exp. 3</td><td>MAE</td><td>39.1</td><td>64.8</td><td>56.1</td><td>67.6</td><td>238.1</td><td>117.8</td><td>278.4</td><td>120.1</td><td>155.7</td><td>207.3</td><td>222.0</td><td>215.0</td></tr><tr><td>MAPE</td><td>16.8%</td><td>27.5%</td><td>22.2%</td><td>30.2%</td><td>85.2%</td><td>56.1%</td><td>96.3%</td><td>54.5%</td><td>142.8%</td><td>97.8%</td><td>203.7%</td><td>101.4%</td></tr><tr><td>RMSE</td><td>57.6</td><td>88.9</td><td>105.1</td><td>89.8</td><td>363.1</td><td>160.9</td><td>435.1</td><td>161.7</td><td>248.9</td><td>390.3</td><td>279.1</td><td>292.9</td></tr></table>

## 4.2. Performance and effects of HWVS module

We further compare the forecasting results generated by different forecasting models with/without the usage of HWVS module, including GLM2/GLM1, IELM2/IELM1, and MID2/MID1. Take the forecasting results in terms of accuracy criterion MAE as an example. GLM2 can generate superior forecasts to GLM1 for 22 datasets while IELM2 (MID2) can generate superior forecasts to IELM1 (MID1) for 26 (25) datasets. p-Values are utilized to further measure these forecasting results in terms of MAE. We de<sup>fi</sup>ne three null hypotheses (HE , HF , and HG ) and their corresponding alternative hypotheses below:

$$
\mathrm{HE} _ {0}: G L M 2 \equiv G L M 1; \mathrm{HA} _ {1}: G L M 2 \succ G L M 1; p = 5 0.
$$

$$
\mathrm{HF} _ {0}: I E L M 2 \equiv I E L M 1; \mathrm{HB} _ {1}: I E L M 2 \succ I E L M 1; p = 6 0.
$$

$$
\mathrm{HG} _ {0} \colon M I D 2 \equiv M I D 1; \mathrm{HC} _ {1} \colon M I D 2 \succ M I D 1; p = 6 0.
$$

The p-values under these hypotheses are 0.028, 0.014, and 0.032 respectively, which are all less than 0.05. We thus reject these hypotheses at the 5% signi<sup>fi</sup>cance level. That is, for more than 50% of datasets, GLM2 generates higher forecasting accuracies than GLM1 does at the 5% signi<sup>fi</sup>cance level. For more than 60% of datasets, IELM2 and MID2 generate higher forecasting accuracies than IELM1 and GLM1, respectively, at the 5% signi<sup>fi</sup>cance level. These indicate that it is statistically signi<sup>fi</sup>cant that the models with the HWVS module can generate better forecasts than corresponding models without the HWVS module. The same conclusion could be drawn when other accuracy criteria were used. It shows that the HWVS module is effective to improve the forecasting accuracy.

In the experiments described in Section 3, different candidate inputs were used due to different data availabilities in cities involved. In each experiment, we searched for the optimal input variable subsets separately because each experiment used different candidate input variables and different sales patterns. The input variable subsets, generated by the HWVS module, contain 3, 7, and 4 variables in experiments 1–3, which are selected out from 15, 13 and 9 candidate variables respectively. Different optimal input variable subsets were then obtained. That is because different intrinsic relations exist between input data (in<sup>fl</sup>uencing factors) and output data (overall sales) in different cases investigated in corresponding experiments. Actually, it depends on sample data whether an in<sup>fl</sup>uencing factor needs to be used as a <sup>fi</sup>nal input variable and incorporated into the forecasting model. According to the variable selection results, the factors, included in the optimal input variable subset, need to be incorporated. It can be found from experimental results that the forecasting performance was not deteriorated by the exclusion of several variables. It indicates that the available in<sup>fl</sup>uencing factors are enough to re<sup>fl</sup>ect the corresponding input/output relations in each experiment. It also indicates that the proposed model, including the HWVS module and the MIF module, is effective to approximate the corresponding input/output relations and generate reliable forecasts in these cases.

Table 2  
Parameters of HS algorithms used in experiments.

<table><tr><td></td><td>HMS</td><td>NI</td><td>HMCR</td><td> $PAR_{min}$ </td><td> $PAR_{max}$ </td><td> $bw_{max}$ </td><td> $bw_{max}$ </td><td>PerHM</td></tr><tr><td>HS-wrapper</td><td>50</td><td>100</td><td>0.95</td><td>0.45</td><td>0.99</td><td>1.E-06</td><td>4</td><td>90%</td></tr><tr><td>HS-ELM</td><td>100</td><td>200</td><td>0.95</td><td>0.45</td><td>0.99</td><td>1.E-06</td><td>4</td><td>90%</td></tr></table>

In addition, the proposed HWVS module effectively reduced the number of input variables whichever candidate input variables were utilized, which resulted in less model parameters and was helpful to decrease the complexity of forecaster so as to improve the generalization performance of the forecaster.

## 5. Conclusions

This paper addresses the early sales-based retail forecasting problem in the retail industry, which is helpful for related retail enterprises to make scienti<sup>fi</sup>c and reliable replenishment forecasting and thus improve the performance and ef<sup>fi</sup>ciency of their retail supply chains.

An effective MID model was developed to handle the problem investigated, in which a DPP module, a HWVS module and a MIF were integrated. The DPP module is responsible for capturing and preprocessing sales data of past products and values of related candidate input variables for the development and validation of the MID model. The HWVS module selects out the optimal input variable subset from given candidate inputs. Using the selected input variables as the inputs of MIF, the MIF is then established to model the relationship between the selected input variables and the sales volumes of retail products. Lastly, the established MIF is utilized to forecast the sales volumes of retail products.

Extensive experiments were conducted to evaluate the proposed MID model in terms of a large variety of typical datasets from realworld retail data. The experimental results indicated that the MID model can tackle the investigated multivariate sales forecasting problem effectively and it is statistically signi<sup>fi</sup>cant that the proposed model could provide much superior performance over the IELM model and the generalized linear model. Experimental results also showed that the HWVS module can effectively <sup>fi</sup>nd the appropriate variable input by eliminating reluctant and irrelevant inputs whichever candidate input variables are used, which results in less model parameters and higher forecasting accuracy. These results show that the proposed model is effective and widely applicable to multivariate sales forecasting problems. In addition, the proposed MID model does not rely on the time series of historical sales data of products to be forecasted, which can thus provide overall sales forecasts for both old and new retail products.

Table 3  
Number of datasets for which MID2 generates better forecasting (training) results

<table><tr><td></td><td>5 other models</td><td>MID1</td><td>IELM2</td><td>IELM1</td><td>GLM2</td><td>GLM1</td></tr><tr><td>MAE</td><td>23 (17)</td><td>26 (17)</td><td>32 (33)</td><td>32 (33)</td><td>33 (33)</td><td>33 (33)</td></tr><tr><td>MAPE</td><td>26 (15)</td><td>28 (16)</td><td>32 (33)</td><td>32 (33)</td><td>33 (29)</td><td>33 (30)</td></tr><tr><td>RMSE</td><td>24 (15)</td><td>28 (15)</td><td>31 (33)</td><td>31 (33)</td><td>33 (33)</td><td>33 (33)</td></tr></table>

Future research will focus on utilizing the proposed MID model to handle other multivariate forecasting problems, such as multivariate time series forecasting problem, and compare the performance of proposed model with multivariate time series forecasting model such as autoregressive moving average model with exogenous inputs. In addition, it is also a worthwhile research direction to compare the effects of different variable selection methods on the forecasting performance of MID model, and further improve the generalization performance and the computational ef<sup>fi</sup>ciency of MID model by utilizing partially connected NNs [34] to replace the HS-ELM-based NN.

## Acknowledgement

The authors acknowledge the supports from Sichuan University, the Fundamental Research Funds for the Central Universities (Grant No. SKYB201301) and the National Natural Science Foundation of China (Grant Nos 71020107027, 71172197).

[1] J.B. Boulden, Fitting the sales forecast to your <sup>fi</sup>rm, Business Horizons 1 (1958) 65–72

[2] Q. Cao, M. Parry, Neural network earnings per share forecasting models: a comparison of backward propagation and the genetic algorithm, Decision Support Systems 47 (2009) 32–41.

[3] R. Carbonneau, G. Kersten, R. Vahidov, Pairwise issue modeling for negotiation counteroffer prediction using neural networks, Decision Support Systems 50 (2011) 449–459.

[4] P. Chang, Y. Wang, C. Tsai, Evolving neural network for printed circuit board sales forecasting, Expert Systems with Applications 29 (2005) 83–92.

[5] F.L. Chen, T.Y. Ou, Gray relation analysis and multilayer functional link network sales forecasting model for perishable food in convenience store, Expert Systems with Ap plications 36 (2009) 7054–7063

[6] F.L. Chen, T.Y. Ou, Sales forecasting system based on Gray extreme learning machine with Taguchi method in retail industry, Expert Systems with Applications 38 (2011) 1336–1345.

[7] C.-C. Chern, et al., Designing a decision-support system for new product sales forecasting, Expert Systems with Applications 37 (2010) 1654–1665.

[8] C. Chu, G. Zhang, A comparative study of linear and nonlinear models for aggregate retail sales forecasting, International Journal of Production Economics 86 (2003) 217-231.

[9] J. De Gooijer, R. Hyndman, 25 years of time series forecasting, International Journal of Forecasting 22 (2006) 443–473.

## References

[10] A.J. Dobson, A.G. Barnett, Introduction to Generalized Linear Models, Chapman & Hall/CRC, Boca Raton, Florida, USA, 2008.

[11] R. Fildes, R. Hastings, The organization and improvement of market forecasting The Journal of the Operational Research Society 45 (1994) 1–16.

[12] M.L. Fisher, A. Raman, A.S. McClelland, Rocket science retailing is almost here — are you ready? Harvard Business Review 78 (2000) 115–124.

[13] E. Gardner, Exponential smoothing: The state of the art — part II, International Journal of Forecasting 22 (2006) 637–666.

[14] Z.X. Guo, et al., Applications of arti<sup>fi</sup>cial intelligence in the apparel industry: a review, Textile Research Journal 81 (2011) 1871–1892.

[15] I. Guyon, A. Elisseeff, An introduction to variable and feature selection, Journal of Machine Learning Research 3 (2003) 1157–1182.

[16] R. Hyndman, A. Koehler, Another look at measures of forecast accuracy, International Journal of Forecasting 22 (2006) 679–688.

[17] M. Jacobi, D. Karimanzira, C. Ament, Water demand forecasting using Kalman <sup>fi</sup>ltering, Proceedings of the 16th IASTED International Conference on Applied Simulation and Modelling, 2007, pp. 199–202.

[18] R. Kohavi, G. John, Wrappers for feature subset selection, Arti<sup>fi</sup>cial Intelligence 97 (1997) 273–324.

[19] S.B. Kotsiantis, D. Kanellopoulos, P.E. Pintelas, Data preprocessing for supervised learning, International Journal of Computer Science 1 (2006).

[20] G. Lancaster, P. Reynolds, Marketing: Made Simple, Elsevier, Oxford, U.K., 2002

[21] T. Lo, An expert-system for choosing demand forecasting techniques, International Journal of Production Economics 33 (1994) 5–15.

[22] M. Mahdavi, M. Fesanghary, E. Damangir, An improved harmony search algorithm for solving optimization problems, Applied Mathematics and Computation 188 (2007) 1567–1579.

[23] S. Makridakis, M. Hibon, ARMA models and the Box–Jenkins methodology, Journal of Forecasting 16 (1997) 147–163.

[24] H. Sakai, et al., Development of a fuzzy sales forecasting system for vending machines, Computers and Industrial Engineering 36 (1999) 427–449.

[25] P. Smith, S. Husein, D. Leonard, Forecasting short term regional gas demand using an expert system, Expert Systems with Applications 10 (1996) 265–273.

[26] Z. Sun, et al., Sales forecasting using extreme learning machine with applications in fashion retailing, Decision Support Systems 46 (2008) 411–419.

[27] K. Tanaka, A sales forecasting model for new-released and nonlinear sales trend products, Expert Systems with Applications 37 (2010) 7387–7393.

[28] Z. Tang, C. Dealmeida, P. Fishwick, Time-series forecasting using neural networks vs Box–Jenkins methodology, Simulation 57 (1991) 303–310.

[29] J. Taylor, Forecasting daily supermarket sales using exponentially weighted quantile regression, European Journal of Operational Research 178 (2007) 154–167.

[30] S. Thomassey, A. Fiordaliso, A hybrid sales forecasting system based on clustering and decision trees, Decision Support Systems 42 (2006) 408–421.

[31] F. Tseng, Quadratic interval innovation diffusion models for new product sales forecasting, Journal of the Operational Research Society 59 (2008) 1120–1127.

[32] P. Winters, Forecasting sales by exponentially weighted moving averages, Management Science (1960).

[33] W.K. Wong, Z.X. Guo, A hybrid intelligent model for medium-term sales forecasting in fashion retail supply chains using extreme learning machine and harmony search algorithm, International Journal of Production Economics 128 (2010) 614–624.

[34] W.K. Wong, Z.X. Guo, S.Y.S. Leung, Partially connected feedforward neural networks on Apollonian networks, Physica A—Statistical Mechanics and Its Applications. 389 (2010) 5298–5307.

[35] J.H. Xie, et al., Kalman <sup>fi</sup>lter estimation of new product diffusion models, Journal of Marketing Research 34 (1997) 378–393.

[36] G. Zhang, M. Qi, Neural network forecasting for seasonal and trend time series, European Journal of Operational Research 160 (2005) 501–514.

![](/api/attachments/MSXYGJZC/fulltext/images/aef7283e4dc0e55ba5fec17629b4c9bf4146a75c67fa0a39cfe2a9ca928f4336.jpg)  
Z.X. Guo received his Ph.D. degree from The Hong Kong Polytechnic University. Currently, he is an associate professor at Business School of Sichuan University. His recent research interests include production planning and control, sales forecasting, intelligent decision making and op timization. He has published more than 10 research papers in refereed journals, such as Information Sciences, International Journal of Production Economics, and IEEE Transactions

![](/api/attachments/MSXYGJZC/fulltext/images/6ff41afea1242eabb609ae4d52adbaff1b1b2b1576499ed132cbed40e2ae7411.jpg)

W.K. Wong received his Ph.D. degree from The Hong Kong Polytechnic University. Currently, he is the associate professor in this university. He has published more than <sup>fi</sup>fty scienti<sup>fi</sup>c articles in refereed journals, including International Journal of Production Economics, Expert Systems with Applications, European Journal of Operational Research, International Journal of Production Research, Computers in Industry, The IEEE Transactions on Systems, Man, and Cybernetics, among others. His recent research interests include modeling of supply chain management, manufacturing planning and scheduling, data mining and knowledge discovery, and time series forecasting.

![](/api/attachments/MSXYGJZC/fulltext/images/716850aba82459f8aa7db9420ef54169a2d47b4eefd4e7ed5ffbd8978b307e83.jpg)

Min Li received her Bachelor degree in Electronics and Information Engineering from the Donghua University, China. She is currently an MPhil student at Institute of Textiles and Clothing of The Hong Kong Polytechninc University, Hong Kong, China, Her recent interest include fashion retail forecasting and supply chain management.
