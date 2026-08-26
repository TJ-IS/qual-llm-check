---
otero_id: 3884
otero_key: "UATC27GA"
title: "A model for improving quality of decisions in mobile health"
authors: "Upkar Varshney"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2014.03.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Upkar Varshney

Department of Computer Information Systems, Georgia State University, Atlanta, GA 30302-4015, United States

a r t i c l e i n f o

Article history: Received 30 May 2012 Received in revised form 30 September 2013 Accepted 14 March 2014 Available online 25 March 2014

Keywords: Mobile health Context-awareness Decisions Performance evaluation Analytical modeling

## a b s t r a c t

The rapid and wide-scale introduction of mobile technologies in healthcare is resulting in an emerging area of mobile health. m-Health has major implications for patients, healthcare professionals, developers, infrastructure providers and regulators in both developed and developing countries. Mobile technologies can not only support instant and ubiquitous access to information, healthcare professionals and patients, but can also create many interesting challenges, including additional complexity and potential for various errors. In this paper, we address how mobile health can be more effectively supported by mobile technologies. More speci<sup>fi</sup>cally, we present two sets of enhancements: (a) context-awareness and processing and (b) improved presentation of information to healthcare professionals. These enhancements are then applied in the conceptual design of a mobile health alert generation and processing system. To evaluate the effectiveness of the proposed enhancements, we develop and utilize an analytical model. Using multiple metrics, including the number of alerts generated and probability of error in alert-response, we show that the proposed enhancements can improve the quality of mobile health. We hope that other researchers design, implement and evaluate additional enhancements in mobile technologies for m-health. While we do not present any prototypes of the systems, the work presented in the paper can lead to prototypes and testing of systems in the future for mobile health

© 2014 Elsevier B.V. All rights reserved.

## 1. Introduction

Mobile technologies are changing the way healthcare services are being designed, implemented, delivered and received. This is resulting in a new area of mobile health (or m-health) and has major implications for individuals, groups, and societies both in developed and developing countries. Mobile health can be simply de<sup>fi</sup>ned as delivery of healthcare services using mobile technologies [8]. Mobile technologies can facilitate instant communications and access to healthcare professionals, and with access to multiple wireless networks, it can increase the speed of decision making, especially for emergency cases. There is a signi<sup>fi</sup>cant potential for utilizing numerous advances of mobile computing in healthcare [24]. m-Health includes multiple applications and several wireless networks including cellular, wireless LANs, and satellites [8]. We envision that other networks such as Bluetooth, ad hoc networks and Zigbee will also play a major role with sensors and RFID in mobile health.

There is a need to study how mobile technologies may affect the quality of healthcare in different scenarios of preventive care, urgent care, emergency care, home health, and long-term care. Mobile devices in healthcare are likely to be diverse, ranging from sensors, RFID, small screen smartphones to larger screen handheld devices [8]. Some work in mobile health include graphical information visualization [9], clinical decision support system for major lung disease (Chronic Obstructive

Pulmonary Disease (COPD)) patients [10], alerts generation for brain activity changes [11], coordination system for emergency medical care [12], management of health conditions of hypertensive patients [13], clinical decision support system for pediatric intensive care [14], and the ontology driven system for chest pain risk assessment [15].

Almost all of the above work focus on designing and developing systems for speci<sup>fi</sup>c health conditions. However, how mobile technologies can be enhanced to improve mobile health has not been studied. Mobile health is likely to involve multiple sources of information. Many decisions, including some by automated devices and then followed by healthcare professionals, need to be made in identifying the needs of patients and providing them with best possible healthcare services. There are numerous challenges in how to support mobile health. In this paper, we address how mobile health can be better supported by enhancements in mobile devices and networks. More speci<sup>fi</sup>cally, we present two sets of enhancements, namely (a) context-awareness and (b) improved presentation of information to healthcare professionals. The <sup>fi</sup>rst enhancement is likely to reduce the amount of traf<sup>fi</sup>c generated, transmitted over networks, and presented to healthcare professionals without sacri<sup>fi</sup>cing the quality of information. The second enhancement is designed to improve the presentation of information to healthcare professional and could reduce the probability of error in alertresponse among others.

In simple case, alerts can be generated by utilizing the absolute values of vital signs as shown in Fig. 1(a). However, such system could lead to many “false-positive” alerts, resulting in waste of healthcare resources. The proposed enhancements are applied in the design of a health alert generation and processing system, where decisions are made by healthcare professionals using mobile technologies as shown in Fig. 1(b). The use of context-awareness can reduce the information traf<sup>fi</sup>c, in terms of number of alerts to healthcare professionals, while improved presentation can reduce the information overload and thus improve the quality of decision making. We show the value of proposed enhancements by improving the ways alerts are more effectively generated by the alert generation system and processed by healthcare professionals in Fig. 1(b). The transmission of alerts through a variety of wireless networks has been addressed in [25]; here we focus on alert generation and processing by healthcare professionals.

![](/api/attachments/UATC27GA/fulltext/images/b5e4d8ef7da54c2ecb5f1e067753d93a0fc7a0668451f6484e3d852f06afaa72.jpg)  
(a) Alert Generation in Wireless Patient Monitoring

![](/api/attachments/UATC27GA/fulltext/images/ed9b25377e38f2b5ff1aeff5f6bd5945d55b85c7792bff8f7c6300232f6e0c43.jpg)  
(b) Alert Generation in Context-aware Monitoring  
Fig. 1. Different possibilities of monitoring and alert generation.

We then evaluate these enhancements using an analytical model. The analytical model is designed to compute the number of alerts generated, delays in alerts and probability of error in alert-response. The use of context-awareness reduces the number of “false-positive” alerts and the probability of error in alert-response is shown to decrease with improved presentation of information. We are not focusing on complex and broad decision making using mobile devices, but rather focusing only on enhancements for mobile technologies to improve mobile health. Much more work is needed in addressing different challenges in decision making for mobile healthcare, including the complexity, quality, speed and effectiveness and the role of infrastructure. Also, the future research should address implementation and prototyping issues in decision making in mobile health using the proposed and other enhancements.

