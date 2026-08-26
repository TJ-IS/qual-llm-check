---
otero_id: 530
otero_key: "YWGBXHZH"
title: "Assessing Between-Group Differences in Information Systems Research: A Comparison of Covariance- and component-Based SEM1"
authors: "Israr Qureshi; Deborah Compeau"
year: "2009"
journal: "MIS Quarterly"
doi: "10.2307/20650285"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Assessing Between-Group Differences in Information Systems Research: A Comparison of Covariance- and Component-Based SEM
Author(s): Israr Qureshi and Deborah Compeau
Source: MIS Quarterly, Vol. 33, No. 1 (Mar., 2009), pp. 197-214
Published by: Management Information Systems Research Center, University of Minnesota
Stable URL: http://www.jstor.org/stable/20650285
Accessed: 30-12-2015 14:50 UTC

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# ASSESSING BETWEEN-GROUP DIFFERENCES IN INFORMATION SYSTEMS RESEARCH: A COMPARISON OF COVARIANCE- AND COMPONENT-BASED SEM $^{1}$

By: Israr Qureshi
Department of Management and Marketing
Hong Kong Polytechnic University
Hung Hom, Hong Kong
HONG KONG
msisrar@inet.polyu.edu.hk

Deborah Compeau
Richard Ivey School of Business
The University of Western Ontario
London, Ontario N6A 3K7
CANADA
dcompeau@ivey.uwo.ca

## Abstract

Multigroup or between-group analyses are common in the information systems literature. The ability to detect the presence or absence of between-group differences and accurately estimate the strength of moderating effects is important in studies that attempt to show contingent effects. In the past, IS scholars have used a variety of approaches to examine these effects, with the partial least squares (PLS) pooled significance test for multigroup becoming the most common (e.g., Ahuja and Thatcher 2005; Enns et al. 2003; Zhu et al. 2006). In other areas of social sciences (Epitropaki and Martin 2005) and management (Mayer and Gavin 2005; Song et al. 2005) research, however, there is greater emphasis on the use of covariance-based structural equation modeling multigroup analysis. This paper compares these two methods through Monte Carlo simulation. Our findings demonstrate the conditions under which covariance-based multigroup analysis is more appropriate as well as those under which there either is no difference or the component-based approach is preferable. In particular, we find that when data are normally distributed, with a small sample size and correlated exogenous variables, the component-based approach is more likely to detect differences between-group than is the covariance-based approach. Both approaches will consistently detect differences under conditions of normality with large sample sizes. With non-normally distributed data, neither technique could consistently detect differences across the groups in two of the paths, suggesting that both techniques struggle with the prediction of a highly skewed and kurtotic dependent variable. Both techniques detected the differences in the other paths consistently under conditions of non-normality, with the component-based approach preferable at moderate effect sizes, particularly for smaller samples.

Keywords: Multigroup analysis, Monte Carlo simulation, covariance-based structural equation modeling, partial least squares, measurement invariance, research methodology, nested models, pooled significance test

## Introduction

The ability to assess between-group differences in theoretical models is important to the information systems literature as numerous studies focus on these differences (e.g., Hsieh et al. 2008; Keil et al. 2000; Zhu et al. 2006). Statistical means to assess them are essential. A variety of means of assessing such relationships exist, including ANOVA and moderated regression. As researchers have developed and tested structural equation models, means for testing between-group differences in these second generation techniques have also been developed (e.g., Chin 2003; Chin et al. 2003; Kenny and Judd 1984). Different statistical techniques, however, have different assumptions and thus may produce different results. Understanding the differences between methods of assessment is important, then, to understand and compare past findings. The purpose of this paper is to compare two common methods of assessing between-group differences in SEM. The first method uses partial least squares (PLS) and involves comparing and testing corresponding path coefficients for different groups through tests of the differences, typically using t-tests (Ahuja and Thatcher 2005; Enns et al. 2003; Hsieh et al. 2008; Zhu et al. 2006). The second approach, less common in information systems research, but more common in other areas of social science and management research, involves multigroup analysis in covariance-based SEM through application software such as EQS, Mplus, LISREL, and AMOS (Epitropaki and Martin 2005; Mayer and Gavin 2005; Rothbard 2001). Both approaches have benefits. It has been argued in the literature that the PLS approach requires fewer distributional assumptions about the data (e.g., Cassel et al. 1999) and works well with smaller sample sizes (e.g., Barclay et al. 1995; Chin 1998b). There is, however, recent debate about the power of PLS to detect effects at smaller sample sizes (Goodhue et al. 2006, 2007; Marcoulides and Saunders 2006). PLS remains better at handling formative constructs (Petter et al. 2007). Methods have been proposed for assessing formative constructs in covariance-based SEM (e.g., Diamantopoulos and Winklhofer 2001) and Mackenzie et al. (2005) suggest ways of getting around the identification problem associated with formative constructs, but they are difficult to use when the formative construct of interest is the ultimate (terminal) dependent variable. On the other hand, the covariance-based approach includes a direct test of measurement invariance and structural invariance, which is not available in component-based SEM software. Perhaps more importantly, it allows the researcher to constrain the measurement models of the groups to be equal, thus ensuring that tests of the differences in structural paths are uncontaminated by differences in measurement properties across the two groups.

While many studies provide comparisons of covariance and component-based SEM, they focus on the general assessment of these two techniques (Fornell and Bookstein 1982). No study, to our knowledge, has assessed the differences in the two methods for assessing between-group differences. Yet, in a recent comparison of interaction effects in PLS and multiple regression, Goodhue et al. (2007) found that even though for general assessment PLS performs better, for interaction effects, multiple regression has more power than PLS. Thus, we believe that despite the large number of studies comparing component-based and covariance-based methods in general, their power to detect between-group path differences remains under-explored.

We compare the techniques with a Monte Carlo simulation, where the two approaches are used to assess differences in path coefficients for simulated data with known parameters. Examining the ability of the techniques to reproduce known parameters is important for assessing statistical techniques. Our design examines the influence of various parameters of research design and data, such as sample size, underlying distribution of the observed variables, number of indicators used to measure the constructs, extent of correlation among the exogenous latent factors, and extent of variation in path coefficients across the groups.

## Between-Group Tests of Differences

Three methods of assessing between-group differences in SEM have been commonly reported in the information systems and management literatures $^{2}$ . The first approach, introduced by Chin (2000), involves estimating model parameters for each group separately using component-based SEM (e.g., PLS) and then performing a between-group test of significance across the groups (e.g., Hsieh et al. 2008; Keil et al. 2000; Venkatesh and Morris 2000). The moderating effect of group membership is examined using a t-test with pooled standard errors. This method is generally labeled as the parametric approach (PA) (Henseler 2007).

The second method is between-group analysis using covariance-based SEM (e.g., Jöreskog 1971; Raykov and Marcoulides 2006). In this paper, we refer to this technique as the covariance SEM approach (CSA). In CSA, measurement model invariance is tested first, to see if the measurement models across the groups are comparable (Cheung and Rensvold 2002). Once measurement equivalence is established or constrained to equality, the between-group structural equation model is tested. In the default model, all of the path coefficients are allowed to vary freely across the two groups.

Subsequently, equality constraints are imposed on the path coefficients. If imposition of equality constraint deteriorates the model fit significantly, then the path coefficients across the groups differ significantly (Byrne 2001; Schumacker and Lomax 2004). This method is not common in the IS literature although there are some isolated examples (e.g., McCoy et al. 2005). In other disciplines this is one of the most common methods for estimating path differences between the groups within the SEM framework (Epitropaki and Martin 2005; Mayer and Gavin 2005; Rothbard 2001).

The third approach is the product indicator approach, originally proposed for covariance-based SEM (Kenny and Judd 1984) and later implemented in PLS (PLS-PI) (Chin et al. 2003). In this approach, a new construct is created, whose indicators are the products of each indicator of construct A with each indicator of construct B. When using PLS-PI to compare two groups, a dummy variable is used to represent the groups and then this variable is multiplied by the indicators of the desired construct(s) to test the moderating effects of group membership.

In this study, we are focusing on between-group differences in naturally occurring groups such as male and female (Byrne 1994) and cross-cultural differences (Reise et al. 1993; Riordan and Vandenberg 1994). These groups may have differences in their measurement models or in their structural models or in both.

Between-group analysis in SEM provides an option for testing measurement invariance or, if desirable, imposing it for isolating structural differences. “Measurement invariance is critically important when comparing groups. If measurement invariance cannot be established, then the finding of a between-group difference cannot be unambiguously interpreted” (Cheung and Rensvold 2002, p. 233). This is because in the absence of measurement invariance we do not know whether the observed differences in path coefficients are on account of true relationships between latent constructs or due to different psychometric responses (Cheung and Rensvold 2002).

Testing measurement invariance is not possible with the product indicator approach, whether in the component-based or covariance-based approach, and we believe this approach is more suitable for continuous moderating variables. It can be reasonably argued that in the case of continuous moderators, the sample is drawn from a single population and measurement invariance may or may not be an issue. For dichotomous variables representing naturally occurring groups, however, samples are presumably drawn from different populations, and thus lack of measurement invariance may confound the structural differences, which are labeled sometimes as gamma differences (Carte and Russell 2003). Thus, we did not include PLS-PI in our study, as it fits better with a situation where two latent constructs (each of which has multiple indicators and each of which is measured on a continuous scale) interact to influence a third construct (Henseler and Fassott 2009; Rigdon et al. 1998).

Based on our assessment of the current state of the literature, we chose to focus on the two most commonly used techniques for assessing between-group differences in path coefficients within SEM: the parametric approach (PA) and the covariance SEM approach (CSA).

