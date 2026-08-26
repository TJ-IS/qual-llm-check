---
otero_id: 26982
otero_key: "SY8FEB4J"
title: "The Problem of Statistical Power in MIS Research"
authors: "Jack J. Baroudi; Wanda J. Orlikowski"
year: "1989"
journal: "MIS Quarterly"
doi: "10.2307/248704"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
The Problem of Statistical Power in MIS Research
Author(s): Jack J. Baroudi and Wanda J. Orlikowski
Source: MIS Quarterly, Vol. 13, No. 1 (Mar., 1989), pp. 87-106
Published by: Management Information Systems Research Center, University of Minnesota
Stable URL: http://www.jstor.org/stable/248704

Accessed: 09/05/2014 14:22

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# The Problem of Statistical Power in MIS Research

By: Jack J. Baroudi\* Information Systems Department Stern School of Management New York University 621 Tisch Hall 40 West 4th Street New York, NY 10003

Wanda J. Orlikowski
Information Technologies Group
Sloan School of Management
Massachusetts Institute of Technology
E53-329
Cambridge, MA 02139

## Abstract

Statistical power is a topic of importance to any researcher using statistical inference testing. Studies with low levels of statistical power usually result in inconclusive findings, even though the researcher may have expended much time and effort gathering the data for analysis. A survey of the statistical power of articles employing statistical inference testing published in leading MIS journals shows that their statistical power is, on average, substantially below accepted norms. The consequence of this low power is that MIS researchers typically have a 40 percent chance of not detecting the phenomenon under study, even though it, in fact, may exist.

Fortunately, there are several techniques, beyond expanding the sample size (which often may be impossible), that researchers can use to improve the power of their studies. Some are as easy as using a different but more powerful statistical test, while others require developing more elaborate sampling plans or a more careful construction of the research design. Attention to the statistical power of a study is one key ingredient in assuring the success of the study. This article should serve as a useful guide for MIS researchers in the planning, execution, and interpretation of inferential statistical analyses.

Keywords: Statistical power, statistical inference testing, research methods, empirical research

ACM Categories: H.0, J.0

## Introduction

Significance testing under the Neyman-Pearson formulation of rejecting or not rejecting a null hypothesis is perhaps the primary means by which researchers in the behavioral sciences, including MIS, detect the presence of an effect in the phenomena they are investigating.

An important component of statistical inference testing is the notion of statistical power, defined as the probability that a statistical test will correctly reject a null hypothesis. Recent discussions in the reference disciplines of MIS suggest that the attention afforded to statistical power has been inadequate, leading to negative consequences for research findings. Surveys of research in communication, education, management, marketing, social psychology, and applied psychology find that most of the published studies have relatively low levels of statistical power (Chase and Chase, 1976; Chase and Tucker, 1975; Cohen, 1962; Katzer and Sodt, 1973; Mazen, et al., 1987; Sawyer and Ball, 1981).

Additionally, failure to provide an adequate level of statistical power has implications for both the execution and the outcomes of research. Stevens (1980) suggests that if researchers are going to invest time, effort, and money in a study, they should want a reasonably good probability of finding significant findings, if, in fact, they exist. Where the power of statistical tests is weak, this probability will be small, and the outcomes will likely be insignificant. Failure to provide information about the particular statistical power of a study can lead to misinterpretation of research results. Such knowledge is necessary to indicate post hoc whether insignificant results were due to poor power levels, or if the phenomenon is, in reality, insignificant.

Given the poor state of affairs with respect to statistical power in disciplines traditionally serving to inform MIS research, we became interested in how well MIS research fares on the issue of statistical power. Culnan (1986) determines that the level of paradigm development in MIS research is far less established than that of the referent disciplines of psychology, management science, sociology, organizational studies, and computer science. It seemed unlikely that MIS research methods and techniques would be any more sophisticated than those prevalent in these referent disciplines. We wanted to determine the status of MIS research regarding this component of statistical inference testing. Our interest culminated in this article, the purpose of which is threefold:

1. To revitalize interest in the issue of statistical power among MIS researchers by reviewing the determinants of statistical power and how statistical power can be used before, during, and after the execution of a research study;

2. To report the results of a survey conducted to assess the statistical power of a sample of MIS research studies and discuss the implications of these findings;

3. To discuss techniques that MIS researchers can use to increase the statistical power of their studies, and hence improve the quality of studies conducted and the conclusions emanating from MIS research.

## Statistical Power: Background

Researchers investigating a phenomenon typically assume that a relationship among the investigated variables exists. Classical statistical inference tests posit a null hypothesis of no relationship between the variables of interest, which researchers hope to reject. Two errors in statistical inference procedures need to be guarded against. Type I error is the probability of incorrectly rejecting a null hypothesis; that is, of finding an effect or relationship when none exists. The risk associated with committing Type I errors is represented by $\alpha$ , the significance criterion. Type II error is the probability of incorrectly sustaining the null hypothesis; that is, of failing to detect an effect or relationship when one exists. The risk associated with committing Type II errors is represented by $\beta$ . The probability that a statistical test will correctly reject a false null hypothesis is known as the power of the test, and is represented by 1 - $\beta$ .

Statistical power becomes particularly crucial to the interpretation of results in those cases where the null hypothesis is false; that is, when the phenomenon being investigated does exist. If the test reveals non-significant results in these circumstances, the usual response is to accept the null hypothesis and conclude that the effect being examined does not exist. $^{1}$ Such a conclusion, however, would not be appropriate if the phenomenon actually exists but was undetected because the statistical test was not powerful enough. In such a case, a conclusion of “no effect” would be misleading; we would be generating a spuriously negative result — committing a Type II error.

There is a distinct asymmetry in the attention paid to the two types of statistical inference errors (Type I and Type II) in the behavioral science and MIS literatures. While the focus on Type I errors is clearly appropriate, Type II errors should not be overlooked. Typically, Type I error ( $\alpha$ ) is carefully guarded against by setting the significance criterion to a prudently low level of .05 or .01. The second type of error ( $\beta$ ), however, is often ignored by researchers (Myers and Melcher, 1969). Yet it need not and, indeed, should not be. The probability of committing a Type II error can be controlled and planned for in advance. In this way, researchers can ensure that statistical tests have sufficient power to detect whether the phenomena being examined exist. While researchers would like to maximize the probability of correctly rejecting the null hypothesis (statistical power), $\alpha$ and $\beta$ are not independent. Hence, having set $\alpha$ , the levels of $\beta$ and 1 - $\beta$ will be constrained. The best that researchers can do is to keep the relationship between the two errors, Type I and Type II, at a reasonable level (Cascio, et al., 1978).

The traditional belief is that the consequences of false positive claims are more serious than those of false negative claims (Cohen, 1965).

Therefore, Type I errors are usually guarded against more stringently. The distribution of risk between Type I and Type II errors, however, needs to be appropriate to the situation at hand. Mazen, et al. (1987) present a graphic illustration of a case where the risk of incurring a Type II error far outweighed that for Type I. They discuss the decision making surrounding the ill-fated Challenger space shuttle, where NASA officials faced a choice between two assumptions.

The first assumption was that the shuttle was unsafe to fly because the performance of the O-ring in the rocket-booster was different from that used on previous missions. The second was that the shuttle was safe to fly because there would be no difference between the performance of the O-rings in this and previous missions. If the mission had been aborted and the O-ring had indeed been functional, Type I error would have been committed. Obviously the cost of the Type II error, launching with a defective O-ring, was much greater than the cost that would have been incurred with Type I error (p. 370).

Researchers who wish to conform to the convention of protecting themselves more against false positive claims should set $\alpha$ to .05 and $\beta$ to .20 (four times as much) (Cohen, 1977). Accepting these recommended values for $\alpha$ and $\beta$ results in a .80 value for power (1 - $\beta$ ), meaning that a statistical test having a power value of .80 has an 80% probability of detecting an effect if it exists. Cohen's prescription of a .80 conventional power level has become widely accepted as the norm (Mazen, et al., 1987; Robins, 1988; Sawyer and Ball, 1981; Stevens, 1980). Studies that employ high power levels (.80 or higher) offer advantages in interpretation of results (Keppel, 1973). Studies with high power that find insignificance provide strong support for the decision not to reject the null hypothesis, while studies with low power provide little support for either the null or alternative hypotheses.

## Statistical Power: Planning and Use

In the next section, we examine the particular determinants of the statistical power of a test and explore some of the ways researchers may use the tool of statistical power analysis to improve the conduct and interpretation of research.

## Determinants of statistical power

The power $(1 - \beta)$ of any statistical test of a null hypothesis is a function of the following three parameters:

1. The significance criterion ( $\alpha$ ), which is the chosen risk of incurring a Type I error, and whether the test is directional (one-tailed) or non-directional (two-tailed). Power increases with larger $\alpha$ and with directional hypothesis tests.

