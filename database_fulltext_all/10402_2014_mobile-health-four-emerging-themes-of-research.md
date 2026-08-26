---
otero_id: 10402
otero_key: "8UCSTUPB"
title: "Mobile health: Four emerging themes of research"
authors: "Upkar Varshney"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2014.06.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Upkar Varshney

Department of Computer Information Systems, Georgia State University, Atlanta, GA 30302-4015, United States

a r t i c l e i n f o

Article history: Received 16 July 2013 Received in revised form 22 April 2014 Accepted 1 June 2014 Available online 22 June 2014

Keywords: Mobile health Information technologies Decision making Emergencies Applications

## a b s t r a c t

Mobile health has been receiving a lot of attention from patients, healthcare professionals, application developers, network service providers and researchers. Mobile health is more than just some healthcare applications on a mobile phone and it can involve sensors and wireless networks in monitoring various conditions, mobile devices to access numerous healthcare services, healthcare professionals to make decisions and provide emergency care, and for the elderly to manage their daily activities in independent living. More speci<sup>fi</sup>cally, m-health can result in major advances in (a) expanding healthcare coverage, (b) improving decision making, (c) managing chronic conditions and (d) providing suitable healthcare in emergencies. To help realize these advances, there are major research challenges that need to be addressed. We classify these challenges in four categories of (a) patients related, (b) healthcare professionals related, (c) IT related and (d) applications related challenges. Within each category, we identify several research problems, and we present some high-level and preliminary solutions along with an agenda for future research. The paper may provide a platform for future research and decisionmaking related to patients, healthcare professionals, applications, and infrastructure. These decisions will significantly impact how future mobile health services will be designed, developed, evaluated, and adopted globally © 2014 Elsevier B.V. All rights reserved.

## 1. Introduction

Mobile health is broadly de<sup>fi</sup>ned as “healthcare to anyone, anytime, and anywhere by removing locational and temporal constraints while increasing both the coverage and the quality of healthcare” [59]. Mobile health is much more than just accessing healthcare applications on a mobile phone as m-health can involve sensors and wireless networks in monitoring various conditions, mobile devices to access a variety of healthcare services, healthcare professionals to make decisions and provide emergency care, and the elderly to manage their daily activities for independent living among other things. Thus mobile health can include numerous sophisticated applications that deal with disease prevention & wellness [61], monitoring and remote care [47,62], mobile decision making [1], and emergency interventions [59]. In addition, several applications on horizon include highly personalized health monitoring [42], mobile healthcare data access [23], and sophisticated mobile telemedicine [65].

We do not claim that m-health can <sup>fi</sup>x all the healthcare problems, but it can improve the reach of healthcare, decision making, management of chronic conditions and emergencies. Mobile health can truly change the way healthcare services are delivered: from the current healthcare professionals-controlled to healthcare professionals-managed. One of the major effects of m-health is empowering patients with information to help them make suitable healthcare decisions, follow advice and medical regimen, and in general have better control of their healthcare. The availability of numerous m-health applications, more than 100,000 at the time of writing this paper, is a major step towards such empowerment of patients. Some other areas of improvement include reduction in cost, more ef<sup>fi</sup>cient processes, and meeting some of the workload needs of healthcare professionals. Certainly much more work is needed to evaluate the effectiveness of mobile health in terms of quality of decision making, quality of care, ef<sup>fi</sup>ciencies of healthcare processes, outcomes of patients, and reduction of overall cost.

## 1.1. Related advances

Several advances in sensing devices, miniaturization of low-power electronics, and wireless networks [5] are fueling the emergence of mobile health. The wireless technologies can be effectively utilized by matching infrastructure capabilities to healthcare needs. These include the use of location tracking, intelligent devices, user interfaces, body sensors, and short-range wireless communications for health monitoring; the use of instant, <sup>fl</sup>exible and universal wireless access to increase the accessibility of healthcare providers; and reliable communication among medical devices, patients, health-care professionals, and vehicles for effective emergency management.

The recent FCC spectrum allocation for mobile medical telemetry can improve both the quality and quantity of medical data that can be transmitted from patients to healthcare professionals [23]. The interoperability among various systems is being addressed by the development of medical standards, industry alliances, and consortiums, such as the IEEE 802.15.6 wireless body area networks (WBANs), Continua Alliance and the European Telecommunications Standards Institute's eHEALTH [23].

Table 1  
M-health comparison in developed and developing countries

<table><tr><td>Attributes</td><td>Developed countries</td><td>Developing countries</td><td>Comments</td></tr><tr><td>Infrastructure</td><td>Well developed</td><td>Somewhat developed and access/reliability challenges</td><td>The interoperability of infrastructure still needs to be addressed</td></tr><tr><td>Most suitable applications</td><td>Mobile apps for health management</td><td>Information on diseases, reminders for care, remote care</td><td>Revolutionary (primary) in developing countries, evolutionary (secondary) in developed countries</td></tr><tr><td>Barriers</td><td>A lack of clear policy, cost of access, security &amp; reliability challenges</td><td>Lack of infrastructure, cultural and social barriers, lack of education, role of alternate medicine</td><td>Numerous barriers can be studied in adoption of m-health in developing and developed countries</td></tr><tr><td>Regulatory environments</td><td>Evolving</td><td>Evolving</td><td>One of the biggest challenges</td></tr><tr><td>Future of m-health</td><td>Secondary but important healthcare role</td><td>Potential for primary healthcare role in underserved/rural areas</td><td>Many challenges need to be overcome</td></tr></table>

One of the major advances fueling the growth of m-health is the worldwide availability of mobile technologies, such as mobile phones of 3rd and 4th generation (3G and 4G), that are usable almost anywhere anytime. The decline in price of access, improved portability and comfort of people in using mobile technologies have all helped m-health moving forward at a rapid pace.

## 1.2. The role of m-health

M-health can play many different roles based on the patients' conditions, their needs and availability of healthcare services. The roles include providing necessary healthcare information anytime anywhere, providing remote and expanded care, access to healthcare professionals anytime anywhere via mobile devices, integrated and real-time information to healthcare professionals for decision making, and the broadcasting of information in cases of disasters.

M-health can reach to places where little or no healthcare is available such as rural areas especially in developing countries and can also allow people in urban areas and developed countries to access some healthcare services while being mobile/away from their places. Mhealth is likely to be incremental in the developed countries as it plays an adjunct role to what is already supported by e-health. M-health is likely to be revolutionary in developing countries, where little infrastructure is available and presence of mobile phones can lead to rapid adoption of mobile health, especially in rural and remote areas. Mhealth in developing countries will play a major role in health interventions [8], prevention of communicable diseases [61] and in improving health literacy [33]. A comparison of m-health in developed and developing countries is shown in Table 1 and different scenarios are presented in Fig. 1.

![](/api/attachments/8UCSTUPB/fulltext/images/f9e32cbaf1b5323bd0dbfbe53f8efebdcd5d09e109d630962b39ca22d53559e4.jpg)  
(a) Mobile Health in Developed countries with 3G/4G Wireless Networks

![](/api/attachments/8UCSTUPB/fulltext/images/b880003b5513e145fa1c4476bf920e9d70f457f227e0472db0d7e97c64551b1c.jpg)  
(b) Mobile Health in Developing countries with 2G/3G Wireless Networks  
Fig. 1. M-health in developed and developing countries.

M-health will also change the way healthcare services are delivered. With mobile devices being integrated in various healthcare processes, many sub-processes will be automated while the rest can be ef<sup>fi</sup>ciently supported by healthcare professionals. For example, m-health can enable highly personalized healthcare in general and suitable interventions for patients to managing their chronic conditions in particular. Highly sophisticated interventions can be designed, developed and offered to patients to manage their complex regimen of medications to improve medication adherence, avoid adverse drug events (ADE) and communicate with healthcare patients as and when necessary in real-time.

## 1.3. The limitations

M-health cannot solve all problems of healthcare as it is highly dependent on sensors, mobile devices and wireless infrastructure. In places where there is no wireless coverage or when mobile devices have battery or access problems, mobile health is simply not possible.

M-health cannot, and should not, completely automate the delivery of healthcare services. There are many m-health applications that must have human involvement due to their potential for damage or injury to the patient's health. FDA has offered some guidelines on what mobile health applications can do and what they cannot and who is liable if a patient is injured due to mobile health applications. In general, if an application is providing healthcare information and is not connected to any healthcare delivery device, the FDA rules will not apply to such applications.

Mobile health is not likely to play a primary role in cities in developed countries, where both “wireline” network infrastructure as well healthcare facilities are readily available. Certainly much more work is needed to evaluate most suitable m-health services in developed as well as developing countries.

