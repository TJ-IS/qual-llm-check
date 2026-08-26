---
otero_id: 15458
otero_key: "6BE7B47Q"
title: "Exploratory factor analysis revisited: How robust methods support the detection of hidden multivariate data structures in IS research"
authors: "Horst Treiblmaier; Peter Filzmoser"
year: "2010"
journal: "Information & Management"
doi: "10.1016/j.im.2010.02.002"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Exploratory factor analysis revisited: How robust methods support the detection of hidden multivariate data structures in IS research

Horst Treiblmaier <sup>a,</sup>\*, Peter Filzmoser <sup>b</sup>

<sup>a</sup> Institute for Management Information Systems, Vienna University of Economics and Business, Augasse 2-6, 1090 Vienna, Austria <sup>b</sup> Department of Statistics and Probability Theory, Vienna University of Technology, Wiedner Hauptstraße 8-10, A-1040 Vienna, Austria

## A R T I C L E I N F O

Article history: Received 4 April 2008 Received in revised form 8 April 2009 Accepted 10 February 2010 Available online 23 February 2010

Keywords: Factor analysis Exploratory factor analysis Classical factor analysis Robust factor analysis Robust statistics

## A B S T R A C T

Exploratory factor analysis is commonly used in IS research to detect multivariate data structures. Frequently, the method is blindly applied without checking if the data fulfill the requirements of the method. We investigated the influence of sample size, data transformation, factor extraction method, rotation, and number of factors on the outcome. We compared classical exploratory factor analysis with a robust counterpart which is less influenced by data outliers and data heterogeneities. Our analyses revealed that robust exploratory factor analysis is more stable than the classical method

\- 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

The number of empirical research papers in top-tier IS journals suggests that the IS discipline frequently uses quantitative research methods. In order to enhance the value of their results, there is an ongoing discussion on how to improve existing methods, avoid potential sources of error, and introduce new ways of data analysis [5,7,14]. Many methodological papers published in leading IS journals have focused on topics that are ‘in fashion’. Examples include the popularity of PLS and, more recently, interest in formative indicators [20].

A strong focus has been placed on confirmation of theory-based models, for example by using LISREL or PLS. To test hypotheses, researchers conduct surveys and usually rely on the results of previously tested measurement instruments. They concentrate on confirmatory aspects, such as achieving a sufficient fit for the model, but often overlook the important role of exploratory statistical techniques that are frequently used prior to a confirmatory study.

In general, the decision of whether to use either an exploratory or a confirmatory procedure depends on the availability of a theory that explains how the hypothesized construct corresponds to the items. In spite of the amount of attention given to confirmatory techniques, Conway and Huffcutt [8] stated that ‘‘researchers tend to make better decisions when EFA (exploratory factor analysis) plays a more consequential role in their research.’

There has also been a long-standing discussion about the eligibility of survey data for various data analysis methods. Especially data generated using Likert-type items – a common technique in IS research – often do not meet the requirements of the applied method, such as normal distribution of the individual variables or multivariate normal distribution. In many cases, latent variables represent users’ attitudes, norms, values, and intentions. To measure these, respondents are typically asked to express their level of agreement on a scale (e.g. 5-point Likert scale: ‘‘strongly agree’’, ‘‘agree’’, ‘‘neutral’’, ‘‘disagree’’, ‘‘strongly disagree’’). Although the underlying latent construct may be seen as a continuum, the items are measured on an ordinal scale. Here, we use a 100-point slider in an online survey to create a metric scale and examine the use of robust factor analysis rather than classical factor analysis in detecting hidden data structures. It consists of three major parts.

\- The capabilities and problems of EFA. We especially want to demonstrate that researchers have a multitude of options such as data transformation, factor extraction method, rotation method, and choosing the optimum number of factors when conducting EFA. If they try various configurations and disregard basic statistical assumptions, they may eventually obtain the results they desire. Previous research has shown that many published applications of EFA are, to some extent, questionable. We also introduce the concept of robust factor analysis, which proposes a viable alternative eliminating many of the shortcomings of nonrobust EFA. By reducing the influence of outliers, robust statistics helps to overcome the strict model assumptions of classical methods, such as the necessity of normal or multivariate normal distribution, which is rarely given in survey-based research.

\- Several examples of how EFA is currently used; e.g. when new scales are developed or the validity of a measurement model is assessed.

\- Robust factor analysis; examining data that we gathered in an Internet-based survey and comparing the results with those obtained by using classical factor analysis and a qualitative study.

## 2. Exploratory factor analysis

Factor analysis, which was popularized by Charles Spearman in the early 1900s, has become one of the most widely used statistical techniques in psychological research [9]. It is therefore of paramount importance in all investigations of human behavior. Its major objective is to reduce a number of observed variables to less factors in order to enhance interpretability and detect hidden structures in the data. Frequently, such structures are used as constructs in sophisticated models in understanding aspects of human behavior. Table 1 shows that researchers using EFA have to make decisions on issues such as robust versus non-robust procedures, data transformation, factor extraction method, factor rotation, and the number of factors retained. All of these strongly influence the final results. Researchers must be aware that there are many factor solutions to one correlation matrix and that their final solution represents just one of many possible choices. Thus, the statement by Chin et al. [6] highlighted the researcher’s freedom in, and responsibility for, determining the output: ‘‘Though the scree plot suggested a smaller number of factors than the Eigenvalue rule, we opted to err on the conservative side by including more factors to avoid the possibility of missing relevant ones’’. Furthermore, the list of options is by no means exhaustive, but only presents a selection of choices commonly made.

## 2.1. Robust versus non-robust

EFA relies on the estimation of the correlation matrix. Once the matrix is available, the loadings and uniquenesses, and subsequently the factor scores are determined. They are usually estimated for the sample correlation matrix, which is the empirical sample covariance matrix standardized by the empirical variances. This classical approach is good if the data are multivariate normally distributed. However, if the data distribution deviates from this ideal distribution, the estimated correlation matrix can be severely biased. Fig. 1 shows this effect. The estimated correlations are visualized by the ellipses which, in case of bivariate normal distribution, should contain 97.5% of the data points. The ellipse with the dashed line is based on the classical estimates, while the one with the solid line uses robust estimates. While the latter ellipse covers the homogeneous majority of observations, the ellipse with the classical estimates is inflated by the deviating data points, which leads to an unrealistic estimation of the correlation and this, in turn, constitutes the basis for the factor analysis.

