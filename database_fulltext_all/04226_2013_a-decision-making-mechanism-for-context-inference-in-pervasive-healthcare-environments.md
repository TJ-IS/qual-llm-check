---
otero_id: 4226
otero_key: "8HQADY89"
title: "A decision-making mechanism for context inference in pervasive healthcare environments"
authors: "Alessandro Copetti; J.C.B. Leite; O. Loques; Mario Fritsch Neves"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.10.010"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A decision-making mechanism for context inference in pervasive healthcare environments

Alessandro Copetti <sup>a,</sup>⁎, J.C.B. Leite <sup>b</sup>, O. Loques <sup>b</sup>, Mario Fritsch Neves <sup>c</sup>

<sup>a</sup> Departamento de Computação, Universidade Federal Fluminense, Rio das Ostras-RJ, Brazil

<sup>b</sup> Instituto de Computação, Universidade Federal Fluminense, Niterói-RJ, Brazil

<sup>c</sup> Departamento de Clínica Médica, Universidade do Estado do Rio de Janeiro, Rio de Janeiro-RJ, Brazil

## a r t i c l e i n f o

Available online 8 October 2012

Keywords: Context inference Fuzzy logic Pervasive healthcare

## a b s t r a c t

This paper presents a Fuzzy approach to health-monitoring of patients in pervasive computing environments A decision model considers three classes of variables that represent the context information being collected: environmental, physiological, and behavioral. A case study of blood pressure monitoring was developed to identify critical situations based on medical knowledge. The solution maintains the interpretability of the decision rules, even after a learning phase which may propose adjustments in these rules. In this phase, the Fuzzy c-Means clustering was chosen to adjust membership functions, using the cluster centers. A medical team evaluated data from 24-h monitoring of 30 patients and the rating was compared with the results of the system. The proposed approach proved to be individualized, identifying critical events in patients with different levels of blood pressure with an accuracy of 90% and low number of false negatives.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Due primarily to advances in wireless sensor technologies positioned not only in environments but also on people's bodies (wearable computing), it is now possible to design remote health-monitoring applications. These applications can execute in pervasive environments equipped with devices capable of performing computation and communication. Taking this into account, it is now possible to envision a domestic environment with processing units that can perform tasks ranging from data collection to emergency identi<sup>fi</sup>cation and noti<sup>fi</sup>cation.

For the sake of clarity, we will use two situations to demonstrate the use of pervasive computing in the domestic environment and the associated challenges related to achieving reliable context inference. For example, an elderly person is monitored in the home environment in a nonintrusive manner with vital sign sensors attached to his body that measure blood pressure and heart rate, among other functions. At a particular moment, a signi<sup>fi</sup>cant alteration in this patient's vital signs occurs. However, in the previous minutes, both a high ambient temperature and an increase in physical activity were detected. Therefore, for that patient, the situation can be interpreted as either critical or normal. The right interpretation requires a careful consideration of each individual's signs of health (possibly including historical data previously collected) in order to avoid unnecessary emergency noti<sup>fi</sup>cations. In another situation, considerable variation in the patient's vital signs is followed by a sensor report of the patient having fallen to the ground; the latter situation is clearly identi<sup>fi</sup>ed as critical. In both situations – characterized as normal or critical – noti<sup>fi</sup>cation should be directed to a health care provider who, in turn, may try to achieve a better understanding of the situation, e.g., by contacting the patient.

In both of these examples, we can identify three classes of variables related to context information: environmental, physiological, and behavioral. Clearly, if data fusion is performed after collecting the variables, we can better characterize the patient's state. As an immediate mapping, the patient's state can be characterized as normal, alert, or emergency. Hence, there is a need to devise decision-making models that can make inferences and characterize monitoring situations in order to avoid false alarms.<sup>1</sup>

In classes of healthcare application that do not involve home moni toring of vital signs, medical knowledge is embedded in a model using fuzzy logic. In general, it is desirable for the model to allow health specialists an understanding of its rules (interpretability). In this context, one interesting approach is to use a hybrid technique for model generation, i.e., neither entirely based on medical knowledge nor entirely based on an annotated dataset but making use of both. Some studies (e.g., [2,26]) have explored this approach, which can involve the following steps: (i) creating initial medical rules, (ii) fuzzi<sup>fi</sup>cation of these fuzzy rules to create the model, and (iii) updating the parameters of the fuzzy model based on the analysis of an annotated dataset.

However, it remains a challenge to build these models to monitor multivariate healthcare data while maintaining the interpretability of the rules because the data can evolve over the lifetime of the system.

In the studies reviewed for this research, we did not <sup>fi</sup>nd an approach to pervasive monitoring that is able to perform the fusion of environmental, physiological, and behavioral data necessary for continuous, real-time identi<sup>fi</sup>cation of critical situations in elder care. This paper proposes a decision-making mechanism of context inference for health monitoring applications. The proposed mechanism brings together medical knowledge, interpretability of the rules, individualization, and adaptability of variations in vital signs based on patients' activities.

The present text is organized as follows: Section 2 reviews relevant research in the area of pervasive home care. Section 3 presents the decision-making model from which both the Inference Module and the Learning Module derive — these are introduced in Sections 4 and 5, respectively. Section 6 discusses the validation of the monitoring proposal. Finally, Section 7 presents the conclusions.

## 2. Related works

The design of a fuzzy inference system can originate from a specialist's knowledge or from the data. According to [13], a system based on specialist knowledge may suffer a loss of accuracy. In [4], it is suggested that the user should choose a level of tradeoff between accuracy and transparency that involves the selection of appropriate parameters for the inference system. We believe that the alternatives must be evaluated to obtain a system that presents interpretability and simultaneously allows the adjustment of the inference system's knowledge base, respecting the characteristics of the health-monitoring problem.

The evolution/adjustment of the fuzzy inference system can be classi<sup>fi</sup>ed into two broad approaches: the adaptation of membership functions and the adaptation of fuzzy rules. Each of these approaches uses training data to perform the adaptation. Two different forms for use in performing such adaptations are presented in [17].

The adaptation of membership functions can perform the following operations on fuzzy sets: shifting, altering or adding. Shifting takes the whole set to a new position in axis X. Altering alters only the core of the fuzzy set. Finally, addition creates a new set. However, in the fuzzy rule adaptation approach, the operations act on the rules in order to modify (substitute the rule variable, change the term of a rule, or change the rule operator), add or enable/disable. Modi<sup>fi</sup>cation maintains the rule, but it can alter its meaning completely. The addition of a new rule generates a rule for the inference system. Enable/ disable can be accomplished by altering the rule's weight.

In the fuzzy rule adaptation approach, there are two main techniques: neuro-fuzzy and genetic Fuzzy [16]. Neuro-fuzzy systems combine the learning capacity of neural networks with the representation of fuzzy logic knowledge. Recent works have explored this technique, including in context-aware environments [2]. The Genetic Fuzzy systems also use genetic algorithms to automatize knowledge acquisition. By means of the crossover and mutation operations, the algorithms generate new parameters and/or new rules for the fuzzy system [16].

