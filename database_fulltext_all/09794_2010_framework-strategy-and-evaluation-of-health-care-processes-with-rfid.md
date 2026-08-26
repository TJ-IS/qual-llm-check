---
otero_id: 9794
otero_key: "K22D9SUU"
title: "Framework, strategy and evaluation of health care processes with RFID"
authors: "Wei Zhou; Selwyn Piramuthu"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.08.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Framework, strategy and evaluation of health care processes with RFID

Wei Zhou <sup>a,c</sup>, Selwyn Piramuthu <sup>b,c,</sup>⁎

<sup>a</sup> Information Systems and Technologies, ESCP Europe, 75543 Paris cedex 11, France

<sup>b</sup> Information Systems and Operations Management, University of Florida, Gainesville, FL 32611, USA

<sup>c</sup> RFID European Lab, Paris, France

## a r t i c l e i n f o

Article history: Received 12 November 2009 Received in revised form 19 July 2010 Accepted 8 August 2010 Available online 12 August 2010

Keywords: RFID Health care

## a b s t r a c t

The working environment in health care organizations is characterized by its demand for highly dynamic process and labor management in which (a) medical personnel are generally associated with several disparate types of tasks, (b) service location and service personnel change frequently, (c) highly uncertain environment where emergency issues could arise at any time, and (d) the stakes are high since invaluable human lives are involved. There is an urgent need from both researchers and health care organizations to develop reasonable management strategies for maintaining a good balance between ef<sup>fi</sup>cient management and superior medical service quality. We discuss the potential for real-time health care coordination and effective medical process and labor management enabled by RFID item-level tracking/tracing identi<sup>fi</sup>cation technology. We explore the uniqueness of instance-level process mining and its application in health care environment. We then propose an adaptive learning framework that supports real-time health care coordination and analyze its bene<sup>fi</sup>ts compared to traditional routine process and labor management. We <sup>fi</sup>nd that while RFID-enabled real-time medical process and labor management provides marginal improvement for premium medical service providers, it generates appreciable improvement both in terms of ef<sup>fi</sup>ciency and service quality for public health care institutions where availability of necessary resources such as medical staff and equipment are highly constrained.

© 2010 Elsevier B.V. All rights reserved

## 1. Introduction

The number of preventable patient safety incidents and/or medical errors such as wrong drug item and/or quantity, transfusion using the wrong blood bag, mislabeled blood sample, among others, is on the rise as budget cuts in health care institutions and pharmaceutical industry translate to related adverse effects. RFID tags are touted to be primary contenders among the technologies used to address this issue. IDTech (2008) predicts the market for RFID tags and associated systems and services in health care to rise from \$120.9 million in 2008 to \$2.03 billion in 2018.

RFID tag use in health care and pharmaceutical industries has seen phenomenal growth in recent years spurred primarily through developments in tagging of drugs, real-time location and instancelevel information (for items such as medical equipment, patients and medical staff), and automated error prevention. Developments in tagging of drugs are driven by the need for improved anti-counterfeiting measures, theft deterrence, and improved stock control and recalls. Real-time instance-level information, generated through RFID-tagged entities, enables the effective use of constrained resources while reducing errors due to inadvertent mismatches (e.g., mother–baby and patient–blood bag mismatch). RFID tag use in automating processes (e.g., appropriate medical record delivery) can reduce possible errors due to human input. Unlike their use in some applications (e.g., toll-payment systems), RFID use in health care and pharmaceutical industries carries with it unquanti<sup>fi</sup>able bene<sup>fi</sup>ts such as safety and security and higher tolerance for longer payback periods.

While patient privacy is a concern when using RFID tags that broadcast information without knowledge of the tagged entity, means to address such issues through cryptography has been under way for the past several years (e.g., [10,11] and the references therein). The existence of multiple privacy frameworks including the Health Insurance Portability and Accountability Act (HIPAA), the Electronic Privacy Information Center (EPIC)'s RFID guidelines, the principles of Fair Information Practices (FIP), and the general concerns associated with the generation and use of any personally identi<sup>fi</sup>able information guide the extent to which personally identi<sup>fi</sup>able information can be gathered, stored, and used.

Togt, et al. [15] demonstrated that, under certain worst-case conditions when maximum power settings were used, electromagnetic interference (EMI) from RFID readers can interfere with medical devices used in critical care. Seidman et al. [13,14] considered the Electromagnetic Compatibility (EMC) between RFID readers and several pacemakers and Implantable Cardiac De<sup>fi</sup>brillators (ICD) and report that reactions ranged from “non-clinically signi<sup>fi</sup>cant events to the potentially harmful inappropriate tachyarrhythmia detection and delivery of therapy or complete inhibition of cardiac pacing.” Standards for RF emissions such as those from the Federal Communications Commission (FCC) and European telecommunications Standards Institute (ETSI) alert medical device manufacturers of possible interference from RFID and other RF sources. The issues related to RF interference can be alleviated through appropriate technological or spatial means. Nevertheless, the bene<sup>fi</sup>cial aspects of RFID-generated item-level information demands serious consideration for RFID tagging entities in health care environments.

Over the years, RFID tags have been successfully incorporated at various levels in a health care setting. The recently introduced Daily RFID Silica Gel wristband tag stores medical record information in a chip rather than paper. This reusable (after high-temperature sterilization), waterproof, and heat-resistant wristband helps identify and match the correct patient and medical staff as well as provides privacy to patients through electronic records. Other examples include Siemens' use of RFID tags for marking sponges used during operations and in identi<sup>fi</sup>cation tags for the operating team itself to eliminate missing sponges that are unintentionally left inside the operated person by tracing them from storage to disposal or reduce errors due to unintended mismatches in personnel.

The health care environment is highly dynamic in its demand for real-time process and labor management where (a) medical personnel are generally associated with several disparate types of tasks, (b) service location and service personnel change frequently, (c) the environment is replete with a high level of uncertainty where emergency issues could arise at any time, and (d) the stakes are extremely high since invaluable human lives are involved. There is an urgent need from both researchers and health care organizations to develop mechanisms for maintaining a good balance between ef<sup>fi</sup>cient management and superior medical service quality within such a high stress work environment.

RFID tag applications, despite their potential in health care industry and their unique applications, have not been extensively studied in this area. Their bene<sup>fi</sup>ts including both tangible and intangible pay-offs and possible application mechanisms are generally not widely known in many business sectors (e.g., [16,19]). We consider the uniqueness of RFID, such as their ability to provide instantaneous item-level information [18] in health care environments and propose an adaptive learning framework to utilize this technology to facilitate human resource management decisions.

While existing research addresses some of the issues discussed above, there is a paucity of published research on improving processes in health care environments using information generated through RFID tags. Although various applications of process mining have been studied in the <sup>fi</sup>eld of health care, we <sup>fi</sup>nd that a majority of existing research in this <sup>fi</sup>eld are focused at the process optimization stage. We extend this to investigate health care optimization problem from a process and labor management perspective to dynamically determine and update medical personnel assignments based on an RFID instance-level tracing/tracking system. Our proposed mechanism provides a fresh look at medical process and labor management utilizing advanced instance-level identi<sup>fi</sup>cation data to improve health care provider/patient ef<sup>fi</sup>ciency/satisfaction.

## 2. Literature review

Hersh et al. [8] assess the value of electronic health care information exchange and inter-operability between providers (hospitals and medical group practices) and independent laboratories, radiology centers, pharmacies, payers, public health departments, and other providers. Their analysis indicates that savings from fully standardized inter-operability and information sharing between health care providers and other types of organizations could save billions of dollars each year.

