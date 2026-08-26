---
otero_id: 864
otero_key: "89QVW3QH"
title: "Smart medication management system and multiple interventions for medication adherence"
authors: "Upkar Varshney"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.10.011"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Smart medication management system and multiple interventions for medication adherence

Upkar Varshney

Department of Computer Information Systems, Georgia State University, Atlanta, GA, USA

a r t i c l e i n f o

Available online 6 October 2012

Keywords: Medication adherence Interventions Smart systems Modeling and performance Health monitoring

## a b s t r a c t

To keep healthcare costs under control, a high-level of medication adherence, or compliance with medication regimen, must be achieved. The multifaceted nature of medication adherence, due to a large number of underlying factors, presents several critical challenges including how to evaluate the current level of adherence how to improve and how to maintain the required level of medication adherence, especially for long-term chronic conditions. Several interventions to improve adherence have been proposed in the healthcare literature, however these are complex, costly and dif<sup>fi</sup>cult to implement. It is also not clear which ones would be effective at what levels of adherence in what conditions and types of patients. Therefore, there is a need to model, evaluate and compare the interventions individually as well as in combinations for their impact on medication adherence. To address this, the design and evaluation of smart medication management system (SMMS) for improving medication adherence are presented in this paper. We also present an analytical model for evaluating the medication adherence using multiple interventions that are supported from SMMS, namely context-aware reminders, improved scheduling of medications, and support from healthcare profes sionals. The performance results show that very high medication adherence is achievable by SMMS for single and multiple medications even for patients with mild cognitive de<sup>fi</sup>ciency. Several powerful “composite” interventions are also proposed and evaluated for medication adherence. It is also shown that the total healthcare savings are signi<sup>fi</sup>cant even for slightly improved medication adherence. With higher hospitalization cost, the savings due to improved medication adherence become even more signi<sup>fi</sup>cant. The proposed work forms the basis to design personalized interventions to patients for improving medication adherence in different surroundings.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

With 3 billion prescriptions/year in US alone [8,9], the cost of medications has been increasing signi<sup>fi</sup>cantly. Further, it is estimated that only between 50 and 60% of such medications are consumed as prescribed [9]. The reasons for not taking medication range from forgetfulness (30%), other priorities (16%), decision to omit (11%), lack of information (9%) and emotional factors (7%) [26]. Such non-adherence to medications leads to 125,000 deaths and \$90 billion in additional hospitalization and procedures every year in US alone [43]. Also, nonadherent patients experience twice the rate of hospitalization than those who are adherent. Some of the prescription medications, especially narcotics; sedatives, hypnotics, and anxiolytics; and stimulants, while used in catch-up mode could also lead to addiction, which requires detoxi<sup>fi</sup>cation and rehabilitation resulting in additional healthcare expenses [25].

Although the term compliance has been used traditionally in healthcare literature, we prefer adherence to imply a more active role of the patient in medication management and this is also the preferred term in recent literature [8,24,26]. We focus on how to improve medication adherence for people who are staying at home, and not in a specialized care center (nursing homes and assisted living) where medications are professionally managed. The complex and multifaceted nature of medication adherence presents several critical challenges for healthcare professionals, patients, caregivers, and health insurance providers:

• Challenge 1: Evaluating the current level of medication adherence.

• Challenge 2: Improving the level of medication adherence.

• Challenge 3: Maintaining the level of adherence for long-term or chronic conditions.

Generally, the approaches used for evaluating the current level of adherence are indirect such as self-reporting and pill counting and direct such as specimen testing. The indirect approaches lead to an overestimation of adherence, while direct approaches are expensive and prohibitive. Electronic monitoring of medication usage has been suggested [9,24,26], but challenges such as correctness of monitoring, usefulness for patient with social and travel commitments, and veri<sup>fi</sup>cation that the patient has actually ingested the correct drug or correct dose need to be addressed [40].

In general, 80% medication adherence is considered satisfactory; however a higher level may be needed for some conditions, such as 95% for HIV medications [26]. Considering the current levels of adherence of 50–60%, one of the healthcare “grand challenges” is to improve medication adherence by 20–30% [40]. Some people, especially the elderly, suffer from the limitations of memory, cognition, and dexterity [21] and their adherence to medications is critical in improving health outcomes and/or management of chronic conditions. The cognitive load refers to load on working memory [6,36], also relates to the number of units of information that can be retained before information loss occurs. There are three types of cognitive loads: intrinsic, extraneous, and germane. Intrinsic load deals with the inherent technical dif-<sup>fi</sup>culty associated with a task. Extraneous load is generated by the manner in which information is presented. Germane load relates with the processing, construction and automation of schemata [36]. The goal is to minimize intrinsic and extraneous cognitive load by reducing the dif<sup>fi</sup>culty of tasks and improved presentation of information. Cognitive processes, such as those dealing with comprehension, inference, decision-making, planning and learning, affect medication adherence in multiple ways (a) the inability to remember due to cognitive de<sup>fi</sup>cits could lead to lower adherence, (b) the presence of distractions (more pleasant) could affect adherence to medications, and (c) the feeling of being overwhelmed due to reduced working memory in managing daily activities, health advice and adherence to multiple medications.

In healthcare research, several interventions to improve medication adherence have been proposed [8,10,24,26], however the effective interventions have been complex and expensive [24]. This paper presents a smart medication system to provide several interventions to be used individually or in combinations for improving long-term medication adherence.

## 1.1. Related work in interventions

The adherence to medication regimens has been monitored since the time of Hippocrates, when “the effects of various potions were recorded with notations of whether the patient has taken them or not” [26]. Since then the technologies for medication adherence have certainly evolved. Currently, medication adherence ranges from using sticky notes, organization of medications in special boxes, and reminders from healthcare professionals. Some patients devise their own medication management systems using the spatial features of their homes, their daily routines, and how and when they visit certain places in their house to help remember to take medications [27].

The adherence is higher for patients with acute conditions as compared to chronic conditions [26]. The people aged 70 and older have the lowest level of adherence and cognitive reasons have been shown to be primary factors [8]. The compliance is lowest when the condition is prolonged as in chronic diseases and/or when the consequences of stopping treatment are delayed [9]. The complexity of factors that play a role in medication adherence needs to be identi<sup>fi</sup>ed [24]. The adherence was lower for psychiatric patient and higher for patients with physical disabilities caused by disease [24]. A classi<sup>fi</sup>cation of various factors behind low adherence into patient factors: memory, cognition, and dexterity, low health literacy, suboptimal beliefs about disease or medications, and concerns about side effects; provider factors: communications skill and complexity of prescribed regimen; and healthcare system factors: cost, restrictions, coverage, access to care, complexity of navigating the medical and pharmacy systems can be found in [21]. For elderly, the attention/concentration and memory were related to medication planning accuracy, while motor dexterity and strength were related to the ability to access medications. The visual perception and memory were the skills most strongly correlated with medication adherence [14]. These are quite different from challenges faced by the pediatric population in medication adherence [10].

Differential diagnosis of non-compliance should lead to interventions that target speci<sup>fi</sup>c causal factors thought to be operative in the individual patient [9]. The interventions identi<sup>fi</sup>ed are (a) reminders, (b) reduced complexity of regimens, (c) family and social support, and, (d) quality of therapeutic alliance. The others are reinforcement, education and behavioral tailoring [9]. The interventions that were effective for long-term care were complex including (a) more convenient care, (b) information, (c) counseling, (d) reminders, (e) self-monitoring, (f) reinforcement and rewards, (g) family therapy, and (h) additional supervision/attention [24]. It has been identi<sup>fi</sup>ed that the successful interventions are complex and costly [26]. The identi<sup>fi</sup>ed interventions are patient education, improved dosing schedules by “more forgiving” (largest drug-life) drugs whose ef<sup>fi</sup>cacy will not be affected by delayed or missed doses, and customizing to the patient's lifestyle including reminders [26]. For cardiovascular medication adherence in the elderly, the interventions identi<sup>fi</sup>ed are (a) simplify regimen and using special packaging, (b) adherence monitoring and feedback to the patient, and (c) personalized education and counseling [21]. In a systematic review of medication adherence in the elderly, the multifaceted and tailored interventions were shown to improve adherence more successfully than single interventions [38].

The adherence decreases as complexity, cost and duration of regimen increase, and more speci<sup>fi</sup>cally, changes in dosing schedules are effective if reduction in dosing frequency is possible [3,24]. It has been shown that the adherence is inversely proportional to the frequency of dose [13,26]. The telephone linked reminder system produced the most striking effect in improving adherence [38].

In general, almost all of the proposed interventions can be classi<sup>fi</sup>ed among three classes:

1 Patient support/motivation: this includes support from family, friends and society, and healthcare professionals to increase patient's motivation in maintaining a level of medication adherence. The motivation could also come from the incentives from insurance companies (waiving of premiums, reduction of cost of devices), healthcare professionals (reduced number of visits), and family members (visits, vacations).

2 Reminders: this includes many different ways to remind patients to take their medications at certain times. The proposed systems include telephone, on-line and in-person reminders.

3 Improved scheduling: this includes adjusting medication doses to patient's speci<sup>fi</sup>c limitations. This could include prescribing medications that have longer half-life to allow for fewer doses per day (may work for some medications only) or giving stronger doses fewer times a day (depending on the patient's ability to tolerate such doses).

Recently, information technologies have been proposed for implementing interventions for medication adherence, where patients can be reminded to take their medications at certain times. The implementation is usually a pill container (Fig. 1) with alarms that go-off at certain times and the pill container remembers how many times it has been opened and closed. Such reminders along with reminders from family members and healthcare professionals could increase the adherence to medications, especially for patients with cognitive and/ or physical disabilities.

![](/api/attachments/89QVW3QH/fulltext/images/5410feceb9536d3654c9d9b107d7057ea7fb26c6fd492288813edbe2c5f75783.jpg)  
Fig. 1. A reminder-based medication system

Medication systems such as pill containers with alarms that go-off at certain times include Magic Medicine Cabinet (MMC), which enables reminding, vital signs, and interaction with healthcare professionals [42]. Smart Medicine Cabinet uses RFID tags to monitor medication boxes and to communicate with a cell phone [31]. Smart Medicine Cabinet also supports reminders, query for contents (medications), expiry date detection, and medication recalls. The limitations of such systems include potential for reduced adherence due to restrictive and in<sup>fl</sup>exible operation, the total cost, and, dif<sup>fi</sup>culty in use with changes in schedule and travel. Any failure or inaccessibility to such system could lead to the patient missing an important dose, thus medication systems should support switching to a manual operation and provide other backup measures to help patient comply with medications. The systems described above are not portable, thus are very limited for patients with varying social and travel schedules.

## 1.2. Requirements of smart medication systems

To address above de<sup>fi</sup>ciencies, smart medication systems should be designed and evaluated. The requirements are (a) to be portable to support travel and social commitments, (b) to be context-aware of its surroundings and patient's activities [4,7], (c) to generate personalized reminders to patients and communicate as necessary, (d) to monitor vital signs of patients, (e) to monitor patient's adherence and (f) to communicate with healthcare professionals as necessary. More speci<sup>fi</sup>- cally, context-awareness implies that the system utilizes various information related to patient's conditions, medications, activities and actions in performing its own set of functions. This could lead to more intelligent and effective actions from the medication systems.

Such systems should also be evaluated by using one or more adherence models, multiple metrics, and several important features including those related to multiple interventions, addiction and overdose monitoring, and patterns of medication adherence should be modeled and evaluated (Fig. 2). The insights obtained from such evaluation can then be incorporated in (re)design of smart medication systems. The proposed smart medication management system (SMMS) is designed to address these requirements.

## 1.3. Our approach and contributions

Broadly, the research question is how information systems can mediate adherence to medication regimen. More speci<sup>fi</sup>cally, we are interested in: how to design, model and evaluate smart medication systems which can support multiple interventions for improving medication adherence. Our approach includes (a) communication with patients, (b) monitoring of medication consumption, and (c) context-sensitive reminders to patients. Additionally, the proposed medication system results in some reinforcement and rewards for improved adherence such as a reduced number of visits to healthcare professionals. Therefore, the proposed SMMS can be used to support and evaluate single as well as “composite” interventions for medication adherence. SMMS can communicate with healthcare professionals and then dispense doses according to “improved scheduling”. It can also communicate with the family members and friends of the patient and receive messages to improve patient's motivation for adherence.

The major contributions of this paper are (a) design and operation of Smart Medication Management System, (b) development of an analytical model for SMMS and multiple interventions and (c) detailed performance results on interventions and improvements in overall healthcare of patients. The paper is organized as follows. In Section 2, we present health promotion model and the model used in the study for medication adherence. In Section 3, we present details of smart medication management system (SMMS). This includes the operation of SMMS and its components, and how it can be used to implement multiple interventions to improve medication adherence. By analyzing the patterns of medication use, SMMS can also be used to predict and avoid medication overdose. The modeling, presented in Section 4, addresses multiple interventions for medication adherence. The results in Section 5 show that although all three interventions can improve the level of medication adherence, context-aware reminders are capable of achieving the highest level of improvement. This section also shows how different interventions can be combined to create very powerful “composite” interventions for highest improvements in medication adherence. Finally, some concluding remarks are made along with future directions of this research in Section 6.

## 2. Theoretical background and adherence model

Health promotion model [28] is used to study adherence to medication. The HPM de<sup>fi</sup>nes health as a positive dynamic state and not merely the absence of disease. The model focuses on individual characteristics and experiences, behavior-speci<sup>fi</sup>c cognitions and affect, and behavioral outcomes (Fig. 3). The health promotion model notes that each person has unique personal characteristics and experiences that affect subsequent actions. The set of variables for behavioral speci<sup>fi</sup>c knowledge and affect has important motivational signi<sup>fi</sup>cance. Health promoting behavior is the desired behavioral outcome and is the end point in the model. The <sup>fi</sup>nal behavioral demand is also in<sup>fl</sup>uenced by the immediate competing demand and preferences, which can derail an intended health promoting actions. Our current work deals with several different parts of health promotion model. One of the most exciting insights is how medication management systems could affect the health promoting behavior using many of the constructs of HPM (Fig. 3). More speci<sup>fi</sup>cally, context-aware reminders are part of situational in<sup>fl</sup>uences, while family members, relatives and caregivers are used to provide interpersonal in<sup>fl</sup>uences to increase health promoting behavior, which may result in adherence to medications. We observe that elderly have fewer competing demands, which will positively affect the health promoting behavior, which in turn may increase adherence to medication. The reduction in perceived barriers improves health promoting behavior [28]. The perceived barriers, especially structural barriers, are shown to be highly signi<sup>fi</sup>cant in elderly women [20]. This could include improved packaging and detailed information on medications. The perceived bene<sup>fi</sup>ts are shown to be signi<sup>fi</sup>cant in various health actions, such as use of hearing protection [15]. The perceived self-ef<sup>fi</sup>cacy has been shown to be a strong predictor of healthy behavior such as exercise for even trained healthcare professionals [29]. The system promotes perceived self-ef<sup>fi</sup>cacy for the patient by showing the patient how to use the system. The interpersonal in<sup>fl</sup>uences lead to a higher level of health promoting behavior [45]. Thus, medication system should facilitate suitable reminders/ alerts for patients from family, caregivers, and healthcare professionals.

![](/api/attachments/89QVW3QH/fulltext/images/0cd069f0619f22451b9c36208046a7ac5f7d861ef2e50a097884fc3d590cec3c.jpg)  
Fig. 2. Design and evaluation requirements of Smart Medication System.

![](/api/attachments/89QVW3QH/fulltext/images/db488f6600644052a16400f3fba41929998a24cae7b810b31ff8cb5f5522131a.jpg)  
Fig. 3. The Health Promotion Model.

As part of the interpersonal in<sup>fl</sup>uences, reminders are effective in improving medication adherence. In a systematic review of multiple randomized controlled trials (RCTs), it is shown that reminders along with other interventions, lead to positive effects on medication adherence [24]. The reminders may also help patients with cognitive limitations and/or forgetfulness, known as number one factor in polling of patients, in taking their medications [26]. The adherence has been found to be lowest in people over 75, where cognitive decline due to aging and cognitive side effects due to certain medications play a major role in medication planning and consumption [8].

In a systematic review of multiple studies, people with better social support were likely to have more positive attitudes towards their medications. Also, the patients living with their family or whose medications were supervised by family members were more likely to be adherent [9].

Various studies using self-report and pill counts have established the inverse relationship between number of daily doses and medication adherence. Using electronic monitoring, the compliance is shown to be decreasing with increased number of doses [5]. The mean compliance rates found were 79% for 1 dose/day, 69% for 2 doses/day, 65% for 3 doses/day and 51% for 4 doses/day. Additionally, the number of different medications taken by patient is shown to negatively affect the compliance rate [14]. In a large study, the patients taking six or more medications were twice as less compliant as patients taking two medications [2]. Improved scheduling by reducing number of doses/day and/or multiple medications per dose can thus improve the medication adherence.

## 2.1. The medication adherence model