Even though the Neuro-fuzzy and Genetic Fuzzy techniques obtain good results in the various areas in which they are applied, they will produce signi<sup>fi</sup>cant changes in the initial rule set of a health monitoring system. In the context of this study, such changes must be minimized to preserve the interpretability of the rules. With the same objective, we seek solutions that do not generate new rules and use few variables in the rule antecedents.

According to [12], when the number of variables increases, the number of rules increases drastically; as a consequence, the number of instances necessary to learn the rule set also increases. One related issue is that the modi<sup>fi</sup>cation of one variable of a given fuzzy set has an impact on all the rules that use that variable. According to [8], it would be better to create larger cores of fuzzy sets.

It is worth noting that a newly generated rule can con<sup>fl</sup>ict with other existing rules, in addition to affecting the interpretability of the rules. If we allow every physician who makes use of the system to generate new rules, we leave doors open for errors in the system. Therefore, we conclude that the preservation of the rules after the learning process maintains the medical knowledge embedded in the fuzzy inference system.

Current systems for home care treatment demand that the patient informs the system of a state of emergency by activating an alarm, for example, via a panic button. Conversely, the system can react when prede<sup>fi</sup>ned limits of vital signs are exceeded, as, for example, in [18]. These variations can be in<sup>fl</sup>uenced by behavioral or environmental conditions. For example, when a person is sleeping or performing a domestic activity, blood pressure is naturally altered [7,24], which can also be a consequence of the ambient temperature [19].

However, few advances have been made with regard to the fusion of different classes of variables [6]. A study exploring the relationship among physiological and psychological variables in home care monitoring is presented in [21]. Certain behavioral variables are also considered, and correlations between variables are made; for example, high stress levels are related to short sleeping time. In [9], a behavioral pro<sup>fi</sup>le of a patient being monitored at home is developed to investigate the relationship between behavioral and physiological variables, especially heart rate. The same decision-making mechanism approach is used in the theoretical construct presented in [25]. This work does not include the concept of behavior, despite citing the possibility of collecting data on agitation and gait. Because it does not address data fusion, it does not consider the association of vital signs with the variable classes of environment and behavior. Furthermore, it does not make it feasible to give weight to rules.

A paper by [26] describes a methodological framework for the automated generation of fuzzy expert systems, which are based on an initial crisp model for cardiovascular domain problems. The fuzzy models produced are tuned using global optimization, i.e., optimizing their parameters to <sup>fi</sup>t an arrhythmia database. While that study considers data taken from publicly available databases, our work uses historical data and patient data generated synthetically from this history.

## 3. The decision-making model for monitoring

This section presents and discusses a decision-making model to identify critical situations, characterized mainly by alterations in vital signs. Its fundamental requirement was the incorporation of medical knowledge. A simple form of representing such knowledge, and one that is well understood by physicians, is the concept of if–then rules. Therefore, we have elaborated rules based on knowledge published in medical guidelines and on the experience of the health specialists in our research group. Continuous monitoring of blood pressure was adopted as the case study. Two examples of the if–then rules used are the following: a) if the patient is sleeping, systolic pressure can naturally decrease 10 mm Hg below the average, whereas diastolic pressure can decrease 7.6 mm Hg; b) if the patient is performing domestic tasks/ activities, systolic pressure could increase to a maximum of 10.7 mm Hg above the average, whereas the diastolic pressure could increase to 6.7 mm Hg.

Two protocols for blood pressure control have been de<sup>fi</sup>ned by the Brazilian Society of Cardiology, both assuming that the monitored person is located outside the physician's of<sup>fi</sup>ce: Home Blood Pressure Monitoring (HBPM) and Ambulatory Blood Pressure Monitoring (ABPM). Despite being used mainly for diagnostic clari<sup>fi</sup>cation [19], these tools can establish a knowledge base for the de<sup>fi</sup>nition of long-term monitoring. The HBPM requires that the patient be measured three times in the morning and three times in the evening for 5 days. The ABPM, on the other hand, should be carried out over a period of 24 h, reaching approximately 80 measurements, at 20 min intervals when awake and 30 min intervals during sleep [24]. In both methods, patients are advised to take notes of their activities, including what they were doing before each measurement. In this study, we have considered the medical guidelines used in the HBPM and ABPM protocols. Nevertheless, our proposal differs from those guidelines in two characteristics. First, we consider long-term control of blood pressure. Second, our proposal leverages these two forms of monitoring to construct a monitoring environment with the use of home and body sensors.

Using the contextual information as a starting point, we aim to infer what we call “the patient state”, which allows us to distinguish between situations characterized as normal, alert, and emergency. A normal state means that the data input has produced a certain value that is expected or reasonable for that patient. The states of alert and emergency, in turn, are categorized as different levels of critical situations. An alert identi<sup>fi</sup>es variations and facilitates medical analysis. A state of emergency determines that the system requests that a new measurement be produced soon thereafter to con<sup>fi</sup>rm the <sup>fi</sup>rst. A warning can then be sent to a physician or emergency service to deal with the problem.

To be suitable for long-term monitoring, the model must respond adequately to patients with different levels of physiological signals, understanding that their average levels may change over time. At the same time, vital sign values that are considered normal in medical guidelines should result in a normal output by the model; this behavior requires the de<sup>fi</sup>nition of generic rules, which are valid for all patients and do not consider individual patients' averages. Furthermore, the state should not be altered abruptly due to small variations in vital signs. The state of emergency, on the other hand, has priority. If an emergency is detected at the same time that another rule results in normal, the latter should not prevail over the former.

In terms of the individualization of each patient, it is necessary to devise a learning process that can update the decision module to deal with cases we refer to as mild alerts. Mild alerts are weak alerts generated by the system, which can be considered normal under certain conditions. A practical example of an adjustment is for patients who normally have a nocturnal drop in blood pressure. In such cases, the system should be adjusted so that it does not generate unnecessary alarms. Likewise, moderate elevations of blood pressure are not considered alarming in medical evaluation.

## 3.1. The decision-making module

We have developed a decision-making system that implements a decision-making model, presented in Fig. 1. In this <sup>fi</sup>gure, the numbers (1), (2), and (3) indicate the steps followed to build the decision model. The arrows indicate the chaining of these steps. The different classes of variables are treated initially by preprocessing that uses information from the patient's pro<sup>fi</sup>le, e.g., an average of the patient's vital signs to calculate deviations from these averages. Next, the inference component completes the context inference in order to determine the patient's state.

After a large number of measurements, the learning component can operate and updates to the variables related to vital signs may be presented to the physician. The specialist's intervention is facilitated by the limits de<sup>fi</sup>nition used in the mild alert concept, which restricts the measurements to be considered by the learning process as a way for the specialist to express tolerance to mild alerts. The goal is to adjust the variables in order to reduce the number of alerts, individualizing treatment but sending alerts in case of important events.

## 4. Inference module

