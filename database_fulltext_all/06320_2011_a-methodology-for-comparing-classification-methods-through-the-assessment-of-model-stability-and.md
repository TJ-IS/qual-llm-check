---
otero_id: 6320
otero_key: "TY7PDCE3"
title: "A methodology for comparing classification methods through the assessment of model stability and validity in variable selection"
authors: "J. Shreve; H. Schneider; O. Soysal"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.08.001"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A methodology for comparing classi<sup>fi</sup>cation methods through the assessment of model stability and validity in variable selection

J. Shreve ⁎, H. Schneider, O. Soysal

Department of Information Systems & Decision Sciences, EJ Ourso College of Business, 3190 Patrick F. Taylor Hall, Louisiana State University, Baton Rouge, LA 70803, USA

## a r t i c l e i n f o

Article history: Received 30 July 2010 Received in revised form 14 May 2011 Accepted 1 August 2011 Available online 11 August 2011

Keywords: Classi<sup>fi</sup>cation Comparison Prediction Variable selection Reliability Validity F-measure

## a b s t r a c t

Classi<sup>fi</sup>cation analysis utilizes features for separating observations into distinct groups for decision-making purposes. This study provides a systematic design for comparing the performance of six classi<sup>fi</sup>cation methods using Monte Carlo simulations and illustrates that the variable selection process is integral in comparing methodologies to ensure minimal bias, enhanced stability, and optimize performance. We quantify the variable selection bias and show that, for suf<sup>fi</sup>ciently large samples, this bias is minimized so that methods can be compared. We address topics relevant to model building and provide prescriptions for future comparisons so as to build a body of evidence for recommending their use

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

With the vast amounts of available information today, companies that employ methods for synthesizing that information stand to gain a clear competitive edge in business. Classi<sup>fi</sup>cation procedures have become an integral part of the business environment as a means of reducing data to concise information for purposes of facilitating better business decisions. Durand [12] published the <sup>fi</sup>rst of many studies aimed at developing a scoring model to predict credit repayment. Managers, auditors, and other decision-makers gain information by modeling features that allow them to predict <sup>fi</sup>rm bankruptcies [49]. Kim and Street [31] used classi<sup>fi</sup>cation procedures to better target prospective customers by identifying households most likely to respond to a solicitation letter. Chiang et al [8] used classi<sup>fi</sup>cation procedures to predict and explain consumers’ choices to purchase from either an online or traditional store. For online purchasing, recommender systems [43] provide a list of suggested items most likely to be of interest to the consumer based upon their purchase history [43]. Bolton and Hand [6] reviewed statistical methods used in detecting illegal business activities associated with money laundering and medical, insurance, and telecommunications fraud. More recently, data mining techniques have gained considerable attention for detecting <sup>fi</sup>nancial fraud [4]. More companies are recognizing that, in order to compete, they must use of data, statistical analysis, and fact-based management philosophies to drive decisions [10]. Understanding these methods is critical in their successful execution and deployment. This paper reviews various classi<sup>fi</sup>cation methods, examines the model building process, and provides a systematic approach for comparing the methods so as to build a body of evidence regarding their usefulness in various situations.

Classi<sup>fi</sup>cation procedures separate observations into two or more distinct groups by identifying features that differentiate between observations with known group membership and use these features to develop a sample speci<sup>fi</sup>c mathematical model for classifying future observations having unknown origin. The goal is to maximize the hitrate, that is, the proportion of observations correctly classi<sup>fi</sup>ed. Traditionally, two considerations must precede the development of a classi<sup>fi</sup>cation model. First, assumptions must be made about the data so as to de<sup>fi</sup>ne the appropriate model estimation approach, or classi<sup>fi</sup>cation method [14,20,29,32,38]. If the assumptions are erroneous, the accuracy of the classi<sup>fi</sup>cation model will be less than optimal. Secondly, the researcher must select a subset of q variables (for qbp) considered "best" such that the predictive accuracy is optimal. This process is referred to as model speci<sup>fi</sup>cation. There are numerous reasons for reducing the number of predictors. Parsimonious models perform better in terms of accuracy and generalizability [8,9,26,38]. The researcher may also be interested in description; that is, de<sup>fi</sup>ning a set of predictors deemed relevant to the outcome of interest. For example, Kim and Street [31] showed that their algorithm, which includes variable selection, provided maximal predictive accuracy and generalizability, while providing managers with useful information for understanding the factors driving consumer response. Levin et al [33] illustrated, through AMOS (their decision support system for Automatic MOdel

Speci<sup>fi</sup>cation), that the estimation and model speci<sup>fi</sup>cation processes must be implemented simultaneously when the goal is to enhance predictive accuracy in targeting customers most likely to respond to a solo mailing.

Once the sample-dependent ‘best’ model is speci<sup>fi</sup>ed and the associated parameter estimates are obtained, evaluation of the model focuses on two critical issues. The <sup>fi</sup>rst, validity, addresses the questions: Are the results representative of what truly exists in the population? Or, is the model correctly speci<sup>fi</sup>ed? Secondly, the researcher is concerned with replication: How likely am I to obtain the same results if I were to conduct the same procedure on repeated random samples selected from the population of interest? If the model fails in terms of these criteria, given a particular variable subset and sample size, then the classi<sup>fi</sup>cation method is useless and there is no sound basis for comparing that method.

This paper shows that to ensure validity and replicability, the variable selection process is necessary. However, variable selection, or model, bias must be addressed as well. This bias occurs when one or more predictor variables have an arti<sup>fi</sup>cial linkage to the class variable, resulting in those variables being selected as best, regardless of the true relational properties existing in the population [3,28,45]. This paper illustrates that the overall bias in estimation due, in part, to the variable selection process itself is minimized and stabilized for suf<sup>fi</sup>ciently large samples. It will further show that replicability in variable selection is established, as well, but in limited degrees for some of the methods under consideration. Once the correct model has been speci<sup>fi</sup>ed for each classi<sup>fi</sup>cation method and evidence of validity and replicability have been established for various sample sizes, there exists a systematic basis to compare the methods in terms of their abilities to both predict and describe various attributes of the population.

This paper provides a comparison of six estimation approaches in two-group classi<sup>fi</sup>cation analysis, namely linear classi<sup>fi</sup>cation function (LCF), quadratic classi<sup>fi</sup>cation function (QCF), logistic (LOG) regression, nearest-neighbor (NNA), kernel density function (KDF) classi<sup>fi</sup>cation, and decision tree (TREE) analyses for various sample sizes of 200, 400, 1000, 2500, 5000, and 10,000, and how those results compare to the population models. Because estimation approaches are not always optimal for the full set of predictors, comparisons of the estimation approaches are made for various sample sizes only after the variable selection process has been completed in order to ensure minimal bias, enhanced stability, and optimal performance. Because much attention has been given to the use of alternative measures of performance where the data are imbalanced [22], this paper looks at comparisons using the F-measure criterion for model selection as well.

This study uses a Monte Carlo simulation to show the extent to which the results of each model estimation and speci<sup>fi</sup>cation process replicate from sample to sample for various sample sizes. These simulations also provide measures of standard errors and selection bias in estimation. Because population data were available, this study assesses the validity, or the degree to which the results re<sup>fl</sup>ected the true population values. In particular, this study illustrates that using conventional sample size prescriptions provides little or no evidence of model performance with respect to replicability and validity. In fact, there is strong evidence that relatively large sample sizes are necessary to ensure adequate model performance. This experimental design is applied to population 1 and population 2, with 26,218 and 72,164 observations, respectively, to provide some evidence that sample size requirements are generalizable. The systematic design of this study provides a clear indication of which estimation approach emerges as best. Although speci<sup>fi</sup>c conclusions about the best model estimation approach apply only to these particular data sets, this study provides a framework for future comparisons of classi<sup>fi</sup>cation analyses using other sources of data.

Section 2 describes the methods of classi<sup>fi</sup>cation considered in this study, namely linear and quadratic classi<sup>fi</sup>cation, logistic regression, nearest-neighbor, kernel density function, and decision tree analyses. Section 3 summarizes the literature comparing the performance of these classi<sup>fi</sup>cation procedures under speci<sup>fi</sup>ed data conditions and argues the need for comparisons in the context of variable selection. Section 4 describes estimation and the use of population hitrates from several perspectives and how they may be used for comparative purposes, along with the de<sup>fi</sup>nition of the F-measure and the rationale for its use when data are imbalanced. There is further discussion on how the hitrates and F-measure are used for establishing validity and replicability. Section 5 discusses the importance of sample size when making statements on the validity and replicability of classi<sup>fi</sup>cation analysis results. General sample size recommendations are reviewed and limitations are suggested. Section 6 brie<sup>fl</sup>y describes the variable selection process, speci<sup>fi</sup>cally subset generation. Section 7 describes the two populations under study and the rationale for de<sup>fi</sup>ning prior probabilities where needed. The data analysis design is described for purposes of establishing both the validity and replicability of classi<sup>fi</sup>cation results. Section 8 describes the results of the classi<sup>fi</sup>cation analyses and the sample size conditions where validity and replicability are established and includes a comparison of the classi<sup>fi</sup>cation methods once established. Finally, Section 9 provides conclusions and suggests a decision support system for the practitioner when comparing classi<sup>fi</sup>cation methods.

## 2. Approaches to classi<sup>fi</sup>cation analysis

## 2.1. Multivariate normal classification rules

