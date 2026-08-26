---
otero_id: 19972
otero_key: "MCEVNFWJ"
title: "Data misrepresentation detection for insurance underwriting fraud prevention"
authors: "Félix Vandervorst; Wouter Verbeke; Tim Verdonck"
year: "2022"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2022.113798"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Data misrepresentation detection for insurance underwriting fraud prevention

![](/api/attachments/MCEVNFWJ/fulltext/images/974946439cd55a2497993ca923bf16e774585cfa950720cdb71a14d7320ad101.jpg)

F´elix Vandervorst <sup>a,b,c,\*</sup>, Wouter Verbeke <sup>b</sup>, Tim Verdonck <sup>c,d</sup>

<sup>a</sup> Allianz Benelux, Data Office, Koning Albert II Laan 32, Brussels 1000, Belgium

<sup>b</sup> KU Leuven, Faculty of Economics and Business, Naamsestraat 69, Leuven 3000, Belgium

<sup>c</sup> University of Antwerp, Department of Mathematics, Middelheimlaan 1, Antwerp 2020, Belgium

<sup>d</sup> KU Leuven, Department of Mathematics, Celestijnenlaan 200B, Leuven 3001, Belgium

## A R T I C L E I N F O

Keywords: Insurance underwriting fraud Premium fraud Data misrepresentation Machine learning Nonlife insurance

## A B S T R A C T

Premium fraud concerns data misrepresentation committed by an insurance customer with the intent to benefit from an unduly low premium at the underwriting of a policy. In this paper, we propose a novel approach for evaluating the risk of underwriting premium fraud at the time of application in the presence of potentially misrepresented self-reported information. The aim of the approach is to support insurance companies in iden tifving fraudulent applications and their decisions to underwrite insurance contract propositions. Likewise, it can be use to make straight-through processing (i.e. automated) underwriting systems more fraudproof, by e.g., triggering a validation on applications prone to misrepresentations. Our approach is based on conditional density estimates for a set of validated contracts. The proposed approach does not require historical fraud labels and can adapt to changes in pricing policy. Moreover, the approach can be used to detect outliers in addition to predicting underwriting fraud and is extended to multivariate self-reported data. We further demonstrate a link between Shapley values in common conditional expectation problems and conditional density estimations to make our approach explainable. We report a case study involving motor insurance underwriting, in which a driver’s identity and driving record can be misrepresented to benefit from an unduly low premium; the results indicate the effectiveness of the proposed approach for detecting and preventing underwriting fraud

## 1. Introduction

Premium fraud concerns the intentional misrepresentation of infor mation that is provided at the time of underwriting of an insurance contract in order to benefit from an unduly low premium. Premium fraud encompasses a variety of patterns and scenarios. In life insurance, for example, self-reported smoking status often has a material impact on expected mortality and, thus, on the premium price [1]. In the absence of an effective and credible strategy for confirming the true smoking status of the policyholder, the latter has a peculiar incentive to conceal this information. In motor insurance contracts, premium prices are often prohibitive for young and inexperienced drivers. Those drivers have a material incentive to overstate their driving experience, for instance, by having an older relative listed on the contract as the main driver on their behalf. [2] estimates that global motor insurance premium fraud amounts to 29 billion dollars annually. In workers’ compensation, the company seeking insurance may misrepresent its payroll information to benefit from insurance coverage at a lower premium price [3]. The Economic Policy Institute reports that 10 to 20% of workers are mis reported in the U.S.A., resulting in lower premiums paid by employers [4].

Premium fraud causes a loss of premiums, which will ultimately result in an increase in insurance premiums for all policyholders, including those who have not committed premium fraud. Another impact of premium fraud lies in the untruthful data collected by the insurance company and the knock-on impact on all decisions or actu arial models that are built on those data. Therefore, the ability to detect such fraud is essential.

Since the nineteen-nineties, researchers and practitioners have been investigating data-driven approaches for improving the power of fraud detection systems [5–7]. However, unlike many other types of fraud, insurance fraud is not self-revealing [8], i.e., the company will not gain knowledge on the fraudulent status of a claim or contract after an event without proactive and costly investigations. The non-self-revealing nature of insurance fraud (including premium fraud) poses a serious challenge for both its identification (the company cannot label past frauds or estimate the extent of the problem) and prediction (without labels, supervised learning is not possible, and unsupervised learning is difficult to validate). The literature on underwriting fraud is focused on the restricted setting in which one binary self-reported variable is potentially misrepresented and does not consider adaptation to changes in pricing policy.

In this paper, we contribute to the literature by presenting a nove approach for detecting premium fraud by evaluating data misrepre sentation risk. The proposed approach is based on conditional density estimation (CDE) of a set of self-reported variables and is adaptive to exogenous changes in pricing policy. Moreover, we present a case study based on real motor insurance data.

The remainder of this paper is structured as follows. In Section $^ { 2 , }$ we present a brief literature review on data misrepresentation and its ap plications in the insurance underwriting literature. Section 3 describes the methodology, in which we detail how premium fraud detection can be approached as a conditional density estimation problem with mixed data types, using the orthogonal basis projection trick of [9] and an adaptation of the random forest algorithm [10]. We also present how the pricing policy can be used in combination with CDE to represent financial motivation. In Section 4, we present an application of the presented methodology to real motor insurance data. Finally, Section 5 presents conclusions and directions for further research.

## 2. Literature review

In [8], underwriting fraud is defined as covering, for example, “the dissimulation of information during application (application fraud) to obtain coverage or a lower premium (premium fraud), the deliberate concealment of existing insurance contracts covering the same property and casualty (P&C) risk, and underwriting coverage for fictitious risks” [8, p. 3]. The motivation behind premium fraud is the financial gain resulting from a misstatement in the underwriting information, such that the premium according to the misrepresented information is lower than the true premium.

The problem of data misrepresentation has a long history in the economic literature, in which researchers aim at estimating statistical models based on contaminated data [11]. The data misrepresentation problem is often formulated in terms of conditional densities [11]. For instance, in [12] the conditional density of the dependent variable $\boldsymbol { Y } ,$ knowing the observed variable $Z ^ { * }$ of its unobserved variable Z is formulated as

$$
f (y | z ^ {*}) = \int f (y | z) g (z | z ^ {*}) d z
$$

where $g ( z | z ^ { * } )$ is the conditional distribution of the true value of $Z = z ,$ knowing the observed value $Z ^ { * } = z ^ { * } , f ( y | z )$ the error-free conditional distribution and $f ( y | z ^ { * } )$ the error-contaminated conditional distribution. The literature on measurement error is focused on contaminated sam ples of $( Y , Z ^ { * } )$ , while making distributional assumptions on the form of the misrepresentation [11]. To the best of our knowledge, [13,14] are the first studies to take this type of statistical approach to data misrep resentation in the context of insurance underwriting. They study the quantification of the misrepresentation of a true value $Z \left( \mathrm { e . g . } \right.$ , smoking status in a health insurance contract) by one corresponding binary selfreported random variable $Z ^ { * } \in \{ 0 , 1 \}$ , compared to a parametric distri bution of the loss $f ( y | z ) \ ( \mathrm { e } . g .$ , gamma or Poisson) assumed in the insurance contract.

$$
\begin{array}{l} f (y | z ^ {*} = 1) = f (y | z = 1), \\ f (y | z ^ {*} = 0) = (1 - P (z = 1 | z ^ {*} = 0)) f (y | z = 0) + P (z = 1 | z ^ {*} = 0) f (y | z = 1), \end{array}
$$

where $P ( z = 1 | z ^ { * } = 0 )$ is the misrepresentation probability parameter.

This equation is identifiable in the case of unidirectional misclassifica tion, i.e., where $f ( y | z ^ { * } = 1 ) = f ( y | z = 1 )$ . Whereas this approach is informative on the prevalence of the problem in a population through the estimation of $P ( z = 1 | z ^ { * } = 0 )$ , it is of little use in improving the underwriting decision process because it is not a contract-dependent representation. To address this shortcoming, [15] proposes an exten sion of the framework established in [13,14] that includes other correctly reported variables, thereby providing a misrepresentation probability that is dependent on the contract details in the context of generalized linear models. However, the proposed models consider only discrete binary factors with unidirectional misclassification. The as sumptions made in the above literature can be unrealistic and limiting in practical applications. Indeed, in many insurance applications, multiple variables may be self-reported, continuous or discrete. Moreover, in surance fraud is dynamic. Fraudsters swiftly capitalize on opportunities [8], such as changes of the pricing policy. The misclassification direction is not necessarily constant in this context. Also, the loss information is available only after a certain observation period.

