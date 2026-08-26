---
otero_id: 20547
otero_key: "WCY935QN"
title: "My Real Avatar has a Doctor Appointment in the Wepital: A System for Persistent, Efficient, and Ubiquitous Medical Care"
authors: "Fatemeh Mariam Zahedi; Huimin Zhao; Patrick Sanvanson; Nitin Walia; Hemant Jain; Reza Shaker"
year: "2022"
journal: "Information & Management"
doi: "10.1016/j.im.2022.103706"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# My Real Avatar has a Doctor Appointment in the Wepital: A System for Persistent, Efficient, and Ubiquitous Medical Care

Fatemeh Mariam Zahedi <sup>a,\*</sup>, Huimin Zhao <sup>b</sup>, Patrick Sanvanson <sup>c</sup>, Nitin Walia <sup>d</sup>, Hemant Jain <sup>e</sup>, Reza Shaker

<sup>a</sup> UWM Distinguished Professor Emerita, ITM Professor Emerita, Sheldon B. Lubar College of Business, University of Wisconsin-Milwaukee

<sup>b</sup> ITM Professor, Sheldon B. Lubar College of Business, University of Wisconsin-Milwaukee

<sup>c</sup> Associate Professor of Medicine, Associate Director, Neurogastroenterology, Motility, and Airway Protection Research Laboratory, Division of Gastroenterology & Hepatology, Medical College of Wisconsin

<sup>d</sup> Clinical Professor, W. P. Carey School of Business, Arizona State University

<sup>e</sup> W. Max Finley Chair for Excellence in Business, Free Enterprise and Capitalism, University of Tennessee Chattanooga

<sup>f</sup> Joseph E. Geenen Professor, Chief, Division of Gastroenterology and Hepatology, Associate Provost for Clinical and Translational Research, Sr. Associate Dean and Director, Clinical and Translational Science Institute of SE Wisconsin, Medical College of Wisconsin

## A R T I C L E I N F O

Keywords: Wepital Real avatar Mypital Theory of affordances Docpital Medical internet Persistence of care Telepresence Trust Time convenience Flexibility about medical care

## A B S T R A C T

COVID-19 created a great deal of personal, social, and economic anxiety in the USA and across the globe and exposed the inadequacy of traditional medical systems in handling large-scale emergencies. While telemedicine and virtual visits have become popular as a result, they end once a visit is over, hence lacking data persistence and continuity in caring for patients. Using the design science research approach with support from the theory of affordances, this paper proposes the design of a medical system (called wepital) in which patients receive care through their real avatars, enabling hospitals and other medical centers to provide immediate care that can continue for as long as a patient needs it. Real avatars are digital representations of patients that embody their real-time vital signs and health information. We have created a functional prototype to demonstrate how the proposed design can work. To assess the usability of the design, we have used the prototype in an experiment to provide medical advice to patient volunteers. Based on a theory-based conceptual model, we collected survey data after the experiment to identify factors contributing to the success of such a system, as measured by patient satisfaction. We report the factors that significantly contribute to the patients’ satisfaction. As part of the application and policy implications of our work, we propose a nationwide system that could supplement and expand the capacity of medical systems at the national or even global level.

## 1. Introduction

Recent outbreaks of SARS, Ebola, and COVID-19 indicate the high likelihood of more epidemics in the future. The question is whether we can build an infrastructure to provide immediate, ubiquitous, and persistent care, with flexible capacity manageable both at normal times and in emergencies. Such a structure by necessity would rely on avail able technologies to scale up medical capacities and improve care processes.

The year 2020 witnessed a quick rise in telemedicine (e.g., [8,13,55,

96]). Insurance companies accepted and encouraged virtual visits, and patients reacted positively to receiving care at home. Even hospital rounds and communications with patients within hospitals became virtual [103]. Yet, telemedicine remains disconnected from patients health records and vital signs. Physicians usually access patients’ re cords on one device and communicate with patients on another device without access to patients’ vital signs in real time. Moreover, such care ends as soon as the session is over, without persistence.<sup>1</sup> Patients who need continuous care (such as older adults with chronic health issues) are left to deal with their medical needs on their own. Patients have to seek more information about their medical issues on their own and have no chance to benefit from and share information with other patients with similar issues or receive group information and updates. Can technology provide a solution?

The use of technology in medicine has two sides. One side involves technologies used by healthcare providers. Research on medical tech nology has focused on the provider side from robots in surgery to the development of virtual human providers [16]. Research on virtual humans and their use as healthcare assistants cover multiple areas, such as health coaches [3,28], psychological evaluation and diagnostic in terviewers (DeVault et al. 2014; [35,51,54,92,100]), and virtual human patients for research, training, and safety assessment of new drugs [71, 115,123] (Appendix A).

On the patient side, wearable sensors connected to mobile devices have emerged for individuals’ health self-management and potentially for the diagnosis, treatment, and management of diseases (Appendix B). Despite the availability of numerous wearable sensors for tracking health parameters and many studies of their medical applications, their use has remained limited and anecdotal. Their usefulness has been questioned by medical researchers as “to what end is mobile health? Tracking and reporting data are means to an end, not the end itself” ([108], p. 963). We argue that neither research nor the industry has paid adequate attention to the use of technology on the patient side. Furthermore, they have yet to provide a viable and integrated online and offline system in which providers and patients come together, allowing patients to walk through the system with their physical self or virtual self to receive persistent care.

This paper provides the first step to address this gap. We rely on the design science theory [43] to propose the design of a medical system (called wepital) with real avatars for patients, develop a prototype that brings recent technologies together, and integrate them with the existing process of medical care for persistent, continuous, and real-time medical care. The integrated (online and offline) system creates a smooth process of care and extends the capacity of hospital systems through adding online options. Moreover, this design renders communication richness for web-based medical care that existing online cares lack.

## 2. Literature Review

The use of technology in medical care has a long history. With the advent of the Internet and smartphones and their use in telecommuni cation, telemedicine has become a viable option to deliver care and has appeared under various names, such as teleHealth, eHealth, mHealth, eVisit, virtual care, and virtual visit. In defining telemedicine, medical research has distinguished it from health informatics early on (e.g., [85]). However, telemedicine goes decades back to NASA space missions that necessitated the monitoring of astronauts’ health in real time and the checking of their vital signs [23]. This approach did not migrate to civilian healthcare. Although the US government started reimbursement for telemedicine in the 1990s, technologies for public telemedicine took less sophisticated forms—phones, emails, blogs, and later video calls and smartphones [124], while most technology innovations concen trated on the healthcare providers’ side.

The US Space Program had solved this problem more than half a century ago. While it is impossible to provide a space suit for every citizen for an integrated system of care, the technology of wearable sensors with apps on smartphones already exists and has exploded in recent years. The literature reports numerous studies on the use of such devices in dealing with various diseases and health problems, including asthma, elderly care, heart failure, hypertension, atrial fibrillation, insomnia, Parkinson’s disease, mental health, cognitive impairment, and type 1 diabetes, as well as several review papers (Appendix B). This literature reports that sensors’ alerts increase people’s awareness of their health status.

However, serious issues continue to plague the effective use of new technologies for medical care. (1) Online and video visits lack persistence, in that once the session is over, no trace of visit will remain unless the physician captures some information about the session on another device. (2) Online and phone visits also lack the naturalness that patients experience in face-to-face office visits. (3) When using app data in an offline office visit, the data on patients’ mobile phone apps leave the office once the visit is over. (4) A database of wearable sensors<sup>2</sup> lists 421 such devices at the end of 2021, of which at least 362 are mobile health monitoring devices [81]. With the ever-growing number of wearable sensors with apps on smartphones, patients’ data are frag mented, disconnected, and scattered on a large array of devices. (5) There is little incentive and immediacy for standardization of data and data sharing across mobile health apps [81]. (6) It is observed that “[m] obile health data are likely to be more useful if combined with [elec tronic health record] EHR data for patient or clinician use.” ([108], p. 960). Such integration requires a process and a location that are not readily available yet [74]. This lack of persistence in sensor data prevents their use in medical decision-making. (7) The control, privacy, and ownership of sensor data, once shared, are not obvious for patients [108].

We argue that the first step is to provide a digital representation of the patient that can embody all health data regardless of their sources, such as real-time vital signs and medical records, under the control of the patient in a natural and understandable form. Therefore, the research questions are as follows: (1) Can we design a sensor-based online system that provides integrated and persistent care based on each patient’s digital self? (2) Will patients be satisfied with receiving care through such a system? We rely on the design science theory and its guidelines [43,47,122] in addressing these research questions.

Design science research is presented and assessed through proof-ofconcept and proof-of-value and use [43,46,47,107]. Proof-of-concept shows the feasibility and promising aspects of the design, whereas proof-of-value and use demonstrates that the design works in action. In this study, the proof-of-concept (Stage 1) involves demonstrating rele vance, presenting the overall design and its requirements, identifying kernel theories supporting the design, and developing a working pro totype of the design.<sup>3</sup> Examining the rigor of our design, the proof-of-value and use (Stage 2) involves a theory-based conceptual model for the design assessment and data collection through a labora tory experiment where the physician relies on the prototype to care for real patients. As evidence of use, we discuss the implications of our work, including a potential nationwide use of our design and its extension.

## 3. Definitions of Real Avatar and Wepital

## 3.1. Real Avatar

The sensor-based artifact proposed in this study is what we call “real avatar.” Avatars are variably referred to as digital personas, aspirational alter egos, and self-representations online [26,27,112] and have been used extensively in multi-person online games. Avatars have human functionalities, such as walking, talking, sitting, standing, teleporting, and interacting with others. Research has reported the use of “medical avatars” for communication and interactions with patients [1,67,131]. We define patient avatars as digital representations of patients. We refer to a patient’s “real avatar” as an avatar that embodies the patient’s vital signs (such as temperature, heart rate, and blood oxygen level) in real time and includes the patient’s health data and medical history—the patient’s digital self. Thus, a real avatar represents the patient more realistically. Moreover, since real avatars have many human function alities, patients can move their real avatars around and receive medical care at different locations, similar to what is commonly done in hospitals and clinics.

## 3.2. Wepital

Merriam-Webster defines a hospital as “an institution where the sick or injured are given medical or surgical care.” It is a physical location that has various specialties and levels of care, including ER, ICU, beds for overnight stays, pharmacies, and medical staff. At present, there is no web-based equivalent for a hospital. We define a wepital as a web-based equivalent of a hospital. We purposefully avoid the word “virtual” since patients’ real avatars digitally represent patients in real time, and the care in a wepital is real, persistent, and continuous. A patient’s real avatar can reside in a wepital and receive different types of care from the medical staff for a short or long period, while the patient stays at home.

We have technologies to create wepitals. Telemedicine and even virtual hospitals (e.g., Mercy Virtual Hospital) are already in place. The difference is that telemedicine with video chats is not persistent, still requires one-on-one interactions, and ends when the visit is over. Having patients stay in the wepital with their real avatars makes it possible to care for them continuously, ubiquitously, and in real time.

## 4. Stage 1. Proof of Concept

Appendix C contains an overall view of the proposed design. Fig. C.1 (Appendix C) shows the flow of data and interactions when a patient uses his/her real avatar to receive medical care in the wepital. Fig. C.2 provides a view of the wepital structure.

Design Relevance. The following scenario demonstrates the rele vance of the design [43,47]. Consider that you wake up in the morning and feel unwell. Maybe you are coming down with something that re sembles COVID-19. Normally you would wonder what to do next. At several points, you must decide what to do next with little certainty. Am I sick enough to ask for medical help? Should I wait to see what happens next? Should I go to the ER? Instead, this morning you decide to go to your device and open an app. This app has your avatar that communi cates with your smart sensors, such as your iWatch, Fitbit, Zephyr health belt, Helo, or advanced versions thereof. Thus, your vital information is loaded from your sensors to an armband of your avatar.

The app takes your avatar to the reception area of the wepital to which you belong. Your avatar’s armband has your encrypted ID and health insurance information that only the authorized receptionist avatar can recognize. The receptionist, through his/her avatar, registers you as a patient (you can hear and communicate with the receptionist through the avatar-to-avatar communication.) Based on the nature of your symptoms, you are advised to stay home while your avatar is sent to an observation room to stay. Now, your home (or a protected part of your home) has become a mypital or “my home-extended hospital.”

In the observation room, there are, say, 49 other patient avatars with low-grade symptoms similar to yours. There is a nurse avatar monitoring the patients in the observation room. Since the symptoms of patients in this room are not severe, the nurse avatar could be a virtual human nurse or an intelligent robot. This nurse avatar can answer simple relevant questions, access your avatar’s armband, and connect your ID to your medical records already in the hospital system. Using its AI algorithm, the nurse avatar decides that you can stay in the observation room for now, advises you to stay home, and suggests what to do and what to eat and drink. An avatar of a real nurse may check the room at given in tervals to make sure all questions are answered. There are posters and video links on the walls for you to read and watch. You talk with other patients with similar symptoms through your avatars, sharing experi ences and information, all anonymously. There is little sense of isolation and being quarantined or imprisoned at your home. It is more like a community of patients with similar symptoms and medical conditions.

At night, the nurse avatar notices from your sensor updates (or your updates to the app or your verbal communication) that you have developed a high fever. You get a notification and confirm the changes. Your avatar is now moved to another group-care room, Room A, where there are, say, 10 patients with a high fever. There is a nurse practitioner behind the nurse avatar in this room, checking your vital signs and medical records and notifying you (through your avatar) what to do. This room is visited by a doctor avatar (with a doctor behind the avatar), who checks the status of patients at appropriate intervals. The doctor avatar may examine you through a private video chat (heard and seen only by you and the doctor) if needed. You may need some medications, which are ordered online and delivered to your home. Your avatar stays in Room A for constant observation as you stay at your home (your mypital).

Later your condition deteriorates, and you are told to move your avatar to another room, Room B. Now you are continuously under observation by a nurse or (more likely) by an intelligent robot nurse. You continue to worsen. The robot informs a nurse. After the interaction with you and maybe a video chat, the nurse decides that you need to be transported to the hospital, dispatches an ambulance to your home, and informs your physician. While in the ambulance, your admission process takes place based on the information on your real avatar, and the on-call physician checks your medical records and vital signs on your real avatar and orders tests. Upon your arrival to the hospital, you are directly transferred to your assigned room, and tests are immediately done. No need for you to decide when to call an ambulance or whether to go to the emergency room (ER). You do not wait in the ER, and the admission process is already done.

Advantages of the Design. (1) You receive persistent care at home and are moved to a hospital as soon as you need in-person hospital care, and hence your online and offline medical care is integrated and streamlined. (2) Your wearable sensors continuously communicate with and send data to the medical staff in the wepital, who care for you as soon as you need it. Thus, you avoid the uncertainty about what to do and unnecessary trips to the ER. (3) In all stages of your care, you can have a sense of being there in a wepital and observe how the medical staff uses your digital self to take care of you. (4) You have the control of your real avatar and its embedded data. You move your digital self around and use it to communicate as though you were there. (5) You see the embodiment of your data and can move it from one medical office to another to receive care when needed. (6) The hospital expands its ca pacity through its wepital and reaches more people and service areas.

## 5. Kernel Theories Guiding the Design and Its Assessment

The design science theory prescribes the specification of metarequirement and requirements of the design, as well as kernel theories that support the design and its assessment [43,46,47].

## 5.1. Meta-requirement of Design—Patient Satisfaction

The success of a design depends on its most important users. In our case, patients are the most important consumers of medical services. User satisfaction has emerged in numerous studies as the gold standard for the success of a design and its implementation in the IS literature [29, 72,88]. Patient satisfaction is also the gold standard for patients assessment of providers [6,9,101] and in the assessment of telehealth [84]. Hence, patient satisfaction constitutes the “meta-requirement” of our design.<sup>4</sup> The next step is to identify the requirements for achieving patient satisfaction.

