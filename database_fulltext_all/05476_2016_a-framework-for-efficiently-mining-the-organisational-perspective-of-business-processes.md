---
otero_id: 5476
otero_key: "ZGQEF2Z9"
title: "A framework for efficiently mining the organisational perspective of business processes"
authors: "Stefan Schönig; Cristina Cabanillas; Stefan Jablonski; Jan Mendling"
year: "2016"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2016.06.012"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A framework for eficiently mining the organisational perspective of business processes<sup>-</sup>

Stefan Schönig<sup>a,</sup>\*, Cristina Cabanillas<sup>b</sup>, Stefan Jablonski<sup>a</sup>, Jan Mendling<sup>b</sup>

<sup>a</sup>University of Bayreuth, Germany <sup>b</sup>Vienna University of Economics and Business, Austria

## A R T I C L E I N F O

Article history: Received 17 August 2015 Received in revised form 10 June 2016 Accepted 15 June 2016 Available online xxxx

Keywords: Business process management Declarative process mining Event log analysis Organisational perspective Resource perspective

## A B S T R A C T

Process mining aims at discovering processes by extracting knowledge from event logs. Such knowledge may refer to different business process perspectives. The organisational perspective deals, among other things, with the assignment of human resources to process activities. Information about the resources that are involved in process activities can be mined from event logs in order to discover resource assignment conditions, which is valuable for process analysis and redesign. Prior process mining approaches in this context present one of the following issues: (i) they are limited to discovering a restricted set of resource assignment conditions; (ii) they do not aim at providing eficient solutions; or (iii) the discovered process models are dificult to read due to the number of assignment conditions included.

In this paper we address these problems and develop an eficient and effective process mining framework that provides extensive support for the discovery of patterns related to resource assignment. The framework is validated in terms of performance and applicability.

© 2016 Elsevier B.V. All rights reserved

## 1. Introduction

Business process management (BPM) is a well accepted method for structuring the activities carried out in an organisation, analysing them for eficiency and effectiveness, and identifying potential for improvement [1]. Processes are not always explicitly defined when the process models are designed. Actual process executions may constitute a valuable input for improving process design. Process mining provides methods for automatic process analysis, among others for discovering processes by extracting knowledge from event logs in form of a process model. Various algorithms are available to discover models capturing the control-flow of a process, related to the behavioural perspective of the process [2, 3]. For perspectives like the organisational perspective, which manages the involvement of human resources in processes, only partial solutions for mining have been developed despite the importance of resource information not only for performance but also for compliance analysis [4–7].

The need to better support the organisational perspective was evidenced by previous approaches that mined this perspective [8–13]. Prior work in this area focused on discovering specific aspects of the organisational perspective such as role models, separation of duty or social networks. However, comprehensive and integrated support for the well-established workflow resource patterns, and specifically in this context for the so-called creation patterns [14], was missing. Furthermore, the close interplay between the organisational and behavioural perspectives was disregarded [15].

In Ref. [16] we addressed these gaps by developing a declarative process mining approach for the organisational perspective, which supports all the creation patterns as well as what we called crossorganisational patterns, which discover how the involvement of resources influences the control-flow of the process.

The research reported in this paper extends our prior work towards an eficient and effective mining framework. As illustrated in Fig. 1, the framework is divided into an event log preprocessing phase, a phase for integrated resource mining including cross-perspective patterns, and a model post-processing phase. We evaluate our approach with an implementation of the three phases; with simulation experiments for measuring performance; and with the application of the approach on a real-life event log for checking its effectiveness.

This research extends our previous work [16] as follows: (i) the developed pre-processing method increases the eficiency of the

S. Schönig, et al. / Decision Support Systems xxx (2016) xxx–xxx

![](/api/attachments/ZGQEF2Z9/fulltext/images/c3483ceaecac578c7e9862d799322b4e2cd4f9fddfd9012f277b2d941d981337.jpg)  
Fig. 1. Framework for discovering resource-aware, declarative process models.

approach; (ii) the developed post-processing techniques increase the understandability of the results; (iii) a prototype of the entire framework has been implemented using Drools; and (iv) the approach has been extensively validated. In addition, the mining approach is explained in more detail. With our work, we complement research on process mining with an extensive support of the organisational perspective.

The remainder of this paper is structured as follows: Section 2 introduces background information. Section 3 describes our process mining approach. Sections 4 and 5 describe the event log preprocessing and postprocessing phases of the framework, respectively. Section 6 explains the evaluations performed. Section 7 describes the related work and Section 8 concludes the paper.

## 2. Background

In the following we introduce the concepts upon which our approach has been developed.

## 2.1. Organisational and cross-perspective patterns in processes

The well-known workflow resource patterns [14] capture the various ways in which resources are represented and utilised in business processes. Of specific interest to our research are the creation patterns since they describe different ways in which resources can be assigned to activities. These patterns, which will be referred to as organisational patterns from now on, include: Direct Distribution, or the ability to specify at design time the identity of the resource that will execute a task. Role-Based Distribution, or the ability to specify at design time that a task can only be executed by resources that have a given role. Organisational Distribution, or the ability to offer or allocate activity instances to resources based on their organisational position and their organisational relationship with other resources. Separation of Duties, or the ability to specify that two tasks must be allocated to different resources in a given process instance. Case Handling, or the ability to allocate all the activity instances within a given process instance to the same resource. Retain Familiar (a.k.a. Binding of Duties), or the ability to allocate an activity instance within a given process instance to the same resource that performed a preceding activity instance. Capability-Based Distribution, or the ability to offer or allocate instances of an activity to resources based on their specific capabilities. Deferred Distribution, or the ability to defer the specification of the identity of the resource that will execute a task until run time. History-Based Distribution, or the ability to offer or allocate activity instances to resources based on their execution history. Note that the creation patterns Authorisation and Automatic Execution are not in the list because they are not directly related to resource assignment.

It has been identified that process control-flow is intertwined with dependencies upon resource characteristics [15]. For instance, sometimes an activity must be executed eventually before another one for specific resources but not for others. As an example, resources with a certain role (e.g., trainees) must always perform a certain activity (e.g., double-check result) before they can continue with the following activity, but this might not be required for other roles (e.g., supervisors). We call this pattern Role-Based Sequence.

A specific collection of such cross-perspective patterns capturing these situations has not been defined. Nonetheless, in general, they can be defined by combining the aforementioned organisational patterns with the control-flow patterns described in Ref. [17]. The Resource-Based Response pattern, e.g., describes that for a special resource a certain activity has to follow eventually on another activity.

The organisational and cross-perspective patterns constitute the set of patterns to be discovered by our framework.<sup>1</sup>

## 2.2. Event logs for mining the organisational perspective

Our mining approach takes as input (i) an event log, i.e., a machine-recorded file that reports on the execution of tasks during the enactment of the instances of a given process; and (ii) organisational background knowledge, i.e., prior knowledge about the roles, capabilities and the membership of resources to organisational units, among others. In an event log, every process instance corresponds to a sequence (trace) of recorded entries, namely, events. We require that events contain an explicit reference to the enacted task and to the operating resource. Both conditions are commonly respected in real-world event logs [2]. For instance, the following excerpt of a business trip process event log encoded in the XES logging format [18] shows the recorded information of the start event of activity Apply for trip performed by resource ST.

```xml
<event>
    <string key="org:resource" value="ST"/>
    <date key="time:timestamp" value="2013-08-06T14:58:00.000+01:00"/>
    <string key="concept:name" value="Apply for trip"/>
    <string key="lifecycle:transition" value="start"/>
</event>
```

## 2.3. Representing the output of the mining

Since our aim is to discover the patterns explained in Section 2.1, the modelling language to represent the discovered processes must offer the possibility to define (i) expressive organisational patterns

S. Schönig, et al. / Decision Support Systems xxx (2016) xxx–xxx

![](/api/attachments/ZGQEF2Z9/fulltext/images/7f2b1804e60b79effbd3083b21a780f8df97f44dca69e03269808b818a9d0f7e.jpg)  
Fig. 2. Organisational meta model and example organisational model.

and (ii) cross-perspective patterns. Two different representational paradigms for process models can be distinguished: procedural models describe which activities can be executed next in a process, and declarative models define by means of rules the execution constraints that the process has to satisfy [17]. Current procedural languages like Business Process Model and Notation (BPMN) [19] put a strong emphasis on control-flow and assume other perspectives to be specified separately. Cross-perspective patterns cannot be readily modelled. Declarative process modelling does not limit the number of perspectives involved in the constraints defined. However, a central shortcoming of existing languages like Declare [17] is that they are not provided with the capability to directly define the connection between the process behaviour and other perspectives. We will use the Declarative Process Intermediate Language (DPIL) [20] for modelling the output of the mining because it supports multiple perspectives including the behavioural and organisational perspectives, as well as the interplay between them. DPIL is expressive enough to cover the workflow patterns [20]. Nonetheless, the concepts of our approach are generic such that other declarative languages, such as Sciff [21] or LTL-based formalisms [22], could also be used as long as they provided support for the modelling of our target patterns.

