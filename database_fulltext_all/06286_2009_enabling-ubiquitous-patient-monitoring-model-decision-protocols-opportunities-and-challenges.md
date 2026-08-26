---
otero_id: 6286
otero_key: "3BPCEWNK"
title: "Enabling ubiquitous patient monitoring: Model, decision protocols, opportunities and challenges"
authors: "Sweta Sneha; Upkar Varshney"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.11.014"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Enabling ubiquitous patient monitoring: Model, decision protocols, opportunities and challenges

Sweta Sneha ⁎, Upkar Varshney

Department of Computer Information Systems, Georgia State University, Atlanta GA 30302, USA

a r t i c l e i n f o

Available online 21 November 2008

Keywords: Patient monitoring Ad hoc wireless networks Healthcare Technology

## a b s t r a c t

Healthcare costs in the US are approximately 15% of GNP and are anticipated to reach 17% of GNP in the near future. Management of chronic diseases via technology based ubiquitous patient monitoring services has been widely proposed as a viable option for economizing healthcare resources, and providing ef<sup>fi</sup>cient, quality healthcare. The process of ubiquitous patient monitoring is information intensive, the information generated is not only fragmented but also spans multiple processes, artifacts, parameters, and decision criteria. The current study explores the complexities associated with the process of ubiquitous patient monitoring and the enabling technologies. The key contribution is a framework that captures the complex processes, the parameters involved, and the decision criteria for ubiquitous patient monitoring. The decision protocols and enabling technologies supporting the processes are detailed in the study along with the opportunities and challenges of ubiquitous patient monitoring. A conceptual model of ubiquitous patient monitoring is developed by leveraging the proposed framework and is validated by a usage scenario. Finally, the implications of future research and contributions of the current research are discussed.

Published by Elsevier B.V.

## 1. Introduction

Healthcare forms an indispensable constituent of the modern society, representing a large percentage of Gross National Product (GNP) and sustaining a high political pro<sup>fi</sup>le and strong public interest [5]. In the wake of the 21st century, healthcare systems around the globe are faced with an exponential rise in expenses, heavy utilization of services associated with a steep rise in aging population, and limited <sup>fi</sup>nancial as well as human resources to manage the growing healthcare needs [13,48]. The current healthcare expenses in the US are approximately 15% of the GNP [25] and projected to reach 17% of the GNP by 2011 [6]. Another trend observed parallel to the rising healthcare costs is the “graying of the globe” — the worldwide population of adults over 65 years of age is on the rise and is expected to reach 761 million by 2025 [46,63]. Fig. 1 depicts the changing global demographics, the resultant increase in the number of aging patients, and the corresponding strain on both the human as well as <sup>fi</sup>nancial resources of the healthcare sector.

Multiple studies in the past have noted the prevalence of chronic diseases in the aging population — seven of the most prevalent chronic illnesses in the US (and their associated in-patient expenses) include: coronary artery diseases (\$25.6 billion), heart failure (\$15.2 billion), chronic obstructive pulmonary diseases (\$6.2 billion), mental health disorders (\$3.9 billion), diabetes (\$3.8 billion), hypertension (\$3.2 billion) and asthma (\$1 billion) [6]. Medicare's high-risk patients, approximately 8 million currently, with <sup>fi</sup>ve or more chronic diseases account for approximately 78% of all health care spending — well over a trillion dollar per year and/or over two-thirds of Medicare's annual spending [3,6,17]. Many healthcare experts agree that current Medicare expense patterns are a re<sup>fl</sup>ection of chronic illnesses managed unsuccessfully [6]. A large percentage of chronic diseases deteriorate to the point where a crisis is reached resulting in unnecessary long-term hospitalization at massive cost to the healthcare sector. A critical inference drawn from epidemiological data and past studies is that preventing occurrences of acute episodes holds the key to providing quality healthcare, reducing incidences of prolonged hospitalizations and resultant healthcare expenses [43]. In order to reduce preventable acute episodes from occurring, it is critical to focus on preclusion of crisis/complications, proactive management of chronic illnesses, and timely detection of anomalies such that patients can lead a normal, healthy lifestyle outside of the hospitals.

Innovative strategies are needed to tackle the spiraling healthcare expenses and to cater to the healthcare needs of an aging population in addition to sustaining the trend towards an independent lifestyle focusing on personalized non-hospital based care [46,60]. One strategy is deployment of a large number of trained healthcare professionals to handle the current healthcare scenario involving chronic illnesses. However, there are two key constraints associated with heavy utilization of human resources towards timely detection of anomalies, prevention of complications, disease management, education/guidance with respect to medications, exercise, and diet (within the context of chronic illnesses): (1) healthcare professionals are limited and over-worked; (2) human resources constitute the most

![](/api/attachments/3BPCEWNK/fulltext/images/c1e67c82901bfd5bd95da71420938fb3ceba74b1d2661f06a7eff37009afbde7.jpg)  
Increasing Patient Population

Fig. 1. Changing global demographics and resultant healthcare needs.

expensive variable in the healthcare sector. Thus heavy utilization of human resources will not only increase the cognitive overload of the healthcare professionals, but will also increase healthcare costs.

This research explores ubiquitous monitoring of chronic patients as a potential solution that seeks to: (1) leverage ubiquitous biomedical sensing, computing, and communication technologies to complement and assist healthcare professionals in efficiently managing chronic illnesses 24× 7, (2) reduce incidences of unnecessary hospitalizations due to undetected complications, (3) provide timely detection of anomalies before it snowballs into a crisis, and (4) provide pertinent medical attention utilizing the expertise of the healthcare professionals for handling anomalies “just-in-time” as and when needed without time and/or location dependency [5,14]. The population targeted for ubiquitous monitoring consists of Medicare's high-risk patients suffering from multiple chronic illnesses and incurring the lion's share (over a trillion dollar) in annual healthcare expenses. Ubiquitous patient monitoring does not intend to replace existing healthcare systems, practices, and personnel instead it seeks to assist and complement the functioning of the existing healthcare systems towards efficient utilization of resources and reducing unnecessary expenses incurred due to poorly managed chronic illnesses.

The market for patient monitoring services is a multi-billion dollar industry [61] that holds the potential to reducing unnecessary healthcare costs while providing quality care to an aging populace. Hence there is an imminent need to fully explore the domain of ubiquitous patient monitoring with respect to critical factors and enabling technologies. However, there is a dearth of research focusing on speci<sup>fi</sup>c understanding of the role of technology based ubiquitous monitoring of patients in improving the practice and delivery of healthcare. Thus the goal of the current research is to:

• Explore the paradigm of ubiquitous patient monitoring within the context of chronic illnesses focusing speci<sup>fi</sup>cally on successful disease management i.e., preventing incidences of unnecessary complications, prolonged hospitalizations, and corresponding expenses;

• Provide clear guidelines focusing on the process of patient monitoring, key parameters involved, decision logic, and an understanding of the technology enabling ef<sup>fi</sup>cient and effective ubiquitous monitoring of chronic illnesses.

Active patient involvement within the ubiquitous patient monitoring paradigm seeks to reduce the mental as well as physical strain of the healthcare professionals, increase complianceto treatment, reduce unexpected hospitalization expenses and promote a better, healthier lifestyle of patients outside the hospital. The sole purpose of this research is to explore the utility of ubiquitous patient monitoring as a means of effective and ef<sup>fi</sup>cient utilization of limited healthcare resources towards an ef<sup>fi</sup>cient healthcare delivery within the context of chronic illnesses and corresponding expenses. The next section articulates the concept of ubiquitous patient monitoring, the associated requirements/challenges, and the enabling technologies.

## 2. Ubiquitous patient monitoring

Ubiquitous Patient Monitoring is a concept that has its roots in the vision of Mark Weiser — the father of ubiquitous computing. His vision of ubiquitous computing is captured beautifully in the following quote: “The most profound technologies are those that disappear. They weave themselves into the fabric of everyday life until they are indistinguishable from it” [62]. Healthcare seems to be the most fertile ground for ubiquitous computing applications since there is no other domain where the importance of making correct decision based on obtaining the right information at the right time is more critical [39,62].

The promise of ubiquitous patient monitoring is an environment constituted <sup>fl</sup>awlessly by enabling technologies that promote continuous, reliable monitoring of patient speci<sup>fi</sup>c medical information without any dependence on time and location such that prompt medical intervention is provided as and when needed. The information obtained is analyzed via ubiquitous computing technologies for timely detection of anomalies and promoting compliance. Consequently, ubiquitous monitoring solutions, both short term and long term at patients' homes, nursing homes, and hospitals, are increasingly seen as a viable option for disease management, reduction in episodes of preventable hospitalizations, corresponding expenses, and provisioning of healthcare services “just in time” as and when needed [41].

