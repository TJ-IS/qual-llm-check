---
otero_id: 1792
otero_key: "UPEAC38D"
title: "A recommendation system for predicting risks across multiple business process instances"
authors: "Raffaele Conforti; Massimiliano de Leoni; Marcello La Rosa; Wil M.P. van der Aalst; Arthur H.M. ter Hofstede"
year: "2015"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2014.10.006"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A recommendation system for predicting risks across multiple business process instances

Raffaele Conforti <sup>a,</sup>⁎, Massimiliano de Leoni <sup>b,c</sup>, Marcello La Rosa <sup>a,d</sup>, Wil M.P. van der Aalst <sup>a,b</sup>, Arthur H.M. ter Hofstede <sup>a,b</sup>

<sup>a</sup> Queensland University of Technology, Australia

<sup>b</sup> Eindhoven University of Technology, The Netherlands

<sup>c</sup> University of Padua, Italy

<sup>d</sup> NICTA Queensland Lab, Brisbane, Australia

## a r t i c l e i n f o

Article history: Received 12 February 2014 Received in revised form 3 October 2014 Accepted 22 October 2014 Available online 6 November 2014

Keywords: Business process management Risk management Risk prediction Job scheduling Work distribution YAWL

## a b s t r a c t

This paper proposes a recommendation system that supports process participants in taking risk-informed decisions, with the goal of reducing risks that may arise during process execution. Risk reduction involves decreasing the likelihood and severity of a process fault from occurring. Given a business process exposed to risks, e.g. a <sup>fi</sup>nancial process exposed to a risk of reputation loss, we enact this process and whenever a process participant needs to provide input to the process, e.g. by selecting the next task to execute or by <sup>fi</sup>lling out a form, we suggest to the participant the action to perform which minimizes the predicted process risk. Risks are predicted by traversing decision trees generated from the logs of past process executions, which consider process data, involved resources, task durations and other information elements like task frequencies. When applied in the context of multiple process instances running concurrently, a second technique is employed that uses integer linear programming to compute the optimal assignment of resources to tasks to be performed, in order to deal with the interplay between risks relative to different instances. The recommendation system has been implemented as a set of components on top of the YAWL BPM system and its effectiveness has been evaluated using a real-life scenario, in collaboration with risk analysts of a large insurance company. The results, based on a simulation of the real-life scenario and its comparison with the event data provided by the company, show that the process instances executed concurrently complete with significantly fewer faults and with lower fault severities, when the recommendations provided by our recommendation system are taken into account.

© 2014 Elsevier B.V. All rights reserved.

## 1. Introduction

A process-related risk measures the likelihood and the severity that a negative outcome, also called fault, will impact on the process objectives [1]. Failing to address process-related risks can result in substantial <sup>fi</sup>nancial and reputational consequences, potentially threatening an organization's existence. Take for example the case of Société Générale, which went bankrupt after a €4.9B loss due to fraud.

Legislative initiatives like Basel II [2] and the Sarbanes–Oxley $\mathsf { A c t } ^ { 1 }$ re<sup>fl</sup>ect the need to better manage business process risks. In line with these initiatives, organizations have started to incorporate process risks as a distinct view in their operational management, with the aim to effectively control such risks. However, to date there is little guidance as to how this can be concretely achieved.

As part of an end-to-end approach for risk-aware Business Process Management (BPM), in [3–5] we proposed several techniques to model risks in executable business process models, detect them as early as possible during process execution, and support process administrators in mitigating these risks by applying changes to the running process instances. However, the limitation of these efforts is that risks are not prevented, but rather acted upon when their likelihood exceeds a tolerance threshold. For example, a mitigation action may entail skipping some tasks when the process instance is very likely to exceed the de<sup>fi</sup>ned maximum cycle time. While effective, mitigation comes at the cost of modifying the process instance, often by skipping tasks or rolling back previously-executed tasks, which may not always be acceptable. Moreover, we have shown that it is not always possible to mitigate all process risks [4]. For example, rolling back a task for the sake of mitigating a risk of cost overrun, may not allow the full recovery of the costs incurred in the execution of that task.

To address these limitations we propose a recommendation system that supports process participants in taking risk-informed decisions, with the aim to reduce process risks preemptively. A process participant takes a decision whenever they have to choose the next task to execute out of those assigned to them at a given process state, or via the data they enter in a user form. This input from the participant may in<sup>fl</sup>uence the risk of a process fault to occur. For each such input, the technique returns a risk prediction in terms of the likelihood and severity that a fault will occur if the process instance is carried out using that input. This prediction is obtained via decision trees which are trained using historical process data such as process variables, resources, task durations and frequencies. The historical data of a process is observed using decision trees which are built from the execution logs of the process, as recorded by the IT systems of an organization.

This way, the participant can take a risk-informed decision as to task to execute next, or can learn the predicted risk of submitting a form with particular data. If the instance is subjected to multiple potential faults, the predictor can return the weighted sum of all fault likelihoods and severities, as well as the individual <sup>fi</sup>gures for each fault. The weight of each fault can be determined based on the severity of the fault's impact on the process objectives.

The above technique only provides “local” risk predictions, i.e. predictions relative to a speci<sup>fi</sup>c process instance. In reality, however, multiple instances of (different) business processes may be executed at any time. Thus, we need to <sup>fi</sup>nd a risk prediction for a speci<sup>fi</sup>c process instance that does not affect the prediction for other instances. The interplay between risks relative to different instances can be caused by the sharing of the same pool of process participants: two instances may require the same scarce resource. In this setting, a sub-optimal distribution of process participants to the set of tasks to be executed may result in a risk increase (e.g. overtime or cost overrun risk). To solve this problem, we equipped our recommendation system with a second technique, based on integer linear programming, which takes input from the risk prediction technique, to <sup>fi</sup>nd an optimal distribution of process participants to tasks. By optimal distribution we mean one that minimizes the overall execution time (i.e. the time taken to complete all running instances) while minimizing the overall level of risk. This distribution is used by the recommendation system to suggest to process participants the next task to perform.

We operationalized our recommendation system on top of the YAWL BPM system by extending an existing YAWL plug-in and by implementing two new custom YAWL services. This implementation prompts process participants with risk predictions upon <sup>fi</sup>lling out a form or for each task that can be executed. We then evaluated the effectiveness of our recommendation system by conducting experiments using a claim handling process in use at a large insurance company. With input from a team of risk analysts from the company, this process has been extensively simulated on the basis of a log recording one year of completed instances of this process. The recommendations provided by our recommendation system signi<sup>fi</sup>cantly reduced the number and severity of faults in a simulation of a real life scenario, compared to the process executed by the company as re<sup>fl</sup>ected by the event data. Further, the results show that it is feasible to predict risks across multiple process instances without impacting on the execution performance of the BPM system.

The remainder of this paper is organized as follows. Section 2 discusses related work. Section 3 contextualizes the recommendation system within our approach for managing process-related risks, while Section 4 presents the YAWL language as part of a running example. Next, Section 5 de<sup>fi</sup>nes the notions of event logs and faults which are required to explain our techniques. Section 6 describes the technique for predicting risks in a single process instance while Section 7 extends this technique to the realm of multiple process instances running concurrently. Section 8 and Section 9 discuss the implementation and evaluation of the recommendation system, respectively. Finally, Section 10 concludes the paper. A provides the formal de<sup>fi</sup>nition of a YAWL speci<sup>fi</sup>cation, the algorithms to generate a prediction function, and technical proofs of two lemmas presented in Section 7.

## 2. Related work

The approach presented in this paper is related to work on risk prediction, job scheduling, operational support and work-item distribution for business processes. In this section we review the state of the art in these <sup>fi</sup>elds to motivate the need for our approach.

## 2.1. Risk prediction

Various risk analysis methods such as OCTAVE [6], CRAMM [7] and CORAS [8] have been de<sup>fi</sup>ned which provide elements of risk-aware process management. Meantime, academics have recognized the importance of managing process-related risks. However, risk analysis methods only provide guidelines for the identi<sup>fi</sup>cation of risks and their mitigation, while academic efforts mostly focus on risk-aware BPM methodologies in general, rather than on concrete approaches for risk prediction [9].

An exception is made by the works of Pika et al. [10] and Suriadi et al. [11]. Pika et al. propose an approach for predicting overtime risks based on statistical analysis. They identify <sup>fi</sup>ve process risk indicators whereby the occurrence of these indicators in a trace indicates the possibility of a delay. Suriadi et al. propose an approach for Root Cause Analysis based on classi<sup>fi</sup>cation algorithms. After enriching a log with information like workload, occurrence of delay, and involvement of resources, they use decision trees to identify the causes of overtime faults. The cause of a fault is obtained as a disjunction of conjunctions of the enriching information. Despite looking at the same problem from different perspectives, these two approaches have quite similar results. These two approaches suffer from the limitation of not considering the data perspective. Further, they limit their scope to the identi<sup>fi</sup>cation of indicators of risks or of causes of faults to support overtime risks only.

In previous work, we presented a wider approach which aims to bridge the gap between risk and process management. This approach consists of two techniques. The <sup>fi</sup>rst one [3,5] allows process modelers to specify process-related faults and related risks on top of (executable) process models, and to detect them at run-time when their risk likelihood exceeds a tolerance threshold. Risks are speci<sup>fi</sup>ed as conditions over control-<sup>fl</sup>ow, resources and data aspects of the process model. The second technique [4] builds on top of the <sup>fi</sup>rst one to cover risk mitigation. As soon as one or more risks are detected which are no longer tolerable, the technique proposes a set of alternative mitigation actions that can be applied by process administrators. A mitigation action is a sequence of controlled changes on a process instance affected by risks, which takes into account a snapshot of the process resources and data, and the current status of the system in which the process is executed.

For a comprehensive review and comparative analysis of work at the intersection of risk management and BPM, we refer to [9].

## 2.2. Job scheduling

The problem of distributing work items to resources in business process execution shares several similarities with the job-shop scheduling [12–15]. Job-shop scheduling concerns M jobs that need to be assigned to N machines, with N b M, while trying to minimize the make-span, i.e. the total length of the schedule. Jobs may have constraints, e.g. job i needs to <sup>fi</sup>nish before job j can be started, certain jobs can only be performed by given machines.

Unfortunately, these approaches are intended for different settings and cannot be specialized for risk-informed work-item assignment. To our knowledge, the techniques of job-shop scheduling are unaware of the concept of cases or process instances, since typically jobs are not associated with a case.

The concept of case is crucial when dealing with process-aware information systems. Work items are executed within process instances and many process instances can be running at the same time, like so many work items may be enabled for execution at the same time. Different instances may be worked on by the same resources and, hence, the allocation within instances may affect the performance of other instances. Without considering the instances in which work items are executed, an important aspect is not considered and, hence, the overall allocation is not really optimized. Moreover, applying job-scheduling for work-item distribution, such work items will be distributed with a push method, i.e. a work item is pushed to a single qualifying resource. This is also related to the fact that the jobs are usually assumed to be executed by machines, whereas, in process-aware information systems, work items are normally being executed by human resources. Work items may also be executed by automatic software services, but this is not the situation in the majority of settings. In [16], it is shown that push strategies already perform very poorly when the resource work-load is moderately high. Therefore, work items ought to be distributed with a pull mechanism, i.e. enabled work items are put in a common pool and offered to qualifying resources, which can freely pick any of them. As a matter of fact, a pull method is by far the most common used in current-day process-aware information systems.

## 2.3. Operational support

The work proposed in this paper is also related to the body of work that is concerned with devising frameworks and architectures to provide operational support for business processes as a service. For instance, Nakatumba et al. [17] propose a service for operational support which generalizes what is proposed in [18]. This service is implemented in ProM, a pluggable framework to implement processaware techniques in a standardized environment. On its own, the service does not implement recommendation algorithms but provides an architecture where such algorithms can be easily plugged in. For instance, the prediction technique in [19] is an example of algorithm plugged into this architecture (more details on this work are provided in the next sub-section). Another example is the work in [20], which concerns a recommendation algorithm based on monitoring the satisfaction of business constraints. This work does not make any form of prediction nor automatic optimal work-item distribution.

As a matter of fact, there is no conceptual or technical limitation that would prevent our approach from being implemented as a plug-in for an operational-support service.

## 2.4. Work-item distribution

Our work on work-item distribution to minimize risks shares commonalities with Operational support and Decision Support Systems (DSSs). We aim to provide recommendations to process participants to take risk-informed decisions. Our work fully embraces the aim of these systems to improve decision making within work systems [30], by providing an extension to existing process-aware information systems.

Mainstream commercial and open-source BPM systems do not feature work-item prioritization. They only allow one to indicate a static priority for tasks (e.g. low, medium or high priority), independent of the characteristics of the process instance and of the quali<sup>fi</sup>ed resources. Similarly, the YAWL system, which is the one we extended, does not provide means for operational support, besides the extension proposed by de Leoni et al. [31], which, however, de<sup>fi</sup>nes very basic metrics only.

Several approaches have been proposed in the literature. Table 1 summarizes and compares the most signi<sup>fi</sup>cant ones, using different criteria:

Weight computation. In order to perform an optimal distribution, every work item needs to be assigned a weight, which may also depend on the resources that is going to perform it or on the moment in time when such work item is performed. These weights can be de<sup>fi</sup>ned either statically by analysts or dynamically computed on the basis of the past history recorded in an event log.

Process perspective. When weights are dynamically de<sup>fi</sup>ned, they may be computed considering different perspectives: control-<sup>fl</sup>ow, resources, data and time.

Optimal assignment. The optimization of work-item distribution can be computed by considering single instances in isolation or trying to optimize the overall performances of all running instances.

Objective. The work-item distribution can be optimized with respect to several factors, such as minimizing the cost, time or maximizing the cooperation. Only few approaches allow one to customize the objective function to minimize/maximize.

Assignment method. Once an optimal distribution is computed, each work item can be pushed to a single quali<sup>fi</sup>ed resource (push method), or it can be put in a common pool and simply recommended to a given resource within this pool, that can then pull the work item (pull method). Note that in this last method different resources within the same pool other than the one the work item was recommended to, may still execute the work-item method.

Comparison of different approaches for operational support in process-aware information systems.

<table><tr><td>Approach</td><td>Weight</td><td>Process perspectives computation</td><td>Optimal distribution</td><td>Objective</td><td>Assignment method</td></tr><tr><td>Kim et al. [21]</td><td>Dynamic</td><td>Control-flow, resource</td><td>-</td><td>Time, cost</td><td>-</td></tr><tr><td>Yang [22]</td><td>Static</td><td>-</td><td>Instance level</td><td>Customizable</td><td>PUSH</td></tr><tr><td>Kumar et al. [23]</td><td>Dynamic</td><td>Control-flow, resource</td><td>Instance level</td><td> $Cooperation^a$ </td><td>PUSH</td></tr><tr><td>Kumar et al. [16]</td><td>Static</td><td>-</td><td>Instance level</td><td>Suitability, urgency, workload</td><td> $PUSH/PULL^b$ </td></tr><tr><td>Huang et al. [24]</td><td>Dynamic</td><td>Control-flow, resource, data, time</td><td>Instance level</td><td>Customizable</td><td>PUSH</td></tr><tr><td>van der Aalst et al. [25]</td><td>Dynamic</td><td>Control-flow</td><td>-</td><td>Time</td><td>-</td></tr><tr><td>Folino et al. [26]</td><td>Dynamic</td><td>Control-flow, resource, data, time</td><td>-</td><td>Time</td><td>-</td></tr><tr><td>van der Spoel et al. [27]</td><td>Dynamic</td><td>Control-flow</td><td>-</td><td>Cost</td><td>-</td></tr><tr><td>Cabanillas et al. [28]</td><td>Static</td><td>Control-flow, resource</td><td>Process level</td><td> $User preference^c$ </td><td>PUSH</td></tr><tr><td>Barba et al. [29]</td><td>Static</td><td>Control-flow, resource</td><td>Instance level</td><td>Time</td><td>PULL</td></tr><tr><td>Maggi et al. [19]</td><td>Dynamic</td><td>Control-flow, resource, data</td><td>-</td><td> $Customizable LTL formulas^d$ </td><td>-</td></tr></table>