One of the goals of this paper is to integrate advances and various challenges for mobile health and identify many important research problems. Towards this goal, we <sup>fi</sup>rst envision what mobile health can do by focusing on (a) extending the reach of healthcare, (b) improving the healthcare decision making processes and their outcomes, (c) better management of chronic healthcare conditions and (d) managing emergencies in Section 2. We then present a framework for mobile health based on four categories of research problems based on patients, healthcare professionals, IT and m-health applications in Section 3. Then, in Section 4, we present research problems and some preliminary solutions for four categories that can be expanded by other researchers. Then we make some concluding remarks in Section 5.

## 2. Applications and bene<sup>fi</sup>ts of mobile health

We focus on what mobile health can do by addressing its ability in (a) extending the reach of healthcare services, (b) improving decision making, (c) preventing and managing chronic conditions and (d) providing faster emergency care. We next discuss these categories one by one.

## 2.1. Extending the reach of healthcare

## 2.1.1. Removal of constraints & improved access

Mobile health can remove locational constraints as there is no need for patient and healthcare professionals to be in the same location or to be stationary. Support for mobility is one of the most exciting features of mobile health. The temporal constraints could be removed for some cases, termed asynchronous version such as an expert reading the patient's records and sending the diagnosis to the primary care physician and patient at a different time. For synchronous version, the patient and healthcare professionals are using mobile health system at the same time, possibly in different locations. Some mobile health applications could exist in both versions such as mobile health monitoring [27,32,53,54] where monitoring of vital signs for certain events is synchronous while monitoring of weight loss, sleep, and daily activity is asynchronous [40].

## 2.1.2. Implementation & focus

Mobile health can be implemented in two variations: automated and human-assisted to support the informational and direct healthcare applications, respectively. Further, the focus can be user-centric vs providercentric. There are numerous examples among the 100,000 health applications for smart phones [23] including medical reference applications [31]. A 2 × 2 classi<sup>fi</sup>cation is shown in Fig. 2. It should be noted that not all mobile health applications can be classi<sup>fi</sup>ed by such simple method. One of the challenges is to classify numerous mobile health applications to help patients decide which applications are similar and which ones are different in what ways. This would also help in developing new applications as identi<sup>fi</sup>ed by the classi<sup>fi</sup>cation scheme [75].

## 2.1.3. The role

In places where healthcare services are readily available, m-health will play a supportive role such as accessing health information and services while being mobile. In rural and remote areas in both developing and developed countries, it will play a primary role. The examples are behavioral healthcare in rural areas using cell phones, adherence reporting and appointment reminders [34], behavioral interventions to reduce cardiovascular risk factors [8], vaccine delivery in sub-Saharan Africa [61], and improving health literacy [33].

## 2.1.4. Delivery model

The healthcare delivery model will evolve from the current healthcare professional-controlled care to healthcare professional-managed care. For some cases, such as for patients in poor conditions, the healthcare professionals will still play a major role, while patients in better conditions would bene<sup>fi</sup>t more from the healthcare professional-managed model of care. As more and more patients start using mobile health applications such as mobile PHR, medical databases, and healthcare informational services, the need for care will change and will move towards the healthcare professional-managed model.

<table><tr><td></td><td>Automated</td><td>Human-assisted</td></tr><tr><td>User Centric</td><td>Mobile Personal Health Record</td><td>Mobile Health Monitoring</td></tr><tr><td>Provider Centric</td><td>Mobile Medical Reference</td><td>Mobile Decision Making</td></tr></table>

Fig. 2. A 2 × 2 classi<sup>fi</sup>cation of m-health applications.

## 2.2. Improving healthcare processes and decision making

One of the major goals of m-health is to make healthcare processes more ef<sup>fi</sup>cient and improve the quality of outcomes. Many healthcare processes are very complex and involve people, technologies and rules. Good understanding of healthcare processes and how people interact with technologies in unpredictable situations, how physicians use technologies, how medical decisions are made, how people take medications, and how the elderly live alone will help towards achieving this goal. By improving various healthcare processes, mobile technologies can also improve the outcomes of various healthcare activities.

## 2.2.1. Healthcare processes

Access to patient's most recent information could reduce the need for “duplicated” tests. Also, access to current medical knowledge can improve the quality of decision making [37]. Mobile technologies can lead to ef<sup>fi</sup>ciency improvements such as decreased time for task completion and accessing history [1]. By collecting and delivering vital information at the point of care, hospitals can improve ef<sup>fi</sup>ciency and safety [1]. It has been shown that the use of mobile systems reduced the task completion time signi<sup>fi</sup>cantly [38]. The average time on monitoring patients was reduced about 40%, while the total time on indirect tasks was reduced about 30% [11].

## 2.2.2. Decision making

Healthcare professionals are trained to perform these decisions under extreme circumstances with little or no advance notice sometimes. Healthcare professionals consider symptoms, medical history, lab results and diagnostic tests among others in reaching to medical decisions. Many times, additional alternatives or choices become available as the decision making process moves forward. Mobile technologies can play a very important, but assistive, role in decision making by supporting the needed information anytime anywhere to anyone authorized. This could include mobile access to expert systems and evidence-based medicine tools [10].

## 2.2.3. Speed of decision making

Mobile technologies can support faster access to healthcare professionals and health information and that could lead to faster decision making [37] such as those needed for emergency cases. The speed vs accuracy of decision making should be studied in different scenarios of preventive care, urgent care, emergency care, home health, and longterm care. Although, mobile technologies can lead to improvements in some steps of decision making, certainly more work is needed towards evaluating the impact on overall decision making.

## 2.2.4. Correctness of decision making

Many medical errors occur due to the lack of correct and complete information at the location and time it is needed, potentially resulting in wrong diagnosis and drug interaction problems [58,20]. Mobile technologies, by improving information access and tracking of patients, supplies and medications, can help to reduce information-related medical errors. More work is needed to evaluate the impact of mobile technologies on other errors, including process errors and knowledge/skill errors [36], such as wrong treatment with right diagnosis.

## 2.3. Preventing and managing chronic conditions

Chronic diseases, such as heart disease, stroke, cancer, diabetes, and arthritis, are among the most common, costly, and preventable of all health problems in the U.S. and heart disease, cancer and stroke lead to 50% of all deaths [7]. Mobile technologies can help in preventing and/or managing chronic diseases by monitoring physical and behavioral health, medications, and activities of daily living (ADL), and by providing mobile-enabled interventions and changing these as needed with time. A model for prevention and management of chronic conditions is shown in Fig. 3.

## 2.3.1. Prevention

The prevention involves mobile health monitoring dealing with activities [54], exercises, health promotion tools and messages [17,35], and caloric and dietary monitoring [66]. These could be implemented in multiple forms such as wearable monitoring systems and sensors in shoes [45] to classify daily activities, Internet-aware exercise machines, cell-phone based applications [57], musical feedback and exercise [41], electronic wellness diary, and social networking-based systems [35]. Other prevention tools include fall detection system [12], wrist-worn integrated health monitoring device [24], guidance system for the elderly [52], stray prevention system for the elderly with dementia (GIS) [28], and, monitoring system analyzing deviations from daily rhythms to predict health changes [17].

## 2.3.2. Management

To manage chronic conditions, mobile technologies can support interventions for medication adherence by using reminders to patients and remote monitoring of adherence. Mobile technologies can support effective management of chronic diseases by faster communications and feedback from healthcare professionals. This can motivate patients, especially younger people, to take better control of their lifestyle. Management of diabetes can be well supported by mobile health [2]. For dietary monitoring, a mobile application can track caloric information, store the food and activities, and keep daily calorie data [56] and can work with swallowing detection using neck sensors [3].

The monitoring of bipolar disorders using mobile device can reduce the possibility of an episode [47] and can support the behavioral healthcare needs in remote areas. To manage Parkinson's disease, a sensor system can monitor the coordination between respiration and locomotion as part of rehabilitation [64]. To help reduce chronic back pain, a smart system can detect and inform a person sitting with incorrect posture [16].

## 2.4. Helping in emergencies

## 2.4.1. Emergency healthcare processes

The goal is to <sup>fi</sup>nd what the problem is and <sup>fi</sup>x it quickly to avoid immediate risks to the patients. The emergency processes include (a) incidence detection, (b) transportation to healthcare facilities, (c) getting patient's information, and (d) making suitable decisions and (e) providing care. Mobile health can play a very important role in emergencies as it can help in speeding up some of the above processes (Fig. 4). The solid lines indicate the sequence in the current emergency care, while dashed lines indicate the steps due to m-health. More speci<sup>fi</sup>cally, the sequence in the current emergency care is 1, 2, 3, 4 and 5. M-health can improve this to 1, 2, and 5 or 1, 2, 4, and 5, or 1, 3, 2, and 5 or 1, 3, 2, 4, and 5. This can be used in making suitable decisions on how m-health can be utilized in emergency care.

## 2.4.2. Improving and speeding existing processes