## Monte Carlo Simulation to Compare Approaches

The structural model we used for simulation of the data includes four constructs and is shown in Figure 1. Two exogenous constructs (A and B) have direct effects on a third construct (C), which in turn has a direct effect on the fourth construct (D). One of the exogenous constructs (A) also has a direct effect on D. This model includes a mix of mediating and direct effects typical of those found in papers that test structural equation models, and has an moderate level of complexity. The number of observed variables in SEM Monte Carlo studies ranges from 4 to 33 (average 11.6) (Hoogland and Boomsma 1998). Our model includes 12 observed indicators for those models that have 3 indicators per construct and 24 observed indicators for those models that have 6 indicators per construct.

Given our goal, to compare the performance of component-based (PA) and covariance-based (CSA) approaches to detecting between-group differences, we investigated the two methods under multiple conditions. We chose six conditions, based on our review of the literature, to be most influential in the performance of the techniques.

First, we systematically varied the magnitude of the between-group path differences. We did this by keeping the path coefficients of one group (the baseline model) fixed and changing the coefficients in the other group (comparison models) to produce differences in path coefficients of 0.05, 0.15, 0.25, 0.35, and 0.45. These path differences provide a range in differences (effect size) from small to large (Cohen 1988).

Figure 1 shows the path coefficients for the baseline and comparison models. Since our purpose was to assess the detection of between-group differences in observed effects, we compared our baseline model (with predetermined values for each of the path coefficients as shown in Figure 1) to five comparison models. These comparison models can be thought of as representing different subgroups where the magnitude of the paths differs by varying amounts. For each of the six models, baseline as well as comparison, 500 samples were generated. Parameters for the baseline model were, as shown in the Figure 1, set to $\mathrm{b}_1 = 0.05$ , $\mathrm{b}_2 = 0.2$ , $\mathrm{b}_3 = 0.35$ , and $\mathrm{b}_4 = 0.6$ . The assessment of group differences was conducted by comparing the 500 samples of the baseline model against the 500 samples of each comparison model (i.e., C1, C2, C3, C4, and C5). Parameters of the first comparison model (C1) were constructed to create small differences in path values ( $|\mathrm{d}(\mathrm{b_i - b^{*}_i})| = 0.05$ ) from the baseline model ( $\mathrm{b^{*}_1 = 0.1}$ , $\mathrm{b^{*}_2 = 0.25}$ , $\mathrm{b^{*}_3 = 0.4}$ , and $\mathrm{b^{*}_4 = 0.55}$ ). Models C2 through C5 had progressively larger differences as shown in the table embedded in the Figure 1.

Figure 1. Simulation Model  
![](/api/attachments/YWGBXHZH/fulltext/images/b0c2b6e2e396d7acefe877cf9abdf453a66964d90b091aa8bf5822b8c2d486bd.jpg)

We focused our analysis on testing differences in the structural model rather than differences in the measurement model, which was by design invariant. In order to assure that the test of structural model invariance is fair, our design ensured measurement model invariance by generating data with

(1) corresponding measurement means (intercepts) equal across the groups (fixed at zero)

(2) corresponding measurement weights equal across the groups

(3) corresponding measurement residuals equal across the groups

(4) equivalence of corresponding factor means across the groups (fixed at zero)

(5) equivalence of corresponding factor variance across the groups (fixed at one)

Multiple group analysis in Mplus was used to test measurement invariance of factors using $\chi^{2}$ difference tests for a set of nested models (Muthén and Muthén 2006). As all of the observed variables (i.e., indicators of the factors) were continuous, the measurement parameters of interest in this case were the intercepts, factor loadings, and residual variances of the factor indicators, and means of factors (Muthén and Muthén 2006). In most disciplines invariance of intercepts and factor loadings are considered sufficient for measurement invariance; however, some disciplines also require invariance of residual variances and factor means (Cheung and Rensvold 2002; Marsh and Hocevar 1985; Muthén and Muthén 2006; Steenkamp and Baumgartner 1998; Vandenberg and Lance 2000). We wanted to test the ability of PA and CSA to capture structural path differences in the most restrictive conditions of measurement invariance and thus considered all four elements.

We used $\chi^{2}$ differences and CFI differences to test for measurement invariance (Cheung and Rensvold 2002; Little 1997; Marcoulides et al. 2008; Muthén and Muthén 2006; Raykov and Marcoulides 2006). A nonsignificant $\chi^{2}$ difference and CFI difference below 0.05 indicates model invariance (Little 1997; Marcoulides et al. 2008; Raykov and Marcoulides 2006). However, Chung and Rensvold (2002) recommend a more conservative 0.01 cutoff level for CFI difference, a suggestion which we adopted.

The default model had no parameters constrained to equality across groups. Subsequently, equality constraints for each of the parameters were imposed. The $\chi^{2}$ value and degrees of freedom of the less restrictive model were subtracted from the $\chi^{2}$ value and degrees of freedom of the nested, more restrictive model.

For each successive model, the $\chi^{2}$ difference was found to be nonsignificant (p<.05), indicating that imposing these constraints did not significantly worsen the model fit. All but 38 samples passed the rigorous invariance test of a CFI difference less than 0.01. This represents less than 0.1 percent of the 48,000 total samples generated for this study. Out of 38 samples, 34 were from non-normal datasets. We resimulated these 38 samples and checked their measurement invariance applying the method outlined above. Based on the above assessments, we are confident that we simulated the samples for the two groups with measurement invariance. We also compared the default model directly with the most restrictive model (that had all the measurement constraints in place) and found that the $\chi^{2}$ difference value was not significant; in addition, the CFI difference was less than 0.01.

The second feature included was sample size, with two levels (n = 100 and n = 500). Since the sample size requirement of PLS versus covariance-based SEM is one of the most commonly cited differences (e.g., Goodhue et al. 2007; Marcoulides and Saunders 2006) we included it as an important parameter of our Monte Carlo study. We used sample sizes of 100 and 500 as representative of small and large samples. The sample size between the groups was kept the same to take into account that PA method works reasonably well if sample sizes are similar (Chin 2003, p. 34).

The number of indicators per construct was included as a third factor, following the suggestion of Chin et al. (2003) to test the effect of a change in the number of indicators. In the IS literature, the average number of indicators used is three (Chin et al. 2003), which is equal to the minimum recommended indicators per construct in the SEM literature (Bollen 1989). Therefore, we decided to use three indicators as the first level for the factor. We compared this with six indicators, following prior studies (e.g., Chin 2003, 2005).

For the models that had three indicators for each construct the loadings were set at 0.7, 0.8, and 0.9. For the models that had six indicators for each construct, the loadings were 0.7, 0.8, 0.9, 0.7, 0.8, and 0.9. Three different loadings for the items of the same construct were chosen as it simulates more closely the conditions of real data, yet at the same time the pattern of loadings was kept constant across the constructs to avoid any confounding effects (Paxton et al. 2001). This type of loading pattern is common in the literature (e.g., Goodhue et al. 2006). Measurement means were fixed at zero for all of the observed indicators (in both groups), and corresponding measurement weights (loadings) were equal for both groups. In addition, corresponding measurement residuals were equal for both groups. For models with three indicators per construct, the measurement residuals were respectively .51, .36, and .19, whereas those for models with six indicators, they were .51, .36, .19, .51, .36, and .19. Means and variances of all the latent variables were fixed at zero and one respectively.

The fourth factor included was the presence or absence of correlations between exogenous constructs. Since the maximum likelihood estimation technique (which is the basis for covariance-based SEM) utilizes full information, in comparison to PLS, we expect it will be more affected by changes in correlations between exogenous variables. To test this possibility in the context of between-group analysis, the correlation between exogenous variables was manipulated. Mplus has a built-in function for generating datasets with the desired correlation between exogenous latent variables. We checked the generated datasets for correlation between exogenous variables using estimation in Mplus and none of the samples had covariances outside the set range of -0.02 to +0.02 (for Corr (A, B) = 0) and 0.38 to 0.42 (for Corr (A, B) = 0.4).

The fifth condition we included as a design feature was normality of the underlying data. This feature was included since past studies have found that normality affects maximum likelihood estimation used in covariance-based SEM more than the partial least squares estimation used in component-based SEM (Chin 1998a; Jöreskog and Wold 1982). In a recent call to compare these two techniques, Marcoulides and

Saunders (2006) explicitly recommend inclusion of this design parameter.

The non-normal data were created using a mixture of two normal subpopulations. Normal data were generated for two classes that have different means and variances for the factor indicators. The combined data are analyzed as though they come from a single population with overall mean of zero and residual variance as fixed (Muthén and Asparouhov 2002; Muthén and Muthén 2002).

The first step followed in this case is to generate data for two classes such that the combination of the data from the two classes has the desired skewness and kurtosis. This is done by allowing one of the classes to represent an outlying group of cases that has different means and variances for the factor indicators. The choice of the proportion of cases in the two classes also affects skewness and kurtosis (Muthén and Muthén 2002).

The non-normal datasets were generated with the indicators of constructs C and D displaying both skewness and kurtosis; the indicators of A and B were normally distributed. We could not also make constructs A and B non-normal, as doing so resulted in data generation errors. The effect of non-normality can be observed on all of the four direct relationships as at least one of the constructs involved has a non-normal distribution. The kurtosis and skewness for the indicators of C were around 3.5 and 3 respectively, whereas those for the indicators of D were around 2.2 and 1.6 respectively. We checked all of the non-normal datasets and those samples that had kurtosis and skewness outside the specified range were removed and replaced by regenerated samples. In total 18 samples had to be regenerated on account of unexpectedly high kurtosis or skewness on the indicators of D.

