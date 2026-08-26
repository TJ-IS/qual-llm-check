---
otero_id: 14736
otero_key: "GUXJCHPZ"
title: "Credit risk measurement and early warning of SMEs: An empirical study of listed SMEs in China"
authors: "Xiaohong Chen; Xiaoding Wang; Desheng Dash Wu"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.03.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Credit risk measurement and early warning of SMEs: An empirical study of listed SMEs in China

Xiaohong Chen <sup>a</sup>, Xiaoding Wang <sup>a</sup>, Desheng Dash Wu <sup>b,</sup>⁎

<sup>a</sup> Business School, Central South University of China, Changsha, Hunan Province 410083, PR China

<sup>b</sup> RiskLab, University of Toronto, 19 Borden ST, Toronto, ON, Canada

## a r t i c l e i n f o

Article history: Received 22 December 2008 Received in revised form 25 January 2010 Accepted 21 March 2010 Available online 29 March 2010

Keywords: Credit risk Small and medium enterprises (SMEs) Early warning KMV mode Distance to default (DD) Asset size Split share structure reform

## a b s t r a c t

In the process of resolving <sup>fi</sup>nancing dif<sup>fi</sup>culties of small and medium enterprises (SMEs) in China, the measurement of credit risk of SMEs is a very challenging problem. In this paper we develop a novel model based on the original KMV model with tunable parameters to measure the credit risk of Chinese listed SMEs. By setting two credit warning lines to monitor the credit crisis of listed SMEs, we <sup>fi</sup>nd that the predictive accuracy of adjusted KMV model is stable to the change of default points in Chinese listed SMEs, which is different from KMV Company's existing result. Our study shows that the credit risk of listed SMEs in China is relatively high and tends to increase during the chosen period from the vear 2004 to 2006. We also find that the asset size has signi<sup>fi</sup>cant impact on credit risk and there are few credit risk <sup>fl</sup>uctuations before and after the split share structure reform.

© 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

Credit risk is the risk of loss due to a debtor's non-payment of a loan or other line of credit (either the principal or interest (coupon) or both). Default occurs when a debtor has not ful<sup>fi</sup>lled his or her legal obligations according to the debt contract, or has violated a loan covenant (condition) of the debt contract, which might occur with all debt obligations including bonds, mortgages, loans, and promissory notes. Since <sup>fi</sup>nancial innovation and derivatives grow rapidly in competitive <sup>fi</sup>nancial industry, credit risk measurement and management become essentially important.

Although small and medium enterprises (SMEs) are the most active economic units in the national economy, the operational risk and credit guarantee risk are very high in SMEs due to their particular characteristics, which lead to a low credit rating in general. The operating performance of Chinese SMEs is poor in general, which results in a high operational risk and guarantee risk to credit guarantee institutions [5,6]. The Financial System Survey Report of Chinese SMEs in 2003–2005 provided by People's Bank of China (including six major cities: Beijing, Xian, Dongguan, Taizhou, Wenzhou and Weihai), shows that 63.93% of the bank's gross bad loans are caused by SMEs. Due to the lack of effective collateral and guarantees, the banks lending to SMEs are confronting much larger default loss. According to the credit rating for 350,041 SMEs made by Industrial and Commercial Bank of China (ICBC China) in 2001, there are only 16.31% of SMEs in grade A or higher, but 83.69% of SMEs in grade BBB or lower by contrast. Credit rating is a main assessment tool referred by credit guarantee, which are very cautious to the SMEs with low credit rating. Therefore, funding shortage is one of the major problems for most SMEs which restrict their developments. Effective measurement of credit risk to SMEs has become a major challenge for <sup>fi</sup>nancial institutions. With the rapid growth of SMEs Plate and the Growth Enterprise Market (GEM) coming up in China, the SMEs will have signi<sup>fi</sup>cant in<sup>fl</sup>uence on Chinese economy as well as the capital market. However, the growth of most SMEs suffers great uncertainty and uncontinuity, in that they usually have established for a very short period and have very limited management experiences. Due to the “growth illusion”, a kind of credit risk is hardly perceived in the case of high-growth SMEs excessively relying on debt <sup>fi</sup>nancing [5]. Therefore, in this paper, we try to do some exploratory research on credit risk monitoring of Chinese listed SMEs.

The rest of the paper is organized as follows. A literature review about credit measurement and warning is provided in Section 2, followed by descriptions of the analytical models and methodologies in Section 3. Then, the parameter estimation, results comparison and analysis are discussed in Section 4. Section 5 concludes the paper.

## 2. Literature review

Before 1970s, the <sup>fi</sup>nancial institutions focused on semi-quantitative analysis in credit measurement and management, which were mainly subjective assessments of customer's credit by <sup>fi</sup>nancial statement analysis. Since 1970s, the western developed countries represented by U.S. developed a series of credit risk models on measurement and management [3]. Thereby the combination of qualitative analysis and quantitative analysis in credit risk measurement in <sup>fi</sup>nancial institutions is realized.

Currently, many models are available for credit risk measurement and credit rating [15,37]. In the main traditional credit risk measurement models, the banker's expert system and rating method are more subjective [29,30]. Furthermore, some statistical methods are commonly used for credit risk prediction. It includes logistic regression analysis [20,24,33], K nearest neighbor [13,28], multiple discriminate analysis (MDA) [16], Z-score model [1] and the improved ZETA credit risk model [26]. The general effort in credit rating prediction using statistical methods was that a simple model with a small list of <sup>fi</sup>nancial variables was succinct and was easy to explain. However, the problem is that the multivariate normality assumptions for independent variables are frequently violated in <sup>fi</sup>nancial data sets, which makes these methods theoretically invalid for <sup>fi</sup>nite samples [15]. Recently, Arti<sup>fi</sup>cial Intelligence (AI) techniques, particularly the neural networks have been used to support credit rating and bankruptcy predictions [2,7,18,34,35]. However, models obtained in this machine learning method are usually very complicated and hard to explain, and they heavily rely on the samples and experimental data.

The modern credit risk measurement model includes four major approaches: CreditMetrics, Credit Portfolio View, CreditRisk+ and KMV model. The J.P. Morgan's CreditMetrics [8] and McKinsey's Credit Portfolio View [36] are directly related to the credit rating mechanism. However, because China's credit rating market is far from mature and lacks suf<sup>fi</sup>cient credit data, the above two models (CreditMetrics and Credit Portfolio View) cannot be used in China. It is also very dif<sup>fi</sup>cult to apply the CreditRisk+ model [31] developed by the Credit Suisse Financial Products into Chinese credit market; that is because the key risk-driven parameter “default rate” of CreditRisk+ model is hard to estimate in present credit market of China. Moreover, the model requires the mutual debts to be independent [9]. The KMV model developed by the KMV Corporation is a structural model based on the modern corporate <sup>fi</sup>nance theory and the option theory. It would be very attractive to apply it to credit market of Chinese SMEs, where the <sup>fi</sup>nancial data and credit information are insuf<sup>fi</sup>cient, patchy or even doesn't exist at all. The KMV model can use appearance information for measurement, such as the <sup>fl</sup>uctuation of stock prices, credibility, macro-economic conditions, and sector's credit risk. It is a dynamic forward-looking approach.

Previous studies con<sup>fi</sup>rm that the KMV model can be applied in the credit market. McQuown [22] pointed out that the <sup>fi</sup>nancial report could re<sup>fl</sup>ect the history of the company and the market price could re<sup>fl</sup>ect the future development trend much better, yet the most accurate measurement of credit risk should use both information at the same time. Kurbat and Korablev [19] tested the KMV model by level validation and calibration analysis. They proved that the KMV model was very effective using the datum of 1000 U.S. companies in three years. Crosbie and Bohn [10] applied KMV model into <sup>fi</sup>nancial companies and found that EDF value could accurately and sensitively monitor the credit changes before insolvency or when a credit event happened. The “New Basel Capital Accord” promoted Internal Ratings-Based (IRB) approach in credit risk management, where KMV was also recommended. It is clear that KMV model has been highly accepted and used in the world.