Incidence detection and transportation involves <sup>fi</sup>nding out the location and extent of the emergencies related to healthcare and then managing it to meet the healthcare needs of the people involved. One solution to this is to design and implement intelligent emergency response using the information from mobile and wireless networks. The information could include locations of emergencies derived from location tracking of enhanced 911 calls. The information from wireless networks can also be used to <sup>fi</sup>nd the best routes and allowing intervehicular communication for traf<sup>fi</sup>c routing. This could be combined with <sup>fi</sup>nding the closest hospital(s) with the needed care and also to check the availability of hospital space.

![](/api/attachments/8UCSTUPB/fulltext/images/c86bd8e473005e32366ef4ce86f507188f93bd786f90dda0e328f0815fea7f5a.jpg)  
Fig. 3. A model for prevention and management of chronic conditions.

## 2.4.3. Access to information in emergencies

The access to information depends on the condition of the patient. One solution is to store the patient information on cell phones, or in implanted or wearable RFID chips that patients can carry. There are important issues of reliability, access, identity theft, limited access, limited storage and what should be stored, and, bene<sup>fi</sup>ts vs privacy trade-off that should be addressed. Other solutions include information on how to access personal health records. The devices can also store health history and known medical conditions as abbreviated electronic health record. A possibility is to provide access to EMR via a person's cell phone as many emergency medical services now utilize a person's cell phone for identi<sup>fi</sup>cation.

Fragmented health information was the main cause of preventable medical errors responsible of a number of deaths each year [58]. No patient should die because the system blocked access to vital data and any such access can show as a violation with a log of who accessed what information [39]. The information from multiple sources can be integrated and adapted to mobile devices of healthcare professionals [44].

## 3. A framework for mobile health

## 3.1. Structured survey of m-health literature

As part of the development of m-health framework, we realized that there should be some dimensions in the framework. To derive the dimensions, we performed a comprehensive literature survey of mobile-health. We considered literature in three related areas of Health Informatics, Biomedical Informatics, and Information Systems (Table 2).

We conducted a literature survey of journals in Information Systems, Healthcare Informatics, and Biomedical Informatics for m-health research published between Jan. 2000 and Dec. 2012. The search involved title, abstract, and keywords for “mobile OR wireless OR pervasive” AND “health”. While studying the literature, some unrelated articles were removed such as those on use of mobile devices causing health problems. The survey yielded 102 articles in above journals. Overall, the trends showed nearly doubling of articles every four years with 15 articles during 2001–2004, 26 during 2005–2008, and 60 during 2009–2012. A closer examination of the contents of the articles reveals several categories in terms of patients, healthcare professionals, IT and applications. Several articles have more than one category and are thus classi<sup>fi</sup>ed (Table 3).

As shown in Table 3, the number of m-health articles in Information Systems includes 16 in journals (1 in EJIS, 10 in DSS, 5 in CACM) and 27 in major IS conferences including ICIS, AMCIS, ECIS and HICSS. Many other IS journals do not have any m-health articles yet. Information Systems is the only area with majority of articles on healthcare professionals. Biomedical Informatics primarily focuses on IT with 79% of its articles <sup>fi</sup>tting in that category of research.

For all m-health literature, IT is the most common research category with 45% articles relying on IT to address the healthcare challenges. About 11% of the articles focus on the design, development and testing of m-health applications. This is expected to increase as more applications are becoming available for mobile devices and are being tested in various clinical and non-clinical situations. Biomedical Informatics has the highest percentage of articles (15%) addressing application issues. Many of the proposed systems would be tested using a variety of methods including those based on theories. A classi<sup>fi</sup>cation of mhealth research and potential outlets is included in Appendix A (Fig. A1).

![](/api/attachments/8UCSTUPB/fulltext/images/9428187a792c906ca3b48cb6605f01cdd720801bbb511b399cfdaac0c6511892.jpg)  
Fig. 4. Emergency care and m-health enhancements.

The list of journals included in the survey.

<table><tr><td>Health informatics (4)</td><td>Biomedical informatics (5)</td><td>Information systems (8)</td></tr><tr><td rowspan="3">International Journal of Medical Informatics (IJMI)</td><td>IEEE Transactions on IT in BioMedicine (TITB) $^a$ </td><td>MIS Quarterly (MISQ)</td></tr><tr><td>IEEE Journal on Selected Areas in Communications (JSAC)</td><td>Information Systems Research (ISR)</td></tr><tr><td>IEEE Sensors Journal</td><td>Journal of MIS (JMIS)</td></tr><tr><td>Health Affairs (HA)</td><td>IEEE Reviews in Biomedical Engineering</td><td>Decision Support Systems (DSS)</td></tr><tr><td>Journal of American Medical Informatics Association (JAMIA)</td><td></td><td>European Journal of IS (EJIS)</td></tr><tr><td rowspan="3">Health Services Research (HSR)</td><td>Mobile Networks and Applications (MONET)</td><td>Information Systems Journal (ISJ)</td></tr><tr><td></td><td>Journal of AIS (JAIS)</td></tr><tr><td></td><td>Communications of the ACM (CACM)</td></tr></table>

<sup>a</sup> Now known as IEEE Journal of Biomedical and Health Informatics (JBHI).

We acknowledge that there are several other categories that are highly important area of research and should be included in a comprehensive framework for mobile health. These categories are (a) legal and regulatory environment including security and (b) adoption and related theories among others. Due to the length restriction, we had to limit the scope of the proposed framework to the above four categories. It is our sincere hope that others will expand the proposed framework to include the additional categories and research problems in mhealth that are not included in this paper.

## 3.2. Development of m-health framework

In addition to the support from the literature for a research framework for m-health, we re<sup>fl</sup>ected on many related research frameworks that have been proposed for mobile applications in other areas. More speci<sup>fi</sup>cally, we studied several frameworks in future decision support systems [67], mobile commerce [72,73], wireless networking [71], mobile health monitoring [68,69], and the context-aware services [70,74]. Using the current m-health literature and research frameworks from mobile application in other areas and our own understanding of what m-health is and what it can become in future, we derived the framework as shown in Fig. 5.

In the high-level view of m-health framework, patients can interact with mobile health applications, which are supported by Information Technologies. Patients may receive care from healthcare professionals directly or via m-health applications. Many such combinations are possible. Many m-health services can be provided to patients that do not rely on m-health applications, but use specialized devices/sensors

## Table 3

Analysis of published articles on m-health

<table><tr><td rowspan="2">Articles from: total</td><td colspan="4">The four identified categories of research</td></tr><tr><td>Patients</td><td>Healthcare professionals</td><td>IT</td><td>Applications</td></tr><tr><td>IS journals: 16</td><td>2 (13%)</td><td>10 (63%)</td><td>6 (38%)</td><td>2 (13%)</td></tr><tr><td>HI journals: 53</td><td>20 (38%)</td><td>17 (32%)</td><td>14 (26%)</td><td>4 (8%)</td></tr><tr><td>BMI (IEEE) journals: 33</td><td>18 (55%)</td><td>7 (21%)</td><td>26 (79%)</td><td>5 (15%)</td></tr><tr><td>Total journals: 102</td><td>40 (39%)</td><td>34 (33%)</td><td>46 (45%)</td><td>11 (11%)</td></tr><tr><td>IS conferences: 27</td><td>10 (37%)</td><td>12 (44%)</td><td>10 (37%)</td><td>2 (7%)</td></tr></table>

Note: As some articles could <sup>fi</sup>t in more than one category, the total percentage in all categories could exceed 100%.

such as those for health monitoring. In the next few sub-sections, we discuss these four categories. The details on research and preliminary/ possible solutions are presented in Section 4.

Our simple framework for m-health can be expanded in several different directions based on the context of research. One such example of expansion in the context of m-health as a service is shown in Fig. 6. When m-health is considered as a service, there are some differences as m-health can be (a) constrained due to regulatory and legal environment, (b) the patient may not completely understand the implications even when signing the consent form, and (c) someone else may be paying for the service, while the patient's life and condition may be impacted directly. However, m-health will allow regular healthcare care to be negotiated for a lower cost, better quality, negotiated pricing by using applications/agents to negotiate with some willing healthcare providers. However, the same cannot be said for emergency care, which should not be negotiated and the focus of m-health service should be enable fastest care meeting the needed threshold of quality at the closest location. It is likely that in the future multiple healthcare professionals will advertise their services for comparison shopping (middleware supported) based on context, history and price (within regulatory framework). Although the healthcare human resources are limited in the US and in most countries, the IT can offer almost unlimited support for M-health services in multiple ways by working with applications that are value-adding to healthcare. Intelligent agents as an application can negotiate various attributes such as appointment time, cost, and can utilize past history of care, outcomes, availability of care as multiple metrics for quality of service. These can summarize all the possible choices to patients and in some cases, even act as a recommender system. This service-oriented view of m-health is shown in Fig. 6.

## 3.3. The patients