Finally, the four paths in our baseline model were of different strengths, ranging from weak (0.05) to strong (0.6). We included these different path strengths to examine the effects of different baseline strengths on our results.

We used 500 replications of each model. In their review of Monte Carlo studies, Powell and Schafer (2001) found that replications ranged from 20 to 1,000 (with a median of 200). However, increasingly, scholars are adopting 500 replications as standard (Bentler et al. 2005; Finch 2006; Goodhue et al. 2006).

The datasets were generated using the Monte Carlo facility available in Mplus. This software provides an easy to use interface for generating datasets and has been used in past for proactive Monte Carlo analysis (Marcoulides and Saunders

2006; Paxton et al. 2001). $^{3}$ The component-based SEM between-group test of significance was estimated using partial least squares (PLS graph version 3.0, build 1126) (Chin 2001) and the covariance-based SEM multigroup analysis was performed using AMOS (Version 7.0) with maximum likelihood (ML) estimation (Arbuckle 2005).

## Results

We ran a six-way analysis of variance to investigate the influences on ability to detect between-group differences, with the following factors, described earlier:

(1) Estimation technique (PA versus CSA)

(2) Number of loadings (3 versus 6)

(3) Normality of data (normal versus non-normal)

(4) Sample size (n = 100 versus n = 500)

(5) Correlation among the exogenous (A and B) constructs $(\mathbf{r} = 0, \mathbf{r} = 0.4)$

(6) Magnitude of difference in paths (d = 0.05, 0.15, 0.25, 0.35, 0.45).

Table 1 presents the main effects.

Five of the main effects were significant at p < 0.001. Overall, the larger the sample size and the larger the difference in the paths between the two samples, the more likely are the tests to detect differences. These two factors account for 12.6 percent and 33.3 percent of the variance in the overall mean differences. In addition, models with six loadings and those with normal data make detection of differences in paths more likely. Finally, using CSA rather than PA will result in greater overall detection of between-group population differences. The effect of correlation among the exogenous variables was not significant (p = 0.423), indicating that this factor had no main effect on the results.

Table 2 shows the results in terms of the number of significant differences detected. We report these results in aggregate, in other words not taking into account which path (A→C, B→C, etc.) is being examined. Thus, each cell contains 2000 path comparisons (4 paths × 500 replications). The number indicates the percentage of significant comparisons out of the 2,000 total comparisons at the .05 level.

<table><tr><td colspan="3">Table 1. ANOVA Result (Combined PA and CSA)</td></tr><tr><td>Source of Variance</td><td>Sig.</td><td>Partial Eta Squared</td></tr><tr><td>Model</td><td>.000</td><td>.726</td></tr><tr><td>Estimation technique (0 = PA, 1 = CSA) (E)</td><td>.000</td><td>.002</td></tr><tr><td>Loadings (L)</td><td>.000</td><td>.009</td></tr><tr><td>Normal (0= normal, 1= non-normal ) (N)</td><td>.000</td><td>.060</td></tr><tr><td>Sample size (S)</td><td>.000</td><td>.126</td></tr><tr><td>Correlation among exogenous variables (C)</td><td>.423</td><td>.000</td></tr><tr><td>Difference in paths (D)</td><td>.000</td><td>.333</td></tr><tr><td colspan="3">This was a six-way ANOVA, For sake of space and simplicity, only the main effects are presented. Appendix A shows the entire ANOVA results.</td></tr></table>

<table><tr><td rowspan="3" colspan="3"></td><td colspan="4">Normal</td><td colspan="4">Non-normal</td></tr><tr><td colspan="2">100</td><td colspan="2">500</td><td colspan="2">100</td><td colspan="2">500</td></tr><tr><td>PA</td><td>CSA</td><td>PA</td><td>CSA</td><td>PA</td><td>CSA</td><td>PA</td><td>CSA</td></tr><tr><td rowspan="10"> $r_{AB}=0$ </td><td rowspan="5">3</td><td>.05</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>25</td></tr><tr><td>.15</td><td>0</td><td>0</td><td>40</td><td>76</td><td>0</td><td>25</td><td>50</td><td>41</td></tr><tr><td>.25</td><td>2</td><td>2</td><td>100</td><td>100</td><td>29</td><td>25</td><td>50</td><td>50</td></tr><tr><td>.35</td><td>31</td><td>68</td><td>100</td><td>100</td><td>50</td><td>42</td><td>50</td><td>50</td></tr><tr><td>.45</td><td>74</td><td>98</td><td>100</td><td>100</td><td>50</td><td>50</td><td>50</td><td>50</td></tr><tr><td rowspan="5">6</td><td>.05</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>25</td></tr><tr><td>.15</td><td>0</td><td>0</td><td>79</td><td>98</td><td>0</td><td>25</td><td>50</td><td>50</td></tr><tr><td>.25</td><td>4</td><td>5</td><td>100</td><td>100</td><td>35</td><td>26</td><td>50</td><td>50</td></tr><tr><td>.35</td><td>50</td><td>88</td><td>100</td><td>100</td><td>50</td><td>48</td><td>50</td><td>50</td></tr><tr><td>.45</td><td>82</td><td>99</td><td>100</td><td>100</td><td>50</td><td>50</td><td>50</td><td>50</td></tr><tr><td rowspan="10"> $r_{AB}=0.4$ </td><td rowspan="5">3</td><td>.05</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>25</td></tr><tr><td>.15</td><td>0</td><td>0</td><td>19</td><td>37</td><td>0</td><td>25</td><td>50</td><td>42</td></tr><tr><td>.25</td><td>1</td><td>1</td><td>100</td><td>100</td><td>30</td><td>25</td><td>50</td><td>50</td></tr><tr><td>.35</td><td>16</td><td>46</td><td>100</td><td>100</td><td>50</td><td>42</td><td>50</td><td>50</td></tr><tr><td>.45</td><td>55</td><td>92</td><td>100</td><td>100</td><td>50</td><td>50</td><td>50</td><td>50</td></tr><tr><td rowspan="5">6</td><td>.05</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>25</td></tr><tr><td>.15</td><td>50</td><td>0</td><td>46</td><td>75</td><td>0</td><td>25</td><td>50</td><td>50</td></tr><tr><td>.25</td><td>96</td><td>4</td><td>100</td><td>100</td><td>36</td><td>26</td><td>50</td><td>50</td></tr><tr><td>.35</td><td>98</td><td>70</td><td>100</td><td>100</td><td>50</td><td>48</td><td>50</td><td>50</td></tr><tr><td>.45</td><td>99</td><td>98</td><td>100</td><td>100</td><td>50</td><td>50</td><td>50</td><td>50</td></tr></table>

The main effects of sample size and data normality can be readily seen in Table 2. In all of the cells where n = 500 more differences are detected than in the corresponding cells where n = 100. Similarly, the number of differences detected for the normal data are consistently higher than for the non-normal data. The effect of non-normality on detection of the significance of paths is well established in the SEM literature (e.g., Dijkstra 1983); our findings demonstrate that it is equally important in between-group comparisons.

Detailed examination of the results in Table 2 shows the effects of the six-way interaction (significant at p < 0.001; see Appendix A for more details). For normal data, with a large sample size (n = 500) and moderate to large differences between the groups (D ≥ 0.25), both PA and CSA accurately detect the differences between-group. Thus, the choice of technique will not influence the results. For smaller path differences, CSA seems to be preferable when the sample size is large and the data are normal, although when the number of loadings is small (three indicators), even this technique shows limited power (power = 0.76 when $r_{AB} = 0$ ; power = 0.36 when $r_{AB} = 0.4$ ).

For normal data and small sample sizes (n = 100), the results are more complex, influenced by both correlation among the exogenous constructs and the number of indicators used to measure each construct. The component-based approach (PA) demonstrates higher power when the exogenous constructs are correlated and the number of loadings is higher (six indicators per construct). This effect holds when the path differences are between 0.15 and 0.35. There is no significant difference between PA and CSA for either very small or very large between-group differences. The CSA approach is preferable when the exogenous constructs are correlated if there are few items per construct (three indicators) and when the exogenous constructs are uncorrelated (regardless of number of loadings). For small path differences (D = 0.05 to 0.25), power for either of the techniques is low.

For non-normal data, the patterns are somewhat different. First, it is important to note that, for both techniques, the ability to detect effects for non-normal data is significantly worse than for normal data. Only about half of the effects are detected in even the best cases. The significant paths identified in Table 2 all relate to the paths from A to D and from C to D. None of the differences in the A–C and B–C paths were detected. Appendix B replicates these results for each of the individual paths. We will return to this finding later.

For non-normal data with a large sample size (n = 500) and moderate to large differences between-group (D ≥ 0.25), both PA and CSA detect differences equally. When the magnitude of between-group differences is very small (D = 0.05), the covariance-based approach is preferable, but when the magnitude is small (D = 0.15), then the component-based approach is better. When the sample size is small (n = 100) and data are non-normal, the component-based approach is either equivalent to the covariance-based approach (D = 0.45) or preferable (when D = 0.25 and even sometimes 0.35). When the magnitude of the difference is small (D = 0.05 and D = 0.15) then the covariance-based approach is preferable. These findings are graphically presented in Figure 2.

So far, we have presented aggregate results, in the sense that we did not differentiate whether the results pertained to path A–C, B–C, A–D, or C–D. Table 3 presents the MANOVA results when effects of each factor are assessed separately for each path.

Several differences in the patterns of results shown here are noteworthy. For smaller paths, whether the data are normal or non-normal makes a huge difference. As the path size increases, the effect of normality decreases. Thus, for path b1 (A–C), which was set at 0.05 in the baseline model, normality explains 65 percent of the variance in the results, while for path b4 (C–D) normality explains only 18 percent of the results. By contrast, both sample size and magnitude of path differences are important across all paths, and their importance tends to increase as the strength of the paths increases. The estimation technique also plays a differential role with respect to strength of paths, becoming more important as path size increases.

