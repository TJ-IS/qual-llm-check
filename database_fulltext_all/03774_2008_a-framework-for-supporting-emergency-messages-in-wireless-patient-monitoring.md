---
otero_id: 3774
otero_key: "FD3X6CYW"
title: "A framework for supporting emergency messages in wireless patient monitoring"
authors: "Upkar Varshney"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.03.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A framework for supporting emergency messages in wireless patient monitoring

Upkar Varshney ⁎

Department of Computer Information Systems, Georgia State University, Atlanta, Georgia 30302-4015, United State

a r t i c l e i n f o

Article history: Received 7 March 2007 Received in revised form 24 March 2008 Accepted 27 March 2008 Available online 8 April 2008

Keywords: Patient monitoring Wireless systems Ad hoc networks Performance evaluation

## a b s t r a c t

Patient monitoring is becoming a requirement for offering a better healthcare to an increasing number of patients in nursing homes and hospitals. During the monitoring, vital signs of patients could <sup>fl</sup>uctuate signi<sup>fi</sup>cantly and/or match certain undesirable patterns and therefore “alerts” or emergency messages must be delivered to healthcare professionals. In this paper, we address how patient monitoring, speci<sup>fi</sup>cally emergency messages, can be supported over wireless ad hoc network formed among patients' devices. The framework describes a wireless patient monitoring system that includes patient monitoring devices, routing protocols and information presentation for vitals signs and parameters. This involves a series of decisions in obtaining and processing vital signs, routing over networks, and delivering to healthcare professionals, who must make suitable medical decisions on patients' healthcare needs. Additionally, several design enhancements to improve the quality and coverage of wireless patient monitoring are presented. The performance results for the proposed ad hoc network based architecture show that reliable message delivery and low monitoring delays can be achieved by using multicast or broadcast-based routing schemes. The proposed monitoring architecture is shown to be scalable and the cognitive load on healthcare professionals is found to be dependent on routing protocols and reliability requirement of emergency messages. The proposed work can be extended to provide personalized healthcare services to people in nursing homes, assisted living, home, and while being mobile.

© 2008 Elsevier B.V. All rights reserved.

## 1. Introduction

With an increasing cost of healthcare and a growing population of seniors in nursing homes and hospitals worldwide, patient monitoring using wireless technologies is being considered as a solution to both improving the quality of healthcare and reducing the rate of increase for healthcare services [2,3,8,12,15]. As many of the patients are mobile and therefore could be well served by using wireless networks for monitoring [26,34,38–40]. In general, patient monitoring involves periodic transmission of routine vital signs and transmission of alerting signals when vital signs cross a threshold, patients cross a certain boundary, or device battery drops below a level. There are many challenges in wireless monitoring of patients, including the coverage, reliability and quality of monitoring. The work done in patient monitoring includes home monitoring [19] wireless telemetry system for EEG epilepsy [30], Bluetooth-based system for digitized ECGs [17], a hospital-wide mobile monitoring system [33], mobile telemedicine [1,10,31,32] and, real-time home monitoring of patients [27]. The work on devices and sensors include clothing-embedded transducers for ECG [12], ring-based sensor [35], minimally invasive wireless sensors for health-monitoring [5,18], and personal health monitors for stress monitoring [13]. More recent work includes support for alerts [14,20], elderly [23,29], real-time monitoring [22], and monitoring for disabled [47]. An autonomous intelligent agent for monitoring Alzheimer patients' health care is presented in [7]. A mobile decision making system for using symptoms of abdominal pain in children's emergency is presented in [28]. Some discussion on DSS requirements for emerging applications can be found in [36]. Several ways to improve medical decision making are included in [4,6,9,24].

One of the most dif<sup>fi</sup>cult challenges in patient monitoring using wireless networks, especially for emergency messages, is the reliability of message delivery. The quality of patient monitoring is also affected by the end-to-end delays or monitoring delays. Additionally, the wireless patient monitoring system should be scalable to support as many patients as possible. Many hospitals and nursing homes are deploying infrastructure-oriented wireless networks, such as wireless LANs, satellites, and cellular and GSM (Global System for Mobile communications) systems, where a <sup>fi</sup>xed infrastructure is utilized to support <sup>fi</sup>xed and mobile patients [41,45]. The potentially spotty coverage, due to time and locationdependent channel quality and signal attenuation resulting in dead spots, of infrastructure-oriented wireless networks [37] will signi<sup>fi</sup>cantly affect the reliability of emergency message delivery [42–44]. The resulting unpredictable quality and reliability of patient monitoring could lead to dif<sup>fi</sup>culty in achieving continuous patient monitoring and delivery of emergency signals from a patient to healthcare professionals, and eventually, the delayed medical response to patients could result in injury [42]. To support the reliability and monitoring delay requirements of patient monitoring, signi<sup>fi</sup>cant work is necessary in creating wireless network architecture and protocols to support routing and delivery of messages carrying a range of vital signs and healthcare information. To overcome the coverage problems of infrastructure-oriented wireless networks, several patient monitoring devices can form an ad hoc network for transmission of emergency messages carrying digitized vital signs [46]. In this paper, a framework is presented to describe a wireless patient monitoring system consisting of patient monitoring devices, ad hoc networks, devices for healthcare professionals, and, network routing protocols. The novelty in the wireless patient monitoring is the use of ad hoc wireless networks for increasing the reliability of emergency message transmission. The results show that reliable message delivery and low monitoring delays are achieved by using multicast or broadcast-based routing schemes.

Now we discuss how vitals signs are represented and digitized, requirements of emergency signals, and the contributions of this paper to wireless patient monitoring.

## 1.1. Vital signs and representation

The vital signs include ECG, blood pressure, pulse, body core temperature, and oxygen saturation [48]. These vital signs are shown in Fig. 1, where each vital sign is represented as an analog signal along with its nominal value. In addition to the diversity and the number of vital signs, the frequency and representation of relevant healthcare information could affect the management of network traf<sup>fi</sup>c, and the achievable reliability and monitoring delay. As shown in Fig. 1, several vital signs are obtained, sampled, and digitized for transmission as network packets. The traf<sup>fi</sup>c generated by digitization of vital signs can be compressed [11], however, increased processing and packet delays, and, potential for any “introduced” errors in critical healthcare information must be carefully considered.

The severity of one or more medical conditions re<sup>fl</sup>ect in changing values of vital signs such as pulse rate involving bradycardia (less than 60 pulse) and tachycardia (more than 100 pulse), blood pressure, breathing rates, oxygen saturation, and ECG. In an ECG signal, P wave represents the sequential activation (depolarization) of the right and left atria, QRS complex shows right and left ventricular depolarization, and ST-T wave is for ventricular re-polarization. The PR interval is the time interval from onset of atrial depolarization (P wave) to onset of ventricular depolarization (QRS complex) and the QT interval is the duration of ventricular depolarization and re-polarization [49]. Any signi<sup>fi</sup>cant changes in wave pattern may indicate patient-speci<sup>fi</sup>c cardio-vascular problems such as missing or weaker P wave indicates atrial problems affecting blood <sup>fl</sup>ow to the heart and a deformation in the Q wave represents damage to the heart. A large increase in the Q wave with respect to overall QRS indicates myocardial infraction, while inverted T wave indicates ischemia. A depressed ST segment indicates obstructions in the arteries. These conditions could be detected by patient monitoring devices or some devices may perform a simple comparison of current ECG signal with a prior ECG signal to generate an alert.

![](/api/attachments/FD3X6CYW/fulltext/images/82625e1a2cc953605e08c58c43e544a318cfc391989866dc65de481b4c9e880b.jpg)  
Fig. 1. Vital signs and digitization.

![](/api/attachments/FD3X6CYW/fulltext/images/c5d0373cded94428a3b91976edd445efe05177ded3eea01b7ecee25b652df292.jpg)  
(b) Detecting Emergencies using 3-Lead ECG  
Fig. 2. Two ECG Systems and detection of emergencies.

