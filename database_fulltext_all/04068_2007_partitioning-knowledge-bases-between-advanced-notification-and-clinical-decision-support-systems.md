---
otero_id: 4068
otero_key: "8MPZTA7S"
title: "Partitioning knowledge bases between advanced notification and clinical decision support systems"
authors: "Yves A. Lussier; Rose Williams; Jianrong Li; Srikant Jalan; Tara Borlawsky; Edie Stern; Inderpal Kohli"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.02.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Decision Support Systems 43 (2007) 1274– 1286

www.elsevier.com/locate/dss

# Partitioning knowledge bases between advanced notification and clinical decision support systems

Yves A. Lussier <sup>a,b,⁎</sup>, Rose Williams <sup>c,⁎</sup>, Jianrong Li <sup>a</sup>, Srikant Jalan <sup>c</sup>, Tara Borlawsky <sup>a</sup>, Edie Stern <sup>c</sup>, Inderpal Kohli <sup>a</sup>

<sup>a</sup> Department of Biomedical Informatics, Columbia University, New York, NY, USA b Department of Medicine, Columbia University, New York, NY, USA <sup>c</sup> IBM Thomas J. Watson Research Center, Hawthorne, NY, USA

Available online 17 April 2006

## Abstract

Clinical decision support system (CDSS) and their logic syntax include the coding of notifications (e.g., Arden Syntax). The following paper will describe the rationale for segregating policies, user preferences and clinical monitoring rules into “advanced notification” and” clinical” components, which together form a novel and complex CDSS. Notification rules and hospital policies are respectively abstracted from care-provider roles and alerting mechanisms. User-defined preferences determine which devices are to be used for receiving notifications. Our design differs from previous notification systems because it integrates a versatile notification platform supporting a wide range of mobile devices with a XML/HL-7 compliant communication protocol. © 2006 Elsevier B.V. All rights reserved.

Keywords: Clinical event monitor; Clinical decision support system; Knowledge bases; Knowledge partition; Notification attributes

## 1. Introduction

Clinical event monitors are decision support systems that generate alert messages based on events of possible clinical significance and related patient data. They can improve health care quality and reduce costs by supplying personnel with the necessary information at desirable times via preferred routes [8]. Automated wireless alerts have been used to prevent medical errors and reduce the time until appropriate treatments are ordered by immediately alerting clinicians to critical laboratory result values [2], allowing them to intervene more quickly than when the information is delivered using more traditional means [23]. The choice of communication channel, such as telephone, alphanumeric pager or, most recently, personal digital assistants (PDAs), depends on the urgency of the message, availability of the responsible caregiver and knowledge of the appropriate message recipients [8]. While mobile technologies afford the clinical setting many advantages for real-time information about a patient's condition remotely, they also add overhead costs in application development, deployment and technical support [19]. One approach is to extend legacy clinical event monitors by including a notification component using current standards (e.g., Arden Syntax). However, there are significant challenges in minimizing any adverse affects on the organization, while the notification component of the clinical DSS application evolves. Frequently changing notification protocols and available mobile devices necessitate a constant evolution of software upgrades to address the emerging technologies.

Furthermore, as many professionals today use an array of devices for mobile communications, what is needed is a configurable technology to address user preferences for delivering alerts. For the clinical setting, this problem is compounded in that physicians rotate ward and patient responsibilities, so that user role and context per patient must also be resolved.

Using middleware technology, one can preserve the existing clinical DSS system while extending its services to include full-featured notification functions [10]. Current DSSs combine clinical logic, institutional policies, users preferences and, when available, notification modalities (e.g., pager, email) [5,14,22]. The Pepagni University Hospital in Greece has built a middleware prototype for sending notifications, including laboratory alerts, over user-customizable communication modalities [10]. However, their prototype does not address issues such as HL7 and HIPAA-compliance standards. As a result, a large number of alerting rules are generated, which amplifies the system complexity following a geometric progression [16]. Previous studies have shown that clinicians have diverse preferences on notification methods [12,21] and institutions have their own policies on communicating alerts to the appropriate personnel [4]. As the number of rules and choices among communication modalities increases, system maintenance becomes a more severe issue [6]. Though flexible and user-configurable clinical notification systems are currently under development [5,14,22], they are limited in their capacity to perform such complex knowledge maintenance. For example, in an institution with N different alerts and M communication modalities, the number of relationships to manage is N⁎M. Thus, modeling institutional directives and individual preferences in the notification modalities can lead to a multiplicative explosion of relationships that significantly increases the complexity of maintaining an [8,20].

We have previously shown that a decoupled system could simplify the maintenance of clinical knowledge bases allowing for the management of policies and users preferences, and have provided guidelines on the parameters (i.e., notification attributes) that such systems should exchange [16]. This paper describes the instantiation of a loosely coupled clinical decision support service (developed by Columbia University Medical Center) with an intelligent notification service (developed by IBM Research). Our prototype utilizes the integration of HL7/ XML communication, HIPAA-compliance protocols and pervasive communication channels. The proposed architecture increases system flexibility while reducing overall maintenance complexity.

## 2. Benefit of partitioning knowledge bases

The portability of handheld technologies is one of their biggest advantages in a clinical setting. Yet, extending legacy event monitors to them by increasing the complexity of the notification component of clinical knowledge bases using current standards, such as the Arden Syntax and Guideline Interchange Format (GLIF), significantly increases the total cost of operations. The Arden Syntax for Medical Logic Modules (MLMs) is a language designed for writing and sharing task-specific health knowledge. By easing the sharing of knowledge bases, the Arden Syntax increases the use of knowledge-based systems in the realm of healthcare by enhancing knowledge sharing abilities of independent systems while reducing maintenance issues and costs [7]. GLIF, a common representation for institutional and national standard practice guidelines, facilitates guideline sharing across different healthcare institutions [13]. Combined, the MLMs found in the Arden Syntax and the syntax of GLIF already partially support the codification of knowledge pertaining to clinical alerts. However, the additional attributes of personal preferences and institutional/departmental policies for patient information communicated across varied devices greatly complicates the maintenance of the notification component of event monitors.