Two factors do not play a differential role across paths. While the number of loadings is important, it does not seem to play a differential role when it comes to strength of paths. Finally, exogenous latent variable correlation does not seem to play an important role across any of the individual paths.

Our assessment of the findings separately for each path also helps to explain the results for the non-normal data. In our aggregate analysis (Table 2, Figure 2), we showed that neither PA nor CSA could consistently detect effects for non-normal data. The maximum number of effects detected was 50 percent, or 1,000 (1,001 in four cases), which is only half of the number of comparisons. In looking at the data on a path by path basis, we observed that both techniques were detecting the differences in paths for b3 and b4 (where D was the dependent construct), but not those for b1 and b2 (where C was the dependent construct). Virtually none of these path differences were detected, regardless of sample size, effect size, exogenous variable correlation, or number of loadings (Appendix B). We believe this relates to the level of non-normality in construct C versus construct D. The skewness and kurtosis values for C are very high (3.5 and 3) while those for D were only moderate (2.2 and 1.6). Thus, both the component and covariance-based techniques seem to be weak in detecting between-group path differences when the dependent construct is very non-normally distributed. $^{4}$

![](/api/attachments/YWGBXHZH/fulltext/images/cb281217baa420cbdb516160a19beb2dee2829b257e1a70dc835e3ab497bd3e4.jpg)

![](/api/attachments/YWGBXHZH/fulltext/images/f469a359d8d2db2db9f091e3e5f28d4ea7c3d45d30868c16223c28e9cd972313.jpg)

![](/api/attachments/YWGBXHZH/fulltext/images/05038dc5b84f8e61c8a28fcd9d5585823d977357f5916e63c93bba64c81215d3.jpg)

![](/api/attachments/YWGBXHZH/fulltext/images/c15e133379a1684595fbde4ab9bb61428bcbcee007fb42a803efb49aedb9092b.jpg)

![](/api/attachments/YWGBXHZH/fulltext/images/420383c0eec738071aebc1d943474445baa5af3e6281fa9e95d4597d87b7fa68.jpg)

![](/api/attachments/YWGBXHZH/fulltext/images/03ed541f1bb5539f995af3900ab20bb9b84af326b6b2bb74ee873d5c9bc809be.jpg)

![](/api/attachments/YWGBXHZH/fulltext/images/4446dc51485bf1a928e1f124944bf1e8d2eed715f0a1ee0913f413c7cac605d7.jpg)

![](/api/attachments/YWGBXHZH/fulltext/images/b3583edf02f3292b49bfc9e70b2d8c56fc38eb3153406d91374fb9323ce61d03.jpg)

![](/api/attachments/YWGBXHZH/fulltext/images/def923a9d0af409b2097c0b7618c1862f6c2985f9d4e8e9f96b553188650ed1c.jpg)

![](/api/attachments/YWGBXHZH/fulltext/images/84f703e11cd0cab88e80f09eab4117e55cb9108b3ff4a910ce73f847d2b544a7.jpg)

![](/api/attachments/YWGBXHZH/fulltext/images/5e9fbd1ebd7888e73f47b67b78414ee31bb69b9455bd56737f3200839b4d5c4e.jpg)

![](/api/attachments/YWGBXHZH/fulltext/images/a7249376f82aef08901bb4fc0ef02d540a94a5099191970ed6e183e698734a4a.jpg)

![](/api/attachments/YWGBXHZH/fulltext/images/eeaccfdcc6c1b5e5a3c8d90869c30a97c27df047d3864a20901effc0f8a17a70.jpg)

![](/api/attachments/YWGBXHZH/fulltext/images/3f97d997941365d97efefbba694b23c65ae326d797f74686507c5ac0e9d72fcf.jpg)

![](/api/attachments/YWGBXHZH/fulltext/images/bfe13a2b9271440cdbc8046193b43b8ebd2d7efafb341b62a73b33333cf07e0f.jpg)

![](/api/attachments/YWGBXHZH/fulltext/images/7885ff5d4c254b8b2b394729189006c07b105e98b2c1e1860414c678348ddf94.jpg)  
In each graph, the horizontal axis represents the path differences between corresponding paths of the baseline model and comparison models. The vertical axis is the count of significantly different paths (at 0.05). Maximum is 2,000.

Figure 2. Comparison of PA (Parametric Approach) and CSA (Covariance SEM Approach)

<table><tr><td colspan="5">Table 3. MANOVA Results for Each Path</td></tr><tr><td rowspan="2">Source of Variance</td><td colspan="4">Partial Eta Squared</td></tr><tr><td>B1(A-C)</td><td>B2(B-C)</td><td>B3(A-D)</td><td>B4(C-D)</td></tr><tr><td>Model</td><td>.913</td><td>.908</td><td>.933</td><td>.960</td></tr><tr><td>Normal (N)</td><td>.751</td><td>.728</td><td>.045</td><td>.338</td></tr><tr><td>Loadings (L)</td><td>.037</td><td>.033</td><td>.047</td><td>.035</td></tr><tr><td>Sample (S)</td><td>.285</td><td>.324</td><td>.464</td><td>.433</td></tr><tr><td>Correlation (C)</td><td>.000</td><td>.001</td><td>.000</td><td>.001</td></tr><tr><td>Estimation technique (E)</td><td>.000</td><td>.012</td><td>.028</td><td>.185</td></tr><tr><td>Difference in path (D)</td><td>.553</td><td>.530</td><td>.757</td><td>.779</td></tr><tr><td>N × E</td><td>.000</td><td>.012</td><td>.011</td><td>.072</td></tr><tr><td>L × E</td><td>.009</td><td>.007</td><td>.002</td><td>.016</td></tr><tr><td>S × E</td><td>.001</td><td>.001</td><td>.017</td><td>.000</td></tr><tr><td>C × E</td><td>.020</td><td>.016</td><td>.003</td><td>.002</td></tr><tr><td>D × E</td><td>.017</td><td>.032</td><td>.048</td><td>.1</td></tr></table>

For the covariance-based approach, this may reflect the sensitivity of the maximum likelihood estimator to distributional assumptions. When we used an asymptotic distribution free (ADF) estimator on a subset of our samples, the results improved appreciably. Thus, it appears that in cases where the data are non-normal, between-group comparisons will be more reliable when an ADF estimator is used. Further study is needed to establish this conclusively.

For the component-based approach, we do not have a clear-cut explanation. As an estimator, PLS does not make any distributional assumption, so non-normality should not be an issue. On the other hand, as a technique of path comparison, PA does make distributional assumptions on path coefficients that should be equally applicable on normal and non-normal data. We tried a distribution free technique of path comparison with PLS, which was proposed by Henseler (2007) $^{5}$ and described later, on a subset of our data. The results improved marginally but the overall pattern and inferences remained unaffected.

## Discussion

This study extends prior research comparing PLS and covariance-based SEM to the specific case of between-group comparisons. Our findings are consistent with past comparisons, which show the importance of sample size, magnitude of difference being investigated, and normality to the performance of component-based and covariance-based approaches to SEM. Yet at least in the specific case of between-group comparisons, our findings provide some important new insights. We found that sample size, magnitude of difference, and normality were critical factors, which explained a significant portion of the variation in the ability to detect between-group differences.

The importance of magnitude of difference between the groups is unsurprising, reflecting the important role of effect size in the power of a test. Both sample size and normality had been previously examined and shown to be important in the context of covariance-based SEM, but their importance in component-based SEM and specifically in the detection of between-group differences was not well established. We found the component-based approach to perform significantly worse when the sample size was small rather than large, thus reinforcing the arguments of Marcoulides and Saunders (2006) that the component-based approach is not as robust in the case of small sample sizes as has been previously argued, especially when the effect size is small. We found that the effect of normality is critical, particularly in the case of highly non-normal dependent constructs. In such cases, neither PA nor CSA may be able to consistently detect differences in structural model paths across different groups. The effect of more moderate normality is bound up with sample size, number of loadings, and correlation between exogenous constructs.

Other complex interactions are also present in our data, suggesting that the choice of technique depends on a variety of conditions in the data. We summarize our findings with a suggested decision tree for researchers trying to decide how to analyze their data (Figure 3).

These results, in particular those that show the relatively lower power of the component-based technique in several of the conditions we tested, may warrant reexamination of some previous findings in the literature. For example, Keil et al. (2000) hypothesized that the “inverse relationship between level of sunk cost and risk perception will be stronger in cultures lower on uncertainty avoidance” (p. 305). Their between-group analysis using PLS failed to capture the difference even though path coefficients varied from -.05 to -0.16. Zhu et al. (2006) found that only one path in their model was significantly different across EDI users and non-users; all other paths were found to be statistically equivalent. Our analysis provides a potential alternative explanation for these nonsignificant findings, specifically that they might reflect the low power of the technique under some conditions rather than a failure of the theory which predicts differences. This is speculative, but may be of interest to researchers in these domains. We note, however, that this explanation does not affect those cases where significant differences have been observed (e.g., Ahuja and Thatcher 2005; Karahanna et al. 1999). Since our concern is with a potential lack of power, we can have confidence that effects which have been detected are, in fact, truly present.

While our primary focus has been on showing the conditions under which either PA or CSA is more effective, our results

![](/api/attachments/YWGBXHZH/fulltext/images/ed62417748c345f5d0e960eb38adaabab417cd50b78b98bd8ffea4a24b4a1944.jpg)  
Figure 3. Decision Tree for Choosing Between PA and CSA