The dynamics of human behavior and the inherent variability of vital signs – along with the uncertainties associated with the data collected by the sensors – must be considered when de<sup>fi</sup>ning the variables of interest. Additionally, medical knowledge is expressed in such a way that makes the application of rigid concepts inappropriate for this type of problem. In consideration of these characteristics, we have adopted a model based on fuzzy logic in order to represent relevant variables and implement the module's decision-making function.

![](/api/attachments/8HQADY89/fulltext/images/65c18a492b750b1aa5ac1716b8477682d8580f69509bc21c8927f3195e37fae1.jpg)  
Fig. 1. Decision-making module <sup>fl</sup>ow.

The variables presented in the ABPM are restricted to blood pressure (BP), heart rate (HR) and activities that are performed by the patient. Thus, the physiological variables we select for our proposal are systolic blood pressure (SBP), diastolic blood pressure (DBP) and heart rate (HR). Both of these variables can be easily collected and rapidly respond according to the patient's state. Among the environmental factors (e.g., light, temperature, noise, and humidity) we have chosen temperature because it has a great in<sup>fl</sup>uence on the patient's health and is easy to measure.

For the patient activity variables, we have considered sleeping, resting, eating, walking and performing domestic activities. As we do not intend to explore recognition techniques in the present work, we have assumed that a subsystem is responsible for informing our system of the activity.

As part of the monitoring protocol, the ABPM (of 24 h) is performed on the patient. This serves mainly to update the patient's blood pressure average. Next, the inference module uses as input the patient's blood pressure average subtracted by each new measurement. As a consequence, an average deviation is produced, which is part of the composition of the rules.

The physiological variables have been modeled in association with the behavioral and environmental variables. As has already been de-<sup>fi</sup>ned, the rules lead to a result from the system (patient state): normal, alert, or emergency. For example, for a sleeping person (Fig. 2), the SBP deviation in relation to the patient's average SBP – as long as it ranges between 0 and −10 mm Hg – is considered normal with full membership. The activity variable is treated as a singleton, that is, only whole values that represent each activity have full membership.

The fuzzy system con<sup>fi</sup>guration has the following parameters: the inference system is the Mamdani; the operator minimum was used for the implication function; for the performance aggregation, the additive operator was used; and <sup>fi</sup>nally, the bisection method was used for defuzzi<sup>fi</sup>cation. These parameters were relevant for the type of problem to be solved, and they were directed to obtain a gradual output from the system for each patient state. The parameters were established empirically, taking the decision-making module strategies into account.

Assigning a weight to each rule also had a decisive role in our proposal. These weights re<sup>fl</sup>ect the problem requirements, as individualization and the identi<sup>fi</sup>cation of critical situations. The criteria for weight assignment were the following: the rules containing the patient's averages should have a greater weight in relation to those that apply to any patient (generic rules); emergency situations have priority over alert and normal situations; and the rules that do not include blood pressure – for example, heart rate and environmental temperature – are assigned a relatively low weight.

A total of 63 rules were de<sup>fi</sup>ned. This large number is justi<sup>fi</sup>ed by the repetition of rules considering each of the 5 activities. For each activity, there are 10 rules that treat SBP and DBP. The 13 other rules are as follows: rules that reinforce emergency situations but are speci<sup>fi</sup>c for hypertensive patients, generic rules, and rules containing variables that do not involve blood pressure. The following example shows the resting rules in relation to the SBP (“deviationSBPResting” variable):

if (activity is resting) and (deviationSBPResting is very low) then (state is emergency)

if (activity is resting) and (deviationSBPResting is low) then (state is alert)

if (activity is resting) and (deviationSBPResting is normal) then (state is normal)

if (activity is resting) and (deviationSBPResting is high) then (state is alert)

if (activity is resting) and (deviationSBPResting is very high) then (state is emergency).

## 5. Learning module

The aim of the learning module is to customize rule parameters to avoid sending unnecessary alarms, using the physician's experience and data collected during a long-term monitoring period for this purpose. At the same time, the system must preserve emergency rules to assure reliability in identifying relevant cases that demand noti<sup>fi</sup>cation (i.e., avoiding false negatives).

The system must <sup>fi</sup>nd new tolerable values that do not consider extreme values that have already occurred. These alterations must be incremental and cautious regarding the proposed adjustment. An adjustment must not create con<sup>fl</sup>icts among the rules. Hence, the learning must be limited and supervised by a specialist. Taking this into account, rule clarity (in the sense of interpretability) must be guaranteed, disallowing the proposition of any adjustments that alter the initial formation of the rules and respecting the adjacent terms of a given fuzzy variable.

Thus, the adjustment mechanism has (see Fig. 1) the following three phases: 1) select a subinterval of mild alert cases (using synthetic data, as discussed in Section 5.1); 2) <sup>fi</sup>nd a representative point (presented in Section 5.2); and 3) adjust rules speci<sup>fi</sup>c to the activities (by means of adjusting the fuzzy set core as normal).

Our methodology for this adjustment is to keep the established distance between the adjacent terms in the initial rules to preserve the medical knowledge incorporated into the model. At the same time, we avoid full membership superposition; for example, $\nexists x | \mu _ { n o r m a l } ( x ) = \mu _ { h i g h } ( x ) = 1$ , where $\mu _ { A } ( { \boldsymbol { x } } )$ is the membership of x in set A.

![](/api/attachments/8HQADY89/fulltext/images/d5fabe446fce1fda6ddb4b072bc329637382739bdd43497e113e835d8a6dead6.jpg)  
Fig. 2. Systolic blood pressure deviation while the patient is sleeping.

## 5.1. synthetic data generation for vital signs monitoring

To build a prototype for the learning module, it is important to perform tests. This is only possible using synthetic data. It is fundamental to generate synthetic data that are very similar to real data. A very important step in this direction is to generate data based on the ABPM, a type of monitoring that is well established in medical practice.

The problem becomes even more complex for blood pressure control. Therefore, we believe that it is especially important to answer the following questions: a) do SPB (or DBP) synthetic data have the same probability distribution as the original data? b) Do synthetic data maintain the same correlations veri<sup>fi</sup>ed in the original data?

In analysis of the ABPM data distribution, we identify a normal distribution. However, this is only valid when we limit the data to only one speci<sup>fi</sup>c activity. Such a limitation is reasonable, considering that for most people, higher blood pressure values are found when the patient is awake and lower when he is sleeping, similarly to the way physical effort can increase vital signs.

Thus, the use of normal distribution in synthetic data generation increases the possibility of obtaining data that are more similar to real data, allowing the learning mechanism to be tested. Another argument is that the normal distribution has already been employed in other works involving the analysis of physiological data [10,20,26].

The correlation among vital signs represents a great challenge. This correlation varies from patient to patient; for some people, when a vital sign increases, another increases as well, while for others, when a certain vital sign increases, another decreases. This correlation must be preserved in the synthetic data so that we can reproduce the patient's vital signs as closely to reality as possible.