The paper is formatted as follows. We present two enhancements for mobile health in Section 2 and Section 3, and performance evaluation in Section 4. Some discussion is presented in Section 5. Finally some concluding remarks are made in Section 6.

## 2. Context-awareness for mobile health

In this section, we focus on adding context-awareness in mobile health. Other enhancements can be designed to improve mobile health, and we expect that many more enhancements will be presented in subsequent papers. In general, context-aware alert generation can

• reduce the amount of information in an alert message by focusing on “changed” values

• reduce the number of alerts by considering the rich context of patients (essentially reducing some false-positives)

• reduce the load for healthcare professionals, which can improve the quality of decision making.

## 2.1. Context-awareness

The context is any information that can be used to characterize the situation of an entity, which is a person, place, or object that is considered relevant to the interaction between a user and an application, including the user and applications themselves [26]. By including the context, richness of communications can be increased and more useful services can be designed. The context can be sensed, derived or explicitly provided [27]. The context information can be acquired from multiple sources: sensors (ambient, location, health), information sources (preferences, information on applications and usage, user history, patient's history) and miscellaneous (current network traf<sup>fi</sup>c, special conditions in user's surroundings, closest place of interest, distance to a hospital). A system is context-aware if it uses context to provide relevant information and/or services to the user, where relevancy depends on the user's task [26]. The context includes who (identity), what (activity), where (location), when (temporal) and why (reasoning for behavior and actions). Fig. 2(a) shows the steps in context-awareness, where it is broken into three phases of information, context and adaptation [8]. The <sup>fi</sup>rst step involves collecting the necessary and relevant information from multiple sources. Then using the “programmed” context protocols, information is integrated and the current context is generated. The <sup>fi</sup>nal step involves adapting to the new context in providing services to the users. After discussing the basics of contextawareness, we now focus on how it can improve alert generation in mobile health. More speci<sup>fi</sup>cally, context-awareness can help in (a) reducing the amount of information, (b) making sense of important information, and (c) improving the quality of decisions by healthcare professionals. The use of context in alert generation is shown in Fig. 2(b). A range of information about the patients must be obtained, ampli<sup>fi</sup>ed, and digitized before transmission. For personalized monitoring, patient's nominal vital signs are de<sup>fi</sup>ned with multiple thresholds, set of actions, undesirable patterns, and inter-relationships. The level of context-awareness could involve health history, activities, and information on missing doses, recent labs, known handicaps, food and diets, and unusual conditions [23]. Some of these factors are used in deriving alerts in Fig. 2(b).

The wearable sensors on patient's body are shown in Fig. 3. In some cases, additional sensors may be used, while in some other cases, fewer sensors may be required. These sensors collect vital signs and other necessary biomedical parameters, which will then be processed by monitoring devices for generating “alerts”. So this is part of information collection necessary for deriving the patient's context.

Context-generation protocols, utilizing weighted probabilities and prediction, derive possible contexts of patient's healthcare needs by integrating and processing information from multiple sources. The context-generation protocols can work with incomplete information in deriving the patient's context and healthcare needs. The contextgeneration protocols assist and do not replace the decision making by healthcare professionals, who make decisions using multiple informational items including the context. There is enough <sup>fl</sup>exibility to allow different alarm logics to be implemented with requirement changes. The future work must address data analysis and alarm logic for complex monitoring scenarios and patients' conditions.

(a) The Steps in Context-awareness  
![](/api/attachments/UATC27GA/fulltext/images/6f29d9d7610c9b04ceabb5843e0adbfed481f192f6192dfa09394ffc6a1510c8.jpg)

![](/api/attachments/UATC27GA/fulltext/images/22462bbe643cf7167fc64a8fc177771097296c65cbaa80610d08068235cbc2e6.jpg)  
(b) Context-aware Alert Generation in Mobile Health  
Fig. 2. Context modeling and generation in mobile health.

One of the goals is to create wireless monitoring with zero “falsenegatives” where severity of patient's condition is not detected and minimal number of “false-positives” where the system overestimates the severity of patient's condition. Monitoring rules, individualized to the patient, are speci<sup>fi</sup>ed by a healthcare professional and could result in a more accurate generation of “alerts”. These rules can be based on the practice of evidence based medicine and the judgment of healthcare professionals on what should be collected, processed and utilized in generation of alerts.

![](/api/attachments/UATC27GA/fulltext/images/0820af9b798d61dc87b873c43f0e2d43852d4bcc3e481fa80c25ed0058d0e359.jpg)  
Fig. 3. Vital signs and biomedical parameters.

For managing complexity, the rules for context-generation could be programmed to limit the possible contexts to cover the most likely problems. The system, to differentiate a multitude of situations, could also utilize physical location, personal health history and current activities. Therefore, if the context is incorrect or there is a problem, the monitoring system would allow the healthcare professional to request more information and make a better decision.

The proposed algorithm for context-awareness is shown in Fig. 4. This algorithm is designed to consider all the attributes from Fig. 2(b) in generating context-aware alerts. The weights (or points) will be initialized and adjusted by healthcare professionals based on the type of monitoring and the patient's condition. The choice of weights will affect the number of false-positives and the amount of information that must be processed will affect accuracy of the context. If certain information is not available or reliable, some weights can be used to avoid the impact of “missed” information.

It is likely that some testing will be done before a reliable set of weights can be determined for a patient. As the patient's condition may change over time, these weights will have to be recalibrated. For the algorithm, additional informational items can be added in future as necessary along with their weights (points). This can include checking speci<sup>fi</sup>c biomedical parameter for the patient as part of a monitored condition. The protocols, implemented as set of rules, are stored and processed in the health monitoring devices that a patient can carry or wear. An example operation of these rules is shown in Fig. 4, where values and rate of change of vital signs along with patient's current activities are utilized in generating the level of emergency for the alerts. Certainly, not all informational items from the algorithm are included, but it shows the promise of context-awareness.

(a) Processing of Vital Signs  
![](/api/attachments/UATC27GA/fulltext/images/4cc5a828488f63a75a02477e9e7d9d323b438844545ce48eab7b639c72294031.jpg)  
Fig. 4. An example of alert generation.

