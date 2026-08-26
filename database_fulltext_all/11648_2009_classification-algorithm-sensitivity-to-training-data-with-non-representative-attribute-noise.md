---
otero_id: 11648
otero_key: "EYVEVBB7"
title: "Classification algorithm sensitivity to training data with non representative attribute noise"
authors: "Michael Mannino; Yanjuan Yang; Young Ryu"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.11.021"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Classi<sup>fi</sup>cation algorithm sensitivity to training data with non representative attribute noise

Michael Mannino <sup>a,</sup>⁎, Yanjuan Yang <sup>a</sup>, Young Ryu <sup>b</sup>

<sup>a</sup> The Business School, University of Colorado Denver, Denver, CO 80217, USA

<sup>b</sup> School of Management, University of Texas at Dallas, Richardson, Texas 75083-0688, USA

## a r t i c l e i n f o

Article history: Received 19 November 2007 Received in revised form 17 November 2008 Accepted 22 November 2008 Available online 3 December 2008

Keywords: Attribute noise Area under the Receiver Operating Curve Classification algorithm

## a b s t r a c t

We present an empirical comparison of classi<sup>fi</sup>cation algorithms when training data contains attribute noise levels not representative of <sup>fi</sup>eld data. To study algorithm sensitivity, we develop an innovative experimental design using noise situation, algorithm, noise level, and training set size as factors. Our results contradict conventional wisdom indicating that investments to achieve representative noise levels may not be worthwhile. In general, over representative training noise should be avoided while under representative training noise is less of a concern. However, interactions among algorithm, noise level, and training set size indicate that these general results may not apply to particular practice situations.

© 2008 Elsevier B.V. All rights reserved.

## 1. Introduction

Classi<sup>fi</sup>cation algorithms have become important tools to support organizational decision making. Successful applications of classi<sup>fi</sup>cation in business decision making have been reported for fault diagnosis in semiconductor manufacturing, loan approval, bank failure prediction, and industry and occupation code prediction. The primary goal of a classi<sup>fi</sup>cation algorithm is to perform at the same level as human experts. Classi<sup>fi</sup>cation algorithms can provide many bene<sup>fi</sup>ts to an organization such as reducing decision making time, improving the consistency of decisions, and reducing dependence on scarce human experts.

Classi<sup>fi</sup>cation algorithms, like other inductive methods, can be sensitive to data quality. In particular, attribute noise can have a signi<sup>fi</sup>cant impact on the performance of a classi<sup>fi</sup>cation algorithm. Attribute value errors in a training set can cause a classi<sup>fi</sup>cation algorithm to form a rule with an incorrect state for an input, while errors in cases to be classi<sup>fi</sup>ed can cause the wrong rule to be used. Attribute noise includes errors from incorrectly measuring an input, wrongly reporting the state of an input, relying on stale values, and using imprecise measurement devices. Error rates in large data sets can be larger than 5% unless careful measures are taken to reduce errors [22,32]. Redman [31] reported error rates for credit records as high as 30% with some recent anecdotal evidence [24] to con<sup>fi</sup>rm this high error rate.

This study involves evaluation of asymmetric attribute noise on classi<sup>fi</sup>cation algorithm performance. Asymmetric means that noise levels in training data are signi<sup>fi</sup>cantly different than noise levels when a classi<sup>fi</sup>er is deployed in the <sup>fi</sup>eld. The conventional wisdom on classi<sup>fi</sup>er design is to replicate <sup>fi</sup>eld noise in training data. This research considers situations when noise levels are different. When training data is obtained from experts or through new data collection, it is dif<sup>fi</sup>cult to account for noise levels in the <sup>fi</sup>eld. The high cost of obtaining training data often necessitates relatively small training set sizes. Sampling error as a result of small, high-dimensional training sets can lead to substantial differences in noise between training and <sup>fi</sup>eld data. When training data is obtained from historical data, the quality of the data may be unknown. In addition, disruptions in the environment can change noise levels encountered in the <sup>fi</sup>eld.

The decision support literature has anecdotal evidence indicating asymmetric noise between system development and system deployment. Kim and Choi [14] argue that errors in operational data may enter into decision support and archived data before detection can improve data quality in the operational sources. Since organizations may have a dif<sup>fi</sup>cult time to measure the costs and bene<sup>fi</sup>ts of data quality, data quality improvements may not occur until a costly event occurs such as a lawsuit, loss of sales, or personal injury. Demarest [8] argues that data warehouse operations are often impacted by poor data quality hidden in source systems. This lack of data quality in the operational systems has caused multiple decision support efforts to fail. Redman [30] argues that system designers are often not aware of process failures that allow poor quality data. Several others [17,34] indicate that the diversity of information providers makes prediction of data quality dif<sup>fi</sup>cult for system designers.

To study asymmetric attribute noise effects, we develop an innovative experimental design with algorithm, noise level, and training set size as factors and relative performance change as the performance measure. We consider under representative training noise (low training noise and high test noise) and over representative training noise (high training noise and low test noise). For noise generation, we study uniform input noise levels on all attributes, variable noise levels, and noise levels assigned by attribute importance. We use two multiple factor research models with repeated measures to test individual factors and factor interactions. To provide a level of external validity, we conduct experiments with four large data sets having a diversity of data types, number of attributes, prevalence, and classi<sup>fi</sup>cation dif<sup>fi</sup>culty.

Our results indicate that over representative training noise should be avoided while under representative training noise is less of a concern. Cleaning <sup>fi</sup>eld data improved performance in the experiments except when a data set was dif<sup>fi</sup>cult to classify by an algorithm. However, interactions among algorithm, noise level, and training set size indicate that these general results may not apply to particular practice situations. In comparisons of relative sensitivity of <sup>fi</sup>ve prominent classi<sup>fi</sup>cation algorithms to asymmetric noise, the most common result was no signi<sup>fi</sup>cant relative sensitivity. However, interactions among training set size and noise level indicates that differences may occur in practice.

This study has important implications for understanding classi<sup>fi</sup>- cation algorithm performance under asymmetric noise. Many business decision environments involve input noise especially involving data provided by outside parties. For example, errors in credit reports, census data, and court records are common. In noisy environments, robustness of algorithm performance can be more important than performance under laboratory conditions. This work is the <sup>fi</sup>rst systematic study to document differences in classi<sup>fi</sup>cation algorithm robustness under varying levels of asymmetric attribute noise and training set sizes.

This paper is organized as follows. Section 2 summarizes related work about theoretical noise models, empirical studies of sensitivity of classi<sup>fi</sup>cation algorithms to noise, and techniques to make classi<sup>fi</sup>cation algorithms robust to noise. Section 3 presents the experimental design to study the impacts of asymmetric noise. Section 4 analyzes the experimental results and discusses issues related to the results. Section 5 concludes the study.

## 2. Related work

A number of theoretical noise models have been proposed as extensions to the theory of Probably, Approximately Correct (PAC) learning. The goal of PAC theory is to derive an upper bound on the number of examples needed to approximately learn a concept within a given error bound and con<sup>fi</sup>dence level. Noise models have been classi<sup>fi</sup>ed by source (random or adversary) and target (attribute versus class). Table 1 summarizes some important theoretical results about noise models. For discrete input spaces and speci<sup>fi</sup>ed concept spaces, these results have established the amount of noise that can be tolerated and the number of examples required to learn a concept. Since this work involves attribute noise, the most important results are in [16] (attribute importance effect on noise impact) and [12] (product attribute noise effects). The research framework in section 3 provides hypotheses to empirically test these theoretical results.

Table 1  
Summary of theoretical results about noise impacts