## 5.2. Theory of Affordances Supporting the Design Requirements

In specifying the overall design requirements, we rely on the theory of affordances as a kernel theory. Gibson [41] coined the term affor dances as the “action capabilities available in organism-environment systems” (Delucia and [52], p. 421). Affordance emphasizes the com bination of two components: the organism (animals, including humans) and the environment [42]. Although the theory of affordances has been applied in many areas, including the design and assessment of infor mation technology (e.g., Kannengiesser and Gero 2012; Volkoff and Strong 2013 [113]), the conceptualization of affordances may vary [52]. Chemero [20] provided a succinct presentation of the theory of affor dances (p. 190):

Affordance = Perceived [animal, affords-BehaviorB (feature, ability)], where the feature of the environment, together with the ability of the animal, affords the animal BehaviorB, and affordance is the perception of the animal about BehaviorB. The environment entails the situation or context in which an affordance is perceived.

The theory of affordances treats an IT artifact with a “holistic view,” avoiding the need to “decompose” it into smaller parts ([68], p. 622). Applying this theory to the context of virtual reality and augmented reality, Steffen et al. [113] identified four types of affordances: dimin ishing negative aspects of the physical world, enhancing positive aspects of the physical world, recreating existing aspects of the physical world, and creating aspects that do not exist in the physical world. An IT artifact may entail features from each category. Applied to our design, the wepital and real avatars constitute the environment that entails the context of medical care, and patients are the user group. Patients’ en gagements with their relevant abilities within this environment result in affordances. Based on the literature, we have identified three important affordances when receiving medical care online: trust, convenience, and telepresence.

## 5.3. Trust Affordance

Trust becomes essential when “the trustor depends on the trustee, being vulnerable to its actions but unable to control its behavior” ([5], p. 3).<sup>5</sup> When receiving medical care, patients feel vulnerable since their health is at risk, they have no expertise in dealing with the medical problem, and they have little control over the attending physician or the hospital/clinic that provides the settings and employs the physician. Trust involves the beliefs that the physician or the hospital/clinic is competent, honest, and has the patients’ best interest in mind [19,111].

## 5.4. Convenience Affordance

Access to medical care has a temporal dimension, which “include the time required to receive services and the opportunity cost of that time. Perceived temporal access represents the self-reported time burden and temporal convenience of receiving services” ([38], p. S643). Patients consider convenience when seeking non-emergency medical care. Research shows that some patients with non-emergency cases go to the ER for convenience [120]. In the USA, patients with low-acuity conditions visit care providers fifty million times per year and are switching to new options (such as retail clinics, drugstore and grocery store clinics, and home visits by a nurse) for convenience and shorter delays in appointment [73]. The four-fold increase in retail clinic visits to six million annually in a two-year period (2007-2009) indicates the importance of convenience for patients in receiving non-emergency care [73].

## 5.5. Telepresence Affordance

Minsky [77] first coined the term “telepresence,” which referred to the remote manipulation of physical objects. In our case, telepresence includes (but is not limited to) the remote manipulation of an IT artifact (real avatar).<sup>6</sup> Telepresence constitutes a perception of “being there” and could vary depending on the environment’s interactivity ([114], p. 6). Research has shown that 3D avatars and virtual worlds increase telepresence [82,93]. Applied to our study, the wepital constitutes a technology-mediated environment in which patients participate with their real avatars and receive medical care. This perception has two components: (1) our design in creating the environment similar to a visit with a physician in a hospital/clinic and (2) the patient who participates in this environment and perceives it as “being there.” Thus, telepresence meets the definition of an affordance—an environment and the patient who uses it for a medical visit.

## 5.6. Kernel Theory Guiding Telepresence Design

How should telepresence’s vividness and interactivity be incorpo rated into the design? One way is to build a campus with buildings and objects in the virtual environment that creates a vivid sense of being in a medical environment and has the capability of being interactive (Fig. C.2 in Appendix C). But what should guide the design of commu nication media for interactivity? The kernel theory that supports the design of communication media is a synthesis of the media synchronicity theory [30] and media naturalness theory [57-59], which were both developed as alternatives to and extensions of the media richness the ory.<sup>7</sup> We use a synthesis of media richness, synchronicity, and natural ness and argue that caring for patients requires a rich set of alternative media that meets the patient–physician communication needs and comes close to face-to-face interactions to promote the interactivity and vividness of the design. The prototype illustrates how the affordances are incorporated in our design.

## 6. The Prototype—Wepital with Real Avatars and Video Links

In a dual-institution (a business school and a medical college) collaboration, we have built a prototype wepital campus on our land in Second Life©, with the following features.

## 6.1. Real Avatar

What makes persistent care for patients in the wepital possible is the real avatar. The challenge is to have the real avatar embody the patient’s vital signs. We used sensors that can send patient vital signs to a cloud database. The sensors we used include FDA-approved BioHarness (by Zephyr, which was later acquired by Medtronic), oximeter, weight scale, and blood pressure sensors. The FDA approval of a wearable sensor is the evidence for its measurement quality (Muzny et al. 2019; [108]).<sup>8</sup> All sensors can connect to Zephyr’s mobile app through Bluetooth. The app uploads patients’ vital signs to Zephyr’s cloud database. We wrote a program to download the vital signs from the cloud database in real time and upload them to the avatars we created in Second Life©. The remotely sensed vital signs are loaded to a green armband worn on the patient’s real avatar.

![](/api/attachments/WCY935QN/fulltext/images/b4e524b1687266361f9d9cf4ebd5243b536e84e570f5785b1b4981fe23e61bf1.jpg)  
Fig. 1. Patient Real Avatar in the Wepital.

Fig. 1 shows the implementation of the design (reported in Fig. C.1, Appendix C). The data flow (1) from the sensors (attached to the pa tient’s body) to an app on a mobile device, (2) which sends the vital signs to the Zephyr/Medtronic cloud database, (3) which in turn are downloaded to our database, and (4) which is then uploaded to the green armband of the patient’s avatar in the wepital. This way, the avatar embodies the patient’s vital signs in real time.

It is possible to load the patient’s medical records and IDs to the avatar. Since the Health Insurance Portability and Accountability Act of 1996 (HIPAA) restrictions at present prohibit our access to patients medical records, this aspect can only be applied in the actual imple mentation of our design by hospitals and clinics. Such addition may be less complicated since most of patients’ medical records do not need update in real time. Furthermore, patients can see where their data reside and conveniently move their real avatars from one wepital to another, boosting their sense of convenience and trust in using the system.

## 6.2. Wepital Campus

In instantiating the overall design (outlined in Fig. C.2, Appendix C), we built a wepital campus with multiple areas and buildings, including an arrival space where avatars land when patients log into the wepital, an auditorium/ observation building, a physician building, a reception building, and others [131,132].

## 6.3. Buildings

The auditorium/observation building has a large conference room for patient avatars under observation and a podium for nurses to observe patient avatars. The physician building contains multiple offices (A, B, and C). Office A is a room for group visits with the physician, Office B for one-on-one visits with the physician, and Office C for emergency ex aminations of patients’ avatars. The design of the buildings emulates familiar pleasant and airy architectures, hence promoting the synchro nicity and naturalness of the wepital environment. The reception building has a reception area for patient avatars to register or schedule a visit.

The building of the wepital campus went through multiple iterations, including consulting with a Second Life© expert, eliciting feedback from physicians, and testing with student participants. We also presented our design to health community leaders in our state. We made many ad justments accordingly. For example, early on, we had a speaker wand that is passed to each speaker to control who should speak next. In testing the prototype, we found that such a wand is not needed and could interrupt the flow of interaction.

## 6.4. Teleporting

We included teleporting stations in the reception building and physician building. By clicking the stations, an avatar can teleport back and forth between the two buildings. This avoids the need for patients to walk their avatars down the path between the buildings, hence saving time and increasing the convenience of moving around in the wepital.

## 6.5. Trust Cues

It is shown that trust can be calibrated by providing information and settings that promote trust [21]. To this end, each avatar is assigned a fictitious name, and only authorized caregivers know the identity of the patient behind the avatar. This anonymity protects patients’ privacy [110] and enhances their trust in the wepital. To further protect the privacy and promote the trust of each patient, only the patient and authorized caregivers can click the armband and see the vital data in real time.

To further boost trust and vividity, we included cues, such as signs from the two universities involved in this project, both well-known in the area. The wepital campus includes the façade of one of the university buildings (where most data collection took place for the experiment). Physician avatars wear white coats common in offline visits.

![](/api/attachments/WCY935QN/fulltext/images/dd8d1666bd2274c8eee23611e03770d59188a60c21bccc34e10de304c2e625e0.jpg)  
Fig. 2. Access to a Patient’s Real-time Vital Signs in the Wepital.

We added numerous cues to the wepital campus to give patients a sense of vivid and immersive experience—patients feeling as if they were visiting a medical campus. These cues include trees and bushes outside, plants inside offices, windows with views of the sky and greeneries, appropriate signages, automatic doors for patient avatars to pass through, medical exam tables for patient avatars to sit on for oneon-one visits, doctor chairs for one-on-one examination, chairs ar ranged in a semi-circle for patient avatars to sit on for group visits, and medical objects, including wheelchairs, hospital infusion stands, and Xray-reader screens.

## 6.6. Communication Methods

In the wepital, caregivers’ and patients’ avatars have multiple op tions for communication, including voice, text message, and body ges tures, and use them as desired, thus increasing the media synchronicity and naturalness in the wepital. If a patient desires to avoid speaking for utmost privacy, he/she can use text and gestural cues to communicate with the medical staff.

## 6.7. Video Visit

The wepital has a video component that allows the doctor to see and examine a patient one-on-one via a video link, which provides the maximum synchronicity and naturalness cues, while preserving the privacy of the patient in a group setting. When a video visit is needed, the doctor and patient can click on a secure link provided in the patient’s green armband, visible only to the patient and attending doctor. We used ustream.tv<sup>9</sup>, which was later acquired by IBM. This component is now changed to Zoom.

Fig. 2 shows the group office, where patients visit the physician in a group setting. When the physician clicks on a patient’s green armband, a window opens (only visible to the physician and the patient, thus pre serving privacy and increasing trust). It has the patient’s vital signs and a link for a one-on-one video visit. When the physician needs to “see” the patient, both would click on the link to have a private video consulta tion. Since the patient can always mute the voice of his/her real avatar in the group room, the one-on-one video conversations remain private, hence preserving privacy.

## 6.8. Persistent Care

For patients who need to be under observation, they would be asked to move their avatars to the auditorium/observation building (Fig. 3). A nurse would have access to their vital signs on the Zephyr/Medtronic secure Web portal. The nurse (or an intelligent robot nurse) can continuously monitor their vital signs in the observation room. More over, the patients can continue to ask the nurse questions or interact with other patients’ avatars.

## 7. Stage 2. Proof of Value and Use: The Assessment Model

For the proof-of-value and use, we assessed our design by using the prototype in a theory-guided laboratory experiment with real patients (conducted prior to COVID-19). The patients visited a physician (who was attending with his avatar) in the wepital with their real avatars and then took a survey after the visit, providing data for the assessment of the success of the wepital visit.

## 7.1. Design Rigor

We conceptualized a theory-based model to assess the salient factors that contribute to the successful use of the wepital design from the perspective of patients, as shown in Fig. 4. The measure of success is patient satisfaction with the physician in the wepital. We continue to rely on the theory of affordances as the kernel theory in hypothesizing how design affordances impact satisfaction—the meta-requirement of the design.

## 7.2. Telepresence Affordance→Satisfaction

Telepresence affordance varies across patients. Those who enjoy new experiences are more willing to try new venues for receiving medical care. Such people will have a higher perception of telepresence.

![](/api/attachments/WCY935QN/fulltext/images/fdba3fbc9fcd886d7b52373b918744cd65c18132d44957d78267151b9c2c29fc.jpg)  
Fig. 3. Nurse Avatar Monitoring Patients’ Real Avatars in the Wepital.

![](/api/attachments/WCY935QN/fulltext/images/96eae168bbcb45124be5e7ea1663c6288ad9c6cdc5847e11e8cd35dfcc88ea61.jpg)  
Fig. 4. Wepital Patient Satisfaction Model.

Research has shown that telepresence enhances enjoyment [61,82]. People approach the experience with positive anticipation and curiosity, increasing their focus on being in the wepital and participating in the interactions. Their active participations lead to more engagement with the physician, and hence more satisfaction with the physician. Thus, we posit the following:

H1. The telepresence affordance of patient-wepital visit is positively associated with patient satisfaction.

## 7.3. Time Convenience Affordance→Satisfaction

Since the COVID-19 pandemic, editorials and policy recommendations point to Internet-based care delivery as a convenient alternative (e.g., [135]). In the case of the wepital, the time convenience includes eliminating the travel time to access medical care depending on the patient’s location and the availability of needed medical specialty. Therefore, time convenience is an affordance as perceived by each pa tient using the wepital. Research has shown that patients’ perception of convenience influences their satisfaction with the care they receive (e.g., [38].) Hence, we posit the following:

![](/api/attachments/WCY935QN/fulltext/images/d02c80a9f39b086c58557c96a8b79a55bc46708dc74ab8c46884193cb0454e3a.jpg)  
Fig. 5. Estimated Wepital Patient Satisfaction Model.

H2. The time convenience affordance of patient-wepital visit is positively associated with patient satisfaction.

## 7.4. Trust Affordance→Satisfaction

Trust has emerged as beliefs about the trustee’s competence, benevolence, and integrity. In this study, trust refers to trust beliefs. The ideal view of beliefs refers to them as “a single corpus of beliefs which (a) is consistent and deductively closed, and (b) guides all of the (rational, deliberate, intentional) actions all of the time” ([34], p. 48). However, beliefs are fragmented and emergent from experiences and perceptions. “A belief-forming mechanism—for example, visual perception—pre sents us with a candidate object of belief” ([34], p. 54). Research has supported the view that beliefs evolve from experiences and exposure to environments and objects in different contexts [21,130]. Therefore, we argue that as patients experience the wepital, they form the trust affordance needed to visit the physician who operates within the wepital. A higher level of trust increases satisfaction [133]. Hence, we posit the following:

H3. The trust affordance of patient-wepital visit is positively associated with patient satisfaction.

## 7.5. Real Avatar Affordance→Satisfaction

People may create avatars for self-representation online as an ideal self, a fantasy self, or a realistic self (Messinger et al. 2008; [117]). Studies have proposed standards for “universal avatars” that can work in different virtual settings and across platforms (Domer 1997; [75]). Ap ple’s avatar patent indicates that the company is working on avatars that can operate across apps and platforms.<sup>10</sup>

Research shows that avatars can change people’s self-perceptions, attitudes, and behaviors [60,75,129].<sup>11</sup> Research also shows that, in creating their own avatars, people tend to keep their core personal identifiers (such as race and gender) but may enhance their physical appearances [75].

Different fields, including healthcare, have begun to explore relying on avatars for communication. Research has reported on cases where providers rely on avatars to deal with medical issues (such as obesity, neurological disorder, and mental health), help patients visualize their healthy self, simulate personalized drug management, and track health progress [48,67,76,95,98]. We argue that adding real-time vital signs (and potentially medical records) to a patient’s avatar creates an avatar that closely represents the patient and increases the bond between the patient and avatar. Therefore, having a real avatar creates the percep tion of a realistic self-representation and enhances patients self-identification with their avatars. This brings the experience of visiting the wepital closer to the familiar office visit, thus increasing the patient’s satisfaction with the wepital. Hence, we posit the following:

H4. Having a real avatar is positively associated with patient satisfaction.

## 7.6. Impact of Patient Predisposition: Flexibility About Medical Care

Patients’ predispositions play a part in forming their affordance perceptions. One such predisposition is being flexible about the venue in which they receive medical care. Research shows that biological systems tend to resist change and revert to the status quo to maintain equilibrium and homeostasis [62]. Some people have a similar tendency. Resistance to change is a preference for the status quo. People may resist change because of the perception of threat, such as loss of control, fear of un certainty, lack of knowledge, and concerns about cost and effort [12, 121]. On the flip side, some people are more inclined to have variety-seeking tendencies, which are defined as the tendency to choose an option that are different from the previous one [56].

Research has studied reasons and motivations for variety-seeking tendencies. Multiple disciplines, including psychology, marketing, and economics, have examined the motivations, sources, and types of such tendencies [70]. Motivations can be derived (such as trying new options including balancing between choices to achieve desired outcomes, addressing a need, reducing uncertainty, and dealing with a given sit uation) or direct (such as having a novel experience, enjoyment, and gaining social status) [53,70,94,105]. Culture also plays a role in variety-seeking as a means of self-expression [56].

In choosing options for receiving medical care, the variety-seeking tendency could have similar motivations, including having more than one option for receiving medical care, balancing between the required time and effort in receiving medical care, enjoying new experiences with technology, prior experiences, prior knowledge, or dealing with a given medical situation. Variety-seeking could be a general tendency or spe cific to a given context. In our case, we focus on variety-seeking in terms of choosing the venue to receive medical care, which we call flexibility about method of care. Having such a flexibility gives people more pos itive views about their experience of receiving care in the wepital and in assessing the affordances of the wepital. In other words, flexibility about method of care is one of the “abilities” of patients that contribute to the telepresence, convenience, and trust affordances. Hence, we posit the following:

H5. Flexibility about method of care is positively associated with tele presence affordance of the wepital.

H6. Flexibility about method of care is positively associated with time convenience affordance of the wepital.

H7. Flexibility about method of care is positively associated with trust affordance in the wepital.

## 7.7. Impact of Patient Predisposition: Lack of Privacy Concern

HIPAA protects the privacy and security of patients’ medical infor mation and treats the privacy of medical records as an enforceable right. People tend to be protective of their sensitive personal, especially financial and medical information. Rising incidents of data breaches in large corporations and governmental institutions have raised people’s awareness about protecting their sensitive data in the online environ ment. Research has measured privacy in different forms, but privacy concern (or lack thereof) has emerged as an appropriate construct for the measurement of privacy [4,127]. Privacy concern is the extent of people’s worries that their personal information could become the subject of opportunistic behaviors or the source of embarrassment [5]. People who worry about their privacy tend to be hesitant to trust, especially in the online environment.

Studies on privacy concern about personal information in finance, ecommerce, and online medical visits have reported that privacy concern has a negative effect on trust. Conversely, the lack of privacy concern has a positive influence on trust [5,50,131]. Applied to the present context, the lack of privacy concern is a patient predisposition that promotes trust affordance in the wepital. Hence, we posit the following:

H8. Lack of privacy concern is positively associated with trust affordance in the wepital.

## 7.8. Impact of Patient Predisposition: Understanding Information

Research and practice in healthcare have emphasized the importance of patient-provider communication in the care process [32]. Depending on their personal characteristics, patients vary in their perception about their communications with their providers [32]. In virtual visits, pa tients simultaneously operate in two worlds—virtual and physical. Some medical fields take advantage of this duality by using virtual worlds to distract patients from various physical circumstances, such as physical pain, dependency on opioids, or dentist-office anxiety [44,106,125].

The two-world distraction could exist in reverse. Disease symptoms and physical environment could distract some patients from fully attending to the communication in virtual worlds. Some people need to focus on reading lips and body language to understand the verbal information. Even the immersive nature of virtual worlds could distract some patients from fully attending to and understanding the information [82]. At the same time, understanding what is being communicated is essential in forming trust [111,131]. This is particularly important in medical visit since the information could critically impact a patient’s well-being. Therefore, we argue that patients’ understanding of information in the wepital is positively associated with trust affordance. Hence, we posit the following:

H9. Understanding information in the wepital is positively associated with trust affordance in the wepital.

## 7.9. Control Variables

Several control variables could influence the successful use of the wepital. Patients’ demographics may influence their perceptions about the visit in the wepital. Furthermore, satisfaction with their own phys ical clinic and the severity of their symptoms may influence their per ceptions and experience of visiting the physician in the wepital (Fig. 4).

## 8. Experiment and Data Collection

## 8.1. Experiment Design

We used our wepital prototype to carry out an experiment with real patients with gastrointestinal (GI) problems. We chose GI problems because they are chronic diseases suitable for our IRB requirement, we had a GI specialist physician participating in the experiment, and more than 60 million people in the USA suffer from them. <sup>12</sup> We received a strict IRB permission for our experiment from the gastroenterology clinic of a hospital associated with a Midwestern medical school. The IRB approval process went through a prolonged and extensive scrutiny. To examine the impact of real avatars on patients’ satisfaction, we recruited two groups of volunteer patients for the experiment, one group without wearable sensors (using a regular avatar) and the other with wearable sensors (using the real avatar). We collected data for the two groups at two different time intervals since the physician needed to follow a fixed script that excluded/included reading patients’ vital signs from their sensor armbands. Appendix D reports details of the recruit ment and experiment.

## 8.2. Data Collection

Patients attended the group settings, as uniquely enabled by the wepital to protect patient anonymity, normally with two people in each session. Due to difficulty in scheduling patient visits, if a patient volunteer had to cancel at the last minute, one of the authors attended the session as the second patient with a patient avatar and went through a scenario with a given set of symptoms, questions, and responses to the physician questions and had a video visit, giving the volunteer the same impression of a group session, to preserve the consistency of data collection for all volunteers. Patients took an online survey on the wepital after the visit. We collected data from 63 patients (29 with and 34 without vital signs added to their avatars). Since two participants (with sensors) refused the one-on-one video visit, we removed their data in the analysis for consistency. Thus, the data analysis was based on data from 61 patients.

## 9. Data Analysis and Results

Whenever possible, we adopted scales from the literature for measuring the model constructs. Based on the literature guideline, we converted all scales to semantic differential scales to ensure content validity and reduce the common method bias (CMB) [22,91]. 13 Appendix E reports the construct definitions and main sources. Appendix F reports the instrument used to collect patient data at the end of the experiment. Appendix G reports demographics of the participants.

## 9.1. Data Analysis

After the data collection, we used a marker variable to purify the collected data by regressing each measured item on the marker variable and capturing the residual of the regression analysis. The captured regression residual replaced the measured item [40,91]. We used the dataset consisting of the columns of captured residuals for our analysis. These precautions addressed the potential threat of CMB in our data.

We performed exploratory factor analysis (EFA) of the constructs. Appendix H reports the results of EFA. All items appropriately loaded to their respective constructs. There was no cross-loading of more than 0.40 (the one minor exception was 0.401). EFA results supported the convergent and discriminant validity of the constructs. We checked for the reliability and validity of constructs in multiple ways, as reported in Appendix I. We used Mplus for model estimation.<sup>14</sup> Appendix J reports the fit indices for the estimation of the measurement model, as well as for the estimated model. All fit indices of measurement-model estima tion were desirably above or below the corresponding thresholds, indi cating a good model fit. Appendix K reports the confirmatory factor loadings in the measurement model. All factor loadings in the mea surement model were above 0.89, and all $\mathrm { R } ^ { 2 }$ values were above 0.73 with highly significant t-values. The results for the measurement model provided additional support for the discriminant and convergent val idity of the constructs. We then estimated the Wepital Patient Satisfac tion Model (Fig. 4) using the MLM method in Mplus.

## 9.2. Results

All but one fit indices for the estimated model were desirably above or below the corresponding threshold levels. The only exception was the standardized root mean square residual (SRMR), which was slightly above the threshold. This was due to the relatively small size of our sample. Asparauhov and Muth´en [2] point out that for small samples, the SRMR above 0.08 commonly occurs and should not be a cause for concern.<sup>15</sup> Fig. 5 reports the estimated model.

The statistically significant $\mathrm { R } ^ { 2 }$ values provided further support for model fit. Patient satisfaction with a physician had an $\mathrm { R } ^ { 2 }$ value of 0.85 (p<0.001). Telepresence, convenience, and trust had $\mathrm { R } ^ { 2 }$ values of 0.54, 0.40, and 0.73, respectively, all with significant p-values well below

0.001. Together, the fit indices showed a satisfactory model fit.

Fig. 5 shows the standardized path coefficients of the model and their levels of significance and corresponding hypotheses. Telepresence affordance had a path coefficient of 0.41 (p<0.001), supporting H1. Similarly, convenience and trust affordances had significant path co efficients of 0.33 and 0.43 (p<0.001 for both), supporting H2 and H3. Having real avatars had significant positive association with patient satisfaction, with a coefficient of 0.11 (p<0.01), supporting H4.

H5–H9 reflect the influences of patients’ predispositions on their perceptions of affordances. Flexibility about method of care had a strong influence on telepresence, convenience, and trust affordances (H–H7) with coefficients of 0.70, 0.63, and 0.29 (all at p<0.001), respectively, indicating that patients with this predisposition could be more likely to form positive perceptions of affordances about the wepital. An unex pected result was that lack of privacy concern did not show a significant influence on trust (H8). Understanding information exerted a strong influence on trust in the wepital, with a path coefficient of 0.65 (p<0.001), supporting H9.

## 9.3. Control Variable Results

Except for gender, none of the control variables was statistically significant. Fig. 5 shows that women were more likely to perceive tel epresence affordance, with a path coefficient of 0.23 (p<0.001).

## 10. Discussion

Several serious gaps in online medical services and use of mHealth prompted our first research question: whether we can design a sensorbased online system that provides integrated and persistent care based on each patient’s digital self. In addressing this research question, we presented a theory-based design. The proof-of-concept stage showed the feasibility of our design. This design has persistence and comes close to a natural interaction in medical offices. It addresses the fragmentation of data across various medical disciplines [90], provides a mechanism for the integration of patients’ mHealth data and electronic health records as has been called for in the medical literature [108], and motivates the standardization and interoperability of data across medical sensors [81]. It gives a patient control of his/her real avatar, its movements, and embedded health data. Furthermore, the anonymity of patients in a group setting allows them to benefit from other patients’ information, experiences, and social interactions, while their true identities are protected.

Our proof-of-value and use involved a limited experiment with real patients using the prototype, in response to our second research ques tion: whether patients will be satisfied with receiving care through our designed system. The results show that our design could be successful in terms of patient satisfaction—the meta requirement. Affordances of trust. convenience. and telepresence can lead to the successful imple mentation of wepitals. Furthermore, people who have more flexibility about method of care and better understand information in the wepital settings would be among the first group willing to receive care in wepitals, with women being more willing to do so. Wepitals, like their hospital counterparts, need to provide a high level of security and pri vacy for patients to foster trust.

To gain a better understanding of the patients’ views about real av atars, we asked questions regarding their feelings and beliefs about their real avatars. Fig. 6 shows that the patients had favorable feelings and beliefs about their real avatars, hence supporting the value and use of our design.

## 11. Implications

## 11.1. Theory Implications

Our work shows that real avatars have the potential to represent people in critical contexts, such as medical care. Our work also points to possible patients’ emotional attachment to their avatars as a mode of self-representation when the avatars carry private and biological ele ments. Although avatars as the next mode of communication have appeared on the technology horizon, real avatars as digital self could go beyond communication and open pathways to novel methods of living and social life.

![](/api/attachments/WCY935QN/fulltext/images/42acec7ebd33706c7f9d86c68ef0096389658d48690d02f529dd356b96a3c3c4.jpg)  
Fig. 6. Patients’ Feelings and Beliefs about Their Real Avatars\*.

![](/api/attachments/WCY935QN/fulltext/images/54490d70830937cf626e47916b7bfadbfb2e56875dc97d7f28c67f76dcf38cea.jpg)  
\*Measured on continuous scales from 0 to 10. Feelings: having high anxiety (0)/having little anxiety (10); very negative (0)/very positive (10); not having fun at all (0)/having a lot of fun (10); not enjoyable at all (0)/enjoyable for sure (10); not pleasant at all (0)/quite pleasant for sure (10); very frustrated (0)/quite relaxed (10); very unsafe (0)/quite safe (10); not satisfied at all (0)/very satisfied (10). Beliefs: not useful at all (0)/very useful (10); not a real experience at all (0)/like a real experience (10); requires too much effort (0)/requires little effort (10); requires too much cost (0)/requires little cost (10); not a real option for me (0)/a real option for me (10)

Our work also demonstrates that the theory of affordances is an appropriate framework for theory-based assessment of design success. Of particular importance is technology design for healthcare delivery. Patient-based technologies, such as sensors and monitors, play increasing roles in healthcare. Our approach provides medicaltechnology researchers and developers with a theoretical basis to test their technology-assisted delivery modes. They could use the theory to discover affordances that contribute to the success of their design and identify predispositions of patients who would be early adopters of their new modes of delivery.

Another theoretical contribution of our work is the identification of affordances that explain a large variation in patient satisfaction when using online delivery of medical care. Many approaches in telemedicine, e-health, and virtual health do not consider the importance of tele presence in helping patients feel they are receiving care at par with visits in physical offices. Our work points to the importance of telepresence in the design of web-based care delivery.

Medical research has identified the importance of trust in physical encounters between patients and care providers. Our work shows that trust plays the same important role in web-based care, and patients understanding contributes significantly to forming such trust. As AI and robots take up a role in patient care, trust affordance should play a significant role in theory-based assessment of such technologies.

## 11.2. Practical and Policy Implications

IS research has received criticism for its inadequate discussions of relevance, practical applications, and policy recommendations [78], which would provide further support for design rigor [46]. In response to this, we describe how our work could have far-reaching applications and policy implications for extending medical capacities, as well as re quirements for such implementations.

First, our design makes it possible to provide persistent care for pa tients while they stay at home. This expands the hospital capacity to patients’ homes (mypital) while their real avatars are continuously being monitored by a nurse or intelligent robot nurse in different rooms, depending on the type of diagnostic and severity of symptoms, in the wepital. Patients do not need to decide when and how to seek help, call an ambulance, or go to the ER.

Second, short-term rehab centers, nursing homes, and other in stitutions that provide care for patients after hospitalization or for chronic diseases also benefit from this approach. By having sensors on patients to provide real-time data to avatars in wepitals, medical experts and nurses assisted by intelligent robot nurses can continuously monitor patients under their care in the wepital and take immediate action when patients’ real avatars signal an emergency. Patients’ loved ones and family members responsible for the patients’ medical care can, with appropriate permissions and access, monitor the well-being and health status of the patients.

Third, our work promotes the creation of pools of qualified and credentialed medical staff (let us call them docpitals, short for doctorextended hospitals) who can treat patients in wepitals across state bor ders. When a hospital becomes short of medical staff, it can ask for help from qualified medical staff in docpitals to cover certain shifts or certain wepital rooms. As shown in Fig. 7, hospitals can extend their physical and staff capacity by adding patients’ rooms at home (mypitals), virtual human supervisors in wepitals, and medical staff in docpitals. In times of extreme need, hospitals can immediately increase capacity by adding more rooms to their wepitals and staffing their wepitals with additional intelligent robots, virtual human providers, and medical staff in docpi tals. Thus, hospitals will have the capacity and capability to better handle pandemics on short notice. More importantly, they will have the capability to extend their resources to remote parts of the country or even the globe.

