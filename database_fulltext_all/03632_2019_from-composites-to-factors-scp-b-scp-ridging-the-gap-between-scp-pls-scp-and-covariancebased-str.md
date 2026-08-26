---
otero_id: 3632
otero_key: "NTW5UZWR"
title: "From composites to factors: <scp>B</scp>ridging the gap between <scp>PLS</scp> and covariance‐based structural equation modelling"
authors: "Ned Kock"
year: "2019"
journal: "Information Systems Journal"
doi: "10.1111/isj.12228"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
R E S E A R C H A R T I C L E

# From composites to factors: Bridging the gap between PLS and covariance‐based structural equation modelling

Ned Kock

Division of International Business and Technology Studies, Texas A&M International University, Laredo, Texas

Correspondence

Ned Kock, Division of International Business and Technology Studies, Texas A&M International University, 5201 University Boulevard, Laredo, TX 78041. Email: nedkock@gmail.com

## Abstract

Partial least squares (PLS) methods possess desirable characteristics that have led to their extensive use in the field of information systems, as well as many other fields, for path analyses with latent variables. Such variables are typically conceptualized as factors in structural equation modelling (SEM). In spite of their desirable characteristics, PLS methods suffer from a fundamental problem: Unlike covariance‐based SEM, they do not deal with factors, but with composites, and as such do not fully account for measurement error. This leads to biased parameters, even as sample sizes grow to infinity. Anchored on a new conceptual foundation, we discuss a method that builds on the consistent PLS technique and that estimates factors, fully accounting for measurement error. We provide evidence that this new method shares the property of statistical consistency with covariance‐based SEM but, like classic PLS methods, has greater statistical power. Moreover, our method provides correlation‐preserving estimates of the factors, which can be used in a variety of other tests. For readers interested in trying it, the new method is implemented in the software WarpPLS. Our detailed discussion should facilitate the implementation of the method in any numeric computing environment, including open source environments such as R and GNU Octave.

## KEYWORDS

measurement error, Monte Carlo simulation, partial least squares, path bias, structural equation modelling, variation sharing

## 1 | INTRODUCTION

The field of information systems (IS) is closely associated with the development, implementation, assessment, and use of the partial least squares (PLS) method (Chin, 1998; Chin, Marcolin, & Newsted, 2003; Dijkstra & Henseler, 2015a; Kock, 2010; Kock & Hadaya, 2018). This method, developed by Wold (1980), has been extensively used in IS studies, as well as in studies in many other fields, to investigate path models with latent variables (Dijkstra & Henseler, 2015a; Goodhue, Lewis, & Thompson, 2012; Kock & Hadaya, 2018). More often than not, latent variables are quantifications of mental constructs, for which multiple imprecise direct measures (indicators) are obtained via questionnaires. In this context, PLS has often been compared with the classic covariance‐based approach to structural equation modelling (SEM)

Such comparisons have led to a continuing and often antagonistic debate among proponents and detractors of PLS (Henseler et al., 2014; Rigdon, 2012; Rönkkö & Evermann, 2013; Rönkkö, McIntosh, & Antonakis, 2015). While this debate has addressed numerous issues, it has often gravitated around one main problem: PLS and related methods do not deal with factors, but with composites. Composites aggregate indicators but do not fully incorporate measurement error and thus can only be seen as approximations of factors. In large part, because of their focus on composites, PLS methods yield biased estimates of various parameters even as sample sizes grow to infinity. Among these asymptotically biased parameters are path coefficients, indicator weights, and indicator loadings

Despite this problem, PLS methods have some clear advantages over covariance‐based SEM, which have led to their growing use. Notably, they virtually always converge to solutions, even with very small sample sizes. This is useful in cases where IS researchers want to investigate small populations (eg, N < 50) to which they have full access, although a combination of weak effects and small sample sizes may lead to problems such as capitalization on error (see, eg, Goodhue, Lewis, & Thompson, 2007; Kock & Hadaya, 2018). Also, PLS methods do not normally have iden tification problems, allowing for the development of fairly complex models and their test with a limited number of indicators.

We make here what we believe to be an important contribution to this debate surrounding PLS methods Anchored on a new conceptual foundation, we discuss a method that combines elements of current PLS methods and covariance‐based SEM and that provides estimates of the composites and correlation‐preserving factors in a path model. In our method, the factors are estimated so as to preserve their true correlations (see, eg, DiStefano, Zhu, & Mindrila, 2009), which addresses the well‐known correlation attenuation problem (Hakstian, Schroeder, & Rogers, 1988; Johnson, 1950; Nunnally & Bernstein, 1994; Nunnaly, 1978). In path models, this problem is frequentl characterized by path coefficient estimates that asymptotically converge to values that underestimate the true value (Goodhue et al., 2012).

Our method builds on the consistent PLS technigue (Diikstra & Henseler. 2015a. 2015b: Diikstra & Schermelleh Engel, 2014), which is a parameter correction technique. Nevertheless, our method, which we refer to as PLSF (where the “F” is a reference to its focus on factor estimation), is not a parameter correction technique. Generally speaking, PLS‐based parameter correction techniques adjust parameters estimated via PLS methods to correct for bias (Dijkstra & Schermelleh‐Engel, 2014; Goodhue et al., 2012; Rönkkö, 2014). Our method estimates prototypical elements, such as factors, which are then used in the production of parameters. As such, no corrections are needed. The consistent PLS technique is used in the estimation of a few coefficients in the early stages of our method, notably the reliabil ities, which are nevertheless critical elements

Diikstra & Henseler (2015a, p. 17) noted that “Not only does [IS] research make ample use of PL S as a method of analysis, but also many extensions and advances of PLS can be credited to [IS] researchers.” We agree with this statement and hope that the PLSF method will be seen as a contribution to this tradition. Our PLSF method is the culmination of several years of research on the basic elements that make it up. Particularly important among those elements is a function that fits a matrix of correlations among composites to a matrix of correlations among factors, which will be discussed later. This function relies on reliability measures. Previous attempts have led to approaches that were less accurate under certain conditions, due to relying on biased reliability estimates, or less computationall efficient, due to the need for nested iterations to converge to more accurate reliability estimates. The method discussed here is so far the one with the broadest range of application, and the greatest computational efficiency.

We provide evidence that our method shares the property of consistency with covariance‐based SEM but, like classic PLS, has greater statistical power. The term “classic PLS” is used from this point forward to refer to current composite‐based PLS methods, particularly PLS mode A (Lohmöller, 1989), and thus to differentiate them from our factor‐based PLSF method. Our method provides estimates of factor scores, which can be used in a variety of other tests. Among such tests are two that have been developed in the field of IS and have been widely used in a variety of fields since their publication: full collinearity tests, which concurrently assess both lateral and vertical collinearity among factors (Kock & Lynn, 2012), and factor nonlinearity tests, where best‐fitting nonlinear functions are esti mated for each pair of linked factors and subseguently used in the estimation of nonlinear path coefficients (Guo Yuan, Archer, & Connelly, 2011; Kock, 2010; Moqbel, Nevo, & Kock, 2013). For readers interested in testing our new method, it is implemented in a widely used commercial SEM software, namely, WarpPLS (Kock, 2010, 2018).

Our discussion is organized as follows. We start by describing an illustrative model, based on IS theory and related empirical work, which we use as a basis for discussion and to generate data for analyses as a true population model. Next, we discuss the PLSF method as a set of four main stages, including a discussion of composites and factors, and how we can go from composites to factors, which is in part what the PLSF method does. A more technica discussion of the PLSF method follows, where it is presented as a set of four main functions. We proceed with an assessment of the method's performance against three other methods, including covariance‐based SEM via full‐information maximum likelihood (FIML). This is done through the juxtaposition of results from analyses of a finite population and from a Monte Carlo experiment. We conclude with a discussion of our findings and its implications. For simplicity, and without any impact on the generality of our discussion, all variables are standardized—ie, scaled to have a mean of zero and standard deviation of one

## 2 | ILLUSTRATIVE MODEL

Figure 1 shows an illustrative model that we will use in the discussion that follows. The model is also used later as a starting point for us to generate data for analyses, as a true population model. It is based on theory and results from field studies and controlled experiments (Kock, 2003, 2007; Kock, Danesh, & Komiak, 2008; Kock & Murphy, 2001; Kock, Verville, Danesh‐Pajou, & DeLuca, 2009), notably a field study involving 156 individuals participating in business process redesign projects employing information technology (IT) solutions to process problems (Kock et al. 2009) and a controlled experiment involving 210 graduate business students majoring in IS (Kock et al., 2008)

![](/api/attachments/NTW5UZWR/fulltext/images/05e55b9c9da710c06c617c546f00b6032182b9027585667ec8ed067f62082004.jpg)  
FIGURE 1 Illustrative model

The model contains five factors, associated with the following constructs: communication flow orientation (CO, $F _ { 1 } ) ;$ ease of understanding (EU, $F _ { 2 } ) ;$ usefulness in the development of IT solutions (GT, $F _ { 3 } ) ;$ accuracy (AC, $F _ { 4 } ) ;$ ; and impact on redesign success (SU, F ). This model is based on communication flow optimization theory (Kock, 2003 2007; Kock et al., 2008, 2009; Kock & Murphy, 2001), a theory that has been developed and validated within the field of IS.

Business processes are sets of interrelated activities (Kock, 2007; Mendling, Strembeck, & Recker, 2012), by which virtually any good or service is produced in organizations. For example, the set of interrelated activities involved in assembling a car, carried out by an automaker, is a business process. Communication flow optimization theory's main domain of application are efforts whereby business processes are analysed, redesigned, and implemented with IT. One of the theory's main predictions is that the extent to which the business process representations used in these efforts focus on how communication takes place in organizations positively affect redesign success. Among other things, the theory highlights the importance of understanding how information and knowledge flow in organizations in order to successfully redesign the organizations' processes with the help of IT.

According to the theory, the overall effect of communication flow orientation on business process redesign success, with respect to the business process representations used, is fully mediated by a few elements that relate to the representations. Chiefly, among these elements are a representation's ease of understanding $( \mathsf { C O } > \mathsf { E U } > \mathsf { S U } )$ , usefulness in the development of IT solutions $( \mathsf { C O } \circ \mathsf { \Sigma } > \mathsf { G T } > \mathsf { S U } )$ , and accuracy $( \mathsf { C O } \circ \mathsf { \Sigma } \circ \mathsf { A C } \circ \mathsf { S U } )$ ). The full mediation is expressed in the model through a path coefficient of magnitude zero for the direct link $\mathsf { C O } > \mathsf { S U }$ . That is, the overal effect of CO on SU is fundamentally an indirect effect.

The various parameters in the model were set based on consistency with the theory and empirical validation studies, variability and complexity for testing purposes, and challenges to our PLSF method. For example, the path coefficients are all different from one another and go from a low value of 0.157 to a high value of 0.542. Also, the loadings cover a range of heterogeneity options, going from no heterogeneity (eg, EU, where all loadings are th same) to high heterogeneity (SU, where all loadings are different). Finally, the inclusion of a single‐item construc (CO) poses a challenge to our PLSF method because, as it will be seen later, it prevents this construct from receiving variation when we go from composites to factors; this is due to the fact that CO, with a loading of 1, is measured without error.

While neither the theory nor the empirical studies that led to it or validated it are the foci of this paper, the fact that our illustrative model is based on a carefully developed and tested theory lends credence to the model's viability. This is important because the model is reasonably complex. Moreover, using a model based on an IS theory make our contribution more meaningful to an IS audience, while hopefully also being meaningful to readers from other fields.

The complexity of the model allows us to incorporate a broad set of comparison criteria into our analyses reflected in a significant variation in several elements such as reliabilities, number of indicators, loadings, loading het erogeneity within each factor, weights, and redundancy measures. For example, reliabilities ranged from 0.757 to 1 and loadings from 0.507 to 1. Such a variation in comparison criteria allowed us to provide a more complete view of the performance of the PLSF method against other methods, without the level of repetition that would have been required should we have chosen to analyse a variety of simpler models. Moreover, using a more complex mode posed challenges to the methods that would not be present in fairly simple models

## 3 | THE PLSF METHOD: FOUR MAIN STAGES

The PLSF method generates estimates of the composites and factors, with these serving as the foundation for the generation of asymptotically unbiased estimates of various model parameters. The method can be seen as being made up of four main stages. This section provides a high‐level overview of these stages, with the goal of giving the reader a broad conceptual understanding of the method. The PLSF method builds on key elements from classic measurement error theory (Nunnally & Bernstein, 1994; Nunnaly, 1978) and the common factor model (Kline, 2010; MacCallum & Tucker, 1991).

## 3.1 | Stage 1: consistent PLS

While our method's main goal is to estimate model parameters by estimating factors, in empirical studies, only factor indicators are available. Since each indicator measures the corresponding factor with error, the indicators themselves do not explain 100% of the variance in the factor. The percentage of the variance explained in the factor (eg, 73%) by its indicators is the reliability associated with the factor. The remaining variance (eg, 27%) is explained by what we cal the “measurement residual,” which is uncorrelated with the factors' indicators.

Given the above, the reliability associated with a factor becomes a critical ingredient for the PLSF method. The reliability must be estimated early on in our PL SE method, in its first stage (ie, stage 1). because it can then serve a the basis for the estimation of the composite associated with the factor in stage 2. The reliability estimate is provided by the consistent PLS technique, which also provides estimates of the factor‐indicator loadings, for each factor These estimates have been shown to be asymptotically unbiased (Dijkstra & Henseler, 2015a, 2015b; Dijkstra $\&$ Schermelleh‐Engel, 2014). This makes the reliability estimate generated by consistent PLS more desirable for our method than other widely used reliability estimates, such as the Cronbach alpha coefficient and the composite reli abilities calculated based on loadings produced by classic PLS algorithms (Dillon & Goldstein, 1984; Peterson & Yeolib, 2013; Sijtsma, 2009).

## 3.2 | Stage 2: composite estimation

In stage 2, we use the reliabilities and loadings from stage 1 to estimate the composites associated with the factors Each of these composites is, like all composites, an exact linear combination of the indicators. However, because of the assumption that each of these composites is uncorrelated with the corresponding measurement residual, it differs from the composites estimated via classic PLS algorithms (Adelman & Lohmoller, 1994; Lohmöller, 1989; McIntosh Edwards, & Antonakis, 2014). The key difference is that each composite is estimated, as a weighted aggregation of the indicators, so that it accounts exactly for the variance explained in the corresponding factor—the reliability associated with the factor.

Once the composites are estimated, we can then calculate the correlations among those composites, which we know to be attenuated with respect to the corresponding factor correlations (Nunnally & Bernstein, 1994; Nunnaly, 1978). That is, for each pair of composites $C _ { j }$ and $C _ { j } ,$ and corresponding factors $F _ { j }$ and $F _ { j } ,$ the correlation between the composites $\Sigma _ { C _ { i } C _ { j } }$ has a lower absolute magnitude than the correlation between the factors $\Sigma _ { F _ { i } F _ { j } }$ .The magnitude of this attenuation is given by the equation below, where $\rho _ { j }$ and $\rho _ { j }$ are the reliabilities associated with factors $F _ { j }$ and $F _ { j } .$

$$
\Sigma_ {F _ {i} F _ {j}} = \frac {\Sigma_ {C _ {i} C _ {j}}}{\sqrt {\rho_ {i} \rho_ {j}}}.
$$

As we can see, since we have estimates of the reliabilities from stage 1 and of the composite correlations, we can therefore easily estimate the correlations among each pair of factors $\sum _ { F _ { i } F _ { j } }$ . This allows us, in stage 3, to go from composites to factors. This is done by gradually sharing variation among composites and measurement residuals, until the composites “become” factors. We know precisely when this is achieved: when the correlations among composites reach the expected estimated correlations among factors. While iterations take place to achieve this, the correlations among the composites and measurement residuals associated with their corresponding factors are kept at zero.

## 3.3 | Stage 3: factor estimation

At the end of stage 2, we obtain estimates of composites that are uncorrelated with measurement residuals. Since the measurement residuals account for the variance in the factors that are not accounted for by the composites, they should be correlated with their corresponding factors and also with other factors in the model. The reason for this is that factors share variation with one another due to the cause‐and‐effect network that connects them.

In stage 3, we start by estimating the correlations among factors based on the correlations among composites and the reliabilities. We also initialize the factors by aggregating the composites and measurement residuals obtained from stage 2. We then iteratively recover the variation shared among composites and measurement residuals into the factors, until convergence is achieved.

The above happens when the correlations among the emerging factors match the target correlations, which were earlier estimated via the correlation attenuation equation. The resulting factors will not incorporate exactly the same patterns of randomness found in the original factors. Those are unique and unrecoverable (Mueller, 1996). However while post‐estimation random patterns will be unique, they will be reduced to uncorrelated error that will have no effect on any parameter estimation (Bentler & Huang, 2014).

## 3.4 | Stage 4: full parameter estimation

In stage 4, we use the factor estimates from stage 3 to obtain various model parameters, of which many becom available. This is done based on the premise that the factors are the original sources of all variation in the model, even though some of the parameters of interest may have already been estimated in intermediate stages. For example, we can estimate loadings by regressing indicators on factors, and weights by regressing factors on indicators. Like in covariance‐based SEM, these parameters are expected to be asymptotically unbiased.

At the end of stage 4, we are left with a collection of correlated factors, where the correlations are expected to match those among the original true factors. For each pair of correlated factors, we end up with the pattern of cor relations schematically illustrated in Figure 2. The factors aggregate composites and measurement residuals. The composite and measurement residual associated with one factor are correlated with the composite and measurement residual associated with the other factor. However, a composite and measurement residual associated with the same factor are uncorrelated.

Conceptually, the PLSF method attempts to recover factors from the indicators used to measure them, where each indicator is an imprecise measure of the factor. To do so, PLSF first estimates composites, whic are unique to the method. The PLSF method assumes that a factors' measurement residual explains the variance in the factor that is not explained by the composite that is made up of the indicators, with the variance in th factor that is explained by composite, and thus by the indicators, being equal to the reliability associated with the factor.

![](/api/attachments/NTW5UZWR/fulltext/images/3e7cc14b5a9d7928350b142ada50096323c661b1e2c8d39a7b29ade1790c7290.jpg)  
Notes: full line = nonzero correlation; dashed line = zero correlation  
FIGURE 2 Correlations among model elements

From the above, we can see that the PLSF method conceptualizes factors as aggregations of composites and measurement residuals, where the composites are in turn aggregations of indicators. The composite and measurement residual weights are obtained directly from the reliabilities estimated in stage 1. The measurement residuals are uncorrelated with the indicators in the same factors, and thus with the composites in the same factors. However, the measurement residuals are correlated with the indicators and measurement residuals associated with other fac tors in the same model.

