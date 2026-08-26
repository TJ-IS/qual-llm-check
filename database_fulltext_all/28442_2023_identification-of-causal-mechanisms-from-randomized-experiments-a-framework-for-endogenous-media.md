---
otero_id: 28442
otero_key: "8PSHZBD3"
title: "Identification of Causal Mechanisms from Randomized Experiments: A Framework for Endogenous Mediation Analysis"
authors: "Jing Peng"
year: "2023"
journal: "Information Systems Research"
doi: "10.1287/isre.2022.1113"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Identification of Causal Mechanisms from Randomized Experiments: A Framework for Endogenous Mediation Analysis

Jing Peng<sup>a</sup>

<sup>a</sup> School of Business, University of Connecticut, Storrs, Connecticut 06269 Contact: jing.peng@uconn.edu, https://orcid.org/0000-0001-5490-6228 (JP)

Received: February 2, 2020 Revised: January 4, 2021; November 15, 2021 Accepted: January 20, 2022 Published Online in Articles in Advance: March 4, 2022

https://doi.org/10.1287/isre.2022.1113

Copyright: © 2022 INFORMS

Abstract. Experimental research in the business disciplines often focuses on the overall treatment effect and the heterogeneity therein. Whereas this type of research allows us to understand the strength and direction of the treatment effect under different conditions, it does not directly speak to the generative mechanisms, namely, why and how the effect arises. A standard procedure to identify the mechanisms underlying a treatment effect is mediation analysis, but extant mediation analysis frameworks either have no causal inter pretation or require the mediators to be unconfounded. Because mediators are posttreatment variables that typically cannot be preassigned beforehand, the endogeneity of media tors remains a serious concern even in randomized experiments. In response to this issue, we present a <sup>fl</sup>exible endogenous mediation analysis framework that still has causal interpre tation when the mediator is endogenous. We then discuss the identi<sup>fi</sup>cation conditions for different types of endogenous mediators, including unobserved or partially observed ones, under this framework. We show that endogenous mediation models can be parametrically identi<sup>fi</sup>ed without an instrumental variable when the generating process of the mediator is nonlinear. We further examine how the identi<sup>fi</sup>cation strengths of these models vary with a series of factors, including the level of endogeneity, the goodness of <sup>fi</sup>t of the mediator model, the percentage of observed mediator values, and the misspeci<sup>fi</sup>cation of the error terms. Finally, we provide guidelines on when and how to use endogenous mediation analysis and discuss implications for experimental design and empirical research. We offer an R package that implements the proposed endogenous mediation models.

History: Ravi Bapna, Senior Editor; Anuj Kumar, Associate Editor. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2022.1113.

Keywords: experiment mechanism mediation endogeneity identi<sup>fi</sup>cation copula

“A common criticism of experiments is that they reveal but do not explain causal relationships” (Bul lock et al. 2010, p. 550).

## 1. Introduction

Randomized experimentation is an increasingly popular approach to estimating causal effects in business disciplines (Aral and Walker 2011, Bapna et al. 2016, Qiu and Kumar 2017, Kumar and Hosanagar 2019, Lu et al. 2019, Zhang et al. 2019, Jung et al. 2020, Sun et al. 2021). However, extant experimental research in this area often focuses on the overall treatment effect and the heterogeneity therein through moderation analyses (e.g., Anderson and Simester 2003, Bapna et al. 2017, Jung et al. 2020, Lee and Hosanagar 2021, Sun et al. 2021). Conceptually, whereas moderation analyses allow us to understand the strength and direction of the treatment effect under different conditions, they do not directly speak to the generative mechanisms, namely, why and how the effect arises (Baron and Kenny 1986).

A treatment could have both direct and indirect effects on the outcome; the indirect effect refers to the portion of effect transmitted through an intermediate variable (i.e., a mediator).<sup>1</sup> Focusing on the total treatment effect and the heterogeneity therein has two limitations. First, it does not allow us to separately test the causal mechanisms behind the direct and indirect effects, which could have different policy implications. Second, the indirect effect is often sensitive to contextual characteristics because it depends on the generating process of the mediator. Consequently, the total treatment effect might not be generalizable across contexts even though the underlying causal mechanisms remain unchanged.<sup>2</sup> Therefore, to identify the causal mechanisms and to provide more generalizable insights, it is important to separate the direct and indirect effects.

The estimation of direct and indirect effects requires a mediation analysis, a standard procedure to investi gate why and how the treatment effect arises (Baron and Kenny 1986, Hayes 2017). Although mediation

(b)

analysis has a long history, it does not have a causal interpretation until the establishment of the causal mediation (CM) analysis framework (Imai et al. 2010a, b; Pearl 2014), which formally de<sup>fi</sup>nes the direct and indirect effects under the potential outcome framework. The causal mediation analysis framework supports both parametric and nonparametric identi<sup>fi</sup>cation of direct and indirect effects under the sequential ignorability assumption (SIA), which implies that no unobserved confounder affects both the mediator and the outcome. The parametric identi<sup>fi</sup>cation of this framework assumes that the mediator and the outcome models follow certain functional forms and then estimate the two models separately. In comparison, the nonparametric identi<sup>fi</sup>cation estimates direct and indirect effects based on the empirical distribution of the treatment, mediator, outcome, and control variables (Imai et al. 2010b). Whereas the nonparametric identi<sup>fi</sup>cation approach sounds compelling, it is dif<sup>fi</sup>- cult to account for the impact of control variables.<sup>3</sup> Without an effective way to incorporate control variables, the SIA assumption is even harder to defend.

Causal mediation analysis is not particularly popular among empirical researchers who are meticulous about causality because the SIA assumption assumes away the endogeneity issue (of the mediator), which is often the primary concern of empirical research. When there are unobserved factors affecting both the outcome and the mediator, the mediator is endogenous. Take the impact of personalization on the usage of a mobile app as an example, in which a privacy concern is a plausible mediator because personalization can reduce app usage by increasing users’ privacy concerns (Awad and Krishnan 2006). A privacy concern is likely endogenous because it can be in<sup>fl</sup>uenced by unobserved factors that also in<sup>fl</sup>uence app usage, such as users’ age and gender (app developers often refrain from asking such information unless necessary). The endogeneity of a mediator may also arise from measurement error. When a mediator is measured through a posttreatment survey, as is often the case, measurement error is a legitimate concern as survey responses are not perfectly reliable (Bound et al. 2001). Whereas the endogeneity of a treatment can be addressed by randomization, it is dif<sup>fi</sup>cult to randomize a mediator because it is a posttreatment variable that typically cannot be preassigned beforehand. Therefore, the endogeneity of mediators remains a serious issue even in randomized experiments.

Another practical problem facing empirical researchers is that the mediator of interest is often not observed or only partially observed. For instance, app developers rarely measure users’ privacy concerns while experi menting with different personalization strategies. Even if they measure privacy concerns, it is unrealistic to do so for all users as the cost can be prohibitive. The cost could be the <sup>fi</sup>nancial compensation used to incentivize users or the user attrition resulting from the requests to report privacy concerns, which can be perceived as annoying and invasive. In light of this issue, recent research extends causal mediation analysis to accom modate unobserved mediators (Muthen and Asparou-´ hov 2015, Albert et al. 2016). However, this stream of research still relies on the SIA assumption and assumes that multiple proxies of the mediators are measured— neither of which is warranted in practice.

To conduct practically desirable mediation analysis that has a causal interpretation and yet does not hinge on the stringent SIA assumption, we present an endog enous mediation (EM) analysis framework that allows the mediator to be endogenous and even unobserved. We consider two common types of endogenous mediation processes in randomized experiments as shown in Figure 1 and study whether and when they can be identi<sup>fi</sup>ed. Speci<sup>fi</sup>cally, we address the following questions:

1. When the treatment effect is mediated by an observed endogenous variable, whether and when can the direct and indirect treatment effects be estimated consistently?

Figure 1. (Color online) Endogenous Mediation in Randomized Experiments  
![](/api/attachments/8PSHZBD3/fulltext/images/07681048fb006cacceee7e93a3b089e4a561f92a393cd77847408eabbf527655.jpg)  
Notes. (a) Endogenous mediation. (b) Latent endogenous mediation. X – randomized treatment, M – mediator, Y – outcome, and U – unobserved confounder. A dashed circle indicates that the variable is unobserved. These two mediation processes can be considered as extensions of model 4 in Hayes (2017) that allow the mediator to be endogenous (and unobserved)

2. When the treatment effect is mediated by an unobserved (latent) endogenous variable, whether and when can the direct and indirect treatment effects be estimated consistently?

The rest of the paper is organized as follows. In Section 2, we discuss the formulation, estimation, and identi<sup>fi</sup>cation conditions of endogenous mediation models for various types of mediators under the endogenous mediation analysis framework. In Section 3, we validate their identi<sup>fi</sup>cation conditions using simulations and systematically investigate the sensitivity of their identi<sup>fi</sup>cation to a series of factors. After that, we provide guidelines on when and how to use endogenous mediation analysis and discuss the practical implications of our <sup>fi</sup>ndings in Section 4. We conclude the paper in Section 5.

## 2. Endogenous Mediation Analysis

2.1. Recursive Two-Stage Modeling Framework To model the endogenous mediation processes depicted in Figure 1, we make the following assumptions regarding the data generating process (DGP).

Assumption 1. The treatment is exogenous.

Assumption 2. We assume a stable unit treatment value

Assumption 3 (Optional). The error terms for the mediator and outcome are bivariate normally distributed.

In randomized experiments, Assumption 1 holds provided that the randomization is implemented properly. Assumption 2 is a standard assumption that the treatment on one unit does not spill over to another unit. Assumption 3, a widely used assumption to model correlated errors in two-stage models (e.g., Heckman 1978, Carrasco 2001, Greene 2009), is imposed to facilitate the derivation of a tractable likelihood function and the discussion of identi<sup>fi</sup>cation conditions. Assumption 3 is not mandatory in our modeling framework. One can use the copula modeling approach to account for other types of joint error distributions (Nelsen 2007, Trivedi and Zimmer 2007, Klein et al. 2019, Li et al. 2019).

Let the random variables X, M, and Y represent the treatment, mediator, and outcome, respectively. Let Z be an exogenous control variable if any; Z becomes an instrumental variable if it exclusively affects the mediator. The observation for unit i can be denoted as $\{ x _ { i } , m _ { i } , z _ { i } , y _ { i } \}$ . With this notation, the basic modeling framework for endogenous mediation analysis can be written as follows:

Mediator equation:

$$
m _ {i} = f (\alpha_ {0} + \alpha_ {1} x _ {i} + \alpha_ {2} z _ {i} + \lambda u _ {i}).\tag{1a}
$$

Outcome equation:

$$
y _ {i} = g (\beta_ {0} + \beta_ {1} x _ {i} + \beta_ {2} z _ {i} + \gamma m _ {i} + \sigma v _ {i}),\tag{1b}
$$

$$
\binom{u _ {i}}{v _ {i}} \sim N \biggl (\binom{0}{0}, \left( \begin{array}{c c} 1 & \rho \\ \rho & 1 \end{array} \right) \biggr),\tag{1c}
$$

where $f ( \cdot )$ and $g ( \cdot )$ represent the functional forms for the mediator (<sup>fi</sup>rst stage) and the outcome (second stage), respectively, with λ and σ denoting the standard deviations of the respective error terms. The dependent variables in both stages can be replaced by their conditional expectations if needed. Transformation of the mediator (e.g., the natural logarithm) is also allowed in the second stage. When there are repeated observations for the same unit, we can use random or <sup>fi</sup>xed effects to capture individual effects.