In order to express organisational information, DPIL builds upon a generic organisational meta model [23] that is depicted in Fig. 2a. It comprises the following elements: Identity represents agents that can be directly assigned to activities, i.e., both human and non-human resources. Group represents abstract agents that may describe several identities as a whole, e.g., roles or groups. Relation represents the different relations (RelationType) that may exist between these elements. It is well suited for defining, e.g., that an identity has a specific role, that a person is the boss of another person, or that a person belongs to a certain department. In this context, relations are generally irreflexive. A relation is irreflexive if an identity cannot be in relation to itself. The supervisor relation, e.g., is irreflexive, since a person cannot be their own supervisor. In addition, some relations may be transitive. A relation is transitive if whenever an individual $i _ { 1 }$ is related to another individual $i _ { 2 }$ with that relation, and $i _ { 2 }$ is in turn related to a third individua $i _ { 3 }$ with the same relation, then $i _ { 1 }$ is also related to $i _ { 3 }$ . For instance, the supervisor and delegate relations are typically transitive because organisations are usually hierarchically structured. Fig. 2b illustrates an exemplary organisational model of a university research group, composed of two roles (Professor, Student) assigned to three people (SJ, ST, BR) and two relations between them indicating who is supervised by whom.

DPIL provides a textual notation based on the use of macros to define reusable rules. For instance, the sequence(a, b) macro states that the existence of a start event of task b implies the previous occurrence of a complete event of task a; and the role(a, r) macro states that an activity a is assigned to a role r. Fig. 3 shows an example of a process for trip management modelled with DPIL. It specifies that it is mandatory to approve a business trip before flight tickets can be booked. Moreover, it is necessary that the approval be carried out by a resource with the role Professor.

## 3. Mining the organisational perspective

In this section we describe our approach to discover organisational and cross-perspective patterns. First, we describe how rule candidates are generated and checked. Then, we classify them according to support, confidence and interest factor values. Finally, we present a catalogue of rule templates that covers the target expressiveness (cf. Section 2.1).

## 3.1. Generation and checking of rule candidates

Declarative process modelling languages like DPIL are based on so-called rule templates. A rule template captures frequently needed relations and defines a particular type of rules. Templates have formal semantics specified through logical formulae and are equipped either with user-friendly graphical representations (e.g., in Declare) or macros in textual languages (e.g., in DPIL). Unlike concrete rules, a rule template consists of placeholders, i.e., typed variables. A rule template is instantiated by providing concrete values for these placeholders. For instance, the model described in Section 2 makes use of two rule templates represented by the macros sequence $( T _ { 1 } , T _ { 2 } )$ and role (T, G). These templates comprise placeholders of type Task T as well as Group $G .$ In all well-known declarative process mining approaches, rule templates are used for querying the provided event log to find solutions for the placeholders. A solution is any combination of concrete values for the placeholders that yields a concrete rule that is satisfied in the event log. First, all possible rules need to be constructed by instantiating the given set of rule templates with all possible combinations of occurring process elements provided in the event log. For example, the sequence template consists of two placeholders of type Task. Assuming that |T| different tasks occur in the event log, $| T | ^ { 2 }$ rule candidates are generated.

Let |H| be the number of different rule templates to be checked and |P (i)| the number of different elements in the event log of $\mathbf { a }$ certain parameter type $P _ { j } ( i )$ contained in rule template $\theta _ { i } .$ Let k(i) be the number of placeholders in $\theta _ { i } .$ The number of generated rule candidates $| R _ { C a n d } | \mathrm { { \ i s \ } } | P _ { 1 } ( 1 ) | \cdot | P _ { 2 } ( 1 ) | \cdot \ldots \cdot | P _ { k ( 1 ) } ( 1 ) | +$ $| P _ { 1 } ( 2 ) | \cdot | P _ { 2 } ( 2 ) | \cdot \ldots \cdot | P _ { k ( 2 ) } ( 2 ) | + \ldots + | P _ { 1 } ( i ) | \cdot | P _ { 2 } ( i ) | \cdot \ldots \cdot | P _ { k ( i ) } ( i ) |$ and therefore,

![](/api/attachments/ZGQEF2Z9/fulltext/images/c8e8c4c4d2c3ce47b469401eb2b7285b8d22625830ef485c3ea94e47637cf49a.jpg)

$$
| R _ {C a n d} | = \sum_ {i = 1} ^ {| \Theta |} \left(\prod_ {j = 1} ^ {k (i)} | P _ {j} (i) |\right)\tag{1}
$$

The resulting candidates are subsequently checked w.r.t. the log. In many cases a rule candidate can be trivially valid. Consider the candidate direc $\mathsf { t } ( t _ { 1 } , i _ { 1 } ) ,$ , i.e., $s t a r t ( o f t _ { 1 } )$ implies start(of t by i ), which holds when task $t _ { 1 }$ is performed by identity $i _ { 1 } ,$ and the event log shown in Table 1. The notation used encodes the start and complete events of a specific task t performed by an identity i with s(t, i) and $\mathsf { c } ( t , i ) ,$ respectively. The given events are ordered temporally so that timestamps are not encoded explicitly. In the first trace the rule holds trivially because $t _ { 1 }$ never happens. Using the terminology of Ref. [24], we say that the rule is vacuously satisfied. It is necessary to discriminate between traces in which a rule is trivially true and traces in which the rule is non-vacuously satisfied. Only the latter are considered interesting [25]. For first order logic rules that depict implications of the form $A \  \ B ,$ , trivially and non-vacuously valid rules can be discriminated by additionally checking the condition A of the rule separately. Table 1 shows the results of checking the nonvacuous satisfaction of the direc $\mathrm { \Delta } [ ( t _ { 1 } , i _ { 1 } )$ rule as well as its condition for each trace of the example log. In the first trace the rule is not (non-vacuously) satisfied because $t _ { 1 }$ is never started, i.e., the condition is false. The rule holds non-vacuously in the traces two to four. It is violated in trace five.

## 3.2. Metrics to classify rule candidates

Checking rule candidates as described above provides for every candidate the number of instances, i.e., the traces in the event log where it non-vacuously holds. Based on these values it is possible to classify rules and to separate non-valid from valid ones. Maggi et al. [24] adopted different metrics, specifically support (supp), confidence (conf) and interest factor (int) proposed by association rule mining for evaluating the relevance of rule candidates. Let |V| be number of traces in an event log V. Let $| \sigma _ { n \nu } ( r ) |$ be the number of traces in which a rule $r : A  B$ is non-vacuously satisfied. The support supp(r), confidence conf(r) and int(r) values of a rule r are defined as:

$$
\operatorname{supp} (r) := \frac {\left| \sigma_ {n v} (r) \right|}{\left| \Phi \right|}, \operatorname{conf} (r) := \frac {\operatorname{supp} (r)}{\operatorname{supp} (A)}, \operatorname{int} (r) := \frac {\operatorname{supp} (r)}{\operatorname{supp} (A) \cdot \operatorname{supp} (B)}\tag{2}
$$

Considering again the event log of Table 1 and the direc $\left( t _ { 1 } , i _ { 1 } \right)$ rule. Its support evaluates to $s u p p ( r ) ~ = ~ 0 . 6$ , its confidence to $c o n f ( r ) = 0 . 7 5$ and its interest factor to $i n t ( r ) = 1 . 2 5$ . We make use of the confidence value to classify a rule candidate r as a valid rule (i.e., satisfied in almost all traces) or a non-valid rule (i.e., violated in most of the recorded traces). Therefore, the threshold minConf is introduced to classify rule candidates. Candidates r with conf $r ) >$ minConf are classified as valid. All rule candidates r with con $\mathrm { \Delta } ( r ) \mathrm { \Omega } <$ minConf are non-valid rules and are not part of the resulting process model. Note that in the case of rules that do not depict implications, the condition is satisfied in every trace; therefore, $s u p p ( A ) = 1$ and $c o n f ( r ) \ = \ s u p p ( r )$ . Using the confidence values of rule candidates it is directly possible to generate a DPIL process model reflecting organisational and cross-perspective patterns.

Event log and satisfaction of an example rule and its condition

<table><tr><td>Trace</td><td>start(of  $t_1$ )</td><td>direct( $t_1,i_1$ )</td></tr><tr><td> $\{ \mathbf{s}(t_2,i_1), \mathbf{c}(t_2,i_2), \mathbf{s}(t_3,i_1), \mathbf{c}(t_3,i_1) \}$ </td><td>False</td><td>False</td></tr><tr><td> $\{ \mathbf{s}(t_1,i_1), \mathbf{c}(t_1,i_1), \mathbf{s}(t_2,i_2), \mathbf{c}(t_2,i_2), \mathbf{s}(t_3,i_1), \mathbf{c}(t_3,i_1) \}$ </td><td>True</td><td>True</td></tr><tr><td> $\{ \mathbf{s}(t_1,i_1), \mathbf{c}(t_1,i_1), \mathbf{s}(t_3,i_3), \mathbf{c}(t_3,i_3), \mathbf{s}(t_2,i_2), \mathbf{c}(t_2,i_2) \}$ </td><td>True</td><td>True</td></tr><tr><td> $\{ \mathbf{s}(t_1,i_1), \mathbf{c}(t_1,i_1), \mathbf{s}(t_3,i_3), \mathbf{c}(t_3,i_3), \mathbf{s}(t_2,i_2), \mathbf{c}(t_2,i_2) \}$ </td><td>True</td><td>True</td></tr></table>

