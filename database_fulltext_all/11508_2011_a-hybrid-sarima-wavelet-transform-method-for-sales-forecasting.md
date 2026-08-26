---
otero_id: 11508
otero_key: "6XCXHC4X"
title: "A hybrid SARIMA wavelet transform method for sales forecasting"
authors: "Tsan-Ming Choi; Yong Yu; Kin-Fan Au"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.12.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A hybrid SARIMA wavelet transform method for sales forecasting

Tsan-Ming Choi ⁎, Yong Yu, Kin-Fan Au

Business Division, Institute of Textiles & Clothing, Faculty of Applied Science and Textiles, The Hong Kong Polytechnic University, Hung Hom, Kowloon, Hong Kong

## a r t i c l e i n f o

Article history: Received 14 January 2010 Received in revised form 6 August 2010 Accepted 5 December 2010 Available online 15 December 2010

Keywords: Sales forecasting SARIMA model Wavelet transform Decision support system

## a b s t r a c t

Time series forecasting, as an important tool in many decision support systems, has been extensively studied and applied for sales forecasting over the past few decades. There are many well-established and widelyadopted forecasting methods such as linear extrapolation and SARIMA. However, their performance is far from perfect and it is especially true when the sales pattern is highly volatile. In this paper, we propose a hybrid forecasting scheme which combines the classic SARIMA method and wavelet transform (SW). We compare the performance of SW with (i) pure SARIMA, (ii) a forecasting scheme based on linear extrapolation with seasonal adjustment (CSD+LESA), and (iii) evolutionary neural networks (ENN). We illustrate the signi<sup>fi</sup>cance of SW and establish the conditions that SW outperforms pure SARIMA and CSD+LESA. We further study the time series features which in<sup>fl</sup>uence the forecasting accuracy, and we propose a method for conducting sales forecasting based on the features of the given sales time series. Experiments are conducted by using real sales data, hypothetical data, and publicly available data sets. We believe that the proposed hybrid method is highly applicable for forecasting sales in the industry.

© 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

Sales forecasting plays a very important role in business operations and it is essentially signi<sup>fi</sup>cant in businesses with a highly volatile sales pattern such as fashion apparels and consumer electronics. A proper selection of models for forecasting sales is one of the major research efforts over the past few decades [16].<sup>1</sup> Although traditional methodologies of sales forecasting such as auto-regression (AR), and integrated moving average model have been proven to be effective in many decision support applications [2,3,9,21], they still have certain shortcomings, and fail in an environment where the sales are more in<sup>fl</sup>uenced by exogenous variables such as size, price, colour, climatic data, effect of media, and price changes. Recently, more and more research efforts have been spent on exploring hybrid forecasting models such as a remarkable method based on clustering and decision trees analysis [22] and some others [1,5,6].

It is well-known that arti<sup>fi</sup>cial intelligence (AI) models [5,6] have more <sup>fl</sup>exibility and can be used to estimate the non-linear relationship. Therefore, many researchers have applied AI models for forecasting problems. For example, in Ref. [11], the authors propose the use of arti<sup>fi</sup>cial neural networks (ANN) approach to forecast women's apparel sales. Their experimental results show that ANN approach outperforms the other two conventional models, namely, single seasonal exponential smoothing model and Winters three parameter models. In Ref. [6], the authors propose a hybrid model for stock price forecasting by integrating multiple regressions, back propagation (BP) neural network and an autoregressive integrated moving average model. In Ref. [23], the performance of a heterogeneous mixture of neural network algorithms for predicting the exchange-traded fund is investigated. A genetic algorithm is utilized to <sup>fi</sup>nd the best mixture of neural networks, the topology of individual networks in the ensemble, and to determine the features set. In Ref. [7], the authors develop an evolving neural network (ENN) forecasting model by integrating genetic algorithms (GA) and ANN for sales forecasting in the electronics industry. Their experimental result shows that the performance of ENN is superior to various traditional statistical models and the back propagation network. In Ref. [8], the authors propose a hybrid system which combines the self-organizing map (SOM) of neural network with case-based reasoning (CBR) model for sales forecasting of newly released books. In Ref. [1], the authors present a hybrid intelligent system combining ARIMA models and neural networks for demand forecasting. Despite the popularity of the ANN related methods, the performance of all these ANN based techniques depends highly on the relationship between the patterns used in training the networks and the expected forecasting patterns. If the diversity or the inconsistency between the training patterns and the expected forecast patterns is signi<sup>fi</sup>cant, the forecast errors of the ANN technique will tend to be relatively high [15]. Moreover, the ANN related methods for sales forecasting in the item-level usually require a very long computational time which makes this method less appealing to many real-world applications in the industry such as fashion apparels because there are thousands of SKUs (products with a unique design, colour, and size). Alternatively, it is argued that sales amount is affected by several nonlinear exogenous variables and periodical components, which can be illustrated by different mathematical models. To improve the forecasting precision, the optimal forecasting model should make a wise use of these different data components. Thus, we can decompose the given time series into component time series with different characteristics, and based on the features of the components, we apply the appropriate type of forecasting scheme and then we convert the forecasting of the timeseries at component levels back to the original time series level. One way of conducting this decomposition is via the wavelet transform.

In recent years, the wavelet transform has yielded encouraging results in multi-resolution analysis as well as many other functions [10,24] and it has also been combined with fuzzy logics for different applications [5]. The wavelet transform allows the decomposition of a signal into different levels of resolution scales, which means that we can extract the required data components. To be speci<sup>fi</sup>c, by using discrete wavelet transformation (DWT), we can decompose the sales data time series into several scales, where both the coarse and <sup>fi</sup>ne parts of the data are obtained. The coarse (approximated) scales reveal the trend, while the <sup>fi</sup>ne (detailed) scales tend to be related to seasonal in<sup>fl</sup>uences, and exogenous variables such as size, price, colour, climatic data, effect of media, and price changes. Afterwards, the multiple regression model and SARIMA forecast model can be adopted for forecasting in the approximated scale and the detailed scales, respectively. Finally, the inverse wavelet transform is used to generate the <sup>fi</sup>nal sales forecasting time series. In Refs. [5] and [24] the wavelet transformation schemes are combined with AI techniques to do forecasting for the <sup>fi</sup>nancial time series. Such hybrid schemes show signi<sup>fi</sup>cant advantages over the traditional AI models. This indicates that the wavelet can be a promising tool in the decomposition of the time series. As a remark, many researchers have studied all kinds of forecasting models while there is no well-agreed rule on specifying which one is better under which condition. In light of the complex nature of many highly volatile sales patterns, many researchers are in favour of the sophisticated models such as SARIMA and ENN, while many others are in favour of simple models such as simple linear inherited models [14,18], which are also supported by many applications in the industry. However, both groups of researchers could consider the use of a certain decomposition scheme to further enhance their original methods and hybrid models are both interesting and promising in the area of forecasting. In this paper, we concentrate on studying a hybrid model which combines the classic SARIMA method and wavelet transform (SW). We compare SW with two other models, namely, the pure SARIMA method and the Classical Seasonal Decomposition with Linear Extrapolation with Seasonal Adjustment method (CSD+LESA). The forecasting schemes are tested for their forecasting performance with arti<sup>fi</sup>cially composed data sets (to study the impacts brought by different features of the sales pattern), real sales data sets, and publicly available data sets. We <sup>fi</sup>nd that these methods perform differently under different conditions. For example, our experiments demonstrate that the SW method outperforms all the others when the data sets are associated with a highly volatile pattern. the CSD + LESA model performs better than the others with data sets which exhibit strong white noise, while the SARIMA model outperforms the above two when seasonality in the data set is very strong which dominates the time series, and the decomposition methods are no better than SARIMA in modelling the seasonality. After obtaining these results, we further develop a decision model (Fig. 13) which helps us select the most appropriate method for each forecasting task in order to achieve the best sales forecasting performance. The paper develops as follows. Section presents multi-scale decomposition for the sales time series using the wavelet transform. Section 3 provides a detailed speci<sup>fi</sup>cation of the forecasting procedure, and the forecasting results based on various models are presented. Section 4 discusses the comparison between the methods. The concluding remarks are provided in Section 5.