<sup>a</sup> Work items are distributed to maximize the quality of the cooperation among resources. This approach assumes that some resources can cooperate better than others when working on a process instance.  
<sup>b</sup> Resources declare their interest in picking some work items for performance. The approach assigns each work item to the interested resource that guarantees the better distribution.  
<sup>c</sup> At design time, users provide preferences for work items. At run time, the system allocates work items to resources to maximize such preferences.  
<sup>d</sup> The expressiveness power of business goals in the form of a single LTL formula is lower than what our approach allows for. In principle, multiple LTL formulas can be provided though one has to balance contrasting recommendations for the satis<sup>fi</sup>ability of such formulas.

Among the available approaches only the one by Cabanillas et al. [28] computes the optimal allocation of resources at the process level. Speci<sup>fi</sup>cally, this work proposes a priority-based resource allocation, where resources are ranked according to preferences de<sup>fi</sup>ned using the Semantic Ontology of User Preferences [32]. Once a work item needs to be executed it is pushed to the resource ranking the highest on the basis of the expressed preferences.

Among the approaches providing optimal distribution only two approaches support a pull assignment. The approach of Barba et al. [29] optimizes process performances, using constraint programming (planning and scheduling problem) where constrains are de<sup>fi</sup>ned considering control-<sup>fl</sup>ow and resources only. On the other hand, the approach of Kumar et al. [16] aims to obtain the right balance between execution time and quality. This approach uses work allocation metrics and various quality attributes to <sup>fi</sup>nd the optimal allocation strategy keeping into consideration the preference of resources for certain work items.

The approach of Yang [22], similar to all the approaches discussed so far, assigns a static weight to each work item. This approach optimizes process execution time and total execution cost according to user preferences. Preferences are de<sup>fi</sup>ned using a multi-attribute utility function that is optimized using the particle swarm optimization algorithm. A second approach by Kumar et al. [23], and the approach of Huang et al. [24], conclude the list of approaches providing optimal distribution of work items. Kumar et al. [23] propose an approach for optimal resource cooperation using integer linear programming to identify the group of resources with the best synergy to perform a process instance while Huang et al. [24] propose to use task operation models.

There are also approaches that focus on prediction only. van der Aalst et al. [25] propose an approach to predict total execution time and remaining execution time. The approach uses logs to generate transition systems annotated with timing information. Transition systems are employed to provide predictions using similarly completed executions as a reference. Folino et al. [26] use a combination of clustering techniques and transition systems. Using clustering they identify process variants in a log and for each cluster they generate a transition system. When a prediction is required, using decision trees the authors identify which cluster the current instance belongs to, and then use the associated transition system to provide a prediction.

van der Spoel et al. [27] propose an approach to predict the cash <sup>fl</sup>ow of a process. This approach uses a combination of process <sup>fl</sup>ow prediction, i.e. predicting how the process execution will proceed, and cost prediction, i.e. predicting how much the execution of a predicted activity will cost. Kim et al. [21] propose the use of decision trees to minimize completion time or total labor cost, where the resource with the lowest predicted completion time or total labor cost is suggested.

Finally, Maggi et al. [19] propose a predictive approach to prevent process constraint violation. Users can de<sup>fi</sup>ne linear temporal logic constraints at any point in time during the execution of a process. Then, when a prediction is required, the approach retrieves all traces having a similar pre<sup>fi</sup>x of the current instance. These instances are then used to generate a decision tree that is used to predict how the process execution should proceed to satisfy the prede<sup>fi</sup>ned constraints.

There are also approaches (e.g., [33–35]) that mine association rules from event logs to de<sup>fi</sup>ne the preferable distribution of work items. However, in the end a resource manager needs to manually assign work items to resources. Manual distributions are clearly inef<sup>fi</sup>cient because they are both unlikely to be optimal and some work items probably remain unassigned for a certain amount of time until the manager takes charge of their assignment. Moreover, the mined rules consider process instances in isolation.

On the basis of the insights emerging from Table 1, we propose a technique that satis<sup>fi</sup>es the following requirements: it should i) use information from different process perspectives to provide predictions; ii) use such predictions to compute an optimal distribution that is not local to individual process instances (instance level) but global across all running instances, which can be from different processes (process level); iii) use user-de<sup>fi</sup>ned faults as objective functions; and iv) leave process participants the <sup>fi</sup>nal choice of whether to execute a recommended work item (pull assignment method).

This paper is an extended version of the conference paper in [36]. With respect to the conference paper, the main extension relates to the provision of support for multi-instance risk prediction. This is achieved by combining our existing technique for risk estimation [36], with a technique for identifying the best distribution of resources to work items of concurrent process instances, using integer linear programming. This technique has been implemented via a new YAWL custom service, the Multi-Instance Prediction Service. Further, the evaluation has been completely redone using a real-life business process in use at a large insurance company. With input from a team of risk analysts from the company, this process has been extensively simulated on the basis of an event log recording one year of completed instances of this process, to show that it is feasible to predict risks across multiple process instances without impacting on performance, and that the recommendations provided by our recommendation system signi<sup>fi</sup>cantly reduce the number and severity of faults, for all instances simulated.

## 3. Risk framework

In this section we elaborate on the type of process-related risks that we can address and on the basis of this, we illustrate an overarching approach for managing process-related risks within which the contribution of this paper <sup>fi</sup>ts.

## 3.1. Process-related risk

In this paper we focus on process-related risks that can be identi<sup>fi</sup>ed within the boundaries of a business process. In particular, we only consider process-related risks which depend on information available during process execution, e.g. task input and output data, allocated resources, time performance. This implies that process-related risks depending on information outside the process boundaries, i.e. the process context (e.g. market <sup>fl</sup>uctuations or weather forecast), cannot be detected. For this reason organizational risks in general are not addressed, such as those related to partners going bankrupt, or price of the fuel going up. Moreover, since we require process execution information we only consider executable business processes. These processes should either be executed by a BPMS on the basis of a process model or be supported by an information system that produces event logs [37], i.e. logs of process-related information which we can use to reconstruct the process instances being executed by aggregating events, such that each instance can be unequivocally identi<sup>fi</sup>ed.

## 3.2. Risk approach

The technique proposed in this paper can be seen as part of a wider approach for the management of process-related risks. This approach aims to enrich the four phases of the traditional BPM lifecycle (Process Design, Implementation, Enactment and Diagnosis) [38] with elements of risk management (cf. Fig. 1).

Before the Process Design phase, we de<sup>fi</sup>ne an initial phase, namely Risk Identification, where existing techniques for risk analysis such as Fault Tree Analysis [39] or Root Cause Analysis [40] can be used to identify possible risks of faults that may eventuate during the execution of a business process. Faults and their risks identi<sup>fi</sup>ed in this phase are mapped onto speci<sup>fi</sup>c aspects of the process model during the Process Design phase, obtaining a risk-annotated process model. In the Process Implementation phase, a more detailed mapping is conducted linking each risk and fault to speci<sup>fi</sup>c aspects of the process model, such as the content of data variables and resource states. In the Process Enactment phase such a risk-annotated process model can be executed to ensure risk-aware process execution. Finally, in the Process Diagnosis phase, information produced during Process Enactment is used in combination with historical data to monitor the occurrence of risks and faults as process instances are executed. This monitoring may trigger mitigation actions in order to (partially) recover the process instance from a fault.

![](/api/attachments/UPEAC38D/fulltext/images/c51adb30b7867b534f1b9d4c2ce9d2af77adcfc93280f5741c820d30d002194c.jpg)  
Fig. 1. Risk-aware BPM lifecycle

The technique presented in this paper <sup>fi</sup>ts in this latter phase, since it aims to provide run-time support in terms of risk prediction, by combining information on risks and faults with historical data. The techniques developed to support the other phases of our risk-aware BPM approach fall outside the scope of this paper, but have been addressed in our earlier work [3,5,4].

## 4. YAWL speci<sup>fi</sup>cation and running example

We developed our technique on top of the YAWL language [41] for several reasons. First, this language is very expressive as it provides a comprehensive support for the work<sup>fl</sup>ow patterns,<sup>2</sup> patterns covering all main process perspectives such as control-<sup>fl</sup>ow, data-<sup>fl</sup>ow, resources, and exceptions. Further, it is an executable language supported by an open-source BPM system, namely the YAWL System. This system is based on a service-oriented architecture, which facilitates the seamless addition of new services, like the ones developed as part of this work. Further, the open-source license facilitates its distribution among academics and practitioners (the system has been downloaded over 100,000 times since its <sup>fi</sup>rst inception in the open-source community). However the elements of the YAWL language used by our technique are common to all process modeling languages, so our technique can in principle be applied to other executable process modeling languages such as BPMN 2.0.

In this section we introduce the basic ingredients of the YAWL language and present them in the context of a running example. This example, whose YAWL model is shown in Fig. 2, captures the Carrier Appointment sub-process of an Order Ful<sup>fi</sup>llment process, which is subjected to several risks. This process is inspired by the VICS industry standard for logistics [42], a standard endorsed by 100+ companies worldwide.

The Carrier Appointment sub-process (see Fig. 2) starts when a Purchase Order Con<sup>fi</sup>rmation is received. A Shipment Planner then estimates the trailer usage and prepares a route guide. Once ready, a Supply Of<sup>fi</sup>cer prepares a quote for the transportation indicating the cost of the shipment, the number of packages and the total freight volume.

If the total volume is over 10,000 lb a full truckload is required. In this case two different Client Liaisons will try to arrange a pickup appointment and a delivery appointment. Before these two tasks are performed, a Senior Supply Of<sup>fi</sup>cer may create a Shipment Information document. In case the Shipment Information document is prepared before the appointments are arranged, a Warehouse Of<sup>fi</sup>cer will arrange a pickup appointment and a Supply Of<sup>fi</sup>cer will arrange a delivery appointment, with the possibility of modifying these appointments until a Warehouse Admin Of<sup>fi</sup>cer produces a Shipment Notice, after which the freight will be picked up from the Warehouse.

If the total volume is up to 10,000 lb and there is more than one package, a Warehouse Of<sup>fi</sup>cer arranges the pickup appointment while a Client Liaison may arrange the delivery appointment. Afterwards, a Senior Supply Of<sup>fi</sup>cer creates a Bill of Lading, a document similar to the Shipment Information. If a delivery appointment is missing a Supply Of<sup>fi</sup>cer takes care of it, after which the rest of the process is the same as for the full truckload option.

Finally, if a single package is to be shipped, a Supply Of<sup>fi</sup>cer has to arrange a pickup appointment, a delivery appointment, and create a Carrier Manifest, after which a Warehouse Admin Of<sup>fi</sup>cer can produce a Shipment Notice.

In YAWL, a process model is encoded via a YAWL speci<sup>fi</sup>cation. A speci<sup>fi</sup>cation is made up of one or more nets (each modeling a sub-process), organized hierarchically in a root net and zero or more sub-nets. Each net is de<sup>fi</sup>ned as a set of conditions (represented as circles), an input condition, an output condition, and a set of tasks (represented as boxes). Tasks are connected to conditions via <sup>fl</sup>ow relations (represented as arcs). In YAWL trivial conditions, i.e. those having a single incoming <sup>fl</sup>ow and a single outgoing <sup>fl</sup>ow, can be hidden. To simplify the discussion in the paper, without loss of generality, we assume a strict alternation between tasks and conditions.

Conditions denote states of execution, for example the state before executing a task or that resulting from its execution. Conditions can also be used for routing purposes when they have more than one incoming and/ or outgoing <sup>fl</sup>ow relation. In particular, a condition followed by multiple tasks, like condition FTL in Fig. 2, represents a deferred choice, i.e. a choice which is not determined by some process data, but rather by the <sup>fi</sup>rst process participant that is going to start one of the outgoing tasks of this condition. In the example, the deferred choice is between tasks Arrange

![](/api/attachments/UPEAC38D/fulltext/images/e1080650db75cb57a2b8b531a52782029055def432552dba91df4dce1ab135c2.jpg)  
Fig. 2. The carrier appointment sub-process of an order ful<sup>fi</sup>llment process, shown in YAWL.

Delivery Appointment, Arrange Pickup Appointment and Create Shipment Information Document, each assigned to a different process participant. When the choice is based on data, this is captured in YAWL by an XOR-split, if only one outgoing arc can be taken like after executing Prepare Transportation Quote. If one or more outgoing arcs can be taken it is captured by an OR-split like after executing Create Shipment Information Document. Similarly, we have XOR-joins and ORjoins that merge multiple incoming arcs in to one. If among all the incoming arcs only one is active we use a XOR-join like before executing Produce Shipment Notice, while if among all incoming arcs one or more arcs are active we use an OR-join like before executing task Create Bill of Lading. Finally, an AND-split is used when all outgoing arcs need to be taken, like after Receive Con<sup>fi</sup>rmation Order, while an AND-join is used to synchronize parallel arcs like before executing Prepare Transportation Quote. Splits and joins are represented as decorators on the task's box.

Tasks are considered to be descriptions of a piece of work that forms part of the overall process. Thus, control-<sup>fl</sup>ow, data, and resourcing speci<sup>fi</sup>cations are all de<sup>fi</sup>ned with reference to tasks at design time. At run-time, each task acts as a template for the instantiation of one or more work items. A work item w = (ta, id) is the run-time instantiation of a task ta for a process instance id.

A new process instance id is started and initialized by placing a token in the input condition of a YAWL net. The token represents the thread of control and <sup>fl</sup>ows through the net as work items are executed. The execution of a work item (ta, id) consumes one token from some of ta's input conditions (depending on the task's type of join) and produces one token in some of ta's output conditions (depending on the task's type of split). In YAWL, work items are performed by either process participants (user tasks) or software services (automated tasks). An example of an automated task is Receive Con<sup>fi</sup>rmation Order in Fig. 2, while an example of user task is Estimate Trailer Usage.

Finally, the preset <sup>•</sup>t of a task t is the set of its input conditions. Similarly, the postset t<sup>•</sup> of a task t is the set of its output conditions. The preset and postset of a condition can be de<sup>fi</sup>ned analogously.

The notions presented above are formalized in A.

## 5. Event logs and fault severity

The execution of completed and running process instances can be stored in an event log:

## De<sup>fi</sup>nition 1. Event log

Let T and V be a set of tasks and variables, respectively. Let U be the set of values that can be assigned to variables. Let R be the set of resources that are potentially involved during the execution. Let D be the universe of timestamps. Let Φ be the set of all partial functions V U that de<sup>fi</sup>ne an assignment of values to a sub-set of variables in V. An event log is a multi-set of traces where each trace (a.k.a. process <sup>L</sup>instance) is a sequence of events of the form $( t , r , d , \phi )$ , where t T is a task, r ∈ R is the resource performing t, d ∈ ℕ is the event's timestamp, and ϕ ∈ Φ is an assignment of values to a sub-set of variables in V. In other words, $\mathcal { L } \in \mathcal { B } ( ( T \times R \times \mathbb { N } \times \phi ) ^ { * } ) .$ 3