## 3.3. Rule templates for mining the organisational perspective

Since DPIL builds upon a flexible organisational meta model (cf. Section $2 . 3 ) ,$ it is possible to define rule templates that describe many aspects of the organisation. By instantiating these rule templates with all possible parameter combinations of defined resources, groups and relation types, it is possible to generate rule candidates that focus on the organisational perspective of the process to be analysed. These candidates can then be checked under consideration of the event log and the organisational model.

In the following we define rule templates and their macros for our target set of patterns. First of all, we distinguish between templates for organisational patterns and templates for cross-perspective patterns.

The former are, in turn, divided into two groups based on the types and number of parameters: rule templates related to a single task and rule templates related to more than one task. We provide representative examples for each group of rule templates that cover frequently needed organisational information. Note that besides the templates described next, further templates could be defined individually to cover the analyst’s needs.

## 3.3.1. Rule templates for the assignment of resources to a single task

This group includes rule templates that define organisational patterns referred to one process activity. The Direct Distribution pattern can be extracted with a direct(T, I) template. Given the free variables T and I and an event log with |T| distinct tasks and |I| distinct resources, there are $| T | \cdot | I |$ candidates to be checked.

## direct(T,I) iff start(of T) implies start(of T by I)

The Role-Based Distribution pattern can be extracted with a role $( T , G )$ template. Here, rule candidates for every task and group combination are generated, i.e., $| T | \cdot | G |$ rule candidates need to be checked.

$$
\begin{array}{l} \text {role(T,G) iff start(of T by :p) implies} \\ \text {relation(subject p predicate hasRole object G)} \end{array}
$$

The Capability-Based Distribution pattern can be extracted with a capability(T, RT, G) template. A capability is represented by a relation of an individual to a group, e.g., i hasDegree ComputerScience. According to the placeholders, $| T | \cdot | R T | \cdot | G |$ candidates are generated.

capability(T, RT, G) iff

start(of T by :p) implies relation(subject p predicate RT object G)

The assignment of resources based on organisational positions of individuals, described by the Organisation-Based Distribution pattern, can be extracted with an orgDistSingle(T, RT, G) template. Here, $| T | \cdot | R T | \cdot | G |$ rules must be checked.

orgDistSingle(T, RT, G) iff

start(of T by :p) implies relation(subject p predicate RT object G

## 3.3.2. Rule templates for the assignment of resources to several tasks

This group includes rule templates that define organisational patterns referred to several tasks. The Separation of Duties pattern can be extracted with a separate $T _ { 1 } , T _ { 2 } )$ template. For this template, $| T | ^ { 2 }$ candidates need to be checked

separate(T1,T2) iff start(of T1 by :p) and start(of T2) implies start(of T2 by not p)

Please cite this article as: S. Schönig, et al., A framework for eficiently mining the organisational perspective of business processes, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.06.012

The Retain Familiar pattern can be extracted with a binding $\left[ T _ { 1 } , T _ { 2 } \right)$ template. Similarly to the previous case, $| T | ^ { 2 }$ candidates need to be checked.

binding(T1,T2) iff start(of T1 by :p) and start(of T2) implies

start(of T2 by p)

The Case Handling pattern can be extracted with a caseHandling template. Here, |T| candidates have to be checked.

caseHandling iff forall(task T start(of T) implies start(of T by :p))

Resources can also be assigned to tasks according to their organisational relation with the performers of other process activities, e.g., an approval task might be assigned to people that can supervise the work done by the performers of a previous task. This is covered by the Organisation-Based Distribution pattern and can be extracted with an $o r g D i s t M u l t i ( T _ { 1 } , T _ { 2 } , R T )$ template where variable RT specifies the type of relation between the two individuals involved. There exist $| T | ^ { 2 } \cdot | R T |$ rule candidates.

orgDistMulti(T1,T2,RT) iff start(of T1 by :p1) and start(of T2 by :p2)

implies relation(subject p1 predicate RT object p2)

## 3.3.3. Cross-perspective rule templates

A cross-perspective rule describes a temporal dependency or constraint between tasks but only applies for a certain set of identities, like in the following examples. Note, that other well-known control-flow patterns described in Ref. [17] can be defined in a similar way. The Role-Based Sequence pattern can be extracted with a roleSequence $T _ { 1 } , T _ { 2 } , G )$ template. Here, $| T | ^ { 2 } \cdot | G |$ candidates need to be checked.

$$
\begin{array}{l} \text {roleSequence(T1,T2,G) iff start(of T2 by :p at :t) and} \\ \text {relation(subject p predicate hasRole object G)} \\ \text {implies complete(of T1 at <   t)} \end{array}
$$

The Resource-Based Response pattern can be extracted with a resourceResponse $( T _ { 1 } , T _ { 2 } , I )$ template. In this case, $| T | ^ { 2 } \cdot | I |$ candidates need to be checked.

resourceResponse(T1,T2,I) iff complete(of T1 by I at :t) implies

start(of T1 at > t)

## 4. Pre-processing to extract meaningful parameters

Real-life event logs and organisational models potentially contain a big set of distinct tasks, resources and groups. For instance, the BPI challenge 2011 event log of a hospital information system [26] contains 623 different tasks and 42 organisational groups. By only considering the role template, this already leads to $6 2 3 . 4 2 \ =$ 26, 166 candidates to be checked. Although many of these parameter combinations never occur together in the same trace, the corresponding rules need to be checked. This problem can also be observed when considering task-resource combinations of the event log in Table 1. Resource i only occurs together with task $t _ { 1 }$ . Hence, candidates of the direct template where $I = i _ { 4 }$ and $T \neq t _ { 1 }$ are trivially true in all traces and can be neglected without checking.

The method proposed in Ref. [24] uses the well-known Apriori algorithm to pre-process the log and to extract task combinations that frequently occur together. The problem of mining frequent itemsets is to find all itemsets that satisfy a user-specified minimum support. The support of an itemset X is the percentage of traces that contain the items of X. Note that this support value is different from the one defined in Section 3.2, which depicts the fraction of traces where a certain rule is non-vacuously satisfied. Specifically, let | | be the total number of traces recorded in the log. Let $\sigma _ { X }$ be the set of traces that contain a set of items X. The support value of an itemset X in V is defined as

$$
\operatorname{supp} (X) = \frac {| \sigma_ {X} |}{| \Phi |}, \text { where } \quad \sigma_ {X} = \{\sigma \in \Phi | \forall_ {x \in X} x \in \sigma \}\tag{3}
$$

A task combination is considered to be relevant if it occurs in a suficient number of traces, i.e., if its support value is greater than a given threshold minSupp. A minSupp of 0.05, e.g., claims that only rule candidates whose parameter combinations occur in at least 5% of the recorded traces are considered. We extended this method to also extract task-resource and task-group combinations that frequently occur together. In this way, it is possible to reduce the number of organisational rule candidates by ignoring infrequent parameter combinations. For instance, for the example log, only one out of three direct $T , i _ { 4 } )$ candidates is generated and checked.

Table 2 shows the form of a single item and the required itemset for the already defined rule templates (cf. Section 3.3). Regarding the rule templates for the assignment of resources to a single task, since only one task is involved, itemsets X with $| X | = 1$ are required. For instance, the direct template has two placeholders, one for tasks and one for identities and hence, itemsets of the form (Task, Identity) are needed. Regarding the rule templates for the assignment of resources to several tasks, since in all these templates two tasks are involved, itemsets with $| X | = 2$ are required. The binding template, e.g., takes frequent items of the form (Task, Task). Finally, the cross-perspective rule templates also have two placeholders and hence, itemsets with $| X | = 2$ are required. The templates capability, orgDistS and orgDistM additionally contain a variable for a relation type. The amount of different relation types in organisational models, however, is usually insignificant compared to the number of different individuals and groups and can therefore be neglected.

## 5. Pruning of discovered models

The output of the mining phase is a process model with rules that state which resources are assigned to the process tasks, e.g., resources with specific roles or capabilities. The mining method extracts all the assignment rules related to each task. However, when several rules are extracted for one single task, not all of them might be strictly necessary to understand the process. Specifically, some rules may be implied by stronger rules because they are less restrictive and do not provide any value to the current resource assignment expression of a task. Those rules complicate the understandability of discovered models and hence, they are unnecessary. We identified two pruning approaches to eliminate unnecessary rules: pruning based on organisational rule hierarchies and pruning based on transitive reduction. The requirement for all pruning operations is that they do not change the meaning of the generated model.

## 5.1. Pruning based on organisational rule hierarchies

Maggi et al. [27] proposed a technique to post-process a discovered model and to remove weaker rules if they are already implied by stronger rules only focusing on the hierarchy of controlflow templates. Hierarchies also exist in the case of organisational rules.

Required itemsets for exemplary organisational rule templates.