An alternative approach to the data misrepresentation problem uses validation data (containing at least values of $z ) ,$ although often not available [11]. When a validated dataset for (sets of) two paired vari ables (Z.X) is available, the problem of estimating the data misrepre sentation of variable Z can be formulated as a CDE problem in which Z is the target variable and $f ( z | x )$ is the conditional density one wishes to estimate. The data used for scoring insurance contracts are of mixed data types, including continuous variables $( \mathrm { e } . g . , \mathrm { a g e } )$ and discrete factors (e. g., car model, zip code). In the case that the target variable is binary, the posterior probability $P ( Z = 1 | X )$ coincides with the conditional mean E[Z|X] [16]. In that case, many well-documented methods are available that can handle a large number of covariates, in particular, Lasso re gressions for mixed data types [17] or decision tree ensembles such as random forests or boosted trees, which are well suited for high dimensional problems involving mixed data types. However, how to obtain an estimate ${ \widehat { f } } ( z | x )$ for a continuous, potentially multivariate variable Z is a less studied statistical problem. One class of approaches in the CDE literature relies on the use of orthogonal transformations of f(z x). The recent work [9] proposes a flexible conditional density estimator (FlexCode) that projects the target variable Z onto an orthogonal basis [18]. Each projection onto the basis is estimated via a well-known conditional mean regression algorithm (e.g. linear models, decision trees) and the goodness-of-fit is evaluated with a variation of the inte grated squared error (CDE loss). Another recent approach to conditiona density estimation is to take the CDE loss of [9] as a variable splitting function in the random forest algorithm of [19], using a variant of a tree structure to estimate $f ( z | x )$ . The most important departure from the original algorithm is the use of the CDE loss of Eq. (5), which is used as a splitting criterion in the construction of each tree t. Random forest CDE (RFCDE) can be interpreted as a weighted kernel density method in which the weights are obtained from a random forest. In this paper, we will focus on those two techniques, FlexCode and RFCDE. Alternative approaches exist for conditional density estimation, albeit sub-optimal in this context. The estimation of ${ \widehat { f } } ( z | x )$ can be approached directly via its conditional distribution ${ \widehat { F } } ( z | x )$ , or via its conditional quantile function $\widehat { Q } _ { z | x } ( \alpha )$ . For instance, quantile regression forests [20] estimate $\widehat { Q } _ { z | x } ( \alpha )$ and ${ \widehat { F } } ( z | x ) ;$ however, the estimated distribution ${ \widehat { F } } ( z | x )$ is non differentiable, and this method is not suited for multivariate responses In this paper, we focus on methods in which the conditional density function ${ \widehat { f } } ( z | x )$ is directly evaluated to avoid differentiability and invertibility conditions on $\widehat F$ and $\widehat { Q } _ { z | x } ( \alpha )$ . Moreover, we have no prior information on the underlying distribution $f ( z | x )$ , which can potentially exhibit multimodality; therefore, we consider only nonparametric methods to avoid having to make assumptions on the shape of the dis tribution $f ( z | x )$ . In the nonparametric literature, a common approach for estimating the conditional density is to combine the estimation of the joint density ${ \widehat { f } } ( z , x )$ with the estimation of the marginal density ${ \widehat { f } } ( x )$ according to ${ \widehat { f } } ( z | x ) = { \frac { { \widehat { f } } ( z , x ) } { { \widehat { f } } ( x ) } }$ . In one class of nonparametric methods, this estimation problem is addressed by means of kernel functions. Reference [21] proposes a kernel density estimator whose bandwidth is estimated via cross-validation and that handles irrelevant covariates. However, this method does not scale well with the dimensionality and size of the dataset, making it impractical for larger datasets.

## 3. Methodology

## 3.1. Problem formulation

Let us define $\mathcal { U }$ as the true set of underwriting information and $\mathcal { U } ^ { \ast }$ as the reported set of underwriting information. An insurance premium $\mu ( \mathcal { U } ^ { * } )$ is the coverage price offered by the insurance company based on the reported information. The job of an insurance underwriter is to assess whether an application with information $\mathcal { U } ^ { * }$ is truthful, that is, whether the reported information is equal to its true value U . In particular, the underwriter must ensure that no misrepresentation has been committed in order to benefit from an unduly low premium, i.e., $\mu ( \mathcal { U } ^ { \ast } ) \langle \mu ( \mathcal { U } )$

Furthermore, we define two subsets of underwriting information, namely, the self-reported information Z and the correctly measured in formation $X ,$ such that $\mathcal { U } = Z \cup X .$ . By construction, only the self reported information is subject to misrepresentation; accordingly, $\boldsymbol { \mathcal { U } } ^ { * } =$ $Z ^ { * } \cup X .$

In Table 1, we present a sketch of a set of insurance contract appli cations where dim $\begin{array} { r } { \mathcal { U } ^ { \ast } ) = p + q , } \end{array}$ dim $( Z ^ { * } ) = q ,$ and $d i m ( X ) = p .$

The premium price $\mu ( Z ^ { * } , X )$ is the price that is offered to the customer given the underwriting information, which characterizes the risk profile of the customer. This is the price that provides the customer with an incentive to misrepresent information in order to benefit from a lower premium $\mu ( Z ^ { * } , X )$ .

The distinction between self-reported and other information enables us to formulate the definition of premium fraud risk as follows:

Premium Fraud Risk $: = P ( \mu ( Z ^ { \ast } , X ) < \mu ( Z , X ) )$

(1)

## 3.2. Self-reported and correctly measured sets of underwriting information

Naturally, an insurance company would prefer that all required un derwriting information include only non-self-reported data. In this case, dim(X) = dim (U), all information is correctly measured, and the pre mium fraud risk in $\operatorname { E q } .$ . (1) is nonexistent. However, the inclusion of selfreported data may add discriminative power and improve the pricing accuracy compared to the use of correctly measured data alone. Insurers need to find the right balance between exposure to data misrepresen tation and pricing accuracy.

As explained earlier, data deemed to belong to the correctly measured set X are data for which the policyholder does not have the

## Table 1

Underwriting problem: Applications submitted to underwriting agents sequen tially at times $t _ { 1 } < t _ { 2 } < \ldots < t _ { m } .$ If an application is validated by an agent, it becomes a contract.

<table><tr><td rowspan="2"></td><td>Premium</td><td colspan="3">Self-Reported</td><td>...</td><td colspan="3">Correctly Measured</td></tr><tr><td> $\mu (Z^{*},X)$ </td><td> $Z_{1}^{*}$ </td><td>...</td><td> $Z_{q}^{*}$ </td><td>...</td><td> $X_{1}$ </td><td>...</td><td> $X_{p}$ </td></tr><tr><td>Application 1,  $t_{1}$ :</td><td>1200</td><td>23</td><td>...</td><td>A</td><td>...</td><td>1100</td><td>...</td><td>18</td></tr><tr><td>Application 2,  $t_{2}$ :</td><td>800</td><td>20</td><td>...</td><td>B</td><td>...</td><td>1200</td><td>...</td><td>21</td></tr><tr><td>Application 3,  $t_{3}$ :</td><td>700</td><td>53</td><td>...</td><td>A</td><td>...</td><td>450</td><td>...</td><td>19</td></tr><tr><td>...</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Application m,  $t_{m}$ :</td><td>980</td><td>28</td><td>...</td><td>A</td><td>...</td><td>3400</td><td>...</td><td>32</td></tr></table>

opportunity to misrepresent their values. The definition and scope of the correctly measured variables are specific to the context of each under writing system. In motor insurance, the detailed characteristics of ve hicles may be sourced from third-party data or national registers. The details on the drivers, however, may be entirely self-reported. In prop erty insurance, geographic and demographic variables can be sourced from external data, whereas data on the risk behaviors of the tenants of buildings are likely to be entirely self-reported. In health insurance, smoking status may be self-reported, whereas the age of an insured person could be verified against a national registry.

Depending on the problem at hand, some data that are technically reported by the policyholder could still be considered correctly measured. For instance, data that would certainly result in denial of insurance coverage at the occurrence of a claim are most unlikely to be misrepresented [22] since there is no financial incentive and, hence, no motivation.

The definitions of sets X and Z may vary over time, depending on the controls, opportunities and pricing policies. The relevant processes and data are also different from one insurance company to another.

For instance, the development of national registers of nonsensitive individual demographic data that are accessible to insurance companies may expand their sets of correctly measured data. On the other hand, data privacy regulations may require insurance companies to exclude some external data and thereby increase their reliance on self-reported data.

## 3.3. Conditional premium fraud risk

The primary objective of our premium fraud model is to provide a risk score based on self-reported information for a given application. Let us expand the previous definitions:

$$
\begin{array}{l} \text { Conditional   Premium   Fraud   Risk: } = P (\mu (Z ^ {*}, X) <   \mu (Z, X) | X = x, Z ^ {*} = z ^ {*}) \\ \qquad = \int_ {\mathcal {Z}} 1 _ {\mu (z ^ {*}, x) <   \mu (z, x)} f (z | x) d ^ {q} z \end{array}\tag{2}
$$

The above equation can be interpreted as the risk that the self reported variables are misstated with respect to a certain pricing pol icy $\mu ,$ given knowledge of the correctly measured information.

The indicator function $1 _ { \mu ( z ^ { \ast } , x ) < \mu ( z , x ) }$ is straightforward to calculate given a commercial pricing policy μ. Note that a broader function $f ( \mu ( z ^ { * }$ $x ) , \mu ( z , x ) )$ can also be considered, for instance, to give more weight to higher differences in premium. The conditional density function $f ( z | x )$ is unknown and needs to be estimated.

## 3.4. Conditional density estimation

Reference [9] proposes a flexible conditional density estimator (FlexCode) based on an orthogonal projection of Z such that the CDE problem is transformed into a series of I conditional expectation esti mation problems. The estimator is written as follows:

$$
\widehat {f} (z | x) = \sum_ {i} ^ {I} \widehat {\mathbb {E}} [ \phi_ {i} (z) | X ] \phi_ {i} (z),\tag{3}
$$

where $\phi _ { i } ( z )$ is the projection of variable z onto the ith dimension of an orthogonal basis $\{ \phi _ { i } \} _ { I }$ of size I. The conditional expectation ${ \widehat { \mathbb { E } } } [ \phi _ { i } ( z ) | X ]$ can be estimated using any type of regression algorithm (e.g., a decision tree, linear model, or neural network). The choice of the optimal basis is evaluated based on the CDE loss.