The key advantage of this framework over the causal mediation analysis framework (Imai et al. 2010a, b; Pearl 2014) is that it allows the error terms in the two equations to be correlated. When the correlation is zero, the endogenous mediation analysis degenerates to parametric causal mediation analysis. Although causal mediation analysis allows researchers to conduct sensitivity analysis with respect to the correlation $\rho$ in several special cases (Imai et al. 2010a, b), it is silent on how to produce consistent parameter estimates in the presence of correlation. Parametric causal mediation analysis does not offer a new modeling paradigm to empirical researchers because the mediator and outcome equations are still estimated separately as in classical mediation analysis (see Tingley et al. 2014 for details).

Because endogenous and causal mediation analysis both seek to identify mediation patterns with causal interpretations under the potential outcome framework, the direct and indirect effects can be de<sup>fi</sup>ned and interpreted in the same way. For a randomized binary treatment, the average treatment effect (ATE), that is, the total effect, can be written as

$$
A T E = E \big [ y _ {i} \mid x _ {i} = 1 \big ] - E \big [ y _ {i} \mid x _ {i} = 0 \big ].\tag{2}
$$

For simplicity, we focus on the case when the direct and indirect effects do not depend on the treatment status.<sup>4</sup> In this case, the average direct effect (ADE) can be simply de<sup>fi</sup>ned as

$$
A D E = E _ {m _ {i} (x _ {i} = 0)} \bigl [ E \bigl [ y _ {i} \mid x _ {i} = 1, m _ {i} \bigr ] - E \bigl [ y _ {i} \mid x _ {i} = 0, m _ {i} \bigr ] \bigr ],\tag{3}
$$

where $m _ { i } ( x _ { i } = 0 )$ represents the distribution of $m _ { i }$ in the absence of treatment.

Moreover, the average indirect effect (i.e., the mediation effect) can be obtained by subtracting the ADE from the ATE. Because the ATE can be consistently estimated by Equation (2), the identi<sup>fi</sup>cation of the mediation process boils down to obtaining a consistent estimate of the ADE. When the outcome equation is linear, the ADE can be reduced to a simple form, namely, $\beta _ { 1 }$ (Pearl 2014). More generally, when the treatment is continuous, we can compute the marginal treatment effect instead. Online Appendix B decomposes the average (marginal) treatment effects for different types of mediators.

This recursive two-stage modeling framework not only encompasses extant two-stage models to address endogeneity, such as the probit model with an endogenous continuous regressor (Rivers and Vuong 1988) and the endogenous treatment effect model (Heckman 1978), it also entails new models for mediation analysis (e.g., when the endogenous mediator is unobserved). Whereas prior studies provide fragmented discussions on the identi<sup>fi</sup>cation conditions of some individual models (e.g., Heckman 1978, Lewbel 2007, Dong and Lewbel 2015, Li et al. 2019), this paper seeks to provide a systematic investigation of the identi<sup>fi</sup>cation conditions of recursive two-stage models for different types of mediators and outcomes with a focus on previously less known or unknown identi<sup>fi</sup>cation conditions.

## 2.2. Endogenous Mediation

This section presents endogenous mediation models for three common types of mediators as well as their identi<sup>fi</sup>cation conditions. Speci<sup>fi</sup>cally, we consider continuous, binary, and count mediators, which are among the most frequently used types of mediators. Here, we focus on endogenous mediation models with a linear outcome equation. Linear regression is particularly popular in analyzing experimental data because of several desirable properties, such as the interpretational convenience of regression coef<sup>fi</sup>cients, the robustness of estimated treatment effect to the inclusion of predetermined endogenous control variables (Stock 2010), and the consistency of moderating effects (i.e., heterogeneous treatment effects) when the treatment is randomized and the moderators are predetermined (Nizalova and Murtazashvili 2016). Of course, the outcome equation need not be linear as is discussed in Section 2.4.

2.2.1. Continuous Mediator. When the mediator is continuous, we can use a linear model in the <sup>fi</sup>rst stage, and the two-stage model becomes

$$
m _ {i} = \alpha_ {0} + \alpha_ {1} x _ {i} + \alpha_ {2} z _ {i} + \lambda u _ {i},\tag{4a}
$$

$$
y _ {i} = \beta_ {0} + \beta_ {1} x _ {i} + \beta_ {2} z _ {i} + \gamma m _ {i} + \sigma v _ {i},\tag{4b}
$$

where $u _ { i }$ and $v _ { i }$ follow a standard bivariate normal distribution with correlation $\rho .$ This model is essentially a linear regression model with an endogenous continuous regressor.

As it is dif<sup>fi</sup>cult to see the identi<sup>fi</sup>cation conditions directly from the joint likelihood function (provided in Online Appendix C), we resort to a two-step estimation procedure, which views endogeneity as an omitted variable problem and estimates the <sup>fi</sup>rst and second stage equations sequentially (Heckman 1978, 1979). The consistency of the two-step procedure is well-established (Murphy and Topel 1985). As shown in Online Appendix D, the outcome equation can be reformulated as

$$
E \big [ y _ {i} | x _ {i}, z _ {i}, m _ {i} \big ] = \beta_ {0} + \beta_ {1} x _ {i} + \beta_ {2} z _ {i} + \gamma m _ {i} + \sigma \rho w _ {i},\tag{4c}
$$

where $\begin{array} { r } { w _ { i } = \frac { m _ { i } - ( \alpha _ { 0 } + \alpha _ { 1 } x _ { i } + \alpha _ { 2 } z _ { i } ) } { \lambda } } \end{array}$ represents the omitted term to account for the endogeneity of $m _ { i } .$ . Because $w _ { i }$ is a linear combination of the other regressors, the multicollinearity issue arises unless the correlation $\rho$ is exactly zero (so that the omitted term drops out of Equation (4c)) or $w _ { i }$ includes a regressor exclusive to the mediator. When the correlation is nonzero, this model is not identi<sup>fi</sup>ed without an instrument.

However, a useful variation of this model can be identi<sup>fi</sup>ed without an instrument. Speci<sup>fi</sup>cally, when the mediator is continuous but nonnegative (e.g., a duration mediator), a common choice is to model the mediator by $\begin{array} { r } { m _ { i } = \exp \left( \alpha _ { 0 } + \alpha _ { 1 } x _ { i } + \alpha _ { 2 } z _ { i } + \lambda u _ { i } \right) } \\ { \mathrm { e } \mathrm { m o d e l } , w _ { i } = \frac { \ln \left( m _ { i } \right) - \left( \alpha _ { 0 } + \alpha _ { 1 } x _ { i } + \alpha _ { 2 } z _ { i } \right) } { \lambda } \mathbf { i } } \end{array}$ . With such a <sup>fi</sup>rst-stag n Equation (4c). Because ln $\left( m _ { i } \right)$ is a highly nonlinear function of $m _ { i } ,$ , this two-stage model generally does not suffer from the multicollinearity issue and is well-identi<sup>fi</sup>ed without any instrument.

The endogenous mediation model for a continuous mediator is also identi<sup>fi</sup>ed when the <sup>fi</sup>rst stage model involves a high-order term (e.g., a quadratic term) or an interaction term that does not appear in the second stage (e.g., the moderated mediation process depicted by model 7 in Hayes 2017). In these special cases, the high-order or interaction term is effectively an instrument for the mediator. Nevertheless, it can be dif<sup>fi</sup>cult to justify why this term should be excluded in the second stage.

2.2.2. Binary Mediator. For a binary mediator, we can use a probit model in the <sup>fi</sup>rst stage:

$$
m _ {i} = 1 (\alpha_ {0} + \alpha_ {1} x _ {i} + \alpha_ {2} z _ {i} + u _ {i} > 0),\tag{5a}
$$

$$
y _ {i} = \beta_ {0} + \beta_ {1} x _ {i} + \beta_ {2} z _ {i} + \gamma m _ {i} + \sigma v _ {i},\tag{5b}
$$

where the standard deviation of the error term in the probit model is normalized to one to ensure that the parameters in the <sup>fi</sup>rst stage can be uniquely identi-<sup>fi</sup>ed. This model is the same as the endogenous treatment effect model (Heckman 1978, Greene 2012) in which the endogeneity issue can also be speci<sup>fi</sup>ed as an omitted variable problem (see Online Appendix D):

$$
\begin{array}{c} E \left[ y _ {i} \mid x _ {i}, z _ {i}, m _ {i} \right] = \beta_ {0} + \beta_ {1} x _ {i} + \beta_ {2} z _ {i} + \gamma m _ {i} + (2 m _ {i} - 1) \rho \sigma \\ * I M R (w _ {i}), \end{array}\tag{5c}
$$

where $w _ { i } = ( 2 m _ { i } - 1 ) ( \alpha _ { 0 } + \alpha _ { 1 } x _ { i } + \alpha _ { 2 } z _ { i } )$ and $I M R ( \cdot )$ represents the inverse Mills ratio (IMR) of the standard normal distribution.

Whereas the IMR function is theoretically nonlinear, it is approximately linear when w<sub>i</sub> is less than 0.5 or so (see Figure 2(a)). If $w _ { i }$ falls into the linear zone for most observations, the multicollinearity issue could still arise (Puhani 2000). The standard approach to circumventing multicollinearity is to use an instrument that affects the mediator but not the outcome, similar to the identi<sup>fi</sup>cation strategy for endogenous selection models (Puhani 2000, d’Haultfoeuille 2010). Nevertheless, instruments are notoriously dif<sup>fi</sup>cult to <sup>fi</sup>nd in practice. For experimental researchers, even though it is easy to obtain exogenous variables through randomized manipulation, it is dif<sup>fi</sup>cult to implement manipulation that affects the mediator but not the outcome (i.e., the exclusion restriction is hard to satisfy).

Much less known is that the multicollinearity problem can be addressed in the absence of an instrument. Speci<sup>fi</sup>cally, we only need to ensure that $w _ { i }$ falls out of the linear zone of the IMR function for a suf<sup>fi</sup>cient proportion of observations. As shown in Figure 2(b), the IMR function deviates more than 150% from the <sup>fi</sup>tted linear function when $\Phi ( w _ { i } )$ , the predicted probability of $m _ { i }$ to take the observed value, is larger than 0.75 (i.e., $w _ { i } > 0 . 6 7 )$ . One easy way to push w<sub>i</sub> out of the linear zone is to include exogenous control variables that have large supports and/or strong effects on the mediator. This approach is similar in spirit to the recent advance on the identi<sup>fi</sup>cation of endogenous selection or treatment models based on a special regressor (Lewbel 2007, Dong and Lewbel 2015). Whereas it is dif<sup>fi</sup>cult to implement manipulations that affect the mediator but not the outcome, it is relatively easy for experimental researchers to design manipulations that have large supports or strong effects on the mediator.

Figure 2. (Color online) Nonlinearity of Inverse Mills Ratio  
![](/api/attachments/8PSHZBD3/fulltext/images/392cab44cd33f05d4eba1f5660828fdf50bd6bcbfd9465334f374cc901a89e54.jpg)

The identi<sup>fi</sup>cation condition for a binary mediator is particularly important because mediators are often either binary in nature or reduced to two levels for simplicity. This discussion suggests that, when the independent variables in the <sup>fi</sup>rst stage can predict the binary mediator well, the identi<sup>fi</sup>cation of the model is strong.

2.2.3. Count Mediator. When the mediator is a count variable, a natural choice for the <sup>fi</sup>rst stage is a Poisson model. However, the standard Poisson model does not have an error term, making it impossible to model the correlation in error terms. In this case, the Poisson lognormal model (Greene 2009) with a normally distributed heterogeneity term is a better <sup>fi</sup>t. The Poisson lognormal model often produces similar estimates with the negative binomial model that assumes a Gamma heterogeneity term. Using a Poisson lognormal <sup>fi</sup>rst stage, the endogenous mediation model becomes the following:

$$
E [ m _ {i} | x _ {i}, z _ {i}, u _ {i} ] = \exp (\alpha_ {0} + \alpha_ {1} x _ {i} + \alpha_ {2} z _ {i} + \lambda u _ {i}),
$$

$$
y _ {i} = \beta_ {0} + \beta_ {1} x _ {i} + \beta_ {2} z _ {i} + \gamma m _ {i} + \sigma v _ {i},\tag{6a}
$$

(6b)

where Equation (6a) speci<sup>fi</sup>es the conditional mean of the Poisson process. As shown in Online Appendix D, the outcome equation can be reformulated as

(b)  
![](/api/attachments/8PSHZBD3/fulltext/images/7061afcf30984f6e869b3380688c3383572e9d0b57e67185d7ed343ca70d00b5.jpg)  
Notes. The linear function in panel (a) is <sup>fi</sup>tted based on the values of IMR in the range of ( 4, 0.5). The percentage difference in panel (b) is com puted as 100\*(IMR-linear)/linear, in which linear represents the <sup>fi</sup>tted linear function. In panel (b), Φ represents the cumulative distributio function of the standard normal distribution.

$$
E [ y _ {i} \mid x _ {i}, z _ {i} ] = \beta_ {0} + \beta_ {1} x _ {i} + \beta_ {2} z _ {i} + \gamma \exp (w _ {i}),\tag{6c}
$$

where $\begin{array} { r } { w _ { i } = \alpha _ { 0 } + \alpha _ { 1 } x _ { i } + \alpha _ { 2 } z _ { i } + \frac { \lambda ^ { 2 } } { 2 } . } \end{array}$ Because the second order derivative of exp w<sub>i</sub> is itself, exp w<sub>i</sub> is highly nonlinear unless $w _ { i }$ is highly negative (i.e., when the second order derivative exp w<sub>i</sub> is close to zero). This condition holds for all observations only in a trivial situation when the mediator is almost always zero. Therefore, this model can be identi<sup>fi</sup>ed by nonlinearity in most cases.

2.2.4. Model Estimation. Whereas the two-step estimator allows us to better understand the identi<sup>fi</sup>cation conditions of an endogenous mediation model, we generally recommend estimating the parameters by maximizing the joint likelihood of the two-stage models because of its attractive asymptotic properties. Speci<sup>fi</sup>- cally, maximum likelihood estimators are consistent, asymptotically normal, and asymptotically ef<sup>fi</sup>cient under mild regularity conditions (Greene 2012). The two-step estimator is not necessarily asymptotically ef<sup>fi</sup>cient and, hence, may produce larger standard errors. Besides, the maximum likelihood estimation extends seamlessly to nonlinear outcome equations and can accommodate latent mediators as is discussed next.

## 2.3. Latent Endogenous Mediation (LEM)

It is very common that the variable mediating the effect of a treatment is not observed by researchers. We now discuss how to accommodate an unobserved endogenous mediator in the recursive two-stage modeling framework.

2.3.1. Unobserved Continuous Mediator. If a continuous mediator is unobserved, the endogenous mediation model becomes

$$
m _ {i} ^ {*} = \alpha_ {0} + \alpha_ {1} x _ {i} + \alpha_ {2} z _ {i} + \lambda u _ {i},\tag{7a}
$$

$$
y _ {i} = \beta_ {0} + \beta_ {1} x _ {i} + \beta_ {2} z _ {i} + \gamma m _ {i} ^ {*} + \sigma v _ {i},\tag{7b}
$$

where $m _ { i } ^ { * }$ represents the latent mediator.

To determine the identi<sup>fi</sup>ability of this model, we can plug Equation (7a) into (7b), which yields

$$
y _ {i} = \beta_ {0} + \gamma \alpha_ {0} + (\beta_ {1} + \gamma \alpha_ {1}) x _ {i} + (\beta_ {2} + \gamma \alpha_ {2}) z _ {i} + \gamma \lambda u _ {i} + \sigma v _ {i}.\tag{7c}
$$

The weighted sum of two bivariate normally distributed variables, that is, $\gamma \lambda u _ { i } + \sigma v _ { i } ,$ , follows a normal distribution, and the parameters in Equation (7c) can be equivalently estimated by regressing Y over X and Z. Although the total treatment effect $\beta _ { 1 } + \gamma \alpha _ { 1 }$ is identi<sup>fi</sup>ed, it is impossible to separate the direct and indirect treatment effects even with an instrument. This <sup>fi</sup>nding extends to nonlinear outcome equations as well. Therefore, when an unobserved mediator is generated by a linear model, the mediation process is not identi<sup>fi</sup>able.

2.3.2. Unobserved Binary Mediator. When the mediator is unobserved, it is often assumed to be binary o categorical to facilitate interpretation. Here, we focus on the case when the unobserved mediator is binary. In this case, we can use a probit model for the <sup>fi</sup>rst stage:

$$
m _ {i} ^ {*} = 1 (\alpha_ {0} + \alpha_ {1} x _ {i} + \alpha_ {2} z _ {i} + u _ {i} > 0),
$$

$$
y _ {i} = \beta_ {0} + \beta_ {1} x _ {i} + \beta_ {2} z _ {i} + \gamma m _ {i} ^ {*} + \sigma v _ {i}.\tag{8a}
$$

(8b)

Because the mediator equation is nonlinear, the issue of perfect multicollinearity does not necessarily arise when plugging Equation (8a) into (8b). Hence, it is possible to identify this model. Online Appendix C discusses how to estimate the parameters using the expectation-maximization algorithm (Dempster et al. 1977). The sign of $\gamma$ is not identi<sup>fi</sup>ed in this model as the two set of parameters $\{ \alpha _ { 0 } , \alpha _ { 1 } , \alpha _ { 2 } , \beta _ { 0 } , \gamma , \rho \}$ and $\{ - \alpha _ { 0 } , - \alpha _ { 1 } , - \alpha _ { 2 } , \beta _ { 0 } + \gamma , - \gamma , - \rho \}$ lead to identical likelihood while holding the other parameters the same. Without loss of generality, γ is restricted to be positive to ensure that the model estimates are unique. When the latent mediator takes more than two levels, we can use a multinomial probit model for the mediator and further assume that all the error terms are multivariate normally distributed to simplify the derivation of the overall likelihood function.

2.3.3. Partially Observed Binary Mediator. In many settings, a mediator is unobserved because it is too costly to measure. However, it might still be affordable to measure the mediator for a random subset of units. The latent mediation model given by Equations (8a) and (8b) can be easily adapted to accommodate a partially observed binary mediator. When a binary mediator is partially observed, the likelihood function for a unit whose mediator is observed reduces to the likelihood for Equations (5a) and (5b). The overall likelihood function can still be maximized using the same expectation-maximization algorithm except that the expectation step only needs to be executed for units whose mediators are unobserved. If the subset of units whose mediator status is measured are not randomly selected, the probability of each unit to be measured (or not measured) should also be considered in the likelihood function. When the mediator is partially observed, the sign of γ can be identi<sup>fi</sup>ed.

Our proposed model for latent mediators has three important differences from extant latent mediation models (Muthen and Asparouhov´ 2015, Albert et al. 2016): (1) our model does not rely on the SIA assumption, (2) our model achieves identi<sup>fi</sup>cation by model ing the DGP rather than by leveraging noisy proxies of the latent mediator, and (3) our model allows the mediator to be partially observed.

2.4. Extensions to Nonlinear Outcome Equations The aforementioned endogenous mediation models can be extended to accommodate nonlinear outcome equations. For instance, when the outcome is binary and we use a probit model for the second stage, the model for a continuous mediator becomes the probit model with an endogenous continuous regressor (Rivers and Vuong 1988), whereas the model for a binary mediator becomes the recursive bivariate probit model (Carrasco 2001, Li et al. 2019). The latent endogenous mediation model can also accommodate nonlinear outcome equations. As an example, Online Appendix C shows how to estimate the latent mediation model for a binary outcome variable.

When the outcome equation is nonlinear, it is analytically dif<sup>fi</sup>cult to specify the endogeneity of the mediator as an omitted variable problem. However, our extensive simulations show that the identi<sup>fi</sup>cation conditions for the linear outcome equation extend to nonlinear outcome equations. In other words, the identi<sup>fi</sup>ability of the endogenous mediation model primarily depends on the functional form of the <sup>fi</sup>rst stage, rather than that of the second stage.

## 2.5. Extension to Other Joint Error Distributions

So far, we assume that the error terms for the mediator and the outcome are bivariate normally distributed. The endogenous mediation analysis framework can be easily extended to incorporate other types of joint error distributions following the copula modeling approach (Nelsen 2007, Trivedi and Zimmer 2007). The copula approach models the joint distribution of multiple random variables in two steps: (1) specify the marginal distribution of each random variable and (2) specify the dependence structure for these random variables. The marginal distributions are called marginals, and the functions characterizing the dependence structures are called copulas.

According to Sklar’s theorem, any multivariate joint distribution can be de<sup>fi</sup>ned using the copula modeling approach (Sklar 1959). For example, the bivariate normality assumption for error terms can be decomposed into two subassumptions: (1) the error terms for the mediator and outcome equations are both normally distributed and (2) the dependence structure of the two error terms is a Gaussian copula. Neither subassumption is necessary for the model to work. The marginals can be speci<sup>fi</sup>ed as other distributions, such as lognormal, logistic, Gamma, Gumbel, or Weibull. There are also other copulas to model the dependence structure among random variables, such as Frank, Clayton, and Joe copulas. The functional forms for these copulas are omitted because of space limitations. Interested readers please refer to Nelsen (2007) and Trivedi and Zimmer (2007) for more information about the copula approach.

Figure 3 shows the scatterplots of two positively cor related random variables whose dependence structure is captured by the Gaussian, Frank, Clayton, and Joe copulas, respectively. Although the rank correlations of the two random variables are the same (i.e., 0.5) in these four subplots, the correlation patterns are different.<sup>5</sup> The Clayton copula represents a dependence structure with strong lower tail dependence but weak upper tail dependence, whereas the Joe copula is vice versa. The Gaussian and Frank copulas both have symmetric upper and lower tail dependencies, but the tail dependence is stronger for the Gaussian copula. In Section 3.4, we discuss the sensitivity of endogenous mediation models to the choices of marginals and copulas.

## 3. Simulation

We validate the identi<sup>fi</sup>cation conditions of endogenous mediation analysis through simulations with a focus on previously less known or unknown identi<sup>fi</sup>- cation conditions for endogeneity, including identi<sup>fi</sup>- cation by the nonlinearity of the <sup>fi</sup>rst stage, enhancing identi<sup>fi</sup>cation with exogenous control variables, and the identi<sup>fi</sup>cation of models with latent endogenous mediators.

We consider three endogenous mediation models. In the <sup>fi</sup>rst model, we use the treatment as the sole regressor in the mediator and outcome equations. In the second model, we assume that an instrument vari able is available for the mediator and include it in the mediator equation. The third model includes a control variable in both equations, which is plausible when an exogenous manipulation affects both the mediator and the outcome. In addition to these endogenous mediation models, we also consider a causal mediation model, which estimates the outcome equation independently from the mediator equation (Tingley et al. 2014). The bias of this model allows us to understand the consequence of the SIA assumption. Table 1 summarizes the purposes of all four models.