Consider the observation vector $X _ { u } ^ { ' } = \{ x _ { i u } : ~ x _ { I u } , ~ x _ { 2 u } , ~ . . . , ~ x _ { p u } \}$ <sup>Xu xiu x1u x2u xpu</sup>randomly selected from a multivariate normal populations where $x _ { i u } \subset \left( - \infty , \infty \right)$ . The group posterior probabilities for each observation $\mathbf { X _ { u } }$ are given by

$$
P (g | \mathbf {X} _ {u}) = \frac {\pi_ {g} | \sum_ {g} | ^ {- \frac {1}{2}} \exp \left(- \frac {1}{2} \Delta_ {u g} ^ {2}\right)}{\sum_ {g ^ {'} = 1} ^ {G} \left[ \pi_ {g ^ {'}} | \sum_ {g ^ {'}} | ^ {- \frac {1}{2}} \exp \left(- \frac {1}{2} \Delta_ {u g ^ {'}} ^ {2}\right) \right]}\tag{1}
$$

where $\pi _ { g }$ is the prior probability of group g, $\Delta _ { \mathrm { { \ u g } } } ^ { 2 } { = } ( \mathrm { { X _ { u ^ { - } } \mu _ { g } } ) ^ { * } \mathrm { { Z ^ { - 1 } } _ { g } ( \mathrm { { X _ { u ^ { - } } \mu _ { g } } ) } } }$ is the Mahalanobis squared generalized distance, μ<sup>’</sup> is the p x 1 vector that represents the expected value of the random vector $\pmb { \chi } _ { u } ,$ and $\sum _ { \mathbf { g } }$ is the $p x p$ <sup>u</sup>population covariance matrix for group g. For classi<sup>fi</sup>cation purposes, the group posterior probabilities are estimated for each $\pmb { X _ { u } }$ and that observation is assigned to the group $^ g$ <sup>Xu</sup>for which the probability of group membership is maximal; that is, where $\hat { P } ( g | X _ { u } ) > \hat { P } ( g ^ { \prime } | X _ { u } )$ for $g \neq g ^ { \prime }$ . This study investigated two methods; <sup>fi</sup>rst, linear classi<sup>fi</sup>cation [15] which uses the posterior probability de<sup>fi</sup>ned in Eq. (1) with group covariance matrices equal; and second, quadratic classi<sup>fi</sup>cation [26] where the group covariance matrices are allowed to vary.

## 2.2. Other classification models

Classical approaches to classi<sup>fi</sup>cation analysis are fully parametric; that is, under the assumption of multivariate normality, the group density functions are fully estimated using only the estimated group mean and covariance matrices. While these approaches are sometimes robust to departures from the assumptions, the researcher may choose a model which more closely re<sup>fl</sup>ects the data. Four such alternative models will be investigated in this study and are brie<sup>fl</sup>y described.

## 2.2.1. Logistic regression model

The logistic regression (LOG) analysis allows for categorical rather than multivariate normal predictor variables. In particular, for each observation unit, LOG provides estimates of the probability that the event of interest (success) will occur as a function of one or more predictor variables and is given by

$$
\hat {P} (s u c c e s s | X _ {u}) = \frac {e ^ {\hat {g} (\mathbf {X} _ {u})}}{1 + e ^ {\hat {g} (\mathbf {X} _ {u})}}\tag{2}
$$

where $\hat { g } ( \mathbf { X } _ { u } ) = b _ { 0 } + b _ { 1 } x _ { 1 u } + b _ { 2 } x _ { 2 u } + \ldots + b _ { p } x _ { p u }$ is a linear composite of the predictor variables [24]. This approach is considered partially parametric [41] as only the log of the ratio of the group density functions is modeled as a linear composite of the predictors. This rule is applied to each of the sample units, and if the probability of belonging to that group (event of interest) is greater than some cutoff value, then that unit is predicted to have originated from that group. This study employs a cutoff value of .50.

## 2.2.2. Nearest-neighbor analysis

A nearest-neighbor analysis (NNA) is a nonparametric approach based on the idea that observations close in proximity to each other are similar and originate from the same group. The NNA does not require distributional assumptions about the data in order to estimate the posterior probabilities. Instead, the largest group proportion of nearest-neighbors provides a means for estimating these probabilities [13,26]. For various M-sized neighborhoods, the probability of group membership is represented by

$$
\hat {P} (g | \mathbf {X} _ {u}) = \frac {q _ {g} \cdot m _ {g}}{\sum_ {g ^ {\prime} = 1} ^ {G} \left(q _ {g ^ {\prime}} \cdot m _ {g ^ {\prime}}\right)}\tag{3}
$$

where ${ \pmb q } _ { \mathbf { g } }$ is the sample prior probability and $\mathbf { m _ { g } }$ is the number of units <sup>g g</sup>belonging to group g. For equal prior probabilities, the M nearestneighbor rule assigns an observation to that group from which the majority of M neighbors originate. This study utilized Mahalanobis distance with pooled covariance matrix for determining distances. Based upon recommendations made by Enas and Choi [13] and Huberty [26], this study used neighborhoods of size M=5.

## 2.2.3. Kernel density function estimation

Finally, kernel density function (KDF) analysis is another nonparametric approach where density functions are estimated from the data directly. These estimated density function values, $\hat { f } ( { \bf { X } } _ { u } | g )$ for $\mathbf { g } { = } 1 , 2 , . . . , \mathbf { G }$ are then used to estimate the posterior probabilities [23,26]:

$$
\hat {P} (g | X _ {u}) = \frac {p _ {g} \hat {f} (X _ {u} | g)}{\sum_ {g ^ {\prime} = 1} ^ {G} \left(p _ {g ^ {\prime}} \hat {f} (X _ {u} | g ^ {\prime})\right)}\tag{4}
$$

While the kernel density function can have several possible forms, this study employs the normal kernel density around the point $\mathbf { X } _ { u g }$ as de<sup>fi</sup>ned by

$$
k \left(\mathbf {X} _ {u g}\right) = (2 \pi) ^ {- p / 2} r ^ {- p} \left(| \sum_ {g} |\right) ^ {- 1 / 2} \exp \left(- \frac {1}{2 r ^ {2}} \left[ \left(\mathbf {X} _ {u} - \mathbf {X} _ {u g}\right) ^ {\prime} \sum_ {g} ^ {- 1} \left(\mathbf {X} _ {u} - \mathbf {X} _ {u g}\right) \right]\right)\tag{5}
$$

where $\Sigma _ { g }$ is a diagonal matrix, r is the <sup>fi</sup>xed radius around the point $X _ { u g } ,$ and $\breve { X } _ { u }$ represents a point within a distance of r from $X _ { u g } .$ The <sup>ug u</sup>probability density function for population $^ g$ <sup>ug</sup>is then obtained by taking the average of the ${ \pmb n } _ { \mathbf { g } }$ normal kernel density estimates de<sup>fi</sup>ned by

$$
\hat {f} (X _ {u} | g) = \frac {1}{n _ {g}} \sum_ {u = 1} ^ {n _ {g}} \hat {k} \left(X _ {u g}\right)\tag{6}
$$

Speci<sup>fi</sup>cally, this study replicates the analysis identical to that of Habbema and Hermans [17] in that group covariances are allowed to vary and density estimates are based upon observations within a radius of one (r =1) from the center unit. In contrast to their investigation, this study utilizes a best-subsets analysis rather than a stepwise approach.

## 2.2.4. Decision tree analysis

The decision tree (TREE) is a classi<sup>fi</sup>cation technique that provides results both easily understood and applied and performs well across a wide range of data situations [7]. Data with a binary class variable, (1) success or (0) failure, and multiple predictor variables are placed into a single group. The analysis proceeds with splitting that group into two smaller groups based upon the best predictor, so that the number of 1's in the success group and number of 0's in the failure group are maximized or impurity is minimized. Partitioning is continued until all resulting regions are pure, or contain observations belonging to just one class. To correct for over<sup>fi</sup>tting at each partition, validation data are classi<sup>fi</sup>ed using the new decision rule to ensure that the rate of missclassi<sup>fi</sup>cation is reduced; otherwise the tree is pruned (i.e.: the set of decision rules is reduced). The result is a set of logical if-then decision rules for classi<sup>fi</sup>ying future observations. The measure of impurity used in this study for selecting the best partitioning variable is the entropy measure for a region S, de<sup>fi</sup>ned as:

$$
\operatorname{Entropy} (S) = - [ p _ {1} \log_ {2} (p _ {1}) + p _ {2} \log_ {2} (p _ {2}) ]\tag{7}
$$

where ${ \sf p } _ { 1 }$ is the proportion of observations in region S belonging to class 1 and ${ \tt p } _ { 2 }$ is the proportion of observations in region S belonging to class 2. This method requires no assumptions about the distribution nor the relationship between the classes and the predictors, such as linearity. It is also robust to outliers as the choice of a cutoff value applies more to the ordering of the variable values as opposed to the value itself. Furthermore, variable selection is intrinsic to the analysis procedure itself.

## 3. Comparison of classi<sup>fi</sup>cation approaches

An extensive set of studies exists that compares the performances of classi<sup>fi</sup>cation methods under various data conditions. Several [11,18,21,25,39] look at comparisons of LCF and LOG when the multivariate normality condition is violated. McLachlan and Byth [39] include varying distances between populations. Meshbane and Morris [40] compared LOG to LCF using 32 real data sets varying by sample sizes, relative group sizes, number of predictors, degree of group separation, and equality of covariance matrices; they [41] compared LCF and QCF under heterogeneous covariance matrices as well. Other studies extend the methods under investigation. Baron [2] used simulated data to compared LCF, LOG, KDF, and rank LDF methods by varying the distribution conditions, including degree of group separation. Finch and Schneider [14] generated several populations having normal and various nonnormal shapes and varying by degree of covariance matrix heterogeneity, degree of group separation, and group size ratios for comparing the LCF, QCF, LOG, and TREE methods. Kiang [29] simulated distortions to data such as nonnormality, nonlinearity, multicollinearity, heterogeneous covariance matrices, modality, time-dependency to compare LCF, LOG, NNA, TREE, neural networks. Bhattacharyya et al [4] compared the performance of LOG, support vector machines (SVMs), and random forests for detecting credit card fraud by varying the proportion of frauds.

