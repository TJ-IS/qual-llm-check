---
otero_id: 21189
otero_key: "D9UM9GWK"
title: "Mobile clinical support system for pediatric emergencies"
authors: "Wojtek Michalowski; Steven Rubin; Roman Slowinski; Szymon Wilk"
year: "2003"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(02)00140-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Mobile clinical support system for pediatric emergencies

Wojtek Michalowski<sup>a,</sup>\*, Steven Rubin<sup>b</sup>, Roman Slowinski<sup>c</sup>, Szymon Wilk<sup>c</sup>

<sup>a</sup> School of Management, University of Ottawa, 136 Jean-Jacques Lussier St. Ottawa, ON, Canada K1N 6N5

<sup>b</sup> Children’s Hospital of Eastern Ontario, Canada

<sup>c</sup> Poznan University of Technology, Poland

Received 1 February 2002; received in revised form 1 May 2002; accepted 1 July 2002

## Abstract

This paper describes the process and methodology of designing and developing a mobile support system to triage abdominal pain in the emergency room (ER) of a hospital. Application of rough sets theory and fuzzy measures to data collected at Children’s Hospital of Eastern Ontario allowed us to identify the most relevant clinical symptoms and signs while evaluating an abdominal pain patient. This information was used to develop a multilevel clinical algorithm that forms the reasoning module of a clinical support system. We describe a client system called Mobile Emergency Triage (MET) that is installed on Palm handheld and that can be used to triage a child irrespective of the available information. We present MET’s functions allowing for the electronic data capture and wireless data transfer. <sup>D</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Clinical decision support system; Data mining; Triage; Mobile computing platform

## 1. Introduction

Abdominal pain in childhood is a highly prevalent symptom caused by organic diseases, psychosocial disturbances and emotional disorders. In many cases, the exact cause is never determined. Medical staff must focus on identifying a minority of cases in need of urgent treatment. For the patients where the diagnosis of appendicitis is in doubt, investigations and repeated assessments conducted by different physicians are time-consuming and may be painful. There is empirical evidence that highlights an obvious advantage of the rapid triage of patients with abdominal pain [2,pp.55, – 61]. However, the central difficulty of such triage is accurate initial assessment based on a limited number of clinical symptoms and signs (attributes) that in combination contribute the most to the diagnosis and management.

This paper describes the development of an easyto-use and caregiver-friendly Mobile Emergency Triage (MET) clinical support system to be used by emergency room (ER) personnel for the evaluation of patients with abdominal pain. Prior to developing such a system, one needs to evaluate and describe in the form of a clinical algorithm the diagnostic practice that is applied to triage a child. Results of our earlier research [11,pp.23 – 28;16,pp.19 – 24] which focused on the evaluation of alternative knowledge discovery methodologies confirm that development of a clinical algorithm for triage of the child with abdominal pain is feasible. Building on these results, we analyzed a large sample of patients’ data in order to develop a multilevel clinical algorithm in the form of decision rules. This algorithm constitutes a reasoning module of the MET system that client component is implemented on the Palm handheld. A client module allows the ER personnel (nurse practitioner (NP) or physician) to triage the child, and to gather pertinent patient information that can be shared easily among various caregivers using wireless communication (IrDA port of the Palm handheld).

The MET system was designed following a general framework developed for the medical aid tools for patient management support [22,pp.82–85], but at the same time, it significantly expands the suggested scope of these tools by:

 supporting early triage irrespectively of the amount of information available about patient’s condition,

 allowing for structured data capture, and

 providing ‘‘triage on demand’’ at the patient’s bedside.

The paper is organized as follows. We start by describing the process of ER management of a child with abdominal pain and information that is collected at that time. The analytical methodology is briefly described in Section 3 and in greater detail in Appendix A. The results are presented in Section 4, and a mobile triage system implemented on Palm handheld is described in Section 5. The paper ends with the conclusions.

## 2. ER management of child with abdominal pain

The typical process of ER management of a child complaining of abdominal pain is illustrated in Fig. 1.

The child is initially assessed by the ER triage nurse practitioner (NP). This assessment is followed by a detailed examination conducted by the ER physician. The possible outcomes of this evaluation are: no management, surgical consult, and not-yetdiagnosed (NYD). No management indicates that the abdominal pain spontaneously subsides. Such a patient can be discharged to the care of his/her regular physician. Surgical consult implies that acute appendicitis is suspected and a surgeon is called. Further inhospital clinical evaluation is needed for the NYD patient.

Triage is the first stage in the process of patient management. The final (actual) diagnosis is known when the patient is discharged, and with the patients triaged as surgical consult, the final diagnosis is obtained from the post-surgery pathology report. Any clinical support system aimed at facilitating ER management should contribute to patient management as described above. The MET system described in this paper is partially following the above process by providing a clinical support of a triage stage only.

There is no consensus in the medical literature regarding the most effective management of abdominal pain patients. Several studies advocate use of some form of a scoring system as a clinical support tool [1,pp.67 –69;8,pp.427 – 432], while others argue that only an experienced member of the pediatric surgical team is capable of the reliable diagnosis of acute appendicitis [18,pp.110– 112]. Current practice in teaching hospitals shows an ER triage accuracy of

![](/api/attachments/D9UM9GWK/fulltext/images/c2467d0bd3a80fbe3c4dfc8fd15f4a5974af8e68160be6a2ceed8a542427d671.jpg)  
Fig. 1. ER management of child with abdominal pain.

50 –60% achieved by an ER triage NP in the case of diagnosing appendicitis. This observation further supports our intent to support a triage stage of the patient management process.

A retrospective chart study using the records of 647 patients with abdominal pain seen during the 1997–2000 period in the ER of the Children’s Hospital of Eastern Ontario (Ottawa, Ontario) involved evaluation for each patient of 12 clinical symptoms and signs (attributes) recommended in current medical texts and practice. These attributes and their domains are given in Table 1. It should be noticed that not every caregiver is able to conduct all the examinations necessary to obtain the values for every attribute. The ER triage NP is trained to acquire the values of some of the attributes (for example, elements of a medical history), while the ER physician is trained to carry out a complete examination.

Table 1  
Clinical symptoms and signs and their domains

<table><tr><td>Attribute code</td><td>Description</td><td>Domain</td></tr><tr><td>Age</td><td>number of years</td><td>0–6, ≥7 years</td></tr><tr><td>Sex</td><td>gender</td><td>male, female</td></tr><tr><td rowspan="2">AbdPainDuration</td><td>length of time</td><td rowspan="2">≤24 h, 1–7 and &gt;7 days</td></tr><tr><td>pain occurs</td></tr><tr><td>AbdPainSite</td><td>the site of maximal pain</td><td>right lower quadrant (RLQ), lower abdomen, other</td></tr><tr><td>AbdPainType</td><td>type of maximal pain</td><td>continuous, other</td></tr><tr><td>Vomiting</td><td>vomiting occurred</td><td>yes, no</td></tr><tr><td>PrevVis</td><td>previous visits to the ER for abdominal pain (irrespective of the site) in the last 48 hours</td><td>yes, no</td></tr><tr><td>Tempr</td><td>fever</td><td>&lt;37, 37–39, ≥39 °C</td></tr><tr><td>AbdTend</td><td>site of maximal tenderness</td><td>RLQ, lower abdomen, other</td></tr><tr><td>Guarding</td><td>localized muscle sustained contraction noted when palpating the abdomen</td><td>absent, present</td></tr><tr><td>LocAbdRebTend</td><td>pain felt at site of maximal tenderness, produced by altering intra-abdominal pressure</td><td>absent, present</td></tr><tr><td>WBC</td><td>white blood cell count</td><td>≤4000, 4000–12000, ≥12000</td></tr></table>