The CDE loss [9] is the integrated square error between the true distribution $f ( z | x )$ and the approximated distribution ${ \widehat { f } } ( z | x )$ , weighted by the marginal density of x.

$$
\begin{array}{l} L ^ {C D E} (f (z | x), \widehat {f} (z | x)) = \iint (f (z | x) - \widehat {f} (z | x)) ^ {2} d z d P (x) \\ \qquad = C _ {f} + \iint \widehat {f} (z | x) ^ {2} d z d P (x) - 2 \iint \widehat {f} (z | x) f (z | x) d z d P (x) \\ \qquad = C _ {f} + \iint \widehat {f} (z | x) ^ {2} d z d P (x) - 2 \iint \widehat {f} (z | x) f (z, x) d z d x \\ \qquad = C _ {f} + E _ {X} \bigg [ \int \widehat {f} (z | x) ^ {2} d z \bigg ] - 2 E _ {X, Y} [ \widehat {f} (z | x) ]. \end{array}\tag{4}
$$

In practical real-world applications, unlike in simulation studies, the distribution $f ( z | x )$ is unknown, which makes the estimation of the conditional density difficult to validate. The above formulation of the CDE loss is convenient because it isolates the $f ( z | x )$ term in a constant that does not depend on the estimator $\cdot { \widehat { f } } ( z | x )$ . The estimator of the above CDE loss in [9] is:

$$
\widehat {L} ^ {C D E} (f (z | x), \widehat {f} (z | x)) = \frac {1}{m} \sum_ {i = 1} ^ {m} \int \widehat {f} (z | x _ {i}) ^ {2} d z - \frac {2}{m} \sum_ {i = 1} ^ {m} \widehat {f} (z _ {i} | x _ {i}),\tag{5}
$$

which is evaluated on m observations held out for the purpose of esti mating ${ \widehat { f } } ( z | x ) , { \mathrm { i . e . } }$ ., the validation set.

This approach conveniently relies on regression models, which are well known by practitioners and are suited for massive parallelization (each of the I regression models can be calculated independently). However, the basis size is assumed to be unique for all $X = x ,$ and using the CDE loss alone as the criterion for selecting the optimal basis size can be misleading for some problems [18]. Note also that the approach can generate spurious bumps or negative values that require postprocessing, as explained in [9].

One popular type of regression model that is suitable for high dimensional sparse datasets of mixed data types (continuous and discrete variables) is a random forest estimator. A random forest esti mator [19] of a conditional mean can be expressed as follows:

$$
\widehat {\mathbb {E}} [ Z | X ] = T ^ {- 1} \sum_ {t = 1} ^ {T} \frac {\sum_ {i = 1} ^ {n} Z _ {i} 1 _ {X _ {i} \in R (x , \theta_ {t})}}{\sum_ {i = 1} ^ {n} 1 _ {X _ {i} \in R (x , \theta_ {t})}},
$$

where T is the number of decision trees, $\theta _ { t }$ denotes the structure of tree t, and $R ( x , \theta _ { t } )$ is the region (leaf) delimited by tree t for observation x. This estimator can be used in $\mathtt { E q . } ( 3 )$ to estimate each of the I projections of z.

Although the orthogonal projection framework proposed in [9] is designed to study univariate responses z, extensions to multivariate re sponses are theoretically possible, as pointed out in the paper, via tensor products. In the bivariate case, where $z = \{ z _ { 1 } , z _ { 2 } \}$ and for two bases {ϕ } and $\{ \phi _ { j } \} \{$

$$
\widehat {f} (z | x) = \sum_ {i, j} \widehat {\mathbb {E}} \left[ \phi_ {i} \left(z _ {1}\right) \phi_ {j} \left(z _ {2}\right) | X \right] \phi_ {i} \left(z _ {1}\right) \phi_ {j} \left(z _ {2}\right).
$$

However, neither the paper nor the related code details a cross validation strategy for finding multiple basis sizes in the case of multi ple variables. The number of models to evaluate is large, becoming $I ^ { * } J$ with only two variables, and the numerical estimation of the CDE los becomes a challenge in itself as the number of dimensions increases, necessitating the computation of a multivariate integral.

The random forest for conditional density estimation in the RFCDE method [10] is defined as follows:

$$
\widehat {f} (z | x) = \left(\sum_ {t = 1} ^ {T} \sum_ {i = 1} ^ {n} \frac {1 _ {X _ {i} \in R (x , \theta_ {t})}}{\sum_ {i = 1} ^ {n} 1 _ {X _ {i} \in R (x , \theta_ {t})}}\right) ^ {- 1} \sum_ {t = 1} ^ {T} \sum_ {i = 1} ^ {n} K _ {H} (Z _ {i} - z) \frac {1 _ {X _ {i} \in R (x , \theta_ {t})}}{\sum_ {i = 1} ^ {n} 1 _ {X _ {i} \in R (x , \theta_ {t})}},\tag{6}
$$

where $K _ { H }$ is a kernel function with bandwidth matrix H.

An approximation is also adopted in [10] to enable the use orthog onal series in order to avoid the calculation of kernel densities at each split, as in [9], the size and type of the basis are parameters to be defined.

However, the CDE loss used in [9,10] has no meaningful interpretation. It alone is not sufficient to evaluate the estimation of $\dot { f } ( \boldsymbol z )$ $x ) .$ We therefore introduce a complimentary evaluation metric in the next section to provide further confidence in and insight into the esti mation o ${ \dot { \left| f ( z | x ) \right. } }$

## 3.5. High-density region for conditional density diagnosis and outlier detection

High-density regions (HDR) are sometimes used in the conditional density estimation literature to diagnose the calibration o ${ \cdot } \widehat { f } ( z | x ) , \mathbf { e } .  g . ,$ , in [9].

The high-density region [23] of a conditional distribution for a given confidence level α is $R ( f _ { \alpha } ) = \{ z : { \widehat { f } } ( z | x ) > f _ { \alpha } \}$ , where $f _ { \alpha }$ is the largest constant such that $P ( Z \in R ( f _ { \alpha } ) | X = x ) = 1 - \alpha .$

The empirical coverage $\widehat { \alpha } ( \alpha )$ is the average proportion of samples of Z that belong to the high-density region for their respective ${ \widehat { f } } ( z | x )$ and a theoretical coverage level $\begin{array} { r } { \alpha , \widehat { \alpha } ( \alpha ) = \frac { 1 } { n } \sum _ { i } ^ { n } 1 _ { z _ { i } \in R _ { i } ( f _ { \alpha } ) } . } \end{array}$ . If ${ \widehat { f } } ( z | x )$ is a good estimator of $f ( z | x )$ , then the empirical coverage should converge to the theoretical coverage for all α levels.

Based on the above definitions, we can define the HDR coverage loss as follows:

$$
L ^ {H D R} (f (z | x), \widehat {f} (z | x)) = \int (\alpha - \widehat {\alpha} (\alpha)) ^ {2} d \alpha ,
$$

which is ≈0 if ${ \widehat { f } } ( z | x ) \approx f ( z | x )$ . Note that the relation between the empirical and theoretical coverages is a necessary but insufficient con dition to determine the calibration of ${ \widehat { f } } ( z | x )$ . For instance, when used as an estimate of ${ \widehat { f } } ( z | x ) .$ , the prior distribution $\widehat { f } ( z )$ can satisfy this coverage test and yet be a poor and uninformative estimator of the posterior distribution. It is, however, an informative loss that can be used in combination with the CDE loss during the training phase of the algo rithm or as a criterion for selecting an optimal basis size in Eq. (3). It is also suited to the case of multivariate variables $z ,$ similar to the CDE loss.

One peculiar byproduct of the use of conditional density estimation in Eq. (2) and high-density regions is the ability to identify outliers in the self-reported values of $z ,$ conditional on $X .$ Using the same calibrated conditional density estimator ${ \widehat { f } } ( z | x )$ , an outlier is defined as $Z ^ { \operatorname { \biggr } } \in R ( f _ { \alpha } )$ for a given α level. Moreover, high-density regions can be mapped to a “traffic light” approach to facilitate communication with non statisticians by means of intuitive code values $[ 7 , { \mathfrak { p } } .$ 282]. A traffic light approach can also be related to a governance policy; for instance, all data points in the red area, $\mathrm { i . e . , }$ points that do not belong to the 99% high-density region, may require a second level of validation.

## 3.6. Pricing policy form μ and stagewise validation of information

The use of generalized linear models (GLMs) is a common standard in the insurance industry for calculating a pricing policy μ. We refer to [24] for a comprehensive overview. In this case, the pricing model can be expressed in a multiplicative form as $\mu ( z , x ) = \mu _ { 0 } \mu _ { z } ( z ) \mu _ { x } ( x )$ , where $\mu _ { 0 }$ is a “baseline premium” and $\mu _ { z } ( z )$ and $\mu _ { x } ( x )$ are relative price increases/ decreases in the values of the variables Z and $X .$

In this case, the premium fraud risk simplifies to

$$
\int_ {\mathcal {Z}} 1 _ {\mu_ {z} (z ^ {*}) \langle \mu_ {z} (z) f (z | x) d ^ {q} z.}\tag{7}
$$

This is convenient for the evaluation of the premium fraud risk in practice, as one requires only the multiplicative factor $\mu _ { z }$ instead of the complete pricing mode $\mu$ to evaluate the fraud risk.

