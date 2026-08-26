---
otero_id: 11350
otero_key: "B8HTM85T"
title: "Evaluating the effect of best practices for business process redesign: An evidence-based approach based on process mining techniques"
authors: "Minsu Cho; Minseok Song; Marco Comuzzi; Sooyoung Yoo"
year: "2017"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2017.10.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Evaluating the effect of best practices for business process redesign: An evidence-based approach based on process mining techniques

![](/api/attachments/B8HTM85T/fulltext/images/117b6a56631fae1a5ecfcb0ee4eccf9460f157a5d121eab1f454b0341541fac4.jpg)

Minsu Cho, Minseok Song, Marco Comuzzi, Sooyoung Yoo

<table><tr><td>PII:</td><td>S0167-9236(17)30182-3</td></tr><tr><td>DOI:</td><td>doi:10.1016/j.dss.2017.10.004</td></tr><tr><td>Reference:</td><td>DECSUP 12885</td></tr><tr><td>To appear in:</td><td>Decision Support Systems</td></tr><tr><td>Received date:</td><td>17 January 2017</td></tr><tr><td>Revised date:</td><td>12 October 2017</td></tr><tr><td>Accepted date:</td><td>12 October 2017</td></tr></table>

Please cite this article as: Minsu Cho, Minseok Song, Marco Comuzzi, Sooyoung Yoo , Evaluating the effect of best practices for business process redesign: An evidence-based approach based on process mining techniques. The address for the corresponding author was captured as affiliation for all authors. Please check if appropriate. Decsup(2017), doi:10.1016/j.dss.2017.10.004

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Evaluating the effect of best practices for business process redesign: an evidence-based approach based on process mining techniques

Minsu Cho<sup>1,2</sup>, Minseok Song<sup>1</sup>, Marco Comuzzi<sup>2</sup>, Sooyoung Yoo<sup>3</sup>

<sup>1</sup> Department of Industrial & Management Engineering, Pohang University of Science and Technology

<sup>2</sup> School of Management Engineering, Ulsan National Institute of Science and Technology

<sup>3</sup> Healthcare ICT Research Center, Seoul National University Bundang Hospital

## Abstract

The management of business processes in modern times is rapidly shifting towards being evidence-based. Business process evaluation indicators tend to focus on process performance only, neglecting the definition of indicators to evaluate other concerns of interest in different phases of the business process lifecycle. Moreover, they usually do not discuss specifically which data must be collected to calculate indicators and whether collecting these data is feasible or not. This paper proposes a business process assessment framework focused on the process redesign lifecycle phase and tightly coupled with process mining as an operational framework to calculate indicators. The framework includes process performance indicators and indicators to assess whether process redesign best practices have been applied and to what implicitly, also defines what data must be collected during process execution to enable their calculation. The framework is evaluated through case studies and a thorough comparison against other approaches in the literature.

Keywords: Process redesign, best practice, process performance indicator, process mining, case study, business process management

## 1 Introduction

Business processes are at the heart of modern organizations and continuously evolve to address changing business requirements [1]. Their execution is often supported by advanced business process management systems [2], which collect and make the available large amount of data for process analysis and improvement [2]. The availability of these data pushes business process (re-)design and improvement to become “evidence-based”. Evidence-based management of business processes is usually implemented using a set of indicators that capture the relevant aspects of business processes and related phases in the process management lifecycle [3].

While several frameworks defining indicators for business process evaluation have been proposed in the literature [3–6], we argue that they suffer from the following two limitations: (i) they assume that the data to calculate indicators are available or, in other words, they do not specify in depth which type of data should be collected in order to calculate indicators and whether that is feasible, and (ii) they only focus on process performance assessment, i.e., they do not provide evidence to analyse and make decisions related to the effective implementation of other specific phases of the business process management lifecycle, such as business process re-design, as in the case of this paper.

<table><tr><td>BP1</td><td>Contact reduction</td></tr><tr><td>BP2</td><td>Integration</td></tr><tr><td>BP3</td><td>Control relocation</td></tr><tr><td>BP4</td><td>Activity elimination</td></tr><tr><td>BP5</td><td>Activity composition</td></tr><tr><td>BP6</td><td>Case types</td></tr><tr><td>BP7</td><td>Triage</td></tr><tr><td>BP8</td><td>Order-based work</td></tr><tr><td>BP9</td><td>Resequencing</td></tr><tr><td>BP10</td><td>Parallelism</td></tr><tr><td></td><td>...</td></tr><tr><td>BP29</td><td>Interfacing</td></tr></table>

![](/api/attachments/B8HTM85T/fulltext/images/f7e984d0868583063c7435745f5f214b6b31677ae6f113b6af8fbb5992dba543.jpg)

<table><tr><td rowspan="6">BPIs (Identifying Implementation)</td><td>BPI1</td><td colspan="2">Derived process models</td></tr><tr><td>BPI2</td><td colspan="2">Resources (Control-rel.)</td></tr><tr><td>BPI3</td><td colspan="2">Number of activity types</td></tr><tr><td>BPI4</td><td colspan="2">Number of events (per timeframe)</td></tr><tr><td></td><td colspan="2">...</td></tr><tr><td>BPI16</td><td colspan="2">Activities (Outsourcing-rel.)</td></tr><tr><td rowspan="10">PPIs (Assessing process improvements)</td><td rowspan="3">Time</td><td>PPIT1</td><td>Time for cases</td></tr><tr><td>PPIT2</td><td>Time of a variant</td></tr><tr><td></td><td>...</td></tr><tr><td>Cost</td><td>PPIC1</td><td>Number of originators</td></tr><tr><td rowspan="3">Quality</td><td>PPIQ1</td><td>Matching rate</td></tr><tr><td>PPIQ2</td><td>Variation of time for cases</td></tr><tr><td></td><td>...</td></tr><tr><td rowspan="3">Flexibility</td><td>PPIF1</td><td>Number of variants</td></tr><tr><td>PPIF2</td><td>Number of relations in the process model</td></tr><tr><td>PPIF3</td><td>Number of relations in the social network</td></tr></table>

Figure 1 Overview of our methodology

This paper proposes a new framework of business process performance indicators that address the limitations identified above (see Figure 1). The development of the proposed framework starts from the process redesign heuristics suggested by Reijers and Mansar [7]. The methodology includes two sets of indicators: (i) one to identify and clearly demonstrate the implementation of the best practice, i.e., Best Practice Implementation indicators (BPIs), and (ii) one to assess process improvements yielded by its application, i.e., Process Performance Indicators (PPIs). In this way, the proposed methodology gives an evidence-based support to the entire business process redesign phase, covering both redesign

# ACCEPTED MANUSCRIPT

implementation (with BPIs) and more traditional process improvement evaluation (with PPIs). This addresses the limitation (ii) identified above.

The proposed framework considers process mining [8–14] as the underlying evidence-based process analysis technology. Therefore, for both types of indicators, we define how they can be calculated using process related data, i.e., event logs, using standard process mining functionality [8–14]. In doing so, we also implicitly identify what kind of process data must be collected to calculate BPIs and PPIs. This addresses limitation (i) of process performance indicators in the literature, by providing a clear link between BPIs & PPIs and the technology for calculating them objectively, i.e., process mining.

The proposed framework is relevant both from a research and a practical standpoint. From a research standpoint, besides addressing the limitations identified above, having scientific methods to assess the reliability of the knowledge base about BPR best practices accumulated thus far in the literature. While many studies advocate the use of quantitative and evidence-based mechanisms to assess business process performance [4], the assessment of BPR best practices and their effect on process performance is often qualitative, based on second-hand data, such as executive and user surveys [7,15]. As recognized by other authors, e.g. [16], a methodology to link BPR best practices to clearly defined, measurable, and repeatable PPIs is currently lacking. From a practical standpoint, the proposed framework gives process analysts and decision makers actionable tools to assess the results of their choices in BPR initiatives.

To show the applicability of the proposed methodology, we present a set of case studies of process redesign in two real-world contexts, i.e., a hospital and a travel agency.

The paper is organized as follows. The next section discusses related works and preliminaries. Section 3 and Section 4 present the methodology and its application in case studies, respectively. A discussion is provided in Section 5, and conclusions are finally drawn in Section 6.

## 2 Related work and preliminaries

This section first reviews related work in the areas of process performance measurement (Section 2.1). Then, it provides required preliminary background knowledge about process mining as a tool for process performance analysis (Section 2.2).

## 2.1 Process performance measurement

Process performance measurement has its roots in the balanced scorecard method developed by Kaplan and Norton [5], who suggested measuring process-related performance in four perspectives, i.e., finance, customer, internal business, and innovation and learning. Similar to this work, there have been other approaches that applied qualitative research method to assess process performances, such as Business Excellence Model, Cambridge Model, Integrated Performance Measurement, and Performance Pyramid [17]. In addition to the qualitative approach, researchers have tried to assess business process performance quantitatively. The existing quantitative methods have been explored in two major streams: proposing a process performance measurement framework and modeling specific process performance indicators. Kueng and Krahn [18] proposed a process performance measurement framework itself that spans from identifying process goals to improving business processes using performance measurements. Also, Kueng requirements on PPIs: quantifiability, sensitivity, linearity, reliability, efficiency, and improvementoriented. Wetzsteing et al. [3] and Popova and Sharpanskykh [6] focused on proposing how to develop individual process indicators based on a KPI ontology and an indicator modeling framework, respectively. Del-Rio-Ortega et al. [4] proposed PPINOT, i.e., a metamodel to define PPIs comprehensively. Also, they suggested how to connect elements in business processes and PPIs and provide an implementation of the metamodel using description logics. Strecker et al. [19] and Pinheiro de Lima et al. [20] proposed a performance measurement system based on PPIs.

The studies reviewed above cannot be utilized immediately to assess effects of the redesign of business processes. For example, a subset of the PPIs in the proposed methodology focuses on the process instance perspective, while BPR assessments employ only global performance measurements, such as overall process performance. Also, a distinctive trait of the methodology presented in this paper is that it provides indicators to check whether BPR is aptly applied or not. Furthermore, most of the existing works do not validate developed PPIs with real data.

## 2.2 Process mining