<table><tr><td>Rule template</td><td>Item</td><td>Itemset</td></tr><tr><td>direct(T, I)</td><td>(Task, identity)</td><td> $L_1$ : {(Task, identity)}</td></tr><tr><td>role(T, G)</td><td>(Task, group)</td><td> $L_1$ : {(Task, group)}</td></tr><tr><td>capability(T, RT, G)</td><td>(Task, group)</td><td> $L_1$ : {(Task), (Group)}</td></tr><tr><td>orgDistS(T, RT, G)</td><td>(Task, group)</td><td> $L_1$ : {(Task), (Group)}</td></tr><tr><td>binding(T, T)</td><td>(Task)</td><td> $L_2$ : {(Task), (Task)}</td></tr><tr><td>separate(T, T)</td><td>(Task)</td><td> $L_2$ : {(Task), (Task)}</td></tr><tr><td>orgDistMulti(T, T, RT)</td><td>(Task, task)</td><td> $L_2$ : {(Task), (Task)}</td></tr><tr><td>roleSequence(T, T, G)</td><td>(Task, group)</td><td> $L_2$ : {(Task, group), (Task, group)}</td></tr></table>

Please cite this article as: S. Schönig, et al., A framework for eficiently mining the organisational perspective of business processes, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.06.012

We define rule hierarchies for the rule templates defined in Section 3.3. For that purpose, we introduce the dominates relation $ _ { d o m }$ between two rules $r _ { 1 }$ and $r _ { 2 } .$ . Specifically, $r _ { 1 } ~  _ { d o m } r _ { 2 }$ means that rule $r _ { 1 }$ is stronger than rule $r _ { 2 } .$ . The defined rule hierarchies can then be used to prune and simplify discovered models. If a model contains two assignment rules $r _ { 1 }$ and $r _ { 2 }$ concerning the same task and $r _ { 1 }  _ { d o m } r _ { 2 }$ , then $r _ { 2 }$ can be pruned, $\mathrm { i . e . }$ , removed from the model. User-defined rule types have to be integrated in exiting hierarchies by modelling experts. In order to justify the rule hierarchies described next, the following sets and functions must be introduced: $T = \{ t _ { 1 } , t _ { 2 } , \ldots , t _ { n } \}$ is a set of tasks; $R _ { i } = \{ r _ { 1 } , r _ { 2 } , . . . , r _ { m } \}$ is a set of assignment rules discovered for task $t _ { i } ; I = \{ i _ { 1 } , i _ { 2 } , \ldots , i _ { p } \}$ is a set of identities (i.e., individuals) of an organisation; $G = \{ g _ { 1 } , g _ { 2 } , . . . , g _ { q } \}$ is a set of user groups of an organisation (e.g., roles); id $: R _ { i }  \stackrel { \cdot } { I }$ returns the set of identities that meet the conditions defined by a rule; $p p : T $ I returns the set of potential performers of a task, where $p p ( t _ { i } ) = \cap R _ { i }$ and $p p ( t _ { i } ) \neq \emptyset$ because otherwise rules would not have been extracted from the event log for task $t _ { i } \mathrm { ; }$ and ap : $T  I$ returns the actual performer of a task for a specific task instance, so that $a p ( t _ { i } ) \in p p ( t _ { i } )$

We next explain how the rule hierarchies have been derived, providing a demonstration and an example for each dominates relation identified.

## 5.1.1. Rule hierarchy for the templates referred to a single task

We first focus on resource assignment rules for a single task (cf. Section 3.3.1), represented as $\Theta _ { 1 } ~ = ~ \{ ~ d i r e c t ( T , I )$ , role(T, G), capability(T, RT, G), orgDistSingle $\cdot T , R T , G ) \}$

Next, we describe and demonstrate the domination relations found out in $\Theta _ { 1 }$ . For that, let us imagine that we have discovered two rules $R _ { 1 } = \{ r _ { 1 } , r _ { 2 } \}$ for task $t _ { 1 }$ . Therefore, $p p ( t _ { 1 } ) = i d ( r _ { 1 } ) \cap i d ( r _ { 2 } )$ $p p ( t _ { 1 } ) \neq \mathfrak { g }$ . The aim in all cases is to prove that $i d ( r _ { 1 } ) \subseteq i d ( r _ { 2 } ) , \mathrm { i . e . }$ the individuals of $r _ { 1 }$ are a subset of the individuals of $r _ { 2 }$ and hence, $r _ { 2 }$ is weaker and can be removed. The resulting rule hierarchy is visualised in Fig. 4a.

direct( $t _ { 1 } , i _ { 1 } \big )  _ { d o m } { \bf r o l e } ( t _ { 1 } , g _ { 1 } ) ,$ direct( $t _ { 1 } , i _ { 1 } )  _ { d o m }$ capability $\tau _ { 1 } , r t _ { 1 } , g _ { 1 } ) ,$ dire $\pmb { \tau } \pmb { t } ( t _ { 1 } , i _ { 1 } ) \  _ { d o m }$ $\mathbf { o r g } \mathbf { D } i s t \mathbf { S } ( t _ { 1 } , r t _ { 1 } , g _ { 1 } ) .$ . Direct rules dominate role rules, capability rules and orgDistS rules. The demonstration of the three relations is the same, being $\begin{array} { r c l } { r _ { 1 } } & { = } & { d i r e c t { ( t _ { 1 } , i _ { 1 } ) } } \end{array}$ in all cases and $r _ { 2 } ~ = ~ r o l e ( t _ { 1 } , g _ { 1 } ) , r _ { 2 } ~ = ~ c a p a b i l i t y ( t _ { 1 } , r t _ { 1 } , g _ { 1 } )$ and $r _ { 2 } =$ $o r g D i s t S ( t _ { 1 } , r t _ { 1 } , g _ { 1 } )$ , respectively.

Proof. We demonstrate that $i d ( r _ { 1 } ) \subseteq i d ( r _ { 2 } )$ by contradiction. Let $i d ( i _ { 1 } ) = \{ r _ { 1 } \}$ and $i d ( r _ { 2 } ) = \{ i _ { 2 } , i _ { 3 } , i _ { 4 } \} , s o i d ( r _ { 1 } ) \not \subseteq i d ( r _ { 2 } )$ . That means that $i _ { 1 }$ does not have role $g _ { 1 }$ . Then, $p p ( t _ { 1 } ) = i d ( r _ { 1 } ) \cap i d ( r _ { 2 } ) = \emptyset ,$ , which is not possible by definition, as aforementioned. Therefore, and since $| i d ( r _ { 1 } ) | = 1 , i d ( r _ { 1 } ) \subseteq i d ( r _ { 2 } )$ is mandatory and hence, $p p ( t _ { 1 } ) = i d ( r _ { 1 } )$ which means that $r _ { 2 }$ is redundant and can be removed.

Example 1. Consider that a specific task Book flight has always been performed by a resource ST who has the role Student according to the organisational model. Then, the proposed method will (inevitably) discover rules direct(Book flight,ST) and role(Book flight,Student). The identities derived from the latter rule are ST and BR. However, there is no evidence that BR can execute the task and hence, the role rule is not strong enough to be considered in the resource assignment.

$r o l e ( t _ { 1 } , i _ { 1 } )  _ { d o m }$ capa $\pmb { b i l i t y } ( t _ { 1 } , r t _ { 1 } , g _ { 1 } ) ,$ , $\ r o l e ( t _ { 1 } , i _ { 1 } ) \quad \nleftrightarrow _ { d o m }$ orgDistS $( t _ { 1 } , r t _ { 1 } , g _ { 1 } ) ,$ , capa $b i l i t y ( t _ { 1 } , r t _ { 1 } , g _ { 1 } )  _ { d o m }$ $\mathbf { o r g } D i s t S ( t _ { 1 } , r t _ { 1 } , g _ { 1 } ) .$ There is no domination relation between role and capability rules, role and orgDist rules, and capability and orgDist rules. The demonstration is equivalent for any $r _ { 1 }$ and $r _ { 2 }$ belonging to these three groups.

Proof. The difference with respect to the previous demonstration lies on the cardinality of the rules involved. In this case, for any $r _ { 1 } , r _ { 2 }$ of one pair of rule types, $| i d ( r _ { 1 } ) | \ge 1$ and $| i d ( r _ { 2 } ) | \ge 1$ . Since $i d ( r _ { 1 } )$ ∩ $i d ( r _ { 2 } ) \ne \emptyset ,$ , then either $i d ( r _ { 1 } ) \subseteq i d ( r _ { 2 } )$ or $i d ( r _ { 2 } ) \subseteq i d ( r _ { 1 } )$ depending on the number of individuals meeting the conditions specified by the rules. Therefore, a subsumption relation cannot be generalised and hence, both rules are, in general, necessary to calculate the potential performers of a task $t _ { 1 }$ , such that $p p ( t _ { 1 } ) = i d ( r _ { 1 } ) \cap i d ( r _ { 2 } )$ .

Example 2. Consider the situation where the rules role(Approve appli cation,Professor) and capability(Approve application,hasDegree,CS) have been extracted. It means that the task has been performed by someone with the role Professor and with a degree in Computer Science (CS). However, there might also be professors that do not have a degree in Computer Science, and vice versa. Therefore, to describe the necessary task condition, both rules are needed.

## 5.1.2. Rule hierarchy for the templates referred to several tasks

