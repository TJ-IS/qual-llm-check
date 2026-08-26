---
otero_id: 11258
otero_key: "MQYVFAD9"
title: "A framework for enabling patient monitoring via mobile ad hoc network"
authors: "Sweta Sneha; Upkar Varshney"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.01.024"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Sweta Sneha <sup>a,</sup>⁎, Upkar Varshney 1

<sup>a</sup> Department of Information Systems, Kennesaw State University, Kennesaw, GA 30144, United State

<sup>b</sup> Department of Computer Information Systems, Georgia State University, Atlanta, GA 30302, United States

## a r t i c l e i n f o

Article history: Received 1 March 2011 Received in revised form 21 October 2012 Accepted 21 January 2013 Available online 12 February 2013

Keywords: Patient monitoring Healthcare Decision framework Mobile ad hoc network Protocols

## a b s t r a c t

A critical component of comprehensive patient monitoring is reliability in communication between the patients and the healthcare professionals without any time and location dependencies. Patient monitoring applications largely rely on infrastructure based wireless networks for signal transmission. However, infrastructure based wireless networks till date, suffer from unpredictable network coverage and have thus been attributed to the unpredictable communication reliability of patient monitoring applications. This research investigates an approach based on leveraging mobile ad hoc network to address the challenge of enhancing communication reliability in the context of patient monitoring, Mobile ad hoc network formed among patient monitoring devices, has the potential of enhancing network coverage and enabling signal transmission from an area which has low or non-existent coverage from infrastructure based networks. In order to utilize mobile ad hoc network in the context of patient monitoring we propose (1) power management protocols that address the challenge of managing the low battery power of patient monitoring devices while maximizing communication reliability and (2) a framework that models the complex decision logic involved in leveraging mobile ad hoc network for diverse patient monitoring scenarios. Analytical evaluation of the proposed approach supports the premise that mobile ad hoc network formed among patient monitoring devices can enhance the reliability of signal transmission thereby improving the quality of patient monitoring applications. Technical and managerial implications of the research <sup>fi</sup>ndings and the direction of future research are discussed.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

Healthcare systems around the globe are experiencing an exponential rise in aging population (expected to reach 761 million by 2025) followed by a corresponding rise in healthcare expenses (projected to reach 20% of the GNP by 2015 for US) and heavy utilization of healthcare services [5,10,15,50,53]. Comprehensive patient monitoring enabled by information communication technologies is widely recognized as an effective tool in containing healthcare expenses, ef<sup>fi</sup>ciently managing chronic diseases, reducing complications and unnecessary hospitalizations, and facilitating ef<sup>fi</sup>cient delivery of a wider range of medical services by the healthcare professionals [8,17,62]. Yet concerns with reliable communication in the context of patient monitoring have been highlighted [15,50,56,57,62]. The sole reliance of patient monitoring applications on infrastructure based wireless networks (which inherently suffer from unpredictable spotty coverage) for transmission has largely been attributed to the incumbent volatility in signal transmission, unreliability in communication, and opportunistic security threats by malicious agents [33]. In the current research we investigate the viability of utilizing mobile ad hoc network to augment the coverage of infrastructure based networks with the objective to enhance communication reliability of patient monitoring solutions.

Consider the following case of patient monitoring supported by infrastructure oriented wireless network followed by a proposed approach utilizing mobile ad hoc network (Fig. 1). Patient “X” resides in a nursing home. A device continuously monitors/analyzes his vital signs and wirelessly transmits alerts when an anomaly is detected. A WLAN — an infrastructure-based wireless network, supports alert transmissions. At 9:00 am a nurse making a routine visit, found “X” dead in the restroom. Later investigation revealed that the monitoring device detected an anomaly in the vital signs and made several attempts to transmit the alert. Unfortunately, the transmission failed due to no network in the restroom.

The proposed solution to the preceding fatal case leverages mobile ad hoc network, formed among patient monitoring devices, to transmit the emergency alert from the area where the coverage from the existing infrastructure based network is low and/or non-existent (Fig. 1). In the absence of wireless coverage in the restroom, the patient's monitoring device “X” forms an ad hoc network with the other nearby devices, “F” and “A”. The alert is transmitted to the nurse “Y” via multiple hops (X–A–B–C–D–E–Y) (Fig. 1). The nurse was able to provide pertinent medical attention to $" X "$ and thus a fatal outcome was evaded. The proposed approach doesn't seek to replace the infrastructure based wireless network(s); it merely proposes to supplement the coverage of infrastructure based wireless network(s) by mobile ad hoc network when the coverage from the former is low or non-existent.

![](/api/attachments/MQYVFAD9/fulltext/images/63f62c95cdb937167ffe35c3576be265b1a6170f7d0b198898fa792b9e3dc6cf.jpg)  
Fig. 1. Signal transmission from “X” to “Y” via mobile ad hoc network.

The current research is based on the premise that in order to support comprehensive monitoring of patients involving transmission of emergency alerts, ensuring reliable end to end communication is a critical requirement. Mobile ad hoc network affords the possibility of enhancing communication reliability in an event when an alert needs to be transmitted from an area with low/non-existent coverage from an infrastructure based network [50,57–60]. The current research is among the <sup>fi</sup>rst to tackle the rich problem space of numerous opportunities and challenges associated with leveraging mobile ad hoc network in the context of patient monitoring. Based on this premise, we address the following research question: “How can mobile ad hoc network be leveraged to maximize communication reliability while optimizing the limited battery power of the patient monitoring devices at minimal delays for diverse monitoring scenarios”? We utilize a multifold approach grounded in the unique characteristics of patient monitoring domain to handle the aforementioned research question. The speci<sup>fi</sup>c research objectives include: (a) investigation of the opportunities and challenges of utilizing mobile ad hoc network for comprehensive patient monitoring. (b) assessment of the various elements that facilitate the development of an integrated framework modeling the complex decision logic of optimizing the limited battery power of the monitoring devices while maximizing reliable end to end communication at minimal delays in diverse patient monitoring scenarios, (c) develop protocols to manage the battery power of the patient monitoring devices such that 100% reliability in end to end communication can be achieved, (d) analytical validation of the proposed approach hypothesizing that mobile ad hoc network can enhance communication reliability in the context of patient monitoring. The results validate the utility of the proposed power management protocols in achieving 100% reliability at minimal delays and are likely to open multiple avenues of future research pertaining to the research and practice of patient monitoring.

The remainder of the paper is structured as follows. Section 2 provides background on prior research in patient monitoring and mobile ad hoc network along with discussing unique issues associated with reliability, power management, and delays in the context of mobile ad hoc network for patient monitoring. Section 3 details the proposed (a) power management protocols for managing the low battery power of the patient monitoring devices and (b) framework that integrates the decision logic of utilizing the proposed power management protocols for diverse patient monitoring scenarios with the objective to enhancing reliability while optimizing power usage and delays in the context of leveraging mobile ad hoc network for patient monitoring. Section 4 presents the analytical model and the performance evaluation results of the proposed approach. Section 5 concludes with a discussion of the implications and limitations of the current research followed by the avenues for future research.

## 2. Background — Patient monitoring and mobile ad hoc networks

The following sections discuss: (a) the requirements, complexities, and current state of research with respect to remote patient monitoring and (b) the challenges/opportunities associated with leveraging mobile ad hoc network in enhancing communication reliability of remote patient monitoring.

## 2.1. Remote patient monitoring

Remote patient monitoring typically involves: (1) a Monitoring State which involves sensing and analyzing disease speci<sup>fi</sup>c vital signs, and (2) a Transmit State where recorded data is transmitted via a wired/wireless network if an anomaly is detected. Remote monitoring of patients not only has diverse requirements pertaining to the context of monitoring (indoor stationary patient or mobile patients indoor/outdoor), signal transmission (alert based, periodic, or continuous), delay tolerance (higher delay for non-emergency and lower delay for emergency messages) but also spans multiple disease speci<sup>fi</sup>c parameters such as: duration of monitoring, frequency of data collection and transmission, amount of data transmitted, and nature of monitoring [50]. Moreover, variability in one parameter affects variability in other parameters. For instance: symptoms associated with myocardial infarction can be sensed at least a week before the heart attack hence the application for monitoring heart failure can potentially have a higher delay tolerance whereas an application monitoring critically ill infants may require no delay in alert transmissions. Applications that have higher delay tolerance can withstand slight disruption in connectivity by storing data locally on the monitoring device till the network becomes available for transmission while others with stringent delay requirements may not be able to withstand any disruption in network coverage. Despite the context speci<sup>fi</sup>c variability associated with the requirements of patient monitoring applications, concerns with reliable communication has been widely highlighted as a key factor impeding the wide-scale utility of comprehensive patient monitoring [50,57–59].

First generation monitoring solutions restricted patient mobility and collected/transmitted data within a hospital via WLANs such as: Micropaq that transmits multi-parametric information via WLANs [64] and LifeSync [31] which uses a short range wireless system (Bluetooth). The next generation monitors collected/transmitted patient's vital signs periodically and allowed patients the <sup>fl</sup>exibility to live at home such as: Medtronic [37], Motiva [66], and CardioNet [65]. Today, it is possible to obtain measurements of heart rate, oxygen saturation, end-tidal $\mathrm { C O } _ { 2 } ,$ serum chemistries, and serum glucose via small, non-invasive sensors. Nonin and Numed have developed Bluetooth based wireless vital sign sensors, while Radianse has developed an

RF-based location-tracking system for use in hospitals. European Commission's MobiHealth Project's goal is to provide continuous monitoring of patients outside the hospital via a 3G-enabled “Body-Area Network” [36].

The enhanced opportunities provided by patient monitoring applications accentuate the challenges with respect to security, privacy, con<sup>fi</sup>dentiality, integrity, storage, and access of sensitive health data in a HIPAA compliant fashion [50]. The pervasiveness of patient monitoring devices and the plethora of critical patient information stored on and accessed from the devices create security risks associated with unwarranted access and use of critical healthcare data [3]. The sole reliance of patient monitoring applications on wireless channels for data communication/transfer further increase security threats [33]. Hence, it is vital to explore techniques to assess and manage the increased security risks with the ubiquity of data access and storage, mobility, wireless channels, power etc. with respect to patient monitoring.

Other research related to issues in patient monitoring include “smart health wearable” [35], interference for telemetry devices [14], PDA as a mobile gateway [23], long-term health monitoring by wearable devices [52], smart-shirt based health monitoring, and a wearable stethoscope [30]. Clothing-embedded transducers for measuring ECG, heart rate variability, and acoustical data, and transmitting wirelessly to a central server are proposed [23]. A requirement model for delivering alert messages is presented in [26]. A design approach for mobile tele-cardiology data compression model is presented by [21] who achieved signi<sup>fi</sup>cant compression ratio and reduction in transmission time over GSM network. Personal health monitors via wireless body area network (BAN) of intelligent sensors are proposed for stress monitoring [24]. Alert Based continuous monitoring of Parkinson patients by intelligent wearable devices is described by [53]. CodeBlue has been proposed as a wireless infrastructure integrating sensors and PDAs for emergency situations such as mass casualty events [36], and LiveNet system has been proposed for proactive healthcare applications [51]. In the recent past research related to improving and managing decision making for enhanced patient care has been undertaken [2,6,11–13,19,25,32,58,59].