In practice, we do not have a priori validated values for the selfreported values on an incoming contract. Instead, we estimate the likelihood $f ( z | x )$ of each possible true value of the self-reported infor mation in the region $\{ z : \mu ( z ) > \mu ( z ^ { * } ) \}$ . This region represents all values of z for which the premium price is greater than the price $\mu ( z ^ { * } )$ and, therefore, the values for which there is a motivation to commit data misrepresentation.

The validation problem may be approached in a stagewise manner such that the premium fraud risk can be refined as the self-reported variables are validated. A conditional density model can provide guid ance to an underwriter as he/she iteratively validates the self-reported values $Z _ { 1 } { ^ * } , Z _ { 2 } { ^ * } , . . . , Z _ { q } { ^ * }$

For instance, in the case of motor insurance, one could first investi gate the validity of a driver’s identity as variable $Z _ { 1 }$ and, as a second step, validate the claims history relating to that driver as a separate variable $Z _ { 2 } .$

One advantage of this approach is that one can use the already validated self-reported values to refine the subsequent prediction and analysis of other self-reported values, $\widehat { f } ( z _ { 2 } | z _ { 1 } , x )$

$$
P \left(\mu \left(Z _ {1} ^ {*}, Z _ {2} ^ {*}, X\right) <   \mu \left(Z _ {1}, Z _ {2}, X\right) \mid X = x, Z _ {1} ^ {*} = z _ {1} ^ {*}, Z _ {2} ^ {*} = z _ {2} ^ {*}\right).
$$

If the pricing policy is multiplicative, i.e., $\begin{array} { r l } { \mu ( Z _ { 1 } , Z _ { 2 } , X ) } & { { } = } \end{array}$ $\mu _ { 0 } \mu _ { z _ { 1 } } ( Z _ { 1 } ) \mu _ { z _ { 2 } } ( Z _ { 2 } ) \mu _ { x } ( X )$ , then the conditional premium fraud risk is:

$$
P \left(\mu_ {z _ {1}} \left(Z _ {1} ^ {*}\right) \mu_ {z _ {2}} \left(Z _ {2} ^ {*}\right) \left\langle \mu_ {z _ {1}} \left(Z _ {1}\right) \mu_ {z _ {2}} \left(Z _ {2}\right) \mid X = x, Z _ {1} ^ {*} = z _ {1} ^ {*}, Z _ {2} ^ {*} = z _ {2} ^ {*}\right). \right.
$$

Once the value of $Z _ { 1 } { ^ * }$ has been validated, the premium fraud risk is updated to:

$$
P \left(\mu_ {z _ {2}} \left(Z _ {2} ^ {*}\right) \left\langle \mu_ {z _ {2}} \left(Z _ {2}\right) \mid X = x, Z _ {1} = z _ {1}, Z _ {2} ^ {*} = z _ {2} ^ {*}\right). \right.
$$

Note that this stagewise approach provides insight into the vulner abilities of an underwriting system and, therefore, its exposure to pre mium fraud at different stages in the validation process. For instance, the variable $Z _ { 1 }$ may be “more difficult” to predict (and $Z _ { 1 } { ^ { * } }$ may be more difficult to validate) than $Z _ { 2 } ~ ( Z _ { 2 } ^ { * } )$ , and thus, the company may exert additional effort in the assessment of $Z _ { 1 }$ .

## 4. Empirical results

## 4.1. Data

Although there can be. in practice, a handful of self-reported vari. ables in motor insurance contracts, two self-reported dimensions in particular are critically important in the determination of the insurance price: the identity of the driver (particularly his/her driving experience and age) and the driving record (represented on an ordinal scale in a bonus-malus insurance system). A bonus-malus insurance system is a merit-based system that reflects the past driving history on a single ordinal scale; for more details, we refer to [25].

The dataset that is used to evaluate the proposed approach contains a sample of 57,000 validated contract quotes $( X _ { i } , Z _ { i } )$ spanning 4 years of history, where $X _ { i }$ represents the detailed information on the vehicle as certified by a third party and $Z _ { i }$ contains the self-reported information. As is usually assumed, the i pairs $( X _ { i } , Z _ { i } )$ are assumed to be i.i.d. in nature. Note that validated contract quotes relate here only to new customers, contract renewals are therefore not included in the dataset.

A history of 4 years is selected here, as this corresponds to one generation of vehicles in Belgium. The correctly measured data X are composed of 38 variables describing vehicles’ features $( \boldsymbol { \mathrm { e . } } \boldsymbol { \mathrm { g . } } ,$ power, age of the car, height, brand, model, segment of car, number of doors, cat alog value).

In the following, we present an application of the proposed meth odology to motor insurance contracts where the self-reported variable Z is:

1. univariate and continuous: the driver’s license age;

2. bivariate and continuous: the driver’s license age and the driver age;

3. multivariate of mixed type: the driving record score and the driver’s license age; and

4. univariate and ordinal: the driving record score.

The vehicle information is provided by a third party and deemed correctly measured.

## 4.2. Application

4.2.1. Univariate and continuous self-reported data: the driver’s license age The marginal distribution f(z) of driver’s license age provides base line information on the expected driver’s license age distribution. The estimator ${ \widehat { f } } ( z )$ is depicted in Fig. 1, where a traffic light approach is used to color four different high-density regions [23] according to three arbitrary levels α.

However, the marginal distribution f(z) is not particularly helpful in validating incoming contracts because the estimated high-density re gions are relatively spread out. One way of narrowing the high-density regions is to add the vehicle information X to estimate the conditional density $f ( z | x )$ for a specific vehicle. If the vehicle is a “good predictor” of the driver’s identity (here, the driver’s license age), we expect $f ( z | x )$ to define narrower high-density regions. The insight gained in this way is measured by the difference between the posterior distribution and the prior distribution. A common measure for comparing two distributions is the Kullback-Leibler divergence measure:

$$
K L (\widehat {f} (z | x), \widehat {f} (z)) = \int \widehat {f} (z | x) l o g \left(\frac {\widehat {f} (z | x)}{\widehat {f} (z)}\right) d z.\tag{8}
$$

Measuring the added value obtained by adding the information X for predicting $z$ is strategically important for considering the acquisition of new correctly measured data to add to the system.

The orthogonal-based estimator of Eq. (3) requires three main types of parameters to be set: the basis type $\phi ,$ the basis size I and the pa rameters of the underlying I regression estimators.

Basis type: We consider the Fourier basis as used in [9], as we expect a relatively smooth function ${ \widehat { f } } ( z | x )$ . The Haar wavelet basis is a suitable candidate for discrete responses. For an overview of alternative suitable basis type choices, we refer to [26].

Basis size: The size of the basis is subject to a typical bias-variance trade-off, with a smaller basis size resulting in a smoother $f ( z | x ) ,$ while higher basis values produce less smooth functions. The size of the basis is evaluated via cross-validation on the basis of the CDE loss as described in [9]. Note that a large basis size is undesirable because as many regression models must be trained as the basis size is large, leading to prohibitive computational costs if no parallelization is implemented. Moreover, we use the HDR coverage loss as a complementary loss, next to the CDE loss to determine the basis size $I ,$ as presented in the meth odology section.

![](/api/attachments/MCEVNFWJ/fulltext/images/b43e11cfcd82787cd864ddcda8f200a0f85cb76843e68a55d79aef698d766833.jpg)  
Fig. 1. Estimator $\hat { \ b { f } } ( \pmb { z } )$ of the marginal distribution of driver’s license age, estimated with a Gaussian kernel of bandwidth 1.3. The colored areas represent the high-density regions at levels of 90, 95 and 99%.

Regression model: Any common regression model for estimating a conditional mean can be considered. Decision tree-based methods are known to have high off-the-shelf performance with mixed data types of high dimensionality with a large number of observations and also are suited to parallelization in most cases. The authors of [9] have proposed FlexCode Random Forest (FlexCode-RF) for mixed data types, which implements Breiman’s random forest algorithm as a regression function [19]. In practice, it is preferable to opt for an off-the-shelf algorithm with good expected performance with minimal tuning, since as many models must be trained as the basis size. We use the fast random forest implementation in [27].

A 5-fold cross-validation strategy is used here to validate the pa rameters used in the base random forest estimator. We refer to [28,29] for an overview of parameter choice, heuristics, and selection in random forests. Note that there is no theoretical guarantee that a set of param eters proven optimal for conditional mean estimation is also optimal for conditional density estimation. This step is taken as the starting point for further parameter optimization and is also useful for comparing the different methods.

In underwriting decision problems, a good understanding of the estimated conditional density function is critical to assess (i) the soundness of the estimators, (ii) the insight gain achieved by adding X when predicting $z ,$ and (iii) its explainability. Indeed, in this case, a single metric such as the CDE loss is insufficient to assess any of these criteria.

In Fig. 2, we present the results of three models trained on a test set of n/3, i.e., 19 k observations. We present the vanilla random forest algo rithm used as the basis for the parameter choice as a point of comparison for a density estimator centered on its conditional mean estimate, albeit not an estimator of ${ \widehat { f } } ( z | x )$ in itself. FlexCode-RF with a Fourier basis of size I = 5 (minimizing the CDE loss) is shown in the middle, and RFCDE is presented on the right.

In Fig. 2, one can observe that FlexCode and RFCDE are both close to the diagonal on the ̂α − α coverage plot. However, FlexCode tends to diverge more from the prior distribution than RFCDE, as measured by

the Kullback-Leibler divergence.

This can be explained by the use of basis transformation in FlexCode versus kernel density estimation in estimating the prior distribution. By contrast, in RFCDE, both the prior and posterior estimators use kernels.

