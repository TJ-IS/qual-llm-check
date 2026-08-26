---
otero_id: 26138
otero_key: "S3EQ2QBH"
title: "Statistical significance versus practical importance in information systems research"
authors: "Ananya Sen; Gary Smith; Claire Van Note"
year: "2022"
journal: "Journal of Information Technology"
doi: "10.1177/02683962211062236"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Statistical signi<sup>fi</sup>cance versus practical importance in information systems research

Ananya Sen, Gary Smith<sup></sup> and Claire Van Note

Journal of Information Technology 2022, Vol. 37(3) 288–300 © Association for Information Technology Trust 2021 Article reuse guidelines: sagepub.com/journals-permissions DOI: 10.1177/02683962211062236 Journals.sagepub.com/jinf ⑤SAGE

## Abstract

It has been reported that many empirical papers published in prestigious journals in economics, psychology, and medicine prioritize statistical signi<sup>fi</sup>cance over practical importance. We investigate whether the same is true of articles published in the MIS Quarterly, a top-tier information systems journal.

## Keywords

statistical signi<sup>fi</sup>cance, practical importance, p-values, effect size, quantitative research, Business intelligence and analytics

## Introduction

Research done in the field of Information Systems (IS) can transform the world but, in order to do so, managers need to know whether the findings are of real practical importance. Null hypothesis significance testing (NHST) does not address this question, since p-values do not tell us whether the estimated effects are substantial or trivial.

In a manifesto directed at IS researchers, Mertens and Recker (2020; abbreviated here as MR) argued that, “We observe that although debates about misinterpretations, abuse, and issues with NHST have persisted for about half a century, they remain largely absent in IS. We find this to be an untenable position for a discipline with a proud quantitative tradition” (p. 1072). One of their criticisms of NHST is that “the p-value is not an indication of the strength or magnitude of an effect” (p. 1076).

Similarly, Mohajeri et al. (2020; abbreviated here as MML) analyzed 27 empirical papers published in 2015 in MIS Quarterly, generally considered to be a top information systems journal (Dean et al., 2011; Lowry, et al., 2013), and concluded that “81% of papers give no consideration to the issue of practical significance at all” (p. 535).

We discuss the difference between statistical significance and practical importance and analyze all 306 empirical papers published in MIS Quarterly over a 10-year period (2010–2019). We find that most focus on statistical significance at the expense of practical importance.

a disease. Classical statisticians insist that we cannot put a probability on the effectiveness of the treatment. It either has an effect or it does not. So, instead, researchers specify a null hypothesis that the treatment has no effect and calculate the probability (the p-value) that the observed difference in recovery rates between the treatment and control groups would be so far from zero if the null hypothesis were true.

Nearly 100 years ago, Fisher (1926) endorsed a 5-percent rule for demonstrating statistical significance:

It is convenient to draw the line at about the level at which we can say: “Either there is something in the treatment, or a coincidence has occurred” … Personally, the writer prefers to set a low standard of significance at the 5 per cent point, and ignore entirely all results which fail to reach this level. (p. 504)

However, statistical significance does not gauge practical importance. In our example, did the medical treatment increase the recovery rate from 20 percent to 40 percent or from 20 percent to 21 percent? The p-value cannot answer this important question.

The distinction between statistical significance and practical importance has been known for decades. Gosset was not only the “Student” who derived the Student’s t-distribution that is often used to calculate p-values, he was also the Head Experimental Brewer at Guinness. He wrote that, in addition to saying that experimental results are statistically significant, researchers would like to be able to say that, “We have significant evidence that if farmers in general do this they will make money by $\mathrm { i t } ^ { \dag }$ (Pearson, 1939: 244). The same sentiment no doubt often applies to IS research.

Over the years, several other problems emerged in the way researchers used and interpreted NHST. In 1988, the International Committee of Medical Journal Editors (ICMJE) revised their Uniform Requirements for Manuscripts Submitted to Biomedical Journals: “Avoid sole reliance on statistical hypothesis testing, such as use of p values, which fail to convey important quantitative information.” (International Committee of Medical Journal, 1988: 260)

In the 1990s, the American Psychological Association and the American Psychological Society both considered banning NHST from psychology journals (Fidler et al., 2004). The fifth edition of the APA Publication Manual called confidence intervals that describe the size of an effect as “the best reporting strategy” (APA 2001: 22). The seventh edition states that if NHST is used, exact p-values should be reported instead of cutoffs like $p < 0 . 0 5$ (APA 2020: 87).

In 2016, the American Statistical Association (ASA) issued a statement on statistical significance and p-values espousing six principles that are intended to “improve the conduct and interpretation of quantitative science” (Wasserstein and Lazar, 2016: 131). Our interest here is with ASA’s principle 5: “A p-value, or statistical significance, does not measure the size of an effect or the importance of a result” (p. 132).

In 2019, more than 800 researchers endorsed a call by Amrhein et al. (2019) to “retire statistical significance and to use confidence intervals.”

## Statistical significance versus practical importance

Consider the multiple regression model

$$
y = \alpha + \beta_ {1} x _ {1} + \dots + \beta_ {k} x _ {k} + e\tag{1}
$$

The t-statistic for a test of the null hypothesis that a regression coefficient $\beta _ { i }$ is zero is equal to the ratio of the coefficient estimate to its standard error

$$
t = \frac {b _ {i}}{s _ {b _ {i}}}\tag{2}
$$

The standard error of the coefficient estimate is

$$
s _ {b _ {i}} = \frac {1}{\sqrt {n - 1}} \frac {s _ {e}}{s _ {x _ {i}}}\tag{3}
$$

where n is the number of observations, $s _ { e }$ is the estimated standard deviation of the error term, and $s _ { x _ { i } }$ is the standard deviation of explanatory variable i. Ceteris paribus, the standard error of the coefficient estimate decreases as the number of observations increases. This means that, unless the estimated coefficient is exactly zero, a sufficiently large sample will necessarily give a statistically significant association even if the magnitude of the coefficient is so close to zero that, for all practical purposes, it is unimportant.

More generally, the assessment of an estimated coefficient should consider whether its value is substantial and plausible. A highly statistically significant relationship between household income and spending (both measured in dollars) with a marginal effect equal to 0.01 would be of no practical importance. A marginal effect less than zero or larger than one would be a reason for distress, not celebration, because a statistically significant implausible coefficient signals something seriously wrong with the data or the model. Perhaps a decimal point was misplaced. Perhaps an important confounding variable was omitted. Instead of rushing off to publish counter-intuitive findings, we should investigate the reasons for the implausible results.

## Assessing practical importance

