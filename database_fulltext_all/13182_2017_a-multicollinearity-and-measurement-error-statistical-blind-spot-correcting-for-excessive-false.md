---
otero_id: 13182
otero_key: "ZMPN82TN"
title: "A MULTICOLLINEARITY AND MEASUREMENT ERROR STATISTICAL BLIND SPOT: CORRECTING FOR EXCESSIVE FALSE POSITIVES IN REGRESSION AND PLS"
authors: "Dale L. Goodhue; William Lewis; Ron Thompson"
year: "2017"
journal: "MIS Quarterly"
doi: "10.25300/misq/2017/41.3.01"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A MULTICOLLINEARITY AND MEASUREMENT ERROR STATISTICAL BLIND SPOT: CORRECTING FOR EXCESSIVE FALSE POSITIVES IN REGRESSION AND PLS<sup>1</sup>

Dale L. Goodhue Terry College of Business, MIS Department, University of Georgia, Athens, GA 30606 U.S.A. {dgoodhue@terry.uga.edu}

William Lewis {william.w.lewis@gmail.com}

Ron Thompson School of Business, Wake Forest University, Winston-Salem, NC 27109 U.S.A. {thompsrl@wfu.edu}

Multiple regression has a previously unrecognized “statistical blind spot” because when multicollnearity and measurement error are present, both path estimates and variance inflation factors are biased. This can result in overestimated t-statistics, and excessive false positives. PLS has the same weakness, but CB-SEM’s estima tion process accounts for measurement error, avoiding the problem. Bringing together partial insights from a range of disciplines to provide a more comprehensive treatment of the problem, we derive equations showing false positives will increase with greater multicollinearity, lower reliability, greater effect size in the dominant correlated construct, and, surprisingly, with higher sample size. Using Monte Carlo simulations, we show that false positives increase as predicted. We also provide a correction for the problem. A literature search found that of IS research papers using regression or PLS for path analysis, 33% were operating in this danger zone. Our findings are important not only for IS, but for all fields using regression or PLS in path analysis

Keywords: Multicollinearity, measurement error, M+ME, multiple regression, partial least squares, PLS, CB-SEM, false positives, Type I error, statistical power, variance inflation factor, VIF, path estimate bias

## Introduction

False positives (Type I errors) are an important concern in behavioral research. By generally setting our hurdle for statistical significance at p < .05, we seek to protect against more than 5% false positives in hypothesis testing. In this paper, we start with a curious inconsistency between papers from two groups of researchers (Reinartz et al. 2009 and Goodhue et al. 2006, 2012) reporting on the statistical power of partial least squares (PLS) and covariance-based structural equation modeling (CB-SEM).<sup>2</sup> In trying to reconcile the inconsistent findings, we exposed a previously unrecognized blind spot in both regression<sup>3</sup> and PLS, that may allow as high as 15% or even 20% false positives<sup>4</sup> under certain (not atypical) conditions of correlated predictor constructs and random measurement error. We found that 33% of the Information Systems (IS) research papers using regression or PLS in three top journals from 2010–2015 were operating in this multicollinearity and measurement error (M+ME) danger area. We suspect that published research in many other research domains is also subject to this blind spot.

<table><tr><td colspan="3">Table 1. Prior Research Bearing On M+ME</td></tr><tr><td></td><td>Research Domain</td><td>Comments</td></tr><tr><td>Johnston 1972</td><td>Econometrics</td><td>A classic econometrics resource. Erroneously assumes VIF will adjust sufficiently to prevent excessive false positives in regression.</td></tr><tr><td>Fuller 1987</td><td>Statistics</td><td>Recognizes the possibility of false positives in regression, but his comments are an aside about false positives with instrumental variables. Does not recognize the more general danger.</td></tr><tr><td>Green and Kiernan 1989</td><td>Financial Econometrics</td><td>Provides equations that can be transformed to show the impact of multicollinearity and measurement error on path bias in regression. Does not consider statistical significance.</td></tr><tr><td>Mason and Perreault 1991</td><td>Marketing</td><td>Focuses on Type II errors in regression. Does not include measurement error and does not consider possibility of excessive false positives.</td></tr><tr><td>Zidek et al. 1996</td><td>Environmetrics</td><td>Cites Fuller 1987, and recognizes the more general danger of false positives in regression, but equations do not expose the critical mechanisms. Erroneously concludes that the problem disappears when the predictor with a false positive is measured with error. Does not propose a solution.</td></tr><tr><td>Grewal et al. 2004</td><td>Marketing</td><td>Considers CB-SEM only. Focuses on Type II errors. Does not consider possibility of Type I errors.</td></tr><tr><td>Freckleton 2011</td><td>Sociobiology</td><td>Recognizes the danger of M+ME in regression but erroneously concludes that the problem disappears when the predictor measured with error has zero effect, so there should be no problem of false positives.</td></tr><tr><td>Current Article</td><td>Information Systems</td><td>Drawing from previous studies, provides equations that expose the mechanisms by which M+ME leads to false positives. Hypotheses are tested with simulations. Proposes a straightforward solution.</td></tr></table>

The path of discovery included the following steps. First, faced with inconsistencies between the researchers mentioned above, we used Monte Carlo simulation to establish the “fact” that regression and PLS created excessive false positives under certain circumstances of M+ME. Second, by going back to past literature, we were able to draw from published work that looked at the impact of M+ME in six different research domains, as shown in Table 1. Each of these works provided some insights into the M+ME phenomenon, but none put all the pieces together and none proposed an effective solution for the excessive false positives problem. The variety of disciplines mentioned suggests that this topic has wide relevance.

By drawing upon those articles, and by transforming their equations to highlight the role of M+ME in creating false positives, we were able to identify the factors causing excessive false positives. With our Monte Carlo simulations, we were able to test and verify the factors exposed in our transformed equations. These transformed equations also allowed us to develop a way to correct the bias created by M+ME and remove the false positives. In short, we were able to draw from a variety of isolated insights on M+ME in diverse fields and present a more complete and verified picture of a statistical blind spot in analysis with regression (and PLS).

Researchers have long accepted the following: (1) multicollinearity (correlated predictor constructs) can bias regression path estimates (Johnston 1972), (2) the variance inflation factor (VIF) (based on the correlation between predictor constructs) protects against excessive false positives due to that bias by increasing the standard deviations of path estimates (Johnston 1972; Neter and Wasserman 1974; Pedhazur 1997), and (3) in regression, random measurement error attenuates estimates of correlations between constructs (Nunnally and Bernstein 1994). We found no evidence that researchers have put these ideas together to realize that because the regression VIF is based on the estimated correlation between two constructs, it is underestimated in the presence of random measurement error. In addition, we found that the regression path estimate bias may increase beyond the ability of even the corrected VIF to counterbalance it.

The result is that when there is random measurement error combined with multicollinearity in regression, small or zero effect size paths can be overestimated and variance inflation factors underestimated. Thus t-statistics for path estimates can be overestimated, and excessive false positives are possible. Our simulation results suggest that this overestimation can result in a statistically significant increase of false positives when the sample size (N) is around 100, the calculated correlations between measures of predictor constructs are around .50, and the reliability of the set of reflective items measuring the constructs is around .80. The problem is exacerbated as the correlation between predictor constructs increases, the strength of the dominant correlated predictor increases, reliabilities decrease, or (somewhat surprisingly) as sample size increases. Our evidence also shows that PLS has the same tendency to false positives as regression, and that this tendency is exacerbated under the same conditions.

This paper makes two significant contributions. First and foremost, it shows (mathematically and with Monte Carlo simulations) that under certain conditions of M+ME, regression and PLS can create excessive false positives. These effects occur even when construct scale measures display acceptable discriminant validity, and when variance inflation factors are well within accepted norms. We show how to correct for this condition in most of the situations that researchers will encounter.

Second, this paper contributes in a small way to the ongoing dialog about when it is appropriate to use PLS, regression, or CB-SEM.<sup>5</sup> Our goal is not to weigh in directly on that dialog.<sup>6</sup> Indirectly, however, our results do suggest that the

Reinartz et al. (2009) assertion that PLS has greater statistical power than CB-SEM is incorrect. Along with the research community in general, Reinartz et al. were unaware of the potential impact of M+ME and thus did not take it into account. Understandably, they interpreted their results as evidence that PLS has higher statistical power than CB-SEM with samples sizes around 100. Our results suggest that the apparent power advantage of PLS in Reinartz et al. is entirely due to M+ME bias.

To define the scope of our work in this paper, we note several boundary conditions: (1) an analysis is testing causal path models, (2) latent constructs are measured with multiple reflective indicators consistent with the common factor model of measurement error (in PLS software packages these are typically modeled using PLS “Mode A”), and (3) measurement errors are random and uncorrelated.<sup>7</sup>

With respect to terminology, we use the term overt correlation to refer to the calculated correlation observed by a researcher using regression or PLS, which may be attenuated by measurement error. We distinguish this from the underlying correlation that exists between the underlying constructs, or an overt correlation that has been corrected for any random measurement error. We use the term reliability to refer to the internal consistency of a set of reflective items designed to measure a latent construct (or more precisely the variance of the true—or underlying—score divided by the variance of the measure). In describing the reliability of the measures in this paper, we are referring to Cronbach’s alpha (Cronbach 1951).

In the next section of the paper we describe our investigation of the conflicting results of Reinartz et al. (2009) versus Goodhue et al. (2006, 2012), and the results that led us to suspect that the M+ME phenomenon first described by Goodhue et al. (2011) might provide an explanation. In the subsequent section (and in Appendices A and B), we review the results from Johnston (1972), Green and Kiernan (1989), and Goodhue et al. (2011) and then extend the argument to show mathematically how correlated predictor constructs combined with random measurement error can lead to overestimated t-statistics for path estimates, first for regression and then for PLS. This leads to a set of hypotheses for when excessive false positives are likely in regression, PLS, and CB-SEM.

The fourth section tests those hypotheses with a series of Monte Carlo simulations. All of our hypothesis testing supports our contentions about M+ME.<sup>8</sup> Finally, in the last section of the paper, we discuss the implications of our findings for researchers using regression, PLS, and CB-SEM. Based on a literature review we show the extent to which the M+ME phenomenon might be affecting findings in published IS research. We then suggest how a researcher might recognize when he or she is in the M+ME danger zone, and how to correct results for M+ME under most conditions.

## Investigating the Puzzle of Two Radically Different Conclusions About PLS Versus CB-SEM Statistical Power

As users of all three statistical techniques (PLS, regression, and CB-SEM) in our research, we were quite interested in the radically different conclusions regarding the statistical power of PLS and CB-SEM arrived at by three simulation studies: Reinartz et al. (2009) and Goodhue et al. (2006, 2012). Although all three studies concluded that CB-SEM resulted in more accurate path estimates, they found quite different results when comparing the statistical power of PLS and CB-SEM. Reinartz et al. concluded that “the statistical power of PLS is always larger or equal to that of CBSEM” (p. 340). In the case of sample sizes of N = 100 and a medium effect size, Reinartz et al. showed PLS’s statistical power clearly dominating CB-SEM (85% versus 51%). In contrast, Goodhue et al. (2006, 2012) found that for sample sizes of 90 to 200, all three techniques had virtually the same statistical power for strong, medium, and small effect sizes. When there was a small difference, it favored CB-SEM.

Seeking to resolve this dilemma, we carried out a partial replication of the studies, obtaining essentially the same results as the original studies. We will focus below on the Reinartz et al. model (shown in Figure 1), since it is the only study of the three where the focal model included multicollinearity. We generated 500 different datasets based on Reinartz et al.’s condition of four indicators for each construct, indicator loadings of .70 each, and sample size of N = 100. This is the condition that for Reinartz et al. showed the largest apparent power advantage of PLS over CB-SEM. We then analyzed all 500 datasets with regression, PLS, and CB-SEM. Because the single medium-effect-size path (β in Figure 1) is the only path for which Reinartz et al. reported path-specific results, we focus only on that β path and its statistical significance.

The results from Reinartz et al. and from our partial replication of it are shown in the first two rows of Table 2. As can be seen, while Reinartz et al.’s published results (row 1) and our replication of Reinartz et al.’s analysis (row 2) are not identical,<sup>9</sup> they certainly exhibit the same pattern. Both seem to show that PLS has a conspicuous and statistically significant advantage<sup>10</sup> over CB-SEM in terms of statistical power.

One difference between the Reinartz et al. analysis and our replication was that we included regression in addition to PLS and CB-SEM. In fact, including regression produced an interesting clue for our exploration. Since our PLS and regression results were almost identical, we inferred that either something was affecting both PLS and regression but not CB-SEM, or it was affecting only CB-SEM and neither PLS nor regression. Goodhue et al. (2011) showed that with OLS regression, multicollinearity combined with measurement error can lead to underestimated variance inflation factors and false positives. Since both of those conditions were present in the Reinartz et al. model, we suspected that might be the explanation. We tested that possibility by changing the value of the β<sub>3</sub> path from .30 to zero so that any statistically significant β<sub>3</sub> paths detected would clearly be false positives (Type I errors). We then used this new model and generated and tested 500 new datasets.<sup>11</sup>

<sup>9</sup>Possible explanations for differences include different approaches to generating random numbers, different initial random number seeds, different approaches toward rounding, and how many significant digits to carry forward. The essential patterns of the two sets of results are consistent with each other, however.

<sup>10</sup>With proportions based on 500 samples, the 95% confidence interval around the PLS values of 85% and 78% is plus or minus 3 and 4%, respectively. The CB-SEM values of 51% (for Reinartz et al.) and 54% (for our replication) are both outside the confidence intervals around the PLS values.

![](/api/attachments/ZMPN82TN/fulltext/images/31c9a668e4f62bd6bd766b13f986019f0d3490d5e56dd7627188b2d1e22c0451.jpg)  
Figure 1. Model Used by Reinartz et al. (2009)

Table 2. Comparing Statistical Power Results from Reinartz et al. and a Replication\*

<table><tr><td>Study</td><td>Effect Size for  $\beta_3$ </td><td>PLS Power for  $\beta_3$ </td><td>CB-SEM Power for  $\beta_3$ </td><td>Regression Power for  $\beta_3$ </td><td>Interpretation</td></tr><tr><td>Reinartz et al.  $\beta_3 = .30$ </td><td>0.14</td><td>85%</td><td>51%</td><td>NA</td><td>Large difference favoring PLS</td></tr><tr><td>Our Replication,  $\beta_3 = .30$ </td><td>0.14</td><td>78%</td><td>54%</td><td>78%</td><td>Large difference favoring PLS and Regression</td></tr><tr><td>Our Replication,  $\beta_3 = .00$ </td><td>Zero</td><td>9.8%</td><td>6.4%</td><td>9.4%</td><td>Excessive False Positives for PLS and Regression</td></tr></table>

\*Also shown is our replication with $\beta _ { 3 }$ = zero to detect false positives. For all, sample size is N = 100, and all constructs are measured with four indicators each with loadings of .7, resulting in a reliability of .79.

Those new results are shown in the third row of Table 2. The 95% confidence interval (around the allowable 5% of false positives for a zero path) extends from 3.1 to 6.9%. The proportions of the 500 datasets where the β path estimate was statistically significant, for both PLS (9.8%) and regression (9.4%), are well outside of that confidence interval, while the proportion for CB-SEM (6.4%) was within it.

We label this situation of false positives from multicollinearity plus random measurement error the M+ME blind spot. It appears that under these circumstances, regression and PLS can overestimate the t-statistics and create excessive false positives. We next look at the three different path estimation techniques and consider the question of why M+ME produces (or does not produce) excessive false positives for each of the three.

## Regression: M+ME and False Positives

## Johnston’s Equations for Path Estimate Bias and VIFs in Regression

(Please see Appendix A for more detail on the material in this section.) Johnston (1972, pp. 161-163) showed that when predictor constructs are correlated in a regression, path values can be biased. He also noted that as the correlation increases, the VIF increases, and along with it the standard deviation of the path estimate. After discussing possible dangers of multicollinearity, Johnston (and authors of other statistics books generally, e.g., Neter and Wasserman 1974; Pedhazur 1997) conclude that except under extreme circumstances, if two predictor constructs are correlated, the VIF will increase the calculated standard errors sufficiently to prevent false positives. As Johnston (1972, p. 163) says,

Thus there is no reason why collinearity should seriously bias the estimate of $\sigma _ { \mathrm { u } 2 }$ and so we expect the standard errors to give adequate warning of collinearity. The effect of an explanatory variable may be sufficiently strong for the estimated coefficient to be statistically different from zero in spite of the effect of collinearity in increasing the standard error, but such collinearity may obscure the presence of less strong effects.

In other words, Johnston suggests that false negatives might be a problem, but false positives should not be. Only when VIFs increase to high values<sup>12</sup> is caution urged. Goodhue et al. (2011) challenged that assertion, noting that when the construct scores are calculated using weighted sums of indicators (as they typically are in regression and PLS analysis), calculated correlations between those constructs are attenuated by measurement error, or biased downward, as shown in the following equation from Nunnally and Bernstein<sup>13</sup> (1994, pp. 241, 257). Below, $\alpha _ { 1 }$ and ${ \bf Q } _ { 2 }$ are the reliabilities of the two correlated predictors, and ${ \rho } _ { 1 2 }$ is the overt or the underlying correlation.

$$
\rho_ {1 2 \text {Overt}} = \rho_ {1 2 \text {Underlying}} * (\alpha_ {1} * \alpha_ {2}) ^ {1 / 2}\tag{1}
$$

and therefore

$$
\rho_ {1 2 \text { Underlying }} = \rho_ {1 2 \text { Overt }} / (\alpha_ {1} * \alpha_ {2}) ^ {1 / 2}\tag{2}
$$

Since these attenuated overt correlations are the only information available to a regression analysis, regression variance inflation factors based on those attenuated correlations are also biased downward. The M+ME blind spot becomes apparent when we look at the equation for the variance of a regression path estimate together with equation 2. Note that the correct VIF is equal to $1 / ( 1 { \cdot } [ \rho _ { 1 2 \mathrm { u n d e r l y i n g } } ] ^ { 2 } )$

$$
\operatorname{Var} \left(\beta_ {2} ^ {\wedge}\right) _ {\text { incorrect }} = \left[ s ^ {2} / \Sigma x _ {2 t} ^ {2} \right] * \left\{1 / \left(1 - \left[ \rho_ {1 2 o v e r t} \right] ^ {2}\right) \right\} \quad (\text { incorrect })\tag{3}
$$

$$
\operatorname{Var} \left(\beta_ {2} ^ {\wedge}\right) _ {\text { Correct }} = \left[ s ^ {2} / \Sigma x _ {2 t} ^ {2} \right] * \left\{1 / \left(1 - \left[ \rho_ {1 2 o v e r t} / \left(\alpha_ {1} * \alpha_ {2}\right) ^ {. 5} \right] ^ {2}\right) \right\} \tag {correct}
$$

This means that as the reliabilities of $\mathrm { X } _ { 1 }$ and $\mathrm { X } _ { 2 } ( \mathbf { \alpha } _ { 1 }$ and ${ \mathfrak { X } } _ { 2 }$ in our equations)<sup>.</sup>decrease from 1, the overt $\rho _ { 1 2 }$ correlation that regression uses in its calculation of the VIF will decrease from the correct underlying value. Therefore VIF will be underestimated, Var(β<sup>^</sup>) will be underestimated, path standard deviations will be underestimated, and t-statistics overestimated. Under these circumstances we clearly run the risk of excessive false positives.

To the best of our knowledge, Goodhue et al. (2011) were the first to recognize the potential of M+ME to bias the variance inflation factor in regression, and thus contribute to excessive Type I errors for path estimates. In Appendix A, we go beyond the work done by Goodhue et al. (2011) and derive the following equation for how bias in the VIF will affect the value of the “square of the t-statistic” for a given path estimate as shown below:<sup>14</sup>

$$
\begin{array}{l} \left(\beta_ {2} ^ {\wedge} \text {t - stat}\right) ^ {2} \text {overestimation} = \\ \left[ \left(1 / \left(\alpha_ {1} * \alpha_ {2}\right)\right) - 1 \right] * \left[ \left(\beta_ {2} ^ {\wedge} - \beta_ {2}\right) ^ {2} (\mathrm{N} - \mathrm{K}) \Sigma x _ {2 i} ^ {2} \left(\rho_ {1 2 - \text {Overt}} ^ {2}\right) \right] / \Sigma \varepsilon_ {i} ^ {2} \\ \text {(Equation A1 - 10 from Appendix A)} (5) \end{array}
$$

Note that equation 5 shows several important aspects of the M+ME phenomenon. Without random measurement error (that is, when $\mathbf { Q } _ { 1 }$ and $\alpha _ { 2 } = 1 . 0 0 )$ , the first term will be zero and there will be no overestimation. The second square-bracketed term in equation (5) contains the impact of the overt correlation between predictor constructs. If the overt correlation between predictor variables ${ ( \mathsf { p } _ { 1 2 0 \mathrm { v e r t } } } ^ { 2 } )$ is zero, the second term will be zero and there will be no overestimation. Finally, the (t-statistic)<sup>2</sup> overestimation will increase approximately proportionally with the sample size. If N-K doubles (N is sample size and K is the number of predictors in the regression), the overestimation in the square of the t-statistic will double.

## Green and Kiernan’s Equations for Path Estimate Bias in Regression

Johnston (as noted above) had shown that multicollinearity could produce bias in regression path estimates. Green and Kiernan (1989) carried the analysis of regression path estimate bias further than Johnston. In particular, Green and Kiernan made a distinction between what we are calling the overt correlation $\left( \rho _ { 1 2 \mathrm { { O v e r t } } } \right)$ and the underlying correlation $( \rho _ { 1 2 \mathrm { U n d e r l y i n g } } ) .$ . The overt correlation is the correlation based on the “signal-plus-noise” or the correlation between the “error containing” measures of the two constructs, while the underlying correlation is the correlation based only on the “signal.” Green and Kiernan (p. 360) developed explicit equations<sup>15</sup> for the “proportional inconsistency” or $\mathrm { { ^ { < } P I ^ { \circ } } }$ of regression path estimates.