With the aim of generating data as similar as possible to that in the ABPM, we have developed Algorithm 1. In the implementation phase, we used the simulation software GenData [23], which generates data preserving the correlation of the data set. Finally, an elimination/ <sup>fi</sup>ltering process is applied to the synthetic data and speci<sup>fi</sup>cally to the blood pressure values, removing extremes values that are not found in the ABPM and considering a safety margin (tolerance).

```matlab
tolerance = 10;
activity = {sleeping, resting, eating, walking, domesticActiv};
foreach patient do
    foreach activity do
    data = getABPMData(activity);
    restrictions[] =
    getMinorAndMajorValueFromVitalSigns(data, tolerance);
    correlation = getVitalSignsCorrelation(data);
    syntheticData[activity]] = normalDistribution(data,
    correlation) syntheticData[activity]] =
    dataFilter(syntheticData[activity], restrictions);
    end
end
```  
Algorithm 1. Synthetic data generation algorithm.

## 5.2. Finding a representative point

The representative point of the mild alert cases gathers the values of each variable that will later be used to alter the parameters of the membership functions. In our study, no matter the technique chosen to determine the representative point, alerts occur in two forms: they are either below or above the patient's blood pressure average. In both groups, we must not consider – or at least, we must place less importance on – extreme values (outliers). Thus, two properties are desired: the elimination of outliers and the de<sup>fi</sup>nition of clusters.

Another important issue relates to the focus our work gives to BP. SBP and DBP share a unique quality among the vital signs because during the processing of blood pressure, neither value is dissociated. On the other hand, it is also possible to treat each of these variables in an isolated manner.

In our research, three different techniques were tested to obtain the representative point.<sup>2</sup> The separate treatment of SBP and DBP is accomplished using a simple technique called Average and Standard Deviation (ASD). The integrated treatment is performed with two techniques that use clusters: Fuzzy c-Means (FCM) [3] and Gustafson– Kessel (GK) [14]. These techniques have been chosen for their distinct methods of calculating distance in relation to a central point. With a solution that considers both the SBP and DBP averages – above and/or below the patient's averages – we obtain separate values that do not maintain the SBP/DBP correlation of the patient. Therefore, one question to be investigated is the effectiveness of the techniques that deal with SBP and DBP separately or together.

A description of the three techniques employed follows, while the tests and details regarding the techniques are presented in Section 6.2.

## 5.2.1. Average and standard deviation (ASD)

In the ASD method, for all alert cases, we divide SBP/DBP values into two sets: above and below the average values. We then form four groups using the patient's SBP/DBP general averages. The <sup>fi</sup>rst group contains the above-average SBP values. The second group includes the above-average DBP values. The third group contains the below-average SBP values. The below-average DBP values are in the fourth group. The following steps are performed for these groups: 1) calculate the average; 2) calculate the standard deviation; 3) eliminate extreme values; and 4) recalculate the average. The average is the representative point.

Due to the simplicity of the ASD, it can also be used with other physiological data, e.g., heart rate and weight. However, owing to the relationship between systolic and diastolic blood pressures [11], it would be interesting to investigate techniques that can assure a more sophisticated treatment, which is accomplished using these clustering techniques.

## 5.2.2. FCM clustering

The Fuzzy c-Means uses the Euclidean distance to calculate the central point. Here, the objective function is to minimize the Euclidean distance between each data object and its clustering center. A parallel objective is to maximize the Euclidean distance between cluster centers [22]. The Euclidean distance between points a and b in an n-dimensional Euclidean space, having $a = ( x _ { 1 } , x _ { 2 } , . . . , x _ { n } )$ and $b = ( y _ { 1 } , y _ { 2 } , . . . , y _ { n } )$ , is:

$$
d (a, b) = \sqrt {(x _ {1} - y _ {1}) ^ {2} + (x _ {2} - y _ {2}) ^ {2} + \ldots + (x _ {n} - y _ {n}) ^ {2}}.
$$

In both the FCM and GK techniques, it is necessary to choose the desired quantity of clusters (c) in advance. We have de<sup>fi</sup>ned this quantity as c=2, which refers to cluster values below and above the patient's blood pressure average. As previously explained, this behavior is expected because the alert points can only be higher or lower than the patient's average.

Fig. 3 presents the possibilities of alert point concentration. Inside the circular area, which includes the patient's general average, the possibility of alert cases is low. Outside the circle, 4 quadrants are identi<sup>fi</sup>ed and used to visualize where the alerts may occur. However, we assume that 2 representative points (which can be in 2 different quadrants or only 1) are enough because we seek a point that represents speci<sup>fi</sup>c concentrations of blood pressure variations. With 2 representative points, it is possible to have a point below and/or above average. Medical experience shows that in elders, SBP is usually high and DBP is unaltered, which accords with this restriction. The representative point, in this case, is between the 1st and the 4th quadrant.

![](/api/attachments/8HQADY89/fulltext/images/5bb5833399f70b4780cde85c10ed97b4c0076bcef0f37ed921fef3fb7feb2256.jpg)  
Fig. 3. Possible areas of alert clusters.

Let us consider an example: a patient with an SBP/DBP average (in mm Hg) of 125/85 and results for the two representative points of 110/70 (3rd quadrant) and 140/75 (4th quadrant). For the sake of adjustment of the SBP, the alert representative points are 140 and 110, one value above and one below the average. Knowing this, we can change the core of the normal set of the SBP variable (for a certain activity) to above and below. As for the DBP, the adjustment can be 70 or 75 because both values are below the average of 85. Thus, in clustering methods, during the representative point calculation process, the SBP/DBP values are treated jointly. However, they are dealt with separately when the adjustment is made to each variable.

## 5.2.3. GK clustering

The Gustafson–Kessel algorithm is a clustering technique that uses the Mahalanobis to determine the central point and is indicated for roughly hyperellipsoidal clustering con<sup>fi</sup>gurations; FCM is more indicated for hyperspheric shapes. The Mahalanobis distance is distinguished from the Euclidean for taking data set correlations into account. This characteristic is of interest in relation to the SBP/DBP because it determines a clustering center with a greater number of points around it. Another advantage is that it identi<sup>fi</sup>es a group that encompasses two quadrants positioned side by side, which does not result in a hyperspheric shape.

The Mahalanobis distance among a group of values with the average $\boldsymbol { \mu } = \left( \mu _ { 1 } , \mu _ { 2 } , \mu _ { 3 } , . . . , \mu _ { p } \right) ^ { T }$ and covariance matrix Σ for a multivariate vector ${ \boldsymbol { x } } = \left( x _ { 1 } , x _ { 2 } , x _ { 3 } , . . . , x _ { p } \right) ^ { T }$ is de<sup>fi</sup>ned as follows:

$$
D _ {M} (x) = \sqrt {(x - \mu) ^ {T} \Sigma^ {- 1} (x - \mu)}.
$$

## 5.3. Methodology for adjusting the rules

