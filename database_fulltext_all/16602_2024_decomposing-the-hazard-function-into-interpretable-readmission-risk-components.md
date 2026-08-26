---
otero_id: 16602
otero_key: "RNBQJ7MF"
title: "Decomposing the hazard function into interpretable readmission risk components"
authors: "James Todd; Steven E. Stern"
year: "2024"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2024.114264"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Decomposing the hazard function into interpretable readmission risk components

Todd, James; Stern, Steven

Published in: Decision Support Systems

DOI: 10.1016/j.dss.2024.114264.

Licence: CC BY

Link to output in Bond University research repository.

Recommended citation(APA): Todd, J., & Stern, S. (2024). Decomposing the hazard function into interpretable readmission risk components. , , 1-9. Article 114264. https://doi.org/10.1016/j.dss.2024.114264.

## General rights

Copyright and moral rights for the publications made accessible in the public portal are retained by the authors and/or other copyright owners and it is a condition of accessing publications that users recognise and abide by the legal requirements associated with these rights.

# Decomposing the hazard function into interpretable readmission risk components

![](/api/attachments/RNBQJ7MF/fulltext/images/de9d1ae9be78feee37ef2441ee25be94c4fbd7d4fdea3c1fc916b2c5f78b7a60.jpg)

James Todd <sup>\*</sup>, Steven E. Stern

Centre for Data Analytics, Bond University, Gold Coast, Queensland, Australia

## A R T I C L E I N F O

Keywords: Survival analysis Hazard rate Exponential sums Hospital readmissions Rehospitalization Summary metrics

## A B S T R A C T

Hospital decision-makers use predictive models to proactively manage risk of readmission for discharged pa tients. While predictions from classification models are easily integrated into decision-making processes, it is unclear how to best integrate predictions of the evolution of risk from time-to-event models. We propose a method for summarising predictions of risk over time that produces interpretable components for use in a variety of decision-making processes. The proposed method summarises predictions of risk over time (hazard functions) by approximating them with a parametric smoother. The components of the smoothed approximation can then serve as the basis for decision-making. To demonstrate the proposed summarisation method, we apply it in the specific case of a previously published model for patients discharged from a large teaching hospital on the Gold Coast. Australia. In this context. we describe how the summaries produced by the method could be used to estimate time until a patient reaches a stable, persistent risk level or to stratify patients according to risks of readmission in excess of patient-specific baselines. Our method is anticipated to be valuable in and outside of healthcare for settings where the evolution of risk is important, with specific examples including posttransplantation risk and reinjury risks.

## 1. Introduction

After receiving tertiary care, discharged patients should return to the community without complications or emergent needs for additional care. Unfortunately, readmissions are not uncommon. In the US, a 2019 analysis estimated the all-condition hospital readmission rate to be 15.3%, based on claims data for Medicare beneficiaries aged at least 65 [1]. Internationally, research considering admissions for chronic con ditions for hospitals in the US, UK, continental Europe, and Australia found that 10.6% of discharged patients experienced emergency 30-day readmissions [2]. While precise rates of readmissions differ by regions and cohorts, the role of hospital-level factors has spurred healthcare policy using readmission rates as quality-of-care metrics internationally [3–6]. There is evidence that such policy has had some success in reducing hospital readmission rates [7] despite concerns about their use as a performance indicator [8,9]. Furthermore, the financial, resource, and patient welfare incentives for hospitals to reduce avoidable read missions have motivated an expanding body of work developing and applying predictive models [10–13]. These models are intended to assist hospitals in managing readmissions by characterising patient-level risks before or at discharge. In particular, such models are used to assimilate and summarise multiple pieces of relevant data about a patient’s risk profile to enable decision-making without information overload [14].

Research investigating predictive models for readmission risk has often adopted classification approaches in which readmission status is based on event occurrence within a fixed time horizon [11,12,14], most commonly 30 days. As these approaches do not explicitly consider the full evolution of risk, they support decision-making based only on measures of risk that generally cannot be updated after discharge. For example, Romero-Brufau, Wyatt [15] describe a system predicting 30- day readmission risk to support decision-making for individual pa tients at discharge, finding that the patient-centred interventions reduced readmissions. However, the focus on individual overall risk means the predicted risk associated with patients discharged at different times cannot be directly compared, preventing ongoing risk stratification.

The development of models under time-to-event approaches has been less common [16–25], despite the problem of readmissions often being used to illustrate such models [26,27]. Time-to-event models aim to capture the temporal evolution of risk rather than static predictions at a single point in time. An example of such a prediction is shown in Fig. 1, where the risk (hazard) of readmission can be seen to evolve over time and the probability of readmission is shown at selected time points. While predictions of risk over time offer greater information than a prediction at a single time point, it is less clear how to incorporate them into decision-making processes. In some cases, research using time-toevent models has evaluated them based on predictions at a single time point, as is done for classification models [16,17,21]. One application of time-to-event models for decision-making has been to dynamically rank patients according to their conditional risk of readmission within a fixed period post-discharge [22,28], thus updating a patient’s risk to reflect its evolution since they were discharged.

![](/api/attachments/RNBQJ7MF/fulltext/images/8e3d3c6b2097f4c5394d6deb0c6ea6da6202760c28f26be04db4ba8c8cb029b3.jpg)  
Fig. 1. The Baseline Hazard of Readmission and Fixed Point Readmission Probabilities.

Generally, the use of predictive models in managing readmission risk is similar whether a classification or time-to-event approach is adopted. In both cases, a suitable model is estimated and then used to generate predictions that are integrated into decision processes. For classification models, predictions above a threshold may be used to identify high-risk patients. For time-to-event models, predictions of readmission risk in 30 days, conditional on time since discharge, have enabled dynamic ranking of patients. Other uses of risk over time predictions have been suggested in prior research, such as detailing the evolution of risk and the duration of elevated risk after discharge [28]. However, no methods for producing corresponding summaries of predictions have been described. Such summaries could aid decisions about the timing of follow-up care or interventions to prevent the unplanned readmissions and potentially avoidable readmissions considered in many studies [29–38].

This lack of methods for summarising risk over time predictions to aid in making informed decisions is the primary focus of this work. We propose a method for summarising predictions of risk over time by decomposing the hazard function into interpretable, additive compo nents. Specifically, we describe a method for summarising predictions of risk over time by employing a parametric function, constructed from a shifted series of exponential decay terms, chosen to closely approximate the predicted hazard function. The proposed method is broadly appli cable to problems in which the hazard function produced by a nonparametric or semi-parametric method has a shape characterised by an overall decreasing trend and a non-zero asymptote. To illustrate the method, we consider a case study using a time-to-event model for readmissions developed in prior research [28]. The utility of this method for readmissions stems from the enhanced ability of decision-makers to reason about the evolution of risk for individual patients; for example, by assessing when a patient’s risk has reached a baseline level and further follow-up is unlikely to be helpful, or prioritising patients with the greatest “excess” risk after adjusting for patient-specific baselines.