In recent years, Chinese scholars discussed the applicability of KMV model in China. Du et al. [11] focused on qualitative analysis of the model and pointed out problems in using KMV. Wang [32] provided comparative study of KMV and other credit risk models. He considered that the KMV model was more suitable for credit risk assessment of listed companies than other models. Recently, some scholars began to apply KMV model into credit risk identi<sup>fi</sup>cation in listed companies. Cheng and Wu [6] (sample number is 15), Zhang et al. [40] (sample number is 60), Yang and Zhang [38] (sample number is 144) and Ye et al. [39] (sample number is 22) adjusted the parameters of KMV model and found that the adjusted model could timely identify and forecast the credit risk of Chinese listed companies. Zheng [42] (sample number is 30) found that the EDF model did not send wrong messages to the listed companies with good performance, but the asset value and equity value in high-risk listed companies were overvalued. Ma [21] applied KMV model into the <sup>fi</sup>nancial distress warning of Chinese listed companies, and found that KMV model had more obvious advantages than the Logistic and Fisher model. Although previous works provide theoretical and empirical proofs that the KMV model is a good guidance and reference for quantitative credit risk management in China, the inference cannot be made directly to Chinese market. Some existing works have discussed the relationship between asset size and default. Moody company's study shows that the asset size is an important factor affecting default. The default probability is very high in large companies who are well-funded, solid and capable of market risks resistance [14]. While in small-sized listed companies, the default probability is big due to the big volatility of stock price [41]. In this paper, we will discuss how the default probability is affected by various risk factors in Chinese listed SMEs. Traditional KMV model used to determine equity value volatility (σ ) by simply adopting stock price volatility, but the effects of equity changes (e.g., the shares distribution) and changes in net assets per share are not considered. This paper will adjust some parameters in KMV model and develop improved version of KMV model to meet the needs of Chinese listed SMEs' credit market. As a unique phenomenon in China, the split share structure reform will also be discussed

## 3. Models

## 3.1. KMV modeling description

KMV model developed by the KMV Company is based on the Merton Option Pricing Theory [23]. It is a set of conceptual frameworks to estimate the default probability of a company. The KMV model assumes that the company will default when the company's asset value is less than liabilities. Fig. 1 reveals the relationship between equity value and asset value. According to the basic idea of Merton model, the KMV model regards the company's equity value as the call option, which considers asset value as the underlying asset and the debt as the exercise price.

![](/api/attachments/GUXJCHPZ/fulltext/images/4252f8b602a8b9db32ff503dc7ecb4b2ce32db7a76cb83155511fcfb56d4456e.jpg)  
Fig. 1. The relationship between equity value and asset value.

<table><tr><td>Time</td><td>2004.1.1–2004.10.28</td><td>2004.10.29–2006.8.20</td><td>2006.8.21–2006.12.31</td></tr><tr><td>Annual percentage rate (APR)</td><td>0.0198</td><td>0.0225</td><td>0.0252</td></tr></table>

In Fig. 1, L denotes the shareholders' initial investment in the company; D denotes the debts in default point. When the asset value (V) is more than the debts (D), shareholders will choose not to default and gain remaining pro<sup>fi</sup>ts after paying debts, which is consistent with an increasing equity value in Fig. 1, and it indicates the call option is executed. While, when the asset value is less than the debts, shareholders will choose default by transferring the total assets to the creditors, which is consistent with a constant equity value in Fig. 1, and it means the call option is not executed [4,10,17,25].

According to the above analysis, we can derive from the Black– Scholes option pricing formula that:

$$
\begin{array}{r} E = V N (d _ {1}) - D e ^ {- r \tau} N (d _ {2}) \\ = f (V, \sigma_ {V}, r, D, \tau), \end{array}\tag{1}
$$

where E denotes the equity value, V denotes the asset value, D denotes the default point, $\sigma _ { v }$ denotes the asset value volatility, r denotes the risk free rate, τ denotes the debt maturity, $N ( \cdot )$ denotes the standard normal cumulative distribution function. In Eq. (1), $d _ { 1 }$ and d can be calculated as follows:

$$
d _ {1} = \frac {\ln (V / D) + (r + \sigma_ {V} ^ {2} / 2) \tau}{\sigma_ {V} \sqrt {\tau}},\tag{2}
$$

$$
d _ {2} = \frac {\ln (V / D) + (r - \sigma_ {V} ^ {2} / 2) \tau}{\sigma_ {V} \sqrt {\tau}} = d _ {1} - \sigma_ {V} \sqrt {\tau}.\tag{3}
$$

There are two unknown parameters V and $\sigma _ { v }$ in Eq. (1) that need to be solved. This can be achieved by introducing the relationship between the equity value volatility (σ ) and the asset value volatility (σ<sub>V</sub>) [14] (see Eq. (4)).

$$
\begin{array}{c} \sigma_ {E} = \frac {V N (d _ {1})}{E} \sigma_ {V} \\ = g (V, \sigma_ {V}, r, D, \tau). \end{array}\tag{4}
$$

After substituting Eqs. (1) and (2) into Eq. (4), we can derive that $\sigma _ { E }$ is the function of V, $\sigma _ { V } , r , D$ and τ.

Thereby, we set a system of equations from Eqs. (1) and (4), where V and $\sigma _ { v }$ are unknown parameters (see Eq. (5)).

