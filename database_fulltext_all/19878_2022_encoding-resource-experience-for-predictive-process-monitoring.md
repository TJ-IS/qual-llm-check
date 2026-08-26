---
otero_id: 19878
otero_key: "HN5TUB7Z"
title: "Encoding resource experience for predictive process monitoring"
authors: "Jongchan Kim; Marco Comuzzi; Marlon Dumas; Fabrizio Maria Maggi; Irene Teinemaa"
year: "2022"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2021.113669"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Encoding resource experience for predictive process monitoring

![](/api/attachments/HN5TUB7Z/fulltext/images/710948228af0421072b4854802a2ba0a675ff0660c286d68da256f659ad389e8.jpg)

Jongchan Kim <sup>a,1</sup>, Marco Comuzzi <sup>b,\*</sup>, Marlon Dumas <sup>c</sup>, Fabrizio Maria Maggi <sup>d</sup>, Irene Teinemaa <sup>e</sup>

<sup>a</sup> Data Science Cell, Big data & AI Lab, Hana Institute of Technology, Seoul, Republic of Korea

<sup>b</sup> Department of Industrial Engineering, Ulsan National Institute of Science and Technology, Ulsan, Republic of Korea

<sup>c</sup> Institute of Computer Science, University of Tartu, Tartu, Estonia

<sup>d</sup> Faculty of Computer Science, Free University of Bozen-Bolzano, Bolzano, Italy

<sup>e</sup> Booking.com, Amsterdam, The Netherlands

## A R T I C L E I N F O

Keywords: Process mining Predictive process monitoring Resource experience

## A B S T R A C T

Events recorded during the execution of a business process can be used to train models to predict, at run-time, the outcome of each execution of the process (a.k.a. case). In this setting, the outcome of a case may refer to whether a given case led to a customer complaint or not, or to a product return or other claims, or whether a case was completed on time or not. Existing approaches to train such predictive models do not take into account infor mation about the prior experience of the (human) resources assigned to each task in the process. Instead, these approaches simply encode the resource who performs each task as a categorical (possibly one-hot encoded) feature. Yet, the experience of the resources involved in the execution of a case may clearly have an impact on the case outcome. For example, specialized resources or resources who are familiar with a given type of case, are more likely to execute the tasks in a case faster and more effectively, leading to a higher probability of a positive outcome. Motivated by this observation, this article proposes and evaluates a framework to extract features from event logs that capture the experience of the resources involved in a business process. The framework exploits traditional principles from the literature to capture resource experience, such as experiential learning and social ties on the workplace. The proposed framework is evaluated by comparing the performance of state-of-the-art predictive models trained with and without the proposed resource experience features, using publicly avail able event logs. The results show that the proposed resource experience features may improve the accuracy of predictive models, but that depends on the process execution context, such as the type of process generating an event log or the type of label that is predicted.

## 1. Introduction

Business processes are often supported by enterprise software sys tems, such as Customer Relationship Management (CRM) systems or Enterprise Resource Planning (ERP) systems. Such systems keep detailed records of relevant events that punctuate the execution of a process, such as the start or completion of tasks, the receipt of messages, etc. These records can be extracted from the databases of these systems and packaged in the form of event logs. In this context, an event log is a collection of (execution) traces, each one capturing the trail of events that occurred during one particular execution of a process (a.k.a. case). Each trace, in turn, consists of a sequence of events. Events are ordered in time, usually because they contain at least one timestamp. Moreover, an event contains a reference to a task, an identifier of the resource that performed the task, and possibly other domain-specific attributes.

Predictive process monitoring is a family of techniques that exploits event logs of business processes in order to generate predictions of future states or properties of each ongoing case of a process. Predictive moni toring methods differ depending on the prediction target. For example, a subset of predictive monitoring methods focus on predicting the remaining time of a case [53], while other methods focus on predicting the next events [9] or the outcome of a case [50]. In this paper, we focus on the latter “outcome-oriented” methods, i.e., we aim at predicting a case outcome expressed as a binary property of a case that is known when the case completes. For instance, in an order-to-cash process, the outcome of a case may be that the customer is satisfied with the deliv ered product (or, conversely, that the customer is unsatisfied), whereas in a helpdesk process the outcome may be that the reported issue is resolved on time (versus late) [50]. Predictive models allow decision makers to trigger actions pro-actively in order to prevent undesirable situations in a process.

In order to train machine learning models for predictive process monitoring, each prefix of a trace in the log (representing a partial case execution) is transformed into a feature vector, which is then labeled by a prediction target (e.g., the case outcome). The resulting set of labeled feature vectors is then used to train a classifier, a regressor or other types of predictive models (e.g., structured predictors). The resulting model is then fed with feature-encoded incomplete cases, at runtime, to generate the desired predictions.

The accuracy of a predictive monitoring method largely depends on the richness of information encoded in the feature vectors representing the incomplete cases. A wide range of methods for encoding incomplete traces as feature vectors have been proposed and evaluated in the literature [50]. These methods differ in terms of how they encode the temporal information (timestamps), the sequences of tasks, the (human) resources that perform each task, and other domain-specific attributes. As far as resources are concerned, existing approaches treat the resource as any ordinary attribute and in doing so, they neglect the fact that the outcome of a case (or the remaining time or other properties of a case) largely depend on the assignment of resources to tasks. In particular, existing predictive process monitoring approaches do not take into ac count the prior experience of the resources assigned to each task in a case.

Yet, resource experience plays an important role in the way a process case will unfold. In both clerical and knowledge-based tasks, users tend to become more efficient and effective as they gain experience on a certain task [29]. The more recent the experience, the stronger this ef fect may be. Also, users may be more efficient or effective when working with other specific users, for instance, because of their good personal relations or fit of personalities [12]. Based on these considerations, we hypothesize that resource information in an event log can be exploited to derive an additional set of features to enhance the performance of the trained predictive models.

This article proposes a framework for deriving features capturing resource experience from the raw data available in an event log. To this end, the paper identifies four dimensions of resource experience in business processes, which can be combined to obtain a wide set of resource experience features. For example, the experience of a resource may be captured by measures related to task familiarity, such as the number of times the resource has executed the same task in previous cases of the same process.

The proposed resource experience features are then used to extend the feature vectors used for training the predictive models. The article then investigates the effect of these resource experience features on the performance of the models used for predicting case outcomes. Specif ically, the paper reports on an evaluation of the proposed framework designed to address two research questions: Do the new features capturing resource experience help to improve the performance of outcome-oriented predictive models? And, among the different types of features capturing resource experience, which one(s) are the most important in determining the behavior of outcome-oriented predictive models?

The paper is organized as follows. Related work and preliminaries are discussed in Section 2. The research problem is introduced in Sec tion 3. Section 4 presents the framework for generating resource expe rience features, while Section 5 presents the experimental evaluation. Concluding remarks are finally drawn in Section 6.

## 2. Background and related work

This section reviews related work about predictive process moni toring and resource information in event logs (Section 2.1) and about management insights regarding business process outcomes and the development of resource experience in the workplace (Section 2.2).

## 2.1. Predictive process monitoring and resource data in event logs

Predictive process monitoring [34] concerns various prediction tasks such as predicting the outcome of a process [32,50], the next event of a running case [46,48], or a time-related measure, e.g., the remaining time until the termination of a running case [47]. In outcome-oriented predictive monitoring, the outcome of a case is usually a binary vari able. Approaches in the literature often define outcomes as the satis faction of service level agreements or the satisfaction of temporal constraints defined on the order and the occurrence of tasks in a case [35,50]. Extensive efforts have been devoted to enhancing the perfor mance of predictive monitoring models from both the pre-processing and the learning sides. During pre-processing, trace clustering tech niques [13,14,32] and sequence encoding techniques [28,50] have been used to efficiently extract features from the input data. In learning, cutting-edge classification and regression algorithms, such as deep learning, have been applied for the purpose of predicting various targets of interests in business processes [19,27,39,47].

All the aforementioned approaches consider intra-case features, generated only using events within an individual case. These are opposed to inter-case features, which are generated using events across multiple cases in the event log [44]. For instance, given an event occurring at a certain time instant, the number of cases active in a business process at that instant or the number of cases waiting to execute a certain activity in the process at that time instant are typical examples of inter-case features.

While in practice different cases are correlated from the perspectives of resource involvement, remaining time and other attributes, inter-case features have not been considered extensively in predictive process monitoring. The importance of incorporating inter-case features has been pointed out in different prediction tasks. In predicting the risk associated with a case, Conforti et al. [11] considers not only the local risk predictors intended for a single instance, but also the interplay be tween risks associated with multiple instances of the same process. This is motivated by the fact that the same resource can be employed by multiple instances running simultaneously, which may lead to multiple instances sharing some risks. Similarly, Senderovich et al. [43] devel oped an inter-case encoding method that considers concurrently active cases for generating inter-case features (e.g., the number of acute pa tients in the emergency department). More recent research has focused on the modelling of interactions among cases to improve process anal ysis and forecasting. Klijn and Fahland [23] have proposed an approach to model inter-case features for remaining time prediction. The features are used to identify contexts of high remaining time prediction errors, such as when cases are batched. Fahland et al. [17] have proposed an approach for reconstructing missing timestamps when cases share physical resources. Brunk at al. [8] have proposed an approach for predicting unexpected events that considers also the case execution context. Generally, we argue that inter-case features in predictive monitoring have been considered mainly from a system load perspec tive. In this paper, we propose a new class of inter-case features, that is, resource-aware features, which capture the experience of resources by referring to their historical involvement in the execution of a process.

Nakatumba and van der Aalst [37] developed a technique to analyse the impact of resource workload on service times using event log data. From the perspective of resource allocation, Arias et al. [3] proposed a resource allocation recommendation framework based on metrics such as frequency, performance, quality, cost, expertise and workload. Zhao et al. [55] propose a resource allocation optimisation model that con siders the constraints of process execution time, cost and resource availability. Bidar et al. [5] consider resource preferences to solve the problem of resource-task allocation in business process automation. Erasmus et al. [16] also aim at improving the resource allocation in business processes by considering the resource ability, specified using the Fleishman’s taxonomy. As far as performance monitoring is con cerned, Senderovich et al. [45] use data mining classification and heuristic methods based on queuing theory to show how the perfor mance of a process can be affected by the scheduling of resources. While focusing on different objectives, these works characterise resources in terms of their expertise or ability, i.e., the set of tasks that they usually perform, workload, $\mathrm { i . e . , }$ , the number of tasks or cases in which they are currently involved in, and the type of outcomes of cases in which they are involved in.

Pika et al. [41] devised a method to mine resource profiles from event logs. These profiles characterize resources in terms of skills, uti lization, preferences, productivity and collaboration. Even though they are not intended to serve as features for predictive process monitoring, the rationale behind the design of resource profiles is in several ways similar to the rationale behind the framework that we propose. For instance, the skills profile is defined by the number of tasks in which a resource participates, while the productivity profile is linked to the outcome of the cases in which resources participate. Similarly, the number of tasks executed by a resource and the ratio of cases involving a resource with positive outcomes are features defined in our framework. A deeper comparison between resource profiles and our proposed fea tures is provided later in Section 4.4.

## 2.2. Business process outcomes and resource experience