Fourth, our work also makes it possible for hospitals to transfer a patient’s avatar to another hospital’s wepital for various reasons, such as to a hospital with more expertise, for a second opinion, or upon the patient’s request. The patient’s avatar (which embodies all his/her medical records) can easily teleport to another wepital.

Fifth, in an advanced application, states can create an infrastructure that facilitates such movements. Each state or city (depending on the number of its hospitals and its population) can create a hub, called a wepital hub, on which its hospitals set up their wepitals. Each hub is supervised for security and compliance at the state level. The collection of wepital hubs creates the US Medical Care Internet, which should be regulated at the federal level for security and compliance (Fig. 8). State and federal governments can provide medical services to more people and handle medical crises with more options and resources. They can disseminate health information and educational materials in wepitals when people have the time and motivation to receive such information and education.

![](/api/attachments/WCY935QN/fulltext/images/5b1dc01aef68ab980bd8acd347df4ea74eb3b3537142c317fab159790bf93b5a.jpg)  
Fig. 7. Extending Hospitals’ Capacity and Providing Persistent Care.

![](/api/attachments/WCY935QN/fulltext/images/7aebbdcfdba2563dc92b333f355c601183f0c27338d1a7031016321d0ccaf5b8.jpg)  
Fig. 8. An Advanced Application at State and National Levels

Sixth, another application of our work is extending patients’ real avatars to the organ level. At present, medical records are displayed on screens and interfaces that are not natural to understand for a nontechnical person. Patients’ avatars could become an interface for pre senting health information at the organ level. For example, the data, background information, and medications related to heart could be displayed on the avatar’s heart, even in multiple languages. Patients and physicians can retrieve the information by clicking the avatar’s heart. This way, patients and physicians will have a common point of reference for communication and understanding. For information that relates to multiple organs or the entire body, armbands, and other avatar acces sories could be used for points of access (Fig. 9a).

Seventh, physicians’ avatars could be extended to include their job related information, such as their patient schedules and patients under persistent care in wepitals. Physicians’ avatars could become real by adding real-time information to their avatars, as shown in Fig. 9b. Physicians can have immediate access to patients’ full information, use their own real avatars as a central point of access to their schedules, messages, and emergency information, become part of docpitals to extend their service areas, and work from home if desired.

Eighth, patients can access the medical care they need and receive persistent care whether they stay at home or remain in care facilities. While in a wepital, patients can talk with other patients about their experiences, learn from each other, avoid unnecessary exposure to contagions, counter the sense of isolation by socializing with others in the wepital, have their loved ones visit them (with permission) from any distance, and move to another wepital for a second opinion or treatment.

Ninth, hospitals can increase their capacity while reducing costs and achieve increased flexibility faster and at lower costs in times of crisis.

This can slow down the rate of increase in healthcare costs. Hospitals can extend their areas of service to reach more patients, extend their care to older adults, hospice care, children, and rehab patients, have advanced notice about potential patient admissions based on the number of pa tients under persistent care in their wepitals, and streamline patient transfer into and out of their care.

## 11.3. Requirements for Successful Implementation

A successful implementation of our design relies on several critical requirements, as listed in Table 1.

## 12. Limitations and Future Extensions

The real avatars in our prototype had sensors loading patients’ vital signs in real time, but due to HIPAA rules, we did not have access to patients’ medical records. Future extensions of our prototype need to examine the effect of real avatars that have access to patients’ medical records.

The size of our sample, albeit after multiple years of diligent recruitment, was small due to the extremely sensitive nature of the context and strict IRB rules on recruiting patients for our experiment. Also, our experiment was conducted in a single context (patients with GI problems) using a prototype. Future extensions could include in-depth experiments and study cases in various medical disciplines with larger samples collected from real hospital-owned wepitals to validate the generalizability of our findings and further explore patients’ views about using their real avatars in wepitals to receive care. Moreover, our experiment involved doctor visits in the wepital but did not involve patients staying in the wepital for persistent care. Further work is needed to examine patient satisfaction with persistent care in the wepital.

The IRB approval prohibited the physician from providing the pa tient volunteers with formal diagnoses and prescriptions in our experi ment, disallowing us to assess other important aspects of design success, such as care quality and outcome, which need to be assessed in formal clinical trials in the future once the feasibility and potential of our design are preliminarily evidenced.

Our work forms the first step in creating wepitals and initiates a proposal for docpitals. It opens up avenues for future research, including more advanced prototypes, test bed implementation by hospitals, and more extensive experiments involving patients and physicians from multiple medical disciplines. Future research should explore the policy implications and impacts of the application of our proposal in depth. As prior research has called for the examination of the link between in formation technology and global public health [18], our work could also be extended to the global level. This work also lays a foundation for new avenues of research and theory-building about real avatars as modes of self-identification, self-representation, communication interface, ideal self, or healthy self.

![](/api/attachments/WCY935QN/fulltext/images/c4722348a2cfb2ed46fd3132a2fe5ecf40884d0513c77999180ae152159094a1.jpg)  
The skeleton overlay image by Gettvimages,com, licensed for use  
Fig. 9. Patient Real Avatar with Full Medical Information and Doctor Real Avatar.

Table 1  
Requirements for Successful Implementation of the Proposed Design.

<table><tr><td>1</td><td>Serious investment and commitment from multiple players—the government and tech companies—to build a secure and scalable infrastructure, including the building blocks of weptitals for hospitals</td></tr><tr><td>2</td><td>Hospitals’ willingness to extend their capacities to weptals and admit patient avatars for care</td></tr><tr><td>3</td><td>Creation of standards for data communication to and from real avatars</td></tr><tr><td>4</td><td>Device and sensor makers’ willingness to follow the standards for data communication to patients’ avatars</td></tr><tr><td>5</td><td>The involvement of medical software companies to connect patients’ medical records to avatars and update medical records with data from avatars</td></tr><tr><td>6</td><td>Uniform standards of care for real and robot medical personnel who staff different types of care rooms in weptals with the same rigor as those in hospitals, including no commercial ads</td></tr><tr><td>7</td><td>The involvement of security companies to devise strict data security, communication, access, and storage</td></tr><tr><td>8</td><td>Strictest standards for access to people’s medical records and protection of their privacy</td></tr><tr><td></td><td>Recognizing this need, the federal government (FDA) in its October 2020 certification rule has called for Fast Healthcare Interoperability Resources.17</td></tr><tr><td>9</td><td>A system of drones and delivery vehicles for delivering treatment items to and picking up test samples from mypitals</td></tr><tr><td>10</td><td>The existence of mobile units of nurses and caregivers to provide assistance in mypitals as needed based on a standard of care</td></tr><tr><td>11</td><td>The willingness of Medicare and health insurance companies to cover weptal costs</td></tr><tr><td>12</td><td>Cross-state credentials and licensing boards for medical staff and specialties</td></tr><tr><td>13</td><td>Training of patients and care providers in the handling and use of real avatars</td></tr></table>

<sup>17</sup> The ONC Cures Act Final Rule, About ONC’s Cures Act Final Rule (healthit.gov, accessed in December 2021), supports seamless access, exchange, and use of electronic health information.

## CRediT authorship contribution statement

Fatemeh Mariam Zahedi: Conceptualization, Methodology, Soft ware, Validation, Formal analysis, Investigation, Resources, Data cura tion, Writing – original draft, Writing – review & editing, Visualization,

Supervision, Project administration, Funding acquisition. Huimin Zhao: Software, Validation, Formal analysis, Investigation, Resources, Data curation, Writing – review & editing. Patrick Sanvanson: Inves tigation, Resources, Data curation. Nitin Walia: Software, Resources, Data curation. Hemant Jain: Resources, Writing – review & editing. Reza Shaker: Validation, Resources, Project administration, Funding acquisition.

## Acknowledgement

We thankfully acknowledge the participation of Arash Babai, MD, Robert Siwiek, MD, and Shahryar Ahmed, MD in an earlier data collection process. This research was partly supported by the University of Wisconsin-Milwaukee in its earlier stage and by the John and Jeanne Burnes Grant from the Clinical and Translational Science Institute of Southeast Wisconsin.

## Appendix A

Selected Studies of Virtual Humans in Healthcare.

<table><tr><td>Study</td><td>Subject Area</td><td>Purpose/Method</td><td>Intervention</td><td>Data</td><td>Results</td></tr><tr><td>[3]</td><td>AI-supported virtual health coaches</td><td>Use a data science approach in virtual coaches</td><td>Reducing risks</td><td>-</td><td>Proposes a framework with emphasis on reliability, fairness, engagement, and ethics in data science</td></tr><tr><td>[25]</td><td>Modeling virtual humans</td><td>Perception of virtual humans&#x27; discomfort</td><td>Mechanism to extract image features identifiable as discomfort</td><td>Simulation</td><td>The method achieved 80% accuracy</td></tr><tr><td>[28]</td><td>Relaxation</td><td>Virtual human breathing relaxation</td><td>Virtual human in a virtual world using sensors</td><td>-</td><td>Proposes an architecture for coaching breathing relaxation</td></tr><tr><td>[31]</td><td>Anxiety and relaxation</td><td>Create and assess virtual human interviewer to assess the extent of stress</td><td>Virtual human coach to reduce PTSD</td><td>351 subjects recruited from Craigslist</td><td>Subjects were willing to disclose their inner thoughts to the virtual interviewer</td></tr><tr><td>[35]</td><td>Depression and anxiety</td><td>Design and evaluation of tasks using virtual humans</td><td>Tasks involved mimicking, dyadic interaction, digital (emotion recall and interpretation of Dixit cards) treatment (mindfulness and reading text loud), and psychometric</td><td>56 subjects</td><td>The group using the virtual human did better than the group using text only for tasks</td></tr><tr><td>[51]</td><td>Depression and anxiety</td><td>Use virtual human to administer psychological questionnaires</td><td>Compared the performance of four groups: self-administered, virtual human, face-to-face real humans, and real human in another room</td><td>55 subjects</td><td>Virtual human&#x27;s performance was comparable with others</td></tr><tr><td>[54]</td><td>Mental health diagnosis and clinician training</td><td>Develop the technology for a virtual human health provider and virtual patient</td><td>Patient care and provider training using virtual patient</td><td>Not reported</td><td>Preliminary tests showed positive assessment</td></tr><tr><td>[63]</td><td></td><td></td><td></td><td>24 national guards&#x27; members from war in Afghanistan and</td><td></td></tr></table>

(continued )

<table><tr><td>Study</td><td>Subject Area</td><td>Purpose/Method</td><td>Intervention</td><td>Data</td><td>Results</td></tr><tr><td>[66]</td><td>Mental health, psychological assessment of PTSD Modeling humans in radiology studies</td><td>Use virtual humans for interviews about symptoms to preserve anonymity and increase rapport Review of virtual human models for medical devices studies and simulation</td><td>Mental health assessment using virtual humans and anonymized real humans Review of methods and technologies used in creating virtual human models</td><td>132 active or retired US military service members recruited from Craigslist Review of 29 virtual human models created since 2004 (an updated list from a previous study) and 9 virtual pregnant women</td><td>Virtual human interviewers were effective in inducing more disclosure While the reliance on anatomically specific virtual humans for safety assessment and R&amp;D is on the rise, challenges exist due to the number of human body parts, accuracy of measurements, and justifying their use</td></tr><tr><td>[71]</td><td>Blood flow in virtual humans</td><td>3D macroscopic blood flow on a full human scale using HemeLB—an open-source 3D fluid dynamics tool—for the study of blood flow in virtual humans</td><td>Coding the simultaneous simulation of arterial and venous vascular trees based on human-specific geometries</td><td>Simulation</td><td>Demonstrates that blood flow in humans can be simulated with virtual humans. Visualization remains an important requirement</td></tr><tr><td>[89]</td><td>Mental health, depression</td><td>Use virtual human for diagnosing depressive disorders</td><td>Diagnosis by psychiatrist vs. virtual human</td><td>179 outpatients</td><td>Embodied conversational agent (virtual human) performed equally well in standardized clinical interviews</td></tr><tr><td>[92]</td><td>Mental health</td><td>Review of various uses of virtual humans as healthcare cognitive assistants in medical fields</td><td>Review and categorization of use, trends, challenges, design guidelines, and technologies</td><td>Papers from various domains, including robotics (6), AI (6), cyber-physical systems (12), HCI (9), and smart health (4)</td><td>Virtual humans in the form of healthcare cognitive assistants will play critical roles in healthcare in the near future</td></tr><tr><td>[99]</td><td>Connecting devices in virtual reality in healthcare</td><td>Develop an approach to connect multiple devices in virtual reality</td><td>An approach to connect devices in using virtual reality</td><td>Method development</td><td>Connected devices in virtual reality, with a limitation of 7 devices</td></tr><tr><td>[100]</td><td>Mental health</td><td>SimCoach project to develop virtual human interviewer</td><td>Virtual human interviewer to assist war veterans</td><td>System development to encourage and engage in discussion of mental health issues</td><td>Expected the veterans and service members to take the first step to seek help for mental health issues</td></tr><tr><td>[115]</td><td>Pain assessment</td><td>Differences in pain assessment based on the demographics of patients using virtual human patients</td><td>Pain assessment differences using cues from virtual human patients</td><td>107 healthcare students, 32 virtual human patients with different profiles</td><td>The assessment of pain by healthcare students differed by gender, race, and age of the virtual human patients</td></tr><tr><td>[123]</td><td>Pain assessment</td><td>Differences in pain assessment based on the demographics of patients using virtual human patients</td><td>Studying the differences in pain assessment by patients&#x27; demographics using virtual human patients</td><td>113 nurses and 80 physicians, 32 virtual human patients with different profiles</td><td>The assessment of pain and prescription of opioids differed by patient demographics</td></tr><tr><td>[128]</td><td>Automatic evaluation of mental health providers&#x27; empathetic responses</td><td>Use virtual human patients to identify empathetic responses in mental health and use the data to automatically evaluate the empathetic performance of mental healthcare providers</td><td>Developed virtual human patients, used them to collect data on the providers&#x27; empathetic responses, trained an evaluation process, and then used the automatic evaluation to assess the performance of providers</td><td>Developed two suicidal virtual human patients, collected 1952 empathetic responses to train for automatic evaluation, and then evaluated the performance of 20 mental healthcare providers</td><td>It is possible to capture empathetic responses using virtual human patients and use the data for training and assessment of mental healthcare providers</td></tr><tr><td>[134]</td><td>Cancer and virtual humans</td><td>Use virtual humans to deliver information about collateral cancer to promote patents&#x27; change of behaviors</td><td>Developed virtual humans for the delivery of cancer information</td><td>73 people in a focus group and 1,400 responses to an online survey</td><td>Offers guidelines for designing virtual humans to deliver information to patients</td></tr></table>

## Appendix B

Selected Studies and Review Papers on Wearable Sensors in mHealth.

<table><tr><td>Study</td><td>Subject Area</td><td>Purpose</td><td>Intervention</td><td>Data</td><td>Results</td></tr><tr><td colspan="6">Use of Wearable Sensors for Health Monitoring</td></tr><tr><td>[7]</td><td>Asthma</td><td>Studies on electronic inhaler sensors that track the time, frequency, and location of short-acting b-agonist (SABA) use</td><td>Self-management tool: access to an app that reports the information collected by the sensor</td><td>120 participants: their days with asthma before and after using the self-management tool</td><td>Using the wearable sensors leads to longer periods of asthma-free days.</td></tr><tr><td>[45]</td><td>Real-time patient data monitoring through data analytics</td><td>Proposes a method for sensing emergency, adapting data sensing, and real-time prediction</td><td>Simulation of existing secondary data for assessment</td><td>Secondary data</td><td>The data analytic method reduces energy use by sensors and removes data redundancy</td></tr><tr><td>[36]</td><td>Type 1 diabetes mellitus</td><td></td><td>An ontology-based clinical decision support system</td><td>NA</td><td></td></tr></table>