Table 2  
Partition of patient records into decision classes

<table><tr><td>Decision class</td><td>No. of charts</td><td>% of charts</td></tr><tr><td>No management</td><td>394</td><td>60.9</td></tr><tr><td>Surgical consult</td><td>195</td><td>30.1</td></tr><tr><td>NYD</td><td>58</td><td>9.0</td></tr><tr><td>Total</td><td>647</td><td>100.0</td></tr></table>

Most of the considered attributes have nominal values (for example, gender or type of pain), some have numerical values (for example, temperature or white blood cell count), and some indicate the location of a condition on the patient’s abdomen (for example, location of the pain or site of tenderness). Values of these latter attributes were collected with the help of special abdomen pictograms, on which the ER physician marked the exact location. Numerical values were discretized according to medical practice, and ‘‘location’’ attributes were assigned a value using an algorithm developed by surgeons and ER physicians for that specific purpose.

Following the patient management process and according to medical practice, patient records were classified into three decision classes (triage outcomes): no management, surgical consult, and NYD. The detailed partition of a data set is given in Table 2. The data set is unbalanced—61% of the patients belong to the no management class, the surgical consult class includes 30% of all records, and the remaining 9% belong to the NYD. Such structure of a data set reflects typical portfolio of abdominal pain cases seen in the ER of a teaching hospital.

Collected data contains a significant number of missing values. Detailed information about these values is presented in Table 3. Values of only one attribute —Age—are known for all patients. Five attributes have more than 10% of missing values, and three of them (Guarding, WBC, and LocAbdRebTend) have more than 20% of missing values.

Fig. 2 reveals an interesting pattern of missing values among the decision classes. Except for two attributes (AbdPainDuration and Tempr), the largest ratio of missing values appears in the no management class, and the smallest in the surgical consult. This may be explained by the fact that if after conducting a few basic examinations the most likely triage is no management, then other symptoms and signs are not checked. Clearly, patients triaged as surgical consult or NYD are examined more thoroughly.

Table 3  
Missing values of the attributes (in %)

<table><tr><td rowspan="2">Attribute Code</td><td colspan="3">Decision class</td></tr><tr><td>No management</td><td>Surgical consult</td><td>NYD</td></tr><tr><td>Age</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td>AbdPainDuration</td><td>0.00</td><td>2.56</td><td>1.72</td></tr><tr><td>AbdPainSite</td><td>2.28</td><td>1.03</td><td>8.62</td></tr><tr><td>AbdPainType</td><td>10.66</td><td>10.26</td><td>13.79</td></tr><tr><td>AbdTendSite</td><td>15.99</td><td>2.56</td><td>15.52</td></tr><tr><td>Guarding</td><td>32.23</td><td>12.82</td><td>22.41</td></tr><tr><td>LocAbdRebTend</td><td>40.36</td><td>22.05</td><td>34.48</td></tr><tr><td>PrevVis</td><td>2.03</td><td>0.00</td><td>0.00</td></tr><tr><td>Sex</td><td>0.25</td><td>0.00</td><td>0.00</td></tr><tr><td>Tempr</td><td>1.52</td><td>2.05</td><td>0.00</td></tr><tr><td>Vomiting</td><td>1.02</td><td>0.51</td><td>1.72</td></tr><tr><td>WBC</td><td>44.16</td><td>2.56</td><td>18.97</td></tr></table>

An important issue to be addressed is the treatment of the attributes with a significant number of missing values. Clearly, they should not be discarded (a common approach in other studies is to remove from further analysis the attributes with a number of missing values above a certain threshold), as their importance depends on the context in which they are evaluated. The WBC attribute is a very good example of such a situation. It has 44% of missing values for the no management class, but less than 3% for the surgical consult class. One can conclude that triage of almost half of the patients was clear and did not require any further investigations, and thus requesting the WBC was not necessary. Thus, the WBC in this particular context is not an important attribute. On the other hand, when a patient is triaged as a surgical consult, the WBC results are very important for that patient’s management, and a minimal number of missing values (less than 3%) should rather be attributed to incorrect entry of the WBC information on the patient’s chart in the ER.

## 3. Methodology

The data set created from the patients’ charts was analyzed for regularities using rough sets analysis and Shapley value based on fuzzy measures [13,14, $\mathrm { p p . } 4 4 3 - 4 5 9 ; 1 7 , \mathrm { p p . } 3 0 7 - 3 1 7 ; 1 9 , \mathrm { p p . } 8 - 2 5 ]$ . The basic notions behind methodologies used to develop the MET system are described in Appendix A. Complete description of the rough sets, fuzzy measures and their use in data analysis can be found in the papers referenced throughout the discussion included in Appendix A.

![](/api/attachments/D9UM9GWK/fulltext/images/a88f5c6abb73577ea1fcdd2c1a227aa3181ef904b3f54aaa1b67b3d376700bfb.jpg)  
Fig. 2. Distribution of the missing values among decision classes.

The key idea of rough sets is related to an approximation of knowledge expressed by decision attributes using knowledge that is expressed by condition attributes. Rough sets theory answers several questions related to such approximation:

(a) Is the data consistent?

(b) What are the nonredundant subsets of condition attributes (reducts) ensuring the same quality of approximation as the whole set of condition attributes?

(c) What are the condition attributes (core) that cannot be eliminated from the approximation without decreasing the quality of the approximation?

(d) What minimal ‘‘if . . ., then . . .’’ decision rules can be induced from the approximations?

Several important aspects of rough sets theory made it of particular interest to the researchers evaluating real data sets describing various decision situations [10]. With respect to the input information, rough sets allow us to analyze both quantitative and qualitative data, and data inconsistencies need not be removed prior to the analysis, as they are dealt with by separating certain and doubtful knowledge extracted from the information table. With reference to the output information, rough sets allow us to acquire a posteriori information regarding the relevance of a particular attribute (or subsets of attributes) for the quality of approximation. Moreover, the final result presented in the form of ‘‘if. . ., then. . .’’ decision rules that are based on the most relevant attributes is easy to interpret. In case evaluation of the condition attributes from the viewpoint of their relevance to decision problem description is inconclusive (a situation we have encountered while developing the MET system), it can be enhanced with the development of Shapley value based on fuzzy measures to establish a partial ordering of the attributes in terms of their information content.

## 4. Results

The medical data set described in Section 2 was analyzed using ROSE software [15,pp.172 –180]. Due to the large number of missing values, an extended rough sets methodology [6,pp.295– 316] was used to:

 find the clinical symptoms and signs that are the most relevant for classifying a patient as no management, surgical consult, or NYD;

 induce the set of decision rules based on the attributes selected in the previous step that ensure a high classification accuracy of patients in the ER.

Evaluation of all condition attributes according to their Shapley values is presented in Table 4. The table also gives the percentages of missing values for each attribute, and the quality of classification associated with the set of attributes containing attributes starting from the ‘‘Tempr’’, up to the attribute in a specific row of Table 4. For example, the quality of classification of 0.094 for the AbdPainSite was achieved for the set of attributes containing Tempr, AbdPainDuration, Sex, Vomiting, and AbdPainSite.