Our work can utilize either the common and very popular 3-lead ECG system or a more comprehensive but dif<sup>fi</sup>cult to wear 12-lead ECG system (Fig. 2). The 3-lead system, used in Cardiac Care Units (CCUs) and commonly implemented as Holter monitor, can detect QRS complex and heartbeats as it observes the electrical activities of the inferior and lateral walls of the left ventricles. Thus it can detect bradycardia, tachycardia, sinus arrest, ventricular tachycardia with broad QRS complexes, and supraventricular tachycardia with narrow QRS complexes [25]. The 12-lead ECG provides spatial information on heart's electrical conductivity in three approximately orthogonal directions as it observes electrical activity at lateral, inferior, septal, and anterioral walls. The 3- lead ECG system is more suitable due to its wearability for more patients in nursing homes and availability. In future, as the 12-lead system becomes more integrated in wearable PMD, it can be utilized for a more precise and comprehensive detection of cardiac problems for emergencies.

## 1.2. Requirements of emergency signals

During the patient monitoring, some vital signs could <sup>fl</sup>uctuate signi<sup>fi</sup>cantly and potentially crossing pre-de<sup>fi</sup>ned thresholds or matching certain undesirable patterns, resulting in “alerts” or emergency messages. The range and patterns of vitals signs must be highly personalized as different patients may have unique ranges of “normal” vital signs. In some cases, an individual vital sign may not result in an emergency situation, however when combined with few more high-normal or low-normal vital signs, an emergency event may occur requiring the transmission of emergency messages to healthcare professionals. Although very important for patient monitoring, there has been little work on emergency messages in wireless patient monitoring [16]. These emergency messages must be reliably delivered to healthcare professionals with minimal delays and message corruption. Many traditional engineering considerations such as network ef<sup>fi</sup>ciency [21], traf<sup>fi</sup>c, and the number of patients that can be monitored or supported by wireless infrastructure may become secondary. However, these affect the scalability and the cognitive load of healthcare professionals that are involved in patient monitoring.

## 1.3. Proposed work and contributions

The primary objective of this paper is to provide a framework to support emergency signal transmission using ad hoc wireless networks, which can be formed among patient-worn devices, including radio-enabled watches and a grid of body sensors. A possible scenario for patient monitoring is shown in Fig. 3, where multiple devices used on a patient can form body area network (BAN) for communications related to different vital signs to healthcare professionals. Both, intra-body BAN and inter-body BAN, involving devices on multiple patients, are ad hoc wireless networks, where topological changes occur with mobility of patients, power transmitted by devices, and the wireless channel characteristics. In practice, patient monitoring could also involve a combination of infrastructure-oriented wireless LANs (with base stations) and ad hoc networks, we focus on ad hoc networks in this paper due to their novelty and potential in supporting emergency messages in patient monitoring.

The framework presented in this paper is designed to support the requirements of patient monitoring, including emergency messages which require very high levels of reliability and low delays. The framework also includes representation for healthcare information and enhancements for network routing in the presence of un-cooperative routers. The novelty in the proposed work involves the use of ad hoc wireless networks for increasing the reliability of emergency message transmission (Section 2). The performance of routing schemes presented in the framework, namely multicast, broadcast, reliable multicast and reliable broadcast for delivery of emergency messages, is also evaluated using analytical modeling techniques (Section 3). The performance results show that reliable message delivery and low monitoring delays can be achieved by using multicast or broadcast-based routing schemes. Using many proposed enhancements, the system is shown to be scalable and the resulting cognitive load on healthcare professionals is found to be reasonable, and relates to the routing protocols used and reliability requirements of patient monitoring.

![](/api/attachments/FD3X6CYW/fulltext/images/2eb8e2def5e318b6e88ac2ff442c0e250be7fe350f40fc676974307b4702b5d9.jpg)  
D1, D2, D3: Patient Monitoring Devices Ri, Rj, Rk: Routing Devices HP1, HP2: Healthcare Professionals  
Fig. 3. Patient monitoring using ad hoc wireless networks

## 2. The framework for ad hoc wireless patient monitoring

The framework utilizes the patient monitoring system (Fig. 4), consisting of patient monitoring devices, ad hoc wireless network(s), the devices for healthcare professionals, and databases for healthcare and relevant medical information. The patient monitoring devices, designed to be highly personalized, measure vital signs and parameters. This is followed by a set of decisions to derive the emergency level. This information along with vital signs, after packetized, is routed through the underlying ad hoc wireless network(s), formed either on demand or proactively, to one or more of healthcare professionals. The personalized medical information and a set of actions are stored in a database and can be downloaded for medical decision making by healthcare professionals. The combination of patient's current vital signs and past medical information could lead to a context, which then would help healthcare professionals in reaching to a suitable and well informed decision on the patient's current medical needs, including need for emergency care.

In the next few sub-sections, different components of framework are described including (a) representation of vital signs and patient parameters, (b) processing of vital signs by patient monitoring devices, (c) routing of emergency messages in the underlying ad hoc wireless networks, (d) reliability of emergency messages, and, (e) several enhancements for overcoming routing problems.

![](/api/attachments/FD3X6CYW/fulltext/images/2661040109acb7fb681734a344c996c4ffdaa91b141320030ad5d0da754fa676.jpg)  
Fig. 4. The proposed wireless patient monitoring system and major components.

## 2.1. Representation of vital signs and parameters

The patient monitoring system is likely to generate a large amount of data with an increase in the number of vital-signs and the frequency of monitoring, and, potentially a large number of patients that may have to be monitored. Also, the amount of information for each patient related to his/her medical history, nominal range of vital signs, and recent patterns of vital signs, could become signi<sup>fi</sup>cant. The amount of data is not only dependent on the patient's medical problems and history, but also on the processing and transmission of vital signs, whole or differential values representing changes since the last transmission or from a range of nominal values. The transmission of differential vital signs will reduce the amount of traf<sup>fi</sup>c on the ad hoc network, resulting in either an increased number of patients that could be monitored or a better quality of monitoring for the existing patients. However, the differential vital signs could also require additional information to be stored in the medical database. The potential tradeoff between bandwidth and storage can be studied for reliability of message delivery, patient monitoring delay, network scalability, and cost of storage.

The informational representation of vital signs and parameters includes the past medical history of patients and a set of actions that must be performed for different healthcare needs. The set of actions could evolve based on the advances in medical knowledge and patient's condition. The representation includes vital signs with multiple thresholds, set of actions, undesirable patterns, and inter-relationship between multiple vital signs. The personalized healthcare information can be kept in one or more databases and will be accessible for integration with current vital signs for presentation to healthcare professionals. The amount of delays in accessing patient's information and the set of actions, and integrating these with the current values of vital-signs could be reduced by parallelizing database access and processing of medical information with the routing of emergency messages over ad hoc wireless networks.

## 2.2. Patient monitoring device and protocol

The vital signs of patients under wireless patient monitoring must be obtained, ampli<sup>fi</sup>ed, and converted to digital signals before getting transmitted over ad hoc wireless networks. There are multiple ways to obtain vital signs noninvasively such as multiple sensors on a patient body, specialized bands and wearable monitors, smart shirts, and watch-type wearable devices. It is envisioned that a patient is likely to have diversity of non-invasive and wearable devices. The proposed con<sup>fi</sup>guration for patient monitoring device is shown in Fig. 5, where vital signs are acquired as analog signals and processed, followed by conversion to digital signals. Then the vitals signs can be stored, displayed and transmitted over ad hoc wireless networks to healthcare professionals for suitable actions on healthcare delivery.