<table><tr><td>Reference</td><td>Noise model</td><td>Significant results</td></tr><tr><td>[16]</td><td>Bernoulli noise process</td><td>Class and attribute noise model; attribute importance influences learning difficulty</td></tr><tr><td>[12]</td><td>Uniform attribute noise, product attribute noise</td><td>Product attribute noise is almost as harmful as class noise</td></tr><tr><td>[7]</td><td>Hybrid noise model</td><td>Noise model combining attribute and class noise; robustness of statistical query learning algorithms to hybrid noise</td></tr><tr><td>[3]</td><td>Nasty noise model</td><td>Noise model generalizing malicious noise; bounds on accuracy and number of examples</td></tr><tr><td>[6]</td><td>Uniform distribution attribute noise</td><td>Noisy distance measure; robust Fourier learning algorithm</td></tr></table>

In early applied studies, researchers developed pruning procedures [19] to re<sup>fi</sup>ne the rule set generated by a learning algorithm. Pruning techniques reduce specialization by eliminating rules in whole or part. Similarly, pruning techniques have also been found useful to handle noise because noise in a training set can lead to extra rules and highly specialized rules. Several techniques have been developed that use a single parameter to control the amount of pruning (error complexity pruning [2] and m-probability-estimate pruning [4]). No guidelines were provided for setting parameter values except that high values should be used when there is a large amount of noise.

In some of the earliest studies on the effects of noise, Quinlan [26,27] found sensitivity of the ID3 decision tree induction algorithm to attribute noise. He demonstrated that the classi<sup>fi</sup>cation accuracy of ID3 was worse for a noise-free training set if the level of <sup>fi</sup>eld noise is high (45% or greater). We extend Quinlan's basic result to more representative levels of noise (below 30%) with additional noise situations (under and over representation of attribute noise), additional factors, and more learning algorithms.

In contrast to pruning techniques and noisy training data, Mannino et al. [18] investigated explicit noise handling using clean training data along with a noise parameter. Explicit noise handling adds noise to clean training data in a controlled manner using the noise parameter. The study demonstrated both analytically and empirically that explicit noise handling has the same expected performance but lower variance than traditional techniques using noisy training data. However, there was no investigation of the main issue of this paper, asymmetric noise levels between training and <sup>fi</sup>eld data.

Two recent empirical studies have focused on attribute noise. Nolan [20] empirically studied the effect of attribute noise on several prominent classi<sup>fi</sup>cation algorithms (C5.0, back propagation neural network, and linear discriminate analysis). He found that the neural network performed signi<sup>fi</sup>cantly better than the other algorithms when noise levels exceeded 10%. His study did not consider many aspects of this research including asymmetric noise levels, different noise rates among attributes, training set size, attribute importance, and relative performance differences rather than absolute performance differences.

In the most closely related study, Zhu and Wu [37] studied the effects of data cleaning on the performance of C4.5. They compared predictive accuracy of C4.5 on combinations of clean and noisy training and test sets. The emphasis in their study is the value of data cleaning either in training data or <sup>fi</sup>eld data. They reached a number of conclusions that are counter to the conventional wisdom established in [26,27] that training data should contain noise representative of <sup>fi</sup>eld data. Our study emphasizes asymmetric levels of noise not cleaning activities, employs a wider set of algorithms along with training set size as factors, uses more re<sup>fi</sup>ned performance measures, and provides a more carefully designed experimental procedure.

Much work has focused on methods to combine classi<sup>fi</sup>er decision to improve performance especially in the presence of classi<sup>fi</sup>cation noise. Ensemble methods combine weak classi<sup>fi</sup>ers using a voting scheme with optional weighting of classi<sup>fi</sup>er decisions. Although some work [9,29] has shown that ensemble methods are susceptible to classi<sup>fi</sup>cation noise and malicious noise, there are no reported results for asymmetric attribute noise.

The debate about the Receiver Operating Characteristic (ROC) curve [25] as a performance measure independent of class prevalence has some similarities with the theme of this research. ROC curves are independent of class prevalence changes if the distribution of cases within each class remains constant. Webb and Ting [35] argue that ROC curves in a training environment may not be realized in practice because class prevalence changes are often accompanied by other environmental changes. Fawcett and Flach [10] counter argue that in many important applications, class prevalence changes are not accompanied by other environmental changes so ROC curves in training will likely hold in practice. Both works address the motivation behind this paper that asymmetry between training and practice environments deserves careful study.

## 3. Research methodology

This section describes the research questions and methodology employed to test the research questions. We describe the hypotheses, framework, experiment design, experiment control procedure, and data sets.

## 3.1. Research questions and framework

The conventional wisdom about attribute noise as established in [26,27] is that training data should contain noise representative of <sup>fi</sup>eld data. A more recent study [37] indicates that training data should be clean regardless of the noise in <sup>fi</sup>eld data. Our goal is to extend these studies with a focus on different levels of noise in training and <sup>fi</sup>eld deployment. As described in the following points, we use a range of classi<sup>fi</sup>cation algorithms, training set sizes, and more re<sup>fi</sup>ned performance measures to extend the results in these studies.

• Training data with non representative noise levels: We want to characterize the relationship between noise level and performance degradation. An improved understanding of performance degradation may provide guidance about investment decisions for acquisition of training data countering the conventional wisdom that a mismatch between training and <sup>fi</sup>eld noise levels is detrimental. If over representation of noise is harmful, an organization may want to remove excessive noise if <sup>fi</sup>eld data is relatively clean. If under representation is not harmful, an organization should not expend resources to obtain a training set with noise representative of <sup>fi</sup>eld data.

• Cleaning <sup>fi</sup>eld data: Organizations may also consider investments to improve the quality of <sup>fi</sup>eld data. We want to characterize the relationship between noise level and performance improvements from cleaning of <sup>fi</sup>eld data. Cleaning <sup>fi</sup>eld data is more expensive than training data so organizations may want to see signi<sup>fi</sup>cant performance improvements before improving data quality. Qualitatively, an organization may want to know how much noise should be removed to improve classi<sup>fi</sup>er performance.

• Tolerance of asymmetric noise by popular classi<sup>fi</sup>cation algorithms: Because ensemble methods have more tolerance for classi<sup>fi</sup>cation noise, we expect that ensemble classi<sup>fi</sup>ers will be more tolerant of asymmetric attribute noise than other classi<sup>fi</sup>ers. Beyond this expectation, the study will evaluate the sensitivity of popular classi<sup>fi</sup>cation algorithms to different levels of asymmetric attribute noise.

• Interaction of training set size and asymmetric attribute noise: Learning curves and training set size have been carefully studied because of the expense of collecting training data. Interaction of training set size with asymmetric noise is important for justifying investment decisions in training data. We expect to see more sensitivity to asymmetric attribute noise on small training sets than medium and large training sets.

• Impact of noise variation (uniform with the same noise level on all attributes versus variable with different noise levels) and attribute importance: Previous theoretical studies have demonstrated more harm due to variable noise on important attributes [12,16]. We expect that variable asymmetric attribute noise will lead to more performance degradation than uniform asymmetric noise. Asymmetric attribute noise directed towards important attributes should have more effect than asymmetric attribute noise that is randomly directed.

To study these research questions, we use a framework involving comparisons between different levels of training and testing noise as depicted in Table 2. Test noise levels indicate actual noise encountered in classi<sup>fi</sup>er deployment in the <sup>fi</sup>eld. Our major interest is in situations of under or over representation of noise in training data. For intraalgorithm comparisons, we use absolute performance differences where $A U C _ { i j }$ denotes area under the receiver operating curve under the speci<sup>fi</sup>ed levels of training (i) and test noise (j). For over representative training noise, we use $A U C _ { H L } – A U C _ { L L }$ (high training noise and low test noise). For under representative training noise, we use $A U C _ { L H ^ { - } } A U C _ { H H }$ (low training noise and high test noise). For comparisons across classi<sup>fi</sup>cation algorithms, we use relative performance differences to focus on noise impact, not other differences among classi<sup>fi</sup>cation algorithms. We use $\frac { \hat { A } U C _ { H L } - A U C _ { L L } } { A U C _ { L L } }$ for over representative training noise levels and $\frac { A U C _ { L H } - A U C _ { H H } } { A U C _ { H H } }$ for under representative training noise levels. Classi<sup>fi</sup>cation algorithms are evaluated for zero and non-zero levels of low noise with the noise level difference (high– low) constant in both cases.