(continued on next page)

(continued )

<table><tr><td>Study</td><td>Subject Area</td><td>Purpose</td><td>Intervention</td><td>Data</td><td>Results</td></tr><tr><td></td><td></td><td>Proposes an ontology architecture to collect, formalize, integrate, analyze, and manipulate patients&#x27; data</td><td>proposed for monitoring patients</td><td></td><td>Proposes the architecture for an intelligent decision support system to monitor type-1 diabetic patients</td></tr><tr><td>[14]</td><td>Elderly care</td><td>Proposes an architecture for monitoring elderly care</td><td>Discusses an architecture for creating a patient cloud database</td><td>NA</td><td>The system collects elderly patient data and makes the data available in a cloud database</td></tr><tr><td>[15]</td><td>Heart failure</td><td>Develops and validates a self-administered 6-minute-walk mobile app to be used by patients at home for the prediction of heart failure</td><td>Using the wearable sensor at home for the 6-minute walk</td><td>Three phases: n=52, 32, 19, respectively</td><td>The wearable sensor is easy to use and provides accurate measurement</td></tr><tr><td>[109]</td><td>Parkinson&#x27;s disease detection</td><td>Proposes a method for the diagnosis of Parkinson&#x27;s disease using voice data</td><td>Diagnosis</td><td>1000 voice samples</td><td>The method achieves 99% accuracy within one second</td></tr><tr><td>[126]</td><td>Network of patients</td><td>Proposes a technology for creating a cloud network of patients through their wearable sensors</td><td>Creating a network of patients&#x27; wearable sensors</td><td>NA</td><td>A prototype cloud-based network was demonstrated at a conference</td></tr><tr><td colspan="6">Review Papers about Wearable Sensors in Healthcare</td></tr><tr><td>[10]</td><td>mHealth apps</td><td>Reviews mHealth apps in third party-curated (trusted) mHealth app libraries</td><td>Self-management using apps</td><td>18 apps were reviewed</td><td>There are a limited number of such apps, and they need to be extended</td></tr><tr><td>[11]</td><td>Mental health</td><td>Reviews the use of virtual reality in mental health</td><td>Assessment and treatment of mental health</td><td>Published papers</td><td>Virtual reality is useful for the assessment and treatment of various mental health issues, and assessments show that virtual reality creates similar physiological and psychological reactions as those in real environments</td></tr><tr><td>[33]</td><td>Heart failure</td><td>Reviews studies about the use of wearable sensors for detecting heart failure and emerging technologies</td><td>Monitoring heart failure</td><td>Published papers</td><td>Wearables have the potentials to improve care for heart failure. Current studies are only observational. There are needs for more studies, a well-structured payment system, and social change in the use of technology</td></tr><tr><td>[64]</td><td>Insomnia</td><td>Reviews digital solutions for cognitive behavioral therapy for insomnia</td><td>Use of various technologies to improve onset of sleep</td><td>Papers on various technologies used for insomnia treatment</td><td>The use of technologies is helpful in dealing with insomnia at the global level, but challenges need to be addressed</td></tr><tr><td>[65]</td><td>Health monitoring of physiological parameters</td><td>Reviews studies about wearable sensors, categorizes them into different categories of physiological parameters and activities, and reviews studies in textile-based wearables</td><td>Apps for health monitoring</td><td>Published papers</td><td>This comprehensive review shows the wealth of research interest in wearables, and future technologies would increase their use</td></tr><tr><td>[79]</td><td>Cognition</td><td>Reviews using self-administrated wearable sensors for cognitive assessment</td><td>Assessment of the feasibility and psychometric property of self-assessment using wearable sensors</td><td>12 published papers</td><td>There is positive evidence of the feasibility and general support for high levels of between- and within-person reliability and construct validity</td></tr><tr><td>[81]</td><td>Wearable sensors with data exchange possibilities</td><td>Reviews available health monitoring wearables with data exchange possibilities and maps wearables into 13 attributes for data exchange</td><td>Self-management</td><td>Published papers; reports on 362 mobile health monitoring devices</td><td>Few systems have FDA approval, few systems support middleware, only 30% allow users access to source data, and only 16% allow transfer of data from the device</td></tr><tr><td>[87]</td><td>Atrial fibrillation (Afib)</td><td>Reviews studies of using wearable sensors in Afib and divides the published papers into validating Afib wearables and screening with them</td><td>Screening for Afib</td><td>43 studies for validating the detection (28 papers) and screening Afib (15 papers)</td><td>The existing studies indicate that wearables with apps are useful in detecting atrial fibrillation</td></tr><tr><td>[90]</td><td>Mobile apps available in app stores used in healthcare</td><td>Reviews and classifies mobile apps in healthcare and papers on scientific validations</td><td>Various app stores&#x27; mobile apps and their use in healthcare</td><td>Published papers and website sources</td><td>Provides a comprehensive review and classification of app stores&#x27; mobile apps in healthcare</td></tr><tr><td>[102]</td><td>Parkinson&#x27;s disease</td><td>Reviews the use of wearable sensors in Parkinson&#x27;s disease management</td><td>Categorizes the use of wearable sensors: early diagnosis, tremor, body motion analysis, motor fluctuations, and home and long-term monitoring</td><td>Published papers, with 1,429 papers found and 136 evaluated</td><td>Provides a comprehensive review with recommendations and trends in each category of use, as well as discussions of automatic real-time assessment, limitations, and open questions</td></tr><tr><td>[108]</td><td>Wearable sensors in healthcare</td><td>Reviews the state of using wearable sensors in healthcare, covering passive and active wearable sensors for medical use</td><td>Using wearable sensors for tracking and diagnostics</td><td>Published papers, covering emerging technologies, future use, and issues</td><td>Provides a comprehensive review of how wearable sensors are used in healthcare, their positives, negatives, future potentials, and needed safeguards</td></tr><tr><td>[119]</td><td>Hypertension</td><td>Reviews the use of mobile blood pressure cuffs for hypertension</td><td>Self-management</td><td>Published papers</td><td>Patients need to be cautioned about inaccuracies</td></tr></table>

Appendix C. The Meta Design of Real Avatar in Wepital

![](/api/attachments/WCY935QN/fulltext/images/d7d4e6daefab8233f00bd6fe3306e4c82abd67066c1050ecac13f8c9b4f50301.jpg)  
Fig. C.1. Meta Design of Data Flow and Interactions, Figure C.2. Meta Design of Wepital.

## Appendix D. Recruitment and Experiment Protocol

Recruitment. Our IRB approval strictly limited our recruitment to patients with heartburn or similar gastrointestinal (GI) problems at a single clinic. The choice of GI problems was approved because they normally are not acute diseases that may need immediate treatment or hospitalization. Each participant received \$100 after the completion of the experiment and the survey.

The IRB-approved recruitment text specifies the following inclusion and exclusion conditions for the real-avatar case (the non-real-avatar recruitment text does not have information regarding sensors).

\- You have had chronic symptoms of irritable bowel syndrome (IBS) or heartburn (Gastroesophageal Reflux Disease or GERD) for more than a year.

\- You are NOT experiencing unintentional weight loss or difficulty in swallowing.

\- You are NOT experiencing blood in stool.

\- You are NOT experiencing any serious symptoms, such as shortness of breath, wheezing, or cough.

\- You have adequate computer skill in using computers and the Internet and entering text in the chat box.

\- You have no hearing disability that prevents you from using a headset.

\- You have no visual impairment that prevents you from seeing the computer screen.

\- You have sufficient knowledge of the English language for communication (speaking, reading, and writing).

\- You agree to use mHealth sensors to capture your physiological data in order to create your real avatar (under a fictitious name).

\- You are of age 18 or older.

Experiment Protocol. The attending physician was a GI specialist, who followed an IRB-approved script for interactions with patients and asked questions about each patient’s history of symptoms and medications. In the real-avatar case, the physician would click on the patient avatar’s green armband to see the patient’s vital signs (only the physician and patient could see the vital data). The physician held a short one-on-one video visit to visually examine the patient, such as asking the patient to open his/her mouth and bring his/her eye close for examination. The physician provided his opinions and suggestions to each patient at the end of the interaction with the patient. The IRB approval prohibited the physician from giving patient formal diagnoses and prescriptions during the experiment. The physician did not have access to the patients' medical records for this experiment due to HIPAA rules.

Location. As required by the IRB approval, the volunteer patients had to come to the laboratory at one of the two universities to make sure that if there was an emergency during the process, an attending staff member could immediately address it. Each patient attended the experiment in a private office with a knowledgeable attending staff member accessible to ensure the patient’s safety in case of a medical emergency during the visit in the wepital (the attending staff member did not observe the patient during the experiment.)

Steps to Avoid Bias. We had created the avatars and logins for patients in advance. To avoid any bias due to pre-exposure to virtual worlds, online visits, and sensors, all participants received a short training about the wepital and how to use their avatars, video chats, and sensors. All patients in the real-avatar case wore the same types of sensors. To avoid potential bias due to differences in the type of computers and use of sensors, participants came to a location where a separate room was set up for each participant with the same type of equipment.

Data Collection for Two Cases: with and without Real Avatar. Per IRB requirements, participants for the real-avatar and non-real-avatar cases were recruited in two time periods in order to have clarity in recruitment and the technology being used. The data for the non-real-avatar case were collected first. In the recruitment for the real-avatar case, we had nine participants who had also participated in the non-real-avatar case. In order to study the effect of having participated in the non-real-avatar case, we divided the real-avatar sample into two sub-samples: having participated and not having participated in the non-real-avatar experiment. For each item used in the analysis, we performed a two-sample t-test. None of the t-tests showed statistical significance, suggesting that our training had removed any potential bias due to having been exposed to virtual worlds and our experiment without real avatar.

Privacy and Anonymity. The experiment was conducted online in the wepital. Through his avatar, the physician could both speak to each patient avatar and write in the text/chat area seen by all patients. However, to strictly preserve the patients’ privacy, as required by the IRB approval, patients communicated (asked and answered questions) in the chat area only so that no one could possibly identify them by their voices. Patients wore sensors in the real-avatar case, and their vital signs were uploaded to the green armbands of their avatars in real time. For each patient, only the patient and the physician could see the information on the patient avatar’s green armband. The physician examined the patient’s vital signs and provided opinions and suggestions accordingly. All avatars had made-up names, and no one had access to the real identities of the patients except the person in charge of consenting them. As required by the IRB approval, a staff member (located at the same location as the participants) was present in the wepital with his, her avatar without any active participation to provide immediate support in case a patient would need any medical emergency attention.

![](/api/attachments/WCY935QN/fulltext/images/a9f66a690a9d927c16ceef63e2c8fa9654e034716cb28362876a498fe18795f6.jpg)  
Fig. D.1. Zephyr BioHarness and Patient Wearing It.

Video Chats. Each patient had the option of attending a one-on-one video consultation. The technology used for video chat was ustream.tv<sup>16</sup> (later acquired by IBM). The physician briefly interacted with and checked the patient in a video call. After this brief interaction, both would return to the wepital group room.

Technologies. The prototype was built on a land we had acquired on Second Life©. For the real avatar case, the wearable sensors collected vital signs, including heart rate, breathing rate, body temperature, ECG, blood oxygen saturation, and weight, from patients. The sensors included FDA approved BioHarness (by Zephyr), oximeter, and scale. Fig. D.1 shows the BioHarness worn around the chest of a patient.

## Appendix E

Construct Definitions and Main Sources.

<table><tr><td>Construct</td><td>Definition</td><td>Main Sources Used</td></tr><tr><td>Flexibility about method of care</td><td>Having a flexible attitude toward the method of care within a healthcare system</td><td>[12],[131]</td></tr><tr><td>Lack of privacy concern</td><td>The lack of concern about the exposure of one&#x27;s private information in the group office visit in the wepital</td><td>[4],[131]</td></tr><tr><td>Understanding information</td><td>The ability to understand information provided in the office visit in the wepital</td><td>[72],[130],[131]</td></tr><tr><td>Telepresence</td><td>The perception of “being there” in an environment mediated by technology as opposed to “presence” that refers to the perception of natural environment</td><td>[17],[93],[114],[118]</td></tr><tr><td>Time convenience</td><td>Perceived convenience related to time savings in office visits in the wepital</td><td>Developed for this study</td></tr><tr><td>Trust</td><td>Trust in the virtual campus</td><td>[5],[86],[131]</td></tr><tr><td>Satisfaction with physician</td><td>Satisfaction with the physician in the office visit in the wepital</td><td>[72],[88],[130]</td></tr><tr><td>Real avatar</td><td>Having sensor data added to patient avatar, a binary variable, 0 or 1</td><td>Specific to the design in this study</td></tr></table>

## Appendix F

## Instrument\*.

<table><tr><td>Construct</td><td>Code</td><td>Item</td></tr><tr><td rowspan="4">Flexibility about method of care</td><td></td><td>In receiving medical services, my attitude about changing the way I receive medical services can be characterized as</td></tr><tr><td>FlexM1</td><td>Very unfavorable/very favorable</td></tr><tr><td>FlexM2</td><td>Not open at all/very open</td></tr><tr><td>FlexM3</td><td>Not comfortable at all/very comfortable</td></tr><tr><td rowspan="4">Lack of privacy concern</td><td></td><td>My level of concern that health information at the Virtual Medical Office, once shared in a (online) group visit</td></tr><tr><td>Priv1</td><td>Will be abused for sure by other patients/will not be abused by other patients at all</td></tr><tr><td>Priv2</td><td>Will be compromised for sure by other patients/will not be compromised by other patients at all</td></tr><tr><td>Priv3</td><td>Will not be kept confidential by other patients/will be kept confidential by other patients</td></tr><tr><td rowspan="4">Understanding information</td><td></td><td>I believe that the medical information I received at the Virtual Medical Office was</td></tr><tr><td>UndInf1</td><td>Not at all clear in meaning/very clear in meaning</td></tr><tr><td>UndInf2</td><td>Difficult to comprehend/easy to comprehend</td></tr><tr><td>UndInf3</td><td>In general, the understandability of the information was very low/very high</td></tr><tr><td rowspan="4">Telepresence</td><td></td><td>Referring to the Virtual Medical Office I just visited, I believe that</td></tr><tr><td>TelePre1</td><td>Its similarity to visiting a physician office/clinic was very low/very high</td></tr><tr><td>TelePre2</td><td>My feeling of being in the same room with a physician was very low/very high</td></tr><tr><td>TelePre3</td><td>The overall feeling that I visited a physician office was very low/very high</td></tr><tr><td rowspan="4">Time convenience</td><td></td><td>Compared with my past experiences of using traditional medical services, I believe using the Virtual Medical Office I just visited</td></tr><tr><td>TConv1</td><td>Increased the time spent at physician&#x27;s office/reduced the time spent at physician&#x27;s office</td></tr><tr><td>TConv2</td><td>Increased the travel time to the physician&#x27;s office/reduced the travel time to the physician&#x27;s office</td></tr><tr><td>TConv3</td><td>Was slower in providing service/was faster in providing service</td></tr><tr><td rowspan="4">Trust</td><td></td><td>In receiving medical services through the Virtual Medical Office, I believe that the office</td></tr><tr><td>Trust1</td><td>Cares only about its own interest/cares about patients&#x27; interest</td></tr><tr><td>Trust2</td><td>Has no integrity/has a great deal of integrity</td></tr><tr><td>Trust3</td><td>Is not capable at all/is very capable</td></tr><tr><td rowspan="4">Satisfaction with physician</td><td></td><td>My feeling about my experience with the physician at the Virtual Medical Office could be characterized as:</td></tr><tr><td>PhSatis1</td><td>Not satisfactory at all/very satisfactory</td></tr><tr><td>PhSatis2</td><td>Not pleased at all/very pleased</td></tr><tr><td>PhSatis3</td><td>Very negative/very positive</td></tr></table>

