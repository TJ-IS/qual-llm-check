---
otero_id: 7572
otero_key: "D5EX47CE"
title: "Applying configurational analysis to IS behavioural research: a methodological alternative for modelling combinatorial complexities"
authors: "Yong Liu; József Mezei; Vassilis Kostakos; Hongxiu Li"
year: "2017"
journal: "Information Systems Journal"
doi: "10.1111/isj.12094"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Applying configurational analysis to IS behavioural research: a methodological alternative for modelling combinatorial complexities

Yong Liu,\* József Mezei,<sup>†,¶</sup> Vassilis Kostakos<sup>‡</sup> & Hongxiu Li<sup>§</sup>

\*Department of Information and Service Economy, Aalto University School of Business, Helsinki, Finland, email: yong.liu@aalto.<sup>fi</sup>, <sup>†</sup>Department of Information Technologies, Åbo Akademi University, Turku, Finland, <sup>‡</sup>Department of Computer Science and Engineering, University of Oulu, Oulu, Finland, <sup>§</sup>Information Systems Science, Department of Management and Entrepreneurship, Turku School of Economics, University of Turku, Turku, Finland, and <sup>¶</sup>RiskLab Finland, Arcada University of Applied Sciences, Helsinki, Finland

Abstract. An important limitation of regression-based analysis stems from the as sumption of symmetric relationships between variables, which is often violated. To overcome this limitation within IS research, we propose the use of the fuzzy-set qualitative comparative analysis (FsQCA) method. The paper elaborates on the rationale for applying this approach to IS behavioural research and how to tailor FsQCA for this purpose. A systematic interpretation of the technique covering its mathematical properties and advanced features is provided. Drawing from an illustrative study of mobile government services adoption by residents of rural areas, the paper demonstrates FsQCA’s potential to supplement regression-based IS behavioural research, by (i) examining asymmetric relationships between a set of antecedents and the IS phenomenon of interest, (ii) providing nuanced coverage of necessary and suf<sup>fi</sup>cient conditions for emergence of an IS behavioural outcome, and (iii) identifying various con<sup>fi</sup>gurations of conditions in association with users demographic characteristics.

Keywords: fuzzy-set qualitative comparative analysis, FsQCA, con<sup>fi</sup>gurationa analysis, multiple regression analysis, structural equation modelling, causa asymmetry

## INTRODUCTION

Scienti<sup>fi</sup>c tools are not neutral: tools-in-use shapes how we think and theorize (Gigerenzer, 1991). Without exception, this applies also to the dominance of regression-based analysis in IS behavioural research, in which researchers frequently utilize multiple measurement indicators in questionnaire-based surveys to collect empirical data on users’ perceptions of di verse IS attributes when explaining various IS use phenomena, such as (continuous) intention to use and actual usage. Regression analysis – in particular, the structural equation modelling technique – has become a key tool used by scholars to model and interpret such phenomena. In this paper, we highlight one important bias of such tools: their assumption that relationships between variables are symmetric. In fact, these relationships are often asymmetric; therefore, a suitable alternative to regression analysis is needed and one such approach would be the use of con<sup>fi</sup>gurational analysis.

Con<sup>fi</sup>guration theory argues that combinations of varying initial conditions can lead to the same outcome. Accordingly, the relationship between an outcome and its preconditions is often asymmet ric rather than symmetric (Ragin, 2000; Fiss, 2007; Park & El Sawy, 2012; Woodside, 2013). For in stance, different user groups may decide to adopt a technology by considering different sets of its attributes (Rogers, 1983; Venkatesh et al., 2003). Certain users may decide not to use a technology until a certain condition is satis<sup>fi</sup>ed, even though the given condition alone cannot result in their intention to use. Such asymmetric relationships and combinatorial complexities cannot be modelled by conventional regression-based methods (RBMs). However, applying a con<sup>fi</sup>gurational approach can offer insights into problems of these types, particularly with regard to IS user behaviour.

To this end, we propose using a set-theoretical con<sup>fi</sup>gurational analysis technique, fuzzy-se qualitative comparative analysis (FsQCA), as a methodological alternative to supplement mainstream RBMs in IS user behavioural research. Developed by Ragin (1987, 2000), FsQCA has be come one of the most popular con<sup>fi</sup>gurational analysis techniques. It has recently gained popularity amongst scientists across a broad spectrum of social science disciplines, though not the IS com munity. The possibilities of this technique offer IS scholars a new data analysis tool, new perspectives for theorizing, and an enhanced understanding of IS user behaviour (c.f. El Sawy et al., 2010).

In this study, we (i) elaborate on con<sup>fi</sup>guration theory and the rationale for embracing con<sup>fi</sup>g urational analysis in IS behavioural research, (ii) systematically establish FsQCA as an effective instrument to detect con<sup>fi</sup>gurations of an IS behaviour outcome, and (iii) demonstrate how to apply the technique to IS behavioural research by means of an illustrative study examining adoption of mobile government services.

## CONFIGURATION THEORY AND APPROACH

To date, IS behavioural research has been grounded mostly in the use of RBMs, including multi ple regression analysis (MRA) and structural equation modelling (SEM). These methods are aimed at understanding the problem from the perspective of variance theories, in which a predictor variable is posited to be both a necessary and a suf<sup>fi</sup>cient condition for the outcome (El Sawy et al., 2010). Therefore, a symmetric relationship is assumed between the variables in RBMs (Morris, 2005; Woodside, 2013); i.e. a change in the ‘cause’ variable results in a change in the ‘effect’ variable, and a low (or high) value of the effect variable corresponds to a low (or high) value of the cause variable. Consequently, asymmetric relationships are beyond the scope of RBMs. While RBMs can model the interaction effect of two predictors on an outcome variable, the relationship between the interaction variable and the outcome variable is assumed to be symmetric.

Con<sup>fi</sup>guration theory, however, allows the modelling of asymmetric relationships between variables (Matzler et al., 2004; Fiss, 2007; El Sawy et al., 2010; Woodside, 2013) because it views phenomena as clusters of interconnected elements that must be simultaneously understood as a holistic integrated pattern (El Sawy et al., 2010). This has two implications. Firstly, a predictor can have an asymmetric relationship with the outcome variable, while a predictor may be insuf-<sup>fi</sup>cient for the outcome to occur, it can serve as a necessary condition for the outcome variable (Fiss, 2007; Woodside, 2013). Speci<sup>fi</sup>cally, a necessary condition represents a condition that is present – to some degree, in the fuzzy set theory sense – in every case that results in the speci<sup>fi</sup>c outcome, while suf<sup>fi</sup>ciency indicates a condition whose presence guarantees the speci<sup>fi</sup>c outcome. Secondly, a variable may affect the outcome only given the presence or absence of one or more additional variables (Fiss, 2007; El Sawy et al., 2010). In other words, multiple variables can act together to bring about the outcome of interest and different ‘recipes’ may exist for combining variables, known as con<sup>fi</sup>gurations. Con<sup>fi</sup>guration theory strongly resonates with the theories of equi<sup>fi</sup>nality in management literature (Fiss, 2011), which posit that ‘a system can reach the same <sup>fi</sup>nal state from different initial conditions and by a variety of different paths (Katz & Kahn, 1978, p. 30).

For our purposes, a ‘con<sup>fi</sup>guration’ is de<sup>fi</sup>ned as a speci<sup>fi</sup>c set of causal variables that, when working together, bring about an outcome of interest (Rihoux & Ragin, 2009; Ragin, 2000). To identify con<sup>fi</sup>gurations in phenomena reliably, qualitative comparative analysis (QCA) is applied to estimate the causal contribution of various possible con<sup>fi</sup>gurations to the expected outcome Among the main variants of QCA are crisp-set QCA, multi-value QCA, and EsQCA (Schneidel & Wagemann, 2010). We focus on FsQCA, one of the most general versions of QCA without posing a signi<sup>fi</sup>cant increase in the computational cost of performing the analysis. Additionally, although with many problems the limited modelling capabilities of multi-value QCA would seem a suf<sup>fi</sup>cient extension to crisp-set QCA, there are some serious pitfalls to be considered with respect to its interpretability and the way it is affected by limited diversity in the dataset as compared to FsQCA (Vink & Van Vliet, 2009).

Since circa 1995, QCA has gradually come to be used by scientists from quite varied research backgrounds (c.f. Skarmeas et al., 2014): political parties (Gordin, 2001), policy analysis (Blake & Adolino, 2001), social movements (Nomiya, 2001), social and political change (Berg-Schlosser & De Meur, 1994), addictive behaviour (Eng & Woodside, 2012), linguistics (Mendel & Korjani, 2012), and welfare states (Peillon, 1996). In the last two years, rapid expan sion of QCA’s use and its widespread use in the social sciences have occurred on account of recent advances in FsQCA, particularly within business and management research in examina tion of phenomena such as organizational innovation (Ganter & Hecker, 2014), successful product innovation (Cheng et al., 2013), inter-organizational technology transfer (Leischnig et al., 2014), and tourism behaviour (Woodside et al., 2011).

## Relevance to IS

Con<sup>fi</sup>guration theory was originally developed in the context of organizational research (c.f. Fiss, 2007; Woodside, 2013). Hence, some researchers have sought to introduce con<sup>fi</sup>gurational analysis to IS research with a focus on organizational performance (Fichman, 2004; El Sawy et al., 2010; Park & El Sawy, 2012; Wendler et al., 2013; Chong et al., 2013).

The work of Fichman (2004) was probably the <sup>fi</sup>rst to introduce the concept of QCA to the IS community. This research focused on organizational IT innovations. Chong et al. (2013) and Wendler et al. (2013) are more recent examples of those applying QCA application in IS research. Efforts by other researchers can be seen in the work of El Sawy et al. (2010) and of Park & El Sawy (2012). In a research commentary, El Sawy et al. (2010) proposed that con<sup>fi</sup>g uration theory offers a different paradigmatic lens for better understanding the complexity of dig ital ecodynamics. More recently, Park & El Sawy (2012) have applied FsQCA to identify different con<sup>fi</sup>gurations that result in a similar level of competitive <sup>fi</sup>rm performance, in which multifaceted roles of IT capability are reported.

Despite valuable insights, con<sup>fi</sup>gurational analysis is still ‘a method which is nearly unrecog nized within our discipline to date’ (Wendler et al., 2013, p. 1457). The uptake of this method in the IS community may be impeded by IS scholars’ unfamiliarity with the approach and by its rapid evolution. In this regard, the paper represents an attempt to increase awareness and dem onstrate application of the FsQCA approach in hopes of generating greater insights in the IS community.

Secondly, the study provides theoretical support for incorporating con<sup>fi</sup>gurational analysis into IS behavioural research through comparison of the features of FsQCA with those of conventional RBMs. Discussion of the use of con<sup>fi</sup>gurational analysis has thus far focused predom inantly on (IS) organizational research. Theories and methods developed for the organizational research may not <sup>fi</sup>t the context of user behavioural research, and vice versa. For instance, is it rational to model asymmetric relationships in IS behavioural research, given the predominant assumption of symmetric relationships between variables in our research tradition? Hence, another contribution of our work is to apply the method to IS behavioural research. We elaborate on our rationale next.

## Asymmetric effects of determinants on IS behaviour

IS behavioural research has focused mostly on detecting the causality of IS use phenomena, with RBMs being the main approach utilized; thereby, causal symmetry has been assumed. However, causal asymmetry is also found within IS behavioural research.

Under assumptions of causal symmetry, the results of correlation or regression analysis are determined by the association pattern of two variables. Consider Figure 1, for instance, which presents a scatterplot of two variables: perceived usefulness (USE) and the behavioural intention to adopt mobile government services. A <sup>fi</sup>ve-point Likert scale from ‘Disagree’ (1) to ‘Agree’ (5) is utilized for the data collection. The correlation between the two variables is positive (r = 0.365) and signi<sup>fi</sup>cant $( p < 0 . 0 0 1 )$ , implying that when users perceive the technology to be more useful they are more likely to adopt it. For RBMs, the highlighted data points in the top left and bottom right appear to be ‘noise’ in the hypothesized symmetric and positive relationship, and they contribute to the unexplained part of behavioural intention. However, these samples contain important information and are evidence of asymmetry. For instance, as is indicated in Figure 1, many users who do not perceive a technology to be useful may still intend to adopt it, while some users who perceive the technology as useful are unwilling to do so. Consequently, systematic explanation of the mechanism underlying these asymmetric relationships may offer important insights.