Several alternative approaches have been suggested to estimate the correlation matrix reliably in the presence of deviations from multivariate normality. A prominent way is to use the Minimum Covariance Determinant (MCD) estimator, which looks for a subset of observations (e.g. at least 50%) with minimal determinant of the empirical covariance matrix, which is then multiplied by a consistency factor. The MCD is highly robust, i.e. up to 50% of the observations can deviate from the multivariate normal distribution. The robust correlation matrix is obtained by standardizing the robust covariances with the square-root of the diagonal elements. The MCD estimator [24] is attractive for its high robustness, especially as there is a fast algorithm available for use in several widely used statistical software packages, such as PASW, R, S-Plus, SPSS, SAS, and STATA.

Plugging in the robust MCD correlation matrix into factor analysis also leads to a highly robust estimation of the loadings and uniquenesses [21]. Outliers can have an unduly high influence on the estimation of these parameters when using the classical correlation matrix, but their influence is limited when using the MCD correlation matrix.

## 2.2. Sample size

Clearly, larger samples outperform smaller samples due to the reduction in the probability of errors, more accurate population estimates and better generalizability of the results. If the overall sample size is too small, errors of inference can occur. Various recommendations pertaining to sample size can be found in the literature. While some authors highlight the importance of absolute sample size, most researchers focus on the ratio between subjects and variables. Recommendations frequently include ratios of 5:1 or 10:1. However, MacCallum et al. [15] showed that this might be an oversimplification; e.g., population factors in data can be adequately recovered if communalities are high and thus sample size is of minor importance. When researchers are confronted with low communalities and poorly overdetermined factors, they recommend sample sizes that are much larger than usually suggested (e.g. a 20:1 ratio). For a robust method the sample size should be even larger because deviating data points will be down-weighted.

Table 1  
Examples of influencing determinants in factor analysis.

<table><tr><td rowspan="6">Robustness</td><td>Robust factor analysis</td><td></td></tr><tr><td>Non-robust factor analysis</td><td></td></tr><tr><td>No transformation</td><td></td></tr><tr><td>Logit</td><td></td></tr><tr><td>Power</td><td></td></tr><tr><td>Box-Cox</td><td></td></tr><tr><td rowspan="4">Factor extraction method</td><td>Classical extraction methods</td><td>Robust extraction methods</td></tr><tr><td>Principal component analysis</td><td>Robust principal component analysis</td></tr><tr><td>Principal factor analysis</td><td>Robust principal factor analysis</td></tr><tr><td>Maximum likelihood</td><td>Robust maximum likelihood</td></tr><tr><td rowspan="6">Rotation</td><td>Orthogonal</td><td>Oblique</td></tr><tr><td>Varimax</td><td>Oblimin</td></tr><tr><td>Quartimax</td><td>Quartimin</td></tr><tr><td>Equamax</td><td>Promax</td></tr><tr><td></td><td>Covarimin</td></tr><tr><td></td><td>McCammon</td></tr><tr><td rowspan="4">Number of factors</td><td>A priori criterion</td><td></td></tr><tr><td>Eigenvalue</td><td></td></tr><tr><td>Scree plot</td><td></td></tr><tr><td>Percentage of variance</td><td></td></tr></table>

![](/api/attachments/6BE7B47Q/fulltext/images/7d0e2da93b0232d694226a05196e4e6e3e35909c50f97fb7defac2b9b053a491.jpg)  
Fig. 1. Estimated correlation of simulated data with outliers.

## 2.3. Data transformation

Essentially, data transformation is used to obtain a particular type of distribution, which may be, for example, normal or symmetric. In addition, it is used to establish a simple systematic relationship between an independent and a dependent variable and to stabilize the variance. Real-world data sets are frequently characterized by their skewness, heteroscedasticity and major outliers; these should be taken into account when applying statistical procedures, depending on specific requirements.

## 2.4. Factor extraction method

Broadly, most models can be categorized as either a component model or a common factor model. The goal of principal component analysis, which is by far the most popular type of a component model, is to retain as much as possible of the original measures’ total variance. Common factor models, differentiate between variance attributable to common factors and variance caused by unique factors. Conway and Huffcutt therefore concluded that ‘‘if a researcher’s purpose is to understand the latent structure of a set of variables (which will usually be the case), then the use of a common factor model such as principal axis or maximum likelihood factoring represents a high-quality decision. (. . .) Given that most researchers do attach meaning beyond the observed variables, the common factor model will generally be the better choice’’. Accordingly, Preacher and MacCallum [22] stated that ‘‘it is strongly recommended that principal component analysis (PCA) be avoided unless the researcher is specifically interested in data reduction’’, and Widaman [29] argued that ‘‘the results suggest that principal component analysis should not be used if a researcher wishes to obtain parameters reflecting latent constructs or factors’’.

Furthermore, the application of the correct factor extraction method depends upon the distribution of the data: a multivariate normal distribution is required when using maximum likelihood as the factor extraction method, whereas principal component analysis and a principal factor analysis require elliptical symmetry. In these cases, normal distribution is not a prerequisite, but the results may still be strongly influenced by the occurrence of non-normally distributed data and outliers because of their dependence on the correlation and the covariance matrix [23]. In such cases a robust method is preferable.

## 2.5. Rotation method

There are a number of different factor rotations; depending on the correlations between the factors. Orthogonal rotations, such as Varimax, Quartimax, and Equamax, do not allow for correlations, whereas oblique rotations, such as Oblimin, Quartimin, and Promax, consider correlated factors. Prior research has shown that an orthogonal method, e.g. Varimax, produces stable results, but when factors are actually correlated, an orthogonal rotation produces an unrealistic solution, while an oblique rotation better reproduces reality. Also, an oblique rotation does not require factors to be correlated, so that the correlations between the factors will be close to zero if the actual data structure is orthogonal. Therefore, oblique rotation is preferred by some researchers.

## 2.6. Number of factors

There are several ways to determine the number of factors to be extracted from the data. Besides using an a priori criterion – which may be useful in replication studies – a researcher may decide to use Eigenvalues (latent root criterion) greater than 1, a visual scree plot, or require a specific amount of variance to be explained by the factors. Researchers may be confronted with the problem of specifying too few factors (underfactoring) or too many (overfactoring). Prior research suggested that the latter leads to fewer errors when factor loadings were estimated. However, specifying too many factors might lead to the creation of constructs with little theoretical value. Outliers or deviating data points can lead to an unrealistic estimation of the number of factors, because they can artificially increase the Eigenvalues of the correlation matrix.

## 2.7. Further issues