While the proposed method was motivated by the problem of hos pital readmissions, the need to make decisions based on the evolution of time-to-event risk is relevant to many domains. For example, predicting the risk of adverse outcomes after organ transplantation is important for resource allocation decisions [39], and measures of total risk could be complemented by estimates of how long it takes a patient to reach a patient-specific baseline. The value of such complementary measures for organ transplantation is reinforced by the explicit focus on multiple time horizons in several predictive models developed in this area [40,41]. Similar examples can be made with respect to soft tissue reinjury risk for elite athletes, where predicted risk of re-injury upon resumption of participation is important but can be complemented by estimates of how long it will take the athlete to reach a persistent, baseline level of risk.

Section 2 provides a description of the general time-to-event problem and details the proposed method for decomposing the hazard function into additive components. Section 3 provides a case study in which the method is applied to the hazard function produced by a Cox’s propor tional hazards model for readmission risk that was developed in prior work. Several applications to decision-making in this context are also described. Section 4 provides a discussion of the methodology with respect to the underlying time-to-event model, hazard function, and potential modifications. Section 5 provides concluding insights and discussion.

## 2. Decomposing the hazard

We begin by briefly outlining the general problem of time-to-event analysis in the presence of right censoring. We consider a set of n ob servations indexed by i, each comprised of a $p \cdot$ -dimensional covariate vector $\pmb { X } _ { i } ;$ a follow-up time $Y _ { i } = m i n ( T _ { i } , C _ { i } )$ , where $T _ { i }$ is the time of the event of interest and $C _ { i }$ is an independent random censoring time; and, the indicator $\delta _ { i } = \mathbf { 1 } ( T _ { i } \leq C _ { i } )$ which denotes whether the follow-up time corresponds to the time of the event. We consider only the case where all observations $i = 1 , . . . , n$ are independent, and none of the covariates are time varying.

When analysing time-to-event data, it is often useful to estimate the probability of being event-free over time $( \mathrm { i . e . } ,$ , the survival function) and the rate of event occurrence over time (i.e., the hazard function):

$$
S (t | \boldsymbol {X} _ {i}) = P r (T _ {i} > t | \boldsymbol {X} _ {i})
$$

$$
\lambda (t | \mathbf {X} _ {i}) = \lim _ {h \rightarrow 0} \frac {\operatorname* {P r} (t <   T _ {i} <   t + h | \mathbf {X} _ {i})}{h \bullet \operatorname* {P r} (T _ {i} > t | \mathbf {X} _ {i})} = \lim _ {h \rightarrow 0} \frac {\mathrm{S} (t | \mathbf {X} _ {i}) - \mathrm{S} (t + h | \mathbf {X} _ {i})}{h \bullet \mathrm{S} (t | \mathbf {X} _ {i})} = \frac {- \frac {d}{d t} \mathrm{S} (t | \mathbf {X} _ {i})}{\mathrm{S} (t | \mathbf {X} _ {i})}
$$

The hazard function can be viewed from several perspectives [42]. Here, the view of the hazard function as the evolution of risk over time for an observation is most relevant.

Many models have been proposed for producing estimates of both survival and hazard functions. Perhaps the most frequently used is Cox’s semi-parametric proportional hazards model [43], also known as Cox regression. Other options include Aalen’s additive hazards model [44,45] and parametric accelerated failure time models [46]. Prominent non-parametric approaches have included tree-based models, both as individual learners [47–52] and in ensembles [51,53–56].

The following subsections describe the proposed method for sum marising a predicted hazard function, as well as evaluating the produced summary, and practical application of the method to hazard functions produced by different model types.

## 2.1. The decomposition structure

To begin, we assume an estimate of the hazard function – $\cdot \ \widehat { \lambda } ( t | \pmb { X } _ { i } ) \ -$ has been produced that is deemed sufficiently reliable to support decision-making. This function is expanded as a summation of K un derlying risk components:

$$
\widehat {\lambda} (t | \mathbf {X} _ {i}) = \sum_ {k = 1} ^ {K} g _ {k} (t; \boldsymbol {\theta} _ {i, k}) + \xi_ {i, t}
$$

where the ${ g } _ { k } ^ { * } { s }$ are non-negative functions of $t ,$ parameterised by $\theta _ { i , k } ,$ representing underlying risk components and $\xi _ { i , t }$ is the time-dependent approximation error.

We restrict attention to scenarios where the estimated hazard func tion is characterised by a monotonic decreasing trend to a non-zero asymptote, characteristics common to many practical settings. Further, in line with these scenarios, we choose the $g _ { k }$ to be exponential decay functions of the form $a e ^ { b t }$ and set the decay constant, b, for the component g to zero, making it a constant shift component. As such, we have:

$$
\widehat {\lambda} (t | \mathbf {X} _ {i}) = \alpha_ {i, 1} + \sum_ {k = 2} ^ {K} \alpha_ {i, k} e ^ {\beta_ {i, k} t} + \xi_ {i, t}
$$

The values of the parameters $\alpha _ { i , 1 } , . . . , \alpha _ { i , K }$ and $0 > \beta _ { i , 2 } > . . . > \beta _ { i , K }$ are determined by minimising the sum of squared errors, $\xi _ { i , t } ^ { 2 } ,$ across a range of t values. We refer to this as a “decomposition” of the hazard into components. Our method is equivalent to using a specific form of parametric smoother for $\widehat { \lambda } ( t | \mathbf { X } _ { i } )$ . For convenience, we denote the smoothed approximation for a given value of K as:

$$
\overline {{\lambda}} _ {K} (t | \mathbf {X} _ {i}) = \alpha_ {i, 1} + \sum_ {k = 2} ^ {K} \alpha_ {i, k} e ^ {\beta_ {i, k} t}
$$

Incorporating this summary into decision-making processes could then be based on the interpretation of the individual components of the smoothed approximation rather than the estimated hazard function. The benefit of this is two-fold. First, small irregular oscillations in the esti mated hazard function are common in semi-parametric and nonparametric models, as is visible in $\mathrm { F i g . ~ 1 }$ , but are removed by the smooth summary. Second, individual components can be used to describe the evolution of risk in several ways. For example, estimating “time to baseline” by finding the value of t for which the smoother is sufficiently close in value to $\alpha _ { 1 } ;$ or, comparing the contribution of each component at different points in time. Several specific examples are discussed for hospital readmissions in Section 3.3.

Given the above framework, the key decision to be made is the choice of $K ,$ which determines the number of exponential decay terms. Smaller values of K will result in more interpretable components, but the approximation, $\overline { { \lambda } } _ { K } ( t | { \bf { X } } _ { i } )$ , may provide a poor summary of the estimated hazard function, $\widehat { \lambda } ( t | \pmb { X } _ { i } )$ . Larger values of K lead to reduced interpret ability but provide a more faithful summary. The choice of K should balance both interpretability and faithfulness of the approximation. Domain knowledge may also inform the choice of K. For example, a patient’s risk of readmission post-discharge may be believed to be a combination of acute risk associated with complications, morbidity risk associated with increased vulnerability while recovering from care, and a persistent background risk. This would lead to the choice: $K = 3$

