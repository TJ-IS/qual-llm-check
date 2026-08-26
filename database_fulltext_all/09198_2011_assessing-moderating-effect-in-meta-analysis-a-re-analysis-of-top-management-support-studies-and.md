---
otero_id: 9198
otero_key: "DQAK23NU"
title: "Assessing moderating effect in meta-analysis: a re-analysis of top management support studies and suggestions for researchers"
authors: "Mark I Hwang; Frank L Schmidt"
year: "2011"
journal: "European Journal of Information Systems"
doi: "10.1057/ejis.2011.12"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
CONTRARIAN STUDY

# Assessing moderating effect in meta-analysis: a re-analysis of top management support studies and suggestions for researchers

Mark I. Hwang<sup>1</sup> and Frank L. Schmidt<sup>2</sup>

<sup>1</sup>Business Information Systems Department, Central Michigan University, Mt. Pleasant, MI, U.S.A.; <sup>2</sup>Tippie College of Business, University of Iowa, Iowa City, IA, U.S.A.

Correspondence: Mark I. Hwang, Business Information Systems Department, Central Michigan University, Mt. Pleasant, MI 48859. U.S.A. Tel: þ 44 989 774 5900; Fax: þ 44 989 774 3356; E-mail: mark.hwang@cmich.edu

## Abstract

Meta-analysis has been increasingly used as a knowledge cumulation tool by IS researchers. In recent years many meta-analysts have conducted moderator analyses in an attempt to develop and test theories. These studies suffer from several methodological problems and, as a result, may have contributed to rather than resolved inconsistent research findings. For example, a previous meta-analysis reports that task interdependence moderates the effect of top management support to render it a non-critical component in systems implementation projects when task interdependence is low. We show that this conclusion is the result of uncorrected measurement error and an erroneous application of a fixed effects regression analysis. We discuss other pitfalls in the detection and confirmation of moderators including the use of the Q statistic and significance tests. Our recommended approach is to break the sample into subgroups and compare their credibility and confidence intervals. This approach is illustrated in a re-analysis of the top management support literature. Our results indicate that top management support is important in both high and low task interdependence groups and in fact may be equally important in both groups. Guidelines are developed to help IS researchers properly conduct moderator analyses in future meta-analytic studies. European Journal of Information Systems (2011) 20, 693–702.

Keywords: management support; IS implementation; systems success; meta-analysis; moderator

## Introduction