EFA poses several other problems that are frequently overlooked. One is the assumption that the measurement errors of the items are uncorrelated. Another important requirement is the metric measurement of the variables. A further problem – in addition to the proper application of factor analysis – is the interpretation of the results, which has often been discussed. One other major issue is the minimum threshold for validity. Factor loadings of 0.30 or higher, which explain approximately 10% of a variable’s variance, should be considered when interpreting a factor. Some have suggested 0.32 as the minimum acceptable factor loading for an item. Interestingly, Peterson [19] reported the same number as the average factor loading in a number of studies using EFA. In social sciences research, items tend to load on a number of factors, so that the threshold values are usually more stringent. Some authors suggest that a factor loading higher than 0.60 on the ‘‘parent factor’’ and a loading of less than 0.40 on a ‘‘foreign factor’’ indicate convergent and discriminant validity of the constructs [6].

## 3. EFA in IS research

In order to assess the relevance of factor analysis for IS research, we performed a full-text search (i.e. including both citation and document text) on the databases EBSCOhost and the ProQuest using three search terms (‘‘factor analysis’’, ‘‘exploratory factor analysis’’ and ‘‘principal component analysis’’). We decided to concentrate on four top IS journals, which frequently publish empirical research and demand a high level of methodological rigor: Information Systems Research (ISR), MIS Quarterly (MISQ), Journal of Management Information Systems (JMIS), and Information & Management (I&M). The results can be found in Table 2, with the figures in parentheses indicating the number of papers published since the year 2000. Even when taking into account that the results partially overlap and not all papers carry out an EFA, the findings clearly indicated that factor analysis is frequently used and discussed in empirical IS research.

EFA is frequently used to discover patterns of multidimensional constructs that are subsequently used for the development of measurement scales. Especially when new frameworks or scales are developed, EFA plays a major role in detecting hidden data structures. Even though the major focus of many papers published in IS top journals lies on model confirmation rather than on scale development, researchers often use pre-studies to develop or refine their measurement instruments [16]. Most frequently, however, EFA is applied in a pre-study to confirm the validity of the scales used.

## 3.1. Development of new frameworks and scales

In order to uncover the underlying data structure of 118 items pertaining to consumers’ perception of data quality, Wang and Strong used a series of factor analyses. As a result, they identify the most important dimensions of data quality, viz. intrinsic, contextual, representational, and accessibility data quality. In order to test for the stability of their results, they varied the number of factors and eliminated those items with insignificant loadings [28]. Torkzadeh and Dhillon used a sophisticated approach to identify factors influencing the success of Internet commerce. They conduct a survey in two phases. The first was intended to reduce the overall number of items, while the second served to fine-tune the instrument. Most notably, they used different methods of rotation (orthogonal and oblique) and different procedures to determine the number of factors (i.e. Eigenvalues and a scree plot) to make their results more stable [26].

## 3.2. Validation of the measurement model

EFA is frequently used to validate a measurement model. Zhu and Kraemer [30], for example, compared the results from a principal component analysis (Equamax rotation) with the results from a confirmatory factor analysis. They used a SEM approach (PLS) to determine the robustness of the measurement model. Koh et al. [12] reported that the results of an EFA (principal component analysis with orthogonal and oblique rotation) produced their hypothesized factor solution. Similarly, Ba and Pavlou [2] used EFA with Varimax rotation in order to account for convergent validity. This procedure was proposed by Segars and Grover [25], who pointed out that ‘‘such results provide evidence of convergent and discriminant validity of scale items’’. However, they also noted that ‘‘exploratory factor models provide no explicit test statistics for ascertaining whether convergent and discriminant validity are achieved’’. Accordingly, Karimi et al. [11] stressed that ‘‘the more commonly used EFA does not validate the convergent and discriminant validities of latent variable indicators’’. Table 3 shows examples of EFA applied in IS research, and states the details reported by the authors.

## 4. Methodology

## 4.1. Survey

In order to compare various methods of factor analysis, we decided to gather primary data rather than rely on an existing dataset. We developed a research question that is of interest to IS researchers from various sub-disciplines. Current customer relationship management (CRM) literature describes how companies strive to build (online) relationships with their (prospective) customers. However, when we were scrutinizing the general concept of ‘‘relationship’’, it turned out that many definitions were vague and concentrated on describing activities rather than the core terms [27]. Existing literature indicates that many factors such as usability, ease of use [1], enjoyment, service [17], interactivity [18] and individualization [13] might be responsible for perceived online relationships between customers and vendors. With this being a supposedly multidimensional construct, it seemed to be an ideal starting point for our research.

Table 2  
Factor analysis mentioned in information systems research<sup>a,b</sup>.

<table><tr><td></td><td>Factor analysis</td><td>Exploratory factor analysis</td><td>Principal component analysis</td></tr><tr><td>MIS Quarterly</td><td>173 (84)</td><td>44 (25)</td><td>32 (17)</td></tr><tr><td>ISR</td><td>54 (37)</td><td>16 (10)</td><td>15 (10)</td></tr><tr><td>JMIS</td><td>159 (74)</td><td>32 (25)</td><td>36 (13)</td></tr><tr><td>I&amp;M</td><td>23 (12)</td><td>3 (0)</td><td>1 (0)</td></tr></table>

<sup>a</sup> Date of analysis: April 2008.  
<sup>b</sup> The number of papers published since the year 2000 is shown in brackets.

Table 3  
Sample applications of exploratory factor analysis in IS research.

<table><tr><td>Paper</td><td>Goal</td><td>Factor extraction model</td><td>Number of factors</td><td>Rotation</td><td>Variance explained</td></tr><tr><td>[26]</td><td>Instrument development (validity)</td><td>PCA</td><td>Phase 1: 4 (Eigenvalue &gt;1)Phase 2: 5 (Eigenvalue &gt;1, scree plot)</td><td>Varimax, oblique rotation</td><td>Phase 1: 72.9%, 68.1%Phase 2: 77.3%, 69.2%</td></tr><tr><td>[30]</td><td>Testing the robustness of the measurement model</td><td>PCA</td><td>n.s.</td><td>Equamax rotation</td><td>n.s.</td></tr><tr><td>[12]</td><td>Assessing construct validity (convergent and discriminant validity)</td><td>PCA</td><td>7 (Eigenvalue &gt;1)</td><td>Varimax rotation, oblique rotation</td><td>77.6%, 76.9%</td></tr></table>

n.s.: not specified.