Further, as experienced in the last year with the changes imposed by the Health Insurance Portability and Accountability Act (HIPAA) regulations, medico-administrative policies change more frequently than clinical rules. This adds to the cost of maintaining clinical knowledge bases. For HIPAA compliance, it is important that institutions implement corporate policies for mobile devices regarding password protection, encryption, authenticated synchronization and physical security of the devices [18]. Finally, securing the integrity of data delivered over mobile channels complicates the event monitor maintenance even further and requires a completely different implementation skill set.

Overall, there are many advantages to partitioning the clinical knowledge from the administrative, and the broadcasting the clinical knowledge to mobile devices. By partitioning the knowledge bases, it is operationally easier to accommodate the different skill sets, the different rates of change, and to ensure that the more frequent changes associated with policies, and the delivery of individual alerts do not affect critical clinical knowledge systems [22]. With more frequent change comes more frequent potential for user error. By partitioning the knowledge bases, we hypothesize that the resulting smaller quantity of simpler and specialized rules will reduce the complexity of development and maintenance.

One method for partitioning knowledge is the “publish and subscribe” communication model. Publish–subscribe methodology enables decoupled and asynchronous messaging, allowing systems to exchange data between independent applications in an event-driven manner. A notification system receives a message from a “publisher” and, through the application of a notification algorithm, attempts to send the message to a “subscriber”. Vanderbil University Medical Center has utilized this methodology of separating the creation and delivery of messages in the implementation of a notification system for new physicians' orders [5]. However, the publish–subscribe model is limited in its ability to manage multiple message formats over a variety of communication channels and does not address issues of access control or encryption [22], which are mandated by HIPAA.

Therefore, our system not only uses a publish– subscribe model for communication, but also provides an additional level of abstraction that enables the identification of “subscriber” based on the providerrole for the patient at the time of a messaging event. Additionally, the prototype includes policy rules, which are reviewed automatically in real time to ensure alert protocol compliance and address fault-tolerance mechanisms for mobile communication. All features are separated from the clinical knowledge base systems.

## 3. Clinical knowledge base

Large-scale automated monitoring of a considerable number of distinct clinical conditions is complex and, to our knowledge, no sizable projects offer user-customizable communication modalities over all monitored conditions using decoupled knowledge bases. As both the numbers of clinical conditions and communication modalities increase, the complexity of customizing user preferences amplifies following a geometric progression [16] and it becomes more difficult for an information system to predict whether a laboratory result merits urgent notification to a particular user [15]. Current implementations of composite DSSs systematically use some form of notification attributes in communication protocols to exchange knowledge among the knowledge bases. A DSS containing clinical knowledge needs to be augmented with notification attributes and then communicated to the notification system in order for medico-administrative knowledge to be useful and independent of each specific clinical alert instantiation.

The Arden Syntax allows for encoding urgency, but this was shown to be insufficient and inadequately scalable for decoupling clinical decisions from decisions in a Criteria-Based Notification System [16]. However, notification attributes (NAs) that describe the urgency and severity of a patient lab result or other clinical data simplify the management of communication modalities and allow for the separation of clinical and medicoadministrative knowledge. This is particularly important for institutions where the manual assignment of a terminal device for every alert is an overwhelming task. Additionally, bundling role and policies with clinical rationale in the same rule increases the risk of unintentionally altering the clinical rule while editing th roles or policies, which are likely to change more often. De-coupling policies and roles from clinical alerts thus has advantages over maintenance (reducing the number of distinct alerts to maintain) and reduces the “risk” that an alteration to a role or policy disables its associated critical alerts. The following notification attributes were developed and incorporated into extensions of GLIF and the Arden Syntax: urgency, severity, risk, evidence and positive predictive value. Urgency refers to the time interval beginning when a message is sent to the time when an iniury or adverse event can affect the patient. Ir the absence of further intervention, the maximum degree of potential injuries to the patient is reflected by the severity attribute. The risk NA represents the probability of the occurrence of an adverse event or injury when intervention is absent. Evidence measures the strength of the evidence supporting a rule and the positive predictive value NA measures the ability of the event monitor to produce a correct message [16]. The methods by which these NAs were developed, using experts opinions and reviewing current practices, their effectiveness for encoding existing clinical conditions and an analysis of two archetypal coding schemes, the Guideline Interchange Format (GLIF) and Arden Syntax, have been previously addressed by our group [3,7–9,13,16].

The five extended NAs provide the clinically relevant information necessary to compute an appropriate target and delivery mechanism for the notification. They afford an institution the advantage of standard interfaces and generic best practice rules, while facilitating institutional-level customization and configuration. These attributes increase the reusability and sharability of institutional event monitor rules across institutions by replacing institution-specific components with generic ones. The message specifications create a standard interface for event monitors to communicate with the message management module. Secondly, standardized message specifications facilitate institutional-level customization and control of event notification by providing the mechanisms to assert these policies. The assignment of alerting mechanisms becomes independent of clinical conditions, removing institution-specific devices and technologies from the knowledge bases of the event monitors, and inserting NAs that are institution-independent and specific to a clinical condition. Third, standardized messaging facilitates both institution-level management of policies and simplifies the user-level preference configuration [16], which supports the publish–subscribe communication model used in event notification systems [5]. Events are assigned to combinations of notification attributes rather than to each instance of clinical alerts.