Each completed trace of the event log is assigned a fault's severity between 0 and 1, where 0 identi<sup>fi</sup>es an execution with no fault and 1 identi<sup>fi</sup>es a fault with the highest severity. To model this, a risk analyst needs to provide a fault function f. The set of all such functions is:

$$
\mathcal {F} = (T \times R \times \mathbb {N} \times \Phi) ^ {*} \rightarrow [ 0, 1 ].
$$

In many settings, processes are associated with different faults. These faults can be combined together by assigning different weights. Let us suppose to have n faults $\{ f _ { 1 } , . . . , f _ { n } \} \subset { \mathcal { F } }$ , we can have a composite fault:

$$
\hat {f} (\sigma) = \frac {\sum_ {1 \leq i \leq n} w _ {i} f _ {i} (\sigma)}{\sum_ {1 \leq i \leq n} w _ {i}} \in \mathcal {F}
$$

where w is the weight of the fault f , with $1 \leq i \leq n$

A complete trace σ of our Carrier Appointment process can be affected by three faults:

Over-time fault. This fault is linked to a Service Level Agreement (SLA) which establishes that the process must terminate within a prede<sup>fi</sup>ned Maximum Cycle Time $d _ { m c t } \left( \mathbf { e . g . } 2 1 \mathrm { ~ h } \right)$ , in order to avoid pecuniary penalties that will incur as a consequence of a violation of the SLA. The severity of the fault grows with the amount of time that the process execution exceeds $d _ { m c t } .$ . Let $d _ { \sigma }$ be the duration of the process instance, i.e. difference between the timestamps of the last and the <sup>fi</sup>rst event of $\sigma .$ Let $d _ { m a x }$ be the maximum duration among all process instances already completed (including σ). The severity of an overtime fault is measured as follows:

$$
f _ {t i m e} (\sigma) = \max \left(\frac {d _ {\sigma} - d _ {m c t}}{\max (d _ {m a x} - d _ {m c t} , 1)}, 0\right).
$$

Reputation-loss fault. During the execution of the process when a “pickup appointment” or a “delivery appointment” is arranged, errors with location or time of the appointment may occur due to a misunderstanding between the company's employee and the customer. In order to keep the reputation high, the company wants to avoid these misunderstandings and having to call the customer again. The severity of this fault is:

$$
f _ {r e p} (\sigma) = \left\{ \begin{array}{l l} 0 & \text { if   tasks   Modify   Delivery   Appointment   and } \\ & \text { Modify   Pick - up   Appointment   do   not   appear   in   } \sigma \\ 1 & \text { if   both   Modify   Delivery   Appointment   and } \\ & \text { Modify   Pick - up   Appointment   appear   in   } \sigma \\ 0. 5 & \text { otherwise. } \end{array} \right.
$$

Cost overrun fault. During the execution of this process, several activities need to be executed, and each of these has an execution cost associated with it. Since the pro<sup>fi</sup>t of the company decreases with a higher shipping cost of a good (or goods), the company wants to reduce them. Of course, there is a pro<sup>fi</sup>t cost beyond which the company will not make any pro<sup>fi</sup>t. The severity increases as the cost goes beyond the pro<sup>fi</sup>t cost. Let $c _ { \mathrm { m a x } }$ be the greatest cost associated with any process instance that has already been completed (including $\sigma )$ . Let $c _ { \sigma }$ be the cost of σ and $c _ { \mathrm { m i n } }$ be the pro<sup>fi</sup>t cost. The severity of a cost fault is:

$$
f _ {c o s t} (\sigma) = \min \left(\frac {\max (c _ {\sigma} - c _ {\min} , 0)}{\max (c _ {\max} - c _ {\min} , 1)}, 1\right).
$$

Moreover, we assume that the company considers Reputation-loss fault to be less signi<sup>fi</sup>cant than the other faults. The company could decide to de<sup>fi</sup>ne a composite fault where the reputation weights half:

$$
f _ {c a r} (\sigma) = \left(f _ {c o s t} (\sigma) + f _ {t i m e} (\sigma) + 0. 5 \cdot f _ {r e p} (\sigma)\right) / 2. 5.
$$

The risk is the product of the estimation of the fault's severity at the end of the process instance execution and the accuracy of such an estimation.

When a process instance is being executed, many factors may in<sup>fl</sup>uence the risk and, ultimately, the severity of a possible fault. For instance, a speci<sup>fi</sup>c order in which a certain set of tasks is performed may increase or decrease the risk, compared to any other. Nonetheless, it is opportune to leave freedom to resources to decide the order of their preference. Indeed, there may be factors outside the system that let resources opt for a speci<sup>fi</sup>c order. For similar reasons, when there are alternative tasks that are all enabled for execution, a risk-aware decision support may highlight those tasks whose execution yields less risk, anyway leaving the <sup>fi</sup>nal decision up to the resource.

## 6. Risk estimation

We aim to provide work-item recommendation to minimize the risk corresponding to the highest product of fault severity and likelihood. For this purpose, it is necessary to predict the most likely fault severity associated with continuing the execution of a process instance for each enabled task. The problem of providing such a prediction can be translated into the problem of <sup>fi</sup>nding the best estimator of a function.

## De<sup>fi</sup>nition 2. Function estimator

Let $X _ { 1 } , . . . , X _ { n }$ be n <sup>fi</sup>nite or in<sup>fi</sup>nite domains. Let Y be a <sup>fi</sup>nite domain. Let $f \colon X _ { 1 } \times X _ { 2 } \times \ldots \times X _ { n } \to Y .$ An estimator of function f is a function $\psi _ { f } : Y {  } 2 ^ { X _ { 1 } \times X _ { 2 } \times . . . \times X _ { n } \times [ 0 , 1 ] }$ , such that, for each $y \in Y , \psi _ { f } ( y )$ returns a set of tuples $( x _ { 1 } , . . . , x _ { n } , l )$ where $( x _ { 1 } , . . . , x _ { n } ) \in ( X _ { 1 } \times X _ { 2 } \times . . . \times X _ { n } )$ is an input domain tuple for which the expected output is y and l is the accuracy of such an estimation. Moreover, $( x _ { 1 } , . . . , x _ { n } , l _ { 1 } ) \in \psi _ { f } ( y _ { 1 } )$ ∧ $( x _ { 1 } , . . . , x _ { n } , l _ { 2 } ) \in \psi _ { f } ( y _ { 2 } ) \Rightarrow l _ { 1 } = l _ { 2 } \wedge y _ { 1 } = y _ { 2 } .$

The function estimator is trained through a set of observation instances. An observation instance is a pair $\left( { \overrightarrow { x } } , y \right)$ <sup></sup>where ${ \overrightarrow { x } } \in X _ { 1 } \times X _ { 2 } \times$ $\dots \times X _ { n }$ is the observed input and $y \in Y$ is the observed output.

<sup>-</sup>The function estimator can easily be built using a number of machine learning techniques. In this paper, we employ the C4.5 algorithm to build decision trees. We decided to use decision tree classi<sup>fi</sup>cation, and speci<sup>fi</sup>cally the C4.5 algorithm, for the following reasons: i) it can handle both continuous and discrete (categorical) attributes; ii) it can handle training data with missing attribute values; iii) it can build models that can be easily interpreted; iv) it can deal with noise; v) it automatically <sup>fi</sup>nds a sub-set of the features that are relevant to the classi<sup>fi</sup>cation (i.e. no need for feature selection); and vi) it automatically discretizes continuous features. This last function helps us signi<sup>fi</sup>cantly simplify the problem of <sup>fi</sup>nding an optimal distribution of work items to resources, as we will discuss in Section 7.

Decision trees classify instances by sorting them down in a tree from the root to some leaf node. Each non-leaf node speci<sup>fi</sup>es a test of some attribute $x _ { 1 } , ~ . . . , ~ x _ { n }$ and each branch descending from that node corresponds to a range of possible values for this attribute. In general, a decision tree represents a disjunction of conjunctions of expressions: each path from the tree root to a leaf corresponds to an expression that ${ \mathrm { i } } s ,$ in fact, a conjunction of attribute tests. Each leaf node is assigned one of the possible output values: if an expression e is associated with a path to a leaf node y, every tuple ${ \overrightarrow { x } } \in X _ { 1 } \times X _ { 2 } \times \ldots \times X _ { n }$ satisfying e is expected to return y as output.

We link the accuracy of a prediction for $\psi _ { f } ( \overline { { y } } )$ to the quality of e as classifying expression. Let I be the set of observation instances used to construct the decision tree. Let $I _ { e } = \left\{ \left( { \overrightarrow { x } } , y \right) \in I { \Big | } { \overrightarrow { x } } \right.$ satisfies $e \}$ and $I _ { e , y } = \left\{ \left( { \overrightarrow { x } } , y \right) \in I _ { e } \middle | y = { \overline { { y } } } \right\}$ . The accuracy is $l = | I _ { e , \overline { { y } } } | / | I _ { e } | ;$ therefore, for all $( ( x _ { 1 } , . . . , x _ { n } ) , y ) \in I _ { e } , ( x _ { 1 } , . . . , x _ { n } , l ) \in \psi _ { f } ( \overline { { y } } )$

<sup>ð Þð Þ ð Þ ð Þ</sup>Fig. 3 shows an example of a possible decision tree. It is the estimator $\boldsymbol { \psi } _ { f _ { \hat { \boldsymbol { r } } } }$ of a function that returns a value belonging to the set H containing the numbers between 0 and 1 with no more than 2 decimals. It is obtained through a set of observation instances based on all data attributes generated during the execution of the process. For example, having as data attributes a resource, a task, the cost of a good, and a process instance's elapsed time, we obtained the following function $f _ { \hat { c } }$ : Resource × Task × GoodCost × TimeElapsed → H. For instance, let us consider the value $y = 0 . 6 .$ . Analyzing the tree, the value is associated with two expressions: $e _ { 1 }$ is (Resource = MichaelBrown ∧ Task = ArrangePickupAppointment) and $e _ { 2 }$ is (Resource ≠ MichaelBrown ∧ GoodCost b 3157 ∧ TimeElapsed $< 3 0 \mathrm { ~ } \land \mathrm { ~ } T a s k =$

![](/api/attachments/UPEAC38D/fulltext/images/b9d3d276ed222bc56f858eae56ab5cbe83661f3b9f1568ba969e6625f8b91a81.jpg)  
Fig. 3. An example of decision tree used to build a function estimator.

CreateShipmentInformationDocument). Let us suppose that, among observation instances (Resource, Task, GoodCost, TimeElapsed, y) s.t. $e _ { 1 }$ or e evaluates to true, $y = 0 . 6$ occurs 60% or 80% of times, respectively. Therefore, $\psi _ { f _ { \hat { r } } } ( 0 . 6 )$ contains the tuples (Resource, Task, GoodCost, TimeElapsed, $\stackrel { \cdot } { 0 . 6 } )$ <sup>Þ</sup>satisfying $e _ { 1 }$ , along with tuples (Resource, Task, GoodCost, TimeElapsed, 0.8) satisfying $e _ { 2 } .$ Regarding computational complexity, if decision trees are used, training ψ with m observation instances is computed in quadratic time with respect to the dimension n (i.e. the number of attributes) of the input tuple, speci<sup>fi</sup>cally $O ( n ^ { 2 } \cdot m )$ [43].

As mentioned before, it is necessary to predict the most likely fault severity associated with continuing the execution of a process instance with each task enabled for execution. Function estimators are used for such a prediction.

Let $\hat { N } = ( T _ { N } , C _ { N } , R _ { N } , V _ { N } , U _ { N } , c a n _ { N } )$ be a YAWL net. In order to provide accurate risks associated with performing work items of a certain process instance, it is important to incorporate the execution history of that process instance into the analysis. In order to avoid over<sup>fi</sup>tting predictive functions the history needs to be abstracted. Speci<sup>fi</sup>cally, we abstract the execution history as two functions: $C _ { r } { : } T _ { N } {  } R$ denoting the last executor of each task and $C _ { t } : T _ { N } $ ℕ denoting the number of times that each task has been performed in the past. Pairs $\left( c _ { r } , c _ { t } \right)$ ∈ $C _ { r } \times C _ { t }$ are called contextual information. Given the execution trace of a (running) instance $\sigma ^ { \prime } \in ( T _ { N } \times R _ { N } \times \mathbb { N } \times \phi )$ , we introduce function getContextInformation(σ ′) that returns the contextual information $\left( c _ { r } , c _ { t } \right)$ that can be constructed from $\sigma ^ { \prime } .$

Let Φ be the set of all possible assignments of values to variables, i.e. the set of all partial functions $V _ { N } { \ A } U _ { N } .$ . Each condition $c \in C _ { N }$ can be associated with a function $f _ { c } : \phi \times c ^ { \bullet } \times R _ { N } \times \mathbb { N } \times C _ { r } \times C _ { t } \to H .$ . If $f _ { c } ( \phi , t , r , n , c _ { r } , c _ { t } ) = y ,$ at the end of the execution of the process instance, the fault's severity is going to be $y$ if the instance continues with resource $\boldsymbol r \in R _ { N }$ that performs task $t \in c ^ { \bullet }$ at time n with contextual information $\left( { { c _ { r } } , { c _ { t } } } \right)$ when variables are assigned values as for function ϕ. Of course, this function is not known but it needs to be estimated, based on the behavior observed in an event log . Therefore, we need to build an estimator $\psi _ { f _ { c } }$ for $f _ { c } .$ <sup>L</sup>Let us consider condition $c _ { F T L }$ (see Fig. 2), and the associated function estimator $\boldsymbol { \psi } _ { f _ { c _ { F T L } } }$ . Let us suppose that the accuracy is 1, i.e. for each $t { \in } c _ { F T L } \bullet _ { f _ { c _ { F T L } } } ( t )$ always returns 1.

If the execution is such that there is a token in FTL, GoodCost b 3157, executing tasks Arrange Pickup Appointment and Arrange Delivery Appointment are associated with a risk of 0.2 and 0.45, respectively. Conversely, executing task Create Shipment Information Document is given a risk of either 0.6 or 0.7, depending on the moment in which task Create Shipment Information Document is started. Therefore, it is evident that it is less “risky” to execute Arrange Pickup Appointment.

The generation of function estimators is obtained as follows. For each process instance in the log and for each event generated during the execution of each process instance, we retrieve context information, time elapsed, and data variables produced. These three elements together constitute an observation instance. This observation instance is assigned to the decision point which precedes the activity generating the event. Once all observation instances are generated, the observation instances associated with each decision point are used to build the function estimator associated with the decision point, using, for example, decision trees. In A we formalize this algorithm (see Algorithm 1).

In this section, we presented a technique to generate prediction functions. It is important to observe that the number of risks that may eventuate during the execution of a process does not affect the prediction algorithm, since we consider the combined risk level of all risks. Speci<sup>fi</sup>cally, we do so by assigning a relative weight to each risk. This weight system allows process administrators to <sup>fi</sup>ne tune the predictive function on the basis of the relative importance of each risk.

## 7. Multi-instance work-item distribution