We are also interested in situations in which cleaning can be done in <sup>fi</sup>eld data. For intra algorithm comparisons, we use $A U C _ { H L ^ { - } } A U C _ { H H }$ for cleaning <sup>fi</sup>eld data. Since we do not actually clean test data, the noise difference between training and test data is handled using the noise level difference factor explained later in this section. If cleaning <sup>fi</sup>eld data improves performance, additional cleaning of training data is covered by the case of over represented training noise.

Noise level difference, training set size, and classi<sup>fi</sup>cation algorithms are used as factors. Because establishing an easily understood functional relationship is dif<sup>fi</sup>cult, we use discrete noise level differences (low: 0 to 0.05, medium: 0.10 to 0.15, and high: 0.20 to 0.25). We randomly choose the noise level difference from a uniform distribution between the speci<sup>fi</sup>ed end points. Because noise levels are not under control of the data mining professional, we randomly vary the levels rather than setting <sup>fi</sup>xed levels of noise. Two training set sizes are used (low: 200 and high: 1000). Since training set size is often controllable by the data mining professional, constant values are used. We use <sup>fi</sup>ve popular classi<sup>fi</sup>cation algorithms having different approaches about concept representation and search: decision tree induction, logistic regression, nearest neighbors, support vector machine, and a meta classi<sup>fi</sup>er using bagging and boosting.

Noise levels are assigned to attributes as uniform noise (same noise level on all attributes), variable noise (different noise levels on attributes), and importance sampled noise (noise level selected by attribute importance). For each observation, a noise difference is randomly selected from a uniform distribution between the speci<sup>fi</sup>ed ranges. For uniform noise, zero and non-zero levels of low noise are considered. With zero-level low noise, the high noise level is the noise difference. For non zero-level low noise, the high level is chosen by randomly selecting a value between the noise difference and 25% larger than the noise difference. The low noise level is the high noise level minus the noise difference. For the variable noise variation, each attribute is randomly assigned a noise level from a uniform distribution between the noise difference and the high noise level used in the uniform noise case. The low noise level is the difference between the randomly assigned high noise level and the noise difference. For importance noise variation, the noise levels used in the variable case are sorted in ascending order. Noise levels are assigned according to attribute importance (largest noise level to the most important attribute) or reverse attribute importance (smallest noise

## Table 2

Asymmetric noise situations

<table><tr><td rowspan="2">Training noise</td><td colspan="2">Test noise</td></tr><tr><td>Low</td><td>High</td></tr><tr><td>Low</td><td> $AUC_{LL}$ </td><td> $AUC_{LH}$ </td></tr><tr><td>High</td><td> $AUC_{HL}$ </td><td> $AUC_{HH}$ </td></tr></table>

level to the most important attribute). Attribute importance is determined by the Ranker search method with information gain as the evaluation function available in Weka [36].

## 3.2. Experiment design and procedure

Our experiment design emphasizes internal validity about conclusions on individual data sets. We use a repeated measures design to investigate noise impacts on individual algorithms (intra-algorithm experiments) and sensitivity to noise among algorithms (interalgorithm experiments). For each experiment, we repeat the randomly determined factor levels (noise level and training set size). In addition, we control the composition of cases in observations consisting of a pair of a training set and a test set. Given the number of factors and the need to isolate the impact of noise on training and test data, an emphasis on internal validity seems appropriate. We could not achieve a high level of internal validity if we had used the individual data set as an observation. We provide some insights about external validity (across data sets) by repeating the experiments on different data sets.

The primary set of experiments applies to intra-algorithm performance using noise situation, noise level difference, and training set size as factors as shown in Table 3. An observation involves a combination of a training set and a test set chosen by sampling without replacement from a classi<sup>fi</sup>ed data set. A randomly selected noise difference level is applied to a training (TR) and a test set (TS) as indicated by a noise situation $( \mathrm { T R _ { L } } \mathrm { - } \mathrm { T S _ { L } } , \mathrm { T R _ { L } } \mathrm { - } \mathrm { T S _ { H } } , \mathrm { T R _ { H } } \mathrm { - } \mathrm { T S _ { L } } , \mathrm { T R _ { H } } \mathrm { - } \mathrm { T S _ { H } } ) .$ For example, the cell b200, Low, $\mathrm { T R _ { L } } \mathrm { - } \mathrm { T S _ { H } } \mathrm { > }$ involves a training set size of 200, a low noise level difference, and a noise situation of lower training noise and higher test noise. Thus, each cell in Table 3 contains 240 observations for the speci<sup>fi</sup>ed training set size and noise level difference applied to four noise situations. The test set size is two times the training set size. Since we use large data sets, data availability is not a problem for the training and test sets. After generating noise, a classi<sup>fi</sup>er is generated using the speci<sup>fi</sup>ed classi<sup>fi</sup>cation algorithm and training set.

An observation is the performance of the speci<sup>fi</sup>ed classi<sup>fi</sup>er on the test set. To control for unwanted variance due to different factor values among observations, identical training/test sets are used for each noise situation and noise level and identical noise levels are used for each training set size. A separate experiment is conducted for each classi<sup>fi</sup>cation algorithm.

The cells with identical noise situations $\mathrm { ( T R _ { L } { - } T S _ { L } \ o r \ T R _ { H } { - } T S _ { H } ) }$ in Table 3 are used to compute the performance measures in Table 2. For example, the measure $A U C _ { H L ^ { - } } A U C _ { L L }$ is computed using results from noise situations $\mathrm { T R } _ { \mathrm { H } } { - } \mathrm { T } S _ { \mathrm { L } }$ and $\mathrm { T R } _ { \mathrm { L } } { - } \mathrm { T } S _ { \mathrm { L } }$ . Thus differences in observations are the basis for the intra-algorithm statistical testing described in section 4.1.

For inter-algorithm comparisons, we use a slightly different design with relative performance change as the dependent variable. We perform pairwise comparisons among algorithms using a mix of training set sizes (200 and 1000) and noise level differences (low, medium, and high). We use 60 paired observations for a speci<sup>fi</sup>ed combination of noise level difference and training set size applied to <sup>fi</sup>ve classi<sup>fi</sup>cation algorithms (J4.8, AdaBoostM1, Support Vector, Nearest Neighbor, and Logistic Regression). Thus, an experiment involves a total of 360 (6×60) paired observations for each classi<sup>fi</sup>cation algorithm. A paired observation involves the same training and testing set for each classi<sup>fi</sup>cation algorithm. A separate experiment is conducted for each noise situation (over-representative and underrepresentative training noise and cleaning <sup>fi</sup>eld data) and data set. If a noise situation is found not signi<sup>fi</sup>cant in the intra algorithm experiment, it can be dropped in the inter-algorithm experiment. Only variable noise is used in the inter-algorithm experiments.

Table 3  
Sample sizes for intra-algorithm experiments