2. The precision of sample estimates, which is primarily influenced by the sample size n. The larger the n, all else being equal, the smaller the error, and the greater the precision, which increases the probability of rejecting the false null hypothesis.

3. The effect size, which represents the magnitude or strength of the relationship among the variables in the population. If other factors are controlled, the larger the effect size, the greater the degree that a phenomenon manifests itself, and the greater the probability that it will be detected and the null hypothesis rejected.

Statistical power and its three determinants are related in such a manner that when any three are known, so is the fourth. Ideally, the researcher planning his or her study should estimate the effect size being investigated, set $\alpha$ and $\beta$ to the desired ratio (hence determining the level of power that is desired for the study), and then solve for the necessary sample size by referring to one of the texts providing tables or graphs that allow such determination (Cohen, 1977; Kraemer and Thiemann, 1987; Myers, 1980). Such explicit consideration of significance-test parameters will ensure that researchers obtain the requisite n to achieve the level of power deemed necessary for their research, while maintaining a reasoned balance between Type I and Type II error rates.

## Effect size

While sample size and significance criterion are relatively well-known and utilized components of inference statistics, effect size is a more poorly understood concept. Sawyer and Ball (1981) in their survey of marketing research find that effect size is not as explicitly considered by researchers as the other two concepts. In the review of

MIS research found later in this article, we find the same to be true of published MIS studies. In this section, in an attempt to re-acquaint MIS researchers with this important component of statistical testing, we examine some of the substantive issues surrounding the concept of effect size. A recognition of the critical role played by effect size in the determination of the power of a statistical test is fundamental to adequate interpretation and application of research results.