Despite the advancement made in the enabling technologies supporting patient monitoring, the existing communication channel between the patient and the healthcare professional remains as a vulnerable link. Signal transmission for patient monitoring solutions has predominantly taken place via cable modem (restricting patient mobility), infrastructure based network such as WLANs, Cellular PCS/GSM, and Satellite based Networks. Some of these networks may lead to spotty and un-predictable coverage due to time and location dependent channel quality and signal attenuation resulting in permanent/ temporary dead spots [57]. Mobile ad hoc network has the potential of complementing the network coverage of infrastructure based network when the coverage from the latter is low/non-existent. Although, some research has been done to meet the objective of immediacy and mobility and address the challenges with a reliable communication scheme and un-cooperative routers in the context of patient monitoring via a multi-hop MANET, the issue is yet to be fully resolved [57–60]. This research is an attempt to explore the opportunities and challenges associated with leveraging mobile ad hoc network and the ubiquity of patient monitoring devices to support power ef<sup>fi</sup>cient, reliable communication at minimal delays in the context of comprehensive patient monitoring.

## 2.2. Leveraging mobile ad hoc networks (MANETs) for comprehensive monitoring

A mobile ad hoc network consists of geographically distributed wireless devices or nodes that can dynamically form a network without a pre-de<sup>fi</sup>ned infrastructure. The nodes act as routers as well as transmitters and communicate with one another over a wireless medium [22,42,44].

Although promising, there are numerous unique challenges associated with wide scale deployment of MANETs for patient monitoring including support for reliability, energy conservation of the battery powered monitoring devices, routing mechanisms, network topology control in a dynamic environment, mobility pattern of the nodes, security, range and signal reception, throughput and bit rates, number of patients that can be supported, and interference [22,42,44,48]. Due to power and size requirements of patients' devices, the range of the transmitted signal is likely to be small. Further, the range is likely to be affected by the frequency of operation, the nature of spectrum used (licensed vs. un-licensed), mobility of nodes, and obstacles. The signal strength can be weakened by 30–90% as it passes through doors, walls, and windows. Additionally, the availability of wireless links varies over space and time due to power loss to a signal. The range is also likely to affect the probability of <sup>fi</sup>nding another cooperative device for further routing. The throughput, or actual number of bits that can be transmitted after subtracting overhead and retransmission, decreases as the distance between nodes increases. Since MANETs operate in a dynamic environment where every link is wireless and every node is mobile, the resulting topological changes affect the consistency of transmission. The number of patients that can be supported via MANETs depends on the bit rate, frequency of monitoring, and the amount of data to be transmitted per patient. The following sections focus on the challenges/opportunities in terms of reliability, delays, and battery power management in the context of e-e signal transmission via MANET.

2.2.1. End to end reliability in signal transmission via mobile ad hoc networks

Reliability in the context of a MANET can be addressed from multiple perspectives. Prior work done in the area of reliability includes broadcast schemes [9], routing protocols [28,67], trade-off between reliability and energy ef<sup>fi</sup>ciency [68], and increasing reliability by using a receiver-initiated hop by hop acknowledgement scheme [34]. Broadcast based routing schemes can greatly enhance the reliability of messages delivery to one or more healthcare professionals; however it results in considerable network traf<sup>fi</sup>c from sending messages to all possible destinations. Similarly, reliability of transmission to the next hop can be increased by multiple retransmissions with hop-byhop acknowledgements (ACK) but it can result in message implosion, high levels of network traf<sup>fi</sup>c, and sub-optimal power usage [34]. The use of multiple ad hoc networks is likely to increase the reliability of message delivery; however the total traf<sup>fi</sup>c on all networks could be signi<sup>fi</sup>cant. Increased power transmission will also lead to increased reliability since it increases the transmission range. However, it can adversely impact the connectivity of the network due to the death of the transmitting node.

A primary requirement in the context of patient monitoring is the probability of locating a cooperative router at each hop in end to end (e–e) signal transmission. Probability of locating a cooperative router is directly dependent on transmitted power and the density of patient monitoring devices (PMDs) in the area of transmission. Thus the performance metric for e–e reliability in this study is the probability of locating a cooperative device at each consecutive hop in e–e routing of the transmitted message [9,59]. From that perspective, reliability in e–e signal transmission is a function of variations in: (a) device density in the area of transmission, (b) transmitted power at each hop in e–e signal transmission, (c) patient/device mobility impacting distribution — uniform/clustered, (d) variations with respect to the clusters in terms of size, number, and (e) the clusters being on/off the route of transmissions. Enhancing reliability con<sup>fl</sup>icts with ef<sup>fi</sup>cient power usage in e–e signal transmission. Based on the application speci<sup>fi</sup>c requirements either reliability or power conservation may be sacri<sup>fi</sup>ced [68].

2.2.2. End to end delays in signal transmission via mobile ad hoc networks

Diverse patient monitoring scenarios dictate variability in the degree of tolerance with respect to e–e delays in signal transmission, such as low delays for emergency and relatively higher delays for routine transmissions. The parameters impacting e–e delays include: (a) service rate of the PMDs, (b) system utilization, and (c) number of e–e hops. Service rate or processing capacity of the PMDs has an inverse relationship with e–e delays in signal transmission. System utilization and number of e–e hops have a direct relationship with e–e delays. The challenge in minimizing e–e delay lies in balancing between minimal hops transmissions and minimal power transmissions.

2.2.3. End to end power consumption in signal transmission via mobile ad hoc networks

In the current context, battery power of the PMDs is critical to supporting comprehensive patient monitoring solutions and thereby forms one of the key performance measures for diverse monitoring scenarios. The level of transmitted power determines the device range and the number of hops from the source to the recipient. The range across which a signal can be coherently received is crucial in determining performance in terms of e–e reliability, e–e delay, and e–e power consumption [38]. Halving the transmission range increases the number of hops by two but decreases the area of the reserved <sup>fl</sup>oor to one fourth, thus allowing for more concurrent transmissions to take place in the same neighborhood [38]. Transmitting at a lower power level conserves battery power and reduces device range but it adversely impacts network connectivity. Network partitioning due to nodes falling out of the transmission range leads to low reliability in e–e transmission. Transmitting at higher power level increases device range and increases the probability of locating one/ more node(s) for further transmission. However, it adversely impacts power usage. Excessive power usage causes death of the nodes, network partitioning, and decrease in e–e reliability. Thus optimal power usage is essential to increasing a device's battery life thereby maintaining the connectivity of the network, increasing time before the network partitions, enhancing e–e reliability of transmission, reducing interference, and increasing throughput. An ideal solution will optimize power usage and spatial reuse while ensuring reliability of e–e transmission [54].

Recently, power control in mobile ad hoc networks has been the focus of extensive research [7,16,38–41,43,47,49,54,55]. A discussion of the tradeoffs involved in selecting the power level is presented by [38]. Network layer routing solutions with focus on energy consumption with throughput being a secondary factor is presented by [49,16]. These approaches reduce energy consumption at the expense of decrease in network throughput and increase in delay. Power control schemes that consider the MAC (Medium Access Control) perspective include research focusing on power control algorithms for network topology control [47], interference aware power control schemes that use broadcasted interference information to bound the power levels of subsequent transmission [63]. Other protocols based on cluster heads acting as base stations [29] and a combination of clustering and power control protocol are also presented [27]. Power control with the focus on minimizing power usage in the presence of a radio model includes: algorithm for minimum energy paths [47], minimizing maximum power level of a node to ensure ‘k’ disjoint paths between any 2 nodes [45]. Heuristic based power minimizing approaches in the absence of a radio model includes: LINT (Local Information No Topology Protocol, no connectivity guarantees) and LILT (Requires Information from Routing Layer), COMPOW (uniformly distributed nodes, network Layer), and CLUSTERPOW (non-uniformly distributed nodes).

## 2.3. Research contribution

The research published in the literature has not fully modeled and evaluated context speci<sup>fi</sup>c mechanics and effects of variable-rate support in transmitted power level [38]. Since context speci<sup>fi</sup>c applications have different requirements, their service requirement and the functions of the associated key parameters can vary signi<sup>fi</sup>cantly [46]. Hence it is critical to conduct context speci<sup>fi</sup>c research assessing the applicability of multi-hop MANET and the performance of the associated key parameters [46,55]. Some research exploring the viability of emergency message transmissions in the context of patient monitoring via multi-hop MANET include assessment of routing schemes and un-cooperative routers. The results found that the routing scheme that best mitigates the presence of un-cooperative routers while providing high reliability and low delays includes broadcast and multicast routing schemes [59,60]. The current research adds to the extant research by addressing the challenge of concurrently meeting the con<sup>fl</sup>icting requirements of ef<sup>fi</sup>ciently utilizing limited battery power of the monitoring devices while maximizing communication reliability and minimizing transmission delay within the context of patient monitoring via multi-hop MANET. The results of the current research not only provide support to the usefulness of the proposed power management protocols in achieving 100% communication reliability at while minimizing power usage and delays but also holds the potential to enable reliable patient monitoring without any dependency on time and location. The speci<sup>fi</sup>c contributions of the current research are presented in Table 1:

## 3. PRD protocols and PM-PRD framework

The section describes the key elements of our proposed approach: (1) Power–Reliability–Delay (PRD) Protocols and (2) the PM-PRD framework. Fig. 2 models the dependency relationship among the variables of interest that impact patient monitoring via a multi-hop MANET. The proposed model is utilized in developing the PRD protocols and the PM-PRD framework.

## Table 1

## Research contributions of the current research.

![](/api/attachments/MQYVFAD9/fulltext/images/a9e55022a939de0b21f06211553a8ea49bc259b0beb615efc07f1e1daeaba7ad.jpg)  
Fig. 2. Dependency model among variables impacting patient monitoring via MANET.

## 3.1. Power–reliability–delay (PRD) protocols

The proposed Power–Reliability–Delay (PRD) Protocols seek to manage the battery power of the PMDs in the case when a multihop MANET is leveraged for signal transmission. Fig. 3 depicts the variability in transmit power by the source (node A) and the intermediate PMDs (nodes B, C, E) in each of the protocol as the signal gets transmitted from the source to the destination (node D). The details of the proposed PRD protocols are as follows:

## 3.1.1. Random from patient and random from cooperative devices (RP-RCD)

This protocol entails the source PMDs and the intermediate routing PMDs to transmit signal at a random power level till the signal reaches the destination (Fig. 3a). The advantage of RP-RCD lies in low processing requirements and can potentially be utilized for non-critical transmissions by PMDs with low processing capability in areas of high density. The biggest disadvantage lies in potential inef<sup>fi</sup>ciency in power usage and unpredictable reliability, power usage, and delay due to variations in transmitted power level at each hop and the number of hops involved in e–e signal transmission.