Business process outcomes concern the improvement of the opera tional efficiency, effectiveness and flexibility of business processes [36]. They are normally evaluated using process performance indicators [1]. While research has scarcely investigated the direct relation between resource experience and business process outcomes, a large body of research has focused on the positive relation between IT implementation and capabilities, in particular ERP systems, and business process out comes [22,54]. In this context, the skills of the IT resources and the actual usage of IT systems normally is positively related with positive process outcomes. In the healthcare sector, the Donabedian conceptual model [15] assumes that the structure of a healthcare organisation, including its human resources, influences the healthcare outcome through the process, i.e., the set of actions that make up the provisioning of healthcare services. Finally, the reflective perspective on business process management [4] suggests that the human resource individual experience can play a major positive role in the design, enactment, monitoring and improvement of organisational business processes.

A number of classic theories in management have highlighted how repeating experience and developing social ties on the workplace can positively influence individual job performance. The commonly under stood concept of the learning curve, which has also found empirical evidence [29,51], explains the idea that performance on the workplace improves with experience at repeating the same or similar tasks. Similar learning dynamics are posited by the theories of experiential learning [20,25] and absorptive capacity at the individual level [10]. Experien tial learning affirms that learning occurs mainly through experience. In the workplace, experience is gained by repeating the same or similar tasks several times. Absorptive capacity is the ability to recognize the value of new information, assimilate it, and apply it for commercial ends [10], which has a positive impact on performance. At the individual level, this translates into the ability of individuals to assimilate and apply knowledge about executing tasks in order to improve their ability to execute them in the future [40]. There is also empirical evidence that experience learned in the workplace can be forgotten [21], which sup ports arguments in favor of periodically refreshing knowledge and skills.

While most evidence of learning through experience applies to clerical and manual work, individual performance in knowledgeintensive work is often associated with properties of both networks and ties [12]. Networks refer to whom a resource interacts with while performing their work, whereas ties refer to the nature of such re lationships, $\mathrm { e . } \mathrm { g . }$ , whether resources have a personality similar to the one of the other resources with whom they have to work. Generally, per formance and creativity in knowledge-intensive work is positively influenced by employees having a central position in organizational networks with strong ties, e.g., strong personality fit or matching work attitudes with other employees [7,12].

## 3. Problem definition

An event in an event log records the execution of a particular work item in an individual execution of a business process, i.e., a process case. Each work item is an instance of a task.

An event log EL contains events. An event e is a tuple $e =$ $( c , a , t , r , ( d _ { 1 } , \nu _ { 1 } ) , . . . , ( d _ { m } , \nu _ { m } ) )$ , where c is the case id, a is the task of which the work $\mathrm { i t e m ^ { 2 } }$ recorded by this event is an instance, t is the timestamp at which the event has been recorded, r is the resource that executed the work item and $( d _ { 1 } , \nu _ { 1 } ) , . . . , ( d _ { m } , \nu _ { m } ) .$ , with $m \geq 0 ,$ , are other domain specific attributes and their values. For instance, the event $e =$ $( 4 5 ,$ assess, 2020.1.2, Alice, amount = 1000, type = deep) captures the fact that, in a process case associated with loan request number $^ { 4 5 , }$ , the resource Alice has executed a deep assessment of a loan request of 1000 USD on January 2nd, 2020. Note that, strictly speaking, the approach proposed in this paper requires, for each event, only the attributes $c ,$ a and $r _ { * }$ The timestamps, in particular, are not required as long as the events in EL are ordered in time.

The universes of all events, tasks, and resources are denoted by ℰ, ??, and ${ \mathcal { R } } ,$ , respectively. We use a dotted notation to identify attributes of events, $\mathrm { e . g . , } e$ . c to identify the case id of event e. We refer to $A _ { \mathrm { E L } } { \subset } { \mathcal { A } }$ as the set of tasks that have at least one event in $E L ,$ i.e., A = $\{ \overline { { a } } \in \mathcal { A } : \exists e \in \mathrm { E L } , e . a = \overline { { a } } \}$

The sequence of events generated in a given case form a trace $\sigma =$ $[ e _ { 1 } , . . . , e _ { n } ]$ , where $\forall i \in [ 1 , n ] , e _ { i } \in \mathcal { E } ,$ , and ∀ $i , j \in [ 1 , n ] , e _ { i } \mathrm { . } c = e _ { j } \mathrm { . } c , \mathrm { i . e . }$ , all events belong to the same case; events in a trace must be ordered in time, using the timestamps when these are available. The universe of all traces is denoted by ??. The function trace : $\mathcal { E } { \longrightarrow } S$ returns the trace σ to which an event e belongs, i.e., trace(e) = σ. Note that attributes of events $e _ { i }$ belonging to a trace σ may be the same $\forall e _ { i } \in \sigma .$ , We refer to these attributes as case-level attributes. For instance, the amount requested in a loan request process is a case-level attribute. Attributes that can change for different events are called event-level attributes.

Given a trace σ of length n and an integer $l \leq n ,$ the prefix function returns the first l events of $\sigma ,$ that ${ \mathrm { i } } s ,$ prefix $( \sigma , l ) = [ e _ { 1 } , . . . , e _ { l } ] { } $ . A labeling function $y : S { \longrightarrow } \mathcal { D }$ is a function mapping a trace $\sigma \in S$ to its class label $y ( \sigma ) \in \mathcal { D } ,$ , with $\mathcal { V }$ being the domain of the class labels. For outcome predictions, ?? is a finite set of categorical outcomes. In the context of this paper, we consider a binary outcome, i.e., $\mathcal { V } = \{ 0 , 1 \}$ . A label can also be associated to prefixes and all prefixes generated from a trace σ have the same class label (the one associated to σ). Similarly, we also define an event labeling function $\mathbf { y } \mathbf { e } : { \mathcal { E } } { \longrightarrow } { \mathcal { V } }$ that associates to an event the label of the trace to which it belongs, i.e., $\mathrm { y e } ( e ) = y ( \mathrm { t r a c e } ( e ) )$ , ∀e.

In the specific case of outcome-based predictive monitoring, pre dictions are made using a classifier that takes as input a fixed number of independent variables (features) and learns a function to estimate the dependent variable (class label). This implies that, in order to use the data in an event log as input to a classifier, each trace in the log must be encoded as a feature vector. A sequence (or trace) encoder $f : S { \longrightarrow } \mathcal { X } _ { 1 }$ × $\dots \times \mathcal { X } _ { P }$ is a function that takes a (partial) trace σ and transforms it into a feature vector in a P-dimensional vector space $\mathcal { X } _ { 1 } \times \ldots \times \mathcal { X } _ { P }$ with $\mathscr { X } _ { p } \subseteq \mathbb { R }$ $1 \leq p \leq P$ being the domain of the p-th feature.

We divide features further into resource-aware and non-resourceaware. The former are generated using resource information in events, while the latter are generated without considering resource information. Let us assume that, among the P features generated from a (partial) trace σ, R features, with $R \leq P ,$ are non-resource-aware, whereas the remaining (P − R) features are resource-aware. Given R non-resourceaware features with domains $\mathcal { X } _ { 1 } , . . . , \mathcal { X } _ { R }$ and $( P - R )$ resource-aware features with domains $\mathcal { X } _ { R + 1 } , . . . , \mathcal { X } _ { P } ,$ we distinguish between resourceaware and non-resource-aware classifiers for outcome-based predictive monitoring. A resource-aware classifier rac is a function that estimates the probability of a class label to be assigned to a feature vector including resource-aware features, i.e., rac : $\mathcal X _ { 1 } \times \ . . . \times \ \mathcal X _ { R } \times \mathcal X _ { R + 1 } \times$ $\therefore . . { \mathcal { X } } _ { P } { \longrightarrow } { \mathcal { Y } } .$ . A non-resource-aware classifier nrac is a function that esti mates the probability of a class label to be assigned to a feature vector that does not include resource-aware features, i.e., nrac : ?? × $. . . \mathcal { X } _ { R } \longrightarrow \mathcal { V }$

![](/api/attachments/HN5TUB7Z/fulltext/images/cd7b651592d2111e18d4b0bee22a814ba9269893584af386ccde85bfcbb0a481.jpg)  
Fig. 1. Resource experience framework

One important element to model resource-aware features is the handoff, which captures the handover of work between resource executing consecutive events in a case. Formally, a handoff $h ( r _ { 1 } , r _ { 2 } )$ , with $r _ { 1 } , r _ { 2 } \in \mathcal { R } _ { : }$ , is a relation that associates a resource r that executed a given work item $e _ { 2 }$ in a trace σ to the resource $r _ { 1 }$ that executed the event e preceding e in σ, that is $h ( r _ { 1 } , r _ { 2 } ) \Leftrightarrow \exists e _ { 1 } , e _ { 2 } , \sigma : e _ { 1 } , e _ { 2 } \in \sigma \land e _ { 1 } . t < e _ { 2 }$ $t \wedge e _ { 1 } . r = r _ { 1 } \wedge e _ { 2 } . r = r _ { 2 } \wedge \sharp e _ { 3 } \in \sigma : e _ { 1 } . t < e _ { 3 } . t < e _ { 2 } . t .$

## 4. Approach

Section 4.1 introduces the framework for encoding resource experi ence, while Section 4.2 defines the dimensions of the framework. Sec tion 4.3 formally defines the resource-aware features considered in this paper, whereas Section 4.4 finally draws a detailed comparison between the proposed framework with the Pika et al.’s one referenced earlier.

## 4.1. A conceptual framework for encoding resource-aware features

To identify relevant features for training machine learning models to predict case outcomes, we systematically asked the $5 { + } 1 \ ^ { \cdots } \mathsf W ^ { \ast }$ questions: Why, Who, Where, When, What, and How. We discarded the “Who” question because the “Who” is the resource itself. We also discarded the “Why” question (“Why has a resource been allocated to a work item?”) because an event log does not directly contain information that would allow us to determine the reasons for a given allocation decision. In addition, in several settings, the allocation decision, as reflected in an event log, may be determined simply by the availability of resources.

The “When” question (“When has a resource performed a given task?”) led us to identify Recency (“When was the most recent occasion when a resource performed a task?”) as a source of features for capturing the notion of experience. The “Where” question (“Where or, more spe cifically, in which context did a resource perform a task?”) led us to identify the Context as a possible source of features. By context, we mean the conditions under which a resource performed a given task. The “What” question led us to observe that resources gain experience in different ways, such as performing a given task or work item, or participating in the same case for which a prediction is being made. We introduce the Target dimension of resource experience to capture these multiple ways for resources to gain experience. Finally, the “How” question (“How much prior experience does a resource have?”) led us to identify the Aspect, i.e., the measure used to quantify the resource experience in the scope identified using the previous dimensions. Accordingly, we retained four dimensions for encoding resource expe rience as a feature vector: Recency, Context, Target, and Aspect (cf. Fig. 1).

Note that the atomic actions that define experience in our framework are (i) execution of work items and (ii) involvement in handoffs. In other words, resources gain experience through executing work items and through interacting with other resources when receiving work from them. The former captures the experiential learning nature of resource experience, whereas the latter captures the importance of social ties in the development of the job experience.

Next, we discuss in detail the dimensions of the proposed framework. For each dimension, we identify the values that it can assume. Note that our objective is to define resource-aware features for each event, when processing a given prefix obtained from a trace.

## 4.2. Dimensions of resource-aware features

Recency (rec): Using the same skills and knowledge to execute work items over and over again keeps them fresh in our memory. At the same time, when skills are not practiced for some time, they start to fade away [21,26]. For instance, a resource that performed a particular task two days ago is likely to perform the same task more efficiently today than another resource who last performed the same task a year ago. The Recency dimension of resource experience accounts for the time scope in which a resource has acquired a given experience. Regarding values, we distinguish between long-term recency, i.e., the considered time scope starts from the time of the earliest event in an event log, and short-term recency, i.e., the time scope is limited to a given time in the past until the timestamp of the current event. In principle, short-term