Practical importance cannot be gauged by a statistical yardstick but is, instead, a subjective decision that depends on the context and may vary from person. For example, statistical tests have frequently been accepted by U.S. courts as prima facie evidence of employment discrimination that violates Title VII of the Civil Rights Act of 1964. However, courts have also recognized that a statistically significant difference may not be of any practical importance. In Moore v. Southwestern Bell, 1979, a promotion test for clerks was passed by 453 of 469 whites (96.6 percent) and by 248 of 277 blacks (89.5 percent). The z-value was 3.91, which has a two-sided p-value of 0.000092; however, the court ruled that, even though the difference in pass rates was statistically significant, it was not substantial enough to prove discrimination.

A very different example is a test of cold-vaccine that involved 548 college students who believed themselves especially susceptible to colds (Diehl et al., 1938). The students who were given the vaccine averaged 1.6 colds while the students who were given an injection of plain water averaged 2.1 colds. The t-value was 6.46 with a twosided p-value of 0.0000000002; yet, the researchers concluded that “the effect is too small to be of practical importance.” Despite the overwhelming statistical evidence, the doctors apparently felt that an average of 0.5 fewer colds per year was not worth the trouble, expense, and possible side effects from taking the vaccine.

In the 1960s, a man named Willard H. Longcor contacted Harvard statistician Frederick Mosteller with an offer to record the results of a very large number of dice rolls as being either even or odd numbers. Longcor subsequently rolled 219 dice 20,000 times each, a total of 4,380,000 rolls, and observed 2,199,714 even numbers, which implies a 9.28 Z-value for a test of the null hypothesis that the probability of an even number is 0.50. (Iverson et al. 1971). The p-value is minuscule, but the observed frequency of even numbers was 0.502, which is arguably unimportant.

What these examples from very different fields demonstrate is that practical importance is fundamentally different from statistical significance and is necessarily subjective. Readers may well disagree about whether an estimated effect is of any practical importance, but researchers should describe the size of the effect in sufficient detail so that readers can make an informed assessment.

## Two information systems examples

Consider a study of the factors affecting the household adoption of smart metering technology (SMT) for monitoring electricity consumption (Wunderlich et al., 2019). The model uses several explanatory variables for a sample of German households to explain household intention to adopt SMT.

The results table (Table 3 in their paper) does not give p-values, but instead uses asterisks to identify the estimated coefficients that have p-values less than 0.10 or 0.05. The interpretation of the results similarly focuses on statistical significance. For example, one of the hypothesized explanatory variables is household income: “Consumers with higher income are able to spend on environmental friendly devices such as SMT and are more likely to adopt it.” The discussion of the results gives the estimated coefficient, 0.062, and notes that the p-value is less than 0.05, but does not discuss practical importance:

Among the different demographic and electricity consumptionrelated variables, we found that H5a, predicting the effect of income level on intention to adopt SMT (β = .062, p < .05) … [was] supported. (p. 683)

The authors also write that, “Consumers with higher income … are likely to adopt SMT” (p. 685), but they do not say how much more likely—they do not consider the practical importance of their finding.

An assessment of whether the effect of income on the intention to adopt SMT is substantial must take into account the units in which income and intention are measured. The authors write that, “Intention is the subjective probability that a person will perform a certain behavior” (p. 678); however, their intention variable is not a probability but, instead, the average value of each household’s response to these three questions:

(1) I can imagine using SMT regularly in my household.

(2) I plan to use SMT in the future.

(3) I intend to use SMT in everyday life.

Although it is nowhere mentioned in the paper, each of these questions was answered on a Likert scale of 1–7 (Wunderlich 2021). Their constructed intention variable has a mean 4.64 and a standard deviation of 1.76.

The income explanatory variable is defined as, “the average income of the consumers” (p. 678). The currency is not identified, but it is likely euros since this is a study of German households. We are not told whether it is weekly, monthly, or annual income and whether the data are recorded in euros, thousands of euros, or some other unit. The descriptive statistics table reports that the income variable has a mean of 4.27 and standard deviation of 1.39, suggesting that the data are monthly income, measured in thousands of euros.

If our assumptions are correct, this means that the regression equation predicts, ceteris paribus, that a 1000-euro increase in monthly household income will increase a household’s intention to adopt SMT on a 1–7 Likert scale by a very modest 0.062.

An alternative way of gauging practical importance is to calculate the elasticity ε at the mean values of the variables

$$
\varepsilon = \frac {\partial \mathbf {y}}{\partial x} \frac {\overline {{x}}}{y}\tag{4}
$$

Here, the elasticity of intention with respect to income is 0.057, which means that a 1 percent increase in monthly income is predicted to increase the value of the intention variable, measured on a 1–7 Likert scale, by 0.057 percent

$$
\varepsilon = \left| 0. 0 6 2 \frac {4 . 2 7}{4 . 6 4} \right| = 0. 0 5 7\tag{5}
$$

To us, the effect of income on intention, though statistically significant, is too small to be of any practical importance. Others may disagree, but this is a matter of subjective judgment, not p-values.

Another explanatory variable in this paper is the introjected perceived locus of control (PLOC), “which is characterized by feelings of misalignment of perceived social influences and personal values” (p. 675). The estimated coefficient for predicting intention to adopt SMT is 0.048 with a p-value less the 0.05, leading the authors to write that “the results surrounding introjected PLOC offer an important revision to the motivational models of the past by highlighting that context plays a very important role” (p. 687). Is the magnitude of the coefficient of sufficient practical importance to warrant an “important revision” because “context plays a very important role”?

Though not described in the paper, the authors measure introjected PLOC by the average of the answers to five questions using a Likert scale of 1–7. Since the introjected-PLOC explanatory variable and the intentionto-adopt dependent variable are both based on Likert scales, the elasticity is an appealing way to gauge whether the estimated effect is substantial. The introjected PLOC elasticity is even smaller than the income elasticity

$$
\varepsilon = \left| 0. 0 4 8 \frac {2 . 4 0}{4 . 6 4} \right| = 0. 0 2 5\tag{6}
$$

In contrast, the estimated elasticity of intention to adopt with respect to internal PLOC is 0.338, which is an order of magnitude higher than the elasticity with respect to introjected PLOC.

Our point is that in addition to statistical significance, it is useful to know whether the estimated effects are of any practical importance and it would be helpful if authors discussed this question so that readers would not have to do the detective work described here.

In sharp contrast, Yue et al. (2019) report their main results in a context that readers can use to assess practical importance (which they call “economically significant”):