It is worthwhile to note that the order of the attributes in Table 4 closely follows the ranking according to a percentage of missing values, especially for those that have more than 10% of missing data. The low rank of the WBC attribute can be explained by the fact that the original data set is not well balanced, with the no management class being the dominant one. Therefore, the large number of missing WBC values for that class had an overwhelming impact on the WBC rank. The overall ranking is consistent with an intuitive observation, that the less information the attribute bears, the less relevant it is according to the Shapley value ranking. The only exception is ‘‘Age’’, which has no missing values, but its low importance may be explained by the very general discretization (see Table 1) that most likely entails the loss of information.

Table 4  
The attributes sorted in a descending order according to Shapley measure

<table><tr><td>Attribute code</td><td>Shapley value</td><td>Quality of classification</td><td>% of missing values</td></tr><tr><td>Tempr</td><td>0.079</td><td>0.000</td><td>1.5</td></tr><tr><td>AbdPainDuration</td><td>0.072</td><td>0.002</td><td>0.9</td></tr><tr><td>Sex</td><td>0.069</td><td>0.002</td><td>0.2</td></tr><tr><td>Vomiting</td><td>0.067</td><td>0.006</td><td>0.9</td></tr><tr><td>AbdPainSite</td><td>0.066</td><td>0.094</td><td>2.5</td></tr><tr><td>PrevVis</td><td>0.065</td><td>0.196</td><td>1.2</td></tr><tr><td>AbdTendSite</td><td>0.053</td><td>0.280</td><td>11.9</td></tr><tr><td>AbdPainType</td><td>0.046</td><td>0.337</td><td>10.8</td></tr><tr><td>Age</td><td>0.045</td><td>0.433</td><td>0.0</td></tr><tr><td>Guarding</td><td>0.031</td><td>0.539</td><td>25.5</td></tr><tr><td>WBC</td><td>0.030</td><td>0.601</td><td>29.4</td></tr><tr><td>LocAbdRebTend</td><td>0.017</td><td>0.640</td><td>32.3</td></tr></table>

The choice of the most relevant attributes on the basis of the information given in Table 4 is not obvious; thus, after consulting with the ER physicians and surgeons, we decided to use several thresholds, beginning with the set of the top five attributes (Tempr, AbdPainDuration, Sex, Vomiting, and Abd-PainSite), for which a considerable increase in the quality of classification was observed. Then, we iteratively enlarged this set with the remaining attributes according to their Shapley value ranking. The LocAbdRebTend was appended last, so we finished with the set containing all 12 condition attributes.

For each set of attributes, we tested the classification accuracy of the corresponding decision rules. The classification accuracy was estimated using 10-fold cross-validation tests [12]. In order to get more reliable results, the validation tests were repeated five times and their results were averaged over all repetitions. The decision rules were induced using the Explore algorithm [20,pp.13 – 28] that generates the set of satisfactory rules that meet predefined requirements (maximum number of elementary conditions in a rule (rule length), the minimum rule strength, and the minimum confidence index). In our analysis, the length of the generated rules was not restricted, the minimum confidence index was set to 0.8, and the minimum strength was later modified during the tests. This modification procedure is described in details in Ref. [21]. Running Explore with a minimum confidence index of 0.8 is equivalent to inducing rules from the lower approximations, calculated in the VPM with b coefficient equal to the confidence index.

Handling of missing values required some changes in the rule induction algorithm. Firstly, we assumed that the rule condition will be satisfied by value equal to the value in a condition or by a missing value (for example, condition Vomiting = ‘yes’ will be met by the value ‘yes’ and also by a missing value). Secondly, the algorithm was modified to ensure robustness of generated rule so it covers at least one object that has a nonmissing (known) value for the condition attributes. The satisfactory results of the 10-fold crossvalidation tests suggest that it is possible to generate ‘‘accurate’’ rules (i.e. ensuring high classification accuracy) using smaller subsets of condition attributes. These test results as well as the satisfactory rules generated for different subsets of the attributes were presented to the pediatric surgeons for the consultations. Ultimately, the multilevel clinical algorithm was developed using three sets of attributes—containing 5, 8, and 11 attributes, respectively—and implemented in the MET system. The rules comprising the clinical algorithm are to be used at various stages of child management in the ER, depending on the amount of available information (thus, the rules created for 5 attributes could be used to suggest the initial triage shortly after the patient is admitted to the ER, while the rules generated for 11 attributes can be applied when most of the necessary examinations have been concluded). It is important to stress here that for a given consultation, the rules from any level (separately and in combination) can be consulted.

Simulation experiment was conducted to evaluate triage accuracy of the multilevel clinical algorithm implemented in the MET client. The triage suggested by MET was correct for almost 91% of no management class patient, for almost 75% of surgical consult patients, and for almost 13% of the NYD class patient. Other medical studies [23,pp.390 –392] explain usually disappointing results obtained for the NYD class by the fact that differentiation between appendicitis and nonspecific abdominal pain (one of the most common complaints among the NYD patients) is very difficult on the basis of regularly evaluated symptoms and signs. From the point of view of a clinical practice, the misclassifications of the patients by MET are medically appropriate (i.e. a patient with some medical condition is not triaged as a no management case) in over 85% of the situations. Moreover, the positive predictive value (i.e. probability that a patient has some medical condition given MET triage of the surgical consult or NYD) of the MET triage is over 81%, and its negative predictive value (i.e. probability that a patient is healthy given MET triage as no management) is over 79%. These experimental results provide early confirmation of the validity of a clinical algorithm and its specific implementation in the MET client.

For illustrative purposes, in Table 5 we present the rules generated for the sets of five clinical symptoms and signs. The relative strength of a rule explains that rule’s coverage (for example, the first rule in Table 5 having the relative strength of 54.6% is capable of matching 54.6% patients from the no management class).

Table 5  
Decision rules generated for five attributes

<table><tr><td>Triage</td><td>AbdPainDuration</td><td>AbdPainSite</td><td>Sex</td><td>Tempr</td><td>Vomiting</td><td>Relative strength (%)</td></tr><tr><td rowspan="2">No management</td><td></td><td>other</td><td></td><td></td><td></td><td>54.6</td></tr><tr><td></td><td></td><td></td><td>&lt;37</td><td>absent</td><td>38.6</td></tr><tr><td rowspan="2">Surgical consult</td><td>1–7 days</td><td>RLQ</td><td>male</td><td></td><td>present</td><td>28.7</td></tr><tr><td></td><td>RLQ</td><td>male</td><td>&lt;37</td><td>present</td><td>16.9</td></tr><tr><td rowspan="2">NYD</td><td>≤24 h</td><td></td><td></td><td>&gt;39</td><td></td><td>1.7</td></tr><tr><td></td><td>other</td><td>male</td><td>&gt;39</td><td>absent</td><td>3.4</td></tr></table>

## 5. Mobile clinical support system