Process mining is a relatively young discipline focused on extracting process-oriented knowledge from event logs stored in information systems [10,13]. Processes in process mining are analyzed along four perspectives, i.e., control-flow, organizational, case, and time perspectives [13]. While the control-flow perspective mainly focuses on discovering process models or frequent episodes in an event log [10,14], the organizational and case perspectives define additional views of processes, such as the social network [9,12], i.e., a graph capturing handovers of work among resources involved in a process, or the temporal logic checker [11], i.e., to check automatically the satisfaction of particular logic constraints case by case based on information in the event log. The time perspective is more related to performance analysis by considering the timing and frequency of events in a process [8,13]. As such, it can be employed to discover bottlenecks in a process model, monitor performance of actors, and calculate workloads. Table 1 shows the overview of the techniques adopted by the framework presented in this paper.

Table 1 Process mining techniques and their objectives

<table><tr><td>Perspective</td><td>Process mining techniques</td><td>Objective</td></tr><tr><td>Control-Flow</td><td>Control-flow mining algorithms [10,14]</td><td>Discovering a process model</td></tr><tr><td>Organizational</td><td>Social network mining algorithms [12]</td><td>Discovering a social network</td></tr><tr><td></td><td>Originator by Task matrix [9]</td><td>Finding a relationship between originators &amp; tasks</td></tr><tr><td>Case</td><td>Linear Temporal Logic Checker [11]</td><td>Testing a rule or a constraint</td></tr><tr><td>Performance</td><td>Log summary [13]</td><td>Getting a summary result of an event log</td></tr><tr><td></td><td>Basic performance analysis [13]</td><td>Computing performance measures</td></tr><tr><td></td><td>Dotted chart analysis [8]</td><td>Observing all events in one glance</td></tr></table>

The remainder of this section introduces the notation used for defining performance indicators, which is based on a common notation adopted by process mining techniques.

Definition 1 (Event, Case, Event Log, Variant, Activity Relation, Originator Relation) Let A be a finite set of activities and O be a finite set of originators. Let T and ET be a finite set of timestamps and event types, respectively. $E = A \times O \times T \times E T$ is the set of events, i.e., combinations of an activity, an

# ACCEPTED MANUSCRIPT

originator, a timestamp, and an event type (e.g. $\boldsymbol { e } _ { i } = \{ a _ { i } , o _ { i } , t _ { i } , e t _ { i } \} )$ . Let ?? be an event log which has a multiset of traces and $\pmb { C } = \{ c _ { 1 } , c _ { 2 } , c _ { 3 } , \ldots , c _ { k } \}$ be the set of cases. A trace $\sigma _ { k } = \left\{ e _ { k , 1 } , e _ { k , 2 } , e _ { k , 3 } , \ldots , e _ { k , n } \right\}$ is mapped into a case $c _ { k } .$ , where $e _ { k , \mathrm { n } }$ denotes n-th event of the k-th case. Let $V = \{ v _ { 1 } , v _ { 2 } , v _ { 3 } , \ \ldots , v _ { o } \}$ be a finite set of variants where $v _ { i }$ is a nonempty subset of all possible combinations of activities. ?????? is a function mapping each ???????? to a ?????????????? $( \mathrm { e . g . ~ } v a r ( c _ { k } )$ is the variant of k-th case). Activity Relation $( \mathbf { A } \mathbf { R } ) \subseteq A \times A$ is a set of activity relations where two events have a causal relations (e.g. $a r _ { k , i j } =$ $\{ ( a _ { k , i } , a _ { k , j } ) | a _ { k , i } , a _ { k , j } \in A \}$ where $e _ { k , i }$ is the predecessor of $e _ { k , j } ~ ( \mathrm { i . e . } ~ e _ { k , i } > e _ { k , j } ) )$ . Originator Relation $( \mathbf { O R } ) \subseteq O \times O$ is a set of originator relations where two events have a causal relations (e.g. $o r _ { k , i j } =$ $\{ ( o _ { k , i } , o _ { k , j } ) | o _ { k , i } , o _ { k , j } \in O \}$ where $e _ { k , i }$ is the predecessor of $e _ { k , j } ~ ( \mathrm { i . e . } ~ e _ { k , i } > e _ { k , j } ) )$ .

## 3 Indicators for business process redesign and performance evaluation

In defining evaluation measures for best practices, our approach has a twofold goal. The first goal is to assess whether a specific best practice has been applied in a BPR initiative. To understand whether a specific effect originates from using the best practice or other factors, in fact, it is important first to be certain that a best practice has been implemented. In this regard, we define BPIs for each of the 29 best practices identified by Reijers and Mansar [7]. The second goal is to understand the impact of the application of best practices when redesigning a business process. In this regard, as previously discussed, we consider the performance dimensions: time, cost, quality, and flexibility. A summary of all best practices, BPIs, and PPIs is shown in Table 2. The table provides what PPIs can be applied for each best practice. Also, applicable PPIs (e.g., PPITs, PPICs, PPIQs, PPIFs) are defined based on the four dimensions. Here, all PPIs can be employed for each best practice, while only a couple of BPIs is applied. In addition, we give potential effects (e.g., positive(+), negative(), neutral()) of each redesign item in four dimensions suggested by Reijers and Mansar [7].

Table 2 Summary of BPIs and PPIs

<table><tr><td rowspan="2">Category</td><td rowspan="2">BP</td><td rowspan="2">BPIs</td><td colspan="4">PPIs</td></tr><tr><td>T(PPIT1~5)</td><td>C(PPIC1)</td><td>Q(PPIQ1~4)</td><td>F(PPIF1~3)</td></tr><tr><td>Customers</td><td>Contact reduction</td><td>Derived process models (BPI1)</td><td>+</td><td>-</td><td>+</td><td>•</td></tr><tr><td rowspan="2"></td><td>Integration</td><td>Derived process models (BPI1)</td><td>+</td><td>+</td><td>●</td><td>-</td></tr><tr><td>Control relocation</td><td>Resources who perform the control-related activity (BPI2)</td><td>●</td><td>-</td><td>+</td><td>●</td></tr><tr><td rowspan="5">Business process operation</td><td>Activity elimination</td><td>Number of activity types (BPI3)</td><td>+</td><td>+</td><td>-</td><td>●</td></tr><tr><td>Activity composition</td><td>Number of activity types (BPI3)</td><td>+</td><td>+</td><td>●</td><td>-</td></tr><tr><td>Case types</td><td>Derived process models (BPI1)</td><td>+</td><td>+</td><td>-</td><td>-</td></tr><tr><td>Triage</td><td>Derived process models (BPI1)</td><td>●</td><td>-</td><td>+</td><td>-</td></tr><tr><td>Order-based work</td><td>Number of events for each timeframe (BPI4)</td><td>+</td><td>-</td><td>●</td><td>●</td></tr><tr><td rowspan="4">Business process behavior</td><td>Resequencing</td><td>Derived process models (BPI1)</td><td>+</td><td>+</td><td>●</td><td>●</td></tr><tr><td>Parallelism</td><td>Derived process models (BPI1)</td><td>+</td><td>-</td><td>●</td><td>-</td></tr><tr><td>Knock-out</td><td>Derived process models (BPI1)</td><td>-</td><td>+</td><td>●</td><td>●</td></tr><tr><td>Exception</td><td>Derived process models (BPI1)</td><td>+</td><td>-</td><td>+</td><td>-</td></tr><tr><td rowspan="10">Organization</td><td>Case assignment</td><td>Number of resources for each case (BPI5)</td><td>●</td><td>●</td><td>+</td><td>-</td></tr><tr><td>Numerical involvement</td><td>Number of resources for each case (BPI5)</td><td>+</td><td>-</td><td>●</td><td>-</td></tr><tr><td>Split responsibilities</td><td>Number of events performed by each resource for activities (BPI6)</td><td>●</td><td>●</td><td>+</td><td>-</td></tr><tr><td>Flexible assignment</td><td>Number of events performed by each resource for activities (BPI7) →Allocated resources for each timeframe (BPI8)</td><td>+</td><td>-</td><td>●</td><td>+</td></tr><tr><td>Specialist-generalist</td><td>Number of events performed by each resource for activities (BPI7) → Specialist-Generalist ratio (BPI9)</td><td>+</td><td>●</td><td>+</td><td>-</td></tr><tr><td>Customer teams</td><td>Derived social networks (BPI10)</td><td>●</td><td>●</td><td>+</td><td>-</td></tr><tr><td>Extra resources</td><td>Number of resources (BPI11)</td><td>+</td><td>-</td><td>●</td><td>+</td></tr><tr><td>Empower</td><td>Derived process models (BPI1) and derived social networks (BPI10)</td><td>+</td><td>●</td><td>-</td><td>+</td></tr><tr><td>Centralization</td><td>Workloads for each resource (BPI12)</td><td>+</td><td>-</td><td>●</td><td>+</td></tr><tr><td>Case manager</td><td>Whether there exists a case manager attribute in the log (BPI13)</td><td>●</td><td>-</td><td>+</td><td>●</td></tr><tr><td rowspan="2">Information</td><td>Control addition</td><td>Derived process models (BPI1)</td><td>-</td><td>-</td><td>+</td><td>●</td></tr><tr><td>Buffering</td><td>Whether there exist any activities related to subscribing (BPI14)</td><td>+</td><td>-</td><td>●</td><td>●</td></tr><tr><td rowspan="2">Technology</td><td>Task automation</td><td>Whether resources appear in the automated activity (BPI15)</td><td>+</td><td>-</td><td>+</td><td>-</td></tr><tr><td>Integral technology</td><td>Whether there exist any changes from technologies (BPI16)</td><td>+</td><td>-</td><td>●</td><td>●</td></tr><tr><td rowspan="3">External environment</td><td>Trusted party</td><td>Whether there exist any activities related to obtaining information from outside (BPI17)</td><td>+</td><td>+</td><td>●</td><td>-</td></tr><tr><td>Outsourcing</td><td>Derived process models for internal party (BPI1)</td><td>+</td><td>+</td><td>●</td><td>-</td></tr><tr><td>Interfacing</td><td>Not applicable</td><td>+</td><td>●</td><td>+</td><td>-</td></tr></table>

## 3.1 BP Implementation indicators (BPIs)