The de<sup>fi</sup>nition of ubiquitous patient monitoring involves two perspectives, one being the domain of application of the technologies enabling ubiquitous computing and the other being the concept that integrates healthcare more seamlessly to our everyday life [27]. Ubiquitous patient monitoring is not merely a technological innovation; it involves a paradigm shift in healthcare practice, delivery and view. This paradigm shift implies technical applications of consumer-operated interoperable standard technologies for health and wellness leveraging the advances in the three classes of technology — ubiquitous sensing/ monitoring, computing, and communication such as: PDA (Personal Digital Assistant), mobile phones, and communication networks. At the level of the healthcare organization, ubiquitous healthcare implies a change from physician-centric systems to patient-centric operational models [28].

Ubiquitous patient monitoring services seek to assist the physicians in managing chronic illnesses and not replace their expertise. While ubiquitous patient monitoring services focus on promoting compliance and detection of anomalies, the focus of the physicians is on provision of pertinent medical attention as and when an anomaly is detected without any delays. The core responsibilities of the healthcare professionals will shift from monitoring patient conditions arising from mismanagement of diseases and undetected anomalies to provision of medical expertise. Ubiquitous technology will step in to take care of the standard, repetitive tasks of monitoring vital signs and promoting compliance with medical advice, performing analysis, and requesting medical assistance only when required.

A multi-dimensional model of ubiquitous patient monitoring depicting the enabling technologies, the bene<sup>fi</sup>ts to the healthcare sector, and the various facets of healthcare services that can potentially be supported in such an environment is depicted in Fig. 2.

## 2.1. Ubiquitous patient monitoring — requirements/challenges

The requirements of patient monitoring are not only diverse supporting indoor and outdoor, as well as stationary and mobile patients but are also complex, and involve multiple parameters such as: duration of monitoring, frequency of data collection and transmission, amount of data transmitted, nature of monitoring such as: alert, periodic or continuous. The following overview of the requirements of patient monitoring shows the complexity, diversity, and somewhat contradictory nature of the requirements. Fig. 3 graphically depicts a conceptual classi<sup>fi</sup>cation of the diversity and complexity of patient monitoring requirements.

![](/api/attachments/3BPCEWNK/fulltext/images/7b392ecc25a1b2c0581797c98f29bdc19c65b5c9ae6d4ad63d3b8a843acf35e8.jpg)  
A Multi-Dimensional Model of Ubiquitous Patient Monitoring Environment Fig. 2. A multi-dimensional model of ubiquitous patient monitoring environment.

## 2.1.1. Monitoring and transmission

Patient monitoring can be continuous, alert driven (on the detection of an abnormal event) or periodic (at <sup>fi</sup>xed times in a day). Continuous monitoring and transmission can provide real-time data for analysis and storage but can also lead to an information overload of healthcare professionals and signi<sup>fi</sup>cant network traf<sup>fi</sup>c. Periodic monitoring and transmission sacri<sup>fi</sup>ces the real-time aspect for a decrease in network traf<sup>fi</sup>c and information overload and is suitable for patients under routine supervision. In alert driven monitoring, the patients are continuously monitored and the acquired data is analyzed for detection of anomalies. Only when an anomaly is detected and medical attention warranted, is a message transmitted over a network. This type of monitoring could result in a time lag in performing analysis and sending alert messages, however, a reduced information load on healthcare professionals who would otherwise be faced with the task of analyzing the incoming data and network traf<sup>fi</sup>c make it a possible choice in some instances of patient monitoring.

## 2.1.2. Reliability of message delivery

Due to the potentially life threatening situations, reliability of message delivery to healthcare professionals is the most critical requirement of patient monitoring. Routine transmission of signals from a patient can tolerate low reliability while emergency messages have the highest reliability requirement. Thus different monitoring messages can be prioritized based on the reliability requirements. The factors impacting reliability in infrastructure and ad hoc wireless networks based solutions include: network coverage, presence of dead spots, device range, available power, bit rate, routing protocol, failure(s) in the network or device, and un-cooperative behavior of other devices.

## 2.1.3. Reasonable time in message delivery

Any delay in message delivery can have fatal consequences. The priority of transmitted message (emergency or routine) can be used to determine the routing of messages by a network to reduce delays, which may be substantially impacted by frequency of monitoring, size of message transmitted, bit rate, and the number of monitored patients. The objective is to have minimum delay in end to end message delivery.

## 2.1.4. Power conservation

Power management of the low powered monitoring devices with diversity in the range of functionality and computing capabilities used for signal transmission poses a challenge in providing reliable patient monitoring solutions. The battery (power source for most wearable devices) typically forms the heaviest component; hence there is a tradeoff between carrying a heavy device and the frequency of recharging the battery. The critical factors impacting utilization of power include the frequency and size of transmitted messages and routing schemes employed for message transmission.

## 2.1.5. Support for mobile patients

Patient monitoring solutions should be able to support mobile patients indoor and outdoor. Patient mobility results in patients moving in and out of network coverage (in an infrastructure based network), thus negatively impacting reliability in patient monitoring. Hence the challenge is to design dependable networking support for monitoring both mobile and stationary patients.

## 2.1.6. Scalability

The patient monitoring network must scale well in terms of the number of monitored patients that can be reliably supported. The factors in<sup>fl</sup>uencing scalability are: bit rate, frequency of monitoring and transmission, and the amount of information transmitted per patient.

## 2.1.7. Manageable cognitive load for healthcare professionals

Analyzing continuous streams of data from monitored patients and making relevant diagnosis can be an arduous task for the healthcare professionals. It can also impact network traf<sup>fi</sup>c and scalability of the patient monitoring systems. The solution promised by the ubiquitous patient monitoring environment is utilization of the computational capabilities of the monitoring devices for intelligent analysis and deductions, and alerting the healthcare professionals only when an anomaly is detected. The collected information can be accessed by the healthcare professionals (if required) to make informed decisions and closely strategize diagnosis, treatments/outcomes, and patient education towards prevention of crisis and reducing episodes of preventable hospitalizations.

![](/api/attachments/3BPCEWNK/fulltext/images/ba565f78df6ef1163f40d40cb0aa78ef6b6272d0093fe6d8ccb629350faa9b15.jpg)  
Fig. 3. A conceptual framework classifying patient monitoring requirements.

## 2.1.8. Confidentiality, security, and privacy

As healthcare information is being transmitted over wireless networks, efforts should be made to keep it con<sup>fi</sup>dential and private. Privacy entails the right of a user to control the collection and dissemination of personal information and security is the protection of user's information from unauthorized users. Privacy and security are one of the key challenges towards large scale adoption and diffusion of ubiquitous computing empowered by wearable devices [24,60]. But depending on the context privacy and security can be on the opposite ends of the spectrum where increasing security could imply lowering privacy and vice versa. This is expected to be one of the most critical requirements for healthcare administrators and government regulators.

## 2.1.9. Invisibility

One of the most promising concepts of ubiquitous healthcare is providing healthcare services pertaining to monitoring, treatment (reminders to take medication), prevention and management of diseases in a manner that causes minimal distraction and is unobtrusive in nature. The devices/computers promoting ubiquitous monitoring should disappear in the background, removing distractions by computers such that the patients can continue with their daily activities without being obstructed by the computers [13,39,62].

## 2.1.10. Proactivity and transparency

Proactivity and transparency refers to the intelligence in the ubiquitous healthcare environment which will be able to sense the current intent of the patient and proactively take certain actions on behalf of the patient. For instance: if the device senses that the patient's ECG has gone beyond a pre speci<sup>fi</sup>ed threshold then the intelligence in the device may want to alert the doctor of the situation and schedule an appointment as soon as possible along with informing the patient of the appointment. But this proactive action should be transparent to the patient as far as possible. The proactivity shouldn't become a source of annoyance.

## 2.1.11. Context awareness

Context awareness is in synch with proactivity since a patient monitoring environment cannot be proactive in assisting a user in decision making unless the right context information is available. For instance, if the patient's hear rate has gone up then the device must be aware of the context where and when the heart rate was high. If the patient was watching an exciting football game which caused the heart rate to go up while the vital signs from other sensors were within the normal range then the device should be able to detect the context and not send alerts. Context information can be recovered from sensors and would essentially contain information about who, what, when and where.

Table 1 presents the requirements/challenges associated with ubiquitous patient monitoring along with the various decision factors which characterize each requirement.

The technologies supporting ubiquitous monitoring of patients exists and is much more sophisticated today than their precursors a decade ago; however the utilization of such technologies for promoting ubiquitous monitoring of patients doesn't come without its own challenges. Despite of the limitations, there are massive opportunities and promises associated with ubiquitous patient monitoring. Some of the key limitations associated with the usage/ implementation:

• Feasibility analysis with respect to cost/bene<sup>fi</sup>t — healthcare sector is running in red and an analysis of the cost and bene<sup>fi</sup>ts in terms of <sup>fi</sup>nancial feasibility, return on investment, and quality of service issues focusing on reduction in hospitalizations and incidences of crisis are critical issues that are yet to be fully explored;

Table 1  
Requirements, decisions, and technology supporting patient monitoring

<table><tr><td>Requirement</td><td>Decision criteria and enabling technologies</td></tr><tr><td>Monitoring</td><td>What to monitor - BP, ECG, body temperature, blood Oxygen levelWhen to monitor - periodically (what time interval), continuouslyHow to monitor - via sensors, physically separate devices ex: thermometer, BP monitor.</td></tr><tr><td>Analysis</td><td>Analyze the collected information before transmission?What to analyze - the vital signs, the compliance factorsHow to analyze - based on stored thresholds, standardized dataHow/what to transmit - which network, patient&#x27;s location, current reading</td></tr><tr><td>Transmission</td><td>What to transmit - complete recorded data, differential data, personal informationHow to transmit - WLANs, cellular PCS/GSM, or ad hoc wireless networksWhen to transmit - periodically, continuously, alert based</td></tr><tr><td>Reliability</td><td>Reliability in sensing, analyzing and transmitting patient information via built in redundancyVarying reliability levels for transmitted messages?- High (emergency), medium (routine), low (reminders)- Reliability in communication enabled by utilizing multiple communication networks</td></tr><tr><td>Delays</td><td>Prioritized transmission. Low - emergency transmission, medium - routine transmission</td></tr><tr><td>Power conservation</td><td>Mobile computing and communication devices with power conservation methods such as sleep cycles, emergency power reserve, solar energy, innovation in conserving/charging devices.</td></tr><tr><td>Support for mobility</td><td>Patients mobile indoors/outdoors?Variation in mobility pattern - high/low speed, children/adults</td></tr><tr><td>Cognitive load on healthcare professional?</td><td>The analysis of the plethora of information collected patients monitored electronically can be an arduous task. However, the cognitive load on the healthcare professional should be low by automating the analysis of the obtained medical information and involving the healthcare professionals only when required.</td></tr><tr><td>Security, privacy, and confidentiality</td><td>High levels of security, privacy and confidentiality.Technologies with built in secure authentication processes, secure fool-proof communication resources, biomedical measurement/sensing devices, and patient specific intelligent devices</td></tr><tr><td>Proactivity and transparency</td><td>Varying levels of proactivity and transparency? Low -&gt; more input, high -&gt; low inputIntelligent environment with the potential of learning and reacting to anomalous conditions.</td></tr><tr><td>Invisibility</td><td>Pervasive presence/disappearance of computing/mobile communication resources, and sensing devices in everyday objects such as smart shirts</td></tr><tr><td>Context awareness</td><td>High level of context awareness in order to correctly analyze the collected information</td></tr></table>

• Acceptance/adoption by the healthcare professionals and target population — healthcare sector has traditionally been slower in adopting technological innovations in the practice and delivery of healthcare than other major sectors such as banking and automotive. EMR (Electronic Medical Records), although endorsed by the government and supported by several technology giants, has met with massive resistance in adoption and usage;

• Actual use of innovative technology based ubiquitous patient monitoring and related bene<sup>fi</sup>ts are additional important concerns that hasn't been assessed/quanti<sup>fi</sup>ed by any prior studies to the best of our knowledge.

## 3. Evolution of patient monitoring solutions

The current advancement in wireless communication technology and patient worn devices for medical telemetry has given a boost to monitoring solutions for patients inside and outside the hospital premises. It is now possible to record and transmit digitized vitals signs in the form of signals from a patient device to the computer or hand-held PDA of healthcare professional instantly, hence reducing the time taken for evaluation and treatment [14,16,26,35]. In the recent past, research and development community has given considerable attention to understanding and developing viable patient monitoring applications and research prototypes for accurately monitoring patients' vital signs and timely detection of anomalies [41]. Several companies, including General Electric, Hewlett Packard, Honeywell, and Intel, have teamed up in the Center for Aging Services Technologies (CAST) in Washington D.C., established in 2002, to encourage collaborative aging-related technology development and to advocate wireless, remote monitoring of patients, speci<sup>fi</sup>cally the aging populace that incurs the largest percentage of healthcare expenses.

First generation monitoring services, involve collection and transmission of data within a hospital using wireless LANs such as Micropaq that transmits multi-parametric information via Wireless LANs [57] and LifeSync [56], which uses short range wireless signals such as Bluetooth to move information within a hospital infrastructure. Next generation monitors, such as Medtronic [34], allow patients to live in their homes while required data is collected and transmitted at prede<sup>fi</sup>ned time — end of day or week. Motiva provides disease management and increased quality of life to the patients via a secure, personalized healthcare communication platform that connects chronic patients at home to their healthcare providers through their TV sets and cable systems for IP access [59]. Some monitors provide short term monitoring for 10–14 days with the intention to diagnose a patient's condition to match it with the correct treatment such as: CardioNet [52], and Biotronik [51]. A system for realtime monitoring of patients in the home environment is presented by [26], asthma in home monitoring via a video monitor and a secure website for uploading the relevant information is presented by [9], and unobtrusive wellness monitoring of elders via sensors by IST Vivago Wristcare with automatic alarm triggering capacity and communication over telephone lines [38]. Recently, prototypes and research have focused on providing monitoring solutions to mobile patients by exploring continuous collection and transmission of vital signs via infrastructure-based wireless network (Wireless LAN, Cellular PCS, and Satellites) [31,35,41]. Work on other related issues in patient monitoring include “smart health wearable” research [32], interference for telemetry devices [12], PDA as a mobile gateway [22], long-term health monitoring by wearable devices [1,45], and, smart shirt based health monitoring [58], a wearable stethoscope [29]. Clothing-embedded transducers for ECG. heart rate variability, and acoustical data and wireless transmission to a central server are proposed in [22]. A requirement model for delivering alert messages is presented in [23]. A design approach for data compression for a mobile tele-cardiology model is presented in [19l, where a significant compression ratio and reduction in transmission time over GSM network was achieved. Strategies for ef<sup>fi</sup>ciently working with digital medical images is described in [42]. Personal health monitors based on wireless body area network (BAN) of intelligent sensors are proposed for stress monitoring [21]. Alert Based continuous monitoring of Parkinson patients by intelligent wearable devices is described in [46]. Monitoring of Alzheimer patients in geriatric residents via an autonomous intelligent agent and effectiveness of remote asthma monitoring is described respectively in [8,11]. Numerous additional means of improving the delivery and quality of healthcare to patients via improved medical decision making is described in [4,15,30,49]. Empowered by technology promoting ubiquitous computing, there has been some research and development efforts for intelligent monitoring of patients in context aware, secure, smart environment for assisting elders to living independently, examples include Gator Tech Smart House [55], Aware Home Project [50], and Elite Care [44].

Although the prior body of research with respect to patient monitoring is noteworthy and has made some outstanding contributions, the primary limitations include the following: (1) the solutions proposed thus far have not delved in the realm of ubiquitous monitoring — thus being inherently constrained in terms of patient mobility, continuous monitoring and timely detection of anomalies, (2) majority of the solutions do not fully utilize the mobile, computational platform to perform analysis of biometric data prior to transmitting thus resulting in high network traf<sup>fi</sup>c, higher bandwidth requirement, and cognitive overload of the healthcare professional with the daunting job of analyzing streams of biometric data and detecting anomalous conditions. There is vast disparity in the degree of reliability and effectiveness of remote patient monitoring services as provided by commercially available portable monitors and research prototypes in the context of timely detection of anomalies and provision of medical attention. One potential source of such disparity can be attributed to the lack of understanding of the complex process, the associated parameters, and the decision protocols associated with patient monitoring solutions. The current study particularly adds value to the rich body of research by developing a concise framework that supports comprehensive, ubiquitous monitoring of chronic illnesses with the goal to: (1) provide timely detection of anomalies and prevent incidences of acute episodes thus reducing avoidable hospitalizations and corresponding expenses, (2) leverage the computational and processing capabilities of the technologies enabling ubiquitous monitoring such that the biometric data is transmitted to the healthcare professional only when an anomaly is detected and medical intervention is warranted; thereby leading to decreased cognitive overload and ef<sup>fi</sup>cient utilization of human resources, reduced network traf<sup>fi</sup>c and bandwidth requirement. Thus the objectives of the current research with respect to the paradigm of ubiquitous patient monitoring and its role in assisting the healthcare sector in providing quality healthcare to chronic illnesses are as follows:

• Articulating the concept/de<sup>fi</sup>nition of ubiquitous patient monitoring and assessing and quantifying the corresponding complex requirements/challenges (section 2).