$$
\left\{ \begin{array}{l} f (V, \sigma_ {V}) - E = 0 \\ g (V, \sigma_ {V}) - \sigma_ {E} = 0 \end{array} \right.\tag{5}
$$

Then we calculate the Jacobian Matrix of the functions. According to the Newton-iterative method, which builds iteration through Taylor expansion, we get Eq. (6).

$$
\binom{V ^ {(k + 1)}}{\sigma_ {V} ^ {(k + 1)}} = \binom{V ^ {(k)}}{\sigma_ {V} ^ {(k)}} - \left( \begin{array}{c c} \frac {\partial f}{\partial V} & \frac {\partial f}{\partial \sigma_ {V}} \\ \frac {\partial g}{\partial V} & \frac {\partial g}{\partial \sigma_ {V}} \end{array} \right) ^ {- 1} \binom{f (V ^ {(k)}, \sigma_ {V} ^ {k}) - E}{g (V ^ {(k)}, \sigma_ {V} ^ {(k)}) - \sigma_ {E}},\tag{6}
$$

where the appropriate initial values $( V ^ { 0 } , \sigma _ { V } ^ { 0 } )$ in Newton iteration are set by use of the trial-and-error method. We have tested nine groups of values $( V ^ { 0 } , \sigma _ { V } ^ { 0 } )$ : three values for initial asset size value $\hat { V } ^ { 0 }$ and three for initial volatility value $\sigma _ { V } ^ { 0 } .$ Our sample size falls in the range of (1.0E+07, 1.0E+09), so we test three levels of values: 1.0E+07, 1.0E+08 and 1.0E+09 for $V ^ { 0 } .$ . The three levels of volatility values are 0.1, 0.01 and 0.001. Computation in trial and error shows that the initial value of (1.0E+09, 0.01) can achieve iteration convergence and the convergence is fast. Based on this, we can calculate the values of V and $\sigma _ { V } .$

When V and $\sigma _ { V }$ are given, the distance to default (DD) in indebted companies can be calculated [10]. In KMV model, DD is de<sup>fi</sup>ned as:

$$
D D = \frac {V - D}{V \sigma_ {v}}.\tag{7}
$$

It is assumed that the asset value of the company follows the normal distribution, thus the default distance re<sup>fl</sup>ects the standard deviation from company's default. Then we can get the company's expected default frequency (EDF):

$$
E D F = N (- D D).\tag{8}
$$

However, the assumption that the asset value is subject to normal distribution is questionable. The KMV Company tries to obtain the empirical value of EDF rather than the theoretical value from models. Fortunately, KMV Company has a huge historical database on default information of companies. They can count the number of default companies with same DD in a year. Then, the empirical value of EDF is the ratio of the above counts to the total number of companies with the same DD. While at present, there is no similar database in Chinese credit market, which means no EDF statistics is available. So in this paper, we take DD as the basis of credit evaluation. DD is a standard index re<sup>fl</sup>ecting the company's credit quality, which can be compared for different companies and for different periods of time. The greater the value is, the more likely the company is to repay debts in due time, as a consequence the defaults will be less and the credit will be better.

## 3.2. Parameter setting

We discuss the calculation of <sup>fi</sup>ve key parameters in this section. The <sup>fi</sup>rst parameter is equality value (E). Prior to China's split share structure reform, domestic A shares were divided into two classes: one type being freely bought and sold by normal investors (tradable shares) and the other that cannot be freely traded (non-tradable shares). This is a special phenomenon in Chinese securities market according to the Code of Good Practice of Exercise of State-owned Corporation Shares [41,43]. The value of non-tradable shares is hard to be estimated and usually lower than the value of tradable shares. If the price of per non-tradable share is simply represented by the price of per tradable share, the company's equity value will be overestimated. Therefore, in this paper we follow the Code of Good Practice of Exercise of State-owned Corporation Shares set by Chinese regulators, and use net assets per share to represent the non-tradable shares price [43]. We can get:

Table 2 DD in three default points.

<table><tr><td colspan="3">Time</td><td>04/3</td><td>04/6</td><td>04/9</td><td>04/12</td><td>05/3</td><td>05/6</td><td>05/9</td><td>05/12</td><td>06/3</td><td>06/6</td><td>06/9</td><td>06/12</td></tr><tr><td rowspan="9">DD mean</td><td rowspan="3"> $D_0$ </td><td>Non-ST</td><td>63.86</td><td>57.26</td><td>59.26</td><td>71.49</td><td>60.19</td><td>60.86</td><td>61.18</td><td>73.17</td><td>70.12</td><td>50.45</td><td>58.34</td><td>52.58</td></tr><tr><td>ST</td><td>40.74</td><td>41.55</td><td>37.71</td><td>37.12</td><td>30.42</td><td>29.64</td><td>27.65</td><td>24.81</td><td>25.63</td><td>25.37</td><td>28.50</td><td>34.36</td></tr><tr><td>Mean-difference</td><td>23.12</td><td>15.71</td><td>21.55</td><td>34.37</td><td>29.77</td><td>31.22</td><td>33.53</td><td>48.36</td><td>44.49</td><td>25.08</td><td>29.84</td><td>18.22</td></tr><tr><td rowspan="3"> $D_1$ </td><td>Non-ST</td><td>63.88</td><td>57.28</td><td>59.28</td><td>71.52</td><td>60.21</td><td>60.90</td><td>61.22</td><td>73.21</td><td>70.17</td><td>50.49</td><td>58.36</td><td>52.61</td></tr><tr><td>ST</td><td>40.75</td><td>41.57</td><td>37.74</td><td>37.14</td><td>30.44</td><td>29.66</td><td>27.67</td><td>24.82</td><td>25.65</td><td>25.39</td><td>28.53</td><td>34.37</td></tr><tr><td>Mean-difference</td><td>23.13</td><td>15.71</td><td>21.54</td><td>34.38</td><td>29.77</td><td>31.24</td><td>33.56</td><td>48.40</td><td>44.52</td><td>25.09</td><td>29.84</td><td>18.24</td></tr><tr><td rowspan="3"> $D_2$ </td><td>Non-ST</td><td>63.83</td><td>57.23</td><td>59.23</td><td>71.45</td><td>60.15</td><td>60.81</td><td>61.13</td><td>73.10</td><td>70.05</td><td>50.40</td><td>58.27</td><td>52.55</td></tr><tr><td>ST</td><td>40.72</td><td>41.53</td><td>37.68</td><td>37.11</td><td>30.41</td><td>29.62</td><td>27.64</td><td>24.79</td><td>25.61</td><td>25.35</td><td>28.48</td><td>34.34</td></tr><tr><td>Mean-difference</td><td>23.12</td><td>15.70</td><td>21.55</td><td>34.34</td><td>29.74</td><td>31.20</td><td>33.49</td><td>48.30</td><td>44.45</td><td>25.06</td><td>29.78</td><td>18.20</td></tr></table>

Note: $D _ { 0 } \colon$ = current liabilities + 0.5×long-term liabilities. D₁ = current liabilities $D _ { 2 } { : }$ = current liabilities + long-term liabilities

Table 3 T-test statistics.

<table><tr><td rowspan="2">DD</td><td rowspan="2"></td><td colspan="2">Levene&#x27;s test for equality of variances</td><td colspan="5">T-test for equality of means</td></tr><tr><td>F</td><td>Significant level</td><td>t</td><td>df</td><td>Significant level (2-tailed)</td><td>Mean-difference</td><td>Standard error difference</td></tr><tr><td rowspan="3">Equal variances assumed</td><td> $D_0$ </td><td>0.006</td><td>0.937</td><td>10.977</td><td>22</td><td>0.000</td><td>29.605</td><td>2.697</td></tr><tr><td> $D_1$ </td><td>0.007</td><td>0.935</td><td>10.979</td><td>22</td><td>0.000</td><td>29.617</td><td>2.698</td></tr><tr><td> $D_2$ </td><td>0.006</td><td>0.938</td><td>10.973</td><td>22</td><td>0.000</td><td>29.577</td><td>2.695</td></tr></table>

Wilcoxon test statistics.

<table><tr><td>DD</td><td> $D_0$ </td><td> $D_1$ </td><td> $D_2$ </td></tr><tr><td>Wilcoxon W</td><td>78.000</td><td>77.800</td><td>77.900</td></tr><tr><td>Z</td><td>-4.157</td><td>-4.156</td><td>-4.157</td></tr><tr><td>Significant level (2-tailed)</td><td>0.000</td><td>0.000</td><td>0.000</td></tr></table>

$$
\begin{array}{r l} \text { Equity   Value } & = \text { the   Closing   Price   of   Tradable   Shares } \\ & \times \text { the   Number   of   Tradable   S   hares } + \text { Net   Assets   per   Share } \\ & \times \text { the   Number   of   Non - tradable   Shares }, \end{array} \tag {9}
$$

where the number of non-tradable shares includes the limited sale of shares in the split share structure reform. The second parameter is equity value volatility (σ ). We introduce a new way to calculate this parameter. Not only the tradable shares price but also the equity changes (such as equity donation, distribution and orientation repurchase in the split share structure reform) and quarterly changes of net assets per share are all considered in the calculation of $\cdot _ { \sigma _ { E } } .$ . It can effectively improve the accuracy in calculation of $\sigma _ { E } . \mathsf { A }$ large number of facts proved that GARCH (1, 1) model applies well to the Chinese stock market [27]. In this paper, after the equity value (E) in each trading day has been calculated, we use GARCH toolbox in Matlab to calculate equity value volatility.

The third parameter is default point (D). KMV Company found that the companies generally do not default when their assets value is up to the book value of total liabilities [10]. When the company defaults, the asset value is generally between the current liabilities and the book value of total liabilities, which can be described to:

$$
D = C L + k \times L L, 1 \geq k \geq 0,\tag{10}
$$

where D denotes default point, CL denotes current liabilities, and LL denotes long-term liabilities. By doing a great deal of observations to the default companies, KMV Company found that the most frequent default point is at $k = 0 . 5 ,$ , and the predictive accuracy of model is sensitive to the changes of default point [10,17]. But this default point is an experiential value based on American companies, which may not be suitable for the listed SMEs in China. The default point must be set by considering the debt structure of a company and the credit situation of a country. Thus, obviously we face a big hurdle in determining the default point of Chinese listed SMEs. Previous studies on default point setting are generally similar to the KMV Company's [27,40]. None of the existing research discussed default points and credit risk of SMEs yet. In this paper, we <sup>fi</sup>rst set three scenarios: $k = 0 . 5 ( D _ { 0 } ) , \ k = 0 ( D _ { 1 } )$ , and $k = 1 \ \left( D _ { 2 } \right)$ , and then compare the effectiveness of credit risk model in Chinese listed SMEs in these three scenarios.

The fourth and <sup>fi</sup>fth parameters are liability maturity (τ) and risk free rate (r). Because of the limited availability of data and information, the calculation time is set for one year to predict the credit risk in next year. While the setting time is consistent with other existing studies, it would be helpful to examine the results. For the risk free rate, we adopt one-year time deposit rate published by the People's Bank of China (see Table 1).

## 4. Parameter and model effectiveness

## 4.1. Sampling and data preprocessing

The data window is from 2004 to 2006. We select samples from listed SMEs in China under the following steps: a) the companies should be listed in Shanghai and Shenzhen Stock Exchange before December 31, 2005 and only issued A shares, which ensures the analyzing time being more than one year. b) The tradable shares of the company are less than 50 million in the period of 2004 to 2006, and by December 31, 2003, the main income or the total assets are less than 500 million RMB and the number of employees is less than 2000 people, which meet the SME Standard in China. c) There is no missing data. After the <sup>fi</sup>rst screening, there are 80 samples that matched. The raw datum are quarterly datum from 2004 to 2006, including net assets per share, current liability, long-term liability, the closing stock price of each trading day, the tradable shares and the non-tradable shares. The entire datum is from Wind Database and Dragoninfo Financial Information References System (DFIRS).