As provided in Table 2, we define 17 BPIs for 29 best practices which suggested by Reijers and Mansar [7]. For each indicator, we also suggest suitable process mining techniques through which it can be calculated. Note that information in event logs for process mining may not be able to cover all possible BPIs. When this is the case, we suggest which additional information is needed to measure the implementation of redesigns.

# ACCEPTED MANUSCRIPT

## 3.1.1 Customer

Contact reduction concerns decreasing the number of communications with customers and integration refers to combining an existing process with a business process of customers. These best practices are related to a change of workflows; thus, they lead to a change of a process model. More in detail, contact reduction removes repetitive loops from the process, while integration removes customer-related contact reduction and the integration best practices can be checked by comparing discovered process models (BPI1) before and after BPR.

Control relocation is defined as transferring controls towards customers. The most obvious evidence of the application of this best practice is that customers, instead of internal employees, perform controlcontrol-related activities (BPI2). Process mining provides the Linear Temporal Logic (LTL) checker [11] that enables to check the satisfaction of LTL constraints in a process. For control relocation, the following constraint can be applied: eventually ((activity == “some control-related activity”) ∧ (resource == “customers”)). Moreover, other resource perspective techniques such as the organizational model mining [12] or the originator by task matrix [9] can also be used to check the implementation of this best practice. Note that activities in the event log should be classified in control-related and noncontrol-related.

## 3.1.2 Business process operation

Activity elimination implies removing unnecessary activities, while activity composition indicates integrating low-level activities into a combined activity. The application of these best practices leads to a change of the number of activity types in the process (BPI3). Therefore, the log summary [13] can be used, since it provides an overall summary of the information in an event log. The log summary results provide a decrease of the value for activity elimination and an increase of that for activity composition.

Case types distinguishes a new process when activities or sub-processes appear for a specific type of cases. Assume that a series of activities in a business process are differentiated based on two types of cases. If this best practice is implemented, it is possible to divide a process into two different processes. Therefore, control-flow mining algorithms [10,14] can be used to check the implementation of this best practice.

Triage separates a common activity into several alternative activities considering the abilities of resources or types of cases. Thus, process instances after redesign can select one of the alternative activities instead of the common activity in the as-is process. As such, the application of this best practice leads to changes in the control flow of a process. More in detail, several alternative activities will appear after the redesign and these will be connected by XOR-split/join gateways in the process model. Therefore, comparing discovered process models (BPI1) is the way to identify the implementation of the triage best practice.

Order-based work eliminates batch-processing and periodic activities in a process. To check its implementation, the number of batch-processing activities needs to be calculated in a process for each timeframe (BPI4). For example, if a hospital eliminates a test activity at a specific time window in the asis setting, e.g., between 10am and 11am, the activity is no longer highly frequent in that time frame in the to-be process model. Process mining provides the basic performance analysis plugin [13] that gives information about the frequency of events in every period (i.e., day-hour chart). Similar information is also provided in the dotted chart [8]. In the chart, batch activities can be identified by time frames crowded with several dots of the same type (e.g., color).

## 3.1.3 Business process behavior

The application of all the best practices in this category results in variations of process models. Therefore, the implementation can be checked by comparing as-is and to-be process models (BPI1).

Resequencing concerns adjusting the ordering of activities. In general, this best practice recommends moving an activity to a more appropriate place in the process, e.g., next to other activities performing similar actions in a process. For instance, once this best practice is applied, in the to-be process we will be able to observe a sequence relationship between the activity and the other activities similar to it.

Parallelism implies to put activities in parallel when possible. Thus, if the parallelism is applied, the relationship between activities in the process model changes from the sequence to the parallel. This can be observed in the to-be process model.

Knock-out concerns controlling the order of knock-out activities, i.e., activities that could terminate the execution of a process. In practice, this best practice is similar to the resequencing best practice, since it resequencing, however, both the locations of knock-outs in a process model and the termination probability of each knock-out activity should be investigated. Based on these measures, it should be checked whether the termination probability is higher as the knock-out activity is put closer to the start.

Exception implies to isolate exceptional cases in a business process. Identifying the application of the exception is similar to integration in Section 3.1.1, since it makes newly added activities or sub-processes for exceptional cases that do not exist in the as-is process model. Therefore, it requires checking the presence of newly added activities or sub-processes for exceptional cases in the to-be process model.

## 3.1.4 Organization

Case assignment concerns making resources perform as many activities as possible in a case. Checking the implementation of this best practice requires measuring the number of resources involved per case. As a result of applying the best practice, a smaller number of resources work together in an individual case. The number of resources involved per case (BPI5) can be obtained from the basic performance analysis [13].

Numerical involvement concerns minimizing the number of resources in a business process. Similar to case assignment, the number of resources involved per case (BPI5) can be calculated to check the implementation of this best practice. Therefore, the number of resources involved per case decreases.

Split responsibilities concerns letting resources perform different activities and have different roles in a business process. Thus, as a result of this best practice, responsibilities in the process will be separated. To check the implementation of this best practice, the number of events executed by each resource for activities (BPI6) must be analyzed. This can be done using the originator by task matrix [9] in process mining. If resource roles are clearly separated, it yields that different resource groups conduct different activities.

Flexible assignment concerns resource allocation so that flexibility can be maximized in the near future. In other words, it means that it is better to assign works to specialists before considering generalists. Checking the implementation of this best practice requires a prerequisite step that divides originators into specialists and generalists. The originator by task matrix [9] can be used to perform this step: in the matrix, specialists will be involved in a limited number of specific activities, whereas generalists will be included in several different activities (BPI7). Once the separation between specialists and generalists has been made, the dotted chart [8] can be used to check which type of resource is allocated first to maximize flexibility (BPI8).

Specialist-generalist concerns controlling the specialist-generalist ratio in a business process. Thus, in common with the flexible assignment, a prerequisite step is to separate specialist from generalist roles or resources (BPI7). Then, the specialist-generalist ratio is calculated for the as-is and to-be process and compared (BPI9). When the implementation of this best practice is considered, organizations predetermine the proper specialist-generalist ratio based on their situations. Therefore, for this best practice, it should be checked whether or not the calculated value is different from the expected value in planning BPR.

Customer teams concerns composing worker groups from different departments to handle specific types of cases entirely. Checking the application of this best practice requires analyzing the as-is and to-be social networks (BPI10). If a working group cooperates to handle a single case, handovers of works in the social network [12] occur within the working group only. In other words, as a result of the implementation of customer teams, the derived social network shows separate working groups.

Extra resources entails increasing the number of resources in a process. As a result of the application of extra resources, the total number of resources (BPI11) in a process increases. The total number of resources involved in a process is shown in the log summary [13].

# ACCEPTED MANUSCRIPT

Empower concerns removing middle management by providing decision-making roles to workers at lower levels. The effects of this best practice are twofold. First, middle management decision-making activities in a business process are eliminated. Second, as the middle management disappears, handovers of work among resources are modified. More in detail, the handovers of work related to activities executed by middle management-oriented in the to-be social network decrease. Thus, as-is and to-be steps, e.g., a test or an inspection activity, and as-is and to-be social networks (BPI10) should be compared to detect changes in handovers of work.

Centralization entails considering resources as if they are centralized. Assume that there is a business process where resources in each location can perform limited types of activities. If the centralization best practice is implemented, these limitations will be removed. Therefore, checking the implementation of this best practice requires additional information about the location of resources. Then, based on the originator by task matrix [9] and the location information, we can check whether the works are distributed regardless of location information after applying the best practice (BPI12).

Case manager concerns designating a resource responsible for a particular case type. Checking the implementation of this best practice requires a particular attribute in event logs identifying the case manager belonging to individual cases. If this information is in event logs, then the case manager manager attribute != Ø) (BPI13).

## 3.1.5 Information

Control addition concerns adding control-related activities to check the completeness of inputs and outputs in a process by adding appropriate activities or sub-processes. To identify the implementation of the best practice, we need to compare the as-is and to-be process models (BPI1). In particular, looking for additional control-related activities in the to-be model is essential for the control addition best practice.

Buffering concerns subscribing to updates instead of requesting information when possible. An effective way to check the application of the best practice is to utilize the LTL checker [11] considering the following constraint: eventually (activity == “some subscribing-related activity”) (BPI14).

## 3.1.6 Technology

Task automation concerns making activities automated when possible. The execution of automated activities is not associated with any human resources. Therefore, the implementation of this best practice can be checked using the following constraint in the LTL checker [11]: eventually ((activity == “automated activity”) ∧ (resource == Ø)) (BPI15). Also, we can assess the implementation of this best practice using the originator by task matrix, by examining resources of automated activities.

Integral technology concerns applying new technology for elevating physical constraints. Given that the implementation of new technology may con precise way of checking the implementation that accounts for all possible scenarios. However, we argue that technology should at least have an impact on the information in event logs, introducing, for instance, new activities and/or new and more precise information that can be logged (BPI16). Therefore, qualitatively comparing as-is and to-be event logs can at least reveal whether a change has occurred in the process. If the as-is and to-be logs contain the same type of information, then we can affirm that the new technology has not been implemented or, at least, it is not used appropriately in the process.

## 3.1.7 External environment

Trusted party concerns using results from a trusted party instead of determining information oneself when possible in a process. The implementation of this best practice can be checked by analyzing whether or not there exist activities in a process that obtain information from outside. This can be monitored through LTL checker [11] as given: eventually (activity == “obtaining outside information-related activity”) (BPI17).

Outsourcing concerns contracting out a (part of a) business process. This can be checked by comparing as-is and to-be process models (BPI1). In particular, only events involving internal employees are likely to appear in an event log. Hence, through event logs it is only possible to check whether a process or part of it is no longer executed and assume that this means that it has been outsourced.

Interfacing concerns developing a standardized interface with customers. We argue that the implementation of this best practice cannot be checked using process mining techniques because it only concerns modifying the way in which communication with customers occurs, but it does not change the customers are not likely to change.

## 3.2 PPIs to assess the effect of best practices on process performance

In Table 2, we suggested 13 PPIs on the basis of four process performance measures explained by Reijers and Mansar [7]. In this section, we give a detailed explanation on PPIs including how to measure them. Table 3 provides a summary of process performance indicators.

Table 3 Process Performance Indicators (PPIs) in four perspectives

