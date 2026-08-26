---
otero_id: 20827
otero_key: "UG6RY6U2"
title: "Automatic ARMA identification using neural networks and the extended sample autocorrelation function: a reevaluation"
authors: "Tim Chenoweth; Robert Hubata; Robert D St. Louis"
year: "2000"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(00)00058-0"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Automatic ARMA identification using neural networks and the extended sample autocorrelation function: a reevaluation

Tim Chenoweth, Robert Hubata, Robert D. St. Louis )

School of Accountancy and Information Management, College of Business, Arizona State UniÕersity, Tempe, AZ 85287-3606, USA

Accepted 24 January 2000

## Abstract

Recently, several researchers have attempted to use neural network approaches in conjunction with the extended sample autocorrelation function ESACF to automatically identify ARMA models. The work to date appears promising, butŽ . generalizations are limited by the fact that the test and training sets for the neural networks were generated from random perturbations of prototype ESACF tables. This paper develops test and training sets by varying the parameters of actual ARMA processes. The results show that the ability of neural networks to accurately identify the order of an ARMAŽ . p,q model from its transformed ESACF is much lower than reported by previous researchers, and is especially low for time series with fewer than 100 observations. q 2000 Elsevier Science B.V. All rights reserved.

Keywords: ARMA model identification; Extended sample autocorrelation function; Iterated autocorrelation coefficient; Neural network; Noise

## 1. Introduction

The Box–Jenkins ARMA modeling approach toŽ . forecasting has been popular with statisticians and other technical specialists for years 1 . Nontechnical <sup>w</sup> <sup>x</sup> managers, on the other hand, have avoided using the approach. One reason for this avoidance is the fact that model identification requires an understanding of the concepts of stationarity, autocorrelation, partial autocorrelation, unit roots, and invertibility, and yet still is not exact. That is, even if the practitioner completely understands the theoretical underpinnings of the approach, identification of an appropriate model still requires a subjective interpretation of the plots of the sample autocorrelation function and the sample partial autocorrelation function 9 . More- <sup>w</sup> <sup>x</sup> over, it is not at all unusual for two experts to identify two very different models for the same data set.

Tsay and Tiao 12 developed the extended sam- <sup>w</sup> <sup>x</sup> ple autocorrelation function ESACF to simplify the Ž . ARMA model identification process. Table 1 represents the ESACF. MA is the order of the moving average process, AR is the order of the autoregressive process, and $r _ { j ( k ) }$ is the value of the autocorrelation coefficient for the jth iterated, kth order autoregressive process at lag j. For an ARMAŽ $p , q )$ model,

Table 1  
General ESACF table for an ARMAŽ . p,q process

<table><tr><td rowspan="2">AR</td><td colspan="5">MA</td></tr><tr><td>0</td><td>1</td><td>2</td><td>3</td><td>...</td></tr><tr><td>0</td><td> $r_{1(0)}$ </td><td> $r_{2(0)}$ </td><td> $r_{3(0)}$ </td><td> $r_{4(0)}$ </td><td>...</td></tr><tr><td>1</td><td> $r_{1(1)}$ </td><td> $r_{2(1)}$ </td><td> $r_{3(1)}$ </td><td> $r_{4(1)}$ </td><td>...</td></tr><tr><td>2</td><td> $r_{1(2)}$ </td><td> $r_{2(2)}$ </td><td> $r_{3(2)}$ </td><td> $r_{4(2)}$ </td><td>...</td></tr><tr><td>3</td><td> $r_{1(3)}$ </td><td> $r_{2(3)}$ </td><td> $r_{3(3)}$ </td><td> $r_{4(3)}$ </td><td>...</td></tr><tr><td> $\vdots$ </td><td> $\vdots$ </td><td> $\vdots$ </td><td> $\vdots$ </td><td> $\vdots$ </td><td>...</td></tr></table>

Tsay and Tiao show that the population value of $r _ { j ( k ) }$ is:

Zero

$$
\begin{array}{l} \text { if } 0 \leq (j - q) > (k - p) \geq \\ 0, \end{array}
$$

A nonzero constant

$$
\text { if } 0 \leq (j - q) \leq (k - p) \geq
$$

$$
\begin{array}{l} 0 \text { or } 0 \leq (j - q) > (k - p) \\ <   0 \end{array}
$$

A continuous

$$
\mathrm{if} 0 > (j - q)
$$

random variable

bounded between

<sup>y</sup>1 and<sup>q</sup>1

Thus the asymptotic ESACF for an ARMA 1,1Ž . process would appear as in Table 2, where X denotes a nonzero value and 0 denotes a zero value.

The order of the ARMA process can be visually determined by noting the row and column numbers of the cell that contains the vertex of the triangle formed by the zeroes. The row number is the order of the autoregressive process, and the column number is the order of the moving average process.