• Developing a concise conceptual framework capturing the (a) key elements and information <sup>fl</sup>ow associated with the process of ubiquitous patient monitoring, and (b) the role of the primary stakeholders — patients/physicians within the framework (section 4).

• Modeling and detailing the fundamental elements constituting the complex process of technology based ubiquitous patient monitoring process, speci<sup>fi</sup>c parameters, decision protocols, information analyzed/generated, and enabling technology corresponding to the processes (section 4).

• Developing a conceptual model of a ubiquitous patient monitoring solution as a proof of concept (section 5).

• Designing a usage scenario to explore the utility of ubiquitous monitoring of patients as a man–machine problem solving system utilizing technology for providing support to the structured processes of patient monitoring while leveraging the tacit expertise of healthcare professionals to provide support to the unstructured processes (section 5).

• Discussing speci<sup>fi</sup>c guidelines for further research, limitations, and challenges of ubiquitous patient monitoring (section 6).

## 4. Proposed framework for ubiquitous patient monitoring

The underlying covenant of technology enabled patient monitoring services is that prompt medical attention will be provided to the patients “just-in-time” as and when required without any constraints based on time and location. Comprehensive, reliable patient monitoring outside the hospitals will not only reduce the healthcare expenses associated with hospitalizations but will also allow precious human resources to be allocated to the healthcare needs of other patients [7,10,33]. An effective patient monitoring solution can be leveraged as a decision support tool where the structured/routine tasks in the patient monitoring process is tackled by technology while the unstructured tasks are tackled by the healthcare professionals. This will not only economize the human resources of the healthcares sector but will also enable improved healthcare of the aging population.

![](/api/attachments/3BPCEWNK/fulltext/images/1f46c13f14831446e5bc3be4262965cfccecbc2592251351b76dcc5cff5ce418.jpg)  
Fig. 4. A framework characterizing the processes of patient monitoring

Ubiquitous patient monitoring system constitutes a man–machine problem solving system, utilizing ubiquitous computing, communication and sensing technologies for providing support to the structured processes of patient monitoring and the tacit/specialized knowledge of a healthcare professional to provide support to the unstructured processes. The structured process in the process of patient monitoring involves: (1) sensing/obtaining speci<sup>fi</sup>c vital signs such as ECG, oxygen saturation level, body temperature, blood pressure, and heart rate, and patient parameters and information such as skin breakdowns, abnormal gait and balance, motor activity and agitation, current location, weight, cigarette smoke, and the amount of moisture in clothes and/or levels of physician speci<sup>fi</sup>ed chemicals as in cancer treatment, (2) analysis of recorded vital signs, and (3) transmitting the data via a communication network (wireless or wired).

The proposed framework consists of the following: (1) a process model depicting the process of patient monitoring, and (2) decision protocols that support each process considering the information generated/analyzed, speci<sup>fi</sup>c parameters that impact each step, and decision criterion for accomplishing structured tasks. The framework (shown in Fig. 4) is then discussed in detail in the context of each process, decision steps, the enabling technologies, the requirements/ challenges, the decision protocols, and the decision criteria/parameters impacting each process.

## 4.1. Sensing

Sensing is the basic process that entails collecting data regarding speci<sup>fi</sup>c conditions including but not limited to the following: vital signs such as ECG, oxygen saturation level, body temperature, blood pressure, and heart rate, and patient parameters and information such as skin breakdowns, abnormal gait and balance, motor activity and agitation, current location, weight, cigarette smoke, the amount of moisture in clothes and/or levels of physician speci<sup>fi</sup>ed chemicals as in cancer treatment, and, routine intake of prescriptions medications as speci<sup>fi</sup>ed. Continuous, comprehensive sensing of patient speci<sup>fi</sup>c conditions is enabled by the devices that can collect multi-parametric vital signs of patients irrespective of time and place, and the sensors/ motes that check speci<sup>fi</sup>c conditions such as sudden increase in weight and missing prescriptions. Wearable biomedical sensors and biomedical clothing and other monitoring devices have made possible the collection and analysis of physiological patient data while the patient is mobile [1]. Inexpensive wireless heart-rate monitors have been available for consumers for several years ex: such as CardioNet [52], which collects ECG data for detection of arrhythmia. The wide spread in<sup>fl</sup>ux of handheld and wearable computers, miniaturization of processors, development of intelligent textiles (Smart Shirt [58]), smart papers, natural communication of the user via intelligent interfaces capable of interpreting speech and gesture are bringing us closer to the vision of ubiquitous monitoring. The technology to support ubiquitous sensing already exists, however the biggest barrier lies in seamless integration and interoperability of the technology such that the patient can lead a normal life with minimal distraction from the technology sensing all of the health related conditions. Fig. 5 shows the decision factors considered in de<sup>fi</sup>ning the process monitoring. The decisions will typically be made under the doctor's recommendation by the patient. The key consideration made in the process of sensing is the frequency and reliability in data collection.

![](/api/attachments/3BPCEWNK/fulltext/images/315aa7506730ea36b00816af28fc106b0c282a7a9e87dd3450891b4eb5062132.jpg)  
Fig. 5. Decision protocol for the process of sensing

## 4.2. Analyzing

Analyzing is the process of evaluating the data collected via sensing in order to detect the presence of any anomalies and take corrective actions as prescribed such as: transmit alert messages to a healthcare professional regarding the detection of anomalies, and call 911 (see Fig. 6). The process of analyzing the collected data before transmitting not only reduces the cognitive overload of the healthcare professionals but also increases the scalability and throughput of the communication channel, however there is a little bit of time lost in analyzing before message transmission. The key considerations made in the process of analyzing the collected data are: to maximize the fault-tolerance of the process so that the anomalies can be detected in an error-free manner, and power conservation of the monitoring analyzing devices. The technology enabling this is ubiquitous computing which seeks to bridge the gap between the virtual and physical world by incorporating computing power (microprocessors) and sensing (sensors) into anything, including not only conventional computers, personal digital assistants (PDAs), mobile phones, printers, but also everyday objects like white goods, toys, plates, cups, glasses, houses, furniture, or even paint (“smart dust”).

![](/api/attachments/3BPCEWNK/fulltext/images/5666988ac1bcac7cb4c6b7212d0b2fe5b5283cc9c8ccf982c0c3931d7908d85e.jpg)  
Fig. 6. Decision protocol for the process of analysis.

![](/api/attachments/3BPCEWNK/fulltext/images/1eb7cd6b90876aff816173c01f673c1b6d1be6423fb43abc4fbd0f0453f73cec.jpg)  
Fig. 7. Decision protocol supporting the process of transmission

## 4.3. Transmitting

Ubiquitous communication technologies supporting reliable transmission of signals between sensors, patient worn computing devices, and healthcare are critical to the success of ubiquitous patient monitoring (see Fig. 7). Ubiquitous communication allows continuous access to data and communication power between people and artifacts with computing and communication capabilities. Mobile and wireless communication technologies and ad-hoc networking are some of the key technologies with respect to ubiquitous communication [27,48,49]. The key consideration made in the process of transmission is to support patient mobility while maximizing reliability of transmission and conserving power of the transmitting device.

The increase in processing power and communication bandwidth along with the corresponding decrease in the cost of processing and communication, with respect to both hardware and software and power consumption have been the fundamental trend in information and communication technologies (ICT) [13,28,48]. This trend is making it both technically and economically possible to integrate processing power and communication capacity to more simple and inexpensive devices and objects. With more than 2 billion mobile devices worldwide, it is evident that the PDAs and mobile devices are slowly becoming an integral part of our lives [48]. The plethora of mobile devices surrounding us with computing and processing capacity offer a mobile wireless platform for running healthcare applications, a user interface and data logging potential for health sensors and monitoring devices and a gateway to connect local devices collecting health related information to global services such as a hospital databases [41,48]. RFID (radio frequency identi<sup>fi</sup>cation technology) allows simple wireless communication with nearby objects to obtain information such as product code, URL or sensor reading. The RFID tags are become inexpensive to be produced in mass scale and do not require battery for operation since they use backscattering in communication.

Transmission of data for patient monitoring has so far been supported by either wired or wireless infrastructure based network. Periodic monitoring in the home environment has been supported via television sets, video monitoring, and two-way broadband connection via cable modem and telephone lines. The wired communication is reliable but doesn't support patient mobility and continuous monitoring. Bluetooth has been utilized for short range wireless communication between the monitoring device and WLANs. Satellite based communication has been used for GPS (Global Positioning System) for outdoor purposes and indoor location tracking is typically supported via RFID (Radio Frequency Identi<sup>fi</sup>cation). WLANs and cellular networks have primarily been used to support continuous patient monitoring along with patient mobility. The transmission channels to transmit the required information include:

![](/api/attachments/3BPCEWNK/fulltext/images/9a6ed8ef127fcf3f22f7f4c748744dc61fdbc7f814fcc3ce260aac57662bf1dd.jpg)  
Fig. 8. Multi-hop signal transmission in ad hoc wireless network.

\- Short range transmission between the sensing and analyzing devices via Bluetooth.

\- Infrastructure oriented wireless network such as WLANs, Cellular PCS/GSM, and Satellite Based Networks. The spotty coverage of existing infrastructure oriented wireless networks (such as cellular networks and wireless LANs) due to time and location dependent channel quality and signal attenuation results in dead spots and can consequently lead to unpredictable quality and reliability of monitoring solutions [48]. The exclusive dependency on infrastructure-oriented wireless networks for patient monitoring has additional challenges including: (a) short range and limited power capabilities of most patient devices, (b) lack of interoperability among multiple wireless LANs, (c) considerable interference in ISM bands from multiple sources, (d) varying capacity of infrastructure-oriented wireless networks, and, (e) lack of application-speci<sup>fi</sup>c priority for transmission of emergency signals. These restrictions and requirements combined with a lack of comprehensive coverage of infrastructure-oriented wireless networks negatively affects the quality of patient monitoring, greatly limits the mobility of patients, and can potentially lead to fatal consequences.

\- Ad Hoc Wireless Networks formed among patient monitoring devices can complement the coverage of infrastructure oriented networks in the areas with limited/no network coverage from infrastructure-oriented networks thereby leading to improved networking support for patient monitoring solutions and consequently enhancing the quality and dependability of patient monitoring solutions. There are numerous opportunities and challenges associated with leveraging mobile ad hoc network to support dependable patient monitoring solutions [47]. A mobile ad hoc network consists of a collection of geographically distributed wireless devices or nodes that can dynamically form a network without a pre-de<sup>fi</sup>ned infrastructure and communicate with one another over a wireless medium [20,36,37] (Fig. 8).

The advantages associated with ad hoc networks are ease and speed of deployment since it can function dynamically without any infrastructure, robustness, <sup>fl</sup>exibility in terms of place of deployment and number of users and lastly the inherent support for mobility which forms the cornerstone of deploying such networks in healthcare since the patients and doctors are both mobile [37,40]. The challenges are related to the variations in the mobility pattern and mobility characteristics of the nodes; asymmetric capabilities of the nodes with respect to transmission range, battery power, processing capacity and mobility; diversity in traf<sup>fi</sup>c characteristics such as bit rate; timeliness constraints, and reliability requirements. The route from the source to the destination typically involves multiple hops and the route is susceptible to changes due to mobility in nodes. Recent advent in personal digital assistants and plethora of mobile patient monitoring devices that are used in transmission of vital signs over short range, have brought to the fore ground the possibility of forming ad hoc networks among patients' devices which can monitor and transmit vital signs.

## 5. Conceptual model — a proof of concept

Although the technology to support ubiquitous patient monitoring exists, the key question is how to create an integrated architecture to achieve the vision. A critical factor leading to increased healthcare expenses is hospitalization for long term care and monitoring. Hence shifting the site of continuous monitoring and care from the hospital to the patient's home can potentially reduce healthcare cost [2,10]. The next section presents a proof-of-concept for ubiquitous patient monitoring as a detailed conceptual model. The model provides details with respect to the various components, the functioning, and the decision criteria considered by each component.

![](/api/attachments/3BPCEWNK/fulltext/images/75279ec4c21f59ca25e72509260f66855dbc28a63aa01b7e9017a8ccee3bfaa4.jpg)  
Fig. 9. Conceptual model of a proposed patient monitoring system.

Table 2  
Monitors and Sensors in the Proposed Conceptual Model

<table><tr><td>Monitors and sensors</td><td>Objective/functionality</td></tr><tr><td>ECG monitor</td><td>Measures ECG of patients. The portable ECG is carried by the patient 24 h a day. The ECG device has two electrodes that are attached to the patient and provide a single channel ECG Signal (Nussbaum et al., 2002)</td></tr><tr><td>Blood sugar monitor</td><td>Monitors blood sugar level at predetermined times as deemed suitable by a doctor.</td></tr><tr><td>Asthma monitor</td><td>Monitors peak air flow level at predetermined times as deemed suitable by a doctor.</td></tr><tr><td>Medication sensor</td><td>Located on the prescriptions (Rx) bottles. Monitors the intake of Rx as advised. If violation detected then relevant signal is sent to the Medication Agent in the patient&#x27;s PDA.</td></tr><tr><td>Weight sensor</td><td>Located on the weighing machine. Senses any critical change in the patient&#x27;s weight based on pre-stored patient&#x27;s weight. If a critical change in weight observed then signal is sent to the Weight Agent in the patient&#x27;s PDA</td></tr><tr><td>Sleep sensor</td><td>Located on the bed. Senses sleep patterns. If sleeplessness or too much sleep is sensed over a 24 h period, then the signal is sent to the sleep agent</td></tr></table>

## 5.1. Conceptual model

The proposed framework is utilized in developing the conceptual model. Fig. 9 represents the conceptual model of a ubiquitous patient monitoring environment equipped with sensors and biometric devices. Each process is broken down into decision segments as outlined in the framework. The development of the conceptual model, the underlying processes, the corresponding parameters, and the decision criteria are discussed in the next few paragraphs.

## 5.1.1. What population segment is served by the proposed model?

The conceptual model is designed to meet the healthcare needs of the Medicare's high-risk patients (approximately 8 million) with <sup>fi</sup>ve or more chronic conditions accounting for over two-thirds of Medicare's annual spending [3,6]. A large percentage of chronic diseases deteriorate to the point where a crisis is reached resulting in long term hospitalization and monitoring of patients at huge costs to the healthcare sector. The proposed study focuses on the following chronic illnesses in the US (and their associated in-patient expenses) include: heart failure (\$15.2 billion), diabetes (\$3.8 billion), hyperten-

## Table 3

Intelligent agents performing speci<sup>fi</sup>c tasks

<table><tr><td>Intelligent agents and corresponding tasks</td></tr><tr><td>Bluetooth agentResides in the PDA, retrieves readings from the wireless ECG monitor, blood sugar monitor, asthma monitor, medication sensor, weight sensor, and sleep sensor.</td></tr><tr><td>Location agentLocation agent uses GPS and/or other location tracking systems (WLANs, RFID) for location of patients.</td></tr><tr><td>Patient data agentStores information about the patient such as: ID, name, address, date of birth (DOB), medical contacts information, scheduling information, blood group, and prescription drugs.</td></tr><tr><td>Medical info. agentUpdates the patient&#x27;s EMR (electronic medical record) with the following information received from the alarm agent: the anomaly detected, the date/time of the event, the ID of the physician receiving/handling the alarm.</td></tr><tr><td>Alarm agentReceives alarm messages sent by the PDA of the patients. Informs a physician of the event who takes the requisite action based on the analysis sent in the message and past patient history accessed via the EMR. Sends back acknowledgement to the respective agent confirming that the alert has been received and is being managed.</td></tr></table>

sion (\$3.2 billion) accounting for a total of \$22.2 billion in total Medicare expenses [3,6].

## 5.1.2. What is monitored and how?

The proposed model monitors a patient's vital signs and speci<sup>fi</sup>c health and compliance conditions. The speci<sup>fi</sup>c vital signs that we propose to monitor and the corresponding means of monitoring are presented in Table 2. Additionally, sensors with computing and communication capabilities will be deployed at speci<sup>fi</sup>c locations in patient's home to monitor a speci<sup>fi</sup>c compliance task (refer to Table 2). The readings from the monitors and sensors are communicated with the intelligent agents located in the patient's PDA. The frequency of monitoring the vital signs and speci<sup>fi</sup>c conditions can be adjusted by a healthcare professional as deemed suitable.

## 5.1.3. What is analyzed and how is the analysis done?

We propose a PDA (Personal Digital Assistant) housed with intelligent agents to perform the task of analyzing the monitored conditions. The use of PDA as a component of the proposed system stems from its ease of use, ubiquitous access to data, and the inherent support for mobility. The use of intelligent agents with clear goals and relevant knowledge, as proposed in the current research, has the capability of assisting healthcare professionals in continuous patient monitoring in the form of ongoing analysis and diagnosis of large amount of complex data and alerting the health center in case of an anomaly via multi agent communication [41]. This has the bene<sup>fi</sup>t of not only reducing the cognitive overload of health care professionals but also promoting timely intervention of health care structure as and when required. The intelligent agents use an ontology that categorizes different alerts, which correspond to violations of boundary conditions as speci<sup>fi</sup>ed by the threshold ECG recordings. The ontology is represented using DAML+OIL [53], which is based on Description Logics [54]. These agents carry out a large chunk of analysis of the ECG in the PDA and send alerts only if an anomaly is detected thereby reducing traf<sup>fi</sup>c on the wireless networks, making the system more cost-ef<sup>fi</sup>cient and involving the health care structure without delay but only when needed. Some of the major telecommunication companies such as Motorola, Fujitsu and BT are taking great initiatives in providing accessibility to agent based services via mobile devices such as mobile phones, PDA or portable PCs [41]. Table 3 presents functionalities of the intelligent agents which are responsible for carrying out certain pre-de<sup>fi</sup>ned tasks. Table 4 presents the protocols and functionalities of intelligent agents tasked with the job of analysis.