We now focus on resource assignment rules that involve two different tasks (cf. Section 3.3.2), represented as $\begin{array} { r l } { \Theta _ { 2 } } & { { } = } \end{array}$ $\{ { \ b i n d i n g ( T _ { 1 } , T _ { 2 } ) }$ $s e p a r a t e ( T _ { 1 } , T _ { 2 } )$ , orgDistMulti $( T _ { 1 } , T _ { 2 } , R T ) \}$ . Next, we describe and demonstrate the domination relations found out in $\Theta _ { 2 }$ For that, let us imagine that we have discovered two rules $R _ { 1 } = \{ r _ { 1 } , r _ { 2 } \}$ for task $t _ { 1 }$ , where one of the rules, in turn, refers to the assignment rule of task $t _ { 2 } .$ . Similarly to the previous case, $p p ( t _ { 1 } ) = i d ( r _ { 1 } ) \cap i d ( r _ { 2 } )$ $p p ( t _ { 1 } ) \neq \varnothing .$ . The aim is again to prove that $i d ( r _ { 1 } ) \subseteq i d ( r _ { 2 } ) ,$ , i.e., the individuals of $r _ { 1 }$ are a subset of the individuals of $r _ { 2 }$ and hence, $r _ { 2 }$ is weaker and can be removed. The resulting rule hierarchy is visualised in Fig. 4b.

separate( $\dot { t } _ { 1 } , t _ { 2 } )  _ { d o m }$ binding(t , t ). There is no domination relation between separate and binding rules.

Proof. The demonstration is a contradiction by definition. The separate rule implies that $\forall a p ( t _ { 1 } ) , \forall a p ( t _ { 2 } )$ in a specific process instance, $a p ( t _ { 1 } ) \neq a p ( t _ { 2 } ) , \mathrm { i . e . }$ ., both tasks have always been performed by different identities. The binding rule, however, states that ∀ap(t<sub>1</sub>), ∀ap(t<sub>2</sub>) in a specific process instance, ap $\dot { \bf \cal t } _ { 1 } ) = a p ( \mathfrak { t } _ { 2 } ) ,$ , i.e., both tasks have always been performed by the same identity. In case both rules were extracted for task $t _ { 1 } , i d ( r _ { 1 } ) \cap i d ( r _ { 2 } ) \ = \ \varnothing$ and hence, $\begin{array} { r } { p p ( t _ { 1 } ) = \ \vartheta . } \end{array}$ Therefore, these two rules can simply never be extracted at the same time because they are mutually exclusive.

orgDistMulti( $t _ { 1 } , t _ { 2 } , r t _ { 1 } )  _ { d o m }$ binding(t , t ). There is no domination relation between orgDistMulti<sup>2</sup> and binding rules.

Proof. Similarly to the previous case, the demonstration is a contradiction by definition. With an orgDistMulti rule using an irreflexible relation, $a p ( t _ { 1 } ) ~ \neq ~ a p ( t _ { 2 } )$ . However, according to the binding rule, $a p ( t _ { 1 } ) = a p ( t _ { 2 } )$ . Hence, rules of these two types will never be extracted at the same time because they are mutually exclusive.

Example 3. Consider the situation where the rules orgDistMulti (Approve application,Apply for trip,supervisor) and binding(Approve application,Apply for trip) have been extracted for a task. It means that the application must be approved by the supervisor of the person who applies for the trip. Since a person cannot be a supervisor of herself, the tasks are performed by different individuals. However,

S. Schönig, et al. / Decision Support Systems xxx (2016) xxx–xxx

![](/api/attachments/ZGQEF2Z9/fulltext/images/7e7fd3e910bad9e840fb54631967ae07ed62e4f12acd71f343acd929aeafc4d9.jpg)  
(a) Assignment rules w.r.t. a single task  
(b) Assignment rules w.r.t. two tasks  
Fig. 4. Hierarchies of organisational patterns

according to the second rule, the two tasks should be performed by the same person.

orgDistMulti $\begin{array} { r l } { \dot { t } _ { 1 } , \dot { t } _ { 2 } , r { t } _ { 1 } \big ) } & { { }  _ { d o m } } \end{array}$ separate $( t _ { 1 } , t _ { 2 } ) .$ . orgDistMulti rules dominate separate rules

Proof. Let $r _ { 1 } ~ = ~ o r g D i s t M u l t i ( t _ { 1 } , t _ { 2 } , r t _ { 1 } )$ and $r _ { 2 } ~ = ~ s e p a r a t e ( t _ { 1 } , t _ { 2 } ) .$ Assuming irreflexible relations in the organisation, according to both rules $a p ( t _ { 1 } ) \neq a p ( t _ { 2 } )$ . Since $i d ( r _ { 1 } ) \subseteq i d ( r _ { 2 } ) , p p ( t _ { 1 } ) = i d ( r _ { 1 } )$ , which means that $r _ { 2 }$ is redundant and can be removed.

Example 4. Consider the situation where the rules orgDistMulti (Approve application,Apply for trip,supervisor) and separate(Approve application,Apply for trip) have been extracted for a task. It means that the application must be approved by the supervisor of the person who applies for the trip. Since a person cannot be a supervisor of herself, the tasks are performed by different individuals. However, not all the other persons in the organisation might be supervisors of the person applying for the trip. Therefore, this condition is more restrictive than the separation of duties and then, the latter is not necessary in the resource assignment expression.

## 5.1.3. Rule hierarchy for the cross-perspective templates

Finally, we address cross-perspective rules (cf. Section 3.3.3), represented as $\Theta _ { 3 } = \{ r o l e S e q u e n c e ( T _ { 1 } , T _ { 2 } , G )$ , resourceSequence(T , T , I)}.

Notice that in this case the approach is different from $\Theta _ { 1 }$ and $\Theta _ { 2 }$ since we aim at generalising under which conditions a specific activity order must take place. That means that a rule $r _ { 1 }$ is stronger than a rule $r _ { 2 }$ if $i d ( r _ { 2 } ) \subseteq i d ( r _ { 1 } )$ . As demonstrated next, roleSequence $\cdot t _ { 1 } , t _ { 2 } , g _ { 1 } )  _ { d o m }$ resourceSequence(t , t , i ).

Proof. Let us imagine that we have discovered two rules $\begin{array} { r c l } { R _ { 1 } } & { = } & { \{ r _ { 1 } , r _ { 2 } \} } \end{array}$ , where $\begin{array} { l l l } { r _ { 1 } } & { = } & { r o l e S e q u e n c e ( t _ { 1 } , t _ { 2 } , g _ { 1 } ) ^ { 3 } } \end{array}$ and $r _ { 2 } = { }$ resourceSequenc $\boldsymbol { \mathbf { \ell } } _ { t _ { 1 } , t _ { 2 } , i _ { 1 } } )$ . The temporal dependency is the same in both cases, specifically, a specific task order determined by $s e q u e n c e ( t _ { 1 } , t _ { 2 } )$ . Therefore, we could assume that $r _ { 1 } = r o l e ( t _ { 1 } , g _ { 1 } )$ and $r _ { 2 } = d i r e c t ( t _ { 1 } , i _ { 1 } )$ . According to the aforementioned criterion, since $| i d ( r _ { 1 } ) | \ge 1$ and $| i d ( r _ { 2 } ) | = 1 , i d ( r _ { 2 } ) \subseteq i d ( r _ { 1 } ) ,$ , i.e., the individuals of $r _ { 2 }$ are a subset of the individuals of $r _ { 1 }$ and hence, $r _ { 2 }$ is weaker and can be removed.

Example 5. Consider that task Apply for trip has always been performed before task Book flight when executed either by resource ST or by resource BR, who have the role Student according to the organisational model. Then, the proposed method will (inevitably) discover rules resourceSequence(Apply for trip,Book flight,ST), resourceSequence(Apply for trip,Book flight,BR) and roleSequence(Apply for trip,Book flight,Student). Since the individuals of both resourceSequence rules (i.e., ST and BR) are a subset of the individuals of the roleSequence rule, they can both be removed from the model.

## 5.2. Pruning based on transitive reduction

The assignment rules in $\Theta _ { 2 }$ (cf. Section 5.1.2) may be affected by transitivity. In particular, redundancy may be caused by the interplay of three or more rules of the same type applied to different activities. Consider a set of discovered binding rules, such as binding(t , t ), $b i n d i n g ( t _ { 2 } , t _ { 3 } )$ and $b i n d i n g ( t _ { 1 } , t _ { 3 } )$ . Here, the rule between $t _ { 1 }$ and $t _ { 3 }$ is redundant because it belongs to the transitive closure of the other rules. In other words, if task $t _ { 1 }$ has always been performed by the same resource as $t _ { 2 } ,$ and task $t _ { 3 }$ has always been performed by the same resource as $t _ { 2 } ,$ , then also $t _ { 1 }$ and $t _ { 3 }$ have been performed by the same resource. Therefore, binding( $t _ { 1 } , t _ { 3 } )$ is unnecessary and could be removed using the transitive reduction algorithm as defined in Ref. [28]. OrgDistMulti rules can be transitively reduced in a similar way if they refer to the same relation type rt and if rt is a transitive relation (cf. Section $2 ) .$ . However, separate rules are not transitive, $\mathrm { i . e . , }$ if $t _ { 1 }$ is not performed by the same resource as $t _ { 2 }$ and $t _ { 2 }$ is not executed by the same resource as $t _ { 3 } ,$ then we cannot conclude that $t _ { 1 }$ is also not performed by the same resource as $t _ { 3 }$

## 6. Evaluation

We evaluate our framework in three steps. We first describe how it has been implemented. We then show its eficiency with simulation experiments. Finally, we report on the results of applying the framework on a real-life event log.