The management of a patient with abdominal pain in the ER requires an initial assessment of his/her condition, repeatedly evaluating the patient’s history, physical findings, and laboratory and radiological tests. On the basis of such an assessment and a triage, a final diagnosis is reached and an appropriate management is selected. Thus, any clinical decision support system needs to have the ability to follow this process and to provide a caregiver with an appropriate level of support at its every stage. It means that such a system should have information-gathering facilities, the ability to triage, and finally, should ‘‘follow a patient’’ as his/her management is transferred between different caregivers. The MET system discussed here maintains all of these features. It allows for the collection of information about the patient’s condition; it uses a three-level clinical algorithm to support the triage irrespective of the amount of available information about a patient. It also provides ‘‘triage on demand’’ by ‘‘following the patient’’—a feature achieved by its implementation on a mobile device such as a Palm handheld. The system has been developed according to the principles of client-server architecture [3]. The client module runs on a Palm handheld with PalmOS 3.5 (or later), and the server is implemented on a PC running Windows NT/2000. Communication among Palm handhelds and between the Palm and the PC is maintained using a wireless infrared (IrDA) port or a cradle adapter, respectively. The desired functionality of the MET system is accomplished through a clear division of the tasks to be performed on the server and on the client side.

The Palm handheld client is responsible for the following tasks:

Gathering patient data. The client is used for entering clinical information (including medical history) about examined patients and storing it in a local database (electronic data capture).

 Supporting the triage decision. Using information currently stored in a local database, the client applies multilevel clinical algorithm to triage a patient.

 Synchronizing patient’s data with other clients. The client is capable of transmitting data from a local database to other clients using a wireless port. It is also capable of receiving data from other clients and storing it in a local database.

 Transferring data to a PC server. The client is able to transfer the contents of a local database to a server using a cradle adapter or infrared port.

The PC server is responsible for the following tasks:

 Managing and synchronizing a centralized database. Using merge/update operations, the server manages a centralized database containing all the patients’ records collected from the Palm handheld clients.

 Periodic analysis of the data stored in a centralized database. The server periodically analyzes the data stored in the centralized database to evaluate and possibly calibrate the clinical algorithm.

![](/api/attachments/D9UM9GWK/fulltext/images/ca7784bf221accb5ac444d2be32a64c359339332a47a7ef726a205001731112f.jpg)  
Fig. 3. System’s architecture.

 Updating the clinical algorithm used by the Palm handheld clients. If necessary, the server automatically updates the clinical algorithm residing on the Palm handheld client through a HotSync function.

![](/api/attachments/D9UM9GWK/fulltext/images/f6ef51dc6f83c2672d6eaaa10d00937df04eb1964b5c6c1c23d4ae99c90ffafa.jpg)  
Fig. 4. Patients’ records entry screen.

The overall system’s architecture is illustrated in Fig. 3.

Use of the system begins with the entry of the patient’s information (including unique PIN) at the moment of the patient’s admission to the ER. Initial data entry screen is presented in Fig. 4.

![](/api/attachments/D9UM9GWK/fulltext/images/d04effc35bb95912e1f899ac3b0eac262a3295e0468d58fabdb5d86637243022.jpg)  
Fig. 5. Graphical data capture.

![](/api/attachments/D9UM9GWK/fulltext/images/8dcb531d1668f9e8d1fc08c7d6eceb6f7772ae0f47e40fd912cce8c3519658d9.jpg)  
Fig. 6. Predefined selection data capture.

![](/api/attachments/D9UM9GWK/fulltext/images/ba3d9fac6342a2efba0a0258e68319a51eb87c9e8eb0a07b9a54f6f4002c799a.jpg)  
Fig. 7. Free-entry data capture.

One of the unique features of the system is its adaptability to different data entry requirements. For example, the results of the physical examination of the abdomen are captured using the pictograms (see Fig. 5). Information about the type of maximal pain is gathered using a predefined selection list (see Fig. 6), while the information about the duration of the pain is entered using a free-entry format (see Fig. 7). For most of the clinical symptoms and signs, the system allows also for the free entry of any additional comments about the patient’s condition (see ‘‘comments button’’ in Figs. 5 and 6) as deemed necessary by the attending health care professional. There is reported evidence that such structured data collection should contribute to the improved triage and diagnosis of a patient [9,pp.341 – 344].

The system’s triage function can be invoked at any time and it uses the most current clinical information to provide a triage recommendation (see Fig. 8 for triage advice screen).

![](/api/attachments/D9UM9GWK/fulltext/images/13dad1c910e78399241c6031b9f9cef59998db4734f1db781677a641cf23dfcb.jpg)  
Fig. 8. Invoking triage function.

Depending on the information available to a caregiver, the MET system invokes the most suitable level of the clinical algorithm, that is, a set of rules providing the best overall match. Even if in a given set there are no rules exactly matching the available data, the system will consult the most closely matching rules but diminishing at the same time a strength factor associated with such consultation. Presentation of this information is illustrated in Fig. 9.

The triage strength factor is calculated on the basis of rules activated during classification. First, for all invoked rules, the matching ratios are calculated (matching ratio is a function of the number of fully matched conditions in the rule, rule’s strength, and rule confidence index). Matching ratios are then summed up within each decision class for all possible rules (for a given set of the attributes) to get total matching ratios. Finally, these total ratios are normalized relative to their maximum values. The normalized ratios are presented to end-used as the triage strength factors. A decision class that acquired the highest triage strength factor is then presented as a ‘‘suggested triage’’. If for all possible triage outcomes the normalized matching rations are equal to zero, then the NYD class is presented as a default triage.

![](/api/attachments/D9UM9GWK/fulltext/images/6a17b8caf9f0575599ce3539ab0d5132cc060f28be1d91d3641537afde13959a.jpg)  
Fig. 9. Strength factor of a triage.

Once the care of a patient has been transferred to another caregiver, all information gathered so far (including triage recommendation) can be beamed (wireless transfer) to another Palm handheld client. When new information about a patient becomes available, the triage function of the system might be invoked again and MET will use updated information to reevaluate the latest triage decision. At the end of the process, all the pertinent patient data is transferred to the PC server, thus either creating or updating each patient’s record in a centralized database.

## 6. Conclusions

The purpose of the research described in this paper was to develop an easy-to-use and mobile clinical system that can support the triage decision for a patient with abdominal pain. The analyzed medical data set had the large number of missing values for some of the attributes. The analysis discussed here would not be possible without a hybrid approach that allowed us to consider the number of missing values and their distribution among the triage classes. This was accomplished with a help of the rough set theory and the fuzzy measure that were used to assess the attributes’ relevance for triage decisions. The generation of satisfactory decision rules and the development of a multilevel clinical algorithm to triage patients in the ER followed this analysis. The application of the clinical algorithm was enhanced with the ability to handle the missing values so the rules with incomplete antecedents were also evaluated. The simulation results (overall triage accuracy, positive and negative predictive values) confirmed validity of the multilevel clinical algorithm for triage of abdominal pain children.

The MET system that was developed follows the basic requirements expected from the effective clinical decision support systems:

 It allows entry of the relevant patient information (medical history, tests, and physical examination).

 It allows storage and transmission of this information.

 It allows consulting the triage function independently of the stage in the patient management process, matching information available to the most appropriate level of a clinical algorithm.

Functionality of the MET is further enhanced by providing all the above in a coordinated manner at a patient’s bedside. Currently, we are working on a limited clinical testing of the system in a teaching hospital in Ontario and expanding the system’s reasoning capabilities to cover the management of a scrotal pain condition in childhood.