Others [1,30,34,42] report the effects of variable subset size on the performance of methods. Asparoukhov and Krzanowski [1] applied thirteen classi<sup>fi</sup>cation procedures to <sup>fi</sup>ve real data sets with small $( \mathtt { p } = 6 )$ , moderate (p=10), and large (p=15 or 17), respectively, and suggested further research include the selection of the optimal predictor subset. Liu and White [34] compared NNA and TREE for variable subset sizes (p=1 to 20); both studies [1,34] used sample sizes less than 200. Nelson et al [42] cited many studies with insuf<sup>fi</sup>cient sample size; therefore, they compared <sup>fi</sup>ve methods for sample sizes up to 1500 and for predictor subsets, 10, 20, and 30, respectively. Kim [30] compared logit regression and arti<sup>fi</sup>cial neural networks, using a full set of 117 predictors and a subset of 27 variables obtained by forward selection. Finally, Steel et al [46] used the variable selection process to compare LCF and QCF under varying conditions; however, their study is limited by sample sizes of 100 for ${ \mathsf { p } } = 1 0 .$

With the exception of Steel [46], none of these take into account the full variable selection process, and thus, ignore the bias due to model misspeci<sup>fi</sup>cation. In fact, those studies that use test data for validation without variable selection are validating the model bias. The authors contend that further comparisons are only possible if variable selection is included and must be done for suf<sup>fi</sup>ciently large sample sizes so that model bias is minimized.

## 4. Hitrate estimation and the F-measure

There are three hitrates to consider when assessing classi<sup>fi</sup>cation the performance. The population hitrate is the proportion of population observations classi<sup>fi</sup>ed correctly using a classi<sup>fi</sup>cation model developed using known population parameters. The actual hitrate is the proportion of correctly classi<sup>fi</sup>ed population observations obtained when using classi<sup>fi</sup>cation rules based upon a speci<sup>fi</sup>c sample; this value is a measure of how well a sample-speci<sup>fi</sup>c rule performs in future repeated random samples. These hitrates are usually unknown because population data are not available; therefore, researchers frequently rely on an estimate of hitrate that does not depend on the distributional form of the population. That hitrate estimate, known as the apparent hitrate, is the proportion of sample observations correctly classi<sup>fi</sup>ed using the sample-speci<sup>fi</sup>c model. This hitrate is sometimes referred to as the internal hitrate.

The apparent hitrate is easy to compute; but it tends to overestimate the actual hitrate because the data used to construct the classi<sup>fi</sup>cation model are those same data used for evaluation purposes [19,37].

Ideally, the apparent hit rate is acceptable when the data are somewhat balanced; that ${ \mathrm { i } } s ,$ when the classes have similar sizes. In recent years, much attention has been focused on the issue of imbalanced data where the sample size for one class is signi<sup>fi</sup>cantly larger than that of the other class. Speci<sup>fi</sup>cally, classi<sup>fi</sup>cation methods tend to provide a higher degree of accuracy for the larger class and very little accuracy for the smaller [22]. Consider the classi<sup>fi</sup>cation matrix for the two-group case in Table 1. The apparent hitrate and the individual class hitrates are de<sup>fi</sup>ned as:

$$
\text { Apparent   hitrate } = \frac {T P + T N}{T P + F N + F P + T N},\tag{8}
$$

$$
\text { Sensitivity } = \frac {T P}{T P + F N} \quad \text { Specificity } = \frac {T N}{T N + F P}
$$

where sensitivity and speci<sup>fi</sup>city represent, respectively, the proportion of positive cases predicted correctly and the proportion of negative cases predicted correctly.

In the case of imbalanced data, if the negative cases represent the majority class, then the overall accuracy is driven by the majority class and re<sup>fl</sup>ects little information about the minority class (the positive cases). For example, if the majority class consists of 95% of the data, a classi<sup>fi</sup>cation rule would have 95% accuracy if all observations were assigned to the majority class, but ignores the fact that all observations in the minority class are incorrectly classi<sup>fi</sup>ed (speci<sup>fi</sup>city=1.0 and sensitivity=0). This is particularly problematic, for example, in the case of disease diagnosis where the existence of a disease is the rare instance. Therefore, there must be an assessment criterion that provides a high level of accuracy for the minority class while balancing the accuracy of the majority class as well.

Table 1 Classi<sup>fi</sup>cation matrix.

<table><tr><td rowspan="2">Predicted Class</td><td colspan="2">True Class</td><td rowspan="2">Total</td></tr><tr><td>POS</td><td>NEG</td></tr><tr><td>POS</td><td>True Positive (TP)</td><td>False Positive (FP)</td><td>TP + FP</td></tr><tr><td>NEG</td><td>False Negative (FN)</td><td>True Negative (TN)</td><td>FN + TN</td></tr><tr><td>Total</td><td>TP + FN</td><td>FP + TN</td><td>TP + FP + FN + TN</td></tr></table>

A common assessment criterion which is equivalent to maximizing the weighted individual class accuracies is the F-measure [48] and is de<sup>fi</sup>ned as:

$$
F - M e a s u r e = \frac {\left(1 + \beta^ {2}\right) \cdot R e c a l l \cdot P r e c i s i o n}{\beta^ {2} \cdot R e c a l l + P r e c i s i o n}\tag{9}
$$

where precision= $= \mathrm { T P / ( T P + F P ) }$ represents the proportion of observations that are predicted to originate from the minority class of those that belong to the minority class, recall (or sensitivity) ${ \bf \Lambda } = \mathrm { T P } / ( \mathrm { T P } + \mathrm { F N } )$ represents the proportion of observations in the minority class that are predicted as minority, and β represents the relative importance of precision versus recall. Like the apparent hitrate, the F-measure is zero when there is no predictive accuracy and 1.0 when all observations are correctly classi<sup>fi</sup>ed.

This paper compares the classi<sup>fi</sup>cation methods across the various sample sizes using the F-measure as an assessment criterion, with $\beta = 1$ for weighing precision and recall equally.

Because population data are available for this study, all three hitrates and the F-measures will be provided as a benchmark for assessing classi<sup>fi</sup>cation accuracy. This is used for determining at what sample size the bias in estimates is minimized by the variable subset process, subsequently allowing for comparison of classi<sup>fi</sup>cation performance across the methods under consideration.

## 5. Sample size

The goal of the researcher is to generalize to the population from which the sample is drawn and this is a function of sample size. Obviously, the larger the sample size, the better the validity of estimation and, thus, assessment of the hitrate. As the number of parameters to be estimated increases, sample size becomes a greater issue with respect to both validity and replicability. Lachenbruch [32] found hitrate estimates to be relatively stable across repeated random samples when the smallest group size was greater than three times the number of predictors. Foley [16] suggested that, for linear classi<sup>fi</sup>cation, the group sample size should be greater than three times the number of predictors. Jain and Chandrasekaran [27] argued that this criterion was too weak for pattern recognition, and proposed a ratio of at least <sup>fi</sup>ve-to-one. Our study shows that sample sizes should be much larger than previously prescribed in order to obtain the optimal model for comparisons in terms of validity and replicability. To establish adequate trends, this study will compare classi<sup>fi</sup>cation methods for samples of sizes 200, 400, 1000, 2500, 5000, and 10000 selected from the known populations.

## 6. Variable selection

The purpose of variable selection is to remove irrelevant and redundant variables, providing a subset of q variables (qbp) considered ‘best’ so that predictive accuracy is maximized. The process of variable selection consists of four steps: subset generation, subset evaluation, stopping criterion, and result validation [35]. Subset generation refers to the creation of a set of candidate variable subsets for evaluation from the $( 2 ^ { p } - 1 )$ possible subsets and falls within three different strategies: complete, sequential, and random searches [9]. An exhaustive search is a type of complete search and requires looking at all $( 2 ^ { p } - 1 )$ possible subsets so that the optimal subset is guaranteed. Sequential searches include forward, backward, and stepwise selections [26]. Forward selection starts with the single variable that has maximum group separation, then adds successive variables until no additional separation is gained. Backward elimination starts with all variables, then eliminates successive variables such that no group separation is lost. Stepwise selection starts with the single best variable, adds successive variables, but also eliminates a variable at any step when it no longer contributes to group separation. Random search algorithm use randomly selected variable subsets as starting points for subset selection. For example, random-start hill-climbing and simulated annealing obtain starting points then proceed with a sequential search. Genetic algorithms (GAs), inspired by the area of evolution, start with randomly selected subsets (chromosomes) and apply the concept of reproduction, crossover, and mutation over multiple generations until a variable subset considered most ‘<sup>fi</sup>t’ is selected [31].

Sequential search procedures are popular due to the availability of computer packages which offer quick results with relatively little effort [26]; however, these methods select variables that maximize group separation ignoring classi<sup>fi</sup>cation accuracy [17,26,36]. As a result, these methods do not always result in the optimal subset for classi<sup>fi</sup>cation and are not necessarily generalizable [47]. Random search algorithms also sacri<sup>fi</sup>ce optimality in exchange for obtaining a good solution quickly. Because this study relies on comparing models that have optimal predictive accuracy, the exhaustive all-possible subsets approach is employed [35].

## 7. Data description and design of analysis

## 7.1. Motor vehicle crash data