Sample predictions from RFCDE compared to the prior distribution estimates for six contracts are presented in Fig. 3.

In Fig. 3, the top and bottom rows of plots represent lower and higher Kullback-Leibler divergence measures, respectively, compared to the prior distribution $\hat { \ b { f } } ( \ b { z } )$ . Lower values of the Kullback-Leibler divergence indicate that the information X does not add much evidence on the true value of the self-reported variable. The distributions presented in the bottom row, however, indicate that the driver of the car is likely less experienced.

4.2.2. Bivariate and continuous self-reported data: The driver’s license age and driver age

In the case that the self-reported variable Z is continuous and bivariate, the methods discussed above are extensible to multivariate prediction via the use of tensor products for orthogonal basis trans formation, similarly to FlexCode [9], and with multivariate kernels for RFCDE [10]

Here, we briefly present a simple example with RFCDE, estimated via a kernel density method.

The CDE loss formulations of Eq. (5) and Eq. (6) are both applicable in multivariate cases. However, the bandwidth H is a 2-by-2 matrix instead of a single scalar as in the univariate case. Duong [30] explains that the bandwidth matrix is usually parameterized as a diagonal matrix (constrained) or as a semi-positive definite and symmetric matrix (unconstrained).

For instance, the conditional distribution estimator of the prior dis tribution ${ \widehat { f } } ( z )$ (where z is bivariate) is $\left( \begin{array} { c c } { { 0 . 1 9 } } & { { 0 } } \\ { { 0 } } & { { 0 . 1 9 } } \end{array} \right)$ in the constrained case and $\left( \begin{array} { c c } { { 0 . 3 4 } } & { { 0 . 2 1 } } \\ { { 0 . 2 1 } } & { { 0 . 3 1 } } \end{array} \right)$ in the unconstrained case, and the resulting