![](/api/attachments/GUXJCHPZ/fulltext/images/c1ce59447cdef0eaaa5cbb44600ce78f7c2451fe703d75e356e565d65ee41b33.jpg)  
Fig. 2. DD difference between non-ST and ST at three points.

Table 5  
![](/api/attachments/GUXJCHPZ/fulltext/images/56c08bd5c83d3a846796d1d4c9e185db510a707390d9eaac98eb8798195c3519.jpg)  
Fig. 3. The number of ST and non-ST companies in different DD intervals.

We execute the Newton-iterative algorithm of KMV model in Matlab software to calculate $V , \sigma _ { V }$ and then DD. The default points are set at $D _ { 0 } , D _ { 1 }$ , and $D _ { 2 }$ respectively. But for one sample we cannot get result from the iteration due to its negative equity value, which cannot be executed in GARCH toolbox in Matlab. Finally, we get 79 sets of results on $V , ~ \sigma _ { V }$ and DD for 12 quarters from 2004 to 2006. The effective samples include 20 ST&\*ST companies and 59 non-ST companies. ST companies are those being special treated because of negative net pro<sup>fi</sup>ts in consecutive years. \*ST companies are those suffering from losses for three consecutive years.

## 4.2. Model validity verification and comparison in different default points

It is generally held that the ST&\*ST companies are in <sup>fi</sup>nancial crisis. They may have higher credit risks than the general ones. We divide the total samples into two groups: Group1 including 20 ST&\*ST companies and Group 2 with 59 non-ST companies.

Firstly, we compare the means of DD in two groups from March, 2004 to December, 2006. The statistics of DD at three default points are shown in Table 2. The results indicate that DD in non-ST companies are all larger than those in ST companies, which re<sup>fl</sup>ects the fact that default risk in non-ST companies is much smaller. It means the DD results yielded from KMV model are valid. Then we conduct a test for two-independent samples to verify the signi<sup>fi</sup>cant difference in DD between non-ST and ST companies (see Tables 3 and 4). The T-test and Wilcoxon test statistics show that the DD of two groups have signi<sup>fi</sup>cant difference at the level of $\alpha = 5 \%$ at three default points, and their respective populations have the same distribution. It indicates that adjusted KMV model can effectively discriminate the default risk in listed SMEs.

The number of ST and non-ST companies in different critical points.

<table><tr><td>DD</td><td>Number (ST)</td><td>Number (non-ST)</td></tr><tr><td>≤30</td><td>8</td><td>0</td></tr><tr><td>&gt;30</td><td>12</td><td>59</td></tr><tr><td>≤50</td><td>18</td><td>21</td></tr><tr><td>&gt;50</td><td>2</td><td>38</td></tr><tr><td>≤70</td><td>20</td><td>44</td></tr><tr><td>&gt;70</td><td>0</td><td>15</td></tr><tr><td>Total</td><td>20</td><td>59</td></tr></table>

Table 6  
The sensitivity and speci<sup>fi</sup>city in different critical points.

<table><tr><td>Critical point</td><td>Sensitivity</td><td>Specificity</td></tr><tr><td>30</td><td>0.40</td><td>0.00</td></tr><tr><td>50</td><td>0.90</td><td>0.36</td></tr><tr><td>70</td><td>1.00</td><td>0.75</td></tr></table>

The mean-difference of DD between non-ST and ST companies gradually increases from 2004 to 2005 and decreases in 2006, and the trends of the DD difference at the three points are almost overlapped (see Fig. 2), which means the DD differences in non-ST and ST companies are stable to the changes of default point.

In order to further verify and compare the validity of KMV model in risk identi<sup>fi</sup>cation, we introduce the Receiver Operating Characteristic Curves (ROC). ROC is used for analyzing the accuracy of classi<sup>fi</sup>cation criteria, which is particularly effective in comparing the accuracy when a variety of classi<sup>fi</sup>cations exist [12]. Many Chinese scholars have also used ROC in the study of KMV model [27,40]. In this paper, we take the case in June 30, 2005 as an example to describe the principle of ROC curve. Fig. 3 shows the number of ST and non-ST companies in different DD intervals. Table 5 shows the cumulative number of ST and non-ST companies when DD is lower than the critical point.

In this paper, the sensitivity is de<sup>fi</sup>ned as the proportion that ST companies are exactly judged to special treatment (ST), the speci<sup>fi</sup>city is de<sup>fi</sup>ned as the proportion that non-ST companies are exactly judged to be outside of ST, the false rate is de<sup>fi</sup>ned as the proportion that non-ST companies are falsely judged to ST and the false rate is just equal to (1−speci<sup>fi</sup>city). As shown in Table 6, when $\mathrm { D D } \leq 3 0$ is viewed as the judgment criterion of ST, the corresponding sensitivity and speci<sup>fi</sup>city are 0.40 and 0.00 respectively. When $\mathrm { D D } \leq 5 0$ is viewed as the judgment criterion of ST, the sensitivity and speci<sup>fi</sup>city values are 0.90 and 0.36 respectively. When DD≤70 is viewed as the judgment criterion of ST, the values are up to 1.00 and 0.75. Then we can get the ROC curve presented in false rate (1−speci<sup>fi</sup>city) (X-axis) and sensitivity (Y-axis) (see Fig. 4 as an example). It shows the relationship between the false judgment rate of non-ST and the true judgment rate of ST in different critical points of DD.