A protocol is also needed in determining when and how vital signs will be measured, checked and coded for transmission. To address this requirement, we present a multilevel threshold based protocols for detecting emergency and abnormal events. The proposed protocol for emergency messages is shown in Fig. 6, where one or more events are generated based on levels and patterns of current vital signs. The patient monitoring device receives patient's medical information, including personalized thresholds and frequency of monitoring for individual vital signs. This will lead to personalized monitoring for emergency events. For simple patient monitoring devices, this information could be obtained from the patient database, while more sophisticated patient monitoring devices could store it locally. Once the vital signs are acquired, threshold and pattern-based processing is done to determine the level of emergency and a suitable action is taken, such as generation of a transmission event with a certain priority. A simple example is shown in Fig. 7 for decision-making for emergencies using blood pressure.

## 2.3. Routing for emergency messages

The support for emergency messages in patient monitoring requires very high reliability of message delivery, low delays and minimal message corruption. To improve the reliability and delay performance, the patient monitoring devices, when not covered by an infrastructure-oriented wireless network, could form an ad hoc wireless network. Such connectivity then can be utilized to transmit packetized information on patient's current vital signs and medical history. For an ad hoc wireless network, emergency messages can be transmitted to healthcare professionals using several different routing schemes (Fig. 8). The routing schemes differ in how messages are routed to a destination, thus affecting the reliability of message delivery and network traf<sup>fi</sup>c, which also affects the end-to-end delay, a critical factor in the transmission of emergency messages in wireless patient monitoring.

The four different routing schemes are proposed here: multicast, reliable multicast, broadcast, and reliable broadcast. In multicast routing, patient information is sent to multiple, not

![](/api/attachments/FD3X6CYW/fulltext/images/0b44de4cadcd40eac9a9fc9d28ecc8b43ec8a90b83479971c05d0ae6a394043b.jpg)  
Fig. 5. The con<sup>fi</sup>guration and functionalities of patient monitoring device.

```txt
(**Receive information on vital signs, thresholds (low, high) and derive waiting time using frequency of monitoring**)
Receive THRSHLD[K] for each VTL_SGN[J]
Receive FRQ[I] for each VTL_SGNS[J]
Generate WT-TM[I] for each VTL_SGNS[J]

(**Normal range is between threshold1(low) & threshold1(high). Above normal is between threshold 1(high) and threshold2(high). Below normal is between threshold 1(low) and threshold2(low). Emergency is above threshold2(high) or below threshold 2(low)**)

For each VTL_SGN[J]
If VTL_SGNS[J] < THRSHLD2[Low]
Generate EMERGENCY_EVENT(LOW)
Else If VTL_SGNS[J] < THRSHLD1[Low]
Generate ABNOR_EVENT(LOW)
Else If VTL_SGNS[J] < THRSHLD1[high]
If WT_TM[I] >=RPRT_TM[I]
Generate TRNSMSN_EVENT;
Else If VTL_SGNS[J] <= THRSHLD2[high]
Generate ABNOR_EVENT(HIGH)
Else Generate EMERGENCY_EVENT(HIGH)

(**Use of a routing scheme and highest priority, multiple re-transmission, unless acknowledged or an action occurs**)

EMERGENCY_EVENT (X)

Select ROUTING_SCHEME_EMER
Set PRIORITY = X

WHILE ((ACK=NOT TRUE) or (ACTION=YES))
    Generate TRNSMSN_EVENT (VTL-SGNS)

ABNOR_EVENT (Y)

Select ROUTING_SCHEME_ABNOR
Set PRIORITY = Y

If WT_TM[I] >=RPRT_TM[I]    (**If wait is already over, go ahead and transmit the vital signs**)
Generate TRNSMSN_EVENT (VTL-SGN);
```  
Fig. 6. The protocol used by patient device.

all, healthcare professionals. This requires creation of multicast tree or structure (so some delays), but the reliability of message delivery is signi<sup>fi</sup>cantly enhanced. Broadcast routing, where patient information is sent in all directions to all nodes, will lead to the best reliability of message delivery, but the resulting network traf<sup>fi</sup>c can be excessive. We propose two new routing schemes: reliable multicast and reliable broadcast. Based on persistent transmission of patient information, these routing schemes can lead to a signi<sup>fi</sup>cantly better reliability performance than multicast and broadcast and thus may be more suitable for the transmission of emergency messages, especially when un-cooperative devices exist in the patient monitoring environment. The details of the proposed routing schemes are shown in Fig. 9. Each of these schemes brings its own complexity, overhead and performance in terms of message delivery and end-to-end delays. The impact of patient mobility, limited device range and failures of routing devices is likely to be very different on the reliability of these routing schemes. It may be possible to switch between the types of routing to allow multiple levels of required performance for messages carrying vital-signs of different levels of emergencies. Also, the intermediate routers (or co-operating devices from other patients) must support the choice of routing schemes.

![](/api/attachments/FD3X6CYW/fulltext/images/5a649ee6a71ec4bc090fdef64b8441776e8447bccf2450228c9099cfc89a3a91.jpg)  
Fig. 7. Decision-making for emergencies using patient's blood pressure (BP).

## 2.4. Devices for healthcare professionals

The devices used by healthcare professionals are also an important factor in the end-to-end delivery and reliability of patient monitoring. These devices will receive vital signs from patient monitoring devices, perform processing, and inform or alert healthcare professionals. To implement these functions, the devices for healthcare professionals will perform the following operations:

![](/api/attachments/FD3X6CYW/fulltext/images/c862db7c23dc96bfa27e13e157c618cd0b3cbda002487559ac76f5dac95b3751.jpg)  
Fig. 8. Different routing schemes in operation.

1. Get vital signs from patient monitoring devices via the ad hoc wireless network(s)

2. Filter some duplicate packets using sequence number and patient identi<sup>fi</sup>cation number

3. Download patient medical information from database

4. Integrate the information from two sources to create context-awareness

5. Display information and alerts for healthcare professional

6. Inform devices of other healthcare professionals to avoid duplicate or con<sup>fl</sup>icting set of actions.

The basic components of the device for healthcare professional and decision-making algorithm are shown in Fig. 10. Once the device receives vital signs from ad hoc network, it will download related medical information from the database using a wireline and/or wireless interface based on the network architecture between the device and the medical database. More details of the protocol are shown in Fig. 11.

## 2.5. Reliability of delivery of emergency messages

In addition to routing schemes and protocols for messages carrying vital signs, several enhancements can be added to further improve the reliability of message delivery over ad hoc wireless networks. These include improved power management, highly reliable transmission, and overcoming problematic routers.

## 2.5.1. Improved power management

In ad hoc networks, the amount of power transmitted will affect both the ability of a patient monitoring device to transmit emergency messages and the end-to-end delivery of these messages. Several enhancements to improve power management of patient monitoring devices include transmission of minimal power to reach to the next co-operating device, resulting in a higher level of power conservation and could also lead to an increased level of participation from devices with limited power budget. These enhancements can be supported by informing simple patient monitoring devices the level of power necessary to reach to the next hop and more complex devices to keep track of required power levels from prior transmissions and/or signals from neighboring hops. Addition enhancements for better power management include (a) the use of hop-by-hop acknowledgements to stop any repeated transmissions, (b) minimizing the frequency and the number of vital signs that must be transmitted, (c) special coding and compression of vital signs, including differential ones, to reduce the number of bits that must be transmitted by the patient monitoring device.

## 2.5.2. Reliability enhancements

Possible enhancements for improving the message delivery include (i) increased power transmission for improving the chances of <sup>fi</sup>nding co-operating devices or a healthcare professional, (ii) multiple re-transmissions and hop-by-hop acknowledgements, (iii) increasing the number of cooperating devices (including <sup>fi</sup>xed devices) and healthcare professionals, (iv) transmission of differential value of vital signs, and, (v) use of multiple ad hoc networks. For enhanced reliability of message delivery, ad hoc networks can be proactively formed even with an increased processing and storage for maintaining, updating and creating ad hoc networks.

