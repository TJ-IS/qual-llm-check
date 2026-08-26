---
otero_id: 9302
otero_key: "UYSYHYE6"
title: "Correcting Measurement Error in Regression Models with Variables Constructed from Aggregated Output of Data Mining Models"
authors: "Mengke Qiao; Ke-Wei Huang"
year: "2025"
journal: "MIS Quarterly"
doi: "10.25300/misq/2024/18026"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# CORRECTING MEASUREMENT ERROR IN REGRESSION MODELS WITH VARIABLES CONSTRUCTED FROM AGGREGATED OUTPUT OF DATA MINING MODELS<sup>1</sup>

Mengke Qiao Culverhouse College of Business, University of Alabama, Tuscaloosa, AL, U.S.A.{mqiao@ua.edu}

Ke-Wei Huang School of Computing, National University of Singapore, SINGAPORE {huangkw@comp.nus.edu.sg}

The burgeoning interest in data mining has catalyzed a proliferation of innovative techniques in extracting useful information from unstructured data sources, such as text and images in social sciences. One typical research design involves a two-stage process. In the first stage, researchers apply the classification algorithm to predict an individual-level categorical variable. In the second stage, researchers aggregate the predicted values to construct a group-level variable for further regression analysis. For example, text classification has been applied to classify whether a review is positive or negative. The predicted review sentiment is aggregated at the product level as a focal independent variable in a regression model to examine the impact of the average review sentiment on product sales. Since the first-stage classification will inevitably have errors, the aggregated variable may suffer from a measurement error in the regression analysis. Our study attempts to systematically investigate the theoretical properties of the estimation bias and introduce solutions rooted in theory to mitigate the issue of measurement error. We propose one exact solution and two approximated solutions based on the central limit theorem (CLT) and the law of large numbers (LLN), respectively. Our theoretical analysis and experimentation confirm that the consistency of regression estimators can be recovered across all examined scenarios and the approximated solutions offer a significantly reduced computational complexity compared to the exact solution. We also provide heuristic guidelines to choose one of three solutions.

Keywords: Data mining, aggregate-level regression model, measurement error, central limit theorem, law of large numbers

## Introduction

The swift advancement of data mining has led social scientists to use classification algorithms to create new variables in regression analysis. Increasingly, researchers have been proposing various novel uses of classification algorithms to construct new variables from unstructured data. For example, text classification has been applied to classify whether a review is subjective or objective (Ghose & Ipeirotis, 2011;

Ghose et al., 2012). The derived review subjectivity is employed as a focal independent variable in the regression to examine its impact on review helpfulness or product sales. Image classification is also gaining popularity. For example, image classification has been applied to classify whether the worker is male or female (Chan & Wang, 2018). The estimated gender is utilized as a focal independent variable in the regression to examine its impact on hiring outcomes.

There are typically two stages in these “hybrid studies,” which are defined as using a first-stage classification algorithm to construct the focal independent or dependent variable for second-stage regression analysis. Throughout this paper, we use the term predictive stage to refer to the first stage and the econometric stage for the second stage. More specifically, in the predictive stage, researchers apply a classification algorithm on a small set of observations with labels (labeled set) to build a classifier. This classifier is applied to the unlabeled dataset to construct a new categorical variable, such as the (predicted) sentiment of a document. In the econometric stage, this newly constructed categorical variable can be directly utilized as the focal independent or dependent variable in a regression. For example, Liu et al. (2020) classified videos based on whether they encode a high or low degree of medical information. The classified output was directly used to predict the collective engagement with the video. In this paper, this type of hybrid study is defined as the “individual-level hybrid study”, where the predictive and econometric stages are analyzed at the same unit of analysis. Yang et al. (2018) and Qiao and Huang (2021) have proposed solutions for this case. However, it is not rare in the IS literature that the unit of analysis in the predictive stage and econometric stage could be different. It is quite common to use the mean or sum of the outcome variable from the predictive stage in the econometric model of the second stage. For example, Huang et al. (2019) examined the impact of the social capital of a member on the member’s provision of informational and emotional support in online support communities in the healthcare domain. In the predictive stage, Huang et al. (2019) classified each online posting message as “informational support” or “emotional support.” In the econometric stage, the regression analysis is conducted at the member level, not at the message level. As a result, the total number of “informational support” or “emotional support” messages posted by one member was constructed to measure the support provision of one member and used as the dependent variable in the econometric stage. In other words, the sum of the output variable of the first stage (not the output variable itself) is used as the dependent variable in the regression model. This type of hybrid study is defined as the “aggregate-level hybrid study,” where the econometric stage is conducted at the aggregate level, while the predictive stage is at the individual level.

One distinct feature of hybrid studies is that the constructed variable includes classification error because the output variable from the predictive stage cannot be classified perfectly. In the econometric stage, it has been welldocumented in the econometrics literature that the measurement error of the independent or dependent variable may affect the estimation results. Yang et al. (2018) is the first paper investigating the measurement error issue in individual-level hybrid studies in the IS field. They adopted two simulation-based methods to correct the estimation bias, SIMEX, and MC-SIMEX, which can be parameterized using performance metrics from data mining models, such as error variance or the confusion matrix.

However, this problem becomes more complicated for aggregate-level hybrid studies and the solutions from the existing literature are not directly applicable due to the following reasons. In aggregate-level studies, we do not know the true values of the aggregated output variable from the prediction stage. In contrast, in individual hybrid studies, we know the true values of the individual output variable in the labeled dataset for classifier training and validation. As a result, in individual-level studies, we can quantify the measurement error model more precisely by the labeled dataset whereas, in aggregate-level studies, we can only estimate the distribution of measurement error probabilistically. For example, suppose researchers want to examine the impact of the average review sentiment on product sales. Unless the reviews of one product are all annotated, we cannot know the true values of the average review sentiment at the product level. Because in almost all hybrid studies, researchers randomly selected a small subset of reviews to be annotated, it is unlikely that we will know the labels of all reviews of one product. As a result, we need to derive a new solution for the aggregated hybrid study.

The aggregated level problem is also worthy of studying because the solutions are different when the aggregation function is mean or sum, which is equally common in the IS literature. Huang et al. (2019) is an example of the sum function. As an example of mean function, Deng et al. (2018) examined the impact of stock returns on microblog sentiment. In the predictive stage, they classified each microblog message as a “positive” or “nonpositive” message. Next, they constructed the “positive sentiment score” by the percentage of positive messages among all the messages, which was employed as the dependent variable in the regression. In other words, the mean of the first stage’s output variable is used as the dependent variable. <sup>2</sup> For ease of exposition, our paper uses the term proxy variable to refer to the predicted output label of the classification algorithm. We use the term true variable to refer to the true label predicted by the proxy variable. This study will investigate four cases. The aggregation function can be mean or sum and the aggregated variable can be used as the dependent or focal independent variable in a regression model. We will analyze the estimation bias and derive the theoretical solutions for all four cases.

The main contribution of our paper is to propose a new estimation procedure for aggregate-level hybrid studies, which is gaining popularity across social science disciplines. In the proposed solution, there are two important steps. First, researchers are recommended to train classifiers to meet several unique criteria, which are required by the “assumptions” in the econometric stage. Roughly speaking, researchers should try to minimize the correlation between the classification error and any other variables, such as the dependent variable in regression analysis. After deciding on the classifier, researchers can apply our theory-grounded solutions for aggregate-level hybrid studies to estimate the regression model. The main innovation of our method is we utilize the individual-level measurement error model and confusion matrix of each aggregated group to derive the aggregate-level measurement error model. Based on this model, we propose three solutions, including an exact solution and two approximated solutions based on the central limit theorem (CLT) and the law of large numbers (LLN). Our theoretical analysis shows that the consistency of regression estimators can be recovered in all cases studied in this paper and the time complexity of the approximated solutions is much better than the exact solution. Our study also contributes to the literature by providing theoretical analysis that quantifies the estimation bias if the researchers simply utilize the aggregated proxy variable without any correction (called the naïve approach in this paper) in the econometric stage. There are several counterintuitive findings. For example, when the mean of the proxy variable is used as the focal independent variable and the aggregation sample is large enough, the coefficient could be overestimated, which is different from the attenuation bias due to the classical measurement error in the traditional statistics literature. Finally, this paper also contributes to providing conditions under which researchers can ignore the measurement error.

The remaining paper is organized as follows. First, we provide a literature review. Next, we report a theoretical analysis of the estimation bias. Then, we report the main theoretical solutions for four cases and evaluate the proposed solutions through simulation studies and real-world applications. Our results show that our method can indeed correct the estimation inconsistency. Finally, we conclude this paper.

## Literature Review

## Aggregate-Level Hybrid Study Applications

Recently, applying supervised machine learning methods to construct variables from unstructured data has gained popularity, which has facilitated the popularity of hybrid studies in the information systems discipline (Chen et al., 2012). Abundant examples of aggregated-level hybrid studies exist in the IS literature. For example, the text label of each online review can be aggregated at the product level on ecommerce websites (Ghose & Ipeirotis, 2011; Wu et al., 2019) or at the seller level in online service marketplaces (Moreno & Terwiesch, 2014). Besides the text label, on Airbnb, the image label of each room is also aggregated at the property level (Zhang et al., 2016). Similarly, extensive examples exist in the online community literature. For example, the labels of individual online postings have been aggregated at the solver level in user support (Q&A) forums (Jabr et al., 2014), at the stock level and at the discussion thread level in online communities for investment (Gu et al., 2007, 2014), at the IT venture level in online blog platform (Aggarwal & Singh, 2013), at the brand level in the social media platform (Luo et al., 2013), at the member level in healthcare virtual support communities (Huang et al., 2019), and at the topic level in the enterprise blogosphere (Singh et al., 2014). In summary, the constructed variable from the classification algorithm can be aggregated at various higher levels depending on research contexts.

Table 1. Summary of Four Cases of Aggregate-Level Hybrid Studies

<table><tr><td></td><td>Aggregation form of the proxy variable</td><td>Example</td><td>Aggregated variable</td><td>Model</td></tr><tr><td>Case1</td><td>mean as IV</td><td>Moreno &amp; Terwiesch (2014)</td><td>Mean of comment labels</td><td>Multinomial logit model</td></tr><tr><td>Case2</td><td>sum as IV</td><td>Gu et al. (2007)</td><td>Sum of post labels</td><td>Multinomial logit model</td></tr><tr><td>Case3</td><td>mean as DV</td><td>Deng et al. (2018)</td><td>Mean of message labels</td><td>Vector autoregression</td></tr><tr><td>Case4</td><td>sum as DV</td><td>Jabr et al. (2014)</td><td>Sum of post labels</td><td>Negative binomial model</td></tr></table>

There are typically four cases of aggregate-level hybrid studies, as summarized in Table 1. In the first case, researchers utilize the mean of the individual-level constructed variable as the focal independent variable in the econometric stage. For example, Moreno and Terwiesch (2014) examined the impact of the reputation score in online service marketplaces on buyers’ and sellers’ behavior. In the predictive stage, they classified each comment received by the seller as “positive” or “negative.” Next, they defined a new variable “reputation score” of each seller by the percentage of “positive” comments among all comments. In the econometric stage, the “reputation score” was used as the focal independent variable in the main regression model. In the second case, researchers utilize the sum of the individual-level variable as the focal independent variable in the econometric model. For example, Gu et al. (2007) examined the impact of the number of quality postings of one stock on the user’s choice of online communities. In the predictive stage, they classified each posting as “noise”, “neutral” or “signal.” In the econometric stage, the count of “signal” posts for one stock was used as the focal independent variable in the econometric model. Because this paper analyzes the network effect of online communities, it makes more sense to use the sum rather than the mean as the aggregation function. The main implication is that while it seems more intuitive to use mean as the aggregation function, there exist cases where researchers have to use sum as the aggregation function for theoretical reasons. An example of the third case is Deng et al. (2018), who examined the impact of stock returns on microblog sentiment. In the predictive stage, they classified each microblog message as “positive” or “non-positive.” Next, they defined the daily “positive sentiment score” by the ratio of the number of positive messages to the total number of messages on that day. In the econometric stage, the “positive sentiment score” was used as the dependent variable in the regression model. An example of the fourth case is Jabr et al. (2014), who examined how the contribution of solvers is affected by the recognition mechanism in user support (Q&A) forums. In the predictive stage, they classified each post as a solution post or not. Next, they defined a new variable “contribution level” of each solver by the number of solution posts. In the econometric stage, the “contribution level” was the key dependent variable in the regression. In this paper, all four cases will be analyzed.

## Measurement Error of Variables in Aggregatelevel Hybrid Studies

Yang et al. (2018) and Qiao and Huang (2021) have investigated measurement error in individual-level hybrid studies in the IS field. To correct the estimation inconsistency, in their pioneering paper, Yang et al. (2018) utilized two simulation-based methods, SIMEX and MC-SIMEX, which were applied to continuous variables with additive measurement error and discrete variables with misclassification (Cook & Stefanski, 1994; Küchenhoff et al., 2006). Qiao and Huang (2021) proposed theoretical solutions to correct the misclassification bias for generalized linear models. However, the proposed methods in both papers cannot be applied in aggregate-level hybrid studies since both solutions require the aggregate-level measurement error model, which cannot be directly quantified from the labeled dataset.

The issue of measurement error has been widely studied by econometricians (Greene, 2012) and biostatisticians (Buonaccorsi, 2010). Abundant methods have been proposed to correct the estimation inconsistency due to measurement error. However, most of the existing literature has mainly focused on solutions involving researchers diagnosing the measurement error model of the mismeasured variable directly. Buonaccorsi (2010) and Carroll et al. (2006) offer detailed analyses. Little literature has analyzed the aggregated measurement error issue with a unique structure where the aggregation step can cancel out or aggravate the individuallevel measurement error. Fuller (1987) examined the measurement error issue in the independent variable when beta coefficients are different for separate groups in the data. However, this combination of grouping and measurement error is different from our setting.

## Theoretical Analysis of Estimation Bias Due to Aggregated Measurement Error

In this section, we first explain and define the required notations of our model. Next, we characterize the mean and variance of the measurement error. Then, we theoretically analyze estimation bias in the linear regression when the measurement error is ignored, as in the naïve approach widely adopted in the existing literature. Finally, we examine the impacts of measurement error in different regression models by simulation.

## Notations and Definitions

In this paper, we consider only one focal variable ${ \bar { X } } _ { i } ,$ which is the mean of the true variable $( { X } _ { i } ^ { j } )$ for the aggregated group i. $M _ { i }$ is the number of observations for aggregating to derive $\bar { X } _ { i } . X _ { i } ^ { j }$ is the true label of row j in aggregated group i. For example, if researchers wanted to examine the impact of the average review sentiment at the product level on product sales, the average review sentiment $( { \bar { X } } _ { i } )$ would be calculated based on the sentiment labels $( \boldsymbol { X } _ { i } ^ { j } )$ of all the reviews received by product i. We define the reviews received by product i as the aggregated group i. $M _ { i }$ is the total number of reviews received by product i (group i). $X _ { i } ^ { j }$ is the true sentiment label of review $j$ in product group i. The value of $X _ { i } ^ { j }$ is unknown and is predicted by the output in the predictive stage. $W _ { i } ^ { j }$ is named the proxy variable of $X _ { i } ^ { j } ,$ , which is constructed by predicted values from the classifier in the predictive stage. In hybrid studies, researchers do not know the values of $X _ { i } ^ { \bar { j } }$ (except in a small, labeled dataset for training a classifier), while $W _ { i } ^ { j }$ is known for all the records. In almost all existing hybrid studies, researchers estimated the regression model by replacing ${ \bar { X } } _ { i }$ with $\bar { W } _ { i }$ given the implicit assumption that $\bar { X } _ { i } { = } \bar { W } _ { i }$ , which does not hold in most scenarios. In this study, we define a classifier as unbiased when $\operatorname { E } ( { \bar { X } } _ { i } ) = \operatorname { E } ( { \bar { W } } _ { i } )$ for all i. Based on this view, in the existing hybrid studies, researchers imposed two strong assumptions: (1) all classifiers are unbiased and (2) $M _ { i }$ is large enough. To the best of our knowledge, none of the existing hybrid studies have discussed whether $\operatorname { E } ( { \bar { X } } _ { i } ) { = } \operatorname { E } ( { \bar { W } } _ { i } )$ for all i is a valid assumption in their empirical studies. Similarly, when the aggregation function is the sum, we define the sum of the true variable and proxy variable by $S _ { X _ { i } }$ and $S _ { W _ { i } }$

To analyze the aggregated measurement error, we need to utilize the information from the aggregate-level confusion matrix. We illustrate the confusion matrix of one aggregated group i in Table 2. Because this is only for one group of data, the total number of cases is $M _ { i } ,$ , which can be decomposed into four important numbers: true positive cases (TP), true negative cases (TN), false positive cases (FP), and false negative cases (FN). We define ℎ as the number of true positive observations. We can express all terms in Table 2 using h and three other notations $M _ { i } , { \bar { W } } _ { i }$ , and ${ \bar { X } } _ { i } .$ . With these terms, we can also express all probability terms by these four variables. For example, we define two probabilities, $\widehat { \mathrm { P r } } _ { i } ^ { \mathrm { T P } } =$ $h / M _ { i } { \bar { X } } _ { i }$ and ${ \widehat { \mathrm { P r } } } _ { i } ^ { \mathrm { F P } } = ( M _ { i } { \bar { W } } _ { i } - h ) / ( M _ { i } - { \bf \bar { M } } _ { i } { \bar { X } } _ { i } )$ . These two values are also the two axes in a typical ROC figure.

## Expected Value and Variance of Aggregated Measurement Error

Given the notations in Table $^ { 2 , }$ it is straightforward to derive the measurement error between $\bar { W } _ { i }$ and ${ \bar { X } } _ { i }$ because $\bar { W } _ { i }$ can be rewritten as a function of ${ \bar { X } } _ { i }$ as follows:

$$
\bar {W} _ {i} = \bar {X} _ {i} \times \widehat {\mathrm{Pr}} _ {i} ^ {\mathrm{TP}} + (1 - \bar {X} _ {i}) \times \widehat {\mathrm{Pr}} _ {i} ^ {\mathrm{FP}}.
$$

Subtracting both sides by ${ \bar { X } } _ { i } ,$ we can derive an expression of the measurement error as:

$$
\bar {e} _ {i} = \bar {W} _ {i} - \bar {X} _ {i} = \bar {X} _ {i} \times \left(\widehat {\mathrm{Pr}} _ {i} ^ {\mathrm{TP}} - 1\right) + (1 - \bar {X} _ {i}) \times \widehat {\mathrm{Pr}} _ {i} ^ {\mathrm{FP}}.
$$

We define the expected values of $\widehat { \mathrm { P r } } _ { i } ^ { \mathrm { T P } }$ and $\widehat { \mathsf { P r } } _ { i } ^ { \mathrm { F P } }$ by $\mathrm { E } ( \widehat { \mathrm { P r } } _ { i } ^ { \mathrm { T P } } ) =$ 1 $\overline { { \mathsf { P r } } } _ { i } ^ { \mathrm { T P } }$ and $\mathrm { E } ( \widehat { \mathrm { P r } } _ { i } ^ { \mathrm { F P } } ) { = } \overline { { \mathrm { P r } } } _ { i } ^ { \mathrm { F P } }$ . Then the expectation and variance of the measurement error can be derived as:

$$
\begin{array}{r} \mathrm{E} (\bar {e} _ {i}) = \mathrm{E} (\bar {X} _ {i}) \times \left(\overline {{\mathrm{Pr}}} _ {i} ^ {\mathrm{TP}} - 1\right) + \left(1 - \mathrm{E} (\bar {X} _ {i})\right) \times \overline {{\mathrm{Pr}}} _ {i} ^ {\mathrm{FP}}, \\ \mathrm{Var} (\bar {e} _ {i}) = \frac {\mathrm{E} (\bar {X} _ {i}) \overline {{\mathrm{Pr}}} _ {i} ^ {\mathrm{TP}} \left(1 - \overline {{\mathrm{Pr}}} _ {i} ^ {\mathrm{TP}}\right) + \left(1 - \mathrm{E} (\bar {X} _ {i})\right) \overline {{\mathrm{Pr}}} _ {i} ^ {\mathrm{FP}} \left(1 - \overline {{\mathrm{Pr}}} _ {i} ^ {\mathrm{FP}}\right)}{M _ {i}} \\ + (\overline {{\mathrm{Pr}}} _ {i} ^ {\mathrm{FN}} + \overline {{\mathrm{Pr}}} _ {i} ^ {\mathrm{FP}}) ^ {2} \mathrm{Var} (\bar {X} _ {i}). \end{array}
$$

The proof is shown in Appendix C. Following a similar logic, we can derive the expectation and variance of the error of the sum $S _ { W _ { i } }$ relative to $S _ { X _ { i } }$ conditional on $M _ { i }$ as follows

$$
\operatorname{E} \big (S _ {e _ {i}} \big) = M _ {i} \operatorname{E} (\bar {e} _ {i}), \operatorname{Var} (S _ {e _ {i}}) = M _ {i} ^ {2} \operatorname{Var} (\bar {e} _ {i}).
$$

In summary, the expectation and variance of measurement error in both cases can be fully characterized by the two proportions of TP and FP because $\operatorname { E } ( { \bar { X } } _ { i } )$ results from the nature of the dataset and is invariant to the classifier performance. Another important implication is that the expectation of the error is zero only when $\mathrm { E } ( { \bar { X } } _ { i } ) \times \left( { \overline { { \mathrm { P r } } } } _ { i } ^ { \mathrm { T P } } - \right.$ $1 ) + \left( 1 - \operatorname { E } ( { \bar { X } } _ { i } ) \right) \times { \overline { { \operatorname* { P r } } } } _ { i } ^ { \operatorname* { F P } } = 0$ . If the proportion of 0 is 50%, this expression simplifies to $\left( \overline { { \mathrm { P r } } } _ { i } ^ { \mathrm { T P } } - 1 \right) + \overline { { \mathrm { P r } } } _ { i } ^ { \mathrm { F P } } = 0$ . In other words, only when the classifier satisfies this condition for all groups will the expectation of the error be zero, and this is unlikely to happen in practice. This is one important empirical condition that has been overlooked by researchers in the literature.