One of the major goals at the start of many research projects is to ensure a sufficient level of content validity (the degree to which items in the measuring instrument represent the content universe in which the instrument will be generalized) [4]. We therefore created a pool of items by conducting a literature research in IS and marketing papers dealing with (online) relationships, (e)CRM and related topics. In this first phase, we tried to generate as many items as possible, even if this led to redundancy, which was to be dealt with in a subsequent phase. We developed a total of 24 items, which were used in the literature as antecedents of online relationships between consumers and vendors. In the next step, we conducted an online survey in cooperation with a newspaper company, who published a link to our questionnaire in two weekly newsletters sent out to 85,500 registered recipients. No incentive was given for filling out the questionnaire. The survey was carried out between 08/25/04 and 09/16/04. We used slider bars ranging from 1 (‘‘strongly disagree’’) to 100 (‘‘strongly agree’’) and gathered a total of 396 responses. After removing incomplete records, 389 usable answers remained. The overall goal of the survey was to measure constituents of online relationships between customers and companies. Although the original questionnaire was in German, no translation and back-translation process was necessary, since we did not use items from existing literature. Instead, the results were translated by the authors and double-checked by a native speaker. The low response rate of 0.5% can be attributed to the fact that we did not use an incentive and that few recipients actually read the whole newsletter. However, this was not a problem since the objective of our study was not the generalization of the results (external validity), but rather the analysis of its factor structure.

## 4.2. Scales

The terms nominal, ordinal, interval, and ratio scales were coined in the 1940s by S.S. Stevens, a US psychologist. Although these have faced strong criticism, this basic classification still prevails in the literature. An important issue is the treatment of survey data, which are frequently collected in Likert-type scales. Integer values are assigned to each category, and the analysis is carried out as though the data was measured on an interval scale; this leads to biased results especially when the product moment correlation coefficient is used.

In order to be able to use robust factor analysis, we had to develop a measurement instrument that better represented a ratio scale than Likert-type scales. Typically, a loss of information occurs, when categorizing an unobserved continuous variable into an ordered categorical variable. We therefore decided to use a magnitude scale, which represented a valid and reliable alternative to category scales. This type of measurement is based on the assumption that there is no fundamental difference between physical measurement and psychophysical measurement. We created a visual analogue scale (VAS), which was simply a line with well-defined end-points on which the respondents indicated their level of agreement [10].

Fig. 2 shows a screenshot of the questionnaire. Based on a number of pretests, we decided to color the sliders red at both ends and blue in the middle. This makes it easier for respondents to differentiate different levels of agreement and it also prevents the accumulation of extreme values. In order to avoid default values, the users had to click on the survey for the slider to appear. This allowed us to count missing values also.

## 5. Results

Prior to our analyses, we tested the eligibility of the data for factor analysis by using the Kaiser–Meyer–Olkin measure of sampling adequacy (MSA). An MSA value of 0.86 indicated a good (‘‘meritorious’’) factorability of the correlation matrix. We also performed a Bartlett sphericity test, which was statistically significant (p < 0.001), indicating the eligibility of the data. This test required normally distributed data and was sensitive to deviations from this assumption. Since our data were nonnormally distributed, this result had to be interpreted with caution.

## 5.1. Comparison between classical and robust factor analyses

As a first step, we used a Shapiro–Wilk test to determine whether our sample had a normal distribution. We found that none of our variables was normally distributed. Since factor analysis is sensitive to non-normally distributed data, we used a logit transformation to create better symmetry and to avoid the default range of 1–100. Nevertheless, normal distribution could not be achieved for any of the variables, since many of the original data values were 1 or 100, corresponding to the extreme positions of the slider in the VAS. Therefore, a power transformation and a Box–Cox transformation were applied; they also did not yield normally distributed data. Since the maximum likelihood method. which requires multivariate normally distributed data, was therefore not appropriate, Principal factor analysis (PFA) was our choice for the factor extraction method. PFA is based on a decomposition of the (reduced) correlation matrix, which is sensitive to severe deviations from an elliptically symmetric form of the data distribution and to outliers in the data. Hence, PFA based on a robust correlation matrix, which results in a robust factor analysis (FA), will be more appropriate for our data. To compute the robust correlation matrix, the MCD (Minimum Covariance Determinant) estimator was used, because it is very robust, fast, and widely available in statistical software packages. Both the robust and non-robust (classical) FA suggested 5–6 factors according to the scree plot and the Eigenvalue criterion. We opted for the larger number of factors in order to avoid underfactoring. An orthogonal rotation such as Varimax resulted in a highly dominant first factor and a rather weak discrimination of the factors according to their loadings. Therefore, an oblique rotation seemed to be the best choice, since it was reasonable to expect that the dimensions of online relationships would correlate with one another. We used Oblimin rotation, but observed very similar results for a variety of other oblique rotation methods (Quartimin, Covarimin, McCammon, Promax, etc.). The resulting biplots of the classical and the robust FA for the first pair of factors are shown in Fig. 3.

<table><tr><td colspan="4">In an online relationship with a company it is important to me that</td></tr><tr><td></td><td>Absolutely disagree</td><td>neutral</td><td>Absolutely agree</td></tr><tr><td>I am personally welcomed</td><td></td><td></td><td></td></tr><tr><td>I receive congratulations on important dates (e.g. birthday)</td><td></td><td></td><td></td></tr><tr><td>I regularly receive individualized newspapers</td><td></td><td></td><td></td></tr><tr><td>I can express my opinions in forums</td><td></td><td></td><td></td></tr><tr><td>I have the opportunity to give feedback</td><td></td><td></td><td></td></tr><tr><td>I can find a contact person at any time</td><td></td><td></td><td></td></tr><tr><td>I get answers for my requests quickly</td><td></td><td></td><td></td></tr><tr><td>I can check my delivery status at any time</td><td></td><td></td><td></td></tr></table>

Fig. 2. Screenshot of the questionnaire (translated).

These biplots show striking differences in both the configuration of the variables (arrows) and the configuration of the observations. The latter were plotted using two different symbols: ‘‘+’’ if the observation was identified as an outlier by the robust method, and ‘‘.’’ for all others. Obviously, the factors in the classical analysis were ‘‘attracted’’ by the outliers, because the factors point in their directions. This is different for the robust analysis, which focuses on the core of the data.

The loading plots shown in Fig. 4 illustrate the differences in factor loadings for all factors of the classical and the robust analysis. The horizontal axis is scaled according to the relative amount of variability explained by each single factor in the FA model, excluding the unexplained part of the variability (uniqueness) of each variable. Additionally, the percentage values at the top display the cumulative explained variance for the total data variability. It is thus possible to see how much of the total variance is explained and the importance of these single factors. The vertical axis is scaled from +1 to 1 and shows the factor loadings. Dashed lines at values of +0.5 and 0.5 help to distinguish the important $( > + 0 . 5 , < - 0 . 5 )$ from the less important. Names of variables with absolute loadings of <0.3 were not plotted because their contribution to the factors was negligible.

This illustrates the difference of the biplots, with some factors changing their order due to their relative importance. The classical method was especially sensitive to changes in the order of the factors, because outliers artificially increased the explained variance of some factors, giving them more importance. There are also major differences in the composition of the loadings for both factor analyses, which also lead to different interpretations.