Meta-analysis has been increasingly used as a knowledge cumulation tool by IS researchers (e.g., Sabherwal et al, 2006; Wu & Lederer, 2009). However, it is underutilized in IS vis-a\`-vis other disciplines. In psychology, for instance, its premier journal, Psychological Bulletin, had published 199 meta-analytic studies as of 2006 (Schmidt et al, 2009). In contrast, after the first meta-analysis paper was published in MIS Quarterly in the early 1990s (Alavi & Joachimsthaler, 1992), the second paper did not appear until almost a decade later (Dennis et al, 2001). Similarly, there is an almost 10-year lag between the first methodology paper (Hwang, 1996) and the second (King & He, 2005) published in IS journals. As more researchers apply the tool, it is critical that they understand methodological issues and the pros and cons of different approaches to avoid data analysis and interpretation errors.

Meta-analysis is useful for integration of research findings across studies and for theory development and testing (Hwang, 1996). The former involves combing effect sizes obtained from individual studies, whereas the latter entails the detection of moderator and mediator variables. In recent years many IS researchers have conducted moderator analyses in meta-analytic studies. However, these analyses are not always helpful to theory advancement. For example, both King & He (2006) and Schepers & Wetzels (2007) examined moderators in the technology acceptance model literature and yet reached different conclusions on the effect of the use of students as subjects. Whereas King & He (2006) found effect sizes smaller for student users than for general users, Schepers & Wetzels (2007) reported the opposite. Instead of resolving inconsistent findings, therefore, a meta-analysis can add to the confusion.

In addition to methodological moderators such as study subjects, substantive moderators have also been investigated. An example is the meta-analysis of the implementation success literature conducted by Sharma & Yetton (2003). While management support has long been theorized to play a critical role in the implementation of information systems (e.g., Garrity, 1963), empirical studies have not always supported this hypothesis (Rangananathan et al, 2004; Ifinedo, 2008). Sharma & Yetton (2003) tested a contingency model and concluded that management support is critical when task interdependence is high, but ‘a relatively weak and probably not critical component when task interdependence is low’ (p. 545).

This would have resolved inconsistent findings on the role of management support if the moderator is legitimate. However, as will be shown later, the Sharma & Yetton (2003) approach is problematic and the moderator they found is probably spurious. This should not be construed as an unfair criticism of the work of Sharma and Yetton, because the approach they followed is actually quite common in both IS and other disciplines. In addition, every study has certain limitations. However, substantive moderators have significant implications for theory development and management practice. Thus, methodological weaknesses that affect the confirmation of substantive moderators should not be lightly discounted. The purpose of this paper is to review common methodological issues in moderator analyses conducted by IS researchers in prior meta-analytic studies. Problems caused by these methodological issues and their remedies are illustrated in a re-analysis of top management support studies. Guidelines are developed to help IS researchers properly conduct moderator analyses in future meta-analytic studies.

## Literature review

Table 1 summarizes moderator analyses conducted by IS researchers in prior meta-analytic studies. In terms of methodology, these studies differ in the effects model that they follow (fixed vs random effects), and the way that moderators are detected and confirmed. There are pitfalls in each of the three aspects, as discussed below.

## Effects model

Various meta-analysis approaches have been developed over the years. The more popular ones are described by Glass and colleagues (Glass, 1976; Glass et al 1981), Hunter and Schmidt (Hunter et al, 1982; Hunter & Schmidt, 1990; Hunter & Schmidt, 2004), and Hedges & Olkin (1985). All approaches aim to derive a mean effect size from the obtained sample as an estimate of the population or true effect size. In addition, a population variance can be estimated, which is a crucial factor in determining how moderator variables can be detected in the theory development and testing stages of meta-analysis.

If the population variance is small or close to zero, it may be reasonable to assume that there is only one true effect size. Any variation in sample effect sizes is then attributed to sampling error. This is known as the fixed effects model. The random effects model, on the other hand, does not assume that the population variance is zero. Instead of one, there is a distribution of true effect sizes. Thus, variation in sample effect sizes can be caused by both sampling error and by between study variance.

The selection of fixed vs random effects model should be based on an understanding of whether or not all studies share a common true effect size rather than on the result of a statistical test (Borenstein et al, 2009, p. 84).

Table 1 Prior moderator analyses of IS topics

<table><tr><td>Study</td><td>Effects model</td><td>Moderator detection</td><td>Moderator confirmation</td></tr><tr><td>Montazemi &amp; Wang (1988)</td><td>Random effects</td><td>Q statistic</td><td>Subgroup variance differences</td></tr><tr><td>Hwang &amp; Wu (1990)</td><td>Random effects</td><td>n.a.</td><td>Subgroup mean differences</td></tr><tr><td>Benbasat &amp; Lim (1993)</td><td>Fixed effects</td><td>Q statistic</td><td>Simple regression</td></tr><tr><td>Dennis et al (2001)</td><td>Random effects</td><td>Q statistic; 75% rule</td><td>t test</td></tr><tr><td>Sharma &amp; Yetton (2003)</td><td>Fixed effects</td><td>Q statistic</td><td>Simple regression</td></tr><tr><td>King &amp; He (2006)</td><td>Random effects</td><td>Q statistic</td><td>Confidence interval differences</td></tr><tr><td>Kohli &amp; Devaraj (2003)</td><td>n.a.</td><td>n.a.</td><td>Multiple regression</td></tr><tr><td>Schepers &amp; Wetzels (2007)</td><td>Random effects</td><td>Q statistic</td><td>Z test</td></tr><tr><td>Joseph et al (2007)</td><td>Random effects</td><td>Q statistic</td><td>Z test</td></tr><tr><td>Sharma &amp; Yetton (2007)</td><td>Fixed effects</td><td>Q statistic</td><td>Multiple regression</td></tr><tr><td>Petter &amp; McLean (2009)</td><td>Random effects</td><td>Credibility intervals</td><td>n.a.</td></tr><tr><td>Wu &amp; Lederer (2009)</td><td>Fixed effects</td><td>Q statistic</td><td>Simple regression</td></tr></table>

In practice, most prior meta-analytic studies were conducted without an explicit consideration of the effects model. The Hunter and Schmidt approach adopts random effects models, and therefore all studies in Table 1 that followed their approach used random effects models. Hedges & Olkin (1985) developed procedures for both fixed and random effects models. However, most researchers (including those listed in Table 1) following their approach used fixed effects models because they were easier to comprehend and compute than random effects models (National Research Council, 1992; Cooper, 1997). In addition, fixed effects models were overwhelmingly chosen despite the fact that many studies failed to check for the precondition of homogeneity of effect sizes (Schmidt et al, 2009). In studies where the check was made, many researchers elected to proceed with fixed effects models even after the check showed that effect sizes were not homogeneous (Hunter & Schmidt, 2004; Schmidt et al, 2009).

The misuse of fixed effects models can result in severe underestimation of the standard error of the true effect size. For example, in an analysis of previous 68 metaanalytic studies, Schmidt et al (2009) found that confidence intervals estimated in fixed effects models were, on average, less than half as wide as those in random effects models. The underestimation of confidence intervals can inflate Type I errors from, say, commonly assumed 5% to a much larger number. Thus, any ‘significant’ mean effect sizes found in such models become doubtful.

Similarly, when regression is used to confirm the existence of moderators (e.g., Sharma & Yetton, 2003, 2007; Wu & Lederer, 2009), the confidence intervals around each moderator are narrower under the fixed effects model than under the random effects model. As a result, the P-value associated with the model and the moderator has a greater chance of becoming significant (Borenstein et al, 2009, p. 196).

Finally, even if these methodological weaknesses can somehow be overcome, fixed effects models have very limited applicability. By definition, fixed effects models assume that all primary studies are drawn from the same population and hence are virtual replications of each other with identical study characteristics such as research design and measures (Aronson et al, 1990). This assumption is rarely, if ever, met in any collection of information systems implementation studies. In fact, even when research settings are limited to similar organizations, implementation of the same technology can result in different outcomes, known as the ‘same-technology, different-outcomes’ phenomenon (Barley, 1986). As Hunter (2010, p. 701) noted that the inherent heterogeneity of IS studies require researchers to assume:

(1) that no matter how similar two organizations may be in observed ways, there will also be unobserved differences among them and (2) that unobserved differences may account for variation in structure both independently of technology. as well as through an interaction with it.

Consequently, random effects models are almost always preferred (Borenstein et al, 2009). Another advantage of using random effects models is that a fixed effects model is a special case of random effects models, one that the population variance happens to be zero (Hunter & Schmidt, 2004). A meta-analyst can, therefore, start with a random effects model and switch to a fixed effects analysis if need be, but the converse is not true (Borenstein et al, 2009).

## Moderator detection

As mentioned previously, if the calculated population variance is small or close to zero, it may be assumed that there is only one true effect size and the selection of fixed effects model is justified. More often than not, however, the calculated population variance is substantial and the meta-analyst may attempt to look for moderator variables as a result. However, many statistical artifacts and errors can cause wide variation in observed effect sizes (Hunter & Schmidt, 1990, 2004). Consequently, Hunter and Schmidt devise a 75% rule, which states that if all artifacts account for 75% or more of the variation in sample variance, then the population variance can be assumed to be zero. This 75% rule was used in some early meta-analyses as the justification for the search for moderator variables (e.g., Dennis et al, 2001).

As shown in Table 1, a more popular test for sample homogeneity is the Q statistic. The Q statistic and similar tests in general have low statistical power, however (Hunter & Schmidt, 1990, 2004; National Research Council, 1992; Borenstein et al, 2009). This means that a non-significant Q statistic could prematurely preclude a search for moderator variables. More often than not, however, the Q test result is significant given the wide variation among observed effect sizes typically found in a meta-analysis. A significant Q statistic, however, does not necessarily mean that moderator variables are in operation. Being a significance test, the Q test result depends on the sample size. If the number of studies under review is large, a significant Q statistic can be caused by the large sample rather than any substantial variation that exists among effect sizes. Similarly, a significant Q statistic can be the result of uncorrected statistical artifacts and errors rather than true moderator variables (Hunter & Schmidt, 1990, 2004).

## Moderator confirmation

If a search for moderator variables is justified, the metaanalyst can use different tools to produce evidence of the moderating effects. Since the early days of metaanalysis, multiple regression has been used as a means to identify moderator variables (e.g., Glass & Smith, 1979; Smith & Glass, 1977). Hedges & Olkin (1985) contended that regular regression was not appropriate for moderator analyses and developed a weighted least squares regression model instead. Their regression model is widely used in prior studies including four of the five listed in Table 1 that used regression.

It should be noted that the regression model described by Hedges & Olkin (1985) assumes a fixed effects analysis and hence a homogeneous sample is the precondition to its use. This is evident from the weight assigned to each study (Hedges & Olkin, 1985, p. 241), which accounts for sampling error only:

$$
w _ {i} = n _ {i} - 3,\tag{1}
$$

where $w _ { i }$ is the weight of study i and $n _ { i }$ is the sample size of study i. This model assumes that all of the nonartifactual variance (i.e., all of the variance in population values across studies) is explained by the moderators in the regression equation, a condition that is rarely met in practice and yet alas often misunderstood or overlooked by researchers.

If a random effects analysis is to be carried out then the weight assigned to each study should include both sampling error and between study variance. Unfortunately, this point was not made explicit by Hedges & Olkin (1985) and the formulas for random effects weight were not given until years later $( \mathrm { e . g . }$ , see Raudenbush, 1994). As a result, the fixed effect regression model was wrongly applied either to a heterogeneous sample (e.g., Benbasat & Lim, 1993) or when the test for homogeneity was ignored (e.g., Sharma & Yetton, 2003, 2007; Wu & Lederer, 2009). This can cause doubt in the ‘significant’ moderator found in the regression model, as we illustrate later in the paper.

When the Hedges & Olkin (1985) regression model is used to test for multiple moderator variables $( \mathrm { e . g . } ,$ Sharma & Yetton, 2007), additional problems may arise. A well-known problem with multiple regression models is multicollinearity. Since many predictor variables are intercorrelated, it is very difficult to isolate the effects of individual moderators. As a result, even though Hedges & Olkin (1985) described both simple and multiple regression models, Hedges et al (1989) discouraged the use of multiple regression models by stating that ‘[I]t is rarely possible to include more than one or two factors in a formal analysis of heterogeneity due to widespread confounding (collinearity) of potential explanatory variables’ (p. 43). An even more serious problem with multiple regression models is the potential of capitalization on chance (Hunter & Schmidt, 1990, 2004). Briefly, as more variables are entered into the regression model, some predictors can be found significant simply by chance. At the same time, low statistical power of regression models can prevent true moderators from being detected (Hunter & Schmidt, 1990, 2004).

In addition to regression, the existence of moderator variables can be demonstrated through a comparison of subgroup means (e.g., Hwang & Wu, 1990) or variances (e.g., Montazemi & Wang, 1988). Hunter & Schmidt (1990) described a significance test based on comparing two subgroup means. This test has been widely used in prior meta-analytic studies published in both IS and non-IS journals (e.g., Griffeth et al, 2000; Dennis et $^ { a l , }$

2001; Joseph et al, 2007) but Hunter & Schmidt (2004, p. 423) recommended comparing subgroup confidence intervals over the significance test. The reason is that significance tests can cause numerous problems in the interpretation of research findings (Schmidt, 2010). One of the problems is that the test result is a function of both the sample size and the Type I error selected. This problem is relevant to meta-analysis when any significance test (e.g., t or Z test) is used to confirm either a main effect or moderating effect.

To summarize, the process of identifying moderators is full of pitfalls. The first challenge is to determine if variation in observed effect sizes is large enough to suggest the existence of moderators. A common practice is to apply some form of Q tests or the 75% rule. However, as mentioned previously, Q tests in general have low statistical power. On the other hand, a significant Q statistic may be caused by statistical artifacts rather than true moderators (Hunter & Schmidt, 1990, 2004). Uncorrected errors in observed correlations can also result in underestimation of variance due to artifacts, and hence an unwarranted search for moderators. It is important, therefore, to correct as much as possible for errors and biases before attempting moderator analysis.

The second challenge is to decide which approach to use to pinpoint the moderator. A common approach is to use the regression model of Hedges & Olkin (1985). This has been done despite the fact that the assumption of homogeneity has been violated. When a fixed effects analysis is applied to a heterogeneous sample, any moderators found can be suspect. When multiple regression is used the result is further confounded by the capitalization on chance problem.

These two challenges can be overcome if theorysuggested moderators exist and can be used to break the meta-analysis sample into subgroups. Our preferred approach is the subgroup analysis described by Hunter & Schmidt (1990, 2004), as elaborated in the next section.

## The Hunter and Schmidt approach to moderator analysis

Hunter & Schmidt (1990, 2004) identified many statistical artifacts that can cause artificial variation in sample variance. The three most important artifacts are sampling error, measurement error, and range restriction. Sampling error can be corrected if the sample size is known for each individual study. Similarly, measurement error can be corrected if scale reliability is available for each individual study. Chapter 3 of Hunter & Schmidt (2004) describes procedures for correcting each correlation individually.<sup>1</sup> Briefly, for each study, four numbers are calculated or obtained: the corrected correlation, sample size, attenuation factor, and sampling error variance.

The corrected correlation is the reported correlation corrected for unreliable measurement using the formula:

$$
r _ {c} = \frac {r _ {o}}{\sqrt {a} \sqrt {b}},\tag{2}
$$

where $r _ { o }$ is the reported correlation and a and b are the reliability of the independent and the dependent variables, respectively. The attenuation factor is simply the ratio of the reported correlation to the corrected correlation. The attenuation factor and the sample size are used to calculate the weight for each study using the formula:

$$
w _ {i} = N _ {i} A _ {i} ^ {2},\tag{3}
$$

where $N _ { i }$ is the sample size of study i and $A _ { i }$ is the attenuation factor of study i. The sampling error in uncorrected correlation is calculated using the formula:

$$
V a r (e _ {o}) \left[ \frac {(1 - \bar {r} _ {o} ^ {2}) ^ {2}}{(N _ {i} - 1)} \right],\tag{4}
$$

where $\bar { r _ { o } }$ is the sample-size-weighted mean of uncorrected correlations and $N _ { i }$ is the sample size of study i. The sampling error in corrected correlation is calculated using the formula:

$$
V a r (e) = \frac {V a r (e _ {o})}{A _ {i} ^ {2}},\tag{5}
$$

where $A _ { i }$ is the attenuation factor for study i.

Then, the final meta-analysis involves calculating the mean corrected correlation, the variance in the corrected correlations, and the sampling error in the corrected correlations. The formulas are as follows:

$$
\bar {r} _ {c} = \frac {\sum w _ {i} r _ {i}}{\sum w _ {i}},\tag{6}
$$

$$
\operatorname{Var} \left(r _ {c}\right) = \frac {\sum w _ {i} \left(r _ {i} - \bar {r} _ {c}\right) ^ {2}}{\sum w _ {i}},\tag{7}
$$

$$
A v e (V e _ {i}) = \frac {\sum w _ {i} V e _ {i}}{\sum w _ {i}},\tag{8}
$$

where $V e _ { i }$ is the sampling error in corrected correlation of study i given in formula (5). The population correlation and variance are calculated using the following formulas:

$$
\bar {\rho} = \bar {r} _ {c},\tag{9}
$$

$$
\operatorname{Var} (\rho) = \operatorname{Var} \left(r _ {c}\right) - \operatorname{Ave} \left(V e _ {i}\right).\tag{10}
$$

The population standard deviation is the square root of the population variance if the latter is positive; if it is negative then the standard deviation is assumed to be zero.

Hunter & Schmidt (1990, 2004) also developed credibility intervals for the true effect size as a means to detect the existence of moderators. After all possible sources of artificial variation across studies are controlled the corrected standard deviation is used to construct a credibility interval around the mean corrected effect size. This is a posterior probability distribution of the population effect size. An 80% credibility interval, for instance, suggests that 80% of the population effect sizes fall into this range.<sup>2</sup> If the credibility interval is substantially large or includes zero, it would suggest that the mean corrected effect size is not an estimate of a single population correlation, but rather an estimate of the mean of a distribution of population effect sizes (Whitener, 1990). In other words, the width of the credibility interval and whether it contains zero provides a measure of the extent that moderators are working. If theories exist in a research area, a theory-suggested moderator can be used to break the meta-analysis sample into subgroups. Separate meta-analyses can then be performed on the subgroups and credibility intervals can also be constructed within each subgroup to further test for the homogeneity of the subgroups.

While a credibility interval containing zero may indicate the existence of moderators, it could also mean that the true effect size is close to or equal zero. Similarly, it invites subjectivity in determining whether an interval is ‘substantially large’. In a simulation, for example, Koslowsky & Sagie (1993) found that credibility intervals as small as 0.11 could indicate the presence of moderators. A more straightforward application of the credibility intervals is to compare the intervals from subgroups. If the intervals overlap, it means that the subgroups may come from the same population and hence there may be no moderators. This is the approach recommended by Hunter & Schmidt (1990, 2004). An example of this application is provided by Viswesvaran et al (1999).

Credibility intervals are often confused with confidence intervals (Whitener, 1990), which refer to estimates of a single value, for example, the mean population correlation (Hunter & Schmidt, 2004, p. 205). Confidence intervals are constructed around the mean corrected correlation using the standard error rather than the standard deviation of the population values as in the case of credibility intervals. Thus, confidence intervals provide a measure of the error (the sampling error) in the estimate of the population mean correlation. Confidence intervals can play a role in moderator analysis, too. If credibility intervals suggest the presence of moderators and if a theory-suggested moderator is available to break a metaanalysis sample into subgroups, confidence intervals can be calculated around subgroup means. To the extent that these subgroup confidence intervals do not overlap, a moderator can be inferred (Viswesvaran et al, 2002).

## Re-analysis of the Sharma and Yetton sample

If the Hedges & Olkin’s (1985) regression model is used, a Q statistic for testing the homogeneity of correlations across studies is available (p. 235):

$$
Q = \sum_ {i = 1} ^ {k} (n _ {i} - 3) (z _ {i} - z _ {+}) ^ {2},\tag{11}
$$

where $n _ { i }$ is the sample size of study i, $Z _ { i }$ is the z-transformed correlation of study i, and $Z _ { + }$ is the sample-size-weighted mean correlation. The null hypothesis of homogeneous effect sizes is to be rejected if the obtained Q statistic exceeds the critical value from the chi-square distribution with k-1 degrees of freedom, where k is the number of studies. Using data given by Sharma & Yetton (2003), we calculated a Q statistic of 63.21, which greatly exceeds 32.67, the 95% point of the chi-square distribution. This should have precluded the use of the regression model of Hedges & Olkin (1985).

Hedges & Olkin (1985) also provided a goodness-of-fit test for their regression model. The statistic $Q _ { E }$ can be obtained from the ‘error sum of squares’ of the regression model (Hedges & Olkin, 1985, p. 241). When the model is correctly specified, $Q _ { E }$ has a chi-square distribution with $k { - } p$ degrees of freedom, where k is the number of studies and p is the number of parameters including the intercept. A large $Q _ { E } ,$ that is, a large error term, calls for a rejection of the specification of the linear model because ‘parameter estimates in misspecified models are difficult or impossible to interpret’ (Hedges & Olkin, 1985, p. 240). We ran the Sharma and Yetton data through a weighted regression model and found $Q _ { E } = 7 2 . 3 5 ,$ which greatly exceeds 31.41, the 95% point of the chi-square distribution, causing doubt in the validity of their model. This result is not surprising because a wellspecified model is one where all of the population variance is explained by the moderators included in the regression equation – a highly unlikely event since only a single predictor variable was investigated by Sharma & Yetton (2003).

Model misspecification suggests that other variables may be working to cause the wide variance in observed correlations (Hedges & Olkin, 1985, p. 187). However, in this case, the problem may have more to do with the analysis than with the variable. Specifically, the regression should have been run under a random effects model as suggested by the result of the homogeneity test. We ran the Sharma and Yetton data using both models and obtained the results shown in Table 2. The first two rows contain results using the data of Sharma & Yetton (2003), which corrected for sampling error only. The smaller confidence interval under the fixed effects model tipped the scales in the significance level of the moderating effect of task interdependence $( P = 0 . 0 3 9 )$ ). Had a random effects analysis been carried out, task interdependence would not have been considered a moderator using the common Type I error of 5% $( P = 0 . 0 5 9 )$ .

Table 2 Moderating effect of task interdependence

<table><tr><td>Model</td><td>Standardized coefficient</td><td>t-value</td><td>P-value</td></tr><tr><td colspan="4">Correlations corrected for sampling error</td></tr><tr><td>Fixed effects</td><td>0.442</td><td>2.203</td><td>0.039</td></tr><tr><td>Random effects</td><td>0.408</td><td>2.001</td><td>0.059</td></tr></table>

<table><tr><td colspan="4">Correlations corrected for sampling and measurement error</td></tr><tr><td>Fixed effects</td><td>0.433</td><td>2.150</td><td>0.044</td></tr><tr><td>Random effects</td><td>0.395</td><td>1.924</td><td>0.069</td></tr></table>

One may argue that a P-value of 0.059 under the random effects model could be considered ‘significant’ if a more lax Type I error is used. That is why we do not advocate the use of any significance tests for data analysis purposes since the result depends on both the sample size and the Type I error selected. Nevertheless, the impact of the effects model used is noteworthy. Moreover, Sharma & Yetton (2003) corrected for only sampling error. We corrected for measurement error in their data as well and ran the regression again. As shown in the last two rows of Table 2, a larger P-value was obtained with more precise data under both fixed and random effects models. Taking into account the effects model and data precision, the evidence on task interdependence as a moderator is tenuous at best.

Applying the Hunter and Schmidt procedure to the data shown in Table 3, we calculated the mean population correlation as 0.35, with a standard deviation of 0.15. The 80% credibility interval is from 0.16 to 0.54. Even though this interval does not contain zero, it seems large enough to suggest that a search for potential moderators may be in order.

Sharma & Yetton (2003) used a six-item scale to measure task interdependence. Their classification is shown in the second column of Table 3. With a five-point scale for each item, the lowest score is 6 and the highest is 30. We took the mid-point and classified a study as having low task interdependence if its score is 18 or less, and classified a study as having high task interdependence if its score is higher than 18 (see column 3 of Table 3). Subgroup results are presented in Table 4.

As shown in Table 4, the mean population correlation of the low task interdependence group is 0.30, compared with 0.44 of the high task interdependence group. If the population variance of both groups had been equal or close to zero, the moderating effect of task interdependence would have been established. The population variance of the low task interdependence group is close to zero, suggesting homogeneity of this group. The population variance of the high task interdependence group, however, is substantial, suggesting that there is still wide variation within this group. Overall, results based on the subgroup means and variances do not support task interdependence as a moderator.

Table 3 Meta-analysis data

<table><tr><td>Study</td><td>Task inter</td><td>Task inter</td><td>Corr</td><td>Reliability mgt support</td><td>Reliability implem. success</td><td>Corrected correlation</td><td>Sample size</td></tr><tr><td>Adekoya</td><td>10.0</td><td>Low</td><td>0.17</td><td>0.72</td><td>0.80</td><td>0.22</td><td>105</td></tr><tr><td>Bajwa</td><td>19.6</td><td>High</td><td>0.13</td><td>0.87</td><td>0.65</td><td>0.17</td><td>65</td></tr><tr><td>Bean et al</td><td>20.0</td><td>High</td><td>0.21</td><td>0.76</td><td>0.75</td><td>0.28</td><td>104</td></tr><tr><td>Dahmer</td><td>7.7</td><td>Low</td><td>0.18</td><td>0.85</td><td>0.75</td><td>0.23</td><td>344</td></tr><tr><td>Ginzberg</td><td>9.8</td><td>Low</td><td>0.07</td><td>0.76</td><td>0.74</td><td>0.09</td><td>34</td></tr><tr><td>Guimaraes et al</td><td>21.2</td><td>High</td><td>0.01</td><td>0.85</td><td>0.83</td><td>0.01</td><td>118</td></tr><tr><td>Hogan</td><td>26.3</td><td>High</td><td>0.68</td><td>0.86</td><td>0.75</td><td>0.85</td><td>56</td></tr><tr><td>Howard &amp; Mendelow</td><td>7.7</td><td>Low</td><td>0.17</td><td>0.76</td><td>0.75</td><td>0.23</td><td>422</td></tr><tr><td>Leonard-Barton &amp; Deschamps</td><td>13.2</td><td>Low</td><td>0.20</td><td>0.56</td><td>0.75</td><td>0.31</td><td>88</td></tr><tr><td>Maish</td><td>13.7</td><td>Low</td><td>0.19</td><td>0.76</td><td>0.75</td><td>0.25</td><td>59</td></tr><tr><td>Prasad</td><td>12.0</td><td>Low</td><td>0.30</td><td>0.74</td><td>0.77</td><td>0.39</td><td>348</td></tr><tr><td>Purvis</td><td>24.7</td><td>High</td><td>0.52</td><td>0.76</td><td>0.75</td><td>0.69</td><td>176</td></tr><tr><td>Robey</td><td>11.0</td><td>Low</td><td>0.31</td><td>0.76</td><td>0.84</td><td>0.39</td><td>66</td></tr><tr><td>Ruppel</td><td>17.2</td><td>Low</td><td>0.39</td><td>0.66</td><td>0.75</td><td>0.55</td><td>120</td></tr><tr><td>Russo</td><td>12.6</td><td>Low</td><td>0.28</td><td>0.76</td><td>0.75</td><td>0.37</td><td>30</td></tr><tr><td>Sanders &amp; Courtney</td><td>20.7</td><td>High</td><td>0.45</td><td>0.76</td><td>0.75</td><td>0.60</td><td>156</td></tr><tr><td>Sanders &amp; Courtney</td><td>20.7</td><td>High</td><td>0.33</td><td>0.76</td><td>0.75</td><td>0.44</td><td>90</td></tr><tr><td>Sanders &amp; Courtney</td><td>20.7</td><td>High</td><td>0.39</td><td>0.76</td><td>0.75</td><td>0.52</td><td>132</td></tr><tr><td>Schultz &amp; Slevin</td><td>19.7</td><td>High</td><td>0.30</td><td>0.76</td><td>0.75</td><td>0.40</td><td>94</td></tr><tr><td>Thompson et al</td><td>8.7</td><td>Low</td><td>0.31</td><td>0.65</td><td>0.64</td><td>0.48</td><td>212</td></tr><tr><td>Whang</td><td>14.4</td><td>Low</td><td>0.11</td><td>0.81</td><td>0.75</td><td>0.14</td><td>106</td></tr><tr><td>Yoon et al</td><td>12.7</td><td>Low</td><td>0.27</td><td>0.84</td><td>0.75</td><td>0.34</td><td>69</td></tr></table>

Note: (1) Task interdependence: Using the scale of Sharma & Yetton (2003), a score of 18 or less is classified as low and a score higher than 18 is classified as high. (2) Some correlations and sample sizes reported by Sharma and Yetton are incorrect and have been corrected here.

Table 4 Subgroup analysis results

<table><tr><td rowspan="2">Task inter.</td><td colspan="4">Average</td><td colspan="2">80% CV</td><td colspan="2">90% CI</td></tr><tr><td>k</td><td>N</td><td> $\rho$ </td><td> $SD_{\rho}$ </td><td>Lower</td><td>Upper</td><td>Lower</td><td>Upper</td></tr><tr><td>Low</td><td>13</td><td>2003</td><td>0.30</td><td>0.05</td><td>0.24</td><td>0.37</td><td>0.26</td><td>0.35</td></tr><tr><td>High</td><td>9</td><td>991</td><td>0.44</td><td>0.22</td><td>0.17</td><td>0.72</td><td>0.32</td><td>0.56</td></tr></table>

Note: k ¼ number of studies; N ¼ total sample size; $\rho = { \mathsf { m e a n } }$ population correlation; $S D _ { \rho } =$ standard deviation of population correlation; $\mathsf { C V = }$ credibility interval; CI ¼ confidence interval.

![](/api/attachments/DQAK23NU/fulltext/images/452c60eb45559737ff836a4a5f61e98e9c83b4d6b7bb64220511faa22cea8a97.jpg)  
Figure 1 Credibility intervals.

Figure 1 shows the credibility intervals and Figure 2 the confidence intervals graphically of the two subgroups.

![](/api/attachments/DQAK23NU/fulltext/images/a59464943f684107d79b3d923483f0222870cf860b7f80e72573d982c0759a9e.jpg)  
Figure 2 Confidence intervals.

As shown in Figure 1, the credibility interval of the low task interdependence group is encompassed entirely by the credibility interval of the high task interdepen dence group. This suggests that the two subgroups come from the same population. The confidence intervals of the two subgroups shown in Figure 2 also overlap, although only slightly. Again, the evidence does not support the hypothesis that task interdependence has a moderating effect on the relationship between management support and system implementation success. As a follow-up check, a significance test for the difference between the two subgroup means was performed using formulas described by Hunter & Schmidt (1990). The resulting Z is 0.65 with a P-value of 0.52, confirming the non-significant effect.

## Conclusions

Meta-analysis is a powerful tool for knowledge cumulation and synthesis but its application requires careful consideration of methodological issues. The search for moderators in meta-analysis is a promising yet error-prone endeavor. As shown in this paper, incorrect conclusions can be reached by using the common regression approach. Whereas Sharma & Yetton (2003) found management support to be ineffective on implementation success under low task interdependence, our findings confirm the critical role of management support across varying task interdependence contexts. Our analysis shows that the low task interdependence group has a medium mean correlation of 0.30 (Cohen & Cohen, 1983) and a 90% confidence interval of 0.26–0.35, both of which attest to the crucial role of management support when task interdependence is low. Management support is considered essential to a successful system implementation because it provides the required resources, leadership, supervision, and control. Whereas some projects may be less resource-intensive than others, all of them require proper leadership and management (Young and Jordan, 2009). A recent metaanalysis further found that top management support has a positive influence on user participation, which in turn has a positive effect on perceived usefulness, user satisfaction, and system use (Sabherwal et al, 2006). In sum, companies are advised to treat management support as a necessary condition for the successful implementation of all systems due to its direct effect on system success and its indirect effect on user participation.

For researchers, it is important to understand that variance reported in prior studies is, for the most part, the results of statistical artifacts. In addition to sampling and measurement errors, a host of other potential errors discussed in Hunter & Schmidt (2004) have not been addressed in the current study. Another source of error is the common method bias (Podsakoff et al, 2003) or error caused by using the same method to collect data on both the independent and dependent variables. A recent meta-analysis found that common method variance accounts for as much as 56% of the variance in observed correlations between perceived usefulness and use (Sharma et al, 2009). Removing the effects of these statistical artifacts must precede any search for moderators in future meta-analytic studies. Including additional top management support studies in a future metaanalysis may also shed light on the phenomenon. The goal of meta-analysis is to take stock and provide directions in a research area. As new techniques or data become available, follow-up meta-analyses can be applied to provide an updated snapshot of the literature. Even though the current research did not find support for task interdependence as a moderator, it is possible that future meta-analyses may reach a different conclusion or find evidence of other moderators. We call on researchers to continue research into the interaction of relevant variables in both primary and meta-analytic studies.

It is worth repeating that it is important to remove as much as possible statistical artifacts before individual effect sizes are combined in a meta-analysis. Compared with the mean effect size of 0.35 found in this research, Sharma & Yetton (2003) reported a mean correlation of 0.24. Our estimated value of 0.35 is 48% larger than the underestimated value of 0.24 reported by Sharma & Yetton (2003). This is a very substantial difference. A small mean coupled with a substantial observed variance can easily lead the analyst to unwarranted searches for moderators. The larger mean in our result is due to the additional correction for measurement error. As more data become available additional artifacts should be removed in future meta-analyses, which will help determine more clearly if other moderators exist to mediate the effect of management support.

In sum, we recommend meta-analysts follow the Hunter and Schmidt approach to correct for statistical artifacts as much as they can. If substantial variance remains after the effects of artifacts are accounted for, moderator analysis can then be conducted based on theory-suggested variables. The evidence should come from comparisons of subgroup credibility and confidence intervals. Figure 3 depicts our recommended process for moderator analysis.

![](/api/attachments/DQAK23NU/fulltext/images/1fa4a3fe0e64137e897531aa212ca4bea2c1ee66f7656ac316a45a77926528e8.jpg)  
Figure 3 Moderator analysis process chart.

Our approach is not without limitations. First, breaking studies into subgroups at times entails dichotomizing a continuous variable such as the number of users. It is likely that no generally accepted ways exist to group the studies. For example, should we have two groups: light and heavy users or three groups: light, medium, and heavy users? Generally, the burden of proof is higher when the number of groups is larger, that is, it will be more difficult to show three non-overlapping credibility intervals than two. We used the ‘easy’ test and tried to show the moderating effect of task interdependence

## About the authors

Mark I. Hwang is a Professor of Information Systems. He holds a Ph.D. in Business Computer Information Systems from the University of North Texas. Dr. Hwang has published articles in business and information systems journals including Advances in Accounting, Business Intelligence Journal, Data Base, Information & Management, Information Resources Management Journal, International Journal of Auditing, International Journal of Business, Journal of Computer Information Systems, Journal of Information, Information Technology, and Organizations, Journal of Information Science, Journal of Information Technology Management, Journal of Management Systems, Managerial Auditing Journal, Multinational Business Review, and Omega. His research interests include business intelligence, data mining, and meta-analysis.

## References

ADEKOYA AA (1993) Evaluation of factors promoting successful microcomputing implementation in the Nigerian workplace. Unpublished doctoral dissertation, Syracuse University.

ALAVI M and JOACHIMSTHALER EA (1992) Revisiting DSS implementation research: a meta-analysis of the literature and suggestions for researchers. MIS Quarterly 16(1), 95–116.

ARONSON E, ELLSWORTH P, CARLSMITH J and GONZALES M (1990) Methods of Research in Social Psychology, 2nd edn, McGraw-Hill, New York.

BAJWA DS (1993) An empirical investigation of the antecedents of executive information system success. Unpublished doctoral dissertation, Southern Illinois University at Carbondale.

BARLEY SR (1986) Technology as an occasion for structuring: evidence from observations of CT scanners and the social order of radiology departments. Administrative Science Quarterly 31(1), 78–108.

BEAN AS, NEAL RD, RADNOR M and TANSIK DK (1975) Structural and behavioral correlates of implementation in U.S. business organizations. In Implementing Operations Research/Management Science (Schultz RL and Slevin DP, Eds), American Elsevier, New York.

BENBASAT I and LIM L (1993) The effects of group, task, context, and technology variables on the usefulness of group support systems: a meta-analysis of experimental studies. Small Group Research 24(4), 430-462.

using two groups and failed. A follow-up test using three groups produced identical result as expected. Second, when more than one potential moderator exists, the ideal is to conduct a fully hierarchical moderator analysis (Hunter & Schmidt, 2004, p. 424), but often there are not sufficient studies in the meta-analysis to allow this. For example, King & He (2006) investigated two moderators, the type of users and the type of usage, in their metaanalysis of the technology acceptance model literature. They performed two separate analyses for the two moderator variables. However, since many variables in a research model are correlated, unless the two moderators are totally independent with additive effects, a single moderator analysis with four subgroups should be conducted. In a fully hierarchical analysis some of the resulting cells may contain too few studies to allow for a meaningful analysis. In this case, the analysis may have to wait until more studies are accumulated.

Frank L. Schmidt is the Ralph L. Sheets Professor of Human Resources in the Tippie College of Business at the University of Iowa. He was one of the two co-inventors of validity generalization methods and has published over 150 journal articles and book chapters. He received the Distinguished Scientific Contributions Award (with John Hunter) from the American Psychological Association (APA) and also received the Distinguished Career Award from the Human Resources Division of the Academy of Management, and the Michael R. Losey Human Resources Research Award from the Society for Human Resource Management (SHRM). He received his doctorate in Industrial/Organizational Psychology from Purdue University.

BORENSTEIN M, HEDGES LV, HIGGINS JPT and ROTHSTEIN HR (2009) Introduction to Meta-Analysis. Wiley, Chichester, West Sussex, United Kingdom.

COHEN J and COHEN P (1983) Applied Multiple Regression/Correlational Analysis for the Behavioral Sciences. Lawrence Erlbaum Associates, Hillsdale, NJ.

C H (1997) Some finer points in meta-analysis. In How Science Takes Stock: The Story of Meta-Analysis (Hunt M, Ed), Russell Sage Foundation, NY.

DAHMER BL (1994) Factors associated with implementation and usage of technology-based training: developing and testing a technology implementation model. Unpublished doctoral dissertation, Vanderbilt University.

DENNIS AR, WIXOM BH and VANDENBERG RJ (2001) Understanding fit and appropriation effects in group support systems via meta-analysis. MIS Quarterly 25(2), 167–193.

GARRITY JT (1963) Top management and computer profits. Harvard Business Review 41(4). 6–12.172–174.

GINZBERG MJ (1981) Early diagnosis of MIS implementation failure: promising results and unanswered questions. Management Science 27(4), 459–478.

GLASS GV (1976) Primary, secondary, and meta-analysis of research. Educational Researcher 5(9). 3–8.

GLASS GV and SMITH ML (1979) Meta-analysis of the relationship between class size and achievements. Educational Evaluation and Policy Analysis 1, 2–16.

GLASS GV, MCGAW B and SMITH ML (1981) Meta-Analysis in Social Research. Sage Publications, California.

GRIFFETH RW, HOM PW and GAERTNER S (2000) A meta-analysis of antecedents and correlates of employee turnover: update, moderator tests, and research implications for the next millennium. Journal of Management 26(3), 463–488.

GUIMARAES T, IGBARIA M and LU M (1992) The determinants of DSS success: an integrated model. Decision Sciences 23(2), 409–430.

HEDGES LV and OLKIN I (1985) Statistical Methods for Meta-Analysis. Academic Press, California.

H LV, S JA and W G (1989) A Practical Guide to Modern Methods of Meta-Analysis. National Science Teachers Association, Washington, DC.

HOGAN PT (1994) Information engineering implementation issues: an information system manager’s perspective. Unpublished doctoral dissertation, University of Texas at Arlington.

HOWARD GS and MENDELOW AL (1991) Discretionary use of computers: an empirically derived explanatory model. Decision Sciences 22(2), 241–265.

HUNTER JE and SCHMIDT FL (1990) Methods of Meta-Analysis: Correcting Error and Bias in Research Findings. Sage Publications, Newbury Park, CA.

HUNTER JE and SCHMIDT FL (2004) Methods of Meta-Analysis: Correcting Error and Bias in Research Findings, 2nd edn, Sage Publications, Newbury Park, CA.

HUNTER JE, SCHMIDT FL and JACKSON GB (1982) Meta-Analysis: Cumulating Research Findings across Studies. Sage Publications, Beverly Hills, CA.

HUNTER III SD (2010) Same technology, different outcome? Reinterpreting Barley’s technology as an occasion for structuring. European Journa of Information Systems 19, 689–703.

HWANG MI (1996) The use of meta-analysis in MIS research: promises and problems. Data Base 27(3), 35–48.

HWANG MI and WU JP (1990) The effectiveness of computer graphics for decision support: a meta-analytic integration of research findings. Data Base 21(2 & 3), 11–20.

IFINEDO P (2008) Impacts of business vision, top management support, and external expertise on ERP success. Business Process Management Journal 14(4), 551–568.

JOSEPH D, NG K, KOH C and ANG S (2007) Turnover of information technology professionals: a narrative review, meta-analytic structural equation modeling, and model development. MIS Quarterly 31(3), 547–577.

K W and H J (2005) Understanding the role and methods of metaanalysis in IS research. Communications of the Association for Information Systems 16, 665–686.

KING W and HE J (2006) A meta-analysis of the technology acceptance model. Information & Management 43, 740–755.

KOHLI R and DEVARAJ S (2003) Measuring information technology payoff: a meta-analysis of structural variables in firm-level empirical research. Information Systems Research 14(2), 127–145.

KOSLOWSKY M and SAGIE A (1993) On the efficacy of credibility intervals as indicators of moderator effects in meta-analytic research. Journal of Organizational Behavior 14(7), 695–699.

LEONARD-BARTON D and DESCHAMPS I (1988) Managerial influence in the implementation of new technology. Management Science 34(10), 1252–1265.

MAISH AM (1979) A user’s behavior toward his MIS. MIS Quarterly 3(1), 39–52.

MoNTAZEMI AR and WANG S (1988) The effects of modes of information presentation on decision-making: a review and meta-analysis. Journa of Management Information Systems 5(3), 101–127.

NATIONAL RESEARCH COUNCIL (1992) Combining Information: Statistica Issues and Opportunities for Research. National Academy of Sciences, Washington, DC.

PETTER S and MCLEAN ER (2009) A meta-analytic assessment of the DeLone and McLean IS success model: an examination of IS success at the individual level. Information & Management 46, 159–166.

PODSAKOFF PM, MACKENZIE SB, LEE JY and PODSAKOFF NP (2003) Common method biases in behavioral research: a critical review of

the literature and recommended remedies. Journal of Applied Psychology 88(5), 879–903.

PRASAD J (1994) The role of end-user’s attitudes in the acceptance of office automation: a field study in a public organization. Unpublished doctoral dissertation, University of Pittsburg.

PURVIS RL (1994) The effects of knowledge embeddedness on the diffusion and infusion of case technologies within organizations. Unpublished doctoral dissertation, Florida State University.

RANGANANATHAN C, WATSON-MANHEIM MB and KEELER J (2004) Bringing professionals on board: lessons on executing IT-enabled organizational transformation. MIS Quarterly Executive 3(3), 151–160.

RAUDENBUSH SW (1994) Random effects models. In Handbook of Research Synthesis (Cooper H and Hedges LV, Eds), Russell Sage Foundation, New York.

ROBEY D (1979) User attitudes and management information system use. Academy of Management Journal 22(3), 527–538.

RUPPEL CP (1995) Correlates of the adoption and implementation of programmer/analyst telework: an organizational perspective. Unpublished doctoral dissertation, Kent State University.

RUSSO NL (1993) The impact of context on innovation in information systems. Unpublished doctoral dissertation, Georgia State University.

SABHERWAL R, JEYARAJ J and CHOWA C (2006) Information system success: individual and organizational determinants. Management Science 52(12), 1849–1864.

SANDERS GL and COURTNEY JF (1985) A field study of organizational factors influencing DSS success. MIS Quarterly 9(1), 77–93.

SCHEPERS J and WETZELS M (2007) A meta-analysis of the technology acceptance model: investigating subjective norm and moderation effects. Information & Management 44, 90–103.

SCHMIDT FL (2010) Detecting and correcting the lies that data tell. Perspectives on Psychological Science 5(3), 233–242.

SCHMIDT FL, OH I and HAYES TL (2009) Fixed- versus random-effects models in meta-analysis: model properties and an empirical comparison of differences in results. British Journal of Mathematical and Statistical Psychology 62(1), 97–128.

SCHULTZ RL and SLEVIN DP (1975) Implementation and organizational validity: an empirical investigation. In Implementing Operations Research/Management Science (Schultz RL and Slevin DP, Eds), American Elsevier, New York.

SHARMA R and YETTON P (2003) The contingent effects of management support and task interdependence on successful information systems implementation. MIS Quarterly 27(4), 533–555.

SHARMA R and YETTON P (2007) The contingent effects of training, technical complexity, and task interdependence on successful information systems implementation. MIS Quarterly 31(2), 219–238.

S R, Y P and C J (2009) Estimating the effect of common method variance: the method-method pair technique with an illustration from TAM research. MIS Quarterly 33(3), 473–490.

SMITH ML and GLASS GV (1977) Meta-analysis of psychotherapy outcome studies. American Psychologist 32(9), 752–760.

THOMPSON RL, HIGGINS CA and HOWELL JM (1991) Personal computing: toward a conceptual model of utilization. MIS Quarterly 15(1), 125–143.

VISWESVARAN C, ONES DS and SCHMIDT FL (2002) The moderating influence of job performance dimensions on convergence of supervisory and peer ratings of job performance: unconfounding construct-level convergence and rating difficulty. Journal of Applied Psychology 87(2), 345–354.

VISWESVARAN C, SANCHEZ JI and FISHER J (1999) Therole of social support in the process of work stress: a meta-analysis. Journal of Vocational Behayior 54(2). 314–334

WHANG J (1992) An empirical study of factors influencing interorganizational information systems implementation: a case study of the real estate industry. Unpublished doctoral dissertation, The University of Nebraska.

WHITENER EM (1990) Confusion of confidence intervals and credibility intervals in meta-analysis. Journal of Applied Psychology 75(3), 315–321.

WU J and LEDERER A (2009) A meta-analysis of the role of environmentbased voluntariness in information technology acceptance. MIS Ouarterly 33(2). 419–432

YooN Y, GUIMARAEs T and O'NEAL O (1995) Exploring the factors associated with expert systems success. MIS Quarterly 19(1), 83–106.

YOUNG R and JORDAN E (2009) Top management support: mantra or necessity? International Journal of Project Management 26(7), 713–725.