## Estimation Bias Due to Aggregated Measurement Error

## Review of Estimation Bias Due to Measurement Error in the Traditional Literature

We consider a simple linear regression with only one regressor: $Y _ { i } = X _ { i } \beta + \varepsilon _ { i } . \varepsilon _ { i }$ is the error term and is independent of $X _ { i }$ . We assume that $X _ { i }$ is unobserved, and we observe $W _ { i }$ instead. Following the standard model setup in the econometrics literature, $W _ { i } = X _ { i } + e _ { i } ~ . ~ e _ { i }$ is the classical measurement error, independent of both $X _ { i }$ and $\varepsilon _ { i } .$ . Then the regression model becomes $Y _ { i } = W _ { i } \beta + \varepsilon _ { i } - e _ { i } \beta .$ . Let N denote the sample size of the dataset. If we ignore $e _ { i }$ in the regression analysis, the estimated ?? will have attenuation bias (Greene, 2012),

$$
\begin{array}{r l} & {\underset {N \to \infty} {\lim} \hat {\beta} = \frac {\mathrm{Cov} (W _ {i} \beta , W _ {i})}{\mathrm{Var} (W _ {i})} + \frac {\mathrm{Cov} (- e _ {i} \beta , W _ {i})}{\mathrm{Var} (W _ {i})} + \frac {\mathrm{Cov} (\varepsilon_ {i} , W _ {i})}{\mathrm{Var} (W _ {i})} = \beta +} \\ & {\frac {\mathrm{Cov} (- e _ {i} , W _ {i})}{\mathrm{Var} (W _ {i})} \beta = \beta - \frac {\sigma_ {e} ^ {2}}{\sigma_ {X} ^ {2} + \sigma_ {e} ^ {2}} \beta ,} \end{array}\tag{1}
$$

where $\sigma _ { X } ^ { 2 }$ and $\sigma _ { e } ^ { 2 }$ are the variance of $X _ { i }$ and $e _ { i } ,$ and $\operatorname { C o v } ( \varepsilon _ { i } , W _ { i } ) = 0$

<table><tr><td colspan="4">Table 2. Confusion Matrix for Predicted Variable</td></tr><tr><td></td><td> $X_{i}^{j}=1$ </td><td> $X_{i}^{j}=0$ </td><td>Sum</td></tr><tr><td> $W_{i}^{j}=1$ </td><td>TP (h)</td><td>FP ( $M_{i}\bar{W}_{i}-h$ )</td><td>( $M_{i}\bar{W}_{i}$ )</td></tr><tr><td> $W_{i}^{j}=0$ </td><td>FN ( $M_{i}\bar{X}_{i}-h$ )</td><td>TN (( $M_{i}-M_{i}\bar{W}_{i}$ )-( $M_{i}\bar{X}_{i}-h$ ))</td><td>( $M_{i}-M_{i}\bar{W}_{i}$ )</td></tr><tr><td>Sum</td><td>( $M_{i}\bar{X}_{i}$ )</td><td>( $M_{i}-M_{i}\bar{X}_{i}$ )</td><td> $M_{i}$ </td></tr></table>

Next, we assume $Y _ { i }$ has the classical measurement error, $y _ { i } =$ $Y _ { i } + e _ { i }$ . Then the regression model becomes $y _ { i } = X _ { i } \beta + \varepsilon _ { i } +$ $e _ { i } ,$ . In this case, if we ignore $e _ { i }$ in the regression analysis, there is no bias in the estimated coefficient (Greene, 2012),

$$
\lim _ {N \to \infty} \hat {\beta} = \frac {\operatorname{Cov} (X _ {i} \beta , X _ {i})}{\operatorname{Var} (X _ {i})} + \frac {\operatorname{Cov} (e _ {i} , X _ {i})}{\operatorname{Var} (X _ {i})} + \frac {\operatorname{Cov} (\varepsilon_ {i} , X _ {i})}{\operatorname{Var} (X _ {i})} = \beta + \frac {\operatorname{Cov} (e _ {i} , X _ {i})}{\operatorname{Var} (X _ {i})} = \beta .\tag{2}
$$

In the following sections, our focus is on analyzing the estimation bias in simple linear regression when the measurement error of the proxy variable is aggregated.

## Mean of Proxy Variable as the Focal Independent Variable

When the mean of the proxy variable is the focal independent variable, the measurement error is averaged, $\bar { e } _ { i } = \bar { W } _ { i } - \bar { X } _ { i }$ . The regression model becomes $Y _ { i } = \bar { W } _ { i } \beta + \varepsilon _ { i } - \bar { e } _ { i } \beta$ . Different from traditional literature, we further decompose $\bar { e } _ { i }$ as:

$$
\bar {e} _ {i} = \mathrm{E} (\bar {e} _ {i}) + \mu_ {i},
$$

where $\begin{array} { r } { \mathrm { E } ( \bar { e } _ { i } ) = - \left( \frac { 1 } { \overrightarrow { \mathrm { P r } } _ { i } ^ { \mathrm { T P } } - \overrightarrow { \mathrm { P r } } _ { i } ^ { \mathrm { F P } } } - 1 \right) \mathrm { E } ( \overrightarrow { W } _ { i } ) + \frac { \overrightarrow { \mathrm { P r } } _ { i } ^ { \mathrm { F P } } } { \overrightarrow { \mathrm { P r } } _ { i } ^ { \mathrm { T P } } - \overrightarrow { \mathrm { P r } } _ { i } ^ { \mathrm { F P } } } , } \end{array}$ the expectation of $\mu _ { i }$ is 0, and the variance of $\mu _ { i }$ is the variance term in the Expected Value and Variance of Aggregated Measurement Error section. The proof is shown in Appendix C.

Next, we derive the formula of estimated $\beta$ by replacing $W _ { i }$ by $\bar { W } _ { i }$ and $e _ { i }$ by $\bar { e } _ { i }$ in Equation (1),

$$
\begin{array}{r l} & {\underset {N \to \infty} {\lim} \hat {\beta} = \beta + \frac {\mathrm{Cov} (- \bar {e} _ {i} , \overline {{W}} _ {i})}{\mathrm{Var} (\overline {{W}} _ {i})} \beta} \\ & {\quad = \beta + \frac {\mathrm{Cov} (- \mathrm{E} (\bar {e} _ {i}) , \overline {{W}} _ {i})}{\mathrm{Var} (\overline {{W}} _ {i})} \beta + \frac {\mathrm{Cov} (- \mu_ {i} , \overline {{W}} _ {i})}{\mathrm{Var} (\overline {{W}} _ {i})} \beta .} \end{array}
$$

We assume that $\overline { { \mathsf { P r } } } _ { i } ^ { \mathrm { T P } }$ and $\overline { { \mathsf { P r } } } _ { i } ^ { \mathrm { F P } }$ are the same across all the aggregated groups. This assumption is also imposed in the subsequent part. Then we can remove subscript i for $\operatorname { E } ( { \bar { e } } _ { i } )$ and obtain:

$$
\begin{array}{r} \lim _ {N \to \infty} \hat {\beta} = \beta + \left(\frac {1}{\overline {{\mathrm{Pr}}} ^ {\mathrm{TP}} - \overline {{\mathrm{Pr}}} ^ {\mathrm{FP}}} - 1\right) \frac {\mathrm{Cov} (\mathrm{E} (\overline {{W}} _ {i}) , \overline {{W}} _ {i})}{\mathrm{Var} (\overline {{W}} _ {i})} \beta \\ + \frac {\mathrm{Cov} (- \mu_ {i} , \overline {{W}} _ {i})}{\mathrm{Var} (\overline {{W}} _ {i})} \beta , \end{array}
$$

where N is the sample size of the full dataset for regression.

When $M _ { i }$ is large enough, $\bar { W } _ { i }$ and $\mu _ { i }$ converge to $\operatorname { E } ( { \overline { { W } } } _ { i } )$ and 0 by the law of large numbers. Therefore, $\frac { \mathrm { C o } \overset { - } { \mathbf { v } } ( \mathrm { E } ( \overline { { W } } _ { i } ) , \overline { { W } } _ { i } ) } { \mathrm { V a r } ( \overline { { W } } _ { i } ) } = 1$ and $\begin{array} { r } { \frac { \mathrm { C o v } ( - \mu _ { i } , \overline { { W } } _ { i } ) } { \mathrm { V a r } ( \overline { { W } } _ { i } ) } = 0 } \end{array}$ . The coefficient is overestimated as follows,

$$
\lim _ {N \to \infty , M _ {i} \to \infty} \hat {\beta} = \beta + \beta \left(\frac {1}{\overline {{\mathrm{Pr}}} ^ {\mathrm{TP}} - \overline {{\mathrm{Pr}}} ^ {\mathrm{FP}}} - 1\right) = \frac {1}{\overline {{\mathrm{Pr}}} ^ {\mathrm{TP}} - \overline {{\mathrm{Pr}}} ^ {\mathrm{FP}}} \beta .
$$

In summary, when the mean of the proxy variable is used as the focal independent variable in simple linear regression, the coefficient varies with $M _ { i }$ and is overestimated by $\frac { 1 } { \overline { { \mathrm { P r } ^ { \mathrm { T P } } - \overline { { \mathrm { P r } ^ { \mathrm { F P } } } } } } }$ when $N$ and $M _ { i }$ are large enough. This result is different from the attenuation bias due to the classical measurement error of the independent variable in the existing measurement error literature in the Review of Estimation Bias Due to Measurement Error in the Traditional Literature section. The reason is that the classical measurement error $\left( \ - e _ { i } \right)$ is negatively correlated with $W _ { i } ,$ while the error of the mean of the proxy variable $( - \bar { e } _ { i } )$ is positively correlated with $\textstyle { \overline { { W } } } _ { i }$ when $M _ { i }$ is large enough.

## Mean of Proxy Variable as the Dependent Variable

When the mean of the proxy variable is utilized as $\mathrm { D V } , \bar { e } _ { i } =$ $\bar { y } _ { i } - \bar { Y } _ { i }$ . The model becomes $\bar { y } _ { i } = X _ { i } \beta + \varepsilon _ { i } + \bar { e } _ { i }$ . Next, the last term is:

$$
\bar {e} _ {i} = \mathrm{E} (\bar {e} _ {i}) + \mu_ {i},
$$

where $\mathrm { E } ( \bar { e } _ { i } ) = X _ { i } \beta \times ( \overline { { \mathrm { P r } } } \mathrm { ^ { T P } - } 1 ) + ( 1 - X _ { i } \beta ) \times \overline { { \mathrm { P r } } } ^ { \mathrm { F P } }$ conditional on $X _ { i }$ .

Finally, we derive the formula of estimated $\beta$ by replacing $e _ { i }$ with $\bar { e } _ { i }$ in Equation (2):

$$
\begin{array}{c} \lim _ {N \to \infty} \hat {\beta} = \beta + \frac {\operatorname{Cov} (\bar {e} _ {i} , X _ {i})}{\operatorname{Var} (X _ {i})} = \beta + \frac {\operatorname{Cov} (\operatorname{E} (\bar {e} _ {i}) , X _ {i})}{\operatorname{Var} (X _ {i})} + \frac {\operatorname{Cov} (\mu_ {i} , X _ {i})}{\operatorname{Var} (X _ {i})} \\ = (\overline {{\operatorname* {P r}}} ^ {\mathrm{TP}} - \overline {{\operatorname* {P r}}} ^ {\mathrm{FP}}) \beta . \end{array}
$$

The third equality results from the fact that ${ \frac { \mathrm { C o v } ( \mu _ { i } , X _ { i } ) } { \mathrm { V a r } ( X _ { i } ) } } = 0 .$ . The detailed proof for this analysis is shown in Appendix C. Therefore, when the mean of the proxy variable is used as the dependent variable in simple linear regression, the coefficient does not vary with $M _ { i }$ and is underestimated by $\overline { { \mathrm { P r } } } ^ { \mathrm { T P } } - \overline { { \mathrm { P r } } } ^ { \mathrm { F P } }$ This result is different from the no-bias results in the traditional statistics literature. The reason is that the literature assumes that the measurement error is not correlated with the independent variable, while in our case, the aggregated measurement error is negatively correlated with the independent variable. The estimation bias results for the sum of proxy variable cases have a slight difference from the mean cases, which are shown in Appendix C due to the page limit.

## Estimation Bias Simulation Results

We also used simulation to characterize how the estimation bias varies with the sample size of the aggregated group and the nature of measurement error in different regression models (including OLS, logit model, and beta-binomial model). Due to the page limit, we omitted the results, which are available upon request. The results are consistent with our theoretical analysis. Generally, the estimation bias decreases when the classification error is smaller. Moreover, when the mean or sum of the proxy variable is used as the focal independent variable, the estimation bias increases from “underestimated” to “overestimated” as the sample size of the aggregated group increases. When the mean or sum of the proxy variable is used as the dependent variable, the coefficient is underestimated and the estimation bias does not change as the sample size of the aggregated group increases.

## Theoretical Solutions

## Theoretical Solution Framework

Our method is built on the traditional probabilistic approach by using the maximum likelihood estimation (MLE) method for correcting the measurement error issue in Carroll et al. (2006). We first introduce a general solution based on this approach.

## True Model in the Econometric Stage

We denote the econometric stage’s true model by $\mathsf { P } ( Y | \bar { X } , Z ; \theta )$ which is the probability function of ?? conditional on ??̅ and ??. The most common example is logistic regression. To illustrate the flexibility of this approach, we will analyze several cases of this function, including the widely used generalized linear model (GLM). In this specification, ?? can be interpreted as the dependent variable, ??̅ can be interpreted as the focal independent variable, and ?? is the vector of the control variables. ?? is a vector of regression parameters for estimation. Testing whether ?? is zero is the objective in hybrid studies. However, in hybrid studies, researchers do not know the values of ??̅ , while $\bar { W }$ is known for all the records. Therefore, in almost all existing literature, researchers simply replace $\bar { X }$ with $\bar { W }$ in $\mathsf { P } ( Y | \bar { X } , Z ; \theta )$ and proceed with the standard estimation procedure using OLS or MLE. Our theoretical and simulation results show that this approach suffers from the measurement error problem, leading to the inconsistent estimation of ??.

## A General Solution by MLE in the Econometric Stage

The correct objective function for MLE should not be replacing ??̅ with ??̅ in $\mathsf { P } ( Y | \bar { X } , Z ; \theta )$ under the implicit assumption that ${ \bar { X } } = { \bar { W } }$ . Instead, ??̅ and other observable variables should be used to estimate the probability distribution of ??̅. The correct objective function is a weighted sum of candidates of true values of ??̅. Formally, the weight is denoted by $\mathsf { P } ( \bar { X } | \bar { W } , Z )$ , which is the probability function of ??̅, conditional on ??̅ and ?? . We define this term as the measurement error model. Empirically, this function needs to be estimated, and this study proposes three methods to estimate this probability function. To explain this issue using the simplest example, we consider a dataset with only two textual reviews for each product and use the mean of these two binary sentiment values as the focal independent variable. When we observe $\bar { W } = 1$ , we need to estimate the probability that the true mean ??̅ could be 0, 0.5, or 1. Most researchers simply “assume” ${ \bar { X } } = { \bar { W } } = 1$ with 100% probability and proceed with MLE for logistic regression. However, to correct the measurement error of ${ \bar { X } } ,$ , the correct approach is to estimate the conditional probability that ??̅ could be 0, 0.5, or 1 and use the following function for MLE:

$$
\mathrm{P} (Y | \bar {W}, Z) = \sum_ {\bar {X}} \mathrm{P} (Y | \bar {X}, Z, \bar {W}) \times \mathrm{P} (\bar {X} | \bar {W}, Z).\tag{3}
$$

Intuitively, this equation means that we compute P(??|??̅ , ??) by taking the expectation of the conditional probability function $\mathsf { P } ( Y | \bar { X } , Z , \bar { W } )$ over all possible values of ??̅. In the following discussion, the focus is on how to estimate the measurement error function $\mathsf { P } ( \bar { X } | \bar { W } , Z )$

## Case 1: Mean of Proxy Variable as the Focal Independent Variable

We first analyze the case in which the mean of the proxy variable is the focal independent variable in the generalized linear model in the econometric stage. This may be the most widely analyzed econometric model among the four cases in the existing literature. The dependent variable in the econometric stage is denoted by $Y _ { i } ,$ which is an N-by-1 vector. The unobservable independent variable is denoted by ${ \bar { X } } _ { i }$ which is the mean of the true variable for the aggregated group $i . { \bar { X } } _ { i }$ is also an N-by-1 vector. $M _ { i }$ is the number of observations for aggregating to derive $\bar { X } _ { i } . X _ { i } ^ { j }$ is the true label of row j in the predictive stage and the mean of $X _ { i } ^ { j }$ in group i is ${ \bar { X } } _ { i }$ . For example, Moreno and Terwiesch (2014) examined the impact of the reputation score in online service marketplaces on buyers’ and sellers’ behavior. The reputation score $( { \bar { X } } _ { i } )$ was defined as the average sentiment of the review comments received by seller i in previous projects. The text classification was applied at the comment level to predict the sentiment label. Next, the authors averaged the comment-level labels to construct the seller-level reputation score. $M _ { i }$ was the total number of comments received by seller i because different sellers may receive different numbers of comments. The unit of econometric analysis is at the seller level.

## True Model in the Econometric Stage

Our proposed solution is applicable to most of the popular econometric models with a probability function that could be estimated by MLE. One widely used model is the generalized linear model (GLM), which is the model explained here. In this case, the ideal regression is specified as:

$$
\begin{array}{r l} & {\mathrm{P} (Y _ {i} | \bar {X} _ {i}, Z _ {i}) = G (\bar {X} _ {i} \beta + Z _ {i} \gamma),} \\ & {\bar {X} _ {i} = \frac {1}{M _ {i}} \sum_ {j = 1} ^ {M _ {i}} X _ {i} ^ {j}, i = 1, \dots , N,} \end{array}\tag{4}
$$

where $G ( )$ is the link function (such as logistic or probit function) and $\beta$ is the focal regression coefficient for estimation, $Z _ { i }$ is an $N –  { \mathrm { b y } } – K$ matrix of control variables. ?? is a K-by-1 vector of regression coefficients of control variables.

## Measurement Error Model 1: Exact Solution by Binomial Distribution

This section explains how to estimate the measurement error model, which is the core of the solution. In hybrid studies, $X _ { i } ^ { j }$ is unobservable and only $W _ { i } ^ { j }$ is observable. Most hybrid studies estimate the following regression model by replacing ${ \bar { X } } _ { i }$ with $\textstyle { \overline { { W } } } _ { i }$ :

$$
\mathrm{P} (Y _ {i} | \bar {X} _ {i} = \bar {W} _ {i}, Z _ {i}) = G \big (\bar {W} _ {i} \hat {\beta} + Z _ {i} \hat {\gamma} \big).
$$

$\hat { \beta }$ is called the naïve estimator throughout this paper. However, the coefficients estimated from this model are not consistent because the probability function does not correctly account for the relationship between ${ \bar { X } } _ { i }$ and $\bar { W } _ { i }$ . The correct objective function for MLE is Equation (3). We make the following two assumptions to further simplify Equation (3).

Assumption 1: $\overline { { W } } _ { i }$ provides no additional information about $Y _ { i }$ conditional on ${ \bar { X } } _ { i }$ and $Z _ { i }$ . In other words, we assume that $\mathsf P ( Y _ { i } | \bar { X } _ { i } , Z _ { i } , \bar { W } _ { i } ) = \mathsf P ( Y _ { i } | \bar { X } _ { i } , Z _ { i } )$

Assumption 2: Define $e _ { i } ^ { g } \ = \ X _ { i } ^ { g } - \operatorname { E } \left( X _ { i } ^ { g } \big | W _ { i } ^ { g } , Z _ { i } , \bar { W } _ { i } \right)$ . We assume that $e _ { i } ^ { g }$ is uncorrelated with $X _ { i } ^ { h }$ and $W _ { i } ^ { h } f o r a l l h \neq g$

Assumption 1 is similar to the standard assumption imposed in the measurement error literature in econometrics. In the textbook version of the measurement error model, the measurement error term does not correlate with the dependent variable.<sup>3</sup> In Assumption 1, we assume that the mean of the proxy variable does not provide additional information for predicting Y. The validity of this assumption depends more on the choice of classifier than the nature of the data. Recall that researchers can choose classification algorithms and hyperparameter tuning to affect the values of ?? . Consequently, there is no business interpretation of $( W - X )$ because its value can be manipulated by researchers. This enables researchers to tune the chosen classifier so that Assumptions 1 and 2 are valid. As a result, the proposed theoretical formula in the econometric stage can produce a consistent estimator of the regression coefficient.

In Assumption 2, $e _ { i } ^ { g }$ represents the residual term between actual $X _ { i } ^ { g }$ and its conditional mean. Assumption 2 implies that this residual term does not correlate with the true values and predicted values of all other observations. The main reason for imposing Assumption 2 is to simplify the proof of theorems. Without this assumption, to estimate the conditional probability distribution of $X _ { i } ^ { g }$ , we need to consider other observations’ predicted labels, and it becomes intractable to include all the predicted labels for predicting $X _ { i } ^ { g }$ since different aggregated groups have different numbers of observations. In general, it is possible that Assumptions 1 and 2 are violated and researchers are advised to make sure that the first stage’s classifier does not produce a classification error that correlates with all other variables.<sup>4</sup>

Theorem 1: Let the labeled dataset be an i.i.d random sample drawn from the population. Given Assumptions 1 and 2, ?? in Equation (4) can be consistently estimated by applying MLE to:

$$
\mathrm{P} (Y _ {i} | \bar {W} _ {i}, Z _ {i}) = \sum_ {\bar {X} _ {i}} \mathrm{P} (Y _ {i} | \bar {X} _ {i}, Z _ {i}) \mathrm{P} (\bar {X} _ {i} | \bar {W} _ {i}, Z _ {i}),\tag{5}
$$