<table><tr><td>Perspective</td><td>PPI#</td><td>Explanation</td><td>Measure</td><td>Aggregation Function</td></tr><tr><td>Time</td><td>PPIT1</td><td>Time for cases in a log</td><td>Cycle Time, Operation Time, Waiting Time</td><td>AVG, MED, MAX, MIN</td></tr><tr><td></td><td>PPIT2</td><td>Time of a variant ( $v_1$ )</td><td>Cycle Time, Operation Time, Waiting Time</td><td>AVG, MED, MAX, MIN</td></tr><tr><td></td><td>PPIT3</td><td>Time of an activity ( $a_1$ )</td><td>Cycle Time, Operation Time, Waiting Time</td><td>AVG, MED, MAX, MIN</td></tr><tr><td></td><td>PPIT4</td><td>Time for events performed by an originator ( $o_1$ )</td><td>Cycle Time, Operation Time, Idle Time</td><td>AVG, MED, MAX, MIN</td></tr><tr><td></td><td>PPIT5</td><td>Time for events performed by an originator ( $o_1$ ) for an activity ( $a_1$ )</td><td>Cycle Time, Operation Time, Idle Time</td><td>AVG, MED, MAX, MIN</td></tr><tr><td>Cost</td><td>PPIC1</td><td>The total number of originators in a log</td><td>Count of elements</td><td>-</td></tr><tr><td>Quality</td><td>PPIQ1</td><td>Matching rate compared to a reference model</td><td>Matching Rate</td><td>-</td></tr><tr><td></td><td>PPIQ2</td><td>Variation of time for cases in a log</td><td>Cycle Time, Operation Time, Waiting Time</td><td>STDEV</td></tr><tr><td></td><td>PPIQ3</td><td>Variation of time of an activity ( $a_1$ )</td><td>Cycle Time, Operation Time, Waiting Time</td><td>STDEV</td></tr><tr><td></td><td>PPIQ4</td><td>Variation of time for events performed by an originator ( $o_1$ )</td><td>Cycle Time, Operation Time, Idle Time</td><td>STDEV</td></tr><tr><td>Flexibility</td><td>PPIF1</td><td>The total number of variants in a log</td><td>Count of elements</td><td>-</td></tr><tr><td></td><td>PPIF2</td><td>The total number of relations in a process model</td><td>Count of elements</td><td>-</td></tr><tr><td></td><td>PPIF3</td><td>The total number of relations in a social network</td><td>Count of elements</td><td>-</td></tr></table>

# ACCEPTED MANUSCRIPT

## 3.2.1 Time

Most BPR efforts aim at increasing the efficiency of business processes by improving time-related indicators, such as decreasing processing time and waiting time. In the proposed methodology, we suggest 5 indicators in the time perspective. All time-related indicators require a basic measure and can be aggregated using standard aggregation functions. In these indicators, the operation time is the actual process time of an activity, and waiting time is the time between the end of the previous activity and the start of the current activity.

## 3.2.2 Cost

To conduct cost-related analyses, event logs should include cost information as an event attribute (i.e., cost-enhanced event logs). If cost-enhanced logs are available, it is possible to assess the effects of $\mathrm { P P I s , }$ it is often unfeasible to obtain cost-enhanced event logs [21]. Thus, we need to develop a cost-related PPI which can be calculated from information commonly available in event logs. In this paper, we suggest an alternative indirect cost-related PPI, i.e., the total number of originators in the log (PPIC1 $( F _ { o } ) )$ since labor cost is usually one of the major cost factors. PPIC1 $\left( F _ { o } \right)$ is defined in Eq. (1).

