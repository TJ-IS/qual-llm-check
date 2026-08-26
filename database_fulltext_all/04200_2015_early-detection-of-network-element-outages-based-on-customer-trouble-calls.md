---
otero_id: 4200
otero_key: "JFRV7EC5"
title: "Early detection of network element outages based on customer trouble calls"
authors: "Željko Deljac; Mirko Randić; Gordan Krčelić"
year: "2015"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2015.02.014"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Early detection of network element outages based on customer trouble calls

Željko Deljac <sup>a,</sup>⁎, Mirko Randić <sup>b</sup>, Gordan Krčelić <sup>a</sup>

<sup>a</sup> T-Hrvatski Telekom (T-HT), Technical Functions, Savska 32, Zagreb, Croatia

<sup>b</sup> Faculty of Electrical Engineering and Computing, University of Zagreb, Croatia

## a r t i c l e i n f o

Article history: Received 13 February 2014 Received in revised form 14 January 2015 Accepted 22 February 2015 Available online 3 March 2015

Keywords: Fault management Broadband network Early fault detection Alarm system Fault detection delay

## a b s t r a c t

This paper deals with the issue of early detection of network element outages. Timeliness of outage detection as well as accuracy in <sup>fi</sup>nding outages on equipment in a telecommunication network depend on the monitoring system used and its performance. The intent of this paper is to investigate and propose a complementary solution to improve the performance of the existing systems in detecting faults earlier than it was able to do before. In developing our approach two constraints are given. The existing operational environment cannot be changed; threshold tuning and parameter changing cannot be done; furthermore no additional infrastructure investment has been planned. Hence, our approach relies on an alternative method based on a two-stage hybrid statistical and diagnostic detector which we designed in a way that exploits additional available data and avoids alarm monitoring system imperfections. The role of this detector is twofold: early detection of network element outages based on customer trouble calls and rule-based decision making for faulty-element isolation based on knowledge derived from fault and network management data. In this paper we present results of statistical analysis of trouble-reporting data. The analysis showed that the timing of customers' trouble reports and their content have information potential that can be utilized for early detection of outages The detector is explained in detail and its accuracy and reduction delay is evaluated. The method presented can reduce the outage detection delay time by 2.33 h on average observed in relation to the performance of an existing fault management process which was designed to detect outages solely on the basis of an alarm monitoring system, for the “dif<sup>fi</sup>culties in work” type of malfunction. We attained an overall probability of correct detection of 95.3%. Out of the total number of outages that hypothetically could be detected, by using this method we were able to detect 77.5% of cases 1 h before the alarm was raised in the existing alarm system, while 23% of cases were detected 4 h before the actual alarm. The approach has been tested on real telecommunication network data over the period of one year.

© 2015 Elsevier B.V. All rights reserved.

## 1. Introduction

Broadband networks contain a multitude of hardware and software components in different locations that can be subject to fault. A typical broadband network (Fig. 1) consists of three main parts. The IP/MPLS core part (1) is based on Multiprotocol Label Switching (MPLS) technology. In addition, there are head-end servers that provide services to users such as: Internet access, access to video services, Internet Protocol TeleVision (IPTV), Video On Demand (VOD) and Voice Over Internet Protocol (VOIP) telephone services. In the access part of the network (2), Digital Subscriber Line Access Multiplexer (DSLAM) architecture is used to link customer traf<sup>fi</sup>c over an ADSL port to the Ethernet aggregation. The physical link between the subscriber and the DSLAM port is a twisted copper pair in subscriber cable — the most common kind of access. The end point of the access part is a Distribution point behind which the customer installation begins. The third part (3) includes network termination equipment (ADSL modem, Splitter), other CPEs (IPTV STB, TV, handset and other devices) and in-house customer installations. This part of the network is spatially most extensive.

From the perspective of broadband network management, faults can be categorized as those that affect services offered only to one particular customer and those that affect a whole group of customers. For example, a network element outage mostly degrades or disables services offered to a larger number of customers. As a result, more people start to report failures. After repair of this kind of fault, problems related to services of the whole group disappear. A fault management system is designed to record data related to all detected and resolved faults as well as reported failures. Most of the data refer to alarms that are used to detect and diagnose faults. Generally, all active network elements throw alarms, but there are passive pieces of equipment in the network incapable of producing alarms. Therefore, not all the network is under the real-time supervision of the fault management system. Data about alarms is entered into the database automatically while other data (e.g. about failures reported by customers) is entered by technicians during the resolving process. Accordingly, databases give an accurate insight into faults, causes of faults and failures that have been reported. In [44] we presented results of the operational data analysis referring to the Croatian telecom T-HT broadband network. The following distribution of faults considering their locations has been derived from operational data. The majority, 70.86%, of faults occur in the customer part of the network (part 3). In the access part (part 2), 26.53% of faults appear, while the remainder, 2.61%, occur in the core part of the network (part 1). Devices in part 1 are mostly doubled, which means redundancy and fault-tolerant characteristics. On the contrary, there are no redundancies related to devices in parts 2 and 3. Therefore, each fault in these parts causes service failure. Early detection and diagnosis of network element outages that appear in the access part (part 2) of a broadband network is the subject of research presented in this paper.

![](/api/attachments/JFRV7EC5/fulltext/images/5d9409a047e6f932d20d86924da3208eaf8b72b83fd113e568327a730dde2625.jpg)  
Fig. 1. Broadband network — main parts. Source: T-HT (2012)

In most cases, a network element outage leaves a clear trail in fault management logs. Moreover, it is possible to distinguish common sequences of reported failures from much intensive reporting that occurs during a network element outage that has affected a larger group of customers. Figs. 2 and 3 depict the daily number of failures reported by customers related to two DSLAMs in the network during the whole year. Fig. 2 shows common situations that happen most of the time, where only minor problems occur on DSLAM during a year and affect particular customers only. On the other hand, Fig. 3 shows an example where DSLAM outages happened 4 times in a year, seriously affecting services offered to the whole group of customers connected to it. For example, in the Croatian T-HT network there are approx. 6000 DSLAMs, so outages like those described don't represent rare events.

Early and accurate outage detection and diagnostics are of great importance for telecom operators because they reduce costs and increase customer satisfaction and loyalty.

Generally, the accuracy of network element outage recognition can be increased by minimizing missed detection, i.e. false negatives. It should be noted that in fault management practice, there are two problems that often reduce accuracy of outages recognition and promptness.

First is an inadequate monitoring system, designed in a way that causes excessive alarm delays and imposes settings of additional criteria on alarm conditions in order to reduce alarm oscillations and to avoid occurrences of alarm storms. False alarms create severe problems for telecom operators. For example, a false alarm may result in unnecessarily sending the maintenance staff onsite for troubleshooting and divert them away from the real faults. False alarms may trigger unneeded actions to be taken on equipment such as resetting, which cause interruption of the customer's service even when it is not necessary. Therefore, wrong decisions, as a consequence of the false alarms, cause incorrectly routed fault-repair process <sup>fl</sup>ow and can lead to large-scale problems, especially when Trouble Tickets are opened massively for proactive fault repair, in automatic mode. On the contrary, if false alarms are frequent, staff may start to ignore alarms, assuming that they are probably all false. Anyway, the uncertainty and confusion that false alarms bring could ultimately lead to ef<sup>fi</sup>ciency reduction and increased maintenance costs. Techniques like deadbands, delay timers and <sup>fi</sup>ltering can signi<sup>fi</sup>- cantly reduce false alarms; a side effect, however, is that using these techniques introduces delay in raising alarms, i.e. detection delay. The design often represents a compromise between minimization of detection delay, false alarm rate and missed alarm rate.

![](/api/attachments/JFRV7EC5/fulltext/images/ac10c8cf99bb37f7907a45f2a7da50a81244dda48b52a409c5b27557a92b508f.jpg)  
Fig. 2. Reported failures on DSLAM in one year; operation without outages.

![](/api/attachments/JFRV7EC5/fulltext/images/cd9b265f164ca3fd3dd0a59fadec2162695a56b2b4d3503c5392aca6e929d906.jpg)  
Fig. 3. Reported failures on DSLAM in one year; outages have occurred.

Second, as we said before, passive pieces of equipment in the network are incapable of participating in generating alarms. Also, some hardware and software defects are not covered by alarms. Problems in such cases can only be detected indirectly, through alarms generated by other equipment or through adequate measurements. Furthermore, alarms will not occur in the cases when thresholds for alarm generation are set incorrectly or when new equipment that is not yet correctly con<sup>fi</sup>gured is installed in the network. Available operational data indicate that nearly 25% of alarms that must or should appear in the Croatian T-HT broadband network fail for some reason and are never raised. We can conclude that there are serious shortcomings in the alarm systems associated with the broadband networks. Our opinion is that these shortcomings can be alleviated by implementing additional functional modules in the fault-management system. These modules should be able to do early detection of outages and faulty-element isolation. They must be designed and implemented appropriately to improve and speed up decision making in the fault-management processes. The research and solution presented in this paper follows this idea. Accordingly, the contributions of this paper are:

• Data related to dynamics of customers' failure reporting are statistically analyzed. Distributions of times that elapse between occurrences of alarm and the moments when customers report failures are derived. The analysis showed that timing of customers' failure reports and their content have information potential to be utilized in the process of early detection of network element outages.

• We propose a new method for speeding up outage detection and faulty network-element isolation that increases ef<sup>fi</sup>ciency of the fault management system; in some extreme cases it is possible to detect an outage 6 h before the occurrence of alarm. The method is developed in a way that meets requirements of the speci<sup>fi</sup>c telecom industrial case and is based on a two-stage hybrid detector. It is adjusted to allow decision making based on rare events and in conditions of considerable uncertainty in the system. The method was tested on historical data collected over one year and the parameters of accuracy and ef<sup>fi</sup>ciency are evaluated.

• The method can be generalized and used in similar cases and situations not related only to fault management in the telecom domain; for example, in all cases where correct decisions have to be made in a short period of time and based on a small number of input events. A precondition is that input information has time-stamps and additional attributes which allow high accuracy of decision-making based on them.

The remainder of the paper is organized as follows. In Section 2, related work on early fault and anomaly detection is presented. Section 3 introduces the data set used and characteristics of failure reporting behavior. Section 4 introduces our proposed method. Section 5 shows the results and performance evaluation and <sup>fi</sup>nally we conclude this study in Section 6.

## 2. Related work

Operationally, a fault should be detected and repaired as soon as possible. This improves system security and quality as well as customer satisfaction. To overcome delays in fault detection and problems with missing alarms, some researchers suggest the usage of additional predictor variables that carry relevant information for speeding up detection. Telecom operators usually resolve this problem by some self-made solutions that are rarely presented in public. On the other hand, a good number of proposed solutions have been published related to the problems of anomaly and intrusion detection. With modi<sup>fi</sup>cations these solutions can be applied to the problem of early outage detection based on discovering signi<sup>fi</sup>cant increases in customer activities related to failure reporting.

Early fault detection is a subject of research in various industries. The authors of [2] analyzed alarms as early indicators of abnormal situations in industrial processes. Diagnostic techniques are classi<sup>fi</sup>ed into two main groups: model-based and process-history based. While seeking a solution for a concrete problem, the authors concluded that improvements in detection can be achieved by combining activities in three main areas: articulating of expert knowledge in rules, decreasing alarm response time, and analysis of alarm sequences.

The detection problem (in the literature often termed change point estimation) refers to determination of the moment when some disturbance or irregularity started. Related to telecommunications industry, two approaches to fault detection improvements dominate and can be distinguished in literature. According to the <sup>fi</sup>rst approach, improvement is based on better management of alarms arising from various parts of a system. Another approach is oriented to indirect variables through which anomalies in system are detected. In [1] detecting unusual system behavior is used for managing alarm storms. Latencies among multiple alarms put load on the control system and reduce the capacity for processing root-cause alarms. The authors of [1] proposed a model with several queuing nodes for alarm preprocessing and alarm <sup>fi</sup>ltering to reduce latency and system overload

In the paper [3] the authors analyze various types of network anomaly detection methods, such as: Change-Point Detection, Wavelet Analysis, Covariance Matrix Analysis, Principal Component Analysis (PCA), Kalman Filter (Statistical methods) and Heavy-Hitter Detection, Heavy-Change Detection (Discrete Algorithms) and Machine Learning approaches — Adaptive Threshold-Based, Clustering, Bayesian Belief Networks, Entropy-Based, HMM (Unsupervised learning) and Markov Decision Processes (Learning with Additional Information). A similar analysis of methods can be found in [12] and [16]. The conclusion is that room still remains to improve the ef<sup>fi</sup>ciency of anomaly detection and to understand which method will perform well in what problem domain.

Evaluations of various methods are presented in [19,21,26,32] and [33]. A survey of various failure prediction methods can be found in [41]. Two theories can leverage fault detection related to telecommunications domain: signal detection theory and decision theory. Detection methods help to adjust sensitivity of detection, while through decision analysis (as a part of decision theory) the bene<sup>fi</sup>t of true alarms and the costs of false alarms have to be calculated for each speci<sup>fi</sup>c application.