3.1.2. Maximum from patient and maximum from cooperative devices (MP-MCD)

This protocol entails the source PMDs and the intermediate routing PMDs to transmit signal at the maximum available power level till the signal reaches the destination (Fig. 3b). The advantage of MP-MCD lies in low processing requirements and can be utilized for critical transmissions with the promise of high reliability and lowest delay even in areas of low density. It is less sensitive to node mobility due to increased transmission range but the biggest disadvantage lies in high power utilization especially in areas of high density which may lead to network partitions due to nodes running out of battery power quicker.

![](/api/attachments/MQYVFAD9/fulltext/images/b74527f26fee89f7d308539b987865e9c060712427f8a3b87162450c0ee5041c.jpg)  
Fig. 3. Variability in transmission power via PRD protocols.

3.1.3. Maximum from patient and optimum from cooperative devices (MP-OCD)

This protocol entails the source PMDs and the intermediate routing PMDs to transmit signal at the maximum and optimum power level respectively till the signal reaches the destination (Fig. 3c). The “Optimum Power Level” is de<sup>fi</sup>ned as the minimum transmit power at which a signal can reach the nearest node. It can be derived by listening to the neighboring transmissions. The advantage of MP-OCD lies in ef-<sup>fi</sup>cient power usage by the intermediate PMDs and high reliability at reasonable delays in e–e signal transmission. It is applicable for routine/emergency transmissions in areas of high density. The disadvantage lies in potential inef<sup>fi</sup>ciency in power usage by source PMD in areas of high density and unnecessary processing/delays by the intermediate PMDs in low device density.

## 3.1.4. Optimum from patient and optimum from cooperative devices (OP-OCD)

This protocol entails the source PMDs and the intermediate routing PMDs to transmit signal at the optimum power level till the signal reaches the destination (Fig. 3d). The advantage of OP-OCD lies in most ef<sup>fi</sup>cient power usage by the PMDs while ensuring high reliability at reasonable delays in e–e signal transmission. It is mostly applicable for transmissions in areas of high density. In low density areas, the optimal transmit power level may end up being the same as maximum power level thereby nullifying the utility of optimal transmissions. The disadvantage lies in potentially longer delays, higher processing requirements by all PMDs involved in signal routing, and unnecessary delays in low device density.

## 3.2. Patient monitoring — Power Reliability Delay (PM-PRD) framework

In order to effectively leverage the proposed approach, its critical to assess and map the requirements of given monitoring scenarios to one/more PRD protocols such that communication reliability is enhanced at minimal power usage and communication delays. The proposed PM-PRD framework captures the decision logic that maps the proposed PRD protocol to the requirements/constraints of the diverse monitoring scenarios. Table 2 presents the relationship between the elements representing diverse monitoring scenarios and the proposed PRD protocols. The parameterization of the elements impacting diverse monitoring scenarios and the respective priorities assigned to communication reliability, power usage, and delays dictates the choice of the PRD protocol that is utilized for communication from the source node (patient's device) to the destination node (healthcare professional's device) via a MANET.

The proposed PM-PRD Framework models the decision logic of mapping one/more PRD protocols to the speci<sup>fi</sup>cations of a given monitoring scenario (Fig. 4). The algorithm associated with the processes underlying the PM-PRD Framework is given in Appendix A.

## 4. Analytical modeling

Healthcare is a complex domain with stringent regulations making comprehensive evaluation of a novel approach in the real environment an extremely challenging task. It is rather complicated to obtain access to a typical facility (such as a hospital or a nursing home), implement the proposed approach in an actual patient monitoring device that mirrors end to end signal transmission via a multi-hop MANET, and allow substantial number of patients to transmit signals under diverse patient monitoring scenarios. Moreover, the security/privacy concerns with transmitting protected health information and the low level of tolerance for service disruption in the healthcare domain adds to the dif<sup>fi</sup>culties in conducting a <sup>fi</sup>eld study to obtain and evaluate real measures in the context of patient monitoring via a multi-hop MANET.

Since a <sup>fi</sup>eld study is beyond the scope of the current study, we utilize analytical modeling technique as a viable approach to conducting a preliminary evaluation of our proposed novel approach [18]. The objective of the evaluation is to establish the usefulness of our approach in enhancing communication reliability at minimal power usage and delays for signal transmission via a multi-hop MANET under diverse monitoring scenarios. The following analytical model, developed for the current study, is grounded in prior research in the context of utilizing mobile ad hoc network for remote patient monitoring. Table 3 presents the symbols used in the analytical model.

Relationship between the elements of diverse monitoring scenarios and PRD protocols

<table><tr><td rowspan="2">Diverse monitoring scenarios represented by variations in the following factors: transmission type, overall density, and availability of battery power</td><td colspan="3">Priority specifications of power, reliability, and delays for diverse monitoring scenarios</td><td rowspan="2">PRD protocols with the best fit to the scenario</td></tr><tr><td>Efficiency in power usage</td><td>Transmission reliability</td><td>Low delays</td></tr><tr><td>Transmission: EmergencyOverall density: HighBatter power: High</td><td>Lowest priority</td><td>Highest priority</td><td>Highest priority</td><td>MP-OCD</td></tr><tr><td>Transmission: Emergency overallDensity: HighBatter power: Low</td><td>Low priority</td><td>Highest priority</td><td>Highest priority</td><td>OP-OCD</td></tr><tr><td>Transmission: EmergencyOverall density: LowBattery power: High</td><td>Lowest priority</td><td>Highest priority</td><td>Highest priority</td><td>MP-MCD</td></tr><tr><td>Transmission: EmergencyOverall density: LowBattery power: Low</td><td>Low priority</td><td>Highest priority</td><td>Highest priority</td><td>OP-OCD</td></tr><tr><td>Transmission: Non-EmergencyOverall density: HighBattery power: High</td><td>Lowest priority</td><td>High priority</td><td>High priority</td><td>OP-OCD</td></tr><tr><td>Transmission: Non-emergencyOverall density: HighBattery power: Low</td><td>Lowest priority</td><td>High priority</td><td>High priority</td><td>OP-OCD or RP-RCD</td></tr><tr><td>Transmission: Non-emergencyOverall density: LowBattery power: High</td><td>Lowest priority</td><td>High priority</td><td>high priority</td><td>OP-OCD</td></tr><tr><td>Transmission: Non-emergencyOverall density: LowBattery power: Low</td><td>Lowest priority</td><td>High priority</td><td>High priority</td><td>OP-OCD or RP-RCD</td></tr></table>

![](/api/attachments/MQYVFAD9/fulltext/images/800795d690b913d47549bf0c28b8d23ba954c19bae2764d3e91ea14e6e97a65c.jpg)  
Fig. 4. PM-PRD framework: decision model for leveraging PRD protocol in diverse scenarios.

4.1. Transmitted power and communication reliability in uniform distribution

The range of the transmitted signal is the circular area with radius equal to $\mathrm { H } _ { \mathrm { { s z i j } } } ,$ , across which a signal can be coherently received by the intermediary monitoring device(s). Power consumed in transmitting

## Table 3

Symbols used in the analytical model

<table><tr><td>A</td><td>Area of transmission</td></tr><tr><td>a</td><td>Propagation constant which theoretically can take value = 2, 3, 4</td></tr><tr><td> $A_{ij}$ </td><td>Area over which the transmitted message is coherently heard in the ith hop for j number of hops with hop size =  $H_{sjiz}$ </td></tr><tr><td> $D_{un}$ </td><td>Device density considering uniform distribution of devices in the area A</td></tr><tr><td> $D_{cl}^{k}$ </td><td>Device density considering clustered distribution of devices in the area A, where the number of clusters is denoted by k</td></tr><tr><td> $D_{cl}$ </td><td>Device density in the cluster</td></tr><tr><td> $H_{scl}$ </td><td>The hop size within a cluster</td></tr><tr><td> $H_{szij}$ </td><td>Hop size of the transmissions for the ith hop where number of hops is j</td></tr><tr><td>L</td><td>The number of devices forming a cluster</td></tr><tr><td> $N_{hps}$ </td><td>Number of hops</td></tr><tr><td> $N_{cl}$ </td><td>Number of clusters</td></tr><tr><td> $N_{hcl}$ </td><td>Number of hops within a cluster on the route of transmission</td></tr><tr><td> $N_{dclk1}$ </td><td>Number of devices/users in the cluster  $k_{1}$ </td></tr><tr><td> $N_{dclk2}$ </td><td>Number of devices/users in the cluster  $k_{2}$ </td></tr><tr><td> $N_{d}$ </td><td>Total number of monitoring devices/users in A</td></tr><tr><td> $P_{bij}$ </td><td>Probability of locating a device for transmission in the ith hop for j number of hops</td></tr><tr><td> $P_{ij}$ </td><td>Power transmitted/consumed in the ith hop where number of hops is j</td></tr><tr><td> $P_{be2ej}$ </td><td>Probability of successfully locating devices for complete e–e transmission where number of hops is j</td></tr><tr><td> $P_{bij}^{CL}$ </td><td>Probability of locating a device for transmission in the ith hop for j number of hops, in the presence of cluster (s)</td></tr><tr><td> $P_{hcl}$ </td><td>Power transmitted in each hop within a cluster</td></tr><tr><td> $P_{bhcl}$ </td><td>Probability of locating a cooperative PMD in each hop within cluster</td></tr><tr><td> $P_{be2ecl}^{CL}$ </td><td>e–e probability of locating a cooperative PMD in each hop within cluster</td></tr><tr><td> $P_{be2ej}^{CL}$ </td><td>Probability of successfully locating devices for complete e–e transmission where number of hops is j, in the presence of cluster(s)</td></tr><tr><td> $R_{e2ej}$ </td><td>Reliability of e–e transmission for j number of hops</td></tr><tr><td> $R_{hij}$ </td><td>Reliability in the ith hop where number of hops is j</td></tr><tr><td>RP_min</td><td>Minimum power required for correct reception at a given level of receiver noise</td></tr><tr><td> $T_{d}$ </td><td>Total distance over which transmission of messages takes place in patient monitoring</td></tr></table>

a signal over $\mathrm { H } _ { \mathrm { { s } z i j } }$ is a function of device range and can be expressed as:

$$
\begin{array}{r l} \mathrm {P_ {ij}} & = \mathrm {RP\_ {m} inx} \left(\mathrm{Const.} \times \mathrm{H} _ {\mathrm{szij}} ^ {\alpha}\right) \\ & \text { where   Const.   is   a   constant   for   propagation } \end{array}\tag{1}
$$

If $\mathrm { P _ { t } }$ is the power transmitted and $\mathrm { P _ { n } }$ is the minimum power required to reach the nearest node with 100% reliability then optimal power level for transmission is expressed as the state where:

$$
\lambda = P _ {t} - P _ {n} \text {   such   that   } \lambda -- > 0.
$$