$$
F _ {o} = \sum_ {q = 1} ^ {m} \left\{ \begin{array}{l l} 1 & \text {if} O _ {q} \in \{\sum_ {0 <   k <   | c |} \sum_ {0 <   i <   n} o _ {k, i} \} \\ 0 & \text {otherwise} \end{array} \right.\tag{1}
$$

This indicator is defined based on the assumption that all resources are full-time equivalents. Assuming that wages are similar among full-time employees, we can evaluate the costs of resources by comparing the number of resources before and after BPR.

## 3.2.3 Quality

A typical approach to evaluating the quality of a process is to check the satisfaction of customers [22]. This external quality is primarily measured through customer surveys, and it is unlikely that this information is available in event logs. For this reason, in this paper, we define PPI metrics which evaluate the extent of standardization on process flows or time-related values. In other words, our analysis focuses on internal process quality, assuming that improved internal quality, e.g., less variable process operating times, is likely to lead to improved customer satisfaction. Four process performance indicators are defined in this perspective (see Table 3).

Definition 2 (Standard Activity Relation (SAR), matching) Let ???????????????? ???????????????? ????????????????(??????) ⊆ ?? × ?? be a set of standard activity relations where two events have a causal relation. Let $M _ { a r } = \mathrm { \{ m a t c h e d . } $ , non-matched} be a set of matching results of activity relations.

????????ℎ?????? : $a r _ { k }  M _ { a r }$ is a function testing whether each activity relations are matched with standard activity relations.

Before introducing how to measure matching rates, we first define standard activity relations and a matching function provided in Definition 2. Assume that there exists a reference model of the process in an organization. We define standard activity relations as the causal activity relations identified in the reference model. Also, the matching function returns true if an activity relation in an event log is involved in standard relations of a reference model, and false otherwise. Figure 2 provides a matching example between a standard model and a log. In the figure, the reference process is $\mathtt { A } \to \mathtt { B } \to \mathtt { C } \to \mathtt { D }$ , which includes three standard relations: (A,B), (B,C), and (C,D). The event log contains 3 variants, 18 cases, and four types of activity relations: (A,B), (B,C), (C,D), and (D,A). Among the activity relations from the log, only first three relations accord with the standard relations, while (D,A) has no counterpart in the reference model.

![](/api/attachments/B8HTM85T/fulltext/images/cc481181f5aa1b3082dce0d222e8efc7d3a709f9bd86809e3df3f7c20ea6ef79.jpg)  
Figure 2 A matching example of standard relations and activity relations

Based on predefined functions, we define the matching rate $( M R _ { a r } )$ in formula (2). It represents the number of activity relations for which the matching function evaluates to true, divided by the number of activity relations.

$$
M R _ {a r} = \frac \sum_ {0 <   k \leq | c |} \sum_ {0 <   i <   j \leq n} \left\{ \begin{array}{c c} 1 & c _ {k} \in L \land e _ {k , i} , e _ {k , j} \in c _ {k} \land e _ {k , i} > e _ {k , j} \land m a t c h i n g (a r _ {k , i j}) = ^ {\prime} m a t c h e d ^ {\prime} \\ 0 & o t h e r w i s e \\ \sum_ {0 <   k \leq | c |} \sum_ {0 <   i <   j \leq n} \left\{ \begin{array}{c c} 1 & c _ {k} \in L \land e _ {k , i} , e _ {k , j} \in c _ {k} \land e _ {k , i} > e _ {k , j} \\ 0 & o t h e r w i s e \end{array} \right. \end{array} \right.\tag{2}
$$

According to Eq. (2), in the above example, among 33 activity relations, 30 activity relations are matched with the standard relations; thus the matching rate is 0.91 (i.e., 30/33).

Indicators PPIQ2, PPIQ3, and PPIQ4 are similar to PPIT2, PPIT3, and PPIT4, but using the standard deviation as aggregation function. These indicators are used to evaluate how diverse are the variations of the time values in the process, per activity, and per resource. Lower standard deviation values entail more stable, streamlined, or standardized processes. As remarked before, more streamlined processes are likely to lead to higher customer satisfaction [23]. Different quality-related indicators may be adopted, such as success rate or failure rate of an activity or a case, cancellation rate, yield rate (for manufacturing processes), or repurchase rate. Information to calculate these indicators, however, is not commonly available in standard event logs that can be handled by process mining tools.

## 3.2.4 Flexibility

Flexibility evaluates the ability of a process of reacting to changes and handling unexpected situations. To assess flexibility, we introduce three indicators, i.e., PPIF1, PPIF2, and, PPIF3, presented in Table 3. PPIF1 $( F _ { v } )$ , the total number of variants in logs, is defined in Eq. (3).

$$
F _ {v} = \sum_ {r = 1} ^ {o} \left\{ \begin{array}{l l} 1 & \text {if V_{r} \in\{\sum_{0 <   k <   |c|} var(c_{k})} \\ 0 & \text {otherwise} \end{array} \right.\tag{3}
$$

In the formula, a variant is a finite set of traces; thus, a high number of variants indicates that logs have diverse case patterns. In other words, a business process with many variants has the ability to handle different types cases. PPIF2 $( F _ { a r } )$ and PPIF3 $( F _ { o r } )$ are defined in formula (4) and (5), respectively.

$$
F _ {a r} = \sum_ {0 <   k \leq | c |} \sum_ {0 <   i <   j \leq n} \left\{ \begin{array}{l l} 1 & \text {if} c _ {k} \in L \land e _ {k, i}, e _ {k, j} \in c _ {k} \land a _ {l}, a _ {m} \in A \land e _ {k, i} > e _ {k, j} \land a _ {k, i} = a _ {l} \land a _ {k, j} = a _ {m} \\ 0 & \text {otherwise} \end{array} \right.\tag{4}
$$

$$
F _ {o r} = \sum_ {0 <   k \leq | c |} \sum_ {0 <   i <   j \leq n} \left\{ \begin{array}{l l} 1 & \text {if} c _ {k} \in L \land e _ {k, i}, e _ {k, j} \in c _ {k} \land a _ {l}, a _ {m} \in A \land e _ {k, i} > e _ {k, j} \land o _ {k, i} = o _ {l} \land o _ {k, j} = o _ {m} \\ 0 & \text {otherwise} \end{array} \right.\tag{5}
$$

PPIF2 $( F _ { a r } )$ and PPIF3 $( F _ { o r } )$ assess the flexibility of a process through measures characterizing process models and social networks discovered from event logs. In particular, they focus on the complexity of the models discovered, intended as number of relations. For example, a higher value of PPIF2 signifies that the process model is more complex and able to handle a higher variety of cases with different control flow. Similarly, higher values of PPIF3 signify that more people are cooperating in the execution of a process.

## 4 Case studies

To validate the proposed framework, we have conducted case studies in two organizations, i.e., a hospital cases, we collected real-life event logs from the information systems supporting the execution of the processes under analysis before and after BPR and computed the relevant indicators proposed in this paper.

## 4.1 BPR at a hospital

## 4.1.1 Context

The first case study has been conducted at a tertiary hospital in Korea hosting about 1400 beds and 40 operation rooms. The extra resources best practice was applied to improve outpatient processes in the clinical neuroscience center and payment processes in the hospital. Two separate applications of this best practice have been identified:

\- BP1: In April 2013, the hospital constructed the new building where the renovated clinical neuroscience center was moved. The hospital increased the number of resources, i.e., clinical doctors, in the center.

\- BP2: One of the problems in the hospital was the long delay in the payment process, and the hospital introduced payment devices (KIOSKs) to overcome this issue. In late 2013, the hospital installed an additional KIOSK.

To understand the effects of best practice implementation, we extracted EHR (Electronic Health Record) outpatient logs for a month before and after the changes. With regard to BP1, we collected one month of data at the clinical neuroscience center in July of 2012 and in July 2013. For BP2, we used event logs about patients’ payments for medical expenses through KIOSKs in July and December 2013. The lag between BPR implementations and to-be data collection was sufficiently large to avoid the transition period between the as-is and to-be configurations. A summary of the event logs of BP1 and BP2 is shown in Table 4.

Table 4 Summary of Event logs

<table><tr><td></td><td colspan="3">BP 1</td><td colspan="3">BP 2</td></tr><tr><td>Indicator</td><td>Before</td><td>After</td><td>Variation (%)</td><td>Before</td><td>After</td><td>Variation (%)</td></tr><tr><td>Number of cases</td><td>1,337</td><td>2,243</td><td>67.8</td><td>9,360</td><td>11,504</td><td>22.9</td></tr><tr><td>Number of events</td><td>6,901</td><td>11,444</td><td>65.8</td><td>66,582</td><td>81,084</td><td>21.8</td></tr><tr><td>Number of activity types</td><td>17</td><td>17</td><td>0.0</td><td>17</td><td>17</td><td>0.0</td></tr><tr><td>Number of originators</td><td>359</td><td>475</td><td>32.3</td><td>1,252</td><td>1,231</td><td>-1.7</td></tr></table>

## 4.1.2 Assessing implementation of best practices

The extra resources-related measure for checking the implementation is the total number of resources (see Table 2). Table 4 shows the number of resources before and after the best practice applied for BP1 and BP2. In the first log for BP1, originators were increased from 359 to 475 (32.3% increase), whereas there was no significant difference in the log for BP2. Considering the resources associated directly with BPR, we calculated the discrepancy in the number of clinicians involved in the neuroscience center and the number of KIOSKs located next to the payment counter. In BP1, the number of doctors who provided clinical services increased from 25 to 33 (32% increase). The indicator for BP2 also moved up from 4 to 5. Therefore, we concluded that the extra resources had been implemented appropriately in both cases.

With regard to BP1, the hospital sought to improve the ability to provide care and services to more patients by employing additional resources. Thus, we investigated the number of patients and events before and after the BPR. Table 4 shows that the neuroscience center managed about 65% more patients and events after applying BPR.

In BP2, the hospital increased the capacity to handle payment activities by adding a self-payment device. We analyzed the number of events involving each KIOSK (see Table 5). The utilization of existing KIOSKs commonly decreased, but overall the total number of events involving KIOSKs in the event log increased by 24.4%. Also, the usage of KIOSKs was more uniform after BPR, as demonstrated by the standard deviation decreasing from 731.33 to 442.34 (39.5% decrease).

Table 5 The changes of additional implementation measures in BP2

<table><tr><td>Elements (Frequency)</td><td>Before</td><td>After</td><td>Variation (%)</td></tr><tr><td>KIOSK A</td><td>3,479</td><td>2,607</td><td>-25.1</td></tr><tr><td>KIOSK B</td><td>2,654</td><td>2,540</td><td>-4.3</td></tr><tr><td>KIOSK C</td><td>2,327</td><td>2,145</td><td>-7.8</td></tr><tr><td>KIOSK D</td><td>1,437</td><td>1,494</td><td>4.0</td></tr><tr><td>KIOSK E (Added)</td><td>-</td><td>3,524</td><td>-</td></tr><tr><td>Total</td><td>9,897</td><td>12,310</td><td>24.4</td></tr><tr><td>Average</td><td>2,474.25</td><td>3,077.5</td><td>24.4</td></tr><tr><td>Standard deviation</td><td>731.33</td><td>442.34</td><td>-39.5</td></tr></table>

## 4.1.3 PPIs application

To quantitatively investigate the effect of the best practice implementations, we calculated PPIs as proposed in Section 3.2. Table 6 shows the PPIs for BP1. For the time perspective, all PPIs decreased after BPR. The average case cycle time decreased by 5%. Waiting times of key activities, such as test and consultation, which directly affects satisfaction of patients [24] decreased by about 13%. For the cost perspective, the number of clinicians increased by about 32%, which should have resulted in an increase of the expenses for the hospital. Regarding the quality perspective, we calculated the matching rate between a reference model provided by the hospital and the process model discovered from the event log using the frequency mining plugin [25]. The matching rate slightly declined after BPR, from 87% to 85%. Also, we analyzed the discrepancy of standard deviations of cycle time for cases in the log and key activities in the process. The standard deviations decreased except for the value of consultation. A lower standard deviation means that the hospital was able to provide the same level of services and it increases the satisfaction of patients, i.e., perceived quality. In the flexibility perspective, we compared the number of variants in the process. The number of process variants increased by 27.5%. However, the discovered process models were very similar and the number of relations among activities in the model remained almost the same before and after BPR (162 to 163). Thus, while the process remained almost the same, the care pathways of outpatients became more diverse and varied. In the social network, the number of relations increased by 38.6%, since the network became more complex as the number of resources involved in the process increased.

Table 6 The changes of PPIs in BP1

## ACCEPTED MANUSCRIPT

<table><tr><td>PPM</td><td>PPI</td><td>Before</td><td>After</td><td>Variation (%)</td></tr><tr><td>Time</td><td>Average of cycle time for cases in the log (min.)</td><td>79.53</td><td>75.91</td><td>-4.6</td></tr><tr><td></td><td>Average of cycle time of consultation (min.)</td><td>35.09</td><td>33.81</td><td>-3.6</td></tr><tr><td></td><td>Average of cycle time of test (min.)</td><td>11.90</td><td>10.60</td><td>-10.9</td></tr><tr><td></td><td>Average of waiting time of consultation (min.)</td><td>27.08</td><td>23.72</td><td>-12.4</td></tr><tr><td></td><td>Average of waiting time of test (min.)</td><td>7.71</td><td>6.61</td><td>-14.3</td></tr><tr><td>Cost</td><td>The number of doctors in the log</td><td>25</td><td>33</td><td>32.0</td></tr><tr><td>Quality</td><td>The matching rate compared to the reference model</td><td>0.87</td><td>0.85</td><td>-2.3</td></tr><tr><td></td><td>Standard deviation of cycle time for cases in the log (min.)</td><td>99.88</td><td>84.11</td><td>-15.8</td></tr><tr><td></td><td>Standard deviation of cycle time of consultation (min.)</td><td>27.91</td><td>30.16</td><td>8.1</td></tr><tr><td></td><td>Standard deviation of cycle time of consultation registration</td><td>73.58</td><td>65.48</td><td>-11.0</td></tr><tr><td></td><td>Standard deviation of cycle time of test (min.)</td><td>17.42</td><td>16.68</td><td>-4.2</td></tr><tr><td></td><td>Standard deviation of cycle time of test registration (min.)</td><td>63.89</td><td>45.72</td><td>-28.4</td></tr><tr><td>Flexibility</td><td>The total number of variants in the log</td><td>494</td><td>630</td><td>27.5</td></tr><tr><td></td><td>The total number of relations in the process model</td><td>162</td><td>163</td><td>0.6</td></tr><tr><td></td><td>The total number of relations in the social network</td><td>2,840</td><td>3,936</td><td>38.6</td></tr></table>

Table 7 shows the PPIs for BP2. The average of cycle time for cases and that of the payment activities decreased by about 6%. Regarding the cost perspective, the number of KIOSKs increased, which should have resulted in an increase of the costs for the hospital. For the quality perspective, the standard deviation for cases in the log decreased slightly from 90.76 to 88.68. However, the standard deviation of the cycle time of the payment slightly increased; thus, we were not able to identify stabilization of payment cycle time according to the growth of KIOSKs. In the flexibility perspective, the number of variants in the log and the number of rel s in the social network increased after BPR. However, there was no noticeable difference in the number of relations in the process model, since the new KIOSK did not change the control flow of the process.

Table 7 The changes of PPIs in BP2

<table><tr><td>PPM</td><td>PPI</td><td>Before</td><td>After</td><td>Variation (%)</td></tr><tr><td>Time</td><td>Average of cycle time for cases in the log (min.)</td><td>85.86</td><td>80.78</td><td>-5.9</td></tr><tr><td></td><td>Average of cycle time of variant 1* (min.)</td><td>39.5</td><td>32</td><td>-19.0</td></tr><tr><td></td><td>Average of cycle time of variant 2* (min.)</td><td>35.4</td><td>36.2</td><td>2.3</td></tr><tr><td></td><td>Average of cycle time of variant 3* (min.)</td><td>37.5</td><td>35.9</td><td>-4.3</td></tr><tr><td></td><td>Average of cycle time of payment (min.)</td><td>9.07</td><td>8.42</td><td>-7.2</td></tr><tr><td></td><td>Average of cycle time of KIOSK A (min.)</td><td>10.86</td><td>9.47</td><td>-12.8</td></tr><tr><td></td><td>Average of cycle time of KIOSK B (min.)</td><td>5.8</td><td>5.16</td><td>-11.0</td></tr><tr><td></td><td>Average of cycle time of KIOSK C (min.)</td><td>10.28</td><td>8.46</td><td>-17.7</td></tr><tr><td></td><td>Average of cycle time of KIOSK D (min.)</td><td>8.81</td><td>10.25</td><td>16.3</td></tr><tr><td></td><td>Average of cycle time of KIOSK E (min.)</td><td>-</td><td>9.18</td><td>(added)</td></tr></table>

## ACCEPTED MANUSCRIPT

<table><tr><td>Cost</td><td>The number of KIOSKs in the log</td><td>4</td><td>5</td><td>25.0</td></tr><tr><td>Quality</td><td>Standard deviation of cycle time for cases in the log (min.)</td><td>90.76</td><td>88.68</td><td>-2.3</td></tr><tr><td></td><td>Standard deviation of cycle time of payment (min.)</td><td>23.44</td><td>25</td><td>6.7</td></tr><tr><td></td><td>Standard deviation of cycle time of KIOSK A (min.)</td><td>23.74</td><td>26.83</td><td>13.0</td></tr><tr><td></td><td>Standard deviation of cycle time of KIOSK B (min.)</td><td>12.68</td><td>8.99</td><td>-29.1</td></tr><tr><td></td><td>Standard deviation of cycle time of KIOSK C (min.)</td><td>27.24</td><td>24.19</td><td>-11.2</td></tr><tr><td></td><td>Standard deviation of cycle time of KIOSK D (min.)</td><td>19.47</td><td>23.78</td><td>22.1</td></tr><tr><td></td><td>Standard deviation of cycle time of KIOSK E (min.)</td><td>-</td><td>21.44</td><td>(added)</td></tr><tr><td>Flexibility</td><td>The total number of variants in the log</td><td>2,913</td><td>3,224</td><td>10.7</td></tr><tr><td></td><td>The total number of relations in the process model</td><td>218</td><td>228</td><td>4.6</td></tr><tr><td></td><td>The total number of relations in the social network</td><td>9,377</td><td>10,575</td><td>12.8</td></tr></table>

<sup>\*</sup>variant 1: Registration → Consultation → Scheduling → Payment → Prescription printing → Treatment  
variant 2: Registration → Consultation → Scheduling → Payment → Prescription printing  
variant 3: Registration → Consultation → Payment → Prescription printing

## 4.1.4 Organizational relevance

The best practice implementation yielded positive effects on the time perspective PPIs in both BP1 and BP2, particularly concerning the average cycle time of the main activities in both cases, i.e., test and consultation in BP1 and payment in BP2. Concerning the cost perspective, both cases showed that adding more resources implied a noticeable increase of costs. Note that the analysis did not cover other costs that were incurred for the implementation of the best practice and for which there was no trace in the event log, e.g., the cost of constructing a new building in BP1 and the costs of relocating the payment devices in BP2. Overall, we concluded that BPR led to negative effects in the cost perspective in both cases. In the quality perspective, PPIs showed both positive and negative effects resulting from the application of the best practice. In BP1, standard deviations of most of the time-related values remained roughly unchanged, except for the matching rate and the time-related values of the consultation activity, which decreased. Similar to BP1, only some of the time-related values in BP2 decreased, and others indicated the opposite effect. Thus, we could not conclude whether the implementation of the best practice had a positive or negative effect on the process. Regarding flexibility, we found that BPR led to an increase of process flexibility in both BP1 and BP2.

To summarize, the application of the increase resource best practice in BP1 and BP2 lead to the following effects on the process: Time – positive, Cost – negative, Quality – neutral, and Flexibility – positive. This evaluation coincides with the suggestions made by Reijers and Mansar [7] for the same best practice.

## 4.2 BPR at a travel agency

## 4.2.1 Context

The second case study was conducted in one of the largest travel agencies in Korea. The company tried to improve the efficiency of the customer reservation change process by applying two best practices: numerical involvement and split responsibilities.

Figure 3 depicts the change of the reservation change process. In the “as-is” process, customers had to wait a long time to modify a reservation since multiple originators with different roles were engaged in the process. For example, if customers wanted to change a hotel reservation, they first contacted the agent where they had made the booking. The agent forwarded the information to a salesperson or an operator who handed over the details to a product developer. After that, the product developer changed the reservation. To notify the customers, information from the product developer flew back to the agent through the salespersons/operators. An additional limitation of the as-is process was the lack of clear separation of the roles of salespersons and operators. Their responsibilities, e.g., managing reservations, consulting, managing agencies, were not exactly overlapping, but very similar.

The numerical involvement best practice was implemented by excluding the salespersons and product developers from the reservation change process and allowing operators to interact with local branches directly. Also, by separating the roles of salespersons and operators, the agency reassigned operators based on regions of travel products, e.g., Europe or Asia. In this way, the split responsibilities best practice was also implemented. As a result, the process becomes more streamlined, as shown in Figure 3.

![](/api/attachments/B8HTM85T/fulltext/images/7210771d2aaa966cd079940693ad86765b4ecb71e04cfa8eaa09e6c16d35836d.jpg)  
Figure 3 The change of the reservation change process

In October 2014, the agency applied BPR to a limited number of agents and operators as a pilot project. We collected two months of data from May to June of 2014 (before BPR) and from November to December of 2014 (after BPR). Table 8 shows the summary of the extracted logs.

Table 8 Summary of Event logs

<table><tr><td>Indicator</td><td>Before</td><td>After</td><td>Variation (%)</td></tr><tr><td>Number of cases</td><td>48,185</td><td>30,766</td><td>-36.2</td></tr><tr><td>Number of events</td><td>314,592</td><td>216,633</td><td>-31.1</td></tr><tr><td>Number of activities</td><td>37</td><td>43</td><td>16.2</td></tr><tr><td>Number of originators</td><td>2,154</td><td>1,671</td><td>-22.4</td></tr></table>

## 4.2.2 Assessing implementation of best practices

First, to check whether the numerical involvement best practice was implemented, we calculated the number of roles of originators per case as presented in Table 2. As a result, the value decreased from 2.61 to 2.42, i.e., 7% decrease. Therefore, we concluded that numerical involvement was implemented in this case. Regarding the split responsibilities, we analyzed the frequency of each activity performed by salespersons and operators. We grouped activities conducted by salespersons and operators into five highlevel activities, i.e., managing reservation, consulting for products, settlement, follow-up management, and managing agencies. After BPR, operators focused on managing reservations and follow-up management, while salespersons dealt with managing agencies and settlement. Therefore, we concluded that the split responsibilities best practice was also implemented in the process.

## 4.2.3 PPIs application

The summary of PPIs evaluation in the four perspectives is presented in Table 9. In the time perspective, we compared the average cycle time of cases before and after BPR. As a result, there was a 3.1% decrease in the average cycle time. With regard to the cost perspective, the number of originators in the log decreased from 2,154 to 1,671 (22.4% decrease). For the quality perspective, the standard deviation of cycle time for cases in the log declined by 2.8% after BPR. There was a 37% reduction in the number of variants, which indicated the process became streamlined by eliminating some of the variants involving the roles removed from the process. Furthermore, there was no substantial difference in the number of relations in the process models before and after applied BPR. Eventually, the number of relations in the social network decreased by 46.0%, which was expected as a consequence of eliminating specific roles.

Table 9 The changes of PPIs in Tour agency case

<table><tr><td>PPM</td><td>PPI</td><td>Before</td><td>After</td><td>Variation (%)</td></tr><tr><td>Time</td><td>Average cycle time for cases in the log (days)</td><td>6.69</td><td>6.48</td><td>-3.1</td></tr><tr><td>Cost</td><td>The number of originators in the log</td><td>2,154</td><td>1,671</td><td>-22.4</td></tr><tr><td>Quality</td><td>Standard deviation of cycle time for cases in the log (days)</td><td>9.62</td><td>9.35</td><td>-2.8</td></tr><tr><td>Flexibility</td><td>The total number of variants in the log</td><td>18,190</td><td>11,467</td><td>-37.0</td></tr><tr><td></td><td>The total number of relations in the process model</td><td>987</td><td>990</td><td>0.3</td></tr><tr><td></td><td>The total number of relations in the social network</td><td>12,497</td><td>6,754</td><td>-46.0</td></tr></table>

## 4.2.4 Organizational relevance

Among the four process performance measures, BPR had a positive effect on the time and the quality perspective. This was because both the average and the standard deviation of cycle time for cases in the log were decreased. About the cost perspective, the number of resources engaged in the process decreased. In other words, the company was able to reallocate a part of their human resources no longer involved in the process to other duties. Based on this consideration, we can conclude that the BPR had a positive effect on the cost perspective. For the flexibility perspective, the effect of BPR was negative. As the process became more streamlined, the overall number of process variants and handover of works all decreased. The effect of BPR in this second case study can be summarized as follows: Time – positive, Cost – positive, Quality – positive, and Flexibility – negative.

Regarding the applied best practices, Reijers and Mansar suggest the following effects:

 Numerical involvement – Time: positive, Cost: negative, Quality: neutral, Flexibility: negative

 Split responsibilities – Time: neutral, Cost: neutral, Quality: positive, Flexibility: negative Although in our case study it is not possible to clearly separate the effects of individual best practices, we argue that the results of our case study support the suggestions of Reijers and Mansar [7] regarding the time, quality, and flexibility perspective. Our results appear to contradict the suggestions regarding the cost perspective. This is because the application of the split responsibilities best practice allowed the tour agency to reallocate resources to different duties. The cost savings derived from the reallocation outpace any costs that could have been incurred to reduce the numerical involvement of resources in the process.

# ACCEPTED MANUSCRIPT

## 5 Discussion

## 5.1 Comparison with existing works on process performance measurements

To clarify the distinctive traits of our framework, we first compare it in depth with the state of the art approaches that measure process performance. Table 10 provides this detailed comparison, which occurs along five criteria: whether an approach is qualitative or quantitative (Research Method), whether it detailed explanations for each indicator, including how to calculate it or what data should be collected (Providing Details for Measures), whether the indicators are defined for specific evidence (Defining Measures for Evidence), and whether it gives tooling supports that address implemented tools or any guidance (Tooling Support).

Table 10 Comparison of our proposal with the existing works

<table><tr><td>Proposal</td><td>Research Method</td><td>Specifying Indicators</td><td>Providing Details for Measures</td><td>Defining Measures for ‘Evidence”</td><td>Tooling Support</td></tr><tr><td>[5]</td><td>Qualitative</td><td>√</td><td>X</td><td>X</td><td>X</td></tr><tr><td>[19,20]</td><td>Quantitative</td><td>X</td><td>X</td><td>X</td><td>√</td></tr><tr><td>[6]</td><td>Quantitative</td><td>√</td><td>X</td><td>X</td><td>X</td></tr><tr><td>[3]</td><td>Quantitative</td><td>√</td><td>X</td><td>X</td><td>√</td></tr><tr><td>[4]</td><td>Quantitative</td><td>√</td><td>√</td><td>X</td><td>√</td></tr><tr><td>Our proposal</td><td>Quantitative</td><td>√</td><td>√</td><td>√</td><td>√</td></tr></table>

Some proposals adopt a qualitative research method, measuring business process performances using second-hand data. Several limitations are associated with these approaches, i.e., there is a lack of reliability and objectiveness due to human interpretation of second-hand data, it normally takes a long time to collect survey-based performance results, and it is usually complex extract information about process performance from such data. A subset of existing works only focuses on providing a holistic viewpoint, defining broad and coarse-grained levels for quantitative assessments of business processes. These approaches tend not to define specific features or indicators that can be directly be used by practitioners to evaluate business processes. Other approaches do not specify in depth which type of data should be collected, how to calculate process indicators and do not provide any type of tooling supports.

# ACCEPTED MANUSCRIPT

In other words, they only focus on defining process performance measurement, but they do not consider the evidence required to calculate indicators can be generated and collected. Compared to the reviewed existing works, our framework follows the quantitative research method and provides decision-makers with an implicit information about what data to collect and how to analyze performance indicators. Also, the proposed framework defines business process implementation indicators. As such, our framework gives an evidence-based support to the redesign phase in the business process lifecycle.

## 5.2 Comparison with existing works that assess effects of redesigns

We explicitly compare our approach with existing works that assess effects of business process redesigns. Table 11 provides this detailed comparisons along five criteria: whether the research method adopted is qualitative or quantitative (Research Method), whether it has the ability to assess that redesign methods are clearly demonstrated (Implementation Checking), whether it provides the ability to assess effects and improvements yielded by BPR (Performance Measurements), whether it provides detailed performance indicators (Detailed Indicators), and whether it gives tooling supports (Tooling Support). The latter two are applicable only when an approach adopts a quantitative research method.

Table 11 Comparison of our proposal with the existing works

<table><tr><td rowspan="2">Proposal</td><td rowspan="2">Research Method</td><td rowspan="2">Implementation Checking</td><td colspan="4">Performance Measurements</td><td rowspan="2">Detailed Indicators</td><td rowspan="2">Tooling Support</td></tr><tr><td>Time</td><td>Cost</td><td>Quality</td><td>Flexibility</td></tr><tr><td>[26,27]</td><td>Qualitative</td><td>X</td><td>✓</td><td>✓</td><td>✓</td><td>X</td><td>N/A</td><td>N/A</td></tr><tr><td>[28,29]</td><td>Qualitative</td><td>X</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>N/A</td><td>N/A</td></tr><tr><td>[30]</td><td>Qualitative</td><td>✓(Survey)</td><td>X</td><td>X</td><td>✓</td><td>X</td><td>N/A</td><td>N/A</td></tr><tr><td>[31]</td><td>Qualitative</td><td>✓(Survey)</td><td>X</td><td>✓</td><td>✓</td><td>X</td><td>N/A</td><td>N/A</td></tr><tr><td>[32]</td><td>Qualitative</td><td>✓(Survey)</td><td>✓</td><td>✓</td><td>✓</td><td>X</td><td>N/A</td><td>N/A</td></tr><tr><td>[33,34]</td><td>Quantitative</td><td>X</td><td>✓</td><td>X</td><td>X</td><td>X</td><td>✓</td><td>✓</td></tr><tr><td>[35]</td><td>Quantitative</td><td>X</td><td>✓</td><td>X</td><td>✓</td><td>✓</td><td>✓</td><td>X</td></tr><tr><td>[36]</td><td>Quantitative</td><td>X</td><td>X</td><td>✓</td><td>✓</td><td>X</td><td>✓</td><td>X</td></tr><tr><td>Our proposal</td><td>Quantitative</td><td>✓(Indicator-based)</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr></table>

Most existing approaches use qualitative-based evaluations using surveys. In other words, the only evidence about BPR implementation provided is the opinion of people involved in the redesign phase. In contrast to this, our framework enables assessing quantitatively the implementation of BPR, through a set of implementation indicators for each best practice. In terms of the effects of BPR, existing works only cover a subset of the performance measures, while our framework provides a systematic evaluation covering the four perspectives of time, cost, quality, and flexibility. Lastly, providing specific performance indicators and a tooling support that gives a guidance how to evaluate redesigns using process mining techniques can also be considered as a distinctiveness of our approach.

## 5.3 Limitations

Our work also has several limitations. From a methodological standpoint, the defined indicators need to be validated in the design phase. The suggested indicators were based on the literature review and the experience of the authors. As such, their robustness can be improved by implementing a validation phase involving other experts in the indicators design phase. Also, our framework can be extended by defining additional BPI indicators for other BPR best practice not considered by Reijers and Mansar [7] and by including a mechanism for generating domain specific PPIs. Furthermore, additional PPIs can be dimension since it is generally unachievable to obtain cost-enhanced logs. However, if event logs including cost information are available, we can define more direct cost-related PPIs. Therefore, future research should extend our framework to cover more effective and practical indicators.

As far as the case study approach is concerned, case studies enable us to cover only a limited set of best practices and their execution has suffered from several difficulties. Most importantly, it has been challenging to obtain enough data before and after the redesign due to security issues, e.g., data anonymization, and to determine an appropriate scope for data extraction considering constraints such as the time of redesign, the amount of data, and other external seasonal patterns. Moreover, the choice of case studies in tourism and health care has facilitated the task of collecting and interpreting data. While process mining techniques have been applied extensively and successfully in the service industry, other industries, such as manufacturing or product development, are largely untested from this point of view. Collecting data and transforming them in a suitable format for analysis using process mining technique may be challenging. Based on the nature of the problem at hand, however, we argue that case studies still

# ACCEPTED MANUSCRIPT

represent the best validation method in this context and future research should strive to develop new case studies to cover a larger set of BPR best practices. Another limitation lies in the lack of statistical analysis characterizing our results. In our case studies, in fact, we only compare the raw data obtained from process mining before and after BPR. While this is giving enough evidence to support or challenge the theoretical interpretation of the effects of BPR best practices, future research should extend our methodology to a more rigorous statistical evaluation of the results.

Finally, we are working to embed our methodology into process mining tools to provide support for BPR practitioners. Existing tools can be extended to automatically compute the values of PPIs given as-is and to-be event logs and the list of best practices applied. Additionally, advanced data visualization techniques can be investigated to facilitate the assessment of BPR initiatives by decision makers less familiar with process mining techniques and tools.

## 6 Conclusions

This paper has proposed a structured approach to assessing the implementation and benefits of business process redesign best practices based on established process analysis techniques, i.e. process mining. The proposed framework has been validated using case studies in a hospital and a tour agency, focusing on the best practices of extra resources (human and physical), numerical involvement and split responsibilities. The results obtained substantially agree with the conclusions drawn in the literature about the effect of best practices in the time, cost, quality and flexibility perspectives on process performance. The proposed framework, while contributing to the body of literature concerned with the validation of BPR best practices, also represents a ready to use tool for practitioners to conduct advanced BPR process analysis. Our work has important implications for both research and practice. From an academic research standpoint, the proposed framework provides a sound and verified method to assess the implementation of BPR best practices univocally. As such, it shifts the paradigm of BPR best practice evaluation towards evidence-based decision making. BPR best practices have been assessed in previous work often based on second-hand data, such as process participants and executive interviews [15,37]. Our framework enables the assessment of BPR best practices based on evidence, i.e., data collected from process executions.

Moreover, the proposed framework can be applied by other researchers to improve the knowledge base about BPR best practice effectiveness. This enables building a large-scale knowledge repository based on case studies that have performed BPR assessments. Such a repository may collect information such as service sectors, relevant business processes, goals of redesigns, applied redesign heuristics, utilized BPIs and PPIs, and application results of case studies. This information allows to improve continuously our knowledge about the effectiveness of different process redesign best practices and possibly to define new evidence-based process redesign best practices.

A further contribution of this paper is to link the realms of business process redesign and process mining. While process mining has been used extensively to discover business processes and analyze their conformance to business requirements [13], it has not been used so far for assessing business process redesign in a structured and reusable manner. This is particularly relevant in the modern world, in which increasing amount of data about business operations are available and in which decision making is shifting paradigmatically towards being evidence-based.

As far as implications for practice are concerned, the proposed methodology gives practitioners a ready to use tool to assess process redesign improvements. Process mining is becoming an increasingly reports in [38] that 75% of interviewed business decision-makers are aware of process mining and are using it in their daily routine or planning to use it in the next year. Also, while conducting our case studies, we noted an increasing sensibility of executives to understand the evidence provided by process mining tools, which facilitated the communication of our results.

As future works, we plan to work on a tool to support the application of the proposed methodology. Furthermore, as an extension of this tool, a method that recommends appropriate best practices based on the value of PPIs would also be beneficial. More in detail, process data may be traced continuously, i.e., in real-time, and effective best practices may be continuously suggested and assessed considering the status of a business process. More case studies should also be conducted to cover a larger set of BPR best practices for further validation.

## Acknowledgements

This work was supported by the National Research Foundation of Korea (NRF) funded by the Ministry of Education, Science and Technology (No. NRF-2014K1A3A7A03073707).

## References

[1] P. Harmon, The scope and evolution of business process management, in: Handb. Bus. Process Manag. 1 Introd. Methods, Inf. Syst., 2015: pp. 37–80.

[2] P. Kueng, Process performance measurement system: A tool to support process-based organizations, Total Qual. Manag. 11 (2000).

[3] B. Wetzstein, Z. Ma, F. Leymann, Towards measuring key performance indicators of semantic business processes, Lect. Notes Bus. Inf. Process. 7 LNBIP (2008) 227–238.

[4] A. Del-Río-Ortega, M. Resinas, C. Cabanillas, A. Ruiz-Cortés, On the definition and design-time analysis of process performance indicators, Inf. Syst. 38 (2013).

[5] R.S. Kaplan, D.P. Norton, The balanced scorecard: translating strategy into action, Harvard Business Press, 1996.

[6] V. Popova, A. Sharpanskykh, Modeling organizational performance indicators, Inf. Syst. 35 (2010) 505–527.

[7] H.A. Reijers, S.L. Mansar, Best practices in business process redesign: An overview and qualitative evaluation of successful redesign heuristics, Omega. 33 (2005) 283–306.

[8] M. Song, W.M.P. van der Aalst, Supporting process mining by showing events at a glance, in: WITS 2007 - Proceedings, 17th Annu. Work. Inf. Technol. Syst., 2007: pp. 140–145.

[9] M. Song, W.M.P. van der Aalst, Towards comprehensive support for organizational mining, Decis. Support Syst. 46 (2008) 300–317.

[10] W. Van Der Aalst, T. Weijters, L. Maruster, Workflow mining: Discovering process models from event logs, IEEE Trans. Knowl. Data Eng. 16 (2004) 1128–1142.

[11] W.M.P. van der Aalst, H.T. De Beer, B.F. van Dongen, Process mining and verification of properties: An approach based on temporal logic, Lect. Notes Comput. Sci. 3760 LNCS (2005)

130–147.

[12] W.M.P. van der Aalst, H.A. Reijers, M. Song, Discovering social networks from event logs, Comput. Support. Coop. Work. 14 (2005) 549–593.

[13] W.M.P. van der Aalst, H.A. Reijers, A.J.M.M. Weijters, B.F. van Dongen, A.K. Alves de Medeiros, M. Song, H.M.W. Verbeek, Business process mining: An industrial application, Inf. Syst. 32 (2007) 713–732.

[14] A.J.M.M. Weijters, W.M.P. van der Aalst, Rediscovering workflow models from event-based data using little thumb, Integr. Comput. Aided. Eng. 10 (2003) 151–162.

[15] M. Al-Mashari, Z. Irani, M. Zairi, Business process reengineering: A survey of international

[16] M.H. Jansen-Vullers, P.A.M. Kleingeld, M.W.N.C. Loosschilder, M. Netjes, H.A. Reijers, Tradeoffs in the performance of workflows - Quantifying the impact of best practices, in: Lect. Notes Comput. Sci. (Including Subser. Lect. Notes Artif. Intell. Lect. Notes Bioinformatics), Business Process Management Workshops, BPM 2007, 2008: pp. 108–119.

[17] M.K.D. Haffey, A.H.B. Duffy, Process performance measurement support - A critical analysis, in: Culley, S and Duffy, A and McMahon, C and Wallace, K (Ed.), Des. Manag. - Process Inf. ISSUES, 2001: pp. 561–568.

[18] P. Kueng, A.J.W. Krahn, Building a Process Performance Measurement System: Some Early Experiences, J. Sci. Ind. Res. (India). 58 (1999).

[19] S. Strecker, U. Frank, D. Heise, H. Kattenstroth, MetricM: A modeling method in support of the reflective design and use of performance measurement systems, Inf. Syst. E-Bus. Manag. 10 (2012) 241–276.

[20] E. Pinheiro De Lima, S.E. Gouvea Da Costa, J.J. Angelis, J. Munik, Performance measurement systems: A consensual analysis of their roles, Int. J. Prod. Econ. 146 (2013) 524–542.

[21] W. Nauta, Towards cost-awareness in process mining, Master’s thesis, Eindhoven University of Technology, 2011.

[22] M. Hammer, J. Champy, Reengineering the corporation: A manifesto for business revolution, Bus. Horiz. 36 (1993) 90–91.

[23] P. Lillrank, The quality of standard, routine and nonroutine processes, Organ. Stud. 24 (2003) 215–233.

[24] A. Berhane, F. Enquselassie, Patients??? preferences for attributes related to health care services at hospitals in amhara region, northern ethiopia: A discrete choice experiment, Patient Prefer. Adherence. 9 (2015) 1293–1301.

[25] M. Cho, M. Song, S. Yoo, A systematic methodology for outpatient process analysis based on process mining, Int. J. Ind. Eng. Theory Appl. Pract. 22 (2015).

[26] C.W. Shen, Effect of business process reengineering on logistics performance: A case study of Taiwan, in: Proc. IEEE Int. Conf. Autom. Logist. ICAL 2007, 2007: pp. 2887–2890.

[27] M. Terziovski, P. Fitzpatrick, P. O’Neill, Successful predictors of business process reengineering (BPR) in financial services, Int. J. Prod. Econ. 84 (2003) 35–50.

[28] S.L. Mansar, H.A. Reijers, Best practices in business process redesign: Use and impact, Bus. Process Manag. J. 13 (2007) 193–213.

[29] G. Mathew, M.M. Sulphey, S. Rajasekar, Scope of business process reengineering in public sector undertakings, Asian Soc. Sci. 11 (2015) 129–141.

[30] S. Adeyemi, M.A. Aremu, Impact assessment of business process reengineering on organisational performance, Eur. J. Soc. Sci. 7 (2008) 115–125.

[31] J. Xiang, N. Archer, B. Detlor, Business process redesign project success: The role of sociotechnical theory, Bus. Process Manag. J. 20 (2014) 773–792.

[32] S.Y. Huang, C.H. Lee, A.A. Chiu, D.C. Yen, How business process reengineering affects information technology investment and employee performance under different performance measurement, Inf. Syst. Front. 17 (2015) 1133–1144.

[33] S. Aguirre, C. Parra, J. Alvarado, Combination of Process Mining and Simulation Techniques for Business Process Redesign: A Methodological Approach, Lect. Notes Bus. Inf. Process. 162

(2013) 24–43.

[34] L. Mǎruşter, N.R.T.P. Van Beest, Redesigning business processes: A methodology based on simulation and process mining techniques, Knowl. Inf. Syst. 21 (2009) 267–297.

[35] Y. Borgianni, G. Cascini, F. Rotini, Business Process Reengineering driven by customer value: A support for undertaking decisions under uncertainty conditions, Comput. Ind. 68 (2015) 132–147.

[36] Y. Ozcelik, Do business process reengineering projects payoff? Evidence from the United States, Int. J. Proj. Manag. 28 (2010) 7–13.

[37] S.M. Siha, G.H. Saad, Business process improvement: Empirical assessment and extensions, Bus. Process Manag. J. 14 (2008) 778–802.

[38] C. Richardson, C. Mines, R. Heffner, N. Fenwick, J.R. Rymer, C. Le Clair, C. Tajima, The New

# ACCEPTED MANUSCRIPT

![](/api/attachments/B8HTM85T/fulltext/images/043cf18bdcced799b27eb2f9d29db0c93d98822caabc1542f5cc13879a4c4a4b.jpg)

Minsu Cho received the B.S. degree in technology management from UNIST (Ulsan National Institute of Science and Technology), Ulsan, South Korea, in 2013. He is currently a Ph.D. candidate in the department of Management Engineering at UNIST. His research interest includes manufacturing process analysis, clinical pathway analysis, simulation analysis based on process mining, and process mining case studies.

![](/api/attachments/B8HTM85T/fulltext/images/005cc7775f7615ea43bae157ef2b907d9466b1c1a16672059cfa836923b38dc2.jpg)

Minseok Song received his Ph.D. degree in industrial & management engineering at POSTECH (Pohang University of Science and Technology) in 2006. He is now an associate professor at the Department of Industrial & Management Engineering at POSTECH. Prior to this, he stayed at the Information Systems department of the Technology Management of Eindhoven University of Technology as a post-doctoral researcher from 2006 until 2009. Also, he was an assistant/associate professor at UNIST (Ulsan National Institute of Science and Technology). His research interest includes business process management, process mining, business analytics, simulation, and social network analysis. He has published more than 60 scientific papers in several top-level venues such as Decision Support Systems, Information Systems, Journal of

Information Technology, International Journal of Medical Informatics, etc.

![](/api/attachments/B8HTM85T/fulltext/images/b4b20b887f4331e1012c71404a080548edd93cec18111830fb5f1e484aa96bec.jpg)

Marco Comuzzi received his PhD in Information technology from Politecnico di Milano in 2007. He is now an associate professor with the School of Management Engineering at UNIST (Ulsan National Institute of Science of Technology), Republic of Korea. Prior to this, he held positions at the Eindhoven University of Technology and City, University of London. His research interests lie in the areas of business process management and enterprise systems. Most recently, his research has focused on developing innovative frequent itemset mining algorithms applied to the extraction of relevant knowledge from business process event logs and on the optimization of business process operational support. He has 50+ academic refereed publications. He serves in the IEEE SMC technical committee on Enterprise Systems since 2016, in the editorial board of Service Oriented Computing and Applications (Springer) since 2011. He serves as a regular reviewer for several academic journals, including the IEEE

Transactions on Services Computing and IEEE Transactions on Industrial Informatics. He has been involved in several EU and national collaborative research projects in the areas of enterprise systems and service-oriented computing and has experience as a consultant on enterprise systems-related issues in the private sector in Italy, UK and Korea.

![](/api/attachments/B8HTM85T/fulltext/images/a18a2b8c2c5947c2ae0884247f04846f1dd8f13b7f25d6a1074ab195d6cb6250.jpg)

Sooyoung Yoo received the Ph.D. degree in the Department of Biomedical Engineering from Seoul National University College of Medicine, Seoul, South Korea in 2008. She is currently an assistant professor at the Office of eHealth Research and Businesses at the Seoul National University Bundang Hospital, South Korea. She is also the Chief of Healthcare ICT Research Center at the hospital. She has worked in the hospital since 2009, and participated in various health IT research projects ranging from electronic health record and information sharing to mobile health and data analytics. Her major research interests include health IT interoperability standards, clinical decision support system, information extraction and information retrieval, mobile health, and smart hospital technologies.

## Highlights

This paper presents an evidence-based methodology to assess the improvements accrued by business process redesign initiatives.

 The methodology provides two sets of evaluation measures to identify implementations of best practices and to assess the process improvements.

 The methodology defines how evaluation measures are calculated from business data (i.e. event logs) using process mining techniques.

 A couple of case studies of process redesign in real world contexts demonstrates the applicability of the proposed methodology.