## 4 | THE PLSF METHOD: FOUR MAIN FUNCTIONS

The PLSF method can be seen as being composed of four main functions: ${ \mathcal { F } } _ { 1 }$ , the consistent PLS function; $\mathcal { F } _ { 2 }$ , the composite estimation function; $\mathcal { F } _ { 3 }$ , the factor estimation function; and ${ \mathcal { F } } _ { 4 }$ , the full parameter estimation function The execution of each function refers to a PLSF stage, for a total of four stages.

## 4.1 | Function $\mathcal { F } _ { 1 }$ : the consistent PLS function

This function, expressed in equation form below, takes as inputs the matrix x of all indicators, and the matrix con taining the model specification. The matrix x has N rows, where N is the sample size, and one column for each of th indicators in the model. The matrix S is made up of two submatrices: one specifying factor‐factor associations and the other specifying indicator‐factor associations—ie, specifying the structural and measurement model links, respec tively. The outputs of function ${ \mathcal { F } } _ { 1 }$ include a column vector $\widehat { \rho }$ containing estimates of the reliabilities associated with all of the factors in the model, and a matrix $\widehat { \lambda }$ of estimates of the loadings for all factors. This function also produces initial estimates of the matrices $\widehat { c }$ and ω of composites and indicator weights, based on the basic design of PLS mode A, which will be used as starting values in the next stage.

$$
\left[ \widehat {\rho}, \widehat {\lambda}, \widehat {C}, \widehat {\omega} \right] = \mathcal {F} _ {1} (\mathsf {x}, \mathcal {S}).
$$

The consistent PLS technique is discussed in detail by Dijkstra and Schermelleh‐Engel (2014), and Dijkstra and Henseler (2015a, 2015b). The corresponding function ${ \mathcal { F } } _ { 1 }$ produces its outputs by first estimating composite weight via the basic design of PLS mode A (Lohmöller, 1989, p. 29), also known as PLS mode A employing the centroid scheme. Then, estimates of the reliabilities and loadings are generated.

## 4.2 | Function $\mathcal { F } _ { 2 } { : }$ the composite estimation function

This function takes as inputs x, $\widehat { \rho } , \widehat { \lambda } , \widehat { C } _ { : }$ , and ω. The composites in the matrix $\hat { c }$ and the indicator weights in the matrix ω are used as initial values, whereas the reliabilities in $\widehat { \rho }$ and loadings in $\widehat { \lambda }$ are fixed across the iterations carried out within $\mathcal { F } _ { 2 }$ . As expressed in equation form below, the outputs of this function comprise the following model‐wide esti mates: a matrix $\widehat { c }$ of composites; a matrix $\widehat { \omega }$ of weights; vectors $\widehat { \omega } _ { C }$ and $\widehat { \omega } _ { \varepsilon }$ of composite and measurement residua weights, respectively; and a matrix $\widehat { \varepsilon }$ of measurement residuals.

$$
\left[ \widehat {C}, \widehat {\omega}, \widehat {\omega} _ {C}, \widehat {\varepsilon}, \widehat {\omega} _ {\varepsilon} \right] = \mathcal {F} _ {2} (x, \widehat {\rho}, \widehat {\lambda}, \widehat {C}, \widehat {\omega}).
$$

It is clear from our previous discussion on composites and factors that each composite is completely determine by its indicators, aggregated based on appropriate weights. The indicators are uncorrelated with the corresponding measurement residual. Therefore, the matrix $\widehat { \varepsilon }$ produced and initially used internally by $\mathcal { F } _ { 2 }$ is at first a matrix of random uncorrelated “noise,” which at the conclusion of $\mathcal { F } _ { 2 }$ stores measurement residuals that are correlated only wit their corresponding factors. In this stochastic approach to estimation, the measurement residuals are necessary for the proper estimation of the composites in $\mathcal { F } _ { 2 }$ , through iterations of three key equations until successive estimates o each of the elements in the weight vectors $\widehat { \omega } _ { i }$ that make up $\widehat { \omega }$ change by less than a small fraction:

$$
\widehat {F} _ {i} = \text { Stdz } \left(\widehat {C} _ {i} \widehat {\omega} _ {i C} + \widehat {\varepsilon} _ {i} \widehat {\omega} _ {i \varepsilon}\right),   \widehat {\theta} _ {i} = x _ {i} - \widehat {F} _ {i} \widehat {\lambda} _ {i} ^ {\prime},   \widehat {\omega} _ {i} = \Sigma_ {x _ {i} x _ {i}} ^ {- 1} \left(\Sigma_ {x _ {i} x _ {i}} - \text { diag } \left(\Sigma_ {x _ {i} \widehat {\theta} _ {i}}\right)\right) \widehat {\lambda} _ {i} ^ {\prime +},
$$

where for each composite ${ \widehat { C } } _ { i } ,$ , we have ${ \widehat F } _ { \dot { I } }$ as its corresponding factor, $\widehat { \theta } _ { i }$ as the matrix of estimated indicator errors $\Sigma _ { x _ { i } x _ { j } }$ as the covariance matrix of the indicators associated with the factor, and $\Sigma _ { x _ { i } \widehat { \theta } _ { i } }$ as the matrix of estimated covari ances among indicators and their errors. The function Stdz(·) denotes the standardization function, and diag(·) returns the diagonal of a matrix, the superscript <sup>′</sup> denotes the transpose operation, the superscript −1 the classic matrix inversion, and the superscript + the Moore‐Penrose pseudoinverse transformation. See Appendix 0 for the derivation o these equations.

## 4.3 | Function $\mathcal { F } _ { 3 } \colon$ the factor estimation function

This function takes as inputs $\widehat { \rho } , \widehat { C } , \widehat { \omega } _ { C } , \widehat { \varepsilon } ,$ and $\widehat { \omega } _ { \varepsilon }$ . As indicated below, the outputs of this function are the final estimates of the matrix of factors $\widehat F$ and the matrix of measurement residuals $\widehat { \varepsilon } .$ These final estimates will contain all of the model‐implied variation that is reflected in the model's key “signature” employed by the PLSF method. This mode “signature” is $\widehat { \Sigma } _ { F F }$ , the estimated matrix of correlations among factors, calculated within $\mathcal { F } _ { 3 }$ based on the matrix of correlations among estimated composites $\Sigma _ { \widehat { c c } }$ and the vector of reliabilities ${ \widehat { \rho } } .$

$$
\left[ \widehat {F}, \widehat {\varepsilon} \right] = \mathcal {F} _ {3} \left(\widehat {\rho}, \widehat {C}, \widehat {\omega} _ {C}, \widehat {\varepsilon}, \widehat {\omega} _ {\varepsilon}\right).
$$

The final estimates of $\widehat { F }$ and $\widehat { \varepsilon }$ are generated within $\mathcal { F } _ { 3 }$ through iterations of the three main equations below, whereby the matrix of correlations among estimated factors $\Sigma _ { \widehat { F F } }$ is fitted to the estimated matrix of correlations among factors $\widehat { \Sigma } _ { F F }$ . While the former (ie, $\Sigma _ { \widehat { F F } } )$ varies across iterations, the latter $( \mathrm { i e } , \widehat { \Sigma } _ { F F } )$ is calculated early in $\mathcal { F } _ { 3 }$ and kept unchanged thereafter within $\mathcal { F } _ { 3 }$ . The iterations continue until the sum of the absolute difference $\widehat { \Sigma } _ { F _ { i } F _ { j } } - \Sigma _ { \widehat { F _ { i } F _ { j } } }$ falls below a small fraction, or until the sum of the absolute differences between successive estimates of $\widehat { \Sigma } _ { \widehat { F _ { i } F _ { j } } }$ changes by less than a small fraction.

$$
\widehat {\varepsilon} _ {i} = \operatorname{Stdz} \left(\widehat {\varepsilon} _ {i} + \left(\widehat {\Sigma} _ {F _ {i} F _ {j}} - \Sigma_ {\widehat {F _ {i}} \widehat {F _ {j}}}\right) \frac {\widehat {\Sigma} _ {F _ {i} F _ {j}}}{\widehat {\omega} _ {i \varepsilon}} \left(\widehat {C} _ {j} \widehat {\omega} _ {j C} + \widehat {\varepsilon} _ {j} \widehat {\omega} _ {j \varepsilon}\right)\right),
$$

$$
\widehat {F} _ {i} = \operatorname{Std} z \left(\widehat {F} _ {i} + \left(\widehat {\omega} _ {i C} - \Sigma_ {\widehat {F _ {i}} \widehat {C _ {i}}}\right) \widehat {C} _ {i} \widehat {\omega} _ {i C}\right),
$$

$$
\widehat {\varepsilon} _ {i} = \operatorname{Stdz} \left(\widehat {\varepsilon} _ {i} - \Sigma_ {\widehat {C _ {i}} \widehat {\varepsilon_ {i}}} \widehat {C} _ {i} \widehat {\omega} _ {i C} + \left(\widehat {\omega} _ {i \varepsilon} - \Sigma_ {\widehat {F _ {i}} \widehat {\varepsilon_ {i}}}\right) \widehat {F} _ {i} \widehat {\omega} _ {i \varepsilon}\right).
$$

The above are labelled “variation sharing” equations. Through them, successive estimates of factors $\widehat { F } _ { \mathfrak { i } }$ and measurement residuals $\widehat { \varepsilon } _ { i }$ acquire or lose variation from correlated factors, composites, and measurement residuals (denoted as $\widehat { F } _ { j } , ~ \widehat { C } _ { j } ,$ , and $\widehat { \varepsilon } _ { j } )$ , in such a way that the following constraints are enforced: $\widehat { \Sigma } _ { F _ { i } F _ { j } } = \Sigma _ { \widehat { F _ { i } } \widehat { F _ { j } } } , \Sigma _ { \widehat { F _ { i } } \widehat { C _ { i } } } = \widehat { \omega } _ { i C }$ $\Sigma _ { \widehat { F _ { i } } \widehat { \varepsilon _ { i } } } = \widehat { \omega } _ { i \varepsilon }$ , and $\Sigma _ { \widehat { C _ { i } \varepsilon _ { i } } } = 0$ . The first constraint, namely, $\widehat { \Sigma } _ { F _ { i } F _ { j } } = \Sigma _ { \widehat { F _ { i } } \widehat { F _ { j } } }$ , drives the iterative convergence process. Se Appendix 0 for the derivation of these equations.

## 4.4 | Function ${ \mathcal { F } } _ { 4 } { \mathrm { : } }$ : the full parameter estimation function

This function, expressed in equation form below, marks the final stage of the PLSF method. It ensures that all estimates produced are internally consistent, by taking as inputs $x , \widehat { F } , \widehat { \omega } _ { C } , \widehat { \varepsilon } ,$ and $\widehat { \omega } _ { \varepsilon }$ . Based on these inputs, notably $\widehat F$ and ${ \widehat { \varepsilon } } ,$ it re‐estimates ${ \widehat { C } } ,$ , ω, and $\widehat { \lambda } .$

$$
\left[ \widehat {C}, \widehat {\omega}, \widehat {\lambda}, \widehat {\beta}, \widehat {\theta}, \widehat {\zeta} \right] = \mathcal {F} _ {4} \Big (x, \widehat {F}, \widehat {\omega} _ {C}, \widehat {\varepsilon}, \widehat {\omega} _ {\varepsilon} \Big).
$$

Additionally, function ${ \mathcal { F } } _ { 4 }$ produces a matrix of estimates of the path coefficients ${ \widehat { \beta } } ,$ indicator residuals ${ \widehat { \theta } } ,$ and endogenous factor residual ${ \widehat { \zeta } } .$ These estimates are obtained by solving the equation below for each endogenous fac tor ${ \widehat F } _ { \mathrm { i } }$ , where $N _ { j }$ is the number of factors $\widehat { F } _ { j } \left( j = 1 . . . N _ { i } \right)$ pointing at ${ \widehat F } _ { i }$ in the model. The instrumental variables $\widehat { I } _ { \dot { I } }$ imple ment a two‐stage least squares estimation and exist for all endogenous factors in the model that contain variation from other factors but are not directly linked with those factors. These instrumental variables control for in-mode endogeneity and their corresponding path coefficients ${ \widehat { \beta } } _ { i }$ allow for endogeneity significance tests. The indicator resid uals in $\widehat { \theta }$ and the residuals in $\widehat { \zeta }$ are subsequently obtained directly based on these factor estimates

$$
\widehat {F} _ {i} = \sum_ {j = 1} ^ {N _ {i}} \widehat {\beta} _ {i j} \widehat {F} _ {j} + \widehat {\beta} _ {i} \widehat {I} _ {i} + \widehat {\zeta} _ {i}.
$$

At the end of the four stages that make up the PLSF method, we have estimates of various parameters stored i the following: $\widehat { F } , \widehat { C } , \widehat { \varepsilon } , \widehat { \zeta } , \widehat { \omega } , \widehat { \omega } _ { C } , \widehat { \omega } _ { \varepsilon } , \widehat { \lambda } , \widehat { \beta } ,$ and ${ \widehat { \theta } } .$ In Appendix 0, we provide all of the steps and equations that make up the PLSF method, for each of the four functions, as well as the algorithmic sequence of their execution and explan atory notes. This should facilitate the implementation of the method in any numeric computing environment, includ ing open source environments such as R and GNU Octave.

## 5 | FINITE POPULATION ILLUSTRATION

A normal finite population $( \mathsf { N } = 1 0 0 0 0 )$ was created, based on the illustrative model described earlier, to demonstrat the performance of the PLSF method vis‐à‐vis other methods. A finite population of this size incorporates only a small amount of sampling error and has the advantage of allowing us to calculate the values of various true mode parameters that can be used in a preliminary assessment of the PLSF method's ability to generate estimates of th true factors (minus uncorrelated error). Among these parameters are path coefficients, full collinearity variance infla tion factors (VIFs), loadings, and weights. The disadvantage of using a finite population is that it does not exactly replicate the properties of the infinite population from which it derives, which is why we also conducted a classic Monte Carlo experiment to assess the PLSF method