Clinical and medical services have generated an enormous amount of data on patients and their medical conditions that could be used to generate invaluable knowledge for many different purposes such as better medical treatment, medical service improvement, and disease diagnoses [12]. There are two main trends in health care information system design, with one approach putting employee and their working relationships at the center that stresses the importance of job satisfaction, workers' needs, and skill enhancement [7,9], and another approach with a focus on patients and end-users [3,4].

Process mining has been studied extensively. With results limited to sequential behavior, Cook et al. [5] considered process mining using neural networks, algorithmic approach, and Markovian approach. Cook et al. [6] studied the measurement of discrepancies between a process model and the actual behavior from event-based data. To facilitate process discovery and work<sup>fl</sup>ow design, many systems have been developed including the IBM MQSeries work<sup>fl</sup>ow. Via a graph generating procedure, Agrawal et al. [1] were the <sup>fi</sup>rst to introduce the idea of applying process mining in the context of work<sup>fl</sup>ow management.

The application of data mining and process discovery in health care environment is not new. For example, Yang et al. [17] propose a datamining framework that utilizes the concept of clinical pathways to facilitate systematic construction. Health care Information System evaluation is nevertheless a very complex problem that could involve these three areas: the complexity of the evaluation object, the complexity of an evaluation project, and the motivation for evaluation [2]. It has been argued that this evaluation that goes into more detail is desirable in health care applications. We evaluate our proposed framework using two criteria: health care process ef<sup>fi</sup>ciency and medical service quality. Clearly there are other factors that also matter in health care management, including medical staff–patient relationship and privacy issues. We focus only on issues related to medical process management.

## 3. Motivating examples

Consider a small clinic in which the medical staff includes two doctors, three nurses and two supporting staff. Our objective is to consider health care resource management such that certain ef<sup>fi</sup>ciency and service quality are maintained. Assume that necessary jobs in this clinic include 10 repetitive tasks and an uncertain number of non-repetitive tasks. Each repetitive task follows a pre-determined routine with an initial learning cost and only a marginal service cost thereafter. Non-repetitive tasks may involve emergency situations and other unexpected events that are common in a health care environment with both learning cost and service cost. Without considering the non-repetitive tasks, the assignment of workload forms a 7 by 10 matrix $[ \Omega ] _ { 7 \times 1 0 ^ { . } }$ Conceptually, knowing the ability of each employee $[ \Psi ] _ { 7 \times 1 0 }$ enables the decision maker to identify task assignments such that a required ef<sup>fi</sup>ciency and service quality can be obtained and maintained. $E _ { i j } { = } \Omega _ { i j } / \Psi _ { i j }$ indicates the ef<sup>fi</sup>ciency of a speci<sup>fi</sup>c task performed by a given medical staff.

A simpli<sup>fi</sup>ed version of this problem is solvable for maximum ef<sup>fi</sup>ciency, for example, when $\Omega \sim \{ \varOmega \in \{ 0 , 1 \} \}$ . Practically, it is more complicated because the service location changes over time and some tasks are shared by multiple medical personnel such that $\Omega \sim \{ \varOmega \in [ 0 , 1 ] \}$ . In a hospital with a large service area even within the same department and with the demand for non-repetitive tasks that could arise any time anywhere, it is rather dif<sup>fi</sup>cult to determine and operationalize an optimal staff (and other related resource) allocation in real-time. With adaptive learning ability that is based on a current snapshot of instance-level information in a constrained hospital area, we claim that our proposed framework is able to provide better ef<sup>fi</sup>ciency and improved satisfaction among medical care personnel and patients.

Consider the following example that illustrates the potential bene<sup>fi</sup>t of incorporating RFID-tagged system in health care process mining and process and labor management. There is one regular (i.e., average) patient and two medical staff (a doctor and a nurse). Assume that the standard procedure involves three different task assignments: preparation, diagnosis and after-treatment care. For a regular patient without special requirements, the task assignment vector is given by

$$
\alpha = \left[ \begin{array}{c c c} P r e p & D g n s & C a r e \\ 1 & 1 & 1 \end{array} \right]
$$

which signi<sup>fi</sup>es one unit of medical preparation, one unit of diagnosis and one unit of after-treatment care. Assume the ability matrix of the doctor and nurse for each of these tasks to be given by:

$$
a = \left[ \begin{array}{c c c c} d t: & 4 & 3 & 1 \\ n s: & 4 & 0 & 1. 1 \end{array} \right]
$$

If we standardize the assignment and ability by time, the doctor takes 20 min (1/3 h) to diagnose an average patient and a nurse takes in<sup>fi</sup>nite time, which makes the nurse unquali<sup>fi</sup>ed for such a task assignment. Both quali<sup>fi</sup>ed for medical preparation, the doctor and the nurse would take equal time (15 min) to <sup>fi</sup>nish this assignment. Given the above, a possible optimal assignment for the above scenario could be:

$$
\beta = \left[ \begin{array}{c c c} 0. 5 & 1 & 0 \\ 0. 5 & 0 & 1 \end{array} \right]
$$

We limit the cumulative set of tasks a medical personnel could take such that after a certain amount of work has been done in a given time period, the service quality of this person decreases.

$$
L = \left[ \begin{array}{c c c c} d r: & 1, & 1. 2, & 1. 5 \\ n s: & 0. 8, & 1, & 1. 4 \end{array} \right]
$$

The time a medical personnel spends performing a certain task can be condensed. For example, a doctor may be constrained to diagnose a patient in 10 min (instead of the normally required 20 min). I.e., the accumulated assignment hours can be more than the actual time spent. In a busy 8 h work day, a doctor can perform 12 h of cumulative assignments by condensing the time taken by each task assignment.

It is natural to relate the service quality to the accumulated medical personnel assignment in a prede<sup>fi</sup>ned work time period. For example, in 1 h a doctor would provide her perfect service if her accumulated workload is lower than 1 h, semi-perfect service between 1 to 1.2 h, below-average service between 1.2 and 1.5 h, and poor service after 1.5 h. The decreased service quality may be a result of increased stress, complication of work environment requiring the performance of multiple tasks simultaneously, shortened communication time, shortened service time, among others.

With quality differentiation, we <sup>fi</sup>nd that the originally optimal solution β would make the nurse to be overloaded with 1.06 h of work. As a result, this nurse's service quality would be below average. A new workload matrix can improve the nurse's service quality by balancing her workload with the doctor, such as

$$
\beta (t) = \left[ \begin{array}{c c c} 0. 5 & 1 & 0. 3 \\ 0. 5 & 0 & 0. 7 \end{array} \right]
$$

Both the doctor and nurse are working under their respective comfort zones and the best possible medical service quality can still be maintained. In a traditional routine-based medical assignment framework, assignment process and service quality information are periodically collected and analyzed to determine the process routine $[ \beta _ { 1 } , \beta _ { 2 } , . . . , \beta _ { N } ]$ for a given time period. New periodic routines may be repetitively modi<sup>fi</sup>ed and updated thereafter.

With RFID instantaneous item-level information tracking and tracing medical physical assets and personnel process mining, predesignated routines can be replaced by instantaneous workload/ service quality analysis and real-time assignments $[ \beta _ { 1 } ( t ) , \beta _ { 2 } ( t ) , . . . , \beta _ { N }$ (t)]. Uncertainties including emergency situation or any unanticipated events at time t, $\{ \varepsilon _ { n } ( t ) | \beta _ { n } ( t ) = \beta _ { n } + \varepsilon _ { n } ( t ) \}$ , under the ultra-dynamic work environment are captured and accommodated by real-time dynamic work assignment. As a result, both medical service quality and cost ef<sup>fi</sup>ciency are improved compared to a traditional routinebased medical assignment framework.

