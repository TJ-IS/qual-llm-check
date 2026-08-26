---
otero_id: 12188
otero_key: "2XD78T72"
title: "Cyber-analytics: Modeling factors associated with healthcare data breaches"
authors: "Alexander McLeod; Diane Dolezel"
year: "2018"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.02.007"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Cyber-analytics: Modeling factors associated with healthcare data breaches☆

Alexander McLeod ⁎, Diane Dolezel

Health Information Management Department, College of Health Professions, 601 University Drive, Texas State University, San Marcos, TX 78163, USA

## a r t i c l e i n f o

Article history: Received 14 August 2017 Received in revised form 17 February 2018 Accepted 17 February 2018 Available online xxxx

Keywords: Security Cyber security Cyber risk Data breach Risk management Exposure Vulnerability assessment Level of exposure Level of security Security modeling Cyber-analytics

## a b s t r a c t

The purpose of this study was to develop a model of factors associated with healthcare data breaches. Variables were operationalized as the healthcare facilities' level of exposure, level of security, and organizational factors. The outcome variable was the binary value for data breach/no data breach. Because healthcare data breaches carry the risk of personal health information exposure, corruption or destruction, this study is important to the healthcare field. Data were obtained from the Department of Health and Human Services database of healthcare facilities reporting data breaches and from a large national database of technical and organizational infrastructure information. Binary logistic regression was utilized to examine a representative data breach model. Results indicate several exposure, security and organizational factors significantly associated with healthcare data breaches. © 2018 Elsevier B.V. All rights reserved.

## 1. Introduction

Preventing healthcare data breaches is hard. Connected healthcare systems necessitate information exchange across multiple devices and platforms, increasing the level of exposure and security risk, exposing the organization to potential data breaches. Patient data may be corrupted, stolen or modified by intrusive cyber agents, causing patients harm when data is used to obtain medical treatment or when the patient's stolen data is used for identity theft [1].

The organization may suffer disruption of services, incur significant costs, and face the possibility of litigation [2]. Moreover, Federal laws mandate heavy penalties for facilities whose negligence contributes to data breaches. For example, New York Presbyterian (NYP) Hospital was fined 3.3 million dollars for the Internet disclosure of 6800 patients' data due to their improperly configured web servers and lax policies for granting database access [3]. In a related lawsuit, Columbia University paid a 1.5 million dollar fine for failing to conduct appropriate risks analyses on IT equipment used to connect to the NYP database servers.

Breach detection is another concern. Although Federal laws dictate that patients be notified of breaches within 60 days, discovery of data breaches may not occur for some time causing a significant lag time in event reporting [4]. Reporting lag time was evident when a cancer center data breach remained undetected for several months, and patients affected by the breach were not notified until five months after it was detected allowing malicious agents to scrutinize the data of 22,000 patients [5].

At the time of this writing in 2017, a record number of breaches had occurred including an employee responding to a phishing email with login credentials [6], successful hacking efforts by the Dark Overlord [7] and a multitude of various WannaCry ransomware encryptions [8]. While only 18 data breaches were reported in the last quarter of 2009, there were 351 data breaches reported during the first half of 2017 – almost two breaches per day! Fig. 1 reports the number of healthcare data breaches by category for the years 2009–2017 as presented in the Department of Health Human Services (DHHS) data breach report for breaches affecting over 500 people [9].

Encrypting data is necessary but not sufficient to prevent data theft. Most data breaches are reported as lost or stolen devices, indicating a lack of physical security for devices. Device loss may also reflect weak security plans (e.g. not physically securing laptops) or inadequate security training of employees. The bottom line is that healthcare institutions remain vulnerable targets for a wide range of cyber threats including technical, physical and human issues [11–13].

Cyber perpetrators continue to exploit these vulnerabilities with increasing sophistication, capitalizing on stolen healthcare records [14,15].

There are many negative effects caused by data breaches impacting uninvolved populations, organizational assets and the healthcare environment in general. Because of the vulnerability of healthcare organizations and the many negative consequences for those experiencing a data breach [16], this work examined factors associated with data breach occurrences. The topic is important because healthcare data breaches expose personal data to theft, modification or misuse [17]. By exploring data breach factors, this paper helps healthcare organizations develop cyber profile models to test associations of data breach occurrence.

![](/api/attachments/2XD78T72/fulltext/images/d3649635846d4762596eefa4f58118a1b78aed9a81d3f7e6a8f1907c6df8156a.jpg)  
Fig. 1. DHHS reported data breaches [10].

## 2. Background

Securing personal health information has been the focus of many important healthcare laws, security frameworks and national computing initiatives. In 2013, then President Barack Obama signed Executive Order 13636: Improving Critical Infrastructure Cybersecurity requiring the National Institute of Standards and Technology (NIST) to develop a Cybersecurity Framework to help manage cyber risk [18]. To provide guidance on best practices for public and private cybersecurity programs, NIST was mandated to create a Cybersecurity Framework [19]. Subsequently, the Department of Homeland Security (DHS) assumed the Federal government's lead in securing the nation's critical infrastructure, which includes monitoring Healthcare and Public Health components of the Cyber Security infrastructure. In 2016, the Commission on Enhancing National Cybersecurity was established to provide recommendations for raising security awareness for electronically stored public and private data [20]. These federal organizations set requirements for healthcare facilities, mandating data breach reporting and enforcing best practices.

## 2.1. Health Insurance Portability and Accountability Act

The Health Insurance Portability and Accountability Act (HIPAA) [21] mandates that covered entities notify the DHHS when personal health information has been breached. Breach notification is also required for vendors and third-party service providers under the Health Information Technology for Economic and Clinical Health Act (HITECH) [22]. “A breach is, generally, an impermissible use or disclosure under the Privacy Rule that compromises the security or privacy of the protected health information [23].” Following a breach, covered entities must notify individuals affected by the breach, the Secretary of the DHHS and sometimes the media. If a breach involves 500 or more individuals, entities discovering the data breach must notify the Secretary via the DHHS website. This requirement enables administrative review of previously unknown occurrences and provides some sense of the scale and frequency of healthcare data breaches.

Per the HIPAA Security Rule, healthcare facilities must implement a risk management plan that protects the confidentiality, integrity and security of all data that they create, maintain, receive or transmit. They must provide protection against security incidents for personal health information used for provisioning patient care [24]. In this context, a security incident is defined as the “attempted or successful unauthorized access, use, disclosure, modification, or destruction of information or interference with system operations in an information system” [25].

The HIPAA Security Rule does not specify what methods or processes when analyzing risk. Healthcare organizations must create their own plan. Many organizations assign a risk level to each anticipated risk, based on the probability of the loss occurring, allowing them to prioritize risks. This is important because realistically all risks cannot be addressed. The disadvantage of this facility-specific approach is that there is no standard way to ensure compliance with HIPAA requirements. Some guidance can be found in the HIPAA implementation plan from NIST [26] and the Office for Civil Rights (OCR) annual guidance on the security rule [27].

## 2.2. Risk management

At a minimum, a facility must have procedures to detect and report all breaches within 60 days of discovery, as required by the OCR. Failing to do so will subject the facility to financial penalties. Penalties to date have been substantial. The first HIPAA enforcement for lack of timely breach notification was a \$475,000 penalty paid by Presence Healthcare [28]. Explicitly, a breach of paper operating room schedules with the personal health information of 836 individuals occurred on October 22, 2013. It was not reported to OCR until January 31, 2014, which is well over the mandatory 60 day reporting period [28].

An associated issue is that the number of data breaches may be under reported. It has been postulated that facilities are considering encryptions as security incidents, which do not involve accessing personal health information, instead of the more serious data breach of personal health information [29]. In reality, facilities should refer to OCR guidelines on encryptions [30] and assume a data breach has occurred unless they have proof that personal health information was not compromised. E.g. ransomware encryptions were reported by over 50% of all hospitals between April 2015 and April 2016, and an additional 25% admitted they had no way to tell if they had been compromised [31]. Although, this translates into 4000 encryption attacks in 2016, a 300% increase over 2015, only nine such intrusions were reported to OCR [32].

## 3. Literature review

A review of the extant literature from areas related to risk management and health care security focused on events and factors related to data breaches, breach occurrences and breach risk areas. This review underscores the scarcity of healthcare data breach models that examine factors related to breaches and found none that examined data for the timeframe included in our study. Thus, this paper adds to the body of knowledge on data breach modeling by providing more current insights into the factors associated with healthcare data breaches.

In every healthcare organization, there exist factors which influence the potential for a data breach. These factors may be categorized by examining the associated information systems, business processes and organizational factors unique to the facility [33]. When contemplating the factors associated with an incident, Liginlal et al. [34] suggested that accidents occur due to a series or chain of events rather than a single cause of failure. Thus, all technological factors, business processes and organizational influences are potential causes of a data breach. Fig. 2 shows how this chain of events is associated in the organization.

## 3.1. Technological factors

A variety of technological innovations are commonly used to track patients, specimens, materials, patient records, and for radiology report generation [35]. Barcodes are typically required on drugs, blood and blood products [36] and often they are used for data entry into Electronic Health Records (EHR) and Electronic Medical Records (EMR). Although the adoption of barcoding in healthcare is generally seen as beneficial [37], especially in reducing medication errors, there are many security issues. First, bar code readers are often hand held wireless devices which may connect to the nearest network router or via Bluetooth to the clinician's wireless workstation. They may be used to issue medication, fluid administration or other clinical functions. The wireless connectivity of these devices has notably low security and a history of default password usage [38]. Adding to these vulnerabilities, free bar code readers are available for use on consumer's smart phones or employees' unsecured BYOD devices. In addition, there is the added burden of evaluating the bar code vendors' security practices for compliance with facility standards.

