---
otero_id: 10608
otero_key: "ZNR5U35J"
title: "Scad-elastic net and the estimation of individual tourism expenditure determinants"
authors: "Antonino Abbruzzo; Juan Gabriel Brida; Raffaele Scuderi"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2014.06.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Scad-elastic net and the estimation of individual tourism expenditure determinants

Antonino Abbruzzo <sup>a</sup>, Juan Gabriel Brida <sup>b</sup>, Raffaele Scuderi <sup>c,</sup>⁎

<sup>a</sup> Dipartimento di Scienze Economiche Aziendali e Statistiche, University of Palermo, Viale delle Scienze Ed. 13, 90128 Palermo, Italy <sup>b</sup> School of Economics and Management, TOMTE (Competence Center in Tourism, Management and Tourism Economics), Free University of Bozen-Bolzano, Piazza, Universita 1, 39100 Bozen-Bolzano, Italy

<sup>c</sup> Faculty of Economic Sciences and Law, University of Enna Kore, Cittadella, Universitaria, 94100 Enna, Italy

## a r t i c l e i n f o

Article history: Received 5 September 2013 Received in revised form 2 June 2014 Accepted 4 June 2014 Available online xxxx

Keywords: Scad-elastic net Collinearity Penalized regression Variable selection Tourism expenditure Uruguay

## a b s t r a c t

This paper introduces the use of scad-elastic net in the assessment of the determinants of individual tourist spending. This technique approaches two main estimation-related issues of primary importance. So far studies of tourism literature have made a wide use of classic regressions, whose results might be affected by multicollinearity. In addition, because of the absence of robust economic theory on tourism behavior, regressor selection is often left to researcher's choice when not driven by non-optimal automatic criteria. Scad-elastic net is an OLS model that accounts for both these problems by including two types of parameters constraints, namely the smoothly clipped absolute deviation (scad) and the ℓ -norm. We analyze an of<sup>fi</sup>cial dataset of incoming tourists to Uruguay. Socio-demographic, psychographic and trip-related variables are used as explanatory of per capita per day tourist expenditure. Signi<sup>fi</sup>cant impact on tourism expenditure of some accommodation facilities such as expensive one and second dwellings, personal experiences rather than the number of past visits, doing certain activities, place of stay, and seasonality are the main conclusions that are drawn from the analysis. © 2014 Elsevier B.V. All rights reserved.

## 1. Introduction

Tourism has become a notable phenomenon for many economies. Beyond sociocultural and political reasons, its economic impact is one of the main motivations for the growing interest on it [27]. The perception of tourism and its economic effects have evolved over time. From being considered as a standardized mass phenomenon, after the eighties it evolved to a more differentiated and <sup>fl</sup>exible model [2]. Today it is meant to be a complex set of products and services for a segmented demand of individuals with different tastes, needs and consumption behavior. Indeed, the search for the maximization of economic impact has to face such heterogeneity. Increasing the average levels of individual spending guests deals with the supply of adequate products and services. Within this differentiated set of costumers, <sup>fi</sup>nding the common signi<sup>fi</sup>cant elements that impact on spending behavior can be of help for addressing the operators' actions. These concerns not only increase in pro<sup>fi</sup>ts, but also search for policies that would improve economic and related effects of tourism in a region, such as occupation, sustainability, and more in general welfare.

Tourism studies have widely adopted this perspective. Speci<sup>fi</sup>cally, econometric models have provided different methodological approaches for the sake of studying the likely average pro<sup>fi</sup>le of tourists, as well as quantifying their impact. Starting from data surveyed at individual level, these studies have tested ‘whether’ and ‘how much’ each variable from a set can explain the spending behavior of tourists. Indeed, knowing the likely individual characteristics that would enhance economic impact can provide signi<sup>fi</sup>cant support to policy decisions. As the comprehensive review by [12] reports, various individual characteristics have been tested in models by the past studies, such as economic constraints (income, assets, health status, etc.), sociodemographic attributes (age, education, gender, place of residence, occupation, etc.), trip-related characteristics (accommodation type, on-site activities, destination, travel information source, etc.) and psychographic variables (opinions, attitudes, motivations, etc.) However, the same review by [12] stresses that different questions are still open. The one that this paper attempts to address mainly is little methodological innovation, which leaves some estimation issues unsolved.

This paper contributes to the strand of the literature on the determinants of individual tourist spending. The main research question deals with the investigation of the signi<sup>fi</sup>cance and impact of a set of variables on individual spending, through an appropriate model that would overcome multicollinearity and perform selection of regressors. To this end, we apply scad-elastic net. It is a regression technique that allows overcoming two main aspects of the estimation methods that have been applied by the previous contributors. Proper selection of explanatory variables is the <sup>fi</sup>rst one. As also [12] report, in the absence of a robust theory on individual tourist behavior the variable choice is usually left to the researcher. Some contributors adopted automatic selection criteria like stepwise, which however have proven to be unstable.

Multicollinearity is a second and well-known problem, which affects the reliability of individual predictors. Scad-elastic net is a method that allows selecting regressors while simultaneously handling multicorrelation. This way, a high number of explanatory variables can be tested. To the best knowledge of the authors, this is the <sup>fi</sup>rst attempt in the tourism literature to apply this technique, as well as to account for these two methodological issues simultaneously. We apply the model to data from the of<sup>fi</sup>cial survey conducted in Uruguay by [31]. Such dataset comprises a wide set of variables that have been used by the previous studies. Results are interpreted in the light of the previous <sup>fi</sup>ndings in the literature, which are resumed by the comprehensive review of [12].

## 2. Background

The systems to support decisions in the tourism <sup>fi</sup>eld have been the object of investigation for several contributions. The range of the topics is wide. Among other themes, researchers have focused on websites [16, 45], hotel room bookings [23] and visitors' routes [42]. In addition, a number of studies are relevant to the decision making processes in tourism, even if they don't explicitly focus on this industry — among others, [33,37,36].

In the tourism demand literature, papers making use of data at individual level to analyze spending have been in a relatively more limited number than others using aggregate data [12]. In addition, the application of new methodologies in the individual spending literature has been more limited if compared to the analysis of aggregate demand [38,30,15]. Use of proper techniques for data analysis is indeed one of the main topics in order to provide opportune support to decision processes. OLS regression has been the most used method in estimating the determinants of individual spending [35,14,24]. Self-selection bias between spenders and non-spenders led also to the use of Tobit model [8,5], and more in general two-step selection approaches [9,11, 21,44]. Further methods assessed the characteristics of individual tourists with different attitude to spending by using quantile regressions [37, 28,40]. Other approaches transformed spending into a binary variable and made use of logistic regression in order to focus on the choice process between tourism and other goods [4,17,34]. Besides these classic techniques, the review paper of [12] reports that in the recent years there has been a renewed interest on the use of novel approaches [1, 46,3].

Usually, the variable selection process has not been driven by robust economic theory, which lacks for consumption behavior in tourism. In the majority of papers regressors were selected on the basis of the previous literature [12]. The alternative approach of using statistical criteria has been relatively less frequent and concerned the application of stepwise analysis, as in [9,35,25,22,43]. However, as reported by [6], stepwise is an unstable technique. As an example, consider two almost identical datasets, in which the second one is obtained by the <sup>fi</sup>rst minus a few randomly chosen observations. [6] stresses that estimating the same model on the two sets could lead to notably different results. In addition, stepwise may drop groups of important regression coef<sup>fi</sup>cients in case of high correlation between the regressors.