More importantly, the number of DDOS (Distributed Denial of Service)-attack posts has a significant negative impact on the number of DDOS-attack victims. A 1% increase in DDOSattack posts decreases the number of DDOS-attack victims by 0.032%. Our dataset contains an average of 196 DDOS-thread– port-effective posts and 2.18 million victim IPs per day. This estimate implies that increasing the discussion by two posts per day would decrease the number of victim IPs by around 700 per day. This impact is economically significant. (p. 83)

## Effect sizes

Some IS researchers (e.g.,, Dimoka et al., 2012; Fang, et al., 2014; Siponen and Vance 2010) report the value of Cohen’s (1988) effect size index $f ^ { 2 }$ for multiple regression models, an index that is based on the square of the multiple correlation coefficient R

$$
f ^ {2} = \frac {R ^ {2}}{1 - R ^ {2}}\tag{7}
$$

Cohen also proposed measuring the effect size when the explanatory variables in set B are added to the explanatory variables in set A by comparing the squared multiple correlation coefficients

$$
f ^ {2} = \frac {R _ {A B} ^ {2} - R _ {A} ^ {2}}{1 - R _ {A B} ^ {2}}\tag{8}
$$

Cohen recommended the classification “conventions” shown in Table 1 corresponding to small, medium, and large effect sizes.

Although the label effect size suggests a measure of the magnitude of an effect, Cohen did not intend these indexes to gauge whether the explanatory variables have substantial effects on the dependent variable, but rather as assessments of how the correlation coefficients compare to other studies in the field. Thus, in choosing 0.36 as a medium effect size, he cited the observation of two psychologists, J. P. Guilford and Benjamin Fruchter, that correlations in psychological testing “may be expected in the range from .00 to .60, with most indices in the lower half of that range” (Cohen, p. 80). Regarding a benchmark for large effects in the behavioral sciences, Cohen remarked that,

Table 1. Small, Medium, and Large Effect Sizes

<table><tr><td></td><td>|R|</td><td> $f^{2}$ </td></tr><tr><td>Small</td><td>0.14</td><td>0.02</td></tr><tr><td>Medium</td><td>0.36</td><td>0.15</td></tr><tr><td>Large</td><td>0.51</td><td>0.35</td></tr></table>

this value (R = 0.51) seems about right for defining a large effect in the middle of the range of fields we cover. It will undoubtedly be often found to be small in sociology, economics, and psychophysics on the one hand, and too large in personality, clinical, and social psychology on the other. As always, this criterion is a compromise that should be rejected when it seems unsuited to the substantive content of any given investigation. (p. 414)

Consistent with his use of effect sizes to gauge the correlations to be expected in the behavioral sciences, Cohen recommends slightly lower cutoffs for simple regression: |R| = 0.10 for a small effect size, 0.30 for medium, and 0.50 for large.

The multiple correlation coefficient is equal to the correlation between the predicted and actual values of the dependent variable. Thus, Cohen’s effect size is a measure of a model’s goodness of fit, and not a measure of the practical importance of any of the model’s explanatory variables. MR recognize this distinction when they recommend that researchers, “Translate effect sizes back to real-world phenomena/measures to demonstrate practical significance” (p. 1087).

The effect size does not depend on the units the variables are measured in and tells us nothing about the practical importance of the model’s coefficients. In our earlier example, a simple regression model might have a 0.9 correlation between household spending and income, giving an extremely large effect size of 4.26. Yet the slope might show that the marginal effect of a thousand-dollar increase in income on spending is only \$1.00, which most would deem of little practical importance. Subjective opinions—not statistical measures like p-values, correlations, or effect sizes—are needed to judge practical importance.

A straightforward way of helping readers assess the practical importance of a model’s coefficients is to report the predicted marginal effects of ceteris paribus changes in the explanatory variables on the model’s dependent variable, similar to our calculations of the predicted effect of an increase in monthly income on a household’s intention to adopt SMT. In some cases, marginal elasticities may be more informative. Table 2 compares the marginal effects and elasticities for several popular regression models. In cases where the model is nonlinear or there are interaction terms, marginal effects can be calculated at the mean values or for a variety of representative values of the explanatory variables.

Table 2. Marginal Effects and Elasticities for Several Regression Models

<table><tr><td>Model</td><td>Marginal Effect $\left( \frac{\partial y}{\partial x} \right)$ </td><td>Elasticity $\left( \frac{\partial y}{\partial x} \frac{x}{y} \right) b_1(x/y)$ </td></tr><tr><td> $y = a + b_1x + b_2z$ </td><td> $b_1$ </td><td> $b_1(x/y)$ </td></tr><tr><td> $y = a + b_1x + b_2x^2$ </td><td> $b_1 + 2b_2x$ </td><td> $(b_1 + 2b_2x)(x/y)$ </td></tr><tr><td> $y = a + b_1x + b_2z + b_3xz$ </td><td> $b_1 + b_3z$ </td><td> $(b_1 + b_3z)(x/y)$ </td></tr><tr><td> $y = a + b_1\ln[x] + b_2\ln[z]$ </td><td> $b_1/x$ </td><td> $b_1/y$ </td></tr><tr><td> $\ln[y] = a + b_1x + b_2z$ </td><td> $b_1y$ </td><td> $b_1x$ </td></tr><tr><td> $\ln[y] = a + b_1\ln[x] + b_2\ln[z]$ </td><td> $b_1y/x$ </td><td> $b_1$ </td></tr></table>

## The neglect of practical importance

Economists have been sharply and repeatedly criticized by McCloskey (1985, 1999, 2002) for confusing statistical significance with practical importance (what she calls “oomph”). An analysis of empirical articles published in the American Economic Review, which is considered to be one of the most prestigious economics journals, found that 70 percent of the papers published in the 1980s did not distinguish between statistical significance and practical importance (McCloskey and Ziliak, 1996) and that 82 percent of the 1990s papers made the same error (Ziliak and McCloskey, 2004).

Ziliak and McCloskey (2008) report that a widespread focus on statistical significance rather than practical importance has also been found in studies of dozens of journals in the fields of psychology, education, and epidemiology (Fidler et al., 2004; Savitz et al., 1994; Vacha-Haase et al., 2000).

MR’s analysis of 43 highly cited papers in top-tier information systems journals does not explicitly tabulate how often papers neglect to discuss the practical importance of their estimates; however, their proposed guidelines state that researchers must not, “Conclude anything about scientific or practical importance based on statistical significance or lack thereof” (p. 1087).

## Mohajeri, Mesgari, and Lee

We noted earlier that MML looked at 27 empirical papers published in MIS Quarterly in 2015 and found that 22 (81 percent) “give no consideration to the issue of practical significance at all” (p. 535). However, their definition of practical significance is problematic in that it is not at all what has historically been meant by practical importance.