Barcoding implementation may also raise concerns. Lack of adequate requirements planning, lack of polices for bar code use, poor integration with existing systems and staff frustration due to bar code equipment issues have led to barcode misuse in hospitals [39]. In one case, a patient with no diabetic history was given the wrong bar coded wristband, and was almost administered a fatal dose of insulin [40]. The mix-up of patients' personal health information suggests a need for barcoding lab labels from other HIS systems instead of from the patient's wristband, and for two identifiers when issuing the wristband and before lab tests. In a second case, nurses perceived that bar code scanning was taking too long went back to typing in the codes [40]. When users are misusing and circumventing the system, this raises security concerns. Thus, bar coding vulnerabilities raise questions with regard to data breaches.

The Center for Medicare and Medicaid (CMS) Meaningful Use Stage 1 and 2 criteria, designed to encourage use of certified EHRs and Clinical Decision Support Systems (CDSS) to reduce medication errors, requires the use of Computerized Physician Order Entry (CPOE) [41]. Leapfrog Group reports on CMS Meaningful Use attestations for CMS stages and CPOE usage. As previously mentioned, CPOE and CDSS use raise security concerns due to their increased data exposure [42].

Participation in health information exchange (HIE) initiatives was also considered given the increase in data sharing. Organizations that engaged in HIEs have greater data exposure and must consider business associates' services, such as cloud hosting, that can pose additional risks. For example, Harrisburg Gastroenterology announced a hacking data breach involving 93,323 patient records on a network server [43]. If data is stored on an external cloud server, the health facility needs to understand the cloud vendors' level of security and prepare for potential data breaches.

Human readable data is hard to secure. The Continuity of Care Document (CCD) document, based on the HL7 Clinical Data Architecture (CDA) architecture, contains information critical to patient care [44]. CDA facilitates data transmission for patient care transfers. Regrettably, the CCD data in is human readable form (XML), that can be read with a web browser, and it is technology neutral. Thus, it can be shared electronically or by giving the patient or caregiver a paper copy.

Biometrics technology is popular, but surprisingly easy to hack. Biometrics identifiers are something unique to you, they include fingerprints, retina scans, voices, face or hand prints have used for system access [45]. In 2013, a fingerprint smudge on an iPhone screen was used to hack the iPhone 5S biometric security [46]. And a high definition picture has been used to create a recognizable fingerprint. Some biometric attacks have special names. The “Man in the Middle” attack uses a recording, your voice for example, to gain access [47], and the “Hill Climbing Attack” that successively changes an image until the biometric system recognizes it. We considered measures related to bar coding, clinical decision system integration, certified electronic health

![](/api/attachments/2XD78T72/fulltext/images/4f52f8fc28af563f71e6b1366491954c3a9163240f912eb5b67ddf08cfd7c193.jpg)  
Fig. 2. NIST strategic/tactical security risk triangle

Please cite this article as: A. McLeod, D. Dolezel, Cyber-analytics: Modeling factors associated with healthcare data breaches, Decision Support Systems (2018), https://doi.org/10.1016/j.dss.2018.02.007

A. McLeod, D. Dolezel / Decision Support Systems xxx (2018) xxx–xxx

record, biometric and health information exchange use as security indicators.

## 3.2. Business process factors

In a data breach case study involving Kaiser Permanente [48], researchers completed a root cause analysis citing multiple reasons for the breach involving people, processes and technology. Furthermore, they recommended compliance with quality information security practices and regulations while following HIPAA guidelines. In this case study, it was established that the data breaches occurred due to a chain of events rather than a single cause of failure [34]. Business processes were assessed for breach potential. Of late, the ubiquitous use of the Internet of Things has increased vulnerabilities by exposing more medical devices [49]. For instance, the increased use of connected healthcare systems, such as dashboards, EMRs (used by individual providers), and CPOEs, enables tracking of record exposure and breaches, but it also increases data exposure [42]. The importance of considering consumer dashboards as a threat is illustrated by Molina Healthcare who reported a data breach via its patient portal on May 26, 2017 involving a “security flaw” that exposed patient healthcare data [50]. In contrast, EMRs are used in a clinician's office for diagnosis and treatment and are not designed for sharing [51]. But, the EMR exposure threat comes from the numerous mobile users and wireless technologies presenting numerous opportunities for hackers [52,53].

Consider Computerized Physician Order Entry (CPOE) systems, which are point of care Clinical Decision Support Systems (CDSS) used for entering medication or lab orders that transmit seamlessly to an EHR [54]. They are necessary for evidenced-based practices [55]; however adoption of these systems can increase exposure risks [56] as they are often used by affiliated users who are not permanent employees and may be remotely accessed from outpatient settings. Because of concerns about these systems and the texting of orders to a CPOE from unsecured personal mobile devices, the Joint Commission initially disallowed texting. Many EHRs simply lacked secure messaging components [57], or authentication making it difficult to determine the identity of the (hopefully authorized) text message sender [58].

Provisioning care in an intensive care unit (ICU) neonatal intensive care unit (NICU) or a trauma emergency area requires utilizing many medical and wireless devices, often with real-time monitoring and dashboards, each presenting a data entry point. A special concern is that many wireless devices and routers retain original manufacturer passwords and business processes are not in place to secure these systems. Hospital growth and scaling of the ICU and NICU by increasing the number of intensive care beds or the number of outpatient visits increases data exposure risks. Proactive organizations often test these areas using penetration testing to determine weaknesses in systems and networks [59].

## 3.3. Organizational factors

Many organizational characteristics may influence data breaches. We considered those indicating size such as AHA admissions, number of full time employees, number of beds, number of operations, total patient days. In addition, complexity as measured by the number of births and number of surgical operations and expenditures seen in net operating revenue, payroll expense, operating expenses and year opened, added to organizational insight. For example, healthcare facilities containing obstetrical and surgical operating units have more complex systems leading to greater potential for breach. Recently, UNC Health reported a data breach of prenatal patient information that was mistakenly transmitted [60]. Surgical units are not immune to data breaches as seen in a breach involving operating rooms. Presence Health recently agreed to pay a \$475,000 fine for late reporting of lost operating room schedules which included patient names, birth dates, dates and types of procedures, medical record numbers, surgeon names and types of an esthesia [61].

Financial expenditures are important. Protecting patient data is expensive and healthcare facilities that fail to spend monies to operate a secure environment are more subject to theft [62]. Data breaches are also expensive in terms of the patients' negative perceptions of the breached facility. Specifically, the cost of an organizational data breach continues to rise and as of 2011 the average cost of a breach was \$7,200,000 [63]. We also posited that larger hospitals as indicated by more beds, births and surgeries and older hospitals those with more leg acy systems, might have more data breaches.

## 4. Related research

Accidental releases of information cause many data breaches however, there are also very large breaches which have been examined. One study of healthcare and non-healthcare industries analyzed 2633 data breaches occurring in the US during 2005–2011. These incidents resulted in loss of N500 million individual records [63]. Investigators concluded that human factors, and implementation of security policies were strongly related to an increase in data breaches. Other researchers continue to signal a need for more focused security training [64]. A later study explored IT security and data breaches from 2005 to 2013 using data from 5000 U.S. hospitals involved in 938 breaches [65]. Researchers focused on adoption of IT Security measures. Results showed that institutional factors influenced data breaches recommending that processes and workflow be tightly integrated with IT security [65].

Other relevant literature assessed cybercrime from a risk assessment and management perspective. Kraemer et al. [66] emphasized nine categories including external influences, human error, management, organization, performance and resource management, policy issues, technology, and training. Massberg and Liu [67] explored the role of organizational factors in curbing cybercrime including security policies, secure remote access, application whitelisting, restricted internet access, antivirus, firewalls, presence of plans regarding incident response, disaster recovery, business continuity, and management support. They used these measures as control variables representing the level of security when studying the relationship between information sharing and the number of breaches.

A few studies assessed organizational maturity factors related to data breaches. Zafar [68] supported constructs originally proposed by Kotulic [69] and several of these variables are suitable in data breach determination analysis. They concluded that organizational maturity may affect the number of incidents. Therefore, measures related to the age of a facility might serve as a proxy for organizational maturity.

Given the large number of healthcare data breaches and the lack of a model of breach factors, the purpose of this study was to examine healthcare organizations experiencing one or more data breaches to develop a cyber profile model of data breaches factors. This model may be of value to organizational decision making when attempting vulnerability reduction. Because healthcare organizations have limited resources, decision support concerning how to best protect against data breaches is important [70].

## 5. Theoretical framework

A review of literature provided a theoretical framework for the study. Reason's Swiss Cheese Model (SCM) depicts systems as stacked slices of Swiss cheese with each slice representing a failure level, and the holes in the slices depicting an ever changing set of vulnerabilities that occur due to operational and organizational failures [71]. When the holes line up, a causation chain forms and undesirable events are more likely to occur. The SCM model of accident causation has been applied to healthcare [72]. It was used by Kamoun and Nicho [71] to explore the data breach causation chain. Their research suggested the focus for data breaches be shifted from employee negligence to establishing organization wide preventive measures. They hypothesized that system weaknesses influenced breaches and that some of the causes included: organizational influence, inadequate security defenses, and unsafe data handling. Their six categories deemed important to prevention are: 1) employee behavior aligned with security culture [73], 2) adoption of best IT governance practices [74], 3) effective policies and procedures for handling personal health information [75], 4) ongoing security training for all employees [76], 5) attention to vendor selection and their handling of personal health information [77], and 6) implementing a strong risk management program. The Kaumon study differs in that they collected data from the Open Security Foundation, DHHS, Privacy Right Clearinghouse, and Big Brother Watch, using different slices.