In what follows, we propose a self-learning mechanism with instantaneous RFID health care process mining and real-time medical resource allocation mechanism. Then we introduce a set of heuristics that enables the proposed mechanism. In Section 4, we model this scenario in both static and dynamic ways so that potential bene<sup>fi</sup>ts of the suggested framework could be further analyzed. Then we discus managerial insights on the conditions under which this framework would work and to what extent.

## 4. Health care process optimization with RFID

Process optimization has been studied extensively through various disciplines. The unique problem of process and labor management in health care domain, however, has not received necessary attention from researchers in the area. The problem of resource allocation including medical personnel is very different from process and labor management in other domains. In health care environment, employees are more likely to be simultaneously involved with multiple tasks, to handle emergency issues, and to work with different sets of colleagues and equipment within the span of a single workday shift. The working environment at a health care organization is much more dynamic and more tense than at most other organizations simply because human lives are directly at stake.

## 4.1. Framework

Fig. 1 illustrates a medical process and labor allocation scenario where each medical personnel is assigned multiple tasks as per their skill-set and skill requirements at this organization based on average estimates. We consider a repetitive task as one that is pre-assigned to each medical personnel and follows certain procedure and a set of standard protocol. For example, pre-surgery preparation as a repetitive task may include sanitizing, preparing surgical equipment, arranging service room, etc. Non-repetitive tasks, represented by dotted lines, on the other hand, occur on an unpredictable basis from the perspective of each individual medical personnel and are therefore not pre-assigned. Medical personnel are trained to take on certain health care tasks, and it is resource intensive for the health care organization to coordinate tasks such that no single resource is overly stressed while other resources are idle.

Traditionally, health care task assignments are pre-designated and are periodically evaluated and updated. Once the task assignments are determined, they are held <sup>fi</sup>xed until the next reevaluation period. Computational and coordination costs are minimized at the expense of reduced <sup>fl</sup>exibility. In our proposed framework, ef<sup>fi</sup>ciency and service quality are continually evaluated on a real-time basis so that improved <sup>fl</sup>exibility is achieved. Ef<sup>fi</sup>ciency can be measured by accumulated workload on each medical personnel. Full service quality is evaluated after the procedure while partial service quality can be obtained during the procedure. While the appropriate hiring of more personnel generally results in increase in overall service quality by reducing average workload and stress on each medical personnel, ef<sup>fi</sup>ciency (workload) and service quality are generally negatively correlated. Measured workload and evaluated service quality are further analyzed to balance economic issues and satisfaction level of both medical personnel and patients. Based on these analyses, further decisions are made on hiring new personnel as well as training existing ones.

![](/api/attachments/K22D9SUU/fulltext/images/d3d7557fc720ea640e71195b36c4e356568b812e6d45c239c2842940fcfe195e.jpg)  
Fig. 1. Personnel resource management in health care

Fig. 2 illustrates the framework for effective health care design with RFID instance-level identi<sup>fi</sup>cation information on medical equipment, staff, and patients. Equipped with RFID tracking/tracing technology, all physical entities in a hospital are instantaneously traced and monitored via a centralized computer system. Information about the movement of a tagged item/person and of any equipment and other resource updates are further analyzed through process mining to discover useful and actionable patterns and to form a knowledge base for future decision making.

## 4.1.1. Process mining

The primary source of input in the proposed system are the individual RFID tags that are distributed across the hospital environment, including personnel, patients, medical equipment, and the general health care organization infrastructure. These RFID tags can either be periodically polled (passive tags) or have continuous conversation with (active tags) to gather necessary up-to-date information on a real-time basis. The information thus obtained can then be used in the system to generate appropriate decisions. RFID data received from various tags are fed to the Process Mining module, which essentially looks for both implicit and explicit usable patterns that are present in this data. Such patterns could include information about the general patterns of room visits by a given doctor in any given day through the speci<sup>fi</sup>c steps taken to address a given ailment. While uncertainties in the medical environment precludes prede<sup>fi</sup>ning allocated resources for any given case, knowing what is currently available is useful to generate possible allocations that improve the overall effectiveness of the health care organization. Moreover, such knowledge can also aid in preempting non-critical tasks when necessary to accommodate tasks (and, in turn, related resources) that require immediate attention. The importance of timely availability of necessary information, including those related to any resource constraints, in emergency situations cannot be overstated when lives are at stake where every second does count.

## 4.1.2. Process optimization

Data from RFID tags as well as a snapshot of the current hospital working environment including the characteristics of arriving patients and patients who are currently being served at the hospital, the availability of medical staff (doctors, nurses, etc.), and the availability of medical equipment and other resources (e.g., rooms for diagnosis, performing operations, etc.), among others, are used as input in this module. The patterns generated in the Process Mining module are used to optimize the general work<sup>fl</sup>ow at the hospital at both <sup>fi</sup>ner and coarser levels of granularity. While it is not easy to achieve <sup>fi</sup>ner levels of granularity in a majority of hospitals due to unavailability of real-time data at that level, the presence of RFID tags enables this in the proposed system. The patterns obtained can also be used for purposes of allocating resources including equipment, rooms, personnel, etc., to achieve improved performance in the entire system.

![](/api/attachments/K22D9SUU/fulltext/images/2846260d1a934f4fc7762bdd70169af8df4de8a4f7ea124936f649bd40e84244.jpg)  
Fig. 2. Adaptive learning scheme for item-level health care process optimization.

The Process Optimization module, therefore, optimizes the processes that take place within the hospital while taking into consideration events that occur at its interface (e.g., arrival of new patients and equipment). This module considers several possible (feasible) alternatives and decides on the most appropriate course of action as per the objective (function) of interest for every point in time using all available resources.

## 4.1.3. Service provision

Output from the Process Optimization module is used as input to the Service Provision module. Here, the chosen alternative course of action is operationalized using appropriate resources. Service provision necessarily involves ef<sup>fi</sup>ciently providing essential service that accomplishes its intended purpose with minimal deleterious effects on this patient as well as other patients and constrained resources. Thanks to process analysis and optimization, an immediate bene<sup>fi</sup>t can be tailored towards improving operational ef<sup>fi</sup>ciency. Another bene<sup>fi</sup>cial side-effect of this is the overall improvement in medical error rates that results from increased attention paid to individual processes. Realization of actual medical services in this module could be selectively measured or to some extent quanti<sup>fi</sup>ed for further data analysis and self-learning for the system to adapt to any new phenomenon and unobserved rules.

## 4.1.4. Evaluation

The Evaluation module performs the necessary function of evaluating the performance of the system. Without some means to measure the performance of the system, it is dif<sup>fi</sup>cult to gauge its current effectiveness as well as the potential for any improvements that can be made. This module essentially monitors the performance of the system continually through the observation of all the processes as they occur in real-time as well as the evaluation of output from each of the processes. While performance at any hospital environment may vary over time depending on current resource constraints that could depend on the supply-side and demand-side dynamics, it is essential to maintain performance within safe limits to avoid compromising the lives of patients as well as everyone involved in the process. Even if the system performs better than expected based on the pre-speci<sup>fi</sup>ed performance criteria and benchmarks, it is necessary to be on the look-out and to consider possible options where further improvement could be effectively achieved without much disruption in the smooth <sup>fl</sup>ow of the system.