Based on the above discussion and literature, a model for medication adherence is shown in Fig. 4. The personal characteristics and abilities include the patient's motivation and cognitive abilities which affect the planning and taking medications as prescribed. The duration and type of illness are shown to affect adherence for chronic diseases after 6 months, where it can drop to 50%. The three interventions we focus on, both individually as well as in various combinations, are shown as motivation and support from family and healthcare professionals, improved scheduling of medications by reducing the frequency of doses, and reminders. These factors are included in the design of SMMS, which implements several interventions as needed for a patient. Based on the model, several metrics are identi<sup>fi</sup>ed for modeling including self medication level, the number of medications to be taken, the number of medications that can be combined for better scheduling, the number of reminders needed, the level of support from family, and the adherence level (fraction of times the correct dose is taken) for single and multiple medications.

## 2.2. The design science approach

For developing Smart Medication Management System, we utilize a design science approach [12,17,22,23,30,37,38,39,41]. Design can be thought of as a mapping from function space (functional requirements as points) to attribute space (artifacts satisfying the mapping as points). Design is the knowledge in the form of techniques and methods for performing this mapping or the knowhow of implementing an artifact that satis<sup>fi</sup>es a set of functional requirements [37]. Using the design guidelines [12], we develop an artifact and evaluate its effectiveness.

![](/api/attachments/89QVW3QH/fulltext/images/c0c93cf4e86dccc04f3a3d20e7a7f8830fe11b6dac6398bda6d2283c1c103ff9.jpg)  
Fig. 4. The identi<sup>fi</sup>ed interventions and their relationships with medication adherence

This is an expanded version of the approach proposed by [37] as it derives requirements for the design and artifact (Fig. 5).

Using the above design science approach, we derived requirements for an artifact that we developed to study medication adherence. The requirements are that SMMS:

(a) To be portable to support travel and social commitments.

(b) To be context-aware of its surroundings and patient's activities [32].

(c) To generate personalized reminders to patients.

(d) To communicate and provide support to patients.

(e) To monitor patient's adherence.

(f) To communicate with healthcare professionals as necessary, especially for improving scheduling.

(g) To implement single and composite interventions for patients.

The design process was iterative and the artifact is a medication monitoring system which can implement one or more interventions as needed to improve medication adherence. The performance of artifact was measured using an analytical model, developed in the paper, and we found that the artifact enhances the adherence to medications. Based on this, several improvements in SMMS design and operation were identi<sup>fi</sup>ed and implemented.

## 3. Smart medication management system (SMMS)

## 3.1. Smart monitoring

It can be facilitated by technologies that can sense and act, communicate, reason, and interact with people. Smart monitoring involves measuring multiple parameters simultaneously over a long-term without disturbing the daily lives of the patients. This can be facilitated by using health monitoring devices inside patients (implanted), over patients (wearable), near to patients (portable) and around patients (environmental) [40]. The examples are implanted sensors, Smartshirt, hand-held devices, and smart environments such as smart house [35]. Wearable sensors are better suited for monitoring vital signs by attaching themselves on the patient's body directly or as a part of clothing (Fig. 6). The sensors could form a body area network and may communicate directly or via a designated sensor to a device such as PDA or cell-phone [34,39]. The use of multiple sensors could overcome errors of measurement and/or malfunction due to rare failures. The requirements of wearable sensors are reliability, robustness, and durability; unobtrusive; able to identify users; communicate with other sensors and devices; and minimal maintenance and fault recovery [16]. For implementation, a combination of wearable and environmental sensors will be more practical for improved reliability of monitoring as well as comprehensive monitoring with more detailed information. The smart monitoring system should operate autonomously without requiring intervention. The monitoring devices [19,33,39,44] can be wearable or hand-held depending on the level of dif<sup>fi</sup>culty in use, portability, and the type of disability for the monitored patient.

![](/api/attachments/89QVW3QH/fulltext/images/ac923ab95361aecd39c7f7d15fc584821f61a9c133b71ea85dfd309176771133.jpg)  
Fig. 5. The design science approach.

![](/api/attachments/89QVW3QH/fulltext/images/b1b9c4002c8457676b45a8792625c1f2e8feb1919f82c3e7dfdd6cde0391fd26.jpg)  
Fig. 6. Smart Monitoring using Sensors.

## 3.2. Smart medication systems

Smart medication management can be performed by systems that can detect, process, and use context-awareness in creating suitable actions including reminders to patients. Such systems can compensate for de<sup>fi</sup>cit of cognitive abilities of the elderly. As shown in Fig. 7, the vital signs and health parameters are obtained and current context of patient is generated by either wearable, portable or environmental technologies [11]. The healthcare professionals collaborate with one another and decision making system, which then interact with medication management system to interact with the patient in the form of contextaware reminders/alerts for higher adherence. The system also provides context-sensitive information to assist the cognitive process involved in interacting with the system, obtaining and ingesting the medication(s). For example, the patient may need help in remembering what medications have to be taken, what dose, when and how. In cases of missed or delayed doses, the system processes on its own or in some cases with the help of a healthcare professional on what needs to be done. The resulting actions could be to either vary the timing and quantity of left-over doses or skip the dose in the worst case if variations are not possible and it is medically safe.

## 3.3. The design of SMMS

The designed system is a smart system and has features and functions that would assist in increasing the adherence to medications. More speci<sup>fi</sup>cally, it meets the requirements for medication management as derived earlier and supports a range of computing and communication technologies such as sensors, radio frequency identi<sup>fi</sup>cation (RFID), Bluetooth, wireless LANs, and wide-area networks. It supports the use of several networks that can be formed among SMMS, radioenabled devices and sensors for enhancing the quality and reliability of adherence monitoring. The adherence data is derived from multiple sensors to improve the reliability of the system by selective integration or weighted averaging of data. Also, any entered data by the patient can be accepted after veri<sup>fi</sup>cation from healthcare professionals. This will help in overcoming any errors due to incorrect generated data from sensors as part of regular operation or rare malfunction.

![](/api/attachments/89QVW3QH/fulltext/images/ef2faf5fb29cf2536ba391328ec0fc9326bbb5302de180814e21f3c540bfa11c.jpg)  
Fig. 7. Smart medication systems.

Wireless networks allow the SMMS to interface with EMR and m-prescriptions for improving the patient safety, and adherence monitoring using Bluetooth and sensors, and noti<sup>fi</sup>cations to physicians (Fig. 8). The use of SMMS in multiple interventions for adherence is shown in Fig. 9. This includes reminders, improved scheduling of medications, and support from family and healthcare professionals. SMMS allows the selection of most suited individual or composite intervention for a patient in collaboration with healthcare professionals. As shown in Fig. 9, it supports dispensing of medications and also senses various actions of the patients related to medication adherence.

SMMS can be in multiple states: informing (about medication), guiding/assisting (on how to take medications), verifying (the medication is taken), negotiating (with HP on changes), monitoring (the adherence), and processing (schedules of medications) as shown in Fig. 10. Using these states, it can implement the selected intervention for the patient. The various functions of SMMS are shown in Fig. 11. This includes getting information on medications and doses, authorized people to be noti<sup>fi</sup>ed, the duration and type of monitoring, managing network connectivity among others. SMMS contains various prescribed medications and doses and will dispense these to the patient as necessary at certain times as programmed by healthcare professionals. It keeps tracks of actual times when these doses are consumed by the patient for computing patterns of medication adherence. In some implementations, where patient's travel support is turned on, SMMS will allow more <sup>fl</sup>exibility on timing of doses, but will still perform other functions as programmed. A simple SMMS algorithm is shown in Fig. 12. The access to EMR by SMMS is shown in Fig. 13. Depending on the implementation, it can also search for similar medications in its surroundings and can monitor any “attempts” by the patient to open its door at times when no medication is scheduled [40].

## 3.4. The operation of SMMS

SMMS also implements interventions, decided by healthcare professionals, as simple as monitoring of medication usage and sending reminders to more complex monitoring of medication usage with interactions from healthcare professionals (HP) as shown in Fig. 14. It generates reminders based on schedule of medications and overall medication adherence goal; location, activities, and current health conditions of the patient; and any special instructions (Fig. 14). The current health conditions can be measured using wearable sensors by attaching them on the patient's body directly or as part of smart clothing. By working with healthcare professionals and patients, SMMS is able to provide highly personalized service to the patient and thus is capable of achieving high levels of medication adherence. SMMS can also be programmed to process any drop in the current level of adherence to suggest change in the intervention. For example, if the patient's adherence drops, and SMMS detects a change in patient's travel, then more <sup>fl</sup>exible timing can be used to allow the patient to continue medications. The most suitable type of reminders can be utilized based on patient's condition and her surroundings.

![](/api/attachments/89QVW3QH/fulltext/images/c67d27cd66512326474d7eae3c882ed2aedfc0fbcc261322998126bf0fc48e7c.jpg)  
Fig. 8. Smart medication management system (SMMS).

