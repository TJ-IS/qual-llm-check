---
otero_id: 6586
otero_key: "UYZZNAPU"
title: "Improving patient flow in a hospital through dynamic allocation of cardiac diagnostic testing time slots"
authors: "Robert W. Day; Matthew D. Dean; Robert Garfinkel; Steven Thompson"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.05.007"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Improving patient <sup>fl</sup>ow in a hospital through dynamic allocation of cardiac diagnostic testing time slots

Robert W. Day <sup>a,1</sup>, Matthew D. Dean <sup>b,</sup>⁎, Robert Garfinkel <sup>a</sup>, Steven Thompson <sup>c</sup>

<sup>a</sup> School of Business, University of Connecticut, 2100 Hillside Road, Storrs, CT 06269, United States

<sup>b</sup> College of Business Administration, University of New Orleans, 2000 Lakeshore Drive, New Orleans, LA 70148, United States

<sup>c</sup> Robins School of Business, University of Richmond, 28 Westhampton Way, Richmond, VA 23173, United States

## a r t i c l e i n f o

Article history: Received 2 July 2009 Received in revised form 4 May 2010 Accepted 13 May 2010 Available online 21 May 2010

Keywords: Health care Patient flow Network <sup>fl</sup>ow Mathematical modeling

## a b s t r a c t

A cardiac diagnostic testing center (CDTC) makes real-time scheduling decisions that impact the use of its resources and the availability of telemetry-equipped beds within a hospital. Both inpatients and outpatients are frequent users of CDTC resources, and physicians prescribe one of several single-phase or multiple-phase test protocols. This complex online decision-making environment is modeled as a <sup>fi</sup>nite-horizon, discretetime Markov decision process (MDP), but the growth of the state space motivates the introduction of a fast heuristic for real-time decision support. We therefore introduce a dynamic network scheduling tool which is both more <sup>fl</sup>exible and more robust, making it applicable to the various con<sup>fi</sup>gurations that may be found in practically any CDTC. We evaluate this new method computationally using simulation, comparing it to both an MDP model for small instances, and to the existing operational practice at our partner hospital for more realistic sized problems.

© 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

Many hospitals in the United States provide a wide range of inpatient and outpatient health care services to the communities they serve. Outpatient services tend to be more lucrative because they require less infrastructural investment and have lower ancillary support costs. The pro<sup>fi</sup>ts obtained from outpatient services are crucial, because they enable the hospital to offset possible losses on certain inpatient services and invest in new medical technologies. Thus, the units that provide outpatient services are often treated as pro<sup>fi</sup>t centers, each of which strives to maximize revenue. Inpatient services, with the exception of some surgical services, are typically not highly lucrative. For these services, the hospital typically receives a lump sum payment determined by the patient's classi<sup>fi</sup>cation to a particular Diagnostic Related Group (DRG) at the time of admission. However inpatient care requires a great deal of infrastructure and support personnel to be constantly in place. This results in very high <sup>fi</sup>xed costs, so that hospital units that provide inpatient services must operate at high levels of utilization in order to break even. The problem of optimally balancing the levels of inpatient versus outpatient services is complicated by the fact that the demand for inpatient services is variable. The need to maintain high levels of utilization and meet uncertain demand makes the management of inpatient services challenging.

While low demand that results in poor utilization is a concern, high demand and the associated congestion can also present a signi<sup>fi</sup>cant problem. For example, if a given inpatient unit in a hospital does not have enough beds to accommodate all patients in need, then some of them will be “held” in the emergency department (ED) until a bed becomes available. When the ED becomes too crowded, it can no longer function effectively. In the extreme case the hospital may have to deny admission to potential inpatients. Often this takes the form of diversion of ambulances to other hospitals, since this is a common manner of inpatient arrival. The hospital then loses the revenue that would have resulted from treating those patients that were diverted, and its reputation as a reliable provider is also damaged.

Some hospital facilities are commonly termed “outpatient units”, although that is not entirely accurate, as these units often provide services to inpatients as well. One typical example is the cardiac diagnostic testing center (CDTC) at Windham Community Memorial Hospital (WCMH) in Willimantic, CT. Like the CDTC at most hospitals, its primary role is to provide a range of cardiac screening tests to outpatients. These screenings are used for preventative care as opposed to the diagnosis of urgent, potentially life threatening conditions. Patients are typically referred to the CDTC by their physicians, and schedule appointments for prescribed tests, well in advance.

The other role of the CDTC is to perform cardiac screenings on inpatients. For them, the stress test is generally the last test prior to discharge because it is the most aggressive in terms of how much strain is placed on the patient's heart. When a patient is admitted with chest pain a number of tests are done that do not place any strain on the heart (blood tests, EKGs, etc.). The purpose of those tests is to <sup>fi</sup>nd evidence that the heart muscle is not receiving enough blood <sup>fl</sup>ow, causing the patient to experience chest pain. When these tests are negative, the <sup>fi</sup>nal test is a stress test to push the heart and see if any symptoms arise. If the heart behaves normally under exercise conditions, then it is safe to send the patient home. Only if symptoms appear during this <sup>fi</sup>nal screening, which in practice is uncommon, must the patient remain hospitalized. At WCMH in particular, even if a stress test is not normal, patients still leave the hospital. Rather than going home they are typically transferred to a larger facility that is able to perform complex cardiovascular procedures such as angioplasty, coronary artery stenting, coronary artery by-pass grafting, etc.

Providing screenings to inpatients presents a challenge because, unlike those for outpatients, the requests for screening often come with little or no notice. If at the time of the request there is no immediate opening, a scheduling decision must be made. In essence, this involves choosing which among various classes of patients, some of whom are inpatients and others outpatients, to service at a given time period. A serious area of concern observed at WCMH prior to our study was that some outpatients do indeed balk, presumably choosing to be screened elsewhere, if they are rescheduled from their prearranged time slot. Further, in many cases physicians are af<sup>fi</sup>liated with multiple hospitals in a given area, and as a result, hospitals face competition from other hospitals when the physicians feel that one hospital is providing better service. Hospitals can also face competition from the physicians that are af<sup>fi</sup>liated with the hospital. For example, one of the cardiologists af<sup>fi</sup>liated with WCMH made the decision a few years prior to our study to stop working with the CDTC and open her own screening clinic. It follows that, considering only the pro<sup>fi</sup>t to the CDTC, part of an intuitively dominant decision rule would be to give priority to outpatients. Thus an ad hoc strategy used by many hospitals, including WCMH, is to give priority to outpatients except in some time slots that are reserved for inpatients.

On the other hand, the CDTC can play a key role in maintaining patient <sup>fl</sup>ow and helping the hospital avoid the negative consequences of an overcrowded ED. By providing an inpatient screening the CDTC effectively “opens a bed” because that patient can now almost always be discharged, either to home or to another hospital, after its completion. This provides the hospital with the ability to accommodate an additional patient, should one arrive. Note that any patient whose screening is delayed must also be assigned a subsequent time slot. Thus, because there are two potential classes of costs, we choose to follow many authors (e.g. [8]) and optimize a composite “social welfare” function of the pro<sup>fi</sup>ts to the hospital from providing patient services, costs to the hospital of lost opportunity, and “inconvenience” costs to the patients of delays in treatment. It should be stressed that the resulting algorithm is a decision support system, so that its users can certainly input any costs that they deem appropriate, including the possibility of not considering patient inconvenience costs by setting those values to zero.

The scheduling problem is complicated by the fact that there are different types of cardiac screenings. Some have multiple phases, some span a two-day period, and the phases in a multiple-phase test must be done in lockstep fashion over time. That is, once a screening begins, or resumes on its second day, subsequent steps in that day must be done in the immediately following time periods. The problem can be modeled as a <sup>fi</sup>nite-horizon, discrete-time Markov decision process (MDP) as described in Appendix A. However, one quickly <sup>fi</sup>nds that the computational methods based on this model tend to be impractically slow and memory intensive when compared to the pace of the actual decision making environment, motivating the introduction of a computationally tractable scheduling tool.

Therefore, we introduce a decision support system based on a Multi-commodity Flow Snapshot Model (MFSM), grounded in the theory of dynamic network optimization. This approach is both <sup>fl</sup>exible and robust, making it applicable to the various con<sup>fi</sup>gurations of patient and test-protocol types that may be found in practically any CDTC. Based on historical data from WCMH, our experiments indicate that the MFSM approach results in drastically improved quality of service for inpatients, with little or no reduction in the quality of service to outpatients relative to the existing policy at WCMH. The bottom line of the hospital will also show a healthy improvement. Our methods provide both an online decision support tool, and a framework by which simulation results may be used as guidance for more pro<sup>fi</sup>table long-term capacity planning.