![](/api/attachments/D5EX47CE/fulltext/images/6589e6222a1db3b4387c8763b2d99e9c4fe978aff661210bc8068aa7d4a07f9c.jpg)  
Figure 1. A scatterplot of two IS perceptual variables.

## Merits of using QCA in IS behavioural research: comparison to RBMs

RBMs enjoy a long history of popularity in the social sciences, although several constraints have been reported (Woodside, 2013; Woodside & Zhang, 2013; Skarmeas et al., 2014). Hence, we should state that the aim of this section is not to suggest that prior RBM studies were inappropriately constructed. Instead, we seek to highlight the advantages of FsQCA as an instrument for supplementing RBM-based IS research.

Firstly, MRA and SEM adopt a ‘net effect’ estimation approach: they estimate the effect size of each independent variable with reference to the dependent variable after controllino for the impact of other independent variables in a model. In consequence, the estimated net effect of the independent variables may <sup>fl</sup>uctuate between being signi<sup>fi</sup>cant and insigni<sup>fi</sup>cant, depending on the presence or absence of additional independent variables (Woodside, 2013). Armstrong (2012) noted that adding variables to an equation does no mean controlling for variables in non-experimental settings, because predictors typically co-vary with each other. This phenomenon actually lends support to con<sup>fi</sup>gurational analy sis: it is the presence or absence of other particular factors that gives meaning to a vari able (c.f. Fiss, 2007).

Secondly, RBMs examine the extent to which symmetric relationships exist between a set of independent variables and a dependent variable (Woodside, 2013). In other words, low or high values of a variable, X, are associated respectively, with low or high values of a variable, Y, and vice versa (Figure 2(B)). A symmetric relationship between X and Y indicates that X is both a necessary and a suf<sup>fi</sup>cient condition for Y. In contrast, in an asymmetric relationship X may be either a suf<sup>fi</sup>cient or a necessary condition for Y.

We demonstrate asymmetric relationships in the following way. A typical case of an asymmetric relationship may involve a high value of X being associated with a high value of Y, while a high value of Y may not be associated with a high value of X. In this case, we claim that X is a suf<sup>fi</sup>cient condition for Y, as shown in Figure 2(C). On the other hand, it is possible for a high value of X not always to be associated with a high value of Y, while a high value of Y is always associated with a high value of X. In this case, we claim that X is a necessary condition for Y, as shown in Figure 2(D). In addi tion, an insigni<sup>fi</sup>cant symmetric relationship between two variables (as in Figure 2(A)) does not necessarily rule out the existence of asymmetric relationships – across part of the sample.

![](/api/attachments/D5EX47CE/fulltext/images/fec05c246e14bf02bbe3da3fa9546b031ebae077b1056d7012eef4afb2e0c73f.jpg)

![](/api/attachments/D5EX47CE/fulltext/images/c8ea8526c3120a17f28bdbf5672da3d62afbd76903a1d9c81d276b2fb654fe80.jpg)

![](/api/attachments/D5EX47CE/fulltext/images/f14b2ba511b24af021391ef269df05f58938cfa3957fca5b85ffa0bcb78a2ff2.jpg)

![](/api/attachments/D5EX47CE/fulltext/images/0e3ff804c1a23ef149d856164b70c595d10f9473111b7afa4881f61401d0dc1a.jpg)  
Figure 2. Visualization of symmetric (B), asymmetric (C and D), and random (A) dependencies between variable (adapted from Wu et al, (2014))

Next, classic regression models treat variables as competing in explaining variance in outcomes rather than as showing how they cooperate or combine to create outcomes (Fiss, 2007), while con<sup>fi</sup>guration theory assumes that there is always more than one combination of conditions that gives rise to a given outcome. Similarly, this applies to the re search on antecedents of IS behaviour: while there might be many signi<sup>fi</sup>cant antecedents of a particular IS outcome, these factors may not necessarily all co-exist to produce an effect, and also a single factor may not lead to the relevant outcome in the absence of other factors.

For instance, some individuals may adopt an IS mainly on account of peer in<sup>fl</sup>uence, while others have an expectation of enhanced performance. In fact, evidence of these effects can be obtained from existing theories, such as the uni<sup>fi</sup>ed theory of acceptance and use of technology (Venkatesh et al., 2003) and innovation diffusion theory (Rogers, 1983), which show that users’ demographic characteristics signi<sup>fi</sup>cantly alter the way they value the attributes of an IS. As IS behaviour tends to be motivated by different variables for different user groups, it is reasonable to assume that different con<sup>fi</sup>gurations exist that generate a particular IS behaviour outcome.

Fourthly, users may not perceive all attributes of a given IS positively. A user who evaluates several attributes of the IS negatively may still adopt it on account of positive evaluation of other attributes. For instance, a considerable proportion of users may evaluate an iPhone as expensive (a negative perception) but still adopt it because they feel that using iPhones is ‘cool’ (a positive perception surrounding social image). Therefore, a positive perception as to social image is a necessary condition for iPhone adoption for those who perceive the price of an iPhone negatively. The negative perception of price, in combination with the positive perception of social image, forms a suf<sup>fi</sup>cient set of conditions (con<sup>fi</sup>guration) for iPhone adoption. However, this conditional combinatorial con<sup>fi</sup>guration cannot be detected by RBMs.

Finally, FsQCA can be more robust as compared to RBMs for two reasons. Firstly, while the results of RBMs can be sensitive to outliers, this is less likely to be an issue for FsQCA because its analysis relies on identifying subsets of the data (details are presented in Section 3). As every observation is translated into a combination of conditions, the inclusion or exclusion of a particular data point simply alters the evaluation of that combination and has no effect on the overall assessment of other causal combinations. Secondly, sample representativeness is less of an issue for FsQCA, because it does not hinge on the assumption that data are drawn from a given probability distribution (Fiss, 2011). This is because FsQCA, when evaluating a con<sup>fi</sup>guration, considers only the subset of samples affected by the con<sup>fi</sup>guration in the whole dataset. If a particular group of users have been over-represented or under-represented, there is little effect on the existence of other con<sup>fi</sup>gurations.

© 2015 Blackwell Publishing Ltd, Information Systems Journal

## Limitations of con<sup>fi</sup>gurational analysis

It is important to point out that FsQCA does have some limitations. Firstly, RBMs are less de manding with respect to prior causal knowledge and have a clear empiricist foundation (Vis, 2012), whereas FsQCA relies on prior knowledge for the choice of the conditions and the outcome, and to simplify con<sup>fi</sup>gurations. Secondly, the interpretation of the results gained by FsQCA is labour-intensive, carrying a high risk of subjective bias. This is especially true when one is interpreting complex solutions. Thirdly, FsQCA requires the calibration of data (Section 3), which is not necessary in RBMs. As Ragin (2008a) points out, this can be a disadvantage but also an advantage: if the researchers are knowledgeable enough about the underlying domain, the freedom to transform traditional variables into fuzzy values can signi<sup>fi</sup>cantly improve the analysis. Fourthly, there is also a lack of proper theoretical grounding when one is determining the precise threshold for various measurements in the application of FsQCA to assess causal con<sup>fi</sup>gurations (Mendel & Korjani, 2012). A threshold value that is too low or high can result in too many or too few retrieved con<sup>fi</sup>gurations respectively. Fifthly, FsQCA is sensitive to case selection, especially with a small sample size, and it cannot detect the solutions if the relevant sample cases are not included. This is a problem in studies with few cases, but when the data are collected from a random sample in suf<sup>fi</sup>cient numbers (where the threshold depends on the number of causal conditions to be considered), it is not a relevant issue. Sixthly, FsQCA lacks of proper procedures for assessing measurement error. Furthermore, FsQCA assesses the empirical relevance and set-theoretical importance of complex combinatorial pathways to the outcome but cannot identify the unique contribution of each individual condition (Skarmeas et al., 2014).

Another limitation of FsQCA is that it was originally developed to measure one-item factors. Therefore, latent variables cannot be directly utilized. Hence, we propose integrating the advantages of a measurement model test using SEM with an asymmetric relationship test using FsQCA (Park & El Sawy, 2012); i.e. after examination of the validity and reliability of latent variables through measurement model tests, the values of the latent variables should be transformed into fuzzy set values for further analysis with FsQCA.

## FSQCA: CONCEPTS AND ANALYSIS

FsQCA was developed by the social scientist Charles Ragin (1987, 2000), who integrated fuzzy set and fuzzy logic principles with QCA; in FsQCA every variable is considered a (fuzzy) set. In the original form of QCA, Boolean sets are used as the basis for the analysis. For example, when we talk about the risk associated with an outcome, a case (which might be an organization or a respondent) is either risky or not risky and is associated with the value 1 or 0 respec: tively. In most situations, this binary classi<sup>fi</sup>cation is not suf<sup>fi</sup>cient to capture the real nature of an observation. In the ideal case, we would like to capture a degree of belonging: if a speci<sup>fi</sup>c case can be classi<sup>fi</sup>ed as very risky, it belongs to the set of risky cases with a degree of 0.9, while a degree of 0.2 indicates low risk. The use of fuzzy set theory corresponds to the original intention of Zadeh (1965), who proposed fuzzy sets and fuzzy logic with broader applications for the social sciences, not solely for engineering and control theory (Seising, 2010).

Vis (2012) points out that a factor that de<sup>fi</sup>nitely in<sup>fl</sup>uences the outcome in only a small subset of cases becomes invisible in a regression-based analysis. FsQCA can identify the patterns that differ across subsets of cases easily and with less stringent data requirements than statistical advances. Compared to conventional RBMs such as MRA or SEM, FsQCA, as a con<sup>fi</sup>gurational analysis approach, offers unique values and new capabilities for socia scientists wishing to ‘describe combinatorial complexities assuming asymmetrical relationships between variables, rather than symmetrical net effects that MRA and SEM usually es timate’ (Skarmeas et al., 2014, p. 1796).

In a recent paper, Mendel & Korjani (2012) summarized the FsQCA method in 13 steps, to make it more approachable from a quantitative point of view. In the following discussion, we describe the most important steps in the analysis by focusing on the issues that highlight the dif ferences between FsQCA and traditional statistical techniques. As is mentioned previously, the main goal with FsQCA is to identify combinations of conditions that result in a speci<sup>fi</sup>c outcome. Two of the most important methodological differences result from this formulation: (a) in FsQCA, several combinations of (necessary and/or suf<sup>fi</sup>cient) conditions (that is, possible multiple solu tions) can be identi<sup>fi</sup>ed, and (b) the effect of a given independent variable on the outcome is not quanti<sup>fi</sup>ed, because we are interested in the combinatorial effects (Woodside, 2013).

## Data calibration

The initial step in the analysis is to convert the variables of the model into sets; this process is called data calibration in FsQCA terminology (Ragin, 2000). According to Ragin (2008a), there are two main types of data calibration: direct (identifying three qualitative breakpoints of the fuzzy sets) and indirect (rescaling the original measurements in line with qualitative assessments). Both approaches rely extensively on the substantive knowledge of the researchers in the calibration process. For this paper, we use direct calibration, and we discuss only this pro cedure in detail in the succeeding texts.