Patients of different demography such as adolescents, adults, and the elderly living independently or in assisted living/nursing homes would interact with mobile health very differently due to their health conditions, attitudes towards care, and knowledge and comfort with mobile technologies and healthcare applications. These differences should be included in the design, development and implementation of mobile health applications and infrastructure. M-health will play a major role for the elderly and to some extent for the adolescents; and somewhat limited role for active healthy adults with limited need for healthcare services and easy access to other technologies for e-health.

## 3.4. Information technologies

The most suited characteristics are support for mobility of patients and healthcare professionals, instant access to information and the immediate attention to devices by everyone. The suitable technologies for healthcare could be divided among four categories: implanted, wearable, portable, and environmental [59]. The respective examples are RFID and sensors, Smart Shirts [26], handheld devices, and Smart Homes [15,54]. These technologies differ in terms of complexity, user interface, reliability, replacement and battery requirements, and the cost.

![](/api/attachments/8UCSTUPB/fulltext/images/76980fed05bfe13ee8cb4272685b5af1445ed1b660697e6215c43b786bd7177b.jpg)  
Fig. 5. A high-level view of m-health framework.

While each of these technologies can play a role in mobile health, more work is needed towards selecting (and even replacing if needed) most suitable technology for the patient (Table 4). This decision could have a major impact on if and how long patients would use mobile technologies. The limitations that hinder acceptance of mobile and ubiquitous technologies include short battery life [1]. Also, varying social contexts of individual use result in different social in<sup>fl</sup>uences that affect the individual's perceptions of user satisfaction with the mobile technology [51].

## 3.5. Applications

There are more than 100,000 mobile health applications available today for different mobile devices. The current mobile health applications deal with healthcare information access, health and disease advice, patient history, and decision support. M-health applications still have plenty of room to grow to take full advantage of unique mobile platform features and truly ful<sup>fi</sup>ll their potential [31]. More advanced applications can include personalized health monitoring [42], adaptable and context-aware applications, and applications based on multi dimensional interfaces. There is a need to study the effectiveness of different mobile health applications for different conditions and patients. More work is also needed in creating a detailed classi<sup>fi</sup>cation of these applications. Research is also needed to improve the security and privacy aspects of these applications and make patients aware of these challenges (Fig. 7).

## 3.6. Healthcare professionals

Healthcare professionals will play a major role in mobile health as they would still make most of the medical decisions related to direct care. Mobile health applications can be divided in two classes (a) where a patient interacts with applications without the involvement of HP and (b) where a patient interacts with applications with the involvement of

![](/api/attachments/8UCSTUPB/fulltext/images/82d9edd29bdcb05cfd97228d3cb6aab87c9cd8847d40d4885afdb2d555606b0c.jpg)  
HP: Limited and Regulated Supply  
Patients: Demand for M-health Services (both via applications and direct by healthcare professionals)  
Applications: Providing unlimited services with and without human involvement  
IT: Supporting unlimited access to mobile applications and other medical devices used in m-health

Fig. 6. A service-oriented view of m-health framework.

Table 4  
Suitable wireless technologies for healthcare.

<table><tr><td></td><td>Implanted</td><td>Wearable</td><td>Portable</td><td>Environmental</td></tr><tr><td>Suited for</td><td>Monitoring of internal organs/compensating for deficiency in operations</td><td>Monitoring of vital signs</td><td>Interacting with patients using mobile apps</td><td>For independent living for adults and the elderly</td></tr><tr><td>Some examples</td><td>Pacemakers, implanted sensors and “ingestible” RFID</td><td>Smart Shirts</td><td>Smart phone with sensors and mobile health apps</td><td>Smart house</td></tr><tr><td>Limitations</td><td>Potential for malfunctionDifficult to replace</td><td>Emerging technologyUsability for the elderly not clear</td><td>Reliability of devices and networks</td><td>Expensive and not easily available yet</td></tr><tr><td>The future</td><td>Limited and specific use</td><td>Potential for widespread use (especially among young people as fashion statement)</td><td>Most market due to widespread use of smart phones with built in sensors</td><td>Smart house may become standard house</td></tr><tr><td>Most likely used by</td><td>People with specific challenges where portable and wearable technologies are not useful</td><td>The young</td><td>Everyone</td><td>The adults and the elderly in independent living</td></tr><tr><td>Comments/additional insights</td><td>High cost of surgery and (long-term) devices</td><td>High cost (not mass produced yet)</td><td>Most cost effective/wide spread deployment</td><td>Most expensive (20–30% on top of regular building cost)</td></tr></table>

HP. The applications can be one way or two ways. A possible taxonomy is shown in Fig. 8 below.

In these scenarios, when HP is involved, he/she will certainly in<sup>fl</sup>uence the adoption of mobile health, while when HP is not involved, the adoption will be primarily in<sup>fl</sup>uenced by applications and the technology.

We <sup>fi</sup>rst discuss when HP is not involved. In this case, mobile applications should be personalized to the patient based on his/her abilities, health conditions, and some incentives can be offered to patients to adopt mobile health.

When HP is involved, the situation becomes much more complex. The portability, task structure, spatial mobility, and system reliability in-<sup>fl</sup>uence the use of mobile technology by healthcare professionals, their degree of satisfaction with the technology, and realization of the net bene<sup>fi</sup>ts [9]. Their acceptance and use of technology and applications are critical towards the success of mobile health [30]. Their familiarity with devices and applications affect the adoption of mobile applications [11,38]. The mobile technologies should be integrated in the work<sup>fl</sup>ow of healthcare professionals. The performance of nurses has been shown to improve when they accessed information anytime anywhere [1]. The role of incentives for healthcare professionals needs to be evaluated in mobile health adoption. The support from insurance companies and the government agencies on payment guidelines on various m-health services will clarify some uncertainty on what and how care provided would be compensated for mobile health.

## 4. Major challenges and research problems

To describe major challenges and research problems, we utilize the key attributes of m-health, as introduced in Section 2. These are (a) overcoming locational constraints and support for mobility, (b) supporting both synchronous and asynchronous versions of mhealth, (c) moving from healthcare professional-controlled to healthcare professional-managed care, (d) supporting both automated and human assisted care, (e) supporting both user-centric and provider-centric m-health, (f) improving the speed, quality and correctness of decision making, (g) improving processes and ef<sup>fi</sup>ciency, (h) supporting decision making by providing anytime anywhere access to information, (i) supporting effective management of chronic conditions as well as emergency care, and, (j) improving the quality of health outcomes.

The framework for mobile health presented in Section 3 can be extended to a research agenda for mobile health. The four dimensions, namely patients, applications, healthcare professionals and information technologies, are included with more speci<sup>fi</sup>c research problems (Fig. 9). The IT infrastructure can overcome locational constraints and provide support for mobility as part of overall support for mobile health. It can also enable mobile health applications in providing synchronous and asynchronous versions of m-health in developing as well as developed countries. IT, applications and healthcare providers can lead to improved processes, better and faster decision making, and highly

![](/api/attachments/8UCSTUPB/fulltext/images/adabef8ccd6be2b443bb9481de2b4d69f72bf3a880352a6eb8a7759af49e1bdc.jpg)  
Fig. 7. Decision making for privacy and bene<sup>fi</sup>ts in m-health.

## Healthcare Professionals

<table><tr><td rowspan="3">Applications</td><td></td><td>Involved</td><td>Not Involved</td></tr><tr><td>One-way</td><td>Reminders/Messages</td><td>Accessing Medical Information</td></tr><tr><td>Two-ways</td><td>Mobile Telemedicine</td><td>Interacting with M-health Applications</td></tr></table>

Fig. 8. A 2 × 2 taxonomy of HP and applications

personalized care. The empowered patients can lead to better management of their health by utilizing both automated and human-assisted care. Further, these all together can lead to much improved quality of health outcomes while reducing the overall cost of care and improving the quality of life for patients.

## 4.1. Research related to applications

Most of the current mobile healthcare applications, including over 100,000 available for mobile devices, deal with healthcare information access, health and disease advice, patient history, and decision support (Fig. 10). This is not a complete listing, but the most common existing mobile health applications and some emerging applications that can meet many goals of mobile health. Most of these applications are user-centric, while some are provider centric such as mobile DSS and mobile medical reference. Some of these applications could have synchronous and asynchronous versions. The choice of using one or the other can be based on the context of care such as patient's condition and/or network coverage and connectivity in non-emergency situations. These applications will support better decision making by providing anytime anywhere access to information and this in turn will lead to improved health outcomes.

We need to evaluate the effectiveness of currently available applications as well as identify more advanced applications for the future. The effectiveness of mobile health should include diverse set of patients including adolescents, adults and the elderly. The effectiveness of mobile health applications can be evaluated clinically, using design science approaches, as well as using theoretical models and user requirements. There is also a need to classify the m-health applications to help everyone conceptualize the differences and similarities, and also to identify the need for new applications. This can also help decision makers in mobile health [75].