\*We used the term “virtual medical office” to avoid the need to describe what a wepital is.

## Appendix G. Participants’ Demographics

The number of female participants was twice that of male participants. The mode of age in our sample was 56–60 years. About half of the par ticipants had an undergraduate degree.

![](/api/attachments/WCY935QN/fulltext/images/b5270e773945cd97cfa60c92b2019c16a07eeca27296dd661d2c0deaaa728fc1.jpg)

![](/api/attachments/WCY935QN/fulltext/images/cb21d42f24c5a7059328089c7b642f89909ea4db1677a3cbdfff41c9c112f857.jpg)

![](/api/attachments/WCY935QN/fulltext/images/244d22a89bea35d6b48ddbe0c522de6b505781fc9ae1703a6f73794b8644bd07.jpg)

## Appendix H

Exploratory Factor Analysis.

<table><tr><td>Constructs on Level 1</td><td>Item</td><td>1</td><td>2</td><td>3</td></tr><tr><td rowspan="3">1. Flexibility about method of care</td><td>FlexM1</td><td>0.094</td><td>-0.926</td><td>-0.125</td></tr><tr><td>FlexM2</td><td>0.202</td><td>-0.918</td><td>-0.186</td></tr><tr><td>FlexM3</td><td>0.240</td><td>-0.894</td><td>-0.237</td></tr><tr><td rowspan="3">2. Lack of privacy concern</td><td>Priv1</td><td>0.932</td><td>-0.170</td><td>-0.261</td></tr><tr><td>Priv2</td><td>0.932</td><td>-0.174</td><td>-0.275</td></tr><tr><td>Priv3</td><td>0.912</td><td>-0.207</td><td>-0.196</td></tr><tr><td rowspan="3">3. Understanding information</td><td>UndInf1</td><td>0.207</td><td>-0.243</td><td>-0.901</td></tr><tr><td>UndInf2</td><td>0.192</td><td>-0.242</td><td>-0.921</td></tr><tr><td>UndInf3</td><td>0.348</td><td>-0.086</td><td>-0.880</td></tr><tr><td>Cumulative variance explained (Level 1)</td><td></td><td>0.320</td><td>0.623</td><td>0.926</td></tr><tr><td>Constructs on Level 2</td><td></td><td>3</td><td>4</td><td>5</td></tr><tr><td rowspan="3">4. Telepresence</td><td>TelePre1</td><td>0.945</td><td>-0.119</td><td>-0.186</td></tr><tr><td>TelePre2</td><td>0.910</td><td>-0.239</td><td>-0.216</td></tr><tr><td>TelePre3</td><td>0.927</td><td>-0.226</td><td>-0.232</td></tr><tr><td rowspan="4">5. Time convenience</td><td>TConv1</td><td>0.185</td><td>-0.179</td><td>-0.907</td></tr><tr><td>TConv2</td><td>0.366</td><td>-0.319</td><td>-0.806</td></tr><tr><td>TConv3</td><td>0.178</td><td>-0.401</td><td>-0.870</td></tr><tr><td>Trust1</td><td>0.121</td><td>-0.897</td><td>-0.297</td></tr><tr><td rowspan="2">6. Trust</td><td>Trust2</td><td>0.179</td><td>-0.905</td><td>-0.268</td></tr><tr><td>Trust3</td><td>0.323</td><td>-0.878</td><td>-0.236</td></tr><tr><td>Cumulative variance explained (Level 2)</td><td></td><td>0.326</td><td>0.639</td><td>0.926</td></tr><tr><td>Constructs on Level 3</td><td></td><td>7</td><td></td><td></td></tr><tr><td rowspan="3">7. Satisfaction with physician</td><td>PhSatis1</td><td>0.979</td><td></td><td></td></tr><tr><td>PhSatis2</td><td>0.983</td><td></td><td></td></tr><tr><td>PhSatis3</td><td>0.954</td><td></td><td></td></tr><tr><td>Cumulative variance explained (Level 3)</td><td></td><td>0.945</td><td></td><td></td></tr></table>

## Appendix I. Construct Reliability and Validity Checks

We checked the reliability of the constructs in three ways, as reported in Table I.1. We computed Cronbach alpha values, which were all above the 0.70 acceptable threshold [83]. Composite factor reliability (CFR) values were above the 0.70 acceptable threshold [104]. Average variance extracted (AVE) values were above the acceptable threshold 0.50 [104]. As an additional check on discriminant validity, we computed the square root of AVE for each construct and compared it with the construct’s correlations with other constructs [37]. For each construct, the square root of AVE was desirably greater than the correlation values (Table I.2). These checks provided support for the reliability and validity of the measured constructs.

Table I.1  
Construct Reliability Checks.

<table><tr><td>Construct</td><td>Cronbach&#x27;s α</td><td>AVE</td><td>CFR</td></tr><tr><td>Flexibility about method of care</td><td>0.938</td><td>0.853</td><td>0.945</td></tr><tr><td>Lack of privacy concern</td><td>0.974</td><td>0.927</td><td>0.974</td></tr><tr><td>Understanding information</td><td>0.942</td><td>0.865</td><td>0.952</td></tr><tr><td>Telepresence</td><td>0.970</td><td>0.917</td><td>0.971</td></tr><tr><td>Time convenience</td><td>0.938</td><td>0.843</td><td>0.941</td></tr><tr><td>Trust</td><td>0.950</td><td>0.921</td><td>0.972</td></tr><tr><td>Satisfaction with physician</td><td>0.971</td><td>0.871</td><td>0.951</td></tr></table>

Table I.2  
Construct Correlations and Comparison with Square Root of AVEs.

<table><tr><td>Construct</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>1. Flexibility about method of care</td><td>0.853</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2. Lack of privacy concern</td><td>0.419</td><td>0.927</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3. Understanding information</td><td>0.468</td><td>0.517</td><td>0.865</td><td></td><td></td><td></td><td></td></tr><tr><td>4. Telepresence</td><td>0.674</td><td>0.127</td><td>0.312</td><td>0.917</td><td></td><td></td><td></td></tr><tr><td>5. Time convenience</td><td>0.593</td><td>0.466</td><td>0.461</td><td>0.489</td><td>0.843</td><td></td><td></td></tr><tr><td>6. Trust</td><td>0.576</td><td>0.500</td><td>0.809</td><td>0.499</td><td>0.663</td><td>0.921</td><td></td></tr><tr><td>7. Satisfaction with physician</td><td>0.778</td><td>0.449</td><td>0.620</td><td>0.736</td><td>0.769</td><td>0.791</td><td>0.871</td></tr></table>

\*The square root values of the AVEs are in boldface on the diagonal.

Appendix J

Fit Indices for the Measurement Model and Wepital Patient Satisfaction Model.

<table><tr><td>Fit Index</td><td>Measurement Model</td><td>Model</td><td>Threshold*</td></tr><tr><td>Normed  $\chi^{2}$ </td><td>1.551</td><td>1.581</td><td>&lt;3</td></tr><tr><td>CFI (Comparative Fit Index)</td><td>0.945</td><td>0.932</td><td>&gt;0.90</td></tr><tr><td>TLI (Tucker-Lewis Index)</td><td>0.932</td><td>0.921</td><td>&gt;0.90</td></tr><tr><td>SRMR (Standardized Root Mean Square Residual)</td><td>0.055</td><td>0.091</td><td>&lt;0.08</td></tr></table>

Sources: [49],[80].

Appendix K

Confirmatory Factor Analysis-the Measurement Model.

<table><tr><td>Item</td><td>Loading</td><td>t-value</td><td> $R^2$ </td></tr><tr><td>FlexM1</td><td>0.900</td><td>31.041</td><td>0.810</td></tr><tr><td>FlexM2</td><td>0.938</td><td>51.799</td><td>0.879</td></tr><tr><td>FlexM3</td><td>0.932</td><td>38.390</td><td>0.868</td></tr><tr><td>Priv1</td><td>0.984</td><td>189.223</td><td>0.968</td></tr><tr><td>Priv2</td><td>0.998</td><td>399.954</td><td>0.996</td></tr><tr><td>Priv3</td><td>0.904</td><td>37.648</td><td>0.817</td></tr><tr><td>UndInf1</td><td>0.927</td><td>55.534</td><td>0.824</td></tr><tr><td>UndInf2</td><td>0.972</td><td>63.753</td><td>0.888</td></tr><tr><td>UndInf3</td><td>0.890</td><td>26.588</td><td>0.900</td></tr><tr><td>TelePre1</td><td>0.939</td><td>68.724</td><td>0.882</td></tr><tr><td>TelePre2</td><td>0.944</td><td>78.206</td><td>0.891</td></tr><tr><td>TelePre3</td><td>0.989</td><td>150.035</td><td>0.978</td></tr><tr><td>TConv1</td><td>0.857</td><td>19.225</td><td>0.735</td></tr><tr><td>TConv2</td><td>0.907</td><td>34.805</td><td>0.823</td></tr><tr><td>TConv3</td><td>0.986</td><td>82.029</td><td>0.972</td></tr><tr><td>Trust1</td><td>0.980</td><td>76.478</td><td>0.960</td></tr><tr><td>Trust2</td><td>0.985</td><td>191.506</td><td>0.971</td></tr><tr><td>Trust3</td><td>0.913</td><td>44.188</td><td>0.834</td></tr><tr><td>PhSatis1</td><td>0.908</td><td>30.692</td><td>0.860</td></tr><tr><td>PhSatis2</td><td>0.942</td><td>46.399</td><td>0.944</td></tr><tr><td>PhSatis3</td><td>0.949</td><td>54.711</td><td>0.792</td></tr></table>

## References

