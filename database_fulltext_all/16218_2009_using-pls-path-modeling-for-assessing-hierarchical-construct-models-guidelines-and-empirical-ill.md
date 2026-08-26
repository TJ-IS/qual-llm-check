---
otero_id: 16218
otero_key: "PVNHXUWZ"
title: "Using PLS Path Modeling for Assessing Hierarchical Construct Models: Guidelines and Empirical Illustration"
authors: "Martin Wetzels; Gaby Odekerken-Schröder; Claudia van Oppen"
year: "2009"
journal: "MIS Quarterly"
doi: "10.2307/20650284"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Using PLS Path Modeling for Assessing Hierarchical Construct Models: Guidelines and Empirical Illustration

Author(s): Martin Wetzels, Gaby Odekerken-Schröder and Claudia van Oppen

Source: MIS Quarterly, Vol. 33, No. 1 (Mar., 2009), pp. 177-195

Published by: Management Information Systems Research Center, University of Minnesota

Stable URL: http://www.jstor.org/stable/20650284

Accessed: 09-06-2015 18:12 UTC

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# USING PLS PATH MODELING FOR ASSESSING HIERARCHICAL CONSTRUCT MODELS: GUIDELINES AND EMPIRICAL ILLUSTRATION $^{1}$

By: Martin Wetzels
Department of Marketing
Maastricht University
Tongersestraat 53
6211 LM Maastricht
THE NETHERLANDS
m.wetzels@mw.unimaas.nl

Gaby Odekerken-Schröder
Department of Marketing
Maastricht University
Tongersestraat 53
6211 LM Maastricht
THE NETHERLANDS
g.schroder@mw.unimaas.nl

Claudia van Oppen
SME Portal
Maastricht University
Tongersestraat 53
6211 LM Maastricht
THE NETHERLANDS
Mkbportal@unimaas.nl

## Abstract

In this paper, the authors show that PLS path modeling can be used to assess a hierarchical construct model. They provide guidelines outlining four key steps to construct a hierarchical construct model using PLS path modeling. This approach is illustrated empirically using a reflective, fourth-order latent variable model of online experiential value in the context of online book and CD retailing. Moreover, the guidelines for the use of PLS path modeling to estimate parameters in a hierarchical construct model are extended beyond the scope of the empirical illustration. The findings of the empirical illustration are used to discuss the use of covariance-based SEM versus PLS path modeling. The authors conclude with the limitations of their study and suggestions for future research.

Keywords: PLS path modeling, hierarchical construct model, empirical illustration, experiential value

## Introduction

Almost 25 years ago Noonan and Wold (1983, p. 283) observed: “Path analysis with hierarchically structured latent variables within the framework of PLS is at an early stage of development, and research is still under way.” Unfortunately, their observation is still a valid one, as applications and research into the use of hierarchical construct models using PLS path modeling are still limited. However, several authors have discussed both the theoretical and empirical contributions hierarchical models can make (Edwards 2001; Edwards and Bagozzi 2000; Jarvis et al. 2003; Law and Wong 1999; MacKenzie et al. 2005; Petter et al. 2007), although almost exclusively in the realm of covariance-based structural equation modeling (SEM). Components-based SEM, or PLS path modeling, can also be used to estimate hierarchical construct models (Lohmöller 1989; Noonan and Wold 1983; Petter et al. 2007; Wold 1982). In this manuscript we will use PLS path modeling to construct a hierarchical construct model, show an empirical application, and provide guidelines for its use. $^{2}$

For our empirical illustration we have chosen the construct of online experiential value, which has recently been advanced as a crucial driver of e-loyalty (Kim and Stoel 2004; Novak et al. 2000). When Mathwick et al. (2001, 2002) introduced, developed, and tested their experiential value scale, they referred to an experience-based value concept. Theoretically, their experiential value concept represents a fourth-order, reflective, hierarchical construct model that consists of intrinsic (hedonic) value and extrinsic (utilitarian) value as underlying dimensions (Babin et al. 1994; Holbrook and Hirschman 1982). Although the authors provide conceptual support for this hierarchical model, their empirical study only partially tests it.

Therefore, our main objective is to demonstrate that PLS path modeling can be used to estimate the parameters in a fourth-order, reflective, hierarchical construct model using online experiential value as an empirical illustration. This demonstration extends the work by Mathwick et al. (2001) by specifying experiential value as a reflective, fourth-order latent variable with hedonic (intrinsic) and utilitarian (extrinsic) value as underlying dimensions at the third-order level. We include the resulting hierarchical model in a structural model assessing its nomological validity. We use this application to demonstrate guidelines for assessing hierarchical models using PLS path modeling.

This paper is structured as follows. We first elaborate on the contributions of hierarchical construct modeling. In the next section we will discuss how hierarchical construct models can be estimated using structural equation modeling. Then we provide guidelines to build hierarchical construct models using PLS path modeling. Subsequently, we provide an empirical demonstration of the procedure suggested. We discuss how the guidelines suggested can be extended beyond the scope of our empirical illustration. Moreover, we discuss the implications of our study by focusing on the conditions under which PLS path modeling might be more adequate than covariance-based SEM. Finally, we conclude with the limitations of the paper and suggestions for further research.

## The Utility of Hierarchical Construct Models

Hierarchical constructs, or multidimensional constructs, as their discussion and application is often limited to a second-order hierarchical structure, can be defined as constructs involving more than one dimension (Edwards 2001, Jarvis et al. 2003; Law and Wong 1999; Law et al. 1998; MacKenzie et al. 2005; Netemeyer et al. 2003; Petter et al. 2007). As such, they can be distinguished from unidimensional constructs, which are characterized by a single underlying dimension (Netemeyer et al. 2003).

The utility of hierarchical construct models is based on a number of theoretical and empirical grounds (Edwards 2001). Proponents of the use of higher-order constructs have argued that they allow for more theoretical parsimony and reduce model complexity (Edwards 2001; Law et al. 1998; MacKenzie et al. 2005); Edwards (2001) summarizes this argument as theoretical utility; theory requires general constructs consisting of specific dimensions or facets. This is closely related to the trade-off between accuracy and generalization as suggested by Gorsuch (1983), who argues that “factors are concerned with narrow areas of generalization where the accuracy is great [whereas] higher-order factors reduce accuracy for an increase in the breadth of generalization” (p. 240). Law et al. (1998, p. 749) even state that “treating dimensions as a set of individual variables precludes any general conclusion between a multidimensional construct and other constructs.”

Moreover, hierarchical construct models allow matching the level of abstraction for predictor and criterion variables (Edwards 2001). Fischer (1980) refers to this as measure specificity, that is, predictor and criterion (latent) variables should be related to each other on the same level of abstraction. For example, Chin and Gopal (1995) discuss three models, in which the intention to adopt GSS is explained by the belief in GSS adoption. Their first model links the underlying dimensions (relative advantage, ease of use, compatibility, and enjoyment) of belief in GSS adoption directly to intention to adopt GSS, without introducing a higher-order latent variable. The second model is a “molar” model, in which belief in GSS adoption is constructed as a latent variable with formative dimensions, while the third model is a “molecular” model, in which belief toward GSS adoption is constructed as a latent variable with reflective dimensions. Model 2 and Model 3 presented by Chin and Gopal show a fit regarding the level of abstraction, while Model 1 links dimensions directly to a potentially higher-order latent variable.

The conceptual grounds raised above are complemented by two empirical points: reliability and validity of measures of the multidimensional constructs (Edwards 2001). Typically, as the heterogeneity of the dimensions of the multidimensional construct increases, the internal consistency of the summed dimension scores will eventually be reduced. Moreover, the construct validity of the dimension measures has been questioned, as it contains large amounts of specific and group variance, which are generally treated as error variance (see Law et al. 1998). Finally, proponents of higher-order constructs contend that such constructs exhibit a higher degree of criterion-related validity, especially if they serve as predictors.

## Estimation of Hierarchical Construct Models

Edwards (2001) proposes an integrative analytical framework on the basis of (covariance-based) structural equation modeling (SEM), which allows for the simultaneous inclusion of higher-order (multidimensional) constructs and their dimensions as latent variables. In a structural model, the higher-order constructs may serve as either cause or effect by being embedded in a nomological network. This approach also allows us to derive the (indirect) effects of lower-order constructs, or dimensions, on outcomes of the higher-order construct as the pairwise product of loadings (or weights for formative constructs) and coefficients of the outcomes. Moreover, SEM allows for the explicit specification of the direction of the relationships between manifest variables and latent variables (Edwards and Bagozzi 2000).

Essentially, two models of higher-order (multidimensional) constructs can be distinguished on the basis of the directions of the relationship between manifest and latent variables (Law and Wong 1999):

(1) the factor model (Chin and Gopal: molecular model; Edwards: superordinate construct model; Jarvis et al.: principal factor model; Law et al.: latent model; MacKenzie et al.: common latent construct), and

(2) the composite model (Chin and Gopal: molar model; Edwards: aggregate construct; Jarvis et al.: composite latent variable model; Law et al.: aggregate model; MacKenzie et al: composite latent construct model).

For the factor model, or reflective construct model, the manifest variables are affected by the latent variable(s) $(LV_{j} \rightarrow MV_{i})$ , whereas for the composite model, or the formative construct model, this relationship is reversed $(LV_{j} \leftarrow MV_{i})$ .

For the reflective construct model, higher-order, or hierarchical, latent variable models can be specified as an alternative to group-factor models, i.e., a latent variable model for which all first-order latent variables are correlated, or a first-order confirmatory factor analysis (Bollen 1989; Guinot et al. 2001; Hunter and Gerbing 1982; Marsh and Hocevar 1985; Rindskopf and Rose 1988). Basically, a hierarchical model imposes an alternative structure on the pattern of correlations (covariances) among lower-order latent variables (or factors) of the group-factor model. As such, the higher-order model represents a restriction of the group-factor model, which allows for correlation of the lower-order latent variables (or factors; Rindskopf and Rose 1988). For example, a second-order model can be specified by the following two equations:

$$
\begin{array}{l} \text {(1)} \quad \mathrm {y_ {i}} = \Lambda_ {\mathrm{y}} \cdot \eta_ {\mathrm{j}} + \varepsilon_ {\mathrm{i}} \\ \text {(2)} \quad \eta_ {\mathrm{j}} = \Gamma \cdot \xi_ {\mathrm{k}} + \zeta_ {\mathrm{j}} \end{array}
$$

The first equation defines the manifest variables $(y_{i})$ in terms of the first-order latent variable $(\eta_{j})$ and an (measurement) error term $(\varepsilon_{i})$ ; $\Lambda_{y}$ denotes the first-order latent variable loadings. The second equation defines the first-order factors $(\eta_{j})$ in terms of the second-order latent variables $(\xi_{k})$ and a disturbance, or residual, term (measurement error for the first-order factor; $\zeta_{j}$ ); $\Gamma$ denotes the second-order latent variable loadings. Obviously, this hierarchical model can be extended to higher-order latent variables, such as third-order latent variables (see Marsh and Hocevar 1985). For a third- or fourth-order model, Equation (2) can be extended as follows:

$$
\eta_ {j} = B \cdot \eta_ {j} + \Gamma \cdot \xi_ {k} + \zeta_ {j} \tag {3}
$$

The term $B\eta_{j}$ represents the higher-order latent variables (or related outcomes) from the first to the $n^{th}$ order, except for the highest order latent variable, which is represented by the term $\Gamma\xi_{k}$ (Edwards 2001; Edwards and Bagozzi 2000). Hierarchical construct models can also be specified using formative constructs and/or a mix of formative and reflective measures (Edwards 2001; Jarvis et al. 2003; MacKenzie et al. 2005; Petter et al. 2007).

Hierarchical models using latent variables can be estimated using SEM. Both covariance-based SEM (Edwards 2001; Jarvis et al. 2003; MacKenzie et al. 2005; Marsh and Hocevar 1985) and component-based SEM, or PLS path modeling (Chin and Gopal 1995; Guinot et al. 2001; Noonan and Wold 1983; Tenenhaus et al. 2005), can be employed to estimate the parameters in a hierarchical model, although covariance-based SEM involves various constraints regarding the distributional properties (multivariate normality), measurement level, sample size, model complexity, identification, and factor indeterminacy (Chin 1998; Fornell and Bookstein 1982).

For covariance-based SEM, these constraints are even more formidable in the case of hierarchical models. To identify reflective higher-order construct models for each single higher-order factor, there should be at least four lower-order factors. For uncorrelated higher-order factors, there should be at least three lower-order factors; while for correlated higher-order factors, there should be at least two lower-order factors (Marsh and Hocevar 1985; Rindskopf and Rose 1988). Moreover, at least two manifest variables are desired for lower-order factors (Rindskopf and Rose 1988). For formative (higher-order) constructs, the restrictions necessary for identification are even more stringent (Bollen and Lennox 1991; Jarvis et al. 2003; MacCallum and Browne 1993; MacKenzie et al. 2005). Edwards provides a detailed overview of the constraints necessary to identify reflective and formative higher-order constructs be it as cause or effect. As the covariance-based SEM approach to estimate higher-order models is not the main focus of this paper interested readers are encouraged to review these sources in more detail. Finally, in addition to the mathematical identification, the higher-order model is also susceptible to empirical underidentification (Chen et al. 2001; Dillon et al., 1987; Rindskopf 1984; Rindskopf and Rose 1988), which can lead to inadmissible solutions and/or nonconvergence, especially because factor correlations might be “very close” to 0 or 1.

These problems might be avoided entirely with the use of component-based SEM or PLS path modeling (Chin 1998; Chin and Newsted 1999; Wold 1985). Fornell and Bookstein (1982) show that PLS path modeling ensures against improper solutions by the removal of factor indeterminacy; latent variable scores are determinate and can be directly estimated. Furthermore, since the residual covariance structure for the measurement error terms and the disturbance terms is not restricted in PLS path modeling, there are no identification problems for recursive models. Finally, Chin and Newsted (1999) observe that PLS path modeling is generally more suitable for studies in which the objective is prediction, the phenomenon under study is new or changing (i.e., the theoretical framework is not yet fully crystallized), the model is relatively complex (i.e., large number of manifest and latent variables), formative constructs are included in the conceptual framework, and the data used does not satisfy the assumptions of (multivariate) normality, large sample size, and independence.

## Guidelines for Specifying Hierarchical Latent Variable Models Using PLS Path Modeling

PLS path modeling allows for the conceptualization of a hierarchical model through the repeated use of manifest variables (Guinot et al. 2001; Lohmöller 1989; Noonan and Wold 1983; Tenenhaus et al. 2005; Wold 1982). A higher-order latent variable can thus be created by specifying a latent variable that represents all the manifest variables of the underlying lower-order latent variables. For example, if a second-order latent variable consists of four underlying first-order latent variables, each with three manifest variables, the second-order latent variable can be specified using all (12) manifest variables of the underlying first-order latent variables. Consequently, the manifest variables are used twice: for the first-order latent variable (“primary” loadings) and for the second-order latent variable (“secondary” loadings). Having thus specified the outer model (measurement model), the inner model (structural model) accounts for the hierarchical component of the model, as it represents the loadings of the second-order latent variable on the first-order latent variables. This approach can obviously easily be extended to higher-order hierarchical models (see Noonan and Wold 1983). As latent variable scores are determinate in PLS path analysis, latent variables scores for lower-order latent variables can be obtained (Chin 1998; Tenenhaus et al. 2005), which can subsequently be used as manifest variables for the higher-order latent variables.

After having discussed the usefulness of PLS in assessing hierarchical latent variable models, we now turn to a practical set of guidelines to construct higher-order latent variables for reflective, hierarchical construct models using PLS path modeling. For instructional purposes, the hierarchical construct model is restricted to the third-order level. Table 1 presents a four step approach to set up higher-order latent variable models in a reflective, hierarchical construct model using PLS path modeling.

As a universal fit measure, such as model $\chi^{2}$ for covariance-based SEM using maximum likelihood estimation and derived fit indices, is not available in PLS path modeling, it lacks an index that allows for a global validation of the model (Chin

Table 1. Guidelines for Specifying Hierarchical Latent Variable Models Using PLS Path Modeling

<table><tr><td>1</td><td>Construct the first-order latent variables (LV11– LV14) and relate them to their respective block of manifest fiables (LV11: MV1– MV3; LV12: MV4– MV6; LV13: MV7– MV9; LV14: MV10– MV12) using Mode A (reflective) in their outer model. The loadings represent the first-order loadings.</td><td></td></tr><tr><td>2</td><td>The second-order latent variables can now be constructed by relating them to the block of the underlying first-order latent variables (LV21: MV1– MV63; LV22: MV7– MV12) using Mode B (reflective) in their outer model (the dashed lines represent the secondary loadings). The first-order latent variables (LV11– LV14) are now related to the second-order latent variables (LV21 and LV22) as reflective dimensions. This inner model represents the second-order loadings.</td><td><img src="/api/attachments/PVNHXUWZ/fulltext/images/ab4787735f72b2036a9cb994dc91a8ebdc9e34f487d741a9a094e499b91b6db9.jpg"/></td></tr><tr><td>3</td><td>The third-order latent variables are now constructed by setting up an outer model consisting of the blocks of manifest variables of the second-order latent variables (for LV3 this means all manifest variables; the dashed lines represent the secondary loadings). The second-order latent variables (LV21 and LV22) are now related to the third-order variable (LV3) as reflective dimensions. The inner model between the second-order and third-order latent variables represents the third-order loadings.</td><td><img src="/api/attachments/PVNHXUWZ/fulltext/images/320942bcb01aecd22e99426c91932090a7f5a83365b97c0ecbf4e6adf7485e86.jpg"/></td></tr><tr><td>4</td><td>Finally, the hierarchical model can now be estimated using PLS path modeling. We obtain estimates for the first-order loadings, second order loadings, and third-order loadings. A nonparametric bootstrapping procedure may be used to obtain standard error and calculate t statistics for inferential purposes.</td><td><img src="/api/attachments/PVNHXUWZ/fulltext/images/3a362d3e88839e0d7bb89aa40c96c1e9518a224554962d33c6d1874c9004d032.jpg"/></td></tr></table>

1998; Tenenhaus et al. 2005). $^{3}$ Although a global goodness-of-fit (GoF) criterion has been proposed for PLS path modeling, it mainly serves a diagnostic purpose and not a formal testing one (see Tenenhaus et al. 2005).

## An Empirical Illustration

## Developing the Conceptual Framework

In our empirical illustration, we use the concept of online experiential value to demonstrate how PLS path modeling can be used to estimate the parameters in a reflective, hierarchical latent variable model. Furthermore, we will embed the hierarchical construct in a nomological network, and relate it to e-loyalty.

Mathwick et al. (2001) were the first to introduce, develop, and test a scale of experiential value in an online context. They define online experiential value as “a perceived, relativistic preference for product attributes or service performances arising from interaction within a consumption setting that facilitates or blocks achievement of customer goals or purposes” (p. 53). Moreover, they base their conceptualization of experiential value on Holbrook’s (1994) work and distinguish between intrinsic (hedonic) and extrinsic (utilitarian) value components on the one hand and active versus reactive sources of value on the other. With respect to the active and reactive sources of value, Holbrook (p. 43) defines the active dimension as “a manipulation of the environment,” such as occurs when people play video games. In the reactive dimension, the consumer mainly acts as a viewer and receiver rather than as an active participant.

Mathwick et al. also distinguish playfulness, aesthetics, customer return on investment (CROI), and service excellence as sources of value. These second-order concepts in turn comprise several first-order constructs. Playfulness involves enjoyment and escapism, aesthetics is composed of visual appeal and entertainment, and CROI is made up of economic value and efficiency; these authors do not define any first-order concepts of service excellence.