S. Schönig, et al. / Decision Support Systems xxx (2016) xxx–xxx

Table 3  
Rules for transforming DPIL to DRL expressions.

<table><tr><td>Nr.</td><td>DPIL expression</td><td>DRL expression</td></tr><tr><td>1</td><td>task T:t</td><td>$t: Task(id == “T”)</td></tr><tr><td>2</td><td>start(of T)</td><td>$t: Task(id == “T”) and Start(Task == $t)</td></tr><tr><td>3</td><td>expr</td><td>rule Idwhen expr then listener.onRuleOccurred(drools.getRule()));</td></tr><tr><td>4</td><td>x implies y</td><td>not (x and not y)</td></tr></table>

## 6.1. Implementation

The problem of checking a large set of rule candidates can be solved by eficient pattern matching methods like the retealgorithm [29]. Instead of checking each rule separately, the rete algorithm first identifies common parts of the provided set of rules and constructs a retenetwork. Based on this decision network, common rule parts just need to be checked once. The JBoss Drools platform<sup>4</sup> provides a current implementation of this method. In order to check rule candidates with Drools, they are translated into the Drools Rule Language (DRL). Like in DPIL, rules in DRL consist of a condition (when part) and a consequence (then part). If the condition holds, the consequence will be performed. DRL supports language elements to describe rules of first order logic, hence being equivalent to DPIL. The transformation of the most important expressions from DPIL to DRL is shown in Table 3. DPIL rules are translated into DRL rules like in row 3. As can be seen, the complete DPIL rule is placed in the when part of the DRL rule. The consequence, i.e., the then part, only contains a procedure call that signals the satisfaction of the corresponding rule to the program environment (listener). Since DRL does not support a logical implication directly, DPIL implications must be translated into DRL according to the logical equivalence $A \to B \equiv \neg ( A \land \neg B )$ (cf. row 4 in Table 3). The described approach has been implemented in the DpilMiner application.<sup>5</sup>

## 6.2. Performance evaluation

To analyse performance we used the DpilMiner with different configurations using an event log of a university business trip management system.<sup>6</sup> The log contains 2104 events of 10 different activities related to the application and the approval of university business trips as well as the management of accommodations and transfers, e.g., booking hotels and transport tickets. The system has been used for 6 months by 11 employees of a research institute of the University of Bayreuth (Germany). The organisational model of the institute assigns the 11 identities to 4 distinct roles, specifically 6 PhD students, 1 professor, 1 secretary and 3 administration employees. In total, there are 128 business trips, i.e., traces, recorded. All the computation times reported in this section are measured on a Core i7 CPU @2.80 GHz with 8 GB Ram.

Our approach has been tested with two different sets of rule templates. Fig. 5a shows the results of applying the approach with template set1, which contains the templates direct, role, binding and orgDistMulti. Fig. 5b shows the results for template set2, which contains the sequence template and the roleSequence cross-perspective template.

We analysed the time to build the rete network, i.e., the rule base<sup>7</sup>, as well as the time to perform the actual mining process taking into account a different number of rule candidates. This was achieved by considering different minSupp values during the pre-processing phase ranging from 0 to 0.4 (cf. Section 4). The analysis shows the feasibility of our approach since in both tests, despite a big amount of candidates, only a manageable number of rules have been discovered. Especially the diagram in Fig. 5b highlights the benefit of the pre-processing approach. With increasing minSupp, the number of candidates to check considerably decreases, which reduces the processing time up to 50%. However, almost the same number of rules has been discovered in all cases before the post-processing phase. However, both diagrams show that the number of extracted rules is clearly reduced by pruning unnecessary rules. Fig. 5b, e.g., shows that the number of rules can be reduced by 50%.

In order to check the eficiency of our approach we also applied the implementation of the DeclareMiner [30] available in the process mining framework (ProM) by only analysing the precedence template of Declare [17], which equates to the sequence template of DPIL. With standard settings, the DeclareMiner needed 14.85 s to analyse the provided event log with the precedence template. Even if we analysed the example log with 2, respectively 4, rule templates, our approach was still faster in any case. For template set 1 and without pre-processing, the generation of the rule base for the rete algorithm took 7.75 s while the actual analysis took only 6.74 s.

## 6.3. Application to real-life event log

In this section we describe our findings when applying the approach to the university business trip log of Section 6.2. We analysed the log with the 6 aforementioned rule templates. With minSupp = 0.1 in the pre-processing phase and after removing unnecessary rules in the post-processing phase, we extracted 34 rules in total. The extracted resource assignment rules are composed of 4 direct, 1 role, 5 binding and 4 orgDistMulti rules. The rules with control-flow information include 14 sequence and 6 roleSequence rules. For the classification in satisfied and violated rules, we used minConf = 0.85 and minInt = 1.0. For space reasons, we only describe some interesting parts of the resulting model (cf. Fig. 6). The discovered model shows that task “Approve Application” has mostly been performed by the identity “SJ” (direct). Furthermore, “Check Application” has mostly been performed by a resource with the role “Administration” (role). The three binding of duties rules show that the resource who booked the flight tickets, the accommodation and the transfer service has to be the person that applies for the trip (binding). Moreover, the resource who approves the trip application is the supervisor of the applicant (orgDistMulti). Regarding cross-perspective patterns, there are cases in which certain employees already booked a flight without applying for the trip. However, when analysing the task order under consideration of performing resources, we extracted that students always applied for the trip before they booked the flight (roleSequence).

In a second step we evaluated the quality of the mining results and how varying the mining configuration, i.e., different thresholds, influences it. Therefore, three discovered models (M1, M2, M3) based on different configurations of the approach on the same event log were discussed and evaluated in a workshop. The models were extracted using different minSupp values during the preprocessing phase as well as different minConf values during the mining phase. Table 4 shows the characteristics of the discovered models. M1 has been discovered by applying the approach without any pre-processing (low filtering). M2 depicts the model that has been described before and is based on a pre-processed log with min-Supp=0.1 (medium filtering). Both M1 and M2 include rules r with conf(r) > 0.85. One task that occurs in less than 10% of traces and the corresponding rules have been filtered in M2. M3 is based on minConf = 0.9, i.e., less rules are classified as satisfied (high filtering). The workshop was carried out with 8 process participants, i.e., university employees that represented all the organisational groups involved. After we provided a general overview about the process and the workshop setting, each of the extracted rules was classified by the participants.

![](/api/attachments/ZGQEF2Z9/fulltext/images/2d528d2cb1eb451c169779c34a5df7715e42a8cdff603dc917243af633b6fe2d.jpg)  
(a) Results using rule template set 1

![](/api/attachments/ZGQEF2Z9/fulltext/images/f6336996964f857d541bd7ba884bf6ef66fef70242d164ed004d54b18b935697.jpg)  
(b) Results using rule template set 2  
Fig. 5. Performance evaluation using different sets of rule templates.

For evaluating the quality of the results, we rely on standard metrics from information retrieval precision and recall [31]. The harmonic mean (F-measure) of precision and recall is an adequate value for measuring the overall quality of extracted models [31]. To compute recall and precision, rules have been classified into one of three categories, i.e., (i) true-positive (T : correctly discovered); (ii) false-positive (F<sub>P</sub>: incorrectly discovered); (iii) false-negative (F<sub>N</sub>: incorrectly missing). Precision, recall and F-measure are defined as follows:

$$
P r e c i s i o n = \frac {T _ {P}}{T _ {P} + F _ {P}}, \quad R e c a l l = \frac {T _ {P}}{T _ {P} + F _ {N}}, \quad F = 2 \cdot \frac {P \cdot R}{P + R}\tag{4}
$$

The results of the workshop as well as the calculated quality metrics are collected in Table 4. First of all, we focus on the results of M2. According to the information gathered from the process participants, 34 of 39 rules have been classified as relevant $\left( T _ { P } \right)$ while 5 rules have been discovered incorrectly $( F _ { P } )$ . Furthermore, 6 missing rules $\left( F _ { N } \right)$ have been identified in the discussion. The reason is that a task and the assignment rules related to that task were filtered in the pre-processing phase. Based on this classification, we obtain Precision=0.87, Recall=0.85 and therefore, F=0.86. Comparing the three models in Table 4 we can observe that M1 has the highest F-measure, $\mathrm { i . e . , }$ the best quality. Since the model was extracted without filtering infrequent behaviour, there were no rules missing (Recall=1.0). Without filtering, however, M1 also contains 7 irrelevant rules leading to a lower precision value. Since M3 is based on a higher minConf threshold, the model contains fewer rules. However, some of the missing rules were identified as relevant by the workshop participants. Due to the missing rules, M3 features the lowest recall and thus also the lowest F-measure.

```julia
ensure direct(Approve Application, SJ)  
ensure role(Check Application, Administration)  
ensure binding(Apply for trip, Book flight)  
ensure binding(Apply for trip, Book accommodation)  
ensure binding(Apply for trip, Book transfer)  
ensure orgDistMulti(Approve Application, Apply for trip, supervisor)  
ensure roleSequence(Apply for trip, Book flight, Student)
```  
Fig. 6. Examples of discovered rules.

## 7. Related work

