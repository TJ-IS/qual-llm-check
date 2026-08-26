---
otero_id: 14908
otero_key: "2S6257B6"
title: "Analysing quadratic effects of formative constructs by means of variance-based structural equation modelling"
authors: "Jörg Henseler; Georg Fassott; Theo K Dijkstra; Bradley Wilson"
year: "2012"
journal: "European Journal of Information Systems"
doi: "10.1057/ejis.2011.36"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Analysing quadratic effects of formative constructs by means of variance-based structural equation modelling<sub>w</sub>

Jo¨rg Henseler<sup>1,2</sup>, Georg Fassott<sup>3</sup>, Theo K. Dijkstra<sup>4</sup> and Bradley Wilson<sup>5</sup>

<sup>1</sup>Institute for Management Research, Radboud University Nijmegen, The Netherlands; <sup>2</sup>Higher Institute of Statistics and Knowledge Management (ISEGI), Universidade Nova de Lisboa, Portugal; <sup>3</sup>Faculty of Business Studies and Economics, University of Kaiserslautern, Germany; <sup>4</sup>Faculty of Economic and Business, University of Groningen, The Netherlands; <sup>5</sup>School of Media and Communication, RMIT University, Melbourne, Australia

Correspondence: Jo¨rg Henseler, Institute for Management Research, Radboud University Nijmegen, Thomas van Aquinostraat 3, 6525 GD Nijmegen, The Netherlands. Tel: 31 24 361 1854; Fax: 31 24 361 1933; E-mail: j.henseler@fm.ru.nl

## Abstract

Together with the development of information systems research, there has also been increased interest in non-linear relationships between focal constructs. This article presents six Partial Least Squares-based approaches for estimating formative constructs’ quadratic effects. In addition, these approaches’ performance is tested by means of a complex Monte Carlo experiment. The experiment reveals significant and substantial differences between the approaches. In general, the performance of the hybrid approach as suggested by Wold (1982) is most convincing in terms of point estimate accuracy, statistical power, and prediction accuracy. The two-stage approach suggested by Chin et al (1996) showed almost the same performance; differences between it and the hybrid approach – although statistically significant – were unsubstantial. Based on these results, the article provides guidelines for the analysis of nonlinear effects by means of variance-based structural equation modelling. European Journal of Information Systems (2012) 21, 99–112. doi:10.1057/ejis.2011.36; published online 6 September 2011

Keywords: partial least squares path modelling; PLS; non-linear effect; quadratic effect

## Introduction

Structural equation modelling (SEM) has become a quasi-standard for survey-based studies in information systems (IS) research. As Gefen & Straub (1997, p. 6) point out, ‘SEM has become de rigueur in validating instruments and testing linkages between constructs’. They distinguish between two families of SEM techniques: covariance-based techniques (represented by LISREL) and variance-based techniques (represented by Partial Least Squares Path Modelling, PLS). PLS path modelling has specifically become a key multivariate analysis method in top-tier IS journals such as the European Journal of Information Systems (EJIS), Information Systems Research (ISR) and the Management Information Systems Quarterly (MISQ). From January 1990 until February 2009, a total of 105 PLS path modelling applications were published in EJIS (18 articles), ISR (21 articles), and MISQ (66 articles), respectively. A reason for the advent of PLS could be its use in estimating formative constructs’ measurement models, which has been very strongly recommended (cf. Chin, 1998; Petter et al, 2007).

Currently, SEM faces an increased demand for methodological advances, as the complexity of hypothesised relationships has steadily increased with scientific disciplines’ development (cf. Cortina, 1993). In many instances, linear effects have already been identified between focal constructs, and researchers’ interest has shifted toward non-linear effects like quadratic effects and interaction effects. However, testing suspected non-linear effects by means of SEM is regarded difficult and ‘problematic’ (Gefen & Straub, 1997, p. 42), which is also due to a lack of clear guidelines on how to undertake a non-linear effect analysis. A wellestablished practice is to transfer guidelines originally meant for interaction effects to quadratic and other nonlinear effects (cf. Moulder & Algina, 2002; Marsh et al, 2004, 2006; Little et al, 2006). While with respect to reflective constructs, there are some papers on quadratic relationships (for a good overview see Schumacker & Marcoulides, 1998), there is hardly any literature on modelling the quadratic effects of formative constructs since Chin et al (1996) introduced both the product indicator and two-step procedures. This may coincide with a general ‘lack of attention to formative constructs in the literature’ (Petter et al, 2007, p. 640). Formative measurement is particularly relevant in the study of organisational constructs when the unit of analysis is companies instead of individuals (Diamantopoulos & Winklhofer, 2001), making it a valuable tool for empirical business success factor research (Albers, 2010).

In the light of the increasing popularity of formative measurement models in the IS disciplines (cf. Petter et al, 2007), strategy (cf. Podsakoff et $^ { a l , }$ 2006), marketing (cf. Jarvis et al, 2003) and beyond (cf. Diamantopoulos & Siguaw, 2006), there is a strong need for SEM approaches that can analyse formative constructs’ non-linear effects. In addition to the Chin et al papers (1996, 2003), only two papers, Wold (1982) and Dijkstra & Henseler (forthcoming), devote attention to the analysis of formative constructs’ non-linear effects. Both of these papers use variance-based SEM. However, none of the previous research examines the suggested approaches’ performance systematically by means of simulation. Consequently, hardly anything is known about their approaches’ relative and absolute performance regarding modelling formative constructs’ non-linear effects. The limited knowledge of how to model quadratic effects is even more striking when taking into account Carte & Russell’s (2003) recommendation that models with interaction terms should always also include the quadratic terms of the respective variables.

The present study aims to fill this gap in knowledge within the PLS literature by answering the research question: How should researchers analyse formative constructs’ quadratic effects by means of variance-based structural equation modelling? We gather all extant and a few new PLS-based approaches for estimating formative constructs quadratic effects and compare their performance by means of a Monte Carlo study. We subsequently derive guidelines on when to use which approach for researchers. Four questions will thereby be answered: (1) Which PLS-based approaches are available for estimating formative constructs’ quadratic effects? (2) Which approach is most convincing in terms of its statistical power to detect formative constructs’ non-linear effects? (3) Which approach delivers the closest estimate of a quadratic effect?

(4) Which approach is preferable when the prediction of the endogenous latent variable’s true scores is of interest?

After a brief revision of formative measurement, we derive PLS-based approaches for estimating formative constructs’ quadratic effects as suggested in the context of interaction effects: the so-called product indicator approach (Chin et $^ { a l , }$ 1996, 2003) and a two-stage approach (Chin et $^ { a l , }$ 2003; Henseler & Fassott, 2010). We thereafter describe an approach for analysing nonlinear effects as initially proposed by Herman Wold (1982). Finally, we include an orthogonalising approach as suggested by Little et al (2006). Since nothing is known about how these approaches perform with regard to formative measurement, we compare them in terms of their behaviour, that is we analyse their point estimate accuracy, statistical power, and predictive capability. In order to illustrate the differences in estimation outcomes, we conduct an extensive computational experiment. We then compare and contrast the results, draw conclusions, and make recommendations regarding how formative constructs’ quadratic effects can be optimally modelled by means of PLS path modelling.

## Formative constructs in management and IS research

Formative constructs are complex variables measured indirectly by means of formative (Fornell, 1982) or causal (Bollen & Lennox, 1991) indicators. The indicators play the role of causal antecedents in the formative construct. Collectively, they determine the formative construct’s conceptual and empirical contents (Jarvis et al, 2003). Formative constructs are usually defined as linear combinations of their respective indicators. One of the few exceptions is the construct ‘ambidexterity’, which is construed as the product of two indicators (Gibson & Birkinshaw, 2004). In the standard linear case, formative constructs are characterised by the following equation:

$$
F = w _ {1} \cdot x _ {1} + w _ {2} \cdot x _ {2} + \dots + w _ {J} \cdot x _ {J} + \zeta .\tag{1}
$$

In Eq. $( 1 ) , x _ { j } ( j = 1 . . . J )$ are the formative indicators, w denote the weight coefficients, and z represents the formative construct’s measurement error. This measurement error resides at the construct level, and according to Diamantopoulos (2006), it represents omitted causes. In practice, most formative constructs are operationalised without the measurement error, because it is subject to indeterminacy. The measurement error’s magnitude can be quantified by means of at least two additional reflective indicators or endogenous variables that depend on the formative construct (Jarvis et $^ { a l , }$ 2003).