The rest of the paper is organized as follows. The relevant related literature is reviewed in Section 2 and in Section 3 the problem is formally de<sup>fi</sup>ned. In Section 4 we provide an overview of the MDP approach with details in Appendix A. The dynamic network model is described in Section 5. In Section 6 we use simulation and real data from WCMH to evaluate the results of the network model relative to the MDP and to the prior decision making policy utilized by WCMH. Conclusions, with managerial implications and directions for future research, are addressed in Section 7.

## 2. Literature review

Ef<sup>fi</sup>ciency of health care operations has been widely studied in the management science literature, and detailed histories of the application of operations research models to problems in the health care industry can be found in [6] and [3]. A number of techniques have been employed to help improve patient <sup>fl</sup>ow including dynamic allocation of patients to the inpatient units [17], bedside registration [14], and applications of simulation and queueing theory to identify and remove patient <sup>fl</sup>ow bottlenecks [12].

The problem of allocating CDTC time slots shares some traits with a number of stochastic control applications. Allocating service capacity over time among several competing customer classes has been studied in various settings outside of health care, including hotel management [2,11], car rentals [4,7], and airline yield management [1]. These articles fall into the category of revenue management. One distinguishing feature between revenue management and our diagnostic allocation problem is that in many instances of revenue management, customers can choose which “fare class” they belong to, whereas in our setting, the screening class is determined by a physician.

The more closely related problem of appointment scheduling and real-time capacity allocation in an MRI setting was addressed by [8]. The use of approximate dynamic programming to solve the problem of dynamically allocating diagnostic imaging resources to multiple patient priority classes, in order to achieve targeted wait times was investigated in [15]. While [15] and [8] consider allocation of time slots among multiple patient classes, the problem addressed here is different for two reasons. First, we expand the state space de<sup>fi</sup>nition to include the number of available inpatient beds for different services. This increases the size and complexity of the problem, but thereby more accurately captures the costs that CDTC decisions impose on the rest of the hospital. Second, we consider time slot allocation decisions for both multiple-phase and single-phase tests. The distinction is that a multiple-phase test involves performing a set of procedures at separate times. To the best of our knowledge a setting involving a mixture of single- and multiple-phase tests with a mixture of patient classes in the operations research health care literature, has not been investigated prior to this study. Our proposed approach to solve the problem uses a dynamic network <sup>fl</sup>ow model. A recent example utilizing dynamic network models to schedule and dispatch concrete trucks was described by [5].

The opportunities and challenges of incorporating location and medical information obtained via wireless monitoring into health care decision-making were discussed in [16] and [9] studied the factors that impact the willingness of patient care providers to utilize technology in decision-making. [13] developed an RFID network design methodology to improve medical device allocation in the context of patients that are transferred from one area of the hospital to another. They model the network design problem as a maximal covering location problem and introduce a criticality index metric to provide hospital decision makers with information regarding whether to expand the inventory of speci<sup>fi</sup>c medical devices. Future research could examine augmenting the system proposed here to incorporate RFID tracking to create an improved system integrating the bene<sup>fi</sup>ts of both approaches. Such an integrated system could enable hospitals to include medical device availability inthe scheduling decision-making process. More closely related to our research, [10] addressed the problem of high level system design in the context of staff and patient scheduling in an ambulatory care clinic. They develop a method for reconciling the information needs and decision rules that exist at the departmental level with those of the hospital, similar to the approach we take here, in which decisions at the department level take into consideration census information across the whole hospital.

## 3. Problem setting

Cardiologists can typically choose from among a number of different types of screenings for each patient. For example, at WCMH there were three options. All consist of one or more of the stages listed below. Each of the three stages takes about 1 h to perform. The stages within a given day must be performed in consecutive periods, while two-day screenings must be completed in successive days. The stages are:

Exercise–monitor: The patient is connected to an electrocardiograph machine and the heart is monitored while the patient exercises.

Rest–inject–image: The patient rests and is then injected with a radio-opaque isotope, and a special camera called a gamma camera is then used to take images of blood <sup>fl</sup>ow through the heart.

Inject–image: The patient is injected with the isotope and the camera takes images of blood <sup>fl</sup>ow through the heart.

Then the three screening types are as follows:

One day regular: Exercise–monitor.

One-day nuclear: Rest–inject–image; exercise–monitor; injectimage.

Two-day nuclear: Day 1 = Exercise–monitor; inject–image. Day 2 = rest–inject–image.

Exercise or “stress” tests are performed in a different room than imaging. After the stress test stage of a one- or two-day nuclear screening, once clean-up is completed, another patient can be brought into the stress room. During each stage of the screening the patient is observed one-on-one by a licensed clinician. Thus the only limiting physical resources are the number of stress rooms and the number of cameras. Because each of the screening types described above can be performed on inpatients and outpatients, there are six distinct patient classes as shown in Table 1. They are: inpatient regular (IR); outpatient regular (OR); inpatient one-day nuclear (I1N); outpatient one-day nuclear (O1N); inpatient two-day nuclear (I2N); outpatient two-day nuclear (O2N)). Table 1 indicates the sequence of resources that are required for each screening on each day. ‘C’ and ‘S’ indicate stages that require a camera or a stress room respectively.

Table 1  
The screening classes at WCMH.

<table><tr><td>Class</td><td>Day 1</td><td>Day 2</td></tr><tr><td>IR, OR</td><td>S</td><td>NA</td></tr><tr><td>I1N, O1N</td><td>C-S-C</td><td>NA</td></tr><tr><td>I2N, O2N</td><td>S-C</td><td>C</td></tr></table>

Initial outpatient reservations are made in advance through direct consultation with the physician's of<sup>fi</sup>ce, the patient, and the scheduler at the CDTC. Appointments will be made only if, at the time of scheduling, there are projected to be suf<sup>fi</sup>cient resources to handle the various steps of the screening. Therefore initial scheduling of outpatients is considered to be exogenous to the decision process. If it is determined, before an outpatient arrives at the hospital, that the reservation cannot be honored, the patient or doctor's of<sup>fi</sup>ce will be noti<sup>fi</sup>ed and the appointment rescheduled. On the other hand, since inpatients are already in the hospital there is no need for external communication. They can simply be rescheduled to a later period in the same day or perhaps to the following day. Of course these decisions come with costs (see Section 4.2). More signi<sup>fi</sup>cantly it is imperative that the decision model itself is able to verify that the rescheduled beginning time (or resuming time in the case of two-day nuclear screenings) is resource feasible.

## 3.1. The state of the hospital

Since the primary motivation to prioritize inpatient screenings is to avoid patient <sup>fl</sup>ow bottlenecks, the evolving state of the hospital in terms of the number of available beds on the specialized inpatient units must be considered. A hospital is capable of providing a number of different patient care services, e.g. cardiology, obstetrics, critical care, neurosurgery, etc. A small community hospital may provide 15–20 different services, while an academic medical center could easily provide more than 100 services. The inpatient units are specialized in a manner that enables them to provide care to patients in need of one or more of these services. A neonatal intensive care unit is an example of a unit specialized to support a single service. In contrast, a general medical/surgical <sup>fl</sup>oor can support several services. Often more than one unit can support a given service. For example, in a large hospital there are typically several units that can provide care to a patient admitted with hyperglycemia, a potentially deadly complication of diabetes.

Some of these services, e.g. cardiology, often require the patient to be on a telemetry monitor in order to continuously monitor heart rhythm and rate. In this problem setting, inpatients in need of cardiac screening directly impact the availability of beds that are capable of supporting services that require telemetry monitoring. However, since the inpatient units can potentially support more than one service, the decision to accept an inpatient request for a screening can impact the <sup>fl</sup>ow of patients in need of services that do not require telemetry. For example, consider an inpatient unit that can provide services to cardiology patients (who require telemetry monitoring) and general medical patients (who do not require telemetry and can use any type of bed). Assume the unit is full, but has one patient who can be discharged after a cardiac screening. Once that patient is discharged, the hospital now has the capacity to admit another cardiology patient or another medical patient.

The state of the hospital is therefore de<sup>fi</sup>ned as the number of beds available to provide care to patients in need of each service. The state evolves over time as a function of random arrivals and the exogenous decisions of bed managers and physicians regarding which <sup>fl</sup>oors to assign to new patients, random departures (patients discharged from the hospital), and decisions made by the CDTC. The probability distributions of the random arrival and departure of patients needing these different services are easily estimated from historical data.

## 4. An overview of the Markov decision process