The conceptual distinction between utilitarian (extrinsic) and hedonic (intrinsic) value already has been demonstrated by Mathwick et al. in an online retail setting of women's apparel and housewares. However, their conceptual model is restricted to a hierarchical model at the second-order level. Yet, Novak et al. (2000) claim that online experiences consist of both experiential and goal-directed aspects and therefore suggest the need to evaluate Web sites according to both hedonic and utilitarian value dimensions. We use Mathwick et al.'s conceptualization to illustrate the assessment of a reflective, fourth-order hierarchical model by using PLS. In line with the proposed guidelines, we assess a model in which hedonic value (reflecting the second-order latent variables aesthetics and playfulness) and utilitarian value (reflecting the second-order latent variables service excellence and CROI) are specified as third-order latent variables and experiential value as a fourth-order latent variable reflecting utilitarian and hedonic value. An overview of the conceptual framework containing the fourth-order conceptual framework is depicted in Figure 1.

To embed online experiential value in a nomological network, we will relate it to e-loyalty. Srinivasan, Anderson, and Ponnavlu (2002) define e-loyalty as a favorable attitude toward a Web site that results in repeat visit behavior. This definition reflects the commonly accepted distinction between attitudinal and behavioral aspects of customer (e-)loyalty. Attitudinal loyalty includes some extent of preference (affect) and commitment, whereas behavioral loyalty consists of revisit intentions (conation) toward a website (e.g., Chaudhuri and Holbrook 2001). Therefore, we test the following hypotheses:

$H_{1a}$ : Online experiential value has a positive impact on attitudinal e-loyalty.

$H_{1b}$ : Online experiential value has a positive impact on behavioral e-loyalty.

As indicated by theory of planned behavior (TPB; Ajzen 1991), consumer attitudes influence behavior. Therefore, we finally test the following hypothesis:

$H_{2}$ : Attitudinal e-loyalty has a positive impact on behavioral e-loyalty.

We posit that the relationship between online experiential value and behavioral e-loyalty is mediated by attitudinal e-loyalty. $H_{1b}$ denotes the direct effect in the (partial) mediation model and has been included to test for mediation. $H_{1a}$ , $H_{1b}$ , and $H_{2}$ complete our conceptual framework (see Figure 1).

## Method

## Research Setting

We demonstrate that PLS path modeling can be used to assess reflective, hierarchical construct models and illustrate this in the context of online CD and book retailers. This context provides an appropriate environment for several reasons. First, research indicates that CDs and books are among the most frequently purchased items online (Kim and Stoel 2004; Kwak et al. 2002). Second, by addressing both product categories, our study is not limited to only one dimension of online experiential value but can address both hedonic and utilitarian value components. Kwak et al. (2002) offer preliminary evidence for this assumption with their indication that to purchase books online, a high degree of information is required, whereas CDs require a low degree of information.

![](/api/attachments/PVNHXUWZ/fulltext/images/2732cff043ea7662f7a00bd739637ddc9be16fd1b319035853ad2c93ddcd727f.jpg)  
Error Terms $(\delta_{i},\varepsilon_{i})$ for the manifest variables and the disturbance terms $(\zeta_{i})$ are omitted to simplify the representation of the model.  
Figure 1. Conceptual Framework

## Sampling

We selected a sample of 1,000 individuals from a large online research panel, then sent an e-mail invitation, containing an embedded URL link to the Website hosting the survey, to each potential respondent. To increase the response rate, we raffled off five cash incentives worth \$12.50, which resulted in a total of 308 respondents. As a screening question, we asked whether the respondent had ever visited or purchased from an online retailer selling both books and CDs, such as Amazon.com or Barnesandnoble.com. On the basis of this screening question, 190 respondents remained for further analysis. Next, we asked these remaining respondents to complete the questionnaire about their most frequently visited online book and CD store to evaluate their online experiences.

Of the participants, 57.6 percent were women; 9.6 percent were younger than 20 years of age, 63.9 percent were between 20 and 25 years, 19.5 percent were between 26 and 30 years, and 7 percent were older than 30 years. Of the total sample population, 73.8 percent considered themselves students, 21.9 percent as being employed, and 4.3 percent as “other.”

## Measurement Instruments

The online questionnaire consisted of previously published multi-item scales with favorable psychometric properties and was administered in English. The experiential value scale we used was introduced by Mathwick et al. (2001). We applied the e-loyalty scale used by Srinivasan et al. (2002) (see Table 2). All of the items were measured on a seven-point Likert-type scale, ranging from “strongly disagree” to “strongly agree.” In addition, information about the respondents’ gender, age, nationality, and profession was collected.

Before the actual research was conducted, five graduate students pretested the questionnaire, paying specific attention to question content, wording, sequence, format and layout, question difficulty, and instructions. During this pretest, we observed the respondents to monitor their reactions and attitudes toward the questionnaire. On the basis of the problems identified by the respondents, we made minor adjustments to the questionnaire. $^{4}$

## Assessing the Hierarchical Structure Using PLS

In assessing the reflective, hierarchical construct model of online experiential value using PLS path modeling, we followed the guidelines suggested by Marcoulides and Saunders (2006):

(1) Propose a model that is consistent with all currently available theoretical knowledge and collect data to test that theory (see previous section).

(2) Perform data screening.

(3) Examine the psychometric properties of all variables in the model.

(4) Examine the magnitude of the relationships and effects between the variables being considered in the proposed model.

(5) Examine the magnitude of the standard errors of the estimates in the proposed model and construct confidence intervals for the population parameters of interest.

(6) Assess and report the power of the study.

We first assessed the distributional properties of the manifest variables. Our inspection of the univariate measures of skewness and kurtosis shows only slight deviations from univariate normality (<|1.0|). However, Mardia's (1970) test of multivariate kurtosis (normalized 9.12, p < 0.001) and Small's (Looney 1995) test of multivariate normality (VQ3 = 246.55, p < 0.001) demonstrate that the assumption of multivariate normality is violated (DeCarlo 1997).

We used PLS Graph 3.0 (Chin 2001) to estimate the parameters in the outer and inner model using PLS path modeling with a path weighting scheme for the inside approximation (Chin 1998; Tenenhaus et al. 2005). Moreover, we used nonparametric bootstrapping (Chin 1998; Efron and Tibshirani 1993; Tenenhaus et al. 2005), as implemented in PLS Graph 3.0, with 500 replications and construct level changes preprocessing to obtain the standard errors of the estimates. The higher-order latent variables were set up through the repeated use of the manifest variables of the lower-order latent variables. We constructed the reflective, hierarchical construct model in PLS path modeling using the four key steps outlined in Table 1.

(1) We constructed the first-order latent variables (LV1-LV7) and related them to their respective block of manifest variables using mode A (reflective) in their outer model.

(2) The second-order latent variables (LV8-LV10) can now be constructed by relating them to the blocks of the underlying first-order latent variables using Mode A (reflective) in their outer model. For LV8 (aesthetics) this means the blocks of LV1 (visual appeal) and LV2 (entertainment), for LV9 (playfulness) the blocks of LV3 (escapism) and LV4 (enjoyment), and for LV10 (customer ROI) the blocks of LV6 (efficiency) and LV7 (economic value). The inner model between the second-order latent variables (LV8-LV10) and the first-order latent variables (LV1-LV7) represents the second-order loadings. LV5 (service excellence) is a first-order latent variable and is hypothesized to be not related to any of the second-order latent variables.

(3) The third-order latent variables are now constructed by setting up an outer model consisting of the blocks of manifest variables of the second-order latent variables. For LV11 (hedonic value), this means the blocks of LV8 (aesthetics; LV1 and LV2 at the first-order level) and LV9 (playfulness; LV3 and LV4 at the first-order level) are used to set up the outer model using Mode A. For LV12 (utilitarian value), this amounts to the blocks of LV5 (service excellence) and LV10 (customer ROI; LV6 and LV7 at the first-order level). The inner model between the second-order and third-order latent variables represents the third-order loadings. LV13 (experiential value) is constructed by relating it to the blocks of the third-order level latent variables LV11 (hedonic value) and LV12 (utilitarian value). For LV13 this means that an outer model is set up using all of the blocks of the first-order latent variables (LV1-LV7). The inner model between the third-order and fourth-order latent variables represents the fourth-order loadings.

<table><tr><td>Construct</td><td>Item</td><td>Loading</td><td>CR</td><td>AVE</td></tr><tr><td colspan="2">EXPERIENTIAL VALUE (Mathwick, Malhotra, and Rigdon 2001)</td><td></td><td></td><td></td></tr><tr><td rowspan="3">Visual Appeal</td><td>The way X displays its products is attractive [ $MV_1$ ]</td><td>0.82</td><td>0.90</td><td>0.75</td></tr><tr><td>X&#x27;s Internet site is aesthetically appealing [ $MV_2$ ]</td><td>0.88</td><td></td><td></td></tr><tr><td>I like the way X&#x27;s Internet site looks [ $MV_3$ ]</td><td>0.90</td><td></td><td></td></tr><tr><td rowspan="3">Entertainment Value</td><td>I think X&#x27;s Internet site is very exciting [ $MV_4$ ]</td><td>0.79</td><td>0.88</td><td>0.70</td></tr><tr><td>The enthusiasm of X&#x27;s Internet site is catching; it picks me up [ $MV_5$ ]</td><td>0.88</td><td></td><td></td></tr><tr><td>X doesn&#x27;t just sell products; it entertains me [ $MV_6$ ]</td><td>0.84</td><td></td><td></td></tr><tr><td rowspan="3">Escapism</td><td>Shopping from X&#x27;s Internet site &quot;gets me away from it all&quot; [ $MV_7$ ]</td><td>0.76</td><td>0.85</td><td>0.65</td></tr><tr><td>Shopping from X makes me feel like I am in another world [ $MV_8$ ]</td><td>0.80</td><td></td><td></td></tr><tr><td>I get so involved when I shop from X that I forget everything else [ $MV_9$ ]</td><td>0.85</td><td></td><td></td></tr><tr><td rowspan="2">Intrinsic Enjoyment</td><td>I enjoy shopping from X&#x27;s Internet site for its own sake, not just for the items I may have purchased [ $MV_{10}$ ]</td><td>0.88</td><td>0.86</td><td>0.76</td></tr><tr><td>I shop from X&#x27;s Internet site for the pure enjoyment of it [ $MV_{11}$ ]</td><td>0.87</td><td></td><td></td></tr><tr><td rowspan="2">Excellence</td><td>When I think of X, I think of excellence [ $MV_{12}$ ]</td><td>0.87</td><td>0.86</td><td>0.76</td></tr><tr><td>I think of X as an expert in the merchandise it offers [ $MV_{13}$ ]</td><td>0.87</td><td></td><td></td></tr><tr><td rowspan="3">Efficiency</td><td>Shopping from X is an efficient way to manage my time [ $MV_{14}$ ]</td><td>0.80</td><td>0.84</td><td>0.64</td></tr><tr><td>Shopping from X&#x27;s Internet site makes my life easier [ $MV_{15}$ ]</td><td>0.78</td><td></td><td></td></tr><tr><td>Shopping from X&#x27;s Internet site fits with my schedule [ $MV_{16}$ ]</td><td>0.82</td><td></td><td></td></tr><tr><td rowspan="3">Economic Value</td><td>X products are a good economic value [ $MV_{17}$ ]</td><td>0.81</td><td>0.87</td><td>0.67</td></tr><tr><td>Overall, I am happy with X&#x27;s prices [ $MV_{18}$ ]</td><td>0.97</td><td></td><td></td></tr><tr><td>The prices of the product(s) I purchased from X&#x27;s Internet site are too high, given the quality of the merchandise [ $MV_{19}$ ]</td><td>0.80</td><td></td><td></td></tr><tr><td colspan="2">E-LOYALTY (Srinivasan, Anderson, and Ponnavolu 2002)</td><td></td><td></td><td></td></tr><tr><td rowspan="3">Attitudinal Loyalty</td><td>I like using this website [ $MV_{20}$ ]</td><td>0.73</td><td>0.85</td><td>0.66</td></tr><tr><td>To me, this is the best retail website to do business with [ $MV_{21}$ ]</td><td>0.84</td><td></td><td></td></tr><tr><td>I belief that this is my favorite retail website [ $MV_{22}$ ]</td><td>0.87</td><td></td><td></td></tr><tr><td rowspan="3">Behavioral Loyalty</td><td>I seldom consider switching to another website [ $MV_{23}$ ]</td><td>0.82</td><td>0.82</td><td>0.61</td></tr><tr><td>As long as the present service continues, I doubt that I would switch to another website [ $MV_{24}$ ]</td><td>0.78</td><td></td><td></td></tr><tr><td>I try to use this website whenever I need to make a purchase [ $MV_{25}$ ]</td><td>0.74</td><td></td><td></td></tr></table>