## 4. Notification knowledge base

## 4.1. User preferences

Our design recognizes that allowing mobile users to decide how they should be notified is part of an efficient communication solution. As such, we have a notification knowledge base that separates user subscription information, device preferences and system configuration data from the clinical alert. Our notification component, filtering incoming content, looks for important keywords and compares the filtered data with the user's criteria as defined in the user's subscription. If a match is found, our component checks the user's device preferences and related information before sending the message to the mobile device. The notification knowledge base includes the user specification of many types of preferences and subscription settings. Notification knowledge also includes delivery channel information such as device name or role, host, port and reassignment of the recipient or role during time periods when the user is unavailable does not want messages delivered (e.g., when off duty). Notification knowledge also includes message rules, which allow the delivery of messages per device based on priority levels. For example, an urgent message may get delivered to the user's pager, while a normal message may be delivered to the user's PDA.

## 4.2. Roles and policies

Our design also recognizes that, in clinical settings, physician schedules rotate responsibility for patient care. A physician ordering a laboratory test and subscribing to the results may no longer be responsible for the patient's care when the results become available. Therefore, our design supports not only how a user is notified, but also who is notified based on the provider's role at the time of message delivery. Thus, our notification knowledge base uses roles to determine the intended recipients of alerts. A role refers to the function or responsibility assumed by a person in the context of a healthcare event. Role information documents a person's association with an identified healthcare activity. Examples include primary care provider, resident, intern, hospitalist, etc. The characteristics of a role are as follows:

▪ A role association can be associated based on the patient, task or certain observation values.

▪ A role can be performed by multiple people.

▪ A person can be performing multiple roles.

▪ A role is specified for a specific period of time that is predetermined based on a schedule.

▪ A notification device can be associated with a role and the person carrying the device implicitly assumes the role.

▪ A role can be pre-specified or it can be specified as a part of each notification event.

▪ A role can be delegated to another person for a specified period.

In our prototype system, we use role information based on the schedule of users. At this time, this information is entered separately and is not integrated with the hospital scheduling system. Future work could obtain this information from the different hospital scheduling systems. Currently, the role information resolves to a single person performing the role at a specified time. Certain role information such as the “attending physician” for a patient or the “ordering physician” who requested the particular test to be performed is derived from the clinical event data, which has been sent to the notification system as a part of the alert content. Once the alert is sent to the device, our system monitors for user acknowledgement.

We have also implemented the delivery of the notifications based on hospital policies. The characteristics of the policy definitions are as follows:

▪ Policies define the workflow of the notification events.

▪ Based on timeouts of positive acknowledgement from the initial recipient, the notification can be cascaded to other recipients using different notification devices.

▪ The recipient can accept or decline the notification request.

▪ There is a catch-all recipient, for notifications that cannot be routed using the pre-defined policies, to

Table 1

Sample HL7 Patient Problem Record Protocol message (HL7 PPR\_PC1)

```csv
MSH|^~\&amp;|VIGILENS|TEST|IBM-IMM|ER|20040527154359||PPR^PC1|
20040527154359320|P|2.4
PID|||123456789^^^MR^COLUMBIA UNIVERSITY HOSPITAL||SMITH^JOHN^J^III^DR^PHD^L||19670515183020|M|||1234 EASY
STREET^STE 1A^HAWTHORNE^NY^10532^USA^B||(914) 123-4567|||SPV1||E|GENERAL MEDICINE^101^A^GENERAL MEDICINE^^^MERCER PAVILION^2^|E|||SJALAN@INS.REALM^ELLEN^ANDY
PRB|AD|20031107112830|112233445566^PANIC HCT^ARDEN MLM
LIST|||||||IP^INPATIENT^PROMBLEMCLASSIFICATIONLIST
ROL||AD|^DAYTIME CLERK^ROLE MASTER LIST|JEDWARDS^EDWARDS^JOHN
ROL||AD|^SUBINTERN^ROLE MASTER LIST|MSMITH^SMITH^MARK
ROL||AD|^INTERN^ROLE MASTER LIST|BMILLER^MILLER^BILL
ROL||AD|^RESIDENT^ROLE MASTER LIST|MPARKER^PARKER^MARY
ROL||AD|^SENIOR RESIDENT^ROLE MASTER LIST|JWILLIAMS^WILLIAMS^JASON
ROL||AD|^ATTENDING PHYSICIAN^ROLE MASTER LIST|SJALAN@INS.REALM^ELLEN^ANDY
ROL||AD|^PCP^ROLE MASTER LIST|EJOHNSON^JOHNSON^ED
ROL||AD|^ORDERING PHYSICIAN^ROLE MASTER LIST|MPETERSON^PETERSON^MIKE
OBX||NM|2479^HCT|1|15|^%|35.4-44.4||||||
OBX||NM|1564%CBC|2|27|^%|10.2-20.5||||||
OBX||TX|^KNEE FRACTURE|3|MULTIPLE FRACTURE OF KNEE JOINTS||||||
NDS|||2^MODERATE||1^60 SECONDS|1^90-100|2^PROBABLE|1^90-100
```

ensure that no notification ever gets lost due to errors in the policy definitions. This also ensures that the notification can be delivered to a responsible person in case of no positive acknowledgement from others.

▪ We must ensure that there are no cyclical loops in the policy definitions.

## 4.3. Fault tolerance for network-device communications and message delivery

In a hospital environment, loss of connectivity to a device is very common. There are network connectivity dead zones within the building, as well as critical care units that prohibit the activation of mobile devices. As such, our notification knowledge base encompasses hospital policies for cascades clinical alerts in case of messages not being delivered due to network outages or device being turned off. For example, if a user does not respond to an alert within 10 min, we retry the message to the same user. If the message has still not been responded to within another 5 min, we cascade the message to the next user in the following order:

Intern Urgent=BlackBerry

YResident Urgent=BlackBerry

YHospitalist Urgent=BlackBerry

YHospitalist FYI=EMail

If any of the roles cannot be resolved then the message is sent to the specified Intelligent Notification System (INS) user, hospitalist1@ins.realm, as an FYI message using Email.

There is increasing evidence that new communication modalities (e.g., two-way pagers, wireless telephones, etc.), when linked with a user's preference configuration, can improve clinicians' efficiency and efficacy [1,17]. Flexible and user-configurable clinical notification systems are currently under development, but these systems are limited in their capacity to maintain complex communication modalities with a large number of rules. Few institutions have implemented large-scale automated monitoring of a considerable number of distinct clinical conditions and, to our knowledge, none of these sizable projects also offer user-customizable communication modalities, institutional policies management and advanced notification, and flexible mechanisms for “fault tolerance”.

## 5. Communication protocol between the clinical and notification decision support systems

The communication protocol between the clinical event monitoring system and the intelligent notification system follows the standard as defined by Health Level 7 (HL7). The data is sent as the HL7 event message type PPR\_PC1 (i.e., Patient Problem Record Protocol). We have extended the HL7 standards using some additional attributes to support the extended NAs generated by the clinical DSS.

The PPR\_PC1 protocol is divided into multiple segments. The MSH (Message Header) segment includes the date and the time of the message and defines the intent, source, destination and syntax specifics of a message. The PID (Patient Identification) segment contains permanent patient identifying and demographic information that, for the most part, is not likely to change frequently. The PV1 (Patient Visit) segment is used by Registration/Patient Administration applications to communicate information on a visit-specific basis, including the patient's assigned location. The PRB (Problem Detail) segment contains the data necessary to add, update, correct and delete the problems of a given individual. The ROL (Role)

segment contains the data necessary to add, update, correct and delete from the record persons involved, as well as their functional involvement with the activity being transmitted. The OBX (Observation/ Result) segment is used to transmit a single observation or observation fragment. There can be multiple ROL segments identifying the different personnel associated with the current task, such as the “ordering physician”, “attending physician”, etc. In addition, there can be multiple OBX segments that identify different observation values. Because the HL7 Notification Detail Standard (NDS) segment only defines the notification message severity, we also include additional NAs. The segment is extended to provide further information, such as the “Notification Alert Urgency”, “Notification Alert Risk”, “Notification Alert Evidence” and the “Notification Alert False

## Table 2

Sample of the equivalent HL7 Patient Problem Record Protocol message (HL7 PPR\_PC1)

```xml
<PPR_PC1 xmlns="urn:hl7-org:v2xml"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="urn:hl7-org:v2xml PPR_PC1.xsd">
    <MSH>
    <MSH.1 Item="1" LongName="Field Separator" Type="ST">|</MSH.1>
    <MSH.2 Item="2" LongName="Encoding Characters" Type="ST">^~&</MSH.2>
    <MSH.3 Item="3" LongName="Sending Application" Table="HL70361" Type="HD">
    <HD.1 LongName="namespace ID" Table="HL70300" Type="IS">CU-Vigilens</HD.1>
    </MSH.3>
    <MSH.4 Item="4" LongName="Sending Facility" Table="HL70362" Type="HD">
    <HD.1 LongName="namespace ID" Table="HL70300" Type="IS">Radiology</HD.1>
    </MSH.4>
    <MSH.5 Item="5" LongName="Receiving Application" Table="HL70361" Type="HD">
    <HD.1 LongName="namespace ID" Table="HL70300" Type="IS">IBM-IMM</HD.1>
    </MSH.5>
    <MSH.6 Item="6" LongName="Receiving Facility" Table="HL70362" Type="HD">
    <HD.1 LongName="namespace ID" Table="HL70300" Type="IS">INS</HD.1>
    </MSH.6>
    <MSH.7 Item="7" LongName="Date/Time Of Message" Type="TS">
    <TS.1 LongName="time of an event" Type="ST">20030827192206</TS.1>
    </MSH.7>
    ......
</MSH>
<PID>
......
</PID>
......
</PPR_PC1>
```

Positive Rate”. These additional attributes along with the information present in the ROL segment help in determining the appropriate physician who should be notified.

The following three tables provide samples to demonstrate the protocol we developed: a sample HL7 message from Vigilens (in the original HL7 format) (Table 1), the equivalent XML representation of the HL7 message (Table 2) and the extended XML segment of the HL7 Notification Detail Standard (Table 3).

Knowledge about all aspects of the message are contained within the notification knowledge base, including the acknowledgment of the receipt of the message, the actual user who is notified, the responses from the users and any cascading of notification that has taken place. The acknowledgement is sent back to the clinical system for logging using the HL7 standard ACK\_NO2 message. The MSA (Message) segment contains the details of the acknowledgement as illustrated in Table 4.

## 6. Design implications for disparate knowledge management

The previous event monitor of our institution (Columbia Presbyterian Medical Center), which contained hundreds of different MLMs, was decommissioned in year 1999 and allowed for only two notification modalities: a patient-oriented secure web portal and an email. Assignment of each email recipient was written directly in the clinical knowledge base in Arden Syntax, which would inevitably have been time consuming for large user communities with varying roles. We have since designed its successor system, “Vigilens”, which is a server-based DSS that allows for secure telemonitoring of clinical repositories and secure notifications over the Internet. Its integration with the notification system (IBM Websphere Everywhere Suite) is illustrated in Fig. 1. Besides decoupling the clinical knowledge bases from the medico-administrative ones, we were also motivated to deploy over a larger variety of pervasive communication devices and to support