In some cases, it is suf<sup>fi</sup>cient to use crisp (0–1) sets to represent a variable: for example, the variable gender, when translated into a set, automatically becomes crisp as it can take only two values. For more complex variables, the original recommendation (and the calibration method used in the original software, and consequently in most of the applications) is to identify three values from the range of the variable that are to correspond to full-membership, the most ambig uous membership, and full non-membership. If the researcher does not have suf<sup>fi</sup>cient knowledge of the underlying variable, the most straightforward procedure is to use the three values 1, 0.5, and 0. The other values of the original variable are calibrated on the basis of a linear function to <sup>fi</sup>t into these three values. For example, if a variable is measured on a <sup>fi</sup>ve-item scale, the membership values for 1, 3, and 5 are 0, 0.5, and 1 respectively, and the memberships for 2 and 4 are assigned in keeping with the assumption of a linear membership function, in line with the researcher's substantive and theoretical knowledge. Substantive knowledge can refer to any knowledge that pertains to relevant information related to the problem domain, the measurement model, or the observed cases (sample). In other words, we use qualitative anchoring to establish a connection between a fuzzy membership function and the original data. In our analysis, for the binary variable gender we use membership values of 0 and 1. For other variables, measured on a <sup>fi</sup>ve-item Likert scale, the two extreme items are translated to the membership values 0 and 1, and the intermediate items are assigned membership values in a sub-linear way, given values of 0.2, 0.4, and 0.7, instead of the equidistant choices 0.25, 0.5, and 0.75.<sup>1</sup> This means that a higher score on the Likert-scale is required from the respondent for intermediate memberships and re<sup>fl</sup>ects the general knowledge that the points on the Likert scale are not equidistant (Busch, 1993). In other words, using this substantive knowledge, instead of applying an equidistant division of the unit interval to calibrate a <sup>fi</sup>ve-item scale (i.e. item i is assigned the membership value $( i - 1 ) ^ { \star } 0 . 2 5 )$ , we can specify a (slightly) lower membership value for lower values of i. This indicates a higher standard for intermediate memberships. Transforming the middle point (neutral value) of a <sup>fi</sup>ve-item scale into 0.5, the latter being the threshold for a con<sup>fi</sup>guration’s selection in the frequency analysis would mean that a neutral opinion positively contributes to the evaluation of a con<sup>fi</sup>guration. To avoid this, we choose to use 0.4 and an intermediate membership value. In general, an understanding of the problem domain can offer information for calibration of an ordinal scale by means of a piecewise linear function (with different slopes on the subdomains).

In our analysis we made use of the FsQCA software developed by Ragin & Davey (2014), which uses the calibration values produced by a linear transformation function, but, in general, the choice of the three membership values and linearity is not necessary, because one can utilize the full [0,1] interval and use non-linear membership functions (Mendel & Korjani, 2012). The use of membership functions different from linear membership functions requires extensive knowledge of the underlying cases. This is a more feasible alternative when FsQCA is applied in reliance on a limited number of extensively analysed cases, for example individual organizations. If there is only a limited amount of information about the respondents in a questionnaire-based dataset, unless detailed knowledge is obtained about the utility functions of the respondents, it is unreasonable to translate an ordinal scale into a membership function that differs from a (piecewise) linear membership function.

## Identifying the most important variable con<sup>fi</sup>gurations

Once each variable is converted into a condition set, all possible variable combinations are evaluated, which means that with k condition sets there are $2 ^ { k }$ possible combinations to be assessed. For example, in a simple case with two condition sets, here the USE and ease of use (EOU) of an IS, there are four logical combinations: ‘USE and EOU’, ‘not USE and EOU’, 'USE and not EOU',and 'not USE and not EOU'

Given a particular combination, we can then calculate the degree to which each case in our dataset supports it. This is done by calculating the minimum of the membership values of the conditions present in the combination, with the complementary value (i.e. 1 value) taken into account when necessary. Continuing our previous example, let us assume that one respondent reported 0.7 for EOU and 0.4 for USE. From these <sup>fi</sup>gures, we calculate the degree for the four possible combinations. For instance, the combination USE and EOU is supported by this respondent degree: min $( 0 . 7 , 0 . 4 ) = 0 . 4$ . On the other hand, the combination not USE and EOU is supported to the degree: min $( 1 - 0 . 4 , 0 . 7 ) = 0 . 6$ . In crisp QCA, a combination is either fully supported or not supported at all by an observation. In FsQCA, the value 0.5 serves as the threshold value in the assessment of which combinations are supported to an acceptable degree.

The process we describe requires $2 ^ { k \star }$ (the number of cases) evaluations. However, Mendel & Korjani (2013) recently proved that for a given case there can be only one causal combination with an overall degree higher than 0.5, thereby greatly simplifying the calculations required. In comparison to the original exponential complexity of the FsQCA algorithm, this reduction represents a distinct advantage over other methods with respect to computationa complexity.

In the next step we discard all combinations that are not supported by at least one case with a degree above 0.5. The remaining combinations are evaluated on the basis of two measures, in the following order:

• Frequency: The combinations that do not represent at least a prede<sup>fi</sup>ned threshold number of cases are excluded from further analysis. For example if this prede<sup>fi</sup>ned threshold is 10, a combination needs to have a membership value greater than 0.5 for at least 10 cases.

• Consistency: Every remaining combination at this point can be considered a potential fuzzy rule that provides a setting of conditions that may or may not result in the de<sup>fi</sup>ned outcome. For checking whether these potential rules are indeed real, a fuzzy subsethood measure is de<sup>fi</sup>ned, which is termed consistency. This measure captures the extent to which a given combination is a suf<sup>fi</sup>cient condition for the outcome. In other words, high consistency indicates that when the causal combination occurs, that case will lead to the outcome under consideration. The original recommendation by Ragin (2008a) is to exclude combinations with a consistency value lower than a threshold of 0.8, but this can be increased or decreased as the problem context dictates. In general, as we deal with several cases (respondents), the consistency for a particular combination is calculated as

$$
\text { Consistency } = \frac {\sum_ {i} \min (\text { support   of   combination   for   respondent } i ; \text { membership   of   outcome   for   respondent } i)}{\sum_ {i} \text { support   of   combination   for   respondent } i}
$$

Continuing our example, we need to check which of the supported combinations is consistent with the outcome ‘Intention’. In our example we consider one respondent, and the only supported combination is not USE and EOU with support 0.6; therefore, the consistency of the rule ‘not USE and EOU leads to Intention’ has to be calculated. We assume that the respondent be ing considered belongs to the fuzzy set Intention with a membership value of 0.4. To calculate the consistency of this combination with the outcome Intention, we calculate min (support of combination, membership of outcome)/(support of combination) or min $( 0 . 6 , \ 0 . 4 ) / 0 . 6 = 0 . 6 7$

Therefore, this respondent is not suf<sup>fi</sup>ciently consistent (above 0.8) with the rule not USE and EOU leads to Intention’.

## Obtaining the solution sets

After identi<sup>fi</sup>cation of all suf<sup>fi</sup>cient combinations, three solution sets can be obtained: complex, parsimonious, and intermediate solutions (Ragin, 2008a). Here, ‘solution’ refers to a combination of conditions that is supported by a high number of cases, where the rule ‘the combination leads to the outcome’ is consistent.

The set of complex solutions is obtained by taking the logical union of suf<sup>fi</sup>cient combinations identi<sup>fi</sup>ed in the previous step and simplifying these by applying traditional logical operations, i.e. union, intersection, and negation. This can be done in an algorithmic fashion via the Quine–McCluskey (QM) minimization method (Mendelson, 1970). To show an example, we suppose now that, additionally to USE and EOU, the variable G (gender) is included in the anal ysis, with $" G "$ representing females and negation, ‘not G’ representing males. We suppose that two con<sup>fi</sup>gurations with high frequency and consistency were identi<sup>fi</sup>ed: ‘USE and not EOU and G’ and ‘USE and not EOU and not G’. As the two con<sup>fi</sup>gurations suggest, the presence of USE and lack of EOU results in intention to use for both genders; intuitively this could be simply expressed with the con<sup>fi</sup>guration USE and not EOU. As this statement holds for both genders, including two con<sup>fi</sup>gurations simply conveys redundant information. Formally, taking the union of the two con<sup>fi</sup>gurations (corresponding to the or operator) and using the property of associa tivity, we can derive that

USE and not EOU and G or USE and not EOU and not G

$$
U S E \text {   and   not   } E O U \text {   and   } (G \text {   or   not   } G) = U S E \text {   and   not   } E O U
$$

In this simple example we obtained the complex solution USE and not EOU by simplifying the con<sup>fi</sup>gurations obtained in the previous step in the FSQCA process. In general, because the number of con<sup>fi</sup>gurations identi<sup>fi</sup>ed can be very large, the number of complex solutions can be large and these may include con<sup>fi</sup>gurations with several terms. This makes the interpretation of the solutions dif<sup>fi</sup>cult and in most cases impractical (Mendel & Korjani, 2012). For this reason, they are usually simpli<sup>fi</sup>ed further into parsimonious and intermediate solutions.

For obtaining the set of parsimonious solutions, the QM method makes use of the combinations that were dropped in the frequency test. The parsimonious solutions can be seen as the causal combinations featuring the minimal number of conditions. To obtain the parsimonious solutions we make use of the information on the causal combinations that do not pass the fre quency threshold in order to simplify the complex solutions through Boolean logic operations. Every complex solution includes at least one parsimonious solution. As the process for deriving parsimonious solutions makes very strong assumptions by utilizing information from all the combinations without considering suf<sup>fi</sup>ciency of frequency, they are usually not presented as the <sup>fi</sup>nal solutions of the FsQCA analysis. However, they are necessary for calculating the intermediate solutions. To continue the example, we identify the complex solution USE and not EOU, and we conclude that the combination USE and EOU does not pass the frequency threshold test. By using logical operations thus

$$
(\text { USE   and   not   EOU }) \text { or } (\text { USE   and   EOU }) = \text { USE   and } (\text { EOU   or   not   EOU }) = \text { USE },
$$

we obtain the parsimonious solution ‘USE’. While it provides a very simple explanation for un derstanding the underlying problem, the calculations make use of information that is not suf<sup>fi</sup> ciently supported by the data. For this reason, researchers, in general, have to be very careful when interpreting and presenting parsimonious solutions.

The intermediate solutions are obtained from the parsimonious and complex solutions through counterfactual analysis (Ragin, 2008a; Fiss, 2011), which builds on the domain knowl edge of the researcher. Consequently, the set of intermediate solutions can vary with the person performing the analysis. The important condition in de<sup>fi</sup>ning counterfactuals so as to simplify complex solutions into intermediate is that the researcher should rely on general, uncontroversial substantive knowledge. In general, the causal combinations contained in the set of intermediate solutions are included in the complex solutions but also contain the parsimonious solutions. For example, by using no substantive knowledge at all, the intermediate solutions are the same as the complex solutions. The traditional way of utilizing substantive knowledge is to specify whether the presence or absence of a condition (according to general knowledge) can be associated with the outcome variable. In counterfactual analysis, we consider every pair of complex and parsimonious solutions. If the parsimonious solution is contained in the complex solution and the substantive knowledge does not contradict the parsimonious solution, we simplify the complex solution by applying the knowledge. In our simple example, we have only one pair, USE and USE and not EOU. If the knowledge to be used states that, in general, ‘not USE is associated with the presence of the outcome variable (Intention), we do not perform counterfactual analysis as it contradicts the parsimonious solution. If the substantive knowledge shows that ‘EOU’ is, in general, associated with the outcome, because it does not contradict the parsimonious solution, we can remove its negation, ‘not EOU’ from the complex solution and thereby obtain the intermediate solution USE. In simple cases involving few variables and basic additional substantive knowledge, the intermediate solutions are identical to either parsimonious or complex solutions. However, in problems entailing several variables, intermediate solutions, on one hand, can simplify complex solutions into interpretable combinations while, on the other hand, overcoming the limitation of strong (and sometimes unjusti<sup>fi</sup>ed) assumptions used for deriving parsimonious solutions. A more detailed and mathematical oriented description of the steps in counterfactual analysis is provided by Mendel & Korjani (2012).

## Interpreting and evaluating the solutions