The adjustment of the speci<sup>fi</sup>c rules for each activity is the last phase of the learning process. Initially, the representative point is subtracted from the patient's average and results in a deviation. For example, if the representative point value of SBP is 140 and the patient's average is 125, the deviation will be 140−125=15. The deviation is the parameter for updating an existing rule.

The methodology adopted for the adjustment is to keep the distances between the adjacent fuzzy sets established in the original rules. Thus, we preserve the medical knowledge embedded in the model. At the same time, we avoid overlaps that occur with full membership: A <sup>fi</sup>nal requirement is to maintain the full membership of the “very low” and “very high” sets unaltered, which imply an emergency.

## 6. Model validation

This Section presents tests for the inference (Section 6.1) and learning (Section 6.2) modules. Additionally, a medical evaluation of the proposal – completed by specialists – is presented in Section 6.3. For these tests, we used real ABPM data obtained from 30 patients. To calculate the sample size, the methodology described in [5] was employed. The sample size of 30 patients was considered suf<sup>fi</sup>cient for this experiment. This sample size is justi<sup>fi</sup>ed by the focus of the study, i.e., SBP and DBP variables obtained from blood pressure monitoring have a small variation.

## 6.1. Inference module evaluation

The objective of the inference module test is to verify whether the alarms are identi<sup>fi</sup>ed as changes in data input occur. Table 1 presents the results for the ABPM data via the traditional method and via the method proposed in this paper (called System in Table 1). The patients were ranked in ascending order according to SBP/DBP and classi<sup>fi</sup>ed using the guidelines presented in [24]. These guidelines establish home monitoring patients with blood pressure greater than 135/85 mm Hg as hypertensive. Via the traditional method, all measurements above 135/85 mm Hg when awake and 120/70 mm Hg while sleeping are characterized as alert. Emergencies are not identi-<sup>fi</sup>ed; it is the physician's responsibility to make this analysis later. We have adopted the term “traditional method” because this is the current manner with which systems process ABPM data.

We de<sup>fi</sup>ned the percentage of alarms as follows:

$$
\% \text {alarms} = ((\text {alert} + \text {emergencies}) / \text {normal}) * 100.
$$

The system indicated a percentage of alarms higher than the ABPM traditional analysis for only the <sup>fi</sup>rst four patients, who have low blood pressure values. This may be because the traditional method does not indicate such low values. The high quantity of alarms produced via the traditional method, on the other hand, occurs because the method considers neither the activity being performed nor the patient's average, among other factors. Another contribution of the inference method is the identi<sup>fi</sup>cation of emergencies that can trigger new measurements and the noti<sup>fi</sup>cation of health professionals.

Evaluation of ABPM data: traditional vs. system.

<table><tr><td rowspan="2">ID</td><td colspan="3">Traditional</td><td colspan="3">System</td><td colspan="2">% alarms</td></tr><tr><td>Normal</td><td>Alert</td><td>Emerg.</td><td>Normal</td><td>Alert</td><td>Emerg.</td><td>Tradit.</td><td>System</td></tr><tr><td>1</td><td>76</td><td>3</td><td>-</td><td>59</td><td>19</td><td>1</td><td>4</td><td>34</td></tr><tr><td>2</td><td>70</td><td>11</td><td>-</td><td>54</td><td>25</td><td>2</td><td>16</td><td>50</td></tr><tr><td>3</td><td>48</td><td>10</td><td>-</td><td>41</td><td>16</td><td>1</td><td>21</td><td>41</td></tr><tr><td>4</td><td>53</td><td>3</td><td>-</td><td>45</td><td>9</td><td>2</td><td>6</td><td>24</td></tr><tr><td>5</td><td>53</td><td>22</td><td>-</td><td>57</td><td>16</td><td>2</td><td>42</td><td>32</td></tr><tr><td>6</td><td>66</td><td>12</td><td>-</td><td>66</td><td>11</td><td>1</td><td>18</td><td>18</td></tr><tr><td>7</td><td>50</td><td>29</td><td>-</td><td>58</td><td>20</td><td>1</td><td>58</td><td>36</td></tr><tr><td>8</td><td>39</td><td>26</td><td>-</td><td>49</td><td>13</td><td>3</td><td>67</td><td>33</td></tr><tr><td>9</td><td>50</td><td>21</td><td>-</td><td>56</td><td>8</td><td>7</td><td>42</td><td>27</td></tr><tr><td>10</td><td>16</td><td>65</td><td>-</td><td>67</td><td>14</td><td>0</td><td>406</td><td>21</td></tr><tr><td>11</td><td>33</td><td>45</td><td>-</td><td>50</td><td>22</td><td>6</td><td>136</td><td>56</td></tr><tr><td>12</td><td>20</td><td>41</td><td>-</td><td>41</td><td>18</td><td>2</td><td>205</td><td>49</td></tr><tr><td>13</td><td>19</td><td>38</td><td>-</td><td>37</td><td>15</td><td>5</td><td>200</td><td>54</td></tr><tr><td>14</td><td>15</td><td>42</td><td>-</td><td>34</td><td>23</td><td>0</td><td>280</td><td>68</td></tr><tr><td>15</td><td>8</td><td>56</td><td>-</td><td>46</td><td>18</td><td>0</td><td>700</td><td>39</td></tr><tr><td>16</td><td>6</td><td>69</td><td>-</td><td>58</td><td>14</td><td>3</td><td>1150</td><td>29</td></tr><tr><td>17</td><td>1</td><td>79</td><td>-</td><td>62</td><td>17</td><td>1</td><td>7900</td><td>29</td></tr><tr><td>18</td><td>7</td><td>54</td><td>-</td><td>37</td><td>22</td><td>2</td><td>771</td><td>65</td></tr><tr><td>19</td><td>6</td><td>75</td><td>-</td><td>45</td><td>36</td><td>0</td><td>1250</td><td>80</td></tr><tr><td>20</td><td>1</td><td>68</td><td>-</td><td>39</td><td>24</td><td>6</td><td>6800</td><td>77</td></tr><tr><td>21</td><td>8</td><td>71</td><td>-</td><td>35</td><td>41</td><td>3</td><td>888</td><td>126</td></tr><tr><td>22</td><td>2</td><td>77</td><td>-</td><td>53</td><td>26</td><td>0</td><td>3850</td><td>49</td></tr><tr><td>23</td><td>2</td><td>55</td><td>-</td><td>38</td><td>16</td><td>3</td><td>2750</td><td>50</td></tr><tr><td>24</td><td>8</td><td>50</td><td>-</td><td>25</td><td>32</td><td>1</td><td>625</td><td>132</td></tr><tr><td>25</td><td>3</td><td>77</td><td>-</td><td>58</td><td>22</td><td>0</td><td>2567</td><td>38</td></tr><tr><td>26</td><td>1</td><td>59</td><td>-</td><td>37</td><td>18</td><td>5</td><td>5900</td><td>62</td></tr><tr><td>27</td><td>1</td><td>57</td><td>-</td><td>32</td><td>25</td><td>1</td><td>5700</td><td>81</td></tr><tr><td>28</td><td>4</td><td>75</td><td>-</td><td>29</td><td>48</td><td>2</td><td>1875</td><td>172</td></tr><tr><td>29</td><td>1</td><td>45</td><td>-</td><td>20</td><td>26</td><td>0</td><td>4500</td><td>130</td></tr><tr><td>30</td><td>0</td><td>63</td><td>-</td><td>25</td><td>38</td><td>0</td><td>-</td><td>152</td></tr></table>