The problem can be modeled as a <sup>fi</sup>nite-horizon, discrete-time, Markov decision process (MDP). Here we give an overview of the basic decisions, rewards, and costs since they are needed in order to motivate the snapshot model of the following section. Further details of the MDP can be found in Appendix A. Time is partitioned into <sup>fi</sup>xedlength one-hour time intervals. At the beginning of a period, the state of the process is observed and a decision is made. Immediate costs and rewards are incurred based on the state and the decision. As indicated earlier we follow [8] in maximizing social welfare. That is, the function to be maximized adds the hospital's expected pro<sup>fi</sup>t and subtracts the inconvenience costs to the patients who are rescheduled.

## 4.1. Decisions

The basic decisions to be made for each time period within a given day are:

The number of each type of screening (IR, OR, I1N, O1N, I2N, and O2N at WCMH) to initiate;

The number of each type of two-day screening (I2N and O2N at WCMH) to resume on their second day;

The rescheduled day and time of each type of screening that was scheduled to begin but was not initiated;

The rescheduled time in the current day to resume each type of two-day screening that was scheduled to resume but was not resumed.

## 4.2. Rewards to the hospital

Deterministic rewards to the CDTC are obtained when an outpatient's screening is realized. These can be monetized based on the fee structure for such screenings. Positive expected rewards accrue to the hospital based on the DRGs and their corresponding fee structures of arriving inpatients. On the other hand negative expected rewards to the CDTC are based on the loss of revenue from outpatients who balk after being rescheduled.

## 4.3. Costs to patients

Both inpatients and outpatients incur inconvenience costs if their screenings are delayed. How to monetize these is a subtle and <sup>fl</sup>exible decision for the user of the system. In our simulations we have followed [8] and based these on the expected hourly wages of a typical patient.

## 5. A DSS based on a Multi-commodity Flow Snapshot Model (MFSM)

For any realistic problem instance, the MDP described above is too large to solve in reasonable time (see Appendix A). In particular, WCMH wanted to make allocation decisions in an online context in less than 10 min. Therefore, we introduce a model based on a current “snapshot” of the state of the hospital, prior to each decision point with the stochastic elements represented by the expected pro<sup>fi</sup>ts (positive or negative) associated with the various decisions. The problem is modeled via a dynamic maximum pro<sup>fi</sup>t multi-commodity <sup>fl</sup>ow formulation. This approach is both <sup>fl</sup>exible and robust, making it applicable to the various con<sup>fi</sup>gurations of patient and test-protocol types that may be found in practically any CDTC or similar center. The snapshot includes the number of available beds on the inpatient units and in the ED. This information is combined with the current CDTC schedule, any outstanding or new requests for cardiac screenings, and patients currently in the screening process.

An integer multi-commodity time-space network <sup>fl</sup>ow model (MFSM) is then constructed, where each test request is a commodity. Each node in the network represents a point in time and a physical location. An arc between two nodes represents a possible step in the process <sup>fl</sup>ow for that particular test request. Pro<sup>fi</sup>ts are associated only with arcs that represent waiting (i.e., the decision to reschedule a patient) and arcs that represent the initiation or resumption of an outpatient screening. The positive pro<sup>fi</sup>ts associated with initiating outpatient tests, and the negative pro<sup>fi</sup>ts associated with making patients wait, are deterministic. In contrast, the negative pro<sup>fi</sup>ts associated with the opportunity cost of not testing inpatients, are based on expectations of new inpatient arrivals in the future. Similarly, for outpatients, they are based on the expected loss from balking.

The stochastic aspect of MFSM is captured by dynamically calculating the pro<sup>fi</sup>ts on the arcs. Since the underlying structure of the network does not change dramatically between time periods, updating the network is more ef<sup>fi</sup>cient than rebuilding it at each decision epoch. Therefore at each decision point the network is updated using the new information (i.e., nodes and arcs are pruned or added and arc pro<sup>fi</sup>ts are adjusted accordingly).

## 5.1. Notation

The following notation is used in the formulation of MFSM:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
s the source node.
t the sink (terminal) node.
i, j node indices.
k test index.
K the set of test requests.
V the node set.
A the arc set.
 $V^{C}$  the set of camera nodes.
 $V^{S}$  the set of stress nodes.
 $V^{W}$  the set of “waiting” nodes.
 $V^{+}(i)=\{j:(i,j)\in A\}$ .
 $V^{-}(i)=\{j:(j,i)\in A\}$ .
 $A_{i}^{C+}$  the set of arcs leaving camera node i, i.e., $\{(i,j)|i\in V^{C},j\in V^{+}(i)\}$ .
 $A_{i}^{S+}$  the set of arcs leaving stress node i, i.e., $\{(i,j)|i\in V^{S},j\in V^{+}(i)\}$ .
 $A_{i}^{W+}$  the set of arcs leaving wait node i, i.e., $\{(i,j)|i\in V^{W},j\in V^{+}(i)\}$ .
C the number of available imaging cameras.
S the number of available stress rooms.
 $z_{ijk}$  the flow over the arc  $(i,j)$  for test k.
 $v_{ijk}$  the expected profit obtained by sending a single unit of flow over the arc  $(i,j)$  for test k.
</div>

Deterministic positive pro<sup>fi</sup>t comes from the arcs associated with screening an outpatient. That is, arcs (i, j) where $i \in V ^ { \mathsf { W } }$ and $j \in$ $( V ^ { \mathsf { C } } \cup V ^ { \mathsf { S } } )$ <sup>2 2</sup>. On the other hand, negative pro<sup>fi</sup>t is assigned to the (rescheduling) arcs $( i , j )$ where $i \in \{ s \} \cup { \hat { V } } ^ { \tilde { W } }$ , and $j \in V ^ { \mathrm { w } }$ in a future <sup>2 2</sup>period. Since the speci<sup>fi</sup>c derivation of these costs relies on the notation of 8, we have placed it immediately after in Appendix B.

## 5.2. Formulation

Fig. 1 illustrates the multi-commodity <sup>fl</sup>ow formulation. It shows a simple example consisting of a single day, three-time slot scenario, and two patient classes (I1N and OR). A multi-commodity timespace network is constructed for two test requests from the OR patient class (Test 1 and Test 3) and a single test request for a patient of class I1N (Test 2). Each node in the network represents a point in space and time, e.g. the nodes labeled 2, 4, and 6 represent the stress test phase of the screening at a particular time. The arc (1, 2) represents the possible decision to begin Test 1 during the <sup>fi</sup>rst time slot. The arc (1, 3) represents the alternate decision of rescheduling initiation of Test 1 to the next time slot, etc.

![](/api/attachments/UYZZNAPU/fulltext/images/8de48d49ae358a5ea1f383f2957c646aba61d6688f7a2af8d4e5dba8e9a9b83e.jpg)  
Fig. 1. An example network representation of a one-day, three-time-slot problem instance. For this miniature and illustrative example, all feasible arcs are shown, indicating the possible sequences of arriving, waiting, and being tested that three patients may experience.

The formulation of the multi-commodity network <sup>fl</sup>ow problem is

$$
\max \sum_ {(i, j) \in A} \sum_ {k \in K} v _ {i j k} z _ {i j k},\tag{1}
$$

s.t.

$$
\sum_ {j \in V ^ {+} (i)} z _ {i j k} - \sum_ {j \in V ^ {-} (i)} z _ {j i k} = 1, \text {   for   } i = s, k \in K,\tag{2}
$$

$$
\sum_ {j \in V ^ {+} (i)} z _ {i j k} - \sum_ {j \in V ^ {-} (i)} z _ {j i k} = 0, \text {   for   all   } i \in V \backslash \{s, t \}, k \in K,\tag{3}
$$

$$
\sum_ {j \in V ^ {+} (i)} z _ {i j k} - \sum_ {j \in V ^ {-} (i)} z _ {j i k} = - 1, \text { for } i = t, k \in K,\tag{4}
$$

$$
\sum_ {k \in K} \sum_ {(i, j) \in A _ {i} ^ {S}} + z _ {i j k} \leq S, \text {   for   all   } i \in V ^ {S},\tag{5}
$$

$$
\sum_ {k \in K} \sum_ {(i, j) \in A _ {i} ^ {C +}} z _ {i j k} \leq C, \text {   for   all   } i \in V ^ {C},\tag{6}
$$

