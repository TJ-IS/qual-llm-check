---
otero_id: 9530
otero_key: "JQFDPDWM"
title: "A note comparing support vector machines and ordered choice models’ predictions of international banks’ ratings"
authors: "Tony Bellotti; Roman Matousek; Chris Stewart"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.03.008"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A note comparing support vector machines and ordered choice models’ predictions of international banks’ ratings

Tony Bellotti <sup>a</sup>, Roman Matousek <sup>b,</sup>⁎, Chris Stewart <sup>c,1</sup>

<sup>a</sup> Department of Mathematics, Imperial College London, South Kensington Campus, London SW7 2AZ, United Kingdom

<sup>b</sup> Centre for EMEA Banking, Finance and Economics, London Metropolitan Business School, London Metropolitan University, 84 Moorgate, London, EC2M 6SQ, United Kingdom

<sup>c</sup> London Metropolitan Business School, London Metropolitan University, 84 Moorgate, London, EC2M 6SQ, United Kingdom

## a r t i c l e i n f o

Article history: Received 26 March 2010 Received in revised form 20 March 2011 Accepted 27 March 2011 Available online 1 April 2011

Keywords: International bank ratings Support vector machines Ordered choice models

## a b s t r a c t

We <sup>fi</sup>nd that support vector machines can produce notably better predictions of international bank ratings than the standard method currently used for this purpose, ordered choice models. This appears due to the support vector machine's ability to estimate a large number of country dummies unrestrictedly, which was not possible with the ordered choice models due to the low sample size.

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

Ratings of sovereign risk, corporate bonds and <sup>fi</sup>nancial institutions conducted by rating agencies (RAs) may be seen as instruments that provide investors with prima facie information about the <sup>fi</sup>nancial position of the subject in question and on the price of credit risk. Pinto [34] argues that RAs’ opinions facilitate capital allocation through supplied information about the <sup>fi</sup>nancial position of the companies in question. Indeed, the RAs exclusive position may be justi<sup>fi</sup>ed because they reduce asymmetric information between investors and companies but also they play an active monitoring function (Bannierand et al. [7]).

Ratings are ordinal measures that should not only re<sup>fl</sup>ect the current <sup>fi</sup>nancial position of sovereign nations, <sup>fi</sup>rms, banks, etc. but also provide information about their future <sup>fi</sup>nancial positions. There has been extensive research in predicting bond ratings using multivariate discriminant analysis, ordered choice models, non-parametric techniques and combined methods’ forecasts to predict bond ratings or default prediction — see, Altman and Saunders [2], Kamstra et al. [27], Kim [28], Van Gestel et al. [37], Ravi Kumar and Ravi [35], Kim and Sohn [29], Hájek [19] and Chen et al. [11] among others. We employ <sup>fi</sup>nancial variables, in addition to country speci<sup>fi</sup>c dummy variables (to capture, for example, country risk), as determinants of bank ratings in our modelling. The main challenge in modelling ratings is to increase the probability of correct classi<sup>fi</sup>cations. Therefore, our comparison of support vector machines (SVM) for regression with ordered choice models for predicting individual bank ratings as produced by Fitch Ratings (FR) is a signi<sup>fi</sup>cant contribution to current research in this <sup>fi</sup>eld. In doing so, we model the bank ratings assigned by FR using both ordered choice models and SVMs with the aim of shedding light upon their determination and comparing the two modelling methodologies.<sup>2</sup> SVM has been applied successfully in several other areas of <sup>fi</sup>nance such as prediction of credit ratings (Huang et al. [23]), small business default prediction (Kim and Sohn [29]), building consumer credit scorecards (Baesens et al. [6], Bellotti and Crook [8]) and it has been proposed for volatility forecasting (Gavrishchaka and Banerjee [16]).

The next section provides a brief literature review, Section 3 describes the data and methods applied while Section 4 discusses the principal empirical <sup>fi</sup>ndings. The last section concludes.

## 2. Literature review — a brief overview

The current empirical research can be divided into two strands. The <sup>fi</sup>rst one is represented by studies that search and try to identify the reliability of ratings assignments. The second strand is focused on empirical research that investigates prediction models for bondratings.

The ability of RAs to assign ratings that provide a true picture about the credit risk of a bank (corporate, sovereign) has been extensively questioned. One of frequent arguments against the ratings reliability is that there is no explicit guarantee that RAs can assess credit risk better than banks themselves. Indeed, all RAs, for example, failed to predict the Asian crisis in the late 1990. Altman and Saunders [3] argued that RAs could provide misleading information since assignments are backward looking rather than forward looking. Another argument against external ratings is the opaque methodologies used by RAs for assessing sovereign and/or corporate risk. Credit ratings are supposed to be assigned on a “through-the-cycle” basis, and not according to transitory <sup>fl</sup>uctuations in credit quality. Amato and Fur<sup>fi</sup>ne [4] analysed changes of credit ratings assignment over business cycles to test the hypothesis about procyclical behaviour of RAs.

Furthermore, RAs do not have, and cannot have, superior information to market participants about uncertainty and the degree of insolvency (illiquidity) of companies. Ammer and Packer [5] tested for inconsistency of RAs across the different sectors. They analysed four sectors — <sup>fi</sup>nancial <sup>fi</sup>rms and non-<sup>fi</sup>nancial <sup>fi</sup>rms in the US and Japan. Their results con<sup>fi</sup>rmed apparent inconsistencies in ratings assignment for US <sup>fi</sup>nancial <sup>fi</sup>rms. In this case, the assigned ratings were higher for non <sup>fi</sup>nancial <sup>fi</sup>rms with similar default risk. Another study that looked at ratings inconsistency was presented by Cantor et al. [9]. They showed that the speculative grade of US banks have higher annual default rates than US non-banks. Morgan [31] attempted to identify the determinants of the difference in two separate RAs’ bank rating assignments using (ordered) logit regressions. Morgan's work is motivated by the inherently opaque nature of banks in terms of those outside of banks, including the RAs, assessing the risks taken by inherently opaque banks. Galil [15] tested the quality of corporate credit rating. The results unambiguously con<sup>fi</sup>rmed that using publicly-available information contributes to better ratings assignments. Nevertheless, ratings provide superior information about default risk than using only public information. Iannotta [24] investigated the opaqueness of banks by analysing the disagreement between rating agencies (split ratings). He concluded that fewer bank issues have split ratings but the probability of a split rating is higher if the model takes into account risk and other issue characteristics. However, he argued that subordinated bonds are subject to more disagreement between rating agencies.