Fig. 3 graphically shows the Swiss Cheese Model as suggested by Reason [78]. The SCM suggests that most undesirable events have multiple failure causes. Using our literature review, we operationalized our SCM slices as Organizational Factors, Level of Security and Level of Exposure.

## 6. Research questions

Given the importance of identifying the likelihood of occurrence of a data breach in a healthcare facility, the research questions for this study are:

1. Is there a relationship between the level of exposure and the likelihood of a data breach?

2. What is the relationship between the level of security and the potential of a data breach?

3. Are organizational factors associated with the likelihood of the occurrence of a data breach?

4. What is the relationships between level of organizational factors, level of exposure and level of security and the likelihood of the occurrence of a data breach?

## 6.1. Research model

Drawing on concepts from these studies and our research questions, we created constructs to independently test hypotheses related to the level of exposure, level of security and organizational effects independently as predictors of hospital data breaches. In addition, we considered a summarized model which included all three constructs.

Our hypotheses are summarized as follows:

H1. The factors related to the level of exposure will be associated with the likelihood of a data breach.

H2. The factors related to the level of security will be associated with the likelihood of a data breach.

H3. The organizational factors will be associated with the likelihood of a data breach.

H4. The combination of exposure, security and organizational factors will be associated with the likelihood of a data breach.

Fig. 4 represents the research hypotheses tested in this work.

## 7. Methodology

This retrospective study was conducted to develop a model of data breaches occurring at healthcare facilities. The study site was a large state university in the Southern United States. Data were collected from the Healthcare Information and Management Systems Society

![](/api/attachments/2XD78T72/fulltext/images/149e850f53ded4c237312bf2458dcf83f0057d8673c2d6b960f5efc08a3e96b0.jpg)  
Fig. 3. Swiss cheese model for data breach factors [78].

Please cite this article as: A. McLeod, D. Dolezel, Cyber-analytics: Modeling factors associated with healthcare data breaches, Decision Support Systems (2018), https://doi.org/10.1016/j.dss.2018.02.007

![](/api/attachments/2XD78T72/fulltext/images/501f0828aa92aa4413464138339e0de65304da5fdea865179030274f6cb77b0b.jpg)  
Fig. 4. Conceptual model of factors hypothesized to cause hospital data breaches

(HIMSS) Analytics Legacy Database and from the Department of Health and Human Services (DHHS) data breach report.

## 7.1. DHHS data breach report

Under Title 45 Code of Federal Regulations 164.408 - Notification to the Secretary, any covered health care entity discovering a breach of unsecured protected health information affecting 500 or more individuals must notify the Secretary of DHHS without unreasonable delay and in no case later than 60 days from the discover of the breach [10]. Notice must be provided electronically via the DHHS breach notification portal and these notifications are publicly available at https://ocrportal.hhs. gov/ocr/breach/breach\_report.jsf. This database was downloaded from the breach website and provided the following data fields: Name of Covered Entity, State, Covered Entity Type, Individuals Affected, Breach Submission Date, Type of Breach, Location of Breached Information, Business Associate Present, Web Description. The DHHS breach list downloaded in Spring 2017 included 1804 breach incidents.

## 7.2. HIMSS analytics legacy database

HIMSS is a voluntary healthcare facility association with the goal of transforming health through information technology [79]. A wholly owned subsidiary, HIMSS Analytics is a global healthcare IT market intelligence, research and standards organization assisting clientele in both healthcare delivery and healthcare technology solutions business development to make lasting improvements in efficiency and performance. One product available to academic researchers is the HIMSS Analytics Legacy Database comprised of responses from over 6600 healthcare organizations. The dataset is comprised of 65 tables representing technological survey responses from healthcare organizations concerning acute care, barcoding, biometric technology, CDSS, computers, connectivity, data center applications, data center facilities, Electronic Medical Record Adoption Model stage validation, entity characteristics, handheld devices, hardware information, hosted software, IE initiatives, IS plans, long term storage, medical devices, medical device interfaces, pharmacy information, supply automation, telecom information, use of IT components, wireless technology, and wireless access.

This data is useful for examining characteristics of 6600 healthcare facilities and when coupled with the DHHS breach list provides information for studying data breaches.

## 7.3. Variables

The binary dependent variable for all research questions was healthcare data breach occurrence versus no breach occurrence. The independent factors were grouped in the constructs level of exposure, level of security and organizational factors based on the literature review. Table 1 lists the variables by construct.

## 7.4. Sample assembly

Data was extracted from the HIMSS Analytics Legacy Database and the DHHS hospital breach report and imported as tables into the study database. Using Structured Query Language, the names of the facilities reporting data breaches were matched with the names in the HIMSS database possessing the hospital factors. Facility names which often presented extraneous symbols and characters were updated and corrections were validated by performing web searches and visually examining facility names and addresses.

Next, it was necessary to replace missing values for retained variables with reasonable estimates. While some researchers recommend exclusion of variables with N50% missing values, other researchers use a more conservative cutoff of 20% [80]. We chose a 20% cutoff value, using SPSS multiple imputation to provide acceptable inferences and preserves the data structure [81]. SPSS uses a Fully Conditional Specification which imputes incomplete data one variable at a time providing great flexibility [82]. In this process, linear regression is used to impute continuous variables and logistic regression is used to impute categorical variables [83]. We then compared the three datasets – the original data, imputed values and the complete data after imputation and considered differences in the means and standard deviations. Typically, variables with many missing values have larger error terms affecting the researcher's ability to detect significant associations. The cleaned and matched data set was then used to assess the model.

Please cite this article as: A. McLeod, D. Dolezel, Cyber-analytics: Modeling factors associated with healthcare data breaches, Decision Support Systems (2018), https://doi.org/10.1016/j.dss.2018.02.007

Constructs and variables used in the model.

<table><tr><td>Construct/variables</td><td>Definition</td></tr><tr><td>Level of exposure (Business)</td><td></td></tr><tr><td>ConsumerDashboard</td><td>Yes/No hospital utilizes a consumer dashboard</td></tr><tr><td>CPOEAffiliatedPhPerc</td><td>Percentage of affiliated physicians using the CPOE system</td></tr><tr><td>CPOEEmergencyDept</td><td>Yes/No the CPOE system is used in the emergency department</td></tr><tr><td>CPOEInpatient</td><td>Yes/No the CPOE system is used in the inpatient setting</td></tr><tr><td>CPOEOtherFTPhPerc</td><td>Percentage of other physicians using the CPOE system</td></tr><tr><td>CPOEPhyPerc</td><td>Percentage range of all medical orders entered by physicians using CPOE</td></tr><tr><td>CPOEOwnOrders</td><td>Time frame for all physicians to be entering all orders into the CPOE system</td></tr><tr><td>EMRPerc</td><td>Percentage of personnel using EMR system</td></tr><tr><td>IEInitiative</td><td>Name of Information Exchange Initiative Hospital is a part of</td></tr><tr><td>IsNICUPresent</td><td>Yes/No facility has a NICU</td></tr><tr><td>NofIntensiveCareBeds</td><td>Number of Intensive Care Bed</td></tr><tr><td>NofOutpatientVisits</td><td>Number of outpatient visits at each Acute-Care Hospital in the most recent fiscal year</td></tr><tr><td>NoofNeonatalIntensiveCareBeds</td><td>Number of Neonatal Intensive Care Beds</td></tr><tr><td>StrucPhyPerc</td><td>The percent range of physician documentation that is captured from structured template documentation solutions</td></tr><tr><td>TraumaLvl</td><td>Trauma Level a hospital is equipped to provide for comprehensive emergency medical services to patients suffering traumatic injuries</td></tr><tr><td>Level of security</td><td></td></tr><tr><td>BarFixAsst</td><td>Barcoding used in Fixed Assets</td></tr><tr><td>BarLab</td><td>Barcoding used in Laboratories</td></tr><tr><td>BarMatMgt</td><td>Barcoding used in Materials Management</td></tr><tr><td>BarMedAdm</td><td>Barcoding used in Medical Administration</td></tr><tr><td>BarOpRoom</td><td>Barcoding used in Operating Room</td></tr><tr><td>BarPatReg</td><td>Barcoding used in Patient Registration</td></tr><tr><td>BarPharm</td><td>Barcoding used in Pharmacy</td></tr><tr><td>BarRadio</td><td>Barcoding used in Radiology</td></tr><tr><td>CCD_Transaction</td><td>Yes/No the hospital is using HL7 CCD (continuum of care document) transactions to share patient data with other organizations</td></tr><tr><td>CDSSDataIntegrated</td><td>Yes/No the medical content data is integrated into workflow applications as clinical decision support tools or decision alerts for clinicians</td></tr><tr><td>CertifiedEHR</td><td>The organization uses a certified EHR system</td></tr><tr><td>CMSAttestationMU1</td><td>Organization has attested to meeting the Stage 1 Meaningful Use requirements</td></tr><tr><td>CMSAttestationMU2</td><td>Organization has attested to meeting the Stage 2 Meaningful Use requirements</td></tr><tr><td>CMSMU1Attest1Year</td><td>Yes/No the facility is prepared to attest to a full year of Stage 1 Meaningful Use</td></tr><tr><td>CMSMU1AttestTFrame</td><td>Timeframe planned for attesting to Meaningful Use Stage 1</td></tr><tr><td>CMSMU2AttestTFrame</td><td>Timeframe planned for attesting to Meaningful Use Stage 2</td></tr><tr><td>CPOEMandated</td><td>Yes/No the healthcare system mandated that physicians utilize CPOE system</td></tr><tr><td>IEInitiativePlan</td><td>Yes/No the hospital plans to participate in an Information Exchange Imitative(s)</td></tr><tr><td>IsBiometric</td><td>Yes/No the hospital uses biometric technology for security</td></tr><tr><td>IsBiometricPlan</td><td>Yes/No the hospital plans to purchase/use biometric technology for security</td></tr><tr><td>Organizational factors</td><td></td></tr><tr><td>AHAAdmissions</td><td>Number of Admissions which includes the number of adult and pediatric admissions only (excluding births). This number includes all patients admitted during the a 12-month reporting period, including neonatal and swing admissions</td></tr><tr><td>NetOperRevenue</td><td>Net operating revenue includes revenues associated with the main operations of the hospital (net inpatient+ net outpatient revenue). It does not include dividends, interest income or non-operating income</td></tr></table>