Several approaches have been proposed in the literature for the discovery of declarative process models. In Ref. [25] the authors present an approach that allows the user to select from a set of predefined Declare templates the ones to be used for the discovery. Maggi et al. propose an evolution of this approach in Ref. [24] to improve performance by pre-processing the event log with frequent pattern mining techniques. Other approaches to improve the performance of process mining are presented in Refs. [3, 32]. Additionally, there are post-processing approaches that aim at simplifying the resulting Declare models in terms of redundancy elimination [33] and disambiguation [27]. The approach proposed in Ref. [34] allows for the specification of rules that go beyond the traditional Declare templates. In Ref. [35], an approach for analysing event logs with Timed Declare, an extension of Declare that relies on timed automata, is described. The work in Ref. [36] first covered the data perspective in declarative process mining, although this approach only allows for the discovery of discriminative activation conditions. In essence, the focus of the aforementioned approaches is control-flow with extensions to cover data without analysing resource-related information.

Complementary to them are techniques for mining the organisational perspective of a process [33]. Methods for analysing event logs w.r.t. resources are mainly focused on enriching a given procedural model with resource assignments [13]. Several methods focus on extracting an organisational model [9] or a social network [8]. There are also approaches that analyse the influence of resources on process performance [10]. However, the approaches that are of

Characteristics, results and metrics of discovered models

<table><tr><td></td><td>Model 1</td><td>Model 2</td><td>Model 3</td></tr><tr><td>Mining configuration</td><td>Low filtering</td><td>Medium filtering</td><td>High filtering</td></tr><tr><td>minSupp (Pre-processing)</td><td>∅</td><td>0.1</td><td>0.1</td></tr><tr><td>minSupp</td><td>∅</td><td>0.2</td><td>0.2</td></tr><tr><td>minConf</td><td>0.85</td><td>0.85</td><td>0.9</td></tr><tr><td colspan="4">Characteristics of models</td></tr><tr><td>Number of tasks</td><td>10</td><td>9</td><td>9</td></tr><tr><td>Number of identities</td><td>10</td><td>10</td><td>10</td></tr><tr><td>Number of rules</td><td>47</td><td>39</td><td>31</td></tr><tr><td colspan="4">Metrics</td></tr><tr><td> $T_P$ (correctly discovered)</td><td>40</td><td>34</td><td>28</td></tr><tr><td> $F_P$ (incorrectly discovered)</td><td>7</td><td>5</td><td>3</td></tr><tr><td> $F_N$ (incorrectly missing)</td><td>0</td><td>6</td><td>12</td></tr><tr><td>Precision</td><td>0.85</td><td>0.87</td><td>0.9</td></tr><tr><td>Recall</td><td>1.0</td><td>0.85</td><td>0.7</td></tr><tr><td>F-measure</td><td>0.92</td><td>0.86</td><td>0.8</td></tr></table>

Please cite this article as: S. Schönig, et al., A framework for eficiently mining the organisational perspective of business processes, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.06.012

Table 5  
Existing approaches for mining the organisational perspective.

<table><tr><td>Pattern</td><td>Mining approach</td></tr><tr><td>Direct Distribution</td><td>[9, 12, 16, 37, 38, 39]</td></tr><tr><td>Role-Based Distribution</td><td>[9, 12, 16, 37, 38, 39]</td></tr><tr><td>Deferred Distribution</td><td>-</td></tr><tr><td>Separation of Duties</td><td>[11, 12, 16]</td></tr><tr><td>Case Handling</td><td>[9, 12, 16]</td></tr><tr><td>Retain Familiar</td><td>[11, 12, 16]</td></tr><tr><td>Capability-Based Distribution</td><td>[16, 37]</td></tr><tr><td>History-Based Distribution</td><td>-</td></tr><tr><td>Organisational Distribution</td><td>[37] (single task) [16] (incl. several tasks)</td></tr><tr><td>Cross-perspective patterns</td><td>[16]</td></tr></table>

highest interest to us are those collected in Table 5, which address the discovery of organisational or cross-perspective patterns. Staff assignment mining [37] is able to extract complex assignment rules based on decision tree learning. However, the resource assignments are only related to one single task (cf. Section 5.1.1). Works on role mining [11, 12] are, on the contrary, interested in those types of rules referring to several tasks (cf. Section 5.1.2) but disregard other patterns. Resource mining is also implemented in ProM. In Ref. [38] the authors propose a two-step technique for enriching a given controlflow model with swimlanes based on the Handover of Roles (HooR) principle.<sup>8</sup> In the first step the pairs of immediately consecutive activities are analysed in terms of potential role changes based on three rules: (i) pairs of immediately consecutive activities that are always executed by the same resource do not involve a HooR, (ii) pairs of immediately consecutive activities that are each executed by exactly the same set of resources do not involve a HooR and (iii) pairs of immediately consecutive activities that are, to a certain proportion w, executed by the same resources do not involve a HooR. All rules are based upon the assumption that each resource has exactly one role. The clustering-inspired algorithm generates a partition of activities for each HooR. The last step of the algorithm merges similar partitions in order to identify the actual roles. Finally, the algorithm chooses the most suitable final partitioning based on an entropy measure.

None of the aforementioned approaches on resource mining covers the whole sets of organisational and cross-perspective patterns that constitute the goal of our work. The DpilMiner was developed to bridge that gap and hence, we used its mining approach [16] for the mining phase of our framework, which we extended with preprocessing and post-processing techniques inspired by the solutions related to mining the process control-flow.

## 8. Conclusions and future work

In this paper we presented a process mining framework to discover resource-aware process models. Our approach is based upon the mining approach introduced in Ref. [16], which we extended with pre-processing and post-processing phases. This increased eficiency while generating simplified process models that provide the same valuable information, as demonstrated by our evaluations.

Since our approach relies on DPIL [20], the mining capabilities are limited to its expressiveness. Therefore, inter-case dependencies, such as those represented in the History-Based Distribution pattern, cannot be discovered. It is an interesting question for future research how such dependencies can be mined and effectively depicted in a process model. Furthermore, there might be more ways to prune discovered models that take into account more knowledge besides hierarchies and transitive reduction. By pruning more intelligently, a better model could be obtained. Finally, we plan to investigate options for mapping the output to graphical process modelling notations to increase readability.

## References

[1] M. Dumas, M.L. Rosa, J. Mendling, H.A. Reijers, Fundamentals of Business Process Management, Springer-Verlag Berlin Heidelberg. 2013. http://dx.doi.org/ 10.1007/978-3-642-33143-5.

[2] W. van der Aalst, Process Mining: Discovery, Conformance and Enhancement of Business Processes, Springer-Verlag Berlin Heidelberg. 2011. http://dx.doi. org/10.1007/978-3-642-19345-3.

[3] C. Di Ciccio, M. Mecella, On the discovery of declarative control flows for artful processes, ACM Trans. Management Inf. Syst. 5 (4) (2015) 24:1–24:37. http:// dx.doi.org/10.1145/2629447.

[4] W.M.P. van der Aalst, M. Rosemann, M. Dumas, Deadline-based escalation in process-aware information systems, Decision Support Systems 43 (2) (2007) 492–511. http://dx.doi.org/10.1016/j.dss.2006.11.005.

[5] W.M.P. van der Aalst, K.M. van Hee, J.M.E.M. van der Werf, A. Kumar, M. Verdonk, Conceptual model for online auditing, Decision Support Systems 50 (3) (2011) 636–647. http://dx.doi.org/10.1016/j.dss.2010.08.014.

[6] M. de Leoni, M. Adams, W.M.P. van der Aalst, A.H.M. ter Hofstede, Visual sup port for work assignment in process-aware information systems: framework formalisation and implementation, Decision Support Systems 54 (1) (2012) 345–361. http://dx.doi.org/10.1016/j.dss.2012.05.042.

[7] C. Cabanillas, D. Knuplesch, M. Resinas, M. Reichert, J. Mendling, A. Ruiz-Cortés, RALph: a graphical notation for resource assignments in business processes, Int. Conf. on Advanced Information Systems Engineering (CAiSE), 9097, 2015. pp. 53–68. http://dx.doi.org/10.1007/978-3-319-19069-3\_4

[8] W. van der Aalst, H.A. Reijers, M. Song, Discovering social networks from event logs, Computer Supported Cooperative Work 14 (6) (2005) 549–593. http://dx. doi.org/10.1007/s10606-005-9005-9.

[9] M. Song, W. van der Aalst, Towards comprehensive support for organizational mining, Decision Support Systems 46 (1) (2008) 300–317. http://dx.doi.org/10. 1016/j.dss.2008.07.002

[10] J. Nakatumba, W. van der Aalst, Analyzing resource behavior using process mining, Business Process Management Workshops, 2010. pp. 69–80. http://dx.doi. org/10.1007/978-3-642-12186-9\_8.

[11] M. Leitner, A. Baumgrass, S. Schefer-Wenzl, S. Rinderle-Ma, M. Strembeck, A case study on the suitability of process mining to produce current-state RBAC models, Business Process Management Workshops, 2012. pp. 719–724. http:// dx.doi.org/10.1007/978-3-642-36285-9\_72.

[12] A. Baumgrass, M. Strembeck, Bridging the gap between role mining and role engineering via migration guides, Inf. Sec. Techn. Report 17 (4) (2013) 148–172. http://dx.doi.org/10.1016/j.istr.2013.03.003.