![](/api/attachments/UATC27GA/fulltext/images/bd7fbebff1103fa27ae9b6526c5eaf26707ead04efce56f85053e66fbb900300.jpg)

![](/api/attachments/UATC27GA/fulltext/images/353c4d6ce481223b41df6e74e1b7cf31f5a18e143e6f7b92ab49e493b045ad75.jpg)  
Fig. 4 (continued).

The enhanced mobile system can be designed to generate fewer messages as multiple factors are used in deriving the context. It will also generate less information per message as only the changed values and parameters that go out of normal range are included. In future, the enhanced system could further reduce the number of messages by <sup>fi</sup>ltering some messages and compression to reduce message size; however more work is needed to study any negative impact of <sup>fi</sup>ltering on healthcare information.

## 3. Improved presentation of information

Decision making in healthcare is a complex process in terms of number of parameters and variables, outcome possibilities, and the amount of information that must be processed [1]. There has been some work in studying cognitive processes for healthcare decision making. This includes understanding the processes involved by observing healthcare professionals [2] and negative impact of multitasking, frequent [4] and presentation of information in diagnosing patient conditions [5]. The research in cognition is applied to address decision making in critical care environment [6].

One way to study decision making for healthcare professionals is to use cognitive load approach [7], where cognitive overload could affect the quality of decision making, possibly resulting in errors and lower quality of healthcare services. Mobile devices can add more complexity, so we present some enhancements to improve the quality of mobile health. There are three types of cognitive loads: intrinsic, extraneous, and germane [16]. Intrinsic load deals with the inherent technical dif<sup>fi</sup>- culty associated with a task. Extraneous load is generated by the manner in which information is presented. Germane load relates with the processing, construction and automation of schemata involved in the long-term learning [7]. The goal here with mobile device enhancement is to minimize intrinsic and extraneous cognitive loads by reducing the dif<sup>fi</sup>culty of tasks and improved presentation of information.

The improved presentation of information, such as focusing on most important information <sup>fi</sup>rst, color coding of information, and multimodal presentation of information to healthcare professionals could reduce their cognitive load and improve their decision making performance. Systems must estimate users' cognitive loads and make judgments about the most suitable combinations of media, modality and the intrusiveness with which the information is presented for adaptation to individual cognitive capability. Media is the pattern of information presented such as visual, auditory and olfactory. Modality is the form or means of presentation. In a high cognitive load environment, media or modality may exceed human capacity, so the system should present information by using a media or modality in which the cognitive load is low. If a user cannot understand or recognize visual information, the system should present this information using auditory medium that is recognizable and perceivable [17]. The reduction in cognitive overload will improve the decision making as there is a strong co-relation between cognitive overload and error rate [18]. Reduction in cognitive overload will also improve the decision accuracy as the healthcare professionals can focus on elimination strategy in decision making. The main idea is the use of dual channel model, where auditory inputs can also be used in information presentation to healthcare professionals. This may require synchronization between visual and auditory inputs for decision making. The synchronization includes both temporal and spatial components. The dual channel model is based on the observation of two independent channels for processing audio (spoken words) and visual information (words and pictures) and each has a certain amount of working capacity [19].

![](/api/attachments/UATC27GA/fulltext/images/9bcdfb1097427e43e424fa16355a1ed070b8b4190c58e0f1c4ea1d86c53c23d3.jpg)

(f) Generation of Alerts  
![](/api/attachments/UATC27GA/fulltext/images/1f80e272658f5906d023e10637be85f6dce6f1d52c4a2d549d8cde1179416399.jpg)  
Fig. 4 (continued).

Based on the above discussion, reduction in the amount of information, suitable and improved presentation of information, and reduction in process complexity could lead to reduction in estimated load. The reduction of information is also limited by the potential for loss of critical information. The load on healthcare professionals can be improved by personalization of the device interface, symbolic representation of information [5], gradual display of information in decreasing importance, and use of assisted larger displays [22]. These translate to the following enhancements for mobile health systems (MHS): (a) the MHS should reduce the number of items to remember and process, (b) the MHS should support improved presentation of information by suitable displays, personalization of interface, color coding and display of most important information <sup>fi</sup>rst, (c) the MHS should utilize both visual as well as audible part of working memory to manage cognitive load of the healthcare professionals, (d) MHS should reduce cognitive load for both phase of decision making: processing phase and action phase, and (e) should utilize various design enhancements to reduce cognitive load to reduce the probability of decision errors. Some of these are shown in Fig. 5.

The alert messages are delivered to health professionals devices, designed with several features such as interface personalization tools, color coded display and preferred ways to create alerts. The process is simpli<sup>fi</sup>ed by the system which presents information in “medically meaningful way”, by showing alerts <sup>fi</sup>rst and then related information in an increasingly detailed manner (Fig. 6). The example describes a situation where certain patient has an emergency (red ball on the <sup>fi</sup>rst screen). The two yellow <sup>fi</sup>elds on second screen show two abnormal values of vital signs (blood pressure and pulse). Individually, neither of these two would constitute an emergency. However the contextaware processing (one of the two proposed enhancements) correctly detects an emergency due to two vital signs being abnormal with patient's history of cardiovascular problems and the current activity as resting (Fig. 4). Some of the information is displayed in green, implying normal values. Some of the additional informational items are converted from visual to audible mode to suit the healthcare professional as presented in Fig. 5.

The enhanced system also offers several choices for decision making based on the derived context earlier. These context-aware clues are designed to assist/enhance decision making and not replace the human decision making. The healthcare professional, who is trained in dealing with information in multiple modes, can select or ignore the likely condition (Fig. 7).

## 4. Performance evaluation

In this section, we present an analytical model to evaluate the impact of various enhancements presented in Section 2 and Section 3. The model is used to estimate the number of alerts, information load and complexity in m-health system with and without proposed enhancements. Then we estimate the errors in alert-response based on the load and available working memory capacity of healthcare professional. Due to the nature of this work, we did not <sup>fi</sup>nd standard metrics. Therefore, we propose and utilize the following metrics

• the number of informational items for decision making

• the number of overlapping alerts

• alert delay/time to intervene

• the number of items converted from visual to auditory mode

• the number of screen switching in mobile device

• the number of steps in decision making

• working memory capacity (WMC)