The latter sentence introduces a second important topic in estimation procedures. Multicollinearity is a classic problem while performing regression estimates. When regressors' selection is not done properly, the presence of the groups of two of more correlated explanatory variables constitutes a serious shortcoming to model estimation. Also here instability can arise, in the sense that one of the variables of a group can exhibit a higher coef<sup>fi</sup>cient. This often causes the scholar to remove variables from the analysis. Multicollinearity in tourism datasets is a problem that may arise quite often. As examples, think about the use of wealth levels, occupation and accommodation in luxury hotels. Or rather, nationality and residence are two other very highly correlated variables which can be both of interest for the present case study, where a high number of former residents of Uruguayan nationality are used to visit their country of origin very often [13]. Another example related to Uruguay is that people from the neighbor country of Argentina constitute a very high portion of tourist <sup>fl</sup>ows and use to repeat the visit [13,1]. Proper assessment of the effects of nationality and number of the past visits needs to consider such relationship.

In order to address these two issues, scad-elastic net [47,19], a model of the category of penalized regressions, will be used in what follows. Regarding model selection, the procedure introduces appropriate parameters constraints that allow to select variables and to estimate parameters simultaneously. After opportune choice of tuning parameters, the procedure provides estimates only for signi<sup>fi</sup>cant regressors. Instead, the less stable stepwise technique estimates different models by including/excluding regressors from the original set, and compares each model's statistics in order to <sup>fi</sup>nd the ‘optimal’ one.

As to multicollinearity, scad-elastic net does not cause computational problems to estimations. The method forces groups of perfectly correlated predictors to have the same coef<sup>fi</sup>cient, and sets of highly correlated predictors to have similar coef<sup>fi</sup>cients. Therefore, in the presence of correlated right hand variables the estimated effect of a regressor on the dependent variable is opportunely spread over all the group of correlated variables. This has implications also for the use of dummy variables, where the exclusion of a reference category is not necessary when deciding the set of data to include. Overall, the use of scadelastic net has the notable advantage of including a large number of variables that the previous studies used to test as determinants of spending, with no concerns about regressors' autocorrelation.

Proper handling of both the two aspects of model selection and collinearity makes this technique providing more stable estimates than classic regressions. In addition, it does not require any distributional assumption on the error. This latter characteristic is proper also of OLS. However, if we want to do model selection from OLS via AIC or BIC, distributional assumptions on the error are needed. Also, scadelastic net can be used with a variety of loss functions. Another general feature is its usability with high-dimensional datasets, even in those cases where the number of variables exceeds the number of observations. Although the dataset we will analyze in what follows has a high number of regressors, their number does not exceed the one of the surveyed tourists.

Despite the advantages of these models, some remarks are needed. Although there might be an attempt to use them as ‘self-working machines’, particular attention should be paid to the choice of tuning parameters. In addition, in case model selection is not necessary because of few nonsigni<sup>fi</sup>cant coef<sup>fi</sup>cients, or no collinearity between explanatory variables occurs, OLS remains the best solution. A third and more methodological remark concerns the relationship between penalty function and likelihood approaches, which seems to be easier to handle from a Bayesian perspective. Bayesian approaches consider parameters as random variables so that distributional assumptions can be considered on the regression parameters. Bayesian approaches give interval estimations and provide the posterior distribution for the estimator [29]. Although this makes the interpretation of the penalty more explicit and probably easier to understand, it introduces other problems in estimation procedures.

## 3. Methodology

Introducing penalty functions on the parameters as in scad-elastic net is a regularized regression approach. The methodology is part of a group that comprises ridge regression, lasso and elastic net. Ridge regression [20] uses the $\ell _ { 2 } .$ -norm in order to constraint parameters. The least absolute shrinkage and selection operator (‘lasso’) [41] instead apply a ℓ -norm. Elastic net [47] is a linear combination of the former two, i.e. of $\ell _ { 1 }$ and $\boldsymbol { \mathscr { l } } _ { 2 }$ -norms. As shown by [47], elastic net presents higher accuracy in prediction than other regression and penalized regression approaches. However it doubles the bias in the estimates.

Please cite this article as: A. Abbruzzo, et al., Scad-elastic net and the estimation of individual tourism expenditure determinants, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.06.003

For this reason we use the smoothly clipped absolute penalty (scad) which is a modi<sup>fi</sup>cation of the elastic net that is proven to reduce the bias. The scad penalty has three important properties: i) singularity at the origin to produce sparse solutions (zero coef<sup>fi</sup>cients); ii) it satis<sup>fi</sup>es certain conditions to produce continuous models (for stability selection); and iii) it is bounded by a constant to produce nearly unbiased estimates for large coef<sup>fi</sup>cients. The lasso penalty that is used by elastic net fails to satisfy the last property.

Next, we summarize the methodology and address the problem of tuning parameter selection.

## 3.1. Penalized regression models

Consider the following regression model with p predictors and n sample size:

$$
\mathbf {y} = X \boldsymbol {\beta} + \epsilon ,
$$

where $X _ { n \times p } = [ \mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } , . . . , \mathbf { x } _ { p } ] , \beta = [ \beta _ { 1 } , \beta _ { 2 } , . . . , \beta _ { p } ] ^ { T } ,$ , and $\mathbf { y } = [ y _ { 1 } , y _ { 2 } , . . . , y _ { n } ] ^ { T } ,$ ϵ is the additive noise with dimension n×1. Suppose that the predictor $\left( \mathbf { X } _ { i } = 1 , . . . , p \right)$ , is normalized to mean zero and variance one, and the regression output y sums to zero. The optimization problem for naive elastic net is:

$$
\hat {\beta} (\text { naive   e.net }) = \arg \min _ {\beta} \left| | \mathbf {y} - X \beta | \right| ^ {2} + \lambda_ {1} \| \beta \| _ {1} + \lambda_ {2} \| \beta \| ^ {2},\tag{1}
$$

where $\aleph _ { 1 }$ and $\lambda _ { 2 }$ are positive weights, and correspond to the tuning parameters that have to be selected, $\begin{array} { r } { \vert \vert \beta \vert \vert _ { 1 } = \sum _ { j = 1 } ^ { p } \vert \beta _ { j } \vert } \end{array}$ is the $\ell _ { 1 } { \mathrm { - n o r m } } ,$ $\begin{array} { r } { | | \beta | | ^ { 2 } = \sum _ { \mathbf { \beta } } ^ { \mathbf { \alpha } _ { p } } = 1 \beta _ { j } ^ { 2 } } \end{array}$ is the $\boldsymbol { \mathscr { l } } _ { 2 } { \mathrm { - n o r m } }$ , and $\| \boldsymbol { \mathsf { y } } - \boldsymbol { X } \beta \| ^ { 2 }$ is the quadratic loss function.

Ridge regression is a speci<sup>fi</sup>c case of Eq. (1) when $\lambda _ { 1 } = 0 .$ . Compared to OLS, the main advantage of using it is that in case a group of explanatory variables presents very high pairwise correlations, ridge tends to assign similar estimation values to all variables in the group. In particular, if they are perfectly correlated we obtain exactly the same regression coef<sup>fi</sup>cients. However, to obtain a more parsimonious model a proper selection of regressors is needed.