The United States experiences thousands of deaths and enormous economic costs each year due to motor vehicle crashes. Motor vehicle crashes are the leading cause of American deaths from 4 to 34 years of age and the third leading cause of death overall. In 2000, there were 41,821 fatalities, 5.3 million non-fatal injuries, and 27.6 million damaged vehicles [5]. The cost exceeded \$230 billion including lost productivity and wages, property damage, medical and rehabilitative costs, legal costs, emergency services, insurance costs, not to mention those intangible costs such as diminished quality-of-life. Crashes involving alcohol accounted for 16,792 fatalities (40.2% of total fatalities) and 513,000 non-fatal injuries with economic costs of \$50.9 billion. However, the true number of alcohol involved fatalities is unknown because not all drivers are tested for blood alcohol contents in fatal or injury crashes and test results of some drivers who have been tested are not reported. Thus, the number of alcohol related crashes has to be estimated.

Two populations for this study were obtained from the Fatality Analysis Reporting Systems (FARS) for Louisiana. Population 1 consists of 26,218 crashes for the year 2001 and Population 2 consists of 72,164 crashes for years 2001 through 2004, each having the class variable (ALC\_RES) coded as 1 if alcohol was involved or 0 otherwise. Research has shown that alcohol-related fatal crashes are a function of age, gender, time of day, and day of week. This study used those predictors, in addition to the report status of the attending police of<sup>fi</sup>cer, number of vehicles involved, injury severity, use of a restraint or seat belt, vehicle body type, past driving violations, nature of object hit in crash. Table 2 provides a description of the eleven predictors (p=11). It should be noted that these data are not multivariate normal nor have equal covariance matrices.

## 7.2. Defining prior probabilities

Review of similar data for several years indicates that 65% of the vehicle crashes did not involve alcohol usage, whereas 35% of crashes did; therefore, the samples of varying sizes were randomly selected from the populations of interest such that each sample consisted of 65% without and 35% with alcohol involvement. Table 3 lists the sample sizes, group size con<sup>fi</sup>gurations, and, for p=11, the ratio of smallest group size-to-number of predictors ordinarily used in sample size prescriptions.

Prior probabilities of group membership represent the probability that an observation belongs to a particular group, ignoring all other information. Classi<sup>fi</sup>cation decisions should use prior probabilities for classifying an object unless other information (predictors) overwhelmingly dictates otherwise. Rudolph and Karson [44] and Huberty [26] compared estimated hitrates for analyses using both equal and unequal priors and found higher estimated hitrates when using estimated prior probabilities than those using equal priors; therefore, this study uses prior probabilities, ${ \sf p } _ { 0 } = 0 . 6 5$ and ${ \sf p } _ { 1 } = 0 . 3 5$ , where applicable.

## 7.3. Validity and replicability

This study was designed to assess the validity and replicability of classi<sup>fi</sup>cation methods (for estimation and variable selection) to provide a basis for comparisons. For any analysis set (using one estimation method on one sample), using eleven predictors, 2047 (or 2<sup>11</sup>–1) models of distinct variable combinations were estimated and the single variable subset resulting in the largest hitrate was selected as the ‘best’ subset. These same steps were applied to each of the <sup>fi</sup>ve classi<sup>fi</sup>cation methods (LCF, QCF, LOG, NNA, and KDF) and for each of the six sample con<sup>fi</sup>gurations resulting in 61,410 sets of analyses (2047 variable subsets×5 methods×6 data sets of various sizes), plus 6 analyses for the TREE (for each of the six sample sizes because TREE does not use an all-subsets approach). The resulting 61,416 analyses were repeated using 25 random samples (resulting in a total of 1,535,250 Monte Carlo classi<sup>fi</sup>cation analyses). An additional 10,236 analyses were conducted to get comparable population optimal hitrates and F-measures (2047 variable subsets×5 methods, plus one TREE analysis) resulting in 1,545,636 total classi<sup>fi</sup>cation analyses for one population. This same approach was repeated on the second population resulting in 3,091,270 sets of analyses for the entire study. The hitrates, F-measures, and associated best subsets were recorded for all analyses for assessing the degree of replicability and validity and to provide standard errors for the all estimates. Insightful Miner 8.0 was used for TREE analyses; PROC DISCRIM (SAS 9.1.3) with a macro designed for conducting all-subset analyses was used for all other analyses.

Description of predictor variables used for selection purposes.

<table><tr><td>Variable</td><td>Description</td><td>Value Assignment</td></tr><tr><td>X1</td><td>Police Reported</td><td>0 = No Drinking, 1 = Drinking, 3 = Unknown, Missing</td></tr><tr><td>X2</td><td>Time of Accident</td><td>1 = Midnight - 4 am, 2 = 5 am - 5 pm, 3 = 6 pm - 8 pm, 4 = 9p - Midnight, 5 = Missing</td></tr><tr><td>X3</td><td>Day of Week</td><td>1 = Monday through Thursday, 2 = Friday through Sunday, 3 = Missing</td></tr><tr><td>X4</td><td>Number of Vehicles</td><td>1 = One vehicle involved, 2 = More than one vehicle involved</td></tr><tr><td>X5</td><td>Injury Severity</td><td>0 = No injury, 1 = Possibly injury, 2 = Non-incapacitating injury3 = Incapacitated, 4 = Fatal, 5 = Injury severity unknown, 6 = Died prior to accident</td></tr><tr><td>X6</td><td>Restraint Usage</td><td>1 = No restraint, 2 = Shoulder and lap restraint, 3 = Other restraint, 4 = Unknown</td></tr><tr><td>X7</td><td>Age of Driver</td><td>1 = 0-17 years, 2 = 18-20 years, 3 = 21-44 years, 4 = 45-64 years, 5 = 65-97 years, 6 = Unknown</td></tr><tr><td>X8</td><td>Vehicle Body Type</td><td>1 = Auto, 2 = SUV, 3 = Light truck, 4 = Bus, 5 = RV, 6 = Medium/Heavy truck,7 = Motor cycle, 8 = Other, 9 = Unknown</td></tr><tr><td>X9</td><td>Gender</td><td>1 = Male, 2 = Female, 3 = Unknown</td></tr><tr><td>X10</td><td>Past Violations</td><td>0 = No violations, 1 = At least one violation, 2 = Unknown</td></tr><tr><td>X11</td><td>Harm</td><td>0 = Hit nothing, 1 = Hit something, 2 = Object hit unknown</td></tr></table>

Table 3  
Group sample sizes and smallest group size-to-number of predictors ratios.

<table><tr><td></td><td>200</td><td>400</td><td>1000</td><td>2500</td><td>5000</td><td>10000</td></tr><tr><td> $n_o$ </td><td>130</td><td>260</td><td>650</td><td>1625</td><td>3250</td><td>6500</td></tr><tr><td> $n_1$ </td><td>70</td><td>140</td><td>350</td><td>875</td><td>1750</td><td>3500</td></tr><tr><td> $n_1/p$ </td><td>6.4</td><td>12.7</td><td>31.8</td><td>79.5</td><td>159.1</td><td>318.2</td></tr></table>

## 8. Results

In order to assess the abilities of the methods to re<sup>fl</sup>ect true population values, we <sup>fi</sup>rst established the optimal hitrates, F-measures, and best variable subsets when applied to the population. For population 1, LCFs were estimated for all 2047 possible variable subsets; these equations were applied to the same population to obtain the parameters; the variable subset containing variables 1 and 4 were optimal with hitrate 0.764 (Table 4). NNA performed best using variables 1 through 8 with the largest hitrate (0.882), differing only by 0.009 when compared to the TREE. Note that the optimal best variable subset for NNA is not considered best for the other methods. In fact, the TREE follows NNA with optimal variable subset 1, 2, 6, 7, 8, and 11, followed by KDF and QCF analyses with best subsets variable 1 and variables 1, 2, 4, 6, 7, 8, and 9, respectively. LCF and LOG analyses perform equally well and at optimal levels, with variables 1 and 4. These results show that performance of methods should not be compared unless the variable selection process is included; otherwise the methods may perform poorly due solely to model misspeci<sup>fi</sup>cation and not the method's inability to detect relationships in the data. The same performance ordering was found for population 2 when using both hitrate and F-measure parameters (Table 4).

Using the popualtion results, we can assess the validity and replicability of the six estimation methods at each of the six samples sizes, and accordingly compare their performance once established. Because NNA and TREE perform best and equally well on the population, we expect similar results when comparing all methods at the various sample sizes across both populations and for the F-measure criterion as well.

Consider <sup>fi</sup>rst population 1. Twenty-<sup>fi</sup>ve random samples were selected for each of the 36 method by sample size combinations (LCF, QCF, LOG, KDF, NNA, TREE by sizes 200, 400, 1000, 2500, 5000, and 10000). For each combination, 25 best subsets and their apparent hitrates were recorded and summarized (Table 5). So, for the LCF analysis at sample size 200, the average of apparent hitrates (AAH) was 0.787 with a standard error of 0.019, resulting in 7 (28%) of the 25 best subsets matching the population best subset X1X4. We used a measure of bias (an overestimate in the population hitrate) as the percent increase in the average apparent hitrate (AAH) when compared to the optimal hitrate. The LCF at sample size 200, had bias measurement 3.08% (=100\*(AAH-Optimal Hitrate)/Optimal Hitrate) meaning that 3.08% more observations were classi<sup>fi</sup>ed correctly using the sample-speci<sup>fi</sup>c estimates than expected when compared to the true hitrate 0.764.