![](/api/attachments/GUXJCHPZ/fulltext/images/61743a2c57955530d5b1359ef122281328ffbff4e6622848fa387f317323e485.jpg)  
Fig. 4. The ROC curve under three default points (in June 30, 2005)

Table 7  
The area under ROC curve in 12 time points.

<table><tr><td></td><td>04/3</td><td>04/6</td><td>04/9</td><td>04/12</td><td>05/3</td><td>05/6</td><td>05/9</td><td>05/12</td><td>06/3</td><td>06/6</td><td>06/9</td><td>06/12</td><td>Mean</td><td>Standard Deviation</td></tr><tr><td> $D_0$ </td><td>0.869</td><td>0.755</td><td>0.873</td><td>0.840</td><td>0.869</td><td>0.889</td><td>0.911</td><td>0.923</td><td>0.902</td><td>0.752</td><td>0.838</td><td>0.815</td><td>0.853</td><td>0.056</td></tr><tr><td> $D_1$ </td><td>0.871</td><td>0.753</td><td>0.874</td><td>0.840</td><td>0.869</td><td>0.889</td><td>0.914</td><td>0.927</td><td>0.903</td><td>0.752</td><td>0.836</td><td>0.815</td><td>0.8536</td><td>0.057</td></tr><tr><td> $D_2$ </td><td>0.869</td><td>0.752</td><td>0.873</td><td>0.840</td><td>0.869</td><td>0.888</td><td>0.911</td><td>0.923</td><td>0.900</td><td>0.754</td><td>0.838</td><td>0.815</td><td>0.8527</td><td>0.056</td></tr></table>

We can use the area under ROC curve to measure the accuracy of KMV model in distinguishing ST and non-ST companies. When the area is in the range of (0.90, 1.00), the accuracy of the model is excellent. When the area is in the range of (0.80, 0.90), the accuracy is good. When the area is in the range of (0.70, 0.80), the accuracy is fair. When the area is in the range of (0.60, 0.70), the accuracy is poor. When the area is in the range of (0.50, 0.60), the accuracy is poor and the model fails.

Table 7 shows the area under ROC curve at three default points from March 2004 to December 2006. The average areas at three default points are 0.8530, 0.8536 and 0.8527 respectively. It indicates that the KMV model can accurately distinguish ST and non-ST companies at three default points. The statistics show that the accuracy at $D _ { 1 }$ (D = Current Liabilities) is a little better than at other two points. But the paired samples T-test shows no signi<sup>fi</sup>cant difference at the three points. It means the predictive accuracy of KMV model is stable. Combining with the results in Fig. 2, we can conclude that the predictive accuracy of KMV model is stable to the changes of default point in Chinese listed SMEs, which is different from the result of KMV Company that the prediction accuracy of KMV model is sensitive to the changes of default points.

## 4.3. Credit risk and warning of Chinese listed SMEs

In this section, we will discuss the situation of credit risk in Chinese listed SMEs and try to set the credit risk warning lines. To facilitate the comparison with previous studies, we choose default point at $D _ { 0 }$ for the following analysis.

The following analysis is based on three groups of samples. Group 1 includes 20 ST&\*ST companies and group 2 includes the rest 59 non-ST companies in Section 4.2. Group 3 includes 20 blue chips companies selected from non-ST companies, which have the best performance and the most average earnings per share (fully diluted)

![](/api/attachments/GUXJCHPZ/fulltext/images/24668e5da08c976ee1d3dc1d64d3d1368606b2dbdaa6d5f92b0f4019d1c3167a.jpg)  
Fig. 5. Distance to default values of ST, non-ST and blue chips.

![](/api/attachments/GUXJCHPZ/fulltext/images/e26a5be56627c1b6a2ca15961e58c273480dc9ecf26f889aa100ac5d792b927a.jpg)  
Fig. 6. Default distance statistics of listed SMEs

Table 8  
A DD comparison with previous studies.

<table><tr><td rowspan="2">Sample</td><td rowspan="2">Time</td><td colspan="2"> $E$  calculation: whether consider</td><td colspan="2"> $\sigma_{E}$  estimation: whether consider</td><td rowspan="2">DD interval with largest ST frequency</td><td rowspan="2">Source</td></tr><tr><td>Tradable shares pricing</td><td>Non-tradable shares pricing</td><td>Equity changes</td><td>Net assets per share</td></tr><tr><td>80 listed SMEs</td><td>2004–2006</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>&lt;30</td><td>This paper</td></tr><tr><td>15 A shares</td><td>2000</td><td>Yes</td><td>No</td><td>No</td><td>No</td><td>&lt;2</td><td>[6]</td></tr><tr><td>30 A shares</td><td>1998–2001</td><td>Yes</td><td>No</td><td>No</td><td>No</td><td>&lt;4</td><td>[40]</td></tr><tr><td>22 A shares</td><td>2000–2003</td><td>Yes</td><td>Yes</td><td>No</td><td>Yes</td><td>&lt;8</td><td>[39]</td></tr><tr><td>60 A shares</td><td>1999–2002</td><td>Yes</td><td>Yes</td><td>No</td><td>Yes</td><td>&lt;4</td><td>[42]</td></tr><tr><td>852 A shares</td><td>2002</td><td>Yes</td><td>No</td><td>No</td><td>No</td><td>&lt;3</td><td>[21]</td></tr></table>

## Table 9

ST frequency in 2004–2006.

<table><tr><td>ST frequency</td><td>≤30</td><td>30-40</td><td>40-50</td><td>50-60</td><td>60-70</td><td>70-80</td><td>80-90</td><td>&gt;90</td></tr><tr><td>200403</td><td>1</td><td>0.7</td><td>0.357</td><td>0.182</td><td>0.2</td><td>0</td><td>0.143</td><td>0</td></tr><tr><td>200406</td><td>1</td><td>0.421</td><td>0.235</td><td>0.1</td><td>0.5</td><td>0</td><td>0.333</td><td>0</td></tr><tr><td>200409</td><td>1</td><td>0.454</td><td>0.235</td><td>0.15</td><td>0.125</td><td>0</td><td>0</td><td>0</td></tr><tr><td>200412</td><td>0.9</td><td>0.571</td><td>0.125</td><td>0.3</td><td>0.071</td><td>0</td><td>0.167</td><td>0.067</td></tr><tr><td>200503</td><td>0.917</td><td>0.444</td><td>0.091</td><td>0.111</td><td>0.083</td><td>0.167</td><td>0</td><td>0</td></tr><tr><td>200506</td><td>1</td><td>0.538</td><td>0.167</td><td>0.083</td><td>0.077</td><td>0</td><td>0</td><td>0</td></tr><tr><td>200509</td><td>1</td><td>0.3</td><td>0.143</td><td>0.067</td><td>0.077</td><td>0</td><td>0</td><td>0</td></tr><tr><td>200512</td><td>1</td><td>0.5</td><td>0.333</td><td>0.071</td><td>0.083</td><td>0</td><td>0</td><td>0</td></tr><tr><td>200603</td><td>1</td><td>0.636</td><td>0</td><td>0.2</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>200606</td><td>0.769</td><td>0.176</td><td>0.158</td><td>0.056</td><td>0.25</td><td>0</td><td>0</td><td>0</td></tr><tr><td>200609</td><td>0.636</td><td>0.636</td><td>0.091</td><td>0.059</td><td>0.091</td><td>0</td><td>0</td><td>0</td></tr><tr><td>200612</td><td>0.667</td><td>1</td><td>0.167</td><td>0</td><td>0.5</td><td>0</td><td></td><td></td></tr><tr><td>3-year average</td><td>0.907</td><td>0.531</td><td>0.175</td><td>0.115</td><td>0.171</td><td>0.014</td><td>0.058</td><td>0.006</td></tr></table>