where the measurement error function can be decomposed as follows:

$$
\begin{array}{r} \mathrm{P} (\bar {X} _ {i} | \overline {{W}} _ {i}, Z _ {i}) = \sum_ {h = 0} ^ {M _ {i} \bar {X} _ {i}} \mathrm{B} \big (h; M _ {i} \overline {{W}} _ {i}, \mathrm{Pr} _ {i} ^ {\mathrm{TP}} \big) \times \mathrm{B} \big (M _ {i} \bar {X} _ {i} - h; M _ {i} \\ - M _ {i} \overline {{W}} _ {i}, \mathrm{Pr} _ {i} ^ {\mathrm{FN}} \big). \end{array}\tag{6}
$$

$\mathsf { B } \big ( h ; M _ { i } \bar { W } _ { i } , \mathsf { P r } _ { i } ^ { \mathrm { T P } } \big )$ and $\mathsf { B } \big ( M _ { i } \bar { X } _ { i } - h ; M _ { i } - M _ { i } \bar { W } _ { i } , \mathsf { P r } _ { i } ^ { \mathsf { F N } } \big )$ are two binomial probability mass functions explained in the following paragraphs. In summary, with Assumption 1, we simplify Equation (3) to Equation (5). With Assumption 2, we decompose $\mathsf { P } ( \bar { X } _ { i } | \bar { W } _ { i } , Z _ { i } )$ using Equation (6). Detailed proof of this theorem is provided in Appendix A. <sup>5</sup> <sup>6</sup>

To derive the conditional probability $\mathsf { P } ( \overline { { X } } _ { i } | \overline { { W } } _ { i } , Z _ { i } )$ at the aggregated level, we rely on the classification confusion matrix from the predictive stage in Table 2. The four important numbers (TP, TN, FP, and FN) correspond to the only four possible values of the individual-level measurement error model $\mathsf { P } ( X _ { i } ^ { j } | W _ { i } ^ { j } , Z _ { i } , \bar { W } _ { i } )$ since both $X _ { i } ^ { j }$ and $W _ { i } ^ { j }$ are binary variables.<sup>7</sup>

Specifically, the probabilities of TP and FN observations at the individual level are $\mathrm { P } ( X _ { i } ^ { j } = 1 / W _ { i } ^ { j } = 1 , Z _ { i } , \overline { { W } } _ { i } )$ and $\operatorname { P } ( X _ { i } ^ { j } =$ $1 / W _ { i } ^ { j } = 0 , Z _ { i } , \bar { W } _ { i } )$ , which are defined as $\mathsf { P r } _ { i } ^ { \mathrm { T P } }$ and $\mathrm { P r } _ { i } ^ { \mathsf { F N } }$ . ?? is the sample size of this aggregated group and we know that there are $M _ { i } { \bar { W } } _ { i }$ predicted positive observations. If the number of actual positive observations is $M _ { i } { \bar { X } } _ { i }$ and h is the number of TP cases, then we must have $M _ { i } { \bar { X } } _ { i } - h$ observations of FN. Now we are ready to explain the intuition behind $\begin{array} { r } { \mathrm { B } \big ( h ; M _ { i } \bar { W } _ { i } , \mathrm { P r } _ { i } ^ { \mathrm { T P } } \big ) \quad \mathrm { ~ a n d ~ } \quad \mathrm { B } ( M _ { i } \bar { X } _ { i } - h ; M _ { i } - M _ { i } \bar { W } _ { i } , \mathrm { P r } _ { i } ^ { \mathrm { F N } } ) } \end{array}$ in Equation (6). Under the independence Assumption 2, the probability of $^ { * * } h$ TP observations out of $M _ { i } { \bar { W } } _ { i }$ predicted positive observations” can be modeled by a binomial distribution, $\mathsf { B } ( h ; M _ { i } \bar { W } _ { i } , \mathsf { P r } _ { i } ^ { \mathrm { T P } } )$ with the first parameter being the number of independent draws (total number of predicted positive observations) and the second parameter being the probability of the event (TP rate). Similarly, $\mathsf { B } \big ( M _ { i } \bar { X } _ { i } - h ; M _ { i } -$ $M _ { i } \overline { { W } } _ { i } , \mathrm { P r } _ { i } ^ { \mathrm { F N } } )$ means the probability that there are $M _ { i } { \bar { X } } _ { i } - h$ FN observations out of $M _ { i } - M _ { i } { \overline { { W } } } _ { i }$ predicted negative observations.

Next, we write the conditional probability function of obtaining this confusion matrix as:

$$
\begin{array}{c} \mathrm{P} (\overline {{X}} _ {i}, h | \overline {{W}} _ {i}, Z _ {i}) = \mathrm{B} \big (h; M _ {i} \overline {{W}} _ {i}, \mathrm{Pr} _ {i} ^ {\mathrm{TP}} \big) \times \mathrm{B} \big (M _ {i} \overline {{X}} _ {i} - h; M _ {i} - \\ M _ {i} \overline {{W}} _ {i}, \mathrm{Pr} _ {i} ^ {\mathrm{FN}} \big). \end{array}
$$

Finally, we decompose $\mathsf { P } ( \overline { { X } } _ { i } | \overline { { W } } _ { i } , Z _ { i } )$ by all possible values of h (the number of true positive observations) and for each pair of $( \bar { X } _ { i } , h )$ , the probability is a multiplicative term of two binomial distribution probabilities. The numbers of predicted positive and negative observations are observable from the output of the first-stage prediction. The two terms $\mathsf { P r } _ { i } ^ { \mathrm { T P } }$ and $\mathrm { P r } _ { i } ^ { \mathrm { F N } }$ conditional on $W _ { i } ^ { j } , Z _ { i }$ , and $\bar { W } _ { i }$ can be estimated by applying logistic regression to the labeled set in the predictive stage with cross-validation. We also provide one example to explain how to calculate $\mathsf { P } ( \overline { { X } } _ { i } | \overline { { W } } _ { i } , Z _ { i } )$ (see Appendix A).

Therefore, given any classifier,<sup>8</sup> we can always estimate the individual-level measurement error model by using the validation dataset. Next, we use this individual-level result and the confusion matrix to estimate the aggregate-level measurement error model using Equation (6). Finally, we correct the estimation bias using Equation $( 5 ) . ^ { 9 }$ However, classifiers with lower accuracy produce the estimated coefficients with larger variances. We recommend that researchers select the classifier with the smallest variance.<sup>10,11</sup>

The major drawback of the solution in Theorem 1 is the complexity issue arising when $M _ { i }$ becomes arbitrarily large. Fortunately, when $M _ { i }$ is large enough, we can apply the central limit theorem or law of large numbers to derive the simplified formula of $\mathsf { P } ( \overline { { X } } _ { i } | \overline { { W } } _ { i } , Z _ { i } )$ . In the next two sections, we analyze the large sample property of this problem.

## Measurement Error Model 2: Approximated Solution by Normal Distribution

In this case, we maintain Assumptions 1 and 2. When $M _ { i }$ is large enough, the mean value of $X _ { i } ^ { j }$ may converge in distribution to a normal distribution by Lyapunov central limit theory (CLT) (Bentkus, 2005). In addition, our solution in Equation (6) relies on the binomial distribution, which is approximated by normal distribution asymptotically (Schader & Schmid, 1989).

Specifically, for predicted positive observations, the number of TP observations follows the binomial distribution $\mathsf { B } \big ( \cdot ; \mathsf { W P } , \mathsf { P r } _ { i } ^ { \mathrm { T P } } \big )$ , with WP equaling $M { \bar { W } } _ { i }$ . For predicted negative observations, the number of FN observations follows $\mathsf { B } \big ( \cdot ; \mathsf { W N } , \mathsf { P r } _ { i } ^ { \mathsf { F N } } \big )$ , with WN equaling $M - M { \bar { W } } _ { i }$ . When the sample size is large enough, two binomial distributions can be approximated by the normal distributions. Specifically, $\mathsf { B } \big ( \cdot ; \mathsf { W P } , \mathsf { P r } _ { i } ^ { \mathrm { T P } } \big )$ is approximated by $\mathrm { N } ( \cdot ; \mathrm { W P } \times$ $\mathrm { P r } _ { i } ^ { \mathrm { T P } } , \mathrm { W P } \times \mathrm { P r } _ { i } ^ { \mathrm { T P } } \times \mathrm { P r } _ { i } ^ { \mathrm { F P } } )$ and $\mathsf { B } \big ( \cdot ; \mathsf { W N } , \mathsf { P r } _ { i } ^ { \mathsf { F N } } \big )$ is approximated by $\mathrm { N } ( \cdot ; \mathrm { W N } \times \mathrm { P r } _ { i } ^ { \mathrm { F N } } , \mathrm { W N } \times \mathrm { P r } _ { i } ^ { \mathrm { F N } } \times \mathrm { P r } _ { i } ^ { \mathrm { T N } } )$ . Detailed proof of this part is provided in Appendix A. With a simple transformation, we can derive the normal density function of the mean ${ \bar { X } } _ { i } .$ . The mean and variance of this normal distribution are given by:

$$
\mu_ {i} = \mathrm{E} (\bar {X} _ {i} | \bar {W} _ {i}, Z _ {i}) = \frac {1}{M _ {i}} [ \mathrm{WP} \times \mathrm{Pr} _ {i} ^ {\mathrm{TP}} + \mathrm{WN} \times \mathrm{Pr} _ {i} ^ {\mathrm{FN}} ],
$$

$$
\sigma_ {i} ^ {2} = \mathrm{Var} (\bar {X} _ {i} | \bar {W} _ {i}, Z _ {i}) = \frac {1}{M _ {i} ^ {2}} [ \mathrm{WP} \times \mathrm{Pr} _ {i} ^ {\mathrm{TP}} \times \mathrm{Pr} _ {i} ^ {\mathrm{FP}} + \mathrm{WN} \times \mathrm{Pr} _ {i} ^ {\mathrm{FN}} \times \mathrm{Pr} _ {i} ^ {\mathrm{TN}} ],
$$

where $\mathrm { C o v } ( \mathrm { T P } , \mathrm { F N } | \bar { W } _ { i } , Z _ { i } ) = 0$ since $X _ { i } ^ { j }$ of the observations are conditionally independent under Assumption 2. However, the normal density function is continuous whereas the possible values of ${ \bar { X } } _ { i }$ are discrete $\begin{array} { r } { ( \mathbf { e . g . , \ } ( 0 , \frac { 1 } { M _ { i } } , \frac { 2 } { M _ { i } } , . . . , 1 ) ) } \end{array}$ . Therefore, we adjust the probability density to probability mass by utilizing the half-unit continuity correction (Rumsey, 2006). Let Φ denote the cumulative distribution function of $f ( \bar { X } _ { i } | \bar { W } _ { i } , Z _ { i } )$

$$
\mathrm{P} (\bar {X} _ {i} | \bar {W} _ {i}, Z _ {i}) = \Phi \left(\bar {X} _ {i} + \frac {1}{M _ {i}} \times 0. 5\right) - \Phi (\bar {X} _ {i} - \frac {1}{M _ {i}} \times 0. 5).\tag{7}
$$

Theorem 2: Let the labeled dataset be an i.i.d random sample drawn from the population. Suppose that Assumptions 1 and 2 hold and $M _ { i }$ is large enough, ?? in Equation (4) can be approximately estimated by applying MLE to Equation (5) where $\mathsf { P } ( \overline { { X } } _ { i } | \overline { { W } } _ { i } , Z _ { i } )$ is estimated by Equation (7).

The time complexity of the approximation method is much better than that of the exact method. Specifically, the time complexity of using Equation (7) to calculate the corrected probability is linear in $M _ { i } ~ ( O ( M _ { i } ) )$ since we only need to calculate the normal density function once to derive $\mathsf { P } ( \overline { { X } } _ { i } | \overline { { W } } _ { i } , Z _ { i } )$ for each possible value of ${ \bar { X } } _ { i } .$ . However, the time complexity of using Equation (6) is quadratic in $M _ { i } ( O ( { M _ { i } } ^ { 2 } ) )$ since there is an extra loop in h.

To apply this method in practice, we would need to decide on a threshold value of group sample size between using the solution in Theorem 1 versus Theorem 2. We borrow the rule of thumb for the normal approximation of a binomial random variable (Schader & Schmid, 1989), which states that the normal approximation is appropriate only if all the realization values within three standard deviations around $\mathbb { E } ( \bar { X } _ { i } | \bar { W } _ { i } , Z _ { i } )$ fall within the range of ${ { \bar { X } } _ { i } } \left( 0 \right.$ to 1), that is:

$$
\mu_ {i} \pm 3 \sigma_ {i} \in (0, 1).
$$

## Measurement Error Model 3: Approximated Solution by Law of Large Numbers

When the sample size is large enough, the mean value of any random variable may converge to its expected value. In our problem, when $M _ { i }$ is large enough, ${ \hat { \bar { X } } } _ { i }$ converges to its conditional expectation $\operatorname { E } ( { \bar { X } } _ { i } | { \bar { W } } _ { i } , Z _ { i } )$ by the strong law of large numbers (LLN) (Feller, 2008).

$$
\mathrm{P} (\bar {X} _ {i} = \mathrm{E} (\bar {X} _ {i} | \bar {W} _ {i}, Z _ {i}) | \bar {W} _ {i}, Z _ {i}) = 1.\tag{8}
$$

In this case, we can have a simple and fast solution by rewriting Equation (5) with the following probability function:

$$
\begin{array}{r} \mathrm{P} (Y _ {i} | \bar {W} _ {i}, Z _ {i}) = \mathrm{P} (Y _ {i} | \bar {X} _ {i} = \mathrm{E} (\bar {X} _ {i} | \bar {W} _ {i}, Z _ {i}), Z _ {i}) \mathrm{P} (\bar {X} _ {i} \\ = \mathrm{E} (\bar {X} _ {i} | \bar {W} _ {i}, Z _ {i}) | \bar {W} _ {i}, Z _ {i}) \\ = \mathrm{P} (Y _ {i} | \bar {X} _ {i} = \mathrm{E} (\bar {X} _ {i} | \bar {W} _ {i}, Z _ {i}), Z _ {i}). \end{array}\tag{9}
$$

The right side of the first equality does not have a summation and it only has the term $\bar { X _ { i } } = \mathrm { E } ( \bar { \bar { X } } _ { i } | \bar { W } _ { i } , Z _ { i } )$ , since Equation (8) implies that $\mathsf P ( \bar { X } _ { i } | \bar { W } _ { i } , Z _ { i } ) = 0$ for all other values of ${ \bar { X } } _ { i } .$ . The time complexity of using Equation (8) is even faster than using Equation (7) since we only need to calculate $\mathbb { E } ( \bar { X } _ { i } | \bar { W } _ { i } , Z _ { i } )$ However, there is no general rule in the literature for LLN approximation. To provide guidance, we follow the rule of thumb for normal approximation to derive one rule for LLN approximation. Specifically, the rule states that the law of large numbers is appropriate only if all the realization values within three standard deviations around $\mathbb { E } ( \bar { X } _ { i } | \bar { W } _ { i } , Z _ { i } )$ fall within the small range of $\mathbb { E } ( \bar { X } _ { i } | \bar { W } _ { i } , Z _ { i } )$ (±0.05). Empirically, researchers can adjust the small range based on their tolerance for error.

$$
\mu_ {i} \pm 3 \sigma_ {i} \in (\mathrm{E} (\bar {X} _ {i} | \bar {W} _ {i}, Z _ {i}) - 0. 0 5, \mathrm{E} (\bar {X} _ {i} | \bar {W} _ {i}, Z _ {i}) + 0. 0 5).
$$

Theorem 3. Let the labeled dataset be the random sample i.i.d drawn from the population. Assuming that Assumptions 1 and 2 hold, ?? in Equation $( 4 )$ can be approximately estimated by applying MLE to Equation $( 5 ) ,$ , where $\mathsf { P } ( \overline { { X } } _ { i } | \overline { { W } } _ { i } , Z _ { i } )$ is estimated by Equation (8) when $M _ { i }$ is large enough.

Full Solution of Case 1. In summary, our full solution for Case 1 involves three steps. First, we train the classifier in the predictive stage with the following criteria. The classifier produces predicted values that satisfy Assumptions 1-2. Second, for each aggregated group, we decide on one of three methods for estimation based on the rules. Finally, among the classifiers that satisfy Assumptions 1-2, we select the most precise classifier that leads to the smallest variance of the estimated regression coefficient.

## Case 2: Sum of Proxy Variable as the Focal Independent Variable

This section analyzes the case where the sum of the proxy variable is utilized as the focal independent variable in the generalized linear model. Roughly speaking, the solution is conceptually the same as that in Case 1. The first two solutions are still applicable with minor adjustments. The third LLN solution is not applicable because the law of large numbers is not applicable to the sum of the proxy variable in Case 2. Due to the page limit, we omitted the technical details.

## Case 3: Mean of Proxy Variable as the Dependent Variable

In this section, we analyze the case where the mean of the proxy variable is utilized as the dependent variable in the regression in the econometric stage. The dependent variable in the econometric stage is denoted by ${ \bar { Y } } _ { i } ,$ which is the mean of the true variable for the aggregated group $i . M _ { i }$ denotes the number of observations for aggregating $\bar { Y } _ { i \cdot } Y _ { i } ^ { j }$ denotes the true label of the observation $j$ for aggregating $\bar { Y _ { i } }$ . For example,

Deng et al. (2018) examined the impact of stock returns on microblog sentiment. They defined the stock-level “sentiment score” (??̅<sub>??</sub>) by the mean of the microblog-level labels (label being “positive” or “non-positive”) within a specific day $i . M _ { i }$ was the number of microblogs on that day.

## True Model in the Econometric Stage

For the true regression model in Case 3, since the dependent variable is a proportion variable ranging from 0 to 1 based on discrete outcomes, the most rigorous specification should utilize the beta-binomial model to fit this distribution (Martin et al., 2020; Oberhofer & Pfaffermayr, 2014). This section also serves the purpose of illustrating the generalizability and applicability of our proposed solution on different types of probabilistic models, in addition to GLM in Cases 1 and 2.

It is intuitive to assume that the number of positive labels follows a binomial distribution:

$$
M _ {i} \bar {Y} _ {i} {\sim} \mathrm{Binomial} (M _ {i}, p _ {i}), \mathrm{and} \bar {Y} _ {i} = \frac {1}{M _ {i}} \sum_ {j = 1} ^ {M _ {i}} Y _ {i} ^ {j}, i = 1, \dots , N,
$$