The knowledge base is the repository for learned knowledge in the system. Once created, it is not uncommon for knowledge bases to remain static with no modi<sup>fi</sup>cations to stored knowledge. Reasons for this could be the additional effort necessary for its operationalization, lack of resources, or plain simple omission. The knowledge base in the system needs to be updated periodically to prevent staleness of acquired knowledge. Moreover, evaluating a process is of no tangible use unless there is a means to act on less than perfect evaluations. I.e., when the evaluation shows that there is room for improvement, it helps to know where exactly this improvement is possible and even better to know what can be done to accomplish this change. In the proposed system using instance-level RFID data, we are able to evaluate and suggest the best course of action through periodic monitoring, evaluating, and incremental learning.

## 4.1.5. Adaptive learning

As the name suggests, the Adaptive Learning module adaptively learns new knowledge and updates existing knowledge. This module is especially critical in highly dynamic environments such as those that exist in emergency hospitals. The primary inputs for this module are those from the Evaluation module and instantaneous data from RFID tags about the general hospital environment. Speci<sup>fi</sup>cally, through continual monitoring, the Evaluation module identi<sup>fi</sup>es knowledge de<sup>fi</sup>cits that may be present in the system. Solutions to address identi<sup>fi</sup>ed de<sup>fi</sup>cits are automatically generated with existing knowledge. Appropriate knowledge that addresses identi<sup>fi</sup>ed de<sup>fi</sup>cits are learned from the environment as well as input from the Evaluation module.

## 4.2. Heuristics

The proposed framework operates by <sup>fi</sup>rst observing the pro<sup>fi</sup>les of current patients and the corresponding tasks that need to be accomplished. The system extracts knowledge of these necessities and transfers this information to the optimization module. The decision variables include the temporal and spatial allocation of medical staff on duty based on the task structure for the set of current events, patients and staff allocations. The output is performance ef<sup>fi</sup>ciency and service quality that should be considered at both instant (short-term) and accumulated (long-term) levels. The general steps that are involved in this process can be summarized as follows:

1. Set length of time between evaluations at the top administrative level (T)

2. Set initial job allocations in all medical units

3. Repeat steps 4–11 until time T

4. $P L M _ { i } ( S , E , P , T ) | _ { \forall i \in N } \Rightarrow$ task allocation at the ith unit

5. Service begins. Specify local time threshold (τ). Set local time=0.

6. If $\cdot P e r f E \nu a l ( P L M _ { i } ( S _ { t } , E _ { t } , P _ { t } , T _ { t } ) ) \ll S ,$ go to step 8.

7. $\mathrm { ~ f ~ } t < \tau , \mathrm { g o ~ t o ~ s t e p ~ } 6 $

8. Calculate $\Xi _ { i } ( 0 \sim t )$ . Learn allocation/performance knowledge

9. I $^ { \ ' } E \{ \sum _ { i \ = \ 1 } ^ { N } \Xi _ { i } ( \Delta ( a l l o c a t i o n \ s t r a t e g y _ { i } ) ) \} <$ pre-determined threshold, go to 11

10. Else, go to step 4

11. Calculate $\sum _ { i \mathop { = } 1 } ^ { N } \overleftrightarrow { \sum } _ { i } \bigl ( \Delta ( a l l o c a t i o n ~ s t r a t e g y _ { i } ) \bigr )$ . Learn global knowl edge and suggest improved global PLM strategy

12. Go to step 1

$P L M _ { i } ( S , E , P , T ) | _ { \forall i \in N }$ in Step 4 represents general process and labor management (PLM) assignment based on the input information about S (staff), E (Equipment), P (Patient) and T (Task requirement). The last step (Step 12) enables repetition of the entire process over time and facilitates resetting the next evaluation time when necessary. While the input parameters are continuously monitored and measured at any speci<sup>fi</sup>c time t as $P e r f E v a l ( S _ { t } , E _ { t } , P _ { t } , T _ { t } ) )$ , new strategy and possible performance evaluations are estimated and compared to the current assignment strategy ${ E \{ \sum _ { i \mathrm { ~ = ~ } 1 } ^ { N } \Xi _ { i } ( \Delta ( a l l o c a t i o n ~ s t r a t e g y _ { i } ) ) \} }$ , where $\Xi _ { i } ( 0 \sim t )$ indicates <sup>ð Þð Þ</sup>the accumulated medical service provision at the ith medical unit during time t. If the bene<sup>fi</sup>t is large enough, the new strategy is adopted which then triggers a new cycle of set up, implementation, and learning thereafter. We also consider process and labor management in a health care institution from a global point of view so that not only the different local medical sections are optimized, but also the interactions and cooperation among these local operations are considered.

## 5. Health care management strategies

Public health care institutions are generally characterized by their medical staff taking on multiple tasks. For example, nurses are required to simultaneously take care of several patients and get involved in different kinds of tasks such as cleaning and preparing medical equipment. In a health care institution where appointment is required, uncertainty arising from dynamic medical service requirement is reduced to minimum. In an emergency clinic, on the other hand, the variance from unexpected service requirement is highly demanding. For instance, a patient with an emergency situation would need immediate treatment or patient without a pre-diagnosed ailment may demand extended time on diagnosis and treatment.

We divide the general health care work environment into four categories that are characterized by (1) whether medical staff takes on multiple tasks, and (2) whether the health care institution takes care of emergency situations (Fig. 3). We do not consider the cases where both single and multiple tasks are handled by medical staff when necessary under normal as well as emergency situations.

The medical labor resource is usually highly constrained in public health care institutions (Scenario III) primarily due to budgetary constraints. Consequently, the medical staff working at a public hospital is usually required to take on multiple tasks simultaneously and sometimes the pressure to get work done in less time than is ideally necessary can be very high. On the other hand, some privately operated health care providers don't require their medical personnel to simultaneously accomplish multiple tasks in order to maintain certain service quality and to reduce medical errors (Scenario I). These are generally supported through higher premiums from patients and by hiring a suf<sup>fi</sup>cient number of staff. Normally health care service providers without emergency obligations operate on schedules from prior appointments, where uncertainty from unexpected medical service requirements is low. Emergency rooms (Scenario IV) in a public hospital are characterized not only by a staff taking on multiple tasks but also by the increased uncertainty from patients' emergency issues. Private or premium emergency facilities (Scenario II) are usually equipped with suf<sup>fi</sup>cient number of staff to ensure service quality. We argue that although the categorization given above is not always 100%, where even the most expensive or exclusive private health care provider may require its staff to work on multiple tasks from time to time, it is more an exception than the norm.

We assume that the available resources in a health care institution are not unlimited for both medical equipment and personnel. This assumption is backed by the large number of heated debates on health care issues taking place across the world. Given limited resources, the work <sup>fl</sup>ow of health care management can be tailored toward either optimizing the ef<sup>fi</sup>ciency or optimizing the service quality. It is necessary to consider both ef<sup>fi</sup>ciency and quality optimization problems because their solutions don't usually converge and, as a result, the conditions under which and to what extent an RFID system should be adopted can be very different. We discuss this problem in the sections that follow.

![](/api/attachments/K22D9SUU/fulltext/images/15bbeba285358dd79be4d9018c58edc7d026bdbe85a282475feffc9447a8ba69.jpg)  
Fig. 3. Chart of scenarios

## 5.1. Efficiency maximization

With RFID tracking and tracing information on both medical equipment and service personnel, we are now able to dynamically optimize the health care service process to improve operational ef<sup>fi</sup>ciency. We consider N different types of health care service assignments in a health care institution of interest using a vector {Ω| $\left[ \Omega _ { 1 } , \Omega _ { 2 } , \cdots \Omega _ { N } \right] \}$ , where $\varOmega _ { n }$ represents a unique kind of assignment such as surgery equipment preparation, patient care, etc. If we have M medical staff who are in charge of completing these assigned tasks, the accumulated workload on these M staff can be represented by the vector $\{ \lambda | [ \lambda _ { 1 } , \lambda _ { 2 } , . . . \lambda _ { M } ] \}$ . Without any external help, these task assignments will be completed by the available medical staff.