These models are evaluated using three commonly used metrics in simulation studies (Imai et al. 2010b, Frandsen 2015, Li et al. 2019), namely, bias, root mean square error (RMSE), and the coverage probabilities (CP). Bias is the average difference between the esti mated parameter value and the true value over multiple simulations. RMSE measures the standard deviation of bias in multiple simulations. CP represents the probability that the 95% con<sup>fi</sup>dence interval of the parameter estimate covers its true value and is expected to be exactly 95% for the true model. Whether the CP is close to 95% allows us to understand whether a model can make reliable statistical inference on the signi<sup>fi</sup>cance level of an independent variable. In our simulations, we focus on the coef<sup>fi</sup> cients of the outcome equation, especially the coef<sup>fi</sup>cient of the treatment variable. When the outcome equation is linear, the coef<sup>fi</sup>cient of the treatment variable can be interpreted as the direct treatment effect.

Figure 3. (Color online) The Dependence Structures Captured by Different Copulas  
![](/api/attachments/8PSHZBD3/fulltext/images/c57b1cbf15c6d80463a919055ef26f902fa4ea42b3f8c9940f5f01f5eea9ec94.jpg)

![](/api/attachments/8PSHZBD3/fulltext/images/35b2d230d6f586a0f019a5c625748077b5c5125b7f0cd77c23f07037a03ab402.jpg)

![](/api/attachments/8PSHZBD3/fulltext/images/c09b1c8d3370a389ed3c55d4ed116e058d21255d43874ded98e9256c9a94333d.jpg)

![](/api/attachments/8PSHZBD3/fulltext/images/8cd4bf564280fb1878dc0cb3b918687f1e4d86e545e7ff3085f6ecd0ad408307.jpg)

## 3.1. Identification by Nonlinearity

To test the possibility of identi<sup>fi</sup>cation by nonlinearity, we begin with the following DGP:

$$
\begin{array}{r l r} & & m _ {i} = 1 (1 + x _ {i} + z _ {i} + u _ {i} > 0), \\ & & y _ {i} = 1 + x _ {i} + m _ {i} + v _ {i}, \\ & & \left( \begin{array}{l} u _ {i} \\ v _ {i} \end{array} \right) \sim N \left(\left( \begin{array}{l} 0 \\ 0 \end{array} \right), \left( \begin{array}{l l} 1 & - 0. 5 \\ - 0. 5 & 1 \end{array} \right)\right), \end{array}\tag{DGP 1}
$$

where $x _ { i }$ is a randomized treatment with equal probabilities to be zero and one. $z _ { i } \sim N ( 0 , 1 )$ is an instrumental variable that affects the mediator but not the out come. To facilitate the computation of biases based on average point estimates, we assume all coef<sup>fi</sup>cients in the DGP to be one. We arbitrarily choose 0.5 as the correlation between the two error terms, but the qualitative results are similar for other values (e.g., 0.5).

To investigate the large sample properties of the models in Table 1, we simulate a relatively large data set with 10,000 observations from this DGP. We skip the last model in Table 1 because no control variable affects both the mediator and the outcome in the DGP. We repeat this process 1,000 times. Table 2 reports the average estimates (from which we can easily calculate the biases), RMSEs, and CPs of the three models for each parameter.

Table 1. Models Used for Comparison

<table><tr><td>Model</td><td>Purpose</td></tr><tr><td>CM</td><td>Understand the potential bias of causal mediation analysis under the SIA assumption</td></tr><tr><td>EM</td><td>Verify the possibility of identification by nonlinearity</td></tr><tr><td>EM with instrument</td><td>Illustrate the identification of model parameters in an ideal situation</td></tr><tr><td>EM with control</td><td>Verify the possibility of improving identification with an exogenous control variable</td></tr></table>

Note. We implement the endogenous mediation models discussed in Section 2 in the R package “endogeneity,” which is available at https:/ CRAN.R-project.org/package=endogeneity.

The average parameter estimates produced by the CM model are considerably different from the true values. The CPs of the CM model are close to zero, suggesting that the 95% con<sup>fi</sup>dence intervals of the parameter estimates almost never cover the true values. In comparison, the average estimates by the EM model are much closer to the true values (e.g., the bias on the treatment variable is only 0.7%) and the RMSEs are about one third of those by the CM model, which demonstrate that accounting for the endogeneity of the mediator can signi<sup>fi</sup>cantly reduce both the magnitude and variance of the bias. Not surprisingly, the CPs of the EM model are also very close to the nominal 95% coverage. More importantly, the performance of the EM model is close to that of the EM mode with an instrument, con<sup>fi</sup>rming that it is possible to identify an EM model through nonlinearity. These <sup>fi</sup>ndings generalize to mediators with nonlinear DGPs, such as count and duration mediators (see Online Appendix E1).

## 3.2. Improving Identification with an Exogenous Control

To investigate whether an exogenous control variable can improve the identi<sup>fi</sup>cation when the nonlinearity of the <sup>fi</sup>rst stage is weak (which often occurs when the mediator is binary), we consider a mediation process identical to (DGP 1) except that we allow the exogenous variable Z to in<sup>fl</sup>uence the outcome (i.e., the exclusion restriction becomes invalid):

$$
\begin{array}{c} m _ {i} = 1 (1 + x _ {i} + z _ {i} + u _ {i} > 0), \\ y _ {i} = 1 + x _ {i} + m _ {i} + z _ {i} + v _ {i}, \\ \binom{u _ {i}}{v _ {i}} \sim N \biggl (\binom{0}{0}, \left( \begin{array}{c c} 1 & - 0. 5 \\ - 0. 5 & 1 \end{array} \right) \biggr). \end{array}\tag{DGP 2}
$$

Table 3 summarizes the results of four mediation models over 1,000 simulations with 10,000 observations each. We do not use the control variable Z in the <sup>fi</sup>rst two models. In the third model, we treat the variable Z as an instrument even though it does not satisfy the exclusion restriction, which allows us to understand the consequence of using an invalid instrument. We use the control variable in the fourth model and see how it improves identi<sup>fi</sup>cation. Consistent with what we observed in Table 2, the biases and RMSEs of the EM model are noticeably smaller than those of the CM model. Once the control variable is used in the EM model, the biases on all parameters immediately drop to no more than 0.3% and the CPs increase to around 95%, demonstrating that an exogenous control variable can effectively improve the identi<sup>fi</sup>cation of an EM model. Conversely, the EM model that incorrectly treats Z as an instrument has much larger biases than the CM model, which suggests that using an invalid instrument can be worse than not using any at all.

In Online Appendix E1, we report additional simulation results for count and duration mediators. Not surprisingly, for count and duration mediators with highly nonlinear <sup>fi</sup>rst stages, the biases of the EM models are negligible, and the RMSEs are very small even without using the control variable. With that being said, we <sup>fi</sup>nd that using the control variable can further reduce the RMSEs of the EM models for count and duration mediators. We also consider a DGP with a nonlinear outcome equation (i.e., a probit model) in Online Appendix E2 and <sup>fi</sup>nd that the use of an exogenous control variable continues to improve identi<sup>fi</sup>cation substantially.

## 3.3. Identification of Latent Endogenous Mediation

To investigate whether the identi<sup>fi</sup>cation conditions for observed mediators generalize to unobserved mediators, we continue to use the data simulated in Section 3.2 and estimate the latent versions of the EM models with and without using the control, treating the mediator as unobserved. Table 4 summarizes the results. Compared with the EM model in Table 3, the LEM model has larger biases and RMSEs, and the CP is noticeably smaller than 95%. Nonetheless, the inclusion of the control variable in the LEM model signi<sup>fi</sup>- cantly reduces the biases and RMSEs. In particular, the average bias on the direct treatment effect drops to 1.5% and the CP increases to 94.9%. This <sup>fi</sup>nding demonstrates that exogenous control variables can effectively improve the identi<sup>fi</sup>cation of the LEM model. In Online Appendix E2, we report additional simulation results for LEM when the outcome equation is a probit model and the results are similar.

Table 2. Identi<sup>fi</sup>cation of Endogenous Mediation with a Binary Mediator

<table><tr><td rowspan="2"></td><td colspan="3">CM</td><td colspan="3">EM</td><td colspan="3">EM with instrument</td></tr><tr><td>Estimate</td><td>RMSE</td><td>CP</td><td>Estimate</td><td>RMSE</td><td>CP</td><td>Estimate</td><td>RMSE</td><td>CP</td></tr><tr><td colspan="10">Outcome</td></tr><tr><td>Intercept</td><td>1.483</td><td>0.484</td><td>0.000</td><td>1.033</td><td>0.165</td><td>0.944</td><td>0.998</td><td>0.037</td><td>0.942</td></tr><tr><td>X</td><td>1.102</td><td>0.103</td><td>0.001</td><td>1.007</td><td>0.039</td><td>0.947</td><td>0.999</td><td>0.021</td><td>0.951</td></tr><tr><td>M</td><td>0.366</td><td>0.635</td><td>0.000</td><td>0.957</td><td>0.215</td><td>0.944</td><td>1.003</td><td>0.045</td><td>0.946</td></tr><tr><td colspan="10">Mediator</td></tr><tr><td>Intercept</td><td></td><td></td><td></td><td>0.707</td><td>0.293</td><td>0.000</td><td>1.002</td><td>0.026</td><td>0.948</td></tr><tr><td>X</td><td></td><td></td><td></td><td>0.707</td><td>0.295</td><td>0.000</td><td>1.000</td><td>0.040</td><td>0.938</td></tr><tr><td>Z</td><td></td><td></td><td></td><td></td><td></td><td></td><td>1.001</td><td>0.026</td><td>0.909</td></tr><tr><td>Correlation</td><td></td><td></td><td></td><td>-0.329</td><td>0.205</td><td>0.462</td><td>-0.502</td><td>0.025</td><td>0.949</td></tr></table>

Notes. In the EM model, the estimates in the <sup>fi</sup>rst stage appear to be biased but they are not because the scale of the parameters is not identi<sup>fi</sup>ed in a probit model. If we multiply the <sup>fi</sup>rst stage coef<sup>fi</sup>cients and the correlation by 1.4, they are very close to the true values.

Table 3. Comparison of Different Identi<sup>fi</sup>cation Strategies

<table><tr><td rowspan="2"></td><td colspan="3">CM</td><td colspan="3">EM</td><td colspan="3">EM with instrument</td><td colspan="3">EM with control</td></tr><tr><td>Estimate</td><td>RMSE</td><td>CP</td><td>Estimate</td><td>RMSE</td><td>CP</td><td>Estimate</td><td>RMSE</td><td>CP</td><td>Estimate</td><td>RMSE</td><td>CP</td></tr><tr><td colspan="13">Outcome</td></tr><tr><td>Intercept</td><td>0.517</td><td>0.485</td><td>0.000</td><td>0.932</td><td>0.319</td><td>0.860</td><td>-0.415</td><td>1.415</td><td>0.000</td><td>0.998</td><td>0.052</td><td>0.951</td></tr><tr><td>X</td><td>0.897</td><td>0.107</td><td>0.045</td><td>0.985</td><td>0.073</td><td>0.895</td><td>0.700</td><td>0.301</td><td>0.000</td><td>0.999</td><td>0.022</td><td>0.957</td></tr><tr><td>M</td><td>1.636</td><td>0.637</td><td>0.000</td><td>1.089</td><td>0.418</td><td>0.862</td><td>2.861</td><td>1.861</td><td>0.000</td><td>1.003</td><td>0.065</td><td>0.948</td></tr><tr><td>Z</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1.000</td><td>0.015</td><td>0.949</td></tr><tr><td colspan="13">Mediator</td></tr><tr><td>Intercept</td><td></td><td></td><td></td><td>0.708</td><td>0.293</td><td>0.000</td><td>0.859</td><td>0.143</td><td>0.000</td><td>1.002</td><td>0.026</td><td>0.941</td></tr><tr><td>X</td><td></td><td></td><td></td><td>0.707</td><td>0.295</td><td>0.000</td><td>0.743</td><td>0.259</td><td>0.000</td><td>1.000</td><td>0.041</td><td>0.934</td></tr><tr><td>Z</td><td></td><td></td><td></td><td></td><td></td><td></td><td>1.190</td><td>0.191</td><td>0.000</td><td>1.001</td><td>0.026</td><td>0.910</td></tr><tr><td>Correlation</td><td></td><td></td><td></td><td>0.214</td><td>0.731</td><td>0.032</td><td>-0.931</td><td>0.431</td><td>0.000</td><td>-0.502</td><td>0.033</td><td>0.949</td></tr></table>