![](/api/attachments/FD3X6CYW/fulltext/images/3f82915a0924563caf0f4aa7fb93a8dee4e53fb853a17c29e5416fc2fbf44b7d.jpg)  
Fig. 9. Routing protocols used by the proposed patient monitoring network.

## 2.5.3. Dealing with problematic routers

In general, the co-operation of other devices in the routing of emergency messages can be achieved by offering incentives, such as a credit, which can later be utilized for reducing nursing home expenses and membership along with prioritized routing in ad hoc networks. In some cases, the cooperation of other devices can even be made as a requirement to be in a nursing home or hospital. However, even with certain incentives, many devices could remain or become uncooperative, while other devices could become unusable due to failure or limited power resulting in the out-of-range problem (Fig. 12). There are four different ways to overcome potential routing problems with un-cooperative routers:

1. Persist in the transmission involving these devices, which may eventually transmit at reduced power level if the device mobility results in a reduced distance to the nexthop.

![](/api/attachments/FD3X6CYW/fulltext/images/37552b59c770f380bc2cc8f1110ce9c10b7788cb3aa269359090e9aa2a31dccd.jpg)  
Fig. 10. The HP device and protocol.

2. Treat non-cooperation as reduced device density for routing purposes

3. Use reliable multicast and reliable broadcast-based routing schemes. However, a higher level of network traf<sup>fi</sup>c could lead to a signi<sup>fi</sup>cant increase in the end-to-end delay.

4. Detect and exclude un-cooperative devices when planning routing paths as in the formation of a multicast tree. lso offer low priority to un-cooperative routers (devices).

The un-cooperative and unusable routers (Fig. 12) include router D as un-cooperative, B as failed, and F as outof-range either due to its limited power budget or due to the distance to healthcare professional (HP2). In case of routing involving D3, A, and B, the messages will not be delivered to healthcare professional (HP4). The same is true for D2, D1 and F. However, when multicast and broadcast routing involve many more devices, the message will reach to at least one healthcare professional (HP1 and HP2).

```txt
HP device
RECEIVE (VTL_SGNS)

(**Check for duplicate packets**)
For CURR_PAT-ID
    If SEQ (VTL_SGNS) <= CURR_SEQ(VTL_SGNS)
    Discard VTL_SGNS

(** checking if the HP is required to be informed/alerted for these vital signs**)
STATUS = NO
If EMERGENCY_LEVEL = LOW
    For I = 1 to MAX_HP_PAT    (**Check if this patient is assigned to the healthcare professional**)
    If PAT_ID = HP[I]    (**Yes, send ACK to patient's device, process vital signs**)
    Send ACK (PAT_ID)
    PROCESS(VTL_SGNS)
    STATUS = YES
    If STATUS = NO
    If CURR_LOAD_HP < THRESHOLD_HP (**If no, check if HP can handle this additional load**)
    PROCESS(VTL_SGNS)
Else    (**In case of emergency, send ACK to patient's device, process vital signs**)
    Send ACK (PAT_ID)
    PROCESS(VTL_SGNS)
    STATUS = YES
    INFORM_ALL_DEVICES    (**Inform all HP devices that you are processing the vital signs**)

PROCESS(VTL_SGNS)
DOWNLOAD INFO(PAT_ID)    (**Download patient info from the database**)
For all VTL_SGNS
INTEGRATE_INFO[VTL_SGNS, INFO]    (**Integrate information from two sources**)
DISPLAY (INFO, VTL_SGNS, ALERTS)    (**Display and alert healthcare professional**)
UPDATE_INFO(PAT_ID)    (**Update patient's information in the database**)
```  
Fig. 11. The protocol used by device for healthcare professionals.

![](/api/attachments/FD3X6CYW/fulltext/images/203c5c5e7833fcd7e1a03cedd95028218a1c402e0669907fad04783927acf3fe.jpg)  
Fig. 12. Un-cooperative routers and emergency messages.

## 3. Performance evaluation

In this section, we present an analytical model to derive the performance of four routing protocols for the delivery of emergency messages. The model employs probability of <sup>fi</sup>nding other devices in different routing schemes to estimate the end-to-end reliability of message delivery. The delays are computed by measuring queuing and processing delays at all cooperative devices. The network traf<sup>fi</sup>c and cognitive load of healthcare professionals are also evaluated for a combination of emergency and normal patient monitoring conditions. The network traf<sup>fi</sup>c under varying frequency of patient monitoring and level of emergency traf<sup>fi</sup>c will affect the number of patients that can be monitored and also the scalability of the proposed system for emergency messages. We also investigate the performance improvement under <sup>fl</sup>exible load of healthcare professionals, where some of them may get more messages.

## 3.1. Analytical model

The following assumptions were made to keep the analytical model tractable and reasonably accurate:

1. The end-to-end path between patients and healthcare professionals is pure ad hoc networks based. This is more complex than that in practice where a combination of wireless LANs and ad hoc networks could be used, and thus is likely to underestimate the end-to-end performance.

2. All devices have equal power budget or range, and processing power. This is a simplifying assumption as in practice many patient monitoring devices are likely to be diverse, and thus will overestimate the performance.

3. The devices are uniformly distributed in the service area. This is a simplifying assumption as in real-life more patients will be clustered.

4. All devices in the ad hoc network can be used as cooperating device for routing purposes.

These assumptions will be relaxed in future work, where potential reduction in performance due to diversity of devices in power and processing along with uneven user distribution will be studied. Before presenting the details of analytical model, the symbols used in the analytical model are shown in Table 1 for better readability of the model.

In the analytical model, the focus is on emergency messages, which can be routed by one of four proposed routing schemes: multicast, broadcast, reliable multicast, and reliable broadcast. Each of these schemes could add its own set of performance challenges in terms of the reliability of message delivery, monitoring delays, cognitive load for healthcare professionals, and scalability of patient monitoring system. To evaluate and compare the routing schemes, we derive equations for these performance attributes using number of co-operating devices, device distribution function, size of covered area, frequency of monitoring, number of hops between patients and healthcare professionals, and traf<sup>fi</sup>c per emergency and normal events.

The maximum number of routes can be computed as follows:

$$
N _ {\mathrm{R}} = (N _ {\mathrm{E}} \times D _ {\mathrm{E}}) (N _ {\mathrm{E}} \times D _ {\mathrm{E}} - 1) / 2\tag{1}
$$

Where $N _ { \mathrm { E } }$ is the number of co-operating devices. $D _ { \mathrm { E } }$ is the devices distribution function, which represents how devices are spread out in a given area, such as a nursing home or a hospital <sup>fl</sup>oor. The value of $D _ { \mathrm { E } }$ will be higher if devices are more evenly distributed in the service area and could be low if many devices are concentrated in a smaller area (clustered) as shown in Fig. 13. These two cases can be de<sup>fi</sup>ned as uniform and clustered distributions. There are many other ways in which users can be distributed over a service area such as multi-clustered with large and mostly empty spaces between clusters.

Variables used in the analytical model