![](/api/attachments/6BE7B47Q/fulltext/images/5a3da0c1e10a4508545e86258ad30ade0363e62941b48e4f193dc1a81bf587ba.jpg)

## 5.2. The influence of data transformation

In order to assess the effect of data transformation, we analyzed the original untransformed data. Then we simulated a 5-point Likert scale by creating five categories with intervals from 1–20, 21–40, 41–60, 61–80, and 81–100. These data resembled the results that would be obtained from a standard questionnaire using a 5-point Likert scale. To make the analyses comparable to previous results, we applied PFA (robust and classical) with 6 factors and Oblimin rotation. However, the robust method does not work for the categorical data, because the algorithm for the MCD estimator leads to singularities. Fig. 5 shows the resulting loading plots.

![](/api/attachments/6BE7B47Q/fulltext/images/70749ac735a477a16435d36cb65e6f68e2ade3eff7db7dd7d27003c91e7cb7c2.jpg)  
Fig. 3. Biplots of classical and robust factor analysis for the first two factors.

Classical FA (logit-transformed data)  
![](/api/attachments/6BE7B47Q/fulltext/images/bb6c4629683c56e537f5f5baab1a976a1a398bc1f0bf8e4e23e453dde1465bbe.jpg)

Robust FA (logit-transformed data)  
![](/api/attachments/6BE7B47Q/fulltext/images/c75c4ec92ec31d4a9d0e9463145e0f882bea3b180518052f419e8a874fe998d1.jpg)  
Fig. 4. Classical factor analysis versus robust factor analysis: factor loadings.

Apart from changes in the order of the factors – the classical analyses are quite similar, although there are several differences for the logit-transformed data. This is not surprising, given that the raw data and the categorized data are very skewed, which leads to biased correlations. But even the robust method gave rise to substantial differences caused by severe deviations from elliptical symmetry.

Table 4 summarizes the results in a concise format. The original wording of the variables ‘01’ to ‘24’ is shown in the rows of the table. The five columns on the right contain the various factors (labeled A–F) of the different analyses shown. In order to improve readability, we did not show the loadings in numbers, but only the respective label A–F of the factor on which the items loaded. Since all analyses resulted in a six factor solution, we used all labels in each of the columns. Capital letters in these columns referred to absolute loadings higher than 0.5, and lower-case letters indicated absolute loadings between 0.3 and 0.5. To facilitate comparison between the five analyses, we changed the labeling of the factors, rather than simply adopting the labels F1–F6, which were determined by the amount of variance explained (i.e. the relative importance of the factors). The labels of the classical factor analysis with logit transformation (CL) were directly taken from Fig. 4 (i.e. A = F1, B = F2. . .). When applying a robust factor analysis with logit transformation (RL), the relative importance of the factors changed. Factor F2 of the robust analysis contained exactly the same items as F3 in the classical analysis. We therefore decided to relabel F2 from the robust solution as ‘C’ instead of ‘B’, to facilitate the comparison. Since the labeling of the factors is arbitrary, this relabeling does not alter the results (i.e. the overall factor structure). However, it should be noted, that in Table 4 the letters no longer show their relative importance, i.e. ‘A’ is simply a label that does not indicate any ranking. In some cells, there are two letters, which shows that the variable loads on two different factors.

Classical FA of original data  
![](/api/attachments/6BE7B47Q/fulltext/images/51b352569e5f7bd7dcf5106eb5c013bd256059b4d812f4aab21096b4cbfdfa76.jpg)

Classical FA of data in scale 1 to 5  
![](/api/attachments/6BE7B47Q/fulltext/images/57d68a178cd67be2082ef1a6529889e94548db9b8e55f4e208986722362da4c4.jpg)

Robust FA of original data  
![](/api/attachments/6BE7B47Q/fulltext/images/96d73b8c0eb11e540dfa2b3d737a412d1f0d022131b21685eecaa325e6cb71c0.jpg)  
Fig. 5. Classical and robust factor analyses on untransformed data.

Table 4  
Comparison of the factor analyses.

<table><tr><td></td><td>Item</td><td>CL</td><td>RL</td><td>CO</td><td>C1-5</td><td>RO</td></tr><tr><td></td><td colspan="6">In an online relationship with a company it is important to me that</td></tr><tr><td>01</td><td>... I am personally welcomed</td><td>B</td><td>B</td><td>B</td><td>B</td><td>B</td></tr><tr><td>02</td><td>... I receive congratulations on important dates (e.g. birthday)</td><td>B</td><td>B</td><td>B</td><td>B</td><td>B</td></tr><tr><td>03</td><td>... I regularly receive individualized newsletters</td><td>B</td><td>E</td><td>B</td><td>B</td><td>Be</td></tr><tr><td>04</td><td>... I can express my opinions in forums</td><td>E</td><td>e</td><td>E</td><td>E</td><td>E</td></tr><tr><td>05</td><td>... I have the opportunity to give feedback</td><td>E</td><td>Ef</td><td>E</td><td>E</td><td>E</td></tr><tr><td>06</td><td>... I can find a contact person at any time</td><td>ef</td><td>F</td><td>ef</td><td>F</td><td>F</td></tr><tr><td>07</td><td>... I get answers for my requests quickly</td><td>af</td><td>F</td><td>F</td><td>F</td><td>F</td></tr><tr><td>08</td><td>... I can check my delivery status at any time</td><td>A</td><td>A</td><td>f</td><td>f</td><td>a</td></tr><tr><td>09</td><td>... I receive individualized offers</td><td>B</td><td>E</td><td>B</td><td>B</td><td>B</td></tr><tr><td>10</td><td>... I get presents or discounts</td><td>C</td><td>C</td><td>C</td><td>C</td><td>C</td></tr><tr><td>11</td><td>... I get aggregated rebates</td><td>C</td><td>C</td><td>C</td><td>C</td><td>C</td></tr><tr><td>12</td><td>... I can customize the website according to my needs</td><td></td><td></td><td></td><td></td><td>b</td></tr><tr><td>13</td><td>... the general terms and conditions are clearly defined</td><td>A</td><td>A</td><td>a</td><td>a</td><td>a</td></tr><tr><td>14</td><td>... the website is well structured</td><td>A</td><td>A</td><td>F</td><td>F</td><td>Af</td></tr><tr><td>15</td><td>... I find the website entertaining</td><td>bd</td><td>ad</td><td>d</td><td>d</td><td>bd</td></tr><tr><td>16</td><td>... the website offers online games</td><td>D</td><td>D</td><td>D</td><td>D</td><td>D</td></tr><tr><td>17</td><td>... I can find information about a company&#x27;s business policy</td><td> $Af^a$ </td><td>ae</td><td>A</td><td>A</td><td>A</td></tr><tr><td>18</td><td>... data can be transmitted over an encrypted connection</td><td>A</td><td>A</td><td>A</td><td>A</td><td>A</td></tr><tr><td>19</td><td>... I can view my personal data at any time</td><td>A</td><td>A</td><td>af</td><td>Af</td><td>A</td></tr><tr><td>20</td><td>... I receive the ordered products and services on time</td><td>A</td><td>af</td><td>F</td><td>F</td><td>af</td></tr><tr><td>21</td><td>... I like the website</td><td>a</td><td>a</td><td>d</td><td>d</td><td>ad</td></tr><tr><td>22</td><td>... I can download software</td><td>D</td><td>aD</td><td>D</td><td>D</td><td>D</td></tr><tr><td>23</td><td>... I can participate in sweepstakes</td><td>D</td><td>D</td><td>d</td><td>d</td><td>D</td></tr><tr><td>24</td><td>... I can send SMS free of charge</td><td>D</td><td>D</td><td>D</td><td>D</td><td>D</td></tr><tr><td></td><td>CL: classical factor analysis with logit transformation</td><td colspan="5">A-F: factors</td></tr><tr><td></td><td>RL: robust factor analysis with logit transformation</td><td colspan="5">Upper-case letters: factor</td></tr><tr><td></td><td>CO: classical factor analysis with original data</td><td colspan="5">Loadings &gt;0.5</td></tr><tr><td></td><td>C1-5: classical factor analysis with five categories</td><td colspan="5">Lower-case letters: factor</td></tr><tr><td></td><td>RO: robust factor analysis with original data</td><td colspan="5">Loadings between 0.3 and 0.5</td></tr></table>

