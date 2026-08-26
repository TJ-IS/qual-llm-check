---
otero_id: 2488
otero_key: "YJ9WVXYD"
title: "Decision support system for Warfarin therapy management using Bayesian networks"
authors: "Barbaros Yet; Kaveh Bastani; Hendry Raharjo; Svante Lifvergren; William Marsh; Bo Bergman"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.10.007"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Decision support system for Warfarin therapy management using Bayesian networks

Barbaros Yet <sup>a,</sup>⁎, Kaveh Bastani <sup>a</sup>, Hendry Raharjo <sup>a</sup>, Svante Lifvergren <sup>b</sup>, William Marsh <sup>c</sup>, Bo Bergman <sup>a</sup>

<sup>a</sup> Department of Technology Management and Economics, Division of Quality Sciences, Chalmers University of Technology, 412 96 Gothenburg, Sweden

<sup>b</sup> The Skaraborg Hospital Group, 541 85, Skövde, Sweden

<sup>c</sup> School of Electronic Engineering and Computer Science, Queen Mary, University of London, London E1 4NS, UK

## a r t i c l e i n f o

Available online 6 October 2012

Keywords: Bayesian networks Warfarin therapy Anticoagulant therapy Decision support systems

## a b s t r a c t

Warfarin therapy is known as a complex process because of the variation in the patients' response. Failure to deal with such variation may lead to death as a result of thrombosis or bleeding. The possible sources of variation such as concomitant illnesses and drug interactions have to be investigated by the clinician in order to deal with the variation. This paper describes a decision support system (DSS) using Bayesian networks for assisting clinicians to make better decisions in Warfarin therapy management. The DSS is developed in collaboration with a Swedish hospital group that manages Warfarin therapy for more than 3000 patients. The proposed model can assist the clinician in making dose-adjustment and follow-up interval decisions, investigating variation causes, and evaluating bleeding and thrombosis risks related to therapy. The model is built upon previous <sup>fi</sup>ndings from medical literature, the knowledge of domain experts, and large dataset of patients.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Warfarin is an oral anticoagulant that is mainly used for preventing thrombosis and embolism in several clinical disorders including atrial <sup>fi</sup>brillation and pulmonary embolism. The duration of Warfarin therapy is often between three months and a lifetime [12]. The effects of Warfarin are generally monitored by International Normalized Ratio (INR) which is the ratio of patient's blood coagulation time to a reference sample. Patients' INR values should be kept within a target therapeutic range since mortality risk will increase considerably if the INR value is outside this range [27].

According to a large multicenter randomized study by Poller et al. [28] the quality of the manual Warfarin management is still not adequate as patients can be kept within therapeutic range only 65% of the time. In Sweden, approximately 150,000 patients are treated with Warfarin and this number is increasing steadily [35]. According to Swedish statistics, around 12 patients die each year as a result of bleedings caused by Warfarin therapy and similar anticoagulant therapies [34]. There appears to be a signi<sup>fi</sup>cant room for improvement to keep the patients' INR values within therapeutic range and to minimize Warfarin related risks.

There are a number of ‘variation factors’ such as drug interactions and concomitant diseases which can increase Warfarin therapy risks by causing unexpected increases or decreases in the INR value [12].

It is dif<sup>fi</sup>cult to know the presence of these factors in advance since some of the variation factors are commonly consumed products such as leafy vegetables, and their consumption usually varies in time. Clinicians have to investigate the presence of these factors in order to lower the risks of Warfarin therapy.

Decision support systems (DSS) have been used for assisting the decision making in Warfarin therapy since 1976 [40]. The main outputs of the Warfarin DSS are dose adjustments (how much the dose should be adjusted?) and follow-up intervals (when should the patient take the next INR test?) [8]. Various studies have shown that DSS are capable of increasing the quality of Warfarin therapy [10,28]. None of the reviewed DSS assists the investigation of variation factors during Warfarin therapy. Moreover, many existing DSSs such as regression models do not deal with the dynamic nature of the therapy (See Section 2).

This paper proposes a DSS using Bayesian networks (BN) for assisting the management of Warfarin therapy. The objective of this DSS is to support dose and follow-up interval decisions while predicting cerebral bleeding and stroke risks, and to assist the investigation of variation factors. Other advantages of the proposed DSS include its <sup>fl</sup>exibility in terms of inputs and outputs, and training support for clinicians.

The BN model has been built in collaboration with the Skaraborg Hospital Group, SkaS, Sweden. The structure of the model is based on relevant medical <sup>fi</sup>ndings published in reputable international journals and the knowledge of the physicians and nurses who are actively working on Warfarin therapy. The parameters of the model are identi<sup>fi</sup>ed from a large dataset of patients, elicitations with the domain experts and published statistics in medical literature.

Genie-SMILE software [11] was used for building and calculating the BN.

The rest of this paper is organized as follows. Previous DSS for Warfarin therapy are reviewed in Section 2. The BN model for Warfarin therapy management is described in Section 3. Validation of the model is presented in Section 4. An example of using the model is provided in Section 5. Discussions and conclusions are presented in Sections 6 and 7 respectively.

## 2. Decisions support systems for Warfarin therapy

Several modeling approaches have been used to develop DSS for Warfarin therapy (Table 1). The main outputs of these models are similar: dose amounts and follow-up intervals; on the other hand their inputs and working principles differ. In the remainder of this section the advantages and disadvantages of several Warfarin therapy DSS are discussed.

Proportional-derivative [24,36] and Bayes forecasting [33] models calculate the recommended dose adjustments from the patient's previous INR values and dose intakes. These models are suitable for the dynamic nature of the treatment since their outputs are based on historical <sup>fl</sup>uctuations of the INR value. On the other hand, they do not take variation factors into account while calculating their outputs. Proportional-derivative and Bayes forecasting models are relatively simple models with few inputs.

Regression models for Warfarin therapy [31,39] output a single dose recommendation based on several variables about the patient's background and variation factors. The previous dose intakes and INR values are not inputs for the reviewed regression models; therefore, these models do not provide decision support on adjusting the dose amount in the long term-therapy. Moreover, regression models are not <sup>fl</sup>exible in terms of required inputs. For example, if a patient's height is an input for a regression model that predicts a Warfarin dose, then the user of the model must know or estimate the height of a particular patient to get the output of the model. This may not be practical if there are numerous inputs and the model is frequently used.

Rule-based models for Warfarin therapy [25,41] are based on clinical guidelines and expert knowledge. These models can have many inputs including variation factors and patient background. On the other hand, they assume that presence of the variation factors and patient background is already known by the user. In other words, these models output a dose-recommendation and a followup interval if the user has information about the presence of the variation factors; however they do not assist the user to <sup>fi</sup>nd the cause of an unexpected INR increase. Moreover, rule-based models are in<sup>fl</sup>exible in their required inputs like the regression models.

## 3. Bayesian network model for the Warfarin therapy DSS

Bayesian networks have been widely used in medical reasoning for diagnosis, treatment selection, risk analysis, and knowledge discovery [21–23,38]. However, their applications to the management of long-term medical therapies have been rare. The DSS presented in this paper is for managing Warfarin therapy, the duration of which is usually between three months and a lifetime [12]. Section 3.1 presents general information about BN and their bene<sup>fi</sup>ts for Warfarin therapy. Sections 3.2 and 3.3 explain respectively how the BN's graphical structure is developed and its parameters are learnt.