• estimated cognitive load units (ECLU)

• estimated errors in alert-response.

The model includes equations for estimating the number of alerts that are generated for a range of frequency of monitoring. The alerts are queued at the same priority level as all alerts that are generated are at high emergency level. In future, multiple priorities can be used in differentiating among alerts.

The number of overlapping alerts is the number of alerts that are waiting for the healthcare professional including the one he/she is processing. The information load is measured as a function of number of overlapping alerts that a healthcare professional has to process, number of informational items, both visual and auditory, and number of steps and number of times screens have to be switched during the decision making process (Fig. 5). The processing at the source device can reduce the number of alerts by utilizing context awareness. Both the complexity of steps and number of steps in decision making are included in estimating information load.

![](/api/attachments/UATC27GA/fulltext/images/b2c70934ffc7c3feeea1d2577094a4a52c61388735aa6cd59520463f6aa8890d.jpg)  
Medically Meaningful Representation/Integration of Information  
Fig. 5. Some enhancements for m-health.

The model used in the evaluation is shown in Fig. 8. The reduction in cognitive overload will improve the decision making as there is a strong co-relation between cognitive overload and error rate [18]. Reduction in cognitive overload will also improve the decision accuracy as the healthcare professionals can focus on elimination strategy in decision making. Severe cognitive load could lead to more unpredictable errors in decision making, especially when the task complexity is high and there are unusual side-effects due to the underlying technologies as observed by [21]. The goal is to reduce cognitive load to reduce error rate and the implications are for system design, interface design, and informational presentation. The main idea is the use of dual channel model, where auditory inputs can also be used in information presentation to healthcare professionals. This may require synchronization between visual and auditory inputs for decision making. The synchronization includes both temporal and spatial components. The dual channel model is based on the observation of two independent channels for processing audio (spoken words) and visual information (words and pictures) and each has a certain amount of working capacity [19]. The working memory has partially independent processors for handling visual and auditory material [20]. The model is shown in Fig. 8, where both visual and auditory modes of information could be used in decision making to better utilize the working memory.

Next, for better readability, the symbols used in the model are shown in Table. 1.

## 4.1. Modeling context-awareness and the number of alerts

The number of alerts in a given time can be expressed in terms of number of times vital signs were monitored and number of times they exceeded certain thresholds for the patients. Based on the threshold values only, some of these alerts could represent “false positives”. Assuming the same threshold values for all patients and uniform distribution of collected sample values, the probability that vital signs exceed the thresholds can be given as $\mathrm { ( M a x \mathrm { \bar { V } - T _ { H } + T _ { L } - M i n V ) \Omega / \Omega ( M a x V - \Omega } }$ MinV). As shown in Table 1, MaxV and MinV represent the theoretical maximum and minimum possible values of vital signs, respectively. T and T represent the high and low thresholds for vital signs for patients, respectively.

The rate of alerts can be given as product of frequency of monitoring and the probability that vital signs exceed the thresholds. Multiplying this further with the number of patients, we derive the rate of alerts generated as

![](/api/attachments/UATC27GA/fulltext/images/c5a5e4d5a7be4eec34ab34567fe6c408efb086155df204e1b84cc3675c438eff.jpg)  
Fig. 6. Display of alerts and related information for healthcare professionals.

![](/api/attachments/UATC27GA/fulltext/images/1ee968926c0b8d603b4510b47dd662858bb9b57f1d960e694dfded48bda587ba.jpg)  
Fig. 7. Simpli<sup>fi</sup>ed Decision Making for Healthcare Professionals

$$
\lambda_ {\mathrm{AL-SIM}} = \mathrm{N} _ {\mathrm{P}} \cdot \text { FoM } \cdot (\text { MaxV } - \mathrm{T} _ {\mathrm{H}} + \mathrm{T} _ {\mathrm{L}} - \text { MinV }) / (\text { MaxV } - \text { MinV })\tag{1}
$$

where $\mathrm { N _ { P } }$ is the number of patients and FoM is the frequency of monitoring. MaxV and MinV represent the theoretical maximum and minimum possible values of vital signs, respectively. $\mathrm { T _ { H } }$ and T represent the high and low thresholds for vital signs for patients, respectively.

For enhanced mobile health system (EMHS), the number of alerts a given time can be expressed in terms of number of times vital signs were monitored and number of times they exceeded the contextsensitive thresholds

$$
\lambda_ {\mathrm{AL-EN}} = \lambda_ {\mathrm{AL-SIM}} \cdot P _ {C A}\tag{2}
$$

where $\mathrm { P _ { C A } }$ is the probability that context-aware operation results in detecting the real emergency, thus reducing the “false positive” alert, which would have gone undetected in Eq. (1). $\mathrm { P _ { C A } }$ can be computed by including all informational items, their probabilities and assigned weights.

As all alerts are treated at the same priority, the delay for an alert or time to intervene by a healthcare professional can be given as

$$
\mathrm{D} _ {\mathrm{AL}} = 1 / (\mu_ {\mathrm{AL}} - \lambda_ {\mathrm{AL}})\tag{3}
$$

where μ or average processing rate for alerts can be expressed as $1 / \left( \mathrm { N } _ { \mathrm { S C R E E N } } \cdot \mathrm { T } _ { \mathrm { S C R E E N } } + \mathrm { N } _ { \mathrm { S T E P S } } \cdot \mathrm { T } _ { \mathrm { S T E P } } \right) . \mathrm { N } _ { \mathrm { S C R E E N } }$ is the number of times screen of mobile device was switched and T<sub>SCREEN</sub> is the screen switching time. $\mathsf { N } _ { \mathsf { S T E P S } }$ is the number of steps and ${ \mathrm { T } } _ { \mathrm { S T E P } }$ is the time spent on each step by a healthcare professional in processing of an alert. The number of overlapping alerts can be given as

$$
\mathrm{N} _ {\mathrm{AL-OL}} = \lambda_ {\mathrm{AL}} / \mathrm{D} _ {\mathrm{AL}}.\tag{4}
$$