where $p _ { i }$ is the probability of $Y _ { i } ^ { j } = 1 = { } ^ { \circ } \mathrm { { ' p o s i t i v e " } }$ and can also be interpreted as the expectation of $Y _ { i } ^ { j } \cdot p _ { i }$ follows a beta distribution. Formally:

$$
p _ {i} \sim \mathrm{Beta} (\theta_ {i} \varphi_ {i}, (1 - \theta_ {i}) \varphi_ {i}).
$$

The beta distribution was chosen because of its wide applicability to popular special cases, such as uniform distribution. There are two parameters of a beta distribution. The first parameter $\theta _ { i }$ represents the expectation of this distribution, $\operatorname { E } ( p _ { i } ) = \theta _ { i }$ . The second parameter $\varphi _ { i }$ acts as a scaling factor that affects the variance of the distribution. A larger $\varphi _ { i }$ implies less variance.

In the literature, researchers also assume the logistic regression function between $\theta _ { i }$ and $X _ { i } { \mathrm { : } }$

$$
\theta_ {i} = \operatorname{E} (p _ {i} | X _ {i}) = \operatorname{E} (\bar {Y _ {i}} | X _ {i}) = \frac {\exp (X _ {i} \beta)}{1 + \exp (X _ {i} \beta)}.\tag{10}
$$

Given these model setups, $\mathrm { P } ( \overline { { Y } } _ { i } | X _ { i } )$ follows the probability mass function of the beta-binomial distribution:<sup>12</sup>

$$
\begin{array}{l} \mathrm{P} (\bar {Y} _ {i} | X _ {i}) \\ = \binom {M _ {i}} {M _ {i} \bar {Y} _ {i}} \frac {\mathrm{B} (\theta_ {i} \varphi_ {i} + M _ {i} \bar {Y} _ {i} , (1 - \theta_ {i}) \varphi_ {i} + M _ {i} - M _ {i} \bar {Y} _ {i})}{\mathrm{B} (\theta_ {i} \varphi_ {i} , (1 - \theta_ {i}) \varphi_ {i})}. \end{array}\tag{11}
$$

<table><tr><td colspan="4">Table 3. Confusion Matrix for Dependent Variable</td></tr><tr><td></td><td> $Y_i^j=1$ </td><td> $Y_i^j=0$ </td><td>Sum</td></tr><tr><td> $y_i^j=1$ </td><td>h (TP)</td><td> $M_i\bar{y}_i-h$  (FP)</td><td> $M_i\bar{y}_i$ </td></tr><tr><td> $y_i^j=0$ </td><td> $M_i\bar{Y}_i-h$  (FN)</td><td> $(M_i-M_i\bar{Y}_i)-(M_i\bar{y}_i-h)$  (TN)</td><td> $M_i-M_i\bar{y}_i$ </td></tr><tr><td>Sum</td><td> $M_i\bar{Y}_i$ </td><td> $M_i-M_i\bar{Y}_i$ </td><td> $M_i$ </td></tr></table>

Measurement Error Model 1: Exact Solution by Binomial Distribution

However, in hybrid studies, $Y _ { i } ^ { j }$ is unobservable and the proxy variable $y _ { i } ^ { j }$ is observable for all records in both labeled and unlabeled sets. Similar to Cases 1 and 2, when researchers ignore the measurement error of $Y _ { i } ^ { j }$ , they estimate the following regression model:

$$
\begin{array}{r l} & {\mathrm{P} (\bar {y} _ {i} | X _ {i})} \\ & {= \binom {M _ {i}} {M _ {i} \bar {y} _ {i}} \frac {\mathrm{B} (\theta_ {i} \varphi_ {i} + M _ {i} \bar {y} _ {i} , (1 - \theta_ {i}) \varphi_ {i} + M _ {i} - M _ {i} \bar {y} _ {i})}{\mathrm{B} (\theta_ {i} \varphi_ {i} , (1 - \theta_ {i}) \varphi_ {i})},} \end{array}\tag{12}
$$

where $\begin{array} { r } { \theta _ { i } = \mathtt { E } ( \bar { y } _ { i } | X _ { i } ) = \frac { \exp ( X _ { i } \widehat { \beta } ) } { 1 + \exp ( X _ { i } \widehat { \beta } ) } . } \end{array}$ However, this probability function does not account for the error between ${ \bar { y } } _ { i }$ and ${ \bar { Y } } _ { i \cdot }$ . The correct objective function for MLE should be re-written as,

$$
\mathrm{P} (\bar {y} _ {i} | X _ {i}) = \sum_ {\bar {Y} _ {i}} \mathrm{P} (\bar {y} _ {i} | \bar {Y} _ {i}, X _ {i}) \mathrm{P} (\bar {Y} _ {i} | X _ {i}).\tag{13}
$$

The second term on the right side of Equation (13) can be computed by Equation (11), which is the true regression model. The first term is the measurement error model that captures the relationship between $\bar { y } _ { i }$ and ${ \bar { Y } } _ { i \cdot }$ To estimate this model, we impose one assumption,

Assumption 3: Define $e _ { i } ^ { g } \ = y _ { i } ^ { g } - \mathtt { E } \big ( y _ { i } ^ { g } \big | X _ { i } , Y _ { i } ^ { g } \big )$ . We assume $e _ { i } ^ { g }$ is uncorrelated with $y _ { i } ^ { h }$ and $Y _ { i } ^ { h } f o r$ all $h \neq g .$

The role of Assumption 3 is similar to Assumption 2. Assumption 3 implies that the residual term $( e _ { i } ^ { g } )$ does not correlate with the true labels and predicted labels of other observations. With Assumption 3, the results can be greatly simplified because we do not need to consider the values of other rows’ variables when predicting $y _ { i } ^ { g }$

Theorem 4: Let the labeled dataset be the i.i.d. random sample drawn from the population. Given Assumption 3, ?? in Equation (11) can be consistently estimated by applying MLE to Equation (13), where $\mathrm { P } ( \bar { y } _ { i } | \bar { Y } _ { i } , X _ { i } )$ can be decomposed as:

$$
\mathrm{P} (\bar {y} _ {i} | \bar {Y} _ {i}, X _ {i}) = \sum_ {h = 0} ^ {M _ {i} \bar {y} _ {i}} \mathrm{B} \big (h; M _ {i} \bar {Y} _ {i}, \mathrm{Pr} _ {i} ^ {\mathrm{TP}} \big) \times \mathrm{B} \big (M _ {i} \bar {y} _ {i} - h; M _ {i} \bar {Y} _ {i}, \mathrm{Pr} _ {i} ^ {\mathrm{FP}} \big).\tag{14}
$$

$\mathsf { B } \big ( h ; M _ { i } \bar { Y } _ { i } , \mathsf { P r } _ { i } ^ { \mathrm { T P } } \big )$ is the binomial probability of $^ { \ast } h$ TP observations out of $M _ { i } { \bar { Y } } _ { i }$ actual positive observations.” $\mathsf { B } ( M _ { i } \bar { y } _ { i } - h ; M _ { i } - M _ { i } \bar { Y } _ { i } , \mathsf { P r } _ { i } ^ { \mathsf { F P } } )$ is the binomial probability of $\mathbf { \tilde { \Sigma } } ^ {  } M _ { i } \mathbf { \bar { y } } _ { i } - h$ FP observations out of $M _ { i } - M _ { i } { \bar { Y } } _ { i }$ actual negative observations”. $\mathsf { P r } _ { i } ^ { \mathrm { T P } }$ and $\mathrm { P r } _ { i } ^ { \mathrm { F P } }$ are the probabilities of TP and FP observations at the individual level, which are $\mathsf { P } ( y _ { i } ^ { j } =$ $1 / Y _ { i } ^ { j } = 1 , X _ { i } )$ and $\mathrm { P } ( y _ { i } ^ { j } = 1 / Y _ { i } ^ { j } = 0 , X _ { i } )$ ). The notations of the confusion matrix for the dependent variable are shown in Table 3. The proof of this theorem and approximated solutions for the large sample case are qualitatively similar to Case 1, which are shown in Appendix B. The full solution of Case 3 is similar to Case 1 and the details were omitted for brevity.

## Case 4: Sum of Proxy Variable as the Dependent Variable

In this section, we analyze the case where the sum of the proxy variable is utilized as the dependent variable in the econometric model. The dependent variable in the econometric stage is denoted by $S _ { Y _ { i } } ,$ , which is the sum of the true variable for the aggregated group $i . Y _ { i } ^ { j }$ denotes the true label of the observation j in group i. For example, Jabr et al. (2014) examined how the contribution of users who provided solutions online is affected by the recognition mechanism in the user support forums. The “contribution level” $\left( { { S _ { Y } } _ { i } } \right)$ of each user is defined as the sum of post-level labels (label being “solution post” or not) and conceptually it should not be specified as a proportion. A proportion variable in this type of application captures the “quality” not the “quantity” of contribution.

## True Model in the Econometric Stage

For the true model in the econometric stage, since $X _ { i }$ may influence $S _ { Y _ { i } }$ through both $\mathrm { P } ( M _ { i } | X _ { i } )$ and $\mathsf { P } \big ( S _ { Y _ { i } } | X _ { i } , M _ { i } \big )$ , we adopt the beta-binomial-Poisson model to model the relationship between $X _ { i }$ and $S _ { Y _ { i } }$ (Lora & Singer, 2008; Zhu et al., 2003). We first model $\mathrm { P } ( M _ { i } | X _ { i } )$ by Poisson model. Next, we model $\mathsf { P } \big ( S _ { Y _ { i } } | X _ { i } , M _ { i } \big )$ by beta-binomial model. The Poisson model for the sample size $M _ { i }$ is given by

$$
\begin{array}{r l} & M _ {i} \sim \mathrm{Poisson} (\lambda_ {i}) \mathrm{and} \lambda_ {i} = \mathrm{E} (M _ {i} | X _ {i}), \\ & \quad = > \mathrm{P} (M _ {i} | X _ {i}) = \frac {e ^ {- \lambda_ {i}} \lambda_ {i} ^ {M _ {i}}}{M _ {i} !}, \qquad \lambda_ {i} = \exp (X _ {i} \gamma). \end{array}\tag{15}
$$

Given $M _ { i } ,$ , we assume the sum of the labels follows a betabinomial distribution,

$$
\begin{array}{r l} & S _ {Y _ {i}} \sim \text {Binomial} (M _ {i}, p _ {i}), p _ {i} \sim \text {Beta} (\theta_ {i} \varphi_ {i}, (1 - \theta_ {i}) \varphi_ {i}), \text {and} S _ {Y _ {i}} \\ & \qquad = \sum_ {j = 1} ^ {M _ {i}} Y _ {i} ^ {j}, i = 1, \dots , N. \\ & = > \mathrm{P} (S _ {Y _ {i}} | X _ {i}, M _ {i}) = \binom {M _ {i}} {S _ {Y _ {i}}} \frac {\mathrm{B} (\theta_ {i} \varphi_ {i} + S _ {Y _ {i}} , (1 - \theta_ {i}) \varphi_ {i} + M _ {i} - S _ {Y _ {i}})}{\mathrm{B} (\theta_ {i} \varphi_ {i} , (1 - \theta_ {i}) \varphi_ {i})}, \theta_ {i} \\ & \qquad = \frac {\exp (X _ {i} \beta)}{1 + \exp (X _ {i} \beta)}, \end{array}
$$

where $\theta _ { i } = \operatorname { E } ( { \bar { Y } } _ { i } | X _ { i } )$ . Then, we can derive the relationship between $S _ { Y _ { i } } , \theta _ { i } ,$ , and $\lambda _ { i }$ as follows,

$$
\operatorname{E} (S _ {Y _ {i}} | X _ {i}) = \operatorname{E} \bigl (\operatorname{E} \bigl (S _ {Y _ {i}} | X _ {i}, M _ {i} \bigr) | X _ {i} \bigr) = \operatorname{E} (M _ {i} \theta_ {i} | X _ {i}) = \theta_ {i} \lambda_ {i}.
$$

Therefore, to investigate the effect of $X _ { i }$ on $S _ { Y _ { i } , \ l }$ we need to estimate $\lambda _ { i }$ and $\theta _ { i }$ , which denote the expectation of $M _ { i }$ and expectation of $\bar { Y _ { i } }$ respectively.

## Measurement Error Model

For $\mathrm { P } ( M _ { i } | X _ { i } )$ , researchers can directly estimate it by utilizing the Poisson model since all the variables are precisely measured. For $\mathsf { P } \big ( S _ { Y _ { i } } | X _ { i } , M _ { i } \big )$ , the true variable $Y _ { i } ^ { j }$ is unobservable and only $y _ { i } ^ { j }$ is observable for all records. If we estimate this regression model with $S _ { y _ { i } }$ as the dependent variable, the estimated $\beta$ is inconsistent.

To eliminate the inconsistency, researchers can follow the solution in Case 3, where the true model specification is the beta-binomial model. Therefore, the solution in Case 3 is part of Case 4. Finally, we can derive the marginal effect of $X _ { i q }$ by

$$
\frac {\partial \mathrm{E} (S _ {Y _ {i}} | X _ {i})}{\partial X _ {i q}} = \gamma_ {q} \exp (X _ {i} \gamma) \Lambda (X _ {i} \beta) + \exp (X _ {i} \gamma) \Lambda^ {\prime} (X _ {i} \beta) \beta_ {q},
$$

where $X _ { i q }$ denotes the $q _ { t h }$ independent variable, Λ() denotes the logistic cumulative distribution function, $\frac { \exp ( X _ { i } \beta ) } { 1 + \exp ( X _ { i } \beta ) }$ , and $\Lambda ^ { \prime } ( )$ is the derivative of $\Lambda ( ) , \Lambda ( ) ( 1 - \Lambda ( ) )$ . Moreover, since $\mathrm { P } ( M _ { i } | X _ { i } )$ is separately estimated, researchers can utilize other count models, such as the negative binomial model (Lora & Singer, 2011).

## Simulation Results

This section reports the simulation results for assessing the effectiveness of the proposed methods. In the predictive stage, we use a real-world dataset and there is no simulated data. Simulation is only employed at the econometric stage so that we know the true values of the regression coefficients.

In the first stage, the real-world dataset is about predicting online review ratings by textual review contents for “Musical Instruments” on Amazon (He & McAuley, 2016). The original ratings for each review had five categories and we generated a binary label, “sentiment,” by relabeling rating value 5 as positive and ratings 1-4 as negative. We compiled two datasets with different numbers of reviews per product. The first dataset included 87,339 reviews for 10,000 products. The number of reviews per product ranged from 1 to 1066, with a standard deviation of 31.424. Since 8467 products had few reviews (less than 10), this dataset was considered a small sample case that better fit the exact solution approach. The second dataset also contained 10,000 products and was constructed for the large sample case that better fit the two approximated solutions. In the second dataset, 6,000 products had less than 10 reviews, whereas 4,000 products had more than 100 reviews. In total, the second dataset included around 450,000 reviews. As a result, the mean or sum of the labels of those 4,000 products met the requirement of the approximated solution by the normal distribution. Moreover, the “large sample” here refers to the number of reviews per product, not the number of products. Both datasets comprised around 60% positive reviews and 40% negative reviews. The classification method was a state-of-art algorithm, XGBoost (Chen & Guestrin, 2016). We utilized the RTextTools package in R to generate the term frequency matrix of the reviews and preprocess the reviews by stemming words, converting the text to its lowercase, and removing the punctuation, stop words, and numbers. We also removed sparse terms that occurred in less than 2% of the reviews.

Regarding the evaluation procedure, we randomly sampled 17,547 rows for the labeled dataset and the remaining dataset was used for the unlabeled set, although we knew the actual labels of all rows in both datasets. Because of this property, we could evaluate the second-stage regression bias by using true labels versus predicted labels. Next, we built the XGBoost classifier on the labeled set and used that classifier to predict the labels on the unlabeled set, pretending that we did not know the labels on the unlabeled set. We also used fivefold cross-validation to compute the performance metrics of XGBoost. Predicted labels were aggregated at the product level and used in the econometric stage’s regression. The true values of the aggregated variable were used in the regression as the first-best benchmarking case.

To assess the performance sensitivity of our method with respect to the classification error, we needed to create similar classifiers with different prediction performances as the candidate classifiers. Our theories suggest that the estimated coefficient is consistent for all classifiers, including classifiers with poor prediction accuracy. For this section, we tuned the “nrounds” hyper-parameter of XGBoost, which indicates the number of boosted trees. We changed “nrounds” from 4 to 200 with a step value of 4 to construct 50 classifiers with different accuracies. The prediction performances of 50 classifiers are depicted in Figure 1, where the x-axis is the “nrounds” divided by 4, and the yaxis is the performance metric value. We report the values of Accuracy, Kappa, F1, and AUC. Figure 1 suggests that the prediction performance generally becomes better as the “nrounds” value increases within 200.

In the second stage, we aggregated the proxy variable, as in the four cases described in the Theoretical Solutions section. The second-stage simulation procedure and results are discussed in the following sections. All experiments were conducted on a PC with Intel i7-6700 3.4GHz CPU and 8GB RAM.

## Case 1: Mean of Proxy Variable as the Focal Independent Variable

The true econometric model is specified as the following logistic regression model with the coefficients being 1 for both right-side variables,

$$
\mathrm{P} (Y _ {i} = 1 | \bar {X} _ {i}, Z _ {i}) = \frac {\exp (0 . 2 + \bar {X} _ {i} + Z _ {i})}{1 + \exp (0 . 2 + \bar {X} _ {i} + Z _ {i})},\tag{16}
$$

where ${ \bar { X } } _ { i }$ is the mean value of review sentiment computed from the first stage. $M _ { i }$ is the number of reviews. $Z _ { i }$ is a simulated control variable. Among these three variables, only $M _ { i }$ is from the actual dataset and the other two were simulated. The simulation procedure involved several steps. We started by simulating $Z _ { i }$ by a normal distribution with a mean of 0 and a variance of 0.25. Given the value of $Z _ { i } ,$ , we specified $\mathsf { P } ( X _ { i } ^ { j } = { 1 } | Z _ { i } )$ as follows:

$$
\mathrm{P} \big (X _ {i} ^ {j} = 1 | Z _ {i} \big) = \frac {\exp (0 . 2 + Z _ {i})}{1 + \exp (0 . 2 + Z _ {i})}.
$$

Third, given the conditional probability function of $X _ { i } ^ { j } ,$ we simulated the realized value of each $X _ { i } ^ { j }$ by Bernoulli distribution. The sum of $X _ { i } ^ { j }$ followed a binomial distribution with parameters $( ~ M _ { i } \ , ~ \mathsf { P } \big ( X _ { i } ^ { j } = 1 | Z _ { i } \big ) )$ . Fourth, given the simulated value of each $X _ { i } ^ { j } .$ , if the value was 1, we randomly matched that row with a positive review record in the actual dataset. This allowed us to compute ${ \bar { X } } _ { i }$ easily and derive $\mathsf { P } ( Y _ { i } = 1 | \bar { X } _ { i } , Z _ { i } )$ using Equation (16). Finally, the Bernoulli distribution was utilized to simulate $Y _ { i }$ using Equation (16).

![](/api/attachments/UYSYHYE6/fulltext/images/c29cc1ceaddd6906375529590c11a42c05b6b3dde94b7ebca01a1d34b4e0f5ae.jpg)

![](/api/attachments/UYSYHYE6/fulltext/images/66c7eb19bc2b470d8867d1adacb1e812a229cc4bdf4a716eab3bdc9199ebb0ec.jpg)  
(a) Results for focal variable (ground truth of $\pmb { \beta _ { 1 } }$ is 1)

![](/api/attachments/UYSYHYE6/fulltext/images/3d80438fa26be864fb18724697b3d3d98149d27b04406c6b4b850146715ad402.jpg)  
(b)Results for control variable (ground truth of $\beta _ { 2 } \ i \ s 1 )$  
Note: Naïve. $\beta _ { 1 }$ refers to the coefficient of ${ \bar { X } } _ { i }$ without correction; Corr. $\beta _ { 1 }$ refers to the coefficient of ${ \bar { X } } _ { i }$ after using the exact solution. $\beta _ { 2 }$ refers to the coefficient of $Z _ { i } .$ ?????? refers to the classifier accuracy.

Figure 2. Simulation Results for Case 1 (Small Sample Case)

## Evaluation of the Exact Solution for Small Sample Case

We first evaluated the exact solution for the small sample case. When using the true mean of review sentiment $( { \bar { X } } _ { i } )$ to derive the empirical regression coefficients, the estimated coefficients for ${ \bar { X } } _ { i }$ and $Z _ { i }$ were 1.094 and 1.006, respectively. This is the ideal solution and is not feasible in practice unless the text classification is perfect.

Next, we derived the regression results from classifiers with errors. For each “nrounds” value, we trained and built a classifier and derived the proxy variable ?? for ?? . The baseline case was regression without any correction: regression by using the mean of the proxy variable $( \overline { { W } } _ { i } )$ as the independent variable. This is also the method widely used in existing literature. Results are indicated in Figures 2a and 2b by the solid lines after we repeated the regression by using 50 different proxy variables based on different “nrounds” values. In the figures, the x-axis is the “nrounds” value divided by 4, and the y-axis on the left side is the coefficient value. The yaxis on the right side shows the accuracy value. The accuracy results are reported by dashed lines. We observe that the focal regression coefficient without any correction is much smaller than the true value 1. The results using Equation (5) and Equation (6) to derive the corrected coefficients for ${ \bar { X } } _ { i }$ and $Z _ { i }$ are depicted as the dotted lines in Figures 2a and 2b. These results suggest that our method corrected the estimation error and is not sensitive to the classifier performance.

## Evaluation of the Approximated Solutions for Large Sample Case

We then evaluated our methods for the large sample case. We first conducted logit regression using the true mean of review sentiment $( { \bar { X } } _ { i } )$ . The estimated coefficients for ${ \bar { X } } _ { i }$ and $Z _ { i }$ were 0.937 and 1.020. Next, we applied three correction methods to this dataset. In the first method, we applied Equation (5) and Equation (6) (exact solution) to the observations aggregated by less than 10 reviews and applied Equation (7) (CLT approximation) to the observations aggregated by over 100 reviews. However, in the second method, we applied Equation (8) (LLN approximation) to the observations aggregated by over 100 reviews. In the third method, we applied the exact solution to the whole dataset to derive the corrected coefficients. The results for the three methods are shown as the dashed, dash-dotted, and dotted lines in Figure 3. We observe that these three lines are indistinguishable. The overlap of the corrected coefficients from the three methods indicates the effectiveness of our approximated solutions when the number of reviews per product is large enough. The results also confirm that our exact and approximated solutions can indeed correct the estimation inconsistency. Moreover, the relative running time of LLN approximation, CLT approximation, and the exact solution was around 1:1.4:6.5. Specifically, the LLN approximation was the fastest. We summarize the time analysis of the first three sections in Table 4.

(b) Results for control variable (ground truth of $\pmb { \beta } _ { 2 }$ is 1)  
![](/api/attachments/UYSYHYE6/fulltext/images/208cb319e9d70c290fb749b5b2f0542de468578b92cfd735152c5ff701033b13.jpg)

![](/api/attachments/UYSYHYE6/fulltext/images/46d1cfb7b1b9f724b5ebb13247f1ab1adf8ea1f3ea7ef505b81306bbee3c1d03.jpg)

$$
\beta_ {1}
$$

Note: Naïve. $\beta _ { 1 }$ refers to the coefficient of ${ \bar { X _ { i } } }$ without correction; Corr. CLT. $\beta _ { 1 }$ refers to the coefficient of ${ \bar { X _ { i } } }$ after applying the CLT approximation solution. Corr. LLN. $. \beta _ { 1 }$ refers to the coefficient of ${ \bar { X } } _ { i }$ after applying the LLN approximation solution. Corr $. \beta _ { 1 }$ refers to the coefficient of ${ \bar { X } } _ { i }$ after using our exact solution. $\beta _ { 2 }$ refers to the coefficient of $Z _ { i } .$

Figure 3. Simulation Results for Case 1 (Large Sample Case)

<table><tr><td colspan="4">Table 4. CPU Run Time Analysis (minutes)</td></tr><tr><td></td><td>Exact</td><td>CLT</td><td>LLN</td></tr><tr><td>Complexity</td><td> $O(M_i^2)$ </td><td> $O(M_i)$ </td><td> $O(1)$ </td></tr><tr><td>CPU run time for Case 1</td><td>32.363</td><td>7.085</td><td>5.107</td></tr><tr><td>CPU run time for Case 2</td><td>48.989</td><td>14.830</td><td>None</td></tr><tr><td>CPU run time for Case 3</td><td>54.801</td><td>24.834</td><td>15.509</td></tr></table>

## Case 2: Sum of Proxy Variable as the Focal Independent Variable

We simulated data using the following logistic regression model with coefficients of 1 for both right-side variables in the econometric stage:

$$
\mathrm{P} \big (Y _ {i} = 1 | S _ {X _ {i}}, Z _ {i} \big) = \frac {\exp \big (- 2 + S _ {X _ {i}} + Z _ {i} \big)}{1 + \exp \big (- 2 + S _ {X _ {i}} + Z _ {i} \big)},\tag{17}
$$

where $\begin{array} { r } { S _ { X _ { i } } = \sum _ { j = 1 } ^ { M _ { i } } X _ { i } ^ { j } . ~ M _ { i } } \end{array}$ is the total number of reviews. $M _ { i }$ is from the actual dataset and $S _ { X _ { i } }$ was simulated by randomly sampling $M _ { i }$ reviews from the actual dataset. $S _ { X _ { i } }$ is the sum of review sentiment. $Z _ { i }$ is a control variable and simulated by $Z _ { i } = - 0 . 5 \times S _ { X _ { i } } + \varepsilon _ { i } . \varepsilon _ { i }$ follows the normal distribution with a mean of 0 and a standard error of 5. Given the values of $S _ { X _ { i } }$ and $Z _ { i }$ , the values of $\mathsf { P } ( Y _ { i } = 1 | S _ { X _ { i } } , Z _ { i } )$ were computed by Equation (17) accordingly. Finally, the Bernoulli distribution was utilized to generate $Y _ { i } .$

## Evaluation of the Exact Solution for Small Sample Case

In the first-best regression analysis, the empirical coefficients for $S _ { X _ { i } }$ and $Z _ { i }$ were 0.992 and 0.983, respectively. Similar to Case 1, we also constructed 50 classifiers. For each classifier, we ran the naïve regression by using the sum of the proxy variable $( S _ { W _ { i } } )$ as the focal independent variable, and the estimated coefficient was much smaller than 1. Next, we derived the corrected coefficients for $S _ { X _ { i } }$ and $Z _ { i } .$ . Figure 4a and Figure 4b show that our method can produce consistent estimations for almost all classifiers.

Note: The legend entries are the same as Figure 2. Figure 4. Simulation Results for Case 2 (Small Sample Case)  
![](/api/attachments/UYSYHYE6/fulltext/images/ebcb89c6c9e19cdd77d68af27b5e86d078d0ad866bc120beacc7d0681f2909f7.jpg)

$$
\beta_ {1}
$$

![](/api/attachments/UYSYHYE6/fulltext/images/1c364c991d56cc362d34aa1189908e234ec70b7e3782ff8a8b122104f1593ca0.jpg)  
(b) Results for Control Variable (Ground Truth of $\pmb { \beta } _ { 2 }$ is 1)

## Evaluation of the Approximated Solutions for Large Sample Case

In the first-best regression analysis, the empirical coefficients for $S _ { X _ { i } }$ and $Z _ { i }$ were 0.938 and 0.954. Naïve regression again produced biased results. In contrast to the Case 1 Results section, we only had two but not three solutions because LLN was not applicable to the sum of sentiment scores. First, we applied the exact solution to the observations aggregated by less than 10 reviews and applied CLT approximation to the observations aggregated by more than 100 reviews. In the second method, we applied the exact solution to the whole dataset to derive the corrected coefficients. The results are shown as dashed lines and dotted lines in Figure 5, respectively. The figures show that the dashed lines and dotted lines are almost identical, which implies the correction effectiveness of the CLT approximation solution. Moreover, the relative running time of CLT approximation and the exact solution was around 1:3.3, indicating that utilizing CLT approximation can achieve both speed and estimation accuracy.

## Case 3: Mean of Proxy Variable as the Dependent Variable

Because $\bar { Y } _ { i }$ is a ratio between 0 and 1, we simulated the regression model using a beta-binomial regression model with coefficients of 1 for both right-side variables:

$$
\begin{array}{r l} & {\mathrm{P} (\bar {Y} _ {i} | X _ {i}, Z _ {i})} \\ & {= \binom {M _ {i}} {M _ {i} \bar {Y} _ {i}} \frac {\mathrm{B} (\theta_ {i} \varphi_ {i} + M _ {i} \bar {Y} _ {i} , (1 - \theta_ {i}) \varphi_ {i} + M _ {i} - M _ {i} \bar {Y} _ {i})}{\mathrm{B} (\theta_ {i} \varphi_ {i} , (1 - \theta_ {i}) \varphi_ {i})},} \end{array}\tag{18}
$$

where $\begin{array} { r } { \bar { Y } _ { i } = \frac { 1 } { M _ { i } } \sum _ { j = 1 } ^ { M _ { i } } Y _ { i } ^ { j } } \end{array}$ and $\begin{array} { r } { \theta _ { i } = \operatorname { E } ( \bar { Y } _ { i } | X _ { i } , Z _ { i } ) = \frac { \exp ( 0 . 5 + X _ { i } + Z _ { i } ) } { 1 + \exp ( 0 . 5 + X _ { i } + Z _ { i } ) } . } \end{array}$ $\bar { Y _ { i } }$ is the mean of review sentiment. $M _ { i }$ is the number of reviews from the actual dataset. For the simulation process, we started by simulating $X _ { i }$ using a standard normal distribution. Second, we simulated $Z _ { i }$ by $Z _ { i } = - 0 . 5 \times X _ { i } + \varepsilon _ { i }$ where $\varepsilon _ { i }$ followed a standard normal distribution. Third, given the values of $X _ { i }$ and $Z _ { i }$ , we derived $\mathbb { E } ( \overline { { Y } } _ { i } | X _ { i } , Z _ { i } )$ using $\frac { \exp ( 0 . 5 + X _ { i } + Z _ { i } ) } { 1 + \exp ( 0 . 5 + X _ { i } + Z _ { i } ) } .$ . Fourth, we set $\varphi _ { i }$ as 4, which implied that the correlation between binary observations within the aggregated group was 0.2. Given the simulated $\theta _ { i }$ and the value of ??<sub>??</sub>, $\mathsf { P } ( \overline { { Y } } _ { i } | X _ { i } , Z _ { i } )$ was computed accordingly by Equation (18) and $M _ { i } { \bar { Y } } _ { i }$ was generated by beta-binomial distribution. Finally, we randomly matched records in actual review data with the simulated $X _ { i }$ and $Z _ { i } ,$ , where the number of reviews and the sum of review sentiment equalled $M _ { i }$ and $M _ { i } { \bar { Y } } _ { i }$

## Evaluation of the Exact Solution for Small Sample Case

In the first-best scenario, the empirical coefficients for $X _ { i }$ and $Z _ { i }$ were 1.037 and 1.004. We ran the naïve regression by using the mean of the proxy variable $( { \overline { { y } } } _ { i } )$ as the dependent variable, following Equation (12). Next, we used Equation (13) and Equation (14) to derive the corrected coefficients for $X _ { i }$ and $Z _ { i }$ . Figures 6a and 6b show that the exact solution corrected the coefficient inconsistency and was not very sensitive to the classifier performance, whereas the naïve solution’s performance was poor across all classifiers.

![](/api/attachments/UYSYHYE6/fulltext/images/55a99e25a9841efb8f6e9a0e754a6c161a21018e144dee07210441dc6eba455f.jpg)  
(a) Results for Focal Variable (Ground Truth of $\pmb { \beta } _ { 1 } \mathbf { i s } \pmb { 1 } )$

![](/api/attachments/UYSYHYE6/fulltext/images/af2dc2092eda9065a814ead25159654ac1442cbb785de1cda494eb2060dd3d85.jpg)  
(b) Results for Control Variable (Ground Truth of $\pmb { \beta } _ { 2 }$ is 1)

Note: The legend entries are the same as Figure 3.  
Figure 5. Simulation Results for Case 2 (Large Sample Case)  
![](/api/attachments/UYSYHYE6/fulltext/images/fea661d3cea80d06cdaffd7e393d641b31a12c323e29e3af3860d65e60005758.jpg)  
(a) Results for Focal Variable (Ground Truth of $\pmb { \beta _ { 1 } }$ is 1)  
Note: The legend entries are the same as Figure 2.  
Figure 6. Simulation Results for Case 3 (Small Sample Case)

Evaluation of the Approximated Solutions for Large Sample Case

In the first-best scenario, the empirical coefficients for $X _ { i }$ and $Z _ { i }$ were 1.010 and 0.997, respectively. Next, we applied three correction methods to the dataset. In the first correction method, we applied Equation (13) and Equation (14) (exact solution) to the observations aggregated by less than 10 reviews and applied the CLT approximation solution to the observations aggregated by more than 100 reviews. The results are depicted as dashed lines in Figures 7a and 7b. In the second correction method, we applied the LLN approximation solution to the observations aggregated by more than 100 reviews. The results are shown as the dotted lines in Figures 7a and 7b. In the third correction method, we applied Equation (13) and Equation (14) (exact solution) to the whole dataset to derive the corrected coefficients. The results are shown as dash-dotted lines in Figures 7a and 7b. The results show that the CLT approximation and the exact solution obtained almost the same coefficients, which indicates the effectiveness of the CLT approximation solution. However, the LLN approximation solution only partially corrected the estimation inconsistency, possibly because the sample size for aggregation was not large enough. The relative running time of LLN approximation, CLT approximation, and the exact solution was 1:1.6:3.7, which shows the superior speed of the approximated solutions.

![](/api/attachments/UYSYHYE6/fulltext/images/c886063f09c9f414015009ea9fea083ba1a6546f9f9ab9fbf22ba9ca0b500888.jpg)  
(b) Results for Control Variable (Ground Truth of $\pmb { \beta } _ { 2 }$ is 1)

## Case 4: Sum of Proxy Variable as the Dependent Variable

We simulated data using the following model with two rightside variables,

$$
\mathrm{P} (M _ {i} | X _ {i}, Z _ {i}) = \frac {\lambda_ {i} ^ {M _ {i}} e ^ {- \lambda_ {i}}}{M _ {i} !}, \lambda_ {i} = \exp \bigl (1. 5 + X _ {i} + Z _ {i} \bigr),\tag{19}
$$

$$
\begin{array}{r l} & {\mathrm{P} (S _ {Y _ {i}} | M _ {i}, X _ {i}, Z _ {i})} \\ & {= \binom {M _ {i}} {S _ {Y _ {i}}} \frac {\mathrm{B} \left(\theta_ {i} \varphi_ {i} + S _ {Y _ {i}} , (1 - \theta_ {i}) \varphi_ {i} + M _ {i} - S _ {Y _ {i}}\right)}{\mathrm{B} \left(\theta_ {i} \varphi_ {i} , (1 - \theta_ {i}) \varphi_ {i}\right)},} \end{array}\tag{20}
$$

![](/api/attachments/UYSYHYE6/fulltext/images/e9d1ecd11161f76919a7e604b2c2c93c53b8008059c11ed2ecf500402580a2af.jpg)

(a) Results for Focal Variable (Ground Truth of $\pmb { \beta _ { 1 } }$ is 1)

where $\begin{array} { r } { \theta _ { i } = \frac { \exp ( 0 . 5 + X _ { i } + Z _ { i } ) } { 1 + \exp ( 0 . 5 + X _ { i } + Z _ { i } ) } , \varphi _ { i } = 4 , Z _ { i } = - 0 . 5 \times X _ { i } + \varepsilon _ { i } , } \end{array}$ and $\begin{array} { r } { S _ { Y _ { i } } = \sum _ { j = 1 } ^ { M _ { i } } Y _ { i } ^ { j } . ~ S _ { Y _ { i } } } \end{array}$ is the sum of review sentiment. $M _ { i }$ is the number of reviews, which was simulated based on Equation (19). $X _ { i }$ and $Z _ { i }$ were simulated following the same procedure in Case 3. The simulation process for Case 4 had two stages. The first stage was used to simulate $M _ { i }$ using the Poisson model. The second stage was used to simulate $S _ { Y _ { i } }$ using betabinomial model. The simulation process of the second stage was the same as Case 3. For the first stage, given simulated values of $X _ { i }$ and $Z _ { i } ,$ , we derived $\mathrm { P } ( M _ { i } | X _ { i } , Z _ { i } )$ using Equation (19) and generated $M _ { i }$ using Poisson distribution. The equations also imply that the theoretical beta coefficients of $X _ { i }$ and $Z _ { i }$ were 1 in both models.

In this case, we needed to estimate both $\mathrm { P } ( M _ { i } | X _ { i } , Z _ { i } )$ and $\mathsf { P } ( S _ { Y _ { i } } | M _ { i } , X _ { i } , Z _ { i } )$ . We utilized the dataset for the small sample case to evaluate our method. We first ran the Poisson model to estimate $\mathsf { P } ( M _ { i } | X _ { i } , Z _ { i } )$ . The empirical coefficients for $X _ { i }$ and $Z _ { i }$ were 0.985 and 0.987, respectively. Next, we ran the betabinomial model using the sum of true review sentiment $S _ { Y _ { i } }$ to estimate $\mathsf { P } ( S _ { Y _ { i } } | M _ { i } , X _ { i } , Z _ { i } )$ . The empirical coefficients for $X _ { i }$ and $Z _ { i }$ were 1.027 and 1.022, respectively. For each classifier, we ran the naïve regression by using the sum of the proxy variable $( S _ { y _ { i } } )$ as the dependent variable. Next, we used Equation (13) and Equation (14) (exact solution) to derive the corrected coefficients for $X _ { i }$ and $Z _ { i }$ . Figures 8a and 8b show the coefficient results. All results are qualitatively the same as those in the previous three cases.

Note: The legend entries are the same as Figure 3.  
Figure 7. Simulation Results for Case 3 (Large Sample Case)  
![](/api/attachments/UYSYHYE6/fulltext/images/e7446cbcdf1ef3236040df9910fd5080f6fc3c5007541bc6d9647d1e3c519026.jpg)

$$
\beta_ {2}
$$

![](/api/attachments/UYSYHYE6/fulltext/images/39c91ea611d09edd377e39ef3865aea87875f9c7b94e2723d3c6ef2d4f04b01c.jpg)  
(a) Results for Focal (Ground Truth of $\pmb { \beta _ { 1 } }$ is 1)

![](/api/attachments/UYSYHYE6/fulltext/images/ea5f74326fa6af05c1c4bb36dd070038a219f67e747578584f3de48c734749bb.jpg)  
(a) Results for Control Variable (Ground Truth of $\pmb { \beta } _ { 2 }$ is 1)

Note: The legend entries are the same as Figure 2.  
Figure 8. Simulation Results for Case 4 (Small Sample Case)

<table><tr><td colspan="9">Table 5. Robustness Results for Case 1 and Case 2</td></tr><tr><td rowspan="2"></td><td colspan="4">Mean</td><td colspan="4">Sum</td></tr><tr><td> $Pr^{TP}$ </td><td> $Pr^{FP}$ </td><td>Naïve</td><td>Our method</td><td> $Pr^{TP}$ </td><td> $Pr^{FP}$ </td><td>Naïve</td><td>Our method</td></tr><tr><td rowspan="4">Setting 1</td><td>0.600</td><td>0.400</td><td>0.336</td><td>0.854</td><td>0.600</td><td>0.400</td><td>0.694</td><td>1.148</td></tr><tr><td>0.700</td><td>0.300</td><td>0.583</td><td>0.893</td><td>0.700</td><td>0.300</td><td>0.842</td><td>1.105</td></tr><tr><td>0.800</td><td>0.200</td><td>0.734</td><td>0.866</td><td>0.800</td><td>0.200</td><td>0.951</td><td>1.056</td></tr><tr><td>0.900</td><td>0.100</td><td>0.938</td><td>0.979</td><td>0.900</td><td>0.100</td><td>0.995</td><td>1.015</td></tr><tr><td rowspan="4">Setting 2</td><td>0.600</td><td>0.400</td><td>1.540</td><td>1.020</td><td>0.600</td><td>0.400</td><td>1.432</td><td>1.028</td></tr><tr><td>0.700</td><td>0.300</td><td>1.685</td><td>1.029</td><td>0.700</td><td>0.300</td><td>1.569</td><td>1.019</td></tr><tr><td>0.800</td><td>0.200</td><td>1.469</td><td>1.041</td><td>0.800</td><td>0.200</td><td>1.384</td><td>1.002</td></tr><tr><td>0.900</td><td>0.100</td><td>1.198</td><td>1.010</td><td>0.900</td><td>0.100</td><td>1.176</td><td>1.008</td></tr></table>

## Robustness Analysis

The validity of our correction method rests on the assumptions in the Theoretical Solutions section. For the robustness tests, we conducted experiments involving the violation of the assumptions.

## Robustness Evaluation of Assumption 2 for Case 1 and Case 2

First, we simulated the sample size of the aggregated group following uniform distribution, $M _ { i } { \sim } U ( 1 , 1 0 )$ and $M _ { i } { \sim } U ( 2 0 , 3 0 )$ for two settings $( i = 1 , \dots , 5 0 0 0 )$ . Second, we simulated $X _ { i } ^ { j }$ using:

Setting 1: $\begin{array} { r } { \mathrm { P } \big ( X _ { i } ^ { j } = 1 \big | X _ { i } ^ { j - 1 } \big ) = \frac { 1 } { 1 + \exp \left( - \alpha _ { i } + X _ { i } ^ { j - 1 } \right) } ; } \end{array}$

$$
\text { Setting   2: } \mathrm{P} (X _ {i} ^ {j} = 1 | X _ {i} ^ {j - 1}) = \frac {1}{1 + \exp (- \alpha_ {i} - X _ {i} ^ {j - 1})},
$$

where $X _ { i } ^ { 1 }$ was simulated by Bernoulli distribution with event probability $p _ { i } { \sim } U ( 0 , 1 )$ and $\begin{array} { r } { \alpha _ { i } = \log { ( \frac { p _ { i } } { 1 - p _ { i } } ) } } \end{array}$ . In this case, $X _ { i } ^ { j }$ and $X _ { i } ^ { j - 1 }$ were correlated, which violates Assumption 2 that two variables are conditionally independent. Third, we modified $X _ { i } ^ { j }$ by setting the true positive rate $( \mathrm { P r } ^ { \mathrm { T P } } )$ and false positive rate $( \mathrm { P r } ^ { \mathrm { F P } } )$ to obtain $W _ { i } ^ { j }$ . Finally, we simulated the dependent variable using $Y _ { i } = 1 + \bar { X } _ { i } + \varepsilon _ { i }$ and $Y _ { i } = 1 + S _ { X _ { i } } + \varepsilon _ { i } . \varepsilon _ { i }$ followed the standard normal distribution. In Table 5, the results show that when Assumption 2 is violated, our method can still correct the bias (closer to the correct value 1 than the naïve method). Moreover, when the classifier’s accuracy becomes better, our method’s performance becomes better.

## Robustness Evaluation of Assumption 3 for Case 3 and Case 4

First, we simulated the sample size of the aggregated group following uniform distribution for Case 3, $M _ { i } { \sim } U ( 1 , 1 0 ) \ ( i =$ $1 , \ldots , 5 0 0 0 )$ ). For Case 4, we simulated the sample size of the group following zero-truncated Poisson distribution with the mean as $\exp ( X _ { i } + 2 )$ and $X _ { i }$ following a standard normal distribution. Second, we computed the expectation of the mean of the labels by $\begin{array} { r } { \operatorname { E } ( \overline { { Y _ { i } } } ) = \frac { 1 } { 1 + \exp { ( - X _ { i } + 0 . 2 ) } } } \end{array}$ . Third, we generated the sum of labels by beta-binomial distribution with the expectation of event probability as $\operatorname { E } ( { \overline { { Y } } } _ { i } )$ and $\varphi _ { i }$ as 1. Fourth, we modified $Y _ { i } ^ { j }$ by setting $\mathrm { P r } ^ { \mathrm { \bar { T } P } }$ and $\mathrm { P r } ^ { \mathrm { F P } }$ to introduce misclassification and obtained $y _ { i } ^ { j }$ . Specifically, we simulate $y _ { i } ^ { j }$ using:

$$
\begin{array}{l} \textbf {S e t t i n g 1 : P (y _ {i} ^ {j} = 1 | Y _ {i} ^ {j} , y _ {i} ^ {j - 1}) = \frac {1}{1 + \exp (- \beta \times Y _ {i} ^ {j} - y _ {i} ^ {j - 1})}}, \\ \textbf {S e t t i n g 2 : P (y _ {i} ^ {j} = 1 | Y _ {i} ^ {j} , y _ {i} ^ {j - 1} , Y _ {i} ^ {j - 1}) = \frac {1}{1 + \exp (- \beta \times Y _ {i} ^ {j} - 0 . 5 \times y _ {i} ^ {j - 1} - 0 . 5 \times Y _ {i} ^ {j - 1})}}. \end{array}
$$

By these two equations, the assumption that $y _ { i } ^ { j }$ and $y _ { i } ^ { j - 1 }$ $( Y _ { i } ^ { j - 1 } )$ are conditionally independent is violated. In the experiments, we changed the values of $\beta$ to obtain different values of $\mathrm { P r } ^ { \mathrm { T P } }$ and $\mathrm { P r } ^ { \mathrm { { F P } } }$ . The results are reported in Table 6. The results show that when Assumption 3 is violated, our method can partially but not fully correct the bias. However, our method still outperforms the naïve method.

## Applications to Real-World Data Set

In this section, we discuss the experiments conducted with a realistic second-stage regression model similar to the models published in IS literature rather than a simulated regression model as in the Simulation section. The Amazon review data described previously were utilized to conduct experiments of evaluating the solutions for Case 1 and Case 2. We only

Table 6. Robustness Results for Case 3 and Case 4 evaluated exact solutions since most products had a small number of reviews in this dataset. For the second-stage regression, we examined the impact of product review sentiment score on product sales rank. Amazon does not publicly display the total number of units sold for a product. Therefore, we used the sales rank of each product as a proxy variable for sales, following the IS literature. In Case 1, product review sentiment was operationalized as the mean of sentiment labels of all the product reviews before the sales rank was observed. We included one control variable, product price. In Case 2, product review sentiment was operationalized as the sum of sentiment labels of the product. We included two control variables, product price, and the total number of reviews. The model specifications are given below:

$$
\begin{array}{l} \textbf {C a s e 1 :} \operatorname{Log} (R a n k) = \beta_ {1} + \beta_ {2} \operatorname{Log} (A v g _ {\text {Sent}} + 1) + \beta_ {3} \operatorname{Log} (P r i c e) + \varepsilon , \\ \textbf {C a s e 2 :} \operatorname{Log} (R a n k) = \beta_ {1} + \beta_ {2} \operatorname{Log} (S u m _ {\text {Sent}} + 1) + \beta_ {3} \operatorname{Log} (P r i c e) + \\ \beta_ {4} \operatorname{Log} (N u m + 1) + \varepsilon . \end{array}
$$