A growing number of constructs are conceptualised and operationalised as formative. Additionally, a large number of presumably reflective constructs can be regarded as misspecified, and should rather be specified as formative (Jarvis et al, 2003; Petter et al, 2007). Many formative constructs in the IS discipline, such as perceived user resources (Mathieson et $^ { a l , }$ 2001), team skills (Wixom & Watson, 2001), and declarative knowledge (Yi & Davis, 2003), can be regarded as modern forms of production factors. As such, they are highly likely to be subject to the well-known law of diminishing marginal returns. Other constructs, which are or could be specified as formative, such as perceived usefulness (Petter et al, 2007), might be subject to the law of marginal utility. In both cases, economic theory strongly suggests that these formative constructs have non-linear effects.

Compilation of possible PLS-based approaches to analyse quadratic effects of formative constructs In 1966, Herman Wold published the first paper on nonlinear iterative least squares, which is the underlying idea of PLS path modelling as well as its sister technique, PLS regression. Regardless of what the original name suggests, and contrary to the scientific progress of PLS regression’s non-linear extensions (cf. Wold et $^ { a l , }$ 1989), non-linear relationships between latent variables have not been a focal objective of PLS path modelling. As far as we know, other than the two Chin et al papers (1996, 2003), estimating non-linear effects by means of PLS path modelling has not received any attention during the last two decades. However, this does not mean that PLS path modelling is not suitable for detecting non-linear effects. Herman Wold himself regarded PLS path modelling as readily equipped to estimate the non-linear effects between latent variables (Wold, 1982).

In the remainder of this section, we will first describe Wold’s original approach (which we will call the hybrid approach in accordance with Henseler & Chin (2010)), and secondly present several other approaches that have been proposed for analysing interaction effects.

## The hybrid approach

In 1982, Herman Wold presented a first approach for the estimation of PLS path models with non-linearities in the structural model. Although he only considered a model with a quadratic term in depth, the approach is generalisable to other non-linear relations between latent variables. The main idea of this approach is to incorporate an internal proxy for each non-linear term during the iterative PLS algorithm’s runtime.

In order to illustrate the working principle of the hybrid approach, we draw on Tenenhaus et al’s (2005) description of the PLS algorithm, and extend it where necessary (in italics). The PLS algorithm delivers estimates for the latent variable scores by means of an iterative process that basically consists of four steps:

(1) Calculating outer proxies of latent variable scores: Outer proxies of the latent variables, $\hat { \xi } _ { j } ^ { o } ,$ are calculated as linear combinations of their respective indicators. The weights of the linear combinations result from step 4 of the previous iteration or are manually initialised. For each non-linear term, a new proxy is created as the element-wise transformation of the respective outer estimates. For instance, in order to incorporate a quadratic effect of the latent variable $\xi _ { j } ,$ a quadratic term proxy is calculated as the element-wise product $o f \hat { \xi } _ { j } ^ { o }$ with $\hat { \xi } _ { j } ^ { o } .$

(2) Estimating inner weights: For each outer proxy, inner weights are calculated to reflect how strongly the proxies of the other latent variables are connected to it. Several inner weighting schemes are available. Wold (1982) originally proposed that the sign should be used of the correlations between a latent variable and its adjacent latent variables (which is the so-called centroid scheme). Alternatives are the factor weighting scheme and the path weighting scheme (see Lohmo¨ller, 1989). Regardless of the weighting scheme, a weight of zero is assigned to all non-adjacent latent variables. Inner weights are also determined for each proxy of a non-linear term.

(3) Calculating inner proxies of latent variable scores: Inner proxies of the latent variables, $\hat { \xi } _ { j } ^ { i } ,$ are calculated as linear combinations of their respective adjacent latent variables’ outer proxies, using the previously determined inner weights. The proxies of non-linear terms are also used to estimate endogenous latent variables’ inner proxies.

(4) Estimating outer weights: The outer weights are either calculated as the covariances between each latent variable and its indicators’ inner proxy (in Mode A) or as the regression weights resulting from the ordinary least squares regression of each latent variable’s inner proxy on its indicators (in Mode B). In this step, no changes are required to the original algorithm, because the non-linear terms do not have any indicators assigned.

These four steps are iterated until the change in outer weights between two iterations falls below a predefined limit. The algorithm terminates after the first step, producing estimates of the latent variable scores of all latent variables, including the non-linear terms. The path coefficients result from the regressions of the endogenous variables’ scores on the explaining variables’ scores (including the non-linear terms).

## The product indicator approach

Busemeyer & Jones (1983) and Kenny & Judd (1984) introduced the initial approaches for the use of SEM methodology to examine quadratic effects among latent variables. These authors suggested building quadratic terms, using the squared indicator values of the relevant latent independent variable as indicators. Chin et al (1996, 2003) were the first to transfer this approach to PLS path modelling. Although these authors limited the application to the analysis of interaction effects, they stated that their approach for creating non-linear product indicators ‘can be extended to the other powers $( \bar { \mathrm { e } } . \mathbf { g } . , X ^ { 2 } .$ $X ^ { 3 } ,$ or $X ^ { 2 } \cdot Z )$ as long as the indicators for the predictor and moderator constructs are viewed as reflective measures’ (1996, p. 35). They called this approach the product indicator approach. Technically, a new latent variable is added for each quadratic effect. This latent variable is measured by means of the so-called product indicators. The product indicators are compiled as all possible indicator products of the respective order (quadratic, cubic, etc.). For instance, the product indicators $x _ { i j }$ of a latent variable representing the quadratic term of a latent variable x with indicators $x _ { i }$ would be construed by the following formula:

$$
x _ {i j} = x _ {i} * x _ {j} \quad \forall i, j.\tag{2}
$$

Here, the asterisk denotes the element-wise product. Polynomial terms of a higher order are built in analogy.

Note that Chin et al (2003) recommend using the centred original indicators to produce the product indicators. Although such a procedure does not necessarily diminish the multicollinearity resulting from building the quadratic term (see Echambadi & Hess, 2007, contrary to Cohen, 1978, and Cronbach, 1987), it does facilitate the interpretation of the model results.

## The simplified product indicator approach

The high number of product indicators if the original latent variable has many indicators can be a caveat of the product indicator approach. In order to obtain a latent variable representing a quadratic term of an original latent variable with k manifest variables, $k ^ { 2 }$ product indicators have to be calculated as the original manifest variables’ element-wise product.

As studies on non-linear effects in SEM show, not only is it feasible to use fewer product indicators (Jo¨reskog & Yang, 1996), but this may also result in a higher statistical power (Jonsson, 1998). We therefore propose a simplified product indicator approach, which only performs the quadratic transformation on each indicator without calculating cross-products. Thus, in the simplified product indicator approach, the non-linear term in the structural model has k product indicators $p _ { i i } = p _ { i } ^ { 2 }$ $i = 1 , \ldots , k .$

## The two-stage approach

The idea of the two-stage approach was initially suggested by Chin et al (1996, 2003) and elaborated by Henseler & Fassott (2010). These authors recognised that if the exogenous variable or the moderator variable are formative, the pair-wise multiplication of indicators might be questionable. ‘Since formative indicators are not assumed to reflect the same underlying construct (i.e. can be independent of one another and measure different factors), the product indicators between two sets of formative indicators will not necessarily tap into the same underlying interaction effect’ (Chin et al, 2003, Appendix D). Henseler & Fassott (2010) supported and advocated Chin’s recommendation to use the two-stage approach instead of the product indicator approach for estimating moderating effects, particularly when formative constructs are involved. The two-stage approach makes use of PLS path modelling’s characteristic of explicitly estimating latent variable scores (cf. Henseler,

2010). In order to analyse quadratic effects in the structural model, the two stages are built up as follows:

(1) In the first stage, the main effect PLS path model is run in order to obtain estimates for the latent variable scores. The latent variable scores are calculated and saved for further analysis.

(2) In the second stage, a quadratic term can be construed as the element-wise product of the latent variable scores of the exogenous variable $\xi _ { j } .$ The latent variable scores of $\xi _ { j }$ and the quadratic term $\xi _ { j } ^ { 2 }$ are used as independent variables in a multiple linear regression explaining the latent variable scores of the endogenous variable $\xi _ { k } .$

The second stage can be realised by multiple linear regression or be implemented within PLS path modelling by means of single indicator measurement models. Note that although the latent variable scores of $\xi _ { j }$ are standardised, the quadratic term is not – and should not be.

While Chin et al (2003) as well as Henseler & Fassott (2010) limit the usage of the two-stage approach to cases when the independent variable is formative, this limitation is not mandatory. Technically, it can also be applied to the estimatation of quadratic effects of reflective constructs (Wilson 2010). However, a clear disadvantage of the two-stage approach is that the quadratic effect is not taken into account when estimating the latent variable scores.