For each classi<sup>fi</sup>cation method to exhibit both validity and replicability at the various sample sizes, sample-speci<sup>fi</sup>c results must match those results found in Table 5. In this study, a method will exhibit validity at a speci<sup>fi</sup>c sample size if the AAH is relatively ‘close’ to the optimal hitrate de<sup>fi</sup>ned by a bias measure less than 1.5% and replicability is established if the population best subset is selected 90% of the time (alpha=0.10). For LCF at sample sizes 200 and 400, the average apparent hitrates (AAH) of 0.787 and 0.776, respectively, deviate considerably from the optimal hitrate of 0.764, having a bias of 3.08 and 1.63, respectively (shaded in Table 5) and is illustrated by the divergent line graphs at those sample sizes (Fig. 1). The distance between those lines (optimal and apparent) can be attributed to several sources of bias; the bias inherent in using the apparent (internal) hitrate for estimation, the bias due to model misspeci<sup>fi</sup>cation, and sampling variability. The bias due to model misspeci<sup>fi</sup>cation is indicated by the bracket for sample size 200. Of the 2047 possible variable subsets, X1 and X4 are selected as best only 7 times (28%) and 8 times (32%) of 25 samples, respectively, thereby indicating the instability in the variable subset selected. In short, bias due to model misspeci<sup>fi</sup>cation is a problem. The results of the LCF analyses neither validate nor replicate the characteristics of the population; both prediction and description are not recommended and comparisons with other methods are impossible.

The results improve once the sample size increases. At sample sizes of 1000 and larger, the AAH values (0.768, 0.769, 0.768, and 0.768, respectively) were relatively close to the optimal hitrate with bias meaures less than 1.5%, supported by the convergent lines in Fig. 1. Weak evidence of replicability appears at sample size 1000 where the population best subset, X1X4, appears 20 (80%) times; however, replicability is established at sample sizes 2500 and larger, where the population best subset appears 23 (92%) , 24 (96%) and 25 (100%) times, respectively. At these larger sample sizes, the model bias is minimal and the distance between the lines is due only to bias in the apparent hitrates and sampling variability. In conclusion, for LCF at sample sizes 1000 and above, one expects accurate optimal hitrate estimates and correct model speci<sup>fi</sup>cation so that both prediction and description can be conducted. In the absence of population data, the analyses re<sup>fl</sup>ect the state of the population; and accordingly, the researcher's decision would have been correct given the sample data at hand. Now that replicability and validity have been established for suf<sup>fi</sup>ciently large sample sizes (1000 and greater), the LCF can be compared to other classi<sup>fi</sup>cation approaches that exhibit both replicability and validity.

For QCF analyses at sample sizes of 200 to 1000, there is considerable bias in the hitrate estimates, illustrated by the divergent lines in Fig. 1, with bias measures of 8.74, 5.11, and 2.84, respectively (shaded in Table 5). Stability in the variable selection process is absent as well. For sample sizes 2500 and larger the results improved. The AAH values were close to the optimal hitrate, 0.807, with bias measures less than 1.5%, indicating strong evidence for validity in hitrate estimation. Evidence of replicability in variable selection is weak with 7 (28%) replications and shows minimal improvement for samples 5000 and larger. The variable selection process is necessary in attaining the optimal hitrate estimate; but because replicability does not exist, using those variables for descrptive purposes is not recommended. Consequently, the QCF analysis results can be compared to other methods for hitrate estimation purposes only for samples of 2500 or larger.

Table 4 Optimal variable subsets and parameters.

<table><tr><td colspan="3">Population 1</td><td colspan="4">Population 2</td></tr><tr><td>Method</td><td>Optimal Hitrate</td><td>Variable Subset</td><td>Optimal Hitrate</td><td>Variable Subset</td><td>Optimal F-measure</td><td>Variable Subset</td></tr><tr><td>NNA</td><td>0.882</td><td>1,2,3,4,5,6,7,8</td><td>0.905</td><td>1,2,3,4,5,6,7,8,9</td><td>0.861</td><td>1,2,3,4,5,6,7,8,9</td></tr><tr><td>TREE</td><td>0.873</td><td>1,2, 6,7,8, 11</td><td>0.901</td><td>1,2, 4,5,6,7,8</td><td> $0.853^a$ </td><td>1,2, 4,5,6,7,8</td></tr><tr><td>KDF</td><td>0.837</td><td>1</td><td>0.874</td><td>1</td><td>0.817</td><td>1, 5, 11</td></tr><tr><td>QCF</td><td>0.807</td><td>1,2, ,4, 6,7,8,9</td><td>0.835</td><td>1,2,3,4,5,6,7,8,9,10</td><td>0.764</td><td>1,2, 4, 10</td></tr><tr><td>LCF</td><td>0.764</td><td>1, 4</td><td>0.780</td><td>1, 4</td><td>0.668</td><td>1, 3,4, 9,10</td></tr><tr><td>LOG</td><td>0.764</td><td>1, 4</td><td>0.780</td><td>1, 4</td><td>0.659</td><td>1, 3,4, 9,10,11</td></tr></table>

a – May not be optimal because selection criterion is entropy.

Table 5  
Average apparent hitrates, standard errors, and replications for population 1.

<table><tr><td rowspan="2" colspan="2">Method</td><td colspan="6">Sample size</td></tr><tr><td>200</td><td>400</td><td>1000</td><td>2500</td><td>5000</td><td>10000</td></tr><tr><td rowspan="2">LCF</td><td>AAH (SE)</td><td>0.787 (0.019)</td><td>0.776 (0.022)</td><td>0.768 (0.013)</td><td>0.769 (0.007)</td><td>0.768 (0.005)</td><td>0.768 (0.003)</td></tr><tr><td>BIAS(REPS)</td><td>3.08 (7)</td><td>1.63 (8)</td><td>0.51 (20)</td><td>0.64 (23)</td><td>0.47 (24)</td><td>0.56 (25)</td></tr><tr><td rowspan="2">QCF</td><td>AAH (SE)</td><td>0.877 (0.017)</td><td>0.848 (0.018)</td><td>0.830 (0.013)</td><td>0.817 (0.007)</td><td>0.814 (0.004)</td><td>0.812 (0.003)</td></tr><tr><td>BIAS(REPS)</td><td>8.74 (0)</td><td>5.11 (0)</td><td>2.84 (5)</td><td>1.26 (7)</td><td>0.85 (10)</td><td>0.57 (14)</td></tr><tr><td rowspan="2">LOG</td><td>AAH (SE)</td><td>0.789 (0.019)</td><td>0.776 (0.022)</td><td>0.768 (0.013)</td><td>0.768 (0.009)</td><td>0.767 (0.006)</td><td>0.768 (0.003)</td></tr><tr><td>BIAS(REPS)</td><td>3.29 (0)</td><td>1.60 (7)</td><td>0.49 (16)</td><td>0.57 (18)</td><td>0.41 (24)</td><td>0.54 (25)</td></tr><tr><td rowspan="2">KDF</td><td>AAH (SE)</td><td>0.967 (0.013)</td><td>0.939 (0.014)</td><td>0.898 (0.007)</td><td>0.866 (0.006)</td><td>0.848 (0.004)</td><td>0.844 (0.003)</td></tr><tr><td>BIAS(REPS)</td><td>15.51 (0)</td><td>12.16 (0)</td><td>7.35 (0)</td><td>3.47 (0)</td><td>1.33 (7)</td><td>0.81 (25)</td></tr><tr><td rowspan="2">NNA</td><td>AAH (SE)</td><td>0.895 (0.016)</td><td>0.887 (0.015)</td><td>0.887 (0.007)</td><td>0.883 (0.005)</td><td>0.881 (0.004)</td><td>0.882 (0.003)</td></tr><tr><td>BIAS(REPS)</td><td>1.47 (0)</td><td>0.52 (0)</td><td>0.50 (0)</td><td>0.08 (0)</td><td>-0.12 (0)</td><td>0.00 (4)</td></tr><tr><td rowspan="2">TREE</td><td>AAH (SE)</td><td>0.903 (0.019)</td><td>0.907 (0.016)</td><td>0.904 (0.008)</td><td>0.896 (0.006)</td><td>0.885 (0.004)</td><td>0.879 (0.003)</td></tr><tr><td>BIAS(REPS)</td><td>3.44 (0)</td><td>3.91 (0)</td><td>3.51 (0)</td><td>2.62 (0)</td><td>1.35 (0)</td><td>0.65 (0)</td></tr></table>

Comparisons of the LCF and QCF analyses can only be done where validity is established for both (n=2500). Normally, the McNemar Z test is used for testing differences in two dependent proportions; however, because of the complexity of this study, the authors used con<sup>fi</sup>dence intervals for comparison purposes. Because the probability of making a Type I error increases with each comparison, the authors use Z = 3 in the calculation of con<sup>fi</sup>dence intervals for more conservative decisions. The QCF signi<sup>fi</sup>cantly outperforms LCF for sample sizes 2500 and larger as represented by the distance between the lines (Fig. 1). The difference between the AAH values of LCF and QCF is the same as the difference in optimal hitrates (0.043) for LCF and QCF (i.e: equal to the differences in the population). While the assumptions of both LCF and QCF are violated for this data set, LCF performs poorest because it is the most restrictive of the two approaches.

The results of the LOG analysis are very similar to those for LCF. For samples of 200 and 400, the AAH values deviate considerably from the optimal hitrate, having bias measures of 3.29 and 1.60, respectively. This is illustrated by the divergent line at those sample sizes (Fig. 2). The variable subsets, X1 and X4 are selected as best 0 times (0%) and 7 times (28%), indicating instability in the variable selection process and model bias. The results of the LOG analyses neither validate nor replicate and comparisons with other methods are impossible. The results improve for sample sizes 1000 and larger. The AAH values were relatively close to the optimal hitrate of 0.764 with bias meaures under 1.5%, supported by the <sup>fl</sup>attening line in Fig. 2. Weak evidence of replicability exists at sample sizes 1000 and 2500, but is established at samples of 5000 and larger, with 24 (96%) reps and 25 reps (100%), respectively. While validity and stability in the hitrate is established at sample sizes 1000 or larger and comparisons are possible, caution should be used for description with samples of 2500 or less.

![](/api/attachments/TY7PDCE3/fulltext/images/afa5c91a5f13e6d5b89ce257814e1b8c5c6d637707f4b2e0233fd63ac5c35e8b.jpg)  
Fig. 1. Average apparent hitrates for LCF and QCF analyses for population 1.