## 2. Multi-scale decomposition using wavelet transform for forecasting

To illustrate the decomposition scheme using the wavelet transform, we start by using the sales time series from an apparel company.

## 2.1. Fashion sales data

In this section, the fashion sales time series of several retail stores of an apparel company have been studied, the data collected covers the sales data for various types of apparels from 1999 to 2003, and sales data points are collected for each day for every class for every store. Daily sales curve over a period from 4 July 2002 to 28 August 2002 is given in Fig. 1. The time series in Fig. 1 is presumed to have weekly seasonality as nearly all daily sales data sets do. However, as what we have observed, the weekly trend is not so clear in the curve. To be systematic, trends and seasonality of the sales data are further supported by calculating auto correlations functions (ACFs). ACF is an important tool for discerning time series patterns, ACF for a given time lag k is given by Eq. (1):

$$
r _ {k} = \frac {\sum_ {t = k + 1} ^ {n} (Y _ {t} - \overline {{Y}}) (Y _ {t - k} - \overline {{Y}})}{\sum_ {t = 1} ^ {n} (Y _ {t} - \overline {{Y}}) ^ {2}},\tag{1}
$$

where $Y _ { i } , ( i { = } 1 , { \ldots } , n )$ is a time series, where Y is the mean value of the time series, k is the time lag. Although this kind of analysis is not a necessity for the wavelet-transform based forecasting models, it helps us understand the trends and seasonality of a given sales data set. Moreover, as we will see later, by checking ACF, we can know more about when SW outperforms CSD+LESA.

## 2.2. Multi-scale decomposition of sales time series

For a given sales time series, in general, it is dif<sup>fi</sup>cult to describe its components very accurately. However, via a wavelet transform, it becomes easier for us to observe these factors and make the forecasting task easier. As the SARIMA model will be employed in studying the time series later, the historical sales data is expected to have at least 50 points to yield a sound analysis. In this section, the historical sales data of an apparel company in 8 weeks (56 out of 66 points is used) will be decomposed in different scales by the discrete wavelet transform.

There are two criteria for the selection of the mother wavelet [12]. Firstly, the shape and the mathematical expression of the wavelet must be selected correctly so that the physical interpretation of the wavelet coef<sup>fi</sup>cients is easy. Secondly, the chosen wavelet must allow a fast computation of the required wavelet coef<sup>fi</sup>cients. In this paper, the discrete approximation of Meyer wavelet (D-Meyer) is hence selected as it is a fast algorithm which also supports discreet transformation [4].

![](/api/attachments/6XCXHC4X/fulltext/images/df03955c4f40956912530089163ab2af0cea3df51811df8d4bafff1d04e376b8.jpg)  
Fig. 1. Daily sale of a speci<sup>fi</sup>c apparel product.

![](/api/attachments/6XCXHC4X/fulltext/images/051701aefbf74ced27e973648d0d693f6152dd0d0baff0c5435a7b0958a66882.jpg)

(b)  
![](/api/attachments/6XCXHC4X/fulltext/images/c58ed97869bb6a0b348e3aace45e6a3089f8138adad110117fa012b734a65941.jpg)

![](/api/attachments/6XCXHC4X/fulltext/images/5fdcad9f7700fd0ab0b1837c1e9e940f6eb06120efdbc732b538e92b20c39442.jpg)

(d)  
![](/api/attachments/6XCXHC4X/fulltext/images/fc6bc4fe8138bd004a8d91a557d60c5d4e2b5337c919e5d7f68ea3d42c2c724e.jpg)  
Fig. 2. D-Meyer three-level wavelet decomposition.

The results in different scales are shown in Fig. 2. Fig. 2 illustrates the three-level decomposition using D-Meyer. We can see from Fig. 2(a) that the detailed scale mainly contains the trend component, Fig. 2(b–d) represent most of the weekly periodic components and stochastic components. Time series forecasting can be produced by forecasting on the trend and seasonal components separately. We thus propose that in applying the wavelet decomposition for the sake of forecasting, it is not necessary to decompose a given time series into too many components. We will address this issue more in the next section.

## 3. Hybrid forecasting based on wavelet transform and SARIMA (SW)

Sales forecasting, especially in the industry such as fashion, is a challenging task because many endogenous as well as exogenous variables, e.g. size, price, colour, climatic data, effect of media, etc., which affect sales, are involved. In the above section, by using discrete wavelet transform (DWT), we decompose the given sales time series into several scales and the detailed and approximated components are obtained. In order to improve the forecasting precision, the optimal forecast models should be tailored for forecasting the components in different scales.

## 3.1. Data processing in the approximated scale

The approximated scale presents mainly a trend component. As our proposed scheme mainly focuses on the sales forecasting for highly volatile patterns and this randomness makes the components in the approximate scales exhibit low seasonality. In our proposed method, we will adopt the ARIMA model for forecasting the components in the approximate scale. This approach is supported by our preliminary experiments conducted during the development of the proposed model with the use of real sales data.

## 3.2. Data processing in the detailed scale

The detailed scale contains mainly the seasonal and stochastic components and should be analyzed by SARIMA. SARIMA is the most popular linear model for forecasting seasonal time series. It has achieved great success in both academic research and industrial applications during the last three decades. A time series $\{ Z _ { t } | 1 , 2 , . . . , k \}$ is generated by SARIMA $\left( p , d , q \right) \left( P , D , Q \right)$ process of Box and Jenkins time series model [3] if

$$
\phi_ {p} (B) \Phi_ {P} (B ^ {s}) (1 - B) ^ {d} (1 - B ^ {s}) ^ {D} Z _ {t} = \theta_ {q} (B) \Theta_ {\mathrm{Q}} (B ^ {s}) \varepsilon_ {t},\tag{2}
$$

where p, d, q, P, D, Q are integers, s is the season length;

$$
\phi_ {p} (B) = 1 - \phi_ {1} B - \phi_ {2} B ^ {2} - \dots - \phi_ {p} B ^ {p},
$$

$$
\Phi_ {p} (B ^ {s}) = 1 - \Phi_ {s} B ^ {s} - \Phi_ {2 s} B ^ {2 s} - \dots - \Phi_ {p s} B ^ {p s},
$$