$^{\dagger}$ α = coefficient alpha; CR = composite reliability; AVE = average variance extracted

(4) Finally, the hierarchical model can now be estimated using PLS path modeling. We obtain estimates for the first-order loadings, second-order loadings, third-order loadings, fourth-order loadings, and structural parameters. A nonparametric bootstrapping procedure may be used to obtain standard error and calculate t statistics for inferential purposes. The psychometric properties of the latent variables and the structural relationships can now be assessed.

A graphical representation of the procedure is provided in Figure 2.

To assess the psychometric properties of the measures, we initially specified a null model for the first-order latent variables, in which we included no structural relationships. To assess the reliability of the measures, we calculated the composite scale reliability (CR; Chin 1998; Fornell and Larcker 1981; Werts et al. 1974) and average variance extracted (AVE; Chin 1998; Fornell and Larcker 1981). As we show in Table 2, the CR exceed 0.80, and the AVE of all measures compellingly exceeds the cut-off value of 0.50 proposed by Fornell and Larcker (1981); the lowest AVE is 0.61 in the null model. Moreover, as we show in Table 3, the square root of the AVE exceeds the intercorrelations of the construct with the other constructs in the model, in support of discriminant validity (Barclay et al. 1995; Chin 1998; Fornell and Larcker 1981; Hulland 1999). Additional support for discriminant validity comes through inspection of the cross-loadings, which are not substantial in magnitude compared with the loadings (Chin 1998; Fornell and Bookstein 1982; Hulland 1999).

![](/api/attachments/PVNHXUWZ/fulltext/images/7c2a69edad84e20a276890fcbac6463abbfc66f08ea4e97a5e78fda0e0022c5f.jpg)  
Figure 2. Designing a Higher-Order Model in PLS Using Repeated Indicators

Table 3. Intercorrelations of the Latent Vairalbes for First-Order Constructs $^{†}$

<table><tr><td colspan="2">Construct</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><td>1.</td><td>Visual Appeal</td><td>0.87</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2.</td><td>Entertainment</td><td>0.65</td><td>0.84</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3.</td><td>Escapism</td><td>0.31</td><td>0.62</td><td>0.81</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4.</td><td>Enjoyment</td><td>0.27</td><td>0.57</td><td>0.70</td><td>0.87</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5.</td><td>Excellence</td><td>0.59</td><td>0.56</td><td>0.37</td><td>0.38</td><td>0.87</td><td></td><td></td><td></td><td></td></tr><tr><td>6.</td><td>Efficiency</td><td>0.32</td><td>0.26</td><td>0.21</td><td>0.20</td><td>0.46</td><td>0.80</td><td></td><td></td><td></td></tr><tr><td>7.</td><td>Economic Value</td><td>0.34</td><td>0.21</td><td>0.05</td><td>-0.03</td><td>0.41</td><td>0.32</td><td>0.82</td><td></td><td></td></tr><tr><td>8.</td><td>Attitudinal Loyalty</td><td>0.62</td><td>0.56</td><td>0.49</td><td>0.42</td><td>0.63</td><td>0.43</td><td>0.34</td><td>0.81</td><td></td></tr><tr><td>9.</td><td>Behavioral Loyalty</td><td>0.34</td><td>0.41</td><td>0.45</td><td>0.34</td><td>0.43</td><td>0.35</td><td>0.32</td><td>0.63</td><td>0.78</td></tr></table>

$^{\dagger}$ Square root of the AVE on the diagonal.

In Table 4, we include the CRs and AVE of the measures in the higher-order models; these also show CRs equal to or greater than 0.80 and AVE greater than 0.65, which provides evidence of reliable measures. As we demonstrate in Table 4, the loadings of the first-order latent variables on the second-order factors exceed 0.8. Similarly, the loadings of the second-order latent variables on the third-order latent variables are equal to or exceed 0.80. Finally, the loading of hedonic value on online experiential value equals 0.93, and the loading of utilitarian value on online experiential value is 0.78, which is in support of the fourth-order model of online experiential value. Our results indicate that all loadings are significant at $\alpha = 0.01$ .

## Assessing the Hierarchical Construct in a Structural Model

To assess the nomological validity of our hierarchical construct model we embedded online experiential value in a nomological network with attitudinal and behavioral e-loyalty. We find support for $H_{1a}$ , $H_{1b}$ , and $H_{2}$ (see Table 3). We find a significant, positive impact of online experiential value on attitudinal e-loyalty ( $H_{1a}$ : $\beta = 0.75 [0.69, 0.85]$ , p < 0.01) $^{5}$ and on behavioral e-loyalty ( $H_{1b}$ : $\beta = 0.17 [0.01, 0.34]$ , p < 0.05). As demonstrated in Table 3, we also find a strong positive relationship between attitudinal e-loyalty and behavioral e-loyalty ( $H_{2}$ : $\beta = 0.50 [0.35, 0.65]$ , p < 0.01). The variance explained by the model in terms of $R^{2}$ is 0.57 for attitudinal e-loyalty and 0.42 for behavioral e-loyalty.

According to the effect sizes defined for $R^{2}$ by Cohen (1988), these effects can be classified as large ( $f^{2}>0.35$ ).

We also tested for a mediation effect of attitudinal e-loyalty in the relationship between online experiential value and behavioral e-loyalty (Baron and Kenny 1986; Holmbeck 1997). As suggested by Holmbeck (1997), we first estimated a model containing only the (direct) effect of online experiential value on behavioral e-loyalty ( $\beta = 0.56, p < 0.01$ ; $R^2 = 0.31$ ). We can now compare this model to the parameter estimates in our conceptual model. Our results suggest that the impact of the direct effect declines ( $\beta = 0.17, p < 0.05$ ) by the inclusion of the indirect effect through the mediator, attitudinal e-loyalty. Using an incremental $F$ test we can test whether including the direct effect of online experiential value on behavioral e-loyalty significantly increases the variance explained for behavioral e-loyalty. Our results suggest a significant impact of the direct effect on the variance explained in behavioral e-loyalty, albeit with a fairly small effect size ( $\Delta R^2 = 0.012, f^2 = 0.02$ , $F_{1,187} = 3.99$ , $p < 0.05$ ). Furthermore, we find that the indirect association between online experiential value and behavioral e-loyalty ( $\beta_{indirect} = 0.38, z = 5.82, p < 0.001$ ) is greater in magnitude than their direct association ( $\beta_{direct} = 0.17, p < 0.05$ ; Baron and Kenny 1986; MacKinnon et al. 2002). To obtain the standard error for the indirect effect we used the bootstrap method suggested by Shrout and Bolger (2002), which seems to be more appropriate for PLS than Sobel's (1982) large sample test. These results provide support for the partially mediating role of attitudinal e-loyalty between online experiential value and behavioral e-loyalty.

Recently, a global fit measure for PLS path modeling has been suggested (Tenenhaus et al. 2005), $GoF$ ( $0 \leq GoF \leq 1$ ), defined as the geometric mean of the average communality and average $R^2$ (for endogenous constructs). Because communality equals AVE in the PLS path modeling approach, we propose a cut-off value of 0.5 for communality, as suggested by Fornell and Larcker (1981). Moreover, in line with the effect sizes for $R^2$ (small: 0.02; medium: 0.13; large: 0.26) proposed by Cohen (1988), we derive the following $GoF$ criteria for small, medium, and large effect sizes of $R^2$ by substituting the minimum average AVE of 0.50 and the effect sizes for $R^2$ in the equation defining $GoF$ ( $GoF = \sqrt{A\overline{VE} * \overline{R}^2}$ ); $GoF_{small} = 0.1$ , $GoF_{medium} = 0.25$ , and $GoF_{large} = 0.36$ . These may serve as baseline values for validating the PLS model globally. For the complete model (see Table 3), we obtained a $GoF$ value of 0.5989, which exceeds the cut-off value of 0.36 for large effect sizes of $R^2$ and allows us to conclude that our model performs well compared to the baseline values defined above. Finally, the $GoF$ can be calculated both for components-based SEM as well covariance-based SEM.