Notes. In addition to the CM model, we have estimated a CM with control model that controls for Z. This model also has noticeable bias because the mediator is still endogenous conditional on X and Z.

## 3.4. Sensitivity Analysis

We conduct a series of sensitivity analyses to investigate the robustness of endogenous mediation analysis and shed light on potential factors in<sup>fl</sup>uencing the bias, RMSE, and CP of the parameter estimates. We begin with examining the sensitivity of EM models to the level of endogeneity (i.e., the correlation in error terms) as compared with the CM models. Next, we investigate the sensitivity of the EM models to the goodness of <sup>fi</sup>t of the <sup>fi</sup>rst stage. Then, we examine how the performance of LEM models varies with the percentage of observed mediators. After that, we investigate the sensitivity of EM models to misspeci<sup>fi</sup>cations of copulas and marginals for the error terms. Our sensitivity analyses in this section focus on binary mediators. The sensitivity analyses for duration and count mediators are provided in Online Appendix F. The <sup>fi</sup>ndings from our sensitivity analyses should be interpreted qualitatively rather than quantitatively because the sizes of bias and RMSE may vary across DGPs.

Table 4. Identi<sup>fi</sup>cation of Latent Endogenous Mediation with a Binary Mediator

<table><tr><td rowspan="2"></td><td colspan="3">LEM</td><td colspan="3">LEM with control</td></tr><tr><td>Estimate</td><td>RMSE</td><td>CP</td><td>Estimate</td><td>RMSE</td><td>CP</td></tr><tr><td colspan="7">Outcome</td></tr><tr><td>Intercept</td><td>0.877</td><td>0.446</td><td>0.861</td><td>0.897</td><td>0.217</td><td>0.909</td></tr><tr><td>X</td><td>0.958</td><td>0.118</td><td>0.837</td><td>0.985</td><td>0.046</td><td>0.949</td></tr><tr><td>M</td><td>1.200</td><td>0.590</td><td>0.786</td><td>1.137</td><td>0.276</td><td>0.864</td></tr><tr><td>Z</td><td></td><td></td><td></td><td>0.987</td><td>0.035</td><td>0.927</td></tr><tr><td colspan="7">Mediator</td></tr><tr><td>Intercept</td><td>0.628</td><td>0.410</td><td>0.623</td><td>0.976</td><td>0.165</td><td>0.951</td></tr><tr><td>X</td><td>0.689</td><td>0.358</td><td>0.636</td><td>0.947</td><td>0.225</td><td>0.882</td></tr><tr><td>Z</td><td></td><td></td><td></td><td>0.945</td><td>0.194</td><td>0.845</td></tr><tr><td>Correlation</td><td>0.185</td><td>0.726</td><td>0.302</td><td>-0.535</td><td>0.072</td><td>0.922</td></tr></table>

3.4.1. Sensitivity to the Correlation Between Error Terms. For this sensitivity analysis, we vary the correlation parameter in (DGP 2) from 0.9 to 0.9 at intervals of 0.1. Figure 4 summarizes how the bias, RMSE, and CP of the CM and EM models vary with the correlation based on 1,000 simulations with 2,000 observations each. The results demonstrate the advantage of the EM model over the CM model in multiple aspects. First, the biases of the EM model in estimating the coef<sup>fi</sup>cients of the treatment and mediator variables in the outcome equation are close to zero regardless of the level of correlation. On the contrary, the estimates of the CM model are highly sensitive to the correlation parameter and are biased unless the correlation parameter is zero (i.e., the SIA assumption holds). Second, the RMSEs of the EM model are much smaller than those of the CM model except when the correlation is very close to zero. The slightly large RMSEs of the EM model at a correlation of zero are expected as the correlation parameter in the EM model is redundant when the true correlation is zero. Third, the CPs of the EM model are always close to 95%, whereas those of the CM model can be much lower than 95% when the correlation is strong or even moderate. Online Appendix F1 reports the sensitivity analysis for count and duration mediators, and the substantive <sup>fi</sup>ndings are similar. Compared with the CM model, the EM model has little to lose when the SIA assumption holds but much to gain when this assumption does not hold.

![](/api/attachments/8PSHZBD3/fulltext/images/3b0b4dc4467f525de62eeb8c32e366a25f1cc9b151e64c40288167cb41c3f4fa.jpg)  
Figure 4. (Color online) Sensitivity to the Correlation Between Error Terms

3.4.2. Sensitivity to the Goodness of Fit of the First Stage. As explained in Section 2.2, the identi<sup>fi</sup>cation of EM models relies on the nonlinearity of the omitted variable. The omitted variable is usually a nonlinear function of the term $\omega _ { i } = \alpha _ { 0 } + \alpha _ { 1 } x _ { i } + \alpha _ { 2 } z _ { i } ,$ , which represents the combined linear effect of the treatment and control variables. The nonlinear function is less likely to be stuck in a linear region if $\omega _ { i }$ has a larger support and variance, which occurs when the treatment and control variables are stronger predictors of the mediator. Therefore, the identi<sup>fi</sup>cation of EM models may depend on the goodness of <sup>fi</sup>t of the <sup>fi</sup>rst stage. Loglikelihood is the most widely used measure for goodness of <sup>fi</sup>t for nonlinear models, but it is unbounded, making its magnitude dif<sup>fi</sup>cult to interpret. A commonly used bounded metric for the goodness of <sup>fi</sup>t of nonlinear models is McFadden’s pseudo $R ^ { 2 } ,$ , which is de<sup>fi</sup>ned as follows:

$$
R ^ {2} = 1 - \frac {\ln L _ {f u l l}}{\ln L _ {i n t e r c e p t}},\tag{9}
$$

where $L _ { f u l l }$ represents the likelihood of the full mediator model and $L _ { i n t e r c e p t }$ represents the likelihood of a reduced mediator model with only the intercept. This pseudo $R ^ { 2 }$ ranges from zero to one and is easy to interpret.

To test how sensitive the identi<sup>fi</sup>cation of an EM model is to the pseudo $R ^ { 2 } ,$ we modify the <sup>fi</sup>rst stage of (DGP 2) to $m _ { i } = 1 ( 1 + x _ { i } + \alpha z _ { i } + u _ { i } > 0 )$ , where α is a scalar. When α is positive, the pseudo $R ^ { 2 }$ of the <sup>fi</sup>rst stage increases monotonically with α. We increase α from zero to one at intervals of 0.1 and then estimate the EM model at each value of α. Figure 5 shows how the various metrics vary with the pseudo $R ^ { 2 }$ based on 1,000 simulations at each value of α with 2,000 observations each.

The biases and RMSEs both decrease with pseudo $R ^ { 2 } ,$ whereas the CP <sup>fi</sup>rst increases with pseudo $\mathbf { \dot { \boldsymbol { R } } } ^ { 2 }$ and then converges to 95%. These <sup>fi</sup>ndings con<sup>fi</sup>rm that the identi<sup>fi</sup>cation of EM models increases with the goodness of <sup>fi</sup>t of the <sup>fi</sup>rst stage. Notably, all three metrics improve dramatically as the pseudo $R ^ { 2 }$ increases from about 0.1 to 0.15, but the improvement diminishes gradually as the pseudo $R ^ { 2 }$ further increases. This <sup>fi</sup>nding suggests that adding more control variables can be particularly helpful when the existing covariates do not predict the mediator well. In Online Appendix F2, we show that the RMSE decreases with the pseudo $R ^ { 2 }$ of the <sup>fi</sup>rst stage for count and duration mediators as well, demonstrating that pseudo $R ^ { 2 }$ is a useful measure for the strength of identi<sup>fi</sup>cation through nonlinearity.

3.4.3. Sensitivity to the Percentage of Observed Values for the Mediator. The LEM model can accommodate partially unobserved binary mediators. This section investigates how the performance of the LEM model varies with the percentage of observed values for the mediator. We simulate 2,000 observations based on (DGP 2) and set the mediator to be observed for 0%–100% randomly selected observations at a step size of 10%. Figure 6 shows how different metrics vary with the observed percentage based on 1,000 simulations at each percentage level. To understand how the partial observability of the mediator helps identify the sign of the mediator’s coef<sup>fi</sup>cient in the outcome equation, we do not restrict the mediator’s coef<sup>fi</sup>cient to be positive when the mediator is fully unobserved.

The results show that the biases and RMSEs drop drastically as the percentage of observed values increases from 0% to 10%, suggesting that the partial observability of the mediator can signi<sup>fi</sup>cantly reduce the bias and variance of the estimates produced by the LEM model. After that, they decrease at a much slower rate. This <sup>fi</sup>nding suggests that, when the measurement of a mediator is costly, it may suf<sup>fi</sup>ce to only measure it for 10%\~20% of units as the marginal return of measuring the mediator for more units diminishes quickly.

It should be noted that the LEM model does not always converge in a concave region, especially when the mediator is fully unobserved. When calculating the evaluation metrics, we exclude simulations in which the LEM model fails to converge properly. In our 1,000 simulations, the failure rate is 12.7% when the mediator is completely unobserved but immediately drops to 0% when the mediator is partially observed. This <sup>fi</sup>nding further demonstrates the effectiveness of the partial observability of the mediator in improving identi<sup>fi</sup>cation. As shown in Online Appendix F3, the sensitivity pattern is similar if the outcome equation is a probit model.

![](/api/attachments/8PSHZBD3/fulltext/images/eeda7bc137fd3c994ab0f471f1316a66970871884603278e5241fd0b468deb53.jpg)  
Figure 5. (Color online) Sensitivity to the Goodness of Fit for a Binary Mediator

3.4.4. Sensitivity to Misspecification of Copulas. So far, the DGPs in our simulations assume that the error terms for the mediator and the outcome are bivariate normally distributed. This assumption is not valid if the error terms do not have normal marginals or the dependence structure between them is not a Gaussian copula. In the remaining two sections, we investigate how misspeci<sup>fi</sup>cations of marginals and copulas in<sup>fl</sup>uence the estimates of EM models.<sup>6</sup> Owing to the central limit theorem, assuming the error terms to have normal marginals is often not a bad assumption. Hence, we begin with the sensitivity analysis on the misspeci<sup>fi</sup>cation of copulas.

For this sensitivity analysis, we consider four variants of (DGP 2) in which the two error terms both have normal marginals, but the dependence structures between them are captured by the Gaussian, Frank, Clayton, and Joe copulas, respectively. These copulas and their rotated versions can account for both positive and negative correlations. For simplicity, we set the rank correlation of the two error terms to be positive (i.e., 0.5) so that we only need to use the standard versions of these copulas. Then, for each DGP, we estimate four models that rely on four different copula speci<sup>fi</sup>cations. Table 5 summarizes the results of each model for each type of DGP based on 1,000 simulations with 2,000 observations each. We only report the average point estimate and the RMSE for each parameter to make the table easier to read.