[13] W. Zhao, X. Zhao, Process mining from the organizational perspective, Advances in Intelligent Systems and Computing, 277, 2014. pp. 701–708. http://dx.doi.org/10.1007/978-3-642-54924-3\_66.

[14] N. Russell, W.M.P. van der Aalst, A.H.M. ter Hofstede, D. Edmond, Workflow resource patterns: identification, representation and tool support, Advanced Information Systems Engineering, 2005. pp. 216–232. http://dx.doi.org/10. 1007/11431855\_16.

[15] M. de Leoni, W.M. van der Aalst, M. Dees, A general process mining framework for correlating, predicting and clustering dynamic behavior based on event logs, Information Systems 56 (2016) 235–257. http://dx.doi.org/10.1016/j.is. 2015.07.003.

[16] S. Schönig, C. Cabanillas, S. Jablonski, J. Mendling, Mining the organisational perspective in agile business processes, Int. Conf. on Enterprise, Business-Process and Information Systems Modeling (BPMDS), Vol. 214 of LNBIP, Springer. 2015, pp. 37–52. http://dx.doi.org/10.1007/978-3-319-19237-6\_3.

[17] W. van der Aalst, M. Pesic, H. Schonenberg, Declarative workflows: balancing between flexibility and support, Computer Science - R&D 23 (2) (2009) 99–113. http://dx.doi.org/10.1007/s00450-009-0057-9.

[18] E. Verbeek, J. Buijs, B. van Dongen, W. van der Aalst, XES, xESame, and ProM 6, information Systems Evolution, 72, 2011. pp. 60–75. http://dx.doi.org/10.1007/ 978-3-642-17722-4.5

[19] OMG, BPMN 2.0, OMG. 2011.

[20] M. Zeising, S. Schönig, S. Jablonski, Towards a common platform for the support of routine and agile business processes, IEEE Int. Conf. on Collaborative Computing: Networking, Applications and Worksharing, 2014. pp. 94–103. http:// dx.doi.org/10.4108/icst.collaboratecom.2014.257269.

[21] M. Montali, Specification and Verification of Declarative Open Interaction Models — A Logic-based Approach, 56. Springer. 2010. http://dx.doi.org/10.1007/ 978-3-642-14538-4

[22] F. Maggi, M. Montali, M. Westergaard, W. van der Aalst, Monitoring business constraints with linear temporal logic: an approach based on colored automata, Int. Conf. on Business Process Management (BPM), 6896, Springer. 2011, pp. 132–147. http://dx.doi.org/10.1007/978-3-642-23059-2\_13.

[23] C. Bussler, Organisationsverwaltung in Workflow-Management-Systemen, Deutscher Universitätsverlag. 1998. http://dx.doi.org/10.1007/978-3-663- 08832-5

[24] F.M. Maggi, J.C. Bose, W. van der Aalst, Eficient discovery of understandable declarative process models from event logs, Int. Conf. on Advanced Information

Systems Engineering (CAiSE), 7328, 2012. pp. 270–285. http://dx.doi.org/10. 1007/978-3-642-31095-9.18

[25] F.M. Maggi, A. Mooij, W. van der Aalst, User-guided discovery of declarative process models, IEEE Symposium on Computational Intelligence and Data Mining, 2011. pp. 192–199. http://dx.doi.org/10.1109/CIDM.2011.5949297.

[26] R.J.C. Bose, W.M.P. van der Aalst, Analysis of patient treatment procedures, Business Process Management Workshops, 99, 2011. pp. 165–166. http://dx. doi.org/10.1007/978-3-642-28108-2\_17.

[27] F.M. Maggi, J.C. Bose, W.M. van der Aalst, A knowledge-based integrated approach for discovering and repairing declare maps, Int. Conf. on Advanced Information Systems Engineering (CAiSE), 7908, 2013. pp. 433–448. http://dx. doi.org/10.1007/978-3-642-38709-8.28.

[28] A.V. Aho, M.R. Garey, J.D. Ullman, The transitive reduction of a directed graph, SIAM J. Comput. 1 (2) (1972) 131–137. http://dx.doi.org/10.1137/0201008.

[29] C. Forgy, Rete: a fast algorithm for the many patterns/many objects match problem, Artif. Intell. 19 (1) (1982) 17–37. http://dx.doi.org/10.1016/0004- 3702(82)90020-0.

[30] F.M. Maggi, Declarative process mining with the declare component of ProM, Business Process Management Demos, Vol. 1021 of CEUR Workshop Proceed ings, 2013. URL http://ceur-ws.org/Vol-1021/paper\_8.pdf.

[31] A. Rozinat, A.K.A de Medeiros, C.W. Günther, A. Weijters, W.M. van der Aalst, The need for a process mining evaluation framework in research and practice, Business Process Management Workshops, 4928, 2008. pp. 84–89. http://dx. doi.org/10.1007/978-3-540-78238-4\_10.

[32] M. Westergaard, C. Stahl, H. Reijers, UnconstrainedMiner: Eficient Discovery of Generalized Declarative Process Models, Eindhoven University of Technology. 2013, URL https://publications.hse.ru/en/preprints/117624631.

[33] J.C. Bose, F.M. Maggi, W. van der Aalst, Enhancing declare maps based on event correlations, Int. Conf. on Business Process Management (BPM), 8094, 2013. pp. 97–112. http://dx.doi.org/10.1007/978-3-642-40176-3\_9.

[34] F. Chesani, E. Lamma, P. Mello, M. Montali, F. Riguzzi, S. Storari, Exploiting inductive logic programming techniques for declarative process mining, Trans. Petri Nets and Other Models of Concurrency 2 (2009) 278–295. http://dx.doi. org/10.1007/978-3-642-00899-3\_16.

[35] F.M. Maggi, Discovering metric temporal business constraints from event logs, Int. Conf. on Perspectives in Business Informatics Research (BIR) 194, Springer. 2014, pp. 261–275. http://dx.doi.org/10.1007/978-3-319-11370-8\_19.

[36] F.M. Maggi, M. Dumas, Discovering data-aware declarative process models from event logs, Int. Conf. on Business Process Management (BPM), 8094, 2013. pp. 1–16. http://dx.doi.org/10.1007/978-3-642-40176-3\_8.

[37] S. Rinderle-Ma, W.M. van der Aalst, Life-cycle Support for Staff Assignment Rules in Process-aware Information Systems, Eindhoven University of Technology. 2007, URL http://dbis.eprints.uni-ulm.de/373/.

[38] A. Burattin, A. Sperduti, M. Veluscek, Business models enhancement through discovery of roles, IEEE Symposium on Computational Intelligence and Data Mining, 2013. pp. 103–110. http://dx.doi.org/10.1109/CIDM.2013.6597224.

[39] T. Jin, J. Wang, L. Wen, Organizational modeling from event logs, Int. Conf. on Grid and Cooperative Computing (GCC), 2007. pp. 670–675. http://dx.doi.org/ 10.1109/GCC2007.93

![](/api/attachments/ZGQEF2Z9/fulltext/images/a1b51b91023d8c562f63930c073e970f5e6c91ad1ae2fdfa2aff92faa48b450f.jpg)  
Dr. Stefan Schönig is a post-doctoral researcher and lecture assistant with the Institute for Computer Science at University of Bayreuth (Germany). His research is focused on the observation and analysis of executed business processes. He has participated in several industry projects that addressed process mining and process monitoring. Based on his work, he has published several scientific papers in international conferences.

![](/api/attachments/ZGQEF2Z9/fulltext/images/2c2e2587264e91a10ae161ee8ca1871d5ffa2e56ad619f6aef58e3536e3c73d2.jpg)

![](/api/attachments/ZGQEF2Z9/fulltext/images/76a21b12e1cfb54d541adebf02acf56e60c21e24aced28ab60d2f47a248ea183.jpg)

![](/api/attachments/ZGQEF2Z9/fulltext/images/4cc98a5c732136dfbe458b369b0c9f3c7baac699a4826141cbd0cd6194fc867b.jpg)

Dr. Cristina Cabanillas is a post-doctoral researcher with the Institute for Information Business at the Vienna University of Economics and Business (Austria). She obtained her PhD degree at the University of Seville (Spain), with a thesis on Human Resource Management in Business Pro cesses. She is currently involved in the FFG SHAPE project Her research interests include business process modelling and analysis, business process compliance, complex event processing, and crowdsourcing and data integration.

Dr.-Ing. Stefan Jablonski is a Full Professor of Computer Science with the Institute for Computer Science at University of Bayreuth (Germany). He is head of the chair for Databases and Information Systems. His major research interests include Business Process Management, flexible process enactment technologies, and meta-modelling. He has been participating in numerous national and interna tional BPM research as well as industrial projects.

Dr. Jan Mendling is a Full Professor with the Institute fo Information Business at Vienna University of Economics and Business (Austria). His research areas include Business Process Management, Conceptual Modelling and Enterprise Systems. He has published more than 200 research papers and articles, among others in ACM Transactions on Software Engineering and Methodology, IEEE Transaction on Software Engineering, Information Systems, and Decision Support Systems. He is member of the editorial board of four international journals, organizer of several academic events on process management, and member of the IEEE Task Force on Process Mining.