The advanced applications could be designed and developed for different populations and diseases, chronic as well as short-term. M-health applications still have plenty of room to grow to take full advantage of unique mobile platform features and truly ful<sup>fi</sup>ll their potential. Also, the near-term introduction of two- or three-dimensional visualization and context-awareness could further enhance m-health applications usability and utility [31]. More advanced applications can include games for healthy eating and wellness. In one trial, children playing the game ate a healthy breakfast 52% of the time as compared to 20% of children not playing this game [48]. New applications that can support behavioral, technical, social and <sup>fi</sup>nancial interventions for medication adherence, wellness, life-style, and management of chronic conditions would be highly desirable.

![](/api/attachments/8UCSTUPB/fulltext/images/44531347082f38e16f57cf87c37a2f41164941ff2321f12b4587a111be6355c8.jpg)  
Fig. 9. Research agenda for mobile health.

![](/api/attachments/8UCSTUPB/fulltext/images/105855159d47ed6063ac46dfb8579b5ec64d8899282668a3de65d474561ca1d2.jpg)  
Increased Personalization & Complexity  
Fig. 10. The current and emerging mobile health applications

An example of an advanced application is shown in Fig. 11. This application monitors the medication consumption and keeps track of when the patient took doses and also informs designated set of people [77]. Such high-level solutions can be expanded, implemented and tested for usefulness, adoption and post-adoption studies as part of mobile health. This is an example of m-health where some parts, such as medication reminders, can be automated and some parts where complex decisions have to be made using clinical knowledge and experience, such as decision on changing medications based on strange side effects, will need to be human-assisted.

Another application is personalized health monitoring, where wearability, ease of use, affordability, and interoperability must be addressed [21] and systems must be safe for both the patient and the operator [13]. Many other applications will emerge from smart wearables, such as Smart Shirts. The requirements of smart health wearable are security, suitable user interface, and user acceptance [32] and effectiveness of user interface for clinically meaningful representation to the healthcare professionals [18]. The use of wearable sensors, ring sensors and watch sensors has been proposed, designed and tested for effectiveness [4,6, 43]. Ring sensors are effective for monitoring of heart rate, oxygen saturation, and heart rate variability [6] while watch sensors, as “all-in-one” system [4] for blood pressure, skin temperature, oxygen saturation, and ECG. Wearable sensors in health monitoring can be very effective [42], however the accuracy of detection can be further improved [29] and more work is needed in addressing adaptability [22]. A patientfocused algorithm for health monitoring is presented in [69] where various health conditions, the current context of the patient and current values of numerous biomedical parameters are included in decision making.

![](/api/attachments/8UCSTUPB/fulltext/images/efd5ba57ffb1e6e117d01686c1ffddeee3468a1684a3a2c30574acbee4a6a94a.jpg)  
Fig. 11. An advanced application for m-health.

## 4.1.1. Additional research opportunities

What are the most suitable applications for mobile health? How to design and evaluate applications for primary and secondary roles of mobile health in developing and developed countries? Can global applications be designed to adapt to changing roles in different places? Considering the number of applications, how to create a classi<sup>fi</sup>cation of mobile health applications?

## 4.2. Research related to patients

More research needs to be done to address how to decide suitability of possible m-health implementation as automated vs human assisted. To start with, patient's condition and severity can be considered. More indirect care with less chance of any harm to patients can be supported by automated mobile health, while the direct healthcare, such as interventions for serious conditions, can be better supported by human assisted m-health. Further, some steps of care for chronic conditions can be selectively automated, while human assistance can be better utilized for more complex steps. As mentioned before, medication reminders for patients can be automated, while to change medications and/or doses due to strange side effects can be more safely performed by healthcare professional. The impact of either or both implementations on chronic health conditions and quality of health outcomes for different set of patients can be studied.

Different patients such as children, adolescents, adults, the elderly living independently or in assisted living or nursing homes would receive and use mobile health very differently. This is due to their health conditions, attitude towards care, and knowledge and comfort with mobile technologies and healthcare applications. One of the fastest growing segments of patients is the elderly, where about 40% of US seniors, or people 65 years and older, experience one or more forms of physical and/or cognitive disabilities. The elderly experience a higher degree of fragility, have lower levels of physical strength, and may experience a degree of cognitive decline.

Both from the cost and quality of life perspectives (independent living), it is highly desirable that the elderly stay in independent homes as long as possible before moving to assisted living and then to nursing homes. One of the Grand Challenges in healthcare is to delay the transition to assisted living by 5 years [59]. To address this, more research is needed in monitoring and analyzing activities of daily living (ADL), including hygiene, food, social needs, medications, sleep, chronic conditions, and safety. The <sup>fi</sup>ve major areas for research related to the elderly are (a) fall prevention, (b) support for mobility, (c) stray prevention, (d) monitoring of dementia and (e) monitoring of daily activities. The cognitive decline for the elderly and the need for support from mobile health are shown in Fig. 12. The need for support from m-health increases as the cognitive decline increases with elderly patients moving to assisted living and then to nursing home. Decision makers will have to consider these limitations when selecting one of several m-health options to support the elderly in independent living, assisted living and nursing homes. These constraints will also lead to utilization of mobile health which is more long-term, user-centric, and highly intelligent to support the elderly as they experience cognitive and physical decline.

A high-level system for mobile health monitoring, a highly personalized and sophisticated mobile health application, is shown in Fig. 13, where the elderly can be monitored at any location (independent home, assisted living or nursing homes) using wearable (sensors or Smart Shirts) or environmental technologies (such as Smart Home) [59]. Such systems can provide a combination of automated as well as human-assisted care and can have synchronous and asynchronous operation based on the needs and condition of patients. Mobile health monitoring is one of several examples (from Fig. 11) where m-health enables overall healthcare to move from HP-controlled to HP-managed. Many important decisions can be made about their healthcare needs based on their current conditions and past history. Also, suitable interventions can be offered such as those based on motivation and support, reminders for activities and medications, and support for declining cognitive abilities among others.

The use of mobile technology and the instant attention it receives can worsen the interaction between patient and healthcare professional. More speci<sup>fi</sup>cally, the quality and length of interaction may be affected negatively. The increased automation of healthcare processes by mobile devices may affect some patients who need more interactions with healthcare professionals, especially the elderly. Any dif<sup>fi</sup>culty in use or delayed information due to infrastructure failures/malfunction may worsen the quality of care. In some cases, an increased number of false positives could lead to wasting of resources or false negatives missing the events needing certain care. The patient's comfort with various mobile technologies for healthcare could negatively impact the success of many healthcare services. Many issues of trust, physical and emotional comfort with wearable sensors and devices and embedded sensors and devices in beds, bathroom, kitchen and appliances (Fig. 14) should be studied in more details. From capabilities point of view, such smart environments and infrastructure can lead to numerous advances in mobile health for patients, however more efforts are necessary to evaluate suitability and usability of smart infrastructure for mobile health environment.

![](/api/attachments/8UCSTUPB/fulltext/images/25ac12593a36137fecc743b947ca72cf37822f1022f42f54d5acc8efb1c922c6.jpg)  
Fig. 12. Cognitive capabilities and the level of support required.

![](/api/attachments/8UCSTUPB/fulltext/images/dbf77c26f5d27c6434a3ce40b7f340c556e097e6e059767558b96f0012e541a3.jpg)  
Fig. 13. The mobile health and the elderly in multiple places.

Another major segment of patients that will play a major role in mhealth are adolescents and young adults. First these patients are not as sick as the elderly and are much more technology-aware and users. These will play an important role in accessing information and acting as a care giver for their friends and families using mobile technologies. Much more work is needed to address the needs and expectations of the adolescents and young adults by mobile health.

## 4.2.1. Additional research opportunities

How to include the conditions of patients and their level of technology literacy in designing suitable m-health applications and technologies? What are the most suitable interventions for adherence with medications and treatment for different patient demography? How can mobile health support independent living for the elderly for ten additional years and save \$500K per person? What are the most suitable applications for the adolescents and young adults? How to facilitate the need of these to play the role of caregivers to their friends and family members?

## 4.3. Research related to healthcare professional

Mobile health could also lead to several challenges due to its inherent nature, its reliance on mobile technologies, and how healthcare professionals and people interact with mobile technologies. As m-health enables healthcare services to move from HP-controlled to HPmanaged, healthcare professionals will need to make serious adjustments in their roles as m-health evolves. More research is needed to address the changing roles of healthcare professionals in terms of what care can be automated and what care must remain human-assisted, how healthcare professionals will deal with “empowered” patients with instant and mobile access to latest healthcare knowledge, and both complexity and usability challenges of mobile health. More work is also needed to address roles of healthcare professionals with mobile health in emergency care, such as those supported by RFID, sensors and mobile devices, and their abilities to handle potential side and/or negative effects of mobile technologies. In some sense, m-health may further increase the technology competence required for healthcare professionals.