<table><tr><td>Symbol</td><td>Meaning</td></tr><tr><td> $A$ </td><td>Length of the rectangular service area</td></tr><tr><td> $B$ </td><td>Width of the rectangular service area</td></tr><tr><td> $C_{E}$ </td><td>The coverage of an individual device</td></tr><tr><td> $C_{L}$ </td><td>The cognitive load of a healthcare professional (messages/s)</td></tr><tr><td> $D_{E}$ </td><td>The devices distribution function</td></tr><tr><td> $D_{EM}$ </td><td>The delay for emergency messages</td></tr><tr><td> $D_{n}$ </td><td>The number of healthcare professionals in patient monitoring</td></tr><tr><td>FoM</td><td>The average frequency of monitoring</td></tr><tr><td>FoMi</td><td>The frequency of monitoring for  $i$ th patient</td></tr><tr><td> $H$ </td><td>The number of hops</td></tr><tr><td> $N$ </td><td>The number of patients under monitoring</td></tr><tr><td> $N_{E}$ </td><td>The number of co-operating devices</td></tr><tr><td> $N_{P}$ </td><td>The number of paths used for routing a message</td></tr><tr><td> $N_{PM}$ </td><td>Number of packets generated in patient monitoring per normal event</td></tr><tr><td> $N_{PRE}$ </td><td>Number of packets generated by the network routing in emergency event</td></tr><tr><td> $N_{PRN}$ </td><td>Number of packets generated by the network routing in normal event</td></tr><tr><td> $N_{R}$ </td><td>The maximum number of routes</td></tr><tr><td> $P$ </td><td>Processing power of a node in messages/s</td></tr><tr><td> $P_{A}$ </td><td>Probability of finding a single (unicast) path to a destination</td></tr><tr><td> $P_{B}$ </td><td>Probability of finding a broadcast path to a destination</td></tr><tr><td> $P_{E}$ </td><td>Probability of emergency monitoring event</td></tr><tr><td> $P_{N}$ </td><td>Probability of normal monitoring event</td></tr><tr><td> $R_{B}$ </td><td>Reliability of message delivery using broadcast routing</td></tr><tr><td> $R_{M}$ </td><td>Reliability of message delivery using multicast routing</td></tr><tr><td> $R_{RB}$ </td><td>Reliability of message delivery using reliable broadcast routing</td></tr><tr><td> $R_{RM}$ </td><td>Reliability of message delivery using reliable multicast routing</td></tr><tr><td> $S_{PE}$ </td><td>Size of packets for emergency monitoring events</td></tr><tr><td> $S_{PN}$ </td><td>Size of packets for normal monitoring events</td></tr><tr><td> $T_{P}$ </td><td>The network traffic per patient</td></tr><tr><td> $U_{E}$ </td><td>The next-hop device probability</td></tr><tr><td> $Z$ </td><td>The number of different levels of patient monitoring frequency</td></tr></table>

## 3.1.1. The reliability of message delivery

The reliability of message delivery can be measured in terms of probability of message reception, which is dependent on the ranges of patient devices, number of cooperating devices, number of routes, and the number of target receivers, which in turn is in<sup>fl</sup>uenced by the choice of routing scheme. In simple terms, the probability of message reception is the probability that a route can be found to a destination user. The probability of <sup>fi</sup>nding a path to a destination user is a joint probability of <sup>fi</sup>nding a minimum number of devices needed to form a path between a patient and a healthcare professional. First, we attempt to derive the probability of <sup>fi</sup>nding a nearby user (device), which will be in<sup>fl</sup>uenced by individual device distribution function $( D _ { \mathrm { E } } ) ,$ total area, the number of users, device range, mobility level, obstacles, interference, and co-relation between user locations where users are together in a room/location for some reason. In simpler terms, the next-hop device probability can be approximated as

$$
U _ {\mathrm{E}} = \min (D _ {\mathrm{E}} \times N _ {\mathrm{E}} \times C _ {\mathrm{E}} / A \times B, 1)\tag{2}
$$

Regular (unicast) routing involves exactly one path between patient and a certain healthcare professional (assigned to this patient), while anycast routing <sup>fi</sup>nds a path between a patient and any healthcare professional. Multicast routing builds M paths between a patient and professionals, while broadcast will use maximum number of possible paths. We choose to use regular multicast and broadcast, and highly reliable version of multicast and broadcast routing. Now the end-to-end reliability for multicast and broadcast-based routing for emergency vital signs and parameters can be expressed as

$$
R _ {M} = \sum_ {J = 1} ^ {M} ^ {M} C _ {J} \times (P _ {\mathrm{A}}) ^ {J} \times (1 - P _ {\mathrm{A}}) ^ {M - J}\tag{3}
$$

Where $P _ { \mathrm { { A } } }$ can be given by $\sum _ { I = 1 } ^ { D _ { n } } { \cal D } n _ { C _ { I } ( U _ { \mathrm { E } } ) } { } ^ { I } ( 1 - U _ { \mathrm { E } } ) ^ { D _ { n } - I }$

$$
R _ {\mathrm{B}} = \sum_ {K = 1} ^ {D _ {n}} ^ {D n} C _ {k} (P _ {\mathrm{B}}) ^ {K} (1 - P _ {\mathrm{B}}) ^ {D _ {n} - K}\tag{4}
$$

Where $P _ { \mathrm { B } }$ or probability of <sup>fi</sup>nding a broadcast path to a destination can be given as $P _ { \mathrm { B } } { = } 1 { - } ( \bar { 1 } { - } R _ { U } ) ^ { \mathrm { P P } }$ and $R _ { U } = \big ( 1 - U _ { \mathrm { E } } ^ { N } \big ) /$ $( 1 - U _ { \mathrm { E } } )$ ·N and PP (the number of paths that exist between a patient and a professional) can be expressed as $( N _ { \mathrm { E } } / D _ { \mathrm { n } } ) ( N _ { \mathrm { E } } /$ $D _ { n } { - } 1 )$ , where $D _ { n }$ is the number of healthcare professionals involved in patient monitoring.

![](/api/attachments/FD3X6CYW/fulltext/images/bf6d9227ac86d3e4ddc2ab2a43cd29821d1b6c5beb2a1ffac4ce81cfd8288b43.jpg)  
Fig. 13. Distribution of users and corresponding values of $D _ { \mathrm { E } } .$

The reliability of message delivery for reliable multicast routing can be expressed as

$$
R _ {\mathrm{RM}} = \sum_ {J = 1} ^ {Q} ^ {Q} C _ {J} \times (R _ {M}) ^ {J} \times (1 - R _ {M}) ^ {Q - J}\tag{5}
$$

Where Q is the number of attempts made by reliable multicast routing to deliver an emergency message. The reliability of message delivery for reliable broadcast routing can be expressed as

$$
R _ {\mathrm{RB}} = \sum_ {K = 1} ^ {G} ^ {G} C _ {K} \times (R _ {\mathrm{B}}) ^ {K} \times (1 - R _ {\mathrm{B}}) ^ {G - K}\tag{6}
$$

Where G is the number of attempts by reliable broadcast routing to deliver an emergency message to one or more healthcare professional.

## 3.1.2. The end-to-end delays

The end-to-end delays for emergency messages depend on the frequency of monitoring, the number of paths used in the routing, number of co-operating devices, processing power of each co-operating device, and the number of users that should be monitored. The average delay for all emergency messages across H hops can be expressed as follows:

$$
D _ {\mathrm{EM}} = (1 / H) \sum_ {K = 1} ^ {H} K \times 1 / \left(P - \left(\sum_ {i = 1} ^ {N} \text { FoMi }\right) \times \mathrm{N} _ {\mathrm{p}} / N _ {\mathrm{E}}\right)\tag{7}
$$

Where H is the number of hops, P is the processing power of nodes in messages/s, FoMi represents frequency of monitoring for ith patient, $N _ { \mathrm { p } }$ is the number of paths used for routing a message, and $N _ { \mathrm { E } }$ is number of co-operating devices. N represents the number of patients that must be monitored. The Eq. (7) can be used to derive delays for four proposed routing schemes by using different number of paths used by a routing scheme. For reliable multicast and reliable broadcast, the total delay will include waiting time between retransmission, number of re-transmissions, and delays per transmission as derived from Eq. (7).

## 3.1.3. The cognitive load for healthcare professionals

As suitable medical decisions must be made for many patients by a healthcare professional, one major challenge would be to keep the amount of processing load, termed cognitive load, at a reasonable level. This would reduce the number of decision making errors by healthcare professionals. Although several factors will affect the cognitive load, we focus on the number of messages that must be received and processed by an individual healthcare professional. Such load can vary widely based on the frequency of monitoring, number of patients that must be monitored, the number of messages per monitored event, and the number of healthcare professionals involved. Thus the cognitive load of individual healthcare professional can be expressed as:

$$
C _ {\mathrm{L}} = \left(1 / D _ {n}\right) \sum_ {i = 1} ^ {N} \left(\text { FoMi } \times N \times (N _ {\mathrm{PRN}} + N _ {\mathrm{PRE}})\right)\tag{8}
$$

There are many ways to manage the cognitive load including increasing the number of healthcare professionals $( D _ { n } ) ,$ reducing the frequency of monitoring (FoMi), and <sup>fi</sup>ltering or combining packets. The frequency of monitoring could be reduced by focusing on abnormal and emergency vents only. The devices of healthcare professionals could be programmed to <sup>fi</sup>lter packets using one or more prespeci<sup>fi</sup>ed criteria. Also, once a healthcare decision has been made by one healthcare professional for an event, a message can be sent to others to stop additional processing for the same event. Also, many other improvements could be tried including the use of uneven load to match individual abilities of healthcare professionals, use of context-awareness of which healthcare professional is busy in routing of messages, and adapting of multiple parameters in Eq. (8) to the current load of healthcare professionals. As the abilities and level of alertness of healthcare professionals can vary throughout a shift or day to day, the intelligent routing of messages can include the current known conditions of healthcare professionals as a decision making criterion. Certainly much more work can be done in this area for wireless health monitoring using improved decision making by healthcare professionals and also by network infrastructure in routing messages to them. The derivation and effective use of context awareness can both improve the quality of medical decision making as well as the workload of healthcare professionals.

## 3.1.4. Network traffic and scalability

Network traf<sup>fi</sup>c per monitored patient is a function of several factors, including frequency of monitoring, probability of normal and emergency events, number and size of packets per event. The total traf<sup>fi</sup>c generated per patient can be given as

$$
T _ {P} = \operatorname{FoM} (P _ {\mathrm{N}} \times N _ {\mathrm{PM}} \times N _ {\mathrm{PRN}} \times S _ {\mathrm{PN}} + P _ {\mathrm{E}} \times N _ {\mathrm{PM}} \times N _ {\mathrm{PRE}} \times S _ {\mathrm{PE}})\tag{9}
$$

Where $P _ { \mathrm { N } }$ and $P _ { \mathrm { E } }$ are probabilities of normal and emergency events, respectively. $N _ { \mathrm { P M } }$ is the number of packets generated in patient monitoring per event. $N _ { \mathrm { P R N } }$ and $N _ { \mathrm { P R E } }$ are the number of packets generated by the network routing in normal and emergency events, respectively. $S _ { \mathrm { P N } }$ and S represent size of packets for normal and emergency events, respectively. The four proposed routing schemes will vary in terms of $N _ { \mathrm { P R N } }$ and $N _ { \mathrm { P R E } }$

For scalability of the proposed patient monitoring network in terms of the number of users supported, the traf<sup>fi</sup>c per user should be kept to a more or less constant level. This can be achieved if the following relationship more or less holds:

$$
\begin{array}{r l} P _ {\mathrm{N}} \times N _ {\mathrm{PRN}} \times S _ {\mathrm{PN}} + (1 - P _ {\mathrm{N}}) \times N _ {\mathrm{PRE}} \times S _ {\mathrm{PE}} \\ = K / \mathrm{FoM} \times N _ {\mathrm{PM}} \end{array}\tag{10}
$$

This can be attempted by adjusting the number of messages generated by routing scheme and/or the size of message carrying patient information with changing probability of emergency. For example if the number of emergency events increases by three times, then the routing scheme can reduce the number of messages it generates or the message size (by differential values of vital signs and parameters) by about the same factor.

## 3.1.5. Impact of un-cooperative nodes

The impact of un-cooperative nodes (as shown in Fig. 12) can be measured in terms of reduced number of devices available for routing. Although, in some cases, an uncooperative device could be the difference between delivery and non-delivery of emergency messages in unicast type routing (single destination and single route), in general multicast and broadcast-based routing schemes are likely to overcome the reliability degradation. The impact of uncooperative devices can be measured in terms of reduced next-hop device probability as follows:

$$
U _ {\mathrm{E-UN}} = U _ {\mathrm{E}} (1 - P _ {\mathrm{UN}})\tag{11}
$$

Where $U _ { \mathrm { E - U N } }$ is the next-hop device probability with uncooperative devices and $P _ { \mathrm { U N } }$ is the probability of encountering an un-cooperative device. The impact on individual routing schemes can be estimated by Eqs. (11) and (3–6). The impact of un-cooperative devices can be compensated, in parts, by reducing clustering of other devices, increased power transmission, and future routing schemes requiring fewer devices for routing.

## 3.2. Performance results

The parameters used in deriving performance results for four routing schemes were 300 users, 3 healthcare professionals, and 18 co-operating devices. For multicast-based routing, the number of routes was 9 and for broadcast-based routing it was 45. The number of attempts by reliablebroadcast and reliable-multicast were two.

One of the most important requirements of emergency messages, the reliability of message delivery, was measured by varying the next-hop device probability. This probability is a function of number of co-operating devices and could model the user distribution and routing problems due to failure, outof-range, and non-cooperation of devices. In simpler terms, a low value of next-hop device probability represents nonuniform distribution of users including one or more clusters and/or a signi<sup>fi</sup>cant level of non-cooperation with available devices. As shown in Fig. 14, lower values of next-hop device probability affect the reliability of message delivery for multicast routing. Although, 98% reliability may be acceptable when vital signs are in normal range, however, for emergency messages this is less than satisfactory. The other three routing schemes are able to achieve 99.8% or better delivery rate under low to medium next-hop device probability. As an increased number of devices become co-operative or can <sup>fi</sup>nd other devices in range for continued routing, all four routing schemes provide near 100% reliability of message delivery.

![](/api/attachments/FD3X6CYW/fulltext/images/3a9a3316284b8ce8f8b5067d89256f11d849c96770935ad3cc9a8ba0e980b2b9.jpg)  
Fig. 14. Reliability of message delivery for four routing protocols

![](/api/attachments/FD3X6CYW/fulltext/images/717d19c84c8a225249c222fe13207ac8b3af82e9ecbd5ae37fb8d8ad84144607.jpg)  
Fig. 15. EMD for emergency messages for four routing protocols.

In addition to end-to-end reliability performance, another crucial factor is the end-to-end monitoring delay. As routing schemes generates a range of network traf<sup>fi</sup>c due to different number of paths and number of hops per path for every monitored event, the delays are likely to be variable. We measured the delays by varying the frequency of monitoring from one in 300 s to one in 10 s, and by keeping the traf<sup>fi</sup>c composition to 90% regular and 10% emergency messages. As shown in Fig. 15, the end-to-end delays for patient monitoring remained low for multicast and broadcast, however, with increased frequency of monitoring delays grow signi<sup>fi</sup>cantly for broadcast routing and also for reliable broadcast. This can be explained due to the potential excessive traf<sup>fi</sup>c generated by these two routing schemes. Multicast and reliable multicast showed little increase in delays as these two schemes lead to a more moderate level of network traf<sup>fi</sup>c.

One of the important factors in the success of patient monitoring system is the ability to keep the cognitive load of healthcare professionals to a reasonable level. It can be said that there are multiple factors and tasks that would affect such load, however from network point of view, the number of messages that must be received and processed by a healthcare professional could be a measure of cognitive load. As shown in Fig. 16, the number of messages to all healthcare professionals increases rapidly for reliable multicast and reliable broadcast schemes, however, the load for multicast and broadcast increases less rapidly. In future, an uneven number of messages delivered to a healthcare professional based on a matching of current load based on other tasks could be explored. Also, the differences in cognitive load for different professionals could be studied. The number of messages can also be reduced by <sup>fi</sup>ltering of messages at healthcare professionals' device using sequence number and patient id. This additional information in a packet will lead to increased overhead at the network due to larger sized packets, and also any incorrect <sup>fi</sup>ltering of an emergency message could lead to major problems for certain patient.