<sup>a</sup> Negative loading.

Some factors were quite stable across different methods of analysis, e.g. factor ‘C’, while others such as ‘B’ and ‘D’ slightly changed across the methods, and factors ‘A’, ‘E’, and ‘F’ were rather unstable: the latter ones were influenced by the method chosen by the researcher. Moreover, variables such as ‘12’ or ‘21’ were poorly represented by all factor models, which showed an additional advantage of factor analysis over principal component analysis, because the interpretation of the resulting factors would be improved by suppressing ‘‘unsuitable’’ variables.

Thus if the required distributional assumptions are ignored, the resulting factors will have a slightly different composition from an analysis where the data was appropriately transformed. But even after transformation, data inhomogeneities or outliers may still be present, leading to a biased classical analysis.

## 5.3. The impact of noise

Robust methods also help by achieving better stability of the results with respect to noise, which may be caused by inaccurate answers from respondents; e.g., the slider bars may have been moved to an arbitrary position, resulting in a less pronounced structure and leading to change in the factors. The impact of noise can be simulated by replacing data records with uniformly distributed data in the range 1–100, and subsequently comparing the resulting loadings with the matrix obtained for the original data. Since both the loadings and the factors can change position, a useful comparison is only possible by using a target rotation [3]. The goal of the rotation is thus to bring the loading pattern resulting from the modified data as close as possible to the original loadings, using an orthogonal or oblique rotation. Our simulation was made for the untransformed as well as for the logittransformed data. We used classical and robust factor analysis with Oblimin rotation, and replaced 10, 20, and 30% of the observations with uniform random noise. For each percentage, 100 simulations were made. The results can be seen in Fig. 6, with the vertical axis showing the absolute frequencies and the horizontal depicting the loading differences.

For the untransformed data, robust factor analysis shows a much higher stability than classical factor analysis if 10% or 20% of the data are noise. For 30%, the amount of instability for robust factor analysis is comparable to that of classical factor analysis. For the logit-transformed data the difference in the behavior of classical and robust factor analysis becomes marginal and the stability is in between both cases (classical and robust FA) for the original data. This can be explained by the fact that the logit transformation reduces the influence of (multivariate) data outliers.

## 5.4. Data interpretation

At this point, we decided to pay attention to the interpretation of the results, choosing a principal factor analysis, since we were interested in discovering the latent structure behind our set of variables. Usually the task of finding adequate terms for the factors is an ex-post process of the research. Since our main focus was on the comparison of methods and since we obtained significantly varying results, we decided to use qualitative studies to find adequate factor labels. Although triangulation of different methods has been strongly recommended, few reported projects have made use of it. In our paper we applied different methods to the same problem, enabling us to cross-validate our findings and thus improve their accuracy.

Since the results of the quantitative factor analyses were open to several interpretations, we decided to pursue a qualitative approach to discover which factor solution resembled a human decision making process. A major advantage of such a study was that we were able to make sure that all of the items were fully understood by the participants. We asked our subjects to sort the items; i.e. it was the group’s task to find a ‘factor structure’ by discussion and general agreement. In order to account for any potential bias caused by their prior knowledge, we decided to use two different groups for each stage of the survey. The first consisted of five experts with a sound knowledge of the Internet working at a large university; the second consisted of five graduate business students.

![](/api/attachments/6BE7B47Q/fulltext/images/aa1ae1e58a1416777df5539d667ef4f6a289774bbe8cc226be6db6b6027d1c3b.jpg)

![](/api/attachments/6BE7B47Q/fulltext/images/57401d9942978534518cc77ec60c6df78f25edb8d9d0d63e37b9352648513ba7.jpg)  
Fig. 6. Stability of classical and robust factor analysis for untransformed and logit-transformed data

We performed two rounds of the sorting studies and the results are shown in Fig. 7.

In round A, each group was asked to sort the items and agree on a common order. The experts decided on seven groups (‘‘Benefits and Incentives’’, ‘‘Clarity and Transparency’’, ‘‘Individualization’’, ‘‘Responsiveness’’, ‘‘Interactivity’’, ‘‘Entertainment’’, ‘‘No Interpretation’’), whereas the students agreed on six groups (‘‘Delivery’’, ‘‘Trust’’, ‘‘Individualization’’, ‘‘Contact’’, ‘‘Service and Entertainment’’, ‘‘No Interpretation’’). Subsequently, all subjects decided which categories were most suitable, i.e. the two groups were asked to merge their categories. They agreed on six groups ‘‘Benefits, Incentives’’, ‘‘Transparency, Trust’’, ‘‘Individualization’’, ‘‘Responsiveness, Contact, and Interactivity’’, ‘‘Service, Entertainment’’ and ‘‘No Interpretation’’.

In round B, we formed two new groups, again consisting of five experts working at a university and five business students, none of whom had participated in the first round. Their task was to assign the items to the categories defined in round A. Although the objective was much more clear-cut than that of the first, there was still considerable disagreement between the two groups on five items (see Fig. 7). Since this was a qualitative study with small sample sizes, we did not test for significant differences due to demographic and socioeconomic attributes of the two groups.