also show us the conditions under which each technique will be at its most effective in detecting between-group effects. The covariance-based approach is at its most effective when the sample size is large and the data are normally distributed. This is consistent with prior research (e.g., Dijkstra 1983) and we extend it to the context of between-group path differences. The number of items and correlation between the exogenous constructs does not seem to influence these results. The component-based approach is also more effective with large sample sizes. When the sample size is large, this approach also seems to be more effective with normally distributed data. When the sample size is small, the impact of the underlying distribution of the data depends on the magnitude of the difference being detected. If the difference is very small (D = 0.05), normality of the data does not matter (the effect will not be detected regardless). If the difference is very large (D = 0.45) then the effect will be reliably detected with normally distributed data, but not non-normal data. But if the difference is moderate, then the differences are more likely to be detected by the component-based approach when the data are not normally distributed, and this effect is more pronounced when the number of items is small. Thus, normality, effect size, and number of indicators used to measure the constructs interact to influence the effectiveness of the component-based technique.

## Limitations and Future Research

Our results must be understood in the context of the study's limitations. Chief among these is the choice of what design factors we excluded from our study. Our model was complex, involving a six-way interaction and requiring 80,000 between-group model comparisons. Adding design features would increase this exponentially and was beyond the scope of our work. However, exclusion of important features could potentially mask important aspects of the results.

So, what did we choose to exclude, and why? First, we did not investigate the effect of measurement quality on the performance of the two techniques. Our primary concern in this paper was with the differences in structural models. Introduction of measurement variance would have confounded our results. However, we recognize that in field settings different subgroups may have different measurement models as they might interpret a construct differently. To the extent that between-group differences can occur at the level of the measurement as well as the structural model, investigating the effect of measurement variance remains an important avenue for future research.

We also did not consider differences in model complexity. We chose, instead, to examine a model of moderate complexity, typical of those present in IS research. Many Monte Carlo studies use variation in model type (e.g., repeating the analysis for models with two, three, or four structural paths). For this study the structural models were the same throughout. It would be interesting to know, however, the effect of increasing complexity of models on the ability of these two techniques to pick up the difference between the groups. Since covariance-based SEM utilizes full information estimates, we would expect it to be more sensitive to changes in model complexity. In a pilot study to this paper, we performed a Monte Carlo study using a very simple model with three exogenous latent variables predicting one endogenous latent variable. In this simple model, CSA was found to be a more powerful technique compared to PA, except when the magnitude of the differences across groups was very high (in which case the PA technique was nearly as powerful). However, when we increased the model complexity for the present analysis by introducing a mediator, PA emerged as the more powerful technique in at least some scenarios. Thus, we believe the complexity of the model may have an important role to play and should be included as an important design parameter in any future study comparing these two techniques.

Third, we did not include an evaluation of the impact of model misspecification or cross-loadings because we felt they were issues that should ideally be resolved at the level of theory rather than on a purely empirical basis. Nevertheless, misspecification has been studied in the past as a design parameter in covariance-based SEM (e.g., Jarvis et al. 2003; MacKenzie et al. 2005) and remains an area for future study in the context of detection of between-group differences.

Finally, as we noted at the outset, we chose to focus our analysis on two of the more commonly used techniques for testing between-group differences for naturally occurring groups. Our analysis should also be extended to include some of the newer methods for testing between-group differences in PLS.

The first of these methods builds on McDonald's (1996) work on principal component analysis using unweighted least squares (ULS) in the covariance-based SEM framework.

Tenenhaus et al. (2009) presents a method (SEM-ULS) of replicating the PLS approach using software meant for covariance-based SEM. The advantage of this method is very much the same as that for other covariance-based SEM (i.e., it is supported by widely used software, parameters can be constrained, it provides global estimation of the whole set of parameters, non-recursive models can be used, etc.). Tenanhaus et al. extended this method to include estimation of group effects.

Chin (2003) proposed a random permutation procedure for multigroup analysis in PLS and demonstrated its application through a field study (Chin and Dibbern 2009). This is a distribution free method for analyzing between-group differences. All possible permutations for reassignment of cases between the two groups are performed and the originally observed difference is tested against this distribution. This method is new and not implemented in any PLS software. This “is probably way beyond what is expected in current applied research” $^{6}$ and hence only one empirical study has employed this method (Chin and Dibbern 2009). In a recent review of moderating effects in PLS models, Henseler and Fassott (2009) recognize this method to be appropriate because it is distribution free; nevertheless they recommend the product indicator and its variant (i.e., a two stage PLS method $^{7}$ ) in their framework due to the nonavailability of the permutation method in component-based SEM software.

Henseler (2007) presents a new bootstrapping approach to multigroup analysis in PLS. The estimation method remains similar to the parametric approach; however, instead of using a t-test, individual path coefficients are obtained from the bootstrap process (e.g., 500 resamples) for each group. This gives us 500 path coefficients each for Group A and for Group B. Each path coefficient for Group A is then compared with each path coefficient for Group B. The number of times path A exceeds path B is counted. The relative frequency of these counts to the total number of comparison reflects the probability of path A being significantly greater than path B (Henseler and Fassott 2009). We applied this method to a small subsample of our study and found that our conclusions for parametric PLS and this method are comparable.

Each of these three techniques offers advantages compared to existing methods, as outlined by their proponents. Future research to compare these methods, building on our findings in this study, would be extremely valuable.

In addition, it will be interesting to compare the two product indicator approaches—one covariance-based (CSA-PI) (Kenny and Judd 1984) and other PLS based (PLS-PI) (Chin et al. 2003)—with each other and also with the approaches discussed above. Due to our focus on between-group differences in naturally occurring groups, we excluded them. However, this remains an important possibility for future research.

## Conclusions

This is the first study to explicitly compare component-based and covariance-based approaches to the assessment of between-group differences. Prior studies have compared the product indicator approach in PLS to regression analysis (Chin et al. 2003) and between-group analysis using the random permutation method in PLS to group comparison using covariance-based SEM (Chin and Dibbern 2009). But no prior studies had compared the PLS based between-group method, which is currently dominant in the IS literature, with the multigroup analysis in covariance-based SEM that dominates in other areas using Monte Carlo studies with known parameters. The comparison of these two techniques is thus important as it helps to put the results obtained in IS research in perspective. Our results demonstrate that there are significant differences between the methods, and that the choice of method is, therefore, material in the conduct of data analysis; thus we provide an important first step in understanding the conditions under which each technique can be most productively used.

## Acknowledgments

We would like to thank the senior editor, Carol Saunders, the associate editor, and the reviewers for their insights. We would also like to thank Babita Bhatt for her help with simulations at a very early stage of this project, and Chris Higgins, who provided helpful comments on the earlier versions of this paper.

## References

Ahuja, M. K., and Thatcher, J. B. 2005. “Moving Beyond Intentions and Toward the Theory of Trying: Effects of Work Environment and Gender on Post-Adoption Information Technology Use,” MIS Quarterly (29:3), pp. 427-459.

Arbuckle, J. L. 2005. AMOS User's Guide, (Version 6.0), Chicago: Small Waters Corporation.

Barclay, D., Thompson, R., and Higgins, C. 1995. “The Partial Least Squares (PLS) Approach to Causal Modeling: Personal Computer Adoption and Use as an Illustration,” Technology Studies (2:2), pp. 285-309.

Bentler, P., Liang, J., and Yuan, K. 2005. “Some Recent Advances in Two-Level Structural Equation Models: Estimation, Testing and Robustness,” in Contemporary Multivariate Analysis and Design of Experiments, J. Fan, and G. Li (eds.), Singapore: World Scientific Publishing Company, Inc., pp. 99-120.

Bollen, K. A. 1989. Structural Equations with Latent Variables, New York: John Wiley and Sons.

Byrne, B. M. 1994. “Testing for the Factorial Validity, Replication, and Invariance of a Measurement Instrument: A Paradigmatic Application Based on the Maslach Burnout Inventory,” Multivariate Behavioral Research (29), pp. 289-311.

Byrne, B. M. 2001. Structural Equation Modeling with AMOS: Basic Concepts, Applications, and Programming, Mahwah, NJ: Lawrence Erlbaum Associates.

Carte, T. A., and Russell, C. J. 2003. “In Pursuit of Moderation: Nine Common Errors and Their Solutions,” MIS Quarterly (27:3), pp. 479-501.

Cassel, C., Hackl, P., and Westlund, A. 1999. “Robustness of Partial Least-Squares Method for Estimating Latent Variable Quality Structures,” Journal of Applied Statistics (26:4), pp. 435-446.

Cheung, G. W., and Rensvold, R. B. 2002. “Evaluating Goodness-of-Fit Indexes for Testing Measurement Invariance,” Structural Equation Modeling (9:2), pp. 233-255.

Chin, W. W. 1998a. “Issues and Opinion on Structural Equation Modeling,” MIS Quarterly (22:1), pp. vii-xvi.

Chin, W. W. 1998b. “The Partial Least Squares Approach for Structural Equation Modeling,” in Modern Methods for Business Research, G. A. Marcoulides (ed.), Mahwah, NJ: Lawrence Erlbaum Associates, pp. 295-336.

Chin, W. W. 2000. “Frequently Asked Questions—Partial Least Squares and PLS-Graph,” updated December 21, 2004; available online at http://disc-nt.cba.uh.edu/chin/plsfaq/plsfaq.htm.

Chin, W. W. 2001. PLS-Graph User's Guide, C. T. Bauer College of Business, University of Houston, Houston, TX; available online at http://www.lemon628.idv.tw/bilab/km/files/plsgraph30manualhubona\_276.pdf.