Attentive readers will notice that the true model parameters for our finite population illustration are not exactl the same as the true values shown earlier for our illustrative model. For example, the true value of the path coeffi cient for the $\mathsf { C O } > \mathsf { E U }$ link is 0.4180 in our illustrative model presented earlier and 0.4223 in our finite population illustration presented here (as will be seen shortly below). This and other related differences in true parameter values are due to sampling error, which arises from the fact that we created a population whose size is finite (not infinite based on the true illustrative model presented earlier.

Full collinearity VIFs were added to our analysis due to their importance in tests of empirical data, as they assess collinearity among all factors in a model (Kock & Lynn, 2012), and also due to the fact that their magnitude of variation and dependence on the estimates of all factor scores make them particularly sensitive to factor estimatio problems. Full collinearity VIFs allow researchers to identify both vertical and lateral collinearity in models. Vertical, or classic, collinearity reflects redundancy among predictors in a model with various factors. Lateral collinearity reflects redundancy among predictors and criteria. Full collinearity VIFs also allow researchers to check for commo method bias (Kock, 2015; Kock & Lynn, 2012)

The methods against which PLSF is compared are covariance‐based SEM through FIML; ordinary least squares (OLS) regression with summed indicators; and PLS mode A employing the path weighting scheme (PLS). The latter is the most widely used form of PLS path modelling employed in the field of IS (Goodhue et al., 2012). We used pretested MATLAB 8.4 code from a widely used commercial software, namely, WarpPLS (Kock, 2010, 2018), for the implementation of the OLS and PLS methods. We developed our own implementation of PLSF, also with

MATLAB 8.4. This implementation, not published until now, has been available in WarpPLS since version 5.0 (released in 2015). For FIML, we used R 3.2.2 and the package lavaan 0.5‐19 (Rosseel, 2012). We employed the same analysis settings as Dijkstra and Henseler (2015a), who compared a similar set of methods.

Table 1 lists the path coefficients and full collinearity VIFs for the finite population. The FIML method does not estimate factor scores, which are needed to calculate the full collinearity VIFs. Several unrefined and refined methods exist to generate correlation‐preserving approximations of factor scores based on FIML outputs (DiStefano et al., 2009), We emploved two refined methods available in lavaan, the Thurstone and Bartlett methods (Bartlett. 1937 DiStefano et al., 2009; Hershberger, 2005; Thurstone, 1935). Only the Thurstone method yielded solutions for our model. The reason for this may be that the Bartlett method requires multiple matrix inversions, including nested inversions (DiStefano et al., 2009, p. 10), which make it inherently unstable. According to a seminal discussion by Bartholomew, Deary, and Lawn (2009), both methods tend to yield very similar results, and the Thurstone method also known as Thomson's method, has a more sound mathematical basis.

Table 2 lists a summarized set of loadings and weights for the finite population. To avoid crowding, and since the patterns observed here repeat themselves across latent variables and indicators, this summarized set focuses on AC and its respective indicators AC1, AC2, …, AC5. In our model, AC has the lowest overall set of loadings and thus potentially poses the most estimation challenges for the PLSF method. The FIML method does not generate esti mates of weights, which is why they are not listed in the table. Loadings and weights for constructs other than AC are provided in Appendix 0.

Figure 3 highlights the differences (RMSEs) with respect to true values for each of the methods.

In each table, the column labelled “True” lists the true values in our finite population of various parameters. Th “Est.” columns list the corresponding estimates employing each method. The “Diff.” columns list the differences between estimates and true values for each method. The row labelled “RMSE” lists root‐mean‐square errors associated with the differences between estimates, calculated as the square roots of the averages of the squared differ ences, which provide a summarized performance measure for each of the methods.

TABLE 1 Path coefficients and full collinearity VIFs for finite population (N = 10 000)

<table><tr><td rowspan="2"></td><td rowspan="2">True</td><td colspan="2">PLSF</td><td colspan="2">FIML</td><td colspan="2">OLS</td><td colspan="2">PLS</td></tr><tr><td>Est.</td><td>Diff.</td><td>Est.</td><td>Diff.</td><td>Est.</td><td>Diff.</td><td>Est.</td><td>Diff.</td></tr><tr><td colspan="10">Path coefficients</td></tr><tr><td>CO &gt; EU</td><td>0.4223</td><td>0.4208</td><td>-0.0015</td><td>0.4188</td><td>-0.0036</td><td>0.3971</td><td>-0.0253</td><td>0.3971</td><td>-0.0252</td></tr><tr><td>CO &gt; GT</td><td>0.5074</td><td>0.5066</td><td>-0.0008</td><td>0.5085</td><td>0.0012</td><td>0.4575</td><td>-0.0499</td><td>0.4599</td><td>-0.0474</td></tr><tr><td>CO &gt; AC</td><td>0.2947</td><td>0.3021</td><td>0.0074</td><td>0.3041</td><td>0.0095</td><td>0.2661</td><td>-0.0286</td><td>0.2673</td><td>-0.0274</td></tr><tr><td>CO &gt; SU</td><td>0.0146</td><td>0.0137</td><td>-0.0009</td><td>0.0132</td><td>-0.0014</td><td>0.0917</td><td>0.0771</td><td>0.0899</td><td>0.0753</td></tr><tr><td>EU &gt; SU</td><td>0.1466</td><td>0.1479</td><td>0.0013</td><td>0.1477</td><td>0.0011</td><td>0.1206</td><td>-0.0259</td><td>0.1219</td><td>-0.0247</td></tr><tr><td>GT &gt; SU</td><td>0.5356</td><td>0.5331</td><td>-0.0025</td><td>0.5262</td><td>-0.0095</td><td>0.3983</td><td>-0.1373</td><td>0.4022</td><td>-0.1334</td></tr><tr><td>AC &gt; SU</td><td>0.2562</td><td>0.2565</td><td>0.0003</td><td>0.2664</td><td>0.0102</td><td>0.2025</td><td>-0.0537</td><td>0.2040</td><td>-0.0522</td></tr><tr><td>RMSE</td><td></td><td>0.0031</td><td></td><td>0.0066</td><td></td><td>0.0679</td><td></td><td>0.0659</td><td></td></tr><tr><td colspan="10">Full collinearity VIFs</td></tr><tr><td>CO</td><td>1.6618</td><td>1.6752</td><td>0.0135</td><td>1.8265</td><td>0.1648</td><td>1.5451</td><td>-0.1167</td><td>1.5489</td><td>-0.1128</td></tr><tr><td>EU</td><td>1.2575</td><td>1.2541</td><td>-0.0034</td><td>1.3119</td><td>0.0544</td><td>1.2084</td><td>-0.0491</td><td>1.2091</td><td>-0.0485</td></tr><tr><td>GT</td><td>1.8865</td><td>1.8921</td><td>0.0055</td><td>2.4263</td><td>0.5398</td><td>1.4966</td><td>-0.3899</td><td>1.5062</td><td>-0.3803</td></tr><tr><td>AC</td><td>1.2186</td><td>1.2181</td><td>-0.0005</td><td>1.3803</td><td>0.1616</td><td>1.1364</td><td>-0.0823</td><td>1.1384</td><td>-0.0803</td></tr><tr><td>SU</td><td>1.8813</td><td>1.8892</td><td>0.0079</td><td>2.5014</td><td>0.6201</td><td>1.4590</td><td>-0.4223</td><td>1.4687</td><td>-0.4127</td></tr><tr><td>RMSE</td><td></td><td>0.0076</td><td></td><td>0.3827</td><td></td><td>0.2658</td><td></td><td>0.2594</td><td></td></tr></table>

Abbreviations: FIML, full‐information maximum likelihood; OLS, ordinary least squares; PLS, partial least squares; VIF, vari ance inflation factor

TABLE 2 Summarized loadings and weights for finite population (N = 10 000)

<table><tr><td rowspan="2"></td><td rowspan="2">True</td><td colspan="2">PLSF</td><td colspan="2">FIML</td><td colspan="2">OLS</td><td colspan="2">PLS</td></tr><tr><td>Est.</td><td>Diff.</td><td>Est.</td><td>Diff.</td><td>Est.</td><td>Diff.</td><td>Est.</td><td>Diff.</td></tr><tr><td colspan="10">Loadings</td></tr><tr><td>AC1 &lt; AC</td><td>0.4955</td><td>0.5007</td><td>0.0052</td><td>0.5108</td><td>0.0153</td><td>0.6529</td><td>0.1574</td><td>0.6157</td><td>0.1202</td></tr><tr><td>AC2 &lt; AC</td><td>0.5959</td><td>0.6005</td><td>0.0046</td><td>0.6036</td><td>0.0077</td><td>0.7050</td><td>0.1091</td><td>0.7059</td><td>0.1100</td></tr><tr><td>AC3 &lt; AC</td><td>0.5986</td><td>0.5969</td><td>-0.0017</td><td>0.5964</td><td>-0.0022</td><td>0.7000</td><td>0.1013</td><td>0.6988</td><td>0.1001</td></tr><tr><td>AC4 &lt; AC</td><td>0.7003</td><td>0.6999</td><td>-0.0004</td><td>0.7002</td><td>-0.0001</td><td>0.7531</td><td>0.0528</td><td>0.7721</td><td>0.0718</td></tr><tr><td>AC5 &lt; AC</td><td>0.7010</td><td>0.6981</td><td>-0.0028</td><td>0.6945</td><td>-0.0064</td><td>0.7513</td><td>0.0504</td><td>0.7647</td><td>0.0638</td></tr><tr><td>RMSE</td><td></td><td>0.0034</td><td></td><td>0.0083</td><td></td><td>0.1022</td><td></td><td>0.0957</td><td></td></tr><tr><td colspan="10">Weights</td></tr><tr><td>AC1 &gt; AC</td><td>0.1385</td><td>0.1387</td><td>0.0003</td><td>...</td><td>...</td><td>0.2807</td><td>0.1423</td><td>0.2275</td><td>0.0890</td></tr><tr><td>AC2 &gt; AC</td><td>0.2077</td><td>0.2132</td><td>0.0055</td><td>...</td><td>...</td><td>0.2807</td><td>0.0730</td><td>0.2788</td><td>0.0711</td></tr><tr><td>AC3 &gt; AC</td><td>0.2174</td><td>0.2171</td><td>-0.0003</td><td>...</td><td>...</td><td>0.2807</td><td>0.0634</td><td>0.2748</td><td>0.0574</td></tr><tr><td>AC4 &gt; AC</td><td>0.3168</td><td>0.3128</td><td>-0.0040</td><td>...</td><td>...</td><td>0.2807</td><td>-0.0361</td><td>0.3123</td><td>-0.0045</td></tr><tr><td>AC5 &gt; AC</td><td>0.3197</td><td>0.3144</td><td>-0.0053</td><td>...</td><td>...</td><td>0.2807</td><td>-0.0390</td><td>0.3007</td><td>-0.0190</td></tr><tr><td>RMSE</td><td></td><td>0.0038</td><td></td><td></td><td>...</td><td>0.0805</td><td></td><td>0.0577</td><td></td></tr></table>

Abbreviations: FIML, full‐information maximum likelihood; OLS, ordinary least squares; PLS, partial least squares.

![](/api/attachments/NTW5UZWR/fulltext/images/d494989b865cf00ff1819d7d047d38eae13f21c916ac0c1165b780c5475832c0.jpg)

![](/api/attachments/NTW5UZWR/fulltext/images/17eaa3c6e5df02ce341f855f0b38fed211ae5c9437c2f56d583562dcbdfe0c94.jpg)

![](/api/attachments/NTW5UZWR/fulltext/images/98cef3ef6d92d4d76a272c4d2cde7ce510e5ce44834827d4af5aa9c21bbb7ae7.jpg)

![](/api/attachments/NTW5UZWR/fulltext/images/a5e3313e49d675b5194e47155472e9c525e030b7c5db99f1e00c05fc52cff16f.jpg)  
FIGURE 3 Differences (RMSEs) with respect to true values. FIML, full‐information maximum likelihood; OLS, ordinary least squares; PLS, partial least squares; VIF, variance inflation factor [Colour figure can be viewed a wileyonlinelibrary.com]

As we can see, the performances of PLSF and FIML were similar in terms of estimation of path coefficients. In this respect, these two methods (ie. PL SE and EIMI) performed significantly better than OLS and PL S. whose corre sponding RMSEs were multiple orders of magnitude higher. In terms of full collinearity VIFs the PLSF method per formed significantly better than the other three methods, with the performance of FIML being the poorest.

The performances of PLSF and FIML were again comparable in terms of loadings, based on their RMSEs, which also suggest that PLSF and FIML performed significantly better than OLS and PLS. Again, the RMSEs for OLS and PLS were multiple orders of magnitude higher. The same pattern is observed with respect to weights for the PLS method, when compared with the OLS and PLS methods. The FIML method does not generate weights.

## 6 | MONTE CARLO EXPERIMENT

While the analyses of the finite population provide an idea of the comparative performance of the four methods, a full Monte Carlo experiment (Paxton, Curran, Bollen, Kirby, & Chen, 2001; Robert & Casella, 2005) is needed to assess performance in terms of statistical power and percentages of false positives, as well as in terms of estimation of path coefficients with respect to an infinite population, where the distorting effect of sampling error is minimized

We generated 1000 samples of normal and nonnormal data with the following sample sizes: 100, 300, and 500 The nonnormal samples were created based on independent χ<sup>2</sup> distributions, with theoretical skewness and excess kurtosis values of <sup>fififi</sup>8<sup>p</sup> and 12, respectively, and thus severely nonnormal. Exogenous factors, endogenous factor errors, and indicator errors were created independently from one another to ensure proper nonnormality propagatio (Kock, 2016). We also conducted two tests of normality on these variables in each nonnormal sample: the classi Jarque‐Bera test (Bera & Jarque, 1981; Jarque & Bera, 1980) and Gel and Gastwirth's (2008) robust version of thi classic test. These tests confirmed the presence of significant nonnormality.

We refer to the sample sizes of 100, 300, and 500, respectively, as small, medium, and large. Our simulated data generation yielded a total of 6000 data samples, which were analysed with the PLSF, FIML, OLS, and PLS methods With normal data, the FIML method converged to solutions in all samples, and with nonnormal data, it failed to converge to solutions in 6.1% of the samples. The PLSF, OLS, and PLS methods converged to solutions in all samples both normal and nonnormal

Tables 3 and 4 show, for each of the path coefficients in our illustrative population model described earlier, the following estimates: the average difference between the path coefficient estimated by each method and the true values (rows labelled “Avg. diff.”); the statistical power of each method (rows labelled “Power”); the standard deviation of the estimate (rows labelled “Std. dev.”); the percentage of false positives yielded by each method for the path whose true value is zero (rows labelled “False pos.”); and, in the final rows at the bottom, the RMSE for each method, calculated based on the average differences. Results for normal and nonnormal data are shown.

In terms of path coefficient estimation accuracy, assessed through average differences between estimated and true values, the performances of the PLSF and FIML methods were similar with both normal and nonnormal data across the three sample sizes. Both methods converged to the true values as sample sizes increased, with PLSF con verging significantly faster. In this respect, the performances of PLSF and FIML were significantly better than OLS and PLS, mimicking the results with respect to the finite population.

Figure 4 highlights the performance in terms of statistical power for each of the methods. This figure reflects the fact that PLSF has greater power than FIML for all paths in all of the sample sizes considered. The focus here is on normal data; the results for the nonnormal data show similar patterns. Six bar charts are shown. At the top of eac chart, the respective path is listed. Next to the vertical axes, we show the power values achieved for each sample size. The sample sizes are shown underneath the horizontal axes.

In summary, in terms of statistical power, assessed through confidence intervals (Dijkstra & Henseler, 2015a; Goodhue et al., 2012), PLSF and PLS presented similar performance, and generally better performance than FIML and OLS. In terms of avoidance of false positives, PLSF and FIML presented similar performance, and much better performance overall than OLS and PLS. With large samples (N = 500), OLS and PLS performed particularly poorl with respect to avoidance of false positives.

## 7 | DISCUSSION

There has been a continuing and often antagonistic debate among proponents and detractors of classic PLS methods (Goodhue et al., 2012; Kock & Hadaya, 2018; McIntosh et al., 2014; Rönkkö et al., 2015). This debate has frequentl centred around one main problem with PLS methods, which is that they do not deal with factors, which we treat as aggregations of indicators and measurement residuals, but with composites. We made here what is arguably an important contribution to this debate by discussing the PLSF method, which is anchored on a new conceptual foundation, Our method combines elements of classic PL S methods and covariance-based SEM and provides estimates of the composites and factors in a path model.

TABLE 3 Monte Carlo experiment results for path coefficients (normal data)

<table><tr><td rowspan="2">Sample Size Method</td><td colspan="4">100</td><td colspan="4">300</td><td colspan="4">500</td></tr><tr><td>PLSF</td><td>FIML</td><td>OLS</td><td>PLS</td><td>PLSF</td><td>FIML</td><td>OLS</td><td>PLS</td><td>PLSF</td><td>FIML</td><td>OLS</td><td>PLS</td></tr><tr><td colspan="13">CO &gt; EU (0.418)</td></tr><tr><td>Avg. diff.</td><td>0.0107</td><td>-0.0047</td><td>-0.0214</td><td>-0.0145</td><td>0.0035</td><td>-0.0017</td><td>-0.0221</td><td>-0.0198</td><td>0.0015</td><td>-0.0022</td><td>-0.0225</td><td>-0.0210</td></tr><tr><td>Power</td><td>100.0%</td><td>98.3%</td><td>99.9%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td></tr><tr><td>Std. dev.</td><td>0.0782</td><td>0.0888</td><td>0.0764</td><td>0.0749</td><td>0.0474</td><td>0.0501</td><td>0.0454</td><td>0.0452</td><td>0.0372</td><td>0.0379</td><td>0.0354</td><td>0.0353</td></tr><tr><td colspan="13">CO &gt; GT (0.515)</td></tr><tr><td>Avg. diff.</td><td>0.0017</td><td>-0.0005</td><td>-0.0554</td><td>-0.0462</td><td>0.0044</td><td>0.0007</td><td>-0.0505</td><td>-0.0459</td><td>0.0040</td><td>0.0012</td><td>-0.0499</td><td>-0.0462</td></tr><tr><td>Power</td><td>100.0%</td><td>99.8%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td></tr><tr><td>Std. dev.</td><td>0.0765</td><td>0.0810</td><td>0.0699</td><td>0.0695</td><td>0.0423</td><td>0.0482</td><td>0.0389</td><td>0.0384</td><td>0.0328</td><td>0.0353</td><td>0.0299</td><td>0.0297</td></tr><tr><td colspan="13">CO &gt; AC (0.288)</td></tr><tr><td>Avg. diff.</td><td>0.0028</td><td>0.0049</td><td>-0.0402</td><td>-0.0174</td><td>0.0026</td><td>0.0084</td><td>-0.0402</td><td>-0.0320</td><td>0.0038</td><td>0.0080</td><td>-0.0368</td><td>-0.0316</td></tr><tr><td>Power</td><td>85.9%</td><td>72.4%</td><td>76.8%</td><td>86.3%</td><td>100.0%</td><td>99.4%</td><td>99.8%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td></tr><tr><td>Std. dev.</td><td>0.1004</td><td>0.1057</td><td>0.0912</td><td>0.0879</td><td>0.0586</td><td>0.0610</td><td>0.0520</td><td>0.0516</td><td>0.0443</td><td>0.0465</td><td>0.0393</td><td>0.0389</td></tr><tr><td colspan="13">CO &gt; SU (0.000)</td></tr><tr><td>Avg. diff.</td><td>-0.0034</td><td>-0.0043</td><td>0.0848</td><td>0.0688</td><td>-0.0100</td><td>0.0010</td><td>0.0814</td><td>0.0742</td><td>-0.0052</td><td>-0.0040</td><td>0.0836</td><td>0.0784</td></tr><tr><td>False pos.</td><td>5.2%</td><td>5.5%</td><td>11.6%</td><td>8.9%</td><td>3.7%</td><td>1.9%</td><td>27.2%</td><td>23.6%</td><td>4.1%</td><td>2.5%</td><td>50.0%</td><td>44.5%</td></tr><tr><td>Std. dev.</td><td>0.1398</td><td>0.1337</td><td>0.1089</td><td>0.1103</td><td>0.0764</td><td>0.0700</td><td>0.0606</td><td>0.0608</td><td>0.0553</td><td>0.0531</td><td>0.0441</td><td>0.0441</td></tr><tr><td colspan="13">EU &gt; SU (0.157)</td></tr><tr><td>Avg. diff.</td><td>0.0092</td><td>0.0009</td><td>-0.0295</td><td>-0.0238</td><td>0.0064</td><td>0.0016</td><td>-0.0263</td><td>-0.0241</td><td>0.0014</td><td>0.0025</td><td>-0.0290</td><td>-0.0273</td></tr><tr><td>Power</td><td>33.7%</td><td>22.7%</td><td>30.5%</td><td>33.2%</td><td>73.8%</td><td>57.8%</td><td>71.5%</td><td>72.0%</td><td>88.1%</td><td>81.2%</td><td>86.3%</td><td>87.7%</td></tr><tr><td>Std. dev.</td><td>0.1092</td><td>0.1112</td><td>0.0888</td><td>0.0898</td><td>0.0629</td><td>0.0610</td><td>0.0520</td><td>0.0522</td><td>0.0502</td><td>0.0467</td><td>0.0421</td><td>0.0419</td></tr><tr><td colspan="13">GT &gt; SU (0.542)</td></tr><tr><td>Avg. diff.</td><td>-0.0029</td><td>-0.0078</td><td>-0.1427</td><td>-0.1258</td><td>0.0053</td><td>-0.0130</td><td>-0.1372</td><td>-0.1279</td><td>0.0065</td><td>-0.0084</td><td>-0.1367</td><td>-0.1287</td></tr><tr><td>Power</td><td>99.6%</td><td>98.3%</td><td>99.6%</td><td>99.8%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td></tr><tr><td>Std. dev.</td><td>0.1120</td><td>0.1152</td><td>0.0836</td><td>0.0844</td><td>0.0663</td><td>0.0604</td><td>0.0498</td><td>0.0497</td><td>0.0496</td><td>0.0492</td><td>0.0379</td><td>0.0375</td></tr><tr><td colspan="13">AC &gt; SU (0.254)</td></tr><tr><td>Avg. diff.</td><td>0.0049</td><td>0.0103</td><td>-0.0619</td><td>-0.0434</td><td>0.0052</td><td>0.0126</td><td>-0.0612</td><td>-0.0537</td><td>0.0033</td><td>0.0093</td><td>-0.0620</td><td>-0.0568</td></tr><tr><td>Power</td><td>61.4%</td><td>58.8%</td><td>60.6%</td><td>67.7%</td><td>98.5%</td><td>97.5%</td><td>98.5%</td><td>98.6%</td><td>100.0%</td><td>99.8%</td><td>99.9%</td><td>100.0%</td></tr><tr><td>Std. dev.</td><td>0.1146</td><td>0.1086</td><td>0.0859</td><td>0.0881</td><td>0.0601</td><td>0.0610</td><td>0.0460</td><td>0.0461</td><td>0.0470</td><td>0.0495</td><td>0.0360</td><td>0.0359</td></tr><tr><td>RMSE</td><td>0.0060</td><td>0.0058</td><td>0.0731</td><td>0.0605</td><td>0.0058</td><td>0.0076</td><td>0.0702</td><td>0.0642</td><td>0.0041</td><td>0.0060</td><td>0.0704</td><td>0.0657</td></tr></table>

Abbreviations: FIML, full‐information maximum likelihood; OLS, ordinary least squares; PLS, partial least squares.

TABLE 4 Monte Carlo experiment results for path coefficients (nonnormal data)

<table><tr><td rowspan="2">Sample Size Method</td><td colspan="4">100</td><td colspan="4">300</td><td colspan="4">500</td></tr><tr><td>PLSF</td><td>FIML</td><td>OLS</td><td>PLS</td><td>PLSF</td><td>FIML</td><td>OLS</td><td>PLS</td><td>PLSF</td><td>FIML</td><td>OLS</td><td>PLS</td></tr><tr><td colspan="13">CO &gt; EU (0.418)</td></tr><tr><td>Avg. diff.</td><td>0.0096</td><td>-0.0036</td><td>-0.0237</td><td>-0.0168</td><td>0.0042</td><td>-0.0011</td><td>-0.0215</td><td>-0.0191</td><td>0.0016</td><td>-0.0035</td><td>-0.0223</td><td>-0.0210</td></tr><tr><td>Power</td><td>100.0%</td><td>93.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td></tr><tr><td>Std. dev.</td><td>0.0810</td><td>0.1218</td><td>0.0780</td><td>0.0771</td><td>0.0459</td><td>0.0710</td><td>0.0435</td><td>0.0435</td><td>0.0348</td><td>0.0569</td><td>0.0330</td><td>0.0330</td></tr><tr><td colspan="13">CO &gt; GT (0.515)</td></tr><tr><td>Avg. diff.</td><td>0.0016</td><td>-0.0042</td><td>-0.0572</td><td>-0.0488</td><td>0.0051</td><td>-0.0065</td><td>-0.0498</td><td>-0.0452</td><td>0.0031</td><td>-0.0042</td><td>-0.0509</td><td>-0.0472</td></tr><tr><td>Power</td><td>100.0%</td><td>98.4%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td></tr><tr><td>Std. dev.</td><td>0.0742</td><td>0.1223</td><td>0.0674</td><td>0.0671</td><td>0.0439</td><td>0.0696</td><td>0.0402</td><td>0.0400</td><td>0.0341</td><td>0.0549</td><td>0.0312</td><td>0.0310</td></tr><tr><td colspan="13">CO &gt; AC (0.288)</td></tr><tr><td>Avg. diff.</td><td>0.0099</td><td>-0.0094</td><td>-0.0438</td><td>-0.0221</td><td>0.0073</td><td>-0.0137</td><td>-0.0359</td><td>-0.0280</td><td>0.0014</td><td>-0.0112</td><td>-0.0391</td><td>-0.0338</td></tr><tr><td>Power</td><td>83.0%</td><td>68.2%</td><td>77.0%</td><td>84.2%</td><td>100.0%</td><td>99.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td></tr><tr><td>Std. dev.</td><td>0.1017</td><td>0.1224</td><td>0.0891</td><td>0.0896</td><td>0.0577</td><td>0.0686</td><td>0.0510</td><td>0.0509</td><td>0.0436</td><td>0.0538</td><td>0.0384</td><td>0.0384</td></tr><tr><td colspan="13">CO &gt; SU (0.000)</td></tr><tr><td>Avg. diff.</td><td>-0.0034</td><td>-0.0015</td><td>0.0811</td><td>0.0648</td><td>-0.0104</td><td>0.0027</td><td>0.0820</td><td>0.0750</td><td>-0.0079</td><td>0.0024</td><td>0.0818</td><td>0.0764</td></tr><tr><td>False pos.</td><td>4.9%</td><td>4.8%</td><td>12.7%</td><td>9.3%</td><td>4.7%</td><td>4.9%</td><td>26.2%</td><td>23.0%</td><td>5.0%</td><td>5.1%</td><td>41.4%</td><td>36.3%</td></tr><tr><td>Std. dev.</td><td>0.1338</td><td>0.1365</td><td>0.1006</td><td>0.1037</td><td>0.0772</td><td>0.0734</td><td>0.0606</td><td>0.0609</td><td>0.0606</td><td>0.0580</td><td>0.0474</td><td>0.0476</td></tr><tr><td colspan="13">EU &gt; SU (0.157)</td></tr><tr><td>Avg. diff.</td><td>0.0081</td><td>-0.0074</td><td>-0.0243</td><td>-0.0178</td><td>0.0050</td><td>-0.0066</td><td>-0.0279</td><td>-0.0257</td><td>0.0048</td><td>-0.0022</td><td>-0.0262</td><td>-0.0246</td></tr><tr><td>Power</td><td>30.8%</td><td>26.3%</td><td>27.3%</td><td>29.2%</td><td>75.2%</td><td>67.4%</td><td>70.3%</td><td>71.8%</td><td>93.4%</td><td>91.2%</td><td>91.9%</td><td>92.5%</td></tr><tr><td>Std. dev.</td><td>0.1164</td><td>0.1122</td><td>0.0935</td><td>0.0955</td><td>0.0617</td><td>0.0627</td><td>0.0513</td><td>0.0513</td><td>0.0476</td><td>0.0479</td><td>0.0394</td><td>0.0394</td></tr><tr><td colspan="13">GT &gt; SU (0.542)</td></tr><tr><td>Avg. diff.</td><td>0.0042</td><td>0.0079</td><td>-0.1375</td><td>-0.1210</td><td>0.0071</td><td>0.0033</td><td>-0.1369</td><td>-0.1275</td><td>0.0070</td><td>0.0036</td><td>-0.1359</td><td>-0.1280</td></tr><tr><td>Power</td><td>100.0%</td><td>96.6%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td></tr><tr><td>Std. dev.</td><td>0.1110</td><td>0.1400</td><td>0.0801</td><td>0.0812</td><td>0.0644</td><td>0.0753</td><td>0.0481</td><td>0.0480</td><td>0.0502</td><td>0.0571</td><td>0.0372</td><td>0.0371</td></tr><tr><td colspan="13">AC &gt; SU (0.254)</td></tr><tr><td>Avg. diff.</td><td>0.0102</td><td>-0.0105</td><td>-0.0620</td><td>-0.0433</td><td>0.0047</td><td>-0.0103</td><td>-0.0617</td><td>-0.0546</td><td>0.0030</td><td>-0.0113</td><td>-0.0623</td><td>-0.0571</td></tr><tr><td>Power</td><td>61.5%</td><td>53.0%</td><td>61.1%</td><td>67.9%</td><td>97.6%</td><td>96.4%</td><td>97.7%</td><td>98.4%</td><td>99.9%</td><td>99.9%</td><td>99.9%</td><td>99.9%</td></tr><tr><td>Std. dev.</td><td>0.1102</td><td>0.1231</td><td>0.0833</td><td>0.0853</td><td>0.0655</td><td>0.0675</td><td>0.0491</td><td>0.0496</td><td>0.0499</td><td>0.0520</td><td>0.0370</td><td>0.0374</td></tr><tr><td>RMSE</td><td>0.0075</td><td>0.0071</td><td>0.0714</td><td>0.0588</td><td>0.0066</td><td>0.0075</td><td>0.0700</td><td>0.0640</td><td>0.0047</td><td>0.0066</td><td>0.0700</td><td>0.0654</td></tr></table>

![](/api/attachments/NTW5UZWR/fulltext/images/e7d63dc096f5c6afdc9582e684b473e25b2104c982b670f0afcba5a839a1b606.jpg)

![](/api/attachments/NTW5UZWR/fulltext/images/f5849e091e159898af1eb6901e46b2a3defa039516fc356579bec872fb670465.jpg)

![](/api/attachments/NTW5UZWR/fulltext/images/cc129dd0df0a49c95df389d29aa9e97be47820ed53b46263dd1e46d686efdc36.jpg)

![](/api/attachments/NTW5UZWR/fulltext/images/7080244227eeae30fe559ab1238dd0fb40044354364669ed489bf5c484a8caf2.jpg)

![](/api/attachments/NTW5UZWR/fulltext/images/f2082bb9ddc4cd407038f40573a37320634de8cc9fb4b533b8f92d0de92b1ba3.jpg)

![](/api/attachments/NTW5UZWR/fulltext/images/a8f05f77054e76cd9b491cae23a95bdfe309a3f3310b09205a9cf8138843aa95.jpg)  
FIGURE 4 Performance in terms of statistical power. FIML, full‐information maximum likelihood; OLS, ordinary least squares; PLS, partial least squares [Colour figure can be viewed at wileyonlinelibrary.com]

## 7.1 | Should we really care about factors?

The methods we compared attempt to recover population parameters, such as path coefficients, based on empirical datasets. In the context of hypothesis‐testing via SEM, biased parameters are problematic in that they may lead to types I and II errors. A type I error occurs when an effect that does not exist in the population is mistaken as a “real” effect based on the analysis of an empirical dataset, which would be a false positive. A type II error occurs when an effect that exists in the population is mistaken as “no effect,” a false negative. Because SEM investigations are typically used for hypothesis testing, it is critical that parameter estimates be as accurate as possible, so that types I and II errors can be avoided. And composite‐based methods, of which the most widely used are classic PLS methods demonstrably generate biased parameters.

Recognition of this problem has led to a new line of prediction‐oriented research employing classic PLS methods particularly PLS mode A, based on a key argument. The argument is that composite‐based methods like classic PLS are as good for prediction as factor‐based methods, if not better, while at the same time being simpler to use and fairly effective at converging to solutions (Shmueli, Ray, Estrada, & Chatla, 2016). For example, let us assume that one wants to build a model of customer purchases at a supermarket, where purchases of a class of products (eg, beer) are modelled as influencing purchases of another class of products (eg, corn chips). According to this prediction argument (ie, PLS is very good for prediction), a model built based on parameters obtained via classic PLS methods would be quite successful at predicting purchases in the future (eg, next month) based on past purchases (eg, last month). Following the prediction argument, such a model would do as good a job as a factor‐based model, if not better. Moreover, the simplicity and computational speed of classic PLS algorithms such as PLS mode A would further tip the balance in their favour in analyses of very large datasets and highly complex prediction‐oriented models. Note that this prediction-oriented type of application is significantly different from hypothesis testing in the context of SEM

While a discussion of the merits of the prediction argument is outside the scope of this paper, its basic premise has been finding increasing support (Carrión, Henseler, Ringle, & Roldán, 2016; Shmueli et al., 2016). The argument has also provided the impetus for related methodological perspectives, such as that the simplicity of classic PLS methods is in fact a virtue in prediction‐oriented applications (Rigdon, 2012) and that classic PLS methods used in prediction‐oriented scenarios should not be compared with factor‐based methods aimed at testing hypotheses i the context of SEM (Rigdon, Sarstedt, & Ringle, 2017). We find these ideas worth pursuing and believe that there may be a bright future for prediction‐oriented research building on classic PLS methods, particularly PLS mode A, if these ideas are found to have merit. We also believe that hypothesis testing in the context of SEM can greatly benefit from factor‐based methods, because it relies heavily on parameter estimation accuracy, hence our proposal of the PLSF method. Should we care about factors? Yes, if we are testing hypotheses in the context of SEM, but perhaps not so much in prediction‐oriented scenarios.

## 7.2 | Statistical efficiency

We showed evidence that PLSF is statistically consistent, like covariance‐based SEM, but has greater statistica power, more in line with PLS. For example, for the path CO > AC (0.288), only PLSF and PLS displayed power greate than 80% for a small sample size (N = 100), respectively, 85.9% and 86.3% with normal data and 83.0% and 84.2% with nonnormal data. For this same path and sample size, covariance‐based SEM had a power of 72.4% with norma data, and 68.2% with nonnormal data

Since between PLSF and PLS, the only statistically consistent method is PLSF, as PLSF asymptotically converges to the true values and PLS does not, this suggests that PLSF is a good candidate in the context of SEM for the sta tistical property of asymptotic “efficiency” (Nikitin & Nikitin, 1995). A method is statistically efficient in an asymptotic sense if it is statistically consistent and also achieves a given level of power with the smallest sample size

## 7.3 | PLSF versus other similar factor‐based variations

Our choice of comparison methods—PLS, FIML, and OLS—mirrors the choices made in two related seminal methodological studies in the field of IS, conducted by Goodhue et al. (2012) and Dijkstra and Henseler (2015a). Both studies provided evidence that parameters can be corrected for attenuation. Goodhue et al. (2012) proposed the use of OLS regression with summed indicators and attenuation correction based on the Cronbach alpha coefficient, whereas Dijkstra and Henseler (2015a) the use of consistent PLS with attenuation correction based on its own true reliabilit estimate.

While our PLSF method is not a parameter correction method, one could argue that the methods proposed by Goodhue et al. (2012) and Dijkstra and Henseler (2015a) could be used with the technique of variation sharing employed in stage 3 of PLSF to provide the basis for two additional methods against which PLSF could be compared. This would allow for the calculation of a wide range of parameters, well beyond the ones originally targeted for correction for attenuation by the two methods. It could be interesting to see how these parameters differ from the tru values in our finite population. We conducted such a comparison and reported the results in Appendix 0, where the two new methods are referred to as OLSa and PLSc. We found that PLSF outperformed OLSa and PLSc in terms o estimation of path coefficients, full collinearity VIFs, loadings, and weights

The main reason why PLSF outperformed these methods is that it estimates composites, in its stage 2, in a way that is arguably more mathematically sound than OLSa and PLSc do. OLSa noniteratively estimates composites as standardized sums of indicators, whereas PLSc employs the iterative PLS mode A algorithm with the centroid scheme (Lohmöller, 1989, p. 29). These lead to biased weights for both OLSa and PLSc, weights that are necessary for producing composites. The final outcomes are composite approximations that are not the ideal starting point for the cal culation of composite correlations to be corrected for attenuation

It is important to note that the approximations of weights produced by consistent PLS in stage 1 of the PLSF method are useful in that they contribute to increasing the computational efficiency of the composite estimation stage of PLSF (stage 2). Without those weights, the PLSF method would have to depart from unit weights, whic are not as good as starting points as are the consistent PLS weights obtained via the PLS mode A algorithm with the centroid scheme (Lohmöller, 1989).

## 7.4 | What if CO had been measured via multiple indicators?

As noted earlier, our decision to include a single‐item construct (CO) allowed us to pose an important challenge to our PLSE method. This prevented this construct from receiving variation when we went from composites to factors because, being a single‐item construct, CO was essentially measured without error. That is, the single indicator used to measure CO was assumed in our data creation and subsequent analysis to be a perfect measure of the construct This is of course different from using a single indicator to measure a construct with error (Bergkvist & Rossiter, 2007; Sarstedt, Diamantopoulos, & Salzberger, 2016; Wanous & Reichers, 1996; Wanous, Reichers, & Hudy, 1997), which would in fact reduce the reliability associated with the construct, and is a practice that is generally not advisable.

One could argue that different results would have been obtained in our analysis had CO been measured via multiple indicators. We addressed this in Appendix 0, where we present the results of an analysis with CO measured through a set of five indicators with heterogeneous loadings. As we expected, neither the performance of PLSF nor that of FIML was noticeably affected. We did notice a further deterioration in the performances of OLS and PLS with respect to path coefficients and full collinearity VIFs. This further deterioration is not particularly surprising since neither OLS nor PLS explicitly accounts for measurement error.

## 7.5 | Advantages and disadvantages of PLSF

The PLSF method presents a few notable advantages when compared with existing SEM methods. It shares the property of consistency with covariance-based SEM. vielding asymptotically unbiased estimates of various parameters but like classic PLS has, greater statistical power, Computationally, the, PLSE method is much simpler than covariance-based SEM. Unlike the PLSE method, covariance-based SEM reguires the calculation of matrices of second order partial derivatives (Hessian matrices) and their inversion, which is often impossible or leads to unacceptable results (Kline. 2010: Mueller. 1996). Finally, the PL SE method provides estimates of factor scores, which can subse: quently be used in a variety of other tests. Among such tests are two that have been developed in the field of IS and have been widely used in a variety of fields since their publication: full collinearity tests, which concurrently assess both lateral and vertical collinearities among factors (Kock & Lynn, 2012) and can be used in common method bias assessments (Kock, 2015; Kock & Lynn, 2012), and factor‐factor nonlinearity tests, where best‐fitting nonlinear func tions are estimated for each pair of causally linked factors and then used in the estimation of modified path coeffi cients that take nonlinearity into consideration (Guo et al., 2011; Kock, 2010; Moqbel et al., 2013).

The PLSF method presents a notable theoretical disadvantage when compared with covariance‐based SEM. The PLSF method does not allow for the estimation of correlations among indicator error terms, which are correlations that can lead to common method bias (Kock, 2015). In covariance‐based SEM, the estimation of correlations among indicator error terms is theoretically possible, as is controlling for those correlations in the estimation of other parameters. In practice, this estimation often leads to identification problems. These identification problems arise from the increase in the number of parameters to be estimated, now including various correlations among indicator error terms, and the consequent need for the problematic calculation and inversion of matrices of second‐order partia derivatives. As noted above, the PLSF method allows for common method bias assessment but not for removal of pathological common method variation. A promising new line of research, which we recommend, is the use of the technique of variation sharing employed in stage 3 of the PLSF method to remove pathological common method var iation from empirical datasets.

With respect to the disadvantage of PLSF discussed above, it is important to note that it is a disadvantage primarily when we compare the use of the PLSF method against covariance‐based SEM, assuming that the model we are analysing is correct. In covariance‐based SEM, the model‐implied network of links among factors and indicators strongly influences the estimation of parameters (Kline, 2010). In other words, in covariance‐based SEM, it is critica that we get the model right prior to estimating parameters based on empirical data. This is much less so in the PLS method, similarly to PLS in general (Lohmöller, 1989), because the factors estimated by PLSF are based on composites. In PLSF, we go from composites to factors, based on correlations among composites. Those correlations are present due to an underlying model structure but are not as influenced as in covariance‐based SEM by a hypothe sized model structure.

## 8 | CONCLUSION

The new PLSF method discussed here combines elements of classic PLS and covariance‐based SEM methods Like classic PLS, it generates parameter estimates after it creates factor scores, with the key difference that PLSF yields estimates of the factors while classic PLS produces approximations. Also, like classic PLS, it makes no data distribution assumptions, which is a characteristic of robust nonparametric methods (Siegel & Castellan. 1998). Like covariance-based SEM. the PLSF method fits covariance matrices. with the key difference that PLSF fits factor covariance matrices while in covariance‐based SEM, the fitting involves indicato covariance matrices.

Since the PLSF method builds on the consistent PLS technique, it can be seen as an endorsement of the use of that technique as a basis for the development of factor‐based path analysis methods. In this respect, it arguably constitutes an important methodological contribution. The reason for this is that in parameter correction techniques such as consistent PLS, typically a different equation has to be developed to correct each parameter class, eg, one equation to correct path coefficients and one equation to correct loadings. The PLSF method, on the other hand, esti mates prototypical elements from which parameters are directly derived without any need for corrections. This places a large number of parameters in the hands of researchers (eg, indicator weights and model‐wide full collinearity VIFs), which can then be used in a variety of tests, including tests that currently do not exist because of limited access to parameter estimates

While flexibility has not been directly addressed in our discussion, it is worth noting that the PLSF method is very flexible, arguably more so than classic PLS and related methods, allowing for many constraints to be imposed or relaxed. In this aspect, it is similar to covariance‐based SEM. For example, while in our analyses, we assumed the common factor model property that indicator errors are uncorrelated, this assumption can be relaxed. To do this we would use an appropriately modified version of the equation relating weights and loadings employed in the com posite estimation stage of PLSF. On the other hand. we could impose constraints by fixing parameters instead of relaxing assumptions. This could be done in any of the four stages

Covariance‐based SEM is often presented as a step beyond Wright's (1934, 1960) path analysis method, because covariance‐based SEM, unlike path analysis, deals with factors. However, while covariance‐based SEM is a factor‐based technique in a mathematical sense, since its underlying mathematics assumes the existence of factors, it does not directly estimate factors as part of its parameter estimation process. In covariance‐based SEM, factors are akin to “black holes” in that they indirectly and greatly influence the estimation of parameters but are never directly “seen.” Arguably, the PLSF method contributes to filling this gap; in it, SEM is truly an extension of Wright's path analysis, with factors estimated directly and subsequently used to estimate mode parameters.

## ORCID

Ned Kock http://orcid.org/0000-0002-5791-5434

## REFERENCES

Adelman, I., & Lohmoller, J.‐B. (1994). Institutions and development in the nineteenth century: A latent variable regression model. Structural Change and Economic Dynamics, 5(2), 329–359. https://doi.org/10.1016/0954‐349X(94)90008‐6

Bartholomew, D. J., Deary, I. J., & Lawn, M. (2009). The origin of factor scores: Spearman, Thomson and Bartlett. British Jour nal of Mathematical and Statistical Psychology, 62(3), 569–582. https://doi.org/10.1348/000711008X365676

Bartlett, M. S. (1937). The statistical conception of mental factors. British Journal of Psychology, 28(1), 97–104.

Bentler, P. M., & Huang, W. (2014). On components, latent variables, PLS and simple methods: Reactions to Rigdon's rethink ing of PLS. Long Range Planning, 47(3), 138–145. https://doi.org/10.1016/j.lrp.2014.02.005

Bera, A. K., & Jarque, C. M. (1981). Efficient tests for normality, homoscedasticity and serial independence of regression residuals: Monte Carlo evidence. Economics Letters, 7(4), 313–318. https://doi.org/10.1016/0165‐1765(81)90035‐5

Bergkvist, L., & Rossiter, J. R. (2007). The predictive validity of multiple‐item versus single‐item measures of the same con structs. Journal of Marketing Research, 44(2), 175–184. https://doi.org/10.1509/jmkr.44.2.175

Carrión, G. C., Henseler, J., Ringle, C. M., & Roldán, J. L. (2016). Prediction‐oriented modeling in business research by means of PLS path modeling. Journal of Business Research, 69(10), 4545–4551. https://doi.org/10.1016/j.jbusres.2016.03.048

Chin, W. W. (1998). Issues and opinion on structural equation modeling. MIS Quarterly, 22(1), vii–xvi

Chin, W. W., Marcolin, B. L., & Newsted, P. R. (2003). A partial least squares latent variable modeling approach for measuring interaction effects: Results from a Monte Carlo simulation study and an electronic‐mail emotion/adoption study. Informa tion Systems Research, 14(2), 189–218. https://doi.org/10.1287/isre.14.2.189.16018

Dijkstra, T. K., & Henseler, J. (2015a). Consistent partial least squares path modeling. MIS Quarterly, 39(2), 297–316. https:// doi.org/10.25300/MISQ/2015/39.2.02

Dijkstra, T. K., & Henseler, J. (2015b). Consistent and asymptotically normal PLS estimators for linear structural equations Computational Statistics & Data Analysis, 81(1), 10–23. https://doi.org/10.1016/j.csda.2014.07.008

Dijkstra, T. K., & Schermelleh‐Engel, K. (2014). Consistent partial least squares for nonlinear structural equation models Psychometrika, 79(4), 585–604. https://doi.org/10.1007/s11336‐013‐9370‐0

Dillon, W. R., & Goldstein, M. (1984). Multivariate analysis: Methods and applications. New York, NY: Wiley.

DiStefano, C., Zhu, M., & Mindrila, D. (2009). Understanding and using factor scores: Considerations for the applied researcher. Practical Assessment, Research & Evaluation, 14(20), 1–11.

Gel, Y. R., & Gastwirth, J. L. (2008). A robust modification of the Jarque‐Bera test of normality. Economics Letters, 99(1) 30–32. https://doi.org/10.1016/j.econlet.2007.05.022

Goodhue, D., Lewis, W., & Thompson, R. (2007). Statistical power in analyzing interaction effects: Questioning the advantage of PLS with product indicators, Information Systems Research. 18(2), 211–227. https://doi,org/10.1287/isre,1070.0123

Goodhue, D. L., Lewis, W., & Thompson, R. (2012). Does PLS have advantages for small sample size or non‐normal data? MI Quarterly, 36(3), 981–1001.

Guo, K. H., Yuan, Y., Archer, N. P., & Connelly, C. E. (2011). Understanding nonmalicious security violations in the workplace: A composite behavior model. Journal of Management Information Systems, 28(2), 203–236. https://doi.org/10.2753 MIS0742‐1222280208

Hakstian, A. R., Schroeder, M. L., & Rogers, W. T. (1988). Inferential procedures for correlation coefficients corrected fo attenuation. Psychometrika, 53(1), 27–43. https://doi.org/10.1007/BF02294192

Henseler, J., Dijkstra, T. K., Sarstedt, M., Ringle, C. M., Diamantopoulos, A., Straub, D. W., … Calantone, R. J. (2014). Common beliefs and reality about PLS—Comments on Rönkkö and Evermann (2013). Organizational Research Methods, 17(2), 182-209. bttps://doi.org/10.1177/1094428114526928

Hershberger, S. L. (2005). Factor scores. In B. S. Everitt, & D. C. Howell (Eds.), Encyclopedia of statistics in behavioral science (pp. 636–644). New York, NY: John Wiley. https://doi.org/10.1002/0470013192.bsa726

Jarque, C. M., & Bera, A. K. (1980). Efficient tests for normality, homoscedasticity and serial independence of regression residuals. Economics Letters, 6(3), 255–259. https://doi.org/10.1016/0165‐1765(80)90024‐5

Johnson, H. G. (1950). Test reliability and correction for attenuation. Psychometrika, 15(2), 115–119. https://doi.org 10.1007/BF02289196

Kline, R. B. (2010). Principles and practice of structural equation modeling. New York, NY: The Guilford Press.

Kock, N. (2003). Communication‐focused business process redesign: Assessing a communication flow optimization mode through an action research study at a defense contractor. IEEE Transactions on Professional Communication, 46(1). 35–54

Kock, N. (2007). Systems analysis and design fundamentals: A business process redesign approach. Thousand Oaks, CA: Sage Publications.

Kock, N. (2010). Using WarpPLS in e‐collaboration studies: An overview of five main analysis steps. International Journal of e Collaboration, 6(4), 1–11. https://doi.org/10.4018/jec.2010100101

Kock, N. (2015). Common method bias in PLS‐SEM: A full collinearity assessment approach. International Journal of e‐Collab oration, 11(4), 1–10.

Kock, N. (2016). Non‐normality propagation among latent variables and indicators in PLS‐SEM simulations. Journal of Modern Applied Statistical Methods, 15(1), 299–315. https://doi.org/10.22237/jmasm/1462076100

Kock, N. (2018). WarpPLS user manual: Version 6.0. Laredo, TX: ScriptWarp Systems.

Kock, N., Danesh, A., & Komiak, P. (2008). A discussion and test of a communication flow optimization approach for business process redesign. Knowledge and Process Management, 15(1), 72–85. https://doi.org/10.1002/kpm.301

Kock, N., & Hadaya, P. (2018). Minimum sample size estimation in PLS‐SEM: The inverse square root and gamma‐exponentia methods. Information Systems Journal, 28(1), 227–261. https://doi.org/10.1111/isj.12131

Kock, N., & Lynn, G. S. (2012). Lateral collinearity and misleading results in variance‐based SEM: An illustration and recom mendations. Journal of the Association for Information Systems, 13(7), 546–580. https://doi.org/10.17705/1jais.00302

Kock, N., & Murphy, F. (2001). Redesigning acquisition processes: A new methodology based on the flow of knowledge and infor mation. Fort Belvoir, VA: Defense Acquisition University Press

Kock, N., Verville, J., Danesh‐Pajou, A., & DeLuca, D. (2009). Communication flow orientation in business process modeling and its effect on redesign success: Results from a field study. Decision Support Systems, 46(2), 562–575. https://doi.org 10.1016/i,dss,2008.10.002

Lohmöller, J.‐B. (1989). Latent variable path modeling with partial least squares. In Heidelberg. Germany: Physica‐Verlag https://doi.org/10.1007/978‐3‐642‐52512‐4

MacCallum, R. C., & Tucker, L. R. (1991). Representing sources of error in the common‐factor model: Implications for theory and practice. Psychological Bulletin, 109(3), 502–511. https://doi.org/10.1037/0033‐2909.109.3.502

McIntosh, C. N., Edwards, J. R., & Antonakis, J. (2014). Reflections on partial least squares path modeling. Organizationa Research Methods, 7(2), 210–251.

Mendling, J., Strembeck, M., & Recker, J. (2012). Factors of process model comprehension—Findings from a series of exper iments. Decision Support Systems, 53(1), 195–206. https://doi.org/10.1016/j.dss.2011.12.013

Moqbel, M., Nevo, S., & Kock, N. (2013). Organizational members' use of social networking sites and job performance: An exploratory study. Information Technology & People, 26(3), 240–264. https://doi.org/10.1108/ITP‐10‐2012‐011

Mueller, R. O. (1996). Basic principles of structural equation modeling. New York, NY: Springer. https://doi.org/10.1007/978 1‐4612‐3974‐1

Nikitin, I. I., & Nikitin, Y. (1995). Asymptotic efficiency of nonparametric tests. Cambridge, England: Cambridge Universit Press. https://doi.org/10.1017/CBO9780511530081

Nunnally, J. C., & Bernstein, I. H. (1994). Psychometric theory. New York, NY: McGraw‐Hill

Nunnaly, J. C. (1978). Psychometric theory. New York, NY: McGraw Hill.

Paxton, P., Curran, P. J., Bollen, K. A., Kirby, J., & Chen, F. (2001). Monte Carlo experiments: Design and implementation Structural Equation Modeling, 8(2), 287–312. https://doi.org/10.1207/S15328007SEM0802\_7

Peterson, R. A., & Yeolib, K. (2013). On the relationship between coefficient alpha and composite reliability. Journal of Applied Psychology, 98(1), 194–198. https://doi.org/10.1037/a0030767

Rigdon, E. E. (2012). Rethinking partial least squares path modeling: In praise of simple methods. Long Range Planning, 45(5– 6), 341–358. https://doi.org/10.1016/j.lrp.2012.09.010

Rigdon, E. E., Sarstedt, M., & Ringle, C. M. (2017). On comparing results from CB‐SEM and PLS‐SEM: Five perspectives and five recommendations. Marketing ZFP, 39(3), 4–16. https://doi.org/10.15358/0344‐1369‐2017‐3‐4

Robert, C. P., & Casella, G. (2005). Monte Carlo statistical methods. New York, NY: Springer.

Rönkkö, M. (2014). The effects of chance correlations on partial least squares path modeling. Organizational Research Methods, 17(2), 164–181. https://doi.org/10.1177/1094428114525667

Rönkkö, M., & Evermann, J. (2013). A critical examination of common beliefs about partial least squares path modeling. Orga nizational Research Methods, 16(3), 425–448. https://doi.org/10.1177/1094428112474693

Rönkkö, M., McIntosh, C. N., & Antonakis, J. (2015). On the adoption of partial least squares in psychological research: Caveat emptor. Personality and Individual Differences, 87(1), 76–84. https://doi.org/10.1016/j.paid.2015.07.019

Rosseel, Y. (2012). lavaan: An R package for structural equation modeling. Journal of Statistical Software, 48(2), 1–36.

Sarstedt, M., Diamantopoulos, A., & Salzberger, T. (2016). Should we use single items? Better not. Journal of Business Research, 69(8), 3199–3203. https://doi.org/10.1016/j.jbusres.2016.02.040

Shmueli, G., Ray, S., Estrada, J. M. V., & Chatla, S. B. (2016). The elephant in the room: Predictive performance of PLS models Journal of Business Research, 69(10), 4552–4564. https://doi.org/10.1016/j.jbusres.2016.03.04

Siegel, S., & Castellan, N. J. (1998). Nonparametric statistics for the behavioral sciences. Boston, MA: McGraw‐Hill

Sijtsma, K. (2009). On the use, the misuse, and the very limited usefulness of Cronbach's alpha. Psychometrika, 74(1), 107–120. https://doi.org/10.1007/s11336‐008‐9101‐0

Thurstone, L. L. (1935). The vectors of mind. Chicago, IL: University of Chicago Press

Wanous, J. P., & Reichers, A. E. (1996). Estimating the reliability of a single‐item measure. Psychological Reports, 78(2), 631–634. https://doi.org/10.2466/pr0.1996.78.2.631

Wanous, J. P., Reichers, A. E., & Hudy, M. J. (1997). Overall job satisfaction: How good are single‐item measures? Journal of Applied Psychology, 82(2), 247–252. https://doi.org/10.1037/0021‐9010.82.2.247

Wold, H. (1980). Model construction and evaluation when theoretical knowledge is scarce. In J. Kmenta, & J. B. Ramsey (Eds.), Evaluation of econometric models (pp. 47–74). Waltham, MA: Academic Press. https://doi.org/10.1016/B978-0- 12-416550-2.50007-8

Wright, S. (1934). The method of path coefficients. The Annals of Mathematical Statistics, 5(3), 161–215. https://doi.org/ 10.1214/aoms/1177732676

Wright, S. (1960). Path coefficients and path regressions: Alternative or complementary concepts? Biometrics, 16(2), 189–202. https://doi.org/10.2307/2527551

## AUTHOR BIOGRAPHY

Ned Kock is a Killam distinguished professor and the chair of the Division of International Business and Technology Studies, in the Sanchez School of Business, at Texas A&M International University. He holds degrees in electronics engineering (BEE), computer science (MS), and management (PhD). Ned has authored and edited several books, including the Sage Publications book titled Systems Analysis and Design Fundamentals: A Business Process Redesign Approach. He has published his research in a number of high‐impact journals including Communications of the ACM, Decision Support Systems, European Journal of Information Systems, European Journal of Operationa Research, IEEE Transactions (various), Information & Management, Information Systems Journal, Journal of the Asso ciation for Information Systems, Journal of Management Information Systems, MIS Quarterly, and Organization Sci ence. He is the developer of media naturalness theory, a communications theory building on evolutionary biology that has been extensively cited by researchers in a variety of fields. He is also the developer of WarpPLS, a widely used structural equation modelling software.

How to cite this article: Kock N. From composites to factors: Bridging the gap between PLS and covariancebased structural equation modelling. Info Systems J. 2019;29:674–706. https://doi.org/10.1111/isj.12228

## APPENDIX A

## DERIVATIONS OF EQUATIONS

Equations A.1, A.2, and A.3 below provide the foundation of $\mathcal { F } _ { 2 } ,$ , the composite estimation function. In these equa tions, $x _ { j }$ is a matrix where each column refers to one of the indicators associated with composite $\widehat { C } _ { i }$ (and thus with factor $\widehat { F } _ { i } ) ; \widehat { \lambda } _ { i } ^ { ' }$ is the transpose of $\widehat { \lambda } _ { i } ,$ , the column vector storing the loadings associated with the indicators; $\widehat { \theta } _ { i }$ is the matrix of indicator error terms; $\widehat { \omega } _ { i C }$ is the composite weight; $\widehat { \omega } _ { i \varepsilon }$ is the measurement residual weight; $\widehat { \omega } _ { i }$ is the column vector of indicator weights; the superscript −1 denotes the classic matrix inversion; and the superscript + denotes the Moore‐Penrose pseudoinverse transformation.

$$
\widehat {F} _ {i} = \operatorname{Std} z \left(\widehat {C} _ {i} \widehat {\omega} _ {i C} + \widehat {\varepsilon} _ {i} \widehat {\omega} _ {i \varepsilon}\right).\tag{A.1}
$$

$$
\widehat {\theta} _ {i} = x _ {i} - \widehat {F} _ {i} \widehat {\lambda} _ {i} ^ {\prime}.\tag{A.2}
$$

$$
\widehat {\omega} _ {i} = \Sigma_ {x _ {i} x _ {i}} ^ {- 1} \bigg (\Sigma_ {x _ {i} x _ {i}} - \mathrm{diag} \bigg (\Sigma_ {x _ {i} \widehat {\theta} _ {i}} \bigg) \bigg) \widehat {\lambda} _ {i} ^ {' +}.\tag{A.3}
$$

Derivation of (A.1). From our previous discussion on composites and factors, we know that

$$
F _ {i} = x _ {i} \omega_ {i} + \varepsilon_ {i} \omega_ {i \varepsilon},   x _ {i} \omega_ {i} = C _ {i} \omega_ {i C}.
$$

Thus, it follows that

$$
F _ {i} = C _ {i} \omega_ {i C} + \varepsilon_ {i} \omega_ {i \varepsilon},
$$

where $F _ { j }$ is expected to be standardized.

Derivation of (A.2). From our previous discussion on composites and factors, we know that

$$
\mathsf {x} _ {\mathrm{i}} = \mathsf {F} _ {\mathrm{i}} \lambda_ {\mathrm{i}} ^ {\prime} + \theta_ {\mathrm{i}}.
$$

Thus it follows that

$$
\theta_ {i} = x _ {i} - F _ {i} \lambda_ {i} ^ {\prime}.
$$

Derivation of (A.3). From our previous discussion on composites and factors, we know that

$$
x _ {i} = F _ {i} \lambda_ {i} ^ {\prime} + \theta_ {i}, F _ {i} = x _ {i} \omega_ {i} + \varepsilon_ {i} \omega_ {i \varepsilon}
$$

Combining these two equations, we obtain

$$
x _ {i} = (x _ {i} \omega_ {i} + \varepsilon_ {i} \omega_ {i \varepsilon}) \lambda_ {i} ^ {\prime} + \theta_ {i} \rightarrow
$$

$$
x _ {i} = x _ {i} \omega_ {i} \lambda_ {i} ^ {\prime} + \varepsilon_ {i} \omega_ {i \varepsilon} \lambda_ {i} ^ {\prime} + \theta_ {i}.
$$

Applying covariance properties to the above, we obtain

$$
\Sigma_ {x _ {i} x _ {i}} = \Sigma_ {x _ {i} x _ {i}} \omega_ {i} \lambda_ {i} ^ {\prime} + \Sigma_ {x _ {i} \varepsilon_ {i}} \omega_ {i \varepsilon} \lambda_ {i} ^ {\prime} + \Sigma_ {x _ {i} \theta_ {i}} \rightarrow
$$

$$
\begin{array}{r}\Sigma_ {x _ {i} x _ {i}} = \Sigma_ {x _ {i} x _ {i}} \omega_ {i} \lambda_ {i} ^ {\prime} + \mathrm{diag} (\Sigma_ {x _ {i} \theta_ {i}}) \rightarrow\\\Sigma_ {x _ {i} x _ {i}} \omega_ {i} \lambda_ {i} = \Sigma_ {x _ {i} x _ {i}} - \mathrm{diag} (\Sigma_ {x _ {i} \theta_ {i}}) \rightarrow\end{array}
$$

$$
\omega_ {i} \lambda_ {i} ^ {\prime} = \Sigma_ {x _ {i} x _ {i}} ^ {- 1} \left(\Sigma_ {x _ {i} x _ {i}} - \operatorname{diag} \left(\Sigma_ {x _ {i} \theta_ {i}}\right)\right),
$$

where the superscript −1 denotes the classic matrix inversion.

To isolate $\omega _ { j }$ in the equation above, we need to use the Moore‐Penrose pseudoinverse transformation, since the classic matrix inversion transformation cannot be applied to a vector. Doing this, we obtain

$$
\omega_ {i} = \Sigma_ {x _ {i} x _ {i}} ^ {- 1} \left(\Sigma_ {x _ {i} x _ {i}} - \operatorname{diag} \left(\Sigma_ {x _ {i} \theta_ {i}}\right)\right) \lambda_ {i} ^ {\prime +},
$$

where the superscript + denotes the Moore‐Penrose pseudoinverse transformation.

Equations A.4, A.5, and A.6 below provide the foundation of $\mathcal { F } _ { 3 }$ , the factor estimation function. Each of these equations includes a variable being updated with a “mix” of itself and other variables, a technique we refer to as “variation sharing,” which causes that variable to receive or lose variation that resides in those other variables Whether variation is gained or lost depends on the sign of the multiplier attached to those other variables. For exam ple, let us consider the simple assignment $\begin{array} { r } { Y = S t d z ( Y + a X ) } \end{array}$ , where both Y and X are standardized. The variable Y gains variation from the variable X if $a > 0$ and loses variation from X if $a < 0 .$ . In either case, the amount of variation gained or lost is reflected in the correlation between Y and X, which itself is a function of a. The more variation Y and X share the greater is the correlation between them. If $a = 0$ , no variation is gained or lost.

$$
\widehat {\varepsilon} _ {i} = \operatorname{Std} z \left(\widehat {\varepsilon} _ {i} + \left(\widehat {\Sigma} _ {F _ {i} F _ {j}} - \Sigma_ {\widehat {F _ {i} F _ {j}}}\right) \frac {\widehat {\Sigma} _ {F _ {i} F _ {j}}}{\widehat {\omega} _ {i \varepsilon}} \left(\widehat {C} _ {j} \widehat {\omega} _ {j C} + \widehat {\varepsilon} _ {j} \widehat {\omega} _ {j \varepsilon}\right)\right),\tag{A.4}
$$

$$
\widehat {F} _ {i} = \operatorname{Std} z \left(\widehat {F} _ {i} + \left(\widehat {\omega} _ {i C} - \Sigma_ {\widehat {F _ {i} C _ {i}}}\right) \widehat {C} _ {i} \widehat {\omega} _ {i C}\right).\tag{A.5}
$$

$$
\widehat {\varepsilon} _ {i} = \operatorname{Stdz} \left(\widehat {\varepsilon} _ {i} - \Sigma_ {\widehat {C _ {i}} \widehat {\varepsilon_ {i}}} \widehat {C} _ {i} \widehat {\omega} _ {i C} + \left(\widehat {\omega} _ {i \varepsilon} - \Sigma_ {\widehat {F _ {i}} \widehat {\varepsilon_ {i}}}\right) \widehat {F} _ {i} \widehat {\omega} _ {i \varepsilon}\right).\tag{A.6}
$$

Derivation of (A.4). From our previous discussion on composites and factors, we know that for each pair of correlated factors $F _ { j }$ and $F _ { j } ,$ we have

$$
F _ {i} = C _ {i} \omega_ {i C} + \varepsilon_ {i} \omega_ {i \varepsilon}, F _ {j} = C _ {j} \omega_ {j C} + \varepsilon_ {j} \omega_ {j \varepsilon}, F _ {i} = \Sigma_ {F _ {i} F _ {j}} F _ {j} + \delta_ {i j},
$$

where $\delta _ { i j }$ is an error term that accounts the variance in $F _ { j }$ that is not explained by $F _ { j } .$

Combining these equations, we have

$$
C _ {i} \frac {\omega_ {i C}}{\omega_ {i \varepsilon}} + \varepsilon_ {i} = \frac {1}{\omega_ {i \varepsilon}} \Sigma_ {F _ {i} F _ {j}} \left(C _ {j} \omega_ {j C} + \varepsilon_ {j} \omega_ {j \varepsilon}\right) + \frac {\delta_ {i j}}{\omega_ {i \varepsilon}}.
$$

We can see that $\varepsilon _ { j }$ shares variation with $C _ { j }$ and $\varepsilon _ { j }$ proportionally to

$$
\frac {\Sigma_ {F _ {i} F _ {j}}}{\omega_ {i \varepsilon}} \left(C _ {j} \omega_ {j C} + \varepsilon_ {j} \omega_ {j \varepsilon}\right).
$$

Thus, in order to make $\Sigma _ { \widehat { F _ { i } F _ { i } } } = \widehat { \Sigma } _ { F _ { i } F _ { j } }$ , we iteratively assign

$$
\widehat {\varepsilon} _ {i} = \operatorname{Stdz} \left(\widehat {\varepsilon} _ {i} + \left(\widehat {\Sigma} _ {F _ {i} F _ {j}} - \Sigma_ {\widehat {F} _ {i} \widehat {F} _ {j}}\right) \frac {\widehat {\Sigma} _ {F _ {i} F _ {j}}}{\widehat {\omega} _ {i \varepsilon}} \left(\widehat {C} _ {j} \widehat {\omega} _ {j C} + \widehat {\varepsilon} _ {j} \widehat {\omega} _ {j \varepsilon}\right)\right).
$$

Note that as $\widehat { \varepsilon } _ { i }$ changes, so does ${ \widehat { F } } _ { i } ,$ because $\begin{array} { r } { F _ { i } = C _ { i } \omega _ { i C } + \varepsilon _ { i } \omega _ { i \varepsilon } , } \end{array}$ , and also that this assignment is only made if $\widehat { \omega } _ { i \varepsilon } > 0$

Derivation of (A.5). As noted above,

$$
F _ {i} = C _ {i} \omega_ {i C} + \varepsilon_ {i} \omega_ {i \varepsilon}.
$$

We can see that $F _ { j }$ shares variation with $C _ { j }$ proportionally to

$$
C _ {i} \omega_ {i C}.
$$

Thus, in order to make $\Sigma _ { \widehat { F _ { i } C _ { i } } } = \widehat { \omega } _ { i C }$ , we iteratively assign

$$
\widehat {F} _ {i} = \operatorname{Stdz} \left(\widehat {F} _ {i} + \left(\widehat {\omega} _ {i C} - \Sigma_ {\widehat {F _ {i}} \widehat {C _ {i}}}\right) \widehat {C} _ {i} \widehat {\omega} _ {i C}\right).
$$

Derivation of $( \mathsf { A } . 6 )$ . From our previous discussion on composites and factors, we know that

$$
\varepsilon_ {i} \bot C _ {i}, \quad \varepsilon_ {i} = F _ {i} \omega_ {i \varepsilon} + \theta_ {i \varepsilon},
$$

where ⊥ means “orthogonal $\mathrm { t o } ^ { \dprime }$ and $\theta _ { i \varepsilon }$ is an error term that accounts for the variation in $\varepsilon _ { j }$ that is not explained by $F _ { i \cdot }$ Note that $\omega _ { i \varepsilon } = \lambda _ { i \varepsilon } .$

We can see that $\varepsilon _ { j }$ shares no variation with $C _ { j }$ and also that $\varepsilon _ { j }$ shares variation with $F _ { j }$ proportionally to

$$
F _ {i} \omega_ {i \varepsilon}.
$$

Thus, in order to make $\Sigma _ { \widehat { C _ { i } \varepsilon _ { i } } } = 0$ and $\Sigma _ { \widehat { F _ { i } } \widehat { \varepsilon _ { i } } } = \widehat { \omega } _ { i \varepsilon }$ , we iteratively assign

$$
\widehat {\varepsilon} _ {i} = \operatorname{Stdz} \left(\widehat {\varepsilon} _ {i} - \Sigma_ {\widehat {C _ {i}} \widehat {\varepsilon_ {i}}} \widehat {C} _ {i} \widehat {\omega} _ {i C} + \left(\widehat {\omega} _ {i \varepsilon} - \Sigma_ {\widehat {F _ {i}} \widehat {\varepsilon_ {i}}}\right) \widehat {F} _ {i} \widehat {\omega} _ {i \varepsilon}\right).
$$

Note that the multiplier $- \sum _ { C _ { i } \varepsilon _ { i } }$ is derived from $0 - \Sigma _ { \widehat { C _ { i } \varepsilon _ { i } } }$

## APPENDIX B

## ALGORITHMIC FORMULATION OF PLSF

In this appendix, we provide all of the equations that make up the PLSF method, for each of the four functions, as well as the algorithmic sequence of their execution and related explanatory notes. We do this with the goal of facil itating the implementation of the method in any numeric computing environment, including open source environ ments such as R and GNU Octave.

## Function $\mathcal { F } _ { 1 } \colon$ the consistent PLS function

In the steps below, $\dot { I } = 1 . . . N _ { C } ,$ and $j = 1 . . . n _ { \mathrm { i } } ,$ , where $N _ { C }$ is the number of composites in the model (the same as the number of factors) and $n _ { j }$ is the number of indicators associated with each composite $C _ { i } .$ Steps 1.1 to 1.7 implement the basic design of PLS mode $\mathsf { A } ,$ also known as PLS mode A, employing the centroid scheme.

Step 1.1 Initialize each indicator weight $\widehat { \omega } _ { i j }$ with 1.

Step 1.2 Store each indicator weight in $\overline { { \overline { { \mathbf { \alpha } } } } } _ { \omega _ { i j } }$ for later comparison.

Step 1.3 Estimate each composite ${ \widehat { C } } _ { i }$ as

$$
\widehat {C} _ {i} = \operatorname{Stdz} \left(\sum_ {j = 1} ^ {n _ {i}} \widehat {\omega} _ {i j} x _ {i j}\right).
$$

where Stdz(·) is the standardization function.

Step 1.4 Set each inner weight $\widehat { v } _ { i j }$ as

$$
\widehat {\mathsf {V}} _ {\mathrm{ij}} = \operatorname{Sign} \left(\Sigma_ {\widehat {\mathsf {C} _ {\mathrm{i}}} \widehat {\mathsf {C} _ {\mathrm{j}}}}\right).
$$

Here, the inner weights are set as the signs $( - 1 \mathsf { o r } + 1 )$ of the estimated correlations among “neighbour” compos ites. Neighbour composites are those that are linked to a composite by arrows, either by pointing at or being pointed at by the composite.

Step 1.5 Estimate each composite ${ \widehat { C } } _ { i }$ as

$$
\widehat {\mathsf {C}} _ {\mathrm{i}} = \operatorname{Std} z \left(\sum_ {\mathrm{j} = 1} ^ {\mathrm{A} _ {\mathrm{i}}} \widehat {\mathrm{v}} _ {\mathrm{ij}} \widehat {\mathsf {C}} _ {\mathrm{j}}\right),
$$

where $S t d z ( \cdot )$ is the standardization function and $A _ { j }$ is the number of composite $\widehat { C } _ { j } \ ( j = 1 . . . A _ { i } )$ that are neighbours of the composite $\widehat { C } _ { i }$

Step 1.6 Solve for each indicator weight $\widehat { \omega } _ { i j }$ the equation

$$
\mathsf {x} _ {\mathrm{ij}} = \widehat {\mathsf {C}} _ {\mathrm{i}} \widehat {\omega} _ {\mathrm{ij}} + \widehat {\epsilon} _ {\mathrm{ij}},
$$

where $\widehat { \epsilon } _ { i j }$ is an error term that accounts for the variation in $x _ { i j }$ that is not explained by ${ \widehat { C } } _ { i }$

Step 1.7 Go back to step 1.2 if any indicator weight $\widehat { \omega } _ { i j }$ differs from the previously stored estimate $\overline { { \mathbf { \Omega } } } _ { \omega _ { i j } }$ by more than a small fraction.

Step 1.8 Estimate each reliability $\widehat { \rho } _ { i }$ and loading vector $\widehat { \lambda } _ { i }$ as

$$
\widehat {\rho} _ {i} = \left(\widehat {\omega} _ {i} ^ {\prime} \widehat {\omega} _ {i}\right) ^ {2} \left(\widehat {\omega} _ {i} ^ {\prime} \left(\Sigma_ {x _ {i} x _ {i}} - \operatorname{diag} \left(\Sigma_ {x _ {i} x _ {i}}\right)\right) \widehat {\omega} _ {i}\right) / \left(\widehat {\omega} _ {i} ^ {\prime} \left(\widehat {\omega} _ {i} \widehat {\omega} _ {i} ^ {\prime} - \operatorname{diag} \left(\widehat {\omega} _ {i} \widehat {\omega} _ {i} ^ {\prime}\right)\right) \widehat {\omega} _ {i}\right),
$$

$$
\widehat {\lambda} _ {i} = \left(\widehat {\omega} _ {i} \sqrt {\widehat {\rho} _ {i}}\right) / \left(\widehat {\omega} _ {i} ^ {\prime} \widehat {\omega} _ {i}\right),
$$

where the superscript <sup>′</sup> denotes the transpose operation, $\Sigma _ { x _ { j } x _ { j } }$ is the covariance matrix of the indicators associated with composite $C _ { i } ,$ and the function diag(·) returns the diagonal of a matrix.

Function $\mathcal { F } _ { 2 } \colon$ the composite estimation function.

In the steps below, $\dot { I } = 1 . . . N _ { C } ,$ where $N _ { C }$ is the number of composites (the same as the number of factors) in the model. From the previous function come estimates of reliabilities and indicator loadings. Also from the previous function come initial estimates of composites and indicator weights

Step 2.1 Set each measurement residua ${ \widehat { \varepsilon } } _ { i } ,$ composite weight $\omega _ { i C } ,$ , and measurement residual weight $\omega _ { i \varepsilon }$ as

$$
\widehat {\varepsilon} _ {i} = \operatorname{Stdz} (\operatorname{Rnd} (N)),
$$

$$
\omega_ {\mathrm{iC}} = \sqrt {\rho_ {\mathrm{i}}},
$$

$$
\omega_ {\mathrm{i} \varepsilon} = \sqrt {1 - \rho_ {\mathrm{i}}},
$$

where Rnd(N) is a function that returns an independent and identically distributed (i.i.d.) variable with N rows, with N being the sample size. In software implementations, the random seed may be set to a fixed value prior to settin $\widehat { \varepsilon } _ { i }$ in order to avoid different results each time an analysis is conducted with the same model and empirical data

Step 2.2 Store all weight vectors $\widehat { \omega } _ { i } \mathrm { i n } ^ { = } \omega _ { i }$ for later comparison.

Step 2.3 Set each factor ${ \widehat F } _ { i }$ as

$$
\widehat {F} _ {i} = \operatorname{Stdz} \left(\widehat {C} _ {i} \widehat {\omega} _ {i C} + \widehat {\varepsilon} _ {i} \widehat {\omega} _ {i \varepsilon}\right).
$$

Step 2.4 Set each indicator error matrix ${ \widehat { \theta } } _ { i }$ as

$$
\widehat {\theta} _ {i} = x _ {i} - \widehat {F} _ {i} \widehat {\lambda} _ {i} ^ {\prime},
$$

where $x _ { j }$ is the matrix of indicators associated with factor $\widehat { F } _ { i } , \widehat { \lambda } _ { i }$ is the vector of loadings associated with the factor, and the <sup>′</sup> superscript indicates the transpose operation.

Step 2.5 Estimate each weight vector $\widehat { \omega } _ { i }$ as

$$
\widehat {\omega} _ {i} = \Sigma_ {x _ {i} x _ {i}} ^ {- 1} \left(\Sigma_ {x _ {i} x _ {i}} - \operatorname{diag} \left(\Sigma_ {\widehat {x _ {i} \theta_ {i}}}\right)\right) \widehat {\lambda} _ {i} ^ {\prime +},
$$

where $\textstyle \sum _ { x _ { j } \ = x _ { j } }$ is the covariance matrix of the indicators associated with factor $\widehat { F } _ { i } , \Sigma _ { \widehat { x _ { i } \theta _ { i } } }$ is the matrix of covariances among the indicators and their errors, diag(·) is a function that returns the diagonal version of a matrix, and the superscript + denotes the Moore‐Penrose pseudoinverse transformation.

Step 2.6 Estimate each composite ${ \widehat { C } } _ { i }$ as

$$
\widehat {C} _ {\mathrm{i}} = \frac {1}{\widehat {\omega} _ {\mathrm{iC}}} (x _ {\mathrm{i}} \widehat {\omega} _ {\mathrm{i}}).
$$

Step 2.7 Go back to step 2.2 if any element of any of the weight vectors $\widehat { \omega } _ { i }$ differs from the previously stored esti mates in $\overline { { \overline { { \mathbf { \alpha } } } } } _ { \omega _ { i } }$ by more than a small fraction.

Function $\mathcal { F } _ { 3 } \mathrm { : }$ : the factor estimation function.

In the steps below, ${ \sf i } , { \sf j } = 1 . . . N _ { F }$ . Here, $N _ { F }$ is the number of factors in the model. Each combination $( \mathfrak { i } , \mathfrak { j } )$ refers to a pair of correlated elements in the model: factors, composites, or measurement residuals. From the previous function come estimates of composites, indicator weights, composite weights, and measurement residual weights. Also come from the previous function initial estimates of measurement residuals. The steps below are carried out for a given factor only if $\widehat { \omega } _ { i \varepsilon } > 0$

Step 3.1 Initialize each factor ${ \widehat F } _ { i }$ as

$$
\widehat {F} _ {i} = \operatorname{Std} z \left(\widehat {C} _ {i} \widehat {\omega} _ {i C} + \widehat {\varepsilon} _ {i} \widehat {\omega} _ {i \varepsilon}\right).
$$

Step 3.2 Set each element of the estimated matrix of correlations among factors $\widehat { \Sigma } _ { F _ { i } F _ { j } }$ as

$$
\widehat {\Sigma} _ {F _ {i} F _ {j}} = \frac {\Sigma_ {\widehat {C _ {i}} \widehat {C _ {j}}}}{\sqrt {\widehat {\rho} _ {i} \widehat {\rho} _ {j}}},
$$

where $\boldsymbol { \Sigma } _ { \widehat { C _ { i } C _ { j } } }$ is the corresponding element of the matrix of correlations among estimated composites.

Step 3.3 Calculate the matrix of correlations among estimated factors $\Sigma _ { \widehat { F F } }$ and store it in $\overline { { \sum } } _ { \widehat { F F } }$ for later comparison. Note that this is not the same as the estimated matrix of correlations among factors $\widehat { \Sigma } _ { F F }$ , which is fixed after step 3.2.

Step 3.4 Add or remove variation in each measurement residual $\widehat { \varepsilon } _ { i }$ by making

$$
\widehat {\varepsilon} _ {i} = \operatorname{Std} z \left(\widehat {\varepsilon} _ {i} + \left(\widehat {\Sigma} _ {F _ {i} F _ {j}} - \Sigma_ {\widehat {F _ {i} F _ {j}}}\right) \frac {\widehat {\Sigma} _ {F _ {i} F _ {j}}}{\widehat {\omega} _ {i \varepsilon}} \left(\widehat {C} _ {j} \widehat {\omega} _ {j C} + \widehat {\varepsilon} _ {j} \widehat {\omega} _ {j \varepsilon}\right)\right),
$$

where $\widehat { \Sigma } _ { \widehat { F _ { i } F _ { j } } }$ is the correlation among each pair of estimated factors.

Step 3.5 Add or remove variation in each factor ${ \widehat F } _ { i }$ by making

$$
\widehat {F} _ {i} = \operatorname{Stdz} \left(\widehat {F} _ {i} + \left(\widehat {\omega} _ {i C} - \Sigma_ {\widehat {F _ {i}} \widehat {C _ {i}}}\right) \widehat {C} _ {i} \widehat {\omega} _ {i C}\right),
$$

where $\overline { { \Sigma } } _ { \widehat { F _ { i } C _ { i } } }$ is the correlation among an estimated factor and its composite

Step 3.6 Add or remove variation in each measurement residual $\widehat { \varepsilon } _ { i }$ by making

$$
\widehat {\varepsilon} _ {i} = \operatorname{Stdz} \left(\widehat {\varepsilon} _ {i} - \Sigma_ {\widehat {C _ {i}} \widehat {\varepsilon_ {i}}} \widehat {C} _ {i} \widehat {\omega} _ {i C} + \left(\widehat {\omega} _ {i \varepsilon} - \Sigma_ {\widehat {F _ {i}} \widehat {\varepsilon_ {i}}}\right) \widehat {F} _ {i} \widehat {\omega} _ {i \varepsilon}\right),
$$

where $\Sigma _ { \widehat { C _ { i } \varepsilon _ { i } } }$ is the correlation between an estimated composite and its corresponding measurement residual and $\Sigma _ { \widehat { F _ { i } \varepsilon _ { i } } }$ is the correlation between an estimated factor and its measurement residual

Step 3.7 Estimate each factor ${ \widehat F } _ { i }$ as

$$
\widehat {F} _ {i} = \operatorname{Stdz} \left(\widehat {C} _ {i} \widehat {\omega} _ {i C} + \widehat {\varepsilon} _ {i} \widehat {\omega} _ {i \varepsilon}\right).
$$

Step 3.8 Estimate each measurement residual $\widehat { \varepsilon } _ { i }$ as

$$
\widehat {\varepsilon} _ {i} = \operatorname{Stdz} \left(\frac {1}{\widehat {\omega} _ {i \varepsilon}} \left(\widehat {F} _ {i} - \widehat {C} _ {i} \widehat {\omega} _ {i C}\right)\right).
$$

Step 3.9 Go back to step 3.3 if the absolute sums of the differences in $\Sigma _ { \widehat { F F } } - \widehat { \Sigma } _ { F F }$ and in $\boldsymbol { \Sigma } _ { \widehat { \boldsymbol { F } \boldsymbol { F } } } - \overline { { \boldsymbol { \Sigma } } } _ { \widehat { \boldsymbol { F } \boldsymbol { F } } }$ both fall above a small fraction.

## Function $\mathcal { F } _ { 4 } \colon$ : the full‐parameter estimation function

In the steps below, $\dot { \iota } = 1 . . . N _ { F }$ , where $N _ { F }$ is the number of factors in the model. From the previous function come estimates of factors, measurement residuals, composite weights, and measurement residual weights.

Step 4.1 Update each composite $\widehat { C } _ { i }$ as

$$
\widehat {C} _ {i} = \operatorname{Stdz} \left(\frac {1}{\widehat {\omega} _ {i C}} \left(\widehat {F} _ {i} - \widehat {\varepsilon} _ {i} \widehat {\omega} _ {i \varepsilon}\right)\right).
$$

Step 4.2 Update each weight vector $\widehat { \omega } _ { i }$ as

$$
\widehat {\omega} _ {i} = x _ {i} ^ {+} \widehat {C} _ {i} \widehat {\omega} _ {i C}.
$$

Step 4.3 Update each loading vector $\widehat { \lambda } _ { i }$ as

$$
\widehat {\lambda} _ {i} = x _ {i} ^ {\prime} \widehat {F} _ {i} ^ {\prime +}.
$$

Step 4.4 Estimate each indicator residual ${ \widehat { \theta } } _ { i }$ as

$$
\widehat {\theta} _ {i} = x _ {i} - \widehat {F} _ {i} \widehat {\lambda} _ {i} ^ {\prime}.
$$

Step 4.5 Solve for each path coefficient ${ \widehat { \beta } } _ { i j }$ the equation involving an endogenous factor

$$
\widehat {F} _ {i} = \sum_ {j = 1} ^ {N _ {i}} \widehat {\beta} _ {i j} \widehat {F} _ {j} + \widehat {\beta} _ {i} \widehat {I} _ {i} + \widehat {\zeta} _ {i},
$$

where $\widehat { \zeta } _ { i }$ is the residual associated with the endogenous factor ${ \widehat F } _ { i }$ and $\widehat { F } _ { j } \ ( j = 1 . . . N _ { i } )$ are the factors that point at the endogenous factor. The instrumental variables $\widehat { I } _ { \dot { I } }$ implement a two‐stage least squares estimation; they exist for al endogenous factors in the model that contain variation from other factors but are not directly linked with those factors.

Step 4.6 Estimate each endogenous factor residual $\widehat { \zeta } _ { i }$ as

$$
\widehat {\zeta} _ {i} = \widehat {F} _ {i} - \sum_ {j = 1} ^ {N _ {i}} \widehat {\beta} _ {i j} \widehat {F} _ {j} - \widehat {\beta} _ {i} \widehat {I} _ {i}.
$$

At the end of the above steps for the four functions, which implement the four stages that make up the PLSF method, we are left with estimates of the following: $\widehat { F } , \widehat { C } , \widehat { \varepsilon } , \widehat { \zeta } , \widehat { \omega } , \widehat { \omega } _ { C } , \widehat { \omega } _ { \varepsilon } , \widehat { \lambda } , \widehat { \beta } ,$ and ${ \widehat { \theta } } .$ To the best of our knowledge no other SEM method provides such an extensive set of estimates. Given this, it is reasonable to expect that these estimates could serve as the basis for the development of a number of new tests that are not currently possible

## APPENDIX C

## LOADINGS AND WEIGHTS FOR CONSTRUCTS OTHER THAN AC

Table C1 below lists loadings and weights for constructs other than AC. These were not provided earlier, on the main body of the paper, to avoid crowding. The FIML method does not generate estimates of weights, which is why they are not listed in the table. The column labelled “True” lists the true values in our finite population of various

TABLE C1 Loadings and weights for constructs other than AC in finite population (N = 10 000)

<table><tr><td rowspan="2"></td><td rowspan="2">True</td><td colspan="2">PLSF</td><td colspan="2">FIML</td><td colspan="2">OLS</td><td colspan="2">PLS</td></tr><tr><td>Est.</td><td>Diff.</td><td>Est.</td><td>Diff.</td><td>Est.</td><td>Diff.</td><td>Est.</td><td>Diff.</td></tr><tr><td colspan="10">Loadings</td></tr><tr><td>CO1 &lt; CO</td><td>1.0000</td><td>1.0000</td><td>0.0000</td><td>1.0000</td><td>0.0000</td><td>1.0000</td><td>0.0000</td><td>1.0000</td><td>0.0000</td></tr><tr><td>EU1 &lt; EU</td><td>0.7988</td><td>0.7985</td><td>-0.0003</td><td>0.7994</td><td>0.0005</td><td>0.8439</td><td>0.0451</td><td>0.8420</td><td>0.0432</td></tr><tr><td>EU2 &lt; EU</td><td>0.7988</td><td>0.7986</td><td>-0.0002</td><td>0.7992</td><td>0.0004</td><td>0.8432</td><td>0.0445</td><td>0.8438</td><td>0.0451</td></tr><tr><td>EU3 &lt; EU</td><td>0.7964</td><td>0.8012</td><td>0.0048</td><td>0.8024</td><td>0.0061</td><td>0.8452</td><td>0.0488</td><td>0.8460</td><td>0.0496</td></tr><tr><td>EU4 &lt; EU</td><td>0.7993</td><td>0.8016</td><td>0.0022</td><td>0.8017</td><td>0.0024</td><td>0.8447</td><td>0.0454</td><td>0.8453</td><td>0.0459</td></tr><tr><td>EU5 &lt; EU</td><td>0.8018</td><td>0.7996</td><td>-0.0022</td><td>0.7987</td><td>-0.0031</td><td>0.8431</td><td>0.0414</td><td>0.8430</td><td>0.0413</td></tr><tr><td>GT1 &lt; GT</td><td>0.6062</td><td>0.6119</td><td>0.0057</td><td>0.6116</td><td>0.0054</td><td>0.7155</td><td>0.1093</td><td>0.7021</td><td>0.0959</td></tr><tr><td>GT2 &lt; GT</td><td>0.5943</td><td>0.5945</td><td>0.0001</td><td>0.5980</td><td>0.0037</td><td>0.7096</td><td>0.1153</td><td>0.6913</td><td>0.0970</td></tr><tr><td>GT3 &lt; GT</td><td>0.6988</td><td>0.6978</td><td>-0.0011</td><td>0.6935</td><td>-0.0053</td><td>0.7630</td><td>0.0641</td><td>0.7660</td><td>0.0671</td></tr><tr><td>GT4 &lt; GT</td><td>0.6981</td><td>0.7043</td><td>0.0062</td><td>0.6989</td><td>0.0008</td><td>0.7675</td><td>0.0694</td><td>0.7727</td><td>0.0746</td></tr><tr><td>GT5 &lt; GT</td><td>0.7968</td><td>0.7924</td><td>-0.0044</td><td>0.7982</td><td>0.0013</td><td>0.8155</td><td>0.0187</td><td>0.8355</td><td>0.0386</td></tr><tr><td>SU1 &lt; SU</td><td>0.5461</td><td>0.5480</td><td>0.0019</td><td>0.5476</td><td>0.0015</td><td>0.6753</td><td>0.1293</td><td>0.6472</td><td>0.1011</td></tr><tr><td>SU2 &lt; SU</td><td>0.6000</td><td>0.6065</td><td>0.0065</td><td>0.6033</td><td>0.0033</td><td>0.7085</td><td>0.1085</td><td>0.6957</td><td>0.0957</td></tr><tr><td>SU3 &lt; SU</td><td>0.6594</td><td>0.6560</td><td>-0.0034</td><td>0.6568</td><td>-0.0025</td><td>0.7354</td><td>0.0761</td><td>0.7409</td><td>0.0816</td></tr><tr><td>SU4 &lt; SU</td><td>0.6981</td><td>0.6906</td><td>-0.0075</td><td>0.6968</td><td>-0.0014</td><td>0.7596</td><td>0.0614</td><td>0.7702</td><td>0.0721</td></tr><tr><td>SU5 &lt; SU</td><td>0.7496</td><td>0.7507</td><td>0.0011</td><td>0.7498</td><td>0.0002</td><td>0.7847</td><td>0.0351</td><td>0.8048</td><td>0.0552</td></tr><tr><td colspan="10">Weights</td></tr><tr><td>CO1 &gt; CO</td><td>1.0000</td><td>1.0000</td><td>0.0000</td><td>...</td><td>...</td><td>1.0000</td><td>0.0000</td><td>1.0000</td><td>0.0000</td></tr><tr><td>EU1 &gt; EU</td><td>0.2242</td><td>0.2121</td><td>-0.0122</td><td>...</td><td>...</td><td>0.2370</td><td>0.0127</td><td>0.2317</td><td>0.0075</td></tr><tr><td>EU2 &gt; EU</td><td>0.2257</td><td>0.2268</td><td>0.0010</td><td>...</td><td>...</td><td>0.2370</td><td>0.0112</td><td>0.2386</td><td>0.0129</td></tr><tr><td>EU3 &gt; EU</td><td>0.2140</td><td>0.2137</td><td>-0.0003</td><td>...</td><td>...</td><td>0.2370</td><td>0.0229</td><td>0.2393</td><td>0.0253</td></tr><tr><td>EU4 &gt; EU</td><td>0.2234</td><td>0.2271</td><td>0.0037</td><td>...</td><td>...</td><td>0.2370</td><td>0.0135</td><td>0.2384</td><td>0.0150</td></tr><tr><td>EU5 &gt; EU</td><td>0.2342</td><td>0.2337</td><td>-0.0005</td><td>...</td><td>...</td><td>0.2370</td><td>0.0028</td><td>0.2367</td><td>0.0025</td></tr><tr><td>GT1 &gt; GT</td><td>0.1628</td><td>0.1687</td><td>0.0059</td><td>...</td><td>...</td><td>0.2652</td><td>0.1023</td><td>0.2392</td><td>0.0763</td></tr><tr><td>GT2 &gt; GT</td><td>0.1566</td><td>0.1613</td><td>0.0047</td><td>...</td><td>...</td><td>0.2652</td><td>0.1086</td><td>0.2329</td><td>0.0763</td></tr><tr><td>GT3 &gt; GT</td><td>0.2398</td><td>0.2232</td><td>-0.0165</td><td>...</td><td>...</td><td>0.2652</td><td>0.0254</td><td>0.2644</td><td>0.0246</td></tr><tr><td>GT4 &gt; GT</td><td>0.2355</td><td>0.2404</td><td>0.0049</td><td>...</td><td>...</td><td>0.2652</td><td>0.0297</td><td>0.2706</td><td>0.0351</td></tr><tr><td>GT5 &gt; GT</td><td>0.3787</td><td>0.3777</td><td>-0.0010</td><td>...</td><td>...</td><td>0.2652</td><td>-0.1135</td><td>0.3106</td><td>-0.0681</td></tr><tr><td>SU1 &gt; SU</td><td>0.1559</td><td>0.1534</td><td>-0.0025</td><td>...</td><td>...</td><td>0.2730</td><td>0.1171</td><td>0.2293</td><td>0.0735</td></tr><tr><td>SU2 &gt; SU</td><td>0.1838</td><td>0.1890</td><td>0.0052</td><td>...</td><td>...</td><td>0.2730</td><td>0.0892</td><td>0.2482</td><td>0.0645</td></tr><tr><td>SU3 &gt; SU</td><td>0.2383</td><td>0.2321</td><td>-0.0062</td><td>...</td><td>...</td><td>0.2730</td><td>0.0347</td><td>0.2771</td><td>0.0388</td></tr><tr><td>SU4 &gt; SU</td><td>0.2735</td><td>0.2694</td><td>-0.0041</td><td>...</td><td>...</td><td>0.2730</td><td>-0.0006</td><td>0.2885</td><td>0.0150</td></tr><tr><td>SU5 &gt; SU</td><td>0.3435</td><td>0.3463</td><td>0.0028</td><td>...</td><td>...</td><td>0.2730</td><td>-0.0705</td><td>0.3123</td><td>-0.0312</td></tr></table>

Abbreviations: FIML, full‐information maximum likelihood; OLS, ordinary least squares; PLS, partial least squares.  
parameters. The “Est.” columns list the corresponding estimates employing each method. The “Diff.” columns list th differences between estimates and true values for each method

## APPENDIX D

## PLSF VERSUS OTHER SIMILAR FACTOR‐BASED VARIATIONS

In this appendix, the PLSF method is compared against two additional methods. These methods are ordinary least squares regression with summed indicators and attenuation correction based on the Cronbach alpha coefficient (OLSa) and consistent PLS with attenuation correction based on its own true reliability estimate (PLSc). The former (ie, OLSa) has been proposed in general terms by Goodhue et al. (2012), and the latter (ie, PLSc) by Dijkstra & Henseler (2015a).

Table D1 lists the path coefficients and full collinearity VIFs for the same finite population used earlier in this paper. Table D2 lists a summarized set of loadings and weights for the finite population. To avoid crowding, and since the patterns observed here repeat themselves across latent variables and indicators, this summarized set focuses on accuracy $( \mathsf { A C } , \mathsf { F _ { 4 } } )$ and its respective indicators AC1, AC2, …, AC5.

TABLE D1 Path coefficients and full collinearity VIFs for finite population (N = 10 000)

<table><tr><td rowspan="2" colspan="2">True</td><td colspan="2">PLSF</td><td colspan="2">OLSa</td><td colspan="2">PLSc</td></tr><tr><td>Est.</td><td>Diff.</td><td>Est.</td><td>Diff.</td><td>Est.</td><td>Diff.</td></tr><tr><td colspan="8">Path coefficients</td></tr><tr><td>CO &gt; EU</td><td>0.4223</td><td>0.4208</td><td>-0.0015</td><td>0.4167</td><td>-0.0056</td><td>0.4161</td><td>-0.0062</td></tr><tr><td>CO &gt; GT</td><td>0.5074</td><td>0.5066</td><td>-0.0008</td><td>0.5060</td><td>-0.0013</td><td>0.5070</td><td>-0.0003</td></tr><tr><td>CO &gt; AC</td><td>0.2947</td><td>0.3021</td><td>0.0074</td><td>0.3043</td><td>0.0096</td><td>0.3059</td><td>0.0112</td></tr><tr><td>CO &gt; SU</td><td>0.0146</td><td>0.0137</td><td>-0.0009</td><td>0.0167</td><td>0.0021</td><td>0.0140</td><td>-0.0006</td></tr><tr><td>EU &gt; SU</td><td>0.1466</td><td>0.1479</td><td>0.0013</td><td>0.1433</td><td>-0.0033</td><td>0.1442</td><td>-0.0023</td></tr><tr><td>GT &gt; SU</td><td>0.5356</td><td>0.5331</td><td>-0.0025</td><td>0.5308</td><td>-0.0049</td><td>0.5343</td><td>-0.0013</td></tr><tr><td>AC &gt; SU</td><td>0.2562</td><td>0.2565</td><td>0.0003</td><td>0.2708</td><td>0.0146</td><td>0.2720</td><td>0.0158</td></tr><tr><td>RMSE</td><td></td><td>0.0031</td><td></td><td>0.0073</td><td></td><td>0.0078</td><td></td></tr><tr><td colspan="8">Full collinearity VIFs</td></tr><tr><td>CO</td><td>1.6618</td><td>1.6752</td><td>0.0135</td><td>1.6591</td><td>-0.0026</td><td>1.6626</td><td>0.0008</td></tr><tr><td>EU</td><td>1.2575</td><td>1.2541</td><td>-0.0034</td><td>1.2486</td><td>-0.0089</td><td>1.2500</td><td>-0.0076</td></tr><tr><td>GT</td><td>1.8865</td><td>1.8921</td><td>0.0055</td><td>1.8747</td><td>-0.0118</td><td>1.8894</td><td>0.0028</td></tr><tr><td>AC</td><td>1.2186</td><td>1.2181</td><td>-0.0005</td><td>1.2397</td><td>0.0211</td><td>1.2440</td><td>0.0253</td></tr><tr><td>SU</td><td>1.8813</td><td>1.8892</td><td>0.0079</td><td>1.8859</td><td>0.0046</td><td>1.9028</td><td>0.0215</td></tr><tr><td>RMSE</td><td></td><td>0.0076</td><td></td><td>0.0118</td><td></td><td>0.0153</td><td></td></tr></table>

TABLE D2 Summarized loadings and weights for finite population (N = 10 000)

<table><tr><td rowspan="2">True</td><td></td><td colspan="2">PLSF</td><td colspan="2">OLSa</td><td colspan="2">PLSc</td></tr><tr><td></td><td>Est.</td><td>Diff.</td><td>Est.</td><td>Diff.</td><td>Est.</td><td>Diff.</td></tr><tr><td colspan="8">Loadings</td></tr><tr><td>AC1 &lt; AC</td><td>0.4955</td><td>0.5007</td><td>0.0052</td><td>0.6507</td><td>0.1552</td><td>0.6288</td><td>0.1333</td></tr><tr><td>AC2 &lt; AC</td><td>0.5959</td><td>0.6005</td><td>0.0046</td><td>0.7048</td><td>0.1089</td><td>0.7038</td><td>0.1079</td></tr><tr><td>AC3 &lt; AC</td><td>0.5986</td><td>0.5969</td><td>-0.0017</td><td>0.6993</td><td>0.1007</td><td>0.6967</td><td>0.0980</td></tr><tr><td>AC4 &lt; AC</td><td>0.7003</td><td>0.6999</td><td>-0.0004</td><td>0.7540</td><td>0.0537</td><td>0.7658</td><td>0.0655</td></tr><tr><td>AC5 &lt; AC</td><td>0.7010</td><td>0.6981</td><td>-0.0028</td><td>0.7517</td><td>0.0507</td><td>0.7626</td><td>0.0617</td></tr><tr><td>RMSE</td><td></td><td>0.0034</td><td></td><td>0.1015</td><td></td><td>0.0971</td><td></td></tr><tr><td colspan="8">Weights</td></tr><tr><td>AC1 &gt; AC</td><td>0.1385</td><td>0.1387</td><td>0.0003</td><td>0.2782</td><td>0.1398</td><td>0.2458</td><td>0.1073</td></tr><tr><td>AC2 &gt; AC</td><td>0.2077</td><td>0.2132</td><td>0.0055</td><td>0.2802</td><td>0.0725</td><td>0.2766</td><td>0.0689</td></tr><tr><td>AC3 &gt; AC</td><td>0.2174</td><td>0.2171</td><td>-0.0003</td><td>0.2806</td><td>0.0632</td><td>0.2731</td><td>0.0558</td></tr><tr><td>AC4 &gt; AC</td><td>0.3168</td><td>0.3128</td><td>-0.0040</td><td>0.2827</td><td>-0.0340</td><td>0.3011</td><td>-0.0157</td></tr><tr><td>AC5 &gt; AC</td><td>0.3197</td><td>0.3144</td><td>-0.0053</td><td>0.2820</td><td>-0.0378</td><td>0.2992</td><td>-0.0206</td></tr><tr><td>RMSE</td><td></td><td>0.0038</td><td></td><td>0.0792</td><td></td><td>0.0633</td><td></td></tr></table>

![](/api/attachments/NTW5UZWR/fulltext/images/b4e379ffced8b87312798687c4524dd2ec80df4b84b6c4b2db3cac4fd5a40acf.jpg)

![](/api/attachments/NTW5UZWR/fulltext/images/12c8bf94fb55ce82cc310b4891963f3a050d649d42d19a8f78bfb20e6ad5aabf.jpg)

![](/api/attachments/NTW5UZWR/fulltext/images/225f3955b5098e51a359b3b7493e61d0c0ebd195f1b4697b18d9be5a44ebf328.jpg)

![](/api/attachments/NTW5UZWR/fulltext/images/1a834e23d0a0500f6b80416ff91cbbe9d606672a3555a25fb2a445ee875194af.jpg)  
FIGURE D1 Differences (RMSEs) with respect to true values [Colour figure can be viewed at wileyonlinelibrary. com]

In each table, the column labelled “True” lists the true values in our finite population of various parameters. Th “Est.” columns list the corresponding estimates employing each method. The “Diff.” columns list the differences between estimates and true values for each method. The row labelled “RMSE” lists root‐mean‐square errors associ ated with the differences between estimates, calculated as the square roots of the averages of the squared differ ences, which provide a summarized performance measure for each of the methods.

Figure D1 highlights the differences (RMSEs) with respect to true values for each of the methods.

As we can see, PLSF outperformed OLSa and PLSc in terms of estimation of path coefficients, full collinearity VIFs, loadings, and weights. The main reason why PLSF outperformed these methods is that it estimates compos ites in a way that is arguably more mathematically sound than the approaches employed by the two comparison methods.

Composites in OLSa are produced by simply summing indicators, whereas in PLSc, they are produced via the basic design of PLS mode A (Lohmöller, 1989, p. 29), also known as PLS mode A employing the centroid scheme Both OLSa and PLSc, like PLSF, perform an attenuation correction. A fundamental difference here, however, is that PLSF uses better estimates of the composites as departure points for attenuation correction

## APPENDIX E

## WHAT IF CO HAD BEEN MEASURED VIA MULTIPLE INDICATORS?

In this appendix, we present the results of an analysis with communication flow orientation (CO) measured through set of five indicators with heterogeneous loadings. The true loadings are listed below, together with other parameters and corresponding true values. In this new analysis, we employed the same finite population used earlier in this paper, with the key difference that we used the previous scores for CO (measured through single indicator) to generate the five new indicators. We then emploved the four methods to estimate CO based on those five new indicators, in the same way that other latent variables were estimated.

Table E1 lists the path coefficients and full collinearity VIFs for this modified finite population. Table E2 lists a summarized set of loadings and weights for this finite population. To avoid crowding, and since the patterns observec here repeat themselves across latent variables and indicators, this summarized set focuses on communication flow orientation (CO, F ) and its respective indicators CO1, CO2, …, CO5. The FIML method does not generate estimates of weights, which is why they are not listed.

TABLE E1 Path coefficients and full collinearity VIFs for finite population (N = 10 000)

<table><tr><td rowspan="2" colspan="2">True</td><td colspan="2">PLSF</td><td colspan="2">FIML</td><td colspan="2">OLS</td><td colspan="2">PLS</td></tr><tr><td>Est.</td><td>Diff.</td><td>Est.</td><td>Diff.</td><td>Est.</td><td>Diff.</td><td>Est.</td><td>Diff.</td></tr><tr><td colspan="10">Path coefficients</td></tr><tr><td>CO &gt; EU</td><td>0.4223</td><td>0.4216</td><td>-0.0007</td><td>0.4143</td><td>-0.0081</td><td>0.3461</td><td>-0.0762</td><td>0.3463</td><td>-0.0760</td></tr><tr><td>CO &gt; GT</td><td>0.5074</td><td>0.5013</td><td>-0.0061</td><td>0.4979</td><td>-0.0095</td><td>0.4014</td><td>-0.1060</td><td>0.4156</td><td>-0.0917</td></tr><tr><td>CO &gt; AC</td><td>0.2947</td><td>0.3001</td><td>0.0054</td><td>0.2948</td><td>0.0001</td><td>0.2295</td><td>-0.0652</td><td>0.2311</td><td>-0.0635</td></tr><tr><td>CO &gt; SU</td><td>0.0146</td><td>0.0130</td><td>-0.0016</td><td>0.0206</td><td>0.0060</td><td>0.0684</td><td>0.0538</td><td>0.0679</td><td>0.0533</td></tr><tr><td>EU &gt; SU</td><td>0.1466</td><td>0.1461</td><td>-0.0005</td><td>0.1485</td><td>0.0019</td><td>0.1270</td><td>-0.0196</td><td>0.1325</td><td>-0.0141</td></tr><tr><td>GT &gt; SU</td><td>0.5356</td><td>0.5342</td><td>-0.0014</td><td>0.5262</td><td>-0.0094</td><td>0.4066</td><td>-0.1290</td><td>0.4091</td><td>-0.1265</td></tr><tr><td>AC &gt; SU</td><td>0.2562</td><td>0.2566</td><td>0.0004</td><td>0.2623</td><td>0.0061</td><td>0.2122</td><td>-0.0440</td><td>0.2073</td><td>-0.0489</td></tr><tr><td>RMSE</td><td></td><td>0.0032</td><td></td><td>0.0068</td><td></td><td>0.0785</td><td></td><td>0.0753</td><td></td></tr><tr><td colspan="10">Full collinearity VIFs</td></tr><tr><td>CO</td><td>1.6618</td><td>1.6616</td><td>-0.0002</td><td>1.8146</td><td>0.1529</td><td>1.3802</td><td>-0.2815</td><td>1.3884</td><td>-0.2734</td></tr><tr><td>EU</td><td>1.2575</td><td>1.2549</td><td>-0.0026</td><td>1.3267</td><td>0.0692</td><td>1.1674</td><td>-0.0901</td><td>1.1691</td><td>-0.0884</td></tr><tr><td>GT</td><td>1.8865</td><td>1.8837</td><td>-0.0028</td><td>2.4026</td><td>0.5161</td><td>1.4454</td><td>-0.4411</td><td>1.4560</td><td>-0.4305</td></tr><tr><td>AC</td><td>1.2186</td><td>1.2132</td><td>-0.0054</td><td>1.3684</td><td>0.1498</td><td>1.1216</td><td>-0.0970</td><td>1.1238</td><td>-0.0948</td></tr><tr><td>SU</td><td>1.8813</td><td>1.8877</td><td>0.0064</td><td>2.5220</td><td>0.6407</td><td>1.4547</td><td>-0.4267</td><td>1.4649</td><td>-0.4164</td></tr><tr><td>RMSE</td><td></td><td>0.0041</td><td></td><td>0.3814</td><td></td><td>0.3077</td><td></td><td>0.3001</td><td></td></tr></table>

Abbreviations: FIML, full‐information maximum likelihood; OLS, ordinary least squares; PLS, partial least squares; VIF, variance inflation factor.

TABLE E2 Summarized loadings and weights for finite population (N = 10 000)

<table><tr><td rowspan="2">True</td><td></td><td colspan="2">PLSF</td><td colspan="2">FIML</td><td colspan="2">OLS</td><td colspan="2">PLS</td></tr><tr><td></td><td>Est.</td><td>Diff.</td><td>Est.</td><td>Diff.</td><td>Est.</td><td>Diff.</td><td>Est.</td><td>Diff.</td></tr><tr><td colspan="10">Loadings</td></tr><tr><td>CO1 &lt; CO</td><td>0.7540</td><td>0.7573</td><td>0.0032</td><td>0.7497</td><td>-0.0043</td><td>0.7871</td><td>0.0331</td><td>0.8062</td><td>0.0522</td></tr><tr><td>CO2 &lt; CO</td><td>0.6981</td><td>0.7020</td><td>0.0039</td><td>0.6931</td><td>-0.0050</td><td>0.7603</td><td>0.0622</td><td>0.7749</td><td>0.0768</td></tr><tr><td>CO3 &lt; CO</td><td>0.6552</td><td>0.6563</td><td>0.0012</td><td>0.6531</td><td>-0.0021</td><td>0.7356</td><td>0.0804</td><td>0.7376</td><td>0.0824</td></tr><tr><td>CO4 &lt; CO</td><td>0.5959</td><td>0.5913</td><td>-0.0046</td><td>0.5899</td><td>-0.0060</td><td>0.7076</td><td>0.1117</td><td>0.6939</td><td>0.0979</td></tr><tr><td>CO5 &lt; CO</td><td>0.5455</td><td>0.5442</td><td>-0.0014</td><td>0.5485</td><td>0.0029</td><td>0.6783</td><td>0.1328</td><td>0.6507</td><td>0.1051</td></tr><tr><td>RMSE</td><td></td><td>0.0032</td><td></td><td>0.0043</td><td></td><td>0.0911</td><td></td><td>0.0849</td><td></td></tr><tr><td colspan="10">Weights</td></tr><tr><td>CO1 &lt; CO</td><td>0.3512</td><td>0.3502</td><td>-0.0010</td><td>...</td><td>...</td><td>0.2730</td><td>-0.0783</td><td>0.3095</td><td>-0.0417</td></tr><tr><td>CO2 &lt; CO</td><td>0.2728</td><td>0.2752</td><td>0.0023</td><td>...</td><td>...</td><td>0.2730</td><td>0.0001</td><td>0.2967</td><td>0.0238</td></tr><tr><td>CO3 &lt; CO</td><td>0.2320</td><td>0.2280</td><td>-0.0039</td><td>...</td><td>...</td><td>0.2730</td><td>0.0410</td><td>0.2698</td><td>0.0378</td></tr><tr><td>CO4 &lt; CO</td><td>0.1800</td><td>0.1822</td><td>0.0022</td><td>...</td><td>...</td><td>0.2730</td><td>0.0929</td><td>0.2473</td><td>0.0672</td></tr><tr><td>CO5 &lt; CO</td><td>0.1527</td><td>0.1540</td><td>0.0013</td><td>...</td><td>...</td><td>0.2728</td><td>0.1201</td><td>0.2286</td><td>0.0759</td></tr><tr><td>RMSE</td><td></td><td>0.0024</td><td></td><td></td><td>...</td><td>0.0786</td><td></td><td></td><td>0.0529</td></tr></table>

Abbreviations: FIML, full‐information maximum likelihood; OLS, ordinary least squares; PLS, partial least squares; VIF, variance inflation factor.

In each table, the column labelled “True” lists the true values in our finite population of various parameters. The “Est.” columns list the corresponding estimates employing each method. The “Diff.” columns list the differences between estimates and true values for each method. The row labelled “RMSE” lists root‐mean‐square errors associ ated with the differences between estimates, calculated as the square roots of the averages of the squared differ ences, which provide a summarized performance measure for each of the methods.

Figure E1 highlights the differences (RMSEs) with respect to true values for each of the methods.

As can be inferred from the results summarized above, the performances of PLSF and FIML were similar in terms of estimation of path coefficients, and significantly better in that respect than OLS and PLS. In terms of full collinearity VIFs, the PLSF method performed significantly better than the other three methods, with the performance of FIML being the poorest.

The performances of PLSF and FIML were similar in terms of loadings, and significantly better in that respect than OLS and PLS. The same pattern was observed with respect to weights for the PLSF method, when this metho was compared with the OLS and PLS methods. As previously noted, the FIML method does not generate weights.

![](/api/attachments/NTW5UZWR/fulltext/images/c7d05065262e230562fb39cfe207e1f73ad1c7df08eebea35f97f4316698ab99.jpg)

![](/api/attachments/NTW5UZWR/fulltext/images/a9e132e75f62ac8700219cf5140ffb4eeaabbe1e71f8c132eddb2bc9cb369f15.jpg)

![](/api/attachments/NTW5UZWR/fulltext/images/300220d63edd891cf0276475db9df837aabb7c6285125278dba09ba62b826077.jpg)

![](/api/attachments/NTW5UZWR/fulltext/images/adb260e411cf24dc7e187fe1ffc970ad17e574c8f5c239afb13cd13d0a9bb9b2.jpg)  
FIGURE E1 Differences (RMSEs) with respect to true values [Colour figure can be viewed at wileyonlinelibrary. com]