## 2.2. Evaluating a decomposition

Having decomposed $\widehat { \lambda } ( t | \mathbf { X } _ { i } )$ into the sum of K components, it is then necessary to evaluate whether the smoothed approximation $\overline { { \lambda } } _ { K } ( t | { \bf X } _ { i } )$ provides a faithful summary. Errors from an insufficiently flexible approximation should be characterised by systematic patterns in sign, while errors from a satisfactory approximation should be scattered around zero. This characteristic is the focus of both the numerical and visual evaluations we suggest. Throughout our description of these evaluations, we focus on errors of approximation and intentionally avoid describing these as residuals from a statistical model.

First, numerical evaluation of $\overline { { \lambda } } _ { K } ( t | { \bf { X } } _ { i } )$ for a given K should assess the presence of systematic autocorrelations in errors. Considering the approximation errors $( \xi _ { i , t } )$ as a time series process, we suggest the use of the Ljung-Box test for autocorrelations. An acceptable approximation should not have autocorrelations in errors which are significantly

different from zero.

Second, complementing the numerical test, two visual assessments of fit are also recommended: a plot of errors over time and a plot overlaying both $\widehat { \lambda } ( t | \pmb { X } _ { i } )$ and $\overline { { \lambda } } _ { K } ( t | { \bf { X } } _ { i } )$ over time. The former plot allows for identifi cation of error clusters or other undesirable characteristics. Errors should be evenly distributed around zero. The latter plot contextualises any problems identified. For example, clusters of similarly signed errors in the first plot may stem from $\overline { { \lambda } } _ { K } ( t | { \bf { X } } _ { i } )$ failing to capture the overall shape of $\widehat { \lambda } ( t | \mathbf { \boldsymbol { X } } _ { i } )$ , which would indicate that $\overline { { \lambda } } _ { K } ( t | { \bf { X } } _ { i } )$ is inadequate as a summary. On the other hand, patterns in errors in the first plot may stem from temporal correlations in $\widehat { \lambda } \left( t | \pmb { X } _ { i } \right)$ causing clusters of errors and may not reflect a failure of $\overline { { \lambda } } _ { K } ( t | { \bf X } _ { i } )$ to capture the overall shape.

Both methods of evaluation are demonstrated as part of the case study in Section 3.

## 2.3. Structured hazard functions

The above subsections described a method to decompose a generic estimate of the hazard function, $\widehat { \lambda } ( t | \mathbf { X } _ { i } ) ,$ , into potentially interpretable components and described methods to evaluate the decomposition, $\overline { { \lambda } } _ { K } ( t | { \bf { X } } _ { i } )$ . Throughout that discussion, a generic hazard function was considered. In practice, decision-makers will often be interested in a set of estimated hazard functions, each of which needs to be meaningfully summarised. If the described method for decomposing hazard functions needed separate application for each hazard function of interest, this may be time intensive. However, the structure of the hazard functions often allows for scalable application of the method. We now consider the scenario where the hazard function of interest. $\widehat { \lambda } ( t | \mathbf { X } _ { i } )$ , has some specific structure determined by either the choice of estimation method or the structure of the observed covariates. Specifically, we have considered that there are n observations and each is associated with an appropriate estimated hazard function – characterised by a decreasing trend and non-zero asymptote – and a decomposition of these hazard functions is desired. The applicability of the proposed method is discussed when all n observations have a corresponding estimate of the hazard function that is:

1. equal to or proportional to one overall hazard function; and

2. equal to or proportional to one of $1 < m < n$ hazard functions.

In the absence of exploitable structure in the underlying model, such as when using techniques based on ensembles $[ 5 1 , 5 3 - 5 6 ]$ , the proposed method would need to be applied individually for each estimated hazard function.

## 2.3.1. Equal to or proportional to one overall hazard function

This scenario may arise if no covariate information is available for the population of interest, resulting in a single population-level hazard function. In this case, fitting and evaluating $\overline { { \lambda } } _ { K } ( t | \mathbf { X } _ { i } ) = \overline { { \lambda } } _ { K } ( t )$ is equivalent to decomposing the hazard function for the whole population. The decomposition may help a decision-maker to understand the evolution of risk, but no differences are allowed for distinguishing between individual observations.

Another way this scenario may arise is when a proportional hazards model is used, such as a Cox regression without strata. This is perhaps the modal outcome of time-to-event modelling exercises involving covariates. In this case, there may be n estimated hazard hazard func tions $\widehat { \lambda } ( t | \mathbf { \boldsymbol { X } } _ { i } )$ , each of which is proportional to a common baseline hazard, as shown below:

$$
\widehat {\lambda} (t | \mathbf {X} _ {i}) = \widehat {\lambda} _ {0} (t) e ^ {\mathbf {X} _ {i} ^ {T} \hat {\mathbf {W}}}
$$

where $\widehat { \pmb { w } }$ is an estimated p-dimensional coefficient vector and $\widehat { \lambda } _ { 0 } ( t )$ is an estimate of the baseline hazard shared by all observations. In this case, the proportionality of the estimated hazard functions can be exploited to apply the described decomposition to all observations. For a given choice of $K ,$ the decomposition will produce a smoothed approximation $\overline { { \lambda } } _ { K } ( t | { \bf { X } } _ { i } )$ in which exponent terms (β) will be constant for all choices of i and base terms (α) will be multiplied by $e ^ { \pmb { X } _ { i } ^ { T } \hat { \pmb { w } } _ { \ast } }$

Table 1 Descriptive Statistics.

<table><tr><td></td><td>Count(% of discharges)</td></tr><tr><td>Discharges</td><td>46,659 (100%)</td></tr><tr><td>Readmissions within:</td><td></td></tr><tr><td>30 days</td><td>6723 (14.41%)</td></tr><tr><td>60 days</td><td>94,31 (20.21%)</td></tr><tr><td>90 days</td><td>11,212 (24.03%)</td></tr><tr><td>120 days</td><td>12,428 (26.64%)</td></tr></table>

Table 2  
Parameter Estimates using Three Components.

<table><tr><td>Parameter</td><td>Estimate</td></tr><tr><td> $\widehat{a}_{0,B}$ </td><td>0.0009</td></tr><tr><td> $\widehat{a}_{0,A}$ </td><td>0.0051</td></tr><tr><td> $\widehat{\beta}_{A}$ </td><td>-0.2738</td></tr><tr><td> $\widehat{\alpha}_{0,M}$ </td><td>0.0039</td></tr><tr><td> $\widehat{\beta}_{M}$ </td><td>-0.0264</td></tr></table>

Quadratic Variation $( t = 1 , 2 , . . . , 1 8 0 ) = 1 . 3 0 3 \mathrm { e } { } .$ 05

Table 3  
Ljung-Box Tests with Three Components.