$$
z _ {i j k} \in \{0, 1 \}, \text {   for   all   } ((i, j) \in A, k \in K.\tag{7}
$$

The constraint sets (2)–(4) ensure the conservation of <sup>fl</sup>ow for each node. The bundle constraints (5)–(6) restrict the <sup>fl</sup>ow out of the stress and camera nodes to their respective capacities.

## 5.3. Size of the model

The size of the problem is a function of the current CDTC schedule and the number of new test requests. For example, for a 10-day time horizon, each with 10 time slots, of which 80% of the slots are booked, a WCMH instance involving three new I1N requests on the <sup>fi</sup>rst day results in 3515 constraints and 6214 variables. If the initial schedule is 90% <sup>fi</sup>lled, the number of constraints increases to 3948, and the number of variables increases to 6928.

The model (1)–(7) is an integer program, and we have veri<sup>fi</sup>ed that its underlying constraint matrix is not totally unimodular. However, as we discuss in Section 6.2, our experiments have shown empirically that this problem is quite easy to solve to optimality.

## 6. Experimental analysis

MFSM was evaluated in two ways. First, for small, computationally tractable problems, we conducted an ex-post analysis to compare it to the MDP. In the second test we compared it against WCMH's current rule of always prioritizing outpatients and reserving occasional slots on the schedule to accommodate inpatients should the need arise.

## 6.1. The MFSM versus the MDP

A comparison of MFSM against the MDP required an ex-post analysis because, after the <sup>fi</sup>rst instance where the two methods make different decisions, the state space and transition probabilities change, and we cannot expect them to yield directly comparable solutions. This makes it impossible to compare performance based on, say the percentage of time the same decision is made. Rather, after the conclusion of each complete scenario, we calculate the value of the decisions made by each method using the same cost structure.

Prior to determining the MDP optimal policy, several simplifying steps were taken to reduce the size of the state space. This focus on “small” problems was done only for the sake of comparing the MDP to MFSM. Without such simpli<sup>fi</sup>cations the MDP quickly became intractable, providing no basis for comparison; in any practical setting, MFSM would not be limited to such a simpli<sup>fi</sup>ed, aggregate state space. To give an idea of the dif<sup>fi</sup>culty of implementing the MDP, <sup>fi</sup>nding the optimal policy for this small instance took over 1h. Additionally, the memory utilized during the policy generation was over one gigabyte. The simpli<sup>fi</sup>ed problem setting included only the three most common patient classes found at WCMH (I1N, OR, and O2N), a single camera, a single stress test room, and a time horizon of two days (i.e., 20 stages). We de<sup>fi</sup>ned three classes of unit specialization, cardiac, general medical/surgical, and emergency services. For ease of exposition we will use b = cardiac, $b _ { g } =$ general, $b _ { e } =$ emergency services. Additionally, the state of the hospital was consolidated and limited to four possibilities:

$$
1. \text { State   1: } b _ {c} = 3, b _ {g} = b _ {e} = 2,
$$

$$
2. \text {   State   2:   } b _ {c} = b _ {g} = b _ {e} = 1,
$$

$$
3. \text { State   3: } b _ {c} = b _ {g} = b _ {e} = 0,
$$

$$
4. \text { State   4: } b _ {c} = b _ {g} = b _ {e} = - 1.
$$

We further restricted the number of patients of each class requesting a test to at most two during each time period, and solved the MDP using backward recursion. The optimal policy was then used in the simulation of the MDP methodology. Using arrival patterns similar to the ones at WCMH, we generated four sets of new request arrivals for the time horizon. We examined arrival rates of an average of two, four, six, and eight new requests over the two-day time horizon. This equates to an average of one, two, three, and four new requests per day. Two thousand unique requests were generated for each of these four levels of arrival. The MDP simulation and the MFSM simulation both used the same arrival sets. Three different initial CDTC schedules were simulated: empty, 50% full (i.e., 10 screenings already scheduled during the 20 period horizon), and 80% full

For the analysis between the two approaches, we calculate the percentage “performance gap” for a single scenario as $( o _ { m } - o _ { n } ) / o _ { m } ,$ where $o _ { m }$ is the ex-post objective value of the MDP and $o _ { n }$ is the expost objective value of the MFSM. In Table 2 the mean percentage performance gap, along with its corresponding 95% con<sup>fi</sup>dence interval, are reported for each of the twelve design points. Overall, as expected, there is a small bias in favor of the MDP but MFSM performs well. Also, note that the con<sup>fi</sup>dence intervals for four of the twelve design points indicate that there is no signi<sup>fi</sup>cant difference between the two approaches (i.e., the ones that contain zero in the 95% con<sup>fi</sup>dence interval). Otherwise, the values for the mean percentage performance gaps indicate that the ex-post objective value of MFSM closely approximates that of the MDP. The higher performance gap rates from the last two design points are a result of having more patients requesting screenings than this experimental CDTC can accommodate within the time horizon. We expect the MDP to outperform MFSM in these cases, because the generated MDP policy explored all of the possibilities, while MFSM takes a snapshot prior to each decision and uses the data to generate expected pro<sup>fi</sup>ts for the various decisions.

Table 2  
A comparison between the MDP and the MFSM. All numbers are rounded to two signi<sup>fi</sup>cant digits to the right of the decimal.

<table><tr><td>Initial schedule</td><td>Arrival volume</td><td>Mean percentage gap</td><td>95% confidence interval</td></tr><tr><td>Empty</td><td>1 per day</td><td>0.00%</td><td>(0.00%, 0.00%)</td></tr><tr><td>Empty</td><td>2 per day</td><td>0.07%</td><td>(-0.04%, 0.19%)</td></tr><tr><td>Empty</td><td>3 per day</td><td>0.10%</td><td>(-0.07%, 0.26%)</td></tr><tr><td>Empty</td><td>4 per day</td><td>0.62%</td><td>(0.23%, 1.01%)</td></tr><tr><td>Half full</td><td>1 per day</td><td>0.19%</td><td>(0.11%, 0.27%)</td></tr><tr><td>Half full</td><td>2 per day</td><td>0.76%</td><td>(0.50%, 1.01%)</td></tr><tr><td>Half full</td><td>3 per day</td><td>1.44%</td><td>(0.53%, 2.34%)</td></tr><tr><td>Half full</td><td>4 per day</td><td>0.76%</td><td>(-1.97%, 3.49%)</td></tr><tr><td>80% full</td><td>1 per day</td><td>3.21%</td><td>(2.90%, 3.52%)</td></tr><tr><td>80% full</td><td>2 per day</td><td>7.89%</td><td>(7.39%, 8.38%)</td></tr><tr><td>80% full</td><td>3 per day</td><td>13.88%</td><td>(11.41%, 16.35%)</td></tr><tr><td>80% full</td><td>4 per day</td><td>17.99%</td><td>(12.93%, 23.04%)</td></tr></table>

On average, when computationally tractable, we expect the MDP to outperform the MFSM heuristic. The difference between the two techniques is in the complexity of how future events are anticipated. In any MDP, current decisions are made under the assumption that future decisions will also be made optimally, but this comes with the huge computational burden of planning decisions for all possible contingencies or possible future states. The MFSM heuristic, on the other hand, ignores the impact of future decisions, and instead simply projects average costs for current decisions, based on probabilities of future events and their costs. Simply put, the MFSM ignores the fact that we will respond to mitigate the effects of unexpected or lowprobability events, whether good or bad, while the MDP does not.

Thus for this small-scale test, we do <sup>fi</sup>nd instances for which the MDP does a better job of anticipating future events, consequently outperforming the MFSM heuristic. As seen in Table 2, the MFSM heuristic performs very well compared to the MDP until we get into a full schedule situation and there is an unexpectedly high volume of inpatient add-on arrivals. It should be noted though, that for this unnaturally small experiment (which was made small-scale enough to implement the MDP) the impact of one suboptimal patient routing decision has a large impact on the system as a percentage. But as we will see in the next section, where we compare MFSM to the hospital's prior policy, we were able to verify through a larger-scale simulation the that the MFSM network approach was robust, making vastly improved decisions in situations where the schedule was full, arrivals were heavy, and the problem instance was of a real-world size.

## 6.2. The MFSM versus the current approach

To compare MFSM with the hospital's current approach we simulated the CDTC's operations for two-week planning periods. Under the current approach some time slots are reserved, but when a con<sup>fl</sup>ict between an outpatient and an inpatient occurs, the policy is to always prioritize the outpatient. We therefore refer to WCMH's current policy as “POP” for prioritize outpatients. The 10 working days in the two-week planning period are divided into 10 one-hour time slots. In order to gain additional insights, we vary the proportion of CDTC capacity allocated to testing outpatients from 60% to 100% as shown in Table 3 for a total of nine design points. (Prior to our study, WCMH typically reserved 90% of the schedule for outpatients).

The simulation contained a common set of 200 independent “sequences” of inpatient test requests. Each sequence of inpatient test requests was created by randomly generating between zero and three inpatient requests (“add-ons”) using a discrete uniformdistribution for each of the 10 days in the planning horizon. This common set of inpatient test requests was used for each of the nine design points. For the simulations we did not consider the possibility of rescheduling outpatients for another day. So, while the outpatients can be delayed, if they cannot be tested on the day they were originally scheduled we assume that the patient decides to be tested at another facility and the hospital loses the revenue. This assumption gives a conservative estimate of the impact of MFSM on the biweekly revenue change because, in reality, a signi<sup>fi</sup>cant percentage (likely a majority) of these patients would be expected to still choose to be tested at WCMH. Finally, we do not consider cancellations from the outpatient schedule since the percentage of “no-shows” at the WCMH CDTC is less than 1%. We analyzed three performance metrics: difference in revenue, the percentage of the outpatients and inpatients requests served, and the number of additional nights rescheduled inpatients must remain in the hospital.

Table 3  
Biweekly revenue increase when adopting MFSM. For all design points, the revenue gains were statistically signi<sup>fi</sup>cant using paired t-tests.

<table><tr><td>Design point</td><td>OP schedule</td><td>Biweekly revenue increase</td></tr><tr><td>1</td><td>60%</td><td>$ 1296.41</td></tr><tr><td>2</td><td>80%</td><td>$ 3142.72</td></tr><tr><td>3</td><td>85%</td><td>$ 5509.32</td></tr><tr><td>4</td><td>87%</td><td>$ 8167.28</td></tr><tr><td>5</td><td>90%</td><td>$11,437.13</td></tr><tr><td>6</td><td>92%</td><td>$14,824.84</td></tr><tr><td>7</td><td>95%</td><td>$18,943.79</td></tr><tr><td>8</td><td>97%</td><td>$23,142.20</td></tr><tr><td>9</td><td>100%</td><td>$28,108.32</td></tr></table>

We used lp\_solve v5.5 to solve all problem instances of MFSM. Problems were <sup>fi</sup>rst solved by relaxing the integrality constraints on the decision variables. We veri<sup>fi</sup>ed that underlying constraint matrix is in fact not totally unimodular, but nonetheless the structure of the objective function in this setting tends to result in optimal solutions that are integer valued. In the rare occasions that fractional solutions were obtained (6.5% of the instances during this experiment) lp\_solve's branch-and-bound routine quickly provided an integer solution with the same objective function value after only a single branching. Thus, in our experience, each MFSM problem instance required a solution of at most two linear programs, with any linear program instance solving in less than one second using lp\_solve. The average solution time was 0.6 seconds.

## 6.3. Results

Tables 3 and 4 show the average biweekly increase in revenue due to using MFSM instead of POP and the 95% con<sup>fi</sup>dence interval for revenue increase. Since WCMH typically allocates 90% of the CDTC capacity to outpatient testing and since the inpatient census is typically elevated for the six month October–March period, we extrapolate an expected revenue gain during this period of approximately \$150,000 (\$11,437.13⁎13). The other half of the year MFSM could help them realize an additional \$40,000 in revenue gains (reduce the outpatient schedule to 80% corresponding to \$3,142.73⁎13), giving WCMH a yearly expected revenue gain of \$190,000.

Table 4  
95% con<sup>fi</sup>dence intervals for biweekly revenue gain.

<table><tr><td>Design point</td><td>OP schedule</td><td>Lower limit</td><td>Upper limit</td></tr><tr><td>1</td><td>60%</td><td>$1152.38</td><td>$1440.43</td></tr><tr><td>2</td><td>80%</td><td>$2623.67</td><td>$3661.77</td></tr><tr><td>3</td><td>85%</td><td>$4500.76</td><td>$6517.88</td></tr><tr><td>4</td><td>87%</td><td>$6802.22</td><td>$9532.34</td></tr><tr><td>5</td><td>90%</td><td>$9642.63</td><td>$13,231.63</td></tr><tr><td>6</td><td>92%</td><td>$12,695.79</td><td>$16,953.90</td></tr><tr><td>7</td><td>95%</td><td>$16,354.68</td><td>$21,532.89</td></tr><tr><td>8</td><td>97%</td><td>$20,115.97</td><td>$26,168.42</td></tr><tr><td>9</td><td>100%</td><td>$24,548.83</td><td>$31,667.82</td></tr></table>

Table 5 A comparison of service quality.

<table><tr><td rowspan="2">Design point</td><td rowspan="2">OP schedule</td><td colspan="3">POP</td><td colspan="3">Network approach</td></tr><tr><td>% of OP served</td><td>% of IP served</td><td>Additional IP nights</td><td>% of OP served</td><td>% of IP served</td><td>Additional IP nights</td></tr><tr><td>1</td><td>60%</td><td>100%</td><td>100%</td><td>0</td><td>100%</td><td>100%</td><td>0</td></tr><tr><td>2</td><td>80%</td><td>100%</td><td>97.03%</td><td>0.31</td><td>98.72%</td><td>99.29%</td><td>0.14</td></tr><tr><td>3</td><td>85%</td><td>100%</td><td>86.86%</td><td>0.85</td><td>96.81%</td><td>97.36%</td><td>0.25</td></tr><tr><td>4</td><td>87%</td><td>100%</td><td>79.58%</td><td>1.34</td><td>95.75%</td><td>96.54%</td><td>0.30</td></tr><tr><td>5</td><td>90%</td><td>100%</td><td>66.58%</td><td>2.03</td><td>94.20%</td><td>95.02%</td><td>0.32</td></tr><tr><td>6</td><td>92%</td><td>100%</td><td>53.90%</td><td>2.67</td><td>92.83%</td><td>93.26%</td><td>0.35</td></tr><tr><td>7</td><td>95%</td><td>100%</td><td>33.89%</td><td>3.62</td><td>90.74%</td><td>90.62%</td><td>0.37</td></tr><tr><td>8</td><td>97%</td><td>100%</td><td>19.93%</td><td>4.45</td><td>89.34%</td><td>88.55%</td><td>0.40</td></tr><tr><td>9</td><td>100%</td><td>100%</td><td>0%</td><td>5.57</td><td>87.45%</td><td>85.38%</td><td>0.42</td></tr></table>

Table 5 compares MFSM to the POP approach in terms of the service provided to inpatients and outpatients. Service level is calculated as the average percentage of inpatient and outpatient requests that are honored during the two-week scheduling period. The graphical illustration of service levels shown in Fig. 2a and b provides some interesting observations. By using MFSM, we are able to signi<sup>fi</sup>cantly improve the inpatient service level with only a small decrease in the outpatient service level. For example, when the CDTC allocates 90% of its testing capacity to outpatients the POP approach provides an inpatient service level of 66.58% and an outpatient service level of 100%. In contrast, MFSM provides an inpatient service level of 95.02% and an outpatient service level of 94.20%.

We also investigate the additional number of nights inpatients have to spend in the hospital. These results are in Table 5. Finally, Fig. 3 compares the average number of inpatient bed-days saved using MFSM and in place of the POP policy.

The difference in the reduction of inpatient bed-days was statistically signi<sup>fi</sup>cant using paired t-tests, in all design points except the <sup>fi</sup>rst design point where only 60% of the CDTC capacity was dedicated to outpatient tests. The result of reserving so much capacity for inpatient tests is that even the POP approach is able to serve all requests resulting in no avoidable additional inpatient nights. For all other design points MFSM outperforms POP.

The graphs in Fig. 2 can also help the CDTC make strategic decisions concerning their desired service levels under MFSM. For instance, if the hospital administration decides to maintain a 90% outpatient service level then Fig. 2a implies that the hospital should <sup>fi</sup>ll 95% of CDTC capacity with outpatient tests. This capacity allocation would also correspond to a service level of approximately 90% for inpatients.

![](/api/attachments/UYZZNAPU/fulltext/images/abc853d14c16dde86ffa3ed10e0a90f11c7414fc13255665bb89bc9c1ccb834f.jpg)  
Fig. 3. Comparison of the additional inpatient nights

## 7. Conclusions

Real-time allocation of cardiac diagnostic screening time slots represents a complex online decision-making problem of whether to screen inpatients or outpatients when con<sup>fl</sup>icts arise. The decision can impact the availability of beds on the inpatient units and the <sup>fi</sup>nancial performance of the hospital. In this paper we model the decision problem facing the CDTC as a discrete-time, <sup>fi</sup>nite-horizon MDP. We also conclude that solving the MDP is computationally intractable given the time constraints of the decision makers, motivating the development of a decision support system based on a dynamic multicommodity network <sup>fl</sup>ow model. The proposed solution method is <sup>fl</sup>exible and robust, making it applicable to a CDTC at almost any hospital. The technique was tested with a local partner hospital and showed that it is possible to achieve signi<sup>fi</sup>cant improvements in quality of service to inpatients and overall hospital revenue, with only minor decreases in outpatient service levels.

![](/api/attachments/UYZZNAPU/fulltext/images/b51ebcfe8920fc9657229991b614660660a377a6968776465a27460b539caea5.jpg)

![](/api/attachments/UYZZNAPU/fulltext/images/2980590f08b28b42f76740a14adf7b02ba79d38b170c2d5f9ac72b5bdd71376a.jpg)  
Fig. 2. A comparison of service levels.

By considering the impact of inpatient census and ED congestion on patient <sup>fl</sup>ow, we provide hospitals with the ability to dynamically prioritize inpatient and outpatient requests for cardiac diagnostic testing services. The result is the ability to provide high service levels to both populations, help ensure the availability of inpatient beds to the individuals that need them, and a net improvement in <sup>fi</sup>nancial performance. Future research should be conducted to determine the optimal location of reserved time slots in the scheduling horizon, in order to improve inpatient service levels while increasing utilization. In addition, the capacity of the CDTC itself could be dynamically altered through the use of overtime and modi<sup>fi</sup>cations to the contracts with the cardiologists that provide medical coverage. Dynamic capacity management can enable the CDTC to achieve higher levels of utilization and service, and enable the hospital to achieve improved patient <sup>fl</sup>ow, quality of care, and <sup>fi</sup>nancial performance.

## Appendix A. Details of the MDP

One-day tests collect rewards when started, since the model constraints ensure that they must <sup>fi</sup>nish, while two-day tests collect rewards when resumed. The transition probabilities for subsequent states are also functions of the initial state and the decision.

## Appendix A1. Notation

The following notation is used in the MDP model (for some we include their realizations at WCMH in parentheses):

Parameters m the number of time periods in a workday. (In the WCMH model, $m = 1 0 . )$

Γ the set of resource types consumed by the CDTC, ({camera (c), stress room $( s ) \}$

$p ^ { \prime }$ the number of each resource, (e.g., $p ^ { c } { = } 2 ; p ^ { s } { = } 1$ indicates that the hospital has two cameras and one stress room).

$Z$ the set of health care services the hospital provides.

$Z ^ { c } \subset Z$ the set of services that require patients to be on cardiac monitoring.

$Z _ { u }$ the set of services that can be accommodated by inpatient unit u.

$U _ { z }$ the set of inpatient units that can accommodate service z.

$\Psi$ the set of services impacted by the decision to start or resume an inpatient screening.

A service z is an element of Ψ if one of the following conditions hold: ( $1 ) z \in Z ^ { c } \mathrm { o r } ( 2 ) \left\{ \cup _ { u \in U _ { z } } Z _ { u } \right\} \cap Z ^ { c } \neq \emptyset .$

Q the set of all screening classes, $( \{ I R , . . . , O 2 N \} )$

$Q ^ { \mathrm { i n } }$ the set of classes of inpatient screenings, ({IR, I1N, I2N}).

$\bar { Q } ^ { \mathrm { { o u t } } }$ the set of classes of outpatient screenings, ({OR, O1N, O2N}).

$Q ^ { 1 } \subseteq Q$ the set of classes with one-day protocols, ({IR, I1N, OR, O1N})

$Q ^ { 2 } \subseteq Q$ the set of classes with two-day protocols, ({I2N, O2N}).

$p _ { i } ^ { f }$ the number of <sup>fi</sup>rst day phases in a class i protocol, (e.g., $p _ { O 2 N } ^ { f } = 2 )$

$p _ { i } ^ { s }$ the number of second day phases for class $i \in Q ^ { 2 } .$

$a _ { i j } ^ { f , \prime } = \left\{ { 1 \atop 0 } \right.$ if the jth first day phase of class i uses resource ℓ otherwise:

$a _ { i j } ^ { s , \ell } = \left\{ { 1 \mathrm { ~ i f ~ t h e ~ } j \mathrm { t h } \mathrm { ~ s } } \right.$ econd day phase of class $i { \in } Q ^ { 2 }$ uses resource $\ell$ ${ \mathcal { T } } = \{ 1 , . . . , T \}$ the index set of time periods, where period t is the current period.

$N ( k ) = k + ( m - k )$ )modm the index of the last time period in the day includes time $k \in \mathcal { T } .$

$\alpha _ { i }$ the reward for testing a patient of class i.

$\Omega _ { z }$ the expected reward for providing service z to a newly arrived patient into the hospital.

$\beta ^ { \mathrm { i n } }$ the cost of delaying the scheduled <sup>fi</sup>rst day start or second day resumption of an inpatient screening by one period within a day.

$\beta ^ { \mathrm { { o u t } } }$ the cost of delaying the scheduled <sup>fi</sup>rst day start or second day resumption of an outpatient screening by one period within a day.

$\gamma ^ { \mathrm { b e d } }$ the expected opportunity cost (due to the inability to admit a newly arrived patient) of making an inpatient wait overnight.

$\gamma ^ { \mathrm { i n } }$ the deterministic cost to the hospital of keeping an inpatient an additional night (because they leave right after screening) in the hospital.

$\gamma ^ { \mathrm { { o u t } } }$ the expected cost, based on the probability of balking, of making an outpatient wait an additional day before beginning a screening.

## Decision variables

At any time t, we make the decision to commit to a test by initiating or resuming it in the current time period. Once a test is initiated or resumed, the necessary resources are reserved for all time periods needed for the phases in the remainder of the current day. When a two-day test is initiated, the second day resources are not committed until the following day. This allows for the possibility that the <sup>fi</sup>nal stage of the two-day nuclear test could be performed at any time on the following day.

$y _ { i } ^ { f }$ the number of class $i \in Q$ screenings to initiate at time t.

$y _ { i } ^ { s }$ the number of class $i \in Q ^ { 2 }$ screenings to resume in their second days at time t.

$x _ { i k } ^ { f }$ the number of class $i \in Q$ screenings currently scheduled to <sup>2</sup>be initiated at time t, “intraday” rescheduled for time $k \in \{ t +$ $1 , . . . , N ( t ) - p _ { i } ^ { f } + 1 \}$ in the current day.

$x _ { i k } ^ { s }$ the number of class $i \in Q ^ { 2 }$ screenings currently scheduled to be resumed at time t, intraday rescheduled for time $k \in \{ t +$ $1 , . . . , N ( t ) - p _ { i } ^ { f } + 1 \}$

$x _ { i 0 } ^ { f }$ the number of class i Q screenings currently scheduled to be <sup>2</sup>initiated at time t, that are instead “extraday rescheduled”, i.e., not rescheduled for any time $k \in \{ t + 1 , . . . , N ( t ) - p _ { i } ^ { f } + 1 \}$ . Note <sup>2</sup>that patients returningfor the second day of a two-day nuclear screening cannot be extraday rescheduled.

## State variables

$w _ { i k } ^ { f }$ the number of class i Q screenings scheduled to start at time $k .$

$w _ { i k } ^ { s }$ the number of class $i \in Q ^ { 2 }$ screenings scheduled to resume at time k.

$O _ { k } ^ { \prime }$ the number of uncommitted resources ℓ available at time k today, where resources become committed from the decisions $y _ { i } ^ { f }$ and $y _ { i } ^ { s }$ .

$b _ { z }$ the total surplus of available beds on units in $U _ { z } .$

$L _ { z } = \left\{ \begin{array} { l l } { 0 \ \mathrm { i f } b _ { z } + \Delta b _ { z } { \geq } 0 } \\ { - ( \Delta b _ { z } + b _ { z } ) \mathrm { o t h e r w i s e } } \end{array} \right.$ the number of newly arrived patients in need of service z, that are diverted to a different hospital due to lack of bed availability (the $\Delta b _ { z }$ are random variables de<sup>fi</sup>ned below).

$L _ { i } ^ { \mathrm { { o u t } } } = \sum _ { k = 1 } ^ { N ( t ) = p _ { i } ^ { r } }$ the total number of rescheduled class $i \in Q ^ { \mathrm { o u t } }$ patients that choose not to return (the $\Delta d _ { i k } ^ { f }$ and $\Delta d _ { i 0 } ^ { f }$ are also de<sup>fi</sup>ned below). Random variables

$\Delta d _ { i k } ^ { f }$ the number of class $i \in Q ^ { \mathrm { o u t } }$ screenings rescheduled to start at time $k \in \{ t + 1 , . . . , N ( t ) - p _ { i } ^ { f } + 1 \}$ that choose not to return. $\Delta d _ { i 0 } ^ { f }$ <sup>2</sup>the number of class extra day rescheduled $i \in Q ^ { \mathrm { o u t } }$ screenings that choose not to return.

$\Delta \lambda _ { z } ^ { u }$ the number of arrivals of patients in need of service z to inpatient unit $u \in U _ { z }$

$\Delta \delta _ { z } ^ { u }$ the number of departures of patients in need of service z from inpatient unit $u \in U _ { z }$

$\Delta b _ { z }$ the change in the surplus of available beds on units in $U _ { z }$ (the change happens during time t, i.e. entering time $t + 1 )$ $\Delta b _ { z }$ is a function of $\Delta \lambda _ { z } ^ { u }$ and $\Delta \delta _ { z } ^ { u }$ and is used for notational convenience. The number of arrivals and the number of departures are independent between services and each other. Hence,

$$
\mathcal {P} (\Delta b _ {z}) = \sum_ {u \in U _ {z}} \sum_ {\overline {{z}} \in Z _ {u}} \mathcal {P} \Bigl (\Delta \lambda \frac {u}{\overline {{z}}} - \Delta \delta \frac {u}{\overline {{z}}} \Bigr).
$$

$\Delta w _ { i k } ^ { f }$ the number of new test requests to start class i screenings at time k.

Appendix A2. Process state

The process state (S) depends on the number of patients waiting to have tests started, the number of patients waiting to have tests <sup>fi</sup>nished, uncommitted numbers of resources at each time period, and the number of available inpatient and ED beds. When a decision is made to begin a test, the resources needed to complete the test are committed to that test in the appropriate time periods.

Appendix A3. Constraints

Feasible decisions at time t satisfy the following:

$$
y _ {i} ^ {f} + x _ {i 0} ^ {f} + \sum_ {k = t + 1} ^ {N (t) - p _ {i} ^ {f} + 1} x _ {i k} ^ {f} = w _ {i t} ^ {f} \text {   for   all   } i \in Q\tag{A.1}
$$

$$
y _ {i} ^ {s} + \sum_ {k = t + 1} ^ {N (t) - p _ {i} ^ {f} + 1} x _ {i k} ^ {s} = w _ {i t} ^ {s} \text {   for   all   } i \in Q ^ {2}\tag{A.2}
$$

$$
\sum_ {i \in Q} \left(a _ {i j} ^ {f, \ell} y _ {i} ^ {f} + a _ {i j} ^ {s, \ell} y _ {i} ^ {s}\right) \leq o _ {t + j - 1} ^ {\ell} \text {   for   all   } j \in \{1,..., N (t) - t \} \text { and   } \ell \in \Gamma\tag{A.3}
$$

Constraints (A.1) ensure that all screenings scheduled to begin at the current time t are either initiated or rescheduled. Constraints $\left( { \mathsf { A } } . 2 \right)$ perform the same function for the second day, except that extra day rescheduling is not an option because, once started, the two-day nuclear stress tests must be completed by the end of the second day. Constraints (A.3) guarantee that resource capacities are not exceeded at any period in the current day.

Appendix A4. Stage reward

At state $S ,$ once a feasible decision $D { \colon } = ( y _ { i } ^ { f } , x _ { i 0 } ^ { f } , x _ { i k } ^ { f } , y _ { i } ^ { s } , x _ { i k } ^ { s } )$ has been made there are immediate bene<sup>fi</sup>ts and costs that yield a net reward of $R ( S , D )$

When tmodm≠0:

$$
R (S, D) = f _ {1} - f _ {2} - f _ {3}
$$

where

$$
f _ {1} = \sum_ {i \in Q ^ {1}} \alpha_ {i} y _ {i} ^ {f} + \sum_ {i \in Q ^ {2}} \alpha_ {i} y _ {i} ^ {s}
$$

$$
f _ {2} = \beta^ {\text { out }} \sum_ {i \in Q ^ {\text { out }}} \sum_ {k = t + 1} ^ {N (t) - p _ {i} ^ {f} + 1} x _ {i k} ^ {f} + \sum_ {i \in Q ^ {\text { out }}} \alpha_ {i} L _ {i} ^ {\text { out }}
$$

$$
f _ {3} = \beta^ {\text {in}} \sum_ {i \in Q ^ {\text {in}}} \sum_ {k = t + 1} ^ {N (t) - p _ {i} ^ {f} + 1} x _ {i k} ^ {f} + \sum_ {z \in Z} \Omega_ {z} L _ {z}
$$

When t mod m=0:

$$
R (S, D) = f _ {1} - f _ {4} - f _ {5}
$$

where

$$
f _ {4} = \gamma^ {\text { out }} \sum_ {i \in Q ^ {\text { out }}} x _ {i 0} ^ {f} + \sum_ {i \in Q ^ {\text { out }}} \alpha_ {i} L _ {i} ^ {\text { out }}
$$

$$
f _ {5} = \gamma^ {\mathrm{in}} \sum_ {i \in Q ^ {\mathrm{in}}} x _ {i 0} ^ {f} + \sum_ {z \in Z} \Omega_ {z} L _ {z}
$$

The reward for providing cardiac screening tests are captured in $f _ { 1 } .$ The cost of rescheduling outpatients to a different time period within the current day plus the cost of losing the outpatients that choose to leave and have the service provided elsewhere are expressed in $f _ { 2 }$ and $f _ { 4 } .$ From a practical standpoint, the possibility of an outpatient deciding to have the service provided elsewhere is only a risk when the decision is made on whether or not to reschedule the initiation of the screening. For outpatients returning for the second day of a twoday nuclear screening, even if the appointment is rescheduled, it is not realistic that the patient would leave and start the entire screening process again with a different provider. The cost of requiring inpatients to wait until a later period in the day plus the expected cost of potential loss of inpatients due to overcrowding, are found in $1 f _ { 3 }$ and $f _ { 5 } .$ The determination of stage reward when t mod $m = 0$ differs from those when t mod $m \neq 0 ,$ since the waiting costs associated with an overnight delay are higher than for those for a single time period within the current day.

## Appendix A5. State transition

Let S be the current state, D the chosen decision array, and $\hat { S }$ the state after arrivals and departures occur. Ŝ is updated as follows:

When tb N(t):

$$
\hat {w} _ {i k} ^ {f} = w _ {i k} ^ {f} + \Delta w _ {i k} ^ {f} + x _ {i k} ^ {f} - \Delta d _ {i k} ^ {f} \mathrm{forall} i, \mathrm{andforall} k = t + 1,..., N (t)
$$

$$
\hat {w} _ {i k} ^ {s} = w _ {i k} ^ {s} + x _ {i k} ^ {s} \text {   for   all   } i, \text {   and   for   all   } k = t + 1,..., N (t)
$$

$$
\hat {o} _ {t + j} ^ {\ell} = o _ {t + j} ^ {\ell} - \sum_ {i \in Q} \left(a _ {i j} ^ {f, \ell} y _ {i} ^ {f} + a _ {i j} ^ {s, \ell} y _ {i} ^ {s}\right) \text {   for   all   } j \in \{0,..., N (t) - t \}, \ell \in \Gamma
$$

$$
\hat {b} _ {z} = \left\{ \begin{array}{l l} b _ {z} + \Delta b _ {z} + L _ {z} & \text { for   all } z \in Z \Psi \\ b _ {z} + \Delta b _ {z} + \sum_ {i \in Q ^ {\mathrm{in}} \cap Q ^ {1}} y _ {i} ^ {f} + \sum_ {i \in Q ^ {\mathrm{in}} \cap Q ^ {2}} y _ {i} ^ {s} + L _ {z} & \text { for   all } z \in \Psi \end{array} \right.
$$

$$
\hat {t} = t + 1
$$

$$
\hat {L} _ {z} = 0
$$

$$
\begin{array}{c} \hat {L} _ {i} ^ {\text { out }} = 0 \text {   for   all   } i \in Q ^ {\text { out }} \\ \text { When   } t = N (t), \end{array}
$$

$$
\hat {w} _ {i k} ^ {f} = w _ {i k} ^ {f} + \Delta w _ {i k} ^ {f} \quad \text {   for   all   } i, \text {   and   for   all   } k = t + 1,..., N (t).
$$

$$
\hat {b} _ {z} = b _ {z} + \Delta b _ {z} + L _ {z} \quad \text { for   all } z \in Z
$$

$$
\hat {t} = t + 1
$$

The state transitions from S to $\hat { S }$ with probability

$$
P _ {S, \hat {S}} (D) = \left[ \prod_ {i \in Q} \mathcal {P} \left(\Delta w _ {i k} ^ {f}\right) \right] \left[ \prod_ {i \in Q ^ {\text { out }}} \mathcal {P} \left(\Delta d _ {i k} ^ {f}\right) \right] \left[ \prod_ {i \in Q ^ {\text { out }}} \mathcal {P} \left(\Delta d _ {i 0} ^ {f}\right) \right] \left[ \prod_ {z \in Z} \mathcal {P} (\Delta \lambda_ {z}) \right] \left[ \prod_ {z \in Z} (\Delta \delta_ {z}) \right].
$$

We make the reasonable assumption that demands for screening classes and time slots within classes are mutually independent, since demand arises from multiple independent sources. Similarly, we assume that the probability that an outpatient who was rescheduled decides not to return, is independent of both the screening class and the time slot. Additionally, the net changes in the number of available beds of the various services are assumed mutually independent.

## Appendix A6. Objective Function

Let V (S) be the maximum expected reward of a T stage problem that begins in state S, and D be the set of feasible decisions that can be made. $\breve { \hat { S } }$ is the state that results from beginning in state S and taking action $\mathbf { \Pi } _ { D \in \mathbf { D } }$ and then random variables are realized. The objective <sup>2</sup>function is

$$
V _ {t} (S) = \max _ {D \in \mathbf {D}} \left\{R (S, D) + \sum_ {\hat {S}} P _ {S, \hat {S}} (D) V _ {t + 1} (\hat {S}) \right\}, t <   T.\tag{A.4}
$$

The “curse of dimensionality” becomes apparent when examining the dimension of the state space. The state variable $b _ { z }$ can range from having no available beds to every bed capable of accommodating service z being open. Let $\overline { { b } } _ { z }$ be the total number beds in $U _ { z }$ plus one $( { \mathrm { i . e . } }$ , the cardinality of the range for $b _ { z } )$ . Within a single time period, then, we will have a dimension on the order of $\Pi _ { z \in z } \overline { { b } } _ { z }$ . For example, a <sup>2</sup>hospital with 20 services and a maximum capacity of 20 for each service results in a dimension of $2 1 ^ { 2 0 }$ for the state variable $b _ { z } .$ Even before considering the other state variables, it is apparent that this model becomes intractable quickly and motivates the desire for another technique.

## Appendix B. Derivation of inpatient delay costs under MFSM

The negative pro<sup>fi</sup>t consists of the sum of the deterministic inconvenience cost to the patient and the expected lost opportunity associated with being unable to admit a new inpatient. The opportunity cost relates only to the decision to delay an inpatient screening request. It is a function of the pro<sup>fi</sup>t associated with admitting a new inpatient and the probability that, in the future time period, the number of available beds will be less than the number of new inpatients. Inpatient arrival rates and the associated pro<sup>fi</sup>ts are easily estimated from historical data. We used an aggregated Poisson distribution with parameter $\lambda _ { z }$ to describe the arrival distribution for each service. To compute $\lambda _ { z }$ using historical admission data, we aggregated the arrival rate for each service over all units capable of treating that type of patient. Hence, $\lambda _ { z } = \Sigma _ { u \in U _ { z } } \lambda _ { z } ^ { u }$ Kolmogorov–Smirnov tests at the $\alpha { = } 0 . 0 5$ <sup>2</sup>level showed that there was a strong goodness-of-<sup>fi</sup>t between the aggregated Poisson distributions and the historical patient arrivals.

The expected cost of delaying an inpatient is then calculated as $\sum { _ { z \in Z } \Omega _ { z } \mathcal { P } ( \lambda _ { z } \geq b _ { z } ) }$ , where $\lambda _ { z }$ is the aggregated arrival rate for patients of service z as described above. The $\mathcal { P } ( \cdot )$ term represents the probability that the number of patients that need a bed is greater than the number of currently available beds. The values for $\Omega _ { z }$ were estimated using WCMH's billing records.

## References

[1] P.P. Belobaba, Application of a probabilistic decision model to airline seat inventory control, Operations Research 37 (2) (1989) 183–197.

[2] G.R. Bitran, S.M. Gilbert, Managing hotel reservations with uncertain arrivals, Operations Research 44 (1) (1996) 35–49.

[3] M.L. Brandeau, F. Sainfort, W.P. Pierskalla (Eds.), Operations Research and Health Care: A Handbook of Methods and Applications, International Series in Operations Research and Management Science, Springer, 2004.

[4] W.J. Carrol, R.C. Grimes, Evolutionary change in product management: experi ences in the car rental industry, Interfaces 25 (5) (1995) 84–104.

[5] M. Durbin, K. Hoffman, The dance of the thirty-ton trucks: dispatching and scheduling in a dynamic environment, Operations Research 56 (1) (2008) 3–19.

[6] C.D. Flagle, Some origins of operations research in the health services, Operations Research 50 (1) (2002) 52–60.

[7] M. Geraghty, E. Johnson, Revenue management saves national car rental, Interfaces 27 (1) (1997) 107–127.

[8] L.V. Green, S.V. Savin, B. Wang, Managing patient service in a diagnostic medical facility, Operations Research 54 (1) (2006) 11–25.

[9] I. Junglas, C. Abraham, B. Ives, Mobile technology at the frontlines of patient care: understanding <sup>fi</sup>t and human drives in utilization decisions and performance, Decision Support Systems 46 (3) (2009) 634–647

[10] J. Liebenau, G. Harindranath, Organizational reconciliation and its implications for organizational decision support systems: a semiotic approach, Decision Support Systems 33 (4) (2002) 389–398.

[11] V. Lieberman, U. Yechiali, On the hotel overbooking problem: an inventory system with stochastic cancellations, Management Science 24 (11) (1978) 1117–1126.

[12] E. Litvak, M.C. Long, A.B. Cooper, M.L. McManus, Emergency department diversion: causes and solutions, Academic Emergency Medicine 8 (11) (2001) 1108–1110.

[13] A. Oztekin, F.M. Pajouh, D. Delen, L.K. Swim, An RFID network design methodology for asset tracking in healthcare, Decision Support Systems 49 (1) (2010) 100–109.

[14] P. Parker, Move care to a higher level with emergency systems, Nursing Management 35 (9) (2004) 82–84.

[15] J. Patrick, M.L. Puterman, M. Queyranne, Dynamic multipriority patient scheduling for a diagnostic resource, Operations Research 56 (6) (2008) 1507–1525.

[16] S. Sneha, U. Varshney, Enabling ubiquitous patient monitoring: model, decision protocols, opportunities and challenges, Decision Support Systems 46 (3) (2009) 606–619.

[17] S. Thompson, M. Nunez, R. Gar<sup>fi</sup>nkel, M.D. Dean, Ef<sup>fi</sup>cient short-term allocation and reallocation of patients to <sup>fl</sup>oors of a hospital during demand surges, Operations Research 57 (2) (2009) 261–273.

Robert W. Day is an Assistant Professor of Operations and Information Management in the School of Business at the University of Connecticut He received his Ph D in Applied Mathematics with a concentration in Operations Research from the University of Maryland College Park in 2o04. His dissertation focused on combinatorial auctions received INFORMS' Dantzig dissertation award in 2005 and later Day and Raghavan received the 2008 INFORMS Computing Society Prize for related work in this area. Their algorithm for setting prices in combinatorial auctions has been adopted for spectrum license auctions in the United Kingdom and the Netherlands. Day continues to study combinatorial auctions and other applications, including Healthcare Operations Research.

Matthew D. Dean is an Assistant Professor of Management in the College of Business Administration at the University of New Orleans. His current research interests include health care operations management and health care information systems. His work has appeared in journals such as Operations Research and Communications of the ACM.

Robert Gar<sup>fi</sup>nkel is a professor in the Operations and Information Management Department of the School of Business at the University of Connecticut. His work on a variety of problems in operations research, mainly involving combinatorial optimization, has appeared in such journals as: Operations Research; Management Science; Informs Journal on Computing; Decision Support Systems, and Mathematical Programming. His current research has focused heavily on the problem of improving ef<sup>fi</sup>ciency in hospital settings. Other ongoing research streams include: optimally balancing valid security concerns against the desire to provide users of a database with valuable information; design of markets for grid computing; construction of recommender systems for shopbots; optimization problems in micro<sup>fl</sup>uidic systems; and optimization in vehicle routing. He is also coauthor of the book Integer Programming with George Nemhauser.

Steven M. Thompson is an Assistant Professor of Information Technology in the Management Department in the Robins School of Business at the University of Richmond, Richmond, VA. His current research interests include health care information technology, health care systems engineering, and issues relating to the use of information technology to coordinate inter-organizational operations. His research has appeared in Operations Research, Information Systems Research, Communications of the ACM, Decision Sciences, and other journals and conference proceedings.