## The orthogonalising approach

Little et al (2006) have recently suggested an orthogonalising approach for modelling moderating and quadratic effects among latent variables in structural equation models. The main objective of their approach is to overcome the problems of multicollinearity that often occur when non-linear terms and linear terms simultaneously enter in multiple regression as independent variables. Henseler & Chin (2010) applied this approach using the PLS algorithm for reflective indicators.

Basically, the orthogonalising approach is an extension of residual centring’s use for moderated multiple regressions, as described by Lance (1988). Residual centring is essentially a two-stage OLS procedure in which a nonlinear term is regressed on its respective linear term. The resulting residuals are then used as in the product indicator approach.

This new orthogonalised non-linear term’s unique variance fully represents the non-linear effect, independent of the linear effect. Owing to the non-linear term’s orthogonality, the parameter estimates of the linear effects in a model with non-linear terms are identical to those in a model without the non-linear terms. Furthermore, residual centring yields a regression coefficient for the non-linear term that can directly be interpreted as the non-linear term’s effect on the dependent variable (cf. Lance, 1988); consequently, this replaces the assessment of the increase in the coefficient of determination due to the non-linear term's inclusion. Since PLS calculates the latent variable scores as linear combinations of the respective indicators, it can be derived that a non-linear term created in this manner is orthogonal to its constituting latent variable.

The orthogonalising approach requires as many indicators as the product indicator approach. Analogously to the simplified product indicator approach, it could be worthwhile applying a simplified orthogonalising approach, which should result in a substantial reduction of indicators.

## Software implementation

As the previous section illustrated, there are six possible PLS-based approaches to model formative constructs’ quadratic effects: (1) the product indicator approach, (2) the simplified product indicator approach, (3) the orthogonalising approach, (4) the simplified orthogonalising approach, (5) the two-stage approach, and (6) the hybrid approach. In order to apply the six approaches and to compare them in terms of their performance, it is crucial to use adequate PLS software. Although five of the six approaches, that is both the product indicator approaches, the two-stage approach, and the two orthogonalising approaches, could be executed by means of available software, one approach, the hybrid approach, requires an enhancement of the standard PLS algorithm. Since none of the available PLS software packages allow modifying the PLS algorithm itself, we created our own implementation of the PLS algorithm by applying the algorithm in vector form and following the detailed description by Tenenhaus et al (2005). As an extension to the PLS algorithm, the hybrid approach was implemented as described in the previous section. We used R2.10.1 (R Development Core Team, 2007) as the programming language. Besides its thorough compliance with the algebraic terms as formulated by Tenenhaus et al (2005), the PLS code’s correctness was also verified by comparing the results of two data analyses conducted with our implementation with the results of the PLS path modelling implementations PLS-Graph 3.0 (Soft Modeling, Inc., 1992–2002) and SmartPLS 2.0 M3 (Ringle et al, 2007). Besides obvious rounding inaccuracies, the results were identical.

## A Monte Carlo experiment

In order to find generalisable patterns and to investigate the appropriateness of the six presented approaches, we conduct a Monte Carlo simulation. The goal of this computational experiment is to elucidate the different approaches’ performance for an analysis of formative constructs’ quadratic effects by means of PLS path modelling. We compare the point estimate accuracy, the power, and the prediction accuracy of the six considered approaches at different quadratic effect sizes, different numbers of observations, and different formative weights. The steps of the Monte Carlo experiment are as follows: Firstly, we define an underlying true model and determine the experimental factors and their levels.

![](/api/attachments/2S6257B6/fulltext/images/bc43aac8892002d6c4a9a1710a8a3e2051a5f3003b8a7d0130a3902ef42c8f49.jpg)  
Figure 1 Population model of the Monte Carlo experiment.

Secondly, we generate random data, which emerge from the model parameters. Thirdly, given the random data, we let each PLS approach estimate the model. Fourthly, we evaluate the outcomes that each approach produces with respect to the population coefficients and in relation with the other approaches.

The choice of the underlying model is crucial for the simulation outcomes. We define an underlying true model that is as simple as possible, consisting of an exogenous formative construct with eight indicators, one endogenous reflective construct with eight indicators, and a quadratic effect. The simulation model is depicted in Figure 1.

All of the standardised loadings of the endogenous reflective construct have a value of 0.8. We specify two sets of weights for the exogenous formative construct. The first set of weights consists of relatively homogenous standardised weights of 0.3 and 0.4. The second set of weights is more heterogenous, with standardised weights ranging from 0.8 to 0.1. As true path coefficients, a value of 0.5 is chosen for the main effect $( \beta _ { 1 } )$ , while values of 0.00, 0.15, 0.35, and 0.50 are chosen for the quadratic effect (b ), representing a non-existent/weak/moderate/ strong effect. With regard to the number of observations, we test two conditions that roughly cover typical sample sizes in social science and management: 100 and 500 observations.

We opt for a repeated measures design, in which the six different approaches form a within-subject factor, while the quadratic effect’s size, the number of observations, and the formative weights’ homogeneity serve as between-subject factors. Table 1 provides a summary of the selected factors and their respective levels. We choose for a full-factorial design in order to have the possibility to capture eventual interaction effects between the factors. Hence, 16 conditions (four levels of quadratic effects  two levels of observations  two levels of formative weights) emerge. A total of 2000 Monte Carlo runs are conducted under each of the 16 conditions, resulting in a total of 32,000 Monte Carlo runs.

Table 1 Design of the computational experiment

<table><tr><td>Factor type</td><td>Factor</td><td>Factor levels</td></tr><tr><td>Within-subject factor</td><td>Approach</td><td>(1) Product indicator approach(2) Simplified product indicator approach(3) orthogonalising approach(4) Simplified orthogonalising approach(5) Two-stage approach(6) Hybrid approach</td></tr><tr><td rowspan="3">Between-subject factors</td><td>Number of observations</td><td>(1) 100(2) 500</td></tr><tr><td>Non-linear effect</td><td>(1) 0.00(2) 0.15(3) 0.35(4) 0.50</td></tr><tr><td>Formative weights</td><td>(1) 0.3, 0.4, 0.3, 0.4, 0.3, 0.4, 0.3, 0.4 (homogenous)(2) 0.8, 0.4, 0.3, 0.2, 0.2, 0.1, 0.1, 0.1 (heterogenous)</td></tr></table>

For each run, independent standard-normal formative indicators are created for the exogenous construct x. The latent variable scores of x are calculated as weighted sum of these indicators and divided by the resulting standard deviation.

Moreover, a standard-normal disturbance term z is created. The scores of the endogenous latent variable are determined as follows:

$$
\begin{array}{l} \eta = \beta_ {1} \cdot \xi + \beta_ {2} \cdot \xi^ {2} \\ \qquad + \sqrt {1 - \beta_ {1} ^ {2} - \beta_ {2} ^ {2} - 2 \cdot \beta_ {1} \cdot \beta_ {2} \cdot \operatorname{cov} (\xi , \xi^ {2})} \cdot \zeta \end{array} .\tag{3}
$$

The covariance between $\xi$ and $\xi ^ { 2 }$ is accounted for in order to obtain standardised latent variable scores for the endogenous construct. The indicator values $\gamma _ { i }$ of the ith reflective indicator of the endogenous latent variable Z are created as a linear combination of the latent variable scores and a standard normal distributed random variable:

$$
x _ {i} := \lambda \cdot \xi + \sqrt {1 - \lambda^ {2}} \cdot \mathcal {N} (0; 1) \quad \forall i.\tag{4}
$$

Furthermore, all indicators $x _ { i }$ is standardised with a mean of zero and a standard deviation of one. As additional input for the product indicator approach, the product indicators are calculated following Eq. (2). For the orthogonalising approach, regressions are applied and their residuals saved as indicators of the quadratic term.

For each run under each condition, all six approaches for analysing the interaction effects between latent variables by means of PLS path modelling are used to estimate the model. Product indicators and orthogonalisation residuals are used as formative indicators of the interaction term. We select the path weighting scheme as the inner weighting scheme, because it is the only scheme that takes the constructs’ causal order into account (Lohmo¨ller, 1989). The endogenous construct is estimated with Mode $\mathrm { A } ,$ which usually represents reflective measurement models (cf. Chin, 1998), whereas Mode B (formative) is applied to the exogenous construct. Each estimation is accompanied by 200 bootstrap calculations in order to assess the estimates’ significance. We ensure that all approaches make use of the same bootstrap samples. The following PLS estimation outcomes are measured for each run:

 path coefficient estimates for the single and non-linear effects;

 bootstrap t-values for all effects; and

 the squared correlation between the endogenous variable’s predicted latent variable scores and its true scores.