The results presented by the inference module demonstrate that the system provides the main requirements for long-term monitoring. The identi<sup>fi</sup>cation of an alarm focuses on large variations because it uses the patient's average and respects a tolerance margin that depends on the activity being performed in the minutes before the measurement is made. Hypertensive patients are treated in a differentiated manner, which allows physicians to give more attention to cases that demand analysis of the causes of blood pressure variations.

## 6.2. Learning module evaluation

The tests of the learning module aim to validate the adjustment mechanism. The goal is to <sup>fi</sup>nd a representative point that once obtained, alters the core of a variable's normal set, creating a new con<sup>fi</sup>guration for the fuzzy inference system.

The input data necessary for <sup>fi</sup>nding the representative point involves ABPM mild alerts and synthetic data. With regard to the latter, 20 different series of data are generated for each patient. For each ABPM record, new SBP, DBP and FC synthetic data are generated, and the activity variable value is maintained. This strategy is consistent with our proposal, as we have associated physiological data with behavior. Conversely, if a new activity is generated, we lose the association among the classes of variables.

In a simpli<sup>fi</sup>ed way, our focus is on determining the representative point in the three techniques: Euclidean Distance (used by FCM), Mahalanobis Distance (used by GK) and the ASD central point. The implementation of the ASD technique was accomplished using code written in C#; the FCM technique implementation was built in Matlab; and the GK algorithm, in its turn, was implemented by adapting the code presented in [1].

Fig. 4 presents the results of the two clustering techniques for the activity characterized as resting. The circles identify the representative/ central points' positions for FCM, and the asterisk identi<sup>fi</sup>es those of GK. The GK clustering technique is unable to de<sup>fi</sup>ne a low value for the SBP. The value obtained, 132, is above the average of 127. We observe that GK did not attribute great relevance to the dispersed set with SBP and DBP low values (3rd quadrant). For this reason, GK does not present a representative point for a below-average adjustment. Even so, this can be understood as a stability factor, as modi<sup>fi</sup>cations will not be proposed based on scattered data. Alternatively, FCM creates central points in clusterings with few elements.

![](/api/attachments/8HQADY89/fulltext/images/91ca259cf22af8ca45d8577c9d9ca3c3f8650325cd68a021a5db5d0d568d51a5.jpg)  
Fig. 4. Central points for patient 9 at rest. The patient's average is 127/73 (‘A’). The results obtained for the FCM were 147/82 and 112/64; for the GK, they were 146/86 and 132/64; and for ASD, they were 143/83 and 107/64.

In the next test, we made a comparison before and after the learning process using only the ABPM data. Before the learning process, we have a fuzzy inference system (one con<sup>fi</sup>guration) for an input of ABPM data. After the learning process is executed, we have 20 different con<sup>fi</sup>gurations for the inference module; each of the con<sup>fi</sup>gurations is executed 20 times. The number of alarms is accounted for in the sleeping and resting activities.

These results show that the three techniques reduce the number of alerts that occur after the learning process. Although the number of alerts is very similar between the techniques, FCM was the most tolerant (smallest amount of alerts), followed by GK and <sup>fi</sup>nally ASD, the most rigid. Using the Euclidean distance for calculating the representative point, FCM is able in most situations to position two points in two quadrants. However, in GK, when there is a great concentration of points in one quadrant, the representative points tend to remain in the same quadrant. As a consequence, FCM proposes values above and below the average, which allows the inclusion of more alerts to be considered normal. Despite the fact that it always proposes values that are above and below the average, ASD presents the disadvantage of treating both SBP and DBP separately, thus considering values that should not be included in the computation.

## 6.3. Medical evaluation of the proposal

As a <sup>fi</sup>nal evaluation of the system, two physicians classi<sup>fi</sup>ed the original ABPM data of the 30 patients. The physicians (here identi<sup>fi</sup>ed as physician A and physician B) classi<sup>fi</sup>ed each measurement as normal, alert or emergency. After the medical evaluation, the system executed with and without the learning process. The execution performed without the learning process encompasses a set of initial rules. In this situation, more tolerance to variations in each patient's physiological data is expected.

A good result for the system is the correct identi<sup>fi</sup>cation of normal, alert and emergency, indicated, respectively, as ‘N’, ‘A’, and ‘E’ in Tables 2 and 3 in the sequel. A crucial point is when a physician identi<sup>fi</sup>es an emergency and the system identi<sup>fi</sup>es it as a normal case, which characterizes a false negative. Conversely, the system's identi-<sup>fi</sup>cation of an emergency not detected by a physician is not likely to be harmful, but it de<sup>fi</sup>nitely characterizes a false positive.

Tables 2(a), (b) and 3(a), and (b) present the confusion matrices with the medical evaluations (rows) and the system results (columns). For the sake of simpli<sup>fi</sup>cation, the results in the with learning tables are shown only for the FCM technique, as the results obtained with this technique are very similar to those obtained via GK and ASD; the reason for this similarity will be explained later. For instance, in Table 2(a) we can observe that physician A identi<sup>fi</sup>ed 10 emergencies and that the system classi<sup>fi</sup>ed one of them as an alert. Physician B, however (Table 3(a) and (b)), did not identify any emergency cases.

Table 2  
Confusion matrix: physician A.

<table><tr><td>Evaluation</td><td colspan="3">System</td></tr><tr><td>Medical</td><td>N</td><td>A</td><td>E</td></tr><tr><td colspan="4">(a) Without learning</td></tr><tr><td>N</td><td>1267</td><td>530</td><td>6</td></tr><tr><td>A</td><td>1</td><td>58</td><td>30</td></tr><tr><td>E</td><td>0</td><td>1</td><td>9</td></tr><tr><td colspan="4">(b) With learning</td></tr><tr><td>N</td><td>1648</td><td>149</td><td>6</td></tr><tr><td>A</td><td>2</td><td>52</td><td>35</td></tr><tr><td>E</td><td>0</td><td>0</td><td>10</td></tr></table>

Table 3  
Confusion matrix: physician B.

<table><tr><td>Evaluation</td><td colspan="3">System</td></tr><tr><td>Medical</td><td>N</td><td>A</td><td>E</td></tr><tr><td colspan="4">(a) Without learning</td></tr><tr><td>N</td><td>1268</td><td>560</td><td>17</td></tr><tr><td>A</td><td>0</td><td>29</td><td>28</td></tr><tr><td>E</td><td>0</td><td>0</td><td>0</td></tr><tr><td colspan="4">(b) With learning</td></tr><tr><td>N</td><td>1647</td><td>175</td><td>23</td></tr><tr><td>A</td><td>3</td><td>26</td><td>28</td></tr><tr><td>E</td><td>0</td><td>0</td><td>0</td></tr></table>