MML argue that researchers should consider three aspects of their empirical findings: statistical significance, practical significance, and relevance. We agree with their notion that statistical significance involves the conventional reporting of p-values.

Their definition of practical significance, however, is very different from what McCloskey calls oomph, MR call the “magnitude of an effect,” the ASA statement calls “the size of an effect,” and we call practical importance. MML define practical significance as the “research impressiveness of statistical results” (p. 528), which can be measured by a “broad range of statistical measures” (p. 535), including Cohen’s $\boldsymbol { \mathrm { f } } ^ { \bar { 2 } } , \boldsymbol { \mathrm { R } } ^ { 2 } , \boldsymbol { \mathrm { x } } ^ { 2 }$ , log-likelihood ratio, Akaike information criterion, and Bayesian information criterion (p. 524). As discussed above, Cohen’s effect sizes and other statistics related to goodness-of-fit do not measure practical importance. Indeed, MML acknowledge that “we can certainly envisage situations where a small effect magnitude can in fact denote a high substantive importance” (p. 544).

MML describe their third criterion, relevance, as follows: “we consider the relevance of an independent/ mediating variable to be concerned with the understandability, and when appropriate, actionability, of the variable in the eyes of nonacademic stakeholders” (p. 535).

They give a hypothetical example involving a multiple regression equation in which the dependent variable is an individual’s proficiency in the use of a firm’s business intelligence (BI) program and the explanatory variables are the person’s age and gender. They argue that the coefficients of these two explanatory variables are not relevant because,

the firm does not consider the factors, indicated by the independent variables, to be actionable. Specifically, the firm does not consider it feasible to change an employee’s age or gender, or consider it ethical to select an employee based on age or gender. (p. 532)

Table 3. Survey Questions

<table><tr><td>Does the paper ...</td></tr><tr><td>1. avoid using statistical significance as the criterion of importance?</td></tr><tr><td>2. avoid using the word significant in ambiguous ways?</td></tr><tr><td>3. include the units and descriptive statistics for all variables?</td></tr><tr><td>4. discuss whether the signs and magnitudes of the estimated coefficients are plausible?</td></tr><tr><td>5. report p-values instead of asterisks?</td></tr><tr><td>6. report confidence intervals for parameters?</td></tr></table>

Suppose, however, that older workers turn out to be more proficient than younger workers. Even if the firm does not hire on the basis of age, it could use the empirical results to estimate the value of long-term contracts, retirement programs, and other compensation packages that increase longterm employee retention.

Or suppose that all employees are given a training program and it is discovered that user proficiency is related to age and gender, specifically, that females are less proficient than men and that older workers are less proficient than younger workers. The firm may want to investigate if there are biases in the training program that hold back women and older workers.

Another situation might involve a training program conducted by a manager named Riley in which age and gender are important predictors of post-training proficiency. Now suppose that Riley leaves the company, the program is taken over by Jordan, and the average proficiency score of employees taking the training program plummets. Is the decline due to the changing age/gender demographics of people taking the program or to the fact that Jordan is running the program instead of Riley? The multiple regression model, using Riley-era data, provides an answer in that it predicts the proficiency scores, taking age and gender into account. If the actual scores with Jordan running the program are lower than the predicted scores, this is evidence that Jordan is not doing as good a job as Riley.

Authors should surely discuss the practical implications of their research, but we do not believe that all research must be relevant in the narrowly defined sense used by MML.

## Methods

We constructed the six-item questionnaire shown in Table 3 which we believe reflects sound statistical practices for empirical papers.<sup>1</sup>

1. Does the paper avoid using statistical significance as the criterion of importance? This is the primary concern of McCloskey and Ziliak, who prioritize practical importance over statistical significance. Our view is that both are important. Consider an A/B test of two web page layouts with a sample of size two—one user is sent to one page and buys something, while the other user is sent to the other page and does not buy anything. We would be reluctant to conclude that the first page is better because it has more oomph, with a 100 percent success rate, compared to a 0 success rate for the second page. To make a sensible choice between the two layouts, we would prefer a substantial difference in user behavior and a persuasively low p-value.

2. Does the paper avoid using the word significant in ambiguous ways, meaning statistically significant in one sentence and of practical importance in another? There should be a clear distinction between statistical significance and practical importance so that readers immediately know which is meant when words like significant, important, and supported are used.

3. Does the paper include the units and descriptive statistics for all variables? The units that the variables are measured in are helpful for interpreting the results; so are descriptive statistics like the mean, median, standard deviation, interquartile range, minimum, and maximum. In addition, descriptive statistics can help identify misplaced decimal points, unintentional negative signs, and other issues with the data. For example, a study of the incomes of U.S. military veterans noticed that the lowest income was zero and, on closer inspection, that nearly 20 percent of the income values were zeros. The analysis was redone, this time distinguishing between people who were employed and those who were not (Smith and Cordes, 2019).

4. Does the paper discuss whether the signs and magnitudes of the estimated coefficients are plausible; for example, reporting marginal effects and elasticities when relevant? Estimated coefficients with oomph and low p-values are nonetheless problematic if the coefficients have implausible signs or magnitudes.

5. Does the paper report p-values instead of asterisks? There is not much difference between p-values of 0.048 and 0.052, but there is a big difference between p-values of 0.048 and $2 . 8 \times 1 0 ^ { - \tilde { 3 } 5 }$ . The use of cutoffs $( \mathrm { e . g . , } \ast \mathrm { : } p < 0 . 0 5 ; \ast \ast \mathrm { : } p < 0 . 0 1 )$ to dichotomize the results into “statistically significant” or “not statistically significant” encourages the ill-founded belief that it is important to count the number of p-values below an arbitrary dividing line.

6. Does the paper report confidence intervals for parameters? Reporting that a 95% confidence interval for a coefficient is 4.72 ± 0.31 is far more informative than simply reporting that the p-value is less than 0.05.

The three authors independently read each paper in its entirety and used the six-item questionnaire in Table 3 to analyze all 306 empirical papers published in MIS Quarterly during the 10-year period, 2010 through 2019. Any disagreements were resolved by the senior author (Smith) rereading the paper.

## Results

A full report of our assessments is here. There will inevitably be some disagreements about yes/no judgments, and we welcome any suggestions regarding the choices we made.

The 306 empirical papers published in MIS Quarterly during this 10-year period generally follow a laudable template: research question, literature review, theoretical background, statement of hypotheses to be tested, methods, results, and discussion. However, our overall conclusion is that the papers typically focus on a tabulation of the number of statistical significant coefficients and do not report p-values, confidence intervals, or (most importantly) marginal effects or elasticities in ways that allow readers to assess the practical importance of the results.