In the following sub-sections, we will report on and discuss the simulation outcomes of the parameter accuracy, statistical power, and prediction accuracy.

## Parameter accuracy

In order to compare the different parameters, we examine the extent to which the parameter estimates deviate from the true values. First, we assess the mean relative bias (MRB). The MRB is the mean over the deviations from the true value, and is algebraically defined as (Reinartz et $^ { a l , }$ 2002, p. 237):

$$
\mathrm{MRB} = \frac {1}{t} \sum_ {i = 1} ^ {t} \frac {\widehat {X} _ {i} - X _ {i}}{X _ {i}}.\tag{5}
$$

Positive MRBs indicate an over-estimation of the true parameter, while negative MRBs are an under-estimation. Tables 2 and 3 provide an overview of the MRBs of each approach under all conditions for the two path coefficients. Table 2 shows a relatively clear pattern: The product indicator approach substantially underestimates the main effect of $\xi$ on $\eta ,$ whereas all other approaches have smaller MRBs. In order to identify reasons for the differences in ${ \hat { \beta } } _ { 1 } ,$ , we examine the generated construct scores’ validity as the shared variance of the approximated construct score $\hat { \xi }$ and the true construct score $\xi .$ Interestingly, all approaches yield the same validity. This means that the differences in $\hat { \beta } _ { 1 }$ can solely be attributed to the way the quadratic term is construed.

As far as the quadratic effect’s relative bias is concerned, we find that the estimates of the product indicator approach, the orthogonalising approach, and the respective simplified approaches exhibit substantial bias – at least for some combinations of the number of indicators and the quadratic effect’s size. Only the two-stage approach and the hybrid approach consistently provide estimates with a relatively small downward bias. In order to identify possible explanations for these differences in the approaches, we examine the validity of the quadratic terms measurement (see the last column of Table 3). This time, there are large differences in the approaches. Both the two-stage approach and the hybrid approach yield acceptable validity levels. However, for all other approaches, the quadratic term’s scores have an unaccep tably low validity. Since the approximated scores share less than half of their variance with the true scores, the validity clearly falls below generally accepted levels (cf. Fornell & Larcker, 1981). Since all four approaches rely on product indicators, it is likely that they capitalise on chance – an idea already previously expressed by Goodhue et al (2007) with regard to the analysis of interaction effects. Chin et al had stated that the product indicator approach works ‘as long as the indicators for the predictor and moderator constructs are viewed as reflective measures’ (1996, p. 35). Our Monte Carlo simulation corroborates this statement in that this procedure performs poorly for formative indicators.

Table 2 MRBs of the linear path (b<sub>1</sub>) and validity of the exogenous formative construct $\hat { \xi }$

<table><tr><td rowspan="2"></td><td rowspan="2">Approach</td><td colspan="4">Non-linear effect</td><td rowspan="2">Validity  $cor^2(\hat{\xi}, \xi)$ </td></tr><tr><td>0.000</td><td>0.150</td><td>0.350</td><td>0.500</td></tr><tr><td rowspan="6">100 observations</td><td>Product indicator</td><td>-0.278</td><td>-0.281</td><td>-0.301</td><td>-0.325</td><td>0.823</td></tr><tr><td>Simplif. prod. ind.</td><td>0.001</td><td>-0.002</td><td>-0.009</td><td>-0.016</td><td>0.823</td></tr><tr><td>Orthogonalising</td><td>0.066</td><td>0.066</td><td>0.067</td><td>0.069</td><td>0.823</td></tr><tr><td>Simplif. orthog.</td><td>0.068</td><td>0.067</td><td>0.068</td><td>0.071</td><td>0.823</td></tr><tr><td>Two-stage</td><td>0.072</td><td>0.061</td><td>0.017</td><td>-0.043</td><td>0.823</td></tr><tr><td>Hybrid</td><td>0.071</td><td>0.061</td><td>0.015</td><td>-0.046</td><td>0.823</td></tr><tr><td rowspan="6">500 observations</td><td>Product indicator</td><td>-0.075</td><td>-0.080</td><td>-0.092</td><td>-0.099</td><td>0.960</td></tr><tr><td>Simplif. prod. ind.</td><td>-0.026</td><td>-0.027</td><td>-0.029</td><td>-0.031</td><td>0.960</td></tr><tr><td>Orthogonalising</td><td>-0.013</td><td>-0.013</td><td>-0.013</td><td>-0.011</td><td>0.960</td></tr><tr><td>Simplif. orthog.</td><td>-0.013</td><td>-0.013</td><td>-0.012</td><td>-0.011</td><td>0.960</td></tr><tr><td>Two-stage</td><td>-0.013</td><td>-0.016</td><td>-0.030</td><td>-0.047</td><td>0.960</td></tr><tr><td>Hybrid</td><td>-0.013</td><td>-0.016</td><td>-0.030</td><td>-0.048</td><td>0.960</td></tr></table>

Table 3 MRBs of the non-linear (quadratic) path (b ) and validity of the quadratic term $\hat { \xi } ^ { 2 }$

<table><tr><td rowspan="2"></td><td rowspan="2">Approach</td><td colspan="3">Non-linear effect</td><td rowspan="2"> $Validity \, cor^{2}(\hat{\xi}^{2}, \xi^{2})$ </td></tr><tr><td>0.150</td><td>0.350</td><td>0.500</td></tr><tr><td rowspan="6">100 observations</td><td>Product indicator</td><td>1.379</td><td>0.505</td><td>0.194</td><td>0.187</td></tr><tr><td>Simplif. prod. ind.</td><td>-0.459</td><td>-0.448</td><td>-0.453</td><td>0.120</td></tr><tr><td>Orthogonalising</td><td>2.121</td><td>0.658</td><td>0.271</td><td>0.204</td></tr><tr><td>Simplif. orthog.</td><td>-0.272</td><td>-0.312</td><td>-0.362</td><td>0.115</td></tr><tr><td>Two-stage</td><td>-0.265</td><td>-0.261</td><td>-0.263</td><td>0.670</td></tr><tr><td>Hybrid</td><td>-0.253</td><td>-0.251</td><td>-0.256</td><td>0.670</td></tr><tr><td rowspan="6">500 observations</td><td>Product indicator</td><td>0.536</td><td>0.042</td><td>0.037</td><td>0.381</td></tr><tr><td>Simplif. prod. ind.</td><td>-0.417</td><td>-0.453</td><td>-0.480</td><td>0.160</td></tr><tr><td>Orthogonalising</td><td>0.796</td><td>0.138</td><td>0.033</td><td>0.456</td></tr><tr><td>Simplif. orthog.</td><td>-0.266</td><td>-0.420</td><td>-0.462</td><td>0.166</td></tr><tr><td>Two-stage</td><td>-0.086</td><td>-0.085</td><td>-0.087</td><td>0.919</td></tr><tr><td>Hybrid</td><td>-0.083</td><td>-0.083</td><td>-0.085</td><td>0.919</td></tr></table>

Table 4 Multivariate tests (Wilks Lambda) over the relative bias of the linear effect $\left( \beta _ { 1 } \right)$ and the quadratic effect (b )

<table><tr><td rowspan="2">Effect</td><td colspan="2">Main effect  $\beta_1$ </td><td colspan="2">Quadratic effect  $\beta_2$ </td></tr><tr><td>Sig.</td><td>Partial  $\eta^2$ </td><td>Sig.</td><td>Partial  $\eta^2$ </td></tr><tr><td>approach</td><td>&lt;0.001</td><td>0.895</td><td>&lt;0.001</td><td>0.759</td></tr><tr><td>approach × effect</td><td>&lt;0.001</td><td>0.095</td><td>&lt;0.001</td><td>0.233</td></tr><tr><td>approach × obs.</td><td>&lt;0.001</td><td>0.801</td><td>&lt;0.001</td><td>0.480</td></tr><tr><td>approach × weights</td><td>&lt;0.001</td><td>0.011</td><td>&lt;0.001</td><td>0.035</td></tr><tr><td>approach × effect × obs.</td><td>&lt;0.001</td><td>0.045</td><td>&lt;0.001</td><td>0.057</td></tr><tr><td>approach × effect × weights</td><td>&lt;0.001</td><td>0.003</td><td>&lt;0.001</td><td>0.013</td></tr><tr><td>approach × obs. × weights</td><td>&lt;0.001</td><td>0.004</td><td>&lt;0.001</td><td>0.013</td></tr><tr><td>4-way interaction</td><td>&lt;0.001</td><td>0.001</td><td>&lt;0.001</td><td>0.011</td></tr></table>

