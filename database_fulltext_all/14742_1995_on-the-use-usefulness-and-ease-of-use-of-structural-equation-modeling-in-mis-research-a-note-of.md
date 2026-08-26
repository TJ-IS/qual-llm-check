---
otero_id: 14742
otero_key: "MPRXTSQR"
title: "On the Use, Usefulness, and Ease of Use of Structural Equation Modeling in MIS Research: A Note of Caution"
authors: "Wynne W. Chin; Peter A. Todd"
year: "1995"
journal: "MIS Quarterly"
doi: "10.2307/249690"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# On the Use, Usefulness, and Ease of Use of Structural Equation Modeling in MIS Research: A Note of Caution

By: Wynne W. Chin
Faculty of Management
University of Calgary
Calgary, Alberta
CANADA
chin@acs.ucalgary.ca

Peter A. Todd
School of Business
Queen's University
Kingston, Ontario K7L 3N6
CANADA
toddp@post.queensu.ca

Keywords: Technology acceptance model, structural equation modeling, confirmatory factor analysis.

ISRL Categories: GB02, A107, AI0403.1, AI0606

## Introduction

Structural equation modeling (SEM) using LISREL, EQS, PLS or other second generation data analysis techniques is increasingly being applied in MIS research. These techniques are important because they provide powerful ways to address key IS research problems such as understanding IT usage. However, they may lead to inappropriate conclusions if statistical criteria are permitted to drive analysis and override substantive understanding of a problem. The purpose of this note is to suggest the need for caution in the application of structural equation modeling and, in particular, to emphasize the need for substantive knowledge to drive modeling, exploration, and interpretation of results. The application of SEM in the absence of well-developed substantive knowledge can lead to equivocal results and may distract researchers from promising research paths.

An examination of two related publications appearing in the MIS Quarterly (Adams, et al., 1992; Segars and Grover, 1993) provides an illustration of some potential pitfalls associated with data-driven SEM. Adams, et al. (1992) provide a replication and independent validation of the ease of use (EOU) and usefulness (U) scales developed by Davis (1989) and Davis, et al. (1989) as the basis for the Technology Acceptance Model (TAM). Using conventional construct validation techniques such as multi-trait multi-method analysis and exploratory factor analysis, Adams, et al. (1992) conclude that Davis' EOU and U scales are psychometrically sound. Then, using structural equation modeling, they examined the relationship between EOU, U, and IT usage for various technologies and conclude that the relationships between the constructs are equivocal.

Segars and Grover (1993) provide a critique of Adams, et al., correctly noting that unless the measurement model, which postulates the relationship between observed measures (or indicators) and their underlying constructs, is both reliable and valid, its application in testing structural relationships may lead to equivocal results. This can occur due to a confounding of substantive and measurement issues. Segars and Grover (1993) go on to provide an excellent discussion of the merits of using SEM as a tool for construct validation. Then, to more fully examine the possibility of measurement problems, using the Adams, et al., data, they provide a revalidation of the EOU and U scales by performing a Confirmatory Factor Analysis (CFA). They conclude that there are measurement problems that the conventional construct validation techniques employed by Adams, et al., did not uncover. We agree with this basic conclusion, but disagree with their attribution for the underlying causes of the problem.

Segars and Grover (hereafter S&G) attribute these measurement problems to, among other issues, the fact that a two-factor model consisting of ease of use and usefulness did not adequately fit the data. To identify the sources of the poor fit, S&G performed an exploratory analysis of the electronic mail data collected by Adams, et al., guided by multiple empirical indicators of model misspecification provided by LISREL. They found a better-fitting model by eliminating two observed measures and then splitting the items used to measure perceived usefulness into two factors. One factor was identified as usefulness and the other as effectiveness. The new three-factor model (including usefulness, effectiveness, and ease of use) was then confirmed by cross validation with the Adams, et al. (1992) voice mail data (S&G, p.523). However, it is unclear both what the substantive interpretation for this three-factor model is and how, if at all, the effectiveness factor might be incorporated into TAM. Since empirical tests of TAM (Adams, et al., 1992; Davis, 1989; 1993; Davis, et al., 1989; Hendrickson, et al., 1993; Mathieson, 1991) have, for the most part, been supportive of the model, it is important to examine the dimensionality of usefulness more closely.