$$
\theta_ {q} (B) = 1 - \theta_ {1} B - \theta_ {2} B ^ {2} - \dots - \theta_ {q} B ^ {q}, \mathrm{and}
$$

$$
\Theta_ {Q} (B ^ {s}) = 1 - \Theta_ {s} B ^ {s} - \Theta_ {2 s} B ^ {2 s} - \dots - \Theta_ {Q s} B ^ {Q s},
$$

![](/api/attachments/6XCXHC4X/fulltext/images/6f71385a83e07ebb3c062233c7a7778daad495b7d6350ba5a10ea017a79c18f4.jpg)  
Fig. 3. The composition of the hypothetical data.

are polynomials in $B ,$ where B is the backward shift operator, $\varepsilon _ { t }$ is the estimated residual at time t, d is the number of regular differences, D is the number of seasonal differences, $\mathbf { , } Z _ { t }$ denotes the observed value at time $t , t = 1 , 2 , . . . , k .$

Fitting a SARIMA model to data involves the following four-step iterative cycles: (a) identify the SARIMA (p, d, q) (P, D, Q)'s structure; (b) estimate unknown parameters; (c) perform goodness-of-<sup>fi</sup>t tests on the estimated residuals; and (d) forecast future outcomes based on the known data. The <sup>fi</sup>tting of SARIMA models is a challenging task (an example can be found in Ref. [19]), and it involves human judgment on the ACF charts. As we concentrate on the effect of the wavelet decomposition, to avoid the human judgment in<sup>fl</sup>uences of SARIMA, we use SARIMA (1,1,0) for all the SARIMA models.

Every $\varepsilon _ { t }$ is independently and identically distributed as a normal random variable with mean 0 and constant variance $\sigma ^ { 2 } .$ . The roots of $\phi _ { p } ( Z ) = 0$ and $\theta _ { q } ( Z ) = 0$ all lie outside the unit circle. In addition, it is suggested by Ref. [3] that a minimum of 50 (preferably 100) observations should be used for the SARIMA model.

## 3.3. Evaluating indices

A good forecasting method needs to take into consideration the degree of accuracy. A popular measure, known as the Mean Absolute Percentage Error (MAPE), is presented as follows:

$$
M A P E = \frac {1}{n} \sum_ {i = 1} ^ {n} \frac {| F _ {i} - A _ {i} |}{A _ {i}},\tag{3}
$$

![](/api/attachments/6XCXHC4X/fulltext/images/8cc87dd57bc09e562a8c0a5e26d37b5b9f527eb661ab3637e738aedc852b1cff.jpg)

![](/api/attachments/6XCXHC4X/fulltext/images/8ee83bdc674d19ddf620394956f8297752655433ce0c20f273ab8fd2d075762b.jpg)

![](/api/attachments/6XCXHC4X/fulltext/images/23e0b3882602c2d44c8eaec71630b7e7353b9b1a5963dec234d7381bb91ca13e.jpg)  
Fig. 4. The 1-level wavelet decomposition.

![](/api/attachments/6XCXHC4X/fulltext/images/272b68b4a8001d16c759293ebf7f4c39720a5e80138313c74910e9a9afcb1aca.jpg)  
Fig. 5. The autocorrelation factor (ACF) of d .

where $F _ { i }$ is the forecast value for period $i , A _ { i }$ is the actual value for period i, n is the total number of periods. As MAPE is good at describing a relative error, which is especially suitable when comparing between different data sets, it is used as the performance index in this paper.

## 3.4. Wavelet-based forecasting and its parameter selection procedure

By using inverse discrete wavelet transform (IDWT), the sales forecasting results are then obtained by the reconstruction of the forecasting data in different scales. As we discussed above, when the wavelet is used in the time series decomposition, the number of decomposition levels has to be determined <sup>fi</sup>rst. Sales time series is hypothetically composed of trend and seasonality. As a result, the major goal of decomposition is to reveal these two major factors. In wavelet decomposition, as the purpose of the decomposition procedure is to <sup>fi</sup>nd the underlying trend and seasonality components, it is not necessary to decompose a time series into too many components. However, a simple one level decomposition often cannot identify the seasonality factors precisely. The experiments on theoretically generated data sets (as in Fig. 3) are hence used to study this feature. In Fig. 4, a 1-level wavelet decomposition is performed as the <sup>fi</sup>rst step. The two components, highfrequency component $d _ { 1 }$ and approximation a, are retrieved. Component $d _ { 1 }$ shows the weekly seasonality when we examine its autocorrelation factor (ACF) chart in Fig. 5, since the ACF is signi<sup>fi</sup>cantly greater than the con<sup>fi</sup>dence limits at lag 7 and lag 14, we consider the seasonality in $d _ { 1 }$ as strong (please refer to Ref. [17] for details about the identi<sup>fi</sup>cation of seasonality in an ACF chart).

When $d _ { 1 }$ with seasonality is found from the 1-level decomposition, the approximation a is not close to the hypothetic trend, and it also has some seasonality cycle in it. As the second step, a 2-level decomposition is performed on the time series. Fig. 6 depicts the decomposition and Fig. 7 depicts the ACF of $d _ { 2 } .$ Again, component $d _ { 2 }$ has a strong weekly seasonality. As both $d _ { 1 }$ and $d _ { 2 }$ have weak seasonality, we add these two up as a single seasonal factor as shown in Fig. 8. The seasonality of the add-up factor is stronger than each single one of $\dot { \boldsymbol { d } } _ { 1 }$ and $d _ { 2 } ,$ , which can be observed in the ACF chart in Fig. 9.

![](/api/attachments/6XCXHC4X/fulltext/images/efbc9db30aaa5f8b5cabb6d05a4cedaae98c8a456e318e71b9510b84f28a7473.jpg)  
Fig. 6. The 2-level wavelet decomposition.

![](/api/attachments/6XCXHC4X/fulltext/images/d1d20ba875c66a45aa707b0e2f314ad5359fb453a11d528c45a80c31895ae1de.jpg)  
Fig. 7. The autocorrelation factor (ACF) of $\cdot \mathrm { ~ } d _ { 2 } .$

In the third step, we further decompose the time series into 3 levels, as shown in Fig. 10, we can no longer <sup>fi</sup>nd the weekly seasonality by observing the ACF in Fig. 11. Though there is a signi<sup>fi</sup>cant value at lag 7, it is not the most signi<sup>fi</sup>cant one among the nearby values and the signi<sup>fi</sup>cance does not repeat at lag 14. When comparing the 3-level wavelet decomposed time series with the original components in Fig. 12, the decomposed components are quite close to the original ones with trend, seasonal cycle and white noise. As the white noise component is not used in the forecasting, the 2- level decomposition is the right level for this situation. In practice, there are often cases where no seasonality is found during the decomposition of any level, we thus suggest using the SARIMA model for the original time series under this condition. There are also cases when a component may have no seasonality, but its <sup>fl</sup>uctuation is signi<sup>fi</sup>cant compared to the original time series so that it cannot be omitted in the forecasting process. Fig. 13 illustrates a complete procedure to deal with these situations.