As further investigation, we conduct two repeated measure ANOVAs, one for the relative bias of the direct effect estimate ${ \hat { \beta } } _ { 1 } ,$ and one for the relative bias of the quadratic effect estimate ${ \hat { \beta } } _ { 2 } .$ . Table 4 contains the multivariate tests for the two ANOVAs. Owing to the large number of cases, all effects are significant, that is all the design factors have an influence on the estimates’ relative bias. Another question, however, is whether all these influences are substantial. Assessing the partial $\eta ^ { 2 }$ as a measure of effect size, we find that only the approach, the number of observations, and the size of the quadratic effect play a role, whereas the formative weights’ homogeneity was irrelevant. Finally, by means of pairwise comparison, we find support for the hybrid approach having a significantly (Po0.001) lower relative bias than the two-stage approach.

## Statistical power

A researcher intending to make a conclusion about the existence of a quadratic effect would like to avoid two errors:

(1) concluding that there is a quadratic effect although in reality there is none (Type I error), and

(2) concluding that there is no quadratic effect although there is one in reality (Type II error).

In order to avoid Type I errors, one uses a predefined significance criterion (for example, $\alpha { = } 0 . 0 5 )$ when rejecting the null hypothesis; in order to avoid Type II errors, one has to apply a statistical test with satisfactory statistical power. ‘The power of a statistical test of a null hypothesis is the probability that it will lead to the rejection of the null hypothesis, i.e., the probability that it will result in the conclusion that the phenomenon exists’ (Cohen, 1988, p. 4). Often, a power of one minus four times the significance level is advocated, thus 80% for a significance criterion of 0.05, implying that a Type I error is regarded as four times as serious as a Type II error.

The power of a statistical test depends on several factors, namely the statistical significance criterion used in the test, the effect size in the population, the sample size, and the measurement reliability. In the Monte Carlo experiment, we keep the measurement reliability constant. Moreover, we use a constant significance criterion of 0.05 throughout the experiment. We evaluate the bootstrap t-values, and estimate the power of each approach per experimental condition as the proportion of the Monte Carlo runs that yielded a significant quadratic effect.

Table 5 provides the mean statistical power of finding a significant quadratic effect $( \beta _ { 2 } > 0 )$ at a significance level of $\alpha { = } 0 . 0 5$ . In general, the two-stage approach and the hybrid approach dominate in terms of statistical power. There is one exception: if there are fewer observations and homogenous indicator weights, the product indicator approach even achieves a somewhat higher statistical power.

To further corroborate these findings, an ANOVA, similar to the one for parameter accuracy, is conducted. The results of the tests of between-subjects effects are presented in Table 6. As anticipated, the number of observations and the strength of the quadratic effect play an important role. Nevertheless, with regard to the partial $\eta ^ { 2 } ,$ , the approach is what matters most.

## Prediction accuracy

A researcher who wants to include non-linear effects in a model for prediction purposes would be interested in the different approaches’ ability to predict an endogenous latent variable. In order to examine the prediction accuracy, we looked at the proportion of the true endogenous variable’s variance that can be explained by each approach.

Again, we consider the 16 predefined conditions. Table 7 exhibits the average (over 2000 Monte Carlo samples) squared correlations $( \mathrm { c o r } ^ { 2 } ( { \hat { Y , } } Y ) )$ between the predicted and the endogenous latent variable’s true values. For this criterion, the orthogonalising approach yields the highest values, followed by the product indicator approach. Also, most of the squared correlations are higher if there are fewer observations, indicating possible overfitting tendencies. Both these findings are a result of the number of free parameters used. In order to control for the number of free parameters, we calculate the adjusted squared correlations $\mathrm { c o r } _ { a d j } ^ { 2 } ( \hat { Y } , Y )$ ). Eq. (6) takes the number of observations n and the number of free parameters k into account.

$$
\begin{array}{l} \operatorname{cor} _ {a d j} ^ {2} (\hat {Y}, Y) \\ = \operatorname{cor} ^ {2} (\hat {Y}, Y) - \frac {k \cdot (1 - \operatorname{cor} ^ {2} (\hat {Y} , Y))}{n - k - 1} \cdot \end{array}\tag{6}
$$

The number of free parameters k is 74 for the orthogonalising and the product indicator approach (72 indicator weights plus 2 path coefficients), 18 for the simplified forms of the orthogonalising and the product indicator approach (16 indicator weights plus 2 path coefficients), and 10 for the two-stage and the hybrid approach (8 indicator weights plus 2 path coefficients). With regard to the adjusted squared correlations, the ranking of approaches changes: the two-stage approach and the hybrid approach now dominate.

Table 5 Mean statistical power of finding a significant (a ¼ 0.05) quadratic effect $( \beta _ { 2 } )$

<table><tr><td rowspan="2">Quadratic effect</td><td rowspan="2">Approach</td><td colspan="2">100 observations</td><td colspan="2">500 observations</td></tr><tr><td>Homogenous weights</td><td>Heterogenous weights</td><td>Homogenous weights</td><td>Heterogenous weights</td></tr><tr><td rowspan="6"> $\beta_{2}=0.00$ </td><td>Product indicator</td><td>0.011</td><td>0.037</td><td>0.011</td><td>0.031</td></tr><tr><td>Simplif. prod. ind.</td><td>0.051</td><td>0.056</td><td>0.046</td><td>0.047</td></tr><tr><td>Orthogonalising</td><td>0.000</td><td>0.014</td><td>0.000</td><td>0.006</td></tr><tr><td>Simplif. orthog.</td><td>0.042</td><td>0.052</td><td>0.036</td><td>0.033</td></tr><tr><td>Two-stage</td><td>0.002</td><td>0.004</td><td>0.000</td><td>0.000</td></tr><tr><td>Hybrid</td><td>0.002</td><td>0.004</td><td>0.000</td><td>0.000</td></tr><tr><td rowspan="6"> $\beta_{2}=0.15$ </td><td>Product indicator</td><td>0.124</td><td>0.108</td><td>0.785</td><td>0.459</td></tr><tr><td>Simplif. prod. ind.</td><td>0.086</td><td>0.090</td><td>0.188</td><td>0.229</td></tr><tr><td>Orthogonalising</td><td>0.086</td><td>0.089</td><td>0.953</td><td>0.453</td></tr><tr><td>Simplif. orthog.</td><td>0.090</td><td>0.095</td><td>0.196</td><td>0.228</td></tr><tr><td>Two-stage</td><td>0.114</td><td>0.127</td><td>0.998</td><td>0.995</td></tr><tr><td>Hybrid</td><td>0.113</td><td>0.126</td><td>0.998</td><td>0.995</td></tr><tr><td rowspan="6"> $\beta_{2}=0.35$ </td><td>Product indicator</td><td>0.872</td><td>0.489</td><td>1.000</td><td>0.996</td></tr><tr><td>Simplif. prod. ind.</td><td>0.209</td><td>0.252</td><td>0.759</td><td>0.824</td></tr><tr><td>Orthogonalising</td><td>0.903</td><td>0.504</td><td>1.000</td><td>1.000</td></tr><tr><td>Simplif. orthog.</td><td>0.226</td><td>0.258</td><td>0.812</td><td>0.852</td></tr><tr><td>Two-stage</td><td>0.798</td><td>0.789</td><td>1.000</td><td>1.000</td></tr><tr><td>Hybrid</td><td>0.798</td><td>0.788</td><td>1.000</td><td>1.000</td></tr><tr><td rowspan="6"> $\beta_{2}=0.50$ </td><td>Product indicator</td><td>0.999</td><td>0.828</td><td>1.000</td><td>1.000</td></tr><tr><td>Simplif. prod. ind.</td><td>0.373</td><td>0.473</td><td>0.963</td><td>0.985</td></tr><tr><td>Orthogonalising</td><td>0.992</td><td>0.815</td><td>1.000</td><td>1.000</td></tr><tr><td>Simplif. orthog.</td><td>0.417</td><td>0.468</td><td>0.981</td><td>0.992</td></tr><tr><td>Two-stage</td><td>0.924</td><td>0.903</td><td>1.000</td><td>1.000</td></tr><tr><td>Hybrid</td><td>0.925</td><td>0.904</td><td>1.000</td><td>1.000</td></tr></table>

Table 6 Multivariate tests (Wilks Lambda) over the statistical power to detect the quadratic effect