Table 1 (continued)

<table><tr><td>Construct/variables</td><td>Definition</td></tr><tr><td>FTETotal</td><td>Total number of IS FTEs</td></tr><tr><td>NofBeds</td><td>Number of Licensed Beds</td></tr><tr><td>NofBirths</td><td>Number of births at each Acute-Care Hospital in the most recent fiscal year</td></tr><tr><td>NofStaffedBeds</td><td>Number of Beds that can be operated at present staffing levels</td></tr><tr><td>NofSurgicalOperations</td><td>Number of inpatient and outpatient surgical operations</td></tr><tr><td>NofTotDischarge</td><td>The total number of patients discharged from the hospital in a calendar year</td></tr><tr><td>NofTotPatientDays</td><td>The number of calendar days of care provided for hospital inpatient treatment under the terms of the patient&#x27;s health plan, excluding the day of discharge</td></tr><tr><td>PayrollExpense</td><td>Payroll expense for a 12-month period, this includes all salaries and wage expense</td></tr><tr><td>PhysTotal</td><td>Total number of physicians in the hospital</td></tr><tr><td>RevOther</td><td>Percentage of patient revenue from other sources, such as CHAMPUS, worker&#x27;s comp., self-pay, etc.</td></tr><tr><td>TotalOperExpense</td><td>The total amount of money the Acute-Care Hospital spends on operations such as staffing, property expenses, etc. for the most recent fiscal year</td></tr><tr><td>YearOpened</td><td>Year Entity was acquired</td></tr></table>

Backwards stepwise logistic regression was used to evaluate the probability of membership in the mutually exclusive groups: facilities that have reported healthcare data breaches and facilities that have not reported healthcare data breaches during the study time. A backwards stepwise logistic model is recommended for exploratory studies where little previous work is available [84].

## 7.5. Data breach model

The basic regression model used to examine binary relationships was:

$$
\begin{array}{r l} \mathrm{Y} = \text { logit   data   breach   occurrence } & = \mathrm{a} + b _ {1} \mathrm{X} _ {1} + b _ {2} \mathrm{X} _ {2} + b _ {3} \mathrm{X} _ {3} \\ & \quad + b _ {4} \mathrm{X} _ {4 +} \dots \end{array}
$$

where p is the probability that the outcome is a 1 or a 0, and Y = logit(p) = ln(p/1-p) is the logarithmic transform of p which represents the probability of the outcome event occurring [84]. Therefore, Y equals 1 when a facility has reported a data breach and 0 when they have not reported a data breach. Moreover, the $\mathrm { X } _ { i }$ variables are the independent predictor variables affecting Y, and the $\mathsf { b } _ { i }$ values, the beta values, are the coefficients of the predictor's contribution to the outcome variable's variation. The model constant is represented by “a”.

## 8. Results

First, a Box-Tidwell test was conducted to ensure that all continous variables were linearly related to the dependent variable (i.e. test of the linearity of the logit). An examination of the interactions of the variable and the log of that variable revealed all significance values are greater that 0.05, indicating this assumption is met [84]. Table 2 presents the Box-Tidwell results.

Second, a test for multicollinearity was conducted utilizing SPSS Collinearity diagnostics. Test results indicated no tolerance b0.1 and no VIF values over 10, signifying no collinearity issues existed [84]. Table 3 presents the results of the collinearity diagnostics.

Next, data for all research questions were analyzed using backward stepwise (Likelihood Ratio) method where the full model initially contains all the predictors. At each step, SPSS checks the model fit using the likelihood ratio and removes the predictor having the least effect on the model fit. This continues until no more predictors can be removed [84].

Table 4  
Table 3 Collinearity diagnostics  
Table 2  
Box-tidwell linearity of logit.

<table><tr><td>Level of exposure</td><td>Sig.</td></tr><tr><td>ConsumerDashboard by LnConsumerDashboard</td><td>0.449</td></tr><tr><td>CPOEAffiliatedPhPerc by LnCPOEAffiliatedPhPerc</td><td>0.444</td></tr><tr><td>CPOEEmergencyDept</td><td>0.153</td></tr><tr><td>CPOEOtherFTPhPerc by LnCPOEOtherFTPhPerc</td><td>0.743</td></tr><tr><td>CPOEPhyPerc by LnCPOEPhyPerc</td><td>0.248</td></tr><tr><td>CPOEOwnOrders by LnCPOEOwnOrders</td><td>0.052</td></tr><tr><td>EMRPerc by LnEMRPerc</td><td>0.697</td></tr><tr><td>IEInitiative by LnIEInitiative</td><td>0.585</td></tr><tr><td>IsNICUPresent by LnIsNICUPresent</td><td>0.571</td></tr><tr><td>NofIntensiveCareBeds by LnNofIntensiveCareBeds</td><td>0.054</td></tr><tr><td>NofOutpatientVisits by LnNofOutpatientVisits</td><td>0.573</td></tr><tr><td>NoOfNeonatalIntensiveCareBeds by LnNoOfNeonatalIntensiveCareBeds</td><td>0.295</td></tr><tr><td>StrucPhyPerc by LnStrucPhyPerc</td><td>0.272</td></tr><tr><td>TraumaLvl by LNTraumaLvl</td><td>0.234</td></tr><tr><td>Level of security</td><td></td></tr><tr><td>CCD_Transaction by LNCCD_Transaction</td><td>0.150</td></tr><tr><td>CDSSDataIntegrated by LNCDSSDataIntegrated</td><td>0.183</td></tr><tr><td>CMSAttestationMU1 by LNCMSAttestationMU1</td><td>0.375</td></tr><tr><td>CMSAttestationMU2 by LNCMSAttestationMU2</td><td>0.420</td></tr><tr><td>CMSMU1Attest1Year by LNCMSMU1Attest1Year</td><td>0.078</td></tr><tr><td>IEInitiativePlan by LNIEInitiativePlan</td><td>0.565</td></tr><tr><td>IsBiometric by LNIsBiometric</td><td>0.645</td></tr><tr><td>IsBiometricPlan by LNIsBiometricPlan</td><td>0.302</td></tr><tr><td>CCD_Transaction by LNCCD_Transaction</td><td>0.150</td></tr><tr><td>CDSSDataIntegrated by LNCDSSDataIntegrated</td><td>0.183</td></tr><tr><td>CMSAttestationMU1 by LNCMSAttestationMU1</td><td>0.375</td></tr><tr><td>CMSAttestationMU2 by LNCMSAttestationMU2</td><td>0.420</td></tr><tr><td>CMSMU1Attest1Year by LNCMSCMU1Attest1Year</td><td>0.078</td></tr><tr><td>IEInitiativePlan by LNIEInitiativePlan</td><td>0.565</td></tr><tr><td>IsBiometric by LNIsBiometric</td><td>0.645</td></tr><tr><td>IsBiometricPlan by LNIsBiometricPlan</td><td>0.302</td></tr><tr><td>Organizational factors</td><td></td></tr><tr><td>NetOperRevenue by LnNetOperRevenue</td><td>0.427</td></tr><tr><td>FTETotal by LnFTETotal</td><td>0.540</td></tr><tr><td>NofBeds by LnNofBeds</td><td>0.080</td></tr><tr><td>NofBirths by LnNofBirths</td><td>0.937</td></tr><tr><td>NofStaffedBeds by LnNofStaffedBeds</td><td>0.196</td></tr><tr><td>NofSurgicalOperations by LnNofSurgicalOperations</td><td>0.159</td></tr><tr><td>NofTotDischarge by LnNofTotDischarge</td><td>0.367</td></tr><tr><td>NofTotPatientDays by LnNofTotPatientDays</td><td>0.505</td></tr><tr><td>PayrollExpense by LnPayrollExpense</td><td>0.257</td></tr><tr><td>PhysTotal by LnPhysTotal</td><td>0.237</td></tr><tr><td>RevOther by LnRevOther</td><td>0.634</td></tr><tr><td>TotalOperExpense by LnTotalOperExpense</td><td>0.275</td></tr></table>

