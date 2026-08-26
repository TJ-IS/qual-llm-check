---
otero_id: 8826
otero_key: "VGBHZBCU"
title: "Retrieving batch organisation of work insights from event logs"
authors: "Niels Martin; Marijke Swennen; Benoît Depaire; Mieke Jans; An Caris; Koen Vanhoof"
year: "2017"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2017.02.012"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Retrieving batch organisation of work insights from event logs

Niels Martin\*, Marijke Swennen, Benoît Depaire, Mieke Jans, An Caris, Koen Vanhoof

Hasselt University, Agoralaan Building D, Diepenbeek 3590, Belgium

## A R T I C L E I N F O

Available online xxxx

Keywords: Batch processing Event log Event log insights Process mining Business process management Process metrics

## A B S T R A C T

Resources can organise their work in batches, i.e. perform activities on multiple cases simultaneously, concurrently or intentionally defer activity execution to handle multiple cases (quasi-) sequentially. As batching behaviour influences process performance, efforts to gain insight on this matter are valuable. In this respect, this paper uses event logs, data files containing process execution information, as an information source. More specifically, this work (i) identifies and formalises three batch processing types, (ii) presents a resource-activity centered approach to identify batching behaviour in an event log and (iii) introduces batch processing metrics to acquire knowledge on batch characteristics and its influence on process execution. These contributions are integrated in the Batch Organisation of Work Identification algorithm (BOWI) which is evaluated on both artificial and real-life data.

© 2017 Elsevier B.V. All rights reserved

## 1. Introduction

Business processes are composed of a series of connected activities executed by resources. Resources, such as process participants or equipment [1], are assigned to activities and typically carry these out on multiple cases such as files or products. Assuming that arriving cases are handled immediately when the resource becomes available is an undue simplification of reality. Employees might deem it more eficient to accumulate files and treat the entire stack later or machines can process multiple products at the same time. This type of resource behaviour is referred to as batch processing.

While the occurrence of batch processing might be readily observable for passive resources such as machines, it is typically less straightforward to determine how human resources, or active resources [1], organise their work. The latter is especially the case for processes in which staff members have a lot of freedom to arrange their tasks as they desire. Direct observation of staff members’ behaviour has limitations as it is both time-consuming and the Hawthorne effect can cause observed behaviour to deviate from real behaviour when humans know they are being observed [2]. Consequently, investigating the use of more readily available information sources is valuable, In this respect, event logs containing process execution information can be analysed, which belongs to the process mining domain. While batch processing is studied widely in the operations management, operations research literature and, to a lesser extent, the process modelling domain, limited attention is attributed to this topic in process mining.

This paper is the first paper to systematically analyse batching behaviour using an event log. More specifically, the key contributions of this paper are threefold. Firstly, three types of batch processing are distinguished and formalised. Secondly, a resource-activity centered approach is presented to identify these batch processing types from an event log. Finally, batch processing metrics are defined to describe the identified batches and the implications of batching on process execution. These contributions are included in the Batch Organisation of Work Identification algorithm (BOWI). Even though the contributions of this paper are of general interest, they are especially useful for business processes in which human resources have significant freedom in their work organisation. As extensive observations would, for instance, be required in such contexts, using the proposed technique allows companies to gain insight in batching behaviour from event data.

The current paper is situated at the intersection between Business Process Management and process mining, which corresponds to one of the focal points of this special issue. More specifically, the generated insights in batching behaviour will support process modelling activities and decision-making within the BPM life cycle [1]. Process modelling is facilitated as event log analysis can provide suitable values for parameters such as the batch size. Integrating batching behaviour will lead to more realistic process models which can, for instance, be used for simulation purposes. Simulation models serve as a decision support tool as it enables organisations to evaluate policy alternatives prior to implementation [3]. Besides shouldering process modelling, BOWI also provides direct support for decisionmaking. The algorithm allows companies to judge the desirability of batching behaviour by showing its influence on process performance. Consequently, a company can determine whether batching behaviour should be encouraged or discouraged. Besides positioning it in the BPM life cycle, this work can also be framed within the BPM use case extend model as it leverages resource information in the event log, which is useful to extend a process model [4].

The paper is structured as follows. Section 2 presents a running example and defines the three types of batch processing. The BOWIalgorithm is outlined in Section 3, after which it is evaluated on both artificial and real-life data in Section 4. Finally, related work, the algorithm’s limitations and conclusions are presented in Sections 5, 6 and 7, respectively.

## 2. Preliminaries

This section presents some preliminary topics that will be used in the remainder of this paper. A running example is introduced in Section 2.1 and three batch processing types are distinguished in Section 2.2.

## 2.1. Running example

Throughout this paper, a simplified process at the emergency department of a hospital will serve as a running example. The process model, annotated with all assumed parameters, is visualised in Fig. 1. After a patient registers at the reception (R), an initial triage and assessment by a doctor follows (T). Next, a patient either (i) undergoes an X-ray examination (X) or (ii) has laboratory tests performed on his blood samples (L) and is subjected to an MRI scan (M). When the required tests are completed, the patient discusses the further treatment with a medical specialist (S) after which the patient checks out (C). All time units are expressed in minutes and patient interarrival times and activity durations are assumed to follow an exponential and triangular distribution, respectively.

## 2.2. Batch processing type definition

Batch processing is defined as a type of work organisation in which a resource executes a particular activity on multiple cases simultaneously or concurrently, or intentionally defers activity execution to handle multiple cases (quasi-) sequentially. As in Martin et al. [5], three batch types are distinguished: simultaneous, concurrent and sequential batch processing. To exemplify the difference between these types, Fig. 2 shows the activities executed for six patients, where an activity is always executed by the same resource across all cases.

• Sequential batch processing. Activity instances are in a sequential batch when a resource intentionally defers the execution of this activity such that multiple cases can be handled (almost) immediately after each other. Consequently, all cases included in a batch need to be present at the activity before the resource starts processing the batch’s first case. The latter distinguishes sequential batch processing from mere queue handling, stressing its intentional nature. In Fig. 2, the initial assessment by a doctor takes place in sequential batches. Given the doctor’s busy schedule, he occupies himself with other tasks until several patients need to undergo an initial assessment, after which they are handled sequentially.

• Simultaneous batch processing. Activity instances are in a simultaneous batch when they are executed by the same resource for distinct cases at exactly the same time. For example: blood samples from several patients can be analysed in the same run, as shown in Fig. 2.

• Concurrent batch processing. Activity instances are in a concurrent batch when they are executed by the same resource for distinct cases partially overlapping in time. This indicates that the resource can handle multiple cases at the same time, but is flexible as it is not required that processing starts and ends at the same time for all cases. In Fig. 2, registrations and checkouts illustrate different types of concurrent batch processing, because, e.g., the receptionist already starts registering the next patient while the current patient is filling out a drug allergy form which is required to finish his registration.

The above batch processing types are largely consistent with Wu [6], where simultaneous and sequential batch processing correspond to the concepts of parallel and serial process batches, respectively. Concurrent batch processing is not included in Wu [6]. In operations management literature, batch processing is commonly referred to as the intermittent production of a particular type of product [7,8], where production volumes are situated between a job shop setting with small volumes and mass production [7].

## 3. Batch organisation of work identification algorithm

This section proposes the Batch Organisation of Work Identification Algorithm (BOWI), which generates insights in batching behaviour from an event log. A general overview is presented in Section 3.1. Afterwards, Sections 3.2–3.6 present the algorithm in more detail. In Section 3.7, the implementation of the algorithm is briefly discussed.

## 3.1. General overview

As shown in Fig. 3, BOWI’s input is an event log. This event log, consisting of atomic events, is converted to an activity log by mapping start events to their corresponding complete events. This activity log is restructured in a resource-activity matrix (RAM), where each cell contains activity instances of a particular resource-activity combination. Using the RAM as an input, a batching matrix (BM) is

