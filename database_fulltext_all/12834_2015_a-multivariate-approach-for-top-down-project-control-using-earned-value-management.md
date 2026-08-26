---
otero_id: 12834
otero_key: "GE7FY2TG"
title: "A multivariate approach for top-down project control using earned value management"
authors: "Jeroen Colin; Annelies Martens; Mario Vanhoucke; Mathieu Wauters"
year: "2015"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2015.08.002"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A multivariate approach for top-down project control using earned value management

Jeroen Colin <sup>a</sup>, Annelies Martens <sup>a</sup>, Mario Vanhoucke <sup>a,b,c,</sup>⁎, Mathieu Wauters <sup>a</sup>

<sup>a</sup> Faculty of Economics Business Administration, Ghent University, Tweekerkenstraat 2, 9000 Gent, Belgium

<sup>b</sup> Technology and Operations Management, Vlerick Business School, Reep 1, 9000 Gent, Belgium

<sup>c</sup> UCL School of Management, University College London, Gower Street, London WC1E 6BT, United Kingdom

## a r t i c l e i n f o

Article history: Received 10 May 2014 Received in revised form 11 June 2015 Accepted 6 August 2015 Available online 14 August 2015

Keywords: Project management Schedule control Earned value management (EVM) Simulation Principal component analysis (PCA)

## a b s t r a c t

Project monitoring and the related decision to proceed to corrective action are crucial components of an integrated project management and control decision support system (DSS). Earned value management/earned schedule (EVM/ES) is a project control methodology that is typically applied for top-down project schedule control. However, traditional models do not correctly account for the multivariate nature of the EVM/ES measurement system. We therefore propose a multivariate model for EVM/ES, which implements a principal component analysis (PCA) on a simulated schedule control reference. During project progress, the real EVM/ES observations can then be projected onto these principal components. This allows for two new multivariate schedule control metrics (T<sup>2</sup> and SPE) to be calculated, which can be dynamically monitored on project control charts. Using a computational experiment, we show that these multivariate schedule control metrics lead to performance improvements and practical advantages in comparison with traditional univariate EVM/ES models.

© 2015 Elsevier B.V. All rights reserved.

## 1. Introduction

Project management (PM) is a subdomain of Operations Research that gained quick momentum with the inception of project planning approaches such as the critical path method (CPM [1]) and the program evaluation and research technique (PERT [2]). These methods aim to construct a baseline schedule in the absence of resource restrictions. Explicit incorporation of resources constituted a logical next step and led to an explosion of solution techniques, problem formulations and extensions. An overview of the resource-constrained project scheduling problem and its many extensions can be found in the standard texts of [3, 4] and [5]. While a realistic baseline plan is of great importance, every project proceeds to the execution phase, disrupting the baseline schedule. Hence, the baseline schedule mainly serves as a reference point throughout project control. Due to the inherent presence of schedule disruptions, controlling the project's performance using techniques such as earned value management (EVM) is key to a project's success. EVM is a project control methodology that originated in the 1960s at the US Department of Defense. EVM aggregates the progress of individual activities to a higher level of the work breakdown structure (WBS) and provides the project manager with an indication of the overall health of the project. Because of the aggregation of information at a low level to a higher level of the WBS structure, EVM is known as a top-down control method ([6]). Three key metrics, namely planned value (PV), earned value (EV) and actual cost (AC) lie at the core of a number of performance indicators. These performance indicators quantify the progress in terms of time and cost and should act as a trigger for corrective action when the project objective is endangered. The fundamentals of EVM can be found in the books of [7] and [8]. Throughout the years, a number of different project control problems have been investigated from a theoretical and empirical perspective. In the next paragraph, a short yet non-exhaustive overview is given of the main themes in project control research.

Three project control research directions are forecasting, stability and triggers for corrective action. They are briefly described along the following lines. One of the main research themes revolved around forecasting the final budget and duration of a project by means of progress data. While initial studies emphasized the cost objective (cf. [9–12]), the paper of [13] introduced the earned schedule concept that renewed academics' interest in the time objective. Project duration forecasting has been investigated by [14] and [15]. [6] called on researchers to find ways in which risk analysis and project control can be of mutual benefit. [16] responded to this call by integrating sensitivity indexes with earned schedule (ES) forecasting methods. Incidentally, a research track that reacted to the recent trend of big data and artificial intelligence emerged. [17] and [18] provided case studies on how support vector machines can be used for project control, which [19] tested on a large set of topologically diverse projects.

A second main theme related to the stability of project control indexes. The Cost Performance Index (CPI), a well-known performance metric to measure and control the cost of the project in progress, has been the subject of scrutiny of many studies ([20] and [21]), leading to the acceptance and rejection of its stable behaviour. [22] criticized the criterion for assessing stability and proposed an alternative in a study in which forecasting stability was examined. A third research track focussed on triggers for corrective action. [23] analyzed the timing of control points, while [24] specified performance limits on the activity level. [25] examined variation on the project level using novel metrics, defined as the Schedule and Cost Control Index. [26] proposed the concept of statistical project control using earned value management and argued for the use of control charts in project control.

The studies cited above all focus on a single problem or criterion and little to no effort is given to integrating the various research streams into an integrated decision framework. Future research will undoubtedly be aimed at the integration of multiple criteria (cf. [27, 28] and [29]) or the development of an integrated project scheduling and control decision support system (DSS). [30] and [31] showed that the presence and quality of an information system led to improved decision-making, project manager satisfaction and better project scheduling, monitoring and control. While research on decision support systems for project control is extremely scarce, these systems found entry in project risk manage ment ([32] and [33]). While to the best of our knowledge no widely ac cepted project control decision support system exists, [34] mentions a number of elements that should be contained within such a system. These elements include status reporting, comparison with the baseline schedule, deviation analysis and implementation of corrective actions. While it is not our ambition to propose a DSS in this paper, we contribute to the analysis of project performance deviations from the baseline plan. Hence, we advance a crucial building block of a DSS. Based on the presented research, project managers can act on a warning signal to take corrective action. As a result, this paper's study lies on the interface between project monitoring and taking action. In this paper, we extract relevant information from multiple project control variables. Using principal component analysis (PCA), the information is combined and can be translated to a control chart. We believe that the presented multivariate model will aid project managers in a number of ways. First of all examining a single control chart instead of one chart for every variable contributes to the ease of use and may lead to less misleading signals. In order to verify if this is the case, the performance of this paper's multivariate control chart will be compared with the results of [26]. Secondly, a warning signal may prompt project managers to take corrective action. A good control chart should be capable of detecting performance problems and, at the same time, it should not issue a warning signal when no problem is found. Similar to [26], we will refer to these criteria as detection performance and probability of overreaction, respectively. Consequently, a second reason for project managers to incorporate the presented multivariate model is because of its improved reliability at detecting problems.

The outline of this paper is as follows. Section 2 introduces multivariate measurements in batch process control and translates these concepts to a project control environment. The employed technique for extracting relevant information from these multivariate measurements is PCA. Section 3 follows the same structure as Section 2. First, some details are provided on the PCA calculations after which a link to schedule control is made. Principal components are the outcome of a PCA and are a linear combination of the original variables. They represent the basis for a new coordinate system onto which the EVM/ES observations during project execution can be projected. In Section 4, we will demonstrate how two new performance metrics, Hotelling's T<sup>2</sup> and squared prediction error, can be calculated based on the PCA of Section 3. The performance of the multivariate method is tested by means of a large computational experiment that contains a diverse set of projects. Section 5 elaborates on how data was generated and explains the role played by Monte Carlo simulations. Additionally, the settings that were used for the simulations are detailed. Section 6 provides results of the computational experiment and benchmarks the performance of this paper's method to the univariate methods of [26]. Final conclusions on this paper's observations and contributions are drawn in Section 7. Four appendices to this paper are available online. They can be freely accessed on the statistical project control research page at www. projectmanagement.ugent.be.

## 2. Multivariate nature of schedule control

This paper advocates the use of a multivariate model for top-down schedule control. Multivariate techniques have a rich history in batch process control, which will be explained in Section 2.1. In Section 2.2, the multivariate nature of top-down schedule control is presented in a formal way. Subsequently, the implications related to this multivariate nature are discussed for the top-down schedule control process. Finally, we indicate why multivariate techniques are suited to deal with these implications.

## 2.1. Multivariate measurements in batch process control

Traditional univariate control charts such as CUSUM charts and Shewhart charts [35] have been widely used in batch process monitoring to monitor the key performance measurements of a batch process [36]. However, since these measurements are all driven by the same underlying events but are monitored independently, the interpretation of these control charts is difficult and might lead to misleading conclusions [37]. Therefore, MacGregor & Kourti [37] introduced the use of multivariate control charts in a batch process control context. In [38], MacGregor identified data overload, redundancy and noise as problems common to many multivariate measurement systems. In order to overcome these problems, numerous multivariate projection methods, such as PCA, have been used since the first application of Hotelling's multivariate ttest measure [39]. For a recent overview and comparison of these projection methods, the reader is referred to Bersimis et al. [40]. It is our belief that PCA is ideally suited for multivariate schedule control. In Section 2.2, a justification for the use of this technique is given.

## 2.2. Multivariate measurements in top-down schedule control