$$
\sum_ {1} ^ {N} \Omega_ {n} = \sum_ {1} ^ {M} \lambda_ {m}\tag{1}
$$

Here, $\omega _ { n m }$ represents the mth staff's work load on the nth assignment so that $\sum { M } _ { } ^ { }$ . After training and routine performance evaluation on each medical staff, the medical staffs' ability on each individual assignment can be measured as:

$$
\left[ \begin{array}{l l l l} \Psi_ {1 1} & \Psi_ {1 2} & \dots & \Psi_ {1 M} \\ \Psi_ {2 1} & \Psi_ {2 2} & \dots & \Psi_ {2 M} \\ & & \dots \\ \Psi_ {N 1} & \Psi_ {N 2} & \dots & \Psi_ {N M} \end{array} \right]
$$

We normalize the medical staff's ability to perform certain assignment by approximating the time that each would take to complete the assigned task. For example, we assume that a nurse's ability to perform surgery is 0. This signi<sup>fi</sup>es that the time for a nurse to perform surgery would be in<sup>fi</sup>nite and that makes it impossible for the nurse to perform such a task assignment. On the other hand, the ability of a well-trained doctor to perform the same surgery task could be a number other than 0, making a doctor the proper candidate for surgery tasks. Another example is where both doctor and nurse are capable of performing surgery preparation, which may involve arranging equipment, sanitization and patient treatment. In this case, the capability of both doctor and nurse to perform such a task differs by their training and specialties such that a nurse may take less time to prepare for a surgery than a doctor. The normalization is on time such that for the same task, the longer it takes the less capable is the staff for that task.

## 5.1.1. Scenario I: single task, without uncertainty

In an idealistic situation without randomness and without multiple tasks, the optimization strategy to improve ef<sup>fi</sup>ciency is contained in the assignment matrix $| \omega | _ { N \times M }$ such that the accumulated time to <sup>fi</sup>nish all required assignments are minimized. So the optimization problem is formulated as:

$$
m i n \left\{\sum_ {n = 1} ^ {N} \sum_ {m = 1} ^ {M} \omega_ {n m} \right\}\tag{2}
$$

subject to:

$$
\sum_ {m = 1} ^ {M} \omega_ {n m} = \Omega_ {n} \lambda_ {m} = \sum_ {n = 1} ^ {M} \omega_ {n m} \leq \overline {{\lambda}} _ {m}\tag{3}
$$

4

$$
\sum_ {1} ^ {N} \Omega_ {n} = \sum_ {1} ^ {M} \lambda_ {m}\tag{5}
$$

where $\overline { { \lambda } } _ { m }$ indicates the mth medical personnel's work limit in a given time period such that $\begin{array} { r } { \mathrm { i f } \sum _ { n } ^ { N } \phantom { } _ { = 1 } \mathbf { 0 } _ { n m } > \overline { { \lambda } } _ { m } } \end{array}$ the service quality of this medical personnel decreases below acceptable level because of increased load and associated stress.

## 5.1.2. Scenario II: single task, with uncertainty

In a more dynamic health care working environment, such as the emergency room, unpredictable issues could demand more resources during certain points in time than that in an appointment-based system. With variance of service demand under consideration, we rewrite {Ω} as a stochastic process such that at a given time T, the actual service demand is the sum of the expectation Ω<sub>i</sub> and a perturbation $\varepsilon _ { i t } , [ \varOmega _ { 1 } +$ $\varepsilon _ { 1 T } , \Omega _ { 2 } + \varepsilon _ { 2 T } , . . . \Omega _ { N } + \varepsilon _ { N T } \big ] _ { t = T } ,$ or simply $[ \mathcal { \Omega } _ { 1 } ( t ) , \mathcal { \Omega } _ { 2 } ( t ) , . . . \mathcal { \Omega } _ { N } ( t ) ]$ <sub>t</sub>.

The ef<sup>fi</sup>ciency optimization problem at time t becomes:

$$
\min \left\{\sum_ {n = 1} ^ {N} \sum_ {m = 1} ^ {M} \omega_ {n m} (t) \right\}\tag{6}
$$

subject to:

$$
\sum_ {m = 1} ^ {M} \omega_ {n m} (t) = \Omega_ {n} (t)\tag{7}
$$

$$
\lambda_ {m} (t) = \sum_ {n = 1} ^ {N} \omega_ {n m} (t) \tilde {\leq} \overline {{\lambda}} _ {m}\tag{8}
$$

$$
\sum_ {1} ^ {N} \Omega_ {n} (t) = \sum_ {1} ^ {M} \lambda_ {m} (t)\tag{9}
$$

If the allocations are ef<sup>fi</sup>cient, we conclude that the system is ef<sup>fi</sup>cient. Because of unpredictability, expression (8) is a loose constraint, which signi<sup>fi</sup>es that under certain conditions such as when there is a surge of emergency issues, medical staff will need to work over their respective limits.

## 5.1.3. Scenario III: multiple tasks, without uncertainty

Public health care institutions are characterized by a high patient volume and high density work assignments on their medical staff who are required to simultaneously take on multiple tasks, which usually incur additional labor cost such as the transportation cost among different sites, setup cost and management cost. For instance, medical staff switch among different locations while simultaneously taking responsibility for multiple tasks. We consider the extra cost for the mth medical staff to take both the ith and the jth tasks as δ<sup>m</sup>. Health care work environment is also complicated by its inability to preassign necessary resource to each individual task. For example, medical equipment and service space are usually allocated on a <sup>fi</sup>rst come <sup>fi</sup>rst serve basis and even pre-assignments could change frequently due to resource constraints. Uncertainty from taking on multiple tasks therefore also depends on the resource constraints at a given time. The cost structure of taking on multiple tasks can therefore be represented as:

$$
\left[ \begin{array}{c c c c c} 0 & \delta_ {1 2} ^ {m} & \delta_ {1 3} ^ {m} & \dots & \delta_ {1 N} ^ {m} \\ 0 & 0 & \delta_ {2 3} ^ {m} & \dots & \delta_ {2 N} ^ {m} \\ & & & \dots & \delta_ {N - 1, N} ^ {m} \\ 0 & 0 & & \dots & 0 \end{array} \right] _ {t}\tag{10}
$$

If more than two tasks are considered simultaneously, the cost is the sum of all possible combinations. For example, if tasks i, j and k are carried out, it would cost $\delta _ { i j k } ^ { m } ( t )$ where $\delta _ { i j k } ^ { m } ( t ) = \delta _ { i j } ^ { m } ( t ) + \delta _ { i k } ^ { m } ( t ) + \delta _ { j k } ^ { m } ( t )$

The ef<sup>fi</sup>ciency optimization problem with multiple tasks under concern is:

$$
m i n \Bigg \{\sum_ {n = 1} ^ {N} \sum_ {m = 1} ^ {M} \left[ \boldsymbol {\omega} _ {n m} + \sum_ {j = 1} ^ {N} \delta_ {n j} ^ {m} (t) \right] \Bigg \}\tag{11}
$$

subject to:

$$
\sum_ {m = 1} ^ {M} \omega_ {n m} = \Omega_ {n}\tag{12}
$$