![](/api/attachments/89QVW3QH/fulltext/images/5fe9efbbd842e26f9b94c47c8722346c0d10e5bcb9a83b21729570f3af3267eb.jpg)  
Fig. 9. SMMS and multiple interventions for improving medication adherence

SMMS utilizes a context-sensitive operation. The design of contextgeneration protocols employs the rule-based method, where a set of rules is speci<sup>fi</sup>ed based on logical connections among vital signs, patient's history and available information. The context-generation protocols are stored and processed in monitoring devices that a patient can carry or wear as a part of smart clothing. The context-generation protocols are designed to assist and not replace the medical decision making by healthcare professionals. Therefore, if the context is incorrect or there is a problem, the monitoring system would allow the healthcare professional to request more information and make a better decision. The context-generation protocols process information in deriving the patient's context and needs. Relevant information is transmitted along with context (Fig. 15). Available information on patient's activities, medical history, and rate of change of vital signs is included along with their relative weights personalized to the patient, which are used to create smart context-sensitive monitoring.

To ensure that the patient has consumed the dispensed medication, swallowing detection sensors can be employed in future [1]. The sensors communicate with the SMMS sensed parameters to indicate that the patient has swallowed the medication to improve the monitoring accuracy [1]. The SMMS could be combined location tracking (patients, services, hospitals, and healthcare services) and remote-help systems (emergencies, hospitalization, police, ambulance). It can also be expanded to act as cognitive assistant (who they are, where they are, and what they are, where they are, and with whom they are) [40]. The context-aware reminders can be sent to the patient on devices such as display screens, cell phones, computers and simple audible alarms where three colorcoded reminders are used (Fig. 16).

![](/api/attachments/89QVW3QH/fulltext/images/5f4e37aa8ce9bf7ccbc01b6ff7193bc333f8e044629b6d7e7e813203d519a830.jpg)  
Fig. 10. Various states of SMMS for multiple interventions.

## 4. Analytical modeling

Several different adherence models could be employed covering a range of patients, from teenagers to geriatric patients, in youth care, home care, assisted living and nursing homes to validate SMMS. The adherence models could include complete-self-care, assisted-care, and complete-dependent-care to cover scenarios of levels of control over consumption of prescription medications. In addition to validation and evaluation, daily, weekly and long-term adherence can be measured to provide more detailed insight in the medication usage patterns. The number of messages over wireless networks can also be measured to study potential overhead and complexity, and could be employed in future SMMS design improvements.

We evaluate the performance of several interventions by SMMS by using analytical modeling. Analytical models are mathematical models

![](/api/attachments/89QVW3QH/fulltext/images/768bbbe9c9b62ebab92d30409ab29c1823dd594bbf1f52123da46260a047e0c0.jpg)  
Fig. 11. The functions and decisions to be made by SMMS

Step 1: If time for a dose and not taken yet Generate a context-aware-reminder in T seconds Display any messages from HP and/or family Dispense a dose if user is ready

Step 2: While dose not taken and still ok to take The number of reminders less than the limit Generate a context-aware-reminder Inform healthcare professional

Step 3: If dose-change = Yes Dispense the dose at scheduled time (go to step 1) Else add to the number of missed doses (go to step 1)

Fig. 12. A simple algorithm for SMMS.

with a closed form solution, where a set of equations is developed and utilized to study the behavior and changes in a system. In the design of computing and communications systems, such models have been used for a long time due to their ability to express complex relationships among many variables or behavior of interests. One of the challenges has been the level of complexity in developing models and subsequent computations, and models of reasonable complexity have been introduced to provide accurate results. Therefore, for evaluation of interventions for medication adherence, mathematical models are both suitable and desirable. More speci<sup>fi</sup>cally, we measure the impact of various designed solutions and effect of multiple interventions on the level of achievable medication adherence.

The model is developed using relationships among several independent (input) variables and dependent (output) variables. As there has been little work on medication systems, no metrics are available for evaluation. The following metrics can be used for measuring the effectiveness of systems for medication adherence:

• The adherence level (fraction of times the correct dose is taken) for single and multiple medications

• The number of medications that can be combined for better scheduling

• The number of reminders needed

• The level of support from family

![](/api/attachments/89QVW3QH/fulltext/images/1ae4489e23108e38c9a7a0eb690e826e7ad8e2bf3ea01eb82952dcc4ca9f351e.jpg)  
Fig. 14. Various actions and responsible parties.

## 4.1. Assumptions

Several assumptions were made to keep the analytical model tractable and reasonably accurate. These assumptions could be relaxed in future work.

• Assumption 1: All medications are treated similarly except those that have inter-dependent relationships. In our model, speci<sup>fi</sup>c characteristics of doses are not modeled for keeping the complexity of our model at a reasonable level.

• Assumption 2: The model assumes that patients are adults and live in independent living and are able to self-medicate as prescribed. The model can be extended to cover adults and children in other surroundings.

• Assumption 3: The model assumes that patients are either compliant or semi-compliant so one or more interventions can be applied. The model can be extended to non-compliant patients in the future.

![](/api/attachments/89QVW3QH/fulltext/images/7989fe95a949c781ab5c315dcb56b3fc8a9dff05c5be0fdb6a0ca67746833781.jpg)  
Fig. 13. Accessing EMR for medication information by SMMS

![](/api/attachments/89QVW3QH/fulltext/images/1a0a3281717b656dcc46712a87b8dabd06985a092da5d6e26f693006a4c8f491.jpg)  
Fig. 15. Operation of SMMS for medication adherence.

## 4.2. Strengths

The model is capable to deriving the level of medication adherence by individual patients. The model can process various probabilities of events and failures of systems, level of cognitive load, types and number of reminders, and multiple factors that may affect medication adherence. The model is also used to compare multiple proposed interventions paper. The model is applicable to patients who are taking medications on their own in independent living. Also, the model is suitable in studying medication. adherence in chronic illnesses, where multiple medications are used over an extended period of time.

## 4.3. Limitations

The model is primarily designed to address medication adherence in independent living, and will need extensions before its use in other more controlled environments such as assisted living and hospitals. The model is designed to provide results with reasonable complexity, and in some cases more re<sup>fi</sup>ned results may be obtained by developing signi<sup>fi</sup>cantly more complex models.

## 4.4. Validation of the model

The model was tested for many known cases to verify its correct functioning. This includes simple test cases where patterns and characteristics can be easily derived or are well known. Under its given set of assumptions, the model produces a reasonably accurate set of results. All major relationships were validated from multiple studies reported in the literature. These include the positive impact of reminders on medication adherence as shown in a systematic review of multiple randomized controlled trials or RCTs [24], the positive impact of reminders for patients with cognitive limitations and/or forgetfulness, more positive attitudes towards medications for people with better social support as shown by a systematic review of multiple studies [9], and reduced compliance with increasing number of doses per day [5] where improved scheduling by reducing number of doses/day and/or multiple medications per tablet can improve the medication adherence. More speci<sup>fi</sup>cally, the output of the model was compared against the historical data presented in [5]. The mean compliance rates found were 79% for 1 dose/day, 69% for 2 doses/day, 65% for 3 doses/day and 51% for 4 doses/day. In a large study, patients taking six or more medications were twice as less compliant as patients taking two medications $[ 2 ] .$ This data matches well with the data from our model. With such validation, our model can then be used to estimate the impact of individual interventions, composite interventions and savings associated with improved medication adherence.

## 4.4.1. General medication adherence

The medication adherence during an observed period can be given by

$$
= \left(\mathrm{N} _ {\text { taken }} / \mathrm{N} _ {\text { pres }}\right) \times 1 0 0 = \left(\mathrm{N} _ {\text { taken }} / \left(\mathrm{N} _ {\text { taken }} + \mathrm{N} _ {\text { left }}\right)\right) \times 1 0 0\tag{1}
$$

where $\mathrm { N } _ { \mathrm { p r e s } }$ is the number of prescribed doses and $\Nu _ { \mathrm { t a k e n } }$ is the number of doses taken by the patient. The adherence can have any value between 0 and 100% (both included). For co-dependent medications, where if medication A is not taken then medication B should not be taken either, $\mathrm { N _ { l e f t } }$ includes both unintentionally and forced missed doses as follows:

$$
\mathrm {N_ {left} = N_ {u - missed} + N_ {f - miss}}.
$$

The time variations between doses are also important. Some patients may take multiple doses to catch-up the missing or delayed doses. To <sup>fi</sup>nd this, the number of times the gap between doses has exceeded the max-interdose-time, or $G _ { \mathrm { M } }$ can be given by

$$
G _ {M} = \sum_ {I = 1} ^ {N _ {p r e s}} \left(\left(T _ {I + 1} - T _ {I}\right) > T _ {m a x}\right)\tag{2a}
$$

