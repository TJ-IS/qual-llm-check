---
otero_id: 2454
otero_key: "MKSHM69V"
title: "Multivariate data quality assessment based on rotated factor scores and confidence ellipsoids"
authors: "Fabrício Alves de Almeida; Rodrigo Reis Leite; Guilherme Ferreira Gomes; José Henrique de Freitas Gomes; Anderson Paulo de Paiva"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.113173"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Multivariate data quality assessment based on rotated factor scores and confidence ellipsoids

Fabrício Alves de Almeida<sup>a,⁎</sup>, Rodrigo Reis Leite<sup>a</sup>, Guilherme Ferreira Gomes<sup>b</sup>, José Henrique de Freitas Gomes<sup>a</sup>, Anderson Paulo de Paiva<sup>a</sup>

<sup>a</sup> Institute of Industrial Engineering and Management, Federal University of Itajubá, Brazil

<sup>b</sup> Mechanical Engineering Institute, Federal University of Itajubá, Brazil

## A R T I C L E I N F O

Keywords: Data quality assessment Decision-making Multivariate measurement system Factor analysis Varimax rotation Confidence ellipsoid

## A B S T R A C T

This study explores the nature of the correlation in data to estimate the data quality to be used in decision: making processes. The main contribution of this research is the introduction of a new multivariate method based on rotated factor scores by varimax strategy for the repeatability and reproducibility study to efectively identify possible data of poor quality leading to measurement errors. In addition, a new confidence ellipsoid-based decision support method is developed. The eficiency of the proposed method was demonstrated using the metallographic measurements of the geometric characteristics of the resistance spot welding process. To prove the eficiency of the proposed method, it was compared with other consolidated techniques such as the analysis of variance, weighted principal components method, and factor analysis without rotation. Thus, we verified that the proposed method performed better interpretation of the latent information, minimizing the dimensionality of the data, and separating the quality attributes analyzed by clusters. One response group was classified as acceptable, and the other as marginal. These results were verified by the confidence ellipsoids, in which the proposed method obeyed the Bonferroni bilateral limits, outlining the factors which demonstrated superior discriminatory power with non-overlapping ellipsoids avoiding the confounding and favoring the better data quality analysis for multicriteria decision-making. When compared with the other approaches, the proposed method demonstrated more reliable and robust results without such deficiencies as inversion of the groupings, neglection of the variance-covariance structure, and the variability attributed to the data within the measurement system.

## 1. Introduction

Improvements in industrial processes aimed at cost reduction and quality improvement [15] are widely discussed. The researchers seek to introduce innovative methodologies based on mathematical modeling to maximize the eficiency and to improve the decision-making in these processes. Among these proposals is the study conducted by McHaney and Douglas [36]. in which they developed a multivariate regression metamodel of a decision support system (DSS) for the task of daily resource allocation in an industry. Gomes et al. [24] used an approach based on artificial neural network (ANN) modeling together with a genetic algorithm for damage detection in carbon fiber reinforced polymer (CFRP) aeronautical plates aiming to create a DSS to provide more precise decision-making for the coupling of sensors in commercial aircrafts. We can also highlight here the work of Gaudencio et al. [29], in which they used the fuzzy decision-making strategy together with the mean square error multivariate approach for the identification of optimal parameters in robust estimators applied to AISI 12 L14 free-machining steel-turning.

However, focusing all eforts on the exclusive improvement of the process may not yield a satisfactory result, as variability can often be attributed to the measurement process [2], which may compromise the quality of the data to be analyzed by the decision maker. According to Moges et al. [37], among the many factors that can afect the decisionmaking process, data quality is the most critical. According to these authors, the poor-quality data may lead to poor decision-making. Thus, they highlight the data quality issue as one of the most crucial problems in many industries. Heinrich and Klier [28] state that data quality assessment has been extensively discussed in the literature related to fields in which high-quality data is required for various business or decision-making processes. Furthermore, Timmerman and Bronselaer [45] infer that data quality is of great interest for the scientific research.

In the literature, it is possible to find several works which address the data quality issue, such as: [21,22,28,37,45]. The importance of data quality has created the need for appropriate metrics for its evaluation [28], leading to the development of diferent measurement approaches [45]. One of the most efective ways to analyze variability and uncertainty in the data quality is to use measurement system assessment (MSA). MSA is helpful in determining the ability of the system to analyze the total variability, and provides reliable aid for decisionmaking in cases where the special cause of variability is associated with the measurement system, and the common cause is variability attributed to the process itself.