![](/api/attachments/6XCXHC4X/fulltext/images/8b72930b4e7838016506486d4565e94ab0f396b5730f5b4455bf9a690c6ff9ec.jpg)

![](/api/attachments/6XCXHC4X/fulltext/images/833bbaa66a3eedb404575e8643eac879b1f43600f72211f4a2c0bf1a7ac6dbe7.jpg)

![](/api/attachments/6XCXHC4X/fulltext/images/2098ead02f463e375897beb9f9354eceb99d6b7dd1d60d6255cb1ac7dfd09b6d.jpg)  
Fig. 8. The 2-level wavelet decomposition with combining seasonality $d _ { 1 } + d _ { 2 } .$

![](/api/attachments/6XCXHC4X/fulltext/images/cf6c69145e14934d98883f288d8207a2f715c1861ece9d8782da4f63b9b202d5.jpg)  
Fig. 9. The autocorrelation factor (ACF) of $d _ { 1 } + d _ { 2 } .$

![](/api/attachments/6XCXHC4X/fulltext/images/dc6e4b9ef4c14b52feb5d7de896f5c1b27d51706b141204e07d349a8621620f0.jpg)

![](/api/attachments/6XCXHC4X/fulltext/images/1c7d50c341a84a2cc663d9376ced865bf399bdab6b01ea10ac9a961a4c107526.jpg)

![](/api/attachments/6XCXHC4X/fulltext/images/ec025e653eb906432b1c1b04074a39901a6cf18561903cddae64dbf06a522f59.jpg)

![](/api/attachments/6XCXHC4X/fulltext/images/56a8d8b0811c228de8ffde897134663c17d9419d739736068f191c0237708554.jpg)  
Fig. 10. The 3-level wavelet decomposition.

![](/api/attachments/6XCXHC4X/fulltext/images/cf66748be71c39e1436f0a9249bb8b90e6d6adbf16e5212faf02df06ae35484e.jpg)  
Fig. 11. The autocorrelation factor (ACF) of $d _ { 3 } .$

![](/api/attachments/6XCXHC4X/fulltext/images/c524b6c5c8da163f996d2dc151a5410611113a3e2ac24a8e5c4899e445df86ef.jpg)

![](/api/attachments/6XCXHC4X/fulltext/images/3c213d1d88820b5011b6ba7b2b23591b1c1be3764819943e4481e53950bdb343.jpg)

![](/api/attachments/6XCXHC4X/fulltext/images/28ed130b6598826f3da370a808edda54741c3ab37c8714b2a7189f90debf463e.jpg)

![](/api/attachments/6XCXHC4X/fulltext/images/1d993ba496044c480fc5f957cfc133e3be686c8f78503f197cb5a3a38c5508b7.jpg)  
Fig. 12. Comparison between the original components and the wavelet decomposed ones. (The solid lines representing the original components and the dashed lines representing the decomposed ones).

As we will employ the SARIMA method in forecasting for the seasonal component, a component with a strong seasonality apparently bene<sup>fi</sup>ts the forecasting. Table 1 further gives a forecasting comparison between the decompositions. This result shows that when a highly volatile pattern exhibits in the decomposed component, the forecasting result is expectedly better.

As in the CSD approach, the other decomposed components, such as $d _ { 3 }$ in Fig. 10, are considered to be white noise, since they cannot bene<sup>fi</sup>t the forecasting, they will not be included in estimating and reconstructing the <sup>fi</sup>nal forecasting. Unlike the CSD approach, although components in the wavelet decomposition may have no seasonality, the amplitude of such components can be quite signi<sup>fi</sup>cant comparing to the original time series. Under this condition, omitting the components can cause inaccurate forecasting. An example of this phenomenon is given in Section 4.3, and based on this experiment, a threshold is set as follows,

$$
T = | \max (d _ {n}) - \min (d _ {n}) | / | \max (S) - \min (S) |,
$$

where $S$ is the original time series, and $d _ { n }$ the decomposed series. According to the experiment in Section 4.3, if TN50%, the decomposition approach is not better than using the SARIMA method and hence SARIMA is suggested under this condition. Based on the previous analysis we develop an algorithm to systematically perform this forecasting procedure. The procedure is shown in Fig. 13. The algorithm starts with the decomposition level setting to be 1. The decomposition is conducted as in Fig. 5 and the $d _ { 1 }$ component's seasonality is examined by its autocorrelation factor, where $r _ { k }$ is de<sup>fi</sup>ned in (1). Usually the ACF analysis involves human judgement of the ACF chart as the Box–Jenkins method suggests. To simplify this procedure, we use automatic judgement. When the ACF at the <sup>fi</sup>rst lag of season length (such as 7 for weekly seasonality) is greater than the corresponding critical value and dominates the other nearby signi<sup>fi</sup>cant ACFs, we consider the underlying series to have strong seasonality. If it is signi<sup>fi</sup>cant but not dominating, we further observe the ACF as the next lag of season length (14 for weekly seasonality); if that ACF is signi<sup>fi</sup>cant, we also consider the underlying series to have strong seasonality. If the seasonality of d is strong, the stopping criterion will be met and the algorithm stops. If the seasonality of $d _ { 1 }$ is not strong enough, the algorithm repeats with the level increased by 1 as shown in Fig. 7. Like the CSD method, we also presume a sales time series to be composed of trend, seasonality, and irregular components, and the wavelet decomposition is to reveal these underlying 3 components, especially the <sup>fi</sup>rst 2 components for forecasting. Apparently, too many levels of the wavelet decomposition do not really help with the accuracy of forecasting because when the decomposition level is increased, the newly generated components are of minor importance. However, as we have observed in Fig. 10, combining two seasonal components with seasonality helps to increase the accuracy of forecasting, this indicates that to decompose the time series into 4 or 5 levels may be helpful. Thus we set an upper bound as 5 levels which mean that the algorithm will stop even if there is no clear seasonality found under the 5 level decomposition. When this situation happens, we recommend utilizing other forecasting methods.

## 4. Comparisons among different methods

In this section, we study the forecasting performance of various methods, which include the pure SARIMA, SW, CSD+LESA. All methods are used in forecasting with hypothetical data and real sales data in fashion business. Some public data sets are also used in the experiments.

## 4.1. Comparison: hypothetical data

The hypothetical data set is composed of the trend, seasonality and white noise components, which are also used in the last section, as shown in Fig. 3. When the CSD+LESA method is employed in analyzing this hypothetical data set, the time series are <sup>fi</sup>rst decomposed into seasonal adjusted series and seasonal adjust factor. The time series are found almost perfectly decomposed into the trend and seasonal factor, as the LESA method in nature presumes a perfect seasonality which exactly matches with this hypothetical condition.

When the SW method is employed on the hypothetical data, the algorithm in Section 3 is employed to determine the levels to be decomposed, in this situation, the algorithm stops with a level of 3, Fig. 10 depicts the decomposition result. After the decomposition, forecasting is carried out on all methods, and the results are shown in Table 2.