Interestingly, the agreements and disagreements of the human evaluation strongly reflected the pattern of the loadings in the different factor analyses. Those items which were assigned to the same factor in round B are printed in boldface. Subsequently, we compared the final results of round B of the qualitative sorting study with the results of the various forms of quantitative factor analysis.

The first group ‘‘Benefits and Incentives’’ was represented by two factors (C and D) in the quantitative analysis, with all factor analyses unambiguously yielding the same result. The problems of allocating items pertaining to ‘‘Transparency and Trust’’ were clearly reflected by the quantitative analyses. While all analyses assigned the same factor ‘A’ to items 13 and 18 (although some were below the threshold of 0.5), items 17 and 19 could not be clearly assigned. ‘‘Individualization’’, which was rather straightforward in the qualitative analysis, clearly showed differences in the various factor analyses performed. The RFA with logit transformation differentiated between two pairs of items (01, 02 vs. 03, 09), while all other analyses identified a single factor. Except for the robust analysis with the original data, no quantitative analysis showed a loading of >0.3 for item 12. The group ‘‘Responsiveness, Contact, and Interactivity’’ consisted of two different factors according to the quantitative analyses (04, 05 vs. 06, 07). The different views of the students and experts which items belong to the group ‘‘Service and Entertainment’’ were reflected in the robust factor analysis with logit transformation. Items that were undisputed among the subjects as well as the others (08, 17, 23) loaded on either factor ‘A’ or ‘D’. Similar results were produced by the robust analysis of the original data and the classical analysis with logit transformation. These results suggest that the uncertainty of experts and students was reflected by inhomogeneities of the survey data leading to unstable factors.

![](/api/attachments/6BE7B47Q/fulltext/images/76e28248b0b56f6b115eac1aac2298e8387816d6e5a562d54d7d97383ce01f5f.jpg)  
Fig. 7. Results of qualitative sorting study.

## 6. Discussion and conclusion

Using factor analysis for exploratory data analysis leaves the researcher with a multitude of options, such as various types of data transformation, the choice of the factor extraction method, factor rotation, and the number of factors to be chosen. Frequently, these choices, as reported in published articles, are not theoretically justified and basic statistical assumptions are violated. We showed how these choices influenced the results. Also, we presented the concept of robust factor analysis, which makes less restrictive assumptions about data distribution than classical factor analysis and reduces the influence of outliers. We showed striking differences when comparing the biplots of classical and robust factor analyses or using different methods of data transformation. To triangulate our methods, we also conducted a qualitative study to identify names for individual factors. This revealed that some groups of variables were clearly assigned to the same factors of all factor analysis methods but that across the various factor analyses, some of the items changed their contribution to the factors. For our sample dataset, a robust factor analysis on the logit-transformed data was necessary to deal with skewed and noisy raw data. The robust solution turned out to be more stable than its classical counterpart. In general, robust factor analysis is less sensitive to deviation from model assumptions, such as normality or inhomogeneity of the observations, and might therefore be a better solution for researchers who have to deal with data containing noise.

Our results also showed the limitations of EFA. It is impossible to find a single best solution and justify it. We therefore used three different criteria to evaluate the quality of the chosen approach. Initially, the method has to be ‘correct’ in terms of basic statistical assumptions. Then, the researcher has to make a choice between several options, which might lead to different solutions. We showed that the interpretability of the results may vary significantly in the different solutions, and that the researcher should carefully select among the correct solutions. The robust solution may not necessarily be easier to interpret. However, the robust factor analysis provides superior results on stability when the amount of noise is moderate. A final limitation pertains to the scale being used: the visual analogue scale is based on a completely different measurement approach than Likert scales.

## References

[1] R. Agarwal, V. Venkatesh, Assessing a firm’s web presence: a heuristic evaluation procedure for the measurement of usability, Information Systems Research 13 (2), 2002, pp. 168–186.

[2] S. Ba, P.A. Pavlou, Evidence of the effect of trust building technology in electronic markets: price premiums and buyer behavior, MIS Quarterly 26 (3), 2002, pp. 243–268.

[3] C.A. Bernaards, R.I. Jennrich, Gradient projection algorithms and software for arbitrary rotation criteria in factor analysis, Educational and Psychological Mea surement 65 (5), 2005, pp. 676–696.

[4] E. Blair, G.M. Zinkhan, Nonresponse and generalizability in academic research Journal of the Academy of Marketing Science 34 (1), 2006, pp. 4–7.

[5] T.A. Carte, C.J. Russell, In pursuit of moderation: nine common errors and their solutions, MIS Quarterly 27 (3), 2003, pp. 479–501.

[6] W.W. Chin, A. Gopal, D.W. Salisbury, Advancing the theory of adaptive structuration: the development of a scale to measure faithfulness of appropriation, Information Systems Research 8 (4), 1997, pp. 342–367.

[7] W.W. Chin, D.W. Salisbury, A. Gopal, P.R. Newsted, Authors’ reply to Allport and Kerler, Information Systems Research 14 (4), 2003, pp. 360–363.

[8] J.M. Conway, A.I. Huffcutt, A review and evaluation of exploratory factor analysis practices in organizational research, Organizational Research Methods 6 (2), 2003, pp. 147–168.

[9] L.R. Fabrigar, D.T. Wegener, R.C. MacCallum, E.J. Strahan, Evaluating the use of exploratory factor analysis in psychological research, Psychological Methods 4 (3), 1999, pp. 272–299.

[10] C. Green, J. Brazier, M. Deverill, Valuing health-related quality of life. A review of health state valuation techniques, Pharmacoeconomics 17 (2), 2000, pp. 151–165.

[11] J. Karimi, T.M. Somers, Y.P. Gupta, Impact of environmental uncertainty and task characteristics on user satisfaction with data, Information Systems Research 15 (2), 2004, pp. 175–193.

[12] C. Koh, S. Ang, D.W. Straub, IT outsourcing success: a psychological contract perspective, Information Systems Research 15 (4), 2004, pp. 356–373.

[13] R.H. Lam, K.H. Lim, Emotions in online shopping: fulfilling customer’s needs through providing emotional features and customizing website features, in: Proceedings of the 25th International Conference on Information Systems, Washington DC USA. 2004 pp. 877-888

[14] A.S. Lee, R.L. Baskerville, Generalizing generalizability in information systems research, Information Systems Research 14 (3), 2003, pp. 221–243.

[15] R.C. MacCallum, K.F. Widaman, K.J. Preacher, S. Hong, Sample size in factor analysis: the role of model error, Multivariate Behavioral Research 36 (4), 2001, pp. 611–637.