<table><tr><td> $\vdots$ </td><td> $\vdots$ </td><td> $\vdots$ </td><td> $\vdots$ </td><td> $\ddots$ </td></tr><tr><td> $e_{1}.c$ </td><td colspan="2"> $\cdots$ </td><td> $e_{1}.r$ </td><td> $\cdots$ </td></tr><tr><td> $e_{2}.c$ </td><td> $e_{2}.a$ </td><td> $e_{2}.t$ </td><td> $e_{2}.r$ </td><td> $\cdots$ </td></tr><tr><td> $\vdots$ </td><td> $\vdots$ </td><td> $\vdots$ </td><td> $\vdots$ </td><td> $\ddots$ </td></tr></table>

Table 1

![](/api/attachments/HN5TUB7Z/fulltext/images/f11217928ecfd6d25c50da201f887dc0052e0b2a03d820884ab309bd5e5b39b9.jpg)  
Fig. 2. Extracting resource-aware features from event logs. (For interpretation of the references to color in the text, the reader is referred to the web version of this article.)

Resource-aware features for asp = frequency.  
Table 3  
Resource-aware features for asp = specialization.

<table><tr><td>Feature</td><td>Target</td><td>Context</td><td>Definition</td></tr><tr><td>n_work_items</td><td>Work item</td><td>General</td><td>Number of work items executed by  $e_i$ . r until  $e_i$ . t</td></tr><tr><td>n_cases</td><td>Case</td><td>General</td><td>Number of cases in which  $e_i$ . r executed at least one work item until  $e_i$ . t</td></tr><tr><td>n_tasks</td><td>Task</td><td>General</td><td>Number of unique tasks executed by  $e_i$ . r until  $e_i$ . t</td></tr><tr><td>n_ho</td><td>ho</td><td>General</td><td>Number of unique handoffs involving  $e_i$ . r executed by  $e_i$ . r until  $e_i$ . t</td></tr><tr><td>n_curr_case</td><td>Work item</td><td>curr_case</td><td>Number of work items executed by  $e_i$ . r until  $e_i$ . t in the current case (i.e., having the same value of  $e_i$ . c)</td></tr><tr><td>n_curr_task</td><td>Work item</td><td>curr_task</td><td>Number of work items executed by  $e_i$ . r until  $e_i$ . t having task equal to  $e_i$ . a</td></tr><tr><td>n_curr_ho</td><td>Work item</td><td>curr_ho</td><td>Number of work items executed by  $e_i$ . r until  $e_i$ . t having handoff equal to  $h(e_{i-1}$ . r,  $e_i$ . r)</td></tr></table>

Table 2  
Resource-aware features for asp = performance.

<table><tr><td>Feature</td><td>Target</td><td>Context</td><td>Definition</td></tr><tr><td>per_case</td><td>Case</td><td>General</td><td>Polarity of cases involving  $e_i$ . r until  $e_i$ . t</td></tr><tr><td>per_work_item</td><td>Work item</td><td>General</td><td>Polarity of work items involving  $e_i$ . r until  $e_i$ . t</td></tr><tr><td>per-curr-task</td><td>Work item</td><td>curr-task</td><td>Polarity of work items involving at least one work item of task  $e_i$ . a executed by  $e_i$ . r until  $e_i$ . t</td></tr><tr><td>per-curr-ho</td><td>Work item</td><td>curr-ho</td><td>Polarity of work items involving one handoff equal to  $h(e_{i-1}$ . r,  $e_i$ . r) until  $e_i$ . t</td></tr></table>

<table><tr><td>Feature</td><td>Target</td><td>Context</td><td>Definition</td></tr><tr><td>sp-work_item-case</td><td>Work item</td><td>General</td><td>A/B, with A the number of work items performed by  $e_i$ . r, B the number of cases executed until  $e_i$ . t</td></tr><tr><td>sp-curr-case</td><td>Work item</td><td>curr-case</td><td>A/B, with A the number of work items performed by  $e_i$ . r in case  $e_i$ . c, B the number of work items executed by  $e_i$ . r until  $e_i$ . t</td></tr><tr><td>sp-curr-task</td><td>Work item</td><td>curr-task</td><td>A/B, with A the number of work items performed by  $e_i$ . r corresponding to task  $e_i$ . a, B the number of work items executed by  $e_i$ . r until  $e_i$ . t</td></tr><tr><td>sp-curr-ho</td><td>Work item</td><td>curr-ho</td><td>A/B, with A the number of work items performed by  $e_i$ . r with handoff equal to h ( $e_{i-1}$ . r,  $e_i$ . r), B the number of work items executed by  $e_i$ . r until  $e_i$ . t</td></tr></table>

recency may also be set considering other domain-specific criteria, such a recent number of terminated cases or a recent number of executed work items. In the evaluation, since we did not have any such domain-specific information for the event logs that we used, we set the value of recency to 30 days before the current event for all event logs. value of recency to 30 days before the current event for all event logs.

Table 4  
Resource-aware features for asp = generalization.

<table><tr><td>Feature</td><td>Target</td><td>Context</td><td>Definition</td></tr><tr><td>gen-task</td><td>Task</td><td>General</td><td>Entropy of distribution of tasks executed by  $e_i$ . r until  $e_i$ . t</td></tr><tr><td>gen-case</td><td>Case</td><td>General</td><td>Entropy of distribution of cases executed by  $e_i$ . r until  $e_i$ . t</td></tr><tr><td>gen-ho</td><td>ho</td><td>General</td><td>Entropy of distribution of handoffs executed by  $e_i$ . r until  $e_i$ . t</td></tr></table>

Context. (con): The management literature highlights that resources do not work in an organizational vacuum, but they are positioned within an organizational network, a certain technical environment, and specific organizational processes and policies [7,12], all of which can influence the way in which they learn and perform their tasks. Based on this

<table><tr><td>Feature Name  $F_i$ </td><td>Feature contribution  $C(F_i)$ </td></tr><tr><td> $F_1$ </td><td>0.041</td></tr><tr><td rowspan="2">Resource-aware features ← $F_3$ </td><td>0.014</td></tr><tr><td>0.011</td></tr><tr><td> $F_2$ </td><td></td></tr><tr><td> $F_6$ </td><td>0.009 ↑</td></tr><tr><td rowspan="3">Filtering threshold → $F_7$ </td><td>0.009</td></tr><tr><td>0.008</td></tr><tr><td>0.008</td></tr></table>

Fig. 3. Illustration of the metrics considered in the feature contribution analysis.

Table 5  
Event logs considered in the evaluation.

<table><tr><td>Log</td><td>Process description</td><td>Outcome description</td><td># cases</td><td># events</td><td>Examples of domain-specific features</td></tr><tr><td>BPIC2011_1</td><td rowspan="4">Treatment and diagnosis process in the Gynaecology department of a Dutch academic hospital</td><td rowspan="4">Temporal constraint satisfaction on the order of occurrence of tasks in a case</td><td>1140</td><td>67,480</td><td rowspan="4">Diagnosis code, Treatment code, Specialism code, Age</td></tr><tr><td>BPIC2011_2</td><td>1140</td><td>149,730</td></tr><tr><td>BPIC2011_3</td><td>1121</td><td>70,546</td></tr><tr><td>BPIC2011_4</td><td>1140</td><td>93,065</td></tr><tr><td>BPIC2012_accepted</td><td rowspan="3">Application for a personal loan or overdraft at a global financing organization</td><td rowspan="3">Whether an application is (accepted, cancelled, or declined); or not</td><td>4685</td><td>186,693</td><td rowspan="3">Amount requested, Lifecycle of an application</td></tr><tr><td>BPIC2012_cancelled</td><td>4685</td><td>186,693</td></tr><tr><td>BPIC2012_declined</td><td>4685</td><td>186,693</td></tr><tr><td>BPIC2015_1</td><td rowspan="5">Application for building permit at 5 Dutch municipalities</td><td rowspan="5">Temporal constraint satisfaction on the order of occurrence of tasks in a case</td><td>696</td><td>28,775</td><td rowspan="5">Application cost, Construction, Area protection, Entrance/Way out</td></tr><tr><td>BPIC2015_2</td><td>753</td><td>41,202</td></tr><tr><td>BPIC2015_3</td><td>1328</td><td>57,488</td></tr><tr><td>BPIC2015_4</td><td>577</td><td>24,234</td></tr><tr><td>BPIC2015_5</td><td>376</td><td>1051</td></tr><tr><td>Road Traffic Fines</td><td>Managing fines punishing road traffic infractions, at an Italian regional agency for traffic management</td><td>Whether a fine is repaid in full or sent for credit collection</td><td>129,615</td><td>460,556</td><td>Article, Vehicle class, Infraction type, Fine amount</td></tr></table>

![](/api/attachments/HN5TUB7Z/fulltext/images/238b24a6b0d645889e2e40f80d0c0206fbcf816ae6b9a9b819942049fdfd620e.jpg)  
Fig. 4. Temporal split-based cross-validation procedure.

consideration, we propose that experience is gained by a resource when operating in the same context, such as repeating the same type of tasks within the same process case. For example, if a resource who has considerable experience in performing administrative tasks, such as checking the completeness of a loan application, is asked to compile a loan offer for the first time, she is likely to be less efficient in this task than another resource who has already compiled loan offers multiple times in the past. As far as the values of this dimension are concerned, context can capture the general experience of a resource, e.g., how many work items a resource has executed in a given process, but more importantly it can be restricted to a more specific domain, such as the current case, i.e., how much experience the resource has in the currently running case in executing work items, or the current task, i.e., how many times a resource has executed a work item corresponding to the same task as the current one, or the current handoff, i.e., how many times a resource has executed a work item following the same handoff as the current one.

Note that this list of values, which we consider in this paper, is not exhaustive, as other types of contexts can be relevant depending on the data available, such as the customer, the product type, the case type, or a cluster of (similar) tasks. Context can also be a combination of several attributes, e.g., to answer questions such as “How much experience does the resource have with the given task-handoff pair?”. Furthermore, the context can be related to a (sub)sequence of work items or tasks, e.g., the sequence of tasks from the last three work items, or the tasks of a certain type, where task type is an attribute available in the event log.

Target (tar): This dimension concerns the type of atomic actions through which experience is gained by a resource. Based on the tradi tional theories of the learning curve [51] and experiential learning [20, 25], experience is gained by a resource by participating in some part of the process, i.e., executing a work item in it. Note that often resource experience and performance benefit also from executing a diverse range of tasks in a process [33,42]. This is also implied by the theory of absorptive capacity at the individual level [40]. However, resources may also improve their experience by sharing insights with other resources during the execution of work. This can be fostered by a personality fit or similar work attitudes with other resources [12]. Since in an event log resource information is only associated with individual work items. we assume that resources interact when they execute consecutive work items, i.e., being involved in a handoff. Therefore, we define the following values for the target dimension:

![](/api/attachments/HN5TUB7Z/fulltext/images/18be3a824238ea513e560ff537fe48ac805c027c1ed308277328c890f3de8163.jpg)  
(a) BPIC 2015 \_1 Random Forest

![](/api/attachments/HN5TUB7Z/fulltext/images/5530edba94969424d678195bc9ec69dee9bd6db4c8997f4441237107b509d421.jpg)  
(b) BPIC 2015 \_1 XGBoost

![](/api/attachments/HN5TUB7Z/fulltext/images/37fb543032554754c1441ff0cf054a68ca0b2812009cd358100cb6db1791b6d2.jpg)  
(c) BPIC 2015 \_2 Random Forest