<table><tr><td>Effect</td><td>Sig.</td><td>Partial  $\eta^{2}$ </td></tr><tr><td>approach</td><td>&lt;0.001</td><td>0.325</td></tr><tr><td>approach × effect</td><td>&lt;0.001</td><td>0.083</td></tr><tr><td>approach × obs.</td><td>&lt;0.001</td><td>0.015</td></tr><tr><td>approach × weights</td><td>&lt;0.001</td><td>0.064</td></tr><tr><td>approach × effect × obs.</td><td>&lt;0.001</td><td>0.121</td></tr><tr><td>approach × effect × weights</td><td>&lt;0.001</td><td>0.013</td></tr><tr><td>approach × obs. × weights</td><td>&lt;0.001</td><td>0.003</td></tr><tr><td>4-way interaction</td><td>&lt;0.001</td><td>0.028</td></tr></table>

In order to test the influence of the experimental design factors on prediction accuracy, we again conduct an ANOVA with repeated measures – this time to explain the adjusted squared correlations between the endogen ous latent variable’s predicted and true scores. As previously, we use the approach as a within-subject factor, and the number of observations, the strength of the quadratic effect, and the homogeneity as betweensubject factors.

The analysis of variance (see Table 8) clearly identifies two dominant effects, namely the interaction of the approach and the number of observations and the direct effect of the approach. Both have partial $\eta ^ { 2 } .$ -values of more than 0.9. The interaction signifies that the differences between the approaches’ prediction accuracy vary with respect to different sample sizes. However, the ranking of the approaches does not change, which means that also the direct effect is interpretable. Pair-wise comparisons reveal that all the approaches differ significantly. Even the difference between the two-stage approach and the hybrid approach is significant $( P { < } 0 . 0 0 1 )$ , although its magnitude is clearly negligible.

## Recommendations

This article asks the question of how to optimally analyse formative constructs’ quadratic effects by means of variance-based SEM. We have provided an overview of the available PLS-based approaches and empirically compared them on the basis of a Monte Carlo simulation study. The consistent results obtained from this computational experiment permit us to provide clear-cut recommendations for researchers who want to analyse formative constructs’ quadratic effects by means of PLS path modelling.

Table 7 Squared correlations and adjusted squared correlations between predicted and true values of the endogenous variable

<table><tr><td rowspan="3">Quadratic effect</td><td rowspan="3">Approach</td><td colspan="2"> $cor^2(\hat{Y}, Y)$ </td><td rowspan="3">Free parameters</td><td colspan="2"> $cor^{2}_{adj}(\hat{Y}, Y)$ </td></tr><tr><td colspan="2">Observations</td><td colspan="2">Observations</td></tr><tr><td>100</td><td>500</td><td>100</td><td>500</td></tr><tr><td rowspan="6"> $\beta_2=0.00$ </td><td>Product indicator</td><td>0.475</td><td>0.294</td><td>74</td><td>-1.078</td><td>0.171</td></tr><tr><td>Simplif. prod. ind.</td><td>0.338</td><td>0.268</td><td>18</td><td>0.191</td><td>0.240</td></tr><tr><td>Orthogonalising</td><td>0.548</td><td>0.308</td><td>74</td><td>-0.792</td><td>0.187</td></tr><tr><td>Simplif. orthog.</td><td>0.356</td><td>0.271</td><td>18</td><td>0.213</td><td>0.243</td></tr><tr><td>Two-stage</td><td>0.305</td><td>0.260</td><td>10</td><td>0.227</td><td>0.245</td></tr><tr><td>Hybrid</td><td>0.305</td><td>0.260</td><td>10</td><td>0.227</td><td>0.245</td></tr><tr><td rowspan="6"> $\beta_2=0.15$ </td><td>Product indicator</td><td>0.486</td><td>0.311</td><td>74</td><td>-1.035</td><td>0.191</td></tr><tr><td>Simplif. prod. ind.</td><td>0.344</td><td>0.273</td><td>18</td><td>0.198</td><td>0.246</td></tr><tr><td>Orthogonalising</td><td>0.560</td><td>0.329</td><td>74</td><td>-0.741</td><td>0.212</td></tr><tr><td>Simplif. orthog.</td><td>0.363</td><td>0.277</td><td>18</td><td>0.221</td><td>0.250</td></tr><tr><td>Two-stage</td><td>0.318</td><td>0.280</td><td>10</td><td>0.242</td><td>0.266</td></tr><tr><td>Hybrid</td><td>0.318</td><td>0.280</td><td>10</td><td>0.242</td><td>0.266</td></tr><tr><td rowspan="6"> $\beta_2=0.35$ </td><td>Product indicator</td><td>0.538</td><td>0.392</td><td>74</td><td>-0.831</td><td>0.287</td></tr><tr><td>Simplif. prod. ind.</td><td>0.367</td><td>0.302</td><td>18</td><td>0.226</td><td>0.276</td></tr><tr><td>Orthogonalising</td><td>0.617</td><td>0.421</td><td>74</td><td>-0.516</td><td>0.320</td></tr><tr><td>Simplif. orthog.</td><td>0.389</td><td>0.306</td><td>18</td><td>0.253</td><td>0.280</td></tr><tr><td>Two-stage</td><td>0.379</td><td>0.371</td><td>10</td><td>0.309</td><td>0.358</td></tr><tr><td>Hybrid</td><td>0.379</td><td>0.371</td><td>10</td><td>0.309</td><td>0.358</td></tr><tr><td rowspan="6"> $\beta_2=0.50$ </td><td>Product indicator</td><td>0.605</td><td>0.498</td><td>74</td><td>-0.564</td><td>0.411</td></tr><tr><td>Simplif. prod. ind.</td><td>0.400</td><td>0.338</td><td>18</td><td>0.266</td><td>0.314</td></tr><tr><td>Orthogonalising</td><td>0.689</td><td>0.538</td><td>74</td><td>-0.230</td><td>0.458</td></tr><tr><td>Simplif. orthog.</td><td>0.424</td><td>0.344</td><td>18</td><td>0.296</td><td>0.319</td></tr><tr><td>Two-stage</td><td>0.456</td><td>0.485</td><td>10</td><td>0.395</td><td>0.475</td></tr><tr><td>Hybrid</td><td>0.456</td><td>0.485</td><td>10</td><td>0.395</td><td>0.475</td></tr></table>

Table 8 F-Tests over the factors influencing the adjusted prediction accuracy $( \mathsf { c o r } _ { a d j } ^ { 2 } ( \hat { Y } ,$ Y)) of the PLS path model

<table><tr><td>Effect</td><td>Sig.</td><td>partial  $\eta^{2}$ </td></tr><tr><td>approach</td><td>&lt;0.001</td><td>0.982</td></tr><tr><td>approach × effect</td><td>&lt;0.001</td><td>0.160</td></tr><tr><td>approach × obs.</td><td>&lt;0.001</td><td>0.969</td></tr><tr><td>approach × weights</td><td>&lt;0.001</td><td>0.063</td></tr><tr><td>approach × effect × obs.</td><td>&lt;0.001</td><td>0.119</td></tr><tr><td>approach × effect × weights</td><td>&lt;0.001</td><td>0.025</td></tr><tr><td>approach × obs. × weights</td><td>&lt;0.001</td><td>0.027</td></tr><tr><td>4-way interaction</td><td>&lt;0.001</td><td>0.011</td></tr></table>

One approach – the hybrid approach – can be said to be ranked first in the three criteria of parameter accuracy, statistical power, and prediction accuracy. The two-stage approach almost showed the same performance; differences between it and the hybrid approach – although statistically significant – were unsubstantial. These findings differ from those related to reflective constructs’ non-linear effects, in which the product indicator approach (Chin et al, 2003) and the orthogonalising approach (Henseler & Chin, 2010) excel. On the basis of our findings, it is possible to make recommendations for the analysis of quadratic effects by means of variancebased SEM.

If researchers want to analyse quadratic effects, they first should assess whether the hypothesised quadratic effect emerges from a formative or a reflective construct. If a reflective construct has a quadratic effect, researchers should follow the recommendations made by Henseler & Chin (2010). On the other hand, if a formative construct has a quadratic effect, researchers should check whether a software implementation of the hybrid approach is available. If it is available, researchers should use it to estimate and bootstrap the quadratic effect, otherwise they should apply the two-stage approach for estimation and bootstrapping. If the quadratic effect is found to be significant, one can start interpreting it. If it is not significant, it might be worthwhile also trying the product indicator approach, because it has a somewhat higher statistical power than the hybrid approach if there are small sample sizes.