After obtaining these three sets of solutions, we can classify causal conditions further, into core and peripheral conditions (Fiss 2011) Core conditions are those conditions that are part ot both parsimonious and intermediate solutions, while peripheral conditions are those that exist only in the intermediate solution but are eliminated in the parsimonious solution. This approach de<sup>fi</sup>nes the causal coreness in terms of the strength of the evidence relative to the outcome, in stead of the connectedness to other con<sup>fi</sup>gurational elements (Fiss, 2011). In other words, as intermediate solutions are derived on the basis of substantive knowledge of the connection between conditions and the outcome variable, differentiating between core and peripheral condi tions depends mainly on this knowledge rather than the relationship with other con<sup>fi</sup>gurations. Speci<sup>fi</sup>cally, for a core condition, the validity of both conditions (e.g. the presence of condition A and its counter-condition and the absence of condition A) is supported by the data. For a peripheral condition, only the condition itself in the con<sup>fi</sup>guration is supported by the data, while it is unclear whether the counter-condition is valid, because there is a lack of relevant data. Furthermore, a peripheral condition is not necessarily unimportant; a peripheral condition can often serve as a necessary condition in the con<sup>fi</sup>guration.

In this paper, we use both complex solutions and intermediate solutions to identify core and peripheral conditions, as recommended by, for example, Ragin & Sonnett (2005) and Ragin (2008a). The main reason behind this methodological choice is that both intermediate and parsimonious solutions require the researcher to make assumptions as to the presence or ab sence of various conditions. When one is obtaining parsimonious solutions, the analysis relies partly on the set of causal combinations that are not present with suf<sup>fi</sup>cient frequency in the dataset while the intermediate solutions are calculated through reliance on assumptions (the assumed knowledge of the researcher) surrounding the effect of individual conditions on the outcome. The assumptions could be made on the basis of prior studies; e.g. the presence of perceived USE should be associated with a high membership value for intention to use (based, for instance, on the technology acceptance model). However, we hypothesize that users with particular negative perceptions will also be able to adopt the technology. Using complex solutions enables presentation of all possible con<sup>fi</sup>gurations.

Finally, in the last step in the analysis, the solutions can be evaluated by means of various coverage measures. The general term ‘coverage’ refers to the proportion of the sum of the membership values of supporting cases for a combination. Coverage is akin to effect size in statistical hypothesis testing (Woodside & Zhang, 2013). Coverage can be calculated in terms of a solution set (a set of con<sup>fi</sup>gurations) or individual solutions. Depending on the group of evaluated con<sup>fi</sup>gurations, a choice of solution, raw or unique coverage can be made, according to Mendel & Korjani (2012).

To illustrate the three coverage measures, we will use the example presented in Table 1. It includes four cases, three possible conditions (USE, EOU, and IMAGE), and the outcome variable Intention. The <sup>fi</sup>rst four columns contain the membership values for the conditions and the outcome. We <sup>fi</sup>nd that there are two con<sup>fi</sup>gurations identi<sup>fi</sup>ed as solutions, Conf1 = USE and

Table 1. Example illustrating the various coverage measures

<table><tr><td>Case</td><td>USE</td><td>EOU</td><td>IMAGE</td><td>Intention</td><td>C1</td><td>C2</td><td>Overall support</td><td>C1 and Intention</td><td>C2 and Intention</td><td>Overall</td></tr><tr><td>1</td><td>0.7</td><td>0.8</td><td>0.6</td><td>0.9</td><td>0.7</td><td>0.6</td><td>0.7</td><td>0.7</td><td>0.6</td><td>0.7</td></tr><tr><td>2</td><td>0.5</td><td>0.6</td><td>0.3</td><td>0.7</td><td>0.5</td><td>0.3</td><td>0.5</td><td>0.5</td><td>0.3</td><td>0.5</td></tr><tr><td>3</td><td>0.7</td><td>0.3</td><td>0.8</td><td>0.9</td><td>0.3</td><td>0.7</td><td>0.7</td><td>0.3</td><td>0.7</td><td>0.7</td></tr><tr><td>4</td><td>0.3</td><td>0.7</td><td>0.8</td><td>0.2</td><td>0.3</td><td>0.3</td><td>0.3</td><td>0.2</td><td>0.2</td><td>0.2</td></tr><tr><td>Sum</td><td>2.2</td><td>2.4</td><td>2.5</td><td>2.7</td><td>1.8</td><td>1.9</td><td>2.2</td><td>1.7</td><td>1.8</td><td>2.1</td></tr></table>

EOU and Conf2 = ‘USE and IMAGE’. The ‘C1’ and ‘C2’ columns present the support for the con<sup>fi</sup>gurations, which is simply the minimum of the two values for the variables in a con<sup>fi</sup>guration, for example, C1 = min (USE and EOU). The column labelled ‘Overall support’ shows the support for the solution set (Conf1, Conf2), as the maximum of the values in the preceding two columns. The columns ‘C1 and Intention’ and ‘C2 and Intention’ show how consistent the con<sup>fi</sup>gurations are with the outcome; for example C1 and Intention = min (C1, Intention). Finally, ‘Overall’ presents the overall consistency of the solution set (Conf1 and Conf2) as the maximum of the values in the preceding two columns.

The <sup>fi</sup>rst coverage measure, solution coverage, is calculated for a solution set (not for an individual solution) and describes the sum of the values obtained from the join of the causal con<sup>fi</sup>gurations and the outcome variable normalized by the sum of the membership values for the outcome variable (Mendel & Korjani, 2012). In other words, it measures to what extent the cases that indicate the presence of the outcome are covered by at least one of the con<sup>fi</sup>gurations from the solution set. In our example, this can be calculated as the quotient of the sum of the columns Overall (the join of the two con<sup>fi</sup>gurations and Intention) and Intention, which is 2.1/2.7 = 0.78.

The raw coverage of a speci<sup>fi</sup>c solution is the join of the con<sup>fi</sup>guration and outcome normalized by the sum of the membership values for the outcome variable (Ragin, 2000; Ganter & Hecker, 2014). Raw coverage provides a measure estimating the extent (in a fuzzy sense) to which a solution covers the dataset: that is. in what percentage of the cases the configuration can be observed. In our case, the raw coverage of Conf1 is calculated as (using the values from the last row of Table 1)

the sum for C1 and Intention=the sum for Intention 1:7=2:7 0:63

For Conf2, it can be calculated similarly as 1.8/2.7 = 0.67.

Unique coverage represents the contribution of a solution beyond what has already been interpreted via other solutions in a solution set (Ragin, 2000; Ganter & Hecker, 2014). In other words, it offers an estimate as to the cases that can be described by a speci<sup>fi</sup>c con<sup>fi</sup>guration and not by any other con<sup>fi</sup>gurations in the solution set. In our example, for a speci<sup>fi</sup>c con<sup>fi</sup>guration it is the difference between the coverage of the whole solution set (precisely the solution coverage) and the raw coverage of the other con<sup>fi</sup>guration. For Conf1, it is

solution coverage – raw coverage of Conf2 0:78–0:67 0:11;

while for Conf2, it is 0.78–0.63 = 0.15

## Summary of FsQCA

As a point of reference, Table 2, in the succeeding texts, includes the de<sup>fi</sup>nitions of importan terms used in the foregoing description. For further review of the discussion in the preceding texts on applying FsQCA, we can summarize the process in terms of four main steps:

1 The calibration process: The variables of the model are converted into fuzzy sets through determination of an appropriate membership value. On the basis of this calibration, the values from the dataset containing the respondents’ answers are transformed into fuzzy membership values.

Table 2. De<sup>fi</sup>nition of the most important concepts in FsQCA

<table><tr><td>Concept</td><td>Definition</td></tr><tr><td>Configuration</td><td>A logical combination of causal conditions</td></tr><tr><td>Frequency</td><td>The number of cases for which a configuration achieves a membership value higher than 0.5 (Ragin, 2008b)</td></tr><tr><td>Consistency</td><td>The extent to which a given combination is a sufficient condition for the outcome (Ragin, 2008b)</td></tr><tr><td>Complex solutions</td><td>Solutions obtained by simplifying, through logical operations the configurations with sufficient frequency and consistency (Mendel &amp; Korjani, 2012)</td></tr><tr><td>Parsimonious solutions</td><td>Solutions obtained by simplifying the complex solutions through use of information from the combinations dropped in the frequency test (Mendel &amp; Korjani, 2012)</td></tr><tr><td>Intermediate solutions</td><td>Solutions obtained from the complex solutions via utilization of substantive knowledge in the form of the presence or absence of some causal conditions (Mendel &amp; Korjani, 2012)</td></tr><tr><td>Core conditions</td><td>Causal conditions that appear in both the parsimonious and intermediate solutions (Fiss, 2011)</td></tr><tr><td>Peripheral conditions</td><td>Causal conditions that appear in the intermediate solutions, but not in the parsimonious solutions (Fiss, 2011)</td></tr><tr><td>Solution coverage</td><td>The proportion of cases (in terms of fuzzy membership value) that can be described by at least one configuration from a solution set (Ragin, 2000)</td></tr><tr><td>Raw coverage</td><td>The proportion of cases (in terms of fuzzy membership value) that can be described by the configuration (Ragin, 2000)</td></tr><tr><td>Unique coverage</td><td>The proportion of cases (in terms of fuzzy membership value) that can be described by a configuration appearing in a solution set but cannot be described by any other configuration from the set (Ragin, 2000)</td></tr></table>

2 Identi<sup>fi</sup>cation of the most important variable con<sup>fi</sup>gurations: Each possible logical combination of the variables is evaluated for every respondent. The combinations that appear enough times and are consistent enough with the data are selected for further analysis.

3 Obtaining the solution sets: The con<sup>fi</sup>gurations identi<sup>fi</sup>ed are simpli<sup>fi</sup>ed and combined through logical operations and counterfactual analysis via the use of additional statements based on the researcher’s substantial knowledge. Three solution sets, complex, intermedi ate, and parsimonious, are identi<sup>fi</sup>ed.

4 Interpretation and evaluation of solutions and solution sets: The solutions identi<sup>fi</sup>ed are broken down further, into core and peripheral conditions. Additionally, various coverage mea sures are used to assess the quality of the solutions and solution sets.

## EXAMPLE: APPLYING FSQCA TO LATENT REFLECTIVE VARIABLES FOR USER PERCEPTIONS

## Variables for analysis and the context of survey-based research

A dataset from a survey-based questionnaire on rural residents’ intention to use mobile government services was utilized in our study. Five variables are proposed as the antecedents of mo bile government services adoption: perceived EOU, perceived (near-term) USE, perceived long-term USE, benevolence, and image. De<sup>fi</sup>nitions for these variables are given in Table 3.

Table 3. De<sup>fi</sup>nition of the latent variables.

<table><tr><td>Variables</td><td>Definition</td><td>Relevant studies</td></tr><tr><td>Perceived ease of use</td><td>Perceived ease of use refers to the degree to which a user believes that using mobile government services would be free of effort.</td><td>Davis (1989)</td></tr><tr><td>Perceived near-term usefulness</td><td>Perceived usefulness is defined as the degree to which an individual perceives that using a particular system would enhance his or her performance of access government information.</td><td>Davis (1989), Thompson et al. (1991), Chang &amp; Cheung (2001), and Liu et al. (2010))</td></tr><tr><td>Perceived long-term usefulness</td><td>Perceived long-term usefulness refers to the degree to which a user believes the use of mobile government services may also bring about outcomes that have a pay-off in the future.</td><td>Thompson et al. (1991), Chang &amp; Cheung (2001), and Liu et al. (2010)</td></tr><tr><td>Benevolence</td><td>Benevolence refers to an individual&#x27;s belief that the trustee cares about her/him and acts in her/his interests.</td><td>Wang &amp; Benbasat (2005)</td></tr><tr><td>Image</td><td>Image refers to citizens&#x27; perceptions that the adoption of mobile government services would enhance the adopters&#x27; status in the social system.</td><td>Phang &amp; Li (2005 and Shareef et al. (2011)</td></tr><tr><td>Behavioural intention</td><td>Behavioural intention refers to a person&#x27;s subjective probability that he/she will perform some behaviour.</td><td>Fishbein &amp; Ajzen (1975)</td></tr></table>