Chin, W. W. 2003. “A Permutation Procedure for Multigroup Comparison of PLS Models,” in PLS and Related Methods, Proceedings of the PLS'03 International Symposium, M. Valares, M. Tenenhaus, P. Coelho, V. Vinzi, and A. Morineau (eds.), Lisbon, pp. 33-43.

Chin, W. W. 2005. “Bootstrap Cross-Validation Indices for PLS Path Model Assessment,” in Evaluation of PLS Models, Proceedings of the PLS'06 International Symposium, T. Aluja, J. Casanovas, V. E. Vinzi, A. Morineau, and M. Tenenhaus (eds.), Barcelona, pp. 43-55.

Chin, W. W., Marcolin, B. L., and Newsted, P. R. 2003. “A Partial Least Squares Latent Variable Modeling Approach for Measuring

Interaction Effects: Results from a Monte Carlo Simulation Study and an Electronic-Mail Emotion/Adoption Study," Information Systems Research (14:2), pp. 189-217.

Cohen, J. 1988. Statistical Power Analysis for the Behavioral Sciences ( $2^{nd}$ ed.), Hillsdale, NJ: Erlbaum, Hillsdale.

Diamanthopoulos, A., and Winklhofer, H. M. 2001. “Index Construction with Formative Indicators: An Alternative to Scale Development,” Journal of Marketing Research (38:2), pp. 269-277.

Chin, W. W., and Dibbern, J. 2009. “A Permutation Based Procedure for Multi-Group PLS Analysis: Results of Tests of Differences on Simulated Data and a Cross of Information System Services between Germany and the USA,” in V. E. Vinzi, W. W. Chin, J. Henseler, and H. Wang (eds), Handbook of Partial Least Squares: Concepts, Methods and Applications in Marketing and Related Fields, Berlin: Springer.

Dijkstra, T. 1983. “Some Comments on Maximum Likelihood and Partial Least Squares Methods,” Journal of Econometrics (22:1/2), pp. 67-90.

Enns, H. G., Huff, S. L., and Higgins, C. A. 2003. “CIO Lateral Influence Behaviors: Gaining Peers’ Commitment to Strategic Information Systems,” MIS Quarterly (27:1), pp. 155-176.

Epitropaki, O., and Martin, R. 2005. “From Ideal to Real: A Longitudinal Study of the Role of Implicit Leadership Theories on Leader-Member Exchanges and Employee Outcomes,” Journal of Applied Psychology (90:4), pp. 659-676.

Finch, H. 2006. “Comparison of the Performance of Varimax and Promax Rotations: Factor Structure Recovery for Dichotomous Items,” Journal of Educational Measurement (43:1), pp. 39-52.

Fornell, C., and Bookstein, F. L. 1982. “Two Structural Equation Models: LISREL and PLS Applied to Consumer Exit-Voice Theory,” Journal of Marketing Research (19:4), pp. 440-452.

Goodhue, D., Lewis, W., and Thompson, R. 2006. “PLS, Small Sample Size and Statistical Power in MIS Research,” in Proceedings of the 39 $^{th}$ Hawaii International Conference on System Sciences, Los Alamitos, CA: IEEE Computer Society Press.

Goodhue, D., Lewis, W., and Thompson, R. 2007. “Statistical Power in Analyzing Interaction Effects: Questioning the Advantage of PLS with Product Indicators,” Information Systems Research (18:2), pp. 211-227.

Henseler, J. 2007. “A New and Simple Approach to Multi-Group Analysis in Partial Least Squares Path Modeling,” in PLS'07: The 5 $^{th}$ International Symposium on PLS and Related Methods, Ås, Norway, September 5-7, pp. 104-107.

Henseler, J., and Fassott, G. 2009. “Testing Moderating Effects in PLS Path Models: An Illustration of Available Procedures,” in: Handbook of PLS and Marketing (in Press), E. V. Vinzi, W. W. Chin, J. Henseler and H. Wang (eds.), Berlin: Springer, forthcoming.

Hoogland, J. J., and Boomsma, A. 1998. “Robustness Studies in Covariance Structure Modeling: An Overview and Meta-Analysis,” Sociological Methods and Research (26), pp. 329-367.

Hsieh, J. J. P. -A., Rai, A., and Keil, M. “Understanding Digital Inequality: Comparing Continued Use Behavioral Models of the Socio-Economically Advantaged and Disadvantaged,” MIS Quarterly (32:1), pp. 97-126.

Jarvis, C. B., MacKenzie, S. B., and Podsakoff, P. M. 2003. “A Critical Review of Construct Indicators and Measurement Model Misspecification in Marketing and Consumer Research,” Journal of Consumer Research (30:2), pp. 199-218.

Jöreskog, K. G. 1971. “Simultaneous Factor Analysis in Several Populations,” Psychometrika (36), pp. 409-426.

Jöreskog, K. G., and Wold, H. 1982. “The ML and PLS Techniques for Modeling with Latent Variables: Historical and Comparative Aspects,” in Systems Under Indirect Observation: Causality, Structure, Prediction, K. G. Jöreskog and H. Wold (eds.), Amsterdam: North Holland, pp. 263-270.

Karahanna, E., Straub, D. W., and Chervany, N. L. 1999. “Information Technology Adoption across Time: A Cross-Sectional Comparison of Pre-Adoption and Post-Adoption Beliefs,” MIS Quarterly (23:2), pp. 183-213.

Keil, M., Tan, B. C. Y., Wei, K. K., Saarinen, T., Tuunainen, V., and Wassenaar, A. 2000. “A Cross-Cultural Study on Escalation of Commitment Behavior in Software Projects,” MIS Quarterly (24:2), pp. 299-325.

Kenny, D. A., and Judd, C. M. 1984. “Estimating the Nonlinear and Interactive Effects of Latent Variables,” Psychological Bulletin (96:1), pp. 201-210.

Little, T. D. 1997. “Mean and Covariance Structures (MACS), Analyses of Cross-Cultural Data: Practical and Theoretical Issues,” Multivariate Behavioral Research (32), pp. 53-76.

MacKenzie, S., Podsakoff, P., and Jarvis, C. 2005. “The Problem of Measurement Model Misspecification in Behavioral and Organizational Research and Some Recommended Solutions,” Journal of Applied Psychology (90:4), pp. 710-730.

Marcoulides, G., Emrich, C., and Marcoulides, L. 2008. “Testing for Multigroup Invariance of the Computer Anxiety Scale,” Educational and Psychological Measurement (68:2), pp. 325-334.

Marcoulides, G. A., and Saunders, C. 2006. “Editor’s Comments: PLS: A Silver Bullet?,” MIS Quarterly (30:2), pp. iii-ix.

Marsh, H., and Hocevar, D. 1985. “Application of Confirmatory Factor Analysis to the Study of Self-Concept: First- and Higher-Order Factor Models and Their Invariance Across Groups,” Psychological Bulletin (97:3), pp. 562-582.

Mayer, R. C., and Gavin, M. B. 2005. “Trust in Management and Performance: Who Minds the Shop While the Employees Watch the Boss?,” Academy of Management Journal (48:5), pp. 874-888.

McCoy, S., Everard, A., and Jones, B. M. 2005. “An Examination of the Technology Acceptance Model in Uruguay and the US: A Focus on Culture,” Journal of Global Information Technology Management (8:2), pp. 27-45.

McDonald, R. 1996. “Path Analysis with Composite Variables,” Multivariate Behavioral Research (31:2), pp. 239-270.