5.1.4. Configuration of the patient's monitoring device — how is the analysis done?

Prior to the <sup>fi</sup>rst use, the Intelligent Agents tasked with analyzing a speci<sup>fi</sup>c patient condition is con<sup>fi</sup>gured by a physician based on the current/past conditions of the patient, thus providing individual patient-centered care. The intelligent agents analyze the data collected from the monitors and the sensors, look for violation of pre-speci<sup>fi</sup>ed thresholds, and transmit alerts to the healthcare centers when needed. The physician speci<sup>fi</sup>es the thresholds, which a particular Agent will refer to before triggering an alarm. The frequency of monitoring each vital sign, under normal conditions (example record ECG every 10 s) as well as abnormal conditions, i.e., after detection of an anomalous reading, (example Record ECG every 1 s for the next 1 min) is also con<sup>fi</sup>gured. The ontology that categorizes the different alerts is built in each PDA by a specialist that describes the alerts that must be checked for every patient. Table 4 gives a detail description and functionality of the various intelligent agents that are tasked with analyzing the monitored parameters, and the protocols.

Table 4 (continued)  
```txt
Intelligent agents — corresponding protocols and functionality

Intelligent agents and corresponding decision protocols

ECG Agent
The ECG Agent receives ECG data via Bluetooth, checks the ECG data for any anomalous conditions. If an anomalous condition is detected then it sends a request for intensive monitoring to the ECG monitor. The readings received during intensive monitoring are analyzed and if all of them meet the violation criteria as defined by the alert conditions defined in the ontology then an alarm is triggered. The alarm triggered is sent to the Alarm Agent at the E-Health Center.

IF ECG[E] <= ECG - 10 OR IF ECG[E] >= ECG + 10
START INTENSIVE MONITORING (record ECG readings every 1 s for the next 1 min)
Violation = 1; Count = 0
WHILE (Violation AND Count < 60)
{ IF ECG[E] <= ECG - 10 OR ECG[E] >= ECG + 10
Count++; ELSE Violation = 0; }
IF (Violation)
SEND ALARM MESSAGE TO THE ALARM AGENT AT THE E-Health Center
ELSE ECG AGENT RETURNS TO NORMAL STATE, SENDS MESG. TO THE ECG MONITOR TO CONTINUE NORMAL ECG MONITORING

Blood Sugar Agent
The Blood Sugar Agent receives blood sugar levels (BSL) via Bluetooth, checks the received levels for any violation. If a violation is detected then two other consecutive readings are requested. The other readings are analyzed and if all of them meet the violation criteria as defined by the alert conditions defined in the ontology then an alarm is triggered.

IF BSL(b) <= BSL - 10 OR IF BSL(b) >= BSL + 10
START INTENSIVE MONITORING (report two consecutive BSL readings)
Violation = 1; Count = 0
WHILE (Violation AND Count < 2)
{ IF BSL(b) <= BSL - 10 OR IF BSL(b) >= BSL + 10
Count++;
ELSE Violation = 0; }
IF (Violation)
SEND ALARM MESSAGE TO THE ALARM AGENT AT THE E-Health Center
ELSE Blood Sugar Agent RETURNS TO NORMAL STATE, SENDS MESG. TO THE Blood Sugar MONITOR TO CONTINUE NORMAL MONITORING

Asthma Agent
The Asthma Agent receives peak flow levels (PFL) via Bluetooth, checks the received levels for any violation. If a violation is detected then two other consecutive readings are requested. The other readings are analyzed and if all of them meet the violation criteria as defined by the alert conditions defined in the ontology then an alarm is triggered. The alarm triggered is sent to the Alarm Agent at the E-Health Center.

IF PFL(p) <= PFL - 10 OR IF PFL(p) >= PFL + 10
START INTENSIVE MONITORING (report two consecutive PFL readings)
Violation = 1; Count = 0
WHILE (Violation AND Count < 2)
{ IF PFL(p) <= PFL - 10 OR IF PFL(p) >= PFL + 10
Count++;
ELSE Violation = 0; }
IF (Violation)
SEND ALARM MESSAGE TO THE ALRM AGENT AT THE E-Health Center
ELSE Blood Sugar Agent RETURNS TO NORMAL STATE, SENDS MESG. TO THE Asthma MONITOR TO CONTINUE NORMAL MONITORING

Medication Agent
Reads the signal from the Medication Sensor and sends reminders to patients to take the medication via audio and text based messages. If medication is skipped beyond a critical level (as predefined by a healthcare professional such as: 2 dosages missed) an alert is routed to the healthcare provider.

MED Missed = 1, COUNT = 0
WHILE (MED Missed AND COUNT < 4) {
Send Reminders via Audio and Text to take MED
Check Med(m) After 30 min;
If Med(m) is Missed
MED Missed = 1;
ELSE MED Missed = 0
COUNT++; }
IF (MED Missed)
SEND ALARM MESSAGE TO THE ALRM AGENT AT THE E-Health Center
ELSE RESUME NORMALLY.
```

```txt
Intelligent agents and corresponding decision protocols
Weight Agent
Reads the signal from the Weight Sensor and analyzes it. If the change in weight is ≤10 units over a 24 h period sends reminders to patients regarding the weight and advises on healthy eating habits. If the change in weight is >15 units over a 24 h period a routine alert is routed to the healthcare provider informing of the event.
IF WT CHANGE <= 10 UNITS
Advice on Healthy Habits and Change in WT via Audio and Text Message
ELSE IF WT CHANGE >= 15 UNITS
SEND ALERT TO ALARM AGENT at the E-Health Center.
Sleep Agent
Reads the signal from the Sleep Sensor and sends messages to patients regarding the pattern in audio and visual mode. An alert is also routed to the healthcare provider informing them of the event
IF SLEEPLESSNESS/TOO MUCH SLEEP
Advice via Audio and Text Message
IF SLEEPLESSNESS/TOO MUCH SLEEP FOR MORE THAN 2 CONSECUTIVE DAYS
SEND ALERT TO ALARM AGENT at the E-Health Center.
```

## 5.1.5. What Information is transmitted and how is the signal transmitted?

The sensors monitoring compliance and the devices monitoring speci<sup>fi</sup>c vital signs transmit the data to the patient's PDA at a prede<sup>fi</sup>ned time interval. For signal transmission we propose a hybrid network in order to increase the reliability of transmission and enhance the network coverage. The transmission of data from the sensors and the monitoring devices to the patient's PDA is done via short range communication medium such as Bluetooth. The transmission of signals between the patients and the healthcare professionals for the most part is to be supported via infrastructure based wireless networks such as WLAN, Cellular/PCS/GSM, and satellite based systems. However, the coverage of infrastructure based networks inherently suffers from temporary/permanent dead spots thereby negatively impacting the reliability of transmission [48]. Thus we propose to use mobile ad-hoc network to complement the coverage of existing infrastructure based networks in areas with limited or no coverage. Utilizing a hybrid network comprising of mobile ad hoc network and other infrastructure based wireless network builds a layer of fault tolerance with respect to patient–doctor communication and thus increases the reliability of transmission. In case an alarm message needs to be transmitted and the patient is outside the coverage of the infrastructure based network then an ad-hoc network formed between the patient's PDA and other devices within the range of the patient's PDA can transmit the alarm via multiple hops till it reaches a healthcare professional or is picked up by an infrastructure based network for further transmission to a healthcare professional (Fig. 10).

## 5.2. Usage scenario