Methods used in DSSs for Making Dose Adjustment and Follow-up interval Decisions.

<table><tr><td>Type of DSS</td><td>Dose amount</td><td>Follow-up interval</td></tr><tr><td>Proportional-derivative controllers [24,36]</td><td>X</td><td></td></tr><tr><td>Bayesian forecasting [33]</td><td>X</td><td></td></tr><tr><td>Regression models [31,39]</td><td>X</td><td></td></tr><tr><td>Rule-based approaches [25,41]</td><td>X</td><td>X</td></tr></table>

## 3.1. Why Bayesian networks?

Bayesian networks are graphical models that represent probabilistic relations and conditional independence among a set of random variables. This section provides a brief overview about BNs; the readers are referred to Koller and Friedman [17] for a more thorough explanation.

A BN consists of a graphical structure and numerical parameters. The structure of the BN is an acyclic graph that consists of nodes that represent the variables and directed arcs that represent the conditional independence assumptions between these variables [17]. If there is an arc from one node to another, the latter is called a child node and the former is called a parent node. The probability of each node is conditioned only on their parent nodes; therefore each node is conditionally independent of their non-descendants given their parents. The joint probability distribution of the model can be represented compactly in a factorized way due to these independence assumptions. The graphical structure and conditional independency assumptions of the BNs are suitable for eliciting causal and associational knowledge from experts and published research results [17].

The parameters of a BN determine the strength of the probabilistic relations between its nodes. Each node in the BN has a set of mutually exclusive and collectively exhaustive states with a probability distribution conditional on the states of its parent nodes, or an unconditional distribution if the node does not have any parents. The conditional and unconditional probabilities can be learned from available data, elicited from domain experts, or gathered from published statistics in medical literature [17]. A BN can have discrete or continuous variables. A discrete variable's probability distribution is shown by a conditional probability table (CPT). All the variables in our BN are discrete; readers are referred to [20,26] for a detailed discussion about using continuous nodes in BNs.

A BN can calculate the posterior probability distributions of its unobserved nodes given the states of the nodes that have been observed (instantiated). It is possible to instantiate any number of nodes in any part of the model and to calculate the posterior probability distributions for the remaining nodes accordingly. Therefore, BNs gives the user a great deal of freedom since the inputs and outputs of the model are not distinguished.

Bayesian networks can be used to make either predictive or diagnostic inferences depending on the available observations. Diagnostic inference is done from symptoms to causes, in the opposite direction of a BN's arcs. For example, if a clinician observes an unusually low INR value, this will increase the belief about a higher Vitamin K intake since a low INR value could be a symptom of high Vitamin K level. Predictive inference is done from causes to effects, in the direction of a BN's arcs. For example, if the clinician has not yet measured the INR value but knows that a patient increased the intake of Vitamin K, this will increase the belief about a lower INR value.

## 3.2. Structure of the model

The model was developed for the patients that have been receiving Warfarin therapy for more than 14 days, described as the maintenance phase of the therapy [8]. There were two main reasons for limiting the model to these patients. Firstly, at the start of therapy, patients are closely monitored by a physician since the drug's effect for these patients may not yet be known [1]. However, patients in the maintenance phase are reviewed at greater intervals. Interventions and follow-up intervals have to be carefully arranged for these patients since there will be a delay before undesired effects are observed and precautions are taken. Secondly, the number of patients in the maintenance phase is signi<sup>fi</sup>cantly higher. For example, in Skaraborg Hospital group approximately 98% of the Warfarin patients are in the maintenance phase. The available resources need to be carefully allocated to these patients to minimize the treatment risks while reducing unnecessary follow-ups.

![](/api/attachments/YJ9WVXYD/fulltext/images/2f62c39db0253f1dca991556bd322a3bc20bc0c40b2839174f6e38238e720c1e.jpg)  
Fig. 1. An overview of the Bayesian network model for the Warfarin therapy management.

The maintenance phase of the therapy is managed through appointments at the hospital. In each appointment, a patient's INR value is measured. If the INR value is outside the patient's therapeutic range, possible variation factors that may cause this change are investigated. Finally, the dose prescription is changed if necessary, and the date of the follow-up meeting is scheduled. A typical appointment at the hospital is illustrated with a patient who is treated with a therapeutic range of 2 to 3. This patient's previous and second previous INR measurements were 2.4 and 2.1, both in the therapeutic range. The patient had an unexpectedly high INR value of 3.6 at his current appointment. The nurse treating the patient will investigate the presence of variation factors that may have caused this unexpected increase. The nurse may decrease the dose to bring the patient's INR to the therapeutic range, and may schedule a sooner follow-up to observe the effects of decreased dose.

In the following subsections, the steps of building the structure of the BN model are described. A simpli<sup>fi</sup>ed version of the model for the dose adjustment and follow-up interval decisions can be seen in Fig. 1. Variables and relations for this part of the model are explained in Section 3.2.1. The rectangular nodes in Fig. 1 are aggregated sub-models of the variation factors and treatment risks which are explained in Sections 3.2.2 and 3.2.3 respectively.

## 3.2.1. Dose adjustment and follow-up interval decisions

The dose adjustment and follow-up interval decisions for the therapy's maintenance phase are made by the nurses at SkaS. The variables, their states and relations related to these decisions were identi<sup>fi</sup>ed by interviews with these nurses.

Current INR value (‘INR’), patient's age (‘Age’) and previously prescribed Warfarin dose (‘Previous Dose’) have been identi<sup>fi</sup>ed as the main variables related to dose adjustment decisions. Ten states were de<sup>fi</sup>ned for the ‘INR’ variable according to the relevant risks.

The ‘Age’ variable has 4 states that are mainly for stratifying older patients. The ‘Previous Dose’ variable has 5 states that indicates the number of 2.5 mg Warfarin pills per week prescribed to the patient at the last follow-up meeting. These variables are identi<sup>fi</sup>ed as the parent of the ‘Dose Change’ variable that shows the percentage of recommended dose change. Twelve states were de<sup>fi</sup>ned for this variable that are a percentage of decrease (D) or increase (I) in the dose, no change in the dose or a pause in the treatment (Table 2).

INR stability is considered as the main factor for determining the length of follow-up intervals since patients with frequent INR changes are subject to higher risks. Consequently, current INR value (‘INR’), patient's age (‘Age’) as well as INR values in previous $\bf ( \ddot { \Phi } \mathrm { I N R } _ { t - 1 } \dot { \Phi } )$ and second previous (‘INR ’) follow-up meetings are identi<sup>fi</sup>ed as the parents of ‘Follow-up Interval’ variable which shows the time until the next INR measurement. Six states were determined for this variable which are in accordance with the practice of the nurses at SkaS. Fig. 1 shows the part of the BN model's structure covering dose-adjustment and follow-up interval decisions. The two rectangular nodes in Fig. 1 stand for the variation factors and bleeding/stroke risk sub-models that are described in Sections 3.2.2 and 3.2.3 respectively.

Selected variables in dose adjustment and follow-up interval decisions.