Given that the reason for use of this dataset is to test FsQCA in IS behavioural research, justi <sup>fi</sup>cation of the subject of the survey questionnaire is not included. Hence, we simply provide a summary of prior studies showing the importance of the variables as antecedents of IS adoption in Table 3.

## The questionnaire-based survey

A <sup>fi</sup>ve-point Likert scale from Disagree (1) to Agree (5) was used to measure each perception item. The measurements for the constructs of our research model are derived from prior stud ies. The measurement for perceived EOU and near-term USE are derived from the work of Davis (1989). The items for measuring perceived long-term USE are based on the study by Liu et al. (2010) and Chang & Cheung (2001). The items for measuring image are adapted from the work of Lee & Kozar (2008) and Moore & Benbasat (1991). Finally, the items for benevolence and intention are derived from the measurements used by Wang & Benbasat (2005) and by Venkatesh et al. (2003) respectively. Note that in IS behavioural research, adoption intention is a frequently explored dependent variable, measuring the degree to which individuals are likely to adopt an IS (c.f. Fishbein & Ajzen, 1975). The IS adoption research offers insights into the antecedents driving the information systems adoption, which represents an important stream of IS behavioural research The measurement conducted for latent variables can be found in Appendix A.

Twenty-one student volunteers, whose families live in the rural regions of China’s Zhejiang province, were recruited to help us collect responses from the villages in which their families reside. Before the survey, the volunteers received training and the purpose of the research was clearly explained to all volunteers. The volunteers were requested to visit about 15–25 different rural families and collect a response from one person per family visited. We collected 433 responses, of which 409 were retained for analysis (responses that had missing values for latent variable measurement were removed from consideration).

## Measurement validity and reliability

The construct validity of the measurement included in the questionnaire was assessed. Specif ically, construct validity indicates the degree to which a factor accurately re<sup>fl</sup>ects the construct of interest (Gefen, 2000; Wade & Nevo, 2006). Construct validity is normally assessed via measurement of convergent validity and discriminant validity. The former denotes the degree to which the measurements of the constructs that are assumed to be theoretically related are actually related (Wade & Nevo, 2006). As is shown in Table 4, the values of Cronbach’s alpha (α), composite reliability, and average variance extracted (AVE) for the constructs are all above the thresholds: 0.7, 0.7, and 0.5 respectively (Gefen, 2000). These results show that adequate convergent validity was obtained for the measurement scales.

Discriminant validity re<sup>fl</sup>ects the extent to which two variables that should not be related to one another are actually unrelated (Gefen, 2000; Wade & Nevo, 2006). As Table 5 shows, the square roots of AVE are higher than their correlations with other constructs. In addition, prin cipal component analysis was conducted for further testing of the measurement validity, as shown in Appendix B. The results show that all items <sup>fi</sup>t their respective factors quite well without any substantial cross loading over 0.4, indicating that there is suf<sup>fi</sup>cient discriminant validity (Fornell & Larcker, 1981; Gefen, 2000).

Table 4. Reliability and convergent validity statistics

<table><tr><td>Construct (no. of items)</td><td>α</td><td>Composite reliability</td><td>Minimal factor loading</td><td>AVE</td></tr><tr><td>Near-term usefulness (4)</td><td>0.890</td><td>0.859</td><td>0.614</td><td>0.608</td></tr><tr><td>Perceived ease of use (4)</td><td>0.904</td><td>0.891</td><td>0.783</td><td>0.671</td></tr><tr><td>Benevolence (3)</td><td>0.912</td><td>0.892</td><td>0.816</td><td>0.734</td></tr><tr><td>Long-term usefulness (3)</td><td>0.907</td><td>0.858</td><td>0.785</td><td>0.668</td></tr><tr><td>Image (3)</td><td>0.952</td><td>0.915</td><td>0.871</td><td>0.783</td></tr><tr><td>Intention (2)</td><td>0.910</td><td>0.865</td><td>0.862</td><td>0.762</td></tr></table>

Table 5. Discriminant validity

<table><tr><td>Construct</td><td>NTU</td><td>EOU</td><td>BEN</td><td>LTU</td><td>IM</td><td>INT</td></tr><tr><td>Near-term usefulness (NTU)</td><td>0.779</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Perceived ease of use (EOU)</td><td>0.514</td><td>0.819</td><td></td><td></td><td></td><td></td></tr><tr><td>Benevolence (BEN)</td><td>0.494</td><td>0.379</td><td>0.856</td><td></td><td></td><td></td></tr><tr><td>Long-term usefulness (LTU)</td><td>0.607</td><td>0.462</td><td>0.407</td><td>0.817</td><td></td><td></td></tr><tr><td>Image (IM)</td><td>0.335</td><td>0.442</td><td>0.442</td><td>0.457</td><td>0.885</td><td></td></tr><tr><td>Intention (INT)</td><td>0.365</td><td>0.420</td><td>0.391</td><td>0.443</td><td>0.452</td><td>0.873</td></tr></table>

Note: The bold diagonals are the square roots of the AVEs of the individual constructs; off diagonal values are the correlations between con structs (all correlation values are signi<sup>fi</sup>cant at p < 0.01 level)

We conducted a Harmon’s one-factor test to examine the common-method bias (Podsakoff et al., 2003). None of the factors was found to account for the majority of the covariance in the variables, which suggests that common method bias is unlikely to merit concern. In addition, a single factor model test was conducted. The single-factor model exhibited a poor <sup>fi</sup>t (CMIN DF = 22.95; $p < 0 . 0 0 1$ ; adjusted goodness-of-<sup>fi</sup>t index (AGFI) = 0.376; normed <sup>fi</sup>t index (NFI) $= 0 . 4 7 5 ;$ incremental <sup>fi</sup>t index (IFI) = 0.486; Tucker–Lewis index (TLI) = 0.420; comparative <sup>fi</sup>t index (CFI) = 0.484; root mean square error of approximation (RMSEA) = 0.232), against the existence of common-method bias. In addition, the measurement model test shows good mode <sup>fi</sup>t (CMIN/DF = 3.33; $p < 0 . 0 0 1$ ; AGFI = 0.850; NFI = 0.931; IFI = 0.951; TLI = 0.938; CFI = 0.951; RMSEA = 0.076).

## Calibration of the Likert scale to fuzzy sets

For performance of the FsQCA,<sup>2</sup> the variables were transformed into fuzzy sets through the use of three qualitative breakpoints: 1, 0.4, and 0. The calibration was performed in the R software environment (the code is provided in Appendix C), and the fuzzy truth table analysis was conducted afterwards by means of the software fs/QCA 2.0. For example when the fuzzy set for the variable EOU was constructed, a membership value of 1 was assigned to respondents who answered 5 in the questionnaire, 0 was assigned to an answer of 1, 0.4 was associated with 3, and the membership values for other answers were speci<sup>fi</sup>ed between these breakpoints – i.e.0.70 for an answer of 4 and 0.20 for 2. In this part of the analysis, perceived EOU, near-term USE, long-term USE, benevolence, image, and additionally gender were included in the model, to allow deriving the suf<sup>fi</sup>cient and necessary conditions for the outcome Intention. In creation of the fuzzy set for gender, male gender was coded with low membership (0) and female with high membership (1).

## Results of FsQCA analysis

Proceeding from prior literature (Table 3), we set certain assumptions for the calculation: the presence of EOU, image, benevolence, and near-term and long-term USE should associate with the presence of intention to use. Also, we set gender as a ‘both’ condition, meaning that gender would be associated with intention to use regardless of whether it was present (female users) or absent (male users).

After calibrating the variables, we set the frequency cutoff at 3 and set the consistency cutoff value to 0.93 in order to identify the different solution sets. Tables 6 and 7 show the con<sup>fi</sup>gurations of the intermediate and complex antecedent conditions that are related to high membership values in the outcome condition of behavioural intention to adopt mobile government services. The con<sup>fi</sup>gurations in Table 7 are grouped on the basis of their core conditions. The raw coverage of the solutions is between 0.109 and 0.338, and the consistency values for all solutions are above 0.92. Ragin (2008a) suggests that gaps in the upper range of consistency are useful for establishing a consistency threshold and that a threshold below 0.75 indicates sub stantial inconsistency. The high consistency of all the reported solutions also indicates that a subset relation exists and supports an argument of suf<sup>fi</sup>ciency (Rihoux & Ragin, 2009).

Table 6. Intermediate solutions of the FsQCA method

<table><tr><td rowspan="2">Solution</td><td colspan="6">Casual conditions</td><td rowspan="2">Raw coverage</td><td rowspan="2">Unique coverage</td><td rowspan="2">Consistency</td><td rowspan="2">Solution coverage</td><td rowspan="2">Solution consistency</td></tr><tr><td>Gender</td><td>Near-term usefulness</td><td>Ease of use</td><td>Long-term usefulness</td><td>Benevolence</td><td>Image</td></tr><tr><td>1</td><td>○</td><td></td><td></td><td></td><td></td><td>●</td><td>0.383</td><td>0.383</td><td>0.911</td><td>0.655</td><td>0.919</td></tr><tr><td>2</td><td>●</td><td></td><td>●</td><td>●</td><td>●</td><td></td><td>0.272</td><td>0.272</td><td>0.931</td><td></td><td></td></tr></table>

Filled circles indicate the presence of the corresponding condition, while open ones symbolize the absence of the condition (in other words, the presence of the negation of the condition). Empty cells represent ‘Don’t care’ conditions. Furthermore, large circles refer to core conditions while small circles indicate peripheral conditions

Table 7. Complex solutions of the FsQCA method

<table><tr><td rowspan="2">Solution</td><td colspan="6">Casual conditions</td><td rowspan="2">Raw coverage</td><td rowspan="2">Unique coverage</td><td rowspan="2">Consistency</td><td rowspan="2">Solution coverage</td><td rowspan="2">Solution consistency</td></tr><tr><td>Gender</td><td>Near-term usefulness</td><td>Ease of use</td><td>Long-term usefulness</td><td>Benevolence</td><td>Image</td></tr><tr><td>1a</td><td>○</td><td></td><td></td><td>●</td><td>●</td><td>●</td><td>0.338</td><td>0.015</td><td>0.956</td><td>0.637</td><td>0.933</td></tr><tr><td>1b</td><td>○</td><td>●</td><td>●</td><td></td><td>●</td><td>●</td><td>0.331</td><td>0.008</td><td>0.948</td><td></td><td></td></tr><tr><td>1c</td><td>○</td><td>●</td><td>●</td><td>●</td><td></td><td>●</td><td>0.330</td><td>0.009</td><td>0.951</td><td></td><td></td></tr><tr><td>1d</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td><td>●</td><td>0.109</td><td>0.005</td><td>0.974</td><td></td><td></td></tr><tr><td>2</td><td>●</td><td></td><td>●</td><td>●</td><td>●</td><td></td><td>0.272</td><td>0.271</td><td>0.931</td><td></td><td></td></tr></table>

Filled circles indicate the presence of the corresponding condition, while open ones symbolize the absence of the condition (in other words, the presence of the negation of the condition). Empty cells represent ‘Don’t care’ conditions. Furthermore, large circles refer to core conditions while small circles indicate peripheral conditions.

For illustration of the relationships between the ‘Intention to adopt’ outcome and the complex solutions identi<sup>fi</sup>ed, the fuzzy membership values for an observation in the two fuzzy sets cor responding to Intention and the seven solutions identi<sup>fi</sup>ed can be depicted as in Appendix D. An observation supports the suf<sup>fi</sup>ciency of a causal combination if the fuzzy membership in Inten tion is higher than the membership in the combination (i.e. the point is above the diagonal line in the plots). As we can observe, most of the cases are above the diagonal; additionally all of the <sup>fi</sup>gures indicate an asymmetric relationship between intention and the antecedent combina tions, supporting the appropriateness of FsQCA as a complement to RBMs.