## 8.1. Research question one

The association between the level of exposure and the likelihood of data breach occurrence was explored. A test of the model with all the level of exposure predictors versus the intercept only model was statistically significant, χ<sup>2</sup> (5, N = 5473) = 65.149, p b 0.001. Table 4 shows the logistic regression results for level of exposure variables. All factors were significant predictors, the number of outpatient visits at each Acute-Care Hospital in the most recent fiscal year (NofOutpatientVisits) and presence of a NICU (IsNicuPresent) were the most significant. The fitted model for level of exposure is:

Y −4:509 −0:007 CPOEAffiliatedPhPerc

<table><tr><td rowspan="2">Variables</td><td colspan="2">Collinearity statistics</td></tr><tr><td>Tolerance</td><td>VIF</td></tr><tr><td>ConsumerDashboard</td><td>0.985</td><td>1.016</td></tr><tr><td>CPOEAffiliatedPhPerc</td><td>0.370</td><td>2.705</td></tr><tr><td>CPOEEmergencyDept</td><td>0.891</td><td>1.122</td></tr><tr><td>CPOEInpatient</td><td>0.888</td><td>1.126</td></tr><tr><td>CPOEOtherFTPhPerc</td><td>0.581</td><td>1.721</td></tr><tr><td>CPOEOwnOrders</td><td>0.986</td><td>1.014</td></tr><tr><td>CPOEPhyPerc</td><td>0.367</td><td>2.725</td></tr><tr><td>EMRPerc</td><td>0.708</td><td>1.413</td></tr><tr><td>IEInitiative</td><td>0.905</td><td>1.105</td></tr><tr><td>IsNICUPresent</td><td>0.471</td><td>2.122</td></tr><tr><td>NofIntensiveCareBeds</td><td>0.657</td><td>1.523</td></tr><tr><td>NofOutpatientVisits</td><td>0.706</td><td>1.416</td></tr><tr><td>NoOfNeonatalIntensiveCareBeds</td><td>0.441</td><td>2.266</td></tr><tr><td>StrucPhyPerc</td><td>0.748</td><td>1.337</td></tr><tr><td>TraumaLvl</td><td>0.976</td><td>1.025</td></tr><tr><td>BarFixAsst</td><td>0.782</td><td>1.279</td></tr><tr><td>BarLab</td><td>0.697</td><td>1.434</td></tr><tr><td>BarMatMgt</td><td>0.757</td><td>1.321</td></tr><tr><td>BarMedAdm</td><td>0.858</td><td>1.166</td></tr><tr><td>BarOpRoom</td><td>0.952</td><td>1.050</td></tr><tr><td>BarPatReg</td><td>0.745</td><td>1.343</td></tr><tr><td>BarPharm</td><td>0.719</td><td>1.390</td></tr><tr><td>BarRadio</td><td>0.793</td><td>1.261</td></tr><tr><td>CCD_Transaction</td><td>0.795</td><td>1.258</td></tr><tr><td>CDSSDataIntegrated</td><td>0.767</td><td>1.304</td></tr><tr><td>CertifiedEHR</td><td>0.748</td><td>1.337</td></tr><tr><td>CMSAttestationMU1</td><td>0.694</td><td>1.441</td></tr><tr><td>CMSAttestationMU2</td><td>0.791</td><td>1.264</td></tr><tr><td>CMSMU1Attest1Year</td><td>0.903</td><td>1.107</td></tr><tr><td>CMSMU1AttestTFrame</td><td>0.772</td><td>1.296</td></tr><tr><td>CMSMU2AttestTFrame</td><td>0.690</td><td>1.449</td></tr><tr><td>CPOEMandated</td><td>0.827</td><td>1.209</td></tr><tr><td>IEInitiativePlan</td><td>0.923</td><td>1.084</td></tr><tr><td>IsBiometric</td><td>0.922</td><td>1.085</td></tr><tr><td>IsBiometricPlan</td><td>0.952</td><td>1.051</td></tr><tr><td>AHAAdmissions</td><td>0.168</td><td>5.949</td></tr><tr><td>NetOperRevenue</td><td>0.030</td><td>33.191</td></tr><tr><td>FTETotal</td><td>0.568</td><td>1.761</td></tr><tr><td>NofBeds</td><td>0.058</td><td>17.209</td></tr><tr><td>NofBirths</td><td>0.415</td><td>2.408</td></tr><tr><td>NofStaffedBeds</td><td>0.045</td><td>22.079</td></tr><tr><td>NofSurgicalOperations</td><td>0.284</td><td>3.515</td></tr><tr><td>NofTotDischarge</td><td>0.099</td><td>10.101</td></tr><tr><td>NofTotPatientDays</td><td>0.103</td><td>9.756</td></tr><tr><td>PayrollExpense</td><td>0.118</td><td>8.477</td></tr><tr><td>PhysTotal</td><td>0.298</td><td>3.354</td></tr><tr><td>RevOther</td><td>0.915</td><td>1.093</td></tr><tr><td>YearOpened</td><td>0.941</td><td>1.063</td></tr></table>

0:180 EMRPerc 0:660 IsNICUPresent

0:007 NofIntensiveCareBeds 0:000001 NofOutpatientVisits

The odds ratio indicates that facilities with NICUs are 1.94 times more likely to have a data breach, when holding all other variables constant. Also, as the percentage of personnel using EMR system (EMRPerc) increases, the odds of having a data breach increases by a factor of 1.197. Notably, signi cance levels for variables related to Consumer Dashboard and NofIntensiveCareBeds (not shown in table) were only slightly N0.05, suggesting that they be examined in future tests.

## 8.2. Research question two

Regarding level of security and data breach occurrences, the test with the full set of security predictors versus the base (intercept only) model was statistically significant, $\chi ^ { 2 } \left( 5 , N = 5 4 7 3 \right) = 3 3 . 9 9 2 , p <$

Logistic regression results for level of exposure.

<table><tr><td>Predictors</td><td> $\beta$ </td><td>S.E.</td><td>Wald  $\chi^{2}$ </td><td>Sig.</td><td>OR</td></tr><tr><td>CPOEAffiliatedPhPerc</td><td>-0.007</td><td>0.003</td><td>6.292</td><td>0.012</td><td>0.993</td></tr><tr><td>EMRPerc</td><td>0.180</td><td>0.080</td><td>5.005</td><td>0.025</td><td>1.197</td></tr><tr><td>IsNICUPresent</td><td>0.660</td><td>0.206</td><td>10.272</td><td>0.001</td><td>1.936</td></tr><tr><td>NofIntensiveCareBeds</td><td>0.007</td><td>0.003</td><td>4.037</td><td>0.045</td><td>1.007</td></tr><tr><td>NofOutpatientVisits</td><td>0.000001</td><td>0.000</td><td>15.953</td><td>0.000</td><td>1.000</td></tr><tr><td>Constant</td><td>-4.509</td><td>0.334</td><td>181.808</td><td>0.000</td><td>0.011</td></tr></table>

Note: β = regression coefficients; S. E. = standard error, Sig. = Significance, OR = odds ratio.

Table 5  
Logistic regression results for level of security variables.

<table><tr><td>Predictors</td><td> $\beta$ </td><td>S.E.</td><td>Wald  $\chi^{2}$ </td><td>Sig.</td><td>OR</td></tr><tr><td>BarLab</td><td>1.289</td><td>0.603</td><td>4.571</td><td>0.033</td><td>3.628</td></tr><tr><td>BarMedAdm</td><td>-0.714</td><td>0.462</td><td>2.387</td><td>0.122</td><td>0.490</td></tr><tr><td>BarOpRoom</td><td>-17.729</td><td>4339.207</td><td>0.000</td><td>0.997</td><td>0.000</td></tr><tr><td>BarPharm</td><td>0.953</td><td>0.522</td><td>3.332</td><td>0.068</td><td>2.594</td></tr><tr><td>IEInitiativePlan</td><td>0.453</td><td>0.191</td><td>5.638</td><td>0.018</td><td>1.573</td></tr><tr><td>Constant</td><td>-5.884</td><td>0.699</td><td>70.937</td><td>0.000</td><td>0.003</td></tr></table>

Note: β = regression coefficients; S. E. = standard error, Sig. = Significance, OR = odds ratio.

0.001. Table 5 presents the level of security backwards regression results. Barcoding used in Laboratories (BarLab) and the hospital planning activities for Health Information Exchange Initiative (IEInitiativePlan) were significant. Results showed the level of security model is.

Y −5:884 1:289 BarLab 0:453 IEInitiativePlan

Per the odds ratio, facilities with lab barcoding are 3.6 times more likely to experience data breach occurrences, holding all other variables constant. Similarly, entities engaged in HIE initiative plans are 1.57 times more likely to experience data breach occurrences.

## 8.3. Research question three

The third question explored organizational factors and the likelihood of data breach occurrence. A test with the full set of predictors was statistically significant, $\chi ^ { 2 } \left( 5 , N = 5 4 7 3 \right) = 9 4 . 0 1 7 , p < 0 . 0 0 1$ . Specifically, the full model's -2LL is 1201.547, reduction of 94.017 from the base (intercept only) model. This is a positive outcome because lower -2LL values designate a better model fit. Table 6 shows the organizational logistic regression results. All variables in the final step of the regression were significant, with the year the hospital was acquired (YearOpened) and the total amount of money the Acute-Care Hospital spends on operations such as staffing, total operating expenses, etc. for the most recent fiscal year (TotalOperExpense) having the most significant effects. The fitted model was.