<table><tr><td rowspan="2">Training set size</td><td colspan="3">Noise level difference</td></tr><tr><td>Low</td><td>Medium</td><td>High</td></tr><tr><td colspan="4">Noise situation</td></tr><tr><td>200</td><td></td><td></td><td></td></tr><tr><td> $TR_L-TS_L$ </td><td>60</td><td>60</td><td>60</td></tr><tr><td> $TR_L-TS_H$ </td><td>60</td><td>60</td><td>60</td></tr><tr><td> $TR_H-TS_L$ </td><td>60</td><td>60</td><td>60</td></tr><tr><td> $TR_H-TS_H$ </td><td>60</td><td>60</td><td>60</td></tr><tr><td>1000</td><td></td><td></td><td></td></tr><tr><td> $TR_L-TS_L$ </td><td>60</td><td>60</td><td>60</td></tr><tr><td> $TR_L-TS_H$ </td><td>60</td><td>60</td><td>60</td></tr><tr><td> $TR_H-TS_L$ </td><td>60</td><td>60</td><td>60</td></tr><tr><td> $TR_H-TS_H$ </td><td>60</td><td>60</td><td>60</td></tr></table>

Table 4  
Summary of data sets

<table><tr><td>Data set</td><td>Source</td><td>Characteristics</td></tr><tr><td>Adult</td><td>UCI repository [13]</td><td>14 attributes, mixed data types, 45,222 cases, about 25–75 class split (income level)</td></tr><tr><td>DGP</td><td>Generated by DGP/2 program from UCI repository</td><td>10,000 cases, 20 numeric attributes, 60–40 class split, 3 peaks per attribute</td></tr><tr><td>Bankruptcy</td><td>Bankruptcy data from S&amp;P Compustat North American database</td><td>12 numeric attributes, 12212 cases, about 97–3 class split (bankruptcy status)</td></tr><tr><td>Thoracic</td><td>United Network for Organ Sharing</td><td>19 tri state attributes, 13,326 cases, about 67–33 class split (thoracic transplant survival)</td></tr></table>

To execute the experiments, control software was developed in Microsoft Visual Studio. The control software randomly perturbs training and test data, builds classi<sup>fi</sup>ers using training data and selected classi<sup>fi</sup>cation algorithms, classi<sup>fi</sup>es test data using the classi<sup>fi</sup>ers, and calculates classi<sup>fi</sup>er performance. The experiment control program uses classi<sup>fi</sup>cation algorithms available in the Weka software for machine learning [36] and data sets stored as Oracle 10g tables. We selected <sup>fi</sup>ve popular algorithms available in Weka: J4.8 (C4.5 decision tree [28]), AdaBoostM1 (boosting classi<sup>fi</sup>er [11]), SMO (support vector machine classi<sup>fi</sup>er with polynomial kernel [15]), IBk (k nearest neighbor classi<sup>fi</sup>er [1]), and Logistic (Ridge logistic regression [5]). Separate experiments are executed for the large data sets described in Table 4. The data sets provide a mix of class distributions, data types, and classi<sup>fi</sup>cation dif<sup>fi</sup>culty (see Table 5 for average AUC scores with clean data).

Data perturbation occurs after determining the training set and testing set for an observation. For each attribute, a random number between 0 and 1 is drawn. If the number is less than or equal to the attribute's noise probability, the value is changed. If the attribute's scale is nominal, the value is randomly changed to any other value. If the attribute's scale is ordinal, the attribute is changed to an adjacent value. If the attribute is numeric (ratio or absolute scale), the value is changed using an equal height histogram with at most 10 ranges. A smaller number of ranges are used for highly skewed numeric attributes. After randomly selecting an adjacent cell of the equal height histogram, a value is randomly selected between the end points of the cell. The Oracle 10g DBMS\_Stats package [21] was used to create histograms for numeric attributes.

Table 5  
Average AUC results on clean data for each data set and algorithm

<table><tr><td>Dataset\algorithm</td><td>AdaBoost</td><td>J4.8</td><td>IBk</td><td>Logistic</td><td>SMO</td></tr><tr><td>Adult</td><td>0.868</td><td>0.769</td><td>0.817</td><td>0.832</td><td>0.857</td></tr><tr><td>Bank</td><td>0.786</td><td>0.528</td><td>0.594</td><td>0.747</td><td>0.626</td></tr><tr><td>DGP</td><td>0.548</td><td>0.549</td><td>0.591</td><td>0.530</td><td>0.525</td></tr><tr><td>Thoracic</td><td>0.709</td><td>0.653</td><td>0.692</td><td>0.722</td><td>0.713</td></tr></table>

Table 6  
Summary of pair-wise testing and error rate

<table><tr><td>Experiment</td><td>Pair-wise tests</td><td>Error rates</td></tr><tr><td>Intra algorithm</td><td>Six pair-wise tests for each noise situation</td><td> $\alpha_{\text{FM}}: 0.265, \alpha_{\text{CW}}: 0.05$ </td></tr><tr><td>Inter algorithm</td><td>10 pair-wise tests for each algorithm combination</td><td> $\alpha_{\text{FM}}: 0.401, \alpha_{\text{CW}}: 0.05$ </td></tr></table>

Executing the experiments was computationally intensive. For a given experiment, the number of times that training is performed is NUMOBS⁎NVLS where NUMOBS is the number of observations and NVLS is the number of noise variation levels (uniform with zero low noise, uniform nonzero noise, variable noise, importance assigned noise, and reverse importance assigned noise). For each intraalgorithm experiment, we have 7200 training executions (1440⁎5). For <sup>fi</sup>ve classi<sup>fi</sup>cation algorithms, we have 36,000 training executions. For each inter-algorithm experiment, we have 1800 (360⁎5) training executions. For four data sets and three noise situations, we have 21,600 training executions (1800⁎12).

## 4. Analysis of results

This section presents the experiment results and discusses insights from the analysis. The signi<sup>fi</sup>cance of the intra and inter-algorithm models is evaluated followed implications of the study on investment decisions in training data.

## 4.1. Evaluation of models

Testing the models speci<sup>fi</sup>ed in section 3.2 involved a family statistical test using ANOVA and a collection of post-hoc or pair-wise comparison tests (www.statistics.com). For the intra-algorithm experiments, we were interested in six comparisons (two training set sizes times three noise level differences) under three noise situations (under representative training noise, over representative training noise, and cleaned <sup>fi</sup>eld data). Since each noise situation uses a different sample, we need to adjust the Type I error rate (α) for the comparison-wise and family-wise error rates<sup>1</sup>. We chose to control the comparison error rate at the traditional 0.05 level and accept a somewhat elevated family error rate as shown in Table 6. For the interalgorithm experiments, we had 10 possible algorithm pairs to test.

## 4.1.1. Intra-algorithm results

The intra-algorithm experimental results show a complex pattern for under and over representative training noise but a clearer pattern for cleaning <sup>fi</sup>eld data as shown in Table 7. Overall, the results partially contradict previous results about training data noise [26,27,37] while supporting results about <sup>fi</sup>eld noise [37]. The additional level of detail in our experiments provides a more complete and rigorous analysis than offered in previous research.

For the two easier data sets (Adult and Thoracic), over representative training noise $( A U C _ { H L } – A U C _ { L L } )$ is usually signi<sup>fi</sup>cant. High training set size in<sup>fl</sup>uences signi<sup>fi</sup>cance for SMO (Adult data set) and Logistic (Adult and Thoracic data sets) indicating that small training sets may not capture enough patterns for these algorithms. On the Adult data set, J4.8 is signi<sup>fi</sup>cant only at low noise level differences possibly due to the lower performance on clean data for J4.8 than the other algorithms (Table 5).

For the two more dif<sup>fi</sup>cult data sets (Bank and DGP), over representative training noise is usually not signi<sup>fi</sup>cant. J4.8 is signi<sup>fi</sup>cant for both data sets when training set size and noise level difference are both high, while IBk is signi<sup>fi</sup>cant for the arti<sup>fi</sup>cial DGP data. The Bank data set is dif<sup>fi</sup>cult due to its high skew with some algorithms able to cope with the skew. The DGP data is dif<sup>fi</sup>cult for all algorithms as shown in Table 5.