With the technique presented so far, each resource is given local risk advice as to what work item to perform next, i.e. a resource is suggested to perform the work item with the lowest overall risk for that combination of process instance and resource, without looking at other resources that may be assigned work items within the same instance or in other instances running concurrently. Clearly, such a local workitem distribution is not optimal, since work items have to compete for resources and this may not guarantee the best allocation from a risk viewpoint. For example, let us consider two resources $r _ { 1 }$ and $r _ { 2 }$ and two work items $w _ { a }$ and $w _ { b }$ such that the risk of $r _ { 1 }$ performing $w _ { a }$ $0 . 2 ,$ and the risk of $r _ { 1 }$ performing $w _ { b }$ is $0 . 6 ,$ while the risk of $r _ { 2 }$ performing $w _ { a }$ is 0.1 and the risk of $r _ { 2 }$ performing $w _ { a }$ is 0.4. Moreover for the company executing these work items, it is equally important to minimize the eventuation of risks as well as the overall execution time. $\operatorname { I f } w _ { a }$ is assigned to $r _ { 2 }$ because locally this resource has the lowest risk, $r _ { 1 }$ will be forced to perform $w _ { b }$ leading to an overall risk of 0.7. Another option is to assign both work items to $r _ { 2 } ,$ yielding an overall risk of 0.5. Both these solutions are non-optimal distributions: the former because the overall risk is too high, the latter, despite the lower risk, because the workload between the two resources is unbalanced, with the result of increasing the overall execution time.

In this section we combine our technique for risk prediction with a technique for computing an optimal distribution of work items to resources (available or busy). By optimal distribution we mean a distribution that minimizes the weighted sum of overall execution time and overall risk across all running instances. In other words, the algorithm aims to balance the distribution of work items across resources while keeping the risk low. This distribution can then be used to provide work item recommendations to resources, such that these can be aided in selecting the best work item to perform. In the example above, the optimal distribution is $r _ { 1 } - w _ { a } { \mathrm { a n d } } r _ { 2 } - w _ { b }$ with an overall risk of 0.6. While this is higher than 0.5 obtained with the second solution, $r _ { 1 }$ and $r _ { 2 }$ will work in parallel thus reducing the overall execution time.

## 7.1. Optimal work-item distribution

Let f be a certain (composite) fault function and assuming we at time τ. Let $I = \{ i d _ { 1 } , . . . , i d _ { n } \}$ be the set of running instances of N. Given an instance id ∈ I, timeElapsed $( i d ) \in \mathbb { N }$ denotes the time elapsed since instance id has started and var $A s s i g n _ { \tau } ( i d ) \in ( V _ { N } \to U _ { N } )$ is the current assignment of values to variables. Moreover, let us denote a function $u s e _ { N } : R _ { N } {  } 2 ^ { T _ { N } \times I }$ that associates each resource with the work items that he/she is executing within the set I of running process instances. Let WE be the set of work items being executed, i.e. $W E = \sum _ { r \in R _ { N } } u s e _ { N } ( r ) .$

Let $W \subseteq T _ { N } \times$ I be the set of work items that are enabled but not started yet. Section 4 has discussed the concept of deferred choice, highlighting that some of the enabled work items are mutually exclusive. Therefore, we introduce an equivalence relation \~ between elements of $W ,$ such that $w _ { a } \sim w _ { b }$ if, picking $w _ { a } \in W$ for execution disables $w _ { b } \in W$ or vice versa. Let W be the partition of W according to relation \~.

For each enabled work item $w \in W ,$ , we perform an estimation time(w) of the expected duration of work item w. For each started work item $\prime \in W E$ , we also perform an estimation time(w) of the amount of time needed by w to be completed. To compute such estimations, we employ the technique proposed in [25] using event log as input.

<sup>L</sup>Let Ψ be the set of function estimators that are computed through Algorithm 1, using net $N ,$ event log $\mathcal { L }$ and given fault function f as input. For each work item $w \in W ,$ let us denote with $r i s k _ { r , w , t }$ the risk of starting a work item w at time t. For example, given a work item w, this can be computed by retrieving the estimation function associated with each decision point preceding w and taking the maximum value of the predicted risk: $r i s k _ { r , w , t } = \tt c a l c R i s k ( N , \uparrow , r , t , w , \Psi )$ <sup>¼ ð</sup>See Algorithm 2 in A for a formal de<sup>fi</sup>nition of this algorithm.

$\mathrm { L e t } m a x T i m e = \sum _ { w \in W \cup W E } t i m e ( w )$ be the maximum duration of execut-

ing all work items that are currently enabled and started. This corresponds to the situation in which work items are just executed sequentially, i.e. a new work item starts only when no other work item is being executed. Given a resource $r \in R _ { N }$ and a work item $( t a , i d ) \in W$ such that $t a \in c a n _ { N } ( r )$ , we compute the set of moments in time in which the risk of r performing $( t a , i d ) : s t a r t _ { r , w } = \{ t \in [ \tau , \tau +$ maxTime] $\Vert r i s k _ { r , w , t } \neq r i s k _ { r , w , t - 1 } \} \cup \{ \tau \}$

Certainly, this can be naively computed by computing the risk for all moments in time between τ and τ + maxTime. Nonetheless, it can be done more ef<sup>fi</sup>ciently by observing the occurrences of splits on the time variable that are present in the decision trees. For instance, let us consider the decision tree in Fig. 3: the only time reference is 30. This reference occurs in a root-to-leaf path in which resource $r \neq$ Michael Brown and Task = Create Shipment Information. Therefore, for each resource $r \in R \ \backslash$ {Michael Brown} and work item $w =$ (Create Shipment Information, $i d ) \in W , s t a r t _ { r , w } = \{ \tau ,$ elapsed(id) + 30}, Moreover, for each work item $w = ( t a , i d ) \in W$ with ta ≠ Create Shipment Information and for each resource $r \in R , s t a r t _ { r , w } =$ {τ}. Similarly, for each work item $w = ( t a , i d ) { \in } W , s t a r t _ { r ^ { \prime } , w } = \{ \tau \}$ with $r ^ { \prime } =$ Michael Brown.

Given a work item w, a resource r and a time $t , \Delta _ { r , w } ( t )$ denotes the <sup>fi</sup>rst moment t′ in time after t in which the risk changes, i.e. $t ^ { \prime } > t , t ^ { \prime } \in$ $s t a r t _ { r , w }$ and there exists no $t ^ { \prime \prime } \in s t a r t _ { r , w }$ such that $t ^ { \prime } > t ^ { \prime \prime } > t$ . If such a moment t′ does not exist, $\Delta _ { r , w } ( t ) = \tau +$ maxTime.

We formulate the problem of distributing work items as a Mixedinteger Linear Programming (MILP) problem. The following two sets of variables are introduced:

• for each resource $\boldsymbol { r } \in { \boldsymbol { R } } _ { N }$ and work item $w = ( t a , i d ) \in W$ such that $t a \in c a n _ { N } ( r )$ , there exists a variable $x _ { r , w , t } .$ . If the solution of the MILP problem is such that $x _ { r , w , t } = 1$ , r is expected to start performing w in interval between t and $\Delta _ { r , w } ( t ) , x _ { r , w , t } = 1$ ; otherwise, $x _ { r , w , t } = 0 ;$

• for each work item w ∈ W ∪ WE (i.e., running or enabled), we introduce a variable $w a _ { r , w } .$ If work item w is not being executed at time τ and is eventually distributed to resource $r ,$ the MILP solution assigns to $w a _ { r , w }$ a value that is equal to the moment in time when resource r is expected to start work item w. If w is not expected to be started by $r , w a _ { r , w } = 0 ;$ ; if w is already being executed by r at time τ $( \mathrm { i . e . } ~ w \in W E ) , w a _ { r , w }$ is statically assigned value τ.

The MILP problem aims to minimize the weighted sum of the expected total execution time and the overall risk:

$$
\min \left(\frac {\alpha}{\text { maxTime }} \sum_ {r \in R _ {N}} \sum_ {w \in W \cup W E} w a _ {r, w} + (1 - \alpha) \sum_ {r \in R _ {N}} \sum_ {w \in W \cap c a n _ {N (r)}} \sum_ {t \in s t a r t _ {r, w}} r i s k _ {r, w, t} \cdot x _ {r, w, t}\right)
$$

where $\alpha \in [ 0 , 1 ]$ is the weight of the expected total execution time w.r.t. the overall risk.

This MILP problem is subject to a number of constraints:

• for each $\boldsymbol { r } \in { \boldsymbol { R } } _ { N }$ and $w = ( t a , i d ) \in W$ such that ta $\in c a n _ { N } ( r )$ , if r starts performing w in the interval between t and $\Delta _ { r , w } ( t ) , x _ { r , w , t }$ must be equal to 1 (and vice versa):

$$
x _ {r, w, t} = 1 \Longleftrightarrow \Delta_ {r, w} (t) > w a _ {r, w} \wedge w a _ {r, w} \geq t;\tag{1}
$$

• For each partition $D \in W _ { \sim }$ , only one work item in D can be executed and it can only be executed by one resource and can only start within one interval:

$$
\sum_ {r \in R _ {N}} \sum_ {w \in D \cap c a n _ {N (r)}} \sum_ {t \in s t a r t _ {r, w}} x _ {r, w, t} = 1.\tag{2}
$$

• Every resource $r \in R _ { N }$ cannot execute more than one work item at any time. Therefore, for each $r \in R _ { N }$ and for each pair of partitions $D _ { 1 } , D _ { 2 } \in W _ { \sim }$ :

$$
\begin{array}{l} \left(\sum_ {w _ {a} \in D _ {1}} w a _ {r, w _ {a}} - \sum_ {w _ {b} \in D _ {2}} w a _ {r, w _ {b}} \geq \sum_ {w _ {b} \in D _ {2}} \sum_ {t \in s t a r t _ {r, w _ {b}}} t i m e (w _ {b}) \cdot x _ {r, w _ {b}, t}\right) \\ \quad \vee \left(\sum_ {w _ {b} \in D _ {2}} w a _ {r, w _ {b}} - \sum_ {w _ {a} \in D _ {1}} w a _ {r, w _ {a}} \geq \sum_ {w _ {a} \in D _ {1}} \sum_ {t \in s t a r t _ {r, w _ {a}}} t i m e (w _ {a}) \cdot x _ {r, w _ {a}, t}\right). \end{array}\tag{3}
$$

In A, we show how constraints in Eq. (1) and in Eq. (3) can be translated into an equivalent set of linear constraints.