Having done this, we derive two conclusions. First, as stated above, we agree with S&G that there were measurement problems in the Adams, et al., data; in our view these problems are likely due to a problematic item in the usefulness scale. Second, we believe that the conclusion that the usefulness scale includes two separate dimensions is likely incorrect. Furthermore, we believe that this conclusion resulted from the way in which the CFA was conducted and, more importantly, because statistical results were used to drive decisions about the identification of constructs. Specifically, there are four issues that lead us to question their conclusions:

1. The cross validation was not based on a sample of independent respondents and is thus biased toward confirmation of any model derived from one sample and applied to the other.

2. The assessment of overall model fit for the two-factor model (i.e., usefulness and ease of use) and the three-factor model (i.e., usefulness, effectiveness, and ease of use) were confounded by changing scales (through item deletion) and constructs in an additive fashion.

3. The sample size in the calibration set (the electronic mail sample) was too small to provide a stable solution for the cross validation and thus may represent a chance event.

4. Most importantly, there was no substantive theoretical rationale provided for the distinction between the usefulness and effectiveness constructs. Rather, model modifications and identification of the effectiveness construct were guided largely by statistical considerations.

Each of these points is expanded upon below. Then, to more fully examine whether the usefulness scale proposed by Davis (1989) is multidimensional, the results of a separate CFA is provided using an independent data set drawn from 259 new voice mail users. The results of this analysis suggest that the Davis usefulness scale is, indeed, unidimensional.

## A Methodological and Substantive Critique

## Point 1: inappropriate cross validation

Cross validation addresses the question of how well a solution obtained by fitting a model to a given sample will fit an independent sample from the same population. It typically begins by randomly splitting a sample into two subsamples. This provides two independent subsamples sharing similar statistical properties. One subsample is then used as a calibration set for model parameter estimation. These parameter estimates are then validated by holding them constant and applying them on the second subsample, which is referred to as the validation set. This is done to test the predictive accuracy of a fitted model, which may have provided a good fit to one data set by capitalizing on the peculiar characteristics of that data set. If the model is valid, the exact parameter estimates from the first data set should predict relationships in the new sample as well. Thus, cross validation can allow us to assess how well various models fit the "population" model.

A key assumption in using this approach is that the subsamples contain independent observations (Mosier, 1951). In the S&G analysis, the electronic and voice mail samples are not statistically independent. Specifically, the 68 respondents in the voice mail sample all provided responses for the electronic mail sample as well (Adams, et al., p. 230). This overlap in respondents has the potential to bias the results in favor of the validation of any data-driven model.

In addition, S&G did not follow the traditional approach of "tight" cross validation, where the parameters obtained in the calibration set are fixed for the validation set, and model fits are then compared (Cudeck and Browne, 1983; MacCallum, et al., 1994). Instead, S&G performed a "loose" form of cross validation, which sets all parameters free to be estimated with the validation set. Such a procedure automatically biases the results toward the more complex model, in this case the two-factor usefulness/effectiveness model, since the $\chi^2$ test statistic must always produce a lower value (and thus, better fit indices) for the more complex model. This situation is analogous to the increase in $R^2$ that will occur when variables are added to a regression model.

## Point 2: item and construct confounds