A table of descriptive statistics was included in 74.2 percent of the papers. However, for our other five questions, the answers were no far more often than yes. We found that 78.1 percent of the papers prioritized statistical significance over practical importance and 73.9 percent did not discuss whether the signs and magnitudes of the estimated coefficients are plausible. Only 9.8 percent avoided using the word significant in ambiguous ways and, coincidentally, only 9.8 percent reported p-values instead of asterisks or cutoffs. Finally, we found that 87.3 percent of the papers did not report any confidence intervals, either numerically or in figures.

## Question 1

Question 1 (Does the paper avoid using statistical significance as the criterion of importance?) was intended to assess the prioritization of statistical significance over practical importance. We found that most papers prioritized statistical significance.

Some papers focused on the number of items on their list of research hypotheses that were confirmed, as determined by measures of statistical significance with little concern for practical importance; for example,

Table 5 summarizes the converged results of the model. As we can see, the fixed effects of apps, off-hour accesses, conf, offsite accesses, and log (DeptSize) all significantly support H1, H2, H3, H4, and H5(a). The cross-level interaction terms are significant, except Apps\*Log (DeptSize), therefore supporting H6(c), H6(d) H6(e), and H6(f), but not H6(b). (Wang et al., 2019: 613)

Some papers misinterpreted a lack of statistical significance as evidence that there was no effect; for example, in the absence of statistical significance, Sivan et al. (2019) wrote that,

taken together, the results of this experiment suggest that making the infringing nature of some links more noticeable to users through the use of a flag has no impact on their propensity to consume infringing versus legal content. (p. A12)

Some incorrectly compared the causal effects of explanatory variables based on statistical significance:

We found that for EPC-H, task performance depended only on run count (visual association) and not on AOI percentage duration (attention). (Bera et al., 2019: 14)

Some papers included or omitted variables based on statistical significance:

The quadratic model explained significantly higher variance than the linear model (F-test value = 3.54, p < 0.05). We also tested a cubic model to check whether it explains more of the variance, but no cubic terms were significant. (Nishant et al., 2019: 815)

Some papers misinterpreted Cohen’s effect size as a measure of practical importance:

The huge effect sizes further demonstrate the considerable impact of data collection choices on IQ. (Lukyanenko et al., 2019: 638)

Some papers gauged the importance of variables by the reduction in mean squared error:

[A]nalysis of covariance test was performed to compare Model 4, which includes the RF and its interaction term, with its nested counterpart in Model 3. The partial F-test (5.41, p < 0.01) showed that Model 4 achieved significant improvement in explanatory power for purchase frequency over Model 3. (Wu et al., 2019: 755–756)

Overall, the 78.1 percent no answers to Question 1 are consistent with the numbers McCloskey and Ziliak found for papers published in the American Economic Review and with the numbers reported for other journals. The elevation of statistical significance over practical importance is evidently widespread.

## Question 2

Question 2 (Does the paper avoid using the word significant in ambiguous ways?) was intended to assess how clearly the authors communicated the distinction between statistical significance and practical importance. Overall, the word significant generally seemed to refer to statistical significance using a criterion of p < 0.05. However, that interpretation was seldom explicit and we judged that in 90.2 percent of the papers, significant could be interpreted in multiple ways. For example, this passage seems to be describing a substantial effect, but may be based on p-values:

Specifically, our findings show the significance of active involvement from followers in such relationships. (Jiang et al., 2019: 12–13)

Similarly, this passage explicitly says “significant impact” and “significant effects,” but is probably referring to p-values:

Our results show that the way technology is designed to present articles has a significant impact on their believability and the subsequent behaviors that the believability influences.…We also found that source ratings purportedly from a panel of experts hired by Facebook had significant effects on the believability of articles. (Kim and Dennis, 2019: 1035)

## Question 3

Question 3 (Does the paper include the units and descriptive statistics for all variables?) was intended to assess whether readers are given enough information about the variables in order to make informed judgments about the coefficient estimates. Reasonable people may well disagree about, say, whether a coefficient is plausible and substantial but, as in the earlier SMT example, knowledge of the units in which the variables are measured and the typical levels and variation are essential for such judgments. A solid 74.2 percent of the papers we surveyed did so, often using a standard table showing the means and standard deviations of the variables and the pairwise correlation coefficients.

## Question 4

Question 4 (Does the paper discuss whether the signs and magnitudes of the estimated coefficients are plausible?) was intended to assess whether the paper discusses the estimated relationships in a way that allows readers to judge whether the results are reasonable, with practical importance being a component of reasonable results. Models are presumably constructed because the authors believe that the relationships among the explanatory and dependent variables are of practical importance, so that if an estimated relationship turns out to be of no practical importance, this contradicts the researcher’s expectations (Smith 2020).

Table 4 (discussed below) shows a typical reporting format. Overall, we found 73.9 percent of the papers deficient regarding question 4. Instead of showing examples of papers that did not assess the reasonableness of the estimated coefficients, we give an example of the useful information that is conveyed by a discussion of the signs and magnitudes of the estimated coefficients:

[F]or firms experiencing low levels of NET (i.e., 1 SD below mean), a change in Board Independence from 0% to 100% leads to a 4.38 percentage point decrease in ROA (p < 0.01), equivalent to a reduction of \$335.17 million in operating income before depreciation (OIBDA) when total assets are evaluated at the mean level. In contrast, at high levels of NET (i.e., 1 SD above mean), a change in Board Independence from 0% to 100% results in a 5.92 percentage point increase in ROA (p < 0.01), equivalent to a gain of almost \$480.05 million in OIBDA on average. To illustrate the marginal effects in a more intuitive manner, in Figure 1 we plot the predicted levels of ROA as a function of board independence under high versus low levels of NET (using a sample median split), along with 95% confidence intervals. (Pan et al., 2018: 989)

## Question 5

Question 5 (Does the paper report p-values instead of asterisks?) was intended to assess the extent to which the results are presented as if research is a contest in which success is measured by the number of p-values below a cutoff like 0.05. An explicit reporting of the actual p-values would be more useful for readers who are pondering whether the reported results can be explained away by coincidence. The use of a multiple-asterisk notation (such as $^ { * } p < 0 . 0 5 ; ~ ^ { * * } p < 0 . 0 1 ; ~ ^ { * * * } p < 0 . 0 0 1 )$ provides some guidance about the low p-values, but it would be more informative to show these values. If a p-value is larger than 0.05, it would be good to know if the p-value was 0.08 or 0.80. Unfortunately, 90.2 percent of the papers followed the convention of simply reporting asterisks or parenthetical inequalities, like (p < 0.05).