As expected, each model works the best when the underlying copula assumption is true. Interestingly, the Gaussian copula model can produce almost unbiased estimates for the treatment variable regard less of which copula is used in the DGP. In contrast, the other copula models produce estimates with sizable biases if the underlying copula assumptions are incorrect. The intuition behind the superior performance of the Gaussian copula is that it allows the error terms to be dependent on the full support. No matter the true dependence of the error terms concentrated on the lower tail (Clayton), the upper tail (Joe), or the middle (Frank), the Gaussian copula can capture the dependence to some extent. Conversely, the other three copulas that focus on local dependencies are sensitive to mismatch. For instance, the estimated rank correlation by the Clayton copula speci<sup>fi</sup>cation is almost zero when the DGP is a Joe copula and vice versa. The robustness of the Gaussian copula to misspeci<sup>fi</sup>cation makes it an attractive option in practice.

Figure 6. (Color online) Sensitivity to the Percentage of Observed Values for the Mediator  
![](/api/attachments/8PSHZBD3/fulltext/images/ffd4a7034c9af65bd91cacbd86fb36f38bebe5afa19a088f7600036ddc172f37.jpg)

Table 5. Sensitivity of Model Estimates to Copula Misspeci<sup>fi</sup>cation

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">Gaussian</td><td colspan="2">Frank</td><td colspan="2">Clayton</td><td colspan="2">Joe</td></tr><tr><td>Estimate</td><td>RMSE</td><td>Estimate</td><td>RMSE</td><td>Estimate</td><td>RMSE</td><td>Estimate</td><td>RMSE</td></tr><tr><td rowspan="3">DGP: Gaussian</td><td>X</td><td>1.000</td><td>0.047</td><td>0.978</td><td>0.053</td><td>0.959</td><td>0.070</td><td>0.909</td><td>0.107</td></tr><tr><td>M</td><td>1.001</td><td>0.106</td><td>1.129</td><td>0.181</td><td>1.194</td><td>0.314</td><td>1.528</td><td>0.578</td></tr><tr><td>Correlation</td><td>0.501</td><td>0.038</td><td>0.473</td><td>0.058</td><td>0.309</td><td>0.207</td><td>0.339</td><td>0.201</td></tr><tr><td rowspan="3">DGP: Frank</td><td>X</td><td>0.994</td><td>0.048</td><td>1.001</td><td>0.047</td><td>0.865</td><td>0.149</td><td>0.954</td><td>0.071</td></tr><tr><td>M</td><td>1.041</td><td>0.120</td><td>1.003</td><td>0.095</td><td>1.824</td><td>0.886</td><td>1.276</td><td>0.340</td></tr><tr><td>Correlation</td><td>0.444</td><td>0.071</td><td>0.501</td><td>0.038</td><td>0.076</td><td>0.435</td><td>0.432</td><td>0.121</td></tr><tr><td rowspan="3">DGP: Clayton</td><td>X</td><td>0.988</td><td>0.049</td><td>0.968</td><td>0.060</td><td>1.001</td><td>0.046</td><td>0.801</td><td>0.204</td></tr><tr><td>M</td><td>1.084</td><td>0.125</td><td>1.274</td><td>0.298</td><td>1.000</td><td>0.076</td><td>2.240</td><td>1.243</td></tr><tr><td>Correlation</td><td>0.550</td><td>0.064</td><td>0.501</td><td>0.051</td><td>0.503</td><td>0.029</td><td>0.021</td><td>0.482</td></tr><tr><td rowspan="3">DGP: Joe</td><td>X</td><td>0.995</td><td>0.049</td><td>1.006</td><td>0.048</td><td>0.855</td><td>0.152</td><td>0.999</td><td>0.046</td></tr><tr><td>M</td><td>1.021</td><td>0.139</td><td>0.895</td><td>0.153</td><td>1.896</td><td>0.898</td><td>0.997</td><td>0.099</td></tr><tr><td>Correlation</td><td>0.372</td><td>0.139</td><td>0.454</td><td>0.063</td><td>0.001</td><td>0.499</td><td>0.501</td><td>0.043</td></tr></table>

Notes. This table focuses on three parameters of primary interest to researchers, namely, the coef<sup>fi</sup>cients of the treatment and the mediator in the outcome equation as well as the estimated rank correlation of the two error terms. Their true values are 1, 1, and 0.5, respectively.

3.4.5. Sensitivity to Misspecification of Marginals. Now, we examine the sensitivity of EM models to misspeci-<sup>fi</sup>cation of marginals. As the outcome equation is often assumed to be linear and the point estimates of linear models are not sensitive to the distributional assumption on the error term, we focus on misspeci<sup>fi</sup>cation of the marginal distribution of the error term in the mediator equation. We consider a binary mediator for this sensitivity analysis because there is a rich set of models for binary response variables stemming from different distributional assumptions on error terms. For example, by assuming that the error term follows a normal/ logistic/Gumbel distribution, the model for a binary dependent variable becomes a probit/logit/complementary log-log (cloglog) model.

We consider three versions of (DGP 2), in which the marginals for the error in the mediator equation are assumed to be normal, logistic, and Gumbel distributions, respectively. For each of the three DGPs, we estimate three EM models in which the <sup>fi</sup>rst stages are probit, logit, and cloglog models, respectively. Table 6 summarizes the average point estimates of each model for each type of DGP based on 1,000 simulations with 2,000 observations each.

Whereas misspeci<sup>fi</sup>cation of the marginal distribution of the error term for the mediator can lead to substantial bias in the <sup>fi</sup>rst stage, the biases in the outcome equation are negligible, and the RMSEs are also small. This <sup>fi</sup>nding suggests that, when the mediator is binary, the estimates in the outcome equation are not sensitive to misspeci<sup>fi</sup>cation of the marginal distribution of the error term for the mediator. This <sup>fi</sup>nding is important as binary mediators are very common in practice.

## 4. Discussion

In addition to the simulations, we further illustrate the differences between CM and EM using several real-world data sets. The results are reported in Online Appendix G. In this section, we summarize the key insights from this study. In Section 4.1, we provide detailed explanations regarding the differences between CM and EM and provide guidelines on when to use each method. In Section 4.2, we more broadly discuss when to use instrument- and model-based identi<sup>fi</sup>cation strategies to address the endogeneity issue, not necessarily that of a mediator. After that, we discuss the implications of our <sup>fi</sup>ndings for both experimental design and empirical research in Sections 4.3 and 4.4.

## 4.1. Endogenous vs. Causal Mediation

EM and CM both have their advantages and disadvantages. The main advantage of CM over EM is that it supports both parametric and nonparametric identi-<sup>fi</sup>cation, whereas the latter only supports parametric identi<sup>fi</sup>cation. Researchers seeking nonparametric identi<sup>fi</sup>cation of a mediation process should use the nonparametric CM approach. Nevertheless, the nonparametric CM approach incorporates control variables through a strati<sup>fi</sup>cation approach (see section 3.2 of Imai et al. 2010b for details), which only supports discrete control variables and is hard to scale to many control variables. Without a practical way to control for observed confounders, the SIA assumption underlying the nonparametric CM approach is very hard to defend.

Table 6. Sensitivity of Model Estimates to Misspeci<sup>fi</sup>cation of Marginals of the First Stage

<table><tr><td rowspan="2">Model</td><td colspan="3">DGP: probit</td><td colspan="3">DGP: logit</td><td colspan="3">DGP: cloglog</td></tr><tr><td>probit</td><td>logit</td><td>cloglog</td><td>probit</td><td>logit</td><td>cloglog</td><td>probit</td><td>logit</td><td>cloglog</td></tr><tr><td colspan="10">Outcome</td></tr><tr><td>Intercept</td><td>1.000(0.086)</td><td>0.993(0.088)</td><td>1.011(0.087)</td><td>1.003(0.090)</td><td>1.001(0.090)</td><td>1.003(0.091)</td><td>0.993(0.102)</td><td>0.980(0.106)</td><td>1.003(0.099)</td></tr><tr><td>X</td><td>1.000(0.047)</td><td>0.997(0.047)</td><td>0.995(0.047)</td><td>0.998(0.049)</td><td>0.997(0.049)</td><td>0.990(0.050)</td><td>0.999(0.044)</td><td>0.997(0.044)</td><td>1.001(0.044)</td></tr><tr><td>M</td><td>1.001(0.106)</td><td>1.010(0.107)</td><td>0.992(0.106)</td><td>0.998(0.120)</td><td>1.001(0.120)</td><td>1.004(0.121)</td><td>1.008(0.114)</td><td>1.021(0.119)</td><td>0.997(0.111)</td></tr><tr><td>Z</td><td>0.999(0.029)</td><td>0.996(0.029)</td><td>0.993(0.029)</td><td>1.000(0.030)</td><td>1.000(0.030)</td><td>0.991(0.031)</td><td>1.000(0.027)</td><td>0.998(0.027)</td><td>1.002(0.026)</td></tr><tr><td colspan="10">Mediator</td></tr><tr><td>Intercept</td><td>1.003(0.053)</td><td>1.759(0.766)</td><td>0.547(0.455)</td><td>0.597(0.405)</td><td>1.006(0.078)</td><td>0.221(0.780)</td><td>1.519(0.523)</td><td>2.691(1.696)</td><td>1.006(0.058)</td></tr><tr><td>X</td><td>1.008(0.089)</td><td>1.812(0.828)</td><td>0.869(0.156)</td><td>0.572(0.433)</td><td>0.999(0.118)</td><td>0.500(0.504)</td><td>1.148(0.184)</td><td>2.092(1.112)</td><td>1.014(0.100)</td></tr><tr><td>Z</td><td>1.003(0.050)</td><td>1.795(0.800)</td><td>0.874(0.137)</td><td>0.575(0.426)</td><td>1.003(0.065)</td><td>0.504(0.497)</td><td>1.126(0.142)</td><td>2.036(1.043)</td><td>1.009(0.067)</td></tr><tr><td>Correlation</td><td>0.501(0.038)</td><td>0.497(0.039)</td><td>0.501(0.038)</td><td>0.501(0.042)</td><td>0.500(0.043)</td><td>0.497(0.043)</td><td>0.494(0.043)</td><td>0.485(0.046)</td><td>0.503(0.042)</td></tr></table>

Notes. The RMSEs are reported in parentheses. The true values are 1 for all coef<sup>fi</sup>cients and 0.5 for the rank correlation. The scales of parameter in the <sup>fi</sup>rst stage models are not identi<sup>fi</sup>ed. The <sup>fi</sup>rst stage estimates can be viewed as consistent if the ratio between any two coef<sup>fi</sup>cients is clos to one.

In practice, researchers conducting mediation analysis typically choose parametric identi<sup>fi</sup>cation because it allows them to easily control for many observed confounders. In such a case, EM is generally a better choice than CM. Whereas EM and CM both make functional assumptions on the generating processes of the mediator and the outcome, EM does not require the error terms in the two stages to be independent. As shown in Section 3.4.1, CM can lead to substantial bias when the SIA assumption is violated. Therefore, researchers looking for parametric identi<sup>fi</sup>cation are generally encouraged to use EM instead of CM for mediation analysis. Even if the SIA assumption holds, EM can still produce consistent estimates because it encapsulates CM as a special case as evident by the simulations in Section 3.4.1. In Online Appendix G2, we further show that CM and EM produce similar results when the SIA assumption is plausible using a public data set.

To be fair, EM can produce biased estimates if its parametric assumption on the dependence structure between the error terms is misspeci<sup>fi</sup>ed or the nonlinearity of the <sup>fi</sup>rst stage is weak (especially for binary mediators). However, as shown in Section 3.4.4, regardless of the actual dependence structure, the bias of EM is very small when we model the dependence structure with a Gaussian copula. The weak nonlinearity issue can be alleviated by adding control variables with large supports and/or strong effects on the mediator.

