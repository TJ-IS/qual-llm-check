---
otero_id: 11742
otero_key: "H8HVSPG5"
title: "A hybrid approach by integrating wavelet-based feature extraction with MARS and SVR for stock index forecasting"
authors: "Ling-Jing Kao; Chih-Chou Chiu; Chi-Jie Lu; Chih-Hsiang Chang"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.11.012"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A hybrid approach by integrating wavelet-based feature extraction with MARS and SVR for stock index forecasting

Ling-Jing Kao <sup>a</sup>, Chih-Chou Chiu <sup>a</sup>, Chi-Jie Lu <sup>b,</sup>⁎, Chih-Hsiang Chang <sup>c</sup>

<sup>a</sup> Department of Business Management, National Taipei University of Technology, Taiwan

<sup>b</sup> Department of Industrial Management, Chien Hsin University of Science and Technology, Taiwan

<sup>c</sup> Institute of Commerce Automation and Management, National Taipei University of Technology, Taiwan

## a r t i c l e i n f o

Article history: Received 20 March 2012 Received in revised form 9 October 2012 Accepted 11 November 2012 Available online 20 November 2012

Keywords: Stock index forecasting Wavelet transform Multivariate adaptive regression splines Support vector regression Feature extraction

## a b s t r a c t

Forecasting stock prices is a major activity of <sup>fi</sup>nancial <sup>fi</sup>rms and private investors when they make investment decisions. Feature extraction is usually the <sup>fi</sup>rst step of a stock price forecasting model development. Wavelet transform, used mainly for the extraction of information contained in signals, is a signal processing technique that can simultaneously analyze the time domain and the frequency domain. When wavelet transform is employed to construct a forecasting model, the wavelet basis functions and decomposition stages need to be determined <sup>fi</sup>rst. However, because forecasting models constructed by different wavelet sub-series would exhibit different forecasting capabilities and yield varying forecast results, the selection of wavelet that can lead to an optimal forecast outcome is extremely critical in model construction. In this study, a new stock price forecasting model which integrates wavelet transform, multivariate adaptive regression splines (MARS), and support vector regression (SVR) (called Wavelet-MARS-SVR) is proposed to not only address the problem of wavelet sub-series selection but also improve the forecast accuracy. The performance of the proposed method is evaluated by comparing the forecasting results of Wavelet-MARS-SVR with the ones made by other <sup>fi</sup>ve competing approaches (Wavelet-SVR, Wavelet-MARS, single ARIMA, single SVR and single ANFIS) on the stock price data of two newly emerging stock markets and two mature stock markets. The empirical study shows that the proposed approach can not only solve the problem of wavelet sub-series selection but also outperform other competing models. Moreover, according to the sub-series which are selected by the proposed approach, we can successfully identify the data of which sessions (or points in time) among past stock market prices exerted signi<sup>fi</sup>cant impact on the construction of the forecasting model. © 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

The stock market has long been one of the investment targets that investors pay most attention to. In order to gain pro<sup>fi</sup>ts or to avoid risks, investors usually conjecture the trend of stock indices and draw up strategies for future investments according to their anticipation. Therefore, the construction of an effective stock price forecasting model which can be used to reduce the personal bias and mistakes is the major concern for individual, institutional investors and researchers. For example, Atsalakis and Valavanis [4] and Bahrammirzaee [6] survey various computing methods in stock market forecasting, Chang and Fan [9] propose an integrated approach of wavelet and fuzzy system for stock price forecasting, Khansa and Liginlal [22] compare the performance of vector autoregression and time-delayer neural network in stock market forecasting, Lu et al. [26] use independent components analysis to perform feature extraction and support vector regression in <sup>fi</sup>nancial time series forecasting, and Tsai and Hsiao [44] combine well-known feature selection methods, principal component analysis, genetic algorithms, and decision trees to identify more representative variables for better prediction. However, owing to the highfrequency, non-stationary and chaotic properties of the stock index data [19,24,48], a stock price forecasting model utilizing the original stock index data fails to provide satisfying forecast results. To solve this problem, before constructing a forecasting model, many studies would <sup>fi</sup>rst utilize an information extraction technique to extract features (also called latent signals) contained in data, then use these extracted characteristics to construct the forecasting model [9,24,26,35].

Wavelet transform, used mainly for extracting information contained in signals, is a type of signal processing technique that can simultaneously analyze the time domain and the frequency domain. Conceptually, wavelet transform uses wavelet basis functions to decompose the original sign into different sub-series and highlight the eigenvalues hidden in the original signal. Traditionally, wavelet transform is primarily applied to image processing or signal processing [36,39,43]; however, with its powerful feature extraction capability, wavelet transform has now been successfully applied to time-series studies [2,7,12,17,18,20,24,32,33,37].

For example, Bjorn [7] employed the wavelet transform to obtain <sup>fi</sup>nancial time series featuring fractal and chaotic characteristics, and utilized these resulting series as input factors to carry out forecasting. Pan and Wang [32] adopted wavelet transform as the estimator of random, non-linear regression and incorporated it into the state space model to carry out an empirical study on the S&P 500 Index, discovering the forecastability of the stock market. Gonghui et al. [18] used redundant Haar wavelet transform, together with the dynamic recurrent neural network, to construct the forecasting model, obtaining experimental results that showed the wavelet transform's capability to effectively increase the forecast accuracy of the neural network. Furthermore, Shin and Han [38] adopted the genetic algorithm to optimize the multi-resolution analysis of wavelet transform and used the arti<sup>fi</sup>cial neural network to forecast the Korean Won exchange rate. The results of Shin and Han [38] showed that the forecast accuracy of the optimized model was clearly better than the general arti<sup>fi</sup>cial neural network.

Zhang et al. [50] extracted features out of <sup>fi</sup>nancial time series by applying wavelet transform to the data and then constructed three different types of forecasting models by taking all the subsets as input variables for the arti<sup>fi</sup>cial neural network, yielding results that indicated the wavelet transform-based model possessed the minimum prediction errors. Dai and Lu [13] utilized wavelet transform to break down closing prices on the Nikkei 225 into multiple sub-series and subsequently built the forecasting model by SVR (support vector regression), discovering that wavelet transform-treated stock price information can effectively enhance the forecasting capability of SVR. Zhao et al. [51] used Shanghai stock market data to compare the forecasting capabilities of the traditional ARIMA model, the ANN model, and the model that combines wavelet transform and arti<sup>fi</sup>cial intelligence techniques. The results show that, in analyzing <sup>fi</sup>nancial time series information, wavelet transform was able to extract more useful information. Chang and Fan [9] integrated Haar wavelet transform and Takagi–Sugeno–Kang (TSK) fuzzy rule-based systems for stock price forecasting. They applied wavelet transform to decompose the time series data into multiple sub-series, calculated the technical indices of stock price in the various sub-series, and ultimately employed the TSK fuzzy-rule-based system to predict stock price based on a set of selected technical indices. The empirical result showed that the wavelet-preprocessed TSK forecasting model outperformed the TSK forecasting model that did not apply wavelet transform.

Generally speaking, when wavelet transform is employed to construct a forecasting model, the wavelet basis functions and decomposition stages need to be determined <sup>fi</sup>rst. The obtained wavelet sub-series are then applied to the forecasting model as input variables. However, because large amount of sub-series are generated from wavelet transform decompositions under different bases and stages, the excessiveness of input variables and the time-consumption of model construction are two problems often encountered when all sub-series are considered simultaneously. Also, forecasting models constructed by different wavelet sub-series would exhibit different forecasting capabilities and yield varying forecast results [13,17,33]. Therefore, how to identify wavelet sub-series that affect the forecast result is indeed an important task.

In this paper, we propose a new stock forecasting approach which integrates wavelet transform, multivariate adaptive regression splines (MARS) and support vector regression (SVR) approach (called Wavelet-MARS-SVR) to not only address the problem of variable selection but also improve the forecast capability. In this new approach, MARS is used to determine the importance of sub-series obtained from wavelet transform, and SVR is used to construct the stock forecasting model. We adopted MARS because it can compute the degrees of importance of variables from the numerous piecewise equations and is often used for identifying signi<sup>fi</sup>cant variables [3,27,47,52]. And SVR is chosen for the stock forecasting model because it has been widely applied to various <sup>fi</sup>nancial time series forecasting problems and has delivered excellent results [6,11,26,31,41,42].

Our proposed approach consists of three stages. In the <sup>fi</sup>rst stage, by utilizing wavelet transform, we decompose the predictor variable under different basis functions and decomposition stages to get the sub-series. In the second stage, we use MARS to identify the signi<sup>fi</sup>cant sub-series among all sub-series obtained from the wavelet transform. Finally, in the third stage, the identi<sup>fi</sup>ed sub-series containing the key factors that affect forecasting accuracy are applied in SVR as new input variables to build a forecasting model.

To evaluate the performance of the proposed method, two newly emerging stock market indices (SSEC & Bovespa) and two mature stock market indices (Dow Jones & Nikkei 225) are used in this study. The forecast accuracy of Wavelet-MARS-SVR is also compared with other approaches, such as Wavelet-SVR, Wavelet-MARS, single ARIMA, single SVR, and single adaptive neuro fuzzy inference system (ANFIS) models. The ARIMA and ANFIS models are selected as benchmarks in model comparison because the ARIMA model is an essential and important approach to forecast stock index [31,48] and the ANFIS model proposed by Jang [21] is a well-known and effective neurofuzzy system for stock price forecasting [5,8,10]. The result shows the proposed Wavelet-MARS-SVR approach can not only solve the problem of variable selection, identify the signi<sup>fi</sup>cant periods that affect the highs and lows of indices for the respective stock markets, but also have the best forecasting accuracy.

This paper contributes to the wavelet literature and stock forecasting in the following three aspects. First, basis functions and decomposition stages that were used to generate the selected sub-series can be investigated, and investigation results can be served as reference for the selection of appropriate wavelet basis functions in predicting a speci<sup>fi</sup>c stock index. Secondly, the signi<sup>fi</sup>cance represented by the selected signi<sup>fi</sup>cant sub-series in respect to stock price data can be analyzed to subsequently <sup>fi</sup>gure out the data of which sessions (or points in time) among past stock market prices exerted signi<sup>fi</sup>cant impacts on the construction of the forecasting model. Thirdly, through the signi<sup>fi</sup>cant sub-series identi-<sup>fi</sup>ed by MARS, the proposed Wavelet-MARS-SVR approach can construct the forecasting model more ef<sup>fi</sup>ciently because the construction time for Wavelet-MARS-SVR is only two-thirds of Wavelet-SVR's.

The rest of this paper is organized as follows. Section II gives a brief introduction to wavelet transform, MARS and SVR. The proposed hybrid forecasting model is thoroughly described in Section III. Section IV presents the empirical results from the datasets including the SSEC, Bovespa, Dow Jones and Nikkei 225 indexes. The paper is concluded in Section V.

## 2. Research methodology

## 2.1. Wavelet transform

In this section, a brief description of wavelet transform is given. For a thorough review of wavelet transform we refer to [14,24,33]. Practical application of wavelet analysis is given in [17].

Wavelet transform is a strong mathematical tool that provides a time-frequency representation of an analyzed signal in the time domain [14,28]. It can be divided into continuous wavelet transform (CWT) and discrete wavelet transform (DWT) depending on their natures. The CWT W(u, v) of signal f(x) with respect to a mother wavelet ψ(x) is given:

$$
W (u, v) = u ^ {- 1 / 2} \int_ {- \infty} ^ {\infty} f (x) \psi \left(\frac {x - v}{u}\right) d x\tag{1}
$$

where the dilation (or scale) parameter u controls the spread of the wavelet and translation parameter v determines its central position.

Translation de<sup>fi</sup>nes the time shift, and dilation de<sup>fi</sup>nes the time scale. The $W ( u , \nu )$ coef<sup>fi</sup>cient (called wavelet coef<sup>fi</sup>cient) represents how well the original signal f(x) and the scaled/translated mother wavelet match. Thus, the set of all wavelet coef<sup>fi</sup>cients, associated to a particular signal, is the wavelet representation of the signal with respect to the mother wavelet.