The number of e–e hops in signal transmission over a given e–e distance $( \mathrm { i . e . \ : T _ { d } ) }$ is modeled as:

$$
\mathrm{N} _ {\text { hps }} = \mathrm{T} _ {\mathrm{d}} / \mathrm{H} _ {\text { szij }} \text { where } \mathrm{N} _ {\text { hps }} \leq \mathrm{j} \text { and } 1 \leq \mathrm{i} \leq \mathrm{j}.\tag{2}
$$

Thus $\mathrm { P _ { e 2 e j } }$ or e–e power transmitted for a given $\mathrm { N _ { h p s } = j }$ over a given $\mathrm { T _ { d } }$ is expressed as

$$
P _ {e 2 e j} = \sum_ {N _ {h p s} = i} ^ {N _ {h p s} = j} P _ {i j} = \sum_ {N _ {h p s} = i} ^ {N _ {h p s} = j} \left(R P _ {-} \min \times \left(\text { Const. } \times H _ {s z i j} ^ {\alpha}\right)\right).\tag{3}
$$

Reliability in e–e signal transmission is modeled in terms of probability of locating another device within the transmission range of the source device [9,59]. Hence reliability can be expressed as a function of variations in: (a) device density in the area of transmission, and (b) device range of the source node which is impacted by transmitted power at each hop in e–e signal transmission. Thus reliability of transmission at each hop can be expressed as follows:

$$
\mathrm{P} _ {\text { bij }} = \mathrm{A} _ {\text { ij }} \times \mathrm{D} _ {\text { un }} = \left(\pi \times \left(\left(\mathrm{P} _ {\text { ij }} / (\mathrm{RP} _ {-} \min \times \text { Const. })\right) ^ {1 / \alpha}\right) ^ {2}\right) \times \mathrm{N} _ {\mathrm{d}} / \mathrm{A}.\tag{4}
$$

The reliability of e–e transmission via a multi-hop ad hoc network where $\mathrm { N _ { h p s } = j }$ can be approximated as:

$$
P _ {b e 2 e j} = \prod_ {N _ {h p s} = 1} ^ {N _ {h p s} = j} \left(\left(\pi \times \left(\left(P _ {i j} / (R P \_ m i n \times C o n s t.)\right) ^ {1 / \alpha}\right) ^ {2}\right) \times N _ {d} / A\right).\tag{5}
$$

4.2. Transmitted power and communication reliability non-uniform distribution

Mobility of patients within a given area could lead to non-uniform distribution such as clustering. The impact of clustering is modeled by varying the size/number of clusters (1 or 2 clusters each with 30% or 40% of $\Nu _ { \mathrm { d } } )$ and the cluster(s) being on and off the route in the area of transmission. For $\mathrm { N _ { c l } } = 1 , \mathrm { i f } \mathrm { N ^ { k 1 } } _ { \mathrm { d c l } }$ is the number of devices in a cluster where k1 stands for $\Nu _ { \mathrm { c l } } = 1$ then:

$$
\mathrm{L} = \mathrm{N} _ {\mathrm{dcl}} ^ {\mathrm{k1}} = 0. 3 \times \mathrm{N} _ {\mathrm{d}} \text {or} 0. 4 \times N _ {d}\tag{6}
$$

For $\mathrm { N _ { c l } } { = } 2 , \mathrm { i f } \mathrm { N ^ { k } } 2 _ { \mathrm { d c l } }$ is the number of devices in a cluster where k2 stands for $\Nu _ { \mathrm { c l } } = 2$ , then the value of L where 2 clusters have 30% of $\Nu _ { \mathrm { d } }$ or 40% of $\Nu _ { \mathrm { d } }$ each can be given as:

$$
\mathrm{L} = \mathrm{N} _ {\mathrm{dcl1}} ^ {\mathrm{k2}} = \mathrm{N} _ {\mathrm{dcl2}} ^ {\mathrm{k2}} = 0. 3 \times \mathrm{N} _ {\mathrm{d}} \text { or } 0. 4 \times \mathrm{N} _ {\mathrm{d}}.\tag{7}
$$

Hence device density in the clusters, where L is the number of devices forming a cluster, is:

$$
\mathrm{D} _ {\mathrm{clk}} = \mathrm{L} / \left(\pi \times \left(\mathrm{H} _ {\text { szij }} / 2\right) ^ {2}\right)\tag{8}
$$

If there is a cluster present in the route of transmission, then the transmission within the cluster can take place via minimal power emission. However, the problem with that is a longer route with considerable delays. In order to minimize delays in alert transmission $\mathrm { { N } } _ { \mathrm { { h c l } } }$ puts a ceiling on the number of hops in a cluster irrespective of the number of devices forming the cluster. Thus $\mathrm { H } _ { \mathrm { s c l } }$ is expressed as:

$$
\begin{array}{r l} \mathrm {H_ {scl}} & = \mathrm {H_ {szij} / N_ {hcl}} \text {   where   } 1 \leq \mathrm {N_ {hcl}} \leq 4 \text {   such   that   } \mathrm {N_ {hcl}} \\ & = \text { Minimum   (L,   4) } \end{array}\tag{9}
$$

e–e power transmitted in the cluster is expressed as:

$$
\mathrm{P} _ {\mathrm{e2ecl}} = \sum_ {1} ^ {\mathrm{N} _ {\mathrm{hcl}}} \left(\mathrm{RP} _ {-} \min \times \left(\text { Const. } \times \mathrm{H} _ {\mathrm{scl}} ^ {\alpha}\right)\right).\tag{10}
$$

Reliability in e–e signal transmission is modeled in terms of probability of locating another device within the transmission range of the source device. Since patient/device mobility impacts distribution in the area of transmission leading to clustered distribution, hence, variations with respect to the clusters in terms of size, number, and the clusters being on/off the route of transmissions impact the probability of successfully locating the next node for transmission. Thus, e–e probability of successful transmission within the cluster where $\Nu _ { \mathrm { c l } } = 1$ or $\Nu _ { \mathrm { c l } } = 2$ is given by:

$$
\mathrm{P} _ {\text { be2ecl }} = \prod_ {1} ^ {\mathrm{N} _ {\mathrm{hcl}}} \mathrm{P} _ {\text { bcl }}\tag{11}
$$

where

$$
\mathrm{P} _ {\mathrm{bcl}} = \mathrm{H} _ {\mathrm{scl}} ^ {2} \times \left(\mathrm{L} / \left(\mathrm{H} _ {\text { szij }} / 2\right) ^ {2}\right).
$$

There is a negative impact on overall device density due to devices lost in cluster(s) which would have otherwise been uniformly distributed in the transmission area. Hence overall density due to clustering is:

$$
\mathrm{D} _ {\mathrm{cl}} = \left(\mathrm{N} _ {\mathrm{d}} + \mathrm{N} _ {\mathrm{cl}} - (\mathrm{L} \times \mathrm{N} _ {\mathrm{cl}})\right) / \mathrm{A}\tag{12}
$$

The probability of locating a device for transmission in the ith hop for j hops, in the presence of cluster (s) is approximated as:

$$
\mathrm{P} _ {\text { bij }} ^ {\mathrm{CL}} = \pi \times \mathrm{H} _ {\text { szij }} ^ {2} \times \mathrm{D} _ {\mathrm{cl}}\tag{13}
$$

Thus the probability of locating devices for successful e–e transmission considering j number of hops, and $N _ { c l } = \mathrm { k }$ where cluster(s) in the route of transmission is given by:

$$
P _ {\text { be2ej }} ^ {C L} = \prod_ {i = 1} ^ {j - k} P _ {\text { bij }} ^ {C L} \times \prod_ {k = 1} ^ {k} P _ {\text { be2ecl }} ^ {k}.\tag{14}
$$

It follows that probability of locating devices for successful e–e transmission considering j number of hops, and $N _ { c l } = 1$ where cluster(s) are not in the route of transmission is given by:

$$
\mathrm{P} _ {\text { be2ej }} ^ {\mathrm{CL}} = \prod_ {\mathrm{i} = 1} ^ {\mathrm{j}} \mathrm{P} _ {\text { bij }} ^ {\mathrm{CL}}.\tag{15}
$$

## 4.3. Transmission delays in the area of transmission

e–e delay is calculated using M/M/1 queue. Total time in each hop (i.e. ith hop in j number of hops) is expressed as:

$$
\mathrm{Ti} = \mathrm{Tq} + \mathrm{Ts} = ((\mathrm{r} / \mu) / (1 - \mathrm{r}) + (1 / \mu))\tag{16}
$$

and e–e delay is expressed as:

$$
D _ {e 2 e} ^ {j} = \sum_ {N _ {h p s} = 1} ^ {N _ {h p s} = j} (1 / \mu) / (1 - r)\tag{17}
$$

## 4.4. Results of performance evaluation

For the purpose of evaluation of our approach in signal transmission via a multi-hop MANET we assume the PMDs in the area of transmission to be (a) cooperative routers, i.e., the PMDs are willing and able to transmit signal till the signal reaches the destination, and (b) symmetrical in terms of processing capacity and battery power. The transmission from the source to destination is assumed to take place in a prede<sup>fi</sup>ned area such as a nursing home, parameterized as a 10×10 square area. Hence the representative route across the hypotenuse has an end to end transmission distance of 14.14 units, the range of the number of end to end hops between 2 and 10 corresponding to the range of transmitted signal varying between 1.414 and 7.07. RP\_min×Const. and α are parameterized as 1, and 2 respectively [57,59,62]. Performance of e–e delay is assessed for varying hops at varying levels of system utilization where service rate (μ) of the PMDs is 100 packets per second (i.e. a PMD takes 0.01 s to process a packet), and system utilization (r) is varied over 0 to 0.9 [59,60]. The range parameters associated with overall density was approximated based on published accounts of number of beds in a typical nursing home. For instance: publically owned nursing home facilities has an average of 61 beds and on an average almost 60% facilities have less than 50 beds [20]. Hence we approximated the range of beds in our model as 5–50 leading to the overall density to range from 0.5 to 0.05 in a 10×10 area. The results establish the usefulness of our proposed approach in enhancing communication reliability at minimal power usage and delays for diverse monitoring scenarios.

![](/api/attachments/MQYVFAD9/fulltext/images/6ec992971a300a85208f2c01e0e7a715b58e5090c0ca0af42f74df67b6e193d1.jpg)  
Fig. 5. e–e power usage over a range of e–e hops.

The evaluation is conducted by comparing the measures of reliability, power usage, and delays in end to end transmission via a multi-hop MANET over a varying range of overall device density (considering both uniform and clustered distribution), transmitted power levels, and system utilization with/without the utilization of the proposed approach.

4.4.1. Results of evaluation without utilizing the proposed approach in e–e signal transmission