For finite sample sizes, random noise generally causes the sample value of $r _ { j ( k ) } \mathrm { t o }$ be nonzero even when the population value is zero. To help sort out noise, and to make it easier to visually identify the order of an $\mathbf { A R M A } ( \mathbf { \phi } _ { p , q } )$ model, Tsay and Tiao suggest transforming each $r _ { j ( k ) }$ value in the ESACF table to zero or one by testing it for statistical significance. Using this approach, the prototype transformed ESACF for an ARMA 1,1 process be- Ž . comes as shown in Table 3, where 1 indicates a sample value for $r _ { j ( k ) }$ that is different from 0 at the 5% level of significance, and 0 indicates a sample value for $r _ { j ( k ) }$ that is not different from 0 at the 5% level of significance.

Table 2  
Prototype ESACF table for an ARMA 1,1 process Ž .

<table><tr><td rowspan="2">AR</td><td colspan="6">MA</td></tr><tr><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>...</td></tr><tr><td>0</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>...</td></tr><tr><td>1</td><td>X</td><td>0</td><td>0</td><td>0</td><td>0</td><td>...</td></tr><tr><td>2</td><td>X</td><td>X</td><td>0</td><td>0</td><td>0</td><td>...</td></tr><tr><td>3</td><td>X</td><td>X</td><td>X</td><td>0</td><td>0</td><td>...</td></tr><tr><td>4</td><td>X</td><td>X</td><td>X</td><td>X</td><td>0</td><td>...</td></tr><tr><td> $\vdots$ </td><td> $\vdots$ </td><td> $\vdots$ </td><td> $\vdots$ </td><td> $\vdots$ </td><td> $\vdots$ </td><td>...</td></tr></table>

Table 3  
Prototype transformed ESACF table for an ARMA 1,1 process Ž .

<table><tr><td rowspan="2">AR</td><td colspan="6">MA</td></tr><tr><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>...</td></tr><tr><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>...</td></tr><tr><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>...</td></tr><tr><td>2</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>...</td></tr><tr><td>3</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>...</td></tr><tr><td>4</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>...</td></tr><tr><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>...</td></tr><tr><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td></td></tr></table>

The transformed ESACF makes it possible to identify a model without transforming the data to achieve stationarity, and without examining plots of the sample autocorrelation function and the sample partial autocorrelation function. Unfortunately, for reasonable sample sizes, the observed transformed ESACF may not closely resemble the prototype transformed ESACF. For example, it would not be unusual for the observed transformed ESACF for an ARMA 1,1 process to appear as in Table 4. In thisŽ . observed transformed ESACF table, it is not clear whether the vertex of the triangle of zeros is at cell 0,0 , cell 1,1 , or cell 1,2 .Ž . Ž . Ž .

Table 4  
Observed transformed ESACF table for an ARMA 1,1 process Ž .

<table><tr><td rowspan="2">AR</td><td colspan="6">MA</td></tr><tr><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>...</td></tr><tr><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>...</td></tr><tr><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>...</td></tr><tr><td>2</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>...</td></tr><tr><td>3</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>...</td></tr><tr><td>4</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>...</td></tr><tr><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>...</td></tr><tr><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td></td></tr></table>

The difficulty of identifying the prototype pattern in an observed ESACF table led several researchers <sup>w</sup> <sup>x</sup> 5–7,13 to explore whether neural networks could be a useful decision aid. Given the pattern in an observed ESACF table, a neural network <sup>w</sup> <sup>x</sup> 2,4,10,11,14 can be trained to choose which prototype pattern is most likely to have generated that observed pattern. The work to date appears promising, but has left three important questions unanswered.

First, both Lee and Jhee 5 and Lee and Oh 6<sup>w x</sup> <sup>w x</sup> generated training and test sets for their neural networks by randomly reversing 10%, 20%, and 30% of the $0 \mathrm { { ^ \circ } s }$ and $1 \mathrm { { } ^ { \circ } s }$ in a set of prototype transformed ESACF tables. Their intention was to see whether the ability of neural networks to correctly identify the order of ARMA models is adversely affected by the amount of noise in the series. Unfortunately, it is not possible to translate random reversals of $0 \mathrm { { ^ \circ } s }$ and $1 \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } }$ in an ESACF table into a meaningful measure of the amount of noise in or any other characteristicŽ of an ARMA process. Thus, for actual ARMA. processes, the number of reversals that are likely to occur in an observed ESACF table is unknown. It also is not known whether those reversals are randomly distributed throughout the transformed ESACF table, or clustered near the border of the triangle formed by the $0 ^ { \circ } \mathrm { s } .$ . Section 4 of this paper shows that if the reversals are clustered near the border, it is much more difficult to identify the order of the ARMA process. Thus, the fact that actual ARMA processes were not used by previous researchers to develop their training and test sets means the ability of neural networks to correctly identify the order of ARMA models currently is not known.

Second, previous researchers have not explicitly addressed the issue of series length. Because Lee and Jhee 5 and Lee and Oh 6 introduced noise by<sup>w x</sup> <sup>w x</sup> randomly reversing $0 \mathrm { { ^ \circ s } }$ and 1’s in a set of prototype transformed ESACF tables, they did not investigate the extent to which reversals in the prototype are dependent upon series length. Because Lee and Park <sup>w x</sup> <sup>w</sup> <sup>x</sup> 7 and Wang and Libert 13 focused on whether neural networks could correctly identify data series that had previously appeared in the literature, they also did not investigate the extent to which the number of reversals in a sample transformed ESACF table is dependent upon series length. The number of