Extended XML segment of the HL7 Notification Detail Standard (NDS)

```txt
<NDS>
<NDS.1 LongName="Notification Reference Number" Type="NM">
20040813122025456875
</NDS.1>
<NDS.2 LongName="Notification Date/Time" Type="TS">
<TS.1 LongName="time of an event" Type
="ST">20030827192206</TS.1>
</NDS.2>
<NDS.3 LongName="Notification Alert Severity" Type="CE">
<CE.1 LongName="identifier (ST)" Type="ST">2</CE.1>
<CE.2 LongName="text" Type="ST">Moderate</CE.2>
</NDS.3>
<NDS.4 LongName="Notification Code" Type="CE">
<CE.1>1</CE.1>
<CE.2>EHC</CE.2>
</NDS.4>
<NDS.5 LongName="Notification Alert Urgency" Type="CE">
<CE.1>1</CE.1>
<CE.2>60 seconds</CE.2>
</NDS.5>
<NDS.6 LongName="Notification Alert Risk" Type="CE">
<CE.1>1</CE.1>
<CE.2>90 - 100</CE.2>
</NDS.6>
<NDS.7 LongName="Notification Alert Evidence" Type="CE">
<CE.1>2</CE.1>
<CE.2>Probable</CE.2>
</NDS.7>
<NDS.8 LongName="Notification Alert False Positive Rate" Type
="CE">
<CE.1>1</CE.1>
<CE.2>90 - 100</CE.2>
</NDS.8>
</NDS>
```

diverse communication protocols. For the purpose of evaluating the feasibility of the proposed loosely coupled systems, we have implemented, in the test server, 40 types of clinical alerts on Vigilens with two types of notification attributes (urgency and severity) and three states (high, low, unknown), leading to six attribute-state combinations. Each policy and user preference can be assigned to one of these six combined states of NAs, which makes them clinically relevant without having to individually deal with each current clinical alert or with future additions. Traditional clinical DSSs either neglect the issues of modalities of communications, policies or user preferences, or address only a small number of combinations because of difficulties with affordably scaling up these aspects and the clinical rules. Indeed, each of these combinations would otherwise have to be implemented in the system.

## 7. A notification protocol for comprehensive decision making with a PDA

In our prototype, alerts are displayed on a PDA device (BlackBerry™ 7510) as a message list in colorcoded HTML. This specific device was originally selected because its server could be implemented behind the hospital's firewall and could generate a true end-toend secure communication between the device and the event monitor. To our knowledge, no other end-to-end push secure protocol is available for PDA-type devices (alternative push protocols basically encrypt messages to the carrier, where the message is decrypted and reencrypted in another communication protocol). Most implementations for PDA communications push an unsecured URL and then pull secure communications. These former implementations do not optimize the efficient secure display of laboratory data, as the user is bound to “pull” all secure results. In addition, the notification protocol has been developed to maximize the immediate decision making process by the clinician. Thus, the protocol includes the usual critical alert (patient name, medical record number, critical value) as well as additional contextual clinical and medicoadministrative information. The first panel displays a list of alerts, one per line. As the physician recipient selects an alert on the first panel, the screen prompts the details of the specific message. Message details include patient name, medical record number, date of birth, room location, the urgency and severity of the alert, contact information (Fig. 2) and additional laboratory results related to the decision making process (Fig. 3). The physician can scroll down to view additional data,

```xml
<ACK_N02>
    <MSH>

......
    </MSH>
    <MSA>
    <MSA.1 Item="18" LongName="Acknowledgement Code" Table="HL70008" Type="ID">AA</MSA.1>
    <MSA.2 Item="10" LongName="Message Control ID" Type="ST">20031216110302460</MSA.2>
    <MSA.3 Item="20" LongName="Text Message" Type="ST">
    <Source>CU</Source>
    <INSNotificationID></INSNotificationID>
    <INSResponseID></INSResponseID>
    <AckType>A</AckType>
    <AckTime>20031216110128</AckTime>
    <RecipientRole></RecipientRole>
    <RecipientName></RecipientName>
    <RecipientDevice></RecipientDevice>
    <RecipientPriority></RecipientPriority>
    <RecipientAction></RecipientAction>
    <RecipientMessage></RecipientMessage>
    <ForwardToRole></ForwardToRole>
    <ForwardToName></ForwardToName>
    <ForwardToDevice></ForwardToDevice>
    <ForwardToPriority></ForwardToPriority>
    <ErrorCode>0</ErrorCode>
    </MSA.3>
    </MSA>
</ACK_N02>
```

![](/api/attachments/8MPZTA7S/fulltext/images/2fa18a1cb91a59e6d27399bcfafee1955d2ce34ae5c8f109640e3316750de8ae.jpg)  
Fig. 1. Clinical event monitoring system (Vigilens) loosely integrated, via secure HL7 protocol over the Internet, with an advanced notification system (Intelligent Notification).

accept the receipt of the alert, or provide additional comments and feedback about the alert. In this same screen, the clinician can also view other associated laboratory values from the test panel. The notification history page (Fig. 4) displays the list of users to whom the notification was sent (due to multiple recipients at the same time or due to cascading policies). The action taken by each recipient and the comments by each physician are also displayed on this screen.

## 8. Discussion