in three years among the total samples. Group 3 is set as the reference group. Fig. 5 demonstrates a comparison of default distances (DD) among the three groups. We <sup>fi</sup>nd that DD in non-ST companies and blue chips are much bigger than in ST companies, which means it is much likely to default in ST companies than in non-ST and blue ones in Chinese listed SMEs. And DD differences between non-ST companies and blue chips are very small, the DD trends of two groups are almost overlapping from 2004 to 2006. The DD trends in ST companies seem much smoother than those in other two groups, which means the DD of ST companies has small changes in three years. It can be concluded that ST companies keeps high default risk for several years, especially in 1–2 years before or after being identi<sup>fi</sup>ed as ST. Combining with Figs. 5 and 2, we <sup>fi</sup>nd that the DD difference between ST and non-ST companies is more and more obvious from 2004 to 2005 due to the improving credit in non-ST companies and the declining credit in ST companies. In 2006, the difference began to slow down, where the credit in non-ST companies decreases a lot but increase slightly in ST companies.

Fig. 6 describes the default distance statistics of listed SMEs. We <sup>fi</sup>nd that the credit in three years is stable. In general, DD <sup>fl</sup>uctuates within the range from 50 to 60 and shows a slight decrease in 2006. The mean and standard deviation of DD change in the same direction with a correlation coef<sup>fi</sup>cient of 0.831, which shows a resonance. This is mainly due to some companies' sudden credit improvement in short time, which brings a quick growth of DD and enlarges the difference between DD and the total average value of DD. It is coincident that DD changes a little in the <sup>fi</sup>rst three quarters and increases a lot in the last quarter both in 2004 and 2005, which indicates that some <sup>fi</sup>nancial information of the Chinese listed SMEs disclosed to public may be fabricated. DD in ST companies is getting smaller from 2004 to 2005 and has a slow recovery in 2006. It means the credit of ST companies is poor in the <sup>fi</sup>rst two years, the closer to be ST, the bigger the default risk is. In 2006, with the help of recapitalization, asset injection, recover arrears and <sup>fi</sup>nancial subsidies, some ST companies get the chance to get rid of de<sup>fi</sup>cits, and the credit tends to get better. The ST label may be removed as expected.

Table 8 shows a DD comparison with previous literatures. We <sup>fi</sup>nd that the DD in this paper is bigger than in previous studies. This is mainly due to a certain model parameter setting, where we take the equity changes (especially induced by the split share structure reform) and the change of net assets per share into consideration to estimate the value of σ . As a result, the equity volatility is much less than previous studies. Because the parameters are adjusted, we can hardly compare our results with existing works based on large companies. However, we can set credit early-warning lines by DD to monitor credit crisis in listed SMEs.

We divide DD into 8 intervals. The frequencies of ST companies in 8 intervals in three years are shown in Table 9. Fig. 7 illustrates the accumulative DD at the end of 2005 and Fig. 8 illustrates the average frequency line of ST in three years. We can conclude that the smaller the DD is, the larger the ST frequency is, which once again veri<sup>fi</sup>es the validity of KMV model on credit rating of listed SMEs. By studying statistics of three years, we <sup>fi</sup>nd ST frequency is the largest when

![](/api/attachments/GUXJCHPZ/fulltext/images/2396a44a070c460733e82dea24961bdf9891c846a753b1ac1b9d8f95d3790e8c.jpg)  
Fig. 7. The accumulative state of DD in 2006 (ST frequency is depicted in black)

![](/api/attachments/GUXJCHPZ/fulltext/images/19e37dc7da79e2b59905918a91e6df37b76817475c3a7e30d020055bd3eff2db.jpg)  
Fig. 8. ST frequency line.

Table 10 DD in different asset sizes.

<table><tr><td></td><td>Size range (100 million yuan)</td><td>The average DD in 3 years</td></tr><tr><td>Small-sized</td><td>0.42–3</td><td>43.262</td></tr><tr><td>Medium-sized</td><td>3.86–5</td><td>55.589</td></tr><tr><td>Large-sized</td><td>6–13.5</td><td>57.984</td></tr></table>

DD∈(−∞, 30). So DD=40 is set for the second grade of credit earlywarning line and DD=30 is set for the <sup>fi</sup>rst grade of credit earlywarning line. We can draw a curve for real-time DD changes. By observing DD in September and December in 2006, including three listed companies under temporary suspension, there are 25 companies (31.6% of total samples) below the second grade warning and 15 companies (18.99% of total samples) below the <sup>fi</sup>rst grade warning. That means half of the listed SMEs below the second grade warning will be in credit crisis in 2007. And 90% of the listed SMEs below the <sup>fi</sup>rst grade warning will be in credit crisis in 2007, the credit situation should be alerted, and some remedy measures should be taken as soon as possible. Thus we <sup>fi</sup>nd, the credit risk of listed SMEs in China is large and the credit situation is not optimistic.

## 4.4. Asset size and credit risk

The previous result shows that the credit risk of Chinese listed SMEs is very big. Comparing the ST frequency line based on 852 medium and large companies in china [21] with the ST frequency line in Fig. 8, we <sup>fi</sup>nd that the default probability in listed SMEs is much bigger than in medium and large companies in China. However, whether credit risk is related to the asset size needs a further discussion. We sort all the samples in descending order according to their 3-year average total assets. The top 20 ranked companies are de<sup>fi</sup>ned as the large-sized group, the last 20 ranked companies are de<sup>fi</sup>ned as the small-sized group, and the rest 19 companies in the middle is de<sup>fi</sup>ned as the medium-sized group. The relationships of assets and DD in three groups are shown in Table 10. Fig. 9 shows the time series of DD in these three groups. Table 10 and Fig. 9 indicate that DD in small-sized SMEs is much lower than in medium and largesized SMEs in general, and the DD trends in medium-sized group and in large-sized group are almost the same, but the former is a little smaller than the latter. That means the probability of default is the largest in small-sized listed SMEs and is much lower in medium and large-sized ones, and the differences between medium and largesized companies are very small. It can be concluded that the smallsized companies with total assets less than 300 million have apparent weaker risk resistance.

Table 11 provides the correlation coef<sup>fi</sup>cient of DD and total assets in three years. In the <sup>fi</sup>rst half of 2004, the total assets and DD is weakly negative correlated. In the latter half of 2004, the correlation turns to be weak positive. It turns to be signi<sup>fi</sup>cantly positive from the beginning of 2005, which indicates the default distance is small in small-sized SMEs, and the probability of default is very large. As time goes, the effects of asset size on credit risk are more and more obvious.

## 4.5. Split share structure reform and credit risk

In this section, we use Fisher test to compare the variances of credit risk in listed SMEs before and after the split share structure reform. The split share structure reform starts in the middle of 2005 and has a great impact on the Chinese stock market. Under the reform, non-tradable shareholders negotiated a compensation plan with tradable shareholders in order to make their shares tradable.

There are 52 listed SMEs under reform or that have <sup>fi</sup>nished shares reform by 2007. Among them, there are only 3 ST companies carrying out the reform, and the majority of reformed companies are non-ST companies (see Table 12). The schedule of reform in listed SMEs is shown in Table 13. We can see that the reform accelerate from the end of 2005 to 2006 and reach the peak in the second quarter of 2006, but in the last quarter of 2006, the reforms suddenly reduced.