![](/api/attachments/FD3X6CYW/fulltext/images/79e59f62670b78c0df34e94b9ada60dfa246a44fba974e60a3d6812bf311bcd3.jpg)  
Fig. 16. The number of messages generated by routing schemes.

The scalability of a patient monitoring system can be determined by the traf<sup>fi</sup>c generated by routing schemes and the way vital signs are used to prepare messages. The amount of network traf<sup>fi</sup>c generated per user can be used to measure the scalability of a patient monitoring system. Using 500 bytes as the size for normal packet and 100 bytes for packet carrying differential vital signs, the traf<sup>fi</sup>c per user is shown in Fig. 17. If simple routing was done where all packets carry the current values of vital signs, the rate of traf<sup>fi</sup>c growth is very high, thus negatively affecting the scalability or the number of patients that can be monitored. However, when differential vital signs were transmitted for normal (not emergency cases), the rate of traf<sup>fi</sup>c increase was much lower even with a signi<sup>fi</sup>cant increase in the number of emergency events.

It is found that an increased emergency traf<sup>fi</sup>c resulted in an increased delays and fewer number of patients that can be monitored. The following conclusions on the achievable performance can be stated here:

• It is possible to achieve almost 100% reliability of delivery of emergency messages specially if broadcast, reliable-multicast, or reliable-broadcast routing schemes can be employed. Multicast based routing scheme can achieve close to 100% reliability for cases involving more uniformly distributed patients and/or fewer non-cooperating devices. Multicast routing is also shown to be affected the most by non-cooperation of routing devices.

• It is possible to achieve very low delays, however the routing schemes that produce nearly 100% reliability also result in a signi<sup>fi</sup>cant network routing traf<sup>fi</sup>c, thus leading to higher delays. Very low delays can be achieved by multicast and broadcast routing schemes. More speci<sup>fi</sup>cally, we found that multicast could lead to the lowest delays even under very frequent patient monitoring and/or emergency events. Overall, multicast and broadcast routing schemes can be used to increase the reliability of transmission of emergency signals while keeping the monitoring delays at low levels.

![](/api/attachments/FD3X6CYW/fulltext/images/8d8dfac7905946b30f636f808aee8d23d7fea8477154634c5592f1313e7e1380.jpg)  
Fig. 17. The network traf<sup>fi</sup>c/user with varying levels of emergency.

• In practice, scalability, in terms of number of patients that can be supported or the frequency of monitoring, will also be an important criterion. An increased number and frequency of emergency messages result in signi<sup>fi</sup>cant network routing traf<sup>fi</sup>c and this non-linear transmission overhead of emergency messages could affect scalability. We found that for a given routing scheme, transmission of differential vital signs could lead to improved scalability. Additional enhancements are necessary, including adapting one or more monitoring parameters, to achieve a higher level of scalability.

• Not as paramount as reliability of message delivery and monitoring delays, the cognitive load of healthcare professionals could affect the usefulness of the proposed patient monitoring system. We found that multicast and broadcastbased schemes lead to fewer messages per healthcare professional. Many device and routing enhancements could lead to a more reasonable level of load for patient monitoring.

## 4. Conclusions and future work

Patient monitoring using wireless technologies has been considered for improving the quality of healthcare to an increased number of patients, especially those in nursing homes and hospitals. During the patient monitoring, some vital signs could <sup>fl</sup>uctuate signi<sup>fi</sup>cantly and potentially cross thresholds, resulting in “alerts” or emergency messages. These emergency messages must be reliably delivered to healthcare professionals with minimal delays. In this paper, we presented a framework designed to support the requirements of patient monitoring, including emergency messages which require very high levels of reliability and low delays. The novelty in the proposed work involves the use of ad hoc wireless networks for increasing the reliability of emergency message transmission. The performance of routing schemes presented in the framework, namely multicast, broadcast, reliable multicast and reliable broadcast for delivery of emergency messages, is also evaluated using analytical modeling techniques. The performance results show that reliable message delivery and low monitoring delays can be achieved by using multicast or broadcast-based routing schemes. Using many proposed enhancements, the system is shown to be scalable and the resulting cognitive load on healthcare professionals is found to be reasonable, and relates to the routing protocols used and reliability requirements of patient monitoring. The future work should involve implementing ad hoc networks and routing schemes for mobile patients, and measure real-life performance. The work could be extended to support highly personalized healthcare services to people in nursing homes, assisted living, homes, and while being mobile. The emerging advances in smart wearable devices and embedded sensors in clothing can lead to implementation of many of the ideas presented in this paper.

## Acknowledgements