Since the CWT is achieved by continuously scaling and translating the mother wavelet, substantial redundant information is generated, which is one of the main disadvantages of CWT [14,17,28]. To alleviate this redundancy problem, researchers always scaled and translated the mother wavelet based on powers of two [14,17,28]. This scheme, known as the DWT, is as accurate as the CWT and is one of the most adopted methods in literature [17,33]. For illustration, we can de<sup>fi</sup>ne the DWT as:

$$
W (p, q) = 2 ^ {- (p / 2)} \sum_ {t = 0} ^ {T - 1} f (t) \psi \left(\frac {t - q \cdot 2 ^ {p}}{2 ^ {p}}\right)\tag{2}
$$

where T is the length of the signal $f ( x )$ . The scaling and translation parameters are functions of the integer variables p and $q \ ( u = 2 ^ { p }$ $\nu = q \cdot 2 ^ { p } )$ ; t is the discrete time index.

In most practical applications, based on multi-resolution analysis (MRA) [28], DWT can be achieved by the straightforward <sup>fi</sup>ltering operation which directly implements a convolution of signal f(t) and the wavelet at scale u. Thus, the wavelet plays a role of band-pass <sup>fi</sup>lter (the band corresponds to the scale). There is a fast algorithm for the DWT. In fast DWT, <sup>fi</sup>rst, an original discrete signal $f ( t )$ is decomposed into two components, $A _ { 1 }$ and $D _ { 1 } ,$ , by convoluting the signal with a decomposition low-pass <sup>fi</sup>lter $( \mathsf { D \_ L P } )$ and a decomposition high-pass <sup>fi</sup>lter (D\_HP), respectively. The decomposition low-pass and highpass <sup>fi</sup>lters can be derived from mother wavelet. The $A _ { 1 }$ , named the approximation of the signal, contains the general trend (or low frequency components) of the signal $f ( t )$ , and the $D _ { 1 } ,$ , named the detail of the signal, is associated with the high frequency components of the signal $f ( t )$ . Then, the approximation $A _ { 1 }$ is again decomposed into a new approximation $A _ { 2 }$ and a detail $D _ { 2 }$ by a larger scale and continuing to a third scale, fourth scale and so on, according to the application. (In Wavelet Transform, the scale parameter u is analogous to frequency and is a measure of the amount of detail in the signal. Therefore, a larger scale means that more of a time series is used in the calculation of the coef<sup>fi</sup>cients). By successive decomposition of the approximations, a multistage decomposition process can be achieved where the original signal is broken down into lower resolution components (or subseries) in terms of the following expansion coef<sup>fi</sup>cients: $f ( t ) =$

$A _ { L } + \sum _ { i = 1 } ^ { L } D _ { i }$ , where $A _ { L }$ is the approximation of the signal f(t) at stage $L ,$ and $D _ { i }$ are the details of the signal f(t) at stage $i { = } 1 , 2 { \mathrm { , . . . , } } L .$ Fig. 1 shows a schematic of multi-resolution analysis of DWT decomposition.

There are many kinds of wavelets which can be used as a mother wavelet, such as Meyer wavelet, Daubechies wavelet, Morlet wavelet and so on [33,36]. These wavelets have different speci<sup>fi</sup>cities. Daubechies wavelet is one of the most widely used wavelets and is compactly supported orthonormal wavelet and has nice performance in time series forecasting [9,24,35,50]. In this paper, the Daubechies wavelet is applied. The names of the Daubechies family wavelets are written as DB“N”, where N is the order, and DB the “surname” of the wavelet.

![](/api/attachments/H8HVSPG5/fulltext/images/8dd68f00d61cf219ce7fbe88dfb8e5e9fa7b276e4230660e60273fa6548a8fdf.jpg)  
Fig. 1. Multi-resolution analysis of DWT decomposition.

In DWT, traditionally, the dyadic down-sampling process is imposed at each stage for ef<sup>fi</sup>ciently compressing the original signal information into a compressed representation [28]. However, the major inconvenience of the DWT with down-sampling is that it is not translationinvariant [24,45]. That is, down-sampling has the undesirable effect: one cannot relate information at a given timing point at different scales in a simple manner. Moreover, while it is desirable in some applications (e.g. image compression) to remove the redundant information, in time series forecasting tasks, the redundant information can be used to improve the accuracy of the forecasting. Unser [45] proposed an overcomplete wavelet representation, namely the discrete wavelet frame transform (DWFT), to alleviate the problem caused by the dyadic down-sampling process of DWT. DWFT resembles the DWT counterpart and avoids the down-sampling operations in DWT. Thus, it guarantees aliasing degree and yields a shift invariant signal representation [24,45]. Like DWT, performing DWFT to L decomposition stages also results in a total of L details sub-series (i.e. $D _ { i } )$ and one approximation sub-series $\left( \mathrm { i } . \mathrm { e } . \ A _ { L } \right)$ . Each sub-series in DWFT has the same size as the original signal.

## 2.2. Multivariate adaptive regression splines

Because, in our proposed Wavelet-MARS-SVR stock price forecasting model, we utilize MARS to identify signi<sup>fi</sup>cant sub-series among all sub-series obtained from the wavelet transform, a brief introduction of MARS is provided in this sub-section.

MARS is a nonlinear and non-parametric regression methodology proposed by Friedman [16]. The MARS modeling procedure is based on a divide-and-conquer strategy in which training data sets are partitioned into separate regions, each of which is assigned its own regression equation.

MARS essentially builds <sup>fl</sup>exible models by <sup>fi</sup>tting piecewise linear regressions; that ${ \mathrm { i } } s ,$ the non-linearity of a model is approximated through the use of separate linear regression slopes in distinct intervals of the independent variable space. Therefore, the slope of the regression line is allowed to change from one interval to the other as the two ‘knot’ points are crossed. The variables to be used and the end points of the intervals for each variable are found through a fast but intensive search procedure. In addition to searching for variables one by one, MARS also searches for interactions between variables, allowing any degree of interaction to be considered as long as it can provide a better <sup>fi</sup>t with the data.

The general MARS function is de<sup>fi</sup>ned by the following equation [16,23].

$$
f (x) = a _ {0} + \sum_ {m = 1} ^ {M} a _ {m} \prod_ {k = 1} ^ {K - m} \left[ s _ {k, m} \left(x (k, m) - t _ {k, m}\right) \right],\tag{3}
$$

where $a _ { 0 }$ is a constant; $a _ { m }$ are the coef<sup>fi</sup>cients of the model, which are estimated to yield the best <sup>fi</sup>t to the data; M is the number of basis functions; K \_m is the number of splits that generate the m-th basis function; $s _ { k , m }$ takes values of either $1 \ 0 \Gamma - 1$ and indicates the right/ left sense of the associated step function; x(k,m) is the label of the independent variable; and $t _ { k , m }$ indicates the knot locations.

The optimal MARS model is determined by a two-stage process. First, MARS initially constructs a very large number of basis functions to over<sup>fi</sup>t the data, where variables are allowed to enter as continuous, categorical, or ordinal, and they can interact with one another or be restricted to entry as additive components only. In the second stage, basis functions are deleted in the order of least contributions using the generalized cross-validation (GCV) criterion [16] which is de<sup>fi</sup>ned as

$$
\operatorname{GCV} (M) = \frac {1}{N} \sum_ {i = 1} ^ {N} \frac {\left[ y _ {i} - f _ {M} \left(x _ {i}\right) \right] ^ {2}}{\left[ 1 - \frac {C (M)}{N} \right] ^ {2}},\tag{4}
$$

where N denotes the number of observations; $C ( M )$ is the cost-penalty measures of a model containing M basis functions; the numerator measures the lack of <sup>fi</sup>t on the M basis function model $f _ { M } ( x _ { i } )$ and the denominator denotes the penalty for model complexity $C ( M ) ) ; y _ { i }$ is the target outputs. In other words, the purpose of C(M) is to penalize model complexity, to avoid over<sup>fi</sup>tting, and to promote model parsimony. To do so, C(M) introduces a cost incurred per basis function to the model. This is similar to the adjusted $R ^ { 2 }$ in least-squares regression. It is usually de<sup>fi</sup>ned as $C ( M ) = M$ in linear least-squares regression.

The importance of a variable is assessed by observing the decrease in the calculated GCV when this variable is removed from the model. This process continues until the remaining basis functions all satisfy the pre-determined requirements.

After creating a MARS model, one can estimate the relative importance of a variable based on its contribution to the <sup>fi</sup>t of the model on a scale of 0–100. To do this, MARS deletes all terms containing the selected variable, re<sup>fi</sup>ts the model and then calculates the <sup>fi</sup>t's reduction, called score. Thus, the score corresponds to the ratio of the reduction in <sup>fi</sup>t produced by these variables to that of the most important variable. The most important variable which has the highest score is the one that reduces the <sup>fi</sup>t of the model most after being deleted, and vice versa. MARS is capable of tracking very complex data structures which are often concealed in high-dimensional data. Please refer to Friedman [16] for more details regarding the model building process.

## 2.3. Support vector regression

SVR, built upon statistical learning theory, is a novel neural network algorithm technique that has received increasing attention as a method for solving nonlinear regression estimation problems. SVR is derived from the structural risk minimization principle to estimate a function by minimizing an upper bound of the generalization error [46].

According to Vapnik [46], the SVR model is expressed as:

$$
f (x) = (\mathbf {z} \cdot \phi (x)) + b,\tag{5}
$$

where z is a weight vector, b is bias, and $\phi ( x )$ is a kernel function which is usually de<sup>fi</sup>ned as a non-linear function to transform non-linear inputs to a linear mode in a high-dimensional feature space. Unlike the traditional regression model whose coef<sup>fi</sup>cients are estimated by minimizing the square loss, SVR applies so called ε-insensitivity loss function to estimate its parameters. ε-insensitivity loss function is de<sup>fi</sup>ned as:

$$
L _ {\varepsilon} (f (x) - y) = \left\{ \begin{array}{c c} | f (x) - y | - \varepsilon & i f | f (x) - y | \geq \varepsilon \\ 0 & \text { otherwise } \end{array} \right.,\tag{6}
$$

where y is the desired(target) output; ε is de<sup>fi</sup>ned as the region of ε-insensitivity. When the predicted value falls into the band area, the loss is zero. In contrast, if the predicted value falls outside the band area, then the loss is equal to the difference between the predicted value and the margin.

When empirical risk and structure risk are considered together, the SVR model can be constructed to minimize the following quadratic programming problem.

$$
\operatorname{Min}: \frac {1}{2} \mathbf {z} ^ {T} \mathbf {z} + C \sum_ {i} \left(\xi_ {i} + \xi_ {i} ^ {*}\right)
$$

$$
\text { Subject   to } \left\{ \begin{array}{c} y _ {i} - \mathbf {z} ^ {T} x _ {i} - b \leq \varepsilon + \xi_ {i} \\ \mathbf {z} ^ {T} x _ {i} + b - y _ {i} \leq \varepsilon + \xi_ {i} ^ {*}, \\ \xi_ {i}, \xi_ {i} ^ {*} \geq 0 \end{array} \right.\tag{7}
$$

where $i { = } 1 , { \ldots } , n$ is the number of training data; $( \xi _ { i } + \xi _ { i } ^ { * } )$ is the empirical risk; $\scriptstyle { \frac { 1 } { 2 } } \mathbf { z } ^ { T } \mathbf { z }$ is the structure risk preventing over-learning and lack of applied universality; and C is a modifying coef<sup>fi</sup>cient representing the trade-off between empirical risk and structure risk. With an appropriate modifying coef<sup>fi</sup>cient C, band area width $\varepsilon ,$ and kernel function $K ,$ the optimum value of each parameter can be solved by Lagrange. We follow Vapnik [46] and adopt the general form of the SVR-based regression function de<sup>fi</sup>ned as

$$
f (x, \mathbf {z}) = f (x, \alpha , \alpha^ {*}) = \sum_ {i = 1} ^ {N} (\alpha_ {i} - \alpha_ {i} ^ {*}) K (x, x _ {i}) + b,\tag{8}
$$

where $\alpha _ { j }$ and $\alpha _ { j } ^ { * }$ are Lagrangian multipliers which satisfy the equality $\alpha _ { j } { \dot { \alpha _ { j } } } ^ { * } = 0 .$

Any function that meets Mercer's condition can be adopted as the kernel function. The candidates include polynomial kernel and radial basis function (RBF) kernel [8]. Among many choices, the RBF kernel is one of the most widely applied kernel function in SVR [11,41,42] and is de<sup>fi</sup>ned as $\begin{array} { r } { K ( x _ { i } , x _ { j } ) = \exp \biggl ( \frac { - \vert \vert x _ { i } - x _ { j } \vert \vert ^ { 2 } } { 2 \sigma ^ { 2 } } \biggr ) } \end{array}$ , where σ denotes the width of the RBF. According to Cherkassky and Ma [11], SVR has the best performance in most forecasting programs when the value of σ is set between 0.1 and 0.5. In this paper, we use the RBF as kernel function and set $\sigma { = } 0 . 2$

As indicated in Eq. (7), SVR model is also affected by the values of parameters C and ε. In literature, there are no general rules for the choice of C and ε. In this research, we adopt the method of grid search proposed by Lin et al. [25] in which exponentially growing sequences of C (for example, $\dot { \mathsf { C } } = \dot { 2 } ^ { - 1 5 } , 2 ^ { - 3 } , 2 ^ { - 1 } , . . . . , 2 ^ { 1 5 } \dot { ) }$ and ε are used to determine the best parameter set of C and ε which can generate the minimum forecasting mean square error.

## 3. Research scheme and model interpretation

## 3.1. Research scheme

The proposed Wavelet-MAR-SVR approach is illustrated in Fig. 2. After data preprocessing, we use wavelet transform to decompose the data into separate sub-series. Then, these sub-series were used as input variables in MARS to perform the variable selection using generalized cross-validation (GCV). Finally, the selected sub-series were integrated into the SVR approach to construct a forecasting model. The detailed illustration of each step in the research scheme is provided as follows:

## Step 1 Data Preprocessing

The daily closing stock prices collected are ordered by time and the non-stationarity of the stock price data is removed by taking Log (Return) of the stock price as shown in Eq. (9):

$$
\operatorname{Log} (\text { Return }) _ {t} = \operatorname{Log} \left(\frac {x _ {t}}{x _ {t - 1}}\right)\tag{9}
$$

where t is today's closing price and t–1 is yesterday's closing price.

## Step 2 Wavelet transform

Wavelet transform is employed to decompose the preprocessed stock price data into wavelet sub-series. Because DB1 (a.k.a. Haar), DB2, DB3 and DB4 of the Daubechies wavelet basis functions are the ones most often applied in the previous studies [9,18,38,49,50], we have used DB1–DB4 as the wavelet basis functions for the wavelet transformation when executing wavelet transform. Regarding the coef<sup>fi</sup>cients of DB1 to DB4, we simply adopted the values (shown in Table 1) proposed by Daubechies [14]. Basically, these coef<sup>fi</sup>cients are derived by reversing the order of the scaling function (low-pass <sup>fi</sup>lter) coef<sup>fi</sup>cients and then reversing the sign of every second one [11,29]. In addition, the maximum stage to apply the wavelet transform depends on how many data points are contained in a data set. According to the literature [43], for the decomposition of any data, it is suf<sup>fi</sup>cient to decompose and obtain all kinds of hidden information when the stage to apply the wavelet transform equals 6. Therefore, in this study, we will take 6 stages as the basis of decomposition. Under the settings of 6 decomposition stages and DB1–DB4 as the wavelet basis functions, we will generate 48 sub-series.

![](/api/attachments/H8HVSPG5/fulltext/images/d29cfd7202c8874f5f31a658e07170d4a58433b008f465abd74d9c97ff2b5c6c.jpg)  
Fig. 2. The proposed Wavelet-MAR-SVR approach

## Step 3 Variable selection by MARS

To identify signi<sup>fi</sup>cant sub-series as our input variables, the MARS approach was utilized herein. In MARS, the variable selection is conducted by calculating generalized cross-validation (GVC) in Eq. (4). As shown in the equation, N calculates observation number; $\sum _ { i = 1 } ^ { N } { [ y _ { i } - f _ { M } ( x _ { i } ) ] } ^ { 2 }$ calculates lack-of-<sup>fi</sup>t of the sum of squared residuals $f _ { M } ( x _ { i } )$ of BF in M number which is found for data set; $\left[ 1 - \frac { C ( M ) } { M } \right] ^ { 2 }$ is the penalty term to apply to M number of BF. The penalty term is applied for reducing the number of BFs, which tend to increase in the model and for restricting the ideal model number. Finally, the ideal MARS model is represented by an equation estimated by the lowest GCV obtained

from Eq. (4). The 48 sub-series decomposed by Wavelet transformation are used as input variables in MARS. And an MARS input variable which has the level of signi<sup>fi</sup>cance greater than 5% is considered as input variable to SVR approach in this study. Forecasting Model Built by SVR

Finally, we build the forecasting model by regarding the significant wavelet sub-series identi<sup>fi</sup>ed by MARS as input variables in SVR. As previously mentioned, we will adopt the grid search as the parameter setting method when carrying out the construction of the forecasting model by SVR.

## 3.2. Model interpretation

Because the analytical result of wavelet transform would vary with varying selections of basis function and varying stages of decomposition, in this study, we speci<sup>fi</sup>cally de<sup>fi</sup>ne the basis functions employed and the stages as the following: DBiDj denotes the detailed sub-series for the $\mathrm { j } ^ { \mathrm { t h } }$ decomposition stage after having carried out the transformation using the DBi basis function; DBiAj denotes the approximated sub-series for the $\mathrm { j } ^ { \mathrm { t h } }$ decomposition stage after having carried out the transformation using the DBi basis function. Next, we use Fig.3 as an example to explain how to determine the signi<sup>fi</sup>cance of each sub-series generated under different basis function and stages.

In Fig. 3, we take 10, 6 and 12 to represent the Log(Return) value of time at t−1, t−2 and t−3 respectively and plan to conduct the wavelet transform at time t using the basis function DB1. Based on the high-pass and low-pass <sup>fi</sup>lter coef<sup>fi</sup>cients for the DB1 basis function as shown in Table 1, we are able to obtain the DB1D1 sub-series. 2.828 and —4.243 respectively. and the DB1A1 sub-series 11.314 and 12.728 respectively. In other words, DB1D1 and DB1A1, respectively, are the resulting detailed sub-series and approximated sub-series generated based on the previous two sessions' Log(Return) values. Similarly, we are able to obtain DB1D2 and DB1A2 sub-series as 0.9998 (=0.7071\*[0.7071\*LR +0.7071\*LR ] 0.7071\*[0.7071\* LR +0.7071\*LR ]) and 17.0001 (=0.7071\*[0.7071\*LR + 0.7071\*LR ]+0.7071\*[0.7071\*LR +0.7071\*LR ]) respectively with the values representing the detailed sub-series and the approximated sub-series generated based on the Log(Return) values for the previous three sessions. In a wavelet transform, the approximation coef<sup>fi</sup>cients can be viewed as the weighted moving average, and the details coef<sup>fi</sup>cients can be taken as representing the degrees of data volatility, i.e. the moving difference. Therefore, if, by the MARS method, DB1A2 was selected as a signi<sup>fi</sup>cant variable, this indicates that the weighted moving average of the previous three sessions exerts an in<sup>fl</sup>uence over the model's forecasting with the effect of the (t 2) session being the most signi<sup>fi</sup>cant.

Decomposition <sup>fi</sup>lter coef<sup>fi</sup>cients of DB1 to DB4.

<table><tr><td>Basis function</td><td colspan="8">Decomposition low-pass filter coefficients (approximation)</td></tr><tr><td>DB1</td><td>0.7071</td><td>0.7071</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>DB2</td><td>-0.1294</td><td>0.2241</td><td>0.8365</td><td>0.483</td><td></td><td></td><td></td><td></td></tr><tr><td>DB3</td><td>0.0352</td><td>-0.0854</td><td>-0.135</td><td>0.4599</td><td>0.8069</td><td>0.3327</td><td></td><td></td></tr><tr><td>DB4</td><td>-0.0106</td><td>0.0329</td><td>0.0308</td><td>-0.187</td><td>-0.028</td><td>0.6309</td><td>0.7148</td><td>0.2304</td></tr><tr><td>Basis function</td><td colspan="8">Decomposition high-pass filter coefficients (detail)</td></tr><tr><td>DB1</td><td>-0.7071</td><td>0.7071</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>DB2</td><td>-0.4830</td><td>0.8365</td><td>-0.2241</td><td>-0.1294</td><td></td><td></td><td></td><td></td></tr><tr><td>DB3</td><td>-0.3327</td><td>0.8069</td><td>-0.4599</td><td>-0.1350</td><td>0.0854</td><td>0.0352</td><td></td><td></td></tr><tr><td>DB4</td><td>-0.2304</td><td>0.7148</td><td>-0.6309</td><td>-0.0280</td><td>0.1870</td><td>0.0308</td><td>-0.0329</td><td>-0.0106</td></tr></table>

Table 3  
Table 2  
![](/api/attachments/H8HVSPG5/fulltext/images/3c152639246fb986f84929c719ae8c943dc41514704b2c4de4b59e4c92878921.jpg)  
Fig. 3. The illustration of weight computation.

Aside from the signi<sup>fi</sup>cance of DB1D1, DB1A1, DB1D2 and DB1A2, we also sort out the impact of DBiDj and DBiAj sub-series (i=1–4, j=1–6) on the forecast result. Respectively, Tables 2 and 3 list the weights of DB1A1 to DB1A4 and the weights of DB1D1 to DB1D4. The weights of

DB2Aj, DB2Dj, DB3Aj, DB3Dj, DB4Aj and DB4Dj, are summarized in the Appendix A. The weights of DB2, DB3 and DB4 are respectively shown in Figs. A1, A2 and A3. From Tables 2 and 3, we discovered that, for DB1A2, DB1A3, DB1A4, DB1A5 and DB1A6 sub-series, the sessions more in<sup>fl</sup>uential on the forecast result are (t−2), (t−2 and t−3), (t−3), (t−3 and t−4) and (t−5) respectively and that, for DB1D2, DB1D3, DB1D4, DB1D5 and DB1D6 sub-series, (t 1 and t 3), (t 1 to t 4), (t−2 and t−4), (t−2 and t−5) and (t−3 and t−5) are the sessions exerting greater in<sup>fl</sup>uences on the forecast result. Moreover, on the more in<sup>fl</sup>uential sessions for the rest of the sub-series that affect the forecast result, one can refer to the sessions that the higher line in the <sup>fi</sup>gure of the Appendix A corresponds to.

The weight table of DB1A1 to DB1A4.

<table><tr><td rowspan="2">Time</td><td colspan="6">Stages</td></tr><tr><td>DB1A1</td><td>DB1A2</td><td>DB1A3</td><td>DB1A4</td><td>DB1A5</td><td>DB1A6</td></tr><tr><td>t-7</td><td></td><td></td><td></td><td></td><td></td><td>0.1250</td></tr><tr><td>t-6</td><td></td><td></td><td></td><td></td><td>0.1768</td><td>0.7500</td></tr><tr><td>t-5</td><td></td><td></td><td></td><td>0.2500</td><td>0.8838</td><td>1.8749</td></tr><tr><td>t-4</td><td></td><td></td><td>0.3535</td><td>1.0000</td><td>1.7677</td><td>2.4999</td></tr><tr><td>t-3</td><td></td><td>0.4999</td><td>1.0606</td><td>1.4999</td><td>1.7677</td><td>1.8749</td></tr><tr><td>t-2</td><td>0.7071</td><td>0.9998</td><td>1.0606</td><td>1.0000</td><td>0.8838</td><td>0.7500</td></tr><tr><td>t-1</td><td>0.7071</td><td>0.4999</td><td>0.3535</td><td>0.2500</td><td>0.1768</td><td>0.1250</td></tr></table>

## 4. Empirical study

## 4.1. Datasets and performance criteria

To evaluate the performance of the proposed Wavelet-MARS-SVR forecasting model, two emerging daily stock market indexes (SSE Composite index of China (called SSEC) and Bovespa index of Brazil) and two mature daily stock market indexes (Dow Jones index of US (called DJ) and Nikkei 225 index of Japan (called N225)) are used herein. All of the data collected in this study are cash closing indexes.

The weight table of DB1D1 to DB1D4.

<table><tr><td rowspan="2">Time</td><td colspan="6">Stages</td></tr><tr><td>DB1D1</td><td>DB1D2</td><td>DB1D3</td><td>DB1D4</td><td>DB1D5</td><td>DB1D6</td></tr><tr><td>t-7</td><td></td><td></td><td></td><td></td><td></td><td>-0.1250</td></tr><tr><td>t-6</td><td></td><td></td><td></td><td></td><td>-0.1768</td><td>-0.5000</td></tr><tr><td>t-5</td><td></td><td></td><td></td><td>-0.2500</td><td>-0.5303</td><td>-0.6250</td></tr><tr><td>t-4</td><td></td><td></td><td>-0.3535</td><td>-0.5000</td><td>-0.3535</td><td>0.0000</td></tr><tr><td>t-3</td><td></td><td>-0.5000</td><td>-0.3535</td><td>0.0000</td><td>0.3535</td><td>0.6250</td></tr><tr><td>t-2</td><td>-0.7071</td><td>0.0000</td><td>0.3535</td><td>0.5000</td><td>0.5303</td><td>0.5000</td></tr><tr><td>t-1</td><td>0.7071</td><td>0.5000</td><td>0.3535</td><td>0.2500</td><td>0.1768</td><td>0.1250</td></tr></table>

![](/api/attachments/H8HVSPG5/fulltext/images/50cf4a938b02eb830920d2a3cc8c4024921fcfe38ad7f330775654719c4d9bae.jpg)  
Fig. 4. The daily SSEC closing indexes from 2006/4/18 to 2010/4/1

The time period for each closing index is summarized and shown in Figs. 4–7. There are a total of 1000 data points for each dataset. The <sup>fi</sup>rst 800 data points (80% of the total sample points) are used as the training sample while the remaining 200 data points (20% of the total sample points) are used as the testing sample.

The forecasting results of the proposed model are compared to integrated wavelet and SVR model without using MARS (called Wavelet-SVR model), integrated wavelet and MARS model without using SVR (called Wavelet-MARS model), single ARIMA, single SVR and single ANFIS models. The forecasting performance is evaluated using the following performance measures: the root mean square error (RMSE), mean absolute difference (MAD), mean absolute percentage error (MAPE), and root mean square percentage error (RMSPE). The de<sup>fi</sup>nitions of these criteria were summarized in Table 4. RMSE, MAD, MAPE and RMSPE are measures of the deviation between actual and predicted values. The smaller the deviation, the better the accuracy.

## 4.2. SSEC index

For Wavelet-SVR model, <sup>fi</sup>rst, the preprocessed data was passed to the wavelet transform model for decomposition. Since the study adopts four basis functions, DB1–DB4, and sets the number of decomposition stages to 6, 48 sub-series are generated following the decomposition process. All these 48 sub-series are directly used as input variables in Wavelet-SVR model. The grid search method is used for searching the best parameter set for Wavelet-SVR model. The testing results of Wavelet-SVR model with combinations of different parameter sets are summarized in Table 5. Table 5 shows that the parameter set $( \mathsf C = 2 ^ { - 1 5 } , \ \mathsf { \varepsilon } = 2 ^ { - 5 } )$ gives the best forecasting result (minimum testing MSE) and is the best parameter set for Wavelet-SVR model in forecasting SSEC index.

For Wavelet-MARS model, the 48 sub-series decomposed by wavelet transform are used as input variables. Table 6 summarizes the obtained signi<sup>fi</sup>cant variables and their relative importance. Among the 48 sub-series, 7 signi<sup>fi</sup>cant sub-series are selected by MARS, being DB4A1, DB4A4, DB2A4, DB4D1, DB1D3, DB3A1 and DB2A5, respectively. We <sup>fi</sup>nd that DB4A1 (approximate function of closing prices for the previous 8 sessions) is the most important percentage in the table, followed by DB4A4 (approximate function for the previous 30 sessions). This <sup>fi</sup>nding suggests that, as it is in a newly emerging market, the stock prices of the SSEC Index are still quite volatile, and therefore, moving averages over longer periods of time is necessary for making forecasting of trends in stock prices.

For the proposed Wavelet-MARS-SVR model, seven important subseries (DB4A1, DB4A4, DB2A4, DB4D1, DB1D3, DB3A1 and DB2A5) identi<sup>fi</sup>ed by MARS are used as input variables in SVR approach. The testing results of Wavelet-MARS-SVR model with combinations of different parameter sets are summarized in Table 7. It can be observed from Table 7 that the parameter set $( \mathsf C = 2 ^ { - 1 3 } , \varepsilon = 2 ^ { - 5 } )$ gives the best forecasting result and hence is the best parameter setup for the proposed Wavelet-MARS-SVR model.

For developing single SVR model, the closing indices of the previous 1 day (t−1), 2 days (t−2) and 3 days (t−3) are directly used as input variables. Table 8 summarizes the model selection results of the single SVR model. As shown in the table, the parameter set $( \mathsf C = 2 ^ { - 1 1 } , \mathsf E =$ 2<sup>−7</sup>) is the best parameter setup for the single SVR model.

The ANFIS toolbox of MATLAB software (MATLAB software, R2012 version, The MathWorks Inc.) is used to analyze the data with the single ANFIS model in this study. The input variables of the single

![](/api/attachments/H8HVSPG5/fulltext/images/4975cd697a5c6d2e4b2a958f5f5ed1d2a74dd0890e15c0c02b19dc931fadb404.jpg)  
Fig. 5. The daily Bovespa closing indexes from 2006/3/14 to 2010/4/1.

![](/api/attachments/H8HVSPG5/fulltext/images/ea5293af494f2f3df34bd6643f8a68269766eb294cbd303c2d23bc130ff96106.jpg)  
Fig. 6. The daily DJ closing indexes from 2006/4/12 to 2010/4/1.

![](/api/attachments/H8HVSPG5/fulltext/images/c3ecfb0e176ade7fda971ebf8ead7ea1e21239dacaa44959eccce4ca1ac719b1.jpg)  
Fig. 7. The daily N225 closing indexes from 2006/3/3 to 2010/4/1.

ANFIS model are the same as the inputs of the single SVR model. The default settings of the ANFIS toolbox are used for forecasting SSEC index.

For single ARIMA model, the data not decomposed by wavelet transform are directly used as input variables. The SPSS statistical package (SPSS software, PC version 12; SPSS Inc.) is used to build ARIMA model in this study. The estimated results are summarized in Table 9.

The SSEC index forecasting results using Wavelet-MARS-SVR, Wavelet-SVR, Wavelet-MARS, single ARIMA, single SVR and single ANFIS models are computed and listed in Table 10. Table 10 depicts that RMSE, MAD, MAPE and RMSPE of the proposed Wavelet-MARS-SVR model are 52.92204, 39.01709, 1.255% and 1.7116%, respectively. It can be observed that these values are smaller than those of the <sup>fi</sup>ve comparison models. It indicates that there is a smaller deviation between the actual and predicted values when the proposed model is applied. Thus, the proposed Wavelet-MARS-SVR model provides a better forecasting result than Wavelet-SVR, Wavelet-MARS, single ARIMA, single SVR and single ANFIS models in terms of forecasting error for SSEC index.

Table 4  
Performance measures and their de<sup>fi</sup>nitions.

<table><tr><td>Metrics</td><td>Calculation*</td></tr><tr><td>RMSE</td><td> $RMSE = \sqrt{\frac{\sum_{i=1}^{n} (T_i - P_i)^2}{n}}$ </td></tr><tr><td>MAD</td><td> $MAD = \frac{\sum_{i=1}^{n} |T_i - P_i|}{n}$ </td></tr><tr><td>MAPE</td><td> $MAPE = \frac{\sum_{i=1}^{n} \left| \frac{T_i - P_i}{T_i} \right|}{N}$ </td></tr><tr><td>RMSPE</td><td> $RMSPE = \sqrt{\frac{\sum_{i=1}^{n} \left( \frac{T_i - P_i}{T_i} \right)^2}{n}}$ </td></tr></table>

⁎ Note that T and P represent the actual and predicted value, respectively, n is total number of data points.

## 4.3. Bovespa, Dow Jones, and Nikkei 225 Stock Indexes

The stock index forecasting for DJ, N225 and Bovespa is conducted using similar modeling process illustrated in Section 4.2. Respectively, Tables 11–13 show the results of MARS-based variable selection for Bovespa, Dow Jones and Nikkei 225.

## Table 5

The model selection results of Wavelet-SVR model-SSEC.

<table><tr><td>C</td><td> $\varepsilon$ </td><td>Training MSE</td><td>Testing MSE</td></tr><tr><td rowspan="5"> $2^{-15}$ </td><td> $2^{-9}$ </td><td>0.0003046</td><td>0.0005085</td></tr><tr><td> $2^{-7}$ </td><td>0.0003029</td><td>0.0005064</td></tr><tr><td> $2^{-5}$ </td><td>0.0003010</td><td>0.0005052</td></tr><tr><td> $2^{-3}$ </td><td>0.0003105</td><td>0.0005164</td></tr><tr><td> $2^{-1}$ </td><td>0.0003175</td><td>0.0005245</td></tr><tr><td rowspan="5"> $2^{-13}$ </td><td> $2^{-9}$ </td><td>0.0003046</td><td>0.0005081</td></tr><tr><td> $2^{-7}$ </td><td>0.0003029</td><td>0.0005064</td></tr><tr><td> $2^{-5}$ </td><td>0.0003039</td><td>0.0005055</td></tr><tr><td> $2^{-3}$ </td><td>0.0003105</td><td>0.0005163</td></tr><tr><td> $2^{-1}$ </td><td>0.0003175</td><td>0.0005245</td></tr><tr><td rowspan="5"> $2^{-11}$ </td><td> $2^{-9}$ </td><td>0.0003046</td><td>0.0005084</td></tr><tr><td> $2^{-7}$ </td><td>0.0003029</td><td>0.0005063</td></tr><tr><td> $2^{-5}$ </td><td>0.0003010</td><td>0.0005052</td></tr><tr><td> $2^{-3}$ </td><td>0.0003105</td><td>0.0005167</td></tr><tr><td> $2^{-1}$ </td><td>0.0003175</td><td>0.0005246</td></tr></table>

Table 6  
Results of MARS-based variable selection – SSEC.

<table><tr><td>Variables</td><td>Connotation of variable</td><td>Std. dev</td><td>GCV value</td><td>Importance (%)</td></tr><tr><td>DB4A1</td><td>Weighted average of closing prices of previous 8 sessions</td><td>0.000485</td><td>0.003</td><td>100.00</td></tr><tr><td>DB4A4</td><td>Weighted average of closing prices of previous 30 sessions</td><td>0.000483</td><td>0.003</td><td>87.97</td></tr><tr><td>DB2A4</td><td>Weighted average of closing prices of previous 7 sessions</td><td>0.000483</td><td>0.003</td><td>80.59</td></tr><tr><td>DB4D1</td><td>Weighted deviation of closing prices of previous 8 sessions</td><td>0.000487</td><td>0.003</td><td>72.06</td></tr><tr><td>DB1D3</td><td>Weighted deviation of closing prices of previous 5 sessions</td><td>0.000484</td><td>0.003</td><td>67.36</td></tr><tr><td>DB3A1</td><td>Weighted average of closing prices of previous 6 sessions</td><td>0.000479</td><td>0.002</td><td>45.90</td></tr><tr><td>DB2A5</td><td>Weighted deviation of closing prices of previous 26 sessions</td><td>0.000480</td><td>0.002</td><td>29.46</td></tr></table>

Table 7  
The model selection results of the proposed Wavelet-MARS-SVR model-SSEC.

<table><tr><td>C</td><td>ε</td><td>Training MSE</td><td>Testing MSE</td></tr><tr><td rowspan="5"> $2^{-13}$ </td><td> $2^{-9}$ </td><td>0.0003047</td><td>0.0005061</td></tr><tr><td> $2^{-7}$ </td><td>0.0003029</td><td>0.0005047</td></tr><tr><td> $2^{-5}$ </td><td>0.0003005</td><td>0.0005037</td></tr><tr><td> $2^{-3}$ </td><td>0.0003090</td><td>0.0005347</td></tr><tr><td> $2^{-1}$ </td><td>0.0003246</td><td>0.0005222</td></tr><tr><td rowspan="5"> $2^{-11}$ </td><td> $2^{-9}$ </td><td>0.0003047</td><td>0.0005061</td></tr><tr><td> $2^{-7}$ </td><td>0.0003029</td><td>0.0005047</td></tr><tr><td> $2^{-5}$ </td><td>0.0003011</td><td>0.0005038</td></tr><tr><td> $2^{-3}$ </td><td>0.0003090</td><td>0.0005147</td></tr><tr><td> $2^{-1}$ </td><td>0.0003246</td><td>0.0005222</td></tr><tr><td rowspan="5"> $2^{-9}$ </td><td> $2^{-9}$ </td><td>0.0003047</td><td>0.0005061</td></tr><tr><td> $2^{-7}$ </td><td>0.0003029</td><td>0.0005047</td></tr><tr><td> $2^{-5}$ </td><td>0.0003011</td><td>0.0005039</td></tr><tr><td> $2^{-3}$ </td><td>0.0003090</td><td>0.0005147</td></tr><tr><td> $2^{-1}$ </td><td>0.0003246</td><td>0.0005322</td></tr></table>

From Table 11, it can be seen that six MARS-selected signi<sup>fi</sup>cant sub-series (DB1A6, DB2D2, DB1D1, DB4D2, DB4A4, DB1D4) have been identi<sup>fi</sup>ed for the Brazil. Among them, DB1A6 (weighted average function of closing prices of previous 6 sessions) exhibits the highest degree of importance, followed by DB2D2 (deviation function of closing functions of previous 9 sessions). Moreover, since the majority of signi<sup>fi</sup>cant sub-series shown in Table 11 are deviation functions, we can infer that, as a result of the Brazil market's higher degree of volatility, stock price deviations would need to be considered in order to make effective predictions on trends in stock prices.

Table 8  
The model selection results of the single SVR model-SSEC

<table><tr><td>C</td><td>ε</td><td>Training MSE</td><td>Testing MSE</td></tr><tr><td rowspan="5"> $2^{-13}$ </td><td> $2^{-9}$ </td><td>0.0003691</td><td>0.0005780</td></tr><tr><td> $2^{-7}$ </td><td>0.0003706</td><td>0.0005768</td></tr><tr><td> $2^{-5}$ </td><td>0.0003788</td><td>0.0005811</td></tr><tr><td> $2^{-3}$ </td><td>0.0003602</td><td>0.0005302</td></tr><tr><td> $2^{-1}$ </td><td>0.0003944</td><td>0.0005923</td></tr><tr><td rowspan="5"> $2^{-11}$ </td><td> $2^{-9}$ </td><td>0.0003519</td><td>0.0005448</td></tr><tr><td> $2^{-7}$ </td><td>0.0003203</td><td>0.0005189</td></tr><tr><td> $2^{-5}$ </td><td>0.0003993</td><td>0.0005708</td></tr><tr><td> $2^{-3}$ </td><td>0.0003305</td><td>0.0005328</td></tr><tr><td> $2^{-1}$ </td><td>0.0004103</td><td>0.0005479</td></tr><tr><td rowspan="5"> $2^{-9}$ </td><td> $2^{-9}$ </td><td>0.0003427</td><td>0.0005201</td></tr><tr><td> $2^{-7}$ </td><td>0.0003618</td><td>0.0005230</td></tr><tr><td> $2^{-5}$ </td><td>0.0004460</td><td>0.0005802</td></tr><tr><td> $2^{-3}$ </td><td>0.0004780</td><td>0.0005998</td></tr><tr><td> $2^{-1}$ </td><td>0.0005248</td><td>0.0006115</td></tr></table>

Table 9  
Single ARIMA model-SSEC.

<table><tr><td>Parameter</td><td>Estimate</td><td>Standard error</td><td>T-value</td><td>Approx Pr&gt;|t|</td><td>Lag</td></tr><tr><td>MU</td><td>-5.50E-06</td><td>4.96E-06</td><td>-1.11</td><td>0.2678</td><td>0</td></tr><tr><td>MA1,1</td><td>1.01136</td><td>0.03539</td><td>28.58</td><td>&lt;.0001</td><td>1</td></tr><tr><td>MA1,2</td><td>-0.0063</td><td>0.05035</td><td>-0.13</td><td>0.9005</td><td>2</td></tr><tr><td>MA1,3</td><td>-0.0668</td><td>0.05029</td><td>-1.33</td><td>0.1845</td><td>3</td></tr><tr><td>MA1,4</td><td>-0.05112</td><td>0.05038</td><td>-1.01</td><td>0.3105</td><td>4</td></tr><tr><td>MA1,5</td><td>0.11286</td><td>0.03538</td><td>3.19</td><td>0.0015</td><td>5</td></tr><tr><td colspan="6">Model parameter</td></tr><tr><td>Constant estimate</td><td>-0.0000055</td><td></td><td></td><td></td><td></td></tr><tr><td>Variance estimate</td><td>0.000502</td><td></td><td></td><td></td><td></td></tr><tr><td>Std error estimate</td><td>0.02241</td><td></td><td></td><td></td><td></td></tr><tr><td>AIC</td><td>-3796.13</td><td></td><td></td><td></td><td></td></tr><tr><td>SBC</td><td>-3768.03</td><td></td><td></td><td></td><td></td></tr><tr><td>Number of residuals</td><td>799</td><td></td><td></td><td></td><td></td></tr></table>

Table 10  
Summary of forecast results by six models on SSEC closing prices.

<table><tr><td>Models</td><td>RMSE</td><td>MAD</td><td>MAPE</td><td>RMSPE</td></tr><tr><td>Wavelet -SVR</td><td>52.93402</td><td>39.05813</td><td>1.268%</td><td>1.7218%</td></tr><tr><td>Wavelet -MARS</td><td>54.98807</td><td>40.37382</td><td>1.310%</td><td>1.7965%</td></tr><tr><td>Wavelet-MARS-SVR</td><td>52.92204</td><td>39.01709</td><td>1.255%</td><td>1.7116%</td></tr><tr><td>Single ARIMA</td><td>54.90912</td><td>40.17590</td><td>1.331%</td><td>1.7357%</td></tr><tr><td>Single SVR</td><td>53.95342</td><td>39.87542</td><td>1.291%</td><td>1.7294%</td></tr><tr><td>Single ANFIS</td><td>54.21242</td><td>39.91241</td><td>1.293%</td><td>1.7307%</td></tr></table>

Table 11  
Results of MARS-based variable selection – BVSP.

<table><tr><td>Variables</td><td>Connotation of variable</td><td>Std. dev</td><td>GCV value</td><td>Importance (%)</td></tr><tr><td>DB1A6</td><td>Weight average function of closing prices of previous 6 sessions</td><td>0.005</td><td>0.000527</td><td>100.00</td></tr><tr><td>DB2D2</td><td>Deviation function of closing prices of previous 9 sessions</td><td>0.005</td><td>0.000524</td><td>87.97</td></tr><tr><td>DB1D1</td><td>Deviation function of closing prices of previous 2 sessions</td><td>0.005</td><td>0.000524</td><td>80.59</td></tr><tr><td>DB4D2</td><td>Deviation function of closing prices of previous 15 sessions</td><td>0.004</td><td>0.000516</td><td>72.06</td></tr><tr><td>DB4A4</td><td>Weighted average function of closing prices of previous 29 sessions</td><td>0.003</td><td>0.000514</td><td>67.36</td></tr><tr><td>DB1D4</td><td>Deviation function of closing prices of previous 5 sessions</td><td>0.003</td><td>0.000512</td><td>45.90</td></tr></table>

Table 12  
Results of MARS-based variable selection – Dow Jones.

<table><tr><td>Variables</td><td>Connotation of variable</td><td>Std. dev</td><td>GCV value</td><td>Importance (%)</td></tr><tr><td>DB3D5</td><td>Weighted average function of closing prices of previous 26 sessions</td><td>0.004</td><td>0.000256</td><td>100.00</td></tr><tr><td>DB1A1</td><td>Weighted average function of closing prices of previous 2 sessions</td><td>0.003</td><td>0.000255</td><td>97.92</td></tr><tr><td>DB2A2</td><td>Weighted average function of closing prices of previous 7 sessions</td><td>0.003</td><td>0.000254</td><td>89.60</td></tr><tr><td>DB3D4</td><td>Deviation function of closing prices of previous 21 sessions</td><td>0.003</td><td>0.000253</td><td>86.26</td></tr><tr><td>DB2D3</td><td>Deviation function of closing prices of previous 13 sessions</td><td>0.003</td><td>0.000252</td><td>76.77</td></tr><tr><td>DB4D1</td><td>Deviation function of closing prices of previous 8 sessions</td><td>0.002</td><td>0.000250</td><td>60.71</td></tr><tr><td>DB2A4</td><td>Weighted average function of closing prices of previous 13 sessions</td><td>0.002</td><td>0.000249</td><td>52.10</td></tr><tr><td>DB1A5</td><td>Deviation function of closing prices of previous 6 sessions</td><td>0.002</td><td>0.000249</td><td>48.57</td></tr></table>

Table 13  
Results of MARS-based variable selection – Nikkei 225.

<table><tr><td>Variables</td><td>Connotation of variable</td><td>Std. dev</td><td>GCV value</td><td>Importance (%)</td></tr><tr><td>DB2A1</td><td>Weighted average function of closing prices of previous 4 sessions</td><td>0.007</td><td>0.000364</td><td>100.00</td></tr><tr><td>DB4D1</td><td>Deviation function of closing prices of previous 8 sessions</td><td>0.005</td><td>0.000351</td><td>77.33</td></tr><tr><td>DB3A2</td><td>Weighted average function of closing prices of previous 11 sessions</td><td>0.004</td><td>0.000345</td><td>63.15</td></tr><tr><td>DB4A1</td><td>Weighted average function of closing prices of previous 8 sessions</td><td>0.004</td><td>0.000344</td><td>61.56</td></tr><tr><td>DB2D4</td><td>Deviation function of closing prices of previous 17 sessions</td><td>0.004</td><td>0.000341</td><td>52.84</td></tr><tr><td>DB3D5</td><td>Deviation function of closing prices of previous 26 sessions</td><td>0.003</td><td>0.000338</td><td>43.16</td></tr><tr><td>DB3D6</td><td>Deviation function of closing prices of previous 31 sessions</td><td>0.002</td><td>0.000336</td><td>35.15</td></tr><tr><td>DB1A4</td><td>Weighted average function of closing prices of previous 5 sessions</td><td>0.005</td><td>0.000333</td><td>17.30</td></tr></table>

Table 14  
Summary of forecast results by six models on BVSP, DJ and N225 closing prices.

<table><tr><td>Stock indexes</td><td>Models</td><td>RMSE</td><td>MAD</td><td>MAPE</td><td>RMSPE</td></tr><tr><td rowspan="6">BVSP</td><td>Wavelet-SVR</td><td>878.7561</td><td>642.7191</td><td>1.044%</td><td>1.430%</td></tr><tr><td>Wavelet-MARS</td><td>881.0468</td><td>651.4920</td><td>1.055%</td><td>1.437%</td></tr><tr><td>Wavelet-MARS-SVR</td><td>876.9092</td><td>641.1467</td><td>1.043%</td><td>1.428%</td></tr><tr><td>Single ARIMA</td><td>883.9282</td><td>652.8783</td><td>1.072%</td><td>1.439%</td></tr><tr><td>Single SVR</td><td>880.0151</td><td>649.6584</td><td>1.053%</td><td>1.436%</td></tr><tr><td>Single ANFIS</td><td>882.0765</td><td>651.6157</td><td>1.057%</td><td>1.437%</td></tr><tr><td rowspan="6">DJ</td><td>Wavelet-SVR</td><td>32.2070</td><td>24.6752</td><td>0.742%</td><td>0.983%</td></tr><tr><td>Wavelet-MARS</td><td>33.0173</td><td>25.4042</td><td>0.762%</td><td>1.010%</td></tr><tr><td>Wavelet-MARS-SVR</td><td>32.2058</td><td>24.6743</td><td>0.741%</td><td>0.983%</td></tr><tr><td>Single ARIMA</td><td>33.6321</td><td>25.3284</td><td>0.753%</td><td>1.053%</td></tr><tr><td>Single SVR</td><td>32.9112</td><td>24.9462</td><td>0.748%</td><td>0.997%</td></tr><tr><td>Single ANFIS</td><td>33.2513</td><td>25.2615</td><td>0.751%</td><td>1.021%</td></tr><tr><td rowspan="6">N225</td><td>Wavelet-SVR</td><td>133.2766</td><td>104.8005</td><td>1.014%</td><td>1.321%</td></tr><tr><td>Wavelet-MARS</td><td>138.8247</td><td>110.5228</td><td>1.093%</td><td>1.381%</td></tr><tr><td>Wavelet-MARS-SVR</td><td>132.3721</td><td>103.4128</td><td>1.012%</td><td>1.303%</td></tr><tr><td>Single ARIMA</td><td>140.3164</td><td>111.2556</td><td>1.130%</td><td>1.380%</td></tr><tr><td>Single SVR</td><td>137.6541</td><td>109.3261</td><td>1.081%</td><td>1.368%</td></tr><tr><td>Single ANFIS</td><td>135.5629</td><td>107.6568</td><td>1.066%</td><td>1.352%</td></tr></table>

With respect to the Dow Jones data, the MARS-selected signi<sup>fi</sup>cant sub-series are summarized in Table 12. As shown in the table, there are eight signi<sup>fi</sup>cant sub-series (DB3D5, DB1A1, DB2A2, DB3D4, DB2D3, DB4D1, DB2A4 and DB1A5) that have been selected. DB3D5 (weighted average function of closing prices of previous 26 sessions) is the most important one, followed by DB1A1 (weighted average function of closing prices of previous 2 sessions). Furthermore, most of these signi<sup>fi</sup>cant sub-series are weighted average functions, indicating the smaller volatility of the U.S. market and the higher reference value of its weighted average information.

Table 13 summarizes the signi<sup>fi</sup>cant sub-series selected by MARS for the Nikkei 225 stock index. As shown in the table, these eight selected, signi<sup>fi</sup>cant sub-series are DB2A1, DB4D1, DB3A2, DB4A1, DB2D4, DB3D5, DB3D6 and DB1A4. Among them, the most important sub-series is DB2A1 (weighted average function of closing prices of previous 4 sessions), and the next most important one is DB4D1 (deviation function of closing prices of previous 8 sessions). Since most sub-series in Table 13 exhibiting higher signi<sup>fi</sup>cance are weighted average functions, we therefore infer and predict that the Japanese stock market is a more stable market and that, for forecasting stock prices, weighted averages can provide more information.

Table 14 summarizes Dow Jones, Nikkei 225, and Bovespa stock index forecasting results using Wavelet-MARS-SVR, Wavelet-SVR, Wavelet-MARS, single ARIMA, single SVR and single ANFIS models, respectively. It can be observed that the proposed Wavelet-MARS-SVR model has the smallest RMSE, MAD, MAPE and RMSPE in comparison with the <sup>fi</sup>ve competing models in every stock market index. (Wavelet-MARS-SVR model only slightly better than Wavelet-SVR model in forecasting error, but the model construction time for Wavelet-MARS-SVR is 2/3 shorter than Wavelet-SVR's.) Thus, the proposed Wavelet-MARS-SVR can produce lower forecasting errors and outperforms the <sup>fi</sup>ve competing models in forecasting SSEC, Bovespa, DJ and N225 stock indexes.

## 4.4. Robustness evaluation

To evaluate the robustness of the proposed method, the performance of the Wavelet-MARS-SVR, Wavelet-SVR, Wavelet-MARS, single ARIMA, single SVR and single ANFIS models was tested using different ratios of training and testing sample sizes. The testing experiment is based on the relative ratio of the size of the training dataset size to complete dataset size. In this section, four relative ratios, 60%, 70%, 80%, and 90% are considered. The forecasting results for the four indexes by the six methods are summarized in Table 15 in terms of RMSE, MAD, MAPE and RMSPE. In Table 15, it can be observed that the proposed Wavelet-MARS-SVR method outperforms the other benchmarking tools under all four different ratios in terms of the four different performance measures. It therefore indicates that Wavelet-MARS-SVR approach indeed provides better forecast accuracy than the other <sup>fi</sup>ve approaches.

Table 15  
Robustness evaluation.

<table><tr><td>Relative ratio</td><td>Models</td><td>China (SSEC) Testing MAPE</td><td>Brazil (BVSP) Testing MAPE</td><td>USA (DJ) Testing MAPE</td><td>Japan (N225) Testing MAPE</td></tr><tr><td rowspan="6">60%</td><td>Wavelet-SVR</td><td>1.561%</td><td>1.892%</td><td>1.493%</td><td>1.673%</td></tr><tr><td>Wavelet -MARS</td><td>1.701%</td><td>1.951%</td><td>2.021%</td><td>2.030%</td></tr><tr><td>Wavelet -MARS-SVR</td><td>1.521%</td><td>1.800%</td><td>1.421%</td><td>1.611%</td></tr><tr><td>Single ARIMA</td><td>1.712%</td><td>2.312%</td><td>1.950%</td><td>1.801%</td></tr><tr><td>Single SVR</td><td>1.673%</td><td>1.940%</td><td>1.711%</td><td>1.778%</td></tr><tr><td>Single ANFIS</td><td>1.698%</td><td>1.951%</td><td>1.721%</td><td>1.769%</td></tr><tr><td rowspan="6">70%</td><td>Wavelet-SVR</td><td>1.321%</td><td>1.279%</td><td>1.051%</td><td>1.242%</td></tr><tr><td>Wavelet -MARS</td><td>1.412%</td><td>1.343%</td><td>1.182%</td><td>1.291%</td></tr><tr><td>Wavelet -MARS-SVR</td><td>1.302%</td><td>1.235%</td><td>1.019%</td><td>1.203%</td></tr><tr><td>Single ARIMA</td><td>1.510%</td><td>1.752%</td><td>1.184%</td><td>1.261%</td></tr><tr><td>Single SVR</td><td>1.351%</td><td>1.302%</td><td>1.094%</td><td>1.257%</td></tr><tr><td>Single ANFIS</td><td>1.355%</td><td>1.331%</td><td>1.096%</td><td>1.255%</td></tr><tr><td rowspan="6">80%</td><td>Wavelet-SVR</td><td>1.268%</td><td>1.044%</td><td>0.742%</td><td>1.014%</td></tr><tr><td>Wavelet -MARS</td><td>1.310%</td><td>1.055%</td><td>0.762%</td><td>1.093%</td></tr><tr><td>Wavelet -MARS-SVR</td><td>1.255%</td><td>1.043%</td><td>0.741%</td><td>1.012%</td></tr><tr><td>Single ARIMA</td><td>1.331%</td><td>1.072%</td><td>0.753%</td><td>1.130%</td></tr><tr><td>Single SVR</td><td>1.291%</td><td>1.053%</td><td>0.748%</td><td>1.081%</td></tr><tr><td>Single ANFIS</td><td>1.293%</td><td>1.057%</td><td>0.751%</td><td>1.066%</td></tr><tr><td rowspan="6">90%</td><td>Wavelet-SVR</td><td>1.021%</td><td>0.918%</td><td>0.606%</td><td>0.940%</td></tr><tr><td>Wavelet -MARS</td><td>1.032%</td><td>0.948%</td><td>0.632%</td><td>1.232%</td></tr><tr><td>Wavelet -MARS-SVR</td><td>1.002%</td><td>0.891%</td><td>0.581%</td><td>0.902%</td></tr><tr><td>Single ARIMA</td><td>1.032%</td><td>0.962%</td><td>0.623%</td><td>1.122%</td></tr><tr><td>Single SVR</td><td>1.029%</td><td>0.945%</td><td>0.615%</td><td>0.985%</td></tr><tr><td>Single ANFIS</td><td>1.029%</td><td>0.946%</td><td>0.619%</td><td>0.977%</td></tr></table>

## 4.5. Significance test

In order to test whether the proposed Wavelet-MAR-SVR model is superior to Wavelet-SVR, Wavelet-MARS, single ARIMA, single SVR and single ANFIS models in <sup>fi</sup>nancial stock index forecasting, the Wilcoxon signed-rank test is applied. The Wilcoxon signed-rank test is a distribution-free, non-parametric technique which determines whether two models are different by comparing the signs and ranks of prediction values. The Wilcoxon signed-rank test is one of the most popular tests in evaluating the predictive capabilities of two different models [15,34,40]. For the details of the Wilcoxon signedrank test, please refer to Diebold and Mariano [15] and Pollock et al. [34].

We employ the test to evaluate the predictive performance of the proposed method and the <sup>fi</sup>ve competing models under different ratios of the size of the training data set to the complete data set. Tables 16 and 17 present the Z statistic values of the two-tailed Wilcoxon signed-rank test for RMSE values between the proposed Wavelet-MARS-SVR model and other <sup>fi</sup>ve competing models in four stock markets. It can be observed from Tables 16 and 17, under different ratios, that the RMSE values of the proposed Wavelet-MARS-SVR model are signi<sup>fi</sup>cantly different from Wavelet-MARS, single ARIMA, single SVR and single ANFIS models. We can therefore conclude that the proposed Wavelet-MARS-SVR model is signi<sup>fi</sup>cantly better than Wavelet-MARS, single ARIMA, single SVR and single ANFIS models in <sup>fi</sup>nancial stock index forecasting.

Even though the RMSE values of the proposed model has no signi<sup>fi</sup>cant difference from Wavelet-SVR, the proposed Wavelet-MARS-SVR model uses less variables to achieve the same forecast accuracy of Wavelet-SVR, which implies that Wavelet-MARS-SVR model is more ef<sup>fi</sup>cient in model construction, and its explanation to the predictor variables provides a solid foundation in ef<sup>fi</sup>cient decision-making.

## 4.6. Investigation of variables in the various markets

The historical sessions are screened from data of different markets. To further illustrate how the MARS selected signi<sup>fi</sup>cant sub-series can be used to explain the in<sup>fl</sup>uence of different sessions on each stock indexes, we sort out the resulting MARS-selected signi<sup>fi</sup>cant sub-series generated from four different training and testing data ratios and summarize the results in Table 18. From the table, we <sup>fi</sup>nd that the DB4D1 sub-series (weighted deviation of previous 8 sessions) appeared more than twice in SSEC, DJ and N225 stock indices and that DB4D2 (weighted deviation of previous 15 sessions) showed up three times in the Bovespa stock index (Figs. A1 and A2). Such results indicate that the degree of volatility in the previous eight sessions has a signi<sup>fi</sup>cant in<sup>fl</sup>uence over the forecasting of the stock market. In addition, based on the weight of coef<sup>fi</sup>cient of DB4D1 as shown in Fig. A3, we are also able to infer further that, for SSEC, DJ and N225 stock indices, the closing price of the (t 7) session has a greater signi<sup>fi</sup>cance on the index forecast than all the ones in the other eight sessions, whereas for the Bovespa stock index, the impact of the closing prices of previous 15 sessions on the index forecast is more signi<sup>fi</sup>cant with the importance of information revealed, with (t−7) and (t−9) sessions being higher than the other 13 sessions. Furthermore, of the selected signi<sup>fi</sup>cant sub-series, the DB4 basis function is the most frequent, which also veri<sup>fi</sup>es indirectly the conclusion made in the literature [1,30].

Wilcoxon signed-rank test between Wavelet-MAR-SVR model, Wavelet-SVR, Wavelet-MARS, single ARIMA, single SVR and single ANFIS models by different relative ratios -SSEC and BVSP. Table 16

<table><tr><td rowspan="2">Models</td><td rowspan="2">Relative ratio</td><td colspan="2">Wavelet-SVR</td><td colspan="2">Wavelet-MARS</td><td colspan="2">Single ARIMA</td><td colspan="2">Single SVR</td><td colspan="2">Single ANFIS</td></tr><tr><td>SSEC</td><td>BVSP</td><td>SSEC</td><td>BVSP</td><td>SSEC</td><td>BVSP</td><td>SSEC</td><td>BVSP</td><td>SSEC</td><td>BVSP</td></tr><tr><td rowspan="4">Wavelet-MAR-SVR</td><td>60%</td><td>-1.091 (.275)</td><td>-1.33 (.183)</td><td>-2.936 **(.003)</td><td>-1.644 *(.096)</td><td>-4.061 **(.000)</td><td>-7.06 **(.000)</td><td>-1.936 **(.041)</td><td>-1.571 *(.099)</td><td>-2.612 **(.010)</td><td>-1.642 *(.096)</td></tr><tr><td>70%</td><td>-0.162 (.871)</td><td>-.817 (.414)</td><td>-2.408 **(.016)</td><td>-1.736 *(.083)</td><td>-4.849 **(.000)</td><td>-5.659 **(.000)</td><td>-1.708 *(.076)</td><td>-1.412 *(.097)</td><td>-1.751 *(.073)</td><td>-1.993 **(.039)</td></tr><tr><td>80%</td><td>-0.89 (.374)</td><td>-.558 (.577)</td><td>-1.223 **(.021)</td><td>-1.752 *(.080)</td><td>-1.206 **(.022)</td><td>-1.956 **(.000)</td><td>-1.011 *(.082)</td><td>-1.731 *(.084)</td><td>-1.063 *(.068)</td><td>-1.912 **(.007)</td></tr><tr><td>90%</td><td>-1.375 (.169)</td><td>-.602 (.547)</td><td>-7.028 **(.000)</td><td>-1.485 *(.093)</td><td>-4.70 **(.000)</td><td>-8.661 **(.050)</td><td>-4.912 **(.000)</td><td>-1.406 *(.096)</td><td>-4.915 **(.000)</td><td>-1.405 *(.096)</td></tr></table>

Note: The numbers in parentheses are the corresponding p-value; \*: pb0.1; \*\*: pb0.05.

Wilcoxon signed-rank test between the six models by different relative ratios-DJ and N225. Table 17

<table><tr><td rowspan="2">Models</td><td rowspan="2">Relative ratio</td><td colspan="2">Wavelet-SVR</td><td colspan="2">Wavelet-MARS</td><td colspan="2">Single ARIMA</td><td colspan="2">Single SVR</td><td colspan="2">Single ANFIS</td></tr><tr><td>DJ</td><td>N225</td><td>DJ</td><td>N225</td><td>DJ</td><td>N225</td><td>DJ</td><td>N225</td><td>DJ</td><td>N225</td></tr><tr><td rowspan="4">Wavelet-MAR-SVR</td><td>60%</td><td>-.960 (.337)</td><td>-.407 (.684)</td><td>-4.378 **(.000)</td><td>-4.153 **(.000)</td><td>-3.899 **(.000)</td><td>-1.836 **(.000)</td><td>-1.861 **(.000)</td><td>-1.719 **(.000)</td><td>-1.903 **(.000)</td><td>-1.516 **(.002)</td></tr><tr><td>70%</td><td>-.876 (.381)</td><td>-.583 (.560)</td><td>-3.832 **(.000)</td><td>-3.870 **(.000)</td><td>-4.561 **(.000)</td><td>-5.572 **(.000)</td><td>-2.091 **(.000)</td><td>-4.097 **(.000)</td><td>-2.103 **(.000)</td><td>-3.921 **(.000)</td></tr><tr><td>80%</td><td>-.350 (.726)</td><td>-.985 (.325)</td><td>-1.807 *(.071)</td><td>-2.578 **(.010)</td><td>-2.263 **(.000)</td><td>-2.365 **(.018)</td><td>-1.587 *(.088)</td><td>-2.162 **(.031)</td><td>-1.867 *(.057)</td><td>-1.932 *(.054)</td></tr><tr><td>90%</td><td>-1.489 (.137)</td><td>-1.76 *(.086)</td><td>-3.452 **(.001)</td><td>-3.37 **(.001)</td><td>-1.987 **(.047)</td><td>-2.094 **(.036)</td><td>-1.637 *(.077)</td><td>-1.968 *(.057)</td><td>-1.712 *(.062)</td><td>-1.912 *(.061)</td></tr><tr><td colspan="12">Note: The numbers in parentheses are the corresponding p-value; *: p&lt;0.1; **: p&lt;0.05.</td></tr></table>

Summary of signi<sup>fi</sup>cant variables selected by the proposed method under different training ratios for the various markets.

<table><tr><td colspan="2">SSEC</td><td colspan="2">BVSP</td><td colspan="2">DJ</td><td colspan="2">N225</td></tr><tr><td>Sub-series</td><td>Freq.</td><td>Sub-series</td><td>Freq.</td><td>Sub-series</td><td>Freq.</td><td>Sub-series</td><td>Freq.</td></tr><tr><td>DB2A4</td><td>4</td><td>DB1A6</td><td>3</td><td>DB2D3</td><td>3</td><td>DB4D1</td><td>3</td></tr><tr><td>DB4A4</td><td>4</td><td>DB1D1</td><td>3</td><td>DB3D4</td><td>3</td><td>DB1A4</td><td>2</td></tr><tr><td>DB4D1</td><td>4</td><td>DB4D2</td><td>3</td><td>DB1A5</td><td>2</td><td>DB2A1</td><td>2</td></tr><tr><td>DB4A1</td><td>3</td><td>DB1D4</td><td>1</td><td>DB2A2</td><td>2</td><td>DB3A2</td><td>2</td></tr><tr><td>DB1D3</td><td>2</td><td>DB2D1</td><td>1</td><td>DB3A6</td><td>2</td><td>DB3D5</td><td>1</td></tr><tr><td>DB2A5</td><td>2</td><td>DB2D3</td><td>1</td><td>DB3D5</td><td>2</td><td>DB1A1</td><td>1</td></tr><tr><td>DB3A1</td><td>2</td><td>DB3D1</td><td>1</td><td>DB4D1</td><td>2</td><td>DB1A2</td><td>1</td></tr><tr><td>DB1D5</td><td>1</td><td>DB3D3</td><td>1</td><td>DB1A1</td><td>1</td><td>DB1A4</td><td>1</td></tr><tr><td>DB2A1</td><td>1</td><td>DB3D4</td><td>1</td><td>DB1A5</td><td>1</td><td>DB1A5</td><td>1</td></tr><tr><td>DB2A3</td><td>1</td><td>DB4A2</td><td>1</td><td>DB1A6</td><td>1</td><td>DB1D2</td><td>1</td></tr><tr><td>DB3A2</td><td>1</td><td>DB4A4</td><td>1</td><td>DB1D3</td><td>1</td><td>DB1D3</td><td>1</td></tr><tr><td>DB3A5</td><td>1</td><td></td><td></td><td>DB2A3</td><td>1</td><td>DB1D6</td><td>1</td></tr><tr><td></td><td></td><td></td><td></td><td>DB2A4</td><td>1</td><td>DB2D3</td><td>1</td></tr><tr><td></td><td></td><td></td><td></td><td>DB2A6</td><td>1</td><td>DB2D4</td><td>1</td></tr><tr><td></td><td></td><td></td><td></td><td>DB2D5</td><td>1</td><td>DB2D5</td><td>1</td></tr><tr><td></td><td></td><td></td><td></td><td>DB3D2</td><td>1</td><td>DB3A5</td><td>1</td></tr><tr><td></td><td></td><td></td><td></td><td>DB4A3</td><td>1</td><td>DB3D2</td><td>1</td></tr><tr><td></td><td></td><td></td><td></td><td>DB4A4</td><td>1</td><td>DB4A1</td><td>1</td></tr><tr><td></td><td></td><td></td><td></td><td>DB4D3</td><td>1</td><td>DB4D2</td><td>1</td></tr><tr><td></td><td></td><td></td><td></td><td>DB4D5</td><td>1</td><td>DB4D4</td><td>1</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>DB3D6</td><td>1</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>DB3D6</td><td>1</td></tr></table>

## 5. Concluding remarks

This paper proposed a three-stage forecasting model by integrating wavelet transform, MARS and SVR for <sup>fi</sup>nancial time series. The proposed Wavelet-MARS-SVR method <sup>fi</sup>rst uses Wavelet transform to decompose the <sup>fi</sup>nancial time series data. Then, the decomposed sub-series are used as input variables in MARS for variable selection. Finally, the identi<sup>fi</sup>ed sub-series containing the key factors that affect forecasting accuracy are applied in SVR as the new input variables to build up a forecasting model.

Four datasets including SSEC index of China, Bovespa index of Brazil, Dow Jones index of US and Nikkei 225 index of Japan are used to evaluate the proposed method. Moreover, this study compares the proposed method with Wavelet-SVR, Wavelet-MARS, single ARIMA, single SVR and single ANFIS models using forecasting error as a criterion. The empirical results show that the proposed model can produce lower forecasting error and outperform other <sup>fi</sup>ve competing models. Moreover, the model construction time for Wavelet-MARS-SVR is 2/3 shorter than Wavelet-SVR's. According to the results, it can be concluded that the proposed method can effectively select the important wavelet sub-series and improve the forecasting performance of SVR. Moreover, through the proposed approach, the data of which sessions among past stock market prices exerted signi<sup>fi</sup>cant impacts on the construction of the forecasting model can be successfully identi<sup>fi</sup>ed. Future research can aim at combining other forecasting tools, like neural networks and grey system theory, in evaluating the ability of the proposed forecasting scheme.

## Acknowledgements

This work is partially supported by the Chien Hsin University of Science and Technology (formerly Ching Yun University), Grant No. 99-IE-002-CM. The authors also gratefully acknowledge the helpful comments and suggestions of the reviewers, which have improved the presentation.

<table><tr><td>i=1</td><td></td><td></td></tr><tr><td>i=2</td><td></td><td></td></tr><tr><td>i=3</td><td></td><td></td></tr><tr><td>i=4</td><td></td><td></td></tr><tr><td>i=5</td><td></td><td></td></tr><tr><td>i=6</td><td></td><td></td></tr><tr><td></td><td>DB2Di</td><td>DB2Ai</td></tr><tr><td>i=6</td><td></td><td></td></tr><tr><td></td><td>DB3Di</td><td>DB3Ai</td></tr><tr><td>i=6</td><td></td><td></td></tr><tr><td></td><td>DB4Di</td><td>DB4Ai</td></tr></table>

Fig. A1. The weights of each period of DB2.

Fig. A2. The weights of each period of DB3.

Fig. A3. The weights of each period of DB4.

## References

[1] D.P. Ahalpara, A. Verma, J.C. Parikh, P.K. Panigrahi, Characterizing and modelling cyclic behaviour in non-stationary time series through multi-resolution analysis Pramana 71 (3) (2008) 459–485.

[2] V. Alarcon-Aquino, J.A. Barria, Multiresolution FIR neural-network-based learning algorithm applied to network traf<sup>fi</sup>c prediction, IEEE Transactions on Systems, Man, and Cybernetics, Part C: Applications and Reviews 36 (2) (2006) 80–92.

[3] A. Andalib, F. Atry, Multi-step ahead forecasts for electricity prices using NARX: a new approach, a critical analysis of one-step ahead forecasts, Energy Conversion and Management 50 (3) (2009) 739–747.

[4] G.S. Atsalakis, K.P. Valavanis, Surveying stock market forecasting techniques – Part II: Soft computing methods, Expert Systems with Applications 36 (3) (2009) 5932–5941.

[5] G.S. Atsalakis, K.P. Valavanis, Forecasting stock market short-term trends using a neuro-fuzzy based methodology, Expert Systems with Applications 36 (7) (2009) 10696–10707.

[6] A. Bahrammirzaee, A comparative survey of arti<sup>fi</sup>cial intelligence applications in <sup>fi</sup>nance: arti<sup>fi</sup>cial neural networks, expert system and hybrid intelligent systems Neural Computing & Applications 19 (8) (2010) 1165–1195.

[7] V. Bjorn, Multiresolution methods for <sup>fi</sup>nancial time series prediction, in: Proceedings of the 1995 IEEE/IAFE on Computational Intelligence for Financial Engineering, New York, 1995, p. 97.

[8] M.A. Boyacioglu, D. Avci, An adaptive network-based fuzzy inference system (ANFIS) for the prediction of stock market return: the case of the Istanbul stock exchange, Expert Systems with Applications 37 (12) (2010) 7908–7912.

[9] P.C. Chang, C.Y. Fan, A hybrid system integrating a wavelet and TSK fuzzy rules for stock price forecasting, IEEE Transactions on Systems, Man, and Cybernetics—Part C: Applications and Reviews 38 (6) (2008) 802–815

[10] J.R. Chang, L.Y. Wei, C.H. Cheng, A hybrid ANFIS model based on AR and volatility for TAIEX forecasting, Applied Soft Computing Journal 11 (1) (2011) 1388–1395.

[11] V. Cherkassky, Y. Ma, Practical selection of SVM parameters and noise estimation for SVM regression, Neural Networks 17 (2004) 113–126.

[12] T.M. Choi, Y. Yu, K.F. Au, A hybrid SARIMA wavelet transform method for sales forecasting, Decision Support Systems 51 (1) (2011) 130–140.

[13] W. Dai, C.J. Lu, Financial time series forecasting using a compound model based on wavelet frame and support vector regression, in: Proceedings of 2008 Fourth International Conference on Natural Computation, Jinan, China, 2008, pp. 328–332.

[14] I. Daubechies, Ten Lectures on Wavelets, Society for Industrial and Applied Mathematics, Pennsylvania, USA, 1992.

[15] F.X. Diebold, R.S. Mariano, Comparing predictive accuracy, Journal of Business and Economic Statistics 13 (1995) 253–263.

[16] J.H. Friedman, Multivariate adaptive regression splines (with discussion), The Annals of Statistics 19 (1991) 1–141.

[17] R. Gençay, F. Selçuk, B. Whitcher, An Introduction to Wavelets and Other Filtering Methods in Finance and Economics, Academic Press, London, 2002.

[18] Z. Gonghui, J.L. Starck, J. Campbell, F. Murtagh, The wavelet transform for <sup>fi</sup>ltering <sup>fi</sup>nancial data streams, Journal of Computational Intelligence in Finance 12 (1999) 18–35.

[19] J.W. Hall, Adaptive selection of U.S. stocks with neural nets, in: G.J. Deboeck (Ed.), Trading on the Edge: Neural, Genetic and Fuzzy Systems for Chaotic Financial Markets, Willey, New York, 1994, pp. 45–65.

[20] S.C. Huang, T.K. Wu, Combining wavelet-based feature extractions with relevance vector machines for stock index forecasting, Expert Systems 25 (2) (2008) 133–149.

[21] J.S. Jang, ANFIS: Adaptive-Network-based Fuzzy Inference Systems, IEEE Transactions on Systems, Man, and Cybernetics 23 (3) (1993) 665–685.

[22] L. Khansa, D. Liginlal, Predicting stock market returns from malicious attacks: a comparative analysis of vector autoregression and time-delayed neural networks, Decision Support Systems 51 (4) (2011) 745–759.

[23] P.A.W. Lewis, J.G. Stevens, Nonlinear modeling of time series using multivariate adaptive regression splines (MARS), Journal of the American Statistical Association 86 (2009) 864–877.

[24] L. Li, Q. Li, S. Zhu, M. Ogihara, A survey on wavelet applications in data mining, SIGKDD Explorations 4 (2) (2003) 49–68.

[25] C.J. Lin, C.W. Hsu, C.C. Chang, A practical guide to support vector classi<sup>fi</sup>cation, Technical Report, Department of Computer Science and Information Engineering National Taiwan University, Taipei, 2003.

[26] C.J. Lu, T.S. Lee, C.C. Chiu, Financial time series forecasting using independent component analysis and support vector regression, Decision Support Systems 47 (2) (2009) 115–125.

[27] C.J. Lu, T.S. Lee, C.M. Lian, Sales forecasting for computer wholesalers: a comparison of multivariate adaptive regression splines and arti<sup>fi</sup>cial neural networks, Decision Support Systems (2012), http://dx.doi.org/10.1016/j.dss.2012.08.006.

[28] S.G. Mallat, A theory for multiresolution signal decomposition: the wavelet representation, IEEE Transactions on Pattern Analysis and Machine Intelligence 11 (7) (1989) 674–693.

[29] M. Misiti, Y. Misiti, G. Oppenheim, J.M. Poggi, MATLAB Wavelet Toolbox User's Guide The MathWorks Inc, Massachusetts USA. 1996

[30] A. Ozun, A. Cifter, Modeling long-term memory effect in stock prices. A comparative analysis with GPH test and Daubechies wavelets, Studies in Economics and Finance 25 (1) (2008).38-48

[31] P.F. Pai, C.S. Lin, A hybrid ARIMA and support vector machines model in stock price forecasting, Omega 33 (2005) 497–505.

[32] Z. Pan, X. Wang, A stochastic nonlinear regression estimator using wavelets, Computational Economics 11 (1998) 89–102.

[33] D.B. Percival, A.T. Walden, Wavelet Methods for Time Series Analysis, Cambridge University Press, Cambridge, UK, 2000.

[34] A.C. Pollock, A. Macaulay, M.E. Thomson, D. Önkal, Performance evaluation of judgmental directional exchange rate predictions, International Journal of Forecasting 21 (3) (2005) 473–489.

[35] J.B. Ramsey, Wavelets in economics and <sup>fi</sup>nance: past and future, Studies in Nonlinear Dynamics & Econometrics 6 (2002) 1–27.

[36] R.M. Rao, A.S. Bopardikar, Wavelet Transforms: Introduction to Theory and Applications, Addison Wesley, Boston, 1998.

[37] Y. Shahriar, W. Ilona, R. Dominik, Wavelet-based prediction of oil prices, Chaos, Solitons and Fractals 25 (2005) 265–275.

[38] T. Shin, I. Han, Optimal signal multi-resolution by genetic algorithms to support arti<sup>fi</sup>cial neural networks for exchange-rate forecasting. Optimal signal multiresolution by genetic algorithms to support arti<sup>fi</sup>cial neural networks for exchange-rate forecasting, Expert Systems with Applications 18 (2002) 257–269.

[39] J.L. Starck, F. Murtagh, A. Bijaoui, Image and Data Analysis: The Multiscale Approach, Cambridge University Press, Cambridge, UK, 1998.

[40] N.R. Swanson, H. White, Forecasting economic time series using <sup>fl</sup>exible versus <sup>fi</sup>xed speci<sup>fi</sup>cation and linear versus nonlinear econometric models, International Journal of Forecasting 13 (1997) 437–461.

[41] F.E.H. Tay, L.J. Cao, Application of support vector machines in <sup>fi</sup>nancial time series forecasting, Omega 29 (2001) 309–317.

[42] F.E.H. Tay, L.J. Cao, Support vector machine with adaptive parameters in <sup>fi</sup>nancial time series forecasting, IEEE Transactions on Neural Networks 14 (2003) 1506–1518.

[43] D.M. Tsai, C.H. Chiang, Automatic band selection for wavelet reconstruction in the application of defect detection, Image and Vision Computing 21 (2003) 413–431.

[44] C.F. Tsai, Y.C. Hsiao, Combining multiple feature selection methods for stock prediction: union, intersection, and multi-intersection approaches, Decision Support Systems 50 (1) (2010) 258–269.

[45] M. Unser, Texture classi<sup>fi</sup>cation and segmentation using wavelet frames, IEEE Transactions on Image Processing 4 (11) (1995) 1549–1560

[46] V.N. Vapnik, The Nature of Statistical Learning Theory, Springer, New York, 2000.

[47] W. Xiao, Q. Zhao, Q. Fei, A comparative study of data mining methods in consumer loans credit scoring management, Journal of Systems Science and Systems Engineering 15 (4) (2006) 419–435.

[48] S.A.M. Yaser, A.F. Atiya, Introduction to <sup>fi</sup>nancial forecasting, Applied Intelligence 6 (1996) 205–213.

[49] S. Youse<sup>fi</sup>, I. Weinreich, D. Reinarz, Wavelet-based prediction of oil prices, Chaos, Solitons and Fractals 25 (2) (2005) 265–275.

[50] B.L. Zhang, R. Coggins, M.A. Jabri, D. Dersch, B. Flower, Multiresolution forecasting for futures trading using wavelet decompositions, IEEE Transactions on Neural Networks 12 (2001) 765–775.

[51] Y. Zhao, Y. Zhang, C. Qi, Prediction Model of Stock Market Returns Based on Wavelet Neural Network, in: Proceedings of 2008 Paci<sup>fi</sup>c-Asia Workshop on Computational Intelligence and Industrial Application, Wuhan, China, 2008, pp. 31-36.

[52] Y. Zhou, H. Leung, Predicting object-oriented software maintainability using multivariate adaptive regression splines, Journal of Systems and Software 80 (8) (2007)1349-1361.

![](/api/attachments/H8HVSPG5/fulltext/images/8b566045371a988018bc956f1437ebdd1e4b359c0d5c87ef3904ea43e26b5dca.jpg)  
Ling-Jing Kao is an assistant professor in the Department of Business Management at National Taipei University of Technology, Taiwan. Her Ph.D. is from The Ohio State University in Marketing. Her research and teaching interests are in the area of application of Bayesian statistical approach and Quantitative Marketing Research. She has published articles in various journals, including Journal of the Operational Research Society, European Journal of Operational Research, and Expert System with Applications.

![](/api/attachments/H8HVSPG5/fulltext/images/d3283e80bd4d4391f8e0c77ad4c17098cd447dd0b344c3b879049b96466fc7cd.jpg)

Chih-Chou Chiu is a professor in the Department of Business Management at National Taipei University of Tech nology. His Ph.D. is from Texas A&M University in Industrial Engineering. His research and teaching interests are in the area of application of arti<sup>fi</sup>cial intelligence, Bayesian statistical approach, data mining and continuous process improvement techniques for manufacturing. He has published articles in various journals, including IIE Transactions, International Journal of Production Research, Journal of Intelligent Manufacturing, International Journal of System Science, and Quality and Reliability Engineering International

![](/api/attachments/H8HVSPG5/fulltext/images/e2a41a4d74e8046916223008aa982f701d39b5ae2a0bf05fa583cb8447064b53.jpg)

Chi-Jie Lu is an associate professor in the Department of Industrial Management at Chien Hsin University of Science and Technology, Taiwan. He got his Ph.D. in Industria Engineering and Management from Yuan-Ze University Taiwan, in 2005. His research and teaching interests are in the area of data mining, time series forecasting, statistical process control, and machine vision and inspection. He has published articles in various journals, including Pattern Recognition, Decision Support Systems, Neurocomputing, Image and Vision Computing, International Journal of Production Economics, International Journal of Production Research and Computational Statistics and Data Analysis.

![](/api/attachments/H8HVSPG5/fulltext/images/d186f6f413210069233816d6ab0aea0b325a01bdc04c196c035a639f51dec283.jpg)  
Chih-Hsiang Chang received his master degree from Institute of Commerce Automation and Management, National Taipei University of Technology, Taiwan, in 2010. His current research interests include machine learning, wavelet transform and stock index forecasting.