The second major strand of empirical research is focused on ratings prediction models. Ratings are ordinal measures that should not only re<sup>fl</sup>ect the current <sup>fi</sup>nancial position of sovereign nations, <sup>fi</sup>rms, banks, etc. but also provide information about their future <sup>fi</sup>nancial positions. Such studies deal with the applied methodological approaches used for <sup>fi</sup>nancial soundness and bond-rating prediction. Recent empirical studies are represented by two groups of research. The <sup>fi</sup>rst group applies statistical techniques such as ordinary least squares (OLS), multiple discriminant analysis (MDA), ordered linear probit models (OLPM) and ordered linear logit model (OLLM). The second group uses arti<sup>fi</sup>cial intelligent methods, especially machine learning techniques such as neural networks (NN), support vector machines (SVM) and other kernel based techniques.

Empirical research employing statistical models to predict bondratings date back to the 1960s. Horrigan [22] and West [39] used OLS while Pinches and Mingo [32,33] applied MDA to predict bond ratings. Altman and Katz [1], Jackson and Boyd [25] applied logistic regression and the probit model. Kamstra et al. [27] applied ordered logit regression combining methods to predict bond ratings from differing individual forecasts. Their methodology was applied in the transportation and industrial sectors using Moody's bond rating services. Their results showed that the modi<sup>fi</sup>ed Kamstra-Kennedy method is superior to Kamstra and Kennedy [26]. Gentry et al. [17] used an nchotomous multivariate probit model with cash-based funds <sup>fl</sup>ow components and <sup>fi</sup>nancial ratios to predict industrial bond ratings. They argued that the n-chotomous probit model provides superior information for evaluating bond classi<sup>fi</sup>cations. Doumpos and Zopounidis [12] in their recent paper show how the ROMETHEE II method can be used for a multicriteria bank rating approach and its implementation into an integrated decision support system.

Recent studies also investigate the movements of <sup>fi</sup>rms (sovereign) across rating categories — see Fuertes and Kalotychou [14], Feng et al. [13], and Stefanescu et al. [36] amongst others.

Arti<sup>fi</sup>cial Intelligence techniques, particularly neural networks and support vector machines (SVMs), have been employed for prediction. Kim [28] used non-parametric techniques designed to capture the dynamic relationship between input and output variables. Huang et al. [23] and Lee [30] show that arti<sup>fi</sup>cial intelligence methods do not provide superior predictions of bond ratings to standard ordered choice methods. We are not aware of any previous studies that seek to model and predict individual bank ratings using ordered choice models and SVMs, which is the aim of this paper.

## 3. Data and methodology

FR is one of the largest rating companies for the banking industry around the world and releases four types of ratings: legal ratings, long-term and short-term (security) ratings and individual ratings. We focus on individual ratings that assess the <sup>fi</sup>nancial position of a bank itself. As stated by FR the rating is closely linked with <sup>fi</sup>nancial performance (<sup>fi</sup>nancial variables). The individual rating provided by FR is divided into <sup>fi</sup>ve broad categories according to the performances of rated banks and subdivided in to a total of nine categories.

We model international banks’ ratings over the period 2000 and 2007.<sup>3</sup> This variable is ordinal and has up to nine ranked categories that are assigned integer values from 1 to 9 (in brackets) thus, E (1), D/E (2), D (3), C/D (4), C (5), B/C (6), B (7), A/B (8), A (9) — lower values indicate lower ratings. The in-sample period used for estimating models is 2000–2006 (517 observations) while 2007 (112 observations) is our hold-out sample used for producing out-ofsample measures of predictive performance.

We use two methods for predicting bank ratings. The <sup>fi</sup>rst is the ordered choice model that is well known to be appropriate for modelling an ordinal dependent variable (see Greene [18]) and is the standard method for modelling bank ratings. The second is the SVM. SVM is an approach that allows us to use complex non-linear models such as polynomial or Gaussian models ef<sup>fi</sup>ciently using kernels. Unlike standard methods, such as logistic regression, SVM is designed to deal with a large number of covariates (features) since it includes a regularization term to control model complexity whilst <sup>fi</sup>tting the data. Not only is this essential when <sup>fi</sup>tting complex non-linear models but it proves an advantage for the bank rating problem when there are a large number of covariates available such as multiple country dummy variables (codes). See Vapnik [38] for a full discussion of SVM in the context of statistical learning theory.

Since the SVM classi<sup>fi</sup>er is binary it is not immediately suitable for the bank rating problem. Multiple bank ratings can be modelled using multiple SVM classi<sup>fi</sup>ers in a “one-against-one” or directed acyclic graph approach (Huang et al. [23]). However this requires many SVMs, which further increases model complexity and computation time. A simpler method is to use SVM regression to model ratings directly. An advantage that SVM regression has in contrast to classical regression techniques such as OLS is that the loss function is ε- insensitive, meaning that differences between the predicted and true value less than ε are not treated as errors.<sup>4</sup> Since we are interested in predicting integers, predictions are rounded to the nearest integer and so are indifferent to the fractional part of the prediction; for example, if the target rating is 2, then predictions of 2.1 or 2.3 are equally valid. Hence we can set ε≤ 0.5 to represent this indifference. This property allows SVM to be a more sensitive model for bank ratings.