![](/api/attachments/HN5TUB7Z/fulltext/images/04d5633db85cdaa076e0ace2e5bb665cd3f417cd7672315cb199c18f4cf3c7b7.jpg)  
(d) BPIC 2015 \_2 XGBoost

![](/api/attachments/HN5TUB7Z/fulltext/images/1039bd89430c93092d6805a15597d2ee2bd57173833b8474efd0ecd704770f87.jpg)  
(e) BPIC 2015 \_3 Random Forest

![](/api/attachments/HN5TUB7Z/fulltext/images/dfe4e3bfbf1ab5191d40b62c4bb52fc83ebeec9d35f62d20c0fe5ca13eb2dd74.jpg)  
(f) BPIC 2015 \_3 XGBoost

![](/api/attachments/HN5TUB7Z/fulltext/images/966f1a085f9749d37aeb815d33b4134340c90ced9758a5b26a37414e35611848.jpg)  
(g) BPIC 2015 \_4 Random Forest

![](/api/attachments/HN5TUB7Z/fulltext/images/62032c6db14158d21b4d48c9b033972a5cd780a86d42c1974a4f206cb81c4c8d.jpg)  
(h) BPIC 2015 \_4 XGBoost

![](/api/attachments/HN5TUB7Z/fulltext/images/5cbb944b21d45f0249afe81faa86726bc2022fced30afac8e9acc5769e8d568e.jpg)  
(i) BPIC 2015 \_5 Random Forest

![](/api/attachments/HN5TUB7Z/fulltext/images/e3115599b708d4e74ad9b46558232d225ac31cdf8255cdb4377498fb791865a4.jpg)  
19  
(j) BPIC 2015 \_5 XGBoost  
Fig. 5. AUC for different prefix lengths for the BPIC 2015 event logs.

Table 6  
Detailed descriptive statistics of BPIC 2015.

<table><tr><td></td><td>BPIC2015_1</td><td>BPIC2015_2</td><td>BPIC2015_3</td><td>BPIC2015_4</td><td>BPIC2015_5</td></tr><tr><td>Mean case duration</td><td>96 days</td><td>160 days</td><td>63 days</td><td>111 days</td><td>101 days</td></tr><tr><td>Median case duration</td><td>63 days</td><td>115 days</td><td>39 days</td><td>92 days</td><td>80 days</td></tr><tr><td>Number of cases</td><td>696</td><td>753</td><td>1328</td><td>577</td><td>1051</td></tr><tr><td>Number of resources</td><td>22</td><td>9</td><td>18</td><td>12</td><td>15</td></tr><tr><td>Mean number of events in a case</td><td>41</td><td>55</td><td>43</td><td>42</td><td>52</td></tr></table>

• Work Item: experience is gained by executing any work item;

• Case: experience is gained by being involved in a case (executing at least one work item in it);

• Task: experience is gained by executing work items(s) of a given task; • Handoff: experience is gained by interacting with other resources, i. $\mathrm { e } _ { \cdot , }$ being involved in a handoff.

Aspect (asp): While, in general, resource experience is positively correlated with resource performance, that may not always be the case in specific situations. For instance, the experiential learning theory highlights that, in some situations, repetitive tasks may put an excessive mental strain on a resource, which may result in a decrease of perfor mance [20]. As far as workplace ties are concerned, the need to interact with other resources with a conflicting personality or a different work attitude may also lead to decreased performance [12]. Therefore, simply considering the frequency at which a resource has been involved in an atomic action (i.e., a target) through which experience is gained is not likely to capture the full extent of the impact of resource experience on resource performance and, consequently, process performance.

In the proposed framework, given a target of resource experience, evaluated in a given context and in a given time scope (recency), there can be multiple aspects that we want to encode into features. As mentioned above, a first aspect to be considered is the frequency at which a given target of experience occurs for a given resource, e.g., counting the number of times a resource executed a particular task, or counting the number of work items performed by a resource in a process case, in a given period of time. However, other aspects that link the resource experience to the type of experience and the level of process perfor mance achieved may be relevant in a specific context. We, therefore, consider the following additional aspects:

• Performance: this aspect concerns the outcome achieved by the cases in which a resource has gained experience and can be calculated as the ratio between the number of cases with a positive outcome and the number of cases with a negative one;

• Specialization and Generalization: these aspects concern the extent to which experience gained by a resource is concentrated on a spe cific target, i.e., a specific case, task, or work item, or diluted across multiple targets;

• Busyness: this aspect concerns the extent to which the experience gained is concentrated in the time scope defined by the Recency dimension. While the Frequency aspect considers the absolute number of atomic actions occurred in a given a time scope for a resource, this aspect relates this number of occurrences to the duration of the considered time scope.

## 4.3. Definition of resource-aware features

Fig. 2 gives an overview of how events in an event log are encoded for predicting outcomes. In this section, our objective is to define the generated when processing the current event e (event e of case 3 in Fig. 2), of a given trace σ, referred to as the current case in the remainder of this section (case 3 in Fig. 2). To generate the features for $e _ { i } ,$ in particular the resource-aware ones, which are intercase, we must consider the events in the log with timestamps that come before the one of e<sub>i</sub> (events in red on the top-right side of Fig. 2). First, we identify the targets of the current event, i.e., its resource, case id, task, and handoff. Then, features are generated. Next, we define in detail how the resource-aware features are calculated based on the current case id, resource, task and handoff.

Note that, for simplicity, Fig. 2 does not consider features generated from case-level attributes. Also, let us clarify that non-resource-aware features are calculated using traditional methods from the literature, e.g., [50], and include features encoding, for instance, the task label or any other domain specific attribute characterizing $e _ { i } .$ The features associated with the events of a case are finally aggregated into a feature-label vector encoding the current case. The resource-aware features associated with e are described in detail next.

By combining the values of the four dimensions of resource experi ence, a number of resource-aware features can be generated. Note that not all possible combinations of values lead to meaningful features. In the following, we discuss in detail the ones that we consider in this paper.

Next, we group the definitions of resource-aware feature by the value of the aspect dimension. For the sake of conciseness, we only consider the value long-term for the Recency dimension. Feature definitions for rec = short − term can be simply derived by reducing the time scope from the general one, i.e., from the time of the earliest event in an event log until the timestamp e . t of the current event, to a given recent time window defined by a given value $\Delta _ { t } , \mathrm { i . e . , } [ e _ { i } \cdot t - \Delta _ { t } , e _ { i } \cdot t ] .$

## 4.3.1. Frequency aspect

The resource-aware features considered for the frequency aspect (asp = frequency) are shown in Table 1. The ones for con = general count the number of work items/cases/tasks/handoffs in which the resource $e _ { i } , r$ has been involved until $e _ { i } , t .$ Additional features are obtained by restricting the context to the current case, task or handoff.

## 4.3.2. Performance aspect

Given that we consider binary class labels, i.e., ?? = {0, 1}, perfor mance can be calculated using the polarity of the traces S⊂?? (or events E⊂ℰ) obtained from the application of the other dimensions in our framework, that is:

$$
\mathrm{polarity} (S) = \frac {\sum_ {\sigma \in S} y (\sigma)}{| S |}
$$

$$
\operatorname{polarity} (E) = \frac {\sum_ {e \in E} \mathrm{ye} (e)}{| E |}.
$$

For instance, given E as the set of all work items executed from the earliest timestamp in an event log until the current timestamp, (rec = long-term, con = general, tar = work item), the polarity calculates the fraction of events in E having class label equal to 1.

The resource-aware features considered for the performance aspect (asp = performance) are shown in Table 2. Since polarity can only be defined at the level of set of cases or set of events, these features can only consider the values tar = work item and tar = case for the target dimen sion. Note that the value of polarity features for target tar = case differ from tar = work item if a resource executes more than one work item in at least one case.

![](/api/attachments/HN5TUB7Z/fulltext/images/c3ed1f204dc44c899d2d92abb446f157a7dab632a01b2e3da7b9aa78ba34bcc3.jpg)  
(a) BPIC 2015 \_1 Random Forest

![](/api/attachments/HN5TUB7Z/fulltext/images/12bfcd532b9d7f61305ccc8d7ed8125fb2f84aa45953e5585604adaa5ebe7e39.jpg)  
(b) BPIC 2015 \_1 XGBoost

![](/api/attachments/HN5TUB7Z/fulltext/images/07dc93491a621cfcb8c7b9aced7ab3ad2589acc6b4896051dddbe14c2f44998c.jpg)  
(c) BPIC 2015 \_2 Random Forest

![](/api/attachments/HN5TUB7Z/fulltext/images/e34e12fac64fa9c070146359868c3a0056b61e03125d7af0026bed1e7318b0b8.jpg)  
(d) BPIC 2015 \_2 XGBoost

![](/api/attachments/HN5TUB7Z/fulltext/images/0edcb29627081f0a121ca208ade3f84529d1d677c352aa985c78286fb96809bf.jpg)  
(e) BPIC 2015 \_3 Random Forest

![](/api/attachments/HN5TUB7Z/fulltext/images/1f7420b90a8b468871d08769c9262dcb86d80a9fea2b3489c965408ae3e7ef32.jpg)  
(f) BPIC 2015 \_3 XGBoost

![](/api/attachments/HN5TUB7Z/fulltext/images/49a49eb1f97cc1abe8b3862456ee3284cb6f5fa6d960fcdf91680a23aaa68154.jpg)  
(g) BPIC 2015 \_4 Random Forest

![](/api/attachments/HN5TUB7Z/fulltext/images/aa488581c24d915bde8cca643f88f63f4ee4618d2dfcbd653c071490989b4968.jpg)

![](/api/attachments/HN5TUB7Z/fulltext/images/1a8e601dcfe8067b48112513691e38a7c48c09328da6a4dd5faa12c217160d0d.jpg)  
(i) BPIC 2015 \_5 Random Forest

(h)BPIC 2015 \_4 XGBoost  
![](/api/attachments/HN5TUB7Z/fulltext/images/bd6373649af767f98e37f481a006a14a3902cf41ac9601947cc1d21b078edcb4.jpg)  
(i) BPIC 2015 \_5 XGBoost  
Fig. 6. AUC for different prefix lengths for the BPIC 2015 event logs using the temporally-split batches.

![](/api/attachments/HN5TUB7Z/fulltext/images/9a2a7d39c414eda872c91eadab276926d957a332f5f9257cae2e52d19b0ccbbb.jpg)  
(a) Ratio of the top-contributing resource-aware features

![](/api/attachments/HN5TUB7Z/fulltext/images/2ceb6a5a4011a7d8986d18e01d7f3ad68ae9c579ff84b88c8b0c5d75ad74b3dc.jpg)  
(b) Ratio of the cumulative contribution of the topcontributing resource-aware features

Fig. 7. Ratio of the number and cumulative contribution of the top-contributing resource-aware features in the BPIC 2015 logs.  
![](/api/attachments/HN5TUB7Z/fulltext/images/9d932485209ec1aa5a38d562e2bd227ff6f39ce9e5c8b3e583fc84a0c5fd9a99.jpg)  
(a) BPIC 2015\_1 50%

![](/api/attachments/HN5TUB7Z/fulltext/images/69392c14fae91436ae798dac7be2c4595a727b2d4c9aa1b0d6a5f8268b21b57a.jpg)  
(b) BPIC 2015\_2 50%

![](/api/attachments/HN5TUB7Z/fulltext/images/d3bf71089b6043f6c7bc91def9c2cc971078cf65ad0d61020f70acac7476ff37.jpg)  
(c) BPIC 2015\_3 50%