We observe that we can compute $\Delta _ { r , w } ( t )$ only if we use a machine-learning method, such as decision trees, that can automatically discretize continuous features such as the time feature in this case. By automatically identifying those time moments that discriminate over risk values, we can split the time feature in time intervals and thus base our predictions on such intervals (e.g., “if elapsed time b t OR elapsed time ≥ t”) instead of working with individual time moments (“if elapsed time $= t _ { 1 }$ OR elapsed time $= t _ { 2 }$ OR elapsed ${ \mathrm { t i m e } } = t _ { 3 } . . . ^ { \ " } )$ . If such automatic discretization of continuous features was not available, we could not compute $\Delta _ { r , w } ( t )$ and consequently we would need to introduce a different variable $x _ { r , w , t }$ for each moment t in time. This would lead to an increase of the complexity of <sup>fi</sup>nding a solution to the MILP problem, which is exponential on the number of variables.

As an example of an instance of the class of MILP problems, let us consider a case where at time τ we want to schedule three work items $w _ { a } ,$ w and $w _ { c } ,$ and we have two resources, $r _ { 1 }$ and $r _ { 2 } ,$ , who can perform them. We know that $w _ { a }$ and $w _ { b }$ are mutually exclusive generating the following partitions $D _ { 1 } = \{ w _ { a } , w _ { b } \}$ , and $D _ { 2 } = \{ w _ { c } \}$ Moreover, we know that the expected duration of each work item is time $ { \left( w _ { a } \right) } = 3 0$ min, time $( w _ { b } ) \ = \ 1 0$ min, and $t i m e ( w _ { c } ) =$ 40 min. We also know that the risk associated with each work item does not change over time. Finally, we know that when performed by resource $r _ { 1 }$ the work items have the following expected risk levels: $r i s k _ { r _ { 1 } , w _ { a } , \tau } = 0 . 2 , r i s k _ { r _ { 1 } , w _ { b } , \tau } = 0 . 7$ , and $r i s k _ { r _ { 1 } , w _ { c } , \tau } = 0 . 6$ while <sup>¼</sup>when performed by resource $r _ { 2 }$ <sup>¼ ¼</sup>the work items have the following expected risk levels: $r i s k _ { r _ { 2 } , w _ { a } , \tau } = 0 . 1 , r i s k _ { r _ { 2 } , w _ { b } , \tau } = 0 . 7$ , and $r i s k _ { r _ { 2 } , w _ { c } , \tau } = 0 . 4 .$

<sup>¼ ¼ ¼</sup>The MILP problem for distributing work items will take the following form (assuming α = 0.5):

$$
\begin{array}{l} \text { minimize } \frac {0 . 5}{\tau + 8 0} \cdot \left(w a _ {r _ {1}, w _ {a}} + w a _ {r _ {1}, w _ {b}} + w a _ {r _ {1}, w _ {c}} + w a _ {r _ {2}, w _ {a}} + w a _ {r _ {2}, w _ {b}} + w a _ {r _ {2}, w _ {c}}\right) + 0. 5 \\ \times (0. 2 \cdot x _ {r _ {1}, w _ {a}, \tau} + 0. 7 \cdot x _ {r _ {1}, w _ {b}, \tau} + 0. 6 \cdot x _ {r _ {1}, w _ {c}, \tau} + 0. 1 \cdot x _ {r _ {2}, w _ {a}, \tau} \\ + 0. 7 \cdot x _ {r _ {2}, w _ {b}, \tau} + 0. 4 \cdot x _ {r _ {2}, w _ {c}, \tau}) \end{array}
$$

subject to the following constraints:

either work item $w _ { a }$ or $w _ { b }$ is executed, whereas $w _ { c }$ has to (instantiation of Eq. (2)):

$$
\begin{array}{l} x _ {r _ {1}, w _ {a}, \tau} + x _ {r _ {1}, w _ {b}, \tau} + x _ {r _ {2}, w _ {a}, \tau} + x _ {r _ {2}, w _ {b}, \tau} = 1 \\ x _ {r _ {1}, w _ {c}, \tau} + x _ {r _ {2}, w _ {c}, \tau} = 1 \end{array}
$$

at any time, all resources, i.e. $r _ { 1 }$ and $r _ { 2 } ,$ can only perform one work item (Eq. (3)):

$$
\begin{array}{c} \left(w a _ {r _ {1}, w _ {c}} - w a _ {r _ {1}, w _ {a}} - w a _ {r _ {1}, w _ {b}} \geq 3 0 \cdot x _ {r _ {1}, w _ {a}, \tau} + 1 0 \cdot x _ {r _ {1}, w _ {b}, \tau}\right) \\ \vee \left(w a _ {r _ {1}, w _ {a}} + w a _ {r _ {1}, w _ {b}} - w a _ {r _ {1}, w _ {c}} \geq 4 0 \cdot x _ {r _ {1}, w _ {c}, \tau}\right) \\ \left(w a _ {r _ {2}, w _ {c}} - w a _ {r _ {2}, w _ {a}} - w a _ {r _ {2}, w _ {b}} \leq 3 0 \cdot x _ {r _ {2}, w _ {a}, \tau} + 1 0 \cdot x _ {r _ {2}, w _ {b}, \tau}\right) \\ \vee \left(w a _ {r _ {2}, w _ {a}} + w a _ {r _ {2}, w _ {b}} - w a _ {r _ {2}, w _ {c}} \leq 4 0 \cdot x _ {r _ {2}, w _ {c}, \tau}\right) \end{array}
$$

instantiation of Eq. (1) for resources $r _ { 1 }$ and $r _ { 2 }$ and work items $w _ { a } ,$ w<sub>b</sub> and w<sub>c</sub>:

$$
\begin{array}{l} x _ {r _ {1}, w _ {a}, \tau} = 1 \Longleftrightarrow w a _ {r _ {1}, w _ {a}} \geq \tau \wedge w a _ {r _ {1}, w _ {a}} <   \tau + 8 0 \\ x _ {r _ {1}, w _ {b}, \tau} = 1 \Longleftrightarrow w a _ {r _ {1}, w _ {b}} \geq \tau \wedge w a _ {r _ {1}, w _ {b}} <   \tau + 8 0 \\ x _ {r _ {1}, w _ {c}, \tau} = 1 \Longleftrightarrow w a _ {r _ {1}, w _ {c}} \geq \tau \wedge w a _ {r _ {1}, w _ {c}} <   \tau + 8 0 \\ x _ {r _ {1}, w _ {a}, \tau} = 1 \Longleftrightarrow w a _ {r _ {2}, w _ {a}} \geq \tau \wedge w a _ {r _ {2}, w _ {a}} <   \tau + 8 0 \\ x _ {r _ {1}, w _ {b}, \tau} = 1 \Longleftrightarrow w a _ {r _ {2}, w _ {b}} \geq \tau \wedge w a _ {r _ {2}, w _ {b}} <   \tau + 8 0 \\ x _ {r _ {1}, w _ {c}, \tau} = 1 \Longleftrightarrow w a _ {r _ {2}, w _ {c}} \geq \tau \wedge w a _ {r _ {2}, w _ {c}} <   \tau + 8 0. \end{array}
$$

The optimal solution to this problem is $w a _ { r _ { 1 } , w _ { a } } = 1 , w a _ { r _ { 1 } , w _ { b } } = 0$ , w $a _ { r _ { 1 } , w _ { c } } = 0 , w a _ { r _ { 2 } , w _ { a } } = 0 , w a _ { r _ { 2 } , w _ { b } } = 0 , w a _ { r _ { 2 } , w _ { c } } = 1 , x _ { r _ { 1 } , w _ { a } , \tau } = 1 , x _ { r _ { 1 } , w _ { b } , \tau } = 0 ,$ $x _ { r _ { 1 } , w _ { c } , \tau } = 0 , x _ { r _ { 2 } , w _ { a } , \tau } = 0 , x _ { r _ { 2 } , w _ { b } , \tau } = 0 , x _ { r _ { 2 } , w _ { c } , \tau } = 1$ <sup>¼ ¼</sup>, that is a schedule <sup>¼</sup>where resource $r _ { 1 }$ <sup>¼ ¼</sup>performs work item $w _ { a }$ <sup>¼</sup>and resource $r _ { 2 }$ performs work item $w _ { c }$

## 7.2. Recommendations for work-item execution

After the optimal distribution is computed, we need to provide a recommendation to r for executing any $w \in W \cap c a n _ { N } ( r )$ . For any work item $w ,$ the recommendation rec(w, r) is a value between 0 and 1, where 0 is assigned to the work item with the highest recommendation and 1 to the work item with the least one. Let us consider an optimal solution s of the MILP problem to distribute work items while minimizing risks. The work-item recommendations for each resource r are given as follows:

• If there exists a work item $w \in W \cap c a n _ { N } ( r )$ such that $x _ { r , w , \tau } = 1$ for solution s, the optimal distribution suggests w to be performed by r at the current time. Therefore, $r e c ( w , r ) = 0$ . For any other work item w′, the value $r e c ( w ^ { \prime } , r )$ is strictly greater than 0 and lower than or equal to 1:

$$
\operatorname{rec} \left(w ^ {\prime}, r\right) = \frac {\operatorname{risk} _ {r , w ^ {\prime} , \tau} + \operatorname{risk} _ {r , w , \tau}}{\operatorname{risk} _ {r , w , \tau} + 1}
$$

r $\scriptstyle { \mathrm { ? } } C ( w ^ { \prime } , r )$ grows proportionally to $r i s k _ { r , w ^ { \prime } , \tau }$ , with $r e c ( w ^ { \prime } , r ) = 1 { \mathrm { i f } } r$ is $k _ { r , w ^ { \prime } , \tau } = 1$

<sup>¼</sup>• Otherwise, r is supposed to start no work item at the current time. However, since recommendations need to be provided also to resources that are not supposed to execute any work item, for each $w \in W \cap c a n _ { N } ( r )$ , we set $r e c ( w , r ) = r i s k _ { r , w , \tau } .$

a) The UI to support participants in choosing the next work item to perform based on risks.

b) The UI to support participants in filling out a form based on risks.

![](/api/attachments/UPEAC38D/fulltext/images/55c949a57b5e59ef6f8bce27b52edafff4f68d7f3fcebc0c83a5eea005ee8353.jpg)  
Fig. 4. Screenshots of the map visualizer extension for risk-aware prediction in YAWL. (a) The UI to support participants in choosing the next work item to perform based on risks. (b) The UI to support participants in <sup>fi</sup>lling out a form based on risks. (For interpretation of the references to color in this <sup>fi</sup>gure, the reader is referred to the web version of this article.)

It is possible that the optimal distribution assigns no work item to a resource r at the current time. This is the case when r is already performing a work item (i.e., no additional work item should be suggested) or there are more resources available than work items to assign.

Let us consider the problem illustrated at the end of Section 7.1. In this problem we have two resources $r _ { 1 }$ and $r _ { 2 }$ and three work items $w _ { a } , w _ { b } ,$ and $w _ { c }$ We recall that the expected risk levels associated with a resource performing a given work item were: $r i s k _ { r _ { 1 } , w _ { a } , \tau } = 0 . 2$ , ris $k _ { r _ { 1 } , w _ { b } , \tau } = 0 . 7$ , and $r i s k _ { r _ { 1 } , w _ { c } , \tau } = 0 . 6$ for resource $r _ { 1 } ,$ and $r i s k _ { r _ { 2 } , w _ { a } , \tau } = 0 . 1 , r i$ $s k _ { r _ { 2 } , w _ { b } , \tau } = 0 . 7$ , and $r i s k _ { r _ { 2 } , w _ { c } , \tau } = 0 . 4$ for resource $r _ { 2 } .$ <sup>¼</sup>. We can then derive that the best allocation requires that resource $r _ { 1 }$ performs work item $w _ { a }$ and resource $r _ { 2 }$ performs work item $w _ { c } .$ Finally, when recommendations about which work item should be performed and by whom will they be required, the recommendation system will return the following values: $r e c ( r _ { 1 } , w _ { a } ) = 0 , r e c ( r _ { 1 } , w _ { b } ) = 0 . 7 5 \mathrm { a n d } r e c ( r _ { 1 } , w _ { c } ) = 0 . 6 7$ for resource $r _ { 1 } ,$ , and rec $\cdot ( r _ { 2 } , w _ { a } ) = 0 . 3 6 , r e c ( r _ { 2 } , w _ { b } ) = 0 . 7 9$ and $r e c ( r _ { 2 } , w _ { c } ) = 0$ for resource $r _ { 2 } .$

## 7.3. Recommendations for filling out forms

In addition to providing risk-informed decision support when picking work items for execution, we provide support during the execution of the work items themselves. Human resources usually perform work items by <sup>fi</sup>lling out a form with the required data. The data that are provided may also in<sup>fl</sup>uence a process risk. Therefore, we want to highlight the expected risk whenever a piece of data is inserted by the resource into the form.

The risk associated with <sup>fi</sup>lling a form with particular data is also computed using Algorithm 2. When used to compute the risk associated with <sup>fi</sup>lling a form to perform a work item (ta, id), varAssign(id) is the variable assignment that would result by submitting a form using the data the resource has inserted so far.

## 8. Implementation

We operationalized our recommendation system on top of the YAWL BPM system, by extending an existing YAWL plug-in and by implementing two new custom YAWL services. This way we realized a risk-aware BPM system supporting multi-instance work distribution and form <sup>fi</sup>lling-out.

The intent of our recommendation system is to “drive” participants during the execution of process instances. This goal can be achieved if participants can easily understand the suggestions proposed by our tool. For this we decided to extend a previous plug-in for the YAWL Worklist Handler, named Map Visualizer [31]. This plug-in provides a graphical user interface to suggest process participants the work items to execute, along with assisting them during the execution of such work items. The tool is based on two orthogonal concepts: maps and metrics. A map can be a geographical map, a process model, an organizational diagram, etc. For each map, work items can be visualized by dots which are located in a meaningful position (e.g., for a geographic map, work items are projected onto the locations where they need to be executed, or for a process-model map onto the boxes of the corresponding tasks in the model). Dots can also be colored according to certain metrics, which determine the suggested level of priority of a work item. This approach offers advantages over traditional BPM systems, which are only equipped with basic client applications where work items available for execution are simply enlisted, and sorted according to given criteria. When users are confronted with hundreds of items, this visualization does not scale well. The validity of the metaphors of maps and metrics used for decision support in process execution was con<sup>fi</sup>rmed through a set of experiments reported in [31]. De Leoni et al. [31] only de<sup>fi</sup>ne very basic metrics. We have extended the repertoire of these metrics with a new metric that is computed by employing the technique described in Section 7.

![](/api/attachments/UPEAC38D/fulltext/images/e15a6bf626b8eadfb017784e73cbdea138148d91f385f4a4bde7672213e65fe7.jpg)  
Fig. 5. The integration of the implemented tools with the YAWL system.

Fig. 4a shows a screenshot of the Map Visualizer where a risk-based metric is employed. The map shows the process model using the YAWL notation and dots are projected onto the corresponding elements of the model. Each dot corresponds to a different work item and is colored according to the risks for the three faults de<sup>fi</sup>ned before. When multiple dots are positioned on the same coordinates, they are merged into a single larger dot whose diameter grows with the number of dots being amalgamated. Colors go from white to black, passing through intermediate shades of yellow, orange, red, purple and brown. The white and black colors identify work items associated with a risk of 0 and 1, respectively. The screenshot in Fig. 4a refers to a con<sup>fi</sup>guration where multiple process instances are being carried out at the same time and, hence, the work items refer to different process instances. The con<sup>fi</sup>guration of dots highlights that the risk is lower if the process participant performs a work item of task Estimate Trailer Usage, Arrange Pickup Appointment or Arrange Delivery Appointment for a certain instance. When clicking on the dot, the participant is shown the process instance of the relative work item(s).

As discussed in Section 7.3, the activity of compiling a form is also supported. Fig. 4b shows a screenshot where, while <sup>fi</sup>lling in a form, participants are shown the risk associated with that speci<sup>fi</sup>c input for that form via a vertical bar (showing a value of 45% in the example, which means a risk of 0.45). While a participant changes the data in the form, the risk value is recomputed accordingly.

Besides the extension to the Map Visualizer, we implemented two new custom services for YAWL, namely the Prediction Service and Multi-Instance Prediction Service. The Prediction Service provides risk prediction and recommendation. It implements the technique described in Section 6 and constructs decision trees through J48, which is the implementation of the C4.5 algorithm in the Weka toolkit for data mining.<sup>4</sup> Since the algorithm is not capable of predicting continuous values, in order to provide a risk prediction we grouped risk levels that are close to each other in intervals of 0.05 (e.g. all risk likelihoods from 0 to 0.04 are considered as 0, from 0.05 to 0.09 as 0.1 and so on).

The Prediction Service communicates with the Log Abstraction Layer described in [3], to be able to retrieve event logs from textual <sup>fi</sup>les, such as from OpenXES event logs, or directly from the YAWL database, which stores both historical information and the current system's state.

The Multi-Instance Prediction Service, similar to the Prediction Service, provides risk prediction and recommendation. The difference between these two services is that in the former a recommendation takes into account all process instances currently running in the system. The Multi-Instance Prediction Service interacts with the Prediction Service to obtain “local” predictions that, in combination with other information derived from the log (e.g. expected task duration, other running instances), are used to <sup>fi</sup>nd the optimal resource allocation using the technique described in Section 7. To this purpose, the Multi-Instance Prediction Service also interacts with the MILP Solver. The MILP Solver provides an interface for the interaction with different integer linear programming solvers. So far we support Gurobi,<sup>5</sup> SCIP<sup>6</sup> and LPSolve.<sup>7</sup> Finally, the Multi-Instance Prediction Service is invoked by the Map Visualizer to obtain the risk predictions and recommendations and show these to process participants in the form of maps. The map vi sualizer works with the standard Worklist Handler provided by YAWL to obtain the up-to-date distribution of work to resources. Fig. 5 shows the diagram of these connections.

## 9. Evaluation

We evaluated our recommendation system using the claim handling process and related event data, of a large insurance company kept under condition of anonymity. The event data recording about one year of completed instances (total: 1065 traces) was used as a benchmark for our evaluation. The claim handling process, modeled in Fig. 6, starts when a new claim is received from a customer. Upon receipt of a claim, a <sup>fi</sup>le review is conducted in order to assess the claim, then the customer is contacted and informed about the result of the assessment. The customer may provide additional documents (“Receive Incoming Correspondence”), which need to be processed (“Process Additional Information”) and the claim may need to be reassessed. After the customer has been contacted, a payment order is generated and authorized in order to process the payment. During the execution of the process model, several updates about the status of the claim may need to be provided to the customer as follow-ups. The claim is closed once the payment has been authorized.

As one can see from the model, this process contains several loops, each of which is executed multiple times, in general.

Four risk analysts working in this insurance company were consulted through an iterative interview process, to identify the risks this process is exposed ${ \mathrm { t o . } } ^ { 8 }$ They reported about three equallyimportant faults related to complete traces σ of the claim handling process:

Over-time fault. This fault is the same as the over-time fault described in Section 5. For this risk we set the Maximum Cycle Time $d _ { m c t } = 3 0$ (i.e. 30 days) and the maximum duration $d _ { m a x } = 3 0 0$ (i.e. 300 days). The severity of an overtime fault is measured as follows:

![](/api/attachments/UPEAC38D/fulltext/images/82f0505cdb8a1a01899ef3a4a40c5d564b21050367c1c788c3aec5b338627275.jpg)  
Fig. 6. The claims handling process used for the evaluation.

$$
f _ {t i m e} (\sigma) = \max \left(\frac {d _ {\sigma} - d _ {m c t}}{\max (d _ {m a x} - d _ {m c t} , 1)}, 0\right).
$$

Customer-dissatisfaction fault. During the execution of the process, if a customer is not updated regularly on their claim, they may feel “unheeded”. A customer dissatis<sup>fi</sup>ed may generate negative consequences such as negative publicity for the insurance company, leading to bad reputation. In order to avoid this kind of situation, the company's policy is to contact their customers at least once every 15 days. Given the set $\Lambda = \{ ( t , ~ r , ~ d , ~ \phi ) \in \sigma | t ~ =$ Request Follow Up $\lor \ t \ =$ Receive New Claim ∨ t = Close Claim} of events belonging to task Request Follow Up, to task Receive New Claim, or to task Close Claim, ordered by timestamp, the severity of this fault is:

$$
f _ {\text { dissatisfaction }} (\sigma) = \sum_ {1 \leq i \leq \| A \|} \max (0, d _ {i + 1} - d _ {i} - 1 5 d a y s)
$$

where $d _ { i }$ is the time stamp of $i ^ { t h }$ event $\in \Lambda .$

Cost overrun fault. Each task has an execution cost associated with it, e.g. the cost of utilizing a resource to perform a task. Since the pro<sup>fi</sup>t of the company decreases with a higher number of tasks executed, the company clearly aims to minimize the number of tasks required to process a claim, for example by reducing the number of followups with the claimant or the need for processing additional documents, and reassessing the claim, once the process has started. The severity of the cost overrun fault increases as the cost goes beyond the minimum. Let $c _ { \sigma }$ be the number of work items executed in $\sigma ,$ $c _ { m a x }$ be the maximum number of work items (e.g. 30) that should be executed in any process instance that has already been completed (including $\sigma ) ,$ and $c _ { m i n }$ be the number of work items with unique label executed in σ. The severity of a cost overrun fault is:

$$
f _ {c o s t} (\sigma) = \min \left(\frac {c _ {\sigma} - c _ {m i n}}{\max (c _ {m a x} - c _ {m i n} , 1)}, 1\right).
$$

The occurrence of these three faults in the logs is checked using the technique that we proposed in [5], which was originally designed for run-time detection of process-related risks.

Trialing our recommendation system within the company was not possible, as the claim handling process concerns thousands of dollars, which cannot be put in danger with experiments. So we had to simulate the execution of this process and the resource behavior using CPN Tools.<sup>9</sup>

We mined the control-<sup>fl</sup>ow of our simulation model from the original log and re<sup>fi</sup>ned it with the help of business analysts of the company, and added the data, resource utilization (i.e. who does what), and task duration, which we also obtained from the log. We then add the frequency of occurrence of each of these elements, on the basis on that observed from the log. This log was also used to train the function estimators.

The CPN Tools model we created is a hierarchical model composed of ten nets that all together count 65 transitions and 62 places. The main net is based on the model showed in Fig. $6 ,$ with additional places and transitions in order to guarantee the interaction with our recommendation system. The remaining nine nets de<sup>fi</sup>ne the behavior of each one of the nine tasks showed in Fig. 6.

We used this model to simulate a constant workload of 50 active instances, in order to maintain a similar ratio to the original log (in the original log we had 271 active instances on average). In order to maintain the ratio between active instances and resources, we reduced the number of resources utilized to one-sixth of the original number observed in the log. Finally, we analyzed the fault distribution of the generated log using the technique presented in [5].

The model created with CPN Tools was able to reproduce the behavior of the original log. The Kolmogorov–Smirnov Z two-samples test (Kolmogorov − Smirnov $Z = 0 . 7 6 3 , p = 0 . 6 0 5 > 0 . 0 5 )$ ) shows no signi<sup>fi</sup>cant difference between the distribution of the composite fault in the original log and that in the simulated log. This result is con<sup>fi</sup>rmed by the Mann–Whitney test $( U = 1 0 9 , 1 6 3 . 0 , z = - 0 . 8 7 5 , p = 0 . 3 8 1 > 0 . 0 5 )$

We performed three sets of experiments. In the <sup>fi</sup>rst set, all the suggestions provided by the recommendation system were followed. In the second set, only 66% of the times the suggestions were followed, and executing the process as the company would have done for the remaining 33% of the times. Finally, in the third set of experiments, only 33% of the times the suggestions provided by our recommendation system were followed. Moreover, for each set of experiments we tested several values of α (i.e. 0.0, 0.25, 0.5, 0.75 and 1.0), where α equal to 0 will shift focus on reducing risks, while α equal to 1 on reducing the overall execution time (see Section 7).

All experiments were executed simulating the execution of the process by means of the CPN Tools model. For each experiment we generated a new log containing 213 fresh log traces (a <sup>fi</sup>fth of the traces contained in the original log). We used a computer with an Intel Core i7 CPU (2.2 GHz), 4 GB of RAM, running Lubuntu v13.10 (64 bit). We used Gurobi 5.6 as MILP Solver as this is the most ef<sup>fi</sup>cient solver among the three that we support $[ 4 4 ] ^ { 1 0 }$ and imposed a time limit of $6 0 s ,$ within which a solution needs to be provided for each problem. For mission-critical processes, the time limit can also be reduced. If a time limit is set and Gurobi cannot <sup>fi</sup>nd a solution within the limit, a sub-optimal solution is returned, i.e. the best solution found so far. The experiments have shown that, practically, the returned solution is always so close to the optimal that it does not in-<sup>fl</sup>uence the <sup>fi</sup>nal fault's magnitude.

a) Results following 100% of the suggestions provided.  
![](/api/attachments/UPEAC38D/fulltext/images/332b98928dd6d2d7e9db5711272e281c52b2324848bf87a7a76e5ea97320513e.jpg)

b) Results following 66% of the suggestions provided.  
![](/api/attachments/UPEAC38D/fulltext/images/27952ce518533988a88b3b0e5824757cd9ec07ea19f6a1a2c54941fb78d36a3a.jpg)

c) Results following 33% of the suggestions provided.  
![](/api/attachments/UPEAC38D/fulltext/images/2d40282413b97592803019b822a3af794b4f11fc97d830badc0148b1a8bf041f.jpg)  
Fig. 7. Comparison of the fault severity when recommendations are and are not followed, with 0 denoting absence of faults. The x-axis represents the severity of the composite fault and the y-axis represents the percentage of instances that completed with a certain severity. (a) Results following 100% of the suggestions provided. (b) Results following 66% of the suggestions provided. (c) Results following 33% of the suggestions provided.

Fig. 7 shows the results of each of the three sets of experiments, comparing the fault severity of the original log with that obtained when recommendations are followed. It is worth highlighting how the results are

## Table 2

Percentage of faulty instances, mean and median fault severity occurring in the reference logs, i.e. original log and simulation model log. Percentage of faulty instances, mean and median fault severity occurring in the test logs aggregated into a unique log, i.e. simulated aggregated, and for each value of α, reported for each of the three sets of experiments (33%, 66% and 100% suggestions used).

<table><tr><td>Reference logs</td><td># Traces</td><td>% Faulty instances</td><td>Average</td><td>Median</td></tr><tr><td>Original</td><td>1065</td><td>89.4%</td><td>0.22</td><td>0.10</td></tr><tr><td>Simulation model</td><td>1065</td><td>92.5%</td><td>0.22</td><td>0.15</td></tr></table>

<table><tr><td rowspan="2">Test logs</td><td rowspan="2"># Traces</td><td colspan="3">Suggestions 100%</td><td colspan="3">Suggestions 66%</td><td colspan="3">Suggestions 33%</td></tr><tr><td>% Faulty instances</td><td>Avg</td><td>Mdn</td><td>% Faulty instances</td><td>Avg</td><td>Mdn</td><td>% Faulty instances</td><td>Avg</td><td>Mdn</td></tr><tr><td>Simulated aggregated</td><td>1065</td><td>26.8%</td><td>0.02</td><td>0.00</td><td>43.9%</td><td>0.03</td><td>0.00</td><td>76.3%</td><td>0.07</td><td>0.05</td></tr><tr><td>- Simulated α = 0.0</td><td>213</td><td>31.9%</td><td>0.02</td><td>0.00</td><td>53.1%</td><td>0.03</td><td>0.05</td><td>80.3%</td><td>0.08</td><td>0.05</td></tr><tr><td>- Simulated α = 0.25</td><td>213</td><td>24.9%</td><td>0.02</td><td>0.00</td><td>42.7%</td><td>0.02</td><td>0.05</td><td>76.5%</td><td>0.07</td><td>0.05</td></tr><tr><td>- Simulated α = 0.5</td><td>213</td><td>14.1%</td><td>0.01</td><td>0.00</td><td>37.1%</td><td>0.02</td><td>0.05</td><td>71.4%</td><td>0.07</td><td>0.05</td></tr><tr><td>- Simulated α = 0.75</td><td>213</td><td>22.1%</td><td>0.01</td><td>0.00</td><td>38.0%</td><td>0.02</td><td>0.05</td><td>77.5%</td><td>0.07</td><td>0.05</td></tr><tr><td>- Simulated α = 1.0</td><td>213</td><td>40.8%</td><td>0.03</td><td>0.00</td><td>48.8%</td><td>0.03</td><td>0.05</td><td>75.6%</td><td>0.08</td><td>0.05</td></tr></table>

![](/api/attachments/UPEAC38D/fulltext/images/4213e039ff81ad0647ba48f7a925a7efafa1034320979d13cfb5527fcacdd4cd.jpg)  
Fig. 8. BoxPlot showing the fault severity occurring in instances of each of the three experiments and of the original log.

given in terms of severity measured for completed instances. Risks are relative to running instances and estimate the expected fault severity and likelihood when such instances complete.

Table 2 shows the results of the experiments. In this table we show percentage of faulty instances, mean and median fault severity obtained during our tests. The values are shown for the original log and the log obtained by our simulation model without using our recommendation system (Simulation model). Same values are also reported for each log obtained using our recommendation system, both in an aggregated log (Simulated aggregated) and for each value of α, over the three sets of experiments (33%, 66% and 100% suggestions used). In the best case (Simulated log with $\alpha = 0 . 5 )$ , our recommendation system was able to reduce the percentage of instances terminating with a fault from 89.4% to 14.1% and the average fault severity from 0.216 to 0.01. In particular, the use of our recommendation system signi<sup>fi</sup>cantly reduced the number of instances terminating with faults, as evidenced by the result of the Pearson's $\chi ^ { 2 }$ test $( \chi ^ { 2 } ( 1 ) = 8 5 7 . 8 4 8 , p < 0 . 0 0 1$ 1 for the <sup>fi</sup>rst set of experiments, $\chi ^ { 2 } ( 1 ) = 4 9 4 . 9 0 7 , p < 0 . 0 0 1$ for the second set, and $\chi ^ { 2 } ( 1 ) = 6 4 . 6 6 3 , p < 0 . 0 0 1$ for the third one, computed over the original log and the simulated aggregated log). Based on the odds ratio, the odds of an instance completing without a fault are respectively 23.06, 10.75, and 2.62 times higher if our suggestions are followed. Moreover, we tested if the number of suggestions followed in<sup>fl</sup>uences the effectiveness of our recommendation system. The Kruskal–Wallis test $( H ( 3 ) = 1 , 6 0 3 . 6 1 , p < 0 . 0 0 1 )$ shows that the overall fault severity among the three sets of experiments (using the Simulated overall dataset, i.e. independent of the value of the parameter α) and the original log is signi<sup>fi</sup>cantly different, and as revealed by Jonkheere's test $( J = 1 , 6 5 8 , 6 3 0 . 5 , z = - 4 1 . 0 3 4 , r = - 0 . 6 3 , p < 0 . 0 0 1 )$ , the median fault severity decreases as more suggestions are followed (see Fig. 8). These two tests indicate that our recommendation system is capable of preventing the occurrence of faults and of reducing their severity. Clearly, it is preferable to follow as many suggestions as possible in order to obtain the best results though this may not always be possible.

We tested how the value of the parameter α in<sup>fl</sup>uences the effectiveness of our recommendation system. We compared the performances obtained with each value of α for each set of experiment. The Kruskal– Wallis test $( H ( 4 ) = 4 6 . 1 7 6 , p < 0 . 0 0 1$ for the <sup>fi</sup>rst set of experiments, $H ( 4 ) = 1 7 . 1 9 1 , p = 0 . 0 0 2 < 0 . 0 5$ for the second one, $H ( 4 ) = 5 . 5 5 8$ $p = 0 . 2 3 5 > 0 . 0 5$ for the third one) shows how the value of parameter α signi<sup>fi</sup>cantly in<sup>fl</sup>uences the median fault severity if the suggestions proposed are followed in at least 66% of the instances. Jonkheere's test $( J = 2 5 1 , 3 0 5 , z = 5 . 5 7 7 , r = 0 . 1 7 , p < 0 . 0 0 1$ for the <sup>fi</sup>rst set of experiments, $J = 2 4 6 , 3 2 2 . 5 , z = 3 . 9 1 8 , r = 0 . 1 2 , p < 0 . 0 0 1$ for the second one) revealed that the median fault severity increases when the value of α diverges from 0.5 moving either toward 0 or 1.

In the case study taken in exam, the duration of an instance has an in<sup>fl</sup>uence over the over-time fault and the cost overrun fault. A short execution time will directly minimize the duration of an instance (thus preventing the over-time fault) but also reduce the number of activities that are executed inside such an instance (thus preventing the cost overrun fault). In light of so, it is not strange that the best results are obtained with $\alpha = 0 . 5$ which strikes a good balance between minimizing risks and overall execution time.

Finally, we performed a sensitivity test over the time limit granted to the MILP Solver. We tested our recommendation system with <sup>fi</sup>ve different time limits, while keeping the value of α equal to 0.5 and following all suggestions (best con<sup>fi</sup>guration for risk prevention). The time limits used were: 5, 10, 20, 40 and 60 s. Fig. 9 shows the distribution of fault severities obtained using these different time limits. We can observe that changing the time limit yields statistically different distributions, as revealed by the Kruskal–Wallis test $( H ( 4 ) =$ $7 4 . 7 3 8 , p < 0 . 0 0 1 \rangle$ ). Moreover, the Jonkheere's test $( J = 1 8 6 , 2 3 8 , z =$ $- 8 . 6 3 1 , r = - 0 . 2 6 4 , p < 0 . 0 0 1 )$ reveals that the median fault severity decreases when more time is granted to the MILP Solver. From a practical point of view though, it is interesting to observe that even with a time limit of 5 s the approach can still notably reduce the fault severity, with 90% of the instances terminating with a fault severity of up to 0.05 out of 1. This suggests that users may set the time limit to be granted to the MILP Solver on the basis of the number of process activities that are critical, i.e. using a low time limit if the number of critical activities is low and a high time limit if that number is high.

Based on the results of our experiments we can conclude that the approach produces a signi<sup>fi</sup>cant reduction in the number of faults and their severity. Speci<sup>fi</sup>cally, for the case study in question we achieved the best results with α equal to 0.5, with a time limit of 60 s. We observe that this parameter can be customized based on the priorities of the company where our approach would be deployed, e.g. an organization may use lower values of α if risk reduction is prioritized over reduction of process duration.

![](/api/attachments/UPEAC38D/fulltext/images/cdc99639095b7aa6a48b921ce86bd3e8778500fe876cec3cc0617df7a8af9281.jpg)  
Fig. 9. Fault severity distribution using different time limits.

## 10. Conclusion

This paper proposes a recommendation system that allows users to take risk-informed decisions when partaking in multiple process instances running concurrently. Using historical information extracted from process execution logs, for each state of a process instance where input is required from a process participant, the recommendation system determines the risk that a fault (or set of faults) will occur if the participant's input is going to be used to carry on the process instance. This input can be in the form of data used to <sup>fi</sup>ll out a user form, or in terms of the next work item chosen to be executed

The recommendation system relies on two techniques: one for predicting risks, the other for identifying the best assignment of participants to the work items currently on offer. The objective is to minimize both the overall risk of each process instance (i.e. the combined risk for all faults) and the execution time of all running process instances.