If we <sup>fi</sup>x $\Lambda _ { 2 } = 0 \mathrm { i n } ( 1 )$ , we obtain the lasso optimization. The lasso was mainly proposed to solve high-dimensional problems that is when the number of variables exceeds the sample size. Lasso was introduced in order to improve OLS and ridge regression by doing shrinkage and variable selection simultaneously. One of its disadvantages is that it selects at most n variables. Moreover, it cannot handle groups of correlated regressors properly. This means that in the presence of a group of variables where the pairwise correlations are very high, lasso tends to arbitrarily select only one variable from that group.

The naive elastic net corresponds to the optimization problem in Eq. (1). It allows doing both variable selection and handle groups of correlated variables. Simulation studies and real data analysis showed that it often outperforms the lasso in terms of prediction accuracy. However, naive elastic net does not perform satisfactorily because of the bias in estimates produced by the two tuning parameters.

## 3.2. Scad-elastic net

The bias in naive elastic net can be partially corrected through the smoothly clipped absolute penalty (scad). It has the important characteristics of making lower shrinkage on the coef<sup>fi</sup>cients that are far from zero, which reduces the bias on the estimates. In order to connect elastic net with scad-elastic net, we re-write the optimization problem in Eq. (1) as:

$$
\hat {\beta} (\text { naive   e.net }) = \arg \min _ {\beta^ {*}} \left| \left| \mathbf {y} ^ {*} - X ^ {*} \beta^ {*} \right| \right| ^ {2} + \gamma \| \beta^ {*} \| _ {1},\tag{2}
$$

where $\begin{array} { r } { \gamma = \frac { \lambda _ { 1 } } { \sqrt { 1 + \lambda _ { 2 } } } , } \end{array}$ and:

$$
y ^ {*} = \binom {\mathbf {y}} {0}, \quad X ^ {*} = (1 + \lambda_ {2}) ^ {- \frac {1}{2}} \binom {X} {\sqrt {\lambda_ {2}} I}, \quad \beta^ {*} = \sqrt {(1 + \lambda_ {2})} \beta .
$$

For any <sup>fi</sup>xed $\lambda _ { 2 } ,$ the naive elastic net is equivalent to a lasso problem with a bigger design matrix. Lasso already had an ef<sup>fi</sup>cient solver called LARS (Least Angle Regression) [18]. The scad-elastic net considers the scad penalty instead of the $\ell _ { 1 }$ penalty. A coordinate descent algorithm for nonconvex optimization problems can be used to obtain the estimates [7].

## 3.3. Tuning parameter selection

Selection of the two tuning parameters $\aleph _ { 1 }$ and $\lambda _ { 2 }$ is still an open question. Usually, information criteria such as AIC and BIC are used in classic regression to do model selection. Since we are not considering maximum likelihood estimators, AIC and BIC cannot be used. Therefore K-fold cross validation seems to be the best option. However in real data analysis particular attention should be paid in choosing $\lambda _ { 1 }$ and $\lambda _ { 2 } ,$ beyond the value that is provided automatically by the cross validation.

In this paper, tuning parameter selection is performed with the aim to <sup>fi</sup>nd a parsimonious model which at the same time can still give a small cross validation error. In particular, we adopt a 10-fold cross validation, where the original sample is randomly partitioned into 10 subsamples of equal size. Of the 10 subsamples, a single subsample is retained as the validation data for testing the model, and the remainder 9 is used as training data. The cross-validation process is then repeated 10 times (the folds), with each of the 10 subsamples used exactly once as the validation data. The 10 results from the folds then can be averaged (or otherwise combined) to produce a single estimation.

## 4. Data analysis

## 4.1. Dataset

The Ministry for Tourism and Sport of Uruguay conducts a quarterly survey on non-resident visitors entering the country for purposes different than migration and working. Uruguay represents an interesting case study for tourism. Although it is the second smallest country in South America, tourist <sup>fl</sup>ow account for about 80% of the total population, and this percentage has increased [13]. Data were recorded at the end of tourists' journey at the main exit points of Uruguay. Structure of the questionnaire is reported by Table 1. This study considers the four 2010 surveys [31], with an overall number of surveyed records of 9328.

Structure of the questionnaire and surveyed variables.

<table><tr><td>Groups</td><td>Variables</td></tr><tr><td>Socio-demographic</td><td>Nationality; country of residence; occupation; education; number of past trips in Uruguay.</td></tr><tr><td>Psychographic</td><td>Main and secondary element(s) of satisfaction and dissatisfaction with the trip.</td></tr><tr><td>Trip-related</td><td>Entry and exit point; mean of transportation to enter, travel and exit Uruguay; entrance and exit date; Trip motivation; travel party size and gender-age composition; main and secondary places of stay; Accommodation type; trip organization; activities; trip information source. Expenditure: total per party size; cost and composition of the package (if any); cost per item of the package (if any); expenditure in accommodation, food and beverage, transportation, cultural activities, tour, shopping, other.</td></tr></table>

Please cite this article as: A. Abbruzzo, et al., Scad-elastic net and the estimation of individual tourism expenditure determinants, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.06.003