In all the scenarios, cases of false negatives did not occur (emergencies that the system classi<sup>fi</sup>ed as normal). This is a matter of extreme importance for the system because it is one of the aspects that guarantee its reliability. We calculated the level of accuracy obtained with and without learning. Accuracy is de<sup>fi</sup>ned as the sum of correctly classi<sup>fi</sup>ed cases (i.e., values in the main diagonal of the confusion matrix) divided by the total number of cases. In the without learning situation, the system accuracy is 70% when compared to physician A's opinion and 68% when compared to physician B's opinion. After executing the learning process, the results achieved as compared with physician A's opinion were 90% accuracy with the FCM technique, 88% with GK, and 86% with ASD. The results relative to physician B's opinion were 2% smaller than the results of physician A.

The number of emergencies after executing the learning process remained the same as the number of emergency alerts reported before running it. Therefore, despite the adjustments produced in the alert cases, the system accomplished its goal of remaining strict for emergency cases while tolerating variations that were considered mild from a medical point of view.

After executing the learning process in the examples, we can observe that 2 cases in Tables 2(b), and 3 cases in Table 3(b) were considered alerts by the physicians and classi<sup>fi</sup>ed as normal by the system. Among these, only one was agreed upon by the physicians to be a certain case of alert. This is the case of a low DBP value resulting from the patient's having informed the system that he was sleeping. Due to this activity, the system classi<sup>fi</sup>ed the situation at the boundary between normal and alert. Because this was the <sup>fi</sup>rst measurement that initiated the period of sleep reported by the patient, it might be the case that he was not yet sleeping, which would cause the system to trigger an alarm. The other cases classi<sup>fi</sup>ed as normal are also consistent with the possibility of data having been input incorrectly by the patient.

The FCM technique obtained the best results, as the number of cases it detected as alerts (that were considered normal by physicians) is smaller than those obtained by GK and ASD. When it comes to the core adjustment of each variable's normal sets, FCM makes a more comprehensive adjustment than the other techniques. This is due to the greater distance FCM offers between the proposed adjustment points while simultaneously monitoring the correlation between SBP and DBP. The intermediate result for GK demonstrates that monitoring correlations is more effective than simply measuring the points' average, as ASD does. However, more experiments on real monitoring will have to be conducted for a complete evaluation.

## 7. Conclusions

This work presented a novel decision-making mechanism for context inference in pervasive health monitoring applications. The proposed monitoring model contemplates rules that perform environmental, physiological and behavioral data fusion. Hence, this system provides a useful tool to support medical analysis. The identi<sup>fi</sup>cation of critical situations is performed in real time in a continuous manner and is supervised by a physician, who controls the system's behavior at a high level (by means of the concept of mild alerts). Thus, our proposal contributes to the creation of individualized models of the patient in the context of health-monitoring in pervasive environments. In practice, the decision mechanism attains a lower rate of false alarms compared to the traditional method of analyzing data from ABPM. This result contributes to a greater acceptance by the medical community of this kind of monitoring system in the identi<sup>fi</sup>cation of critical situations.

An important issue is that a number of variables can be considered in the solution due to the system's <sup>fl</sup>exibility. The adopted model helps solve intrinsic ambiguities that are inherent to the process of monitoring variables with mutual correlation. Likewise, the model makes it possible to prioritize the rules containing the most signi<sup>fi</sup>- cant variables from a medical point of view.

A great challenge for health-monitoring systems that use rules is to perform the learning model without jeopardizing the interpretability of the rules. This proposal addresses this issue with a set of solutions: the inference system uses few variables for the antecedent of each rule, the adjustments are performed under medical supervision, and <sup>fi</sup>nally, the learning takes place based on representative points that serve to adjust speci<sup>fi</sup>c rules. The strategy of turning mild alert cases into normal cases allows the system to be used for long-term monitoring.

We have improved the quality of the dataset used for vital sign monitoring because each patient has his/her own peculiarities and may even live a normal life despite having abnormal blood pressure, for example. The evaluation using real data from ABPM con<sup>fi</sup>rmed this fact by achieving good results with both hypotensive and hypertensive patients. In addition, we believe that the use of a clustering technique, instead of a global optimization such as that presented in [26], makes it easier for the physician to comprehend the proposed new settings for the adjusted parameters.

The data used to test the learning process were obtained via synthetic data generation based on data derived from real patients, preserving the SBP/DBP correlation and treating the original data classi<sup>fi</sup>ed by the activity variable. In consideration of the activity being performed, the stronger the relationship between the vital signs and contextual information, the more consistent the synthetic data will be.

ABPM data has one basic limitation: people do not take note of all their activities. We believe that by using subsystems that autonomously recognize an activity, especially the intensity of the movements involved, we can improve the association between the collected physiological and behavioral data.

To our knowledge, there are no available databases containing data obtained from daily monitoring of a patient over a relatively long period. To overcome this lack of data, which hinders the learning process, we produced synthetic data reproducing a similar pattern to that found in real data. Potentially, this data generation approach can help reduce the system adaptation period for the individual being monitored, but more tests are needed. To address this, we intend to develop a database of measurements and make the set of rules for blood pressure monitoring available. Therefore, other research groups will be able to propose changes, such as the inclusion of other rules and variables, contributing to the evaluation and evolution of the proposed approach.

## Acknowledgments

The authors thank CNPq and FAPERJ for partially funding the present work and are in debt to Prof. A.C.L. da Nóbrega and Dr. T.P.C. Barbosa for their support in the areas of health and medicine.

## References

[1] J. Abonyi, B. Feil, Cluster analysis for data mining and system identi<sup>fi</sup>cation, Birkhäuser Basel 2007

[2] C. Anagnostopoulos, S. Hadjiefthymiades, Advanced fuzzy inference engines in situation aware computing Fuzzy Sets and Systems 161 (4) (2010) 498–521.

[3] J.C. Bezdek, Pattern Recognition with Fuzzy Objective Function Algorithm, Plenum Press, NewYork, USA, 1981.

[4] G. Castellano, A.M. Fanelli, C. Mencar, Design and application of hybrid intelligent systems, in: Ch. Design of Transparent Mamdani Fuzzy Inference Systems, IOS Press, Amsterdam, The Netherlands, 2003, pp. 468–476.

[5] W.G. Cochran, Sampling Techniques, 3rd edition Wiley, New York, USA, 1977.

[6] A. Copetti, Monitoramento inteligente e sensível ao contexto na assistência domiciliar telemonitorada (in Portuguese), Ph.D. thesis, Instituto de Computação, Universidade Federal Fluminense, Niterói, Brazil (December 2010).

[7] A.C.L. da Nobrega, The subacute effects of exercise: concept, characteristics, and clinical implications, Exercise and Sport Sciences Reviews 33 (2) (2005) 84–87.