For three data sets (Adult, Bank, and DGP), under representative training noise $( A U C _ { L H ^ { - } } A U C _ { H H } )$ is usually not signi<sup>fi</sup>cant. Table 7 shows some exceptions for large training sets and high noise levels especially for IBk. For the Thoracic data set, under representative training noise is usually signi<sup>fi</sup>cant with the exception of J4.8 and SMO. J4.8 is the lowest performing algorithm on the Thoracic data set.

The results for cleaning <sup>fi</sup>eld data partially con<sup>fi</sup>rm the results in [37]. Cleaning <sup>fi</sup>eld data always signi<sup>fi</sup>cantly improves performance for the easier data sets (Adult and Thoracic). For the dif<sup>fi</sup>cult data sets (Bank and DGP), cleaning <sup>fi</sup>eld data has mixed results. Cleaning <sup>fi</sup>eld data is only signi<sup>fi</sup>cant for large training sets for the Bank data set for

Summary of intra-algorithm test results

<table><tr><td colspan="2">Dataset\alg</td><td>Over (training)</td><td>Under (training)</td><td>Cleaning (field)</td></tr><tr><td rowspan="5">Adult</td><td>J4.8</td><td>Significant when noise level is low (0.010, 0.77)</td><td>Not significant</td><td>Significant (0.000, 2.05)</td></tr><tr><td>AdaBoost</td><td>Significant (0.000, 1.70)</td><td>Not significant</td><td>Significant (0.000, 2.85)</td></tr><tr><td>SMO</td><td>Significant when  $TS_{H}-NL_{L}$  (0.003, 1.65)</td><td>Not significant</td><td>Significant (0.000, 1.48)</td></tr><tr><td>IBk</td><td>Significant (0.000, 1.34)</td><td>Significant for uniform and variable noise (0.015, 0.73)</td><td>Significant (0.000, 1.36)</td></tr><tr><td>Logistic</td><td>Significant when training set size is high (0.008, 1.28)</td><td>Significant when training set size is high (0.021, 0.71)</td><td>Significant (0.000, 1.87)</td></tr><tr><td rowspan="5">Bank</td><td>J4.8</td><td>Significant when  $TS_{H}-NL_{L}$  (0.013, 0.93)</td><td>Significant when  $TS_{H}-NL_{L}$  (0.022, 0.88)</td><td>Significant when training set size is high (0.009, 1.78)</td></tr><tr><td>AdaBoost</td><td>Not significant</td><td>Not significant</td><td>Significant when training set size is high (0.000, 2.05)</td></tr><tr><td>SMO</td><td>Not significant</td><td>Not significant</td><td>Not significant</td></tr><tr><td>IBk</td><td>Not significant</td><td>Not significant</td><td>Significant when training set size is high (0.003, 1.92)</td></tr><tr><td>Logistic</td><td>Not significant</td><td>Significant when  $TS_{L}-NL_{H}$  (0.012, 0.96)</td><td>Significant when training set size is high (0.003, 1.73)</td></tr><tr><td rowspan="5">DGP</td><td>J4.8</td><td>Significant when  $TS_{H}-NL_{H}$  (0.000, 1.32)</td><td>Significant when  $TS_{H}-NL_{H}$  (0.003, 1.48)</td><td>Significant when training set size is high (0.001, 1.65)</td></tr><tr><td>AdaBoost</td><td>Not significant</td><td>Not significant</td><td>Significant (0.000, 1.60)</td></tr><tr><td>SMO</td><td>Not significant</td><td>Not significant</td><td>Not significant</td></tr><tr><td>IBk</td><td>Significant (0.005, 1.71)</td><td>Significant when training set size is high (0.010, 0.78)</td><td>Significant except for  $TS_{L}-NL_{L}$  and  $TS_{L}-NL_{M}$  (0.009, 1.04)</td></tr><tr><td>Logistic</td><td>Not significant</td><td>Not significant</td><td>Not significant</td></tr><tr><td rowspan="5">Thoracic</td><td>J4.8</td><td>Significant (0.000, 1.55)</td><td>Not significant</td><td>Significant (0.000, 1.33)</td></tr><tr><td>AdaBoost</td><td>Significant (0.000, 1.47)</td><td>Significant (0.003, 1.21)</td><td>Significant (0.000, 1.65)</td></tr><tr><td>SMO</td><td>Significant (0.011, 0.86)</td><td>Significant when  $TS_{H}-NL_{H}$  for uniform and importance noise (0.022, 0.72)</td><td>Significant (0.001, 1.26)</td></tr><tr><td>IBk</td><td>Significant (0.000, 2.06)</td><td>Significant (0.018, 0.77)</td><td>Significant (0.000, 1.45)</td></tr><tr><td>Logistic</td><td>Significant when training set size is high for uniform, variable noise (0.019, 0.72)</td><td>Significant (0.008, 1.47)</td><td>Significant (0.003, 1.63)</td></tr></table>

Each cell summarizes 30 test results (3 noise level differences×2 training set sizes×5 noise variations). A cell is labeled signi<sup>fi</sup>cant if all results meet the 0.05 α level. The numbers in parentheses are the median p-values and effect sizes computed using the Hedge's g measure, An effect size of 0.8 is considered large

![](/api/attachments/EYVEVBB7/fulltext/images/80d22916c87526e034b311a7f7849408d50ade9c1f2a1f5a852ec434ce3e941d.jpg)  
Fig. 1. Over representative training noise results for J4.8 with the Adult data set.

all algorithms except SMO. The DGP results are highly mixed with SMO and Logistic not signi<sup>fi</sup>cant for any factors, J4.8 only signi<sup>fi</sup>cant with large training sets, and IBk signi<sup>fi</sup>cant for small training set sizes with low and moderate noise level differences.

Performance graphs con<sup>fi</sup>rm some of the results shown in Table 7. As shown in Figs. 1 and 2, the performance differences for over representative training noise disappear for J4.8 and AdaBoost in the Adult data set as the noise level difference increases for large training sets (LL-HL1000). For small training sets (LL-HL200), the results show unstable performance for both J4.8 and AdaBoost in situations of over representative training noise. For under representative training noise, the performance graphs con<sup>fi</sup>rm non signi<sup>fi</sup>cance as the graphs frequently cross for both J4.8 and AdaBoost (Figs. 3 and 4). The graphs show more instability for small training sets (HH-LH200) than large training sets (HH-LH1000).

In summary, training set size and data set dif<sup>fi</sup>culty seem to explain some con<sup>fl</sup>icting differences for over-representative, under-representative, and cleaned <sup>fi</sup>eld data. Noise level difference does not explain con<sup>fl</sup>icting results although noise level difference is important in the non-con<sup>fl</sup>icting results.

## 4.1.2. Inter-algorithm results

For the inter-algorithm comparison, we considered two noise situations (over-representative training noise and cleaned <sup>fi</sup>eld data) with variable noise. For over-representative training noise, a positive performance difference (algorithm 1–algorithm 2) means that algorithm 1 has less relative sensitivity than algorithm 2. Likewise, a negative performance difference means that algorithm 1 has more relative sensitivity than algorithm 2. Since the level of noise can be dif<sup>fi</sup>cult to control in a training set, less sensitivity is preferred. For cleaned <sup>fi</sup>eld data, a positive performance difference (algorithm 1– algorithm 2) means that algorithm 1 has more relative sensitivity than algorithm 2. These results can provide insights into the desirability of cleaning <sup>fi</sup>eld data because cleaning <sup>fi</sup>eld data for a more sensitive algorithm has more impact than cleaning <sup>fi</sup>eld data for a less sensitive algorithm.

