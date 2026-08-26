---
otero_id: 16124
otero_key: "SENK7TKJ"
title: "Does PLS Have Advantages for Small Sample Size or Non-Normal Data?"
authors: "Dale L. Goodhue; William Lewis; Ron Thompson"
year: "2012"
journal: "MIS Quarterly"
doi: "10.2307/41703490"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Does PLS Have Advantages for Small Sample Size or Non-Normal Data?
Author(s): Dale L. Goodhue, William Lewis and Ron Thompson
Source: MIS Quarterly, Vol. 36, No. 3 (September 2012), pp. 981-1001
Published by: Management Information Systems Research Center, University of Minnesota
Stable URL: http://www.jstor.org/stable/41703490
Accessed: 28-02-2018 14:19 UTC

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://about.jstor.org/terms

# DOES PLS HAVE ADVANTAGES FOR SMALL SAMPLE SIZE OR NON-NORMAL DATA? $^{1}$

Dale L. Goodhue
Terry College of Business, MIS Department, University of Georgia,
Athens, GA 30606 U.S.A. {dgoodhue@terry.uga.edu}

William Lewis
{william.w.lewis@gmail.com}

Ron Thompson
Schools of Business, Wake Forest University,
Winston-Salem, NC 27109 U.S.A. {thompsrl@wfu.edu}

There is a pervasive belief in the MIS research community that PLS has advantages over other techniques when analyzing small sample sizes or data with non-normal distributions. Based on these beliefs, major MIS journals have published studies using PLS with sample sizes that would be deemed unacceptably small if used with other statistical techniques. We used Monte Carlo simulation more extensively than previous research to evaluate PLS, multiple regression, and LISREL in terms of accuracy and statistical power under varying conditions of sample size, normality of the data, number of indicators per construct, reliability of the indicators, and complexity of the research model. We found that PLS performed as effectively as the other techniques in detecting actual paths, and not falsely detecting non-existent paths. However, because PLS (like regression) apparently does not compensate for measurement error, PLS and regression were consistently less accurate than LISREL. When used with small sample sizes, PLS, like the other techniques, suffers from increased standard deviations, decreased statistical power, and reduced accuracy. All three techniques were remarkably robust against moderate departures from normality, and equally so. In total, we found that the similarities in results across the three techniques were much stronger than the differences.

Keywords: Partial least squares, PLS, regression, structural equation modeling, statistical power, small sample size, non-normal distributions, Monte Carlo simulation

## Introduction

There is a pervasive belief in the Management Information Systems (MIS) research community that for small sample

A much earlier version of this paper was published in a conference proceedings (Goodhue et al. 2006).

sizes or data with non-normal distributions, partial least squares (PLS) has advantages that make it more appropriate than other statistical estimation techniques such as regression or covariance-based structural equation modeling (CB-SEM) with LISREL, Mplus, etc. Partly because of these beliefs, PLS has been widely adopted in the MIS research community.

To get a clearer picture of the extent of these beliefs in the MIS field, we examined three top MIS journals (Information Systems Research [ISR], Journal of Management Information Systems [JMIS], and MIS Quarterly [MISQ]). We identified all articles that used some form of path analysis published from 2006 to 2010, inclusive—188 articles across the three journals. Overall, PLS was used for 49% of the path analysis papers in these three MIS journals. Of the 90 articles using PLS, at least 35% stated that PLS had special abilities relative to small sample size and/or non-normal distributions. Thirteen of these studies (14%) had sample sizes smaller than 80 (which we will show is insufficient). Four of the 13 papers stated that PLS had these special abilities without any supporting citations. This suggests that these beliefs are so widely accepted they are seen as no longer needing support from the literature.

There are a relatively small number of articles that are most often cited to support the claim that PLS has advantages at small sample sizes (e.g., Barclay et al. 1995; Chin 1998; Chin et al. 2003; Gefen et al. 2000), with other sources also cited at times (Chin and Newsted 1999; Falk and Miller 1992; Fornell and Bookstein 1982; Lohmöller 1988). The most commonly cited minimum sample rule for PLS might be termed the “10 times” rule, which states that the sample size should be at least 10 times the number of incoming paths to the construct with the most incoming paths (Barclay et al. 1995; Chin and Newsted 1998). Some MIS researchers have also cited Falk and Miller (1992) to justify using a “5 times” rule.

Chin and Newsted (1999, p. 327) added the following caution to their description of the 10 times rule:

Ideally, for a more accurate assessment, one needs to specify the effect size for each regression analysis and look up the power tables provided by Cohen (1988) or Green's (1991) approximation to these tables.

However, MIS researchers appear to have interpreted these and similar statements to imply that, although one could use Cohen's tables to determine the minimum allowable sample size required to conduct a given study, one can also use the "rule of 10" or even the "rule of 5." For example Kahai and Cooper (2003, p. 277) used a sample size of 31 in a study published in JMIS; Malhotra et al. (2007, p. 268) used a sample size of 41 in ISR. Chin and his coauthors used a sample size of 17 in MISQ (Majchrzak et al. 2005, p. 660).