For example, Table 4 shows how Wunderlich et al. (2019: 684) summarized the main results of their study of the variables that influence household adoption of smart metering technology (SMT). The placement of the R<sup>2</sup> values at the top of the table suggests that goodness of fit is the most important criterion for judging models—more important than the coefficients of the explanatory variables.

Table 4. Results from the Hierarchical Regression

<table><tr><td></td><td>Model 1</td><td>Model 2</td></tr><tr><td> $R^2$ </td><td>.575</td><td>.587</td></tr><tr><td> $\Delta R2^2$ </td><td></td><td>.012**</td></tr><tr><td colspan="3">Motivational variables:</td></tr><tr><td>Attitude</td><td>.403**</td><td>.393**</td></tr><tr><td>Internal PLOC</td><td>.359**</td><td>.337**</td></tr><tr><td>External PLOC</td><td>.069**</td><td>.080**</td></tr><tr><td>Introjected PLOC</td><td>.042*</td><td>.048**</td></tr><tr><td colspan="3">Household demographic variables:</td></tr><tr><td>Income</td><td></td><td>.062**</td></tr><tr><td>Household Size</td><td></td><td>-.010</td></tr><tr><td>Age</td><td></td><td>-.071**</td></tr><tr><td>Education</td><td></td><td>-.004</td></tr><tr><td colspan="3">Electricity-consumption related variables:</td></tr><tr><td>Average electricity costs per month</td><td></td><td>-.030</td></tr><tr><td>Annual electricity consumption</td><td></td><td>.023</td></tr><tr><td>Number of times switched energy supplier</td><td></td><td>.019</td></tr><tr><td colspan="3">Privacy-related variables:</td></tr><tr><td>Perceived privacy risk</td><td></td><td>-.043*</td></tr><tr><td colspan="3">Innovation-related variables:</td></tr><tr><td>Inherent innovativeness</td><td></td><td>.048**</td></tr><tr><td>Willingness to pay for energy efficient innovations</td><td></td><td>-.003</td></tr></table>

\*p < .1

What also stands out in Table 4 is the image created by the large number of coefficients with asterisks (12 of 18, including 8 of 8 for the motivational variables), which conveys the visual impression of a successful model. Careful readers might notice that a single asterisk refers to p < 0.10 rather than $p < 0 . 0 5$ and, also, that we are not told whether the p-values are one-tailed or two-tailed.

The accompanying description of the results does little more than recite the incomplete information in the table:

As Hypothesis 1 predicted, the results indicated that consumers’ attitude toward SMT would have a positive influence on the individual’s intention to adopt SMT (β = 0.393, p < 0.05). Hypothesis 2 predicted that internal PLOC would have a positive influence on the individual’s intention to adopt SMT. The results supported this prediction $( \beta = 0 . 3 3 7 , p < 0 . 0 5 )$ Hypothesis 3, which predicted that external PLOC would have a positive influence on individuals’ intention to adopt SMT, was also supported $( \beta = 0 . 0 8 0 , p < 0 . 0 5 )$ . Hypothesis 4 predicted a negative influence of introjected PLOC on individuals’ intention to adopt SMT. This prediction was not supported, as our findings suggest a positive effect $( \beta = 0 . 0 4 8 , p < 0 . 0 5 )$ . In addition, among the different demographic and electricity consumption-related variables, we found that H5a, predicting the effect of income level on intention to adopt SMT (β = 0.062, p < 0.05), H5c, predicting the effect of age on intention to adopt $( \beta = - 0 . 0 7 1 , p < 0 . 0 5 )$ , H7, predicting the effect of perceived privacy risk on intention to adopt $( \beta = - 0 . 0 4 3 , p < 0 . 1 )$ , and H8a, predicting the effect of innovativeness on intention to adopt $( \beta = 0 . 0 4 8 , p < 0 . 0 5 )$ , were supported. In contrast, H5b, predicting the effect of household size on intention to adopt $( \beta = - 0 . 0 1 0 , n . \mathrm { ~ s . } ) .$ , and H5d, predicting the effect of education, were not supported (β = 0.004, n. s.). Similarly, H6a–c, predicting the effects of average monthly electricity costs on intenton to adopt (β = 0.030, n. s.), average annual electricity consumption on intention to adopt $( \beta = 0 . 0 2 3 , n . \ \mathrm { s . } )$ , and the extent of switching of energy suppliers on intention to adopt, were not supported (β = 0.019, n. s.). Finally, individuals willingness to pay (i.e., H7b) was also not found to have the predicted effect on intention to adopt SMT (β = 0.003, n. s.). (682–683)

The inclusion of the anticipated signs of the coefficients is welcome, but there is no need to repeat the coefficient estimates and remind readers which estimates earned an asterisk. An interpretation of the magnitudes of the coefficients would have been much more informative. We noted earlier that the 0.062 income and 0.048 introjected PLOC coefficients seem to be of little practical importance. What about the other coefficients?

## Question 6

Question 6 (Does the paper report confidence intervals for parameters?) was intended to assess whether the results are presented in ways that help readers assess the magnitudes of the estimates, taking into account the possible effects of sampling error. We recorded a yes answer if confidence intervals were reported or shown in a figure for any of the coefficients. Nonetheless, 87.3 percent of the papers did neither. Those papers that did include confidence intervals typically used figures that required readers to estimate the numerical values from the axes.

## Comparison of our results with MML

MML’s Table 5 reports their evaluation of the 27 quantitative articles published in MIS Quarterly in 2015, and we can compare their judgments to our assessments of these same articles. We do not assess relevance, and MML do not assess our criteria 1, 2, 3, 5, and 6. The closest comparison is column 3 in MML’s Table 5 (“Does the paper offer any judgment, with supporting rationale, indicating whether the [reported effect sizes] are practically significant?”) with our criterion 4 (“Does the paper discuss whether the signs and magnitudes of the estimated coefficients are plausible?”). Even if the authors of these 27 papers did not make an explicit judgement about whether the signs and magnitudes of the estimated coefficients are plausible (which is, after all, a subjective assessment), we judged a paper to have satisfied our criterion 4 if the author discusses the size of the coefficients in terms that can be assessed by readers.

Overall, MML gives a yes answer to 5 of 27 papers, while we give a yes answer to 7 papers. In two cases, MML judged yes while we judged no; in four cases, MML judged no while we judged yes. We will first consider the two cases where MML judged yes while we judged no.