It should also be noted that EM is not identi<sup>fi</sup>ed without an instrument when the <sup>fi</sup>rst stage is linear. In this special circumstance, CM still works but generally produces biased estimates unless the SIA assumption is true. Nevertheless, the sensitivity analysis developed for this special case under the CM framework (Imai et al. 2010a, b) can be useful as it allows researchers to understand how the estimates vary with the correlation between the error terms.

## 4.2. Instrument- vs. Model-Based Identification

The empirical approaches to addressing the endogeneity issue can be broadly classi<sup>fi</sup>ed as instrumentand model-based. The instrument-based approach hinges on the availability of valid instruments. A valid instrument must satisfy two criteria: (i) it is correlated with the endogenous variable and (ii) it is uncorrelated with the error term in the outcome equation (i.e., exclusion restriction). The exclusion restriction is an assumption that cannot be empirically tested. Instead of relying on the availability of instruments, the model-based approach addresses endogeneity by making parametric assumptions on the DGP and is also known as identi<sup>fi</sup>cation by functional form. The instrument- and model-based identi<sup>fi</sup>cation strategies rely on fundamentally different assumptions and, hence, are complementary to each other. Researchers should consider both whenever possible. However, there are certain conditions when one strategy is more appealing than the other.

When there are well-justi<sup>fi</sup>ed instruments, the instrument-based approach is generally preferred as its consistency relies on fewer parametric assumptions. For example, when the outcome equation is linear, the standard estimation methods for the instrument-based approach, such as two-stage least squares and generalized method of moments, can provide consistent estimates without a parametric assumption on how the error terms for the endogenous variable and the outcome variable are correlated. Moreover, it is consistent even if the <sup>fi</sup>rst stage equation is misspeci<sup>fi</sup>ed though misspeci<sup>fi</sup>cation of the <sup>fi</sup>rst stage can reduce the ef<sup>fi</sup>- ciency of the estimates (i.e., increase the standard errors of the estimates). Nevertheless, the instrument-based approach can perform rather poorly when the instrument is weak or when the exclusion restriction is violated.

In the absence of plausible instruments, researchers should be very careful in using the instrument-based approach. In Section 3, we show that using an invalid instrument can be worse than simply ignoring the endogeneity. In this situation, the model-based approach can be more useful if the generating process for the endogenous variable is nonlinear. Whereas the model-based approach may suffer from misspeci<sup>fi</sup>cation bias when the parametric assumption on the DGP is incorrect, it is not tied to any speci<sup>fi</sup>c parametric assumption. Researchers are free to try different parametric assumptions and see if the model estimates remain consistent. Our sensitivity analysis suggests that misspecifying the dependence structure of the error terms as a Gaussian copula does not lead to signi<sup>fi</sup>cant bias, whereas misspecifying it as other copulas do. Moreover, in the case of a binary mediator, we <sup>fi</sup>nd that misspeci<sup>fi</sup>cation on the functional form of the <sup>fi</sup>rst stage does not result in noticeable bias. The bivariate normality assumption commonly used in two-stage models is a decent choice as the implied normality assumption on marginals is backed by the central limit theorem and the implied Gaussian copula is quite robust to misspeci<sup>fi</sup>cation.

In addition to the instrument- and model-based approaches, there also exists a hybrid approach that is a combination of the two when the generating process for the endogenous variable is nonlinear. This hybrid approach operates by <sup>fi</sup>tting a nonlinear model for the endogenous variable and then using the <sup>fi</sup>tted (predicted) values as an instrument for the endogenous variable (Angrist and Krueger 2001). We refer to this approach as the FittedIV approach. Compared with the model-based approach discussed in this paper, the FittedIV approach does not require any parametric assumption on how the error terms in the two stages are correlated. Whereas this approach sounds attractive, Angrist and Krueger (2001, p. 80) recommend against using it as it “does not generate consistent estimates unless the nonlinear model happens to be exactly right.” Wooldridge (2010) further argues that this approach may run into a multicollinearity issue because of the high correlation between the <sup>fi</sup>tted values and the variables used to predict the <sup>fi</sup>tted values. In Online Appendix H, we show that this FittedIV approach indeed suffers from the multicollinearity issue and is much more sensitive to the goodness of <sup>fi</sup>t of the <sup>fi</sup>rst stage than the model-based approach. Wooldridge (2010) suggests using this hybrid approach only when there is an instrument variable already. In such a case, using the <sup>fi</sup>tted instrument in place of the original instrument can produce more ef<sup>fi</sup>cient estimates at the cost of making an extra assumption on the functional form of the <sup>fi</sup>rst stage.

## 4.3. Implications for Experimental Design

Given that mediators are likely to be endogenous as posttreatment variables, countermeasures should be considered when designing an experiment. Although the literature on experimental mediation analysis is sparse, it is commonly believed that addressing the endogeneity of a mediator requires a separate manipulation for the mediator (Bullock et al. 2010, Pirlott and MacKinnon 2016). Two recently proposed experimental designs for mediation analysis are parallel design and parallel encouragement design, in which the mediator is manipulated in parallel with the treatment (Imai and Yamamoto 2013, Imai et al. 2013). The former design allows researchers to identify the mediation effect for all units but requires the manipulation of the mediator to be perfect (i.e., the mediator can be set to any level desired by the researcher, which is highly unrealistic). Conversely, the latter design allows the manipulation to be imperfect but can only identify the mediation effect for compliers (i.e., units whose mediator levels are affected by the manipulation). Both designs require the manipulation to satisfy the exclusion restriction. However, the exclusion restriction is untestable, and it is also dif<sup>fi</sup>cult to argue a priori that a stimulus used to in<sup>fl</sup>uence the mediator cannot possibly affect the outcome other than through the mediator.

Contrary to the current state of knowledge, our results suggest that, when the generating process of the mediator is nonlinear and explicitly modeled, (1) the manipulation for the mediator is recommended but not required for identi<sup>fi</sup>cation, (2) the manipulation need not satisfy the exclusion restriction or be perfect, and (3) the mediator need not be fully observed if it is binary or categorical. These novel insights have important implications for the design and analysis of experiments. In particular, any exogenous manipulation with a strong effect on the mediator can be helpful for the identi<sup>fi</sup>cation of an endogenous mediation process. When the exclusion restriction can be justi<sup>fi</sup>ed, the exogenous manipulation can be used as an instrument for instrumentbased identi<sup>fi</sup>cation. When the exclusion restriction is hard to justify, it can still be used to improve modelbased identi<sup>fi</sup>cation.

## 4.4. Implications for Empirical Research

Our research <sup>fi</sup>ndings have important implications for empirical researchers. First, modeling the DGP is essential to understand the mechanisms behind treatment effects even for experimental studies. When the direct and indirect mechanisms have opposite effects, the direction of the total treatment effect may be hard to generalize across contexts even if the mechanisms at work remain the same (see Online Appendix A for an example). This <sup>fi</sup>nding is consistent with the replication crisis in experimental studies (Open Science Collaboration 2015, Shrout and Rodgers 2018). To improve the external validity of experiments, researchers are urged to go beyond heterogeneous treatment effects and gain deeper insights into the underlying causal mechanisms through mediation analysis. An experiment should not be considered failed simply because the ATE is insignificant because an insigni<sup>fi</sup>cant ATE does not imply that the underlying causal mechanisms for direct and indirect effects are not in play.

Second, by proposing a set of novel models to deal with unobserved or partially observed binary mediators, which can be extended to accommodate categorical mediators, we show that it is possible to identify a mediation process without observing the mediator or any proxy of it. Nevertheless, an inherent limitation with latent mediation analysis is that it cannot pin down the exact mediator at work because the mediator of interest is not directly observed. Therefore, the interpretation of the results from latent mediation analysis can be somewhat arbitrary though the directional effects of the treatment on the mediator and the mediator on the outcome can help us understand the nature of the mediator. To pinpoint the mediator in play, an effective solution is to measure the mediator for a subset of units and reestimate the model, which can not only resolve the ambiguity in interpreting the mediation patterns, but can also greatly improve model identi<sup>fi</sup>cation.

Third, the recursive two-stage models presented in this paper are not limited to addressing the endogeneity of mediators. They can also be used to address the endogeneity of the treatment variables in both experimental and observational studies. For example, in certain circumstances, the treatment status of interest (e.g., whether one attends a job training program) cannot be randomized directly, and researchers can only implement manipulations that can in<sup>fl</sup>uence but not determine the treatment status (e.g., offering <sup>fi</sup>nancial incentive to encourage workers to attend the job training program). In such an encouragement design, the treatment status is endogenous because of a compliance issue, but we can use the two-stage models discussed in Section 2 to address the endogeneity of the treatment status. In observational studies, the two-stage models can also be applied if there exist exogenous control variables that are predictive of the treatment status. Whereas this requirement seems to be restrictive, it should be noted that control variables are often implicitly assumed to be exogenous in regression models, especially in nonlinear models. Online Appendix G3 illustrates how recursive two-stage models can be used to address the endogeneity of treatment variables in an observational data set.

Finally, the instrument- and model-based approaches to addressing endogeneity are complementary to each other. Given that they rely on fundamentally different assumptions and have different levels of ef<sup>fi</sup>ciency, researchers are recommended to consider both approaches whenever possible. If these two approaches produce consistent results (see Online Appendix G3 for an example), it gives us more con<sup>fi</sup>dence in the results as we only need the assumption underlying one identi-<sup>fi</sup>cation strategy to be reasonable (i.e., the instrument is valid, or the parametric assumption is not too far away from the true DGP). On the other hand, the discrepancy between these two approaches raises potential red <sup>fl</sup>ags about the robustness of the <sup>fi</sup>ndings.

## 5. Conclusion

In this paper, we introduce a much-needed methodological framework for researchers striving to identify causal mechanisms from experiments. In particular, we present a comprehensive endogenous mediation analysis framework that allows researchers to conduct practically desirable mediation analysis for different types of mediators, including unobserved or partially unobserved ones, without the stringent SIA assumption on mediators. We validate the effectiveness of the proposed endogenous mediation analysis framework using extensive simulations and sensitivity analyses as well as three applications on real-world data sets.

Our work makes the following contributions to the literature. First, built on extant literature on addressing endogeneity with two-stage models, we present a recursive two-stage mediation analysis framework without the SIA assumption, which can easily accommodate different types of endogenous mediators for different types of outcomes under <sup>fl</sup>exible parametric assumptions. Second, we propose a set of novel latent mediation models for unobserved or partially observed endogenous binary mediators, which can be further extended to handle endogenous categorical mediators. Third, we investigate the identi<sup>fi</sup>cation conditions of endogenous mediation analysis for different types of mediators and shed light on some previously less known or unknown identi<sup>fi</sup>cation conditions for endogeneity. Fourth, we thoroughly examine the sensitivity of model estimates to a series of factors, including the correlation in error terms, the goodness of <sup>fi</sup>t of the mediator model, the percentage of observed mediator values, and the misspeci<sup>fi</sup>cation of copulas and marginals for the error terms, which provides important insights into when and how to use endogenous mediation analysis. Finally, we provide detailed guidelines on when to use endogenous versus causal mediation analysis and lengthy discussions on the implications of our work for both experimental design and empirical research.