<table><tr><td>Variables</td><td>States</td></tr><tr><td>Age</td><td>{age&lt;70, 70≤age&lt;75, 75≤age&lt;80, 80≤age}</td></tr><tr><td>INR, INRt-1, INRt-2</td><td>{INR&lt;1.5, 1.5≤INR&lt;1.8, 1.8≤INR&lt;2, 2≤INR&lt;3, 3≤INR&lt;3.2, 3.2≤INR&lt;3.5, 3.5≤INR&lt;4, 4≤INR&lt;5, 5≤INR&lt;8, 8≤INR}</td></tr><tr><td>Previous dose (PD) in 2.5 mg pills/week</td><td>{0≤PD&lt;5, 5≤PD&lt;10, 10≤PD&lt;15, 15≤PD&lt;20, 20≤PD}</td></tr><tr><td rowspan="5">Dose change (DC) in %</td><td>{I(20≤DC),I(15≤DC&lt;20),I(10≤DC&lt;15), I(5≤DC&lt;10),I(0≤DC&lt;5),no change,D(0</td></tr><tr><td>D(5</td></tr><tr><td>D(10</td></tr><tr><td>D(15</td></tr><tr><td>D(20</td></tr><tr><td>Follow-up interval</td><td>{in 2 to 4 days, in 1 week, in 2 weeks, in 4 weeks, in 6 weeks, in more than 6 weeks}</td></tr></table>

Table 3 Selected variables in variation factors.

<table><tr><td>Variables</td><td>States</td></tr><tr><td>Non-adherence to prescription</td><td>{yes, no}</td></tr><tr><td>Vitamin K</td><td>{yes, no}</td></tr><tr><td>Alcohol consumption</td><td>{yes, no}</td></tr><tr><td>Cancer</td><td>{yes, no}</td></tr><tr><td>Liver disease</td><td>{yes, no}</td></tr><tr><td>Infection</td><td>{yes, no}</td></tr><tr><td>Thyroid dysfunction</td><td>{hyperthyroidism,hypothyroidism, none}</td></tr><tr><td>Drugs (heracillin, tegretol, alvedon, fenantoin,ciproxin, bactrim, tiparol, azatioprin, zolpidem,tamoxifen, lexinor, cordarone, flagyl, diflucan)</td><td>{yes, no}</td></tr></table>

## 3.2.2. Analysis of variation factors in Warfarin therapy

There are numerous factors that can cause variation in a patient's INR value [5,8,12,13,16]. Twenty one of these factors are included in the BN model following the domain experts' recommendations (Table 3). The parameters about the strength of relations between the variation factors and the INR were elicited from the experts since the amount of data available was inadequate to learn the parameters from the data.

The number of parameters in a CPT grows exponentially; if all 21 of these variables are linked as parents to the INR variable in the BN, the CPT of this variable requires over one million parameters. As a result, elicitation becomes infeasible. To solve this problem, two simpli<sup>fi</sup>cation approaches were used.

The <sup>fi</sup>rst simpli<sup>fi</sup>cation is to reduce the size of the CPT by adding extra nodes between a group of parents and the child node. Two variables that summarize the effects of drug (‘Drug Effects’) and disease interactions (‘Concomitant Diseases’) were added to the Warfarin model, so that the number of parents to ‘INR’ node was decreased from 21 to 5. This technique is known as ‘parent divorcing’ [18].

The variable ‘Drug Effects’ represents an increase or a decrease in the INR value caused by a drug interaction. The domain experts selected 14 drugs for the model which interact with Warfarin and are likely to be encountered at SkaS. There are many other drugs that interact with Warfarin as well [13].

The variable ‘Concomitant Diseases’ represents a variation in the INR value due to certain diseases. The diseases included in the model were based on domain knowledge and Demirkan et al.'s study [5]. The BN fragment about variation factors is shown in Fig. 2.

In spite of using ‘parent divorcing’, the number of probabilities still makes elicitation infeasible. For example, more than 30000 parameters need to be elicited for the CPT of the ‘Drug Effects’ node. The Noisy-OR/MAX gate models were used to overcome this problem. The Noisy-OR gate model assumes that parents of a common child act independently on it and at least the presence of one of the parents is required for affecting the child [6]. This assumption reduces the number of parameters that need to be identi<sup>fi</sup>ed from 2<sup>n</sup> to n in a binary model, since only the direct in<sup>fl</sup>uence of each parent is required to be identi<sup>fi</sup>ed. Noisy-MAX gate model is the generalization of the Noisy-OR gate for n-ary variables. A noisy-MAX gate model was applied to the ‘INR’, ‘Drug Effects’ and ‘Concomitant Diseases’ nodes. The domain experts agreed to the assumption of independent effects for these nodes. The number of probabilities that needed to be elicited for the ‘INR’ node decreased from 648 to 99, for the ‘Drug Effects’ node it was decreased from 32768 to 30, and for the ‘Concomitant Diseases' node it was decreased from 48 to 14.

## 3.2.3. Evaluation of cerebral bleeding risk and stroke risk in Warfarin therapy

The variables and relations for the part of the model about cerebral bleeding and stroke risk were derived from the medical literature [9,32]. States of the variables are shown in Table 4. The risk of cerebral bleeding increases as the INR value increases [7,14]. On the other hand, the risk of stroke increases if a patient's INR value decreases [15]. Therefore, variable ‘INR’ was determined as one of the modi<sup>fi</sup>ers of ‘Cerebral Bleeding Risk’ and ‘Stroke Risk’ variables.

Apart from INR value, there are several other risk factors which can increase the risk of bleeding even if the patient's INR is stable [3,32]. Shireman et al. [32] have developed a model to evaluate the bleeding risk of stable Warfarin patients. Following this model, the variables ‘Age’, ‘Gender’, ‘Presence of Recent Bleeding’, ‘Presence of Historical Bleeding’, ‘Alcohol or Drug Abuse’, ‘Diabetes’, ‘Antiplatelet Drugs’ and ‘Anemia’ were added to the BN. The ‘Bleeding Risk Index’ variable classi<sup>fi</sup>es the patients as having low, medium or high bleeding risk.

![](/api/attachments/YJ9WVXYD/fulltext/images/50f9b6f75b98b576c4a3d47351482d553d8b33cce9e7171bb7e3033b93db0f68.jpg)  
Fig. 2. Bayesian network sub-model about the variation factors.

Table 4  
Selected variables in bleeding and stroke risk.

<table><tr><td>Variables</td><td>States</td><td>Variables</td><td>States</td></tr><tr><td>Cerebral bleeding risk</td><td>{yes, no}</td><td>Presence of historical bleeding</td><td>{yes, no}</td></tr><tr><td>Stroke risk</td><td>{yes, no}</td><td>Alcohol or drug abuse</td><td>{yes, no}</td></tr><tr><td>Bleeding risk index</td><td>{low, medium, high}</td><td>Diabetes</td><td>{yes, no}</td></tr><tr><td>CHADS2 score</td><td>{0,1,2,34,5,6}</td><td>Anemia</td><td>{yes, no}</td></tr><tr><td>Age</td><td>{age&lt;70, 70≤age&lt;75, 75≤age&lt;80, 80≤age}</td><td>Congestive heart failure</td><td>{yes, no}</td></tr><tr><td>Gender</td><td>{male, female}</td><td>Hypertension</td><td>{yes, no}</td></tr><tr><td>Presence of recent bleeding</td><td>{yes, no}</td><td>Transient ischemic attack (TIA) or previous stroke</td><td>{yes, no}</td></tr><tr><td>Antiplatelet drugs</td><td>{yes, no}</td><td></td><td></td></tr></table>

The stroke risk of a stable patient is calculated by Gage et al.'s model named ‘CHADS ’ [9]. This model calculates a stroke risk score between 0 and 6 based on several risk factors. In accordance with the model, ‘Diabetes’, ‘Congestive Heart Failure’, ‘Hypertension’, ‘TIA’, ‘CHADS Score’ variables were added to the BN. The bleeding risk [32] and CHADS [9] models were implemented since these models were recognized and used by the domain experts at SkaS. The BN sub-model about bleeding and stroke risks is shown in Fig. 3. The nodes ‘Age’ and ‘INR’ are represented by a rectangular shape in Fig. 3 as these nodes are shared with the main model shown in Fig. 1.

## 3.3. Parameters of the model

The probabilities for the model parameters were learned from data (Section 3.3.1), elicited from domain experts (Section 3.3.2), and gathered from statistics in medical literature (Section 3.3.2).

## 3.3.1. Learning from data

SkaS has large amount of data that record the clinical information of Warfarin patients and their INR measurements at each hospital meeting. A sample of the data recorded at hospital appointments can be seen in Table 5.

The CPTs of dose adjustment and follow-up interval sub models, and unconditional probabilities for patient's age, gender, concomitant diseases and drugs were learned from the data. On the other hand, the CPT of ‘INR’ could not be learned from the data since there were no records of the times when the patients were suffering from the concomitant diseases or were using the drugs that interact with Warfarin. In other words, although the patients’ disease and drug history were known, the presence of these diseases and drugs were not recorded at each meeting. The parameters that were learned from the data can be seen in Table 6.

Our data had information about 4652 patients and 63249 hospital meetings in 2009. Before learning the probabilities, the data was analyzed and preprocessed in order to exclude the parts that are not clinically relevant or reliable [30]. The main steps of data preprocessing can be seen in Fig. 4.

First of all, the data contained information about patients with various therapeutic ranges. Therapeutic range is the range of values that a patient's INR value is aimed to be kept in. The optimal therapeutic range for the majority of Warfarin patients is 2 to 3 [1,8,27]. The aim of the therapy is to keep the INR value higher than 2 and lower than 3 for these patients. On the other hand, Warfarin is used for treating several diseases, and some of these diseases are treated with different therapeutic ranges. Since reasoning and decisionmaking about patients with different therapeutic ranges can be quite different; the BN was developed only for the patients with therapeutic range of 2 to 3. We therefore excluded the patients with other therapeutic ranges which left 57,296 remaining appointment records.

Second, our model aims to manage the Warfarin therapy for the patients that have been receiving the therapy for more than 14 days. Therefore, the records about the patients that are in the <sup>fi</sup>rst 14 days of their Warfarin therapy are excluded from the learning data which left 53,503 remaining records. The records that had no other values but patient identi<sup>fi</sup>cation number were also excluded as were duplicate records leaving 48,872 records. Finally, some extreme situations in the data, such as 400 days intervals between two INR measurements, were analyzed with the domain experts and removed from the data, which led to a <sup>fi</sup>nal count of 48,666 patient records.

After the data were re<sup>fi</sup>ned, the expectation maximization (EM) algorithm [17] was used to learn the CPTs for dose-adjustment and follow-up interval sub-models. The EM algorithm is a two-step algorithm that is capable of coping with incomplete data. In the <sup>fi</sup>rst step, the algorithm calculates expected values for the missing values and completes the data. In the second step, it <sup>fi</sup>nds a maximum likelihood estimate for the parameters. The steps continue iteratively until the algorithm converges.

![](/api/attachments/YJ9WVXYD/fulltext/images/f01b6d07640b94ace07062ff5e9f0e54dd297bb9863d5125c588d255b420bc56.jpg)  
Fig. 3. Bayesian network sub-model about the cerebral bleeding and stroke risks.

Table 6  
Table 5 Sample of Warfarin data

<table><tr><td>Patient ID</td><td>Gender</td><td>Age</td><td>Therapy start</td><td>Appointment date</td><td>Therapeutic range</td><td>Weekly dose (pills)</td><td>Follow-up (days)</td><td>INR</td></tr><tr><td>3</td><td>F</td><td>85</td><td>3.1.09</td><td>30.03.09</td><td>2.0–3.0</td><td>4.5</td><td>7</td><td>2.4</td></tr><tr><td>3</td><td>F</td><td>85</td><td>3.1.09</td><td>06.04.09</td><td>2.0–3.0</td><td>4.5</td><td></td><td>2.5</td></tr><tr><td>4</td><td>M</td><td>98</td><td>30.3.09</td><td>07.10.09</td><td>2.0–3.0</td><td>10</td><td>28</td><td>2.8</td></tr><tr><td>4</td><td>M</td><td>98</td><td>30.3.09</td><td>04.11.09</td><td>2.0–3.0</td><td>10</td><td>23</td><td>3.1</td></tr><tr><td>4</td><td>M</td><td>98</td><td>30.3.09</td><td>27.11.09</td><td>2.0–3.0</td><td>7</td><td>3</td><td>1.9</td></tr><tr><td>4</td><td>M</td><td>98</td><td>30.3.09</td><td>30.11.09</td><td>2.0–3.0</td><td>10</td><td>7</td><td>2.3</td></tr><tr><td>4</td><td>M</td><td>98</td><td>30.3.09</td><td>07.12.09</td><td>2.0–3.0</td><td>10</td><td></td><td>2.8</td></tr><tr><td>5</td><td>F</td><td>52</td><td>31.1.03</td><td>25.08.09</td><td>2.0–3.0</td><td>9.5</td><td>28</td><td>2.4</td></tr><tr><td>5</td><td>F</td><td>52</td><td>31.1.03</td><td>22.09.09</td><td>2.0–3.0</td><td>9.5</td><td>28</td><td>2.2</td></tr><tr><td>5</td><td>F</td><td>52</td><td>31.1.03</td><td>20.10.09</td><td>2.0–3.0</td><td>9.5</td><td>30</td><td>2.3</td></tr></table>

## 3.3.2. Expert elicitation

Data about the in<sup>fl</sup>uence of variation factors on INR and several unconditional probabilities, such as vitamin K intake, were not available. On the other hand, several clinicians at SkaS had extensive experience of Warfarin treatment. The unconditional probabilities and CPTs for several variables were elicited from those domain experts. These variables can be seen in Table 6.

Two methods were used for probability elicitation. The <sup>fi</sup>rst of these methods is a linear probability scale with both verbal and numerical anchors [37]. This method was used and found effective for eliciting the conditional probabilities from physicians to build a BN [37]. Verbal anchors in this method are provided as physicians tend to express the probabilities in verbal rather than numerical form [19]. Numerical anchors are also provided for the situations in which the expert is more comfortable with numerical expression of probabilities (Fig. 5).

The parameters of some unconditional probabilities were very low in our case, and linear probability scales are not suitable for elicitation of such low probabilities [29]. For these variables, we used a second method, which was to ask the expert to imagine 1000 Warfarin patients, and express the likelihood of the elicited parameter among these patients.

Parameter elicitation was conducted with the fourth author, who is a physician and the manager of Warfarin process improvement group at SkaS. Before the <sup>fi</sup>rst elicitation session, a short tutorial about the elicitation methods and biases was given to the expert. In this tutorial, the risk of overcon<sup>fi</sup>dence, availability, control, anchoring and adjustment biases were explained with examples. Information about these biases can be found in [29]. After the tutorial, a clear measurement scale was determined for each variable. The expert was informed that he could change his previous answers and he should tell the elicitors whenever he is not comfortable with the question structure or the elicitation method. During the elicitation, several questions were restructured with the experts. For example, the domain expert asked for a solid example of non-adherence while answering a question about the patients' adherence to prescription. Consequently, a typical non-adherence situation encountered at the hospital was added to the question statement.

Knowledge source of the model's parameters.

<table><tr><td>Knowledge Source</td><td>Parameters</td></tr><tr><td>Data</td><td>Age, alcohol or drug abuse, alvedon, anemia, antiplatelet drugs, azatioprin, bactrim, cancer, ciproxin, congestive heart failure, cordarone, diabetes, diflucan, dose change, fenantoin, flagyl, follow-up interval, heracillin, hypertension, infection, INR (prior), INRt-1, INRt-2, lexinor, liver disease, previous dose, stroke or TIA, thyroid dysfunction, tiparol, tamoxifen, tegretol, zolpidem.</td></tr><tr><td>Experts</td><td>Alcohol consumption, concomitant diseases, drug effects, historical bleeding, INR (conditional), non-adherence to prescription, recent bleeding, vitamin K.</td></tr><tr><td>Literature</td><td>Bleeding risk index, cerebral bleeding risk, CHADS2 score, stroke risk.</td></tr></table>

Probability scale was used comfortably by the expert. On the other hand, the expert had some concerns in terms of expressing the unconditional probabilities in numbers. For example, the expert felt uncomfortable about the accuracy of his answer to a question like: ‘Imagine 1000 Warfarin using patients, how many of them drink two glasses of wine (or equivalent amount of alcohol) one week before the

![](/api/attachments/YJ9WVXYD/fulltext/images/ec993c61d403d65a5b988b49cb6aa7a3e2ab2f8ca53a8e07012aeaaad964aa20.jpg)  
Fig. 4. Preprocessing of the Data.

![](/api/attachments/YJ9WVXYD/fulltext/images/7f107936361fb992ce30747d8633e09e20deba14b59886f7f824f2900a31b4d8.jpg)

## INR Alcohol Consumption

1) Consider a warfarin patient that drank two glasses of wine or equal amount of alcohol in previous week (and no other variation cause is present). How likely is it that this patient will have INR value more than 8.0?

Fig. 5. Example question of probability elicitation with verbal and numerical anchors.

INR measurement?’. Consequently, elicitors explained to the expert that his answers should re<sup>fl</sup>ect his beliefs and experiences rather than being precise answers.

The probability elicitation techniques used in this study have several disadvantages in terms of biases and errors compared to the indirect elicitation techniques such as the use of reference lotteries [18]. On the other hand, the quality and robustness of the directly elicited probabilities can be improved by conducting sensitivity analysis [4]. The indirect techniques were considered impracticable for this study since they require more time, and medical experts would need extensive training to be comfortable with these techniques [37].

One-way sensitivity analysis was used to re<sup>fi</sup>ne the elicited probabilities. In this technique, the parameters of each variable are varied one-by-one and the sensitivity of a target variable is observed. The sensitivity of the ‘INR’, ‘Dose Change’ and ‘Follow-up Intervals’ parameters to other elicited variables were plotted. These plots were shown to the expert, and the parameters were modi<sup>fi</sup>ed if they were found over or under sensitive by the expert. Two examples of these plots are shown in Fig. 6. New plots were prepared and discussed after each modi<sup>fi</sup>cation, and the process continued until the model behavior was found to be satisfactory by the expert. Two-way sensitivity analysis was not conducted since the elicited parameters are in a Noisy-OR model so that each acts independently of the others.

## 3.3.3. Probabilities from published medical literature

The bleeding and stroke risk evaluation sub-models are based on Shireman et al.'s bleeding risk model [32] and CHADS model [9] respectively (see Section 3.2.3). In both Shireman et al. [32] and Gage et al.'s study [9], the bleeding and stroke risks according to their models are presented. These risks were used for the CPTs of the risk sub-models.

INR value's effect on the bleeding and stroke risk needs to be integrated to the model as well. Parameters for this part are gathered from [15], which presents the odds ratios of stroke according to different INR values, and [7], which presents the odds ratios of cerebral bleeding risk with INR values. The parameters gathered from published sources are summarized in Table 6.

It should be noted that only patients with atrial <sup>fi</sup>brillation were studied in [7,9,15,32], therefore bleeding and stroke risk sub-models should be considered accurate for these patients. Moreover, the data used in these studies were gathered mainly from the hospitals in the United States. On the other hand, the bleeding and stroke risk parts of the model were still considered to be useful by the domain experts since a similar study focusing on Swedish patients could not be found, and more than 70% of the patients that uses Warfarin are suffering from atrial <sup>fi</sup>brillation at SkaS.

## 4. Model veri<sup>fi</sup>cation and validation

Two methods were used to validate the Warfarin therapy management model. The first of these methods was 10-fold cross validation [18]. This method was used to validate the parts of the model that have been learned from the data. In a 10-fold cross validation, the data are divided into 10 equal sized subsamples. One of these subsamples is spared for validation and the remaining 9 subsamples are used for training the data. This process is repeated 10 times until each of the subsamples is used for validating the data and then results are averaged to give a performance estimate. This method was used to test whether the most probable dose adjustment and follow-up interval outputs of the model are similar to the decisions taken by physicians in the past cases and recorded in the data.

![](/api/attachments/YJ9WVXYD/fulltext/images/c0b1d319ace2ff9d1c9c12c80d567712f931c7b698e6c95e7b9b2012b4857c26.jpg)

![](/api/attachments/YJ9WVXYD/fulltext/images/1b5616cc5661b5cbdce67a0d30a8bb7311f6a39e82f4c39777a2a6f7dd6151c9.jpg)  
Fig. 6. Example of the plots used for sensitivity analysis.

Table 7  
Percentage of actual dose adjustment and follow-up intervals predicted by the 1, 2 and 3 most probable model states.

<table><tr><td>Probable states</td><td>Dose adjustment</td><td>Follow-up interval</td></tr><tr><td>Most probable</td><td>75%</td><td>46%</td></tr><tr><td>2 Most probable</td><td>84%</td><td>79%</td></tr><tr><td>3 Most probable</td><td>92%</td><td>92%</td></tr></table>

Table 8  
Observed variables in the example application of the model.

<table><tr><td>Variables</td><td>States</td><td>Variables</td><td>States</td></tr><tr><td>Age</td><td>84</td><td>Hypertension</td><td>yes</td></tr><tr><td>Gender</td><td>Male</td><td>Previous dose (pills)</td><td>12</td></tr><tr><td>INR</td><td>3.6</td><td>Alcohol or drug abuse</td><td>no</td></tr><tr><td> $INR_{t-1}$ </td><td>2.4</td><td>Diabetes</td><td>no</td></tr><tr><td> $INR_{t-2}$ </td><td>2.1</td><td>Congestive heart failure</td><td>no</td></tr></table>

In over 75% of the cases, the actual dose adjustment decision was the model's most probable output, and it was one of the two most probable outputs of the model in 84% of the cases. For follow-up intervals, the actual decision was the same with the most probable output in 46% of the cases, and it was one of the two most probable outputs in 79% of the cases. The model's recommendations were skewed towards shorter follow-up intervals, especially if the follow-up interval decision is more than 4 weeks. The results are shown in Table 7.

The elicited parts of the model were validated by case-based evaluation. Thirty cases with random instantiations of INR and several variation factors were generated. The main aim of this part of the model was to investigate which variation factors may have caused an INR <sup>fl</sup>uctuation. The domain experts reviewed the posterior probability distribution of the non-instantiated variation factors, and they were satis<sup>fi</sup>ed with the shown distributions in 83% of the cases. Their main disagreements to the model were in the cases where INR value was instantiated slightly over the therapeutic range. It was explained that even if none of the variations factors is present, a minor change in INR value can occur for an unknown reason. With the exception of this point, the majority of the diagnostic inferences regarding variation factors were found to be consistent with their practical experience.

## 5. Application of the Bayesian network model

In this section, an example application of the BN model is presented. The description of the example and the model's outputs are presented in Sections 5.1 and 5.2 respectively.

## 5.1. Description of the example

An 84 year old male patient is in the maintenance phase of Warfarin therapy and his therapeutic INR range is 2 to 3. A nurse at SkaS measures the current INR value of the patient as 3.6, which is above the upper bound of the therapeutic range. The patient was prescribed with 12 Warfarin 2.5 mg pills per week. His two previous INR measurements are 2.4 and 2.1, both of which are in the therapeutic range. The nurse checks the patient's records to gather information about his medical history and Warfarin therapy. The information is entered as inputs to the BN model (Table 8). More inputs can be entered and the model's outputs can be recalculated if the nurse gathers additional information during the meeting.

![](/api/attachments/YJ9WVXYD/fulltext/images/5fc7f9603a8723598514cc2f5f8f7cccc1554112ef893295bc4d2d12fe613c3b.jpg)  
Fig. 7. Updated Bayesian network with instantiated variables on dose adjustment and follow-up interval decisions.

Table 9  
The most probable sources of variation for the patient with an INR of 3.6 without having any information about variation factors.

<table><tr><td>Variation factors</td><td>Probability</td></tr><tr><td>Alcohol consumption</td><td>52%</td></tr><tr><td>Alvedon</td><td>26%</td></tr><tr><td>Tiparol</td><td>8%</td></tr></table>

Table 10  
The most probable sources of variation for the patient with an INR of 3.6 after ‘alcohol consumption’ is instantiated.

<table><tr><td>Variation Factors</td><td>Probability</td></tr><tr><td>Alvedon</td><td>42%</td></tr><tr><td>Tiparol</td><td>12%</td></tr><tr><td>Infection</td><td>9%</td></tr></table>

## 5.2. Bayesian network model's outputs

## 5.2.1. Dose adjustment and follow-up interval decisions

Fig. 7 shows the model's outputs of dose adjustment and follow-up interval decisions. The variables ‘INR’, $\mathrm { ^ { * } I N R _ { t - 1 } } \mathrm { ^ { * } , \mathrm { ^ { * } I N R _ { t - 2 } } } \mathrm { ^ { * } , }$ , ‘Age’ and ‘Previous Dose’ are instantiated as the nurse gathers the relevant information about those variables. The model provides its outputs as probability distributions. The most probable states are a 5 to 10 percent decrease in the previous dose (with 41% probability) and a follow-up meeting in 2 weeks (with 50% probability). The second most probable states are 0 to 5 percent decrease (with 20% probability) in the previous dose and a follow-up meeting in 1 week (with 30% probability). The probabilities for the recommendations represent the frequency of decisions given in a similar context by the experts, since the parameters of ‘Dose Change’ and ‘Follow-up Interval’ node are learned from the data that contains the previous decisions of the domain experts. The outputs of the model can assist the nurse in making these decisions.

## 5.2.2. Analysis of variation factors in Warfarin therapy

This part of the model outputs the most probable causes of variation in the patient's INR value. As the current INR value of the patient is 3.6, the nurse wants to know about the causes of this high INR value. The current INR value is instantiated, and the alcohol consumption (with 52% probability) is found to be the most probable source of variation (Table 9). The nurse can ask the patient whether he had consumed alcohol before his INR test. If the patient says that he has not consumed alcohol in the previous week, the nurse can update the model by instantiating the variable ‘alcohol consumption’ as ‘No’. The model recalculates the probabilities with the new information; it diagnoses drug effect as the most probable source of variation, and Alvedon (with probability of 41%) as the most probable kind of drug that may have been used (Table 10). The nurse can continue to investigate the variation factors according to the most probable outputs of the model and update the model with instantiations until the true cause of variation is found. If the factor that caused the variation is found, the nurse can take preventive actions to keep the patient's INR value stable.

5.2.3. Evaluation of cerebral bleeding risk and stroke risk in Warfarin therapy

The model's prediction of cerebral bleeding and stroke risks is presented in Fig. 8. In this part of the model, the variables ‘Age’, ‘Gender’, ‘Diabetes’, ‘INR’, ‘Congestive Heart Failure’ and ‘Hypertension’ are instantiated according to the medical information about the patient. The model <sup>fi</sup>nds the risks of cerebral bleeding as 4% and stroke as 6%. This cerebral bleeding risk is almost four times higher than the risk of a stable Warfarin patient since the patient's INR range is over the therapeutic range. The stroke risk is also relatively high due to the presence of risk factors such as hypertension and older age. These estimated risks are used to review the dose adjustment and follow-up decisions.

## 6. Discussion

Bayesian networks provide a great deal of <sup>fl</sup>exibility in terms of their inputs and outputs, since any set of variables can be instantiated and the posterior distributions of the remaining variables in the BN are updated. Here, the BN can be used to reason diagnostically when some of the variation factors are unknown, taking account of those that are known. This <sup>fl</sup>exibility contrasts with the regression and rule-based models, which require all of their inputs about variation factors to be entered.

The results of the BN are probability distributions showing the model's con<sup>fi</sup>dence in the recommendation, which is the most probable state. For example, if the model calculates probability distribution of ‘Dose Change’ as 5% dose increase with 51% probability and 10% dose increase with 49% probability, it can be considered that the model recommends both changes with similar con<sup>fi</sup>dence. On the other hand, if the model calculates the probability of 5% dose increase as 99%, then the con<sup>fi</sup>dence in the recommendation is higher.

![](/api/attachments/YJ9WVXYD/fulltext/images/55bbcb237d9be8e7551fc3043522294dfcff47c310abfc220020e8c55cd78a68.jpg)  
Fig. 8. Updated Bayesian network with instantiated variables on cerebral bleeding and stroke risk evaluation.

This is especially useful when there is a discrepancy between the model's recommendation and the user's opinion. The user can evaluate the model's con<sup>fi</sup>dence in its recommendations and consider the second and third most probable states. In rule-based or regression models, on the other hand, the outputs are single dose estimates.

The diagnostic inference about the variation factors is useful for investigating the possible causes of unexpectedly high or low INR values. These inferences can assist the clinician as a guideline for patient interviews. By using the model, the clinician can start investigating the most probable cause according to the given situation. This can speed up the investigating process by decreasing the number of questions asked about very rare events which can be do not occur in most of the situations. Increasing the ef<sup>fi</sup>ciency of computer assisted interviews is important [2], and BN have potential bene<sup>fi</sup>ts in this area.

The BN model's structure and parameters are built using published medical <sup>fi</sup>ndings, expert knowledge, and large dataset from the hospital. The model therefore represents both domain knowledge and the hospital's practice. It can be used as a training instrument for the clinicians who are new to the Warfarin therapy. It is possible to show different scenarios and analyze causal relations such as the relations between bleeding risk and INR for the training of clinicians. Moreover, the model can also be used to analyze the current practice in Warfarin therapy management. Its structure and parameters can be modi<sup>fi</sup>ed to adapt the further changes in the practice [23].

There are several limitations to the model which could be addressed in a further work. First, the BN model has been built for the patients that have target therapeutic range of 2 to 3 in the maintenance phase of the therapy. Furthermore, the parameters of the bleeding risk and stroke sub-models are based on the statistics about atrial <sup>fi</sup>brillation patients. Although a model with these limitations can be used for the majority of the patients under Warfarin treatment, they prevent the model from being used for all of them.

Second, the probability elicitation process for parameters was carried out with a single expert. Although, the expert is an experienced physician who is actively involved in Warfarin therapy, eliciting with more experts can be helpful in reducing the bias and errors [30].

## 7. Conclusion

The aim of the work described here is to propose a DSS using BNs for assisting clinicians in managing Warfarin therapy. The BN model is built upon the medical literature, the data and the knowledge of domain experts from a Swedish hospital. The model is capable of recommending dose adjustment and follow-up interval decisions. Unlike most of other DSS utilized in the Warfarin therapy, the BN model also assists investigation of the factors that may cause variation in INR and evaluates the cerebral bleeding and stroke risks related to the therapy.

In order to validate the dose adjustment and follow-up interval decisions of the model, 10-fold cross validation method was used. It was found that the actual dose adjustment and follow-up interval decision was one of the two most probable outputs of the model in 84% and 79% of the cases respectively. The BN model's performance in investigating possible variation factors was tested with the experts, as there was no data available for this validation. Out of the 30 cases generated for this test, the experts agreed with the model in 83% of the cases. The part of the model used to estimate the cerebral bleeding and stroke risks is built upon the validated statistics in the medical literature; however, since no data about bleeding and stroke incidences were available, no additional validation was possible for this part of the model.

For further research, this model could be expanded to manage all of the Warfarin therapy including both the initiation phase and the maintenance phase. Moreover, it could be adapted to manage other target therapeutic ranges such as 2.5 to 3.5. More conclusive statements about the model's reliability could be made if the model were validated prospectively. Finally, the model's user interface can be simpli<sup>fi</sup>ed to make it easier to use and update by the clinicians.

## Acknowledgments

This research is supported by a funding from the Kristina Stenborgs foundation through the Centre for Healthcare Improvement at Chalmers University of Technology. The authors also acknowledge the constructive comments of the reviewers and the invaluable support from the project group at Skaraborg Hospital Group, SkaS.

## References

[1] J. Ansell, J. Hirsh, J. Dalen, H. Bussey, D. Anderson, L. Poller, A. Jacobson, D. Deykin, D. Matchar, Managing oral anticoagulant therapy, Chest 119 (2001) 22S–38S

[2] J.W. Bachman, The patient–computer interview: a neglected tool that can aid the clinician, Mayo Clinic Proceedings 78 (2003) 67–78.

[3] R.J. Beyth, L.M. Quinn, C.S. Landefeld, Prospective evaluation of an index for predicting the risk of major bleeding in outpatients treated with Warfarin, The American Journal of Medicine 105 (1998) 91–99.

[4] V.H.M. Coupe, L.C. van der Gaag, J.D.F. Habbema, Sensitivity analysis: an aid for belief network quanti<sup>fi</sup>cation, Knowledge Engineering Review 15 (2000) 1–18.

[5] K. Demirkan, M.A. Stephens, K.P. Newman, T.H. Self, Response to Warfarin and other oral anticoagulants: effects of disease states, Southern Medical Journal 93 (2000) 448–454.

[6] J.D. Díez, M.J. Druzdzel, Canonical probabilistic models for knowledge engineering, Technical Report, CISIAD-06-01, UNED, Spain, 2006.

[7] M.C. Fang, Y. Chang, E.M. Hylek, J. Rosand, S.M. Greenberg, A.S. Go, D.E. Singer, Advanced age, anticoagulation intensity, and risk for intracranial hemorrhage among patients taking Warfarin for atrial <sup>fi</sup>brillation, Annals of Internal Medicine 141 (2004) 745–752.

[8] B.F. Gage, S.D. Fihn, R.H. White, Management and dosing of Warfarin therapy, The American Journal of Medicine 109 (2000) 481–488.

[9] B.F. Gage, A.D. Waterman, W. Shannon, M. Boechler, M.W. Rich, M.J. Radford, Validation of clinical classi<sup>fi</sup>cation schemes for predicting stroke: results from the National Registry of Atrial Fibrillation, JAMA : The Journal of the American Medical Association 285 (2001) 2864–2870.

[10] A.X. Garg, N.K. Adhikari, H. McDonald, M.P. Rosas-Arellano, P.J. Devereaux, J. Beyene, J. Sam, R.B. Haynes, Effects of computerized clinical decision support systems on practitioner performance and patient outcomes: a systematic review, JAMA : The Journal of the American Medical Association 293 (2005) 1223–1238

[11] Genie-SMILE. Available at: http://genie.sis.pitt.edu/ [Accessed 29 November 2011].

[12] J. Hirsh, V. Fuster, J. Ansell, J.L. Halperin, American Heart Association/American College of Cardiology Foundation guide to Warfarin therapy, Journal of the American College of Cardiology 41 (2003) 1633–1652.

[13] A.M. Holbrook, J.A. Pereira, R. Labiris, H. McDonald, J.D. Douketis, M. Crowther, P.S. Wells. Systematic overview of Warfarin and its drug and food interactions. Archives of Internal Medicine 165 (2005) 1095–1106.

[14] E.M. Hylek, D.E. Singer, Risk factors for intracranial hemorrhage in outpatients taking Warfarin, Annals of Internal Medicine 120 (1994) 897–902.

[15] E.M. Hylek, S.J. Skates, M.A. Sheehan, D.E. Singer, An analysis of the lowest effective intensity of prophylactic anticoagulation for patients with nonrheumatic atrial fibrillation, The New England Journal of Medicine 335 (1996) 540–546

[16] A. Jaffer, L. Bragg, Practical tips for Warfarin dosing and monitoring, Cleveland Clinic Journal of Medicine 70 (2003) 361–371.

[17] D. Koller, N. Friedman, Probabilistic Graphical Models: Principles and Techniques, The MIT Press, Cambridge, 2009.

[18] K. Korb, A. Nicholson, Bayesian Arti<sup>fi</sup>cial Intelligence, Champman & Hall, London, 2004.

[19] B. Kuipers, A.J. Moskowitz, J.P. Kassirer, Critical decisions under uncertainty: Representation and structure, Cognitive Science 12 (1988) 177–210.

[20] H. Langeseth, T.D. Nielsen, R. Rumi, A. Salmeron, Inference in hybrid Bayesian networks, Reliability Engineering and System Safety 94 (10) (2009) 1499–1509.

[21] S.M. Lee, P.A. Abbott, Bayesian networks for knowledge discovery in large datasets: basics for nurse researchers, Journal of Biomedical Informatics 36 (2003).389-399

[22] P.J. Lucas, L.C. van der Gaag, A. Abu-Hanna, Bayesian networks in biomedicine and health-care, Artificial Intelligence in Medicine 30 (2004) 201-214

[23] I. Maglogiannis, E. Za<sup>fi</sup>ropoulos, A. Platis, C. Lambrinoudakis, Risk analysis of a patient monitoring system using Bayesian Network modeling, Journal of Biomedical Informatics 39 (2006) 637–647

[24] C. Manotti, M. Moia, G. Palareti, V. Pengo, L. Ria, A.G. Dettori, Effect of computeraided management on the quality of treatment in anticoagulated patients: a prospective, randomized, multicenter trial of APROAT (Automated PRogram for Oral Anticoagulant Treatment), Haematologica 86 (2001) 1060–1070.

[25] A. Margolis, F. Flores, M. Kierszenbaum, Z. Cavallo, B. Botti, E. D'Ottone, N. Tavella, J. Torres, Warfarin 2.0—a computer program for Warfarin management. Design and clinical use, Proceedings of the Annual Symposium on Computer Applications in Medical Care (1994) 846–850.

[26] M. Neil, M. Tailor, D. Marquez, Inference in Bayesian networks using dynamic discretisation, Statistics and Computing 17 (3) (2007) 219–233.

[27] A. Oden, M. Fahlen, Oral anticoagulation and risk of death: a medical record linkage study, BMJ 325 (2002) 1073–1075.

[28] L. Poller, M. Keown, S. Ibrahim, G. Lowe, M. Moia, A.G. Turpie, C. Roberts, A.M. van den Besselaar, F.J. van der Meer, A. Tripodi, G. Palareti, C. Shiach, S. Bryan, M. Samama, M. Burgess-Wilson, A. Heagerty, P. Maccallum, D. Wright, J. Jespersen, An international multicenter randomized study of computer-assisted oral anticoagulant dosage vs. medical staff dosage, Journal of Thrombosis and Haemostasis 6 (2008) 935–943.

[29] S. Renooij, Probability elicitation for belief networks: issues to consider, Knowledge Engineering Review 16 (2001) 255–269.

[30] H. Sagreiya, R.B. Altman, The utility of general purpose versus specialty clinical databases for research: Warfarin dose estimation from extracted clinical variables, Journal of Biomedical Informatics 43 (5) (2010) 747–751.

[31] H. Schelleman, J. Chen, J. Christie, C.W. Newcomb, C.M. Brensinger, M. Price, A.S. Whitehead, C. Kealey, C.F. Thorn, F.F. Samaha, S.E. Kimmel, Dosing Algorithms to Predict Warfarin Response in Caucasians and African Americans, Clin. Pharmacol. Ther. 84 (3) (2008) 332–339.

[32] T.I. Shireman, J.D. Mahnken, P.A. Howard, T.F. Kresowik, Q. Hou, E.F. Ellerbeck, Development of a contemporary bleeding risk model for elderly Warfarin recipients, Chest 130 (2006) 1390–1396.

[33] J.M. Svec, R.W. Coleman, D.R. Mungall, T.M. Ludden, Bayesian pharmacokinetic/ pharmacodynamic forecasting of prothrombin response to Warfarin therapy: preliminary evaluation, Therapeutic Drug Monitoring 7 (1985) 174–180.

[34] The Swedish National Board of Health and Welfare, An Overview of Patient Safety, 2004. (in Swedish).

[35] The Swedish National Board of Health and Welfare, Statistics – Health and Welfare, 2009. (in Swedish).

[36] B. Vadher, D.L. Patterson, M. Leaning, Evaluation of a decision support system for initiation and control of oral anticoagulation in a randomised trial, BMJ 314 (1997) 1252–1256.

[37] L.C. van der Gaag, S. Renooij, C.L. Witteman, B.M. Aleman, B.G. Taal, Probabilities for a probabilistic network: a case study in oesophageal cancer, Arti<sup>fi</sup>cial Intelli gence in Medicine 25 (2002) 123–148.

[38] M.A. van Gerven, B.G. Taal, P.J. Lucas, Dynamic Bayesian networks as prognostic models for clinical patient management, Journal of Biomedical Informatics 41 (2008) 515–529.

[39] M. Wadelius, L.Y. Chen, J.D. Lindh, N. Eriksson, M.J. Ghori, S. Bumpstead, L. Holm, R. McGinnis, A. Rane, P. Deloukas, The largest prospective Warfarin-treated cohort supports genetic forecasting, Blood 113 (2009) 784–792.

[40] H. Wiegman, A.M. Vossepoel, A computer program for long term anticoagulation control, Computer Programs in Biomedicine 7 (1977) 71–84.

[41] S.E. Wilson, L. Costantini, M.A. Crowther, Paper-based dosing algorithms for maintenance of Warfarin anticoagulation, Journal of Thrombosis and Thrombolysis 23 (2007) 195–198.

Barbaros Yet is a PhD candidate at the Risk Assessment and Decision Analysis research group in the School of Electronics Engineering and Computer Science, Queen Mary, University of London. He holds a M.S. degree in Quality and Operations Management from Chalmers University of Technology Sweden and a B.S. degree in Industrial Engineering from Middle East Technical University, Turkey. His research focuses on providing decision support in highly uncertain domains by developing probabilistic graphical models that integrates expert knowledge with statistical data

Kaveh Bastani received the B.S. degree in industrial engineering from Sharif University of Technology, Tehran, Iran, in 2008, and the M.S. degree in quality management from Chalmers University of Technology, Gothenburg, Sweden, in 2010. He is currently a Ph.D. student at the School of Industrial Engineering and Management, Oklahoma State University. His research focuses on the quality improvement for large and complex manufacturing systems through integrating the engineering knowledge of the processes and the statistical methods

Hendry Raharjo obtained his Joint-PhD degree from National University of Singapore and Eindhoven University of Technology. He is working as a senior researcher at Chalmers University of Technology. His research has been published in journals, such as European Journal of Operational Research, Expert Systems with Applications, Quality Engineering, International Journal of Production Research, Computers and Industrial Engineering, Quality and Reliability Engineering, and Total Quality Management and Business Excellence. He has been an active reviewer for more than 10 international journals.

Svante Lifvergren, M. D., works as development director at the Skaraborg Hospital Group (SkaS). He is a specialist in internal and pulmonary medicine and has worked as a senior physician at SkaS since 1998. He is a member of SkaS executive management team since 2006. He is also the executive manager for the Centre for Healthcare Improvement at Chalmers University of Technology since 2011 (www.chi.chalmers.se). Since 2011, he is also a member of the associate editorial board for Action Research Journal, Sage. Dr Lifvergren has published peer-reviewed articles on six-sigma and process management in healthcare. Moreover, he is the lead author of several chapters in different edited volumes, elaborating on sustainable healthcare systems as well coordinated care processes for elderly people with multiple diseases. Dr Lifvergren has been the process manager for the overall Warfarin process at SkaS since 2006.

William Marsh is a lecturer in the School of Electronics Engineering and Computer Science at Queen Mary University of London, where he is a member of the Risk Assessment and Decision Analysis research group. He holds a PhD in Computer Science from the University of Southampton. His research interests are in probabilistic modeling for risk assessment and decision support, with applications in medicine, systems and software engineering. He prefers to do research in collaboration with application experts.

Bo Bergman is SKF professor in Quality Sciences at Chalmers University of Technology since 1999. During 1969–1984 he worked as a reliability engineer, internal statistical consultant, and operations researcher in the aerospace industry. Concurrently, he became a PhD in Mathematical Statistics from the University of Lund. During 1983–1999 he was a professor of Quality Technology and Management at Linköping University, where he was responsible for the creation of education and research in the quality <sup>fi</sup>eld. Currently, his main research focus is on healthcare innovation and improvement. He is the author or co-author of over a hundred scienti<sup>fi</sup>c papers and a number of books.