![](/api/attachments/VGBHZBCU/fulltext/images/7f2f2e16279e737b09b5f60c20fe63d207368bda1b880d76fd64d75d5aedf709.jpg)  
Fig. 1. Process model running example.

Please cite this article as: N. Martin et al., Retrieving batch organisation of work insights from event logs, Decision Support Systems (2017), http://dx.doi.org/10.1016/j.dss.2017.02.012

<table><tr><td>patient 1</td><td>R</td><td>T</td><td>L</td><td>M</td><td>S</td><td>C</td><td></td><td></td></tr><tr><td>patient 2</td><td>R</td><td>T</td><td>X</td><td>S</td><td>C</td><td></td><td></td><td></td></tr><tr><td>patient 3</td><td>R</td><td>T</td><td>L</td><td>M</td><td>S</td><td>C</td><td></td><td></td></tr><tr><td>patient 4</td><td>R</td><td>T</td><td>L</td><td></td><td>M</td><td>S</td><td>C</td><td></td></tr><tr><td>patient 5</td><td>R</td><td>T</td><td>L</td><td></td><td></td><td>M</td><td>S</td><td>C</td></tr><tr><td>patient 6</td><td>R</td><td>T</td><td>X</td><td>S</td><td>C</td><td></td><td></td><td></td></tr></table>

Resources per activity: R: receptionist 1, T: doctor 1, L: lab assistant 1, M: nurse 1, X: nurse 2, S: specialist 1, C: receptionist 2

Fig. 2. Conceptual representation of six cases executed in the running example process.

created for each batch processing type. A BM mimics the structure of the RAM, but groups activity instances that are executed in the type of batch under consideration. This information is used to calculate batch processing metrics such as the batch size.

## 3.2. Event log requirements

BOWI requires an event log, composed of ordered events related to a particular case and activity, as input. For each event, the timestamp, executing resource and transaction type needs to be recorded. Two transaction types have to be registered for BOWI: start and complete. Moreover, each start event should have an accompanying complete event with the same resource being associated to both events.

While Table 1 illustrates the event log structure, its key characteristics can be formalised as follows:

Definition 1 (Event log characteristics). Let E be the set of all events included in event log E. Moreover, let $\forall e \in { \mathcal { E } } \colon$

$\# _ { c a s e } ( e )$ represents the case associated to event e

$\# _ { a c t i v i t y } ( e )$ represents the activity associated to event e

$\# _ { r e s o u r c e } ( e )$ represents the resource associated to event e

$\# _ { t i m e } ( e )$ represents the timestamp associated to event e

$\# _ { t r a n s } ( e )$ represents the transaction type associated to event e

Then, in this paper, $\forall e ~ \in ~ \mathcal { E } ~ : ~ \# _ { c a s e } ( e ) ~ \neq \bot ~ \land \# _ { a c t i v i t y } ( e ) ~ \neq \bot$ $\wedge \# _ { t e s o u r c e } ( e ) ~ \neq \perp \quad \wedge \# _ { t i m e } ( e ) ~ \neq \perp \quad \wedge \# _ { t r a n s } ( e ) ~ \in ~ \{ s t a r t , c o m p l e t e \} .$ where ⊥ represents a null value. Moreover, every start event should have an accompanying complete event, i.e. $\forall e _ { 1 } ~ \in ~ \mathcal { E } , \exists e _ { 2 } ~ \in ~ \mathcal { E } ~ :$ $\# _ { c a s e } ( e _ { 1 } ) = \# _ { c a s e } ( e _ { 2 } ) \wedge \# _ { a c t i v i y } ( e _ { 1 } ) = \# _ { a c t i v i y } ( e _ { 2 } ) \wedge \# _ { r e s o u r c e } ( e _ { 1 } ) =$ $\# _ { r e s o u r c e } ( e _ { 2 } ) \wedge \# _ { t i m e } ( e _ { 1 } ) \leq \# _ { t i m e } ( e _ { 2 } ) \wedge \# _ { t r a n s } ( e _ { 1 } ) = s t a r t \wedge \# _ { t r a n s } ( e _ { 2 } ) =$ complete. When $| e _ { 2 } | > 1$ , i.e. when more than one event satisfies the conditions outlined for $e _ { 2 } ,$ , it is required that $| e _ { 1 } | = | e _ { 2 } |$

## 3.3. Activity log creation

To retrieve batch processing insights, the atomic events in the event log are converted to activity instances, i.e. the execution of a particular activity by a particular resource on a particular case. To this end, each start event is mapped on its corresponding complete event, i.e. the complete event that is associated to the same case, activity and resource in the event log. When multiple start and complete events are present for a particular case, activity and resource combination, the first occurring unmapped start event will iteratively be mapped to the first occurring unmapped complete event. The activity log obtained from the event log in Table 1 is shown in Table 2.

![](/api/attachments/VGBHZBCU/fulltext/images/4dbb418e4d3a43f420aadd36b8a8b16f750ed61123d393ee3e68a570e6e366e4.jpg)  
Fig. 3. Overview of BOWI.

Please cite this article as: N. Martin et al., Retrieving batch organisation of work insights from event logs, Decision Support Systems (2017), http://dx.doi.org/10.1016/j.dss.2017.02.012

N. Martin et al. / Decision Support Systems xxx (2017) xxx–xxx

Table 1  
Illustration of event log structure.

<table><tr><td>Case id</td><td>Timestamp</td><td>Activity</td><td>Transaction type</td><td>Resource</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>Patient 22</td><td>03/01/2016 11:14:41</td><td>X-ray</td><td>Start</td><td>Nurse 2</td></tr><tr><td>Patient 22</td><td>03/01/2016 11:22:37</td><td>X-ray</td><td>Complete</td><td>Nurse 2</td></tr><tr><td>Patient 25</td><td>03/01/2016 11:22:37</td><td>X-ray</td><td>Start</td><td>Nurse 2</td></tr><tr><td>Patient 34</td><td>03/01/2016 11:22:54</td><td>Blood test</td><td>Start</td><td>Lab assistant 1</td></tr><tr><td>Patient 42</td><td>03/01/2016 11:25:17</td><td>Registration</td><td>Start</td><td>Receptionist 1</td></tr><tr><td>Patient 34</td><td>03/01/2016 11:28:02</td><td>Blood test</td><td>Complete</td><td>Lab assistant 1</td></tr><tr><td>Patient 42</td><td>03/01/2016 11:31:58</td><td>Registration</td><td>Complete</td><td>Receptionist 1</td></tr><tr><td>Patient 25</td><td>03/01/2016 11:32:18</td><td>X-ray</td><td>Complete</td><td>Nurse 2</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr></table>

Definition 2 (Activity log). Let L be an activity log based on event log E. Then A is composed of a set of activity instances ${ \mathcal { A } } .$ Each activity instance depicts the execution of an activity a by resource r on case $c ,$ started at time $\tau _ { s t a r t }$ and completed at time $\tau _ { c o m p l e t e } . \mathrm { A n }$ activity instance is represented by $\eta = ( c , a , r , \tau _ { s t a r t } , \tau _ { c o m p l e t e } ) ,$ where $\# _ { k } ( \eta )$ represents the value of attribute k for activity instance g as suggested for events in Definition 1. All activity instances i ∈ L are sorted according to $\tau _ { s t a r t } , \mathrm { i . e . } \forall \eta _ { i } , \eta _ { i + 1 } \in L : \# _ { \tau _ { s t a r t } } ( \eta _ { i } ) \leq \# _ { \tau _ { s t a r t } } ( \eta _ { i + 1 } ) .$

## 3.4. Resource-activity matrix

As the batch organisation of work reflects how resources execute an activity, batching behaviour will be identified at the resourceactivity level. To this end, the activity log is restructured in a RAM, where each cell contains activity instances associated to a particular resource-activity combination. An excerpt of the nurse 2 - X-ray RAM cell is shown in Table 3.