<table><tr><td>Lag</td><td> $\chi^2(lag)$ </td><td>p-value</td></tr><tr><td>1</td><td>0.3756</td><td>0.5400</td></tr><tr><td>2</td><td>1.3057</td><td>0.5206</td></tr><tr><td>3</td><td>1.6227</td><td>0.6542</td></tr><tr><td>4</td><td>3.9838</td><td>0.4082</td></tr><tr><td>5</td><td>3.9876</td><td>0.5512</td></tr></table>

![](/api/attachments/RNBQJ7MF/fulltext/images/03d845b0586d4ba91a9353803ca81c34b6911c766952ebeacc64c02f7d2817f1.jpg)  
Fig. 2. Three-Component Model for the Baseline Hazard.

$$
\widehat {\lambda} _ {0} (t) = \alpha_ {0, 1} + \sum_ {k = 2} ^ {K} \alpha_ {0, k} e ^ {\beta_ {0, k} t} + \xi_ {0, t} = \overline {{\lambda}} _ {0, K} (t) + \xi_ {0, t}
$$

$$
\widehat {\lambda} _ {0} (t) e ^ {\boldsymbol {X} _ {i} ^ {T} \hat {\boldsymbol {W}}} = \widehat {\lambda} (t | \boldsymbol {X} _ {i}) = \overline {{\lambda}} _ {0, K} (t) e ^ {\boldsymbol {X} _ {i} ^ {T} \hat {\boldsymbol {W}}} + \left(\xi_ {0, t} e ^ {\boldsymbol {X} _ {i} ^ {T} \hat {\boldsymbol {W}}}\right)
$$

As shown, if the baseline estimate of the hazard is decomposed into additive components, this can be generalised to any other observation $i \in { 1 , . . . }$ n using the associated coefficient vector <sup>̂</sup>W from the underlying model.

![](/api/attachments/RNBQJ7MF/fulltext/images/ef0f106f117c4adafa67a45d94f97f13f70d3e15e1367b5c293461a7313a8350.jpg)  
Fig. 3. Errors of the Three-Component Model for the Baseline Hazard.

![](/api/attachments/RNBQJ7MF/fulltext/images/2e1f36f868945a8e1f71f926fc6f502f9ed5a4d4fb2f482a984bf5da5ed8145f.jpg)  
Fig. 4. Two-Component Model for the Baseline Hazard.

![](/api/attachments/RNBQJ7MF/fulltext/images/b334fb8443dd259b9a0db7988b4f80c168208f5883ec44644460a666262f064f.jpg)  
Fig. 5. Errors of the Two-Component Model for the Baseline Hazard.

## 2.3.2. Equal to or proportional to one $\ o f 1 < m < n$ hazard functions

There are two common ways that the n estimated hazard functions can be equal to or proportional to some m hazard functions. First, the underlying model used to estimate the hazard function may only provide m unique estimates of the hazard function. This may be the case if a small number of unique covariate vectors are possible. For example, if the only covariate is a binary indicator for a person’s smoking status, only $m = 2$ hazard functions can be constructed. Alternatively, tech niques like survival trees aim to partition observations into homoge neous groups. A survival tree with 5 terminal nodes will produce $m = 5$ unique hazard functions. In the case that there are only m unique hazard function estimates, the proposed decomposition would need to be applied m times, without sharing data between each group.

The second possibility is a Cox regression model with strata, allowing for different baseline hazard functions for different values of a cate gorical covariate. For example, smokers and non-smokers may have nonproportional hazards. This is not equivalent to two independent esti mates of the baseline hazard functions, $\widehat { \lambda } _ { 0 , y e s } ( t )$ and $\widehat { \lambda } _ { 0 , n o } ( t )$ , as the two groups share a coefficient vector ${ \widehat { \pmb { W } } } .$ . Given m unique baseline hazard functions, the decomposition method would need to be applied m times. For a given stratum, if the baseline estimate of the hazard is decomposed into additive components, this can be generalised to any other obser vation in that stratum as shown previously.

## 2.4. Summary

The above subsections have described the proposed method for summarising a time-to-event model’s estimate of the hazard function. The method uses a parametric smoother to decompose the hazard function into a sum of interpretable components. As the number of components is modifiable, methods for evaluating the decomposition are also suggested, based on a test of autocorrelation in errors and visual assessment. Finally, the practical application of the proposed method to scenarios with structured hazard functions was described. Throughout, we restrict attention to hazard functions characterised by a decreasing trend and non-zero asymptote, which are a feature of many problems.

## 3. Application to gold coast hospital readmission data

We now illustrate the decomposition method, including its con struction and evaluation, with a case study. To reinforce the role of the decomposition as a method for summarising an acceptable model’s predictions, rather than being a predictive model itself, we use a Cox regression model published in prior research [28].

## 3.1. The underlying model and data

The underlying time-to-event model considered in this case study is a Cox regression model used to predict risk of readmission. The data used to estimate this model related to a cohort of adults admitted as inpatients via the emergency department of Gold Coast University Hospital, a large public teaching hospital on the Gold Coast in Australia. Ethics approval for this research was obtained from the Bond University Human Research Ethics Committee (HREC JT00253). Table 1 reports the size of the dataset and the proportion of discharges associated with read missions within different time periods. Each observation corresponds to a patient discharged from hospital and the time until readmission is of interest.

For each discharge, 19 features corresponding to basic demographic information $( \mathrm { i . e . , }$ region of Gold Coast, age, sex), prior utilisation of healthcare services, and length of stay were available for modelling at the time of patient discharge, as detailed in Todd, Gepp [28]. The hazard function was estimated using the Efron approximation [57] for ties. The details of the final model are omitted for brevity and to focus attention on the decomposition method rather than the exact underlying model.

Model details are available upon request and more extensive description of both the data and modelling process has been previously reported by Todd, Gepp [28].

## 3.2. Applying the decomposition

Given the underlying model, an estimate of the hazard function for any given discharge can be produced, as previously illustrated in Fig. 1. This then needs to be summarised into a format supporting related decision-making. Risk dynamics beyond 180 days are assumed to be of little interest given the resource constraints faced by hospitals, though the restriction to 180 days was not imposed in model estimation.

To decompose the estimated hazard, the risk of readmission postdischarge is hypothesised to be a sum of background, acute, and morbidity risk, corresponding to $K = 3 ,$ . We replace numeric subscripts with letters reflecting the interpretation of components as background $( B ) ,$ , acute $( A )$ , and morbidity (M) risk:

$$
\widehat {\lambda} (t | \mathbf {X} _ {i}) = \alpha_ {i, B} + \alpha_ {i, A} e ^ {\beta_ {A} t} + \alpha_ {i, M} e ^ {\beta_ {M} t} + \xi_ {i, t}
$$

In this formulation, $\alpha _ { i , B } , \alpha _ { i , A }$ and $\alpha _ { i , M }$ reflect the scale of background, acute, and morbidity risk and vary across observations. $\beta _ { A }$ and $\beta _ { M }$ reflect the rate of decay for acute and morbidity risks. These latter parameters do not vary across observations because of the proportionality of all hazard functions produced by the underlying model, as shown in Section 2.3. For generality, we apply the decomposition method to the baseline hazard function:

$$
\begin{array}{l} \widehat {\lambda} _ {0} (t) = \alpha_ {0, B} + \alpha_ {0, A} e ^ {\beta_ {A} t} + \alpha_ {0, M} e ^ {\beta_ {M} t} + \xi_ {0, t} \\ \widehat {\lambda} _ {0} (t) = \overline {{\lambda}} _ {3} (t) + \xi_ {0, t} \end{array}
$$

An alternative specification may have involved only two components of risk, a care-related decaying component and a constant background component. We include the results of the decomposition model with only two components in the Appendix for illustrative purposes.

Having set $K = 3 ,$ , Table 2 presents the parameters estimated via least-squares procedures. Parameter estimates are initialised for the estimation algorithm according to approximate expectations about the relative contribution of acute and morbidity risks and their persistence:

• The $\alpha _ { 0 , B } , \alpha _ { 0 , A } ,$ , and $\alpha _ { 0 , M }$ parameters are initialised as the minimum hazard, 70% of the maximum hazard, and 20% of the maximum hazard respectively, reflecting the expectation that most of the initial risk of readmission is expected to be acute $( \mathrm { i . e . , }$ , risk of rapid dete rioration or complications).

• The $\beta _ { A }$ and $\beta _ { M }$ parameters are initialised as − 0.17 and $\textsuperscript { - } 0 . 0 7$ respectively, corresponding to approximate half-lives of four and ten days for the two risk components. This reflects the short-lived acute risk of readmission relative to morbidity risk.

Informed by the initialisation for the Levenberg-Marquardt algo rithm, the parameter estimates for the acute and morbidity components approximately align with expectations of rank and magnitude. The acute component of risk has a larger initial contribution than the morbidity element, as $\alpha _ { 0 , A }$ is approximately 25% larger than $\alpha _ { 0 , M } .$ . The acute component also decays more rapidly than the morbidity component, with approximate half-lives of 2.5 and 26 days respectively.

## 3.2.1. Diagnostics

Having decomposed $\widehat { \lambda } _ { 0 } ( t )$ into the sum of 3 components, it is necessary to evaluate whether the smoothed approximation $\overline { { \lambda } } _ { 3 } ( t )$ pro vides a faithful summary.

First, the autocorrelation of errors is evaluated via the Ljung-Box test at lags of 1 to 5. The $\chi ^ { 2 }$ test statistics and p-values for each lag are re ported in Table 3. At all considered lags, there is insufficient evidence to reject the null hypothesis of zero autocorrelation.

Second, two visuals are considered. The first visualization overlays the smoothed approximation and the underlying components on the estimated hazard function (Fig. 2) and the second shows the approxi mation errors over time (Fig. 3). In general, these plots indicate the smoothed approximation satisfactorily captures the trends of the esti mated hazard, and we note:

1. The smoothed approximation has a small period of consistent un derestimation around 75 days, most clearly shown in Fig. 3. Fig. 2 indicates that this is not due to a systematic deficiency of the smoothed approximation and is likely attributable to variation in the estimated hazard function. The low impact of this period is further supported by the earlier statistical test.

2. Fig. 3 indicates a pattern in the magnitude of errors, with larger errors immediately post-discharge. This is less evident in Fig. 2, where perpendicular offsets are more naturally observed rather than vertical offsets. The greater magnitude of errors immediately post discharge is driven by the larger vertical scale of the hazard func tion in this region of the data and steeper overall descent.

Overall, it appears that the decomposition structure provides a good description of the dynamics of the estimated hazard function. The errors do not exhibit systematic correlations and the smoothed approximation captures the trends of the estimated hazard function. As such, the fitted components comprising the smoothed approximation could be used to better describe the evolving risk profiles of discharged patients.

## 3.3. Utility for managing readmission risk

Hospital decision-makers using quantitative readmission risk models rely on the summaries of risk produced by these models for discharged patients. This is most evident in classification approaches, where the risk model estimates the risk of readmission within a fixed period and the patients can be ranked on this basis. Time-to-event models provide complementary utility and greater flexibility, such as dynamic ranking of patients even after discharge. The decomposition of risk into inter pretable components are similarly complementary and flexible. Several potential uses of the interpretable components by hospital decision makers for summarising patient risk are briefly outlined here.

## 3.3.1. Total risk

An immediately appealing summary of a patient’s readmission risk is their total risk of readmission, perhaps within a fixed period. This matches the proposed usage of classification models that estimate the risk of readmission within 30 days or other horizons. The decomposition discussed here enables the same summarisation of patient risk, and subsequent ranking for prioritisation, but allows for the removal of the background component of risk. This is desirable if care-related risk is of primary interest for mitigation.

In the case that the hazard function is estimated with Cox’s pro portional hazards model, as in this case study, removing the background component will not affect the relative rankings of risk within a fixed horizon. It will, however, provide more meaningful individual risk es timates to balance against management options under resource constraints.

## 3.3.2. Time until acceptable risk

A second way to summarise a patient's readmission risk is the time until their risk falls below a pre-defined threshold. Such summaries cannot be produced with classification models. Time-to-event models can compute such summaries, but the implicit inclusion of the back ground component again results in undesirable characteristics. For example, a patient defined as high-risk may also have a large back ground component and so they may never fall below the ‘acceptable threshold, or at least within a useful time frame. Conversely, a low-risk patient may never exceed the threshold, despite have meaningful care

related risk in the short term.

With the above separation of risk components, patients can instead be summarised according to the time until their care-related risk falls below a threshold. This summary has several attractive features, including a guarantee for the exponential terms to eventually become effectively zero and allowance for patient-specific timeframes. One statistically motivated threshold would be the time until the acute components is less than the standard error associated with the back ground component, perhaps estimated via a bootstrap procedure.

## 3.3.3. Component-specific risk management

A key benefit of the proposed decomposition is the ability to omit the background risk component from summaries of patient risk. Extending this, the acute and morbidity risk components could also be considered individually as well as together. The contribution of each component to total risk and the time taken to fall below a threshold can inform component-specific management strategies. These may include specific actions, such as interventions to manage acute risk, as well as simply informing other stakeholders, such as primary care providers who can assist in the management of morbidity risk in the community.

## 3.3.4. Dynamic risk ranking

The utility of time-to-event models for dynamic ranking of read mission risk has been highlighted previously [28]. A direct extension of such applications, given an appropriate decomposition, is for rankings to be based on individual components of interest. If it is decided that the hospital is responsible for acute risk, or that a given set of strategies are relevant to this component, then the separation of this component from total risk allows for a corresponding dynamic ranking of all discharged patients.

## 4. Discussion

In the previous sections we have described a method for decom posing a hazard function into a sum of interpretable components. We require only that the hazard function has a decreasing trend and a nonzero asymptote. We have also applied the method to the problem of readmission risk modelling with a Cox regression model, illustrated the use of suggested diagnostics, and outlined several practical uses of interpretable components produced by the decomposition. The following subsections discuss the method with respect to restrictions on the hazard shape, potential modifications to the parameter estimation process, and generalisability.

