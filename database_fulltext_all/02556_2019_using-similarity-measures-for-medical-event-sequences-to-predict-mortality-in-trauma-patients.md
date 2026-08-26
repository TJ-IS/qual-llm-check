---
otero_id: 2556
otero_key: "QJ3WKUN6"
title: "Using similarity measures for medical event sequences to predict mortality in trauma patients"
authors: "Joel Fredrickson; Michael Mannino; Omar Alqahtani; Farnoush Banaei-Kashani"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.10.008"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Using similarity measures for medical event sequences to predict mortality in trauma patients

![](/api/attachments/QJ3WKUN6/fulltext/images/6d61337dd5c787a0767b24f0e5a0269efb41e3e659e08fc5ffccf0dae747d00d.jpg)

Joel Fredrickson<sup>a</sup>, Michael Mannino<sup>a,⁎</sup>, Omar Alqahtani<sup>b</sup>, Farnoush Banaei-Kashani<sup>b</sup>

<sup>a</sup> Business School, University of Colorado Denver, United States of America

<sup>b</sup> Department of Computer Science and Engineering, University of Colorado Denver, United States of America

## A R T I C L E I N F O

Keywords: Medical event sequence Similarity measure Retrospective mortality prediction Trauma centers

## A B S T R A C T

We extend a similarity measure for medical event sequences (MESs) and evaluate its classification performance for retrospective mortality prediction of trauma patient outcomes. Retrospective mortality prediction is a benchmarking task used by trauma care governance bodies to assist with policy decisions. We extend the similarity measure, the Optimal Temporal Common Subsequence for MESs (OTCS-MES), by generalizing the event-matching component with a plug-in weighting element. The extended OTCS-MES uses an event prevalence weight developed in our previous study and an event severity weight developed for this study. In the empirical evaluation of classification performance, we provide a more complete evaluation than previous studies. We compare the predictive performance of the Trauma Mortality Prediction Model (TMPM), an accepted regression approach for mortality prediction in trauma data, to nearest neighbor algorithms using similarity measures for MESs. Using a data set from the National Trauma Data Bank, our results indicate improved predictive performance for an ensemble of nearest neighbor classifiers over TMPM. Our analysis reveals a superior Receiver Operating Characteristics (ROC) curve, larger AUC, and improved operating points on a ROC curve. We also study methods to adjust for uncommon class prediction: weighted voting, neighborhood size, and case base size. Results provide strong evidence that similarity measures for medical event sequences are a powerful and easily adapted method assisting with health care policy advances.

## 1. Introduction

## 1.1. Trauma care evaluation

This study involves mortality prediction for trauma centers, an important classification task having established methods. There is an essential focus on trauma care because trauma injuries are the leading cause of death in people younger than 44 and the fifth leading cause of death for all age groups [1]. Additionally, treatment methods for trauma related injuries are extremely costly, often leading to more expensive forms of care. The importance and cost of trauma care mandate benchmarks for trauma center performance relative to the injury severity of incoming patients. Cassidy et al. [2] maintain that “accurate injury severity scoring systems are essential for benchmarking outcomes and objectively evaluating and improving trauma care.”

With injury being the leading cause of lost years of life and escalating trauma care costs, improved trauma patient outcomes and streamlined care delivery are important objectives of researchers and policy makers. As such, the Trauma Care Systems Planning and Development Act was passed to improve trauma care and establish a Division of Trauma in the Department of Health and Human Services. Resulting regional trauma systems are designed to reduce mortality from injury. Furthermore, governance bodies, including the World Health Organization and the American College of Surgeons, provide consensus-based policy recommendations on the structure of trauma systems. This attention to trauma care has shown positive results with an estimated 15% reduction in the odds of mortality and decreases in both disability outcomes and costs [3]. Informed policy decisions by trauma governance bodies remain of utmost importance.

The method advanced in this research improves trauma policy decisions to help mitigate the “major knowledge gap on which components of a trauma system contribute to their efectiveness” [3]. We propose our method to more accurately evaluate trauma center performance to facilitate better policy decisions. In confirmation, trauma care administrators state the “the next logical step in the process of trauma system evaluation is to establish measures that consistently capture true outcome performance” and “evaluation of trauma system efectiveness will require ongoing outcome analysis in what must remain an uncompromising commitment to optimal outcome for the injured patient” [4].

## 1.2. Retrospective mortality prediction

Evaluating trauma care based on benchmarks for mortality rates, dependent upon injury severity, involves retrospective mortality pre diction. Retrospective mortality prediction methods for trauma care have “important clinical and economic implications because these tools are used to evaluate patient outcomes and quality of care” [5]. Essentially, retrospective mortality prediction enables governance bodies to measure trauma care delivery based on benchmark mortality rates for comparable patients or injury mix. Trauma centers demonstrating superior patient outcomes inform policy and resource allocation decisions concerning the various components of trauma care systems (transportation, triage, facility design, benchmarking, etc.). Retrospective eva luation of trauma care is a commonly researched area. A recent Google Scholar search using trauma + retrospective + “mortality prediction” since 2017, generated 674 articles in the result.

Typically for trauma care, mortality prediction models use historical incidents to correlate patient attributes and injury severity to known trauma discharge dispositions (deceased or non-deceased). Retrospective mortality prediction provides injury outcome benchmarks to help improve level of trauma care through more informed policy decisions. Trauma centers having superior performance, evidenced by comparatively low mortality rates, are surveyed to determine which components of trauma care systems are predominant. For example, studies [4] using retrospective mortality prediction have compared trauma care between (a) in-hospital facilities and external trauma centers, (b) level I and level II trauma centers, and (c) trauma centers in high and low-middle income countries. An example of a resulting policy change, from such studies, is continuation of a 2-tiered designation system for trauma care [6].

In addition to evaluating trauma center performance, retrospective mortality prediction enables study of mortality rates across patient cohorts. For example, Hashmi et al. [7] projected mortality rates from reference studies for an age group comparison of outcomes for trauma patients. In summary, retrospective mortality prediction establishes guidelines for appropriate outcomes from trauma care to help inform trauma care system policies. Accordingly, the research advanced in this study intends to improve established methods for trauma mortality prediction.

## 1.3. Mortality prediction using similarity measures

Because of the importance of mortality prediction for trauma centers, researchers have developed several prominent prediction methods. The most widely accepted method, the Trauma Mortality Prediction Model (TMPM), involves detailed regression modeling of individual injury codes using a large training sample. TMPM [1] uses derived coeficients for more than one thousand injury codes to make mortality predictions.

In this paper, we study an alternative approach to mortality prediction based on similarity of medical events in a patient's trauma incident. Our approach requires no exogenous data contained in linked EHRs but relies solely on data elements endogenous to the trauma in cident registry. Furthermore, predicting mortality based on incident similarity provides better explanation than regression prediction as si milar cases provide explanation of a prediction. Prediction based on similarity using nearest neighbor classification does not require training, although it requires indexing of trauma incidents for eficient computation of nearest neighbors. Alternatively, training is required to reduce the number of cases in a reference set.

## 1.4. Research methodology

We compare predictive performance of nearest neighbor classification using a similarity measure to TMPM, a prominent approach for mortality prediction in trauma data. In nearest neighbor classification, we use OTCS-MES with two weighting approaches (event prevalence and event severity), the original OTCS with only exact matching of event codes, and an ensemble using these three classifiers. We compare performance with three important measures: receiver operating characteristic (ROC) curves, area under a ROC curve (AUC), and operating points derived from a ROC curve. Results are based on a substantial data set from the National Trauma Data Bank. Our results indicate superior performance for an ensemble of nearest neighbor classifiers over TMPM on ROC curve analysis and AUC. For optimal operating points, the ensemble provides better performance than TMPM especially as the importance of sensitivity increases. We also study the impact of oversampled training data versus lifted voting for the uncommon mortality class, weighted voting, neighborhood size, and case base size.

## 1.5. Contributions

This study makes three important contributions. Most importantly, this study developed a new classification method with better performance than the accepted standard, TMPM. The ensemble of nearest neighbor classifiers obtained better performance than TMPM on ROC curves, AUC, and optimal operating points on a ROC curve. No studie have used nearest neighbor classification for mortality prediction with an uncommon mortality class. As an important secondary contribution, generalization of the event matching component of OTCS-MES makes event matching applicable to a wider variety of medical domains. As another secondary contribution, the detailed performance comparison provides a more complete analysis than previous studies. For example, prior studies neglected to compare performance on operating points on a ROC curve.

This paper continues as follows. The second section reviews prio work on mortality prediction for trauma centers and similarity measures for MESs. The third section presents the design of the experiment comparing nearest neighbor prediction with OTCS-MES to TMPM. The fourth section presents results of the experiment and discusses implications. The fifth section summarizes the paper and identifies future extensions.

## 2. Related work