densities ${ \widehat { f } } ( z )$ with a Gaussian kernel are displayed in Fig. 4 (with

![](/api/attachments/MCEVNFWJ/fulltext/images/00906c4624e8e56d3e8f6294e3340092cb7eb7d8204f3753ac61fa25116f4a0b.jpg)

![](/api/attachments/MCEVNFWJ/fulltext/images/f45b4d94e5732457e3c28b570053b78a99774029d2556c0637f3cd51c65fefd0.jpg)

![](/api/attachments/MCEVNFWJ/fulltext/images/cc1d50ae37f51d11d13b33ef55c9f4127d05471cd5aa876e7cdb3e359f1840fd.jpg)

![](/api/attachments/MCEVNFWJ/fulltext/images/77af336503070c6e8289d2b18822f604a8c83815a84b3a282d9d27a8566bbe7a.jpg)

![](/api/attachments/MCEVNFWJ/fulltext/images/5610945592b9a0e71600f0818b9376627de07618dbda9df30b0ba2db8be78a97.jpg)

![](/api/attachments/MCEVNFWJ/fulltext/images/b2ee7fc2b1a6617910722aa2778f5e155c653c7bbbe2382fc27fb4b90a93b70f.jpg)  
Fig. 2. Theoretical versus empirical coverage plots and Kullback-Leibler divergence measures for the vanilla random forest algorithm (left). FlexCode-RF (middle and RFCDE (right).

![](/api/attachments/MCEVNFWJ/fulltext/images/4c8814716140d90ad31b6bb09626afca71f15b112231060ef039d6c379af481b.jpg)

![](/api/attachments/MCEVNFWJ/fulltext/images/7e042f0f6bf4ffca86e5cce355316f83f210549f156845a416b9a3ef0e15c70a.jpg)

![](/api/attachments/MCEVNFWJ/fulltext/images/7b344ca5380a0b2828703b31f6f51a6c060a20ca1ec0a23e2e19d50db610745d.jpg)

![](/api/attachments/MCEVNFWJ/fulltext/images/f2d1142243efabfdfa70d2d5d4a3f1148244b3f14405b48790f25a0e792ba92a.jpg)

![](/api/attachments/MCEVNFWJ/fulltext/images/1558522981e3c16587f432ed7f4a2d399657318c70099316a94cbceb0e119359.jpg)

![](/api/attachments/MCEVNFWJ/fulltext/images/23705ca8fb1ea45891dd37ca3e48fab37996a53efbee752c7dd04ea9676a2d0b.jpg)  
Fig. 3. Sample predictions with the RFCDE estimate ${ \widehat { f } } ( z | x )$ and the prior density ${ \widehat { f } } ( z )$ in gray.

![](/api/attachments/MCEVNFWJ/fulltext/images/90328cbe73ad4067ea8ef9ab94a6c0bb6b508d777e544c5769bf86c6e11f3e12.jpg)

![](/api/attachments/MCEVNFWJ/fulltext/images/5383b23b40ee8ac68c32676f9d269fa185a1a9acc97d3ed74333f76edebb6ba2.jpg)  
Fig. 4. Kernel density estimation of the prior distribution $\hat { \ b { f } } ( \pmb { z } )$ with a constrained bandwidth matrix (left) and an unconstrained (right) density estimation of the prior.

prescaling of the data and the Sum of Asymptotic Mean Squared Error pilot bandwidth selector; see [30] for a detailed explanation).

There are many possible strategies for the parameterization of $H ,$ most of which are based on a numerical procedure (a “plug-in” esti mator) or a cross-validation methodology; we refer to [30] for an overview. However, those methods estimate the matrix H for each density function ${ \widehat { f } } ( z | x )$ and can exhibit numerical instabilities, which is undesirable, particularly when the model is intended to provide guid ance to nonstatisticians.

A simple approach to guarantee the stability of the bandwidth esti mation is to estimate the parameter of the prior density function ${ \widehat { f } } ( z )$ and fix it for any conditional density function in Eq. (6).

Fig. 5 presents one sample prediction.

4.2.3. Bivariate mixed self-reported data: driver’s license age and driving score

In the case that the self-reported variable Z is multivariate and of mixed type (discrete and continuous), computing the conditional pre mium fraud risk requires the evaluation of a joint conditional density ${ \widehat { f } } ( z _ { 1 } , z _ { 2 } | x )$

RFCDE is designed for one type of variable, and FlexCode is uni variate. Here, we adapt the method of FlexCode to mixed-type multi variate responses using heterogeneous basis types, similar to the vectorvalued extension sketched in [9], via tensor products. {ϕ } is a Fourier basis of size I, and $\{ \phi _ { j } \} _ { J }$ is a Haar basis of size J. In this case, we set the size of the basis $\{ \phi _ { j } \} _ { J }$ to the cardinality of the discrete variable. Figs. 6 and 7 present the CDE loss and HDR coverage loss for different values of the basis size I. In this case, we observe that both losses are minimized by a basis of size 3. Note that in this application, the postprocessing of the estimated densities is limited to removing negative values and uniform scaling of the density surface to ensure that it integrates to 1.

![](/api/attachments/MCEVNFWJ/fulltext/images/c1b10a4650d83e97b48c8f8fb437e6663de503751f5c9e0fb2abc11220b82f2b.jpg)

![](/api/attachments/MCEVNFWJ/fulltext/images/4d030fd6e3103dd803c08ce72d854ac32306ba8b3693acfb880fd9ba8ce4a1e5.jpg)

![](/api/attachments/MCEVNFWJ/fulltext/images/a34d0d3b0b0fda78031c2e928e6ff5506d4a81ca13675ee2f5ace957c70560c4.jpg)  
Fig. 5. Conditional density function ${ \widehat { f } } ( z | x )$ for a bivariate Z (driver age and license age). The bandwidth matrix H is the constrained diagonal matrix of Fig. 4.

One sample prediction is depicted in Fig. 8. We observe a high probability mass at a low driving score, which corresponds to drivers with a good driving score. A second high-probability region is observed at a mid-range driving score, corresponding to the driving score of a new driver.

## 4.3. Fraud score application

In this section, we briefly present an application of the fraud score in a simplified, univariate setting with the driver’s license age as the selfreported variable and a pricing function which is strictly decreasing with driver’s license age (see Fig. 13 in Appendix). We apply the pre mium fraud risk model to a sample of new contract propositions, with a threshold of 5% increase in premium price to exclude small premium price differences.

The dataset that is used to evaluate the proposed approach contains a sample of $^ { 7 3 , 0 0 0 }$ applications spanning 4 years of history. The appli cations contain data which resulted in a validation and were accepted by the insurance company, as well as applications which were rejected. Note that the sample used here contains applications which were vali dated and therefore used in the training of the conditional density estimation ${ \widehat { f } } ( z | x )$

![](/api/attachments/MCEVNFWJ/fulltext/images/a378e85fbccb32d11f04b4e960d5389e557b92bb11981cf7bda3b152c7bec586.jpg)  
Fig. 6. CDE loss on the test set.

![](/api/attachments/MCEVNFWJ/fulltext/images/90343614a3e24a9927ec390ce444ef99d63f2a8424520924e1deb7822b085a8d.jpg)  
Fig. 7. HDR coverage loss on the test set.

![](/api/attachments/MCEVNFWJ/fulltext/images/f2c2b6fe591c3f8686e8fc52a1c8b1567a86521a8955a59de112fd926ce1aa14.jpg)  
Fig. 8. Sample prediction for bivariate self-reported data of mixed type.

Fig. 9 presents the distribution of the fraud risk score on a sample of contracts to validate. A sub-segment of 2500 applications from this sample has been labeled by experts as presenting a larger premium fraud risk, although these applications have not confirmed to effectively involve fraud. This sub-segment contains old cars with a self-reported middle-aged main driver, who has already a contract for another vehicle. Therefore, the segment is classified as potentially containing hidden young main drivers. Fig. 10 presents the fraud risk scores for this sub-segment. The difference in distributions suggests that our model does well in classifying those suspicious applications.

![](/api/attachments/MCEVNFWJ/fulltext/images/832b2342c790886d20bbc63f5a3f2030659fbdf03bd182b4cb74844fc5341f12.jpg)  
Fig. 9. Histogram of premium fraud risk estimated on a sample new contract propositions.

![](/api/attachments/MCEVNFWJ/fulltext/images/f618f94d7d8df87dcad4beb0c07a08a85b328f20afdd48b30d7c37799a6abd36.jpg)  
Fig. 10. Histogram of premium fraud risk estimated on a “risky” sub-sample of new contract propositions.

Additionally, in Fig. 11, we present the CDEs of three randomly sampled applications from sub-segment of Fig. 10. The self-reported value $z ^ { * }$ for those applications is presented in red. The area filled cor responds to the region on the CDE where premium price would be 5% higher than with the self-reported value, and the surface represents the premium fraud risk. We provide in appendix an infographic summari zing the decision support systems’ steps and discuss computation aspects.

## 4.4. Note on the explainability of <sup>̂</sup>f (z|x)

The explainability of a model is of critical concern towards its adoption and is a challenging task, even for common regression models estimating the conditional mean E[Z|X].

![](/api/attachments/MCEVNFWJ/fulltext/images/4bdb04fc9992c5a10a505ab55c356621b800d823d49dc9f75017a7a2f6152e71.jpg)

In that regard, Shapley values from game theory is a popular approach for explaining black-box models [31]. Shapley values are attributed at the prediction level; typically, each feature in vector x is attributed a contribution Φ (a Shapley value) to the difference between $\widehat { \mathbb { E } } [ Z ]$ and ${ \widehat { \mathbb { E } } } [ Z | X ]$ for a specific prediction.

In this section, we investigate the explainability of FlexCode and its input feature X. In particular we present an additive explanation to a CDE model of the form: $\begin{array} { r } { f ( z \vert \boldsymbol { x } ) = \Phi _ { 0 } ^ { \bar { f } ( z \vert \boldsymbol { x } ) } ( z ) + \sum _ { j } \Phi _ { j } ^ { f ( z \vert \boldsymbol { x } ) } ( z , \boldsymbol { x } ) } \end{array}$ . We present in appendix the details and proofs on the methods to conveniently reuse the Shapley values from the regression models underlying FlexCode in the context of a CDE problem.

Fig. 12 presents a sample prediction of ${ \widehat { f } } ( z | x ) .$ , where we are inter ested in explaining the difference between the prior distribution $\Phi _ { 0 } ( z )$ and the posterior distribution ${ \widehat { f } } ( z | x )$ (CDE raw). This difference is explained by the contribution of each variable $j , \Phi _ { j } ^ { f ( z | x ) } ( x )$

![](/api/attachments/MCEVNFWJ/fulltext/images/8080236e4a4e33cf7955eb778b0caf7fe561b01437ef5a3e37e275b8306b0e38.jpg)  
Fig. 12. Variable contribution for a sample prediction, explaining the differ ence between the prior distribution Φ (z) and the estimator of a sample pos terior distribution ${ \widehat { f } } ( z | x )$ (CDE raw). Four sampled variables’ Shapley values Φ<sup>f</sup> ${ \bf \Psi } ^ { ( z | x ) } ( z , x )$ are presented.

![](/api/attachments/MCEVNFWJ/fulltext/images/0ce14f93f177b366b2b0574d257f99b3afed9d6ac10f11d54d50d4781425b11e.jpg)

![](/api/attachments/MCEVNFWJ/fulltext/images/ff3828a441194ea685818d5c87bcdc3d31bd0bf66f8974c2e37327a047ec04a4.jpg)  
Fig. 11. Sample premium fraud risk scores prediction and self-reported values of driver’s license age.

In this figure we observe the model predicts a higher density on less experienced driver compared to the prior distribution. One can learn for instance that for the lowest value of driver’s license age $( \mathbf { a t } \ z = 0 )$ , the power, height, length and car age have a positive contribution on the <sup>̂</sup>f (z|x) for observation x.

Likewise, the bump on the right side of Fig. 12 may appear curious, we observe that the age of the car feature explains in part this prediction for this observation.

The displayed sum of the values $\sum _ { j } \Phi _ { j } ^ { f ( z | x ) } ( z , x )$ with $j = 0 , . . . , p$ is equal to ${ \widehat { f } } ( z | x )$ for all values of ${ \mathit { z } } ,$ as expected by the additivity property of Shapley values.

The outcomes of model explanation also serves as justification for a model user to further investigate a given element of a contract or justify the refusal of a contract proposition.

Moreover, model explanation is helpful from a modeling perspective in applying the Occam’s razor principle to the input feature space X, for instance, to discard “dummy” variables that do not play any role in prediction. It can also be used in the assessment of adding new dimen sion(s) to the input variables $X , \mathrm { e . g . }$ , sourcing additional variables on the vehicle.

## 4.5. Discussion

We have seen that conditional density estimation can be used as a means to estimate the plausibility of self-reported information in mul tiple formats (multivariate, mixed data types). The validation of a CDE system is inherently difficult because we do not observe the true con ditional densities, only sample points. Criteria such as the CDE loss and high-density regions may be used to validate vastly different ap proaches, for instance, orthonormal projections (FlexCode) and weighted kernel density estimators (RFCDE), as two valid candidates, as we have seen in Fig. 2.

The choice of the CDE technique depends on the nature of the self reported data. In this paper, we apply the method to multivariate self reported data of mixed type (discrete and continuous). Other applica tions may benefit from simpler approaches to CDE when the selfreported data are univariate or of nonmixed type or if a parametric form (e.g., a Gaussian distribution) can be reasonably assumed. The efficiency of our method in fighting fraud depends on the predictability of the self-reported values based on the correctly measured values. In the application to motor insurance data presented here, the task can be summarized as guessing drivers’ characteristics based on their vehicles characteristics.

In this application, we have limited the correctly measured variables to vehicle information. Other correctly measured information could also be added to the system to enable better prediction of the self-reported values to further improve the effectiveness of the system.

## 5. Conclusions

In this paper, we have formulated premium fraud detection as a con ditional density estimation problem. The estimation of conditional functions relies on the availability of a dataset of true values $( X _ { i } , Z _ { i } )$ that has been previously validated by experts.

This formulation enables us to explicitly estimate the distribution of the self-reported variables and their relation to the pricing policy, thereby yielding a risk evaluation in the opportunity-motivation framework of [8] in the context of premium fraud.

Conditional density estimation can also be used for performing (conditional) anomaly detection to detect outliers across specific di mensions Z using high-density regions and a traffic light approach [7].

We have discussed state-of-the-art techniques for estimating the conditional densities of continuous variables in large datasets of mixed data types [9,10], which has remained a challenging statistical problem to date. Notably, the use of a single criterion such as the CDE loss [9] appears insufficient to evaluate the overall calibration of the conditional densities. We have proposed an alternative loss function based on the high-density regions of [23] as a complementary loss function in CDE problems. We have presented how Shapley additive explanation [31,32] can be adapted to CDE problems to make the estimated conditional densities explainable.

Moreover, we have discussed how the validation of a contract proposition can be approached in a stagewise manner. The under standing of the predictability of a given stage in the validation of a contract can provide insight into the weaknesses of the underwriting process and allow actions to be taken accordingly to improve the robustness of contract validation. For instance, a higher uncertainty around a driver’s identity based on the car compared to a lower un certainty around the prediction of a driving record based on the driver’s identity and the car can motivate the acquisition of additional data predictive of the driver’s identity or a change in the variable used for pricing.

Further developments in nonparametric conditional estimation methods could also be benchmarked against the techniques and evalu ation metrics used herein. Future research could investigate the use of the realized loss per contract as an additional source of information supplementary to our premium fraud risk score, thereby creating con nections between the approaches of [13,14] and our own.

Our approach can be used by insurance companies to improve their decision making process in the validation of insurance contracts with potentially misrepresented self-reported information. For instance, in automated insurance underwriting (“straight-through processing”), our premium fraud risk score could be used to trigger a validation of the selfreported variable.

Our approach can also be applied for fraud detection in other, noninsurance domains in the application stage (application fraud), such as overstated income on credit applications to benefit from unduly low rates [33–35] or accounting misconduct [36].

## CRediT authorship contribution statement

Felix ´ Vandervorst: Conceptualization, Data curation, Methodology, Software, Writing – original draft. Wouter Verbeke: Conceptualization, Supervision, Methodology, Writing – review & editing. Tim Verdonck: Conceptualization, Supervision, Methodology, Writing – review & editing.

## Acknowledgments

We are grateful for the contribution of the Allianz Chair on Pre scriptive Business Analytics in Insurance at KULeuven. Furthermore, we appreciate the opportunity that Allianz Benelux provides us to dedicate time to research activities.

## Appendix A

## A.1. Pricing calculation and premium fraud examples in multiplicative pricing models

We present here two examples based on dummy data to illustrate (a) a premium calculation and (b) premium fraud when the pricing model has a multiplicative form. The pricing policy has the form $\mu ( z , x ) = \mu _ { 0 } \mu _ { z } ( z ) \mu _ { x } ( x )$ , where ${ } ; \mu _ { 0 }$ is a “baseline premium” and $\mu _ { z } ( z )$ and $\mu _ { x } ( x )$ are relative increases/

decreases in the values of variables Z and X.

(a) Premium calculation example: Suppose that the baseline premium $\mu _ { 0 }$ is set to 100 monthly, a car considered safe translates into the pricing policy as $\mu _ { x } ( x ) = 0 . 9$ , and an inexperienced driver translates into the pricing policy as $\mu _ { z } ( z ) = 1 . 2$ . Then, the proposed price of the corresponding insurance policy is $1 0 0 ^ { \div } 0 . 9 ^ { \ast } 1 . 2 = 1 0 8$ monthly.

(b) Premium fraud example: In Figs. 13 and 14, one can read out, for instance, that the premium price $\mu ( z ^ { * } , x )$ for a driver reported as having $z _ { 1 } { } ^ { * } { = } 2 0$ years of driving experience and being $z _ { 2 } { ^ { \ast } } { = } 4 5$ years old pays a premium of $\mu = \mu _ { 0 } \mu _ { z 1 } ( z _ { 1 } { ^ * } ) \mu _ { z 2 } ( z _ { 2 } { ^ * } ) \mu _ { x } ( x )$ , where $\mu _ { z 1 } ( 2 0 ) = 1 . 0 5$ and $\mu _ { z 2 } ( 4 5 ) =$ 0.99. Then, if the “true” driver, who is the child of the reported driver and in fact has 1 year of driving experience $( \mu _ { z 1 } ( 1 ) = 1 . 3 0 )$ and is 25 years old $( \mu _ { z 2 } ( 2 5 ) = 0 . 9 5 )$ , the premium that the true driver should pay would increase by $\frac { \mu _ { z _ { 1 } } ( z _ { 1 } ) \mu _ { z _ { 2 } } ( z _ { 2 } ) } { \mu _ { z _ { 1 } } \left( z _ { 1 } ^ { * } \right) \mu _ { z _ { 2 } } \left( z _ { 2 } ^ { * } \right) } { = }$ 18.8% over the premium currently being paid.

![](/api/attachments/MCEVNFWJ/fulltext/images/5abc6dc844103077bcd85b3aa1d69b63427ecaa72e9f7783d8dfc8e4f32cbbec.jpg)  
Fig. 13. $\mu _ { z 1 } { : }$ Relative increase in premium price according to the driver’s license age variable.

![](/api/attachments/MCEVNFWJ/fulltext/images/9ea451d0b3ded8974e1ec4edf7ca37683f9176c93c12a5d711d43d58c4a8f725.jpg)  
Fig. 14. $\mu _ { z _ { 2 } } \mathrm { : }$ Relative increase in premium price according to the driver age variable.

## A.2. Detailed note on the explainability $o f { \widehat { f } } ( z | x )$

Borrowing the notation from [32], the Shapley $\Phi _ { j } ^ { \delta } ( x )$ of a model δ for feature j and observation x equals:

$$
\Phi_ {j} ^ {\delta} (x) = \sum_ {Q \subseteq S \backslash \{j \}} \mathscr {C} \left(\delta_ {Q \cup \{j \}} (x) - \delta_ {Q} (x)\right),
$$

where Q is a subset (coalition) feature of $S = \{ 1 , . . . , p \} , p$ is the dimension of the input feature $X , j$ is the jth feature of X, $\begin{array} { r } { \mathcal { C } : = \frac { | Q | ! ( | S | - | Q | - 1 ) ! } { | S | ! } , ( \delta _ { Q \cup \{ j \} } ( x ) - } \end{array}$ $\delta _ { Q } ( x ) )$ ) measures the contribution of adding variable j to the coalition Q for a model δ and $\Phi _ { 0 } ^ { \delta } = \delta _ { \delta } ( \omega )$ ). The model δ can be expressed as the sum of it Shapley values, $\begin{array} { r } { \delta ( { \boldsymbol x } ) = \Phi _ { 0 } ^ { \delta } + \sum _ { j } \Phi _ { j } ^ { \delta } ( { \boldsymbol x } ) } \end{array}$ as per the additivity property of Shapley values.