The objective of evaluation in this section is to show the impact of diverse monitoring scenarios manifested in terms of variations in overall device density, device range, end to end hops, and system utilization on reliability, power usage, and delays when signal transmission via a MANET takes place without utilizing the proposed approach. The results validate that (a) e–e reliability, power usage, and delays are signi<sup>fi</sup>cantly impacted by variations in monitoring scenarios, and (b) communication reliability is not always 100% in diverse monitoring scenarios when the proposed approach is not utilized in e–e signal transmission from the source to destination via a multi-hop MANET. The subsequent sections discuss the signi<sup>fi</sup>- cant research results.

4.4.1.1. Case A: Varying power, density, and system utilization in uniform device distribution (C=0). This section presents the impact of varying transmitted power, overall device density, and system utilization in the area of transmission considering the case of uniform device distribution. Variations in transmit power is represented by variations in number of end to end hops over a given transmission distance between the source and destination. The results conclusively validate the inverse relationship of power conservation with reliability and e–e delays. As the hops increase, power consumption decreases at the cost of increase in e–e delays (over varying levels of system utilization) and decrease in e–e reliability at low levels of device density (Fig. 5–7). The result validates that multi-hop transmission optimizes battery power. The reduction in power usage by transmitting signals via $N _ { h p s }$ can potentially be by a factor of $N _ { h p s } ^ { \alpha - 1 }$ instead of transmitting via a single hop over a given distance. e–e reliability increases non-linearly as the e–e power transmitted increases for a given level of device density (Fig. 6). Achieving 100% reliability in e–e signal transmission at decreased device density requires increased utilization of battery power. The e–e delays have a low gradient in increase when the system utilization is less than 50% beyond which the increase is exponential (Fig. 7). At low levels of utilization, transmit power can be minimized, however at high system utilization minimizing e–e delays leads to maximizing power usage.

![](/api/attachments/MQYVFAD9/fulltext/images/ef4114eb3d308879f31d298fff0d8b48617bf2f2a8ff6b7be197b1c77e38d3e0.jpg)  
Fig. 6. e–e reliability over a range of density & e–e hops.

![](/api/attachments/MQYVFAD9/fulltext/images/4d6a59652a3a10d339d1a88d922e32029e762b856b647722b43798b47e6db481.jpg)  
Fig. 7. e–e delays over a range of system utilization and e–e hops.

4.4.1.2. Case B: Varying power, density, in clustered distribution (C=1/2, 30/40% of PMD, on/off route). This section presents the impact of varying (a) transmitted power, and (b) overall device density in the area of transmission considering the case of non-uniform/clustered device distribution. Since e–e power usage and e–e delays are not functions of variations in overall device density, hence only the performance analysis of e–e reliability is presented. In the case of 1/2 cluster(s) with 30%/40% PMDs forming the cluster, the overall device density in the area of transmission decreases. The decrease in $D _ { c l }$ reduces the reliability of e–e transmission over the entire range of variations in transmitted power as the size of cluster increases. The e–e reliability when the size of cluster=40% of PMDs is lower than the e–e reliability when the size of cluster=30% of PMDs for a given level of e–e transmitted power (Figs. 8 and 9). Additionally, the results show that the decrease in e–e reliability for a given level of transmitted power is more pronounced when the clusters are off the route of e–e transmission (Figs. 9, 11, 13, and 15). As the number of clusters increases, further reducing the device density in the area of transmission, the e–e reliability is signi<sup>fi</sup>cantly reduced at the given range of transmitted power (Figs. 12 and 14). The results also hold the inverse relationship between e–e reliability and transmitted power.

![](/api/attachments/MQYVFAD9/fulltext/images/e67b5ad63db9ccbabaeae942e6b2f385190ab65db199615988a1c458d9cd8f56.jpg)  
Fig. 8. e–e reliability over a range of density and e–e hops, for 1 cluster with 30% of PMDs, on transmit route.

![](/api/attachments/MQYVFAD9/fulltext/images/738048b5cb3a3c549c6bace78298dd09442761607582bb864cf2b8df8fad7247.jpg)  
Fig. 9. e–e reliability over a range of density and e–e hops, for 1 cluster with 30% of PMDs, off transmit route.

4.4.2. Results of evaluation with utilizing the proposed approach in e–e signal transmission

The results in this section validate the utility of the proposed approach in enhancing communication reliability while minimizing power usage and delays when signal transmission takes place via a multi-hop MANET for diverse monitoring scenarios. Diverse monitoring scenarios are manifested by varying overall device density, device range, end to end hops, and system utilization. In contrast signal transmissions without utilizing the proposed approach failed to maximize communication reliability under similar conditions (refer to Figs. 5–15). The results point out that the protocols MP-MCD, OP-OCD, MP-OCD all achieve 100% communication reliability under diverse monitoring scenarios. The choice of the utilization of the protocols is associated with difference in power usage (maximum for MP-MCD, average for MP-OCD, and minimum for OP-OCD) and delays (minimum for MP-MCD, average for MP-OCD, and maximum for OP-OCD) under diverse scenarios. Once the overall device density in the area of transmission reaches 0.2, the power usage and delays associated with each protocol becomes constant. Before 0.2, the power usage and delays have a slight curve. Hence if the device density in the area of transmission is below 0.2 and battery power is suf<sup>fi</sup>ciently high, it is advisable to utilize highest power transmit protocol (MP-MCD) at lowest delay for high level alerts and to utilize moderately lower power transmit protocol (OP-OCD or MP-OCD) at moderate delay for low level alerts. If the device density in the area of transmission is higher than 0.2 and battery power is suf<sup>fi</sup>ciently high, it is advisable to be conservative in battery power usage by utilizing the OP-OCD at the highest delay if the transmission is for a low level alert otherwise utilize the MP-MCD or MP-OCD for a high level alert transmission.

![](/api/attachments/MQYVFAD9/fulltext/images/3ce07ecd4270219a578c853ef0c2a2d73f9f8aa195e7432962b8b46fcff9aa8b.jpg)  
Fig. 10. e–e reliability over a range of density and e–e hops, for 1 cluster with 40% of PMDs, on transmit route.

![](/api/attachments/MQYVFAD9/fulltext/images/cd390f97efdc4378ec41d540bf2bcdf4e5f99b1993f9f74e8facde3abc39d8b4.jpg)  
Fig. 11. e–e reliability over a range of density and e–e hops, for 1 cluster with 40% of PMDs, off transmit route.

4.4.2.1. Case C: Varying Power, density, and system utilization for uniform device distribution (C=0). This section presents the impact of utilizing the PRD protocols over a varying range of overall device density and system utilization in the area of transmission for uniform device distribution. The proposed PRD protocols manifest varying levels of transmit power by the source and intermediate routing devices. The results conclusively validate that by utilizing the proposed approach in e–e signal transmission from the source to destination via a multi-hop MANET, communication reliability is enhanced at minimal power usage and delays for diverse monitoring scenarios (Fig. 16–21).

All protocols maximize reliability under diverse monitoring scenarios, except RP-RCD. The performance of RP-RCD is erratic and unpredictable in terms of e–e power, e–e reliability, and e–e delays in transmission for diverse scenarios (Fig. 16). Power utilized by RP-RCD and MP-MCD is not impacted by device density in the area of transmission due to the protocols' behavior of transmitting at random and maximum power, respectively (Fig. 16). Moreover, e–e power transmitted by protocols OP-OCD and MP-OCD has an inverse relationship with overall device density due to higher level of power transmitted to maximize reliability at lower levels of device density in the area of transmission (Fig. 16). The performance of e–e delays with respect to the PRD protocols at varying levels of system utilization shows that MP-MCD affords lowest delays for varying levels of system utilization while OP-OCD has the highest delays in e–e signal transmission (due to longer route involving more hops than other protocols). The e–e delays increases non-linearly as system utilization increases for OP-OCD, MP-MCD, and MP-OCD protocols. For instance if transmission takes place by OP-OCD, at 15% of system utilization e–e delay is 0.12 whereas at 90% system utilization e–e delay increases to 1.00. e–e delays have a positive relationship with overall device density for variable levels of system utilization (Fig. 18–21). OP-OCD followed by MP-MCD are the most power ef<sup>fi</sup>cient and the least delay ef<sup>fi</sup>cient protocol for diverse monitoring scenarios over a varying range of device density and system utilization (Figs. 16, 19–21). Hence MP-MCD is potentially the best suited for emergency transmission with high delay constraints while OP-OCD is best suited for routine transmissions with lower delay constraints. These assessments and allocations are consistent with the PM-PRD framework.

![](/api/attachments/MQYVFAD9/fulltext/images/47c2a14ef81276c2f9d40c7d5653b325146f1aba70ac3dd64ddc0a659979fb94.jpg)  
Fig. 12. e–e reliability over a range of density and e–e hops for 2 clusters with 30% of PMDs, on transmit route.

![](/api/attachments/MQYVFAD9/fulltext/images/08144d66059f89b290c025b4ba8ed2dc1ca3611586aaf1c18267eaa5390299c6.jpg)  
Fig. 13. e–e reliability over a range of density and e–e hops for 2 clusters with 30% of PMDs, off transmit route.

4.4.2.2. Case D: Varying power, density, and system utilization for clustered device distribution (C=0). This section presents the impact of utilizing the PRD protocols over a varying range of overall device density and system utilization in the area of transmission for clustered device distribution. Variation in cluster is represented in terms of 1 or 2 clusters on/off the route of transmission with 30 to 40% of PMDs in the cluster. Clustering negatively impacts overall device density in the area of transmission The proposed PRD protocols manifest varying levels of transmit power by the source and intermediate routing devices. The results validate that by utilizing the proposed approach in signal transmission from the source to destination via a multi-hop MANET, communication reliability is enhanced at minimal power usage and delays for diverse monitoring scenarios even in the case of clustering (Figs. 22–27). In contrast signal transmissions without utilizing the proposed approach failed to maximize e–e reliability under similar conditions.

All of the power management protocols still maximize communication reliability in diverse scenarios, except RP-RCD whose behavior remains unpredictable. OP-OCD is still the best in terms of power consumption and the worst in terms of delays for varying levels of system utilization followed by MP-OCD (Figs. 22, 25–27). The power consumed by the protocols RPRCD and MP-MCD in e–e signal transmission is independent of the device density and hence is not impacted by clustering (Fig. 22). Since OP-OCD and MP-OCD have an inverse relationship with overall device density, hence clustering leads to a slight increase in e–e power transmitted in order to maximize reliability at lower levels of device density. However, MP-MCD is still the best suited for emergency transmission while OP-OCD is best suited for routine transmissions. A critical observation in the case of clustering is that although it has an adverse impact on device density and power consumption it has a positive impact on delays for variable levels of system utilization. As the number/size of clusters increases the overall density in the area of transmission decreases thereby leading to increased power transmitted in order to maximize reliability resulting in a decrease in e–e hops and delays. Similar results were obtained for two clusters.

![](/api/attachments/MQYVFAD9/fulltext/images/1bb7d0eea40af25daad7e084b2443c2b8da985d4339429772e31ac095db5f709.jpg)  
Fig. 14. e–e reliability over a range of density and e–e hops for 2 clusters with 40% of PMDs, on transmit route.