The delays for alerts with and without context-awareness are shown in Fig. 9. When context-awareness is utilized, we consider multiple cases when the number of alerts is reduced to 95%, 90%, 85% and 80% of the original values. The processing delay for alerts is signi<sup>fi</sup>cantly improved for these cases, as the number of patients per healthcare professional is increased. We limited the maximum number of patients per healthcare professional to be 20. The delays will increase signi<sup>fi</sup>cantly as the number of patients is increased under a healthcare professional responsible for receiving and processing alerts. More work is needed in evaluating different scenarios of multiple healthcare professionals and routing of alerts to healthcare professional with least load and/or faster response time.

## 4.2. Modeling estimated load & errors

In modeling estimated load, we focus on the load on working memory as long-term memory is assumed to be unlimited, thus not affecting the estimation in cognitive load. The decision making process will have two phases: processing phase and action phase, where a healthcare professional could experience different cognitive loads. The maximum cognitive load experienced by healthcare professional is the higher of these two values, thus

$$
\mathrm{CL} _ {\text { MAX }} = \operatorname{Max} (\mathrm{CL} _ {1}, \mathrm{CL} _ {2})\tag{5}
$$

where $\mathrm { C L } _ { 1 }$ represents the cognitive load in thought-processing phase and is estimated as $\mathrm { N _ { A L - O L } + N _ { V I S U A L } }$ . CL represents the cognitive load in action-taking phase and is estimated as $\mathsf { N } _ { \mathsf { S C R E E N } } + \mathsf { N } _ { \mathsf { S T E P S } }$

$\Nu _ { \tt A L - O L }$ the number of overlapped alerts can be derived from Eqs. (1) and $( 2 )$ . Without the proposed enhancements, $\mathsf { N } _ { \mathrm { V I S U A L } }$ would include all informational items in the decision making, thus

$$
N _ {\text { VISUAL - SIM }} = N _ {\text { DM - SIM }} = N _ {\text { A }} + N _ {\text { HIS }}\tag{6}
$$

Table 1 List of notations.

<table><tr><td>Symbol</td><td>Meaning</td><td>Symbol</td><td>Meaning</td></tr><tr><td>A</td><td>The number of visual items that have been converted to auditory items</td><td> $N_{AL-OL}$ </td><td>The number of overlapping alerts</td></tr><tr><td> $C_A$ </td><td>The number of changed parameters in an alert</td><td> $N_{DM}$ </td><td>The total number of information items needed in decision making</td></tr><tr><td> $CL_{MAX}$ </td><td>The estimated cognitive load</td><td> $N_{DM-EN}$ </td><td>The total number of information items needed in decision making in enhanced case</td></tr><tr><td> $CL_1$ </td><td>The estimated cognitive load during processing phase</td><td> $N_{HIS}$ </td><td>The number of items from history needed in decision making</td></tr><tr><td> $CL_2$ </td><td>The estimated cognitive load during action phase</td><td> $N_P$ </td><td>The number of patients</td></tr><tr><td> $CL_I$ </td><td>Represents cognitive load of ith task</td><td> $N_{SCREEN}$ </td><td>The number of screen changes in decision making</td></tr><tr><td> $D_{AL}$ </td><td>The alert delay or time to intervene</td><td> $N_{STEPS}$ </td><td>The number of steps in decision making</td></tr><tr><td>FoM</td><td>The frequency of monitoring (of vital signs)</td><td> $N_{VISUAL}$ </td><td>The number of visual items in decision making</td></tr><tr><td> $λ_{AL-SIM}$ </td><td>The average rate of alerts in simple case</td><td> $N_{VISUAL-SIM}$ </td><td>The number of visual items in decision making in simple case</td></tr><tr><td> $λ_{AL-EN}$ </td><td>The average rate of alerts in enhanced case</td><td> $P_{CA}$ </td><td>The probability that context-aware protocols detect an emergency</td></tr><tr><td>m</td><td>The slope of working memory capacity</td><td> $T_L$ </td><td>The lower threshold for a vital sign</td></tr><tr><td> $μ_{AL}$ </td><td>or average processing rate for alerts</td><td></td><td></td></tr><tr><td>MaxV</td><td>The maximum value of a vital sign</td><td> $T_H$ </td><td>The higher threshold for a vital sign</td></tr><tr><td>MinV</td><td>The minimum value of a vital sign</td><td> $T_{SCREEN}$ </td><td>The screen switching time</td></tr><tr><td>N</td><td>The number of tasks in time T</td><td> $T_{STEP}$ </td><td>the time spent on each step by a healthcare professional in processing of an alert</td></tr><tr><td> $N_A$ </td><td>The number of parameters in alert message</td><td>WMC</td><td>The maximum working memory capacity at time = 0</td></tr></table>

![](/api/attachments/UATC27GA/fulltext/images/70043fb8b1fb46b29af1718517cb70d6f18785b6fb1ee17aafb9564b0a13d64b.jpg)  
Fig. 8. The model used in the evaluation.

where $\mathrm { N } _ { \mathrm { D M - S I M } } \mathrm { i }$ is the number of items needed for decision making and is a function of the number of parameters in alert message $\left( \mathsf { N } _ { \mathrm { A } } \right)$ and the number of relevant items in patient history $( \mathsf { N } _ { \mathrm { H I S } } )$

$\mathsf { N } _ { \mathrm { V I S U A L } }$ for the enhanced mobile health system would be reduced by $\mathsf { A } ,$ the number of visual items that have been converted to auditory items, therefore

$$
N _ {\text { VISUAL - EN }} = N _ {\text { DM - EN }} - A = C _ {A} + N _ {\text { HIS }} - A\tag{7}
$$

where $\mathsf { N } _ { \mathrm { D M - E N } }$ is the number of items needed for decision making and is equal to the number of parameters reported in context-aware alert message $\big ( \mathsf { C } _ { \mathsf { A } } \big )$ and the number of relevant items in patient history $( \mathsf { N } _ { \mathrm { H I S } } ) . \mathsf { C } _ { \mathsf { A } }$ is the number of changed parameters and thus $\mathsf { C } _ { \mathsf { A } } < = \mathsf { N } _ { \mathsf { A } }$ (the number of parameters in an alert). For alert generation and processing systems, $\mathsf { C } _ { \mathsf { A } }$ is likely to vary from 1 to 3 implying 1 to 3 vital signs have been changed, while $\Nu _ { \mathrm { A } }$ is likely to be between 5 and 8 representing the all vital signs and biomedical parameters of interest. A represents the number of visual items converted to auditory items.