Tian and Xu (2015) reported Cohen’s $\mathrm { F } ^ { 2 }$ values, and MML judged this a satisfactory measure of practical significance, but we did not consider $\mathrm { F } ^ { 2 }$ values to be a measure of practical importance, for reasons explained earlier. MML also gave a yes assessment for Kankanhalli et al. (2015) because the authors gauged measurement invariance for two models by reporting that the difference between the comparative fit index (CFI) was less than 0.01. We gave a no assessment because the authors did not discuss the estimated magnitudes of the effects of the explanatory variables on their dependent variables.

The first of the four cases where MML judged no while we judged yes is Wang et al. (2015). Our positive assessment was based on the fact that the estimated coefficients were interpreted with statements such as this:

Our results indicated that the business value of an application (BVM) increased the risk of an application experiencing unauthorized attempts $( \widehat { \beta } _ { 1 } ^ { } = 0 . 2 2 )$ , supporting H1. One level increase in BVM increased the instantaneous probability (or the hazard rate) of an application experiencing unauthorized attempts by 24 percent on average with everything else being equal. (p. 104)

The second disagreement was Faraj et al. (2015), where we were persuaded by statements such as this

To interpret the coefficients in Table 4, we calculated the percentage change in expected count of leader identifications. For example, in Model 3, we find that for one standard deviation increase in knowledge contribution, sociability, and structural social capital, the expected average number of times a leader is identified by others increases by 67.3 percent, 12.5 percent, and 34.1 percent, respectively. (p. 403)

The third disagreement was Rai et al. (2015), where we were convinced by statements such as this:

When firm i in year t is one standard deviation above the industry mean in its investments to develop interfirm process integration capability (i.e., z = 1 for INTER) and increases reliance in that year by 10 percent on the wholesale market for electricity it sells to customers (i.e., 0.1 increase in MSI), then in the next year it realizes a 0.11 percent increase in ROA $( \mathrm { \beta } \mathrm { \times I N T E R } \times \mathrm { M S I } \mathrm { = } 0 . 0 1 1 \times 1 \times 0 . 1 = 0 . 0 0 1 1 ) .$ . (p. 879)

The fourth disagreement was Ramasubbu et al. (2015), which included statements like this:

Confirming hypothesis 1, the results indicate that a percentage increase in requirements volatility leads to about a 13 percentage-point increase in process diversity $( \beta = 0 . 1 2 9 ; p <$ 0.001). (p. 799)

## Recommendations

We are not critiquing the models, hypotheses, data, or statistical procedures in the papers we reviewed but, rather, we are encouraging IS authors to present their results in meaningful ways that may make their conclusions more persuasive to managers who might implement some of their findings. Such changes by IS authors can be encouraged and reinforced by editors and reviewers. If editors insist that authors de-emphasize artificial cutoffs for statistical significance and discuss the practical importance of their results, authors will surely do so.

We recommend these guidelines that follow from our six questions:

1. Statistical significance should not be the primary measure of a model’s success. P-values are needed to help assess the extent to which chance might explain the results, but a model’s importance depends on much more than low p-values.

2. Avoid using the word significant in ambiguous ways. Our preference is to describe practical importance with words like economically significant, meaningful, important, or substantial and to avoid the phrase statistically significant entirely because it reinforces the idea that there is a strict cutoff between significance and insignificance.

3. Show the units and descriptive statistics for all variables, most conveniently in a table that facilitates comparisons.

4. Report marginal effects and/or marginal elasticities that help readers assess the plausibility and practical importance of the results.

5. Report p-values instead of asterisks or parenthetical inequalities based on arbitrary demarcations, so that readers can judge for themselves whether chance is a viable explanation of the results.

6. Report confidence intervals that help readers gauge the uncertainty in the estimated coefficients.

Our recommendations are generally consistent with those of MR (1083–1086) and MML (p. 546). One substantive difference is that MR propose that researchers, “Eliminate NHST as an approach to data analysis.” We discourage arbitrary cutoffs, but we believe that conventional p-values are often helpful for ascertaining whether the reported effects of a treatment or explanatory variable can be attributed to sampling error. The second substantive difference is that both MR and MML recommend always reporting effect sizes which we believe are too often misinterpreted as measures of practical importance.

## Conclusion

In order to investigate whether IS journals prioritize statistical significance over practical importance, we looked at all 306 empirical papers published in MIS Quarterly over the 10-year period, 2010 through 2019.

Articles published in the MIS Quarterly typically report whether the p-values for the model’s coefficients are below specified thresholds for statistical significance, and do not report the actual p-values that would allow readers to judge for themselves whether chance is a plausible explanation for the observed statistical relationships. Nor do the papers report confidence intervals that would allow readers to assess the uncertainty in the estimated coefficients. Nor do they report marginal effects or elasticities that would allow readers to gauge the practical importance of the coefficients.

As a top-tier journal, MIS Quarterly presumably publishes exceptional research and sets an example for other IS journals. For IS to achieve its goals of using technology to improve society, managers need to be able to assess the practical importance of IS research. Authors, reviewers, and editors can facilitate such assessments by moving beyond arbitrary cutoffs for statistical significance and discussing whether the estimated effects are substantial enough to make a real difference.

## Declaration of con<sup>fl</sup>icting interests

The author declared no potential conflicts of interest with respect to the research, authorship, and/or publication of this article.

## Funding

The author received no financial support for the research, authorship, and/or publication of this article.

## ORCID iD

Gary Smith  https://orcid.org/0000-0002-5173-2741

## Notes

1. We initially included two other questions (7. Does the paper avoid comparing the importance of variables based on the absolute size of the p-values? 8. Does the paper avoid choosing variables for inclusion solely on the basis of statistical significance?) but, while reading the papers, decided that (7) was too ambiguous and (8) was too difficult to assess, since preliminary models may not be reported in published papers.

## References

Amrhein V, Greenland S and McShane B (2019) Scientists rise up against statistical significance. Nature 567(7748): 305–307.

APA (2001) Publication Manual of the American Psychological Association. 5th Edition. Washington, DC: American Psychological Association.

APA (2020) Publication Manual of the American Psychological Association. 7th Edition. Washington, DC: American Psychological Association.

Bera P, Soffer P and Parsons J (2019) Using eye tracking to expose cognitive processes in understanding conceptual models. MIS Quarterly 43(4): 1105–1126.

Cohen J (1988) Statistical Power Analysis for the Behavioral Sciences. 2nd edition. Hillsdale, NJ: Lawrence Erlbaum Associates.

Dean DL, Lowry PB and Humpherys S (2011) Profiling the research productivity of tenured information systems faculty at U.S. institutions. MIS Quarterly 35(1): 1–15.