Early warning systems are used in the <sup>fi</sup>eld of communication for detection of malicious attacks and intrusions, but in medicine they are used for detection of epidemics and for diagnosing diseases: see for example [4] and [17]. An early detection method based on a machinelearning approach is presented in [5]. A Distributed Time-Delay Arti<sup>fi</sup>cial Neural Network is used to solve a multi class problem of network attack detection, see [11]. Methods of soft computing are often used alone, but they can be used in combination with rule-based expert systems too. Generally, an approach to anomaly detection involves the comparison of two time series. The <sup>fi</sup>rst series describes a user's activities without the presence of an intrusive factor, while the second time series describes a user's activities with one or more intrusive factors. Thus, the data collected can be used to create a knowledge database that contains the patterns of the customers' activities as a function of equipment faults.

The authors of [6] proposed a method based on three-step sketches that allows computation of PCA and improves the true and false positive detection rates. The possibility of improving detection based on the PCA method supplemented with Support Vector Data Description (SVDD) algorithm was explored in [24]. This approach is effective for nonlinear process modeling. Ashfaq et al. [7] analyzed the methods most often used for network anomaly detection and proposed a few promising guidelines to improve the accuracy and scalability of Network Anomaly Detection Systems. In the context of our work, the guidelines to improve the detection accuracy numbered 1, 2, 4 and 7 have importance. Xiong et al. [8] analyze two methods for detection of anomalies that occur in cloud computing systems. The <sup>fi</sup>rst is based on synergetic neural networks (SNN), while the second is based on catastrophe theory (CT). Both represent new approaches vis-à-vis standard detection methods and are based on dynamic characteristics of the network traf<sup>fi</sup>c in cloud communications.

The authors of [9] discuss 4 challenging tasks in anomaly detection: multi-modal traf<sup>fi</sup>c (the boundary between normal and anomalous events is not precise), network attacks adapt themselves continuously, previous known anomalies would soon be out of date and network traf-<sup>fi</sup>c data often contain noise which is very similar to the true anomalies. These four issues can all pose dif<sup>fi</sup>culties in traf<sup>fi</sup>c anomaly detection.

Single model approaches are very unreliable, so some authors propose a combination of anomaly detectors generated by various rules and characteristics (i.e. a combination of atomic detectors). The combination leads to stronger and more robust detection: the proposed algorithm improves the detection accuracy by 10% to 20%. Al-Mamory and Zhang [10] consider the possibility of reducing the number of false positive alarms. This is achieved by a data mining technique that has been developed to group alarms and to produce clusters. By using the nearest neighboring algorithm for alarm clustering, the average reduction ratio was about 74% of the total alarms. In order to reduce false positive alarms, various techniques that impose delays and clustering are analyzed in [23,27,31], and [37]. Feature-based analysis very often brings bene<sup>fi</sup>ts compared with volume as a principal metric; accordingly in [13] anomaly detection via IP address entropy demonstrates the best results, similarly in [30]. The authors of [39] used a sequencematching algorithm to distinguish common user behavior from anomalous behavior by smoothing the similarity stream in order to detect anomaly.

A hybrid approach for anomaly detection was used in [14], where a method for entropy calculation is supplemented with a Support Vector Machine model for better anomaly identi<sup>fi</sup>cation. A similar approach is presented in [22]. In [15] an ensemble of three methods with special characteristics: clustering, local anomaly detection and anomaly detection fusion by averaging was implemented to improve anomaly detection accuracy. Similarly, hybrid approaches can be found in [34]. Traf<sup>fi</sup>c volume and <sup>fl</sup>ow are used as parameters to detect traf<sup>fi</sup>c anomaly in [20]; Six Sigma and varying tolerance factor methods are used to identify dynamic thresholds. A system for alarm grouping in order to facilitate <sup>fi</sup>nding a common cause, named CueT, was introduced in [28], while in [29] a real-time alarm algorithm which can recognize traf<sup>fi</sup>c anomaly, based on dynamic thresholds settings, was presented. In [35] different approaches to alarm correlations are analyzed, such as dynamic recognition of statistical patterns based on historical alarm data. The possibility of improving alarm system based on learning automata is presented in [38].

One example of an intelligent alarm production system in a telecommunication network is presented in [36]. The authors of [40] analyzed the recognition of four classes of network traf<sup>fi</sup>c anomalies: outages, <sup>fl</sup>ash crowds, attacks, and measurement fail, using data from 2 sources – Simple Network Management Protocol (SNMP) queries sent to network nodes and data available from IP <sup>fl</sup>ow monitors – by applying a variety of time-frequency analysis techniques. The Operational Fault Detection (OFD) class of algorithms for detection fault signatures is described in [42], while in [43] the authors predict failures using a series of events and their occurrence times, applying Hidden Markov Model. Adjusting the decision threshold of a naive Bayes classi<sup>fi</sup>er is used in defect prediction models which are analyzed in [25].

As was already mentioned, in this paper we describe the design of a two-stage hybrid detector. Its operation is based on four well-known detection approaches (time-based detection, Neyman–Pearson detection, Bayesian network decision approach and early detection concept) which are composed in an original way. The time-based detection principle means usage of a time-stamped variable as base for making decision and is applied, for example, in papers [47–49]. The Neyman– Pearson detection approach for calculating decision boundaries, detection rate and false alarm rate is used in [52–54]. Two examples where Bayesian networks are used for classi<sup>fi</sup>cation in probabilistic expert systems are presented in [50,55]. Early detection of problems based on sensitive statistical methods for critical-values calculation and triggering of the “out-of-control” signal is described in [4,51].

## 3. Characteristics of failure reporting behavior

The data sets which have been used in this study for discovering patterns in sequences of customers' trouble calls representing (non) existence of an outage, were obtained from two main sources. The <sup>fi</sup>rst source – the Trouble Tickets database – contains information related to trouble reporting and troubleshooting. Four <sup>fi</sup>elds from the database were used, see Table 1.

The second data source – the Error Logging database – is a component of the Network Management System. It includes information about network element outages (alarm logs). Relevant data extracted from the Error Logging database, is named the Alarm Logs table and is shown in Table 2.

We analyzed data collected during the period from January 2012 to December 2012. The total number of recorded failure reports submitted by customers to the call center in this period was 780,000 while the number of network element outages in the same period was 788. After linking and matching the data from the trouble ticket and alarm logging records, our data set contained 3723 records related to failure reports. These 3723 records represent failures caused by 542 network element outages in the yearly period mentioned. The remaining 246 outages did not cause any customer's trouble calls, so they were not relevant for further analysis. Most likely, they represent either very short-term outages so customers didn't notice them or outages that didn't affect the quality of customer service.

Relevant data extracted from the Trouble Tickets database (Trouble Tickets table).

<table><tr><td>ID</td><td>Field name</td><td>Field description</td></tr><tr><td>1</td><td>Faulty_Service</td><td>Affected service, identified according to customer&#x27;s reports. For the purpose of this study only ADSL and IPTV related services have been selected.</td></tr><tr><td>2</td><td>Reporting_Time</td><td>The time at which the customer who reported failure had called contact center.</td></tr><tr><td>3</td><td>Fixing_Time</td><td>The time at which the fault was fixed. Information entered by technician who had fixed the fault.</td></tr><tr><td>4</td><td>ID_DSLAM</td><td>DSLAM identification. Unique ID for entire network. This field is used as a link to the alarm logs table.</td></tr></table>

Table 2  
Relevant data extracted from the error logging database (alarm logs table).

<table><tr><td>ID</td><td>Field name</td><td>Field description</td></tr><tr><td>1</td><td>Element_Name</td><td>DSLAM identification. Unique ID for entire network. This field is used as a link to the Trouble Tickets table.</td></tr><tr><td>2</td><td>Fault_Type</td><td>Fault type. Possible types are: break down, service degradation or occasionally occurring fault.</td></tr><tr><td>3</td><td>Fault_Cause</td><td>Causes of problems are grouped as software error, hardware failure, transmission and power supply.</td></tr><tr><td>4</td><td>Alarm_Start_Time</td><td>The time at which the alarm first appeared.</td></tr><tr><td>5</td><td>Alarm_End_Time</td><td>Alarm ceasing time, after repair.</td></tr><tr><td>6</td><td>Affected_Customers</td><td>The number of customers affected by the network element outage.</td></tr></table>

Beside the two mentioned main sources of input information, there are several additional sources which are used for multi-class classi<sup>fi</sup>cation, i.e. for faulty element isolation. Predictor variables, introduced in Table 3, represent those explanatory variables selected among the system variables which have a signi<sup>fi</sup>cant impact on accuracy of classi<sup>fi</sup>cation.

Our intention was to consider the time period before the moment of alarm arrival and several hours after the element repair. In this period we analyzed the behavior of customers whose services are unavailable or degraded with regard to the reaction speed and number of customers who had reacted. As we have already highlighted, their reactions are recorded in the form of trouble tickets. The exact moment when a network element outage happened often is not known. The reasons for this are the incapability of producing alarms, for passive, and the imperfection in the alarm system, for active pieces of equipment. Therefore, in outage detections we should rely on indirect “symptom” variables such as customer trouble reports.

Data available in Trouble Tickets and alarm logs contain information about the time when a customer reported failure as well as about the time when alarm was raised. Due to imperfect design of the alarm system, in most cases an alarm arrives after the <sup>fi</sup>rst customer complaints about service. In real fault management systems there is a certain amount of time that elapses from the occurrence of element outage to its announcement in the form of an alarm message. There are the following phases in the process of alarm creation that take time: problem detection, veri<sup>fi</sup>cation of criteria for declaring an alarm, composing the alarm message and sending it to the monitoring system, displaying alarm message and recording the message in the Error Logging

## Table 3

De<sup>fi</sup>nitions of input and output variables used for multi-class classi<sup>fi</sup>cation.

<table><tr><td>Variable</td><td>Definition</td><td>Value</td></tr><tr><td>Line measurement</td><td>Results of triggered line measurement on the customer&#x27;s line</td><td>0 if operating1 if broken</td></tr><tr><td>Announced work DSLAM</td><td>Announced work on a DSLAM</td><td>0 if none1 if any</td></tr><tr><td>Announced work cable</td><td>Announced work on a cable</td><td>0 if none1 if any</td></tr><tr><td>TM result cable</td><td>Text mining outcome</td><td>0 if other1 if cable</td></tr><tr><td>TM result DSLAM</td><td>Text mining outcome</td><td>0 if other1 if DSLAM</td></tr><tr><td>DSLAM status</td><td>The operational status of a DSLAM</td><td>0 if operating1 if blocked</td></tr><tr><td>Network element</td><td>Network element in fault</td><td>DSLAM/cable/individual fault</td></tr></table>

database. For example, a more detailed analysis of end-to-end delay of alarm process and inter-process latency is presented in [1]. The authors of [18] consider the relationship among detection delay, false alarm rate and missed alarm rate, using a Markov process combined with techniques of deadbands (alarms are raised and cleared according to two different limits) and delay-timers (the alarm is raised if n consecutive samples cross the alarm limit, the alarm is ceased if m consecutive samples go below the limit). In addition to alarm delays, some alarm messages never appear, partly because of failures and partly due to wrong matching/pairing.

To exploit characteristics of the customers' failure reporting behavior for early outage detections, it is important to quantify the speed of customers' reaction to the outage occurrences and service failures.

Based on this knowledge, the telecom operator can adjust response times of their management systems that can automatically react at the very beginning when the failure reporting starts. Customers' failure reporting behavior is complex. The time that elapses from element outage that causes service failure to the moment of reporting the failure dominantly depends on:

• customers' average daily usage of services (whether the customer is using the service at the time or shortly after the outage occurs)

• customers' expected actions/behavior (active or passive/indifference) in the moment when she becomes aware of service failure (if the customer knows reporting procedure, whether the customer is trying to <sup>fi</sup>x the problem alone, habit of calling call center or habit of passively waiting until the service doesn't start to work again etc.).

Our model is based on the following assumptions. The alarm arrival time (alarm start time) is set as a = 0, thus failure reporting time b can be less or greater than 0. The purpose of the analysis is to <sup>fi</sup>nd two probability distribution functions of times elapsing between alarm arrival and failure reports. If failure reports arrive after alarm reporting, delay times are considered, but if reports precede the alarm, reporting precedence is said to occur. An algorithm for calculating delay and precedence times is listed below. A precondition for the algorithm is to have completed records in both tables, which is not always the case due to the incompleteness of the data and a variety of errors that occur in production environment. Missed data were almost impossible to reconstruct, so we reject uncompleted records. There were about 1% of uncompleted records so this does not mean a statistically signi<sup>fi</sup>cant loss of information.