Muthén, B., and Asparouhov, T. 2002. “Using Mplus Monte Carlo Simulations in Practice: A Note on Non-Normal Missing Data in Latent Variable Models,” Version 2 (available at http://www.statmodel.com/download/webnotes/mc2.pdf).

Muthén, L. K., and Muthén, B. O. 2002. “How to Use a Monte Carlo Study to Decide on Sample Size and Determine Power,” Structural Equation Modeling (9:4), pp. 599-620.

Muthén, L. K., and Muthén, B. O. 2006. Mplus User's Guide: Statistical Analysis with Latent Variables ( $4^{th}$ ed.), Los Angeles: Muthén & Muthén.

Paxton, P., Curran, P. J., Bollen, K. A., Kirby, J. B., and Chen, F. 2001. “Monte Carlo Experiments: Design and Implementation,” Structural Equation Modeling (8:2), pp. 287-312.

Petter, S., Straub, D., and Rai, A. 2007. “Specifying Formative Constructs in Information Systems Research,” MIS Quarterly (31:4), pp. 623-656.

Powell, D. A., and Schafer, W. D. 2001. “The Robustness of the Likelihood Ratio Chi-Square Test for Structural Equation Models: A Meta-Analysis,” Journal of Educational and Behavioral Statistics (26:1), pp. 105-132.

Raykov, T., and Marcoulides, G. A. 2006. A First Course in Structural Equation Modeling ( $2^{nd}$ ed.), Mahwah, NJ: Lawrence Erlbaum Associates.

Reise, S. P., Widaman, K. F., and Pugh, R. H. 1993. “Confirmatory Factor Analysis and Item Response Theory: Two Approaches for Exploring Measurement Invariance,” Psychological Bulletin (114), pp. 552-566.

Rigdon, E. E., Schumacker, R. E., and Wothke, W. 1998. “A Comparative Review of Interaction and Nonlinear Modeling,” in Interaction and Nonlinear Effects in Structural Equation Modeling, R. E. Schumacker and G. A. Marcoulides (eds.), Mahwah, NJ: Lawrence Erlbaum Associates, pp. 1-16.

Riordan, C. M., and Vandenberg, R. J. 1994. “A Central Question in Cross-Cultural Research: Do Employees of Different Cultures Interpret Work-Related Measures in an Equivalent Manner?,” Journal of Management (20), pp. 643-671.

Rothbard, N. P. 2001. “Enriching or Depleting? The Dynamics of Engagement in Work and Family Roles,” Administrative Science Quarterly (46:4), pp. 655-684.

Schumacker, R. E., and Lomax, R. G. 2004. A Beginner's Guide to Structural Equation Modeling, Mahwah, NJ: Lawrence Erlbaum Associates.

Song, M., Droge, C., Hanvanich, S., and Calantone, R. 2005. "Marketing and Technology Resource Complementarity: An Analysis of Their Interaction Effect in Two Environmental Contexts," Strategic Management Journal (26:3), pp. 259-276.

Steenkamp, J., and Baumgartner, H. 1998. “Assessing Measurement Invariance in Cross-National Consumer Research,” Journal of Consumer Research (25:1), pp. 78-90.

Tenenhaus, M., Mauger, E., and Guinot, C. 2009. “Use of ULS-SEM and PLS-SEM to Measure a Group Effect in a Regression Model Relating Two Blocks of Binary Variables,” in Handbook of PLS and Marketing (in Press), E. V. Vinzi, W. W. Chin, J. Henseler and H. Wang (eds.), Berlin: Springer, forthcoming.

Vandenberg, R., and Lance, C. 2000. “A Review and Synthesis of the Measurement Invariance Literature: Suggestions, Practices, and Recommendations for Organizational Research,” Organizational Research Methods (3:1), pp. 4-70.

Venkatesh, V., and Morris, M. G. 2000. “Why Don’t Men Ever Stop to Ask for Directions? Gender, Social Influence, and Their Role in Technology Acceptance and Usage Behavior,” MIS Quarterly (24:1), pp. 115-139.

Zhu, K., Kraemer, K. L., Gurbaxani, V., and Xu, S. X. 2006. "Migration to Open-Standard Interorganizational Systems: Network Effects, Switching Costs, and Path Dependency," MIS Quarterly (30:Special Issue), pp. 515-539.

## About the Authors

Israr Qureshi is an assistant professor at the Hong Kong Polytechnic University, Hong Kong. He has worked for 9 years in IT project implementation and management. Israr earned his Ph.D. at the University of Western Ontario in 2008. His research approach is informed by social networks theory and analysis, and his thesis investigated influence of computer-mediated communication on social capital. Additional areas of interest are social informatics, knowledge sharing, and electronic commerce.

Deborah Compeau is an associate professor of Management Information Systems in the Ivey Business School at the University of Western Ontario. Her research focuses on the individual user of information and communications technologies, viewed from a social cognitive perspective. In particular, she is interested in understanding what organizations can do to facilitate individual adoption of and learning about information technologies. Her research has been published in a variety of IS journals.

## Appendix A

## Complete ANOVA Results

<table><tr><td>Source</td><td>Sig.</td><td>Partial Eta Squared</td></tr><tr><td>Model</td><td>.000</td><td>.726</td></tr><tr><td>Estimation technique (0 = PA, 1 = CSA)</td><td>.000</td><td>.002</td></tr><tr><td>Loadings</td><td>.000</td><td>.009</td></tr><tr><td>Normal (0 = normal, 1 = non-normal )</td><td>.000</td><td>.060</td></tr><tr><td>Sample size</td><td>.000</td><td>.126</td></tr><tr><td>Correlation amongst exogenous variables</td><td>.423</td><td>.000</td></tr><tr><td>Difference in paths (Diff)</td><td>.000</td><td>.333</td></tr><tr><td></td><td></td><td></td></tr><tr><td>Loadings × Normal</td><td>.000</td><td>.006</td></tr><tr><td>Loadings × Sample</td><td>.000</td><td>.002</td></tr><tr><td>Loadings × Corr</td><td>.000</td><td>.002</td></tr><tr><td>Loadings × diff</td><td>.000</td><td>.004</td></tr><tr><td>Loadings × E</td><td>.000</td><td>.002</td></tr><tr><td>Normal × Sample</td><td>.000</td><td>.030</td></tr><tr><td>Normal × Corr</td><td>.733</td><td>.000</td></tr><tr><td>Normal × diff</td><td>.000</td><td>.065</td></tr><tr><td>Normal × E</td><td>.011</td><td>.000</td></tr><tr><td>Sample × Corr</td><td>.000</td><td>.002</td></tr><tr><td>Sample × diff</td><td>.000</td><td>.072</td></tr><tr><td>Sample × E</td><td>.000</td><td>.000</td></tr><tr><td>Corr × diff</td><td>.000</td><td>.002</td></tr><tr><td>Corr × E</td><td>.000</td><td>.002</td></tr><tr><td>diff × E</td><td>.000</td><td>.006</td></tr><tr><td></td><td></td><td></td></tr><tr><td>Loadings × Normal × Sample</td><td>.000</td><td>.002</td></tr><tr><td>Loadings × Normal × Corr</td><td>.000</td><td>.002</td></tr><tr><td>Loadings × Normal × diff</td><td>.000</td><td>.003</td></tr><tr><td>Loadings × Normal × E</td><td>.000</td><td>.002</td></tr><tr><td>Loadings × Sample × Corr</td><td>.000</td><td>.002</td></tr><tr><td>Loadings × Sample × diff</td><td>.000</td><td>.006</td></tr><tr><td>Loadings × Sample × E</td><td>.000</td><td>.002</td></tr><tr><td>Loadings × Corr × diff</td><td>.000</td><td>.001</td></tr><tr><td>Loadings × Corr × E</td><td>.000</td><td>.001</td></tr><tr><td>Loadings × diff × E</td><td>.000</td><td>.001</td></tr><tr><td>Normal × Sample × Corr</td><td>.000</td><td>.002</td></tr><tr><td>Normal × Sample × diff</td><td>.000</td><td>.033</td></tr><tr><td>Normal × Sample × E</td><td>.000</td><td>.000</td></tr><tr><td>Normal × Corr × diff</td><td>.000</td><td>.002</td></tr><tr><td>Normal × Corr × E</td><td>.000</td><td>.002</td></tr><tr><td>Normal × diff × E</td><td>.000</td><td>.005</td></tr></table>

<table><tr><td>Source</td><td>Sig.</td><td>Partial Eta Squared</td></tr><tr><td>Sample × Corr × diff</td><td>.000</td><td>.004</td></tr><tr><td>Sample × Corr × E</td><td>.000</td><td>.002</td></tr><tr><td>Sample × diff × E</td><td>.000</td><td>.005</td></tr><tr><td>Corr × diff × E</td><td>.000</td><td>.001</td></tr><tr><td></td><td></td><td></td></tr><tr><td>Loadings × Normal × Sample × Corr</td><td>.000</td><td>.002</td></tr><tr><td>Loadings × Normal × Sample × diff</td><td>.000</td><td>.004</td></tr><tr><td>Loadings × Normal × Sample × E</td><td>.000</td><td>.002</td></tr><tr><td>Loadings × Normal × Corr × diff</td><td>.000</td><td>.001</td></tr><tr><td>Loadings × Normal × Corr × E</td><td>.000</td><td>.001</td></tr><tr><td>Loadings × Normal × diff × E</td><td>.000</td><td>.001</td></tr><tr><td>Loadings × Sample × Corr × diff</td><td>.000</td><td>.001</td></tr><tr><td>Loadings × Sample × Corr × E</td><td>.000</td><td>.002</td></tr><tr><td>Loadings × Sample × diff × E</td><td>.000</td><td>.001</td></tr><tr><td>Loadings × Corr × diff × E</td><td>.000</td><td>.001</td></tr><tr><td>Normal × Sample × Corr × diff</td><td>.000</td><td>.004</td></tr><tr><td>Normal × Sample × Corr × E</td><td>.000</td><td>.001</td></tr><tr><td>Normal × Sample × diff × E</td><td>.000</td><td>.016</td></tr><tr><td>Normal × Corr × diff × E</td><td>.000</td><td>.001</td></tr><tr><td>Sample × Corr × diff × E</td><td>.000</td><td>.001</td></tr><tr><td></td><td></td><td></td></tr><tr><td>Loadings × Normal × Sample × Corr × diff</td><td>.000</td><td>.001</td></tr><tr><td>Loadings × Normal × Sample × Corr × E</td><td>.000</td><td>.002</td></tr><tr><td>Loadings × Normal × Sample × diff × E</td><td>.000</td><td>.001</td></tr><tr><td>Loadings × Normal × Corr × diff × E</td><td>.000</td><td>.001</td></tr><tr><td>Loadings × Sample × Corr × diff × E</td><td>.000</td><td>.001</td></tr><tr><td>Normal × Sample × Corr × diff × E</td><td>.000</td><td>.001</td></tr><tr><td>Loadings × Normal × Sample × Corr × diff</td><td>.000</td><td>.001</td></tr></table>

## Appendix B

Results of Between-Group Path Comparison (for Individual Paths)  
For Path A–C (0.05)

<table><tr><td rowspan="3" colspan="3"></td><td colspan="4">Normal</td><td colspan="4">Non-normal</td></tr><tr><td colspan="2">100</td><td colspan="2">500</td><td colspan="2">100</td><td colspan="2">500</td></tr><tr><td>PA</td><td>CSA</td><td>PA</td><td>CSA</td><td>PA</td><td>CSA</td><td>PA</td><td>CSA</td></tr><tr><td rowspan="10"> $r_{AB}=0$ </td><td rowspan="5">3</td><td>.05</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>.15</td><td>0</td><td>0</td><td>47</td><td>86</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>.25</td><td>1</td><td>1</td><td>100</td><td>100</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>.35</td><td>28</td><td>73</td><td>100</td><td>100</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>.45</td><td>73</td><td>100</td><td>100</td><td>100</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td rowspan="5">6</td><td>.05</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>.15</td><td>0</td><td>0</td><td>80</td><td>100</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>.25</td><td>2</td><td>3</td><td>100</td><td>100</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>.35</td><td>47</td><td>92</td><td>100</td><td>100</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>.45</td><td>83</td><td>100</td><td>100</td><td>100</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td rowspan="10"> $r_{AB}=0.4$ </td><td rowspan="5">3</td><td>.05</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>.15</td><td>0</td><td>0</td><td>27</td><td>13</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>.25</td><td>1</td><td>0</td><td>100</td><td>100</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>.35</td><td>19</td><td>35</td><td>100</td><td>100</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>.45</td><td>66</td><td>95</td><td>100</td><td>100</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td rowspan="5">6</td><td>.05</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>.15</td><td>57</td><td>0</td><td>50</td><td>61</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>.25</td><td>99</td><td>0</td><td>100</td><td>100</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>.35</td><td>100</td><td>67</td><td>100</td><td>100</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>.45</td><td>100</td><td>99</td><td>100</td><td>100</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

Numbers in cells indicate the percentage of path comparisons that were significant at p = 0.05 out of total 500 comparisons per cell. Bold numbers indicate that they are significantly different from numbers in corresponding cells of other between-group comparison technique at 0.05.

For Path B–C (0.20)

<table><tr><td rowspan="3" colspan="3"></td><td colspan="4">Normal</td><td colspan="4">Non-normal</td></tr><tr><td colspan="2">100</td><td colspan="2">500</td><td colspan="2">100</td><td colspan="2">500</td></tr><tr><td>PA</td><td>CSA</td><td>PA</td><td>CSA</td><td>PA</td><td>CSA</td><td>PA</td><td>CSA</td></tr><tr><td rowspan="10"> $r_{AB}=0$ </td><td rowspan="5">3</td><td>.05</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>.15</td><td>0</td><td>0</td><td>40</td><td>82</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>.25</td><td>1</td><td>0</td><td>100</td><td>100</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>.35</td><td>15</td><td>70</td><td>100</td><td>100</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>.45</td><td>50</td><td>100</td><td>100</td><td>100</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td rowspan="5">6</td><td>.05</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>.15</td><td>0</td><td>0</td><td>77</td><td>99</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>.25</td><td>1</td><td>2</td><td>100</td><td>100</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>.35</td><td>23</td><td>92</td><td>100</td><td>100</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>.45</td><td>54</td><td>100</td><td>100</td><td>100</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td rowspan="10"> $r_{AB}=0.4$ </td><td rowspan="5">3</td><td>.05</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>.15</td><td>0</td><td>0</td><td>15</td><td>14</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>.25</td><td>0</td><td>0</td><td>100</td><td>100</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>.35</td><td>5</td><td>35</td><td>100</td><td>100</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>.45</td><td>31</td><td>92</td><td>100</td><td>100</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td rowspan="5">6</td><td>.05</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>.15</td><td>31</td><td>0</td><td>25</td><td>59</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>.25</td><td>87</td><td>0</td><td>100</td><td>100</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>.35</td><td>93</td><td>61</td><td>100</td><td>100</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>.45</td><td>95</td><td>99</td><td>100</td><td>100</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

Numbers in cells indicate the percentage of path comparisons that were significant at p = 0.05 out of total 500 comparisons per cell. Bold numbers indicate that they are significantly different from numbers in corresponding cells of other between-group comparison technique at 0.05.

Numbers in cells indicate the percentage of path comparisons that were significant at p=0.05 out of total 500 comparisons per cell. Bold numbers indicate that they are significantly different from numbers in corresponding cells of other between-group comparison technique at 0.05.

For Path A–D (0.35)

<table><tr><td rowspan="3" colspan="3"></td><td colspan="4">Normal</td><td colspan="4">Non-normal</td></tr><tr><td colspan="2">100</td><td colspan="2">500</td><td colspan="2">100</td><td colspan="2">500</td></tr><tr><td>PA</td><td>CSA</td><td>PA</td><td>CSA</td><td>PA</td><td>CSA</td><td>PA</td><td>CSA</td></tr><tr><td rowspan="10"> $r_{AB}=0$ </td><td rowspan="5">3</td><td>.05</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>.15</td><td>0</td><td>0</td><td>64</td><td>53</td><td>1</td><td>0</td><td>100</td><td>65</td></tr><tr><td>.25</td><td>2</td><td>2</td><td>100</td><td>100</td><td>62</td><td>1</td><td>100</td><td>100</td></tr><tr><td>.35</td><td>40</td><td>50</td><td>100</td><td>100</td><td>99</td><td>67</td><td>100</td><td>100</td></tr><tr><td>.45</td><td>84</td><td>93</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td></tr><tr><td rowspan="5">6</td><td>.05</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>.15</td><td>0</td><td>0</td><td>93</td><td>93</td><td>1</td><td>0</td><td>100</td><td>98</td></tr><tr><td>.25</td><td>5</td><td>3</td><td>100</td><td>100</td><td>81</td><td>3</td><td>100</td><td>100</td></tr><tr><td>.35</td><td>60</td><td>77</td><td>100</td><td>100</td><td>100</td><td>93</td><td>100</td><td>100</td></tr><tr><td>.45</td><td>93</td><td>98</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td></tr><tr><td rowspan="10"> $r_{AB}=0.4$ </td><td rowspan="5">3</td><td>.05</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>.15</td><td>0</td><td>0</td><td>31</td><td>41</td><td>1</td><td>0</td><td>100</td><td>66</td></tr><tr><td>.25</td><td>1</td><td>2</td><td>100</td><td>100</td><td>59</td><td>1</td><td>100</td><td>100</td></tr><tr><td>.35</td><td>21</td><td>37</td><td>100</td><td>100</td><td>99</td><td>66</td><td>100</td><td>100</td></tr><tr><td>.45</td><td>60</td><td>79</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td></tr><tr><td rowspan="5">6</td><td>.05</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>.15</td><td>58</td><td>0</td><td>71</td><td>82</td><td>0</td><td>0</td><td>100</td><td>98</td></tr><tr><td>.25</td><td>98</td><td>5</td><td>100</td><td>100</td><td>79</td><td>3</td><td>100</td><td>100</td></tr><tr><td>.35</td><td>100</td><td>63</td><td>100</td><td>100</td><td>100</td><td>92</td><td>100</td><td>100</td></tr><tr><td>.45</td><td>100</td><td>94</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td></tr></table>

For Path C–D (0.6)

<table><tr><td rowspan="3" colspan="3"></td><td colspan="4">Normal</td><td colspan="4">Non-normal</td></tr><tr><td colspan="2">100</td><td colspan="2">500</td><td colspan="2">100</td><td colspan="2">500</td></tr><tr><td>PA</td><td>CSA</td><td>PA</td><td>CSA</td><td>PA</td><td>CSA</td><td>PA</td><td>CSA</td></tr><tr><td rowspan="10"> $r_{AB}=0$ </td><td rowspan="5">3</td><td>.05</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>5</td><td>0</td><td>100</td></tr><tr><td>.15</td><td>0</td><td>0</td><td>10</td><td>82</td><td>0</td><td>100</td><td>100</td><td>100</td></tr><tr><td>.25</td><td>2</td><td>5</td><td>100</td><td>100</td><td>54</td><td>100</td><td>100</td><td>100</td></tr><tr><td>.35</td><td>41</td><td>79</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td></tr><tr><td>.45</td><td>88</td><td>99</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td></tr><tr><td rowspan="5">6</td><td>.05</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>9</td><td>0</td><td>100</td></tr><tr><td>.15</td><td>0</td><td>0</td><td>66</td><td>98</td><td>0</td><td>100</td><td>100</td><td>100</td></tr><tr><td>.25</td><td>9</td><td>13</td><td>100</td><td>100</td><td>58</td><td>100</td><td>100</td><td>100</td></tr><tr><td>.35</td><td>74</td><td>91</td><td>100</td><td>100</td><td>99</td><td>100</td><td>100</td><td>100</td></tr><tr><td>.45</td><td>98</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td></tr><tr><td rowspan="10"> $r_{AB}=0.4$ </td><td rowspan="5">3</td><td>.05</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>5</td><td>0</td><td>100</td></tr><tr><td>.15</td><td>0</td><td>0</td><td>2</td><td>80</td><td>0</td><td>100</td><td>100</td><td>100</td></tr><tr><td>.25</td><td>1</td><td>3</td><td>100</td><td>100</td><td>61</td><td>100</td><td>100</td><td>100</td></tr><tr><td>.35</td><td>19</td><td>77</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td></tr><tr><td>.45</td><td>65</td><td>99</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td></tr><tr><td rowspan="5">6</td><td>.05</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>9</td><td>0</td><td>100</td></tr><tr><td>.15</td><td>54</td><td>0</td><td>39</td><td>98</td><td>0</td><td>100</td><td>100</td><td>100</td></tr><tr><td>.25</td><td>99</td><td>10</td><td>100</td><td>100</td><td>65</td><td>100</td><td>100</td><td>100</td></tr><tr><td>.35</td><td>100</td><td>90</td><td>100</td><td>100</td><td>99</td><td>100</td><td>100</td><td>100</td></tr><tr><td>.45</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td></tr><tr><td colspan="11">Numbers in cells indicate the percentage of path comparisons that were significant at p = 0.05 out of total 500 comparisons per cell.Bold numbers indicate that they are significantly different from numbers in corresponding cells of other between-group comparison technique at 0.05.</td></tr></table>