According to Mast and Trip [18], there are several statistical methodologies that aim to improve the data quality and, consequently, the decision-making, such as the six sigma methodology. However, as its applicability often depends on the process data, the data quality is considered as a crucial parameter to be analyzed. Therefore, the quality of the data is of great importance. Thus, the diagnosis and identification of variability in the data intended for the use in decision-making is done to avoid taking the wrong decisions. In other words, if the data quality used in the decision-making process is not high, the decision maker may come to an unsatisfactory or even erroneous conclusion. Woodal and Borror [50] state that the best approach to analyze the capability of measurement systems is through the gage repeatability and reproducibility study (GR&R). This strategy analyzes the variability within and between systems, and verifies the consistency of the analysis corresponding to the same operator by measuring several diferent parts (or decision-making units – DMU's). Other than this, the variability of several operators in the measurements is considered. This strategy also evaluates replicated measurements, which are used to verify the con sistency and variability of an instrument or an operator, thereby prioritizing the diagnosis of the data quality. In this way, repeatability can be considered as the variation within the system and reproducibility as the variation caused by the measurements between the analyzed systems [2].

In light of the methods used in the GR&R studies, several authors emphasize the approach employing the analysis of variance (ANOVA) as a widely used technique [2,7]. ANOVA classifies the variance of the measurement system into two components, namely, repeatability and reproducibility. Several studies apply the GR&R strategy to conduct the attribute, crossed, expanded, and nested methods of analysis using the univariate ANOVA approach. The analysis of data by univariate techniques is widely used in several applications, specifically, in the economic and health oriented segments. However, when analyzing several datasets of the same segment, it is necessary to estimate the correlation between the data. Furthermore. the variance-covariance structure of the data should be taken into consideration.

Many decision-making processes possess a considerable amount of critical-to-quality characteristics (CTQ), and evaluating them univariately can result in inaccurate analysis and unsatisfactory practical conclusions [3]. A Type I error may occur when performing a statistical control in a univariate manner (i.e., separately) to track a multivariate situation. Therefore, when the data has multiple correlations, it is more appropriate to use multivariate strategies. Many authors have used multivariate approaches in several applications, such as [6,10,11,26,31,34]. However, the use of the multivariate techniques for MSA, specifically for the GR&R study, has not been explored in the literature to a great extent. Among the methods found in the published research we can outline the work of Majeske [35], who proposed the multivariate analysis of variance (MANOVA), and the work of Wang and Yang [47] that applies principal component analysis (PCA) to solve this problem. Both of the above-mentioned strategies focused on the GR &R studies. In view of these methods, Peruchi et al. [40] proposed the weighted principal component (WPC) strategy (originally proposed by Liao [33] for multiobjective optimization) for application in MSA. According to this study, the WPC approach is superior to the other techniques used in the GR&R studies (both univariate and multivariate)

because they presented more robust results and achieved confidence intervals with greater precision. Finally, Almeida et al. [17] proposed a single vector approach called weighted factor scores (WF) using nonrotating factor scores, which were weighted by their respective eigenvalues.

In relation to the research which employs multivariate methods linked to the GR&R studies, we can mention the work of Hamada [27] and Scagliarini [43], which used the MANOVA method applied to the simulated and literature data, respectively. Peruchi et al. [41] used a weighted approach based on the application of MANOVA to the steel turning process. Flyn et al. [20] used MANOVA and PCA in military applications, and Almeida et al. [3] used WPC to evaluate the variability and quality of measurement instruments in the spot welding process.

This indicates the potential for further studies and proposals to estimate the quality of massive correlated data used in the decisionmaking processes. In small or large-scale numerical procedures that can be measured (such as multicriteria decision-making processes), uncertainty should be considered when collecting these data, which eventually have a significant level of correlation. This justifies the use of multivariate techniques together with the strategies such as analytic hierarchy process (AHP). This is a widely used modern approach and has been applied in recent studies as outlined in several related articles [8,9,32,49]. To the best of our knowledge, none of the studies hitherto attempted have considered conducting a GR&R multivariate study using the factor analysis (FA) technique with a rotated axes approach to estimate the data quality for the purposes of decision-making. Almeida et al. [3] in their work initially suggested the use of FA with rotated factor scores applied to MSA to enhance the data quality analysis; however, no other work has considered this proposal with a rotated axes approach.

According to Rencher [42], the FA method seeks to reduce the repetition of information between the variables through the use of a smaller number of latent variables. This is characterized as an important method for treating data that have the variance-covariance structure due to the presence of correlation. Moreover, the factor loads estimated through extraction methods do not always allow the determination of the factors. That is, it is not always possible to clearly identify which factors a given observable variable is associated with. According to Johnson and Wichern [30], in a desirable factorial load pattern, each variable has a high factorial load on a single common factor and moderate and small loads on the remaining common factors. However, this ideal structure of factor loads is not always obtained in the real world. Therefore, rotating the original factor loads is a standard practice. According to Costello and Osborne [12], the purpose of the original factor load rotation is to obtain an easily interpretable, simpler, and clear data structure to avoid the confounding of variables.

Given the great importance of obtaining a quality correlated dataset for multicriteria decision-making applications, this paper proposes a multivariate measurement system assessment method by evaluating the repeatability and reproducibility of the measurement process. To assist in the assessment of the data quality for use in decision-making processes, we seek to improve the quality attributes to be analyzed in multicriteria processes using the proposed method, which is based on rotated factor scores. This method will allow the proper analysis of the multicorrelated structure of the data. It performs the interpretation of the latent data through the rotation of the axes, thereby reducing the dimensionality of the analyzed data and separating them into clusters. In addition, we evaluated the results using confidence ellipsoids and by conducting the variability analysis using non-overlapping multivariate confidence intervals and Bonferroni bilateral limits. This approach favors the compilation of useful information from the combined raw data, allowing for robust decision-making by analyzing the quality of the massive correlated data. To assess the performance of the proposed method, it is applied to a real process. That is, it is applied to the measurement of the geometric characteristics of the resistance spot welding (RSW) process (indentation depth, penetration, nugget width, and fusion zone). To prove the eficiency of the proposed method, the results are compared with the results of other methods found in the literature (ANOVA and WPC). In addition, the results are compared to the factor analysis conducted on the same data with unrotated scores.

This paper is organized as follows: Section 2 presents the theoretical reference to the importance of data quality in the decision-making processes. Furthermore, it discusses in detail the techniques used in the related studies (GR&R and multivariate approaches). In Section 3, the proposed method is presented, along with all the steps and equations required for its application in detail. The application of the method is presented in Section 4 with a focus on its application to the evaluation of the geometric characteristics of the spot welding process. In addition, its comparison with other methods is discussed. Finally, Section 5 presents the conclusions of the study.

## 2. Theoretical background

## 2.1. Data quality in DSSs

Data quality is regarded as the most important factor to be con sidered in decision-making processes [28], being a study area in various research segments. In decision-making processes, the results are affected by many diferent factors. However, data quality is very critical. [37]. Taking into account the constant increase in the number of studies focused on this [37], it is important to properly analyze and assess data quality.

According to Wang and Strong [48], data quality can be defined as the extent to which the data are suitable for users. Data of poor quality can lead to inappropriate decisions, which is a crucial problem for organizations [22]. Critical losses can occur when a company makes the wrong decisions owing to poor data processing [28]. This is confirmed by the studies that propose diferent dimensions for data quality [5,23,46]. In the study conducted by Wang and Strong [48], the authors emphasize that it is necessary to acknowledge the multidimensional nature of data quality by measuring the data according to the perception identified by the users. The same authors have determined that data quality depends on four diferent categories, namely: intrinsic data quality, which is related to data accuracy; accessibility data quality, which is the ease of data collection; contextual data quality, which evaluated the data against the context in which it was obtained: and representational data quality, where the data are expected to be presented clearly. Several related studies emphasize data quality in the context of DSSs [21,22,28,37,45].

Another important factor considered in the data quality studies is data assessment. According to Grange and Benbasat [25], data assessment is characterized by retrieving sophisticated and latent information from the data for the purpose of conducting precious and concise evaluation. Thus, data assessment is a way for companies to make better decisions. [25]. Although it is not the main objective of data analysis [19], there is a shortage of these types of studies in the lit erature [22]. Therefore, in this paper, we propose an alternative methodology to diagnose and measure uncertainty and the quality of massive correlated data.

## 2.2. Gage repeatability and reproducibility

One of the most widely applied strategies to analyze the elements of variation in the measurement system is the GR&R method [4,44]. GR&R may be considered as a particular example of the analysis of variance two-way with random efects [3], i.e., on efects observed for levels of a randomly selected factor. Thereby, factor A represents a set of several parts (or DMUs in that context) and factor B denotes a certain number of operators that perform the measurements. In this way, parts and operators can be considered as random factors, because both of them can be selected from a large set of options. Thus, the model for the study

can be defined as per Eq. (1):

$$
y _ {i j k} = \mu + \tau_ {i} + \beta_ {j} + (\tau \beta) _ {i j} + \varepsilon_ {i j k} \left\{ \begin{array}{l l} i = 1, 2,..., a \\ j = 1, 2,..., b \\ k = 1, 2,..., n \end{array} \right.\tag{1}
$$

where y represents the response variable, μ represents the value mean, $\tau _ { i } \sim N ( 0 , \sigma _ { \tau } )$ represents the random variable for each part, $\beta _ { j } \sim N ( 0 , \sigma _ { \beta } )$ is the random variable for operator, and $\alpha \beta _ { i j } \sim N ( 0 , \sigma _ { \tau \beta } )$ is the random variable for interaction. $\varepsilon _ { i j k } \sim N ( 0 , \sigma _ { \varepsilon } )$ is the estimated error term. In addition, a refers to the number of parts, b to the number of operators, and n to the number of replicas. Considering the independent normally distributed data with zero mean and the variances equal to ${ \sigma _ { \tau } } ^ { 2 } , { \sigma _ { \beta } } ^ { 2 } , { \sigma _ { \left( \tau \beta \right) } } ^ { 2 } ,$ respectively, the total variance can be defined as shown in $\operatorname { E q . } \ ( 2 ) ,$

$$
\sigma_ {y} ^ {2} = \sigma_ {\tau} ^ {2} + \sigma_ {\beta} ^ {2} + \sigma_ {(\tau \beta)} ^ {2} + \sigma_ {\varepsilon} ^ {2}\tag{2}
$$

These variances represent the variation components. Considering the random model for the analysis of variance, we observe that the fixed models are similar to the random models. However, they difer due to the nature of the mean square of random efects. If the null hypothesi is rejected, it is concluded that there is significant variability between the population and sample data, however, if the null hypothesis is not rejected, there is no variability in the population [38]. These concepts adopted for the GR&R study allow generalizing the sets of parts and operators. The calculation of the sum of squares (and their respective mean squares expected for random efects terms) to find the components of variance can be performed according to Eq. (3). Analogously, the expressions required to perform the GR&R study are provided in Tables 1–3.

$$
y _ {\dots} = \sum_ {i = 1} ^ {a} \sum_ {j = 1} ^ {b} \sum_ {k = 1} ^ {n} y _ {i j k} = a b n \mu + b n \sum_ {i = 1} ^ {a} \tau_ {i} + a n \sum_ {j = 1} ^ {b} \beta_ {j} + n \sum_ {i = 1} ^ {a} \sum_ {j = 1} ^ {b} (\tau \beta_ {i j}) _ {i j} + \varepsilon_ {\dots}\tag{3}
$$

To properly evaluate and classify the measurement system, the percentage of variation can be calculated using Eq. (4). Results with the variability < 10% are considered as acceptable. In addition, the number of distinct categories identified by the measurement system is calculated as per Eq. (5). Table 4 indicates the acceptance criteria of the established measurement system [1].

$$
\% R \& R = \left(\frac {\sigma_ {M S}}{\sigma_ {T}}\right) 1 0 0\tag{4}
$$

$$
n d c = \sqrt {\frac {2 \sigma_ {P} ^ {2}}{\sigma_ {M S} ^ {2}}} = 1. 4 1 \frac {\sigma_ {P}}{\sigma_ {M S}}\tag{5}
$$

## 2.3. Multivariate approaches

## 2.3.1. Factor analysis

Factor analysis (FA) is a multivariate statistical technique used to reconsider the size of a problem of the analysis, monitoring, or process improvement, when there are several response variables with statistically significant correlation structure. According to Johnson and Wichern [30], the objective of FA is to describe the various response variables $( y _ { i } , i = 1 , 2 , . . . , p )$ , which are observable in terms of common characteristics between them $( f _ { j } , j = 1 , 2 , . . . , m )$ . When m $< { \tt p } ,$ they are known as common factors or latent variables, i.e., unobservable vari ables.

Two-way ANOVA for random efects (Part I).

<table><tr><td>Source</td><td>DF</td><td>SS</td><td>MS</td></tr><tr><td>(A)</td><td>(a-1)</td><td> $SS_A = \frac{1}{(bn)} \sum_{i=1}^{a} y^{2}_{i..} - \frac{y^{2}...}{(abn)}$ </td><td> $MS_A = \frac{SS_A}{(a-1)}$ </td></tr><tr><td>(B)</td><td>(b-1)</td><td> $SS_B = \frac{1}{(an)} \sum_{j=1}^{b} y^{2}_{j.} - \frac{y^{2}...}{(abn)}$ </td><td> $MS_B = \frac{SS_B}{(b-1)}$ </td></tr><tr><td>(AB)</td><td>(a-1)(b-1)</td><td> $SS_{AB} = SS_P - SS_A - SS_B$ </td><td> $MS_{AB} = \frac{SS_{AB}}{df_{AB}}$ </td></tr><tr><td>Error</td><td>ab(n-1)</td><td> $SS_E = SS_T - SS_A - SS_B - SS_{AB}$ </td><td> $MS_E = \frac{SS_E}{ab(n-1)}$ </td></tr><tr><td>Total</td><td>(abn-1)</td><td> $SS_T = \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{i=1}^{n} y^{2}_{ijk} - \frac{(y..)^2}{abn}$ </td><td></td></tr></table>

Table 2  
Two-way ANOVA for random efects (Part II).

<table><tr><td>Source</td><td>Var Comp</td><td>F</td><td>P-Value</td></tr><tr><td>(A)</td><td> $\sigma_{\tau}^{2} = \frac{MS_{A} - MS_{AB}}{bn}$ </td><td> $F_{(A)} = \frac{MS_{A}}{MS_{AB}}$ </td><td> $1 - F_{(A)-1}[F_{A}; (a - 1); ab(n - 1)]$ </td></tr><tr><td>(B)</td><td> $\sigma_{\beta}^{2} = \frac{MS_{B} - MS_{AB}}{an}$ </td><td> $F_{(B)} = \frac{MS_{B}}{MS_{AB}}$ </td><td> $1 - F_{(B)-1}[F_{B}; (b - 1); ab(n - 1)]$ </td></tr><tr><td>(AB)</td><td> $\sigma_{\tau\beta}^{2} = \frac{MS_{AB} - MSE}{n}$ </td><td> $F_{(AB)} = \frac{MS_{AB}}{MS_{E}}$ </td><td> $1 - F_{(AB)-1}[F_{AB}; df_{AB}; ab(n - 1)]$ </td></tr><tr><td>Error</td><td> $\sigma_{e}^{2}$ </td><td></td><td></td></tr><tr><td>Total</td><td> $\sigma_{y}^{2}$ </td><td></td><td></td></tr></table>

The linear relationship that represents the FA model describing the relationship between the response variables and latent variables is mathematically expressed according to Eq. (6):

$$
\mathbf {Y} - \boldsymbol {\mu} = \mathbf {L F} + \varepsilon\tag{6}
$$

where $\mathbf { Y } _ { ( p \times 1 ) }$ is a random vector of response variables, $\mu _ { ( p \times 1 ) }$ is a vector of population means, $\mathbf { L } _ { ( p \times m ) }$ is a factor loading matrix $( \mathrm { E q . ~ } ( 7 ) ) , \mathrm { F } _ { ( m \times 1 ) }$ is a random vector of latent variables, and $\mathbf { \varepsilon } \mathbf { \varepsilon } \mathbf { e } _ { ( p \times 1 ) }$ is a random vector of errors, also known as vector-specific factors. The factor load $l _ { i j }$ comprises covariance, or correlation, between response $Y _ { i }$ and the latent variable $f _ { j } ,$ in other words, $l _ { i j }$ is a measure of influence of $Y _ { i }$ in $f _ { j }$ [42].

$$
\mathbf {L} = \left[ \begin{array}{c c c c} l _ {1 1} & l _ {1 2} & \dots & l _ {1 m} \\ l _ {2 1} & l _ {2 2} & \dots & l _ {2 m} \\ \vdots & \vdots & \ddots & \vdots \\ l _ {p 1} & l _ {p 2} & \dots & l _ {p m} \end{array} \right]\tag{7}
$$

While performing FA, it is necessary to ensure that the original set of response variables is adequate for the application of this multivariate technique in consideration [30]. To evaluate such suitability, two tests may be used: the Bartlett sphericity test, and the Kaiser-Meyer-Olkin (KMO) measure of the sampling adequacy index.

The Bartlett sphericity test assumes that the dataset $\pmb { Y } = [ Y _ { 1 } , Y _ { 2 } , . . . ,$ $Y _ { p } ] ^ { \mathrm { T } }$ follows a normal multivariate distribution and thereafter, uses the test statistic $\chi _ { \alpha ; \ \nu } { } ^ { 2 }$ to test, whether the correlation matrix is an identity matrix, where α is the level of significance and $\nu = p ( p - 1 ) / 2$ degrees of freedom. Thereby, we accept the null hypothesis that the correlation matrix is equal to the identity matrix, that is, the data are not correlated, when $\chi ^ { 2 } > \chi _ { \alpha ; \mathrm { ~ } [ p ( p - 1 ) / 2 ] } { } ^ { 2 } $ , where the value of $\chi ^ { 2 }$ is calculated according to Eq. (8), and in this equation n is the number of observations in each response [42].

Gage R&R: percentage of contribution and study variation.  
Table 4  
Classification criteria for the measurement system.

<table><tr><td>Measurement System Assesment</td><td>%GR&amp;R</td></tr><tr><td>Acceptable</td><td>&lt; 10%</td></tr><tr><td>Marginal</td><td>10%-30%</td></tr><tr><td>Unacceptable</td><td>&gt;30%</td></tr><tr><td>ndc</td><td>&gt;5</td></tr></table>

$$
\chi^ {2} = - \left[ n - 1 - \frac {(2 p + 5)}{6} \right] \ln | \mathbf {R} |\tag{8}
$$

The KMO index ranges from 0 to 1, and is deemed acceptable when its values $\tt a r e > 0 . 5 ,$ . This index can be calculated according to Eq. (9), where $r _ { i j }$ and $q _ { i j }$ are the sample correlation matrices R and the antiimage correlation matrix Q [42], respectively.

$$
K M O = \frac {\sum_ {i \neq j} r _ {i j} ^ {2}}{\sum_ {i \neq j} r _ {i j} ^ {2} + \sum_ {i \neq j} q _ {i j} ^ {2}}\tag{9}
$$

The mathematical emphasis in FA is to express the population covariance $\pmb { \Sigma } _ { ( p \times p ) }$ matrix in terms of L and $\Psi ( p \times p )$ . This is known as the specific variance matrix, in which the main diagonal terms are $\psi _ { i }$ (errors), and the terms outside the main diagonal are null. As the population parameters are unknown, the matrix Σ can be estimated by the sample covariance matrix $\pmb { S } _ { ( p \times p ) } .$ However, in most problems involving multivariate analyses, the scales between the response variables are discrepant; therefore, it is more appropriate to model the sample correlation matrix $\mathbf { R } _ { ( p \times p ) } ,$ which is insensitive to the discrepancy between the original scales and produces more accurate results when compared to the case where S is used. Therefore, the matrix R can be expressed according to Eq. (10). From Eq. (10), it is derived that ${ \Sigma _ { j = 1 } } ^ { m } { l _ { i j } } ^ { \bar { 2 } } = { h _ { i } } ^ { 2 } ;$ which is the $i ^ { t h }$ commonality comprising a part of the total variance of $Y _ { i }$ explained by all the latent variables; and $\psi _ { i }$ is a part of the total variance of $Y _ { i }$ explained by the specific factor ε [42].

$$
\mathbf {R} = \mathbf {L L} ^ {T} + \boldsymbol {\Psi}\tag{10}
$$

<table><tr><td>Source</td><td>Var comp</td><td>% Contribution</td><td>%Study var</td></tr><tr><td>Total Gage R&amp;R</td><td> $\sigma_{\beta}^{2} + \sigma_{\tau\beta}^{2} + \sigma_{\varepsilon}^{2}$ </td><td> $\frac{(\sigma_{\beta}^{2} + \sigma_{\tau\beta}^{2} + \sigma_{\varepsilon}^{2})}{\sigma_{\mathbf{T}}^{2}}$ </td><td> $\left( \frac{1}{\sigma_{\mathbf{T}}} \right) \sqrt{(\sigma_{\beta}^{2} + \sigma_{\tau\beta}^{2} + \sigma_{\varepsilon}^{2})}$ </td></tr><tr><td>Repeatability</td><td> $\sigma_{e}^{2}$ </td><td> $\frac{\sigma_{\varepsilon}^{2}}{\sigma_{\mathbf{T}}^{2}}$ </td><td> $\frac{\sigma_{\varepsilon}}{\sigma_{\mathbf{T}}}$ </td></tr><tr><td>Reproductibility</td><td> $\sigma_{\beta}^{2} + \sigma_{\tau\beta}^{2}$ </td><td> $\frac{(\sigma_{\beta}^{2} + \sigma_{\tau\beta}^{2})}{\sigma_{\mathbf{T}}^{2}}$ </td><td> $\left( \frac{1}{\sigma_{\mathbf{T}}} \right) \sqrt{(\sigma_{\beta}^{2} + \sigma_{\tau\beta}^{2})}$ </td></tr><tr><td>Operators</td><td> $\sigma_{\beta}^{2}$ </td><td> $\frac{\sigma_{\beta}^{2}}{\sigma_{\mathbf{T}}^{2}}$ </td><td> $\frac{\sigma_{\beta}}{\sigma_{\mathbf{T}}}$ </td></tr><tr><td>Part-to-part</td><td> $\sigma_{\tau}^{2}$ </td><td> $\frac{\sigma_{\tau}^{2}}{\sigma_{\mathbf{T}}^{2}}$ </td><td> $\frac{\sigma_{\tau}}{\sigma_{\mathbf{T}}}$ </td></tr><tr><td>Total variation</td><td> $\sigma_{\mathbf{T}}^{2} = \sigma_{\tau}^{2} + \sigma_{\beta}^{2} + \sigma_{\tau\beta}^{2} + \sigma_{\varepsilon}^{2}$ </td><td>100%</td><td>100%</td></tr></table>

To calculate L and Ψ, several estimation methods can be used. The most commonly methods used are the principal component (PC) method and the maximum likelihood (ML) methods. The PC method is usually preferred among the others most widely used, because it does not require a specific probability distribution of the response variables, and consequently, is more robust in terms of the original data. This method is based on the spectral decomposition of the matrices S or R used to estimate factor loads and specific variances [30].

According to the mathematical perspective of factorial load estimation of the PC method, the matrix L can be estimated according to Eq. (11):

$$
\mathbf {L} = \mathbf {P} _ {m} \boldsymbol {\Lambda} _ {m} ^ {1 / 2} = [ \sqrt {\lambda_ {1}} \mathbf {e} _ {1}, \sqrt {\lambda_ {2}} \mathbf {e} _ {2}, \dots , \sqrt {\lambda_ {m}} \mathbf {e} _ {m} ]\tag{11}
$$

where ${ \bf P } _ { m } = [ { \bf e } _ { 1 } , ~ { \bf e } _ { 2 } , . . . , ~ { \bf e } _ { m } ]$ is a matrix $p \times$ m of the first m normalized eigenvectors of R; and ${ \Lambda } _ { m } = { \left[ { \lambda } _ { i } \right] }$ is a diagonal matrix $m \times m$ of the eigenvalues $( \lambda _ { i } )$ of R, where both matrices are obtained through the spectral decomposition of R. Therefore, the specific variances are ob tained using Eqs. (10) and (11), according to Eq. (12).

$$
\boldsymbol {\Psi} = \operatorname{diag} (\mathbf {R} - \mathbf {L L} ^ {T})\tag{12}
$$

There are several criteria to choose the number of factors m, while performing $\mathrm { F A , }$ necessarily being $m \ < \ p .$ Rencher [42] highlights the two main criteria: the number of factors m has to be suficient to obtain a cumulative variance ratio of at least 80% of the total variance; while using the sample correlation matrix, the quantity of factors m has to be equal to the quantity of eigenvalues greater than the mean eigenvalues, in this case $\lambda i \geq 1$

In most cases, the interpretation of factor loads is dificult; therefore, it is important to rotate the factor loads. This approach benefits from a simpler load structure that can be obtained to facilitate the association of the factors common to the response variables [12]. The rotated factor load matrix, called L<sup>°</sup>, has the same ability to reproduce S or R and also maintains the estimates of commonalities and specific variances as $\begin{array} { r } { \bar { { \bf L } } ^ { \mathrm { ~ \tiny ~ { ~ = ~ } ~ } } { \bf L } { \bf T } , } \end{array}$ where T is an orthogonal matrix for rotating L [42]. According to Johnson and Wichern [30], the rotation method most commonly used for this purpose is known as varimax. This rotation method allows the selection of an orthogonal matrix T to generate rotated factor loadings that maximize the objective function of variance expressed in Eq. (13).

$$
V = \frac {1}{p} \sum_ {j = 1} ^ {m} \left[ \sum_ {i = 1} ^ {p} \tilde {l} _ {i j} ^ {\circ 4} - \left(\sum_ {i = 1} ^ {p} \tilde {l} _ {i j} ^ {\circ 2}\right) ^ {2} / p \right]\tag{13}
$$

where $\widetilde { l } _ { i j } ^ { \circ } = l _ { i j } ^ { \circ } / \sqrt { h _ { i } ^ { 2 } } , \mathrm { i . e . , }$ , the relation between the rotated factorial load and the $i ^ { t h }$ commonality.

In FA, it is common to obtain estimates (factor scores) of the latent variables to conduct subsequent procedures, such as analysis and optimizations. According to Johnson and Wichern [30], estimates of the common factors can be obtained by minimizing the sum of squared residuals of the factor model. Thereby, the rotated factor scores are obtained according to Eq. (14):

$$
\mathbf {F} = \mathbf {Z} [ \mathbf {L} ^ {\circ} (\mathbf {L} ^ {\circ T} \mathbf {L} ^ {\circ}) ^ {- 1} ]\tag{14}
$$

where $\mathbf { F } _ { ( n \times m ) }$ is the matrix of estimates of rotated latent variables $\mathbf { R } ,$ n is the number of observations in each response variable, and ${ \bf { Z } } _ { ( n \times p ) }$ is the matrix of the standardized values of the response variables.

## 2.3.2. Confidence region for simultaneous intervals

Estimation of the confidence intervals for multivariate cases can performed using the region of the diference of mean vectors. The confidence region in the multivariate case can be defined considering the distribution $T ^ { 2 }$ Hotelling, where, according to Ferreira [13], a region of 100(1–α) % confidence is defined by Eq. (15):

$$
C R = \left\{\boldsymbol {\mu} _ {d} \in \Re^ {p} \middle | n (\boldsymbol {\mu} _ {d} - \overline {{\mathbf {d}}}) ^ {T} \mathbf {s} _ {d} ^ {- 1} (\boldsymbol {\mu} _ {d} - \overline {{\mathbf {d}}}) \leq \frac {\nu p}{\nu + 1 - p} F _ {\alpha , p, \nu + 1 - p} \right\}\tag{15}
$$

where $\nu = n - 1 ,$ , and $F _ { \alpha , \ p , \ \nu + 1 - p }$ is the upper 100α% quantile of the F distribution with $p \texttt { e } \nu + 1 - p$ degrees of freedom. Considering a bivariate case, using the eigenvalues and eigenvectors of Σ given by Eqs. (16) and (17), respectively, it is possible to illustrate this region called the confidence ellipsoids.

$$
\lambda_ {i} = \frac {\sigma_ {1 1} + \sigma_ {2 2} \pm \sqrt {(\sigma_ {1 1} - \sigma_ {2 2}) ^ {2} + 4 \sigma_ {1 2} ^ {2}}}{2}; i = 1, 2\tag{16}
$$

$$
\cos (\theta) = \frac {\sigma_ {1 2}}{\sqrt {(\lambda_ {1} - \sigma_ {1 1}) ^ {2} + \sigma_ {1 2} ^ {2}}}\tag{17}
$$

To evaluate simultaneous confidence intervals for a linear combination of the mean vector of the diferences $\pmb { \mu _ { d } } = \pmb { \delta }$ given by $e ^ { \mathrm { T } } \delta = e _ { 1 } \delta _ { 1 } + \ e _ { 2 } \delta _ { 2 } + \ldots + e _ { p } \delta _ { p }$ according to Ferreira [13], we use the maximum likelihood (ML) estimator given by the linear combination of the ML estimator of the mean vector, i.e., $\mathbf { e } ^ { T } \overline { { \mathbf { D } } } _ { . } = e _ { 1 } \overline { { D } } _ { . 1 } + e _ { 2 } \overline { { D } } _ { . 2 } + . . . + e _ { p } \overline { { D } } _ { . p } .$ Covariance of this linear combination is expressed as Cov(e $\bar { \mathbf { \Gamma } } \overline { { \mathbf { D } } } \mathbf { ) } = e ^ { T } \pmb { \Sigma } _ { d } \pmb { e } / n$ . For a sample case, we use the estimator given by $\widehat { \pmb { \Sigma } } = ( \mathbf { e } ^ { T } \overline { { \mathbf { D } } } ) = e ^ { T } \pmb { S } _ { d } \mathbf { e } / n$

Thus, to analyze the Bonferroni bilateral intervals, we can use the following equation described in Eq. (18) [13].

$$
C I _ {1 - \alpha} (\mathbf {e} ^ {T} \pmb {\mu} _ {d}) \colon \quad \mathbf {e} ^ {T} \overline {{\mathbf {D}}} _ {.} \pm t _ {\alpha / (2 m), \nu} \sqrt {\frac {\mathbf {e} ^ {T} \mathbf {S} _ {d} \mathbf {e}}{n}}\tag{18}
$$

where, $t _ { \alpha / ( 2 m ) } ,$ ν is the upper 100α% quantile of t of the Student distribution, and $\nu = n - 1 ,$ for m diferent choices of the linear combi nation vector e.

Considering the strategies discussed above, it is possible to implement the proposed method adequately.

## 3. Multivariate decision-making approach employed for measurement system and based on rotated factor scores and confidence ellipsoids

Given the importance of ensuring appropriate data quality in DSSs, it is necessary to properly assess the data quality, so that the decisionmaking process is not skewed by the use of data of insuficient quality. To evaluate the data quality, one has to evaluate variability of the considered dataset. For this purpose, the repeatability and reproducibility study can be applied, which consist of many approaches to ensure reliability of the analysis. In multicriteria decision-making, one should consider the variance-covariance structure of the data. Among these approaches, the most important are those ones that prioritize the correlated data, such as MANOVA, PCA, WPC, and WF.

Almeida et al. [3] suggested an approach for multivariate studies that uses the factor analysis strategy. Furthermore, it is able to perform the interpretation of data properly. Therefore, the present study proposes a new multivariate approach to gage the studies based on rotated factor scores and confidence ellipsoids. This approach has an advantage in terms of the interpretation of latent information owing to its ability to rotate the axes using the varimax method. This allows for the better explanation of information, as well as the formation of appropriate clusters and prioritization of the assessment of the data quality for multicriteria decision-making processes. The proposed method for rotated factor scores includes the steps shown in Fig. 1.

Step 1: Assess the correlation structure between the quality characteristics

To obtain an a priori properly designed data collection for a GR&R study, it is necessary to evaluate the correlation of the data (the data quality characteristics). This evaluation is verified through the Pearson correlation as described in Eq. (19).

$$
\rho_ {C T Q _ {i} C T Q _ {j}} = \frac {C o v _ {C T Q _ {i} C T Q _ {j}}}{\sqrt {\sigma_ {C T Q _ {i}} ^ {2} \sigma_ {C T Q _ {j}} ^ {2}}} ; \quad \forall i, j = 1, 2, \dots , q\tag{19}
$$

After calculating the correlation, its significance should be checked. If the correlation is significant, then the data are suitable to be applied to the multivariate strategy; therefore, Step 2 can be executed. If the data characteristics do not confirm the presence of a significant correlation, a univariate approach such as the ANOVA method needs to be applied (Step 1.1).

Step 2: Apply the Bartlett sphericity test and estimate the KMO index to verify the suitability for FA

![](/api/attachments/MKSHM69V/fulltext/images/a1ef62a0b434997163d14a5d82eac1460f26274da0c67d580984e7206ad14743.jpg)  
Fig. 1. Flowchart of the steps involved in the proposed method.

After verifying if the data present has a significant variance-covariance structure, the next step is to check if the data are appropriate to use the FA strategy. To do this, the proposed method applies the Bartlett sphericity test and the Kaiser-Meyer-Olkin measure of the sampling adequacy index described in Eqs. (8) and (9), respectively.

If the data are adequate to apply FA, the method proceeds to Step 3. If the data are not suitable, another multivariate approach, such as the PCA strategy, should be used for the analysis (Step 2.1).

## Step 3: Extract the rotated factor scores

In the view of the nature of correlated data, the FA method is applied to extract the rotated factor scores using the varimax method. This step can be divided into 4 substeps:

Initially, the number of factors that are necessary to obtain satisfactory interpretation of the data should be determined. To do this, the proposed method applies the Kaiser criterion [42], which indicates that a quantity of m factors that have an eigenvalue ≥1 should be considered. In addition, the explanation percentage is also considered. That is, it is considered appropriate if the factors explain at least 80% of the data.

After defining the number of factors, the factor scores are to be estimated. The factor scores are estimated through the principal components using the regression method called the ordinary least squares (OLS). The variance of the $j ^ { t h }$ factor in relation to the total variation is calculated according to Eq. (20). The covariance between the factors is expected to be equal to $\delta , \mathrm { i . e . , }$ , the factors are not related to each other, which can be expressed as per Eq. (21) [42].

$$
V a r (f _ {j}) = \sum_ {i = 1} ^ {p} l _ {i j} ^ {\circ 2}\tag{20}
$$

$$
C o v (\mathbf {F}) = E \left(\mathbf {F} \mathbf {F} ^ {T}\right) = \mathbf {I} _ {(m \times m)} = \left[ \begin{array}{c c c c} 1 & 0 & \dots & 0 \\ 0 & 1 & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & 1 \end{array} \right]\tag{21}
$$

• The rotated factor scores can be obtained as per Eq. (22). Therefore, the first column of the matrix F is composed of the n scores of the first factor, and the second column of F is composed of the n scores of the second factor, and so on.

$$
\begin{array}{l} \mathbf {F} = \mathbf {Z} [ \mathbf {L} ^ {\circ} (\mathbf {L} ^ {\circ T} \mathbf {L} ^ {\circ}) ^ {- 1} ] \\ = \left[ \begin{array}{c c c c} \left(\frac {C T Q _ {1 1} - \overline {{C T Q _ {1}}}}{\sqrt {s _ {1 1}}}\right) & \left(\frac {C T Q _ {1 2} - \overline {{C T Q _ {2}}}}{\sqrt {s _ {2 2}}}\right) & \dots & \left(\frac {C T Q _ {1 p} - \overline {{C T Q _ {p}}}}{\sqrt {s _ {p p}}}\right) \\ \left(\frac {C T Q _ {2 1} - \overline {{C Q T _ {1}}}}{\sqrt {s _ {1 1}}}\right) & \left(\frac {C T Q _ {2 2} - \overline {{C T Q _ {2}}}}{\sqrt {s _ {2 2}}}\right) & \dots & \left(\frac {C T Q _ {2 p} - \overline {{C T Q _ {p}}}}{\sqrt {s _ {p p}}}\right) \\ \vdots & \vdots & \ddots & \vdots \\ \left(\frac {C T Q _ {n 1} - \overline {{C T Q _ {1}}}}{\sqrt {s _ {1 1}}}\right) & \left(\frac {C T Q _ {n 2} - \overline {{C T Q _ {2}}}}{\sqrt {s _ {2 2}}}\right) & \dots & \left(\frac {C T Q _ {n p} - \overline {{C T Q _ {p}}}}{\sqrt {s _ {p p}}}\right) \end{array} \right] \times \\ \left\{\left[ \begin{array}{c c c c} l _ {1 1} ^ {\circ} & l _ {1 2} ^ {\circ} & \dots & l _ {1 m} ^ {\circ} \\ l _ {2 1} ^ {\circ} & l _ {2 2} ^ {\circ} & \dots & l _ {2 m} ^ {\circ} \\ \vdots & \vdots & \ddots & \vdots \\ l _ {p 1} ^ {\circ} & l _ {p 2} ^ {\circ} & \dots & l _ {p m} ^ {\circ} \end{array} \right] \times \left(\left[ \begin{array}{c c c c} l _ {1 1} ^ {\circ} & l _ {2 1} ^ {\circ} & \dots & l _ {p 1} ^ {\circ} \\ l _ {1 2} ^ {\circ} & l _ {2 2} ^ {\circ} & \dots & l _ {p 2} ^ {\circ} \\ \vdots & \vdots & \ddots & \vdots \\ l _ {1 m} ^ {\circ} & l _ {2 m} ^ {\circ} & \dots & l _ {p m} ^ {\circ} \end{array} \right] \times \left[ \begin{array}{c c c c} l _ {1 1} ^ {\circ} & l _ {1 2} ^ {\circ} & \dots & l _ {1 m} ^ {\circ} \\ l _ {2 1} ^ {\circ} & l _ {2 2} ^ {\circ} & \dots & l _ {2 m} ^ {\circ} \\ \vdots & \vdots & \ddots \\ l _ {p 1} ^ {\circ} & l _ {p 2} ^ {\circ} & \dots & l _ {p m} ^ {\circ} \end{array} \right]\right) ^ {- 1} \right\} \\ \end{array}\tag{22}
$$

• After obtaining the rotated factor scores, it is possible to verify, which vector of the factors better interprets certain quality characteristics (depending on the quantity of factors). Thereby, the method generates the formation of grouping, or cluster, between the factor scores and the original data. It is important to note that if only one factor is used, it is not possible to perform the rotation strategy. Step 4: Estimate variance components

Given the rotated factor scores obtained using the varimax method, as mentioned in the previous step, it is possible to estimate the variation components of the study. Therefore, for the rotated factor scores, we have the FA model for the measurement system with significant interaction term as described by Eq. (23):

Table 5  
Variation components for the $\mathrm { G R } \& \mathrm { R } _ { \mathrm { m } }$ study.

<table><tr><td></td><td></td><td colspan="2">With interaction</td><td>Without interaction</td></tr><tr><td>Process</td><td> $\hat{\sigma}_{P}^{2}$ </td><td>=</td><td> $\frac{MS_{A}-MS_{AB}}{bn}$ </td><td> $\frac{MS_{A}-MS_{E}}{bn}$ </td></tr><tr><td>Repeatability</td><td> $\hat{\sigma}_{repeat}^{2}$ </td><td>=</td><td> $MS_{E}$ </td><td> $MS_{E}$ </td></tr><tr><td>Reproducibility</td><td> $\hat{\sigma}_{reprod}^{2}$ </td><td>=</td><td> $\frac{MS_{B}-MS_{AB}}{an}+\frac{MS_{AB}-MS_{E}}{n}$ </td><td> $\frac{MS_{B}-MS_{E}}{an}$ </td></tr><tr><td>Measurement system</td><td> $\hat{\sigma}_{MS}^{2}$ </td><td>=</td><td> $\hat{\sigma}_{repeat}^{2}+\hat{\sigma}_{reprod}^{2}$ </td><td> $\hat{\sigma}_{repeat}^{2}+\hat{\sigma}_{reprod}^{2}$ </td></tr><tr><td>Total variation</td><td> $\hat{\sigma}_{T}^{2}$ </td><td>=</td><td> $\hat{\sigma}_{P}^{2}+\hat{\sigma}_{MS}^{2}$ </td><td> $\hat{\sigma}_{P}^{2}+\hat{\sigma}_{MS}^{2}$ </td></tr></table>

$$
\mathbf {F A} _ {i j k} = \mu + \tau_ {i} + \beta_ {j} + (\tau \beta) _ {i j} + \varepsilon_ {i j k} \left\{ \begin{array}{l l} i = 1, 2, \dots , a \\ j = 1, 2, \dots , b \\ k = 1, 2, \dots , n \end{array} \right.\tag{23}
$$

where we have the following variables: $\mu$ is constant; τ , β , τβ , and ε are independent random variables with zero mean and variance $\sigma _ { \tau } ^ { 2 } , \sigma _ { \beta } ^ { \dot { 2 } } ,$ ${ \sigma _ { \tau \beta } } ^ { 2 } ,$ , and ${ \sigma _ { \varepsilon } } ^ { 2 } ,$ respectively. The variation components are presented in detail in Table 5, where $M S _ { A } , M S _ { B } , M S _ { A B } ,$ and $M S _ { E }$ represent the mean squares for the part factor, operator factor, interaction term, and error term, respectively.

However, if the analysis on variance indicates that the term of interaction between the part and the operator is insignificant, it has to be removed. In this way, the summarized model can be represented as per Eq. (24), where the variation components are those as indicated in Table 5.

$$
\mathbf {F A} _ {i j k} = \mu + \tau_ {i} + \beta_ {j} + \varepsilon_ {i j k}\tag{24}
$$

Step 5: Estimate the multivariate indices and confidence ellipsoids

After estimating the variation components, the next step is to calculate the multivariate indicators of the study. These indicators can be classified by the contribution percentage of the system variability (%R& ${ \boldsymbol { R _ { m } } } )$ and the number of distinct categories identified by the system $( n d c _ { m } )$ . Therefore, for multivariate indicators, we need to perform the calculation of $\% R \& R _ { m }$ and $n d c _ { m }$ according to Eqs. (25) and (26), respectively. Considering the same indications of AIAG [1], we obtain the classification criteria for the measurement system as presented in Table 4.

$$
\% R \& R _ {m} = \sqrt {\frac {\sigma_ {M S} ^ {2}}{(\sigma_ {P} ^ {2} + \sigma_ {M S} ^ {2})}} \times 1 0 0\tag{25}
$$

$$
n d c _ {m} = \sqrt {2 \left[ \frac {\sigma_ {\tau} ^ {2}}{(\sigma_ {\beta} ^ {2} + \sigma_ {\tau \beta} ^ {2}) + \sigma_ {\varepsilon} ^ {2}} \right]}\tag{26}
$$

In addition to the multivariate indicators, the confidence intervals for the measurements need to be calculated. In the case of multiple correlation in the data, it is appropriate to evaluate multivariate confidence intervals through confidence ellipses. The ellipses/ellipsoids allow evaluating the region of confidence for the mean and the data. In this way, it is possible to verify if the values present greater confounding to identify the distinct categories in the system analyzing ellipses that overlap with each other. Thereby, from previous calculations and information on eigenvalues and eigenvectors, we defined the for mulation of the proposed confidence ellipsoids described by Eq. (27).

$$
\left\{ \begin{array}{l} E \left[ \widehat {y} _ {1} (\mathbf {x} | \mathbf {x} _ {0} ^ {i}) \right] \\ E \left[ \widehat {y} _ {2} (\mathbf {x} | \mathbf {x} _ {0} ^ {i}) \right] \end{array} \right\} + \sqrt {\frac {p (n - 1)}{n (n - p)} F _ {(p , n - p)} (\alpha)} \times \left[ \begin{array}{c c} \sqrt {\lambda_ {1}} & 0 \\ 0 & \sqrt {\lambda_ {2}} \end{array} \right] \times \left[ \begin{array}{c c} e _ {1 1} & e _ {1 2} \\ e _ {2 1} & e _ {2 2} \end{array} \right] \times \left[ \begin{array}{c c} e _ {1 3} & e _ {1 4} \\ e _ {2 3} & e _ {2 4} \end{array} \right]\tag{27}
$$

![](/api/attachments/MKSHM69V/fulltext/images/1810b8829dd51a9ad255b7fee776179520030d1a9fd3016278d961f9560d6152.jpg)  
Fig. 2. Constant density ellipsoid.

for $O \leq \theta \leq \pi ,$ , where $\begin{array} { r } { \left[ { E } \left[ \widehat { y _ { 1 } } ( \mathbf { x } \mid \mathbf { x } _ { 0 } ^ { i } ) \right] \right] = \left[ { \pmb { \mu } } _ { x } \right] } \\ { { E } \left[ \widehat { y _ { 2 } } ( \mathbf { x } \mid \mathbf { x } _ { 0 } ^ { i } ) \right] \Big | = \left[ { \pmb { \mu } } _ { y } \right] } \end{array}$ represents the mear vector; $[ \lambda _ { 1 } \lambda _ { 2 } ] ^ { \mathrm { T } }$ and $\left[ { \begin{array} { l l } { e _ { 1 1 } } & { e _ { 1 2 } } \\ { e _ { 2 1 } } & { e _ { 2 2 } } \end{array} } \right]$ are the eigenvalues and the eigenvector matrix of $\Sigma ,$ respectively; p indicates the number of variables analyzed; n is the number of observations in the dataset; $\mathbf { x } _ { O } ^ { i }$ is the $i ^ { t h }$ measured part. Tetha (θ) is the angle used to calculate the parametric coordinates of the ellipse at each point of the $X Y$ plane. In Appendix $\mathrm { A } ,$ the description is provided on the mathematical details of the concentration ellipsoid definition for multivariate confidence intervals used in this study.

It is possible to illustrate the confidence ellipsoids for the means and for the data from the two-dimensional perspective and, consequently, to evaluate the measurement system by checking if the ellipsoids overlap and measuring the assigned variability. Fig. 2 shows the normal bivariate random vector constant density ellipsoid for a confidence interval $( \lambda - \alpha )$

After calculation of the confidence ellipsoids for the means, the proposed method verifies whether the ellipses respect the intervals of the Bonferroni bilateral limits to confirm the adequacy of the obtained results. Considering the ML estimator given by the linear combination of the estimator ML of the vectors of meanse ${ } ^ { T } \mathbf { C T Q } . = e _ { 1 } \overline { { { C T Q } _ { . 1 } } } + e _ { 2 } \overline { { { C T Q } _ { . 2 } } } + . . . + e _ { p } \overline { { { C T Q } _ { . p } } } ,$ the Bonferroni bilateral interval can be described according to Eq. (28).

$$
C I _ {1 - \alpha} (\mathbf {e} ^ {T} \boldsymbol {\mu} _ {d}) \colon \quad \mathbf {e} ^ {T} \overline {{\mathbf {C T Q .}}} \pm t _ {\alpha / (2 m), \nu} \sqrt {\frac {\mathbf {e} ^ {T} \mathbf {S} _ {d} \mathbf {e}}{n}}\tag{28}
$$

## 4. Experimental application

## 4.1. Resistance spot welding (RSW)

To demonstrate the application of the proposed method, an experimental study was conducted on a real and widely used process in the industry, the resistance spot welding (RSW). It is possible to check the quality attributes of RSW through the specific tests [14]. Considering the end product, it is possible to verify the geometrical char acteristics of the spot weld quality, such as indentation depth (ID), penetration (P), nugget width (NW), and the fusion zone (FZ) [51]. These characteristics can be verified according to the scheme presented in Fig. 3.

All measurements were performed in a random manner using eight parts (a), three replicates (n), four diferent operators (b). In total, 96 data points were obtained for each test collecting four distinct quality characteristics (ID, P, NW, and FZ) and presenting a total of 384

Table 7

![](/api/attachments/MKSHM69V/fulltext/images/c26d9ec6489a148435f121473ce738ceece0259e6968210bc414e9c463b9c0c3.jpg)  
Fig. 3. Geometric characterization of the welded point.

measurement data points described in Table 6.

## 4.2. Application of the proposed method

Using the measurements of the attributes (or the data quality characteristics) described in Table $^ { 6 , }$ we can apply the proposed method as described in Fig. 1. All statistical treatments and proposals were implemented using the software R Studio®, Visual Basic for Applications (VBA), and Minitab18®. Running the procedure described in Step 1, it is possible to verify that the attributes present significant correlation with the Pearson maximum value equal to 0.890 for the char acteristics FZ and P, as outlined in Table 7.

Prior to initiating Step 2, the multivariate normality of the original dataset represented by the vector CTQ = [FZ, P, ID, NW] was tested. The Mardia multivariate normality test revealed that the data from the original CTQs did not follow the normal multivariate probability dis tribution, as the Mardia skewness and kurtosis measurements were both non-significant with p-value = .000.

At Step 2, the Bartlett sphericity test was applied, because the same part of the assumption that the dataset follows a normal multivariate distribution was considered. Consequently, to test the adequacy of CTQs to the application of FA, only the KMO measurement was used. The overall KMO was 0.72 indicating an appropriate degree of adequacy of CTQs applied to FA. In addition, the individual KMO values for each CTQ were observed as follows: $K M O _ { I D } = 0 . 8 0 ; \ K M O _ { P } = 0 . 6 7 ;$ $K M O _ { N W } = 0 . 7 9$ and $K M O _ { F Z } = 0 . 6 7 ;$ being all higher than the reference value of 0.5 indicating that all CTQs have to remain in FA.

Considering that the original set of attributes is appropriate to the

Correlation analysis for ID, P, NW, and FZ.

<table><tr><td></td><td>ID</td><td>P</td><td>NW</td></tr><tr><td rowspan="2">P</td><td>0.593(1)</td><td></td><td></td></tr><tr><td>0.000(2)</td><td></td><td></td></tr><tr><td rowspan="2">NW</td><td>0.685(1)</td><td>0.614(1)</td><td></td></tr><tr><td>0.000(2)</td><td>0.000(2)</td><td></td></tr><tr><td rowspan="2">FZ</td><td>0.534(1)</td><td>0.890(1)</td><td>0.543(1)</td></tr><tr><td>0.000(2)</td><td>0.000(2)</td><td>0.000(2)</td></tr></table>

<sup>1</sup> Pearson correlation.  
2 p-Value.

## Table 8

Factor analysis with varimax rotation.

<table><tr><td colspan="5">Eigenanalysis of the correlation matrix</td></tr><tr><td>Eigenvalue</td><td>2.9351</td><td>0.6452</td><td>0.3149</td><td>0.1047</td></tr><tr><td>Proportion</td><td>0.734</td><td>0.161</td><td>0.079</td><td>0.026</td></tr><tr><td>Cumulative</td><td>0.734</td><td>0.895</td><td>0.974</td><td>1</td></tr><tr><td colspan="5">Rotated factor loadings and communalities</td></tr><tr><td>Variable</td><td>FA1</td><td>FA2</td><td colspan="2">Communality</td></tr><tr><td>FZ</td><td>0.934</td><td>0.285</td><td colspan="2">0.953</td></tr><tr><td>P</td><td>0.892</td><td>0.384</td><td colspan="2">0.943</td></tr><tr><td>ID</td><td>0.295</td><td>0.872</td><td colspan="2">0.848</td></tr><tr><td>NW</td><td>0.325</td><td>0.855</td><td colspan="2">0.837</td></tr><tr><td>Variance</td><td>1.8595</td><td>1.7208</td><td colspan="2">3.5804</td></tr><tr><td>% Var</td><td>0.465</td><td>0.43</td><td colspan="2">0.895</td></tr></table>

Bold data indicates significant at higher loadings within a factor.

FA application, we proceed to Step 3, which includes the application of the multivariate factor analysis strategy with extraction of the rotated factor scores using the varimax method (Eq. (22)). Analyzing the eigenvalues and the percentage of explanation presented in Table 8, it can be concluded according to the Kaiser's criterion [17] that two FAs adequately represent the four quality characteristics in question.

Considering the advantages of FA, mainly owing to rotating the axes for interpretation of latent information, it is possible to verify the rotated factor loadings and communalities as represented in Table 8. In this way, the correctness of grouping the quality responses to the factors is verified. FA1 provides better interpretation of the FZ and P responses, while FA2 results in a higher level of interpretation for ID and NW. To verify these results graphically, the hierarchical cluster analysis (HCA) was performed to group the responses with similar mathematical models using the Ward's linkage method to minimize the loss of information in connection of two groups. Fig. 4 presents the two-dimensional diagram generated to illustrate groupings and distinctions in levels. Through the HCA based on the correlation coeficients and the Ward's linkage method, the formation of two distinct groups can be verified confirming graphically the results presented in Table 8. After extraction of the rotated scores, we obtain the values of the rotated factor scores for FA1 and FA2, respectively, as presented in Table 9.

Table 6  
Observed measurements of the geometric characteristics in RSW.

<table><tr><td rowspan="2">n</td><td rowspan="2">a</td><td colspan="4">b = A</td><td colspan="4">b = B</td><td colspan="4">b = C</td><td colspan="4">b = D</td></tr><tr><td>ID</td><td>P</td><td>NW</td><td>FZ</td><td>ID</td><td>P</td><td>NW</td><td>FZ</td><td>ID</td><td>P</td><td>NW</td><td>FZ</td><td>ID</td><td>P</td><td>NW</td><td>FZ</td></tr><tr><td>1</td><td>1</td><td>0.1910</td><td>0.9884</td><td>4.2946</td><td>3.0447</td><td>0.2021</td><td>0.9779</td><td>4.3239</td><td>3.1238</td><td>0.2010</td><td>0.9486</td><td>4.3440</td><td>3.0030</td><td>0.1915</td><td>0.9687</td><td>4.3843</td><td>3.1041</td></tr><tr><td>2</td><td>1</td><td>0.2023</td><td>0.9778</td><td>4.2741</td><td>3.0633</td><td>0.1909</td><td>0.9775</td><td>4.3246</td><td>3.1335</td><td>0.1916</td><td>0.9578</td><td>4.3542</td><td>3.0551</td><td>0.1908</td><td>0.9875</td><td>4.3542</td><td>3.0842</td></tr><tr><td>3</td><td>1</td><td>0.1919</td><td>0.9582</td><td>4.3528</td><td>3.1132</td><td>0.2016</td><td>0.9680</td><td>4.2935</td><td>3.1539</td><td>0.1912</td><td>0.9470</td><td>4.3542</td><td>3.0940</td><td>0.1921</td><td>0.9861</td><td>4.3843</td><td>3.1736</td></tr><tr><td>1</td><td>2</td><td>0.2107</td><td>1.1164</td><td>4.6539</td><td>3.3439</td><td>0.2021</td><td>1.1387</td><td>4.7436</td><td>3.3327</td><td>0.2120</td><td>1.1166</td><td>4.7342</td><td>3.1939</td><td>0.2117</td><td>1.1188</td><td>4.7243</td><td>3.3041</td></tr><tr><td>2</td><td>2</td><td>0.2116</td><td>1.1084</td><td>4.7241</td><td>3.2931</td><td>0.2122</td><td>1.1382</td><td>4.7246</td><td>3.2942</td><td>0.2222</td><td>1.1172</td><td>4.7248</td><td>3.2929</td><td>0.2016</td><td>1.1372</td><td>4.8439</td><td>3.3633</td></tr><tr><td>3</td><td>2</td><td>0.2117</td><td>1.1269</td><td>4.7844</td><td>3.2439</td><td>0.2211</td><td>1.1268</td><td>4.7544</td><td>3.3430</td><td>0.2220</td><td>1.1160</td><td>4.7335</td><td>3.3532</td><td>0.2118</td><td>1.1264</td><td>4.8544</td><td>3.5238</td></tr><tr><td>1</td><td>3</td><td>0.1314</td><td>1.0261</td><td>3.5340</td><td>3.1137</td><td>0.1333</td><td>1.0568</td><td>3.6045</td><td>3.2244</td><td>0.1217</td><td>1.0177</td><td>3.6448</td><td>3.1933</td><td>0.1216</td><td>1.0485</td><td>3.6741</td><td>3.3441</td></tr><tr><td>2</td><td>3</td><td>0.1214</td><td>1.0178</td><td>3.6637</td><td>3.1236</td><td>0.1217</td><td>1.0567</td><td>3.6148</td><td>3.2545</td><td>0.1214</td><td>1.0178</td><td>3.6350</td><td>3.1240</td><td>0.1310</td><td>1.0578</td><td>3.6739</td><td>3.3336</td></tr><tr><td>3</td><td>3</td><td>0.1227</td><td>1.0175</td><td>3.6440</td><td>3.0937</td><td>0.1215</td><td>1.0476</td><td>3.5648</td><td>3.2543</td><td>0.1316</td><td>1.0191</td><td>3.6444</td><td>3.1938</td><td>0.1318</td><td>1.0463</td><td>3.6546</td><td>3.2943</td></tr><tr><td>1</td><td>4</td><td>0.0687</td><td>0.9772</td><td>3.5444</td><td>2.9646</td><td>0.0714</td><td>0.9875</td><td>3.5745</td><td>3.0345</td><td>0.0694</td><td>0.9689</td><td>3.5343</td><td>2.9141</td><td>0.0677</td><td>0.9679</td><td>3.5251</td><td>3.0332</td></tr><tr><td>2</td><td>4</td><td>0.0723</td><td>0.9867</td><td>3.5442</td><td>2.9338</td><td>0.0691</td><td>0.9874</td><td>3.5455</td><td>3.0131</td><td>0.0689</td><td>0.9668</td><td>3.5642</td><td>2.8739</td><td>0.0718</td><td>0.9782</td><td>3.5743</td><td>3.0433</td></tr><tr><td>3</td><td>4</td><td>0.0704</td><td>0.9669</td><td>3.5643</td><td>2.9744</td><td>0.0709</td><td>0.9562</td><td>3.5344</td><td>3.0035</td><td>0.0707</td><td>0.9581</td><td>3.5138</td><td>2.8436</td><td>0.0722</td><td>0.9673</td><td>3.5743</td><td>2.9937</td></tr><tr><td>1</td><td>5</td><td>0.2518</td><td>1.1886</td><td>4.5848</td><td>4.6337</td><td>0.2616</td><td>1.1762</td><td>4.5540</td><td>4.6328</td><td>0.2618</td><td>1.1878</td><td>4.6136</td><td>4.4831</td><td>0.2717</td><td>1.1977</td><td>4.5336</td><td>4.6432</td></tr><tr><td>2</td><td>5</td><td>0.2524</td><td>1.1996</td><td>4.5141</td><td>4.5236</td><td>0.2612</td><td>1.1978</td><td>4.5438</td><td>4.6330</td><td>0.2511</td><td>1.1971</td><td>4.6437</td><td>4.5832</td><td>0.2711</td><td>1.1994</td><td>4.5239</td><td>4.5930</td></tr><tr><td>3</td><td>5</td><td>0.2612</td><td>1.2094</td><td>4.5237</td><td>4.6748</td><td>0.2714</td><td>1.1779</td><td>4.5639</td><td>4.6933</td><td>0.2612</td><td>1.2069</td><td>4.5847</td><td>4.5741</td><td>0.2519</td><td>1.1980</td><td>4.6239</td><td>4.7732</td></tr><tr><td>1</td><td>6</td><td>0.2017</td><td>1.0976</td><td>3.8045</td><td>3.6249</td><td>0.1914</td><td>1.0966</td><td>3.7946</td><td>3.6530</td><td>0.2017</td><td>1.0894</td><td>3.8439</td><td>3.5027</td><td>0.2023</td><td>1.1084</td><td>3.8439</td><td>3.7240</td></tr><tr><td>2</td><td>6</td><td>0.1918</td><td>1.0978</td><td>3.7843</td><td>3.5538</td><td>0.1915</td><td>1.1072</td><td>3.8041</td><td>3.6644</td><td>0.2013</td><td>1.0987</td><td>3.8334</td><td>3.6148</td><td>0.2019</td><td>1.1166</td><td>3.8745</td><td>3.6634</td></tr><tr><td>3</td><td>6</td><td>0.2018</td><td>1.0871</td><td>3.7950</td><td>3.6343</td><td>0.2014</td><td>1.0881</td><td>3.8246</td><td>3.6344</td><td>0.2015</td><td>1.0787</td><td>3.8341</td><td>3.5838</td><td>0.1929</td><td>1.1076</td><td>3.8744</td><td>3.7335</td></tr><tr><td>1</td><td>7</td><td>0.1689</td><td>1.1588</td><td>4.7939</td><td>4.1835</td><td>0.1818</td><td>1.1470</td><td>4.8237</td><td>4.3037</td><td>0.1682</td><td>1.1472</td><td>4.8346</td><td>4.1940</td><td>0.1712</td><td>1.1682</td><td>4.8144</td><td>4.3026</td></tr><tr><td>2</td><td>7</td><td>0.1715</td><td>1.1674</td><td>4.8639</td><td>4.2538</td><td>0.1715</td><td>1.1788</td><td>4.8050</td><td>4.2833</td><td>0.1725</td><td>1.1373</td><td>4.8143</td><td>4.2229</td><td>0.1638</td><td>1.1670</td><td>4.9245</td><td>4.3935</td></tr><tr><td>3</td><td>7</td><td>0.1720</td><td>1.1587</td><td>4.7944</td><td>4.1723</td><td>0.1712</td><td>1.1371</td><td>4.8139</td><td>4.2938</td><td>0.1709</td><td>1.1393</td><td>4.8248</td><td>4.2442</td><td>0.1708</td><td>1.1581</td><td>4.8441</td><td>4.2937</td></tr><tr><td>1</td><td>8</td><td>0.1416</td><td>1.1385</td><td>4.0739</td><td>4.0146</td><td>0.1414</td><td>1.1578</td><td>4.1445</td><td>4.1830</td><td>0.1407</td><td>1.1265</td><td>4.1841</td><td>4.0026</td><td>0.1375</td><td>1.1280</td><td>4.1243</td><td>4.1437</td></tr><tr><td>2</td><td>8</td><td>0.1430</td><td>1.1380</td><td>4.1646</td><td>4.0435</td><td>0.1410</td><td>1.1487</td><td>4.1242</td><td>4.1437</td><td>0.1421</td><td>1.1374</td><td>4.1639</td><td>4.0643</td><td>0.1415</td><td>1.1582</td><td>4.1945</td><td>4.1532</td></tr><tr><td>3</td><td>8</td><td>0.1417</td><td>1.1278</td><td>4.0846</td><td>4.0541</td><td>0.1416</td><td>1.1379</td><td>4.1339</td><td>4.1137</td><td>0.1392</td><td>1.1377</td><td>4.0938</td><td>4.0343</td><td>0.1429</td><td>1.1486</td><td>4.1841</td><td>4.2033</td></tr></table>

All values were measured on the millimeter [mm] scale (except FZ: [mm<sup>2</sup>]).

Table 9  
![](/api/attachments/MKSHM69V/fulltext/images/23509117821e58ba340d3911ac04d1dc79924ca425049873f5ee139903fe10e3.jpg)  
Fig. 4. Clusters of quality characteristics and rotated factor scores.

After extraction of the rotated scores, the variation components of the study need to be estimated for each of the factors as presented in Step 4. From the analysis of variance of each FA (Eqs. (23) and (24)), it is possible to verify that the interaction term is not significant for FA2 with p-value equal to 0.496. However, FA1 provides a significant interaction term (p-value equal to 0.016). Fig. 5 shows the interaction plot for FA1 and FA2. Thereby, based on the results provided in Table 10 it is possible to verify the analysis of variance with the interaction term for FA1; and without the interaction term for FA2 (Table 11).

From this analysis, it is possible to verify that the operators do not present statistically significant diferences in their measurements (for both factors). After this verification, it is possible to calculate the multivariate indicators (Step 5). Table 12 represents the contribution of the measurement system to both factors. For FA1, it can be seen that the value of $\% R \& R _ { m }$ is equal to 14.61, and $n d c _ { m }$ is equal to 9. However, for FA2, the value of %R&R is 7.67, and ndc is equal to 18.

Given the obtained results, it can be verified that the characteristic FZ and P represented by FA1 are classified as marginal, while the characteristics ID and NW can be classified as acceptable. This step is important, as it shows that the method provides adequate separation of the responses with greater variability and the response with lower variability, i.e., being able to properly classify attributes according to their respective classification criterion. This allows verifying correctly, which responses contributed at the greatest extent to the measurement error without disregarding the variance-covariance structure allowing for the accurate analysis for diferent groups. In addition, it allows performing the data quality analysis to exclude information with high variability from being carried forward, which could result in the erroneous decision–making outcome.

To verify the correctness of the multivariate measurement system assessment, we calculate the confidence ellipsoids considering a 95% confidence interval for the analysis. Considering Eq. (27) presented above, it is possible to visually analyze the behavior of variability of the parts/DMUs through the confidence regions of the means and the data according to the two-dimensional structure, as shown in Fig. 6.

Fig. 6 illustrates the confidence ellipsoids for FA1 and FA2, in this figure, it can be seen that FA1 provides greater variability in data presenting the overlapping ellipsoids, which indicates the confounding in the analysis results. This confirms that the variability in the attributes does not allow the system to identify more distinct categories, i.e., it impairs the separability of information and may lead to the erroneous decision–making outcome. However, considering FA2, the ellipses

Rotated factor scores for the GR&R study.

<table><tr><td rowspan="2">n</td><td rowspan="2">a</td><td colspan="2">b=A</td><td colspan="2">b=B</td><td colspan="2">b=C</td><td colspan="2">b=D</td></tr><tr><td>FA1</td><td>FA2</td><td>FA1</td><td>FA2</td><td>FA1</td><td>FA2</td><td>FA1</td><td>FA2</td></tr><tr><td>1</td><td>1</td><td>-1.5508</td><td>0.8548</td><td>-1.5989</td><td>1.0127</td><td>-1.9563</td><td>1.1452</td><td>-1.6673</td><td>0.9938</td></tr><tr><td>2</td><td>1</td><td>-1.6483</td><td>0.9771</td><td>-1.5385</td><td>0.8726</td><td>-1.7897</td><td>0.9999</td><td>-1.5379</td><td>0.9161</td></tr><tr><td>3</td><td>1</td><td>-1.7193</td><td>0.9722</td><td>-1.6182</td><td>0.9701</td><td>-1.8199</td><td>0.9976</td><td>-1.4630</td><td>0.9319</td></tr><tr><td>1</td><td>2</td><td>-0.5377</td><td>1.1824</td><td>-0.3923</td><td>1.1606</td><td>-0.7565</td><td>1.3818</td><td>-0.6050</td><td>1.3058</td></tr><tr><td>2</td><td>2</td><td>-0.6923</td><td>1.3306</td><td>-0.4794</td><td>1.2782</td><td>-0.6789</td><td>1.4437</td><td>-0.4119</td><td>1.2795</td></tr><tr><td>3</td><td>2</td><td>-0.6457</td><td>1.4014</td><td>-0.5596</td><td>1.4267</td><td>-0.6197</td><td>1.4258</td><td>-0.3535</td><td>1.3612</td></tr><tr><td>1</td><td>3</td><td>-0.5629</td><td>-1.0246</td><td>-0.2536</td><td>-1.0213</td><td>-0.5366</td><td>-1.0142</td><td>-0.1508</td><td>-1.1117</td></tr><tr><td>2</td><td>3</td><td>-0.6253</td><td>-0.9579</td><td>-0.1697</td><td>-1.1638</td><td>-0.6114</td><td>-0.9973</td><td>-0.1399</td><td>-1.0104</td></tr><tr><td>3</td><td>3</td><td>-0.6595</td><td>-0.9535</td><td>-0.2110</td><td>-1.2163</td><td>-0.5719</td><td>-0.8967</td><td>-0.2636</td><td>-0.9845</td></tr><tr><td>1</td><td>4</td><td>-0.8030</td><td>-1.6059</td><td>-0.6733</td><td>-1.5869</td><td>-0.9206</td><td>-1.5696</td><td>-0.7755</td><td>-1.6597</td></tr><tr><td>2</td><td>4</td><td>-0.7875</td><td>-1.5660</td><td>-0.6748</td><td>-1.6440</td><td>-0.9948</td><td>-1.5108</td><td>-0.7317</td><td>-1.5680</td></tr><tr><td>3</td><td>4</td><td>-0.8829</td><td>-1.5421</td><td>-0.9140</td><td>-1.5697</td><td>-1.0778</td><td>-1.5252</td><td>-0.8704</td><td>-1.5167</td></tr><tr><td>1</td><td>5</td><td>1.3399</td><td>0.8094</td><td>1.2183</td><td>0.9125</td><td>1.0969</td><td>1.0471</td><td>1.3479</td><td>0.9599</td></tr><tr><td>2</td><td>5</td><td>1.3200</td><td>0.7523</td><td>1.3808</td><td>0.8502</td><td>1.3173</td><td>0.8892</td><td>1.3084</td><td>0.9607</td></tr><tr><td>3</td><td>5</td><td>1.5229</td><td>0.7788</td><td>1.2513</td><td>1.0128</td><td>1.3578</td><td>0.9169</td><td>1.5528</td><td>0.7764</td></tr><tr><td>1</td><td>6</td><td>0.0984</td><td>-0.1903</td><td>0.1769</td><td>-0.3417</td><td>-0.1229</td><td>-0.0596</td><td>0.2714</td><td>-0.1996</td></tr><tr><td>2</td><td>6</td><td>0.0718</td><td>-0.3044</td><td>0.2617</td><td>-0.3544</td><td>0.0827</td><td>-0.1529</td><td>0.2467</td><td>-0.1493</td></tr><tr><td>3</td><td>6</td><td>0.0378</td><td>-0.1856</td><td>0.0331</td><td>-0.1520</td><td>-0.0991</td><td>-0.0940</td><td>0.3063</td><td>-0.2760</td></tr><tr><td>1</td><td>7</td><td>0.8841</td><td>0.3628</td><td>0.8663</td><td>0.5258</td><td>0.7971</td><td>0.4280</td><td>1.0715</td><td>0.3413</td></tr><tr><td>2</td><td>7</td><td>0.9837</td><td>0.4384</td><td>1.1282</td><td>0.3204</td><td>0.7492</td><td>0.4585</td><td>1.1526</td><td>0.3589</td></tr><tr><td>3</td><td>7</td><td>0.8555</td><td>0.4072</td><td>0.8374</td><td>0.4075</td><td>0.7912</td><td>0.4388</td><td>0.9762</td><td>0.4018</td></tr><tr><td>1</td><td>8</td><td>1.0048</td><td>-0.8318</td><td>1.3096</td><td>-0.8596</td><td>0.8567</td><td>-0.6621</td><td>1.0765</td><td>-0.8557</td></tr><tr><td>2</td><td>8</td><td>0.9861</td><td>-0.7039</td><td>1.2093</td><td>-0.8546</td><td>1.0108</td><td>-0.7249</td><td>1.2535</td><td>-0.7761</td></tr><tr><td>3</td><td>8</td><td>0.9687</td><td>-0.8140</td><td>1.0889</td><td>-0.7975</td><td>1.0241</td><td>-0.8421</td><td>1.2417</td><td>-0.7786</td></tr></table>

![](/api/attachments/MKSHM69V/fulltext/images/e2f3eb3d3bf338ba4f255bcb9c17f6e8b798a43b6312825231f3722926971b64.jpg)

![](/api/attachments/MKSHM69V/fulltext/images/60545c3451554bbca7e8d67998a94e4a402e4814132a660d3f7f674c174c10a9.jpg)  
Fig. 5. Interaction plot for (a) FA1 and (b) FA2.

Table 10  
Two-way analysis of variance with interaction for FA1.

<table><tr><td>Source</td><td>DF</td><td>SS</td><td>MS</td><td>F</td><td>P</td></tr><tr><td>Parts</td><td>7</td><td>93.1317</td><td>13.3045</td><td>803.087</td><td>0.000</td></tr><tr><td>Operators</td><td>3</td><td>0.9998</td><td>0.3333</td><td>20.116</td><td>0.000</td></tr><tr><td>Parts × operators</td><td>21</td><td>0.3479</td><td>0.0166</td><td>2.037</td><td>0.016</td></tr><tr><td>Repeatability</td><td>64</td><td>0.5206</td><td>0.0081</td><td></td><td></td></tr><tr><td>Total</td><td>95</td><td>95.0000</td><td></td><td></td><td></td></tr></table>

Bold data indicates not significant interaction.

Table 11  
Two-way analysis of variance without interaction for FA2.

<table><tr><td>Source</td><td>DF</td><td>SS</td><td>MS</td><td>F</td><td>P</td></tr><tr><td>Parts</td><td>7</td><td>94.4416</td><td>13.4917</td><td>2707.86</td><td>0.000</td></tr><tr><td>Operators</td><td>3</td><td>0.1349</td><td>0.045</td><td>9.03</td><td>0.000</td></tr><tr><td>Repeatability</td><td>85</td><td>0.4235</td><td>0.005</td><td></td><td></td></tr><tr><td>Total</td><td>95</td><td>95.0000</td><td></td><td></td><td></td></tr></table>

Table 12  
Variance component contribution for GR&R .

<table><tr><td rowspan="2">Source</td><td colspan="2">FA1</td><td colspan="2">FA2</td></tr><tr><td>σ</td><td>%Study var</td><td>σ</td><td>%Study var</td></tr><tr><td> $σ_{GR&R}$ </td><td>0.15537</td><td>14.61</td><td>0.08154</td><td>7.67</td></tr><tr><td> $σ_{repeatability}$ </td><td>0.09019</td><td>8.48</td><td>0.07059</td><td>6.64</td></tr><tr><td> $σ_{reproducibility}$ </td><td>0.12652</td><td>11.89</td><td>0.04082</td><td>3.84</td></tr><tr><td> $σ_{operators}$ </td><td>0.11487</td><td>10.8</td><td>0.04082</td><td>3.84</td></tr><tr><td> $σ_{part × operators}$ </td><td>0.05302</td><td>4.98</td><td>-</td><td>-</td></tr><tr><td> $σ_{part-to-part}$ </td><td>1.0523</td><td>98.93</td><td>1.06014</td><td>99.71</td></tr><tr><td> $σ_T$ </td><td>1.06371</td><td>100</td><td>1.06327</td><td>100</td></tr><tr><td>ndc</td><td>9</td><td></td><td>18</td><td></td></tr></table>

present the diferent behavior with less variability and without overlapping ellipsoids indicating the high quality of the data used in the analysis of these attributes. The behavior of the ellipsoids confirms the results of the analysis based on $\mathrm { G R } \& \mathrm { R } _ { \mathrm { m } }$ indicating that FA1 (Fig. 6(a)) presents greater variability and needs to be classified as marginal. From Fig. 6(b), it can be seen that the ellipses can be easily identified, as they do not present overlaps indicating the smaller variability of the data represented by FA2.

To confirm the importance of the method, we also analyzed the intervals of the Bonferroni bilateral limits. Table 13 provides the description of the values of the multivariate intervals along with the Bonferroni intervals. Figs. 7 and 8 graphically show the Bonferroni intervals for each of the FA1 and FA2 parts, respectively. Although the study of FA1 presents greater variability (being classified as marginal), it is possible to verify that the ellipsoids respect the limits of the Bonferroni bilateral intervals.

## 4.3. Comparison with other GR&R methods

To represent the benefits of the proposed FA method with rotated factor scores for data quality assessment in the uncertainty and variability analysis, other methods discussed in the literature are applied to the same numerical example: the univariate ANOVA method and the multivariate WPC method. Considering the ANOVA method, we evaluate each of the data quality characteristics separately. This method was chosen because it is widely used in the literature. In particular, it was applied in studies [2,16] aimed to evaluate variability of measurement systems, i.e., to evaluate the quality of the data to be used for the purposes such as multiobjective optimization. As an example of the multivariate approach, we chose the WPC method proposed by Peruchi et al. in [40], where the authors state that this method is superior to other multivariate methods such as MANOVA and PCA. In addition, the same authors afirm that the WPC method is a better choice to evaluate the data that present significant correlation comparing to the ANOVA method. Finally, the proposed method is compared to the FA approach with unrotated factor scores (without rotating the axes using the varimax method)

## 4.3.1. ANOVA

Applying the univariate ANOVA method, it is possible to verify that only the quality characteristics P presents a significant interaction term (p-value equal to 0.003). Table 14 presents the variation and classification components of the measurement system for each of the quality responses. It is possible to verify that the NW and ID responses provide the acceptable values in the variation contribution, both are classified as acceptable. However, the answers P and FZ provide the higher variance contribution values classifying them as marginal according to the classification criteria established by the AIAG [1].

As the same measuring device is used to analyze all attributes, in our case, the geometric characteristics of the same weld point, the more detailed analysis shows that these responses are highly correlated (see Table 7). Therefore, evaluating the measurement system considering independent responses may not be the most appropriate method [3,17,40], which may lead to erroneous decision-making outcome. In this way, the example also includes the comparison with the WPC method, which represents the geometric characteristics of the welded point in a single vector and uses the multivariate approach to evaluate the data quality.

![](/api/attachments/MKSHM69V/fulltext/images/ad021bd796a7acaea1592ad36b8b7880937aea76ded90621357c0ab609b0226b.jpg)

![](/api/attachments/MKSHM69V/fulltext/images/cb05d4b756edb5e06b62b15f5c4adddab17495fca5d7e6af98931d072fde6056.jpg)  
Fig. 6. 95% confidence ellipsoids (mean and data) for (a) FA1 and (b) FA2.

Table 13  
Bonferroni bilateral limits for quality characteristics.

<table><tr><td rowspan="3">Part</td><td colspan="5">FA1</td><td colspan="5">FA2</td></tr><tr><td colspan="5">Penetration (P)</td><td colspan="5">Indentation depth (ID)</td></tr><tr><td>Mean</td><td>LB</td><td>UB</td><td> $LB_{Bonferroni}$ </td><td> $UB_{Bonferroni}$ </td><td>Mean</td><td>LB</td><td>UB</td><td> $LB_{Bonferroni}$ </td><td> $UB_{Bonferroni}$ </td></tr><tr><td>1</td><td>0.97029</td><td>0.96655</td><td>0.97403</td><td>0.96648</td><td>0.97410</td><td>0.19483</td><td>0.19352</td><td>0.19614</td><td>0.19350</td><td>0.19616</td></tr><tr><td>2</td><td>1.12397</td><td>1.12141</td><td>1.12653</td><td>1.12136</td><td>1.12658</td><td>0.21256</td><td>0.21086</td><td>0.21426</td><td>0.21082</td><td>0.21430</td></tr><tr><td>3</td><td>1.03581</td><td>1.03129</td><td>1.04033</td><td>1.03120</td><td>1.04042</td><td>0.12592</td><td>0.12458</td><td>0.12726</td><td>0.12456</td><td>0.12728</td></tr><tr><td>4</td><td>0.97242</td><td>0.96964</td><td>0.97520</td><td>0.96959</td><td>0.97525</td><td>0.07029</td><td>0.06991</td><td>0.07068</td><td>0.06990</td><td>0.07068</td></tr><tr><td>5</td><td>1.19470</td><td>1.19208</td><td>1.19732</td><td>1.19204</td><td>1.19736</td><td>0.26070</td><td>0.25872</td><td>0.26268</td><td>0.25868</td><td>0.26272</td></tr><tr><td>6</td><td>1.09782</td><td>1.09505</td><td>1.10059</td><td>1.09500</td><td>1.10064</td><td>0.19843</td><td>0.19719</td><td>0.19967</td><td>0.19717</td><td>0.19969</td></tr><tr><td>7</td><td>1.15541</td><td>1.15190</td><td>1.15892</td><td>1.15184</td><td>1.15898</td><td>0.17119</td><td>0.17015</td><td>0.17223</td><td>0.17013</td><td>0.17225</td></tr><tr><td>8</td><td>1.14043</td><td>1.13766</td><td>1.14320</td><td>1.13761</td><td>1.14325</td><td>0.14118</td><td>0.14079</td><td>0.14157</td><td>0.14079</td><td>0.14158</td></tr><tr><td rowspan="3">Part</td><td colspan="5">FA1</td><td colspan="5">FA2</td></tr><tr><td colspan="5">Fusion zone (FZ)</td><td colspan="5">Nugget width (NW)</td></tr><tr><td>Mean</td><td>LB</td><td>UB</td><td> $LB_{Bonferroni}$ </td><td> $UB_{Bonferroni}$ </td><td>Mean</td><td>LB</td><td>UB</td><td> $LB_{Bonferroni}$ </td><td> $UB_{Bonferroni}$ </td></tr><tr><td>1</td><td>3.0955</td><td>3.0831</td><td>3.1079</td><td>3.0828</td><td>3.1082</td><td>4.3366</td><td>4.3276</td><td>4.3456</td><td>4.3275</td><td>4.3457</td></tr><tr><td>2</td><td>3.3235</td><td>3.3032</td><td>3.3438</td><td>3.3028</td><td>3.3442</td><td>4.7500</td><td>4.7360</td><td>4.7640</td><td>4.7357</td><td>4.7643</td></tr><tr><td>3</td><td>3.2123</td><td>3.1902</td><td>3.2344</td><td>3.1898</td><td>3.2348</td><td>3.6294</td><td>3.6183</td><td>3.6405</td><td>3.6181</td><td>3.6407</td></tr><tr><td>4</td><td>2.9688</td><td>2.9522</td><td>2.9854</td><td>2.9519</td><td>2.9857</td><td>3.5494</td><td>3.5442</td><td>3.5547</td><td>3.5441</td><td>3.5548</td></tr><tr><td>5</td><td>4.6201</td><td>4.6005</td><td>4.6397</td><td>4.6001</td><td>4.6401</td><td>4.5673</td><td>4.5564</td><td>4.5782</td><td>4.5562</td><td>4.5784</td></tr><tr><td>6</td><td>3.6323</td><td>3.6157</td><td>3.6489</td><td>3.6154</td><td>3.6492</td><td>3.8259</td><td>3.8182</td><td>3.8337</td><td>3.8181</td><td>3.8338</td></tr><tr><td>7</td><td>4.2618</td><td>4.2457</td><td>4.2779</td><td>4.2454</td><td>4.2782</td><td>4.8293</td><td>4.8201</td><td>4.8385</td><td>4.8199</td><td>4.8387</td></tr><tr><td>8</td><td>4.0962</td><td>4.0787</td><td>4.1137</td><td>4.0783</td><td>4.1141</td><td>4.1392</td><td>4.1288</td><td>4.1496</td><td>4.1286</td><td>4.1498</td></tr></table>

## 4.3.2. WPC

Given the significant correlation of the data, the WPC method (detailed in [40]) was applied initially creating a WPC vector as described in Eq. (29) and defining the component scores weighted by their respective eigenvalues. The supplementary material (Appendix B) provides the scores of each component, in addition to the WPC vector

![](/api/attachments/MKSHM69V/fulltext/images/260ab2f0ec8c704ded195361b22023e31c7135e4170d33c1b689f9e918c8d6c7.jpg)

![](/api/attachments/MKSHM69V/fulltext/images/e8cfb29d73d5770875b2b11b32a1a3fbfcb0bebbacf971360ea8d83ea305728e.jpg)

![](/api/attachments/MKSHM69V/fulltext/images/3269c13bd6aca0dc83bbc3dce9f0157a02c00569d42cf964ab794562adc466a0.jpg)

![](/api/attachments/MKSHM69V/fulltext/images/014d3835c3ce99b2940645db07f9af5980591025397c2ee601882977584a87e6.jpg)

![](/api/attachments/MKSHM69V/fulltext/images/e977aab906ddf63e07c628d5851ac6a03327d68e6421f2ce2d361aaa9725504b.jpg)

![](/api/attachments/MKSHM69V/fulltext/images/9bdab3f23e6f827b054bb89f026edc2f0e7731b5872d2d27eea73aadf96fbae1.jpg)

![](/api/attachments/MKSHM69V/fulltext/images/42e7c98b97d9245f7f4e6ed113fb994984efdeaa12853b5a560c36a85b56f7ed.jpg)

![](/api/attachments/MKSHM69V/fulltext/images/2aed923e0ef1d516685fa9365c6c63d19b3dc6c2c63b9dcfe7ceb168c469a845.jpg)  
Fig. 7. 95% confidence ellipsoids of means applying Bonferroni bilateral limits for FA1.

values.

$$
\begin{array}{r l} \mathbf {W P C} & = \sum_ {i = 1} ^ {q} [ \lambda_ {i} (\mathbf {P C _ {i}}) ] \\ & = 2. 9 3 5 1 \mathbf {P C _ {1}} + 0. 6 4 5 2 \mathbf {P C _ {2}} + 0. 3 1 4 9 \mathbf {P C _ {3}} + 0. 1 0 4 7 \mathbf {P C _ {4}} \end{array}\tag{29}
$$

The analysis of variance indicates that the interaction term was insignificant with p-value equal to 0.142. From Table 14, it can be seen that the method provided a contribution percentage in variability of %R $\& R = 7 . 2 3$ classifying it as acceptable. This result shows that the WPC method neglects the characteristics that present greater variability camouflaging the data of low quality. Failure to properly identify the data with high variability results in the inadequate multicriteria decision–- making outcome. This result infers that the WPC approach may not be the most appropriate choice for analyzing several quality attributes lacking robust evaluation and impairing decision-making for variability assessment. In addition, similarly as in the ANOVA approach, the WPC method does not allow for reduction in the data dimensionality (even though this is one of the main characteristics of the PCA strategy), as it considers all the principal components to create the WPC vector. Fig. 9 presents the HCA obtained through the Ward linkage method for the major components along with the original responses illustrating similarity of their behavior. It can be seen that only the first PC has considerable similarity with the quality characteristics, while the other components (also used to create the WPC vector) do not present an adequate level of similarity.

## 4.3.3. Unrotated factor scores

After comparing the proposed method with other alternative approaches (ANOVA and WPC), we assess it in comparison to the method without the rotation factor scores. Applying the method implying unrotation of the axes, we can see in Fig. 10 that the clusters of the quality attributes show diferent behavior comparing to the method with varimax rotation. The unrotated method presents a cluster inversion of the responses. In this approach, FA1 represents most interpretations of the original data, while FA2 does not present a considerable level of similarity.

Through the analysis of variance, we can verify that FA1 and FA2 present a non-significant interaction term (p-value equal to 0.051 and

Table 14  
![](/api/attachments/MKSHM69V/fulltext/images/9fd7420067f9f089181a04ee8932b9431d1ec3214dbf54605e26728e093f9d02.jpg)

![](/api/attachments/MKSHM69V/fulltext/images/ef24cd03c419e9d716be8f0c2f8c9936db50ea94a9b43e584f54219d20924dd3.jpg)

![](/api/attachments/MKSHM69V/fulltext/images/b3261baeb85469e5ae681f102a86b4b4875962187457734ad5faf9799b1b556c.jpg)

![](/api/attachments/MKSHM69V/fulltext/images/ce29748f205d2b6a9f56676dd17cc76bf7198b29490a7da25c6f142a8e6fa271.jpg)

![](/api/attachments/MKSHM69V/fulltext/images/0104671cec68ef2c72a4fa504ffc2828e69511a7d537bf1648976c036f553ebb.jpg)

![](/api/attachments/MKSHM69V/fulltext/images/9279f00fb372e2b06bd5793aa899206332e7a64126c2b19f127349390c91ad2d.jpg)

![](/api/attachments/MKSHM69V/fulltext/images/6c5f87a4a6dd0a74a9e76d0eb2a07e08a00fd9bd06294abef2ce267c279c4fb0.jpg)

![](/api/attachments/MKSHM69V/fulltext/images/dedf62d73b61dcda32be97d7beb9cfac5b2a397aa29e9c98d21c727e7226f069.jpg)  
Fig. 8. 95% confidence ellipsoids of means applying Bonferroni bilateral limits for FA2.

Classification through ANOVA, WPC, and FA (unrotated) methods.

<table><tr><td rowspan="2"></td><td colspan="4">ANOVA</td><td rowspan="2">WPC</td><td colspan="2">FA (unrotated)</td></tr><tr><td>ID</td><td>P</td><td>NW</td><td>FZ</td><td>FA1</td><td>FA2</td></tr><tr><td> $\sigma_{\text{repeatability}}$ </td><td>0.0051</td><td>0.0093</td><td>0.0338</td><td>0.0466</td><td>0.2734</td><td>0.0590</td><td>0.1083</td></tr><tr><td> $\sigma_{\text{reproducibility}}$ </td><td>0.0000</td><td>0.0094</td><td>0.0219</td><td>0.0579</td><td>0.2764</td><td>0.0634</td><td>0.1054</td></tr><tr><td> $\sigma_T$ </td><td>0.0589</td><td>0.0854</td><td>0.5007</td><td>0.6120</td><td>5.3795</td><td>1.0635</td><td>1.0635</td></tr><tr><td>%R&amp;R</td><td>8.63</td><td>15.52</td><td>8.04</td><td>12.15</td><td>7.23</td><td>8.14</td><td>14.21</td></tr><tr><td>ndc</td><td>16</td><td>8</td><td>17</td><td>11</td><td>19</td><td>17</td><td>9</td></tr></table>

$0 . 0 7 5 ,$ respectively). Estimating the variation components and calculating the multivariate indicators, we find (in Table 14) that FA1 and FA2 have values of %R&R equal to 8.14 and 14.21, respectively. This result indicates that FA1 is classified as acceptable; however, the first factor represents a large amount of the interpretation of the quality attributes resulting in confounding in the interpretation of these data. This result may cause undesirable outcome of decision-making classifying this analysis as inadequate.

![](/api/attachments/MKSHM69V/fulltext/images/98a8339fcc61c9950347cb5d4b31c18a01566207979f424d95dabc153b3d7020.jpg)  
Fig. 9. Clusters of quality characteristics and principal component scores.

![](/api/attachments/MKSHM69V/fulltext/images/6188aa056ad0fb4d4efe9aaf6307d78aeb1e53442e7aa695305345d350f2fb68.jpg)

This can be explained by absence of rotation of the axes, consequently, FA1 and FA2 could not adequately explain the variability of the quality attributes resulting in inadequate interpretation of the latent data and failing to separate the groups appropriately.

## 5. Conclusions

This study aimed to propose a new decision support strategy for data quality assessment via a multivariate measurement system using the gage repeatability and reproducibility study (GR&R). Thus, the present study focuses on a new multivariate method based on rotated factor scores and confidence ellipsoids. Furthermore, it seeks to improve the decision support process by analyzing the quality of massive correlated data. To confirm the eficiency of the proposed method, it was applied to the attributes of a real RSW process, that is, the evaluation of the geometric characteristics of the weld point. In addition, we compared our results with other methods used in the literature such as ANOVA and WPC. Furthermore, we also compared it with the results of FA with unrotated factor scores. The following conclusions were derived from the application of this strategy:

The method presents a multivariate option that allows the interpretation of latent information of data with multiple correlation. Furthermore, it allows for the analysis of data quality in an acceptable manner. In addition to reducing the dimensionality of the data to be analyzed, it allows more efective decision-making through the use of undistorted information.

The behavior of the method in a real case was assessed through the experimental application and the behavior of the correlated data was analyzed. Moreover, satisfactory results were achieved through the grouping of the quality attributes to be considered in the data quality estimation. Using this approach, one can classify the mea surement system for each cluster in an appropriate manner.

Comparison with alternative methods showed that the univariate

ANOVA method was unable to perform lean assessment for the measurement process. Moreover, it neglects the variance-covariance structure of the data. The multivariate WPC method provided a single but inadequate evaluation by classifying the whole data quality as acceptable. In addition, 50% of the quality attributes having high variability in the measurements were classified as marginal. In other words, both methods showed unsatisfactory re sults which could impair the decision-making process.

By analyzing the results of the FA method without the varimax rotation, we observed that the interpretation of the data was confusing. It was noted that the clusters presented inversions promoting a divergent interpretation without the rotation of the axes, which could lead to improper decision-making.

• We can verify the multivariate behavior of the data through the use of confidence ellipsoids, thereby illustrating the presence of variability in the measurements of each group created by the proposed method. Furthermore, FA2 achieved superior discriminatory power with nonoverlapping ellipsoids. It is important to note that for both factors, the Bonferroni bilateral limits were taken into consideration.

Finally, we can infer that ellipsoid visualization techniques coupled with the MSA approach employing rotated factor scores can be deemed as useful and appropriate for assessing the data quality to be used in the multicriteria decision-making processes. In addition, the proposed method is confirmed to be a useful alternative for the analysis of possibly skewed data and can be applied in various fields for decision-making support.

## Acknowledgments

The authors would like to express their gratitude to the following Brazilian institutes: FAPEMIG (project number APQ-00385-18), CAPES, and CNPq (project number 303586/2015-0 and 409318/2017-5) for their support to this research.

## Appendix A. Confidence ellipsoids

According to Ferreira [32], the theorem for concentration ellipsoids, in which a random vector X is $\pmb { X } \in \Re ^ { p } \mathrm { : }$ , which presents a certain normal multivariate distribution with mean $\pmb { \mu } ,$ covariance matrix $\Sigma ,$ and density $f _ { \mathbf { X } } ( \mathbf { x } )$ )is formulated as follows:

$$
(\mathbf {X} - \boldsymbol {\mu}) ^ {T} \boldsymbol {\Sigma} ^ {- 1} (\mathbf {X} - \boldsymbol {\mu})\tag{A.1}
$$

This equation shows the chi-square distribution with p degrees of freedom, given by ${ \chi _ { p } } ^ { 2 } ,$ , and the region defining the concentration ellipsoid 100(1 – α)% given by Eq. (A.2).

$$
(\mathbf {X} - \boldsymbol {\mu}) ^ {T} \boldsymbol {\Sigma} ^ {- 1} (\mathbf {X} - \boldsymbol {\mu}) \leq \chi_ {\alpha , p} ^ {2}\tag{A.2}
$$

For this, in $\chi _ { \alpha , \ p } { } ^ { 2 } , p$ defines the upper quantile 100α% of the chi-square distribution with $\nu = p$ degrees of freedom obtained by probabilistic P $( { \chi _ { p } } ^ { 2 } > { \chi _ { \alpha , p } } ^ { 2 } ) = \alpha .$

Proof:

Considering the matrix equivalence $\Sigma ^ { - 1 } = \Sigma ^ { - 1 / 2 } \Sigma ^ { - 1 / 2 }$ , the Eq. (A.1) can be defined by Eq. (A.3).

$$
(\mathbf {X} - \boldsymbol {\mu}) ^ {T} \boldsymbol {\Sigma} ^ {- 1} (\mathbf {X} - \boldsymbol {\mu}) = (\mathbf {X} - \boldsymbol {\mu}) ^ {T} \boldsymbol {\Sigma} ^ {- 1 / 2} \boldsymbol {\Sigma} ^ {- 1 / 2} (\mathbf {X} - \boldsymbol {\mu})\tag{A.3}
$$

Given the linear transformation $\pmb { Z } = \pmb { \Sigma } ^ { - 1 / 2 } ( \pmb { X } - \pmb { \mu } ) = [ Z _ { 1 } , Z _ { 2 } , . . . , Z _ { p } ] ^ { \mathrm { T } }$ , we have:

$$
(\mathbf {X} - \boldsymbol {\mu}) ^ {T} \pmb {\Sigma} ^ {- 1} (\mathbf {X} - \boldsymbol {\mu}) = \mathbf {Z} ^ {T} \mathbf {Z} = \sum_ {i = 1} ^ {p} Z _ {i} ^ {2}\tag{A.4}
$$

Let X be a vector that is normal multivariate according to Ferreira [32], Z provides a multivariate normal distribution with mean and variance represented by:

$$
\boldsymbol {\mu} _ {\mathbf {z}} = E \left[ \boldsymbol {\Sigma} ^ {- 1 / 2} (\mathbf {X} - \boldsymbol {\mu}) \right] = 0
$$

and

(A.5)

$$
\begin{array}{r l} & {\pmb {\Sigma_ {z}} = E (\mathbf {Z} - \pmb {\mu_ {z}}) (\mathbf {Z} - \pmb {\mu_ {z}}) ^ {T}} \\ & {\quad = E (\mathbf {Z Z} ^ {T})} \\ & {\quad = E [ \pmb {\Sigma} ^ {- 1 / 2} (\mathbf {X} - \pmb {\mu}) (\mathbf {X} - \pmb {\mu}) ^ {T} \pmb {\Sigma} ^ {- 1 / 2} ]} \\ & {\quad = \pmb {\Sigma} ^ {- 1 / 2} E (\mathbf {X} - \pmb {\mu}) (\mathbf {X} - \pmb {\mu}) ^ {T} \pmb {\Sigma} ^ {- 1 / 2}} \\ & {\quad = \pmb {\Sigma} ^ {- 1 / 2} \pmb {\Sigma} \pmb {\Sigma} ^ {- 1 / 2} = \mathbf {I}} \end{array}\tag{A.6}
$$

where I represents the identity.

In this way, it can be inferred that $Z _ { i } , \forall i = 1 , 2 , . . . , p$ is a normal variable with mean $\mu _ { i }$ equal to zero, and variance $\sigma _ { i i }$ equal to 1. According to Ferreira [32], $Z _ { 1 } , Z _ { 2 } , . . . , Z _ { p }$ are independently distributed, because $\sigma _ { i k }$ is equal to zero $\forall i , k = 1 , 2 , . . . , p$ with $i \neq k .$

Considering a variable H formed by the sum of the p standard-normal variables summed squared $H = \sum _ { i = 1 } ^ { p } Z _ { i } ^ { 2 } = ( \mathbf { X } - { \boldsymbol { \mu } } ) ^ { T } \Sigma ^ { - 1 } ( \mathbf { X } - { \boldsymbol { \mu } } )$ , Ferreira in [32] states that it is necessary to show that H has the chi-square distribution with $\nu = p$ degrees of freedom. In this way, the joint density of the variables of the Z vector can be obtained according to Eq. (A.7).

$$
f _ {\mathbf {z}} (\mathbf {z}) = (2 \pi) ^ {- p / 2} \mathrm{exp} \biggl \{- \frac {1}{2} \mathbf {z} ^ {T} \mathbf {z} \biggr \}\tag{A.7}
$$

Therefore, the function that demonstrates moments of H is equal to:

$$
\begin{array}{r l} & m _ {H} = E (e ^ {t H}) = E (e ^ {t \mathbf {z} ^ {T} \mathbf {z}}) = \int_ {\Re^ {p}} (2 \pi) ^ {- p / 2} e ^ {t \mathbf {z} ^ {T} \mathbf {z}} \exp \biggl \{- \frac {1}{2} \mathbf {z} ^ {T} \mathbf {z} \biggr \} d \mathbf {z} \\ & \qquad = \int_ {\Re^ {p}} (2 \pi) ^ {- p / 2} \exp \biggl \{- \frac {1}{2} \mathbf {z} ^ {T} \mathbf {z} + t \mathbf {z} ^ {T} \mathbf {z} \biggr \} d \mathbf {z} \\ & \qquad = \int_ {\Re^ {p}} (2 \pi) ^ {- p / 2} \exp \biggl \{- \frac {1}{2} \mathbf {z} ^ {T} \mathbf {z} (1 - 2 t) \biggr \} d \mathbf {z} \\ & \qquad = \int_ {\Re^ {p}} (2 \pi) ^ {- p / 2} \exp \biggl \{- \frac {1}{2} (1 - 2 t) \sum_ {i = 1} ^ {p} z _ {i} ^ {2} \biggr \} d \mathbf {z}. \end{array}\tag{A.8}
$$

The multiple integral of Eq. (A.8) can be written as a product of integrals, such as Eq. (A.9).

$$
\begin{array}{l} m _ {H} (t) = \prod_ {i = 1} ^ {p} \int_ {- \infty} ^ {\infty} (2 \pi) ^ {- 1 / 2} \exp \left\{- \frac {1}{2} (1 - 2 t) z _ {i} ^ {2} \right\} d \mathbf {z} _ {i} \\ = \prod_ {i = 1} ^ {p} \frac {1}{\sqrt {1 - 2 t}} \int_ {- \infty} ^ {\infty} \frac {\sqrt {1 - 2 t}}{2 \pi} \exp \left\{- \frac {1}{2} (1 - 2 t) z _ {i} ^ {2} \right\} d \mathbf {z} _ {i} \end{array}\tag{A.9}
$$

As the integrand is equal to 1, we have:

$$
m _ {H} (t) = \prod_ {i = 1} ^ {p} \frac {1}{\sqrt {1 - 2 t}} = \left(\frac {1}{1 - 2 t}\right) ^ {p / 2}, \quad f o r t \leq \frac {1}{2}\tag{A.10}
$$

This function generates moments of the chi-square distribution with p– degrees of freedom [39] [46]. As the upper quantile $\chi _ { \alpha , { p } ^ { 2 } }$ of the chi square distribution, we have $P ( \chi _ { p } ^ { \ 2 } \leq \chi _ { \alpha , p } ^ { \ 2 } ) = 1 - \alpha .$ . Consequently, substituting ${ \chi _ { p } } ^ { 2 }$ for $( { \pmb X } - { \pmb \mu } ) ^ { \operatorname { T } } { \pmb \Sigma } ^ { - 1 } ( { \pmb X } - { \pmb \mu } )$ ) can be verified as per Eq. (A.11). which was indicated in Eq. (A.2).

$$
P (\chi_ {p} ^ {2} \leq \chi_ {\alpha , p} ^ {2}) = P [ (\mathbf {X} - \boldsymbol {\mu}) ^ {T} \boldsymbol {\Sigma} ^ {- 1} (\mathbf {X} - \boldsymbol {\mu}) \leq \chi_ {\alpha , p} ^ {2} ] = 1 - \alpha\tag{A.11}
$$

## Appendix B. Supplementary data

Supplementary data to this article can be found online at https://doi.org/10.1016/j.dss.2019.113173.

## References

[1] AIAG, Measurement Systems Analysis: Reference Manual, 4th ed., Automotive Industry Action Group, Detroid, MI, USA, 2010

[2] F.A. Almeida, G.F. Gomes, R.C. Sabioni, J.H.F. Gomes, V.R. Paula, A.P. Paiva, S.C. Costa, A gage study applied in shear test to identify variation causes from a resistance spot welding measurement system, Stroj. Vestn. J. Mech. Eng. 64 (2018) 621–631.https://doi org/10.5545/sv-ime 2018.5235

[3] F.A. Almeida, T.I. De Paula, R.R. Leite, G.F. Gomes, J.H.F. Gomes, A.P. Paiva, P.P. Balestrassi. A multivariate GR&R approach to variability evaluation of measuring instruments in resistance spot welding process, J. Manuf. Process. 36 (2018) 465–479, https://doi.org/10.1016/j.jmapro.2018.10.030.

[4] A. Al-Refaie, N. Bata, Evaluating measurement and process capabilities by GR&R with four quality measures, Measurement 43 (2010) 842–851, https://doi.org/10. 1016/LMEASUREMENT,2010.02.016

[5] O. Arazy, O. Nov, R. Patterson, L. Yeo, Information quality in wikipedia: the efects of group composition and task conflict, J. Manag. Inf. Syst. 27 (2011) 71–98, https://doi.org/10.2753/MIS0742-1222270403.

[6] G. Belinato, F.A. de Almeida, A.P. Paiva, J.H. de F. Gomes, P.P. Balestrassi, P.A.R.C. Rosa, A multivariate normal boundary intersection PCA-based approach to reduce dimensionality in optimization problems for LBM process, Eng. Comput. 35 (2019)1533–1544. https://doi.org/10.1007/s00366-018-0678-3.

[7] R.K. Burdick, C.M. Borror, D.C. Montgomery, A review of methods for measurement systems capability analysis, J. Oual. Technol. 35 (2003) 342–354, https://doi,org 10.1080/00224065 2003.11980232

[8] T. Cai, H. Wu, J. Qin, J. Qiao, Y. Yang, Y. Wu, D. Qiao, H. Xu, Y. Cao, In vitro evaluation by PCA and AHP of potential antidiabetic properties of lactic acid bac teria isolated from traditional fermented food, Lwt 115 (2019) 108455, , https:// doi.org/10.1016/i.lwt.2019.108455.

[9] M.C. Carnera, Selection of diagnostic techniques and instrumentation in a pre dictive maintenance program. A case study, Decis. Support. Syst. 38 (2005)

539–555, https://doi.org/10.1016/j.dss.2003.09.003.

[10] J. Colin, A. Martens, M. Vanhoucke, M. Wauters, A multivariate approach for top down project control using earned value management, Decis. Support. Syst. 79 (2015).65–76. https://doi.org/10.1016/LDSS.2015.08.002

[11] C. Combes, J. Azema, Clustering using principal component analysis applied to autonomy–disability of elderly people, Decis. Support. Syst. 55 (2013) 578–586, https://doi.org/10.1016/J.DSS.2012.10.016.

[12] A.B. Costello, J.W. Osborne, Best practices in exploratory factor analysis: four recommendations for getting the most from your analysis, Pract. Assess. Res. Eval. (2005) 1–9 (papers2://publication/uuid/256DEBAD-ECC4-4DC4-99FD-E67E4D567AEC).

[13] D.F. (Federal U. of L. Ferreira, Estatística Multivariada), 3th ed., UFLA, Lavras, 2018.

[14] S.. Darwish, S.. Al-Dekhial, Micro-hardness of spot welded (B.S. 1050) commercial aluminium as correlated with welding variables and strength attributes. J. Mater Process, Technol, 91 (1999) 43–51, https://doi,org/10.1016/S0924-0136(98)00414-2

[15] F.A. de Almeida, G.F. Gomes, V.R. De Paula, J.E. Corrêa, A.P. De Paiva, J.H. De Freitas Gomes, J.B. Turrioni, A weighted mean square error approach to the robust optimization of the surface roughness in an AISI 12L14 free-machining steel-turning process, Stroj. Vestnik/Journal Mech. Eng. 64 (2018) 147–156, https://doi.org/10. 5545/sv-ime.2017.4901

[16] F.A. de Almeida, J.H.F. Gomes, G.F. Gomes, E.L. Romão, P.P. Balestrassi, Variation causes analysis attributed to diferent metrological instruments to verify the geometric characteristics of a spot welding process, Soldag. e Insp. 23 (2018), https:/ doi.org/10.1590/0104-9224/SJ2304.05.

[17] F.A. de Almeida, G.F. Gomes, J.H.D. Gaudêncio, J.H. de F. Gomes, A.P. de Paiva, A new multivariate approach based on weighted factor scores and confidence ellipses to precision evaluation of textured fiber bobbins measurement system, Precis. Eng. 60 (2019) 520–534. https://doi,org/10.1016/J.PRECISIONENG,2019.09.010.

[18] J. De Mast, A. Trip, Gauge R&R studies for destructive measurements, J. Qual. Technol. 37 (2005) 40–49, https://doi.org/10.1080/00224065.2005.11980299.

[19] A.V. Ertemel, Consumer insight as competitive advantage using big data and ana lytics, Int. J. Commer. Financ. 1 (2015) 45–51.

[20] M.J. Flynn, S. Sarkani, T.A. Mazzuchi, Regression analysis of automatic measurement systems, IEEE Trans. Instrum. Meas. 58 (2009) 3373–3379, https://doi.org/ 10.1109/TIM.2009.2025467.

[21] I.A. Gelman, Setting priorities for data accuracy improvements in satisficing deci sion-making scenarios: a guiding theory, Decis. Support. Syst. 48 (2010) 507–520, https://doi.org/10.1016/j.dss.2009.11.001.

[22] M. Ghasemaghaei, G. Calic, Can big data improve firm decision quality? The role of data quality and data diagnosticity, Decis. Support. Syst. 120 (2019) 38–49, https:/ doi.org/10.1016/j.dss.2019.03.008.

[23] M. Ghasemaghaei, K. Hassanein, A macro model of online information quality perceptions: a review and synthesis of the literature, Comput. Hum. Behav. 55 (2016) 972–991, https://doi.org/10.1016/J.CHB.2015.09.027.

[24] G.F. Gomes, F.A. de Almeida, D.M. Junqueira, S.S. da Cunha, A.C. Ancelotti, Optimized damage identification in CFRP plates by reduced mode shapes and GA-ANN methods, Eng. Struct. 181 (2019), https://doi.org/10.1016/j.engstruct.2018.11.081.

[25] C. Grange, I. Benbasat, A. Burton-Jones, With a little help from my friends: cultivating serendipity in online shopping environments, Inf. Manag. 56 (2019) 225–235, https://doi.org/10.1016/J.IM.2018.06.001.

[26] Z.X. Guo, W.K. Wong, M. Li, A multivariate intelligent decision-making model for retail sales forecasting, Decis, Support. Syst. 55 (2013) 247–255. https://doi,org 10.1016/LDSS 2013.01.026

[27] M.S. Hamada, A Bayesian approach to multivariate measurement system assessment. J. Oual, Technol. 48 (2016) 246–252, https://doi,org/10.1080/00224065. 2016.11918164

[28] B. Heinrich, M. Klier, Metric-based data quality assessment — developing and evaluating a probability-based currency metric, Decis. Support. Syst. 72 (2015) 82–96. https://doi.org/10.1016/i.dss.2015.02.009

[29] J. Helena, D. Gaudêncio, F. Alves, D. Almeida, J. Batista, C. Quinino, P. Paulo, A. Paulo, D. Paiva, A multiobjective optimization model for machining quality in the AISI 12L14 steel turning process using fuzzy multivariate mean square error, Precis Eng, 56 (2019) 303–320. https://doi,org/10.1016/i,precisioneng,2019.01.001.

[30] D. Johnson, R.A., Wichern, Applied Multivariate Statistical Analysis, 6th ed., Prentice-Hall, New Jersey, 2007.

[31] P.A. Jokinen, Visualization of multivariate processes using principal component analysis and nonlinear inverse modelling, Decis. Support. Syst. 11 (1994) 53–65, https://doi.org/10.1016/0167-9236(94)90065-5.

[32] J. Lee, S.H. Kang, J. Rosenberger, S.B. Kim, A hybrid approach of goal programming for weapon systems selection, Comput. Ind. Eng. 58 (2010) 521–527, https://doi. org/10.1016/i.cie,2009.11.013.

[33] H.-C. Liao, Multi-response optimization using weighted principal component, Int. J. Adv. Manuf. Technol. 27 (2006) 720–725, https://doi.org/10.1007/s00170-004-2248-7.

[34] C.-J. Lu, T.-S. Lee, C.-M. Lian, Sales forecasting for computer wholesalers: a compar ison of multivariate adaptive regression splines and artificial neural networks, Decis. Support, Syst, 54 (2012) 584–596. https://doi,org/10.1016/JDSS.2012.08.006.

[35]. K.D. Maieske, Approval criteria for multivariate measurement systems. J. Oual Technol. 40 (2008) 140–153, https://doi.org/10.1080/00224065.2008.11917721.

[36] R.W. McHaney, D.E. Douglas, Multivariate regression metamodel: A DSS application in industry, Decis. Support. Syst. 19 (1997) 43–52, https://doi.org/10.1016/ S0167-9236(96)00037-1

[37] H. Moges, V. Van Vlasselaer, W. Lemahieu, B. Baesens, Determining the use of data quality metadata (DQM) for decision making purposes and its impact on decision outcomes — an exploratory study, Decis. Support. Syst. 83 (2016) 32–46, https:/ doi.org/10.1016/j.dss.2015.12.006.

[38] D.C. Montgomery, Design and Analysis of Experiments, 9th ed., John Wiley & Sons,

New York, 2017.

[39] A.M. Mood, Alexander M. Mood, Franklin A. Graybill, Duane C. Boes (Eds.), 1913-, Introduction to the Theory of Statistics. McGraw-Hill. New York. 1974

[40] R.S. Peruchi, P.P. Balestrassi, A.P. de Paiva, J.R. Ferreira, M. de Santana Carmelossi, A new multivariate Gage R&R method for correlated characteristics. Int. J. Prod. Econ. 144 (2013) 301–315, https://doi.org/10.1016/J.IJPE.2013.02.018.

[41] R.S. Peruchi, A.P. Paiva, P.P. Balestrassi, J.R. Ferreira, R. Sawhney, Weighted approach for multivariate analysis of variance in measurement system analysis, Precis. Eng. 38 (2014) 651–658, https://doi.org/10.1016/J.PRECISIONENG.2014.03.001.

[42] Alvin C. Rencher, Methods of Multivariate Analysis, 2nd ed., John Wiley & Sons, Inc, New York, 2002, https://doi.org/10.1002/0471271357.

[43] M. Scagliarini, A method for improving multivariate measurement systems assess ment, Qual. Reliab. Eng. Int. 31 (2015) 977–988, https://doi.org/10.1002/qre.1653.

[44] Y.-R. Shiau, Decision support for of-line gage evaluation and improving on-line gage usage, J. Manuf. Syst. 19 (2001) 318–331, https://doi.org/10.1016/S0278- 6125(01)89004-X

[45] Y. Timmerman, A. Bronselaer, Measuring data quality in information systems research, Decis. Support. Syst. (2019) 113138, , https://doi.org/10.1016/j.dss.2019. 113138.

[46] W.H. W, SiteQual: an integrated measure of web site quality, J. Enterp. Inf. Manag. 17 (2004) 430–440, https://doi.org/10.1108/17410390410566724.

[47] F.-K. Wang, C.-W. Yang, Applying principal component analysis to a GR&R study, J. Chinese Inst. Ind. Eng. 24 (2007) 182–189, https://doi.org/10.1080/ 10170660709509032.

[48] R.Y. Wang, D.M. Strong, Beyond accuracy: what data quality means to data con sumers, J. Manag. Inf. Syst. 12 (1996) 5–33, https://doi.org/10.1080/07421222 1996.11518099

[49] Y. Wang, H. Li, Complex chemical process operation evaluations using a novel analytic hierarchy process model integrating deep residual network with principal component analysis, Chemom. Intell. Lab. Syst. 191 (2019) 118–128, https://doi. org/10.1016/j.chemolab.2019.06.011.

[50] W.H. Woodall, C.M. Borror, Some relationships between Gage R&RCriteria, Qual. Reliab. Eng. Int. 24 (2008), https://doi.org/10.1002/qre.870.

[51] M. ZHOU, H. ZHANG, J. HU, Relationships between quality and attributes of spot welds, Weld. J. (2003) 72–77.

![](/api/attachments/MKSHM69V/fulltext/images/a75e40babce4e0702ade1e194d7cf8a85d5a291638ea77f05885464af62e0311.jpg)

Fabrício Alves de Almeida got his bachelor's degree in economics at Faculty of Economic Sciences Southern Minas Gerais, got his master's degree in industrial engineering at Federal University of Itajubá (UNIFEI) and is currently a PhD student in industrial engineering at UNIFEI as well Nowadays, he is also a professor at Faculty of Economic Sciences Southern Minas Gerais and member of the research group of the Nucleus of Manufacturing Optimization and Innovation Technology with h6 factor. His research areas are: multivariate statistical analysis, multiobjective optimization, quality engineering, industrial economics and design of experiments.

![](/api/attachments/MKSHM69V/fulltext/images/23683cf0de84dd82e9e1fd314047b5974e7612de93143277cde5d51f57c47650.jpg)

Rodrigo Reis Leite got his bachelor's degree in industrial engineering at Federal University of São João Del-Rei, got his master's degree in industrial engineering at the Federal University of Itajubá and is currently a phd student in industrial engineering at UNIFEI as well. Member of the Teaching, Research and Extension Group on Quality and Product and the Nucleus of Manufacturing Optimization and Innovation Technology. He is interested in control, modeling and optimization of processes with the aid of statistical quality control (CEQ), planning and analysis of experiments (DOE), multivariate statistics and multi-objective optimization.

![](/api/attachments/MKSHM69V/fulltext/images/977230742f6a09336811166528f761a07014468e2764aec966c80ff243d2d754.jpg)

Guilherme Ferreira Gomes is a professor of the Mechanical Engineering Institute at Federal University of Itajubá (UNIFEI). He got his bachelor's degree in mechanical engineering at UNIFEI. his master's degree in mechanical engineering at UNIFFL and master's degree in industria and mechanical engineering at École Nationale d'Ingénieurs de Metz. He has experience in Mechanical Engineering, working mainly in the following topics: structural analysis. materials resistance. numerical simulation. numerical methods. finite element method. optimization methods. artificial neural networks and engineering materials (metallic and composite)., Metrics since 2017: 85 citations and h6 factor.

![](/api/attachments/MKSHM69V/fulltext/images/fc2f3da53c1234b1d674657e5d3ac06683b9bc789787ea095920986251e8cb03.jpg)

Anderson Paulo de Paiva is a professor of the Industria Engineering and Management Institute at Federal University of Itajubá since 2005. He has 67 journal papers published on Web of Science, 67 journal papers published on Scopus and he has a H9 factor. He got his bachelor' degree in mechanical engineering at Centro Universitário do Sul de Minas in 1996, his master's degree in industrial engineering at Federal University of Itajubá (UNIFEI) in 2004 and his doctor's degree in mechanical engineering at Federal University of Itajubá (UNIFEI) in 2006. His main research areas are: multiobjective optimization, design of experiments and multivariate statistics.

![](/api/attachments/MKSHM69V/fulltext/images/253302af5bd49d22af00e52efff29b8843594af467bd0cb478172f0d649a2a61.jpg)  
methods and materials management.

José Henrique de Freitas Gomes is a Mechanical Industrial Engineer from the Federal University of Itajubá (2003–2007), with master's degree (2008–2010) and PhD (2010−2013) in Industrial Engineering from the same institution. Currently Associate Professor I of the Institute of Industrial and Management Engineering (IEPG) of the Federal University of Itajubá, in the undergraduate courses in Production Engineering and Administration, and postgraduate in Production Engineering. It acts in the research lines of modeling, analysis and optimization of production systems and manufacturing operations. His main research areas are: application and improvement of multi-objective methods, statistical methods, mathematical programming