## Algorithm: calculating of precedence/delay.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
01 sort table Alarm Logs on Alarm_Start_Time ascending
02 sort table Trouble Tickets on Reporting_Time ascending
03 for each  $a_{i} \in$  Alarm_Start_Time do
04    Temp_DSLAM = ID_DSLAM
05    T1 =  $a_{i}$  - 24
06    T2 =  $a_{i}$  + 24
07    for each  $b_{i} \in$  Reporting_Time in range{T1 to T2} do
08    if Element_Name = Temp_DSLAM then
09    if delay =  $b_{i}$  -  $a_{i}$ 
10    add new record in Results
11    write Temp_DSLAM, delay
12    end if
13    end for
14 end for
15 select Results
16 do 2-minute histogram
</div>

The Algorithm is designed in such a way that for each element outage found in the Alarm Logs table, related failures reported within time interval (time window) T2–T1 are found in records from the Trouble Tickets table. For records that ful<sup>fi</sup>ll the condition, the difference (Reporting\_Time − Alarm\_Start\_Time) is calculated that represents precedence or delay of reporting about failures. The calculated times are then sorted according to 2 minute intervals, and the result is the precedence/delay times distribution depicted in Fig. 4.

Around 400 min after an alarm arrives, the number of reported failures becomes so small that they start disappearing into noise. Also, before the appearance of an alarm, customers are reporting failures in increased volume.

![](/api/attachments/JFRV7EC5/fulltext/images/752e4af9467ab561263c0fa51b9d5e503af86e8eba7efa5cb4d74dbdd04deb2d.jpg)  
Fig. 4. Precedence/delay time distribution.

The curve shown in Fig. 4 re<sup>fl</sup>ects two main phases in the failure reporting process that should be modeled separately because each phase has unique conditions and characteristics. They can be described as follows:

• First is a period when dif<sup>fi</sup>culties begin to intensify – internal error counters are incrementing, service is degraded – but in this period no alarm has yet appeared. At the beginning of this period, problems with service may occur sporadically for various reasons.

• The beginning of the second period coincides with the alarm — a network element is blocked and a whole group of customers affected by the fault have lost their service, and they report failures intensively. After that, the fault is being repaired, and service will become available to most users. Transient echoes of the fault are possible, manifested in a small number of failures reported by customers whose devices were left in some suspect or problematic state which prevents their services from starting to function. After that, the number of reports decreases and they then become lost in the noise representing sporadic failure reports that are not related to the original element outage.

We eliminate average noise from the <sup>fi</sup>rst part of the curve depicted in Fig. 4 and create a histogram consisting of 10-minute bins (Fig. 5). We approximated empirical data related to the <sup>fi</sup>rst phase with values of the following three distributions: Exponential, Weibull and Gamma.

We used the chi-squared test to test the following hypotheses: “empirical data <sup>fi</sup>t the X distribution with the signi<sup>fi</sup>cance level of $\alpha = 0 . 0 1 \ "$ where X represents one of the three above mentioned distributions, to con<sup>fi</sup>rm or reject particular distributions. Results of testing the hypotheses are shown in Table 4.

![](/api/attachments/JFRV7EC5/fulltext/images/55715d699a693dc0eb10a358b571b45e06a5880072327187aa51608aeee9cdaf.jpg)  
Fig. 5. Fault reporting precedence.

It is evident that the chi-squared test con<sup>fi</sup>rms only one hypothesis: empirical data <sup>fi</sup>t the Exponential distribution with the signi<sup>fi</sup>cance factor (level) of α = 0.01, while the others should be rejected.

In the second phase, by de<sup>fi</sup>nition, the element is blocked and services fail. Similarly to what we do for the <sup>fi</sup>rst phase, we create a histogram consisting of 10-minute bins (Fig. 6). By eliminating noise and the tail the histogram drops and as a result it represents the relevant times more accurately. We approximated the empirical data with the following four distributions: Weibull, Poisson, Gamma and Lognormal.

It is obvious that the Log normal distribution represents the set of empirical data well. However, we applied the chi-squared test to the following hypothesis: “empirical data <sup>fi</sup>t the X distribution with the signi<sup>fi</sup>cance level of $\alpha = 0 . 0 1 \ "$ where X represents one of the four distributions mentioned, to con<sup>fi</sup>rm or reject a particular distribution with the chosen level of signi<sup>fi</sup>cance. Results of testing the hypotheses are shown in Table 5.

The hypothesis is accepted if the chi-squared value of deviations between empirical and theoretically obtained data is less than the critical value 99% (1 − α). Also the hypothesis is accepted if the calculated p-value is greater than the signi<sup>fi</sup>cance level (α).

P-value is the probability of getting the same or more extreme results when the null hypothesis is true. In accordance with the results of the Chi square test given in Table 5, only the hypothesis that the empirical data are distributed according to a lognormal distribution can be accepted; other hypotheses are rejected.

From the cumulative distribution (Fig. 7) it is evident that the majority of reported failures (90%) occur in the <sup>fi</sup>rst 100 min from the moment when an element is blocked (alarm started). In the <sup>fi</sup>rst hour 72% failures have already been reported.

Fig. 8 shows distributions of empirical data obtained for phases 1 and 2 shown in 1-minute intervals with Exponential and Lognormal distributions that <sup>fi</sup>t the empirical data well.

It is an interesting question how many customers from the entire group of affected customers actually report the failure during the element outage. Two curves are drawn from empirical data containing a sample of $\mathrm { N _ { A } } = 7 3 2 8 7$ customers affected by outages. The <sup>fi</sup>rst curve (solid line) displays the percentage of users who reported the failure out of the total number of affected customers. The second curve is a 1-percent cumulative. It is evident that in 90% of cases, the number of customers that report the failure does not exceed 11%. In 99.7% of cases, the number of such customers does not exceed 27%. The average number of customers who report failure during an outage is 5.08% — a relatively small number.

The distributions shown in Fig. 9 indicate the number of input events which our detection method should rely on. If we take into account the fact that on average the number of customers connected to a DSLAM is about 150 and if, on average, only 5% of customers report a failure, this results in only 7.5 relevant reports during the whole outage timeline on average. Therefore, outage detections have to be done on a small number of events.

Table 4  
Chi-square test, <sup>fi</sup>rst phase.

<table><tr><td>Distribution candidate</td><td> $\chi^{2}_{(x)}$ </td><td> $\chi^{2}_{(0.99)}$ </td><td> $\chi^{2}_{(x)} < \chi^{2}_{(0.99)}$ </td><td>Acceptance of the hypothesis</td></tr><tr><td>Exponential</td><td>45.9</td><td>54.7</td><td>Yes</td><td>Yes</td></tr><tr><td>Gamma</td><td>59.8</td><td>52.2</td><td>No</td><td>No</td></tr><tr><td>Weibull</td><td>56.4</td><td>53.4</td><td>No</td><td>No</td></tr><tr><td>Distribution candidate</td><td>Significance level α</td><td>p-Value</td><td>p &gt;α</td><td>Acceptance of the hypothesis</td></tr><tr><td>Exponential</td><td>0.01</td><td>0.067</td><td>Yes</td><td>Yes</td></tr><tr><td>Gamma</td><td>0.01</td><td>0.0014</td><td>No</td><td>No</td></tr><tr><td>Weibull</td><td>0.01</td><td>0.0049</td><td>No</td><td>No</td></tr></table>

![](/api/attachments/JFRV7EC5/fulltext/images/f6b211ecfc020af68282c1e162a496d65d18105c493bfee2c644d2a83e9ee2f8.jpg)  
Fig. 6. Fault reporting delay.

The results of statistical modeling presented in this section show the following:

• Delay between the moment when dif<sup>fi</sup>culties with element functioning start and the moment when <sup>fi</sup>rst failure reports occur is quite short, i.e. the <sup>fi</sup>rst reports start to arrive just after the moment of malfunction. This happens because today the usage of broadband services has become so intense and continuous that it includes any time of day and night.

• The number of reported failures that arrive during the outage is small but suf<sup>fi</sup>cient to support detection.

We can conclude that the sequence of reported failures has information potential that can be utilized for early detection of network element outages. Fig. 10 shows the timeline of a network element outage with the sequence of events and phases for “dif<sup>fi</sup>culties in work” type of malfunction, from fault occurrence, through failure reporting, over fault <sup>fi</sup>xing, up to the normalization. The corresponding number of failures reported by customers during various phases of an outage is sketched as a curve.

## 4. Method for early detection of outages

Generally, design of a method depends on the nature of the relevant process and the characteristics of input data used. We based our design on the following <sup>fi</sup>ndings listed in the previous section:

• The relative number of failures reported per outage of the individual elements is small.

• A relatively large amount of historical data (fault management) is available and suitable for machine learning.

Table 5  
Chi-square test, second phase.

<table><tr><td>Distribution candidate</td><td> $\chi^2_{(x)}$ </td><td> $\chi^2_{(0.99)}$ </td><td> $\chi^2_{(x)} < \chi^2_{(0.99)}$ </td><td>Acceptance of the hypothesis</td></tr><tr><td>Weibull</td><td>254.1</td><td>34.8</td><td>No</td><td>No</td></tr><tr><td>Poisson</td><td>2867.6</td><td>26.2</td><td>No</td><td>No</td></tr><tr><td>Gamma</td><td>203.7</td><td>34.8</td><td>No</td><td>No</td></tr><tr><td>Lognormal</td><td>27.6</td><td>36.2</td><td>Yes</td><td>Yes</td></tr><tr><td>Distribution candidate</td><td>Significance level α</td><td>p-Value</td><td>p &gt;α</td><td>Acceptance of the hypothesis</td></tr><tr><td>Weibull</td><td>0.01</td><td>1.20E-43</td><td>No</td><td>No</td></tr><tr><td>Poisson</td><td>0.01</td><td>0</td><td>No</td><td>No</td></tr><tr><td>Gamma</td><td>0.01</td><td>1.80E-33</td><td>No</td><td>No</td></tr><tr><td>Lognormal</td><td>0.01</td><td>0.092</td><td>Yes</td><td>Yes</td></tr></table>

![](/api/attachments/JFRV7EC5/fulltext/images/b36b5ddf08aea362ef496e7e80967c1ad01e09db53f7b74e50f5ba3893e92621.jpg)  
Fig. 7. Cumulative distribution of delay.

• Data from the network management system are available but we must be aware of the presence of noise and missing data.

Taking into account knowledge about the characteristics of relevant processes and the available data, we decided to build a method that relies on a two-stage hybrid statistical detector and a probabilistic diagnostic detector. The <sup>fi</sup>rst stage is responsible for outage detection, while determining the exact location of a faulty element is based on the second stage.

Since the exact times of the occurrences of all the failure reporting events are recorded, the <sup>fi</sup>rst stage should be a statistical detector based just on these data. Detection of anomalies is often based on threshold/variable value comparison to indicate threshold crossings and decide if the change actually occurred. In the case of outage detections, such an approach would not be appropriate. We need to use an adaptive threshold, due to the different capacity of the equipment. The threshold value strongly depends on the number of events i.e. failure reports relevant for detection. In turn, the quantity of reports depends on the number of customers connected to a network element whose services could be degraded. The number of customers varies from a few of them per element to nearly a thousand (as we said before, the average value is 150). The number of customers also fluctuates due to the constant provisioning of new customers and disconnecting of existing ones. Therefore, threshold values should be calculated and adapted in accordance with the number of currently active customers on a network element every time before detection starts.

In order to maximize the probability of detection we chose a Neyman–Pearson detection approach that is primarily used in resolving binary detection problems. The Neyman–Pearson approach [58] is specially suitable for use in cases where the null hypothesis (H0) denotes the absence of the signal or the absence of statistical difference between two data sets. The alternative hypothesis (H1) indicates the complete opposite, presence of a signal. Detection of an outage is very similar to signal detection, so the choice of the Neyman–Pearson detector looks like the more favorable approach. It allows us to maximize the probability of detection, while maintaining the probability of false alarm at an appropriate level [59,60]. Performance evaluation (see last section of this paper) shows that Neyman–Pearson detector is able to signi<sup>fi</sup>cantly improve ef<sup>fi</sup>ciency of the process of detecting the existence of outages and isolation of the faulty element.

![](/api/attachments/JFRV7EC5/fulltext/images/f48e42aa8ac101af5566a9d74745ef663be2158a8ac8d993b9a7b19b1564a3fd.jpg)  
Fig. 8. Empirical and <sup>fi</sup>tted distributions.

![](/api/attachments/JFRV7EC5/fulltext/images/b5749e3bc39c81f0b47bde6b969667cfe9820f0e762c9086cbe90e20f2502ca6.jpg)  
Fig. 9. Reporting rate.

In detection practice, discrete-events based and volume-based principles of detection are far more common in relation to the time-based principles. This means that a control variable is usually used to count events during a certain period of time (n-second intervals). There are several reasons for this. Firstly, sensors, detectors and counters in detector systems (e.g. radars, wireless sensor networks, calls or packet counters) do periodic readings of value at equal time intervals. In such technical cases, the number of events or measured values is large, so statistically signi<sup>fi</sup>cant distinction is possible either mutually or in relation to the noise. Thus, bin-width error does not have important in<sup>fl</sup>uence on the overall model error. The volume-based method has a wide range of applications in communications, radar, wireless sensor networks, network attack detection, biomedicine, etc. Secondly, individual events are not distinguishable from each other on the basis of a time attribute because such an attribute usually doesn't exist. Finally, detection speed is great, in fact it is performed within a single scanning interval so there is no need for additional speeding.