<table><tr><td colspan="5">Hierarchical ModelSecond-Order Model</td></tr><tr><td></td><td>Aesthetics</td><td>Playfulness</td><td>Service  $Excellence^b$ </td><td>Customer ROI</td></tr><tr><td>CR</td><td>0.92</td><td>0.92</td><td>n.a.</td><td>0.80</td></tr><tr><td>AVE</td><td>0.86</td><td>0.86</td><td>n.a.</td><td>0.67</td></tr><tr><td>Visual Appeal</td><td> $0.91^{**} [0.88, 0.94]^c$ </td><td></td><td>n.a.</td><td></td></tr><tr><td>Entertainment</td><td> $0.91^{**} [0.89, 0.94]$ </td><td></td><td>n.a.</td><td></td></tr><tr><td>Escapism</td><td></td><td> $0.95^{**} [0.93, 0.96]$ </td><td>n.a.</td><td></td></tr><tr><td>Enjoyment</td><td></td><td> $0.90^{**} [0.87, 0.93]$ </td><td>n.a.</td><td></td></tr><tr><td>Efficiency</td><td></td><td></td><td>n.a.</td><td> $0.81^{**} [0.72, 0.87]$ </td></tr><tr><td>Economic Value</td><td></td><td></td><td>n.a.</td><td> $0.83^{**} [0.76, 0.87]$ </td></tr><tr><td colspan="5">Third-Order Model</td></tr><tr><td></td><td>Hedonic Value</td><td>Utilitarian Value</td><td></td><td></td></tr><tr><td>CR</td><td>0.86</td><td>0.86</td><td></td><td></td></tr><tr><td>AVE</td><td>0.76</td><td>0.76</td><td></td><td></td></tr><tr><td>Aesthetics</td><td> $0.90^{**} [0.86, 0.93]$ </td><td></td><td></td><td></td></tr><tr><td>Playfulness</td><td> $0.84^{**} [0.79, 0.88]$ </td><td></td><td></td><td></td></tr><tr><td>Excellence</td><td></td><td> $0.80^{**} [0.74, 0.86]$ </td><td></td><td></td></tr><tr><td>Customer ROI</td><td></td><td> $0.94^{**} [0.90, 0.96]$ </td><td></td><td></td></tr><tr><td colspan="5">Fourth-Order Model</td></tr><tr><td></td><td>Experiential Value</td><td></td><td></td><td></td></tr><tr><td>CR</td><td>0.85</td><td></td><td></td><td></td></tr><tr><td>AVE</td><td>0.74</td><td></td><td></td><td></td></tr><tr><td>Hedonic Value</td><td> $0.93^{**} [0.90, 0.95]$ </td><td></td><td></td><td></td></tr><tr><td>Utilitarian Value</td><td> $0.78^{**} [0.69, 0.82]$ </td><td></td><td></td><td></td></tr><tr><td colspan="5">Structural Model</td></tr><tr><td></td><td>Attitudinal Loyalty</td><td>Behavioral Loyalty</td><td></td><td></td></tr><tr><td> $Hedonic Valued$ </td><td> $0.70^{**} [0.64, 0.80]$ </td><td> $0.51^{**} [0.43, 0.62]$ </td><td></td><td></td></tr><tr><td> $Utilitarian Valued$ </td><td> $0.59^{**} [0.50, 0.68]$ </td><td> $0.44^{**} [0.34, 0.52]$ </td><td></td><td></td></tr><tr><td>Experiential Value</td><td> $H_{1a}: 0.75^{**} [0.69, 0.85]$ </td><td> $H_{1b}: 0.17^{**} [0.01, 0.34]$ </td><td></td><td></td></tr><tr><td>Attitudinal Loyalty</td><td></td><td> $H_2: 0.50^{**} [0.35, 0.65]$ </td><td></td><td></td></tr><tr><td> $R^2$ </td><td> $0.57^{**}$ </td><td> $0.42^{**}$ </td><td></td><td></td></tr></table>

$^{a*}$ p < 0.05; $^{**}$ p < 0.01; n.s. = not significant.  
$^{b}$ Service excellence is specified as a first-order factor in the null model. However, in the hierarchical model, service excellence constitutes a second-order factor.  
$^{c}$ Percentile estimate of 95% confidence interval (Efron and Tibshirani 1993).  
$^{d}$ Total effects between utilitarian value and attitudinal and behavioral loyalty and hedonic value and attitudinal and behavioral loyalty.

In addition to the direct effects of the fourth-order construct, online experiential value, on attitudinal and behavioral loyalty, we can also derive the indirect effects of the third-order constructs, hedonic and utilitarian value, on attitudinal and behavioral e-loyalty. We use the product of the loading of hedonic and utilitarian value on online experiential value and the coefficient that represents the effect of online experiential value on attitudinal e-loyalty (Edwards 2001). As Table 3 demonstrates, the indirect effect between hedonic value and attitudinal e-loyalty is $0.93 * 0.75 = 0.70$ ( $z = 18.24$ , $p < 0.001$ ), whereas that between utilitarian value and attitudinal e-loyalty is $0.78 * 0.75 = 0.59$ ( $z = 12.87$ , $p < 0.01$ ). The same procedure can be followed to derive the indirect effect between hedonic and utilitarian value and behavioral e-loyalty. The total effect of hedonic value on behavioral e-loyalty is $0.51$ ( $z = 10.55$ , $p < 0.01$ ), and the total effect of utilitarian value on behavioral e-loyalty is $0.43$ ( $z = 9.13$ , $p < 0.01$ ). Obviously, this approach also works for lower order constructs and formative constructs (Edwards 2001).

Marcoulides and Saunders (2006, p. viii) have cautioned IS researchers using PLS path modeling: “PLS is not a silver bullet to be used with samples of any size.” Consequently, they have strongly recommended that the power of the study should be assessed and recommended. The power $(1-\beta)$ of a test is defined as the probability of rejecting a false $H_{0}$ ; power constitutes the complement to type II error $(\beta;$ Baroudi and Orlikowski 1989; Cohen 1992). As a convention for behavioral research a value of 0.80 is used for power (Baroudi and Orlikowski 1989; Cohen 1988 1992). We used the PWR package (Champely 2007) in R to conduct the power calculations. R is an open source programming language and software environment for statistical computing and graphics (R Development Core Team 2007). Our results revealed that the power for all the parameters in our conceptual model exceeds 0.99. $^{7}$

## Application of the Guidelines

Building on the original conceptualization by Mathwick et al. (2001), all of the relationships in the hierarchical structure representing experiential value were reflective (or mode A;

Chin 1998; molecular model, Chin and Gopal 1995). These relationships, however, could also be specified as formative (or mode B, Chin 1998; molar model, Chin and Gopal 1995) or a mix of formative and reflective relationships (Edwards 2001; Jarvis et al. 2003). In covariance-based SEM, this would require constraints, which would not allow identification for the construct per se, except by adding reflective indicators or relating it to at least two unrelated constructs (Jarvis et al. 2003; MacCallum and Browne 1993). The latter is rather awkward in a higher-order model and the former is conceptually unappealing.

The PLS path modeling approach proposed in this paper can also be applied to formative relationships in the higher-order structure. PLS path modeling can also be used for hierarchical models with formative constructs or a mix of formative and reflective constructs. For the first-order level latent variables, this could be accomplished by using mode B instead of mode A. For the higher-order constructs, the direction of the relationships will need to be reversed (Lohmöller 1989; Noonan and Wold 1983; Tenenhaus et al. 2005; Wold 1982). However, this will result in a $R^2$ value of the higher order construct of unity. This is similar to Diamantopolous and Winklhofer's (2001) suggestion to set the error term to zero to obtain identification in a covariance-based SEM context. Obviously, relating a reflective higher-order construct to this formative construct, or using the formative construct as an effect, would be superfluous as all variance has been explained by the lower-order formative constructs.

Moreover, the relationship between experiential value and attitudinal and behavioral loyalty would not be affected by reversing the relationships in the hierarchical structure (e.g., changing all of the reflective relationships to formative relationships); however, the weights obtained in the formative mode could be used to assess the impact of the lower-order constructs on the higher-order constructs. Finally, the choice for formative or reflective is and remains a substantive one (Diamantopolous and Winklhofer 2001; Jarvis et al. 2003, MacKenzie et al. 2005; Petter et al. 2007) and for experiential value the literature review indicates an all reflective approach for the hierarchical structure (see Mathwick et al. 2001). Interested readers should consult Petter et al. (2007) for guidance regarding the assessment and analysis of formative constructs in the IS field.

## Discussion and Implications

The main objective of this study was to demonstrate that PLS path modeling can be used to assess hierarchical models. We provided an empirical illustration by using data from an online retail setting and develop a detailed set of guidelines for constructing a hierarchical model using PLS path modeling. The application of PLS path modeling to hierarchical construct models makes it possible to extend the theoretical contributions of the original study. Our results provide empirical support for the third- and fourth-order latent variable model. Our empirical study also illustrates that higher order constructs can be incorporated in structural models as we provide empirical evidence of the positive impact of online experiential value on attitudinal and behavioral e-loyalty. The fourth-order reflective hierarchical construct model reveals that online experiential value is an important driver of online attitudinal and behavioral loyalty.

Covariance-based SEM and components-based SEM, or PLS path modeling, should be regarded as complementary methods. It is the objective of covariance-based SEM to minimize the (maximum likelihood) fitting function between the sample covariance matrix and the (parameter) implied covariance matrix. For PLS path modeling, on the other hand, parameter estimates are obtained to minimize the residual variance of all dependent variables (manifest and latent variables). However, there might be conditions under which PLS path modeling might outperform covariance-based SEM for assessing hierarchical construct models.

The identification of reflective hierarchical models using covariance-based SEM is not an easy task. Even if the model per se is theoretically identified, it might still suffer from empirical underidentification, which may cause nonconvergence and/or improper solutions. For formative hierarchical construct models, or hierarchical construct models with a mix of formative and reflective constructs, the challenges might even prove more formidable in that respect. PLS path modeling is not as susceptible to identification problems and improper solutions as covariance-based SEM. As far as hierarchical construct models are concerned, we have provided practical guidelines to construct higher-order latent variables using PLS path modeling. We have demonstrated the use of these guidelines in an empirical illustration of a reflective, fourth-order model embedded in a nomological network. Finally, we have discussed the extension of the guidelines to hierarchical construct models beyond the scope of the empirical illustration.