[8] I. Derbel, N. Hachani, H. Ounelli, in: Membership Functions Generation Based on Density Function, International Conference on Computational Intelligence and Security, 1, 2008, pp. 96–101.

[9] F. Duchêne, C. Garbay, V. Rialle, Learning recurrent behaviors from heterogeneous multivariate time-series, Arti<sup>fi</sup>cial Intelligence in Medicine 39 (1) (2007) 25–47

[10] E. El-Samahy, M. Mahfouf, D.A. Linkens, A closed-loop hybrid physiological model relating to subjects under physical stress, Arti<sup>fi</sup>cial Intelligence In Medicine 38 (3) (2006) 257–274.

[11] B. Gavish, I.Z. Ben-Dov, M. Bursztyn, Linear relationship between systolic and diastolic blood pressure monitored over 24 h: assessment and correlates, Journal of Hypertension 26 (2) (2008) 199–209

[12] S.N. Ghazavi, T.W. Liao, Medical data mining by fuzzy modeling with selected features, Arti<sup>fi</sup>cial Intelligence in Medicine 43 (3) (2008) 195–206.

[13] S. Guillaume, Designing fuzzy inference systems from data: an interpretabilityoriented review, IEEE Transactions on Fuzzy Systems 9 (3) (2001) 426–443.

[14] E.E. Gustafson, W.C. Kessel, in: Fuzzy Clustering with a Fuzzy Covariance Matrix, IEEE Conference on Decision and Control, 17, 1979, pp. 761–766.

[15] J. Han, M. Kamber, A. Tung, Spatial clustering methods in data mining: a survey, Geographic Data Mining and Knowledge Discovery 21 (2001) 1–29.

[16] F. Hoffmann, Evolutionary algorithms for fuzzy control system design, Proceedings of the IEEE 89 (9) (2001) 1318–1333.

[17] R. Huang, in: Adaptive Fuzzy Control: A GA Approach, Fifth IEEE International Conference on Fuzzy Systems, 2, 1996, pp. 1266–1272.

[18] P. Leijdekkers, V. Gay, E. Lawrence, Smart homecare system for health tele monitoring, First International Conference on the Digital Society, 2007.

[19] D. Mion, W. Oigman, F. Nobre, MAPA: Monitorização Ambulatorial da Pressão Arterial. (in Portuguese) 3rd edition Atheneu RJ, 2004.

[20] P. R. Norris, Toward new vital signs: Tools and methods for physiologic data capture, analysis, and decision support in critical care, Ph.D. thesis, Biomedical Informatics, Vanderbilt University, Nashville, Tennessee, USA (May 2006)

[21] J. Pärkkä, J. Merilahti, E. Mattila, E. Malm, K. Antila, M. Tuomisto, A. Saarinen, M. van Gils, I. Korhonen, Relationship of psychological and physiological variables in longterm self-monitored data during work ability rehabilitation program, IEEE Transactions on Information Technology in Biomedicine 13 (2) (2009) 141–151.

[22] T. Ross, Fuzzy Logic with Engineering Applications, McGraw-Hill, New York, USA, 1995.

[23] J. Ruscio, N. Haslam, Introduction to the Taxometric Method: A Practical Guide, Lawrence Erlbaum, 2006.

[24] SBC, V Diretrizes Brasileiras de Hipertensão Arterial. (in Portuguese) Arquivos Brasileiros de Cardiologia 89 (3) (2007) 1–56.

[25] S. Sneha, U. Varshney, Enabling ubiquitous patient monitoring: model, decision protocols, opportunities and challenges, Decision Support Systems 46 (3) (2009) 606–619.

[26] M.G. Tsipouras, C. Voglis, D.I. Fotiadis, A framework for fuzzy expert system creationapplication to cardiovascular diseases, IEEE Transactions on Biomedical Enginnering 54 (11) (2007) 2089–2105.

![](/api/attachments/8HQADY89/fulltext/images/2c3650aee16222375c04474a77524032e352b491ddd0f76424364940e8cd73da.jpg)  
Alessandro Copetti is an Associate Professor at the Department of Computer Science of Fluminense Federal University (UFF), in Rio das Ostras, Brazil. He received the B.Sc. degree in Computer Science, in 1994, from the Universidade do Noroeste do Estado do Rio Grande do Sul and the M.Sc, in Computer Science, in 2000, from the Catholic University of Rio Grande do Sul and the Ph.D. in Computer Science, in 2010, from the Fluminense Federal University. His current interests include pervasive healthcare, ubiquitous computing and computational intelligence. He is a member of the ACM and the Brazilian Computer Society (SBC).

![](/api/attachments/8HQADY89/fulltext/images/e0065ccb09fe18b522b7da077b5c447d1edcd1b289df601770b8ba06ebabd20e.jpg)

Julius C. B. Leite is a Professor at the Computing Institute of Fluminense Federal University (UFF), in Niterói, Brazil He received the B.Sc. degree in Electronics Engineering, in 1974, and the M.Sc. in Digital Electronics, in 1977, both from the Catholic University of Rio de Janeiro and the Ph.D. degree, in 1983, from the University of Manchester Institute of Science and Technology, UK. His interests in: clude real-time systems power-aware systems and sensor networks. He is a member of the Brazilian Computer Society (SBC). coordinates the Tempo Laboratory at UFE and has served on program committees of several international conferences.

![](/api/attachments/8HQADY89/fulltext/images/4dbfe5d94f3b3bdd3ec70eb3be763e3f0f067d56471e680cfea7385e0938392b.jpg)

Orlando Loques is a Professor at the Computing Institute of Fluminense Federal University (UFF), in Niterói, Brazil. He received the B.Sc. degree in Electronics Engineering, in 1973, and the M.Sc. in Digital Electronics in 1976, both from the Catholic University of Rio de Janeiro. In 1984, he received the Ph.D. degree in Computer Science from the Imperial College of Science and Technology, UK. His interests include distributed and parallel systems, pervasive and ubiquitous computing, and energy-aware computing. He is a member of the ACM and the Brazilian Computer Society (SBC), and has served on several scienti<sup>fi</sup>c committees.

![](/api/attachments/8HQADY89/fulltext/images/42de3226f3afe9862e0f7fefaba9002c6be6db7d3594e5d9e71aca47fec304a8.jpg)

Mario Fritsch Neves is a Professor at the State University of Rio de Janeiro (UERJ), Brazil, working in the Department of Clinical Medicine. He received the B.Sc. degree in Medicine, in 1986, and he completed Residence in Internal Medicine, in 1989, and received the M.Sc. in Cardiology, in 1997, and the Ph.D. in Biomedical Sciences, in 2003. His fellowship was in Experimental Hypertension at Institute of Clinical Research of Montreal (Canada, 2001–2002). He is member of the Brazilian Society of Cardiology (SBC) and the current President of Society of Hypertension in the State of Rio de Janeiro (SOHERJ).