To provide a context for the experiment design and results in the next sections, we review previous work on mortality prediction for trauma centers and similarity measures for MESs. We review early methods for mortality prediction (Injury Severity Score and Abbreviated Injury Scale) as well as two contemporary methods (the Bayesian Trauma Prediction Model and TMPM). The empirical evaluation incorporates the current industry standard, TMPM, and classifiers based on extending OTCS-MES.

## 2.1. Injury severity score and abbreviated injury scale

Because of the importance of mortality prediction for trauma centers, several severity-scoring systems have been developed. The Injury Severity Score, an early method for severity scoring, uses the Abbreviated Injury Scales to score injuries and predict trauma outcomes [2]. The International Classification of Diseases, Clinical Modification, version 9 (ICD-9-CM) is a more recent coding system that includes injury classifications. Because the National Trauma Data Standard now mandates ICD-9-CM, the Injury Severity Score method provides an option to use ICD-9-CM versus severity scores [1].

Alternative severity scoring models to the Injury Severity Score have been proposed. The International Classification of Diseases Injury

Severity Score uses empirically derived survival risk ratios for ICD-9- CM codes. This method calculates the proportion of survivors among patients having an ICD-9-CM injury code [1]. Another alternative approach, the Single-Worst Injury Model, focuses on injury assessment using a patient's single most severe injury. The single worst injury is commonly determined by the abbreviated injury score [8]. In preliminary injury scoring, the single worst injury was often used to predict outcomes. However, subsequent scoring systems leverage multiple injuries to contribute to outcome prediction [9].

## 2.2. Regression models for mortality prediction

Burd et al. [10] developed the Bayesian Logistic Injury Severity Score to leverage ICD-9-CM trauma coding with 2210 possible injury codes and 243,037 two-way interactions among injury codes. This model relies solely on ICD-9-CM codes without the need for psychological or supplementary data often input to other methods. Additionally, this methodology uses injury interactions, not just individual injury codes. Burd et al. [10] found slight improvements in prediction performance with the Bayesian Logistic Injury Severity Score compared to methods described previously, but much better model calibration with the Hosmer-Lemeshow h-statistic. Prediction performance was most apparent among patients at lower risk for mortality.