Next $\mathsf { N } _ { \mathsf { S C R E E N } }$ or number of screen switching can be given as ${ \mathrm { N } } _ { \mathrm { D M } } / { \cal S } ,$ where S is the number of items that can be displayed on a mobile device. S can range from 1–3 for a smart phone to 8–10 for a tablet computer. N is the number of steps and can be reduced by displaying the most important information and context-sensitive decision steps.

To reduce cognitive load (and related errors in alert-response), the goal is to minimize $\mathrm { N _ { A L - O L } , N _ { S C R E E N } , N _ { V I S U A L } }$ and $\mathsf { N } _ { \mathsf { S T E P S } }$ . The value of Ndepends on the total number of items needed for decision making and the number of items that can be displayed on one screen, which will be smaller for handheld/mobile devices. N can be reduced by adjusting the interface to healthcare professionals. Various combinations can be attempted to minimize cognitive load.

![](/api/attachments/UATC27GA/fulltext/images/29a56a331576672d3c8ca610c8bf3cf32b58b9faf33bfed8a2ca2e620eba6ca7.jpg)  
Fig. 9. Improved response time for alerts with context-awareness

Next we derive the probability of errors in alert-response based on cognitive load of tasks and available working memory capacity. The WMC may decline during a shift due to residual impact of tasks as shown in Fig. 10(a) or may remain constant. We model this as shown in Fig. 10(b), where slope of WMC-time can be made zero to represent constant WMC during a shift. Any decline in WMC during a shift can increase the probability of error in alert-response. Also, the level of expertise may be modeled as reduced slope of WMC-time and/or higher value of WMC.

The estimated error in alert-response is given by the probability of cognitive load of the task exceeding the current working memory capacity of the healthcare professional. The long-term memory capacity is assumed to be too large to have any effect on the current task. The estimated error in alert-response can be expressed over the entire duration T as Probability $( \mathbf { C L } _ { \mathrm { I } } > \mathsf { W M C } _ { \mathrm { I } } )$ , which can be expressed using normalization as

$$
= (1 / N) \sum_ {1 = 1} ^ {N} \operatorname{Max} (\operatorname{Min} ((\mathrm{CL} _ {\mathrm{I}} - \mathrm{WMC} _ {\mathrm{I}}) / \mathrm{WMC}, 1), 0)\tag{8}
$$

and WMC can be further expressed as $\mathrm { W M C - \ m . T . I / N . }$ CL represents cognitive load of Ith task, N is the number of tasks in T, m is the slope of working memory capacity, and WMC is the maximum working memory capacity $\mathsf { a t t } = 0 .$ Without design enhancements, $\mathrm { C L } _ { \mathrm { I } }$ is kept at WMC. For enhanced mobile health system (EMHS), $\mathrm { C L } _ { \mathrm { I } }$ is found to be smaller.

The impact of increased number of overlapping alerts to a healthcare professional is shown in Fig. 11. The number of overlapping alerts is a function of alert generation (with or without context-awareness), condition of patients, and the processing time for the healthcare professional. We found that cognitive load without proposed enhancements was always more than 9, thus exceeding the “normal” cognitive capacity range of working memory 5 to $) ( 7 - 2 \tan 7 + 2 )$ according to cognitive load theory. When multiple enhancements were utilized, the cognitive load was signi<sup>fi</sup>cantly reduced and came to a highly desirable value. For example, when $\mathsf A = 2$ implying 2 information items were converted to auditory item, the cognitive load was reduced to the desirable value for most cases. However, for $\mathrm { A } = 4 ,$ , the load was always in the desirable range even when a maximum of 5 overlapping alerts had to be dealt simultaneously by the healthcare professional.

We also varied the number of items in decision making from 4 to 16 and found that without enhancements, higher cognitive load occurs even when the number of items was 8. However, the proposed enhancements resulted in desirable values even when the number of items was increased to 12, which is much higher than what is likely to occur in most healthcare decision making situations in mobile health (Fig. 12).

Next we estimate the error in alert-response that can happen due to the cognitive load of a task being higher than the current working memory of a healthcare professional. Without enhancements, we estimate that over 10 h and 20 cases and sharp decline in working memory, the probability of errors can be as high as 25%. The probability is much lower when the tasks are mediated by enhanced mobile health systems with 10% and 20% reduction in cognitive loads from Eqs. (5) and (6) even for a high rate of decay of working memory. This is shown in Fig. 13.

(a) Residual Effect in Working Memory  
![](/api/attachments/UATC27GA/fulltext/images/4f67f1cda32deddaa5b6fa8c9b41cfdf5d0017f397bc521dd7514723171c3921.jpg)  
(b) Cognitive load of tasks and WMC during shift

![](/api/attachments/UATC27GA/fulltext/images/6fc7bd593e47cde7f702d166d43e28e3b22412e4dbf0ff60e440e2bf3c963739.jpg)  
Fig. 10. Residual effect and WMC.

Next we estimate the probability of error in alert-response for a range of tasks. These range from simple, routine, and complex tasks. Without enhancements, the error rate could be as high as 55% for the complex task, while the enhanced system could bring this to 0–15% range. The probability of error was much lower for less complex tasks (Fig. 14). Certainly, more work is needed in reducing the error rate to even a lower value, with additional enhancements in mobile computing, devices and interfaces.

The ability to convert visual items to auditory items has a major impact on cognitive load as well as error in alert-response. The use of enhanced mobile health system can reduce the probability of error in alert-response even under high rate of memory decay re<sup>fl</sup>ecting the tiredness of healthcare professional. The complexity of tasks can be reduced by speci<sup>fi</sup>c design enhancements including the use of auditory informational items. The resulting decline in cognitive load leads to lower probability of error in alert-response by healthcare professionals.

![](/api/attachments/UATC27GA/fulltext/images/cb16e09e9beb4c09f2d81124dd5f693193debbb6a7acdec59427f66bf0114a02.jpg)  
Fig. 11. Impact of overlapping alerts on estimated cognitive load.