Type I errors reversals ofŽ $0 ^ { \circ } \mathrm { s } )$ in an observed transformed ESACF table does not depend on series length, assuming the approximation of the asymptotic variance of the $r _ { j ( k ) } \mathrm { \ ' s }$ based on Bartlett’s formula is accurate. However, the number of Type II errors reversals of 1’s in an observed transformedŽ . ESACF table does depend on series length, since series length is what determines the power of the test. Thus it appears that series length may have an important impact on the ability of neural nets to correctly identify the order of ARMA models. Currently, the magnitude of this impact is unknown.

Third, converting the sample $r _ { j ( k ) }$ values to 0’s and $1 ^ { \circ } { \mathrm { s } }$ significantŽ . <sup>s</sup> 1, nonsignificant<sup>s</sup> 0 mimics the manual procedure that was suggested by Tsay and Tiao 12 , but may throw away information that<sup>w</sup> <sup>x</sup> can be used by the neural network to identify the underlying model. From a human perspective, using $0 \mathrm { { ^ \circ } s }$ and $1 \mathrm { { } } \mathrm { { } } \mathrm { { s } }$ may be preferable to using the sample values for $r _ { j ( k ) } ;$ but from a neural network perspective, it is not at all clear that throwing away the information contained in the sample values for $r _ { j ( k ) }$ is desirable. Currently, it is not known whether the ability of neural networks to correctly identify the order of ARMA models is enhanced or diminished by converting each sample value for $r _ { j ( k ) }$ to either 0 or 1.

The objective of this paper is to investigate the above three issues. More specifically, the objective is to measure:

1. The ability of a neural network to correctly identify the order of an underlying ARMA process given its sample ESACF table

2. The extent to which series length affects the ability of neural networks to correctly identify the order of the underlying ARMA process

3. Whether the ability of neural networks to correctly identify the order of the underlying ARMA process can be improved by using as input the sample $( - 1 < r _ { j ( k ) } < + 1 )$ values of the iterated autocorrelation coefficients rather than the transformed $( r _ { j ( k ) } = 0 \mathrm { ~ o r ~ } r _ { j ( k ) } = 1 )$ values.

When pursuing these objectives, ability is measured in terms of the percent of instances in which the neural network correctly identifies the order of the ARMA process. This makes the selection of the neural network’s training and test sets very important. The next section explains how the training and test sets were selected. In order to provide a basis for comparison with previous research, Section 3 replicates the work done by Lee and Jhee. Section 4 extends previous research by measuring the ability of neural networks to correctly identify the order of ARMA processes when actual series of varying lengths are used to generate the transformed ESACF tables. Section 5 further extends previous research by using actual rather than transformed values of the iterated autocorrelation coefficients to perform the pattern matching. The paper concludes with an assessment of the overall ability of neural networks to correctly identify the order of ARMA processes.

## 2. The training and test sets

If a neural network is trained and tested on series that are easy to identify, then the results are not generalizable to all series. This raises the question of what is an easy series to identify, and what is a difficult series to identify. In regression analyses, the difficulty of parameter estimation is a function of the size of the parameter, $\beta ,$ , and the size of the standard error of the parameter’s estimator, $\sigma _ { \hat { \beta } }$ . The size of $\sigma _ { \hat { \beta } }$ , in turn, depends upon the standard error of the regression, $\sigma _ { \varepsilon } ,$ , and the length of the series, n Žassuming time is the only independent variable ..

The situation is slightly different for ARMA models. The general form for an $\mathbf { A R M A } ( \mathbf { \phi } _ { p , q } )$ model is:

$$
\begin{array}{c} \Big (1 - \phi_ {1} B ^ {1} - \phi_ {2} B ^ {2} - \ldots - \phi_ {p} B ^ {p} \Big) Y _ {\mathrm{t}} \\ = \Big (1 - \theta_ {1} B ^ {1} - \theta_ {2} B ^ {2} - \ldots - \theta_ {q} B ^ {q} \Big) \varepsilon_ {\mathrm{t}} \end{array}
$$

where $Y _ { \mathrm { t } }$ is the series value, $\varepsilon _ { \mathrm { t } }$ is the noise value, B is the backshift operator, the $\phi ^ { \prime } \mathrm { s }$ are the autoregressive parameters, and the $\theta ^ { \star } s$ are the moving average parameters. Granger and Newbold 3 show that the<sup>w</sup> <sup>x</sup> covariance matrix of the ARMA parameter estimators depends on the size of the parameters and the length of the series, but does not depend on the standard deviation of the error term, $\sigma _ { \varepsilon } .$ Because the difficulty of parameter estimation does not depend on the amount of noise in the series, that factor does not need to be considered when selecting the series to train and test the neural network. The factors that must be considered are: 1 the order of the underly-Ž .

ing ARMA process; 2 the values of the ARMAŽ . parameters; and 3 the length of the series. Each of Ž . these factors is considered below.

## 2.1. Orders of the ARMA processes

An infinite order AR model can be represented by a first order MA model, and an infinite order MA model can be represented by a first order AR model Ž<sup>w</sup> <sup>x</sup> 8 , pp. 39 and 46 . Consequently, it generally is. possible to closely approximate a high order moving average model with a low order autoregressive model and vice versa. This is the reason why ARMA models generally have only a few parameters 8 , p. Ž<sup>w</sup> <sup>x</sup> 48 . Because ARMA models generally contain only. low order moving average and autoregressive parameters, only the following eight low order models were used to train and test the neural networks in this study: MA 1 , MA 2 , AR 1 , AR 2 , Ž . Ž . Ž . Ž . ARMA 1,1 , ARMA 1,2 , ARMA 2,1 , and Ž . Ž . Ž . ARMA 2,2 .Ž .

## 2.2. Values of the ARMA parameters

For any given series length, the values of the ARMA parameters determine how difficult it is to accurately estimate the parameters. To ensure that the training and test sets would not be biased in terms of parameter values that are easy to estimate, the parameter values for the generated series were randomly selected from the range of permissible values values that result in series that are stationaryŽ and invertible . To ensure adequate coverage of the. entire range, multiple parameter values were randomly generated for each of the eight $\mathbf { A R M A } ( \mathbf { \phi } _ { p , q } )$ processes. More specifically, the training set consisted of 100 series for each of the eight models $( 1 0 0 \times 8 = 8 0 0$ . series in total , and each of the 10 test sets consisted of 10 series for each of the eight models $( 1 0 \times 1 0 \times 8 = 8 0 0$ .  series in total . Ten different test sets were generated to facilitate construction of confidence intervals for the accuracy estimates.

The randomly selected parameter values were plotted to observe their distributions. For both the first and second order models, the parameter values were nearly uniformly distributed across the range of feasible values. This was true for both the training set and the test sets.

## 2.3. Lengths of the ARMA series

The standard errors of both the ARMA parameters and the iterated sample autocorrelation coefficients are inversely related to the length of the underlying series. Two different series lengths were selected for this study. A series length of 3000 was selected because the standard errors of both the ARMA parameters and the iterated sample autocorrelation coefficients are very close to zero for series of this length 12 . This should make the observed<sup>w</sup> <sup>x</sup> ESACF table be nearly identical to the prototype ESACF table, and thus make it very simple to identify the order of the underlying ARMA process. More succinctly, this is a best case scenario. It sets an upper limit on what can be expected in terms of the ability of a neural network to identify the order of an underlying ARMA process from its ESACF table.

A series length of 100 was selected because, for a monthly data series, this represents over 8 years of data. Given that economic and other environmental conditions change over time, it rarely is the case that more than 8 years of data are relevant for forecasting purposes. If the neural network is not effective at identifying the order of the underlying ARMA process from the ESACF table for series of this length, it is unlikely that this approach will be useful for practitioners. If the approach is effective for series of this length, then additional work will be required to determine the small sample properties of the approach.

## 3. Replication of Lee and Jhee’s 1994 work

Lee and Jhee 5 generated both their test and<sup>w</sup> <sup>x</sup> training sets by beginning with a transformed prototype ESACF, and then randomly inverting a specific number of elements i.e. changing a 1 to a 0 or viceŽ versa . In this manner, Lee and Jhee produced both. training and test sets with noise levels of approximately 10%, 20%, and 30% i.e. approximately 10%,Ž 20%, or 30% of the elements were inverted . The. noise levels are not exactly 10%, 20% and 30% because the number of $0 \mathrm { { ^ \circ } s }$ that were inverted was restricted to be less than $1 2 - p - q .$ The reason given for this restriction was that ‘‘noises in the triangle easily break the original shape of the ESACF pattern’’ What actually does and does not break the shape of the ESACF pattern is discussed in Section 4 of this paper.

Random reversals of 0’s and 1’s in the transformed prototype ESACF cannot be translated into meaningful characteristics of the underlying ARMA process, such as the values of the ARMA parameters or the length of the series. Nonetheless, the work of Lee and Jhee is replicated here in order to show that the algorithm used in this paper is equivalent to the algorithm used by Lee and Jhee with respect to its ability to discriminate among alternative ESACF patterns.

For several reasons, this paper’s replicated results are not expected to be identical to the results obtained by Lee and Jhee. The most significant differences between what they did and what we did are: Ž . Ž 1 they used 35 prototype ESACF tables up to an ARMA 5,5 model , whereas we used only eight Ž . . prototype ESACF tables up to an ARMA 2,2Ž Ž . model ; and 2 they used 10 by 10 ESACF tables, . Ž . whereas we used 8 by 8 ESACF tables. In addition, slightly different network configurations and learning algorithms were used in the two studies. Nevertheless, as shown in Table 5, the results from the two studies are remarkably similar. The average difference between the two classification percents is only 1.2 percentage points. Moreover, the difference between the two classification percents is not statistically significant at the 5% level for any of the nine cells in Table 5.

Table 5  
A comparison of Lee and Jhee’s results L&J with this study’s replication of Lee and Jhee’s work REPŽ . Ž .

<table><tr><td rowspan="2">Noise level in test set</td><td rowspan="2">Study indicator</td><td colspan="3">Mean correct classification % for different noise levels in the training set</td></tr><tr><td>10% Noise</td><td>20% Noise</td><td>30% Noise</td></tr><tr><td rowspan="2">10% Noise</td><td>L&amp;J</td><td>96.9</td><td>95.8</td><td>96.1</td></tr><tr><td>REP</td><td>93.0</td><td>97.5</td><td>97.5</td></tr><tr><td rowspan="2">20% Noise</td><td>L&amp;J</td><td>78.9</td><td>84.1</td><td>83.0</td></tr><tr><td>REP</td><td>72.0</td><td>82.0</td><td>87.0</td></tr><tr><td rowspan="2">30% Noise</td><td>L&amp;J</td><td>58.3</td><td>65.0</td><td>65.7</td></tr><tr><td>REP</td><td>56.5</td><td>63.0</td><td>64.5</td></tr></table>

The fact that our replicated results are nearly identical to Lee and Jhee’s original results is very important for interpreting the results presented in the remaining sections of this paper. Because there is very little difference in the discriminatory power of the algorithm used by Lee and Jhee and the algorithm used in this paper, ineffectiveness of the learning algorithm used in this paper cannot be the explanation for the inability of the neural networks to correctly identify the order of time series models when the ESACF is generated from actual ARMA processes.

## 4. Results from actual time series data

Table 5 appears to support Lee and Jhee’s assertion that neural networks are reasonably accurate with respect to identifying the order of an ARMA model given its ESACF table. Examination of how the results reported in Table 5 were produced, however, shows that actual ARMA processes were not used to generate the ESACF tables that were used as training and test sets for the neural networks. To draw any conclusions from Table 5, it is necessary to know what the noise level in ESACF tables is likely to be for actual ARMA processes. This section uses actual ARMA processes to generate the ESACF tables that are used as training and test sets for the neural networks.

## 4.1. Noise leÕels in the transformed ESACF tables

The noise level that is likely to be present in transformed ESACF tables was determined as follows.

Ž . 1 For each of the eight ARMA models identified in Section 2.1, 10 time series of length 3000 were generated for a total of 80 time series . The parame- Ž . ters for each time series were randomly selected from the permissible region, and the error terms were randomly selected from a normal distribution with a mean of zero and a standard deviation of one.

Ž . 2 For each of the 80 randomly generated time series in Step 1, a transformed ESACF table was generated; and for each observed transformed ESACF table, the total number of inversions was recorded. An inversion is defined as an instance in which a value in the observed transformed ESACF table is inverted 0 inverted to 1, or 1 inverted to 0 from itsŽ . corresponding value in the appropriate prototype transformed ESACF table.

Ž . 3 For the 80 ESACF tables, the mean number of inversions per ESACF table was computed, along with the standard deviation and a 95% confidence interval for the mean.

Steps 1 through 3 above also were performed for time series of length 100. The results are reported in Table 6.

The total number of elements in each ESACF table was 64 the table was 8 by 8 . The results showŽ . that for a time series with 3000 elements, approximately 11 inversions would be expected, which equates to a noise level of 17%. For a time series of length 100, approximately 21 inversions would be expected, which equates to a noise level of 33%. Table 5 does not contain entries for either 17% or 33% noise levels. Nevertheless, interpolation in Table 5 indicates that: 1 a neural network should be ableŽ .

Table 6  
Mean number of inversions per ESACF table

<table><tr><td>Time series length</td><td>Mean number of inverted elements</td><td>Mean percent of inverted elements</td><td>Standard deviation of mean</td><td>95% Confidence interval for mean</td></tr><tr><td>3000</td><td>10.87</td><td>17.0</td><td>0.53</td><td> $9.8 \leq \text{Mean} \leq 11.9$ </td></tr><tr><td>100</td><td>21.45</td><td>33.5</td><td>0.84</td><td> $20.6 \leq \text{Mean} \leq 22.3$ </td></tr></table>

Table 7  
Percent correctly classified by neural network for transformed iterated autocorrelation coefficients

<table><tr><td>Time series length</td><td>Average noise level</td><td>Mean % correct</td><td>SD of mean</td><td>95% Confidence interval</td></tr><tr><td>3000</td><td>17.0%</td><td>49.38</td><td>3.57</td><td> $42.34 \leq \text{Mean} \leq 56.36$ </td></tr><tr><td>100</td><td>33.5%</td><td>20.38</td><td>2.01</td><td> $16.44 \leq \text{Mean} \leq 24.31$ </td></tr></table>

to correctly identify the order of the underlying ARMA process for around 85% of series with a length of 3000; and 2 a neural network should be Ž . able to correctly identify the order of the underlying ARMA process for around 65% of series with a length of 100.

## 4.2. Accuracy of the neural network

Because actual ARMA processes were not used to generate the ESACF tables that comprised the training and test sets for the neural networks in Table 5, there is no assurance that the results reported in Table 5 are generalizable to actual ARMA processes. Table 7 presents results for the situation where actual ARMA processes were used to generate the ESACF tables. More specifically, the training and test sets were generated as follows.

Ž . 1 For the training set, 100 different series were randomly generated for each of the eight ARMA model types identified in Section 2.1 800 series inŽ total . The parameters for each model instance were. randomly generated from the permissible region, and the error terms were randomly generated from a normal distribution with a mean of zero and a standard deviation of one.

Ž . 2 Ten test sets were produced. For each test set, 10 different series were randomly generated for each of the eight ARMA model types identified in Section 2.1 80 series in total . The parameters for eachŽ . model instance were randomly generated from the permissible region, and the error terms were randomly generated from a normal distribution with a mean of zero and a standard deviation of one.

The training and test sets for both series lengths Ž . series of length 3000 and series of length 100 were generated using this procedure. In addition, the same parameter values were used for both series lengths.

Each neural network one for series of lengthŽ 3000 and one for series of length 100 was trained. using the training set, and tested using all 10 test sets. The neural networks were built in exactly the same manner as the network used to generate the results in Table 5. Nevertheless, the results in Table 7 are much different than the results in Table 5. For series of length 3000, the percent correctly classified is around 35 percentage points lower in Table 7; and for series of length 100, the percent correctly classified is around 45 percentage points lower in Table 7. Table 7 clearly shows that the ability of a neural network to correctly identify the order of an ARMA process from its sample ESACF is much lower than previously reported.

Two possible explanations are offered for the very large differences between the results reported in Tables 5 and 7. First, both humans and neural networks determine the order of the ARMA model by identifying the boundary between the zeroes and the ones in the transformed ESACF table see Table 3 .Ž . Hence the most damaging place for an inversion to occur is on the boundary between the $0 \mathrm { { ^ \circ } s }$ and the $1 \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } }$ Žeither the 1’s that are contiguous to the $0 ^ { \cdot } \mathrm { s } ,$ or the $0 \mathrm { { ^ \circ } s }$ that are contiguous to the 1’s . The results re-. ported in Table 5 assume that inversions in transformed ESACF tables are randomly distributed throughout the tables. That assumption does not appear to be valid. For the 80 series in the test sets, a disproportionate number of the inversions occurred on the boundary. Table 8 shows that, for series of length 3000, an inversion is 2.63 times more likely to occur on a boundary element than on a nonboundary element. For series of length 100, an inversion is

Table 8  
Boundary vs. nonboundary inversions

<table><tr><td></td><td>Percent of inverted boundary elements</td><td>Percent of inverted nonboundary elements</td><td>Ratio of boundary to nonboundary inversion percents</td></tr><tr><td>Length 3000</td><td>24.1</td><td>9.17</td><td>2.628</td></tr><tr><td>Length 100</td><td>37.6</td><td>31.2</td><td>1.205</td></tr></table>

1.20 times more likely to occur on a boundary element than on a nonboundary element.

The disproportionate number of inversions on the boundary, especially for very long series lengths, makes it more difficult for a neural network to determine the order of an $\mathbf { A R M A } ( \mathbf { \phi } _ { p , q } )$ model from its ESACF table.

The second explanation for the dramatic differences between the results reported in Tables 5 and 7 stems from two inconsistencies in Table 5. First, the noise levels for the training sets are mislabeled in Table 5. The training set labeled 20% noise in Table 5 actually contains a mixture of ESACF tables containing 10% noise and ESACF tables containing 20% noise. In fact, there are as many tables with 10% noise as there are tables with 20% noise in the group labeled 20% noise. Thus the average noise is 15%, not 20%. Similarly, the training set labeled 30% noise in Table 5 actually contains a mixture of ESACF tables containing 10% noise, 20% noise, and 30% noise, with the same number of tables from each noise category. Thus the average noise is 20%, not 30%.

The second inconsistency in Table 5 is that the size of the training set increases as the noise level increases. The training set for the 20% noise level contains all of the ESACF tables in the training set for the 10% noise level plus ESACF tables with 20% noise, and thus is nearly twice as large as the training set for the 10% noise level. Similarly, the training set for the 30% noise level contains all of the ESACF tables in the training set for the 20% noise level plus ESACF tables with 30% noise, and thus is nearly 33% larger than the training set for the 20% noise level. Larger training sets generally result in more accurate classification. The results in Table 5 indicate that accuracy increases as the noise level in the training set increases. This counterintuitive result may be due to increases in the size of the training sets rather than increases in the noise level in the training sets.

In Table 7, the noise level column is the average noise level, and the training sets are the same size for series of length 100 and series of length 3000. Since the purpose of Table 5 is to compare the algorithm used by Lee and Jhee 5 with the algorithm used in <sup>w</sup> <sup>x</sup> this paper, it was necessary to replicate Lee and Jhee’s inconsistencies in Table 5. However, because the columns are mislabeled in Table 5, and because the size of the training sets is not constant in Table 5, the information reported in Table 5 is not as meaningful as the information reported in Table 7.

## 5. Untransformed values of the iterated autocorrelation coefficients

Converting the sample $r _ { j ( k ) }$ values to $0 \mathrm { { ^ \circ } s }$ and 1’s Ž . significant<sup>s</sup> 1, nonsignificant<sup>s</sup> 0 makes it easier for humans to see the pattern in the ESACF table, but may throw away information that could be used by the neural network to identify the underlying model. A priori, it is not clear whether throwing away the information contained in the sample values for $r _ { j ( k ) }$ is desirable or undesirable. This section examines whether the ability of neural networks to correctly identify the order of the underlying ARMA process can be improved by using as inputs the sample $( - 1 < r _ { j ( k ) } < + 1 )$ values of the iterated autocorrelation coefficients rather than the transformed $( r _ { j ( k ) } = 0 \mathrm { ~ o r ~ } r _ { j ( k ) } = 1 )$ values.

In this experiment, the ESACF tables used for the training and test sets were the same ones that were used to conduct the experiment described in Section 4, except that the raw values for the $r _ { j ( k ) }$ were not converted to zeroes and ones. Moreover, the neural networks were built in the same manner as the networks used to produce the results in Table 7.

Comparison of Table 9 with Table 7 shows that the neural networks performed much more poorly when raw untransformed values were used for theŽ . iterated autocorrelation coefficients. The most likely explanation for this is that many of the population values for the $r _ { j ( k ) }$ are quite small. This makes it very difficult for both humans and neural networks to determine whether a nonzero sample value for a $r _ { j ( k ) }$ is due to sampling error or a nonzero population value. Table 9 clearly shows that the ability of a neural network to correctly identify the order of an underlying ARMA process from its ESACF cannot be improved by using untransformed rather than transformed values for the iterated autocorrelation coefficients.

Percent correctly classified by neural net for untransformed iterated autocorrelation coefficients

<table><tr><td>Time series length</td><td>Mean % correct</td><td>SD of mean</td><td>95% Confidence interval</td></tr><tr><td>3000</td><td>16.12</td><td>1.36</td><td> $13.04 \leq \text{Mean} \leq 19.21$ </td></tr><tr><td>100</td><td>10.50</td><td>1.53</td><td> $7.04 \leq \text{Mean} \leq 13.96$ </td></tr></table>

## 6. Conclusions and future research

This paper examines the ability of a neural network to identify the order of an underlying ARMA process from its ESACF table. Following the lead of several other authors 5–7,13 , ability is quantified as <sup>w</sup> <sup>x</sup> the percent of instances in which the neural network correctly identifies the order of the ARMA process. The most important findings are:

Ž . 1 The ability of a neural network to correctly identify the order of an ARMA process from its sample ESACF is much lower than previously reported. For series of length 100, the percent of instances in which the order is correctly identified is only 20%. This indicates that the approach may not be very useful to practitioners.

Ž . 2 Series length dramatically affects the ability of neural networks to correctly identify the order of the underlying ARMA process. The longer the series, the more accurate the identification process. However, the percent of instances in which the order is correctly identified is below 50% even for extremely long series lengths 3000 observations . Ž .

Ž . 3 The ability of neural networks to correctly identify the order of the underlying ARMA process cannot be improved by using as inputs the sample $( - 1 < r _ { j ( k ) } < + 1 )$ values of the iterated autocorrelation coefficients rather than the transformed $( r _ { j ( k ) } = 0$ or $r _ { j ( k ) } = 1 )$ values. Using the raw untransformed  Ž . values for $r _ { j ( k ) }$ reduced the accuracy by 48% for series of length 100, and by 67% for series of length 3000.

Taken together, the above findings indicate that neural networks may not be able to accurately identify the order of an ARMA process from its ESACF table.

Before abandoning the approach, however, additional research is needed. First, neural networks may not have to accurately identify the order of the underlying ARMA model in a high percentage of cases in order to be useful. The reason for this is that many ARMA models are equivalent, or nearly equivalent. For example the model

$$
\begin{array}{r l} \big (1 - 0. 7 B \big) Y _ {\mathrm{t}} & = \big (1 - 0. 5 B - 0. 1 4 B ^ {2} \big) \varepsilon_ {\mathrm{t}} \\ & = \big (1 + 0. 2 B \big) \big (1 - 0. 7 B \big) \varepsilon_ {\mathrm{t}} \end{array}
$$

is exactly equivalent to

$$
Y _ {\mathrm{t}} = (1 + 0. 2 B) \varepsilon_ {\mathrm{t}}.
$$

But the model

$$
\begin{array}{r l} (1 - 0. 6 9 B) Y _ {\mathrm{t}} & = (1 - 0. 5 B - 0. 1 4 B ^ {2}) \varepsilon_ {\mathrm{t}} \\ & = (1 + 0. 2 B) (1 - 0. 7 B) \varepsilon_ {\mathrm{t}} \end{array}
$$

is not exactly equivalent to

$$
Y _ {\mathrm{t}} = (1 + 0. 2 B) \varepsilon_ {\mathrm{t}}.
$$

In practice, does it really matter if $( 1 - 0 . 6 9 \mathbf { B } ) Y _ { \mathrm { t } } =$ $( 1 - 0 . 5 B - 0 . 1 4 B ^ { 2 } ) \varepsilon _ { \mathrm { t } }$ is identified as an ARMA 0,1 model rather than an ARMA 1,2Ž . Ž . model? Will forecasts from the two models be nearly identical? Currently, no criteria exist for defining practical equivalence for ARMA models. Moreover, if such criteria can be defined, no one knows how accurate neural nets will be at identifying a model that is practically equivalent to the true model.

Second, many practitioners currently use overfitting to determine the order of an ARMA process. Overfitting adding an additional autoregressive orŽ moving average parameter and testing it for significance is an easily understood and easily imple-. mented procedure. Unfortunately, no one has shown how accurate overfitting is. If neural nets are more accurate than overfitting, then they will be helpful to practitioners. If neural nets are less accurate than overfitting, then they probably will not be very helpful to practitioners. Additional research is needed to define what is practical equivalence, to determine how accurate neural nets are at identifying a practically equivalent model, and to determine how accurate overfitting is at identifying a practically equivalent model.

## 7. Uncited references

<sup>w</sup> <sup>x</sup> <sub>14</sub> w x <sub>2</sub> w x <sub>4</sub> w x <sub>9</sub>

## References

<sup>w</sup> <sup>x</sup> 1 G.E.P. Box, G.M. Jenkins, Time Series Analysis: Forecasting and Control, Holden-Day, San Francisco, CA, 1976.

<sup>w</sup> <sup>x</sup> 2 G. Cybenko, Approximation by superpositions of a sigmoidal function, Mathematics of Control, Signals, and Systems 2 Ž .1989 303–314.

<sup>w</sup> <sup>x</sup> 3 C.W.J. Granger, P. Newbold, Forecasting Economic Time Series, Academic Press, San Diego, CA, 1986.

<sup>w</sup> <sup>x</sup> 4 S. Haykin, Neural Networks: A Comprehensive Foundation, MacMillan, New York, NY, 1995.

<sup>w</sup> <sup>x</sup> 5 J.K. Lee, W.C. Jhee, A two stage neural network approach for ARMA model identification with ESACF, Decision Support Systems 11 1994 461–479.Ž .

<sup>w</sup> <sup>x</sup> 6 K.C. Lee, S.B. Oh, An intelligent approach to time series identification by a neural network-driven decision tree classifier, Decision Support Systems 17 1996 183–197.Ž .

<sup>w</sup> <sup>x</sup> 7 K.C. Lee, S.J. Park, Decision support in time series modeling by pattern recognition, Decision Support Systems 4 1988Ž . 199–207.

<sup>w</sup> <sup>x</sup> 8 C.R. Nelson, Applied Time Series Analysis for Managerial Forecasting, Holden-Day, San Francisco, CA, 1973.

<sup>w</sup> <sup>x</sup> 9 K. Ord, S. Lowe, Automatic Forecasting, The American Statistician 50 1 1996 88–94.Ž . Ž .

<sup>w</sup> <sup>x</sup> 10 M. Riedmiller and H. Braun, A Direct Adaptive Method for Faster Back Propagation Learning: the RPROP Algorithm, Proceedings of the Ieee Conference on Neural Networks, San Francisco, CA, IEEE Press, 1993.

<sup>w</sup> <sup>x</sup> 11 Rumelhart et al., Parallel Distributed Processing: Explorations in the Microstructure of Cognition Vols. 1 and 2 MIT Press, Cambridge, MA, 1986.

<sup>w</sup> <sup>x</sup> 12 R.S. Tsay, G.C. Tiao, Consistent estimates of autoregressive parameters and extended sample autocorrelation functions for stationary and nonstationary ARMA models, Journal of the American Statistical Association 79 385 1984 8–96.Ž . Ž .

<sup>w</sup> <sup>x</sup> 13 L. Wang, G.A. Libert, Combining pattern recognition techniques with Akaike’s information critieria for identifying ARMA models, IEEE Transactions on Signal Processing 42 Ž . Ž . 6 1994 1388–1396.

<sup>w</sup> <sup>x</sup> 14 S. Weiss, C. Kulikowski, Computer Systems That Learn, Morgan Kaufmann, 1991.

Tim Chenoweth is an Assistant Professor of Computer Information Systems in the College of Business at Arizona State University. He received his PhD degree from Washington State University in 1996. Dr.Chenoweth currently is conducting research in the areas of applying machine learning techniques to large-scale business problems and making technical tools more accessible to non-technical managers.

Robert Hubata is an econometrician at American Express Company in Phoenix, Arizona. He received an AB in Mathematics from the University of California at Berkeley in 1967, and an MS in Decision and Information Systems from Arizona State University main campus in 1994. He currently is a doctoral student atŽ . Arizona State University. His research interests and publications are in the areas of time series modeling, forecasting, and econometrics. He is a member of Phi Kappa Phi, the American Mathematical Society, the American Statistical Association, and the Mathematical Association of America.

Robert St. Louis is an Associate Professor of Computer Information Systems in the College of Business at Arizona State University. He received an AB in Economics in 1966 from Rockhurst College, an MS in Economics in 1968 from Purdue University, and a PhD in Economics in 1972 from Purdue University. His research and teaching interests are in the areas of databases, data mining, and decision support systems.