Proposition 1. If f(z| x) admits an orthonormal decomposition of the form $\begin{array} { r } { f (  { \boldsymbol { z } } |  { \boldsymbol { x } } ) = \sum _ { i } \phi _ { i } (  { \boldsymbol { z } } ) \mathbb { E } [ \phi _ { i } (  { \boldsymbol { Z } } ) |  { \boldsymbol { X } } ] , \Phi _ { i } ^ { \mathbb { E } [ \phi _ { i } (  { \boldsymbol { Z } } ) |  { \boldsymbol { X } } ] } } \end{array}$ (x)is the Shapley value of the jth feature of the modelE $\cdot [ \phi _ { i } ( Z ) \left| X \right]$ , and $\Phi _ { j } ^ { f ( z | x ) } ( x )$ the Shapley value of the jth feature of model $f ( z | x ) f o r$ a value of z, then $\begin{array} { r } { \Phi _ { j } ^ { f ( z | x ) } ( z , x ) = \sum _ { i } ^ { { \bar { \prime } } } \phi _ { i } ( z ) \Phi _ { j } ^ { \phi _ { i } ( Z ) } ( x ) } \end{array}$ proof:

$$
\begin{array}{c} \Phi_ {j} ^ {f (z | x)} (z, x) = \sum_ {Q \subseteq S \setminus \{j \}} \mathcal {C} \big (f \big (z | x _ {Q \cup \{j \}} \big) - f (z | x _ {Q}) \big) \\ = \sum_ {Q \subseteq S \setminus \{j \}} \mathcal {C} \bigg (\sum_ {i} \phi_ {i} (z) \mathbb {E} \big [ \phi_ {i} (Z)   | X _ {Q \cup \{j \}} \big ] - \sum_ {i} \phi_ {i} (z) \mathbb {E} [ \phi_ {i} (Z)   | X _ {Q} ] \bigg) \\ = \sum_ {i} \phi_ {i} (z) \sum_ {Q \subseteq S \setminus \{j \}} \mathcal {C} \big (\mathbb {E} \big [ \phi_ {i} (Z)   | X _ {Q \cup \{j \}} \big ] - \mathbb {E} [ \phi_ {i} (Z)   | X _ {Q} ] \big) \\ = \sum_ {i} \phi_ {i} (z) \Phi_ {j} ^ {\mathbb {E} [ \phi_ {i} (Z)   | X ]} (x). \end{array}
$$

This result is convenient as it enables to use the explanations of the underlying regression coefficients of models $\mathbb { E } [ \phi _ { i } ( Z ) \left| X \right]$

Similarly to the above proposition, we can also relate the Shapley values $\Phi _ { j } ^ { \mathbb { E } [ Z | X ] } ( x )$ of the conditional expectation E[Z|X] to the Shapley values of the regression coefficients $\Phi _ { j } ^ { \mathbb { E } [ \phi _ { i } ( Z ) \vert X ] } ( x ) ,$ thanks to the relation $\begin{array} { r } { \mathbb { E } [ Z | X ] = \int z f ( z | x ) d z . } \end{array}$ . The result and proof are provided in Appendix.

The conditional expectation E[Z|X] is related to the conditional density by $\begin{array} { r } { \mathbb { E } [ Z | X ] = \int z f ( z | x ) d z . } \end{array}$

Proposition 2. $H f ( z | x )$ admits an orthonormal decomposition of the form $\begin{array} { r } { \dot { \mathbf { \sigma } } ( { \boldsymbol z } | { \boldsymbol x } ) = \sum _ { i } \phi _ { i } ( { \boldsymbol z } ) \mathbb { E } [ \phi _ { i } ( { \boldsymbol Z } ) | { \boldsymbol X } ] , \Phi _ { j } ^ { \mathbb { E } [ { \boldsymbol Z } | { \boldsymbol X } ] } } \end{array}$ (x)is the Shapley value of the jth feature of the modelE[Z|X], andΦ<sup>E[ϕi(Z) |X]</sup>(x)is the Shapley value of the jth feature of the modelE $[ \phi _ { i } ( Z ) \mid X ] ,$ , then $\begin{array} { r } { \mathfrak { p } _ { j } ^ { \mathbb { E } [ Z | X ] } ( { \pmb x } ) \overset { ^ { \prime } } { = } \int \ d { z } \sum _ { i } \phi _ { i } ( { \pmb z } ) \Phi _ { j } ^ { \mathbb { E } [ \phi _ { i } ( Z ) | X ] } } \end{array}$ <sup>]</sup>(x)dz

proof:

$$
\begin{array}{c} \Phi_ {j} ^ {\mathbb {E} [ Z | X ]} (x) = \sum_ {Q \subseteq S \setminus \{j \}} \mathcal {C} \big (\mathbb {E} \big [ Z | X _ {Q \cup \{j \}} \big ] - \mathbb {E} [ Z | X _ {Q} ] \big) \\ = \sum_ {Q \subseteq S \setminus \{j \}} \mathcal {C} \bigg (\int z f \big (z | x _ {Q \cup \{j \}} \big) d z - \int z f (z | x _ {Q}) d z \bigg) \\ = \sum_ {Q \subseteq S \setminus \{j \}} \mathcal {C} \bigg (\int z \sum_ {i} \phi_ {i} (z) \mathbb {E} \big [ \phi_ {i} (Z)   | X _ {Q \cup \{j \}}   \big ] d z - \int z \sum_ {i} \phi_ {i} (z) \mathbb {E} [ \phi_ {i} (Z)   | X _ {Q} ] d z \bigg) \\ = \int z \sum_ {i} \phi_ {i} (z) \sum_ {Q \subseteq S \setminus \{j \}} \mathcal {C} \big (\mathbb {E} \big [ \phi_ {i} (Z)   | X _ {Q \cup \{j \}}   \big ] - \mathbb {E} [ \phi_ {i} (Z)   | X _ {Q} ] \big) d z \\ = \int z \sum_ {i} \phi_ {i} (z) \Phi_ {j} ^ {\mathbb {E} [ \phi_ {i} (Z)   | X ]} (x) d z. \end{array}
$$