Using a Monte Carlo simulation, Cassell et al. (1999) show that PLS path modeling is quite robust to deviations from normality, except for highly skewed distributions.

If higher-order constructs are embedded in a nomological network, either as cause or effect, model complexity might be an additional factor in the trade-off between covariance-based

SEM and PLS path modeling. Although only used for instructional purposes, neither Edwards (2001) nor Law and Wong (1999) specify a total disaggregation model for their multidimensional constructs, be they reflective or formative, but rely on a first-order partial aggregation model, in which the aggregated mean over the manifest variables of the first-order latent variables are used as “manifest” variables for the second-order latent variables (Bagozzi and Edwards 1999), thus potentially confounding the (measurement) error term (at the manifest variable level) and the disturbance, or residual, term (at the latent variable level). Model complexity does not pose as severe a restriction to PLS path modeling as to covariance-based SEM, since PLS path modeling at any moment only estimates a subset of parameters, hence partial least squares. Consequently, PLS path modeling would be more suitable to more complex models including models with hierarchical constructs (with a total disaggregation approach), mediating effects and moderating effects (see Chin et al. 2003).

The analysis of formative constructs in covariance-based SEM is not an easy task, as it involves identification rules, which make its application rather difficult, especially for multidimensional or hierarchical models. PLS path modeling generally allows for the easy handling of formative constructs. Although the biasing effects of incorrectly specifying formative constructs as reflective are well documented (Jarvis et al. 2003), in their review of the IS literature, Petter et al. (2007) report that 30 percent of the constructs are incorrectly specified. In response to this, they have provided a roadmap (p. 642) for IS researchers to identify formative constructs, assessing the validity of the measures and analyzing the model. Although we have focused on a reflective higher-order model in our empirical illustration, we have indicated that our guidelines may be extended to formative constructs. A notable example of the use of formative constructs in a multidimensional model is provided by Rai et al. (2006).

## Limitations and Suggestions for Future Research

Our empirical illustration of the use of PLS path modeling constitutes only a single study with limited generalizability. Therefore, we hope that our exposition and guidelines will assist researchers with future applications of PLS path modeling for hierarchical construct models. It would be useful for future research to compare PLS path modeling versus covariance-based SEM and compare the performance under a number of different conditions (sample size, model complexity, number of manifest variables per latent variables, distributional properties of the manifest variables, the direction of the relationship between manifest and latent variables including potential incorrect specification, missing data, etc.).

To compare results across contexts, multi-sample analysis is quite frequently used in covariance-based SEM (e.g., Vandenberg and Lance 2000). Comparison across contexts or groups might very well contribute to the generalizability of findings. Multi-sample analysis can be applied in PLS path modeling using a t test to compare parameter estimates across samples (see Duxbury and Higgins 1991). However, the use of asymptotic (i.e., large sample) tests is not quite adequate for PLS path modeling. Therefore, Chin and Dibbern (2009) propose a permutation-based approach to multi-sample analysis in PLS path modeling.

The main advantage of covariance based SEM over PLS path modeling is the use of formal testing procedures allowing for the assessment of the validity of global model fit (Bollen 1989; Chin 1998; Tenenhaus et al. 2005). For hierarchical construct models, we cannot only assess the model fit by using these formal testing procedures, we can also test different (alternative) nested models (Edwards 2001; Marsh and Hocevar 1985; Rindskopf and Rose 1988). For example, the second-order model is nested in the first-order, group factor model. By applying the appropriate restrictions and comparing the model fit, the appropriateness of the restrictions can be assessed (Rindskopf and Rose 1988).

For PLS path modeling this approach is unfortunately not possible, and consequently the validity of the model cannot be globally assessed in PLS path modeling. The GoF proposed by Tenenhaus et al. (2005) mainly serves a diagnostic value and cannot be employed in that respect. However, the application of the Schmid-Leiman solution (Schmid and Leiman 1957) might provide useful diagnostic information. The Schmid-Leiman solution allows us to assess the variance explained by the different levels of latent variables in our hierarchical model. Applying the Schmid-Leiman solution to our empirical illustration, we find that almost 70 percent of the variance explained can be attributed to the higher-order factors (second-order and upward; Wolf and Preising 2005). $^{8}$ Unfortunately, this approach only applies to reflective hierarchical construct models.

We modeled hierarchical construct models by repeated use of manifest variables. However, as latent variable scores are determinate in PLS path modeling, we could also conceive of an approach in which latent variable scores are obtained for the lower-order latent variables in a sequential fashion and used as manifest variables for the higher-order latent variables. We would need to explore how this sequential latent variable score method compares to the repeated use of manifest variables. Furthermore, we would need to assess the underlying assumptions and guidelines for the use of this approach. $^{9}$

The use of actual data sets should be complemented by Monte Carlo simulations (see Paxton et al. 2001). Monte Carlo simulations might prove an interesting tool to explore the impact of improper solutions in covariance-based SEM for hierarchical models and the potential for PLS path modeling to serve as a remedy to this problem. A Monte Carlo simulation would allow us to compare the performance of covariance-based SEM versus PLS path modeling for hierarchical construct models. It would be interesting to contrast the performance of covariance-based SEM with the repeated use of manifest indicators approach and the latent variable score approach in PLS path modeling. For the Monte Carlo simulations, we would need to assess convergence, the accuracy of the parameter estimates, statistical power, and model fit of hierarchical construct models under a number of different conditions, such as the number of levels in the hierarchical model, the number of manifest and/or latent variables (model complexity), the number of manifest variables per latent variable, distributional properties of the manifest variables, measurement levels of the manifest variables, the use of reflective or formative constructs, the reliability of measures, and missing data patterns. EQS 6.1 (Bentler 2004) might be very useful to conduct these Monte Carlo simulations, as it applies restrictions to parameter estimates to avoid improper solutions (see Paxton et al. 2001). Furthermore, EQS 6.1 provides an overview of the number of simulations that successfully converge and indicates the condition code if simulations do not successfully converge. This might provide important diagnostic information in the case of hierarchical construct models. Finally, EQS 6.1 allows for the generation of non-normal data, the inclusion of contamination effects, the application of nonparametric bootstraps and the use of missing data patterns.

## Acknowledgments

The authors would like to thank three anonymous reviewers and the special issue editorial team, Carol Saunders, George Marcoulides, and Wynne Chin, for their constructive and encouraging comments. We feel that our paper has greatly benefitted from the review process.

The authors thank Elisabeth Brüggen, June Cotte, and Charla Mathwick for their valuable comments and suggestions on previous drafts of this paper and Wendy van der Klein for her assistance in the data collection stage. Finally, we would like to thank Hans-Georg Wolf for providing us with the SPSS syntax code for the fourth-order Schmid-Leiman solution.

## References

Ajzen, I. 1991. “The Theory of Planned Behavior,” Organizational Behavior & Human Decision Processes (50:2), pp. 179-211.

Babin, B. J., Darden W. R., and Griffin, M. 1994. “Work and/or Fun: Measuring Hedonic and Utilitarian Shopping Value,” Journal of Consumer Research (20:1), pp. 644-656.

Bacharach, S. B. 1989. “Organizational Theories: Some Criteria for Evaluation,” The Academy of Management Review (14:4), pp. 496-515.

Bagozzi, R. P., and Edwards, J. R. 1999. “A General Approach for Representing Constructs in Organizational Research,” Organizational Research Methods (1:1), pp. 45-87.

Barclay, D. W., Higgins, C., and Thompson, R. 1995. “The Partial Least Square (PLS) Approach to Causal Modeling: Personal Computer Adoption and Use as an Illustration,” Technology Studies (2:2), pp. 285-309.

Baron, R. M., and Kenny, D. A. 1986. “The Moderator-Mediator Variable Distinction in Social Psychological Research: Conceptual, Strategic and Statistical Considerations,” Journal of Personality and Social Psychology (51:6), pp. 1173-1182.

Baroudi, J., and Orlikowski, W. 1989. “The Problem of Statistical Power in MIS Research,” MIS Quarterly (13:1), pp. 87-106.

Bentler, P. M. 2004. EQS 6 Structural Equations Program Manual, Encino, CA: Multivariate Software, Inc.

Bollen, K. A. 1989. Structural Equations with Latent Variables, New York: Wiley.

Bollen, K. A., and Lennox, R. 1991. “Conventional Wisdom on Measurement: A Structural Equation Perspective. Psychological Bulletin (110:2), pp. 305-314.

Cassel, C., Hackl, P., and Westlund, A. 1999. “Robustness of Partial Least-Squares Method for Estimating Latent Variable Quality Structures,” Journal of Applied Statistics (26:4), pp. 435-446.

Champely, S. 2007. PWR: Basic Functions for Power Analysis, R Package Version 1.1.

Chaudhuri, A., and Holbrook, M. B. 2001. “The Chain of Effects from Brand Trust and Brand Affect to Brand Performance: The Role of Brand Loyalty,” Journal of Marketing (65:2), pp. 81-93.

Chen, F., Bollen, K. A., Paxton, P., Curran, P. J., and Kirby, J. B. "Improper Solutions in Structural Equation Models: Causes, Consequences, and Strategies." Sociological Methods and Research (29:4), pp. 468-508.

Chin, W. W. 1998. “The Partial Least Squares Approach to Structural Equation Modeling,” in Modern Business Research Methods, G. A. Marcoulides (ed.), Mahwah, NJ: Lawrence Erlbaum Associates, pp. 295-336.

Chin, W. W. 2001. PLS - Graph User's Guide Version 3.0., Houston, TX: Soft Modeling Inc.

Chin, W. W., and Dibbern, J. 2009. “A Permutation Based Procedure for Multi-Group PLS Analysis: Results of Tests of Differences on Simulated Data and a Cross of Information System Services between Germany and the USA,” in V. E. Vinzi, W. W. Chin, J. Henseler, and H. Wang (eds), Handbook of Partial Least Squares: Concepts, Methods and Applications in Marketing and Related Fields, Berlin: Springer.

