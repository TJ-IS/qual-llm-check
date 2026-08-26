---
otero_id: 26654
otero_key: "J43EHASP"
title: "Research Report—Principles for Examining Predictive Validity: The Case of Information Systems Spending Forecasts"
authors: "Fred Collopy; Monica Adya; J. Scott Armstrong"
year: "1994"
journal: "Information Systems Research"
doi: "10.1287/isre.5.2.170"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## H4R

![](/api/attachments/J43EHASP/fulltext/images/cdda910135b6b1f838523d2bff774c9aa95a7ecc7c4fb9a33e7153aae58e8d36.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Research Report—Principles for Examining Predictive Validity: The Case of Information Systems Spending Forecasts

Fred Collopy, Monica Adya, J. Scott Armstrong,

To cite this article:

Fred Collopy, Monica Adya, J. Scott Armstrong, (1994) Research Report—Principles for Examining Predictive Validity: The Case of Information Systems Spending Forecasts. Information Systems Research 5(2):170-179. http://dx.doi.org/10.1287/ isre.5.2.170

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 1994 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/J43EHASP/fulltext/images/706352d915a4bf8d54ecd1092a0b829fad6a7afa2c632b0e00390772914e08db.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

RESEARCH REPORT

# Principles for Examining Predictive Validity: The Case of Information Systems Spending Forecasts

Fred Collopy

The Weatherhead School

Case Western Reserve University

Monica Adya

J. Scott Armstrong

Cleveland, Ohuo 44106

The Weatherhead School

Case Western Reserve University

Cleveland, Ohio 44106

The Wharton School

Universıty of Pennsylvania

Philadelphia, PA 19104

Research over two decades has advanced the knowledge of how to assess predictive validity. We believe this has value to information systems (IS) researchers. To demonstrate, we used a widely cited study of IS spending. In that study, price-adjusted diffusion models were proposed to explain and to forecast aggregate U.S. information systems spending. That study concluded that such models would produce more accurate forecasts than would simple linear trend extrapolation. However, one can argue that the validation procedure provided an advantage to the diffusion models. We reexamined the results using an alternative validation procedure based on three principles extracted from forecasting research: (1) use ex ante (out-of-sample) performance rather than the fit to the historical data, (2) use well-accepted models as a basis for comparison, and (3) use an adequate sample of forecasts. Validation using this alternative procedure did confirm the importance of the priceadjustment, but simple trend extrapolations were found to be more accurate than the price-adjusted diffusion models.

Brown's linear exponential smoothing—C'ombined forecasts—Damped trend exponential smoothing—Diffusion—Extrapolation-Forecast accuracy-Information systems spending—Price-adjusted diffusion models—Validation

## Introduction

【n the past two decades, much has been learned about testing the predictive validity of models. We believe that utilization of the findings from the forecasting literature will lead to improved assessments of predictive validity in information systems (IS) research. To demonstrate this, we reanalyzed the models proposed in an oft-cited study about information systems spending by Gurbaxani and Mendelson (1990), which we refer to as “G&M". The G&M paper presents models that, in our opinion, pass tests of face validity. In this paper we examine the models' predictive validity.

![](/api/attachments/J43EHASP/fulltext/images/f02f9e20284a811fa315eb8bd389f5fa1337089ea9cc907002fc6276454f64e4.jpg)  
FiGURE 1. Information Systems Spending in the U.S

In their paper, G&M modified some traditional diffusion models to analyze aggregate spending on information systems in the United States. Their primary objective was to establish the importance of price as a determinant of IS spending. G&M is an important study because it provides empirical comparisons of alternative approaches. In our opinion, such studies represent the best in management science. Also, G&M is the most comprehensive attempt yet to quantify and to explain the growth of aggregate U.S. spending on IS. Its analysis of the role of price provides insights about changes in the historical rates of IS spending growth. Finally, given the role of IS n the economy, a model that improves our understanding of IS expenditures would seem to be of substantial importance.

In addition to using their price-adjusted diffusion models to provide causal explanations, G&M proposed that the models be used to forecast aggregate spending on information systems. They stated that their model “. . . has implications for forecasting the magnitude of IS expenditures into the future (p. 42)." In comparisons of their model with other prediction techniques, they concluded that their model provided more accurate forecasts. This study examines G&M's conclusions about the utility of their model for forecasting IS expenditures by providing an alternative analysis, using data provided by G&M and techniques drawn from the field of forecasting

## G&M's Data, Models, and Validation Procedure

G&M tested their models using a time series based on the responses of user organizations to surveys conducted by International Data Corporation (IDC). The respondents' estimated their IS expenditures, which included spending on mainframes, minicomputers, microcomputers, data entry equipment, data communications equipment, line charges, software, services, supplies, and overhead. This also included replacement, supplies, labor, and other recurring costs. The costs of users time (outside of IS organizations) were not included. The IDC database contains information on more than 80% of the general purpose computers installed in the U.S.

These data represent consumption, not adoption. Figure 1 shows this series in current dollars and in 1972 constant dollars, and Appendix A presents the data.

G&M proposed an adaptation to diffusion models. Diffusion (or S-shaped) models posit a changing rate of growth that can depend on two opposing factors. First, as potential customers are brought into contact with the product, the extent to which the product has already been accepted exerts a positive influence on growth. Second, increases in the level of use can exert a negative influence on the growth rate because the number of potential customers decreases.

Can diffusion models be expected to perform well in forecasting the G&M data? Potential threats include a lack of empirical support for diffusion models, difficulty in estimating saturation levels, and the risks associated with their complex functional forms. There is little empirical evidence on the conditions under which diffusion models are most appropriate for forecasting. Meade's (1984) review of the empirical evidence for diffusion curves contains six studies that involve forecasting, but these studies were based on small samples and none of them provided benchmarks for comparing the performance of the diffusion models. Rao (1985) examined the forecast validity of several diffusion methods and found them to be less accurate than simpler extrapolation methods. However, the empirical evidence on this matter remains sparse.

The functional form of diffusion models is complex (Mahajan and Muller 1979, Meade 1984). Initially, the series grows slowly, then increases its growth rate at some point, and, finally, it decreases the growth rate as it approaches a saturation level Standard diffusion models assume a constant total population of potential customers. But for many technologies there is a third segment of the diffusion process: the entry of individuals into the pool of potential customers (see Meade 1984, Mahajan et al. 1990). The population of potential customers can be expanded through a reduction in price, and G&M proposed an extension to incorporate price, arguing that “a considerable share of IS spending growth is due to price effects (p. 28)." They refer to their extended versions of the three basic diffusion models as price-adjusted diffusion models.

Diffusion models also require estimates of the saturation level. This is either provided as an input to the model or is estimated from the historical data, as part of the fitting process. An historical series often contains little evidence as to the eventual saturation level, so Martino (1983) recommends against estimating the saturation level in this way. In G&M, saturation levels are estimated from the historical data. Furthermore, because IS spending measures consumption rather than adoption, it is particularly difficult to establish a saturation level.

As we described above, diffusion models introduce complexity by their shape. Models with complex functional forms seldom improve forecast accuracy (Armstrong 1985, pp. 200–202, reviews the evidence on this issue). This apparently occurs because complex models increase the risk of extending false patterns.

G&M provide empirical support to show that their price-adjusted diffusion models yield accurate forecasts. However, one can argue that their test provided an advantage to the price-adjusted diffusion model. For each of the price-adjusted diffusion models, they used all of the data from 1960 to 1987 to produce a fitted model. They then compared the last value of the fitted model with the actual observed value for 1987 (one of the values that was used in fitting the model). The difference between the fitted value and the observed value represented the forecasting error for the priceadjusted diffusion model. For each of the alternative models (which they refer to as linear and exponential extrapolation), they obtained their parameter estimates using only two observations—the actual values for 1970 and 1980. Then they extrapolated to produce a forecast for 1987. The difference between the extrapolated value and the actual 1987 observation was used to assess the accuracy of the alternative model. The two sets of forecast errors were then compared. G&M concluded that the price-adjusted Gompertz curve provided the best forecast.

## An Alternative Validation Procedure

We reexamined the results in G&M, using the same series they analyzed. We also examined the same diffusion models, including their price-adjusted diffusion models. We based the formulations on those presented in G&M. To ensure that we were using them as G&M did, we first replicated the results given in that paper. The details of the diffusion models and our application of them to produce forecasts are provided in Appendix B. Application of the models was a complex process. We think that practitioners would, in general, experience difficulty in using price-adjusted diffusion models correctly. Following the recommendation in Armstrong and Collopy (1992), we used the Median Absolute Percentage Error (MdAPE) to assess accuracy.

Empirical research has established principles that are useful in ensuring the predictive validity of time series models. To assess the forecasting validity of a proposed model: (1) use ex ante (out-of-sample) performance rather than the fit to the historical data, (2) use well-accepted models as a basis for comparison, and (3) use an adequate sample of forecasts. In this section, we describe how each of these principles effected the design of our validation procedure.

## Use of ex ante Performance for Comparisons

The G&M models produced good fits to the historical time series, with R²s between 0.95 and 0.999. However, forecasting researchers have learned that the fit of a model to historical data is not a reliable indicator of the ability of that model to forecast future values of the series (for a summary, see Armstrong 1985, pp. 338–339). It is common in the forecasting field to validate models using ex ante (out-of-sample) forecasts, but in G&M, the diffusion models' “forecasts" are from within sample (they used the actual value for 1987 when fitting the model). The alternative extrapolation forecasts were seven-year-ahead ex ante forecasts (they did not use the 1987 value when fitting the model). A comparison of models should be based on having the same dlata available for fitting each model.

In this study we relied upon comparisons of ex ante forecasts from all of the methods. 'That is, models were fit using some of the historical data, forecasts were produced, and then the models’ forecasts were compared on hold-out data (data which are not used at all in fitting the models).

## Use of Well-accepted Models as a Reference

G&M recognized the need for comparisons with alternative models when they proposed comparing their price-adjusted diffusion models with linear and exponential trend models. The alternative models they chose, though, were estimated using only two observations, while their price-adjusted diffusion models were estimated using 28 observations.

The forecasting literature expresses a preference for simpler models unless a strong case has been made for complexity. The research findings indicate that relatively simple extrapolation models are robust (Armstrong 1984). We compared the diffusion models examined by G&M with simple extrapolation methods, including linear regression against time, Brown's linear exponential smoothing, damped trend exponential smoothing, and an average of the three (referred to as equal weights). These methods are relatively simple, widely used, well-documented in the literature, and have performed well in previous comparative studies. We chose them a priori. Below, we briefly describe why each of these models was chosen.

As a functional form for the simple linear regression against time, we chose an additive form. The additive form represents a more conservative choice when there is uncertainty about the proper form. In the case of IS spending, uncertainty arises because of changes in the basic (long-term) trend, and because the net effect of the underlying causal forces is not clear: price has a downward force on dollar sales while quality has an upward force.

The linear regression places equal weight upon all available historical data. For an alternative model that weights recent data more heavily, we selected exponential smoothing (Brown 1959). This approach is useful when the series is changing rapidly, as seems to be the case with IS spending.

We also used damped trend smoothing which offers another opportunity to improve the accuracy of extrapolations by reducing the magnitude of the trend component based on the variation in the historical series. This introduces some complexity but the value of this procedure has been supported empirically (Gardner and McKenzie 1985).'

Finally, we combined the three forecasts from simple methods by weighing them equally. Many studies have been conducted to identify the most effective combining strategies (Clemen 1989). A simple average has proven to be robust, in the sense that it is typically more accurate than the average error of the individual forecasts, and it is usually as accurate as other sets of a priori weights.

## Use of an Adequate Sample of Forecasts

G&M based their conclusion about the forecast utility of the price-adjusted diffusion models on a single forecast. The use of successive updating provides a larger sample size for comparing the performance of the alternative methods. We first estimated the parameters of each model using the data from 1960 through 1974, then produced forecasts for ten years (1975–1984) and calculated forecast errors. The next observation, 1975, was then added to the historical data, the model parameters were re-estimated, forecasts were made, and errors were calculated. The procedure was repeated until the estimation data included all but the last observation. This produced 13 one-year-ahead forecasts, 12 two-year-ahead forecasts, and so forth, up to 4 ten-year-ahead forecasts. In all, there were 85 forecasts and 13 starting points for each method.

## Results

The random walk (which simply extends the latest observation and assumes no change) was used as a benchmark for comparisons. The average MdAPE across all ten horizons for the three basic diffusion models was 21.3. This is about 20% less than the error from benchmark random walk forecasts. The logistic, which Martino's (1983) guidelines suggest would be the most appropriate of the diffusion models, did not perforrn well. Its average MdAPE was 31.9, which was 18% larger than that from the random walk

TABLE 1  
Median Absolute Percentage Errors of Alternative Extrapolatton Strategies

<table><tr><td rowspan="2"></td><td colspan="10">Forecast Horizon</td><td rowspan="2">Average1 to 10(85)</td></tr><tr><td>1(13)</td><td>2(12)</td><td>3(11)</td><td>4(10)</td><td>5(9)</td><td>6(8)</td><td>7(7)</td><td>8(6)</td><td>9(5)</td><td>10(4)</td></tr><tr><td>Random Walk</td><td>5.6</td><td>11.2</td><td>16.4</td><td>21.8</td><td>25.4</td><td>30.2</td><td>34.0</td><td>37.5</td><td>42.4</td><td>45.6</td><td>27.0</td></tr><tr><td>Logistic</td><td>19.4</td><td>21.6</td><td>23.7</td><td>28.0</td><td>32.1</td><td>34.6</td><td>37.1</td><td>39.3</td><td>41.3</td><td>41.6</td><td>31.9</td></tr><tr><td>Gompertz</td><td>8.4</td><td>9.0</td><td>12.1</td><td>12.0</td><td>13.5</td><td>14.7</td><td>16.7</td><td>16.9</td><td>17.0</td><td>16.0</td><td>13.6</td></tr><tr><td>Modified Exponential</td><td>7.9</td><td>9.7</td><td>12.0</td><td>14.6</td><td>18.2</td><td>20.2</td><td>22.4</td><td>24.5</td><td>26.1</td><td>26.9</td><td>18.3</td></tr><tr><td>Avg Diffusion</td><td>11.9</td><td>13.4</td><td>15.9</td><td>18.2</td><td>21.3</td><td>23.2</td><td>25.4</td><td>26.9</td><td>28.2</td><td>28.1</td><td>21.3</td></tr><tr><td>Price-Adjusted Logistic</td><td>5.3</td><td>5.3</td><td>5.2</td><td>5.4</td><td>5.3</td><td>5.1</td><td>5.5</td><td>6.7</td><td>7.9</td><td>7.9</td><td>6.0</td></tr><tr><td>Price-Adjusted Gompertz</td><td>6.1</td><td>6.5</td><td>8.5</td><td>12.0</td><td>13.6</td><td>14.8</td><td>16.7</td><td>16.9</td><td>17.0</td><td>16.0</td><td>12.8</td></tr><tr><td>Price-Adjusted Mod Exp</td><td>3.2</td><td>4.9</td><td>4.8</td><td>6.2</td><td>8.2</td><td>10.6</td><td>11.8</td><td>13.7</td><td>17.4</td><td>18.6</td><td>9.9</td></tr><tr><td>Avg Price-Adjusted</td><td>4.9</td><td>5.6</td><td>6.2</td><td>7.9</td><td>9.1</td><td>10.2</td><td>11.3</td><td>12.4</td><td>14.1</td><td>14.2</td><td>9.6</td></tr><tr><td>Regression</td><td>2.9</td><td>2.9</td><td>3.2</td><td>3.9</td><td>4.5</td><td>5.3</td><td>4.7</td><td>5.5</td><td>6.4</td><td>5.3</td><td>4.5</td></tr><tr><td>Brown&#x27;s Lin Exp Smooth</td><td>1.8</td><td>4.3</td><td>6.5</td><td>7.6</td><td>5.1</td><td>7.7</td><td>6.0</td><td>11.9</td><td>2.3</td><td>18.1</td><td>7.1</td></tr><tr><td>Damped Trerd Exp Smooth</td><td>2.0</td><td>4.1</td><td>7.0</td><td>7.9</td><td>5.3</td><td>10.3</td><td>9.5</td><td>15.6</td><td>7.0</td><td>19.3</td><td>8.8</td></tr><tr><td>Avg Simple Extrap</td><td>2.2</td><td>3.7</td><td>5.6</td><td>6.5</td><td>5.0</td><td>7.8</td><td>6.8</td><td>11.0</td><td>5.2</td><td>14.3</td><td>6.8</td></tr><tr><td>Equal Weights</td><td>1.4</td><td>2.9</td><td>5.9</td><td>6.3</td><td>4.3</td><td>8.5</td><td>7.5</td><td>11.0</td><td>4.4</td><td>13.6</td><td>6.6</td></tr></table>

Number of forecasts in parentheses.

The price adjustment improved the accuracy of each of the three diffusion models. Overall, the MdAPE was reduced from 21.3 to 9.6. The price adjustment was particularly effective when applied to the logistic, resulting in a MdAPE of 6.0. For 194 of the 255 comparisons, the price-adjusted forecast had a lower error than the standard model. A paired sign test was significant at p < 0.0001. (There is likely some correlation among the errors, so this result overstates the significance). This supports G&M's position that a price parameter is an important addition to standard diffusion models, not only for explanatory purposes, but also for prediction.

G&M concluded that their price-adjusted diffusion models produced better forecasts than did a simple linear trend extrapolation. However, when subjected to the above-described validation procedure, they did not. The linear regression against time had an overall MdAPE of 4.5, lower than that for any of the price-adjusted diffusion models

Table 1 presents the MdAPEs for each method for each of the ten years of the forecast horizon. It also provides the unweighted averages across the ten years.

Brown's exponential smoothing and damped-trend exponential smoothing were relatively accurate. Their MdAPEs, averaged across the ten horizons, were 7.1 and 8.8, respectively. The simple trend extrapolation methods, with their average MdAPE of 6.8, were more accurate than the price-adjusted diffusion models, with their average MdAPE of 9.6.

An equally-weighted combination of the three simple trend extrapolations was slightly more accurate than the average of the components (MdAPE of 6.6 versus 6.8). Across all horizons, the errors from combining forecasts were about 3% less than the errors of the average component. The equally-weighted combination tended to be more useful for the short-range forecasts; for forecast horizons of up through five years, it reduced the error by about 10%, whereas for horizons of six through ten years, there was no error reduction.

The accuracy of the typical price-adjusted diffusion was not superior to that of the equally-weighted combined forecast models. On average, its error was about 45% larger.

The price adjusted logistic was the most accurate of the diffusion models, but there was no a priori basis for selecting this model in preference to the other price-adjusted models. Its error was slightly less than that for the equally-weighted combination of the simple methods.

## Conclusions

We believe that G&M's models shed light on why simple S-shaped curves provide inadequate fits to the historical IS spending data and provide insight into the effects of price. G&M's price-adjusted models proved superior to traditional diffusion models, supporting their claim for the importance of price as a determinant of IS spending growth. However, their claim that such models would prove more accurate than simple and widely-used extrapolation methods was not supported.

It appears to be a commonly held view that spending on information systems is growing in an explosive fashion. The same view has been held at other times. If experience is any indication, one of the implications of the analysis presented here is that we are more likely to be close to true future values of spending on information systems if we assume that they will continue to grow in a simple linear fashion.

We propose that IS researchers who wish to validate their models for making forecasts should rely upon ex ante comparisons, make comparisons with well-established, reasonable alternatives, and use adequate samples. Given the evidence, we recommend that IS researchers and practitioners not use diffusion models for forecasting IS spending.\*

Acknowledgements. Gadi Ariav, Katherine Auer, Dick Boland, Chris Chatfield, Joshua Eliashberg, Katrine Kirk, Henry Lucas, Joseph Martino, Nigel Meade, Betty Vandenbosch, the editors, and several anonymous reviewers provided useful comments on earlier drafts of this article. Suzanne Berman and Vanessa Lacoss provided editorial assistance.

Appendix A: Information Systems Spending in the U.S. (\$ Billions)

<table><tr><td>Year</td><td>Nominal</td><td>Constant 1972</td></tr><tr><td>1960</td><td>1.25</td><td>1.77</td></tr><tr><td>1961</td><td>1.81</td><td>2.53</td></tr><tr><td>1962</td><td>2.47</td><td>3.41</td></tr><tr><td>1963</td><td>3.35</td><td>4.57</td></tr><tr><td>1964</td><td>4.58</td><td>6.16</td></tr><tr><td>1965</td><td>6.11</td><td>8.11</td></tr><tr><td>1966</td><td>7.96</td><td>10.27</td></tr><tr><td>1967</td><td>10.81</td><td>13.51</td></tr><tr><td>1968</td><td>13.88</td><td>16.64</td></tr><tr><td>1969</td><td>17.54</td><td>19.99</td></tr><tr><td>1970</td><td>20.95</td><td>22.57</td></tr><tr><td>1971</td><td>23.54</td><td>24.23</td></tr><tr><td>1972</td><td>26.28</td><td>26.28</td></tr><tr><td>1973</td><td>30.15</td><td>28.38</td></tr><tr><td>1974</td><td>34.41</td><td>29.10</td></tr><tr><td>1975</td><td>38.68</td><td>30.01</td></tr><tr><td>1976</td><td>44.38</td><td>32.64</td></tr><tr><td>1977</td><td>51.38</td><td>35.32</td></tr><tr><td>1978</td><td>58.72</td><td>37.56</td></tr><tr><td>1979</td><td>67.56</td><td>38.75</td></tr><tr><td>1980</td><td>80.54</td><td>40.86</td></tr><tr><td>1981</td><td>95.22</td><td>43.76</td></tr><tr><td>1982</td><td>106.87</td><td>46.36</td></tr><tr><td>1983</td><td>120.42</td><td>50.47</td></tr><tr><td>1984</td><td>136.31</td><td>54.62</td></tr><tr><td>1985</td><td>145.45</td><td>56.68</td></tr><tr><td>1986</td><td>153.42</td><td>58.66</td></tr><tr><td>1987</td><td>160.76</td><td>59.10</td></tr></table>

## Appendix B: Description of Application of the Diffusion Models

We replicated and validated the six diffusion models considered by G&M. These were:

Gompertz

$$
B _ {t} = K A ^ {b t}.
$$

Logistic

$$
B _ {t} = 1 / (K + 4 b ^ {\prime}).
$$

Modified-Exponential

$$
B _ {t} = e ^ {a (h / t)},
$$

Price-Adjusted Gompertz

$$
B _ {t} = K A ^ {b} e ^ {\lambda t}.
$$

Price-Adjusted Logistic

$$
B _ {t} = (1 / (K + A b ^ {t})) e ^ {\lambda t},
$$

Price-Adjusted Modıfied-Exponential

$$
B _ {t} = e ^ {a \cdot (b / t) + \lambda t}.
$$

where

! = year,

B, = real level of total IS spendıng in year t,

K, A, a, and h = parameters to be estimated

e = price adjustment to the basıc diffusion models.

The price-adjusted models were the basıc diffusion models multiplied by a function to account for the price adjustment. Because the price-adjusted models would have been difficult to estimate in their existing form, G&M 1ransformed them to the estimation equations:

$$
\begin{array}{l l} \text { Price - Adjusted Gompertz } & \log (B _ {t}) = \log K + \lambda t + b ^ {\prime} \log A, \\ \text { Price - Adjusted Logistic } & 1 / B _ {t} = (K + A b ^ {\prime}) e ^ {- \lambda t}, \\ \text { Price - Adj   Mod - Exponential } & \log (B _ {t}) = a - (b / t) + \lambda t. \end{array}
$$

All six models were estimated using the nonlinear regression procedure of SYSTAT 5.0. Specifically, we used the Sımplex approach to estimate for all but the price-adjusted logistic model. In performing these analyses, our effort was to keep the estimation process as consistent as possible across all six methods Another concern was to introduce as little external information as possible to the process. Details of estimating the six models follow

## Modified-Exponential Mode

Both the original and a log-transformed version of this model were estimated. However, the transformed model did not vield reasonable parameter estimates or forecasts. Hence, we used the original model in the analysis.

## Gompertz Model

The original version of the Gompertz model did not converge to an optımal solution. The log-transformed version of the model converged and produced reasonable parameters and forecasts.

## Logistic Model

There were no convergence problems with either the original or log-transformed versions of the logistic model. However, the forecasts generated using the original model did not appear reasonable. Results from using the transformed model were much more reasonable. Consequently, our analysis was based on this version.

## Price-Adjusted Modıfied-Exponental Model

G&M estimated parameter values using the log-transformed version of the price-adjusted modified-exponential model. When we used this version, we were able to replicate their results. However, some of the forecasts generated using this model looked unreasonable. We were able to produce much more reasonable forecasts using the original version of the model.

## Price-Adjusted Gompertz Model

The original formulation of the price-adjusted Gompertz model did not converge even when given initial starting values. We were able to use the log-transformed version of the model to produce reasonable forecasts when we added the constraint that λ be nonnegative.

## Price-Adjusted Logistıc Modet

The original version of the price-adjusted logistic model failed to converge. We were unable to replicate G&M without provıding their results as initial values. Even then some of the forecasts did not look reasonable We changed the estimation technique to use the Quasi-Newton technique. This permitted us to replication of G&M's results and vielded forecasts that look reasonable.

## References

Armstrong, J. S., “Forecasting by Extrapolation: Conclusions from 25 Years of Research," Interfaces, 14 (Nov.-Dec. 1984), 52-66.

-, Long-Range Forecasting, John Wiley, New York, 1985.

- and F. Collopy, “Error Measures for Generalizing about Forecasting Methods: Empirical Comparisons," International Journal of Forecasting, 8 (1992), 69–80.

Brown, R. G., Statistical Forecastıng for Inventory Control, McGraw-Hill, New York, 1959.

Clemen, R T., "Combining Forecasts: A Review and Annotated Bibliography," International Journal o Forecastng. 5 (1989), 559–583

Gardner, E. S., Jr. and E. McKenzie, “Forecasting Trends in Time Series," Management Science, 31 (1985), 1237–1246

Gurbaxani, V. and H. Mendelson, “An Integrative Model of Information Systems Spending Growth," Information Systems Research, 1 (1990). 23–46

Mahajan, V and E. Muller, "Innovation Diffusion and New-Product Growth Models in Marketing," Journal of Marketıng, 43 (1979), 55–68

-, and F. Bass, “New Product Diffusion Models in Marketing: A Revıew and Directions for Research," Journal of Marketing, 54 (1990), 1–26

Meade, N., "he Use ofGrowth Curves in Forecasting Market Development—A Review and Appraisal," Journal of Forecasting, 3 (1984), 429–451.

Martino, J., Technologıcal Forecasting for Decision Makıng. North Holland, New York, 1983.

Rao, S., “An Empirical Comparison of Sales Forecasting Models," Jour nal of Product Innovatton Management, 4 (1985), 232–242