![](/api/attachments/HN5TUB7Z/fulltext/images/04ba65c71b4c195acfd0834ebe6ae104015e29251605547943de5bf309c6b97d.jpg)  
(d) BPIC 2015\_4 50%

![](/api/attachments/HN5TUB7Z/fulltext/images/c44b3f41cb76ce38d9320ab818588d6e1be1da2ad9a1074424066a12514806bc.jpg)  
(e) BPIC 2015\_5 50%  
Fig. 8. Distribution of the top-contributing resource-aware features for the 50% percentile in the BPIC 2015 logs.

## 4.3.3. Specialization and generalization aspects

Specialization and generalization concern assessing whether a resource is specialized in performing a particular task, or possesses more general experience, i.e., has performed several tasks with rather uniform frequencies in the same process. Specialization is calculated as the ratio between the experience of a resource related to a given target in a specific context and the experience of the resource related to the same target in a more general context, e.g., the ratio between the number of work items performed by a resource in a given case and the total number of work items executed by that resource in the entire process determine the specialization of a resource related to the target work item in the context of the current case. Generalization is calculated as the entropy of the distribution of a given a target, e.g., the entropy of the distribution of all tasks executed by a resource until the current event. Given a target $T = \{ t _ { k } \} , \ : { \mathrm { e . g . } }$ , a list of tasks, the entropy of T is calculated as follows:

$$
\operatorname{entropy} (T) = - \sum_ {k} p _ {T} \left(t _ {k}\right) \cdot \log \left(p _ {T} \left(t _ {k}\right)\right)
$$

where ${ p } _ { T } ( t _ { k } )$ is the relative frequency of $t _ { k }$ in T.

The definitions of the resource-aware features considered for the specialization and generalization aspects are shown in Tables 3 and $^ { 4 , }$ respectively.

## 4.3.4. Busyness aspect

Busyness features are calculated by dividing a feature value (ob tained as a frequency) by the time span in which that feature value was calculated. For instance, given the number of work items performed by a resource r, the busyness of r can be calculated as the ratio between this number and the difference between the latest and the earliest timestamp of the tasks executed by r.

As far as feature definitions are concerned, for busyness we consider one single feature busyness with tar = work item and con = general, defined as the number of work items executed by e . r until e . t divided by the time, calculated in days, between the earliest timestamp in the event log and the current timestamp e . t.

To conclude, for a given event, there are a total of 38 resource-aware features, i.e., the 19 described in this section, plus the dual 19 features obtained by considering the recency value $r e c = s h o r t - t e r m .$

## 4.4. Detailed comparison with Pika et al.’s framework

To conclude this section, we can now compare more in depth the proposed resource-aware features with the resource profiles proposed by Pika et al. [41]. Many of the resource-aware features that we propose can be directly subsumed from resource profiles. In particular, this ap plies to all features involving the frequency of work item executions and resource involvement in cases. However, while resource profiles are calculated only using data of completed cases, the resource-aware fea tures that we propose are designed to be calculated for each new event executed in a trace. In addition, the proposed features consider aspects of resource behavior that are not considered by resource profiles, such as the polarity of process outcomes, the entropy, the busyness and the number of work items having the same value of case/task/handoff as the current event. We also consider more detailed features involving work handoffs among resources, whereas resource profiles only consider the total number of handoffs involving a given resource.

![](/api/attachments/HN5TUB7Z/fulltext/images/376f5e687cb2c6d7d66132c3e497a3dcdfda0436c6d2fa5e9391c2630e107372.jpg)  
(a) BPIC 2012\_accepted Random Forest

![](/api/attachments/HN5TUB7Z/fulltext/images/099cce11ae86eeee39fe360375c80679a3cda9f0a0403023f7b12b04a3b0ee15.jpg)  
(b) BPIC 2012\_accepted XGBoost

![](/api/attachments/HN5TUB7Z/fulltext/images/201bf5a0ccd21d8fe855e407d2146ea507c9b53e43d68194e727ad747b6c9bfe.jpg)  
(c) BPIC 2012\_cancelled Random Forest

![](/api/attachments/HN5TUB7Z/fulltext/images/7f2c8558ca943fa81045659001532ea294de36e370c294f1ba5f2e086a74bdb6.jpg)  
(d) BPIC 2012\_cancelled XGBoost

![](/api/attachments/HN5TUB7Z/fulltext/images/e57fb777499085bdb5d98a87dbf652d118697f32e26c57f3dba2eff5a5d55562.jpg)  
(e) BPIC 2012\_declined Random Forest

![](/api/attachments/HN5TUB7Z/fulltext/images/adccfed6dbf63dc1bd753b62990ba897d6897259e3ed3613aca83501181dd9b9.jpg)  
(f) BPIC 2012\_declined XGBoost  
Fig. 9. AUC for different prefix lengths for the BPIC 2012 event logs.

In addition, some of the resource profiles are calculated using domain specific attributes that normally are unavailable in event logs, such as customer feedback or task creator, or are suitable only in specific scenarios. Conversely, the resource-aware features that we propose require attributes that are universally available in event logs, such as case id, activity and resource attributes. Examples of resource profiles that are suitable in specific scenarios are found in the Preferences cate gory. For example, the New attribute values profile in the Preferences category refers to an attribute value never seen before in any prior event.

In reality, an event log may fail to capture all the historic events per taining to the corresponding process, for instance because it logs events only belonging to a specific time period. Therefore, it is uncertain whether an attribute value unseen before the current event is actually a completely new one. Also, the Activity reassignments profile is defined as the number of occurrences of an activity initiated by a given resource and eventually completed by a different one. This assumes that an event log contains information about a work item execution lifecycle, which is often not the case in reality. In addition, this situation does not neces sarily model a resource reassignment as, in some cases, tasks may require multiple resources to sequentially or simultaneously work for their successful completion.

## 5. Evaluation

The first objective of the evaluation is to assess to what extent and/or in which situations the features capturing resource experience defined in this paper increase the performance of outcome-oriented predictive process monitoring. Then, a second objective is to analyse more in detail the explanatory power of resource-aware features. To do ${ \bf { S O } } ,$ we conduct an explainability analysis, to understand the degree to which different types of resource-aware features contribute to the predictions made by a model.

![](/api/attachments/HN5TUB7Z/fulltext/images/6dc7925764ed0a748e48ebdb2ec5db58b3f1b98a5a10b37de19b40cf5c9c86e7.jpg)  
(a) BPIC 2012\_accepted Random Forest

![](/api/attachments/HN5TUB7Z/fulltext/images/f7e55e50a1dea458056ad488dc99f1a902d53311d3826459b42799c594037d13.jpg)  
(b) BPIC 2012\_accepted XGBoost

![](/api/attachments/HN5TUB7Z/fulltext/images/c067581c2f61c4633b843c959e95e92ae458f516317222533ccf978116e2085e.jpg)  
(c) BPIC 2012\_cancelled Random Forest

![](/api/attachments/HN5TUB7Z/fulltext/images/7bb882984c8329bf99701a752cb214e299cc2ffbbad311f4ec7943e42127dba0.jpg)  
(d) BPIC 2012\_cancelled XGBoost

![](/api/attachments/HN5TUB7Z/fulltext/images/89c49fa6bbc22fae4703bb36a2050487cfbc513f4e0baf43ceca7a3656c76e83.jpg)  
(e) BPIC 2012\_declined Random Forest

![](/api/attachments/HN5TUB7Z/fulltext/images/7102281c01db0ee5b3600559dc27a0b3002a08134ff6d62e038228f6c1fed776.jpg)  
(f) BPIC 2012\_declined XGBoost  
Fig. 10. AUC for different prefix lengths for the BPIC 2012 event logs using the temporally-split batches

![](/api/attachments/HN5TUB7Z/fulltext/images/982b4884cab2693c6e6b148ec001d0254a10e30d15222af816c6774ba80c3578.jpg)  
(a) Ratio of the top-contributing resource-aware features

![](/api/attachments/HN5TUB7Z/fulltext/images/a77405e8df999ccbf5cb0b5ab311e8fcbf0ef720d9b9df36cc32a574b0c919d4.jpg)  
(b) Ratio of the cumulative contribution of the topcontributing resource-aware features  
Fig. 11. Ratio of the number and cumulative contribution of the top-contributing resource-aware features in the BPIC 2012 logs.

![](/api/attachments/HN5TUB7Z/fulltext/images/f8cde394714b5cad108867b5b7bceffb476b1bb3ed9dd94ca27e910c933b9a2c.jpg)  
(a) BPIC 2012\_accepted 10%

![](/api/attachments/HN5TUB7Z/fulltext/images/e673b0cc599148cf1776bf078b3ff50a6b6b6e40d7453aedea8c7cd16b894638.jpg)  
(b) BPIC 2012\_cancelled 10%

![](/api/attachments/HN5TUB7Z/fulltext/images/fe5a9af400081bc12c1040e28d572be77f8a6a11c6251940c44453da19107417.jpg)  
(c) BPIC 2012\_declined 10%

![](/api/attachments/HN5TUB7Z/fulltext/images/8d3a4fa92b6324e49d7605375e9b8dc63ccd4afd3371248b80fa4ca6a0d464ce.jpg)  
(d) BPIC 2012\_accepted 50%

![](/api/attachments/HN5TUB7Z/fulltext/images/266e34b095d5349d40dbb0bc11845ae8a262d9302e4e8d226e4742dc8148d0e1.jpg)  
(e) BPIC 2012\_cancelled 50%

![](/api/attachments/HN5TUB7Z/fulltext/images/f7fbc189cb4371a11404fcdf10a2ab8a11187b64ed73dfd9d3d7c2ced53341e5.jpg)  
(f) BPIC 2012\_declined 50%  
Fig. 12. Distribution of the top-contributing resource-aware features for the 10% and 50% percentiles in the BPIC 2012 logs.

We conducted a set of experiments<sup>4</sup> using different event logs pub licly available. For each event log we compare the performance achieved by the model trained using only non-resource-aware features (that is, nrac) and the one that uses also resource-aware features (rac), all other conditions staying equal. As a performance measure we consider the AUC. The AUC is the area under the Receiver Operating Characteristic (ROC) curve, which is constructed based on true positive and false positive rates. It has been considered extensively as a performance measure in existing research on predictive process monitoring [50,52] because it tends to remain unbiased even with imbalanced class labels.

In all the experiments, we consider zero-bucketing of traces and index-based sequence encoding:

• Bucketing in predictive process monitoring [50] is the practice of dividing the encoded prefixes into buckets, i.e., groups, and then training a separate classifier using each bucket of prefixes. Zero-bucketing, which we choose in this work, refers to a default setting in which encoded prefixes are not divided into groups and, therefore, only one classification model is trained with all the encoded prefixes from traces in an event log. In this configuration, prefixes of different length are encoded into feature vectors of different lengths and zero-padding is applied when necessary to bring all feature vectors to the same length for training/testing the classifier.

• Prefixes in predictive process monitoring can be encoded in different ways. A typical solution, which we adopt in this work, is the indexbased sequence encoding [28], whereby each event is encoded into a sequence of features derived from its attributes. Case-level attri butes are encoded only once for each prefix. Index-based encoding is opposed to aggregation encodings, in which the features for encod ing a case (or a prefix) can be derived by aggregating the values of the attributes of different events (for instance, the values of a numeric attribute across different events of a case may be aggregated into a single feature by using their average). Index-based encoding naturally fits the proposed framework to generate resource-aware features, since these features, by definition, characterize each event in a prefix.