Diehl HS, Baker AB and Cowan DW (1938) Cold Vaccines. Journal of the American Medical Association 111: 1168–1173.

Dimoka A, Hong Y and Pavlou PA (2012) On product uncertainty in online markets: theory and evidence. MIS Quarterly 36(2): 395–426.

Fang Y, Qureshi I, Qureshi I, et al. (2014) Trust, satisfaction, and online repurchase intention: the moderating role of perceived effectiveness of e-commerce institutional mechanisms. MIS Quarterly 38(2): 407–427.

Faraj S, Kudaravalli S, Kudaravalli S, et al. (2015) Leading collaboration in online communities. MIS Quarterly 39(2): 393–412.

Fidler F, Thomason N, Cumming G, et al. (2004) Editors can lead researchers to confidence intervals, but can’t make them think. Psychological Science 15(2): 119–126.

Fisher RA (1926) The arrangement of field experiments. Journal of the Ministry of Agriculture of Great Britain 33: 503–513.

International Committee of Medical Journal (1988) Uniform requirements for manuscripts submitted to biomedical journals. international committee of medical journal editors. European Journal of Haematology 41: 98–108.

Iverson GR, Longcor WH, Mosteller F, et al. (1971) Bias and runs in dice throwing and recording: a few million throws. Psychometrika 36(1): 1–19.

Jiang Q, Tan C, Sia CL, et al. (2019) Followership in an opensource software project and its significance in code reuse. MIS Quarterly 43(4): 1303–1319.

Kankanhalli A, Ye H, Ye H, et al. (2015) Comparing potential and actual innovators: an empirical study of mobile data services innovation. MIS Quarterly 39(3): 667–682.

Kim A, Dennis AR and Dennis AR (2019) Says who? The effects of presentation format and source rating on fake news in social media. MIS Quarterly 43(3): 1025–1039.

Lowry PB, Moody GD, Moody GD, et al. (2013) Evaluating journal quality and the association for information systems senior scholars’ journal basket via bibliometric measures: do expert journal assessments add value?. MIS Quarterly 37(4): 993–1012.

Lukyanenko R, Parsons J, Parsons J, et al. (2019) Expecting the unexpected: effects of data collection design choices on the quality of crowdsourced user-generated content. MIS Quarterly 43(2): 623–647.

McCloskey DN (1985) The Rhetoric of Economics. Madison, WI: University of Wisconsin Press.

McCloskey DN (1999) Other Things equal: cassandra’s open letter to her economist colleagues. Eastern Economic Journal 25(3): 357–363.

McCloskey DN (2002) The Secret Sins of Economics. Chicago, IL: Prickly Paradigm Press.

McCloskey DN and Ziliak ST (1996) The standard error of regressions. Journal of Economic Literature 34(1): 97–114.

Mertens W, Recker J and Recker J (2020) New guidelines for null hypothesis significance testing in hypothetico-deductive is research. Journal of the Association for Information Systems 21(4): 1072–1102.

Mohajeri K, Mesgari M and Lee AS (2020) When statistical significance is not enough: investigating relevance, practical

significance, and statistical significance. MIS Quarterly 44(2): 525–559.

Nishant R, Srivastava SC, Srivastava SC, et al. (2019) Using polynomial modeling to understand service quality in egovernment websites. MIS Quarterly 43(3): 807–826.

Pan Y, Huang P, Huang P, et al. (2018) Board independence and firm performance in the it industry: the moderating role of new entry threats. MIS Quarterly 42(3): 979–1000.

Pearson ES (1939) “Student” as statistician. Biometrika 30(3/ 4Jan): 210–250.

Rai A, Arikan I, Arikan I, et al. (2015) Fit and misfit of plural sourcing strategies and IT-enabled process integration capabilities: consequences of firm performance in the U.S. electric utility industry. MIS Quarterly 39(4): 865–885.

Ramasubbu N, Bharadwaj A, Bharadwaj A, et al. (2015) Software process diversity: conceptualization, measurement, and analysis of impact on project performance. MIS Quarterly 39(4): 787–807.

Savitz DA, Tolo K-A and Poole C (1994) Statistical significance testing in the American journal of epidemiology, 1970- 1990. American Journal of Epidemiology 139(10): 1047–1052.

Siponen M and Vance A (2010) Neutralization: New insights into the problem of employee information systems security policy violations. MIS Quarterly 34(3): 487–502.

Sivan L, Smith MD and Telang R (2019) Do search engines influence media piracy? Evidence from a randomized study. MIS Quarterly 43(4): 1143–1154.

Smith G (2020) Data mining fool’s gold. Journal of Information Technology 35(3): 182–194.

Smith G and Cordes J (2019) The 9 Pitfalls of Data Science. Oxford, UK: Oxford University Press.

Tian F, Xu SX and Xu SX (2015) How do enterprise resource planning systems affect firm risk? post-implementation impact. MIS Quarterly 39(1): 39–60.

Vacha-Haase T, Nilsson JE, Reetz DR, et al. (2000) Reporting practices and APA editorial policies regarding statistical significance and effect size. Theory & Psychology 10(3): 413–425.

Wang J, Gupta M, Gupta M, et al. (2015) Insider threats in a financial institution: analysis of attack-proneness of information systems applications. MIS Quarterly 39(12): 91–112.

Wang J, Shan Z, Gupta M, et al. (2019) A longitudinal study of unauthorized access attempts on information systems: the role of opportunity contexts. MIS Quarterly 43(2): 601–622

Wasserstein RL and Lazar NA (2016) The ASA statement on p-Values: context, process, and purpose. The American Statistician 70(2): 129–133. DOI: 10.1080/00031305.2016. 1154108.

Wu J, Huang L, Huang L, et al. (2019) Operationalizing regulatory focus in the digital age: evidence from an e-commerce context. MIS Quarterly 43(3): 745–764.

Wunderlich P (2021) e-Mail Correspondence. October 22.

Wunderlich P, Veit DJ, Veit DJ, et al. (2019) Adoption of Sustainable Technologies: A Mixed-Methods Study of German Households. MIS Quarterly 43(2): 673–691.

Yue WT, Wang Q, Wang Q-H, et al. (2019) See No Evil, Hear No Evil? Dissecting the Impact of Online Hacker Forums. MIS Quarterly 43(1): 73–95.

Ziliak ST and McCloskey DN (2004) Size matters: the standard error of regressions in the american economic review. The Journal of Socio-Economics 33(5): 527–546.

Ziliak ST and McCloskey DN (2008) The Cult of Statistical Significance. Ann Arbor, MI: The University of Michigan Press.