We designed the recommendation system in a language-independent manner, using common notions of executable process models such as tasks and work items borrowed from the YAWL language. We then implemented the recommendation system as a set of components for the YAWL system. For each user decision, the recommendation system provides recommendations to participants in the form of visual aids on top of YAWL models. We also extended the YAWL user form visualizer, to show a risk pro<sup>fi</sup>le based on the data inserted by the participant for a given form. Although we implemented our ideas in the context of the YAWL system, our recommendation system can easily be integrated with other BPM systems by implementing an interface that allows the communication through the “log abstraction layer” (in [5] we showed how it can be integrated with the Oracle BPEL 10 g database), and by extending the Map-Based Worklist Handler in order to list work items belonging to a different BPM system than the YAWL system.

We simulated a real-life process model based on one year of execution logs extracted from a large insurance company, and in collaboration with risk analysts from the company we identi<sup>fi</sup>ed the risks affecting this process. We used these logs to train our recommendation system. Then we performed various statistical tests while simulating new process instances following the recommendations provided by our recommendation system, and measured the number and severity of the faults upon instance completion. Since in reality it might not always be feasible to follow the recommendations provided, we varied the percentage of recommendations to be followed by the simulated instances. Even when following one recommendation out of three, the recommendation system was able to signi<sup>fi</sup>cantly reduce the number and severity of faults. Further, results show that risks can be predicted online, i.e. while business processes are being executed, without impacting on execution performance.

The proposed recommendation system can only address processrelated risks in so far as these depend on information available during process execution, i.e. task input and output data, allocated resources and time performance. This implies that risks depending on information outside the boundaries of a process, i.e. its context (e.g. market <sup>fl</sup>uctuations or weather forecast) cannot be detected.

While our approach is independent of any speci<sup>fi</sup>c machine-learning method, in this paper we leveraged on decision-tree classi<sup>fi</sup>cation. Decision trees have, among others, the advantage of automatically discretizing continuous features. We used this information to drastically simplify the MILP problem in order to <sup>fi</sup>nd an optimal work-item allocation to resources. However, decision trees cannot deal with class attributes that are de<sup>fi</sup>ned over a continuous domain, such as the fault severity. To overcome this issue, we had to discretize the range of fault severity values (between 0 and 1) into intervals of 0.05. This limitation could be lifted by using methods that combine classi<sup>fi</sup>cation and regression trees, such as CART methods. This is certainly a direction for future work.

Another limitation is that we cannot guarantee to <sup>fi</sup>nd the optimal solution, because of the time bound that we impose on the MILP Solver for ef<sup>fi</sup>ciency reasons. However, our experiments show that this time limit can be as short as 5 s (i.e. near real-time), to obtain a signi<sup>fi</sup>cant reduction in the number of faults.

The recommendation system we propose relies on a couple of assumptions. While we deal with multiple process instances sharing the same pool of participants, we assume no sharing of data between instances. Further, we only assume that one participant can perform a single task at a time. These assumptions offer opportunities for future work. For example, for the sharing of data between instances we need to reformulate the MILP problem in order to consider that the risk estimation of a work item may change as a consequence of the modi<sup>fi</sup>- cation of data by work items that have been scheduled to be performed <sup>fi</sup>rst. For allowing participants to perform multiple tasks at a time we need to assign a capacity to each resource as the maximum number of work items that resource can perform in parallel. Our MILP problem needs to be reformulated in order to take this capacity into account.

## Acknowledgments

This research is partly funded by the ARC Discovery Project “Riskaware Business Process Management” (DP110100091). NICTA is funded by the Australian Government as represented by the Department of Broadband, Communications and the Digital Economy and the Australian Research Council through the ICT Centre of Excellence program.

## Appendix A

This appendix provides the formal de<sup>fi</sup>nition of YAWL, the algorithms discussed in Section 6, and the mathematical proofs of Lemmas 1 and 2 discussed in Section 7.1.

## A.1. YAWL definition

De<sup>fi</sup>nition 3. A YAWL net $N { \in } N$ is a tuple ${ \cal N } = ( T _ { N } , C _ { N } , i , o ,$ F<sub>N</sub>, $R _ { N } , V _ { N } , U _ { N } , c a n _ { N } )$ where:

• $T _ { N }$ is the set of tasks of N;

• $C _ { N }$ is the set of conditions of $N ;$

$i \in C _ { N }$ is the input condition;

$o \in C _ { N }$ is the output condition;

• $\mathsf { A }$ <sup>fl</sup>ow relation $F _ { N } \subseteq ( C _ { N } \setminus \{ o \} \times T _ { N } ) \cup ( T _ { N } \times C _ { N } \setminus \{ i \} ) ;$

• $R _ { N }$ is the set of resources authorized to perform any tasks in $T _ { N } ;$

• $V _ { N }$ is the set of variables that are de<sup>fi</sup>ned in the net;

• $U _ { N }$ is the set of values that can be assigned to variables;

• can<sub>N</sub> : $R _ { N }  2 ^ { T _ { N } }$ is a function that associates resources with the tasks that are authorized to perform.

Compared to [41] we use a simpli<sup>fi</sup>ed de<sup>fi</sup>nition of YAWL nets, which describes those parts that are relevant for the article. YAWL supports sophisticated authorization mechanisms as described in the resource patterns [45]. The above de<sup>fi</sup>nition describes a simpli<sup>fi</sup>ed version where authorizations are speci<sup>fi</sup>ed at task level and applies to all work items of a certain task. As such, this de<sup>fi</sup>nition is generalizable to other executable process modeling languages.

We use the following auxiliary functions from [41]. The preset of a task t is the set of its input conditions: $\mathbf { \dot { \eta } } t = \{ c \in C _ { N } | ( c , t ) \in F _ { N } \}$ . Similarly, the postset of a task t is the set of its output conditions: $t ^ { \bullet } =$ $\{ c \in C _ { N } | ( t , c ) \in F _ { N } \}$ . The preset and postset of a condition can be de<sup>fi</sup>ned analogously.

## Algorithm 1. GENERATEFUNCTIONESTIMATORSFORRISKRREDICTION

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Data:  $\mathbf{N} = (T_N, C_N, R_N, V_N, U_N, \text{can}_N) - \text{A YAWL net}, \mathcal{L} - \text{An event log}, \mathfrak{f} \in \mathcal{F} - \text{A fault function}$ 

Result: A Function  $\Psi$  that associates each condition  $c \in C_N$  with a function estimator  $\psi_c$ 

1 Let I be a function whose domain is the set of conditions  $c \in C_N$ , and initially for all  $c \in C_N$ ,  $I(c) = \emptyset$ .

2 foreach trace  $\sigma = \langle(t_1, r_1, d_1, \phi_1), \ldots, (t_n, r_1, d_n, \phi_n) \rangle \in \mathcal{L}$  do

3 Set function A such that dom(A) =  $\emptyset$ 

4 for  $i \leftarrow 1$  to n do

5  $(c_r, c_t) \leftarrow \text{getContextInformation}(\langle(t_1, r_1, d_1, \phi_1), \ldots, (t_i, r_i, d_i, \phi_i) \rangle)$ 

6 Time elapsed  $\overline{d} \leftarrow (d_i - d_1)$ 

7  $J \leftarrow (A \odot (t_i, r_i, \overline{d}) \odot c_r \odot c_t), f(\sigma))$ 

8 foreach  $c \in ^{\bullet} t_i$  do  $I(c) \leftarrow I(c) \cup \{J\}$ ;

9 foreach variable  $v \in dom(\phi_i)$  do  $A(v) \leftarrow \phi_i(v)$ ;

10 end

11 end

12 Set function  $\Psi$  such that dom( $\Psi$ ) =  $\emptyset$ 

13 foreach condition  $c \in C_N$  do  $\Psi(c) \leftarrow buildFunctionEstimator(I(c))$ ;

14 return  $\Psi$
</div>

Algorithm 1 details how function estimators $\boldsymbol { \psi } _ { f _ { c } }$ can be constructed. In the algorithm, we use ⊙ to concatenate tuples: given two tuples ${ \vec { x } } =$ $( x _ { 1 } , . . . , x _ { n } )$ and $\begin{array} { r } { \overrightarrow { y } = ( y _ { 1 } , . . . , y _ { m } ) , \overrightarrow { x } \odot \overrightarrow { y } = ( x _ { 1 } , . . . , x _ { n } , \overleftarrow { y } _ { 1 } , . . . , y _ { m } ) . } \end{array}$ <sup>¼</sup>. Operator ⊙ can also be overloaded to deal with functions de<sup>fi</sup>ned on a <sup>fi</sup>nite and orð Þ ¼ $f \colon W \to Z$ <sup>¼ ð Þ</sup>be a function de<sup>fi</sup>ned on an ordered domain $W = \{ w _ { 1 } , . . . , w _ { o } \}$ . If we denote $z _ { i } = f ( w _ { i } )$ with $1 \leq i \leq 0 ,$ , f ⊙ x $\mathbf { \xi } = ( z _ { 1 } , . . . , z _ { o } , x _ { 1 } , . . . , x _ { n } )$

Algorithm 1 is periodically executed, e.g., every week or after every k process instances are completed. In this way, the predictions are updated according to the recent process executions. The input parameters of the algorithm are a YAWL net N, an event log with traces referring to past executions of instances of the process modeled by N, and a fault function. The output is a function Ψ that associates each condition c with function estimator $\boldsymbol { \psi } _ { f _ { c } }$ . Initially, in line 1, we initialize function I which is going to associate each condition c with the set of observation instances associated with the executions of tasks in the postset of p. From line 2 to line 12, we iteratively replay all traces σ to build the observation instances. While replaying, a function A keeps the current value's assignment to variables (line 3). For each trace's event $\left( t _ { i } , r _ { i } , d _ { i } , \phi _ { i } \right)$ , <sup>fi</sup>rst we build the tuple C of the contextual information (line 5) and compute the elapsed time d(line 6). Then, we build an observation instance J where tuple $\Big ( A \odot \Big ( t _ { i } , r _ { i } , \overline { d } \Big ) \odot c _ { r } \odot c _ { t } \Big )$ is the observed input and the fault severity f(σ) is the observed output. This observation instance is put into the set of observation instances relative to each condition $c \in \cdot _ { t _ { i } }$ . In lines 11–13, we update the current value's assignment during the replay, i.e. we rewrite function A. Finally, in lines 16–19, we build each function estimator $\boldsymbol { \psi } _ { f _ { c } }$ for condition f by the relative observation instances and rewrite $\Psi \ : \mathrm { s . t . } \ : \Psi ( c ) = \psi _ { c }$ .

## Algorithm 2. CALCRISK

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Data:  $N = (T_{N}, C_{N}, R_{N}, V_{N}, U_{N}, can_{N}) - A$  YAWL net,  $f \in F - A$  fault function, r - resource, t - time,  $(ta, id) - work$  item
Result: A risk value
1 risk ← 0
2  $\phi \leftarrow varAssign(id)$ 
3  $d \leftarrow timeElapsed(id)$ 
4  $(c_{r}, c_{t}) \leftarrow具体情况Information(history(id))$ 
5 foreach condition  $c \in \bullet t$  do
6    $\psi \leftarrow \Psi(c)$ 
7    Pick (severity, l) such that  $(\phi, t_{a}, r, d, c_{r}, c_{t}, l) \in \psi(severity)$ 
8    risk ← max(severity · l, risk)
9 end
</div>

Algorithm 2 details how to calculate the risk associated with the execution of a work item. When a prediction for the execution of work item w by resource r is required, the algorithm retrieves the values of all variables during the execution, the elapsed time (i.e. the time passed from the start of the process), and contextual information about the process instance to which the work item belongs to.

The algorithm then retrieves the function estimator associated with each decision point in the preset of w. From each of these function estimators, a prediction of the risk resulting from r executing w is obtained. The variable assignments, the elapsed time, the contextual information, w, and r are used as input for the function estimator. Finally, the prediction having the highest product between predicted fault severity and likelihood of the prediction is returned.

Lemma 1. Constraints of the form as in Eq. (1) can be rewritten into sets of equivalent constraints of the form as in Eq. (A.1).

$$
\begin{array}{l} - w a _ {r, w} - M \cdot (1 - x _ {r, w, t}) \leq - t \\ w a _ {r, w} - M \cdot (1 - x _ {r, w, t}) <   \Delta_ {r, w} (t) \\ w a _ {r, w} - M \cdot x _ {r, w, t} - M \cdot o _ {r, w, t} ^ {\prime} <   t \\ - w a _ {r, w} - M \cdot x _ {r, w, t} - M \cdot (1 - o _ {r, w, t} ^ {\prime}) \leq - \Delta_ {r, w} (t) \end{array}\tag{A.1}
$$

where M is a suf<sup>fi</sup>ciently large number (e.g., the largest machinerepresentable number) and $o _ { r , w , t }$ is a boolean variable that needs to be introduced in the MILP problem.

Proof of Lemma 1. Let us consider $x _ { r , w , t }$ and its possible values 1 and 0. If $x _ { r , w , t } = 1$ then the last two constraints will be satis<sup>fi</sup>ed by − $M \cdot x _ { r , w , t } \ll t - w a _ { r , w }$ and $- \ M \cdot \ x _ { r , w , t } \ll - \ \Delta _ { r , w } ( t ) \ - \ w a _ { r , w } .$ . In order to satisfy the <sup>fi</sup>rst two constraints, since M $\mathbf { \nabla } \cdot \left( 1 - x _ { r , w , t } \right) = 0 ,$ $w a _ { r , w }$ must be $w a _ { r , w } \geq t \land w a _ { r , w } < \Delta _ { r , w } ( t )$ , that is exactly the second part of the constraint de<sup>fi</sup>ned in Eq. (1).