![](/api/attachments/EYVEVBB7/fulltext/images/c1c79a80ef45c3007da61bf283e8a6cebfea6c0ba0df9fbe75e65f8d0ff8d2d2.jpg)  
Fig. 2. Over representative training noise results for AdaBoost with the Adult data set.

![](/api/attachments/EYVEVBB7/fulltext/images/8f9c33c0d8d624ec80f2604756e1b65319325ce081ddb2a514dc67a63dbe8a78.jpg)  
Fig. 3. Under representative training noise results for J4.8 with the Adult data set.

When comparing all algorithms, the inter-algorithm results are mixed as summarized in Table 8. The conclusions in Table 8 are based on signi<sup>fi</sup>cance counts for each data set as shown in Tables 9 and 10. A Count + value indicates the number of times a statistical test was signi<sup>fi</sup>cant comparing the algorithm to any other algorithm with a mean difference less sensitive. A Count 0 value indicates the number of times a statistical test was not signi<sup>fi</sup>cant comparing the algorithm to any other algorithm. For example in 24 statistical tests with over representative training noise, SMO is less sensitive in 16 tests but not signi<sup>fi</sup>cantly different in 8 tests. Most comparisons for the Adult data set are not signi<sup>fi</sup>cant as the Count 0 column counts are largest in all but two rows. Across data sets, IBk is more sensitive on three data sets (Adult, Thoracic, and DGP), while Logistic is more sensitive on the DGP and Thoracic data sets for over representative training noise. For cleaned <sup>fi</sup>eld data, Logistic regression is more sensitive on three data sets but less sensitive on one data set (DGP).

When comparing selected algorithm pairs, the inter-algorithm results provide more clarity as depicted in Table 11. The comparison is limited to algorithm pairs with close performance on clean data as reported in Table 5 for the two easier data sets (Adult and Thoracic). On the Adult data set, the results reinforce that AdaBoost is preferred to SMO but provide some doubt about the preference for IBk as compared to Logistic. On the Thoracic data set, the results provide some doubt that AdaBoost is a worse choice than SMO and Logistic but reinforce that Logistic is preferred to SMO.

Performance graphs provide some different conclusions than statistical tests as depicted in Figs. 5 and 6 on the Adult data set. Fig. 5 shows stacked bar graphs in which the height of a bar is the sum of the median relative AUC performance differences. J4.8 appears most sensitive in Fig. 5 although the statistical tests indicate that the relative performance difference between J4.8 and other algorithms is usually not signi<sup>fi</sup>cant. Likewise, the statistical conclusions for the cleaned <sup>fi</sup>eld data are not apparent in the bar graphs of Fig. 6. The learning algorithms appear equally sensitive in Fig. 6, contrary to results in Table 10 showing SMO and Logistic less sensitive.

![](/api/attachments/EYVEVBB7/fulltext/images/a61a922ae13e5fc39c8feab792a549106d4808daacfa9c92fe06e1bbe7120c61.jpg)  
Fig. 4. Under representative training noise results for AdaBoost with the Adult data set.

Table 9  
Table 8  
Summary of inter-algorithm test results

<table><tr><td>Data set</td><td>Over representative training noise</td><td>Cleaned field data</td></tr><tr><td>Adult</td><td>SMO is less sensitive than others. AdaBoost and IBk are more sensitive to noise than others.</td><td>Logistic is most sensitive. IBk is somewhat less sensitive than others.</td></tr><tr><td>Bank</td><td>Most differences are not significant. J4.8 is less sensitive than Logistic when training set size is high and noise level difference is medium.</td><td>Algorithm differences are significant when training set size is high. IBk and Logistic are more sensitive than others. SMO is less sensitive to noise.</td></tr><tr><td>DGP</td><td>Logistic is less sensitive than others. IBk is most sensitive to noise.</td><td>IBk is most sensitive to noise. SMO and Logistic are less sensitive to noise than others.</td></tr><tr><td>Thoracic</td><td>Logistic is less sensitive than others. IBk is most sensitive to noise.</td><td>Logistic is more sensitive to noise. IBk is less sensitive to noise.</td></tr></table>

Signi<sup>fi</sup>cance counts (α=0.05) for the Adult data set

<table><tr><td>Noise situation</td><td>Algorithm</td><td>Count +</td><td>Count -</td><td>Count 0</td></tr><tr><td rowspan="5">Over</td><td>J4.8</td><td>0</td><td>5 (0.008, 1.68)</td><td>19</td></tr><tr><td>AdaBoost</td><td>1 (0.014, 1.13)</td><td>10 (0.010, 1.34)</td><td>13</td></tr><tr><td>SMO</td><td>16 (0.027, 0.86)</td><td>0</td><td>8</td></tr><tr><td>IBk</td><td>2 (0.009, 1.31)</td><td>10 (0.028, 0.68)</td><td>12</td></tr><tr><td>Logistic</td><td>9 (0.026, 0.82)</td><td>3 (0.014, 1.12)</td><td>12</td></tr><tr><td rowspan="5">Cleaning</td><td>J4.8</td><td>4 (0.018, 1.12)</td><td>6 (0.028, 0.98)</td><td>14</td></tr><tr><td>AdaBoost</td><td>2 (0.009, 1.56)</td><td>8 (0.021, 0.77)</td><td>14</td></tr><tr><td>SMO</td><td>3 (0.009, 1.18)</td><td>9 (0.024, 0.82)</td><td>12</td></tr><tr><td>IBk</td><td>2 (0.012, 0.91)</td><td>10 (0.026, 0.78)</td><td>12</td></tr><tr><td>Logistic</td><td>22 (0.029, 0.73)</td><td>0</td><td>2</td></tr></table>

The numbers in parentheses are the median p-values and effect sizes computed using the Hedge's g measure. An effect size of 0.8 is considered large

The box charts in Figs. 7 and 8 indicate the dispersion of the performance measures in the intra and inter-algorithms experiments. The performance on the Bankruptcy data set shows most dispersion on both parts of the distribution. The wide dispersion may be due to the interaction of noise and high class skew. The box charts also show anomalous situations in which over-representative training noise can lead to improved performance and cleaning <sup>fi</sup>eld data can lead to worse performance. These anomalous situations are most pronounced for the Bankruptcy data set but exist to lesser degrees for the other data sets.

## 4.2. Discussion

Our results partially contradict previous results. Quinlan [26,27] found that under representative training noise is harmful at high levels of <sup>fi</sup>eld noise. Our results found that under representative training noise was typically not harmful. Zhu and Wu [37] found that over representative training noise was harmful and under represented training noise was bene<sup>fi</sup>cial. Our results con<sup>fi</sup>rm their conclusion about over representative training noise but do not con<sup>fi</sup>rm their results on under representative training noise. Our results con<sup>fi</sup>rm their results for cleaning <sup>fi</sup>eld data.

Signi<sup>fi</sup>cance counts (α=0.05) for the thoracic data set