Decoupling the recipient assignment from the clinical knowledge base was deemed essential to reduce the complexity of the maintenance of clinical knowledge in the context of increasingly varying medicoadministrative policies subsequent to the HIPAA regulations. The efficiency and effectiveness of partitioning clinical and administrative knowledge bases has been evaluated using analytic metrics including mathematical formulas for determining the complexity of knowledge base maintenance. Indeed, the escalating potential changes in the former clinical knowledge base were directly related to the product of an increasing number of dimensions related to assigning the correct recipients for an alert (shown in Eq. (1) below with an example). In contrast, the proposed model does not increase geometrically with every dimension, but rather linearly (additive rather than multiplicative) as shown in Eqs. (2a)–(2d). As shown in Eqs. (3a) (3b), since the number of recipients (IoR = thousands in our hospital) and therefore of possible user preferences (Pr⁎IoR) are vastly larger than the number of notification attributes (NA = 2 in this example), of communication modalities (CM = PDA, pagers) or of roles (R) in an institution, the term NP in Eq. (1) is far greater than the term NP in Eq. (2a). In Eqs. (3a) (3b), we show that the ratio of the number of parameters of a common system to a decoupled system is approximately equal to the number of clinical logic rules times the number of policies divided by the number of notification attributes introduced by the decoupling.

8.1. Eq. (1). Complexity of notification in a common clinical and administrative knowledge base

$$
\mathrm{NP} _ {1} = \mathrm{CL} ^ {*} \mathrm{Po} ^ {*} \mathrm{Pr} ^ {*} \mathrm{IoR} ^ {*} R ^ {*} \mathrm{CM}\tag{1}
$$

Where: $\mathrm { N P _ { 1 } } \mathrm { = n u m b e r }$ of parameters to be assigned in a “common” logical rule, CL = number of clinical logic rules (e.g., K N 7 meq/l), Po = number of policies (logic rules), Pr = number of user preferences per user, R= number of roles, CM =number of communication modalities (e.g., PDA, secure portal, pager, secure email) and IoR = number of instances of recipient (physician “JD”, nurse $^ { \mathrm { \tiny { s } 6 } } \mathrm { E L } ^ { \mathrm { \tiny { > } } } .$ , etc.).

![](/api/attachments/8MPZTA7S/fulltext/images/664b29a2426c87a8352f1a24398e3697cf97f5186f3fbe05f248706d3a97017f.jpg)  
Fig. 2. Display of a critical alert showing the clinical notification attributes (critical, urgent) on the second topmost row, the critical message and providing the contact information of the patient. Notifications criteria are used by the notification system to route the message according to roles, policies and user preferences to the right recipient(s) using the right modality(ies) of communication(s).

8.2. Eqs. (2a)–(2d). Simplicity of notification in decoupled clinical and administrative knowledge bases

$$
\begin{array}{r l} \mathrm{NP} _ {2} & = \mathrm{NP} _ {\mathrm{C}} + \mathrm{NP} _ {\mathrm{Po}} + \mathrm{NP} _ {\mathrm{Pr}} \\ & = \mathrm{NA} ^ {*} (\mathrm{CL} + \mathrm{Po} ^ {*} \{R ^ {*} \mathrm{CM} \} + \mathrm{Pr} ^ {*} \{\mathrm{IoR} ^ {*} R ^ {*} \mathrm{CM} \}) \end{array}\tag{2a}
$$

$$
\mathrm{NP} _ {\mathrm{C}} = \mathrm{NA} ^ {*} \mathrm{CL}\tag{2b}
$$

$$
\mathrm{NP} _ {\mathrm{Po}} = \mathrm{NA} ^ {*} \mathrm{Po} ^ {*} R ^ {*} \mathrm{CM}\tag{2c}
$$

$$
\mathrm{NP} _ {\mathrm{Pr}} = \mathrm{NA} ^ {*} \mathrm{Pr} ^ {*} R ^ {*} \mathrm{CM} ^ {*} \mathrm{IoR}\tag{2d}
$$

where: $\mathrm { N P } _ { 2 }$ = number of parameters to be assigned in a “decoupled” set of logical rules, $ \mathrm { N P } _ { \mathrm { C } } { = }$ number of parameters to be assigned in the clinical knowledge base, $\mathrm { N P _ { P o } = n u m b e r }$ of parameters to be assigned in the policy knowledge base, $\mathrm { N P _ { P r } = n u m b e r }$ of parameters to be assigned in the a preference knowledge base and NA = number of notification attributes (passed as parameters between the alerting and notification systems due to the decoupled knowledge bases).

8.3. Eqs. (3a) (3b). Ratio of number of parameters of common system to decoupled system

From Eqs. (1) and (2a), we can calculate the ratio $\frac { \mathrm { N P _ { 1 } } } { \mathrm { N P _ { 2 } } }$ , where a value greater than one argues in favor of the

![](/api/attachments/8MPZTA7S/fulltext/images/fe5b8f318a3b526e07b03d19156a47238a30d0f27e25f257d844bdf2826fdf2f.jpg)  
Fig. 3. Display of laboratory panel associated to a critical alert message.

![](/api/attachments/8MPZTA7S/fulltext/images/aa7896568d78cb3a9b7b67f5e826d68f8ffe1ade2a1e4fae3619cb8f0a388f05.jpg)  
Fig. 4. The notification history page displays the list of users to whom the notification was sent.

proposed decoupled methods represented in (2a)–(2d). One can further demonstrate that

$$
\begin{array}{r l} \frac {\mathrm{NP} _ {1}}{\mathrm{NP} _ {2}} & = \frac {\mathrm{CL} ^ {*} \mathrm{Po} ^ {*} \left\{\mathrm{Pr} ^ {*} \mathrm{IoR} ^ {*} R ^ {*} \mathrm{CM} \right\}}{\mathrm{NA} ^ {*} (\mathrm{CL} + \mathrm{Po} ^ {*} \left\{R ^ {*} \mathrm{CM} \right\} + \mathrm{Pr} ^ {*} \left\{\mathrm{IoR} ^ {*} R ^ {*} \mathrm{CM} \right\})} \\ & = \frac {\mathrm{CL} ^ {*} \mathrm{Po}}{\mathrm{NA} ^ {*} \left(\frac {\mathrm{CL}}{\mathrm{Pr} ^ {*} \mathrm{IoR} ^ {*} R ^ {*} \mathrm{CM}} + \frac {\mathrm{Po}}{\mathrm{Pr} ^ {*} \mathrm{IoR}} + 1\right)} \end{array}\tag{3a}
$$