The effect size measures the effectiveness of a theory to explain or predict empirical observations (Webster and Starbuck, 1988). It represents an estimate of the magnitude of the investigated phenomenon in the population. Several researchers have suggested that effect size can be expressed in terms of the proportion of explained variance (Cohen, 1965; 1973; Friedman, 1968; Hays, 1963; 1981; Kraemer and Thiemann, 1987). Increasingly, researchers are urging that effect sizes be reported along with significance levels as indicators of the importance of findings, and as means of comparing findings across studies. (See review by O'Grady, 1982.) Effect sizes are seen as particularly important, since investigators can directly control significance levels by making more or less observations, while effect sizes are more robust measures of theories' effectiveness (Webster and Starbuck, 1988).

Nelson, et al. (1986) conducted a survey of psychology researchers and found that their confidence in a study's findings depended primarily on significance levels and only secondarily on effect sizes. Cohen (1965) expresses this confusion very well: "A neat semantic trap has been set: 'What matters is significance — what is significant is significance — that which is significant, matters.' Finally, the trap is sprung: 'If it is significant, it matters' " (p. 101). Cohen proceeds to warn researchers about distinguishing between statistical significance and degree of association, recommending that they report both measures in their research results. O'Grady (1982), however, argues persuasively that there are severe limitations on the usefulness of measures of association. He cautions against attaching too much substance to the information researchers provide about the phenomena investigated.

Among the many issues he examines, O'Grady discusses two that are particularly pertinent to the role of effect size in influencing the power of statistical tests. The first of these is that theories, in general, suggest that the behavior and attitudes examined in the research literature have multiple determinants. As many researchers are limited (by time, money, methodology, and the like) to examining only a few variables per investigation, the measures of explained variance of any one study are inescapably limited from the start. The second issue stems from the discipline of psychometrics, which informs us that there are inevitable errors in measurement that arise from the process of operationalization and imperfect reliability of measures. These errors impose an upper bound on the size of the effects that can be detected. O'Grady (1982) notes that all of the behavioral sciences will "produce small measures of explained variance because of measurement problems alone" (p. 770).

O'Grady's explication of these effect-size issues leads us to suggest that the phenomena investigated in MIS research studies are unlikely to display large effects and that, typically, small to medium effect sizes should be anticipated. From a psychological perspective, a medium difference should be large enough to be noticeable. A small effect, on the other hand, is relatively imperceptible, with medium effects being about twice as large as small effects in the population (Mazen, et al., 1987). A large effect, in general, is so apparent as to “render a statistical test virtually superfluous” (Cohen, 1965, p. 97).

Of the three power parameters, effect size is probably the most important determinant of statistical power. Cohen (1973) notes that "If ES [effect size] has been judiciously estimated, as it should be, power analysis is a powerful, in fact the only rational, guide to planning the relevant details of the research" (p. 277). However, effect size is perhaps the most difficult parameter for researchers to estimate. It can sometimes be determined by establishing an index for effect size from the proportion of explained variance accounted for in prior research (Mazen, et al., 1987). Unfortunately, this is unlikely to be very useful in the case of MIS research where subareas of the discipline do not have well-established cumulative findings of specific phenomena (Culnan, 1986). Further, many MIS research studies do not report sufficient information to calculate the proportion of explained variance.

Where an area of research is new, or where it is infeasible to calculate such an index, researchers can perform a pilot study and attempt to estimate a value for the effect size from this preliminary analysis (Stevens, 1980), or they can employ conventional effect sizes representing small, medium and large effect-size levels of a phenomenon. Such proxy effect-size levels were established by Cohen (1977) and have become something of a research standard, being widely accepted and utilized by behavioral science researchers (Cascio, et al., 1978; Mazen, et al., 1987; Robins, 1988; Sawyer and Ball, 1981).

An illustration of Cohen's effect-size conventions would be the effect-size index for the difference between two means, which is the standardized difference $d$ between them. $^{2}$ For small, medium, and large effect sizes, $d$ is assigned the values of .20, .50, and .80, respectively (Cohen, 1977). In other words, a small effect is defined as a .20 standard deviation between population means, a medium effect as a .50 standard deviation between population means, and a large effect as a .80 standard deviation between population means. Cohen (1977) provides conventional, proxy effect-size levels to be detected by many of the standard statistical tests (i.e., correlation, analysis of variance, multiple regression analysis, Chi-square, and the difference between two proportions). Cohen (1977) notes, however, that these conventions should serve as useful guidelines only and should not be mindlessly adhered to when a particular research situation indicates otherwise.

Kraemer and Thiemann (1987) propose an alternative approach to estimating effect sizes. Unlike Cohen (1977), they have compiled a single power table appropriate for a wide selection of common statistical tests. (See Kraemer and Thiemann, 1987, p. 28.) To use this table, however, preliminary data is needed, gleaned either from prior research or by conducting a pilot study. From such preliminary evidence, data can be obtained on the parameter of interest (such as the mean, correlation coefficient, and so on), and the variability of the statistic (such as the standard deviation). Then the expected quantitative difference constituting the primary hypothesis to be tested in the current study is determined (e.g., the difference between the expected mean of the control group and the expected mean of the treatment group). This difference is then divided by the measure of variability obtained from the preliminary evidence, to yield what Kraemer and Thiemann call a critical effect size. This critical effect size has advantages in that it captures the particular characteristics of the study at hand; that is, “the critical effect size is population-specific as well as measurement-specific” (Kraemer and Thiemann, 1987, p. 24). $^{3}$ In the absence of such information, however, researchers are advised to utilize Cohen’s (1977) effect-size standards.

## Using statistical power analysis

Analyzing the power of statistical tests is a useful technique at all three stages of a research project: before, during and after. In each case, determining the power allows the researcher to take action that will improve his or her research study, either by increasing the probability of detecting significant findings, or by qualifying the research results to permit better interpretation of findings.

## A Priori Determination of Statistical Power

As statistical power measures the a priori probability of detecting significant effects (Medler, et al., 1981), power analysis can be used as a planning tool to ensure that a particular research study has a reasonable probability of detecting a significant finding. At the onset of a study, the researcher can use the statistical power function to determine the sample size necessary to achieve desired levels of his or her chosen parameters. Assigning a high level to statistical power (for example, .80) supplies the research study with a non-trivial probability of finding an effect, if it exists. Cohen (1977) provides power tables for various common statistical tests that can be consulted to determine the sample size for specified values of $\alpha$ , power, and effect size.

This determination can be repeated a number of times, each time with different levels of the parameters to establish acceptable levels, given the researcher's resource constraints and intentions. There are clearly numerous tradeoffs involved in power calculations at this stage of a research project. Each individual researcher will determine his or her own specific settings. We urge that these tradeoffs be consciously surfaced and debated, so that researchers, by making explicit and informed decisions, can play a more active role in determining the characteristics of their studies.

## Post Hoc Determination of Statistical Power

Researchers can also use power analysis to perform post hoc evaluations of the power of given statistical tests in their own or other's research as the type of test, the sample size, and the significance level are known. If the effect size is not provided, the researcher can estimate a value by using one of the techniques outlined in the previous section. With these known parameters, the power of the statistical test to detect significant findings can be determined. Here the question posed above is reversed. That is, the sample size has already been established, and what is sought is the level of statistical power. Cohen (1977) provides tables for each of the major statistical tests that indicate a study's power given the type of test, the significance criterion, the study's sample size, and an estimate of the effect size being investigated.

Cohen's evaluation is particularly informative in evaluating how much weight to attach to non-significant findings. If the null hypothesis is not rejected by a specific research study with low power, it is difficult to determine whether there is, in fact, no (or negligible) relationship in the population, or whether the study was not sensitive enough (power was too low) to detect the relationship actually present in the population. Reporting the power of a particular test provides us with at least some interpretation of the results, and guards against premature conclusions of “no effect.” The reported power levels, if low, may suggest additional research with more powerful studies rather than continued acceptance of the null hypothesis.

Medler, et al. (1981) suggest an interesting combination of the previous two uses of power analysis. They propose the use of post hoc power analysis in the planning stages of a research study, when the intent is to determine the probability of encountering a significant finding in a secondary analysis of previously collected data. Here the researcher has a given data set and wants to establish how feasible it will be to use the data to investigate some phenomenon. He or she will estimate the anticipated effect size, set $\alpha$ to its desired level, select the type of test that will be utilized, and, given the sample size of the data set, determine whether there is an acceptable level of power to conduct the study.

## Determination of Statistical Power During a Study

A third application of power analysis is its use in field experiments evaluating the impact of some program or innovation, where the design is a “case-flow design” (Medler, et al., 1981), with subjects trickling in over time. Here the traditional determination of how many subjects are needed to achieve adequate power cannot be done a priori, as cases are gained and lost as a consequence of real world dynamics. Rather, the critical question becomes how long the study must continue in order to achieve an adequate level of power. In the context of case-flow research designs, ongoing power analysis during the study can provide a rationale for ending the field experiment by establishing the analytic value of the next subject. Using power analysis, the minimum size of an effect that can be detected in the study’s current sample can be computed. As new subjects are added (and as statistical power increases concomitantly) the minimum effect size that can be detected is decreased.

The critical issue, however, is not to decrease this minimal detectable effect as much as possible but rather to determine whether the incremental improvement in power associated with more subjects is worth the marginal effort required to continue the study. As an example, Medler, et al. (1981) note that after 200 cases the total decrease in effect size (r-squared in this case) up to 1000 cases is only .03. Thus, the additional 800 subjects add very little to the study's ability to detect significant effects yet add considerably to the researcher's time and effort to process the cases.

A decision to terminate a study may also be warranted where subjects in the case-flow design have been lost through attrition. The net effect of attrition is typically devastating for the level of statistical power. For example, an acceptable level of power to detect an effect (r-squared of .026 with 300 cases) may become unacceptable through loss of subjects (r-squared becomes .073 with 150 cases) (Medler, et al., 1981). Thus, ongoing power analysis during a study allows the continuous monitoring of case-flow designs and the informed determination of the feasibility of terminating or continuing the study.

## Statistical Power in MIS Research

In this section we report on the results of a survey we undertook to determine the attention paid to the issue of statistical power in MIS research and to calculate the levels of statistical power characterizing published MIS studies. We then compare the MIS results against the mean levels of statistical power prevailing in fields that traditionally serve as referent disciplines for MIS researchers. We conclude the section by discussing some of the implications of our findings for progress in, and interpretation of, MIS research.

## Method

We wanted to assess the level of statistical power in a representative sample of MIS research and reviewed the issues of four major journals publishing MIS research over the five-year period from January 1980 to July 1985. The journals selected were: Communications of the ACM, Decision Sciences, Management Sciences, and MIS Quarterly. Only empirical studies were relevant, and, in particular, those employing inferential statistics. Sixty-three articles matched these criteria. Table 1 shows their distribution.

Table 1. Distribution of MIS Studies Employing Statistical Inference Testing: January 1980 - July 1985

<table><tr><td>Journal</td><td>Number</td><td>Percent</td></tr><tr><td rowspan="3">MIS Quarterly Communications of the ACM Management Science</td><td>27</td><td>42.9%</td></tr><tr><td>18</td><td>28.5%</td></tr><tr><td>9</td><td>14.3%</td></tr><tr><td>Decision Sciences</td><td>9</td><td>14.3%</td></tr><tr><td>TOTAL</td><td>63</td><td>100%</td></tr></table>

Both parametric and non-parametric tests were included, the power of the latter tests being determined by using analogous parametric tests where appropriate (Hays, 1981; Kraemer and

Thiemann, 1987; Welkowitz, et al., 1982). For example, the t-test for means approximates for the Mann-Whitney U test, the parametric F test for the Kruskal-Wallis H test, and so on. As noted in Cohen (1962) the effect of such approximations slightly overestimates the power of the tests. Overall, however, this positive bias is trivial.

Of the 63 articles selected, five include statistical tests for which appropriate power calculations are not possible, and hence these are not included in the sample. These studies utilized tests such as Wilk's lambda and ANAVA (sic) direction statistics. One article proves insufficient information to conduct a power analysis and is also excluded from the survey.

It should be noted that while most of the articles involve a number of significance tests, not all of these are equally relevant to the major hypotheses of the research. Only tests of the major hypotheses are included in the analyses. Table 2 presents the distribution of the types of statistical tests that constitute the final sample. While the Chi-squared test is a non-parametric one, it is a sufficiently well-known and utilized statistical procedure that we have analyzed it separately from the category of non-parametric procedures. The category of non-parametric tests shown in Table 2 includes the Mann-Whitney test, the Kruskall-Wallis test, and the Wilcoxon test.

Table 2. Distribution of Statistical Tests Employed in 57 MIS Studies

<table><tr><td>Statistical Test</td><td>Number</td><td>Percent</td></tr><tr><td>ANOVA</td><td>46</td><td>30.9%</td></tr><tr><td>Correlation</td><td>22</td><td>14.8%</td></tr><tr><td>T-test</td><td>21</td><td>14.1%</td></tr><tr><td>Chi-Square</td><td>20</td><td>13.4%</td></tr><tr><td>Non-Parametric</td><td>18</td><td>12.1%</td></tr><tr><td>Regression</td><td>13</td><td>8.7%</td></tr><tr><td>Partial Correlation</td><td>7</td><td>4.6%</td></tr><tr><td>Proportion</td><td>1</td><td>0.7%</td></tr><tr><td>Proportion Differences</td><td>1</td><td>0.7%</td></tr><tr><td>TOTAL</td><td>149</td><td>100%</td></tr></table>

As in past surveys of statistical power in other disciplines (Chase and Chase, 1976; Chase and Tucker, 1975; Cohen, 1962; Katzer and Sodt, 1973; Mazen, et al., 1987; Sawyer and Ball, 1981), the power of each test is determined by using the study's given sample size, setting the $\alpha$ level to the conventional level of .05, and choosing the non-directional critical region for all power computations. Because determining an appropriate effect size for each study would be impossible, we also followed prior power surveys in employing Cohen's (1977) definition of three levels of effect size (small, medium, and large) for different types of statistical tests. These effect-size levels make it possible to compare power levels across studies in this survey, as well as across surveys conducted in other disciplines.

## Results

The 57 selected studies yielded 149 statistical tests of the major hypotheses being investigated. Table 3 shows the distribution of mean sample sizes for the MIS studies by type of statistical test. As can be seen, regression, correlation, and Chi-squared analyses are the only ones attaining on average more than a hundred subjects. Caution, however, is needed in interpreting this data. The high standard deviation levels in many of the entries reveal a large amount of variation in sample sizes. For example, among the non-parametric subsample the average sample size is 93; yet this is misleading, as further investigation reveals that of the 18 non-parametric tests we examined, 13 have an average sample size of 14, while two have sample sizes of over 300.

Table 3. Distribution of Sample Sizes Occuring in 57 MIS Studies

<table><tr><td rowspan="2">Statistical Test</td><td colspan="2">Sample Size</td></tr><tr><td>Mean</td><td>Std. Dev.</td></tr><tr><td>Regression</td><td>216</td><td>163</td></tr><tr><td>Correlation</td><td>132</td><td>203</td></tr><tr><td>Chi-Square</td><td>119</td><td>79</td></tr><tr><td>Non-Parametric</td><td>93</td><td>165</td></tr><tr><td>ANOVA</td><td>64</td><td>79</td></tr><tr><td>Partial Correlation</td><td>47</td><td>14</td></tr><tr><td>T-test</td><td>45</td><td>41</td></tr><tr><td>Proportion</td><td>24</td><td>N.A.</td></tr><tr><td>Proportion Differences</td><td>18</td><td>N.A.</td></tr><tr><td>AVERAGE</td><td>84</td><td></td></tr></table>

N.A. = Tests for which there is only one subject in the sample and no standard deviation can be calculated.

Power values were determined for each of the 149 tests culled from the articles. The mean power of the tests at each of the three effect-size levels was determined via the use of Cohen's (1977) power tables. Table 4 presents the power distributions for the 149 statistical tests using Cohen's conventional values for small, medium, and large effect sizes.

\- Small Effect Size: The average statistical power of the tests when we estimated small effect sizes is conspicuously small at .19. This means that if we assume that the phenomena being investigated exhibit only small effects, then, on average, the MIS studies examined have only a one in five chance of detecting them. Table 4 shows that $99\%$ of the tests are below the .80 conventional power level, and $93\%$ have a less than 50 percent chance of detecting significant results.

\- Medium Effect Size: When we assume medium effect sizes, the average statistical power of the tests increases to .60. While this is an improvement over the .19 achieved by tests of small effects, the studies still have, on average, less than a two-thirds chance of detecting their phenomena. Table 4 indicates that of the tests examined, $34\%$ achieve the conventional .80 power level or better, and $60\%$ obtain a more than 50 percent chance of detecting significant findings.

\- Large Effect Size: The outlook improves substantially when we assume large effects. The average statistical power of the tests is .83. Table 4 shows that a respectable $66\%$ of the tests attain or exceed the .80 power level, and only $9\%$ have a less than 50 percent chance of correctly rejecting their major null hypotheses.

Table 5 lists the power of the studies by type of statistical test employed. With the exception of regression, none of the tests reaches the .80 power level (assuming medium effect sizes). ANOVA tests account for almost one-third of all MIS statistical analyses, yet their mean power level (assuming medium effect sizes) is only .56. Thus, only when one assumes that the effect being studied is so large as to make statistical testing unnecessary do MIS studies on average reach adequate power levels. Even then, 34% fall below the .80 level.

Table 4. Frequency and Cumulative Percentage Distribution of the Statistical Power of 57 MIS Studies\*

<table><tr><td rowspan="2">Stasticial Power Level</td><td colspan="2">Small Effect</td><td colspan="2">Medium Effect</td><td colspan="2">Large Effect</td></tr><tr><td>Frequency</td><td>Cumulative Percentage</td><td>Frequency</td><td>Cumulative Percentage</td><td>Frequency</td><td>Cumulative Percentage</td></tr><tr><td>.91 - .99</td><td>—</td><td>—</td><td>40</td><td>100%</td><td>90</td><td>100%</td></tr><tr><td>.81 - .90</td><td>2</td><td>100%</td><td>11</td><td>73%</td><td>8</td><td>40%</td></tr><tr><td>.71 - .80</td><td>—</td><td>—</td><td>8</td><td>66%</td><td>11</td><td>34%</td></tr><tr><td>.61 - .70</td><td>2</td><td>99%</td><td>18</td><td>60%</td><td>15</td><td>27%</td></tr><tr><td>.51 - .60</td><td>6</td><td>97%</td><td>12</td><td>48%</td><td>11</td><td>17%</td></tr><tr><td>.41 - .50</td><td>5</td><td>93%</td><td>6</td><td>40%</td><td>3</td><td>9%</td></tr><tr><td>.31 - .40</td><td>2</td><td>90%</td><td>21</td><td>36%</td><td>7</td><td>7%</td></tr><tr><td>.21 - .30</td><td>30</td><td>89%</td><td>20</td><td>22%</td><td>1</td><td>3%</td></tr><tr><td>.11 - .20</td><td>42</td><td>68%</td><td>11</td><td>9%</td><td>2</td><td>2%</td></tr><tr><td>.00 - .10</td><td>60</td><td>40%</td><td>2</td><td>1%</td><td>1</td><td>1%</td></tr><tr><td>TOTAL</td><td>149</td><td>—</td><td>149</td><td>—</td><td>149</td><td>—</td></tr><tr><td>Average Power</td><td colspan="2">0.19</td><td colspan="2">0.60</td><td colspan="2">0.83</td></tr></table>

\* Assuming small, medium, and large effect sizes, a non-directional test, and a 0.05 significance criterion.

## Statistical power in other disciplines

Our interest in the statistical power of MIS research was stimulated by a number of reviews of the statistical power levels of research in disciplines such as management (Mazen, et al., 1987), marketing (Sawyer and Ball, 1981), applied psychology (Chase and Chase, 1976), communication (Chase and Tucker, 1975), education (Brewer, 1972), and social psychology (Cohen, 1962). These are all disciplines that typically inform MIS research (Culnan, 1986).

Table 6 shows a comparison of the mean power levels obtained in published research of these various disciplines, including this survey. $^{4}$ While the statistical power of MIS research is comparable to or better than levels achieved by social psychology, education, and communication research, it falls below the levels attained by studies in applied psychology, marketing, and management. It might be further speculated that MIS studies would not appear in the median of this group if power surveys would be performed on more recent social psychology, education, and communication research. We would expect these three fields to have benefited from their earlier power reviews, with contemporary research displaying improved power levels.

Table 5. Distribution of Power Values of 57 MIS Studies by Statistical Test\*

<table><tr><td rowspan="3">Statistical Test</td><td colspan="6">Statistical Power Values</td></tr><tr><td colspan="2">Small Effect</td><td colspan="2">Medium Effect</td><td colspan="2">Large Effect</td></tr><tr><td>Mean</td><td>Standard Deviation</td><td>Mean</td><td>Standard Deviation</td><td>Mean</td><td>Standard Deviation</td></tr><tr><td>ANOVA</td><td>.20</td><td>19</td><td>.56</td><td>30</td><td>.79</td><td>25</td></tr><tr><td>Correlation</td><td>.19</td><td>17</td><td>.68</td><td>28</td><td>.89</td><td>18</td></tr><tr><td>T-test</td><td>.16</td><td>10</td><td>.53</td><td>27</td><td>.79</td><td>22</td></tr><tr><td>Chi-Square</td><td>.16</td><td>10</td><td>.67</td><td>32</td><td>.89</td><td>17</td></tr><tr><td>Non-Parametric</td><td>.16</td><td>165</td><td>.42</td><td>28</td><td>.69</td><td>22</td></tr><tr><td>Regression</td><td>.29</td><td>14</td><td>.91</td><td>12</td><td>.99</td><td>0.3</td></tr><tr><td>Partial Correlation</td><td>.23</td><td>9</td><td>.62</td><td>16</td><td>.93</td><td>8</td></tr><tr><td>Proportion</td><td>.10</td><td>N.A.</td><td>.36</td><td>N.A.</td><td>.77</td><td>N.A.</td></tr><tr><td>Proportion Differences</td><td>.09</td><td>N.A.</td><td>.32</td><td>N.A.</td><td>.67</td><td>N.A.</td></tr></table>

\* Assuming small, medium, and large effect sizes, a non-directional test, and a 0.05 significance criterion. N.A. = Tests for which there is only one subject in the sample and no standard deviation can be calculated.

Table 6. Interdisciplinary Comparison of Statistical Power Values\*

<table><tr><td rowspan="2">Discipline Surveyed</td><td rowspan="2">Number of Studies Surveyed</td><td colspan="3">Means of Statistical Power Values for Different Effect-Size Assumptions</td></tr><tr><td>Small</td><td>Medium</td><td>Large</td></tr><tr><td>Social Psychology (Cohen, 1962)</td><td>70</td><td>.18</td><td>.48</td><td>.83</td></tr><tr><td>Education (Brewer, 1972)</td><td>47</td><td>.14</td><td>.58</td><td>.78</td></tr><tr><td>Communication (Chase and Tucker, 1975)</td><td>46</td><td>.18</td><td>.52</td><td>.79</td></tr><tr><td>Applied Psychology (Chase and Chase, 1976)</td><td>121</td><td>.25</td><td>.67</td><td>.86</td></tr><tr><td>Marketing (Sawyér and Ball, 1981)</td><td>23</td><td>.41</td><td>.89</td><td>.98</td></tr><tr><td>Management (Mazen, et al., 1987)</td><td>84</td><td>.31</td><td>.77</td><td>.91</td></tr><tr><td>MIS (Baroudi and Orlikowski, 1989)</td><td>57</td><td>.19</td><td>.60</td><td>.83</td></tr><tr><td>AVERAGE</td><td>64</td><td>.24</td><td>.64</td><td>.85</td></tr></table>

\* Assuming small, medium, and large effect sizes.

This survey of MIS research studies has revealed, as have surveys of other disciplines, that the explicit discussion, use, and reporting of statistical power analysis are not common. In fact, representation of power issues is almost non-existent among the 57 studies examined. The inattention to statistical power and its consequences has implications for how MIS research should be interpreted.

## Discussion of implications

Sawyer and Ball (1981) discuss two major issues involving statistical power that are particularly relevant to research in MIS: interpretation and replication. This article reviews these and then discusses one other issue, the unit of analysis, that is of growing importance in the MIS field as it moves toward studying group decision systems, collaborative work, and organizational impacts of information technology.

## Interpreting Low Statistical Power

A research design should have adequate power to detect an anticipated effect size. If resources are limited and preclude attaining a satisfactory level of statistical power, the research is probably not worth the time, effort, and cost of inferential statistics. Under these circumstances, researchers need to carefully determine whether the costs involved in conducting the research are worth the substantial risk of not demonstrating any effect. The researchers should also determine whether the phenomenon can be investigated via some other research technique that does not rely on statistical power. (Later in this article, we offer some recommendations for researchers.)

If, however, the researcher persists with the study, at the very least he or she needs to be aware that the study's probability of rejecting a null hypothesis, even if it is false, is slight under conventional Type I error rates. Thus, if no effects are detected, the researcher needs to qualify his or her results by reporting the low power associated with the statistical tests. In particular, researchers in situations of low statistical power should not conclude (as was commonplace among the MIS studies examined) that because significance was not obtained the phenomenon does not exist. Indeed, we have found numerous instances of misstatements among

MIS researchers who assumed that non-significance indicated the absence of an effect. A more appropriate conclusion in such circumstances is to report that no significant findings were demonstrated in the current study, and that this may be due to the low power associated with the statistical tests employed.

Collectively, these misstatements and inconclusive findings may result in MIS researchers prematurely abandoning what may be promising areas of research. By incorrectly concluding that the phenomenon under investigation has no effect, they are discouraging researchers from pursuing this direction in other studies. An excellent illustration of this danger was recently presented by a study conducted by Robins (1988) into a specialized segment of the literature on depression. He was interested in determining why there was so much inconsistency across the many studies done in this area. His results are illuminating. Of the 87 studies he examines, only eight have adequate power (.80) to detect the small-to-medium population effect posited. Further, the few studies with fairly high power all report significant relationships, while the studies with low statistical power tend to find little support for the relationship. In the context of the present discussion on the impact of power, this should not be a surprise. Robins (1988) notes that “too few studies of the relations between depression and causal attributions have had adequate statistical power to provide meaningful conclusions” (p. 886). As a consequence, what appeared to be a wealth of studies with inconsistent findings proves to be only a small number of reliable, confirming studies.

We attempted to determine if a similar misconception of research exists within some area of the MIS discipline by surveying the literature on user involvement. $^{5}$ Ives and Olson (1984), in their well-known review of studies on user involvement and MIS success, report a number of studies that do not find significant relationships. (See their Table 3, p. 597.) We examined eight of these studies and found the average sample size to be relatively low at 36. Calculating the power of each of the statistical tests employed in these studies, we found that they have average power values of .12 (when small effect sizes are posited), .46 (when medium effect sizes are posited), and .82 (when large effect sizes are posited). $^{6}$ Reflecting on these findings, it appears that some future user involvement research effort may be necessary to determine which of the earlier findings are correct in their conclusions of no demonstrable effects, as opposed to those effects that were not found because the tests simply were not powerful enough to detect them.

## Replication Studies

Where a study fails to reject a null hypothesis due to low power, conclusions about the phenomenon are not possible. Replications of the study, with greater power, may resolve the indeterminancy. Replicating a study enables a researcher to better estimate the likely effect size and deliberately plan for adequate power to detect that effect size. Tversky and Kahneman (1971), however, conclude that researchers mistakenly tend to underpower attempted replications. They note that the statistical power of studies replicating non-significant research results needs to exceed that of the original study. MIS researchers should heed this advice.

## Unit of Analysis

Research conducted in the context of organizations often involves the use of groups as the unit of analysis. Within the MIS domain, studies of group DSS, the impacts of information technology on work groups, or the facilitation of collaborative activity are obvious candidates. The focus of attention in such studies is on group characteristics (e.g., the group's interaction, performance, operation, productivity, and so on). In such cases, questions about groups are not reducible to questions about the individual group members. Hence, selecting the individual subjects as the unit of analysis is inappropriate, even though this tactic increases sample size as well as the probability of detecting significant findings (Barcikowski, 1981). This is not only theoretically unjustified but also violates the important assumption of individual subject independence (subjects from a single group typically yield scores that are highly correlated) that characterizes some statistical procedures, such as the analysis of variance.

Barcikowski discusses power analysis in the context where the group is the unit of analysis, and the observations within a group are correlated. As may be anticipated, the sample size requirements (for comparable power levels) in such a situation exceed those needed by studies employing independent, individual subjects. Further, power declines as the relationship among the members of a group increases, as well as when the size of the group is enlarged. Interested researchers intending to use groups as the unit of analysis are referred to Barcikowski (1981) for a discussion of the appropriate procedures to be followed for statistical power analysis in such circumstances.

## Ways to Increase Statistical Power

This section explores several of the techniques that can be utilized by MIS researchers to improve the power of their statistical tests. Some examples of how these techniques might be used in the context of MIS research are provided. We also discuss some alternative research strategies, not dependent on statistical power, that may be useful in studying phenomena of interest to the MIS discipline.

## Increasing sample size

The most obvious way to increase the power of a study is to increase sample size. Large sample sizes are expensive, however, in terms of time, effort, and money. So an important moderator here is the researcher's objective. If the researcher's primary purpose is the precise estimation of the true parameter values, then the larger the sample size, the better (Hays, 1981). But this is not the purpose of many studies. Often, studies are exploratory in that the intent is to detect and map out the main relationships in some sub-area of a discipline. In this context, the research study serves as a guide, establishing research directions to be examined in future, more refined investigations. As a consequence, the largest possible sample size may not be an appropriate use of resources. So the issue of increasing sample size must reflect the intent of the research. As a general rule, a sample size should be large enough to give confidence that medium effects will be detected while being small enough so that trivial associations will be excluded from significance (Hays, 1981).

In many cases, however, increasing sample size, even though desirable, may be prohibitive or not possible in the time frame available. Fortunately, there are other techniques that can be used to improve the power of a study. Some of the techniques are as simple as choosing a different statistical technique or more carefully selecting one's sample. Following is a discussion of these techniques.

## Statistical tests

The recommendation here is to select the most powerful statistical test that is available and appropriate for the study at hand. In general, parametric tests are much more powerful than their analogous non-parametric tests (Kraemer and Thiemann, 1987) and should be employed when appropriate. It is important to keep in mind that different parametric tests assume different population distributions and conditions. For example, the F and t-tests assume a normal distribution in the population and equal variances among the group tested. Where these assumptions are violated, statistical texts (e.g., Hays, 1981) tend to recommend the use of non-parametric procedures. This, however, may not be appropriate. Cohen (1965) provides ample empirical evidence that a non-parametric test should be substituted for a parametric test only under conditions of extreme assumption violation, and that such violations rarely occur in behavioral or psychological research.

Additionally, non-parametric tests are not free of assumptions, as is often assumed by researchers. Cohen (1965) points out that the Wilcoxon and Mann-Whitney U (two popular non-parametric tests employed in MIS research) assume that the populations being sampled have identical distributions. He also notes that both tests are quite sensitive to violation of this condition. Given the robustness and enhanced power provided by parametric tests, researchers are encouraged to use the parametric test most appropriate for their study and resort to non-parametric procedures only in the rare case of extreme assumption violations.

The power of statistical tests can also be enhanced by retaining as much information as possible about the dependent variable. If this variable can reliably be measured along a continuum, it should not be reduced to a 5-point, 7-point, or dichotomous scale. To do so would be to lose information, necessitating a much larger sample size to achieve adequate power (Kraemer and Thiemann, 1987). In general, tests comparing data categorized into groups require larger sample sizes for adequate power than if that data had been measured continuously (Robins, 1988). Where continuous data can be naturally captured in this form, we encourage researchers to resist the temptation of force-fitting such data into artificial groups. Similarly, statistics that permit continuous data to be analyzed in continuous form, such as regression, should be used over those that require data to be divided in groups, such as the analysis of variance. Statistical procedures that force continuous data into groups inevitably result in a loss of power.

## Sampling plans

Underlying all power analysis computations is the assumption that the sample for the study is drawn at random from the population of interest. Clearly any deviations from this assumption will result in overestimation of the statistical power of the tests. Hence, researchers can ensure that their tests are as powerful as the computations indicate by randomly selecting subjects. We realize, however, that this is often not under the control of the investigators and that they typically have to settle for a convenience sample. In such cases, researchers performing a priori power analyses to determine necessary sample size need to remember that the n they compute will be underestimated.

An exception to the above random sampling rule is the employment of purposeful sampling strategies. In certain instances it is possible to select a sample based on some predictor value. To illustrate, suppose a researcher is interested in the effect of age on PC use. Rather than randomly selecting subjects regardless of age, the researcher can improve the power of his or her study by purposively selecting subjects depending on their ages. Two common sampling strategies are extreme group and rectangular sampling plans. The former strategy can greatly increase the power of studies where the relationship between the independent and dependent variables can be assumed to be linear, as is usually the case with psychological tests (Osburn and Greener, 1978). If the relationship cannot be assumed to be linear, then sampling to achieve a rectangular distribution may increase the power of the statistical tests (Osburn and Greener, 1978). In general, researchers are urged to utilize appropriate purposeful sampling strategies that are more powerful than regular random sampling. Where purposeful sampling is not possible, random sampling is preferred.

Another useful sampling technique to improve statistical power is increasing the homogeneity of the sample, which has the effect of reducing the standard error of the statistic (Sawyer and Ball, 1981). We detected several such attempts among the examined MIS research papers, although it was not entirely clear that statistical power was the rationale for such a strategy. For example, when studying IS personnel, it is possible to homogenize the sample by limiting it to systems development personnel (development programmers, analysts and project leaders) rather than including the systems programming, operations and technical staff. This would yield a much more heterogeneous sample. It is possible to homogenize the sample even further by including only development programmers or development analysts. The researcher must be aware of the tradeoffs of this technique, however; what is gained in statistical power is lost in generalizability.

The two sampling techniques just discussed must not be confused. The result of purposeful sampling is to obtain greater range on the variable(s) of interest. In contrast, increasing the homogeneity of the sample is conducted on variables not of central interest to the current study, hence resulting in a decrease in the standard error due to extraneous variance. It is important to note that researchers should not homogenize their sample on the dependent or independent variables, as this will result in a severe restriction in range and substantially reduce the power of the statistical tests.

## Research design

A clear ingredient in a successful and powerful study is an appropriate research design. This section reviews how the choice of variables, techniques for reducing error, and the purposeful allocation of subjects to treatments can all be used to enhance the power of a study.

## Choice of Variables

Kraemer and Thiemann (1987) note that the careful selection of which independent variables to include and exclude is crucial to raising the power of a study and the scope of its potential findings. They suggest that only “factors that are absolutely necessary to the research question, or that have a documented and strong relationship to the response, should be chosen, and these factors should be relatively independent of each other (to avoid problems of confounding or collinearity)” (p. 52). They also caution researchers that including marginally relevant factors decreases the power of the design, necessitating a much larger sample size. Another danger is a greater risk of non-significant results.

Kraemer and Thiemann provide an illustration of the impact of high intercorrelation among predictor variables (e.g., race, socioeconomic status, level of education, and family income). A study of the relationship between one of these predictor variables and the outcome variable required 20 to 50 subjects for adequate power, while a study investigating all four predictor variables simultaneously required 200 to 500 subjects for the same level of statistical power. As Kraemer and Thiemann recommend, “Choose a few predictor variables and choose them carefully” (p. 65).

## Reducing Error

A common-sense approach to increasing statistical power is to reduce the measurement error as much as possible. According to Sutcliffe (1980), “Lack of maintenance of equipment, sloppiness in taking readings, and so on, are all conducive to errors of measurement; and conversely, tighter control is aimed at their reduction” (p. 513). Therefore, any procedure to reduce such error that the researcher can employ in the design of his or her study will increase its power. In the context of MIS research, assume a researcher wishes to evaluate experimentally the ease of use of two different PC packages. It is important that all subjects use the same keyboards and monitors, and further, if they are already PC users, that the keyboards and monitors be ones they are currently using.

If some subjects are forced to use unfamiliar keyboards with different key layouts or monitors with different resolution or color, this may increase the “noise” in the experiment and reduce the effectiveness and the ability of the experiment to detect any true differences between the packages.

Another source of measurement error that can greatly reduce the power of a study is the unreliability of the measures. The statistical power of a study declines sharply as the reliability of the instrument degrades. Schmidt, et al. (1976) investigate statistical power in criterion-related studies and find that in validation studies, criterion unreliability and restriction in range dramatically increase the necessary sample size required to maintain adequate levels of power. To reduce the effect of unreliable measurement, Sutcliffe (1980) recommends making more than one observation per subject per treatment. While it is not possible for investigators to eliminate all error from individual observations, such use of multiple data collection techniques may average out the effects of the errors.

A particularly useful technique for reducing error is the utilization of a repeated measures design. With limited sample-size conditions and a low effect size, covariation between the pre-test and post-test measures greatly increases power (Arvey, et al, 1985). This is true because covariation between measures decreases the standard error of the statistic employed (Trattner and O'Leary, 1980). An example of such a design would be an MIS researcher evaluating how satisfied users are with a particular information system. In a repeated measures design the researcher repeatedly polls the users on how satisfied they are with the system (the dependent measure). Given that the same measure is used over time, the measure of satisfaction will be correlated with itself, and this will increase the power of the study by reducing the level of measurement error. It may not always be possible or desirable, however, to use such a design, as the research question may not lend itself to repeated measurement (Kraemer and Thiemann, 1987).

An effect similar to repeated measures is attainable by employing factorial designs that employ blocking, stratification, or matching criteria that can control for extraneous factors, such as gender, race, age, income, education, and so on. As Kraemer and Thiemann caution, however, the expected benefits of increased power will result only if these factors are judiciously chosen to be very highly correlated with the dependent variable and if they can be reliably measured. Where factors are redundant or correlate only moderately with the dependent variable, and if there is no increase in the number of subjects studied, the opposite effect will be achieved: the statistical power of the design will be less than that of the original, unblocked design.

Researchers can also reduce standard error and increase power by employing a research design that covaries a measure of pre-existing differences (Arvey, et al., 1985). Analysis of covariance (ANACOVA) is a statistical procedure permitting the designation of one or more independent variables as covariates, hence removing extraneous variation from the dependent variable. For example, in the evaluation study of the two PC packages, it is possible, using ANACOVA, to control for the subjects' level of computer expertise or some other pre-existing condition (such as experience with PCs) that the MIS researcher believes may confound the primary relationship being investigated (the comparative ease of use of the two PC packages). This procedure is recommended where appropriate, as it can enhance the power of the statistical test.

## Allocation of Subjects

Another important concern regarding research design is how the researcher allocates his or her subjects among the experimental treatments. With multiple groups, the researcher should always maintain equal n's in each group to maximize power (Schmidt and Hunter, 1978). As Medler, et al. (1981) observe, if the group sizes are unequal, attenuation of observed effect sizes can occur, which potentially undermines the statistical power of the analysis, regardless of the total n. When unequal n's are present, a subset of the subjects will contribute nothing to the study's power. Based on an example given by Medler, et al., imagine that a researcher is investigating the relationship between a training program and subjects' use of an information system. The researcher has 108 subjects in total, distributed across two groups; one receives the training (n = 86), and the other does not (n = 22). When the statistical power of a test with unequal n's is estimated, the harmonic mean is utilized. For this example the harmonic mean will be 35. $^{7}$ This study is equivalent to one with equal group sizes of 35, for a total of only 70 subjects. Thus, the skewed distribution of subjects between the groups “wasted” 38 cases. Had the 108 subjects been divided equally between the two groups (54 in each group), both the significance level and the statistical power of the study would have been enhanced.

Unequal sample sizes can also interact with the type of statistical test to deflate power even more. In factorial designs, unequal cell sizes may skew the marginal distributions of the factors, also attenuating the observed correlations and reducing the power of the study (Medler, et al., 1981). In factorial designs, if it is not possible to maintain equal n's, the researcher can minimize the diminution of power by obtaining proportional n's in the rows and columns. To illustrate, assume that in addition to training versus no training, the subjects in the above example are also split along prior computer experience into two groups, giving a two by two design: training × experience. If equal n's in the four cells are not possible, ensuring that the n's in each row and column are in proportion will also maximize statistical power. MIS researchers are better off spending time designing studies with equal or proportional n's, even though the n's may be smaller, than spending time and effort getting larger n's that result in unequal or disproportional groups. As demonstrated, the care with which a researcher designs his or her study can have a major effect on the statistical power of the study.

## Combining studies

One of the most frequently mentioned means of increasing power is combining studies of the same variable in a meta-analysis (Drasgow and Kang, 1984; Sawyer and Ball, 1981; Schmidt and Hunter, 1978; Trattner and O'Leary, 1980; Wing, 1982). The power of a meta-analysis study greatly exceeds that of any individual study (assuming no one study accounts for a disproportionate amount of the overall N) because the N of the meta-analysis is a function of the n's of the individual studies. Examples of such meta-analyses can be commonly found in other disciplines (e.g., Jackson and Schuler, 1985; Robins, 1988; Sweeney, et al., 1986). A few subfields within MIS have matured to the point that a large number of studies exist around a particular variable, as in the case of user involvement (Ives and Olson, 1984). It is possible to combine the studies of user involvement into one large meta-analysis study, as has been done by Pettingell, et al., (1988). These results allow the effects of the various independent variables on user involvement to be stated with much greater power and certainty. The process of combining such studies is not simple, however (O'Grady, 1982), and should only be performed when technically feasible. The interested reader is directed to Glass, et al., (1981) for a thorough treatment of meta-analytic procedures.

## Relaxing alpha

The convention of setting alpha to some predetermined level such as .01 or .05 has a long history in statistical inference testing (Cowles and Davis, 1982). Recently, however, researchers have begun to question the utility of such an approach and have indicated a need to “rationalize” research by viewing alpha as a variable, like any other, subject to adjustment (Cascio and Zedeck, 1983). Myers and Melcher (1969) note, “To set $\alpha$ at the same level, say 0.05 for all hypothesis testing situations is hardly rational. Rather, for some actions the probability of not taking the right action when the hypothesis is true should be small such as one out of 100 times; while for other statistical inference problems this alpha error should be rather large such as 30 or 40 percent” (p. B-35).

Cascio and Zedek (1983) suggest that the level of alpha should be determined by the relative seriousness of Type I and Type II errors. By using a fixed small value for alpha, researchers may be inappropriately increasing their chances of a Type II error. For example, assume Cohen's standard of setting $\beta$ to .20 and $\alpha$ to its usual .05. In doing so, we are in effect making the judgement that the danger of a Type I error is four times as serious as a Type II error. This may, in fact, not always be appropriate. In a preliminary, exploratory study, for example, where because of resource constraints, researchers are unable to obtain a large sample, it may be expedient to let $\alpha$ grow larger and keep $\beta$ small. This process avoids prematurely closing off avenues of study due to an inability to detect significance because of the small sample.

In certain areas of MIS research, small samples may be the norm when the subjects of interest are typically inaccessible, such as chief executive officers, or where the researchers wish to study the impacts of particular systems used only in a limited number of installations, such as new CASE tools, group DSS, and expert systems. In these cases, if the researchers wish to use inferential statistics, and if other techniques of increasing statistical power are inappropriate, they can let $\alpha$ increase above its usually low level to increase the statistical power of their study. Researchers should tell their readers, however, that the increase in $\alpha$ has raised the probability that a Type I error will occur. Thus, researchers must be cognizant of the costs of both Type I and Type II errors when setting $\alpha$ and $\beta$ levels.

## Directional vs. non-directional tests

It is possible to increase the power of a study by moving from a two-tailed to a one-tailed test of significance. For example, a one-tailed test with an $\alpha$ of .05 has the same power as a two-tailed test with an $\alpha$ of .10. In deciding between directional and non-directional tests, however, the primary guide must be the original question. Is the researcher seeking a directional difference between the variables, or a difference only in kind or degree? Given some level of $\alpha$ and some true alternative hypothesis, the power of a one-tailed test exceeds that of a two-tailed test if the effect is in the predicted direction. Clearly, when the effect lies in the opposite direction, the power of the test will be very low. As Hays (1981) notes, the researcher is penalized for framing a stupid question.

So when a researcher uses a directional test, the form of the question must indicate that the only alternative of logical or practical consequence occurs in the specified direction. Hays (1981) cites the case of researchers considering a new treatment for some disease for which the cure rate is known. Here the researchers are interested in determining whether the treatment improves the cure rate, and they have no interest in any possible reduction in the known cure rate. In this situation, the researchers are justified in focusing their resources on obtaining high levels of power to detect a truly better treatment and ignoring the fact that such a strategy yields very low power if the treatment is a poor one.

Most behavioral science research is framed in non-directional terms; indeed, Cohen (1965) advises researchers to avoid directional tests except in very narrow circumstances. A number of commentators (Hays, 1981; Schmidt, et al., 1976) note that directional tests are only valid where results in the opposite direction of any magnitude are not at all feasible, as might be the case in established subfields where there are legitimate prior hypotheses about the direction of the relationship. In general though, where researchers are asking questions such as "What is going on?" they should adopt the safe strategy of non-directional tests.

## Effect size

As noted in the previous sections, it is reasonable to expect the effect sizes that MIS researchers are investigating to be relatively small. Beyond the techniques discussed above, there is little that researchers can do in power-analytic terms to attenuate the inexorable dampening impact of small effect sizes on statistical power. However, as Cohen (1973) observes, there are other strategies available: "Obviously, the solution to the problem of very small ES [effect sizes] in behavioral science is to emulate the older sciences: strive toward developing the insights which lead to research procedures and instruments which make effects measurably large enough to be detected by experiments of reasonable size" (p. 228). As an illustration, astronomers for centuries have been developing better and more sensitive telescopes to detect stars of increasingly dimmer magnitude. MIS researchers should determine the extent to which they can heed Cohen's advice to make the effects they are interested in "bigger," rather than passively reconciling themselves to small effects.

## Alternatives to classical inference testing

To improve their ability to obtain meaningful results, MIS researchers might usefully adopt alternative research approaches. These alternative strategies do not depend on inferential statistics and, as a consequence, either alleviate or do not require consideration of statistical power. Some of these different approaches are outlined here.

One approach would be the utilization of Bayesian statistical procedures, which are much more flexible than classical inference statistics, as they do not force a reliance on a yes/no rejection of the null hypothesis. Bayesian statistics depart from classical inference statistics on two particular points (Pfaffenberger and Patterson, 1977). First, Bayesian statistics, unlike classical statistics, permit the use of subjective probability distributions in the construction of a test of a hypothesis or confidence interval. Second, Bayesian statistics permit probability statements to be made about possible values of the population parameters, while classical inference statistics require the population parameter to either equal some value or not (the dichotomous accept or reject situation). Illustrations of the use of Bayesian statistics in hypothesis testing can be found in Greenwald (1975).

A further departure from the classic statistical examination of phenomena would be the adoption of qualitative or interpretive research methodologies that provide alternatives to the statistical inference testing methodologies. Such alternative approaches offer many advantages to the researcher that stem from the in-depth, non-deterministic, contextual nature of such investigations. Researchers adopting such methodologies as case studies and ethnographies explore phenomena via multiple methods of data collection and analysis (semi-structured and unstructured interviews, observations, document review, and unobtrusive measures). For more information on these approaches to research, we refer interested readers to Benbasat, et al. (1987), Miles and Huberman (1984), and Yin (1984) for discussions of case studies, and Agar (1980), Lincoln and Guba (1985), Orlikowski, et al. (1988), and Van Maanen, et al. (1982) for discussions of ethnographic research. These alternative approaches to MIS research are particularly useful in the exploratory stages of specific subfields, such as the burgeoning field of collaborative work, or in those subfields where the phenomena investigated are complex, dynamic, and multi-faceted, as in investigations of the impacts of information technology and the implementation of information systems.

## Conclusions

In this article we have reviewed the issue of statistical power and drawn attention to its determinants and the many factors that influence the probability that a given study will detect significant findings. In a survey of five years of MIS research, we found the average levels of statistical power to be relatively low. Fortunately, the problem of power is one that can, with diligence, be remedied. We have presented a number of recommendations for improving the power of statistical tests and have offered some suggestions for adopting alternative research strategies.

Publication of research results is the main avenue for the dissemination of ideas in academic disciplines, including MIS. It thus behooves researchers to ensure that what is communicated will lead to increased understanding and facilitate others to build on the findings. Based on our review of five years of published MIS research in four journals, we have a few recommendations to authors and journal editors regarding the inclusion of certain kinds of information in journal articles. We urge that all published empirical studies report:

\- a detailed description of the sites or situations studied, as well as the measures employed and their particular psychometric properties;

\- the number and characteristics of subjects involved, including how they were selected and motivated to participate in the study;

\- the rationale of the power analyses (including the appropriate effect-size estimates) and the statistical power of the tests performed;

\- the sample effect-size levels actually obtained (e.g., expressed as proportion of variance measures), in addition to the significance information typically provided.

The value of reporting the actual effect sizes obtained in the current sample, in addition to estimated effect sizes, is explicated by Cohen (1973): "the sample ES [effect size], confidence-bounded, is a far better estimate of the population ES than the hypothesized ES which led to the power estimates" (p. 227). Reporting these values would provide an effect-size index that might usefully inform future research in an area (including any possible meta-analyses). The reporting of power levels allows readers to treat studies with low power cautiously while facilitating the interpretation of non-significant results; that is, by distinguishing non-significance that reliably indicates little or no effect from instances of inconclusive findings that can be attributed to low power.

Statistical power, if neglected, can have relatively negative, or at least indeterminate consequences for progress in MIS research. If statistical power is seriously attended to, however, it can become a valuable tool for MIS researchers, serving to improve the planning, conduct, reporting, and interpretation of MIS studies.

## Acknowledgements

The authors would like to thank the anonymous reviewers and the associate editor for their helpful comments. Thanks are also due to Jacob Cohen, Michael Ginzberg, and Hank Lucas for their suggestions on earlier drafts of this article.

## References

Agar, M.H. The Professional Stranger, Academic Press, New York, NY, 1980.

Arvey, R., Cole, D., Hazucha, J. and Hartanto, F. "Statistical Power of Training Evaluation Designs," Personnel Psychology (38:3), Autumn 1985, pp. 493-507.

Barcikowski, R. "Statistical Power with Group Mean as the Unit of Analysis," Journal of Educational Statistics (6:3), Fall 1981, pp. 267-285.

Benbasat, I., Goldstein, D. and Mead, M. "The Case Research Strategy in Studies of Information Systems," MIS Quarterly (11:3), September 1987, pp. 369-387.

Brewer, J. "On the Power of Statistical Tests in the American Educational Research Journal," American Educational Research Journal (9), 1972, pp. 391-401.

Cascio, W., Valenzi, E. and Silbey, V. "Validation and Statistical Power: Implications for Applied Research," Journal of Applied Psychology (63:5), October 1978, pp. 589-595.

Cascio, W. and Zedeck, S. “Open a New Window in Rational Research Planning; Adjust Alpha to Maximize Statistical Power,” Personnel Psychology (36:3), Autumn 1983, pp. 517-526.

Chase, L.J. and Chase, R.B. "A Statistical Power Analysis of Applied Psychological Research," Journal of Applied Psychology (61:2), April 1976, pp. 234-237.

Chase, L.J. and Tucker, R.K. "A Power-Analytic Examination of Contemporary Communication Research," Speech Monographs (42:1), March 1975, pp. 29-41.

Cohen, J. "The Statistical Power of Abnormal-Social Psychological Research: A Review," Journal of Abnormal and Social Psychology (65:3), August 1962, pp. 145-153.

Cohen, J. "Some Statistical Issues in Psychological Research" in Handbook of Clinical Psychology, B.B. Woleman (ed.), McGraw-Hill, New York, NY, 1965, pp. 95-121.

Cohen, J. "Statistical Power Analysis and Research Results," American Educational Research Journal (10:3), 1973, pp. 225-230.

Cohen, J. Statistical Power Analysis for the Behavioral Sciences, revised edition, Academic Press, New York, NY, 1977.

Cowles, M. and Davis, C. "On the Origins of the .05 Level of Statistical Significances, American Psychologist (37:5), May 1982, pp. 553-558.

Culnan, M. “Intellectual Development of Management Information Systems 1972-1982: Co-Citation Analysis,” Management Science (32:2), February 1986, pp. 156-172.

Drasgow, F. and Kang, T. "Statistical Power of Differential Validity and Differential Prediction Analysis for Detecting Measurement Nonequivalence," Journal of Applied Psychology (69:3), August 1984, pp. 498-508.

Friedman, H. "Magnitude of Experimental Effect and a Table for Its Rapid Estimation," Psychological Bulletin (70:4), October 1968, pp. 245-251.

Friedman, H. "Simplified Determination of Statistical Power, Magnitude of Effect, and Research Sample Sizes," Educational and Psychological Measurement (42:2), Summer 1982, pp. 521-526.

Glass, G., McCaw, B. and Smith, M.L. Meta-Analysis in Social Research, Sage Publications, Inc., Beverly Hills, CA, 1981.

Greenwald, A. “Consequences of Prejudice Against the Null Hypothesis,” Psychological Bulletin (82:1), January 1975, pp. 1-19.

Hays, W.L. Statistics for Psychologists, Holt, Rinehart and Winston Inc., New York, NY, 1963.

Hays, W.L. Statistics, 3rd edition, Holt, Rinehart and Winston Inc., New York, NY, 1981.

Ives, B. and Olson, M.H. "User Involvement and MIS Success," Management Science (30:5), May 1984, pp. 586-603.

Jackson, S. and Schuler, R. "A Meta-Analysis and Conceptual Critique of Research on Role Ambiguity and Role Conflict in Work Settings," Organizational Behavior and Human Decision Process (36:1), August 1985, pp. 16-78.

Katzer, J. and Sodt, J. "An Analysis of the Use of Statistical Theory in Communications Research," Journal of Communication (23:3), September 1973, pp. 251-265.

Keppel, G. Design and Analysis: A Researcher's Handbook, Prentice-Hall, Inc., Englewood Cliffs, NJ, 1973.

Kraemer, H.C. and Thiemann, S. How Many Subjects?: Statistical Power Analysis in Research, Sage Publications, Beverly Hills, CA, 1987.

Lincoln, Y.S. and Guba, E.G. Naturalistic Inquiry, Sage Publications, Beverly Hills, CA, 1985.

Mazen, A., Graf, L., Kellogg, C. and Hemmasi, M. "Statistical Power in Contemporary Management Research," Academy of Management Journal (30:2), June 1987, pp. 369-380.

Medler, J., Schneider, P. and Schneider, A. "Statistical Power Analysis and Experimental Field Research," Evaluation Review (5:6), 1981, pp. 834-850.

Meyers, B.L. and Melcher, A.J. "On the Choice of Risk levels in Managerial Decision-Making," Management Science (16:2), 1969, pp. B31-B39.

Miles, M.B. and Huberman, A.M. Qualitative Data Analysis, Sage Publications Inc., Beverly Hills, CA, 1984.

Myers, J.L. Fundamentals of Experimental Design, Allyn and Bacon, Boston, MA, 1980.

Nelson, N., Rosenthal, R. and Rosen, R.L. “Interpretation of Significance Levels and Effect Sizes by Psychological Researchers,” American Psychologist (41:1), November 1986, pp. 1299-1301.

O'Grady, K.E. "Measures of Explained Variance: Cautions and Limitations," Psychological Bulletin (92:3), November 1982, pp. 766-777.

Orlikowski, W.J., Baroudi, J. and Rosen, M. "Interpretivism as an Alternative IS Research Paradigm," unpublished paper presented at Academy of Management Meeting, Anaheim, CA, August 1988.

Osburn, H. and Greener, J. "Optimal Sampling Strategies for Validation Studies," Journal of Applied Psychology (63:5), October 1978, pp. 602-608.

Pettingell, K., Marshall, T. and Remington, W. "A Review of the Influence of User Involvement on System Success," Proceedings of the International Conference on Information Systems, Minneapolis, MN, December 1988, pp. 227-236.

Pfaffenberger, R. and Patterson, J. Statistical Methods for Business and Economics, Richard D. Irwin, Inc., Homewood, IL, 1977.

Robins, C.J. "Attributions and Depression: Why is the Literature So Inconsistent?" Journal of Personality and Social Psychology (54:5), May 1988, pp. 880-889.

Sawyer, A. and Ball, D. "Statistical Power and Effect Size in Marketing Research," Journal of Marketing Research (18:3), August 1981, pp. 275-290.

Schmidt, F. and Hunter, J. "Moderator Research and the Law of Small Numbers," Personnel Psychology (31:2), Summer 1978, pp. 215-232.

Schmidt, F., Hunter, J. and Urry, V. "Statistical Power in Criterion-Related Validation Studies," Journal of Applied Psychology (61:4), August 1976, pp. 473-485.

Stevens, J.P. "Power of the Multivariate Analysis of Variance Tests," Psychological Bulletin (88:3), November 1980, pp. 728-737.

Sutcliffe, J.P. "On the Relationship of Reliability to Statistical Power," Psychological Bulletin (88:2), September 1980, pp. 509-515.

Sweeney, P.D., Anderson, K. and Bailey, S. "Attributional Style in Depression: A Meta-Analytic Review," Journal of Personality and Social Psychology (50:5), May 1986, pp. 974-991.

Trattner, M. and O'Leary, B. "Sample Sizes for Specified Statistical Power in Testing for Differential Validity," Journal of Applied Psychology (65:2), April 1980, pp. 127-134.

Tversky, A. and Kahneman, D. "Belief in the Law of Small Numbers," Psychological Bulletin (76:2), August 1971, pp. 105-110.

Van Maanen, J., Dabbs, J. and Faulkner, R.R. Varieties of Qualitative Research, Sage Publications Inc., Beverly Hills, CA, 1982.

Webster, J. and Starbuck, W.H. "Theory Building in Industrial and Organizational Psychology," in International Review of Industrial and Organizational Psychology, G.L. Cooper and I.T. Robertson (eds.), John Wiley and Sons, Chichester, UK, 1988, pp. 93-138.

Welkowitz, J., Ewen, R. and Cohen, J. Statistics for the Behavioral Sciences, 3rd edition, Academic Press, New York, NY, 1982.

Wing, H. "Statistical Hazards in the Determination of Adverse Impact with Small Samples," Personnel Psychology (35:1), Spring 1982, pp. 153-163.

Yin, Robert K. Case Study Research: Design and Methods, Sage Publications, Beverly Hills, CA, 1984.

## About the Authors

Jack J. Baroudi is associate professor of information systems at New York University's Stern School of Business, where he also received his Ph.D. in 1984. His current research interests focus on the careers and management of information systems personnel, and discrimination issues in the information systems work place. Professor Baroudi's articles have appeared in MIS Quarterly, Communications of the ACM, The Journal of MIS, and OFFICE: Technology and People.

Wanda J. Orlikowski is assistant professor of information technologies at the Massachusetts Institute of Technology Sloan School of Management. She received her Ph.D. in information systems from New York University in 1988. Her current research focuses on the interaction between computer-mediated work and organizational structure, control, culture, communication, and production. Professor Orlikowski has published articles in The Journal of MIS, OFFICE: Technology and People, Research in the Sociology of Work, and Proceedings of AAAI.