The approach used to develop MET can be generalized for design of decision support systems in a variety of areas. One of the fallacies of several DSS is that they provide needed information when it is not needed the most. It is because of established paradigm that DSS is stationary and is being used by a decision maker in well-defined circumstances. Our work on MET clearly showed that it is not a case and that some form of support is required outside established decision-making boundaries. We have addressed that issue by implementing a ‘‘front end’’ DSS on a mobile platform such as Palm handheld. This creates a ‘‘DSS in a pocket’’ model allowing a decision-maker to get support irrespectively of a location and decisionmaking environment. Enhancing the DSS capabilities with data gathering function allows capturing data characteristic for specific situation and later using it for improving DSS advisory ability. Such ‘‘self-learning’’ of a DSS model component may prove of particular importance when a high level of volatility and timeliness characterizes knowledge about a particular situation.

## Acknowledgements

The research reported in this paper was supported by the grants from the Polish Committee for Scientific Research, the Foundation for Polish Science, and the Natural Sciences and Engineering Research Council of Canada. The authors would like to thank Eric Payne for help in developing a data set from the ER admission charts, and Ann Burgess for editorial assistance.

The MET system was created using PUMATECH Satellite Forms Enterprise Edition RAD environment.

## Appendix A

## A.1. Rough sets theory

For rough sets analysis, the data is supplied in the form of an information $t a b l e ,$ in which rows represent objects (patients’ charts) and columns represent attributes (clinical symptoms and signs and triage outcomes recorded on the charts). Each cell of the table indicates an evaluation (quantitative or qualitative) of an object represented by the corresponding row by means of an attribute represented by the corresponding column. Formally, an information table is the 4-tuple $S =$ $< U , Q , V , f > _ { }$ , where $U$ is a finite set of objects (universe), Q is a finite set of attributes, $V = \cup _ { q \in Q } V _ { q }$ and $V _ { q }$ is the domain of the attribute $q , f \colon U \times Q \to V$ is a function called information function such that $f ( x , q ) { \in } V _ { q }$ for each $q \in Q , x \in U .$ The set $\mathcal { Q }$ is divided into a set $C$ of condition attributes, and a set $D$ of decision attributes (for the data set described in this paper, it is a singleton—the triage outcome).

Each object x of U is described by a vector of evaluations (attribute values), called description of x in terms of the attributes of $\mathcal { Q } .$ This vector represents available information about x. Objects having the identical description are called indiscernible. In general, the indiscernibility relation on $U ,$ denoted by $I _ { P } ,$ is associated with every (nonempty) subset of attributes $P \subseteq Q$

$$
\begin{array}{l} I _ {P} = \{(x, y) \in U \times U: \\ f _ {q} (x) = f _ {q} (y), \quad \text { for   each } q \in P \} \end{array}\tag{1}
$$

Clearly, the relation (1) is an equivalence relation (reflexive, symmetric, and transitive); thus, it partitions set U into equivalence classes called P-elementary sets. The family of all the equivalence classes of relation $I _ { P }$ is denoted by $U | I _ { P }$ and the equivalence class containing an object $x { \in } U$ is denoted by $I _ { P } ( x )$ . If $( x , y ) { \in } I _ { P } ,$ then objects x and y are P-indiscernible.

The partitions of set U induced by subsets of condition attributes and subsets of decision attributes represent knowledge about U.

For a demonstration of the basic concepts of rough sets, let us assume that X is a nonempty subset of $U ,$ for example, an equivalence class with respect to set $D$ of decision attributes, and $P \subseteq C$ is a subset of condition attributes.

We say that object x<sup>a</sup>X belongs certainly to X if all objects from the P-elementary set $I _ { P } ( x )$ also belong to X, i.e. $I _ { P } ( x ) \subseteq X$ . Then, for a given P, information about object x is consistent with information about other objects from U.

We say, moreover, that object x<sup>a</sup>U could belong to X if at least one object from the P-elementary set $I _ { P } ( x )$ belongs to $X ,$ i.e. $I _ { P } ( x ) \cap X \neq \emptyset . \mathrm { I f } \ \emptyset \neq I _ { P } ( x ) \cap X \neq I _ { P } ( x )$ then, for a given P, information about object x is inconsistent with information about other objects from $I _ { P } ( x )$

For $P \subseteq C$ , the set of all objects belonging certainly to X constitutes the P-lower approximation of $X ,$ denoted by P(X), and the set of all objects that could belong to X constitutes the P-upper approximation of $X ,$ denoted by ${ \overline { { P } } } ( X )$

$$
\underline {{P}} (X) = \{x \in U: I _ {P} (x) \subseteq X \},\tag{2}
$$

$$
\overline {{P}} (X) = \{x \in U: I _ {P} (x) \cap X \neq \emptyset \}.\tag{3}
$$

The difference between the upper and lower approximations of X is called the P-boundary of X:

$$
B n _ {P} (X) = \overline {{P}} (X) - \underline {{P}} (X).\tag{4}
$$

The P-boundary of X is composed of inconsistent objects that belong to X with some ambiguity. The following relations hold: ${ \underline { { P } } } ( X ) \subseteq X \subseteq { \overline { { P } } } \left( X \right)$ ， ${ \underline { { P } } } ( X ) =$ $U - \overline { { P } } ( U - X )$

The family of all the sets $X \subseteq U$ having the same lower and upper approximations is called a rough set.

The rough approximations of a subset $X \subseteq U$ can be extended to partitions of $U ,$ in particular, to the partition induced by decision attributes from D. This partition corresponds to the classification of objects into decision classes—the lower approximations of decision classes represent certain knowledge, upper approximations represent possible knowledge, and the boundaries represent doubtful knowledge about the classification, expressed in terms of condition attributes from $P \subseteq C .$

Given a partition of U into decision classes, $C l { = } \{ C l _ { t } ,$ $t { \in } T \} , T { = } \{ 1 , . . . , n \}$ , the P-boundary with respect to $k { > } 1$ classes $\{ C l _ { t 1 } , . . . , C l _ { t k } \} \subseteq \{ C l _ { 1 } , . . . , C l _ { n } \}$ is defined as

$$
B d _ {P} \left(\left\{C l _ {t 1}, \dots , C l _ {t k} \right\}\right) = \left(\bigcap_ {t = t 1, \dots , t k} B n _ {P} \left(C l _ {t}\right)\right)
$$

$$
\cap \left(\bigcap_ {t \neq t 1, \dots , t k} (U - B n _ {P} (C l _ {t}))\right).\tag{5}
$$

The objects from $B d _ { P } ( \{ C l _ { t 1 } , . . . , C l _ { t k } \} )$ can be assigned to one of the classes $C l _ { t 1 } , . . . , C l _ { t k } .$ , however, P and all its subsets do not provide enough information to do this assignment precisely.

Using the rough approximations of decision classes, it is possible to induce decision rules describing the classification represented by examples contained in the information table. These are logical statements (implications) of the type $^ { \mathrm { s } } \mathrm { i f } \ldots ,$ then. . .’’, where the antecedent (condition part) is a conjunction of the elementary conditions concerning particular condition attributes, and the consequence (decision part) is a disjunction of possible assignments to particular classes of a partition of U induced by decision attributes. Given a partition Cl of $U ,$ the syntax of the rule is the following:

$$
\begin{array}{l} \text { ``   if   } f (x, q _ {1}) = r _ {q 1} \text {   and } \\ f (x, q _ {2}) = r _ {q 2} \text {   and   ... } \\ f (x, q _ {p}) = r _ {q p}, \text {   then   } x \text {   is   assigned   to   } C l _ {t 1} \text {   or   ...   } C l _ {t k} ^ {\prime \prime}, \end{array}\tag{6}
$$

where $\{ q _ { 1 } , . . . , q _ { p } \} \subseteq C , ( r _ { q 1 } , . . . , r _ { q p } ) \in V _ { q 1 } \times . . . \times V _ { q p } ,$ and $\{ C l _ { t 1 } , . . . , C l _ { t k } \} \subseteq \{ C l _ { 1 } , . . . , C l _ { n } \}$ . If the consequence is univocal, i.e. k = 1, then the rule is exact, otherwise, it is approximate or uncertain.

Let us observe that for any $C l _ { t } { = } \{ C l _ { 1 } , . . . . , C l _ { n } \}$ and $P \subseteq C$ , the definition (2) of P-lower approximation of $\mathrm { C l } _ { t }$ can be rewritten as

$$
\underline {{P}} \left(\mathrm{Cl} _ {t}\right) = \{x \in U: \text {   for   each   } y \in U,
$$

$$
\text { if   } y I _ {P} x, \text {   then   } y \in C l _ {t} \}\tag{7}
$$

Thus, the objects belonging to the lower approximation $\underline { { P } } ( C l _ { t } )$ can be considered as prototypes for the induction of exact decision rules.

Therefore, the statement $\mathop {  } \mathrm { i f } ~ f ( x , q _ { 1 } ) = r _ { q 1 }$ and $f ( x , q _ { 2 } ) = r _ { q 2 }$ and $\therefore f ( x , q _ { p } ) = r _ { q p } ,$ , then x is assigned to $\mathrm { C l } _ { t } ^ { \mathbf { \gamma } , \mathbf { \gamma } }$ is accepted as an exact decision rule if and only if there exists at least one object $y { \in } \underline { { P } } ( C l _ { t } )$ $P { = } \{ q _ { 1 } , . . . . q _ { p } \}$ , such that $f ( y , q _ { 1 } ) = r _ { q 1 }$ and $f ( y , q _ { 2 } ) = r _ { q 2 }$ and $\therefore \cdot \cdot f ( y , q _ { p } ) = r _ { q p } .$

Given $\{ C \bar { l } _ { t 1 } , . . . , C l _ { t k } \} \subseteq \{ C l _ { 1 } , . . . , C l _ { n } \}$ we can write

$$
B d _ {P} \left(\left\{C l _ {t 1}, \dots , C l _ {t k} \right\}\right) = \{x \in U: \text {   for   each   } y \in U,
$$

$$
\text { if   } y I _ {P} x, \text {   then   } y \in C l _ {t 1} \text {   or   } \dots C l _ {t k} \}.\tag{8}
$$

Thus, the objects belonging to the boundary $B d _ { P } ( \{ C l _ { t 1 } , . . . , C l _ { t k } \} )$ can be considered as a basis for the induction of approximate decision rules.

The analysis of large information tables shows that the calculation of approximations according to Eqs. (2) and (3) may result in a large P-boundary of X. Consequently, it leads to weak decision rules (supported by few objects from lower approximations). In such a case, it seems reasonable to relax the conditions for the assignment of objects into lower approximations by allowing it to include some inconsistent objects. This relaxation is called a variable precision model (VPM) and is described in [Ref.24,pp.39–59]. VPM defines lower approximations using a limited number of counterexamples that is controlled by predefined level of certainty $\beta ~ ( 0 < \beta \leq 1 )$ . In VPM, the P-lower approximation of X in U is defined as:

$$
\underline {{P}} (X) = \left\{x \in U: \frac {| I _ {P} (x) \cap X |}{| I _ {P} (x) |} \geq \beta \right\}.\tag{9}
$$

If $\beta$ is set to 1, then the VPM model is equivalent to Eq. (2).

Decision rules induced from the lower approximations of decision classes defined by Eq. (9) have univocal consequences (decisions); however, the confidence index of each rule (defined as the number of objects matching both the condition and decision part of the rule to the number of objects matching the condition part only) varies from $\beta$ to 1.

The accuracy of the approximation of $X \subseteq U$ by the attributes from $P$ is given as the ratio:

$$
\alpha_ {P} (X) = \frac {| \underline {{P}} (X) |}{| \overline {{P}} (X) |}.\tag{10}
$$

The quality of the approximation of $X \subseteq U$ by the attributes from P is given as the ratio:

$$
\gamma_ {P} (X) = \frac {| \underline {{P}} (X) |}{| X |}.\tag{11}
$$

where $0 \leq \gamma _ { P } ( X ) \leq 1$ and the quality represents the relative frequency of the objects correctly classified by means of the attributes from P.

The quality of the approximation of classification Cl by set of attributes $P$ is given as:

$$
\gamma_ {P} (\boldsymbol {C l}) = \frac {\sum_ {i = 1} ^ {n} | \underline {{P}} (C l _ {i}) |}{| U |}.\tag{12}
$$

It is called in short quality of classification and specifies the ratio of all P-correctly classified objects to all objects in the information table.

Each minimal subset $P \subseteq C$ such that $\gamma _ { P } ( C l ) =$ $\gamma _ { C } ( C l )$ is called a reduct of S and denoted by ${ \cal R E D } _ { C l } \left( C \right)$ . An information table can have more than one reduct. The intersection of all reducts is called a core and is denoted by $C O R E _ { C l }$ (C). The core is composed of indispensable attributes that cannot be removed from the information table without decreasing the quality of classification. Condition attributes that do not belong to any reduct are called superfluous.

## A.2 . Missing values

In order to use the classical rough sets approach to information tables with missing data (empty cells in the condition portion of the information table), the tables must be converted by:

(a) replacing the missing value with a special value (for example, N/A) and then treating it as a known value;

(b) replacing the missing value with a known one (for example, with the average or most frequent value of the corresponding condition attribute in a whole data set or in a given decision class).

Both approaches have serious shortcomings. Using the former one, it is possible to obtain decision rules with conditions based on missing values that are represented by a selected special value. Such rules are difficult to interpret (for example, it is unreasonable to interpret a rule that in a condition part has an attribute with N/A value). The latter approach may falsify the data (by assigning for example, the most frequent value without any sound justification), especially when the number of missing values is large.

To address these shortcomings, an extension to rough sets theory was proposed $[ 6 , 9 \mathsf { p } . 2 9 5 - 3 1 6 ]$ , and it is briefly discussed here.

The definition of the information table $( S = < U , Q ,$ $V , f > )$ is extended by assuming that the set V is augmented to include the missing value (indicated by ‘‘\*’’).

Instead of the indiscernibility relation $I _ { P } ,$ , a new type of relation, denoted by $I _ { P } ^ { * }$ is introduced. For each object $x , y \in U$ and for each subset of attributes $P \subseteq Q ,$ $y I _ { P } ^ { * } x$ means that $f ( x , q ) = f ( y , q )$ , or $f ( x , q ) = *$ , or $f ( y , q ) = *$ , for every $q \in P .$ Let $I _ { P } ^ { * } ( x ) { = } \{ y { \in } U  \colon y I _ { P } ^ { * } x \}$ for each $x { \in } U$ and for each $P { \subseteq } Q . \ I _ { P } ^ { * }$ is a reflexive and symmetric but not transitive binary relation. Finally, let $U _ { P } ^ { * } { = } \{ x { \in } U \colon f ( x , q ) \neq *$ for at least one $q \in P \}$