In order to present a formal characterisation of the top-down schedule control process, let us consider a vector x of EVM/ES measurements along the lifetime of the project as an observation for a multivariate random variable X. This random variable X represents the schedule performance measurements of a project (SV, SPI, SV(t), SPI(t)) as observed at the top WBS level. In EVM/ES, X is a function of the underlying activity level performance which can be expressed as the multivariate random variable D, containing the real durations for all activities in the project. In this research, we do not intend to calculate the activity level schedule performance explicitly. Instead, we would like to infer a state of schedule control, i.e. whether the activity durations conform to a pre-defined state of control, based on aggregated EVM data. In Section 5 we elaborate on how this state of schedule control is defined.

Based on this implicit inference process, control charts and their corresponding control limits are constructed. In Section 4, we will provide more details on how these charts and limits will be developed and how the information gathered from all four performance measures can be combined into a single control chart. These control charts will be presented to the project manager and will produce a signal when a control limit is exceeded. The project manager is then provided with an indication that the underlying activity durations do not conform with the predefined state of control and will likely invest time and resources to drill down the WBS of the project to find the activities that cause the departure from this pre-defined state of control.

With respect to the multivariate nature of EVM/ES observations, the following aspects (previously addressed by MacGregor [38]) should be considered:

• Data overload: As the project progresses, performance indicators are captured periodically, leading to a large data volume. To the best of our knowledge, none of the performance indicators has been identified to be the most reliable across all project outcomes. It is hence advisable for the project manager to monitor and interpret all EVM/ES schedule control metrics simultaneously.

• Redundancy: Redundancy, or collinearity, is a problem that is found when different observed variables are influenced by a common factor and should be addressed when inference is made from a multivariate variable [41]. The presence of redundancy in multivariate schedule control data is twofold. First, consider the SV and SPI of a project, observed at a particular time. Both measurements are the result of the same EV and PV of the project and are hence subject to redundancy. Second, even when the vector x is composed out of observations for a single EVM/ES performance metric along the lifetime of the project (instead of all four schedule performance metrics), x can still be subject to redundancy. If we suppose, for instance, that SPI(t) is measured along the lifetime of the project, it is likely that some of the observations for SPI(t) are influenced by the same couple of activities, hence collinearity will exist between these variables.

• Noise: In a statistical context, noise can be defined as the presence of unexplained variation in a sample. A multivariate schedule control procedure can be subject to noise due to two reasons. First of all, it has been shown that SPI behaves unreliably towards the end of late projects, since for any execution of a project that experiences delays, SPI will equal 1 at the end of the project [42]. However, in early stages of the project the information contained in SPI can be valuable for schedule control. Even in late stages of the project, the rate at which SPI converges towards 1 and the timing of the point at which the increase towards 1 takes place can provide the project manager with effective information with respect to the underlying activity level performance. Second, at higher WBS levels noise can be present in EVM/ES measurements due to the interplay between critical and non-critical activities [43]. Potential problems might be masked due to this interplay when the effects of non-performing activities are neutralised by well-performing activities. We therefore reason that a complex multivariate system such as EVM/ES could benefit from an automatic mechanism to identify and handle noise.

To conclude this section, we argue that PCA is an appropriate technique to deal with the multivariate nature of top-down schedule control. First of all, PCA is a statistical procedure that can be used to reduce the dimensionality of a large dataset with many potentially interrelated variables. Above that, the principal components, which are the outcome of a PCA, are calculated such that the first few components contain much of the information, while the last components are dominated by noise and can hence be disregarded without great information loss [44]. In Section 3, the calculation of these components is described in detail.

## 3. Principal component analysis of EVM/ES schedule performance metrics

In this section, we will first introduce the basics of a PCA and how it can be performed. Second, we will discuss how this technique can be applied in a schedule control context.

## 3.1. Calculating principal components

In the very early years of the 20th century PCA was developed by Pearson [45]. Ever since, PCA has been a popular procedure to reduce the dimensionality of a variable space. Full coverage on the basics of linear algebra, fundamental to PCA, lies outside the scope of this paper and the reader is referred to the recent book of Jolliffe [44]. Instead, we will give a brief overview of the matrix calculus that is required for a PCA.

PCA assumes that the true rank of a matrix of observations X is less than the number of observations which are made. Consequently, it conjectures that the observations can be projected onto a new set of coordinate axes, thereby removing redundancy and noise from the system. The PCA decomposition method first calculates the principal components of the observation space, i.e. the directions that will make up the new coordinate axes. These principal components are often also named the latent variables, since they represent the underlying (unobservable) factors really influencing the system dynamics. Consider a $( n \times P )$ matrix X that is a collection of n measurements for a P-variate randomly distributed variable x. The first principal component of x is defined as the vector of coefficients ${ \bf p } _ { 1 }$ for which the linear combination $t _ { 1 } = \mathbf { x p } _ { 1 }$ captures as much variance as possible contained in X, subject to $| { \bf p } _ { 1 } | = 1$ . The second principal component is then the vector of coefficients ${ \bf p } _ { 2 }$ for which the linear combination $t _ { 2 } = \mathbf { x } \mathbf { p } _ { 2 }$ contains as much of the variance from X that is not captured within $t _ { 1 } .$ . Additional principal components up to P are similarly defined.

In practice, a PCA is always performed using the computationally efficient singular value decomposition (SVD [46]) of X $( \boldsymbol { X } = \mathsf { U L A } ^ { T } )$ . A PCA decomposition of the matrix X can be written as

$$
X = \mathrm{TP} ^ {T}.\tag{1}
$$

Correspondingly, the standard deviation of the ith principal component (Eq. (2)) can be obtained from the singular values on the diagonal of L, since these are equal to the square roots of the eigenvalues $( \sqrt { l _ { i } ^ { 2 } } , \forall i \in \{ 1 , . . . , P \} )$ of X<sup>T</sup>X.

$$
s _ {\mathbf {t} _ {\mathrm{i}}} = \sqrt {\frac {l _ {i} ^ {2}}{n - 1}}.\tag{2}
$$

The score-loading nomenclature is very common in PCA literature and is therefore adopted here. The matrix of loadings $\mathrm { P } =$ $\left[ \pmb { \mathrm { p } } _ { 1 } \quad \pmb { \mathrm { p } } _ { 2 } \quad \dots \quad \pmb { \mathrm { p } } _ { P } \right]$ can be seen as a $( 1 \times P )$ collection of $( P \times 1 )$ <sup>½ -</sup>vectors of coefficients for the linear combination $t _ { i } = \mathbf { x } \mathbf { p } _ { i }$ that defines the ith principal component. A related term “matrix of rotations” expresses the geometrical interpretation of the loadings, as they represent a new coordinate space onto which x is projected. The $( n \times P )$ matrix of scores T can then be interpreted as the values in the new coordinate space for the collection of n measurements of x.

With respect to a PCA's ability to remove redundancy and noise, we need to discuss the relative importance of the different principal components. We will now explore this matter and discuss whether all principal components should be retained.

If all of the P principal components are retained for further analysis of the data, an observation for the P-variate vector of observations x can be reconstructed from its $( 1 \times P )$ vector of scores t, as expressed in Eq. (3).

$$
\mathbf {x} = \mathbf {t P} ^ {T} = \sum_ {i = 1} ^ {P} t _ {i} \mathbf {p} _ {i}.\tag{3}
$$

PCA is designed to reduce the dimensionality of a problem in a structured manner, with a minimal loss of valuable information. We assume that an integer k $( 0 < k \leq P )$ exists such that the last P–k principal components do not represent valuable information for our system. By definition, each principal component will only explain a small part of the original variation contained in X. For now we state that if only k principal components are retained, the original observation for the P-variate vector of observations x can be estimated as x^ from its $( 1 \times k )$ vector of scores t, as depicted in Eq. (4).

$$
\hat {\mathbf {x}} = \mathbf {t P} ^ {T} = \sum_ {i = 1} ^ {k} t _ {i} \mathbf {p} _ {i}.\tag{4}
$$

For the collection of n observations for x in X, the matrix form is presented in Eq. $( 5 )$ , where $\mathrm { T } _ { k }$ is the $( n \times k )$ matrix of scores, $\mathrm { P } _ { k }$ is the $( P \times k )$ matrix of loadings when only k principal components are retained and $\mathtt { E } _ { k }$ is the $( n \times P )$ error matrix.

$$
X = \sum_ {i = 1} ^ {k} \mathrm{T} _ {k} \mathrm{P} _ {k} ^ {T} + \mathrm{E} _ {k}.\tag{5}
$$

$\mathtt { E } _ { k }$ can be seen as the collection of error vectors e, each corresponding to the vector x when only k principal components are retained:

$$
\mathbf {e} = \mathbf {x} - \hat {\mathbf {x}} = \sum_ {i = k + 1} ^ {P} t _ {i} \mathbf {p} _ {i}.\tag{6}
$$

## 3.2. PCA model for project schedule control

When PCA is implemented on a large dataset, it is essential that the matrix X containing this dataset is in an appropriate format. This aspect has been dealt with in numerous publications for continuous monitoring of batch processes. An EVM/ES schedule control matrix can be considered to resemble the process matrix of a batch process that can be unfolded into a flat structure according to MacGregor [37] and Kourti [47]. Table 1 introduces the symbols and variables that are used in this section.

Symbols and abbreviations used in PCA for EVM/ES schedule control.