Chin, W. W., and Gopal, A. 1995. “Adoption Intention in GSS: Relative Importance of Beliefs,” Data Base Advances (26:2/3), pp. 42-64.

Chin, W. W., Marcolin, B. L., and Newsted, P. R. 2003. “A Partial Least Squares Latent Variable Modeling Approach for Measuring Interaction Effects: Results from a Monte Carlo Simulation Study and an Electronic-Mail Emotion/Adoption Study,” Information Systems Research (14:2), pp. 189-217.

Chin, W. W., and Newsted, P. R. 1999. “Structural Equation Modeling analysis with Small Samples Using Partial Least Squares,” in R. Hoyle (ed.), Statistical Strategies for Small Sample Research, Thousand Oaks, CA: Sage Publications, pp. 307-341.

Cohen, J. 1988. Statistical Power Analysis for the Behavioral Sciences, Hillsdale, NJ: Lawrence Erlbaum Associates.

Cohen, J. 1992. “A Power Primer,” Psychological Bulletin (112:1), pp. 155-159.

DeCarlo, L. T. 1997. “On the Meaning and Use of Kurtosis,” Psychological Methods (2:3), pp. 292-307.

Diamantopoulos, D., and Winklhofer, H. 2001. “Index Construction with Formative Indicators: An Alternative to Scale Development,” Journal of Marketing Research (38:2), pp. 269-277.

Dillon, W. R., Kumar, A., and Mulani, N. 1987. “Offending Estimates in Covariance Structure Analysis: Comments on Causes and Solutions to Heywood Cases,” Psychological Bulletin (101:1), pp.126-135.

Duxbury, L. E., and Higgins, C. A. 1991. “Gender Differences in Work-Family Conflict,” Journal of Applied Psychology (76:1), pp. 60-74.

Edwards, J. R. 2001. “Multidimensional Constructs in Organizational Behavior Research: An Integrative Analytical Framework,” Organizational Research Methods (4:2), pp.144-192.

Edwards, J. R., and Bagozzi, R. P. 2000. “On the Nature and Direction of the Relationship between Constructs and Measures,” Psychological Methods (5:2), pp. 155-174.

Efron, B., and Tibshirani, R. J. 1993. An Introduction to the Bootstrap, New York: Chapman and Hall.

Fischer, C. D. 1980. “On the Dubious Wisdom of Expecting Job Satisfaction to Correlate with Performance,” Academy of Management Review (5:4), pp. 607-612.

Fornell, C., and Bookstein, F. L. 1982. “Two Structural Equations Models: LISREL and PLS Applied to Consumer Exit-Voice Theory,” Journal of Marketing Research (19:4), pp. 440-452.

Fornell, C., and Larcker, D. F. 1981. “Evaluating Structural Equation Models with Unobservable Variables and Measurement Error,” Journal of Marketing Research (18:1), pp. 39-50.