As we can observe in Table 2, the forecasting performances of CSD and SW are quite similar, either in the overall scale or weekly scale. This result is different from Ref. [14] which claims that the simple approach LESA is better than the other sophisticated methods. These two methods are both better than the SARIMA model, which means that the decomposition bene<sup>fi</sup>ts the forecasting in this situation.

It is natural that features of the time series greatly in<sup>fl</sup>uence the forecasting result. These features are essentially the statistical factors of the trend, seasonality and irregular components. In this section, we carry out two experiments on the hypothetical data with different parameters, namely the hypothetical data with the white noise variance increased to 500, and the hypothetical data with the seasonal variance increased to 600. Table 3 gives the result of the comparison, in which “Column $A S "$ list the original result where the white noise variance is 10, as in Table 1, “Column $\mathsf { B } \boldsymbol { S } ^ { \ ' }$ list the result when the variance of the white noise is increased to 500 and “Column $C s "$ list the result when the variance of the seasonal cycle is increased to 600. While all methods provide worse forecasting because of the increased variance of the white noise (as seen by comparing “Column $\boldsymbol { \mathrm { B } } \boldsymbol { s } ^ { \prime \prime }$ in Table 3), it is interesting to notice that the CSD+LESA method provides a little bit better forecasting than SW. However, as seen in the “Column $C s " ,$ , when the variance of the seasonal cycle increases,

![](/api/attachments/6XCXHC4X/fulltext/images/6e782c592c09d651545d56ba0881cbef0311815dac24a341bc2c35b18035553e.jpg)  
Fig. 13. The procedure of sales forecasting using the hybrid SARIMA wavelet transform method. (As a remark, this algorithm is not depicted with the standard <sup>fl</sup>ow chart notation).

SW performs much better than the CSD+LESA method. Table 4 summarizes the above <sup>fi</sup>ndings.

Although the CSD+LESA method performs slightly better than SW when the white noise variance is big, it is no longer better when the variance of the seasonal cycle increases which governs the features of the time series. The SARIMA model still produces the worst forecasting results compared to SW and CSD+LESA when the seasonal features of the time series are changed. In the following section, we further study the forecasting performance of these methods with real sales data.

Table 1  
Forecasting comparison of decomposition in different levels.

<table><tr><td rowspan="2">Week</td><td colspan="2">1 level decomposition (a,  $d_1$ )</td><td colspan="2">2 levels decomposition (a,  $d_2$ )</td><td colspan="2">2 levels decomposition (a,  $d_1+d_2$ )</td><td colspan="2">3 levels decomposition (a,  $d_1+d_2$ ,  $d_3$ )</td></tr><tr><td>MAPE</td><td>MSE</td><td>MAPE</td><td>MSE</td><td>MAPE</td><td>MSE</td><td>MAPE</td><td>MSE</td></tr><tr><td>Week 8</td><td>0.06</td><td>8.4</td><td>0.07</td><td>15.2</td><td>0.06</td><td>9.7</td><td>0.07</td><td>13.6</td></tr><tr><td>Week 9</td><td>0.11</td><td>42.1</td><td>0.13</td><td>59.2</td><td>0.10</td><td>28.6</td><td>0.11</td><td>50.1</td></tr><tr><td>Week 10</td><td>0.07</td><td>15.3</td><td>0.08</td><td>21.1</td><td>0.06</td><td>8.3</td><td>0.09</td><td>45.3</td></tr><tr><td>Week 11</td><td>0.10</td><td>38.3</td><td>0.09</td><td>50.7</td><td>0.09</td><td>33.1</td><td>0.12</td><td>55.7</td></tr><tr><td>Week 12</td><td>0.05</td><td>10.8</td><td>0.11</td><td>52.8</td><td>0.04</td><td>6.5</td><td>0.03</td><td>2.8</td></tr><tr><td>Week 13</td><td>0.04</td><td>5.5</td><td>0.11</td><td>47.6</td><td>0.04</td><td>4.3</td><td>0.07</td><td>10.6</td></tr><tr><td>Overall MAPE</td><td>0.072</td><td>20.1</td><td>0.101</td><td>41.1</td><td>0.066</td><td>15.1</td><td>0.082</td><td>29.7</td></tr></table>

Forecasting comparison on hypothetical data

<table><tr><td rowspan="2">Week</td><td colspan="2">SARIMA</td><td colspan="2">ARIMA_SARIMA_WAVELET (trend + season)</td><td colspan="2">CSD + LESA</td></tr><tr><td>MAPE</td><td>MSE</td><td>MAPE</td><td>MSE</td><td>MAPE</td><td>MSE</td></tr><tr><td>Week 8</td><td>0.058</td><td>12.4</td><td>0.062</td><td>21.7</td><td>0.073</td><td>55.1</td></tr><tr><td>Week 9</td><td>0.120</td><td>33.1</td><td>0.060</td><td>15.4</td><td>0.052</td><td>19.6</td></tr><tr><td>Week 10</td><td>0.056</td><td>15.2</td><td>0.057</td><td>18.1</td><td>0.061</td><td>42.1</td></tr><tr><td>Week 11</td><td>0.094</td><td>56.2</td><td>0.043</td><td>7.7</td><td>0.057</td><td>10.5</td></tr><tr><td>Week 12</td><td>0.062</td><td>30.8</td><td>0.042</td><td>6.8</td><td>0.030</td><td>4.3</td></tr><tr><td>Week 13</td><td>0.033</td><td>9.6</td><td>0.043</td><td>8.9</td><td>0.041</td><td>8.5</td></tr><tr><td>Overall MAPE</td><td>0.071</td><td>26.2</td><td>0.051</td><td>13.1</td><td>0.052</td><td>23.4</td></tr></table>

Forecasting comparison with different parameters.

<table><tr><td rowspan="2">Week</td><td colspan="3">SARIMA</td><td colspan="3">SW</td><td colspan="3">CSD + LESA</td></tr><tr><td>A</td><td>B</td><td>C</td><td>A</td><td>B</td><td>C</td><td>A</td><td>B</td><td>C</td></tr><tr><td>Week 8</td><td>0.058</td><td>1.11</td><td>0.068</td><td>0.062</td><td>1.18</td><td>0.067</td><td>0.073</td><td>1.11</td><td>0.099</td></tr><tr><td>Week 9</td><td>0.120</td><td>1.97</td><td>0.138</td><td>0.060</td><td>1.43</td><td>0.073</td><td>0.052</td><td>1.17</td><td>0.054</td></tr><tr><td>Week 10</td><td>0.056</td><td>0.68</td><td>0.073</td><td>0.057</td><td>0.78</td><td>0.067</td><td>0.061</td><td>0.77</td><td>0.083</td></tr><tr><td>Week 11</td><td>0.094</td><td>0.40</td><td>0.109</td><td>0.043</td><td>0.21</td><td>0.053</td><td>0.057</td><td>0.31</td><td>0.078</td></tr><tr><td>Week 12</td><td>0.062</td><td>0.46</td><td>0.066</td><td>0.042</td><td>0.44</td><td>0.045</td><td>0.030</td><td>0.33</td><td>0.059</td></tr><tr><td>Week 13</td><td>0.033</td><td>0.51</td><td>0.039</td><td>0.043</td><td>0.44</td><td>0.047</td><td>0.041</td><td>0.42</td><td>0.060</td></tr><tr><td>Overall MAPE</td><td>0.071</td><td>0.85</td><td>0.082</td><td>0.051</td><td>0.74</td><td>0.058</td><td>0.052</td><td>0.69</td><td>0.072</td></tr></table>