<table><tr><td colspan="2">Earned value/earned schedule</td></tr><tr><td colspan="2">Project EVM/ES key metrics</td></tr><tr><td>BAC</td><td>Budget at completion of the project</td></tr><tr><td> $PV_t$ </td><td>Planned value of the project at period t</td></tr><tr><td> $EV_t$ </td><td>Earned value of the project at period t</td></tr><tr><td> $ES_t$ </td><td>Earned schedule of the project at period t</td></tr><tr><td> $PC_t$ </td><td>Percentage complete of the project at period t: $PC_t = EV_t / BAC$ </td></tr><tr><td colspan="2">Project EVM/ES performance metrics</td></tr><tr><td> $SV_t = EV_t - PV_t$ </td><td>Schedule variance of the project at period t</td></tr><tr><td> $SPI_t = EV_t / PV_t$ </td><td>Schedule performance index of the project at period t</td></tr><tr><td> $SV(t)_t = ES_t - t$ </td><td>Schedule variance using earned schedule of the project at period t</td></tr><tr><td> $SPI(t)_t = ES_t / t$ </td><td>Schedule performance index using earned schedule of the project at period t</td></tr><tr><td colspan="2">with:</td></tr><tr><td>t=1,...,T</td><td>Current time period (otherwise denoted as AT)</td></tr><tr><td>T</td><td>Total duration of the project</td></tr></table>

Schedule control observations

<table><tr><td> $\Delta PC$ </td><td>The percentage complete increment between two review periods</td></tr><tr><td>K</td><td>The total number of review periods for which each project execution in the reference data has observations:  $K = 100/\Delta PC$ </td></tr><tr><td> $\kappa$ </td><td>The index for the review period ( $\kappa \in 1 : K$ )</td></tr><tr><td>J</td><td>The number of performance metrics included in the schedule analysis</td></tr><tr><td> $\mathbf{x}_{\kappa,1 : J}$ </td><td>Vector of observations at review period  $\kappa$ , including J performance metrics</td></tr><tr><td> $P = J^{*} K$ </td><td>The total number of observations for each project execution</td></tr></table>

During the execution of a project, a functional EVM/ES system will require periodic measurements of the performance metrics displayed in Table 1. In practice this might be done using software [48–50] and as specified within a contractual agreement or scheduled at distinct time interval along the project lifetime. The schedule control reference, from which principal components will be calculated, are fictitious project executions that are produced by a Monte Carlo simulation on activity durations. Different fictitious project executions can lead to different numbers of performance variables recorded for each execution. To have an equal amount of observations for each execution, equally spaced over the lifespan of a project, it is not appropriate to use a time index increasing from the start to the end of the project. Instead, our simulation model will use the project percentage complete (PC ) as a scaled time-indicator ranging from 0% to 100%. Without loss of generality, we will assume that the project schedule performance metrics are captured after each $\Delta \mathsf { P C }$ percentage of the work performed.

We present our methodology in a general form, and proceed with a vector of observations $\mathbf { x } _ { \kappa , 1 : J }$ with length J reported at each review period $\kappa \in \{ 1 , . . . , K \}$ , when $\mathsf { P C } = \kappa \Delta \mathsf { P C }$ percentage of the work in the project is completed. In the experimental results section of this paper, $\mathbf { x } _ { k , j }$ will be equal to [SV, SPI, SV(t), SPI(t)] for $j \in \{ 1 , . . . , 4 \}$ as the periodically reviewed EVM/ES schedule control metrics. The outcome of a Monte Carlo simulation on the duration of the activities results in a set of fictitious project executions, for which the EVM/ES observations are structured as the three-dimensional matrix presented at the top of Fig. 1. For each periodic review period $\kappa \in \{ 1 , . . . , K \} ,$ , J EVM/ES schedule control metrics are observed for n Monte Carlo runs. In order to use Eq. ((1)) to perform a PCA decomposition, the three-dimensional matrix consisting of K times n × J matrices has to be unfolded into a big $n \times K J$ (with $P =$ KJ) two-dimensional matrix as presented in Fig. 1.

Since we will combine SV and SV(t), which are expressed in monetary and time units respectively, with dimensionless indices SPI and SPI(t), we need to scale and centre each column of the matrix X before the PCA is performed. The SV and $\mathrm { S V ( t ) }$ values will be much larger than the SPI and SPI(t) values. This could result in relatively higher weights assigned to the SV and $\mathrm { S V } ( \mathrm { t } )$ observations in the loading vectors found by PCA, which might then lead to wrong interpretations. We will adopt the normalisation per column which is most common in literature, but other weighted PCA examples can also be found [40].

## 4. Multivariate schedule control using EVM/ES

In this section, we will apply the PCA decomposition discussed in Section 3 to produce two multivariate schedule control metrics, Hotelling's $T ^ { 2 }$ and SPE. In Section 4.1, these metrics will be discussed. Section 4.2 introduces how these metrics will be dynamically applied on project progress data. Furthermore, issues related to this dynamic use will be addressed. Section 4.3 presents how tolerance limits can be calculated prior to the execution of the project.

## 4.1. Two new schedule control metrics

Let us assume that we have a simulated schedule control reference in the appropriate matrix format X. This matrix contains observations for all J EVM/ES schedule performance metrics, for all K review periods and for all n fictitious project executions produced by a Monte Carlo simulation. The PCA decomposition of X results in a matrix of loadings P and a matrix of scores T. Let us assume that the project is now executed in real life, which results in a vector of observations $\pmb { x } _ { n e w } .$ This P-variate vector of observations will now be referenced against the PCA model, producing two schedule control metrics $( T ^ { 2 }$ Section 4.1.1 and SPE, Section 4.1.2), in order to assess the schedule performance of the project that is being executed.

![](/api/attachments/GE7FY2TG/fulltext/images/dd3ff746c656d1a2ab4435e8317735a6ef68055e3773eb3ce5752431247279c0.jpg)  
EVM/ES measurements × K PC-instances  
Fig. 1. Unfolding of the three-dimensional project data matrix ([51]).

## 4.1.1. Hotelling's T<sup>2</sup>

Hotelling [39] proposed the $T ^ { 2 }$ measure as a multivariate extension of the t-statistic, frequently used in statistical hypothesis testing. If the population covariance Σ for the P-variate variable x is not known, it can be estimated from its sample covariance matrix S (Eq. (7)) using n samples, where x is used to represent the P-variate mean of x.

$$
S = \frac {1}{n - 1} \sum_ {i = 1} ^ {n} \left(\mathbf {x} _ {i} - \overline {{\mathbf {x}}}\right) ^ {T} (\mathbf {x} _ {i} - \overline {{\mathbf {x}}}).\tag{7}
$$

In $\operatorname { E q . }$ . (8), Hotelling's $T ^ { 2 }$ statistic is used to measure the weighted multivariate distance of $\pmb { x } _ { n e w }$ from this mean X.

$$
T ^ {2} = (\mathbf {x} _ {n e w} - \overline {{\mathbf {x}}}) S ^ {- 1} (\mathbf {x} _ {n e w} - \overline {{\mathbf {x}}}) ^ {T}.\tag{8}
$$

It should be noted that, in order to calculate $T ^ { 2 }$ directly from $\mathbf { x } _ { n e w } ,$ the inverse of the covariance matrix S needs to be calculated. As discussed earlier, collinearity and noise in the multivariate variable severely impede the accurate calculation of this inverse.

Calculating $T ^ { 2 }$ from the scores resulting from a prior PCA decomposition, however, is much more computationally stable. Principal components are mutually independent and thus the covariance matrix is reduced to a diagonal matrix, for which calculating the inverse is trivial.

The scores for the new vector of observations $\mathbf { t } _ { n e w }$ can be found by projecting the P-variate EVM/ES observation vector $\mathbf { x } _ { n e w }$ onto the $k -$ dimensional principal component space (Eq. (9)).

$$
\mathbf {t} _ {n e w} = \mathbf {x} _ {n e w} \mathrm{P}.\tag{9}
$$

Hotelling's $T ^ { 2 }$ can then be calculated as depicted in Eq. (10), with $( \mathbf { t } _ { n e w } ) _ { i }$ the ith element of the vector of scores $\mathbf { t } _ { n e w }$ and $s _ { \mathbf { t } _ { i } } ^ { 2 }$ the estimated variance of the ith principal component.

$$
T _ {k} ^ {2} = \sum_ {i = 1} ^ {k} \left(\frac {\left(\mathbf {t} _ {\text {new}}\right) _ {i}}{\mathbf {s} _ {\mathbf {t} _ {i}}}\right) ^ {2}.\tag{10}
$$

From Eq. (10), it can be seen that calculating $T ^ { 2 }$ on the scores results in the summation of terms $\left( ( \mathbf { t } _ { n e w } ) _ { i } / s _ { \mathbf { t } _ { i } } \right) ^ { 2 }$ . While the last P–K principal components have almost no effect on X, their small variances $s _ { \mathbf { t } _ { i } } ^ { 2 }$ would lead to very large weighted distances, even for the slightest deviation. It is therefore apparent that these components should not be retained in the calculation, since they explain very little of the variation in X and generally represent random noise or errors introduced by the measurement system. Retaining only the first k principal components is hence of importance to ensure that only the principal components with the greatest influence on the EVM/ES schedule control vector x are retained.

## 4.1.2. The squared prediction error SPE

