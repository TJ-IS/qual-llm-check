---
otero_id: 26504
otero_key: "PJNPTKAY"
title: "A Partial Least Squares Latent Variable Modeling Approach for Measuring Interaction Effects: Results from a Monte Carlo Simulation Study and an Electronic-Mail Emotion/Adoption Study"
authors: "Wynne W. Chin; Barbara L. Marcolin; Peter R. Newsted"
year: "2003"
journal: "Information Systems Research"
doi: "10.1287/isre.14.2.189.16018"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HR

![](/api/attachments/PJNPTKAY/fulltext/images/e318b61707eb076d6c8142e6d4fd7df4b92f4a3be8b706ad481a9b0d3ff4f9a6.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# A Partial Least Squares Latent Variable Modeling Approach for Measuring Interaction Effects: Results from a Monte Carlo Simulation Study and an Electronic-Mail Emotion/Adoption Study

Wynne W. Chin, Barbara L. Marcolin, Peter R. Newsted,

To cite this article:

Wynne W. Chin, Barbara L. Marcolin, Peter R. Newsted, (2003) A Partial Least Squares Latent Variable Modeling Approach for Measuring Interaction Effects: Results from a Monte Carlo Simulation Study and an Electronic-Mail Emotion/Adoption Study. Information Systems Research 14(2):189-217. http://dx.doi.org/10.1287/isre.14.2.189.16018

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 2003 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/PJNPTKAY/fulltext/images/8503aaf377dc93980f58c0e546bf14733c49c49b895d27ddaf2eb5b543ca5631.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# A Partial Least Squares Latent Variable Modeling Approach for Measuring Interaction Effects: Results from a Monte Carlo Simulation Study and an Electronic-Mail Emotion/Adoption Study

Wynne W. Chin • Barbara L. Marcolin • Peter R. Newsted

C. T. Bauer College of Business, University of Houston, Houston, Texas 77204

Haskayne School of Business, University of Calgary, 2500 University Drive NW,

Calgary, Alberta, Canada, T2N 1N4

Centre for Innovative Management, Athabasca University, 22 Sir Winston Churchill Avenue, St. Alberta, Alberta, Canada, T8N 1B4

wchin@uh.edu • marcolin@ucalgary.ca • pnewsted@mba.athabascau.ca

he ability to detect and accurately estimate the strength of interaction effects are criti-1 cal issues that are fundamental to social science research in general and IS research in particular. Within the IS discipline, a significant percentage of research has been devoted to examining the conditions and contexts under which relationships may vary, often under the general umbrella of contingency theory (cf. McKeen et al. 1994, Weill and Olson 1989). In our survey of such studies, the majority failed to either detect or provide an estimate of the effect size. In cases where effect sizes are estimated, the numbers are generally small. These results have led some researchers to question both the usefulness of contingency theory and the need to detect interaction effects (e.g., Weill and Olson 1989). This paper addresses this issue by providing a new latent variable modeling approach that can give more accurate estimates of interaction effects by accounting for the measurement error that attenuates the estimated relationships. The capacity of this approach at recovering true effects in comparison to summated regression is demonstrated in a Monte Carlo study that creates a simulated data set in which the underlying true effects are known. Analysis of a second, empirical data set is included to demonstrate the technique's use within IS theory. In this second analysis, substantial direct and interaction effects of enjoyment on electronic-mail adoption are shown to exist.

<sub>(</sub>PLS; Moderators; Interaction Effects; Structural Equation Modeling; Measurement Error <sub>)</sub>

## Introduction

The ability to detect and accurately estimate interaction effects1 between quantitative variables can be difficult. Within the IS discipline, both empirical and theoretical models presenting such relationships can easily be found going back several decades (e.g., Powers and Dickson 1973, Ginzberg 1979, Franz 1979). In fact, it can be argued that a significant percentage of IS research has been devoted to examining those moderating variables that create interaction effects (i.e., the conditions and contexts under which theoretical relationships may vary) often under the general umbrella of contingency theory (McKeen et al. 1994, Weill and Olson 1989), and within emerging theories (Goodhue and Thompson 1995, Chan et al. 1997, Taylor and Todd 1995, Davis et al. 1992).

Yet, as to be presented in this paper, a majority of past IS studies have either failed to detect a moderating influence or have failed to provide an estimate of the size of the interaction effect. If presented, the effect size values are generally small. Collectively these results suggest that moderators have a small influence on our developing theories, which in turn has led some researchers to question the usefulness of contingency theory and the need to detect interaction effects (e.g., Weill and Olson 1989). Essentially, the argument is: “Why develop contingency theories or attempt to measure such interaction effects if the extant research indicates either no or minimal effects?”

The position of this paper is that our current lack of understanding and development of contingent effects may be a byproduct of the analytic method as opposed to a failing of theoretical development. Problems in measuring interaction effects are especially pronounced in field research and observational studies (e.g., McClelland and Judd 1993), where much of the difficulties can be attributed to measurement error. Measurement error has been cited as the cause of both lowering the ability to detect as well as underestimating the true effects (Busemeyer and Jones 1983; Aiken and West 1991, pp. 160–165).

The most common techniques employed in IS research for moderator analysis are regression and ANOVA.<sup>2</sup> Yet, these techniques assume the single item measures being used are perfectly reliable (i.e., error free). To compensate for this, additional item measures are often created, combined into a summated scale, and then used in moderated regression or ANOVA analysis. The reliability of the scale is assessed using internal consistency measures such as Cronbach’s alpha, which (consistent with the summation process) assumes equal weighting of items.

While an improvement over single item measures, it is important to recognize at least two assumptions held in creating summated scales. The first assumption, by nature of the equal weighting process, treats all items as equal in their reliabilities. In turn, this implies all items are equal in their contribution towards estimating the interaction effect. The second assumption is the reliability of the summated scale will remain the same when applied later within a theoretical model. This assumption may not be true given that the reliability estimate is made in isolation as opposed to within the context for which it is subsequently used. Chin and Marcolin (1995), for example, have shown that the reliability of individual items, and therefore the internal consistency of scales, can differ when used in different models. Unfortunately, by virtue of the summation process, we have no opportunity to assess the validity of these two assumptions—that being equal item reliability and unchanging scale reliability.

Thus, moderator analysis should not only account for measurement error during the initial scale construction, but also during the statistical analysis that estimates the interaction effect. A more realistic approach would be to weight the individual items for each scale based on their individual contributions in the context of the interaction model being tested. By weighting items that are more predictive and reliable in estimating an interaction effect, a more accurate scale can be created. It should also provide information when the analysis is completed on the variability of each measure such that only more reliable measures are used for future research.

As a possible solution for assessing and accounting for measurement error when analyzing interaction effects, Kenny and Judd (1984) proposed using a product-indicator approach, in which measures of latent constructs are crossmultiplied to form interaction terms that are used to estimate the underlying latent interaction construct within the LISREL algorithm. While this general approach has been employed in several studies (Kenny and Judd 1984,

Jöreskog and Yang 1996), growing evidence from the literature suggests that the LISREL productindicator approach can be problematic for several reasons. These reasons include the fact that the LISREL product-indicator approach is technically demanding, often resulting in analytical errors and, even if modeled correctly, is not a complete solution (Bollen and Paxton 1998, p. 267; Li et al. 1998; Ping 1996). These problems are discussed in the Literature Review section below.

Overall, if IS theory is to develop in appropriate ways, our analytical techniques must help uncover the “true" underlying interaction effects we seek. It should neither hinder this search nor propagate the inherent weaknesses of older techniques. Hence, any IS researcher considering moderating influences within a theoretical model should be aware of the problems discussed in this paper so as to produce valid and accurate results.

Towards this end, we argue that a moderator's measurement error should be considered not only in initial reliability assessment, but also in subsequent analyses of the theoretical model. A new latent variable modeling approach within partial least squares (PLS) is shown to provide this subsequent assessment of measurement, thus overcoming problems within both traditional analytical techniques that can mask measurement error (e.g., aggregated or single indicators) and current problems associated with LISRELbased approaches.

Empirical data is presented to demonstrate how these analytical techniques impact theoretical development through the presentation of two studies: A simulated data set where the underlying true effects are known and an electronic-mail adoption data set where the emotion enjoyment is shown to have not only a substantial direct effect on adoption intention, but also an interaction effect that is stronger than those typically found in IS research. The simulated data set was developed using rigorous Monte Carlo techniques. The analysis of this data enables the comparison of factors—reliability, effect size, number of indicators, and sample size—that can influence measurement error within the analytical techniques.

It will be argued that the new latent variable modeling approach provides more accurate estimates of interaction effects by accounting for the measurement error within measures that, when ignored, can attenuate the estimated relationships. These more accurate estimates should improve the validation of theories, ensuring that fruitful avenues are maintained and new ones are detected. To the best of our knowledge, the use of product indicators to model interaction effects in a PLS analysis has never been published and by providing this new procedure, we believe researchers will be better able to more accurately detect and estimate contingent relationships—an ability that has been argued in the past to be an useful approach for advancing social science research (Greenwald et al. 1986).

The remainder of this paper is structured as follows. First, the growing importance of interaction terms within IS research is established, and the continuing tendency to employ analysis techniques that accounts for or assesses the fallibility of measures in this work is noted. A summary of the cumulative knowledge is presented, providing an overall picture of theoretical advancements surrounding interaction terms (i.e., moderators). These theoretical advancements include a discussion of measurement error, reliability, LISRELbased approaches, and summated scales to illustrate their role within the analysis of interaction terms. Then a new latent variable PLS modeling approach is introduced in an effort to improve on the previous shortcomings. Following that, two studies are presented to provide empirical evidence. Discussion and conclusions are then offered, summarizing how best to use this new approach.

## Literature Review

Interaction terms have been used in the IS field for some time; moderators, multiplicative terms, contingency terms or contingency theory, and interaction effects are all expressions used to refer to interaction terms. We begin by examining the growing importance of interaction terms within the IS literature and the extent to which previous IS contingency research has primarily applied analytical techniques, such as ANOVA<sup>3</sup> and multiple regression, that assume infallible measures. Measurement error is the primary problem that is exposed within these analytical practices, which raises other problems within this literature, such as the use of summated scales. The primary problem with these analytical practices is their inability to handle or present information relating to impact of measurement error. These problems are highlighted and discussed.

## Importance to Emerging Theory

Moderators are important to theories being advanced within the IS field, as can be seen by their long history in the literature and their increasing use in dominant theories. Two of these emerging IS theories that employ moderators are task-technology fit (Goodhue and Thompson 1995) and business-IT strategic fit (Chan et al. 1997), which are discussed after a brief review of the history of moderator use in IS research.

Through an exhaustive review of the information systems literature back to 1980,4 moderators were found to be present from the start and their importance is evident. For instance, Schonberger (1980) considered how information systems design approaches led to good systems but only when the contingent factors were appropriately matched, such as information needs for MIS supporting functions matching the decision-making type. More recently, McKeen et al. (1994) summarized the contingency studies that existed for the relationship between user participation and satisfaction, and suggested that two out of four moderating variables, namely task and system complexity, changed the relationship. However, with a change in $R ^ { 2 }$ of 0.012, these two moderators were considered unsubstantial. The authors concluded that these moderating variables were probably not the only two important ones and suggested five other promising moderators for future investigation. From the authors’ experience, the unmoderated relationship was not seen as adequate for an investigation into user participation and satisfaction. Throughout the years, similar studies employing moderators can be found in information systems research providing a long and important history.

In addition to this long history, moderators are increasingly used in dominant theories within the field. Two well-known theories in which the concept of moderation is important are Goodhue and Thompson's (1995) task-technology fit model and Chan et al.'s (1997) business-IT strategic fit model. Goodhue and Thompson (1995) suggest that technology characteristics, moderate relationships between task and individual characteristics, and system use. And, although the authors theorize the impact of technology characteristics on these relationships as moderating, they go on in this paper to develop these constructs in mediating,<sup>5</sup> as opposed to moderating, relationships. Chan et al. (1997) carried the moderation concept from theory to analysis. They found that alignment between business strategy and IT strategy was a better predictor of business performance and IS effectiveness than either strategy on its own. In their final analysis, they modeled alignment as a moderating influence on the relationship between IS strategy and business strategy. Several other dominant IS theories (Davis' 1989 TAM model, Doll and Torkzedah's 1991 user participation/involvement model) and the streams of research that extend these models and others (e.g., Hartwick and Barki 1994, p. 461) suggest that moderators are an important avenue of future development, and many calls are noted in the literature. McKeen et al. (1994) noted these calls as far back as 1984 (Ives and Olson 1984) and heralded the investigation of more contingency factors and the expansion of the theoretical complexity of moderated models. These calls are constantly repeated within the field (e.g., Anderson 1985, Vanderslice 1987, Tait and Vessy 1988, Doll and Torkzedah 1989, Sambamurthy and Zmud 1999).

In addition to calls from within the field, there is evidence from other fields that the relatively young

IS field can expect moderators to grow in prominence. If the IS field follows a similar evolutionary path to that of other fields, such as organizational behavior and psychology (Stone 1988), moderators will likely be used more and assume a prominent role within IS research investigations. This trend is evidenced in the literature6 with the number of articles that investigate moderators steadily rising since 1980 and the number of moderators within these articles continually expanding. As the IS field applies more complex theories, its methodologies and analytical approaches, such as the use of moderators, will become more important. Dominant theories are, increasingly, employing moderators in a central role, one that is likely to remain for some time.

## Problems Emerging

Although many laud the importance of moderators within theoretical development, others within the IS field have questioned the overall usefulness of contingency research (which is based on moderators). Weill and Olson (1989) did exactly this when they stated that the “highly mixed empirical results” (p. 79) is evidence of a lack of contribution to knowledge (p. 67). Cavaye (1995) suggests that the “literature regularly proclaims” (p. 319) the importance of moderating influences for user participation and IS development project success, but “empirical research continues to provide inconsistent results" (p. 319). These inconsistencies raise doubt in researcher’s minds, bringing into question the value of this work (p. 317) and creating a mistaken impression that moderators are not important.

In fact, this negative conclusion is exactly the opposite of what Cavaye (1995) was arguing, although never stated explicitly. She argued that contingency factors might explain many of these “inconsistent" or “inconclusive” results, listing numerous moderating influences that might better capture this theoretical relationship. Raising the importance of moderators within theoretical development is exactly her point and an underlying message of this paper. To accomplish this, however, we need to be aware of the shortcomings of our current techniques

## Current Shortcomings in the Moderator Literature

The difficulties, as expressed within the moderator literature,7 are presented next. In particular, we focus on eight, emergent, key problem areas for assessing moderators,<sup>8</sup> including measurement error and how reliability, summated scales, number of indicators, effect size, sample size, power, and incomplete reporting influence the subsequent empirical analyses and results.

Measurement Error and Reliability. error is most often assessed first through reliability analysis and then ignored or constrained in the subsequent analysis of the theoretical relationships. The sequence goes as follows: Measurement error assessments typically begin with a Cronbach's reliability check where reliability levels are determined and poorly convergent items are excluded, then variables are aggregated into a single score (e.g., summed or averaged).<sup>9</sup> Once this aggregation or reduction to a single item takes place, further assessment of measurement error in any subsequent analysis is impossible because the measurement error has been fixed by the scale construction method. Fixing in this way causes inaccuracies in the subsequent estimates of the theoretical relationships, as will be shown below.

Compounded with this fixed-scale construction is the use of subsequent analytical techniques that cannot assess measurement error. Regression and ANOVA are the preferred methods used to test moderators (see Tables 1 and 2<sup>7</sup> <sup>8</sup>) in IS research, and they, by definition, focus on single measures (scaled or otherwise). Unfortunately, additional tests to assess the discriminant and nomological validity of the individual items within the theoretical model (i.e., main and interaction effects) can never be made. Measurement error as a result of a multi-item scale cannot be assessed within these techniques, and, as a result, issues of multidimensionality, poor items and construct interpretation are hampered.

Summated Scales. scales is noted here as the practice is often proposed as the solution to the measurement error problem. To overcome the issue of single indicators, many researchers have employed the practice of summing items to create a single indicator for use within regression or ANOVA,<sup>10</sup> with the belief that the resulting summated scale better accounts for the underlying measurement error (Gelderman 1998, same issue for averaged scales; Igbaria and Baroudi 1993). Although this summation practice performs better than single indicators, it can mask measurement error through the two-step process described above in which item aggregation is performed outside of the theoretical context in which the aggregated score is subsequently used. Thus, summated scales, while found to be the standard practice in the IS literature, can be suboptimal in two ways: Equal item reliability and unchanging scale reliability.

In summing items into a single measure, the assumption is made that all items are equally reliable. However, this summing approach, while reducing measurement error, is suboptimal relative to the PLS algorithm. PLS treats each indicator separately, allowing each item to differ in the amount of influence on the construct estimate. Therefore, indicators with weaker relationships to related indicators and the latent construct<sup>11</sup> are given lower weightings (Lohmöller 1989; Wold 1982, 1985, 1989), resulting in higher reliability for the construct estimate and thus stronger theoretical development.

Summated scales can also be suboptimal because the reliability estimate of the construct is made in isolation from the theoretical model in which it is to be used. The practice of aggregating items may give a false sense that measurement error has been handled when, in fact, measurement error should be rechecked in the context of the final theoretical model before assurances of minimal measurement error are made. As will be shown in the empirical data section, the two-step approach leads to suboptimal estimates and yet, as seen from our review, represents the current dominant approach used in IS research.

<sup>Number</sup> <sup>of</sup> <sup>Items.</sup> The next logical extension is to begin employing multiple measures so as to capture and analyze measurement error. Reliability theory tells us that the greater the number of indicators used to measure a construct, the more reliable and accurate the subsequent analyses will be (Carmines and Zeller 1979). Furthermore, reliability increases even faster when higher quality (i.e., more reliable) individual items are used, and hence, higher quality items should always be the goal. However if high quality items cannot be guaranteed, extra items should be proposed and analyzed.

Few moderator studies are employing these high quality or multiple item scales. Although reliability is not always reported, our best guess from a review of the reported data is that the IS field is achieving about 0.70 reliability. From a review of the regression and path analysis articles, which are closest to accounting for measurement error, the average number of indicators observed was three.<sup>12</sup> Most structural equation modeling literature suggests that three indicators should be a minimum and not an average (Bollen 1989). Consequently, when reliability is lower or the number of indicators is small, measurement error is more problematic, which further complicates theoretical model development.

LISREL Solution for Summated Scales. iance-based techniques, such as LISREL, can accommodate measurement error but are not necessarily the best alternative for overcoming summated scale problems. These techniques have been shown to be less than ideal under many data conditions for analyzing interaction terms using the productindicator approach (Bollen and Paxton 1998, p. 267; Li et al. 1998, p. 240; Ping 1996). Comparisons between LISREL and PLS are highlighted in Table 4,13 discussed below, and compared later to the PLS productindicator approach.

Various LISREL specifications have been conducted in the past (Kenny and Judd 1984, Jöreskog and Yang 1996); however, Ping (1996) recently noted that these covariance-based procedures “may produce specification tedium, errors, and estimation difficulties in larger structural equations models" (p. 166). Part of the difficulty involves the need to calculate and specify in the software the required set of <sup>nonlinear</sup> <sup>constraints</sup>, which increases exponentially with the number of indicators. In agreement, Bollen and Paxton (1998, p. 267, emphasis added) stated that “the best known procedures for models with interactions of latent variables are tech-<sup>nically</sup> <sup>demanding</sup>. Not only does the potential user need to be familiar with structural equation modeling (SEM), but the researcher must be familiar with programming nonlinear and linear constraints and must be comfortable with fairly large and complicated models.” In agreement, Li et al. (1998, p. 26) stressed “the need for care in the specification of nonlinear constraints in models” and go on to state that “mistakes can easily be made, the consequences of which may be worse than ignoring the interaction effect in the first place.” Again, these constraints grow exponentially with the number of interaction terms.

To overcome the need to calculate such constraints, Ping (1995, 1996) recommended an <sup>alternative</sup> <sup>two-step</sup> <sup>approach</sup> that advocates conducting analysis in two steps, separating measurement and structural model assessments. However, the ability to assess the reliability and validity of individual items using such a two-step approach has been questioned (Fornell and Yi 1992). The two-step approach makes more demanding analytical assumptions concerning both uncorrelated errors and multivariate normality of observed variables, and fails to adjust standard errors for constrained parameters that are necessary so as to anchor scales for interpretation (Bollen and Paxton 1998, p. 280). Thus, the standard errors of estimates for parameters, such as loadings, error terms, and variance of latent product variables, are unknown and no significance test statistics are available two-step method provides only an <sup>approximation</sup> <sup>of</sup> the true results ing assumptions are met. Those assumptions are that (a) the model is correct and (b) the data are multivariate normal (Li et al. 1998, p. 24), which are two conditions that are often not met.

Even if the preceding conditions are met, there are additional operational issues to consider. In general, when the number of indicators in a model goes beyond 40 or 50, computation tends to not even converge. Because of the full information algorithm, the computational demands grow exponentially as one increases the number of items used. In addition, the sample size required to yield stable parameter and model fit estimates must also increase (more on this issue later).

Finally, in contrast to both summated regression and our PLS approach, the LISREL algorithm does not explicitly calculate construct scores. Thus, if a goal of the researcher is to obtain a single best approximation of each construct, LISREL will not provide this as part of the process in estimating the interaction effect. In all, LISREL moderator specifications are technically demanding and not necessarily the complete solution.

## Effect Size, Power, Sample Size, and Reporting

Other problems noted in the literature included effect sizes, sample size, power, and incomplete reporting, which are often intertwined with each other and, hence, are handled here collectively so as to highlight the types of problems encountered. Only 21% of the moderators tested in IS studies (Table 1) were found to be significant, which begs the question as to whether the other effects did not exist or were just not detected?

Effect size<sup>14</sup> was not reported for 71% of the significant moderators in the nine regression-based articles (Table 3). The three remaining moderator estimates, based on Cohen’s (1988) guidelines, yielded two small effects (0.036 and 0.050) and a medium effect (0.123). Several things accounted for our inability to report the effect sizes of the interaction terms in the reviewed work, including the use of techniques that restrict an effect size calculation such as split samples, the lack of sufficient information (e.g., standard error) to standardize unstandardized estimates, or omission of effects in the manuscripts for other unspecified reasons. Inconsistent reporting, the latter finding, hinders any attempt to aggregate the field of knowledge (Weill and Olson 1989).

Sample sizes averaged 81.5 for articles using regression or path analysis, and 148 for articles using analysis of variance techniques (Table 1). Statistical power was reported in only four articles with just one of these indicating the recommended 0.80 (Cohen 1988). In general, power is impacted by small effect sizes, small sample sizes, random measurement error, larger standard deviation, and nonnormal data distributions. Given the fact that many of these power-limiting conditions existed within the literature reviewed, one wonders whether an explanation for the null results is that they were just not detected.

In conclusion, moderators have a long history within the IS research field and are gaining prominence in many emerging theories. Despite the ongoing calls to increase investigation into moderating effects, problems have emerged around measurement error, reliability, single item measures, summated scales, inconsistent results, and small overall impact. Few studies have used analytic techniques that can calculate effect size or can present a complete solution (e.g., LISREL). Power levels tend to be low. Meta-analyses are either theoretical (Trice and Treacy 1986, Goodhue 1986) or report inconsistent results (Cavaye 1995). These inconsistent results are often blamed on different operationalizations of the constructs, uncontrolled research factors, inappropriate quantitative studies with little richness in the understanding of the influences, and poorly validated instruments (Cavaye 1995). We believe these problems are opportunities for improvement.

To such an end, a new latent variable modeling approach for analyzing interaction effects is now introduced and its ability to address these problems is discussed. Empirical evidence is then presented from two studies: A Monte Carlo study and an IT-adoption data set. The Monte Carlo study allows us to assess the approach’s improvement over previous techniques, while the IT adoption study demonstrates the use of the new approach within an actual IS data set and theoretical framework.

## PLS Product-Indicator Approach for Measuring Interaction

To account for the effects of measurement error, a product-indicator approach in conjunction with PLS is proposed. To the best of our knowledge, this represents the first time such a technique has been applied using PLS for assessing interaction effects. Both Chan et al. (1997) and Bergeron et al. (2001), for example, discuss the theoretical implications of moderators as a fit variable but never fully demonstrate the empirical properties of such a product-indicator technique. Chan et al.’s (1997) work comes closest to a moderated model but was missing two crucial main effects paths in the final model analyzed. Paths between each exogenous15 construct and each endogenous construct, in this model, must be analyzed. When the main effect variables are missing in the analysis, interaction path coefficients are not true interaction effects (Jaccard et al. 1990). Furthermore, the individual items were not centered or standardized, the moderation scores were averaged and the scores were then used as a formative measure,16 a sequence that results in uninterpretable coefficients.<sup>17</sup> Consequently, an empirical demonstration of the PLS technique is crucial for understanding an appropriate analytical process in which such errors in execution are avoided.

## PLS Appropriateness

The use of PLS has been gaining interest and use among IS researchers in recent years (Compeau and Higgins 1995, Aubert et al. 1994, Chin and Gopal 1995) because of its ability to model latent constructs under conditions of nonnormality and with small to medium sample sizes. It is important to recognize that the operational act of creating product terms by multiplying measures together (to be discussed next) in and of itself is not new. These product terms are used in traditional multiple regression and, as described earlier, have been used for covariance-based solutions using software such as LISREL. Rather, it is the coupling and conceptualization of these product indicators within an easy-to-use PLS context that is new.

Being a components-based structural equation modeling technique, PLS is similar to regression, but simultaneously models the structural paths (i.e., theoretical relationships among latent variables) and measurement paths (i.e., relationships between a latent variable and its indicators). Rather than assume equal weights for all indicators of a scale, the PLS algorithm allows each indicator to vary in how much it contributes to the composite score of the latent variable. Thus, indicators with weaker relationships to related indicators and to the latent construct are given lower weightings, and those varied weightings are carried through to an assessment of the theoretical estimates. In this sense, PLS is preferable to techniques such as single-item regression that assumes errorfree measurement, summated regression that assumes equal-weighted measurement and factor score-based regression that assumes constrained measurement error within the estimates of the theoretical variables (Lohmöller 1989; Wold 1982, 1985, 1989).18

Our PLS product-indicator approach represents a one-step technique that requires no additional specification of parameter constraints or assumptions of multivariate normality, can be used to estimate large complex models (even when embedded in the middle of a nomological network), and estimates standard errors via resampling procedures (see Chin 1998b for a discussion of resampling procedures in conjunction with PLS). Furthermore, <sup>sample</sup> <sup>size</sup> (as to be demonstrated by the Monte Carlo study) is not constrained by the number of product indicators as would be the case in LISREL estimations, which require increasingly larger sample sizes as the number of indicators grows. A simple PLS heuristic<sup>19</sup> for main-effects-only models indicates that a sample size of 30 would be a reasonable starting point for the three-construct model discussed here and is independent of the number of indicators used. As shown in Appendix A, the comparable LISREL sample would be 200 and increases quickly as the number of indicators increase (up to 1,820 sample size for 12 indicators). Practically, as the model complexity increases beyond 40 or 50 indicators, the LISREL software may <sup>not</sup> <sup>even</sup> <sup>converge</sup>. The PLS approach, in contrast, has been shown to yield computational results for a model with 672 indicators, 21 latent variables, and 200 cases in approximately 1.5 minutes on a 166-MHz Pentium computer (Chin and Newsted 1999, p. 335).

The final point of comparison to be clarified is that the underlying assumption of <sup>uncorrelated</sup> <sup>error</sup> <sup>terms</sup> among indicators cannot, by definition, hold true for any moderator analysis (see Kenny and Judd 1984 for derivation). Because they are created through multiplication, the error terms for the product indicators are partially correlated with the error terms for the indicators of the other exogenous constructs.<sup>20</sup> While problematic if not accounted for within covariancebased modeling software such as LISREL, these correlations may actually help provide a more accurate estimation of the interaction effect when using PLS The reason is that there is a known bias in PLS that underestimates the structural effects.21 While there are no known ways to estimate the amount of bias or inaccurate estimates in a complex model, we do have formulae to account for this bias in single- and twoconstruct models (see Chin 1998b, p. 330 for details). In these cases, bias is reduced with more indicators, and hence we can expect the same tempering effects within our Monte Carlo analysis. Whether or not reduced bias continues to be true in the multiconstruct case will be assessed in the next section. Overall, we believe that the data conditions within the IS field are likely more aligned with the requirements of the PLS approach than the requirements of the LISREL approach.

## PLS Setup

Predictor, moderator, and dependent variables under this PLS approach are viewed as latent variables or constructs, which are ideas that cannot be measured directly. Instead, multiple indicators, or measures, for these latent variables must be obtained. Although it is possible to gather measures in many ways, one example of a measure is a survey question in a data collection instrument. For this analytic technique, each indicator is modeled as being influenced by both the underlying latent variable (i.e., reflective indicators) and error. Product indicators reflecting the latent interaction variables are then created by multiplying the indicators from the predictor and the moderator variables (see Figure 2). This analytical model is consistent with the theoretical model shown in Figure 3. Each set of indicators reflecting their underlying construct or latent variable are then submitted to PLS for estimation resulting in a more accurate assessment of the underlying latent variables and their relationships.

Figure 2 Model with Three Indicators per Main Construct and Nine Produce Indicators for the Interaction Construct  
![](/api/attachments/PJNPTKAY/fulltext/images/256a2aad2796666bf3b01959db9611d36bd780296a2bf8a2acdaceaa18f12819.jpg)  
Note. Path coefficients at the levels specified were created through Monte Carlo simulations.

## Standardizing or Centering Measures

An important step in undertaking the PLS productindicator approach is to determine whether indicators must be standardized or centered. Standardizing or centering indicators helps avoid computational errors by lowering the correlation between the product indi-

Figure 3 Comparable Theoretical Model for Analytic Model in Figure 2  
![](/api/attachments/PJNPTKAY/fulltext/images/9086217bd5310ba0368464548823f725e7bd0c513aba04660d8aee6c7ed42b7d.jpg)

<sup>21</sup> It will be demonstrated in the next section that this PLS bias is less problematic than regression’s underestimation.

cators and their individual components (Smith and Sasaki 1979); consequently, <sup>one</sup> of the techniques must always be used. Furthermore, without such a process, each product term would likely have a different interpretation, limiting the ability of the PLS procedure to accurately estimate the underlying interaction construct. Standardizing or centering the indicators also allows an easier interpretation of the resulting regression beta for the predictor variable. This beta represents the effect expected at the mean value of the moderator variable, which is set to zero.

Standardization is used for reflective measures if it is decided that they can be conceived of as approximately parallel indicators (i.e., equivalent in their measurement of the underlying construct) and no a priori emphasis is given to a particular indicator in the set. Under this situation, all indicators reflecting the predictor and moderator constructs are standardized<sup>22</sup> to a mean of zero and variance of one (Jaccard et al. 1990, Aiken and West 1991). This approach can be done for ordinal- and interval-level items, such as Likert-scaled attitudinal items, and must be calculated before submitting the data to PLS. Many statistical packages can save standardized Z scores to a file to facilitate this calculation.

Alternatively, centering can be used to maintain the scale metric (or units of measurement), which might be necessary for theoretical interpretation. If it is decided that some indicators are theoretically more important than others, indicators would only be centered—to achieve a mean of zero—by sub tracting the mean from every score. This centering technique is only used if it is felt that the original metric of the items or their variances should be maintained, and usually must be calculated explicitly within a statistical package before submitting the data to PLS. For ratio-level items, it is important to have all items transformed to the same metric in addition to being centered. For example, if you measured temperatures in both Celsius and Fahrenheit, you must convert them all to the same scale. After that, you need to center each temperature indicator by subtracting the respective means of the converted scales from their respective data values. Otherwise, the estimated latent variable score produced by PLS would be indeterminable and hence uninterpretable.

## Calculating Interaction Term Measures

Once the standardized or centered indicators of the predictor variable <sup>X</sup> and the moderator variable <sup>Z</sup> are calculated, product indicators are developed by creating all possible products from the two sets of indicators, usually through an explicit multiplication. These product indicators are used to reflect the latent interaction variable. For example, if there are three measures reflecting the main predictor <sup>X</sup> and three measures for the moderator variable <sup>Z</sup>, there would be nine measures for representing the interaction term $X * Z .$ Graphically, this is depicted in Figure 2. Because any indicator reflecting the predictor <sup>X</sup> or moderator Z is viewed as interchangeable with another from the same set, any product indicator $x _ { i } * z _ { i }$ would represent a parallel measure of the underlying latent interaction variable X \* Z.

## PLS Estimation

The PLS procedure is then used to estimate the latent variables as an exact linear combination of its indicators with the goal of maximizing the explained variance for the indicators and latent variables. Following a series of ordinary least squares analyses, PLS optimally weights the indicators such that a resulting latent variable estimate can be obtained.23 The weights provide an exact linear combination of the indicators for forming the latent variable score that is not only maximally correlated with its own set of indicators, as in components analysis, but also correlated with other latent variables according to the structural, or theoretical, model.

Empirical data illustrating the PLS approach is now presented. Because our purpose is to improve on the dominant technique found in the literature (i.e., regression and ANOVA), comparisons to singleindicator regression and summated regression are included. The first study presents a simulated Monte Carlo data set where true effects are known and the ability of each technique to estimate these coefficients is shown. The second study presents an IS data set around e-mail adoption with the moderating influence of emotion.

## Study 1: Monte Carlo Simulation

To test the efficacy of the PLS product-indicator approach for detecting and estimating interaction effects where measurement error exists, a Monte Carlo simulation study was first executed. PLS, single-indicator regression, and summated regression analytical techniques are compared under varying conditions of effect size, sample size, number of indicators, and measurement error—the influences most prevalent in the literature and central to the interaction term analysis. We begin our presentation of this study by explaining Monte Carlo simulation and follow this with a description of the predetermined population parameters used to assess our PLS product-indicator approach. Because accounting for measurement error is at the heart of the difference between the PLS and regression techniques, loading patterns are first held at a level of 0.70 to provide a baseline comparison, and later varied to extend our understanding. The baseline case and subsequent variations are briefly outlined before the simulation results are shown.

## Monte Carlo Simulation

Monte Carlo simulations are typically applied by latent variable/structural equation modeling researchers to ascertain the robustness of statistical estimators (e.g., Chin and Newsted 1999, Chou et al. 1991, Sharma et al. 1989). Monte Carlo simulation refers to a procedure of generating artificial data, based on a specific statistical model that is defined in terms of a stochastic generating mechanism (Noreen 1989). In other words, we create data that conforms to specifically stated model parameters, such as structural paths (e.g., main and interaction effects), factor loadings, and error terms. Two different approaches have been used to generate data to assess the robustness of latent variable methods In the Monte Carlo approach, the implied covariance matrix of the observed variables is computed for given values on the parameters in the model and then data are generated on the observed variables from a multivariate distribution having this covariance matrix. Thus, data are only generated for the observed variables and not for the construct level. In the alternative approach, data are first generated for the latent variables according to the relationships specified in the model and then data are generated for the observed variables from the latent variables in the model. This latter approach is better suited to generate data with the distributional characteristics imposed by the model. For this study, we apply the second approach, consistent with the examples and functionality available in the software package PRELIS 2.14 (Jöreskog and Sorbom 1993).

## Monte Carlo Population Parameters

Using PRELIS 2.14 (Jöreskog and Sorbom 1993), data were generated to conform to an underlying population model where the standardized beta of X on Y was 0.30, the beta of Z on Y was 0.50, and the interaction effect (X \* Z) was 0.30. The model is shown in Figure 2. Indicators for all primary constructs, or latent variables, were modeled as having factor loadings of 0.70 because this is a minimum standard of the IS literature.24 Thus, the true scores for the main and interaction effects are known. The goal here is to determine how well the PLS product-indicator approach detects and recovers (i.e., estimates) the true effects under conditions of measurement error.

## Monte Carlo Design—The Baseline Case and Subsequent Cases of Comparison

The Monte Carlo design is intended to achieve several objectives. The first objective, as our baseline case, is to assess how well the new PLS product-indicator method performs at retrieving the true population parameter. As such, sample sizes are varied at 20, 50,

100, 150, 200, and 500 cases, and the number of indicators per primary construct of X, Z, and Y are varied at 1, 2, 4, 6, 8, 10, and 12. For each cell in this completely crossed design, 500 simulations were performed. For example, in the cell representing sample size 50 and 4 indicators per construct, 500 data sets were generated consisting of sample sizes of 50 where each case had 4 indicators for each of the 3 constructs $X , Z ,$ and <sup>Y</sup> (factor loadings of 0.70), and 16 product indicators for <sup>X</sup> ∗ <sup>Z</sup> (factor loadings of 0.49).

A second objective, after examining the absolute performance of the new approach, is a comparison to regression-based estimates. A comparison between the PLS product-indicator approach and singleindicator regression is made, which represents a simple initial point of departure to establish the relative effectiveness of the product-indicator approach in accommodating measures with error. In addition, the comparison between the PLS product-indicator approach and the common practice of summing scales within a regression analysis (the often suggested solution for addressing measurement error) is also undertaken. Using the data generated from the Monte Carlo simulation, summated scales are created and employed in additional regression analyses. The path estimates for the summated regression analyses are then compared to those obtained via the PLS productindicator approach.

As a final objective, unequal loadings (a situation more typical among research studies) are compared with the Monte Carlo data for the PLS productindicator and summated regression approaches. While the next analysis is not exhaustive, a brief simulation is provided to see how both techniques perform under conditions of heterogeneous loading patterns (i.e., not all 0.70).

Having described the Monte Carlo objectives, the results are now presented. We begin with a discussion of significant levels and the influences of sample size and number of indicators followed by a discussion of the ability to estimate the known/true underlying path estimates.

## Significance

Tables $5 , 6 ,$ and 7 provide the results and significance tests for the $6 \times 7$ crossed design in which PLS runs were made using PLS-Graph version 3.0 (Chin 2001). As noted, a single indicator multiple regression forms the initial baseline of comparison for how well the PLS product-indicator approach performs. Results of using single-indicator regression with varying sample sizes are provided in the column of Table 7 labeled “one item per construct.” When using PLS, the case of one indicator per construct is identical to performing a multiple regression with a single-indicator measure.

Accurate estimates are invaluable to IS research and only achieved if analytical techniques can both detect and estimate the true scores. Advocating that detection by itself is sufficient (i.e., significance) is incomplete because the goal is to accurately detect the true score if it exists. Hence, we will first examine the pattern of significance and then, with this pattern in mind, consider the accuracy of the estimations. Only then can conclusions be drawn.

Significance levels achieved within each cell from the single-indicator regression and PLS analyses are shown in Table 5. In general, small sample sizes or few indicators produced few significant estimations at $p \leq 0 . 0 5$ . For example, multiple regression using a single indicator, as represented by the first column, did not detect a significant effect. The predictor X term and the moderator Z term achieved significance sooner at sample sizes of 100 and 50, respectively. Consequently, PLS’s ability to estimate the noninteraction terms that are either more reliable or have larger effect sizes <sup>z</sup> = 0 50<sup></sup> is reaffirmed. The singleindicator approach appears inadequate for estimating interaction terms because no results were significant.

Let us pause for a moment to understand three possible patterns of significance. These ideal patterns of results, as shown in Table 6, might be formed if (i) only the number of indicators has an influence, (ii) only sample size has an influence, or (iii) both have an equal influence. A solid line is drawn to distinguish where the results change from nonsignificant to significant.

If only the number of indicators had an influence, then a solid vertical line would be observed as shown in Table 6(i), because no matter how large the sample size grew, the significance within a column would not change. If only sample size had an influence, then a solid horizontal line would be observed as shown in

![](/api/attachments/PJNPTKAY/fulltext/images/b2372dbbefd946d139cfe89d6d475f50139b74d7959d893b91039a19790dff93.jpg)  
(i) Only number of indicators has an effect

![](/api/attachments/PJNPTKAY/fulltext/images/4b40192d5297de0cdceff30fbe26e555dc8484fca83dcccf96bdad29e8e65c79.jpg)  
Table 6 Possible Patterns of Significance Indicators

Table 5 Tests of Significance for the Mean Estimates Shown in Table 7 (500 Runs in Each Cell) Predictor: X (.30) Number of Indicators (dashed line)

<table><tr><td>Sample Size</td><td>1</td><td>2</td><td>4</td><td>6</td><td>8</td><td>10</td><td>12</td></tr><tr><td>20</td><td colspan="7"></td></tr><tr><td>50</td><td colspan="4"></td><td>*</td><td>*</td><td>*</td></tr><tr><td>100</td><td colspan="2"></td><td>**</td><td>**</td><td>**</td><td>**</td><td>**</td></tr><tr><td>150</td><td></td><td>**</td><td>**</td><td>**</td><td>**</td><td>**</td><td>**</td></tr><tr><td>200</td><td></td><td>*</td><td>**</td><td>**</td><td>**</td><td>**</td><td>**</td></tr><tr><td>500</td><td></td><td>*</td><td>**</td><td>**</td><td>**</td><td>**</td><td>**</td></tr></table>

<table><tr><td>Sample Size</td><td>1</td><td>2</td><td>4</td><td>6</td><td>8</td><td>10</td><td>12</td></tr><tr><td>20</td><td colspan="7"></td></tr><tr><td>50</td><td colspan="2"></td><td>**</td><td>**</td><td>**</td><td>**</td><td>**</td></tr><tr><td>100</td><td colspan="2">*</td><td>**</td><td>**</td><td>**</td><td>**</td><td>**</td></tr><tr><td>150</td><td></td><td>**</td><td>**</td><td>**</td><td>**</td><td>**</td><td>**</td></tr><tr><td>200</td><td colspan="2">*</td><td>**</td><td>**</td><td>**</td><td>**</td><td>**</td></tr><tr><td>500</td><td colspan="2">*</td><td>**</td><td>**</td><td>**</td><td>**</td><td>**</td></tr></table>

<table><tr><td>Sample Size</td><td>1</td><td>2</td><td>4</td><td>6</td><td>8</td><td>10</td><td>12</td></tr><tr><td>20</td><td colspan="7"></td></tr><tr><td>50</td><td colspan="7"></td></tr><tr><td>100</td><td colspan="2"></td><td>*</td><td>**</td><td>**</td><td>**</td><td>**</td></tr><tr><td>150</td><td></td><td>*</td><td>**</td><td>**</td><td>**</td><td>**</td><td>**</td></tr><tr><td>200</td><td></td><td></td><td>**</td><td>**</td><td>**</td><td>**</td><td>**</td></tr><tr><td>500</td><td></td><td></td><td>**</td><td>**</td><td>**</td><td>**</td><td>**</td></tr></table>

Note. ∗p < 005 (one-tailed t value: 1.66, df 499).  
∗∗p < 001 (one-tailed t value: 2.36, df 499) (outlined by the dark line).  
(ii) Only sample size has an effect

![](/api/attachments/PJNPTKAY/fulltext/images/66bb405a5b67dfc8ad88c6de743af0c1a265959e98eff2cf9c59dab17d6b57d3.jpg)

Table 6(ii), because no matter how many indicators were used the significance within a row would not change. Finally, if both had an equal influence, then a tiered, diagonal line would be observed as shown in Table 6(iii), because significance would change incrementally by both rows (sample size impact) and columns (indicator impact). These patterns will be compared throughout the results.

<sup>Sample</sup> <sup>Size.</sup> As a general observation regarding Table 5, it can be seen that smaller sample sizes did not produce significant results for many of the combinations across each of the predictor, moderator and interaction terms. The sample size of 20 failed to detect the true effect in all combinations. Interaction term results for the sample size of 50, also, were not significant. Small sample sizes clearly should be avoided when analyzing moderator variables

For larger sample sizes, there appears to be a threshold after which an increase in sample size does not change the significance level.<sup>25</sup> The dashed, solid, and double lines designate the division between nonsignificant and significant at 0.01, a conservative level that balances both detection and estimation results as will be seen below. The first two parts of Table 5 for predictor <sup>X</sup> and moderator <sup>Z</sup> appear to have flat, horizontal lines, and the last part for the interaction term appears to have a more slightly tiered pattern. Accordingly, these patterns reconfirm that, for the PLS product-indicator approach, sample size is more influential in determining significance for noninteraction terms and terms with large effect sizes, but the patterns also suggest that both sample size and the number of indicators are influential in determining significance for interaction terms. The equality of these latter influences will be revisited again when reviewing path estimation.

<sup>Indicators.</sup> The influence of indicators is promising. More indicators were generally significant, and it is clearly seen that fewer indicators (under four) often lead to nonsignificant results until either a larger sample size was used, such as 150 or over, or a true effect was larger, such as $Z = 0 . 5 0 .$ . Significance at 0.01 was achieved for the interaction term at 6 indicators—100 sample size, and 4 indicators—150 sample size, representing ideal threshold values for sample size and number of indicators in PLS.

Taken together, the results of significance levels for sample size and number of indicators suggest that appropriate detection of interaction terms require sample sizes of 100–150 and 4 or more indicators for each predictor and moderator constructs. The ideal threshold combinations outlined above imply that increasing the number of indicators when analyzing moderators is just as important as gathering more data. Determining significance is an important first step and essential when calculating the correct path estimates. The ability of the techniques to capture true path estimates is now explored.

## Path Estimation

After reviewing significance, true score estimation can be addressed. Table 7 provides the path estimations and standard error results for the different combinations of sample size and number of indicators.

## Single-Indicator Regression

Keeping in mind that a perfect estimation procedure should result in 0.30 for the <sup>x</sup> to <sup>y</sup> path, 0.50 for the <sup>z</sup> to <sup>y</sup> path, and 0.30 for the <sup>x</sup> ∗<sup>z</sup> to <sup>y</sup> path, note that the Table 7 single-indicator regression results (Column 1), which are under conditions of measurement error, consistently (and significantly) underestimated these true effects. The reason, as discussed earlier, is that single-indicator regression does not explicitly take into account the attenuating effects of measurement error. At a sample size of 500, for example, path estimations for single-indicator regression are one-half to one-third of the true effects. Estimation of the interaction term, keeping in mind that none yielded significant results, was only 0.098—far from the 0.30 true score. Therefore, the single-indicator regression approach never seems to yield the true effects even when larger sample sizes are used.

## Ideal PLS Interaction Terms

Estimation with the PLS product-indicator approach is promising. Specifically, the number of indicators has a slightly greater positive impact on results than do larger sample sizes. This conclusion is based on the observations that, as shown in Table 7, the interaction term estimation (values below the double lines are significant) approaches the 0.30 true score at 8 indicators—100 sample size within 10% of the true score (i.e., above 0.27) and is close to estimation at 6 indicators—150 sample size. These cell combinations are slightly higher than the threshold ideals suggested above, with the 4 indicators—150 sample size combination falling about 15% away from the true score.

Table 7 PLS Path Estimation from Monte Carlo Simulation (500 Runs per Cell)

<table><tr><td></td><td colspan="7">Indicators per construct</td></tr><tr><td>Sample size</td><td>one item per constructa</td><td>two per construct (4 for interaction)</td><td>four per construct (16 for interaction)</td><td>six per construct (36 for interaction)</td><td>eight per construct (64 for interaction)</td><td>ten per construct (100 for interaction)</td><td>twelve per construct (144 for interaction)</td></tr><tr><td>20</td><td>x --&gt;y 0.186(0.276)z --&gt;y 0.330(0.286)x*z--&gt;y 0.162(0.352)</td><td>x --&gt;y 0.186(0.276)z --&gt;y 0.330(0.286)x*z--&gt;y 0.162(0.352)</td><td>x --&gt;y 0.215(0.250)z --&gt;y 0.334(0.264)x*z--&gt;y 0.250(0.370)</td><td>x --&gt;y 0.219(0.237)z --&gt;y 0.335(0.251)x*z--&gt;y 0.276(0.377)</td><td>x --&gt;y 0.217(0.238)z --&gt;y 0.341(0.254)x*z--&gt;y 0.267(0.402)</td><td>x --&gt;y 0.220(0.237)z --&gt;y 0.341(0.251)x*z--&gt;y 0.305(0.375)</td><td>x --&gt;y 0.217(0.223)z --&gt;y 0.323(0.259)x*z--&gt;y 0.308(0.424)</td></tr><tr><td>50</td><td>x --&gt;y 0.130(0.220)z --&gt;y 0.241(0.298)x*z--&gt;y 0.104(0.248)</td><td>x --&gt;y 0.195(0.187)z --&gt;y 0.326(0.218)x*z--&gt;y 0.172(0.236)</td><td>x --&gt;y 0.232(0.153)z --&gt;y 0.386(0.159)x*z--&gt;y 0.274(0.186)</td><td>x --&gt;y 0.251(0.139)z --&gt;y 0.390(0.154)x*z--&gt;y 0.276(0.232)</td><td>x --&gt;y 0.263(0.131)z --&gt;y 0.403(0.142)x*z--&gt;y 0.304(0.216)</td><td>x --&gt;y 0.264(0.124)z --&gt;y 0.396(0.142)x*z--&gt;y 0.320(0.230)</td><td>x --&gt;y 0.267(0.126)z --&gt;y 0.418(0.134)x*z--&gt;y 0.333(0.221)</td></tr><tr><td>100</td><td>x --&gt;y 0.140(0.186)z --&gt;y 0.247(0.270)x*z--&gt;y 0.114(0.210)</td><td>x --&gt;y 0.208(0.130)z --&gt;y 0.326(0.195)x*z--&gt;y 0.169(0.181)</td><td>x --&gt;y 0.256(0.091)z --&gt;y 0.382(0.143)x*z--&gt;y 0.256(0.120)</td><td>x --&gt;y 0.260(0.100)z --&gt;y 0.410(0.120)x*z--&gt;y 0.282(0.119)</td><td>x --&gt;y 0.274(0.078)z --&gt;y 0.431(0.097)x*z--&gt;y 0.304(0.112)</td><td>x --&gt;y 0.283(0.080)z --&gt;y 0.434(0.097)x*z--&gt;y 0.308(0.117)</td><td>x --&gt;y 0.276(0.080)z --&gt;y 0.444(0.092)x*z--&gt;y 0.332(0.087)</td></tr><tr><td>150</td><td>x --&gt;y 0.145(0.174)z --&gt;y 0.243(0.269)x*z--&gt;y 0.102(0.214)</td><td>x --&gt;y 0.256(0.091)z --&gt;y 0.382(0.143)x*z--&gt;y 0.256(0.120)</td><td>x --&gt;y 0.245(0.086)z --&gt;y 0.397(0.122)x*z--&gt;y 0.242(0.100)</td><td>x --&gt;y 0.261(0.073)z --&gt;y 0.417(0.104)x*z--&gt;y 0.277(0.080)</td><td>x --&gt;y 0.265(0.070)z --&gt;y 0.440(0.085)x*z--&gt;y 0.291(0.078)</td><td>x --&gt;y 0.271(0.070)z --&gt;y 0.448(0.080)x*z--&gt;y 0.298(0.065)</td><td>x --&gt;y 0.280(0.062)z --&gt;y 0.453(0.075)x*z--&gt;y 0.303(0.070)</td></tr><tr><td>200</td><td>x --&gt;y 0.151(0.164)z --&gt;y 0.246(0.263)x*z--&gt;y 0.102(0.211)</td><td>x --&gt;y 0.199(0.120)z --&gt;y 0.328(0.183)x*z--&gt;y 0.176(0.143)</td><td>x --&gt;y 0.243(0.081)z --&gt;y 0.397(0.118)x*z--&gt;y 0.242(0.082)</td><td>x --&gt;y 0.259(0.068)z --&gt;y 0.426(0.092)x*z--&gt;y 0.267(0.063)</td><td>x --&gt;y 0.273(0.072)z --&gt;y 0.432(0.096)x*z--&gt;y 0.300(0.108)</td><td>x --&gt;y 0.275(0.059)z --&gt;y 0.448(0.073)x*z--&gt;y 0.291(0.058)</td><td>x --&gt;y 0.280(0.056)z --&gt;y 0.456(0.067)x*z--&gt;y 0.300(0.049)</td></tr><tr><td>500</td><td>x --&gt;y 0.146(0.160)z --&gt;y 0.246(0..258)x*z--&gt;y 0.098(0.206)</td><td>x --&gt;y 0.198(0.109)z --&gt;y 0.328(0.176)x*z--&gt;y 0.165(0.142)</td><td>x --&gt;y 0.242(0.069)z --&gt;y 0.396(0.110)x*z--&gt;y 0.222(0.087)</td><td>x --&gt;y 0.257(0.057)z --&gt;y 0.424(0.084)x*z--&gt;y 0.248(0.064)</td><td>x --&gt;y 0.268(0.047)z --&gt;y 0.441(0.068)x*z--&gt;y 0.262(0.051)</td><td>x --&gt;y 0.271(0.044)z --&gt;y 0.452(0.058)x*z--&gt;y 0.269(0.048)</td><td>x --&gt;y 0.278(0.041)z --&gt;y 0.458(0.053)x*z--&gt;y 0.277(0.043)</td></tr></table>

Note. x -<sup></sup>y refers to the mean of 500 path estimates from predictor x to criterion y (true score 030; below dashed line denotes significance).  
z -<sup></sup>y refers to the mean of 500 path estimates from the moderator variable z to criterion y (true score 050; below solid line denotes significance).  
x z -<sup></sup>y refers to the mean of the 500 path estimates for the interaction effect of z on the path from x to y (true score 030; below double lines denote significance).  
Significance is denoted through the bolded lines with values below the lines being significant at 0.01. Dashed line is predictor X , solid line is moderator Z, and double line is interaction term X Z.  
<sup>a</sup>Same as single-indicator multiple regression (population standard errors are within parentheses).

## Number of Indicators or Sample Size

In the cells above and to the left of the ideal thresholds identified above, path estimations are well below the true score by at least 15%-20%. In the cells below and to the right of these threshold points in the table, the influence of sample size and number of indicators can be evaluated by the patterns of estimation Increasing the sample size (i.e., estimations further down the columns) does not improve on these estimations and, in fact, can make them worse. For instance, the interaction path estimations for 6 and 8 indicators at a 500 sample size dropped to 0.248 and 0.262, respectively, from 0.261 and 0.304 values at the thresholds. This pattern is generally consistent throughout the other columns as well.

Increasing the number of indicators (i.e., estimations across the rows), however, does improve estimations more consistently. Within a row, each increase in indicators generally produces an increase in the estimation, consistently moving toward or maintaining the true score. Thus, more indicators help estimate the “true” parameter more closely.

## Power

Sample size alone did not appear to help much at uncovering the true parameter for interaction terms, and hence a strategy of gathering more data (i.e., increasing sample size) might not be helpful. Although this was observed in the data, it is important to recognize how sample size and the number of indicators contribute to statistical estimates through power. For a discussion of these influences on power, see Appendix B.<sup>26</sup>

## Inaccurate True Score Estimates

As seen in the literature review, attenuation of the estimates through measurement error is a condition that creates inaccurate true score estimates. This condition exists in the Monte Carlo data and had an effect on single-indicator regression, while only having a slight dampening effect on PLS estimates.

Single-Indicator Regression Biases. <sub>Estimation</sub> <sub>of</sub> the interaction term of X \* Z for the single-indicator regression analysis resulted in estimations around 0.10 (Table 7) when they should be 0.30. Such results could leave the researcher with the impression that an interaction effect is much smaller than its true score, or even that the interaction effect is possibly nonexistent. This interaction term estimation, in particular, would generally represent the worst among the estimations, because the interaction reliability will be necessarily smaller because it is a product of the reliabilities of the predictor and moderator indicators.

PLS Biases. indicator regression, we see that PLS still tends to underestimate the structural paths that connect constructs. At the same time, PLS tends to overestimate the measurement paths connecting constructs to their indicators. Loadings in these results are overestimated as Table 8<sup>27</sup> displays. The true loadings were set in the Monte Carlo analysis at 0.70 for the main-effects constructs of predictor X and moderator Z, and by implication at 0.49 for the interaction construct of X \* Z. If we consider from Table 5 only the loadings for significant estimates, we can see that the loadings in Table 8 tend to be inflated by more than 10% in the two- and four-indicator situation. And, as conjectured by Chin (1995, p. 319), it is not until we use 10 to 12 indicators that a more accurate loading estimate is reached.

Thus, contrasted to other causal modeling techniques (e.g., LISREL), PLS tends to be more conservative in its estimates of theoretical (i.e., structural) paths and more positively biased towards its loading estimates. This implies caution against putting too much emphasis on PLS loadings when there are few indicators (i.e., ≤8). Among the significant estimates, we do see that, on average, the estimates for the interaction construct of X \* Z were closer to the 0.30 true effect than the estimates of predictor X to their true effect of 0.30. Our interaction construct thus had reduced estimation bias. With the initial results of the baseline Monte Carlo study in mind, a short exploration of two further comparisons—summated scales within regression and heterogeneous loadings—are undertaken.

## Summated Regression—with Baseline Data

Using the same Monte Carlo data as in the baseline case, the practice of summing scales was employed for the 2- through 12-indicator cases. Multiple regression was then used to provide significance levels and true-score estimates. Interaction term results from this summated regression are shown in Table 9. These significance results demonstrate patterns more similar to the PLS product-indicator approach patterns than the single-indicator regression patterns (Table 7). However, summated regression still consistently underestimated the true theoretical interaction term scores by more than 10% in 41 of 42 cells. Of the significant results, most are substantially below the correct score.

Table 9 Monte Carlo Path Estimation for Interaction Term X Z Using Summated Regression (500 Runs per Cell) with Means, Population Standard Errors in Parentheses, and t-Stats, Respectively

<table><tr><td></td><td colspan="6">Indicators per construct</td></tr><tr><td>Sample size</td><td>two per construct (4 for interaction) (std. Error) t value</td><td>four per construct (16 for interaction)</td><td>six per construct (36 for interaction)</td><td>eight per construct (64 for interaction)</td><td>ten per construct (100 for interaction)</td><td>twelve per construct (144 for interaction)</td></tr><tr><td>20</td><td>0.146(.290)0.502</td><td>0.205(.259)0.792</td><td>0.232(.236)0.982</td><td>0.229(.248)0.926</td><td>0.240(.237)1.015</td><td>0.243(.231)1.053</td></tr><tr><td>50</td><td>0.151(.210)0.717</td><td>0.210(.159)1.324</td><td>0.216(.150)1.436</td><td>0.238(.145)1.646</td><td>0.242(.144)1.688</td><td>0.268(.130)2.066</td></tr><tr><td>100</td><td>0.150(.180)0.830</td><td>0.212(.130)1.631</td><td>0.233(.112)2.070</td><td>0.249(0.090)2.509</td><td>0.250(.103)2.435</td><td>0.270(.091)2.965</td></tr><tr><td>150</td><td>0.212(.130)1.631</td><td>0.209(.121)1.730</td><td>0.238(.096)2.480</td><td>0.255(.083)3.079</td><td>0.255(.082)3.118</td><td>0.260(.079)3.288</td></tr><tr><td>200</td><td>0.160(.155)1.035</td><td>0.205(.105)2.038</td><td>0.236(.089)2.668</td><td>0.252(.095)2.669</td><td>0.257(.077)3.314</td><td>0.270(.064)4.244</td></tr><tr><td>500</td><td>0.157(.149)1.054</td><td>0.211(.098)2.158</td><td>0.236(.075)3.159</td><td>0.250(.061)4.072</td><td>0.257(.059)4.365</td><td>0.265(.052)5.094</td></tr></table>

Note. True score 030. Significance is denoted through the bolded double lines with values below the lines being significant at 0.01. t 236, P 001, one-tail.

These conclusions are drawn, in part, from the significance levels and estimates shown in Table 9, where double lines denote patterns of significance for summated regression. Any interaction term value below the double line is significant at 0.01. The pattern of significance is somewhat similar to the PLS productindicator approach, but less effective in detection with 8 indicator—100 sample size and 6 indicator—150 sample size cells being identified as ideal points. All values for the 2 and 4 indicators are not significant, and the 6 indicator—100 sample size cell did not emerge as significant as it was in the PLS baseline case.

Beyond the fact that summated regression detects the interaction true score at later points than does PLS, we can also compare the accuracy of both estimates from the true value of 0.30 via the mean rela-<sup>tive</sup> <sup>bias</sup> (MRB). Analogous to the formula provided by Reinartz et al. (2002), the average percentage bias for the <sup>t</sup> = 500 runs from the true population estimate $X _ { p o p }$ of 0.3 can be determined as follows:

$$
M R B = 1 0 0 * \frac {1}{t} \sum_ {i = 1} ^ {t} \frac {X _ {p o p} - X _ {i}}{X _ {p o p}}.
$$

From Figure 4, no summated regression estimate reached the true interaction score of 0.30, and only two cells (12 indicators—200 and 100 sample sizes) came within 10% of that score. Most of the PLS estimates reached the 10% threshold at 6 indicators and were within the 5% range at 8 indicators.<sup>28</sup>

Figure 4 Mean Relative Bias in PLS and Regression Interaction Terms Highlighting the Influence of the Number of Items and Sample Size (0% Represents Zero Bias in the True Score Estimation)  
![](/api/attachments/PJNPTKAY/fulltext/images/cfbf6ff529bd47a24352188de1c01a125100d659f4b93ca4ed67a39dbba0ceeb.jpg)

In contrast to the interaction term results, the ability to detect the direct effects of predictor <sup>X</sup> and moderator <sup>Z</sup> were identical for both summated regression and PLS.<sup>29</sup> For strong effect sizes <sup>Z</sup> = 0 50<sup></sup>, both procedures were able to detect an effect at 4 indicators— 50 sample size. For the moderate effect size <sup>X</sup>  0 30<sup></sup>, more data (sample size  100) or more indicators (4+) was required to obtain significance. But these moderate effect sizes are not consistently estimated (i.e., within 10% of the true score) until eight or more indicators are used. Small sample sizes performed poorly once again until either a large effect size existed <sup>Z</sup> = 0 50<sup></sup> or a large number of indicators were used.

## Summated Regression—with Heterogenous Loadings

To this point in the analysis, the data set created with the Monte Carlo simulation maintained a 0.70 loading pattern, which reflects a typical level found within the IS literature and provided a consistent benchmark for comparing sample size, effect size, and number of indicators. Comparing the summated regression-based technique to the new PLS productindicator approach under varying loading patterns is the objective of the next simulation. The results of this comparison are shown in Table 10.

![](/api/attachments/PJNPTKAY/fulltext/images/71d2e2876953b9455664dcc0679c3f448d1d8c83bbdcbf1b99b69ac1b686bbf7.jpg)

In this analysis, loadings were varied for the independent <sup>X</sup> variable and the moderating <sup>Z</sup> variable. By varying these loadings, conditions of heterogeneous constructs were simulated, reflecting the existence of more and less measurement error among a set of items, as shown in Table 10, first column. The dependent <sup>Y</sup> variable was maintained at 0.70 loadings to simplify the design. Furthermore, based on the previous Monte Carlo results, sample size was set at 100 and the number of indicators kept at either 6 or 8, which was the ideal range in the baseline case balancing both significance and accurate estimation. Average regression scores were calculated for the <sup>X</sup> and <sup>Y</sup> variables by averaging the indicators, respectively, and were calculated for the moderating <sup>Z</sup> variable by multiplying the averaged <sup>X</sup> and <sup>Y</sup> values. Even though scores could have been aggregated through various techniques, this method produced the best regression results.

Monte Carlo Simulation Comparing the Impact of Heterogeneous Loadings on the Interaction Estimate (in Bold) for the PLS Product Indicator Approach and Regression Using Averaged Scores with Population Standard Errors in Parentheses (Sample Size of 100, 500 Runs per Cell, 8 and 6 Indicators)

<table><tr><td></td><td>Factor Loading Patterns for 6 items - pattern repeated for both X and Z  $constructs^a$ </td><td colspan="2">PLS Product Indicator Estimates (Std. Error)</td><td colspan="2">Regression Estimates Using Averaged Scores (Std. Error)</td></tr><tr><td>A1</td><td>2 at .80, 2 at .702 at.60</td><td>x*z--&gt;y 0.285(0.108)</td><td>**</td><td>x*z--&gt;y 0.234(0.112)</td><td>*</td></tr><tr><td>A2</td><td>3 at .803 at .70</td><td>x*z--&gt;y 0.288(0.091)</td><td>**</td><td>x*z--&gt;y 0.246(0.102)</td><td>**</td></tr><tr><td>A3</td><td>3 at .803 at .60</td><td>x*z--&gt;y 0.283(0.112)</td><td>**</td><td>x*z--&gt;y 0.228(0.115)</td><td>*</td></tr><tr><td>A4</td><td>2 at .80, 2 at .602 at .40</td><td>x*z--&gt;y 0.302(0.123)</td><td>**</td><td>x*z--&gt;y 0.218(0.124)</td><td>*</td></tr><tr><td>A5</td><td>3 at .803 at .40</td><td>x*z--&gt;y 0.296(0.123)</td><td>**</td><td>x*z--&gt;y 0.213(0.128)</td><td>*</td></tr><tr><td>A6</td><td>3 at .703 at.60</td><td>x*z--&gt;y 0.280(0.145)</td><td>*</td><td>x*z--&gt;y 0.221(0.124)</td><td>*</td></tr><tr><td>A7</td><td>2 at.70, 2 at .602 at .30</td><td>x*z--&gt;y 0.304(0.129)</td><td>*</td><td>x*z--&gt;y 0.189(0.144)</td><td>*</td></tr></table>

<table><tr><td></td><td>Factor Loading Patterns for 8 items - pattern repeated for both X and Z  $constructs^a$ </td><td colspan="2">PLS Product Indicator Estimates (Std. Error)</td><td colspan="2">Regression Estimates Using Averaged Scores (Std. Error)</td></tr><tr><td>B1</td><td>4 at .80, 2 at .702 at .60</td><td>x*z--&gt; y 0.293(0.121)</td><td>**</td><td>x*z--&gt; y 0.250(0.102)</td><td>**</td></tr><tr><td>B2</td><td>4 at .804 at .70</td><td>x*z--&gt; y 0.297(0.114)</td><td>**</td><td>x*z--&gt; y 0.234(0.109)</td><td>*</td></tr><tr><td>B3</td><td>4 at .804 at .60</td><td>x*z--&gt; y 0.306(0.107)</td><td>**</td><td>x*z--&gt; y 0.251(0.099)</td><td>*</td></tr><tr><td>B4</td><td>4 at .80, 2 at .60,2 at .40</td><td>x*z--&gt; y 0.311(0.112)</td><td>**</td><td>x*z--&gt; y 0.240(0.109)</td><td>*</td></tr><tr><td>B5</td><td>6 at .802 at .40</td><td>x*z--&gt; y 0.318(0.124)</td><td>**</td><td>x*z--&gt; y 0.223(0.118)</td><td>*</td></tr><tr><td>B6</td><td>4 at .704 at .60</td><td>x*z--&gt; y 0.305(0.115)</td><td>**</td><td>x*z--&gt; y 0.234(0.112)</td><td>*</td></tr><tr><td>B7</td><td>4 at .70, 2 at .602 at .30</td><td>x*z--&gt; y 0.314(0.134)</td><td>**</td><td>x*z--&gt; y 0.224(0.118)</td><td>*</td></tr></table>

x z -<sup></sup>y refers to the mean of the 500 path estimates for the interaction effect of z on the path from x to y (true score <sub>=</sub> 030).  
<sup>a</sup>Dependent variable loadings are held at 0.70 to simplify the design.  
∗Significant at 0.05; ∗∗significant at 0.01.

The results in Table 10 show that in all instances of heterogeneous loadings for the eight-indicator situation, the PLS product indicator approach <sup>consistently</sup> estimates the 0.30 true effect of the interaction term (as seen in the bolded values and the MRB values within 5% of the true estimate, Figure 5), and these differences are not statistically significant. The summated regression approach, on the other hand, was both significantly different <sub>and</sub> consistently underestimates <sub>the</sub> 0.30 true effect by 16%–37%. No matter whether loadings vary a little as in the case with 0.80 and 0.70 loading combinations or vary a lot as in the case with 0.70, 0.60, and 0.30 loading combinations, PLS performed well, demonstrating its ability to handle measurement error and produce consistent results. For the six-indicator situation, as expected, the estimates tended to be lower. But again, we see an improvement of using PLS over summated regression. Here the estimates using summated regression ranged from 0.19 to 0.25, while the lowest PLS estimate was at 0.28. As in the homogeneous case, the patterns for the direct effects of predictor <sup>X</sup> and moderator <sup>Z</sup> under the summated regression approach were similar to earlier results.<sup>30</sup> This, then, leads us to conclude that when the reality of varying loadings patterns and lower reliability emerge, PLS is more accurate in its estimates of true scores than is summated regression.

Figure 5 Comparison of PLS and Regression Interaction Terms MRB Under Conditions of Heterogeneous Item Quality (0% Represents Zero Bias in the True Score Estimation)  
![](/api/attachments/PJNPTKAY/fulltext/images/77ad6c79a8985ce4a6a5c01d897d976af009e4cbf1afff0d71cfbae2536b284e.jpg)

![](/api/attachments/PJNPTKAY/fulltext/images/ffe5146f883fcb959119c96231a9eb761d29984748f1031fe62fbac36a08ff19.jpg)

<sup>30</sup> Because of page limitations, these results are not presented but are available from the authors upon request.

## Summary

Taking all the results from sample size, number of indicators, effect size, and reliability into account, a minimum sample size of 150 with 4 indicators or a minimum sample size of 100 with 6 indicators appears best to balance the trade-offs for detection and accurate estimate. Researchers should always strive for the highest reliability possible in their measures. Unfortunately, lower or varied reliability is a reality of research in the IS field, one that is not likely to go away. The PLS product-indicator approach, demonstrated above, provides researchers with a technique that allows them to manage this reality. Variability in individual item reliability did not influence the PLS estimates in our eight-indicator simulation. With these threshold combinations, structural path estimates will be within 10% of the true effects, as shown in Table 7, and the overestimation of the measurement paths will be kept to a minimum, as shown in Table 8.

This conclusion, in combination with our findings in the literature review, may provide a possible explanation for the poor results of the past moderator studies. Recall that, in our literature review, studies examining moderators employed an average sample size of 81.5 and an average number of three indicators. PLS improved on single-indicator measures and summated scales, and handled varying effect sizes, sample sizes, power levels, number of indicators, and reliabilities. Although we cannot conclude from our analysis how other effect sizes, loadings, and reliabilities would fare, these should be tested in the future to get an even greater appraisal of how PLS and summated regression estimates may vary. Smaller sample sizes and fewer indicators using the PLS product-indicator approach would likely be appropriate when using more reliable indicators (i.e., loadings higher than 0.70), but we cannot estimate by how much the estimates would rise.

Now that we have demonstrated through this Monte Carlo analysis that the PLS approach improves on regression-based techniques, the role of the PLS approach within IS theory is explored. Empirical data for the moderating influence of enjoyment on the well-known relationship between perceived usefulness and intention to use is now presented.

## Study 2: The Moderating Effect of Enjoyment on the Perceived Usefulness/IT-Adoption Intention Relationship

This section presents the PLS product-indicator approach as applied to detecting the interaction effect of enjoyment on the perceived usefulness/ITadoption intention relationship. In Davis’ (1989) original presentation of this model, perceived usefulness and perceived ease of use were modeled as having direct effects on adoption intention. Later, Davis et al. (1992) note the difference between extrinsic and intrinsic sources of motivation to computer use in the workplace. While usefulness, an extrinsic source of motivation, had a significant effect on adoption intention, enjoyment, an intrinsic source of motivation defined as the extent to which the activity of using the computer is perceived to be enjoyable in its own right apart from any performance consequences, was felt to also have a direct effect. Their study found that both perceived usefulness and enjoyment mediated the influence of perceived ease of use on intention. Thus, perceived ease of use was not included in predicting intention for this analysis.

The question becomes whether enjoyment also moderates the usefulness to the intention relationship. Consider the following example to illustrate the potential role of enjoyment as a moderator. The TAM model states that the stronger a person's belief in the usefulness of an information technology (IT), the more he/she would intend to use it. Yet, we also believe that the impact of this belief on IT-usage intention is negatively moderated by the level of enjoyment the individual has during his or her use of the IT. In essence, when the usage experience is more enjoyable, the impact of perceived usefulness on future intention to use is lower. Conversely, the less enjoyable one perceives the IT to be, the stronger the impact of one's perception of usefulness on intention to use. This phenomenon is based on a cognitive consistency argument in which the underlying theory is that when IT usage is extremely enjoyable, instrumental issues, such as perceived usefulness, ought not to come into one's decision-making criteria for future usage. In fact, for those people whose predominant purpose is enjoyment, more usefulness may be considered a detrimental feature, thereby negatively impacting intention to use. Thus, all else being equal, if we had two different groups of people in which the first group perceived the IT to be highly enjoyable and the second group perceived it to be highly unenjoyable, we would expect a low to negative correlation between perceived usefulness and IT-usage intention for the first group, and a high correlation for the second group. In this scenario, the dependent variable <sup>Y</sup> <sup></sup> would represent IT-usage intention, and the predictor <sup>X</sup> and moderator <sup>Z</sup> variables would represent perceived usefulness and enjoyment, respectively.

Chin and Gopal (1995) similarly found that both enjoyment and relative advantage (which uses identical items to perceived usefulness) had an effect on group support system adoption intentions. In their article, they state “that there is also the possibility of interaction effects among the constructs that were not taken into account in this study. For example, Davis et al. (1992) indicated that a positive interaction might exist between enjoyment and usefulness. Because of its similarity to usefulness, the relative advantage construct used in this study may also have an interaction effect with enjoyment” (p. 58).

To test the possibility of such an interaction effect, the perceived usefulness and enjoyment items were used to examine the adoption intention of electronic mail. See Appendix $C ^ { 3 1 }$ for construct definition, items used, and organizational setting.

In formulating and testing for interaction effects using PLS, one needs to follow a hierarchical process similar to that used in multiple regression in which one compares the results of two models (i.e., one with and one without the interaction construct) Standardized indicators were chosen for this analysis because Likert scales were employed in this study, and the indicators were considered to be theoretically parallel. The standardizations were calculated using SPSS 9.0. For the analysis with the interaction construct (as depicted in Figure 2), it is necessary to include the two main effects constructs (in this study, perceived usefulness and enjoyment) to assess how the moderator construct, enjoyment, influences the impact of perceived usefulness on intention When using the default standardized output from PLS, the standardized beta estimate of the main construct <sup>X</sup> (perceived usefulness) on dependent construct <sup>Y</sup> (intention) is interpreted as the amount of influence of <sup>X</sup> on <sup>Y</sup> when the moderator construct <sup>Z</sup> (enjoyment) is equal to zero. Likewise, the beta estimate from moderator construct <sup>Z</sup> to <sup>Y</sup> is interpreted as the amount of direct influence of <sup>Z</sup> on <sup>Y</sup> when <sup>X</sup> is equal to zero.

The standardized path estimate from the interaction construct informs us how a change in the level of the moderator construct <sup>Z</sup> (enjoyment) would change the influence of the main construct X (perceived usefulness) on dependent construct <sup>Y</sup> (intention). Thus, if X (perceived usefulness) has an estimated beta effect of B on Y (intention), a beta M from the interaction construct can be interpreted as a beta change to <sup>B</sup> +<sup>M</sup> for the estimated path from X (perceived usefulness)

to <sup>Y</sup> (intention) when <sup>Z</sup> (enjoyment) increases by one standard deviation from the baseline of zero.

You can also compare the squared multiple correlation $( R ^ { 2 } )$ for this interaction model with the squared multiple correlation for the “main effects" model, which excludes the interaction construct. The difference between the squared multiple correlations is used to assess the overall effect size $f ^ { 2 }$ for the interaction where 0.02, 0.15, and 0.35 have been suggested as small, moderate, and large effects, respectively (Cohen 1988).<sup>32</sup> It is important to understand that a small $f ^ { 2 }$ does not necessarily imply an unimportant effect. Even a small interaction effects can be meaningful under extreme moderating conditions, if the resulting beta changes are meaningful, then it is important to take these conditions into account.

The results of this study, as shown in Figure $6 , ^ { 3 3 }$ give a standardized beta of 0.449 from usefulness to intention, 0.227 from enjoyment to intention, and an interaction effect of -0.209 with a total $R ^ { 2 }$ of 0.50. Thus, these results imply that one standard deviation increase in enjoyment will not only impact intention directly by 0.227, but it would also decrease the impact of perceived usefulness to intention from 0.449 to 0.240. As expected, the main effects model, shown in Figure $7 , ^ { 3 4 }$ resulted in a slightly higher standardized beta and a smaller $R ^ { 2 }$ of 0.465. The interaction construct, therefore, has an effect size f of $0 . 0 7 , ^ { 3 5 }$ which is between a small and medium effect and is larger than found in most past IS studies. Even with a small-to-moderate effect size, these beta estimates help inform us of the conditions under which enjoyment becomes a dominant factor—equaling and potentially overshadowing perceived usefulness. For the group of people who perceive electronic mail to be extremely enjoyable, perceived usefulness will be a less important factor on usage intention than is enjoyment. If there is a reasonable likelihood of encountering such a group, being aware of this interaction becomes important.

To assess whether the interaction effect and main effects were significant, a bootstrap resampling procedure (Efron and Tibshirani 1993) was performed. The results of 500 resamples indicate that all paths, weights and loadings, (as shown in Table 11) were significant at the 0.01 level.36

The accuracy of the path estimates to the true effects must be assessed next. As noted earlier, the estimates of the structural paths tend to be more accurate as the reliability score for the estimated construct increases. To assess the reliability of the latent variable estimated by PLS, the composite reliabilities as suggested by Werts et al. (1974) were calculated and are presented in Table 11. Use of this formula, which does not assume equal loadings or error terms among the measures, typically provides more accurate estimates of the composite reliability. Overall, except for enjoyment with a three-indicator composite reliability of 0.85, the composite reliabilities of the other constructs are very high—at or above 0.96. In the case of enjoyment, if we employ the composite reliability as a bias correction factor, the 0.227 path between enjoyment and intention increases slightly to 0.246.

As a contrast, we summed the indicators and performed a moderated regression analysis instead. The result was a smaller interaction path of 0 140 $( p < 0 . 0 5 )$ with a correspondingly smaller $R ^ { 2 }$ of 0.422. Furthermore, the effect could not be considered significant at the 0.01 level. With the main effects $R ^ { 2 }$ of 0.404, this yields a substantially lower change in $R ^ { 2 }$ of 0.018 and an $f ^ { 2 }$ of 0.03. Contrast these numbers with those obtained using PLS (path of −0 209 with p < $f ^ { 2 }$ of 0.07) and we see the theoretically weighted scales of PLS outperformed the summated scales by more than a factor of two. Thus, without the PLS procedure, we would not be able to conclusively prove that enjoyment, an intrinsic motivation to use a computer, represents a significant and substantive moderating effect in the TAM model.

## Discussion and Conclusion

This paper provided a new approach towards the assessment of interaction effects among continuous variables. IS research over the past 15 years has predominantly employed multiple regressionand ANOVA-based analytic techniques to investigate these interaction terms. Less than one-quarter of the interaction terms investigated in these works have been found to be significant, with only a handful of the articles providing an effect size estimate. As suggested, these cumulative results may be due to the analytic technique employed—specifically, multiple regression where this technique was demonstrated through the Monte Carlo simulation to often underestimate the moderator effect size by 16%-37%, depending on the number of indicators used.

As Cronbach (1987, p. 417) has urged, "further investigation of statistical power in studies of interaction and invention of more sensitive research strategies are much to be desired.” Following this sentiment, this study has provided an initial sense of the efficiency and effectiveness of a new PLS product-indicator approach. Through the use of the new approach, it has been shown that sample sizes of approximately 100 with eight indicators per main effect construct, and loadings of 0.70 are needed to detect an interaction effect and to yield reasonably consistent estimates. The combination of 150 sample size, 6 indicators, and 0.70 loadings also produced similar, significant results. In contrast, the average sample size and number of indicators in past IS studies were 81.5 and 3, respectively, much lower than the standards suggested by the Monte Carlo simulation. Increasing the number of indicators was shown to have a larger impact on consistent estimations than did increasing the sample size. Increasing the reliability of indicators will also help, but this typically emerges only after several attempts are made at building better questions and more unidimensional constructs.

It is important to understand that these suggested levels pertain only to detecting interaction effects. By virtue of the fact that product indicators are multiplicatively less reliable than their respective indicators, the recommended sample size and indicator levels will always be larger than models with only direct effects. The heuristics for sample size and indicators using PLS typically make assumptions that the loadings of indicators are 0.70 or higher. In the case of modeling interaction effects, we must increase these requirements.

Several additional findings around known PLS biases, influences of different reliabilities, extensions for nonlinear indicators, and use of formative indicators are possible from these results. Appendix D<sup>37</sup> provides a more complete technical discussion of these insights.

Finally, it is important to highlight the results of the Monte Carlo simulation with heterogeneous loadings. It is typically the case that measures used in research can vary in the amount of measurement error. PLS is well suited for use in this situation because its primary objective is to differentially weight a set of items to produce the best predictive construct scores. While summated regression would, by default, treat all measures identically, our PLS product-indicator results demonstrate that discounting poor interaction terms can yield better overall estimates. However, the ability to sort through the poor performing items as they are applied within a particular predictive model is equally important. While not presented here because of page limitations, the PLS results via the loading estimates can help a researcher determine which items are of good quality and which need further improvement for future studies.

In summary, the new PLS product-indicator approach seems to yield promising results for researchers interested in assessing interaction effects. The Monte Carlo exercise demonstrated that single-indicator regression was inadequate for assessing interaction terms and that summated regression, while performing better, still underestimated the correct values by substantial margins. In particular, under conditions of heterogenous loadings where the individual item reliabilities varied, the PLS product-indicator approach came to the fore in retrieving the “true" population parameter, whereas regression resulted in at least a 16% underestimation. In estimating noninteraction terms that have higher reliabilities, summated regression and PLS performed equally well.

Study 2, which evaluated the PLS approach using an IS empirical data set on enjoyment and use intention again found that the PLS approach retrieved an interaction estimate 33% higher than the summated regression approach. While not as conclusive as the simulation, the effect size was found to be higher than in previous IS studies and twice the size estimated in the summated regression.

In all, it is hoped that the issues raised in this paper—such as appropriate sample size, multiple indicators, reliability, and power—will be part of the mindset and standard information provided in future research papers. Attention to these issues in future research should help the IS field build a cumulative body of knowledge with fewer problems than that found through the literature review. As stated at the start of the paper, it indeed might be the case that theoretical advancement of moderators has been impaired more by analytical techniques than by the lack of conceptualizing contingent factors. We believe that moderators’ roles within emerging theories are poised to have large effects on the field, if only we can improve on the analytical techniques to aid in this discovery.

## Acknowledgments

This research was supported in part by a grant from the Social Sciences and Humanities Research Council of Canada whose assistance is gratefully acknowledged. The authors also wish to thank Theodora Lo for her assistance in the literature review and earlier simulation runs. An earlier version of this paper was presented at the 1996 International Conference on Information Systems.

## References

Anderson, J. C., D. W. Gerbing. 1988. Structural equation modeling in practice: A review and recommended two-step approach. Psych. Bull. 103 <sub>411–423.</sub>

Ang, S., L. L. Cummings, D. W. Straub, E. P. Christopher. 1993. The effects of information technology and the perceived mood of the feedback giver on feedback seeking. <sup>Inform.</sup> <sup>Systems</sup> <sup>Res.</sup> 4(3) 240–261.

Anson, R., R. Bostrom, W. Bayard. 1995. An experiment assessing group support system and facilitator effects on meeting out-Management Sci. 41

<sub>Aiken,</sub> <sub>L.</sub> <sub>S.,</sub> <sub>S.</sub> <sub>G.</sub> <sub>West.</sub> <sub>1991.</sub> Multiple Regression: Testing and Inter-<sup>preting</sup> <sup>Interactions</sup>. Sage Publications, Newbury Park, CA.

Aubert, B. A., S. Rivard, M. Patry. 1994. Development of measures to assess dimensions of IS operation transactions. J. I. DeGross, Proc. 15th Internat. Conf. Inform. Systems. Vancouver, British Columbia, 13–26.

Bell, J. 1984. The effect of presentation form on the use of information in annual reports. <sup>Management</sup> <sup>Sci.</sup> <sup>30</sup>(2) 169–185.

Bentler, P. M., C. P. Chou. 1988. Practical issues in structural mod-<sub>eling.</sub> <sub>J.</sub> <sub>S.</sub> <sub>Long,</sub> <sub>ed.</sub> Common Problems/Proper Solutions, Avoiding Error in Quantitative Research Park, CA, 161–192.

Bergeron, F., L. Raymond, S. Rivard. 2001. Fit in strategic information technology management research: An empirical comparison of perspectives. OMEGA 29 125–142.

Structural Equation Models with Latent Variables. Wiley, New York.

, P. Paxton. 1998. Interaction of latent variables in structural Structural Equation Modeling 5

Bostrom, R. P., L. Olfman, M. K. Sein. 1990. The importance of learning style in end-user training. <sup>MIS</sup> <sup>Quart.</sup> 101–119.

Brown, C. V., R. P. Bostrom. 1994. Organization designs for the management of end-user computing: Reexamining the contin-J. Management Inform. Systems 20

Busemeyer, J. R., L. E. Jones. 1983. Analysis of multiplicative combination rules when the causal variables are measured with Psych. Bull. 93

<sub>Carmines,</sub> <sub>E.</sub> <sub>G.,</sub> <sub>R.</sub> <sub>A.</sub> <sub>Zeller.</sub> <sub>1979.</sub> Reliability and Validity Assessment<sub>.</sub> Sage University Paper Series on Quantitative Applications in the Social Science, Series no. 07-017. Sage Publications, Beverly Hills, CA.

Cavaye, A. L. M. 1995. User participation in system development Inform. Management 29

Chan, H. C., B. C. Y. Tan, K. W. Wei. 1994. The query cube: A framework for assessing user productivity with database infor-Proc. 15th Internat. Conf. Inform. Systems couver, British Columbia, Canada.

Chan, Y. E., S. L. Huff, D. W. Barclay, D. G. Copeland. 1997. Business strategic orientation, information systems strategic orientation, Inform. Systems Res. 8

Chidambaram, L., B. Jones. 1993. Impact of communication medium and computer support on group perceptions and performance: A comparison of face-to-face and dispersed meet-MIS Quart. 17

Chin, W. Y. W. 1995. PLS is to LISREL as principal components analysis is to common factor analysis. <sup>Tech.</sup> <sup>Stud.</sup> <sup>2</sup> 315–319.

. 1998a. Issues and opinion on structural equation modeling. MIS Quart. 22

. 1998b. The partial least squares approach for structural equa-Modern Methods for <sup>Business</sup> <sup>Research</sup>. Lawrence Erlbaum Associates, Mahwah, NJ, 295-336.

. 2001. PLS-Graph Manual, Version 3.0, Unpublished.

, A. Gopal. 1995. Adoption intention in GSS: Importance of Data Base Adv. 26

, B. L. Marcolin. 1995. The holistic approach to construct validation in IS research: Examples of the interplay between the-<sub>ory</sub> <sub>and</sub> <sub>measurement.</sub> Admin. Sci. Assoc. Canada—23rd Conf., <sup>IS</sup> <sup>Proc.</sup>, Vol. 16. Windsor, Ontario, Canada.

, P. R. Newsted. 1999. Structural equation modeling analysis with small samples using partial least squares. Rick Hoyle, ed. Statistical Strategies for Small Sample Research<sub>.</sub> <sub>Sage</sub> <sub>Publications,</sub> Thousand Oaks, CA, 307–341.

Chou, C., P. M. Bentler, A. Satorra. 1991. Scaled test statistics and robust standard errors for non-normal data in covariance structure analysis: A Monte Carlo study. <sup>British</sup> <sup>J.</sup> <sup>Math.</sup> <sup>Statist.</sup> Psych. 44

Chung, W. Y., S. Iacono. 1994. Use of advanced features and perceptions of software quality: An experimental study. <sup>Twenty-</sup> Seventh Hawaii Internat. Conf. System Sci. <sub>Hawaii.</sub>

<sub>Cohen,</sub> <sub>J.</sub> <sub>1988.</sub> Statistical Power Analysis for the Behavioral Sciences<sub>,</sub> 2nd ed. Lawrence Erlbaum, Hillsdale, NJ.

<sub>,</sub> <sub>P.</sub> <sub>Cohen.</sub> <sub>1983.</sub> Applied Multiple Regression/Correlation Analysis for the Behavioral Sciences, 2nd ed. Lawrence Erlbaum Associates, Hillsdale, NJ.

Compeau, D. R., C. A. Higgins. 1995. Application of social cognitive theory to training for computer skills. <sup>Inform.</sup> <sup>Systems</sup> <sup>Res.</sup> <sup>6</sup> 118–143.

Cook, G. J. 1993. An empirical investigation of information search strategies with implications for decision support system Decision Sci. 24

Cronbach, L. J. 1987. Statistical tests for moderator variables: Flaws in analyses recently proposed. <sup>Psych.</sup> <sup>Bull.</sup> <sup>102</sup> 414–417.

Crossland, M. D., B. E. Wynne. 1994. Measuring and testing the effectiveness of a spatial decision support system. <sup>Twenty-</sup> Seventh Hawaii Internat. Conf. System Sci. <sub>Hawaii,</sub> <sub>IEEE</sub> <sub>Com-</sub> puter Society Press, Los Aamitos, CA.

, J. N. Scudder, R. T. Herschel, B. E. Wynne. 1993. Measuring the relationships of task and cognitive style factors and their effects on individual decision-making effectiveness using a geographic information system. <sup>Twenty-Sixth</sup> <sup>Hawaii</sup> <sup>Internat.</sup> <sup>Conf.</sup> <sup>System</sup> <sup>Sci.</sup> IEEE Computer Society Press, Los Alamitos, CA.

Culnan, M. J. 1987. Mapping the intellectual structure of MIS, 1980–1985: A co-citation analysis. <sup>MIS</sup> <sup>Quart.</sup> <sup>11</sup>(3) 340–353.

Davis, F. D. 1989. Perceived usefulness, perceived ease of use, and user acceptance of information technology. <sup>MIS</sup> <sup>Quart.</sup> <sup>13</sup> 319–340.

, R. P. Bagozzi, P. R. Warshaw. 1992. Extrinsic and intrinsic motivation to use computers in the workplace. <sup>J.</sup> <sup>Appl.</sup> <sup>Soc.</sup> <sup>Psych.</sup> <sup>22</sup> 1111–1132.

Davis, S. A., R. P. Bostrom. 1993. Training end users: An experimental investigation of the roles of the computer interface and training methods. <sup>MIS</sup> <sup>Quart.</sup> <sup>17</sup>(1) 61–85.

DeSanctis, G., M. D'Onofrio, V. Sambamurthy, M. S. Poole 1989. Comprehensiveness and restrictiveness in group decision

heuristics: Effects of computer support on consensus decision <sub>making.</sub> The Proc. Internat. Conf. Inform. System<sub>.</sub> <sub>Boston,</sub> <sub>MA,</sub> 131-140.

Dickson, G. W., G. DeSanctis, D. J. McBride. 1986. Understanding the effectiveness of computer graphics for decision support: A cumulative experimental report. <sup>Comm.</sup> <sup>ACM</sup> <sup>29</sup>(1) 40–47.

, J.-E. L. Partridge, L. H. Robinson. 1993. Exploring modes of facilitative support for GDSS technology. <sup>MIS</sup> <sup>Quart.</sup> <sup>17</sup>(2) 173–194.

Doll, W. J., G. Torkzadeh. 1989. A discrepancy model of end-user computing involvement. <sup>Management</sup> <sup>Sci.</sup> <sup>35</sup>(10) 1151–1171.

. 1991. The measurement of end-user computing satisfaction: Theoretical and methodological issues. MIS Quart. (March) 5–10.

Duxbury, L. E., C. A. Higgins, S. Mills. 1992. After-hours telecommuting and work-family conflict: A comparative analysis. Inform. Sys. Res. 3

Eckel, N. 1987. The interaction between the relative accuracy of probabilistic vs. deterministic predictions and the level of prediction-task difficulty. <sup>Decision</sup> <sup>Sci.</sup> <sup>18</sup>(2) 206–217.

Efron, B., R. J. Tibshirani. 1993. <sup>An</sup> <sup>Introduction</sup> <sup>to</sup> <sup>the</sup> <sup>Bootstrap</sup> (Monographs on Statistics and Applied Probability, #57). Chapman & Hall, New York.

Fedorowicz, J., E. Oz, P. D. Berger. 1992. A learning curve analysis of expert system use. <sup>Decision</sup> <sup>Sci.</sup> <sup>23</sup>(4) 797–818.

Fornell, C., F. L. Bookstein. 1982. Two structural equation models: LISREL and PLS applied to consumer exit-voice theory. <sup>J.</sup> <sup>Mar-</sup> keting Res. 19 <sub>440–452.</sub>

, Y. Yi. 1992. Assumption of the two-step approach to latent variable modeling. Sociological Methods Res. 20 291–320.

, P. Lorange, J. Roos. 1990. The cooperative venture formation process: A latent variable structural modeling approach. <sup>Man-</sup> agement Sci. 36 <sub>1246–1255.</sub>

Franz, C. R. 1979. Contingency factors affecting the user involvement role in the design of successful information systems. Unpublished Ph.D. dissertation, University of Nebraska, Lincoln, NE.

Gelderman, M. 1998. The relation between user satisfaction, usage of information systems and performance. <sup>Inform.</sup> <sup>Management</sup> 34 11-18.

George, J. F., G. K. Eason, J. F. Nunamaker, Jr., G. B. Northcraft. 1990. A study of collaborative group work with and without computer-based support. <sup>Inform.</sup> <sup>Systems</sup> <sup>Res.</sup> <sup>1</sup>(4) 394–415.

Ginzberg, M. J. 1979. A study of the implementation process. <sup>TIMS</sup> Stud. Management Sci. 13 <sub>85–102.</sub>

Goodhue, D. 1986. IS attitudes: Toward theoretical and definition <sub>clarity.</sub> Proc. Internat. Conf. Inform. Systems<sub>,</sub> <sub>December</sub> <sub>15–17.</sub> San Diego, CA, 181–194.

, R. L. Thompson. 1995. Task-technology fit and individual MIS Quart. 19

Goslar, M. D., G. I. Green, T. H. Hughes. 1986. Decision support systems: An empirical assessment for decision making. <sup>Decision</sup> Sci. 17

Greenwald, A. G., A. R. Pratkanis, M. R. Leippe, M. H. Baumgardner. 1986. Under what conditions does theory obstruct research Psych. Rev. 93

Hale, D. P., G. M. Kasper. 1989. The effect of human-computer interchange protocol on decision performance. <sup>J.</sup> <sup>Management</sup> Inform. Systems 6<sub>(1)</sub> <sub>5–20.</sub>

Hartwick, J., H. Barki. 1994. Explaining the role of user participation in information systems use. <sup>Management</sup> <sup>Sci.</sup> <sup>40</sup> 440–465.

Hiltz, S. R., K. Johnson, M. Turoff. 1991. Group decision support: The effects of designated human leaders and statistical feedback in computerized conferences. <sup>J.</sup> <sup>Management</sup> <sup>Inform.</sup> Systems 8

Hughes, C. T., M. L. Gibson. 1991. Students as surrogates for managers in a decision-making environment: An experimental <sub>study.</sub> J. Management Inform. Systems 8<sub>(2)</sub> <sub>153–166.</sub>

Igbaria, M., J. J. Baroudi. 1993. A short-form measure of career orientations: A psychometric evaluation. <sup>J.</sup> <sup>Management</sup> <sup>Inform.</sup> Systems 10

. 1995. The impact of job performance evaluations on career advancement prospects: An examination of gender differences in the IS workplace. MIS Quart. 19(1) 107–123.

Ives, B., M. H. Olson. 1984. User involvement and MIS success: A review of research. <sup>Management</sup> <sup>Sci.</sup> <sup>30</sup>(5) 589–603.

Jaccard, J., R. Turrisi, C. K. Wan. 1990. <sup>Interaction</sup> <sup>Effects</sup> <sup>In</sup> <sup>Multiple</sup> <sup>Regression.</sup> Sage University Paper Series on Quantitative Applications in the Social Sciences, Series #07-072. Sage Publications, Newbury Park, CA.

Jacobs, S. M., R. T. Keim. 1988. An experimental study in overcoming hypothesis-confirming search strategies in computerized <sub>information</sub> <sub>retrieval</sub> <sub>systems.</sub> Proc. Internat. Conf. Inform. Sys-<sup>tems</sup>. Minneapolis, MN, 81–89.

Jarvenpaa, S. L., J. J. Machesky. 1986. End user learning behavior in data analysis and data modeling tools. <sup>Internat.</sup> <sup>Conf.</sup> <sup>Inform.</sup> <sup>Systems</sup>. San Diego, CA.

, V. S. Rao, G. P. Huber. 1988. Computer support for meetings of groups working on unstructured problems: A field experi-MIS Quart. 12

Jones, W. J., R. J. McLeod. 1986. The structure of executive information systems: An exploratory analysis. Decision Sci. 17 220–249.

Jöreskog, K. G., D. Sorbom. 1993. <sup>PRELIS</sup> <sup>2</sup> <sup>User’s</sup> <sup>Reference</sup> <sup>Guide</sup>. Scientific Software International, Lincolnwood, IL.

<sub>,</sub> <sub>H.</sub> <sub>Wold.</sub> <sub>1982.</sub> Systems Under Indirect Observation—Causality <sup>Structure</sup> <sup>Prediction</sup>. North-Holland Publishing Company, Amsterdam, The Netherlands.

, F. Yang. 1996. Nonlinear structural equation models: The Kenny-Judd model with interaction effect. G. A. Marcoulides, <sub>R.</sub> <sub>E.</sub> <sub>Schumacker,</sub> <sub>eds.</sub> Advanced Structural Equation Modeling, <sup>Issues</sup> <sup>and</sup> <sup>Techniques</sup>. Lawrence Erlbaum Associates, Mahway, NJ, 57–88.

Kasper, G. M., R. P. Cerveny. 1985. A laboratory study of user characteristics and decision-making performance in end-user com-Inform. Management 9

Keil, M., R. Mixon, T. Saarinen, V. Tuunainen. 1994–95. Understanding runaway information technology projects: Results from

an international research program based on escalation theory. J. Management Inform. Systems 11<sub>(3)</sub> <sub>65–85.</sub>

Kenny, D. A., C. M. Judd. 1984. Estimating the nonlinear and inter-Psych. Bull. 96

Kim, K. K., N. S. Umanath. 1992–1993. Structure and perceived effectiveness of software development subunits: A task contin-<sub>gency</sub> <sub>analysis.</sub> J. Management Inform. Systems 9<sub>(3)</sub> <sub>157–181.</sub>

Kwon, T. H. 1990. A diffusion of innovation approach to MIS infusion: Conceptualization, methodology, and management <sub>strategies.</sub> Proc. Internat. Conf. Inform. Systems<sub>.</sub> <sub>Copenhagen,</sub> Denmark, 139–147.

Li, F., P. Harmer, T. E. Duncan, S. C. Duncan, A. Acock, S. Boles 1998. Approaches to testing interaction effects using structural equation modeling methodology. <sup>Multivariate</sup> <sup>Behavioral</sup> <sup>Res.</sup> <sup>33</sup>(1) 1–39.

<sub>Lohmöller,</sub> <sub>J.-B.</sub> <sub>1984.</sub> LVPLS Program Manual: Latent Variables Path Analysis with Partial Least-Squares Estimation<sub>.</sub> <sub>Zentralarchiv</sub> <sub>für</sub> empirische Sozialforschung, Köln, Germany.

<sub>.</sub> <sub>1989.</sub> Latent Variable Path Modeling with Partial Least Squares<sub>.</sub> Physica-Verlag, Heidelberg, Germany.

Lohse, G. L., E. J. Johnson. 1996. A comparison of two process Twenty-Ninth Hawaii Internat. Conf. System Sci.

Mackay, J. M., S. H. Barr, M. G. Kletke. 1992. An empirical investigation of the effects of decision aids on problem-solving processes. <sup>Decision</sup> <sup>Sci.</sup> <sup>23</sup>(1) 648–672.

McClelland, G. H., C. M. Judd. 1993. Statistical difficulties of detect-Psych. Bull. 114

McKeen, J. D., T. Guimaraes, J. C. Wetherbe. 1994. The relationship between user participation and user satisfaction: An investigation of four contingency factors. <sup>MIS</sup> <sup>Quart.</sup> <sup>18</sup> 427–451.

Mookerjee, V. S., B. L. Dos Santos. 1993. Inductive expert system design: Maximizing system value. <sup>Inform.</sup> <sup>Systems</sup> <sup>Res.</sup> <sup>4</sup>(2) 111–140.

, M. V. Mannino, R. Gilson. 1995. Improving the performance stability of inductive expert systems under input noise. <sup>Inform.</sup> Systems Res. 6

Motiwall, J., F. Y. K. Pheng. 1982. Decision effectiveness and information use: Effects of cognitive style, complexity, and stress. Proc. Internat. Conf. Inform. Systems Arbor, MI, 137–151.

Computer Intensive Methods for Testing Hypothe-<sup>ses,</sup> <sup>An</sup> <sup>Introduction</sup>. John Wiley & Sons, New York.

Nunamaker, J. F., Jr., A. R. Dennis, J. S. Valacich, D. R. Vogel. 1991. Information technology for negotiation groups: Generat-Management Sci. 37

Nutt, P. C. 1986. Evaluating MIS design principles. <sup>MIS</sup> <sup>Quart.</sup> 139-155.

Olfman, L., M. K. Sein, R. P. Bostrom. 1989. EUC training: Comparison of methods and the role of individual differences. Proc. 22nd Annual Hawaii Internat. Conf. System Sci

Ping, J. R. A. 1995. A parsimonious estimating technique for interaction and quadratic latent variables. <sup>J.</sup> <sup>Marketing</sup> <sup>Res.</sup> <sup>32</sup> 336–347.

. 1996. Latent variable interaction and quadratic effect estimation: A two-step technique using structural equation analysis. Psych. Bull. 119

Powers, R. F., G. W. Dickson. 1973. MIS project management: Myths, opinions, and reality. California Management Rev. 15 147-156.

Premkumar, G., W. R. King. 1994. The evaluation of strategic information system planning. <sup>Inform.</sup> <sup>Management</sup> <sup>26</sup> 327–340.

Reinartz, W. J., R. Echambadi, W. W. Chin. 2002. Generating nonnormal data for simulation of structural equation models using Multivariate Behavioral Res. 37

Sambamurthy, V., G. DeSanctis. 1990. An experimental evaluation of GDSS effects on group performance during stakeholder <sub>analysis.</sub> Proc. 23rd Annual Hawaii Internat. Conf. System Sci<sub>.</sub> IEEE Computer Society Press, Hawaii.

, R. Zmud. 1999. Arrangements for information technology governance: A theory of multiple contingencies. <sup>MIS</sup> <sup>Quart.</sup> <sup>23</sup>(2) 261–290.

Santhanam, R., M. K. Sein. 1994. Improving end-user proficiency: Effects of conceptual training and nature of interaction. <sup>Inform.</sup> Systems Res. 5

Schonberger, R. J. 1980. MIS design: A contingency approach. <sup>MIS</sup> Quart. 4 <sub>13–20.</sub>

Sengupta, K., D. Te’eni. 1993. Cognitive feedback in GDSS: Improving control and convergence. <sup>MIS</sup> <sup>Quart.</sup> <sup>17</sup>(1) 87–113.

Sharma, S., S. Durvasula, W. R. Dillon. 1989. Some results on the behavior of alternate covariance structure estimation proce-J. Marketing Res. XXVI

Smith, K. W., M. S. Sasaki. 1979. Decreasing multicollinearity: A method for models with multiplicative functions. <sup>Sociological</sup> Methods Res. 8

Stone, E. F. 1988. Moderator variables in research: A review and analysis of conceptual and methodological issues. <sup>Res.</sup> <sup>Personal</sup> and Human Resources Management 6 <sub>191–229.</sub>

Suh, K. S., A. M. Jenkins. 1992. A comparison of linear keyword and restricted natural language data base interfaces for novice Inform. Systems Res. 3

Tabachnick, B. G., L. S. Fidell. 1989. <sup>Using</sup> <sup>Multivariate</sup> <sup>Statistics</sup>, 2nd ed. Harper and Row, New York.

Tait, P., I. Vessey. 1988. The effect of user involvement on system success: A continency approach. <sup>MIS</sup> <sup>Quart.</sup> (March) 90–107.

Tan, B. C. Y., K. K. Wei, R. T. Watson. 1993. Dampening status influence using a group support system: An empirical study. <sup>Proc.</sup> Internat. Conf. Inform. Systems

Taylor, S., P. A. Todd. 1995. Understanding information technology usage: A test of competing models. <sup>Inform.</sup> <sup>Systems</sup> <sup>Res.</sup> <sup>6</sup>(2) 144-176.

Todd, P., I. Benbasat. 1991. An experimental investigation of the impact of computer based decision aids on decision making strategies. <sup>Inform.</sup> <sup>Systems</sup> <sup>Res.</sup> <sup>2</sup>(2) 87–115.

. 1992. The use of information in decision making: An experimental investigation of the impact of computer-based MIS Quart. 16

Trice, A. W., M. E. Treacy. 1986. Utilization as a dependent variable <sub>in</sub> <sub>MIS</sub> <sub>research.</sub> Proc. Internat. Conf. Inform. Systems<sub>,</sub> <sub>December</sub> 15–17. San Diego, CA, 227–239.

Umanath, N. S., R. W. Scamell, R. D. Sidhartha. 1990. An examination of two screen/report design variables in an information <sub>recall</sub> <sub>context.</sub> J. Management Inform. Systems 21<sub>(1)</sub> <sub>216–241.</sub>

Vogel, D., J. Lehman, G. Dickson. 1986. The impact of graphical displays on persuasion: An empirical study. <sup>Internat.</sup> <sup>Conf.</sup> <sup>Inform.</sup> Systems

Watson, R. T., T. H. Ho, K. S. Raman. 1994. A fourth dimension of Comm. ACM 37

Weill, P., M. H. Olson. 1989. An assessment of the contingency theory of management information systems. <sup>J.</sup> <sup>Management</sup> <sup>Inform.</sup> Systems 6 <sub>59–85.</sub>

Werts, C. E., R. L. Linn, K. G. Jöreskog. 1974. Intraclass reliability estimates: Testing structural assumptions. <sup>Educational</sup> <sup>Psych.</sup> Measurement 34

Wilson, E. V., T. B. A. Addo. 1994. The joint effects of interac-

tions between data display and task variables on task perfor-Internat. Conf. Inform. Systems Columbia, Canada.

Wold, H. 1982. Soft modeling—The basic design and some extensions. K. Jöreskog, H. Wold, eds. <sup>Systems</sup> <sup>Under</sup> <sup>Indirect</sup> <sup>Obser-</sup> vation II. North-Holland Press, Amsterdam, The Netherlands, 1-53.

. 1985. Partial least squares. S. Kotz, N. L. Johnson, eds. Encyclopedia of Statistical Sciences<sub>,</sub> <sub>Vol.</sub> <sub>6.</sub> <sub>Wiley,</sub> <sub>New</sub> <sub>York,</sub> 581–591.

. 1989. Introduction to the second generation of multivariate analysis. H. Wold, ed. <sup>Theoretical</sup> <sup>Empiricism</sup>. Paragon House, New York, vii-xi.

Wood, J. G., J. T. Nosek. 1994. Discrimination of structure and technology in a group support system: The role of process complexity. <sup>Internat.</sup> <sup>Conf.</sup> <sup>Inform.</sup> <sup>Systems</sup>. Vancouver, British Columbia, Canada

## ISR June 2003, Volume 14#2, Supplemental Material

## Literature Review Summary:

Of the 8110 published articles over the 15-year period for the journals<sup>1</sup> we reviewed, 74 articles contained moderator variables, as summarized in Tables 1, 2 and 3 and as graphed in Figure 1. These articles represent an estimated 6 percent of all experimental and survey research. See below for an explanation.

Figure 1. Number of moderator based IS studies and moderators examined over time.  
![](/api/attachments/PJNPTKAY/fulltext/images/393f00da679ba1d2feac388c9fae84554ca90f1d1482ff65b510082a4db582c6.jpg)

## Moderators Employed Summary:

Number of articles employing moderators is likely underestimated since we followed a very strict definition of moderation, that being theoretical development that fully conceived the moderator as an interaction term and then analyzed this interaction term within the empirical testing. Although many believe in the importance of moderators, they do not adhere to these same criteria. Some conceive variables as moderators, either explicitly or implicitly, but never test them empirically as an interaction term, just as an independent variable (e.g., the extensive work on contingency theory). Some never empirically test the moderators at all, choosing to put forth a theoretical model that adds to an ever-growing list (See Table 1: Other Techniques). Nevertheless, such articles emphasize that moderating influences are important to the IS field regardless of how the concept is described or labeled.

The 6 percent is estimated from the 74 articles that had empirically tested moderators divided by the approximate 1200 articles employing experimental and survey methods. The 1200 article count is determined from the following calculation: 3000 articles pertaining to IS topics exist in the journals we reviewed (8110 articles in total, but approximately 5000 were about Finance, Marketing and other field’s topics). Articles were excluded from the outlets of Management Science, CACM and HICSS when they dealt with topics unrelated to IS issues. Furthermore, Farhoomand (1987) indicated that survey and experimental work accounted for about 30% of the research strategies employed from 1977 to 1985, and Teng and Galletta (1990) confirmed this trend citing their findings that nearly 50% of all projects underway at the time involved survey or experimental approaches. Averaging these figures, 40% or 1200 articles of the published works in the period we reviewed was used to represent the possible empirical results.

<table><tr><td></td><td>Regression Based Techniques</td><td>ANOVA Based Techniques</td><td>Other  $Techniques^a$ </td><td>Total</td></tr><tr><td>Total Articles</td><td></td><td></td><td></td><td>8110</td></tr><tr><td>Articles with Moderators</td><td>7(10%)</td><td>48(64.9%)</td><td>19(25.7%)</td><td>74(100%)</td></tr><tr><td>Total Moderators Found</td><td>22</td><td>267</td><td>N/A</td><td>289</td></tr><tr><td>Number of Significant Moderators (.05 or .01)</td><td>12</td><td>56</td><td>N/A</td><td>68</td></tr><tr><td>Average Sample Size</td><td>81.5</td><td>148</td><td>N/A</td><td></td></tr><tr><td>Average Beta Estimate</td><td>.10</td><td>N/A</td><td>N/A</td><td></td></tr></table>

<sup>a</sup> Other includes theoretical work, meta-analysis, other mathematical techniques, correlation analysis, case analysis and one PLS analysis with un-interpretable results. See details in Tables 2 and 3 below. Table 1. Summary of Literature Review.

<table><tr><td>Study Number and Authors</td><td>Sample Size</td><td>Power Discussed</td><td>Average Number of Indicators</td><td>Number of significant  $moderators^a$ </td><td>Change in R-square</td><td>Effect Size (f2)</td></tr><tr><td>1 Dickson, Partridge &amp; Robinson, 1993</td><td>36</td><td>no</td><td>n/a</td><td>0/1</td><td>n.s.</td><td>n.s.</td></tr><tr><td>2 Kim &amp; Umanath, 1993</td><td>30</td><td>no</td><td>5</td><td>3/4</td><td>No individual tests provided for each interaction term</td><td>Not available</td></tr><tr><td>3 Kwon, 1990</td><td>30/27</td><td>no</td><td>n/a</td><td>2/4</td><td>Split sample – N/A</td><td>Not available</td></tr><tr><td>4 Premkumar &amp; King, 1994</td><td>249</td><td>No</td><td>3</td><td>1/3</td><td>0.033</td><td>0.05</td></tr><tr><td>5 McKeen, Guimaraes &amp; Wetherbe, 1994</td><td>151</td><td>No</td><td>8</td><td>0/4</td><td>n.s.</td><td>n.s.</td></tr><tr><td>6 Venkatesh &amp; Davis, 1994</td><td>47</td><td>No</td><td>1</td><td>1/4</td><td>N/A</td><td>Not available</td></tr><tr><td>7 Igbaria &amp; Baroudi, 1995</td><td>77/32</td><td>.80</td><td>1/1</td><td>3/3</td><td>0.03,0.08,third one not reported</td><td>0.036,0.123, N/A</td></tr><tr><td></td><td>81.5(average)</td><td></td><td>3.0(average)</td><td>10/23</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

<sup>a</sup> n/m means n out of m moderators were found to be significant at least at the .05 level. For example, 3/4 means 3 out of 4 moderators tested were significant at .05.  
Table 2. Summary of Moderator Articles Employing Regression and Path Analysis.

<table><tr><td>Article Number</td><td>Authors and Year</td><td>Sample Size</td><td>Significant  $Moderators^a$ </td></tr><tr><td>1</td><td>Nunamaker et al. 1991</td><td>441/387</td><td>2/22</td></tr><tr><td>2</td><td>Brown &amp; Bostrom 1994</td><td>105</td><td>0/5</td></tr><tr><td>3</td><td>Keil et al. 1994-95</td><td>313/254</td><td>0/1</td></tr><tr><td>4</td><td>Suh &amp; Jenkins 1992</td><td>60</td><td>2/4</td></tr><tr><td>5</td><td>George et al. 1990</td><td>180</td><td>2/14</td></tr><tr><td>6</td><td>Umanath, Scamell &amp; Das, 1990</td><td>114</td><td>0/1</td></tr><tr><td>7</td><td>Hale &amp; Kasker, 1989</td><td>24</td><td>0/1</td></tr><tr><td>8</td><td>Watson, Ho &amp; Raman, 1994</td><td>287/255</td><td>0/2</td></tr><tr><td>9</td><td>Chidambaram &amp; Jones, 1993</td><td>84</td><td>3/3</td></tr><tr><td>10</td><td>Todd &amp; Benbasat, 1992</td><td>56</td><td>0/2</td></tr><tr><td>11</td><td>Crossland &amp; Wynne, 1994</td><td>256</td><td>1/2</td></tr><tr><td>12</td><td>Motiwalla &amp; Pheng, 1982</td><td>51</td><td>1/8</td></tr><tr><td>13</td><td>Wilson &amp; Addo, 1994</td><td>36</td><td>2/3</td></tr><tr><td>14</td><td>Wood &amp; Nosek, 1994</td><td>132</td><td>2/6</td></tr><tr><td>15</td><td>Mookerjee &amp; DosSantos, 1993</td><td>360</td><td>4/4</td></tr><tr><td>16</td><td>Hiltz Johnson &amp; Turoff, 1991</td><td>120</td><td>1/3</td></tr><tr><td>17</td><td>Crossland, Scudder, Herschel &amp; Wynne, 1993</td><td>142</td><td>1/8</td></tr><tr><td>18</td><td>Chung &amp; Iacono, 1994</td><td>36</td><td>1/3</td></tr><tr><td>19</td><td>Tan, Wei &amp; Watson, 1993</td><td>288</td><td>1/3</td></tr><tr><td>20</td><td>Jacobs &amp; Keim, 1988</td><td>70</td><td>1/2</td></tr><tr><td>21</td><td>Sengupta &amp; Te&#x27;eni, 1993</td><td>90</td><td>1/3</td></tr><tr><td>22</td><td>Mookerjee, Mannino &amp; Gilson, 1995</td><td>50/148/200/200/200</td><td>2/10</td></tr><tr><td>23</td><td>Ang, Cummings, Straub &amp; Early, 1993</td><td>72</td><td>0/2</td></tr><tr><td>24</td><td>Jones &amp; McLeod, 1986 (transactions for 5 people)</td><td>1454</td><td>1/4</td></tr><tr><td>25</td><td>Gosler, Green &amp; Hughes, 1986</td><td>43</td><td>1/3</td></tr><tr><td>26</td><td>Kasper &amp; Cervany, 1985</td><td>96</td><td>1/3</td></tr><tr><td>27</td><td>Bostrom, Olfman &amp; Sein, 1990</td><td>19/39/89/61</td><td>1/5</td></tr><tr><td>28</td><td>Nutt, 1986</td><td>48</td><td>2/43</td></tr><tr><td>29</td><td>Eckel, 1987 (time series)</td><td>81</td><td>1/4</td></tr><tr><td>30</td><td>Bell, 1984</td><td>30</td><td>1/4</td></tr><tr><td>31</td><td>Dickson, DeSanctis &amp; McBride, 1986</td><td>363</td><td>1/8</td></tr><tr><td>32</td><td>Cook, 1993</td><td>83</td><td>0/2</td></tr><tr><td>33</td><td>Fedorowicz, Oz &amp; Berger, 1992</td><td>32</td><td>1/2</td></tr><tr><td>34</td><td>Mackay, Barr &amp; Kletke, 1992</td><td>18</td><td>1/2</td></tr><tr><td>35</td><td>Jarvenpaa, Rao &amp; Huber, 1988</td><td>21</td><td>1/9</td></tr><tr><td>36</td><td>Hughes &amp; Gibson, 1991</td><td>53/63</td><td>1/1</td></tr><tr><td>37</td><td>Vogel, Lehman &amp; Dickson, 1986</td><td>174</td><td>1/9</td></tr><tr><td>38</td><td>Davis &amp; Bostrom, 1993</td><td>80</td><td>0/4</td></tr><tr><td>39</td><td>Santhanam &amp; Sein, 1994</td><td>39/27</td><td>1/2</td></tr><tr><td>40</td><td>Duxbury, Higgins &amp; Mills, 1992</td><td>504</td><td>0/1</td></tr><tr><td>41</td><td>Ansom, Bostrom &amp; Wynne, 1995</td><td>48</td><td>0/3</td></tr><tr><td>42</td><td>DeSanctis, D&#x27;Onofrio, Smabamurthy &amp; Poole, 1989</td><td>56</td><td>0/1</td></tr><tr><td>43</td><td>Chan, Tan &amp; Wei, 1994</td><td>112</td><td>2/4</td></tr><tr><td>44</td><td>Lohse and Johnson, 1996</td><td>36</td><td>2/4 *not certain</td></tr><tr><td>45</td><td>Sambamurthy &amp; DeSanctis, 1990</td><td>39</td><td>1/2</td></tr><tr><td>46</td><td>Olfman, Sein, Bostrom, 1989</td><td>64</td><td>1/20</td></tr><tr><td>47</td><td>Jarvenpaa &amp; Machesky, 1986</td><td>36</td><td>1/1</td></tr><tr><td>48</td><td>Todd &amp; Benbasat, 1991</td><td>56</td><td>2/4</td></tr><tr><td colspan="2">Count of Samples</td><td>60</td><td>56/267</td></tr><tr><td colspan="2">Average Sample Size and Percentage of Significant Moderators</td><td>147.9</td><td>21%</td></tr></table>

<sup>a</sup> n/m means n out of m moderators were found significant. For example, 2/22 means 2 out of 22 moderators tested in the paper were significant.

Table 3. Summary of Articles using Analysis of Variance Based Techniques.

<table><tr><td></td><td></td><td colspan="6">Indicators per construct</td></tr><tr><td>Sample size</td><td>Effect (st.err)</td><td>two per construct (4 for interaction)</td><td>four per construct (16 for interaction)</td><td>six per construct (36 for interaction)</td><td>eight per construct (64 for interaction)</td><td>ten per construct (100 for interaction)</td><td>twelve per construct (144 for interaction)</td></tr><tr><td rowspan="2">20</td><td>xx-&gt;yy</td><td>0.186 (.252)</td><td>0.240 (.234)</td><td>0.257 (.213)</td><td>0.261 (.227)</td><td>0.275 (.217)</td><td>0.279 (.204)</td></tr><tr><td>zz-&gt;yy</td><td>0.339 (.266)</td><td>0.396 (.229)</td><td>0.417 (.215)</td><td>0.443 (.211)</td><td>0.450 (.223)</td><td>0.467 (.194)</td></tr><tr><td rowspan="2">50</td><td>xx-&gt;yy</td><td>0.187 (.178)</td><td>0.232 (.141)</td><td>0.256 (.127)</td><td>0.272 (.112)</td><td>0.270 (.124)</td><td>0.276 (.123)</td></tr><tr><td>zz-&gt;yy</td><td>0.324 (.220)</td><td>0.402 (.155)</td><td>0.422 (.136)</td><td>0.437 (.132)</td><td>0.445 (.122)</td><td>0.464 (.117)</td></tr><tr><td rowspan="2">100</td><td>xx-&gt;yy</td><td>0.199 (.136)</td><td>0.247 (.100)</td><td>0.256 (.099)</td><td>0.267 (.089)</td><td>0.278 (.087)</td><td>0.274 (.086)</td></tr><tr><td>zz-&gt;yy</td><td>0.323 (.199)</td><td>0.386 (.143)</td><td>0.422 (.114)</td><td>0.445 (.091)</td><td>0.450 (.092)</td><td>0.459 (.088)</td></tr><tr><td rowspan="2">150</td><td>xx-&gt;yy</td><td>0.247 (0100)</td><td>0.240 (.091)</td><td>0.255 (.080)</td><td>0.261 (.077)</td><td>0.265 (.078)</td><td>0.276 (.069)</td></tr><tr><td>zz-&gt;yy</td><td>0.386 (.143)</td><td>0.398 (.123)</td><td>0.421 (.103)</td><td>0.446 (.083)</td><td>0.455 (.078)</td><td>0.460 (.074)</td></tr><tr><td rowspan="2">200</td><td>xx-&gt;yy</td><td>0.193 (.125)</td><td>0.237 (.087)</td><td>0.254 (.074)</td><td>0.266 (.084)</td><td>0.272 (.064)</td><td>0.276 (.061)</td></tr><tr><td>zz-&gt;yy</td><td>0.327 (.185)</td><td>0.397 (.119)</td><td>0.429 (.091)</td><td>0.444 (.090)</td><td>0.452 (.072)</td><td>0.461 (.065)</td></tr><tr><td rowspan="2">500</td><td>xx-&gt;yy</td><td>0.196 (.111)</td><td>0.240 (.071)</td><td>0.254 (.059)</td><td>0.266 (.049)</td><td>0.270 (.046)</td><td>0.276 (.043)</td></tr><tr><td>zz-&gt;yy</td><td>0.327 (.177)</td><td>0.395 (.111)</td><td>0.424 (.084)</td><td>0.441 (.068)</td><td>0.453 (.058)</td><td>0.460 (.052)</td></tr></table>

T<sub>rue score</sub>= 3 0 <sub>an</sub>d 5 0 <sub>respec</sub>ti<sub>ve</sub>l<sub>y</sub> Si<sub>gn</sub>ifi<sub>cance</sub> i<sub>s</sub> d<sub>eno</sub>t<sub>e</sub>d th<sub>roug</sub>h th<sub>e</sub> b<sub>o</sub>ld<sub>e</sub>d d<sub>ou</sub>bl<sub>e</sub> li<sub>nes w</sub>ith <sub>va</sub>l<sub>ues</sub> b<sub>e</sub>l<sub>ow</sub> th<sub>e</sub> li<sub>nes</sub> b<sub>e</sub>i<sub>ng s</sub>i<sub>gn</sub>ifi<sub>can</sub>t <sub>a</sub>t 0 1 t=2 3 6 P< = 01 <sub>one</sub>-t<sub>a</sub>il  
Table for Footnote 29 in Paper - Monte Carlo Path Estimation for Direct Effect Terms (XX and ZZ) using Summated Regression (500 Runs per Cell)<sub>.</sub>

Si<sub>gn</sub>ifi<sub>can</sub>t <sub>a</sub>t 0 <sub>.</sub> 0 1  
![](/api/attachments/PJNPTKAY/fulltext/images/35fa038d5198105623c188d1b404256c1e3e85d1bb51da3501027ad749d8672a.jpg)  
Fi<sub>gu</sub>r<sub>e</sub> 6<sub>.</sub> R<sub>esu</sub>lt<sub>s o</sub>f th<sub>e</sub> Int<sub>e</sub>ra<sub>c</sub>ti<sub>o</sub>n M<sub>o</sub>d<sub>e</sub>l<sub>.</sub>

![](/api/attachments/PJNPTKAY/fulltext/images/39b7790490076b125fe3fcf3f457c28eb25e86c81f0be86d531ff5fb8f0453fd.jpg)  
Fi<sub>gu</sub>r<sub>e</sub> 7 R<sub>esu</sub>lt<sub>s o</sub>f th<sub>e</sub> Main Eff<sub>ec</sub>t<sub>s</sub> M<sub>o</sub>d<sub>e</sub>l

Fi<sub>gu</sub>r<sub>e</sub> 8<sub>.</sub> Dir<sub>ec</sub>t Eff<sub>ec</sub>t X M<sub>e</sub>an R<sub>e</sub>lati<sub>ve</sub> Bia<sub>s</sub> in PLS and R<sub>eg</sub>r<sub>ess</sub>i<sub>o</sub>n hi<sub>g</sub>hli<sub>g</sub>htin<sub>g</sub> th<sub>e</sub> infl<sub>ue</sub>n<sub>ce</sub> <sub>o</sub>f th<sub>e</sub> N<sub>u</sub>mb<sub>e</sub>r <sub>o</sub>f It<sub>e</sub>m<sub>s</sub> and Sam<sub>p</sub>l<sub>e</sub> Si<sub>ze</sub>  
(0 % represents zero bias in the true score estimation)  
![](/api/attachments/PJNPTKAY/fulltext/images/e079b946fec0d3c3d75bcdb6bffee575abc4ce94ad3a581df49cc955a1b0c484.jpg)

![](/api/attachments/PJNPTKAY/fulltext/images/d9e27ed9f8fb521d0c2c22b1bfbe89567d1b6713c92049ad89f23decc4af54eb.jpg)

Fi<sub>gu</sub>r<sub>e</sub> 9<sub>.</sub> Dir<sub>ec</sub>t Eff<sub>ec</sub>t Z M<sub>e</sub>an R<sub>e</sub>lati<sub>ve</sub> Bia<sub>s</sub> in PLS and R<sub>eg</sub>r<sub>ess</sub>i<sub>o</sub>n hi<sub>g</sub>hli<sub>g</sub>htin<sub>g</sub> th<sub>e</sub> infl<sub>ue</sub>n<sub>ce</sub> <sub>o</sub>f th<sub>e</sub> N<sub>u</sub>mb<sub>e</sub>r <sub>o</sub>f It<sub>e</sub>m<sub>s</sub> and Sam<sub>p</sub>l<sub>e</sub> Si<sub>ze</sub>  
(0 % represents zero bias in the true score estimation)  
![](/api/attachments/PJNPTKAY/fulltext/images/44c3aafda3937f961eb8938f37a41c59e739de8b478a6cd53c26c1964070ccd4.jpg)

![](/api/attachments/PJNPTKAY/fulltext/images/f106444027406b765123eba7a37e89f9e13c82109e7214d3ee417f5557d940da.jpg)

<table><tr><td>Dimension</td><td>Covariance Based Structural Equation Modeling (e.g., LISREL)</td><td>Partial Least Squares (PLS)</td></tr><tr><td>Model specification for moderators</td><td>Tedious and technically demanding - requiring the researcher, in addition to creating product indicators, to operationally:Specify correlated errors,Use mean-covariance analysis,Algebraically calculate both linear and non-linear constraints for model specification. These constraints grow exponentially with the number of interaction terms.</td><td>Simple – operationally requires only the creation of product indicators.</td></tr><tr><td>Multivariate normality</td><td>Assumed</td><td>Not assumed</td></tr><tr><td>Sample size issues:</td><td></td><td></td></tr><tr><td>- constraints</td><td>Constrained by number of interaction indicators</td><td>Independent of indicators (if reflective)</td></tr><tr><td>- heuristic rule</td><td>Requires about 100-200 minimum for any model, but increases with the number of interaction term indicators due to the number of parameters being estimated.</td><td>10 times the most complex regression (see Appendix A)</td></tr><tr><td>- example</td><td>1820 sample size required for 12-indicator model in Table 12 (364 parameters times 5 cases per parameter (Bentler &amp; Chou 1988)).</td><td>e.g., 30 sample size required for 12 Indicator model of Table 7.</td></tr><tr><td>Types of indicators</td><td>Reflective only</td><td>Reflective or formative</td></tr><tr><td>Run-time estimation:</td><td></td><td></td></tr><tr><td>- errors occurring during estimation</td><td>Typical in large models.Might not converge at 40-50 Indicators or greater</td><td>Rare, almost always converges</td></tr><tr><td>- computational time for estimation</td><td>Slow (minutes) as indicators in the model go beyond 40-50</td><td>Fast (seconds) for models with hundreds of indicators.</td></tr><tr><td>- standard error estimates (e.g., loadings and structural paths)</td><td>Unknown under Ping&#x27;s two-step approach.</td><td>Estimated using bootstrap re-sampling</td></tr><tr><td>Interaction Construct Score</td><td>Indeterminate – not part of the estimation process.</td><td>Determinate – developed to predict the dependent variable</td></tr><tr><td>Conclusion</td><td>Technically and operationally demanding, data conditions often not met, and computational solutions may not be obtained.</td><td>Operationally simpler, more consistent with data normality and sample size conditions, and solutions normally achievable.</td></tr></table>

Table 4. Comparison of Handling of Moderators in Partial Least Squares’s (PLS) and Covariance Based Structural Equation Modelng’s (e.g., LISREL)  
Drawn from Ping (1995,1996); Bollen & Paxton (1998); Fornell & Yi 1992; Kenny & Judd 1984; Joreskog &Yang 1996

<table><tr><td>Sample Size</td><td>X (.70)</td><td>Z (.70)</td><td> $X^*Z (.49)^a$ </td></tr><tr><td>Two Indicators</td><td></td><td></td><td></td></tr><tr><td>20</td><td>0.788</td><td>0.811</td><td>0.628</td></tr><tr><td>50</td><td>0.805</td><td>0.842</td><td>0.645</td></tr><tr><td>100</td><td>0.833</td><td>0.855</td><td>0.662</td></tr><tr><td>150</td><td>0.843</td><td>0.858</td><td>0.674</td></tr><tr><td>200</td><td>0.850</td><td>0.861</td><td>0.701</td></tr><tr><td>500</td><td>0.859</td><td>0.861</td><td>0.732</td></tr><tr><td>Four Indicators</td><td></td><td></td><td></td></tr><tr><td>20</td><td>0.699</td><td>0.734</td><td>0.509</td></tr><tr><td>50</td><td>0.732</td><td>0.770</td><td>0.529</td></tr><tr><td>100</td><td>0.767</td><td>0.779</td><td>0.557</td></tr><tr><td>150</td><td>0.775</td><td>0.783</td><td>0.579</td></tr><tr><td>200</td><td>0.780</td><td>0.784</td><td>0.592</td></tr><tr><td>500</td><td>0.783</td><td>0.785</td><td>0.610</td></tr><tr><td>Six Indicators</td><td></td><td></td><td></td></tr><tr><td>20</td><td>0.679</td><td>0.712</td><td>0.467</td></tr><tr><td>50</td><td>0.714</td><td>0.746</td><td>0.482</td></tr><tr><td>100</td><td>0.736</td><td>0.755</td><td>0.520</td></tr><tr><td>150</td><td>0.751</td><td>0.756</td><td>0.547</td></tr><tr><td>200</td><td>0.755</td><td>0.757</td><td>0.558</td></tr><tr><td>500</td><td>0.757</td><td>0.757</td><td>0.571</td></tr><tr><td>Eight Indicators</td><td></td><td></td><td></td></tr><tr><td>20</td><td>0.672</td><td>0.707</td><td>0.456</td></tr><tr><td>50</td><td>0.708</td><td>0.734</td><td>0.478</td></tr><tr><td>100</td><td>0.729</td><td>0.742</td><td>0.511</td></tr><tr><td>150</td><td>0.735</td><td>0.742</td><td>0.533</td></tr><tr><td>200</td><td>0.735</td><td>0.742</td><td>0.532</td></tr><tr><td>500</td><td>0.743</td><td>0.744</td><td>0.552</td></tr><tr><td>Ten Indicators</td><td></td><td></td><td></td></tr><tr><td>20</td><td>0.658</td><td>0.697</td><td>0.446</td></tr><tr><td>50</td><td>0.695</td><td>0.724</td><td>0.459</td></tr><tr><td>100</td><td>0.723</td><td>0.732</td><td>0.502</td></tr><tr><td>150</td><td>0.727</td><td>0.732</td><td>0.518</td></tr><tr><td>200</td><td>0.733</td><td>0.734</td><td>0.526</td></tr><tr><td>500</td><td>0.734</td><td>0.736</td><td>0.537</td></tr><tr><td>Twelve Indicators</td><td></td><td></td><td></td></tr><tr><td>20</td><td>0.658</td><td>0.688</td><td>0.420</td></tr><tr><td>50</td><td>0.697</td><td>0.720</td><td>0.472</td></tr><tr><td>100</td><td>0.720</td><td>0.728</td><td>0.503</td></tr><tr><td>150</td><td>0.726</td><td>0.727</td><td>0.514</td></tr><tr><td>200</td><td>0.726</td><td>0.729</td><td>0.523</td></tr><tr><td>500</td><td>0.729</td><td>0.729</td><td>0.530</td></tr></table>

<sup>a</sup> True population loadings in brackets  
<sup>b</sup> Average refers to taking the mean of the loadings (across 500 runs) for each indicator connected to a construct and then calculating an overall mean by considering the number of indicators involved. Table 8. Average Loadings for each Construct<sup>b</sup>.

<table><tr><td>ITEM</td><td>WEIGHT</td><td>LOADING</td></tr><tr><td colspan="3">Perceived Usefulness composite reliability = 0.975</td></tr><tr><td>UFL1</td><td>0.175</td><td>0.890</td></tr><tr><td>UFL2</td><td>0.166</td><td>0.934</td></tr><tr><td>UFL3</td><td>0.179</td><td>0.951</td></tr><tr><td>UFL4</td><td>0.183</td><td>0.958</td></tr><tr><td>UFL5</td><td>0.177</td><td>0.944</td></tr><tr><td>UFL6</td><td>0.196</td><td>0.904</td></tr><tr><td colspan="3">Enjoyment composite reliability = 0.853</td></tr><tr><td>ENJ1</td><td>0.463</td><td>0.907</td></tr><tr><td>ENJ2</td><td>0.488</td><td>0.867</td></tr><tr><td>ENJ3</td><td>0.244</td><td>0.645</td></tr><tr><td colspan="3">Intention composite reliability = 0.964</td></tr><tr><td>INT1</td><td>0.329</td><td>0.945</td></tr><tr><td>INT2</td><td>0.362</td><td>0.949</td></tr><tr><td>INT3</td><td>0.364</td><td>0.949</td></tr><tr><td colspan="3">Interaction composite reliability = 0.980</td></tr><tr><td>UFL1ENJ1</td><td>0.079</td><td>0.890</td></tr><tr><td>UFL1ENJ2</td><td>0.070</td><td>0.848</td></tr><tr><td>UFL1ENJ3</td><td>0.063</td><td>0.831</td></tr><tr><td>UFL2ENJ1</td><td>0.068</td><td>0.878</td></tr><tr><td>UFL2ENJ2</td><td>0.065</td><td>0.828</td></tr><tr><td>UFL2ENJ3</td><td>0.050</td><td>0.802</td></tr><tr><td>UFL3ENJ1</td><td>0.070</td><td>0.906</td></tr><tr><td>UFL3ENJ2</td><td>0.064</td><td>0.842</td></tr><tr><td>UFL3ENJ3</td><td>0.050</td><td>0.813</td></tr><tr><td>UFL4ENJ1</td><td>0.071</td><td>0.903</td></tr><tr><td>UFL4ENJ2</td><td>0.069</td><td>0.882</td></tr><tr><td>UFL4ENJ3</td><td>0.050</td><td>0.836</td></tr><tr><td>UFL5ENJ1</td><td>0.072</td><td>0.908</td></tr><tr><td>UFL5ENJ2</td><td>0.067</td><td>0.873</td></tr><tr><td>UFL5ENJ3</td><td>0.052</td><td>0.829</td></tr><tr><td>UFL6ENJ1</td><td>0.079</td><td>0.878</td></tr><tr><td>UFL6ENJ2</td><td>0.074</td><td>0.843</td></tr><tr><td>UFL6ENJ3</td><td>0.053</td><td>0.789</td></tr></table>

\* All significant at 0.01  
Table 11. Weights and Loadings Results from PLS Analysis of the Interaction Model for Study 2.

## Expected Reliability

These summated regression estimate results should not be too surprising. The reliability of the composite (i.e., Cronbach’s alpha) for these sets of items can be calculated as $\frac { N \overline { { \rho } } } { 1 + \overline { { \rho } } [ N - 1 ] }$ , where

is the average inter-item correlation and N is the number of items. In the case of a homogenous set of 8 item loadings set at 0.70, the inter-item loadings are all 0.49 and the resulting alpha becomes 0.885 for the main effects. Since the interaction items are not independent, the reliability is calculated as the product of the alphas for the two main effects $( \mathrm { i . e . , . 0 8 8 5 ^ { 2 } = 0 . 7 8 3 } )$ as opposed to using the alpha calculations for the 64 items. While these consistency measures look reasonable, it theoretically implies that a true population interaction effect of 0.30 would yield an estimate of 0.250 $( \mathrm { i . e . , ~ } \sqrt { 0 . 8 8 5 } ^ { \ast } 0 . 3 0 ^ { \ast } \sqrt { 0 . 7 8 3 } )$ . In the case of our simulation at sample size of 100, we obtained a lower mean interaction of 0.249 $( \mathrm { s . e . } = 0 . 0 9 0 )$ likely representing some variation in the loadings from 0.70.

## APPENDIX A -- PLS Method

Partial Least Squares (PLS) can be a powerful method of analysis because of the minimal demands on measurement scales, sample size, and residual distributions. Although PLS can be used for theory confirmation, it can also be used to suggest where relationships might or might not exist and to suggest propositions for later testing.

As an alternative to the more widely known covariance fitting approach (exemplified by software such as LISREL, EQS, COSAN, AMOS, and SEPATH), the component-based PLS avoids two serious problems: inadmissible solutions and factor indeterminacy (Fornell and Bookstein, 1982). The philosophical distinction between these approaches is whether structural equation modeling is used for theory testing and development or for predictive applications (Anderson and Gerbing, 1988). In situations where prior theory is strong and further testing and development is the goal, covariance based full-information estimation methods (e.g., using Maximum Likelihood or Generalized Least Squares) are more appropriate. Yet, due to the indeterminacy of factor score estimations, there exists a loss of predictive accuracy. This, of course, is not of concern in theory testing where structural relationships (i.e., parameter estimation) among concepts is of prime concern.

For application and prediction, a PLS approach is often more suitable. Under this approach, it is assumed that all the measured variance is useful variance to be explained. Since the approach estimates the latent variables as exact linear combinations of the observed measures, it avoids the indeterminacy problem and provides an exact definition of component scores. Using an iterative estimation technique (Wold, 1982), the PLS approach provides a general model which encompasses, among other techniques, canonical correlation, redundancy analysis, multiple regression, multivariate analysis of variance, and principle components.

As a consequence of using an iterative algorithm consisting of a series of ordinary least squares analyses, identification is not a problem for recursive (i.e., one way path) models nor does it presume any distributional form for measured variables. Furthermore, sample size can be smaller, with a standard rule of thumb suggesting that it be equal to the larger of the following: (1) ten times the number of indicators for the scale with the largest number of formative (i.e., causal) indicators (note that scales for constructs designated with reflective indicators as specified in this study can be ignored), or (2) ten times the largest number of structural paths directed at a particular construct in the structural model. A weak rule of thumb, similar to the heuristic for multiple regression (Tabachnik and Fidell, 1989, p. 129), would be to use a multiplier of five instead of ten for the preceding formulae. An extreme example is given by Wold (1989) who analyzed 27 variables using two latent constructs with a data set consisting of ten cases. For more details, see Chin and Newsted (1999).

When estimating interaction effects, Ping (1996) noted that recent covariance based procedures “can produce specification tedium and errors or estimation difficulties in larger structural equations models” (1996). Ping (1995; 1996) has suggested an alternative two-step approach to overcome these limitations however the ability to assess the reliability and validity of individual items using a two step approach has been questioned (Fornell and Yi, 1992).

Second order factors can be approximated using various procedures. One of the easiest to implement is the approach of repeated indicators known as the hierarchical component model suggested by Wold (cf. Lohmöller, 1989, pp. 130-133). In essence, a second order factor is directly measured by observed variables for all the first order factors. While this approach repeats the number of manifest variables used, the model can be estimated by the standard PLS algorithm. This procedure works best with equal numbers of indicators for each construct.

Finally, PLS is considered better suited for explaining complex relationships (Fornell, Lorange, and Roos, 1990; Fornell and Bookstein, 1982). As stated by Wold (1985, p. 589), “PLS comes to the fore in larger models, when the importance shifts from individual variables and parameters to packages of variables and aggregate parameters.” Wold states later (p. 590), “In large, complex models with latent variables PLS is virtually without competition.”

Nevertheless, being a limited information method, PLS parameter estimates are less than optimal regarding bias and consistency. The estimates will be asymptotically correct under the joint conditions of consistency (large sample size) and consistency at large (the number of indicators per latent variable becomes large). Otherwise, estimates on paths from construct to loadings tend to be overestimated and structural paths among constructs underestimated. Furthermore, standard errors need to be estimated via resampling procedures such as jackknifing or bootstrapping (cf. Efron and Gong, 1983). The significance of paths can also be determined by using the jackknife statistics resulting from a blindfolding resampling procedure (Lohmöller, 1984, pp. 5-09 through 5-12). The blindfolding procedure omits a part of the data matrix for the construct being examined and then estimates the model parameters. This is done a number of times based on the blindfold omission distance. Results obtained from this resampling procedure include the jackknifed estimated means and standard deviations.

In this paper, all structural paths were significant at the 0.01 level using a bootstrapping sample of 200. Also, it should be noted that by using the PLS algorithm under a reflective mode for all constructs, we eliminate any concerns of collinearity within blocks of variables used to represent underlying constructs.

Overall, rather than being viewed as competitive models, the covariance fitting procedures (i.e., ML and GLS) and the variance-based PLS approach have been argued as complementary in nature. According to Jöreskog and Wold (1982, p 270):

“ML is theory-oriented, and emphasizes the transition from exploratory to confirmatory analysis. PLS is primarily intended for causal-predictive analysis in situations of high complexity but low theoretical information.”

## Sample Size Required for PLS Product Indicator Approach Compared to LISREL

While the sample size suggested here might seem quite large, it is relatively small when contrasted against the sample size necessary for covariance-based procedures using software such as LISREL or EQS. Table 12 below contains a few simple heuristics for sample size calculations compared between PLS and LISREL. As an extreme, consider the case of twelve indicators per construct. This represents, as a first approximation (ignoring correlated error terms and non-linear constraints), 364 parameters to be estimated<sup>2</sup>. While a power analysis or simulation study provides a more accurate means for estimating the necessary sample size, Bentler and Chou (1988, p. 172) gave a heuristic of 5 cases per parameter estimated under normal conditions. Using this rule of thumb, a sample size of 1820 would be needed to analyze the same model used in this paper in either LISREL or EQS. Even for the simpler two indicators per construct case, you would still need a sample size of 120. For nonnormal conditions, Bentler and Chou recommend a minimum ratio of 10 cases per parameter estimated.

<table><tr><td>Model</td><td>LISREL Parameters</td><td>LISREL Sample Size (x 5 cases)</td><td>PLS Sample Size (x 10 cases)</td></tr><tr><td>3 constructs with 3, 3 and 9 indicators1 DV with 3 indicators</td><td>40</td><td>200</td><td>30</td></tr><tr><td>3 constructs with 12, 12 and 144 indicators1 DV with 12indicators</td><td>364</td><td>1820</td><td>30</td></tr><tr><td>21 constructs with 672 indicators</td><td>Min 1366</td><td>6830</td><td>210</td></tr></table>

Table 12 Simple Heuristics for LISREL and PLS Sample Size Requirements\* \*Power Analysis is best completed suggestions such as those provide by Bentler and Chou’s 1988 (p. 172).

## APPENDIX B -- Power Implications

Sample size and the number of indicators contribute to statistical estimates through an influence on power. While increasing sample size will provide a more accurate estimate of a parameter (i.e., smaller standard error), that parameter estimate can still be inconsistent (i.e., biased from the true score). The evidence is seen in the patterns of the standard errors and the estimations. In Table 7, it can be seen that standard errors within a column get smaller as the sample size increased. For instance, the standard error for X\*Z (2 indicators) reduces from .352 to .142 as sample size increases from 20 to 500. This increase in statistical precision affords more power to detect an effect should one exist, but the estimations are not consistent in terms of the estimates moving closer to the true population parameter with larger sample sizes. This inconsistency with sample size is demonstrated by noting that the path estimates within the columns did not increase systematically toward the known true effects. For example, the interaction term of X\*Z in the second column (2 indicators) changed from .162 to .165 when sample size increased from 20 to 500, which is far removed from the .30 true effect.

Therefore, this simulation partially demonstrates what Wold (1985; 1989) termed “consistency at large” for PLS estimation. This term refers to the tendency in PLS estimation to get closer to the true population parameter, or true score, as the number of indicators and sample size increase.

Power also increases when the number of indicators increases. Table 5 shows how this can happen. Compare any row in the interaction term results and you will note that the .01 significance level for that sample size is achieved with a larger set of indicators. For instance, with a 100 sample size, increasing the number of indicators to 6 will obtain a .01 significance. At a sample size of 150, 4 indicators are needed to achieve the same significance level. In contrast, the predictor X results, whose indicators are more reliable than those of the interaction term by a factor of a square root, reaches .01 significance for the 100 sample size with an even smaller number of indicators -- 2. The moderator Z term with a larger effect size achieves the same .01 significance at 50 sample size and 2 indicators. These results demonstrate the tradeoffs among reliability of measures, sample size, and number of indicators that a researcher can consider.

# APPENDIX C -- Construct Definitions and Items Used For Study 2

Perceived Usefulness

Construct Definition (Davis, 1989): The degree to which a system is perceived to enhance one's performance.

UFL1 Using Electronic Mail in my job enables (would enable) me to accomplish tasks more quickly.

UFL2 Using Electronic Mail improves (would improve) my job performance.

UFL3 Using Electronic Mail in my job increases (would increase) my productivity.

UFL4 Using Electronic Mail enhances (would enhance) my effectiveness on the job.

UFL5 Using Electronic Mail makes it (would make it)easier to do my job.

UFL6 I find (would find) Electronic Mail useful in my job.

(7 point scale using: extremely likely, quite, slightly, neither, slightly, quite, extremely unlikely)

Future tense wording in parentheses were added to be meaningful for a percentage of respondents who have not used electronic mail.

## Enjoyment

Construct Definition (Davis, Bagozzi, and Warshaw, 1992): The extent to which the activity of using the computer is perceived to be enjoyable in its own right, apart from any performance consequences. (Electronic Mail was substituted for the behavior of using the computer).

ENJ1 I find (would find) using Electronic Mail to be enjoyable.

(7 pt scale using: extremely likely, quite, slightly, neither, slightly, quite, extremely unlikely)

ENJ2 The actual process of using Electronic Mail is (would be)

(7 point scale using: extremely unpleasant, quite, slightly, neither, slightly, quite, extremely pleasant)

ENJ3 I have (would have) fun using Electronic Mail.

(7 point scale using: extremely likely, quite, slightly, neither, slightly, quite, extremely unlikely)

Intention To Regularly Use Electronic Mail

Construct Definition: A measure of the strength of one’s intention to perform a behavior [behavioral intention]. In this case, the behavior is to use Electronic Mail regularly.

INT1 I presently intend to use Electronic Mail regularly:

(7 pt scale using: extremely likely, quite, slightly, neither, slightly, quite, extremely unlikely)

INT2 My actual intention to use Electronic Mail regularly is:

(7 point scale using: extremely strong, quite, slightly, neither, slightly, quite, extremely weak)

INT3 Once again, to what extent do you at present intend to use Electronic Mail regularly:

(11 point scale from 0 to 10 with anchors Definite no, Definite Yes)

The data were obtained from a single organization that had recently installed electronic mail.<sup>3</sup> A total of 60 questions relating to a recent introduction of electronic mail were presented. Of the 575 questionnaires distributed, 250 usable responses were analyzed representing 43.5 percent of those surveyed. On average, the respondents had been using electronic mail for 9 months, sent 2.53 messages per day (s.d. = 2.36) and received 4.79 messages per day (s.d. = 3.49). Respondents were on average 39 years old (s.d. = 9.28) and had worked for the company an average of 11 years (s.d. = 6.9). Sixty percent of the respondents were male. The respondents came from various levels in the organization, 13 percent were managers, 12 percent were engineers, 38 percent were technicians, and the remaining 37 percent were clerical workers.

# APPENDIX D -- Detailed Explanation of Known PLS Biases, Reliability, Non-Linear Indicators and Formative Indicators

Actual PLS Biases

Under situations with smaller sample sizes or few indicators, the known bias in PLS for underestimating the structural paths among constructs and overestimating the measurement loadings may occur. Using an actual data set, the interaction effect between enjoyment and perceived usefulness on adoption intention was demonstrated. With the simulation study as a guide, it is likely that the structural effects are still being underestimated and the construct loadings are being overestimated since the number of indicators for the two constructs were 3 and 6 respectively. But in this case, using a 10 percent inflation rule, the structural true scores are likely higher since the loading estimates are in the 0.90 region. The extent to which the negative moderating effect of enjoyment holds up in future studies is debatable, but the results do suggest the need for further research regarding the role of emotions in general and enjoyment in particular for predicting IT intentions and usage behaviors.

## Increase Reliability

It is possible that, with more reliable measures (true loadings of 0.80 or higher), the need for 6 to 8 indicators per construct, as well as the sample size, may be relaxed. Thus it is important to reiterate that whereas sample size increases the power to detect an effect, the key issue for consistent estimation of the true “population” effect is in obtaining reliable estimates of the underlying construct. This can be accomplished by either increasing the number of indicators at a given level of reliability or by increasing the reliability of the indicators at a given number of indicators (e.g., two indicators with 0.80 loading yields equivalent construct reliability to 8 indicators at 0.50 loadings). Or, in other words, a couple of good quality measures are as good as many less reliable measures.

Overall, more simulation studies need to be conducted (under varying conditions) to assess how PLS in general and the PLS product-indicator approach in particular perform. While the ability to detect and obtain consistent estimates will likely occur sooner with more reliable measures, it is not clear how the procedure will work for a non-homogeneous set of indicators where both the degree of normality and loadings vary. Based on our understanding of the PLS algorithm, it would be expected to perform better than a strategy of simply summing the individual indicators for each construct to create a composite score and then using multiple regression. The reliability assessment of the averaged regression approach shown in Table 11 clearly demonstrated the weakness that yielded moderator scores much less than the true effect size.

## Non-linear Aggregation

The approach presented here of creating nonlinear product indicators for PLS estimation can be extended to other powers (e.g., $\mathrm { X } ^ { 2 } , \mathrm { X } ^ { 3 }$ , or $X ^ { 2 * } Z )$ as long as the indicators for the predictor and moderator constructs are viewed as reflective measures. If analyzing formative measures,<sup>4</sup> see the explanation below for how to adjust the PLS approach. Further, the indicators need not be interval level. We believe that ordinal or even dichotomous variables can be used as long as there is a large enough set to represent the underlying continuous latent variable.

Ideally, these additional power constructs for the main components $( \mathrm { i } . \mathrm { e } . , X ^ { 2 }$ and $Z ^ { 2 } )$ should be included with the interaction construct when conducting a stepwise regression. Assuming composite reliabilities are equivalent, if the product construct enters first relative to the other constructs that would indicate the presence of an interaction effect. Without such a process, we cannot conclusively attribute the effect to the interaction term. Due to page limitations, this analysis was not performed with the Study 2 data since the goal of this paper was to demonstrate the new approach.

## Formative Indicators

The current procedure, as described in this paper, cannot be used for formative indicators, which are viewed as measures that create a latent construct (see Chin and Gopal 1995 for a discussion regarding the formative/reflective distinction). Since formative indicators are not assumed to reflect the same underlying construct (i.e., can be independent of one another and measuring different factors), the product indicators between two sets of formative indicators will not necessarily tap into the same underlying interaction effect.

One alternative approach for formative indicators would be to follow a two-step score construction procedure. The first step would entail using the formative indicators in conjunction with PLS to create underlying construct scores for the predictor and moderator variables. Step two would then consist of taking those single composite construct scores to create a single interaction term.