Y 13:449 0:000017 NofBirths 0:002 NofStaffedBeds

−0:000041 NofSurgicalOperations

0:000000113 TotalOperExpense −0:009 YearOpened

## 8.4. Research question four

All associations between the level of security, level of exposure, organizational factors, and the likelihood of the occurrence of a data breach were examined. All study variables were entered into a backwards stepwise logistic regression. The model with all predictors, versus the intercept only model, was significant, $\chi ^ { 2 } \left( 9 , N = 5 4 7 3 \right) = 1 1 6 . 1 0 , p <$ 0.001. The full model predictors correctly predicted 10% of the data breach occurrences. Table 7 displays the logistic regression results for the breach data model. The strongest predictors were YearOpen,

Logistic regression results for organizational factors.

<table><tr><td>Predictors</td><td> $\beta$ </td><td>S.E.</td><td>Wald  $\chi^2$ </td><td>Sig.</td><td>OR</td></tr><tr><td>NofBirths</td><td>0.000017</td><td>0.000</td><td>6.963</td><td>0.008</td><td>1.000</td></tr><tr><td>NofStaffedBeds</td><td>0.002</td><td>0.001</td><td>5.289</td><td>0.021</td><td>1.002</td></tr><tr><td>NofSurgicalOperations</td><td>- 0.000041</td><td>0.000</td><td>5.005</td><td>0.025</td><td>1.000</td></tr><tr><td>TotalOperExpense</td><td>0.000000113</td><td>0.000</td><td>8.890</td><td>0.003</td><td>1.000</td></tr><tr><td>YearOpened</td><td>-0.009</td><td>0.002</td><td>17.289</td><td>0.000</td><td>0.991</td></tr><tr><td>Constant</td><td>13.449</td><td>4.230</td><td>10.109</td><td>0.001</td><td>693,066</td></tr></table>

Note: β = regression coefficients; S. E. = standard error, Sig. = Significance, OR = odds ratio.

## Table 7

Logistic regression results for breach data model.

<table><tr><td>Predictors</td><td> $\beta$ </td><td>S.E.</td><td>Wald  $\chi^2$ </td><td>Sig.</td><td>OR</td></tr><tr><td>CPOEAffiliatedPhPerc</td><td>-0.007</td><td>0.003</td><td>7.012</td><td>0.008</td><td>0.993</td></tr><tr><td>BarLab</td><td>1.384</td><td>0.596</td><td>5.400</td><td>0.020</td><td>3.991</td></tr><tr><td>BarOpRoom</td><td>-17.671</td><td>4196.675</td><td>0.000</td><td>0.997</td><td>0.000</td></tr><tr><td>IEInitiativePlan</td><td>0.367</td><td>0.196</td><td>3.517</td><td>0.061</td><td>1.443</td></tr><tr><td>NofBirths</td><td>0.000017</td><td>0.000</td><td>6.966</td><td>0.008</td><td>1.000</td></tr><tr><td>NofStaffedBeds</td><td>0.002</td><td>0.001</td><td>5.659</td><td>0.017</td><td>1.002</td></tr><tr><td>NofSurgicalOperations</td><td>0.000044</td><td>0.000</td><td>5.891</td><td>0.015</td><td>1.000</td></tr><tr><td>TotalOperExpense</td><td>0.000000012</td><td>0.000</td><td>10.177</td><td>0.001</td><td>1.000</td></tr><tr><td>YearOpened</td><td>-0.008</td><td>0.002</td><td>13.918</td><td>0.000</td><td>0.992</td></tr><tr><td>Constant</td><td>10.789</td><td>4.344</td><td>6.168</td><td>0.013</td><td>48,496.025</td></tr></table>

Note: β = regression coefficients; S. E. = standard error, Sig. = Significance, OR = odds ratio.

TotalOperExpense, CPOEAffiliatedPhPerc and NoOfBirths. The fitted model for all predictors is.

Y 10:789 −0:007 CPOEAffiliatedPhPerc 1:384 Bar Lab

0:000017 NofBirths 0:002 NofStaffedBeds

−0:000044 NofSurgicalOperations

0:000000012 TotalOperExpense −0:008 YearOpened

## 9. Discussion

The results of this work provided interesting insight into some of the factors associated with healthcare data breaches. While many of these breaches are the result of insider threats or accidental release of information, many are malicious in nature. In other cases, the level of exposure, level of security and organizational factors aligned, allowing data breaches to occur. We considered four research questions based on these “Swiss Cheese” aligning constructs and discuss results for each research question.

## 9.1. Research question one

First, the relationship between the level of exposure and the likelihood of data breach occurrence was explored. Significant predictors included the percentage of affiliated physicians using a computerized physician order entry system, the percentage of hospital personnel using the EMR system, whether a neonatal intensive care unit was present, the number of intensive care beds, and the number of outpatient visits. It appears that the increased connectivity involving medical systems provides opportunities for those that would do harm. In addition, the number of non-regular personnel using these systems seems to indicate a weakness, potentially due to less training, inappropriate use or simple carelessness. Increased size of intensive care units could be introducing issues related to a variety of connected medical devices and this may be the case with increasing outpatient visits as well. It is becoming clear that increased connectivity means increased exposure.

One huge benefit in collecting organizational information, is the ability to keep track of record exposure and subsequent breaches, an advantage not available prior to reporting. While reporting is important, organizational entities must also recognize exposure variables such as those considered here. For example, the use of a CPOE system by affiliated users who are not permanent employees introduces susceptibilities. Furthermore, having a neonatal intensive care unit (NICU) necessitates the deployment of many electronic and wireless devices, with each device interface presents an entry point protected by a login and password. Since many medical systems retain original manufacturer passwords, having a NICU may introduce portals of entry for malicious agents.

This same principal applies to the number of intensive care beds and the number of outpatient visits since both necessitate accessing patient

Please cite this article as: A. McLeod, D. Dolezel, Cyber-analytics: Modeling factors associated with healthcare data breaches, Decision Support Systems (2018), https://doi.org/10.1016/j.dss.2018.02.007

A. McLeod, D. Dolezel / Decision Support Systems xxx (2018) xxx–xxx

and hospital clinical systems from many locations for care provisioning. Healthcare organizations providing many intensive care beds typically utilize a variety of medical devices, and these devices need to be correctly managed to reduce. In large organizations with many intensive care beds and outpatient or ambulatory services, increased exposure takes the form of multiple devices and processes to manage patient care and data. One of the best tools to test to reveal such exposures is penetration testing.

## 9.2. Research question two

Next, the relationship between the level of security and the occurrence of a data breach was considered. While technology can increase the level of security through the use of biometrics, barcoding, and radio frequency identification, these tools continue face operational challenges in healthcare settings. For this work, we considered existing data related to security, examining barcoding use in laboratories, medical administration, operating rooms, pharmacy, health information exchange planning activities, biometric planning, health information exchange planning, clinical decision support planning, and certified electronic health record planning as potential security indicators.

Interestingly, laboratory barcoding was a significant predictor of data breaches, while pharmaceutical barcoding use was only marginally significant. While barcoding results are understandable, the effect of planning activities is troublesome. It may be that planning activities reflect a temporal response due to a noted vulnerability. That is, organizations may have already recognized a security need and started planning for additional technological tools, and subsequently were breached. Organizations that plan for greater connectivity are more able to securely manage data, however contracting with business associates for services such as cloud hosting pose additional risks. Those healthcare facilities that do not question business associate's ability to protect data, the associate's level of security and the associate's planned response to malware attacks, will face a greater likelihood of experiencing the difficulties associated with a breach indicating that organizations need to be proactive in planning for cybersecurity risk [85].

## 9.3. Research question three

The third construct examined was organizational factors and their association with data breaches. Factors related to complexity fall within this purview as well as organization size, age and expenditures. Because there are so many characteristics potentially influencing data breaches, we considered those available in the data set indicating size, complexity and expenditures. Predictors included AHA admissions, net operating revenue, number of full time employees, number of beds, number of operations, total patient days, payroll expense, operating expenses and year opened. Significant organizational predictors related to complexity included number of births and number of surgical operations. Healthcare facilities containing obstetrical and surgical operating units have more complex systems leading to greater potential for breach. Surgical units are not immune to data breaches and may pose a greater risk given increased use of technology. In summary, increased healthcare facility complexity leads to greater odds of experiencing a breach as demonstrated by the significance of these organizational factors.

Financial expenditures are important. They represent another potential factor affecting data breaches. Protecting patient data is expensive and healthcare facilities that fail to spend monies to operate a secure environment are more subject to theft [86]. Data breaches are even more expensive in terms of dollars and in terms of the patients' negative perceptions of the breached facility. Specifically, the actual cost of a data breach continues to rise. Interestingly, total operating expenses were significant in this study, however teasing out security expenditures was not possible as that level of detail was not present in the dataset.

The last variable in the organizational factor list was year opened. In this study, the age of the healthcare organization was a significant predictor of breaches. Newer facilities reported fewer breaches and this may be due to newer technologies employed, less legacy systems and better infrastructure. It may also be related to facility life cycle since other types of organizations are known to have age related effects.

## 9.4. Research question four