This study first conducted two regression models using true review sentiment to derive the true regression coefficients, which are reported in Table 7. The results show that the sentiment was negatively associated with the product sales rank (Lower rank means more sales). Products with more positive reviews were more likely to achieve higher sales. Furthermore, products with a higher price were more likely to obtain fewer sales. Next, similar to the Simulation section, we constructed 50 classifiers. For each classifier, we ran the naive regression by using the mean and sum of predicted sentiment as the focal independent variables (the worst case without any correction). In addition, we used our solutions to derive the corrected coefficients. Figures 9 and 10 report the results for Case 1 and Case 2, respectively. In these figures, the y-axis shows the difference between the estimated coefficients using two different methods and the true coefficient. $\beta _ { 1 } , \beta _ { 2 }$ , and $\beta _ { 3 }$ refer to the coefficient difference of the review sentiment, product price, and the number of reviews. The results of $\beta _ { 2 }$ are almost the same in both cases. Therefore, we omitted the results of $\overline { { \beta } } _ { 2 }$ for Case 2.

<table><tr><td rowspan="2"></td><td colspan="4">Mean</td><td colspan="4">Sum</td></tr><tr><td> $Pr^{TP}$ </td><td> $Pr^{FP}$ </td><td>Naïve</td><td>Our method</td><td> $Pr^{TP}$ </td><td> $Pr^{FP}$ </td><td>Naïve</td><td>Our method</td></tr><tr><td rowspan="4">Setting 1</td><td>0.708</td><td>0.507</td><td>0.183</td><td>0.798</td><td>0.735</td><td>0.521</td><td>0.288</td><td>1.001</td></tr><tr><td>0.796</td><td>0.388</td><td>0.362</td><td>0.874</td><td>0.820</td><td>0.401</td><td>0.478</td><td>0.992</td></tr><tr><td>0.869</td><td>0.259</td><td>0.565</td><td>0.965</td><td>0.888</td><td>0.277</td><td>0.670</td><td>1.023</td></tr><tr><td>0.937</td><td>0.129</td><td>0.772</td><td>0.949</td><td>0.949</td><td>0.141</td><td>0.844</td><td>1.015</td></tr><tr><td rowspan="4">Setting 2</td><td>0.725</td><td>0.471</td><td>0.260</td><td>0.883</td><td>0.756</td><td>0.491</td><td>0.338</td><td>0.969</td></tr><tr><td>0.803</td><td>0.360</td><td>0.433</td><td>0.963</td><td>0.828</td><td>0.381</td><td>0.504</td><td>0.949</td></tr><tr><td>0.873</td><td>0.245</td><td>0.607</td><td>0.983</td><td>0.893</td><td>0.261</td><td>0.674</td><td>1.003</td></tr><tr><td>0.939</td><td>0.121</td><td>0.775</td><td>0.963</td><td>0.949</td><td>0.136</td><td>0.833</td><td>0.981</td></tr></table>

<table><tr><td colspan="7">Table 7. Estimated Regression Coefficients by Using True Review Sentiments</td></tr><tr><td></td><td>Sentiment</td><td>SD</td><td>Price</td><td>SD</td><td>No. of reviews</td><td>SD</td></tr><tr><td>Case 1</td><td>-0.681</td><td>(0.047)</td><td>0.187</td><td>(0.008)</td><td></td><td></td></tr><tr><td>Case 2</td><td>-0.381</td><td>(0.022)</td><td>0.174</td><td>(0.006)</td><td>-0.542</td><td>(0.022)</td></tr></table>

![](/api/attachments/UYSYHYE6/fulltext/images/e3d1d02b0464d90da48a7ee88ca98cd3a15220d24c5dbece5d9e1e922a59e10f.jpg)  
(a) Results for Review Sentiment

![](/api/attachments/UYSYHYE6/fulltext/images/43b0047e1aef2f46587af1b30797eda503de7733fe4ec807bc9dfdefba60c107.jpg)  
(b) Results for Product Price  
Note: The legend entries are the same as Figure 2.

Figure 9. Coefficient Results for Case 1  
![](/api/attachments/UYSYHYE6/fulltext/images/d117a65ff4e7a40d4f53a70bdae5aaa5446f4b9004100c0d6384e9006c1e39ae.jpg)  
(a) Results for Review Sentiment

![](/api/attachments/UYSYHYE6/fulltext/images/025bd2e908915e693d4d8e1f2fd46c97f6292dedb9c29df1f687a7363d2d9795.jpg)  
(b) Results for No. of Reviews

Note: The legend entries are the same as Figure 2.

Figure 10. Coefficient Results for Case 2

Comparing Naïve $. \beta _ { 1 }$ with 0 indicates a substantial bias in the estimator for both scenarios in the absence of any corrective method. In contrast, an analysis of Naïve ${ \bf \nabla } \cdot \beta _ { 2 }$ versus 0 reveals that misclassification in the sentiment variable did not bias the coefficients of the product price in either case. The reason may be that the correlation coefficients between product price and both the mean and sum of review sentiment were very small.

The coefficients were only 0.006 and -0.021 with p-values of 0.542 and 0.040. Comparing Naïve ${ . \beta _ { 3 } }$ with 0 shows that the misclassification in the sentiment variable biased the coefficients of the total number of reviews. Comparing Corr. $\beta _ { 1 }$ and Corr. $\beta _ { 3 }$ with 0 underscores the efficacy of our methodology in rectifying the estimation bias.

## Discussion and Conclusion

Inspired by the pioneering work of Yang et al. (2018) and the solution proposed by Qiao and Huang (2021) for individual hybrid studies, our paper proposes a new solution for aggregate-level hybrid studies, which has not been analyzed in the literature. The contribution of our study is twofold. First, we analyzed how the regression estimation bias may vary with classification error in the prediction stage and the sample size of the aggregated group. Second, our proposed solution can improve the estimation accuracy in aggregate-level hybrid studies, which seem to be more prevalent than individual-level hybrid studies. In this study, we derived theoretical formulas of consistent estimators of regression coefficients for four common types of aggregatelevel hybrid studies. We evaluated our solutions using both simulation and real-world data analysis and our experimentation shows that our method can produce consistent regression estimators and that the estimation results are not very sensitive to classification error. The simulation and real-world application both show that our method can indeed correct the inconsistency of estimated coefficients by the naïve regression approach.

However, our proposed method may not achieve perfect correction performance if the three assumptions of our method are not satisfied. In particular, Assumptions 2 and 3 are more likely to be violated in practice. It is strongly advised that researchers endeavor to train classifiers that adhere closely to Assumptions 1-3 to ensure that the regression estimators are consistent. Given that the proposed method is more complicated than the naïve method, we recommend that researchers use the naïve approach in the following three scenarios. First, in cases where classification performance is exceedingly high (e.g., 95% or greater), the measurement error after aggregation is likely to be minimal, thereby diminishing the utility of our correction technique. Second, if empirical data indicate a breach of Assumptions 1-3, our method cannot guarantee the production of a consistent estimator. Under such circumstances, our method should be regarded as a supplementary test for the specific hybrid study. Lastly, when the mean of the proxy variable is used in regression and the sample size of aggregation is large, because of the law of large numbers, naïve methods (without any correction) with an unbiased classifier can produce consistent estimates. The importance of an unbiased classifier in the predictive stage deserves more attention from researchers engaged in hybrid studies.

The current study’s theoretical contributions are confined to certain econometric models that can be estimated by maximum likelihood estimation (MLE), such as generalized linear models, survival models, and beta-binomial models. These findings do not extend to more complex regressions, such as panel, time series, and vector autoregression models. Theoretical results of other models could be derived using a similar probabilistic approach but it is not possible to cover all cases in one paper. Second, while our approach can accommodate multi-class outputs at the predictive stage, such an extension would require further exploration of central limit theorem-based approximations due to the computational intensity of the exact solution. Third, our results may not be applicable to other aggregation functions, such as the standard deviation of the proxy variable. Fourth, when the prediction performance is poor, the variance of regression coefficient estimates may be significantly inflated despite the estimator consistency. Therefore, it is necessary to investigate the precise interplay between coefficient variance and classification accuracy. Lastly, determining the most effective data annotation strategy for enhanced regression estimation in hybrid studies remains a pertinent topic for future investigation.

## Acknowledgments

The authors thank the senior editor, the associate editor, and the anonymous reviewers for their constructive comments and valuable suggestions. This research/project was supported by the National Research Foundation, Singapore under its Industry Alignment Fund—Pre-Positioning (IAF-PP) Funding Initiative. Any opinions, findings, conclusions, or recommendations expressed in this material are those of the author(s) and do not reflect the views of National Research Foundation, Singapore.

## References

Aggarwal, R., & Singh, H. (2013). Differential influence of blogs across different stages of decision making: The case of venture capitalists. MIS Quarterly, 37(4), 1093-1112. https://doi.org/ 10.25300/MISQ/2013/37.4.05

Bentkus, V. (2005). A Lyapunov-type bound in Rd. Theory of Probability & Its Applications, 49(2), 311-323. https://doi.org/ 10.1137/S0040585X97981123

Buonaccorsi, J. P. (2010). Measurement error: models, methods, and applications. Chapman and Hall/CRC. https://doi.org/10.1201/ 9781420066586

Carroll, R. J., Ruppert, D., Crainiceanu, C. M., & Stefanski, L. A. (2006). Measurement error in nonlinear models: A modern perspective. Chapman & Hall/CRC. https://doi.org/10.1201/9781 420010138

Chan, J., & Wang, J. (2018). Hiring preferences in online labor markets: Evidence of a female hiring bias. Management Science, 64(7), 2973-2994. https://doi.org/10.1287/mnsc.2017.2756

Chen, H., Chiang, R. H., & Storey, V. C. (2012). Business intelligence and analytics: from big data to big impact. MIS Quarterly, 36(4), 1165-1188. https://doi.org/10.2307/41703503

Chen, T., & Guestrin, C. (2016). Xgboost: A scalable tree boosting system. In Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining. https://doi.org/10.1145/2939672.293978

Cook, J. R., & Stefanski, L. A. (1994). Simulation-extrapolation estimation in parametric measurement error models. Journal of the American Statistical Association, 89(428), 1314-1328. https://doi.org/10.1080/01621459.1994.10476871

Deng, S., Huang, Z. J., Sinha, A. P., & Zhao, H. (2018). The interaction between microblog sentiment and stock return: An empirical examination. MIS Quarterly, 42(3), 895-918. https://doi.org/10. 25300/MISQ/2018/1426

Feller, W. (2008). An introduction to probability theory and its applications (Vol. 2). John Wiley & Sons. https://doi.org/ 10.1080/00224065.1970.11980411

Fuller, W. A. (1987). Measurement Error Models. John Wiley & Sons. https://doi.org/10.1002/9780470316665

Ghose, A., & Ipeirotis, P. G. (2011). Estimating the helpfulness and economic impact of product reviews: Mining text and reviewer characteristics. IEEE Transactions on Knowledge and Data Engineering, 23(10), 1498-1512. https://doi.org/10.1109/TKDE. 2010.188

Ghose, A., Ipeirotis, P. G., & Li, B. (2012). Designing ranking systems for hotels on travel search engines by mining user-generated and crowdsourced content. Marketing Science, 31(3), 493-520. https://doi.org/10.1287/mksc.1110.0700

Greene, W. H. (2012). Econometric analysis. Pearson.

Gu, B., Konana, P., Raghunathan, R., & Chen, H. M. (2014). Research note—The allure of homophily in social media: Evidence from investor responses on virtual communities. Information Systems Research, 25(3), 604-617. https://doi.org/10.1287/isre.2014.0531

Gu, B., Konana, P., Rajagopalan, B., & Chen, H.-W. M. (2007). Competition among virtual communities and user valuation: The case of investing-related communities. Information Systems Research, 18(1), 68-85. https://doi.org/10.1287/isre.1070.0114

He, R., & McAuley, J. (2016). Ups and downs: Modeling the visual evolution of fashion trends with one-class collaborative filtering. In Proceedings of the 25th International Conference on World Wide Web. https://doi.org/10.1145/2872427.2883037

Huang, K.-Y., Chengalur-Smith, I., & Pinsonneault, A. (2019). Sharing is caring: Social support provision and companionship activities in healthcare virtual support communities. MIS Quarterly, 43(2), 395-424. https://doi.org/10.25300/MISQ/2019/13225

Jabr, W., Mookerjee, R., Tan, Y., & Mookerjee, V. S. (2014). Leveraging philanthropic behavior for customer support: The case of user support forums. MIS Quarterly, 38(1), 187-208. https://doi.org/10.25300/MISQ/2014/38.1.09

Küchenhoff, H., Mwalili, S. M., & Lesaffre, E. (2006). A general method for dealing with misclassification in regression: The misclassification SIMEX. Biometrics, 62(1), 85-96. https://doi.org/ 10.1111/j.1541-0420.2005.00396.x

Liu, X., Zhang, B., Susarlia, A., & Padman, R. (2020). Go to YouTube and call me in the morning: Use of social media for chronic

conditions. MIS Quarterly, 44(1), 257-283. https://doi.org/ 10.25300/MISQ/2020/15107

Lora, M. I., & Singer, J. M. (2008). Beta‐binomial/Poisson regression models for repeated bivariate counts. Statistics in Medicine, 27(17), 3366-3381. https://doi.org/10.1002/sim.3303

Lora, M. I., & Singer, J. M. (2011). Beta-binomial/gamma-Poisson regression models for repeated counts with random parameters. Brazilian Journal of Probability and Statistics, 25(2), 218-235. https://doi.org/10.1214/10-BJPS118

Luo, X., Zhang, J. J., Gu, B., & Phang, C. (2013). Expert blogs and consumer perceptions of competing brands. MIS Quarterly, 41(2), 371-395. https://doi.org/10.25300/MISQ/2017/41.2.03

Martin, B. D., Witten, D., & Willis, A. D. (2020). Modeling microbial abundances and dysbiosis with beta-binomial regression. Annals of Applied Statistics, 14(1), 94-115. https://doi.org/10.1214/19-AOA S1283

Moreno, A., & Terwiesch, C. (2014). Doing business with strangers: Reputation in online service marketplaces. Information Systems Research, 25(4), 865-886. https://doi.org/10.1214/19-AOAS1283

Murphy, K. M., & Topel, R. H. (2002). Estimation and inference in two-step econometric models. Journal of Business & Economic Statistics, 20(1), 88-97. https://doi.org/10.1198/0735001027534 10417

Oberhofer, H., & Pfaffermayr, M. (2014). Two-part models for fractional responses defined as ratios of integers. Econometrics, 2(3), 123-144. https://doi.org/10.3390/econometrics2030123

Qiao, M., & Huang, K.-W. (2021). Correcting misclassification bias in regression models with variables generated via data mining. Information Systems Research, 32(2), 462-480. https://doi.org 10.1287/isre.2020.0977

Rumsey, D. J. (2006). Probability for dummies. John Wiley & Sons.

Schader, M., & Schmid, F. (1989). Two rules of thumb for the approximation of the binomial distribution by the normal distribution. The American Statistician, 43(1), 23-24. https://doi.org/10.2307/2685162

Singh, P. V., Sahoo, N., & Mukhopadhyay, T. (2014). How to attract and retain readers in enterprise blogging? Information Systems Research, 25(1), 35-52. https://doi.org/10.1287/isre.2013.0509

Wu, J., Huang, L., & Zhao, J. L. (2019). Operationalizing regulatory focus in the digital age: Evidence from an e-commerce context. MIS Quarterly, 43(3), 745-764. https://doi.org/10.25300/MISQ 2019/14420

Yang, M., Adomavicius, G., Burtch, G., & Ren, Y. (2018). Mind the gap: Accounting for measurement error and misclassification in variables generated via data mining. Information Systems Research, 29(1), 4-24. https://doi.org/10.1287/isre.2017.0727

Zhang, S., Lee, D., Singh, P. V., & Srinivasan, K. (2016). How much is an image worth? An empirical analysis of property’s image aesthetic quality on demand at AirBNB. In Proceedings of the International Conference on Information Systems.

Zhu, J., Eickhoff, J. C., & Kaiser, M. S. (2003). Modeling the dependence between number of trials and success probability in beta‐binomial-Poisson mixture distributions. Biometrics, 59(4), 955-961. https://doi.org/10.1111/j.0006-341X.2003.00110.x

## About the Authors

Mengke Qiao is an assistant professor of information systems at the Culverhouse College of Business, University of Alabama. She received her Ph.D. in information systems and analytics from the National University of Singapore. Her research interests focus on machine learning and causal inference. Her research has been published in Information Systems Research.

Ke-Wei Huang is the executive director of Asian Institute of Digital Finance and an associate professor in the Department of

Information Systems and Analytics at the National University of Singapore (NUS). He received his Ph.D., M.Phil., and M.Sc. degrees in information systems from the Stern School of Business at New York University. His research interests include machine learning and causal inference, applied data mining in finance, IT labor economics and entrepreneurship, and the economics of IS (pricing digital goods). His research has been published in scholarly journals including Information Systems Research, Strategic Management Journal, and Production and Operations Management.

## Appendix A

## Technical Details of Case 1

## Proof of Theorem 1

Given Assumption 2, we can derive the following two equations:

$$
\mathrm{P} (X _ {i} ^ {g} | W _ {i} ^ {1}, \dots , W _ {i} ^ {M _ {i}}, Z _ {i}, \overline {{W}} _ {i}) = \mathrm{P} (X _ {i} ^ {g} | W _ {i} ^ {g}, Z _ {i}, \overline {{W}} _ {i}),\tag{21}
$$

$$
\mathrm{P} (X _ {i} ^ {g} | W _ {i} ^ {1}, \dots , W _ {i} ^ {M _ {i}}, Z _ {i}, \overline {{W}} _ {i}, X _ {i} ^ {h}) = \mathrm{P} (X _ {i} ^ {g} | W _ {i} ^ {1}, \dots , W _ {i} ^ {M _ {i}}, Z _ {i}, \overline {{W}} _ {i}).\tag{22}
$$

The first equation is derived based on the conditional independence between $X _ { i } ^ { g }$ and $W _ { i } ^ { h }$ . The second equation is based on the conditional independence between $X _ { i } ^ { g }$ and $X _ { i } ^ { h }$

Given these two equations, we can derive:

$$
\begin{array}{c} \mathrm{P} (X _ {i} ^ {1}, \ldots , X _ {i} ^ {M _ {i}} | W _ {i} ^ {1}, \ldots , W _ {i} ^ {M _ {i}}, Z _ {i}, \overline {{W}} _ {i}) \\ = \mathrm{P} (X _ {i} ^ {1} | W _ {i} ^ {1}, \ldots , W _ {i} ^ {M _ {i}}, Z _ {i}, \overline {{W}} _ {i}) \times \ldots \times \mathrm{P} (X _ {i} ^ {M _ {i}} | W _ {i} ^ {1}, \ldots , W _ {i} ^ {M _ {i}}, Z _ {i}, \overline {{W}} _ {i}) \\ = \mathrm{P} (X _ {i} ^ {1} | W _ {i} ^ {1}, Z _ {i}, \overline {{W}} _ {i}) \times \ldots \times \mathrm{P} (X _ {i} ^ {M _ {i}} | W _ {i} ^ {M _ {i}}, Z _ {i}, \overline {{W}} _ {i}) = \prod_ {j = 1} ^ {M _ {i}} \mathrm{P} (X _ {i} ^ {j} | W _ {i} ^ {j}, Z _ {i}, \overline {{W}} _ {i}). \end{array}
$$

The first equality is derived based on Equation (22) and the second equality is based on Equation (21).

Since there are only four values for $\mathsf { P } ( X _ { i } ^ { j } | W _ { i } ^ { j } , Z _ { i } , \varlimsup _ { i } )$ , given the combination of $X _ { i } ^ { 1 } , \ldots , X _ { i } ^ { M _ { i } }$ and $W _ { i } ^ { 1 } , \ldots , W _ { i } ^ { M _ { i } }$ with TP value as $h ,$ we can further derive:

$$
\begin{array}{c} \mathrm{P} (X _ {i} ^ {1}, \ldots , X _ {i} ^ {M _ {i}} | W _ {i} ^ {1}, \ldots , W _ {i} ^ {M _ {i}}, Z _ {i}, \overline {{W}} _ {i}) = \prod_ {j = 1} ^ {M _ {i}} \mathrm{P} (X _ {i} ^ {j} | W _ {i} ^ {j}, Z _ {i}, \overline {{W}} _ {i}) \\ = \underbrace {(\mathrm{Pr} _ {i} ^ {\mathrm{TP}}) ^ {h}} _ {A} \underbrace {\left(\mathrm{Pr} _ {i} ^ {\mathrm{FP}}\right) ^ {M _ {i} \overline {{W}} _ {i} - h}} _ {B} \times \underbrace {\left(\mathrm{Pr} _ {i} ^ {\mathrm{FN}}\right) ^ {M _ {i} \overline {{X}} _ {i} - h}} _ {C} \underbrace {\left(\mathrm{Pr} _ {i} ^ {\mathrm{TN}}\right) ^ {M _ {i} - M _ {i} \overline {{W}} _ {i} - (M _ {i} \overline {{X}} _ {i} - h)}} _ {D}, \end{array}
$$

where terms A, B, C, and D represent the probabilities of the true positive, false positive, false negative, and true negative observations. There are several important observations from this expression. First, this probability depends only on $\bar { W } _ { i }$ and $M _ { i } ,$ but not the combination of $W _ { i } ^ { 1 } , \ldots , W _ { i } ^ { M _ { i } }$ . Second, this probability also does not depend on the specific combination of $X _ { i } ^ { 1 } , \ldots , \bar { X } _ { i } ^ { M _ { i } }$ while it only depends on $h , { \bar { X } } _ { i } ,$ and $M _ { i } .$ In other words, the probabilities of all the combinations of $X _ { i } ^ { 1 } , \ldots , X _ { i } ^ { M _ { i } }$ and $W _ { i } ^ { 1 } , \ldots , W _ { i } ^ { M _ { i } }$ with the same ${ \bar { X } } _ { i } , { \bar { W } } _ { i } , M _ { i } ,$ and h are the same. As a result, we can derive the conditional probability for each pair of $( { \bar { X } } _ { i } , h )$ , which is a multiplicative term of two binomial distribution probabilities:

$$
\begin{array}{r l} & {\mathrm{P} (\bar {X} _ {i}, h | \overline {{W}} _ {i}, Z _ {i}) = \binom {M _ {i} \overline {{W}} _ {i}} {h} \big (\mathrm{Pr} _ {i} ^ {\mathrm{TP}} \big) ^ {h} \big (\mathrm{Pr} _ {i} ^ {\mathrm{FP}} \big) ^ {M _ {i} \overline {{W}} _ {i} - h} \times \binom {M _ {i} - M _ {i} \overline {{W}} _ {i}} {M _ {i} \bar {X} _ {i} - h} \big (\mathrm{Pr} _ {i} ^ {\mathrm{FN}} \big) ^ {M _ {i} \bar {X} _ {i} - h} \big (\mathrm{Pr} _ {i} ^ {\mathrm{TN}} \big) ^ {- (M _ {i} \bar {X} _ {i} - h)}} \\ & {\qquad = \mathrm{B} \big (h; M _ {i} \overline {{W}} _ {i}, \mathrm{Pr} _ {i} ^ {\mathrm{TP}} \big) \times \mathrm{B} \big (M _ {i} \bar {X} _ {i} - h; M _ {i} - M _ {i} \overline {{W}} _ {i}, \mathrm{Pr} _ {i} ^ {\mathrm{FN}} \big),} \end{array}
$$

where $\binom { M _ { i } \hat W _ { i } } { h }$ refers to the number of combinations where h true positive observations exist out of all the predicted positive observations $( M _ { i } \overline { { { W } } } _ { i } ) ; \left( \begin{array} { c } { { M _ { i } - M _ { i } \overline { { { W } } } _ { i } } } \\ { { M _ { i } \bar { X } _ { i } - h } } \end{array} \right)$ refers to the number of combinations where $M _ { i } { \bar { X } } _ { i } - h$ false negative observations exist out of all the predicted negative observations $( M _ { i } - M _ { i } { \bar { W } } _ { i } )$ . Finally, we can further decompose $\mathsf { P } ( \overline { { X } } _ { i } | \overline { { W } } _ { i } , Z _ { i } )$ by all possible values of true positive observations (captured by $\begin{array} { r } { h ) , \mathrm { P } ( \overline { { X } } _ { i } | \overline { { W } } _ { i } , Z _ { i } ) = \sum _ { h = 0 } ^ { M _ { i } \overline { { X } } _ { i } } \mathrm { P } ( \overline { { X } } _ { i } , h | \overline { { W } } _ { i } , Z _ { i } ) } \end{array}$

Example 1: Assume ${ \bar { X } } _ { 1 }$ is the average value of ?? (True review sentiment) from two reviews. The possible value of ${ \bar { X } } _ { 1 }$ is 0, 0.5, or 1. Similarly, the mean of the proxy variable $\boldsymbol { \overline { { W } } _ { 1 } }$ can also be 0, 0.5, or 1. Take $\bar { W } _ { 1 } = 0 . 5$ as an example, which indicates that one review is predicted as positive while the other is predicted as negative. Next, we can infer the conditional probability that $\bar { X } _ { 1 } \mathrm { { i s } } 0 , 0 . 5 , \mathrm { o r { } } 1 . \mathrm { { I f } } \bar { X } _ { 1 } = 1 _ { \mathrm { { i s } } }$ then we have one TP review and one FN review. $\begin{array} { r } { \operatorname { I f } \bar { X } _ { 1 } = 0 . } \end{array}$ , then we have one FP review and one TN review. The confusion matrices of these two examples are illustrated in Table A1 and Table A2. Given these two confusion matrices, we can calculate the conditional probability by Equation (6).

<table><tr><td colspan="4">Table A1. Confusion Matrix ( $\overline{X}_{1} = 1$ )</td></tr><tr><td></td><td> $X_{i}^{j} = 1$ </td><td> $X_{i}^{j} = 0$ </td><td>Sum</td></tr><tr><td> $W_{i}^{j} = 1$ </td><td>1</td><td>0</td><td>1</td></tr><tr><td> $W_{i}^{j} = 0$ </td><td>1</td><td>0</td><td>1</td></tr><tr><td>Sum</td><td>2</td><td>0</td><td>2</td></tr></table>

<table><tr><td colspan="4">Table A2. Confusion Matrix ( $\overline{X}_{1} = 0$ )</td></tr><tr><td></td><td> $X_{i}^{j} = 1$ </td><td> $X_{i}^{j} = 0$ </td><td>Sum</td></tr><tr><td> $W_{i}^{j} = 1$ </td><td>0</td><td>1</td><td>1</td></tr><tr><td> $W_{i}^{j} = 0$ </td><td>0</td><td>1</td><td>1</td></tr><tr><td>Sum</td><td>0</td><td>2</td><td>2</td></tr></table>

<table><tr><td colspan="4">Table A3. Confusion Matrix 1 (h = 0)</td></tr><tr><td></td><td> $X_{i}^{j} = 1$ </td><td> $X_{i}^{j} = 0$ </td><td>Sum</td></tr><tr><td> $W_{i}^{j} = 1$ </td><td>0</td><td>1</td><td>1</td></tr><tr><td> $W_{i}^{j} = 0$ </td><td>1</td><td>0</td><td>1</td></tr><tr><td>Sum</td><td>1</td><td>1</td><td>2</td></tr></table>

<table><tr><td colspan="4">Table A4. Confusion Matrix 2 (h = 1)</td></tr><tr><td></td><td> $X_{i}^{j} = 1$ </td><td> $X_{i}^{j} = 0$ </td><td>Sum</td></tr><tr><td> $W_{i}^{j} = 1$ </td><td>1</td><td>0</td><td>1</td></tr><tr><td> $W_{i}^{j} = 0$ </td><td>0</td><td>1</td><td>1</td></tr><tr><td>Sum</td><td>1</td><td>1</td><td>2</td></tr></table>

If $\bar { X } _ { 1 } = 0 . 5$ , there are two scenarios and it is the more complicated case. Either both reviews are predicted correctly or predicted wrongly. This is the additional loop over ℎ in Equation (7). We can derive two confusion matrices, which are illustrated in Table A3 and Table A4.These two matrices correspond to two possible numbers of true positive reviews (h). When ℎ equals 0 or 1, we can derive the first or second confusion matrix. Mathematically, $\bar { \mathsf P } ( \bar { X } _ { 1 } = 0 . 5 | \bar { W } _ { 1 } , Z _ { 1 } )$ can be expressed as:

$$
\mathrm{P} (\bar {X} _ {1} = 0. 5 | \overline {{W}} _ {1}, Z _ {1}) = \mathrm{P} (\bar {X} _ {1} = 0. 5, h = 0 | \overline {{W}} _ {1}, Z _ {1}) + \mathrm{P} (\bar {X} _ {1} = 0. 5, h = 1 | \overline {{W}} _ {1}, Z _ {1}),
$$

$$
\mathrm{where} \mathrm{P} (\bar {X} _ {1} = 0. 5, h = 0 | \bar {W} _ {1}, Z _ {1}) = \mathrm{B} (0; 1, \mathrm{Pr} ^ {\mathrm{TP}}) \times \mathrm{B} (1; 1, \mathrm{Pr} ^ {\mathrm{FN}}) \mathrm{and}
$$

$$
\mathrm{P} (\bar {X} _ {1} = 0. 5, h = 1 | \bar {W} _ {1}, Z _ {1}) = \mathrm{B} (1; 1, \mathrm{Pr} ^ {\mathrm{TP}}) \times \mathrm{B} (0; 1, \mathrm{Pr} ^ {\mathrm{FN}}).
$$

## Proof of Approximated Solution by Normal Distribution

For predicted positive observations, the number of TP observations follows a binomial distribution, $\mathsf { B } ( \cdot ; \mathsf { W P } , \mathsf { P r } _ { i } ^ { \mathrm { T P } } )$ . The mean and variance of this binomial distribution are,

$$
\operatorname{E} (\mathrm{TP} | \bar {W} _ {i}, Z _ {i}) = \operatorname{WP} \times \operatorname * {P r} _ {i} ^ {\mathrm{TP}}, \operatorname{Var} (\mathrm{TP} | \bar {W} _ {i}, Z _ {i}) = \operatorname{WP} \times \operatorname * {P r} _ {i} ^ {\mathrm{TP}} \times \operatorname * {P r} _ {i} ^ {\mathrm{FP}}.
$$

For predicted negative observations, the number of FN observations follows a binomial distribution, $\mathsf { B } ( \cdot ; \mathsf { W N } , \mathsf { P r } _ { i } ^ { \mathsf { F N } } )$ . The mean and variance of this binomial distribution are:

$$
\operatorname{E} (\mathrm{FN} | \bar {W} _ {i}, Z _ {i}) = \mathrm{WN} \times \operatorname * {P r} _ {i} ^ {\mathrm{FN}}, \operatorname{Var} (\mathrm{FN} | \bar {W} _ {i}, Z _ {i}) = \mathrm{WN} \times \operatorname * {P r} _ {i} ^ {\mathrm{FN}} \times \operatorname * {P r} _ {i} ^ {\mathrm{TN}}.
$$

When the sample size is large enough, two binomial distributions can be approximated by the normal distribution. Since ${ \bar { X } } _ { i }$ is a linear transformation of TP and FN $( \frac { \mathrm { T P + F N } } { M _ { i } } )$ , we can derive the mean and variance of the normal distribution of ${ \bar { X } } _ { i }$ by the following formulas:

$$
\mu_ {i} = \operatorname{E} (\bar {X} _ {i} | \bar {W} _ {i}, Z _ {i}) = \frac {1}{M _ {i}} \big [ \operatorname{E} (\mathrm{TP} | \bar {W} _ {i}, Z _ {i}) + \operatorname{E} (\mathrm{FN} | \bar {W} _ {i}, Z _ {i}) \big ] = \frac {1}{M _ {i}} \big [ \mathrm{WP} \times \mathrm{Pr} _ {i} ^ {\mathrm{TP}} + \mathrm{WN} \times \mathrm{Pr} _ {i} ^ {\mathrm{FN}} \big ].
$$

$$
\begin{array}{r} \sigma_ {i} ^ {2} = \mathrm{Var} (\bar {X} _ {i} | \bar {W} _ {i}, Z _ {i}) = \frac {1}{M _ {i} ^ {2}} \big [ \mathrm{Var} (\mathrm{TP} | \bar {W} _ {i}, Z _ {i}) + \mathrm{Var} (\mathrm{FN} | \bar {W} _ {i}, Z _ {i}) + \mathrm{Cov} (\mathrm{TP}, \mathrm{FN} | \bar {W} _ {i}, Z _ {i}) \big ] \\ = \frac {1}{M _ {i} ^ {2}} \big [ \mathrm{WP} \times \mathrm{Pr} _ {i} ^ {\mathrm{TP}} \times \mathrm{Pr} _ {i} ^ {\mathrm{FP}} + \mathrm{WN} \times \mathrm{Pr} _ {i} ^ {\mathrm{FN}} \times \mathrm{Pr} _ {i} ^ {\mathrm{TN}} \big ], \end{array}
$$

where $\mathrm { C o v } ( \mathrm { T P } , \mathrm { F N } | \bar { W } _ { i } , Z _ { i } ) = 0$ since $X _ { i } ^ { j }$ of the observations are conditionally independent under Assumption 2.

## Extension to Multiple Focal Independent Variables

Assume we have two focal independent variables $( \bar { X } _ { 1 i }$ and ${ \bar { X } } _ { 2 i } )$ constructed from two individual-level variables,<sup>13</sup> $X _ { 1 i } ^ { j }$ and $X _ { 2 i } ^ { j }$ . For example, we have 1000 products and each product has some reviews. Each review has two proxy variables, one is review sentiment with two labels (positive or negative), and the other is review subjectivity with two labels (objective or subjective). ${ \bar { X } } _ { 1 i }$ is the mean of sentiment labels and $\hat { \bar { X } } _ { 2 i }$ is the mean of the subjectivity labels for product ??. The true regression model is defined as $\mathsf { P } ( Y _ { i } | \bar { X } _ { 1 i } , \bar { X } _ { 2 i } , Z _ { i } )$ . Then, following the logic of Equation (5), our corrected probability function is:

$$
\mathrm{P} (Y _ {i} | \overline {{W}} _ {1 i}, \overline {{W}} _ {2 i}, Z _ {i}) = \sum_ {\bar {X} _ {1 i}, \bar {X} _ {2 i}} \mathrm{P} (Y _ {i} | \bar {X} _ {1 i}, \bar {X} _ {2 i}, Z _ {i}) \mathrm{P} (\bar {X} _ {1 i}, \bar {X} _ {2 i} | \overline {{W}} _ {1 i}, \overline {{W}} _ {2 i}, Z _ {i}).
$$

where $\mathrm { P } ( \bar { X } _ { 1 i } , \bar { X } _ { 2 i } | \bar { W } _ { 1 i } , \bar { W } _ { 2 i } , Z _ { i } )$ is the aggregate-level measurement error function. Next, we decompose this function into two terms where each term has only one focal variable:

$$
\begin{array}{r l} & {\mathrm{P} (\bar {X} _ {1 i}, \bar {X} _ {2 i} | \bar {W} _ {1 i}, \bar {W} _ {2 i}, Z _ {i}) = \mathrm{P} (\bar {X} _ {1 i} | \bar {X} _ {2 i}, \bar {W} _ {1 i}, \bar {W} _ {2 i}, Z _ {i}) \times \mathrm{P} (\bar {X} _ {2 i} | \bar {W} _ {1 i}, \bar {W} _ {2 i}, Z _ {i})} \\ & {\qquad = \mathrm{P} (\bar {X} _ {1 i} | \bar {W} _ {1 i}, \bar {W} _ {2 i}, Z _ {i}) \times \mathrm{P} (\bar {X} _ {2 i} | \bar {W} _ {1 i}, \bar {W} _ {2 i}, Z _ {i}),} \end{array}
$$

where $\mathsf P ( \bar { X } _ { 1 i } | \bar { W } _ { 1 i } , \bar { W } _ { 2 i } , Z _ { i } )$ and $\mathsf P ( \bar { X } _ { 2 i } | \bar { W } _ { 1 i } , \bar { W } _ { 2 i } , Z _ { i } )$ can be estimated following the methods in the Theoretical Solution for Case 1 section. The assumption of this decomposition is that ${ \bar { X } } _ { 1 i }$ and ${ \bar { X } } _ { 2 i }$ are conditionally independent on $\bar { W } _ { 1 i } , \bar { W } _ { 2 i } ,$ and $Z _ { i }$ . This assumption implies that ${ \bar { X } } _ { 2 i }$ cannot provide additional information for inferring the probability function of ${ \bar { X } } _ { 1 i }$ conditional on $( \hat { W } _ { 1 i } , \hat { W } _ { 2 i } , Z _ { i } )$ . In other words, we assume $\mathrm { P } ( \bar { X } _ { 1 i } | \bar { X } _ { 2 i } , \bar { W } _ { 1 i } , \bar { W } _ { 2 i } , Z _ { i } ) = \mathrm { P } ( \bar { X } _ { 1 i } | \bar { W } _ { 1 i } , \bar { W } _ { 2 i } , Z _ { i } )$ . The reason for imposing this assumption is to simplify the joint probability by the product of two marginal probabilities with only one focal variable, which can be estimated by Equation (6).

## Appendix B

## Technical Details of Case 3

## Proof of Theorem 4

Given Assumption 3, we can derive the following two equations:

$$
\mathrm{P} (y _ {i} ^ {g} | Y _ {i} ^ {1}, \dots , Y _ {i} ^ {M _ {i}}, X _ {i}) = \mathrm{P} (y _ {i} ^ {g} | Y _ {i} ^ {g}, X _ {i}),
$$

$$
\mathrm{P} (y _ {i} ^ {g} | Y _ {i} ^ {1}, \dots , Y _ {i} ^ {M _ {i}}, X _ {i}, y _ {i} ^ {h}) = \mathrm{P} (y _ {i} ^ {g} | Y _ {i} ^ {1}, \dots , Y _ {i} ^ {M _ {i}}, X _ {i}).
$$

The first equation is derived based on the conditional independence between $y _ { i } ^ { g }$ and $Y _ { i } ^ { h }$ . The second equation is based on the conditional independence between $y _ { i } ^ { g }$ and $y _ { i } ^ { h }$

Given these two equations, we can derive, $\begin{array} { r } { \mathsf { P } ( y _ { i } ^ { 1 } , \ldots , y _ { i } ^ { M _ { i } } | Y _ { i } ^ { 1 } , \ldots , Y _ { i } ^ { M _ { i } } , X _ { i } ) = \prod _ { j = 1 } ^ { M _ { i } } \mathsf { P } ( y _ { i } ^ { j } | Y _ { i } ^ { j } , X _ { i } ) . } \end{array}$

Since there are only four values for $\mathsf { P } ( y _ { i } ^ { j } | Y _ { i } ^ { j } , X _ { i } )$ , given the combination of $y _ { i } ^ { 1 } , \ldots , y _ { i } ^ { M _ { i } }$ and $Y _ { i } ^ { 1 } , \dots , Y _ { i } ^ { M _ { i } }$ with TP value as $h ,$ we can further derive:

$$
\begin{array}{c} \mathrm{P} (y _ {i} ^ {1}, \ldots , y _ {i} ^ {M _ {i}} | Y _ {i} ^ {1}, \ldots , Y _ {i} ^ {M _ {i}}, X _ {i}) = \prod_ {j = 1} ^ {M _ {i}} \mathrm{P} (y _ {i} ^ {j} | Y _ {i} ^ {j}, X _ {i}) \\ = \underbrace {\left(\mathrm{Pr} _ {i} ^ {\mathrm{TP}}\right) ^ {h}} _ {A} \underbrace {\left(\mathrm{Pr} _ {i} ^ {\mathrm{FN}}\right) ^ {M _ {i} \bar {Y} _ {i} - h}} _ {B} \times \underbrace {\left(\mathrm{Pr} _ {i} ^ {\mathrm{FP}}\right) ^ {M _ {i} \bar {y} _ {i} - h}} _ {C} \underbrace {\left(\mathrm{Pr} _ {i} ^ {\mathrm{TN}}\right) ^ {M _ {i} - M _ {i} \bar {Y} _ {i} - (M _ {i} \bar {y} _ {i} - h)}} _ {D}. \end{array}
$$

Next, we derive the conditional probability for each pair of $( { \bar { y } } _ { i } , h )$ , which is a multiplicative term of two binomial distribution probabilities:

$$
\begin{array}{r l} & {\mathrm{P} (\bar {y} _ {i}, h | \bar {Y} _ {i}, X _ {i}) = \binom {M _ {i} \bar {Y} _ {i}} {h} \big (\mathrm{Pr} _ {i} ^ {\mathrm{TP}} \big) ^ {h} \big (\mathrm{Pr} _ {i} ^ {\mathrm{FN}} \big) ^ {M _ {i} \bar {Y} _ {i} - h} \times \binom {M _ {i} - M _ {i} \bar {Y} _ {i}} {M _ {i} \bar {y} _ {i} - h} \big (\mathrm{Pr} _ {i} ^ {\mathrm{FP}} \big) ^ {M _ {i} \bar {y} _ {i} - h} \big (\mathrm{Pr} _ {i} ^ {\mathrm{TN}} \big) ^ {- (M _ {i} \bar {y} _ {i} - h)}} \\ & {\qquad = \mathrm{B} \big (h; M _ {i} \bar {Y} _ {i}, \mathrm{Pr} _ {i} ^ {\mathrm{TP}} \big) \times \mathrm{B} \big (M _ {i} \bar {y} _ {i} - h; M _ {i} - M _ {i} \bar {Y} _ {i}, \mathrm{Pr} _ {i} ^ {\mathrm{FP}} \big).} \end{array}
$$

Finally, we can decompose $\mathsf { P } ( \bar { y } _ { i } | \bar { Y } _ { i } , X _ { i } )$ by all possible values of true positive observations, $\begin{array} { r } { \mathrm { P } ( \bar { y } _ { i } | \bar { Y } _ { i } , X _ { i } ) = \sum _ { h = 0 } ^ { M _ { i } \bar { y } _ { i } } \mathrm { P } ( \bar { y } _ { i } , h | \bar { Y } _ { i } , X _ { i } ) } \end{array}$

## Measurement Error Model 2: Approximated Solution by Normal Distribution

To simplify the computation, we can apply Lyapunov central limit theorem to approximate the distribution of the mean of $y _ { i } ^ { j }$ by the normal distribution. By setting $M _ { i } { \bar { Y } } _ { i }$ as YP and $M _ { i } - M _ { i } { \bar { Y } } _ { i }$ as YN, the mean and variance of the normal density function $( f ( { \bar { y } } _ { i } | { \bar { Y } } _ { i } , X _ { i } ) )$ ) are given by:

$$
\mu_ {i} = \operatorname{E} (\bar {y} _ {i} | \bar {Y} _ {i}, X _ {i}) = \frac {1}{M _ {i}} \big [ \mathrm{YP} \times \mathrm{Pr} _ {i} ^ {\mathrm{TP}} + \mathrm{YN} \times \mathrm{Pr} _ {i} ^ {\mathrm{FP}} \big ],
$$

$$
\sigma_ {i} ^ {2} = \mathrm{Var} (\bar {y} _ {i} | \bar {Y} _ {i}, X _ {i}) = \frac {1}{M _ {i} ^ {2}} \big [ \mathrm{YP} \times \mathrm{Pr} _ {i} ^ {\mathrm{TP}} \times \mathrm{Pr} _ {i} ^ {\mathrm{FN}} + \mathrm{YN} \times \mathrm{Pr} _ {i} ^ {\mathrm{FP}} \times \mathrm{Pr} _ {i} ^ {\mathrm{TN}} \big ],
$$

where $\mathrm { C o v } ( \mathrm { T P } , \mathrm { F P } | \bar { Y } _ { i } , X _ { i } ) = 0$ since $y _ { i } ^ { j }$ of the observations are conditionally independent given Assumption 3. Next, we utilize half-unit continuity correction to derive $\mathsf { P } ( \overline { { y } } _ { i } | \overline { { Y } } _ { i } , X _ { i } )$ . Let Φ denote the cumulative distribution function of $f ( \bar { y } _ { i } | \bar { Y } _ { i } , X _ { i } )$ :