## 4.1. Hazard function shapes

Hazard functions can be ‘bathtub’-shaped, increasing, constant, or other shapes. The restriction to only decreasing hazard functions with non-zero asymptotes is motivated by an emphasis on producing inter pretable summaries of risk over time. While excellent numerical ap proximations for many other types of hazard functions are possible, the interpretability and thus utility of the individual components are reduced. For example, a commonly observed shape of hazard rate in volves an initial increase in hazard followed by a decrease. For the problem of readmissions, such a hazard function might be observed if there were a temporary protective effect from treatment. This could cause an initial increase in observed risk as the protection wears off in the first few days, followed by decreasing risk as patients’ conditions stabilise. While a smoothed approximation based on more complex functions could capture such shapes, the need for greater complexity does not readily align with our goal of providing interpretable summaries.

## 4.2. Modifying parameter estimation

Parameter estimation for the nonlinear decomposition structure is easily performed through least square procedures using established procedures and software. Modifications to these procedures may be warranted if errors are expected to contain outliers, such as in the case of hazard functions with high variability. In the authors’ experience, this issue is common in machine learning time-to-event models and is rele vant in determining whether estimates of the hazard function produced by the underlying time-to-event model are ‘acceptable’. In these sce narios, a more appropriate objective function that is less sensitive to outliers can be selected for optimisation. An intuitively appealing approach would be to introduce time-dependent weights ω<sub>t</sub> to account for uncertainty in the hazard function across time.

Modifications to the parameter estimation process may also be motivated by the dissonance between the observed and numerical fit show in Fig. 2 and Fig. 3. Larger numerical errors were observed at earlier times, but visual inspection indicated that the smoothed approximation provided a good description of the estimated hazard. If the visual inspection is decided to be of greater importance, errors based on perpendicular offsets rather than vertical offsets could be considered in the objective function. Perpendicular offsets would also better reflect the ordering of the observed data. Finally, if the original goal of fitting the underlying time-to-event model is to support decision-makers and a smoother hazard function is required, smoothness can be incentivised in the estimation of the underlying model.

## 4.3. Generalisability

In Section 3, we described the application of the decomposition method in a specific context, readmission risk modelling, and with a specific type of underlying time-to-event model, Cox regression. The implications of varving these two elements bears discussion.

If the context for the case study were changed to consider read missions for a different hospital or patient cohort, the major steps in applying and using the proposed decomposition would remain un changed. We wish to highlight, however, that the process would need to be repeated for this new setting. The proposed method provides sum maries of model predictions to better integrate an accepted model in decision-making processes. Matching the focus on the decision-makers at the hospital-level rather than system-level, the components pro duced by the decomposition should not be expected to generalise be tween hospitals and cohorts unless the underlying model is expected too as well.

If the context for the case study were changed to consider a wholly different problem, such as time to reinjury for athletes in a particular sport, the major steps in applying the decomposition would be un changed. The practical uses of the resulting components would differ from the readmission-specific applications suggested in Section 3.3, but we would expect context-specific uses to consider similar principles. For example, time until acceptable risk might be of interest for determining rehabilitation time instead of follow-up care.

The implications of changing the underlying modelling technique from Cox regression to an alternative is perhaps more fundamental. As described in Section 2.3, applying the decomposition to multiple hazard functions is straightforward when those hazard functions are propor tional to one another, as was the case in the Cox regression model of Section 3. A natural extension to this type of Cox regression model is to include strata, which allows for difference baseline hazard functions according to one or more categorical features. In such cases, the major steps of the decomposition can be applied without change except that they should be repeated for each of the strata. Similarly, any model producing a relatively small number of unique predictions simply re quires repeated application of the model. If, however, many unique predictions are possible without a shared structure, the steps in the decomposition would need to be repeated for each new prediction.

## 5. Conclusion

Motivated by the problem of readmissions and the practical use of time-to-event models in decision-making processes, we have proposed a method for summarising predictions of risk over time. The proposed method serves as a complement to other summaries of risk over time predictions for domains where the evolution of risk is important for decision-making. Our method decomposes the predictions of risk over time (the hazard function) produced by a time-to-event model into interpretable, additive components. These components together form a smoothed approximation of the hazard function and can be used to summarise the evolution of risk over time. To illustrate the method and the types of decision-making it enables, we considered a case study involving readmission prediction from prior research [28]. We described how the results of the decomposition could be used to estimate time until acceptable risk, measure the elevated risk relevant for man agement, and rank patients. While these applications focus on the problem of readmissions, the underlying ideas are broadly applicable to settings in which predictions of risk over time are relevant to decisionmakers. Regardless of setting, however, the descriptive nature of the method should be borne in mind to guard against inappropriate infer ential conclusions.

Two limitations of this work are important to mention. First, we restricted attention to hazard functions with decreasing trends and nonzero asymptotes. While it is technically possible to decompose hazard function shapes with only minor modifications, the reduced interpret ability of the results compromises their value for decision-making. Second, if the underlying time-to-event model produces many unique and non-proportional hazard functions, the proposed method is likely impractical at scale.

Finally, two areas of future work are identified. First, future research should validate whether the interpretation of components described in Section 3 is consistent with reasons for readmission. We intend to conduct this research using more detailed hospital data to determine whether readmissions can be classified as being unrelated to the original admission, indirectly related, or directly related. These correspond to the components interpreted as background, morbidity, and acute risk. Second, future research could aim to better derive the properties of the method for decomposition and extend it beyond the hazard shape of the present work.

## Funding

This work was supported by an Australian Government Research Training Program Scholarship (James Todd). It was also supported by Healthcare Logic Pty Ltd. via Australian Innovation Connections Grants (ICG0043 and ICG000945).

## CRediT authorship contribution statement

James Todd: Writing – review & editing, Writing – original draft, Visualization, Software, Methodology, Formal analysis, Conceptualiza tion. Steven E. Stern: Writing – review & editing, Supervision, Meth odology, Conceptualization.

## Declaration of competing interest

The authors declare the following financial interests/personal re lationships which may be considered as potential competing interests:

Steven E. Stern reports financial support was provided by Healthcare Logic Pty Ltd. James Todd reports financial support was provided by Australian Government Department of Education. If there are other authors, they declare that they have no known competing financial in terests or personal relationships that could have appeared to influence the work reported in this paper.

## Data availability

The authors do not have permission to share data.

## Acknowledgements

The authors thank Healthcare Logic Pty Ltd., who provided the data for the project.

## Appendix A

The hazard function produced for readmission risk in Section 3 is well described by a smoothed approximation based on one constant component and two decaying components. This section briefly illustrates the case where the hazard function is decomposed into one constant component and one decaying component, which provides a poor description of the hazard function. Considering the constant and decaying components in the context of background (B) risk and care-related (C) risk, the two-component decomposition model for the baseline estimated hazard is given as:

$$
\widehat {\lambda} _ {0} (t) = \alpha_ {0, B} + \alpha_ {0, C} e ^ {\beta_ {C} t} + \xi_ {0, t} = \overline {{\lambda}} _ {2} (t) + \xi_ {0, t}
$$

For parameter estimation, $\alpha _ { 0 , B }$ and $\alpha _ { 0 , C }$ are initialised as the minimum and the range of the baseline hazard function respectively. The $\beta _ { C }$ parameter is initialised as − 0.035, corresponding to an approximate half-life of 20 days for the care-related component. The final parameter estimates from the Levenberg-Marquardt algorithm are given in Table 4.

<table><tr><td colspan="2">Table 4Parameter Estimates using Two Components.</td></tr><tr><td>Parameter</td><td>Estimate</td></tr><tr><td> $\widehat{\alpha}_{0,B}$ </td><td>0.0011</td></tr><tr><td> $\widehat{\alpha}_{0,C}$ </td><td>0.0060</td></tr><tr><td> $\widehat{\beta}_{C}$ </td><td>-0.0462</td></tr><tr><td colspan="2">Quadratic Variation (t=1,2,...,180)=</td></tr></table>

2.403e-05

Table 5 presents the results of the Liung-Box test for autocorrelation in errors at lags of 1 to $^ { 5 , }$ showing strong evidence of autocorrelation at all lags In Fig. 4, the smoothed approximation and underlying components are overlayed with the estimated hazard function. In Fig. 5, approximation errors over time are shown.

Table 5  
Ljung-Box Tests with Two Components.

<table><tr><td>Lag</td><td> $\chi^2(lag)$ </td><td>p-value</td></tr><tr><td>1</td><td>20.10188</td><td>&lt;0.0001</td></tr><tr><td>2</td><td>28.13450</td><td>&lt;0.0001</td></tr><tr><td>3</td><td>45.09870</td><td>&lt;0.0001</td></tr><tr><td>4</td><td>53.23925</td><td>&lt;0.0001</td></tr><tr><td>5</td><td>57.78371</td><td>&lt;0.0001</td></tr></table>

Deviations are more pronounced in Fig. $^ { 4 , }$ but both figures indicate similar deficiencies in the fitted model. The decomposition model un derestimates the hazard in the medium-term (30–105 days) and overestimates the hazard in the long-term (past 135 days). In the short term (0–15 days) the model fails to capture the initial peak of the hazard and then overestimates.

Overall, the decomposition model provides a poor description of the estimated hazard, showing poor ability to capture its dynamics. It is thus inappropriate for this model to be used to provide interpretable summaries of the hazard curve for decision-makers.

## Ethics

The research associated with this paper received ethics approval from the Bond University Human Research Ethics Committee. Ethics application number JT00253.

## References

[1] Medicare Payment Advisory Commission, Report to the Congress: Medicare and

[2] H.-P. Brunner-La Rocca, et al., Reasons for readmission after hospital discharge in patients with chronic diseases-information from an international dataset, PLoS One 15 (2020) e0233457, https://doi.org/10.1371/journal.pone.0233457.

[3] Centers for Medicare and Medicaid Services, Hospital Readmissions Reduction Program (HRRP), 2020 [cited 2021 May 6]; Available from: https://www.cms.go v/Medicare/Medicare-Fee-for-Service-Payment/AcuteInpatientPPS/Readmission s-Reduction-Program.

[4] Independent Hospital Pricing Authority, National Efficient Price Determination 2021–22, 2021.

[5] R.P. Jindal, D.K. Gauri, G. Singh, S. Nicholson, Factors influencing hospital readmission penalties: are they really under hospitals' control? Decis. Support Syst. 110 (2018) 58–70.

[6] S.R. Kristensen, M. Bech, W. Quentin, A roadmap for comparing readmission policies with application to Denmark, England, Germany and the United States, Health Policy 119 (3) (2015).264–273

[7] Medicare Payment Advisory Commission, Report to the Congress. Chapter 1: Mandated report: the effects of the Hospital Readmissions Reduction Program, 2018.

[8] C. Fischer, et al., Is the readmission rate a valid quality indicator? A review of the evidence, PLoS One 9 (11) (2014) e112282.

[9] A.M. Sheehy, et al., Health care policy that relies on poor measurement is ineffective: lessons from the hospital readmissions reduction program, Health Serv. Res, 58 (3) (2023) 549–553

[10] D. Kansagara, et al., Risk prediction models for hospital readmission: a systematic

[11] A. Artetxe, A. Beristain, M. Grana, ˜ Predictive models for hospital readmission risk: a systematic review of methods, Comput. Methods Prog. Biomed. 164 (2018) 49–64.

[12] Y. Huang, A. Talwar, S. Chatterjee, R.R. Aparasu, Application of machine learning in predicting hospital readmissions: a scoping review of the literature, BMC Med. Res. Methodol. 21 (1) (2021) 96.

[13] N. Ines Marina, et al., Applicability of predictive models for 30-day unplanned hospital readmission risk in paediatrics: a systematic review, BMJ Open 12 (3) (2022) e055956.

[14] O. Ben-Assuli, T. Heart, R. Klempfner, R. Padman, Human-machine collaboration for feature selection and integration to improve congestive Heart failure risk prediction, Decis. Support. Syst. 172 (2023) 113982.

[15] S. Romero-Brufau, et al., Implementation of artificial intelligence-based clinical decision support to reduce hospital readmissions at a regional hospital, Appl. Clin. Inform. 11 (4) (2020) 570–577

[16] L. Wang, et al., Predicting risk of hospitalization or death among patients with Heart failure in the veterans health administration, Am. J. Cardiol. 110 (9) (2012) 1342-1349.

[17] S. Yu, et al., Predicting readmission risk with institution-specific prediction models, Artif. Intell. Med. 65 (2) (2015) 89–96.

[18] A. Alassaad, et al., A tool for prediction of risk of rehospitalisation and mortality in the hospitalised elderly: secondary analysis of clinical trial data, BMJ Open 5 (2) (2015) e007259.

[19] A.D. Tulloch, A.S. David, G. Thornicroft, Exploring the predictors of early readmission to psychiatric hospital, Epidemiol. Psychiatr. Sci. 25 (2) (2016) 181–193.

[20] A. Alaeddini, J.E. Helm, P. Shi, S.H.A. Faruqui, An integrated framework for reducing hospital readmissions using risk trajectories characterization and discharge timing optimization, IISE Trans. Healthc. Syst. Eng. 9 (2) (2019) 172–185.

[21] H.M. Krumholz, et al., Do non-clinical factors improve prediction of readmission risk?: Results from the tele-HE study. JACC: Heart Failure 4 (1) (2016) 12–20.

[22] S. Hao, et al., Development, validation and deployment of a real time 30 day hospital readmission risk assessment tool in the maine healthcare information exchange, PLoS One 10 (10) (2015) e0140271.

[23] B. Padhukasahasram, C.K. Reddy, Y. Li, D.E. Lanfear, Joint impact of clinical and behavioral variables on the risk of unplanned readmission and death after a heart failure hospitalization, PLoS One 10 (6) (2015) e0129553.