The results of the remaining classi<sup>fi</sup>cation methods, NNA, KDF, and TREE analyses (Table 5) are illustrated in Figs. 2. For NNA, validity in the hitrate estimate is established for all sample sizes with bias measures less than 1.5%, but fails to demonstrate replicability in variable selection even at the largest sample sizes; so while variable selection is important in attaining optimal prediction and comparisons with other methods are possible, the variables should not be used for descriptive purposes. For KDF analyses, validity in hitrate estimation is attained for samples of 5000 and larger (illustrated by the <sup>fl</sup>attening of the line in Fig. 2), thereby supporting comparisons with other methods. However, replicability in variable selection exists only for sample size 10000. Finally, for TREE analyses, validity in hitrate estimation exists at a samples of 5000 and 10000 with bias measures less than 1.5%. For TREE analyses, there is no evidence of replicability at any sample size.

Now that the validity and stability in hitrate estimation has been established for all methods at sample sizes 5000 and larger (where the n -to-p ratio is 159.10), comparisons can be made using con<sup>fi</sup>dence intervals. At both sample sizes 5000 and 10000, NNA and TREE have no signi<sup>fi</sup>cant differences, but both signi<sup>fi</sup>cantly outperform KDF. KDF is better than QCF which is better than both LCF and LOG (where LCF and LOG have no signi<sup>fi</sup>cant differences). These comparative results are consistent with analyses obtained when population data were used, further illustrating the need for including the variable selection process. While replication does not exist for all methods and all sample sizes, it is important to note that the variable selection process itself is important as a means of obtaining the maximal hitrates at the various sample sizes. Note also that when NNA and TREE both emerge as best when compared to all other estimation methods, their performance is a function of the unique subset selected; use of any other variable subset would have resulted in less than optimal performance and would have had no validity in terms of future predictions. Finally, because validity is established at sample size 2500 for LCF, QCF, LOG, and NNA (not TREE nor KDF), comparisons are appropriate; NNA is signifcantly better than QCF, and QCF is better than both LCF and LOG.

![](/api/attachments/TY7PDCE3/fulltext/images/193c669daf5b5f8a93593011a04f45fca74a16d4f057f4b610197ee923ac68a5.jpg)  
Fig. 2. Comparison of methods using average apparent hitrates for population 1.

Similar results are found when analyzing hitrates across sample sizes and methods for population 2 (Table 6). As the sample size for each of the methods increases, the estimated hitrates converge to the optimal hitrates as seen in Fig. 3. Note that a visual inspection results in the same order of performance when compared to population 1 . When comparing the bias results for both populations, the sample sizes at which convergence is reached are almost identical with two exceptions. First, for population 2, TREE reached convergence at sample size 2500; whereas for population 1, convergence was reached at sample size 5000. Second, for popluation 2, QCF at sample size 400 does not seem to exhibit bias; however, under further investigation, their was one sample that provided an extremely low hitrate resulting in an average apparent hitrate lower than expected. Because bias exists through sample size 2500, comparison of results can only be done at the larger sample sizes. At sample size 10000, the results are identical to population 1; namely, NNA and TREE have no signi<sup>fi</sup>cant differences and both outperform KDF which outperforms QCF, followed by LCF and LOG which have insigni<sup>fi</sup>cant differences. For sample size 5000, NNA, TREE, KDF, and QCF have no signi<sup>fi</sup>cant differences, but all outperform both LCF and LOG. By the criteria set in this study, replication of the population best variable subset occured only at sample size 10,000 for LCF and LOG and slight evidence for KDF. So, while replication properties do not not seem to generalize to the larger population, the variable selection process itself is important for selecting models where hitrate properties do generalize. At sample size 2500, comparisons of LCF, QCF, LOG, TREE, and NNA are appropriate. Consequently, NNA and TREE perform equally well and signifcantly better than both LCF and LOG which also perform equally well. While QCF is between NNA and LOG, it does not differ from any method because of its relatively large standard error.

The trends when comparing hitrates and F-measures for population 2 are identical as well and indicated by Table 7 and Fig. 4. As the sample sizes increase, the average F-measures converge to the population Fmeasures. Assuming that F-measures can be approximated by the normal distribution, con<sup>fi</sup>dence intervals were used to test differences in performance. At sample size 10000, the results are identical to hirates;

![](/api/attachments/TY7PDCE3/fulltext/images/aa583a3c43c3b7db21233e783c729c4f4a3956fb49e79c48a9f3f6c62382a3b4.jpg)  
Fig. 3. Comparison of methods using average apparent hitrates for population 2.

namely, NNA and TREE have no signi<sup>fi</sup>cant differences and both outperform KDF which outperforms QCF, followed by LCF and LOG which have insigni<sup>fi</sup>cant differences. For sample size 5000, NNA, TREE, KDF, and QCF have no signi<sup>fi</sup>cant differences, but all outperform both LCF and LOG. Subset replication, however, does not exist when using the F-measure as a selection criterion, but subset selection itself is critical in ensuring the optimal F-measure. The authors do not de<sup>fi</sup>ne a bias measure for the F-measure, but let's assume, based upon hitrate trends, that validity is established at sample size 2500 for LCF, QCF, LOG, TREE, and NNA. The results are identical; that is, NNA and TREE perform equally well and signifcantly better than both LCF and LOG which also perform equally well.

Standard errors by population, method and sample size are illustrated in Fig. 5. For population 1, all standard errors increase (except NNA and TREE) from sample size 200 to 400. All methods have standard errors decreasing from size 400 to below 0.005 at size 10000, with LOG lagging at sizes 2500 and 5000 (Table 5). For population 2, the standard errors for LCF are extreme at sample sizes 200 and 400, and for QCF, the values are consistently larger than 0.015 through sample size 5000. KDF has an extremely low standard error at sample size 200; upon further inspection this seems to be because the hitrate estimate hits the ceiling of 1.0. With the exception of QCF, all standard errrors decrease through 10000, and resembling those for population 1 at sample sizes 5000 and 10000. Finally, for the Fmeasure, standard errors for LCF, QCF, and TREE are relatively large for sample sizes 200 and 400, but decrease through size 10000, with a lower rate of decrease for QCF. KDF has constant standard errors for sample sizes 200 and 400, then gradually decrease through size 10,000. The trends are different for both NNA and LOG. NNA has an extremely small standard error at sample size 200, increases through 1000, varies through 5000, then drops at size 10,000. LOG is relatively constant at sample sizes 200 and 400, increases at 1000, levels at 5000, and drops through 10000. Where validity exists for all methods (from sample size 2500 and larger), all standard errors decrease.

Average apparent hitrates, standard errors, and replications for population 2.

<table><tr><td rowspan="2" colspan="2">Method</td><td colspan="6">Sample size</td></tr><tr><td>200</td><td>400</td><td>1000</td><td>2500</td><td>5000</td><td>10000</td></tr><tr><td rowspan="2">LCF</td><td>AAH (SE)</td><td>0.735 (0.047)</td><td>0.760 (0.038)</td><td>0.785 (0.012)</td><td>.782 (0.009)</td><td>0.781 (0.007)</td><td>0.781 (0.003)</td></tr><tr><td>BIAS(REPS)</td><td>-5.81 (2)</td><td>-2.60 (0)</td><td>0.61 (12)</td><td>0.22 (17)</td><td>0.15 (19)</td><td>0.11 (22)</td></tr><tr><td rowspan="2">QCF</td><td>AAH (SE)</td><td>0.852 (0.022)</td><td>0.840 (0.023)</td><td>0.865 (0.018)</td><td>0.852 (0.020)</td><td>0.851 (0.016)</td><td>0.842 (0.007)</td></tr><tr><td>BIAS(REPS)</td><td>2.01 (2)</td><td>0.60 (2)</td><td>3.54 (0)</td><td>2.02 (1)</td><td>1.94 (1)</td><td>0.84 (4)</td></tr><tr><td rowspan="2">LOG</td><td>AAH (SE)</td><td>0.853 (0.020)</td><td>0.873 (0.017)</td><td>0.786 (0.013)</td><td>0.783 (0.010)</td><td>0.784 (0.006)</td><td>0.781 (0.003)</td></tr><tr><td>BIAS(REPS)</td><td>9.29 (2)</td><td>11.84 (1)</td><td>0.74 (15)</td><td>0.41 (14)</td><td>0.43 (19)</td><td>0.11 (22)</td></tr><tr><td rowspan="2">KDF</td><td>AAH (SE)</td><td>0.981 (0.009)</td><td>0.954 (0.013)</td><td>0.929 (0.008)</td><td>0.897 (0.007)</td><td>0.883 (0.006)</td><td>0.874 (0.002)</td></tr><tr><td>BIAS(REPS)</td><td>12.33 (0)</td><td>9.13 (0)</td><td>6.27 (0)</td><td>2.61 (0)</td><td>1.10 (1)</td><td>0.08 (21)</td></tr><tr><td rowspan="2">NNA</td><td>AAH (SE)</td><td>0.906 (0.017)</td><td>0.897 (0.016)</td><td>0.908 (0.008)</td><td>0.903 (0.007)</td><td>0.904 (0.005)</td><td>0.903 (0.002)</td></tr><tr><td>BIAS(REPS)</td><td>0.06 (0)</td><td>-0.91 (0)</td><td>0.33 (0)</td><td>-0.26 (0)</td><td>-0.17 (0)</td><td>-0.27 (0)</td></tr><tr><td rowspan="2">TREE</td><td>AAH (SE)</td><td>0.919 (0.017)</td><td>0.920 (0.010)</td><td>0.918 (0.007)</td><td>0.913 (0.006)</td><td>0.907 (0.005)</td><td>0.903 (0.003)</td></tr><tr><td>BIAS(REPS)</td><td>1.98 (0)</td><td>2.08 (0)</td><td>1.91 (1)</td><td>1.28 (0)</td><td>0.68 (1)</td><td>0.17 (11)</td></tr></table>