In our view, a key finding of S&G is that the poor fit obtained for the Adams, et al., data is due to the presence of a third underlying construct they term "effectiveness." S&G also note that another potential source of inadequate fit were two poor indicators (one for usefulness and one for ease of use). However, the analysis does not conclusively confirm the three-factor model since the re-analysis combines changes in the formation of the constructs and changes in the scales in an additive fashion, first splitting usefulness into two constructs, then subsequently eliminating items from the usefulness and ease of use scales. Thus, the analysis suggests that all three changes together lead to an acceptable model fit. It does not directly support the conclusion that the addition of a third factor alone leads to an acceptable model fit. Indeed, S&G (1993, p. 522) note that a three-factor model based on the original scales, without item dele tion, though improved over the two-factor model, still resulted in a poor overall model fit. Our own re-analysis suggests that item deletion alone would provide an acceptable fit for a measurement model, with usefulness represented as a single factor.

## Point 3: likelihood of capitalization of chance

MacCallum, et al. (1992, p. 490) suggest that there ought to be “skepticism about generalizability of models resulting from data-driven modifications of an initial model.” Specification searches, such as those performed by S&G, typically show inconsistent and unstable outcomes for sample sizes of 100 to 400 observations (MacCallum, 1986). Subsamples of observations drawn from a larger sample will often suggest different modifications (MacCallum, et al., 1992). In other words, such specification searches produce unstable results that may highlight chance patterns in the data. Therefore, it is possible that the suggested separation of usefulness and effectiveness, which was driven by a specification search on a relatively small sample, may be due to chance.

## Point 4: lack of substantive knowledge and theoretical justification

While we have pointed out certain technical limitations in the analysis, the key point that concerns us is the lack of a substantive, theoretical justification for the separation of usefulness and effectiveness. S&G (p. 524) state that there exists a “certain degree of face validity” to the identification of the new effectiveness construct. It is not clear what the basis is for this statement. To our knowledge, there has not been any prior work to suggest how effectiveness is conceptually distinct from the “perceived usefulness” construct. No definition of the effectiveness construct is provided, nor is it clear how to distinguish effectiveness from usefulness.

According to Davis (1989, p. 320), perceived usefulness is defined as "the degree to which a person believes that using a particular system would enhance his or her job performance."