Using $I _ { P } ^ { * } { } _ { : }$ , the definitions of the P-lower and $P -$ upper approximation of X become:

$$
\underline {{I}} _ {P} ^ {*} (X) = \{x \in U _ {P} ^ {*}: I _ {P} ^ {*} (x) \subseteq X \},\tag{13}
$$

$$
\overline {{I}} _ {P} ^ {*} (X) = \{x \in U _ {P} ^ {*}: I _ {P} ^ {*} (x) \cap X \neq \emptyset \}.\tag{14}
$$

P-lower approximation can be also calculated using the VPM model as

$$
\underline {{I}} _ {P} ^ {*} (X) = \left\{x \in U _ {P} ^ {*}: \frac {| I _ {P} ^ {*} (X) \cap X |}{| I _ {P} ^ {*} (x) |} \geq \beta \right\}.\tag{15}
$$

The approximations defined in Eqs. (13) and (14) are further used to calculate the P-boundary of $X ,$ accuracy of approximation of $X ,$ and the quality of the approximation of X.

Given the partition Cl of $U ,$ one can calculate the quality of the classification of Cl and use this measure to find reducts and core of attributes.

Using the rough approximations (13) and (14), it is possible to induce a generalized description of the examples contained in the information table in terms of decision rules (see Appendix A.1).

Since each decision rule (6) is an implication, a minimal decision rule represents a unique implication in the sense that there is no other implication having a subset of elementary conditions and the same consequent.

We say that $y \in U$ supports the exact decision rule $\mathfrak { e } _ { \mathrm { i f } } f ( x , q _ { 1 } ) = r _ { q 1 }$ and $f ( x , q _ { 2 } ) = r _ { q 2 }$ and $\begin{array} { r } { \ldots \mathopen { } \mathclose \bgroup \left( f ( x , q _ { p } ) \aftergroup \egroup \right) = r _ { q p } , } \end{array}$ then x is assigned to $C l _ { j } ^ { , , }$ , if $[ f ( y , q _ { 1 } ) = r _ { q 1 }$ and/or $f ( y , q _ { 1 } ) = * ]$ and $[ f ( y , q _ { 2 } ) = r _ { q 2 }$ and/or $f ( y , q _ { 2 } ) = * ] . . .$ and $[ f ( y , q _ { p } ) = r _ { q p }$ and/or $f ( y , q _ { p } ) = * ]$ and $\scriptstyle { y } \in C l _ { t }$

Similarly, we say that $y \in U$ supports the approximate decision rule $\mathop {  } \mathrm { i f } f ( x , q _ { 1 } ) = r _ { q 1 }$ and $f ( x , q _ { 2 } ) = r _ { q 2 }$ and $\therefore \cdot \cdot f ( x , q _ { p } ) = r _ { q p } ,$ , then x is assigned to $C l _ { t 1 }$ or . . . $C l _ { t k } ? { \boldsymbol { \mathit { \Sigma } } }$ , if $[ f ( y , q _ { 1 } ) = r _ { q 1 }$ and/or $f ( y , q _ { 1 } ) = * ]$ and $[ f ( y , q _ { 2 } ) = r _ { q 2 }$ and/or $f ( y , q _ { 2 } ) { = } * ] \ . . .$ . and $[ f ( y , q _ { p } ) = r _ { q p }$ and/or $f ( y , q _ { p } ) = * ]$ and $y { \in } B d _ { \mathrm { C } } ^ { * } ( \{ C l _ { t 1 } , . . . , C l _ { t k } \} )$

Decision rules induced from lower approximations defined by Eq. (15) have univocal consequences (decisions); however, the confidence index of each rule varies from $\beta$ to 1.

## A.3. Fuzzy measure

The quality of classification (calculated using either $I _ { P }$ or $I _ { P } ^ { * } )$ satisfies the properties of the set functions called fuzzy measures. Such measures can be used for modeling the importance of coalitions [4,pp.445, – 456], or as proposed in Refs. $[ 5 , \mathsf { p p } . 9 9 - $ 103;7,pp.1 –47], to assess the relative value of the information supplied by each attribute and to analyze the interactions among the attributes (using the quality of classification calculated according to Ref. [11]). Let us explain this point in greater detail.

Let $C { = } \{ q _ { 1 } , . . . , q _ { n } \}$ be a finite set, whose elements could be the players in a game, condition attributes in an information table, different criteria in a multicriteria decision problem, etc. Let PS(C) denote the power set of $C ,$ i.e. the set of all subsets of C. A fuzzy measure on $C$ is a set function $\mu \colon P S ( C ) \longrightarrow [ 0 , 1 ]$ satisfying the following axioms:

$$
\begin{array}{l} \text { a) } \mu (\emptyset) = 0, \mu (C) \leq 1, \\ \text { b) } A \subseteq B \text { implies } \mu (A) \leq \mu (B), \text { for   all } A, B \in P S (C). \end{array}
$$

Within game theory, the fuzzy measure $\mu ( A )$ is called the characteristic function and represents the payoff obtained by the coalition $A \subseteq C$ in a cooperative game; in a multi-attribute classification, $\mu ( A )$ can be interpreted as the conjoint importance of the attributes from $A \subseteq C .$

In game theory, some indices were proposed as specific solutions of cooperative games. The most important of those is the Shapley value $[ 1 7 , \mathsf { p p } . 3 0 7 -$ $3 1 7 ]$ , defined for every element $q _ { i } { \in } C$ as:

$$
\begin{array}{l} \phi_ {S} (q _ {i}) = \sum_ {P \subseteq C - \{q _ {i} \}} \frac {(n - | P | - 1) ! | P | !}{n !} \\ \qquad \times [ \mu (P \cup \{q _ {i} \}) - \mu (P) ]. \end{array}\tag{16}
$$

The Shapley value can be interpreted as an average contribution of the element $q _ { i }$ to all the possible coalitions (combinations) of the elements from C.

Looking at the contribution of particular attributes to the conjoint importance of the set of attributes, from the rough set perspective, one can notice that the quality of the approximation of classification Cl by set of attributes P is a fuzzy measure, thus $\mu ( P ) { = } \gamma _ { P } ( \mathrm { C l } )$ for every $P \subseteq C .$ . For $P { = } C ,$ , the value of $\gamma _ { C } ( \mathrm { C l } )$ is shared among the elements of C according to the Shapley formula, i.e. $\begin{array} { r } { \sum _ { i = 1 } ^ { n } \phi _ { S } ( q _ { i } ) = \mu ( P ) = \gamma _ { C } ( \mathbf { C } \mathbf { l } ) } \end{array}$

Thus, the Shapley value $\phi _ { S } ( q _ { i } )$ can be used to assess the contribution of a single attribute $q _ { i }$ to the quality of a classification. Those attributes with higher value of $\phi _ { S } ( { q } _ { i } )$ are considered to explain better relationships in a data set.

## References

[1] T.I. Anatol, Y. Holder, A scoring system for use in the diagnosis of acute abdominal pain in childhood, West Indian Medical Journal (44) (1995) 67 – 69.