$$
\begin{array}{l l} \mathrm{PI} _ {\beta 1} = & (\beta_ {1} - \operatorname{plim} \beta_ {1} ^ {\wedge}) / \beta_ {1} = \\ & [ (1 - \alpha_ {1}) / (1 - \rho_ {1 2} ^ {2}) ] * [ 1 - (\rho_ {1 2} * (\beta_ {2} / \beta_ {1})) ] \end{array}\tag{6}
$$

$$
\begin{array}{l l} \mathrm{PI} _ {\beta 2} = & (\beta_ {2} - \operatorname{plim} \beta_ {2} ^ {\wedge}) / \beta_ {2} = \\ & [ (1 - \alpha_ {1}) / (1 - \rho_ {1 2} ^ {2}) ] * [ 1 - (\rho_ {1 2} * (\beta_ {1} / \beta_ {2})) ] \end{array}\tag{7}
$$

Here $\beta _ { \mathrm { i } }$ is the underlying path value, and $\beta _ { \mathrm { i } } ^ { \wedge }$ is the overt path estimate. The $\rho _ { 1 2 }$ is the overt correlation between $\mathrm { X } _ { 1 }$ and $\mathrm { X } _ { 2 } ,$ and $\alpha _ { 1 }$ is the reliability of $\mathrm { X } _ { 1 }$ and of $\mathrm { X } _ { 2 }$ (assumed to be equal<sup>16</sup>). The “plim” in front of the $\beta _ { \mathrm { i } } ^ { \wedge }$ terms indicates the equation is strictly true only when an infinite sample size is used.<sup>17</sup> These equations show that the bias (or the proportional inconsistency) increases with lower reliability, with higher correlation between constructs, and with the ratio of the path values of the correlated constructs. Note that if the correlation between predictor constructs is zero, Green and Kiernan’s equations reduce the path bias to that caused by measurement error attenuation. If the reliability is $1 . 0 ,$ the equations reduce the path bias to that correctable by the wellknown VIF adjustment to the path standard deviation.

Green and Kiernan were not concerned with the impact of their findings on statistical significance. They were focused on more substantive issues in financial econometrics. Nevertheless, their equations are valuable to us in understanding the impact of M+ME. In particular, their equations show that with two positively correlated constructs, each with positive paths to a third construct, M+ME will always cause the dominant path to be underestimated and (unless the nondominant path is close to the value of the dominant path) the nondominant path will be overestimated. This last can contribute to excessive false positives.

Our analysis of the M+ME problem leads us to the following hypotheses for regression analysis when the underlying model is otherwise held constant (the “R” denotes regression):

Hypothesis #1-R: When there is sufficiently large multicollinearity and also random measurement error, regression will result in overestimated t-statistics for paths with zero effect, resulting in the occurrence of excessive false positives for those paths.

Hypothesis #2-R: For regression, the proportion of false positives for paths with zero effect will increase with each of the following:

2a-R increasing correlation between predictor constructs,

2b-R increasing random measurement error, and 2c-R increasing sample size.

Focusing on the causes of the above, we also hypothesize the following:

Hypothesis #3-R: For regression with measurement error:

3a-R The path standard deviations estimated by regression will increase only by the amount of the overt VIF, not by the amount of the underlying VIF.

Finally, based on the Green and Kiernan equations:

3b-R Assuming $\beta _ { 1 }$ and $\rho _ { 1 2 }$ are both positive, $\beta _ { 2 } = 0$ and $\beta _ { 1 }$ and $\beta _ { 2 }$ are both measured with error, the average regression path estimates for $\beta _ { 2 }$ will be about zero when there is no underlying correlation between predictor constructs, but will increase as the underlying correlations increase.

## PLS: M+ME and False Positives

PLS is another frequently used statistical analysis technique in IS research. One might believe that because PLS users typically employ bootstrapping<sup>18</sup> instead of the regression equations to estimate path variances (and therefore PLS does not use the variance inflation factor), PLS should not be subject to the biases in statistical significance visible in the regression equations for Var(β<sup>^</sup><sub>2</sub>) discussed earlier. However, the empirical evidence (in Goodhue et al. 2011 and in our reanalysis of the Reinartz et al. 2009 model) suggests that regression and PLS share the same behavior in the presence of M+ME.

Both regression and PLS can be thought of as having three steps:<sup>19</sup> (1) determining the weights for the construct indicators and calculating proxy scores for the constructs in the model, (2) using those proxy construct scores in ordinary least squares regression to calculate path estimates, and (3) determining the statistical significance of the path estimates. In regression, step one is typically taken care of very simply: equal weights are given to all indicators. In contrast, PLS iterates through a process to find a set of supposedly better indicator weights for each construct.

We do not suggest the M+ME problem has any impact on either regression’s or PLS’s determination of the indicator weights. It is in the second step, where both regression and PLS literally do the same thing, that the M+ME problem has an impact. For each endogenous construct, both techniques use ordinary least squares regression to analyze the construct scores developed in step one, and thus estimate the strength of hypothesized paths between constructs. In this ordinary least squares step, both regression and PLS will create biased estimates as suggested by Green and Kiernan’s equations.

In the third step, regression and PLS utilize quite different approaches. Regression calculates standard deviations utilizing normal distribution theory. In PLS, bootstrapping creates hundreds (or thousands) of new datasets by taking repeated random samples (with replacement) from the original data points, reanalyzes each new dataset, and in this way generates hundreds (or thousands) of new estimates for each path. The variation in the path estimates of these bootstrapping samples is presumed to reflect the variation in the population as a whole. Bootstrapping uses this variation to draw conclusions about the appropriate standard deviation value for each estimated path.

In Appendix B, we present a conceptual argument for why bootstrapping will not protect PLS against excessive false positives. Rather, each of the bootstrapping path estimates seen by PLS will be biased by about the same amount as the original PLS estimate. Therefore the path variance seen by bootstrapping in PLS will be about the same as the path variance seen by regression, and no larger than that seen by regression. Based on the above, we hypothesize the following (the “P” refers to PLS):

Hypothesis #1-P: When there is sufficiently large multicollinearity and also random measurement error, PLS will result in overestimated t-statistics for paths with zero effect, which will be apparent in the occurrence of excessive false positives for those paths.

Hypothesis #2-P: For PLS, the proportion of false positives for paths with zero effect will increase with each of the following:

2a-P increasing correlation between predictor constructs,

2b-P increasing random measurement error, and 2c-P increasing sample size.

Focusing on the question of how PLS’s bootstrapping responds to M+ME (specifically our assertion that its bootstrapping estimates for the path standard deviation and its path estimates do not correct for M+ME and are therefore about the same as seen for regression), we also hypothesize:

Hypothesis #3-P: For PLS, as multicollinearity increases:

3a-P The path standard deviations estimated by PLS will increase only by the amount of the “overt” VIF, not by the amount of the “underlying” VIF.

3b-P Assuming $\beta _ { 1 }$ and $\rho _ { 1 2 }$ are both positive, $\beta _ { 2 } = 0$ and $\beta _ { 1 }$ and $\beta _ { 2 }$ are both measured with error, the average PLS path estimates for $\beta _ { 2 }$ will be about zero when there is no correlation between predictor constructs, but will increase as the underlying correlation increases.

## CB-SEM Analysis: M+ME andFalse Positives

CB-SEM analysis involves a coherent set of simultaneous equations that take into account a number of factors including indicator loadings, random measurement error, construct correlations, and path values. Therefore we would expect that path estimates will not be attenuated by random measurement error and estimated path standard deviations will be sufficiently increased to avoid excessive Type I errors. This is not to say that path estimates in CB-SEM will be stable when predictor constructs are highly correlated. As Grewal et al. (2004) showed, greater multicollinearity does increase path standard deviations and thus increases false negatives (Type II errors) in CB-SEM.<sup>20</sup>

Hypothesis #1-C: When there is multicollinearity and also random measurement error, CB-SEM will not result in overestimated t-statistics for paths with zero effect. This will be apparent in no excessive occurrence of false positives for those paths.

Hypothesis #2-C: For CB-SEM, the proportion of false positives for paths with zero effect will not exceed the confidence interval around 5%, even with:

2a-C increasing correlation between predictor constructs,

2b-C increasing random measurement error, and 2c-C increasing sample size.

## Testing the Hypotheses with Monte Carlo Simulation

Monte Carlo simulation has been used extensively to investigate a variety of statistical analysis issues (e.g., Fornell and Larcker 1981; Goodhue et al. 2007). With Monte Carlo simulation, we start with a “true” underlying base model that has known properties because we define them in advance. The first model we will use (a modification of that used by Goodhue et al. 2012) is shown in Figure 2. For our first simulation analyses, we used a sample size (N) of 100, which is a fairly common lower bound for much IS research of this type.<sup>21</sup>

As shown in Figure 2, each construct is measured by three indicators with initial loadings of .70, .76, and .82, which will give us a reliability of .80 for each of the constructs.<sup>22</sup> This reliability of .80 is equivalent to the usual recommended cutoff value for reliability in reasonably mature research streams (Carmines and Zeller 1979). In the model, X1 and X3 each have a moderate effect size<sup>23</sup> influence on Y1 (due to path values of .292). X4 has a strong effect size influence (due to a path value of .51). X2 has a zero effect on Y1. Therefore, any statistically significant value found for the X2 to Y1 path (β<sub>2</sub>) is a false positive.

For our initial analysis we tested 20 conditions: all combinations of four levels of measurement reliability (1.00, .90, .80, and .70) and five levels of correlation between X1 and X2 (0.0, .40, .60, .80, and .90). For each condition, we generated 500 datasets of 100 cases each, and analyzed each separately using regression, PLS (PLS-Graph 3.0; Chin and Frye 2003), and then CB-SEM (LISREL 8.80). After that analysis, we then determined for each statistical technique: (1) the average estimated value (across 500 datasets) for each path, and (2) the proportion of X2 to Y1 paths (out of 500) that were false positives, that is, statistically significant (p < .05). Since we are using a statistical significance level of p < .05, we would expect about 5% false positives. As we noted in footnote #11, for our 500 samples in each treatment condition, any proportion higher than 6.9% is statistically significant evidence of excessive false positives.

Figure 3 shows our results for N = 100 using regression (Panel 3A), PLS (Panel 3B), and CB-SEM (Panel 3C). The two dashed horizontal lines show the limits of the 95% confidence interval around 5% false positives. For an underlying correlation of .60 and measurement reliability of .80, the results show a statistically significant number of excessive false positives for Regression and PLS (around 8%), but not for CB-SEM. Note that with a reliability of .80, an underlying correlation of .60 will appear as an overt correlation of (.60 \* .80) or .48.

In Panels 3A and 3B, as the correlation between X1 and X2 goes up, or reliability goes down, generally the percent of false positives for Regression and PLS goes up. This is not true for CB-SEM (Panel 3C). This shows support for hypotheses 1-R, 2a-R, 2b-R for regression; hypotheses 1-P, 2a-P, 2b-P for PLS; and hypotheses 1-C, 2a-C, and 2b-C for CB-SEM.

In Figure 4 we reproduced the Figure 3 Monte Carlo simulation but this time we generated data based not just on N = 100, but also N = 200 and N = 300, all with a reliability of .80.

We again produced and analyzed 500 different datasets for each of 15 conditions, varying sample size (100, 200, and 300) and correlation between the predictor constructs (0.0, .40, .60, .80, and .90). Looking at the Panel 4A (regression), and Panel 4B (PLS) the dashed horizontal lines indicate the 95% confidence interval around 5%, the acceptable level of false positives. For both regression and PLS, there is not much impact when the underlying correlation is .40 or less, but with underlying correlations of .60 and above, the problems are apparent at N = 100, and consistent with equation 5, increase with increasing sample size.

Finally, in Panel 4C for CB-SEM, we see no excessive false positives, even with high correlations and large sample size. These results from Figure 4 show support for Hypotheses 2c-R, 2c-P, and 2c-C.

We turn to Hypothesis 3, looking at the possible underlying causes of the false positives seen in regression and PLS. At a correlation value of zero, the standard deviation (StDev) values should be unaffected by the VIF or the M+ME for both regression and PLS. Using equation 4, we can predict what the correct StDev values (using the correct variance inflation factor) should be for each level of multicollinearity as we go from zero to .4 to .6 for example. Using equation 3, we can

![](/api/attachments/ZMPN82TN/fulltext/images/a25f15dcacfd9035953a7bfddea71a60a4a4dda1516780050dc02c4af4abf8d3.jpg)  
Figure 2. Baseline Model for Monte Carlo Simulations

![](/api/attachments/ZMPN82TN/fulltext/images/45ae829202863e3d81f06385eb59d78903bf3d8ad201b8607d04b175afed06b8.jpg)  
Panel 3A. Regression: Percent of False Positives at Different Levels of $\pmb { \rho } _ { 1 2 }$

![](/api/attachments/ZMPN82TN/fulltext/images/c9580de4c52b0e7b7559aa7afdbec053c9e29bc5085126baa4a20acafac596d1.jpg)  
Panel 3B. PLS: Percent of False Positives at Different Levels of $\boldsymbol { \mathsf { p } } _ { 1 2 }$

![](/api/attachments/ZMPN82TN/fulltext/images/d912fe3f82979b7cf5421909fb023e2a6cced0a27f5f70b95a5b390668872744.jpg)  
Panel 3C. CB-SEM: Percent of False Positives at Different Levels of $\boldsymbol { \mathsf { p } } _ { 1 2 }$  
Figure 3. False Positives from Correlations and Measurement Error (for all, N = 100, β<sub>2</sub> = .292)

![](/api/attachments/ZMPN82TN/fulltext/images/cabd69468e105f6e13c136ecc178dfdcfe605fa1e96a417189b2de4bc31882dd.jpg)

Panel 4A. Regression: Percent of False Positives at Different Levels of $\pmb { \rho } _ { 1 2 }$  
![](/api/attachments/ZMPN82TN/fulltext/images/1f4552bc75ceaa58db58c89b4178afef50ecf89edba0c17c4a424b58972c6dce.jpg)

Panel 4B. PLS: Percent of False Positives at Different Levels of $\boldsymbol { \mathsf { p } } _ { 1 2 }$  
![](/api/attachments/ZMPN82TN/fulltext/images/6055a01c9455d213d04afb0fe8bc093abf3834be4adddd82cd3f9de0dacef426.jpg)

Panel 4C. CB-SEM: Percent of False Positives at Different Levels of $\boldsymbol { \mathsf { p } } _ { 1 2 }$