## 5. Discussion

In this paper, we focused on how enhancements can be designed and added in mobile technologies to support mobile health. This work can be considered a part of the big picture of decision making in mobile health, which is an area of signi<sup>fi</sup>cant complexity and importance. The enhancements were designed to (a) reduce the amount of information by context-aware operation of mobile technologies and (b) to improve the presentation of information to healthcare professionals. These enhancements were designed using a cognitive load model and evaluated using an analytical model. The results show that information reduction and improved display could reduce the load of healthcare professionals and improve the quality of decisions for some tasks related to alert generation and decision making in health monitoring.

In the context of health monitoring, our propositions were (a) the alert-response time will improve by using context-awareness in alert generation, and (b) carefully designed mobile computing systems can reduce the cognitive load and thus error rate in alert response. We found support for both of these propositions from our results in Section 4. When context-awareness is utilized, and the number of alerts is reduced to 95%, 90%, 85% and 80% of the original values, the processing delay for alerts is signi<sup>fi</sup>cantly improved for these cases, as the number of patients per healthcare professional is increased. The alert-response time was signi<sup>fi</sup>- cantly lower when context-aware operation resulted in 20% less alerts. The ability to convert visual items to auditory items has a major impact on cognitive load as well as error in alert-response for health monitoring. The use of enhanced mobile health system can reduce the probability of error in alert-response even under high rate of memory decay re<sup>fl</sup>ecting the tiredness of healthcare professional involved in decision making in health monitoring. The complexity of tasks can be reduced by speci<sup>fi</sup>c design enhancements including the use of auditory informational items. The resulting decline in cognitive load leads to lower probability of error in alert-response by healthcare professionals, speci<sup>fi</sup>cally in decision making in health monitoring.

![](/api/attachments/UATC27GA/fulltext/images/2b430919105f7906523133022c1d6eb4a7a387948e7f9f47cf054da9cdacc861.jpg)  
Fig. 12. Estimated cognitive load for number of informational items.

![](/api/attachments/UATC27GA/fulltext/images/fe875a95d20975ba8bb35ae8bc62a4075374699c22258d30ccbd6dd0d8b872a1.jpg)  
Fig. 13. Reduction in error in alert-response by proposed enhancements

The work presented here on alert generation and processing in health monitoring can be expanded to study other decisions and their impact on mobile health. A signi<sup>fi</sup>cant amount of research is needed to study various challenges in decision making processes in mobile health. We hope that the work will inspire other researchers to address more complex decision making in mobile health.

## 6. Conclusions and future research

In this paper, we addressed how mobile health can be better supported by enhancements in mobile devices and networks. More specifically, we presented two sets of enhancements, namely (a) contextawareness and (b) improved presentation of information to healthcare professionals. These enhancements are then applied in the design of an alert generation and processing system, where decisions related to alert processing are made by healthcare professionals using mobile devices. The enhancements supported an improved presentation of information by suitable displays, personalization of healthcare professional's devices, color coding of conditions, and display of most important information <sup>fi</sup>rst.

![](/api/attachments/UATC27GA/fulltext/images/1c3a36e25e4664063f7be271bdd4911d38b7fad8c7513591a29e33da0f679980.jpg)  
Fig. 14. Reduction in error in alert-response for different task-complexity.

The performance was measured using an analytical model. We found that the number of alerts and the number of visual items were reduced, thus reducing the number of informational items a healthcare professional has to process. This along with personalization of user interface supported the improved presentation of information. The number of steps in decision making could be further reduced, but the complexity of individual steps may lead to some increase in the load. The trade-offs of these two factor on cognitive load could lead to some very interesting research that we are currently pursuing and will be addressed in a subsequent paper.

There are many signi<sup>fi</sup>cant challenges that must be addressed in future research in mobile health. This can include challenges such as (a) design and implementation of suitable enhancements, (b) testing of enhanced systems with healthcare professionals in a variety of settings, and (c) design of suitable interfaces for mobile devices in healthcare. It is our hope that this paper creates more awareness of important research challenges and opportunities for researchers in mobile health and related areas.

We classify some opportunities and challenges in mobile health as follows:

• Mobile computing challenges: how existing and emerging technologies can be tailored to improve quality of care, improved health and overall quality of life for both patients and healthcare professionals? More speci<sup>fi</sup>cally what and how suitable enhancements can be designed, developed and implemented for improved care?

• Information quality challenges: how mobile health needs and utilizes the “right” information at the “right” time at the “right” speed at any location? Also, how information quality will affect the overall quality of care?

• Healthcare professionals' challenges: how mobile health will affect the cognitive load and decision making by healthcare professionals? What can be done to reduce the complexity and the quality of decision making in mobile health?

• Interoperability challenges: How data from multiple sources will interoperate and lead to usable and current information in mobile health decisions and delivery of service?

• Security and privacy challenges: How different components of mobile health will work together to allow the “anytime” “anywhere” information to “anyone authorized”?

Several comments can be made here in relation to the above challenges and opportunities. Mobile technologies allow information to be made available quickly, but cannot improve the quality of information it is presenting to the patients or healthcare professionals. However, how information is presented to healthcare professionals can affect their load and resulting quality of decisions. The enhancements that are designed to reduce the amount of information should also consider any loss of healthcare information and its impact on decision making. The enhancements should be tested in clinical setting for usefulness and should be improved based on how healthcare professionals make decisions.

More work is needed in identifying how mobile technologies will affect cognitive load for a range of healthcare professionals covering ex perts and not-so experts, preventive and emergency care, common and rare conditions, and physical and mental illnesses. Work is also needed to study the intersections among (a) the quality of decisions by healthcare professionals, (b) the quality of healthcare delivery and quality of life for patients and (c) the quality of life for healthcare professionals.

## Appendix A. Supplementary data

Supplementary data to this article can be found online at http://dx. doi.org/10.1016/j.dss.2014.03.005.

## References

[1] G. Groopman, How Doctors Think, Houghton Mif<sup>fl</sup>in, Boston, 2008.

[2] A. Kushniruk, V. Patel, Cognitive evaluation of decision making processes and assessment of information technology in medicine, International Journal of Medical Informatics 2 (51) (1988) 83–90.