[2] M. Fioravanti, F. Di Cesare, L. Ramelli, F. La Torre, A. Nicastro, S. Messinetti, Presurgery information and psychological adjustment to enterostomy, Italian Journal of Surgical Science (18) (1988) 55– 61.

[3] N. Ford, Web Developer.Com Guide to Building Intelligent Web Sites with Java Script, Wiley, New York, 1998.

[4] M. Grabisch, k-Order additive discrete fuzzy measures and their representation, Fuzzy Sets and Systems (89) (1997) 167– 189.

[5] S. Greco, B. Matarazzo, R. Slowinski, Fuzzy measures as a technique for rough set analysis, Proc. 6th European Congress on Intelligent Techniques and Soft Computing (EUFIT’98), Verlag Meinz, Aachen, 1998, pp. 99– 103.

[6] S. Greco, B. Matarazzo, R. Slowinski, Dealing with missing data in rough set analysis of multi-attribute and multi-criteria decision problems, in: S.H. Zanakis, G. Doukidis, C. Zopounidis (Eds.), Decision Making: Recent Developments and Worldwide Applications, Kluwer Academic Publishing, Dordrecht, 2000, pp. 295 – 316.

[7] S. Greco, B. Matarazzo, R. Slowinski, Rough sets theory for multicriteria decision analysis, European Journal of Operational Research (129) (2001) 1 – 47.

[8] S. Hallan, T. Edna, Estimating the probability of acute appendicitis using clinical criteria of a structured record sheet: the physician against the computer, European Journal of Surgery (163) (1997) 427 – 432.

[9] H. Korner, K. Sondenaa, J.A. Soreide, Structured data collection improves the diagnosis of acute appendicitis, British Journal of Surgery (85) (1998) 341– 344.

[10] T. Lin, N. Cercone (Eds.), Rough Sets and Data Mining, Kluwer Academic Publishing, Dordrecht, 1997.

[11] W. Michalowski, S. Rubin, R. Slowinski, Sz. Wilk, Triage of the child with abdominal pain: a clinical algorithm for emergency patient management, Paediatrics and Child Health (6) (2001) 23–28.

[12] T. Mitchell, Machine Learning, McGraw-Hill, New York, 1997.

[13] Z. Pawlak, Rough Sets: Theoretical Aspects of Reasoning about Data, Kluwer Academic Publishing, Dordrecht, 1991.

[14] Z. Pawlak, R. Slowinski, Rough set approach to multi-attribute decision analysis, European Journal of Operational Research (72) (1994) 443– 459.

[15] B. Predki, Sz. Wilk, Rough set based data exploration using ROSE system, in: Z.W. Ras, A. Skowron (Eds.), Foundations of Intelligent Systems, Springer-Verlag, Berlin, 1999, pp. 172– 180.

[16] S. Rubin, W. Michalowski, R. Slowinski, Sz. Wilk, Computerassisted triage of abdominal pain in childhood: a suggested clinical algorithm, Proc. Conference on Simulation in Health Sciences, The Society for Computer Simulation International, San Diego, 2001, pp. 19 – 24.

[17] L.S. Shapley, A value for n-person games, in: H.W. Kuhn, A.W. Tucker (Eds.), Contributions to the Theory of Games II, Princeton Univ. Press, Princeton, 1953, pp. 307 – 317.

[18] E.T. Simpson, A. Smith, The management of acute abdominal pain in children, Journal of Paediatric Child Health (32) (1996) 110 – 112.

[19] R. Slowinski, Rough sets approach to decision analysis, AI Expert Magazine (10) (1995) 8 – 25.

[20] J. Stefanowski, D. Vanderpooten, Induction of decision rules in classification and discovery-oriented perspectives, International Journal of Intelligent Systems (16) (2001) 13 – 28.

[21] J. Stefanowski, Sz. Wilk, Evaluating business credit risk by means of approach integrating decision rules and case based reasoning, International Journal of Intelligent Systems in Accounting Finance and Management (10) (2001) 97 – 114.

[22] G.C. Sutton, Computer-aided diagnosis: a review, British Journal of Surgery (76) (1989) 82– 85.

[23] N.M.A. Williams, J.M. Johnstone, N.W. Everson, The diagnostic value of symptoms and signs in childhood abdominal pain, Journal of the Royal College of Surgery (43) (1998) 390– 392.

[24] W. Ziarko, Variable precision rough sets model, Journal of Computer and Systems Sciences (1) (1993) 39– 59.

![](/api/attachments/D9UM9GWK/fulltext/images/d863ea73097353fa11c6a7a92afb2940764ab2b2607e0904345729e701b79756.jpg)

Wojtek Michalowski is a professor of decision and management sciences at the School of Management and adjunct professor in the Faculty of Medicine, University of Ottawa (Canada). He is also director of the Master of Health Administration Program. During 1997 – 1998 academic year, he was senior research scholar at the International Institute for Applied Systems Analysis (Austria). He received M.Econ. in Econometrics and PhD in Operations

Research from the Warsaw School of Economics. Wojtek’s research interests include clinical decision support, decision analysis, health care management, multiple objective linear programming, and rough sets theory. He has written over 60 refereed papers and has published articles in some 30 journals, including Paediatrics and Child Health, Management Science, Naval Research Logistics, Operations Research, Journal of Optimization Theory and Applications, IEEE Systems, Man and Cybernetics, IEEE Expert, and European Journal of Operational Research.

Steven Rubin is a professor of surgery at the Faculty of Medicine, University of Ottawa and head of general surgery at the Children’s Hospital of Eastern Ontario (Canada). During the 1993 – 1999 period, he was director of surgical residency at the University of Ottawa, and currently he is program director for pediatric general surgery at the Postgraduate Medical Education Division. He published over 50 refereed papers and gave numerous invited presentations at national and international conferences.

![](/api/attachments/D9UM9GWK/fulltext/images/218bf58fac616d0f46328ff975e8b3ce56bab0a07e6277a4c5d966108ca3be82.jpg)

Roman Slowinski is a professor of operations research and decision science in the Institute of Computing Science, Poznan University of Technology (Poland) and director of Laboratory of Intelligent Decision Support Systems. He has been European Chair Professor at the University of Paris Dauphine and Research Professor at the Swiss Federal Institute of Technology, and at the University of Catania. He is coeditor of the European Journal of Opera-

tional Research, editor of Foundations of Computing and Decision Sciences, and area-editor of Fuzzy Sets and Systems. Roman Slowinski is recipient of the Sixth EURO Gold Medal by the European Association of OR Societies, and of the Edgeworth-Pareto Award, by the International Society on Multiple Criteria Decision Making. He is Doctor Honoris Causa of the Polytechnic University of Mons (Belgium) and of the University of Paris-Dauphine (France).

![](/api/attachments/D9UM9GWK/fulltext/images/e7fa3c1bbcbe59bfdcf0d1420ec1ee18d8500d4ba1b9f2987cdbe2c55267124b.jpg)

Szymon Wilk received the MSc (computer science) in 1997 and currently is a researcher and doctoral student at the Institute of Computing Science, Poznan University of Technology (Poland). During 1998 – 1999 period, he was involved with the Decision Analysis and Support Project at the International Institute for Applied Systems Analysis (Austria). His research interests include design of decision support systems and the applications of machine

learning and rough sets theory in clinical decision making.