![](/api/attachments/8UCSTUPB/fulltext/images/adf2811e1a02ac48fc6cc32cbaebe08c3cc86bab8d20177788cbdc779af74a4b.jpg)  
Fig. 14. Sensors and smart infrastructure.

With mobile health, one of the major challenges faced by healthcare professionals is the presence of “empowered” patients. On one hand, such patients will not need to be educated about healthcare; however their attitude and knowledge of healthcare may interact with the healthcare professionals' decision making. Many healthcare professionals may not enjoy these “empowered” patients. Certainly, much work is needed to study the complexity and quality of healthcare in m-health environment. Also, some work is needed to address the complexity in care provided to patients with differing backgrounds in m-health.

Healthcare decision making is complex in terms of number of parameters and variables, outcome possibilities, and information that must be processed and healthcare professionals need to make these complex decisions with no margins for errors. Mobile health will increase the frequency of interruptions as the healthcare professionals can be interrupted using mobile devices. The use of mobile devices on top of other medical technologies and tasks can increase the level of multitasking. Combining this with the complexity of many healthcare processes and tasks, there is some chance for an increased cognitive load, or even cognitive overload for healthcare professionals [63]. The frequent interruptions, multitasking and increased cognitive load [25,46] may result in some errors of attention and even attribution errors [55]. The situation could become more complex if the interface of mobile device is not suitable to fast reading and writing, such as poor visibility and hard to read fonts. This may lead to incorrect reading or incorrect entry of important information. Several steps can be taken to reduce cognitive load including (a) reduction of information, (b) suitable and improved presentation of information, and (c) reduction in process complexity. There are several ways to reduce the amount of information, but any such reduction is also limited by the potential for loss of critical information which may affect the quality of needed care to the patient. One of general techniques is context-awareness, where only the most relevant information along with the context is utilized [14]. This process includes <sup>fi</sup>ltering of some information based on identi<sup>fi</sup>ed relevancy, however, healthcare professionals could access such information if required for decision making. As the reduction of information is directly related to the cognitive load [55], this appears to be one promising method to reduce cognitive load of healthcare professional. As suggested by CLT [55], among the components of cognitive load, intrinsic load is in<sup>fl</sup>uenced by the inherent dif<sup>fi</sup>culty of the task. Therefore, simplifying the overall process for healthcare professionals will lead to some reduction in intrinsic load. The process simpli<sup>fi</sup>cation may be implemented in multiple ways including <sup>fi</sup>ltering of information where decisions only involve the most relevant information. Additionally, automation of several tasks in decisions for healthcare delivery could simplify the process. The prior training of healthcare professionals could help reduce “perceived” complexity of the process.

A high-level solution for decision making in healthcare using mobile device is shown in Fig. 15, which implements some of the above enhancements to reduce cognitive load [76]. Better interfaces can be developed that can adapt to cognitive capacity of decision makers or can be programmed to different healthcare professionals as needed.

## 4.3.1. Additional research opportunities

What enhancements can be made in information representation, display, and processing by mobile devices, both with small screen and not-so-small screens? Can personalization of mobile devices improve the quality and speed of decision making? How most suitable devicehuman interfaces can be designed and evaluated for different population segments? How to speed up decision-making while improving the quality of decisions and resulting health outcomes? What processes can be improved and how? How to study the effectiveness of these changes in processes? How to identify any side effects of such changes?

## 4.4. Research in information technologies

As identi<sup>fi</sup>ed in Section 2, m-health involves overcoming locational and temporal constraints and the support for mobility for patients, healthcare professionals and medical devices involved in care delivery among other things, IT and more speci<sup>fi</sup>cally, mobile computing infrastructure must support these requirements at different levels. These can range from small area mobility, such as a room, to wide-area mobility, such as a country and even a planet. The infrastructure should also support both synchronous and asynchronous versions of mobile health based on needs and availability of mobile networking resources. As mobile health will likely play a primary role in developing countries, minimal m-health requirements can be derived to ensure that network infrastructure can provide the necessary support for m-health. Infrastructure can also play in providing the needed access to healthcare information anytime anywhere and thus support the quality and speed of decision making in m-health. The infrastructure can also lead to prioritized allocation of network resources to meet different requirements of regular and emergency m-health services.

![](/api/attachments/8UCSTUPB/fulltext/images/8ee22f69c1844dfcfcbefa6977f894965b2fac6a5b804d1d2b33a8b954352d62.jpg)  
Minimize the Number of Screen Switching  
Fig. 15. Cognitive load and healthcare professionals in m-health

![](/api/attachments/8UCSTUPB/fulltext/images/91cd52f2300285519d3a802517443eedad153c1f2babebcd5851da9905806ddf.jpg)  
Fig. 16. Design and evaluation of m-health systems.

The capabilities and limitations of underlying wireless infrastructure would affect the overall experience of patients and healthcare professionals with mobile health. More work is needed in addressing several requirements of wireless infrastructure. One way is to de<sup>fi</sup>ne healthcare quality of service (H-QoS) for integrated research in healthcare infrastructure as follows.

## 4.4.1. Reliability

It can affect the ability to access information when you really need it. A major challenge for most wireless networks can be affected both by lack of network coverage as well as malfunctions of devices and failures of infrastructure components [59]. Lack of interoperability with other systems and interference can also affect the access to necessary information [23].

## 4.4.2. Access to healthcare data

To satisfy this key requirement of mobile health, the infrastructure should be able to connect patients and healthcare professionals to applications and servers and allow quick access to the desired data. This would need physical connectivity, suf<sup>fi</sup>cient bandwidth and real-time delivery or low delays. There are many high-end mobile health applications, such as ultrasound images, that will require signi<sup>fi</sup>cant bandwidth from the underlying wireless networks to meet the medical quality requirements [19].

The current 3G/4G cellular wireless networks can provide physical connectivity based on the location and network coverage of patients and healthcare professionals, but bandwidth limitations could affect real-time access to healthcare data and applications [59]. Wireless LANs can provide bandwidth, but real-time delivery or low delay access is a limitation. Infrastructure components can be strategically placed to support mobile healthcare applications in terms of coverage and data capacity [49].

## 4.4.3. Support for mobile devices and sensors

The mobile health environment is likely to involve heterogeneous mobile devices and sensors. Work is needed in supporting a range of mobile devices with their characteristics and limitations. More work is needed in improving medical usability of sensors and mobile devices including how medical information can be best represented on mobile devices. Additionally, research is needed to address level of discomfort in data collection and the design of user-friendly interface for the elderly [23].

## 4.4.4. Network and location management

Mobile health can be supported by multiple different networks such as cellular networks, wireless LANs [65], satellites and ad hoc networks [60]. Further, several wireless networks will need to work together as patient's information can be collected by sensors, then transmitted using Bluetooth network to a mobile device, which can then use a 3G/ 4G wireless network [50]. Therefore, some research is also needed in creating integration of wireless solutions.

M-health systems can be designed and evaluated using the approach shown in Fig. 16, where various kernel theories, such as cognitive load theory and health promotion model, can be used to derive requirements for m-health systems. These requirements can then be used in the design and evaluation of m-health systems, which can then in<sup>fl</sup>uence the kernel theories.

## 4.4.5. Additional research opportunities

How to enable and enhance the existing infrastructure for mobile health? Are software, hardware and networking enhancements suf<sup>fi</sup>- cient to provide reliable and quick access to the information anywhere anytime? How to design smart mobile-health applications to overcome varying limitations of infrastructure and provide the same experience to the patients and healthcare professionals?

## 5. Conclusions

Mobile health is an emerging area of research and has attracted some attention from different segments of healthcare, technology and management research. One of the goals of this paper is to integrate many of these advances and also identify some important research problems. We presented a framework for mobile health with four categories of patients, healthcare professionals, IT and m-health applications. Then we presented a research framework to discuss many important and emerging research problems in m-health. As much as we are tempted, we do not label our framework as comprehensive and the <sup>fi</sup>nal word in mobile health which is still an emerging area of research and can evolve in many different directions. There are some limitations of the proposed framework including its limited focus on four categories. A highly desirable extension of the framework could include additional categories of (a) regulatory environment and security and (b) adoption of mobile health. We expect that other researchers will expand the proposed framework to include these additional categories while identifying numerous research problems.

Mobile health can further lead to many important advances in healthcare and information technologies. These are proactive health and wellness management, where chronic conditions can be detected and managed much before any major complications, design and use of medications that are most suited to individual patients, healthcare systems that are context aware to provide necessary interventions as needed for health and medications, smart technologies that can sense and support the needs of the elderly in independent living. Personalized and intelligent monitoring of patients can lead to better health outcomes at a lower healthcare cost. It is our hope that this paper leads to more research in identi<sup>fi</sup>ed areas and, the proposed framework and high-level solutions are useful in furthering progress in this important and emerging area.

## Appendix A. Research outlets, impact of m-health