![](/api/attachments/MCEVNFWJ/fulltext/images/bfde3cb4a861b3237f28be47d108aef40c328e083462cb78bd8e4e11abd6b78d.jpg)  
Fig. 15. Overview of the decision support system for an univariate self-reported variable Z.

## A.3. Note on the computational aspects of the decision support system

We add a few comments on the computational aspects of the decision support system using orthonormal bases with an infographic in the case of an univariate self-reported variable (illustrating Section 4.3).

We distinguish three phases of the decision support system: training, validation and prediction. We assume the decision support system is intended to score new incoming contract propositions, hence the computational aspects of the prediction phase is more important than those attached to the training and validation phases.

The training and validation phases are proportional to the underlying regression model training and prediction times. In the above graph, the training phase and validation are implemented sequentially and stopped at model I + 1 (where a decrease in the loss function is observed), hence the global computation time is roughly I + 1 times the underlying model’s training and prediction. This computation time can be reduced from I + 1 to 1 times the underlying model’s if the computational architecture allows to evaluate in parallel the different models. Similarly to the validation phase, the prediction phase requires a prediction of each underlying regression model, hence will be proportional to I times the prediction of the regression models (which can also be reduced with parallelization). The prediction step also requires the prediction from the pricing policy μ(x, z), for a grid of values of z. The pricing policy μ is typically a (generalized) linear model, whose prediction times are negligible.

In this application we used the fast implementation of random forest as underlying regression model. The algorithm is described in [27], where the performance are detailed and documented for different problems and dataset sizes.

Note that the choice of the basis type depends on the support and smoothness of variable Z, the self-reported of interest and can motivate variations around this theme.

## References

[1] G. Schuman, Misrepresentation of smoking history in life insurance applications, Tort & Ins. LJ 30 (1994) 103.

[2] I. S. Office, The Challenge of Auto Insurance Premium Leakage, Tech. rep., Inc. Verisk Analytics, 2017.

[3] R.A. Derrig, V. Zicko, Prosecuting insurance fraud—a case study of the Massachusetts experience in the 1990s, Risk Manag. Insur. Rev. 5 (2) (2002) 77-104.

[4] F. Carr´e, (in)dependent contractor misclassification, Econ. Policy Inst. Briefing Paper 403 (2015).

[5] E.W. Ngai, Y. Hu, Y.H. Wong, Y. Chen, X. Sun, The application of data mining techniques in financial fraud detection: a classification framework and an academic review of literature, Decis. Support. Syst. 50 (3) (2011) 559–569.

[6] V. Chandola, A. Banerjee, V. Kumar, Anomaly detection: a survey, ACM Computing Surveys (CSUR) 41 (3) (2009) 1–58

[7] B. Baesens, V. Van Vlasselaer, W. Verbeke, Fraud Analytics Using Descriptive, Predictive, and Social Network Techniques: A Guide to Data Science for Fraud Detection, John Wilev & Sons, 2015

[8] S. Viaene, G. Dedene, Insurance fraud: issues and challenges, Geneva Pap. Risk Insur,-Issues Pract, 29 (2) (2004) 313–333.

[9] R. Izbicki, A.B. Lee, et al., Converting high-dimensional regression to highdimensional conditional density estimation, Electron. J. Stat. 11 (2) (2017) 2800–2831.

[10] N. Dalmasso, T. Pospisil, A.B. Lee, R. Izbicki, P.E. Freeman, A.I. Malz, Conditional density estimation tools in python and r with applications to photometric redshifts and likelihood-free cosmological inference, Astron. Comput. 30 (2020), 100362.

[111 S.M. Schennach. Recent advances in the measurement error literature. Annu. Rey

[12] Y. Hu, G. Ridder, Estimation of nonlinear models with mismeasured regressors using marginal information, J. Appl, Econ. 27 (3) (2012) 347–385.

[13] M. Xia, P. Gustafson, Bayesian regression models adjusting for unidirectional covariate misclassification, Can. J. Stat, 44 (2) (2016) 198–218.

[14] R.M. Akakpo, M. Xia, A.M. Polansky, Frequentist inference in insurance ratemaking models adjusting for misrepresentation, ASTIN Bull. J. IAA 49 (1) (2019) 117–146.

[15] M. Xia, L. Hua, G. Vadnais, Embedded predictive analysis of misrepresentation risk in glm ratemaking models, Variance: Advancing Sci. Risk 12 (1) (2018) 39–58

[16] L. Devroye, L. Gyorfi, ¨ G. Lugosi, A Probabilistic Theory of Pattern Recognition Vol. 31. Springer Science & Business Media, 2013.

[17] S. Devriendt, K. Antonio, T. Reynkens, R. Verbelen, Sparse regression with multitype regularized feature modeling, Insur. Math. Econ. 96 (2020) 248–261.

[18] M. Rosenblatt, Curve estimates, Ann, Math. Stat. 42 (6) (1971) 1815–1842

[19] L. Breiman, Random forests, Mach. Learn. 45 (1) (2001) 5–32.

[20] N. Meinshausen, Quantile regression forests, J. Mach. Learn. Res. 7 (Jun) (2006) 983–999.

[21] P. Hall, J. Racine, Q. Li, Cross-validation and the estimation of conditional probability densities, J. Am. Stat. Assoc. 99 (468) (2004) 1015–1026.

[22] R.S. Winsor, Misrepresentation and Non Disclosure on Applications for Insurance, Blaney McMurtry LLP. 1995

[23] R.J. Hyndman, Computing and graphing highest density regions, Am. Stat. 50 (2) (1996) 120–126.

[24] P. De Jong, G.Z. Heller, et al., Generalized Linear Models for Insurance Data, Cambridge Books, 2008.

[25] J. Lemaire, Bonus-malus Systems in Automobile Insurance Vol. 19, Springer Science & Business Media. 2012

[26] S. Mallat, A Wavelet Tour of Signal Processing, Elsevier, 1999.

[27] M.N. Wright, A. Ziegler, Eanger: a fast implementation of random forests for high dimensional data in c++ and r, J. Stat. Softw. 77 (1) (2017).

[28] G. Biau, E. Scornet, A random forest guided tour, Test 25 (2) (2016) 197–227.

[29] P. Probst, M.N. Wright, A.-L. Boulesteix, Hyperparameters and tuning strategies for random forest, Wiley Interdiscip. Rev. Data Min. Knowl. Disc. 9 (3) (2019), e1301.

[30] T. Duong, et al., ks: Kernel density estimation and kernel discriminant analysis for multivariate data in r, J. Stat. Softw. 21 (7) (2007) 1–16.

[31] S.M. Lundberg, S.-I. Lee, A unified approach to interpreting model predictions, in: Advances in Neural Information Processing Systems. 2017. pp. 4765–4774.

[32] E. Strumbelj, <sup>ˇ</sup> I. Kononenko, Explaining prediction models and individual predictions with feature contributions. Knowl. Inf, Syst, 41 (3) (2014) 647–665

[33] M.D. Pendley, G. Costello, M. Kelsch, The impact of poor underwriting practices and fraud in subprime rmbs performance, Fitch Ratings US Resid. Mortg. Spec Rep. (2007).

[34] A. Mian, A. Sufi, Fraudulent income overstatement on mortgage applications during the credit expansion of 2002 to 2005, Rev, Financ, Stud. 30 (6) (2017) 1832–1864.

[35] B.W. Ambrose, J. Conklin, J. Yoshida, Credit rationing, income exaggeration, and adverse selection in the mortgage market, J. Financ. 71 (6) (2016) 2637–2686.

[36] P.R. Hahn, J.S. Murray, I. Manolopoulou, A bayesian partial identification approach to inferring the prevalence of accounting misconduct. J. Am. Stat. Assoc. 111 (513) (2016) 14–26

Felix ´ Vandervorst is a Senior Data Scientist at Allianz Benelux and Ph.D. student at the Katholieke Universiteit Leuven and University of Antwerp. He holds a Master in business engineering and in actuarial sciences. His research interest is on fraud detection for in surance using machine learning and the limitations of conventional statistical learning methods in real-life fraud prone systems.

Wouter Verbeke is associate professor of data analytics at the Katholieke Universiteit Leuven. He graduated in 2007 as a Civil Engineer and obtained a Ph.D. in applied eco nomics at the Katholieke Universiteit Leuven in 2012. His research is situated in the field of prescriptive and profit-driven analytics and is driven by real-life business applications in fraud, customer relationship, credit risk, supply chain, and human resources management.

Tim Verdonck is a professor at the University of Antwerp and at the Katholieke Universiteit Leuven. He has a degree in Mathematics and a PhD in Science: Mathematics obtained at the University of Antwerp. During his PhD he successfully took the Master in insurance and the Master in financial and actuarial engineering, both at KU Leuven. He belongs to ROBUSTLeuven, the research group on Robust Statistics and his research fo cuses on the adaptation and application of robust methods for financial, actuarial and economic data sets