Non-resource-aware features, including the ones derived from the case-level attributes, are generated using the same pre-processing scripts of Teinemaa et al. [50]. A set of 38 resource-aware features are gener ated for each event in a prefix as discussed in the previous section. As classifiers, we consider random forest (RF) and Xgboost (XGB), which have emerged as the best performing classifiers across different event logs in the benchmark published by Teinemaa et al. [50].

We also present an in-depth feature contribution analysis using SHAP (Shapley Additive Explanations) [31]. Based on the coalitional game theory, SHAP is able to calculate the degree to which each feature contributes on average to a prediction. SHAP is a robust explainable Al technique commonly used in particular to interpret black box models, such as deep learning models. Since, in this work, we use RF and XGB, in the experiments, we have used TreeSHAP [30], a fast implementation of the SHAP method fit for tree-based classification models.

The metrics that we use in the feature contribution analysis are shown in Fig. 3. After having ordered all the features in descending order by contribution (calculated using the absolute value of the TreeSHAP’s feature importance), we first calculate the sum of all the feature con tributions and then we consider the top-contributing ones in a given percentile. For instance, in Fig. 3, the 75% percentile of feature contri bution includes the features $F _ { 1 } , F _ { 3 } , F _ { 2 } , F _ { 6 } .$ For a given percentile, in the evaluation we consider (i) the ratio of features belonging to it that are resource-aware (50% in the 75% percentile in the figure) and (ii) the ratio of the cumulative contribution of the resource-aware features belonging to it (in the figure, 33%). The former provides the absolute number of resource-aware features that are contributing to the pre dictions. The latter gives a more detailed insight on the relative magnitude of the contribution of these features.

## 5.1. Datasets and experimental settings

For our experiments, we have considered all the datasets used in the benchmark published by Teinemaa et al. [50] and containing the resource attribute. In particular, we have used the event logs of the Business Process Intelligence Challenge 2011 (BPIC 2011, 1 dataset with 4 different labelings, which we treat as 4 different datasets in this sec tion). the Business Process Intelligence Challenge 2012 (BPIC 2012, 1 dataset with 3 different labelings, which we treat as 3 different datasets) and the Business Process Intelligence Challenge 2015 (BPIC 2015, 5 event logs). Additionally, we have considered the Road Traffic Fines (RTF) event log. All the event logs are publicly available at https://dat a.4tu.nl/. Table 5 reports the descriptive statistics of these logs, briefly describing also the type of process generating the log, the outcome label

![](/api/attachments/HN5TUB7Z/fulltext/images/dbf59c884d7122a53bee142da43ee583661de518f5769ef6a295fa0b7e3a67eb.jpg)  
(a) BPIC 2011\_1 Random Forest

![](/api/attachments/HN5TUB7Z/fulltext/images/0e633d56508f4641eda7b20dea02836dd835f7eb28dba35139bb49153beb98aa.jpg)  
(b) BPIC 2011\_1 XGBoost

![](/api/attachments/HN5TUB7Z/fulltext/images/b70432309a146e024d3d67f2c7cd84f33e559597ecd9f89944b682483b47ad48.jpg)  
(c) BPIC 2011\_2 Random Forest

![](/api/attachments/HN5TUB7Z/fulltext/images/275081b680d8d4ebeba1b99b6bb5e932f4b8d9512cc82198af242f8ddc1c361f.jpg)  
(d) BPIC 2011\_2 XGBoost

![](/api/attachments/HN5TUB7Z/fulltext/images/175e80b99213173851f03f6ec6ab13b5740561b7596f2484127e7f436b2086c6.jpg)  
(e) BPIC 2011\_3 Random Forest

![](/api/attachments/HN5TUB7Z/fulltext/images/3522566ed7379062d445c79d8d7c37da6f276da6a1665a74f8ce0fde95415678.jpg)

![](/api/attachments/HN5TUB7Z/fulltext/images/3f6faf4541656788505dbea8062a8211b8478dbe677fe02c8e9b8efcea178dd7.jpg)  
(g) BPIC 2011\_4 Random Forest

(f) BPIC 2011\_3 XGBoost  
![](/api/attachments/HN5TUB7Z/fulltext/images/b43299e32b6ab36e37d3c2e4f5be8ba4f1b845b2ebdd8c6b2198fbc5526bcba5.jpg)  
(h) BPIC 2011\_4 XGBoost  
Fig. 13. AUC for different prefix lengths for the BPIC 2011 event logs.

to be predicted, and examples of domain-specific information from which non-resource-aware features are derived. Note that some event logs have more than one label (4 for BPIC 2011 and 3 for BPIC 2012). For these, we consider a different log for each label available. For BPIC 2011, 19 cases are missing the 3rd label. Also, the number of events for the BPIC 2011 event logs is different for each label because the cases are cut at the prefix in which the satisfaction/violation of the constraint determining the label becomes known [50]. More details about the la bels used is given later while discussing the results.

Outcome-oriented predictive process monitoring is an instance of the early time-series classification problem, whereby its aim is to predict the correct outcome of a case prefix as soon as possible after its beginning. Therefore, the performance of predictive models is usually evaluated on early (i.e., short) prefixes. In this work, similarly to others in the literature [52,50], we consider prefixes generated using up to the first 20 events for the BPIC event logs and up to the first 10 events for the RTF log.

![](/api/attachments/HN5TUB7Z/fulltext/images/4501d1a5ef9db6531d96fdaad9854d68151c647305297ba1aaf8dcbf2d65639f.jpg)  
(a) BPIC 2011\_1 Random Forest

![](/api/attachments/HN5TUB7Z/fulltext/images/994bf102d219dff03a5d5d8a19f9247595fe9a732c83659de99cba1377390374.jpg)  
(c) BPIC 2011\_2 Random Forest

![](/api/attachments/HN5TUB7Z/fulltext/images/cc256303a24d0cf7ca0900ebe09762384fb6244254cba8d5f8424357d78564a0.jpg)  
(b) BPIC 2011.1 XGBoost

![](/api/attachments/HN5TUB7Z/fulltext/images/a681533491ae52daab39a656e1711530191e3c68072027737f33bdee4549ede7.jpg)  
(d) BPIC 2011\_2 XGBoost

![](/api/attachments/HN5TUB7Z/fulltext/images/28c974cd75e8cfeff81fd55ed1e77abd76168d3c0eb460875d9d6ae692d2ce3d.jpg)  
(e) BPIC 2011\_3 Random Forest

![](/api/attachments/HN5TUB7Z/fulltext/images/60e67837afe67c81f06b190616d51ae00820571e6086fa64937c9cd35927255a.jpg)

![](/api/attachments/HN5TUB7Z/fulltext/images/79a07df5a5d03a6595144752a23a8092d6c4cce689aa94bf0dea4828a72467e9.jpg)  
(f) BPIC 2011\_3 XGBoost

(g) BPIC 2011\_4 Random Forest  
![](/api/attachments/HN5TUB7Z/fulltext/images/cc222f5a376480747900655e253f9a4f99d6803a47a20a6842f258c3e1c2465d.jpg)  
(h) BPIC 2011\_4 XGBoost  
Fig. 14. AUC for different prefix lengths for the BPIC 2011 event logs using the temporally-split batches

Because of the time-series nature of event log data, in the experi ments we consider a temporal split of traces [49]. Given a split time stamp $t _ { s } ,$ the training set contains the traces for which the first event occurs before the split timestamp $( e _ { 1 } . t < t _ { s } )$ . whereas the test set contains the traces for which $e _ { 1 } . t > t _ { s } .$ The split timestamp $t _ { s }$ is chosen by imposing a given ratio between traces in the training/test sets (e.g., 80%/20%) The events e of the traces in the training set with $e \cdot t > t _ { s }$ are then discarded. Such a temporal split is required to ensure that a model is not trained using events that happen in the future with respect to the ones used for testing.

To account for the variability of traces across time and achieve robust results, we also implemented a temporal split-based cross-validation procedure, which is depicted in Fig. 4. An event log is split into nine batches containing roughly the same number of prefixes using the temporal split mechanism described above. Then, we train and test five models (rac -rac ). Each model uses four consecutive batches for training and the next batch for testing (i.e., using a stride of 1). An additional model (rac) is trained and tested using the whole event log, i. $\mathrm { e } _ { \cdot , }$ using 80% of traces for training and 20% for testing after applying the temporal split.

![](/api/attachments/HN5TUB7Z/fulltext/images/53e7fb9a2880ec31ec33ae7e315f3b94b6a3e97f79653b1a964ffd8f3786bb7c.jpg)  
(a) Ratio of the top-contributing resource-aware features

![](/api/attachments/HN5TUB7Z/fulltext/images/0cebc4b34ba40a9c0e0721e5447f1679aaaf5127e0af4c7c6359489118bc90ec.jpg)  
(b) Ratio of the cumulative contribution of the topcontributing resource-aware features

Fig. 15. Ratio of the number and cumulative contribution of the top-contributing resource-aware features in the BPIC 2011 logs.  
![](/api/attachments/HN5TUB7Z/fulltext/images/f6b6a00012b2f06ee64582a5aba93759ae28052e88957864d1aa1b6b8fc3f1d7.jpg)  
(a) RTF Random Forest

![](/api/attachments/HN5TUB7Z/fulltext/images/23451438105de893faa9e0dd6a924f545ebc4a4b253b1c3d074275206df3ebad.jpg)  
(b) RTF XGBoost

Fig. 16. AUC for different prefix lengths for the RTF event log.  
![](/api/attachments/HN5TUB7Z/fulltext/images/9cb62dd0aae15c5b360f758f55f7aec82f6bac1dc32048804597731b32e82553.jpg)  
(a) RTF Random Forest

![](/api/attachments/HN5TUB7Z/fulltext/images/0c78613e48abc9c98aa933ce2990a30835e45bd00a8ce3b85433840d6d592e67.jpg)  
(b) RTF XGBoost  
Fig. 17. AUC for different prefix lengths for the RTF event log using the temporally-split batches

As classifiers, we consider the Python implementation of RF and XGB in the packages scikit-learn and xgboost, respectively. For the hyperparameter configurations, we use the Tree-structured Parzen Estimator (TPE). For RF, TPE has been applied to find the ideal value of the hyperparameter max \_ f eatures in the interval max \_ f eatures ∈ [0, 1]. For XGB, TPE has been applied to find the 5 hyperparameters learning \_ r ate, sub \_ s ample, max \_ d epth, colsample \_ b ytree and min \_ c hild \_ w eight in the intervals learning \_ r ate ∈ [0, 1], subsample ∈ [0.5, 1], max d epth ∈ $\{ x | x \in \mathbb { N } , 4 \leq x \leq 3 0 \}$ , colsample \_ b ytree ∈ [0.5, 1] and min c hild w eight $\in \{ 1 , 2 , 3 , 4 , 5 , 6 \}$ . The values obtained from the hyperparameter optimization are available in the github repository.

## 5.2. Results

The impact of the resource-aware features on the model performance and their contribution to the prediction with respect to the nonresource-aware ones differ for each event log analysed. Therefore, this section includes a separate discussion for each (set of) event log(s).

## 5.2.1. BPIC 2015 event logs

Fig. 5 shows the performance obtained by the models that use (rac)

or do not use (nrac) the resource-aware features for prefixes of different lengths using RF and XGB. The relative performance of the two models varies greatly depending on the event log considered.