![](/api/attachments/GUXJCHPZ/fulltext/images/cecb2a586c7eb09b2f6bc929041a07ca3dd36fb1f9a25ab767dbebc0c32df445.jpg)  
Fig. 9. DD comparison in different sizes.

Table 11  
Correlation coef<sup>fi</sup>cient of DD and total assets.

<table><tr><td>Time</td><td>04/3</td><td>04/6</td><td>04/9</td><td>04/12</td><td>05/3</td><td>05/6</td><td>05/9</td><td>05/12</td><td>06/3</td><td>06/6</td><td>06/9</td><td>06/12</td></tr><tr><td>Pearson correlation coefficient</td><td>-0.030</td><td>-0.024</td><td>0.096</td><td>0.154</td><td>0.203</td><td>0.329*</td><td>0.303*</td><td>0.411*</td><td>0.396*</td><td>0.421*</td><td>0.377*</td><td>0.234</td></tr><tr><td>P value (two-tail)</td><td>0.820</td><td>0.848</td><td>0.405</td><td>0.181</td><td>0.080</td><td>0.003</td><td>0.007</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.001</td><td>0.349</td></tr><tr><td>Total assets (100 million)</td><td>4.796</td><td>4.715</td><td>5.017</td><td>4.656</td><td>4.719</td><td>4.758</td><td>4.851</td><td>4.607</td><td>4.689</td><td>4.802</td><td>4.949</td><td>5.899</td></tr></table>

Note: “\*” indicates that it is signi<sup>fi</sup>cant at the level of 1%.

However, whether the reform would affect the credit risk of listed SMEs is still unknown. In this paper, we collect two types of DD and σ before and after shares reform to compare the variances of credit risk. Fisher test can be used to judge whether the shares reform has impacts on credit risk. We divide the credit risk (DD value) into two classes with the boundary of the date starting shares reform: preshares reform refers to the period from the beginning of 2004 to the initial date of reform, and post-shares reform refers to the period from the initial date of reform to the beginning of 2007. The tests of equality of group means show that both DD means and σ means before and after reform are not signi<sup>fi</sup>cant in statistics at α-level of 5% (see Table 14), which means for both σ and DD, there is no signi<sup>fi</sup>cant differences before and after shares reform. The validity test of discriminant function shows that the discriminant effect is not signi<sup>fi</sup>cant (see Table 15), which means the credit risk before and after the reform cannot be discriminated effectively. We can conclude that there is no obvious difference in credit risk before and after shares reform, and the reform has few impacts on credit risk.

## 5. Conclusions and further consideration

In this paper, we propose a new method to improve the accuracy of σ in KMV model. The KMV model with tuned parameters is capable of identifying and predicting the credit risk of listed SMEs. Through multiple tests, the validity of the model is veri<sup>fi</sup>ed with the experimental results, which are very consistent with the reality. We <sup>fi</sup>nd that the predictive accuracy of adjusted KMV model is stable to the changes of default point in Chinese listed SMEs, which is different to the KMV Company's results where datum come from western countries. Along with the improvement of information disclosure and Chinese equity market, the default distance calculated by KMV model will be much closer to the true value, and the model will be much more effective to identify the credit risk of listed SMEs.

In general, the credit of Chinese listed SMEs is poor and stable from 2004 to 2006, with DD ranging from 50 to 60. The ST Company is much likely to default than the non-ST companies and blue chips. The credit of ST companies is poorest in the <sup>fi</sup>rst two years and tends to improve in 2006. The closer to the date being identi<sup>fi</sup>ed as ST, the higher the default risk is. Fortunately, Some ST companies have the possibility to get rid of de<sup>fi</sup>cits with the help of recapitalization, asset injection, recover arrears and <sup>fi</sup>nancial subsidies, and the ST label might be <sup>fi</sup>nally removed.

Table 12  
Split share structure reform progress sheet.

<table><tr><td>Reform progress</td><td>Under the way or have finished</td><td>No reform</td></tr><tr><td>Non-ST (59)</td><td>49</td><td>10</td></tr><tr><td>ST (20)</td><td>3</td><td>17</td></tr><tr><td>Total</td><td>52</td><td>27</td></tr></table>

Table 13  
Split share structure reform schedule in listed SMEs.

<table><tr><td>Reform schedule</td><td>3rd season in 2005</td><td>4th season in 2005</td><td>1st season in 2006</td><td>2nd season 2 in 2006</td><td>3rd season in 2006</td><td>4th season in 2006</td><td>Total</td></tr><tr><td>Under the way or have finished</td><td>2</td><td>12</td><td>6</td><td>19</td><td>12</td><td>1</td><td>52</td></tr></table>

We set two credit warning lines for Chinese listed SMEs. The DD=40 is set for the second grade warning, and the DD=30 is set for the <sup>fi</sup>rst grade warning. Results show that there are big credit risks in Chinese listed SMEs. Half of listed SMEs below the second grade warning will be in credit crisis in the next year and the credit condition must be attended closely. 90% of listed SMEs below the <sup>fi</sup>rst grade warning will be in credit crisis in the near future, the credit condition must be alerted and some remedy measures should be taken as soon as possible. The credit warning lines can assist the securities regulatory institutions in monitoring the credit crisis of listed SMEs and they just play the role of the EDF value, which is con<sup>fi</sup>dential inside KMV Company. In the future, we can also build a mapping relation between DD and EDF by gathering years of default datum.

We <sup>fi</sup>nd that the asset size has signi<sup>fi</sup>cant impact on credit risk. The probability of default is the biggest among small-sized listed SMEs and much lower in medium and large-sized ones. The default differences between medium and large-sized companies are tiny. The risk resistance in small business with total assets less than 300 million is the poorest. Assets size and default risk are weakly positively correlated in the <sup>fi</sup>rst half of 2004 and weakly negatively correlated in the latter half of 2004. When going into 2005, they show a signi<sup>fi</sup>cant negative correlation. As time goes, the impacts of asset size on credit risk will become more and more obvious.

The credit risk does not change very much before and after the split share structure reform, which brings few impacts on credit risk in the test period. However, the observation after reform is not long enough, the lagged effects of equity changes on credit risk may not be found in a short period of time.

Future works would be done in building the most optimum function of two volatilities (σ and σ ) for listed SMEs. More data should be collected to verify the results produced by our model.

Table 14  
Tests of equality of group means.

<table><tr><td></td><td>Wilks&#x27; lambda</td><td>F</td><td>df1</td><td>df2</td><td>Significant level</td></tr><tr><td>DD</td><td>0.979</td><td>2.194</td><td>1</td><td>102</td><td>0.142</td></tr><tr><td> $\sigma_E$ </td><td>0.975</td><td>2.587</td><td>1</td><td>102</td><td>0.111</td></tr></table>

Table 15  
Wilks' lambda.

<table><tr><td>Test of function(s)</td><td>Wilks&#x27; lambda</td><td>Chi-square</td><td>df</td><td>Significant level</td></tr><tr><td>1</td><td>0.974</td><td>2.695</td><td>2</td><td>0.260</td></tr></table>

[12] J.P. Egan, Signal Detection Theory and ROC Analysis, Academic Press, New York, 1975.

## Acknowledgements

This work was partially supported by the National Natural Science Foundation of China (Grants No. 70921001, No. 70631004). The authors are also grateful to the referees for their helpful comments and valuable suggestions for improving the earlier version of the paper.

## References

[1] E.I. Altman, R.G. Haldeman, P. Narayanan, Zeta analysis: a new model to identify bankruptcy risk of corporations, Journal of Banking and Finance 7 (1) (1977) 29–54.