A descriptive usage scenario is presented to demonstrate the utility of the proposed conceptual model. Patient X is being continuously monitored for detection of anomalous conditions and disease management. One morning the patient woke up at 6 am. The sleep sensor did not observe any irregularity in patient's sleep patterns. The patient goes to the restroom and takes his weight. The weight sensor observes no critical change in patient's weight. The patient is getting ready to go to out and has forgotten to take his morning medication. The medication sensor senses that the medication hasn't been taken by 8 a.m. and sends a signal to the medication agent which reminds the patient to take the medication. The patient takes the medication and goes to a nearby shopping mall for lunch. During the monitoring the ECG agent detects an irregularity and requests intensive monitoring for the next 30 s. All ECG readings in the intensive monitoring session were in the critical range. Hence an emergency alert is transmitted by the transmission agent. The patient is in a dead spot where there is no coverage of the wireless network. Hence an ad hoc network is formed and signal is transmitted from the patient's device (at the maximum power level) to the other co-operating devices in the range of transmission. After two hops, the third hop is a cellular base station which picks up the signal and routes it to the healthcare provider. The healthcare professional reads the message, takes prompt medical action to resuscitate the patient. In the absence of ubiquitous patient monitoring, the patient could have lost his life and/or ended up in the hospital for an extended period of time due to complications arising from missed medications, or anomalies going unnoticed. The key contribution of ubiquitous patient monitoring is improved healthcare delivery by timely and reliable detection of anomalies and enhancing the ef<sup>fi</sup>ciency of the physicians by assisting them in providing pertinent medical attention as and when needed.

![](/api/attachments/3BPCEWNK/fulltext/images/65cab66a9187a30638da32ab7e1df01e92cf6a875d4ec81e534f2fca0a11fa3c.jpg)  
Fig. 10. Transmission from patient to healthcare professional via hybrid network.

## 6. Conclusion and future research

Technology based ubiquitous patient monitoring has been proposed for promoting wellness, prevention, disease management, compliance, and reduced incidences of hospitalizations and corresponding expenses [10,18,33]. However, the focus so far has been on the development of artifacts with little or no attention given to re<sup>fi</sup>ning the process of patient monitoring and de<sup>fi</sup>ning clear guidelines that can be universally applied to developing effective, ef<sup>fi</sup>cient patient monitoring solutions. In the current research we address this gap and make the following contributions to the existing body of research in patient monitoring. First we develop a framework that characterizes the basic processes that can be universally applied for ubiquitous patient monitoring. Second, we describe in detail the decision protocols, key parameters, and enabling technologies for each process. Third, we articulate the requirements and challenges of ubiquitous patient monitoring and evaluate the myriad of technologies enabling the development of ubiquitous patient monitoring. The proposed framework and decision protocols are grounded in the requirements of patient monitoring. The requirements, challenges, and evaluation of enabling technologies are based on an in depth review of pertinent literature in the area. Lastly, we also propose a conceptual model of a ubiquitous patient monitoring system based on the proposed framework and clear concise guidelines. The contribution of the proposed innovative strategy is effective healthcare delivery, increased compliance with medical advice, and improved quality of life of patients outside of the hospital.

Although, ubiquitous patient monitoring is still in its infancy the possibilities of leveraging it as a decision support tool are vast and the realization process has merely begun. Future work will help to <sup>fi</sup>ne tune the concept and help to bring forth the realization of a ubiquitous healthcare environment. It is our hope that some of the current issues will open the door for future research. Future work may address the issue of issue of acceptability of the system along with the level of trust of doctors and patients in the ubiquitous healthcare environment. A research based on testable hypotheses can potentially provide some substantive <sup>fi</sup>nding with respect to adoption of ubiquitous healthcare. In the light of HIPAA, security and reliability of transactions made over a wireless network are important concerns. Future research addressing the issue of increasing security and reliability of mobile communication is imperative to the success of ubiquitous healthcare. There is also research needed to address the mechanism exploring how patient monitoring systems can be utilized as a decision support tool for healthcare professionals.

## Acknowledgment