Fu, J.-R. 2007. VisualPLS, Release 1.04 (beta), National Kaoshing University of Applied Sciences, Taiwan (available online at http://fs.mis.kuas.edu.tw/\~fred/vpls).

Gorsuch, R. L. 1983. Factor Analysis, Hillsdale, NJ: Lawrence Erlbaum Associates.

Guinot, C., Latreille, J., and Tenenhaus, M. 2001. “PLS Path Modeling and Multiple Table Analysis: Application to the Cosmetic Habits of Women in Ile-de-France,” Chemometrics and Intelligent Laboratory Systems (58:2), pp. 247-259.

Holbrook, M. B. 1994. “The Nature of Customer Value: An Axiology of Services in the Consumption Experience,” in Service Quality: New Directions in Theory and Practice, R. T. Rust and R. L. Oliver (eds.), Newbury Park, CA: Sage Publications, pp. 21-71.

Holbrook, M. B., and Hirschman, E. C. 1982. “The Experiential Aspects of Consumption: Consumer Fantasies, Feelings, and Fun,” Journal of Consumer Research (9:3), pp.132-140.

Holmbeck, G. N. 1997. “Toward Terminological, Conceptual, and Statistical Clarity in the Study of Mediators and Moderators: Examples from the Child-Clinical and Pediatric Psychology Literatures,” Journal of Counseling and Clinical Psychology (65:4), pp. 599-610.

Hulland, J. 1999. “Use of Partial Least Squares (PLS) in Strategic Management Research: A Review of Four Recent Studies,” Strategic Management Journal (20:2), pp. 195-204.

Hunter, J. E., and Gerbing, D. W. 1982. “Unidimensional Measurement, Second-Order Factor Analysis and Causal Models,” in Research in Organizational Behavior, B. M. Staw and L. L. Cummings (eds.), Amsterdam: Elsevier B.V., pp. 267-320.

Jarvis, D., MacKenzie, S., and Podsakoff, P. 2003. “A Critical Review of Construct Indicators and Measurement Model Misspecification in Marketing and Consumer Research,” Journal of Consumer Research (30:3), pp. 199-218.

Kim, S., and Stoel, L. 2004. “Dimensional Hierarchy of Retail Website Quality,” Information & Management (41:5), pp. 619-633.

Kwak, H., Fox, R. J., and Zinkhan, G. M. 2002. “What Products Can Be Successfully Promoted and Sold Via the Internet?,” Journal of Advertising Research (42:1), pp. 23-38.

Law, K. S., and Wong, C. 1999. “Multidimensional Constructs In Structural Equation Analysis: An Illustration Using the Job Perception and Job Satisfaction Constructs,” Journal of Management (25:2), pp. 143-160.

Law, K. S., Wong C., and Mobley, W. H. 1998. “Toward a Taxonomy of Multidimensional Constructs,” Academy of Management Review (23:4), pp. 741-755.

Lohmöller, J.-B. 1989. Latent Variable Path Modeling with Partial Least Squares, Heidelberg: Physica-Verlag.

Looney, S. W. 1995. “How to Use Tests for Univariate Normality to Assess Multivariate Normality,” American Statistician (49), pp. 64-70.

MacCallum, R. C., and Browne, M. W. 1993. “The Use of Causal Indicators in Covariance Structure Models: Some Practical Issues,” Psychological Bulletin (114:3), pp. 533-541.

MacKenzie, S. B., Podsakoff, P. M., and Jarvis, C. B. 2005. “The Problem of Measurement Model Misspecification in Behavioral and Organizational Research and Some Recommended Solutions,” Journal of Applied Psychology (90:4), pp. 710-730.

MacKinnon, D. P., Lockwood, C. M., Hoffman, J. M., West, S. G., and Sheets, V. 2002. “A Comparison of Methods to Test Mediation and Other Intervening Variable Effects,” Psychological Methods (7:1), pp. 83-104.

Marcoulides, G. A., and Saunders, C. 2006. “PLS: A Silver Bullet,” MIS Quarterly (30:2), pp. iii-ix.

Mardia, K. V. 1970. “Measures of Multivariate Skewness and Kurtosis with Applications,” Biometrika (57:3), pp. 519-530.

Marsh, H. W., and Hocevar, D. 1985. “The Application of Confirmatory Factor Analysis to the Study of the Self-Concept: First and Higher Order Factor Structures and Their Invariance Across Age Groups,” Psychological Bulletin (97:3), pp. 562-582.

Mathwick, C., Malhotra, N., and Rigdon, E. 2001. “Experiential Value: Conceptualization, Measurement and Application in the Catalog and Internet Shopping Environment,” Journal of Retailing (77:1), pp. 39-56.

Mathwick, C., Malhotra, N., and Rigdon, E. 2002. “The Effect of Dynamic Retail Experiences on Experiential Perceptions of Value: An Internet and Catalog Comparison,” Journal of Retailing (78:1), pp. 51-61.

Netemeyer, R. G., Bearden, W. O., and Sharma, S. 2003. Scaling Procedures: Issues and Applications, Thousand Oaks, CA: Sage Publications.

Noonan, R., and Wold, H. 1993. "Evaluating School Systems Using Partial Least Squares," Evaluation in Education (7), pp. 219-364.

Novak, T. P., Hoffman, D. L., and Yung, Y.-F. 2000. “Measuring the Customer Experience in Online Environments: A Structural Modeling Approach,” Marketing Science (19:1), pp. 22-42.

Paxton, P., Curran, P. J., Bollen, K. A., Kirby, J., and Chen, F. 2001. “Monte Carlo Experiments: Design and Implementation,” Structural Equation Modeling (8:2), pp. 287-312.

Petter, S., Straub, D., and Rai, A. 2007. “Specifying Formative Constructs in Information Systems Research,” MIS Quarterly (31:1), pp. 623-656.

R Development Core Team. 2007. R: A Language and Environment for Statistical Computing, R Foundation for Statistical Computing, Vienna, Austria (http://www.R-project.org).

Rai, A., Patnayakuni, R., and Seth, N. 2006. “Firm Performance Impacts of Digitally Enabled Supply Chain Integration Capabilities,” MIS Quarterly (30:2), pp. 225-246.

Rindskopf, D. 1984. “Structural Equation Models: Empirical Identification, Heywood Cases and Related Problem,” Sociological Methods and Research (13:1), pp. 109-119.

Rindskopf, D., and Rose, T. 1988. “Second Order Factor Analysis: Some Theory and Applications,” Multivariate Behavioral Research (23:1), pp. 51-67.

Schmid, J., and Leiman, J. N. 1957. “The Development of Hierarchical Factor Solutions,” Psychometrika (22), pp.53-61.

Shrout, P. E., and Bolger, N. 2002. “Mediation in Experimental and Nonexperimental Studies: New Procedures and Recommendations,” Psychological Methods (7:4), pp. 422-455

Sobel, M. E. 1982. “Asymptotic Confidence Intervals for Indirect Effects in Structural Equation Models,” in Sociological Methodology, S. Leinhardt (ed.), San Francisco: Jossey-Bass, pp. 290-313.

Srinivasan, S. S., Anderson, R., and Ponnavlu, K. 2002. “Customer Loyalty in E-Commerce: An Exploration of its Antecedents and Consequences,” Journal of Retailing (78:1), pp. 41-50.

Tenenhaus, M., Vinzi, V. E. Chatelin, Y-M., and Lauro, C. 2005. "PLS Path Modeling," Computational Statistics and Data Analysis (48:1), pp. 159-205.

Vandenberg, R. J., and Lance, C. E. 2000. “A Review and Synthesis of the Measurement Invariance Literature: Suggestions, Practices, and Recommendations for Organizational Research,” Organizational Research Methods (3:1), pp. 4-70.

Werts, C. E., Linn, R. L., and Jöreskög, K. G. 1974. “Intraclass Reliability Estimates: Testing Structural Assumptions,” Educational and Psychological Measurement (34:1), pp. 25-33.

Wold, H. 1982. “Soft Modeling: The Basic Design and Some Extensions,” in Systems Under Indirect Observation: Causality, Structure, Prediction (Volume 2), K. G. Jöreskog and H. Wold (eds.), Amsterdam: North Holland, pp.1-54.

Wold, H. 1985. “Partial Least Squares,” in Encyclopedia of Statistical Sciences (Volume 6), S. Kotz and N. L. Johnson (eds.), New York: Wiley, pp. 581-591.

Wolf, H.-G., and Preising, K. 2005. “Exploring Item and Higher Order Factor Structure with the Schmid-Leiman Solution: Syntax Codes for SPSS and SAS,” Behavior Research Methods (37:1), pp. 48-58.

## About the Authors

Martin Wetzels is a professor of marketing and supply chain research in the Department of Marketing at Maastricht University, the Netherlands. His main research interests are customer satisfaction and dissatisfaction, customer value, services marketing, business-to-business marketing (online) marketing research, supply chain management, cross-functional cooperation, e-commerce, new product development, technology infusion in services, and relationship marketing. His work has been published in Management Science, Journal of the Academy of Marketing Science, Journal of Retailing, Information & Management, Computers & Education, Marketing Letters, International Journal of Research in Marketing, Journal of Business Research, Journal of Interactive Marketing, Journal of Economic Psychology, and Journal of Management Studies. He has contributed more than 70 papers to conference proceedings.

Gaby Odekerken-Schröder is an associate professor in marketing at Maastricht University. Her main research interests are related to the domains of relationship marketing, services marketing, customer (e-)loyalty, and consumer behavior. She is member of the editorial board of Journal of Relationship Marketing and ad hoc reviewer for Journal of Marketing and International Journal of Service Industry Management. Her research has been published in Journal of Marketing, Journal of Business Research, European Journal of Marketing, International Marketing Review, Journal of Retailing and Consumer Services, Journal of Consumer Marketing, and many other international journals.

Claudia A. M. L. van Oppen finished her Ph.D. in marketing at Maastricht University. She is currently the manager of the SME Portal of Maastricht University, responsible for facilitating, coordinating and managing the knowledge transfer between Maastricht University and entrepreneurs in the (EU) region.

Covariance Matrix of Manifest Variables $^{†}$  
Appendix

<table><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td><td>21</td><td>2</td><td>23</td><td>24</td><td>25</td></tr><tr><td>1. APPEAL01</td><td>1.65</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2. APPEAL02</td><td>1.00</td><td>2.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3. APPEAL03</td><td>1.01</td><td>1.34</td><td>1.67</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4. ENT01</td><td>1.05</td><td>1.13</td><td>0.99</td><td>2.11</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5. ENT02</td><td>0.68</td><td>1.19</td><td>0.99</td><td>1.07</td><td>1.78</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>6. ENT03</td><td>0.42</td><td>0.95</td><td>0.82</td><td>1.08</td><td>1.35</td><td>2.51</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>7. ESC01</td><td>0.39</td><td>0.52</td><td>0.36</td><td>0.87</td><td>0.62</td><td>0.88</td><td>1.83</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>8. ESC02</td><td>0.05</td><td>0.50</td><td>0.34</td><td>0.45</td><td>0.82</td><td>1.09</td><td>0.70</td><td>1.89</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>9. ESC03</td><td>0.19</td><td>0.63</td><td>0.47</td><td>0.67</td><td>0.81</td><td>1.11</td><td>0.86</td><td>0.99</td><td>1.68</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>10. ENJOY01</td><td>0.39</td><td>0.46</td><td>0.41</td><td>0.64</td><td>0.76</td><td>1.13</td><td>0.74</td><td>0.98</td><td>0.83</td><td>2.42</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>11. ENJOY02</td><td>0.19</td><td>0.45</td><td>0.42</td><td>0.45</td><td>0.79</td><td>1.24</td><td>0.73</td><td>1.12</td><td>1.18</td><td>1.09</td><td>1.72</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>12. EFF01</td><td>0.51</td><td>0.57</td><td>0.51</td><td>0.45</td><td>0.47</td><td>0.46</td><td>0.22</td><td>0.33</td><td>0.31</td><td>0.44</td><td>0.10</td><td>2.87</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>13. EFF02</td><td>0.42</td><td>0.66</td><td>0.48</td><td>0.22</td><td>0.55</td><td>0.54</td><td>0.12</td><td>0.62</td><td>0.61</td><td>0.57</td><td>0.39</td><td>1.23</td><td>2.84</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>14. EFF03</td><td>0.27</td><td>0.55</td><td>0.36</td><td>0.23</td><td>0.29</td><td>0.44</td><td>0.39</td><td>0.12</td><td>0.31</td><td>0.34</td><td>0.17</td><td>1.23</td><td>1.17</td><td>2.17</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15. ECVAL01</td><td>0.56</td><td>0.72</td><td>0.65</td><td>0.43</td><td>0.48</td><td>0.40</td><td>0.18</td><td>0.28</td><td>0.17</td><td>0.20</td><td>0.03</td><td>0.87</td><td>0.47</td><td>0.56</td><td>1.72</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>16. ECVAL02</td><td>0.35</td><td>0.35</td><td>0.40</td><td>0.36</td><td>0.30</td><td>0.34</td><td>0.05</td><td>0.07</td><td>0.05</td><td>0.05</td><td>-0.05</td><td>0.35</td><td>0.40</td><td>0.42</td><td>0.95</td><td>1.57</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>17. ECVAL03</td><td>0.31</td><td>0.24</td><td>0.15</td><td>0.09</td><td>0.03</td><td>0.00</td><td>-0.01</td><td>0.07</td><td>-0.20</td><td>-0.13</td><td>-0.27</td><td>0.35</td><td>0.13</td><td>0.37</td><td>0.74</td><td>0.87</td><td>1.61</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>18. EXCEL01</td><td>0.87</td><td>1.16</td><td>1.00</td><td>0.92</td><td>1.06</td><td>0.98</td><td>0.49</td><td>0.62</td><td>0.57</td><td>0.76</td><td>0.64</td><td>0.82</td><td>0.71</td><td>0.78</td><td>0.70</td><td>0.59</td><td>0.48</td><td>2.12</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>19. EXCEL02</td><td>0.54</td><td>0.94</td><td>0.84</td><td>0.81</td><td>0.80</td><td>0.80</td><td>0.36</td><td>0.50</td><td>0.56</td><td>0.71</td><td>0.42</td><td>0.84</td><td>0.67</td><td>0.91</td><td>0.60</td><td>0.63</td><td>0.43</td><td>1.19</td><td>2.45</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>20. ALOY01</td><td>0.86</td><td>0.97</td><td>1.00</td><td>0.71</td><td>0.90</td><td>0.97</td><td>0.47</td><td>0.55</td><td>0.61</td><td>0.65</td><td>0.56</td><td>0.77</td><td>1.06</td><td>0.64</td><td>0.62</td><td>0.52</td><td>0.20</td><td>0.99</td><td>0.83</td><td>1.78</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>21. ALOY02</td><td>0.55</td><td>0.94</td><td>0.74</td><td>0.73</td><td>0.76</td><td>0.97</td><td>0.58</td><td>0.71</td><td>0.87</td><td>0.70</td><td>0.75</td><td>0.66</td><td>0.71</td><td>0.73</td><td>0.60</td><td>0.38</td><td>0.41</td><td>1.12</td><td>1.06</td><td>0.78</td><td>2.53</td><td></td><td></td><td></td><td></td></tr><tr><td>22. ALOY03</td><td>0.79</td><td>1.11</td><td>0.96</td><td>0.81</td><td>0.92</td><td>0.87</td><td>0.59</td><td>0.74</td><td>0.78</td><td>0.60</td><td>0.65</td><td>0.41</td><td>0.79</td><td>0.50</td><td>0.59</td><td>0.40</td><td>0.34</td><td>1.20</td><td>0.91</td><td>0.96</td><td>1.67</td><td>2.67</td><td></td><td></td><td></td></tr><tr><td>23. BLOY01</td><td>0.53</td><td>0.55</td><td>0.46</td><td>0.59</td><td>0.62</td><td>0.58</td><td>0.49</td><td>0.42</td><td>0.72</td><td>0.60</td><td>0.44</td><td>0.55</td><td>0.76</td><td>0.32</td><td>0.48</td><td>0.51</td><td>0.22</td><td>0.75</td><td>0.57</td><td>0.77</td><td>0.81</td><td>1.15</td><td>2.87</td><td></td><td></td></tr><tr><td>24. BLO02</td><td>0.56</td><td>0.86</td><td>0.61</td><td>0.69</td><td>0.80</td><td>1.11</td><td>0.37</td><td>0.73</td><td>0.93</td><td>0.70</td><td>0.59</td><td>0.52</td><td>0.85</td><td>0.40</td><td>0.62</td><td>0.56</td><td>0.21</td><td>1.06</td><td>0.70</td><td>0.87</td><td>1.18</td><td>1.51</td><td>1.67</td><td>2.90</td><td></td></tr><tr><td>25. BLOY03</td><td>0.39</td><td>0.60</td><td>0.53</td><td>0.35</td><td>0.78</td><td>0.84</td><td>0.42</td><td>1.06</td><td>0.93</td><td>0.75</td><td>0.61</td><td>0.62</td><td>1.08</td><td>0.70</td><td>0.73</td><td>0.54</td><td>0.36</td><td>0.95</td><td>0.84</td><td>0.91</td><td>1.22</td><td>1.54</td><td>1.06</td><td>1.29</td><td>3.27</td></tr></table>