assuming that $\mathrm { C L } \ll \mathrm { P r } * \mathrm { I o R } * R * \mathrm { C M }$ and that $\mathrm { P o } \ll$ Pr⁎IoR (which are reasonable assumptions in a clinical DSS, since the number of users, IoR is usually an order of magnitude bigger than the number of rules, CL):

$$
\frac {\mathrm{NP} _ {1}}{\mathrm{NP} _ {2}} \approx \frac {\mathrm{CL} ^ {*} \mathrm{Po}}{\mathrm{NA}} > > 1
$$

because the number of notification attributes; NA; is small

3b

Fig. 5 illustrates the calculations of Eq. (3b) for a range of values relevant to many event monitors. The horizontal axis pertains to the number of distinct clinical logic rules, while the vertical axis is the number of different policies in an institution. We are assuming a constant rate of notification criteria. The stratified results in the graph are the calculated range of values for the ratio. A ratio greatly larger than 1 illustrates that there is probably an economy of labor in using a decoupled system. The data demonstrates that the maintenance of coupled systems as compared to decoupled system increases geometrically as clinical rules and policies are added. For example, our system currently operates with about 50 clinical rules and three policies (star in Fig. 5). As shown, the ratio demonstrates that operating with the same number of parameters in a coupled system would have required 150 logical rules rather than 53. We expect the new DSS to rapidly evolve to the level of clinical rules previously maintained (250). Additional projected economies are significant: the fully developed DSS at Columbia University Medical Center is expected to comprise well over three policies and 250 clinical logic rules; thus, according to the metric (Eq. (3b)), 253 total parameters would be developed in decoupled system instead of 750 in a coupled system.

Thus, as proposed by March and Smith [11], we have created an instantiation (our software) that operationalizes the conceptual understanding of the problem (e.g., the need for decoupled knowledge bases and the need for multiple communication modalities). We have focused our evaluation on the measure of the efficiency and on the theory underlying this measure.

In addition, one can easily assess that the number of logical rules times the number of policies times the number of user preferences are likely to be much more abundant than the number of notification attributes (in our case, six combinations); thus, we can conclude algebraically that in most cases $\mathrm { N P } _ { 1 } \gg \mathrm { N P } _ { 2 } \mathrm { : }$ simply stated, the number of parameters to implement and maintain in the decoupled knowledge base system are more advantageous than the status quo.

One limitation of this study is that only a subset of the previously published notification attributes has been implemented (“severity” and “urgency”). As the quantity of clinical and medico-administrative rules increase, it is likely that the implementation of additional notification attributes is required to increase the value, particularly the “clinical evidence” in support of the alert generated. This is particularly useful for “calculated” events such as drug–drug interactions, where the evidence in the literature varies from anecdotal to well-established. Additionally, implementation of additional modalities of communications would allow for studying the value of the implementation for managing user preference choices; currently our experience has focused on implementation of policies and clinical alerts.

![](/api/attachments/8MPZTA7S/fulltext/images/c3ccab93d4b68f48349f1d457b0f372d508c5148130e12b481b2694723d491aa.jpg)  
Fig. 5. Labor reduction estimated from the stratified results of the ratio of the number of logic rules required to maintain a coupled (common) decision support system (NP1) divided by the number of rules required in the decoupled DSS (NP2). A ratio ≫ 1 likely demonstrates that there is an economy of labor in using a decoupled system. The data illustrates that the maintenance of coupled systems as compared to decoupled system increases geometrically as clinical rules and policies are added. For example, our system currently operates with about 50 clinical rules and three policies (star). Operating the same number of rules in a coupled system would have required 150 logical rules rather than 53. We expect the new DSS to rapidl evolve to the level of clinical rules previously maintained (250). Additional projected economies are significant: the fully developed DSS at Columbia University Medical Center is expected to comprise well over three policies and 250 clinical logic rules; thus, according to the metric (Eq. (3b)), 253 total parameters would be developed in decoupled system instead of 750 in a coupled system.

We have described notification attributes to increase the scalability, development, and maintenance of decoupled and distributed clinical, and notification knowledge bases. We have demonstrated an implementation that incorporates roles, a publish–subscribe model and a HIPAA-compliant notification mechanism involving the development of a communication protocol between a clinical decision support system and a notification DSS. We have then examined in a research environment the feasibility and functionality of the implementation. Additionally, we have also provided an evaluation metric to assess the value of the proposed methods in other environments. In summary, we have demonstrated in this proof-of-concept study that clinical and notification rules can be decoupled via notification attributes, honoring stringent HIPAA-compliant security criteria, and that this decoupling enables an increase in flexibility of notification with a potential for significantly reduced management cost of notification rules such as policies and user preferences.

## Acknowledgements

The team acknowledges the partial funding form the Columbia Center for Advanced Information Management (NYSTAR), as well as the managerial contribution of Guruduth Banavar and Lorraine Herger.

## References

[1] E. Ammenwerth, et al., Mobile information and communication tools in the hospital, Int. J. Med. Inform., vol. 57(1), 2000, pp. 21–40.

[2] A.E. Carroll, D.A. Christakis, Pediatricians' use of and attitudes about personal digital assistants, Pediatrics 113 (2) (2004) 238–242.