$\operatorname { I f } x _ { r , w , t } = 0$ then $M \cdot ( 1 - x _ { r , w , t } ) = M .$ . This satis<sup>fi</sup>es the <sup>fi</sup>rst two constraints sinc ${ \mathsf { \Omega } } _ { \ast } ^ { \ast } - M \cdot ( 1 - x _ { r , w , t } ) \ll - t + w a _ { r , w } \operatorname { a n d } - M \cdot ( 1 -$ $x _ { r , w , t } ) \ll \Delta _ { r , w } ( t ) - w a _ { r , w } ,$ . The third constraint can be satis<sup>fi</sup>ed only if w $_ { \cdot r , w } < t$ t or if $o _ { r , w , t } / = 1$ , similar thing can be said for the fourth constraint that will be satis<sup>fi</sup>ed only if $w a _ { r , w } \geq \Delta _ { r , w } ( t )$ or if $\dot { } o _ { r , w , t } { } ^ { \prime } = 0$ . We can derive that in order to satisfy the last two constraints we either have $w a _ { r , w } <$ t and $o _ { r , w , t ^ { ' } } = 0$ , or we have $w a _ { r , w } \geq \Delta _ { r , w } ( t )$ and $o _ { r , w , t } / = 1$ . As we can see for $x _ { r , w , t } = 0$ the only way to satisfy the constraints of $\operatorname { E q . } \left( \mathrm { A . 1 } \right)$ is to violate the second part of the constraint de<sup>fi</sup>ned in Eq. (1). □

Lemma 2. Constraints of the form as in $E q . ( 3 )$ can be rewritten into sets of equivalent constraints of the form as in Eq. (A.2).

Similarly, the constraints in Eq. (3) can be transformed into a set of linear constraints as follows:

$$
\begin{array}{l} \sum_ {w _ {b} \in D _ {2}} w a _ {r, w _ {b}} - \sum_ {w _ {a} \in D _ {1}} w a _ {r, w _ {a}} + \sum_ {w _ {b} \in D _ {2}} \sum_ {t \in s t a r t _ {r, w _ {b}}} t i m e (w _ {b}) \cdot x _ {r, w _ {b}, t} - M \cdot o _ {r, D _ {1}, D _ {2}, t} \leq 0 \\ \sum_ {w _ {a} \in D _ {1}} w a _ {r, w _ {a}} - \sum_ {w _ {b} \in D _ {2}} w a _ {r, w _ {b}} + \sum_ {w _ {a} \in D _ {1}} \sum_ {t \in s t a r t _ {r, w _ {a}}} t i m e (w _ {a}) \cdot x _ {r, w _ {a}, t} - M \cdot \left(1 - o _ {r, D _ {1}, D _ {2}, t}\right) \leq 0 \end{array}\tag{A.2}
$$

where M is a suf<sup>fi</sup>ciently large number and $o _ { r , D _ { 1 } , D _ { 2 } , 1 }$ is a boolean variable that needs to be introduced in the MILP problem.

Proof of Lemma 2. Let us consider the constraints in Eq. (A.2), and let us introduce for readability purposes the following equality:

$$
\begin{array}{l} \sum_ {w _ {b} \in D _ {2}} w a _ {r, w _ {b}} - \sum_ {w _ {a} \in D _ {1}} w a _ {r, w _ {a}} + \sum_ {w _ {b} \in D _ {2}} \sum_ {t \in s t a r t _ {r, w _ {b}}} t i m e (w _ {b}) \cdot x _ {r, w _ {b}, t} = a \\ \sum_ {w _ {a} \in D _ {1}} w a _ {r, w _ {a}} - \sum_ {w _ {b} \in D _ {2}} w a _ {r, w _ {b}} + \sum_ {w _ {a} \in D _ {1}} \sum_ {t \in s t a r t _ {r, w _ {a}}} t i m e (w _ {a}) \cdot x _ {r, w _ {a}, t} = b. \end{array}
$$

we can then rewrite Eq. (A.2) as:

$$
\begin{array}{l} a - M \cdot o _ {r, D _ {1}, D _ {2}, t} \leq 0 \\ b - M \cdot \left(1 - o _ {r, D _ {1}, D _ {2}, t}\right) \leq 0. \end{array}
$$

The <sup>fi</sup>rst constraint in Eq. (A.2) can only be satis<sup>fi</sup>ed if either $a \leq 0$ or $\mathrm { i f } - M \cdot 0 _ { r , D _ { 1 } , D _ { 2 } , t } \leq 0 .$ . Similarly, the second constraint can only be satis<sup>fi</sup>ed <sup></sup>if either $b \leq 0$ or $\mathrm { i f } - M \cdot \left( 1 - O _ { r , D _ { 1 } , D _ { 2 } , t } \right) \leq 0 .$ . Since $O r , D _ { 1 } , D _ { 2 } , t$ can only be 0 or <sup></sup>1, we can see that in order to satisfy both constraints either $a \leq 0$ or $b \leq 0$ must be satis<sup>fi</sup>ed that is exactly the constraint de<sup>fi</sup>ned in Eq. (3).

## Appendix B. Supplementary data

Supplementary data to this article can be found online at http://dx. doi.org/10.1016/j.dss.2014.10.006.

## References

[1] Standards Australia and Standards New Zealand, Standard AS/NZS ISO 31000, 2009.

[2] Basel Committee on Bankin Supervision, Basel II — International Convergence of Capital Measurement and Capital Standards, 2006.

[3] R. Conforti, G. Fortino, M. La Rosa, A. ter Hofstede, History-aware, real-time risk detection in business processes, Proc. of CoopIS, Volume 7044 of LNCSSpringer, 2011.

[4] R. Conforti, A.H.M. ter Hofstede, M. La Rosa, M. Adams, Automated risk mitigation in business processes, Proc. of CoopIS, Volume 7565 of LNCSSpringer, 2012.

[5] R. Conforti, M. La Rosa, G. Fortino, A. ter Hofstede, J. Recker, M. Adams, Real-time risk monitoring in business processes: a sensor-based approach, Journal of Systems and Software 86 (2013) 2939–2965.

[6] C. Alberts, A. Dorofee, OCTAVE criteria, version 2.0, Technical Report CMU/SEI-2001- TR-016, Carnegie Mellon University, 2001.

[7] B. Barber, J. Davey, The Use of the CCTA Risk Analysis and Management Methodology CRAMM in Health Information Systems, MEDINFO, North Holland Publishing, 1992.

[8] M. Lund, B. Solhaug, K. Stølen, Model-driven Risk Analysis — The CORAS Approach, Springer, 2011.

[9] Suriadi Suriadi, Burkhard Weiß, Winkelmann Axel, Arthur H.M. ter Hofstede, Michael Adams, Raffaele Conforti, Colin Fidge, Marcello La Rosa, Ouyang Chun Pika Anastasiia, Rosemann Michael, Wynn Moe, Current Research in Risk-aware Business Process Management―Overview, Comparison, and Gap Analysis, Communications of the Association for Information Systems: Vol. 34 (2014) Article 52. Available at: http://aisel.aisnet.org/cais/vol34/iss1/52.

[10] A. Pika, W. van der Aalst, C. Fidge, A. ter Hofstede, M. Wynn, Predicting deadline transgressions using event logs, Proc. of BPM Workshop 2012, Volume 132 of LNBIPSpringer, 2013.

[11] S. Suriadi, C. Ouyang, W. van der Aalst, A. ter Hofstede, Root cause analysis with enriched process logs, Proc. of BPM Workshop 2012, Volume 132 of LNBIPSpringer, 2013.

[12] D. Vengerov, A reinforcement learning approach to dynamic resource allocation, Engineering Applications of Arti<sup>fi</sup>cial Intelligence 20 (2007) 383–390.

[13] S.E. Elmaghraby, Resource allocation via dynamic programming in activity networks, European Journal of Operational Research 64 (1993) 199–215.

[14] K. Baker, Introduction to Sequencing and Scheduling, Wiley, 1974.

[15] W. Zhang, T.G. Dietterich, A reinforcement learning approach to job-shop scheduling, Proceedings of the 14th International Joint Conference on Arti<sup>fi</sup>cial Intelligence JCAI'95 Vol 2 Morgan Kaufmann Publishers Inc San Francisco CA USA 1995 pp. 1114-1120

[16] A. Kumar, W.M.P. van der Aalst, E.M.W. Verbeek, Dynamic work distribution in workflow management systems: how to balance quality and performance, Journal of Management Information Systems 18 (2002).157–193

[17] J. Nakatumba, M. Westergaard, W.M.P. van der Aalst, A meta-model for operational support, BPM Center Report BPM-12-05, 2012 (BPMcenter.org).

[18] H. Schonenberg, B. Weber, B.F. Dongen, W.M.P. Aalst, Supporting <sup>fl</sup>exible processes through recommendations based on history, Proceedings of the 6th Conference Business Process Management (BPM 2008), Volume 5240 of LNCSSpringer, Berlin Heidelberg, 2008.

[19] F.M. Maggi, C. Di Francescomarino, M. Dumas, C. Ghidini, Predictive monitoring of business processes, in: M. Jarke, J. Mylopoulos, C. Quix, C. Rolland, Y. Manolopoulos, H. Mouratidis, J. Horkoff (Eds.), Proceedings of the 26th International Conference on Advanced Information Systems Engineering (CAiSE'14), Volume 8484 of Lecture Notes in Computer ScienceSpringer International Publishing, 2014, pp. 457–472.

[20] M. Montali, F.M. Maggi, F. Chesani, P. Mello, W.M.P. v. d. Aalst, Monitoring business constraints with the event calculus, ACM Transactions on Intelligent Systems and Technology 5 (17) (2013) 1–17 (30).

[21] A. Kim, J. Obregon, J.-Y. Jung, Constructing decision trees from process logs for performer recommendation, Proceedings of 2013 Business Process Management Workshops, LNBIP, Springer, 2014 (To appear).

[22] I.-T. Yang, Utility-based decision support system for schedule optimization, Decision Support Systems 44 (2008) 595–605.

[23] A. Kumar, R. Dijkman, M. Song, Optimal resource assignment in work<sup>fl</sup>ows for maximizing cooperation, Business Process Management, Volume 8094 of LNCSSpringer, Berlin Heidelberg, 2013 pp. 235–250.

[24] Z. Huang, X. Lu, H. Duan, A task operation model for resource allocation optimization in business process management, IEEE Transactions on Systems, Man, and Cybernetics Part A: Systems and Humans 42 (2012) 1256–1270.

[25] W.M.P. van der Aalst, M.H. Schonenberg, M. Song, Time prediction based on process mining, Information Systems 36 (2011) 450–475

[26] F. Folino, M. Guarascio, L. Pontieri, Discovering context-aware models for predicting business process performances, Proceedings of Cooperative Information Systems (CoopIS 2012), Volume 7565 of LNCSSpringer, 2012.

[27] S. van der Spoel, M. van Keulen, C. Amrit, Process prediction in noisy data sets: a case study in a Dutch hospital. Proceedings of the Second International Symposium on Data-driven Process Discovery and Analysis, SIMPDA 2012, Volume 162 of LNBIPSpringer Verlag, 2013 pp. 60–83

[28] C. Cabanillas, J.M. García, M. Resinas, D. Ruiz, J. Mendling, A. Ruiz-Cortés, Prioritybased human resource allocation in business processes, Proceedings of 11th International Conference on Service Oriented Computing (ICSOC 2013), Volume 8274 of LNCS, 2013, pp. 374–388.

[29] I. Barba, B. Weber, C. Valle, Supporting the optimized execution of business processes through recommendations, Business Process Management Workshops, Volume 99 of LNBIPSpringer, Berlin Heidelberg, 2012, pp. 135–140.

[30] S. Alter, A work system view of DSS in its fourth decade, Decision Support Systems 38 (2004) 319–327.

[31] M. de Leoni, M. Adams, W.M.P. van der Aalst, A.H.M. ter Hofstede, Visual support for work assignment in process-aware information systems: framework formalisation and implementation, Decision Support Systems 54 (2012) 345–361.

[32] J. Garca, D. Ruiz, A. Ruiz-Corts, A model of user preferences for semantic services discovery and ranking, in: L. Aroyo, G. Antoniou, E. Hyvnen, A. ten Teije, H. Stuckenschmidt, L. Cabral, T. Tudorache (Eds.), The Semantic Web: Research and Applications, Volume 6089 of LNCSSpringer, 2010, pp. 1–14.

[33] S. Rinderle-Ma, W.M. van der Aalst, Life-cycle support for staff assignment rules in process-aware information systems, Technical Report WP 213, BETA Working Paper SeriesEindhoven University of Technology, 2007.

[34] Z. Huang, X. Lu, H. Duan, Mining association rules to support resource allocation in business process management, Expert Systems with Applications 38 (2011) 9483–9490.

[35] Y. Liu, J. Wang, Y. Yang, J. Sun, A semi-automatic approach for work<sup>fl</sup>ow staff assignment, Computers in Industry 59 (2008) 463–476.

[36] R. Conforti, M. de Leoni, M. La Rosa, W.M. van der Aalst, Supporting risk-informed decisions during business process execution, Proceedings of CAiSE, Volume 7908 of LNCSSpringer, 2013, pp. 116–132.

[37] W. Aalst, Process Mining — Discovery, Conformance and Enhancement of Business Processes, Springer, 2011.

[38] M. Dumas, W.M.P. van der Aalst, A.H.M. ter Hofstede, Process-Aware Information Systems: Bridging People and Software Through Process Technology, Wiley & Sons, 2005.

[39] I.E. Commission, IEC 61025 Fault Tree Analysis (FTA), 1990.

[40] W. Johnson, MORT — The Management Oversight and Risk Tree, U.S. Atomic Energy Commission, 1973.

[41] A.H.M. ter Hofstede, W.M.P. van der Aalst, M. Adams, N. Russell, Modern Business Process Automation: YAWL and its Support Environment, Springer, 2010.

[42] Voluntary Interindustry Commerce Solutions Association, Voluntary Inter-industry Commerce Standard (VICS), http://www.vics.org (Accessed: June 2011).

[43] J.R. Quinlan, C4.5: Programs for Machine Learning, Morgan Kaufmann Publishers Inc., 1993

[44] T. Koch, T. Achterberg, E. Andersen, O. Bastert, T. Berthold, R. Bixby, E. Danna, G. Gamrath, A. Gleixner, S. Heinz, A. Lodi, H. Mittelmann, T. Ralphs, D. Salvagnin, D. Steffy, K. Wolter, Miplib 2010, Mathematical Programming Computation 3 (2011) 103–163.

[45] N. Russell, W.M.P. van der Aalst, A.H.M. ter Hofstede, D. Edmond, Work<sup>fl</sup>ow resource patterns: identi<sup>fi</sup>cation, representation and tool support, Proceedings of CAiSE, Volume 3520 of LNCSSpringer, 2005, pp. 216–232.

Raffaele Conforti is a post-doctoral research fellow in the Information Systems School in the Science and Engineering Faculty, Queensland University of Technology, Brisbane, Australia. He received his PhD from Queensland University of Technology in 2014. He is conducting research in the area of business process management. His research focuses on incorporating aspects of risk management into business process management systems. In particular he focuses on the identi<sup>fi</sup>cation of techniques for automatic detection, prevention and mitigation of risks that may eventuate during the execution of business pro cesses.

Massimiliano de Leoni is an Assistant Professor of Information Systems at the Technische Universiteit Eindhoven (TU/e), The Netherlands. In 2009, he earned a Ph.D. in Computer Engineering at SAPIENZA - University of Rome (Italy) discussing a dissertation on “Adaptive Process Management in Highly Dynamic and Pervasive Scenarios”. He has been guest research fellow at Queensland University of Technology, Vienna University of Economics and Business and University of Naples. His research interests are in the area of Processaware Information Systems and Business Process Management, predominantly focusing on multi-perspective process mining, process-aware decision support systems and visualization techniques for business process management and analysis.

Marcello La Rosa is associate professor of business process management and academic director for corporate engagements for the Information Systems School at the Queensland University of Technology, Brisbane, Australia. He researches on process consolidation, mining, con<sup>fi</sup>guration and automation. He received his PhD degree from Queensland University of Technology in 2009.

Wil van der Aalst is a full professor of Information Systems at the Technische Universiteit Eindhoven (TU/e). He is also an adjunct professor at Queensland University of Technology (QUT). His research interests include work<sup>fl</sup>ow management, process mining, Petri nets, business process management, process modeling, and process analysis. He is an elected member of the Royal Holland Society of Sciences and Humanities (Koninklijke Hollandsche Maatschappij der Wetenschappen) and the Academy of Europe (Academia Europaea).

Arthur ter Hofstede is a Professor in the Information Systems School in the Science and Engineering Faculty, Queensland University of Technology, Brisbane, Australia, and is Head of the Business Process Management Discipline. He is also a Professor in the Information Systems Group at Eindhoven University of Technology, Eindhoven, The Netherlands His main research interests lie in the areas of business process automation and process mining.