Table 7  
Average F-measures, standard errors, and replications for population 2.

<table><tr><td rowspan="2">Method</td><td colspan="6">Sample size</td></tr><tr><td>200</td><td>400</td><td>1000</td><td>2500</td><td>5000</td><td>10000</td></tr><tr><td>LCF</td><td>0.772 (0.047/0)</td><td>0.798 (0.039/4)</td><td>0.672 (0.022/3)</td><td>0.663 (0.021/3)</td><td>0.664 (0.012/7)</td><td>0.664 (0.006/17)</td></tr><tr><td>QCF</td><td>0.879 (0.021/0)</td><td>0.870 (0.023/0)</td><td>0.796 (0.022/0)</td><td>0.776 (0.022/1)</td><td>0.775 (0.017/3)</td><td>0.766 (0.004/4)</td></tr><tr><td>LOG</td><td>0.894 (0.014/0)</td><td>0.896 (0.012/0)</td><td>0.672 (0.024/1)</td><td>0.666 (0.024/0)</td><td>0.664 (0.016/1)</td><td>0.660 (0.008/3)</td></tr><tr><td>KDF</td><td>0.984 (0.007/0)</td><td>0.963 (0.011/0)</td><td>0.904 (0.018/0)</td><td>0.856 (0.010/0)</td><td>0.839 (0.013/0)</td><td>0.819 (0.005/5)</td></tr><tr><td>NNA</td><td>0.925 (0.014/0)</td><td>0.917 (0.014/0)</td><td>0.877 (0.012/0)</td><td>0.869 (0.009/0)</td><td>0.870 (0.006/0)</td><td>0.870 (0.006/0)</td></tr><tr><td>TREE</td><td>0.885 (0.023/x)</td><td>0.885 (0.018/x)</td><td>0.882 (0.012/x)</td><td>0.874 (0.011/x)</td><td>0.865 (0.008/x)</td><td>0.857 (0.006/x)</td></tr></table>

x=Does not apply to the method.

These results should be viewed in terms of their methodological implications. In practice, classi<sup>fi</sup>cation methods should be selected with respect to how closely the characteristics of the data are aligned with the associated assumptions. While the LCF method is effective in describing the population at suf<sup>fi</sup>ciently large sample sizes, it is not surprising that the LCF's performance is poorest as it is the most restrictive of the fully parametric approaches and least resembles this data. In fact, the performance of the LCF would be more competitive with other methods in cases where its assumptions are met. The QCF is also fully parametric and, thus, restrictive; but relaxing the equal variance assumption improves its performance. It should be noted also that the LCF and LOG are identical in performance, supporting the conclusions of [11,41] that these methods are equivalent when multivariate assumptions are violated.

It is also expected that the least restrictive, nonparametric procedures perform best. Both NNA and TREE methods partition the predictor spaces into decision regions; therefore performance should be comparable. In particular, NNA and TREE performed signi<sup>fi</sup>cantly better than the other methods which is consistent with the comparisons that exist for the population. While the KDF provides a smoothing alternative to parametric procedures, allowing for a better <sup>fi</sup>t, the estimates are based upon the average of the group normal density functions for a speci<sup>fi</sup>c radius about the obervation under consideration, possibly hindering the relative performance; therefore KDF falls behind NNA and TREE. These same conclusions refer to these same methods when using the F-measure as a selection criterion.

This study shows that for sample sizes 5000 and larger (n-to-p ratio 159.1 and larger), comparisons of all methods are valid, regardless of the population size. This is much larger than previously recommended sample size requirements [16,26,27,32] and may be due to the idea that larger sample sizes are required to minimize the effects of model bias. Furthermore, it should be stressed that at these sample sizes, all conclusions about estimates and relative performance of the methods re<sup>fl</sup>ect exactly what exists in the population. For sample size 2500 (n-to-p ratio 79.5), there is weak evidence of bias for TREE and KDF, so that comparisons made with those methods should be conducted with caution (and may be possible under another de<sup>fi</sup>nition of bias). The bias does seem to be minimal so that conclusions about the relative performance of all methods re<sup>fl</sup>ects the relative performance that exists in the population. Comparisons of methods at sample sizes 1000 or less should not be considered because of invalid estimates and the existence of model bias. In fact, bias effects results to the extent that the performance ordering of the methods does not match that which exists in the population. Finally, while variable subset replicability seems weak for most methods, especially when reviewing results of the larger population, the subset selection process is necessary in attaining validity. Further study is needed to establish variable selection for descriptive purposes.

![](/api/attachments/TY7PDCE3/fulltext/images/c67707dff0a2f2dfc5b1e942e3ecedbb639025d49cf4642e4eed6e920742ba00.jpg)  
Fig. 4. Comparison of methods using F-measures for population 2.

## 9. Conclusions and implications for the practioner

This study uses an analysis design in order to assess the validity and replicability of classi<sup>fi</sup>cation analyses in terms of both prediction and description for comparative purposes. This study illustrates that the variable selection process is critical in order to ensure optimal and stable results in the estimation process so that methods can be compared. This paper illustrates that past sample size prescriptions are insuf<sup>fi</sup>cient to ensure that the best variable subset is selected or that acceptable levels of accuracy are achieved. Our results show that for relatively small sample sizes, the bias in the hitrate estimate due to model bias is quanti<sup>fi</sup>able and contributes a signi<sup>fi</sup>cant amount of variation to estimates. As a result, comparisons are not appropriate. While validity seems to generalize for the two populations, further research is needed for investigating trends, especially using smaller populations and for explaining the behavior of subset replication and standard errors as well. Finally, using different selection criteria (hitrate and F-measures), the subsets selected as best matched 61% of the time, with most agreement occuring at the smaller sample sizes, and to a lesser extent for NNA. Further research is necessary for populations that have a greater degree of imbalance.

Kiang [29] argued that no single method provides the best approach for the various data characteristics arising in the area of business, and suggested that, if a single set of guidelines were established, then the literature may provide a means of reporting and building a body of evidence in terms of discovering trends relative to particular data characteristics. Our paper illustrates that this design, including the variable selection process, provides an accurate picture of the population and should be used for future comparative studies. Additional studies should be carried in order to investigate the sample size requirements for predictor set sizes other than p=11. Related to the replicability in the variable selection process is the degree to which multicollinearity exists. While multicollinearity is not a problem when analyses are used strictly for prediction, the volume and extensive nature of this study prohibited investigating the effects of multicollinearity on variable selection and replicability and, thus, further research is needed. This study utilized M nearest-neighbor rule for M=5 and a radius of one for the estimated kernel density functions

[4] S. Bhattacharyya, J. Sanjeev, K. Tharakunnel, J.C. Westland, Data mining for credit card fraud: A comparative study, Decision Support Systems 50 (2011) 602–613.

![](/api/attachments/TY7PDCE3/fulltext/images/02e4f1bcc806fd9aae6035d8a3a4527ef766753f0070f30a0ce8e11edba0ae04.jpg)  
LINEAR QUAD LOGISTIC NNA KDF TREE  
Fig. 5. Standard errors of average apparent hitrates and F-measures.

around the observation of interest; further studies should take into account various neighborhood sizes and radii in order to assess the effects of those parameters. Finally, with this research design, other issues that ordinarily exist when conducting classi<sup>fi</sup>cation analysis can be addressed as well.

This study addressed topics pertinent to the use of classi<sup>fi</sup>cation analyses and can be used for providing guidelines for future analyses. When conducting comparisons, we suggest selecting samples of various sizes from either real or simulated populations and assessing performance in terms of predictive accuracy and replication; the variable selection process must be used to ensure optimal results. For each classi<sup>fi</sup>cation analysis, we suggest the following DSS based upon guidelines set by Huberty [26]:

## 1. De<sup>fi</sup>ne groups of interest

2. Select the initial set of predictors based upon theory, past research, availability, cost, etc.

3. Ensure samples of suf<sup>fi</sup>cient sizes are included, say 1000 or greater, to ensure stability and validity. Give consideration when using equal or proportional sampling.

4. De<sup>fi</sup>ne prior probabilities and/or costs of misclassi<sup>fi</sup>cation where necessary.

5. Provide descriptive statistics and check for normality, equality of group covariance matrices, and Outliers.

6. Select the criterion for subset selection, hitrate or F-meaure, for example.

7. Conduct the analysis, including all-subset variable selection, using training data, then validate on test data (preferably population data)

8. Make comparisons across the methods and assess performance as it relates to the distributions characteristics of the population

9. Report results so as to build a body of evidence for arriving at general comparative conclusions

## References

[1] O.K. Asparoukhov, W.J. Krzanowski, A comparison of discriminant procedures for binary variables, Computational Statistics & Data Analysis 38 (2001) 139–160.

[2] A. Baron, Misclassi<sup>fi</sup>cation among methods used for multiple group discrimination – the effects of distributional properties Statistics in Medicine 10 (1991) 757–766.

[3] V.L. Berardi, B.E. Patuwo, M.Y. Hu, A principled approach for building and evaluating neural network classification models. Decision Support Systems 38 (2004) 233–246.

[5] L.J. Blincoe, A. Seay, E. Zaloshnja, T. Miller, E. Romano, S. Lutcher, R. Spicer, The economic impact of motor vehicle crashes 2000, Washington, DC, National Highway Safety Administration, DOTHS 809 (May 2002) 446.

[6] R. Bolton, D.J. Hand, Statistical fraud detection: A review (with discussion), Statistical Science 17 (3) (2002) 235–255.