[11 G. Aali. T. Kariotis. F. Shokraneh. Avatar Therapy for People with Schizophrenia or Related Disorders. Cochrane Database of Systematic Reviews 5 (2020)

[2] T. Asparauhov, B. Muth´en, 2018. SRMR in Mplus. https://www.statmodel.com download/SRMR2.pdf, downloaded February 2021.

[3] S. Baee, M. Rucker, A. Baglione, M.K. Ameko, L. Barnes, A Framework for Addressing the Risks and Opportunities Al-Supported Virtual Health Coaches, in: Proceedings of the 14th EAI International Conference on Pervasive Computing Technologies for Healthcare, 2020, pp. 251–254. May.

[4] G. Bansal, F.M. Zahedi, D. Gefen, The Impact of Personal Dispositions on Information Sensitivity, Privacy Concern and Trust in Disclosing Health Information Online, Decision Support Systems 49 (2010) 138–150.

[5] G. Bansal, F.M. Zahedi, D. Gefen, Do Context and Personality Matter? Trust and Privacy Concerns in Disclosing Private Information Online. Information & Management 53 (1) (2016) 1–21.

[6] C. Bao, I.R. Bardhan, H. Singh, B.A. Meyer, K. Kirksey, Patient–Provider Engagement and its Impact on Health Outcomes: A Longitudinal Study of Patient Portal Use, MIS Quarterly 44 (2) (2020) 699–723.

[7] M.A. Barrett. O. Humblet, J.E. Marcus, K. Henderson, T. Smith. N.J. Eid. W. Sublett, et al., Effect of a Mobile Health, Sensor-driven Asthma Management Platform on Asthma Control, Annals of Allergy, Asthma & Immunology 119 (5) (2017) 415–421

[8] E.Z. Barsom, T.M. Feenstra, W.A. Bemelman, J.H. Bonjer, M.P. Schijven, Coping with COVID-19: Scaling up Virtual Care to Standard Practice, Nature Medicine 26 (5) (2020) 632–634.

[9] E. Batbaatar, J. Dorjdagva, A. Luvsannyam, M.M. Savino, P. Amenta, Determinants of Patient Satisfaction: A Systematic Review Perspectives in Public Health 137 (2) (2017) 89–101

[10] C. Baxter, J.A. Carroll, B. Keogh, C. Vandelanotte, Assessment of Mobile Health Apps Using Built-in Smartphone Sensors for Diagnosis and Treatment: Systematic Survey of Apps Listed in International Curated Health App Libraries, JMIR mHealth and uHealth 8 (2) (2020) e16741.

[11] I.H. Bell, J. Nicholas, M. Alvarez-Jimenez, A. Thompson, L. Valmaggia, Virtual Reality as a Clinical Tool in Mental Health Research and Practice, Dialogues in Clinical Neuroscience 22 (2) (2020) 169–177.

[12] A. Bhattacherjee, N. Hikmet, Physicians’ Resistance Toward Healthcare Information Technology: A Theoretical Model and Empirical Test, European

[13] A. Bokolo. Use of Telemedicine and Virtual Care for Remote Treatment ir Response to COVID-19 Pandemic, Journal of Medical Systems 44 (7) (2020) 1–9

[14] H. Boudra. A. Obaid. A.M. Amia. An Intelligent Medical Monitoring System Based on Sensors and Wireless Sensor Network, in: IEEE 2014 International Conference on Advances in Computing, Communications, and Informatics (ICACCI), 2014, pp. 1650–1656.

[15] G.C. Brooks, E. Vittinghoff, S. Iyer, D. Tandon, P. Kuhar, K.M. Madsen, G. M. Marcus, M.J. Pletcher, J.E. Olgin, Accuracy and Usability of a Self-Administered 6-Minute Walk Test Smartphone Application, Circulation: Heart Failure 8 (5) (2015) 905–913.

[16] D. Burden, M. Savin-Baden, Virtual Humans: Today and Tomorrow, Chapman and Hall/CRC. 2019.

[17] K. Burke, Chidambaram, How Much Bandwidth is Enough? A Longitudina Examination of Media Characteristics and Group Outcomes, MIS Quarterly 23 (4) (1999) 557–579

[18] B. Cabieses, G. Faba, M. Espinoza, G. Santorelli, The Link Between Information and Communication Technologies and Global Public Health: Pushing Forward, Telemedicine and e-Health 19 (11) (2013) 879–887.

[19] S. Chandra, M. Mohammadnezhad, P. Ward, Trust and Communication in a Doctor-Patient Relationship: A Literature Review. Journal of Healthcare Communications 3 (3) (2018) 1–6, 36.

[20] A. Chemero, An Outline of a Theory of Affordances, Ecological Psychology 15 (2) (2003) 181–195.

[21] Y. Chen, F.M. Zahedi, A. Abbasi, D. Dobolyi, Trust Calibration of Automated Security IT Artifacts: A Multi-Domain Study of Phishing-Website Detection Tools Information & Management 58 (1) (2021). Article 103394.

[22] W.W. Chin, N. Johnson, A. Schwarz, A Fast Form Approach to Measuring Technology Acceptance and Other Constructs. MIS Ouarterly 32 (4) (2008 687-703.

[23] C. Cipolat, M. Geiges, The History of Telemedicine, in: G. Burg (Ed.), Telemedicine and Teledermatology. Karger, New York, NY. 2003, pp. 6–11.

[24] R.L. Daft, R.H. Lengel, Organizational Information Requirements, Media Richness and Structural Design, Management Science 32 (5) (1986) 554–571.

[25] G.P. Dal Molin. E.M. Nomura. B.M. Dalmoro. F.D.A. Victor, S.R. Musse, Can We Estimate the Perceived Comfort of Virtual Human Faces using Visual Cues?, in:

2021 IEEE 15th International Conference on Semantic Computing, 2021, pp. 366–369. January.

[26] B. Damer, S. DiPaola, J. Paniaras, K. Parsons, B. Roel, M. Ma, Putting a Human Face on Cyberspace (Panel) Designing Avatars and the Virtual Worlds They Live in, in: Proceedings of the 24th Annual Conference on Computer Graphics and Interactive Techniques, 1997, pp. 462–464. August.

[27] B. Damer, J. Judson, J. Dove, S. Illustrator-DiPaola, A. Illustrator-Ebtekar, S. Illustrator-McGehee. Avatars! Exploring and Building Virtual Worlds on the Internet, Designed By-Walker, R. and Produced By-Reber, K, , Peachpit Press, 1997.

[28] S. Dar, V. Lush, U. Bernardet, The Virtual Human Breathing Relaxation System, in: The 5th Experiment International Conference, 2019, pp. 276–277. June.

[29] W.H. DeLone, E.R. McLean, The DeLone and McLean model of Information Systems Success: a Ten-year Update, Journal of Management Information Systems 19 (4) (2003) 9–30.

[30] A.R. Dennis, R.M.; Fuller, J.S. Valacich, Media, Tasks, and Communication Processes: A Theory of Media Synchronicity, MIS Ouarterly 32 (3) (2008) 575–600.

[31] D. DeVault, R. Artstein, G. Benn, T. Dey, E. Fast, A. Gainer, K. Georgila, J. Gratch, A Hartholt M Lhommet G Lucas SimSensei Kiosk: A Virtual Human Interviewer for Healthcare Decision Support, in: Proceedings of the 2014 International Conference on Autonomous Agents and Multi-Agent Systems, International Foundation for Autonomous Agents and Multiagent Systems (www. ifaamas.org), 2014, pp. 1061–1068. May.

[32] J.E. DeVoe, L.S. Wallace, G.E. Fryer Jr., Measuring Patients’ Perceptions of Communication with Healthcare Providers: Do Differences in Demographic and Socioeconomic Characteristics Matter? Health Expectations 12 (1) (2009) 70–80.

[33] A.D. DeVore, J. Wosik, A.F. Hernandez, The Future of Wearables in Heart Failure Patients, JACC: Heart Failure 7 (11) (2019) 922–932.

[34] A. Egan, Seeing and Believing: Perception, Belief Formation and the Divided Mind. Philosophical Studies 140 (1) (2008) 47–63.

[35] J.O. Egede, D. Price, D.B. Krishnan, S. Jaiswal, N. Elliott, R. Morriss, M.J.G. Trigo, N. Nixon, P. Liddle, C. Greenhalgh, M. Valstar, Design and Evaluation of Virtual Human Mediated Tasks for Assessment of Depression and Anxiety, in: Proceedings of the 21st ACM International Conference on Intelligent Virtual Agents, 2021, pp. 52–59. September.

[36] S. El-Sappagh, F. Ali, A. Hendawi, J-H. Jang, K-S. Kwak, A mobile Health Monitoring-and-Treatment System Based on Integration of the SSN Sensor Ontology and the HL7 FHIR Standard, BMC Medical Informatics and Decision Making 19 (1) (2019) 1–36.

[37] C. Fornell, D.F. Larcker, Evaluating Structural Equation Models with Unobservable Variables and Measurement Error. Journal of Marketing Research 18 (1) (1981) 39–50

[39] D. Gefen, E.; Karahanna, D.W. Straub, Trust and TAM in Online Shopping: An Integrated Model. MIS quarterly 27 (1) (2003) 51–90.

[40] D. Gefen, E.E. Rigdon. D. Straub. An Update and Extension to SEM Guidelines for Administrative and Social Science Research, MIS Quarterly 35 (2) (2011) iii–xiv.

[38] J.C. Fortney, J.F. Burgess, H.B. Bosworth, B.M. Booth, P.J. Kaboli, A Reconceptualization of Access for 21st Century Healthcare. Journal of General Internal Medicine 26 (2) (2011) 639.

[41] J.J. Gibson, The Senses Considered as Perceptual Systems, George Allen & Unwin LTD, London, 1966.

[42] J.J. Gibson. The Theory of Affordances. In Perceiving, Acting, and Knowing: Toward an Ecological Psychology. Lawrence Erlbaum Associates, Hillsdale. N.J. 1977. pp. 67–82.

[43] S. Gregor, A.R. Hevner, Positioning and Presenting Design science Research fo Maximum Impact, MIS Quarterly 37 (2) (2013) 337–355.

[44] A. Gupta, K. Scott, M. Dukewich, Innovative Technology Using Virtual Reality in the Treatment of Pain: Does it Reduce Pain via Distraction, or is There More to it?

[45] H. Harb, A. Mansour, A. Nasser, E.M. Cruz, I.T. de la Diez, A Sensor-based Data Analytics for Patient Monitoring in Connected Healthcare Applications JFEF Sensors Journal 21 (2) (2020) 974–984.

[46] A.R. Hevner, A Three Cycle View of Design Science Research, Scandinavian Journal of Information Systems 19 (2) (2007) 87–92.

[47] A.R. Hevner, S.T. March, J. Park, S. Ram, Design Science in Information Systems Research, MIS Quarterly 28 (1) (2004) 75–105.

[48] M. Horne, A. Hill, H. Ugail, T. Murrells, M. Hardy, Using Personalised Avatars in a Weight Loss Management Programme: Participants’ Perspectives, European Journal of Public Health 30 (Supplement 5) (2020), https://doi.org/10.1093/ eurpub/ckaa166.036 ckaa166.036.

[49] L. Hu, P.M. Bentler, Cut-Off Criteria for Fit Indexes in Covariance Matrix Analysis: Conventional Criteria versus New Alternatives, Structural Equation Modeling 6 (1) (1999) 1–55.

[50] E. Hutchings, M. Loomes. P. Butow. E.M. Bovle. A Systematic Literature Review of Health Consumer Attitudes towards Secondary Use and Sharing of Health Administrative and Clinical Trial Data: A Focus on Privacy, Trust, and Transparency. Systematic Reviews 9 (1) (2020) 1–41.

[51] S. Jaiswal, M. Valstar. K. Kusumam. C. Greenhalgh. Virtual Human Ouestionnaire for Analysis Of Depression. Anxiety and Personality, in: Proceedings of the 19th ACM International Conference on Intelligent Virtual Agents, 2019, pp. 81–87 July.

[52] K.S. Jones, What is an Affordance? Ecological Psychology 15 (2) (2003) 107–114.

[53] B.E. Kahn. M.U. Kalwani, D.G. Morrison, Measuring Variety-Seeking and Reinforcement Behaviors Using Panel Data, Journal of Marketing Research 23 (2) (1986) 89–100.

[54] P. Kenny, T. Parsons, J. Gratch, A. Rizzo, Virtual Humans for Assisted Health Care, in: Proceedings of the 1st International Conference on Pervasive Technologies Related to Assistive Environments, 2008, pp. 1–4. July.

[55] S. Khairat, C. Meng, Y. Xu, B. Edson, R. Gianforcaro, Interpreting COVID-19 and Virtual Care Trends: Cohort Study, JMIR Public Health and Surveillance 6 (2) (2020) e18811.

[56] H.S. Kim, A. Drolet, Choice and Self-Expression: A Cultural Analysis of Variety Seeking, Journal of Personality and Social Psychology 85 (2) (2003) 373–382.

[57] N. Kock, Media Richness or Media Naturalness? The Evolution of Our Biological Communication Apparatus and Its Influence on Our Behavior Toward E Communication Tools, IEEE Transactions on Professional Communication 48 (2) (2005) 117–130.

[58] N. Kock, Information Systems Theorizing Based on Evolutionary Psychology: An Interdisciplinary Review and Theory Integration Framework, MIS Quarterly 33 (2) (2009) 395–418

[59] N. Kock, V. Garza, Media Naturalness Reduction and Compensatory Channel Expansion: A Study of Online and Face-To-Face Sections of the Same Course. System and Technology Advancements in Distance Learning, IGI Global, 2013 pp. 112–123.

[60] M. Kocur, P. Schauhuber, V. Schwind, C. Wolff, N. Henze, The Effects of Self-and External Perception of Avatars on Cognitive Task Performance in Virtual Reality, in: 26<sup>th</sup> ACM Symposium on Virtual Reality Software and Technology, 2020, pp. 1–11. November.

[61] E-J. Lee, J. Park, Enhancing Virtual Presence in E-Tail: Dynamics of Cue Multiplicity, International Journal of Electronic Commerce 18 (4) (2014) 117–146.

[62] K. Lewin, Frontiers in Group Dynamics: I. Concept, Method, and Reality in Social Sciences, Social Equilibria, and Social Change, Human Relations 1 (5) (1947) 5–41.

[63] G.M. Lucas, A. Rizzo, J. Gratch, S. Scherer, G. Stratou, J. Boberg, L.P. Morency, Reporting Mental Health Symptoms: Breaking Down Barriers to Care with Virtual Human Interviewers, Frontiers in Robotics and AI (2017), https://doi.org/ 10.3389/frobt.2017.00051. October 12.

[64] A.I. Luik, S.D. Kyle, C.A. Espie, Digital Cognitive Behavioral Therapy (dCBT) for Insomnia: A State-of-the-Science Review, Current Sleep Medicine Reports 3 (2) (2017) 48–56.

[65] S. Majumder, T. Mondal, M.J. Deen, Wearable Sensors for Remote Health Monitoring, Sensors 17 (1) (2017) 1–45, article #130.

[66] S.N. Makarov, G.M. Noetscher, J. Yanamadala, M.W. Piazza, S. Louie, A. Prokop, A. Nazarian, A. Nummenmaa, Virtual Human Models for Electromagnetic Studies and their Applications, IEEE Reviews in Biomedical Engineering 10 (2017)

[67] J. Mann, The Medical Avatar and its Role in Neurorehabilitation and Neuroplasticity: A Review. Neurorehabilitation Journal 46 (4) (2020) 467–482

[68] M.L, Markus, M.S. Silver. A foundation for the study of IT effects: A New Look at Desanctis and Poole's Concepts of Structural Features and Spirit Journal of the Association for Information Systems 9 (10/11) (2008) 609–632

[69] R.C. Mayer, J.H. Davis, F.D. Schoorman, An Integrative Model of Organizational Trust. Academy of Management Review 20 (3) (1995) 709–734.

[70] L. McAlister, E. Pessemier, Variety Seeking Behavior: An Interdisciplinary Review, Journal of Consumer Research 9 (3) (1982) 311–322

[71] J.W. McCullough, R.A. Richardson, A. Patronis, R. Halver, R. Marshall M. Ruefenacht, B.J. Wylie, T. Odaker, M. Wiedemann, B. Lloyd, E. Neufeld, Interface Focus 11 (1) (2021), 20190119.

[72] V. McKinney, K. Yoon, F.M. Zahedi, The Measurement of Web-Customer Satisfaction: An Expectation and Disconfirmation Approach, Information Systems Research 13 (3) (2002) 296–315

[73] A. Mehrotra, The Convenience Revolution for Treatment of Low-Acuity Conditions, Journal of the American Medical Association 310 (1) (2013) 35–36.

[74] A. Menychtas, D. Papadimatos, P. Tsanakas, I. Maglogiannis, On the Integration of Wearable Sensors in IoT Enabled mHealth and Quantified-self Applications. Interactive Mobile Communication, Technologies and Learning, Springer, Cham, 2017, pp. 77–88.

[75] P.R. Messinger, X. Ge, K. Smirnov, E. Stroulia, K. Lyons, Reflections of the Extended Self: Visual Self-Representation in Avatar-Mediated Environments, Journal of Business Research 100 (2019) 531–546

[76] E. Miller, D. Polson, Apps, Avatars, and Robots: The future of Mental Healthcare,

[77] M. Minsky, Telepresence, Omni (1980) 45–51. June.

[78] K. Mohajeri, M. Mesgari, A.S. Lee, When Statistical Significance is not Enough: Investigating Relevance, Practical Significance, and Statistical Significance, MIS Quarterly 44 (2) (2020) 525–559.

[79] R.C. Moore, J. Swendsen, C.A. Depp, Applications for Self-Administered Mobile Cognitive Assessments in Clinical Research: A Systematic Review, Internationa Journal of Methods in Psychiatric Research 26 (4) (2017) 1–12, e1562.

[80] B.O. Muth´en, L. Muth´en, The Comprehensive Modeling Program for Applied Researchers User Guide. Muthén and Muthén, Los Angeles. 2003, p. 68

[81] M. Muzny, A. Henriksen, A. Giordanengo, J. Muzik, A. Grøttland, H. Blixgård. G. Hartvigsen. E. Arsand. Wearable Sensors with Possibilities for Data Exchange: Analyzing Status and Needs of Different Actors in Mobile Health Monitoring Systems, International Journal of Medical Informatics 133 (2020) 1–8, 104017.

[82] F.F.H. Nah, B. Eschenbrenner, D. DeWester, Enhancing Brand Equity through Elow and Telepresence: A Comparison of 2D and 3D Virtual Worlds MIS Ouarterly 35 (3) (2011) 731–747.

[83] J.C. Nunnally, I.H. Bernstein, Psychometric Theory, 2nd ed., McGraw Hill, New York, 1978.

[84] J.F. Orlando, M. Beard, S. Kumar, Systematic Review of Patient and Caregivers Satisfaction with Telehealth Videoconferencing as a Mode of Service Delivery in Managing Patients’ Health, PLOS ONE 14 (8) (2019), e0221848.

[85] C. Pagliari, D. Sloan, P. Gregor, F. Sullivan, D. Detmer, J.P. Kahan, W. Oortwijn, S. MacGillivray, What is eHealth (4): A Scoping Exercise to Map the Field, Journal of Medical Internet Research 7 (1) (2005) e9.

[86] P.A. Pavlou, D. Gefen, Building Effective Online Marketplaces with Institution-Based Trust. Information Systems Research 15 (1) (2004) 27–53.

[87] C.R.L. Perales, C. Ruben, H.GC. Van Spall, S. Maeda, A. Jimenez, D.C. Lat¸cu, A. Milman, F. Kirakoya-Samadoulougou, M.A. Mamas, D. Muser, R.C. Arroyo, Mobile Health Applications for the Detection of Atrial Fibrillation: A Systematic Review, EP Europace 23 (1) (2021) 11–28.

[88] S. Petter, W. DeLone, E.R. McLean, Information systems success: The Quest for the Independent Variables, Journal of Management Information Systems 29 (4) (2013) 7–62.

[89] P. Philip, J.A. Micoulaud-Franchi, P. Sagaspe, E.D. Sevin, J. Olive, S. Bioulac, A. Sauteraud, Virtual Human as a New Diagnostic Tool: A Proof of Concept Study in the Field of Major Depressive Disorders, Scientific Reports 7 (1) (2017) 1–7.

[90] I.M. Pires, G. Marques, N.M. Garcia, F. Florez-Revuelta, ´ V. Ponciano, S. Oniani, A Research on the Classification and Applicability of the Mobile Health Applications, Journal of Personalized Medicine 10 (1) (2020) 1–30, article # 11.

[91] P.M. Podsakoff, S.B. MacKenzie, J-Y. Lee, N.P. Podsakoff, Common Method Biases in Behavioral Research: A Critical Review of the Literature and Recommended Remedies, Journal of Applied Psychology 88 (5) (2003) 879–903.

[92] S.M. Preum, S. Munir, M. Ma, M.S. Yasar, D.J. Stone, R. Williams, H. Alemzadeh, J.A. Stankovic, A Review of Cognitive Assistants for Healthcare: Trends, Prospects, and Future Directions, ACM Computing Surveys 53 (6) (2021) 1–37.

[93] L. Qui, I. Benbasat, An Investigation into the Effects of Text to Speech Voice and 3D Avatars on the Perception of Presence and Flow of Live Help in Electronic Commerce, ACM Transactions on Computer Human Interaction 12 (4) (2o05) 329–355.

[94] R.K. Ratner, B.E. Kahn, The Impact of Private versus Public Consumption on Variety-Seeking Behavior, Journal of Consumer Research 29 (2) (2002) 246–257.

[95] K. Ravvaz, J.A. Weissert, C.T. Ruff, C.L. Chi, P.J. Tonellato, Personalized Anticoagulation: Optimizing Warfarin Management using Genetics and Simulated Clinical Trials, Circulation: Cardiovascular Genetics 10 (6) (2017), e001804.

[96] A. Reddy, E. Gunnink, S.A. Deeds, S.L. Hagan, L. Heyworth, T.F. Mattras, K. M. Nelson, A Rapid Mobilization of ‘Virtual’ Primary Care Services in Response to COVID-19 at Veterans Health Administration, Healthcare 8 (4) (2020), 100464.

[97] T. Regia-Corte, M. Marchal, G. Cirio, A. L´ecuyer, Perceiving Affordances in Virtual Reality: Influence of Person and Environmental Properties in Perception of Standing on Virtual Grounds. Virtual Reality 17 (1) (2013) 17–28.

[98] M. Rheu, Y. Jang, W. Peng, Enhancing Healthy Behaviors through Virtual Self: A Systematic Review of Health Interventions using Avatars, Games for Health Journal 9 (2) (2020) 85–94.

[99] E.H. Ribeiro. M. de Paiva Guimarães, J.R.F. Brega. A.F. Brandão. D.R. Colombo Dias. Biomechanics Sensor Nodes for Body Tracking: A Development Solution for Virtual Reality Interaction, in: Symposium on Virtual and Augmented Reality, 2021, pp. 120–126. October.

[100] A.A. Rizzo, B. Lange, J.G. Buckwalter, E. Forbell, J. Kim, K. Sagae, J. Williams, B. O. Rothbaum, J. Difede, G. Reger, T. Parsons, et al., An Intelligent Virtual Human System for Providing Healthcare Information and Support, in: J.D. Westwood, et al. (Eds.). Medicine Meets Virtual Reality, IOS Press, 2011, pp. 503–509.

[101] D. Romanow, A. Rai, M. Keil, CPOE-enabled Coordination: Appropriation for Deep Structure Use and Impacts on Patient Outcomes, MIS Quarterly 42 (1) (2018).189–212

[102] E. Rovini, C. Maremmani, F. Cavallo, How Wearable Sensors Can Support Parkinson's Disease Diagnosis and Treatment: A Systematic Review. Frontiers in

[103] L.H. Schwamm, J. Estrada, A. Erskine, A. Licurse, Virtual Care: New Models of Caring for our Patients and Workforce, The Lancet Digital Health 2 (6) (2020) e282–e285.

[104] A.H. Segars, Assessing the Unidimensionality f Measurement: A Paradigm and Illustration within the Context of Information Systems Research, Omega 25 (1) (1997) 107–121.

[105] J. Sevilla, J. Lu, B.E. Kahn, Variety Seeking, Satiation, and Maximizing Enjoyment over Time, Journal of Consumer Psychology 29 (1) (2019) 89–103.

[106] S. Shafi, S. Manzoor, N. Kaushik. Distraction using Virtual Reality Technology: A Review. International Journal of Advanced Research 3 (12) (2015) 1465–1468.

[107] M. Silic, P.B. Lowry, Using Design-science Based Gamification to Improve Organizational Security Training and Compliance. Journal of Management Information Systems 37 (1) (2020) 129–161.

[108] I. Sim, Mobile Devices and Health, New England Journal of Medicine 381 (10) (2019) 956–968.

[109] S. Singh, W. Xu, Robust Detection of Parkinson’s Disease Using Harvested Smartphone Voice Data: A Telemedicine Approach, Telemedicine and e-Health 26 (3) (2020) 327–334.

[110] J. Siöström, P. Ågerfalk, A. Heyner, The Design of a System for Online Psychosocial Care: Balancing Privacy and Accountability in Sensitive Online Healthcare Environments Journal of the AIS (2022)

[111] J. Song, F.M. Zahedi, Trust in Health Infomediaries, Decision Support Systems 43

[112] S.C. Srivastava, S. Chandra, Social Presence in Virtual World Collaboration: An Uncertainty Reduction Perspective using a Mixed Methods Approach, MIS Quarterly 42 (3) (2018) 779–804.

[113] J.H. Steffen, J.E. Gaskin, T.O. Meservy, J.L. Jenkins, I. Wolman, Framework of Affordances for Virtual Reality and Augmented Reality, Journal of Management Information Systems 36 (3) (2019) 683–729

[114] J. Steuer, Defining Virtual Reality: Dimensions Determining Telepresence, Journal of Communication 42 (4) (1992) 73–93

[115] L.A. Stutts, A.T. Hirsh, S.Z. George, M.E. Robinson, Investigating Patient Characteristics on Pain Assessment Using Virtual Human Technology, European Journal of Pain 14 (10) (2010) 1040–1045

[116] K.S. Suh, Impact of Communication Medium on Task Performance and Satisfaction: An Examination of Media-Richness Theory. Information & Management 35 (5) (1999) 295–312

[117] K.S. Suh, H. Kim, E.K. Suh, What if Your Avatar Looks Like You? Dual-Congruity Perspectives for Avatar Use, MIS Quarterly 35 (3) (2011) 711–729.

[118] K.S. Suh, Y.E. Lee, The Effects of Virtual Reality on Consumer Learning: An Empirical Investigation, MIS Quarterly 29 (4) (2005) 673–697.

[119] N.D. Thangada, N. Garg, A.; Pandey, N. Kumar, The Emerging Role of Mobile-Health Applications in the Management of Hypertension, Current Cardiology Reports 20 (9) (2018) 1–9.

[120] J.C.H. Tsai, Y.W. Liang, W.S. Pearson, Utilization of Emergency Department in Patients with Non-Urgent Medical Problems: Patient Preference and Emergency Department Convenience, Journal of the Formosan Medical Association 109 (7) (2010) 533–542.

[121] V. Venkatesh, S.A. Brown, A Longitudinal Investigation of Personal Computers in Homes: Adoption Determinants and Emerging Challenges, MIS Quarterly 25 (1) (2001) 71–102.

[122] J.G. Walls, G.R. Widmeyer, O.A. El Sawy, Building an Information System Design Theory for Vigilant EIS, Information Systems Research 3 (1) (1992) 36–59.

[123] L.D. Wandner, M.W. Heft, B.C. Lok, A.T. Hirsh, S.Z. George, A.L. Horgas, J. W. Atchison. C.A. Torres. M.E. Robinson. The Impact of Patients' Gender. Race and Age on Health Care Professionals’ Pain Management Decisions: An Online Survey Using Virtual Human Technology, International Journal of Nursing Studies 51 (5) (2014) 726–733.

[124] A. Wernhart, S. Gahbauer, D. Haluza, eHealth and Telemedicine: Practices and Beliefs among Healthcare Professionals and Medical Students at a Medical University, PLOS ONE 14 (2) (2019), e0213067, https://doi.org/10.1371 journal. pone.0213067.

[125] B.K. Wiederhold, K. Gao, C. Sulea, M.D. Wiederhold, Virtual Reality as a Distraction Technique in Chronic Pain Patients, Cyberpsychology, Behavior, and Social Networking 17 (6) (2014) 346–352

[126] T. Wu, J-M. Redouté, M.R.A. Yuce, Wearable Wireless Medical Sensor Network System Towards Internet-of-Patients. in: 2018 JEEE SENSORS. 2018. pp. 1–3.

[127] H. Xu. T. Dinev. J. Smith. P. Hart. Information Privacy Concerns: Linking Individual Perceptions with Institutional Privacy Assurances Journal of the Association for Information Systems 12 (12) (2011) 798–824.

[128] H. Yao, A.G. de Siqueira, A. Foster, I. Galynker, B. Lok, Toward Automated Evaluation of Empathetic Responses in Virtual Human Interaction Systems for Mental Health Scenarios, in: Proceedings of the 20th ACM International Conference on Intelligent Virtual Agents, 2020, pp. 1–8. October

[129] G. Yoon, P.T. Vargas, Know Thy Avatar: The Unintended Effect of Virtual-Self Representation on Behavior, Psychological Science 25 (4) (2014) 1043–1045.

[130] F.M. Zahedi, J. Song, Dynamics of Trust Revision: Using Health Infomediary, Journal of Management Information Systems 24 (4) (2008) 225–248

[131] F.M. Zahedi, N. Walia, H. Jain, Augmented Virtual Doctor Office: Theory-Based Design and Assessment, Journal of Management Information Systems 33 (3) (2016).776–808

[132] F. Zahedi, H. Zhao, N. Walia, H. Jain, P. Sanvanson, R. Shaker, Treating Patients Real Avatars in the Virtual Medical Office, IEEE Intelligent Systems 29 (2) (2014) 67–71.

[133] F.M. Zahedi, G. Bansal, J. Ische, Success Factors in Cooperative Online Marketplaces: Trust as The Social Capital and Value Generator in Vendors Exchange Relationships, Journal of Organizational Computing and Electronic Commerce 20 (4) (2010) 295–327.

[134] M. Zalake, F. Tavassoli, K. Duke, T. George, F. Modave, J. Neil, J. Krieger, B. Lok, Internet-based Tailored Virtual Human Health Intervention to Promote Colorectal Cancer Screening: Design Guidelines from Two User Studies, Journal or

[135] H. Zhao, S. Du, J. Cai, Y. Mao, Recommendations for Medical Care of Oncological Patients During the COVID-19 Epidemic: Experiences from China. Updates in Surgery 72 (2) (2020) 235–236.

Fatemeh Mariam Zahedi is a UWM Distinguished Professor Emerita and ITM Professor Emerita at the Sheldon B. Lubar College of Business, University of Wisconsin-Milwaukee She has received her doctoral degree from Indiana University. She has published more than 130 refereed papers in premier journals and conference proceedings, including MIS Quarterly, Information Systems Research, Journal of Management Information Systems, Man agement Science. IEEE Transactions on Software Engineering, Operations Research. IEEE Transactions on Systems, Man, and Cybernetics. IIE Transactions, Review of Economics and Statistics, and others. She has served as a senior editor and an associate editor of MIS Ouarterly, on editorial board of Journal of Management Information Systems, and an associate editor of Information System Research. Dr. Zahedi has been the PI of grants funded by NSF and other agencies. She is the author of two books: Quality Information Systems and Intelligent Systems for Business. She has received several research, teaching, and best paper awards. In a study by Stanford University, Dr. Zahedi was ranked among the top

2% scientists in the world in her field (https://uwm.edu/business/lubar-researchers-amon g-the-top-2-percent-of-scientists-worldwide-based-on-citations/). The list of Dr. Zahedi’s publications is available on https://scholar.google.com/citations?user=RUVoJuU AAAAJ&hl=en.

Huimin Zhao is a Professor of Information Technology Management at the Sheldon B. Lubar College of Business, University of Wisconsin-Milwaukee. He received his Ph.D degree in Management Information Systems from the University of Arizona. His research interests include data mining and healthcare informatics. He has published in such journals as MIS Quarterly, Journal of Management Information Systems, Communications of the ACM, IEEE Transactions on Knowledge and Data Engineering, and many others. Dr. Zhao currently serves as an associate editor for Information Systems Research and an associate editor for the Journal of Business Analytics, and has served as an associate editor for MIS Quarterly and a senior editor for Decision Support Systems.

Patrick Sanvanson, MD is an Associate Professor of Medicine at the Medical College of Wisconsin (MCW) and Associate Director of the Neurogastroenterology, Motility, and Airway Protection Research Laboratory in the Division of Gastroenterology & Hepatology at MCW. He earned his medical degree at MCW, completed an Internal Medicine residenc at Washington University in St. Louis, and completed his fellowship training in Gastro enterology & Hepatology at MCW. Dr. Sanvanson is an instrumental member of the worldrenowned Gastrointestinal Motility team at MCW that includes the MCW Dysphagia Institute. He practices Gastroenterology at Froedtert & the Medical College of Wisconsin Hospital and Gastroenterology Clinic in Milwaukee, Wisconsin. He is actively involved in research focusing on esophageal and aerodigestive tract sensory and motor physiology, and visceral pain. He is principal investigator in a multiple principal-investigator NIH R01 grant titled “Neuromolecular Mechanisms of Chronic Pelvic Pain in Neonatally-Induced Cystitis.”

Nitin Walia received his Ph.D. degree in Information Systems from the University of Wisconsin-Milwaukee. He also holds M.S. degrees from Oakland University, MI, and Pune University, India. He is currently a Clinical Professor in the W. P. Carey School of Business at Arizona State University. His main research interests include business analytics, data mining, healthcare delivery systems, online marketplaces, and web design interface issues. He is also working on issues related to providing medical services through a virtual world. His work has been published in several national and international journals, including the Journal of Management Information Systems, Journal of Information Technology Case and

Application Research, Electronic Commerce Research, IEEE Transactions on Software Engi neering, IEEE Intelligent Systems Journal, and International Journal of Electronic Busines Management.

Hemant Jain is W. Max Finely Chair and Professor of Data Analytics, in Rollins College of Business at University of Tennessee Chattanooga. His work has appeared in ISR, MISQ, IEEE Transactions on Software Engineering, JMIS, IEEE Transactions on Systems Man and Cybernetics, Naval Research Quarterly, Decision Sciences, Decision Support Systems, Commu nications of ACM, and Information & Management. He served as Associate Editor-in-Chief of IEEE Transactions on Services Computing and as Associate Editor of JAIS & ISR. He received his Ph. D from Lehigh University, a M. Tech. from IIT Kharagpur, and B. E. from University of Indore, India

Reza Shaker, MD is Joseph E. Geenen professor of Medicine, Radiology, and Otolaryn gology, Chief of the Division of Gastroenterology and Hepatology, Director of the Digestive Disease Center, and senior associate dean at the Medical College of Wisconsin. He is the founder and director of Center for Translational Science Institute of Southern Wisconsin. Dr. Shaker received his medical degree from Tehran University Medical School, completed his Internal Medicine residency at Kingsbrook Jewish Medical Center in Brooklyn, NY, and his Gastroenterology Fellowship at the Medical College of Wisconsin. Dr. Shaker is an internationally recognized gastroenterologist and an investigator in the field of dysphagia, gastroesophageal reflux disease and cerebral cortical control of gastrointestinal sensory motor function. His research has led to some of the seminal discoveries in the area of airway protection. He was the first to describe that the deglutitive upper esophageal sphincter opening can be increased by strengthening exercises of the suprahyoid muscles—the Shaker Exercise. His work has led to the description of the subliminal domain of gut sensory function, allowing investigation of direct braingut axis without the influence of human cognition. He developed the field of functional interaction between the upper gut and aerodigestive tract, leading to the discovery of several related reflexes. Dr. Shaker has developed the technique of transnasal unsedated upper GI endoscopy for concurrent evaluation of the aerodigestive and upper GI tracts. He is the founder of the Dysphagia Research Society and the Medical College of Wisconsin’s Dysphagia Institute. Dr. Shaker has published more than 330 papers in academic journals and has been the PI of numerous grants from NIH and other agencies. He has received many awards, has served as the editor, guest editor, and editorial board member of ten academic journals, and has had leadership positions in many national academic and policy-making committees.
