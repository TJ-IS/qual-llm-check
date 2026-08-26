---
otero_id: 2180
otero_key: "N5N9CAQA"
title: "Research Note—Partial Least Squares and Models with Formatively Specified Endogenous Constructs: A Cautionary Note"
authors: "Miguel I. Aguirre-Urreta; George M. Marakas"
year: "2014"
journal: "Information Systems Research"
doi: "10.1287/isre.2013.0493"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HR

![](/api/attachments/N5N9CAQA/fulltext/images/6b8edcc8d4ef22a33b5439f553899787b05236f6e9888740cc3329127d6204bc.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Research Note—Partial Least Squares and Models with Formatively Specified Endogenous Constructs: A Cautionary Note

Miguel Aguirre-Urreta, George Marakas

To cite this article:

Miguel Aguirre-Urreta, George Marakas (2013) Research Note—Partial Least Squares and Models with Formatively Specified Endogenous Constructs: A Cautionary Note. Information Systems Research

Published online in Articles in Advance 05 Sep 2013

http://dx.doi.org/10.1287/isre.2013.0493

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2013, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/N5N9CAQA/fulltext/images/b2221ce20daa697edd833750fda1671d4cbe1ef2d49937b732146058918a661e.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Research Note

# Partial Least Squares and Models with Formatively Specified Endogenous Constructs: A Cautionary Note

Miguel Aguirre-Urreta

School of Accountancy and Management Information Systems, DePaul University, Chicago, Illinois 60604, maguirr6@depaul.edu

George Marakas

College of Business Administration, Florida International University, Miami, Florida 33199, gmarakas@fiu.edu

nformation systems researchers have recently begun to propose models that include formatively specified Iconstructs, and largely rely on partial least squares (PLS) to estimate the parameters of interest in those models. In this research, we focus on those cases where the formatively specified constructs are endogenous to other constructs in the research model in addition to their own manifest indicators, which are quite common in published research in the discipline, and analyze whether PLS is a valid statistical technique for estimating those models. Although there is evidence that covariance-based approaches can accurately estimate them, this is the first research that examines whether PLS can indeed do so. Through a theoretical analysis based on the inner workings of the PLS algorithm, which is later validated and extended through a series of Monte Carlo simulations, we conclude that is not the case. Specifically, estimates obtained from PLS are capturing something other than the relationship of interest when the formatively specified constructs are endogenous to others in the model. We show how our results apply more generally to a class of models, and discuss implications for future research practice.

Key words: formative specification; partial least squares; research methods; structural equation modeling History: Vijay Mookerjee, Senior Editor; Sunil Mithas, Associate Editor. This paper was received on July 13, 2011, and was with the authors for 7 months for 2 revisions. Published online in Articles in Advance.

## Introduction

Though theoretical development and resulting theories are generally couched in terms of unobservable constructs that influence each other, empirical testing of those requires the collection of data and the specification of a model that relates the collected data to the unobservable constructs researchers believe those data represent. In the past, this relationship between unobservable construct and manifest indicators would have been conceptualized as what we now call reflective, that is, where the direction of causality flows from the unobservable construct to the manifest indicators. In a reflective specification, changes in the unobservable construct are presumed to cause<sup>1</sup> changes in the manifest indicators. An alternative way of specifying this relationship, in a formative manner, shows the unobservable construct as a consequence of the manifest indicators, reversing the direction of causality. In this case, changes in the manifest indicators are presumed to cause changes in the unobservable construct (for a complete discussion of the differences between the two approaches see Bollen and Lennox 1991). These two approaches to setting the relationship between the unobservable constructs used in our theories and the manifest indicators used to collect data differ greatly in both their interpretation and how models including each are specified and estimated.

Although some of the work dates from earlier (Bollen 1984, Bollen and Lennox 1991, Cohen et al. 1990, Curtis and Jackson 1962), this distinction was brought to the attention of the organizational and social science research communities by the research of Diamantopoulos and Winklhofer (2001) and Jarvis and colleagues (Jarvis et al. 2003, MacKenzie et al. 2005). Special issues on the topic also appeared in Psychological Methods (volume 12, issue 2, 2007) and the Journal of Business Research (volume 61, issue 12, 2008). Within the IS discipline proper, work by Petter

Table 1 Recent Research Involving First-Order Formative Constructs

<table><tr><td>Article</td><td>Sample size</td><td>Structural position</td><td>Technique</td></tr><tr><td>Chengalur-Smith et al. (2010)</td><td>149</td><td>Endogenous only</td><td>PLS</td></tr><tr><td>Iacovou et al. (2009)</td><td>561</td><td>Endogenous only</td><td>PLS</td></tr><tr><td>Kim and Benbasat (2010)</td><td>128</td><td>Endogenous only</td><td>PLS, ANOVA</td></tr><tr><td>Klein and Rai (2009)</td><td>91</td><td>Endogenous only</td><td>PLS</td></tr><tr><td>Lee and Xia (2010)</td><td>505</td><td>Endogenous only</td><td>PLS</td></tr><tr><td>Liang et al. (2007)</td><td>77</td><td>Endogenous only</td><td>PLS</td></tr><tr><td>Limayen et al. (2007)</td><td>227</td><td>Endogenous only</td><td>PLS</td></tr><tr><td>Rai et al. (2009)</td><td>166</td><td>Endogenous only</td><td>PLS</td></tr><tr><td>Sia et al. (2009)</td><td>166,128</td><td>Endogenous only</td><td>PLS</td></tr><tr><td>Venkatesh and Ramesh (2006)</td><td>201,169,766</td><td>Endogenous only</td><td>PLS</td></tr><tr><td>Yi and Davis (2003)</td><td>95</td><td>Endogenous only</td><td>PLS</td></tr><tr><td>Choi et al. (2010)</td><td>743</td><td>Exogenous and endogenous</td><td>PLS</td></tr><tr><td>Lowry et al. (2009)</td><td>346</td><td>Exogenous and endogenous</td><td>PLS</td></tr><tr><td>Malhotra et al. (2007)</td><td>41</td><td>Exogenous and endogenous</td><td>PLS</td></tr><tr><td>Pee et al. (2010)</td><td>95</td><td>Exogenous and endogenous</td><td>PLS</td></tr><tr><td>Zhu et al. (2006)</td><td>1,394</td><td>Exogenous and endogenous</td><td>PLS</td></tr></table>

Notes. Sample size indicates the number of subjects included in the research; values separated by commas indicate multiple studies or samples. Structural position indicates whether formatively specified variables were included in research models only as endogenous (to other constructs beyond its observed formative indicators) variables, or whether research models included formatively-specified constructs in both endogenous and exogenous positions.

et al. (2007), Cenfetelli and Bassellier (2009) and Kim et al. (2010) has examined various aspects of the formative approach to construct specification. In recent years, as shown in Table 1, there has been a growth in the usage of formatively specified constructs in IS research. To the extent that the usage of this alternative specification mode better corresponds to the underlying structure of the models researchers are interested in estimating, this is clearly an important development. Though the distinction between formative and reflective specifications is conceptually straightforward, statistical issues have proven to be more complex. Before moving forward, we would be remiss not to acknowledge that there are researchers who are very critical of formative measurement practices in general and have outright called for their abandonment (Edwards 2011). If this outlook were to prevail, it would be conceivable that formative measurement would eventually not be employed anymore in the management and social sciences—including IS research—in the future. At the same time, there are others who have advocated for the use of formative measurement as well, many of which have been cited above, and thus the issue does not seem close to being settled. Although this discussion is beyond the scope of the current work, we focus on the validity of one particular approach to the estimation of research models that does include formatively specified constructs. In particular, we examine the adequacy of using PLS to analyze one specific—though quite common in IS research, as discussed below—scenario, where formatively specified endogenous constructs are included in a research model. As a result, our concern here is with the validity of one statistical modeling approach for analyzing one particular usage of formative measurement.

Table 1 shows a comprehensive survey of all studies including one or more formatively specified first order constructs in their research models that appeared in the 2006–2010 period in MIS Quarterly, Information Systems Research, the Journal of Management Information Systems, or the Journal of the Association for Information Systems and which employed PLS as the statistical technique of choice. In this short period of time, 16 studies were published that included formatively specified first order constructs in either an exogenous<sup>2</sup> or endogenous position, which we believe reflects the strong interest that IS researchers have displayed in this methodological development. Only three other studies including formatively specified first order constructs in the research models, but that did not employ PLS, were identified. One possible explanation for this observation is that the usage of covariance-based approaches when formatively specified endogenous constructs are employed requires researchers to engage in complex identification issues, whereas PLS is not concerned with those (Petter et al. 2007). Indeed, it has been argued that PLS is a valid alternative for modeling this type of specifications (Chin 1998, Petter et al. 2007), and it is also the case that some aspects of the PLS algorithm (i.e., mode B estimation) resemble a formative specification. However, to the best of our knowledge, there is no research that has examined whether it is indeed the case that PLS is a valid alternative when formatively specified endogenous constructs are included in a research model, as is the case in every single study included in Table 1. Although there is evidence that, when correctly specified, covariancebased approaches can accurately model these (see, for instance, Correctly Specified Model 2 in Petter et al. 2007 and Jarvis et al. 2003), the same kind of evidence is lacking for PLS.

In this research we examine this issue by first conducting a theoretical analysis based on how the PLS algorithm, as is used by researchers in practice, would model these kinds of scenarios. This analysis is later validated and extended with a series of Monte Carlo simulations. Through these, we show that PLS should not be considered a valid approach to the estimation of this kind of model. In particular, our analysis reveals that estimates are capturing something other than the relationship of interest. We also show how our findings can be extended to more complex models, and discuss their implications for research practice and evaluation of published work.

## Research Model and Model Decomposition

To better ground our discussion of this issue we will employ the model shown in Figure 1 throughout this research. This model is useful in that it captures the essential features of the problem at hand without adding unnecessary complexity to our examples. Later in this research we show that our results apply to similar but more complex models, such as those with more than one predictor emitting a path to a formatively specified endogenous construct, or those with different values for the parameters included in the model.

The model shown in Figure 1 includes an exogenous latent variable () specified as reflective and measured by four indicators in an essentially congeneric (Little et al. 2006) manner. This exogenous latent variable emits a single path $( \gamma _ { 4 } )$ into a formatively specified endogenous latent variable $( \eta _ { 1 } )$ —this is the main relationship of interest here. This endogenous latent variable is also defined by three other formative indicators $( x _ { 1 } , x _ { 2 } ,$ , and $x _ { 3 } )$ that are correlated among themselves, and an uncorrelated disturbance term $( \zeta _ { 1 } )$ that represents unmeasured causes and/or “random shoc $\mathrm { \ k s ^ { \prime \prime } }$ (James et al. 1983) that influence this latent variable. Two paths are emitted into two other reflectively specified and essentially congeneric latent variables $( \eta _ { 2 }$ and $\eta _ { 3 } )$ , each measured by four indicators. The major issue under examination here is the extent to which PLS can accurately estimate the parameter relating the exogenous latent variable to the formatively specified endogenous one; that is, accuracy in the estimation of $\gamma _ { 4 }$ in Figure 1. For this purpose, the relevant functional equations that can be deduced from the model in Figure 1 are the following (throughout this research we express variables as deviations from their means without loss of generality, as intercepts do not play a role in any of these issues):

$$
\eta_ {1} = \gamma_ {1} x _ {1} + \gamma_ {2} x _ {2} + \gamma_ {3} x _ {3} + \gamma_ {4} \xi + \zeta_ {1},
$$

$$
y _ {i} = \lambda_ {i} \xi + \theta_ {i}, i = 1, 2, 3, 4.\tag{1}
$$

(2)

After collecting data on the 15 observed variables shown in Figure 1, researchers who have chosen PLS to conduct their analysis would then specify their model in the following manner—to be specific about how PLS would be used in this instance, we have included a screenshot of how this model would be analyzed using PLS-Graph 3.0 (Chin 1993). See Figure 2.<sup>3</sup>

Figure 1 Population Model  
![](/api/attachments/N5N9CAQA/fulltext/images/1bc58252009bf504c00847d3ce31e73c5e7eeab10e50d3d40bbccc363458f2c2.jpg)

Figure 2 Screenshot of Model Specification in PLS-Graph 3.0  
![](/api/attachments/N5N9CAQA/fulltext/images/a389a585d29615eef65c16148ed34e51ba921fc8e9eed296cab08e4fcb0c4aad.jpg)

## Overview of the PLS Algorithm

The PLS algorithm essentially entails the generation of estimates for three different sets of parameters in a model: (1) the block structure (also referred to as the outer relations), which relates indicators to composite variables and produces a loading for each indicator, (2) the inner or structural relations, which specify path coefficients between the presumed latent variables, according to the theoretical model proposed by the investigator, and (3) weight relations, which help provide explicit estimates (i.e., scores) for each composite variable, as a weighted aggregate of its indicators. In all cases both latent and manifest variables are scaled to zero means and unit variances in order to eliminate constant terms from the equations. For both the outer and inner relations, PLS incorporates the assumption of predictor specification, such that both indicators and composite variables are conditionally independent based on their predictors (Wold 1982). PLS arrives at estimates for these parameters by means of an iterative multistage procedure.

In the first stage, an iterative procedure is used to obtain explicit estimates of the latent variables through a weighted combination of their indicators. This is accomplished by iteratively calculating weights and estimates of weighted composites for each latent variable until a convergence criterion is reached. There are two distinct procedures used to calculate estimates for the weights in each iteration, depending on whether these are obtained by either single (inward-directed, or mode A) or multiple (outward-directed, or Mode B) regression, using the prior estimate of the latent variable as an instrumental variable. This first half of the iterative scheme is called the outside approximation. After a score has been obtained for each of the composite variables, these are refined through different weighting approaches (such as the centroid, factor, and path schemes described by Lohmöller 1989) based on the composite variables that are adjacent (that is, directly related through path coefficients) in the structural or inner relations. The process iterates back and forth until the convergence criterion is achieved. The reason the technique is called partial is because it only takes into consideration adjacent variables when refining the estimates and not the model as a whole. This part of the iteration is referred to as the inside approximation.

Thus, the algorithm starts by calculating an estimate for the latent variable, such that $Y = { \overline { { f } } } \Sigma ( w _ { i } * x _ { i } )$ where $f$ is a scalar that gives the estimate unit variance, $w _ { i }$ is the set of weight estimates, and $x _ { i }$ is the set of indicators for the latent variable, measured as deviations from their means. The very first estimate is rather arbitrary, but rapidly improves in the first few iterations. This first estimate is then improved through the inside approximation process described above. In the next step, using the estimate for each composite variable just obtained, a new set of indicator weights is derived; if using mode A through solving for the set of weights $w _ { i }$ in the formula $x _ { i } = w _ { i } Y +$ $e _ { i } ;$ if using mode B for the particular estimate, through solving for $w _ { i }$ in the formula $\begin{array} { r } { Y = \sum ( w _ { i } x _ { i } + e _ { i } ) } \end{array}$

Having thus obtained a new set of weights, the algorithm iterates by obtaining a rescaled estimate of the latent variable $\dot { Y }$ by using the formula presented in the prior paragraph, and going through another round of inside approximations. After iteration stops because of a lack of change in subsequent weight estimates, the PLS algorithm has produced an estimate for each latent variable in the model as a weighted aggregate of each indicator in its block structure, which is then fed into the next stage of the process. Using these estimates, the second stage entails estimating the final path coefficients between latent variables adjacent in the theoretical model by simple ordinary least squares (OLS) regression between the weighted components obtained in the first stage, and the calculation of the estimated block structure (e.g., loadings) by regressing each indicator on the composite variable estimate for its corresponding block. The third and last stage of PLS removes the standardization imposed above and estimates means and location parameters for both manifest and composite variables.

## Formative Specifications in PLS

In this particular case, the following expressions are of importance. Using the subscript c to indicate that we are referring to the corresponding weighted composites, the two latent variables of interest would be represented in PLS as follows, where $w _ { i }$ and $k _ { i }$ are the two sets of iteratively obtained weights used in the creation of the composites:

$$
\xi_ {c} = w _ {1} y _ {1} + w _ {2} y _ {2} + w _ {3} y _ {3} + w _ {4} y _ {4},\tag{3}
$$

$$
\eta_ {1 c} = k _ {1} x _ {1} + k _ {2} x _ {2} + k _ {3} x _ {3}.\tag{4}
$$

Equations (3) and (4), then, show how PLS creates the composites that are used in place of the constructs of interest, as weighted aggregates of the observed indicators directly attached to each. A comparison between (1), which shows the determinants of the formatively specified endogenous construct with (4), which shows how PLS forms the composite that stands in for that construct in the PLS models, provides evidence of an issue with how endogenous formatively specified constructs are represented in PLS, which we expand upon in more detail below: in the composite formed by PLS—which is a weighted sum of the manifest formative indicators—there is nothing of the predictor variable included in the formulation. As a result, there is no shared variance between the two composites, that is, because of the relationship of interest, which leads us to question the results that are obtained from PLS when such a model is estimated. After forming the composites shown in (3) and (4), the estimate of the relationship between the two constructs of interest is obtained by estimating an OLS regression between the two composites that represent those constructs in the PLS model, as shown in (5), where $\eta _ { 1 c }$ is the composite representing the formatively specified latent variable, $\xi _ { c }$ is the composite representing the latent predictor, $g$ is the OLS regression estimate of the relationship between the two composites, and e is the residual term:

$$
\eta_ {1 c} = g \xi_ {c} + e.\tag{5}
$$

By replacing (3) and (4) into (5), we obtain the following:

$$
\begin{array}{r l} & k _ {1} x _ {1} + k _ {2} x _ {2} + k _ {3} x _ {3} \\ & \qquad = g (w _ {1} y _ {1} + w _ {2} y _ {2} + w _ {3} y _ {3} + w _ {4} y _ {4}) + e. \end{array}\tag{6}
$$

Equation (1) states that a formatively specified latent variable is a function of its manifest indicators, a latent predictor, and a disturbance term. Equation (6)—which is the equation estimated by PLS when modeling this relationship, on the other hand, states that the formative indicators of that same latent variable are a function of the reflective indicators of the latent predictor. Thus we go from (1), where formative indicators and the latent predictor are all different causes of the formatively specified endogenous variable, to the scenario in (6), where some of those causes—the manifest formative indicators—are a function of manifest indicators representing another of the causal influences shown in (1). We believe these are fundamentally different scenarios, and taking an estimate obtained from the model shown in (6) to be a valid estimate for a parameter in (1) raises a host of issues around that estimate, which we discuss in more detail next.

In this particular case, there being a single independent variable, the relationship between $\xi _ { c }$ and $\eta _ { 1 c }$ equals the correlation between the two composites. As we discuss later, however, our results apply equally to other, more complex relationships with multiple predictors. The correlation between the two composites equals their covariance divided by the product of their respective standard deviations, as shown in (7):

$$
g = \frac {\operatorname{Cov} (\xi_ {c} , \eta_ {1 c})}{\sqrt {\operatorname{Var} (\xi_ {c})} \sqrt {\operatorname{Var} (\eta_ {1 c})}}.\tag{7}
$$

For reasons that will become evident shortly, it is safe here to ignore the denominator. Expanding the expression for the covariance in the numerator in (7) yields the following:

$$
\begin{array}{r} \mathrm{Cov} (\xi_ {c}, \eta_ {1 c}) = \mathrm{Cov} \big (w _ {1} y _ {1} + w _ {2} y _ {2} + w _ {3} y _ {3} + w _ {4} y _ {4}, \\ k _ {1} x _ {1} + k _ {2} x _ {2} + k _ {3} x _ {3} \big). \end{array}\tag{8}
$$

Fully decomposing the covariance in (8) with the help of the equivalences included in Appendix $\mathrm { A } ^ { 4 }$ results in the following expression:

$$
\begin{array}{r l} \mathrm{Cov} (\xi_ {c}, \eta_ {1 c}) = & w _ {1} k _ {1} \mathrm{Cov} (y _ {1}, x _ {1}) + w _ {1} k _ {2} \mathrm{Cov} (y _ {1}, x _ {2}) \\ & + w _ {1} k _ {3} \mathrm{Cov} (y _ {1}, x _ {3}) + w _ {2} k _ {1} \mathrm{Cov} (y _ {2}, x _ {1}) \\ & + w _ {2} k _ {2} \mathrm{Cov} (y _ {2}, x _ {2}) + w _ {2} k _ {3} \mathrm{Cov} (y _ {2}, x _ {3}) \\ & + w _ {3} k _ {1} \mathrm{Cov} (y _ {3}, x _ {1}) + w _ {3} k _ {2} \mathrm{Cov} (y _ {3}, x _ {2}) \\ & + w _ {3} k _ {3} \mathrm{Cov} (y _ {3}, x _ {3}) + w _ {4} k _ {1} \mathrm{Cov} (y _ {4}, x _ {1}) \\ & + w _ {4} k _ {2} \mathrm{Cov} (y _ {4}, x _ {2}) + w _ {4} k _ {3} \mathrm{Cov} (y _ {4}, x _ {3}). \end{array}\tag{9}
$$

The key observation here is that, in the population model shown in Figure 1 and from where collected data would come from, all these covariances equal zero. Therefore, regardless of the true population value of $\gamma _ { 4 } ,$ any estimates of this coefficient obtained from estimating the model shown in Figure 1 using PLS (as shown in Figure 2) will indicate a lack of any relationship between the two constructs of interest. Clearly, this is not what researchers observe in practice. When samples are collected from a population that has the structure represented in Figure 1, estimates different from zero will be obtained for the coefficient of interest. However, those estimates will be due solely to the variability present in the sampling process, such that the covariances shown in (9) will differ from zero randomly in each particular sample, but will have no necessary relationship with the true population value of the coefficient. On average, estimates obtained for the model shown in Figure 1 from PLS will equal zero, regardless of the underlying population value of the path coefficient of interest.

## Monte Carlo Simulations

This is clearly a surprising result. To validate our findings through alternative means, we generated simulated data from the model in Figure 1 under three different scenarios, with standardized population values for $\gamma _ { 4 }$ of 0, 0.30, and 0.50, and repeatedly analyzed those samples in PLS-Graph 3.0 (Chin 1993) with the model specification shown in Figure 2. Covariance matrices for these simulations are included in Appendix B in order to facilitate replication of our results. Full details of these simulations are as follows:

1. All variables shown in Figure 1, both latent and observed, are standardized to zero means and standard deviations equal to one, and drawn from a multivariate normal distribution.

2. All loadings for reflective indicators were set at 0.80, with their residual variances representing 36% of the total variance of each indicator. These values have been defined in order to generate data but have no effect on our results.

3. The disturbance term $\zeta _ { 1 }$ represents 5% of the total variance in $\eta _ { 1 }$ . The paths $\beta _ { 1 }$ and $\beta _ { 2 }$ were fixed at 0.50 and 0.60, respectively. Disturbance terms $\zeta _ { 2 }$ and $\zeta _ { 3 }$ represent 75% and 64% of the total variance in the corresponding latent variables. Thus, explained variances for $\eta _ { 2 }$ and $\eta _ { 3 }$ were 25% and 36%, respectively. Changing these values has also no impact on our results.

4. The three observed formative indicators, $x _ { 1 } , \ x _ { 2 } ,$ and $x _ { 3 } ,$ were correlated at 0.30.<sup>5</sup> Paths from these indicators to $\eta _ { 1 }$ were equal for all three indicators and were set to values such that, together with the specific values taken by $\gamma _ { 4 }$ in each of the three scenarios and the disturbance term $\zeta _ { 1 } ,$ , the total variance of $\eta _ { 1 }$ would equal one in all scenarios. These values were 0.445 (for $\gamma _ { 4 } = 0 )$ , 0.423 (for $\gamma _ { 4 } = 0 . 3 0 )$ , and 0.382 (for $\gamma _ { 4 } = 0 . 5 0 )$ for the three scenarios discussed here.

5. Sample size was held constant at 300. Though sample size also has no effect on our results, working with smaller (larger) samples has the general effect of increasing (decreasing) the sampling variability present when each sample is collected. As a result, estimates obtained from larger samples will be more closely grouped around the population value of the corresponding parameters. Each of the three scenarios was replicated 1,000 times.

Simulated data for these models were generated as follows. Each model was specified using the values noted above for each parameter in MPlus 3.0 (Muthén and Muthén 1998–2011)—sample data generation code (annotated) is included in Appendix C. In addition to generating data using the sample code, it is possible to do so starting with the implied pop ulation covariance matrices provided in Appendix $\scriptstyle \mathrm { \mathrm { B } , }$ using alternative software packages such as EQS (as done by Petter et al. 2007) or SAS (following the examples set by Fan and Fan 2005; see Appendix E for instructions on how to do this in SAS). To validate the accuracy of the data simulation process, the covariance matrix implied by each different model was calculated following path-tracing rules (the matrices included in Appendix B). Then, a large sample (one million data points) was generated from the models specified in MPlus, its sample covariance matrix calculated, and then the latter was compared to the population covariance matrix that was implied by the model from which the data were generated, with no noticeable differences. This comparison verifies that the covariance matrix implied by the model specified in the data generation process matches that implied by the population models as described above, which helps ensure the accuracy of the simulation process. From each of these replications in each of the three scenarios we extracted the estimate for the coefficient of interest and averaged those estimates over all replications. Consistent with our discussion above, the average estimate for $\gamma _ { 4 }$ in the first scenario (population value = 0) was −0000306, for the second scenario (population value = 0030) 0.005232, and for the third scenario (population value = 0050) the average estimate was −0000402. As noted above, it is not the underlying population value for the parameter $\gamma _ { 4 }$ that drives the estimates that can be obtained from PLS estimation of this model, but rather the values of the covariances shown in (9) which, although different from zero in each individual sample because of sampling variability, average zero over repeated samples. Indeed, the average covariance of those shown in (9) across all replications and the three scenarios (obtained from estimating the covariance matrix of each generated sample and averaging across samples and scenarios) was −0000057. As noted before, these covariances are the only quantities involved in the PLS estimate of $\gamma _ { 4 } .$ In this particular case, those covariances were all equal to zero by design, and thus the obtained estimates reflect that feature of the underlying population model. In a later section we expand on this by considering other values for these covariances, and show that it is only these values, and not the structural relationship of interest, that feature into the estimates obtained from PLS.

## Rationale for This Effect: Comparison with Reflective Models

The underlying rationale behind these results is the lack of covariation between the two weighted composites that substitute for the latent variables of interest when estimating the model shown in Figure 1 using PLS. To fully understand why this is the case, it is instructive to also review why this issue does not appear in other contexts where PLS is commonly used. We do this by examining how PLS would estimate a model where all latent variables are reflectively specified, such as the one shown in Figure $^ { 3 , }$ and then work our way back to the focal scenario here and why these issues arise in this particular context.

The population model depicted in Figure 3 contains only two latent variables, $\dot { \xi }$ and , both of which are measured by four reflective indicators, $y _ { 1 - 4 }$ and $y _ { 5 - 8 } ,$ respectively. There is only a single path connecting the two latent variables. In this case, the reflective indicators can be expressed as a function of their respective latent variables and a residual variance term, similar to (2) above:

$$
y _ {i} = \lambda_ {i} \xi + \theta_ {i}, \quad i = 1, 2, 3, 4,
$$

$$
y _ {i} = \lambda_ {i} \eta + \theta_ {i}, i = 5, 6, 7, 8.\tag{10}
$$

(11)

In addition, the following equation captures the relationship between the two latent variables in the model:

$$
\eta = \gamma \xi + \zeta .\tag{12}
$$

Replacing (12) in (11) yields the following for the reflective indicators of $\eta \colon$

$$
y _ {i} = \lambda_ {i} (\gamma \xi + \zeta) + \theta_ {i}, i = 5, 6, 7, 8.\tag{13}
$$

When data are collected from the population shown in Figure 3 and analyzed using PLS, the two latent variables would be represented by weighted composites of their respective indicators. Again using the subscript c to indicate composites and $w _ { i }$ and $k _ { i }$ for the two sets of weights, the corresponding composites in PLS can be represented as

Figure 3 A Simple Two-Construct Reflective Model  
![](/api/attachments/N5N9CAQA/fulltext/images/9e170701937b994d64c2f2ad8fdfe84fd8092e6c301a85370cd0e95d4494ee92.jpg)

$$
\xi_ {c} = w _ {1} y _ {1} + w _ {2} y _ {2} + w _ {3} y _ {3} + w _ {4} y _ {4},\tag{14}
$$

$$
\eta_ {c} = k _ {1} y _ {5} + k _ {2} y _ {6} + k _ {3} y _ {7} + k _ {4} y _ {8}.\tag{15}
$$

As before, the relationship between the two composites will be a function of the covariance between them. In this case, the covariance between $\xi _ { c }$ and $\eta _ { c }$ can be expressed as

$$
\begin{array}{c} \operatorname{Cov} (\xi_ {c}, \eta_ {c}) = \operatorname{Cov} \bigl (w _ {1} y _ {1} + w _ {2} y _ {2} + w _ {3} y _ {3} + w _ {4} y _ {4}, \\ k _ {1} y _ {5} + k _ {2} y _ {6} + k _ {3} y _ {7} + k _ {4} y _ {8} \bigr). \end{array}\tag{16}
$$

Replacing (10) and (13) into (16) yields the following expression for this covariance in terms of the population quantities shown in Figure 3:

$$
\begin{array}{r l} & {= \mathrm{Cov} \big (w _ {1} (\lambda_ {1} \xi + \theta_ {1}) + w _ {2} (\lambda_ {2} \xi + \theta_ {2})} \\ & {\qquad + w _ {3} (\lambda_ {3} \xi + \theta_ {3}) + w _ {4} (\lambda_ {4} \xi + \theta_ {4}),} \\ & {\qquad k _ {1} \big (\lambda_ {5} (\gamma \xi + \zeta) + \theta_ {5} \big) + k _ {2} \big (\lambda_ {6} (\gamma \xi + \zeta) + \theta_ {6} \big)} \\ & {\qquad + k _ {3} \big (\lambda_ {7} (\gamma \xi + \zeta) + \theta_ {7} \big) + k _ {4} \big (\lambda_ {8} (\gamma \xi + \zeta) + \theta_ {8} \big) \big).} \end{array}\tag{17}
$$

After grouping and rearranging the terms,

$$
\begin{array}{l} \operatorname{Cov} (\xi_ {c}, \eta_ {c}) \\ = \operatorname{Cov} \bigl (\xi (w _ {1} \lambda_ {1} + w _ {2} \lambda_ {2} + w _ {3} \lambda_ {3} + w _ {4} \lambda_ {4}) \\ \qquad + w _ {1} \theta_ {1} + w _ {2} \theta_ {2} + w _ {3} \theta_ {3} + w _ {4} \theta_ {4}, \\ \gamma \xi (k _ {1} \lambda_ {5} + k _ {2} \lambda_ {6} + k _ {3} \lambda_ {7} + k _ {4} \lambda_ {8}) \\ \qquad + \zeta (k _ {1} \lambda_ {5} + k _ {2} \lambda_ {6} + k _ {3} \lambda_ {7} + k _ {4} \lambda_ {8}) \\ \qquad + k _ {1} \theta_ {5} + k _ {2} \theta_ {6} + k _ {3} \theta_ {7} + k _ {4} \theta_ {8}). \end{array}\tag{18}
$$

Although these quantities will deviate from their population value because of sampling variability in any specific sample, in the population model shown in Figure 3 the disturbance term $\zeta$ and the residual terms $\Theta _ { i }$ are uncorrelated with any other quantities in the model. Thus, assuming that any covariances involving these residuals and disturbances in (18) would equal zero in the population, as is commonly done,<sup>6</sup> the expression simplifies to

$$
\begin{array}{c} \operatorname{Cov} (\xi_ {c}, \eta_ {c}) = \operatorname{Cov} \bigl (\xi (w _ {1} \lambda_ {1} + w _ {2} \lambda_ {2} + w _ {3} \lambda_ {3} + w _ {4} \lambda_ {4}), \\ \gamma \xi (k _ {1} \lambda_ {5} + k _ {2} \lambda_ {6} + k _ {3} \lambda_ {7} + k _ {4} \lambda_ {8}) \bigr). \end{array}\tag{19}
$$

Using the expressions in Appendix A, (19) can be expressed as

$$
\begin{array}{c} \operatorname{Cov} (\xi_ {c}, \eta_ {c}) = \gamma (w _ {1} \lambda_ {1} + w _ {2} \lambda_ {2} + w _ {3} \lambda_ {3} + w _ {4} \lambda_ {4}) \\ \cdot (k _ {1} \lambda_ {5} + k _ {2} \lambda_ {6} + k _ {3} \lambda_ {7} + k _ {4} \lambda_ {8}) \operatorname{Var} (\xi). \end{array}\tag{20}
$$

As a result, when employing PLS to estimate the model shown in Figure 3, the estimate for the relationship between the two latent variables will be a function of three quantities, leaving aside sampling variability (as noted above): the true value for the coefficient of interest (), how well each of the indicators of the independent variable capture the nature of the construct (represented by the loadings) and how much weight each indicator is given in the composite representing the independent variable $( w _ { 1 } \lambda _ { 1 } + w _ { 2 } \lambda _ { 2 } +$ $w _ { 3 } \lambda _ { 3 } + w _ { 4 } \lambda _ { 4 }$ in (20)), and how well each of the indicators of the dependent variable captures the nature of the construct (represented by the loadings) and how much weight each indicator is given in the composite representing the dependent variable $( k _ { 1 } \lambda _ { 5 } + k _ { 2 } \lambda _ { 6 } +$ $k _ { 3 } \lambda _ { 7 } \bar { + } k _ { 4 } \lambda _ { 8 }$ in (20)). In short, the true effect and the reliability of each composite involved. The key result arising from (20) is that when a model such as the one depicted in Figure 3 is analyzed using PLS the composites used to represent each of the constructs will have shared variance between them that includes variance due to the coefficient of interest. The other terms in (20) represent the loss of reliability that is incurred by employing weighted composites of variables containing both true score and error variance in them; this is, however, a well-known and understood feature of PLS.

We are now thus in a position to better understand the results discussed before. In the case just elaborated any variance shared by the observed indicators of the latent variables involved is due to, at least partly, the relationship that is the focus of the research. Sampling variability aside, if the model shown in Figure 3 is correctly specified then any systematic relationship between the two composites representing the latent variables of interest is a reflection of the underlying relationship that exists in the population. If those two composites are not related beyond the effects of chance, it is because they are also not related in the population. As a result, even if the estimates obtained by PLS are biased because of unreliability in those composites, they still do reflect an underlying population value. In a model like the one shown in Figure $^ { 3 , }$ then, the issue is how accurate is PLS in estimating those relationships.

This is not the case, however, in the particular scenario under examination in this research. If data are sampled from a population such as the one depicted in Figure 1, there will be no variance in $x _ { 1 } - x _ { 3 }$ that is due to the presence (or absence) of any relationship between the latent variables of interest. Whereas in the reflective case just discussed the individual items that formed each composite were related as a result of the relationship of interest between the two latent variables the composites represent, that will not be the case in the population model shown in Figure 1. In this case, there is no relationship between the observed indicators representing the exogenous construct $( \mathrm { e } . \mathrm { g } . , y _ { 1 - 4 } )$ and those attached to the endogenous, formatively specified construct; that is, $x _ { 1 } , \ x _ { 2 }$ and $x _ { 3 } .$ As can be seen from examining the population model shown in Figure 1, there is no necessary relationship between the exogenous latent variable, which in the PLS model would be represented as a composite of $y _ { 1 - 4 }$ and the formative indicators of the endogenous latent variable, which PLS would represent as a composite of $x _ { 1 - 3 } .$ . As a result of this lack of shared variance between the two sets of indicators used to represent the two latent variables of interest, any estimates obtained from PLS in this case will be different from zero only because of the presence of sampling variability. The statistical technique, however, cannot estimate the parameter of interest from relating two sets of indicators that do not in any way contain that relationship. As we discuss later in more detail, it is perfectly possible for $x _ { 1 } - x _ { 3 }$ to be correlated with $y _ { 1 } - y _ { 4 }$ when the relationship between $\xi$ and $\eta _ { 1 }$ is zero, or for those two groups of variables to be uncorrelated when the relationship between $\xi$ and $\eta _ { 1 }$ is not zero, or any case in between. However, even if these indicators are in some way related to each other—for example, due to sharing a common antecedent—the parameter of interest to researchers, $\gamma _ { 4 } ,$ will not be part of that relationship. We discuss some situations in which this may occur later in this research.

## Generalization and Further Validation

To summarize up to this point, the estimates of structural parameters of interest obtained from the use of PLS are the result of the covariances present in the groups of individual indicators that are employed to form composites representing the latent variables in the model. When the relationship between those individual indicators and their respective latent variables is reflective, composites of those indicators that represent latent variables that are related in the population from which data are collected will share common variance because of the existence of that relationship. Even if biased because of less than perfect reliability of those composites, estimates obtained from PLS will to some degree capture the presence of the underlying relationship of interest. When the endogenous latent variable in such a relationship is related to its observed indicators in a formative manner, as is the case in the model shown in Figure 1, the composites representing the latent variables in PLS do not necessarily share any common variance that is due to the structural relationship that is of interest to the researcher. Although those composites may be related because of other reasons—we provide some examples later—those do not capture the parameter of interest. Rather, any estimates obtained from PLS in these scenarios are capturing something else entirely, the covariances between the two composites that are due to other effects present in the population that are different from those postulated by the researcher. Indeed, PLS is not capable of modeling the relationship between one or more exogenous latent variables and a formatively specified endogenous one. This is irrespective of the particular values taken by that parameter in the population; rather, PLS captures in its estimates of this relationship the covariances between the manifest formative indicators of the endogenous construct and those of the latent predictor, which is not the relationship researchers are attempting to estimate. This is the major result of interest here.

## Additional Monte Carlo Simulations

To further validate our results and extend them to scenarios different from those considered above, we expanded our earlier simulations to include cases where various population values for $\gamma _ { 4 }$ are considered in combination with various values for the covariances between the observed formative indicators of $\eta _ { 1 }$ (that is, $x _ { 1 } , \ x _ { 2 } ,$ , and $x _ { 3 } )$ and the latent exogenous variable $\xi .$ In addition to the previously considered case of no correlation between the observed formative indicators and the latent exogenous variable, we also considered scenarios where those would be correlated at 0.20, 0.40, and $0 . 6 0 . ^ { 7 }$ To accommodate these scenarios, as before, the coefficients linking the observed formative indicators and the latent variable $\eta _ { 1 }$ were modified accordingly to obtain a value of one for the variance of this latent variable. All other parameters in these simulations were kept as in the previously reported ones. As well, 1,000 replications were conducted in each combination. Results from this exercise are reported in Table 2.

Table 2 Results from Monte Carlo Simulations

<table><tr><td rowspan="2">Population value for  $\gamma_4$ </td><td colspan="4">Correlation between  $\xi$  and  $x_{1-3}$ </td></tr><tr><td>0</td><td>0.2</td><td>0.4</td><td>0.6</td></tr><tr><td>0</td><td>-0.0031</td><td>0.2602</td><td>0.5167</td><td>0.7716</td></tr><tr><td>0.30</td><td>0.0052</td><td>0.2652</td><td>0.5174</td><td>0.7704</td></tr><tr><td>0.50</td><td>-0.0040</td><td>0.2647</td><td>0.5155</td><td>0.7711</td></tr></table>

Note. Values shown are estimates obtained from PLS analyses averaged over all replications in each condition for the regression coefficient linking the two latent variables of interest.

To further validate the adequacy of our simulations and the mathematical developments above, we obtained data for each replication in each condition that allowed us to verify that the expression shown in (9) was indeed correct. This was accomplished in the following manner. First, the weights estimated by PLS and used to create the two components of interest, as well as the PLS estimate for the relationship between them, were extracted from the results of each replication. Second, employing the sample data generated for each replication we calculated the full covariance matrix between all observed variables related to these two composites $( y _ { 1 } - y _ { 4 }$ and $x _ { 1 } - x _ { 3 } )$ . Using the expanded expression for the covariance between the two composites shown in (9) and the full formula for the coefficient linking the two composites shown in (4), we recalculated these quantities and compared them with the results obtained from the PLS analysis for the regression parameter of interest. That is, using the weights assigned by PLS to each observed variable for each component, and the variances and covariances between those observed variables, we calculated the value for the regression coefficient that would be obtained from the PLS analysis if our mathematical developments above were correct. A comparison between the two shows no differences between these quantities beyond the three decimal places that the PLS software uses to report the results.

Results from our simulations, shown in Table $^ { 2 , }$ are in line with what would be expected if the expression developed in (9) lies behind the estimates provided by PLS, and go against what researchers would expect to obtain if PLS were actually able to adequately model this particular case of a formatively specified latent variable that is endogenous to other latent variables in the model, in addition to its own corresponding observed formative indicators. The first column of Table 2 reiterates the results obtained previously for completeness and to ease the comparison with the extensions discussed here. As we have discussed before, when the covariances between the observed formative indicators and the latent exogenous variable are zero in the population, then any values different than zero obtained from PLS analyses will be the result solely of sampling variability inherent in the process of collecting finite samples of data from a population. On average, however, those results approximate what should be obtained at the population level. In the first case, when the covariances between these variables are zero, the average estimate for the relationship obtained from PLS will also be zero, irrespective of the true population value of that relationship. This much was validated in our first set of simulations.

In the remaining columns of Table 2 the results show average (over 1,000 replications each) estimates obtained from PLS for various combinations of population values and correlations between the observed formative indicators and the exogenous latent variable. As can be seen, these estimates do not bear any direct relationship with the underlying population value that is being estimated here. Rather, they reflect the degree to which the observed formative indicators and the exogenous latent variable are correlated, this is irrespective of the population value for the parameter. For example, the first row in Table 2 shows that, for a population value of zero for the relationship between the two latent variables, the average PLS estimate will be close to zero (−000031) when the correlation between these variables is also zero, but will take on very different values when those correlations are not zero at the population: 0.2602 when the population correlations are 0.20, 0.5167 when those are 0.40, and 0.7716 when those are 0.60; in all these cases, however, the true population value of the parameter was kept always at zero. The results reported in the remaining rows show a similar pattern, which confirms our arguments about the nature of the estimates calculated by PLS for this particular type of scenario: those are a function of the sample value of the covariances between the observed formative indicators and any exogenous latent variables included in the relationship. These estimates do not, however, bear any relationship with the underlying parameter researchers are attempting to estimate. As discussed before and shown in (9), the parameter itself plays no role in the formula from which estimates are derived. We believe these results have major implications for current research practice.

## Applicability to More Complex Models

These results are not, however, dependent on the particular research model shown in Figure 1 and used throughout this research. Whereas this particular example included a single exogenous latent variable to simplify calculations and the derivations discussed before, our results extend to models with multiple latent variables having an effect on a formatively specified endogenous latent variable. Consider, for example, the expression of standardized regression coefficients, which are those produced by PLS, in matrix form (Pedhazur 1997):

$$
\beta = R ^ {- 1} r.\tag{21}
$$

In (21) $\beta$ is a column vector of standardized regression coefficients, $R ^ { - 1 }$ is the inverse of the correlation matrix of the independent composites, and r is a column vector of correlations between those and the dependent composite that stands in for the Formatively specified latent variable. As a result, standardized regression coefficients are a function of the correlations between the different predictor composite variables and the dependent composite. In the kind of models that are of interest here, the dependent composite, which stands in for the formatively specified latent variable, is a weighted sum of the observed formative indicators associated with it, whereas the predictor composites are also weighted sums of the observed indicators, formative or reflective, attached to them in the model. As before, the lack of any shared variance between the predictor and dependent composites that is due to the relationship of interest is also an issue when we extend our findings to the more general case of multiple predictors expressed in (21)—the correlations captured by the vector r in (21) above are due only to the existence of a relationship between the independent predictors and the observed formative indicators of the dependent latent variable, but do not capture any part of the relationship between the latent predictors and the latent dependent variable.

This shows that our results are not specific to the particular research model shown in Figure 1 but rather apply to a more general class of models where a formatively specified latent variable is endogenous to other latent variables in the model, which can be either formatively or reflectively specified themselves, and to its own observed formative indicators. Although the decomposition of (21) in a manner similar to what was done earlier would be more involved and complex because of the larger number of parameters and covariances that play a role in the

PLS estimates of the regression coefficients of interest, the underlying principle is the same: any variance shared by the observed formative indicators and the latent predictors, which results in shared variance between the observed formative indicators and the observed reflective indicators of those predictors, both of which are then incorporated into the composites created by PLS, is not a result of the relationships of interest here; that is, the effects of the latent predictors on the dependent latent variable.

## Correlation Between Latent Predictors and Formative Indicators

Although it is possible that the latent predictors and the observed formative indicators are indeed correlated, this occurs for reasons that are independent of the relationships researchers are attempting to estimate, and the magnitude of those correlations does not have any necessary relationship with these parameters of interest. It is, for example, possible for the observed formative indicators and the latent predictors to be correlated because of a number of reasons, which we discuss in more detail next; however, those correlations do not provide any information that can be used in the estimation of the regression coefficient between the latent predictors and the endogenous latent variable. On the other hand, it is this information that is being captured by PLS in the form of the estimate provided by the technique, which results in the many issues discussed above. In summary, PLS cannot adequately model this type of relationship between latent variables, which represents a major limitation of this commonly used technique.

The issue of whether observed formative indicators should be allowed to correlate among themselves and with any other exogenous variables in the model has been discussed in some detail by MacCallum and Browne (1993) and more recently by Petter et al. (2007). Although the focus there was somewhat different than here, both authors note that fixing correlations among the observed formative indicators or between the observed formative indicators and other predictors in the model to zero amounts to making very stringent theoretical statements about the complete lack of a relationship between those variables, which are rather unlikely in practice. Correlations between the observed formative indicators of the endogenous latent variable and one or more of the predictor latent variables can be due to a number of factors. First, it is possible that both share an antecedent, $\mathrm { e . g . }$ , a common cause that is not captured in the research model. If $x _ { 1 } - x _ { 3 }$ and $\xi$ in Figure 1 are both due to one or more shared causes, which can be direct or mediated through other intervening variables (two examples of this possibility are shown in Figure 4), then these variables would be correlated among themselves when those antecedents are not included in the model. These correlations would, in turn, show in collected data as correlations between the corresponding observed variables. These relationships, however, do not necessarily imply the existence of a relationship between the two latent variables of interest. PLS would, however, incorporate those correlations into its estimate of the regression parameter linking both latent variables, which is the main issue at hand here.

Figure 4  
(a)  
![](/api/attachments/N5N9CAQA/fulltext/images/09d78b69a7bd247ba1aa8e5db76ab016c68fcfbca78b59af805ef9943f92f808.jpg)

Consider, for example, the population model shown in Figure 4(a). In this case, there is a common antecedent that influences both the exogenous latent variable and the formative indicators of the endogenous latent variable (the indicators of the common antecedent are omitted for clarity). As a result of these influences, the reflective indicators of the former will be correlated with the formative indicators of the latter, due to their shared antecedent. The strength of these correlations will be a function of the values of the various parameters through which the common antecedent influences the manifest indicators, $\mathrm { e . g . , ~ } \ \gamma _ { c c 1 - 4 }$ and $\lambda _ { 1 - 4 } ,$ where cc stands for common cause. When such a model is estimated using PLS, the only variance shared by the weighted composite of $y _ { 1 - 4 }$ representing the exogenous construct and that of $x _ { 1 - 3 }$ representing the endogenous construct will be due to this common antecedent—the parameter of interest, $\gamma _ { 4 } ,$ is not part of this shared variance between the two composites. Also note that this is irrespective of whether the researcher is aware of the common antecedent and that construct is also included in the model. A similar problem arises in the example shown in Figure 4(b), where the influence of a common antecedent is mediated through other intervening variables (indicators of these are also omitted for clarity). In both cases what would be estimated by PLS as representing the structural parameter of interest would be due to shared variance because of a common antecedent. In such a scenario any estimates for $\gamma _ { 4 }$ obtained would represent these effects, and not the one researchers are interested in estimating. In fact, $\gamma _ { 4 }$ could take on any value in the population—including zero—and that would have no effect on the estimate obtained, as previously discussed.

(b)  
![](/api/attachments/N5N9CAQA/fulltext/images/599ec876e510705f4546b82cc229cfb8eca868e9cf1a424a231ecac555e18121.jpg)

Another possibility for the existence of a correlation between the observed formative indicators of the endogenous latent variable and its latent predictors would be a direct relationship between these variables, such that the observed formative indicators of the endogenous latent variable are formative indicators of the predictor as well, or are themselves an effect of that same predictor, as shown in Figure 5. Both of these cases would also result in the presence of covariance between the composites of interest that would be captured by PLS in its estimate, but not adequately represent the underlying population

Figure 5  
(a)  
![](/api/attachments/N5N9CAQA/fulltext/images/46a334bbff690b61d35b01b856d9bad0468239bc8266208fdc3707403e647723.jpg)  
parameter of interest. If the true population model were similar to Figure $5 ( \mathsf { a } ) _ { \mathsf { \Pi } }$ , then the estimate produced by PLS of the relationship between $\xi$ and $\eta _ { 1 }$ would in fact be capturing the presence of an indirect effect of $\xi$ on $\eta _ { 1 }$ that is channeled through the formative indicators $x _ { 1 } - x _ { 3 }$ rather than the direct effect of $\xi$ on $\eta _ { 1 } .$ . In a case such as the one depicted on Figure 5(b) the estimate of the relationship between $\xi$ and $\eta _ { 1 }$ would be a case of a spurious relationship due to unmodeled common causes, similar to the ones depicted in Figures $4 ( \mathsf { a } )$ and 4(b).

Although the scenarios depicted in Figures 4 and 5 are clearly not exhaustive of all the possible ways in which the two sets of manifest indicators that form each composite could be related, they serve to highlight the fact that any estimates obtained from the application of PLS to this kind of relationship would be in fact capturing the presence or absence of these other ways in which the indicators are related, but not the underlying parameter of interest. When the two sets of indicators are not related to each other in any way, the estimate for the parameter will be zero— beyond sampling variability—regardless of the actual population value of the relationship. When the two sets of indicators are related in some way, such as in the examples just discussed, it is those relationships that will be captured in the estimate, also regardless of the actual population value of the relationship of interest.

## Formative Specification and Endogenous Constructs

Finally, there is another take on this issue that may lead researchers to rethink the nature of the relationships between latent variables and formative indicators in current research models. As formatively specified latent variables are presumed to be fully determined by the set of observed formative indicators included in their specification (e.g., a “census” of indicators, cf. Bollen and Lennox 1991, Bollen 2011), it could be argued this would prevent those latent variables from being on the receiving end of any relationships that do not involve their formative indicators. That is, if a formatively specified latent variable receives a direct effect from another latent variable, as is the case in our models and how we currently conceptualize of these relationships in the discipline (see, for instance, Petter et al. 2007), that would be indicative of a misspecification in the research model, as formatively specified latent variables can only receive effects from their own formative indicators. If such effects were significant, however, that may indicate that the latent predictor is in fact related to the formatively specified latent variable, but only indirectly and through one or more of its formative indicators. In this conceptualization, a formatively specified latent variable is fully determined by the set of its manifest formative indicators and it is only through effects on those that other variables in a research model affect the formatively specified latent variable. Figure 6 shows such an example with a single relationship between a latent predictor and a formative indicator.

(b)  
![](/api/attachments/N5N9CAQA/fulltext/images/fbf951b02ecde35f81a3bbc3ed9312f3a45572e862a781bcf3d9dcee2d357b7f.jpg)

Note the difference between Figure 6 and earlier examples (e.g., Figure 5(a)) with regards to both how the models are specified as well as how the relationships included in those would be interpreted. Whereas in Figure 5(a) a possible way in which there would be a covariance between a latent predictor and a formative indicator—in addition the main relationship of interest between the two latent variables—was included, in Figure 6 there is no direct relationship between the latent variables themselves; rather, the effects of the latent predictor are fully channeled through one of the formative indicators of the formatively specified

Figure 6

![](/api/attachments/N5N9CAQA/fulltext/images/8a28826a3f7bb297f92e26473a45265c54e8cd262efbd3f6f37d23ad8f148daa.jpg)

endogenous latent variable. Indeed, in this conceptualization of formatively specified latent variables, following from the discussion above, there would never be direct relationships between latent variables themselves, as those that are formatively specified should only receive direct effects from their manifest, formative indicators. In this case, any significant effects previously established should then be understood as not being between the latent variables themselves, but rather indirect effects through one or more formative indicators.

In a sense, this would make the formative indicator through which these effects are channeled a reflective indicator of the latent predictor, and the meaning of the residual term in the formative indicator would also need to be further conceptualized. We believe the conceptual implications of this approach have not been fully explored yet, and more research in this regard is needed. However, we would also note that these models could also be estimated and tested using covariance-based approaches, in which a model such as the one shown in Figure 6 can be specified directly with existing techniques. PLS, on the other hand, models constructs as weighted composites of the manifest variables directly attached to them, and would not seem to allow for specific modeling of indirect effects through a specific formative indicator. As noted before, more careful consideration of the issue is needed before it can be applied in research practice.

It should be noted that the models used in this research, which are consistent with our current conceptualization of formatively specified endogenous latent variables (cf. Petter et al. 2007), can be fully specified, simulated, and estimated, as we have done here. The issue raised in this last discussion has to do with whether this is the correct approach to conceptualizing formatively specified endogenous latent variables, or alternative relationships are needed. We believe this is an area where further research and thinking are needed, particularly about the implications that the latter conceptualization would have for our interpretation of both existing and future research. In that regard, we hope this brief discussion will bring the issue to the fore and help inspire renewed efforts to examine these issues.

## Implications for Researchers

The major result obtained from this research is that there is no necessary relationship between estimates obtained by PLS and the underlying population value of those parameters under certain conditions; specifically, the problem arises when attempting to estimate the relationship between one or more latent predictors and a formatively specified latent variable that is endogenous to those as well as to its set of observed formative indicators. We should be clear in stating that the issue at hand here is not whether PLS can recover certain parameters more or less accurately, as has been the focus of most research examining this technique; rather, our results indicate that, for this particular scenario (commonly found in actual research, as shown in Table 1), estimates obtained from PLS analyses are not capturing the intended relationship.

Our results have important implications for the practice of research. As previously discussed, a number of studies have been conducted with research models that would give rise to the same problem discussed here, and analyzed with PLS. Given that our results indicate that any estimates obtained from those analyses bear no direct relationship with the actual parameters the researchers were interested in estimating, the validity of those results must unfortunately be called into question. This is the case even if those results were found to be significantly different from zero by the original researchers and all commonly accepted validation procedures were carefully followed, as any results obtained were in fact modeling correlations between various observed variables that do not represent the relationship under investigation. Researchers who are interested in seeing how our arguments apply to their published or ongoing work can do so by doing the following. In doing this, it is important to distinguish the original research model conceptualized by the researcher, such as the one shown in Figure $^ { 1 , }$ and the research model as specified in PLS, shown in Figure 2. First, write down the expressions implied by the model as stated in PLS (and not by the model the researcher was originally interested in testing); for the model shown in Figure 2 those would be, from (14) and (15):

$$
\begin{array}{c} \xi_ {c} = w _ {1} y _ {1} + w _ {2} y _ {2} + w _ {3} y _ {3} + w _ {4} y _ {4}, \\ \eta_ {1 c} = k _ {1} x _ {1} + k _ {2} x _ {2} + k _ {3} x _ {3}, \quad \eta_ {1 c} = \gamma \xi_ {c} + D _ {1}, \end{array}\tag{22}
$$

where $D _ { 1 }$ represents the variance in the dependent composite not explained by the predictor composite, to distinguish it from the latent disturbance term $\zeta _ { 1 }$ that refers to a population quantity. Taken together, the expressions in (22) imply the following:

$$
\begin{array}{r l} & k _ {1} x _ {1} + k _ {2} x _ {2} + k _ {3} x _ {3} \\ & \qquad = \gamma (w _ {1} y _ {1} + w _ {2} y _ {2} + w _ {3} y _ {3} + w _ {4} y _ {4}) + D _ {1}. \end{array}\tag{23}
$$

Researchers can then compare (23) with their research model as originally conceptualized, as shown in Figure 1, and see whether the relationships implied by their research model are consistent with those actually being tested when specifying said model in PLS. As has been argued throughout this research, for the particular case of relationships where a latent variable that is endogenous to other latent variables in addition to its corresponding observed formative indicators, the two representations—Figure 1 and (23)—are not consistent with each other. If Figure 1 shows how researchers have conceived of their study, our research shows PLS is not testing that conceptualization—put more strongly, PLS cannot estimate the model shown in Figure 1 for the various reasons already discussed.

## Model Specification Issues and PLS

Throughout this work we have assumed that researchers have correctly specified the nature of the latent variables included in their models—that ${ \mathrm { i } } { \mathrm { s } } ,$ whether a variable has been formatively or reflectively specified matches the form of the relationship between latent variable and manifest indicators that exist in the underlying population model from which the data were sampled. It is important to at least briefly consider, however, what researchers can expect when those relationships are misspecified, and how such a misspecification will affect the conclusions that can be reached from the estimates about the relationships of interest that can be obtained from PLS. We will consider first the case of an endogenous latent variable that is truly formative but misspecified as reflective, and then the case when the endogenous latent variable is truly reflective and misspecified as formative. In both cases, the latent predictor is truly reflective and correctly specified. For ease of exposition these cases are discussed in terms of a single latent predictor and single latent endogenous variable, though the underlying logic of our discussion can be extended to more complex cases. This issue is important because researchers may see running a model with one specification or the other and obtaining similar results as a measure of the robustness of the estimates, which we show here is not the case.

In the first scenario, a reflectively specified latent predictor has a direct effect on a formatively specified endogenous latent variable. This is a similar case to the models that we have employed here so far.

When modeled in PLS, the latent predictor will be represented by a weighted composite of its reflective indicators (using the outward-directed weighting mode) and the endogenous variable with a weighted composite of its formative indicators (using the innerdirected weighting mode). As we have extensively discussed here, in this scenario the estimates provided by PLS for the relationship between the constructs of interest are dependent on the covariances between both sets of indicators, which do not include the underlying parameter of interest. However, it is also instructive to consider what would happen were the researcher to misspecify the dependent construct as reflective (outward-directed mode in PLS). In this case, the same two sets of indicators will be used to form the two composites that stand in for the latent variables in PLS, and as a result the same set of covariances will underlie the estimate of the relationship provided by PLS. Since what are truly formative indicators of the dependent variable share no necessary relationship with the latent predictor and its reflective indicators, as was the case before, any estimates for the relationship between the constructs obtained from a misspecified model will also result in spurious values, as they do not include the underlying coefficient of interest. Those estimates may be different from those originally obtained when the model was correctly specified, because of differences in the weighting schemes used, but are nonetheless not a necessary representation of the relationship that is being investigated.

In the second scenario considered here, a reflectively specified latent predictor has a direct effect on an also reflectively specified endogenous latent variable. As before, each construct will be represented in PLS with a weighted composite of the manifest indicators directly attached to it. In this case, there is shared variance between the two sets of indicators that is due to the relationship between the constructs: there is variance due to the latent predictor in its own reflective indicators (by virtue of their loadings on the latent variable) as well as in the reflective indicators of the dependent variable (since those are a function of their own latent variable, which is in turn a function—at least partially—of the latent predictor). When correctly specified, both composites will be formed using the outward-directed weighting scheme. In this case, there is shared variance between the composites due to the shared variance across their respective indicators, and this shared variance is due to the relationship of interest. As a result, and subject to the degree of measurement error present in each composite, the estimate of the effect of the latent predictor on the endogenous variable obtained from PLS will be representative of the underlying population value (attenuated because of less than perfect reliability in each composite; this is, however, a well-known feature of PLS). Finally, if a researcher were to misspecify the measurement model of the endogenous construct as formative (when it should truly be reflective), the only difference with the scenario just discussed would lie with the weighting scheme employed (inner directed instead of outward directed); however, the same indicators would be employed to form the composite representing the dependent construct. Given that the same indicators—and hence the same covariances between those and the indicators of the latent predictor— are involved, the only difference between estimates obtained from a correctly specified and a misspecified model lies with the potentially different weights that will be estimated by the iterative process underlying PLS.

Though we do not attempt to provide a comprehensive treatment of the effects of model misspecification when PLS is employed as the statistical technique of choice, it is important to highlight that the underlying nature of the measurement model in the population seems to be a major factor in deciding whether the estimates obtained from PLS capture the underlying relationships of interest. When the true measurement relation for an endogenous variable is formative in nature, any estimates obtained from PLS—whether the model is correctly specified or not—will not accurately capture the relationship between the two constructs, because of the lack of shared variance between the indicators of each that is due to that relationship. This is the main result of interest in this research.

Our work is also related to earlier research by Kim et al. (2010). Though their work refers exclusively to models where the formatively specified construct is in an exogenous position with respect to other constructs in the model, our work considers only those cases where the formatively specified constructs are endogenous to other constructs in the research model. We believe, however, that our conclusions with regards to PLS are not that different. A review of the results reported in Tables 3 and 4 of their work show that PLS displays stronger (i.e., higher) reported paths than those resulting from a LISREL analysis of the same data and research model, even when the underlying models are arguably misspecified with respect to theory. The underlying rationale for this effect is, we believe, that PLS seeks to maximize explained variance in the dependent variables in the model by taking advantage of any correlations between variables that are present in the data (Rönkkö and Ylitalo 2010), whereas LISREL (and other covariance-based approaches such as MPlus, used here) seek to minimize model misfit, and those two goals are not necessarily equivalent in their outcomes. In this light it is possible that PLS, as noted by Kim et al. (2010), provides results that are less accurate but more statistically favorable, in the sense that higher estimates are more likely, everything else being equal, to reach conventionally accepted significance levels. In our case, however, we go beyond the degree of accuracy in PLS estimates, which was the focus of that research, and into whether the estimates provided by PLS for the particular scenario under consideration here do at all capture the underlying population parameter of interest, which we show is not the case.

## Conclusion

Recent work in Information Systems (Aguirre-Urreta and Marakas 2012; Marakas et al. 2007, 2008; Petter et al. 2007) and other disciplines has alerted researchers to the need to carefully consider the specification of the relationship between latent variables and observed indicators. Though the traditional approach of reflectively specifying that relationship (that is, where the direction of causality flows from latent variable to observed indicator) has certainly not fallen into disuse, a significant portion of published research in the last few years has turned to formatively specifying that relationship—where causality flows from observed indicator to latent variables. Though both covariance based (e.g., LISREL, MPlus, EQS, and others) and component based (such as PLS) have been presented as competing alternatives for the analysis of models including formatively specified constructs, the latter has been the preferred approach employed by IS researchers. Justification for this choice is commonly provided by citing presumed limitations of covariance-based techniques when models include formative specifications, though it is not altogether clear that those accurately reflect actual limitations in this regard.

Although PLS appears to be the technique of choice for modeling this type of relationship, this is the first research that examines to what extent the technique is at all appropriate for these situations. Based on a theoretical analysis of the relationships actually being estimated by PLS and how those compare with the relationships of interest, which was subsequently validated empirically through Monte Carlo simulations, we show here that PLS is not an adequate approach to modeling scenarios where a latent variable of interest is endogenous to other latent variables in the research model in addition to its own observed formative indicators. In these cases PLS provides estimates based on covariation between observed formative indicators of the endogenous latent variable and the latent predictors, which is realized in samples as covariation between observed indicators representing both latent variables. Furthermore, though discussed here for the case of a single latent predictor for ease of exposition, our results extend to the more general case of any number of latent predictors and a formatively specified endogenous latent variable. As a consequence, our results are of wide applicability to scenarios commonly encountered by IS researchers, as can be seen from Table 1. Also evidenced by Table 1, researchers in the IS discipline have been eager to explore the use of alternative model specifications that, in their judgment, better reflect the underlying nature of the phenomena under study—this is certainly an important development, as can be seen from the relatively large number of studies shown in Table 1 that have been published in the last few years. Coupled with this important development, we believe, is a need for statistical techniques that can appropriately accommodate those intentions. In this research we examined the most commonly used alternative, and found that researchers should be skeptic about what is really being estimated when results are obtained. In this spirit, we hope our results can help improve the practice of research in our discipline.

## Supplemental Material

Supplemental material to this paper is available at http://dx .doi.org/10.1287/isre.2013.0493.

## Acknowledgments

The authors would like to thank the senior editor, the associate editor, and the anonymous reviewers for helpful comments on previous versions of this research. Any errors or omissions remain those of the authors.

## References

Aguirre-Urreta M, Marakas G (2012) Revisiting bias due to construct misspecification: Different results from considering coefficients in standardized form. MIS Quart. 36(1):123–138.

Bollen K (1984) Multiple indicators: Internal consistency or no necessary relationship. Quality and Quantity 18:377–385.

Bollen K (2011) Evaluating effect, composite, and causal indicators in structural equation models. MIS Quart. 35(2):359–372.

Bollen K, Lennox R (1991) Conventional wisdom on measurement: A structural equation perspective. Psych. Bull. 110(2):305–314.

Cenfetelli R, Bassellier G (2009) Interpretation of formative measurement in information systems research. MIS Quart. 33(4): 689–708.

Chengalur-Smith I, Nevo S, Demertzoglu P (2010) An empirical analysis of the business value of open source infrastructure technologies. J. Assoc. Inform. Systems 11:708–729.

Chin W (1993) PLS-Graph User’s Guide, Version 3.0. (Soft Modeling, Inc.)

Chin W (1998) Issues and opinions in structural equation modeling. MIS Quart. 22(1):vii–xvi.

Choi S, Lee H, Yoo Y (2010) The impact of information technology and transactive memory systems on knowledge sharing, application, and team performance: A field study. MIS Quart. 34(4):855–870.

Cohen J (1988) Statistical Power Analysis for the Behavioral Sciences (Lawrence Erlbaum, Hillsdale, NJ).

Cohen P, Cohen J, Teresi J, Marchi M, Velez C (1990) Problems in the measurement of latent variables in structural equations causal models. Appl. Psych. Measurement 14(2):183–196.

Curtis R, Jackson E (1962) Multiple indicators in survey research. Amer. J. Soc. 68(2):195–204.

Diamantopoulos A, Winklhofer H (2001) Index construction with formative indicators: An alternative to scale development. J. Marketing Res. 38:269–277.

Edwards J (2011) The fallacy of formative measurement. Organ. Res. Methods 14(2):370–388.

Fan X, Fan X (2005) Using SAS for Monte Carlo simulation research in SEM. Structural Equation Model 12(2):299–333.

Feller J, Finnegan P, Fitzgerald B, Hayes J (2008) From peer production to productization: A study of socially enabled business exchanges in open source service networks. Inform. Systems Res. 19(4):475–493.

Henseler J (2010) On the convergence of the partial least squares path modeling algorithm. Comput. Statist. 25(1):107–120.

Iacovou C, Thompson R, Smith H (2009) Selective status reporting in information systems projects: A dyadic-level investigation. MIS Quart. 33(4):785–810.

James L, Mulaik S, Brett J (1983) Causal Analysis: Assumptions, Models, and Data (Sage Publications, Beverly Hills, CA).

Jarvis C, MacKenzie S, Podsakoff P (2003) A critical review of construct indicators and measurement model misspecification in marketing and consumer research. J. Consumer Res. 30:199–218.

Kim D, Benbasat I (2010) Trust-assuring arguments in B2C e-commerce: Impact of content, source, and price on trust. J. Management Inform. Systems 26(3):175–206.

Kim G, Shin B, Grover V (2010) Investigating two contradictory views of formative measurement in information systems research. MIS Quart. 34(2):345–365.

Klein R, Rai A (2009) Interfirm strategic information flows in logistics supply chain relationships. MIS Quart. 33(4):735–762.

Lee G, Xia W (2010) Toward agile: An integrated analysis of quantitative and qualitative data on software development agility. MIS Quart. 34(1):87–114.

Liang H, Saraf N, Hu Q, Xue Y (2007) Assimilation of enterprise systems: The effect of institutional pressures and the mediating role of top management. MIS Quart. 31(1):59–87.

Limayen M, Hirt S, Cheung C (2007) How habit limits the predictive power of intention: The case of information systems continuance. MIS Quart. 31(4):705–737.

Little T, Slegers D, Card N (2006) A non-arbitrary method of identifying and scaling latent variables in SEM and MACS models. Structural Equation Model. 13(1):59–72.

Lohmöller J (1989) Latent Variable Path Modeling with Partial Least Squares (Physica-Verlag, Heidelberg, Berlin).

Lowry P, Romano N, Jenkins J, Guthrie R (2009) The CMC interactivity model: How interactivity enhances communication quality and process satisfaction in lean-media groups. J. Management Inform. Systems 26(1):155–195.

MacCallum R, Browne M (1993) The use of causal indicators in covariance structure models: Some practical issues. Psych. Bull. 114(3):533–541.

MacKenzie S, Podsakoff P, Jarvis C (2005) The problem of measurement model misspecification in behavioral and organizational research and some recommended solutions. J. Appl. Psych. 90(4):710–730.

Malhotra A, Gosain S, El Sawy O (2007) Absorptive capacity configurations in supply chains: Gearing for partner-enabled market knowledge creation. MIS Quart. 29(1):145–187.

Marakas G, Johnson R, Clay P (2007) The evolving nature of the computer self-efficacy construct: An empirical investigation of measurement construction, validity, reliability and stability over time. J. Assoc. Inform. Systems 8(1):16–46.

Marakas G, Johnson R, Clay P (2008) Formative vs. reflective measurement: A reply to Hardin, Chang, and Fuller. J. Assoc. Inform. Systems 9(9):535–543.

Mithas S, Krishnan M (2009) From association to causation via a potential outcomes approach. Inform. Systems Res. 20(2): 295–313.

Muthén L, Muthén B (1998–2011) Mplus User’s Guide (Muthén & Muthén, Los Angeles).

Pedhazur E (1997) Multiple Regression in Behavioral Research (Thomson Learning, Stamford, CT).

Pee L, Kankanhalli A, Kim H (2010) Knowledge sharing in information systems development: A social interdependence perspective. J. Assoc. Inform. Systems 11(10):550–575.

Petter S, Straub D, Rai A (2007) Specifying formative constructs in information systems research. MIS Quart. 31(4):623–656.

Rai A, Brown P, Tang X (2009) Organizational assimilation of electronic procurement innovations. J. Management Inform. Systems 26(1):257–296.

Rönkkö M, Ylitalo J (2010) Construct validity in partial least squares path modeling. Proc. Internat. Conf. Inform. Systems, St. Louis, MO, http://aisel.aisnet.org/icis2010\_submission/155.

Sia C, Lim K, Leung K, Lee M, Huang W, Benbasat I (2009) Web strategies to promote Internet shopping: Is culturalcustomization needed? MIS Quart. 33(3):491–512.

Venkatesh V, Ramesh V (2006) Web and wireless site usability: Understanding differences and modeling use. MIS Quart. 30(1):181–206.

Whitaker J, Mithas S, Krishnan M (2010) Organizational learning and capabilities for onshore and offshore business process outsourcing. J. Management Inform. Systems 27(3):11–42.

Wold H (1982) Soft modeling—The basic design and some extensions. Jöreskorg K, Wold H, eds. Systems Under Indirect Observation—Part II (North-Holland Publishing, New York), 1–54.

Yi M, Davis F (2003) Developing and validating an observational learning model of computer software training and skill acquisition. Inform. Systems Res. 14(2):146–169.

Zhu K, Kraemer K, Gurbaxani V, Xin Xu S (2006) Migration to openstandard interorganizational systems: Network effects, switching costs, and path dependency. MIS Quart. 30(SI):515–538.