$$
\mathrm{P} (\bar {y} _ {i} | \bar {Y} _ {i}, X _ {i}) = \Phi \left(\bar {y} _ {i} + \frac {1}{M _ {i}} \times 0. 5\right) - \Phi (\bar {y} _ {i} - \frac {1}{M _ {i}} \times 0. 5).\tag{23}
$$

The rule of normal approximation by CLT is that all the values within three standard deviations around $\mathbb { E } ( \bar { y } _ { i } | \bar { Y } _ { i } , X _ { i } )$ fall within the range of $\bar { y } _ { i } \left( 0 \mathrm { t o } 1 \right)$ . All technical details of this part are qualitatively the same as Case 1.

Theorem 5: Let the labeled dataset be the random sample i.i.d drawn from the population. Suppose Assumption 3 holds, $\beta$ in Equation (11) can be approximately estimated by applying MLE to Equation (13) where $\mathrm { P } ( \bar { y } _ { i } | \bar { Y } _ { i } , X _ { i } )$ is estimated by Equation (23) when $M _ { i }$ is large enough.

## Measurement Error Model 3: Approximated Solution by Law of Large Numbers.

When $M _ { i }$ is large enough, $\bar { y } _ { i }$ converges to its conditional expectation $\mathbb { E } ( \bar { y } _ { i } | \bar { Y } _ { i } , X _ { i } )$ by the strong law of large numbers (Feller, 2008):

$$
\mathrm{P} (\bar {y} _ {i} = \mathrm{E} (\bar {y} _ {i} | \bar {Y} _ {i}, X _ {i}) | \bar {Y} _ {i}, X _ {i}) = 1.\tag{24}
$$

By modifying equality, $\bar { y } _ { i } = \mathrm { E } ( \bar { y } _ { i } | \bar { Y } _ { i } , X _ { i } )$ , we derive the formula of $\bar { Y } _ { i }$ as follows:

$$
\bar {Y} _ {i} ^ {*} = \frac {\bar {y} _ {i} - \mathrm{Pr} _ {i} ^ {\mathrm{FP}}}{\mathrm{Pr} _ {i} ^ {\mathrm{TP}} - \mathrm{Pr} _ {i} ^ {\mathrm{FP}}}.
$$

Finally, Equation (13) can be simplified to:

$$
\mathrm{P} (\bar {y} _ {i} | X _ {i}) = \mathrm{P} \big (\bar {y} _ {i} = \mathrm{E} \big (\bar {y} _ {i} | \bar {Y} _ {i} ^ {*}, X _ {i} \big) | \bar {Y} _ {i} ^ {*}, X _ {i} \big) \mathrm{P} (\bar {Y} _ {i} ^ {*} | X _ {i}) = \mathrm{P} (\bar {Y} _ {i} ^ {*} | X _ {i}).
$$

The right side of the first equality only has the term when $\bar { y } _ { i } = \mathtt { E } \big ( \bar { y } _ { i } | \bar { Y } _ { i } ^ { * } , X _ { i } \big )$ since Equation (16) implies that $\mathsf { P } \big ( \bar { y } _ { i } | \bar { Y _ { i } } ^ { * } , X _ { i } \big ) = 0$ for all other possible values of $\bar { Y } _ { i }$

Theorem 6: Let the labeled dataset be the random sample i.i.d drawn from the population. Suppose Assumption 3 holds, $\beta$ in Equation $( l I )$ can be consistently estimated by applying MLE to Equation (13) where $\mathrm { P } ( \bar { y } _ { i } | \bar { Y } _ { i } , X _ { i } )$ is estimated by Equation (24) when $M _ { i }$ is large enough.

## Appendix C

## Proof of Theoretical Analysis of Estimation Bias

## Technical Details of Expected Value and Variance of Aggregated Measurement Error

Let $\overline { { W } } _ { i } - \bar { X } _ { i } = \bar { X } _ { i } \times \left( \widehat { \mathrm { P r } } _ { i } ^ { \mathrm { T P } } - 1 \right) + ( 1 - \bar { X } _ { i } ) \times \widehat { \mathrm { P r } } _ { i } ^ { \mathrm { F P } }$ . The expectation of this measurement error is derived from the law of total expectation:

$$
\mathrm{E} (\overline {{W}} _ {i} - \bar {X} _ {i}) = \mathrm{E} \left(\mathrm{E} \big (\bar {X} _ {i} \times \big (\widehat {\mathrm{Pr}} _ {i} ^ {\mathrm{TP}} - 1 \big) + (1 - \bar {X} _ {i}) \times \widehat {\mathrm{Pr}} _ {i} ^ {\mathrm{FP}} \big | \bar {X} _ {i} \big)\right)
$$

$$
= \operatorname{E} \big (\bar {X} _ {i} \times \big (\overline {{\operatorname * {P r}}} _ {i} ^ {\mathrm{TP}} - 1 \big) + (1 - \bar {X} _ {i}) \times \overline {{\operatorname * {P r}}} _ {i} ^ {\mathrm{FP}} \big) = \operatorname{E} (\bar {X} _ {i}) \times \big (\overline {{\operatorname * {P r}}} _ {i} ^ {\mathrm{TP}} - 1 \big) + \big (1 - \operatorname{E} (\bar {X} _ {i}) \big) \times \overline {{\operatorname * {P r}}} _ {i} ^ {\mathrm{FP}}.
$$

The variance of measurement error is derived by the law of total variance:

$$
\begin{array}{r l r} & & {\mathrm{Var} (\overline {{W}} _ {i} - \bar {X} _ {i}) = \mathrm{E} \big (\mathrm{Var} (\overline {{W}} _ {i} - \bar {X} _ {i} | \bar {X} _ {i}) \big) + \mathrm{Var} (\mathrm{E} (\overline {{W}} _ {i} - \bar {X} _ {i} | \bar {X} _ {i}))} \\ & & {= \mathrm{E} \left(\frac {\bar {X} _ {i} \overline {{\mathrm{Pr}}} _ {i} ^ {\mathrm{TP}} \big (1 - \overline {{\mathrm{Pr}}} _ {i} ^ {\mathrm{TP}} \big) + (1 - \bar {X} _ {i}) \overline {{\mathrm{Pr}}} _ {i} ^ {\mathrm{FP}} \big (1 - \overline {{\mathrm{Pr}}} _ {i} ^ {\mathrm{FP}} \big)}{M _ {i}}\right) + \mathrm{Var} (\bar {X} _ {i} \times \big (\overline {{\mathrm{Pr}}} _ {i} ^ {\mathrm{TP}} - 1 \big) + (1 - \bar {X} _ {i}) \times \overline {{\mathrm{Pr}}} _ {i} ^ {\mathrm{FP}})} \\ & & {= \frac {\mathrm{E} (\bar {X} _ {i}) \overline {{\mathrm{Pr}}} _ {i} ^ {\mathrm{TP}} \big (1 - \overline {{\mathrm{Pr}}} _ {i} ^ {\mathrm{TP}} \big) + \big (1 - \mathrm{E} (\bar {X} _ {i}) \big) \overline {{\mathrm{Pr}}} _ {i} ^ {\mathrm{FP}} \big (1 - \overline {{\mathrm{Pr}}} _ {i} ^ {\mathrm{FP}} \big)}{M _ {i}} + \big (\overline {{\mathrm{Pr}}} _ {i} ^ {\mathrm{FN}} + \overline {{\mathrm{Pr}}} _ {i} ^ {\mathrm{FP}} \big) ^ {2} \mathrm{Var} (\bar {X} _ {i}).} \end{array}
$$

## Technical Details of Mean of Proxy Variable as the Focal Independent Variable

Let $\bar { W } _ { i } - \bar { X } _ { i } = \bar { e } _ { i } = \mathtt { E } ( \bar { e } _ { i } ) + \mu _ { i }$ . Given $\begin{array} { r } { \mathrm { E } ( \bar { X } _ { i } ) = \left( \frac { 1 } { \overline { { \mathrm { P r } } } ^ { \mathrm { T P } } - \overline { { \mathrm { P r } } } ^ { \mathrm { F P } } } \right) \mathrm { E } ( \overline { { W } } _ { i } ) - \frac { \overline { { \mathrm { P r } } } ^ { \mathrm { F P } } } { \overline { { \mathrm { P r } } } ^ { \mathrm { T P } } - \overline { { \mathrm { P r } } } ^ { \mathrm { F P } } } , } \end{array}$ we derive $\begin{array} { r } { \mathrm { E } ( \bar { e } _ { i } ) \ \mathrm { a s } - \left( \frac { 1 } { \overrightarrow { \mathrm { P r } } ^ { \mathrm { T P } } - \overrightarrow { \mathrm { P r } } ^ { \mathrm { F P } } } - 1 \right) \mathrm { E } ( \overrightarrow { W } _ { i } ) + \frac { \overrightarrow { \mathrm { P r } } ^ { \mathrm { F P } } } { \overrightarrow { \mathrm { P r } } ^ { \mathrm { T P } } - \overrightarrow { \mathrm { P r } } ^ { \mathrm { F P } } } . } \end{array}$

$$
\begin{array}{c} \lim _ {N \to \infty} \hat {\beta} = \beta + \beta \frac {\mathrm{Cov} (- \bar {e} _ {i} , \overline {{W}} _ {i})}{\mathrm{Var} (\overline {{W}} _ {i})} = \beta + \beta \frac {\mathrm{Cov} (- \mathrm{E} (\bar {e} _ {i}) , \overline {{W}} _ {i})}{V a r (\overline {{W}} _ {i})} + \beta \frac {\mathrm{Cov} (- \mu_ {i} , \overline {{W}} _ {i})}{V a r (\overline {{W}} _ {i})} \\ = \beta + \beta \left(\frac {1}{\overline {{\mathrm{Pr}}} ^ {\mathrm{TP}} - \overline {{\mathrm{Pr}}} ^ {\mathrm{FP}}} - 1\right) \frac {\mathrm{Cov} (\mathrm{E} (\overline {{W}} _ {i}) , \overline {{W}} _ {i})}{\mathrm{Var} (\overline {{W}} _ {i})} + \beta \frac {\mathrm{Cov} (- \mu_ {i} , \overline {{W}} _ {i})}{V a r (\overline {{W}} _ {i})}. \end{array}
$$

## Technical Details of Mean of Proxy Variable as the Dependent Variable

Let $\bar { e } _ { i } = \mathrm { E } ( \bar { e } _ { i } ) + \mu _ { i } ,$ , where $\mathrm { E } ( \bar { e } _ { i } ) = X _ { i } \beta \times ( \overline { { \mathrm { P r } } } \mathrm { ^ { T P } - } 1 ) + ( 1 - X _ { i } \beta ) \ \times \overline { { \mathrm { P r } } } ^ { \mathrm { F P } }$ conditional on $X _ { i }$ by the law of total expectation. We derive the formula of estimated $\beta$ by replacing $e _ { i }$ by $\bar { e } _ { i }$ in Equation (2):

$$
\begin{array}{l} \lim _ {N \to \infty} \hat {\beta} = \beta + \frac {\operatorname{Cov} (\bar {e} _ {i} , X _ {i})}{\operatorname{Var} (X _ {i})} = \beta + \frac {\operatorname{Cov} (\operatorname{E} (\bar {e} _ {i}) , X _ {i})}{\operatorname{Var} (X _ {i})} + \frac {\operatorname{Cov} (\mu_ {i} , X _ {i})}{\operatorname{Var} (X _ {i})} \\ = \beta + (\overline {{\operatorname* {P r}}} ^ {\mathrm{TP}} - 1 - \overline {{\operatorname* {P r}}} ^ {\mathrm{FP}}) \beta + \frac {\operatorname{Cov} (\mu_ {i} , X _ {i})}{\operatorname{Var} (X _ {i})} = (\overline {{\operatorname* {P r}}} ^ {\mathrm{TP}} - \overline {{\operatorname* {P r}}} ^ {\mathrm{FP}}) \beta , \end{array}
$$

where ${ \frac { \mathrm { C o v } ( \mu _ { i } , X _ { i } ) } { \mathrm { V a r } ( X _ { i } ) } } = 0 .$ . The proof $\mathrm { f o r } { \frac { \mathrm { C o v } ( \mu _ { i } , X _ { i } ) } { \mathrm { V a r } ( X _ { i } ) } }$ equaling 0 is based on covariance formula $\operatorname { C o v } ( A , B ) = \operatorname { E } ( A B ) - \operatorname { E } ( A ) \operatorname { E } ( B )$ and the law of total expectation:

$$
\begin{array}{r} \mu_ {i} = (X _ {i} \beta) \times \left[ (\widehat {\mathrm{Pr}} _ {i} ^ {\mathrm{TP}} - \overline {{\mathrm{Pr}}} ^ {\mathrm{TP}}) - (\widehat {\mathrm{Pr}} _ {i} ^ {\mathrm{FP}} - \overline {{\mathrm{Pr}}} ^ {\mathrm{FP}}) \right] + \widehat {\mathrm{Pr}} _ {i} ^ {\mathrm{FP}} - \overline {{\mathrm{Pr}}} ^ {\mathrm{FP}} + (\widehat {\mathrm{Pr}} _ {i} ^ {\mathrm{TP}} - \widehat {\mathrm{Pr}} _ {i} ^ {\mathrm{FP}} - 1) \varepsilon_ {i}. \\ \operatorname{Cov} (\mu_ {i}, X _ {i}) = \operatorname{E} (\mu_ {i} X _ {i}) - \operatorname{E} (\mu_ {i}) \operatorname{E} (X _ {i}) = 0. \end{array}
$$

Due to the page limit, we omitted the details.

## Technical Details for Sum of Proxy Variable as the Focal Independent Variable

Let $S _ { W _ { i } } - S _ { X _ { i } } = S _ { e _ { i } } = \operatorname { E } \left( S _ { e _ { i } } \right) + \mu _ { i }$ , where $\begin{array} { r } { \mathrm { E } \big ( S _ { e _ { i } } \big ) = - \left( \frac { 1 } { \mathtt { P r } ^ { \mathrm { T P } } - \overline { { \mathrm { P r } } } ^ { \mathrm { F P } } } - 1 \right) \mathrm { E } \big ( S _ { W _ { i } } \big ) + \frac { \overline { { \mathrm { P r } } } ^ { \mathrm { F P } } } { \overline { { \mathrm { P r } } } ^ { \mathrm { T P } } - \overline { { \mathrm { P r } } } ^ { \mathrm { F P } } } M _ { i } . } \end{array}$ . Then, we derive,

$$
\lim _ {N \to \infty} \hat {\beta} = \beta + \beta \left(\frac {1}{\overline {{\operatorname* {P r}}} ^ {\mathrm{TP}} - \overline {{\operatorname* {P r}}} ^ {\mathrm{FP}}} - 1\right) \frac {\operatorname{Cov} \bigl (\operatorname{E} (S _ {W _ {i}}) , S _ {W _ {i}} \bigr)}{\operatorname{Var} (S _ {W _ {i}})} - \beta \frac {\overline {{\operatorname* {P r}}} ^ {\mathrm{FP}}}{\overline {{\operatorname* {P r}}} ^ {\mathrm{TP}} - \overline {{\operatorname* {P r}}} ^ {\mathrm{FP}}} \rho + \beta \frac {\operatorname{Cov} \bigl (\mu_ {i} , S _ {W _ {i}} \bigr)}{\operatorname{Var} (S _ {W _ {i}})},
$$

where $\rho = { \frac { \mathrm { C o v } ( M _ { i } , S _ { W _ { i } } ) } { \mathrm { V a r } ( S _ { W _ { i } } ) } }$ . Next, we define $M _ { i } { ^ * }$ as the maximum value of $M _ { i } ,$ , and $\begin{array} { r } { s _ { i } = \frac { M _ { i } } { { M _ { i } } ^ { * } } . } \end{array}$

$$
\frac {\operatorname{Cov} \bigl (\operatorname{E} \bigl (S _ {W _ {i}} \bigr) , S _ {W _ {i}} \bigr)}{\operatorname{Var} \bigl (S _ {W _ {i}} \bigr)} = \frac {\operatorname{Cov} (s _ {i} \operatorname{E} (\overline {{W}} _ {i}) , s _ {i} \overline {{W}} _ {i})}{\operatorname{Var} (s _ {i} \overline {{W}} _ {i})}, \qquad \frac {\operatorname{Cov} \bigl (\mu_ {i} , S _ {W _ {i}} \bigr)}{\operatorname{Var} \bigl (S _ {W _ {i}} \bigr)} = \frac {\operatorname{Cov} (s _ {i} \mu_ {i} / M _ {i} , s _ {i} \overline {{W}} _ {i})}{\operatorname{Var} (s _ {i} \overline {{W}} _ {i})}.
$$

Since $s _ { i }$ is a ratio between 0 and 1, this transformation enables us to apply the law of large numbers to simplify the formula. Specifically, when $M _ { i }$ is large enough, $\bar { W } _ { i }$ will converge to $\operatorname { E } ( { \overline { { W } } } _ { i } )$ and $\mu _ { i } / M _ { i }$ will converge to 0 by the law of large numbers. Therefore, $\begin{array} { r l r } {  { \frac { \mathrm { C o v } ( s _ { i } \mathrm { E } ( \overline { { W } } _ { i } ) , s _ { i } \overline { { W } } _ { i } ) } { \mathrm { V a r } ( s _ { i } \overline { { W } } _ { i } ) } = } } \end{array}$ 1 and $\begin{array} { r } { \frac { \mathrm { C o v } ( s _ { i } \mu _ { i } / M _ { i } , s _ { i } \ W _ { i } ) } { \mathrm { V a r } ( s _ { i } \bar { W } _ { i } ) } = 0 } \end{array}$ . As a result:

$$
\lim _ {N \to \infty , M _ {i} \to \infty} \hat {\beta} = \beta \left(\frac {1}{\overline {{\mathrm{Pr}}} ^ {\mathrm{TP}} - \overline {{\mathrm{Pr}}} ^ {\mathrm{FP}}}\right) - \beta \frac {\overline {{\mathrm{Pr}}} ^ {\mathrm{FP}}}{\overline {{\mathrm{Pr}}} ^ {\mathrm{TP}} - \overline {{\mathrm{Pr}}} ^ {\mathrm{FP}}} \rho .
$$

## Technical Details for Sum of Proxy Variable as the Dependent Variable

Let $S _ { e _ { i } } = S _ { y _ { i } } - S _ { Y _ { i } } = S _ { Y _ { i } } \times \left( \widehat { \mathrm { P r } } _ { i } ^ { \mathrm { T P } } - 1 \right) + \left( M _ { i } - S _ { Y _ { i } } \right) \times \widehat { \mathrm { P r } } _ { i } ^ { \mathrm { F P } }$ . Further, $S _ { e _ { i } } = \operatorname { E } \left( S _ { e _ { i } } \right) + \mu _ { i }$ , where $\operatorname { E } \left( S _ { e _ { i } } \right) = ( X _ { i } \beta \times ( { \overline { { \operatorname { P r } } } } ^ { \mathrm { T P } } - 1 ) + ( M _ { i } -$ $X _ { i } \beta ) \ \times \overline { { \operatorname* { P r } } } ^ { \mathrm { F P } } )$ conditional on $X _ { i }$ by the law of total expectation, and $\mu _ { i } = ( X _ { i } \beta ) \times \left[ \left( \widehat { \mathrm { P r } } _ { i } ^ { \mathrm { T P } } - \overrightarrow { \mathrm { P r } } ^ { \mathrm { T P } } \right) - \left( \widehat { \mathrm { P r } } _ { i } ^ { \mathrm { F P } } - \overrightarrow { \mathrm { P r } } ^ { \mathrm { F P } } \right) \right] + M _ { i } \times ( \widehat { \mathrm { P r } } _ { i } ^ { \mathrm { F P } } - \overrightarrow { \mathrm { P r } } ^ { \mathrm { F P } } )$ $\overline { { \mathrm { P r } } } ^ { \mathrm { F P } } ) + ( \widehat { \mathrm { P r } } _ { i } ^ { \mathrm { T P } } - \widehat { \mathrm { P r } } _ { i } ^ { \mathrm { F P } } - 1 ) \varepsilon _ { i }$ . Next, we obtain:

$$
\begin{array}{c} \lim _ {N \to \infty} \hat {\beta} = \beta + \frac {\operatorname{Cov} (S _ {e _ {i}} , X _ {i})}{\operatorname{Var} (X _ {i})} = \beta + \frac {\operatorname{Cov} (\operatorname{E} (S _ {e _ {i}}) , X _ {i})}{\operatorname{Var} (X _ {i})} + \frac {\operatorname{Cov} (\mu_ {i} , X _ {i})}{\operatorname{Var} (X _ {i})} \\ = \beta + \beta (\overline {{\operatorname{Pr}}} ^ {\mathrm{TP}} - \overline {{\operatorname{Pr}}} ^ {\mathrm{FP}} - 1) + \operatorname{Pr} ^ {\mathrm{FP}} \varphi + \frac {\operatorname{Cov} (\mu_ {i} , X _ {i})}{\operatorname{Var} (X _ {i})} = \beta (\overline {{\operatorname{Pr}}} ^ {\mathrm{TP}} - \overline {{\operatorname{Pr}}} ^ {\mathrm{FP}}) + \overline {{\operatorname{Pr}}} ^ {\mathrm{FP}} \varphi , \end{array}
$$

where $\begin{array} { r } { \varphi = \frac { \operatorname { C o v } ( M _ { i } , X _ { i } ) } { \operatorname { V a r } ( X _ { i } ) } \mathrm { ~ a n d ~ } \frac { \operatorname { C o v } ( \mu _ { i } , X _ { i } ) } { \operatorname { V a r } ( X _ { i } ) } = 0 } \end{array}$ . Following a similar logic to the third part of this Appendix, we can prove that $\mathrm { C o v } ( \mu _ { i } , X _ { i } ) = 0$