Figure 4. False Positives with Increased Sample Size (for all, reliability = .80, β<sub>1</sub> = .292.  
![](/api/attachments/ZMPN82TN/fulltext/images/c298dc50fd3acfe942f96d751491f4ea99e7b9f6ef11ce14a5915ce816e7b3eb.jpg)  
Figure 5. Theoretical Corrected and Uncorrected Standard Deviations for β Path and Average Standard Deviations Estimated by Regression and PLS (for all, reliability = .80, N = 100, β<sub>1</sub> = .292)

![](/api/attachments/ZMPN82TN/fulltext/images/e1a1744bc8bd2a55353ef67f3768513da7b69387c53519e4335bc2b8de327448.jpg)  
Dashed box shows when excessive false positives are apparent. $( \mathsf { N } = 1 0 0 , \mathsf { \beta } _ { 1 } = . 2 9 2 )$

Figure 6. Average Estimated Path Values for the Zero X2  Y1 Path

also predict what the biased StDev values (using the biased or uncorrected variance inflation factor) should be for each level of multicollinearity. The top two lines in Figure 5 show the theoretical corrected and uncorrected StDev values for our simulation, assuming a sample size of 100 and reliability of .80.

Based on the analysis of our 500 simulation datasets, the bottom two lines in Figure 5 show the average overt standard deviations from our simulations, computed from PLS (bootstrapping) and from regression (using normal distribution theory). As can be seen, PLS estimates for the standard deviations of the paths are quite close to those of regression (the lines overlap), and both seem to be based on the StDevs that would be seen if M+ME is ignored (the second line from the top). This is strong support for hypothesis 3a-R and 3a-P.

Figure 6 shows the impact of M+ME on the bias for the zero effect size X2  Y1 path estimate, hypotheses 3b-R and 3b-P. Clearly, as the underlying correlation increases, path estimates for the zero path increase as predicted, for both regression and PLS, but not for CB-SEM. Since the true value is zero throughout, this is strong support for hypotheses 3b-R and 3b-P. Beyond a correlation of .40, there are excessive false positives for PLS and regression.

These results suggest that M+ME has its impact through biasing both (1) calculated standard deviations and (2) path estimates, in regression and in PLS. They suggest that PLS’s bootstrapping resamples tend to be biased in the same direction and by about the same amount as regression, following Green and Kiernan’s equations. In other words, it suggests that PLS is just as susceptible to M+ME problems as regression. This is support for Hypotheses 3b-R and 3b-P.

## Additional False Positives Due to Large $\beta _ { 1 }$ Paths

Finally, although not originally hypothesized, we realized in our testing that the number of false positives increases with the size of the $\beta _ { 1 }$ path.<sup>24</sup> In retrospect this is not surprising, since the “proportional inconsistency” (or path bias) for β<sub>2</sub> in Green and Kiernan’s equation 7 contains the prominent term $( \beta _ { 1 } / \beta _ { 2 } )$ When β<sub>2</sub> is small, (as it often will be when the true β<sub>2</sub> in the underlying model is near zero) the $( \beta _ { 1 } / \beta _ { 2 } )$ value will be large and very dependent on the values of $\beta _ { 1 }$ . Thus, we can expect a larger proportional bias, larger path biases, (and thus more false positives) when $\beta _ { 1 }$ gets larger.

This impact of larger $\beta _ { 1 }$ path values is demonstrated in Figure 7. At this point in the paper, we narrow our examples to only regression results, since it is clear that regression and PLS share the same M+ME problems. Figure 7 shows results for datasets having a reliability of .80 and a sample size of N = 200. Notice that the larger the $\beta _ { \mathrm { l } }$ path, the more the impact on false positives for $\beta _ { 2 } .$ Recognize that the largest β value, (.600) is a “very large” effect size (.51), and that the other two (.464 and .292) are “large” and “medium” effect sizes, respectively. It can be seen that the differences in $\beta _ { 1 }$ path values have an important impact.

## Summary of Hypothesis Testing Results

Our simulations have provided support for all our hypotheses. Specifically, in both regression and PLS, excessive false positives are possible, and the incidence increases with measurement error, with the size of the correlation between predictor constructs and with sample size. It addition, though not hypothesized, false positives increase with the size of the dominant construct of a correlated pair. At the same time, we did not find excessive false positives with CB-SEM under any of these conditions.

![](/api/attachments/ZMPN82TN/fulltext/images/9d74b6f5095e94e6ccba34f07f278c6890caf69441b22cae1358e917d7d4c877.jpg)  
Figure 7. Regression False Positives as β<sub>1</sub> Increases (from .292 to .600) (Alpha = .80, N = 200)

## Correcting for M+ME Biases

Fortunately, because we have an equation for the bias in the VIF (equation 4) and in the path estimates for regression (equations 6 and 7 from Green and Kiernan), it is possible to correct for the bias due to M+ME. The process involves several steps. The correct VIF for the biased path estimate must be determined, the biased path estimate must be transformed to the correct value using Green and Kiernan’s equations, and the implications of that path estimate transformation on the standard deviation of the resulting path must be taken into account (see Appendix A). Although this might sound daunting, we have created an excel spreadsheet application (also described in Appendix D and available on the MISQ web site) that carries out all these steps. The input required and the output provided are shown in Figure 8.

For the researcher needing to apply these corrections, Appendix D walks through the steps, including examples and results. Figure 9 shows the results of applying our corrections to the same simulation data displayed in Figure 7, showing the impact of higher β<sub>1</sub> values. It can be seen that the M+ME correction reduces false positives to an acceptable level.

## The Challenge of Combinations of High Correlations

Our correction above for M+ME in regression and PLS assumes that there is only one highly correlated pair of constructs in any given regression equation. When there are more than two correlated constructs predicting the dependent variable in a single regression equation, the situation becomes more complex. Details of our review of IS journals are described in the next section. Of the 37 IS articles we identified as being in the M+ME danger zone, 15 had at least three independent variables correlated, with one correlation > .50 and a second > .30. It appears that this may be enough to create excessive false positives. This is an area where more research is needed. Appendix E goes into this issue in more depth. Until future research provides a more appealing solution, the short answer for those analyzing models where this might be the case, is to (1) switch to a CB-SEM technique, (2) verify the regression or PLS results with a separate CB-SEM analysis, (3) revise the model, possibly by introducing higher-order constructs (Edwards, 2001), or (4) both change the model and switch to CB-SEM. The first option sidesteps the problem, since CB-SEM takes measurement error into account in its basic estimation process.

## Possible Concerns, Future Directions

There are a number of issues that need to be considered relative to the relevance and accuracy of our work. We deal with several of these below.

![](/api/attachments/ZMPN82TN/fulltext/images/92b8ee4c6f03ea967b12b12d3920ef7f331fce57154660115b8580f61ea4d1ef.jpg)  
Figure 8. The Input and Results Display of the M+ME Correction Application

![](/api/attachments/ZMPN82TN/fulltext/images/31b92d65fd8c7c2005a382695ab9bb7ff19cc421912aafb24bbcc09807e5cd22.jpg)  
Figure 9. Regression Results After Correcting the Analyses in Figure 7 (N = 200, Alpha = .80)

## How Big a Problem Is this for IS Researchers?

We reviewed three top IS journals: MIS Quarterly, Information Systems Research, and the Journal of Management Information Systems from 2010 to 2015 (inclusive) looking for papers that used PLS, regression, or CB-SEM to analyze path models for hypothesis testing. We found 365 such papers in this period. Of these, 30% did not report construct correlations and 41% reported at least one (overt) correlation of greater than .50. Of the 41% with high overt correlations, 37% had correlations between .50 and .60, and 63% were greater than .60. Recall that a reported (overt) correlation of .50 with reliability of .80 probably indicates an underlying correlation of around .60, and an overt correlation of .60 indicates an underlying correlation of around .75.

Altogether, of the 365 published papers, 132 used constructs measured with multiple items, and reported both correlations and reliabilities. Twenty of these used CB-SEM, and 112 used PLS or regression. Of these 112 papers, 37 (33%) had at least one correlation greater than .50 and a combined reliability<sup>25</sup> of less than .90.<sup>26</sup>

In other words, of the regression and PLS papers that included enough information that we could evaluate them, 33% were operating in the M+ME danger zone. We are not suggesting that all 37 of these papers are reporting levels of statistical significance (i.e., p < .05 or p < .01) that are in error, but we are suggesting that all 37 of them are inadvertently reporting overestimated t-statistics. Correcting this might or might not change the level of statistical significance reported by the authors.

Are these 112 papers with 37 in the M+ME danger zone representative of regression and PLS IS papers in general? That isn’t clear, but it certainly is possible. The implication is that IS researchers too often operate in the M+ME danger zone. More importantly, researchers are completely unaware of the danger. Given a new awareness of M+ME, we would suggest that analyses that are in the M+ME danger zone deserve a closer look to rule out the possibility of excessive false positives.

## What About Single Item Measures?

In the introduction of this paper, we set as a boundary condition for our work that we were examining causal models involving the use of latent constructs measured with multiple reflective indicators. We explicitly excluded situations involving the use of single item measures. We would like to point out, however, that the M+ME phenomenon is also relevant for single item measures. Specifically, it is uncommon to have measures that do not contain some amount of measurement error (even though researchers employing single indicators with regression or PLS typically assume no measurement error). As a result, a research model involving two or more highly-correlated, single item variables is also susceptible to M+ME.

We recommend that researchers employing single item measures use the M+ME correction application we created to determine if M+ME could be an issue, and if so how best to address it. The primary challenge here is that with single item measures, we generally do not know the reliability. Nevertheless, a researcher could employ sensitivity analysis by assuming different levels of reliability (e.g., .80, or .90 rather than 1.00) and see what impact that would have. Alternatively, a researcher could use CB-SEM and explicitly model some level of measurement error.

## How Would Negative Paths or Negative Correlations Change the Picture?

Some research (e.g., Mela and Kopalle 2002) has suggested that positive versus negative correlations would have different impacts on path biases. In Appendix C we address this issue. There we see that negative values for the paths or correlations do have different impact on results, but that all of these situations still conform to the Green and Kiernan equations, and our M+ME correction application works properly under all combinations of positive and negative signs.

## Discriminant Validity Problems Versus M+ME

One alternative explanation for the results we obtained might be framed within the larger context of measurement model misspecification, and specifically the presence of a lack of discriminant validity among constructs.<sup>27</sup> A lack of discriminant validity could certainly result in false positives. In Appendix F we test the possibility that measurement validity problems (rather than M+ME) are the source of the excessive false positives we found. From these tests it is clear that the two phenomena share some causal factors, but are actually quite distinct. Most telling is the fact that as sample size increases, discriminant validity problems are greatly reduced, while M+ME problems are greatly increased. M+ME and discriminant validity are clearly separate issues. Even if an analysis of the data shows acceptable discriminant validity, it can still be vulnerable to M+ME bias.

## Discussion and Conclusion

Drawing primarily from articles in six different disciplines, and carefully testing our insights with Monte Carlo simulation, we have identified and verified a previously unrecognized statistical blind-spot in regression analysis. We have shown that when correlated predictor constructs are measured with random measurement error, there is the potential for excessive false positives, not only in regression but also in PLS. CB-SEM avoids this problem. We have suggested that when using regression or PLS, if overt correlations are around .50 or higher, attention should be given to the M+ME possibility. We have also demonstrated a large increase in false positives when sample size increases, suggesting special caution when analyzing large sample sizes. Given the above danger of excessive false positives, we find dangerous the reality that a number of published IS articles do not report construct correlations and reliabilities. We suggest that editors and reviewers should require researchers to report this information in order to demonstrate that their results are not biased by M+ME.

In addition to showing that M+ME is a potential problem, we have provided recommendations for researchers who find themselves working with data where M+ME could be a concern. When there is only a single pair of correlated constructs predicting a third, the problem can be corrected by using the M+ME correction application, which will adjust the VIFs, correct the path bias, and recalculate standard deviations of the path estimates. (For the interested reader, Appendix G shows a pictorial display of the impact of M+ME and of correcting for it.)

We also suggested that “combinations” of high correlations (more than two highly correlated constructs affecting the same dependent construct), can create M+ME problems that are tougher to address. Correlations of .50 combined with another correlation of as low as .30 can be problematic. At present, the only surefire recommendation would be to check results with a CB-SEM analysis or to use second order factors. This is clearly an area in need of more research.

How about just dropping troublesome constructs? The problem with that approach is that dropping one of a pair of correlated constructs suggests to readers that the dropped construct has no impact in the real world, and that all the impact comes from the included construct. In fact, the researcher has no basis for asserting this. Given what we now know about M+ME, what the data is telling us is not that the second construct has no impact, but rather that given the high correlation, the separate path estimates are too unstable to be relied on.

When the hypotheses suggest different and separable impacts, it may be difficult to accept that it may not be possible to separate out the individual causal effects, at least with the current dataset. You might be in the situation described by Johnston (1972, p. 164):

If multicollinearity proves serious enough in the sense that estimated parameters have an unsatisfactory low degree of precision, we are in the statistical position of not being able to make bricks without straw. The remedy lies essentially in the acquisition, if possible, of new data or information, which will break the multicollinearity deadlock.

Even if the separate impacts cannot be determined, some real value may be produced by testing to determine if the combination of the two constructs has a statistically significant impact on the dependent construct. This can be determined by an F-test that looks at the statistical significance of the increase in the R<sup>2</sup> if both constructs are added, versus neither added.<sup>28</sup> If the F-test (Cohen 1988) shows that the two constructs together explain a significant amount of variance in the dependent variable, you have demonstrated the importance of those two constructs. If nothing else, you show that future research should take both constructs into account.

Finally, our work presents persuasive evidence that Reinartz et al.’s (2009) finding that PLS has greater statistical power than CB-SEM is incorrect. We are not suggesting that Reinartz et al. made a mistake in their analysis, but rather that because researchers in general were not aware of the M+ME blind spot, Reinartz et al. were also unaware of the potential impact on their results.

Given that we have shown that a substantial number of published papers in IS research use data within the M+ME danger zone, we also wish to stress that these other previously published authors, like Reinartz et al., are blameless. In the future, however, we would suggest that authors take responsibility for checking their analyses for M+ME problems. We are not suggesting that researchers abandon the use of regression or PLS in favor of CB-SEM techniques just because of the potential for more false positives under the M+ME conditions. Rather, we suggest that researchers who employ these techniques be aware of the M+ME bias and use available corrections when analyses appear to be in the M+ME danger zone.

As scientists, we want to test our hypotheses by gathering and analyzing reliable data. Because of a lack of awareness about the M+ME blind spot, it appears that too often we may have mislead ourselves into believing we had support for hypotheses, when actually we did not. Since a major way in which science moves forward is by absorbing and building on findings from past papers, the M+ME blind spot, if not addressed, means that too often we might be building on sand, rather than bedrock.

We recognize that these assertions may be a challenge to established ways of interpreting the results of regression and PLS not just in IS research, but in behavioral and other fields that use regression or PLS. Some readers may be skeptical. We encourage further examination of this issue, confident that it will confirm what our equations and simulations have shown.

Cohen, J. 1988. Statistical Power Analysis for the Behavioral Sciences (2<sup>nd</sup> ed.), Hillsdale, NJ: Lawrence Erlbaum Associates.

## Acknowledgments

The authors would like to thank the Senior Editor, the Associate Editor, and anonymous reviewers for their invaluable assistance in advancing this work. They would also like to acknowledge the financial support offered by the Wake Forest School of Business.

## References

Barclay, D., Higgins, C., and Thompson, R. 1995. “The Partial Least Squares (PLS) Approach to Causal Modeling: Personal Computer Adoption and Use as an Illustration,” Technology Studies (2:2), pp. 285-309.

Bentler, P. M., and Huang, W. 2014. “On Components, Latent Variables, PLS and Simple Methods: Reactions to Rigdon’s Rethinking of PLS,” Long Range Planning (47:3), pp. 138-145.

Carmines, E. G., and Zeller, R. A. 1979. Reliability and Validity Assessment, Beverly Hills, CA: Sage Publications.

Chin, W. W. 1998. “The Partial Least Squares Approach to Structural Equation Modeling,” in Modern Methods for Business Research, G. A. Marcoulides (ed.), London: Psychology Press, pp. 295-336.

Chin, W. W., and Frye, T. 2003. PLS-Graph, Soft Modeling Inc.

Craney, T. A. and Surles, J. G. 2002. “Model-Dependent Variance Inflation Factor Cutoff Values, Quality Engineering (14:3), pp. 39-50.

Cronbach, L. J. 1951. “Coefficient Alpha and the Internal Structure of Tests,” Psychometrika (16:3), pp. 297-334.

Edwards, J. R. 2001. “Multidimensional Constructs in Organizational Behavior Research: An Integrative Analytic Framework,” Organizational Research Methods (4:2), pp. 144-192.

Fornell, C., and Larcker, D. 1981. “Evaluating Structural Equation Models with Unobservable Variables and Measurement Error,” Journal of Marketing Research (18:1), pp. 39-50.

Freckleton, R. 2011. “Dealing with Collinearity in Behavioral and Ecological Data: Model Averaging and the Problems of Measurement Error,” Behavioral Ecology and Sociobiology (65:1), pp. 91-101.

Fuller, W. 1987. Measurement Error Models, New York: Wiley.

Gefen, D., Rigdon, E., and Straub, D. 2011. “Editor’s Comments: An Update and Extension to SEM Guidelines for Administrative and Social Science Research,” MIS Quarterly (35:2), pp. iii-xiv.

Goodhue, D., Lewis, W., and Thompson, R. 2006. “Small Sample Size and Statistical Power in MIS Research,” in Proceedings of the 39<sup>th</sup> Hawaii International Conference on Systems Sciences, R. Sprague (ed.), Los Alamitos, CA: IEEE Computer Society Press, January 4-7.

Goodhue, D., Lewis, W., and Thompson, R. 2007. “Statistical Power in Analyzing Interaction Effects: Questioning the Advantage of PLS with Product Indicators,” Information Systems Research (18:2), pp. 211-227.

Goodhue, D., Lewis, W., and Thompson, R. 2011. “A Dangerous Blind Spot in IS Research: False Positives Due to Multicollinearity Combined with Measurement Error,” in Proceedings

of the 17<sup>th</sup> Americas Conference on Information Systems, Detroit, MI, August 4-7.

Goodhue, D., Lewis, W. and Thompson, R. 2012. “Does PLS Have Advantages for Small Sample Size or Non-Normal Data?,” MIS Quarterly (36:3), pp. 981-1001.

Green, C. J., and Kiernan, E. 1989. “Multicollinearity and Measurement Error in Econometric Financial Modelling,” The Manchester School (57:4), pp. 357-369.

Grewal, R., Cote, J. A., and Baumgartner, H. 2004. “Multicollinearity and Measurement Error in Structural Equation Models: Implications for Theory Testing,” Marketing Science (23:4), pp. 519-29.

Hair, J. F., Sarstedt, M., Pieper, T. M., Ringle, C. M. 2012. “An Assessment of the Use of Partial Least Squares Structural Equation Modeling in Marketing Research,” Long Range Planning (45:5/6), pp. 320-340.

Henseler, J., Dijkstra, T., Sarstedt, M., Ringle, C., Diamantopoulos, A., Straub, D., Ketchen, D. Hair, J., Hult, G., and Calantone, R. 2014. “Common Beliefs and Reality About PLS,” Organizational Research Methods (17:2), pp. 182-209.

Henseler, J., Ringle, C., and Sarstedt, M. 2015. “A New Criterion for Assessing Discriminant Validity in Variance-Based Structural Equation Modeling,” Journal of the Academy of Marketing Science (43:1), pp. 115-135.

Hwang, H., Malhotra, N. K., Kim, Y., Tomiuk, M. A., and Hong, S. 2010. “A Comparative Study on Parameter Recovery of Three Approaches to Structural Equation Modeling,” Journal of Marketing Research (47:4), pp. 699–712.

Johnston, J. 1972. Econometric Methods (2<sup>nd</sup> ed.), New York: McGraw-Hill.

Mason, C. H., and Perreault Jr., W. D. 1991. “Collinearity, Power, and Interpretation of Multiple Regression Analysis,” Journal of Marketing Research (28:3), pp. 268-280.

McIntosh, C., Edwards, J. and Antonakis, J. 2014. “Reflections on Partial Least Squares Path Modeling,” Organizational Research Methods (17:2), pp. 210-251.

Mela, C., and Kopalle, P. 2002. “The Impact of Collinearity on Regression Analysis: the Asymmetric Effect of Negative and Positive Correlations,” Applied Economics (34:6), pp. 667-677.

Neter, J., and Wasserman, W. 1974. Applied Linear Statistical Models (1<sup>st</sup> ed.), Homewood, IL: Richard D. Irwin.

Neter. J., Wasserman, W., and Kutner, M. 1985. Applied Linear Statistical Models (2<sup>nd</sup> ed.), Homewood, IL: Richard D. Irwin.

Nunnally, J. C., and Bernstein, I. H. 1994. Psychometric Theory (3<sup>rd</sup> ed.), New York: McGraw-Hill.

Pedhazur, E. J. 1997. Multiple Regression in Behavioral Research (3<sup>rd</sup> ed.), Victoria, Australia: Wadsworth.

Reinartz, W., Haenlein, M., Henseler, J. 2009. “An Empirical Comparison of the Efficacy of Covariance-Based and Variance-Based SEM,” International Journal of Research in Marketing (26:4), pp. 332-344.

Rigdon, E. E. 2012. “Rethinking Partial Least Squares Path Modeling: In Praise of Simple Methods,” Long Range Planning (45:5-6), pp. 341-358.

Ringle, C. M., Sarstedt, M., and Straub, D. 2012. “A Critical Look at the Use of PLS-SEM in MIS Quarterly,” MIS Quarterly (36:1), pp. iii-xiv.

Rönkkö, M. 2014. “The Effects of Chance Correlations on Partial Least Squares Path Modeling,” Organizational Research Methods (17:2), pp. 164-181.

Rönkkö, M, and Evermann, J. 2013. “A Critical Examination of Common Beliefs about Partial Least Squares Path Modeling,” Organizational Research Methods (16:3), pp. 425-448.

Rönkkö, M., McIntosh, C., Antonakis, J., and Edwards, J. 2016. “Partial Least Squares Path Modeling: Time for Some Serious Second Thoughts,” Journal of Operations Management (47-47), pp. 9-27.

Rönkkö, M, and Ylitalo, J. 2010. “Construct Validity in Partial Least Squares Path Modeling,” International Conference on Information Systems, St. Louis, MO.

Sarstedt, M., Hair, J., Ringle, C., Thiele, K., and Gudergan, S. 2016. “Estimation Issues with PLS and CBSEM: Where the Bias Lies!,” Journal of Business Research (69), pp. 3998-4010.

Zidek, J., Wong, H., Le, N. D., and Burnett, R. 1996. “Causality, Measurement Error and Multicollinearity in Epidemiology,” Environmetrics (7:4), pp. 441-451.

## About the Authors

Dale Goodhue is a professor emeritus at the University of Georgia’s Terry College of Business. He is the former MIS Department head, and former C. Herman and Mary Virginia Terry Chair of Business Administration. He has published in journals including Management Science, MIS Quarterly, Information Systems Research, Decision Sciences, and Sloan Management Review. Dale’s research interests include measuring impacts of information systems, the impact of task technology fit on individual performance, the management of data and other IS infrastructures/resources, the impacts of enterprise systems on organizations, and the strengths and weaknesses of various statistical techniques.

William Lewis is an independent consultant and a former assistant professor of MIS in the Department of Management and Information Systems at Louisiana Tech University. His research has appeared in several journals including MIS Quarterly and Communications of the ACM. William’s research interests include business continuity planning, individual technology adoption in organizations, IS leadership, and research methodology.

Ronald (Ron) Thompson is the John B. McKinnon Professor and Area Chair in the School of Business at Wake Forest University. His research has been published in a variety of journals, including MIS Quarterly, Information Systems Research, Journal of Management Information Systems, and Journal of the AIS. Ron is a former senior editor for MIS Quarterly, and also formerly served on the editorial board for Journal of the AIS. He holds a Ph.D. from the Ivey School at the University of Western Ontario. His current research interest include managing IS projects, moral identity, and the strengths and weaknesses of various statistical analysis techniques.

# A MULTICOLLINEARITY AND MEASUREMENT ERROR STATISTICAL BLIND SPOT: CORRECTING FOR EXCESSIVE FALSE POSITIVES IN REGRESSION AND PLS

Dale L. Goodhue Terry College of Business, MIS Department, University of Georgia, Athens, GA 30606 U.S.A. {dgoodhue@terry.uga.edu}

William Lewis {william.w.lewis@gmail.com}

Ron Thompson School of Business, Wake Forest University, Winston-Salem, NC 27109 U.S.A. {thompsrl@wfu.edu}

## Appendix A

Deriving Equations for M+ME Biases and for t-statistic Overestimations

## Determining the Impact of VIF Bias on the t-statistic

Consider first the situation where we have no measurement error. Using standard equations for the estimated standard error of $\beta _ { 2 }$ from any regression textbook, an unbiased and consistent estimate of the standard error is

$$
\mathrm{s} ^ {2} = \Sigma \varepsilon_ {\mathrm{i}} ^ {2} / (\mathrm{N-K})\tag{A1-1}
$$

and the estimate of the variance of $\beta _ { 2 }$ is

$$
\operatorname{Var} \left(\beta_ {2} ^ {\wedge}\right) = \left[ s ^ {2} / \Sigma x _ {2 i} ^ {2} \right] * \left[ 1 / \left(1 - \rho_ {1 2 \text { Underlying }} ^ {2}\right) \right]\tag{A1-2}
$$

When the error terms are normally distributed, the following has a t distribution:

$$
\mathrm{t} - \text { stat } = (\beta_ {2} ^ {\wedge} - \beta_ {2}) / \{\text { Var } (\beta_ {2} ^ {\wedge}) \}. ^ {5} \quad \sim t _ {\text { N - K }}\tag{A1-3}
$$

Substituting in the equations for Var ( β<sup>^</sup><sub>2</sub>) and $s ^ { 2 }$ from above (A1-1 and A1-2), we can see the impact of correlated predictor variables on the t-stat.

$$
\begin{array}{l l} \text {t - stat} = (\beta_ {2} ^ {\wedge} - \beta_ {2}) & / \quad \{\left[ s ^ {2} / \Sigma x _ {2 i} ^ {2} \right] * [ 1 / (1 - \rho_ {1 2 \text {Underlying}} ^ {2}) ] \} ^ {- 5} \\ \text {t - stat} = (\beta_ {2} ^ {\wedge} - \beta_ {2}) & / \quad \{\left[ \{\Sigma \varepsilon_ {i} ^ {2} / (N - K) \} \right] / \Sigma x _ {2 i} ^ {2} ]) * [ 1 / (1 - \rho_ {1 2 \text {Underlying}} ^ {2}) ] \} ^ {- 5} \end{array}
$$

Rearranging terms:

$$
\text { t - stat } = \quad (\beta_ {2} ^ {\wedge} - \beta_ {2}) \qquad / \qquad \{[ \Sigma \epsilon_ {i} ^ {2} / \{(N - K) * \Sigma x _ {2 i} ^ {2} \} ] * [ 1 / (1 - \rho_ {1 2 \text { Underlying }} ^ {2}) ] \}. ^ {5}
$$

Squaring both sides:

$$
\begin{array}{l l} (t - \text { stat }) ^ {2} = (\beta_ {2} ^ {\wedge} - \beta_ {2}) ^ {2} & / \{\left[ \Sigma \varepsilon_ {i} ^ {2} / \{(N - K) * \Sigma x _ {2 i} ^ {2} \} \right] * [ 1 / (1 - \rho_ {1 2 \text { Underlying }} ^ {2}) ] \} \\ (t - \text { stat }) ^ {2} = (\beta_ {2} ^ {\wedge} - \beta_ {2}) ^ {2} & * \{\left[ (N - K) * \Sigma x _ {2 i} ^ {2} \right] / \Sigma \varepsilon_ {i} ^ {2} ] * [ (1 - \rho_ {1 2 \text { Underlying }} ^ {2}) / 1 ] \} \\ (t - \text { stat }) ^ {2} = (\beta_ {2} ^ {\wedge} - \beta_ {2}) ^ {2} & * \{\left[ (N - K) * \Sigma x _ {2 i} ^ {2} * (1 - \rho_ {1 2 \text { Underlying }} ^ {2}) \right] / \Sigma \varepsilon_ {i} ^ {2} \end{array}
$$

Rearranging terms:

$$
\begin{array}{l} (t - \text { stat }) ^ {2} = \left\{\left[ (\beta_ {2} ^ {\wedge} - \beta_ {2}) ^ {2} * (N - K) * \Sigma x _ {2 i} ^ {2} * (1) / \Sigma \varepsilon_ {i} ^ {2} \right. \right\} \\ - \left\{\left[ (\beta_ {2} ^ {\wedge} - \beta_ {2}) ^ {2} * (N - K) * \Sigma x _ {2 i} ^ {2} * (\rho_ {1 2 \text { Underlying }} ^ {2}) \right] / \Sigma \varepsilon_ {i} ^ {2} \right\} \end{array}\tag{A1-4}
$$

Note that the first half of equation (A1-4) is the squared t-statistic if there were no correlation between $\mathrm { X } _ { 1 }$ and $\mathrm { X } _ { 2 } .$ . The second half is the correction for when there is a correlation (at this point all assuming no measurement error).

As suggested by Goodhue et al. (2011), the problem with the above is that the estimate for the correlation $\left( \rho _ { \mathrm { 1 2 U n d e r l y i n g } } \right)$ assumes perfect measurement (i.e., that the $\mathrm { X } _ { \mathrm { i } }$ values have no random measurement error). In regression, estimates of the two constructs are based on averaged or summed indicator scores, and any estimate of the $\rho _ { \mathrm { 1 2 U n d e r l y i n g } }$ correlation will be attenuated (reduced) by the random measurement error, as shown below:

$$
\rho_ {1 2 \text { Underlying }} = \rho_ {1 2 \text { Overt }} / (\alpha_ {1} * \alpha_ {2}) ^ {1 / 2}
$$

(Equation 2 from the paper proper)

(A1-5)

When we do have measurement error, $\rho _ { \mathrm { 1 2 - O v e r t } }$ is not equal to $\rho _ { \mathrm { 1 2 U n d e r l y i n g } } .$ When the t-stat calculated by regression has not been corrected for attenuation, A1-4 becomes:

$$
\begin{array}{r l} (t \text {-stat} _ {\text {Overt}}) ^ {2} _ {\text {(incorrect)}} = & \{[ (\beta_ {2} ^ {\wedge} - \beta_ {2}) ^ {2} * (N - K) * \Sigma x _ {2 i} ^ {2} ] / \Sigma \varepsilon_ {i} ^ {2} \} \\ & - \{[ (\beta_ {2} ^ {\wedge} - \beta_ {2}) ^ {2} * (N - K) * \Sigma x _ {2 i} ^ {2} * (\rho_ {1 2 \text {-Overt2}}) ] / \Sigma \varepsilon_ {i} ^ {2} \} \end{array}\tag{A1-6}
$$

Below (in equation A1-7) we show how the t-statistic value is biased by the incorrect ${ \mathrm { V I F } } ,$ assuming we know the reliabilities for $\mathrm { X } _ { 1 }$ and $\mathrm { X } _ { 2 }$ The first two lines are equation A1-6, assuming there is no correction to the VIF for random measurement error. The third line adds back the amount that was incorrectly subtracted out to correct for the X and X correlation (incorrect because not taking into account random measurement error attenuation), and then the fourth line subtracts the proper amount to correct for $\mathrm { X } _ { 1 }$ and $\mathrm { X } _ { 2 }$ correlation (taking into account random measurement error attenuation).

$$
\begin{array}{l} (t \text {-stat} _ {\text {Corrected}}) ^ {2} = \{[ (\beta_ {2} ^ {\wedge} - \beta_ {2}) ^ {2} * (N - K) * \Sigma x _ {2 i} ^ {2} ] / \Sigma \varepsilon_ {i} ^ {2} \} \\ \quad - \{[ (\beta_ {2} ^ {\wedge} - \beta_ {2}) ^ {2} * (N - K) * \Sigma x _ {2 i} ^ {2} * (\rho_ {1 2 \text {-Overt}} ^ {2}) ] / \Sigma \varepsilon_ {i} ^ {2} \} \\ \quad + \{[ (\beta_ {2} ^ {\wedge} - \beta_ {2}) ^ {2} * (N - K) * \Sigma x _ {2 i} ^ {2} * (\rho_ {1 2 \text {-Overt}} ^ {2}) ] / \Sigma \varepsilon_ {i} ^ {2} \} \\ \quad - \{[ (\beta_ {2} ^ {\wedge} - \beta_ {2}) ^ {2} * (N - K) * \Sigma x _ {2 i} ^ {2} * (\rho_ {1 2 \text {Underlying2}}) ] / \Sigma \varepsilon_ {i} ^ {2} \} \end{array}\tag{A1-7}
$$

The amount by which regression is overestimating the “t-statistic squared” due to the incorrect VIF is the following. This is the last two terms of equation A1-7 with the signs (and order) reversed:

$$
\begin{array}{l} (t - \text {stat}) ^ {2} \text {overestimation} = (t - \text {stat} _ {\text {Overt}}) ^ {2} - (t - \text {stat} _ {\text {Corrected}}) ^ {2} = \\ \quad + \{[ (\beta_ {2} ^ {\wedge} - \beta_ {2}) ^ {2} * (N - K) * \Sigma x _ {2 i} ^ {2} * (\rho_ {1 2 \text {Underlying} 2}) ] / \Sigma \varepsilon_ {i} ^ {2} \} \\ \quad - \{[ (\beta_ {2} ^ {\wedge} - \beta_ {2}) ^ {2} * (N - K) * \Sigma x _ {2 i} ^ {2} * (\rho_ {1 2 - \text {Overt}}) ^ {2}) ] / \Sigma \varepsilon_ {i} ^ {2} \} \end{array}\tag{A1-8}
$$

By inserting the square of equation A1-5 for the ${ \rho } _ { 1 2 \mathrm { U n d e r l y i n g } } ^ { 2 }$ term in A1-8, we get the following:

$$
\begin{array}{l} \left(\mathrm{t-stat}\right) ^ {2} \text {overestimation} = \left[ \left(\beta_ {2} ^ {\wedge} - \beta_ {2}\right) ^ {2} (\mathrm{N} - \mathrm{K}) \Sigma \mathrm{x} _ {2 \mathrm{i}} ^ {2} \left(\rho_ {1 2 \mathrm{Overt}} ^ {2}\right) / \left(\alpha_ {1} * \alpha_ {2}\right) \right] / \Sigma \varepsilon_ {\mathrm{i}} ^ {2} \\ - \left[ \left(\beta_ {2} ^ {\wedge} - \beta_ {2}\right) ^ {2} (\mathrm{N} - \mathrm{K}) \Sigma \mathrm{x} _ {2 \mathrm{i}} ^ {2} \left(\rho_ {1 2 \mathrm{Overt}} ^ {2}\right) \right] / \Sigma \varepsilon_ {\mathrm{i}} ^ {2} \end{array}\tag{A1-9}
$$

Gathering common terms, the amount the t-statistic squared in regression is overestimated due to the VIF bias when there are both correlated predictors and random measurement error is

$$
(t - \text { stat }) ^ {2} \text {   overestimation } = [ (1 / (\alpha_ {1} * \alpha_ {2})) - 1 ] * [ (\beta_ {2} ^ {\wedge} - \beta_ {2}) ^ {2} (N - K) \Sigma x _ {2 i} ^ {2} (\rho_ {1 2 - 0 \text {vert}} ^ {2}) ] / \Sigma \varepsilon_ {i} ^ {2}\tag{A1-10}
$$

Equation A1-10 is helpful in seeing the impact of various factors on the t-statistic overestimation due to bias in the VIF. It was one of the insights that led to our hypothesis generation. Of course it does not tell the full story, which would also require taking into account the path bias embodied in equations 6 and 7 from the paper, and determining the corrected standard deviation for the corrected estimated underlying path. We explain the logic of that below.

## Correcting the Path Estimates for the M+ME Bias

Johnston’s (1972) equations. Consider the following regression equation:

$$
\mathrm{Yi} = \beta_ {0} + \beta_ {1} \mathrm{X} _ {1 \mathrm{i}} + \beta_ {2} \mathrm{X} _ {2 \mathrm{i}} + \dots . + \beta_ {\mathrm{k}} \mathrm{X} _ {\mathrm{ki}} + \varepsilon_ {\mathrm{i}}\tag{A1-11}
$$

Though the essential results extend to the full equation above, for simplicity we will ignore all the $\beta _ { \mathrm { k } } X _ { \mathrm { k i } }$ terms above when k is greater than 2, giving

$$
\mathrm{Yi} = \beta_ {0} + \beta_ {1} \mathrm{X} _ {1 \mathrm{i}} + \beta_ {2} \mathrm{X} _ {2 \mathrm{i}} + \varepsilon_ {\mathrm{i}}\tag{A1-12}
$$

Following Johnston (1972, pp. 160-162), if we first look at the impact of multicollinearity on bias in the regression path estimates of $\beta _ { \mathrm { l } }$ and β (that is, ${ \beta } _ { 1 } ^ { \wedge }$ and β<sup>^</sup>), we see the following:

$$
\beta_ {1} ^ {\wedge} - \beta_ {1} = \Sigma u x _ {1} - (\rho_ {1 2} * \Sigma u v) / (1 - \rho_ {1 2} ^ {2})\tag{A1-13}
$$

and

$$
\beta_ {2} ^ {\wedge} - \beta_ {2} = (\Sigma \mathrm{uv}) / (1 - \rho_ {1 2} ^ {2})\tag{A1-14}
$$

where u is the vector of error terms in ${ \mathrm { Y } } ;$ v is the vector of error terms in the equation for $\mathrm { X } _ { 2 }$ as a function of $\mathrm { X } _ { \mathrm { i } } ;$ and ${ \boldsymbol \rho } _ { 1 2 }$ is the underlying correlation between $\mathrm { X } _ { 1 }$ and $\mathrm { X } _ { 2 }$

It is not necessary for the reader to understand the two equations in depth, but only to understand that mathematically, when $\mathrm { X } _ { 1 }$ and $\mathrm { X } _ { 2 }$ are correlated and the error terms u and v are non-zero,<sup>2</sup> regression estimates of ${ \bf \widehat { \mathbf { \beta } } } _ { 1 } ^ { \setminus }$ and $\boldsymbol { \beta } _ { 2 } ^ { \setminus }$ will be biased away from the underlying value (the true value absent any systematic error). We note that as $\rho _ { 1 2 }$ increases, the size of the negative bias for ${ \beta } _ { 1 } ^ { \wedge }$ increases. Likewise, as $\rho _ { 1 2 }$ increases, th size of the positive bias for $\boldsymbol { \beta } _ { 2 } ^ { \setminus }$ increases. Johnston goes on to say that a large correlation between independent variables ${ } ^ { \mathfrak { s c } } { } _ { \mathrm { i s } }$ thus likely to produce large and opposite errors in ${ \beta } _ { \mathrm { l } } ^ { \wedge }$ and $\beta _ { 2 } ^ { \cdot } , \mathrm { i f } \beta _ { 1 } ^ { \cdot }$ underestimates $\beta _ { \mathrm { 1 } } ,$ then $\beta _ { 2 } ^ { \setminus }$ is likely to overestimate $\beta _ { 2 }$ and vice versa. It is thus very important that the standard errors should alert one to the presence of multicollinearity” (p. 162).

Green and Kiernans’s (1989, pp. 359-363) equations. Green and Keirnan carried the analysis of the impact of multicollinearity and random measurement error on regression path biases further than Johnston. In particular, Green and Kiernan make a clear distinction between what we are calling the $^ { \mathfrak { c } \mathfrak { c } } \mathrm { o v e r t } ^ { \mathfrak { p } } \left( \mathfrak { p } _ { 1 2 \mathrm { o v e r t } } \right)$ and the $\mathrm { ^ { * } u n d e r l y i n g } ^ { \mathrm { \prime * } } \left( \mathrm { \pmb { p } } _ { \mathrm { 1 2 u n d e r l y i n g } } \right)$ correlation—the overt correlation is the correlation based on the “signalplus-noise” or the correlation between the “error containing” measures of the two constructs, while the “underlying” correlation is the correlation based only on the “signal,” without the noise (Green and Kiernan 1989, p. 360.)

<sup>1</sup>We note that it would be incorrect to suggest that we can take the square root of both sides of equation (A1-10) and therefore determine that

$$
\text { t - stat   overestimation } = \{[ (1 / \alpha_ {1} * \alpha_ {2}) - 1 ] * [ (\beta_ {2} ^ {\wedge} - \beta_ {2}) ^ {2} (\mathrm{N-K}) \Sigma x _ {2 i} (\rho_ {1 2 - \text { Overt }} ^ {2}) ] / \Sigma \varepsilon_ {i} ^ {2} \}. 5\tag{not correct}
$$

The (t-stat)<sup>2</sup> overestimation term is not the same as [t-stat overestimation]<sup>2</sup>.

Under fairly general conditions (equal reliability $\{ { \bf { \alpha } } \alpha _ { 1 } = \alpha _ { 2 } \}$ for $\beta _ { \mathrm { l } }$ and $\beta _ { 2 ; } \beta _ { 1 } > 0 )$ , Green and Keirnan gave equations for what they call “proportional inconsistencies” or $\mathrm { ( P I _ { j } ) }$ defined as (β – plim $\beta _ { \mathrm { i } } ^ { \mathrm { \wedge } } \mathrm { ) / \beta _ { \mathrm { i } } }$ . If PI is positive, then plim $\beta _ { \mathrm { i } } ^ { \wedge }$ is less than $\beta _ { \mathrm { i } } \left( \mathrm { i } . \mathrm { e } _ { \cdot } \right.$ , an underestimation); If $\mathrm { P I } _ { \mathrm { i } }$ is negative, then plim $\beta _ { \mathrm { i } } ^ { \wedge }$ is greater than $\beta _ { \mathrm { i } } ; ( \mathrm { i } . \mathrm { e } .$ ., an overestimation). We will reproduce two of their equations, folding in several other additional reasonable assumption that are appropriate to our analysis here.<sup>3</sup> With this assumption Green and Kiernan’s equations for the proportional inconsistency show us more about the impact of M+ME on regression estimates than Johnston’s treatment.

$$
\mathrm{PI} _ {\beta 1} = \left(\beta_ {1} - \operatorname{plim} \beta_ {1} ^ {\wedge}\right) / \beta_ {1} = \left[ \left(1 - \alpha_ {1}\right) / \left(1 - \rho_ {1 2} ^ {2}\right) \right] * \left[ 1 - \left(\rho_ {1 2} * \left(\beta_ {2} / \beta_ {1}\right)\right) \right] \quad (\text { Equation   6   repeated }) \tag {A1-15}
$$

$$
\mathrm{PI} _ {\beta 2} = \left(\beta_ {2} - \operatorname{plim} \beta_ {2} ^ {\wedge}\right) / \beta_ {2} = \left[ \left(1 - \alpha_ {1}\right) / \left(1 - \rho_ {1 2} ^ {2}\right) \right] * \left[ 1 - \left(\rho_ {1 2} * \left(\beta_ {1} / \beta_ {2}\right)\right) \right] \quad (\text { Equation   7   repeated })\tag{A1-16}
$$

Here $\rho _ { 1 2 }$ is the $\mathbf { \bar { \Psi } } _ { 0 } ^ { \mathsf { c c } } _ { \mathbf { \Psi } } \mathbf { \mathrm { e r t } } ^ { \mathsf { \tiny { 5 } } } \mathbf { \Psi }$ correlation between $\mathrm { X } _ { 1 }$ and $\mathrm { X } _ { 2 } , \mathrm { \bf q } _ { 1 }$ is the reliability of $\mathrm { X } _ { \mathrm { l } }$ and of $\mathrm { X } _ { 2 } ( \alpha _ { \mathrm { l } }$ is assumed be equal to $\mathrm { \bf q } _ { 2 } ) . ^ { 4 } \mathrm { \bf ~ P I _ { i } }$ indicates the proportional amount the plim $\beta _ { \mathrm { i } } ^ { \setminus }$ estimate has been biased away from the true (or underlying) value of ${ \mathrm { ' } } \beta _ { \mathrm { i } }$ . The “plim” indicates that plim βˆ would be the estimate if there were an infinite number of data points. (As stated earlier in the paper, we found that with sample sizes of 100 to 200, the equations predicted the values of regression path estimates reasonably accurately, and for collections of 500 datasets at those sample sizes, quite accurately in the aggregate).

These equations can give us a feel for how M+ME will affect regression path estimates. Assume for the moment that $\beta _ { 1 } , \beta _ { 2 } ,$ and $\rho _ { 1 2 }$ are all positive and $\beta _ { 1 }$ is greater than $\beta _ { 2 }$ (a not uncommon situation). Under these conditions, given that $\mathbf { { \alpha } } _ { \mathbf { { 1 } } } , \mathbf { { \rho } } _ { 1 2 } ,$ and $\beta _ { 2 } / \beta _ { 1 }$ are all less than one, it can be seen that $\mathrm { P I } _ { \{ 3 1 } $ will always be greater than zero. (Recall that: $\mathrm { P I } _ { \mathrm { i } } { > } 0 \Rightarrow \mathrm { \beta } _ { \mathrm { i } } ^ { \mathrm { ^ { \wedge } } }$ is underestimated.) Therefore given our assumptions, when there is multicollinearity and random measurement error, the dominant $\beta _ { 1 }$ will always be underestimated.

Depending on the values of $\rho _ { \mathrm { 1 3 } }$ and $\beta _ { 1 } / \beta _ { 2 }$ , the non-dominant $\beta _ { 2 }$ could be under- or over-estimated. In Appendix C we present the logic that shows that except when $\beta _ { 1 }$ and $\beta _ { 2 }$ have close to the same value, M+ME will tend to push the $\boldsymbol { \beta } _ { 2 } ^ { \setminus }$ estimate higher than $\beta _ { 2 } \ i \mathrm { f } \ \beta _ { 2 }$ β if is positive.

Equations for Correcting the Path Estimate Bias. Although the algebra is tedious, equations A1-15 and A1-16 can be turned around to allow us to calculate estimates of the underlying $\beta$ values, given the β<sup>^</sup> and $\boldsymbol { \beta } _ { 2 } ^ { \setminus }$ estimates, as follows:

$$
\text { Let } C = (1 - \alpha_ {1}) / (1 - \rho_ {1 2} ^ {2})
$$

$$
\begin{array}{l} \text {(Recall that when \alpha_ {1} is not equal to \alpha_ {2} we use} \\ \alpha_ {1} = \alpha_ {\text { combination }} = (\alpha_ {1} * \alpha_ {2}) ^ {1 / 2}. \text { See footnote \#16.}) \end{array}
$$

$$
\left(\beta_ {1} - \beta_ {1} ^ {\wedge}\right) / \beta_ {1} = C * \left[ 1 - \rho_ {1 2} * \beta_ {2} / \beta_ {1} \right]
$$

$$
\left(\beta_ {1} - \beta_ {1} ^ {\wedge}\right) = \beta_ {1} \left\{\mathrm{C} * \left[ 1 - \rho_ {1 2} * \beta_ {2} / \beta_ {1} \right] \right\}
$$

(Green and Kiernan’s Equation for $\mathrm { P I } _ { \beta 1 } )$

$$
\beta_ {1} = \beta_ {1} ^ {\wedge} + \beta_ {1} C * [ 1 - \rho_ {1 2} * \beta_ {2} / \beta_ {1} ]
$$

$$
\beta_ {1} = \beta_ {1} ^ {\wedge} + \beta_ {1} C - C * \rho_ {1 2} * \beta_ {2} ]
$$

$$
\left. \beta_ {1} - \beta_ {1} C = \beta_ {1} ^ {\wedge} - C * \rho_ {1 2} * \beta_ {2} \right]
$$

$$
\beta_ {1} = \beta_ {1} ^ {\wedge} / (1 - C) - [ C * \rho_ {1 2} * \beta_ {2} ] / (1 - C)
$$

Similarly

$$
\beta_ {2} = \beta_ {2} ^ {\wedge} / (1 - C) - [ C * \rho_ {1 2} * \{\beta_ {1} \} ] / (1 - C)
$$

Substituting in $( \beta _ { \mathrm { 1 } } )$ and collecting terms,

$$
\beta_ {2} = \beta_ {2} ^ {\wedge} / (1 - C) - [ C * \rho_ {1 2} * \{\beta_ {1} ^ {\wedge} / (1 - C) - [ X * \rho_ {1 2} * \beta_ {2} ] / (1 - C) \} ] / (1 - C)
$$

$$
\beta_ {2} = \beta_ {2} ^ {\wedge} / (1 - C) - C * \rho_ {1 2} * \beta_ {1} ^ {\wedge} / (1 - C) ^ {2} + \left[ \left(C * \rho_ {1 2}\right) ^ {2} * \beta_ {2} \right] / (1 - C) ^ {2}
$$

$$
\beta_ {2} - \left(\mathrm{C} * \rho_ {1 2}\right) ^ {2} * \beta_ {2} / (1 - \mathrm{C}) ^ {2} = \beta_ {2} ^ {\wedge} / (1 - \mathrm{C}) - \mathrm{C} * \rho_ {1 2} * \beta_ {1} ^ {\wedge} / (1 - \mathrm{C}) ^ {2}
$$

$$
\beta_ {2} \left[ 1 - \left(\mathrm{C} * \rho_ {1 2}\right) ^ {2} / (1 - \mathrm{C}) ^ {2} \right] = \beta_ {2} ^ {\wedge} / (1 - \mathrm{C}) - \mathrm{C} * \rho_ {1 2} * \beta_ {1} ^ {\wedge} / (1 - \mathrm{C}) ^ {2}
$$

$$
\beta_ {2} = \left[ \beta_ {2} ^ {\wedge} / (1 - C) - C * \rho_ {1 2} * \beta^ {\wedge} / (1 - C) ^ {2} \right] / \left[ 1 - \left(C * \rho_ {1 2}\right) ^ {2} / (1 - C) ^ {2} \right]
$$

$$
\beta_ {2} = \beta_ {2} ^ {\wedge} / (1 - C) - C * \rho_ {1 2} * \beta_ {1} ^ {\wedge} / (1 - C) ^ {2} / \left[ (1 - C) ^ {2} - (C * \rho_ {1 2}) ^ {2} \right] / (1 - C) ^ {2}
$$

$$
\beta_ {2} = \frac {\beta_ {2} ^ {\wedge} * (1 - C) - C * \rho_ {1 2} * \beta_ {1} ^ {\wedge}}{\left[ (1 - C) ^ {2} \right] - \left(C * \rho_ {1 2}\right) ^ {2}}\tag{A1-17}
$$

Similarly

$$
\beta_ {1} = \frac {\hat {\beta_ {1}} * (1 - C) - C * \rho_ {1 2} * \hat {\beta_ {2}}}{[ (1 - C) ^ {2} ] - (C * \rho_ {1 2}) ^ {2}}\tag{A1-18}
$$

Correcting the Standard Deviation of the Corrected Path Estimate. One final insight is needed in correcting for the M+ME path bias. To determine the proper estimate of the path standard deviation, we have to recognize that the path bias created by the M+ME comes with a change in the standard deviation. To calculate the corrected standard deviation for the true path we need to, in a sense, undo that change. Once the variances of the $\beta _ { 1 } ^ { \wedge }$ and $\boldsymbol { \beta } _ { 2 } ^ { \setminus }$ paths have been corrected for the VIF bias (Equation A1-2), the variance of the estimates for the above underlying $\beta _ { 1 }$ and $\beta _ { 2 }$ paths can be calculated using a standard result from statistics:

$$
\begin{array}{l l} \text { if } & \beta_ {2} = a * \beta_ {2} ^ {\wedge} + b * \beta_ {1} ^ {\wedge} \\ \text { then } & \operatorname{Var} (\beta_ {2}) = a ^ {2} * \operatorname{Var} (\beta_ {2} ^ {\wedge}) + b ^ {2} * \operatorname{Var} (\hat {} _ {1}) \end{array}\tag{A1-19}
$$

where in our case $\mathbf { \ddot { a } } ^ { , \nu }$ is $\left( 1  – \mathrm { C } \right) / \{ ( 1 – \mathrm { C } ) ^ { 2 } - ( \mathrm { C } * \rho _ { 1 2 } ) ^ { 2 } \}$ , and $\mathbf { \bar { \Delta } } ^ { \mathrm { c } } ( \mathbf { b } ^ { \mathrm { , } \mathrm { , } }$ is $\mathrm { C } * \rho _ { 1 2 } / \{ ( 1 { - } \mathrm { C } ) ^ { 2 } - ( \mathrm { C } * \rho _ { 1 2 } ) ^ { 2 } \}$ from equation $_ { \mathrm { A l - 1 7 } }$

## Appendix B

## Will PLS with Bootstrapping Correct for M+ME?

For PLS with bootstrapping to correct for the M+ME blindspot seen in regression, it would need to overcome the deficiency noted in our equation 3 versus our equation 4. That is, it would need to somehow incorporate random measurement error into its estimate for the standard deviations of the X1 and X2 paths leading to Y1. We see two possible ways that PLS with bootstrapping could do this. First, bootstrapping could determine the reliability of the two constructs (in our case the X1 and X2 constructs). It could then adjust its (bootstrapping determined) standard deviation of the path using those reliabilities, similarly to our equation 4. However, we see no point in the PLS bootstrapping process where the reliability of the two construct measures is taken into account. For each bootstrapping resample, after the indicator weights are determined and the proxy construct scores calculated, all information about the indicator values is discarded. What occurs is that OLS regression is used with the proxy construct scores to determine another set of path values. Nowhere in the process is the information (for explicitly determining the measurement reliability of the constructs) used by PLS or its bootstrapping process.

A second possibility could be that bootstrapping automatically takes M+ME into account. The central assumption of bootstrapping in general (Mooney and Duval 1993) is that the variation contained in a given sample is representative of the variation existing in the larger population. If this were true for the M+ME blind spot, then bootstrapping could correctly incorporate the extra variation due to M+ME and suggest appropriately larger standard deviations.

If in some bootstrapping resamples M+ME led to additional overestimations of the path values, and in others M+ME led to additional underestimations, then the total distribution of the bootstrapping resample path values would be appropriately wider, and estimations for the path standard deviations would have increased accordingly. However, recall that each PLS bootstrapping resample is drawn from the original sample and therefore contains roughly the same underlying $\beta _ { 1 } , \beta _ { 2 } , \rho _ { 1 2 }$ , and other characteristics as the original sample. We showed in Appendix A that Green and Kiernan’s equations (A1-15 and A1-16) clearly indicate that when there is M+ME and both path estimates are positive and not too close together, regression will tend to systematically underestimate ${ \beta } _ { 1 } ^ { \wedge }$ and systematically overestimate $\beta _ { 2 } ^ { \setminus }$ based on the reliability and the values of $\beta _ { 1 } , \ \beta _ { 2 } .$ , and ${ \rho _ { 1 2 } } ^ { 5 }$ The bias seen in Green and Kiernan’s equations (6 and 7) for regression will then be apparent in each of the bootstrapping regression results

Therefore, it is reasonable to assume that when PLS uses OLS to estimate paths for each of its bootstrapping samples, it will tend to systematically underestimate each of those $\beta _ { 1 } ^ { \wedge }$ path estimates by roughly the same amount, and to systematically overestimate each of those $\boldsymbol { \beta } _ { 2 } ^ { \setminus }$ estimates by roughly the same amount. If that is true, instead of having the collection of bootstrapping $\boldsymbol { \beta } _ { 2 } ^ { \setminus }$ path estimates more widely dispersed, they will be biased but about as closely spaced as if there were no M+ME bias.

PLS’s bootstrapping distributions should therefore incorporate the same variance inflation factor as seen in equation 3, mirroring the results seen in regression. We see no argument for a way in which the PLS bootstrapping resamples will incorporate the correction shown in our equation 4.

## Appendix C

## Further Exploration of Green and Kiernan’s Equations: Impact of Negative Paths or Negative Correlations

Mela and Kopalle (2002) have argued that positive versus negative correlations would have very different (asymmetric) impacts on path biases and path estimate variances. For us (with multicollinearity and random measurement error) that question is answered by looking again at Green and Kiernan’s (1989, p. 360) equations for the bias (or proportional inconsistency) in the estimates for ${ \beta } _ { \mathrm { l } } ^ { \wedge }$ and $\beta _ { 2 } ^ { \setminus } .$

$$
\begin{array}{l} \mathrm{PI} _ {\beta 1} = (\beta_ {1} - \operatorname{plim} \beta_ {1} ^ {\wedge}) / \beta_ {1} = [ (1 - \alpha_ {1}) / (1 - \rho_ {1 2} ^ {2}) ] * [ 1 - (\rho_ {1 2} * (\beta_ {2} / \beta_ {1})) ] \\ \mathrm{PI} _ {\beta 2} = (\beta_ {2} - \operatorname{plim} \beta_ {2} ^ {\wedge}) / \beta_ {2} = [ (1 - \alpha_ {1}) / (1 - \rho_ {1 2} ^ {2}) ] * [ 1 - (\rho_ {1 2} * (\beta_ {1} / \beta_ {2})) ] \end{array}
$$

(Eq. 6 repeated) (Eq. 7 repeated)

Equations 6 and $^ { 7 , }$ repeated above, can tell us quite a bit about the behavior of ${ \beta } _ { \mathrm { l } } ^ { \wedge }$ and $\textstyle { \bigl \beta } _ { 2 } ^ { \wedge } .$ First, remember that if $\mathrm { P I } _ { \mathrm { \beta i } } \mathrm { \ i s } > 0$ , then $| \beta _ { 1 } ^ { \setminus } |$ is an underestimation of $\lVert \beta _ { \mathrm { i } } \rVert .$ . If $\mathrm { P I } _ { \mathrm { \beta i } } \mathrm { i } \mathrm { s } < 0$ , then $| \beta _ { \mathrm { i } } ^ { \setminus } |$ is an overestimation of| β |. If |β<sup>^</sup>| is an underestimation of |β |, this means that $| \beta _ { \mathrm { i } } ^ { \wedge } |$ is closer to zero than $| \beta _ { \mathrm { i } } |$ . Whether $\beta _ { 1 }$ or $\beta _ { 2 }$ are over- or under-estimated depends upon the sign of $\mathrm { P I } _ { \{ 3 1 } $ or $\mathrm { P I } _ { \beta 2 } .$ . Note that in both equations, the $[ ( 1 ~ \cdot ~ $ ${ \bf \alpha } _ { { \bf { \Lambda } } } ) / ( 1 { - } { \rho _ { 1 2 } } ^ { 2 } ) \stackrel { \cdot } { . }$ ] term before the asterisk is always positive. Therefore whether $\beta _ { 1 }$ or β are over or under-estimated depends upon the sign of $[ 1 - ( \mathsf { p } _ { 1 2 }$ $\ast _ { \mathrm { \ell } } ( \beta _ { 2 } / \beta _ { 1 } ) ]$ or $[ 1 - ( \mathsf { p } _ { 1 2 } * ( \mathsf { \{ \beta }  _ { 1 } / \mathsf { \beta } _ { 2 } ) ) ]$ ]. Table C1 shows the impact of different combinations of negative and positive signs on $[ 1 - ( \mathsf { p } _ { 1 2 } * ( \mathsf { \{ \beta }  _ { 2 } / \mathsf { \beta } _ { 1 } ) ) ]$ or $[ 1 - ( \mathsf { p } _ { 1 2 } * ( \mathsf { \{ \{ \beta } _ { 1 } / \mathsf { \{ \beta } _ { 2 } )    ) ]$ , and therefore on the value and sign of the proportional inconsistencies.

One interesting outcome is apparent in the column labeled “Decision Condition” of Table C1. For $\beta _ { 1 }$ there is no decision: $\mathrm { i f } | \beta _ { 1 } ^ { \wedge } | > | \beta _ { 2 } ^ { \wedge } |$ |, we would say that $\beta _ { 1 } ^ { \wedge }$ is dominant. In this case ${ | \ \beta _ { 1 } ^ { \wedge } }$ | will always be an underestimation of $\beta _ { \mathrm { l } }$ |. More interesting is the case for $| \beta _ { 2 } ^ { \setminus } | . \ \mathrm { I f } | \ \beta _ { 2 } ^ { \setminus } |$ is relatively large (i.e. , greater than $| \rho _ { 1 2 } * \beta _ { 1 } ^ { \wedge } | )$ , then $\hat { | \beta _ { 2 } | }$ will also be an underestimate of $\mid \beta _ { 2 } \mid .$ Otherwise, $| \beta _ { 2 } ^ { \setminus } |$ will be an overestimate of $\left. \beta _ { 2 } \right| .$ This last can lead to false positives.

Relative to Mela and Kopalle’s arguments, in fact it can be seen that having zero or two negative signs for $\rho _ { 1 2 } , \beta _ { 1 }$ ,and $\beta _ { 2 }$ creates a quite different configuration of the results than having one or three negatives. Having exactly two of the signs negative keeps the same configuration of results, though it does cause one or more path estimate biases to switch (symmetrically) from positive to negative. This all suggests a slightly different reading of the Mela and Kopalle paper. Although they focused on the impact of omitted but correlated variables, behavior simila to their findings can be created without omitted variables, by adding measurement error and collinearity. The impacts Mela and Kopalle seek to show have the same relationship as those pointed out above from Green and Kiernan’s equations.

Table C1. Behavior of Proportional Inconsistencies (Green and Kiernans’s PI) (Assuming |β<sub>1</sub>| > |β<sub>2</sub>|)

<table><tr><td>Focus on PIβ1 or PIβ2</td><td>Decision Condition</td><td>Relationship of |ρ12* β2/β1| to “1”</td><td># Minus Signs among ρ12, β2, β1</td><td>What Happens to 1 - (ρ12* β2/β1)</td><td>What Happens to PIβ1 or PIβ2</td><td></td></tr><tr><td>PIβ1=(1-ρ1)/(1-ρ122)* [1-(ρ12* β2/β1)]</td><td>none</td><td>|ρ12* β2/β1| always &lt; 1</td><td>0 or 2 Minus signs</td><td>(ρ12*β2/β1) subtracts from one</td><td>PIβ1 is always positive</td><td>|β1^| is an under-estimate of |β1|</td></tr><tr><td></td><td></td><td></td><td>1 or 3 Minus signs</td><td>(ρ12*β2/β1) adds to one</td><td>PIβ1 is more positive</td><td>|β1^| is a bigger underestimate of |β1|</td></tr><tr><td>PIβ2=(1-ρ1)/(1-ρ122)* [1-(ρ12*β1/β2)]</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>|ρ12*β1|&lt; |β2|(|β2| is relatively large)</td><td>|ρ12* β1/β2| always &lt; 1</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>0 or 2 Minus signs</td><td>(ρ12* β1/β2) subtracts from one</td><td>PIβ2 is always positive</td><td>|β2^| is an underestimate of |β2|</td></tr><tr><td></td><td></td><td></td><td>1 or 3 Minus signs</td><td>(ρ12* β1/β2) adds to one</td><td>PIβ2 is more positive</td><td>|β2^| is a bigger underestimate of |β2|</td></tr><tr><td></td><td>|ρ12* β1|&gt; |β2|(β2 is relatively small)</td><td>|ρ12*β1/β2| always &gt; 1</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>0 or 2 minus signs</td><td>(ρ12* β1/β2) subtracts from one</td><td>PIβ2 is always negative</td><td>|β2^| is an overestimate of |β2|</td></tr><tr><td></td><td></td><td></td><td>1 or 3 Minus signs</td><td>(ρ12* β1/β2) adds to one</td><td>PIβ2 is positive</td><td>|β2^| is an under-estimate of |β2|</td></tr></table>

## Appendix D

## Correcting for M+ME Biases — Step by Step

When might an analysis be in the M+ME danger zone? For the sake of illustration, consider the model and correlations shown in Figure D1. Here we have nine constructs connected by hypothesized paths, showing selected (overt) path estimates and selected (overt) inter-construct correlations. How would a researcher recognize that any particular pair of these constructs is near enough to the M+ME danger zone to possibly require the correction? Note that Figures 3 through 7 and Figure 9 in the paper show underlying correlations. If a researcher compares their own results to Figures 3 through 7, they need to use equation 2 to convert overt correlations to underlying correlations. Note also that the M+ME Correction Application requires “overt” correlations, not underlying correlations.

![](/api/attachments/ZMPN82TN/fulltext/images/2a93cde892585f4946884922c3671225f10823039999c2f1c55a599aede01458.jpg)  
Figure D1. Overt Correlations in Hypothetical Model with N = 200, Reliability = .80

Step One: Identify Correlations of Interest. First, recognize that in Figure D1, only the seven overt correlations or paths with a value (or the word “small”) added to the link are of concern to us. Note that the path between G and H is of concern even though it is modeled as a path rather than a correlation, because G and H are correlated, and both participate in the regression equation predicting construct I. Note also that even if the overt correlation between construct C and construct D were very high, say.72, that would not be of concern, because constructs C and D do not participate in the same regression equation.

Categorize all high correlation situations into two groups. Notice that the upper part of the figure shows two of what we will call an “isolated” high correlation—only two highly correlated constructs participating in the same regression. The bottom part of Figure D1 shows a different situation—three highly correlated constructs all participating in the same regression, specifically D, E, and F are correlated and all predict H. This latter situation we will call a “combination” of high correlations. These “combination” situations present more of a challenge than the isolated high correlation and will be dealt with in Appendix E.

Step Two: Assess and perhaps correct the “isolated” correlations of interest. There are two isolated correlations in Figure D1 that should be examined: A and B predicting G, and G and H predicting I (both having an overt correlation of .40).

To rule out obviously non-problematic correlated pairs, one can do a quick (very approximate) back of the envelope calculation to determine if there is even any cause for concern, as follows. For example, if the reliability of constructs A and B in Figure D1 is .80, using equation 2, we conclude that the underlying correlations are about .50 for A with B (and for G with H). To get a general feeling for whether A and B predicting G might involve a substantive M+ME bias, we can refer to Figure 7 (rather than Figures 4A or 4B, because the N is 200). If the sample size were closer to n = 100, then Figures 4A or 4B might be appropriate.

In Figure 7 we see that an analysis with a $\beta _ { \mathrm { l } }$ about .292, sample size of N = 200, and an underlying correlation of .50 gives us about a 7% likelihood of excessive false positives, near the top of the 95% confidence interval around 5% false positives. This suggests that we should use the M+ME Correction Application to check the possibility of an M+ME bias.

The M+ME correction application will correct for the bias to the VIF, correct the path biases, and adjust the standard deviations for the corrected path values. This downloadable application is available on the MISQ web site (Online Supplements: M+ME Correction Application). Figure 8 of the article proper displays the front end of the application, showing the input required (on the left side) and the results of the correction calculations on the right side. First, be sure that you are using the standardized regression (or PLS) results. Though here we will assume that $\beta _ { \mathrm { l } }$ is the dominant path (the construct whose path has the highest absolute value), that is not necessary. With this understanding, enter the regression results for the two (overt) path estimates from regression or PLS, the two overt t-statistics, the two reliabilities (for X1 and X2) and the overt (or apparent) correlation between X1 and X2. The corrected path values, t-statistics and p values will be displayed by the M+ME correction application. Because it is relatively easy to use, the M+ME correction application can be used without referring to the figure in the paper as a “back-of-the-envelope” approximation.

Table D1 shows the results of applying the corrections. The first set of rows in Table D1 shows the A and B predicting G situation when it is entered into the M+ME correction application. The input values are to the left, and the corrected path values and t-statistics are shown to the right. In this case the path correction has increased the B  G path slightly (to .184) and the recalculated standard deviation has decreased the t-statistic a good bit (to 1.561). The result is that the corrected B to G path is no longer statistically significant.

The second “isolated correlation” from Figure D1 is G and H predicting I, with G and H correlated at .40. This situation is depicted in the second set of rows of Table D1. There the H to I path is shown to be statistically significant even with the M+ME correction, though note that the t-statistic has dropped from 2.90 to 2.02. Finally, the third example in Table D1 has the same input as the second, but a correlation of .60 instead of .40. This increase in multicollinearity takes its toll, and under these circumstances the H to I path is no longer statistically significant after we apply the M+ME correction.

Note that in all three examples, the uncorrected results show that the questionable path is statistically significant (i.e., different from zero with 95% confidence). In two of those, the correction shows that the questionable path is not actually significant, and should not be considered different from zero.

We suggest that there is no place for optimists in questions of statistical significance. When M+ME for a particular path is not clearly ruled out by displays such as those in Figures 4A, 4B, or 7, the correction should be applied by inputting the relevant data into the M+ME correction application. Applying this correction to regression or PLS results when M+ME is not a problem will not create new problems. Instead, it will give the researcher a more accurate value for the t-statistic.

Table D1. Input and Output (Corrected Path Values and t-statistics) for the M+ME Correction Application

<table><tr><td></td><td colspan="8">Needed Input</td><td colspan="5">Output</td></tr><tr><td>Relation-ship</td><td>N</td><td> $β^1$ </td><td> $β^2$ </td><td> $β^1t$ </td><td> $β^2t$ </td><td> $\alpha_1$ </td><td> $\alpha_2$ </td><td> $\rho_{12}$ </td><td>Path</td><td>Significance Without Corrections</td><td>Corrected Path Est</td><td>Corrected t-stat</td><td>Significance with path and VIF correction</td></tr><tr><td rowspan="2">A, B → G;  $\rho_{a,b} = .40$ </td><td>200</td><td>.257</td><td>.170</td><td>3.50</td><td>2.05</td><td>.80</td><td>.80</td><td>.40</td><td>B→G</td><td>yes</td><td>0.184</td><td>1.56</td><td>Not Sig!</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>A→G</td><td>yes</td><td>0.314</td><td>3.00</td><td>yes</td></tr><tr><td rowspan="2">G,H → I;  $\rho_{g,h} = .40$ </td><td>200</td><td>.462</td><td>.240</td><td>2.89</td><td>2.90</td><td>.80</td><td>.80</td><td>.40</td><td>H→I</td><td>yes</td><td>0.243</td><td>2.02</td><td>yes</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>G→I</td><td>yes</td><td>0.576</td><td>2.55</td><td>yes</td></tr><tr><td rowspan="2">G,H → I;  $\rho_{g,h} = .60$ </td><td>200</td><td>.462</td><td>.240</td><td>2.89</td><td>2.90</td><td>.80</td><td>.80</td><td>.60</td><td>H→I</td><td>yes</td><td>0.179</td><td>1.01</td><td>Not Sig!</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>G→I</td><td>yes</td><td>0.623</td><td>2.03</td><td>yes</td></tr></table>

## Appendix E

## The Challenge of Combinations of High Correlations

In the lower part of Figure D1 we see a “combination” of three constructs (D, E, and F) connected with one high and one only moderately high overt correlation, both of which affect the E to H path (that is .380 and .320 overt correlations, suggesting underlying correlations of .475 and .400). The third overt correlation (between D and F) is .304, suggesting an underlying value of .380. We acknowledge at the outset that we do not fully understand all the issues relating to multiple high correlations situations. The problem is that Green and Kiernan’s (1989) equations do not extend to three intercorrelated constructs. In fact both pairs of correlated constructs have an impact on the estimated E to H path estimate and their impact could be additive or in some cases more than additive. This means that except for turning to CB-SEM, we do not have an effective way to correct for the path biases in regression or PLS, when faced with such a situation. This is an area where additional research would be quite valuable.

A key insight in understanding combinations of high correlations is that there are three general archetypes of the underlying “causes” of these three way configurations of correlations, as shown in Figure E1. Of course the cause may contain a mixture of several of these types, plus the possibility of direct causal links between the focal constructs (in this case Constructs D, E or F.

On the top left of Figure E1 (Panel A, single underlying cause) we see that the correlations between all three constructs are due to relationships with a single underlying construct. As it turns out, there is a reasonable correction approach when the combination of high correlations is produced by a single underlying construct. In those situations the M+ME biases can be considered additive, and it is possible to correct for the largest correlation as we have shown in the previous section for isolated high correlations. Once this is done, the researcher can determine (very roughly) from the size of the remaining correlation (for example using Figures 3, 4, or 7), whether that remaining correlation by itself would put the analysis into the M+ME danger zone. If not, then the single correlation correction method is sufficient. One definitely should not apply the M+ME correction application a second time.

Unfortunately we know of no way to determine, from the data a researcher would have, whether a combination of correlations was caused by two, or even three, background constructs. Thus we have no way to safely assume a single underlying cause. This poses a difficult problem.

In Figure E2 we show the uncorrected results from data generated by each of the archetypal possible causes, along with the results after the highest correlation has been corrected. The figure does show that correcting for the dominant correlation always improves the situation. But unfortunately, even with the correction, some of the lines are well above the 95% confidence interval around .05.

Since the researcher cannot know which situation they are working with, and since it is not appropriate to optimistically “assume the best possible situation” in hypothesis testing, we cannot recommend using the M+ME correction with combinations of high correlations.

![](/api/attachments/ZMPN82TN/fulltext/images/f7319e3bfd45c18de40c7698c2f048cdb3eaaac5164bab39f287816a9ff39b80.jpg)  
Panel A. Single Underlying Cause

![](/api/attachments/ZMPN82TN/fulltext/images/5bf8b9679bb383c343d8ea79702bc67f26fbcefa5fe12783e56f851070dfecbb.jpg)  
Panel B. Two Distinct Underlying Causes

![](/api/attachments/ZMPN82TN/fulltext/images/59dd2d57392b89d45f81fc1c822e02f1df7593c2dcd85d48840e17aaa13b0f59.jpg)  
Panel C. Three Distinct Underlying Causes  
Figure E1. Three Different Archetypal Causes of Combinations of High Correlations

![](/api/attachments/ZMPN82TN/fulltext/images/ff41596f4ec78e5667371b48ae557f3a750426ab2bbdbd2a1f6607e03a208440.jpg)  
No Correction Versus Dominant Correlation Corrected, $\alpha = . 8 0 , \mathsf { N } = 2 0 0 , \mathsf { X } 1 \to \mathsf { Y } 1 = . 4 2 0$

Figure E2. Regression False Positives Results from Combinations of High Correlations

![](/api/attachments/ZMPN82TN/fulltext/images/45a9c9ff11af9871f4a74af9c201c53a9ea2ff93d10cc97fc2d07038d63f20be.jpg)

α = .80, N = 200, X1  Y1 = .420

Figure E3. CB-SEM False Positives Results From Combinations of High Correlations

One safe method to use in combinations of high correlation situations would be to convert the analysis over to CB-SEM. Figure E3 shows the results from that method. We see that with CB-SEM, the large numbers of false positives never appear in the first place.<sup>7</sup> Though it may require extra work for those not well-versed in the use of CB-SEM, this clearly provides a solution to the combination of high correlation M+ME situation. Alternatively (or in conjunction), it may be appropriate to change the underlying model (e.g., using higher-order constructs).

As stated earlier, we do not fully understand the combinations of high correlation situation. Because combinations of high correlations do appear in IS research, additional research in this area could be helpful.

## Appendix F

## Testing Whether M+ME False Positives Could Be Due to Discriminant Validity Problems

One alternative explanation for the results we obtained might be framed within the larger context of measurement model misspecification, and specifically the presence of a lack of discriminant validity among constructs. To address this possibility, we conducted some ancillary analyses. We found the following. First, using chi square difference tests of discriminant validity and one of our Monte Carlo simulation datasets (500 samples each of N = 100, reliability = .80, ρ = .80) we did find evidence of discriminant validity problems. Specifically, 56 (or about 10%) of the samples had discriminant validity problems, as compared to 59 (also about 10%) samples with M+ME false positives. Although these numbers are quite close, only 4 samples had both discriminant validity problems and excessive false positives.

We note further that although both false positives and discriminant validity problems are exacerbated by increasing correlations and decreasing reliabilities, those two phenomena react quite differently to increasing sample size. As shown in Figure F1, larger sample sizes decrease discriminant validity problems to virtually zero, while they increase M+ME false positives substantially. Thus it is clear that the two phenomena share some causal factors but are actually quite distinct. Knowing that a dataset suffers from one of these phenomena does not provide much knowledge about the likelihood that it also suffers from the other.

![](/api/attachments/ZMPN82TN/fulltext/images/bf83c1dea5906ec85dbc63b0a4a06fe5651967b868a882c7a42a25a9ed2f663a.jpg)

$$
\left(\beta_ {1} \text {   path } = . 2 9 2, N = 1 0 0, \alpha = . 8 0, \rho_ {1 2} = . 8 0\right)
$$

Figure F1. Sample Size and Discriminant Validity Problems Versus M+ME False Positives

## Appendix G

## Pictorial Depiction: M+ME Impact on Regression and CB-SEM

Some readers may find it helpful to see a graphical representation of the impact of M+ME on regression and CB-SEM results for 500 samples as in our Monte Carlo simulations. Throughout we will be looking at an underlying X1 to Y1 path of .600, an X2 to Y1 path of zero, a sample size of N = 200, and reliability of .80 for both X1 and X2. For both regression and CB-SEM, the average path estimates across the 500 samples is shown below in Figures G1, G2, and G3, for three different scenarios. Along with the average path estimates, also shown is a representation of the distribution of those 500 estimates around that average estimate. The distribution curves shown comes from calculating the standard deviation of the 500 path estimates, and displaying them as a curve anchored at the average path estimate plus 2 times the standard deviation, and the average path estimate minus 2 times the standard deviation.

We first look at the results when the underlying reality is a zero correlation between X1 and X2. That is, when there is no M+ME. We will then shift our focus to the situation where M+ME is extreme, with a correlation between X1 and X2 of .90.

Figure G1 shows the results for β (a zero path) when there is no correlation between X1 and X2. The average $\beta _ { 2 }$ path estimates for regression and CB-SEM are both about zero, and the distribution curves for both span from about -1.3 to + 1.5. These results are what we might have expected.

In Figure G2 we show the results when the correlation between X1 and X2 is .90, a very high correlation. Though M+ME will rarely or never be this extreme in practice, this scenario allows us to see more clearly what the specific effects of M+ME are, and why this is a problem. Under these conditions, CB-SEM returns a path estimate for β of near zero, and a standard deviation that is about 7 times as large as it was when ${ \boldsymbol \rho } _ { 1 2 }$ was .00 (.497 versus .068). The very large spread of the β path estimations suggests that the high correlation between X1 and X2 makes the resulting path estimates very dependent upon random variance in the data. CB-SEM recognizes this and increases the standard deviation it uses appropriately.

For regression under these conditions, the average path estimate is quite skewed (from near zero at ${ \rho } _ { 1 2 } = 0$ to a value of .175 at ${ \rho } _ { 1 2 } = . 9 0$ . This is as predicted by the Green and Kiernan equations. The distribution around the .175 based on the standard deviation of the regression estimates is about as wide as in Figure G1, but now shifted up, so that most of the estimates are now significantly different from zero. This is of course misleading, since the true path is zero. This makes the M+ME bias very apparent.

In Figure G3, we have used the Green and Kiernan equations to correct for the M+ME path bias in regression, and at the same time corrected the standard deviation values in regression, also based on the VIF and Green and Kiernan equations. These corrections have removed the path bias, and now the bias and the dispersion of the path values are roughly equal for regression and for CB-SEM, and both reflect the uncertainly created by the large correlation between X1 and X2.

![](/api/attachments/ZMPN82TN/fulltext/images/bab90ae3fd3a6827cfa5fc5aa319ce6e90f91eea5036da38c8b8ea3b5504e9c8.jpg)  
Figure G1. Regression and CB-SEM When Correlation Between X1 and X2 is 0.00

![](/api/attachments/ZMPN82TN/fulltext/images/c1b3063bd6d8d7b047de4ccbc723cbb66cc0255f3f7e9cf6762d4a5af398fd92.jpg)  
Figure G2. Regression and CB-SEM When Correlation Between X1 and X2 is 0.90

![](/api/attachments/ZMPN82TN/fulltext/images/c3672010d578f9fc96265cadc24f04612fd787e687198ed15bd991f4afc8a980.jpg)  
Figure G3. Regression and CB-SEM When Correlation Between X1 and X2 is 0.90, After VIF and Green and Kiernan Path Bias Corrections

## References

Goodhue, D., Lewis, W., and Thompson, R. 2011. “A Dangerous Blind Spot in IS Research: False Positives Due to Multicollinearity Combined with Measurement Error,” in Proceedings of the 17<sup>th</sup> Americas Conference on Information Systems, Detroit, MI, August 4-7.

Green, C. J., and Kiernan, E. 1989. “Multicollinearity and Measurement Error in Econometric Financial Modelling,” The Manchester School (57:4), pp. 357-369.

Johnston, J. 1972. Econometric Methods (2<sup>nd</sup> ed.), New York: McGraw-Hill.

Mela, C., and Kopalle, P. 2002. “The Impact of Collinearity on Regression Analysis: the Asymmetric Effect of Negative and Positive Correlations,” Applied Economics (34:6), pp. 667-677.

Mooney, C. Z., and Duval, R. D. 1993. Bootstrapping: A Nonparametric Approach to Statistical Inference, Beverly Hills, CA: Sage Publications.

# A MULTICOLLINEARITY AND MEASUREMENT ERROR STATISTICAL BLIND SPOT: CORRECTING FOR EXCESSIVE FALSE POSITIVES IN REGRESSION AND PLS

Dale L. Goodhue Terry College of Business, MIS Department, University of Georgia, Athens, GA 30606 U.S.A. {dgoodhue@terry.uga.edu}

William Lewis {william.w.lewis@gmail.com}

Ron Thompson School of Business, Wake Forest University, Winston-Salem, NC 27109 U.S.A. {thompsrl@wfu.edu}

## Appendix A

Deriving Equations for M+ME Biases and for t-statistic Overestimations

## Determining the Impact of VIF Bias on the t-statistic

Consider first the situation where we have no measurement error. Using standard equations for the estimated standard error of $\beta _ { 2 }$ from any regression textbook, an unbiased and consistent estimate of the standard error is

$$
\mathrm{s} ^ {2} = \Sigma \varepsilon_ {\mathrm{i}} ^ {2} / (\mathrm{N-K})\tag{A1-1}
$$

and the estimate of the variance of $\beta _ { 2 }$ is

$$
\operatorname{Var} \left(\beta_ {2} ^ {\wedge}\right) = \left[ s ^ {2} / \Sigma x _ {2 i} ^ {2} \right] * \left[ 1 / \left(1 - \rho_ {1 2 \text { Underlying }} ^ {2}\right) \right]\tag{A1-2}
$$

When the error terms are normally distributed, the following has a t distribution:

$$
\mathrm{t} - \text { stat } = (\beta_ {2} ^ {\wedge} - \beta_ {2}) / \{\text { Var } (\beta_ {2} ^ {\wedge}) \}. ^ {5} \quad \sim t _ {\text { N - K }}\tag{A1-3}
$$

Substituting in the equations for Var ( β<sup>^</sup><sub>2</sub>) and $s ^ { 2 }$ from above (A1-1 and A1-2), we can see the impact of correlated predictor variables on the t-stat.

$$
\begin{array}{l l} \text {t - stat} = (\beta_ {2} ^ {\wedge} - \beta_ {2}) & / \quad \{\left[ s ^ {2} / \Sigma x _ {2 i} ^ {2} \right] * [ 1 / (1 - \rho_ {1 2 \text {Underlying}} ^ {2}) ] \} ^ {- 5} \\ \text {t - stat} = (\beta_ {2} ^ {\wedge} - \beta_ {2}) & / \quad \{\left[ \{\Sigma \varepsilon_ {i} ^ {2} / (N - K) \} \right] / \Sigma x _ {2 i} ^ {2} ]) * [ 1 / (1 - \rho_ {1 2 \text {Underlying}} ^ {2}) ] \} ^ {- 5} \end{array}
$$

Rearranging terms:

$$
\text { t - stat } = \quad (\beta_ {2} ^ {\wedge} - \beta_ {2}) \qquad / \qquad \{[ \Sigma \epsilon_ {i} ^ {2} / \{(N - K) * \Sigma x _ {2 i} ^ {2} \} ] * [ 1 / (1 - \rho_ {1 2 \text { Underlying }} ^ {2}) ] \}. ^ {5}
$$

Squaring both sides:

$$
\begin{array}{l l} (t - \text { stat }) ^ {2} = (\beta_ {2} ^ {\wedge} - \beta_ {2}) ^ {2} & / \{\left[ \Sigma \varepsilon_ {i} ^ {2} / \{(N - K) * \Sigma x _ {2 i} ^ {2} \} \right] * [ 1 / (1 - \rho_ {1 2 \text { Underlying }} ^ {2}) ] \} \\ (t - \text { stat }) ^ {2} = (\beta_ {2} ^ {\wedge} - \beta_ {2}) ^ {2} & * \{\left[ (N - K) * \Sigma x _ {2 i} ^ {2} \right] / \Sigma \varepsilon_ {i} ^ {2} ] * [ (1 - \rho_ {1 2 \text { Underlying }} ^ {2}) / 1 ] \} \\ (t - \text { stat }) ^ {2} = (\beta_ {2} ^ {\wedge} - \beta_ {2}) ^ {2} & * \{\left[ (N - K) * \Sigma x _ {2 i} ^ {2} * (1 - \rho_ {1 2 \text { Underlying }} ^ {2}) \right] / \Sigma \varepsilon_ {i} ^ {2} \end{array}
$$

Rearranging terms:

$$
\begin{array}{l} (t - \text { stat }) ^ {2} = \left\{\left[ (\beta_ {2} ^ {\wedge} - \beta_ {2}) ^ {2} * (N - K) * \Sigma x _ {2 i} ^ {2} * (1) / \Sigma \varepsilon_ {i} ^ {2} \right. \right\} \\ - \left\{\left[ (\beta_ {2} ^ {\wedge} - \beta_ {2}) ^ {2} * (N - K) * \Sigma x _ {2 i} ^ {2} * (\rho_ {1 2 \text { Underlying }} ^ {2}) \right] / \Sigma \varepsilon_ {i} ^ {2} \right\} \end{array}\tag{A1-4}
$$

Note that the first half of equation (A1-4) is the squared t-statistic if there were no correlation between $\mathrm { X } _ { 1 }$ and $\mathrm { X } _ { 2 } .$ . The second half is the correction for when there is a correlation (at this point all assuming no measurement error).

As suggested by Goodhue et al. (2011), the problem with the above is that the estimate for the correlation $\left( \rho _ { \mathrm { 1 2 U n d e r l y i n g } } \right)$ assumes perfect measurement (i.e., that the $\mathrm { X } _ { \mathrm { i } }$ values have no random measurement error). In regression, estimates of the two constructs are based on averaged or summed indicator scores, and any estimate of the $\rho _ { \mathrm { 1 2 U n d e r l y i n g } }$ correlation will be attenuated (reduced) by the random measurement error, as shown below:

$$
\rho_ {1 2 \text { Underlying }} = \rho_ {1 2 \text { Overt }} / (\alpha_ {1} * \alpha_ {2}) ^ {1 / 2}
$$

(Equation 2 from the paper proper)

(A1-5)

When we do have measurement error, $\rho _ { \mathrm { 1 2 - O v e r t } }$ is not equal to $\rho _ { \mathrm { 1 2 U n d e r l y i n g } } .$ When the t-stat calculated by regression has not been corrected for attenuation, A1-4 becomes:

$$
\begin{array}{r l} (t \text {-stat} _ {\text {Overt}}) ^ {2} _ {\text {(incorrect)}} = & \{[ (\beta_ {2} ^ {\wedge} - \beta_ {2}) ^ {2} * (N - K) * \Sigma x _ {2 i} ^ {2} ] / \Sigma \varepsilon_ {i} ^ {2} \} \\ & - \{[ (\beta_ {2} ^ {\wedge} - \beta_ {2}) ^ {2} * (N - K) * \Sigma x _ {2 i} ^ {2} * (\rho_ {1 2 \text {-Overt2}}) ] / \Sigma \varepsilon_ {i} ^ {2} \} \end{array}\tag{A1-6}
$$

Below (in equation A1-7) we show how the t-statistic value is biased by the incorrect ${ \mathrm { V I F } } ,$ assuming we know the reliabilities for $\mathrm { X } _ { 1 }$ and $\mathrm { X } _ { 2 }$ The first two lines are equation A1-6, assuming there is no correction to the VIF for random measurement error. The third line adds back the amount that was incorrectly subtracted out to correct for the X and X correlation (incorrect because not taking into account random measurement error attenuation), and then the fourth line subtracts the proper amount to correct for $\mathrm { X } _ { 1 }$ and $\mathrm { X } _ { 2 }$ correlation (taking into account random measurement error attenuation).

$$
\begin{array}{l} (t \text {-stat} _ {\text {Corrected}}) ^ {2} = \{[ (\beta_ {2} ^ {\wedge} - \beta_ {2}) ^ {2} * (N - K) * \Sigma x _ {2 i} ^ {2} ] / \Sigma \varepsilon_ {i} ^ {2} \} \\ \quad - \{[ (\beta_ {2} ^ {\wedge} - \beta_ {2}) ^ {2} * (N - K) * \Sigma x _ {2 i} ^ {2} * (\rho_ {1 2 \text {-Overt}} ^ {2}) ] / \Sigma \varepsilon_ {i} ^ {2} \} \\ \quad + \{[ (\beta_ {2} ^ {\wedge} - \beta_ {2}) ^ {2} * (N - K) * \Sigma x _ {2 i} ^ {2} * (\rho_ {1 2 \text {-Overt}} ^ {2}) ] / \Sigma \varepsilon_ {i} ^ {2} \} \\ \quad - \{[ (\beta_ {2} ^ {\wedge} - \beta_ {2}) ^ {2} * (N - K) * \Sigma x _ {2 i} ^ {2} * (\rho_ {1 2 \text {Underlying2}}) ] / \Sigma \varepsilon_ {i} ^ {2} \} \end{array}\tag{A1-7}
$$

The amount by which regression is overestimating the “t-statistic squared” due to the incorrect VIF is the following. This is the last two terms of equation A1-7 with the signs (and order) reversed:

$$
\begin{array}{l} (t - \text {stat}) ^ {2} \text {overestimation} = (t - \text {stat} _ {\text {Overt}}) ^ {2} - (t - \text {stat} _ {\text {Corrected}}) ^ {2} = \\ \quad + \{[ (\beta_ {2} ^ {\wedge} - \beta_ {2}) ^ {2} * (N - K) * \Sigma x _ {2 i} ^ {2} * (\rho_ {1 2 \text {Underlying} 2}) ] / \Sigma \varepsilon_ {i} ^ {2} \} \\ \quad - \{[ (\beta_ {2} ^ {\wedge} - \beta_ {2}) ^ {2} * (N - K) * \Sigma x _ {2 i} ^ {2} * (\rho_ {1 2 - \text {Overt}}) ^ {2}) ] / \Sigma \varepsilon_ {i} ^ {2} \} \end{array}\tag{A1-8}
$$

By inserting the square of equation A1-5 for the ${ \rho } _ { 1 2 \mathrm { U n d e r l y i n g } } ^ { 2 }$ term in A1-8, we get the following:

$$
\begin{array}{l} \left(\mathrm{t-stat}\right) ^ {2} \text {overestimation} = \left[ \left(\beta_ {2} ^ {\wedge} - \beta_ {2}\right) ^ {2} (\mathrm{N} - \mathrm{K}) \Sigma \mathrm{x} _ {2 \mathrm{i}} ^ {2} \left(\rho_ {1 2 \mathrm{Overt}} ^ {2}\right) / \left(\alpha_ {1} * \alpha_ {2}\right) \right] / \Sigma \varepsilon_ {\mathrm{i}} ^ {2} \\ - \left[ \left(\beta_ {2} ^ {\wedge} - \beta_ {2}\right) ^ {2} (\mathrm{N} - \mathrm{K}) \Sigma \mathrm{x} _ {2 \mathrm{i}} ^ {2} \left(\rho_ {1 2 \mathrm{Overt}} ^ {2}\right) \right] / \Sigma \varepsilon_ {\mathrm{i}} ^ {2} \end{array}\tag{A1-9}
$$

Gathering common terms, the amount the t-statistic squared in regression is overestimated due to the VIF bias when there are both correlated predictors and random measurement error is

$$
(t - \text { stat }) ^ {2} \text {   overestimation } = [ (1 / (\alpha_ {1} * \alpha_ {2})) - 1 ] * [ (\beta_ {2} ^ {\wedge} - \beta_ {2}) ^ {2} (N - K) \Sigma x _ {2 i} ^ {2} (\rho_ {1 2 - 0 \text {vert}} ^ {2}) ] / \Sigma \varepsilon_ {i} ^ {2}\tag{A1-10}
$$

Equation A1-10 is helpful in seeing the impact of various factors on the t-statistic overestimation due to bias in the VIF. It was one of the insights that led to our hypothesis generation. Of course it does not tell the full story, which would also require taking into account the path bias embodied in equations 6 and 7 from the paper, and determining the corrected standard deviation for the corrected estimated underlying path. We explain the logic of that below.

## Correcting the Path Estimates for the M+ME Bias

Johnston’s (1972) equations. Consider the following regression equation:

$$
\mathrm{Yi} = \beta_ {0} + \beta_ {1} \mathrm{X} _ {1 \mathrm{i}} + \beta_ {2} \mathrm{X} _ {2 \mathrm{i}} + \dots . + \beta_ {\mathrm{k}} \mathrm{X} _ {\mathrm{ki}} + \varepsilon_ {\mathrm{i}}\tag{A1-11}
$$

Though the essential results extend to the full equation above, for simplicity we will ignore all the $\beta _ { \mathrm { k } } X _ { \mathrm { k i } }$ terms above when k is greater than 2, giving

$$
\mathrm{Yi} = \beta_ {0} + \beta_ {1} \mathrm{X} _ {1 \mathrm{i}} + \beta_ {2} \mathrm{X} _ {2 \mathrm{i}} + \varepsilon_ {\mathrm{i}}\tag{A1-12}
$$

Following Johnston (1972, pp. 160-162), if we first look at the impact of multicollinearity on bias in the regression path estimates of $\beta _ { \mathrm { l } }$ and β (that is, ${ \beta } _ { 1 } ^ { \wedge }$ and β<sup>^</sup>), we see the following:

$$
\beta_ {1} ^ {\wedge} - \beta_ {1} = \Sigma u x _ {1} - (\rho_ {1 2} * \Sigma u v) / (1 - \rho_ {1 2} ^ {2})\tag{A1-13}
$$

and

$$
\beta_ {2} ^ {\wedge} - \beta_ {2} = (\Sigma \mathrm{uv}) / (1 - \rho_ {1 2} ^ {2})\tag{A1-14}
$$

where u is the vector of error terms in ${ \mathrm { Y } } ;$ v is the vector of error terms in the equation for $\mathrm { X } _ { 2 }$ as a function of $\mathrm { X } _ { \mathrm { i } } ;$ and ${ \boldsymbol \rho } _ { 1 2 }$ is the underlying correlation between $\mathrm { X } _ { 1 }$ and $\mathrm { X } _ { 2 }$

It is not necessary for the reader to understand the two equations in depth, but only to understand that mathematically, when $\mathrm { X } _ { 1 }$ and $\mathrm { X } _ { 2 }$ are correlated and the error terms u and v are non-zero,<sup>2</sup> regression estimates of ${ \bf \widehat { \mathbf { \beta } } } _ { 1 } ^ { \setminus }$ and $\boldsymbol { \beta } _ { 2 } ^ { \setminus }$ will be biased away from the underlying value (the true value absent any systematic error). We note that as $\rho _ { 1 2 }$ increases, the size of the negative bias for ${ \beta } _ { 1 } ^ { \wedge }$ increases. Likewise, as $\rho _ { 1 2 }$ increases, th size of the positive bias for $\boldsymbol { \beta } _ { 2 } ^ { \setminus }$ increases. Johnston goes on to say that a large correlation between independent variables ${ } ^ { \mathfrak { s c } } { } _ { \mathrm { i s } }$ thus likely to produce large and opposite errors in ${ \beta } _ { \mathrm { l } } ^ { \wedge }$ and $\beta _ { 2 } ^ { \cdot } , \mathrm { i f } \beta _ { 1 } ^ { \cdot }$ underestimates $\beta _ { \mathrm { 1 } } ,$ then $\beta _ { 2 } ^ { \setminus }$ is likely to overestimate $\beta _ { 2 }$ and vice versa. It is thus very important that the standard errors should alert one to the presence of multicollinearity” (p. 162).

Green and Kiernans’s (1989, pp. 359-363) equations. Green and Keirnan carried the analysis of the impact of multicollinearity and random measurement error on regression path biases further than Johnston. In particular, Green and Kiernan make a clear distinction between what we are calling the $^ { \mathfrak { c } \mathfrak { c } } \mathrm { o v e r t } ^ { \mathfrak { p } } \left( \mathfrak { p } _ { 1 2 \mathrm { o v e r t } } \right)$ and the $\mathrm { ^ { * } u n d e r l y i n g } ^ { \mathrm { \prime * } } \left( \mathrm { \pmb { p } } _ { \mathrm { 1 2 u n d e r l y i n g } } \right)$ correlation—the overt correlation is the correlation based on the “signalplus-noise” or the correlation between the “error containing” measures of the two constructs, while the “underlying” correlation is the correlation based only on the “signal,” without the noise (Green and Kiernan 1989, p. 360.)

<sup>1</sup>We note that it would be incorrect to suggest that we can take the square root of both sides of equation (A1-10) and therefore determine that

$$
\text { t - stat   overestimation } = \{[ (1 / \alpha_ {1} * \alpha_ {2}) - 1 ] * [ (\beta_ {2} ^ {\wedge} - \beta_ {2}) ^ {2} (\mathrm{N-K}) \Sigma x _ {2 i} (\rho_ {1 2 - \text { Overt }} ^ {2}) ] / \Sigma \varepsilon_ {i} ^ {2} \}. 5\tag{not correct}
$$

The (t-stat)<sup>2</sup> overestimation term is not the same as [t-stat overestimation]<sup>2</sup>.

Under fairly general conditions (equal reliability $\{ { \bf { \alpha } } \alpha _ { 1 } = \alpha _ { 2 } \}$ for $\beta _ { \mathrm { l } }$ and $\beta _ { 2 ; } \beta _ { 1 } > 0 )$ , Green and Keirnan gave equations for what they call “proportional inconsistencies” or $\mathrm { ( P I _ { j } ) }$ defined as (β – plim $\beta _ { \mathrm { i } } ^ { \mathrm { \wedge } } \mathrm { ) / \beta _ { \mathrm { i } } }$ . If PI is positive, then plim $\beta _ { \mathrm { i } } ^ { \wedge }$ is less than $\beta _ { \mathrm { i } } \left( \mathrm { i } . \mathrm { e } _ { \cdot } \right.$ , an underestimation); If $\mathrm { P I } _ { \mathrm { i } }$ is negative, then plim $\beta _ { \mathrm { i } } ^ { \wedge }$ is greater than $\beta _ { \mathrm { i } } ; ( \mathrm { i } . \mathrm { e } .$ ., an overestimation). We will reproduce two of their equations, folding in several other additional reasonable assumption that are appropriate to our analysis here.<sup>3</sup> With this assumption Green and Kiernan’s equations for the proportional inconsistency show us more about the impact of M+ME on regression estimates than Johnston’s treatment.

$$
\mathrm{PI} _ {\beta 1} = \left(\beta_ {1} - \operatorname{plim} \beta_ {1} ^ {\wedge}\right) / \beta_ {1} = \left[ \left(1 - \alpha_ {1}\right) / \left(1 - \rho_ {1 2} ^ {2}\right) \right] * \left[ 1 - \left(\rho_ {1 2} * \left(\beta_ {2} / \beta_ {1}\right)\right) \right] \quad (\text { Equation   6   repeated }) \tag {A1-15}
$$

$$
\mathrm{PI} _ {\beta 2} = \left(\beta_ {2} - \operatorname{plim} \beta_ {2} ^ {\wedge}\right) / \beta_ {2} = \left[ \left(1 - \alpha_ {1}\right) / \left(1 - \rho_ {1 2} ^ {2}\right) \right] * \left[ 1 - \left(\rho_ {1 2} * \left(\beta_ {1} / \beta_ {2}\right)\right) \right] \quad (\text { Equation   7   repeated })\tag{A1-16}
$$

Here $\rho _ { 1 2 }$ is the $\mathbf { \bar { \Psi } } _ { 0 } ^ { \mathsf { c c } } _ { \mathbf { \Psi } } \mathbf { \mathrm { e r t } } ^ { \mathsf { \tiny { 5 } } } \mathbf { \Psi }$ correlation between $\mathrm { X } _ { 1 }$ and $\mathrm { X } _ { 2 } , \mathrm { \bf q } _ { 1 }$ is the reliability of $\mathrm { X } _ { \mathrm { l } }$ and of $\mathrm { X } _ { 2 } ( \alpha _ { \mathrm { l } }$ is assumed be equal to $\mathrm { \bf q } _ { 2 } ) . ^ { 4 } \mathrm { \bf ~ P I _ { i } }$ indicates the proportional amount the plim $\beta _ { \mathrm { i } } ^ { \setminus }$ estimate has been biased away from the true (or underlying) value of ${ \mathrm { ' } } \beta _ { \mathrm { i } }$ . The “plim” indicates that plim βˆ would be the estimate if there were an infinite number of data points. (As stated earlier in the paper, we found that with sample sizes of 100 to 200, the equations predicted the values of regression path estimates reasonably accurately, and for collections of 500 datasets at those sample sizes, quite accurately in the aggregate).

These equations can give us a feel for how M+ME will affect regression path estimates. Assume for the moment that $\beta _ { 1 } , \beta _ { 2 } ,$ and $\rho _ { 1 2 }$ are all positive and $\beta _ { 1 }$ is greater than $\beta _ { 2 }$ (a not uncommon situation). Under these conditions, given that $\mathbf { { \alpha } } _ { \mathbf { { 1 } } } , \mathbf { { \rho } } _ { 1 2 } ,$ and $\beta _ { 2 } / \beta _ { 1 }$ are all less than one, it can be seen that $\mathrm { P I } _ { \{ 3 1 } $ will always be greater than zero. (Recall that: $\mathrm { P I } _ { \mathrm { i } } { > } 0 \Rightarrow \mathrm { \beta } _ { \mathrm { i } } ^ { \mathrm { ^ { \wedge } } }$ is underestimated.) Therefore given our assumptions, when there is multicollinearity and random measurement error, the dominant $\beta _ { 1 }$ will always be underestimated.

Depending on the values of $\rho _ { \mathrm { 1 3 } }$ and $\beta _ { 1 } / \beta _ { 2 }$ , the non-dominant $\beta _ { 2 }$ could be under- or over-estimated. In Appendix C we present the logic that shows that except when $\beta _ { 1 }$ and $\beta _ { 2 }$ have close to the same value, M+ME will tend to push the $\boldsymbol { \beta } _ { 2 } ^ { \setminus }$ estimate higher than $\beta _ { 2 } \ i \mathrm { f } \ \beta _ { 2 }$ β if is positive.

Equations for Correcting the Path Estimate Bias. Although the algebra is tedious, equations A1-15 and A1-16 can be turned around to allow us to calculate estimates of the underlying $\beta$ values, given the β<sup>^</sup> and $\boldsymbol { \beta } _ { 2 } ^ { \setminus }$ estimates, as follows:

$$
\text { Let } C = (1 - \alpha_ {1}) / (1 - \rho_ {1 2} ^ {2})
$$

$$
\begin{array}{l} \text {(Recall that when \alpha_ {1} is not equal to \alpha_ {2} we use} \\ \alpha_ {1} = \alpha_ {\text { combination }} = (\alpha_ {1} * \alpha_ {2}) ^ {1 / 2}. \text { See footnote \#16.}) \end{array}
$$

$$
\left(\beta_ {1} - \beta_ {1} ^ {\wedge}\right) / \beta_ {1} = C * \left[ 1 - \rho_ {1 2} * \beta_ {2} / \beta_ {1} \right]
$$

$$
\left(\beta_ {1} - \beta_ {1} ^ {\wedge}\right) = \beta_ {1} \left\{\mathrm{C} * \left[ 1 - \rho_ {1 2} * \beta_ {2} / \beta_ {1} \right] \right\}
$$

(Green and Kiernan’s Equation for $\mathrm { P I } _ { \beta 1 } )$

$$
\beta_ {1} = \beta_ {1} ^ {\wedge} + \beta_ {1} C * [ 1 - \rho_ {1 2} * \beta_ {2} / \beta_ {1} ]
$$

$$
\beta_ {1} = \beta_ {1} ^ {\wedge} + \beta_ {1} C - C * \rho_ {1 2} * \beta_ {2} ]
$$

$$
\left. \beta_ {1} - \beta_ {1} C = \beta_ {1} ^ {\wedge} - C * \rho_ {1 2} * \beta_ {2} \right]
$$

$$
\beta_ {1} = \beta_ {1} ^ {\wedge} / (1 - C) - [ C * \rho_ {1 2} * \beta_ {2} ] / (1 - C)
$$

Similarly

$$
\beta_ {2} = \beta_ {2} ^ {\wedge} / (1 - C) - [ C * \rho_ {1 2} * \{\beta_ {1} \} ] / (1 - C)
$$

Substituting in $( \beta _ { \mathrm { 1 } } )$ and collecting terms,

$$
\beta_ {2} = \beta_ {2} ^ {\wedge} / (1 - C) - [ C * \rho_ {1 2} * \{\beta_ {1} ^ {\wedge} / (1 - C) - [ X * \rho_ {1 2} * \beta_ {2} ] / (1 - C) \} ] / (1 - C)
$$

$$
\beta_ {2} = \beta_ {2} ^ {\wedge} / (1 - C) - C * \rho_ {1 2} * \beta_ {1} ^ {\wedge} / (1 - C) ^ {2} + \left[ \left(C * \rho_ {1 2}\right) ^ {2} * \beta_ {2} \right] / (1 - C) ^ {2}
$$

$$
\beta_ {2} - \left(\mathrm{C} * \rho_ {1 2}\right) ^ {2} * \beta_ {2} / (1 - \mathrm{C}) ^ {2} = \beta_ {2} ^ {\wedge} / (1 - \mathrm{C}) - \mathrm{C} * \rho_ {1 2} * \beta_ {1} ^ {\wedge} / (1 - \mathrm{C}) ^ {2}
$$

$$
\beta_ {2} \left[ 1 - \left(\mathrm{C} * \rho_ {1 2}\right) ^ {2} / (1 - \mathrm{C}) ^ {2} \right] = \beta_ {2} ^ {\wedge} / (1 - \mathrm{C}) - \mathrm{C} * \rho_ {1 2} * \beta_ {1} ^ {\wedge} / (1 - \mathrm{C}) ^ {2}
$$

$$
\beta_ {2} = \left[ \beta_ {2} ^ {\wedge} / (1 - C) - C * \rho_ {1 2} * \beta^ {\wedge} / (1 - C) ^ {2} \right] / \left[ 1 - \left(C * \rho_ {1 2}\right) ^ {2} / (1 - C) ^ {2} \right]
$$

$$
\beta_ {2} = \beta_ {2} ^ {\wedge} / (1 - C) - C * \rho_ {1 2} * \beta_ {1} ^ {\wedge} / (1 - C) ^ {2} / \left[ (1 - C) ^ {2} - (C * \rho_ {1 2}) ^ {2} \right] / (1 - C) ^ {2}
$$

$$
\beta_ {2} = \frac {\beta_ {2} ^ {\wedge} * (1 - C) - C * \rho_ {1 2} * \beta_ {1} ^ {\wedge}}{\left[ (1 - C) ^ {2} \right] - \left(C * \rho_ {1 2}\right) ^ {2}}\tag{A1-17}
$$

Similarly

$$
\beta_ {1} = \frac {\hat {\beta_ {1}} * (1 - C) - C * \rho_ {1 2} * \hat {\beta_ {2}}}{[ (1 - C) ^ {2} ] - (C * \rho_ {1 2}) ^ {2}}\tag{A1-18}
$$

Correcting the Standard Deviation of the Corrected Path Estimate. One final insight is needed in correcting for the M+ME path bias. To determine the proper estimate of the path standard deviation, we have to recognize that the path bias created by the M+ME comes with a change in the standard deviation. To calculate the corrected standard deviation for the true path we need to, in a sense, undo that change. Once the variances of the $\beta _ { 1 } ^ { \wedge }$ and $\boldsymbol { \beta } _ { 2 } ^ { \setminus }$ paths have been corrected for the VIF bias (Equation A1-2), the variance of the estimates for the above underlying $\beta _ { 1 }$ and $\beta _ { 2 }$ paths can be calculated using a standard result from statistics:

$$
\begin{array}{l l} \text { if } & \beta_ {2} = a * \beta_ {2} ^ {\wedge} + b * \beta_ {1} ^ {\wedge} \\ \text { then } & \operatorname{Var} (\beta_ {2}) = a ^ {2} * \operatorname{Var} (\beta_ {2} ^ {\wedge}) + b ^ {2} * \operatorname{Var} (\hat {} _ {1}) \end{array}\tag{A1-19}
$$

where in our case $\mathbf { \ddot { a } } ^ { , \nu }$ is $\left( 1  – \mathrm { C } \right) / \{ ( 1 – \mathrm { C } ) ^ { 2 } - ( \mathrm { C } * \rho _ { 1 2 } ) ^ { 2 } \}$ , and $\mathbf { \bar { \Delta } } ^ { \mathrm { c } } ( \mathbf { b } ^ { \mathrm { , } \mathrm { , } }$ is $\mathrm { C } * \rho _ { 1 2 } / \{ ( 1 { - } \mathrm { C } ) ^ { 2 } - ( \mathrm { C } * \rho _ { 1 2 } ) ^ { 2 } \}$ from equation $_ { \mathrm { A l - 1 7 } }$

## Appendix B

## Will PLS with Bootstrapping Correct for M+ME?

For PLS with bootstrapping to correct for the M+ME blindspot seen in regression, it would need to overcome the deficiency noted in our equation 3 versus our equation 4. That is, it would need to somehow incorporate random measurement error into its estimate for the standard deviations of the X1 and X2 paths leading to Y1. We see two possible ways that PLS with bootstrapping could do this. First, bootstrapping could determine the reliability of the two constructs (in our case the X1 and X2 constructs). It could then adjust its (bootstrapping determined) standard deviation of the path using those reliabilities, similarly to our equation 4. However, we see no point in the PLS bootstrapping process where the reliability of the two construct measures is taken into account. For each bootstrapping resample, after the indicator weights are determined and the proxy construct scores calculated, all information about the indicator values is discarded. What occurs is that OLS regression is used with the proxy construct scores to determine another set of path values. Nowhere in the process is the information (for explicitly determining the measurement reliability of the constructs) used by PLS or its bootstrapping process.

A second possibility could be that bootstrapping automatically takes M+ME into account. The central assumption of bootstrapping in general (Mooney and Duval 1993) is that the variation contained in a given sample is representative of the variation existing in the larger population. If this were true for the M+ME blind spot, then bootstrapping could correctly incorporate the extra variation due to M+ME and suggest appropriately larger standard deviations.

If in some bootstrapping resamples M+ME led to additional overestimations of the path values, and in others M+ME led to additional underestimations, then the total distribution of the bootstrapping resample path values would be appropriately wider, and estimations for the path standard deviations would have increased accordingly. However, recall that each PLS bootstrapping resample is drawn from the original sample and therefore contains roughly the same underlying $\beta _ { 1 } , \beta _ { 2 } , \rho _ { 1 2 }$ , and other characteristics as the original sample. We showed in Appendix A that Green and Kiernan’s equations (A1-15 and A1-16) clearly indicate that when there is M+ME and both path estimates are positive and not too close together, regression will tend to systematically underestimate ${ \beta } _ { 1 } ^ { \wedge }$ and systematically overestimate $\beta _ { 2 } ^ { \setminus }$ based on the reliability and the values of $\beta _ { 1 } , \ \beta _ { 2 } .$ , and ${ \rho _ { 1 2 } } ^ { 5 }$ The bias seen in Green and Kiernan’s equations (6 and 7) for regression will then be apparent in each of the bootstrapping regression results

Therefore, it is reasonable to assume that when PLS uses OLS to estimate paths for each of its bootstrapping samples, it will tend to systematically underestimate each of those $\beta _ { 1 } ^ { \wedge }$ path estimates by roughly the same amount, and to systematically overestimate each of those $\boldsymbol { \beta } _ { 2 } ^ { \setminus }$ estimates by roughly the same amount. If that is true, instead of having the collection of bootstrapping $\boldsymbol { \beta } _ { 2 } ^ { \setminus }$ path estimates more widely dispersed, they will be biased but about as closely spaced as if there were no M+ME bias.

PLS’s bootstrapping distributions should therefore incorporate the same variance inflation factor as seen in equation 3, mirroring the results seen in regression. We see no argument for a way in which the PLS bootstrapping resamples will incorporate the correction shown in our equation 4.

## Appendix C

## Further Exploration of Green and Kiernan’s Equations: Impact of Negative Paths or Negative Correlations

Mela and Kopalle (2002) have argued that positive versus negative correlations would have very different (asymmetric) impacts on path biases and path estimate variances. For us (with multicollinearity and random measurement error) that question is answered by looking again at Green and Kiernan’s (1989, p. 360) equations for the bias (or proportional inconsistency) in the estimates for ${ \beta } _ { \mathrm { l } } ^ { \wedge }$ and $\beta _ { 2 } ^ { \setminus } .$

$$
\begin{array}{l} \mathrm{PI} _ {\beta 1} = (\beta_ {1} - \operatorname{plim} \beta_ {1} ^ {\wedge}) / \beta_ {1} = [ (1 - \alpha_ {1}) / (1 - \rho_ {1 2} ^ {2}) ] * [ 1 - (\rho_ {1 2} * (\beta_ {2} / \beta_ {1})) ] \\ \mathrm{PI} _ {\beta 2} = (\beta_ {2} - \operatorname{plim} \beta_ {2} ^ {\wedge}) / \beta_ {2} = [ (1 - \alpha_ {1}) / (1 - \rho_ {1 2} ^ {2}) ] * [ 1 - (\rho_ {1 2} * (\beta_ {1} / \beta_ {2})) ] \end{array}
$$

(Eq. 6 repeated) (Eq. 7 repeated)

Equations 6 and $^ { 7 , }$ repeated above, can tell us quite a bit about the behavior of ${ \beta } _ { \mathrm { l } } ^ { \wedge }$ and $\textstyle { \bigl \beta } _ { 2 } ^ { \wedge } .$ First, remember that if $\mathrm { P I } _ { \mathrm { \beta i } } \mathrm { \ i s } > 0$ , then $| \beta _ { 1 } ^ { \setminus } |$ is an underestimation of $\lVert \beta _ { \mathrm { i } } \rVert .$ . If $\mathrm { P I } _ { \mathrm { \beta i } } \mathrm { i } \mathrm { s } < 0$ , then $| \beta _ { \mathrm { i } } ^ { \setminus } |$ is an overestimation of| β |. If |β<sup>^</sup>| is an underestimation of |β |, this means that $| \beta _ { \mathrm { i } } ^ { \wedge } |$ is closer to zero than $| \beta _ { \mathrm { i } } |$ . Whether $\beta _ { 1 }$ or $\beta _ { 2 }$ are over- or under-estimated depends upon the sign of $\mathrm { P I } _ { \{ 3 1 } $ or $\mathrm { P I } _ { \beta 2 } .$ . Note that in both equations, the $[ ( 1 ~ \cdot ~ $ ${ \bf \alpha } _ { { \bf { \Lambda } } } ) / ( 1 { - } { \rho _ { 1 2 } } ^ { 2 } ) \stackrel { \cdot } { . }$ ] term before the asterisk is always positive. Therefore whether $\beta _ { 1 }$ or β are over or under-estimated depends upon the sign of $[ 1 - ( \mathsf { p } _ { 1 2 }$ $\ast _ { \mathrm { \ell } } ( \beta _ { 2 } / \beta _ { 1 } ) ]$ or $[ 1 - ( \mathsf { p } _ { 1 2 } * ( \mathsf { \{ \beta }  _ { 1 } / \mathsf { \beta } _ { 2 } ) ) ]$ ]. Table C1 shows the impact of different combinations of negative and positive signs on $[ 1 - ( \mathsf { p } _ { 1 2 } * ( \mathsf { \{ \beta }  _ { 2 } / \mathsf { \beta } _ { 1 } ) ) ]$ or $[ 1 - ( \mathsf { p } _ { 1 2 } * ( \mathsf { \{ \{ \beta } _ { 1 } / \mathsf { \{ \beta } _ { 2 } )    ) ]$ , and therefore on the value and sign of the proportional inconsistencies.

One interesting outcome is apparent in the column labeled “Decision Condition” of Table C1. For $\beta _ { 1 }$ there is no decision: $\mathrm { i f } | \beta _ { 1 } ^ { \wedge } | > | \beta _ { 2 } ^ { \wedge } |$ |, we would say that $\beta _ { 1 } ^ { \wedge }$ is dominant. In this case ${ | \ \beta _ { 1 } ^ { \wedge } }$ | will always be an underestimation of $\beta _ { \mathrm { l } }$ |. More interesting is the case for $| \beta _ { 2 } ^ { \setminus } | . \ \mathrm { I f } | \ \beta _ { 2 } ^ { \setminus } |$ is relatively large (i.e. , greater than $| \rho _ { 1 2 } * \beta _ { 1 } ^ { \wedge } | )$ , then $\hat { | \beta _ { 2 } | }$ will also be an underestimate of $\mid \beta _ { 2 } \mid .$ Otherwise, $| \beta _ { 2 } ^ { \setminus } |$ will be an overestimate of $\left. \beta _ { 2 } \right| .$ This last can lead to false positives.

Relative to Mela and Kopalle’s arguments, in fact it can be seen that having zero or two negative signs for $\rho _ { 1 2 } , \beta _ { 1 }$ ,and $\beta _ { 2 }$ creates a quite different configuration of the results than having one or three negatives. Having exactly two of the signs negative keeps the same configuration of results, though it does cause one or more path estimate biases to switch (symmetrically) from positive to negative. This all suggests a slightly different reading of the Mela and Kopalle paper. Although they focused on the impact of omitted but correlated variables, behavior simila to their findings can be created without omitted variables, by adding measurement error and collinearity. The impacts Mela and Kopalle seek to show have the same relationship as those pointed out above from Green and Kiernan’s equations.

Table C1. Behavior of Proportional Inconsistencies (Green and Kiernans’s PI) (Assuming |β<sub>1</sub>| > |β<sub>2</sub>|)

<table><tr><td>Focus on PIβ1 or PIβ2</td><td>Decision Condition</td><td>Relationship of |ρ12* β2/β1| to “1”</td><td># Minus Signs among ρ12, β2, β1</td><td>What Happens to 1 - (ρ12* β2/β1)</td><td>What Happens to PIβ1 or PIβ2</td><td></td></tr><tr><td>PIβ1=(1-ρ1)/(1-ρ122)* [1-(ρ12* β2/β1)]</td><td>none</td><td>|ρ12* β2/β1| always &lt; 1</td><td>0 or 2 Minus signs</td><td>(ρ12*β2/β1) subtracts from one</td><td>PIβ1 is always positive</td><td>|β1^| is an under-estimate of |β1|</td></tr><tr><td></td><td></td><td></td><td>1 or 3 Minus signs</td><td>(ρ12*β2/β1) adds to one</td><td>PIβ1 is more positive</td><td>|β1^| is a bigger underestimate of |β1|</td></tr><tr><td>PIβ2=(1-ρ1)/(1-ρ122)* [1-(ρ12*β1/β2)]</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>|ρ12*β1|&lt; |β2|(|β2| is relatively large)</td><td>|ρ12* β1/β2| always &lt; 1</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>0 or 2 Minus signs</td><td>(ρ12* β1/β2) subtracts from one</td><td>PIβ2 is always positive</td><td>|β2^| is an underestimate of |β2|</td></tr><tr><td></td><td></td><td></td><td>1 or 3 Minus signs</td><td>(ρ12* β1/β2) adds to one</td><td>PIβ2 is more positive</td><td>|β2^| is a bigger underestimate of |β2|</td></tr><tr><td></td><td>|ρ12* β1|&gt; |β2|(β2 is relatively small)</td><td>|ρ12*β1/β2| always &gt; 1</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>0 or 2 minus signs</td><td>(ρ12* β1/β2) subtracts from one</td><td>PIβ2 is always negative</td><td>|β2^| is an overestimate of |β2|</td></tr><tr><td></td><td></td><td></td><td>1 or 3 Minus signs</td><td>(ρ12* β1/β2) adds to one</td><td>PIβ2 is positive</td><td>|β2^| is an under-estimate of |β2|</td></tr></table>

## Appendix D

## Correcting for M+ME Biases — Step by Step

When might an analysis be in the M+ME danger zone? For the sake of illustration, consider the model and correlations shown in Figure D1. Here we have nine constructs connected by hypothesized paths, showing selected (overt) path estimates and selected (overt) inter-construct correlations. How would a researcher recognize that any particular pair of these constructs is near enough to the M+ME danger zone to possibly require the correction? Note that Figures 3 through 7 and Figure 9 in the paper show underlying correlations. If a researcher compares their own results to Figures 3 through 7, they need to use equation 2 to convert overt correlations to underlying correlations. Note also that the M+ME Correction Application requires “overt” correlations, not underlying correlations.

![](/api/attachments/ZMPN82TN/fulltext/images/ac914b9734b08bdbee28c14d864bff0197cbf94e20aba2e4e882f8ed08d689ad.jpg)  
Figure D1. Overt Correlations in Hypothetical Model with N = 200, Reliability = .80

Step One: Identify Correlations of Interest. First, recognize that in Figure D1, only the seven overt correlations or paths with a value (or the word “small”) added to the link are of concern to us. Note that the path between G and H is of concern even though it is modeled as a path rather than a correlation, because G and H are correlated, and both participate in the regression equation predicting construct I. Note also that even if the overt correlation between construct C and construct D were very high, say.72, that would not be of concern, because constructs C and D do not participate in the same regression equation.

Categorize all high correlation situations into two groups. Notice that the upper part of the figure shows two of what we will call an “isolated” high correlation—only two highly correlated constructs participating in the same regression. The bottom part of Figure D1 shows a different situation—three highly correlated constructs all participating in the same regression, specifically D, E, and F are correlated and all predict H. This latter situation we will call a “combination” of high correlations. These “combination” situations present more of a challenge than the isolated high correlation and will be dealt with in Appendix E.

Step Two: Assess and perhaps correct the “isolated” correlations of interest. There are two isolated correlations in Figure D1 that should be examined: A and B predicting G, and G and H predicting I (both having an overt correlation of .40).

To rule out obviously non-problematic correlated pairs, one can do a quick (very approximate) back of the envelope calculation to determine if there is even any cause for concern, as follows. For example, if the reliability of constructs A and B in Figure D1 is .80, using equation 2, we conclude that the underlying correlations are about .50 for A with B (and for G with H). To get a general feeling for whether A and B predicting G might involve a substantive M+ME bias, we can refer to Figure 7 (rather than Figures 4A or 4B, because the N is 200). If the sample size were closer to n = 100, then Figures 4A or 4B might be appropriate.

In Figure 7 we see that an analysis with a $\beta _ { \mathrm { l } }$ about .292, sample size of N = 200, and an underlying correlation of .50 gives us about a 7% likelihood of excessive false positives, near the top of the 95% confidence interval around 5% false positives. This suggests that we should use the M+ME Correction Application to check the possibility of an M+ME bias.

The M+ME correction application will correct for the bias to the VIF, correct the path biases, and adjust the standard deviations for the corrected path values. This downloadable application is available on the MISQ web site (Online Supplements: M+ME Correction Application). Figure 8 of the article proper displays the front end of the application, showing the input required (on the left side) and the results of the correction calculations on the right side. First, be sure that you are using the standardized regression (or PLS) results. Though here we will assume that $\beta _ { \mathrm { l } }$ is the dominant path (the construct whose path has the highest absolute value), that is not necessary. With this understanding, enter the regression results for the two (overt) path estimates from regression or PLS, the two overt t-statistics, the two reliabilities (for X1 and X2) and the overt (or apparent) correlation between X1 and X2. The corrected path values, t-statistics and p values will be displayed by the M+ME correction application. Because it is relatively easy to use, the M+ME correction application can be used without referring to the figure in the paper as a “back-of-the-envelope” approximation.

Table D1 shows the results of applying the corrections. The first set of rows in Table D1 shows the A and B predicting G situation when it is entered into the M+ME correction application. The input values are to the left, and the corrected path values and t-statistics are shown to the right. In this case the path correction has increased the B  G path slightly (to .184) and the recalculated standard deviation has decreased the t-statistic a good bit (to 1.561). The result is that the corrected B to G path is no longer statistically significant.

The second “isolated correlation” from Figure D1 is G and H predicting I, with G and H correlated at .40. This situation is depicted in the second set of rows of Table D1. There the H to I path is shown to be statistically significant even with the M+ME correction, though note that the t-statistic has dropped from 2.90 to 2.02. Finally, the third example in Table D1 has the same input as the second, but a correlation of .60 instead of .40. This increase in multicollinearity takes its toll, and under these circumstances the H to I path is no longer statistically significant after we apply the M+ME correction.

Note that in all three examples, the uncorrected results show that the questionable path is statistically significant (i.e., different from zero with 95% confidence). In two of those, the correction shows that the questionable path is not actually significant, and should not be considered different from zero.

We suggest that there is no place for optimists in questions of statistical significance. When M+ME for a particular path is not clearly ruled out by displays such as those in Figures 4A, 4B, or 7, the correction should be applied by inputting the relevant data into the M+ME correction application. Applying this correction to regression or PLS results when M+ME is not a problem will not create new problems. Instead, it will give the researcher a more accurate value for the t-statistic.

Table D1. Input and Output (Corrected Path Values and t-statistics) for the M+ME Correction Application

<table><tr><td></td><td colspan="8">Needed Input</td><td colspan="5">Output</td></tr><tr><td>Relation-ship</td><td>N</td><td> $β^1$ </td><td> $β^2$ </td><td> $β^1t$ </td><td> $β^2t$ </td><td> $\alpha_1$ </td><td> $\alpha_2$ </td><td> $\rho_{12}$ </td><td>Path</td><td>Significance Without Corrections</td><td>Corrected Path Est</td><td>Corrected t-stat</td><td>Significance with path and VIF correction</td></tr><tr><td rowspan="2">A, B → G;  $\rho_{a,b} = .40$ </td><td>200</td><td>.257</td><td>.170</td><td>3.50</td><td>2.05</td><td>.80</td><td>.80</td><td>.40</td><td>B→G</td><td>yes</td><td>0.184</td><td>1.56</td><td>Not Sig!</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>A→G</td><td>yes</td><td>0.314</td><td>3.00</td><td>yes</td></tr><tr><td rowspan="2">G,H → I;  $\rho_{g,h} = .40$ </td><td>200</td><td>.462</td><td>.240</td><td>2.89</td><td>2.90</td><td>.80</td><td>.80</td><td>.40</td><td>H→I</td><td>yes</td><td>0.243</td><td>2.02</td><td>yes</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>G→I</td><td>yes</td><td>0.576</td><td>2.55</td><td>yes</td></tr><tr><td rowspan="2">G,H → I;  $\rho_{g,h} = .60$ </td><td>200</td><td>.462</td><td>.240</td><td>2.89</td><td>2.90</td><td>.80</td><td>.80</td><td>.60</td><td>H→I</td><td>yes</td><td>0.179</td><td>1.01</td><td>Not Sig!</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>G→I</td><td>yes</td><td>0.623</td><td>2.03</td><td>yes</td></tr></table>

## Appendix E

## The Challenge of Combinations of High Correlations

In the lower part of Figure D1 we see a “combination” of three constructs (D, E, and F) connected with one high and one only moderately high overt correlation, both of which affect the E to H path (that is .380 and .320 overt correlations, suggesting underlying correlations of .475 and .400). The third overt correlation (between D and F) is .304, suggesting an underlying value of .380. We acknowledge at the outset that we do not fully understand all the issues relating to multiple high correlations situations. The problem is that Green and Kiernan’s (1989) equations do not extend to three intercorrelated constructs. In fact both pairs of correlated constructs have an impact on the estimated E to H path estimate and their impact could be additive or in some cases more than additive. This means that except for turning to CB-SEM, we do not have an effective way to correct for the path biases in regression or PLS, when faced with such a situation. This is an area where additional research would be quite valuable.

A key insight in understanding combinations of high correlations is that there are three general archetypes of the underlying “causes” of these three way configurations of correlations, as shown in Figure E1. Of course the cause may contain a mixture of several of these types, plus the possibility of direct causal links between the focal constructs (in this case Constructs D, E or F.

On the top left of Figure E1 (Panel A, single underlying cause) we see that the correlations between all three constructs are due to relationships with a single underlying construct. As it turns out, there is a reasonable correction approach when the combination of high correlations is produced by a single underlying construct. In those situations the M+ME biases can be considered additive, and it is possible to correct for the largest correlation as we have shown in the previous section for isolated high correlations. Once this is done, the researcher can determine (very roughly) from the size of the remaining correlation (for example using Figures 3, 4, or 7), whether that remaining correlation by itself would put the analysis into the M+ME danger zone. If not, then the single correlation correction method is sufficient. One definitely should not apply the M+ME correction application a second time.

Unfortunately we know of no way to determine, from the data a researcher would have, whether a combination of correlations was caused by two, or even three, background constructs. Thus we have no way to safely assume a single underlying cause. This poses a difficult problem.

In Figure E2 we show the uncorrected results from data generated by each of the archetypal possible causes, along with the results after the highest correlation has been corrected. The figure does show that correcting for the dominant correlation always improves the situation. But unfortunately, even with the correction, some of the lines are well above the 95% confidence interval around .05.

Since the researcher cannot know which situation they are working with, and since it is not appropriate to optimistically “assume the best possible situation” in hypothesis testing, we cannot recommend using the M+ME correction with combinations of high correlations.

![](/api/attachments/ZMPN82TN/fulltext/images/f5bcbaa2175ee4528f3c74a05238032721893a6b9d009ea9820ef65a6c020387.jpg)  
Panel A. Single Underlying Cause

![](/api/attachments/ZMPN82TN/fulltext/images/af50b0998d6e08d665ff5e70754d6aca68b9088eb606b18b060c8e6bea3024ec.jpg)  
Panel B. Two Distinct Underlying Causes

![](/api/attachments/ZMPN82TN/fulltext/images/1fca4835ece344d7255c1ad8af4a316eb90e3850036f2c9e97efb165e70e0739.jpg)  
Panel C. Three Distinct Underlying Causes  
Figure E1. Three Different Archetypal Causes of Combinations of High Correlations

![](/api/attachments/ZMPN82TN/fulltext/images/493b86799d37d21e75951c307e82a72b7e3f4aa3dd3d8550a6bc0f6b6889600b.jpg)  
No Correction Versus Dominant Correlation Corrected, $\alpha = . 8 0 , \mathsf { N } = 2 0 0 , \mathsf { X } 1 \to \mathsf { Y } 1 = . 4 2 0$

Figure E2. Regression False Positives Results from Combinations of High Correlations

![](/api/attachments/ZMPN82TN/fulltext/images/a761fd4dd356bb8f2c245d6a11333311181be89663bc44e02d605ab9b2d54d41.jpg)

α = .80, N = 200, X1  Y1 = .420

Figure E3. CB-SEM False Positives Results From Combinations of High Correlations

One safe method to use in combinations of high correlation situations would be to convert the analysis over to CB-SEM. Figure E3 shows the results from that method. We see that with CB-SEM, the large numbers of false positives never appear in the first place.<sup>7</sup> Though it may require extra work for those not well-versed in the use of CB-SEM, this clearly provides a solution to the combination of high correlation M+ME situation. Alternatively (or in conjunction), it may be appropriate to change the underlying model (e.g., using higher-order constructs).

As stated earlier, we do not fully understand the combinations of high correlation situation. Because combinations of high correlations do appear in IS research, additional research in this area could be helpful.

## Appendix F

## Testing Whether M+ME False Positives Could Be Due to Discriminant Validity Problems

One alternative explanation for the results we obtained might be framed within the larger context of measurement model misspecification, and specifically the presence of a lack of discriminant validity among constructs. To address this possibility, we conducted some ancillary analyses. We found the following. First, using chi square difference tests of discriminant validity and one of our Monte Carlo simulation datasets (500 samples each of N = 100, reliability = .80, ρ = .80) we did find evidence of discriminant validity problems. Specifically, 56 (or about 10%) of the samples had discriminant validity problems, as compared to 59 (also about 10%) samples with M+ME false positives. Although these numbers are quite close, only 4 samples had both discriminant validity problems and excessive false positives.

We note further that although both false positives and discriminant validity problems are exacerbated by increasing correlations and decreasing reliabilities, those two phenomena react quite differently to increasing sample size. As shown in Figure F1, larger sample sizes decrease discriminant validity problems to virtually zero, while they increase M+ME false positives substantially. Thus it is clear that the two phenomena share some causal factors but are actually quite distinct. Knowing that a dataset suffers from one of these phenomena does not provide much knowledge about the likelihood that it also suffers from the other.

![](/api/attachments/ZMPN82TN/fulltext/images/d7976c409eafcf4c418e666bcf601eae169d1f74e6e2160400c1e9b5dbfe48c5.jpg)

$$
\left(\beta_ {1} \text {   path } = . 2 9 2, N = 1 0 0, \alpha = . 8 0, \rho_ {1 2} = . 8 0\right)
$$

Figure F1. Sample Size and Discriminant Validity Problems Versus M+ME False Positives

## Appendix G

## Pictorial Depiction: M+ME Impact on Regression and CB-SEM

Some readers may find it helpful to see a graphical representation of the impact of M+ME on regression and CB-SEM results for 500 samples as in our Monte Carlo simulations. Throughout we will be looking at an underlying X1 to Y1 path of .600, an X2 to Y1 path of zero, a sample size of N = 200, and reliability of .80 for both X1 and X2. For both regression and CB-SEM, the average path estimates across the 500 samples is shown below in Figures G1, G2, and G3, for three different scenarios. Along with the average path estimates, also shown is a representation of the distribution of those 500 estimates around that average estimate. The distribution curves shown comes from calculating the standard deviation of the 500 path estimates, and displaying them as a curve anchored at the average path estimate plus 2 times the standard deviation, and the average path estimate minus 2 times the standard deviation.

We first look at the results when the underlying reality is a zero correlation between X1 and X2. That is, when there is no M+ME. We will then shift our focus to the situation where M+ME is extreme, with a correlation between X1 and X2 of .90.

Figure G1 shows the results for β (a zero path) when there is no correlation between X1 and X2. The average $\beta _ { 2 }$ path estimates for regression and CB-SEM are both about zero, and the distribution curves for both span from about -1.3 to + 1.5. These results are what we might have expected.

In Figure G2 we show the results when the correlation between X1 and X2 is .90, a very high correlation. Though M+ME will rarely or never be this extreme in practice, this scenario allows us to see more clearly what the specific effects of M+ME are, and why this is a problem. Under these conditions, CB-SEM returns a path estimate for β of near zero, and a standard deviation that is about 7 times as large as it was when ${ \boldsymbol \rho } _ { 1 2 }$ was .00 (.497 versus .068). The very large spread of the β path estimations suggests that the high correlation between X1 and X2 makes the resulting path estimates very dependent upon random variance in the data. CB-SEM recognizes this and increases the standard deviation it uses appropriately.

For regression under these conditions, the average path estimate is quite skewed (from near zero at ${ \rho } _ { 1 2 } = 0$ to a value of .175 at ${ \rho } _ { 1 2 } = . 9 0$ . This is as predicted by the Green and Kiernan equations. The distribution around the .175 based on the standard deviation of the regression estimates is about as wide as in Figure G1, but now shifted up, so that most of the estimates are now significantly different from zero. This is of course misleading, since the true path is zero. This makes the M+ME bias very apparent.

In Figure G3, we have used the Green and Kiernan equations to correct for the M+ME path bias in regression, and at the same time corrected the standard deviation values in regression, also based on the VIF and Green and Kiernan equations. These corrections have removed the path bias, and now the bias and the dispersion of the path values are roughly equal for regression and for CB-SEM, and both reflect the uncertainly created by the large correlation between X1 and X2.

![](/api/attachments/ZMPN82TN/fulltext/images/98351bd7a9ee28f58f3d848e8eed87184abe162f9150b55bc500a917902734cd.jpg)  
Figure G1. Regression and CB-SEM When Correlation Between X1 and X2 is 0.00

![](/api/attachments/ZMPN82TN/fulltext/images/02d911cc89d22fe166c875fdef5ededecbddb597ce54fdff79b3e103d3680bf6.jpg)  
Figure G2. Regression and CB-SEM When Correlation Between X1 and X2 is 0.90

![](/api/attachments/ZMPN82TN/fulltext/images/fed8d44579bfa6f5a87ad33a041cb0725555f083be77fcedae3d7c46748986f4.jpg)  
Figure G3. Regression and CB-SEM When Correlation Between X1 and X2 is 0.90, After VIF and Green and Kiernan Path Bias Corrections

## References

Goodhue, D., Lewis, W., and Thompson, R. 2011. “A Dangerous Blind Spot in IS Research: False Positives Due to Multicollinearity Combined with Measurement Error,” in Proceedings of the 17<sup>th</sup> Americas Conference on Information Systems, Detroit, MI, August 4-7.

Green, C. J., and Kiernan, E. 1989. “Multicollinearity and Measurement Error in Econometric Financial Modelling,” The Manchester School (57:4), pp. 357-369.

Johnston, J. 1972. Econometric Methods (2<sup>nd</sup> ed.), New York: McGraw-Hill.

Mela, C., and Kopalle, P. 2002. “The Impact of Collinearity on Regression Analysis: the Asymmetric Effect of Negative and Positive Correlations,” Applied Economics (34:6), pp. 667-677.

Mooney, C. Z., and Duval, R. D. 1993. Bootstrapping: A Nonparametric Approach to Statistical Inference, Beverly Hills, CA: Sage Publications.