Fiss (2011) has suggested that the con<sup>fi</sup>gurations can be further classi<sup>fi</sup>ed, into <sup>fi</sup>rst-order and second-order solutions, on the basis of the equi<sup>fi</sup>nality of the different core conditions exhibited. Using Fiss’s method (Fiss, 2011), we identify two <sup>fi</sup>rst-order equi<sup>fi</sup>nalities of solutions, along with a second-order, within-type equi<sup>fi</sup>nality for solution 1 (1a, 1b, 1c, and 1d), as shown in Table 7.

The results in Table 6 show that, given our assumptions, there are two major con<sup>fi</sup>gurations leading to intention to use. Speci<sup>fi</sup>cally, for a group of male users, the presence of image is suf<sup>fi</sup>cient for obtaining intention to use, regardless of these users’ perceptions of the EOU, benevolence, and near-term and long-term USE. In other words, solution 1 suggests a group of males seeking image-enhancement. Solution 2 presents a combination of the presence of EOU, long-term USE and benevolence for a group of female users. This suggests that certain female users are willing to adopt the technology if they have an aim of improvement in their quality of life in combination with a belief that the government is trustworthy in providing them with technology that can be easily used.

The unique coverage value in Table 6 suggests that con<sup>fi</sup>guration 1 uniquely covers 38.3% of the membership of the observations belonging to the fuzzy set ‘Intention to use’, while solution 2 uniquely covers 27.2% of the membership values. Therefore, solution 1 is a more prevalent recipe than con<sup>fi</sup>guration 2 for facilitating adoption of the technology.

Table 7 provides more detailed information for determination of the features of the user groups that are speci<sup>fi</sup>ed in the intermediate solutions (Table 6). For instance, solutions 1a, 1b, 1c, and 1d (Table 7) can be regarded as a detailed characterization of the major features of four key sub-groups of users as described by solution 1 in Table 6. Speci<sup>fi</sup>cally, we can see that image is a suf<sup>fi</sup>cient condition for a male user group with high membership of both be nevolence and long-term USE of adopting the technology (solution 1a). Also, image is a suf<sup>fi</sup> cient condition for another male user group with negative perceptions as to EOU, benevolence, and near-term and long-term USE of adopting the technology.

Therefore, based on both the core and peripheral conditions across all the con<sup>fi</sup>gurations, practical suggestions can be made with relevance for different user groups. This offers practitioners a reference for adopting relevant strategies based on the particular features of the different user groups. Specifically, the peripheral conditions as well as the absent' core perceptions de<sup>fi</sup>ned the features of the particular user groups. The ‘present’ core perceptions determined which strategies practitioners should improve with respect to the user groups in question.

For instance, for practitioners, the results suggest that it is important to enhance the perception of image for male users (solution 1). Speci<sup>fi</sup>cally, image will be a suf<sup>fi</sup>cient condition for four particular male user groups. These four user groups are characterized by (i) positive perceptions of long-term USE and benevolence (solution 1a); (ii) positive perceptions of nearterm USE, EOU, and benevolence (solution 1b); (iii) positive perceptions as to EOU and near-term and long-term USE (solution 1c); and (iv) negative perceptions of the perceived EOU, benevolence, and near-term and long-term USE (solution 1d). The peripheral conditions may be necessary for the core conditions to take effect. Therefore, with those males who report a high value for benevolence, it is necessary to increase the perceived long-term USE (solution 1a) or EOU and near-term USE (solution 1b), so that image can work as a suf-<sup>fi</sup>cient condition. Solution 2 indicates the strategies for females: the practitioners need to im prove the perceived EOU, benevolence and long-term USE in order for females to adopt their technology.

Furthermore, as is mentioned previously, the coverage value of a solution indicates the percentage of the aggregated membership values for the cases that take the given path speci<sup>fi</sup>ed by the solution to the outcome, enabling researchers to assess the importance of the individual causal paths. In terms of overall solution coverage, the combined models account for about 66% of membership in the outcome. No unique condition is found to be shared across all solutions, suggesting the lack of a unique necessary condition. This also suggests the exis tence of large deviations in the motivations for adopting the technology.

The theoretical implications of the results can be described in brief as (i) offering evidence that causal asymmetry exists in the context of mobile government services adoption; (ii) identi fying two main con<sup>fi</sup>gurations for the mobile government services adoption, along with their relative importance via unique coverage; (iii) discriminating the relative importance of a factor in a con<sup>fi</sup>guration through detection of core vs. peripheral factors; and (iv) specifying the relevance of a particular con<sup>fi</sup>guration to a speci<sup>fi</sup>c gender group in mobile government services adoption.

## DISCUSSION

To contrast FsQCA with RBMs, duplication of the test with an RBM was performed. The results are provided in Appendix E. Speci<sup>fi</sup>cally, the SEM test shows that perceived image, long-term USE, EOU, and benevolence have a signi<sup>fi</sup>cant in<sup>fl</sup>uence on intention to use while gender<sup>3</sup> and near-term USE are insigni<sup>fi</sup>cant determinants. The model explained 36.2% of the variance of intention to use. In other words, a high proportion of variance remains unexplained.

It is worth noting that RBMs and FsQCA differ in their assumptions and in how they interpret social phenomena, and subsequently the respective nature of both the knowledge and theory that they establish. More speci<sup>fi</sup>cally, even though RBMs and FsQCA share the same target ob jective for study of IS user behaviour, the insight they offer differs substantially (c.f. Becker & Niehaves, 2007).

From an epistemological perspective, RBMs such as MRA and SEM are instruments for obtaining ‘linear-style’ knowledge of an assumed ‘symmetric and linear’ world, and factors in this world compete in the explanation of outcomes – for example, through ${ \mathsf { R } } ^ { 2 }$ . In other words, MRA and SEM are manipulated to reduce the complexity of human nature to a symmetric and linear world through looking separately at the effect of each individual factor in order to facilitate easier, intuitive but simpli<sup>fi</sup>ed interpretation of social phenomena.

We can take the result of SEM analysis as an example. Near-term USE in this study was reported to have no signi<sup>fi</sup>cant linear relationship with intention to use. Frequently, this kind of insigni<sup>fi</sup>cant relationship is interpreted as con<sup>fi</sup>rming that there is no effect at all, because the matter of assuming of a symmetric relationship is often ignored. Meanwhile, the interpreta tion of each independent variable can (and should) be performed separately and individually. For instance, a one-unit increase in the value of image can, on its own, lead to an increase in intention to use amounting to 0.228 units (Appendix E), independently of the initial values of other variables. Therefore, suggestions from RBMs for practitioners can include adopting strategies to improve people’s perceptions of image (β = 0.228), long-term USE (β = 0.225), EOU $( \beta = 0 . 1 7 8 )$ , and benevolence (β = 0.151) and that they should not focus on near-term USE or gender issues.

Epistemologically, FsQCA describes the world of IS user phenomena in a different manner. It assumes the existence of asymmetric relationships in this world, therefore necessary and/or suf<sup>fi</sup>cient conditions are needed if one is to capture a particular social phenomenon. Accordingly, in contrast to RBMs, the world of FsQCA is not necessarily linear and symmetric, though it does not object to the existence of symmetric relationships. For instance, whilst the results of SEM analysis reject the existence of signi<sup>fi</sup>cant (linear) impact of both near-term USE and gender on intention to use, FsQCA reports the two variables as either core or peripheral conditions in different solutions that trigger the intention to adopt. In other words, factors reported with no signi<sup>fi</sup>cant linear relationships may be reported as important conditions by FsQCA from an asymmetric relationship perspective. In addition, through con<sup>fi</sup>gurations, FsQCA interpret the effect of an individual variable by considering the presence or absence of other variables, thereby resulting in an understanding of the effect of ‘variable in context’.

Moreover, when accounting for the features of RBMs, researchers have to make a symmetric hypothesis and build relevant theories that are based on symmetric relationships between variables (c.f. Davis, 1989). Frequent appearance of the same factor in different studies—as a signi<sup>fi</sup>cant and in<sup>fl</sup>uential factor in the symmetric relationship in question – is widely understood as indicating accumulation of the knowledge that this factor is important, and the theory is thereby further con<sup>fi</sup>rmed. In our illustrative study, image is the most in<sup>fl</sup>uential factor and if this <sup>fi</sup>nding is broadly con<sup>fi</sup>rmed by other studies of e-government, image would be likely utilized as a core factor in future model/theory-building linked to e-government services adoption.

In contrast, the knowledge accumulation or theory-building in FsQCA is grounded not in hy pothesized symmetric relationships between individual factors, but in the existence and popularity of con<sup>fi</sup>gurations portraying how individual factors function together in bringing about a given outcome. The frequent appearance of a particular con<sup>fi</sup>guration across different research contexts facilitates accumulating understanding of its importance or of knowledge of the con<sup>fi</sup>guration. For instance, the primacy of image among males in the solutions in the study described here highlights its importance in motivating their adoption of the technology. If substantiall more studies report similar <sup>fi</sup>ndings or con<sup>fi</sup>gurations, this fact can be used as a theoretical basis for development of relevant adoption theories. From this perspective, we tentatively propose that the major difference in theory’s building and testing between con<sup>fi</sup>gurational analysis and RBMs may be that RBM theory is fundamentally based on testing of individual factors and individually hypothesized relationships while con<sup>fi</sup>gurational analysis is based on testing the validity of particular con<sup>fi</sup>gurations or added combinations of particular variables. From our review of FsQCA literature, it seems that con<sup>fi</sup>gurational research today is still at the stage of tentatively implementing FsQCA in different contexts, on the basis of the hypothesized importance of individual factors. In this regard, we tend to believe that a long enough period for accumulating understanding of the importance of particular con<sup>fi</sup>gurations is a necessary step in providing important materials for the building of a future, more sophisticated con<sup>fi</sup>guration-based theory. More detailed comparison between RBMs and FsQCA is provided in Appendix F.

To summarize, we argue that the main bene<sup>fi</sup>t of FsQCA lies in supplementing mainstream, symmetric-relationship-based RBMs by offering a more complete understanding of IS use phenomena from an asymmetric relationship perspective: enabling new insights, greater knowledge in the <sup>fi</sup>eld, and new IS theory. Meanwhile, IS researchers should also be aware of FsQCA’s

© 2015 Blackwell Publishing Ltd, Information Systems Journal potential drawbacks (Subsection 2.4): interpreting very complex results is highly labourintensive, potentially resulting in a large amount of subjective bias. Finally, considering the features of both RBMs and FsQCA, we recommend the use of FsQCA as a supplement to mainstream RBMs in IS research when (i) the conventional symmetric approach cannot satisfactorily interpret the given IS phenomenon of interest, (ii) evidence suggesting asymmetric relationships becomes a prevalent issue (Figure 1),<sup>4</sup> or (iii) the primary task of the research is full interpretation of the given IS phenomenon of interest. Similar to SEM, construct validity is an important requirement when the relationships between latent variables can be studied for FsQCA.

## CONCLUSIONS AND LIMITATIONS

The paper has described our endeavor to introduce FsQCA to the IS behavioural research community in terms of its capacity to model asymmetric relationships among IS behaviour determinants. We believe that introducing the FsQCA to the IS user behaviour research commu nity enables new insights into IS user behaviour, in line with similar processes in other socia science disciplines. It is an in-depth guide to the use of the method and an example showcasing the differences and bene<sup>fi</sup>ts of the methodology brought by the method relative to RBMs. We hope it speeds up the IS community’s adoption of FsQCA.

Here, we have offered evidence of the asymmetric effects of IS behavioural determinants on IS behaviour. This result is not astonishing, given that pure symmetrical relationships are rare in practice (Woodside, 2013). This lays a fundamental and concrete foundation for future incorporation of FsQCA into IS behaviour research. We have also demonstrated how FsQCA aids in detecting and uncovering asymmetric relationships in explanations of IS behaviour phenomena, by such means as tailoring the data calibration technique related to full membership for the uniqueness of IS user perception variables. The identi<sup>fi</sup>cation of con<sup>fi</sup>gurations contributes to a new basis of understand ing IS user phenomena and for future development of both knowledge and theory.