Finally, the relationships between level of exposure, level of security, organizational factors and the likelihood of the occurrence of a data breach were considered together. Combining all individual construct's significant variables into a single model yielded associated results. Predictors included computerized physician order entry system affiliated physicians, barcoding in laboratories, number of births, number of staffed beds, number of surgical operations, total operating expenses and year opened. In addition, health information exchange planning and the number of neonatal intensive care beds were marginally significant. This model reveals factors associated with users, technological complexity of the facility, size and age of the organization and expenditures. How organizations deal with these factors affects the likelihood of experiencing a data breach.

## 9.5. Limitations

As is the case with all research, there are several limitations for this study. The first limitation was the quantity and quality of data available. The DHSS breach report provided data for reported breach incidents over the period of 2009–2017. This work included only DHHS breach reports limiting the research. The DHHS breach reporting requirement of N500 records means that smaller breaches are not reported and therefore not included in this study. Moreover, there are questions about the number of breaches being underreported, especially given the large number of attacks, non-compliance fines and settlements being levered.

Second, the HIMSS Analytics Legacy Database used in this study provided organizational data for the year 2015. Matching data between independent data sets of this size is challenging and panel data would provide richer analysis. The factors analyzed from the data set are also limiting and additional attributes may provide a greater insight.

Third, the results of this work show a small amount of explanatory power using this model. Exploratory research often reports low r square results, limiting practical significance. The variance explained in this model was quite low, however the goal of studies such as this is to establish relationships and associations rather than produce a predictive model.

Fourth, the exploratory nature of the research is a limitation. Exploratory hypothesis testing involving multiple test iterations with many variables increases the Type 1 (false positive) error rate [87]. We considered lowering the alpha level, which could reduce the Type 1 error rate, but this increases the potential for Type II (false negative) errors. Depending on the cohesiveness of the variables, it is easy to see how such an exploratory approach can lead to false positives. Optimally, the existence of more research in this area to guide the study would have allowed for more precise variable selection and fewer iterations of testing.

## 10. Conclusion

This study modeled many exposure, security and organizational factors to determine associations with healthcare data breaches. Because of continued phishing, hacking and other malware assaults on healthcare information systems, this work is important to consumers who risk losing their healthcare data to criminals. Organizations collecting personal health information have a legal and moral duty to protect such data and therefore need to be proactive in understanding the causes of data breaches. This is not an easy task, however and there is much that can be done to improve the current state of healthcare security.

Regarding level of exposure, three things of importance related to these systems. First, the potential impact of affiliated personnel using healthcare systems and second how much active use of an EMR system is in place. Obviously both the quantity and the quality of users will impact security. Complex organizations, such as those operating NICUs, those having many intensive care beds and those with outpatient ambulatory offerings, need to pay attention and fund security related activities. Health organizations such as these are more vulnerable than less complex organizations.

Considering those elements related to security, technological and planning activities appear critical. Where technology is rolled out to improve efficiency and effectiveness, security must follow. Those organizations incorporating barcoding, RFID and biometrics should evaluate not only the technology but their ability to protect personal health information. Significant planning efforts need to also consider processes associated with the use of business associate cloud technologies.

Organizational aspects mostly reflect descriptive associations. For example, the number of births occurring in a healthcare facility is probably tied to whether an obstetrical ward is present, but this also is a flag indicating increased complexity and size. Greater intricacy and interconnectedness might mean greater risk. A similar situation is indicated by the number of surgical operations. A large metropolitan hospital with a high trauma level might perform many more complex operations and use more interconnected devices.

Other descriptive characteristics include the number of staffed beds – a good proxy for size. Healthcare facilities should be aware that as they grow, they become more of a target and are more likely to be breached. We found that based on the number of beds, large hospitals were more than twice as likely to experience data breaches as smaller hospitals. This means that patients have a greater chance of having their personal health information breached at larger hospitals. A higher number of beds may also be associated with a greater number of medical devices and increased network traffic with more accesses to the Internet of Things. Protecting as you grow brings additional cost and operating budgets are important. Is the organization adequately funding security tools, personnel and training? Finally, the age of the facility should be considered when evaluating the potential for breach. How old is the hospital's infrastructure? Instead of continuing to patch aging legacy systems, consider replacement to avoid age related security disadvantages.

Because of the use of large unassociated data sets, this work has seyeral noted limitations. It represents an attempt to model the level of exposure, level of security and organizational factors associated with healthcare data breaches. Future research should endeavor to improve the quantity and quality of data to improve predictability and reliability of breach models. Other potential research involves improving the constructs developed here, considering a more complex measure of breach such as the number of records stolen, or adding unstructured data to breach analysis to discover hidden factors.

The importance of understanding how and why breaches occur cannot be over stressed. Our results provide an initial modeling effort for understanding the complexity of factors which may be associated with a healthcare data breach. Security standards facilitated the development of potential influences. This work categorized and analyzed these influences and grouped them to create constructs related to the level of security, exposure and organizational factors impacting data breaches. Breach determination remains important given the large number of phishing, hacking and other malicious acts.

Alexander McLeod is an Assistant Professor at Texas State University in the College of Health Professions – Health Information Management Department. He received his Ph.D. in Information Technology from the University of Texas at San Antonio. Research interests include cyber analytics, security, privacy, healthcare information systems, and technology. He has published in Business Process Management Journal,

Communications of the Association of Information Systems, CPA Journal, Decision Sciences Journal of Innovative Education, Educational Perspectives in Health Informatics and Information Management, Fraud, Information Systems Frontiers, International Journal of Biomedical Engineering and Technology, International Journal of Business Information Systems, International Journal of Electronic Healthcare, International Journal of Healthcare Information Systems and Informatics, Journal of Accounting Education, Journal of Business Ethics, Journal of Information Privacy and Security, Journal of Information Science and Technology, Journal of Information Systems Education, Perspectives in Health Information Management.

Dr. Diane Dolezel is an assistant professor in the HIM department at Texas State University where she teaches graduate and undergraduate students classes in informatics, analytics, and data use; healthcare research and data analysis, and quality management. Ms. Dolezel earned a Doctorate of Education with a focus in Instructional Leadership. She has authored book chapters and has published several peer reviewed research articles on usability of web-based PHRs, data migration for EHRs, metadata, data analysis relational databases, and other informatics topics. She is a frequent speaker at national and regional AHIMA, HIMSS and TSAHP conferences on relational databases, electronically stored information, informatics, and data analytics. She worked in the information technology field for many years as a senior developer and consultant with significant experience in database programming and systems integration. At the university, she serves on the faculty student research forum. Professionally, she has served on the AHIMA Foundation Council for Academic Excellence, Faculty Development Workgroup, and, was awarded an AHIMA Merit Scholarship as a graduate student.

## Acknowledgements

No organization funding was received for this research. We would like to acknowledge the graduate research assistants who provided assistance in merging the large amount of data used in this research.

## References

[1] R.D. Stachel, M. DeLaHaye, Security breaches in healthcare data: an application of the actor-network theory, issues in Information Systems 16 (2015) 185–194

[2] J. Davis, Cyberattack at Appalachian Regional Healthcare Keeping EHR Down after Six Days, Healthcare IT News, HIMSS Media, 2016.

[3] Office for Civil Rights, Data Breach Results in \$4.8 Million HIPAA Settlements, 2017. [4] DHHS, Breach Notification Rule, 2017.

[5] J. Davis, Michigan Cancer Center Notifies 22,000 Patients of Breach 5 Months after Hack, Healthcare IT News, 2017.

[6] J. Davis, Phishing Attack on UC Davis Health Breaches Data on 15,000 Patients, Healthcare IT News, 2017.

[7] J. Davis, The DarkOverlord Leaks Celebrity Patient Data from Beverly Hills Provider, Healthcare IT News, 2017.

[8] J. Davis, NSA Uncovers Ties between North Korea and WannaCry Attacks, Healthcare IT News, 2017.

[9] DHHS, Breaches Affecting 500 or More Individuals, 2015.

[10] DHHS, Breaches Affecting 500 or More Individuals, Department of Health & Human Services. 2015

[11] Department of Homeland Security, Cybersecurity Overview, Department of Homeland Security, 2016

[12] S.B. Wikina, What caused the breach? An examination of use of information technology and health data breaches, Perspect. Health Inf. Manag. 11 (2014).

[13] B.-Y. Ng, A. Kankanhalli, Y.C. Xu, Studying users' computer security behavior: a health belief perspective, Decis. Support. Syst. 46 (2009) 815–825.

[14] T. Floyd, M. Grieco, E.F. Reid, Mining Hospital Data Breach Records: Cyber Threats to US hospitals Intelligence and Security Informatics (ISI). 2016 IFFE Conference on JEEE 2016.43-48

[15] D. Gibbs, K. Lalani, A. McLeod, Beware the Internet's Dark Side: What HIM Professionals and Patients Should Know About the Dark Web L. AHIMA (2017). Accessed date: 1 August 2017.

[16] J. Reason, Managing the Risks of Organizational Accidents, Routledge, 2016.

[17] T. Judson, M. Haas, T. Lagu, Medical identity theft: prevention and reconciliation initiatives at Massachusetts General Hospital, Jt. Comm. J. Qual. Patient Saf. 40 (2014) 291–295.

[18] B. Obama, in: T.W. House (Ed.), Executive Order–Improving Critical Infrastructure Cybersecurity, 2013.

[19] NIST, Framework for Improving Critical Infrastructure Cybersecurity, 2014.

[20] NIST, Commission on Enhancing National Cybersecurity, U.S. Department of Commerce 2017