For the interpretation of the non-linear effect, it should be noted that whereas the non-linear effect’s path coefficient may serve as a first entry to interpretation, the quadratic terms’ regression coefficient should not be the basis for assessing the quadratic effect’s strength (cf. Carte & Russell, 2003). Instead, Cohen’s (1988) $\scriptstyle \int ^ { 2 }$ effect size measure for hierarchical multiple regression can be applied. It is defined as:

$$
f ^ {2} = \frac {R _ {i n c l u d e d} ^ {2} - R _ {e x c l u d e d} ^ {2}}{1 - R _ {i n c l u d e d} ^ {2}},\tag{7}
$$

where $R _ { e x c l u d e d } ^ { 2 }$ is the variance accounted for by the independent variable as such, and $R _ { i n c l u d e d } ^ { 2 }$ is the combined variance accounted for by the independent latent variable’s linear and non-linear effects. By convention, $f ^ { 2 }$ effect sizes of 0.02, 0.15, and 0.35 are regarded as small, medium, and large, respectively (Cohen, 1988). Effect sizes smaller than 0.02 indicate a lack of substantiality. Since unsubstantial effects imply negligible influence on the explanandum, they should receive minimal attention. It is quite unlikely that these effects would yield important theoretical or managerial implications. However, substantial effects should be extensively discussed, and their theoretical and managerial implications highlighted.

Figure 2 is a flow chart, which sums up the recommendations.

In order to facilitate sample size decisions for studies incorporating formative constructs’ non-linear effects, we estimated the hybrid approach’s statistical power for sample sizes ranging from 50 to 500 by means of further Monte Carlo runs. The outcome is displayed in Figure $^ { 3 , }$ showing the hybrid approach’s statistical power for small, medium, and strong effects and for various sample sizes.

## Limitations and further research

It was our aim to compare the suitability of several PLS-based approaches for the analysis of formative constructs’ quadratic effects. Through this study, we have enabled researchers to easily examine formative constructs’ quadratic effects in a variance-based SEM framework. Our paper is thus an invitation to search for curvilinear and other non-linear effects – not only in IS research, but also in other management disciplines and beyond.

As shown, the hybrid approach requires a modification of the PLS algorithm. Unfortunately, none of the leading PLS software distributions – LVPLS (Lohmo¨ller, 1987), PLS-Graph (Chin/Soft Modeling, Inc., 1992–2002), SmartPLS (Ringle et al, 2007), SPAD-PLS (Test & Go, 2006), XLSTAT-PLS (Addinsoft, 2007) – has implemented $\operatorname { i t } ,$ so that this approach is not as yet available for researchers. Given the hybrid approach’s favourable characteristics regarding the estimation of formative constructs’ non-linear effects, a software implementation in the not-too-distant future is highly desirable. We therefore encourage PLS software providers to take this further step. Another promising option is the plspm package (Sa´nchez & Trinchera, 2010), which is part of the open source project R (R Development Core Team, 2007), because it permits the PLS algorithm to be modified. However, analysts can always make use of the two-stage approach, which demonstrated a performance almost equal to that of the hybrid approach.

![](/api/attachments/2S6257B6/fulltext/images/d01aa7a9d9fcc9e7a5dc66166e0b12e9a0dd7740067204703d831ac51e1785fa.jpg)  
Figure 2 Framework for determining quadratic effects in PLS path models.

![](/api/attachments/2S6257B6/fulltext/images/116a2f8d6811ec7a15a0e2d5e52c9b34e480cf451a23e14f75813b3f1196ecdf.jpg)  
Figure 3 Estimated marginal means of the statistical power to detect a quadratic effect of $\beta _ { 2 } = 0 . 1 5$

Since we limited our study to PLS-based approaches, other SEM techniques like LISREL and regressions of summated scales were not considered. For direct effects, a comparison of the biases in PLS estimates with the biases in the estimates of covariance structure-based SEM has already been carried out elsewhere (cf. Cassel et al, 1999; Reinartz et al, 2009). However, it may be fruitful to extend such research to incorporate both PLS and LISREL

## About the authors

Jo¨rg Henseler is an Associate Professor at the Institute for Management Research, Nijmegen School of Management, Radboud University Nijmegen, The Netherlands, and a Visiting Professor at The Higher Institute of Statistics and Knowledge Management (ISEGI), Universidade Nova de Lisboa, Portugal. His research interests encompass structural equation modelling marketing research, service management, and innovation management. He has published in scholarly journals including Computational Statistics, International Journal of Research in Marketing, and Structural Equation Modeling, and he is editor of two handbooks on partial least squares path modelling.

Georg Fassott is an Associate Professor in the Faculty of Business Studies and Economics at the University of Kaiserslautern, Germany. His research interests are in the areas of e-commerce, entrepreneurial marketing, and structural equation modelling. His recent articles have appeared in journals such as International Journal of Internet Marketing and Advertising, International Marketing Review, Journal of Consumer Behaviour, and Journal of Relationship Marketing.

## References

ADDINSOFT (2007) XLSTAT-PLS. Addinsoft, Paris, France.

ALBERS S (2010) PLS and success factor studies in marketing. In Handbook of Partial Least Squares: Concepts, Methods, and Applications. Vol. II of Computational Statistics (ESPOSITO VINZI V, CHIN WW, HENSELER J and WANG H. Eds), pp 409–425. Springer, Heidelberg.

BOLLEN KA and LENNOX R (1991) Conventional wisdom on measurement: a structural equation perspective. Psychological Bulletin 110(2), 305–314.

BUSEMEYER JB and JONES LE (1983) Analysis of multiplicative combination rules when causal variables are measured with error. Psychologica Bulletin 93(3). 549–562.

approaches to model formative constructs’ quadratic effects.

The hybrid approach and the two-stage approach clearly demonstrated the best parameter accuracy of all approaches. However, in absolute terms, these two approaches are also imperfect. Both tend to underestimate the quadratic effect. A potential solution might be a correction for attenuation, as suggested by Henseler et al (2009) in the context of formative measurement or by Dijkstra (2010) for use with PLS in general.

Finally, our empirical findings regarding non-linear effects were limited to quadratic terms. Future research could strive for the replication of our recommendations with other polynomial terms or other commonly used non-linear functions such as exponential or logarithmic functions.

Theo K. Dijkstra is a Professor at the University of Groningen, The Netherlands. He was a Fulbright scholar at the University of California, Department of Psychology. He has published in journals including Econometrica, Psychometrika, The International Economic Review, and the British Journal of Mathematical and Statistical Psychology. He also worked for an institutional asset manager, responsible for the development of decision support tools and portfolio strategies. His research interests include statistical methodology, multivariate statistics, multicriteria decision analysis, and partial least squares.

Bradley Wilson is a Senior Lecturer in the School of Media and Communication, RMIT University, Melbourne, Australia. He has published in the Handbook of Partial Least Squares, Industrial Marketing Management, Sport Marketing Quarterly, International Journal of Sports Marketing and Sponsorship, Public Relations Review and International Journal of Sport Management and Marketing. His research encompasses branding, communication, sponsorship, crises and cause-related marketing often utilising advanced multivariate methods developments.

CARTE TA and RUSSELL CJ (2003) In pursuit of moderation: nine common errors and their solution. MIS Quarterly 27(3), 479-501.

CASSEL C. HACKL P and WESTLUND A (1999) Robustness of partial least squares method of estimating latent variable quality structures. Journal of Applied Statistics 26(4), 435–446.

CHIN WW (1998) The partial least squares approach to structural equation modeling. In Modern Methods for Business Research (MARCOULIDES GA, Ed), pp 295–336, Lawrence Erlbaum Associates, Inc.. Mahwah. NI.

CHIN WW, MARCOLIN BL and NEWSTED PR (1996) A partial least squares latent variable modeling approach for measuring interaction effects. Results from a Monte Carlo simulation study and voice mail emotion/ adoption study. In Proceedings of the Seventeenth International Conference on Information Systems (DeGROSS JI, JARVENPAA S and SRINIVASAN A, Eds), pp 21–41, Cleveland, OH.

CHIN WW, MARCOLIN BL and NEWSTED PR (June 2003) A partial least squares latent variable modeling approach for measuring interaction effects. Results from a Monte Carlo simulation study and an electronic-mai emotion/adopion study. Information Systems Research 14(2), 189–217.

COHEN J (1978) Partialed products are interactions; partialed powers are curve components. Psychological Bulletin 85(4), 858–866.

COHEN J (1988) Statistical Power Analysis for the Behavioral Sciences, 2nd edn, Lawrence Erlbaum Associates, Hillsdale.

CORTINA JM (1993) Interaction, nonlinearity, and multicollinearity: implications for multiple regression. Journal of Management 19(4), 915–922.