[2] E.I. Altman, G. Marco, F. Varetto, Corporate distress diagnosis: comparisons using linear discriminant analysis and neural networks (The Italian Experience), Journal of Banking and Finance 18 (3) (1994) 505–529.

[3] E.I. Altman, A. Saunders, Credit risk measurement: developments over the last 20 years, Journal of Banking & Finance 21 (1998) 1721–1742.

[4] J.B. Caouette, E.I. Altman, P. Narayanan, Managing Credit Risk: the Next Great Financial Challenge, John Wiley & Sons, Inc, New York, 1998.

[5] X. Chen, W. Han, J. She, The credit risk, company quality and growth illusion, Economic Theory and Business Management 12 (2006) 62–67.

[6] P. Cheng, C. Wu, New method to analyze credit status of the listed companies, Systems Engineering Theory, Methodology and Applications 11 (2) (2002) 89–93.

[7] P.K. Coats, L.F. Fant, Recognizing <sup>fi</sup>nancial distress patterns using a neural network tool, Financial Management 22 (3) (1993) 142–155.

[8] Credit Metrics, Technical Document, J.P. Morgan & Co., New York, April 1997.

[9] Credit Suisse Financial Products, CreditRisk+: a Credit Risk Management Framework London, 1. 1997.

[10] P.J. Crosbie, J.R. Bohn, Modeling default risk, White Paper, Moody's KMV, Revised December, 2003.

[11] H.W. Du, W. Yang, Applying KMV model in China: issues in empirical studies, Studies of International Finance 11 (2004) 22–27.

[13] W.E. Henley, D.J. Hand, Construction of a k-nearest-neighbour credit-scoring system, IMA Journal of Management Mathematics 8 (4) (1997) 305–321.

[14] J. Hull, Options, Futures, and Other Derivative Securities, 3rd EditionPrentice Hall New Jersey, 1997.

[15] Z. Huang, H. Chen, C.J. Hsu, W.H. Chen, S. Wu, Credit rating analysis with support vector machines and neural networks: a market comparative study, Decision Support System 37 (2004) 543-558

[16] H.Y. Izan, Corporate distress in Australia, Journal of Banking and Finance 8 (2) (1984) 303–320.

[17] S. Kealhofer, J. Bohn, Portfolio management of default risk, White Paper, Moody's KMV. San Francisco, Revised May 31, 2001.

[18] C.L. Kun, H. Ingoo, K. Youngsig, Hybrid neural network models for bankruptcy predictions, Decision Support Systems 18 (1) (1996) 63–72

[19] M. Kurbat, I. Korablev, Methodology for testing the level of the EDF™ credit measure, White Paper, Moody's KMV, Revised August 08, 2002.

[20] D. Martin, Early warning of bank failure: a logit regression approach, Journal of Banking and Finance 1 (3) (1977) 249–276.

[21] R. Ma, Testing KMV on the <sup>fi</sup>nancial distress of listed companies in China, Application of Statistics and Management 25 (5) (2006) 593–601.

[22] J.A. McQuown, A Comment on Market vs. Accounting-Based Measures of Default Risk, KMV Corporation, LLC, San Francisco, September, 1993.

[23] R.C. Merton, On the pricing of corporate debt: the risk structure of interest rates, Journal of Finance 29 (1974) 449–470

[24] J.A. Ohlson, Financial ratios and the probabilistic prediction of bankruptcy, Journal of Accounting Research 18 (1) (1980) 109–130.

[25] A. Saunders, L. Allen, Credit Risk Measurement: New Approaches to Value at Risk and Other Paradigms, John Wiley & Sons, New York, March, 2002.

[26] J. Scott, The probability of bankruptcy: a comparison of empirical predictions and theoretical models, Journal of Banking and Finance 5 (3) (1981) 317–344.

[27] X. Shi, R. Ren, Empirical tests of consistency between market-based and accounting based credit models, Systems Engineering—Theory & Practice 10 (2005) 12–20.

[28] K.S. Shin, I. Han, A case-based approach using inductive indexing for corporate bond rating, Decision Support Systems 32 (2001) 41–52.

[29] L.D. Smith, E.C. Lawrence, Forecasting issues on a liquidating long-term loan portfolio, Journal of Banking and Finance 19 (6) (1995) 959–985.

[30] R.A. Sommerville, R.J. Taf<sup>fl</sup>er, Banker judgment versus formal forecasting models: the case of country risk assessment, Journal of Banking and Finance 19 (2) (1995) 281–297.

[31] C. Suisse, CreditRisk+: a Credit Risk Management Framework, Credit Suisse Financial Products London, 1, 1997.

[32] Q. Wang, J. Chen, The study of credit risk model and pricing method, Modern Finance and Economics: Journal of Tianjin University of Finance and Economics 22 (4) (2002) 14–16.

[33] R.C. West, A factor-analytic approach to bank condition, Journal of Banking and Finance 9 (2) (1985) 253–266

[34] D. West, Neural network credit scoring models, Computer & Operations Research 27 (11–12) (2000) 1131–1152.

[35] R.L. Wilson, S.R. Sharda, Bankruptcy prediction using neural networks, Decision Support Systems 11 (5) (1994) 545–557.

[36] D. Wu, D.L. Olson, Enterprise risk management: small business scorecard analysis Production Planning & Control 120 (4) (2009) 362–369.

[37] D. Wu, D.L. Olson, Enterprise risk management: coping with model risk in a large bank, Journal of Operational Research Society 61 (2) (2010) 179–190.

[38] X. Yang, Y. Zhang, An empirical study on credit risk management of China's listed companies, China Soft Science 1 (2004) 43–47.

[39] Q. Ye, N. Jing, L. Xu, Research on credit risk measurement based on the Capital Market Theory, Economist 2 (2005) 112–117.

[40] L. Zhang, Z. Yang, S. Chen, An application of KMV model in credit risk evaluation of public companies, System Engineering 22 (11) (2004) 84–89.

[41] S. Zhang, A comparison of the market value of listed companies under the examining and approving system, Financial Theory and Practice (7) (2006).

[42] M. Zheng, Empirical research of credit risk for the public company using EDF model, Journal of Industrial Engineering and Engineering Management 19 (3) (2005) 151–154.

[43] Chinese Stock Supervisory Committee, Code of Good Practice of Exercise of State-Owned Corporation Shares, 1997, p. 62.

Xiaohong Chen is the dean and professor at Business School, Central South University of China, Changsha, Hunan Province, China. She has published more than 100 papers in national and international journals.

Xiaoding Wang is a PhD at Business School, Central South University of China, Changsha, Hunan Province, China. Her research mainly focuses on credit risk management and data mining. She has published more than 10 papers in national and international journals.

Desheng Dash Wu is the af<sup>fi</sup>liate professor at RiskLab of University of Toronto and director of RiskChina Research Center at University of Toronto. His research interests focus on enterprise risk management, performance evaluation, and decision support system. He has published more than 60 journal papers appeared in such journals as Risk Analysis, Decision Support Systems, International Journal of Production Research. European Journal of Operational Research, Expert Systems with Applications, International Journal of Production Economics, Annals of Operations Research, Journal of Operational Research Society, IEEE Transactions on Knowledge and Data Engineering, Computers and Operations Research, International Journal of System Science, et al. He has coauthored 3 books with David L Olson. He has served as editor/guest editor/chair for several journals/ conferences. The special issues he edited include those for Human and Ecological Risk Assessment (2009, 2010), Production Planning and Control (2009), Computers and Operations Research (2010), International Journal of Environment and Pollution (2009) and Annals of Operations Research (2010). He is a member of PRMIA (the Professional Risk Managers' International Association) Academic Advisory Committee and global ethics committee member.