Furthermore, this work has provided detailed guidance on how to use FsQCA in IS behaviour research. Various features of FsQCA have been discussed and advanced functions described, offering a possibility for IS scholars to tailor the method to the contexts of their own research. In addition, proceeding from the work of Fiss (2011), we have incorporated the concept of core and peripheral conditions into our understanding, to differentiate the effects of different condi tions in a con<sup>fi</sup>guration.

Through the study, we offer evidence that different con<sup>fi</sup>gurations leading to the same behavioural outcomes do exist. Our results show that FsQCA is applicable to IS behaviour research and can offer new insights in understanding IS phenomena. In particular, the con<sup>fi</sup>gurations assist in con<sup>fi</sup>rming and quantifying how (i) different con<sup>fi</sup>gurations of determinants lead to the same IS behaviour and that (ii) users who have negative perceptions of a certain attribute of

IS will still adopt the IS on account of the positive value they attribute to some other features of the IS. Understanding the trade-offs between individual attributes and identifying different paths to the behavioural outcome are important for researchers and practitioners alike.

The knowledge obtained from FsQCA and from RBMs are of epistemologically different nature. Harmoniously integrating knowledge gained from the use of FsQCA and RBMs into a uni<sup>fi</sup>ed theory is a challenge that our study cannot address. Given the limits of our experience and knowledge, some unknown bene<sup>fi</sup>ts and problems of applying FsQCA within IS behavioural research may exist. Furthermore, the rapid advancing of FsQCA and its broad usage may well mean that some innovative implementation of the method has appeared during our writing process. We call for further independent and innovative research to ascertain the full potential of FsQCA for IS research.

## REFERENCE

Armstrong, J. (2012) Illusions in regression analysis. International Journal of Forecasting, 28, 689–694.

Becker, J. & Niehaves, B. (2007) Epistemological perspectives on IS research: a framework for analysing and systematizing epistemological assumptions. Information Systems Journal, 17, 197–214.

Berg-Schlosser, D. & De Meur, G. (1994) Conditions of democracy in interwar Europe: a Boolean test of major hypotheses. Comparative Politics, 26, 253–279.

Blake, C. & Adolino, J. (2001) The enactment of nationa health insurance: a Boolean analysis of twenty advanced industrial countries. Journal of Health Politics, Policy and L aw, 26, 679–708

Busch, M. (1993) Using Likert scales in L2 research: a researcher comments. TESOL Quarterly, 27, 733–736.

Chang, M. & Cheung, W. (2001) Determinants of the intention to use Internet/WWW at work: a con<sup>fi</sup>rmatory study. Information & Management, 39(1), 1–14.

Cheng, C.-F., Chang, M.-L. & Li, C.-S. (2013) Con<sup>fi</sup>gura paths to successful product innovation. Journal of Business Research, 66, 2561–2573.

Chong, J., Techatassanasoontorn, A. & Doolin, B. (2013). Exploring qualitative comparative analysis in IS Research. In PACIS.

Davis, F. (1989) Perceived usefulness, perceived ease of use, and user acceptance of information technology. MIS Quarterly, 13, 319–340.

El Sawy, O.A., Malhotra, A., Park, Y. & Pavlou, P.A. (2010) Research commentary—seeking the con<sup>fi</sup>gurations of digital ecodynamics: it takes three to tango. Information Systems Research, 21, 835–848.

Eng, S. & Woodside, A.G. (2012) Con<sup>fi</sup>gural analysis of the drinking man: fuzzy-set qualitative comparative analyses, Addictive Behaviors, 37, 541–3.

Fichman, R. (2004) Going beyond the dominant paradigm for information technology innovation research: emerging concepts and methods. Journal of the Association for Information Systems, 5, 314–355.

Fishbein, M. & Ajzen, I. (1975) Belief, attitude, intention, and behavior: an introduction to theory and research. Addison-Wesley, MA.

Fiss, P. (2007) A set-theoretic approach to organizationa con<sup>fi</sup>gurations. Academy of Management Review, 32, 1180–1198.

Fiss, P. (2011) Building better causal theories: a fuzzy set approach to typologies in organization research. Academy of Management Journal, 54, 393–420

Fornell, C. & Larcker, D. (1981) Evaluating structura equation models with unobservable variables and mea surement error. Journal of Marketing Research, 18, 39–50.

Ganter, A. & Hecker, A. (2014) Con<sup>fi</sup>gurational paths to or ganizational innovation: qualitative comparative analyses of antecedents and contingencies. Journal of Business Research, 67, 1285–1292.

Gefen, D. (2000) Structural equation modelling and regression: guidelines for research practice. Communications of the Association for Information Systems, 4, 1–70.

Gigerenzer, G. (1991) From tools to theories: a heuristic of discovery in cognitive psychology. Psychological Review, 98, 254–267.

Gordin, J. (2001) The electoral fate of ethnoregionalis parties in Western Europe: a Boolean test of extant explanations. Scandinavian Political Studies, 24, 149–170.

Jamieson, S. (2004) Likert scales: how to (ab)use them. Medical Education, 381212–1218

Katz, D. & Kahn, R.L. (1978) The social psychology of or ganizations. Wiley, New York.

Lee, Y. & Kozar, K. (2008) An empirical investigation o anti-spyware software adoption: a multitheoretical per spective. Information & Management, 45, 109–119.

Leischnig, A., Geigenmueller, A. & Lohmann, S. (2014) On the role of alliance management capability, organiza tional compatibility, and interaction quality in interorgani zational technology transfer. Journal of Business Research, 67, 1049–1057.

Liu, Y., Li, H. & Carlsson, C. (2010) Factors driving the adoption of m-learning: an empirical study. Computers & Education, 55, 1211–1219.

Matzler, K., Bailom, F., Hinterhuber, H.H., Renzl, B. & Pichler, J. (2004) The asymmetric relationship between attribute-level performance and overall customer satisfaction: a reconsideration of the importance– performance analysis. Industrial Marketing Management, 33, 271–277.

Mendel, J.M. & Korjani, M.M. (2012) Charles Ragin’s fuzzy set qualitative comparative analysis (fsQCA) used for lin guistic summarizations. Information Sciences, 202, 1–23.

Mendel, J.M. & Korjani, M.M. (2013) Theoretical aspects o fuzzy set qualitative comparative analysis (fsQCA). Infor mation Sciences, 237, 137–161.

Mendelson, E. (1970) Schaum’s outline of theory and problems of Boolean algebra and switching circuits. McGraw-Hill, New York.

Moore, G. & Benbasat, I. (1991) Development of an instru ment to measure the perceptions of adopting an informa tion technology innovation. Information Systems Research, 2, 192–222.

Morris, D. (2005). Causal inference in the social sciences: variance theory, process theory, and system dynamics. In Proceedings of the 23rd International Conference of the System Dynamics Society.

Nomiya, D. 2001. Peasants’ rebellion and social change: application [of QCA] to historical data. In: Shituteki Hikaku Bunseki (Qualitative comparative analysis), N. Kanomata, D. Nomiya & K. Hasegawa, (eds.), pp. 79–94. Mineruva Syobo, Kyoto, Japan.

Park, Y. & El Sawy, O.A. (2012). Discovering the multiface ted roles of information technologies with a holistic con <sup>fi</sup>gurational theory approach. 2012 45th Hawaii International Conference on System Sciences, pp.5204–5212.

Peillon, M. (1996) A qualitative comparative analysis of welfare legitimacy. Journal of European Social Policy, 6, 175–190.

Phang, C & Li, Y. (2005). Senior citizens’ adoption of E-government: in quest of the antecedents of perceived usefulness. In Proceedings of the 38th Hawaii Interna tional Conference on System Sciences. pp. 1–8.

Podsakoff, P.M., MacKenzie, S.B., Lee, J.-Y. & Podsakoff, N.D. (2003) Common method biases in behavioral re search: a critical review of the literature and recom mended remedies. Journal of Applied Psychology, 88, 879–903.

Ragin, C.C. (2008a) Redesigning Social Inquiry: Fuzzy Sets and Beyond. University of Chicago Press, Chicago

Ragin, C. (2008b). User’s guide to fuzzy-set/qualitativ comparative analysis, Available at: http://www.u.ari zona.edu/\~cragin/fsQCA/download/fsQCAManual.pdf.

Ragin, C. & Davey, S. (2014). fs/QCA [Computer Pro gramme], Version 2.5. Available at: http://www compasss.org/software.htm.

Ragin, C. & Sonnett, J. (2005). Between complexity and parsimony: limited diversity, counterfactual cases, and comparative analysis. In: Vergleichen in de Politikwissenschaft, VS Verlag for Sozialwissencahften, Kropp S., Minkenberg M. (eds.). Springer, Wiesbaden Available at: http://escholarship.org/uc/item/1zf567tt.pd [Accessed June 22, 2014].

Ragin, C.C. (2000) In: Fuzzy Set Social Science, Ragin, C C. (ed). University of Chicago Press, Chicago.

Ragin, C.C. (1987) In: The Comparative Method: Moving Beyond Qualitative and Quantitative Strategies, Ragin C.C. (ed). University of California Press, Berkeley.

Rihoux, B. & Ragin, C.C. (2009). In: Con<sup>fi</sup>gurational com parative methods: Qualitative comparative analysis (QCA) and related techniques, Rihoux B. & Ragin C. C. (eds.). Thousand Oaks and London, Sage.

Rogers, E.M. (1983) Diffusion of innovations. Free Press New York.

Schneider, C. & Wagemann, C. (2010) Standards of good practice in qualitative comparative analysis (QCA) and fuzzy-sets. Comparative Sociology, 9, 397–418.

Seising, R. (2010). Complexity and Fuzziness in 20th Cen tury Science and Technology. In IPMU 2010. Dortmund, pp. 356–365.

Shareef, M.A., Kumar, V., Kumar, U. & Dwivedi, Y.K. (2011) e-government adoption model (GAM): differing service maturity levels. Government Information Quarterly 28(1), 17–35.

Skarmeas, D., Leonidou, C.N. & Saridakis, C. (2014) Ex amining the role of CSR skepticism using fuzzy-set qual itative comparative analysis. Journal of Business Research, 67, 1976–1805.

Thompson, R., Higgins, C. & Howell, J. (1991) Persona computing: toward a conceptual model of utilization. MIS Quarterly, 15, 125–143.

Venkatesh, V., Morris, M.G., Davis, G.G. & Davis, F.D (2003) User acceptance of information technology: to ward a uni<sup>fi</sup>ed view. MIS Quarterly, 27, 425–478.

Vink, M.P. & Van Vliet, O. (2009) Not quite crisp, not yet fuzzy? Assessing the potentials and pitfalls of multivalue QCA. Field Methods, 21, 265–289.

Vis, B. (2012) The comparative advantages of fsQCA and regression analysis for moderately large-N analyses. Sociological Methods & Research, 41, 168–198.

Wade, M.R. & Nevo, S. (2006) Development and validation of a perceptual instrument to measure e-commerce performance. International Journal of Electronic Commerce, 10, 123–146.

Wang, W. & Benbasat, I. (2005) Trust in and adoption of online recommendation agents. Journal of the Association for Information Systems, 6, 72–101.

Wendler, R., Bukvova, H. & Leupold, S. (2013). Qualitative comparative analysis in information systems and Wirtschaftsinformatik. In 11th International COnference on Wirtschaftsinformatik. pp. 1457–1471.

Woodside, A. & Zhang, M. (2013) Cultural diversity and marketing transactions: are market integration, large

community size, and world religions necessary for fair ness in ephemeral exchanges? Psychology & Marketing, 30, 263–276.

Woodside, A.G. (2013) Moving beyond multiple regression analysis to algorithms: calling for adoption of a paradigm shift from symmetric to asymmetric thinking in data analysis and crafting theory. Journal of Business Research, 66, 463–472.