[3] J. Choi, Y.A. Lussier, E.A. Mendoca, Adapting current Arden Syntax knowledge for an object oriented event monitor, AMIA Annu. Symp. Proc., 2003, p. 814.

[4] E. Coiera, V. Tombs, Communication behaviours in a hospital setting: an observational study, British Medical Journal 316 (7132) (1998) 673–676.

[5] A. Geissbuhler, et al., Design of a general clinical notification system based on the publish–subscribe paradigm, Proc. AMIA Annu. Fall Symp., 1997, pp. 126–130.

[6] W.R. Hogan, M.M. Wagner, Optimal use of communication channels in clinical event monitoring, Proc. AMIA Symp., 1998, pp. 617–621.

[7] G. Hripcsak, et al., Rationale for the Arden Syntax, Computers in Biomedical Research 27 (4) (1994) 291–324.

[8] G. Hripcsak, et al., Design of a clinical event monitor, Computers in Biomedical Research 29 (3) (1996) 194–221.

[9] R.A. Jenders, et al., Medical decision support: experience with implementing the Arden Syntax at the Columbia-Presbyterian Medical Center, Proc. Annu. Symp. Comput. Appl. Med. Care, 1995, pp. 169–173.

[10] E. Kafeza, et al., Alerts in mobile healthcare applications: requirements and pilot study, IEEE Transactions on Information Technology in Biomedicine 8 (2) (2004) 173–181.

[11] S.T. March, G.T. Smith, Design and natural science research on information technology, Decision Support Systems 15 (1995) 251–266.

[12] L. McKnight, et al., Perceived information needs and communication difficulties of inpatient physicians and nurses, Proc. AMIA Symp., 2001, pp. 453–457.

[13] L. Ohno-Machado, et al., The guideline interchange format: a model for representing guidelines, Journal of the American Medical Informatics Association 5 (4) (1998) 357–372.

[14] M. Oppenheim, et al., Design of a clinical alert system to facilitate development, testing, maintenance, and user-specific notification, Proc. AMIA Symp., 2000, pp. 630–634.

[15] E.G. Poon, et al., Real-time notification of laboratory data requested by users through alphanumeric pagers, Journal of the American Medical Informatics Association 9 (3) (2002) 217–222.

[16] Y. Tao, et al., Extended attributes of event monitor systems for criteria-based notification modalities, Proc. AMIA Symp., 2002, pp. 762–766.

[17] K.E. Tate, R.M. Gardner, K. Scherting, Nurses, pagers, and patient-specific criteria: three keys to improved critical value reporting, Proc. Annu. Symp. Comput. Appl. Med. Care, 1995, pp. 164–168.

[18] M.J. Tooey, A. Mayo, Handheld technologies in a clinical setting: state of the technology and resources, AACN Clinical Issues 14 (3) (2003) 342–349.

[19] M. Tschopp, C. Lovis, A. Geissbuhler, Understanding usage patterns of handheld computers in clinical practice, Proc. AMIA Symp., 2002, pp. 806–809.

[20] M.M. Wagner, M.C. Pankaskie, W.R. Hogan, Clinical event monitoring at the University of Pittsburgh, Proc. AMIA Symp., 1997, pp. 188–192.

[21] M. Wagner, et al., Preferences of interns and residents for e-mail, paging, or traditional methods for the delivery of different types of clinical information, Journal of the American Medical Informatics Association (1998) 140–144.

[22] M.M. Wagner, et al., Design of a clinical notification system, Proc. AMIA Symp., 1999, pp. 989–993.

[23] H.R. Warner Jr., et al., Clinical event management using push technology—implementation and evaluation at two health care centers, Proc. AMIA Symp., 1998, pp. 106–110.

Yves A. Lussier, MD, B. Engineering, has been Assistant Professor of Medicine and Biomedical Informatics at Columbia University since 2001. He has been conducting translational research and development in ontologies and NLP systems for over 15 years. In 1991, he developed the first commercial biomedical ontology system organized as a directed acyclic graph, which contained 60,000 concepts (Purkinje.com, 1990). He is actively involved with two major NIHfunded ontology groups: the Systematized Nomenclature of Medicine (SNOMED) and the Phenotype Attribute Ontology Committee of the Gene Ontology Consortium. Furthermore, he also has served or is serving on more than a dozen boards (governance, scientific and editorial), including the Editorial Board of SNOMED from the College of American Pathologists. He cumulates over 160 publications, communications and invited lectures.

His research group is currently conducting hypothesis-driven translational research that focuses on the use of knowledge technologies to accurately individualize the understanding, prediction and treatments of diseases. More specifically, he has developed computational methods that bring together ontologies, natural language processing (NLP), artificial intelligence and heterogeneous data integration to analyze an increasingly large and complex wealth of clinical, genomic and molecular databases. His research group has recently completed three significant projects in molecular medicine including the design of an oligonucleotide microarray for the detection of all known vertebrate viruses in collaboration with Dr. W. Ian Lipkin, and pioneered genome scale “systems” analyses of (i) the human phenome and (ii) of the prokaryotic phenome.

Dr. Rose Williams, a computational scientist at the IBM Thomas J. Watson Research Center, cumulates 20 years of research and development experience in architecture design and code implementation. Dr. Williams has developed a distinctive expertise in computational medicine: with focus on data mining, artificial intelligence, trends analysis and advanced database processing. She is currently involved in biomedical projects spanning areas of standards, advanced SQL and database extensions, complex data models and class implementation, coding to advanced data analysis toolkits, and a variety of other “middleware” and “Internet” related programming, mobile and non-mobile user interface design and implementation, and also mobile-to-enterprise infrastructure/data exchange/security. She is also a recognized technical authority influencing IBM strategies, products and business opportunities.