This research was supported, in part, by research grants from National Science Foundation (SCI# 0439737) and Robinson College (RPC) of Georgia State University.

## References

[1] G. Anogianakis, S. Maglarera, A. Pomportsis, Relief for maritime medica emergencies through telematics, IEEE Transactions on Information Technologies in Biomedicine 2 (4) (1998)

[2] P. Bauer, M. Sichitiu, R. Istepanian, K. Premaratne, The mobile patient: wireless distributed sensor networks for patient monitoring and care, Proc. IEEE EMBS International Conference on Information Technolog Applications in Biomedicine, Arlington, VA, 2000.

[3] A. Bhargava, M. Zoltowski, Sensors and wireless communication for medical care, Proc.14th International Workshop on Database and Expert Systems Applications, 2003.

[4] C. Bielza, J. Fernández del Pozo, P.J.F. Lucas, Explaining clinical decisions by extracting regularity patterns, Decision Support Systems 44 (2) (2008).

[5] O. Boric-Lubecke and V.M. Lubecke, Wireless house calls: using communications technology for health care and monitoring, IEEE Microwave Magazine (2002).

[6] S. Brahnam, C.F. Chuang, R.S. Sexton, F.Y. Shih, Machine assessment of neonatal facial expressions of acute pain, Decision Support Systems 43 (4) (2007).

[7] J.M. Corchadoa, J. Bajo, Y. Paza, D.I. Tapiaa, Intelligent environment for monitoring Alzheimer patients, agent technology for health care, Decision Support Systems 44 (2) (2008).

[8] I.A. Gieras, The proliferation of patient-worn wireless telemetry technologies within the U.S. healthcare environment, Proc. 4th International IEEE EMBS Special Topic Conference on Information Technology Applications in Biomedicine, 2003.

[9] P.J.H. Hu, C.P. Wei, T.H. Cheng, J.X. Chen, Predicting adequacy of vancomycin regimens: a learning-based classi<sup>fi</sup>cation approach to improving clinical decision making, Decision Support Systems 43 (4) (2007).

[10] K. Hung, Y.T. Zhang, Implementation of a WAP-based telemedicine system for patient monitoring, IEEE Transactions on Information Technologies in Biomedicine 7 (2) (2003).

[11] R.S.H. Istepanian. A.A. Petrosian, Optimal zonal wayelet-based ECG data compression for a mobile telecardiology system, IEEE Transactions on Information Technology in Biomedicine 4 (3) (2000).

[12] E. Jovanov, A. O'Donnel, A. Morgan, B. Priddy, R. Hormigo, Prolonged telemetric monitoring of heart rate variability using wireless intelligent sensors and a mobile gateway, In Proc. Second Joint IEEE EMBS/BMES Conference, 2002.

[13] E. Jovanov, A. O'Donnell Lords, D. Raskovic, P.G. Cox, R. Adhami, and F. Andrasik, Stress monitoring using a distributed wireless intelligent sensor system, IEEE Engineering in Medicine and Biology Magazine 22 (3) (2003).

[14] E. Kafeza, D.K.W. Chiu, S.C. Cheung, M. Kafeza, Alerts in mobile healthcare applications: requirements and pilot study, IEEE Transactions on Information Technologies in Biomedicine 8 (2) (2004).

[15] A. Kara, Protecting privacy in remote-patient monitoring, IEEE Computer 34(5) (2001).

[16] S.E. Kern and D. Jaron, Healthcare technology, economics and policy: an evolving balance, IEEE Engineering in Medicine and Biology Magazine 22(1) 2003.

[17] S. Khoor, K. Nieberl, K. Fugedi, E. Kail, Telemedicine ECG-telemetry with Bluetooth technology, Proc. Computers in Cardiology, 2001.

[18] J.C. Kyu, H.H. Asada, Wireless, battery-less stethoscope for wearable health monitoring, Proc. the IEEE 28th Annual Northeast Bioengineering Conference, 2002.

[19] R.G. Lee, H.S. Shen, C.C. Lin, K.C. Chang, J.H. Chen, Home telecare system using cable television plants—an experimental <sup>fi</sup>eld trial, IEEE Transactions on Information Technologies in Biomedicine 4 (1) (2000).

[20] R. Lee, K. Chen, C. Hsiao. C. Tseng, A mobile care system with alert mechanism, IEEE Transactions on Information Technology in Biomedicine 11 (5) (2007).

[21] F. Li, K. Wu, Reliable, distributed and energy-ef<sup>fi</sup>cient broadcasting in multi-hop mobile ad hoc networks. Proc. 27th IEEE Conference on Local Computer Networks, 2002.

[22] B. Lin, N. Chou, F. Chong, S. Chen, RTWPMS: a real-time wireless physiological monitoring system, IEEE Transactions on Information Technology in Biomedicine 10 (4) (2006).

[23] C. Lin, M. Chiu, C. Hsiao, R. Lee, Y. Tsai, Wireless health care service system for elderly with dementia, IEEE Transactions on Information Technology in Biomedicine 10 (2) (2006).

[24] L. Lin, P. J-H Hu, O.R.L. Sheng, A decision support system for lower back pain diagnosis: uncertainty management and clinical evaluations, Decision Support Systems 42 (2) (2006).

[25] K. Liszka, M. Mackin, M. Lichter, D. York, D. Pillai, and D. Rosenbaum, Keeping a Beat on the Heart, IEEE Pervasive Computing, 3(4) (2004).

[26] A. Lymberis, A. Smart, Wearables for remote health monitoring, from prevention to rehabilitation: current R&D. future challenges. Proc. 4th International IEEE EMBS Conference on Information Technology Applications in Biomedicine, 2003.

[27] G.G. Mendoza, B.Q. Tran, In-home wireless monitoring of physiological data for heart failure patients, Proc. of the Second Joint IEEE EMBS/ BMES. 2002.

[28] W. Michalowski, S. Rubin, R. Slowinski, S. Wilk, Mobile clinical support system for pediatric emergencies, Decision Support Systems 36 (2) (2003).

[29] M. Mikkonen, S. Vayrynen, V. Ikonen, M.O. Heikkila, User and Concept Studies as Tools in Developing Mobile Communication Services for the Elderly, Springer-Verlag’s Personal and Ubiquitous Computing, vol. 6, 2002.

[30] S. Modarreszadeh, Wireless, 32-channel, EEG and epilepsy monitoring system, Proc. 19th Annual IEEE International Conference on Engineering in Medicine and Biology, 1997.

[31] C.S. Pattichis, E. Kyriacou, S. Voskarides, M.S. Pattichis, R. Istepanian and C.N. Schizas, Wireless telemedicine systems: an overview, IEEE Antenna's and Propagation Magazine 44(2) (2002).

[32] S. Pavlopoulos, E. Kyriacou, A. Berler, S. Dembeyiotis, D. Koutsouris, Novel emergency telemedicine system based on wireless communication technology—AMBULANCE, IEEE Transactions on Information Technology in Biomedicine 2 (4) (1998)

[33] J.K. Pollard, S. Rohman, M.E. Fry, A web-based mobile medical monitoring system, International Workshop on Intelligent Data Acquisition and Advanced Computing Systems: Technology and Applications, 2001.

[34] K. Raatikainen, H. Christensen, and T. Nakajima, Application requirements for middleware for mobile and pervasive systems, ACM mobile computing and communications review (MC2R) 6(4) (2002).

[35] S. Rhee, B.H. Yang, K. Chang, H.H. Asada, The ring sensor: a new ambulatory wearable sensor for twenty-four hour patient monitoring, Proc. 20th Annual IEEE International Conference on Engineering in Medicine and Biology, 1998.

[36] J.P. Shim, M. Warkentin, J. Courtney, D.J. Power, R. Sharda, C. Carlsson, Past, present, and future of decision support technology, Decision Support Systems 33 (2) (2002).

[37] W. Stallings, Wireless Communications and Networks, First ed.Prentice Hall, NJ, 2002.

[38] V. Stanford, Using pervasive computing to deliver elder care, IEEE Pervasive Computing Magazine, 1(1) (2002).

[39] T. Suzuki, M. Doi, LifeMinder: an evidence-based wearable healthcare assistant Proc, ACM CHL Conference, 2001

[40] P. Varday, Z. Benyo, B. Benyo, An open architecture patient monitoring system using standard technologies, IEEE Transactions on Information Technologies in Biomedicine 6 (1) (2002).

[41] U. Varshney, and R. Vetter, Emerging Wireless and Mobile Networks, Communications of the association for computing machinery (ACM) 43 (6) (2000).

[42] U. Varshney, Wireless networks for patient monitoring, Proc. Americas Conference on Information Systems (AMCIS), 2004

[43] U. Varshney, Pervasive healthcare, IEEE Computer 36(12) (2003).

[44] U. Varshney. The status and future of 802.11-based WLANs. IEEE Computer 36(6) (2003).

[45] U. Varshney, Patient monitoring using infrastructure-oriented wireless LANs, International Journal on Electronic Healthcare 2 (2) (2006).

[46] U. Varshney, Support for emergency message transmission, Proceedings of Hawaii International Conference on Systems Sciences (HICSS), 2006.

[47] U. Varshney, Managing wireless health monitoring for patients with disabilities, IEEE IT Professional 8(6) (2006).

[48] Vital Signs: MedlinePlus, at http://www.nlm.nih.gov/medlineplus/ ency/article/002341.htm.

[49] Website for ECG: http://library.med.utah.edu/kw/ecg/ecg\_outline/Lesson1/index.html.

Upkar Varshney is on the faculty of CIS at Georgia State University. His current interests include wireless networks, pervasive healthcare, and mobile commerce. In 2006, he was ranked among the most productive (top 1%) Information Systems researchers in the World for 2001–2005. He is the cofounder (with Prof. Imrich Chlamtac) of International Pervasive Health Conference and also co-chaired the conference in 2006. Upkar is also the program co-chair for Americas Conference on Information Systems (AMCIS-2009) in San Francisco.

He has authored over 120 papers including more than 50 in journals. Widely known for his contributions, he is the author of some of the most cited papers in wireless networks and mobile commerce. The total number of citations (in journals and conferences) for his top ten papers exceeds one thousand. He is also the author of the some of the most downloaded and viewed papers including ACM Transactions in 2004 (out of 25 ACM transactions of 4000 papers) and ACM/Springer MONET in 2005 (out of about 400 papers).

Upkar has presented over <sup>fi</sup>fty very well received tutorials, workshops, and keynotes at major wireless, computing, and information systems conferences. He has also received grants from several funding agencies including the prestigious

National Science Foundation. Hundreds of students have ranked him as their best professor at Georgia State University. His teaching awards include Myron T. Greene Outstanding Teaching Award (2004), RCB College Distinguished Teaching Award (2002), and, Myron T. Greene Outstanding Teaching Award (2000). He is or has been an editor/guest editor for journals such as ACM/Kluwer MONET, IEEE Computer, Decision Support Systems (DSS), Communications of the AIS (CAIS), Int. J. on Network Management (IJNM), Int. Journal on Mobile Communications (IJMC), Int. Journal of Wireless and Mobile Computing (IJWMC), and Handbook of Research on Mobile Business.