Hotelling's $T ^ { 2 }$ statistic can be used to monitor the weighted distance of the vector of schedule performance observations as projected onto a reference defined by the principal components. However, this metric will only detect whether or not the observed variation is greater than what was contained within the reference data matrix X. When this variation on the activity level is significantly different than the reference variation, the basis formed by the principal components might no longer be representative. In order to monitor whether the applied principal component analysis transformation is still representative for the new vector of observations $\pmb { x } _ { n e w }$ the squared prediction error (SPE) should be calculated. The SPE represents the squared perpendicular distance of the new P-variate observation from the projection space defined by the principal components and is calculated in Eq. (11), where e is defined for $\mathbf { x } _ { n e w }$ using Eq. (6) if k principal components are retained.

$$
S P E = \mathbf {e e} ^ {T} = \sum_ {i = 1} ^ {P} \left(\mathbf {x} _ {\text { new }, i} - \hat {\mathbf {x}} _ {\text { new }, i}\right) ^ {2}.\tag{11}
$$

## 4.2. Dynamic use of the $T ^ { 2 }$ and SPE schedule control metrics

We want to apply the proposed $T ^ { 2 }$ and SPE schedule measures ${ \mathrm { d } } \mathbf { y } .$ namically during the project execution phase. The new vector of observations $\mathbf { x } _ { n e w }$ needs to be projected onto the principal component space produced by the PCA decomposition of the schedule control reference X. Moreover, in order to calculate the scores $\mathbf { t } _ { n e w }$ with Eq. (9), the $( 1 \times P )$ vector $\mathbf { x } _ { n e w }$ needs to be complete. However, at a review period $\kappa \in \{ 1 , . . . , K \}$ of the project in progress, only κJ of the P observations will be available. To come up with an estimate for the scores $\mathbf { t } _ { n e w }$ we will need to deal with the problem of missing observations [52]. For notation purposes, we divide the vector of observations x into a $( 1 \times { \cal { K } } J )$ vector $\mathbf { x } ^ { * }$ for which values are already recorded and a $( 1 \times ( K - \kappa ) J )$ vector $\mathbf { x } ^ { \# }$ of missing measurements $( { \bf x } = [ { \bf x } ^ { * } \mathrm { ~ \bf ~ x } ^ { \# } ] )$

The problem of producing an estimate for t<sub>new</sub> when there are only observations available for $\mathbf { x } ^ { * }$ is described in the literature as dealing with missing data for on-line process monitoring. Different procedures have been proposed to deal with missing data in the literature and a comprehensive comparison is given by Nelson [53]. Conditional mean replacement (CMR) has been found to perform well by this study and is implemented here to produce an estimate ^ for ${ \bf t } _ { n e w }$ during the dynamic project control process.

In CMR, the expected values for the conditional multivariate distribution are used to estimate $\mathbf { x } ^ { \# }$ , given the present data and the most accurate estimate for the mean x and covariance matrix $\boldsymbol { \mathrm { S } } ( \hat { \mathbf { x } } ^ { \# } = \mathbb { E }$ $( \mathbf { x } ^ { \# } | \mathbf { x } ^ { * } , \mathbf { \overline { { x } } } , S ) )$ . In order to estimate the scores ^ using CMR, the covariance <sup>ð j ÞÞ</sup>matrix should be rewritten into the form of Eq. (12), where $\Theta = \operatorname { T } ^ { T } \operatorname { T } /$ $( n - 1 )$ represents a diagonal matrix with the variances explained by each principal component on its diagonal and the matrix of loadings is restructured as $\mathsf { P } = \bigl [ \mathsf { P } _ { \mathsf { P } ^ { \ast } } ^ { \# }$ .

$$
S = \left[ \begin{array}{c c} P ^ {\#} \Theta P ^ {\# T} & P ^ {\#} \Theta P ^ {* T} \\ P ^ {*} \Theta P ^ {\# T} & P ^ {*} \Theta P ^ {* T} \end{array} \right] = \left[ \begin{array}{c c} S _ {1 1} & S _ {1 2} \\ S _ {2 1} & S _ {2 2} \end{array} \right].\tag{12}
$$

Subsequently, the scores $\hat { \tau }$ can be estimated as follows:

$$
\hat {\boldsymbol {\tau}} = \mathbf {x} ^ {*} S _ {2 2} ^ {- 1} S _ {2 1} P ^ {\#} + \mathbf {x} ^ {*} P ^ {*}.\tag{13}
$$

## 4.3. Tolerance limits for the $T ^ { 2 }$ and SPE schedule control metrics

During the execution of a project, the $T ^ { 2 }$ and SPE metrics, calculated at the top WBS level, should be interpreted to infer a state of activity level schedule control. The most straightforward interpretation follows when a warning signal arises at the top WBS level. If either the $T ^ { 2 }$ or the SPE metric exceeds a tolerance limit, a warning signal is said to be produced. This warning signal should then indicate that the activity level performance no longer conforms with a pre-defined state of schedule control.

For independence with respect to distributional assumptions, we propose the use of the empirical cumulative distribution function (ecdf) for $T ^ { 2 }$ and SPE. In practice, this requires the calculation of the $T ^ { 2 }$ and SPE schedule control metric at each review period $( \forall \ 1 \leq \kappa \leq K )$ and for each fictitious project execution in our schedule control reference X. Obviously, the estimate ^, produced using CMR, now replaces the score vector $\mathbf { t } _ { n e w }$ in calculating $T ^ { 2 }$ and SPE for all κ b K. The tolerance limits at a review period κ for $T ^ { 2 }$ and SPE can then be calculated in accordance with a tolerance level α as the αth sample quantile. We refer to Hyndman and Fan [54] for more details on the calculations of the sample quantiles.

## 5. Experimental test design

In this section, the design of experiments to characterise the performance of the $T ^ { 2 }$ and the SPE metrics for project control is outlined. Section 5.1 introduces the data generation process to create a project benchmark set. In Section 5.2, the Monte Carlo simulations are described in detail. Section 5.3 provides the measures to quantify the performance of the multivariate model using the $T ^ { 2 }$ and the SPE schedule control metrics.

## 5.1. Data generation

In this section, the process of data generation will be elaborated. In order to make our findings generally applicable, a large set of diverse projects will be generated. The performance of the $T ^ { 2 }$ and SPE schedule control metrics will be assessed on this set of projects. In total, 900 pro jects with 30 activities each were generated by the project network generator RanGen [55]. Projects from this set were extensively used in previous research on project control [6, 16, 26, 19].

In real-life projects, the project manager makes an educated estimate of the duration and cost of the various activities. In computational studies, this process is imitated by drawing the estimated activity duration and cost from a simple statistical distribution. The baseline durations are randomly assigned to the 30 activities in the projects. They are sampled from a uniform distribution between 8 and 56 days. The baseline duration (estimate) for an activity i will be denoted as ${ \hat { d } } _ { i } .$ . The fixed cost for each activity is sampled uniformly between €0 and €500 and the variable cost is sampled uniformly between €700 and €1500. The schedule, referred to as the baseline schedule during the execution of the project, is the earliest start schedule obtained from a single forward pass of the critical path method.

## 5.2. Monte Carlo simulations

Simulation techniques have been widely used in recent studies on both project management [19, 26, 33] and decision support systems [33, 56]. In DSS, the use of simulation techniques can be an alternative to or complement for empirical research [57]. In a project management context, the application of Monte Carlo simulations enables the incorporation of activity duration and cost uncertainties by assigning a probability distribution function to the baseline estimates. Consequently, Monte Carlo simulations are an excellent tool to try to better understand the effects of uncertainty on the project outcome [58, 59]. For a more thorough discussion on how Monte Carlo simulations can be used in project management, the reader is referred to [60]. In this paper, Monte Carlo simulations serve a double purpose, which is discussed in Section 5.2.2. Section 5.2.1 describes the dynamic project progress model with which EVM/ES measurements are produced for ctitious project executions. In Section 5.2.3, the combined use of variation and risk input modelling for activity durations is described.

## 5.2.1. EVM/ES model

Fictitious project executions are simulated using P2 Engine [50] to generate EVM/ES data at K = 19 distinct PC intervals, with $\Delta \mathrm { P C } = 5 \% ,$ from 5% to 95%. At any review period $\kappa \in { 1 , . . , K }$ we chose $\mathbf { x } _ { \kappa , 1 } : J =$ [SV, SPI, SV(t), SPI(t)] for $j \in \{ 1 , . . . , 4 \}$ to be the periodically reviewed EVM/ES schedule control metrics. A total of $P = 1 9 \times 4 = 7 6$ original variables are thus recorded for the matrix X. It is worth noting that these variables contribute to the data overload a project manager is facing and hence, a PCA aids in reducing the number of variables.

Our model assumes that the EV for a single activity follows a linear accrue, starting from its actual start up to its BAC when it is finished [6]. The PV follows this same linear accrue from the planned start up to the planned finish time of the activity. EV and PV are calculated in P2 Engine at the project level and are compared to produce the SV, SPI, SV(t) and SPI(t) schedule performance metrics at each review period κ (cf. Table 1).

The calculations for the PCA decomposition and the CMR procedure to produce the $T ^ { 2 }$ and SPE schedule control metrics, along with the analysis of the results presented in Section 6, were implemented in the statistical programming language R [61].

## 5.2.2. Two-phased experiment

Monte Carlo simulations serve a dual purpose in our experiments. In the first phase the outcome of a large simulation (10,000 runs) is used to build a schedule control reference set for each of the 900 projects, which is then used to perform the PCA decomposition. The preferred state of schedule control will then determine which fictitious project executions end up in the reference data matrix X. We will provide additional detail on how we define this state of schedule control in Section 5.3. In the second phase of the Monte Carlo experiment, project progress situations are simulated (now with 1000 runs per project), where the activity level performance might not conform with the pre-defined state of schedule control that was constructed in the first phase. The warning signals that are generated by the $T ^ { 2 }$ and SPE control charts should accurately indicate whether or not the pre-defined state of control can be confirmed at the activity level. A control chart needs to strike a balance between two related issues. First of all, activity problems that endanger the project objective should be detected. Secondly, the project manager will only want to drill down into the WBS if the project is at risk. Hence, the probability of overreaction (i.e. a warning signal is issued but the project is doing fine) should be kept low while the detection performance should be maximised. Details on the performance and the balance between detection and overreaction of the $T ^ { 2 }$ and SPE metrics will be provided in Section 5.3.

## 5.2.3. Activity duration input modelling

The Monte Carlo simulations in this paper produce fictitious executions to generate project progress data. To that purpose, we need an appropriate model to accurately represent the uncertainty experienced at the activity level of the project. We opted for a combined input modelling where both risk and variation, often considered as separate sources of uncertainty in project management literature [62], are represented using separate probability distributions. We have chosen to implement probability functions from the family of generalised beta distributions, which have long been used in project management [6, 19, 63] due to their ability to accurately mimic the behaviour of random input processes driving the system [64], and their association to PERTstyle three point estimates [65]. The probability density function for a generalised beta random variable D is stated in Eq. ((14)), where Γ() denotes the gamma function and $\theta _ { 1 }$ and $\theta _ { 2 }$ represent shape parameters.

$$
f _ {\mathbf {D}} (d | a, b, \theta_ {1}, \theta_ {2}) = \left\{ \begin{array}{l l} \frac {\Gamma (\theta_ {1} + \theta_ {2})}{\Gamma (\theta_ {1}) \Gamma (\theta_ {2})} \frac {(d - a) ^ {\theta_ {1} - 1} (b - d) ^ {\theta_ {2} - 1}}{(b - d) ^ {\theta_ {1} + \theta_ {2} - 1}} & \text { if } a \leq d \leq b \\ 0 & \text { if } d <   a \lor b <   d \end{array} \right.\tag{14}
$$

We propose the use of a parameter vector ${ \pmb { \omega } } = ( a , b , m , \mu )$ with estimates for the minimum (a), the maximum (b), the mode (m) and the mean (μ) of the distribution, expressed as fractions of the baseline estimate duration $\hat { \boldsymbol { d } } _ { i }$ for activity i∈ . Specific settings for the different sce-<sup>N</sup>narios are presented in Table 2. From the shape parameters can be found using:

$$
\left\{ \begin{array}{l l} \theta_ {1} (\boldsymbol {\omega}) & = - \frac {(b + a - 2 m) (a - \mu)}{(m - \mu) (a - b)} \\ \theta_ {2} (\boldsymbol {\omega}) & = \frac {(b + a - 2 m) (b - \mu)}{(m - \mu) (a - b)} \end{array} \right..\tag{15}
$$

In each Monte Carlo simulation, risk is first modelled using the concept of linear association [66, 26]. Due to the absence of a unified methodology to test the impact of risky events or dependencies between activities in the project management literature, Trietsch et al. [66] suggest the use of a positive random variable B to act as a bias term in simulations of project executions. B is most easily perceived as a consistent over- or underestimation of activity durations, or a project-wide effect of an uncertain event. In our experiments, we will assign a parameter vector ${ \pmb { \omega } } _ { R }$ to represent this risk factor. Consequently, for each fictitious project execution in the simulation, a bias term is sampled from the generalised beta distribution with parameter vector ${ \pmb { \omega } } _ { R } .$ Subsequently, for all activities in the project, variation is added using a parameter vector ${ \pmb \omega } _ { V }$ which can be chosen independently from ${ \pmb \omega } _ { R } .$ The duration d of an activity i in a fictitious project execution can then ultimately be considered as a sample from a generalised beta distribution (with parameter vector ${ \pmb { \omega } } _ { V } )$ multiplied with a biased baseline estimate $\hat { B d _ { i } }$

In the experiments, for which results will be shown in Section $6 , \pmb { \omega } _ { R }$ and ${ \pmb \omega } _ { V }$ are chosen separately from the set of parameter vectors presented in Table 2. A distinction is made between the general performance experiment and the sensitivity experiment. In the general performance experiment, activity duration distributions are chosen such that the activities finish on average early ( ), on time ( ) or late ( ). As a result, the performance of different project outcomes is compared. The sensitivity experiment zooms in on the distribution for which activities end on time. We derived two distinct sets of parameter vectors $( \pmb { \omega } _ { 2 \mu _ { 1 } }$ to ${ \pmb { \omega } } _ { 2 \mu _ { 5 } }$ and $\pmb { \omega } _ { 2 s _ { 1 } } \ \mathrm { t o } \ \pmb { \omega } _ { 2 s _ { 6 } } )$ to model changes in respectively the mean and the standard deviation. These can be used in the sensitivity experiment to test the robustness to over- or underestimation, when assumptions are made with respect to distributional characteristics of the activity durations.

Parameter vectors for the generalised beta distribution.

<table><tr><td colspan="3">General performance experiment</td><td colspan="6">Sensitivity experiment</td></tr><tr><td rowspan="2"> $\omega$ </td><td rowspan="2">(a,b,m,μ)</td><td rowspan="2"> $\sigma$ </td><td colspan="3">Mean</td><td colspan="3">Standard deviation</td></tr><tr><td> $\omega$ </td><td>(a,b,m,μ)</td><td> $\sigma$ </td><td> $\omega$ </td><td>(a,b,m,μ)</td><td> $\sigma$ </td></tr><tr><td> $\omega_1$ </td><td>(0.1,1.2,0.7,0.6)</td><td>0.38</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="6"> $\omega_2$ </td><td rowspan="6">(0.2,4,0.9,1)</td><td rowspan="6">0.30</td><td> $\omega_{2\mu_1}$ </td><td>(0.2,4,0.51,0.7)</td><td>0.3</td><td> $\omega_{2s_1}$ </td><td>(0.2,4,0.40,1)</td><td>0.50</td></tr><tr><td> $\omega_{2\mu_2}$ </td><td>(0.2,4,0.90,1.0)</td><td>0.3</td><td> $\omega_{2s_2}$ </td><td>(0.2,4,0.70,1)</td><td>0.42</td></tr><tr><td> $\omega_{2\mu_3}$ </td><td>(0.2,4,1.22,1.3)</td><td>0.3</td><td> $\omega_{2s_3}$ </td><td>(0.2,4,0.85,1)</td><td>0.35</td></tr><tr><td> $\omega_{2\mu_4}$ </td><td>(0.2,4,1.57,1.6)</td><td>0.3</td><td> $\omega_{2s_4}$ </td><td>(0.2,4,0.92,1)</td><td>0.28</td></tr><tr><td> $\omega_{2\mu_5}$ </td><td>(0.2,4,1.89,1.9)</td><td>0.3</td><td> $\omega_{2s_5}$ </td><td>(0.2,4,0.96,1)</td><td>0.20</td></tr><tr><td></td><td></td><td></td><td> $\omega_{2s_6}$ </td><td>(0.2,4,0.98,1)</td><td>0.15</td></tr><tr><td> $\omega_3$ </td><td>(0.9,4,1.3,1.4)</td><td>0.38</td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

## 5.3. Performance measurement

In order to show the performance improvement of employing a multivariate model, the obtained results will be compared and contrasted with the schedule control process using statistical tolerance limits. This univariate procedure was presented by Colin and Vanhoucke (2014) [26] and uses statistical tolerance limits for SV, SPI, SV(t) and SPI(t). The schedule control metrics were applied either directly (X chart) or monitored by means of the difference between two consecutive measurements (R chart). The X and R charts were shown to outperform the decision making based on rules-ofthumb that are omnipresent in EVM/ES schedule control in practice. We were able to obtain a fair comparison in our experiments since the same fictitious project executions were used to calculate tolerance limits for both the univariate and multivariate EVM/ES schedule control metrics. Subsequently, we compared the warning signals generated by all performance metrics with respect to the underlying activity level of the project for additional fictitious project executions in the second phase.

In order to demonstrate the performance of the newly proposed multivariate control metrics, we first needed to define a state of schedule control, as established at the activity level of the project. The performance of the decision process could then be quantified by whether or not this state of control can be correctly inferred from the observations made at the highest WBS level. We measured this performance using two measures, the detection performance and the probability of overreactions. These measures quantify the balance a control chart should maintain, as discussed in Section 5.2.2. The detection performance and probability of overreactions can be combined into a single measure that reports on the overall control chart performance and is known in the classification technique literature as the area under the curve. The state of schedule control, detection performance, probability of overreactions and the combination into the area under the curve will be discussed in the following paragraphs.

## 5.3.1. Defining a state of schedule control

The state of schedule control is primarily defined by the fictitious project executions that are included in the schedule control reference matrix X. This reference is then used to calculate tolerance limits and to compare with the executions of the second phase of the Monte Carlo simulations. We will illustrate along the following lines how a set of fictitious project executions, generated in the first phase of the simulation model, is chosen to constitute the project schedule control reference.

In the first phase of the Monte Carlo simulation, specific values are chosen for the parameter vectors ${ \pmb { \omega } } _ { R }$ and ${ \pmb \omega } _ { V } $ which results in a probability distribution for the simulated activity durations of a project. Fig. 2 illustrates the process of choosing executions that end up in the schedule control reference set. The x-axis of the figure corresponds with the proportion of the simulated activity duration (d ) to the baseline activity duration $( \hat { d } _ { i } )$ . The y-axis represents the probability density. <sup>ð Þ</sup>The line in Fig. 2 shows the approximated density of the activity durations from a sample of 10,000 fictitious project executions, where ${ \pmb { \omega } } _ { R } = { \pmb { \omega } } _ { 2 }$ and ${ \pmb { \omega } } _ { V } = { \pmb { \omega } } _ { 2 }$ . The histograms in lightgrey and darkgrey in Fig. 2 represent two fictitious project executions from this sample of

![](/api/attachments/GE7FY2TG/fulltext/images/2baa3d021ea1af337ce733b90e4f4bb75b373d9c51cc227aba87fc502e3e5dd0.jpg)  
Fig. 2. Activity level test for schedule control: Kolmogorov–Smirnov.

10,000. Even though these fictitious executions were simulated from the same distribution, they are very dissimilar in terms of their appearance on the activity duration scale.

Fig. 2 illustrates how it can be difficult to define a state of schedule control due to random variation. We will therefore employ a metric to describe how close a fictitious project execution lies to the empirical density, approximated from all 10,000 samples. We test for each execution whether it is likely to have been sampled from the empirical distribution function, which is based on ${ \pmb { \omega } } _ { R }$ and ${ \pmb \omega } _ { V }$ . We do this using the two-sample Kolmogorov–Smirnov (K–S) statistic, a wellestablished non-parametric statistic to test the equality of two distributions [67]. Corresponding to a significance level of $\eta = 0 . 0 0 1$ a critical value $( \mathrm { K } - \mathsf { S } _ { \eta } = 0 . 3 6 )$ ) for the K–S statistic can be found [68]. Using the K–S statistic and its critical value, the schedule control reference set will only include executions for which the sample of activity durations is likely to have been drawn from the empirical distribution. $\left( \mathbb { K } - \mathbb { S } < \mathbb { K } - \mathbb { S } _ { \eta } \right)$ .

## 5.3.2. Detection performance

In the second phase of the simulation experiment, we test whether the signals generated at the highest WBS level correspond to the underlying activity level schedule performance. In other words, for a project execution that does not conform with the defined state of schedule control $\left( \operatorname { K } - \operatorname { S } > \operatorname { K } - \operatorname { S } _ { \eta } \right)$ , the project manager should be given a warning during the lifetime of the project. The detection performance is thereby calculated for all runs in the second phase as the ratio of the number of runs that generate a signal to the total number of runs that do not comply with the state of schedule control.

## 5.3.3. Probability of overreactions

In conjunction with the detection performance, a dual measure needs to be formulated. The probability of overreactions measures whether the control charts provide a false warning signal to the project manager. This corresponds with a situation where the project manager receives a warning signal, yet when drilling down into the WBS no major problems can be identified. Hence, the project manager's effort has been in vain. The probability of overreactions can be calculated from all runs in the second phase of the simulation experiment for which the state of schedule control can still be assumed to be representative $( \operatorname { K } - \mathsf { S } < \operatorname { K } - \mathsf { S } _ { \eta } )$

![](/api/attachments/GE7FY2TG/fulltext/images/2cbb2acc1da7522b000a05e30e01095675b5473e708f44ce0fd48dcd5233e08e.jpg)  
Fig. 3. Illustration of the duality of the detection performance and the probability of overreactions.

## 5.3.4. Area under the curve

As mentioned previously, a control metric should yield a good balance between a high detection performance and low probability of overreaction. In order to integrate the dynamics of both the probability of overreactions and the detection performance and provide an overall picture of the multivariate metrics' qualities, we propose the use of the area under the curve. This measure is widely used in classification testing and machine learning [69] and, as the name suggest, can be obtained by Riemann integration of the curves produced by the probability of overreaction/detection performance couples, as displayed in Fig. 3. The probability of overreactions is denoted along the x-axis and the detection performance along the y-axis. The points in the graph show the values of the detection performance and probability of overreaction for different values of α, the αth quantile for the statistical tolerance limits. From a pragmatic perspective, α incorporates a project manager's aversion to risk and the willingness to investigate potentially false warning signals [26]. The area under the curve will be the main instrument for reporting on the performance of the $T ^ { 2 }$ and SPE metrics, which is detailed in the next section.

## 6. Results

In order to demonstrate the added value of employing multivariate instead of univariate models, two large simulation experiments were conducted that make use of the parameter vectors introduced in Table 2 of Section 5.2.3. Using the parameter vectors outlined under general performance experiment, we will discuss the overall improvement of multivariate schedule control over the univariate use of EVM/ ES metrics in Section 6.1. Additionally, we explore the number of principal components that should be retained in the analysis for schedule control. The sensitivity experiment was conducted using the parameter vectors for the generalised beta family of distributions where either the mean $\left( \pmb { \omega } _ { 2 \mu _ { 1 } } \ \mathrm { t } \circ \pmb { \omega } _ { 2 \mu _ { 5 } } \right)$ ) or the standard deviation is varied $( { \pmb { \omega } } _ { 2 s _ { 1 } }$ to ${ \pmb { \omega } } _ { 2 s _ { 6 } } )$ . In Section 6.2, we present the effect of an under- or overestimation of the mean or standard deviation on the performance of the multivariate model.

## 6.1. General performance experiment

In order to compare the general performance of the multivariate and univariate schedule control metrics described in this paper, a simulation experiment was carried out with scenarios where activities end either early, on time or late, on average. These project outcomes were obtained by means of a careful choice of the risk and variation parameter vectors. Fig. 4 displays the performance of the multivariate and univariate models, in which the x-axis denotes the values for the couple $( \pmb { \omega } _ { R } , \pmb { \omega } _ { V } )$ to establish early, on time and late project outcomes. The boxplots of Fig. 4 present the recorded area under the curve for the multivariate $T ^ { 2 }$ and SPE metrics, and the univariate schedule control metrics $\mathrm { x }$ and R from Colin and Vanhoucke (2014) [26]. As mentioned previously, the area under the curve represents the detection performance and probability of overreaction, with a higher value corresponding to a higher performance level. Overall, Fig. 4 shows that the multivariate metrics outperform the traditional univariate use of EVM/ES across all scenarios. The difference between the $T ^ { 2 }$ metric and the SPE is small, with the latter outperforming the former slightly. The difference between the multivariate and the univariate control metrics becomes smaller in situations where activities are on time or late on average, but the multivariate approaches still show to be significantly better.

![](/api/attachments/GE7FY2TG/fulltext/images/48ab895b88c21b6d3c84498c92221ae1af494e956308b23f7a4f67c81feacc4d.jpg)  
Fig. 4. General performance comparison of the univariate and multivariate models.

## Number of principal components

![](/api/attachments/GE7FY2TG/fulltext/images/fa8c32a06f8f9d4453bce89e097f43f9d5a932fe576060d37116154aeff20e4d.jpg)  
Fig. 5. Optimal number of principal components for the multivariate schedule control metrics.

## 6.1.1. Number of principal components to retain

When performing a PCA, a delicate balance needs to be maintained between selecting a sufficient amount of principal components such that enough variation is captured and limiting the amount of principal components to avoid reintroducing noise (cf. Section 2). Hence, the number of principal components should be varied since this balance may differ depending on the schedule control metric at hand. In this paragraph, the results of varying the number of principal components to retain are presented. To that end, the results of Fig. 4 are restructured. Fig. 5 shows the recorded area under the curve for the $T ^ { 2 }$ and SPE metrics in function of the number of principal components k retained in the model. It shows that, in general, the $T ^ { 2 }$ metric benefits from a very low number of principal components (preferably only 1), while the SPE metric performs better when more principal components are included in the PCA model.

A similar analysis was conducted for the univariate X and R control procedures, where we searched for the EVM/ES control metric (SV, SPI, SV(t), SPI(t)) that delivered the best performance. These findings are presented in Fig. 6, where a birds-eye perspective is given on six histograms in which the relative size of the points represents how often a certain metric is found to be performing best. A single EVM/ES metric that outperforms all other could not be found. This finding is of crucial importance since it confirms that a project manager should monitor all metrics through a project's progress at the expense of the problems cited in Section 2. This problem is alleviated by our multivariate model since the PCA combines all EVM/ES schedule control metrics. We therefore recommend a combined use of all EVM/ES schedule control metrics, where none is neglected during the execution of the project.

## 6.2. Sensitivity experiment

The statistical tolerance limits for the schedule control metrics discussed in this paper are obtained from a simulated set of fictitious project executions. These are generated using a Monte Carlo simulation, for which probability distributions serve as input to model the real activity durations. In a realistic project environment, it is not always possible to produce probability distributions that accurately reflect the stochastic nature of the input processes. Consequently, an under or over-estimation of one of the distributional characteristics cannot always be avoided.

We model this situation using the parameter vectors ${ \pmb { \omega } } _ { 2 \mu _ { 1 } }$ ${ \pmb { \omega } } _ { 2 \mu _ { 5 } }$ to test a change in the mean and ${ \pmb { \omega } } _ { 2 s _ { 1 } }$ to ${ \pmb { \omega } } _ { 2 s _ { 6 } }$ to test a change of the standard deviation. In the sensitivity experiment, the statistical tolerance limits are produced from a state of schedule control defined by $\begin{array} { r } { \pmb { \omega } _ { R } = \pmb { \omega } _ { V } = \pmb { \omega } _ { 2 } . } \end{array}$ Additional fictitious project executions are generated with alternately one of the parameter vectors $\pmb { \omega } _ { 2 \mu _ { 1 } } . . . \pmb { \omega } _ { 2 \mu _ { 5 } }$ or ${ \pmb { \omega } } _ { 2 s _ { 1 } }$ ${ \pmb { \omega } } _ { 2 s _ { 6 } }$ assigned to either or ${ \pmb \omega } _ { V } ,$ in order to test the effect of a change in the mean or standard deviation.

![](/api/attachments/GE7FY2TG/fulltext/images/821e9ffd1af1fed57c19e3da921c6c7cbfcadbadb48dccbbc3734dff3f070622.jpg)  
Fig. 6. Optimal schedule control metrics.

Fig. 7 shows the calculated area under the curve for the univariate and multivariate procedures, where the left pane displays the impact of a change in the mean and the right pane depicts the impact of a change in the standard deviation. The pre-defined state of schedule control ${ \bf ( } { \pmb { \omega } } _ { R } = { \pmb { \omega } } _ { V } = { \pmb { \omega } } _ { 2 } )$ has a mean equal to 1 and a standard deviation of 0.3.

From the left pane of Fig. 7, we can conclude that the performance of the R schedule control procedure decreases drastically for projects for which the average activity duration increases. The $T ^ { 2 }$ , SPE and X schedule control procedure seem to be much more robust to under- or overestimates of the mean activity duration.

With respect to the impact of changes in the standard deviation of the underlying activity durations, all of the investigated schedule control procedures exhibit the same behaviour. When the standard deviation is larger than what was assumed for calculating the schedule control reference, the performance of the decision making process decreases significantly, as shown in the right-hand side of Fig. 7.

## 7. Conclusion

In this paper, we present a multivariate model using EVM/ES for topdown project schedule control. This model assumes an important role in a decision support system since it lies on the interface between monitoring and corrective action taking. Based on the results of the proposed multivariate model, the project manager drills down into the WBS and takes action if the project is endangered. The need for a multivariate approach is dictated by the very nature of the EVM/ES measurement system. A project manager is faced with observations for the EVM/ES variables that suffer from data overload, redundancy and noise. Based on the principle of batch process control, we have introduced a multivariate model for top-down project schedule control. Two multivariate schedule control metrics $( T ^ { 2 }$ and SPE) are proposed, that can be presented to the end user of the DSS on control charts.

It is our belief that the proposed multivariate model leads to a number of distinct advantages, which are discussed along the following lines.

• A large simulation experiment, in line with previous project control research, showed that the $T ^ { 2 }$ and SPE metrics outperform the current state-of-the-art choices for EVM/ES project control. The multivariate metrics, whose performance was measured using the area under the curve, demonstrate a superior ability in inferring underlying activity level performance from top-down schedule control metrics.

• The experimental results also indicated that data overload is a realistic threat. No univariate schedule control metric was found to consistently outperform the other univariate metrics. As a result, a project manager who makes use of univariate control charts should monitor all schedule control metrics. Additionally, the project manager runs the risk of receiving mixed warning signals, where some metrics indicate that the project is endangered, while others show that the project is still fine.

• Implementing the multivariate procedure in a DSS leads to practical advantages. We have shown that the use of a single multivariate metric $\left( T ^ { 2 } \thinspace 0 \mathrm { r } S P E \right)$ can lead to considerable improvements and reduces the issue of data overload. Furthermore, the application of a PCA also removes redundancies and noise from the inference process of activity level schedule performance. Reporting a single multivariate metric is also useful from a reporting and communications point of view. The presented model is more accurate and should inspire a larger degree of confidence of the project manager in this component of a DSS.

Robustness of the project control approaches  
![](/api/attachments/GE7FY2TG/fulltext/images/1633259ab737a30e3d5317f4e570c2c7c6f9e099bb2a3e302a3a8af686b6691d.jpg)  
Fig. 7. Influence of a change in the mean and the standard deviation on the project schedule control performance.

Hence, it is our hope that this increased confidence will also lead to timelier corrective action.

Future work is inspired by the fact that the recorded area under the curve is still mostly lower than 1. This implies that some portion of the activity level performance is still obscured by the aggregated EVM/ES observations. While this issue is intrinsically connected to a top-down control process, the question rises whether other projection methods or transformations might improve the inference process even more. Apart from this future research direction, attempts should be made to integrate the project control research streams into a single decision support system.

## References

[1] J. Kelley, M. Walker, Critical Path Planning and Scheduling: An Introduction, Mauchly Associates, Ambler, PA, 1959

[2] W. Fazar, Program evaluation and review technique, The American Statistician 13 (1959) 10.

[3] W. Herroelen, B. De Reyck, E. Demeulemeester, Resource-constrained project scheduling: a survey of recent developments, Computers & Operations Research 25 (1998) 279–302.

[4] R. Kolisch, R. Padman, An integrated survey of deterministic project scheduling, OMEGA: International Journal of Management Science 29 (3) (2001) 249–272.

[5] S. Hartmann, D. Briskorn, A survey of variants and extensions of the resourceconstrained project scheduling problem, European Journal of Operational Research 207 (2010) 1–15.

[6] M. Vanhoucke, On the dynamic use of project performance and schedule risk information during project tracking, OMEGA: International Journal of Management Science 39 (2011) 416–426.

[7] Q. Fleming, J. Koppelman, Earned Value Project Management, 3rd edition Project Management Institute, Newton Square, Pennsylvania, 2010 URL http://books.google.be/books?id=ZMRVngEACAAI

[8] M. Vanhoucke, Measuring time — improving Project performance using earned value management, International Series in Operations Research and Management Science, vol, 136, Springer, 2010

[9] D. Christensen, The estimate at completion problem: a review of three studies, Project Management Journal 24 (1993) 37–42.

[10] D. Christensen, Cost overrun optimism: fact or fiction? Acquisition Review Quarterly (Winter 1994) 25–38.

[11] D. Christensen, R. Antolini, J. McKinney, A review of estimate at completion (EAC) research, Journal of Cost Analysis and Management (Spring 1995) 41–62.

[12] O. Zwikael, S. Globerson, T. Raz. Evaluation of models for forecasting the final cost of a project, Project Management Journal 31 (1) (2000) 53–57.

[13] W. Lipke, Achieving normality for cost, The Measurable News (Fall/Winter 2003) 5 11.

[14] S. Vandevoorde, M. Vanhoucke, A comparison of different project duration forecasting methods using earned value metrics, International Journal of Project Management 24 (2006) 289–302.

[15] M. Vanhoucke, S. Vandevoorde, A simulation and evaluation of earned value metrics to forecast the project duration, Journal of the Operational Research Society 58 (2007) 1361–1374.

[16] R. Elshaer, Impact of sensitivity information on the prediction of project's duration using earned schedule method, International Journal of Project Management 31 (2013) 579–588.

[17] M.-Y. Cheng, Y.-W. Wu. Evolutionary support vector machine inference system fon construction management, Automation in Construction 18 (5) (2009) 597–604.

[18] M.-Y. Cheng, H.-S. Peng, Y.-W. Wu, T.-L. Chen, Estimate at completion for construction projects using evolutionary support vector machine inference model, Automation in Construction 19 (5) (2010) 619–629.

[19] M. Wauters, M. Vanhoucke, Support vector machine regression for project control forecasting, Automation in Construction 47 (2014) 92–106.

[20] D. Christensen, K. Payne, Cost performance index stability — fact or fiction? Journal of Parametrics 10 (1992) 27 40.

[21] K. Henderson, O. Zwikael, Does project performance stability exist? A reexamination of CPI and evaluation of SPI(t) stability? Crosstalk — The Journal of Defense Software Engineering 21 (2008) 7–13.

[22] M. Wauters, M. Vanhoucke, Study of the stability of earned value management forecasting, Journal of Construction Engineering and Management 141 (4) (2015) 1–10.

[23] T. Raz, E. Erel, Optimal timing of project control points, European Journal of Operational Research 127 (2) (2000) 252–261.

[24] R.A. Bowman, Developing activity duration specification limits for effective project control, European Journal of Operational Research 174 (2) (2006) 1191–1204

[25] J. Pajares, A. López-Paredes, An extension of the EVM analysis for project monitoring: the cost control index and the schedule control index, International Journal of Project Management 29 (2011) 615–621.

[26] J. Colin, M. Vanhoucke, Setting tolerance limits for statistical project control using earned value management, OMEGA: International Journal of Management Science 49 (2014) 107–122.

[27] M. Lauras, G. Marques, D. Gourc, Towards a multi-dimensional project performance measurement system Decision Support Systems 55 (2013) 927–937

[28] C. Mota, A. Almeida, L. Alencar, A multiple criteria decision model for assigning pri orities to activities in project management, International Journal of Project Management 27 (2009) 175–181

[29] G. Marques, D. Gourc, M. Lauras, Multi-criteria performance analysis for decision making in project management, International Journal of Project Management 29 (2010) 1057–1069.

[30] M. Caniëls, R. Bakens, The effects of project management information systems on decision making in a multi project environment, International Journal of Project Management 30 (2012) 162–175.

[31] L. Raymond, F. Bergeron, Project management information systems: an empirical study of their impact on project managers and project success, International Journal of Project Management 26 (2008) 213 220.

[32] Y. Hu, J. Du, X. Zhang, X. Hao, E. Ngai, M. Fan, M. Liu, An integrative framework for intelligent software risk planning, Decision Support Systems 55 (2013) 927–937.

[33] C. Fang, F. Marle, A simulation-based risk network model for decision support in project risk management, Decision Support Systems 52 (2012) 635–644.

[34] O. Hazir, A review of analytical models, approaches and decision support tools in project monitoring and control, International Journal of Project Management 33 (2015) 808–815.

[35] W.A. Shewhart, Economic Control of Quality of Manufactured Product, vol. 509ASQ Quality Press, 1931.

[36] Y. Fang, J. Zhang, Performance of control charts for autoregressive conditional heteroscedastic processes, Journal of Applied Statistics 26 (6) (1999) 701–714.

[37] I. MacGregor, T. Kourti, Statistical process control of multivariate processes, Control Engineering Practice 3 (3) (1995) 403–414

[38] J.F. MacGregor, Using on-line process data to improve quality: challenges for statisticians\*, International Statistical Review 65 (3) (1997) 309–323.

[39] H. Hotelling, A generalized t test and measure of multivariate dispersion, Proc. Second Berkeley Symp. on Math. Statist. and Prob 1951, pp. 23–41.

[40] S. Bersimis, S. Psarakis, J. Panaretos, Multivariate statistical process control charts: an overview, Quality and Reliability Engineering International 23 (5) (2006) 517–543.

[41] G.W. Stewart, et al., Collinearity and least squares regression, Statistical Science 2 (1) (1987) 68–84.

[42] W. Lipke, O. Zwikael, K. Henderson, F. Anbari, Prediction of project outcome: the application of statistical methods to earned value management and earned schedule performance indexes, International Journal of Project Management 27 (2009) 400–407.

[43] M. Vanhoucke, Measuring the efficiency of project control using fictitious and empirical project data, International Journal of Project Management 30 (2012) 252–263.

[44] I. Jolliffe, Principal Component Analysis, Wiley Online Library, 2005

[45] K. Pearson, Liii. On lines and planes of closest fit to systems of points in space, The London, Edinburgh, and Dublin Philosophical Magazine and Journal of Science 2 (11) (1901) 559–572.

[46] E. Anderson, Z. Bai, C. Bischof, S. Blackford, J. Demmel, J. Dongarra, J. Du Croz, A. Greenbaum, S. Hammerling, A. McKenney, et al., LAPACK Users' Guide, vol. 9Siam, 1999.

[47] T. Kourti, J.F. MacGregor, Process analysis, monitoring and diagnosis, using multivariate projection methods, Chemometrics and Intelligent Laboratory Systems 28 (1) (1995) 3–21.

[48] M. Vanhoucke, Dynamic scheduling: integrating schedule risk analysis with earned value management, The Measurable News 2 (2012) 11–13.

[49] DecisionEdge, http://www.decisionedge.com/2014.

[50] P2 EngineVisit the P2 Engine website at www.p2engine.com (Jan. 2013).

[51] D.S. Lee, J.M. Park, P.A. Vanrolleghem, Adaptive multiscale principal component analysis for on-line monitoring of a sequencing batch reactor, Journal of Biotechnology 116 (2) (2005) 195.

[52] P. Nomikos, J.F. MacGregor, Multivariate SPC charts for monitoring batch processes, Technometrics 37 (1) (1995) 41–59.

[53] P.R. Nelson, J.F. MacGregor, P.A. Taylor, The impact of missing measurements on PCA and PLS prediction and monitoring applications, Chemometrics and Intelligent Laboratory Systems 80 (1) (2006) 1–12.

[54] R.J. Hyndman, Y. Fan, Sample quantiles in statistical packages, The American Statistician 50 (4) (1996) 361–365.

[55] E. Demeulemeester, M. Vanhoucke, W. Herroelen, Rangen: a random network generator for activity-on-the-node networks, Journal of Scheduling 6 (2003) 17–38.

[56] E. Orta, M. Ruiz, N. Hurtado, D. Gawn, Decision-making in IT service management: a simulation based approach, Decision Support Systems 66 (2014) 36–51.

[57] D. Arnott, G. Pervan, Eight key issues for the decision support systems discipline, Decision Support Systems 44 (2008) 657–672.

[58] M. Vanhoucke, An overview of recent research results and future research avenues using simulation studies in project management, ISRN Computational Mathematics (2013) 1–19 Article ID513549.

[59] Y.H. Kwak, L. Ingall, Exploring Monte Carlo simulation applications for project management, Risk Management 9 (1) (2007) 44–57.

[60] T. Williams, The contribution of mathematical modelling to the practice of project management, IMA Journal of Management Mathematics 14 (1) (2003) 3–30.

[61] R Core Team, R: A Language and Environment for Statistical Computing, R Foundation for Statistical Computing, Vienna, Austria, 2013 URL http://www.R-project.org.

[62] C. Loch, A. De Meyer, M. Pich, Managing the unknown: a new approach to managing high uncertainty and risk in project, John Wiley and Sons, Inc., New Jersey, 2006.

[63] S. AbouRizk, D. Halpin, J. Wilson, Fitting beta distributions based on sample data, Journal of Construction Engineering and Management 120 (1994) 288–305.

[64] M.E. Kuhl E.K. Lada N.M. Steiger M.A. Wagner LR. Wilson Introduction to modeling and generating probabilistic input processes for simulation, in: S. Henderson, B. Biller, M. Hsieh, I. Shortle. I. Tew, R. Barton (Eds.). Proceedings of the 2007 Winter Simulation Conference, Institute of Electrical and Electronics Engineers, New Jersey 2007, pp. 63–76.

[65] W.J. McBride, C.W. McClelland, Pert and the beta distribution, IEEE Transactions on Engineering Management 14 (4) (1967) 166–169.

[66] D. Trietsch, L. Mazmanyan, L. Govergyan, K.R. Baker, Modeling activity times by the Parkinson distribution with a lognormal core: theory and validation, European Journal of Operational Research 216 (2012) 386–396.

[67] A.N. Pettitt, M.A. Stephens, The Kolmogorov–Smirnov goodness-of-fit statistic with discrete and grouped data, Technometrics 19 (2) (1977) 205–210.

[68] G. Marsaglia, W.W. Tsang, J. Wang, Evaluating Kolmogorov's distribution, Journal of Statistical Software 8 (18) (2003) 1–4.

[69] T. Hastie, R. Tibshirani, J. Friedman, T. Hastie, J. Friedman, R. Tibshirani, The Elements of Statistical Learning, vol. 2Springer, 2009.

Jeroen Colin is a research assistant at the Operations Management group of the Faculty of Economics and Business Administration at Ghent University (Belgium). He obtained a Master's degree in Civil Engineering at Ghent University and has joined the OR&S group in 2009.

His research interest lies in dynamic project scheduling and control using statistical pro ject control and more advanced statistical techniques. Most of his work has been presented at EVM Europe and other international conferences. He is also responsible for the exercise teaching sessions of the Production Management course.

Annelies Martens is a research assistant at the Operations Management group of the Faculty of Economics and Business Administration at Ghent University (Belgium). She obtained a Master's degree in Commercial Engineering at UGent and has joined the OR&S group in 2014.

Her research interest lies in the optimization and the integration of risk management and project control.

Mario Vanhoucke is a Professor of Business Management and Operations Research at Ghent University (Belgium), Vlerick Business School (Belgium, Russia, China) and University College London (UK). He has a PhD in Operations Management from the University of Leuven (Belgium) and a Master's degree in Commercial Engineering from the University of Leuven (Belgium). He teaches Project Management, Business Statistics, Decision Sciences for Business and Applied Operations Research

His main research interest lies in the integration of project scheduling, risk management and project control using combinatorial optimization models. He is an advisor for several PhD projects, has published papers in various international publications and is the autho of three project management books published by Springer.

Mario Vanhoucke is also a founding member and Director of the EVM Europe Association (, www.evm-europe.eu). He is also a partner in the company OR–AS which has released a commercial project management software tool ProTrack 3.0 as well as a research PM soft ware engine P2 Engine. He also works on an online learning tool PM Knowledge Center

Mathieu Wauters is a research assistant at the Operations Management group of the faculty of Economics and Business Administration at Ghent University (Belgium). He obtained a Master's degree in Commercial Engineering at Ghent University and has joined the OR&S group in 2010

His research interest lies in the optimization of time/cost trade-offs in project scheduling and its link to project control using Earned Value Management, and has published several papers in international journals. He has presented his work at the Project Management and Scheduling conference. He has been responsible for the exercise teaching sessions of the Proiect Management course