In particular, there are two cases worth noticing: the second log, in which rac is consistently worse than nrac, and the third log, in which rac is better than nrac. The reason behind these different behaviors could be due to the fact that the two event logs refer to process execution contexts that are completely different. According to van der Ham [18], who presented an in-depth analysis of the different logs used for the BPIC 2015, the second log of this set refers to a municipality executing the process in a very inefficient way, whereas the third log refers to a mu nicipality executing the same process efficiently. This performance dif ference is also acknowledged by the data shown in Table 6, where we can see that the mean and median case duration of the process in the third log are considerably lower than the ones in the second log. Based on these results, we can conclude that, in this experiment, using the resource-aware features appears to be effective when the process is executed efficiently, whereas it can be detrimental to the predictive performance when the process is executed inefficiently. Specifically, modeling resource experience in this particular context helps building better predictors when resources are working efficiently.

Fig. 6 shows the performance obtained using the models trained on the temporally-split batches. The results show a consistent difference in terms of performance obtained by these models. This may highlight that the impact of the resource-aware features varies over time since also the experience of the resources varies.

Fig. 7 shows the ratio of the top-contributing resource-aware features and the ratio of their cumulative contribution for different percentiles for the rac model. From the plots, we can notice that, for all percentiles, the resource-aware features contribute more to the predictions in the case of third event log in the BPIC 2015 set of logs, which is the one for which the rac model performs better than nrac. In addition, for the second and the third event logs, the contribution magnitudes of the resource-aware features tend to converge to a value of 40% for the 90% percentile. This means that, when almost all the features are considered, the contribution of the resource-aware features to the prediction be comes rather high for these two logs. However, this contribution leads to wrong predictions in the case of the second log, thus decreasing the performance of the model.

Fig. 8 shows the distribution of the contributions of different resource-aware features within the 50% percentile across the di mensions defined in Section 4. Note that most of the features shown in the figure refer to the frequency aspect of the framework, e.g., counting the number of cases or work items in which the resource of the current event has been involved. Since this type of features mainly refer to the experiential learning of the resource behavior, we can conclude that, in this particular context, the experience accumulated by the resources is highly contributing to explain the predictions made by the models.

As a last remark, we have to consider that, for the BPIC 2015 event logs, the label to be predicted is the satisfaction of the following tem poral constraint: the activity “send confirmation receipt” must not be eventually followed by “retrieve missing data” (that is, a confirmation should not be sent to the client if additional information to close a case is still needed). This constraint appears to refer to standard working pro cedures that could easily be learnt by a human resource participating in the process and may not be directly linked to the efficacy and effec tiveness of the resources in executing their job. This aspect may also justify the fluctuating performance achieved with these logs.

## 5.2.2. BPIC 2012 event logs

Fig. 9 shows the performance obtained by rac and nrac for different prefix lengths with RF and XGB. Fig. 10 shows the performance of the models trained using the temporally-split batches.

Two insights emerge clearly: with the BPIC 2012 event logs, the models trained using the resource-aware features are more accurate and, particularly in the case of the accepted and cancelled event logs, there is not much variability in the performance of the models trained using traces belonging to different time batches.

The positive influence of the resource-aware features on the perfor mance of the classifiers, in this case, may be due to the fact that the label to be predicted explicitly captures the outcome of the process, i.e., whether a request will be accepted, cancelled, or declined, and therefore may be directly influenced by the experience of the resources in the process. This conclusion is supported by the fact that according to Adriansyah and Bujis [2], and Bose and van der Aalst [6], who have analyzed these datasets in detail, the resources in this process tend to work as specialists: in particular, some resources are specialized in approving applications, while others are specialized in dealing with more problematic applications. This level of specialization may signal the fact that the experience developed in the workplace by these re sources is important to correctly predict the outcome of a process case.

Fig. 11 shows the analysis of the feature contribution for rac. From the plots, it can be clearly seen that, in this case, the resource-aware features contribute massively to the predictions: in the case of the accepted log, for instance, all the features in the top 10% percentile are resource-aware, while for the cancelled event log the number and cu mulative contribution of the resource-aware features in the top 10% percentile is also very high (50% and 65%, respectively). These results show the importance of the resource-aware features for these logs.

Fig. 12 shows the distribution of different top-contributing resourceaware features within the 10% and 50% percentiles. It can be noticed that, particularly for the accepted and cancelled event logs, the number of tasks executed by a resource is the most frequent type of highly contributing resource-aware features (specifically, the only one appearing in the 10% percentile). This can be seen as an indication that the experiential nature of learning is important in this context: resources get more efficient at what they do as they execute more tasks in the process.

## 5.2.3. BPIC 2011 event logs

Fig. 13 shows the performance obtained by rac and nrac for different prefix lengths with RF and XGB. Fig. 14 shows the performance of the models trained using the temporally-split batches.

In this case, it can be seen that the resource-aware features do not seem to have an influence, either positive or negative, on the perfor mance of the models. This may be due to the fact that the label to be predicted, in this case, is the satisfaction of a temporal constraint, which is not likely to indicate whether a case was executed efficiently or not.

Fig. 15 shows the ratio of the top-contributing resource-aware fea tures and the ratio of their cumulative contribution for different per centiles for rac. These results show that the resource-aware features do not contribute particularly to the prediction (specifically, there are no resource-aware features within the 10% and 25% percentiles). Note that the labels to be predicted in this event log are defined by temporal constraints, e.g., either one of the two activities “tumor marker CA-19.9” and “ca-125 using meia” must be executed in a case, which capture the execution of standard exams dictated by clinical pathways. In this case, human resources should simply interpret correctly the guidelines pre scribing (or not) correctly the execution of the exams. The human resource experience and/or social ties probably bear a limited impact on their behaviour in the process. This confirms that resource-aware fea tures are not important in this particular context. For this reason, we omit the analysis of the distribution of the type of important resourceaware features for these event logs.

## 5.2.4. Road traffic fines event log

Fig. 16 shows the performance obtained by rac and nrac for different prefix lengths with RF and XGB. Fig. 17 shows the performance of the models trained using the temporally-split batches.

Similarly to the case of the BPIC 2011 event logs, also in this case using the resource-aware features proposed neither improves nor de creases substantially the performance of the model. This may be due to the fact that the label to be predicted, i.e., whether a fine is repaid in full or sent for credit collection (see Table 5), concerns the behaviour of the customer of the process (i.e., the motorist supposed to pay the fine), rather than the behavior of the resources handling the fine.

## 5.3. Threats to validity

To conclude the discussion on the experimental results, we briefly discuss here the threats to validity of the presented evaluation. Con cerning the internal validity, a general problem in predictive process monitoring is that considering prefixes as the basis for encoding the feature vectors may introduce irrelevant features and/or spurious cor relations between the feature vectors and the labels that improve the performance of a model without having discovered higher level concepts [24]. The experiments that we present here may also suffer from the same problem, which could be mitigated by using different predictive models, like the ones based on LSTM that use a different type of encoding, or focusing on global predictions, i.e., considering only fully-completed traces for training. In this paper, we also considered only a limited number of combinations of bucketing and encoding methods. This was done to maintain the number of experiments manageable and prioritizing the choice to consider a large set of event logs. As we discussed while presenting the results of each group of event logs, the results may also be influenced greatly by the type of label to be predicted. In some cases, the label represents a process outcome that is most likely linked to the resource experience, while, in other cases, it represents the satisfaction of a constraint, which may not be directly influenced by the resources, or a process outcome driven by the behavior of the customer, rather than by the behavior of the resources involved in the process.

Concerning the construct validity of the proposed resource-aware features, in this work we only consider features that can be extracted from an individual event log, which contains events logged for one specific business process. As such, the proposed resource-aware features are constructed using resource task performance measures in one pro cess as a proxy of resource experience. We acknowledge that an event log is limited both in time and scope and that more reliable features may be extracted by considering data spanning in time beyond an event log time scale and/or data gathered from other contexts in which resources may have gained experience, such as related business processes and onthe-job training. We also believe, however, to have partly mitigated this threat, at least as far as the time scale is concerned, by considering event logs with a large time scale (often spanning years of process execution). Therefore, we believe to have considered, for each process, a sufficient amount of data to get an indication of the effect of the proposed resource-aware features on the performance of a predictive model.

Concerning the external validity, for some of the event logs that we considered (BPIC 2011 and RTF) there is no domain-specific information available to provide an in-depth analysis of the experimental results More generally, the experimental results show that it is not possible to draw general conclusions about the role and the impact of the resourceaware features in predictive process monitoring, and that each process execution context has to be considered independently in order to assess the effectiveness of the proposed framework.

## 6. Conclusions

This article proposes a framework for extracting features from event logs capturing the notion of resource experience for the purpose of training models for outcome-oriented predictive process monitoring. The proposed framework defines four dimensions of resource-aware features, i.e., Recency, Context, Target, and Aspect, which are derived from an analysis of the management theories pertaining to resource experience.

The experimental evaluation showed that, in some cases, the pro posed features can help improving the performance of the outcomeoriented predictive models. However, the effectiveness of the pro posed features strongly depends on the process execution context and the results differ based on the event logs considered. In particular, we found that models trained using resource-aware features are more likely to show higher performance in contexts where the process is executed efficiently or when the label to be predicted captures an outcome that clearly depends on the efficiency of the resources in executing their tasks. In other words, the proposed features appear to be effective when the outcome label measures an actual business process outcome [36] related with process efficiency, effectiveness or flexibility improvements.

The research presented in this paper can be extended along several lines. First, the experimental evaluation focused on predicting case outcomes. However, resource experience features can also be applied to other predictive monitoring use cases, such as predicting the remaining time of a case. Second, the proposed framework is designed to be generic, i.e., independent of a specific application domain. However, the results presented in this paper have shown that the application domain clearly influences the effectiveness of the proposed framework. There fore, further refinements should be conceived for specific domains like, for example, the manufacturing domain, where the frequent execution of the same task by a resource may lead to fatigue effects, which may cancel out the benefits of task familiarity and recency. Moreover, since resources may be involved in several processes within the same domain, resource-aware features could also be extended to capture the fact that experience gained in one process may be reused in a different one. This links to the more general field of cross-process research in process mining, which is emerging only recently in the literature [38]. Finally, the approach presented in this article may be used as a starting point to design experiments to validate a range of disciplines and theories from a managerial perspective. For instance, comparing in different contexts the predictive power of features capturing the repetition of the same task and the execution of different tasks in a process could substantiate managerial findings about the impact on performance of specialised v. general skills.

## Acknowledgment

This research was partly funded by the Estonian Research Council (grant PRG887) and by the 0000 Project Fund (Project Number 1.210079.01) of UNIST (Ulsan National Institute of Science & Technology).

## References

[1] W.M.P. van der Aalst, Process Mining: Data Science in Action, Springer, 2016

[2] A. Adriansyah, J.C. Buijs, Mining process performance from event logs, in: International Conference on Business Process Management, Springer, 2012, pp. 217–218.

[3] M. Arias, E. Rojas, J. Munoz-Gama, M. Sepúlveda, A framework for recommending resource allocation based on process mining, in: International Conference on Business Process Management, Springer, 2016, pp. 458–470.

[4] S. Balzert, P. Fettke, P. Loos, A framework for reflective business proces IEEE, 2012, pp. 3642–3651.

[5] R. Bidar, A. ter Hofstede, R. Sindhgatta, C. Ouyang, Preference-based resource and task allocation in business process automation, in: OTM Confederated International Conferences “On the Move to Meaningful Internet Systems, Springer, 2019, pp. 404–421.

[6] R.J.C. Bose, W.M. van der Aalst, Process mining applied to the BPI challenge 2012: Business Process Management, Springer, 2012, pp. 221–222.