[7] L. Breiman, J.H. Friedman, R.A. Olshen, C.J. Stone, Classi<sup>fi</sup>cation and regression trees, Belmont, CA, Wadsworth, 1984.

[8] W.K. Chiang, D. Zhang, L. Zhou, Predicting and explaining patronage behavior toward web and traditional stores using neural networks: a comparative analysis with logistic regression, Decision Support Systems 41 (2006) 514–531.

[9] M. Dash, H. Liu, Feature selection for classi<sup>fi</sup>cation, Intelligent Data Analysis 1 (1–4) (1997)131-156

[10] T.H. Davenport, J.G. Harris, Competing on Analytics: The New Science of Winning, Harvard Business School Press, Boston, MA, 2006.

[11] E.L. Dey, A.W. Astin, Statistical alternatives for studying college student retention: A comparative analysis of logit, probit, and linear regression, Research in Higher Education 34 (1993) 569–581.

[12] D. Durand, Risk elements in consumer installment lending, Studies in consumer installment <sup>fi</sup>nancing, vol. 8, National Bureau of Economic Research, New York, 1941.

[13] G.G. Enas, S.C. Choi, Choice of the smoothing parameter and ef<sup>fi</sup>ciency of k-nearest neighbor classi<sup>fi</sup>cation, Computers and Mathematics with Applications 12A (2) (1986) 235–244.

[14] W.H. Finch, M.K. Schneider, Missclassi<sup>fi</sup>cation rates for four methods of group classi<sup>fi</sup>cation, Educational ad Psychological Measurement 66 (2) (2006) 240–257.

[15] R.A. Fisher, The use of multiple measures in taxonomic problems, Annals of Eugenics 7 (1936) 179–188.

[16] D.H. Foley, Consideration of sample and feature size, IEEE Transactions on Information Theory 18 (1972) 618–626.

[17] J.D.F. Habbema, J. Hermans, Selection of variable in discriminant analysis by F-statistic and error rate, Technometrics 19 (4) (1977) 487–493.

[18] M. Halperin, W.C. Blackwelder, J.I. Verter, Estimation of the multivariate logistic risk function: A comparison of the discriminant function and maximum likelihood approaches, Journal of Chronic Diseases 24 (1971) 125–158.

[19] D.J. Hand, Common errors in data analysis: the apparent error rate of classi<sup>fi</sup>cation rules, Psychological Medicine 13 (1983) 201–203.

[20] D.J. Hand, Construction and Assessment of Classi<sup>fi</sup>cation Rules, Wiley, Chicester, UK, 1997.

[21] F.E. Harrell, K.L. Lee, A comparison of the discrimination of discriminant analysis and logistic regression under multivariate normality, in: P.K. Sen (Ed.), Biostatistics Statistics in Biomedical, Public Health, and Environmental Sciences, The Bernard G. Greenberg Volume, , 1985, pp. 333–343, North Holland, Amsterdam.

[22] H. He, E.A. Garcia, Learning from imbalanced data, IEEE Transactions on Knowledge and Data Engineering 21 (9) (2009) 1263–1284.

[23] J. Hermans, J.D.F. Habbema, Manual for the LLOC discrim and analysis programs, University of Leiden, Department of Medical Statistics 1976

[24] D. Hosmer, S. Lemeshow, Applied Logistic Regression, Wiley, New York, 1989.

[25] T. Hosmer, D.W. Hosmer, L.L. Fisher, A comparison of the maximum likelihood and discriminant function estimators of the coef<sup>fi</sup>cients of the logistic regression model for mixed continuous and discrete variables. Communications in Statistics B12 (1983) 577-593.

[26] C.J. Huberty, Applied discriminant analysis, Wiley, New York, 1994.

[27] A.K. Jain, B. Chandrasekaran, Dimensionality and sample size consideration in pattern recognition practice, Handbook of Statistics 2 (1982) 835–855.

[28] D. Jensen, J. Neville, Linkage and autocorrelation cause feature selection bias in relational learning, Proceedings of the Nineteenth International Conference on Machine Learning (ICML2002), Morgan Kaufmann (2002) 259–266.

[29] M. Kiang, A comparative assessment of classification methods. Decision Support Systems 35 (2003) 441–454.

[30] Y. Kim, Toward a successful CRM: variable selection, sampling, and ensemble, Decision Support Systems 41 (2006) 542–553.

[31] Y. Kim, W.N. Street, An intelligent system for customer targeting: a data mining approach, Decision Support Systems 37 (2004) 215–228.

[32] P.A. Lachenbruch, On expected probabilities of misclassi<sup>fi</sup>cation in discriminant analysis, necessary sample size, and a relation with multiple correlation coef<sup>fi</sup>cient, Biometrics 24 (1968) 823–834.

[33] N. Levin, J. Zahavi, M. Olitsky, AMOS – A probability-driven, customer-oriented decisions support system for target marketing of solo mailings, European Journal of Operational Research 87 (1995) 708–721.

[34] W.Z. Liu, A.P. White, A comparison of nearest neighbor and tree-based methods of non-parametric discriminant analysis, Journal of Statistical Computation and Simulation 53 (1995) 41–50.

[35] H. Liu, L. Yu, Toward integrating feature selection algorithms for classi<sup>fi</sup>cation and clustering, IEEE Transactions on Knowledge and Data Engineering 17 (4) (2006) 491–502.

[36] R.J. McKay, N.A. Campbell, Variable selection techniques in discriminant analysis: I. Description, and II. Allocation, British Journal of Mathematical and Statistical Psychology 35 (1982) 1–41.

[37] G.J. McLachlan, The bias of sample-based posterior probabilities, Biomedical Journal 19 (1977) 421–426.

[38] G.J. McLachlan, Discriminant Analysis and Statistical Pattern Recognition, Wiley, New York, 1992.

[39] G.J. McLachlan, K. Byth, Expected error rates for logistic regression versus normal discriminant analysis, Biometrical Journal 21 (1979) 47–56.

[40] A. Meshbane, J.D. Morris, Predictive discriminant analysis versus logistic regression in two-group classi<sup>fi</sup>cation problems, paper presented at the annual meeting of the American Educational Research Association, New York, , 1996.

[41] A. Meshbane, J.D. Morris, A method for selecting between linear and quadratic classi<sup>fi</sup>cation models in discriminant analysis, The Journal of Experimental Education 63 (3) (1996) 263–273.

[42] B.J. Nelson, G.C. Runger, J. Si, An error rate comparison of classi<sup>fi</sup>cation methods with continuous explanatory variables, IIE Transactions 35 (2003) 557–566.

[43] P. Resnik, H. Varian, Recommender Systems, Communications of the ACM 40 (3) (1997) 56–58.

[44] P.M. Rudolph, M. Karson, The effects of unequal priors and unequal misclassi<sup>fi</sup>cation costs on MDA, Journal of Applied Statistics 15 (1988) 69–83.

[45] S.K. Singhi, H. Liu, Feature subset selection bias for classi<sup>fi</sup>cation learning, Proceedings of the 23rd international conference on machine learning, Pittsburg, PA, ACM International Conference Proceeding Series, vol. 148, 2006, pp. 849–856.

[46] S.J. Steel, N. Louw, N.J. LeRoux, A comparison of the post selection error rate behavior of the normal and quadratic linear discriminant rules, Journal of Statistical Computation and Simulation 65 (2000) 157–172.

[47] B. Thompson, Stepwise regression and stepwise discriminant analysis need not apply here: A guideline editorial, Educational and Psychological Measurement 55(1995).525-534

[48] C. van Rijsbergen, Information retrieval, Butterworths, London, 1979.

[49] R. Wilson, R. Sharda, Bankruptcy prediction using neural networks, Decision Support Systems 11 (1994) 545–557.

![](/api/attachments/TY7PDCE3/fulltext/images/a4481c7b2403e99843e4f000284b4fb6907727ef4ccab33b91e9d1bac8633384.jpg)

Joni N. Shreve is an Instructor of Information Systems and Decision Sciences at Louisiana State University and A&M College, Baton Rouge. She received her MS in Statistics and PhD in Educational Psychology with an emphasis in Statistical Methodology, both from the University of Georgia, Athens. Prior to joining LSU, she was a senior staff consultant for the National Center for Infectious Diseases at the Centers for Disease Control, Atlanta, GA. Her research interests include Classi<sup>fi</sup>cation Analysis, Data Mining, and Business Intelligence.

![](/api/attachments/TY7PDCE3/fulltext/images/2810f07e91b29372167f3eb53e2f769a77d36bc10079eeef509d7d89f892220a.jpg)

Helmut Schneider is Associate Dean of Research Helmut Schneider in the E. I. Ourso College of Business at Louisiana State University. He received his Ph.D. in Operations Management and Statistics from the Free University of Berlin. Prior to joining LSU he taught statistics at the Free University in Berlin, was a visiting scholar from the University of North Carolina at Chapel Hill and the University of Arkansas in Fayetteville. He has published two books and over 50 articles in refereed journals in the areas of OM and statistics. His research has appeared in Management Science, Operations Research, European Journal of Operational Research, Production and Operations Management, Naval Research Logistics, Technometrics, Biometrika. He is on the editorial board of the Quality Management Journal.

![](/api/attachments/TY7PDCE3/fulltext/images/b73b0bc1d0e22db5dd902a00d374410419a30918d3f68111ba09194d81e96757.jpg)

Omer M. Soysal is an Assistant Professor of Information Systems and Decision Sciences at Louisiana State University and A&M College. Baton Rouge. He received his MS in Computer Science from the Southern University and A&M College and in Electronics Engineering from the Inonu University. He earned his PhD in Computer Science from the Louisiana State University and A&M College. His research interests include Computer Vision, Machine Learning, Data Mining, Medical Informatics, Geographic Information Systems, Traf<sup>fi</sup>c Accident Analysis, and Image Database Systems.