![](/api/attachments/MQYVFAD9/fulltext/images/48ccb98423b2e27bcea516faf2512ce08a903bfd5599a129339e61f040d1e547.jpg)  
Fig. 15. e–e reliability over a range of density and e–e hops for 2 clusters with 40% of PMDs, off transmit route.

The analysis of the results lends support to the research premise that mobile ad hoc network formed among patient monitoring devices can potentially be utilized to enhance network coverage in areas where the coverage from the infrastructure based network is spotty and/or non-existent, thereby improving the quality of remote patient monitoring. Table 4 summarizes and compares the results of evaluation with/without utilizing the proposed approach for end to end transmission via a MANET. A key inference drawn from the comparison is not only the validation of the utility of the proposed approach in maximizing communication reliability while minimizing power usage and delays in diverse scenarios but also the proof that the same does not hold true when the proposed approach is not utilized for signal transmission via a multi-hop MANET in similar conditions.

![](/api/attachments/MQYVFAD9/fulltext/images/4003e7be3ddbb65e29116ea04ba9823e3f7e8b90774c7da22530e2b079d850b3.jpg)  
Fig. 16. e–e power usage for uniform distribution (C=0).

![](/api/attachments/MQYVFAD9/fulltext/images/c3107306619a74da3a0d804c09cef122eb7589cc4b8a11ebc91139fd388e44a1.jpg)  
Fig. 17. e–e reliability for uniform distribution (C=0)

![](/api/attachments/MQYVFAD9/fulltext/images/a1bcee8e8f7a1ad66fcc57d1baa45944d321a50f76d4afe1a93263e890a6a2e1.jpg)  
Fig. 18. e–e hops for uniform distribution, C=0.

## 5. Conclusion and future research

The underlying premise of the current research is that reliable communication between a patient and a healthcare professional is a critical requirement of comprehensive patient monitoring solutions especially for the instances involving emergency transmissions. However, the lingering concern with the unpredictable spotty network coverage of infrastructure based networks in the context of technology enabled patient monitoring is yet to be fully resolved, thereby negatively impacting the potential of remote patient monitoring applications. Mobile ad hoc network has the potential of complementing the network coverage of infrastructure based network when the coverage from latter is low/non-existent. Although promising there are several challenges associated with leveraging mobile ad hoc network in the context of patient monitoring.

![](/api/attachments/MQYVFAD9/fulltext/images/7c43c1d2f7fd6bbee41882a75d97e6d6eddce10d9dd340c61219424206275204.jpg)  
Fig. 19. e–e delays for uniform distribution (C=0) system utilization=15%.

![](/api/attachments/MQYVFAD9/fulltext/images/106e189db0b3663afb3cff468e680ccebccd3e2b82bc5ece473aac3e7906c180.jpg)  
Fig. 20. e–e delays in transmission for uniform device distribution (C=0) at System utilization=45%

Some of the past research have addressed the challenges associated with management of routing schemes and un-cooperative routers for emergency message transmission via multi-hop MANET [58–60]. The results suggest that the routing schemes that are better suited to achieve high reliability and low delays are broadcast and multicast, especially in the presence of un-cooperative routers [59,60]. The current research adds to the extant research by investigating the challenge of optimizing power usage of the low-powered monitoring devices while achieving 100% communication reliability at minimal delays in the context of leveraging mobile ad hoc network for patient monitoring in areas where the coverage from infrastructure based networks is spotty and/or non-existent. The speci<sup>fi</sup>c contributions of the current research to the existing body of research are: (a) concurrently addressing the con<sup>fl</sup>icting requirements associated with power management of the low-powered patient monitoring devices while enhancing communication reliability and minimizing transmission delays, (b) modeling the relationship among the parameters impacting patient monitoring via mobile ad hoc network based on in-depth review of prior research in the domain of patient monitoring and mobile ad hoc network, (c) developing protocols utilizing variable rate transmit power for managing the low-power of the patient monitoring devices such that communication reliability is maximized, (d) developing a framework that models the complex decision logic of assessing speci<sup>fi</sup>c parameter values for diverse patient monitoring scenarios and mapping one/ more power management protocols that best <sup>fi</sup>t the context speci<sup>fi</sup>c requirements, (e) developing an extensible analytical model for evaluation of the usefulness of the proposed approach. The results conclusively validate the utility of the proposed power management protocols in achieving 100% communication reliability while minimizing power usage and delays in diverse patient monitoring scenarios.

![](/api/attachments/MQYVFAD9/fulltext/images/70c756e9e8b4a9715072674baeabaecc3249393810c7064b14e30c5220538fbc.jpg)  
Fig. 21. e–e delays in transmission for uniform device distribution (C=0) at System utilization = 90%

![](/api/attachments/MQYVFAD9/fulltext/images/f41afeeb98021eac4883382a2a18a1b2915395c8f9a77df8f4282b82476a47fe.jpg)  
Fig. 22. e–e power usage for 1 cluster with 30% of PMDs.

The proposed protocols, framework, and the analytical model offer a validated foundation that can be built upon by future investigators studying the rich problem space of patient monitoring via MANET. An interesting extension will be to combine the current research with the previous research assessing different routing schemes, i.e., to apply the proposed power management protocols in different routing schemes such as: multicast, broadcast etc. to assess which combination of routing scheme and power management protocol is the most promising for maximizing reliability at minimal power consumption and delays. Additional research can also extend the analytical model and further test the robustness of the proposed approach by including other key parameters such as: security/privacy of transmitted data, scalability of the current approach, dynamic route changes in transmission via pure MANET and/or hybrid network architecture (MANET+ infrastructure based networks). Since the resources required for a <sup>fi</sup>eld evaluation of the proposed approach has been a limiting factor in the current research, future research can implement the proposed approach in a real setting such as a nursing home facility and use precise measurements of context speci<sup>fi</sup>c parameters to strengthen and further validate the research results.

Since the underlying assumption of the current research is that a patient needs to communicate an alert from an area with low/no coverage from infrastructure based networks, hence we focused on achieving 100% communication reliability via a multi-hop MANET by employing the proposed power management protocols for diverse monitoring scenarios such that power usage is optimized while maxi mizing communication reliability at minimal delays. Future research can extend the current research by investigating techniques that can address disease/context speci<sup>fi</sup>c requirements pertaining to delay tolerance, error tolerance, and transmissions/re-transmissions when the network coverage is low or non-existent. Research investigating methods for effective management of local data storage in combination with transmitted data is also warranted in future research since it can potentially lead to a reduction in network traf<sup>fi</sup>c and ef<sup>fi</sup>cient management of healthcare resources [61]. Additionally, since healthcare is a highly regulated environment with stringent requirements associated with security, privacy, con<sup>fi</sup>dentiality, and access of protected health data hence future research exploring the impact of utilizing MANET for data transmission will not only be highly desirable but may also have a profound impact on the adoption and utilization of MANET based approach by the patient population.

![](/api/attachments/MQYVFAD9/fulltext/images/9c3e6b094ed04467f3513376bcd35d0d62440409b98b34887336e380814820aa.jpg)  
Fig. 23. e–e reliability for 1 cluster with 30% of PMDs.

![](/api/attachments/MQYVFAD9/fulltext/images/0e2cdd4df05d694839c21f3c8ac3861859c5cd26a6e61ccabd69403a0ca0db4b.jpg)  
Fig. 24. e–e hops for 1 cluster with 30% of PMDs.

Another interesting aspect of future research will be an assessment of the impact of 4G on the existing issues pertaining to the context of reliable transmission with respect to patient monitoring. The emerging 4G wireless networks [1,4] will in general support wireless health monitoring. More speci<sup>fi</sup>cally, the current 4G networks offer higher bandwidth [4] which can help bandwidth-intensive health monitoring applications. It is not clear if 4G networks will improve the wireless coverage, which was the motivating factor for this study. Also, 4G networks may improve the interconnection or interfacing among multiple wireless networks [1], thus supporting ad hoc networks to easily interface with other wireless networks. This can lead to multiple implementations of hybrid network con<sup>fi</sup>gurations involving infrastructure-based and ad hoc networks. Thus, many of the ideas presented in this paper can still be implemented in such networks for health monitoring. Another area of future study would be an inspection of how the proposed protocols perform in a ZigBee environment in terms of data rate, battery life, and communication reliability.

![](/api/attachments/MQYVFAD9/fulltext/images/e4c00c3b045df1f9961ba5de39a0ab2ee2e3b4b37b0d76ee1f252efa030e5972.jpg)  
Fig. 25. Delays for 1 cluster, 30% of PMDs, 15% utilization.

![](/api/attachments/MQYVFAD9/fulltext/images/b7494ba91e83f76381b37473b61b40bdec24e30c72003466821781f271c27f11.jpg)  
Fig. 26. e–e delays in the case of 1 cluster with 30% of PMDs at 45% system utilization

The current research has the potential to signi<sup>fi</sup>cantly impact the practice and management of remote patient monitoring. By implementing the proposed protocols and the decision logic in the patient monitoring devices, patients can be pervasively monitored for timely detection of anomalies and prompt medical intervention without any dependency on location and time. The results show that 100% communication reliability can be achieved by utilizing the proposed power management protocols, MP-MCD, OP-OCD, MP-OCD, under diverse monitoring scenarios. The choice of utilizing a particular protocol for a given monitoring scenario is associated with the requirements/constraints with respect to power consumption (maximum for MP-MCD, average for MP-OCD and minimum for OP-OCD) and delays (minimum for MP-MCD, average for MP-OCD and maximum for OP-OCD). For instance: the proposed approach can potentially be utilized in a nursing home with relatively high density of patients by utilizing the most power ef<sup>fi</sup>cient protocol, i.e. OP-OCD, while outside the nursing home transmissions can utilize the least power ef<sup>fi</sup>cient protocol, i.e. MP-MCD, in order to compensate

![](/api/attachments/MQYVFAD9/fulltext/images/f554aeec855e24d595c774f69e2595ed746f39f0f102221c7b2c606142f249bd.jpg)  
Fig. 27. e–e delays in the case of 1 cluster with 30% of PMDs at 90% system utilization.

Key results with/without utilizing the proposed approach in transmission via MANET.

for the potential variability in density in the environment outside the nursing home. Since the most power ef<sup>fi</sup>cient protocol leads to higher delays and vice-versa, hence situations requiring low delay tolerance may utilize MP-MCD for transmission while situations that can withstand higher delay may conserve the limited power supply by utilizing OP-OCD for transmitting at a lower power. Moreover, since mobile ad hoc network can be formed among the patient monitoring devices proactively on demand without any infrastructure, hence the implementation may not add to the existing cost of wireless network in existing nursing home facilities that are strapped for <sup>fi</sup>nancial resources. Although, an exact cost bene<sup>fi</sup>t analysis of utilizing the proposed approach versus adding further infrastructure based network support is outside the scope of the current research, future research can address this limitation by investigating these options.

## Acknowledgment