A: forecasting on original data (white noise's variance=10); B: forecasting on data with the variance of white noise component increased to 500; C: forecasting on data with the variance of seasonal cycle component increased to 600.

## 4.2. Comparison: real fashion sales data

The real fashion sales data set adopted here has been discussed in Section 2. Without theoretically perfect seasonality, a seasonality factor is retrieved by the CSD method. As for the decomposition of SW, the decomposition level is increased to be 2 compared to the decomposition on the hypothetical data with perfect seasonality. The <sup>fi</sup>nal result is presented in Table 5, which shows that the SW method dominates the CSD+LESA method in the forecasting of real fashion sales data. While the SARIMA method produces slightly better forecasting than the CSD+LESA method, it still cannot compete with the SW method.

Forecasting variation with different parameters.

<table><tr><td>Components changes</td><td>SW</td><td>CSD + LESA</td></tr><tr><td>Original</td><td>√</td><td>0</td></tr><tr><td> $\sigma_{WN}$  increased</td><td>0</td><td>√</td></tr><tr><td> $\sigma_{SC}$  increased</td><td>√</td><td>0</td></tr></table>

σ : variance of white noise, $\sigma _ { S C } :$ variance of seasonal cycle.  
√ : better in the comparison of forecasting accuracy, O : worse in the comparison of forecasting accuracy.

Forecasting comparison on real fashion sales data.

<table><tr><td rowspan="2">Week</td><td colspan="2">SARIMA</td><td colspan="2">SW (trend + seasonality)</td><td colspan="2">CSD + LESA</td></tr><tr><td>MAPE</td><td>MAE</td><td>MAPE</td><td>MAE</td><td>MAPE</td><td>MAE</td></tr><tr><td>Week 8</td><td>0.30</td><td>0.031</td><td>0.17</td><td>0.019</td><td>0.26</td><td>0.025</td></tr><tr><td>Week 9</td><td>1.11</td><td>0.113</td><td>0.93</td><td>0.101</td><td>1.14</td><td>0.112</td></tr><tr><td>Week 10</td><td>0.32</td><td>0.033</td><td>0.26</td><td>0.033</td><td>0.39</td><td>0.040</td></tr><tr><td>Week 11</td><td>0.37</td><td>0.035</td><td>0.35</td><td>0.034</td><td>0.45</td><td>0.045</td></tr><tr><td>Week 12</td><td>0.27</td><td>0.027</td><td>0.30</td><td>0.032</td><td>0.31</td><td>0.032</td></tr><tr><td>Week 13</td><td>0.69</td><td>0.070</td><td>0.62</td><td>0.063</td><td>0.65</td><td>0.063</td></tr><tr><td>Overall MAPE</td><td>0.51</td><td>0.052</td><td>0.44</td><td>0.047</td><td>0.53</td><td>0.053</td></tr></table>

## 4.3. Comparison: public available sales data

A publicly available data set, Monthly Australian sales of sparkling wine from Time Series Data Library http://www-personal.buseco. monash.edu.au/\~hyndman/TSDL/, is used in this analysis. The time series is depicted in Fig. 14. The autocorrelation analysis over the time series shows a very signi<sup>fi</sup>cant ACF at lag 12, which is more than double of the critical value. This indicates a strong yearly seasonality in the monthly Australian sales of the sparkling wine time series.

Applying the method described in Section 2, two components with seasonality $( d _ { 1 } , d _ { 2 } )$ are found, while $d _ { 3 }$ has no obvious seasonality, the threshold of it is T=55%. So, a 3-level decomposition is performed on the time series. The forecasting comparison of SARIMA, SW and CSD+ LESA is shown in Table 6. Again, similar to the forecasting results for the real data of fashion sales, SW performs better than the CSD+LESA method. As the simple linear extrapolation inherently presumes the unrealistic perfect linear trend in the time series, the forecasting results of CSD+LESA can be quite poor. In the comparison, the pure SARIMA method is found to be the best one among the three. The reason is that: although $d _ { 3 }$ has no seasonality, its T value is very signi<sup>fi</sup>cant (TN50%) and hence it should not be omitted in the forecasting process. This implies that the proposed decomposition approach is not effective under this situation, and the pure SARIMA is the preferred method.

![](/api/attachments/6XCXHC4X/fulltext/images/750b9fa39802e1084b90f73fd054023e5071c01eb57743b99f3ed426ec2ed822.jpg)  
Fig. 14. Monthly Australian sales of sparkling wine.

Table 6  
Forecasting comparison in MAPE.

<table><tr><td rowspan="2">Year</td><td colspan="2">SARIMA</td><td colspan="2">CSD + LESA</td><td colspan="2">SW (a,  $d_1 + d_2$ )</td></tr><tr><td>MAPE</td><td>MSE</td><td>MAPE</td><td>MSE</td><td>MAPE</td><td>MSE</td></tr><tr><td>Year 5</td><td>0.112</td><td>173,772</td><td>0.225</td><td>501,338</td><td>0.193</td><td>471,156</td></tr><tr><td>Year 6</td><td>0.108</td><td>177,076</td><td>0.258</td><td>632,895</td><td>0.133</td><td>268,435</td></tr><tr><td>Year 7</td><td>0.147</td><td>260,421</td><td>0.160</td><td>284,633</td><td>0.189</td><td>435,231</td></tr><tr><td>Year 8</td><td>0.194</td><td>419,619</td><td>0.452</td><td>1,158,342</td><td>0.372</td><td>828,612</td></tr><tr><td>Year 9</td><td>0.188</td><td>288,082</td><td>0.378</td><td>868,532</td><td>0.347</td><td>793,487</td></tr><tr><td>Overall MAPE</td><td>0.150</td><td>263,794</td><td>0.290</td><td>574,290</td><td>0.20</td><td>466,153</td></tr></table>

Another publicly available time series is ten years data of monthly production of woolen yarn in Australia (Australian Bureau of Statistics), as shown in Fig. 15.

Applying the method described in Section 3, we obtain the decomposition scheme which sets a level to be 3. The forecasting comparison is shown in Table 7. Again the SW method produces better forecasting than the CSD+LESA method in general. The $\mathrm { C S D + L E S A }$ method produces better forecasting for years 5 and 6, but the situation changes for year 7. Although for year 8, the CSD+LESA method gives better forecasting compared to SW, the difference is actually very marginal; and for year 9, the SW method is again signi<sup>fi</sup>cantly better than the CSD+LESA method. As we can observe from the time series, the seasonal features have changed a lot between year 6 and year 7 (at month 72), and the approximation component which represents the trend in the time series also changes. This indicates that the CSD+LESA method cannot adapt to the changes of the underlying components in a time series. In this experiment, the SARIMA model produces almost the same forecasting accuracy as the SW model but does not exceed it. The Bayesian Information Criterion (BIC) [20], which is a statistical criterion for the model selection, can be used as a reference in the selection. The BIC is given by: $B I C = n \ l n ( S S E / n ) + k \ l n ( n )$ , where n is the number of observations, k is the number of free parameters to be estimated, SSE is the sum of squared errors from the estimated model. The BIC is an increasing function of SSE and an increasing function of k. Thus, for any two given estimated models, the model with the lower value of BIC is preferred. The BIC is also given in Table 7, where n is the number of observations and k is the number of parameters used in all SARIMA analysis. As shown in Table 7, in most cases, the BIC of the SARIMA model is lower than that of the SW model's. The implications are discussed in Section 5.

![](/api/attachments/6XCXHC4X/fulltext/images/03b669100dcfa2d144341fdfc2ba0a04391319fdde4b27d5db4f8da6a55271c3.jpg)  
Fig. 15. Monthly production of wool yarn in Australia.

Table 7  
Forecasting comparison in MAPE.

<table><tr><td rowspan="2">Year</td><td colspan="3">SARIMA</td><td colspan="2">CSD + LESA</td><td colspan="3">SW (a,  $d_2+d_3$ )</td></tr><tr><td>MAPE</td><td>MSE</td><td>BIC</td><td>MAPE</td><td>MSE</td><td>MAPE</td><td>MSE</td><td>BIC</td></tr><tr><td>Year 5</td><td>0.050</td><td>18,543.7</td><td>595.7</td><td>0.049</td><td>20,149.1</td><td>0.054</td><td>21,521.3</td><td>617.3</td></tr><tr><td>Year 6</td><td>0.048</td><td>25,165.2</td><td>616.9</td><td>0.031</td><td>14,139.1</td><td>0.046</td><td>26,611.4</td><td>631.9</td></tr><tr><td>Year 7</td><td>0.050</td><td>21,061.6</td><td>604.5</td><td>0.071</td><td>33,511.7</td><td>0.055</td><td>22,412.2</td><td>620.0</td></tr><tr><td>Year 8</td><td>0.227</td><td>286,908.3</td><td>785.4</td><td>0.200</td><td>250,407.4</td><td>0.203</td><td>23,1746.5</td><td>781.8</td></tr><tr><td>Year 9</td><td>0.123</td><td>88,303.2</td><td>703.8</td><td>0.227</td><td>267,963.8</td><td>0.135</td><td>12,7253.8</td><td>740.3</td></tr><tr><td>Overall</td><td>0.099</td><td>87,996.4</td><td></td><td>0.116</td><td>117,234.2</td><td>0.098</td><td>85,909.1</td><td></td></tr></table>

4.4. Comparison between SW and other well-established and traditional methods

To study the forecasting performances of the SW method and other traditional forecasting methods, a further comparison is conducted among the SW method, CSD+LESA method, Exponential Smoothing (ES) method and Evolutionary Neural Network (ENN) method. The Winters method of ES is employed in this experiment so that the ES method can adapt to the time series with seasonality, and the ENN method which is employed here is a hybrid arti<sup>fi</sup>cial intelligence method. The real fashion sales data which is mentioned in Section 2 is used in this comparison. The comparison of the overall forecasting accuracy in MAPE is given in Table 8, together with a comparison in the computation time of these methods.

As shown in Table 8, the ES method produces a reasonably good forecasting accuracy, although it is slightly worse than the SW method, it is better than the SARIMA and the CSD+LESA methods. The ENN method produces the best forecasting accuracy among all of these methods, but it is very time-consuming in running the evolution process. While the ES method and the SARIMA method can produce forecasting result very promptly, their accuracy is much lower than SW. In terms of computational time, for SARIMA and SW models, the computational times are similar which are both less than 5 min. For CSD+LESA and ES, the computational times are very short and are less than 1 min. For ENN, the computational time is very long. In our setting for ENN, with 14 inputs of the past two weeks sales data and 10 hidden neurons, the required computational time is 5.5 h. In fact, when the neural network is represented by a binary chromosome, the ENN with 14 inputs and 10 hidden neurons has to search in a space with a size of 2<sup>14</sup> <sup>⁎</sup> <sup>10</sup>, which is obviously a huge searching space. This directly leads to a very heavy computational burden for ENN. As a consequence, from Table 8, we can observe that the SW method produces the second best result. Notice that the difference on accuracy performance between the SW and ENN methods is not big. While considering the required computational time and <sup>fl</sup>exibility in terms of applications, SW has its strength and it is actually a good choice for everyday forecasting task for highly volatile sales pattern from an industry such as fashion apparels. As a remark, when we compare SW and ES, the amount of improvement on MAPE brought by SW is 0.04 (which is equal to 9.1% of the percentage error reduction). This amount is comparable to the amount of improvement on MAPE when we compare ENN and SW (i.e., 0.05). However, ENN requires a very long computational time (5.5 h) which hinders its real world applications. Thus, even though the time for SW (b5 min) is much longer than ES (b1 min),<sup>2</sup> they both are fast enough for real-world applications. Moreover, it is well-known that ES is only good for forecasting stationary time-series [13] and its performance will generally be poor for highly volatile sales pattern whereas our study in this paper has shown that SW is much more versatile and can function well under this situation. We thus believe that SW has its strength in real world applications.

Table 8  
Forecasting comparison of different methods

<table><tr><td></td><td>SARIMA</td><td>SW</td><td>CSD + LESA</td><td>ES</td><td>ENN</td></tr><tr><td>MAPE</td><td>0.51</td><td>0.44</td><td>0.53</td><td>0.48</td><td>0.39</td></tr><tr><td>Run time</td><td>&lt;5 min</td><td>&lt;5 min</td><td>&lt;1 min</td><td>&lt;1 min</td><td>5.5 h</td></tr></table>

## 5. Discussions and conclusion

This paper studies three forecasting methods, the CSD+LESA, pure SARIMA, and the hybrid SARIMA with wavelet transform method (SW). The advantages and disadvantages of these methods are studied and compared. From our analysis, we <sup>fi</sup>nd that the CSD+ LESA method can produce good forecasting accuracy on data sets in which the white noise appears to dominate the other factors. It is the best one when the variance of the white noise component of the data is huge, but it becomes worse than SW when the variance of the seasonal cycle component of the data becomes signi<sup>fi</sup>cant. Further study shows that, for the real data set which exhibits signi<sup>fi</sup>cant seasonality, the SW method performs much better in terms of forecasting accuracy compared to the CSD+LESA method. For real data with relatively weak seasonality and highly variable seasonality factor, SW still outperforms the CSD+LESA method, which proposes to us that the CSD+LESA method fails to perform well for highly volatile sales pattern. As comparing to the SARIMA methods, both SW and CSD+LESA seem to perform better under most conditions, with an exception when the decomposed components have very signi<sup>fi</sup>- cant amplitude which cannot be omitted in the forecasting, the SARIMA method outperforms SW and CSD+LESA. This is the case when the seasonality is the dominating component. Thus, pure SARIMA is recommended in this case. We incorporate this important <sup>fi</sup>nding in our proposed forecasting scheme under SW. Observing that the CSD+LESA method can only produce the best result when the white noise is huge while the SW method produces an only slightly worse result under that condition, we believe that SW does outperform the CSD+LESA method for practical applications in forecasting sales with highly patterns.

In conclusion, we have developed a novel algorithm which combines the classic SARIMA method and the wavelet transform method (called, SW) for forecasting sales time series with a highly volatile pattern. We have conducted experiments with the use of hypothetical data sets, real sales data from the fashion industry, and some public data available online. We have identi<sup>fi</sup>ed the conditions under which SW outperforms other methods. A <sup>fi</sup>nal comparison using the real data set among various well-established methods is made and the result supports that our proposed SW method is a practical and implementable forecasting scheme for sales forecasting in an industry such as fashion.

## Acknowledgements

We sincerely thank Professor Andrew Whinston (the editor), and the anonymous reviewer for their many helpful suggestions and kind advice. We would like to thank the RGC(HK) General Research Funding Scheme (grant number: PolyU 5146/06E) and the Hong Kong Polytechnic University for providing research funding to support this piece of research. Thanks are given to C.H. Chiu for many of his helpful suggestions.

## References

[1] L. Aburto, R. Weber, Improved supply chain management based on hybrid demand forecasts, Applied Soft Computing 7 (2007) 136–144.

[2] D.D. Achabal, S.H. Mcintyre, S.A. Smith, K. Kalyanam, A decision support system for vendor managed inventory, Journal of Retailing 76 (2000) 430–454.

[3] G.E.P. Box, G.M. Jenkins, Time Series Analysis: Forecasting and Control, Holden-Day, San Francisco, 1976.

[4] C.S. Burrus, R.A. Gopinath, H. Guo, Introduction to Wavelets and Wavelet Transforms: A Primer, Prentice Hall, New Jersey, 1998

[5] P.C. Chang, C.Y. Fan, A hybrid system integrating a wavelet and TSK fuzzy rules for stock price forecasting, IEEE Transactions on Systems, Man, and Cybernetics, Part C 38 (2008) 802–815.

[6] P.C. Chang, C.Y. Lai, A hybrid system combining self-organizing maps with casebased reasoning in wholesaler's new-release book forecasting, Expert Systems with Applications 29 (2005) 183–192.

[7] P.C. Chang, Y.W. Wang, C.Y. Tsai, Evolving neural network for printed circuit board sales, Expert Systems with Applications 29 (2005) 83–92.

[8] P.C. Chang, Y.W. Wang, W.N. Yang, An investigation of the hybrid forecasting models for stock price variation in Taiwan, Journal of the Chinese Institute of Industrial Engineering 21 (2004) 358–368.

[9] T.M. Choi, D. Li, H. Yan, Mean-variance analysis for the newsvendor problem, IEEE Transactions on Systems, Man, and Cybernetics, Part A 38 (2008) 1169–1180

[10] K.C. Chui, Introduction to Wavelet, Academic Press, San Diego, CA, USA, 1992.

[11] C. Frank, A. Garg, A. Raheja, L. Sztandera, Forecasting apparel sales using mathematical modeling, International Journal of Clothing Science and Technology 15 (2003) 107–125.

[12] R. Gencay, F. Selcuk, B. Whitcher, Wavelets and other Filtering Methods in Finance andEconomics, Academic Press, New York, 2001.

[13] J.E. Hanke, D.W. Wichern, Business Forecasting, 9th ed.Prentice Hall, 2009.

[14] C.S. Hilas, S.K. Goudos, J.N. Sahalos, Seasonal decomposition and forecasting of telecommunication data: a comparative case study, Technological Forecasting & Social Change 73 (2006) 495–509.

[15] H.S. Hippert, C.E. Pedreira, R.C. Souza, Neural networks for short-term load forecasting: a review and evaluation, IEEE Transactions on Power Systems 16 (2001) 44–55.

[16] W.Y. Liang, C.C. Huang, Agent-based demand forecast in multi-echelon supply chain Decision Support Systems 42 (2006) 390–407

[17] S.G. Makridakis, S.C. Wheelright, V.E. McGee, Forecasting: Methods and Applications, 3rd ed.Wiley, New Yark, 1998.

[18] F.F. Nobre, A.B.S. Monteiro, P.R. Telles, G.D. Williamson, Dynamic linear model and SARIMA: a comparison of their forecasting performance in epidemiology, Statistics in Medicine 20 (2001) 3051–3069.

[19] K. Papagiannaki, N. Taft, Z.L. Zhang, D. Christopher, Long-term forecasting of internet backbone traffic: observations and initial models. The 18th IEEE INFOCOM Conference (San Francisco, March 30–April 3, 2003), 2003.

[20] G. Schwarz, Estimating the dimension of a model, Annals of Statistics 6 (1978) 461-464

[21] J. Taylor, Forecasting daily supermarket sales using exponentially weighted quantile regression, European Journal of Operational Research 178 (2007) 154–167.

[22] S. Thomassey, A. Fiordaliso, A hybrid sales forecasting system based on clustering and decision trees, Decision Support Systems 42 (2006) 408–421.

[23] M. Versace, R. Bhatt, O. Hinds, M. Shiffer, Predicting the exchange traded fund DIA with a combination of genetic algorithms and neural networks, Expert Systems with Applications 27 (2004) 417–425.

[24] B.L. Zhang, R. Coggins, M.A. Jabri, D. Dersch, B. Flower, Multiresolution forecasting for futures trading using wavelet decompositions, IEEE Transactions on Neural Networks 12 (2001) 765–775.

![](/api/attachments/6XCXHC4X/fulltext/images/29a38b4960a53bba2712eeb4f81ec807134f64f4b7d8ba50d3c6159f6e855244.jpg)  
Tsan-Ming Choi received his PhD from The Chinese University of Hong Kong. He is currently an associate professor at The Hong Kong Polytechnic University. His current research interests mainly focus on systems engineering and supply chain operations. He has published in leading academic journals such as IEEE Transactions on Automatic Control, Automatica, Production and Operations Management, Decision Support Systems, IEEE Transactions on Systems, Man, and Cybernetics — Parts A and B, and various other IEEE Transactions. He is the editor/co-editor of three research handbooks and seven special issues in academic journals. He is currently an associate editor of IEEE Transactions on Systems Man and Cybernetics – Part A

![](/api/attachments/6XCXHC4X/fulltext/images/e4e75f5e4834934604b225a099bdb8c9cadc877b34fb9965f1a53d968c605c0b.jpg)

Yong Yu is currently a postdoctoral research associate at the Hong Kong Polytechnic University. He received his PhD from the Hong Kong Polytechnic University and he published in journals such as Decision Support Systems and International Journal of Production Economics.

![](/api/attachments/6XCXHC4X/fulltext/images/490af4c887af8589b1c9d5c5a8bfbe51c23025b74c1756abb90c920c75437921.jpg)

Kin-fan Au is associate professor in the Institute of Textiles and Clothing of The Hong Kong Polytechnic University. His research interest is in the business aspects of fashion and textiles, particularly in the area of global trading of fashion and textile products. Dr. Au has published many papers in textiles and related journals on topics of world trading, offshore production and modelling of textiles and apparel trade.