[21] U.S. Congress, Health Insurance Portability and Accountability Act, U.S. Department of Health & Human Services, 1996.

[22] U.S. Congress, Health Information Technology for Economic and Clinical Health Act, US. Department of Health and Human Services, 2009.

[23] DHHS, HIPAA Security Guidance, 2006

[24] Office for Civil Rights, Summary of the HIPAA Security Rule, 2010.

[25] U.S. Congress, Title 45 Code of Federal Regulations, U.S. Government Printing Office, 2011.

[26] NIST, An Introductory Resource Guide for Implementing the Health Insurance Portability and Accountability Act (HIPAA) Security Rule, 2008.

[27] Office for Civil Rights, Guidance on Risk Analysis Requirements under the HIPAA Security Rule, 2014.

[28] DHHS, First HIPAA Enforcement Action for Lack of Timely Breach Notification Settles for \$475,000 U.S, Department of Health and Human Services, 2017.

[29] J. Davis, Health Data Breaches vs. Security Incidents: A Primer, Healthcare IT News, 2017.

[30] DHHS, Fact Sheet: Ransomware and HIPAA, 2017.

[31] J. Davis, Ransomware Rising, but where Are all the Breach Reports? Healthcare IT News, 2017 (Ed.).

[32] J. Davis, Ransomware Rising, but Where Are All the Breach Reports? Healthcare IT News, 2017.

[33] NIST Computer Security Division, Minimum Security Requirements for Federal Information and Information Systems, Federal Information Processing Standard Publication 200, 2006.

[34] D. Liginlal, I. Sim, L. Khansa, How significant is human error as a cause of privacy breaches? An empirical study and a framework for error management, Comput. Secur. 28 (2009) 215–228.

[35] H. Adams, A. Campbell, Automated radiographic report generation using barcode technology, Am. J. Roentgenol. 145 (1985) 177–180.

[36] FDA, Guidance for Industry Bar Code Label Requirements Questions and Answers, 2011.

[37] P.L. Shaw, D. Carter, Quality and Performance Improvement in Healthcare, AHIMA, Chicago, IL, 2015.

[38] M. Farik, A. Ali, Analysis of default passwords in routers against brute-force attack, Int. J. Technol. Enhanc. Emerg. Eng. Res. 4 (2015) 341–345.

[39] P. Hachesu, Z. Leila, H. Hassankhani, Recommendations for using barcode in hospital process, Acta Inform. Med. 24 (2016) 206–2010.

[40] C. McDonald, Computerization can create safety hazards: a bar-coding near miss, Ann. Intern, Med. 144 (2006) 510–516.

[41] S. Biederman, D. Dolezel, Introduction to Healthcare Informatics, AHIMA, Chicago, IL, 2017.

[42] P. Veríssimo, N. Neve, M. Correia, The CRUTIAL reference critical information infrastructure architecture: a blueprint, Int. J. Syst. Syst. Eng. 1 (2008) 78–79.

[43] T. Sullivan, 93,000 Patient Records Exposed by Pennsylvania Provider, Healthcare IT News, 2017.

[44] M. McNickle, 5 Things to Know about CCD, 2012.

[45] D. Dolezel, Introduction to Healthcare Informatics, Second Edition, 2017.

[46] K. Flynn, Your iPhone can Be Hacked with a Photo of your Thumb, 2014.

[47] S.I.R. Room, Biometrics: A Double Edged Sword - Security and Privacy, 2002

[48] J. Collmann, T. Cooper, Breaching the security of the Kaiser Permanente internet patient portal: the organizational foundations of information security I. Am, Med. Inform, Assoc, 14 (2007) 239–243

[49] J.S. Kumar, D.R. Patel, A survey on internet of things: security and privacy issues, Int. I. Comput, Appl, 90 (2014).

[50] J. Davis, Molina Healthcare Breached, Exposed Patient Data for over a Month, Healthcare IT News, 2017.

[51] P. Garrett, EMR vs EHR – What Is the Difference?ONC 2011.

[52] K. Kiho Yeo, K. Lee, S. Yoo, Pitfalls and security measures for the mobile EMR system in medical facilities, Healthc Inform. Res, 18 (2012) 125-135

[53] B. Hewitt, D. Dolezel, A. McLeod, Mobile device security: perspectives of future healthcare workers, Perspect. Health Inf. Manag. (2017) 1–14.

[54] P.K. Oachs, A.L. Watters, Health information management concepts, Principles and Practice, AHIMA, Chicago: IL, 2016.

[55] M.P. Garnica, CPOE: an essential tool for evidence-based practice, Nurse Pract. 36 (2011) 12–15.

[56] R. Asija, R. Nallusamy, A Survey on Security and Privacy of Healthcare Data, 2014.

[57] C. Pellegrini, The Joint Commission Clarifies Stance on Secure Text Messaging of Pa tient Care Orders, American College of Surgeons, 2017.

[58] J. Commission, Update: texting orders, Jt. Comm. Perspect. 36 (2016).

[59] N. Antunes, M. Vieira, Penetration testing for web services, Computer 47 (2014) 30–36.

[60] M. Burns, Data Breach may Involve Hundreds of UNC Health Prenatal Patients, wral. com .

[61] A. Marotti, Presence Health Agrees to \$475,000 Settlement over Data Breach, Chicago Tribune, 2017.

[62] R. Sen, S. Borle, Estimating the contextual risk of data breach: an empirical approach, J. Manag. Inf. Syst. 32 (2015) 314–341.

[63] R. Ayyagari, An exploratory analysis of data breaches from 2005–2011: trends and insights, J. Inf. Priv. Secur. 8 (2012) 33–56.

[64] A. Yazdanmehr, J. Wang, Employees' information security policy compliance: a norm activation perspective, Decis. Support. Syst. 92 (2016) 36–46.

[65] C. Angst, E. Block, K. Kelley, When do IT security investments matter? Accounting for the influence of institutional factors in the context of healthcare data breaches, MIS Q. 41 (2017) 893–916.

[66] S. Kraemer, P. Carayon, J. Clem, Human and organizational factors in computer and information security: pathways to vulnerabilities, Comput. Secur. 28 (2009) 509–520.

[67] M. Maasberg, C. Liu, Network Effects and Data Breaches: Investigating the Impact of Information Sharing and the Cyber Black Market, University of Texas, San Antonio, 2015.

[68] H. Zafar, Security risk management at a fortune 500 firm: a case study, J. Inform. Priv. Secur. 7 (2011) 23–53.

[69] A.G. Kotulic, The security of the IT resource and management support: security risk management (SRM) program effectiveness, Challenges of Information Technology Management in the 21st Century, 2000 Information Resources Management Associ ation International Conference, Anchorage, Alaska, 2000.

[70] H.S.B. Herath, T.C. Herath, IT security auditing: a performance evaluation decision model, Decis. Support. Syst. 57 (2014) 54–63.

[71] F. Kamoun, M. Nicho, Human and organizational factors of healthcare data breaches: the Swiss cheese model of data breach causation and prevention, Int. J. Healthc. Inf. Syst. Inform. 9 (2014) 42–60.

[72] J. Stein, K. Heiss, The Swiss cheese model of adverse event occurrence—closing the holes, Semin. Pediatr. Surg. 24 (2015) 278–282.

[73] A. Da Veiga, J.H. Eloff, A framework and assessment instrument for information security culture, Comput. Secur. 29 (2010) 196–207.

[74] Ponemon, Cost of data breach: United States, Ponemon Research Report, Ponemon Institute, 2011.2012

[75] T.J. Kobus, The A to Z of healthcare data breaches, J. Healthc. Risk Manag. 32 (2012) 24–28.

[76] A. Wirth, The importance of cybersecurity training for HTM professionals, Biomed. Instrum. Technol. 50 (2016) 381–383.

[77] A.M. Khalfan, Information security considerations in IS/IT outsourcing projects: a descriptive case study of two sectors, Int. J. Inf. Manag. 24 (2004) 29–42.

[78] J. Reason, The contribution of latent human failures to the breakdown of complex systems, Philos. Trans. R. Soc. Lond. B Biol. Sci. 327 (1990) 475–484

[79] HIMSS Legacy Workgroup, History of the Healthcare Information and Management Systems Society, HIMSS, 2013.

[80] G.D. Garson, Missing Values Analysis and Data Imputation, Statistical Associates Publishing Asheboro, Asheboro NC 2015

[81] S. Van Buuren, Multiple imputation of discrete and continuous data by fully conditional specification, Stat, Methods Med. Res. 16 (2007) 219–242.

[82] C.K. Enders, Multiple imputation as a flexible tool for missing data handling in clinical research, Behav. Res. Ther. 98 (2017) 4–18.

[83] C.K. Enders, Applied Missing Data, 2017

[84] A. Field, Discovering Statistics Using IBM SPSS Statistics, 4th ed. Sage, Los Angeles, 2013.

[85] L.P. Rees, J.K. Deane, T.R. Rakes, W.H. Baker, Decision support for cybersecurity risk planning, Decis. Support. Syst. 51 (2011) 493–505.

[86] C.D. Huang, R.S. Behara, J. Goo, Optimal information security investment in a healthcare information exchange: an economic analysis, Decis. Support. Syst. 61 (2014) 1–11.

[87] R. Ho, Handbook of Univariate and Multivariate Data Analysis with IBM SPSS, 2nd ed. CRC Press, 2014.