The Trauma Mortality Prediction Model (TMPM), a probit regres sion model, supports alternative injury codes and has shown improved predictive performance. TMPM uses approximately 1000 diferent types of injuries characterized by these coding sets. TMPM comprises two separate probit models. Model 1 uses all possible injuries as binary predictors with death as the binary outcome. Model 2 uses indicators of body region severity. A weighted average of the coeficients of the two regression models provides the empirical severity for each injury. Empirical analysis showed that TMPM provided superior performance than other ICD-9-CM based models. However, analysis in previous studies omitted analysis of operating points. Superior predictive performance of TMPM was most noted as the number of injuries increased [2]. In this study, we use TMPM because of its performance and availability. The R implementation of TMPM facilitated usage in our experiments (https://cran.r-project.org/web/packages/tmpm/tmpm. pdf).

## 2.3. Optimal temporal common subsequence for medical event sequences

In previous research, we developed a similarity measure for MESs known as the Optimal Temporal Common Subsequence for Medical Event Sequences (OTCS-MES). Its development was motivated by limitations in other proposed methods, particularly the original OTCS [11]. In a detailed empirical evaluation [12], we compared OTCS-MES to the original OTCS and Artemis, a measure incorporating event alignment. This comparison used inpatient MESs with ICD-9-CM codes and outpatient MESs with procedure codes. Overall, we found a small overlap in nearest neighbors among the three similarity measures, demonstrating the superior design of OTCS-MES with its emphasis on unique aspects of medical events. With extreme weighting on just the event matching components of OTCS and OTCS-MES, simple overlap rates for shared nearest neighbors ranged from 25% for small neighborhood sizes (5) to 40% for large neighborhood sizes (50) in inpatient data and 60% for large neighborhood sizes in outpatient data.

The evaluation in our previous study [12] never investigated classification performance. Although OTCS-MES contains components for both event similarity and temporal structure similarity, this study only uses the event-matching component because trauma incidents are reported without timing of incident events. To use OTCS-MES for classification, we generalize it to provide a level of domain customization. Unique to trauma prediction, we use event severity weighting in addition to event prevalence weighting. This generalization of weights for event matching allows the use of OTCS-MES in a wider variety of medical domains.

## 3. Design of empirical evaluation

This section explains the research methodology for evaluating the performance of similarity-based classification on trauma mortality prediction. Our objective is to determine whether nearest neighbor classification, using MES adapted similarity measures, is a viable method to assess trauma care and inform governance policy makers in a critical health domain. Our research methodology is basically twofold: first we perform secondary research to arrive at the best classification method, then we perform primary research to evaluate our optimal predictive method against alternative similarity measures and the industry standard for trauma outcome prediction, TMPM. The design of our classification method using similarity measures is secondary research because it supports our primary research goal of performance valuation for similarity measure classification as a predictive method.

## 3.1. Overview of research methodology

Initially, our research methodology concerns the use of MES similarity measures to find like trauma incidents based on injury (event) sequence matching. We first explain similarity measures and their application within nearest neighbor classification to predict trauma outcomes (Sections 3.2 and 3.3). We then turn to our secondary research, aimed at designing the most efective approach to classification pre diction of uncommon mortality in trauma incidents (Section 3.4). Specifically, we evaluate and select the following parameters for our classification method:

• Voting method for nearest neighbor trauma incidents - traditional majority voting or soft voting with proportional weights.

• Size for nearest neighbor cohort - 1 through 49 (odd only).

Adjustment method for imbalanced data - majority voting, oversampling, or certainty-factor voting.

Case base size - 5000, 10,000 or 50,000 training incidents and 2000 test incidents.

After defining the best kNN nearest neighbor classification method based on secondary research, we move on to our primary research evaluating trauma mortality prediction using our alternative method. We start by presenting our primary research hypotheses for OTCS-MES performance (Section 3.5). Performance is evaluated against both the industry gold standard TMPM, and among the various similarity measure approaches (original OTCS exact matching, and OTCS-MES prevalence and severity weighted partial matching). The research methodology section continues by detailing the trauma data used for our empirical evaluation and associated data filters required for an equitable empirical evaluation (Section 3.6). Finally, we present the performance measures chosen to evaluate our alternative predictive method (Section 3.7).

## 3.2. Similarity measures for medical event sequences

This study uses three similarity measures, the original OTCS, OTCS-MES with event prevalence weights (OTCS-MES EP), and OTCS-MES with event severity weights (OTCS-MES ES). Although all three measures contain components for event matching and temporal structure of events, this study only uses the event-matching component because trauma records do not have a temporal structure.

## 3.2.1. Original OTCS

The original Optimal Temporal Common Subsequence (OTCS), developed by Zheng et al. [11], uses exact matching for events. Given a state-sequence defined as $S _ { n } = [ s _ { 1 } , ~ . . . , ~ s _ { \mathrm { n } } ]$ , the OTCS compares two state-sequences $S _ { m }$ and $S _ { n } ^ { \prime }$ based upon exact matching of the states (events) within S and S′ [11]. Therefore, when applied to MESs, the original OTCS would require that an ICD-9-CM code match exactly in

both length and content.

Although the OTCS was motivated by temporally spaced state sequences, the hierarchical nature of MESs was not utilized in the measure. Thus, the OTCS does not incorporate partial event matching, only counting the number of exact (non-partial) matches between event sequences. For example, if one MES contains ICD-9-CM code 250.00 and a second MES contains ICD-9-CM code 250.01, the original OTCS would not find a match although they represent highly related medical events. In addition, the OTCS does not allow weighting of matched events in its event matching component. For example, if two MESs share medical events 250.01 and 279.00, these matched events are given equal weight by the original OTCS. The original OTCS simply counts matched events, regardless of event likelihood, risk, or severity.

## 3.2.2. OTCS-MES with prevalence weights (OTCS-MES EP)

In contrast to the original OTCS, OTCS-MES integrates unique features of MESs. OTCS-MES provides a matching component that integrates event prevalence, event duplication, and hierarchical coding, important elements of MESs. Event prevalence, normalized to mitigate heavy positive skew and compact distribution, provides weights for matched events. Partial matching captures similarity based on the hierarchical organization of event codes, increasing similarity beyond exact matching. For example, if one MES contains ICD-9-CM code 250.00 and a second MES contains ICD-9-CM code 250.01, OTCS-MES considers these events matching at the 4-digit level but not at the 5- digit level (most specific ICD-9-CM codes).

The event matching component in [12] uses normalized event prevalence weighting. Since this paper just uses event matching, the other components of OTCS-MES are ignored. Eq. (1) shows the definition of the event matching component using event prevalence (OTCS-MES EP). In the numerator, the event matching component sums prevalence weights in the numerator and accounts for the number of matched events in the denominator. The denominator value is the maximum matched events across all MES pairs plus one, less the number of matched events between the two MESs under consideration.

$$
O T C S - M E S E P = \left(\frac {\sum_ {e   i n   M E} ^ {M S S i z e} N P W _ {e}}{\max _ {C} \sum_ {e   i n   C} ^ {M S S i z e} N P W _ {e}}\right) / (P D M + 1 - M S S i z e L i m i t)\tag{1}
$$

where

ME is the set of all matching events in the pair of cases (medical event sequences),

C is set of all cases, and

MSSize is the cardinality of the associated set.

● $N P W _ { e }$ is the normalized prevalence weight of event e,

PDM is the maximum matched event limit, and

• MSSizeLimit is the number of event matches in the pair of case constrained by the matched event limit.

Event prevalence weighting presumes that rarer events matched between two MESs indicate greater similarity than more common matched events. OTCS-MES EP calculates individual event likelihood or prevalence using the complete set of trauma incident events and associated diagnosis codes described in the Section 3.4. An event's pre valence weight is one minus the event's frequency rate, so larger values (weights) indicate rarer events. OTCS-MES EP normalizes the summation of prevalence weights of matched events by the maximum prevalence weight summation across all MES pairs. Additionally, OTCS-MES EP retains replicated matched events versus the original OTCS measure that removes replicated event matches.

## 3.2.3. OTCS-MES with severity weighting

For trauma data, event severity provides intuitive appeal to weight matching events for mortality prediction. As previously presented, early methods for mortality prediction incorporated injury scoring systems with event severity. Reference literature identified two important factors for injury scoring, injury type and anatomical body region. Injury type describes the nature of the injury and includes values such as contusion, sprain, open wound, and dislocation. Body region involves the anatomical area of the body injured, such as head and neck, spine and back, torso, and extremities. Based on these two variables, Barell et al. [13] developed a matrix having nature of injury columns, body region rows, and ICD-9-CM injury codes in each cell. As an extension to this work, Clark and Ahmad [14] assigned a survivor proportion to each cell of the Barell matrix.

Our study uses the Clark/Ahmad extension with survivor proportions assigned to each ICD-9-CM injury code. A severity weight equals one minus the survivor proportion, with larger values indicating more severe events. Eq. (2) defines OTCS-MES ES, a revision of OTCS-MES EP, for severity weights. Essentially, we are replacing the prevalence weight for a matched event, as shown in Eq. (1), with the severity weight for that same matched event. We then sum the severity weights for all matched events between our MESs under consideration and normalize this value according to the maximum severity weight summation value across all MES pairs.

$$
O T C S - M E S E S = \left(\frac {\sum_ {e i n M E} ^ {M S S i z e} S W _ {e}}{\max _ {C} \sum_ {e i n C} ^ {M S S i z e} S W _ {e}}\right) / (P D M + 1 - M S S i z e L i m i t)\tag{2}
$$

where

• ME is the set of all matching events in the pair of cases (medical event sequences),

• C is set of all cases,

• MSSize is the cardinality of the associated set,

$S W _ { e }$ is the normalized severity weight of event $e ,$

• PDM is the maximum matched event limit, and

• MSSizeLimit is the number of event matches in the pair of cases constrained by the matched event limit.

## 3.3. Nearest neighbor classification for mortality prediction

The kNN classification algorithm [15] provides a simple but computationally intense approach for classification using a distance function. To make classification decisions, the kNN classification algorithm uses a neighborhood of k nearest neighbors with majority voting among the k neighbors. In this study, inverted similarity measures (1 – similarity) were used as distance measures. The kNN classification algorithm requires no training so it is lazy. However, it uses all cases to classify new cases so it requires large storage space and high search cost to retrieve nearest neighbors. Search cost can be substantially reduced by indexing so that indexing can be considered a training cost, qualifying the designation as a lazy learning algorithm. To reduce computational requirements for large case bases, we created indexes for creation and search of dissimilarity matrices.

kNN classification has low bias but high variance [16]. The decision boundaries in kNN vary in a nonlinear manner, providing flexibility for classification decisions. Each case has a positive probability of correct classification for some training sets. In contrast, kNN classification has high variance with sensitivity to noise in relevant attributes. Classification algorithms with high variance tend to overfit. For kNN, distance function, neighborhood size, and case base size influence bias and variance, emphasizing the importance of these choices.

To improve prediction performance, we use two variations of nearest neighbor classification. Weighted voting allows more impact for neighbors close to a target case and less impact for far neighbors. The main benefit of weighted voted is less sensitivity to neighborhood size.

We use proportional weights defined by Dudani [17] as an alternative to traditional equal weighting voting.

Ensembles combine predictions of individual classifiers typically using weighted voting among classifiers on each case. Ensembles improve classification results for diverse classifiers with diferent biases. Many ensemble methods have been proposed for nearest neighbor classification, using both training and voting to combine individual classifiers [18]. We use a soft voting ensemble (scikit-learn.org/table/ modules/ensemble.html) with cases labeled according to sum of pre dicted scores. This ensemble involves additional classification resources, as it requires determination of nearest neighbors for each component classifier.

## 3.4. Secondary research - accommodating the uncommon mortality class

Despite the serious nature of patients admitted to trauma centers, mortality is uncommon. Treatment at a trauma center is short-term so only death between admittance and discharge counts as mortality. Patients dead on arrival and discharged to another facility do not count in the mortality disposition recorded in trauma data. After adjusting for death outside of the trauma center window, missing data, small trauma centers, and few diagnosis codes, the deceased prevalence in our sample data was 6.28%.

Over sampling of the uncommon class provides a typical strategy for dealing with imbalanced data. Although Maloof [19] indicates some conflicts in results of over versus under sampling, the availability of cases for the uncommon class drives usage of over sampling. Since ample data was available, we used over sampling to deal with the uncommon mortality class. Specifically, we used the Over-Sampling Op timum Fraction [20] to increase the proportion of mortality events in training data. Eq. (3) defines the Kalton Over-Sampling Optimum Fraction $f _ { h }$ for class h where $P _ { h }$ is the prevalence of the uncommon class and c is the ratio of the data collection costs per case of the uncommon to the common class. Using Eq. (3) with the trauma mortality prevalence of 6.28% and equal data collection costs yields an optimum sampling fraction of 25.07%.

$$
f h \propto \sqrt {\frac {P h}{P h (c - 1) + 1}}\tag{3}
$$

A second strategy for dealing with an uncommon class modifies the majority voting rule. When the prevalence of the uncommon class cannot be adjusted, a modified voting rule can compensate for the scarcity of cases of the uncommon class. Zhang [21] proposed kNN-CF, with certainty-factor voting for imbalanced data. kNN-CF classification accounts for the lift in proportion of extreme outcomes among the k nearest-neighbors over the proportion of extreme outcomes in the population as a whole. In our experiment, we also used certainty factor voting as an alternative to adjust for the uncommon mortality class.

## 3.5. Primary research – Evaluating trauma mortality prediction using similarity measures

This study asserts that a similarity measure adapted to medical event histories can be a valuable method to evaluate trauma care and inform strategic policy. Trauma centers more correctly identified as superior performers serve as better examples for those centers performing less well, based on anticipated mortality rates. Within this broad assertion, this experiment addresses the predictive capability of MES-adapted similarity measures for the classification of trauma in cident outcomes using the incident's bundle of event codes only. We are interested in comparisons involving the predictive performance of classifiers using individual similarity measures (OTCS, OTCS-MES EP, and OTCS-MES ES), the existing standard for trauma morbidity pre diction (TMPM), and an ensemble of nearest neighbor classifiers using individual similarity measures. We aim to observe improved prediction performance for OTCS-MES over TMPM and improved prediction ability of OTCS-MES relative to the original OTCS. The following list presents hypotheses concerning predictive performance.

1. TMPM, as the recognized best method, performs better than the MES similarity measures (OTCS, OTCS-MES EP, OTCS-MES ES, and OTCS ensemble).

As explained previously, TMPM was designed specifically to predict mortality for trauma center incidents. Its derivation, based on a large amount of trauma data, contains two probit regression models accounting for the type of injury and body region for the injury. According to Glance et al. [1], since TMPM-ICD9 performs better than ICISS and the SWI model, it should be preferred to them for risk-adjusting trauma outcomes when injuries are recorded using ICD-9-CM codes. Furthermore, Cassidy et al. [2] confirms the superiority of TMPM for injury scoring of pediatric patients especially as the number of injuries increases. Because NTDB mandates ICD coding for trauma incidents, TMPM should continue as the preferred method for trauma incident prediction.

2. OTCS-MES, adapted to medical event sequences, performs better than the original OTCS similarity measure on morbidity prediction.

Unlike the original OTCS similarity measure, OTCS-MES allows generalized weighting of matched event and partial matching. These two capabilities should result in improved prediction on trauma morbidity prediction. Despite these shortcomings, the OTCS may still identify the most important matching events to predict mortality in trauma patients. Lack of coding detail negates the advantage of weighted, partial matching. Coding detail depends on data collection practices at trauma centers and perhaps beyond trauma centers with some ICD codes reported in a patient's medical record before a trauma incident occurs. The original OTCS may match predictive performance of OTCS-MES with large amounts of cases and large neighborhood sizes.

3. OTCS-MES using event severity weighting (OTCS-MES ES) performs better than the OTCS-MES using event prevalence weighting (OTCS-MES EP).

Injury severity is an appropriate weighting method for scoring trauma incidents based on referential literature. Also, injury severity has already been quantified by several scoring systems. Most recently, scoring systems based on ICD-9-CM codes and incorporating injury type and anatomical region have been found efective in classification experiments [22]. OTCS-MES ES, using an event severity score (the Barell matrix survivor proportion), should demonstrate improved performance for trauma incident classification.

4. The best ensemble combining individual similarity classifiers should perform better than individual similarity-based classifiers.

Ensembles improve performance of diverse classifiers. We expect enough diversity between event matching based on exact matching, normalized event prevalence with partial matching, and event severity with partial matching to achieve improved prediction results.

Table 1 summarizes choices for algorithm voting, neighborhood size, adjustment method for imbalanced data, and case base size. The secondary investigation determines best choices for these variables. The secondary analysis on neighborhood size also indicates if trauma data contain noise where sensitivity to small neighborhood sizes (1 to 5) reflects noisy data.

## 3.6. Trauma data set

Hospital-based trauma registries provide a foundation for much research about improving care of injured patients. Research has been limited by the lack of consistent, quality data received from disparate hospitals, regions, and states. To address this limitation, the American College of Surgeons developed the National Trauma Data Standard (www.facs.org/quality-programs/trauma/ntdb/ntds) to standardize core variables across hospitals. A wide variety of trauma centers contribute to the National Trauma Data Bank (www.facs.org/quality programs/trauma/ntdb), a large aggregation of trauma data conforming to the National Trauma Data Standard.

Table 1  
Summary of Variables for Secondary Research Questions.

<table><tr><td>Variable</td><td>Choices</td></tr><tr><td>Nearest neighbor algorithm voting</td><td>Traditional majority voting and soft voting with proportional weights</td></tr><tr><td>Neighborhood size (k)</td><td>1 to 49 (odd only)</td></tr><tr><td>Adjustment method for imbalanced data</td><td>Majority voting, Oversampling, CF voting</td></tr><tr><td>Case base size</td><td>5000, 10,000, 50,000</td></tr></table>

Table 3  
Summary of Diagnosis Detail in Trauma and Inpatient Data.

<table><tr><td>Length of diagnosis code</td><td>Inpatient events (# of diagnosis codes)</td><td>Inpatient events (% of total)</td><td>Trauma events (# of diagnosis codes)</td><td>Trauma events (% of total)</td></tr><tr><td>3 Digits</td><td>1988</td><td>5.31%</td><td>1588</td><td>3.52%</td></tr><tr><td>4 Digits</td><td>13,337</td><td>35.61%</td><td>23,026</td><td>51.06%</td></tr><tr><td>5 Digits</td><td>22,123</td><td>59.08%</td><td>20,478</td><td>45.41%</td></tr><tr><td>Total</td><td>37,448</td><td>100.00%</td><td>45,092</td><td>100.00%</td></tr></table>

Table 2  
Summary of Filtered Trauma Data using the National Trauma Data Bank.

<table><tr><td></td><td>2015 trauma incidents remaining</td></tr><tr><td>Original data set</td><td>917,865</td></tr><tr><td>(1) Excluded incidents with all diagnoses being non-trauma (based on MARC table)</td><td>728,309</td></tr><tr><td>(2) Excluded incidents for patients w/age &lt; 1 year, or missing age or gender</td><td>685,587</td></tr><tr><td>(3) Excluded incidents with missing discharge disposition (HOSPDISP n/a)</td><td>590,288</td></tr><tr><td>(4) Excluded incidents w/patient DOA or w/transfer to another facility</td><td>427,545</td></tr><tr><td>(5) Excluded incidents for facilities handling &lt; 500 incidents during the year</td><td>403,534</td></tr><tr><td>(6) Excluded incidents having fewer than 5 diagnosis (event) codes</td><td>175,319</td></tr><tr><td>(6a) Deceased disposition (6.28%)</td><td>11,010</td></tr><tr><td>(6b) Non-deceased disposition (93.72%)</td><td>164,309</td></tr></table>

## 3.6.1. Data filters

We used the National Trauma Data Bank for our morbidity predic tion experiment. Specifically, we randomly selected various test and training data from the complete set of 2015 trauma incidents in the trauma registries for 2015. Table 2 summarizes filters applied to the trauma data, consistent with filters in [1]. We apply these filters to ensure that all methods, including those developed by other researchers, are using equivalent evaluation data.

As further corroboration, Burd et al. [10] applied these same data filters during development of the Bayesian Logistic Injury Severity Score. The final filter excluding trauma incidents having less than five diagnosis codes (events) is applied in accord with TMPM which uses the five most severe injury codes in its regression.

From the 175,319 incidents having at least five events, we randomly selected 50,000 trauma incidents for a case base and 2000 cases for testing. The training data set contains 465,325 total diagnosis codes (4053 unique ICD-9-CM codes). We used the same test set to evaluate all hypotheses. Due to a shortage of deceased cases, the case base contained only a prevalence of 22%, yielding 10,900 deceased cases.

## 3.6.2. ICD-9-CM code granularity

OTCS-MES uses hierarchical matching that leverages the more detailed diagnoses provided by 4- and 5-digit ICD-9-CM codes. The level of coding detail in a data set afects the predictive performance of OTCS-MES compared to OTCS. As shown in Table 3, inpatient data<sup>1</sup> contains more detailed codes (59% are 5-digits in length) than the trauma data (45% are 5-digits in length). However, trauma data contains a lower percentage of 3-digit codes (3.5%) than inpatient data (5.3%). Based on these results, OTCS-MES (EP and ES) may lose some advantage over OTCS due to the reduced level of diagnosis code detail for trauma incident data.

## 3.7. Performance measures

For statistical evaluations, we use Area under the Receiver Operating Characteristic Curve (AUROC or AUC) as the primary performance measure. AUC provides a prevalence independent measure of discrimination ability in risk prediction models. AUC has several equivalent interpretations including the expectation that a uniformly drawn random positive example ranks higher than a uniformly drawn negative example. Calculation of AUC requires a ROC curve of classification scores. For nearest neighbor algorithms, we used voting proportions among nearest neighbors as classification scores. We performed two-tailed tests of AUC using Mann-Whitney confidence intervals augmented with the Logit transformation [23]. In a detailed simulation study [24], the augmented Mann-Whitney intervals provided good AUC coverage, robustness to unbalanced sample sizes and normality departures, and reasonable power.

Although AUC is widely recognized as a measure of discrimination ability, it does not provide an operating point for a classifier. To deploy a classifier, one must select an operating point corresponding to a score threshold. Each ROC point has an associated confusion matrix char acterizing positive and negative predictions using the scoring threshold. In our experiment, we evaluated operating points using three measures, Youden's J statistic (also known as Youden's Index), the weighted Youden's Index, and the Neyman-Pearson criterion. Youden's index [25], computed as sensitivity + specificity −1, ranges from −1 to 1. A value of 1 indicates a perfect test with no false positives or false negatives. Li et al. [26] introduced the weighted Youden's Index when sensitivity and specificity are not equally important. In this study, the importance of predicting a trauma incident outcome of deceased correctly (sensitivity) is more important than predicting a non-deceased outcome. Although dificult to quantify, trauma center morbidity is a costlier outcome in both treatment options and risk [27]. In contrast to the tradeof in the Youden's Index, the Neyman-Pearson criterion [28] maximizes sensitivity at false positive constraint levels.

Table 4  
Comparison of Over-Sampled and Imbalanced Training Data $( k = 1 5 ) .$

<table><tr><td>Similarity measure</td><td>Sensitivity</td><td>Specificity</td><td>Accuracy</td><td>Youden</td><td>AUC</td></tr><tr><td colspan="6">Over-sampled trauma data</td></tr><tr><td>OTCS</td><td>0.8341</td><td>0.4106</td><td>0.4339</td><td>0.2447</td><td>0.7300</td></tr><tr><td>OTCS-MES EP</td><td>0.7795</td><td>0.5566</td><td>0.5689</td><td>0.3362</td><td>0.7719</td></tr><tr><td>OTCS-MES ES</td><td>0.7227</td><td>0.5960</td><td>0.6030</td><td>0.3188</td><td>0.7939</td></tr><tr><td>Average</td><td>0.7788</td><td>0.5211</td><td>0.5353</td><td>0.2999</td><td>0.7652</td></tr><tr><td colspan="6">Imbalanced (normal) trauma data</td></tr><tr><td>OTCS</td><td>0.4464</td><td>0.6515</td><td>0.6383</td><td>0.0979</td><td>0.6755</td></tr><tr><td>OTCS-MES EP</td><td>0.3960</td><td>0.7215</td><td>0.7005</td><td>0.1174</td><td>0.7049</td></tr><tr><td>OTCS-MES ES</td><td>0.4643</td><td>0.6976</td><td>0.6826</td><td>0.1619</td><td>0.7288</td></tr><tr><td>Average</td><td>0.4356</td><td>0.6902</td><td>0.6738</td><td>0.1257</td><td>0.7031</td></tr></table>

## 4. Results of empirical evaluation

This section presents results of the empirical evaluation covering the primary and secondary research questions. Results of the secondary research questions are presented first as the primary research questions use results from the investigation of the secondary questions.

## 4.1. Secondary research - accommodating the uncommon mortality class

The results begin with an analysis of imbalanced versus over-sam pled trauma data for training. We compare average performance for methods dealing with imbalanced data (over-sampled data and certainty-factor voting). Results in Tables 4 and 5 use kNN with a neigh borhood size (k) of 15. In Table 4, using average results across voting methods, over-sampled training demonstrates improved performance based on Youden's Index (0.30 versus 0.13), along with AUC (0.7652 versus 0.7031). Furthermore, over-sampled data improves the key metric in trauma incident prediction of sensitivity (0.7788 versus 0.4356). In accordance with Kalton [20], these results suggest that over-sampled training delivers improved predictive performance on trauma morbidity across the three similarity measures.

Table 5 shows that changing the voting method between majority and certainty-factor has minimal impact on predictive performance. Certainty factor and majority voting have similar average values across sampling methods, for both Youden's Index and AUC. Interestingly, certainty-factor voting provides substantial improvements in sensitivity for mortality prediction, but much lower results for specificity and accuracy.

Weighted voting improves predictive performance as shown in Table 6. For the moderate neighborhood size (k = 15), weighted voting provides better performance for AUC, Youden's Index, and sensitivity. For the large neighborhood size (k = 49), weighted voting improves AUC performance. Weighted voting provides more improvements on smaller neighborhoods demonstrating some sensitivity of nearest neighbor classification to the neighborhood size. Since AUC is the pri mary performance measure, the primary investigation uses weighted voting for each similarity measure.

To gain insight about the sensitivity of neighborhood size (k), we increased neighborhood sizes (odd values only) from 1 to 49, and then measured AUC for each k value. Fig. 1 illustrates the impact of in creased neighborhood size on AUC for each classification algorithm. All three similarity measures demonstrate improved performance with larger neighborhood sizes. Performance gains remain level for OTCS-MES EP and OTCS-MES ES after $\mathbf { k } = 2 9$ . For OTCS, performance in creases slightly until leveling of at k = 45. Fig. 2 provides additional insight into the impact of increased neighborhood size on the two techniques for dealing with imbalanced data, over-sampling and certainty-factor voting. Again, increased neighborhood size improves AUC performance for both techniques dealing with imbalanced data. The variability of predictive performance indicates some instability of nearest-neighbor classification in trauma data.

In the last part of the secondary analysis, we compared several case

Table 5  
Comparison of Certainty-Factor and Majority Voting $( \mathbf { k } = 1 5 ) .$

<table><tr><td>Similarity measure</td><td>Sensitivity</td><td>Specificity</td><td>Accuracy</td><td>Youden</td><td>AUC</td></tr><tr><td colspan="6">Majority voting</td></tr><tr><td>OTCS</td><td>0.3656</td><td>0.8169</td><td>0.7876</td><td>0.1825</td><td>0.7049</td></tr><tr><td>OTCS-MES EP</td><td>0.3283</td><td>0.8762</td><td>0.8415</td><td>0.2045</td><td>0.7429</td></tr><tr><td>OTCS-MES ES</td><td>0.3149</td><td>0.9192</td><td>0.8818</td><td>0.2341</td><td>0.7615</td></tr><tr><td>Average</td><td>0.3362</td><td>0.8708</td><td>0.8369</td><td>0.2070</td><td>0.7364</td></tr><tr><td colspan="6">Certainty-factor voting</td></tr><tr><td>OTCS</td><td>0.9149</td><td>0.2452</td><td>0.2846</td><td>0.1601</td><td>0.7007</td></tr><tr><td>OTCS-MES EP</td><td>0.8472</td><td>0.4019</td><td>0.4279</td><td>0.2491</td><td>0.7339</td></tr><tr><td>OTCS-MES ES</td><td>0.8721</td><td>0.3744</td><td>0.4038</td><td>0.2466</td><td>0.7612</td></tr><tr><td>Average</td><td>0.8781</td><td>0.3405</td><td>0.3721</td><td>0.2186</td><td>0.7319</td></tr></table>

## Table 6

Comparison of Weighted and Non-Weighted Voting.

<table><tr><td>Similarity measure</td><td>Sensitivity</td><td>Specificity</td><td>Accuracy</td><td>Youden</td><td>AUC</td></tr><tr><td colspan="6">Weighted voting based on similarity measure value (k = 15)</td></tr><tr><td>OTCS</td><td>0.8182</td><td>0.5545</td><td>0.5690</td><td>0.3727</td><td>0.7573</td></tr><tr><td>OTCS-MES EP</td><td>0.7455</td><td>0.6360</td><td>0.6420</td><td>0.3814</td><td>0.7658</td></tr><tr><td>OTCS-MES ES</td><td>0.7545</td><td>0.7238</td><td>0.7255</td><td>0.4784</td><td>0.8066</td></tr><tr><td>Average</td><td>0.7727</td><td>0.6381</td><td>0.6455</td><td>0.4108</td><td>0.7766</td></tr><tr><td colspan="6">Non-weighted voting (k = 15)</td></tr><tr><td>OTCS</td><td>0.3656</td><td>0.8169</td><td>0.7876</td><td>0.1825</td><td>0.7049</td></tr><tr><td>OTCS-MES EP</td><td>0.3283</td><td>0.8762</td><td>0.8415</td><td>0.2045</td><td>0.7429</td></tr><tr><td>OTCS-MES ES</td><td>0.3149</td><td>0.9192</td><td>0.8818</td><td>0.2341</td><td>0.7615</td></tr><tr><td>Average</td><td>0.3362</td><td>0.8708</td><td>0.8369</td><td>0.2070</td><td>0.7364</td></tr><tr><td colspan="6">Weighted voting based on similarity measure value (k = 49)</td></tr><tr><td>OTCS</td><td>0.7455</td><td>0.6783</td><td>0.6820</td><td>0.4238</td><td>0.7722</td></tr><tr><td>OTCS-MES EP</td><td>0.7000</td><td>0.6995</td><td>0.6995</td><td>0.3995</td><td>0.7921</td></tr><tr><td>OTCS-MES ES</td><td>0.7091</td><td>0.7228</td><td>0.7220</td><td>0.4318</td><td>0.8255</td></tr><tr><td>Average</td><td>0.7182</td><td>0.7002</td><td>0.7012</td><td>0.4184</td><td>0.7966</td></tr><tr><td colspan="6">Non-weighted voting (k = 49)</td></tr><tr><td>OTCS</td><td>0.7545</td><td>0.6302</td><td>0.6370</td><td>0.3847</td><td>0.7545</td></tr><tr><td>OTCS-MES EP</td><td>0.7455</td><td>0.6873</td><td>0.6905</td><td>0.4328</td><td>0.7455</td></tr><tr><td>OTCS-MES ES</td><td>0.7364</td><td>0.7947</td><td>0.7915</td><td>0.5311</td><td>0.8191</td></tr><tr><td>Average</td><td>0.7455</td><td>0.7041</td><td>0.7063</td><td>0.4495</td><td>0.7730</td></tr></table>

base sizes to gain insights about performance improvements with a larger number of cases. Fig. 3 indicates mixed results with additional cases having small improvements for some classifiers, but slightly worse performance for other classifies. Since 50,000 cases provide a noticeable improvement for OTCS, we use the largest case base in analysis of primary research questions.

The primary research results, presented in the next subsection, use the sampling, voting and classification methods recommended by our secondary research. Specifically, our secondary analysis suggests a classification methodology that involves (1) over-sampled training based on the Kalton Optimum Sampling Fraction, (2) weighted nearestneighbor voting, (3) large neighborhood size $\left( \mathbf { k } > 4 1 \right)$ , and (4) large case base (50,000).

## 4.2. Primary research – Evaluating trauma mortality prediction using similarity measures

## 4.2.1. Analysis of AUC

Table 7 presents confidence intervals<sup>2</sup> and related p values addressing the primary hypotheses. For Hypothesis 1, the results show efects for TMPM compared to each individual OTCS measure and the OTCS ensemble. For Hypothesis 2, the results show efects for both OTCS-MES EP and OTCS-MES ES versus OTCS. For Hypothesis 3, test results show efects between OTCS-MES EP and OTCS-MES ES at an alpha of 0.10.

![](/api/attachments/QJ3WKUN6/fulltext/images/e312761cba690b8e4f230215c8df1dba19a0c929387baf0fd9f55a95febb6646.jpg)

![](/api/attachments/QJ3WKUN6/fulltext/images/063eb76ba90e48457dc409e6715c0fbc7d2a8b193297bb19ec59adc697630e0b.jpg)  
Fig. 1. Comparison of Similarity Measures by Neighborhood Size (k).

For Hypothesis 4, test results show efects for all three classifiers versus the ensemble classifier, demonstrating suficient diversity among in dividual classifiers.

ROC curves provide a visual representation of performance diferences. In Fig. 4, the ROC curve for the ensemble dominates all other ROC curves except for two small intervals. The ROC curve for TMPM dominates the ROC curves for OTCS and OTCS-EP at false positive values below 0.40. For false positive values above 0.5. the ROC curves switch with the two similarity measures dominating TMPM. The ROC curves for TMPM and OTCS-MES ES cross in several areas with OTCS MES showing a small advantage at low false positive values, but TMPM showing a small advantage at larger false positive values.

## 4.2.2. Analysis of operating points

For insight about operating points on a ROC curve, we examine results across score thresholds. Fig. 6 shows Youden's Index values for each classification method over score thresholds. For TMPM, the threshold represents the probability of death, while the threshold for the kNN methods represents the voting proportion. Fig. 5 shows a linear increase in Youden's Index for TMPM until peaking at a low threshold (0.20) for probability of death. For the kNN methods, the graphs appear symmetric with peaks at 0.55 for the ensemble, 0.50 for OTCS-MES ES, 0.60 for OTCS-EP and 0.50 for OTCS-MES.

For optimal results on operating points, OTCS-MES ES and the ensemble outperform TMPM when using equal weights for sensitivity and specificity. As shown in Table $^ { 8 , }$ the Youden values for OTCS-MES ES (0.5430) and the ensemble (0.5541) are slightly better than TMPM (0.5296). The optimal threshold for TMPM (0.20) is much lower than the thresholds for the kNN methods (0.50 and 0.55). Since the sensitivity values for TMPM (0.700), OTCS-MES ES (0.7182), and the ensemble (0.7091) are rather low, more emphasis on sensitivity should be given to choose an operating point.

The OTCS methods show an increasing advantage over TMPM as the weight on sensitivity increases. Fig. 6 shows weighted Youden Index values as the sensitivity weight increases from equal sensitivity/specificity (1/1) to high preference for sensitivity (10/1). The ensemble dominates TMPM at all weight levels. The individual OTCS approaches (OTCS, OTCS-MES EP, and OTCS-MES ES) dominate TMPM at sensitivity weights above 3/1. The performance of TMPM remains relatively flat over the range of sensitivity weights, while the four OTCS approaches increase in a linear manner with an increasing performance improvement over TMPM.

![](/api/attachments/QJ3WKUN6/fulltext/images/981b65b21870cd7330852a0a6dc9f6d4a5c0424fbc2697f008bc692cca1f5151.jpg)  
Fig. 2. Comparison of Methods for Imbalanced Data Sets on AUC.

![](/api/attachments/QJ3WKUN6/fulltext/images/4e89d577f435430a10046b72105bd421b8334756409bf63c1692ec9d58911bcb.jpg)  
Fig. 3. Impact of Case Base Size on AUC.

Table 7  
Statistical Testing Results for Hypotheses.

<table><tr><td>Test</td><td>Classification method 1</td><td>Classification method 2</td><td>p-value</td></tr><tr><td>1a</td><td>TMPM(AUC 0.8392 CI:0.8326–0.8458)</td><td>OTCS(AUC 0.7894 CI:0.7840–0.7948)</td><td>&lt; 0.0001*</td></tr><tr><td>1b</td><td></td><td>OTCS-MES EP(AUC 0.8065 CI:0.8008–0.8122)</td><td>&lt; 0.0001*</td></tr><tr><td>1c</td><td></td><td>OTCS-MES ES(AUC 0.8194 CI:0.8120–0.8268)</td><td>0.0056*</td></tr><tr><td>1d</td><td></td><td>OTCS-MES Ensemble(AUC 0.8589 CI:0.8521–0.8657)</td><td>0.0037*</td></tr><tr><td>2a</td><td>OTCS-MES EP(AUC 0.8065 CI:0.8008–0.8122)</td><td>OTCS(AUC 0.7894 CI:0.7840–0.7948)</td><td>0.0024*</td></tr><tr><td>2b</td><td>OTCS-MES ES(AUC 0.8194 CI:0.8120–0.8268)</td><td>OTCS(AUC 0.7894 CI:0.7840–0.7948)</td><td>&lt; 0.0001*</td></tr><tr><td>3</td><td>OTCS-MES ES(AUC 0.8194 CI:0.8120–0.8268)</td><td>OTCS-MES EP(AUC 0.8065 CI:0.8008–0.8122)</td><td>0.0524**</td></tr><tr><td>4a</td><td>OTCS-MES Ensemble(AUC 0.8589 CI:0.8521–0.8657)</td><td>OTCS(AUC 0.7894 CI:0.7840–0.7948)</td><td>&lt; 0.0001*</td></tr><tr><td>4b</td><td></td><td>OTCS-MES EP(AUC 0.8065 CI:0.8008–0.8122)</td><td>&lt; 0.0001*</td></tr><tr><td>4c</td><td></td><td>OTCS-MES ES(AUC 0.8194 CI:0.8120–0.8268)</td><td>&lt; 0.0001*</td></tr></table>

\*Significant at traditional alpha of 0.05. The family-wise error rate (probability of making at least one Type I error) for simultaneous testing of 10 comparisons is 0.22. \*\*Significant at alpha level of 0.10.

![](/api/attachments/QJ3WKUN6/fulltext/images/331c273f9c22949ee50ef8526749219d879f2e9385b4e4bf4824125c438aa94a.jpg)  
Fig. 4. ROC Curves for Mortality Prediction.

The ensemble approach also shows advantages over TMPM using the Neyman-Pearson criteria. As shown in Fig. 7, the ensemble provides higher sensitivity at false positive constraints below 0.6. At false positive constraints above $0 . 6 ,$ TMPM and the ensemble show similar sen sitivity values with some crossing between the TMPM and ensemble graphs. For the individual OTCS methods, TMPM shows an advantage for false positive constraints above 0.5. For small false positive constraint levels, the individual OTCS methods show higher sensitivity values.

## 4.3. Discussion

Overall, the analysis provides evidence (Table 9) to support all hypotheses except 1d between TMPM and the OTCS ensemble. Results demonstrate strong evidence to reject null hypotheses (equal AUC performance) except for less evidence to support Hypothesis 3 involving OTCS-MES ES and OTCS-MES EP. Similarity measures using partial matching and matching weights provide better performance than simple matching. Event severity based on domain knowledge of injuries provides improved predictive performance than prevalence without domain knowledge of injuries. The OTCS ensemble provides improved predictive performance demonstrating enough diversity in the base classifiers (OTCS, OTCS-MES EP, and OTCS-MES ES). TMPM, developed with a large set of data and specialized domain knowledge, provides improved predictive performance than nearest neighbor classifiers using similarity measures.

Table 8  
Confusion Matrix Summary for Equal Weights.

<table><tr><td>Method</td><td>Sensitivity</td><td>Specificity</td><td>Accuracy</td><td>Youden</td><td>Threshold</td></tr><tr><td>TMPM</td><td>0.7000</td><td>0.8296</td><td>0.8225</td><td>0.5296</td><td>0.20</td></tr><tr><td>OTCS</td><td>0.6818</td><td>0.7164</td><td>0.7145</td><td>0.3982</td><td>0.55</td></tr><tr><td>OTCS-MES ES</td><td>0.7182</td><td>0.8249</td><td>0.8190</td><td>0.5430</td><td>0.50</td></tr><tr><td>OTCS-MES EP</td><td>0.8182</td><td>0.6238</td><td>0.6345</td><td>0.4420</td><td>0.45</td></tr><tr><td>Ensemble</td><td>0.7091</td><td>0.8450</td><td>0.8375</td><td>0.5541</td><td>0.55</td></tr></table>

![](/api/attachments/QJ3WKUN6/fulltext/images/3c0f461808aff1581ab85d02291469cecb6d4ba07c54fde110b8ab286c8bba46.jpg)  
Fig. 5. Confusion Matrix Performance of Classification Methods.

![](/api/attachments/QJ3WKUN6/fulltext/images/955bdac4148380545b084975a0d505adaa9ce277993993c3d9caebf3b03147dd.jpg)  
Fig. 6. Weighted Youden's Index by Method and Cost Ratio.

The AUC values for Hypothesis 1d (TMPM versus OTCS ensemble) conflict with expected results. The performance diference is large enough to have confidence that the ensemble provides improved perfor mance to the established TMPM.

The ensemble of nearest neighbor classifiers provides advantages in simplicity and explanation capability over TMPM. The ensemble needs no training as compared to extensive training with a large data set by TMPM. TMPM may also require periodic retraining to deal with concept drift. However, the ensemble requires more classification efort, com bining nearest neighbor search of three component classifiers. Indexing may be necessary to mitigate the additional resource usage for three nearest neighbor searches. Nearest neighbor classifiers provide superior explanations with details of prominent cases rather regression coeficients in the complex TMPM model. However, the ensemble compli cates explanations with a need to combine prominent cases from component classifiers.

Table 9  
Summary of Findings on Hypotheses

<table><tr><td>Hypothesis</td><td>Result</td><td>Comments</td></tr><tr><td>1a</td><td>TMPM &gt; OTCS</td><td>Strong evidence to confirm</td></tr><tr><td>1b</td><td>TMPM &gt; OTCS-MES EP</td><td>Strong evidence to confirm</td></tr><tr><td>1c</td><td>TMPM &gt; OTCS-MES EP</td><td>Strong evidence to confirm</td></tr><tr><td>1d</td><td>OTCS Ensemble &gt; TMPM</td><td>Strong evidence of opposite effect</td></tr><tr><td>2a</td><td>OTCS-MES EP &gt; OTCS</td><td>Strong evidence to confirm</td></tr><tr><td>2b</td><td>OTCS-MES ES &gt; OTCS</td><td>Strong evidence to confirm</td></tr><tr><td>3</td><td>OTCS-MES ES &gt; OTCS-MES EP</td><td>Some evidence to confirm</td></tr><tr><td>4a</td><td>OTCS Ensemble &gt; OTCS</td><td>Strong evidence to confirm</td></tr><tr><td>4b</td><td>OTCS Ensemble &gt; OTCS-MES EP</td><td>Strong evidence to confirm</td></tr><tr><td>4c</td><td>OTCS Ensemble &gt; OTCS-MES ES</td><td>Strong evidence to confirm</td></tr></table>

![](/api/attachments/QJ3WKUN6/fulltext/images/6ca52cc0bd46dce2e960c1c23b28c6dd58756b9c81fb65e700d85e7197865110.jpg)  
Fig. 7. Maximum Sensitivity for False Positive Constraints (Neyman-Pearson criteria).

Table 10  
Match Level in Trauma Data.

<table><tr><td rowspan="2">Target ICD-9-CM length</td><td rowspan="2">Match level</td><td colspan="2">Test incidents (2 K)</td></tr><tr><td># of matches</td><td>% of total matches</td></tr><tr><td>3</td><td>3</td><td>264,774</td><td>3.70%</td></tr><tr><td>4</td><td>3</td><td>2,236,076</td><td>31.25%</td></tr><tr><td>4</td><td>4</td><td>1,347,003</td><td>18.82%</td></tr><tr><td>5</td><td>3</td><td>1,750,320</td><td>24.46%</td></tr><tr><td>5</td><td>4</td><td>1,086,807</td><td>15.19%</td></tr><tr><td>5</td><td>5</td><td>470,492</td><td>6.58%</td></tr><tr><td>Exact matches</td><td></td><td>2,082,269</td><td>29.10%</td></tr><tr><td>Partial matches</td><td></td><td>5,073,203</td><td>70.90%</td></tr><tr><td>Total matches</td><td></td><td>7,155,472</td><td>100.00%</td></tr></table>

Simplification of the ensemble has little negative impact. An ensemble using OTCS-ES and OTCS-EP generates an AUC of 0.8546, just slightly less than the AUC using three component classifiers (0.8568). OTCS with exact matching adds little diversity to the partial, weighted event matching in OTCS-MES EP and OTCS-MES ES.

An ensemble with four component classifiers (OTCS, OTCS-MES EP, OTCS-MES ES, and TMPM) provides a slight performance improvement. The four-component ensemble generates an AUC of 0.8649 compared to 0.8568 with three components. However, explanation of classification decisions would be dificult, combining important cases and regression coeficients for prominent medical events.

The AUC values for TMPM (0.839) are below the reported value (0.88) in Glance et al. [1]. A possible explanation for TMPM's smaller AUC value is concept drift in more recent trauma data (2015) used in this study than used in the original study (2002 to 2006).

The ensemble method also provides better performance than TMPM using an operating point on a ROC curve. With equal weight on sensitivity and specificity, the ensemble provides a more credible score threshold (0.55) than TMPM (0.20) as well as a slightly larger, optimal Youden value (0.5541 versus 0.5296). However, sensitivity values at the optimal Youden value seems too low so higher weighting for sensitivity seems likely in practice. The nearest neighbor methods (in dividual and ensemble) provide linear improvements in the weighted Youden value as the cost ratio increases. The ensemble approach also shows advantages over TMPM using the Neyman-Pearson criteria at false positive constraints below 0.5. If a false positive constraint of 0.4 is feasible in practice, the ensemble should provide suficient sensitivity (0.9545).

An important assertion in this study is the significance of partial, weighted matching with OTCS-MES versus the original OTCS. Concerning the OTCS-MES benefits for partial matching, Table 10 in dicates that over 70% of the matched events between MESs are partial. Essentially, the original OTCS misses all partial matches with 3 and 4- digit partial matches containing valuable similarity information.

## 5. Conclusion

We extended a similarity measure for medical event sequences (MESs) and evaluated its classification performance for mortality prediction using a data set of trauma incidents. To generalize the Optimal Temporal Common Subsequence for MESs (OTCS-MES) developed in a previous study [12], we separated event matching into degree of matching (exact or partial using hierarchical structure of event codes) and weights to indicate importance or relevance of events. The OTCS-MES EP uses partial matching and event prevalence (EP) weights, while the OTCS-MES ES uses partial matching and event severity (ES)

weights. We compared these methods to the original OTCS [11] measure with only exact event code matching and no weights.

We compared the performance of nearest neighbor classification using MES similarity measures to the Trauma Mortality Prediction Model (TMPM), an accepted regression model for mortality prediction for trauma patients. The comparisons used a substantial data set from the National Trauma Data Bank. The secondary part of the comparison determined reasonable values for neighborhood size (k), weighted voting, method to handle imbalanced mortality class, and case base size with a preference for large neighbor sizes, weighted voting, oversampling, and large case base. The primary part of the experiment compared nearest neighbor classification to TMPM using Receiver Operating Characteristic (ROC) Curves, Area under a ROC curve (AUC), and confusion matrices derived from operating points on the Receiver Operating Characteristic (ROC) curves. The results demonstrated an advantage on ROC curves, AUC, and operating points for the ensemble of nearest neighbor classifiers.

Importantly, this research provides a better method to retrospectively evaluate trauma care for specific trauma centers or care facilities. The method in this paper supports improved strategic decisions concerning trauma care processes based on a better measure of care performance. Governance bodies for trauma care face multiple procedural and resource allocation decisions. The decisions involving trauma system components are many and varied, including stafing, EMS transport systems, triage and transport protocols, EMS/trauma center communication systems, facility design and inclusive coverage. We feel our OTCS-MES based method can improve strategic decisions in these areas based on superior care facility templates derived from high per forming trauma centers.

We plan future work on classification performance of linked patient records and a query architecture for medical event sequences. Linked patient records combine patient characteristics and medical event sequences. We plan to extend mortality prediction combining medical events with key characteristics of trauma patients. We also plan to predict high-risk patients using patient characteristics and MESs containing both medical events and temporal structure. To support clinical decision-making using MESs, we will develop a query architecture supporting both similarity measures for linked MESs and regular expression matching to capture important patterns in MESs. To evaluate the query architecture, we will cooperate with medical professionals and analysts to determine use cases and evaluate utility of query results. We will also develop storage and optimization techniques for large databases of linked MESs.

## Acknowledgements

The Department of Education GAANN Program (grant P200A150283), focused on Big Data Science and Engineering, provided partial support for this research through a fellowship.

## References

[1] L.G. Glance, T.M. Osler, D.B. Mukamel, W. Meredith, J. Wagner, A.W. Dick, TMPM-ICD9: a trauma mortality prediction model based on ICD-9-CM codes. Annals of Surgery 249 (6) (2009) 1032–1039.

[2] L.D. Cassidy, A. Cook, A. Ertl, D. Gourlay, T. Osler, Is the trauma mortality prediction model (TMPM-ICD-9-CM) a valid predictor of mortality in pediatric trauma patients? Journal of Pediatric Surgery 49 (1) (2014) 189–192.

[3] L. Moore, H. Champion, P.A. Tardif, B.L. Kuimi, G. O'Reilly, A. Leppaniemi, ... C. Gaarder, Impact of trauma system structure on injury outcomes: a systemati review and meta-analysis, World Journal of Surgery 42 (5) (2018) 1327–1339.

[4] B. Celso, J. Tepas, B. Langland-Orban, E. Pracht, L. Papa, L. Lottenberg, L. Flint, A systematic review and meta-analysis comparing outcome of severely injured pa tients treated in trauma centers following the establishment of trauma systems, Journal of Trauma and Acute Care Surgery 60 (2) (2006) 371–378.

[5] S. Weeks. K. Stevens, A. Haider. D. Efron. E. Haut. E. MacKenzie, E. Schneider, A modified Kampala trauma score (KTS) effectively predicts mortality in trauma patients, Iniury 47 (1) (2016).125–129

[6] LG. Glance. T.M. Osler. D.B. Mukamel. A.W. Dick. Impact of trauma center designation on outcomes: is there a difference between level I and level I trauma

centers? Journal of the American College of Surgeons 215 (3) (2012) 372–378.

[7] A. Hashmi, I. Ibrahim-Zada, P. Rhee, H. Aziz, M.J. Fain, R.S. Friese, B. Joseph, Predictors of mortality in geriatric trauma patients: a systematic review and meta analysis, Journal of Trauma and Acute Care Surgery 76 (3) (2014) 894–901.

[8] H. Tohira, I. Jacobs, D. Mountain, N. Gibson, A. Yeo, Systematic review of predictive performance of injury severity scoring tools, Scandinavian Journal of Trauma, Resuscitation and Emergency Medicine 20 (1) (2012) 63.

[9] P. Kilgo, T. Osler, W. Meredith, The worst injury predicts mortality outcome the best: rethinking the role of multiple injuries in trauma outcome scoring, Journal of Trauma and Acute Care Surgery 55 (4) (2003) 599–607.

[10] R.S. Burd, M. Ouyang, D. Madigan, Bayesian logistic injury severity score: a method for predicting mortality using international classification of disease-9 codes, Academic Emergency Medicine 15 (5) (2008) 466–475.

[11] A. Zheng, X. Zhou, J. Ma, M. Petridis, The optimal temporal common subsequence, Proceedings of the 2nd International Conference on Software Engineering and Data Mining (SEDM). JEEE. Chengdu. China. June. 2010. pp. 316–321

[12] M. Mannino, J. Fredrickson, F. Banaei-Kashani, I. Linck, R.A. Raghda, Development and evaluation of a similarity measure for medical event sequences, ACM Transactions on Management Information Systems (TMIS) 8 (2–3) (2017) 8.

[13] V. Barell, L. Aharonson-Daniel, A. Fingerhut, E. Mackenzie, A. Ziv, V. Boyko, A. Abargel, M. Avitzour, R. Heruti, An introduction to the Barell body region by nature of injury diagnosis matrix, Injury Prevention 8 (2) (June, 2002) 91–96.

[14] D. Clark, S. Ahmad, Estimating injury severity using the Barell matrix, Injury Prevention 12 (2) (2006) 111–116.

[15] N. Bhatia, V. Ashey, Survey of nearest neighbor techniques. International Journal of Computer Science and Information Security 8 (2) (2009) 14–22

[16] C. Manning, P. Raghavan, H. Schutze, Introduction to Information Retrieval, Cambridge University Press, 2008, informationretrieval.org.

[17] S.A. Dudani, The distance-weighted k-nearest-neighbor rule, IEEE Transactions on Systems, Man, and Cybernetics (4) (1976) 325–327.

[18] N. Garcia-Pedrajas, D. Ortiz-Boyer, Boosting k-nearest neighbor classifier by mean of input space projection, Expert Systems with Applications 36 (2009) 10570–10582.

[19] M. Maloof, Learning when data sets are imbalanced and when costs are unequal and unknown, Proceedings of ICML-2003 Workshop on Learning from Imbalanced Data Sets II, vol. 2, 2003, pp. 1–2.

[20] G. Kalton, Methods for oversampling rare subpopulations in social surveys, Survey Methodology 35 (2) (2009) 125–141.

[21] S. Zhang, KNN-CF approach: incorporating certainty factor to kNN classification, JEEE Intelligent Informatics Bulletin 11. (1) (2010) 24–33

[22] H. Hedegaard, R. Johnson, M. Warner, L. Chen, J. Annest, “Proposed framework for presenting injury data using the international classification of diseases,” tenth revision, clinical modification (ICD-10-CM) diagnosis codes, National Health Statistics Reports (89) (2016) 1–20.

[23] G. Qin, L. Hotilovac, Comparison of non-parametric confidence intervals for the area under the roc curve of a continuous-scale diagnostic test. Statistical Methods ir Medical Research 17 (2008) 207–221.

[24] M. Kottas, O. Kuss, A. Zapf, A modified Wald interval for the area under the ROC curve (AUC) in diagnostic case-control studies, BMC Medical Research Methodology 14 (1) (2014) 26.

[25] W. Youden. Index for rating diagnostic tests, Cancer 3 (1950) 32–35.

[26] D. Li. F. Shen, Y. Yin, J. Peng, P. Chen, Weighted Youden index and its two-independent-sample comparison based on weighted sensitivity and specificity. Chinese Medical Journal 126 (6) (2013) 1150–1154.

[27] C. Newgard, R. Lowe, Cost savings in trauma systems: the devil's in the details, Annals of Emergency Medicine 67 (1) (2016) 68–70.

[28] J. Neyman, E. Pearson, On the problem of the most eficient tests of statistica hypotheses, Philosophical Transactions of the Royal Society 231 (694–706) (1933) 289–337.

[29] cms.gov, CMS 2008–2010 Data Entrepreneurs' Synthetic Public Use File (DE-SynPUF). http://www.cms.goy/Research-Statistics-Data-and-Systems/ Downloadable-Public-Use-Files/SynPUFs/DE\_Syn\_PUF.html, (2018).

Joel Fredrickson Joel Fredrickson is a fourth-year Ph.D. student in the computer science and information system program at University of Colorado Denver. He has extensive experience in health information systems, currently employed as the Director of Analytics and Outcomes at AxisPoint Health, formerly known as McKesson Health Solutions. He has research interests in health care analytics and clinical decision support systems.

He received a master’s degree in computer science from University of Denver and a bachelor’s degree in computer science from King Khalid University, Saudi Arabia. He is interested in time-series spatial data and event sequence data.

Michael Mannino is an associate professor in the Business School of the University of Colorado Denver. Previously he was on the faculty at the University of Florida, University of Texas at Austin, and University of Washington. He has been active in research about database management, knowledge representation, and organizational impacts of technology. He has published articles in major journals of the IEEE (Transactions on Knowledge and Data Engineering and Transactions on Software Engineering), ACM (Transactions on Management Information Systems, Communications and Computing Surveys), INFORMS (Informs Journal on Computing and Information Systems Research), and Elsevier (Decision Support Systems). His research includes several popular survey and tutorial articles as well as many papers describing original research. He is the author of the textbook, Database Design, Application Development, and Administration in its seventh edition.

Omar Alqahtani Omar Alqahtani is a fourth-year Ph.D. student in the computer science and information system program at University of Colorado Denver. He received a master’s degree in computer science from University of Denver and a bachelor’s degree in computer science from King Khalid University, Saudi Arabia. He is interested in time-series spatial data and event sequence data.

Farnoush Banaei-Kashani Farnoush Banaei-Kashani is currently an assistant professor at the Department of Computer Science and Engineering, University of Colorado Denver where he directs a US DoEd GAANN PhD Fellowship Program in "Big Data Science and Engineering" and an MS Program in "Data Science in Biomedicine". Previously, he was a research scientist at the Computer Science Department, University of Southern California (USC). Dr. Banaei-Kashani is passionate about performing fundamental research toward building practical, large-scale data-intensive systems, with particular interest in Datadriven Decision-making Systems (DDSs), i.e., systems that automate the process of decision-making based on (big) data. Toward this end, he has organized his research and education activities around two tracks: a Data Science track and a Data Management and Mining track. With the Data Science track. his team engage with real-world problems that can benefit from data-driven solutions (consisting of all data scientific life-cycle components). given various combinations of the Big Data challenges. In particular. his lab has experienced with a number of data-driven decision-making systems (DDSs) from various application areas, such as health informatics, computational genetics, IoT, intelligent transportation, and scientific computing. The Data Science track complements the Data Management and Mining track by providing practical real-world problems, which Dr. Banaei-Kashani's team generalize, formalize, and rigorously study as novel data management and mining as well as machine learning problems. In particular, his team has special interest in the following areas (among others): spatiotemporal data management and mining, graph data management and mining, high-throughput data management and mining using modern hardware, and next generation database engines (or NewSQL). Dr. Banaei-Kashani has published more than 60 referred papers and has received several awards, including an ACM Sensys 2016 Best Paper Award and an IEEE CloudCom 2010 Best Paper Award. He frequently serves as a program committee member of highly ranked database conferences (including ICDE. VLDB and SIGSPATIAL). and has also chaired many workshops and conferences over last few vears, including SIGSPATIAL. 2018 Conference. Dr. Banaei-Kashani's research has been supported by grants from both governmental agencies (DoEd, NSF, NIH, DOT, DOJ and NASA) and industry (Google, IBM, Chevron and Intel).