[7] D.J. Brass, J. Galaskiewicz, H.R. Greve, W. Tsai, Taking stock of networks and organizations: a multilevel perspective, Acad. Manag. J. 47 (2004) 795–817.

[8] J. Brunk. M. Stierle. L. Papke, K. Revoredo. M. Matzner. J. Becker. Cause ys, effect in context-sensitive prediction of business process instances. Inf, Syst. 95 (2021) 101635.

[9] M. Ceci. P.F. Lanotte. F. Fumarola. D.P. Cavallo. D. Malerba. Completion time and next activity prediction of processes using sequential pattern mining. in: International Conference on Discovery Science, Springer, 2014, pp. 49–61.

[10] W.M. Cohen, D.A. Levinthal, Absorptive capacity: a new perspective on learning and innovation, Adm. Sci. Q. 35 (1990) 128–152.

[11] R. Conforti, M. de Leoni, M. La Rosa, W.M. van der Aalst, A.H. ter Hofstede, A recommendation system for predicting risks across multiple business process instances, Decis. Support Syst. 69 (2015) 1–19.

[12] R. Cross, J.N. Cummings, Tie and network correlates of individual performance in knowledge-intensive work, Acad. Manag. J. 47 (2004) 928–937.

[13] M. De Leoni, W.M. van der Aalst, M. Dees, A general process mining framework for correlating, predicting and clustering dynamic behavior based on event logs, Inf. Syst. 56 (2016) 235–257.

[14] C. Di Francescomarino, M. Dumas, F.M. Maggi, I. Teinemaa, Clustering-based predictive process monitoring. JEEE Trans. Sery. Comput. 12 (2016) 896–909.

[15] A. Donabedian, The quality of care: how can it be assessed? JAMA 260 (1988) 1743-1748.

[16] J. Erasmus, I. Vanderfeesten, K. Traganos, X. Jie-A-Looi, A. Kleingeld, P. Grefen, A method to enable ability-based human resource allocation in business process management systems, in: IFIP Working Conference on the Practice of Enterprise Modeling, Springer, 2018, pp. 37–52.

[17] D. Fahland, V. Denisov, W. van der Aalst, Inferring Unobserved Events in Systems With Shared Resources and Queues, 2021, arXiv:2103.00167.

[18] U. van der Ham, Benchmarking of five dutch municipalities with process mining techniques reveals opportunities for improvement, Bus. Process Intell. Chall. 2015 (2015).

[19] N. Harane, S. Rathi, Comprehensive survey on deep learning approaches in predictive business process monitoring. Modern Approaches in Machine Learning and Cognitive Science: A Walkthrough, Springer, 2020, pp. 115–128.

[20] J.A. H¨ausser, S. Schulz-Hardt, T. Schultze, A. Tomaschek, A. Mojzisch, Experimental evidence for the effects of task repetitiveness on mental strain and objective work performance, J. Organ. Behav. 35 (2014) 705–721.

[21] M.Y. Jaber, S. Sikstrom, ¨ A numerical comparison of three potential learning and forgetting models, Int. J. Prod. Econ. 92 (2004) 281–294.

[22] J. Karimi, T.M. Somers, A. Bhattacherjee, The role of information systems resources in erp capability building and business process outcomes, J. Manag. Inf. Syst. 24 (2007) 221–260.

[23] E.L. Klijn, D. Fahland, Identifying and reducing errors in remaining time prediction due to inter-case dynamics, in: 2020 2nd International Conference on Process Mining (ICPM), IEEE, 2020, pp. 25–32.

[24] C. Klinkmüller, N.R. van Beest, I. Weber, Towards reliable predictive process monitoring, in: International Conference on Advanced Information Systems Engineering, Springer, 2018, pp. 163–181.

[25] D.A. Kolb, Experiential Learning: Experience as the Source of Learning and Development, FT Press, 2014.

[26] P. Korytkowski, Competences-based performance model of multi-skilled workers with learning and forgetting, Expert Syst. Appl. 77 (2017) 226–235.

[27] W. Kratsch, J. Manderscheid, M. Roglinger, ¨ J. Seyfried, Machine learning in business process monitoring: a comparison of deep learning and classical approaches used for outcome prediction, Bus. Inf. Syst. Eng. (2020) 1–16.

[28] A. Leontjeva, R. Conforti, C. Di Francescomarino, M. Dumas, F.M. Maggi, Complex symbolic sequence encodings for predictive monitoring of business processes, in: International Conference on Business Process Management, Springer, 2016, pp. 297–313.

[29] M.B. Lieberman, The learning curve, diffusion, and competitive strategy, Strateg. Manag. J. 8 (1987) 441–452.

[30] S.M. Lundberg, G. Erion, H. Chen, A. DeGrave, J.M. Prutkin, B. Nair, R. Katz, J. Himmelfarb, N. Bansal, S.I. Lee, From local explanations to global understanding with explainable AI for trees, Nat, Mach, Intell. 2 (2020) 56–67.

[31] S.M. Lundberg, S.I. Lee, A unified approach to interpreting model predictions, Adv. Neural Inf. Process. Syst. 30 (2017) 4765–4774.

[32] F.M. Maggi, C. Di Francescomarino, M. Dumas, C. Ghidini, Predictive monitoring of business processes, in: International Conference on Advanced Information Systems Engineering, Springer, 2014, pp. 457–472.

[33] B. Małachowski, P. Korytkowski, Competence-based performance model of multiskilled workers, Comput. Ind. Eng. 91 (2016) 165–177.

[34] A.E. M´arquez-Chamorro, M. Resinas, A. Ruiz-Cort´es, Predictive monitoring of business processes: a survey, IEEE Trans. Serv. Comput. 11 (2017) 962–977.

[35] A.E. Marquez-Chamorro, ´ M. Resinas, A. Ruiz-Cort´es, M. Toro, Run-time prediction of business process indicators using evolutionary decision rules, Expert Syst. Appl. 87 (2017) 1–14.

[36] J.G. Mooney, V. Gurbaxani, K.L. Kraemer, A process oriented framework for assessing the business value of information technology. ACM SIGMIS Database DATABASE Adv. Inf, Syst, 27 (1996) 68–81

[37] J. Nakatumba, W.M. van der Aalst, Analyzing resource behavior using process mining, in: International Conference on Business Process Management, Springer, 2009, pp. 69–80.

[38] D.A. Neu. J. Lahann. P. Fettke. A systematic literature review on state-of-the-art deep learning methods for process prediction, Artif. Intell. Rev. (2021) 1–27.

[39] G. Park, M. Song, Predicting performances in business processes using deep neural

[40] J.H. Park, H.J. Suh, H.D. Yang, Perceived absorptive capacity of individual users in performance of enterprise resource planning (ERP) usage: the case for korean firms, Inf, Manag, 44 (2007) 300–312.

[41] A. Pika, M. Leyer, M.T. Wynn, C.J. Fidge, A.H.T. Hofstede, W.M.V.D. Aalst, Mining resource profiles from event logs, ACM Trans. Manag. Inf. Sys. (TMIS) 8 (2017) 1–30.

[42] A. Pika, M.T. Wynn, Workforce upskilling: a history-based approach for recommending unfamiliar process activities. in: International Conference on Advanced Information Systems Engineering, Springer, 2020, pp. 334–349.

[43] A. Senderovich, C. Di Francescomarino, C. Ghidini, K. Jorbina, F.M. Maggi, Intra and inter-case features in predictive process monitoring: a tale of two dimensions in: International Conference on Business Process Management, Springer, 2017, pp. 306–323.

[44] A. Senderovich, C. Di Francescomarino, F.M. Maggi, From knowledge-driven to data-driven inter-case feature encoding in predictive process monitoring, Inf. Syst. 84 (2019) 255–264

[45] A. Senderovich, M. Weidlich, A. Gal, A. Mandelbaum, Mining resource scheduling protocols, in: International Conference on Business Process Management, Springer, 2014, pp. 200–216.

[46] B.A. Tama, M. Comuzzi, An empirical comparison of classification techniques fo next event prediction using business process event logs, Expert Syst. Appl. 129 (2019) 233–245

[47] N. Tax, I. Verenich, M. La Rosa, M. Dumas, Predictive business process monitoring with LSTM neural networks, in: International Conference on Advanced Information Systems Engineering, Springer, 2017, pp. 477–492.

[48] F. Taymouri, M. La Rosa, S. Erfani, Z.D. Bozorgi, I. Verenich, Predictive business process monitoring via generative adversarial nets: the case of next event prediction, in: International Conference on Business Process Management, Springer, 2020, pp. 237–256.

[49] I. Teinemaa, M. Dumas, A. Leontjeva, F.M. Maggi, Temporal stability in predictive process monitoring, Data Min. Knowl. Discov. 32 (2018) 1306–1338.

[50] I. Teinemaa, M. Dumas, M.L. Rosa, F.M. Maggi, Outcome-oriented predictive process monitoring: review and benchmark, ACM Trans. Knowl. Discov. Data (TKDD) 13 (2019) 1–57.

[51] C. Terwiesch, R.E. Bohn, Learning and process improvement during production ramp-up, Int. J. Prod. Econ. 70 (2001) 1–19.

[52] I. Verenich, M. Dumas, M. La Rosa, F.M. Maggi, C. Di Francescomarino, Complex symbolic sequence clustering and multiple classifiers for predictive process monitoring, in: International Conference on Business Process Management, Springer, 2016, pp. 218–229.

[53] I. Verenich, M. Dumas, M.L. Rosa, F.M. Maggi, I. Teinemaa, Survey and crossbenchmark comparison of remaining time prediction methods in business process monitoring, ACM Trans. Intell. Syst. Technol. 10 (2019), 34:1–34:34.

[54] B. Wieder, P. Booth, Z.P. Matolcsy, M.L. Ossimitz, The impact of erp systems on firm and business process performance, J. Enterp. Inf, Manag, (2006)

[55] W. Zhao, L. Yang, H. Liu, R. Wu, The optimization of resource allocation based on process mining, in: International Conference on Intelligent Computing, Springer, 2015. pp. 341–353.

Jongchan Kim is Ph.D. Candidate at the Department of Industrial Engineering, Ulsan National Institute of Science and Technology (UNIST), Ulsan, South Korea. His research interests include artificial intelligence for process mining, machine learning applications and quality of predictions in predictive monitoring

Marco Comuzzi is Associate Professor at the Department of Industrial Engineering, Ulsan National Institute of Science and Technology (UNIST), Ulsan, South Korea. He holds a Ph. D. in Information Technology from Politecnico di Milano obtained in 2007. His research interests include business process management, data science and blockchain.

Marlon Dumas is Professor of Information Systems and University of Tartu, Estonia and Co-Founder at Apromore – a company dedicated to commercializing open-source process mining solutions. His research focuses on process mining, process simulation. and Al methods for automated process improvement. He is co-author of the textbook “Funda mentals of Business Process Management” (Springer, 2013).

Fabrizio Maria Maggi is Associate Professor at the Research Centre for Knowledge and Data (KRDB) – Faculty of Computer Science – Free University of Bozen-Bolzano. His research interest has focused in the last years on the application of Artificial Intelligence to Business Process Management. He is one of the promoters of the Rule Mining initiative (rulemining.org). He is committee member of the journal track of the European Confer ence on Machine Learning and Principles and Practice of Knowledge Discovery in Data bases (ECMLPKDD).

Irene Teinemaa is a machine learning scientist at Booking.com. Her research interests are in the fields of causal inference, recommender systems, predictive analytics, and other applied machine learning methods. She received a PhD in Computer Science from Uni versity of Tartu in 2019 for her work working on predictive and prescriptive monitoring of business processes.