[24] L. Pereira, et al., Unscheduled-return-visits after an emergency department (ED) attendance and clinical link between both visits in patients aged 75 years and over: a prospective observational study, PLoS One 10 (2015) e0123803, https://doi.org/ 10.1371/iournal.pone.0123803

[25] N.Q. Tran, et al., Leveraging deep survival models to predict quality of care risk in diverse hospital readmissions, Sci, Rep. 13 (1) (2023) 10479.

[26] X.-R. Liu. Y. Pawitan. M.S. Clements. Generalized survival models for correlated

[27] D. Pietzner, A. Wienke, The trend-renewal process: a useful model for medical recurrence data, Stat. Med. 32 (1) (2013) 142–152.

[28] J. Todd, A. Gepp, S. Stern, B.J. Vanstone, Improving decision making in the management of hospital readmissions using modern survival analysis techniques, Decis. Support. Syst. 156 (2022) 113747.

[29] V. Betihavas, et al., An absolute risk prediction model to determine unplanned cardiovascular readmissions for adults with chronic heart failure, Heart, Lung Circulat, 24 (11) (2015) 1068–1073

[30] D.J. Morgan, et al., Assessment of machine learning vs standard prediction rules for predicting hospital readmissions, JAMA Netw. Open 2 (3) (2019) e190348.

[31] J. Considine, et al., Factors associated with unplanned readmissions in a major Australian health service, Aust. Health Rey, 43 (1) (2019) 1–9.

[32] S. Radovanovi´c, et al., A framework for integrating domain knowledge in logistic regression with application to hospital readmission prediction, Int. J. Artif. Intell. Tools 28 (6) (2019).

[33] M. Deschepper, K. Eeckloo, D. Vogelaers, W. Waegeman, A hospital wide predictive model for unplanned readmission using hierarchical ICD data, Comput. Methods Prog, Biomed, 173 (2019) 177–183

[34] S. Kalagara, et al., Machine learning modeling for predicting hospital readmission following lumbar laminectomy, J. Neurosurg. Spine 30 (3) (2019) 344–352.

[35] M. Grzyb, et al., Multi-task cox proportional hazard model for predicting risk of unplanned hospital readmission, in: 2017 Systems and Information Engineering Design Symposium, SIEDS 201Z. 2017

[36] S. Rana, et al., Predicting unplanned readmission after myocardial infarction from routinely collected administrative hospital data, Aust. Health Rev. 38 (4) (2014) 377–382.

[37] M.F. Cunha Ferr´e, et al., 72-hour hospital readmission of older people after hospital discharge with home care services, Home Health Care Serv. Q. 38 (3) (2019) 153–161.

[38] J. Donz´e, D. Aujesky, D. Williams, J.L. Schnipper, Potentially avoidable 30-day hospital readmissions in medical patients: derivation and validation of a prediction model, JAMA Intern. Med. 173 (8) (2013) 632–638.

[39] H. Ahady Dolatsara, et al., A two-stage machine learning framework to predict heart transplantation survival probabilities over time with a monotonic probability constraint, Decis. Support. Syst. 137 (2020) 113363.

[40] K. Topuz, et al., Predicting graft survival among kidney transplant recipients: a Bayesian decision support model, Decis. Support. Syst. 106 (2018) 97–109.

[41] A. Dag, et al., Predicting heart transplantation outcomes through data analytics, Decis. Support. Syst. 94 (2017) 42–52.

[42] O.O. Aalen, H.K. Gjessing, Understanding the shape of the hazard rate: a process point of view, Stat. Sci. 16 (1) (2001) 1–14.

[43] D.R. Cox, Regression models and life-tables, J. R. Stat. Soc. B. Methodol. 34 (2) (1972) 187–220.

[44] O. Aalen, A linear regression model for the analysis of life times, Stat. Med. 8 (8) (1989) 907–925.

[45] O. Aalen, Further results on the non-parametric linear regression model in survival analysis, Stat. Med. 12 (17) (1993) 1569–1588.

[46] L.J. Wei, The accelerated failure time model: a useful alternative to the cox regression model in survival analysis, Stat. Med. 11 (14–15) (1992) 1871–1879.

[47] M. Leblanc, J. Crowley, Relative risk trees for censored survival data, Biometrics 48 (2) (1992) 411.

[48] A.M. Molinaro, S. Dudoit, M.J. van Der Laan, Tree-based multivariate regression and density estimation with right-censored data, J. Multivar. Anal. 90 (1) (2004) 154–177.

[49] M. Radespiel-Troger, ¨ T. Rabenstein, H.T. Schneider, B. Lausen, Comparison of treebased methods for prognostic stratification of survival data, Artif. Intell. Med. 28 (3) (2003) 323–341.

[50] J.A. Steingrimsson, L. Diao, A. Molinaro, R.L. Strawderman, Doubly robust survival trees, Stat. Med. 35 (20) (2016) 3595–3612.

[51] J.A. Steingrimsson, L. Diao, R.L. Strawderman, Censoring unbiased regression trees and ensembles, J. Am. Stat. Assoc. 114 (525) (2019) 370–383.

[52] R. Xu, S. Adak, Survival analysis with time-varying regression effects using a treebased approach, Biometrics 58 (2) (2002) 305–315.

[53] T. Hothorn, et al., Survival ensembles, Biostatistics 7 (3) (2006) 355–373.

[54] H. Ishwaran. U.B. Kogalur. Consistency of random survival forests, Stat. Prob. Lett 80 (13) (2010) 1056–1064.

[55] H. Ishwaran, U.B. Kogalur, E.H. Blackstone, M.S. Lauer, Random survival forests Ann. Appl, Stat. 2 (3) (2008) 841–860

[56] R. Zhu, M.R. Kosorok, Recursively imputed survival trees, J. Am. Stat. Assoc. 107 (497) (2012) 331–340.

[57] B. Efron. The efficiency of Cox's likelihood function for censored data, J. Am. Stat Assoc, 72 (359) (1977) 557–565.

James Todd is an Assistant Professor of Data Analytics at Bond University. As part of the Centre for Data Analytics, his research focuses on the application of advanced statistical, machine learning, and deep learning techniques to translate large and varied data sources into insights supporting organisational decision-making. In recognition of the need for effective analytics to include stakeholders throughout the process, partnerships with in dustry have been a theme of past work. Notable examples of such projects have included those in the healthcare space, such as the application of machine learning techniques to improve patient management. This work has been published in international journals such as Decision Support Systems and the International Journal of Medical Informatics.

Steven Stern is Professor of Data Science at the Bond Business School and Bond University Centre for Data Analytics. His research has covered a wide range of both theoretical and applied topics from asymptotic likelihood theory and resampling methods to probabilisti data integration and application of modern learning techniques to finance, sport science and health and medical informatics. He is the current custodian of the Duckworth-Lewis-Stern method used for setting fair targets in limited-overs cricket matches where play is interrupted by rain, Steven was awarded his PhD in Mathematical Statistics from Stanford University.