Mobile Health  
![](/api/attachments/8UCSTUPB/fulltext/images/99d87bfd7ad7a9f5bbba252a611d824dc2d41367f2ab53d2a3ffa78a111b3240.jpg)  
Fig. A1. Mobile health research areas, activities and possible outlets.

Table A1  
The impact of m-health at different levels.

<table><tr><td>The level</td><td>Impact (issues &amp; challenges)</td><td>Comments</td></tr><tr><td>Individual level (patient)</td><td>Major impact (adherence, how the care is received, information on healthcare)</td><td>A majority of work in m-health is focusing on the patients</td></tr><tr><td>Team level (care giver, healthcare professionals)</td><td>Major impact (efficiency, quality and speed of delivery of care, reduction in cost)</td><td>Some work in m-health is focusing on healthcare professionals</td></tr><tr><td>Organizational level (healthcare providers, employers, insurance, government)</td><td>Some impact (security, billing, cost, incentives, outcomes, wellness and prevention, disaster care)</td><td>Little work is being done to address organizational level impact of m-health</td></tr><tr><td>Inter-organizational level (e.g. regulator to device manufacturer)</td><td>Less impact (security and privacy of communications and information exchange, partnerships for m-health, regulatory changes)</td><td>Little work is being done to address inter-organizational level impact of m-health</td></tr></table>

## References

[1] D.L. Abraham, I. Junglas, B. Ives, Mobile technology at the frontlines of patient care: understanding <sup>fi</sup>t and human drives in utilization decisions and performance, Decision Support Systems 46 (3) (February 2009) 634–647.

[2] E. Alasaarela, N.S. Oliver, Wireless solutions for managing diabetes: a review and future prospects, Technology and Health Care 17 (5-6) (December 2009) 353–367.

[3] O. Amft, G. Troster, Methods for detection and classi<sup>fi</sup>cation of normal swallowing from muscle activation and sound, Proceedings of First International Conference on Pervasive Computing Technologies for Healthcare (IEEE), 2006.

[4] U. Anliker, J. Ward, P. Luckowicz, AMON: a wearable multiparameter medical monitoring and alert system, IEEE Transactions on Biomedical 8 (4) (December 2004) 415–427.

[5] D. Apiletti, E. Baralis, G. Bruno, T. Cerquitelli, Real-time analysis of physiological data to support medical applications, IEEE Transactions on Biomedical 13 (3) (May 2009) 313–321.

[6] H. Asada, P. Shaltis, A. Reisner, S. Rhee, R. Hutchinson, Mobile monitoring with wearable photoplethysmographic biosensors, IEEE Engineering in Medicine and Biology Magazine 22 (3) (May-June 2003) 28–40.

[7] CDC Website on Chronic Diseases, http://www.cdc.gov/chronicdisease/index.htm 2011.

[8] C.V. Chan, D.R. Kaufman, A technology selection framework for supporting delivery of patient-oriented health interventions in developing countries, Journal of Biomed ical Informatics 43 (2) (April 2010) 300–306.

[9] S. Chatterjee, S. Chakraborty, S. Sarker, S. Sarker, F.Y. Lau, Examining the success factors for mobile work in healthcare: a deductive study Decision Support Systems 46 (3)(Feb 2009) 620–633

[10] A. Cohen, Evidence-based medicine, the essential role of systematic reviews, and the need for automated text mining tools, Proceedings of the 1st ACM International Health Informatics Symposium (IHI-2010), 2010.

[11] J.M. Corchado, J. Bajo, Y. Paz, D.I. Tapia, Intelligent environment for monitoring Alzheimer patients, agent technology for health care, Decision Support Systems 44 (2) (January 2008) 382–396.

[12] J. Dai, X. Bai, Z. Yang, Z. Shen, D. Xuan, Mobile phone-based pervasive fall detection, Personal and Ubiquitous Computing 14 (7) (October 2010) 633–643.

[13] U. Edström, J. Skönevik, T. Bäcklund, J. Karlsson, A <sup>fl</sup>exible measurement system for physiological signals in mobile health care, Proc. 27th Annual International Conference of JEEE Eng, Med, Biol, Soc 2005 pp. 2161–2162

[14] J. Favela, M. Rodriguez, A. Preciado, V.M. Gonzalez, Integrating context-aware public displays into a mobile hospital information system, IEEE Transactions on Information Technology in Biomedicine 8 (3) (2004) 279–286.

[15] S. Helal, W. Mann, H. Zabadani, J. King, Y. Kaddoura, E. Jensen, The Gator Tech smart house: a programmable pervasive space, IEEE Computer 38 (3) (March 2005) 64–74.

[16] Y. Hu, A. Stoelting, Y.-T. Wang, Y. Zou, M. Sarrafzadeh, Providing a cushion for wireless healthcare application development, IEEE Potentials (Jan/Feb 2010) 19–23.

[17] S. Intille, A new research challenge: persuasive technology to motivate healthy aging, IEEE Transactions on Information Technology in Biomedicine 8 (3) (September 2004) 235–237.

[18] R. Isais, K. Nguyen, G. Perez, R. Rubio, H. Nazeran, A low-cost microcontroller-based wireless ECG-blood pressure telemonitor for home care, Proceedings of the 25th Annual International Conference of the IEEE Engineering in Medicine and Biology Society 2003 pp. 3157–3160

[19] R.S.H. Istepanian, N.Y. Philip, M.G. Martini, Medical QoS provision based on reinforcement learning in ultrasound streaming over 3.5G wireless systems, IEEE Journal on Selected Areas in Communications 27 (4) (May 2009) 566–574