where $\operatorname { T } _ { \operatorname* { m a x } }$ is the maximum allowed time between two doses to remain medically compliant. The value of $G _ { \mathrm { M } }$ can be used to determine the number of times the patient has skipped or delayed a medication. Each value of $\left( \mathrm { T } _ { \mathrm { I } + 1 } - \mathrm { T } _ { \mathrm { I } } \right)$ that exceeds three days will indicate “medication holiday”, an observed phenomenon in patients with poor adherence [8,24,26]. Also, the number of times the gap between doses is less than the minimum-interdose-time, or $\mathsf { G } _ { \mathrm { L } }$ can be given as

$$
G _ {L} = \sum_ {I = 1} ^ {N _ {\text { pres }}} \left(\left(T _ {I + 1} - T _ {I}\right) <   T _ {\min}\right)\tag{2b}
$$

![](/api/attachments/89QVW3QH/fulltext/images/aa3f3e413b80499ba488ff7e503d68c541d52a63984cccc9f99e573954709a14.jpg)

![](/api/attachments/89QVW3QH/fulltext/images/1576ba06d4ca096d618a217597a9a571634714cb07c7a56293ad0eb164d9c54c.jpg)  
Fig. 16. Display of context-aware reminders.

![](/api/attachments/89QVW3QH/fulltext/images/916b211250b1b0baf05a07b759dde739e65a48fb6e40237d4ab2df0e64975eec.jpg)

where $ \mathrm { T } _ { \mathrm { m i n } }$ is the minimum allowed time between two doses to remain medically compliant. The value of ${ \bf G } _ { \mathrm { L } }$ can be used to determine the number of times the patient has overdosed or attempted a catch-up on a medication. Multiple neighboring values of $( \mathrm { T } _ { \mathrm { I } + 1 } - \mathrm { T } _ { \mathrm { I } } )$ would indicate “medication addiction”, another observed phenomenon in patients taking medications with potential for addiction [8,24,26].

## 4.4.2. SMMS characteristics

The end-to-end reliability of SMMS can be given as

$$
= 1 - \left(1 - P _ {c}\right) ^ {a} \left(1 - P _ {p}\right) ^ {b} \left(1 - P _ {n}\right) ^ {c}\tag{3}
$$

where $\mathrm { P _ { c } }$ is the probability of accurate collection of information (sensing), $\mathrm { { P _ { p } } }$ is the probability of correct processing, and $\mathrm { { P _ { n } } }$ is the probability of message delivery over the network. The values of $\mathsf { a } ,$ b and c represent the number of ways something can be performed.

The average probability of access to a network is the same, however the number of networks that can be accessed could be different thus resulting in a different overall probability of network access. $\mathrm { P _ { i } }$ is the overall probability of network access and can be simpli<sup>fi</sup>ed as

$$
P _ {i} = \sum_ {R = 1} ^ {N} C _ {R} * (P _ {N}) ^ {R} * (1 - P _ {N}) ^ {N - R}.\tag{4}
$$

The effectiveness of context generation can be measured by the overall probability of correct diagnosis expressed as

$$
\mathrm{P} _ {\mathrm{CD}} = \left(\mathrm{P} _ {\mathrm{CD-A}} \cdot \mathrm{P} _ {\mathrm{A}} + \mathrm{P} _ {\mathrm{CD-B}} \cdot \mathrm{P} _ {\mathrm{B}}\right) / \left(\mathrm{P} _ {\mathrm{A}} + \mathrm{P} _ {\mathrm{B}}\right)\tag{5}
$$

Where $\mathrm { P _ { A } }$ and $\mathrm { P _ { B } }$ are the probabilities of events A and B, respectively. $\mathrm { P _ { C D - A } }$ PCD-A and $\mathrm { P _ { C D - B } }$ are the probabilities of correct diagnosis when events are A and B, respectively.