[16] N.K. Malhotra, S.S. Kim, J. Agarwal, Internet users’ information privacy concerns (IUIPC): the construct, the scale, and a causal model, Information Systems Research 15 (4), 2004, pp. 336–355.

[17] M O’Neill, A. Palmer, C. Wright, Disconfirming user expectations of the online service experience: inferred versus direct disconfirmation modeling, Internet Research 13 (4), 2003, pp. 281–296.

[18] J.W. Palmer, Web site usability, design, and performance metrics, Information Systems Research 13 (2), 2002, pp. 151–167.

[19] R.A Peterson, A meta-analysis of variance accounted for and factor loadings in exploratory factor analysis, Marketing Letters 11 (3), 2000, pp. 261–275.

[20] S. Petter, D. Straub, A. Rai, Specifying formative indicators in information systems research, MIS Quarterly 31 (4), 2007, pp. 623–656.

[21] G. Pison, P.J. Rousseeuw, P. Filzmoser, C. Croux, Robust factor analysis, Journal of Multivariate Analysis 84 (1), 2003, pp. 145–172.

[22] K.J. Preacher, R.C. MacCallum, Reparing Tom Swift’s electric factor analysis machine, Understanding Statistics 2 (1), 2003, pp. 13–43.

[23] C. Reimann, P. Filzmoser, R.G. Garrett, Factor analysis applied to regional geochemical data: problems and possibilities, Applied Geochemistry 17 (3), 2002, pp 185–206.

[24] P.J. Rousseeuw, K. Van Driessen, A fast algorithm for the minimum covariance determinant estimator, Technometrics 41 (3), 1999, pp. 212–223.

[25] A.H. Segars, V. Grover, Re-examining perceived ease of use and usefulness: a confirmatory factor analysis, MIS Quarterly 17 (4), 1993, pp. 517–525.

[26] G. Torkzadeh, G. Dhillon, Measuring factors that influence the success of Internet commerce, Information Systems Research 13 (2), 2002, pp. 187–204.

[27] H. Treiblmaier, Building relationships between consumers and online vendors: empirical findings from Austria, in: Proceedings of the Fourth Annual Workshop on HCL Research in MIS Las Vegas USA 2005

[28] R.Y. Wang, D.M. Strong, Beyond accuracy: what data quality means to data consumers, Journal of Management Information Systems 12 (4), 1996, pp. 5–33.

[29] K.F. Widaman, Common factor analysis versus principal component analysis: differential bias in representing model parameters? Multivariate Behavioral Research 28 (3). 1993 pp. 263-311

[30] K. Zhu, K.L. Kraemer, Post-adoption variations in usage and value of e-business by organizations: cross-country evidence from the retail industry, Information Systems Research 16 (1), 2005, pp. 61–84.

## Glossary

Communality: Proportion of a variable’s variance which is explained by a factor structure.

Confirmatory Factor Analysis (CFA): Used to verify the hypothesized factor structure of a set of observed variables. The researcher specifies the relationships between the variables a priori and uses CFA to test the hypotheses.

Eigenvalue: Represents the sum of squared loadings for a factor. It is frequently used to determine the number of factors.

Exploratory Factor Analysis (EFA): Used to find an underlying structure between a set of observed variables without specifying a priori relationships.

Factor Loading: (see: Loading)

Heteroscedasticity: Refers to a situation when the variance of the variable differs. Various statistical tests require the equality of the variances (homoscedasticity). Kaiser–Meyer–Olkin: (see: Measure of Sampling Adequacy (MSA))

Loading: Denotes (for standardized data) the correlation between a variable and a factor.

Measure of Sampling Adequacy (MSA): A statistic which is calculated both for the entire correlation matrix and each individual variable. It is used to measure the appropriateness of the raw data to apply a factor analysis.

Minimum Covariance Determinant (MCD) estimator: The minimum covariance determinant (MCD) estimator is a highly robust estimator of multivariate location and scatter. The objective is to find those h observations whose sample covariance matrix has the lowest determinant. The value h determines the robustness, and it can be chosen between about half the observations and all observations.

Rotation: A transformation of the factor loadings in order to approximate a simpler and more meaningful structure.

Orthogonal: Group of rotation methods which imply that the extracted factors are uncorrelated.

Varimax: The variances of the squared factor loadings for each factor are considered, and the sum of these variances is maximized.

Quartimax: The sum of all factor loadings to the power of four is maximized.

Equamax: Maximizes a weighted sum of the Varimax and Quartimax criteria. Oblique: Group of rotation methods which allow the extracted factors to be correlated.

Quartimin: Minimizes the sum of the cross products of the squared variable loadings.

Covarimin: Similar to Quartimin, but adjusts for the overall size of the squared loadings of each factor.

Oblimin: Generalizes and combines Quartimin and Covarimin rotation.

Promax: Tries to fit a target matrix which has a simple structure.

McCammon: Minimizes an entropy ratio.

Principal Component Analysis: Reduces the number of observed variables to a smaller number of principal components, which account for the essential amount of variance in the data.

Principal Factor Analysis: Similar to principal component analysis, but accounts only for the essential variance that is common to the variables

Scree Plot: Shows the Eigenvalues in descending order of magnitude as a function of the Eigenvalue index. It is used to determine the number of principal components or factors.

Skewness: Measures the asymmetry of a distribution.

Transformation: Changes the distribution of the data set with the usual objective of approximating a normal distribution.

Logit: Mainly used if the observed data are ratios or proportions.

Power: The data are transformed using power functions.

Box–Cox: One particular way of parametrizing the power transformation.

![](/api/attachments/6BE7B47Q/fulltext/images/fca553770d8baa29e81cca16c49a76aacb0a4522c8c78a6dccdc3ce41bad38e1.jpg)

Horst Treiblmaier is an Associate Professor of Infor mation Systems at the Vienna University of Economics and Business, where he received a Ph.D. in Management Information Systems in 2001. He worked as a Visiting Professor at the University of California, Los Angeles, the University of British Columbia, the University of Technology in Sydney and the Kazakhstan Institute of Management. Economics and Strategic Research (KIMEP). His research and teaching interests include electronic marketing, web site analysis, business statistics, human computer interaction and programming.

![](/api/attachments/6BE7B47Q/fulltext/images/d870efab5584938970f2ad0a32420d3890649bc6db0f5a69b12564d34085c52c.jpg)

Peter Filzmoser is an Associate Professor of Statistics at the Vienna University of Technology. He worked as a Visiting Professor at the University of Vienna, the University of Toulouse I, and the Belarusian State University. His research and teaching interests include robust statistics, multivariate statistical methods, and computational statistics.