Woodside, A.G., Hsu, S.-Y. & Marshall, R. (2011) General the ory of cultures’ consequences on international tourism be havior. Journal of Business Research, 64, 785–799.

Wu, P.-L., Yeh, S.-S., Huan, T.C. & Woodside, A.G. (2014) Applying complexity theory to deepen service dominant logic: con<sup>fi</sup>gural analysis of customer experience-and outcome assessments of professional services for per sonal transformations. Journal of Business Research, 67, 1647–1670.

Zadeh, L. (1965) Fuzzy sets. Information and Control, 8, 338–353.

## APPENDIX A.

## PERCEIVED EASE OF USE

EOU1: I think it is easy to access San-nong-related government information through a mobile phone.

EOU2: For me, it is easy to access San-nong-related government information through a mobile phone.

EOU3: Learning to use a mobile government for San-nong-related government information is easy.

EOU4: Overall, mobile government is easy to use.

## Perceived near-term usefulness

PU1: Mobile government improves my ef<sup>fi</sup>ciency in accessing San-nong-related government information.

PU2: Mobile government makes it easier to access San-nong-related government information.

PU3: Mobile government saves my time and effort to access San-nong-related government information.

PU4: Mobile government improves my performance to access San-nong-related government information.

© 2015 Blackwell Publishing Ltd, Information Systems Journal

## Perceived long-term usefulness

VA1: Using mobile government helps improve my family income.

VA2: Mobile government improves my production ef<sup>fi</sup>ciency.

VA3: Using mobile government helps improve the quality of my life.

## Benevolence

BE1: Mobile government puts peasants’ interests <sup>fi</sup>rst.

BE2: Mobile government keeps peasants’ interests in mind.

BE3: Mobile government understands peasants’ needs and preferences.

## Image

IM1: People who adopt mobile government have a better reputation.

IM2: People who adopt mobile government have high prestige.

IM3: People who adopt mobile government have a better social status.

## Intention

INT1: I plan to use mobile government in the future.

INT2: I predict that I will use mobile government in the future.

APPENDIX B.

<table><tr><td colspan="7">Rotated component matrix</td></tr><tr><td rowspan="2"></td><td colspan="6">Component</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>Long-term usefulness1</td><td>.202</td><td>.226</td><td>.137</td><td>.132</td><td>.827</td><td>.209</td></tr><tr><td>Long-term usefulness2</td><td>.152</td><td>.259</td><td>.198</td><td>.109</td><td>.840</td><td>.088</td></tr><tr><td>Long-term usefulness3</td><td>.185</td><td>.289</td><td>.204</td><td>.171</td><td>.785</td><td>.142</td></tr><tr><td>Near-term usefulness1</td><td>.139</td><td>.842</td><td>.019</td><td>.205</td><td>.186</td><td>.129</td></tr><tr><td>Near-term usefulness2</td><td>.192</td><td>.846</td><td>.006</td><td>.155</td><td>.191</td><td>.124</td></tr><tr><td>Near-term usefulness3</td><td>.246</td><td>.794</td><td>.108</td><td>.156</td><td>.221</td><td>.062</td></tr><tr><td>Near-term usefulness4</td><td>.259</td><td>.614</td><td>.289</td><td>.222</td><td>.349</td><td>.005</td></tr><tr><td>Benevolence1</td><td>.138</td><td>.198</td><td>.132</td><td>.881</td><td>.103</td><td>.148</td></tr><tr><td>Benevolence2</td><td>.124</td><td>.223</td><td>.178</td><td>.872</td><td>.103</td><td>.109</td></tr><tr><td>Benevolence3</td><td>.149</td><td>.160</td><td>.218</td><td>.816</td><td>.175</td><td>.093</td></tr><tr><td>Ease of Use1</td><td>.823</td><td>.205</td><td>.109</td><td>.154</td><td>.151</td><td>.056</td></tr><tr><td>Ease of Use2</td><td>.848</td><td>.135</td><td>.170</td><td>.078</td><td>.226</td><td>.053</td></tr><tr><td>Ease of Use3</td><td>.783</td><td>.242</td><td>.164</td><td>.113</td><td>.049</td><td>.189</td></tr><tr><td>Ease of Use4</td><td>.821</td><td>.148</td><td>.184</td><td>.127</td><td>.145</td><td>.190</td></tr><tr><td>Image1</td><td>.173</td><td>.108</td><td>.893</td><td>.176</td><td>.154</td><td>.148</td></tr><tr><td>Image2</td><td>.199</td><td>.093</td><td>.871</td><td>.197</td><td>.201</td><td>.145</td></tr><tr><td>Image3</td><td>.197</td><td>.035</td><td>.891</td><td>.167</td><td>.155</td><td>.166</td></tr><tr><td>Behavioural Intention1</td><td>.184</td><td>.123</td><td>.234</td><td>.168</td><td>.191</td><td>.862</td></tr><tr><td>Behavioural Intention2</td><td>.190</td><td>.131</td><td>.175</td><td>.147</td><td>.159</td><td>.884</td></tr></table>

## APPENDIX C.

#The following is the R code developed to facilitate data calibration.

#First we calibrate binary variables using the following function.

#The original variable has values 1 and 2 (if it is 0 and 1, there is no need for calibration)

bin <- function(x) x-1

\# We can calibrate every binary, Var.b.i variable as follows

Var.b.1.f <- bin(Var.b.1)

Var.b.n.f <- bin(Var.b.n)

\# Here is a general function to calibrate a variable by using an ordinal scale with k items into fuzzy memberships

\# First, we de<sup>fi</sup>ne the linear membership function on a subinterval of the domain

\# Later, x will be the scale item to be recalibrated, a and b two

\# consecutive scale items with corresponding associated fuzzy membership values m and n

bas <- function(x,a,b,m,n) m+(n-m)\*((x-a)/(b-a))

\# Using this function we can create a general calibration function

\# The m\_i values are all the membership values associated to the scale

\# and are to be de<sup>fi</sup>ned in the next step

\# The calibration will result in a piecewise linear function

likert <- function(x,m\_1,m\_2,…,m\_k) ifelse(x < 2, bas(x,1,2,m\_1,m\_2),

ifelse(x > = 2 & x < 3,bas(x,2,3,m\_2,m\_3),…

ifelse(x > = k 1 & x < = k, bas(x,k-1,k,m\_k-1,m\_k),0 ))))

#Here we de<sup>fi</sup>ne the breaking point for the membership function

$$
n \_ 1 <   - 0
$$

$$
n \_ 2 <   - 0. 2
$$

$$
n \_ 3 <   - 0. 4
$$

© 2015 Blackwell Publishing Ltd, Information Systems Journal

…n\_k <- 1

\# Finally we calibrate the ordinal variables Var.o.i

Var.o.1.f <- likert(Var.o.1,n\_1,n\_2,…,n\_k)

Var.o.m.f <- likert(Var.o.m,n\_1,n\_2,…,n\_k)

![](/api/attachments/D5EX47CE/fulltext/images/fcf4bd0e6036903e3831c962436d0f2604aa80359ab2037992ae6764568022f7.jpg)

APPENDIX D.  
![](/api/attachments/D5EX47CE/fulltext/images/67a9759cce761fcb6ba634d02de5d4a0761de9506f6edc7ae2afc04a006e0a60.jpg)

![](/api/attachments/D5EX47CE/fulltext/images/b8ea1af60ddbd9c0d2b58771308f8e166d22f804041334fdc4b34c63f255bff1.jpg)

![](/api/attachments/D5EX47CE/fulltext/images/558ad2d4e4a4ce8bf976c2a2ac66eac96b8b66816c7de90477de08d47f9a274f.jpg)

![](/api/attachments/D5EX47CE/fulltext/images/261d8180ea5dfdc8997bcee9a31865352d0fd662056136bc5ecbc5292533e43d.jpg)

![](/api/attachments/D5EX47CE/fulltext/images/84dba0c8b78a68dc051bbfba5aaf9c890311e127ebfa836eccd3a5e99226b5b1.jpg)

![](/api/attachments/D5EX47CE/fulltext/images/db1acb8db81b2caa706efca9c2b3cb2bf45acff27c120ea2ba201bfdc8bb4f9f.jpg)

APPENDIX E.

<table><tr><td>Hypothesized relationship</td><td>Path coefficient</td><td>p-value</td></tr><tr><td>Gender → Intention</td><td>0.009</td><td>Not significant</td></tr><tr><td>Near-term usefulness → Intention</td><td>-0.009</td><td>Not significant</td></tr><tr><td>Ease of use → Intention</td><td>0.178</td><td>p&lt;0.01</td></tr><tr><td>Long-term usefulness → Intention</td><td>0.225</td><td>p&lt;0.01</td></tr><tr><td>Benevolence → Intention</td><td>0.151</td><td>p&lt;0.01</td></tr><tr><td>Image → Intention</td><td>0.228</td><td>p&lt;0.001</td></tr></table>

• In RBMs, coding of gender as a numeric variable (1 or 2 for male or female respectively)

$R ^ { 2 }$ explained: 36.2%.

• Model <sup>fi</sup>t index: CMIN/DF = 3.17; p < 0.001; AGFI = 0.850; NFI = 0.929; IFI = 0.950; TLI = 0.936; CFI = 0.950; RMSEA = 0.073

• Correlation between gender and intention (correlation = - 0.032, p = 0.524).

APPENDIX F.

<table><tr><td></td><td>RBMs</td><td>FsQCA</td></tr><tr><td>Key assumptions</td><td>The relationships between variables are assumed to be symmetric and linear in MRA and SEM.- The five precursors aresymmetricallyrelated to the intention to use.</td><td>The relationships between variables can be either asymmetric or symmetric.- The precursors are identified as sufficient and/or necessary conditions for the intention to use.</td></tr><tr><td>Hypothesized direction of relationship (HDR)</td><td>HDR affects the acceptance or rejection of a hypothesis.- The precursors positively relate to intention to use.</td><td>HDR affects the results of intermediate solutions, but not complex solutions- The presence of each of five predictors is assumed to be associated with the presence of the intention to use in intermediate solutions.</td></tr><tr><td>Relationships between precursors</td><td>Precursors compete to explain the phenomena through  $R^2$ .- Adding a new precursor tends to reduce the predictive power of other variables, even though it may increase the total  $R^2$ .</td><td>Precursors cooperate to explain the phenomena by means of configurations.- Adding a new variable probably enriches the configurations. However, it may make interpretation of the result more difficult.</td></tr><tr><td>Examination of relationship</td><td>Thep-value is used:- For example: image significantly affects the intention to use at the level of p-value &lt; 0.001.</td><td>Consistency is used to measure the sufficiency of a combination- For example: a consistency 0.91 for Intermediate solution 1 means that 91% of the membership of intention to use is accounted for in the cases wherein the configuration male and image is present.</td></tr><tr><td>Interpretation of counter-hypothesized relationship (CHR)</td><td>A CHR cannot be well explained, as it conflicts with prior knowledge.- An example is found in the samples in the red region of Figure 1.</td><td>A CHR can be properly explained.- For example: people who have a negative perception of near-term usefulness may also exhibit adoption when particular conditions are satisfied.</td></tr><tr><td>Estimation for individual factor</td><td>The effect of an individual factor can and should be interpreted individually.- For example: A one-unit increase in the value for image can lead to a 0.228-unit increase in intention to use.- Explaining the effect of individual variables is easy.</td><td>Usually, the effect of a factor cannot be interpreted on its own without consideration of other factors.- An example is solution 1 in Table 6.- Explaining the effect of an individual variable is difficult.</td></tr><tr><td>Knowledge accumulation</td><td>Acceptance or rejection of a hypothesis is based on the strength of its effect.</td><td>Detection of a configuration is related to its existence and coverage value.</td></tr><tr><td>Theory-building</td><td>The generalization of hypotheses is handled by application of the assumption of a symmetric relationship.</td><td>The generalization of a configuration is based on the assumption that asymmetric relationships can exist.</td></tr></table>