SVM regression is expressed formally as follows. Given n observations $( \mathbf { x } _ { i } , y _ { i } )$ where $x _ { i }$ is a vector of covariates and $y _ { i }$ is a real number outcome, then SVM regression constructs a linear model $\hat { y } = \mathbf { w } \cdot \mathbf { x } + b ,$ where w is a vector of weights on the covariates and b is an intercept, by solving the quadratic optimization problem:

$$
\begin{array}{l} \min _ {\mathbf {w}: \boldsymbol {\xi}: \boldsymbol {\xi} ^ {*}} \left(\frac {1}{2} \mathbf {w} \cdot \mathbf {w} + C \sum_ {i = 1} ^ {n} \xi_ {i} + \xi_ {i} ^ {*}\right) \\ \text { subject   to } \left\{ \begin{array}{r c l} y _ {i} - \mathbf {w} \cdot \mathbf {x} _ {i} - b & \leq & \varepsilon + \xi_ {i} \\ y _ {i} - \mathbf {w} \cdot \mathbf {x} _ {i} - b & \geq & \varepsilon + \xi_ {i} ^ {*}. \\ \xi_ {i}, \xi_ {i} ^ {*} & \geq & 0 \end{array} \right. \end{array}
$$

This minimizes a linear combination of a regularization term that controls the complexity of the model $\left( { \pmb w } \cdot { \pmb w } \right)$ along with model <sup>fi</sup>t on the slack variables $\xi _ { i }$ and $\xi _ { i } ^ { * } .$ . The relative importance of these two optimization goals is controlled by the parameter C.Lower values give greater emphasis to reducing model complexity whilst larger values of C give greater emphasis to model <sup>fi</sup>t. Increasing $C$ should give better model <sup>fi</sup>t on the training set (in-sample) but this will not always be translated into better <sup>fi</sup>t on the test set (out-of-sample) since improvements may be due to over-<sup>fi</sup>tting. The three constraints ensure that each observation $y _ { i }$ is no more than $\varepsilon + \xi _ { i }$ above and no less than $\varepsilon + \xi _ { i } ^ { * }$ below the hyperplane given by the linear model w $\cdot \mathbf { x } _ { i } + b ,$ whilst both $\xi _ { i }$ and $\xi _ { i } ^ { * }$ must be greater than zero. Therefore, essentially, $\xi _ { i }$ and $\xi _ { i } ^ { * }$ represent the error terms. Note that, unlike speci<sup>fi</sup>cations of other statistical models, in SVM notation, ε denotes a <sup>fi</sup>xed constant parameter in the SVM and should not be confused with an error term. This formulation of SVM is a least absolute value regression method with an ε-insensitive loss function:

$$
L (y, \hat {y}) = \left\{ \begin{array}{c l} 0 & \text { if } | y - \hat {y} | \leq \varepsilon \\ | y - \hat {y} | - \varepsilon & \text { otherwise } \end{array} \right..
$$

This means that any difference between the observed and predicted value which is less than ε does not incur a penalty, otherwise the penalty is linear with the difference.

This representation is in primary form, but it can be transformed into dual form using Lagrange multipliers. In dual form non-linear models can be implemented ef<sup>fi</sup>ciently using kernel methods. Typical kernels are polynomial and Gaussian kernels (Vapnik [38]). There are several alternative implementations of SVM. We used the LIBSVM software package, a popular and robust implementation of SVM developed by Chang and Lin [10] at National Taiwan University.

We apply the SVM method to bank ratings data and compare its insample and out-of-sample predictive performance with that of the current standard method for modelling ratings; ordered choice models. Various combinations of ε and C are considered in the SVM application.

We consider three sets of covariates to model bank ratings: (i) <sup>fi</sup>nancial variables, (ii) the year in which the rating was made, [denoted $t i m e _ { i t } ]$ and (iii) 89 country dummy variables (there are banks from 90 countries in total) to account for country-speci<sup>fi</sup>c effects (such as country risk and different legal and regulatory frameworks across countries). The ordered choice models could not be estimated when these 89 country dummy variables were all entered simultaneously, so a single index of indicators that captures cross-country differences, in the spirit of Hendry [20], was used to facilitate estimation.<sup>5</sup> The country index is constructed using the average bank rating for each country over the 2000 – 2006 in-sample estimation period only (no information from the hold-out sample is employed) and is reported in Table 1. The 89 individual dummy variables could all be entered together in the SVM application.

Table 1 Country index.

<table><tr><td>Country</td><td>Weight</td><td>Country</td><td>Weight</td><td>Country</td><td>Weight</td></tr><tr><td>Albania</td><td>2.000</td><td>Hong Kong</td><td>6.000</td><td>Oman</td><td>5.000</td></tr><tr><td>Andorra</td><td>7.000</td><td>Hungary</td><td>3.000</td><td>Pakistan</td><td>2.333</td></tr><tr><td>Argentina</td><td>3.000</td><td>Iceland</td><td>0.000</td><td>Panama</td><td>5.000</td></tr><tr><td>Armenia</td><td>2.000</td><td>India</td><td>3.429</td><td>Peru</td><td>4.000</td></tr><tr><td>Australia</td><td>5.000</td><td>Indonesia</td><td>3.700</td><td>Philippines</td><td>3.000</td></tr><tr><td>Austria</td><td>6.000</td><td>Iran</td><td>3.000</td><td>Poland</td><td>4.250</td></tr><tr><td>Azerbaijan</td><td>2.000</td><td>Ireland</td><td>0.000</td><td>Qatar</td><td>5.333</td></tr><tr><td>Bahrain</td><td>5.250</td><td>Israel</td><td>4.667</td><td>Romania</td><td>3.000</td></tr><tr><td>Bangladesh</td><td>1.000</td><td>Italy</td><td>6.100</td><td>Russia</td><td>2.957</td></tr><tr><td>Belarus</td><td>1.750</td><td>Jamaica</td><td>3.000</td><td>San Marino</td><td>6.000</td></tr><tr><td>Benin</td><td>3.000</td><td>Japan</td><td>4.706</td><td>Saudi Arabia</td><td>6.600</td></tr><tr><td>Bermuda</td><td>5.000</td><td>Jordan</td><td>6.000</td><td>Serbia</td><td>2.000</td></tr><tr><td>Bosnia and Herzegovina</td><td>2.000</td><td>Kazakhstan</td><td>3.000</td><td>Slovakia</td><td>4.500</td></tr><tr><td>Brazil</td><td>4.333</td><td>Kenya</td><td>3.000</td><td>Slovenia</td><td>5.667</td></tr><tr><td>Bulgaria</td><td>3.500</td><td>Korea</td><td>5.667</td><td>South Africa</td><td>0.000</td></tr><tr><td>Canada</td><td>7.000</td><td>Kuwait</td><td>5.500</td><td>Spain</td><td>6.833</td></tr><tr><td>Chile</td><td>5.500</td><td>Latvia</td><td>3.500</td><td>Sri Lanka</td><td>2.000</td></tr><tr><td>China</td><td>2.231</td><td>Lebanon</td><td>3.000</td><td>Sweden</td><td>0.000</td></tr><tr><td>Colombia</td><td>0.000</td><td>Lithuania</td><td>4.000</td><td>Switzerland</td><td>6.750</td></tr><tr><td>Costa Rica</td><td>4.000</td><td>Macau</td><td>5.000</td><td>Taiwan</td><td>4.357</td></tr><tr><td>Cyprus</td><td>4.000</td><td>Macedonia</td><td>2.000</td><td>Thailand</td><td>4.143</td></tr><tr><td>Czech Republic</td><td>6.000</td><td>Malaysia</td><td>4.667</td><td>Trinidad</td><td>5.000</td></tr><tr><td>Dominican</td><td>1.667</td><td>Malta</td><td>4.000</td><td>Tunisia</td><td>3.000</td></tr><tr><td>Egypt</td><td>3.500</td><td>Mexico</td><td>5.143</td><td>Turkey</td><td>3.667</td></tr><tr><td>El Salvador</td><td>4.000</td><td>Mongolia</td><td>0.000</td><td>UAE</td><td>5.250</td></tr><tr><td>Estonia</td><td>6.000</td><td>Morocco</td><td>0.000</td><td>UK</td><td>5.875</td></tr><tr><td>France</td><td>5.778</td><td>Netherlands</td><td>6.500</td><td>Ukraine</td><td>2.273</td></tr><tr><td>Georgia</td><td>3.000</td><td>Niger</td><td>2.000</td><td>USA</td><td>6.876</td></tr><tr><td>Germany</td><td>5.444</td><td>Nigeria</td><td>3.000</td><td>Venezuela</td><td>2.857</td></tr><tr><td>Greece</td><td>5.667</td><td>Norway</td><td>7.000</td><td>Vietnam</td><td>3.000</td></tr></table>

Notes: The country index is constructed using the average rating for each country based upon the in-sample estimation period only. A country with a zero entry implies that no banks for that country appear in the estimation period.

For the <sup>fi</sup>nancial variables the <sup>fi</sup>rst lagged values of the following are considered as potential determinants of bank ratings. The ratio of equity to total assets [denoted $E q u i t y _ { i t } ] ,$ the ratio of liquid assets to total assets $[ L i q u i d i t y _ { i t } ]$ the natural logarithm of total assets $[ \ln ( A s s e t s ) _ { i t } ]$ and the net interest margin [NI\_Margin]. Also considered are $N O A _ { i t } { = } O I A _ { i t } { - }$ $O E A _ { i t }$ (where $O I A _ { i t }$ is the ratio of operating income to total assets and $O E A _ { i t }$ is the ratio of operating expenses to assets), the ratio of operating expenses to total operating income $[ O E O I _ { i t } ]$ and the return on equity $[ R \bar { O } A E _ { i t } ] . ^ { 6 }$

We do not include current values of these seven <sup>fi</sup>nancial covariates because they may contain information that was unknown at the time the rating was made. For example, if a bank's rating was decided in January 2006 then the value of any explanatory factor measured over the whole of 2006 would be unknown when the rating was made.

## 4. Results

Two versions of ordered logit and probit models are used to predict bank ratings: a general model (including all potential explanatory variables) and a favoured parsimonious speci<sup>fi</sup>cation obtained using a cross-sectional variant of the general-to-speci<sup>fi</sup>c methodology.<sup>7</sup> Because the favoured parsimonious model includes time in the logit speci<sup>fi</sup>cation and excludes time for the probit model we report two parsimonious models (one including time and one excluding time) for both logit and probit forms. These estimated ordered choice models are reported in Table 2.

Table 2 Bank ratings ordered choice regressions.

<table><tr><td rowspan="3">Variables</td><td colspan="3">Logit specifications</td><td colspan="3">Probit specifications</td></tr><tr><td rowspan="2">General model</td><td colspan="2">Parsimonious models</td><td rowspan="2">General model</td><td colspan="2">Parsimonious model</td></tr><tr><td>With time</td><td>Without time</td><td>With time</td><td>Without time</td></tr><tr><td>Country</td><td>2.184 (16.166)</td><td>2.145 (17.797)</td><td>2.163 (18.021)</td><td>1.156 (14.658)</td><td>1.141 (15.999)</td><td>1.153 (16.029)</td></tr><tr><td>Time</td><td>-0.131 (-2.306)</td><td>-0.143 (-2.674)</td><td></td><td>-0.059 (-1.611)</td><td>-0.063 (-1.807)</td><td></td></tr><tr><td>Equityt-1</td><td>0.057 (6.060)</td><td>0.062 (7.336)</td><td>0.060 (7.098)</td><td>0.033 (5.731)</td><td>0.035 (6.697)</td><td>0.035 (6.611)</td></tr><tr><td>Liquidityt-1</td><td>0.057 (0.111)</td><td></td><td></td><td>-0.056 (-0.184)</td><td></td><td></td></tr><tr><td>ln(Assets)t-1</td><td>0.483 (9.260)</td><td>0.470 (9.136)</td><td>0.443 (8.966)</td><td>0.260 (8.410)</td><td>0.251 (8.197)</td><td>0.240 (8.523)</td></tr><tr><td>NI_Margint-1</td><td>0.038 (0.911)</td><td></td><td></td><td>0.020 (0.813)</td><td></td><td></td></tr><tr><td>NOAt-1</td><td>6.368 (0.978)</td><td></td><td></td><td>3.373 (0.929)</td><td></td><td></td></tr><tr><td>OEOf-1</td><td>-0.324 (-3.238)</td><td>-0.429 (-4.404)</td><td>-0.453 (-4.458)</td><td>-0.207 (-3.086)</td><td>-0.261 (-4.401)</td><td>-0.268 (-4.417)</td></tr><tr><td>ROAEt-1</td><td>0.014 (1.785)</td><td>0.022 (3.933)</td><td>0.024 (4.433)</td><td>0.010 (1.966)</td><td>0.013 (3.909)</td><td>0.014 (4.270)</td></tr><tr><td colspan="7">Limit points</td></tr><tr><td>λ1</td><td>9.566 (9.928)</td><td>8.960 (11.770)</td><td>9.359 (12.316)</td><td>5.381 (9.663)</td><td>5.077 (11.469)</td><td>5.274 (11.706)</td></tr><tr><td>λ2</td><td>12.769 (12.413)</td><td>12.145 (14.189)</td><td>12.513 (14.510)</td><td>6.937 (11.880)</td><td>6.627 (13.585)</td><td>6.823 (13.496)</td></tr><tr><td>λ3</td><td>15.506 (13.738)</td><td>14.873 (15.659)</td><td>15.208 (15.893)</td><td>8.349 (12.889)</td><td>8.041 (14.516)</td><td>8.228 (14.403)</td></tr><tr><td>λ4</td><td>17.308 (14.512)</td><td>16.685 (16.246)</td><td>17.000 (16.465)</td><td>9.288 (13.503)</td><td>8.984 (14.935)</td><td>9.166 (14.836)</td></tr><tr><td>λ5</td><td>19.838 (15.446)</td><td>19.217 (17.001)</td><td>19.522 (17.209)</td><td>10.630 (14.322)</td><td>10.324 (15.574)</td><td>10.506 (15.477)</td></tr><tr><td>λ6</td><td>21.841 (16.214)</td><td>21.211 (17.757)</td><td>21.502 (17.952)</td><td>11.711 (15.056)</td><td>11.399 (16.260)</td><td>11.576 (16.172)</td></tr><tr><td>λ7</td><td>24.260 (17.292)</td><td>23.613 (18.786)</td><td>23.877 (18.995)</td><td>13.063 (16.199)</td><td>12.742 (17.376)</td><td>12.914 (17.283)</td></tr><tr><td>λ8</td><td>26.498 (17.675)</td><td>25.836 (18.877)</td><td>26.087 (19.154)</td><td>14.200 (16.505)</td><td>13.870 (17.475)</td><td>14.026 (17.531)</td></tr><tr><td colspan="7">Fit measures</td></tr><tr><td>Pseudo R2</td><td>0.396</td><td>0.394</td><td>0.391</td><td>0.376</td><td>0.375</td><td>0.373</td></tr><tr><td>SBC</td><td>2.604</td><td>2.573</td><td>2.574</td><td>2.682</td><td>2.650</td><td>2.646</td></tr><tr><td>LR statistic</td><td>811.670 [0.000]</td><td>808.964 [0.000]</td><td>802.199 [0.000]</td><td>771.571 [0.000]</td><td>769.032 [0.000]</td><td>764.958 [0.000]</td></tr><tr><td>LR(general→*)</td><td>NA</td><td>2.706 [0.439]</td><td>9.471 [0.050]</td><td>NA</td><td>2.540 [0.468]</td><td>6.613 [0.158]</td></tr><tr><td>Observations</td><td>517</td><td>517</td><td>517</td><td>517</td><td>517</td><td>517</td></tr></table>

Notes: The dependent variable is a bank's rating which has nine categories that correspond to the integer values in the range of 1 to 9 and vields eight limit points, λ, i = 1. 2. ... 8 (the intercept is not separately identi<sup>fi</sup>ed from the limit points). Z-statistics (in parentheses) are based upon Huber-White standard errors. Also reported are the Pseudo $R ^ { 2 } ,$ Schwartz's information criterion, SBC, and likelihood ratio tests for the model's explanatory power, LR Statistic, and the deletion of variables from the general model to obtain the parsimonious model, LR(general →\*). Probability values are given in square parentheses. All regressions were estimated using E-Views 6.0 and STATA 11 over the period 2000–2006.

Table 3 Ordered choice models percentage of correct predictions.

<table><tr><td></td><td>Logit</td><td>Probit</td></tr><tr><td>General</td><td>36.607% (53.191%)</td><td>37.500% (52.418%)</td></tr><tr><td>Parsimonious (with time)</td><td>38.393% (52.031%)</td><td>39.286% (51.838%)</td></tr><tr><td>Parsimonious (without time)</td><td>35.714% (51.064%)</td><td>33.036% (50.870%)</td></tr><tr><td>General (without country index)</td><td>19.643% (30.948%)</td><td>21.429% (31.141%)</td></tr></table>

The out-of-sample percentage of correct predictions (PCP) is reported with the corresponding in-sample values given in parentheses. The predicted rating for each observation is chosen upon the basis of the category with the highest probability. The expected PCP when the 9 rating categories are selected randomly is 11.11%.

The percentage of correct predictions (PCPs) of bank ratings from these ordered choice models (both in-sample and out-of-sample) are reported in Table 3. From Table 3 the general model has the highest in-sample PCP for both logit and probit speci<sup>fi</sup>cations (being 53.191% and 52.418%, respectively) and, upon this criterion, the general model would be chosen for producing out-of-sample predictions. However, the parsimonious model (with time) has the highest out-of-sample PCPs for both logit and probit speci<sup>fi</sup>cations (being 38.393% and 39.286%, respectively). Two points are clear from this. First, the model with the highest in-sample predictive performance is not necessarily the one with the greatest out-of-sample performance — although the difference between the best model's out-of-sample PCP and the model's out-of-sample PCP chosen upon the basis of the highest insample PCP is less than two percentage points. Second, the out-ofsample predictive performance is substantially lower than the corresponding in-sample predictive performance (by approximately 15 percentage points). Nevertheless, the out-of-sample predictive performance is also substantially greater (by up to 28 percentage points) than would be expected by predicting the 9 rating categories randomly (being 11.111%).

SVM's percentage of correct predictions (grid search on 2000 – 2006 data only).

<table><tr><td rowspan="2">C</td><td colspan="4">ε</td></tr><tr><td>0</td><td>0.25</td><td>0.5</td><td>0.75</td></tr><tr><td>0.125</td><td>39.458%</td><td>39.265%</td><td>38.104%</td><td>36.364%</td></tr><tr><td>0.25</td><td>38.491%</td><td>40.232%</td><td>36.750%</td><td>37.718%</td></tr><tr><td>0.5</td><td>40.619%</td><td>41.006%</td><td>39.458%</td><td>36.750%</td></tr><tr><td>1</td><td>42.553%</td><td>44.101%</td><td>40.039%</td><td>37.911%</td></tr><tr><td>2</td><td>42.747%</td><td>45.261%</td><td>43.520%</td><td>39.652%</td></tr><tr><td>4</td><td>42.360%</td><td>45.648%</td><td>43.520%</td><td>40.232%</td></tr><tr><td>8</td><td>43.327%</td><td>45.455%</td><td>44.681%</td><td>40.619%</td></tr><tr><td>16</td><td>43.327%</td><td>45.068%</td><td>44.294%</td><td>41.393%</td></tr><tr><td>32</td><td>43.520%</td><td>45.648%</td><td>45.068%</td><td>41.586%</td></tr><tr><td>64</td><td>42.553%</td><td>46.228%</td><td>44.487%</td><td>41.199%</td></tr><tr><td>128</td><td>42.550%</td><td>45.260%</td><td>44.490%</td><td>41.200%</td></tr><tr><td>256</td><td>43.330%</td><td>44.870%</td><td>44.490%</td><td>40.620%</td></tr></table>

The grid search percentage of correct predictions (PCP) is reported for various combinations of C and ε in an SVM incorporating the <sup>fi</sup>rst lags of all <sup>fi</sup>nancial variables, all country indicators individually and excluding the time variable. The grid search procedure uses 10-fold cross-validation using only data between 2000 and 2006, where bold-italic emphasis indicates the optimal value.

Table 5  
SVM's Percentage of correct predictions (in-sample and out-of-sample).

<table><tr><td colspan="5">Model: C=64, ε=0.25, including 1 lag of all financial variables</td></tr><tr><td>Countries</td><td>Country index</td><td>Time</td><td>In-sample</td><td>Out-of-sample</td></tr><tr><td>Y</td><td></td><td>Y</td><td>59.2%</td><td>40.2%</td></tr><tr><td>Y</td><td></td><td></td><td>57.6%</td><td>44.6%</td></tr><tr><td></td><td>Y</td><td>Y</td><td>53.8%</td><td>41.1%</td></tr><tr><td></td><td>Y</td><td></td><td>53.0%</td><td>41.1%</td></tr><tr><td></td><td></td><td>Y</td><td>29.8%</td><td>27.7%</td></tr><tr><td></td><td></td><td></td><td>29.2%</td><td>23.2%</td></tr></table>

The in-sample and out-of-sample percentage of correct predictions are given for SVMs using the optimal parameters $( \mathsf { C } = 6 4 , \varepsilon = 0 . 2 5 )$ and including one lag of all financial variables. If country indicators are included individually in the SVM a Y is given in the column headed Countries otherwise it is left blank. A Y in the column headed Country Index indicates that the country index was included in the model while a Y in the column headed Time means that the time variable was incorporated in the SVM.

Regarding SVMs, the parameters C and need to be set. The selection of parameter values is automated using a grid search of PCPs of bank ratings obtained from the SVM that includes all country indicators and <sup>fi</sup>nancial variables but excludes the time variable for various combinations of C and ε and is reported in Table 4.<sup>8</sup> This search employs 10-fold cross-validation using only in-sample data to choose the optimal values, being C=64 and $\varepsilon = 0 . 2 5 . ^ { 9 }$ Using crossvalidation for the grid search means that optimal values are chosen based on out-of-sample predictions from within the in-sample period. That is, the 10 estimation and hold-out samples are drawn from the 517 in-sample data points from between 2000 and 2006 only. This ensures that the choice of parameter values is based on independent validation data, without using the 2007 out-of-sample data.

Table 5 reports PCPs for SVMs with C=64 and ε=0.25 for a variety of speci<sup>fi</sup>cations that contain or exclude the 89 individual country dummies (the column denoted Country in Table 5), the country index and the time variable — all speci<sup>fi</sup>cations include all of the <sup>fi</sup>nancial variables. The highest in-sample and out-of-sample PCPs are for SVMs that include the 89 country indicator variables separately. In-sample the SVM including time has the highest PCP (being 59.2% which compares with 57.6% for the model excluding time), however, the largest out-of-sample PCP is for the model excluding time (being 44.6% compared to 40.2% for the model including time). Two points are worthy of note. First, similar to our <sup>fi</sup>nding for the ordered choice models, the SVM with the highest insample PCP is not necessarily that with the greatest out-of-sample PCP. Second, SVMs that estimate all 89 country indicators unrestrictedly have superior PCPs (both in-sample and out-of-sample) to ordered choice models, where the difference between the best out-ofsample PCP for the two methods is about <sup>fi</sup>ve percentage points. This suggests that SVMs provide greater predictive accuracy than the methods currently used as standard for predicting ratings, being ordered choice models. This is important given that prediction is the primary purpose of such models.<sup>10</sup>

Interestingly, the PCPs of the SVMs that use the country index are generally much lower than the SVMs that include the 89 individual country dummy variables (both in-sample and out-of-sample) and are very similar to the PCPs of ordered choice models that also use this country index (if the PCPs are slightly larger for SVMs). Hence, it would seem that the superior predictive performance of SVMs over ordered choice models is because SVMs can be estimated including the large number of country dummies unrestrictedly, whereas the ordered choice models cannot.<sup>11</sup>

The PCPs of the SVM when country dummy variables (and country index) are excluded range from 29.2% to 29.8% in-sample and from 23.2% to 27.7% out-of-sample. This is a substantially worse performance relative to when country dummies (or the country index) are included. This dramatic deterioration in predictive performance when country effects are not accounted for is also exhibited by the ordered choice models [see the row entitled General (without country index) in Table 3]. This highlights the importance of accounting for country effects in predicting international bank ratings.

## 5. Conclusions

We have found that SVM for regression can produce notably better in-sample and out-of-sample predictions of international bank ratings than the standard method currently used for this purpose, ordered choice models. This appears due to the SVM's ability to estimate a large number of country dummies unrestrictedly, which was not possible with the ordered choice models due to the sample size.<sup>12</sup> Given that the primary purpose of modelling ratings is prediction this is an important result. We also highlight the crucial importance of modelling country effects when attempting to predict bank ratings.

## Acknowledgment

We gratefully acknowledge the helpful comments and suggestions of two anonymous referees on an earlier version of this paper. Any remaining errors are our own.

## References

[1] E.I. Altman, S. Katz, Statistical bond rating classi<sup>fi</sup>cation using <sup>fi</sup>nancial and accounting data, in: M. Schiff, G. Sorter (Eds.), Proceedings of the Conference on Topical Research in Accounting, New York University Press, New York, 1976, pp. 205–239.

[2] E.I. Altman, A. Saunders, Credit risk measurement: developments over the last 20 years, Journal of Banking and Finance 21 (11–12) (1997) 1721–1742

[3] E.I. Altman, A. Saunders, An analysis and critique of the BIS proposal on capital adequacy and ratings, Journal of Banking & Finance 25 (1) (2001) 25–46.

[4] J.D. Amato, C.H. Fur<sup>fi</sup>ne, Are Credit Ratings Procyclical? Journal of Banking and Finance 28 (11) (2004) 2641–2677.

[5] J. Ammer, F. Packer, How Consistent are Credit Ratings? A Geographical and Sectoral Analysis of Default Risk, Available at: Board of Governors of the Federal Reserve System International Discussion Paper No. 668, 2000. http://www3. interscience.wiley.com/cgi-bin/fulltext/121392086/PDFSTART.

[6] B. Baesens, T. van Gestel, S. Viaene, M. Stepanova, J. Suykens, J. Vanthienen, Benchmarking state-of-the-art classi<sup>fi</sup>cation algorithms for credit scoring, The Journal of the Operational Research Society 54 (6) (2003) 1082–1088.

[7] C.E. Bannierand, C.W. Hirsch, The economic function of credit rating agencies — what does the watchlist tell us? Journal of Banking & Finance 34 (12) (2010) 3037–3049.

[8] T. Bellotti, J. Crook, Support vector machines for credit scoring and discovery of signi<sup>fi</sup>cant features, Expert Systems with Applications 36 (2) (2009) 3302–3308.

[9] R. Cantor, T. Collins, E. Falkenstein, D. Hamilton, C.M. Hu, C.M. Chair, S. Nayar, R Ray, E. Rutan, F. Zarin, Testing for Rating Consistency in Annual Default Rates, Moody's Investor Service (2001).

[10] C.-C. Chang, C.-J. Lin, LIBSVM: A Library for Support Vector Machines Software available at, 2001. http://www.csie.ntu.edu.tw/\~cjlin/libsvm.

[11] X. Chen, X. Wang, D.D. Wu, Credit risk measurement and early warning of SMEs: An empirical study of listed SMEs in China, Decision Support Systems 49 (3) (2010) 301–310.

[12] M. Doumpos, C. Zopounidis, A multicriteria decision support system for bank rating, Decision Support Systems 50 (1) (2010) 55–63.

[13] D. Feng, C. Gourieroux, J. Jasiak, The ordered qualitative model for credit rating transitions, Journal of Empirical Finance 15 (1) (2008) 111–130.

[14] A.M. Fuertes, E. Kalotychou, On sovereign credit migration: a study of alternative estimators and rating dynamics, Computational Statistics and Data Analysis 51 (7) (2007) 3448–3483.

[15] K. Galil, The Quality of Corporate Credit Rating: An Empirical Investigation Available at SSRN: EFMA 2003 Helsinki Meetings, 2003. http://wwww.ssrn.com abstract=406681, doi:10.2139/ssrn.406681.

[16] V.V. Gavrishchaka, S. Banerjee, Support vector machine as an ef<sup>fi</sup>cient framework for stock market volatility forecasting, Computational Management Science 3 (2) (2006) 147–160.

[17] J.A. Gentry, D.T. Whitford, P. Newbold, Predicting industrial bond ratings with a probit model and fund <sup>fl</sup>ow components, The Financial Review 23 (3) (2005) 269–286.

[18] W.H. Greene, Econometric Analysis, Pearson, sixth ed, Prentice Hall, 2008.

[19] P. Hájek, Municipal credit rating modelling by neural networks, Decision Support Systems 51 (1) (2011) 108–118.

[20] D.F. Hendry, Modelling UK In<sup>fl</sup>ation, 1875–1991, Journal of Applied Econometric 16 (3) (2001) 255–275.

[21] D.F. Hendry, C. Santos, Regression models with data-based indicator variables, Oxford Bulletin of Economics and statistics 67 (5) (2005) 571–595.

[22] J.O. Horrigan, The determination of long-term credit standing with <sup>fi</sup>nancial ratios, Journal of Accounting Research 4 (1966) 44–62

[23] Z. Huang, H. Chen, C.-J. Hsu, W.-H. Chen, S. Wu, Credit rating analysis with support vector machines and neural networks: a market comparative study, Decision Support Systems 37 (4) (2004) 543–558.

[24] G. Iannotta, Testing for opaqueness in the European banking industry: evidence from bond credit ratings, Journal of Financial Services Research 30 (3) (2006) 287–309.

[25] J.D. Jackson, J.W. Boyd, A statistical approach to modelling the behavior of bond raters, The Journal of Behavioral Economics 17 (3) (1988) 173–193.

[26] M. Kamstra, P. Kennedy, Combining qualitative forecasts using logit, International Journal of Forecasting 14 (1) (1998) 83–93.

[27] M. Kamstra, P. Kennedy, T.K. Suan, Combining bond rating forecasts using logit, The Financial Review 37 (2) (2001) 75–96.

[28] S.K. Kim, Predicting bond ratings using publicly available information, Expert Systems with Applications 29 (1) (2005) 75–81.

[29] H.S. Kim, S.Y. Sohn, Support vector machines for default prediction of SMEs based on technology credit, European Journal of Operational Research 201 (2009) 838–846.

[30] Y.C. Lee, Application of support vector machines to corporate credit rating prediction, Expert Systems with Applications 33 (1) (2007) 67–74.

[31] D.P. Morgan, Rating Banks: Risk and Uncertainty in an Opaque Industry, The American Economic Review 92 (4) (2002) 874–888.

[32] G.E. Pinches, K.A. Mingo, A multivariate analysis of industrial bond ratings, Journal of Finance 28 (March 1973) 1–18.

[33] G.E. Pinches, K.A. Mingo, A note on the role of subordination in determining industrial bond ratings, Journal of Finance 30 (March 1975) 201–206.

[34] A.R. Pinto, Control and responsibility of credit rating agencies in the United States, American Journal of Comparative Law 54 (SUPPL) (2006) 341–356.

[35] P. Ravi Kumar, V. Ravi, Bankruptcy prediction in banks and <sup>fi</sup>rms via statistical and intelligent techniques — a review, European Journal of Operational Research 180 (2007) 1–28.

[36] C. Stefanescu, R. Tunaru, S. Turnbull, The Credit Rating Process and Estimation of Transition Probabilities: A Bayesian Approach, Journal of Empirical Finance 16 (2) (2009) 216–234.

[37] T. Van Gestel, B. Baesens, J.A.K. Suykens, D. Van den Poel, D.E. Baestaens, M. Willekens, Bayesian kernel based classi<sup>fi</sup>cation for <sup>fi</sup>nancial distress detection, European Journal of Operational Research 172 (2006) 979–1003.

[38] V. Vapnik, The Nature of Statistical Learning Theory, Springer, NY, 1995.

[39] R.R. West, An alternative approach to predicting corporate bond ratings, Journal of Accounting Research 8 (Spring 1970) 118–125.

Tony Bellotti is Lecturer in Statistics in the Department of Mathematics at Imperial College London. He received his PhD in computational learning from Royal Holloway, University of London in 2006 and his main research interest is the application of statistical and machine learning models in credit risk analysis. Tony is an Honorary Fellow in the Credit Research Centre at the University of Edinburgh.

Roman Matousek is Professor of Finance and Director of Centre for EMEA Banking, Finance and Economics at London Metropolitan University. Roman is also Managing Editor for International Journal of Monetary Economics and Finance. His research encompasses theoretical and empirical inquiry into issues of banking ef<sup>fi</sup>ciency, regulation, microeconomics of banking and monetary policy. His research outcomes have been published in academic journals including: Journal of Banking and Finance, The European Journal of Finance, OMEGA, Journal of International Financial Markets, Institutions and Money, Journal of Comparative Economics, Review of International Economics, Journal of Financial Regulation and Compliance.

Chris Stewart is Senior Lecturer in Economics at London Metropolitan Business School, London Metropolitan University. His quali<sup>fi</sup>cations include BA Political Economy (Thames Polytechnic), MSc Economics (Birkbeck College, University of London) and PhD “Modelling and Comparing OECD Countries’ Consumer Behaviour” (London Guildhall University). Chris has published around 30 papers in refereed academic journals including: Applied Economics, Economics Letters, Economic Modelling, Empirical Economics, Expert Systems with Applications, International Review of Applied Economics, Journal of Financial Regulation and Compliance, Journal of Forecasting, Journal of Policy Modelling, The Manchester School, Review of International Economics and Small Business Economics. These are primarily empirical papers on various topics including: international bank ratings, consumer behaviour, exchange rates, <sup>fi</sup>rm performance, fund manager performance, identity, regional development, small and medium size enterprise share and spurious correlation.