<table><tr><td>Noise situation</td><td>Algorithm</td><td>Count +</td><td>Count -</td><td>Count 0</td></tr><tr><td rowspan="5">Over</td><td>J4.8</td><td>4 (0.032, 0.93)</td><td>7 (0.026, 0.81)</td><td>13</td></tr><tr><td>AdaBoost</td><td>8 (0.027, 0.78)</td><td>6 (0.026, 0.73)</td><td>10</td></tr><tr><td>SMO</td><td>10 (0.023, 0.92)</td><td>7 (0.013, 1.21)</td><td>7</td></tr><tr><td>IBk</td><td>0</td><td>20 (0.037, 0.68)</td><td>4</td></tr><tr><td>Logistic</td><td>18 (0.032, 0.92)</td><td>0</td><td>6</td></tr><tr><td rowspan="5">Cleaning</td><td>J4.8</td><td>6 (0.030, 0.75)</td><td>8 (0.038, 0.77)</td><td>10</td></tr><tr><td>AdaBoost</td><td>8 (0.028, 0.88)</td><td>14 (0.021, 1.05)</td><td>2</td></tr><tr><td>SMO</td><td>15 (0.035, 0.59)</td><td>2 (0.011, 1.18)</td><td>7</td></tr><tr><td>IBk</td><td>0</td><td>22 (0.039, 0.64)</td><td>2</td></tr><tr><td>Logistic</td><td>17 (0.037, 0.63)</td><td>0</td><td>7</td></tr></table>

The numbers in parentheses are the median p-values and median effect sizes computed using the Hedge's g measure, An effect size of 0.8 is considered large.

Table 11  
Summary of sensitivity for algorithm pair

<table><tr><td>Data set</td><td>Over representative training noise</td><td>Cleaned field data</td></tr><tr><td>Adult</td><td>AdaBoost (0.868) vs. SMO (0.857): strong evidence that AdaBoost is less sensitive;IBk (0.817) vs. Logistic (0.832): good evidence that Logistic is less sensitive</td><td>AdaBoost (0.868) vs. SMO (0.857): little evidence of sensitivity preferenceIBk (0.817) vs. Logistic (0.832): good evidence that Logistic is less sensitive</td></tr><tr><td>Thoracic</td><td>AdaBoost (0.709) vs. Logistic (0.722): some evidence that AdaBoost is less sensitive;AdaBoost (0.709) vs. SMO (0.713): some evidence that AdaBoost is less sensitive;SMO (0.713) vs. Logistic (0.722): strong evidence that Logistic is less sensitive</td><td>AdaBoost (0.709) vs. Logistic (0.722): strong evidence that AdaBoost is less sensitive;AdaBoost (0.709) vs. SMO (0.713): strong evidence that AdaBoost is less sensitive;SMO (0.713) vs. Logistic (0.722): a little evidence that SMO is less sensitive</td></tr></table>

The numbers in parentheses are the average performance on clean data from Table 5

Beyond these general results, our results indicate a complex pattern of algorithm performance in the presence of asymmetric attribute noise. The results provide much more detail about interactions among algorithm, noise level, and training set size than previous research [26,27,37]. In addition, our study had a more careful design with better performance measures and rigorous statistical methodology so our conclusions have more validity than these previous studies. Decision makers should note important exceptions for over representative training noise, under representative training noise, and cleaned <sup>fi</sup>eld data as shown in Table 12. The interactions among algorithm, noise level, and training set size indicate that these general results may not apply to particular practice situations.

Our results provide some practical advice to decision makers regarding the alignment of noise levels between training and <sup>fi</sup>eld data. Data mining professionals should use clean training data if the data can be obtained without much cost (such as from experts) even if <sup>fi</sup>eld data have noise. If there is substantial cost to cleaning training data, the cleaning cost may not be worthwhile. Unless a data mining professional expects little noise in the <sup>fi</sup>eld data, cleaning the training data is likely not to be worthwhile. Due to exceptions in Table 12, riskaverse decision makers should be concerned with both over representative and under representative training noise.

![](/api/attachments/EYVEVBB7/fulltext/images/359a0315892dad10eb66c28be05e48fc57ca176528814e931a4ade83f44445cf.jpg)  
Fig. 5. Median performance differences for over representative noise of the Adult data set. Legend: NLL: noise level low, NLM: noise level medium, NLH: noise level high, TSL: training set size low, TSH: training set size high.

![](/api/attachments/EYVEVBB7/fulltext/images/c0acb812f3f2e192de6bd2de6c077e762166c960256516ef85fdca9e13d0708d.jpg)  
Fig. 6. Median performance differences for cleaned <sup>fi</sup>eld data of the Adult data set. Legend: NLL: noise level low, NLM: noise level medium, NLH: noise level high, TSL: training set size low, TSH: training set size high.

![](/api/attachments/EYVEVBB7/fulltext/images/93a76e1910adc38f0c095921bc08c43d7fd4e96baab7f0f6508f5d387374f1f3.jpg)  
Fig. 7. Box charts for the over representative training noise situation. Legend: D—J4.8; A— Adaboost; S—SMO; N—IBk; L—Logistic regression; 1—Adult; 2—Bankruptcy; 3—DGP; 4— Thoracic.

![](/api/attachments/EYVEVBB7/fulltext/images/ea9c680009e2d2596ee555f1ac5811d33ef754a130947a0f6fb742a035a5f0aa.jpg)  
Fig. 8. Box charts for data cleaning situation. Legend: D—J4.8; A—Adaboost; S—SMO; N— IBk; L—Logistic regression; 1—Adult; 2—Bankruptcy; 3—DGP; 4—Thoracic.

Table 12  
Exceptions to general results

<table><tr><td>General result</td><td>Exceptions</td></tr><tr><td>Over representative training noise harmful</td><td>Only significant for low noise levels and large data sets for several algorithms on the Adult data set; Not significant for most factors on the Bank and DGP data sets</td></tr><tr><td>Under representative training noise not harmful</td><td>Significant for several algorithms on the Thoracic data set; Significant for uniform and variable noise with the IBk algorithm on the Adult data set</td></tr><tr><td>Cleaning field data beneficial</td><td>Mostly insignificant on the Bank and DGP data sets</td></tr></table>

Two minor surprises involved the lack of impact of noise variation and ensemble learning algorithms. Although we think that variable attribute noise is the most realistic approach, it was surprising not to see that uniform and importance sampled noise had little differential impact. The results did not show much evidence that ensemble methods (AdaBoost-M1) had less relative sensitivity than other learning algorithms.

The results of these experiments are consistent with the results in [23] about training set size and data set dif<sup>fi</sup>culty. Learning ef<sup>fi</sup>ciency varies by classi<sup>fi</sup>cation algorithm as shown in [23]. Similarly, the interaction of training set size and asymmetric attribute noise varies by algorithm. The experimental results suggest that data set dif<sup>fi</sup>culty, as evidenced by average AUC scores with clean data, in<sup>fl</sup>uences the effect of asymmetric attribute noise. Future research with more data sets and careful measurement of data set dif<sup>fi</sup>culty would be useful.

## 5. Conclusion

We presented an empirical comparison about asymmetric noise levels between training and <sup>fi</sup>eld environments. We developed an innovative experimental design with algorithm, noise level, and training set size as factors and relative performance change as the performance measure. We considered under representative training noise, over representative training noise, and cleaned <sup>fi</sup>eld data. For noise generation, we studied uniform input noise levels on all attributes, variable noise levels, and noise levels assigned by attribute importance. Our results indicated that over representative training noise should be avoided while under representative training noise was less of a concern. Cleaning <sup>fi</sup>eld data usually improved performance. However, the interactions among algorithm, noise level, and training set size indicate that these general results may not apply to particular practice situations.

This study with an emphasis on internal validity has limitations on conclusions in a wide variety of domains. To study the interactions of noise level differences and training set size, internal validity with controls about confounding effects was necessary. A follow-on experiment with an emphasis on data set characteristics such as dif<sup>fi</sup>culty and prevalence could provide additional explanation of classi<sup>fi</sup>er dif<sup>fi</sup>culty with asymmetric noise to complement this study. In addition, variations of learning algorithms could be studied to understand the impact of noise handling methods on asymmetric attribute noise. We are also interested in similar experiments to study malicious attribute noise with active adversaries creating noise.

## References

[1] D. Aha, D. Kibler, Instance-based learning algorithms, Machine Learning 6 (1991) 37–66.