A recent editorial by Gefen, Rigdon, and Straub (2011) in MIS Quarterly provided guidelines for choosing between PLS and CB-SEM analysis techniques. They expressed some concern about PLS and sample size, referencing Marcoulides and Saunders (2006) with respect to “the apparent misuse of perceived leniencies such as assumptions about minimum sample size in partial least squares (PLS),” but in their article proper they did not directly address the issue. However, in their Appendix B they did distinguish between regression on the one hand (where they suggest that minimum sample size is primarily an issue of statistical power and is well addressed by Cohen's 1988 guidance), and PLS and CBSEM on the other hand (where sample size plays a more complex role). They do note that “the core of the PLS estimation method—ordinary least squares—is remarkably stable even at low sample sizes.” They suggest that this gave rise to the “10 times” rule, although they point out that it “is only a rule of thumb, however, and has not been backed up with substantive research.” Similarly, Ringle, Sarstedt, and Straub (2012) noted that very few researchers employing PLS reported any attempts to determine the adequacy of their sample size (other than the 10 times rule), but they did go on to suggest that power tables from regression could be used.

Hair et al. (2011) also provided guidelines for when the use of PLS is appropriate, and with respect to sample size they repeated the “10 times” rule. While they did go on to caution that “although this rule of thumb does not take into account effect size, reliability, the number of indicators, and other factors known to affect power and can thus be misleading,” they still conclude that “it nevertheless provides a rough estimate of minimum sample size requirements.” In their summary table of guidelines for applying PLS, the 10 times rule is the only guidance for minimum sample size, without any caveat. Likewise in another work, Hair, Ringle, and Sarstedt (2011) recommend the 10 times rule without any caveat.

Statements about PLS and non-normal data are also common, such as the following quote cited widely in MIS research: "Because PLS estimation involves no assumption about the population or scale of measurement, there are no distributional requirements" (Fornell and Bookstein, 1982, p. 443). Many seem to have interpreted this to mean that while the distribution of data used in a regression or LISREL analysis is important, it is less important or perhaps even irrelevant for PLS analysis. More recently it has been suggested the PLS may not have an advantage on this score, because new estimation techniques with CB-SEM provide options that are quite robust to departures from normality (Gefen et al. 2011; Hair et al. 2011). Nonetheless, recommendations to use PLS when data are to some extent non-normal still appear (Hair, Ringle, and Sarstedt 2011, p. 144).

Thus while some articles and editorials have issued cautions against assuming too much for PLS's special capabilities (e.g., Gefen et al. 2011; Goodhue et al. 2006; Marcoulides and Saunders 2006), many of the recommendations lack specificity. In particular, cautions about the 10 times rule for sample size typically do not suggest any concrete alternative, even though that rule's validity has not been tested empirically. As a result, MIS journal articles continue to cite and use the 10 times rule. For example, Zhang et al. explicitly use it in determining the minimum sample size for their PLS analysis in their December 2011 MIS Quarterly article. Clearly a subset of the social science research community still believes that the 10 times rule provides an acceptable guideline.

In our study we use Monte Carlo simulation to empirically address the issues of small sample sizes and non-normal distributions. Specifically, we look at the relative efficacy of PLS, regression, and CB-SEM (or as we will refer to it here, LISREL $^{2}$ ) under a variety of conditions. By efficacy we mean their ability to support a researcher's need to statistically test hypothesized relationships among constructs. $^{3}$ We specifically test to see whether these techniques have different abilities in terms of: (1) arriving at a solution, (2) producing accurate path estimates, (3) avoiding false positives (Type 1 errors), and (4) avoiding false negatives (Type 2 errors, related to statistical power). We also test each of the techniques against commonly accepted standards (e.g., at least 80% power, no more than 5% false positives, and path estimates that are as accurate as possible). A primary goal of our work is to provide researchers with some concrete findings to help inform decisions relating to: (1) designing research studies, (2) selecting analysis techniques, and (3) interpreting the results obtained.

We accomplish this by using Monte Carlo simulation to compare results across different statistical analysis techniques (Goodhue et al. 2012). We employ PLS, regression and LISREL to analyze identical collections of sets of 500 data sets each, using the identical research model. We start with a relatively simple model and five different sample sizes, and then do sensitivity testing by varying distributional properties of the data, number and reliability of indicators, and complexity of the model.

Our study provides four important contributions. First, we show that as sample sizes are reduced, all three techniques suffer from increasing standard deviations for the path estimates and the attendant decrease in accuracy, and all have about the same resulting loss in statistical power. $^{4}$ This strongly suggests that PLS has no advantage for either accuracy or statistical power at small sample size, and that the 10 times rule is a misleading guide to minimal sample size for all three techniques equally. Second, all three techniques were relatively robust (and equally so) to moderate departures from normality and all suffered somewhat (again about equally) under extreme departures from normality. This strongly suggests that PLS has no advantage with non-normal distributions. Third, these results hold with simple and more complex models. Fourth, LISREL consistently produces more accurate estimates of path strengths. PLS and regression are not only less accurate than LISREL and about equally so, but the amount of underestimation is quite consistent with Nunnally and Bernstein's (1994, pp. 241, 257) equation for the attenuation of relationship strength due to measurement error. This leads us to the conclusion that PLS, like regression, does not take measurement error into account in its path estimates, as opposed to LISREL and other CB-SEM techniques which do.

In this note we restrict our focus to situations where researchers use PLS, LISREL, or regression and have a hypothesized model with reflective, multi-indicator construct data. Given our focus on the efficacy of the three techniques rather than examining how they operate, we do not describe the techniques in detail. Interested readers are encouraged to review published work (e.g., Barclay et al. 1995; Chin 1998; Chin and Newsted 1999; Fornell 1984; Fornell and Bookstein 1982; Gefen et al. 2000; Hayduk 1987; Kline 1998) to obtain more detailed descriptions of the different statistical analysis techniques. However, we will provide enough of a description of each technique to justify the presumption that we might get different path or statistical significance estimates depending on which technique was used, even using the exact same input data.

Following Rönkkö and Ylitalo (2010), we can think of regression and PLS as both having three steps: (1) determining the weightings for the construct indicators, (2) using those weights to calculate composite construct scores and using ordinary least squares to calculate path estimates, and (3) determining the statistical significance of the path estimates. For regression, the first step is usually accomplished by giving equal weights to all indicators. Then composite scores are determined, and each dependent composite construct and all its predictors are then analyzed separately. Regression uses ordinary least squares (linear algebra) to calculate the solution for the path values that minimizes the squared differences between the predicted and the actual scores for each dependent construct. There is no iteration involved. The regression solution includes estimates of the standard deviation of each path estimate, from which statistical significance can be determined, using normal distribution theory.

In PLS, step one is the core of its uniqueness. As opposed to regression where equal weights are used, PLS iterates through a process to find the “optimal” indicator weights for each construct, such that the overall $R^{2}$ for all dependent constructs is maximized. The second step in PLS, as in regression, uses the indicator weights to calculate construct scores which are then used in ordinary least squares to determine final path estimates. The third step in PLS is to determine the standard deviations of those path estimates with bootstrapping. $^{5}$ This third PLS step contrasts with regression where normal distribution theory is used, but bootstrapping could also be used with regression. Thus note that both PLS and regression use weighted averages of indicator values to develop construct scores, and both use ordinary least squares to determine path values. The critical difference between the two in terms of path values is that regression uses equally weighted indicator scores, while PLS has a process intended to optimize weights.

LISREL is quite different from regression and PLS. It also uses linear algebra, but its equations include all constructs, all indicators, all error terms, and all relationships between them in a single analysis. LISREL iterates between two processes: (1) taking a candidate solution for the various parameters (with candidate values for paths between constructs, error variances, etc.) and generating the implied covariance matrix for the indicators, and (2) comparing that implied covariance matrix with the sample covariance matrix. From this comparison, the degree of fit between the candidate solution and the actual data is determined, and changes to the various parameters in the candidate solution are suggested. This then feeds back into step 1, until limited changes are suggested. Since step 1 also includes estimates of the standard deviation of each path estimate, statistical significance can be determined using normal distribution theory.

Monte Carlo simulation has been used to study issues such as bias sizes in PLS estimates (Cassel et al. 1999), impact of different correlation structures on goodness of fit tests (Fornell and Larcker 1981), and the efficacy of PLS with product indicators versus regression in detecting interaction effects (Chin et al. 2003; Goodhue et al. 2007). The remainder of this paper begins with a quick explanation of Monte Carlo simulation and how it can be used to assess the efficacy of different statistical techniques. We do this so we can explain how our examination of the simulation data goes significantly beyond that employed by previous researchers who investigated PLS using Monte Carlo simulation (Cassel et al. 1999; Chin et al. 2003; Chin and Newsted, 1999). Following that, we describe four simulation studies used to test the three techniques under varying conditions. We end with a discussion of our overall findings, and their implications.

## How to Test "Efficacy" with Monte Carlo Simulation: Our Approach and Previous Approaches

Use of the Monte Carlo simulation approach requires the researcher to start with a prespecified “true” model (such as shown in Figure 1) that includes both the strength of paths and the amount of random variance in linkages (between constructs, and between constructs and their indicators). From the prespecified model, sets of simulated questionnaire responses are generated using random number generators. $^{6}$ Then the same sets of questionnaire responses are analyzed by each of the three techniques in turn. The analysis results can be compared across techniques and against accepted standards. Repeating this process with many different data sets (in our case, 500) for each condition tested removes the worry that any given result is atypical.

Figure 1 shows the model used as the basis for much of our analysis. (We will modify it to test different specific issues.) We have four constructs (Ksi1 through Ksi4) that “cause” changes in the value of a fifth construct (Eta1). Three of the four independent constructs have the following effect sizes: large (.35), medium (.15), and small (.02), to correspond to Cohen’s (1988) suggested values. We also include an effect size of zero so we can test for false positives. See the notes in Figure 1 for more detail.

![](/api/attachments/SENK7TKJ/fulltext/images/9f9a5687528ca58e58b65c0d14de2b9415ceb734e90c1bbb7d7390d7a3a49480.jpg)

The five constructs are each measured by three reflective indicators with weights of .7, .8, and .9, giving them a Cronbach's alpha of .84. In addition to the path coefficients and the indicator loadings, random error is added to the indicator scores and to the value for Eta1, so as to give each a variance of 1.0.

\*\*Although only three intercorrelations between the Ksi constructs are shown (to keep the diagram from becoming too cluttered), in our analysis it is assumed that all four constructs correlate freely with each other. Since regression and PLS impose no constraints on correlations between exogenous constructs, in our LISREL analysis we also allow the constructs to freely correlate at whatever level best fits the data. We do this to keep the assumptions for regression, PLS, and LISREL equivalent on this score, even though the data is generated from a model that has the Ksi constructs independent.

\*\*\*Following Cohen (1988), the relationship between the path coefficients and the effect sizes is given below. By construction (we generate the data that way) Ksi1 through Ksi4 are independent, and all five constructs are N(0,1) distributed and therefore have a variance of 1.0. Therefore, the partial R $^{2}$ for each Ksi is the square of the partial correlation (or the square of the path coefficient). With path coefficients of .48, .314, and .114, the partial R $^{2}$ s are .230, .099, and .013. This gives an overall R $^{2}$ of .342. Effect size is then the partial R $^{2}$ divided by the unexplained variance. Unexplained variance is (1 - .342) = .658. This gives:

Gamma1 = .230 / (1 - .342) = .350

Gamma2 = .099 / (1 - .342) = .150

Gamma3 = .013 / (1 - .342) = .020

Figure 1. The Simple Model: The Basis for Studies 1 Through 3

We use an example to illustrate how our studies differ from previous Monte Carlo simulation studies (and to explain why we therefore draw different conclusions). In this illustration we will focus on the Gamma2 path (medium effect size) of Figure 1, and compare the results from regression analysis with the results from PLS analysis. The rule of 10 would suggest n = 40 is a minimum sample size for PLS given the model in Figure 1.

Using a random number generator and the relationships from the Figure 1 model, we generated 500 data sets of 40 "questionnaires" each (20,000 questionnaire responses total). This could be thought of as 500 researchers, each with a sample size of $n = 40$ . In this example, we are interested in predicting what a $501^{\text{st}}$ researcher with a similar sample size from the same population might find if he or she analyzed that data set with PLS or regression. Figure 2 shows the results of analyzing the 500 data sets first with regression and then with PLS. Figure 2a is a histogram of the 500 regression path estimates for Gamma2; Figure 2c shows the same thing for PLS estimates, based on exactly the same 500 data sets.

![](/api/attachments/SENK7TKJ/fulltext/images/b8fe5cb530f66e80b4236afc6bb8205368cc43e354edef0b106c605cbda53a3e.jpg)  
Figure 2. Monte Carlo Results for Medium Effect Size, N = 40  
However, we went further than the comparisons done by earlier studies and also examined the number of data sets that resulted in statistically significant paths and the standard deviations of the 500 path estimates. Figures 2b and 2d show the 500 associated t statistics for Gamma2, using regression and PLS respectively. Since the t statistic cutoff for p < .05 in this regression is $2.03^{7}$ (the heavy dotted vertical line), we see in Figure 2b that about 40% of the 500 regression data sets found a statistically significant Gamma2 path. From Figure 2d we see that 41% of the PLS data sets found a significant Gamma2 path.

In Figure 2a, the mean Gamma2 estimate across 500 data sets is .255 for regression, as shown by the heavy dotted vertical line. Lighter dotted lines show the 95% confidence interval for the path value the 501 $^{st}$ research should expect. Notice in Figure 2c that PLS has a slightly higher mean value for Gamma2 (.273). Although the difference is not large, our results for Gamma2 accuracy are consistent with those of Chin and Newsted (1999); PLS produces a slightly larger estimate than regression, on average.

$^{7}$ For an n = 40 regression with four constructs and a constant, the degrees of freedom are 40 - 5 = 35.

PLS seems to have the advantage: a slightly higher average path estimate and a slightly higher statistical power. But this seeming advantage is misleading. First of all, the 95% confidence intervals for the path value the 501 $^{st}$ researcher will likely see for Gamma2 using regression (in Figure 2a) and PLS (in Figure 2C) almost completely overlap. Although PLS has a higher mean value than regression (.018 higher), that difference is not statistically significant at the p < .05 level. Second, for statistical power, the 95% confidence interval around regression's power (40%) and PLS's power (41%) goes from about .36% to about .45%. $^{8}$ Thus the small difference of 40% versus 41% is not even close to being statistically significant. From a statistical point of view, neither the accuracy nor the power obtained from PLS can be distinguished from that obtained from regression in this analysis.

More importantly, since 80% power is the generally sought minimum acceptable level of power, both 40% and 41% power are unacceptably low. About 60% of the time, true medium effect size paths will not be detected by either technique at this sample size.

Let us focus for a minute just on the issue of accuracy of PLS estimates. In three of the empirical articles often used to justify PLS's special capabilities (Cassel et al. 1999; Chin et al. 2003; Chin and Newsted), $^{9}$ the authors displayed both average path estimates (or average biases) and standard deviations of the path estimates. However, each set of authors focused attention almost entirely on the average accuracy of the path estimate, concluding that it did not change much with decreases in sample size. None placed much importance on the fact that as their sample size went down, standard deviations of the path estimates went up:

• from .069 at n = 500 to .250 at n = 20 for Chin et al. (a factor of 3.5);

• from .107 at n = 200 to .380 at n = 20 for Chin and Newsted (a factor of 3.5); and

• from .019 at n = 1000 to .092 at n = 50 for Cassel et al. (a factor of 4) $^{10}$

Focusing on the average path estimate bias can mask serious problems, since a combination of very high and very low path estimates might still average out to about the true value. Our interpretation of the results in all three of these papers is that as sample size goes down, the average bias across hundreds of data sets does not change much, but the “wildness” (standard deviation) of individual path estimates increases considerably. In the context of Figures 2a and 2c, the wider the “spread” of the data in the histogram (and the wider its 95% confidence interval), the greater the “wildness” of the estimates. Increasingly wild estimates do not suggest to us that PLS is robust to changes in sample size. We do not mean to suggest that PLS is more wild than regression or LISREL at these sample sizes. As will be seen, we only suggest that all three techniques suffer at small sample sizes, and about equally so.

Therefore, in our analysis, we will look at the average bias of the 500 path estimates as the above articles did, but also at the average of the standard deviations of those path estimates and at the proportion of data sets that found a significant path. Very different conclusions will be drawn by using this additional information.

## Study 1: The Effect of Sample Size with a Simple Model

In this study, our objective was to assess the relative efficacy of the three techniques under conditions of varying sample size, using normally distributed data, well measured constructs, and a simple but realistic model of construct relationships. We used the model shown in Figure 1, and sample sizes of 20, 40, 90, 150, and 200, generating 500 data sets for each sample size. $^{[11]}$ For our model, 20 is the required sample size based on the “rule of 5”; 40 is the required sample size based on the “rule of 10”; 90 is perhaps just below the minimum sample size acceptable for LISREL, 200 is a conservative estimate of minimum sample size based on 5 times the number of LISREL estimated parameters, $^{12}$ and 150 is roughly the mid-point between 90 and 200. For each of the five sample sizes, we analyzed the 500 data sets using multiple regression, $^{13}$ PLS-Graph, $^{14}$ and LISREL. $^{15}$ Results for Study 1 are displayed in graphical form in Figure 3, with actual values in Appendix A, Tables A1, A2, and A3.

Simple Model: Arriving at a Solution. We found that virtually all of our runs with regression and PLS arrived at viable solutions (i.e., converged with admissible results). With LISREL, for n = 40, 11 of the 500 data sets did not. For n = 20, 164 of 500 runs did not. At n = 90 and above, these problems of LISREL disappeared in our analysis. These are not surprising results. As is well known, LISREL might not converge or might produce inadmissible values at smaller sample sizes; for the most part, regression and PLS do not share this weakness.

Simple Model: False Positives. All three techniques found false positives for the false path from Ksi4 to Eta1 roughly 5% of the time. This is exactly as it should be when we fix the statistical significance hurdle at p < .05. In all of our studies based on the model in Figure 1, we found no problems with excessive false positives (Type 1 errors) for any of the techniques.

Simple Model: Accuracy. Figures 3a (large effect size) and 3b (medium effect size) show differences in accuracy across the 500 data sets, with details in Appendix A, Table A1. The small effect size paths are hardly ever detected, at any of our sample sizes, so they are not displayed.

Accuracy is represented as the “bias” or percent departure from the true value in the Figure 1 model. Chin and Newsted (1999) observed that PLS provided estimates for path coefficients that were more accurate than regression. Our results in Figures 3a and 3b were similar. It could be argued that at all of these sample sizes, PLS is arithmetically “more accurate" than regression, since the PLS line is above the regression line. However, the differences are quite small. Discounting the small effect size path (which never achieved even a 35% statistical power), there are ten possible accuracy comparisons (large and medium effect sizes times five different sample sizes). For only one of these ten was the mean PLS path estimate statistically significant $^{16}$ and higher than the mean regression path estimate. That was at n = 90 and medium effect size.

More importantly, the LISREL path estimates were consistently more accurate than those of PLS. Again, discounting the small effect size path, for nine of the ten possible comparisons the mean LISREL path estimate was statistically significantly higher than the mean PLS path estimate. (The exception was at n = 20 and medium effect size.) We also note that at n = 40 and n = 20, the LISREL estimates should be discounted because that is far below any recommended sample size for LISREL. However, PLS and regression don't fare much better at those sample sizes!

Similar to Chin and Newsted (1999) and Cassel et al. (1999), we found that for any given sample size, by averaging across all 500 data sets, inaccuracies of the individual data sets tend to cancel each other out (some high and some low), and for all three statistical techniques, the average across 500 data sets seems to be robust to reductions in sample size, at least down to n = 40. The picture changes when we look at standard deviations of the 500 path estimates. These are shown for the Gamma1 path (large effect size) in Figure 3c and for the Gamma2 path (medium effect) in Figure 3d. These graphs give a sense of how “wild” the 500 individual path estimates can be as sample size goes down. From n = 200 to n = 20, the standard deviations for regression and PLS increase by a factor of about 3, and for LISREL by a factor of almost 5. Even though the bias when averaged across 500 data sets is robust, the findings for individual data sets are not robust with respect to sample size. Below about n = 90, the chance of having an accurate path estimate for an individual sample decreases markedly for all three techniques.

Simple Model: Detecting Paths That Do Exist. Power is the proportion (of the 500 data sets) for which the t statistic for true paths exceeds the p < .05 level. $^{17}$ We determined

![](/api/attachments/SENK7TKJ/fulltext/images/bf713c46bc93a042da7086d47089536bd8066118b94d7263f1b865ab510c5cf5.jpg)

![](/api/attachments/SENK7TKJ/fulltext/images/b3b8f6bf64bc4828e80e061cfeb0b129d42e2c0e3fa546ecb3a355a613fc7422.jpg)

![](/api/attachments/SENK7TKJ/fulltext/images/b62d89cf073f224c9df9850f5dc583775e5ee3853cb8194ba92a989e875c7167.jpg)

![](/api/attachments/SENK7TKJ/fulltext/images/15e27728868a55334154054eef86b209feb3408a8a5b51b40ce2ee28fd6dd8ce.jpg)

![](/api/attachments/SENK7TKJ/fulltext/images/1dff32d770edc8949a9913a3ae3ad38a8978c48bcc3c65d7bc77bc788e234674.jpg)

![](/api/attachments/SENK7TKJ/fulltext/images/13a2073dcf27963b8079be20625639c6e63cda92599c74664cbc85c612950f85.jpg)  
Figure 3. Simple Model, Normal Distributions (Each point on the graphs represents 500 data sets at that condition)

power for regression and LISREL by using the 500 t-statistics provided by the technique. For PLS we used the bootstrapping option with 100 resamples for each of the 500 analyses. This means that each reported statistical significance value for PLS is based on 50,000 bootstrapping resamples (500 data sets times 100 resamples). In Appendix

B we address in more depth the reasons for using 100 bootstrapping resamples instead of a larger number, and provide a sensitivity analysis to check the impact on our results.

Figures 3e (large effect size) and 3f (medium effect size) show the power results for the three techniques as the sample size decreases (right to left) from 200 to 20. Details for the power analysis are shown in Appendix A, Table A2. To give a point of comparison, given our base model (Figure 1), a medium effect size, n = 40, and looking across 500 data sets, Cohen (1988) would predict a power of about .44, with the 95% confidence interval going from about .40 to about .48. Similarly, for a large effect size and n = 40, Cohen would predict power between .78 and .84.

Three things are immediately clear from Figures 3e and 3f. First, there is almost no difference between the techniques in their ability to detect true paths for n = 40 and above—the three lines are almost on top of each other. Only at n = 20 for the medium effect size (Figure 3f) are the differences great enough to be statistically significant. At that sample size, regression's power of 22% is statistically significantly higher than PLS's power of 15%, which is statistically significantly higher that LISREL's power of 10%. Second, all of these values are abysmal—none are even close to the recommended power value of 80%. Third, Cohen's predictions of power are remarkably accurate, taking into account effect size, the overall model, and n.

From Figures 3e and 3f, it is clear that sample sizes smaller than 90 can make it difficult to detect a medium effect size, regardless of what technique is used. Following the rule of 10 here (n = 40) with a medium effect size produces a power of only about 40%. The rule of 5 produces a power of about 20%. The striking result of this analysis is that all three techniques achieve about the same power at any reasonable sample size (e.g., 90 or above), and they also achieve nearly the same level of power at lower sample sizes (e.g., 20 or 40). If any technique has a power advantage at low sample sizes it is regression, though all are unacceptable for a medium effect size at n = 40 or n = 20.

Simple Model: Summary. In our simulation with normally distributed data, we do not observe any advantage of PLS over the other two techniques at sample sizes of 90 or above, nor do we observe any advantage over regression at smaller sample sizes for either accuracy or power. Clearly, for all three techniques, individual estimates become increasingly wild as sample size decreases. In moving from n = 200 to n = 20, the standard deviations are increased by a factor of at least 2.5. Therefore, none of the techniques reached an acceptable level of power for n = 20, and only a large effect size had acceptable power for n = 40. Instead of PLS demonstrating greater efficacy, the dominant finding from Study 1 is that all three techniques seem to have remarkably similar performance, and respond in remarkably similar ways to decreasing sample size. The only difference suggested is the greater path estimate accuracy of LISREL.

## Study 2: Simple Model and Non-Normal Data

Although PLS may not have an advantage with normally distributed data, much data in behavioral research is not normally distributed (Micceri 1989). It may be that the advantage of PLS is only apparent with non-normally distributed data. In Study 2 we tested the impact of non-normal data on the efficacy of our three techniques, generating our non-normal data using Fleishman's (1978) tables and approach. Results for Study 2 are displayed in graphical form in Figure 4. Appendix C has a detailed report of our findings for the simple model and non-normal data with actual values in Appendix A, Tables A4 for path estimates and A5 for power. Below we summarize what we found.

Non-Normal Data: Summary. It appears that all three techniques are fairly robust to small to moderate skew or kurtosis (up to skew = 1.1 and kurtosis = 1.6). However, with more extremely skewed data (skew = 1.8 and kurtosis = 3.8), all three techniques suffer a substantial and statistically significant loss of power for both n = 40 and n = 90 (the two sample sizes we tested). For example with n = 90 and medium effect size, regression's power is 76% with normal data, but drops to 53% for extremely skewed data. Under the same conditions PLS's power drops from 75% to 48%, while LISREL drops from 79% to 50%. Although some have argued that new estimator options are what makes CB-SEM robust to non-normality (Gefen et al. 2011), we note that we used maximum likelihood estimate in all of our LISREL analyses. This suggests that, at least for our simple model, CB-SEM with maximum likelihood is as resistant to departures from normality as regression or PLS.

The overall results for the non-normal data do not contradict what was observed in Study 1. All three techniques seem to respond in approximately the same way to non-normality. Regardless of the distribution of the data, none of the techniques has sufficient power to detect a medium effect size at n = 40. Only at n = 90 do any of the techniques have approximately an 80% power to detect a medium effect size, and that is not changed by moderate departures from normality for any of the techniques.

## Study 3: Number of Indicators, Reliability

The data in Studies 1 and 2 utilized three indicators per construct with loadings of 0.70, 0.80, and 0.90. However, researchers doing field studies often have a greater number of indicators, and empirical work has demonstrated that the number of indicators used in the analysis can impact the path estimates of PLS (McDonald 1996). It seems important, therefore, to extend our previous study by examining the impact, if any, that changes in the number of indicators have on the results.

![](/api/attachments/SENK7TKJ/fulltext/images/b255887c5d8c6802cb6e89f09902e34ad8662f6b5b98bd519bdb27947f0def42.jpg)

![](/api/attachments/SENK7TKJ/fulltext/images/18940109ec8970111f71d56029045310e3e90419ec76fca6efb91cc690a8ef12.jpg)

![](/api/attachments/SENK7TKJ/fulltext/images/9ea179e958de24cccc56d179c94eef9cd1209537e8da775a177e233a72b088c4.jpg)

![](/api/attachments/SENK7TKJ/fulltext/images/fb769ea878e12fffae09be85f310641deb02df627cf1ba3a7c3ec4a22a96b9c7.jpg)

![](/api/attachments/SENK7TKJ/fulltext/images/5d0357791eba4a1454a8e0bab30b133c0ef1792bea09509d2a98784b1ab0d7d1.jpg)

![](/api/attachments/SENK7TKJ/fulltext/images/651eb40542a804565ae50ba9e577730425032deafcdb57512a8652f2c530c0cb.jpg)  
Figure 4. Simple Model, Non-Normal Distributions (Each point on the graphs represents 500 data sets at that condition)

In addition, the reliability of the constructs in the Study 1 model can be considered comfortably high (Cronbach's alpha = 0.84). To test the impact of less reliable and more diverse indicators, we generated two additional groups of data sets, with lower and higher reliabilities (Cronbach's alpha = .74 and .91 respectively). A write-up for all of the Study 3 findings is included in Appendix C, and is summarized below. Details are in Appendix A, Tables A6 (path estimates) and A7 (power) for the six indicator model, and A8 (path estimates) and A9 (power) for the lower loadings model.

Number of Indicators and Reliability: Summary. The doubling of the number of indicators from three to six per construct gave higher scale reliability (from .84 to .91) and therefore each technique had slightly higher power. However, it had no effect on the relative performance of the three techniques for accuracy or power and none achieved 80% power at n = 40. Similarly, changing the indicator loadings from (.7, .8, .9) to (.6, .7, .8) reduced the reliabilities from .84 to .74, and caused all three techniques to lose power. However (as with the earlier studies) this also did not change the relative performance. Our results suggest that changing by moderate amounts the number of indicators or indicator loadings (both of which affect reliability) does not produce any evidence of a PLS advantage over regression or LISREL.

## Study 4: A More Complex Model

The models that we used in Studies 1, 2, and 3 are quite simple, with four independent variables and one dependent variable. PLS may have more relative advantage when employed with more complicated models. For example, Chin and Newsted (1999) used a model comprised of multiple constructs predicting a focal construct which then predicted multiple dependent constructs. $^{18}$

To investigate model complexity, we created a more complex model as shown in Figure 5. It contains seven constructs that can be partitioned into three interconnected submodels. Starting from the bottom and working up, we see that Ksi3 and Eta3 together cause variation in Eta4, but in this case there is no direct link between Ksi3 and Eta4. Therefore Eta3 fully mediates the relationship between Ksi3 and Eta4. Moving to the middle of the diagram and looking at Ksi2, Eta2, and Eta4, we see that Eta2 only partially mediates the relationship between Ksi2 and Eta4, as there is also a direct relationship between Ksi2 and Eta4. Finally, at the top of the diagram looking at Ksi1, Eta1 and Eta4, we see that Eta1 does not mediate the relationship between Ksi1 and Eta4, as there is no direct relationship between Eta1 and Eta4. All paths have approximately a medium effect size. See the note in Figure 5 for more detail.

As before, we generated 500 data sets from the model for each sample size condition (n = 20, 40, 90, and 150), and analyzed each sample using all three techniques. Note that we decided not to test the results at n = 200, since all of our earlier tests had high power at n = 150 and there was not much difference in moving from n = 150 to n = 200. Also note that applying the rule of 10 would give a minimum sample size of 60 for PLS for this model.

We should note that Reinartz et al, (2009) used a fairly complex model and compared the accuracy and statistical power of PLS and CB-SEM at sample sizes of 100 and greater. They concluded that CB-SEM was more accurate, but that PLS had more statistical power. Since these statistical power results are quite different from our own results in this paper, it raises the question of whether the statistical power of either or both PLS and CB-SEM are highly variable depending upon the particular model being analyzed. We also note that Reinartz et al. did not test for false positives.

Arriving at a solution. The findings for the complex model are quite similar to those for the simpler model. For n = 90 and 150, all techniques arrived at a solution. For n = 20 and 40, LISREL had the expected difficulties; 99 of the n = 20 and two of the n = 40 LISREL runs did not produce a solution.

Accuracy. There are seven true paths in Figure 5 and two zero (non-existent) paths. The full results for the individual paths in the complex model are shown in Appendix A, Tables A10 (accuracy) and A11 (power). To conserve space (and be respectful of the readers' stamina), for accuracy and statistical power we will look only at two of the seven paths (Ksi3 → Eta3 and Eta3 → Eta4), with these results shown in Figure 6. These two paths are quite representative of all seven true paths. In Figure 7 we move the level of abstraction up and look at statistical power as averages across all seven true paths and both false paths.

As shown in Figures 6a and 6b, for both the Ksi3 → Eta3 and Eta3 → Eta4 paths, PLS had a slight advantage over regression in terms of bias (path accuracy), but as before LISREL had the least bias. We note that at n = 20, LISREL's bias advantage largely disappeared.

Although the average bias across 500 data sets was reasonably robust to decreases in sample size, the standard deviation across the 500 path estimates was not, repeating what was found in the simpler model. For all techniques, as the sample size goes down, the average path estimate standard deviations go up, as can be seen in Figure 6c and 6d. For all three techniques and for both the paths displayed, the standard deviation increased by a factor of about 2.5 as sample size dropped from 150 to 20.

Statistical Power. In terms of statistical power, for n = 90 and above, the three techniques were remarkably similar for both the Ksi3 → Eta3 and Eta3 → Eta4 paths—the three lines essentially blur together, as can be seen in Figures 6e and 6f. At n = 40 and below, none of the techniques has acceptable power, but statistically significant differences do begin to appear. However, they are inconsistent. At n = 40, for the Ksi3 → Eta3 path, PLS's power (59%) is significantly larger than LISREL's (53%). But for the Eta3 → Eta4 path, LISREL's power (43%) is significantly larger than PLS's (35%). At n = 20, again there are inconsistent significant differences in the power. For the Ksi3 → Eta3 path, PLS's power (37%) is significantly larger than both LISREL's and regression's, but for the Eta3 → Eta4 path, regression's power (22%) is significantly larger than PLS's (19%) or LISREL's (15%). We note that at n = 40 and below, none of the techniques has even close to acceptable power.

![](/api/attachments/SENK7TKJ/fulltext/images/f7ca3fa744b9c6cdb54a137e191bc4233b758a1bc0c4c8269af415f823ffb7d1.jpg)  
Note: Starting from the bottom of the figure and working up, we see that Ksi3 and Eta3 together can cause variation in Eta 4, but in this case there is no direct link between Ksi3 and Eta4. Therefore, Eta 3 fully moderates the relationship between Ksi3 and Eta4. Looking at Ksi2, Eta2, and Eta4, we see that Eta2 only partially moderates the relationship between Ksi2 and Eta4, since there is also a direct relationship between Ksi2 and Eta4. Finally, looking at Ksi1, Eta1 and Eta4, we see that Eta1 does not moderate the relationship between Ksi1 and Eta4, as there is no relationship between Eta1 and Eta4.

The actual relationships between the Ksi2, Eta2, and Eta4 constructs are all created to have a medium effect size of .15 (ala Cohen 1988). The actual relationships between Ksi1, Eta1, and Eta4 are all slightly less than a medium effect size at .12; while the relationships between Ksi3, Eta3, and Eta4 are all slightly more than a medium effect size at .18. Although not shown, all constructs are measured with three indicators having .7, .8, and .9 loadings, respectively.

Figure 5. A More Complex Model, the Basis for Study 4 (With three types of mediation)

False Positives. The paths from Eta1 to Eta4 and from Ksi3 to Eta4 are non-existent, allowing us to test for false positives. The proportion of false positives for these two paths is shown in Figures 6g and 6h. Here we see something unexpected. Although no technique consistently shows up as better or worse than the others, the 95% confidence interval around 5% was exceeded (i.e., higher than 6.9% false positives) at least once for each technique. This suggests that in more complex models, false positives may become a concern.

Average Power Across All Seven True Paths. Given the inconsistencies in the dominant technique for the power of individual paths at sample sizes of less than n = 90, a look at the behavior averaged across all seven true paths in the complex model becomes of interest. These averaged power values $^{19}$ are shown in Figure 7a, and at the bottom of Appendix A Table A11. As expected, for sample sizes n = 90 and above, the values for the average of the seven true paths are almost on top of one another, with no statistically significant

![](/api/attachments/SENK7TKJ/fulltext/images/2803166ea60513ca9006cba9c12c8573029236d38c22dd0ce0f9fb9045b9921b.jpg)

![](/api/attachments/SENK7TKJ/fulltext/images/e6d79b378eb467e6f4a0905b0b00fddbcac1ca33036b2d10d94f154d54040994.jpg)

![](/api/attachments/SENK7TKJ/fulltext/images/c03a77c0c6874ad34a84b93d7db59973d3da4eca908b5f3e82c5ed78bb9d13f4.jpg)

![](/api/attachments/SENK7TKJ/fulltext/images/25f5dd1b22c5105063937c96cd8d0722c41674d0a391de507b1f9b2b05ac4927.jpg)

![](/api/attachments/SENK7TKJ/fulltext/images/72df3915de3429f2b8ac2631f6b7eb66fa64e69004d703cf78e9656397fe9eea.jpg)

![](/api/attachments/SENK7TKJ/fulltext/images/0c6fa35848ce7e25b5559b457c3239ee2be465eb331e2e9c87974441b6af62c1.jpg)

![](/api/attachments/SENK7TKJ/fulltext/images/0685458715766eeb59dee8367a833c4ca48c40911184ecd406a4fbfe451f9c89.jpg)

![](/api/attachments/SENK7TKJ/fulltext/images/5b95e0b7a1c2937be2b82d3f41fc56d8800a4aac6fd13532669c8ee44564c640.jpg)

Figure 6. Complex Model: Selected Paths (Each point on the graphs represents 500 data sets at that condition)

![](/api/attachments/SENK7TKJ/fulltext/images/0ea36b11f7bf5f7271968981fb3cba1aa95f3c6d1604b4526c58d5101a87a945.jpg)

![](/api/attachments/SENK7TKJ/fulltext/images/969910291c2d5ce6641fd341b1676eb6d296784fdd65789d0779de6f36e19245.jpg)  
Figure 7. Complex Model: Averages Across Seven True and Two False Paths (Each point on the graph represents 3,500 (7a) or 1,000 (7b) data sets)

differences. However, at n = 40, regression is significantly lower than the other techniques (41.2% versus 43.0%), while at n = 20, regression is significantly higher than the other techniques (23.2% versus 19% and 15%). Given that below n = 90 none of these power values are even close to the target of 80%, these inconsistent differences may not be very important.

Average False Positives. Similarly, to increase the level of abstraction on the erratic picture of false positives, we averaged across both false paths as shown in Figure 7b and Table A11 of Appendix A. Each combined power score represents a proportion of false positives (out of 1,000). With 1,000 trials, $^{20}$ the 95% confidence interval around .05 goes from 3.6 to 6.4. From Figure 6b, it can be seen that across all sample sizes regression just barely stays within the “safe” range of false positives. For sample sizes of 90 and above, both LISREL and PLS have too many false positives, especially at n = 90 where PLS has 7.5% and LISREL 7.1% false positives (see Table A11). These values are worthy of concern, since false positives threaten our ability to draw correct conclusions from our statistical methods.

For n = 20 and n = 40, LISREL's proportion of false positives increases to about 10%; regression jumps up but then drops for n = 20; and PLS's drops to an average of 4%. Thus both LISREL and regression have excessive false positives at n = 40 and below, while PLS has an acceptable number. We do note that PLS's average power at these sample sizes is quite low (43% at n = 40 and 26% at n = 20).

Complex Model with Non-Normal Data. There is also the possibility that a different picture might emerge if the complex model were analyzed with non-normal data, so we tested this as well. See Table A12 in Appendix A for the specific results. In fact, all three techniques have about the same percentage drop in power with extremely non-normal data, regardless of whether the simple or the complex model is used. If any technique has the advantage, it is regression, for both the simple or complex model. PLS has no apparent advantage when using more complex models and non-normal data.

Complex Model Summary. The most prominent finding for the complex model is that, for the most part, the results closely mirror what we found with the simpler model. LISREL has a slight advantage in accuracy across the board. For power, there are differences between PLS versus regression or LISREL on particular paths of the model—some paths consistently seem to favor PLS, others LISREL. However, an average across all seven true paths gives statistically indistinguishable power for all three techniques for both n = 90 and n = 150.

For n = 40, PLS and LISREL power values are identical, and statistically larger than regression's, although all values are below 43%. For n = 20, regression's power is significantly higher than PLS and LISREL, but all values are below 25%. Interestingly, at each sample size except n = 20, the average power for the complex model (with its seven approximately medium effect sized paths) is within a percent or two of the medium effective size power for the simpler model.

However, there is one striking difference from the simpler model. With the complex model both PLS and LISREL have an unsettling number of false positives, especially at sample sizes of 90 where PLS has 7.5% and LISREL 7.1%. The difference between these values and the allowable 5% is statistically significant. We attribute the somewhat higher number of false positives to the fact that in each case, the false predictor constructs were correlated with the true predictor constructs. This creates some amount of multicollinearity and may make the results less stable (see Goodhue et al. 2011a). This condition may often be present in more complex models and is a potential concern.

Overall, the results suggest that small sample size and non-normality have the same effect in the complex model that they do in the simple model. We again see no advantage for PLS, except fewer false positives at sample sizes of 40 or less, where power is below 50% for all techniques.

## Post Hoc Analysis: Accuracy Differences $^{21}$

Across all of our studies, LISREL seemed to have the advantage in terms of path estimate accuracy. For the simple model, Figure 8a shows the average bias at different values of effect size and reliability. LISREL was closer to the true value (bias closer to zero) than PLS in 24 of 27 comparisons. $^{22}$ Looking just at LISREL and PLS (the two leading contenders), and taking as the null hypothesis that either technique had a 50% chance of being the most accurate in every comparison, we can use the binomial distribution to ask, what is the likelihood of having only zero, 1, 2, or 3 comparisons favoring PLS out of 27 trials under those assumptions? With this nonparametric test, we reject the hypothesis that LISREL is no more accurate than PLS, with a p value of .00002. The picture is similar if we look at results from the non-normal data, or the more complex model.

In fact, Figure 8a shows PLS to be quite a bit more similar to regression than it is to LISREL in terms of accuracy. Given the apparent fact of LISREL's accuracy advantage over PLS (and regression), a reasonable question is to ask is, why? A possible answer comes from other work we have been conducting that suggests that the level of measurement reliability could hold the answer. It is generally accepted that regression does not account for measurement reliability in its path estimates, but that LISREL does. Regression path estimates are “attenuated” by measurement error, according to the following equation from Nunnally and Bernstein (1994, pp. 241, 257):

$$
\begin{array}{l} \text { Apparent   Correlation } _ {\mathrm{XY}} = \text { Actual   Correlation } _ {\mathrm{XY}} \times \\ \text { Square   Root(Reliability } _ {\mathrm{X}} \times \text { Reliability } _ {\mathrm{Y}}) \end{array}
$$

Given this equation, and knowing the reliabilities of all of the constructs in our various studies, we should be able to "adjust" the attenuated regression path estimates to the correct value using the reliability of the constructs in our model. Figure 8b shows both PLS and regression path estimates corrected for measurement error and LISREL estimates unchanged. Looking at Figures 8a and 8b suggests the following: The negative bias of PLS and regression is proportional to the reliability of the constructs, and is essentially corrected when Nunnally and Bernstein's equation is used. The only time this is not true is when a small effect size is involved, in which case the reliability correction sometimes seems to over correct for PLS. Figures 8a and 8b suggest that PLS is more similar to regression than it is to LISREL in the way in which it compensates for measurement error. In retrospect, this is not so surprising. It is consistent with both McDonald (1996, pp. 266-267) and Dijkstra (1983, p. 81) who suggest that when dealing with multiple indicators for each construct, as measurement error goes up, both PLS and regression will suffer increasingly in terms of accuracy in comparison with LISREL.

Consider the PLS process in “mode A” (when all constructs have reflective indicators, which is what our study involves). As we said earlier in this note, we can think of the PLS process as having three major steps. The first step is to iterate through a process to determine the optimal indicator weights for each construct. The second step uses those weights to calculate construct scores which are then used in ordinary least squares regression to determine path estimates. The third step is to determine the standard deviations of those path estimates with bootstrapping.

We would submit that if PLS has somehow taken into account measurement error in determining its path estimates, then it must have done so in step 1. This has to be the case, since beyond this point (in step 2) all path estimates are determined by ordinary least squares regression, which is known to not compensate for measurement error. But all that comes out of step 1 is the appropriate weights for the indicators. If PLS compensates for measurement error, it must do so by assigning just the right combination of weights. We would

![](/api/attachments/SENK7TKJ/fulltext/images/9c6a138163bf94c528e050cb46714ca62b34f6eb22874c9c78f70cec80fc9f21.jpg)

![](/api/attachments/SENK7TKJ/fulltext/images/34ba2e15e782e52e0374f4341b4b3dea3dafafde91bfb57204a132e820acfe30.jpg)

Figure 8. Bias for Effect Size and Alpha, Uncorrected and Corrected (Each point on the graphs represents 1,500 data sets at that condition)

submit that unless at least one indicator measures the construct without error, there is no conceivable weighting scheme that will overcome measurement error. In fact, our empirical evidence seems to suggest that PLS path estimates (like regression path estimates) do not compensate for measurement error at all, while LISREL path estimates do.

We recognize this may be a controversial statement, since it is counter to the widespread belief among MIS researchers. However we are not the first to suggest it. Marcoulides et al. (2009, p. 172) commented:

We note that in cases where the model errors are not explicitly taken into account for the estimation of endogenous latent variables, a new approach proposed by Vittadini et al. (2007) would need to be used to appropriately determine the PLS model estimates. This is because in PLS...[for reflective constructs] the model errors are not taken into account.

Our work is a bit more explicit than the Marcoulides et al. comment—we show that PLS is like regression in ignoring measurement error in determining its path estimates, and that the same correction (Nunnally and Bernstein 1994) can be used in either PLS or regression to address this weakness.

Our findings on measurement error also suggest a different perspective on Wold's (1982) assertion that PLS has “consistency at large.” He suggests that given an infinite number of indicators and an infinite sample size, PLS path estimates will have no bias. We would point out that if there were an infinite number of indicators, then Cronbach's alpha would be 1, there would be no measurement error, and Wold's claim and ours would be the same: no measurement bias in the PLS path estimates, nor in the regression estimates, nor in the LISREL estimates. This suggests that saying that PLS has "consistency at large" is not actually a unique or useful selling point.

## Limitations and Opportunities for Future Research

As with any study, there are a number of limitations that may lead to opportunities for future research. For example, most of the data generated for use in this study were designed to have relatively high indicator loadings with few cross-loadings. While such well-behaved data created a level playing field, actual field data often exhibits more challenging characteristics. Future studies could be designed to test the three techniques across a variety of other data conditions, including indicators that cross-load (i.e., load on constructs other than the one they are intended to measure), or constructs exhibiting multicollinearity. Furthermore, future studies could examine the testing of more complex models involving formative measurement (Barclay et al. 1995; Chin 1998; Petter et al. 2007).

In addition, it is important to recognize that all of our analyses with the more complex model involved approximately medium effect sizes. We do not expect that the relative performance between the three techniques would change much with different effect sizes, however.

## Conclusion

The belief among MIS researchers that PLS has special powers at small sample size or with non-normal distributions is strongly and widely held in the MIS research community. Our study, however, found no advantage of PLS over the other techniques for non-normal data or for small sample size (other than the universally stated concern that with smaller samples, LISREL may not converge). This should not be surprising; all of these techniques can be thought of as attempts to make meaningful statements about latent variables in a population on the basis of a small sample. Even if a true random sample is drawn (which already suggests problems), basic statistics tells us that the smaller the N, the less sure we can be about our estimates.

Earlier in this paper, we indicated that one of our primary goals was to provide guidance to researchers in terms of designing studies, selecting statistical analysis techniques, and interpreting results. We do so here.

## Study Design

Although many have argued that there are important differences between the efficacies of the three techniques under certain conditions, in our studies what is much more prominent than the differences is the surprising similarity of the results. In our studies, all suffered from increasingly large standard deviations for their path estimates as sample sizes decreased, and from the resulting drop in statistical power. None could successfully detect medium effect sizes on a consistent basis using sample sizes recommended by the rule of 10 or the rule of 5. All techniques showed substantial (and about equal) robustness in response to small or moderate departures from normality; all showed significant losses in response to extreme non-normality.

Recommendation: When determining the minimum sample size to obtain adequate power, use Cohen's approach (regardless of the technique to be used). Do not rely on the rule of 10 (or the rule of 5) for PLS. It also might be fruitful for social science researchers to more precisely identify the amounts and types of non-normality, so we know better at what point such problems become threatening.

## Interpretation of Results

We do need to consider what our findings for PLS and small sample size might mean in terms of existing published research that found statistically significant results using PLS with small sample size. First, with the simple model, none of the techniques showed excessive false positives. Even though with the more complex model we did find evidence of greater than a 5% occurrence of false positives with all three techniques, with that model and smaller sample size PLS had the smallest occurrence of false positives. Therefore, overall there is nothing in our findings to suggest that any previously reported statistically significant results found with PLS and small sample sizes are suspect. $^{23}$ We note that our findings suggest that regression would be equally likely to find such statistically significant relationships at those small sample sizes. On the other hand, studies using PLS and small sample sizes that failed to detect a hypothesized path (e.g., Malhotra et al. 2007), may well have a false negative.

Recommendation: In studies where small sample sizes were used (with any of the techniques, including PLS) and a hypothesized path was not observed to be statistically significant, this should not be interpreted as a lack of support for the hypothesis. In these cases, further testing with larger sample sizes is probably warranted.

## Selecting a Technique

One important difference between the techniques did stand out. This is the suggestion that PLS, unlike LISREL, seems not to compensate for measurement error in its path estimates. In fact, PLS seems to be quite comparable to regression in all its performance measures, including accuracy of path estimates. If accuracy is a major concern, both PLS and regression have poorer performance than LISREL. The magnitude of the difference in path estimates, however, was not great.

Recommendation: Here, interestingly, the three authors of this note are not in complete agreement. One point of view suggests that if one is in the early stages of a research investigation and is concerned more with identifying potential relationships than the magnitude of those relationships, then regression or PLS would be appropriate. As the research stream progresses and accuracy of the estimates becomes more important, LISREL (or other CB-SEM techniques) would likely be preferable.

The second point of view suggests the following: Both regression and CB-SEM techniques have received a great deal of attention from statisticians over the years, and their advantages and limitations are generally well established. PLS has received much less attention (at least until more recently), and hence we are still learning about its properties and how it behaves under various conditions. In addition to the evidence presented here (with respect to a loss of power at small sample sizes, etc.) some recent studies have provided preliminary evidence of other potential short-comings, such as greater susceptibility to multicollinearity problems than CB-SEM and regression (Goodhue et al. 2011b), lower construct validity when measurement errors are correlated across constructs (Rönkkö and Ylitalo 2010), and an inability to detect mis-specified models (Evermann and Tate 2010). As a result, one could argue that researchers would be well advised to use PLS with caution (until more is known about its properties), and to rely on more well-established techniques under most circumstances.

In conclusion, we want to stress that in our empirical work, even though it seems to have no special abilities with respect to sample size or non-normality, PLS did not perform worse than the other techniques in terms of statistical power and avoidance of false positives. These are perhaps the most important performance attributes of hypothesis testing. PLS is still a convenient and powerful technique that is appropriate for many research situations. For example, with complex research models, PLS may have an advantage over regression in that it can analyze the whole model as a unit, rather than dividing it into pieces. However, we found that PLS certainly is not a silver bullet for overcoming the challenges of small sample size or non-normality. At reasonable sample sizes, LISREL has equal power and greater accuracy.

## Acknowledgments

Professor Thompson would like to acknowledge the generous financial support of the Wake Forest Schools of Business in helping to complete this research project.

## References

Barclay, D., Higgins, C., and Thompson, R. 1995. “The Partial Least Squares (PLS) Approach to Causal Modeling: Personal Computer Adoption and Use as an Illustration,” Technology Studies (2:2), pp. 285-309.

Bagozzi, R. P., and Edwards, J. R. 1998. “A General Approach for Representing Constructs in Organizational Research,” Organizational Research Methods (1:1), pp. 45-87.

Bollen, K. A. 1989. Structural Equations with Latent Variables, New York: Wiley.

Cassel, C., Hackl, P., and Westlund, A. 1999. “Robustness of Partial Least-Squares Method for Estimating Latent Variable Quality Structures,” Journal of Applied Statistics (26:4), pp. 435-446.

Chin, W. W. 1998. “The Partial Least Squares Approach to Structural Equation Modeling,” in Modern Methods for Business Research, G. A. Marcoulides (ed.), London: Psychology Press, pp. 295-336.

Chin, W. W. 2001. PLS Graph User's Guide, Version 3.0, Houston, TX: Soft Modeling, Inc.

Chin, W. W., Marcolin, B., and Newsted, P. 2003. “A Partial Least Squares Latent Variable Modeling Approach for Measuring Interaction Effects: Results from a Monte Carlo Simulation Study and an Electronic-Mail Emotion/Adoption Study,” Information Systems Research (14:2), pp. 189-217.

Chin, W. W., and Newsted, P. R. 1999. “Structural Equation Modeling Analysis with Small Samples Using Partial Least Squares,” in Statistical Strategies for Small Sample Research, R. Hoyle (ed.), Newbury Park, CA: Sage Publications, pp. 307-341.

Cohen, J. 1988. Statistical Power Analysis for the Behavioral Sciences, Hillsdale, N: Lawrence Erlbaum Associates.

Dijkstra, T. 1983. “Some Comments on maximum Likelihood and Partial Least Squares Methods,” Journal of Econometrics (22), pp. 67-90.

Evermann, J., and Tate, M. 2010. “Testing Models or Fitting Models? Identifying Model Misspecification in PLS,” in Proceedings of the 31 $^{st}$ International Conference on Information Systems, St. Louis, MO, December 12-15.

Falk, R. F., and Miller, N. B. 1992. A Primer for Soft Modeling, Akron, OH: University of Akron Press.

Fleishman, A. I. 1978. “A Method for Simulating Non-Normal Distributions,” Psychometrika (43:4), pp. 521-532.

Fornell, C. 1984. “A Second Generation of Multivariate Analysis: Classification of Methods and Implications for Marketing Research,” Working Paper, University of Michigan.

Fornell, C., and Bookstein, F. 1982. “Two Structural Equation Models: LISREL and PLS Applied to Consumer Exit-Voice Theory,” Journal of Marketing Research (19), pp. 440-452.

Fornell, C., and Larcker, D. 1981. “Evaluating Structural Equation Models with Unobservable Variables and Measurement Error,” Journal of Marketing Research (18), pp. 39-50.

Gefen, D., Rigdon, E., and Straub, D. 2011. “Editor’s Comments: An Update and Extension to SEM Guidelines for Administrative and Social Science Research,” MIS Quarterly (35:2), pp. iii-xiv.

Gefen, D., Straub, D., and Boudreau, M. C. 2000. “Structural Equation Modeling and Regression: Guidelines for Research Practice,” Communications of the Association for Information Systems (4:Article 7).

Goodhue, D., Lewis, W., and Thompson, R. 2006. “Small Sample Size and Statistical Power in MIS Research,” in Proceedings of the 39 $^{th}$ Hawaii International Conference on Systems Sciences, R. Sprague (ed.), Los Alamitos, CA: IEEE Computer Society Press, January 4-7.

Goodhue, D., Lewis, W., and Thompson, R. 2007. “Research Note – Statistical Power in Analyzing Interaction Effects: Questioning the Advantage of PLS With Product Indicators,” Information Systems Research (18:2), pp. 211-227.

Goodhue, D., Lewis, W., and Thompson, R. 2011a. “A Dangerous Blind Spot in IS Research: False Positives Due to Multicollinearity Combined with Measurement Error,” in Proceedings of the 17 $^{th}$ Americas Conference on Information Systems, Detroit, MI, August 4-7.

Goodhue, D., Lewis, W., and Thompson, R. 2011b. “Measurement Error in PLS, Regression and CB-SEM,” in Proceedings of the 6 $^{th}$ Mediterranean Conference on Information Systems Sciences, Limassol, Cyprus, September 3-5.

Goodhue, D., Lewis., W., and Thompson, R. 2012. “Comparing PLS to Regression and LISREL: A Response to Marcoulides, Chin, and Saunders,” MIS Quarterly (36:3), pp. 703-716.

Green, S. B. 199. “How Many Subjects Does it Take to Do A Regression Analysis,” Multivariate Behavioral Research (26), pp. 499-510.

Hayduk, L. A. 1987. Structural Equation Modeling with LISREL, Baltimore, MD: Johns Hopkins University Press.

Hair, J. F., Jr., Anderson, R. E., Tatham, R. L., and Black, W. C. 1998. Multivariate Data Analysis with Readings ( $5^{th}$ ed.), Englewood Cliffs, NJ: Prentice Hall.

Hair, J. F., Ringle, C. M., and Sarstedt, M. 2011. “PLS-SEM: Indeed a Silver Bullet,” Journal of Marketing Theory and Practice (19:2), pp. 139-151.

Hair, J. F., Sarstedt, M., Ringle, C. M., and Mena, J. A. 2011. “An Assessment of the Use of Partial Least Squares Structural Equation Modeling in Marketing Research,” Journal of the Academy of Marketing Science, Online Publication (DOI 10.1007/s11747-011-0261-6).

Kahai, S. S., and Cooper, R. B. 2003. “Exploring the Core Concepts of Media Richness Theory: The Impact of Cue Multiplicity and Feedback Immediacy on Decision Quality,” Journal of Management Information Systems (20:1), pp. 263-299.

Kline, R. B. 1998. Principles and Practice of Structural Equation Modeling, New York: Guilford Press.

Lohmöller, J. B. 1988. “The PLS Program System: Latent Variables Path Analysis with Partial Least Squares Estimation,” Multivariate Behavioral Research (23), pp. 125-127.

MacCallum, R., Browne, M., and Sugawara, H. 1996. “Power Analysis and Determination of Sample Size for Covariance Structure Modeling,” Psychological Methods (1:2), pp. 130-149.

Majchrzak, A., Beath, C. M., Lim, R. A., and Chin, W. W. 2005. "Managing Client Dialogues During Information Systems Design to Facilitate Client Learning," MIS Quarterly (29:4), pp. 653-672.

Malhotra, A., Gosain, S., and El Sawy, O. 2007. “Leveraging Standard Electronic Business Interfaces to Enable Adaptive Supply Chain Partnerships,” Information Systems Research (18:3), pp. 260-279.

Marcoulides, G. A., Chin, W. W., and Saunders, C. 2009. “Foreword: A Critical Look at Partial Least Squares Modeling,” MIS Quarterly (33:1), pp. 171-175.

Marcoulides, G. A., and Saunders, C. 2006. “Editor’s Comments: PLS: A Silver Bullet?,” MIS Quarterly (30:2), pp. iii-ix.

McDonald, R. P. 1996. "Path Analysis with Composite Variables," Multivariate Behavioral Research (31:2), pp. 239-270.

Micceri, T. 1989. “The Unicorn, the Normal Curve, and Other Improbable Creatures,” Psychological Bulletin (105:1), pp. 156-166.

Nunnally, J. C., and Bernstein, I. H. 1994. Psychometric Theory ( $3^{rd}$ ed.), New York: McGraw-Hill.

Petter, S., Straub, D., and Rai, A. 2007. “Specifying Formative Constructs in Information Systems Research,” MIS Quarterly (31:4), pp. 623-656.

Reinartz, W., Haenlein, M., and Henseler, J. 2009. “An Empirical Comparison of the Efficacy of Covariance-Based and Variance-Based SEM, 2009,” International Journal of Research in Marketing (26), pp. 332-344.

Ringle, C., Sarstedt, M., and Straub, D. 2012. “Editor’s Comments: A Critical Look at the Use of PLS-SEM in MIS Quarterly,” MIS Quarterly (36:1), pp. iii-xiv.

Rivard, S., and Huff, S. 1988. “Factors of Success for End-User Computing,” Communications of the ACM (31:5), pp. 552-561.

Rönkkö, M, and Ylitalo, J. 2010. “Construct Validity in Partial Least Squares Path Modeling,” in Proceedings of the 31 $^{st}$ International Conference on Information Systems, St. Louis, MO, December 12-15.

Wold, H. O. 1982. “Soft Modeling: The Basic Design and Some Extensions,” in Systems Under Indirect Observation: Causality, Structure, Prediction, Part II, K. G. Jöreskog and H. Wold (eds.), Amsterdam: North-Holland.

Wood, R. E., Goodman, F. S., Beckmann, N., and Cook, A. 2008. "Mediation Testing in Management Research: A Review and Proposals," Organizational Research Methods (11:2), pp 270-295.

Vittadimi, G., Minotti, S. I., Fattore, M., and Lovaglio, P. G. 2007. "On the Relationship Among Latent Variables and Residuals in PLS Path Modeling: The Formative-Reflective Scheme," Computational Statistics and Data Analysis (51:12), pp. 5828-5846.

Zhang, T., Agarwal, R., and Lucas, H., Jr. 2011. “The Value of IT-Enabled Retailer Learning: Personalized Product Recommendations and Customer Store Loyalty in Electronic Markets,” MIS Quarterly (35:4), pp. 859-882.

## About the Authors

Dale Goodhue is the MIS Department head, and the C. Herman and Mary Virginia Terry Chair of Business Administration at the University of Georgia's Terry College of Business. He has published in journals including Management Science, MIS Quarterly, Information Systems Research, Decision Sciences, and Sloan Management Review. Dale's research interests include measuring impacts of information systems, the impact of task–technology fit on individual performance, the management of data and other IS infrastructures/resources, the impacts of enterprise systems on organizations, and the strengths and weaknesses of various statistical techniques.

William Lewis is an independent consultant and a former assistant professor of MIS in the Department of Management and Information Systems at Louisiana Tech University. His research has appeared in several journals including MIS Quarterly and Communications of the ACM. William's research interests include business continuity planning, individual technology adoption in organizations, IS leadership, and research methodology.

Ronald L. Thompson is a professor in the Schools of Business at Wake Forest University. His research has been published in a variety of journals, including MIS Quarterly, Information Systems Research, Journal of Management Information Systems, and Information & Management. Ron is currently a senior editor for MIS Quarterly, and formerly served on the editorial board for the Journal of the Association for Information Systems. He holds a Ph.D. from the Ivey School at the University of Western Ontario. His current research interests include managing information systems projects and the use of advanced data analysis techniques in Information Systems research.