$$
\lambda_ {m} = \sum_ {n = 1} ^ {N} \left[ \omega_ {n m} + \sum_ {j = 1} ^ {n} \delta_ {n j} ^ {m} (t) \right] \leq \overline {{\lambda}} _ {m}\tag{13}
$$

$$
\sum_ {1} ^ {N} \Omega_ {n} = \sum_ {1} ^ {M} \lambda_ {m} - \sum_ {m = 1} ^ {M} \sum_ {n = 1} ^ {N} \sum_ {j = 1} ^ {N} \delta_ {n j} ^ {m} (t)\tag{14}
$$

5.1.4. Scenario IV: multiple tasks, with uncertainty

Featured with both multiple task work load and a high level of uncertainty, emergency service in a public hospital is the worst-case scenario in our discussion. With both dynamic medical service demand and health care staff taking on multiple tasks, our ef<sup>fi</sup>ciency optimization problem becomes:

$$
\min \left\{\sum_ {n = 1} ^ {N} \sum_ {m = 1} ^ {M} \left[ \omega_ {n m} (t) + \sum_ {j = 1} ^ {N} \delta_ {n j} ^ {m} (t) \right] \right\}\tag{15}
$$

subject to:

$$
\sum_ {m = 1} ^ {M} \omega_ {n m} (t) = \Omega_ {n} (t)\tag{16}
$$

$$
\lambda_ {m} (t) = \sum_ {n = 1} ^ {N} \left[ \omega_ {n m} (t) + \sum_ {j = 1} ^ {N} \delta_ {n j} ^ {m} (t) \right] \tilde {\leq} \overline {{\lambda}} _ {m}\tag{17}
$$

$$
\sum_ {1} ^ {N} \Omega_ {n} (t) = \sum_ {1} ^ {M} \lambda_ {m} (t) - \sum_ {m = 1} ^ {M} \sum_ {n = 1} ^ {N} \sum_ {j = 1} ^ {N} \delta_ {n j} ^ {m} (t)\tag{18}
$$

Proposition 1. Under efficiency optimization, both routine-based management and adaptive learning-based intelligent system perform the same under Scenarios I and II; adaptive learning-based intelligent system outperforms routine-based management under Scenarios III and IV.

Most existing health care services adopt rule-based management strategies under which pre-determined procedures are strictly followed to achieve necessary medical objectives. To prevent complexities and therefore confusion, most medical staff assignment strategies carry a similar rule that is generally not <sup>fl</sup>exible. Comparing results from rulebased management to those from the proposed dynamic process management scheme, with or without dynamic issues, it is readily observed that both management strategies result in similar performance without multiple tasks. It is a direct consequence of eliminating uncertainty associated with unde<sup>fi</sup>ned tasks from happening by assuming that we can accurately and completely categorize the possible assignments in a given health care work environment. Therefore, all possibilities would be captured in a prede<sup>fi</sup>ned assignment framework such that uncertainty is present only in work load assignments. Ef<sup>fi</sup>ciency maximization rules would assign the most suitable personnel on each assignment at any time point just as in dynamic allocation management. It can also be explained by the solutions from expressions (2), (3), (4) and (5) by assigning the most capable medical personnel to each task.

Proposition 1 also implies that RFID has a great potential to improve performance ef<sup>fi</sup>ciency in most public health care institutions that are characterized by heavy duty work load and high service demand. It is obvious here that without RFID instantaneous information, the additional cost for medical staff to take on multiple tasks cannot be accurately captured on a real-time basis and as a result, no better decision could possibly be made without such re<sup>fi</sup>ned information. Arti<sup>fi</sup>cial intelligence-assisted dynamic process management has obvious advantages here for being able to not only monitor item-level process information on site but also analyze and utilize such information to improve system effectiveness and overall ef<sup>fi</sup>ciency.

## 5.2. Service quality/satisfaction maximization

In general, improving service quality, patient satisfaction, or ef<sup>fi</sup>ciency does not necessarily lead to the same allocation solution for health care service providers. In many situations, such as in private hospitals or service oriented institutions, overall service quality generally takes higher priority than ef<sup>fi</sup>ciency.

Consider the service quality, $\theta _ { n m } ,$ of the nth task performed by the mth medical personnel as a function of accumulated tasks this person has completed, such that $\begin{array} { r } { \theta _ { n m } = \Theta ( \sum _ { i = 1 } ^ { N } \omega _ { i m } \mid _ { n \neq i } ) } \end{array}$ . Generally speak-<sup>j</sup>ing, the more tasks a person works on, the lower the overall quality of the resulting work performance due to fatigue or complications arising from simultaneously dealing with multiple tasks. For modeling purpose, we could consider this problem in a discrete format or in a continuous one. The example that we discussed in the previous section considers service quality in a discrete manner where the service quality decreases to certain levels over prede<sup>fi</sup>ned thresholds. We could also consider service quality in a continuous form.

$$
\theta_ {n m} = e ^ {k _ {n} \left(1 - \sum_ {i = 1} ^ {N} \omega_ {i m} | _ {n \neq i}\right)}\tag{19}
$$

where $k _ { n }$ is a dummy variable that indicates how workload affects service quality for the nth job. In the context of Scenario IV and in both discrete and continuous forms, we model the service quality maximization problem as:

$$
\max \left\{\sum_ {n = 1} ^ {N} \sum_ {m = 1} ^ {M} \theta_ {n m} (t) \right\}\tag{20}
$$

subject to:

$$
\theta_ {n m} = \Theta \left(k _ {n}, \sum_ {i = 1} ^ {N} \left[ \omega_ {i m} | _ {n \neq i} + \sum_ {j = 1} ^ {N} \delta_ {i j} ^ {m} (t) \right]\right)\tag{21}
$$

$$
\sum_ {m = 1} ^ {M} \omega_ {n m} (t) = \Omega_ {n} (t)\tag{22}
$$

$$
\lambda_ {m} (t) = \sum_ {n = 1} ^ {N} \left[ \omega_ {n m} (t) + \sum_ {j = 1} ^ {N} \delta_ {n j} ^ {m} \right] \tilde {\leq} \overline {{\lambda}} _ {m}\tag{23}
$$

$$
\sum_ {n = 1} ^ {N} \Omega_ {n} (t) = \sum_ {m = 1} ^ {M} \left[ \lambda_ {m} (t) - \sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {N} \delta_ {i j} ^ {m} \right]\tag{24}
$$

Proposition 2. Simultaneous involvement of medical personnel in multiple tasks deteriorates the overall efficiency and overall service quality in health care institutions.

With respect to ef<sup>fi</sup>ciency, it is clear that taking on multiple tasks always involves related additional work $\sum _ { \substack { \{ m , n \} } } \delta _ { m n } ( t )$ that is a direct <sup>f g ð Þ</sup>result of additional movement of staff and medical equipment, additional required work for coordination, and additional setup work for the medical staff. The service quality also deteriorates due to the possibility of an over-worked staff that likely results in more complications in the work environment and therefore a higher possibility for medical errors.

Proposition 3. Under medical service quality optimization, both routinebased management and adaptive learning-based intelligent system perform the same under Scenario I; adaptive learning-based intelligent system outperforms routine-based management under Scenarios II, III and IV.