Definition 3 (Resource-activity matrix). Let RAM represent the resource-activity matrix and let $R A M ( a , r )$ be the cell of RAM related to activity a and resource r. Then $R A M ( a , r ) = \{ \eta \in L | \# _ { a c t i v i t y } ( \eta ) =$ $a \land \# _ { r e s o u r c e } ( \eta ) = r \}$

To prepare the RAM for analysis, immediate rework is removed, which refers to the repeated execution of a particular activity by a resource on the same case (almost) immediately after each other. Immediate rework is not consistent with the definition of batch processing as batching focuses on activity execution on distinct cases. Consequently, for these instances immediate rework is replaced by a single activity instance with $\tau _ { s t a r t }$ the start timestamp of the first immediate rework instance and $\tau _ { c o m p l e t e }$ the complete timestamp of the last immediate rework instance.

## 3.5. Batching matrices

In general, a batch is a set of activity instances. To identify batches, BOWI creates a batching matrix (BM) for each batch processing type. The structure of these BMs mimics the RAM, i.e. each cell focuses on one resource-activity combination. Taking a RAM cell as input, activity instances are grouped based on the conditions of the batch type under consideration. These instance sets are recorded in the corresponding BM cell, where instances in a singleton set could not be grouped based on the type of batch under consideration.

Definition 4 (Batch). A batch b is a set of activity instances $\eta \in L ,$ for which $\forall \eta _ { i } , \eta _ { j } ~ \in ~ b ~ : ~ \# _ { a c t i v i t y } ( \eta _ { i } ) ~ = ~ \# _ { a c t i v t y } ( \eta _ { j } ) \wedge \# _ { r e s o u r c e } ( \eta _ { i } ) ~ =$ $\# _ { r e s o u r c e } ( \eta _ { j } )$ , i.e. all instances in b originate from a particular cell $R A M ( a , r )$ in the RAM.

The definitions of the three BMs can, consistent with Section 2.2, be formalised as follows:

Definition 5 (Simultaneous batching matrix). Let $B M _ { s i m }$ represent the simultaneous batching matrix and let $B M _ { s i m } ( a , r )$ be the cell of $B M _ { s i m }$ related to activity a and resource r. Then $B M _ { s i m } ( a , r )$ consists of a set of batches B. When b represents a batch in ${ \mathcal { B } } ,$ then $\forall \eta _ { i } , \eta _ { j } \in$ $b : \mathcal { H } _ { \tau _ { s t a r t } } ( \eta _ { i } ) = \# _ { \tau _ { s t a r t } } ( \eta _ { j } ) \wedge \# _ { \tau _ { c o m p l e t e } } ( \eta _ { i } ) = \# _ { \tau _ { c o m p l e t e } } ( \eta _ { j } ) ( \forall b \in \mathbf { \dot { \mathcal { B } } } )$ Moreover, $\forall b _ { i } , b _ { j } \in \mathcal { B } : b _ { i } \cup b _ { j } \notin \mathcal { B }$ , i.e. any combination of batches in $B M _ { s i m } ( a , r )$ does not fulfill the aforementioned conditions.

Definition 6 (Concurrent batching matrix). Let $B M _ { c o n c }$ represent the concurrent batching matrix and let $B M _ { c o n c } ( a , r )$ be the cell of $B M _ { c o n c }$ related to activity a and resource r. Then $B M _ { c o n c } ( a , r )$ consists of a set of batches B. When b represents a batch in B, then ∀ $h , \eta _ { i + 1 } ~ \in ~ b ~ : ~ \# _ { \tau _ { s t a r t } } ( \eta _ { i } ) ~ \leq ~ \# _ { \tau _ { s t a r t } } ( \eta _ { i + 1 } ) ~ < ~ \# _ { \tau _ { c o m p l e t e } } ( \eta _ { i } ) ~ \land$ $\left( \# _ { \tau _ { s t a r t } } ( \eta _ { i } ) \neq \# _ { \tau _ { s t a r t } } ( \eta _ { i + 1 } ) \vee \# _ { \tau _ { c o m p l e t e } } ( \eta _ { i } ) \neq \# _ { \tau _ { c o m p l e t e } } ( \eta _ { i + 1 } ) \right) ( \forall b \in \mathcal { B } ) .$ Moreover, $\forall b _ { i } , b _ { j } \in \mathcal { B } : b _ { i } \cup b _ { j } \notin \dot { \mathcal { B } } ,$ i.e. any combination of batches in $B M _ { c o n c } ( a , r )$ does not fulfill the aforementioned conditions.

While the formalisation of the simultaneous and concurrent BM directly follows from the definition of the respective batch type in Section 2.2, the specification of the sequential BM is subject to more restrictions. Firstly, the time between the complete timestamp of a case and the start timestamp of the next should be lower than c. This parameter can be set to a strictly positive value to accommodate, e.g., some set-up time required to open a new file after the previous one

Illustration of an activity log.  
Table 2

<table><tr><td>Case id</td><td>Activity</td><td>Resource</td><td> $\tau_{start}$ </td><td> $\tau_{complete}$ </td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>Patient 22</td><td>X-ray</td><td>Nurse 2</td><td>03/01/2016 11:14:41</td><td>03/01/2016 11:22:37</td></tr><tr><td>Patient 25</td><td>X-ray</td><td>Nurse 2</td><td>03/01/2016 11:22:37</td><td>03/01/2016 11:32:18</td></tr><tr><td>Patient 34</td><td>Blood test</td><td>Lab assistant 1</td><td>03/01/2016 11:22:54</td><td>03/01/2016 11:28:02</td></tr><tr><td>Patient 42</td><td>Registration</td><td>Receptionist 1</td><td>03/01/2016 11:25:17</td><td>03/01/2016 11:31:58</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr></table>

Please cite this article as: N. Martin et al., Retrieving batch organisation of work insights from event logs, Decision Support Systems (2017), http://dx.doi.org/10.1016/j.dss.2017.02.012

Table 3  
Table 4  
Illustration of RAM cell nurse 2 - X-ray.

<table><tr><td>Case id</td><td> $\tau_{start}$ </td><td> $\tau_{complete}$ </td></tr><tr><td>...</td><td>...</td><td>...</td></tr><tr><td>Patient 22</td><td>03/01/2016 11:14:41</td><td>03/01/2016 11:22:37</td></tr><tr><td>Patient 25</td><td>03/01/2016 11:22:37</td><td>03/01/2016 11:32:18</td></tr><tr><td>Patient 27</td><td>03/01/2016 11:52:03</td><td>03/01/2016 12:03:01</td></tr><tr><td>Patient 28</td><td>03/01/2016 12:03:01</td><td>03/01/2016 12:11:51</td></tr><tr><td>...</td><td>...</td><td>...</td></tr></table>

is processed. However, c should be small to remain consistent with the idea of batch processing and no other resource activity can be recorded while processing cases in a sequential batch.

Secondly, to integrate the distinction between sequential batch processing and regular queue handling, a function 0 is introduced. This function returns the time at which a case arrives at the activity under consideration. Case arrival is proxied by the completion time of the prior activity executed on this case. Consequently, the preceding activity needs to be known. This control-flow notion can be retrieved using domain knowledge or by applying a controlflow discovery algorithm on the event log. Given the large body of research on the latter [9], the operationalisation of 0 is not treated here.

Thirdly, none of the cases can be included in a simultaneous or concurrent batch for the activity under consideration. This way, it can be avoided that sequences of these two batch types are treated as a sequential batch.

Finally, if multiple cases arrive at the same time at the activity under consideration, they can only form a sequential batch when the first case in this batch is not processed (quasi-)immediately upon arrival. This can, for example, be relevant when the activity preceding the activity under consideration is executed in a simultaneous batch.

Definition 7 (Sequential batching matrix). Let $B M _ { s e q }$ represent the sequential batching matrix and let $B M _ { s e q } ( a , r )$ be the cell of $B M _ { s e q }$ related to activity a and resource r. Then $\bar { B } M _ { s e q } ( a , r )$ consists of a set of batches B. When b represents a batch in B, then $\forall \eta _ { i } , \eta _ { i + 1 } \in b ,$ the following conditions cumulatively hold:

$$
\left(\# _ {\tau_ {s t a r t}} \left(\eta_ {i + 1}\right) - \# _ {\tau_ {c o m p l e t e}} \left(\eta_ {i}\right)\right) \in [ 0, \gamma ], \text { with } \gamma \geq 0
$$

$\begin{array} { r } { \hat { \sharp } e \in E : \# _ { r e s o u r c e } ( e ) = \# _ { r e s o u r c e } ( \eta _ { i } ) \wedge \# _ { \tau _ { c o m p l e t e } } ( \eta _ { i } ) \leq \# _ { t i m e } ( e ) \leq } \end{array}$ $\# _ { \tau _ { s t a r t } } ( \eta _ { i + 1 } )$

$\phi ( \eta _ { i } ) \leq \# _ { \tau _ { s t a r t } } ( \eta _ { 1 } ) \wedge \phi ( \eta _ { i + 1 } ) \leq \# _ { \tau _ { s t a r t } } ( \eta _ { 1 } )$ , where $\eta _ { 1 }$ represents the first processed case in b and $\phi ( \eta _ { x } )$ is a function returning the arrival of case $\# _ { c a s e } ( \eta _ { x } )$ at activity a

$\eta _ { i } , \eta _ { i + 1 } \notin \{ b ^ { \prime } | ( b ^ { \prime } \in \ B M _ { s i m } \vee b ^ { \prime } \ \in \ B M _ { c o n c } ) \wedge | b ^ { \prime } | > 1 \}$ , with |b<sup></sup>| expressing the number of activity instances included in batch b<sup></sup>

• when $\phi ( { \eta } _ { i } ) = \phi ( { \eta } _ { i + 1 } ) = \phi ( { \eta } _ { 1 } ) ,$ then $\# _ { \tau _ { s t a r t } } ( \eta _ { 1 } ) > \phi ( \eta _ { i } ) + \gamma ,$ with $\gamma \geq 0$

$\left( \forall b \in \mathcal { B } \right)$ . Moreover, $\forall b _ { i } , b _ { j } \in \mathcal { B } : b _ { i } \cup b _ { j } \notin \mathcal { B } ,$ i.e. any combination of batches in $B M _ { s e q } ( a , r )$ does not fulfill the conditions outlined above.

An appropriate value of c can be determined using domain knowledge. When such knowledge is unavailable, the event log can support its specification by studying time differences between complete and start timestamps of subsequent non-overlapping activity instances.

To illustrate Definitions 5–7, they are applied to all activity instances in RAM cell nurse $2 - X - r a y$ , depicted in Table 3. Two sequential batches are found, causing $\{ c _ { 2 2 } , c _ { 2 5 } \}$ and $\{ c _ { 2 7 } , c _ { 2 8 } \}$ to be added to the $B M _ { s e q , n u r s e 2 - X - r a y }$ cell. In the other BMs, these instances are added as singletons.

Batch organisation of work metrics.

<table><tr><td>Metric</td><td>Description</td></tr><tr><td>Frequency of batch processing</td><td>The absolute and relative number of times that a set of  $BM_x(a, r)$  contains two or more activity instances.</td></tr><tr><td>Batch size</td><td>Summary statistics of the number of activity instances in each set of  $BM_x(a, r)$ , both including and excluding sets of size one.</td></tr><tr><td>Number of cases included in a batch</td><td>The absolute and relative number of cases that appear in each set of  $BM_x(a, r)$ .</td></tr><tr><td>Duration of activity instances in a batch</td><td>Summary statistics of the difference between the duration of the activity instances in each set of size two or more in  $BM_x(a, r)$  compared to the duration for sets of size one.</td></tr><tr><td>Waiting time of activity instances in a batch</td><td>Summary statistics of the difference between the waiting time of the activity instances in each set of  $BM_x(a, r)$  compared to activity instances not in this set.</td></tr><tr><td>Overlap in concurrent batches</td><td>Summary statistics of the amount of time that the activities in a concurrent batch are actually concurrent.</td></tr></table>

The three batching matrices contain all batch identification information. It should be noted that batch identification is independent of the complexity of the process control-flow as it is situated on the resource-activity level. Control-flow complexity can render the imputation of arrival events more dificult as this requires knowledge on the prior activity for a particular case. Arrival times are used in Definition 7 in an effort to distinguish sequential batching from regular queue handling.

## 3.6. Batch organisation of work metrics

Using the information in the batching matrices as input, batch processing metrics are defined, which describe batching behaviour and provide insight in its business value. Table 4 provides an overview of the metrics, which are briefly explained in the remainder of this subsection. All metrics are defined on the resource-activity level. However, aggregations to other levels of analysis such as the activity level, the resource level and the level of the complete event log can be derived.

## 3.6.1. Frequency of batch processing

The batch processing frequency expresses how often a particular type of batching takes place in an absolute sense and relative to the number of sets in the corresponding BM cell. In Fig. 2, for instance, the laboratory test (L) is performed by the lab assistant in two simultaneous batches, which accounts for 100% of the sets in the associated $B M _ { s i m }$ cell.

## 3.6.2. Batch size

Besides knowing how frequent a particular batch type occurs, the batch size is another valuable metric. As BMs also include singleton sets, indicating that an instance is not part of a batch of this type, batch size summary statistics (such as the mean, median, standard deviation, etc.) can be calculated both including and excluding singleton sets. In Fig. 2, two simultaneous batches of laboratory tests (L) of size two are observed. This generates, for instance, a mean batch size of two and an associated standard deviation of zero.

## 3.6.3. Number of cases included in a batch

This metric combines insights from the prior two metrics by determining the number of cases that are included in a particular type of batch. For instance, 100% of the patients receiving a blood test have this test executed in the laboratory (L) as part of a simultaneous batch in Fig. 2.

For concurrent batch processing, an additional calculation can be performed. According to Definition $6 ,$ concurrent batching requires that subsequent instances have an overlap in time. However, this does not imply that all instances in a batch overlap. Consequently, summary statistics on the number of cases that a resource actually handles concurrently can be determined. The registration (R) of patient 1 in Fig. 2 is for example not overlapping in time with the registration of patients 5 and 6, while they are still in the same concurrent batch.

## 3.6.4. Duration of activity instances in a batch

The effect of batching on activity duration can be determined as resources may become more eficient when they have to perform a similar task on multiple cases. To this end, the duration of instances included in a batch are compared to the duration for instances that are not part of a batch. A nurse might need, e.g., 20 min to perform an X-ray for three patients sequentially, while she needs 10 min to conduct an X-ray separately as she needs to get accustomed to the settings of the machine.

## 3.6.5. Waiting time of activity instances in a batch

The global eficiency gain of batch processing should be weighed against the increase in waiting time for individual cases, which is the elapsed time between case arrival and the start of activity execution. In Fig. 2, patient 1 has to wait until $t _ { 1 0 }$ before triage and assessment (T) starts, even though the patient is registered at $t _ { 6 }$ and the doctor could have assessed him at $t _ { 6 } .$ . As is the case for activity duration, waiting time summary statistics are provided for batched cases and non-batched cases.

## 3.6.6. Overlap in concurrent batches

For concurrent batching, the time overlap between batched cases can also be calculated. This enables the organisation to determine whether an employee starts working on the next case right before he finishes the previous one, or immediately after its start. Summary statistics are provided for the percentage overlap in time. In Fig. 2, the mean overlap between concurrently batched cases for the checkout (C) activity equals 62.5%.

## 3.7. Implementation

BOWI is fully implemented using $\mathsf { R } ^ { 1 }$ , a programming language for which a large set of packages is available which can be used to create application-specific functions. The key packages that are used are dplyr for data manipulations such as sorting and data summarisations, lubridate to work with timestamps and reshape for converting the event log to an activity log.

Algorithm 1 provides the pseudocode for BOWI’s batch identification component. It directly follows from the formalisation introduced in this section and shows that batches are identified from an activity log by parsing it once and comparing each line in this log with the prior one. In this way, the algorithm enriches the activity log with batch information by adding two columns: (i) a batch number, grouping activity instances that belong to the same batch and (ii) the batch type, indicating which of the three batching types prevails. This is all information required to create BMs and calculate the metrics. Each metric is implemented as a separate function, which makes the framework easily extendable with additional metrics.

## Algorithm 1. Batch organisation of work identification.

```txt
Input: eventLog: an event log (list of complex objects representing events), controlFlowNotion:
    knowledge on the prior activity that is executed for a case to support (when required) arrival
    event imputation, tolerances: time tolerances for sequential batch processing

Output: a: activity log with batching information (list of complex objects representing activity instances)

1: eventLog ← ADDARRIVALEVENTS(eventLog, controlFlowNotion)
    ▷imputes (when required) arrival events using knowledge on the prior activity executed for a case

2: a ← CONVERTToACTIVITYLOG(eventLog)
    ▷creates activity instances by mapping corresponding events

3: a ← SORTACTIVITYLOG(a)
    ▷sort rows in activity log based on variables in following order: activity, resource, start timestamp and complete timestamp

4: a ← REMOVEIMMEDIATEREWORK(a)
    ▷removes immediate rework from activity log

5: batchNumber ← 1
    ▷initialise value - instances in a batch will have the same batchNumber

6: a[1].batchNr ← batchNumber ▷initialise batchNumber value for first instance in activity log

7: firstCaseStart ← a[1].start
    ▷initialise value representing the start timestamp of the first case of a potential batch

8: tol ← GETTOLERANCE(tolerances, a[1].activity, a[1].resource)
    ▷determines sequential batch proc.time tolerance for particular resource-activity combination

9: n ← NUMBEROFROWS(a)    ▷number of rows in activity log

10: for i = 2 to n do

11: currentActivity ← a[i].activity    ▷activity of instance under analysis

12: priorActivity ← a[i - 1].activity    ▷activity of prior instance in a

13: currentResource ← a[i].resource

14: priorResource ← a[i - 1].resource

15: currentArrival ← a[i].arrival

16: currentStart ← a[i].start

17: priorStart ← a[i - 1].start

18: currentComplete ← a[i].complete

19: priorComplete ← a[i - 1].complete

20: priorBatchType ← a[i - 1].batchType    ▷batch type to which the prior case belongs

21: if currentActivity == priorActivity and

22: currentResource == priorResource then

23: if currentStart == priorStart and    ▷simultaneous batch processing

24: currentComplete == priorComplete and

25: priorBatchType is empty or simultaneous then

26: a[i].batchNumber ← batchNumber

27: a[i].batchType ← simultaneous

28: if a[i - 1].batchType is empty then

29: a[i - 1].batchType ← simultaneous

30: end if

31: else if currentStart ≥ priorStart and    ▷concurrent batch processing

32: currentStart < priorComplete and

33: currentComplete ≠ priorComplete and

34: priorBatchType is empty or concurrent then

35: a[i].batchNumber ← batchNumber

36: a[i].batchType ← concurrent

37: if a[i - 1].batchType is empty then

38: a[i - 1].batchType ← concurrent

39: end if

40: else if currentStart ≥ priorComplete and    ▷sequential batch processing

41: currentStart ≤ priorComplete + tol and

42: currentArrival ≤ firstCaseStart and

43: !RESOURCEACTIVE(a, currentResource, priorComplete, currentStart) and

44: priorBatchType is empty or sequential then

45: a[i].batchNumber ← batchNumber

46: a[i].batchType ← sequential

47: if a[i - 1].batchType is empty then

48: a[i - 1].batchType ← sequential

49: end if

50: else    ▷start a new batch
```

N. Martin et al. / Decision Support Systems xxx (2017) xxx–xxx

## Algorithm 1 (continued)

55: else 56: batchNumber ← batchNumber + 1 57: a[i].batchNumber ← batchNumber 58: firstCaseStart ← currentStart 59: tol ← GETToLERANCE(tolerances, currentActivity, currentResource) 60: end if 61: end for 62: return a >returns activity loq enriched with batching informatior

## 4. Evaluation

A twofold approach is used to evaluate the algorithm: Section 4.1 focuses on BOWI’s ability to correctly rediscover batches in artificial event logs and Section 4.2 discusses the application of the algorithm on real-life logs.

## 4.1. Artificial event logs

## 4.1.1. Experimental design

BOWI’s performance is evaluated by investigating its ability to rediscover known batches solely using an artificial event log. To this end, an artificial log is generated based on a generalised version of the process model in Fig. 1. For each of the seven resource-activity combinations, it is randomly determined whether no, simultaneous, sequential or concurrent batching prevails with all options having the same probability. In the latter three cases, an integer batch size is randomly drawn from the set {2,3,4,5}. Given these inputs, the event log generator autonomously determines which cases are batched for each activity and generates a log considering 500 cases that enter the process. The data file also indicates which cases are grouped as a batch of a particular type. This information is only used for evaluation purposes and is removed from the event log that is provided to BOWI.

After executing BOWI on the event log, the algorithm’s output is compared to the real batch composition. For a particular resourceactivity combination, a case is correctly classified by BOWI when it is (i) contained in its correct batch in the BM of the batch type prevailing in reality and (ii) included as a singleton in the BMs of the other two batch types. Consequently, the evaluation centers around the detection of errors, which are (i) cases that are included in a batch of the correct type but in the wrong composition and (ii) cases being included in a batch of a particular type while they are not included in such a batch in reality. Using these conditions, the number of errors is calculated for each resource-activity combination. The first condition is defined rather rigorously as the composition of discovered batches has to be completely correct. For instance: when BOWI rediscovers a batch for all but one case, all cases in this batch are reported as errors because they are not part of the exact same batch prevailing in reality.

The aforementioned constitutes one experiment. To determine the number of experiments, an a priori power analysis for a onesample Wilcoxon singed-rank test is conducted. To achieve a power value (i.e. the probability of rejecting the null hypothesis when it is false) of 0.80 [10] and given a family-wise significance level to 0.05 and effect size of 0.20 (the value proposed by Cohen [11] for the detection of small effects), the power analysis shows that at least 185 event logs need to be generated. Consequently, the number of artificial event logs is set to 200, which surpasses this lower bound.

## 4.1.2. Results

The application of the experimental design calculates, for each resource-activity combination in an event log, the number of errors.

These results are aggregated by grouping resource-activity combinations in 12 classes, expressing a combination of the real batch type in the event log (no batching, simultaneous, concurrent or sequential batching) and BOWI’s output (simultaneous, concurrent or sequential BMs). For each of them, a decimal error proportion is calculated by dividing the number of errors by the number of cases that are included in the real batches for that class.

Table 5 reports summary statistics on the error proportions detected for the 12 classes over all 200 event logs. With ‘seq - seq’ and ‘no batch - seq’ as an exception, all classes show that BOWI’s output is free from errors. This confirms that BOWI can rediscover existing batches solely using the event log. Moreover, the algorithm does, e.g., not detect sequential batch processing when concurrent batch processing prevails.

Regarding BOWI’s detection of sequential batch processing, errors are detected when either sequential batch processing prevails in reality or no batch processing takes place. For an event log in which sequential batch processing is introduced, BOWI does not rediscover the exact composition of these batches for, on average, 7.62% of batched cases, with a standard deviation of 15.41% point. These errors are fairly concentrated as an exact match, i.e. an error proportion of zero is present for 243 of the 352 observations (69.03%). For the remaining 109 observations, several explanations for the observed deviations can be identified. When sequential batch processing is inserted in the event log for the first activity, no arrival proxy will be available in the resulting event log as no prior activity is present. Consequently, conditions related to the arrival proxy in Definition 7 cannot be checked, leading to a less stringent definition. This can cause multiple batches of a particular size that are executed one after another to be included as a single batch in BOWI’s output. The same holds when the activity under analysis is preceded by an activity where simultaneous batch processing prevails with a higher batch size than the batch size for the activity under analysis. When the arriving simultaneous batch is processed immediately upon arrival, BOWI will detect, e.g., a batch of size four instead of two batches of size two. Even though this will be included as an error in Table 5, BOWI’s output is a valid representation of business intuition in this case.

When no batch processing is included for a resource-activity combination in the event log, i.e. when all cases are expected to be included as a singleton in each of the BMs, the error proportion of BOWI is higher. The mean error proportion equals 54.08% with a standard deviation of 16.20% point and a median of 56.77%. Studying the error proportion on the activity level for the ‘no batch - seq’ situation shows that it is the highest for the start activity. This can, once again, be attributed to the less strict definition due to the absence of an arrival proxy. For the other activities, errors can be explained by the arrival of cases in, e.g., a simultaneous batch which is not handled immediately upon arrival. Even though it is recorded as an error, it presents a valid occurrence of sequential batch processing in a business context. Even when cases arrive separately, sequential batch processing can also be detected when long queues are formed. In this case, a subset of queueing cases fulfills the conditions of Definition 7. Despite the fact that Definition 7 aims to distinguish between regular queue handling and sequential batch processing, it should be noted that the definition aims to strike a balance between

## Table 5

Summary statistics on the error proportion of BOWI’s output.

<table><tr><td rowspan="2">Event log input - BOWI output</td><td colspan="5">Error proportion</td></tr><tr><td>Mean</td><td>sd</td><td>Median</td><td>Min</td><td>Max</td></tr><tr><td>seq - seq</td><td>0.08</td><td>0.15</td><td>0.01</td><td>0.00</td><td>1.00</td></tr><tr><td>no batch - seq</td><td>0.54</td><td>0.16</td><td>0.57</td><td>0.13</td><td>0.82</td></tr><tr><td>All 10 other classes</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td></tr></table>

accuracy and clarity. Instead of enumerating and excluding all possible exceptions, leading to an incomprehensible definition, a limited set of understandable conditions is specified.

For the sake of completeness, a one-sided one-sample Wilcoxon signed-rank test is performed for each class in Table 5 testing the null hypothesis that the median observed error proportion is zero against the alternative hypothesis that it is larger than zero. This test is used as the normality assumption underlying the t-test is not deemed appropriate in the current context. As anticipated, the null hypothesis is rejected for ‘seq - seq’ (V = 5, 995, p :< 2.2 • 10<sup>−16</sup>) and ‘no batch - seq’ (V = 53, 301, p :< 2.2•10<sup>−16</sup>), even when a Bonferroni correction [12] is applied with a family-wise significance level of 5%. For the other combinations of event log input and BOWI’s output, no test statistics can be calculated as all observations equal zero.

## 4.2. Real-life event log

To demonstrate that BOWI can generate insights in batching behaviour in a real world business context, the algorithm is applied to real-life event logs from two different contexts: a call center and a production company.

## 4.2.1. Event log of a call center

BOWI is applied to a real-life event log, based on data of a bank’s call center made available by the Technion Service Enterprise Engineering Center<sup>2</sup>. Incoming calls are directed to a voice response unit (VRU), where automated voice information guides the caller. When the VRU does not enable callers to service themselves, they are redirected to a queue, after which they are connected to an agent. After converting the dataset to an event log format, 34 resource-activity combinations are included. More specifically, the log contains the VRU - Handling by VRU combination and the activity Handling by agent, which is executed by 33 distinct staff members. The results reported in this section are based on an analysis of 169,065 calls registered in the first semester of 1999.

Within the analysis set, batching behaviour is detected for 31 resource-activity combinations. For Handling by VRU, which is always handled by resource VRU, both concurrent and simultaneous batching is detected, with respectively 26% and 0.33% of all calls being batched. The significant number of calls handled concurrently is due to the VRU’s design to handle multiple calls concurrently on different lines. Simultaneous batching is present to a far lesser extent as it requires that, by coincidence, multiple calls arrive at exactly the same time and require the same processing time.

For 30 out of 33 agents performing Handling by agent, batching behaviour is detected. Concurrent batching is present, but its prevalence is low as, on average, only 1.85% of the calls are included in a concurrent batch. Sequential batch processing is also discovered, but to a far lesser extent with an average of 0.03% of the calls belonging to a sequential batch. When focusing on concurrent batching, Table 6 summarises some of BOWI’s metrics for the five agents handling calls concurrently the most often.

Table 6 shows that, even for the agents for which concurrent batching is observed the most, the proportion of batched calls is rather limited as it ranges between 2.05% and 2.53%. The mean batch size varies between 2.16 and 2.23 calls. Hence, batching is not fundamentally integrated in the operations of a call center, which could be anticipated given its characteristics. Concurrent batching can take place when an agent already takes another call while the caller is looking for a particular document or the agent is awaiting input from the bank. This is supported by the fact that the mean duration tends to be longer for batched calls than for non-batched calls.

4.2.2. Event log of a production company

BOWI is also applied to a real-life event log of a production process, which is available at the 4TU Data Center<sup>3</sup>. It contains process execution data for 225 cases undergoing activities such as flat grinding and packing. In the log, 27 distinct activities and 31 unique resources are included.

Applying BOWI shows that batch processing is detected for 29 of the 57 resource-activity combinations in the event log. More specifically, simultaneous, concurrent and sequential batching is present for respectively, 9, 25 and 17 resource-activity combinations. This includes 14 resource-activity pairs for which both concurrent and sequential batches are present and 7 resource-activity pairs for which all batch types are detected.

Using the number of cases included in a batch metric, it is concluded that concurrent batch processing is the most prevalent. When considering all resource-activity combinations where concurrent batch processing occurs, on average 23.50% of all cases is batched. For simultaneous and sequential batching, this is 15.55% and 11.31% respectively. Consequently, the remainder of this discussion focuses on concurrent batching.

When concurrent batching occurs, an important part of the cases is batched. This indicates that batching is fundamentally integrated in the organisation’s process. Table 7 summarises some BOWI metric values for the five resource-activity combinations for which the highest number of concurrent batches is detected. For these resource-activity combinations, the proportion of cases being part of a concurrent batch ranges from 28% to 77%. The batch sizes are situated between 2.34 and 3.33, with standard deviations between 0.61 and 2.11. The influence of batch processing on activity duration outlined in literature does not hold as batched cases tend to take longer than non-batched cases. It might be the case that batching takes place for a particular type of product, which requires less intensive processing. Concerning the difference in waiting times between batched and non-batched cases, the results are mixed depending on the resource-activity combination. From the time overlap metric, it follows that there is a significant overlap between concurrently handled cases. This indicates that genuine concurrent batch processing is detected, and not sequential batch processing with inaccurate timestamp registration.

## 5. Related work

BOWI is based on a distinction between simultaneous, concurrent and sequential batching. While Wu [6] and Pufahl and Weske [13] distinguish between the parallel and sequential execution of activities, other references such as Pufahl et al. [14] and Pufahl et al. [14,15] only consider simultaneous batch processing. Consequently, this paper presents a more versatile perspective on batch processing.

Batch processing is studied in several domains, but mainly within the field of operations management, with a key focus on topics such as order batching [16], scheduling [17,18] and operational excellence [19,20]. Often, the trade-off between additional waiting times and reduced setup costs is mentioned [19,20]. This is also explicitly recognised in business process management literature [14,21–23].

Within the process modelling and execution domain, Pufahl and Weske [13] specify the concept of batch activities and identify specification parameters such as the batch size. While Pufahl and Weske [13] focus on a single batch activity, Pufahl et al. [23] extend these concepts to batch regions. The latter are a series of model constructs such as activities that handle cases in a batch. Recently, batch processing is studied for activities in different processes by means of object life cycles [24]. As Pufahl and Weske [13,24] and Pufahl et al. [23] primarily focus on the activity level, they do not explicitly take into account that the organisation of work for a particular activity can differ among resources. BOWI includes this perspective by considering the resource-activity level as the key level of analysis. This is consistent with Liu and Hu [21] given that batching strategies can differ among resources. While Pufahl and Weske [13,24] and Pufahl et al. [23] focus on process modelling and the specification of execution semantics, Pufahl et al. [14] focus on performance evaluation of batch activities. Solely considering the simultaneous batch processing case, cost functions are defined for both service and waiting costs and an analytical solution is proposed making use of queuing theory. In this way, the benefits of introducing simultaneous batch processing can be quantified and a recommended batch size can be calculated. However, the suggested approach focuses on a single activity which, moreover, must fulfill the conditions of a particular queuing model [14]. As follows from the above discussion, related work tends to focus on modelling batch processing at design time. However, Pufahl et al. [22] suggest an approach to dynamically adjust the batch activity configuration parameters depending on, e.g., the planned maintenance of a machine. This more flexible perspective on batching is also included in Pufahl and Weske [24], where a set of cases that might be batched is solely suggested to the resource.

Table 6  
BOWI metrics calculated for concurrent batching by five resources for activity Handling by agent in the call center event log.

<table><tr><td rowspan="2">Agent</td><td rowspan="2">Frequency</td><td colspan="2">Batch size</td><td rowspan="2"># batched cases (rel.)</td><td colspan="2">Duration (mean) $^a$ </td><td rowspan="2">Time overlap</td></tr><tr><td>Mean</td><td>sd</td><td>Batch</td><td>No batch</td></tr><tr><td>SHARON</td><td>152</td><td>2.23</td><td>0.42</td><td>2.49</td><td>4.27</td><td>2.28</td><td>0.46</td></tr><tr><td>KAZAV</td><td>121</td><td>2.17</td><td>0.39</td><td>2.53</td><td>4.71</td><td>3.21</td><td>0.47</td></tr><tr><td>MORIAH</td><td>114</td><td>2.18</td><td>0.38</td><td>2.64</td><td>4.21</td><td>3.14</td><td>0.50</td></tr><tr><td>TOVA</td><td>107</td><td>2.16</td><td>0.39</td><td>2.54</td><td>4.32</td><td>2.84</td><td>0.47</td></tr><tr><td>STEREN</td><td>87</td><td>2.18</td><td>0.39</td><td>2.05</td><td>6.13</td><td>3.04</td><td>0.52</td></tr></table>

<sup>a</sup> Expressed in minutes.

Besides Wen et al. [15] and Nakatumba [25] as notable exceptions, no research attention is devoted to batch processing within the process mining field. This is consistent with Martin et al. [3], where the retrieval of batch processing insights from event logs is marked as a research gap. Wen et al. [15] consider the problem of mining the process control-flow when the process contains activities where simultaneous batch processing occurs. For these activities, the authors assume that, for a particular batch, events are only logged for one of the cases in this batch. This is similar to Liu and Hu [21], where batched cases are temporarily merged and decomposed afterwards. In contrast, BOWI assumes that events are recorded for all individual cases in a batch. When this is not the case, the work presented in Wen et al. [15] forms a valuable starting point for the simultaneous batch processing case. In Wen et al. [15], a method is developed that aims to add the missing events of batched cases, after which, e.g., existing control-flow discovery algorithms can be applied. This complemented log can also be used to apply BOWI.

Nakatumba [25] proposes a method to identify batch processing in which all resource actions, i.e. executions of activities, are placed on a timeline and grouped in so called chunks. A new chunk is started when the elapsed time between the end of an action and the start of the following action exceeds 1 h. When a period such as a working day is composed of multiple chunks, Nakatumba [25] states that batch processing occurs. This paper extends the work of Nakatumba [25] in several ways. Firstly, in contrast to Nakatumba [25], BOWI does not make abstraction from the difference between activities, reflecting the fact that some activities might be more eligible for batch processing. Secondly, the arbitrary delay of 1 h between periods of activity is replaced by a forma definition of several types of batch processing. Finally, BOWI complements the work of Nakatumba [25] by distinguishing between batch processing and regular queue handling.

## 6. Limitations

Despite BOWI’s ability to mine and describe batching behaviour from an event log, some limitations need to be recognised. Firstly, the log should contain both start and complete events and resource information, which is often not the case in existing real-life event logs. Moreover, the level of detail at which timestamps and resources are recorded determines the granularity at which batching behaviour is identified. When, e.g., only resource classes are recorded, no distinction can be made between specific resources.

Secondly, BOWI does not explicitly consider the issue of noise in timestamp registration. Hence, it relies on accurate event registration for each case, which can require that a process is backed by a system which automatically logs resource action instead of relying on manual intervention to log events. Nevertheless, some features of BOWI should be highlighted related to inaccurate timestamp registration. For sequential batching, a time tolerance that is allowed between consecutive instances in a sequential batch can be specified. When the start and complete timestamps of cases in a simultaneous batch are not identical, BOWI will label it as a concurrent batch. However, the value of the time overlap metric will show a high overlap, indicating that it might be an inaccurately recorded simultaneous batch.

Thirdly, the creation of an activity log requires mapping corresponding start and complete events. When a case passes a resourceactivity combination multiple times, each start event is mapped to the first occurring unmapped complete event. When this mapping

BOWI metrics calculated for concurrent batching for five resource-activity combinations from the production company event log.

<table><tr><td rowspan="2">Res.-act. comb. $^a$ </td><td rowspan="2">Freq.</td><td rowspan="2">Batch size (mean)</td><td rowspan="2"># batched cases (rel.)</td><td colspan="2">Duration (mean)</td><td colspan="2">Waiting time (mean)</td><td rowspan="2">Time overlap</td></tr><tr><td>Batch</td><td>No batch</td><td>Batch</td><td>No batch</td></tr><tr><td>1</td><td>121</td><td>3.33</td><td>0.77</td><td>2.23</td><td>1.27</td><td>22.92</td><td>48.11</td><td>0.86</td></tr><tr><td>2</td><td>118</td><td>2.83</td><td>0.66</td><td>1.74</td><td>1.27</td><td>18.83</td><td>17.54</td><td>0.79</td></tr><tr><td>3</td><td>61</td><td>2.36</td><td>0.39</td><td>2.31</td><td>1.45</td><td>45.90</td><td>58.37</td><td>0.65</td></tr><tr><td>4</td><td>34</td><td>2.47</td><td>0.34</td><td>6.07</td><td>5.88</td><td>7.15</td><td>3.35</td><td>0.51</td></tr><tr><td>5</td><td>29</td><td>2.34</td><td>0.28</td><td>6.45</td><td>5.11</td><td>5.77</td><td>9.09</td><td>0.50</td></tr></table>

<sup>a</sup> 1: Qual. Check 1 - Final Insp. Q.C., 2: Qual. Check 1 - Turn. & Mil. Q.C, 3: Machine 1 - Lapping, 4: Machine 4 - Turn. & Mil., 5: Machine 6 - Turn. & Mil.

Please cite this article as: N. Martin et al., Retrieving batch organisation of work insights from event logs, Decision Support Systems (2017), http://dx.doi.org/10.1016/j.dss.2017.02.012

does not correspond to reality, it will influence batch detection as the activity log is its key input.

Finally, a case’s arrival time at an activity is needed to distinguish sequential batching from regular queue handling. When this information is not included in the event log, it can be proxied by the completion time of the prior activity. However, this requires control-flow insights, i.e. the prior activity needs to be known, which is not trivial for complex processes. However, the absence of such a proxy does not impede BOWI from being applied, but renders the conditions to detect sequential batching less strict.

## 7. Conclusion

This paper focuses on the retrieval of batch processing insights from an event log. To this end, three types of batching are identified and formalised, i.e. simultaneous, concurrent and sequential batching. Using these definitions, the Batch Organisation of Work Identification algorithm (BOWI) is developed to identify batches and calculate metrics summarising batching behaviour. The algorithm is evaluated on artificial event logs, showing that it can rediscover batches under most circumstances. Moreover, BOWI is applied to real-life event logs from a call center and production context.

Future extensions of BOWI can generate even more versatile batch processing insights from an event log. Firstly, the effect of noise on BOWI’s performance can be studied in order to make the algorithm more resilient to noise. Secondly, BOWI’s scope can be broadened by considering multiple consecutive activities instead of only a single activity, which is mentioned in Wen et al. [15] and Liu and Hu [21] and is consistent with the batch regions notion in Pufahl et al. [23]. Finally, insights in batch logic by modelling the reasoning behind batching is an additional analysis dimension. Batching logic can be modelled by mining batch activation rules, which can merely depend on the number of queueing cases or can be contingent on, e.g., the time of day or case attributes.

## References

[1] M. Dumas, M. La Rosa, J. Mendling, H.A. Reijers, Fundamentals of Business Process Management, Springer, Heidelberg, 2013.

[2] D. McBride, The Process of Research in Psychology, Sage, Thousand Oaks, 2016.

[3] N. Martin, B. Depaire, A. Caris, The use of process mining in business process simulation model construction: structuring the field, Bus. Inf. Syst. Eng. 58 (1) (2016) 73–87.

[4] W. van der Aalst, Business process management: a comprehensive survey, ISRN Softw. Eng. 2013 (2013) 1–37.

[5] N. Martin, M. Swennen, B. Depaire, M. Jans, A. Caris, K. Vanhoof, Batch processing: definition and event log identification, CEUR Workshop Proc. 1527 (2015)137-140

[6] K. Wu, Taxonomy of batch queueing models in manufacturing systems, Eur. J. Oper, Res, 237 (1) (2014) 129–135.

[7] P. Murthy, Production and Operations Management, New Age International Publishers, New Delhi, 2005.

[8] M. Telsang, Production Management, S. Chand & Company Ltd, New Delhi, 2005.

[9] W. van der Aalst, Process Mining: Discovery, conformance and Enhancement of Business Processes, Springer, Heidelberg, 2011.

[10] J. Cohen, A power primer, Psychol. Bull. 112 (1992) 155–159.

[11] J. Cohen, Statistical Power Analysis for the Behavioral Sciences, Lawrence Erlbaum Associates, New Jersey, 1988.

[12] S. Holm, A simple sequentially rejective multiple test procedure, Scand. J. Stat. 6 (2) (1979) 65–70.

[13] L. Pufahl, M. Weske, Batch activities in process modeling and execution, Lect. Notes Comput. Sci 8274 (2013) 283–297.

[14] L. Pufahl, E. Bazhenova, M. Weske, Evaluating the performance of a batch activity in process models, Lect. Notes Bus. Inf. Process. 202 (2014) 277–290.

[15] Y. Wen, Z. Chen, J. Liu, J. Chen, Mining batch processing workflow models from event logs, Concurrency Comput. Pract. Exp. 25 (13) (2013) 1928–1942.

[16] S. Henn, S. Koch, G. Wäscher, Order Batching in Order Picking Warehouses: A Survey of Solution Approaches, Springer, London, 2012.

[17] P. Brucker, Scheduling Algorithms, Springer, Heidelberg, 2007.

[18] M.L. Pinedo, Scheduling: Theory, Algorithms, and Systems, Springer, New York, 2012.

[19] E.M. Goldratt, Theory of constraints, North River Press, Croton-on-Hudson, 1990.

[20] R. Arbulu, I. Tommelein, K. Walsh, J. Hershauer, Value stream analysis of a re-engineered construction supply chain, Build. Res, Inf, 31 (2)(2003) 161–171.

[21] J. Liu, J. Hu, Dynamic batch processing in workflows: model and implementation, Futur. Gener. Comput. Syst. 23 (3) (2007) 338–347.

[22] L. Pufahl, N. Herzberg, A. Meyer, M. Weske, Flexible batch configuration in business processes based on events, Lect. Notes Comput. Sci 8831 (2014) 63–78.

[23] L. Pufahl, A. Meyer, M. Weske, Batch regions: process instance synchronization based on data, Proceedings of the IEEE International Enterprise Distributed Object Computing Conference, 2014. pp. 150–159.

[24] L. Pufahl, M. Weske, Batch processing across multiple business processes based on object life cycles, Lect. Notes Bus. Inf. Process. 255 (2016) 195–208.

[25] J.J. Nakatumba, Resource-Aware Business Process Management: Analysis and Support (Ph.D. Thesis), Eindhoven University of Technology. 2013.

Niels Martin is a PhD student at the Faculty of Business Economics of Hasselt University, Belgium. He is a member of the research group Business Informatics, where his research deals with the use of event log knowledge to construct more realistic business process simulation models. More specifically, his three key research topics are entity arrival rate modelling, the identification of batch processing and resource schedule retrieval.

Marijke Swennen graduated in 2011 as Master Applied Economic Sciences: Business Engineering in Management Information Systems at Hasselt University, Belgium. In October 2011, she started her PhD research in the research Business Informatics field, on which she will be working until the end of 2016. More specifically, her research deals with the use of process mining to support the principles of operational excellence in companies.

Beno<sup>ˆ</sup>it Depaire is Assistant Professor at the Faculty of Business Economics, Hasselt University. He belongs to the research group Business Informatics within the Quantitative Methods Department. His research interests focus on the application of data mining, statistics and process mining within a business-related context.

Mieke Jans obtained her PhD degree in Accounting Information Systems in 2009. The topic of her dissertation was the application of data mining and process mining for internal fraud risk reduction. For 5 years, Mieke combined an academic career with a career in industry at Deloitte, where she was responsible for the process mining projects in audit and operational eficiency contexts. Since september 2014, Mieke is full-time associated with Hasselt University, doing research on process mining in a business context.

An Caris is Assistant Professor of Operations Management and Logistics at Hasselt University (Belgium) within the Faculty of Business Economics. She received a Master degree in Business Engineering with a major in Operations Management and Logistics at the Limburg University Centre (LUC). Belgium, in 2003 In 2010 she defended her Ph D. in Applied Economic Sciences at Hasselt University, Belgium. She takes a research interest in modelling intermodal freight transport networks, vehicle routing problems, simulation models and metaheuristics

Koen Vanhoof studied physics and computer science and promoted in 1998 at the Katholic Universiy of Leuven. He joined Hasselt University in 1989. His major research interests are in the areas of data mining, statistics, knowledge engineering and modelling, computational intelligence methods, decision support systems, process modelling, process mining and soft computing. The application domains are information management, marketing and finance, mobility and trafic safety. He has authored and/or co-authored over 60 peer-reviewed journal articles and about 8 book chapters and 60 conference papers. He is co-editor of the International Journal of Information Theory and Applications. Currently he is responsible for courses such as Business Intelligence, Business process modelling, Knowledge discovery management. He is project leader of the Business informatics research group at Hasselt University.

Please cite this article as: N. Martin et al., Retrieving batch organisation of work insights from event logs, Decision Support Systems (2017), http://dx.doi.org/10.1016/j.dss.2017.02.012