The work was supported, in part, by a National Science Foundation (NSF) research grant (SCI#0439737).

## Table 4

3 OP-OCD is the most ef<sup>fi</sup>cient power management protocol followed by MP-OCD. MP-MCD is the least power ef<sup>fi</sup>cient protocol. Power transmitted by OP-OCD and MP-OCD has an inverse relationship with overall device density while MP-MCD and RP-RCD are not impacted by device density. As the device density increases, the transmit power required to reach the nearest node decreases and as the density decreases, higher transmit power is required to reach the nearest node

4 While OP-OCD minimizes power usage it maximizes delays and while MP-MCD maximizes power usage it minimizes delays over a varying range of device density and system utilization. Hence MP-MCD is best suited for emergency transmission while OP-OCD for non-critical transmissions with higher delay tolerance.

5 The e–e delays increases non-linearly as system utilization increases for OP-OCD, MP-MCD, and MP-OCD protocols. For instance if transmission takes place by OP-OCD, at 15% of system utilization e–e delay is 0.12 whereas at 90% system utilization, e–e delay increases to 1.00, i.e., almost a 90% increase in delays as the system utilization increases from 15% to 90%. Hence, at higher levels of system utilization, it is best to utilize MP–MCD in order to minimize delays at the cost of higher power utilization.

6 Clustering leads to a slight increase in e–e power transmitted in order to maximize reliability over diverse monitoring scenarios. A critical observation in case of clustering is that although it has an adverse impact on device density and power consumption it has a positive impact on delays for variable levels of system utilization, i.e., end to end delay in case of clustered distribution is slightly lower due to increased power transmissions to make-up for decreased device density.

```txt
Algorithm for Process1-Task 3: Assess the Applicability of Sleep Strategy: Analyze Battery Power
ANALYZE BATTERY POWER LEVEL (BPL) OF THE PMD
If BPL >= Threshold Battery Power (TBP) then BPL = High Else BPL = Low
```

## Appendix A. Formal expressions/algorithm of the PM-PRD scheme

```txt
Algorithm for Process1-Task 1: Analyze Patient's Vital Signs
OBTAIN VITAL SIGNS (AT PRESPECIFIED INTERVALS)
ANALYZE CURRENT READINGS AGAINST PRIOR STORED READINGS
If the current readings > Threshold Readings OR If the current readings < Threshold Readings
Alert Detected = True Alert Transmitted = False
CATEGORIZE ALERTS
If Anomalous Reading is > X points above Threshold Reading
ALERT = EMERGENCY Else ALERT = ROUTINE
```

```txt
Algorithm Process1-Task 2: Analyze Patient's Environment
ANALYZE OVERALL DEVICE DENSITY (ODD) AND PRESENCE OF CLUSTERS
If Overall Device Density (ODD) in Transmission area >= Threshold Device Density (TDD)
ODD = High Else ODD = Low
ANALYZE BATTERY POWER LEVEL (BPL) OF THE PMD
If BPL >= Threshold Battery Power (TBP)
BPL = High Else BPL = Low
```

```txt
Algorithm for Process 3-Task 7: Transmissions based on PM-PRD Scheme
IF AN ANOMALY IS DETECTED AND TRANSMISSION IS WARRANTED
    If Alert Transmitted = False AND If Alert = Emergency
    ANALYZE OVERALL DEVICE DENSITY (ODD) AND PRESENCE OF CLUSTERS
    If Overall Device Density (ODD) in Transmission area >= Threshold Device Density (TDD)
    If there are No Clusters Detected in Transmission area //Uniform Distribution//
    ANALYZE BATTERY POWER LEVEL (BPL) OF THE PMD
    If BPL >= Threshold Battery Power (TBP)
    INVOKE PRD PROTOCOL MP-OCD
    Else INVOKE PRD PROTOCOL RP-RCD
    Else // Clustered Distribution// INVOKE PRD PROTOCOL MP-MCD
    Alert Transmitted = True
    If Alert Transmitted = False AND If Alert = Routine
    ANALYZE OVERALL DEVICE DENSITY (ODD) AND PRESENCE OF CLUSTERS
    If Overall Device Density (ODD) in Transmission area >= Threshold Device Density (TDD)
    If there are No Clusters Detected in Transmission area //Uniform Distribution//
```

```txt
ANALYZE BATTERY POWER LEVEL (BPL) OF THE PMD
If BPL >= Threshold Battery Power (TBP)
INVOKE PRD PROTOCOL OP-OCD
Else INVOKE PRD PROTOCOL RP-RCD
Else // Clustered Distribution // INVOKE PRD PROTOCOL MP-OCD
Alert Transmitted = True
```

```txt
Algorithm Process 3: Task 6: Assess the Applicability of Sleep Strategy

INVOKE SLEEP STRATEGY IF NO ANOMALIES DETECTED
ANALYZE OVERALL DEVICE DENSITY (ODD) AND PRESENCE OF CLUSTERS
If Overall Device Density (ODD) in Transmission area >= Threshold Device Density (TDD)
If there are No Clusters Detected in Transmission area //Uniform Distribution//
PMD transitions to Sleep Mode for the duration of the “Idle State”
Else If the PMD is in a Cluster //Clustered Distribution-PMD in the Cluster//
PMD transitions to Sleep Mode during the “Idle State”
Else PMD Listens/Routes Transmitted Signal //PMD not in the Cluster//
Since Sleep Strategy Requirements are Violated//
```

```txt
Algorithm Invoking the PRD Protocols

INVOKE PRD PROTOCOL MP-MCD
Transmit Signal = MP-MCD
PMD Transmit Signal = Maximum Power Level of the PMD
IMD (Intermediate Monitoring Device) Transmit Signal = Maximum Power Level
If BPL of IMD <= TBP for supporting Maximum Power Level
Transmission at the particular node=RP-RCD //Random Power Level from the Available Power//
INVOKE PRD PROTOCOL MP-OCD
Transmit Signal = MP-OCD
PMD Transmit Signal = Maximum Power Level of the PMD
IMD (Intermediate Monitoring Device) Transmit Signal = Optimal Power Level
Optimal Power Level = Minimal Power Level to Transmit a Signal to the Next Node
//Derived Based on Listening to Prior Transmissions –Largely Dependent on Device Density//
If BPL of IMD <= TBP for supporting Optimal Power Level
Transmission at the particular node=RP-RCD //Random Power Level from the Available Power//
INVOKE PRD PROTOCOL OP-OCD
Transmit Signal = OP-OCD
PMD Transmit Signal = Optimal Power Level of the PMD
IMD (Intermediate Monitoring Device) Transmit Signal = Optimal Power Level
Optimal Power Level = Minimal Power Level to Transmit a Signal to the Next Node
//Derived Based on Listening to Prior Transmissions –Largely Dependent on Device Density//
If BPL of IMD <= TBP for supporting Optimal Power Level
Transmission at the particular node=RP-RCD //Random Power Level from the Available Power//
INVOKE PRD PROTOCOL RP-RCD
Transmit Signal = OP-OCD
Random Power Level = A random power level from the available power level of the PMD
PMD Transmit Signal = Random Power Level
IMD (Intermediate Monitoring Device) Transmit Signal = Random Power Level
```

## References

[1] P. Ahluwalia, U. Varshney, Composite quality of service and decision making perspectives in wireless networks, Decision Support Systems 46 (2) (2009) 542–551.

[2] C. Bielza, J. Fernández del Pozo, P.J.F. Lucas, Explaining clinical decisions by extracting regularity patterns, Decision Support Systems 44 (2) (2008).

[3] J. Bohn, F. Gärtner, H. Vogt, Dependability issues of pervasive computing in a healthcare environment, Security in Pervasive Computing 2802 (2004) 160–169.

[4] I. Bose, Fourth generation wireless systems: requirements and challenges for the next frontier, Communications of the AIS (May 2006)

[5] C. Boult, et al., Innovative healthcare for chronically ill older persons: results of a national survey, The American Journal of Managed Care (September 1999).

[6] S. Brahnam, C.F. Chuang, R.S. Sexton, F.Y. Shih, Machine assessment of neonatal facial expressions of acute pain, Decision Support Systems 43 (4) (2007).

[7] C. Chao, J. Sheu, I. Chou, An adaptive quorum-based energy conserving protocol for IEEE 802.11 ad hoc networks, IEEE Transactions in Mobile Computing, vol. 5, no. 5, May 2006, pp. 560–570.

[8] M. Chiasson, et al., Strangers in a strange land: can IS meet the challenges and opportunities of research in healthcare, Proc. of the Tenth Americas Conference in Information Systems (AMCIS), 2004.

[9] S.Y. Cho, J.H. Sin, B.I. Mun, Reliable broadcast scheme initiated by receiver in ad hoc networks, Proc. of the 28th Annual IEEE International Conference on Local Computer Networks. Noy 2003.

[10] Chronic Care Improvement, ITAA E-Health white paper: a product of the E-health committee, May 2004.

[11] J.M. Corchado, J. Bajo, Y.D. Paz, D.I. Tapia, Intelligent environment for monitoring Alzheimer patients, agent technology for health care, Decision Support Systems (2008) 44.

[12] J.M. Corchadoa, J. Bajo, Y. Paza, D.I. Tapiaa, Intelligent environment for monitoring Alzheimer patients, agent technology for health care, Decision Support Systems 44 (2008).

[13] R.W. Day, M.D. Dean, R. Gar<sup>fi</sup>nkel, S. Thompson, Improving patient <sup>fl</sup>ow in a hospital through dynamic allocation of cardiac diagnostic testing time slots, Decision Support Systems 49 (2010).

[14] I.A. Gieras, The proliferation of patient-worn wireless telemetry technologies within the U.S. healthcare environment, Proc. of 4th International IEEE EMBS Special Topic Conference on Information Technology Applications in Biomedicine, 2003, pp. 295–298.

[15] S. Goldberg, N. Wickramasinghe, 21st century healthcare — the wireless panacea, Proc. of the 36th Hawaii International Conference on System Sciences, 2003.

[16] J. Gomez, et al., PARO: supporting dynamic power control routing in wireless ad hoc networks, ACM/Kluwer Journal of Wireless Networks 9 (5) (2003)

[17] F. Gouaux, et al., Smart devices for the early detection and interpretation of cardiological syndromes, Proc. 4th Annual IEEE Conf. On Information Technology Applications in Biomedicine, UK, 2003.

[18] A. Gupta, R. Sharda, Improving the science of healthcare delivery and informatics using modeling approaches, Decision Support Systems (2012).

[19] P.J.H. Hu, C.P. Wei, T.H. Cheng, J.X. Chen, Predicting adequacy of vancomycin regimens: a learning-based classi<sup>fi</sup>cation approach to improving clinical decision making, Decision Support Systems 43 (4) (2007).

[20] Information Report No. 185 on Nursing Home, American Society of Planning Of<sup>fi</sup>- cials. April 1964.

[21] R. Istepanian, A. Petrosian, Optimal zonal wavelet-based ECG data compression for a mobile telecardiology system, IEEE Transactions on Information Technology in Biomedicine 4 (3) (Sept 2000) 200–211.

[22] S. Jain, Energy Aware Communication in Ad-hoc Networks, Technical Report UW-CSE, University of Washington, Seattle, March 2003.

[23] E. Jovanov, A. O'Donnel, A. Morgan, B. Priddy, R. Hormigo, Prolonged telemetric monitoring of heart rate variability using wireless intelligent sensors and a mobile gateway, Proc. of the Second Joint IEEE EMBS/BMES Conference, 2002, pp. 1875–1876.

[24] E. Jovanov, et al., Stress monitoring using a distributed wireless intelligent sensor system, IEEE Engineering in Medicine and Biology Magazine 22 (3) (May-June 2003) 49–55.

[25] I. Junglas, C. Abraham, B. Ives, Mobile technology at the frontlines of patient care: understanding <sup>fi</sup>t and human drives in utilization decisions and performance, Decision Support Systems 46 (2009).

[26] E. Kafeza, D. Chiu, S. Cheung, M. Kafeza, Alerts in mobile healthcare applications: requirements and pilot study, IEEE Transactions on Information Technologies in Biomedicine 8 (3) (2004) 173–181.

[27] V. Kawadia, P.R. Kumar, Power control and clustering in ad hoc networks, Proc. of IEEE INFOCOM Conference, 2003.

[28] J.M. Kim, Y.I. Eom, An adaptive routing protocol for supporting reliable communication in wireless ad-hoc network environments, Proc. IEEE Paci<sup>fi</sup>c Rim Int. Symp on Depend. Computing, 2001.

[29] T.J. Kwon, M. Gerla, Clustering with power control, Proc. of IEEE MILCOM Conference, 1999.

[30] J.C. Kyu, H.H. Asada, Wireless, battery-less stethoscope for wearable health monitoring, Proc. the IEEE 28th Annual Northeast Bioengineering Conference, Philadelphia, PA, 2002, pp. 187–188.

[31] LifeSync, www.wirelessecg.com2005.

[32] L. Lin, P.J.-H. Hu, O.R.L. Sheng, A decision support system for lower back pain diagnosis: uncertainty management and clinical evaluations, Decision Support Systems 42 (2) (2006).

[33] Y. Liu, J.A. Clark, S. Stepney, “Devices are people too” using process patterns to elicit security requirements in novel domains: a ubiquitous healthcare example, Security in Pervasive Computing 3450 (2005) 31–45.

[34] W. Lou, J. Wu, A reliable broadcast algorithm with selected acknowledgements in mobile ad hoc networks, Proc. of IEEE Conference on Global Communications (Globecom), August 2003.

[35] A. Lymberis, Smart wearables for remote health monitoring, from prevention to rehabilitation: current R&D, future challenges, Proc. of 4th International IEEE EMBS Special Topic Conference on Information Technology Applications in Biomedicine, 2003, pp. 272–275.

[36] D. Malan, T.R.F. Fulford-Jones, M. Welsh, S. Moulton, CodeBlue: an ad hoc sensor network infrastructure for emergency medical care, Proc of the MobiSys 2004 Workshop on Applications of Mobile Embedded Systems (WAMES 2004), 2004, pp. 12–14.

[37] G.G. Mendoza, B.Q. Tran, G.G. Mendoza, B.Q. Tran, In-homewireless monitoring of physiological data for heart failure patients. 2002

[38] A. Muqattash, M.M. Krunz, A distributed transmission power control protocol for mobile ad hoc networks, IEEE Transactions on Mobile Computing (2004).

[39] A. Muqattash, M. Krunz, A distributed transmission power control protocol for mobile ad hoc networks, IEEE Transactions in Mobile Computing 3 (10) (April 2004) 113–128.

[40] S. Naqvi, L. Patnaik, A distributed channel access protocol for ad hoc networks with feedback power control, IEEE Transactions in Mobile Computing 5 (10) (October 2006) 1448–1459.

[41] S. Panichpapiboon, G. Ferrari, O. Tonguz, Optimal transmit power in wireless sensor networks, IEEE Transactions in Mobile Computing 5 (10) (October 2006) 1432–1447.

[42] L. Qin, T. Kunz, Survey on mobile ad hoc network routing protocols and cross-layer design, Carleton University Systems and Computer Engineering, Technical Report SCE-04-14, August 2004.

[43] B. Radunovic, J. Le Boudec, Rate performance objectives of multihop wireless networks, IEEE Transactions in Mobile Computing 3 (4) (October 2004) 334–349.

[44] R. Rajaraman, Topology control and routing in ad hoc networks: a survey, ACM SIGACT News 33 (2002) 2.

[45] R. Ramanathan, On the performance of ad hoc networks with beamforming antennas, Proc. of IEEE/ACM International Symposium on Mobile Ad Hoc Networking and Computing (MobiHoc), October 2001, pp. 95–105.

[46] Reddy, et al., A review of QOS research in MANETs, IEEE Transactions in Mobile Computing (2006).

[47] V. Rodoplu, T. Meng, Minimum energy mobile wireless networks, IEEE Journal on Selected Areas in Communications 17 (8) (August 1999).

[48] S. Sesay, Z. Yang, J. He, A survey on mobile ad hoc wireless networks, Information Technology Journal 3 (2004) 2.

[49] S. Singh, M. Woo, C.S. Raghavendra, Power aware routing in mobile ad hoc networks Proc, of ACM MobiCom Conference, 1998

[50] S. Sneha, U. Varshney, Enabling ubiquitous patient monitoring: model, decision protocols, opportunities and challenges, Decision Support Systems 46 (3) (2009) 606–619.

[51] M. Sung, A. Pentland, MIThril LiveNet: health and lifestyle networking, Proc. Workshop on Applications of Mobile Embedded Systems (WAMES'04) Mobisys'04, Boston, MA, June 2004.

[52] T. Suzuki, M. Doi, LifeMinder: an evidence-based wearable healthcare assistant, Proceedings of the ACM CHI Conference, 2001.

[53] A. Tablado, A. Illarramendi, J. Bermudez, A. Goni, Intelligent monitoring of elderly people, Proc. 4th Annual IEEE Conf. On Information Technology Applications in Biomedicine, UK, 2003.

[54] N.H. Vaidya, Open problems in mobile ad hoc networking, Keynote talk presented at the Workshop on Local Area Networks, November 14 2001, (Tampa, Florida).

[55] N.H. Vaidya, Tutorial on mobile ad hoc networks: routing, MAC and transport issues, A tutorial at Infocom, 2006.

[56] U. Varshney, Pervasive healthcare, Computer 36 (12) (2003) 138–140

[57] U. Varshney, Using wireless networks for enhanced monitoring of patients, Proc. of Americas Conference on Information Systems (AMCIS), 2004.

[58] U. Varshney, Managing comprehensive wireless patient monitoring, Pervasive Health Conference and Workshops, Nov.–Dec. 2006, 2006, pp. 1–4.

[59] U. Varshney, A framework for supporting emergency messages in wireless patient monitoring, Decision Support Systems 45 (2008) 981–996.

[60] U. Varshney, Addressing un-cooperation of routers in wireless patient monitoring, Proceedings of the 19th IEEE Symposium on Computer-Based Medical Systems, 2006.

[61] U. Varshney, Enhancing wireless patient monitoring by integrating stored and live patient information, Proceedings of the 19th IEEE Symposium on Computer-Based Medical Systems, 2006.

[62] U. Varshney, S. Sneha, Wireless patient monitoring: reliability and power management, Proc. 2nd International Conference on Broadband Networks 2 (2005).

[63] R. Wattenhofer, et al., Distributed topology control for power ef<sup>fi</sup>cient operation in multi-hop wireless ad hoc networks, Proc. of IEEE INFOCOM Conference, 2001.

[64] Website of Welch Allyn, http://www.monitoring.welchallyn.com/products/ wireless.

[65] Website for Cardionet, http://cardionet.com/.

[66] Website of Philips, http://www.medical.philips.com/main/news/content/<sup>fi</sup>le\_630. html.

[67] J. Wu, W. Lou, Forward-node-set-based broadcast in clustered mobile ad hoc networks, Wireless Communications and Mobile Computing (2003).

[68] J. Zhu, S. Papavassiliou, On the connectivity modeling and the tradeoffs between reliability and energy ef<sup>fi</sup>ciency in large scale wireless sensor networks, Proc. IEEE Wireless Communications and Networking Conference, March 2003.

Dr. Sweta Sneha is an Assistant Professor of Information Systems at Kennesaw State University. She received her doctorate in Computer Information Systems from Georgia State University. Her research interests center around a wide array of technical and behavioral challenges pertaining to “E-Health/M-Health.” She has conducted and published multiple researches in (a) wireless network and enhanced decision support systems for innovative e-health/m-health services, (b) adoption, usage, and integration of emerging e-health/m-health services in the practice and delivery of healthcare by the healthcare professionals, and (c) organizational impact and process change associated with the integration and usage of e-health/m-health services by the healthcare sector. Her research has been published premier journals and conferences including IEEE Communications, Decision Support Systems, Decision Sciences, International Journal of Medical Informatics, Communications of the Association of Information Systems, International Journal of Electronic Healthcare, Hawaii International Conference on System Sciences, Americas Conference on Information Systems, and IEEE Broadmed. She has also authored a book titled Revolutionizing Health Monitoring. In addition, she has been actively involved in the organization of many national/international conferences, Americas Conference in Information Systems (AMCIS — as a minitrack co-chair), Pervasive Health Conference, and Clinical Research in Georgia Conference. She has also been invited speaker at the M-Health Summit.

Upkar Varshney is currently an Associate Professor of Computer Information Systems at Georgia State University, Atlanta. His current interests include pervasive healthcare, mobile commerce, ubiquitous computing, and wireless networks. He has authored over 130 papers including 60 in national and international journals. He is credited with several “<sup>fi</sup>rst” papers in streams of mobile commerce and pervasive healthcare. According to Scholar-Google, his papers are among the highly cited and have been cited more than 2000 times. He was the founding co-chair (with Prof. Imrich Chlamtac) of International Pervasive Health Conference (http://www.pervasivehealth.org/previous/index.html) in 2006 and the steering committee co-chair for 2008 conference (http://www. pervasivehealth.org). Upkar was also the program co-chair for Americas Conference on Information Systems (AMCIS-2009).

Upkar has presented over <sup>fi</sup>fty tutorials, workshops, and a few keynotes at major wireless, computing, and information systems conferences. He has also received grants totaling \$500K from several funding agencies including the National Science Foundation. His teaching awards include Myron T. Greene Outstanding Teaching Award (2004), RCB College Distinguished Teaching Award (2002), and Myron T. Greene Outstanding Teaching Award (2000). He has served or is serving as an editor/guest editor for several major journals including IEEE Transactions on IT in Biomedicine, ACM/Springer Mobile Networks (MONET), Decision Support Systems (DSS), IEEE Computer, Communications of the AIS (CAIS), Int. J. on Network Management (IJNM), Int. Journal on Mobile Communications (IJMC) among others.