The sample is mainly composed of Argentinians (61.23%), Uruguayans (15,71%) and Brazilians (12.77%), who are nearly all used to self-organize their trip (97.14%). About 87% of visitors is resident in the surrounding areas of Uruguay in Argentina (71.98%) and Brazil (14.39%). This may explain the high number of repeat visitors (see also [13]): only 5.26% come for the <sup>fi</sup>rst time, whereas 49.03% declare they have already visited Uruguay six times or more, including the one of the interview. Further signals related to a repetitive visiting behavior emerge from other variables such as motivation of the trip (leisure is the main one with 59.45%, but 24.26% come to meet their families), and main accommodation facilities (friends or family's house – 33.07% – is second after hotels or hostels — 42.43%). In addition, the main mean of transportation to enter the country is maritime (43.30%), which supports the idea of the importance of tourism from neighbor countries as for Argentinians crossing Riode la Plata river. Montevideo (37.14%), followed by Punta del Este (25.63%) and a set of inland places (16.16%) are the three main destinations.

## 4.2. Variables

Response variable is total expenditure per capita per day in USD. The boxplot of Fig. 1 shows that the distribution of the original levels is asymmetric. Also, there are relatively few values of expenditure that are greater than \$300. Therefore we excluded those observations that reported values exceeding this threshold. This reduced the sample to 8453 units.

The detailed composition of the 27 explanatory variables is reported in Appendix A. Note that, since each categorical variable with k levels is transformed in k dichotomous variables, the overall number of explanatory variables is 114. Unfortunately important characteristics were not collected. These include gender and age, two classic variables of individual consumption analysis, which however appeared to be infrequently related to spending [12]. But among all, the exclusion of income is crucial as economic theory suggests that it is the basic determinant of consumptions.

Due to the low development of economic theory in the <sup>fi</sup>eld of individual spending behavior in tourism, the framework we will adopt to formulate hypotheses on the impact of independent variables is based on the review by [12]. In that work authors resume the frequency each category of variables resulted to be signi<sup>fi</sup>cant from the previous empirical studies. For more details the interested reader can consult the references reported therein. The hypotheses we formulate on each variable are the following ones.

Total Expenditure  
![](/api/attachments/ZNR5U35J/fulltext/images/8b3c72822c71e8d8c45fc731ef9302a3fb023f27bed5930a991297ff8e5f401c.jpg)  
Fig. 1. Boxplot of the total expenditure per person per day, USD.

## H1. Nationality and country of residence

The presence of Uruguayans living abroad and returning home for holiday constitutes a main characteristic of tourism in the country [13]. Therefore we hypothesize that they have a signi<sup>fi</sup>cant but negative impact on total spending, in particular due to a lower expenditure in accommodation and the possibility to be hosted by local people or stay at their own houses. For what concerns other nationalities and countries, we expect their role not to be signi<sup>fi</sup>cant as the previous evidence seems to indicate. The inclusion of both these two highly correlated variables is unusual in the tourism literature, but of course this is possible because of the adopted model.

## H2. Highest educational level attained

Education was not found to be a signi<sup>fi</sup>cant driver of tourist expenditure by the majority of the previous papers. Therefore we expect the related dummy variables to be dropped, or at most to be signi<sup>fi</sup>cant only partly.

## H3. Occupation

Also this variable was found to be infrequently related to spending. However, due to the absence of income in the dataset, it might be expressive of wealth levels.

## H4. Trip motivation and elements of satisfaction/dissatisfaction

The majority of the previous studies found that psychographic variables are not signi<sup>fi</sup>cantly related to spending. We assume this for motivations. For what concerns speci<sup>fi</sup>c elements of satisfaction or dissatisfaction with the trip such hypothesis can be partly released. In fact, positive or negative feelings for some aspects of the trip can stimulate the attitude to spending.

## H5. Activities

‘Things to do while at a destination’ have not found frequent con<sup>fi</sup>rmatory evidence about their signi<sup>fi</sup>cant role for spending. This happens because not all activities require a ‘price’ to pay, beyond the fact that they would not reveal a particular spending behavior. However, in principle some of them can be thought to be directly related to spending, such as shopping.

## H6. Main information source for the trip

In the previous papers the kind of information source for the trip has been found to be very poorly related to spending. However this evidence can be questioned in a country like Uruguay, where repeat tourism has noticeable dimensions. Accordingly we can hypothesize that the previous experience of repeaters about the country, which undoubtedly affects the need of not using external information sources, has signi<sup>fi</sup>cant impact on expenditure.

## H7. Trip organization

This is one of the elements that was found to be frequently related to spending. Consistently, we assume that there exists a signi<sup>fi</sup>cant relationship. Speci<sup>fi</sup>cally this could happen for the purchase of tourist packages, which is expected to be more expensive than self organization.

## H8. Mean of transportation to enter the country

Literature found that the type of mean of transportation has been signi<sup>fi</sup>cantly linked to spending in the majority of the papers. We suppose that this occurs also for Uruguay. In particular, as [1] report, tourists coming from neighbor countries are the majority and use to take relatively cheap transportations such as road and maritime. On the contrary, international tourists from other countries make use of air transport that is a relatively more expensive one. In this sense, we might expect a higher and positive impact on spending by this latter category of tourists.

## H9. Main destination

The place where tourists stayed longer was estimated as signi<sup>fi</sup>cant element in<sup>fl</sup>uencing spending by most of the literature. Accordingly we suppose that such territorial effect exists, and it is positive for the most touristic places as Montevideo and Punta del Este.

## H10. Loyalty

Repeat visit was not found to be signi<sup>fi</sup>cantly related to spending. We also assume this hypothesis.

## H11. Accommodation type

The majority of papers found signi<sup>fi</sup>cant relationship of this variable with spending. Consistently we adopt this empirical <sup>fi</sup>nding as a hypothesis, and assume that spending increases with the expensiveness of the accommodation type.

## H12. Time

The dataset reports the time when the interview was held. Since people are interviewed while exiting the country, we can mean it as time of the holiday. For the latter factor, literature found signi<sup>fi</sup>cant relationship with spending. We then hypothesize seasonal effects in spending.

## H13. Travel party size

[12] note that most of the studies using per capita expenditure as response variable found signi<sup>fi</sup>cant negative relationship with party size. Accordingly we assume that the signi<sup>fi</sup>cant effect on spending decreases with the rise of people in the travel group.

## 5. Results

Selection of the tuning parameters $\aleph _ { 1 }$ and $\lambda _ { 2 }$ was the <sup>fi</sup>rst step of estimations. To this end, we built a grid of values with ten equidistant values for $( 0 . 0 1 , . . . 0 . 9 9 )$ and 100 values for $\lambda _ { 1 } \in ( - 4 , 4 )$ on the logarithm scale. Consistently with what emerged from cross-validation, we observed that smaller cross validation errors (cve) were obtained for the values of $\lambda _ { 2 }$ between 0.88 and 0.99. Then the second step was to select a <sup>fi</sup>nest grid of $\lambda _ { 2 } \in ( 0 . 8 8 , 0 . 9 9 ) _ { s s } .$ . We chose $\aleph _ { 2 } = 0 . 9 8$ which in our opinion was the best compromise between parsimony and minimization of the cve.

Fig. 2 shows the cross validation for $\aleph _ { 2 } = 0 . 9 8$ and $\lambda _ { 1 } \in ( - 3 . 3 , 3 . 3 )$ on the logarithm scale. For every combination of cve and log $\left( \aleph _ { 1 } \right)$ – dots – vertical segments represent approximately 68% con<sup>fi</sup>dence intervals. Every value of log $\aleph _ { 1 }$ corresponds to a number of variables to select. From our estimations the minimum cve is equal to 1230 – horizontal continuous line – and suggests log $( \lambda _ { 1 } ) = - 0 . 7 3 - \tt v e r t i c a$ l dotted line – where the number of signi<sup>fi</sup>cant predictors would be 61. However Fig. 2 suggests that a more parsimonious model can be chosen. In fact the horizontal line of the minimum cve falls also within the error bars of lower numbers of variables. Accordingly we select log $( \lambda _ { 1 } ) = 0 . 0 9$ that is $\lambda _ { 1 } = 1 . 1 0$ , which corresponds to 33 variables. Note that with the original log $( \lambda _ { 1 } ) = - 0 . 7 3$ we would have $R ^ { 2 } = 0 . 5 4$ and standard deviation is 35.075. Selecting log $( \lambda 1 ) = 0 . 0 9$ leads to $R ^ { 2 } = 0 . 5 1$ and standard deviation of 35.22, which are both very close to the ones of log $( \Lambda _ { 1 } ) = - 0 . 7 3 .$

![](/api/attachments/ZNR5U35J/fulltext/images/0ed0874a7819d09d9f77cf5edc9f8691c16de9a1acfb7a9d75a3be2188c67895.jpg)  
Fig. 2. Cross validation error (cve) and error bars representing approximate 68% con<sup>fi</sup>- dence intervals for $\aleph _ { 2 } = 0 . 9 8$ and a range of values of $\lambda _ { 1 } .$ The horizontal axis represents the range of values for λ on a logarithm scale. The gray vertical line indicates the point were cross validation error was minimized. The number of selected variables can be read on the top of the figure for each $\aleph _ { 1 }$

Once the number of variables is selected, the next step is to identify the variables to include in the analysis. In order to do this, it is useful to refer to path diagrams like the one reported in Fig. 3. To avoid confusion variable's name of each path is not reported in the <sup>fi</sup>gure. However the plot can be read as follows. The graph reports information on how many variables correspond to every value of λ (x-axis), whereas the value of coef<sup>fi</sup>cients can be read on the y-axis. In the leftmost part of the graph, in correspondence of very high values o $\mathrm { \dot { \alpha } } _ { \mathrm { \dot { \alpha } } }$ (almost 30) all coef<sup>fi</sup>cients have a value of zero, and the model to choose would take into account only the intercept. As we move rightward $\aleph _ { 1 }$ decreases, and the number of variables to include increases. When it becomes equal, say, to 25 we observe that a vertical line passing through $\Lambda _ { 1 } = 2 5$ would cross only one of the displayed paths, and speci<sup>fi</sup>cally in the part of the graph

![](/api/attachments/ZNR5U35J/fulltext/images/854e936b56b6539e5c5eea0e8e7d59aea20a5bf7573e07e39cf60ae35b94a39b.jpg)  
Fig. 3. Path of regression coef<sup>fi</sup>cients.

Please cite this article as: A. Abbruzzo, et al., Scad-elastic net and the estimation of individual tourism expenditure determinants, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.06.003

where positive β's are reported. This increasing path corresponds to Punta del Este as main destination of the trip. This way, putting for instance $ \lambda _ { 1 } = 1 5$ we would select 2 variables both with positive coef<sup>fi</sup>- cients. Setting $\lambda _ { 1 } = 1 . 1 0$ as in the vertical line of Fig. 3 that is the value we found previously from analyzing Fig. 2, we <sup>fi</sup>nd the 33 variables we were searching for as well as their coef<sup>fi</sup>cients. Of course, as λ tends to become zero all 144 original variables would have been selected. The list of selected variables as well as their coef<sup>fi</sup>cients' estimated values is reported in Tables 2 and 3, respectively for positive and negative values. The labels of each variable are reported in Appendix A. For every coef<sup>fi</sup>- cient bootstrapped standard errors are also estimated, although it can be noted that they are too ‘optimistic’ (i.e., tighter) than what we would expect from OLS. It can be also seen that satisfaction with the prices and casino attending in Table 2 report unusually high standard errors. However this is due to the relatively small number of people declaring satisfaction for these items.

## 5.1. Discussion

Classic regression models have serious shortcomings when groups of highly correlated predictors need to be included in the analysis. Also variable selection procedures such as stepwise can produce unstable results. The main advantage of scad-elastic net regression is twofold, inasmuch as it is able to handle multicollinearity and do model selection. The use of this methodology allowed testing of a high number of predictors, with no particular concerns about the possibility that the most correlated ones and a non-parsimonious model would provide misleading estimates. Indeed, the approach introduces some bias in the estimates. However the other component of the mean square error, that is the variability of the estimator, reduces and compensates such bias.

Despite these methodological advantages, some negative aspects emerge. For instance, the choice of the two tuning parameters can be problematic. Alternative Bayesian approaches avoid this problem and produce posterior distributions for the parameters. In this sense, further research could investigate the Bayesian approach for the sake of comparing it with the penalized regression, in the context of the individual tourist expenditure.

Overall, estimation and selection procedures lead to results that are consistent with the hypothesis we made on each variable. They point out the prominent role of accommodation facilities in predicting the levels of individual per day expenditure. The highest coef<sup>fi</sup>cients correspond to the most expensive accommodation types, that is staying at <sup>fi</sup>ve (\$35.58) and four (\$26.43) stars hotel.

Table 2  
Positive regression coef<sup>fi</sup>cients and bootstrapped standard errors.

<table><tr><td>Variables</td><td> $\hat{\beta}$ </td><td> $\text{se}(\hat{\beta})$ </td></tr><tr><td>(Intercept)</td><td>51.06</td><td>7.48</td></tr><tr><td>LocPrinc_PuntaEste</td><td>48.77</td><td>2.12</td></tr><tr><td>AccomType_Hotel5</td><td>35.58</td><td>4.15</td></tr><tr><td>AccomType_Hotel4</td><td>26.43</td><td>1.62</td></tr><tr><td>TripOrganization_Pack-Abroad</td><td>17.21</td><td>9.97</td></tr><tr><td>N_group_1</td><td>17.00</td><td>1.28</td></tr><tr><td>Satisfaction_Casinos</td><td>15.96</td><td>19.89</td></tr><tr><td>ShoppingAct</td><td>15.14</td><td>1.98</td></tr><tr><td>TransportationUsed_Airplane</td><td>14.65</td><td>1.07</td></tr><tr><td>LocPrinc_Monte</td><td>14.49</td><td>2.10</td></tr><tr><td>TripOrganization_Pack-Uruguay</td><td>13.15</td><td>9.30</td></tr><tr><td>N_group_2</td><td>12.72</td><td>1.01</td></tr><tr><td>AccomType_Own-House</td><td>10.66</td><td>3.51</td></tr><tr><td>Time_4</td><td>7.58</td><td>1.94</td></tr><tr><td>AccomType_Apart-Hotel</td><td>5.37</td><td>4.01</td></tr><tr><td>Satisfaction_Punta_del_Este</td><td>3.75</td><td>3.96</td></tr><tr><td>TripInformation_Personal Experience</td><td>3.61</td><td>2.87</td></tr><tr><td>N_group_3</td><td>1.55</td><td>1.24</td></tr><tr><td>Satisfaction_Prices</td><td>0.78</td><td>15.35</td></tr><tr><td>Occupation_Employer</td><td>0.36</td><td>0.77</td></tr></table>

## Table 3

Negative regression coef<sup>fi</sup>cients and standard deviation estimated with bootstrap.

<table><tr><td>Variables</td><td> $\hat{\beta}$ </td><td>sd( $\hat{\beta}$ )</td></tr><tr><td>AccomType_House-Relatives</td><td>-23.67</td><td>1.11</td></tr><tr><td>AccomType_Camping</td><td>-22.04</td><td>0.00</td></tr><tr><td>AccomType_Friends/Family</td><td>-21.81</td><td>0.08</td></tr><tr><td>AccomType_Hotel2</td><td>-18.67</td><td>0.08</td></tr><tr><td>LocPrinc_Inland</td><td>-8.35</td><td>0.08</td></tr><tr><td>Time_3</td><td>-3.27</td><td>0.48</td></tr><tr><td>TripInformation_Internet</td><td>-2.95</td><td>0.81</td></tr><tr><td>Occupation_Student</td><td>-2.48</td><td>0.47</td></tr><tr><td>Degree_Primary-Secondary</td><td>-2.07</td><td>0.00</td></tr><tr><td>LocPrinc_betwPE_Monte</td><td>-1.79</td><td>0.22</td></tr><tr><td>Dissatisfaction_Prices</td><td>-1.46</td><td>0.04</td></tr><tr><td>Occupation_Retired</td><td>-1.03</td><td>0.24</td></tr><tr><td>CongressAct</td><td>-0.74</td><td>0.35</td></tr><tr><td>Nationality_Uruguay</td><td>-0.72</td><td>7.48</td></tr></table>

These high values seem to absorb the information related to the high price of these structures from individual expenditure. But also those who stay at their own houses impact positively on expenditure (\$10.66), as well as staying in Apart-Hotels (\$5.37). Negative impact on spending is instead reported by relatives' houses (−\$23.67) or friends/family (−\$21.81), as well as camping (−\$22.04) and twostarred hotels (−\$18.67).

From these early results, this could appear as expected only partially. After all, together with transportation, accommodation is usually the most in<sup>fl</sup>uential item of the total expenditure on tourism goods. Of course, this can explain why facilities such as four and <sup>fi</sup>ve stars hotel present a highly positive impact, whereas staying at two stars hotels, friends or relatives' house and camping present negative coef<sup>fi</sup>cients. But the average daily price does not suf<sup>fi</sup>ce to explain the empirical evidence of a positive impact of staying at own houses. The latter variable was not used frequently in the literature, and results do not provide the same indications. [32] found evidence about the positive in<sup>fl</sup>uence of staying at own house on spending. Instead, [26] <sup>fi</sup>nd it as non signi<sup>fi</sup>cant. Indeed, in this speci<sup>fi</sup>c case study it is indicative of the positive impact of second dwellings for tourism in Uruguay [13]. Places like Punta del Este are characterized by a high presence of second dwellings that are owned also by foreign tourists, especially those residing in neighbor countries like Argentina and Brazil. Thus, owners of second houses for holidays tend to spend more than the ‘average’ tourist. This could be ascribed to the relatively higher income of such owners. Also the maintenance costs for these accommodation facilities are high and can justify the higher levels of expenditure. In any case, what is indicative is that encouraging tourism for second dwellings does not mean to favor less remunerative forms of tourism. Rather, it seems to establish a process that may bring constant revenues to territories.

The high presence of owners of second dwellings, as well as the closeness to metropolitan areas of other countries such as Buenos Aires in Argentina, brings a high number of tourists to repeat the visit to Uruguay [13]. Nevertheless, what emerges from the estimations is very peculiar. In general, none of the six regressors related to the repeat visit is signi<sup>fi</sup>cantly related to spending. However, a positive impact to expenditure comes from those who had the previous personal experience about the country. Personal experience in fact increases average spending by \$3.61, whereas those who gathered information from the internet for their trip tend to decrease their spending levels by −\$2.95. In this context, given other variables Uruguayans living abroad seem to take advantage of their knowledge in order to spend less than the average (−\$0.72). This may indicate that the experienced tourist makes a ‘qualitative’ selection of items to purchase, rather than taking advantage of the past experience for the sake of saving money. Instead, internet appears to be as an information source for those who want to spend less. Together with what was already commented, this may be in favor of suggesting that direct experience encourages the amount of spending more than mediated information from internet. These variables were already included in very few previous studies. Both were reported by [39], who found positive sign not only for self experience, but also for internet. [17] adopt a somehow similar questionnaire item where the respondent declared that no information for the trip was needed, which was found not to be signi<sup>fi</sup>cant. In a country where repeat tourism has a prominent importance, it is noteworthy to emphasize that the previous experience had signi<sup>fi</sup>cant importance for expenditure than the recording of past experience of the place. Of course this testing was possible due to the methodology we used, inasmuch as the two variables are highly correlated. This aspect can be a good starting point about items to investigate with future surveys and research, in order to proxy loyalty.

In general, one might argue that results about purchasing behaviors is affected by incompleteness of information about wealth levels. To overcome these limitations, occupation has been used as a proxy of income. However, results about the in<sup>fl</sup>uence of certain types of occupation (i.e., employers, students, retired) are partially consistent with the use of occupation as proxy for wealth. In particular, employers show a slightly positive effect (\$0.36), whereas negative one on spending is reported by students (−\$2.48) and retired (−\$1.03). Low education levels are also negatively related (−\$2.07).

Another aspect of interest regards the main place of stay. Results sketch a sort of map of the territory in terms of economic impact. Staying at Punta del Este, the worldwide known beach resort, increases the average spending by the highest estimated amount (\$48.77). Such effect is much higher than staying in Montevideo, the capital city, which is worth \$14.49. In addition, those who declare to be satis<sup>fi</sup>ed with staying at Punta del Este spend on average \$3.75 more than others. A negative effect is instead reported by those who spent their vacation in coastal places between Punta del Este and Montevideo (−\$1.79), or in inland places (−\$8.35). Undoubtedly, this distinction between areas emerges because of the importance of the most touristic areas such as Punta del Este and Montevideo. But at the same time, the significance of other two areas, though with a negative sign, can suggest to design tourism development policies consistently with the needs and characteristics of territories. Also, the presence of seasonal effects in spending constitutes an important indication for stakeholders for the sake of maximizing the economic impact of tourism. The latter emerges for the third (−\$3.27) and fourth (\$7.58) quarters, corresponding respectively to winter and spring.

For what concerns the ‘logistics’ of the trip, the purchase of a tour package, either ‘outside’ (\$17.21) or ‘in’ (\$13.15) Uruguay leads to a signi<sup>fi</sup>cantly higher average expenditure. As already stressed by research hypothesis, such phenomenon can be ascribed perhaps to the additional fees that tour operators require from each tourist, compared to the selforganized trip.

Expectedly, per capita per day expenditure increases with the decrease of number of people in the travel party. Travelling alone raises an average expenditure of \$17.00. This number decreases for couples (\$12.72), and lowers further for groups made by three people (\$1.55).

People that entered Uruguay via airplane constitute the segment that spent signi<sup>fi</sup>cantly more than others (\$14.65). Among the activities, the pro<sup>fi</sup>le of high spenders is associated with the attendance of casinos and positive satisfaction with them (\$15.96). Similar effect is recorded by doing shopping (\$15.14). Those who enter Uruguay for attending conferences have instead a slightly negative impact (−\$0.74).

It is interesting to note that the sample signi<sup>fi</sup>cantly splits into two about the opinion on price levels as positive or negative. However those who reveal a negative opinion (−\$1.46) have greater incidence in absolute terms than those who declare a positive one (\$0.78).

individual tourism expenditure. Empirical <sup>fi</sup>ndings concerned data from a 2010 survey on incoming tourists to Uruguay. The use of the scad-elastic net had the advantage to test the high number of variables that was present in the dataset. The model was able to handle even the most correlated ones, such as nationality and residence. In addition, proper selection of the signi<sup>fi</sup>cant ones was made. Of course, this approach is alternative to the one based on economic models, which tests a set of regressors with no exclusion of signi<sup>fi</sup>- cant variables.

Results were consistent with research hypotheses. Accommodation facilities reported a prominent role in predicting the levels of individual per day expenditure. The positive and signi<sup>fi</sup>cant impact of staying at own houses has to be remarked. Second holiday dwellings are in fact a very common phenomenon in the country. This evidence was only found in one previous work. Indeed, it encourages policymakers to promote the second housing investment, which is likely to generate positive economic returns over the time.

This paper introduced the use of penalized regression approaches, and speci<sup>fi</sup>cally of scad-elastic net, to assess the determinants of

Despite the high number of repeat visitors, the mere number of past visitations has no signi<sup>fi</sup>cant in<sup>fl</sup>uence to the levels of individual expenditure. Rather, positive impact is the one of the more general categories of ‘experienced’ tourist, who declares that the main source of information is her/his past experience. Once more, we remark that the testing of both variables was possible to the characteristics of the adopted. Number of previous visits, or rather whether a visitor has been to a place or not, has been a classical way to survey loyalty [10]. In a country where repeat tourism accounts for a very high number of tourists, this <sup>fi</sup>nding leads one to think about the importance of experience about places, rather than the mere ‘numeric’ loyalty, in in<sup>fl</sup>uencing spending patterns. Indeed, this can be an interesting topic for the future research.

Other evidence concerned the spatial and time distribution of spending. The <sup>fi</sup>rst one comes from a signi<sup>fi</sup>cant difference of the impact of expenditure among areas. This can suggest designing of ad hoc territorial policies for tourism that would maximize the economic impact, by opportune territorial distribution of infrastructures, facilities and activities. In addition, seasonal effects matter in two out of four quarters of the year.

This attempt to apply the penalized regression model in tourism is indeed encouraging. Results partially con<sup>fi</sup>rm what the previous works already pointed out. However the novel evidence that emerged may provide practical indications in order to drive tourism operators' policies.

Future research can extend the application to other comparable datasets, for the sake of testing whether the selection mechanism operates in such a way that the same elements emerge as signi<sup>fi</sup>cant explanatory variables. Moreover, constant empirical evidence about the role of certain variables can be of support also to economic theory.

## Acknowledgment

This research was supported by the Autonomous Province of Bolzano (Italy) project Le attrazioni culturali e naturali come motore dello sviluppo turistico. Un'analisi del loro impatto economico, sociale e culturale, and by the Free University of Bolzano (Italy) projects Determinants of tourist expenditure: theory and microeconometric models and Tourism and economic growth: the role of transportations and spatial contiguity. A preliminary version of this paper was presented at the TCVT2 2013 Workshop — Tourists as Consumers, Visitors, Travellers, Brunico, Italy, June 2–4.

## 6. Conclusions

## References

[1] A. Abbruzzo LG. Brida R. Scuderi Determinants of individual tourist expenditure as a network: empirical <sup>fi</sup>ndings from Uruguay, Tourism Management (2013) http://dx.doi.org/10.1016/i.tourman,2014.01.014

Please cite this article as: A. Abbruzzo, et al., Scad-elastic net and the estimation of individual tourism expenditure determinants, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.06.003

## Appendix A. List of used variables and their modalities. Semicolons separate modalities

<table><tr><td>Label</td><td>Description</td><td>Categories</td></tr><tr><td>Nationality</td><td>Nationality</td><td>Argentina; Brazil; Uruguay; Oth. South America; Oth.</td></tr><tr><td>Residence</td><td>Country of residence</td><td>Argentina; Brazil; Oth. South America; Oth.</td></tr><tr><td>Degree</td><td>Highest educational level attained</td><td>Primary/secondary;Univ. not compl.; Univ. compl.; Oth.</td></tr><tr><td>Occupation</td><td>Occupation</td><td>Employer, merchant, industrialist, farmer, businessman; Administrative employee,cashier, salesperson, banking, public employee; Skilled worker, vehicle driver, craftsman;Professional, technician, teacher, artist, journalist, customs broker; Retired; Student; Oth.</td></tr><tr><td>Motivation</td><td>Trip motivation</td><td>Leisure; second house; business; study; visit relatives; Oth.</td></tr><tr><td>BusinessAct</td><td>Activity: business</td><td>Dichotomous: yes/no</td></tr><tr><td>ParentalAct</td><td>Activity: visited relatives</td><td>Dichotomous: yes/no</td></tr><tr><td>CulturalAct</td><td>Activity: cultural</td><td>Dichotomous: yes/no</td></tr><tr><td>SportAct</td><td>Activity: sport</td><td>Dichotomous: yes/no</td></tr><tr><td>TourismAct</td><td>Activity: tourism</td><td>Dichotomous: yes/no</td></tr><tr><td>NaturalisticAct</td><td>Activity: vis. naturalistic pl.</td><td>Dichotomous: yes/no</td></tr><tr><td>BeachAct</td><td>Activity: beach</td><td>Dichotomous: yes/no</td></tr><tr><td>ShoppingAct</td><td>Activity: shopping</td><td>Dichotomous: yes/no</td></tr><tr><td>MuseumAct</td><td>Activity: vis. museum(s)</td><td>Dichotomous: yes/no</td></tr><tr><td>HistoricalAct</td><td>Activity: vis. historical pl.</td><td>Dichotomous: yes/no</td></tr><tr><td>CongressAct</td><td>Activity: attended a congress</td><td>Dichotomous: yes/no</td></tr><tr><td>OthersAct</td><td>Activity: other</td><td>Dichotomous: yes/no</td></tr><tr><td>TripInformation</td><td>Main source of information</td><td>Travel agency; friends; internet; personal experience; Oth.</td></tr><tr><td>TripOrganization</td><td>How the trip was organized</td><td>On tourist&#x27;s own; package purchased in Uruguay; package purchased abroad</td></tr><tr><td>TransportationUsed</td><td>Mean of transportation used to enter Uruguay</td><td>Airplane; car; bus/coach;Land transportation, oth.;Maritime transportation, other; Oth.</td></tr><tr><td>Label</td><td>Description</td><td>Categories</td></tr><tr><td>LocPrinc</td><td>Main destination</td><td>Punta del Este; Montevideo; place between Punta del Este and Montevideo; place in frontof Buenos Aires; Punta del Este west seashore; Inland place</td></tr><tr><td>N_Visit</td><td>Loyalty: number of past visits</td><td>0; 1; 2; 3; 4; &gt;4</td></tr><tr><td>AccomType</td><td>Typology of accommodation</td><td>Friends/family; hotels 1*, 2*, hostel; hotel 3*; hotel 4*; hotel 5*; own house; rented house;camping; aparthotel; bungalow; relatives&#x27; house; Oth.</td></tr><tr><td>Time</td><td>Quarter of the interview</td><td>1: First; 2: second; 3: third; 4: fourth</td></tr><tr><td>N_group</td><td>Travel party size</td><td>1; 2; 3; 4; 5; ≥6</td></tr><tr><td>Satisfaction</td><td>Main element of satisfaction</td><td>Everything; people; safety; coast; food; casinos; Punta del Este; Oth. tourist areas;handicraft; architecture; landscapes; prices; Oth.</td></tr><tr><td>Dissatisfaction</td><td>Main element of dissatisfaction</td><td>Prices; roads; road signs; public services; nothing; infrastructures; lack of entertainment;hygiene; safety; taxis; traffic; road services; care on services; Corte de puentes; Oth.</td></tr></table>

[2] E. Aguil Perez, C. Juaneda Sampol, Tourist expenditure for mass tourism markets, Annals of Tourism Research 3 (2000) 624–637.

[3] J. Alegre, M. Cladera, Tourist expenditure and quality: why repeat tourists can spend less than first-timers Tourism Economics 3 (2010) 517–533

[4] J. Alegre, S. Mateo, L. Pou, An analysis of households' appraisal of their budget constraints for potential participation in tourism, Tourism Management 1 (2010) 45–56.

[5] A. Bilgic, W.J. Florkowski, J. Yoder, D.F. Schreiner, Estimating <sup>fi</sup>shing and hunting leisure spending shares in the United States, Tourism Management 4 (2008) 771–782.

[6] L. Breiman, Heuristics of instability and stabilization in model selection, The Annals of Statistics 6 (1996) 2350–2383.

[7] P. Breheny, J. Huang, Coordinate descent algorithms for nonconvex penalized regression, with applications to biological feature selection, Annals of Applied Statistics 1 (2011) 232–253

[8] J.G. Brida, D. Bukstein, N. Garrido, E. Tealde, Cruise passengers' expenditure in the Caribbean port of call of Cartagena de Indias: a cross-section data analysis, Tourism Economics 2 (2012) 431–447.

[9] J.G. Brida, M. Disegna, R. Scuderi, Visitors of two types of museums: do expenditure patterns differ? Tourism Economics 5 (2013) 1027–1047

[10] J.G. Brida, M. Disegna, R. Scuderi, The behaviour of repeat visitors to museums: review and empirical <sup>fi</sup>ndings, Quality and Quantity (2013), http://dx.doi.org/ 10.1007/s11135-013-9927-0

[11] J.G. Brida, V. Fasone, R. Scuderi, S. Zapata-Aguirre, Exploring the determinants of cruise passengers' expenditure while at ports of call in Uruguay, Tourism Economics (2013), http://dx.doi.org/10.5367/te.2013.0322 (Fast Track).

[12] J.G. Brida, R. Scuderi, Determinants of tourist expenditure: a review of microeconometric models, Tourism Management Perspectives (2013, April) 28–40.

[13] J.G. Brida, J. Pereyra, R. Scuderi, Repeat tourism in Uruguay: modelling truncated distributions of count data, Quality and Quantity 1 (2014) 475–491.

[14] D. Chhabra, Identifying annual variations in the spending behavior and economic impacts of day trippers to Sacramento, California, USA, Journal of Vacation Market ing 1 (2006) 93–98.

[15] G.I. Crouch, The study of international tourism demand: a survey of practice, Journal of Travel Research 4 (1994) 41–55.

[16] B.G.C. Dellaert, Tourists' Valuation of Other Tourists' Contributions to Travel Websites, in: D.R. Fesenmaier, S. Klein, D. Buhalis (Eds.), Information and Communication Technologies in Tourism, Springer-Verlag, Wien, 2000, pp. 293–302.

[17] S. Dolnicar, G.I. Crouch, T. Devinney, T. Huybers, J.J. Louviere, H. Oppewal, Tourism and discretionary income allocation. Heterogeneity among households, Tourism Management 1 (2008) 44–45

[18] B. Efron, T. Hastie, I. Johnstone, R. Tibshirani, Least angle regression, The Annals of Statistics 2 (2004) 407–451

[19] J. Fan, R. Li, Variable selection via nonconcave penalized likelihood and its oracle properties, Journal of the American Statistical Association 456 (2001) 1348–1360.

[20] A.E. Hoerl, R.W. Kennard, Ridge regression: biased estimation for nonorthogonal problems, Technometrics 1 (1970) 55–67.

[21] S.C.S. Jang, S. Ham, A double-hurdle analysis of travel expenditure: baby boomer seniors versus older seniors, Tourism Management 3 (2009) 372–380.

[22] E. Kastenholz, Analysing determinants of visitor spending for the rural tourist market in North Portugal Tourism Economics 4 (2005) 555–569

[23] S. Kisilevich, D. Keim, L. Rokach, A GIS-based Decision Support System for Hotel Room Rate Estimation and Temporal Price Prediction: The Hotel Brokers' Context Decision Support Systems, 2013. 1119–1133

[24] M. Kozak, An analysis of tourist spending and its determinants, Anatolia 2 (2001) 196–202.

[25] M. Kruger, M. Saayman, S.M. Ellis, Determinants of visitor expenditure at the Aardklop National Arts Festival Event Management 2 (2010) 137–148

[26] C. Laesser, G.I. Crouch, Segmenting markets by travel expenditure patterns: the case of international visitors to Australia, Journal of Travel Research 4 (2006) 397–406

[27] C.K. Lee, T. Var, T.W. Blaine, Determinants of inbound tourist expenditures, Annals of Tourism Research 3 (1996) 527–547.

[28] A.A. Lew, P.T. Ng, Using quantile regression to understand visitor spending, Journal of Travel Research 10 (2011) 1–11.

[29] Q. Li, N. Lin, The Bayesian elastic net, International Society for Bayesian Analysis 1 (2010) 151–170.

[30] C. Lim, Review of international tourism demand models, Annals of Tourism Research 4 (1997) 835–849

[31] Ministerio de Turismo y Deporte, Bases de datos encuestas de turismo receptivo 2010, http://www.turismo.gub.uy/estadisticas/item/385-bases-de-datos 2011 Accessed 15 December 2011.

[32] J.L. Nicolau, F.J. Más, Heckit modelling of tourist expenditure: evidence from Spain, International Journal of Service Industry Management 3 (2005) 271–293.

[33] H. Nysveen, P.E. Pedersen, An exploratory study of customers' perception of company web sites offering various interactive applications: moderating effects of customers' Internet experience, Decision Support Systems 137–150 (2004).

[34] M. Saayman, A. Saayman, Sociodemographics and visiting patterns of arts festival in South Africa, Event Management 4 (2006) 211–222.

[35] M. Saayman, A. Saayman, Determinants of spending: an evaluation of three majo sporting events, International Journal of Tourism Research 2 (2012) 124–138.

[36] Q. Shambour, J. Lu, A trust-semantic fusion-based recommendation approach for e-business applications, Decision Support Systems 768–780 (2012).

[37] D. Schniederjans, E.S. Cao, M. Schniederjans, Enhancing <sup>fi</sup>nancial performance with social media: an impression management perspective, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2012.12.027.

[38] H. Song, G. Li, Tourism demand modelling and forecasting — a review of recent research, Tourism Management 2 (2008) 203–220.

[39] B. Svensson, P. Moreno, D. Martín, Understanding travel expenditure by means of market segmentation, Service Industries Journal 10 (2011) 1683–1698.

[40] C. Thrane, E. Farstad, Domestic tourism expenditures: the non-linear effects of length of stay and travel party size, Tourism Management 1 (2011) 46–52.

[41] R. Tibshirani, Regression shrinkage and selection via the Lasso, Journal of the Royal Statistical Society, Series B (Statistical Methodology) 1 (1996) 267–288.

[42] C.Y. Tsai, S.H. Chung, A personalized route recommendation service for theme parks using RFID information and tourist behavior, Decision Support Systems 514–527 (2012).

[43] T.J. Tyrrell, R.J. Johnston, Assessing expenditure changes related to welcome center visits, Journal of Travel Research 1 (2003) 100–106.

[44] R.O. Weagley, E. Huh, Leisure expenditures of retired and near-retired households, Journal of Leisure Research 1 (2004) 101–127.

[45] Z. Xiang, U. Gretzel, Role of social media in online travel information search, Tourism Management 179–188 (2010).

[46] H. Zhang, J. Zhang, M. Kuwano, An integrated model of tourists time use and expenditure behaviour with self-selection based on a fully nested Archimedean copula function, Tourism Management 6 (2012) 1562–1573.

[47] H. Zou, T. Hastie, Regularization and variable selection via the elastic net, Journal of the Royal Statistical Society: Series B (Statistical Methodology) 2 (2005) 301–320.

Antonio Abbruzzo is a research assistant at University of Palermo. His main competences are in the network analysis and graphical models and in particular on model-based network inference by using penalized likelihood. He has a degree and a Ph.D. in Statistics both from University of Palermo (Italy).

Juan Gabriel Brida is an associate professor of Economics at the School of Economics and Management, Free University of Bozen-Bolzano, Italy. His research interests and expertise are in the areas of tourism economics and economic growth. He has a degree in Mathematics from the Universidad de la Republica (Uruguay) and a Ph.D. in Economics from the University of Siena.

Raffaele Scuderi is an associate professor of Economic Policy at the Faculty of Economic Sciences and Law, University of Enna “Kore”, Italy. He has a degree in Business Economics and a Ph.D. in Applied Statistics both from University of Palermo (Italy). His research interests concern tourist behavior at micro level, club convergence and economic growth.