The situation is completely different in the case of network-element outage detections. There is no periodic scanning but failure reports arrive in random order with unpredictable timing. Each report has a timestamp attribute. Inserting the arriving reports into arti<sup>fi</sup>cial time intervals would not make sense because it would result in a very big bin-width error in the learning phase and signi<sup>fi</sup>cant discretization error in the usage phase, especially for network elements with a small number of connected customers. The timestamp which is assigned to each failure report allows us to use time differences in report arrivals. Finally, fault management requires an ef<sup>fi</sup>cient system for early detection. Any delay due to introducing some arti<sup>fi</sup>cial full time intervals would decrease performance in the sense of detection speed. In the design of our detector we applied a time-based principle. The control variable is adjusted in a way to accept the time difference between occurrences of two consecutive events. We are convinced that such an approach is more precise because it exploits all available information and avoids bin-width errors which are caused by counting type of control variables. Information about the time remains intact, which is very suitable for the case where the relative number of reported failures per outage is relatively small.

![](/api/attachments/JFRV7EC5/fulltext/images/0b405ea3dacc18d90859015688f65393b74fb13207dcfbac855e3958050e1979.jpg)  
Fig. 10. Outage timeline.

To the best of our knowledge, a time-based statistical method has not been used previously in the form we suggest in this paper. A similar method has only been used for the analysis of rare events in the <sup>fi</sup>eld of temporal data mining. The goal of temporal data mining is discovering hidden temporal patterns of unexpected trends. This is usable for rare-events analysis in outbreaks of infectious diseases, earthquakes, warning systems for ecological disasters, and fraud detection. In some situations, only the ordering among the records is important for temporal analysis, and the notion of time as such is not. But in situations of temporal analysis of rare events [47], the time of occurrence of the event (timestamp) is given for all events as an attribute. The authors in [47] calculate risk of certain severe adverse reactions in relation to the sequential patterns of drug exposure. In Ref. [48] a time-stamped vector of features is used to detect cellular phone fraud. Similarly in Ref. [49] a general framework for <sup>fi</sup>eld-failure prediction using failuretime data with dynamic covariate information is presented. Retaining the time variable in continuous form discretization error (truncation error) is avoided.

This <sup>fi</sup>rst stage of detector is used to determine whether a group or an individual fault is present or not. The second stage is a Bayesian network classi<sup>fi</sup>er, based on data from the Network Management and Customer Relationship Management providing information about the kinds and types of elements and type of failures, which is used to determine i.e. to isolate the exact element that has caused a fault. The Bayesian decision approach is suitable for multi-criteria decision and multi-class classi<sup>fi</sup>cation (for testing of multiple hypotheses). Element isolation, which means selecting exactly one faulty element from a number of elements, is a typical multi-class classi<sup>fi</sup>cation problem.

Among the other methods coming to our attention, entropy methods are eliminated due to excessive dispersion of our data and a relatively small share of the targeted events in the total amount. The method of tracking sequences (Hidden Markov Model) is rejected because of uncertainty that the customer brings in the part of fault reporting. Methods using Neural networks and similar soft computing methods are, at least for now, rejected due to potential complications with the time interdependencies. Furthermore, one can see that there are a variety of imperfections in the data sequences, so we conclude that the pattern matching technique or sequence matching technique would not be suitable because the noticed irregularities in the pattern are signi<sup>fi</sup>cant.

## 4.1. Outages detection using statistical decision technique

For calculating the statistical threshold, the data set used in Section 3 has been extended with data about faults that were not network element outages, but affected only individual customers. These additional data are also given in the form of time intervals between the arrival of two consecutive failure reports related to network elements (t<sup>e</sup> intervals). The result of such an extension is a set Q which can be divided into three subsets each representing a particular state of the network: normal operating state without outages $\left( 0 _ { \mathrm { n } } \right)$ , the period where there is a risk that outcomes of an announced work or element outage affect the operation of the network $( \mathrm { Q } _ { \mathrm { w } } )$ and operating state with outages $\left( \mathbb { Q } _ { 0 } \right)$ . The following equation holds: $\mathrm { Q } = \mathrm { Q } _ { \mathrm { n } } \cup \mathrm { Q } _ { \mathrm { w } } \cup \mathrm { Q } _ { \mathrm { o } } ,$ . Because we used real, operational data about faults, in preliminary analysis of the data we have seen that perfect separation between subsets wasn't possible, so subsets overlap as shown in Fig. 11. For example, for a failure that occurred after maintenance work in the network, we were not always sure, whether the failure was caused by exactly that work or was caused by some other factor. Such cases belong to the intersection of $\mathrm { Q } _ { \mathrm { w } }$ and $\mathbb { Q } _ { \mathrm { n } } .$ These areas of overlap are critical for the design of the detector.

![](/api/attachments/JFRV7EC5/fulltext/images/5e5ce5bfa8c4f4792f51cdee23cd85d8421067e10013756b268d4ab3516d2f0b.jpg)  
Fig. 11. Data sets and intersections.

Variables and indexes used in the model as well as functions used to calculate probabilities of different events in the statistical model are described in Tables 6 and 7.

Values of control variable $\lambda ( \mathrm { i } )$ are calculated from time intervals t<sup>e</sup> and normalized by $N _ { A } ^ { e }$ regarding different number of customers per network element. The natural logarithm is used here because the standard linear scale does not give us a suitable view — the $t _ { c } ^ { e }$ covers a large range of values.

Finally, to calculate the probability density it was necessary to group the values of λ into classes, so we do integer rounding:

$$
\lambda (i) = \text { round } \big (\ln \big (\mathrm{t} _ {\mathrm{c}} ^ {\mathrm{e}} (\mathrm{i}) \mathrm{N} _ {\mathrm{A}} ^ {\mathrm{e}} \big).\tag{1}
$$

Probability density functions $\mathsf { p } _ { \mathsf { o } } ( \lambda ) , \mathsf { p } _ { \mathsf { w } } ( \lambda )$ and $\mathfrak { p } _ { \mathrm { n } } ( \lambda )$ are calculated for all three states of the network. Density probabilities of two consecutive faults are calculated using two-dimensional indicator functions. The indicator functions are de<sup>fi</sup>ned as:

$$
I _ {Q _ {n}} (n, \lambda) := \left\{ \begin{array}{l l} 1, & \lambda = \lambda_ {n} \\ 0, & \lambda \neq \lambda_ {n} \end{array} \right. \quad \forall \lambda , n\tag{2}
$$

$$
I _ {Q _ {w}} (m, \lambda) := \left\{ \begin{array}{l l} 1, & \lambda = \lambda_ {m} \\ 0, & \lambda \neq \lambda_ {m} \end{array} \right. \quad \forall \lambda , m\tag{3}
$$

Variables and indexes used throughout the model.

<table><tr><td>Notation</td><td>Definition</td></tr><tr><td> $e = 1,\dots,E$ </td><td>Index of a network element. E represents total number of network elements.</td></tr><tr><td> $t_{c}^{e}$ </td><td>Time intervals between arrival of two consecutive failure reports related to a network element  $e$ .</td></tr><tr><td> $i = 1,\dots,I$ </td><td>Index of a  $t_{c}^{e}$  element in set Q. I represents total number of  $t_{c}^{e}$  elements in set Q.</td></tr><tr><td> $k = 1,\dots,K$ </td><td>Index of the  $t_{c}^{e}$  element from the set Q related to faulty network element  $e$  which caused reported failures up to 7 h before an outcome of announced work or existence of an outage become known to the staff.</td></tr><tr><td> $m = 1,\dots,M$ </td><td>Index of  $t_{c}^{e}$  elements from the set  $Q_{w}$ .</td></tr><tr><td> $n = 1,\dots,N$ </td><td>Index of  $t_{c}^{e}$  elements from the set  $Q_{n}$ .</td></tr><tr><td> $o = 1,\dots,O$ </td><td>Index of  $t_{c}^{e}$  elements from the set  $Q_{o}$ .</td></tr><tr><td> $\lambda = 1,\dots,\Lambda$ </td><td>Normalized and rounded time intervals between arrival of two consecutive failure reports.</td></tr><tr><td> $\lambda_{o}$ </td><td>Threshold, the value that must be exceeded to elicit a response.</td></tr><tr><td> $N_{A}^{e}$ </td><td>Total number of customers affected by an outage on network element  $e$ .</td></tr><tr><td> $N_{R}^{e}$ </td><td>Number of customers affected by an outage on network element  $e$  who reported failure.</td></tr></table>

Functions used throughout the model.

<table><tr><td>Notation</td><td>Definition</td></tr><tr><td> $p_n(\lambda)$ </td><td>Probability of two consecutive reported failures on the same network element for the normal network state</td></tr><tr><td> $p_w(\lambda)$ </td><td>Probability of two consecutive reported failures on the same network element for the network risk state</td></tr><tr><td> $p_o(\lambda)$ </td><td>Probability of two consecutive reported failures on the same network element for the network outage state</td></tr><tr><td> $I_{Qn}(n, \lambda)$ </td><td>Indicator function for those  $\lambda$  that are related to the normal network state</td></tr><tr><td> $I_{Qw}(m, \lambda)$ </td><td>Indicator function for those  $\lambda$  that are related to the network risk state</td></tr><tr><td> $I_{Qo}(o, \lambda)$ </td><td>Indicator function for those  $\lambda$  that are related to the network outage state</td></tr><tr><td> $p_t(t)$ </td><td>Average probability of correct response in relation to the alarm timeline</td></tr><tr><td> $p_c(\lambda)$ </td><td>The overall probability of a correct response for a given threshold value (accuracy)</td></tr><tr><td> $p_{fp}(\lambda)$ </td><td>Probability of the false positive rate for a given threshold value</td></tr><tr><td> $p_{fn}(\lambda)$ </td><td>Probability of the false negative rate for a given threshold value</td></tr><tr><td> $p_{tp}(\lambda)$ </td><td>Probability of the true positive rate for a given threshold value</td></tr><tr><td> $p_{tn}(\lambda)$ </td><td>Probability of the true negative rate for a given threshold value</td></tr></table>

$$
I _ {Q _ {o}} (o, \lambda) := \left\{ \begin{array}{l l} 1, & \lambda = \lambda_ {o} \\ 0, & \lambda \neq \lambda_ {o} \end{array} \right. \quad \forall \lambda , o\tag{4}
$$

$$
\mathrm{p} _ {\mathrm{n}} (\lambda) = \sum_ {\mathrm{n} = 1} ^ {N} \left(I _ {Q _ {\mathrm{n}}} (n, \lambda)\right) / N \quad \forall \lambda , n\tag{5}
$$

$$
\mathrm{p} _ {w} (\lambda) = \sum_ {m = 1} ^ {M} \left(I _ {Q _ {m}} (n, \lambda)\right) / M \quad \forall \lambda , m\tag{6}
$$

$$
\mathrm{p} _ {o} (\lambda) = \sum_ {o = 1} ^ {O} \left(I _ {Q _ {o}} (n, \lambda)\right) / O \quad \forall \lambda , o.\tag{7}
$$

Fig. 12 shows the calculated values of functions $\mathsf { p } _ { \mathsf { o } } ( \lambda ) , \mathsf { p } _ { \mathsf { w } } ( \lambda )$ and $\mathsf { p } _ { \mathrm { n } } ( \mathsf { \Lambda } )$ . In particular, the dark line in the <sup>fi</sup>gure represents the distribution of time intervals between two consecutive reported failures in a period of outage. Failures that customers report in this period are mainly related to the outage. These data can be considered as “signal”. The light curve represents the distribution of the control variable during normal operation of the network (outage noti<sup>fi</sup>cations don't exist). It is, in fact, the distribution of time intervals between two consecutive reports of “regular” failure on customer service on the same element, caused by any other reason except group fault on the cable or DSLAM. It may be a situation like: the remote controller for the TV is broken and must be replaced; or the customer has forgotten the user password and a new one needs to be created. These data can be considered as “noise”. An overlap between the two curves exists, therefore there will be no perfect separation.

The last curve (in the middle) represents the probability distribution of the control variable related to the period during or just after the announced or unannounced maintenance work on a group network element, regardless of whether the failures are caused by the outage or not. The value of the control variable depends on the outcomes of maintenance work. Maintenance work can end up in two outcomes: “outage” if a service interruption was caused or “normal” if the work was <sup>fi</sup>nished without service interruption. It was found that outcomes of this work cannot be precisely determined in advance. As can be seen in Fig. 12. the probability distribution function related to “maintenance work in the netwo $\cdot \mathbf { k } ^ { \mathfrak { n } }$ has a large overlap with the other two subsets. The purpose of detection isn't to discover an outage's root cause (e.g. maintenance, electrical discharge, worn-out equipment, breakdown, and hardware defect) but to determine whether the outage did or did not occur. In this sense, the probability distribution function related to “maintenance work in the network” has no signi<sup>fi</sup>cance for the <sup>fi</sup>rst stage detector analysis (performance and ROC view). However, information related to “maintenance work” (Announced work DSLAM and Announced work cable listed earlier in the Table 3) are used in the second detector stage in the form of input variables to the Bayesian network because they raise the classi<sup>fi</sup>cation accuracy.

![](/api/attachments/JFRV7EC5/fulltext/images/acca8963579cc1ce77365016bf00e3f84db2757dd5447d5ef169ee29c3cc8141.jpg)  
Fig. 12. Probability density functions (normal/maintenance work/outage period)

Table 8  
De<sup>fi</sup>nitions of terms.

<table><tr><td>Notation</td><td>Definition</td></tr><tr><td>Positive</td><td>Cases classified as “positives” (outage) by the detector</td></tr><tr><td>Negative</td><td>Cases classified as “negatives” (normal) by the detector</td></tr><tr><td>Outage</td><td>Actual outage cases (faults affecting a group of customers)</td></tr><tr><td>Normal</td><td>Actual normal cases (faults affecting an individual customer)</td></tr><tr><td>TPR</td><td>True positive rate (sensitivity) = positives correctly classified/number of actual outage cases</td></tr><tr><td>TNR</td><td>True negative rate (Specificity) = negatives correctly classified/number of actual normal cases</td></tr><tr><td>FPR</td><td>False positive rate = positives incorrectly classified/number of actual normal cases</td></tr><tr><td>FNR</td><td>False negative rate = negatives incorrectly classified/number of actual outage cases</td></tr></table>

Knowing PDFs enables us to calculate the optimal threshold value. Terms concerning performance measurement of the detector are listed and de<sup>fi</sup>ned in Table 8. An optimal threshold value $\left( \lambda _ { \_ 0 } \right)$ can be determined by calculating the maximum value of the overall probability of a correct response (the accuracy) $\mathsf { p } _ { \mathrm { c } } ( \mathsf { \lambda } )$ expressed by Eq. (8). The $\mathsf { p } _ { \mathsf { c } } ( \mathsf { \Lambda } )$ is expressed as a sum of the probability of true positives and the probability of true negatives (correct rejection).

$$
p _ {c} (\lambda) = p _ {o +} p _ {t p} (\lambda) + p _ {o -} p _ {t n} (\lambda)\tag{8}
$$

The ratio of the total number of events referring to the outage $\left( \mathfrak { p } _ { \mathfrak { o } + } \right)$ and the total number of events referring to the individual type of fault $\left( \mathfrak { p } _ { 0 - } \right)$ is pre-de<sup>fi</sup>ned as 30:70, based on actual data. The dark line in Fig. 13 denotes a probability of $\mathsf { p } _ { \mathsf { c } }$ with respect to threshold value (λ): on the left side of the curve all responses are NO (the fault is not a groupaffecting fault), then p goes to a maximum, and <sup>fi</sup>nally, on the right side, declines in average value for outage 0.3.

![](/api/attachments/JFRV7EC5/fulltext/images/88abb7f3dc2373651ddd4244791bf967889b9f6980b624cdadc4296b91391509.jpg)  
Fig. 13. Accuracy.

![](/api/attachments/JFRV7EC5/fulltext/images/f4ae30499b1d9fa7ae648b5b21aee7451d5694564af5434949c6e5baafc7e3ea.jpg)  
Fig. 14. False positive and false negative rates.

Functions of the performance measures $( \mathsf { p } _ { \mathrm { t p } } , \mathsf { p } _ { \mathrm { t n } } , \mathsf { p } _ { \mathrm { f p } } \mathrm { ~ i ~ } \mathsf { p } _ { \mathrm { f n } } )$ were obtained from the following expressions:

$$
p _ {t p} (\lambda) = \sum_ {\lambda = 1} ^ {\lambda} p _ {o} (\lambda) \quad \forall \lambda\tag{9}
$$

$$
p _ {t n} (\lambda) = \sum_ {\lambda = \lambda + 1} ^ {\lambda = \Lambda} p _ {n} (\lambda) \quad \forall \lambda\tag{10}
$$

$$
\mathsf {p} _ {\mathrm{fp}} (\lambda) = \sum_ {\lambda = 1} ^ {\lambda} \mathsf {p} _ {\mathrm{n}} (\lambda) \quad \forall \lambda\tag{11}
$$

$$
p _ {f n} (\lambda) = \sum_ {\lambda = \lambda + 1} ^ {\lambda = \Lambda} p _ {o} (\lambda) \quad \forall \lambda .\tag{12}
$$

Both true positive and true negative are correct detections and improve process performance, whereas the false positive and false negative generate process waste, each in its own way. A false negative (incorrectly rejected) results in directing the trouble ticket processing to the wrong <sup>fi</sup>eld repair group of technicians, i.e. to a group for individual customer faults, instead to a team of network specialists. It causes an unnecessary on-site visit and re-dispatching to another group and is thus process waste for operator. In false positive (incorrectly identi<sup>fi</sup>ed) cases, the trouble ticket is incorrectly directed to a team of network specialists. Since this failure is not caused by an element outage affecting a group of customers, but by a fault of some other device, after the intervention of a specialist, customer service still does not work, and the failure needs to be reported again, which is process waste for operator and customer.

Obviously, threshold value $\lambda _ { 0 }$ can be adjusted to suit the business requirement. The business requirement may be to choose a threshold value which leads to highest percentage of overall correct positives. If we look at Fig. 13, this is the case if $\Lambda _ { 0 } = 1 0 ;$ there is a maximum value for $\mathrm { p } _ { \mathrm { c } } ,$ 90.5%, true positive rate was 91.95%, and true negative rate was 89.87%. However, business requirements can be different, especially in a situation where false negatives and false positives do not cause the same business costs. For example, if we want to reduce the process waste related to false negatives, then we increase $\lambda _ { 0 } ,$ e.g. from 10 to 11, then a larger number of cases will be declared as outages and overall performance falls from 90.5% to 86.3%, but false negatives fall from 8% to 0.67%. Relations between false negative and false positive cases that cause process waste are shown in Fig. 14. Threshold selection may be a matter of multi-variable analysis, where, apart from <sup>fi</sup>nancial criteria — costs, other criteria such as customer's criteria, customer satisfaction, customer segment, or still others may be used.

![](/api/attachments/JFRV7EC5/fulltext/images/fc0e27bd8f93003d7e8c01d15aa0772f50c99fc6314fb677db1778ac8c59eee8.jpg)  
Fig. 15. Total costs.

Classi<sup>fi</sup>cation of optimality issues in terms of calculation and representation of expected costs are the subject of several researches. Thus, the authors in [45] elaborate ROC representation trying to show expected costs more explicitly. Similarly, the authors in [46] present an ROCCH-hybrid method to compare classi<sup>fi</sup>ers in imprecise and changing environments in/for real-world applications, for different comparison metrics (expected cost, lift, precision, recall, and workforce utilization). In the context of telecom business requirements, two optimization strategies seem to be important. First, if penalties for exceeding the limit of the number of wrong decisions (FP or FN) are too high, then this number needs to be reduced to a permissible level. Respecting this requirement we have to maximize the probability of detection. However, considering only the frequencies of FP and FN cases (Fig. 14) is not suf<sup>fi</sup>cient from the perspective of cost-oriented optimal maintenance and business decision making, because the cost component is not emphasized as much as it needs to be. In the cases of imbalanced classes (the frequency of normal failures – negative outcomes – is significantly higher than frequencies of outages — positive outcomes) and different misclassi<sup>fi</sup>cation costs (cost of a false positive is lower than the cost of a false negative case), as in our case, de<sup>fi</sup>ciency of such a consideration is even greater. Second strategy is related to a more likely business requirement – reducing the total cost – where optimization of costsensitive learning model needs to be adapted accordingly.

The costs of dealing with various cases (wrong or right decisions) can be estimated on the basis of real business data. The cost $\mathsf { C } _ { \mathrm { t n } }$ of dealing with a true negative case is estimated to be between \$25 and \$65 (on-site repair by a technician), while the cost $C _ { \mathrm { f n } }$ of dealing with a false negative case is estimated to be between \$140 and \$260 (unnecessary on-site visit of a technician + delay in repairing the groupaffecting faulty network element + potential regulatory <sup>fi</sup>nes for a group-affecting outage + on-site repair by a team of network specialists). The cost ${ \mathsf { C } } _ { \mathrm { t p } }$ of dealing with a true positive case is estimated to be between \$100 and \$200 (on-site repair by a team of network specialists), while the cost ${ \mathsf { C } } _ { \mathrm { f p } }$ of dealing with a false positive case is between \$105 and \$220 (unnecessary on-site visit of a team of network specialists + delay in repairing the faulty equipment + potential regulatory <sup>fi</sup>nes + on-site repair by a technician). Variations occur due to different contractors' prices, or whether the work is undertaken using contractors or own staff. The cost of “on-site visit/repair by a technician” is considerably lower than the cost of “on-site visit/repair by a team of network specialists” because of expensive measuring instruments and equipments engaged in team interventions.

Thresholding is a simple and effective technique for selecting the probability that minimizes the total cost [56]. We calculate total costs for each possible threshold C(λ) from the representative training sample. Minimal expected cost is obtained by <sup>fi</sup>nding the minimum of the function C(λ). According to Elkan [57], costs have to be measured against a <sup>fi</sup>xed baseline, as an opportunity cost or a foregone bene<sup>fi</sup>t, to avoid mistakes in cost–bene<sup>fi</sup>t representation. In the two-class case, with known confusion matrix and cost matrix, as in our case, expected total cost can be expressed by the equation:

$$
C (\lambda) = \frac {\mathrm{TP} (\lambda) C _ {\mathrm{tp}} + \mathrm{FN} (\lambda) C _ {\mathrm{fn}} + \mathrm{FP} (\lambda) C _ {\mathrm{fp}} + \mathrm{TN} (\lambda) C _ {\mathrm{tn}}}{\mathrm{TP} (\lambda) + \mathrm{FN} (\lambda) + \mathrm{FP} (\lambda) + \mathrm{TN} (\lambda)}\tag{13}
$$

where the number of events TP (true positives), FN (false negatives) FP (false positives), and TN (true negatives) are obtained by varying the input parameter λ while ${ \mathsf { C } } _ { \mathrm { { f n } } } , { \mathsf { C } } _ { \mathrm { { f n } } } , { \mathsf { C } } _ { \mathrm { { f p } } } ,$ and $C _ { \mathrm { t p } }$ are related costs.

A diagram that shows total cost with respect to threshold, with $\mathrm { C } _ { \mathrm { f n } } ,$ $\mathrm { C } _ { \mathrm { f p } } , \mathrm { C } _ { \mathrm { t n } } ,$ and $C _ { \mathrm { t p } }$ as varying parameters, would give an optimal view. Fig. 15 illustrates movements of total costs for three representative quadruples of values for $\mathsf { C } _ { \mathrm { { f n } } } , \mathsf { C } _ { \mathrm { { f p } } } , \mathsf { C } _ { \mathrm { { t n } } } ,$ and $C _ { \mathrm { t p } }$ as parameter. For given related costs, an optimal threshold that gives the lowest total cost can be chosen.

## 4.2. Determination of network element in outage

Statistically-based detection of whether the outage is present or not represents the <sup>fi</sup>rst part of our proposed method for network element outage management. The second part refers to the determination of which network element is in outage. As already mentioned in the Introduction, elements in the access part of a network DSLAMs and cables are not duplicated, i.e. there is no redundancy, as is the case with most of the elements in the core part of the broadband network (e.g. switches, broadband remote access servers and service platforms). Fig. 16 shows the architecture of the network from the perspective of redundancy.

The third part of the network contains equipment located at the end user's home. This equipment is not redundant and is related exclusively to a single customer. Consequently, only failures that affect a single user can occur on this equipment, and so they are not the subject of this paper.

Fig. 16 shows that just DSLAMs and cables are critical to the operation of services offered to groups of customers because they are only non-redundant elements in the chain. The quick identi<sup>fi</sup>cation of an outage on them is operationally signi<sup>fi</sup>cant. Hereafter we will just focus on and propose improvements in locating a particular DSLAM or cable compared to the existing process in T-HT.

Data sources containing signi<sup>fi</sup>cant and valuable information for determining the exact location of a faulty element are:

Line measurement data — include data obtained through the two measurement systems. The <sup>fi</sup>rst group of data is obtained by line broadband measurements, and includes information about Bandwidth Downstream and Upstream Rates, Up/Down Signal-to-Noise Ratio, Up/Down Attenuation, Resynchronizations, Error Seconds, Equipment States, and Up/down DSLAM Power. The second group of data is obtained through DC/static measurements, such as the resistance between the wires, capacity, foreign voltage, estimated distance to the termination, etc. From these data the most useful information are the estimated distance to the termination and status of equipment. Information about the line termination indicates that the cable is broken or not, and Equipment Status indicates the status of DSLAM. Other information can be used as predictor variables but are slightly less important.

![](/api/attachments/JFRV7EC5/fulltext/images/92cc5c0208168dc5d29e3841bc4c6017673d214ffa06530dba64c6ff44cab105.jpg)  
Fig. 16. Network architecture.

Trouble Tickets data — a trouble ticket contains many details about the case of a single fault, and tracks the problem from the opening, through dispatching and fault removing, up to the closure. Data contained in the ticket can be divided into 3 parts:

• user (user data and problem description),

• technical (information on the equipment and services),

• process (information on progress, branches, tasks, time).

From these data, we try to get information about an actual failure manifestation from the customer perspective. Reason codes and the description <sup>fi</sup>eld are most useful for the analysis.

Fault management logs (technical processes and announcement logs) — here one can <sup>fi</sup>nd information about all the processes that are currently running related to the analyzed customer, furthermore, information about the announced or unannounced works in the network, as well as information about the process of migrating customers to new technology or new equipment and the like.

Apart from data logs, there are functional modules in the network management system that could be used for the purposes of faulty element isolation. These are the text mining module and module for the triggered measurement that are now independent of each other and functionally unrelated. Text mining is applied on the text that the customer types in a web reporting form (or that the agent enters in the description <sup>fi</sup>eld during the process of failure reporting) in order to classify the failure in one of n prede<sup>fi</sup>ned classes. For example, string cases that contain one of the following “bb no li, no bb sin, broadband no li, dslam error, no light ds, indic blinks, dsl no li, dslam\_er, no light dsl, no adsl, dsl dont work, not\_ok, dsl blinks, blinks ds, blinks ads, not ok” have been assigned to the class “Synchronization error” and cases with “thund, lightn, sto, stro, bur” to the class “Electrical discharges”. The current number of classes we use in T-HT is 17 (n ), and the most common classes are “Synchronization error”, “No signal”, “Jerkiness of picture” and “Electrical discharges”. The current rate of classi<sup>fi</sup>ed cases is 93% (7% remains unclassi<sup>fi</sup>ed), whereas the rate of those correctly parsed is 90%. Triggered measurements have been started automatically at the beginning of the fault repair process. Based on these measurements the ticket has been directed to the proper technician group for fault <sup>fi</sup>xing. Accuracy of measurement results is very high, except in rare situations when the measuring equipment is out of service so that measurements are not available.

A detector of a faulty network element must ful<sup>fi</sup>ll the following conditions: insensitivity to noisy and missing data, ability to learn on a large-scale data set, output values are probabilities [0–1], binary input values, fast processing and ability to bring expert knowledge in the model, so a Bayesian network emerged as a good solution.

Since the logical relationships between resources in the network are known to experts from the domain, de<sup>fi</sup>ning the structure of the Bayesian network was not a dif<sup>fi</sup>cult task. Also, all the attributes for all variables in the domain are included in the data for training, so learning the table of conditional probabilities, using the frequency of appearance of attributes in the training-set, becomes much easier. Fig. 17 illustrates the structure of the Bayesian network we designed. GeNIe2 (program environment for graphical probabilistic models) has been used to learn the parameters of the Bayesian network from a data set.

After completion of the learning process the parameters of the de<sup>fi</sup>ned network structure are calculated. Fig. 18 shows values of marginal and conditional probability distributions for the network nodes.

There are 7 nodes, 6 nodes for binary input variables and 1 node for an output with 3 states (assuming no double-faults). Input variables are treated as predictor variables, which means that the outcome (e.g. fault of the element) causes a change in the state variable and through these changes we can detect the failure. This determines the direction of the arcs in the network.

According to the proposed method, after the <sup>fi</sup>rst stage where the presence or absence of outage has been detected, the second stage starts with collecting data from three sources (text mining, triggered measurement and fault logs checking) to get predictor variables and isolate the faulty element.

Some changes have been made in the existing modules to increase the information value of predictive variables. Thus, two new classes have been introduced in the current text-mining module, “DSLAM outage” and “Cable outage.” For example, if a customer's remark in description he or she has <sup>fi</sup>led contains the words “partially”, “partly”, or their shortened version, this means that some service is up and some is down, which would mean that the DSLAM is blocked, internet service is down, voice service is up, because voice is running on other equipment. Otherwise, the words “totally” and “complete” suggest that all services are down, because the cable is broken.

Also, the existing classes could be used to improve the rate of cases positively classi<sup>fi</sup>ed into two new classes, depending on correlations between them. Variables TM result cable and TM result DSLAM were obtained from these sources. The second group of data is obtained by line measurement and control status. Using triggered measurement we get the data for the variables DSLAM status and Line measurement. Finally, Fault logs provide information about announced technical activities running in the network that can cause outage, and give the data source for the variables Announced work DSLAM and Announced work cable. These variables constitute the data content that are used as the inputs to the Bayesian network, which determines the probability of fault location.

The second stage, in addition to the function of element isolation, has a useful feature that provides the ability to detect an incorrectly recognized outage in the <sup>fi</sup>rst stage. In this case, the previous classi<sup>fi</sup>cation may be corrected, if the probability of the outcome is greater. In this way, FPR can be additionally reduced.

![](/api/attachments/JFRV7EC5/fulltext/images/6eae64370ef61aee58ff26b908d106bbd27372e5ac12c492411fa4d935ce66ef.jpg)  
Fig. 17. The structure of the Bayesian network.

![](/api/attachments/JFRV7EC5/fulltext/images/be14ea726d16c0c1a647e55a98fd3b942eadcc207a9486ce3c2907cc6b27e6df.jpg)  
Fig. 18. The joint probability distribution of the Bayesian network.

4.3. An integrated system for early detection of outages and faulty element isolation

We propose connecting modules of the two-stage detector into an integrated system for early outage detection and faulty element isolation. Fig. 19 shows the current process already implemented in T-HT (the left side, in black) and the proposed solution (on the right side of the <sup>fi</sup>gure, in red). Four symbols are used in the <sup>fi</sup>gure: rectangles represent subprocesses (tasks), a can represents data store, trapezoids represent manual operation while hexagons represent data preparation tasks. Position and role of the detector in the overall fault management process is clearly designated.

Generally, desirable characteristics of a fault management system are: quick detection, ability to precisely isolate a faulty element, robustness and adaptability. Our idea is to move “decision making” as early as possible in the fault repair process, preferably to utilize new values of prediction variables as soon as they appear and become available to the detector, and not to wait for a subsequent process stage for their use. The detector is positioned in the process in just the right way to comply with the aforementioned characteristics. Robustness under various noise or uncertainties related to the process is ensured by choosing an appropriate method that is resistant to them.

![](/api/attachments/JFRV7EC5/fulltext/images/75f087afe921735cf501f70f66cf0efacd9f6569b4dcea37b16acdddeccc6dea.jpg)  
Fig. 19. The group-affecting fault detection process that now exists in T-HT and proposed extensions.

Also, using a type of detector that enables learning could be valuable for network administrators because it is adaptable to changing conditions, e.g. when the network grows in size and complexity, when users change their behavior, or generally when more information becomes available. Implementing this detector in a production environment opens the possibility of automating fault-repair management and ensures that the decision-making process is controllable. This system is adjusted to a speci<sup>fi</sup>c problem and considerably improves the fault management process in T-HT, but it can be applied in similar situations where accuracy of event detection and element classi<sup>fi</sup>cation are both required. As we stressed before, the presuppositions are: the control variable should be time-stamped (continuous time) and relevant input events should be appropriately described by additional attributes.

## 5. Performance evaluation and result discussion

Widely accepted measures for evaluating the obtained results in signal detection and decision theory are: the receiver-operating characteristic (ROC) curve which expresses sensitivity as a function of speci<sup>fi</sup>city; $\mathtt { R } ^ { 2 }$ (R square), a measure of model suitability; the aforementioned parameters (TPR, TNR, FPR, and FNR); residual analysis; area under curve (AUC), and so on.

We analyzed the performance of the <sup>fi</sup>rst and second detector stage, and <sup>fi</sup>nally the performance of the detector as a whole. The evaluation is based on the following measures: TPR, TNR, FPR, and FNR indicators, ROC curve, confusion matrix and reduced delay time.

## 5.1. Performance of the first detector stage

We have already stated that at the optimal threshold 90.5% of overall correct positives are achieved. This accuracy is obtained using detection with two time points. However, after the moment of detection new calls for the same element keep coming continuously and they increase the percentage of accuracy.

In the analyzed data set for a single element there were 87 calls out of the total 226 affected customers in a period of 4.8 h. In this and similar cases, the accuracy of outage detection grows to almost 100%. Yet these are exceptional cases. As we stressed before, the number of users who report the fault is small. To get an indication of how the accuracy changes over time we used a simple algorithm, which for each new call that arrives after the <sup>fi</sup>rst detection for the element (indicated by n) increases the probability of TPR detection by the formula:

![](/api/attachments/JFRV7EC5/fulltext/images/a293df637359f2f18840f247d8a3d122eb2190390e36bf32435d9d20df8fcaf6.jpg)  
Fig. 20. Timeline of true positive rate\*.

![](/api/attachments/JFRV7EC5/fulltext/images/df3e861f5d0c824f42e3c67374d626a2cd06b2f652c4b33831a5957a13bf0c43.jpg)  
Fig. 21. ROC curves.

$$
p _ {t p n} (n) = 1 - \left(1 - p _ {t p 1}\right) ^ {n}.\tag{14}
$$

The evolution of average TPR\* through time, with $\lambda _ { \sigma }$ as varying parameter, is shown in Fig. 20, where time t = 0 indicates moment of alarm occurrence. TPR\* indicates the ratio of positively detected faults and the number of outages at that time (i.e., the number of possible detections for the moment).

The data set used in calculation is a subset of $t _ { c } ^ { e }$ time intervals from the set Q related to faulty network element e which caused reported failures up to 7 h before an outcome of announced work or existence of an outage becomes known to the staff (in Table 6 indicated by index k). These seek to quantify the accuracy of the outage detection in the <sup>fi</sup>rst phase of an outage timeline.

A receiver operating characteristic curve, true positive rate vs. false positive rate, graphically illustrates the performance of our detection system, Fig. 21. The <sup>fi</sup>gure shows the different ROC curves depending on the number of points used for detection. The curve “ROC 2 points” represents the situation when only two points of detection are used and has the best overall detection performance. The curves “ROC 3 points” and “ROC 4 points” (with a larger number of points required for detection) have a lower performance because waiting for more points causes losses in detection.

Because of the small number of customers' failure reports, especially related to the network elements with a small number of connected customers, a situation appears where for 100% of outages detected on the basis of two points, for 82.8% of them a third event (report) later arrives, and for 72.2% of them a fourth event arrives too. Thus for 27.8% of outages, a fourth event (report about failure) never appears so detection in this cases is impossible; this is evident in the decline of the ROC curves, as can be seen in the right part of the diagrams in Fig. 21.

Table 9 shows the performance of different types of detectors; the parameters of TPR, TNR, FPR, FNR and AUC are compared. AUC (area under the receiver operating characteristic curve) is a common summary measurement for detector performance, maximum AUC = 1 indicates perfect differentiation, while the lowest AUC = 0.5 indicates random 50–50 classi<sup>fi</sup>cation. The Youden index (J), the maximum potential effectiveness of the detector, maximizes the vertical distance from the line of equality to the point on the ROC curve, J = max [TPR–FPR], and the parameters are given in the table with this condition. Curve “ROC curve $4 "$ has an extremely good (low) false positive rate, but all other parameters are worse. This type of detection may be required in special situations where false positive cases produce big process waste.

Detection method.

<table><tr><td>Detection method</td><td>TPR</td><td>TNR</td><td>FPR</td><td>FNR</td><td>AUC</td><td>J</td></tr><tr><td></td><td>0.9195</td><td>0.8987</td><td>0.1013</td><td>0.0805</td><td>0.9684</td><td>0.8182</td></tr><tr><td>3-point detection</td><td>0.7614</td><td>0.9897</td><td>0.0103</td><td>0.2386</td><td>0.7784</td><td>0.7512</td></tr><tr><td>4-point detection</td><td>0.6645</td><td>0.9990</td><td>0.0010</td><td>0.3355</td><td>0.6614</td><td>0.6634</td></tr></table>

Confusion matrix of stage 2, with stage 1 deactivated.

<table><tr><td rowspan="2" colspan="2"></td><td colspan="3">Predicted class</td><td rowspan="2">Total</td></tr><tr><td>DSLAM outage</td><td>Cable outage</td><td>Individual fault</td></tr><tr><td rowspan="4">Actual class</td><td>DSLAM outage</td><td>789 (74.6%)</td><td>53 (5.0%)</td><td>215 (20.3%)</td><td>1057</td></tr><tr><td>Cable outage</td><td>58 (3.0%)</td><td>1632 (83.4%)</td><td>266 (13.6%)</td><td>1956</td></tr><tr><td>Individual fault</td><td>292 (4.2%)</td><td>200 (2.9%)</td><td>6495 (93.0%)</td><td>6987</td></tr><tr><td>Total</td><td>1139</td><td>1885</td><td>6976</td><td></td></tr></table>

## 5.2. Performance of the second detector stage

If we analyze the second stage separately, without the <sup>fi</sup>rst one, which means that it binds the data set directly to its input without prior separation of individual faults, a confusion matrix appears as shown in Table 10.

We see that in this mode, the second stage gives bad results in distinguishing outages from faults affecting individual customers (individual faults). Only 74.6% of the DSLAM outages and 83.4% of the cable outages are classi<sup>fi</sup>ed correctly. On the other hand classi<sup>fi</sup>cation between the DSLAM outages and the cable outages is signi<sup>fi</sup>cantly better (5.0% and 3.0% of misclassi<sup>fi</sup>cations), and this property is a major feature of the second stage.

The <sup>fi</sup>rst stage is much better at distinguishing outages from individual cases, and if we re-connect the <sup>fi</sup>rst and the second stages, bringing to the second stage only the cases classi<sup>fi</sup>ed as outage (actual operational work), the confusion matrix turns out to be as in Table 11, and the performance improvement is visible.

Distinguishing DSLAM and cable now takes on the desired proportion, more than 90%. Although we intuitively assumed that the detector should have two levels, it is now clear why we did so. The advantage of using a two-stage detector is that it takes the best from each method and gets the optimum result in total. The confusion matrices above show results for one-point detection. For two-point detection, performance is even better.

## 5.3. Overall detector performance

Beside sensitivity and speci<sup>fi</sup>city, the timeline as a term expresses time delay from the time of the event itself to the time of its detection (detection delay). Ultimately, we would like to estimate the reduction in delay, i.e. how much earlier our detector can detect an outage than the existing surveillance system and how many events are thereby affected. Moving backward on the timeline, we sum up the number of correctly detected outages in comparison to the total number of outages that occurred, with varying detection threshold $\lambda _ { 0 } .$ Time t = 0 indicates occurrence of alarm by the existing surveillance system, Fig. 22. Unlike Fig. 20, where the denominator indicates the number of outages that can be detected at the moment, here the denominator indicates the total number of outages.

Confusion matrix of stage 2, with stage 1 activated.

<table><tr><td rowspan="2" colspan="2"></td><td colspan="3">Predicted class</td><td rowspan="2">Total</td></tr><tr><td>DSLAM outage</td><td>Cable outage</td><td>Individual fault</td></tr><tr><td rowspan="4">Actual class</td><td>DSLAM outage</td><td>863 (90.3%)</td><td>49 (5.1%)</td><td>44 (4.6%)</td><td>956</td></tr><tr><td>Cable outage</td><td>27 (1.5%)</td><td>1721 (93.9%)</td><td>85 (4.6%)</td><td>1833</td></tr><tr><td>Individual fault</td><td>7 (5.3%)</td><td>51 (14.2%)</td><td>153 (72.5%)</td><td>211</td></tr><tr><td>Total</td><td>897</td><td>1821</td><td>282</td><td></td></tr></table>

![](/api/attachments/JFRV7EC5/fulltext/images/55bf1a84708734dd18abb6d3f1b788d0ffd3a51556e23ab2f5753ee4de712dac.jpg)  
Fig. 22. Timeline of true positive rate

The <sup>fi</sup>gure shows that, with the threshold parameter of 11.5, a small number of outages can be detected up to 6 h prior to the alarm, while for the same $\lambda _ { \_ 0 } ,$ the average delay time of alarm is reduced by 2.33 h. It can be seen that reducing the detection threshold to 8.5 leads to a decrease in the number of detected cases by more than half. In doing so, of course, the other performance indicators should be monitored.

Finally, we conducted analyses of overall detector performance. The <sup>fi</sup>rst stage and the second stage are merged and the results are given for the detector as a whole. The detector can be operated in two ways. In the <sup>fi</sup>rst mode, only the <sup>fi</sup>rst stage can determine whether or not the outage exists, while the second stage classi<sup>fi</sup>es the outage. This “simple” operating mode (mode 1) of detector is shown in Fig. 23.

In some cases we have seen that the accuracy of detection can be increased if we let both stages make the decision and then choose the one with higher probability. To enable this operation mode, the detector is expanded with two new elements: summing junction which collects decisions from the two previous detection steps D1 and D2, and a new decision element D3 that chooses the more likely decision. So in this more complex operating mode (mode 2), the decision of the <sup>fi</sup>rst stage can be corrected by the second stage. Its working principle is shown in Fig. 24.

Here, in this overall detector performance analysis, de<sup>fi</sup>nitions of TPR, TNR, FPR, and FNR are slightly changed from those given in Table 8. Positives indicate both proper outage/individual fault detection and isolation of the element that is causing the problem. The two operating modes are analyzed and the results are shown in Table 12. The table also contains the results of stage 2 alone, while stage 1 alone is not analyzed there because it cannot do both functions (detection and classi<sup>fi</sup>cation), but only one (detection).

![](/api/attachments/JFRV7EC5/fulltext/images/43fb68e269097ce278e401aef2768d42da1e41a641a97796a124d6fb25e46928.jpg)  
Fig. 23. Operating mode 1.

![](/api/attachments/JFRV7EC5/fulltext/images/fa88ff34dc226a5ee132bb1663dfd7aca8647797e43f1e700478aa5e1d455d74.jpg)  
Fig. 24. Operating mode 2.

Results show that both the sensitivity and the speci<sup>fi</sup>city are at a high level (93.7% and 95.6%), whereas the process waste, FPR and FNR, are at an acceptable level of 4.4% and 6.3%.

## 6. Conclusion

In this paper we present a method for detecting network element outages that affect a group of customers. Our research refers to the real telecommunications network with the main intention of analyzing the possibility of decreasing the detection delay and improving detection accuracy by exploiting data unused so far. For a better insight into the problem we give an overview of the fault types and locations in common broadband telecommunication networks. Furthermore, we analyzed statistically the user's habits, including how quickly they report a failure related to their services and how many of them will do this. Thus we get the empirical distributions of number of reports. The data obtained showed that the customer trouble call as a variable, owing to the promptness, is suitable as a predictor.

Other predictor variables have been found among the fault and network management data. We proposed a hybrid model of detection adapted to the speci<sup>fi</sup>c environment in which the detection takes place. A two-stage detector, for outage detection and element isolation, is designed. A combination of two techniques, statistical detection technique applied in the <sup>fi</sup>rst stage and Bayesian probabilistic network for isolation in the second one, yields high detector performance. Based on a one-year (2012) data set from the T-HT broadband network, performance indicators show that the sensitivity of detection rose from 75% to 93.74%, and the average detection delay is reduced by 2.33 h.

Overall detector performance.

<table><tr><td>Detector operating mode</td><td>with λ</td><td>TPR</td><td>TNR</td><td>FPR</td><td>FNR</td></tr><tr><td>Stage 2 (alone)</td><td>-</td><td>0.8916</td><td>0.8916</td><td>0.1084</td><td>0.1084</td></tr><tr><td>Operating mode 1 (stage 1 + stage 2)</td><td>10</td><td>0.8678</td><td>0.8987</td><td>0.1013</td><td>0.1322</td></tr><tr><td>Operating mode 2 (stage 1 + stage 2)</td><td>10</td><td>0.8678</td><td>0.9769</td><td>0.0231</td><td>0.1322</td></tr><tr><td>Operating mode 2 (stage 1 + stage 2)</td><td>11</td><td>0.9374</td><td>0.9561</td><td>0.0439</td><td>0.0626</td></tr></table>

The usage of the proposed and especially designed hybrid detector provides signi<sup>fi</sup>cantly greater ef<sup>fi</sup>ciency in early outage detection. We believe that this approach is also applicable in similar practical industrial cases for cost-oriented companies. This includes large-scale technical systems like electric power or telecom systems where outages impact a large number of customers. We will continue doing research to <sup>fi</sup>nd additional prediction variables and methods to even more increase the accuracy of detection of network element outages.

## References

[1] J. Yang, L. Li, C. Yang, S. Shen, Intelligent fault management system to auto detect and handle an alarm overload, Journal of Computational Information Systems 8 (21) (2012) 9035–9046 (Article No. 43., ISSN: 1553–9105).

[2] C. Agudelo, F.M. Anglada, E.Q. Cucarella, E.G. Moreno, Integration of techniques for early fault detection and diagnosis for improving process safety: application to a <sup>fl</sup>uid catalytic cracking re<sup>fi</sup>nery process, Journal of Loss Prevention in the Process Industries 26 (4) (2013) 660–665 (ISSN: 0950–4230).

[3] M. Thottan, G. Liu, C. Ji, Anomaly Detection Approaches for Communication Networks, Computer Communications and Networks, Algorithms for Next Generation Networks, Springer-Verlag, 2010. 239–261 (ISBN 978-1-84882-764-6).

[4] M.M. Wagner, T. Fu-Chiang, J.U. Espino, V.M. Dato, D.F. Sittig, R.A. Caruana, L.F. McGinnis, D.W. Deer<sup>fi</sup>eld, M.J. Druzdzel, D.B. Fridsma, The emerging science of very early detection of disease outbreaks, Journal of Public Health Management and Practice 7 (6) (2001) (pp. 51–50, ISSN: 1078–4659)

[5] L.M. Ibrahim, Anomaly network intrusion detection system based on distributed time-delay neural network (DTDNN), Journal of Engineering Science and Technology 5 (4) (2010) 457–471 (ISSN 1823–4690).

[6] Y. Kanda, R. Fontugne, K. Fukuda, T. Sugawara, ADMIRE: anomaly detection method using entropy-based PCA with three-step sketches, Computer Communications 36 (5) (2013) 575–588 (ISSN: 0140–3664).

[7] A.B. Ashfaq, M.Q. Ali, S.A. Khayam, Accuracy improving guidelines for network anomaly detection systems, Journal in Computer Virology 7 (1) (2009) 63–81 (February 2011, 19, (ISSN: 1772–9904)).

[8] W. Xiong, H. Hu, N. Xiong, L.T. Yang, W.-C. Peng, X. Wang, Y. Qu, Anomaly secure detection methods by analyzing dynamic characteristics of the network traf<sup>fi</sup>c in cloud communications, Information Sciences, Elsevier 258 (2014) 403–415 (ISSN: 0020- 0255).

[9] J. Gao, W. Fan, D. Turaga, O. Verscheure, X. Meng, L. Su, J. Han, Consensus Extraction from Heterogeneous Detectors to Improve Performance over Network Traf<sup>fi</sup>c Anomaly Detection, Conference: IEEE INFOCOM 2011, 2011, pp. 181–185 (ISBN: 978-1-4244-9921-2).

[10] S.O. Al-Mamory, H. Zhang, Intrusion detection alarms reduction using root cause analysis and clustering, Computer Communications 32 (2) (2009) 419–430 (ISSN: 0140–3664).

[11] I. Lorenzo-Fonseca, F. Maciá-Pérez, F.J. Mora-Gimeno, R. Lau-Fernández, J.A. Gil-Martínez-Abarca, D. Marcos-Jorquera, Intrusion detection method using neural networks based on the reduction of characteristics, bio-inspired systems: computational and ambient intelligence, Lecture Notes in Computer Science 5517 (2009) 1296-1303 (ISBN: 978-3-642-02477-1)

[12] C. Ji, M. Thotton, Anomaly detection in IP networks, IEEE Transactions on Signal Processing 51 (8) (2003) 2191–2204 (ISSN: 1053-587X).

[13] A. Lakhina, M. Crovella, C. Diot, Mining anomalies using traf<sup>fi</sup>c feature distributions, SIGCOMM Proceedings of the 2005 Conference on Applications, Technologies, Architectures, and Protocols for Computer Communications, 2005, pp. 217–228 (ISBN:1-59593-009-4).

[14] B. Agarwal, N. Mittal, Hybrid approach for detection of anomaly network traf<sup>fi</sup>c using data mining techniques, 2nd International Conference on Communication, Computing & Security (ICCCS-2012), Procedia Technology, 6, 2012, pp. 996–1003 (ISBN: 978-1-4503-0464-1).

[15] J.B.D. Cabrera, C. Gutierrez, R.K. Mehra, Ensemble methods for anomaly detection and distributed intrusion detection in mobile ad-hoc networks, special issue on applications of ensemble methods Information Fusion 9 (1) (2008) 96–119 (ISSN: 1566–2535).

[16] A. Patcha, J.-M. Park, An overview of anomaly detection techniques: existing solutions and latest technological trends, Computer Networks 51 (12) (2007) 3448-3470 (ISSN:1389-1286).

[17] A.J. Oliner, A.V. Kulkarni, A. Aiken, Community epidemic detection using time-correlated anomalies, recent advances in intrusion detection, Lecture Notes in Computer Science 6307 (2010) 360–381 (ISBN: 978-3-642-15511-6).

[18] N.A. Adnana, I. Izadi, T. Chen, On expected detection delays for alarm systems with deadbands and delav-timers, Journal of Process Control 21 (9) (2011) 1318-1331 (ISSN: 0959–1524).

[19] J.M. Estevez-Tapiador, P. Garcia-Teodoro, J.E. Diaz-Verdejo, Anomaly detection methods in wired networks: a survey and taxonomy, Computer Communications 27 (16) (2004) 1569–1584 (ISSN: 0140–3664).

[20] B.B. Gupta, M. Misra, R.C. Joshi, An ISP level solution to combat DDoS attacks using combined statistical based approach, Journal of Information Assurance and Securit 3 (2) (2008) 102–110 (ISSN 1554–1010).

[21] P. Garcia-Teodoro, J. Diaz-Verdejo, G. Macia-Fernandez, E. Vazquez, Anomaly-based network intrusion detection: techniques, systems and challenges, Computers & Security 28 (1–2) (2009) 18–28 (ISSN: 0167–4048).

[22] J. Koshal, M. Bag, Cascading of C4.5 decision tree and support vector machine for rule based intrusion detection system, International Journal of Computer Network and Information Security 4 (2012) 8–20 (ISSN: 2074–9090).

[23] J. Wanga, T. Chen. An online method for detection and reduction of chattering alarms due to oscillation, Computers and Chemical Engineering (2013), Vol. 54, pp. 140–150, (ISSN: 0098–1354)

[24] Y. Zhao, S. Wang, F. Xiao, Pattern recognition-based chillers fault detection method using Support Vector Data Description (SVDD), Applied Energy, Elsevier 112 (2013) 1041–1048.

[25] A. Tosuna, A. Benera, B. Turhanb, T. Menzies. Practical considerations in deploying statistical methods for defect prediction: A case study within the Turkish telecommunications industry, Information and Software Technology (2010), Vol. 52, Issue 11, pp. 1242–1257, (ISSN: 0950–5849)

[26] S. Selvakani, R.S. Rajesh, Escalate intrusion detection using GA–NN, International Journal of Open Problems in Computer Science and Mathematics 2 (2) (2009) (ISSN: 1998–6262).

[27] Z. Miller, W. Hu, Data stream subspace clustering for anomalous network packet detection, Journal of Information Security 3 (3) (2012) 215–223 (ISSN: 2153–1242).

[28] S. Amershi, B. Lee, A. Kapoor, R. Mahajan, B. Christian, CueT: human-guided fast and accurate network alarm triage, Proceedings of the Conference on Human Factors in Computing Systems (SIGCHI2011), 2011, pp. 157–166 (ISBN: 978-1-4503-0228-9).

[29] J. Yang, L. Han, Y. Xie, The research on real-time alarm algorithm in network traf<sup>fi</sup>c monitoring system, Proceedings of the Broadband Network and Multimedia Technology (IC-BNMT2010), 2010, pp. 243–246 (ISBN: 978-1-4244-6769-3).

[30] Y. Xiang, K. Li, W. Zhou, Low-rate DDoS attacks detection and traceback by using new information metrics, IEEE Transactions on Information Forensics and Security 6 (2) (2011) 426–437 (ISSN: 1556–6013).

[31] R. Perdisci, G. Giacinto, F. Roli, Alarm clustering for intrusion detection systems in computer networks, Engineering Applications of Arti<sup>fi</sup>cial Intelligence 19 (4) (2006) 429–438 (ISSN: 0952–1976).

[32] C.-Y. Chiu, Y.-J. Lee, C.-C. Chang, W.-Y. Luo, H.-C. Huang, Semi-supervised learning for false alarm reduction, advances in data mining, applications and theoretical aspects, Lecture Notes in Computer Science 6171 (2010) 595–605 (ISBN: 978-3- 642-14400-4).

[33] S.S. Kandeeban, R.S. Rajesh, Integrated intrusion detection system using soft computing, International Journal of Network Security 10 (2) (2010) 87–92 (ISSN: 1816–3548).

[34] Z. Muda, W. Yassin, M.N. Sulaiman, N.I. Udzir, A K-means and naive Bayes learning approach for better intrusion detection, Information Technology Journal 10 (3) (2011) 648–655 (ISSN: 1812–5638).

[35] L. Liu Mengfei, Application of Alarm Correlation Method in EPON Networks, Science paper Online, Electrics, Communication and Autocontrol Technologyweb source: http://www.paper.edu.cn/2010

[36] R. Costa, N. Cachulo, P. Cortez, An intelligent alarm management system for large-scale telecommunication companies, Proceedings of the 14th Portuguese Conference on Arti<sup>fi</sup>cial Intelligence (EPIA09): Progress in Arti<sup>fi</sup>cial Intelligence, 2009, pp. 386–399 (ISBN: 978-3-642-04685-8).

[37] S.H. Oh, W.S. Lee, An anomaly intrusion detection method by clustering normal user behavior, Computers & Security 22 (7) (2003) 596–612 (ISSN: 0167–4048).

[38] M.I. Bonab, S.M. Noorhosseini, F. Akbari, Dynamic alarm correlation based on cellular learning automata in telecommunication networks, International Journal of Computer Science and Network Security (IICSNS09) 9 (12) (2009) (ISSN: 1738-7906).

[39] W.-G. Tian, L.-Z. Gao, C.-I. Sun, M.-Y. Duan, E.-Y. Zhang, A method for anomaly detection of user behaviors based on machine learning, The Journal of China Universities of Posts and Telecommunications 13 (2) (2006) 61–65 (ISSN: 1005–8885).

[40] P. Barford, J. Kline, D. Plonka, A. Ron, A signal analysis of network traf<sup>fi</sup>c anomalies, Proceedings of the 2nd ACM SIGCOMM Workshop on Internet Measurement (IMW02), 2002, pp. 71–82 (ISBN:1-58113-603-X).

[41] N. Muthumani, A.S. Thanamani, A survey on failure prediction methods, International Journal of Engineering Science and Technology (IJEST2011) 3 (2) (2011) 1400–1404 (ISSN: 0975–5462).

[42] B. Cheung, G. Kumar, S.A. Rao, Statistical algorithms in fault detection and prediction: toward a healthier network, Proceedings of Bell Labs Technical Journal, vol. 9, issue 4, 2005, pp. 171–185 (ISSN: 1538–7305).

[43] N. Muthumani, A.S. Thanamani, Optimizing hidden Markov model for failure prediction — comparison of Gaine's optimization and minimum message length estimator, International Journal on Computer Science & Engineering 3 (2) (2011) 892–898 (ISSN: 0975–3397).

[44] Ž. Deljac, M. Kunštić, B. Spahija, A comparison of traditional forecasting methods for short-term and long-term prediction of faults in the broadband networks, MIPRO 2011, Proceeding of 34th International Convention on Information and Communication Technology, Electronics and Microelectronics — CTI, 2011, pp. 517–523 (ISBN: 978-953-233-067-0).

[45] C. Drummond, R.C. Holte, Explicitly representing expected cost: an alternative to ROC representation, KDD 2000, Proceedings of the Sixth ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 2000, pp. 198–207 (ISBN: 1-58113-233-6).

[46] F. Provost, T. Fawcett, Robust classi<sup>fi</sup>cation for imprecise environments, Journal Machine Learning 42 (3) (2001) 203–231 (ISSN: 0885–6125)

[47] J. Chen, H. He, G. Williams, H. Jin, Temporal sequence associations for rare events, advances in knowledge discovery and data mining, Lecture Notes in Computer Science 3056 (2010) 235–239 (ISBN: 978-3-540-22064-0).

[48] T. Fawcett, F. Provost, Activity monitoring: noticing interesting changes in behavior, KDD 1999, Proceedings of the Fifth ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 1999, pp. 53–62 (ISBN: 1-58113-143-7).

[49] Y. Hong, W.Q. Meeker, Field-failure predictions based on failure-time data with dynamic covariate information, Technometrics 55 (2) (2011) 135–149 (ISSN: 0040–1706).

[50] A. Oniesko, P. Lucas, M.J. Druzdzel, Comparison of rule-based and Bayesian network approaches in medical diagnostic systems, arti<sup>fi</sup>cial intelligence in medicine, Lecture Notes in Computer Science 2101 (2001) 283–292 (ISBN: 978-3-540-42294-5).

[51] H. Wu, W.Q. Meeker, Early detection of reliability problems using information from warranty databases, Tehnometrics 44 (2) (2002) 120–133 (ISSN: 0040–1706).

[52] X. Fu, W. Yu, D. Cheng, X. Tan, K. Streef, S. Graham, On recognizing virtual honeypots and countermeasures, DASC 2006, Proceedings of the 2nd IEEE International Symposium on Dependable, Autonomic and Secure Computing, 2006, pp. 211–218 (ISBN: 0-7695-2539-3).

[53] A. Mohammadi, M.R. Taban, J. Abouei, H. Torabi, Cooperative spectrum sensing against noise uncertainty using Neyman–Pearson lemma on fuzzy hypothesis test, Applied Soft Computing 13 (7) (2013) 3307–3313 (ISSN: 1568–4946).

[54] H. Shekhar, R. Polikar, P. Ramuhalli, X. Liu, M. Das, L. Udpa, S.S. Udpa, Dynamic thresholding for automated analysis of bobbin probe eddy current data, International Journal of Applied Electromagnetics and Mechanics 15 (2002) 39–46 (ISSN: 1383–5416).

[55] Y. Hu, X. Zhang, E.W.T. Ngai, R. Cai, M. Liu, Software project risk analysis using Bayesian networks with causality constraints, Decision Support Systems 56 (2013) 439–499 (ISSN 0167–9236)

[56] V.S. Sheng, C.X. Ling, Thresholding for making classi<sup>fi</sup>ers cost-sensitive, Proc. of the 21st National Conference on Arti<sup>fi</sup>cial Intelligence, vol. 1, AAAI, 2006, pp. 476–481 (ISBN: 978-1-57735-281-5).

[57] C. Elkan, The foundations of cost-sensitive learning, Proc. of the 17th International Joint Conference on Arti<sup>fi</sup>cial Intelligence, vol. 2, IJCAI, 2001, pp. 973–978 (ISBN: 978-1-558-60812-2).

[58] J. Neyman, E.S. Pearson, On the problem of the most ef<sup>fi</sup>cient tests of statistical hypotheses, Philosophical Transactions of the Royal Society of London. Series A 231 (1933) 289–337.

[59] G. Casella, R. Berger, Statistical Inference. Duxbury, Paci<sup>fi</sup>c Grove, 2002. (ISBN: 0-534-24312-6).

[60] C. Scott, R. Nowak, A Neyman–Pearson approach to statistical learning, Journal of IEEE Transactions on Information Theory 51 (11) (2005) (ISSN: 0018–9448).

![](/api/attachments/JFRV7EC5/fulltext/images/f21aaab0f9471d731f71f848b2d20e6bb2c8013bdc8d8fd722a518bded4597a9.jpg)  
Željko Deljac has been working as a Senior Service Management and Quality Assurance Expert at the T-Croatian Telecom. He is currently pursuing his PhD in the department of Telecommunications at the Faculty of electrical engineering and computing, University of Zagreb. His doctoral research focuses on the development and application of data mining techniques in fault management and failure prediction. His research interests include research on usage of arti<sup>fi</sup>cial intelli gence in network and services management.

![](/api/attachments/JFRV7EC5/fulltext/images/7de5f500ee0f97ee51a33b086edeb3ab8230be55f29668b7d3addd01e6dd66bf.jpg)

![](/api/attachments/JFRV7EC5/fulltext/images/c379901175f5c6a0a776eb2490a9f4cb16c4f486bb0f9359da2a3241008d2dad.jpg)

Mirko Randić is an Assistant Professor at the Faculty of Electrical Engineering and Computing, University of Zagreb where he received his Ph.D. His research interests include systems, networks and service management, software systems modeling and service performance modeling. His work has been published in several peer reviewed journals, such as Software, practice & experience, Journal for Control, Measurement, Electronics, Computing and Communications Journal of Computing and Information Technology, and other journals and book chapters.

Gordan Krčelić received his B.S. in Mechanical Engineering from the Faculty of Mechanical Engineering and Naval Architecture, University of Zagreb and M.S. in Electrical Engineering from the Faculty of Electrical Engineering and Computing, University of Zagreb. He is working as Quality Assurance Expert at the T-Croatian Telecom. He is a certi<sup>fi</sup>ed Project Management Professional and Six Sigma Black Belt. His projects were mostly process improvement focused using Six Sigma + LEAN methodology. He started his postgraduate doctoral study at the Faculty of Organization and Informatics, University of Zagreb. His research interests include processes management, service management and high-level planning.