[2] L. Breiman, J. Friedman, R. Olshen, C. Stone, Classi<sup>fi</sup>cation and Regression Trees Wadsworth Publishing, Belmont, CA, 1984.

[3] N. Bshouty, N. Eiron, E. Kushilevitz, PAC learning with nasty noise, Theoretical Computer Science 288 (2) (October 2002) 255–275.

[4] N. Bshouty, J. Jackson, T. Tamon, Uniform-distribution attribute noise learnability, Information and Computation 187 (2) (2003) 277–290.

[5] S. Cessie, J. Houwelingen, Ridge estimators in logistic regression, Applied Statistics 41 (1) (1992) 191-201

[6] B. Cestnik, I. Bratko, On estimating probabilities in tree pruning, Proceedings of the European Working Session on Machine Learning, Springer-Verlag, Porto, Portugal March 1991, pp. 138–150.

[7] S. Decatur, Learning in hybrid noise environments using statistical queries, in: D. Fisher, H. Lens (Eds.), Learning From Data: AI and Statistics, Springer-Verlag, 1996, pp. 259–270.

[8] M. Demarest, The Politics of Data Warehousing, 07/23/2004 DSSResources.COM, http://dssresources.com/papers/features/demarest/demarest07232004.html.

[9] T. Dietterich, An experimental comparison of three methods for constructing ensembles of decision trees: bagging, boosting, and randomization, Machine Learning 40 (2) (2000) 139–158.

[10] T. Fawcett, P. Flach, A response to Webb and Ting's on the application of ROC analysis to predict classi<sup>fi</sup>cation performance under varying class distributions Machine Learning 58 (2005) 33–38

[11] Y. Freund, R. Schapire, Experiments with a new boosting algorithm, Proc. International Conference on Machine Learning, Morgan Kaufmann, San Francisco 1996, pp. 148–156.

[12] S. Goldman, R. Stone, Can PAC algorithms tolerate random attribute noise? Algorithimica 14 (1995) 70–84.

[13] S. Hettich, C. Blake, C. Merz, UCI Repository of Machine Learning Databases, Department of Information and Computer Science, University of California, Irvine, 1998 http://www.ics.uci.edu/\~mlearn/MLRepository.html.

[14] W. Kim, B. Choi, Towards quantifying data quality costs, Journal of Object Technology 2 (4) (July–August 2003) 69–76

[15] S. Keerthi, S. Shevade, C. Bhattacharyya, K. Murthy, Improvements to Platt's SMO algorithm for SVM classi<sup>fi</sup>er design, Neural Computation 13 (3) (2001) 637–649.

[16] P. Laird, Learning from Good and Bad Data, Kluwer Academic Publishers, Norwell MA, 1988.

[17] S. Li, B. Lin, Accessing information sharing and information quality in supply chain management, Decision Support Systems 42 (3) (December 2006) 1641–1656.

[18] M. Mannino, V. Mookerjee, R. Gilson, Improving the performance stability of inductive expert systems under input noise, Information Systems Research 6 (4) (December 1995) 328–356.

[19] J. Mingers, An empirical comparison of pruning methods for decision tree induction, Machine Learning 4 (2) (1989) 227–243.

[20] J. Nolan, Computer systems that learn: an empirical study of the effect of noise on the performance of three classi<sup>fi</sup>cation methods, Expert Systems Applications 23 (1) (2002) 39–47.

[21] Oracle Corporation, Oracle<sup>®</sup> 10.2 Database Performance Tuning Guide, 2006 www.oracle.com.

[22] K. Orr, Data quality and systems theory, CACM 41 (2) (February 1998) 66–71.

[23] C. Perlich, F. Provost, J. Simonoff, Tree induction vs. logistic regression: a learning curve analysis, Journal of Machine Learning Research 4 (2003) 211–255.

[24] D. Pierce, L. Ackerman, Data Aggregators: A Study of Data Quality and Responsiveness, May 2005 available from http://www.privacyactivism.org/docs/ DataAggregatorsStudy.html.

[25] F. Provost, T. Fawcett, Robust classi<sup>fi</sup>cation for imprecise environments, Machine Learning Journal 42 (3) (March 2001) 203–231.

[26] J. Quinlan, Induction of decision trees, Machine Learning 1 (1986) 81–106.

[27] J. Quinlan, The effect of noise on concept learning, in: R.S. Michalski, J.G. Carbonell, T.M. Mitchell (Eds.), Machine Learning, an Arti<sup>fi</sup>cial Intelligence Approach, Volume II, Morgan Kaufmann, 1986, pp. 149–166.

[28] J. Quinlan, C4.5: Programs for Machine Learning, Morgan Kaufmann Publishers, San Mateo, CA, 1993

[29] R. Ratch, T. Onoda, K. Muller, Soft margins for AdaBoost, Machine Learning 42 (2001) 287–320

[30] T. Redman, Data quality for telecommunications, IEEE Journal on Selected Areas in Communications 12 (2) (Feb. 1994) 306–312.

[31] T. Redman, Data Quality for the Information Age, Artech House, 1996

[32] T. Redman, The impact of poor data quality on the typical enterprise, CACM 41 (2) (February 1998) 79–82.

[33] Z. Sidak, Rectangular con<sup>fi</sup>dence regions for the means of multivariate normal distributions, JASA 62 (1967) 626–633.

[34] K. Su, H. Huang, X. Wu, S. Zhang, A logical framework for identifying quality knowledge from different data sources, Decision Support Systems 42 (3) (December 2006) 1673–1683.

[35] G. Webb, K. Ting, On the application of ROC analysis to predict classi<sup>fi</sup>cation performance under varying class distributions, Machine Learning 58 (2005) 25–32.

[36] I. Witten, E. Frank, Data Mining: Practical Machine Learning Tools and Techniques, 2nd EditionMorgan Kaufmann, San Francisco, 2005.

[37] X. Zhu, X. Wu, Class noise vs. attribute noise: a quantitative study of their impacts, Arti<sup>fi</sup>cial Intelligence Review 22 (3) (2004) 177–210

![](/api/attachments/EYVEVBB7/fulltext/images/01b429745aa441f472d0cef840834c3a7cea720c2a1624420fe60337fc606fd8.jpg)

Michael V. Mannino is an associate professor in the Business School of the University of Colorado Denver. Previously he was on the faculty at the University of Florida, University of Texas at Austin, and University of Washington. He has been active in research about database management, knowledge representation, and organizational impacts of technology. He has published articles in major journals of the IEEE (Transactions on Knowledge and Data Engineering and Transactions on Software Engineering), ACM (Communications and Computing Surveys), and INFORMS (Informs Journal on Computing and Information Systems Research), His research includes several popular

survey and tutorial articles as well as many papers describing original research. He is the author of the textbook, Database Design, Application Development, and Administration in its fourth edition

![](/api/attachments/EYVEVBB7/fulltext/images/233b2b6f6780b065c7474c4cca3286c0480104a72f9c8c70c63ac538ceb33fb7.jpg)

Yanjuan Yang is a doctoral student in the Computer Science and Information Systems program at the University of Colorado, Denver. She received her M.S. in Computer Science from the University of Bristol, and her B.S. in Management from North China University of Technology. Her current research interests include data mining, deception detection and database systems.

Young U. Ryu received his Ph.D. in management science and information systems from the University of Texas Austin, in 1992. Since 1992, he has been af<sup>fi</sup>liated with the Department of Information Systems and Operations Management, School of Management, University of Texas, Dallas, where he is currently Associate Professor, His main interests of study include data mining, database, and information security.

![](/api/attachments/EYVEVBB7/fulltext/images/f57c4a038a7176c69ad597b08a633e4bcc2ec5fed57388816b44783195f3458c.jpg)