The quality of medical service is very closely related to operational ef<sup>fi</sup>ciency when constraints are present. Although the solution that optimizes one doesn't necessarily optimize the other, generally speaking if one can improve ef<sup>fi</sup>ciency, it has a direct corresponding effect on service quality. Proposition 1 states that dynamic medical process management is advantageous to the traditional routine-based process management under Scenarios III and IV, while both performs equal under Scenarios I and II. Because Scenario I has no modeled uncertainty from emergency issues or from being involved in multiple tasks, there is very little space for both ef<sup>fi</sup>ciency and quality improvement by switching to dynamic process management from a static routine-based management scenario. Dynamic process management results in improved medical service quality under Scenario II since a medical staff's possibility of exceeding their work limit can be easily prevented by switching job assignment to another quali<sup>fi</sup>ed staff who is yet to reach the assigned work limit for compromised (i.e., less than peak) performance. On the other hand, although not necessarily ef<sup>fi</sup>cient, the quality of medical service can be guaranteed in premium health care institutions.

We have thus far considered cases with the objective of ef<sup>fi</sup>ciency maximization or quality optimization. A mixed solution can also be reached to balance ef<sup>fi</sup>ciency and quality by appropriately setting the objective functions in the adaptive learning module. Due to the increase in complexity for accurate analyses of the mixed solutions, we perform simulation analysis to understand its dynamics.

In summary, the above scenarios are based on perfect information, which is enabled by 100% accurate RFID item-level information on physical assets, medical staff and patients. With such perfect information and dynamic process and labor management, the system is able to analyze and recommend an optimal solution (or semioptimal solution with computational limit) so that a maximum/semimaximum working ef<sup>fi</sup>ciency can be maintained. As a result, the industry bene<sup>fi</sup>ts by reduced labor cost, increased ef<sup>fi</sup>ciency and overall improved health care service quality.

Without perfect information, routines are made and generally updated based on purely historical data without considering the current state of the system. As a consequence, ef<sup>fi</sup>ciency, service quality, and satisfaction are prone to be compromised. In the next section, we analyze the potential bene<sup>fi</sup>ts of scenarios incorporating RFID item-level information in health care compared to those without RFID tracking/tracing information. We provide managerial insights on conditions and strategies of RFID implementation in what follows.

## 5.3. Data and strategy analysis

We evaluate the above-proposed management strategies in a small clinic with one doctor and two nurses on four selected job assignments: prior preparation, patient diagnostic interview, treatment, posterior medical treatment. Normally, prior preparation and posterior medical treatment are serviced by nurses, although the doctor is well quali<sup>fi</sup>ed (but may not be as experienced as the nurses) for these tasks. Diagnostic interview and medical treatment are performed by the doctor while nurses may provide assistance for these two tasks. The evaluation is based on 80 normalized working hours, during which time uncertainties from emergency issues and from multiple tasks are captured. In order to <sup>fi</sup>nd the working conditions and the extent to which the proposed dynamic labor management could bene<sup>fi</sup>t the practitioner, we study the four scenarios discussed before: single task with prior appointments, single task with emergency requests, multiple tasks with prior appointments and multiple tasks with emergency requests.

![](/api/attachments/K22D9SUU/fulltext/images/becef817f2d68591b448cfb1e8ef03c596ba1fb9ea9f3f1c2589515cc7db611e.jpg)  
Absolute value of workload improvement

Accumulated workloads under scenario III & IV  
![](/api/attachments/K22D9SUU/fulltext/images/ded5f026b784aa015d4c03d62d35d9eef77631ee99cb36423f9955decdaa405d.jpg)

![](/api/attachments/K22D9SUU/fulltext/images/e2daf20bfef504d93dc9d54ce9332b677e8c20160a777a0b9d50519f1c21a7a2.jpg)

Percentage of improvement  
![](/api/attachments/K22D9SUU/fulltext/images/3c9784f62acaa977fbec09f6c1a82372a8f9a80fbe7f0750115aa4d651db15b5.jpg)  
Fig. 4. Accumulated workload under Scenarios I, II, III and IV (with uncertainty from both emergency issues and from multiple tasks). Absolute value and percentage of ef<sup>fi</sup>ciency improvement of implementing dynamic process management over traditional routine-based management under Scenarios III and IV.

Fig. 4 shows the accumulated workload under Scenarios I, II, III and IV as well as the absolute value and percentage of ef<sup>fi</sup>ciency improvement in implementing dynamic process management over traditional routine-based management under Scenarios III and IV. Fig. 4 shows that the performance of routine-based and RFID dynamic process and labor management renders the same ef<sup>fi</sup>ciency (Propoposition 1). While we test the performance differentiation on the amplitude of uncertainty by considering more unexpected issues, we <sup>fi</sup>nd that the more stressful (high workload and high uncertain medical issues) and constrained the situation is, the more ef<sup>fi</sup>ciency improvement the health care institution could possibly gain. The performance improvement is 17.05% in our experiment when medical staff is required to simultaneously take on multiple tasks resulting in double the normal work load. We argue that at a larger health care institution, the bene<sup>fi</sup>t could be more than that in a small clinic environment where the solution is more continuous than discrete such that the space for improvement is even larger. Considering the uncertainty from emergency issues and simultaneous involvement in multiple tasks separately, we further illustrate the individual effects on performance improvement and total workload from these two randomness respectively in Fig. 5, where the X axis indicates the level of randomness from emergency issues and the Y axis indicates the one from multiple tasks.

Fig. 6 shows the absolute value and percentage of ef<sup>fi</sup>ciency improvement by implementing dynamic process management over traditional routine-based management under Scenarios III and IV with respect to the two kinds of uncertainties arising from emergency issues and simultaneous involvement in multiple tasks separately.

In summary, Fig. 7 illustrates the four scenarios of health care work conditions that we considered, the two strategies (routine-based and dynamic management) and their implementation bene<sup>fi</sup>ts as well as challenges.

## 6. Discussion

Health care process and labor management problems have unique characteristics given that they occur under highly dynamic medical environments. The primary characteristic that differentiates this scenario is the fact that human lives are at stake with every patient who walks in and every decision that is made in these work environments. Although traditional static routine-based management has its advantages and is merits, we develop an innovative mechanism based on instantaneous item-level information and realtime coordination to generate and maintain ef<sup>fi</sup>cient process and labor management in a highly constrained, dynamic, and stressful health care environment.

While RFID tags are slowly becoming popular in heath care settings, their unique applications in this <sup>fi</sup>eld beg to be explored based on their unique characteristics (such as their ability to provide instantaneous instance-level information). We propose an adaptive learning framework utilizing this technology to facilitate the health care process and labor management decisions. We simultaneously incorporate RFID-enabled process mining and process and labor management in a health care environment where more <sup>fl</sup>exibility in dealing with multiple tasks and readiness to handle emergency situations are necessary.

We study this framework to understand its dynamics vis-à-vis a static process and labor management scenario under different health care settings that are characterized by uncertainties from emergency issues

## Accumulated workloads under Routine based II

![](/api/attachments/K22D9SUU/fulltext/images/1aaa90cec2d6a3c098f980cda6fcfdfc03751ea364dc5d5b9eba3fa9d2545e0c.jpg)

Accumulated workloads under Routine based IV  
![](/api/attachments/K22D9SUU/fulltext/images/9dc6f05d5aee9e59d4069eaa20560288603827eefec0008bf0ae0aa107aafa8c.jpg)

## Accumulated workloads under Dynamic management III

![](/api/attachments/K22D9SUU/fulltext/images/cccd830e26422c5e135d67f796aa4829184e2ad66e0d56694963b4357df92ff4.jpg)

Accumulated workloads under Dynamic management IV  
![](/api/attachments/K22D9SUU/fulltext/images/e23b7d32c6d891a94eb90ea93cadafaef09f2eca8d27cb587c134adacc6a98a5.jpg)  
Fig. 5. Accumulated workload under Scenarios III and IV, with dynamic process management and traditional routine-based management. Randomness from emergency issues and multiple tasks are considered separately.