[3] A. Laxmisan, F. Hakimzada, O. Sayan, R. Green, J. Zhang, V. Patel, The multitasking clinician: decision-making and cognitive demand during and after team handoffs in emergency care, International Journal of Medical Informatics 11 (76) (2007) 801–811.

[4] F.-Y. Kuo, C.-W. Hsu, R.-F. Day, An exploratory study of cognitive effort involved in decision under framing-an application of the eye-tracking technology, Decision Support Systems 48 (1) (2009) 81–91.

[5] M. Workman, M. Lesser, J. Kim, An exploratory study of cognitive load in diagnosing patient conditions, International Journal for Quality in Health Care 3 (19) (2007) 127–133.

[6] V. Patel, J. Zhang, N.A. Yoskowitz, R. Green, O.R. Sayan, Translational cognition for decision support in critical care environments: a review, Journal of Biomedical Informatics 41 (3) (2008) 413–431.

[7] J. Sweller, Cognitive load during problem solving: effects on learning, Cognitive Science 12 (1988) 257–285.

[8] U. Varshney, Pervasive Healthcare Computing: EMR/EHR, Wireless and Health Monitoring, First Edition Springer Verlag, New York, 2009.

[9] K.M. Simonic, A. Holzinger, M. Bloice, J. Hermann, K.M. Simonic, A. Holzinger, M. Bloice, J. Hermann, Optimizing long-term treatment of rheumatoid arthritis with systematic documentation, Proc. of 5th Inter. Conference on Pervasive Computing Technologies for Healthcare, PervasiveHealth, 2011.

[10] Bianying Song, et al., Decision support for teletraining of COPD patients, Proc. of 3rd Inter. Conference on Pervasive Computing Technologies for Healthcare, PervasiveHealth. 2009

[11] A.M. Cheriyan, Z. Kalbarczyk, R.K. Iyer, A.O. Jarvi, T.M. Gallagher, K.L. Watkin, Pervasive embedded real time monitoring of EEG & Sp02, Proc. of 3rd International Conference on Pervasive Computing Technologies for Healthcare, (PervasiveHealth) and Workshops, 2009.

[12] M. Hassinen, M. Marttila-Kontio, EMS coordination in large scale emergencies using automated patient monitoring Proc, of 2nd International Conference on Pervasive Computing Technologies for Healthcare, (PervasiveHealth) and Workshops, 2008.

[13] A. Copetti, O. Loques, J.C.B. Leite, T.P.C. Barbosa, A.C.L. da Nobrega, Intelligent contextaware monitoring of hypertensive patients, Proc. of 3rd International Conference on Pervasive Computing Technologies for Healthcare, PervasiveHealth, 2009.

[14] F. Wu, M. Williams, P. Kazanzides, K. Brady, J. Fackler, A modular clinical decision support system, Proc. of 3rd International Conference on Pervasive Computing Technologies for Healthcare, (PervasiveHealth) and Workshops, 2009.

[15] K. Farooq, A. Hussain, S. Leslie, C. Eckl, W. Slack, Ontology-driven cardiovascular decision support system, Proc. of 5th International Conference on Pervasive Computing Technologies for Healthcare, (PervasiveHealth) and Workshops, 2011.

[16] CLT: Cognitive Load Theory, From theories used in IS research: cognitive load theory, available at http://www.fsc.yorku.ca/york/istheory/wiki/index.php/Cognitive\_load\_ theory 2009.

[17] F. Wada, S. Tano, Basic system architecture for adaptive information presentation in high cognitive load environment, 26th Annual Conference of the IEEE Industrial Electronics Society, IECON 2000, Oct. 2000, pp. 515–520.

[18] P. Ayers, Using subjective measures to detect variations in intrinsic cognitive load within problems, Learning and Instruction 16 (2006) 389–400.

[19] L. Quiroga, M. Crosby, M. Iding, Reducing cognitive load, Proc. of 37th International Conference on System Sciences, Published by IEEE Computer Society Press, 2004.

[20] S.Y. Mousavi, R. Low, J. Sweller, Reducing cognitive load by mixing auditory and visual presentation modes, Journal of Education Psychology 87 (2) (June 1995) 319–334.

[21] M. Skov, R. Hoegh, Supporting information access in a hospital ward by a contextaware mobile electronic patient record, Pervasive and Ubiquitous Computing, (10) 4, Springer-Verlag, 2006, pp. 205–214.

[22] J. Favela, M. Rodriguez, A. Preciado, V.M. Gonzalez, Integrating context-aware public displays into a mobile hospital information system, IEEE Transactions on Information Technology in Biomedicine 3 (8) (2004) 279–286.

[23] U. Varshney, A framework for context-aware wireless wellness monitoring, Proc. IEEE Wireless Telecom Symposium, 2012

[24] S. Sneha, U. Varshney, Enabling ubiquitous patient monitoring: model, decision protocols, opportunities and challenges, Decision Support Systems 46 (3) (2009).

[25] U. Varshney, A framework for supporting emergency messages in wireless patient monitoring, Decision Support Systems 45 (4) (2008).

[26] A. Dey, G. Abowd, Towards a better understanding of context and contextawareness, Tech Report, GIT-GVU-99-22, June 1999.

[27] G. Mostifaoui, J. Pasquier-Rocha, P. Brkzillon, Context-aware computing: a guide for the pervasive computing community, Proc. IEEE/ACS International Conference on Pervasive Services (ICPS), 2004, pp. 39–48

Upkar Varshney is currently Associate Professor of Computer Information Systems at Georgia State University Atlanta. His current interests include mobile health pervasive computing, and wireless networks. He has authored over 170 papers including more than 70 in national and international journals. He is the author of Pervasive Healthcare Computing, published by Springer in 2009 and 2010. According to Google Scholar, his papers have been cited more than 4000 times. He is the founding co-chair of International Pervasive Health Conference was the program co-chair for Americas Conference on Information Systems (AMCIS-2009). He has served or is serving as an editor for IEEE Transactions on IT in Biomedicine, IEEE Access MegaJournal, Decision Support Systems (DSS), and IEEE Computer.