Our work can be extended in several directions. Because the inclusion of endogenous control variables can lead to bias in nonlinear models, we focus on improving model identi<sup>fi</sup>cation with exogenous control variables. For experimental researchers, this is not too much hassle as exogenous control variables can be easily obtained by implementing additional manipulations that can in<sup>fl</sup>uence the mediator. However, for empirical researchers working on observational data, exogenous control variables are not always available. Future research could explore the conditions under which the exogeneity of controls can be relaxed, especially when the outcome equation is linear because linear models are known to be more robust to the inclusion of endogenous controls than nonlinear models. Moreover, the endogenous mediation analysis framework can be extended to incorporate multiple mediators and outcomes. For example, the multivariate probit model can be used to model multiple binary mediators and outcomes. Similarly, the multivariate Poisson lognormal model can be used to model multiple count mediators and outcomes (Aitchison and Ho 1989). More <sup>fl</sup>exible combinations for different types of mediators and outcomes are also possible (e.g., Filippou et al. 2019). However, the identi<sup>fi</sup>cation conditions of such models may be complicated. Finally, future research can investigate why the endogenous mediation model for a binary mediator is robust to the misspeci<sup>fi</sup>cation of the functional form of the <sup>fi</sup>rst stage and whether this <sup>fi</sup>nding extends to other types of mediators.

## Acknowledgments

The author thanks the senior editor, the associate editor, and three anonymous reviewers for their constructive comments throughout the review process.

## Endnotes

<sup>1</sup> If there is more than one mediator, researchers often focus on a mediator of theoretical or practical interest. In that case, the direct effect represents the part of the treatment effect that cannot be explained by the focal mediator.

<sup>2</sup> Online Appendix A provides a mediation process in which simply changing the baseline distribution of the mediator can change the direction of the total effect.

<sup>3</sup> In the nonparametric approach, all control variables need to be integrated out based on their empirical distributions. When there are many control variables, it is difficult to estimate the joint empirical distribution of control variables reliably, especially when some control variables are continuous. As a workaround, Imai et al (2010b, section 4.2) propose to estimate the direct and indirect effects independently within each stratum of control variables Nevertheless, this workaround does not scale well as the number o observations per stratum decreases exponentially with the number of control variables.

<sup>4</sup> If the direct and indirect effects vary with treatment status, we can add an interaction term between the treatment and the mediator in the outcome equation.

In copula modeling, we typically use rank correlations (e.g., Ken dall’s tau) to measure the correlation of two random variables Unlike the usual Pearson correlation, rank correlations are invariant to strictly increasing nonlinear transformations. We use Kendall’s tau to measure rank correlation in this paper.

<sup>6</sup> We use the copula and GJRM packages for the simulations in Sections 3.4.4 and 3.4.5. These two packages are available at https:// CRAN.R-project.org/package=copula and https://CRAN.R-project org/package=GJRM. All other simulations rely on the endogeneity package that is available at https://CRAN.R-project.org/package =endogeneity.

## References

Aitchison J, Ho CH (1989) The multivariate Poisson-log normal distribution. Biometrika 76(4):643–653.

Albert JM, Geng C, Nelson S (2016) Causal mediation analysis with a latent mediator. Biometrical J. 58(3):535–548.

Anderson ET, Simester DI (2003) Effects of \$9 price endings on retail sales: Evidence from <sup>fi</sup>eld experiments. Quant. Marketing Econom. 1(1):93–110.

Angrist JD, Krueger AB (2001) Instrumental variables and the search for identi<sup>fi</sup>cation: From supply and demand to natural experiments. J. Econom. Perspect. 15(4):69–85.

Aral S, Walker D (2011) Creating social contagion through viral product design: A randomized trial of peer in<sup>fl</sup>uence in networks. Management Sci. 57(9):1623–1639.

Awad NF, Krishnan MS (2006) The personalization privacy paradox: An empirical evaluation of information transparency and the willingness to be pro<sup>fi</sup>led online for personalization. Man agement Inform. Systems Quart. 30(1):13–28.

Bapna R, Qiu L, Rice S (2017) Repeated interactions vs. social ties: Quantifying the economic value of trust, forgiveness, and reputation using a <sup>fi</sup>eld experiment. Management Inform. Systems Quart. 41(3):841–866.

Bapna R, Ramaprasad J, Shmueli G, Umyarov A (2016) One-way mirrors in online dating: A randomized <sup>fi</sup>eld experiment. Man agement Sci. 62(11):3100–3122.

Baron RM, Kenny DA (1986) The moderator-mediator variable distinction in social psychological research: Conceptual, strategic, and statistical considerations. J. Personality Soc. Psych. 51(6):1173–1182.

Bound J, Brown C, Mathiowetz N (2001) Measurement error in survey data. Heckman JJ, Leamer E, eds. Handbook of Econometrics (North-Holland, Amsterdam), 3705–3843.

Bullock JG, Green DP, Ha SE (2010) Yes, but what’s the mechanism? (Don’t expect an easy answer). J. Personality Soc. Psych. 98(4): 550–558.

Carrasco R (2001) Binary choice with binary endogenous regressors in panel data: Estimating the effect of fertility on female labor participation. J. Bus. Econom. Statist. 19(4):385–394.

Dempster APP, Laird NM, Rubin DB (1977) Maximum likelihood from incomplete data via the EM algorithm. J. Roy. Statist. Soc. B 39(1):1–38.

d’Haultfoeuille X (2010) A new instrumental method for dealing with endogenous selection. J. Econometrics 154(1):1–15.

Dong Y, Lewbel A (2015) A simple estimator for binary choice models with endogenous regressors. Econometric Rev. 34(1–2):82– 105.

Filippou P, Kneib T, Marra G, Radice R (2019) A trivariate additive regression model with arbitrary link functions and varying correlation matrix. J. Statist. Planning Inference 199:236–248.

Frandsen BR (2015) Treatment effects with censoring and endogeneity. J. Amer. Statist. Assoc. 110(512):1745–1752.

Greene WH (2009) Models for count data with endogenous partici pation. Empirical Econom. 36(1):133–173.

Greene WH (2012) Econometric Analysis, 7th ed. (Pearson, Boston).

Hayes AF (2017) Introduction to Mediation, Moderation, and Conditional Process Analysis, Second Edition: A Regression-Based Approach (The Guilford Press, New York-London).

Heckman JJ (1978) Dummy endogenous variables in a simultaneous equation system. Econometrica 46(4):931–959.

Heckman JJ (1979) Sample selection bias as a speci<sup>fi</sup>cation error. Econometrica 47(1):153–161.

Imai K, Yamamoto T (2013) Identi<sup>fi</sup>cation and sensitivity analysis for multiple causal mechanisms: Revisiting evidence from fram ing experiments. Political Anal. 21(2):141–171.

Imai K, Keele L, Tingley D (2010a) A general approach to causal mediation analysis. Psych. Methods 15(4):309–334.

Imai K, Keele L, Yamamoto T (2010b) Identi<sup>fi</sup>cation, inference and sensitivity analysis for causal mediation effects. Statist. Sci. 25(1):51–71.

Imai K, Tingley D, Yamamoto T (2013) Experimental designs for iden tifying causal mechanisms. J. Roy. Statist. Soc. Ser. A 176(1):5–51.

Jung J, Bapna R, Golden J, Sun T (2020) Words matter! Toward prosocial call-to-action for online referral: Evidence from two <sup>fi</sup>eld experiments. Inform. Systems Res. 31(1):16–36.

Klein N, Kneib T, Marra G, Radice R, Rokicki S, McGovern ME (2019) Mixed binary-continuous copula regression models with application to adverse birth outcomes. Statist. Medicine 38(3):413–436.

Kumar A, Hosanagar K (2019) Measuring the value of recom mendation links on product demand. Inform. Systems Res. 30(3):819–838.

Lee D, Hosanagar K (2021) How do product attributes and reviews moderate the impact of recommender systems through pur chase stages? Management Sci. 67(1):524–546.

Lewbel A (2007) Endogenous selection or treatment model estimation. J. Econometrics 141(2):777–806.

Li C, Poskitt DS, Zhao X (2019) The bivariate probit model, maximum likelihood estimation, pseudo true parameters and partial identi<sup>fi</sup>cation. J. Econometrics 209(1):94–113.

Lu Y, Gupta A, Ketter W, Van Heck E (2019) Information transparency in business-to-business auction markets: The role of win ner identity disclosure. Management Sci. 65(9):4261–4279.

Murphy KM, Topel RH (1985) Estimation and inference in two-step econometric models. J. Bus. Econom. Statist. 3(4):370–379.

Muthen B, Asparouhov T (2015) Causal effects in mediation model- ´ ing: An introduction with applications to latent variables. Structural Equation Model. 22(1):12–23.

Nelsen RB (2007) An Introduction to Copulas (Springer Science & Business Media)

Nizalova OY, Murtazashvili I (2016) Exogenous treatment and endogenous factors: Vanishing of omitted variable bias on the interaction term. J. Econom. Methods 5(1):71–77.

Open Science Collaboration (2015) Estimating the reproducibility of psychological science. Sci. 349(6251):aac4716.

Pearl J (2014) Interpretation and identi<sup>fi</sup>cation of causal mediation Psych. Methods 19(4):459–481.

Pirlott AG, MacKinnon DP (2016) Design approaches to experimental mediation. J. Experiment. Soc. Psych. 66:29–38.

Puhani PA (2000) The Heckman correction for sample selection and its critique. J. Econom. Surveys. 14(1):53–68.

Qiu L, Kumar S (2017) Understanding voluntary knowledge provision and content contribution through a social-media-based prediction market: A <sup>fi</sup>eld experiment. Inform. Systems Res. 28(3):529–546.

Rivers D, Vuong QH (1988) Limited information estimators and exogeneity tests for simultaneous probit models. J. Econometrics 39(3):347–366.

Shrout PE, Rodgers JL (2018) Psychology, science, and knowledge construction: Broadening perspectives from the replication crisis. Annual Rev. Psych. 69(1):487–510.

Sklar M (1959) Fonctions de repartition an dimensions et leurs marges Publications de l’Institut Statistique de l’Universite de Paris´ 8:229–231.

Stock JH (2010) The other transformation in econometric practice: Robust tools for inference. J. Econom. Perspect. 24(2):83–94.

Sun T, Viswanathan S, Zheleva E (2021) Creating social contagion through <sup>fi</sup>rm mediated message design: Evidence from a randomized <sup>fi</sup>eld experiment. Management Sci. 67(2):808–827.

Tingley D, Yamamoto T, Hirose K, Keele L, Imai K (2014) Mediation: R package for causal mediation analysis. J. Statist. Software 59(5):1–38.

Trivedi PK, Zimmer DM (2007) Copula Modeling: An Introduction for Practitioners (Now Publishers Inc., Boston-Delft).

Wooldridge JM (2010) Econometric Analysis of Cross Section and Panel Data (MIT Press, Cambridge-London).

Zhang Y, Li B, Luo X, Wang X (2019) Personalized mobile targeting with user engagement stages: Combining a structural hidden Markov model and <sup>fi</sup>eld experiment. Inform. Systems Res. 30(3): 787–804.

C<sub>opy</sub>ri<sub>g</sub>ht 2023 b<sub>y</sub> INFORMS <sub>a</sub>ll ri<sub>g</sub>ht<sub>s</sub> r<sub>ese</sub>r<sub>ve</sub>d<sub>.</sub> C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e</sub> <sub>p</sub>r<sub>ope</sub>rt<sub>y</sub> <sub>o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pe</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h <sub>a</sub>nd it<sub>s</sub> <sub>co</sub>nt<sub>e</sub>nt m<sub>ay</sub> <sub>no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or ema</sub>il<sub>e</sub>d t<sub>o mu</sub>lti<sub>p</sub>l<sub>e s</sub>it<sub>es or pos</sub>t<sub>e</sub>d t<sub>o a</sub> li<sub>s</sub>t<sub>serv w</sub>ith<sub>ou</sub>t th<sub>e copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup><sub>s</sub> <sub>expres s</sub> <sub>wr</sub>itt<sub>en</sub> <sub>perm</sub>i<sub>s s</sub>i<sub>on.</sub> H<sub>owever</sub> <sub>users</sub> <sub>may</sub> <sub>pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or</sub> <sub>ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use</sub>