The work was supported, in part, by a National Science Foundation (NSF) research grant (SCI#0439737).

## References

[1] P. Bonato, Wearable sensors/systems and their impact on biomedical engineering, IEEE Engineering Medicine and Biology Magazine 22 (3) (2003).

[2] O.J. Bott, E. Ammenwerth, B. Brigl, P. Knaup, E. Lang, R. Pilgram, B. Pfeifer, F. Ruderich, A.C. Wolff, R. Haux, C. Kulikowski, The challenges of ubiquitous computing in health care: technology, concepts and solutions, Methods of Information in Medicine 44 (3) (2005).

[3] C. Boult, R.L. Kane, J.T. Pacala, E.H. Wagner, Innovative healthcare for chronically ill older persons: results of a national survey, The American Journal of Managed Care 5 (9) (1999).

[4] S. Brahnam, C.F. Chuang, R.S. Sexton, F.Y. Shih, Machine assessment of neonatal facial expressions of acute pain Decision Support Systems 43 (4) (2007).

[5] M. Chiasson, E. Davidson, B. Kaplan, R. Kukafka, G. Kuperman, Strangers in a strange land: can IS meet the challenges and opportunities of research in healthcare? Proceedings of the Tenth Americas Conference in Information Systems, 2004

[6] Chronic Care Improvement, ITAA E-Health White Paper: A Product of the E-health Committee, 2004, p. 5.

[7] R.C. Coile, B.E. Trusko, Healthcare 2020: technology in the new millennium, Health Management Technology 20 (11) (1999).

[8] J.M. Corchadoa, J. Bajo, Y. Paza, D.I. Tapiaa, Intelligent environment for monitoring Alzheimer patients, agent technology for health care, Decision Support Systems 44 (2) (2008).

[9] M.J. Covington, W. Long, S. Srinivasan, A.K. Dev, M. Ahamad, G.D. Abowd, Securing context-aware applications using environment roles, In Symposium on Access Control Model and Technology, 2001.

[10] E. Dishman, Inventing wellness systems for aging in place, IEEE Computer 37 (5) (2004)

[11] G.B. Doherty, R.N. Ross, P.E. Ross, The effectiveness of an interactive electronic lung function monitoring system in the total management of refractory asthma, Disease Management and Health Outcomes 3 (2) (1998).

[12] I.A. Gieras, The proliferation of patient-worn wireless telemetry technologies within the U.S. healthcare environment, Proceedings of 4th International IEEE EMBS Special Topic Conference on Information Technology Applications in Biomedicine, 2003.

[13] S. Goldberg, N. Wickramasinghe, 21st century healthcare — the wireless panacea, Proceedings of the 36th Hawaii International Conference on Systems Sciences, 2003.

[14] F. Gouaux, L. Simon-Chautemps, S. Adami, M. Arzi, D. Assanelli, J. Fayn, M.C. Forlini, C. Malossi, A. Martinez, J. Placide, G.L. Ziliani, P. Rubel, Smart devices for the earl detection and interpretation of cardiological syndromes, In Proceedings of the 4th International IEEE EMBS Conference on Information Technology Applications in Biomedicine UK, 2003.

[15] P.J.H. Hu, C.P. Wei, T.H. Cheng, J.X. Chen, Predicting adequacy of vancomycin regimens: a learning-based classi<sup>fi</sup>cation approach to improving clinical decision making, Decision Support Systems 43 (4) (2007).

[16] K. Hung, Y. Zhang, Implementation of a WAP-based telemedicine system for patient monitoring, IEEE transactions on Information Technology in Biomedicine 7 (2) (2003)

[17] D.J. Hunter, Disease management: has it a future? 320 (7234) (2000).

[18] IOM. To err is human: building a safer health system, US Institute of Medicine Report. http://www.nap.edu/books/0309068371/html/.

[19] R.S.H. Istepanian, A.A. Petrosian, Optimal zonal wavelet-based ECG data compression for a mobile telecardiology system, IEEE Transactions on Information Technology in Biomedicine 4 (3) (2000)

[20] S. Jain, Energyaware communication in ad-hoc networks, Technical Report University of Washington Seattle–CSE, March 2003.

[21] E. Jovanov, A. O'Donnel, A. Morgan, B. Priddy, R. Hormigo, Prolonged telemetric monitoring of heart rate variability using wireless intelligent sensors and a mobile gateway, In Proc. Second Joint IEEE EMBS/BMES Conference, 2002.

[22] E. Jovanov, A. O'Donnell Lords, D. Raskovic, P.G. Cox, R. Adhami, F. Andrasik, Stress monitoring using a distributed wireless intelligent sensor system, IEEE Engineering in Medicine and Biology Magazine 22 (3) (2003).

[23] E. Kafeza, D.K.W. Chiu, S.C. Cheung, M. Kafeza, Alerts in mobile healthcare applications: requirements and pilot study, IEEE Transactions on Information Technologies in Biomedicine 8 (2) (2004).

[24] A. Kara, Protecting privacy in remote-patient monitoring, IEEE Computer 34 (5) (2001).

[25] S.E. Kern, D. Jaron, Healthcare technology, economics and policy: an evolving balance, IEEE Engineering in Medicine and Biology Magazine 22 (1) (2003)

[26] S. Khoor, K. Nieberl, K. Fugedi, E. Kail, Telemedicine ECG-telemetry with Bluetooth technology, Proceedings of Computers in Cardiology, 2001.

[27] I. Korhonen, J.E. Bardram, Guest editorial introduction to the special section on pervasive healthcare, IEEE Transactions on Information Technology in Biomedicine 8 (3) (2004).

[28] I. Korhonen, J. Parkka, M.V. Gils, Health monitoring in the home of the future: infrastructure and usage models for wearable sensors, IEEE Engineering Medicine and Biology Magazine 22 (3) (2003).

[29] J.C. Kyu, H.H. Asada, Wireless, battery-less stethoscope for wearable health monitoring, Proc. the IEEE 28th Annual Northeast Bioengineering Conference, 2002.

[30] L. Lin, P. J-H Hu, O.R.L. Sheng, A decision support system for lower back pain diagnosis: uncertainty management and clinical evaluations, Decision Support Systems 42 (2) (2006).

[31] K. Liszka, M. Mackin, M. Lichter, D. York, D. Pillai, D. Rosenbaum, Keeping a beat on the heart, IEEE Pervasive Computing 3 (4) (2004).

[32] A. Lymberis, A. Smart, Wearables for remote health monitoring, from prevention to rehabilitation: current R&D future challenges Proc. 4th International JEEE EMBS Conference on Information Technology Applications in Biomedicine, 2003.

[33] M.K. McGee, E-Health on the Horizon, 989, May 2004

[34] G.G. Mendoza, B.Q. Tran, In-home wireless monitoring of physiological data for heart failure patients, In Proc. of the Second Joint IEEE EMBS/BMES 24th Annual Conference and the Annual Fall Meeting of the Biomedical Engineering Society Conference 2002

[35] D. Nussbaum, X. Wu, An architecture of scalable wireless monitoring system, In Proc. of the 25th Annual international Conference of the IEEE EMBS Cancun Mexico, 2002.

[36] L. Qin, T. Kunz, Survey on mobile ad hoc network routing protocols and cross-layer design, Carleton University Systems and Computer Engineering, Technical Report SCE-04-14, August 2004

[37] R. Rajaraman, Topology control and routing in ad hoc networks: a survey, ACM SIGACT News, 33(2) (2002).

[38] A. Sarela, I. Korhonen, L. Lötjönen, M. Sola, M. Myllymäki, IST Vivago — an intelligent social and remote wellness monitoring system for the elderly, In Proceedings of the 4th Annual IEEE EMBS Special Topics Conf. on Information Technology Application in Biomedicine, 2003.

[39] M. Satyanaryanan, Pervasive computing: vision and challenges, IEEE Personal Communications 8 (4) (2001).

[40] S. Sesay, Z. Yang, J. He, A survey on mobile ad hoc wireless networks, Information Technology Journal 3 (2) (2004).

[41] S. Sneha, U. Varshney, Wireless ECG monitoring system for pervasive healthcare, In Proceedings of the Eleventh Americas Conference on Information Systems, AMCIS, Omaha NE, 2005.

[42] S. Sneha, A. Dulipovici, Strategies for working with digital medical images, In Proceedings of Hawaii International Conference on Systems Sciences, 2006.

[43] S. Sneha, Patient Monitoring via Mobile Ad Hoc Networks: Maximizing Reliability while Minimizing Power Usage and Delays, Doctoral Dissertation, Georgia State University, May 2008.

[44] V. Stanford, Using pervasive computing to deliver elder care, IEEE Pervasive Computing Magazine 1 (1) (2002).

[45] T. Suzuki, M. Doi, LifeMinder: an evidence-based wearable healthcare assistant, Proc, ACM CHL Conference. 2001

[46] A. Tablado, A. Illarramendi, J. Bermudez, A. Goni, Intelligent monitoring of elderly people, Proc. 4th Annual IEEE Conf. On Information Technology Applications in Biomedicine UK, 2003.

[47] N.H. Vaidya, Tutorial on Mobile Ad Hoc Networks: Routing, MAC and Transport Issues, INFOCOM, 2006.

[48] U. Varshney, Pervasive healthcare: applications, challenges and wireless solutions, Communications of the Association of Information Systems, 2005.

[49] U. Varshney, A framework for supporting emergency messages in wireless patient monitoring, Decision Support Systems, April 2008.

[50] Website: Aware Home Project: http://www.awarehome.gatech.edu/projects/index.html. [51] Website: Biotronik, httn://www biotronik com/ [51] Website: Biotronik, http://www.biotronik.com/.

[52] Website: Cardionet, http://www.cardionet.com/

[53] Website DAML: http://www.daml.org (2005).

[54] Website Description Logic Homepage: http://dl.kr.org (2003).

[55] Website: Gator Tech Smart House: http://www.icta.u<sup>fl</sup>.edu/gt.htm

[56] Website: LifeSync — www.wirelessecg.com, 2005.

[57] Website: Patient Monitoring by Welch Allyn (http://www.monitoring.welchallyn. com/products/wireless/).

[58] Website for Smart Shirt: http://www.smartshirt.gatech.edu.

[59] Website: TV-based Monitoring by Philips (http://www.medical.philips.com/main/ news/content/file 630.html

[60] Website: US Administration on Aging Report on Demographic Changes, http:// www.aoa.dhhs.gov/aoa/stats/aging21/demography.html.

[61] Website: US Patient Monitoring Industry Overlook. http://www.frost.com/prod/ servlet/report-homepage.pag?repid=A369-01-00-00-00.

[62] M. Weiser, The Computer for the Twenty-First Century, Scienti<sup>fi</sup>c American, 265 (3) (1991).

[63] World Health Organization, Death by Cause, Sex and Mortality Stratum in WHO Regions. 1999.

![](/api/attachments/3BPCEWNK/fulltext/images/802589e836133656668861ccc27becdd9c22ee68b313f77ed38f169083356bce.jpg)

Sweta Sneha is an Assistant Professor at Kennesaw State University in the Department of Computer Science and Information Systems. She has a Bachelor of Science in Computer Science from University of Maryland, College Park and a PhD in Computer Information Systems from Georgia State University. Sweta's research interests center around a wide array of technical and behavioral challenges related to the emerging <sup>fi</sup>eld of “E-Health,” which lies at the intersection of telecommunication, information technology, healthcar sector, and business. Her goal is to research, analyze, and recommend technical and/or behavioral solutions to meet the challenges associated with the spiraling healthcare expenses, the aging population, and the need to integrate

use technology in the practice and delivery of healthcare, Within the e-health umbrella she has conducted and published research in: (a) wireless network and enhanced decision support systems for innovative e-health services seeking to economize human/<sup>fi</sup>nancial healthcare resources, (b) adoption, usage, and integration of emerging e-health services in the practice and delivery of healthcare by the healthcare professionals such as: Electronic Medical Records (EMR) and the corresponding performance improvement in the quality of patient care, and (c) organizational impact and process change associated with the integration and usage of e-health services by the healthcare sector. She has published several research papers in premier IS conferences and journals including AMCIS, HICSS IEEE Broadmed and IEEE Communications. She has also worked as an Information Technology (IT) Consultant within the Management Consulting Practice of Pricewater houseCoopers, one of the leading IT and management consulting <sup>fi</sup>rms in the world.

![](/api/attachments/3BPCEWNK/fulltext/images/3af8e51b47b31d69cab390d35d6ffe2ab275d858e7d1ab44c70a17c19ea83395.jpg)

Upkar Varshney is on the faculty of CIS at Georgia State University. His current interests include wireless networks, pervasive healthcare, ubiquitous computing and mobile commerce. He is the co-founder (with Prof. Imrich Chlamtac) of International Pervasive Health Conference and also cochaired the conference in 2006. Upkar is also the program cochair for Americas Conference on Information Systems (AMCIS-2009) in San Francisco.

He has authored over 120 papers including about 60 in journals, including 30 in IEEE and ACM publications. He is the author of several heavily downloaded and cited papers in wireless networks, pervasive healthcare, and mobile com

merce. According to scholar.google, the total number of journal and conference citations for his papers exceeds 1700.

Upkar has presented several very well received tutorials and workshops (and even a few keynotes) at wireless, computing, and information systems conferences. He has also received grants from several funding agencies including the National Science Foundation His teaching awards include Myron T. Greene Outstanding Teaching Award (2004), RCB College Distinguished Teaching Award (2002), and, Myron T. Greene Outstanding Teaching Award (2000).

He is serving or has served as an editor/guest editor for IEEE Transactions on IT in Biomedicine, ACM/Kluwer Mobile Networks (MONET), IEEE Computer, Decision Support Systems (DSS), Communications of the AIS (CAIS), Int. J. on Network Management (IJNM), Int. Journal on Mobile Communications (IJMC), Int. Journal of Wireless and Mobile Computing (IJWMC), and Handbook of Research on Mobile Business.