CRONBACH LJ (1987) Statistical tests for moderator variables: flaws in analyses recently proposed. Psychological Bulletin 102(3), 414–417.

DIAMANTOPOULOS A (2006) The error term in formative measurement models: interpretation and modeling implications. Journal of Modelling in Management 1(1), 7–17.

DIAMANTOPOULOS A and SIGUAW JA (2006) Formative versus reflective indicators in organizational measure development: a comparison and empirical illustration. British Journal of Management 17(4), 263–282.

DIAMANTOPOULOS A and WINKLHOFER HM (2001) Index construction with formative indicators: an alternative to scale development. Journal of Marketing Research 38(2), 269–277.

D TK (2010) Latent variables and indices: Herman Wold’s basic design and partial least squares. In Handbook of Partial Least Squares: Concepts, Methods, and Applications. Vol. II of Computational Statistics (VINZI VE, CHIN WW, HENSELER J and WANG H, Eds), pp 23–46, Springer, Heidelberg.

DIJKSTRA TK and HENSELER J (forthcoming) Prescriptions for dimension reduction, with interacting factors. Quality & Quantity 26(3), 438–445.

ECHAMBADI R and HESS J (2007) Mean-centering does not alleviate collinearity problems in moderated multiple regression. Marketing Science 26(3), 438–445.

FORNELL C (1982) A second generation of multivariate analysis: an overview. In A Second Generation of Multivariate Analysis (F C, Ed), Vol. 1, pp 1–21, Greenwood, Westport.

FORNELL C and LARCKER DF (1981) Evaluating structural equation models with unobservable variables and measurement error. Journa of Marketing Research 18(1), 39–50.

GEFEN D and STRAUB D (1997) Gender differences in the perception and use of e-mail: an extension to the technology acceptance model. MIS Quarterly 21(4), 389–400.

GIBSON C and BIRKINSHAW J (2004) The antecedents, consequences, and mediating role of organizational ambidexterity. Academy of Management Journal 47(2), 209–226.

G D, L W and T R (2007) Statistical power in analyzing interaction effects: questioning the advantage of PLS with product indicators. Information Systems Research 18(2), 211–227.

HENSELER J (2010) On the convergence of the partial least squares path modeling algorithm. Computational Statistics 25(1), 107–120.

HENSELER J and CHIN WW (2010) A comparison of approaches for the analysis of interaction effects between latent variables using partial least squares path modeling. Structural Equation Modeling: A Multidisciplinary Journal 17(1), 82–109.

HENSELER J and FASSOTT G (2010) Testing moderating effects in PLS path models: an illustration of available procedures. In Handbook of Partial Least Squares: Concepts, Methods, and Applications. Vol. II of Computational StatistiCs (EsPOSITO VINZI V. CHIN WW. HENSELER I and WANG H, Eds), pp 713–735, Springer, Heidelberg.

HENSELER J, RINGLE CM and SINKOVICS RR (2009) The use of partial least squares path modeling in international marketing. Advances in International Marketing 20, 277–319.

JARVIS CB, MACKENZIE SB and PODSAKOFF P (2003) A critical review of construct indicators and measurement model misspecification in marketing and consumer research. Journal of Consumer Research 30(2). 199–218.

JONSSON FY (1998) Nonlinear structural equation models: the kenny-judd model with interaction effects. In Interaction and Nonlinear Effects in Structural Equation Modeling (SCHUMACKER RE and MACOULIDES GA, Eds), pp 17–42, Lawrence Erlbaum Associates, Mahwah, NJ.

Jo¨RESKOG KG and YANG F (1996) Nonlinear structural equation models: the Kenny-Judd model with interaction effects. In Advanced Structural Equation Modeling: Issues and Techniques (MACOULIDES GA and SCHUMACKER RE, Eds), pp 57–88, Lawrence Erlbaum Associates, Hillsdale, NJ.

KENNY DA and JUDD CM (1984) Estimating the nonlinear and interactive effects of latent variables. Psychological Bulletin 96(1), 201–210.

LANCE CE (1988) Residual centering, exploratory and confirmatory moderator analysis, and decomposition of effects in path models containing interactions. Applied Psychological Measurement 12(2), 163–175.

LITTLE TD, BOVAIRD JA and WIDAMAN KF (2006) On the merits of orthogonalizing powered and product terms: implications for modeling interactions among latent variables. Structural Equation Modeling 13(4), 497–519.

LOHMo¨LLER J-B (1987) LVPLS 1.8 Program Manual: Latent Variable Path Analysis with Partial Least Squares Estimation. Zentralarchiv fu¨r Empirische Sozialforschung, Universita¨t zu Ko¨ln, Cologne, Germany.

LOHMo¨LLER J-B (1989) Latent Variable Path Modeling with Partial Least Squares. Physica, Heidelberg.

MARSH H, WEN Z and HAU K (2006) Structural equation models of latent interaction and quadratic effects. In Structural Equation Modeling: A Second Course (HANCOCK GR and MUELLER RO, Eds), pp 225–265, IAS, Charlotte, NC.

M HW, W Z and H KT (2004) Structural equation models of latent interactions: evaluation of alternative estimation strategies and indicator construction. Psychological Methods 9(3), 275–300.

MATHIESON K, PEACOCK E and CHIN W (2001) Extending the technology acceptance model: the influence of perceived user resources. ACM SIGMIS Database 32(3), 86–112.

M B and A J (2002) Comparison of methods for estimating and testing latent variable interactions. Structural Equation Modeling: A Multidisciplinary Journal 9(1), 1–19.

PETTER S, STRAUB D and RAI A (2007) Specifying formative constructs in information systems research. MIS Quarterly 31(4), 623–656.

PODSAKOFF N, SHEN W and PODSAKOFF P (2006) The role of formative measurement models in strategic management research: review, critique, and implications for future research. Research Methodology in Strategy and Management 3(1), 197–252.

R D C T (2007) R: A Language and Environment for Statistical Computing. R Foundation for Statistical Computing. Vienna, Austria. [WWW document] http://www.R-project.org.

R WJ, E R and C WW (2002) Generating nonnorma data for simulation of structural equation models using Mattson’s method. Multivariate Behavioral Research 37(2), 227–244.

R WJ, H M and H J (2009) An empirical comparison of the efficacy of covariance-based and variance-based SEM. International Journal of Research in Marketing 26(4), 332–344.

RINGLE CM, WENDE S and WILL A (2007) SmartPLS 2.0 M3. University of Hamburg, Hamburg, Germany. [WWW document] http://www .smartpls.de.

SA<sup>´</sup>NCHEZ G and TRINCHERA L (2010) plspm – Partial Least Squares Data Analysis Methods. Universitat Politecnica de Catalunya. [WWW document] http://cran.r-project.org/web/packages/plspm/.

SCHUMACKER RE and MARCOULIDES GA (Eds) (1998) Interaction and Nonlinear Effects in Structural Equation Modeling. Lawrence Erlbaum Associates, Mahwah, NJ.

SOFT MODELING, INC (1992–2002) PLS-Graph Version 3.0. Houston, TX. [WWW document] http://www.plsgraph.com.

TENENHAUS M, VINZI VE, CHATELIN YM and LAURO C (2005) PLS path modeling. Computational Statistics and Data Analysis 48(1), 159-205.

TEST & GO (2006) SPAD Version 6.0.0. Test & Go, Paris, France.

WILSON B (2010) Using PLS to investigate interaction effects between higher order brand constructs. In Handbook of Partial Least Squares: Concepts, Methods, and Applications. (ESPOSITO VINZI V, CHIN WW, HENSELER J and WANG H, Eds), Vol. II of Computational Statistics pp 621–654. Springer. Heidelberg

WIXOM B and WATSON H (2001) An empirical investigation of the factors affecting data warehousing success. MIS Quarterly 25(1), 17–41.

WOLD HOA (1966) Non-linear estimation by iterative least squares procedures. In Research Papers in Statistics (DAVID FN, Ed), pp 411–444, Wiley, London, New York, Sydney.

WOLD HOA (1982) Soft modelling: the basic design and some extensions. In Systems Under Indirect Observation. Causality, Structure,

Prediction Vol. II. (JO¨ RESKOG KG and WOLD HOA, Eds), pp 1–54, North-Holland, Amsterdam, New York, Oxford.

WOLD S, KETTANEH-WOLD N and SKAGERBERG B (1989) Nonlinear PLS modeling. Chemometrics and Intelligent Laboratory Systems 7(1), 53–65.

YI M and DAVIS F (2003) Developing and validating an observational learning model of computer software training and skill acquisition. Information Systems Research 14(2), 146–169.