This is clearly reflected in the wording for the three items specified for that construct (e.g., "Using . . . would make it easier to do my job"). There are three main facets to these items (the behavior of system use, the context of "my job," and the positive expectation linking system use to job performance). The items specified for effectiveness seem to share the same properties ("Using . . . would enhance my effectiveness on the job"; Using . . . would improve my job performance"). Thus, it is unclear how these two items differ conceptually from the other three and thus, how effectiveness and usefulness might differ conceptually. Our argument is simply that they do not and that the distinction may be due to statistical artifact. That such an outcome may occur when employing SEM techniques to drive model respecification is well documented. As MacCallum, et al. (1992) note, the methodological literature in SEM

... is replete with warnings that modifications must be substantively justified ... If a parameter is to be added to a model, the researcher must be able to provide a clear substantive interpretation of that parameter. This recommendation is intended to prevent the addition of meaningless parameters to a model simply for the purpose of improving goodness of fit to a particular sample (p. 491).

MacCallum, et al. (1992) also note that even when substantive justifications for model modifications are offered, there may be concern as to the rigor and validity of those justifications. Steiger (1990, c.f. MacCallum, et al., 1992) similarly states the problem as follows:

What percentage of researchers would find themselves unable to think up a 'theoretical justification' for freeing a parameter? In the absence of empirical information to the contrary, I assume that the answer ... is 'near zero' (p. 175).

The advice given by MacCallum, et al. (1992) that a “clear and well-founded interpretation be offered for any modification” is important, and, we believe, represents a necessary condition for conducting specification searches. In this case, without such a justification it is impossible to assess the substantive merit of the separation of usefulness and effectiveness.

To summarize, the suggestion that the perceived usefulness construct includes two dimensions, "usefulness" and "effectiveness," may be unwarranted. First, as indicated in points 1 to 3 above, there are some technical problems with the analysis on which this conclusion is based. Second, and in our view more importantly, there is no readily apparent substantive rationale for splitting perceived usefulness into two distinct dimensions. To further test whether the usefulness measure proposed by Davis is unidimensional or multidimensional, the results of a CFA are now examined based on a new, independent data set drawn from a larger sample of voice mail users.

## Re-Examining Usefulness and Effectiveness

Using both our own data set and the original Adams, et al., data, our analyses will specifically examine whether Davis' (1989) single-factor usefulness scale is best modeled as one factor—usefulness—or two factors—usefulness and effectiveness. To compare the one- and two-factor solutions several tests are presented: traditional sample-based tests of model fit; distribution-free resampling procedures (i.e., permutation analysis and bootstrap resampling); and two cross-validations—first, using the original Adams, et al., data as a calibration set and the new data as a validation set and second, performing a Monte Carlo study of 20 pairs of cross-validations based on random subsamples from the new data set. The use of these different techniques allows us to assess the confidence in our findings, and each addresses different methodological concerns. At the same time, we recognize that there are more analyses included here than are necessary to make our point. This has been done to illustrate the range of approaches that can be taken to model testing and to provide pointers to authoritative references in the literature that describe the techniques in greater detail.

Covariance matrices are used for all analyses, and all tests were performed with both EQS version 4.02 (Bentler, 1992) and AMOS version 3.1 (Arbuckle, 1993) using the Maximum Likelihood Estimation (MLE) procedure. Maximum Likelihood is the most appropriate estimation procedure given our sample size (Hu, et al., 1992). To overcome the limitations of MLE with respect to multivariate normality we also examine results using distribution-free resampling. This latter approach requires no assumption about statistical distribution and does not place the same limitations on sample size as other techniques. An examination of the consistency between the different analyses allows us to assess the confidence that can be placed in the results.

## The new sample

The new data set was obtained from a single organization that had recently installed voice mail. Davis' (1989) ease of use and usefulness scales were included in the first part of a 120-item questionnaire. A total of 575 questionnaires were distributed, and 259 usable responses were returned, representing a 45 percent response rate. On average, the respondents had been using voice mail for less than a month, had sent 2.14 messages per day (standard deviation- s.d. = 2.07), and had received 4.49 messages per day (s.d. = 4.87). Respondents came from various levels in the organization.

## Presentation of findings

## Overall Model Fit

Using the measures suggested by S&G and our new data set, we first compare model fit and parameter estimates of both a one-factor "usefulness" only model and a two-factor "usefulness/effectiveness" model. The resulting fit statistics and parameter estimates are presented in Table 1 and Figures 1 and 2 respectively. The $\chi^2$ test statistics are not statistically different for the two models ( $\Delta\chi^2 = 0.235$ ; $p > 0.6$ ). Further, the correlation between the usefulness and effectiveness factors of .995 (as shown in Figure 2) suggests a lack of discriminant validity, that the two factors may be identical, and that they should be merged into a single factor. All fit indices suggest that the single-factor model is as good as the two-factor model, and a number of them suggest that the single-factor model is better (see Table 1 e, k, l, m, and n).

Based on this analysis, the new data set suggests a good fit for the single-factor usefulness model. However, to provide a comprehensive assessment, the properties of the data need to be taken into account. In our case, the scale items were univariate normal but, taken together, violated assumptions of multivariate normality. In addition, our sample, while larger than that used in prior studies of these constructs, is relatively small for this type of analysis. Given this we also employ supplementary analyses that are not sensitive to sample size limitations or distributional assumptions.

Table 1. Fit Indices for the Single-Factor and Two-Factor Usefulness Model—New Data Set

<table><tr><td></td><td>Guidelines</td><td>Single-Factor Model</td><td>Two-Factor Model</td></tr><tr><td>a.  $\chi^2$ </td><td>smaller is better*</td><td>34.66</td><td>34.43**</td></tr><tr><td>b. Degrees of freedom</td><td></td><td>5</td><td>4</td></tr><tr><td>c. Root Mean Square Residual</td><td>&lt;.05</td><td>0.045</td><td>0.045</td></tr><tr><td>d. Jöreskog &amp; Sörborn GFI</td><td>&gt;.90</td><td>0.95</td><td>0.95</td></tr><tr><td>e. Jöreskog &amp; Sörborn AGFI</td><td>&gt;.90</td><td>0.84</td><td>0.80</td></tr><tr><td>f. Bentler-Bonnett normed (NFI)</td><td>&gt;.90</td><td>0.98</td><td>0.98</td></tr><tr><td>g. Bentler-Bonnett non-normed (NNFI)</td><td>&gt;.90</td><td>0.96</td><td>0.95</td></tr><tr><td>h. Bollen (delta 2)</td><td>&gt;.90</td><td>0.98</td><td>0.98</td></tr><tr><td>i. McDonald centrality measure</td><td>&gt;.90</td><td>0.94</td><td>0.94</td></tr><tr><td>j. Bentler Comparative Fit</td><td>&gt;.90</td><td>0.98</td><td>0.98</td></tr><tr><td>k. Akaike Information Criterion (AIC)</td><td>smaller is better</td><td>64.67</td><td>66.43</td></tr><tr><td>l. Consistent AIC</td><td>smaller is better</td><td>133.0</td><td>139.3</td></tr><tr><td>m. Browne-Cudeck single sample cross-validation</td><td>smaller is better</td><td>65.4</td><td>67.2</td></tr><tr><td>n. Tight Cross-Validation Fit</td><td>smaller is better</td><td>0.52</td><td>0.56</td></tr><tr><td>o. p (permutation)</td><td>&lt;.05 + % invariant (= .15 in this study)</td><td>n/a</td><td>0.39</td></tr><tr><td>p. p (bootstrap)</td><td>larger is better</td><td>0.014</td><td>0.003</td></tr></table>

$^{*}\chi^{2}=1424$ for the baseline independence model, which assumes no relationship among the items.  
\*\*Change in $\chi^2$ relative to the two-factor model is not significant ( $p > 0.60$ ).

![](/api/attachments/MPRXTSQR/fulltext/images/ae79b6fa0aea00c23b8623c0db3f0b62f6375682b5613a9ca5a5df2c9eec33b4.jpg)

Figure 1. Parameter Estimates for Single-Factor Usefulness Model Using New Data Set  
![](/api/attachments/MPRXTSQR/fulltext/images/0bcfa88e7eb85b35dd4b65af0f2f21409dc42ef74df11e9721934739d11d355d.jpg)  
Figure 2. Parameter Estimates for Two-Factor Usefulness Model Using New Data Set

## Distribution-Free Resampling

To test the proposed two-factor model, we performed a randomization test, permuting the usefulness indicators to randomly create various two-factor models (see Edgington, 1987 for details). If the two-factor effectiveness/usefulness model is supported, then it should fit better than models with two randomly created factors. Conversely, if a large percentage of the randomly created models results in equal or better fit, then doubt is raised about the validity of the proposed two-factor model.

Table 2. Model Discrepancy Fits For 20 Cross-Validations Comparing the Single and Two-Factor Usefulness Model—New Data Set

<table><tr><td>Sample</td><td>One-Factor Model</td><td>Two-Factor Model</td></tr><tr><td>1*</td><td>1.13**</td><td>1.13</td></tr><tr><td>2</td><td>0.42</td><td>0.49</td></tr><tr><td>3</td><td>0.41</td><td>0.41</td></tr><tr><td>4*</td><td>0.48</td><td>0.48</td></tr><tr><td>5</td><td>0.42</td><td>0.47</td></tr><tr><td>6*</td><td>0.54</td><td>0.54</td></tr><tr><td>7*</td><td>0.72</td><td>0.72</td></tr><tr><td>8</td><td>0.50</td><td>0.53</td></tr><tr><td>9</td><td>0.47</td><td>0.61</td></tr><tr><td>10</td><td>0.67</td><td>0.85</td></tr><tr><td>11*</td><td>0.46</td><td>0.46</td></tr><tr><td>12*</td><td>0.38</td><td>0.38</td></tr><tr><td>13*</td><td>0.33</td><td>0.33</td></tr><tr><td>14</td><td>0.51</td><td>0.51</td></tr><tr><td>15</td><td>0.36</td><td>0.37</td></tr><tr><td>16</td><td>0.41</td><td>0.43</td></tr><tr><td>17*</td><td>0.18</td><td>0.19</td></tr><tr><td>18*</td><td>0.39</td><td>0.39</td></tr><tr><td>19*</td><td>0.94</td><td>0.94</td></tr><tr><td>20*</td><td>0.63</td><td>0.63</td></tr></table>

\* Indicates instances where the two-factor model had correlations set at 1.  
\*\* Smaller values indicate better fit.

Table 3. Covariance Matrix for Voice Mail Data From the Adams, et al., Study

<table><tr><td colspan="3">Make.</td><td colspan="2">Enchance</td></tr><tr><td colspan="2">Job</td><td rowspan="2">Increase Productivity</td><td rowspan="2">My Effectiveness</td><td rowspan="2">Improve Job Performance</td></tr><tr><td>Easier</td><td>Useful</td></tr><tr><td>2.282</td><td></td><td></td><td></td><td></td></tr><tr><td>1.521</td><td>1.773</td><td></td><td></td><td></td></tr><tr><td>1.897</td><td>1.582</td><td>2.598</td><td></td><td></td></tr><tr><td>1.906</td><td>1.513</td><td>1.980</td><td>2.872</td><td></td></tr><tr><td>1.812</td><td>1.529</td><td>1.950</td><td>2.395</td><td>2.901</td></tr></table>

Excluding the proposed model there are 119 permutations of the five items into two factors. The hypothesized usefulness/effectiveness model outperformed randomly created two-factor models in only 12 (10 percent) of the 119 possible cases. Sixty of the random models resulted in inadmissible estimates. Forty-seven of the random combinations were either as good, or better than, the proposed two-factor model. Thus, there is approximately a 0.40 probability (47/119) that a randomly produced two-factor model will fit as well or better than the proposed usefulness/effectiveness model (see Table 1o).

In addition to the randomization test, we performed a bootstrap resampling procedure. This is useful when normality assumptions are violated and when sample size is relatively small (Bollen and Stine, 1992). Using the Bollen-Stine procedure for transforming the data, we performed 2000 bootstrap sample analyses for the one- and two-factor models. Each of the 2000 analyses uses a different data set obtained by sampling 259 observations with replacement from our original data set. The results also suggest that the single-factor model is better than the two-factor model (Table 1p).

## Cross Validation

Finally, we performed two sets of cross validations. First, the Adams, et al., voice mail sample was used as a calibration set. The estimates (see Figures 3 and 4) were then used for prediction on the new data set. Tables 3 and 4 show the two covariance matrices. The results of the cross validation show that the single-factor model fits as well as the two-factor usefulness/effectiveness model (see Table 1n).

For the second cross validation, as suggested by MacCallum, et al. (1994), we randomly split the new data set into two subsamples, using one as the calibration set and applying the resulting estimates to the second subsample as a validation set. This procedure was repeated 20 times, using 20 randomly formed split samples. For all 20 cases, the single-factor model was equal to, or better than, the two-factor model (see Table 2 $^{1}$ ). Overall, these results strongly suggest that the single-factor usefulness model fits the “true population” model better than the two-factor model.

Table 4. Covariance Matrix, Univariate, and Multivariate Statistics for New Voice Mail Data (n=259)

<table><tr><td></td><td>Make Job Easier</td><td>Useful</td><td>Increase Productivity</td><td>Enhance My Effectiveness</td><td>Improve Job Performance</td></tr><tr><td></td><td>2.467</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>2.061</td><td>2.380</td><td></td><td></td><td></td></tr><tr><td></td><td>2.082</td><td>1.928</td><td>2.464</td><td></td><td></td></tr><tr><td></td><td>2.025</td><td>2.001</td><td>2.036</td><td>2.469</td><td></td></tr><tr><td></td><td>2.043</td><td>1.910</td><td>2.186</td><td>2.067</td><td>2.669</td></tr><tr><td rowspan="2">item mean skewness</td><td>4.68</td><td>5.06</td><td>4.64</td><td>4.58</td><td>4.41</td></tr><tr><td>-0.74</td><td>-0.98</td><td>-0.67</td><td>-0.64</td><td>-0.57</td></tr><tr><td>kurtosis</td><td>-0.05</td><td>0.36</td><td>-0.17</td><td>-0.35</td><td>-0.46</td></tr></table>

Mardia's Coefficient of Multivariate Normality (G2,P) = 31.0393; p<0.01.

## Concluding Remarks

The purpose of this note has been to highlight problems that may result when statistical indicators drive substantive decisions in structural equation modeling. In particular, we raised concerns regarding the exploratory procedure used by S&G (1993). Our concerns were based on methodological limitations and, more importantly, on the absence of substantive reasoning for the addition of effectiveness as a construct distinct from usefulness. We demonstrated through re-analysis of Adams, et al.'s (1992) original data and a new independent data set that the single-factor usefulness measure developed by Davis (1989) has reasonable psychometric properties. Thus, our analysis suggests that there is no empirical support or substantive rationale for the separation of the usefulness construct into two dimensions.

We conclude by emphasizing our view that SEM techniques should be applied within a framework provided by substantive knowledge of the phenomena of interest (MacCallum, 1986; MacCallum, et al., 1992). In particular, researchers need to be extremely careful when performing specification searches. To do otherwise is to risk generating spurious results. We are not arguing that SEM techniques are inappropriate in MIS research. Quite the contrary, we believe that they are useful and applicable to a wide class of problems in IS research. The reasons for their application in construct validation and modeling have been well articulated by Segars and Grover. We do, however, want to stress the need for careful attention to detail in utilizing these techniques, coupled with a strong focus on substance and theory. Under these conditions the use of SEM should lead to valid conclusions. Finally, even if one is not well versed in such procedures, substantive and theoretical knowledge can be a strong ally, and researchers should be cautious in interpreting and reporting the results of any work based on SEM modeling that are not supported by substantive theoretical arguments.

## Acknowledgements

This work was supported, in part, by grants from the Social Sciences and Humanities Research Council of Canada and the School of Business Research Program at Queen's University. We are grateful to Yolande Chan, Barb Marcolin, Michael Parent, Shirley Taylor, and the anonymous reviewers for their helpful comments on earlier drafts of this paper.

![](/api/attachments/MPRXTSQR/fulltext/images/6d47ff0e73bd58eb8830eea0603b652cb30fd4d393df8a725c98f5f8911bc4c3.jpg)

Figure 3. Parameter Estimates for Single-Factor Usefulness Model Using Adams, et al., Data Set  
![](/api/attachments/MPRXTSQR/fulltext/images/7c61d4da7bc442f71660bca7544456e39350dc70909c4131ecd9c822fc847ffb.jpg)  
Figure 4. Parameter Estimates for Two-Factor Usefulness Model Using Adams, et al., Data Set

## References

Adams, D. A., Nelson, R. R., and Todd, P. A. "Perceived Usefulness, Ease of Use, and Usage of Information Technology: A Replication," MIS Quarterly (16:2), June 1992, pp. 227-247.

Arbuckle, J. AMOS 3.1 Documentation Package, Department of Psychology, Temple University, Philadelphia, PA, 1993.

Bentler, P.M. EQS Structural Equations Program Manual, BMDP Statistical Software, Inc., Los Angeles, CA, 1992.

Bollen, K.A. and Stine, R. A. "Bootstrapping Goodness-of-Fit Measures in Structural Equation Models," Sociological Methods & Research (21:2), November 1992, pp. 205-229.

Cudeck, R. and Browne, M.W. "Cross-Validation of Covariance Structures," Multivariate Behavioral Research (18), May 1983, pp. 147-167.

Davis, F.D. "Perceived Usefulness, Perceived Ease of Use, and User Acceptance of Information Technology," MIS Quarterly (13:3), September 1989, pp. 319-340.

Davis, F.D. "User Acceptance of Information Technology: System Characteristics, User Perceptions, and Behavioral Impacts," International Journal of Man-Machine Studies (38), September 1993, pp. 475-487.

Davis, F.D., Bagozzi, R., and Warshaw, P. "User Acceptance of Computer Technology: A Comparison of Two Theoretical Models," Management Science (35:8), August 1989, pp. 982-1003.

Edgington, E.S. Randomization Tests, (2nd ed.), Marcel Dekker, Inc, New York, NY, 1987.

Hendrickson, A.R., Massey, P.D., and Cronan, T.P. "On the Test-Retest Reliability of the Perceived Usefulness and Perceived Ease of Use Scales," MIS Quarterly (17:2), 1993, pp. 227-230.

Hu, L., Bentler, P.M., and Kano, Y. "Can Test Statistics in Covariance Structure Analysis Be Trusted?" Psychological Bulletin (112:2), 1992, pp. 351-362.

MacCallum, R. "Specification Searches in Covariance Structure Modeling," Psychological Bulletin (100:1), July 1986, pp. 107-120.

MacCallum, R.C., Roznowski, M., and Necowitz, L. B. "Model Modification in Covariance Structure Analysis: The Problem of Capitalization on Chance," Psychological Bulletin (111:3), 1992, pp. 490-504.

MacCallum, R.C., Roznowski, M., Mar, C.M., and Reith, J.V. "Alternative Strategies for

Cross-Validation of Covariance Structure Models," Multivariate Behavioral Research (29:1), 1994, pp. 1-32.

Mathieson, K. "Predicting User Intentions: Comparing the Technology Acceptance Model with the Theory of Planned Behavior," Information Systems Research (2:3), September 1991, pp. 173-191.

Mosier, C.I. "Problems and Designs of Cross-Validation," Educational and Psychological Measurement (11), Spring 1951, pp. 5-11.

Segars, A.H. and Grover, V. "Re-Examining Perceived Ease of Use and Usefulness: A Confirmatory Factor Analysis," MIS Quarterly (17:4), December 1993, pp. 517-525.

Steiger, J.H. "Structural Equation Model Evaluation and Modification: An Interval Estimation Approach," Multivariate Behavioral Research (25), 1990, pp. 173-180.

## About the Authors

Wynne W. Chin is an associate professor in the Faculty of Management at the University of Calgary. He received his A.B. in biophysics from U.C. Berkeley, his M.S. in biomedical engineering from Northwestern University, and an M.B.A. and Ph.D. in computers and information systems from the University of Michigan. To the chagrin of his two daughters Christina (5 and a half years) and Angela (10 months) and his wife Kelly (? years), he spends a lot of family time working on casual models related to IT adoption and GSS meeting processes. Some of his efforts are even published or forthcoming in journals such as ISR, DataBase, JMIS, and Decision Sciences, with the rest relegated to the recycle bin for crayon drawings.

Peter A. Todd is an associate professor of management information systems and chair of the Research Program in the School of Business at Queen's University. He received his Ph.D. in management information systems from the University of British Columbia and has previously served on the faculty of the University of Houston. He has published papers in a variety of journals including MIS Quarterly and ISR. His primary research interests include human-computer interaction, decision support systems, behavioral decision making, and the adoption and diffusion of information technology.