![](/api/attachments/K22D9SUU/fulltext/images/9c5e81159af0f664f9db72279d1f87fd40fc4b4131ede81a923973f884c43616.jpg)

![](/api/attachments/K22D9SUU/fulltext/images/a6e350d9f8d5b2e7732fe47a42f4f6c3b4d1030f853c83dae6a2c2e456cd0e0d.jpg)

![](/api/attachments/K22D9SUU/fulltext/images/109c4b8e52363e8fe130d5ace44056593800dfddde663ef25444f0c893865aae.jpg)

![](/api/attachments/K22D9SUU/fulltext/images/1a0212a7b72025f7f7db4edcb27c52c1a09a052797bdc7333f56bed7ff954243.jpg)  
Fig. 6. Absolute value and percentage of ef<sup>fi</sup>ciency improvement of implementing dynamic process management over the traditional routine-based management under Scenarios III and IV. Randomness from emergency issues and multiple tasks are considered separately

and workload randomness due to simultaneous involvement in multiple tasks. Our model analysis concurs with our data analysis in that public health care institutions would bene<sup>fi</sup>t more from adopting the proposed real-time process and labor management than private or premium health care institutions since essential resources (especially human labor and equipment) in public hospitals are highly constrained.

We considered ef<sup>fi</sup>ciency maximization and service quality enhancement. While the proposed framework is able to adjust itself towards a preset objective that leads to a mixed strategy with both ef<sup>fi</sup>ciency and service quality balanced, increased computational complexity prevented us from accurately analyzing such mixed strategy. It is left as an exercise for another study.

<table><tr><td></td><td>Examples</td><td>Characteristics</td><td>Routine-Based Process Management</td><td>RFID Dynamic Process Management</td></tr><tr><td>Scenario I</td><td>Premium healthcare institutions</td><td>Appointment-based, single task, sufficient staffing</td><td>Both efficiency and service can be maintained</td><td>No difference with Routine-based process management</td></tr><tr><td>Scenario II</td><td>Premium emergency rooms</td><td>Emergency issues, single tasks (multiple tasks when necessary), sufficient staffing</td><td>Both efficiency and service can be maintained, with small possibility of low service quality with certain emergency issues</td><td>No efficiency improvement; service quality improvement is marginal</td></tr><tr><td>Scenario III</td><td>Public hospitals, under-staffed private clinics</td><td>Appointment-based, multiple tasks, staffing on the edge</td><td>Hard to manage efficiency, certain service quality maintained</td><td>Improvement on both efficiency and service quality</td></tr><tr><td>Scenario IV</td><td>Public emergency rooms</td><td>Emergency issues, multiple tasks, staffing on the edge</td><td>Hard to manage efficiency, service quality not guaranteed</td><td>Improvement on both efficiency and service quality</td></tr></table>

Fig. 7. Scenarios of health care working conditions, strategies, and implementation challenges.

## References

[1] R. Agrawal, D. Gunopulos, F. Leymann, Mining process models from work<sup>fl</sup>ow logs, Proceedings of the Sixth International Conference on Extending Database Technology (1998) 469–483.

[2] E. Ammenwerth, S. Graber, G. Herrmann, T. Burkle, Evaluation of health information systems — problems and challenges, International Journal of Medical Informatics 71 (2–3) (2003) 125–135.

[3] M. Berg, Patient care information systems and health care work: a sociotechnical approach, International Journal of Medical Informatics 55 (2) (1999) 87–101.

[4] M. Berg, C. Langenberg, I.V.D. Berg, J. Kwakkernaat, Considerations for sociotechnical design: experiences with an electronic patient record in a clinical context, International Journal of Medicine Informatics 52 (1998) 243–251.

[5] J.E. Cook, A.L. Wolf, Discovering models of software processes from event-based data, ACM Transactions on Software Engineering and Methodology 7 (3) (1998) 215–249.

[6] J.E. Cook, A.L. Wolf, Software process validation: quantitatively measuring the correspondence of a process to a model, ACM Transactions on Software Engineering and Methodology 8 (2) (1999) 147–176.

[7] A. Friedman, D.S. Comford, Computer systems development: history, organization and implementation, Wiley, 1989.

[8] W. Hersh, Health care information technology: progress and barriers, Journal of the American Medical Association 292 (18) (2004) 2273–2274.

[9] E. Mumford, M. Weir, Computer Systems in Work Design: the ETHICS Method, Wiley, 1979.

[10] S. Piramuthu, Protocols for tag/reader authentication, Decision Support Systems 43 (3) (2007) 897–914.

[11] S. Piramuthu, Lightweight cryptographic authentication in passive RFID-tagged systems, IEEE Transactions on Systems, Man, and Cybernetics - Part C 38 (3) (2008) 360–376.

[12] J.C. Prather, D.F. Lobach, L.K. Goodwin, J.W. Hales, M.L. Hage, W.E. Hammond, Medical data mining: knowledge discovery in a clinical data warehouse, Proceedings of the AMIA Annual Fall Symposium (1997) 101–105.

[13] S. Seidman, P. Ruggera, R. Brockman, B. Lewis, J. Guag, M. Shein, W. Clement, J. Kippola, D. Digby, C. Barber, D. Huntwork, Electromagnetic compatibility of

pacemakers and implantable cardiac de<sup>fi</sup>brillators exposed to RFID readers, International Journal of Radio Frequency Identi<sup>fi</sup>cation Technology and Applications 3 (2007) 237–246.

[14] S. Seidman, R. Brockman, B. Lewis, M. Shein, In vitro tests reveal sample radio frequency identi<sup>fi</sup>cation readers inducing clinically signi<sup>fi</sup>cant electromagnetic interference to implantable pacemakers and implantable cardioverter–de<sup>fi</sup>brillators, HeartRhythm 7 (1) (2010) 99–107.

[15] R.v.d. Togt, E.J.v. Lieshout, R. Hensbrock, E. Beinat, J.M. Binnekade, P.J.M. Bakker, Electromagnetic interference from radio frequency identi<sup>fi</sup>cation inducing potentially hazardous incidents in critical care medical equipment, Journal of the American Medical Association 299 (24) (2008) 2884–2890.

[16] Y.-J. Tu, W. Zhou, S. Piramuthu, Identifying RFID-embedded objects in pervasive healthcare applications, Decision Support Systems 46 (2) (2009) 586–593.

[17] W.S. Yang, S.Y. Hwang, A process-mining framework for the detection of healthcare fraud and abuse, Expert Systems with Applications 31 (1) (2005) 56–68.

[18] W. Zhou, RFID and item-level visibility, European Journal of Operational Research 198 (1) (2009) 252–258

[19] W. Zhou, Y.-J. Tu, S. Piramuthu, RFID-enabled item-level retail pricing, Decision Support Systems 48 (1) (2009) 169–179.

Wei Zhou received his Ph.D. in Information Systems from the University of Florida in 2008. He is Assistant Professor of Information Systems and Technologies and a member of the RFID European Lab at ESCP Europe. His research interests include RFID-enabled item-level information visibility, Internet advertising, and knowledge-based learning systems. His work has appeared in European Journal of Operational Research, IEEE Transactions on Geosciences and Remote Sensing, International Journal of Electronic Commerce, and Optical Engineering.

Selwyn Piramuthu is Professor of Information Systems at the University of Florida. He is a member of the RFID European Lab at ESCP Europe. His research interests include RFID systems, pattern recognition and its application in supply chain management, computer-aided manufacturing, and <sup>fi</sup>nancial credit-risk analysis