[20] JAMA Abstract, Estimating hospital deaths due to medical errors, Journal of American Medical Association 286 (4) (July 2001) (http://jama.ama-assn.org/ issues/y286n4/rfull/ioc02235.html#abstract )

[21] Y. Jianchu, R. Schmitz, S. Warren, A wearable point-of-care system for home use that incorporates plug-and-play and wireless standards, IEEE Transactions on Information Technology in Biomedicine 9 (3) (September 2005) 363–371.

[22] S. Junnila, H. Kailanto, J. Merilahti, A.-M. Vainio, A. Vehkaoja, M. Zakrzewski, J. Hyttinen, Wireless, multipurpose in-home health monitoring platform: two case trials, IEEE Transactions on Biomedical 14 (2) (March 2010) 447–455.

[23] A. Kailas, C. Chong, F. Watanabe, From mobile phones to personal wellness dashboards, IEEE Pulse 1 (1) (July/August 2010) 57–63.

[24] J. Kang, T. Yoo, H. Kim, A wrist-worn integrated health monitoring instrument with a tele-reporting device for telemedicine and telecare, IEEE Transactions on Instrumentation and Measurement 55 (5) (Oct 2006) 1655–1661.

[25] A. Laxmisan, F. Hakimzada, O. Sayan, R. Green, J. Zhang, V. Patel, The multitasking clinician: decision-making and cognitive demand during and after team handoffs in emergency care, International Journal of Medical Informatics 76 (11) (2007) 801–811.

[26] LifeShirt, available at http://www.vivometrics.com/site/system.html

[27] B. Lin, N. Chou, F. Chong, S. Chen, RTWPMS: a real-time wireless physiological monitoring system, IEEE Transactions on Information Technology in Biomedicine 10 (4) (October 2006) 647–656.

[28] C. Lin, M. Chiu, C. Hsiao, R. Lee, Y. Tsai, A wireless healthcare service system for elderly with dementia JEEE Transactions on Information Technology in Biomedicine 10 (2) (October 2006) 696–704.

[29] C.-T. Lin, et al., An intelligent telecardiology system using a wearable and wireless ECG to detect atrial <sup>fi</sup>brillation, IEEE Transactions on Biomedical 14 (3) (May 2010) 726–733.

[30] S.-P. Lin, Determinants of adoption of mobile healthcare service, International Journal of Mobile Communications 9 (3) (June 2011) 298–315.

[31] C. Liu, Q. Zhu, K.A. Holroyd, E.K. Seng, Status and trends of mobile-health applications for iOS devices: a developer's perspective, Journal of Systems and Software 84 (11) (November 2011) 2022–2033.

[32] A. Lymberis, Smart wearable systems for personalised health management: current R&D and future challenges, Proc. 25th Annual International Conference of IEEE Eng. Med. Biol. Society, 2003, pp. 3716–3719.

[33] M. Mackert, B. Love, P. Whitten, Patient education on mobile devices: an e-health intervention for low health literate audiences, Journal of Information Science 35 (1) (Feb 2009) 82–93.

[34] N. Mahmud, J. Rodriguez, J. Nesbit, A text message-based intervention to bridge the healthcare communication gap in the rural developing world, Technology and Health Care 18 (2) (May 2010) 137–144.

[35] J. Maitland, S. Sherwood, L. Barkhuus, I. Anderson, M. Hall, B. Brown, M. Chalmers, H. Muller, Increasing the awareness of daily activity levels with pervasive computing, Proceedings of First International Conference on Pervasive Computing Technologies for Healthcare (IEEE), 2006.

[36] M. Makeham, S. Dovey, M. County, M. Kidd, An international taxonomy for errors in general practice: a pilot study, Medical Journal of Australia 177 (July 15th 2002) 68–72.

[37] W. Michalowski, S. Rubin, R. Slowinski, S. Wilk, Mobile clinical support system for pediatric emergencies, Decision Support Systems 36 (2) (2003) 161–176.

[38] T. Mitsa, P.J. Fortier, A. Shrestha, G. Yang, N.M. Dluhy, E.S. O'Neill, Information systems and healthcare XXI: a dynamic, client-centric, point-of-care system for the novice nurse, Communications of the Association for Information Systems 19 (36) (2007).

[39] J. Moller, H. Vosegaard, Experiences with electronic health records, IEEE IT Professional 10 (2) (March-April 2008) 19–23.

[40] M. Ogawa, T. Togawa, The concept of home health monitoring, Proc. of 5th International Workshop on Enterprise Networking and Computing in Healthcare (Healthcom), 2003.

[41] N. Oliver, L. Kreger-Stickles, Enhancing exercise performance through real-time physiological monitoring and music: a user study, Proceedings of First International Conference on Pervasive Computing Technologies for Healthcare (IEEE), 2006.

[42] A. Pantelopoulos, N.G. Bourbakis, A survey on wearable sensor-based systems for health monitoring and prognosis, IEEE Transactions on Systems, Man, and Cybernetics Part C: Applications and Reviews 40 (1) (January 2010) 1–12.

[43] R. Paradiso, G. Loriga, N. Taccini, A wearable health care system based on knitted integrated sensors, IEEE Transactions on Biomedical 9 (3) (September 2005) 337-344

[44] E. Park, H.S. Nam, A service-oriented medical framework for fast and adaptive information delivery in mobile environment, IEEE Transactions on Biomedical 13 (6) (November 2009) 1049–1056

[45] J. Parkka, M. Ermes, P. Korpipaa, J. Mantyjarvi, J. Peltola, I. Korhonen, Activity classi-<sup>fi</sup>cation using realistic data from wearable sensors, IEEE Transactions on Information Technology in Biomedicine 10 (1) (Jan 2006) 119–128.

[46] V. Patel, J. Zhang, N.A. Yoskowitz, R. Green, O.R. Sayan, Translational cognition for decision support in critical care environments: a review, Journal of Biomedical Informatics 41 (3) (2008) 413–431.

[47] P.A. Prociow, J.A. Crowe, Towards personalised ambient monitoring of mental health via mobile technologies, Technology and Health Care 18 (4-5) (November 2010) 275–284.

[48] J. Pollak, G. Gay, S. Byrne, E. Wagner, D. Retelny, L. Humphreys, It's time to eat! Using mobile games to promote healthy eating, IEEE Pervasive Computing 9 (3) (July-Sept 2010) 21–27.

[49] N. Pongthaipat, J. Kabara, Designing wireless networks to support data rate require ments of healthcare systems, Proceedings of First International Conference on Pervasive Computing Technologies for Healthcare (IEEE), 2006

[50] M. Rasid, B. Woodward, Bluetooth telemedicine processor for multichannel biomedical signal transmission via mobile cellular networks IFFE Transactions on Informa: tion Technology in Biomedicine 9 (1) (March 2005) 35–43.

[51] R. Scheepers, H. Scheepers, O.K. Ngwenyama, Contextual in<sup>fl</sup>uences on user satisfaction with mobile computing: findings from two healthcare organizations, European Journal of Information Systems 15 (3) (June 2006) 261–268.

[52] M. Spenko, H. Yu, S. Dubowsky, Robotic personal aids for mobility and monitoring for the elderly, IEEE Transactions on Nuclear Systems Rehabilitation Engineering 14 (3) (September 2006) 344–351.

[53] V. Stanford, Using pervasive computing to deliver elder care, IEEE Pervasive Computing 1 (1) (Jan-March 2002) 10–13.

[54] D. Stefanov, Z. Bien, W. Bang, The smart house for older persons and persons with physical disabilities: structure, technology, arrangements, and perspectives, IEEE Transactions on Neural Systems and Rehabilitation Engineering 12 (2) (June 2004) 228–250.

[55] J. Sweller, Cognitive load during problem solving: effects on learning, Cognitive Science 12 (2) (1988) 257–285.

[56] C. Tsai, G. Lee, F. Raab, G. Norman, T. Sohn, W. Griswold, K. Patrick, Usability and feasibility of PMEB: a mobile phone application for monitoring real time caloric balance, Proceedings of First International Conference on Pervasive Computing Technologies for Healthcare, 2006.

[57] M. Turunen, et al., Multimodal and mobile conversational health and <sup>fi</sup>tness companions, Computer Speech and Language 25 (2) (April 2011) 192–209.

[58] US Institute of Medicine (IOM) Report, To err is human: building a safer, health system.http://www.nap.edu/books/0309068371/html/

[59] U. Varshney, Pervasive Healthcare Computing: EMR/EHR, Wireless and Health Monitoring, Springer, New York, 2009.

[60] U. Varshney, S. Sneha, Patient monitoring using ad hoc wireless networks: reliability and power management, IEEE Communications Magazine 44 (4) (April 2006) 49–55.

[61] R. Walton, B. Derenzi, Value-sensitive design and health care in Africa, IEEE Transactions on Professional Communication 52 (4) (December 2009) 325–328.

[62] WelchAllyn Monitoring Devices, http://www.monitoring.welchallyn.com/products/ wireless 2011.

[63] M. Workman, M. Lesser, J. Kim, An exploratory study of cognitive load in diagnosing patient conditions, International Journal for Quality in Healthcare 19 (3) (2007) 127–133.

[64] H. Ying, et al., Distributed intelligent sensor network for the rehabilitation of Parkinson's patients, IEEE Transactions on Biomedical 15 (2) (March 2011) 268–276.

[65] Y. Zhang, N. Ansari, H. Tsunoda, Wireless telemedicine services over integrated IEEE 802.11/WLAN and IEEE 802.16/WiMAX networks, IEEE Wireless Communications (Feb 2010) 30–36.

[66] F. Zhu, M. Bosch, I. Woo, S.Y. Kim, C.J. Boushey, D.S. Ebert, E.J. Delp, The use of mobile devices in aiding dietary assessment and evaluation, IEEE Journal of Selected Topics in Signal Processing 4 (4) (August 2010) 756–766.

[67] J.P. Shim, M. Warkentin, J. Courtney, D.J. Power, R. Sharda, C. Carlsson, Past, present, and future of decision support technology, Decision Support Systems 33 (2) (2002).

[68] S. Sneha, U. Varshney, Enabling ubiquitous patient monitoring: model, decision protocols, opportunities and challenges, Decision Support Systems 46 (3) (2009).

[69] U. Varshney, A framework for supporting emergency messages in wireless patient monitoring, Decision Support Systems 45 (4) (2008).

[70] O.B. Kyon, N. Sadeh, Applying case-based reasoning and multi-agent intelligent system to context-aware comparative shopping, Decision Support Systems 37 (2004).

[71] P. Ahluwalia, U. Varshney, Composite quality of service and decision making perspectives in wireless networks, Decision Support Systems 46 (2009).

[72] T.C. Du, E.Y. Li, E. Wei, Mobile agents for a brokering service in the electronic marketplace, Decision Support Systems 39 (2005).

[73] E.W.T. Ngai, A. Gunasakaran, A review for mobile commerce research and applications, Decision Support Systems 43 (2007).

[74] I. Bose, X. Chen, A framework for context sensitive services: a knowledge discovery based approach, Decision Support Systems 48 (2009)

[75] R. Nickerson, U. Varshney, J. Muntermann, A method for taxonomy development and its application in information systems, European Journal on Information Systems 22 (3) (2013).

[76] U. Varshney, Mobile computing for healthcare: two enhancements, Decision Support Systems (2014) (Accepted for publication).

[77] U. Varshney, Smart medication management system and multiple interventions for medication adherence, Decision Support Systems 55 (2) (2013)

Upkar Varshney is currently an Associate Professor of Computer Information Systems at Georgia State University, Atlanta. His current interests include mobile health, pervasive computing, and wireless networks. He has authored over 175 papers including 70 in national and international journals. He is the author of Pervasive Healthcare, published by Springer in 2009 and 2010. According to Google Scholar, his papers have been cited more than 4600 times

He is the founding co-chair of International Pervasive Health Conference and was the program co-chair for Americas Conference on Information Systems (AMCIS-2009).

He has served or is serving as an editor for IEEE Transactions on IT in Biomedicine, IEEE Access MegaJournal, ACM/Springer Mobile Networks (MONET) and Int. Journal on Interdisciplinary Telecom and Networking. He is also serving as Senior Editor for Decision Support Systems (DSS) and IEEE Computer