$$
P _ {C D - A} = \left(\sum_ {I = 1} ^ {N} (W _ {I} \cdot P (C _ {I} > T _ {I})\right) - \sum_ {J = 1} ^ {N} \left(\left(W _ {J} \cdot P \left(C _ {J} > T _ {J}\right)\right)\right) / \sum_ {I = 1} ^ {N} (W _ {I} \cdot P (C _ {I} > T _ {I})).\tag{6}
$$

Where W represents the weight given to attribute I and $\mathrm { P } ( \mathrm { C } _ { \mathrm { I } } { > } \mathrm { T } _ { \mathrm { I } } )$ is the probability that value of attribute I is more than the set threshold for attribute I. The choice of weights (or points) and setting of patientspeci<sup>fi</sup>c thresholds will improve the overall probability of correct diagnosis from the scheme.

The weighted score for multiple factors can be expressed as

$$
S _ {t o t} = \sum_ {I = 1} ^ {M} \left(W _ {i - o p t} + E _ {i}\right) (S _ {i} + e _ {i})\tag{7}
$$

where ${ \mathsf { W } } _ { \mathrm { i - o p t } }$ is the optimal weight for ith factor and $\mathrm { E _ { i } }$ is the error introduced (difference between assigned weights and optimal weights). S is the value of ith symptom and $\mathsf { e } _ { \mathrm { i } }$ is the introduced error due to measurement and processing. The values of two errors will decide the levels of false positives and false negatives. In general, these errors may cancel out leading to accurate diagnosis, if both are positive, the results will have higher false positives. If both are negatives, the results will have more false negatives.

## 4.4.3. Modeling of reminders

The level of medication adherence has been shown to improve by reminders [24] and especially for patients with cognitive limitations and/or forgetfulness [9]. In general, the medication adherence is dependent on the patient's ability to take his/her medication (self medication), the effectiveness of SMMS to detect, process, and transmit set of actions, and the effectiveness of the reminders to the patient.

Therefore, the daily medication adherence due to reminders can be given as

$$
M A = (1 / M) \sum_ {j = 1} ^ {M} \left(P _ {j} + \left(1 - P _ {j}\right) \sum_ {i - 1} ^ {N} \left(\left(D _ {i j} \cdot R _ {i j}\right) \prod_ {r = 1} ^ {i - 1} \left(1 - D _ {i j} \cdot R _ {i j}\right)\right) \right.\tag{8}
$$

where $\mathrm { P _ { j } }$ is the probability that patient took the jth medication as scheduled, $\mathrm { D _ { i j } }$ is the probability that SMMS detects if the patient has not taken the jth medication on ith attempt from the system, $\mathrm { R _ { i j } }$ is the probability that for jth medication the ith action/reminder from SMMS is effective. M is the number of medication doses per day for the patient, and N is the number of reminders for a medication.

The desirable number of context-sensitive reminders can be computed as follows:

$$
\mathrm{N} _ {\text { desirable }} = \operatorname{Min} (\mathrm{N} _ {\min}, \mathrm{N} _ {\text { tolerable }})\tag{9}
$$

$ { \mathrm { N } } _ { \mathrm { m i n } }$ is the value of N to achieve a certain medication adherence and $\mathrm { N _ { t o l e r a b l e } }$ is based on cognitive load and cognitive de<sup>fi</sup>ciency, if any, for patients such as elderly and people with cognitive health problems.

## 4.4.4. Impact of number of medications

The medication adherence has been shown to be decreasing exponentially with an increased number of medications and/or doses [5]. Also, the patients taking six or more medications were twice as less compliant as patients taking two medications [2]. We can model the impact of number of medications on medication adherence using the probability that patient took all C doses on the kth day (without any reminders)

$$
= \prod_ {j = 1} ^ {C} \left(P _ {j k}\right).
$$

The improvement with fewer drugs and doses (totaling to C1) can be given as

$$
= \prod_ {j = 1} ^ {C 1} \left(P _ {j k}\right) - \prod_ {j = 1} ^ {C} \left(P _ {j k}\right).\tag{10}
$$

The value of $\mathrm { P _ { j k } }$ without any interventions varies from 50 to 80% [5]. For simpli<sup>fi</sup>cation, we could assume that $\mathrm { P _ { j k } = P _ { j + 1 \ k } }$ for all j, meaning the probability of taking any dose is the same throughout the day. Depending on the patient, this may decline slowly over time especially for chronic conditions.

## 4.4.5. Support from family and healthcare professionals

The support from family has been shown to improve the level of motivation a patient has towards taking the medications [28]. Also, more positive attitudes towards medications for people with better social support and therapeutic alliance are shown by a systematic review of multiple studies [9]. To model the improvement due to better support, we realized that there are two components to overall self-medication level, one based on the patient's characteristics [28] and another one due to the support from family and healthcare professionals. These two components are additive, but cannot exceed 100%, therefore, the following expression can be developed:

$$
\mathrm{P} _ {\mathrm{jk}} = \operatorname{Min} \left(\left(\text { Base } * \mathrm{E} _ {\mathrm{jk}} + \mathrm{C} _ {\mathrm{jk}} \cdot \mathrm{T} _ {\mathrm{jk}} \cdot \mathrm{M} _ {\mathrm{jk}}\right), 1\right)\tag{11}
$$

where Base is the inherent level of self-medication, ${ \sf C } _ { \mathrm { j k } }$ is the probability of SMMS functioning correctly, $\mathrm { T _ { j k } }$ represents the probability that required dose is available when needed including during travel, E represents the probability that patient's cognitive ability meets or exceeds the threshold for self-adherence, and $\mathrm { M _ { j k } }$ represents additional motivational factor. This includes social and family support and effective therapeutic alliance with a healthcare professional. For our independent living environment, the realistic ranges of these variables are Ba $\cdot { \mathrm { e } } = 0 \mathrm { t o } 1 , \mathrm { C _ { j k } } = . 8 \mathrm { t o } 1 , \mathrm { T _ { j k } } = 0 \mathrm { t o } 1 , \mathrm { E _ { j k } } = 0 . 4 \mathrm { t o } 1$ (age dependent), and $\mathrm { M } _ { \mathrm { i k } } { = } 0$ to 1. The actual values can be higher or lower for some very speci<sup>fi</sup>c cases.

## 4.4.6. Adherence due to composite interventions

The composite medication adherence is dependent on the patient's ability to take his/her medication (self medication), the effectiveness of SMMS, reminders, improved scheduling of medications, and the level of support from family and healthcare professionals. Therefore, the overall medication adherence due to composite interventions can be given as

$$
M A = (1 / D * M) \sum_ {k = 1} ^ {D} \sum_ {J = 1} ^ {M} \left(P _ {j k} + \left(1 - P _ {j k}\right) \sum_ {i = 1} ^ {N} \left(\left(D _ {i j k} \cdot R _ {i j k}\right) \prod_ {r = 1} ^ {i - 1} \left(1 - D _ {i j k} \cdot R _ {i j k}\right)\right) \right.\tag{12}
$$

where $\mathrm { P _ { j k } }$ is the probability that on kth day the patient took his/her jth medication as scheduled and it re<sup>fl</sup>ects both self-motivation and the support from family and healthcare professionals, $\mathrm { D _ { i j k } }$ is the probability that on kth day SMMS detects if the patient has not taken the jth medication on ith attempt from the system, $\mathrm { R _ { i j k } }$ is the probability that on kth day, for jth medication the ith action/reminder from SMMS is effective. Also, D is the duration for medication adherence, M is the number of medications per day due to improved scheduling, and N is the number of reminders for a medication.

$\mathrm { P _ { j k } }$ is dependent on patient's cognitive abilities, self-motivation, support from family and friends, medication availability, correct functioning of the medication systems including the level of dif<sup>fi</sup>culty in taking a medication. This is given in Eq. (11).

$\mathrm { D _ { i j k } }$ is dependent on sensors detecting the event correctly, transmission of messages, and correctness of algorithm, and thus given as

$$
D _ {i j k} = S _ {i j k} \cdot N _ {i j k} \cdot A _ {i j k}\tag{13}
$$

where $S _ { \mathrm { i j k } }$ is the probability that on kth day, ith event for jth medication was detected correctly by sensors, $\mathrm { N _ { i j k } }$ is the probability that the ith event for jth medication was transmitted correctly given the correct detection by sensors, and $\mathsf { A } _ { \mathrm { i j k } }$ is the probability that ith event for jth medication was processed correctly by the context-aware algorithm given both correct detection and transmission of the event. So, $\mathrm { N _ { i j k } }$ and $\mathsf { A } _ { \mathrm { i j k } }$ are conditional probabilities as if the detection is not correct then transmission and processing of events are not of any use. $\mathrm { R _ { i j k } }$ is dependent on the system's ability to reach patient when needed, patient's cognitive abilities, and cognitive load. This can be expressed as

$$
\mathrm{R} _ {\mathrm{ijk}} = \mathrm{W} _ {\mathrm{ijk}} \cdot \mathrm{E} _ {\mathrm{ijk}}\tag{14}
$$

where $\mathsf { W } _ { \mathrm { i j k } }$ represents the probability to reach the patient and $\mathrm { E _ { i j k } }$ represents the probability that patient's cognitive ability meets or exceeds to the threshold for self-adherence.

One way to evaluate $\mathrm { D _ { i j k } }$ is to compute false alarm rate [18]. The four variables used are TP (True Positive) when the patient takes medicine and system detects it correctly, TN (True Negative) when the patient does not take medicine and the system detects it correctly, FP (False Positive) when the patient takes medicine and the system fails to detect it, and FN (False Negative) when the patient does not take the medicine and system concludes that it has been taken. The four metrics of precision, sensitivity, speci<sup>fi</sup>city and false alarm [18] are:

$$
\text { Precision   or   Accuracy } = \mathrm{TP} / (\mathrm{TP} + \mathrm{FP}) (\text { maximize })\tag{15}
$$

$$
\text { Sensitivity   or   recall } = \mathrm{TP} / (\mathrm{TP} + \mathrm{FN}) (\text { maximize })\tag{16}
$$

$$
\text { Specificity } = \mathrm{TN} / (\mathrm{FP} + \mathrm{TN}) (\text { maximize })\tag{17}
$$

$$
\text { False   alarm } = 1 - \text { Specificity } = \mathrm{FP} / (\mathrm{FP} + \mathrm{TN}).\tag{18}
$$

The goal is to have zero false negatives and minimal number of false positives. Having both false positives and false negatives to be zero would require a system to be both highly sensitive and highly speci<sup>fi</sup>c in its operation, which is even harder to achieve in practice. The other desirable performance includes 100% correct decisions by context-aware systems, no errors in networks, and 100% correct medical decisions.

## 4.4.7. Saving due to Improved Adherence

The cost-saving due to improved adherence can be expressed as

$$
T _ {s a v} = \left(C _ {H} + L P _ {H}\right) \cdot R _ {H} - \left(C _ {S M M S} + C _ {c o m m} + C _ {t r a i n}\right)\tag{19}
$$

where $C _ { \mathrm { H } }$ represents the total hospitalization cost including related family expenses, $\mathsf { R } _ { \mathrm { H } }$ is the reduction in the number of hospitalization, LPH is the lost productivity per hospitalization, and ${ \mathsf { C } } _ { \mathsf { S M M S } }$ is the cost of $\mathrm { \dot { S } M M S , C _ { c o m m } }$ is the cost of communications and $\mathsf { C } _ { \mathrm { t r a i n } }$ is the cost of training. The value of $\mathsf { R } _ { \mathrm { H } } \mathrm { i } \mathsf { s } \left( \mathrm { H } - \mathrm { H } _ { \mathrm { I } } \right)$ where H is the number of hospitalization in a given period of time and HI is the number of hospitalization with an intervention for medication adherence. $\mathrm { H _ { I } }$ is a function of both the level of medication adherence and the threshold value for satisfactory adherence for the given health condition and the prescribed medication. If medication adherence is assumed to be the only factor leading to or avoiding conditions resulting in hospitalization, then

$$
\mathrm{R} _ {\mathrm{H}} = ((\mathrm{H} - \mathrm{H} * \mathrm{P} (\mathrm{MA} > = \mathrm{MA} _ {\mathrm{TH}})).\tag{20}
$$

## 5. Results and discussion

Using the analytical model, we derived several results on the impact of SMMS reliability on medication adherence, the impact of multiple and dependent medications, adherence improvement with SMMS, and the impact of single and “composite” interventions on medication adherence.

## 5.1. The impact of infrastructure

The reliability of infrastructure relates with the ability to sense and transmit/receive messages on patient's adherence. The impact of reliability is shown in Fig. 17, where medication adherence is improved by increasing the number of context-sensitive reminders. Therefore, SMMS can still function well when the infrastructure is not highly reliable. However, with higher reliability, the number of messages needed to achieve a certain level of adherence is signi<sup>fi</sup>cantly reduced. The impact of patient's self-medication behavior on overall medication adherence is shown in Fig. 18, where adherence is signi<sup>fi</sup>cantly improved by using highly persistent SMMS (higher values of N).

![](/api/attachments/89QVW3QH/fulltext/images/6119ea2913f1c1a849c299308a552651197808421c8da4262c16ed6cda4a93fc.jpg)  
Fig. 17. The impact of reliability on medication adherence.

![](/api/attachments/89QVW3QH/fulltext/images/71a05e31b2fa6ba49d2fa86fef1f110139d45af7b671f32b2cb15bbcd503f545.jpg)  
Fig. 18. Improvement in medication adherence by SMMS.

## 5.2. Impact of dependent drug

The impact of increased dependence among medications along with the number of medications on adherence is shown in Fig. 19. As expected, as the number of medications increases, the adherence level goes down due to added complexity and reminders and this is consistent with clinical trials on adherence [2,5]. We found low levels of adherence for patients without SMMS and it got worse for dependent medications. The use of SMMS improves the adherence even under multiple medications with inter-dependent relationships.

## 5.3. Effectiveness of interventions

Three different interventions are evaluated here. These include increased motivation, improved scheduling/long-life of medications, and the proposed context-sensitive reminders. First, we present the impact of increased motivation, due to family and social support or due to effective therapeutic alliance with healthcare professionals, on medication adherence. The level of medication adherence for different levels of additional motivation is shown in Fig. 20. A higher degree of motivation is shown to improve overall medication adherence even under multiple medications per day regime.

![](/api/attachments/89QVW3QH/fulltext/images/02e6f934c07ab19c6692454d945844e10615a74be5f8012758d9efb0e04a0d3a.jpg)  
Fig. 19. Medication adherence with increased dependent medications.

![](/api/attachments/89QVW3QH/fulltext/images/2924056b06d37176b2cfcb6ac70012f1b995935402f0a6eabf2c1e69a62f106e.jpg)  
Fig. 20. Medication adherence with increasing support under varying cognitive abilities.

The impact of multiple medications on overall adherence is shown in Fig. 21, where the adherence improves by 50% when the number of doses is reduced from 6 to 2 per day. This matches well with data obtained from clinical trials [2,5], where there is a signi<sup>fi</sup>cant decrease in adherence with increased number of medications and/or doses.

A comparison among three different sets of interventions for improving medication adherence is shown in Fig. 22. The improved “scheduling”, “support”, and “reminders” all lead to a higher level of adherence, however reminders (using SMMS) produce the highest degree of medication adherence.

We wanted to explore how these three different sets of interventions would work together. Since a “composite” intervention could be designed in multiple different ways such as different motivation factors, different levels of persistence of reminders, and the level of improved scheduling. The performance of four different “composite” interventions is shown in Fig. 23. The parameters of interventions are shown in Table 1. The best performance is obtained with high persistence of reminders. Many other combinations of “composite” interventions can be designed.

## 5.4. Reduction in hospitalization cost

The total savings, shown in Table 2, are signi<sup>fi</sup>cant even under reduction of hospitalization events by one and with cost of SMMS at \$1000. As the total hospitalization cost goes up, the savings due to improved medication adherence become even more signi<sup>fi</sup>cant.

![](/api/attachments/89QVW3QH/fulltext/images/a1fdf20978fdc9826f2d1901177028a7675b73382165c16d8fba6b66be04e15c.jpg)  
Fig. 21. Medication adherence for multiple drugs.

![](/api/attachments/89QVW3QH/fulltext/images/53ec4d1859493511e3fb726e35e5b2ffe63d8852830fe41bef2e6b7d150645ec.jpg)  
Fig. 22. Impact of reminders (frequency and effectiveness) on medication adherence.

From the above model and results, the following observations can be made:

• Medication adherence can be improved by increasing the number of context-sensitive reminders. For some people, there may be a limit on how many reminders for each dose should be sent.

• If the reliability of associated infrastructure is high, the number of reminders needed to achieve a certain level of adherence is signi<sup>fi</sup> cantly reduced.

• SMMS is very effective in creating context-sensitive reminders in improving the level of medication adherence even under scenarios of multiple medications/day. The use of SMMS improves the adherence even under multiple medications with inter-dependent relationships.

• SMMS leads to signi<sup>fi</sup>cantly higher level of medication adherence as compared to two other sets of interventions, namely “higher support” for the patient and improved “scheduling” of medications both of which are shown to improve overall medication adherence.

• Under multiple “composite” interventions, based on motivation factors, persistence of reminders, and improved scheduling, the best performance is obtained when context-sensitive reminders are persistently used. In future, many other combinations of “composite” interventions can be designed.

• The total healthcare savings are signi<sup>fi</sup>cant even under slightly improved medication adherence. With higher hospitalization cost, the savings due to improved adherence become even more signi<sup>fi</sup>cant.

![](/api/attachments/89QVW3QH/fulltext/images/3647422210926605a9e2d29147d3dd57356d002a7e868204c6f802c10812c619.jpg)  
Fig. 23. The performance of four composite interventions.

Table 1  
The four composite interventions.

<table><tr><td>Composite intervention</td><td>Support (M)</td><td>Reminders (R)</td><td>Scheduling (I)</td><td>Comment</td></tr><tr><td>1</td><td>0.1</td><td>1</td><td>2</td><td>Baseline composite intervention</td></tr><tr><td>2</td><td>0.2</td><td>1</td><td>2</td><td>Double the support from baseline</td></tr><tr><td>3</td><td>0.1</td><td>1</td><td>1</td><td>Twice as good schedule from baseline</td></tr><tr><td>4</td><td>0.1</td><td>2</td><td>2</td><td>Double the number of reminders from baseline</td></tr></table>

## 6. Conclusions and future work

Medication adherence is a major challenge in healthcare research due to its complexity and impact on overall health outcomes. As the cost of prescription medication has been skyrocketing, it is critical to address this challenge both from the quality of care as well as cost angles. In this paper, we address medication adherence by modeling and evaluating multiple interventions both individually and in various combinations. We presented the design and performance evaluation of smart medication management system (SMMS) to support multiple interventions to improve medication adherence. We present multiple metrics which can be used in measuring and evaluating the level of medication adherence. Using an analytical model, multiple interventions were modeled and evaluated.

The performance results show that medication adherence is signi<sup>fi</sup>- cantly improved for single and multiple medications. Medication adherence is also improved by increasing the number of context-sensitive reminders. SMMS is very effective in creating context-sensitive reminders in improving the level of medication adherence even under scenarios of multiple medications/day. The use of SMMS also improves the adherence even under multiple medications with inter-dependent relationships. SMMS leads to signi<sup>fi</sup>cantly higher level of medication adherence as compared to two other sets of interventions, namely “higher support” for the patient and improved “scheduling” of medications both of which are shown to improve overall medication adherence. Under multiple “composite” interventions, the best performance is obtained when context-sensitive reminders are persistently used. The total healthcare savings are signi<sup>fi</sup>cant even under slightly improved medication adherence. With higher hospitalization cost, the savings due to improved medication adherence become even more signi<sup>fi</sup>cant. We also found substantial cost savings even when the cost of hospitalization was low and the cost of medication monitoring was signi<sup>fi</sup>cant.

The future work could include (a) several adherence models to study the effectiveness of systems, (b) cost, complexity and <sup>fl</sup>exibility of SMMS, and, (c) incentives for patient's consent. Additional research could include development of prototypes for different environments and multi-site testing.

Table 2  
Cost savings per patient/year with improved medication adherence.

<table><tr><td> $C_{H} + L{P}_{H}$ </td><td> $R_{H}$ </td><td> $C_{SMMS} + C_{comm} + C_{train}$ </td><td> $T_{sav}$ </td></tr><tr><td rowspan="3">$1000</td><td>1</td><td>$100</td><td>$900</td></tr><tr><td>3</td><td>$500</td><td>$2500</td></tr><tr><td>5</td><td>$1000</td><td>$4000</td></tr><tr><td rowspan="3">$5000</td><td>1</td><td>$100</td><td>$4900</td></tr><tr><td>3</td><td>$500</td><td>$14,500</td></tr><tr><td>5</td><td>$1000</td><td>$24,000</td></tr><tr><td rowspan="3">$10,000</td><td>1</td><td>$100</td><td>$9900</td></tr><tr><td>3</td><td>$500</td><td>$29,500</td></tr><tr><td>5</td><td>$1000</td><td>$49,000</td></tr><tr><td rowspan="3">$50,000</td><td>1</td><td>$100</td><td>$49,000</td></tr><tr><td>3</td><td>$500</td><td>$149,500</td></tr><tr><td>5</td><td>$1000</td><td>$249,000</td></tr></table>

## References

[1] O. Amft, G. Troster, Methods for detection and classi<sup>fi</sup>cation of normal swallowing from muscle activation and sound, in: Proc. Pervasive Healthcare Conference, 2006.

[2] R. Chapman, J. Benner, A. Petrilla, J. Tierce, S. Collins, D. Battleman, J. Schwartz, Predictors of adherence with antihypertensive and lipid-lowering therapy, Archives of Internal Medicine 165 (2005).

[3] R. Chapman, J. Yeaw, C. Roberts, Association between adherence and calcium-channel blocker and statin medication and likelyhood of Cardiovascular events among US managed care enrollees, BMC Cardiovascular Disorders 10 (29) (2010).

[4] Jae-Hun Choi et al., Proactive medication assistances based on spatiotemporal context awareness of aged persons, in: Proc. of 30th Int. Conf. IEEE Engineering in Medicine and Biology Society (2008).

[5] A. Claxton, J. Cramer, C. Pierce, A systematic review of the associations between dose regimens and medication compliance, Clinical Therapeutics 23 (8) (2001).

[6] CLT: Cognitive Load Theory, From theories used in IS research: cognitive load theory. available at http://www.fsc.yorku.ca/york/istheory/wiki/index.php/Cognitive\_load\_ theory.

[7] A. Dey, G. Abowd, Towards a better understanding of context and contextawareness, in: Tech Report, GIT-GVU-99-22, June 1999.

[8] J. Dunbar-Jaco, M.K. Mortimer-Stephens, Treatment adherence in chronic disease, Journal of Clinical Epidemiology 54 (2001).

[9] W.S. Fenton, C.R. Blyler, R. Heinssen, Determinants of medication compliance in schizophrenia: empirical and clinical <sup>fi</sup>ndings, Schizophrenia Bulletin 23 (4) (1997).

[10] V. Hamrin, E. McCarthy, V. Tyson, Pediatric psychotropic medication initiation and adherence: a literature review based on social exchange theory, Journal of Child and Adolescent Psychiatric Nursing 23 (3) (2010).

[11] S. Helal, W. Mann, H. Zabadani, J. King, Y. Kaddoura, E. Jansen, The gator tech smart house: a programmable pervasive space, IEEE Computer 38 (3) (2005).

[12] A.R. Hevner, S.T. March, J. Park, S. Ram, Design science in information systems research, MIS Quarterly 28 (1) (2004).

[13] K. Ingersoll, J. Cohen, The impact of medication regimen factors on adherence to chronic treatment: a review of literature, Journal of Behavior Medicine 31 (3) (2008).

[14] L. Issac, et al., Compliance and cognitive function: a methodological approach to measuring unintentional errors in medication compliance in the elderly, The Gerontologist 33 (6) (1993).

[15] M. Kerr, S. Lusk, D. Ronis, Explaining Mexican American workers' hearing protection use with the health promotion model, Nursing Research 51 (2) (2002).

[16] I. Korhonen, J. Parkka, M. Gils, Health monitoring in the home of the future, IEEE Engineering in Medicine and Biology Magazine 22 (3) (2003).

[17] W. Kuechler, V. Vaishnavi, On theory development in design science research: anatomy of a research project, European Journal of Information Systems 17 (2008).

[18] N. Lavrac, Machine learning for data mining in medicine, in: Proc. Arti<sup>fi</sup>cial Intelligence in Medicine (AIMDM), 1999.

[19] LifeShirt, http://www.vivometrics.com/site/system.html.

[20] J. Lucas, S. Orshan, F. Cook, Determinants of health-promotion behavior among women ages 65 and above living in the community, Scholarly Inquiry for Nursing Practice 14 (2000).

[21] D. Mann, Resistant disease or resistant patient: problems with adherence to cardiovascular medications in the elderly, Geriatrics 64 (9) (2009).

[22] S. March, G. Smith, Design and natural science research on information technology, Decision Support Systems 15 (1995).

[23] M.L. Markus, A. Majchrzak, L. Gasser, A design theory for systems that support emergent knowledge processes, MIS Quarterly 26 (3) (2002).

[24] H. McDonald, A. Garg, R. Haynes, Interventions to enhance patient adherence to medication prescriptions, Journal of American Medication Association (JAMA) 288 (22) (2002).

[25] NIH website for prescription drug abuse, http://www.nlm.nih.gov/medlineplus/ prescriptiondrugabuse.html 2010 (accessed on July 21, 2010).

[26] L. Osterberg, T. Blaschke, Adherence to medication, The New England Journal of Medicine 353 (5) (2005).

[27] L. Palen, S. Aalokke, Of pill boxes and piano benches: “home-made” methods for managing medication, in: Proc, of ACM Conf. Computer Supported Collaborative Work, 2006.

[28] N.J. Pender, C. Murdaugh, M.A. Parsons, Health Promotion in Nursing Practice, 5 ed. Prentice- Hall, Upper Saddle River, NJ, 2006.

[29] J. Piazza, K. Conrad, J. Wilbur, Exercise behavior among female occupational health nurses: in<sup>fl</sup>uence of self-ef<sup>fi</sup>cacy, perceived health, control, and age, Journal of the American Association of Occupational Health Nurses (AAOHN) 49 (2) (2001).

[30] J.P. Shim, M. Warkentin, J. Courtney, D.J. Power, R. Sharda, C. Carlsson, Past, present, and future of decision support technology, Decision Support Systems 33 (2) (2002).

[31] Siegemund, C. Florkemeier, Interaction in Pervasive computing settings using bluetooth-enabled active tags and passive RFID technology together with mobile phones, in: Proc. of IEEE Conference on Pervasive Computing (Percom03) (2003).

[32] M. Skov, R. Hoegh, Supporting information access in a hospital ward by a contextaware mobile electronic patient record, Journal of Pervasive and Ubiquitous Computing (10) (2006).

[33] Smart Shirt, http://www.gtwm.gatech.edu.

[34] S. Sneha, U. Varshney, Enabling ubiquitous patient monitoring: model, decision protocols, opportunities and challenges, Decision Support Systems 46 (3) (2009).

[35] D. Stefanov, Z. Bien, W. Bang, The smart house for older persons and persons with physical disabilities: structure, technology, arrangements, and perspectives, IEEE Transactions on Neural Systems and Rehabilitation Engineering 12 (2) (2004).

[36] J. Sweller, Cognitive load during problem solving: effects on learning, Cognitive Science (12) (1988).

[37] V. Vaishnavi, W. Kuechler, Design Science Research Methods and Patterns, <sup>fi</sup>rst ed. Auerbach Publications. Boca Raton. 2007

[38] M. van Eijken, S. Tsang, M. Wensing, P.A. de Smet, R.P. Grol, Interventions to improve compliance in older patients living in the community: a systemic review of the literature, Drugs & Aging 20 (3) (2003).

[39] U. Varshney, A framework for supporting emergency messages in wireless patient monitoring, Decision Support Systems 45 (4) (2008).

[40] U. Varshney, Pervasive healthcare computing: EMR/EHR, Wireless and Health Monitoring, <sup>fi</sup>rst ed., Springer, New York, 2009.

[41] J. Walls, G. Widmeyer, O. El Sawy, Building an information system design theory for vigilant EIS, Information Systems Research 3 (1) (1992).

[42] D. Wan, D. Wan, Magic medicine cabinet: a situated portal for consumer healthcare, in: Proc. Int. Symp. Handheld and Ubiquitous Computing, 1999.

[43] Website for M-pill, http://www.m-pill.com/index.php?browse=compliance.

[44] WelchAllyn, http://www.monitoring.welchallyn.com/products/wireless/.

[45] T. Wu, N. Pender, Determinants of physical activity among Taiwanese adoles cents: application of health promotion model, Research in Nursing & Health 25 (1) (2002).

Upkar Varshney is currently an Associate Professor of Computer Information Systems at Georgia State University, Atlanta. His current interests include mobile health, pervasive computing, and wireless networks. He has authored over 150 papers including 70 in national and international journals. He is the author of Pervasive Healthcare, published by Springer in 2009 and 2010. He is credited with several “<sup>fi</sup>rst” papers in streams of mobile commerce and pervasive healthcare. According to Scholar-Google, his papers are among the highly cited and have been cited more than 3000 times. He was the founding co-chair (with Prof. Imrich Chlamtac) of the International Pervasive Health Conference (http://www.pervasivehealth.org/previous/index.html) in 2006 and the steering committee co-chair for the 2008 conference (http://www.pervasivehealth. org). Upkar was the program co-chair for the Americas Conference on Information Systems (AMCIS-2009). Upkar has presented over fifty tutorials workshops, and a few kevnotes at maior wireless, computing, and information systems conferences. He has also received grants totaling \$500K from several funding agencies including the National Science Foundation. His teaching awards include the Myron T. Greene Outstanding Teaching Award (2004), the RCB College Distinguished Teaching Award (2002), and the Myron T. Greene Outstanding Teaching Award (2000). He has served or is serving as an editor/guest editor for several major journals including IEEE Transactions on IT in Biomedicine, ACM/Springer Mobile Networks (MONET), Decision Support Systems (DSS), IEEE Computer, Communications of the AIS (CAIS), Int. J. on Network Management (IJNM), Int. Journal on Mobile Communications (IJMC) among others.
