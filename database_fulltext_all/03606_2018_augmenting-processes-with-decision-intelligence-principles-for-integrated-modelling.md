---
otero_id: 3606
otero_key: "VWR5J8JV"
title: "Augmenting processes with decision intelligence: Principles for integrated modelling"
authors: "Faruk Hasić; Johannes De Smedt; Jan Vanthienen"
year: "2018"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2017.12.008"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Augmenting processes with decision intelligence: Principles for integrated modelling

![](/api/attachments/VWR5J8JV/fulltext/images/60ce56439b43f0cd7eb36a7658b311de3bde00f5f408ee7fc87a96bfca670998.jpg)

Faruk Hasic´ <sup>a,</sup>\*, Johannes De Smedt<sup>b</sup>, Jan Vanthienen<sup>a</sup>

<sup>a</sup> Leuven Institute for Research on Information Systems (LIRIS), KU Leuven, Naamsestraat 69, Leuven B-3000, Belgium

<sup>b</sup> Management Science and Business Economics Group, University of Edinburgh Business School, 29 Buccleuch Place, Edinburgh, UK

## A R T I C L E I N F O

Article history: Received 21 May 2017 Received in revised form 20 December 2017 Accepted 20 December 2017 Available online xxxx

Keywords: Decision modelling DMN Process modelling BPMN Integrated modelling Separation of concerns

## A B S T R A C T

Until recently decisions were mostly modelled within the process. Such an approach was shown to impair the maintainability, scalability, and flexibility of both processes and decisions. Lately, literature is moving towards a separation of concerns between the process and decision model. Most notably, the introduction of the Decision Model and Notation (DMN) standard provides a suitable solution for filling the void of decision representation. This raises the question whether decisions and processes can easily be separated and consistently integrated. We introduce an integrated way of modelling the process, while providing a decision model which encompasses the process in its entirety, rather than focusing on local decision points only. Specifically, this paper contributes formal definitions for decision models and for the integration of processes and decisions. Additionally, inconsistencies between process and decision models are identified and we remedy those inconsistencies by establishing Five Principles for integrated Process and Decision Modelling (5PDM). The principles are subsequently illustrated and validated on a case of a Belgian accounting company.

© 2017 Elsevier B.V. All rights reserved

## 1. Introduction

The prevalence of new works on decision modelling and mining, as witnessed by the vast amount of new works on Decision Model and Notation [1–5], shows an increasing interest in documenting, modelling, and analysing the decision dimension of processes. DMN has two levels that are to be used in conjunction. Firstly, there is the decision requirement level, represented by the Decision Requirement Diagram (DRD), which depicts the requirements of decisions and the dependencies between elements involved in the decision model. Secondly, there is the decision logic level, which presents ways to specify the underlying decision logic. Usually, the decision logic is specified in decision table form. An example of a DRD is given in Fig. 1. DMN is designed as a declarative decision language. As a result DMN provides no decision resolution mechanism, as this is left to the invoking context (e.g. a process). The same holds for the processing and storage of outputs and intermediate results. Besides DMN, also the Product Data Model (PDM) [6] is a well-known language to capture the dependencies that exist between decisions and their input in workflows. DMN, however, is more driven by the decision and its rationale compared to PDM, which rather focuses on the data and its impact on the workflow.

Organisations use Business Process Management (BPM) and Decision Management (DM) to analyse, and improve their processes. The new DMN standard has the clear intention to be used in conjunction with Business Process Modelling and Notation (BPMN) [5,7-10]. Since the introduction of DMN, the general consensus is to model decisions outside processes. BPM is moving towards this separation of concerns paradigm [11] by externalising the decisions from the process flow.

The contribution of this paper is fourfold: (1) a formal definition of decision models and their relation to process models is established; (2) a list of inconsistencies between process and decision models is provided based on existing literature and on the formal definitions formulated in this paper; (3) a set of modelling guidelines is instituted to remedy the inconsistencies between process and decision models. The guidelines are contributed in the form of Five Principles for integrated Process and Decision Modelling (5PDM), in analogy with [12]; (4) the proposed modelling principles are applied and tested on a real life industry case.

This paper is structured as follows. In Section 2 the design science approach used in this paper is explained, while Section 3 handles the necessities for integrated modelling and decision modelling. In

![](/api/attachments/VWR5J8JV/fulltext/images/057d462dfe9e41f83976d1b16a3bfe85423106b9eed092eaea93bb49f8f297ef.jpg)  
Fig. 1. Decision model for customer acceptance at a Belgian accounting firm.

Section 4 a formalisation of the DMN standard and related constructs is provided which will serve as the basis for the approach of integrated modelling. Section 5 outlines challenges of integration by providing scenarios containing inconsistency concerns, followed by Section 6 which extracts principles for integrated process and decision modelling from the previous sections. In Section 7, the modelling principles are illustrated on a case from industry, and in Section 8 a systematic approach to mitigate inconsistencies is provided. Finally, Section 9 discusses the contributions and future work.

## 2. Methodology

This paper follows a design science approach [13], structured along three different cycles to obtain an artifact, being the 5PDM. First of all, the application domain and population was delineated as practitioners who develop models for integrating decisions into processes for process-aware information systems during the relevance cycle. Next, we have identified the problem of inconsistent use of decisions within processes and hence the issues that arise regarding maintainability, scalability, flexibility, understandability and reusability of decisions and processes in Sections 1 and 3. We have argued that these are the relevant issues tackled when separating concerns in modelling endeavours through the use of the separation of concerns and Service-Oriented Architecture paradigms in Sections 4 and 5. Based on the previous work of the authors, a literature review, and insights from industry (i.e. the case study environment), it was noted that there are no suitable guidelines, and that from previously produced models in research no streamlined approach was suggested. Next, an initial set of guidelines, i.e. the proposed solution artifact, were built in Section 6, according to examples from practice and research. They were validated by practitioners, as illustrated in Section 7, and previous work [5], during the design cycle. Finally, this work aims at formalising the procedure to adhere to the guidelines in Section 8 and bringing them to the body of literature on decision and process modelling. Note that these cycles work like cogs, and the relevance cycle was influenced both by insights from literature, as well as practice and design iterations, while the rigor cycle produced initial findings which were reflected in the design.

## 3. Why integrated decision and process modelling?

This section provides a motivation and related work for separating and integrating process and decision models. Additionally, we provide a running example that will be used throughout this paper.

## 3.1. Motivation and related work

In the trend towards integration several situations can be identified. Basic solutions see processes represented using only BPMN, or decisions using only DMN. This approach works only in the most straightforward cases, where no decisions are made during the process, or where only the result of a single decision is needed respectively. Slightly more evolved situations see a complete decision model represented by a single activity in a business process. This approach will only be valid for straightforward processes and decisions. Decisions are often emulated using intricate control flows, which can result in cascading gateways. These hidden decisions must be identified in the process. After identifying and modelling these decisions the resulting model must be integrated consistently with the process model. This insuficient separation of concerns results in maintainability issues [5,14-16]. In more complex processes several decisions might influence both the flow and the result. Representing these decisions and invoking them correctly in the process is crucial for a proper understanding of the process. However, these more convoluted situations have encountered little consideration in literature.

Numerous works have already dealt with data-aware processes and process consistency regarding data management. Extensions regarding data-awareness in process modelling have been proposed as well. In [17] an ontology-based knowledge-intensive approach is suggested, while [18] proposes an enhancement of declarative process models with DMN logic. Furthermore, works concerning data-aware/coloured Petri Nets are available as well, offering a formally sound approach to data and process integration [19]. However, merely focusing on data fragments is not suficient to incorporate decision-awareness into processes, which DMN aims to achieve. Furthermore, it has been illustrated how the Decision Model [20], a decision representation similar to DMN, can be used within business process models as well [21] to ofload the control flow from embedded decisions. The findings of this paper are also compatible with the Decision Model after a straightforward conversion of its decision and input blocks into DRD constructs.

The decision modelling approaches present in literature often breach the separation of concerns between control and data flow, resulting in spaghetti-like processes, thus negatively influencing maintenance, flexibility, scalability and reusability [5,7,14,15,22-26]. They do this by hard-coding and fixing the decisions in processes. Consequently, splits and joins in processes are misused to represent typical decision artifacts such as decision tables. Recently, more attention was given to the separation of processes and decision logic, as such an approach is supported by the DMN standard [1] that can be used in conjunction with BPMN [5,15,27]. Decoupling decisions and processes to stimulate flexibility, maintenance, and reusability, yet integrating decision and process models is therefore of paramount importance [5,15,28].

The separation of concerns has enjoyed plenty of attention, mainly in the domain of software modelling and design [11], but recently it has become an evident trend in BPM as well. This has moved decision management towards the paradigm of Service-Oriented Architecture (SOA), by representing decisions as externalised services. In research several conceptual decision service platforms [23,29] and ontologies [30] have been proposed. Separation of concerns and SOA offer firm motivation for keeping multi-perspective modelling tasks isolated and founded on a basis which can be used to ensure consistency. The integrated modelling and externalisation was already considered in terms of business rules [31,32]. With DMN, externalisation of decisions has become a possibility, since decisions can be encapsulated in separate decision models. These decisions are modelled separately from other concerns, such as processes, and they are implemented as a service which we call Decision as a Service (DaaS). Other information systems, e.g. process-aware information systems, can invoke the decision services from the separate decision layer on demand, i.e. Decision on Demand (DoD). Consequently, a decision model can be invoked and used as a service, adhering to the SOA paradigm and benefiting maintainability, scalability, flexibility, and reusability [5,7,8,11,15,23,24,26,28,31,33]. This emphasises the necessity for a separate, yet integrated modelling of decisions and processes.

## 3.2. Running example

In this paper the integration of decision and process modelling will be elucidated through a case study in a Belgian accounting firm. By law, Belgian accounting firms are obligated to provide a decision model to the public authorities on which they base their decision of accepting or rejecting customers. Fig. 1 depicts the decision model for customer acceptance at the firm. Customer Acceptance is decided based on the customer’s Risk Level, which on its turn depends on a Financial Position Check and a Background Check of the customer. The decision logic is externalised to this model and a complementary process model is provided in Fig. 2. This process model will have to comply with the decision model in order to correctly fulfill the customer acceptance process, i.e. the process model must be modelled consistently with the decision model. However, Fig. 2 contains plenty inconsistencies, as will be discussed in the following sections.

## 4. Formal definitions

In this section, a formal basis is given for DMN constructs and for the connection between decisions and processes, which is key for the integration.

## 4.1. Basic DMN constructs

We formalise DMN to aid us in the consistent integration of processes and decisions. We adopt the definition of decisions and decision requirement diagrams from [28,34] and expand them to include subdecisions, interfaces, and invocability.

Definition 1. A decision requirement diagram DRD is a tuple $( D _ { d m } , I D , I R )$ consisting of a finite non-empty set of decision nodes $D _ { d m } ,$ a finite non-empty set of input data nodes ID, and a finite non-empty set of directed edges IR representing the information requirements such that $I R \subseteq ( D _ { d m } \cup I D ) \times D _ { d m }$ , and $( D _ { d m } \cup I D , I R )$ is a directed acyclic graph (DAG).

The DMN specification allows a DRD to be an incomplete or partial representation of the decision requirements in a decision model. The complete set of requirements $R _ { D M }$ is derived from the set of all DRDs.

The information contained in this set can be combined into a single DRD representing the entire decision requirements level, i.e. the decision requirement graph (DRG). We extend the notion of a DRG, in such a way that a DRG is a DRD which is self-contained as explained in Definition 2.

Definition 2. A decision requirement diagram ${ D R D } \in { R _ { D M } }$ is a decision requirement graph DRG if and only if for every decision in the diagram all its modelled requirements, present in at least one diagram in $R _ { D M } ,$ , are also represented in the diagram.

According to DMN a decision is the logic used to determine an output from a given input. In BPMN a decision is an activity, i.e. the act of using the decision logic. Another common meaning is that a decision is the actual result, which we call the output of a decision. We define a decision using its essential elements.

Definition 3. A decision $d \in D _ { d m }$ is a tuple $( I _ { d } , { \cal O } _ { d } , L ) ,$ where $I \subseteq I D$ is a set of input symbols, O a set of output symbols and L the decision logic defining the relation between symbols in $I _ { d }$ and symbols in $O _ { d } .$

In case of decision tables, a commonly used reasoning construct in decision models, $I _ { d }$ and $O _ { d }$ contain the names of the input, and output elements, respectively, and L is the table itself, i.e. the set of decision rules present in the table. Note that, since a DRD is a DAG, $I _ { d } \cap O _ { d } = \beta$ . In DRDs these decisions $d _ { i }$ are represented by the decision nodes $D _ { i } \in D _ { d m }$ . We will use $D$ to refer to both a decision and its representing node in a DRD. From the definition of DRGs we can derive an important property of decisions.

From Definition 2 we know that a DRG contains exactly all information requirements of its decisions. Thus there can only exist one

![](/api/attachments/VWR5J8JV/fulltext/images/68749b813f8b79f302b871f6a3e6888023d135eccddd835751e390ccad07ca0b.jpg)  
Fig. 2. Process model for customer acceptance at a Belgian accounting firm.

DRG with D as its single top-level decision. We use $D R G _ { D }$ to denote this DRG.

To identify incorrect uses of decisions in process models it is important to know their structure. Decisions are often structured hierarchically.

Definition 4. A decision D<sup></sup> is a subdecision of decision D if and only if it is part of $D R G _ { D } ,$ , but not D itself.

This order of decisions and subdecisions can be defined by using the property that DRDs are directed acyclic graphs, from Definition 1. From this property we know that each DRD has a topological order. The concept of topological orders is closely related to partial orders resulting in Property 1.

Property 1. The topological order of a DRD induces a partial order ≤ on the decisions contained in the DRD.

When integrating decisions with processes, reducing the coupling between both is important for flexibility and maintainability, as stated by the Service-Oriented paradigm. In this paradigm, decisions are viewed as an external service which exists as a unit decoupled from the process that can be invoked by the process. In [15,33], the advantages of decision services are elaborated on, showing that the Service-Oriented paradigm enables flexibility, maintainability and scalability. This is achieved by making abstraction of decisions in the process and only connecting the process to the decisions through an interface of the decision service. In order to define the interface, Definition 5 first defines the input requirement set.

Definition 5. The decision input requirement set dirs of a decision D is the set of all sets of input data which are suficient to invoke D. dirs contains sets of input data directly or indirectly required by D. The largest set in dirs is the set of all input data nodes for which there exists a path to D in $D R G _ { D }$ . The smallest set in dirs is D<sup></sup>s input set I . dirs is constructed inductively by the following rule:

I ∈ dirs and for all $s \in d i r s _ { D }$ if there is an $i \in s$ such that $i \in O _ { D } ^ { \prime }$ for some D<sup></sup> in $D R G _ { D } ,$ then $S \setminus \{ i \} \cup I _ { D } ^ { \prime } \in d i r s _ { D }$

A decision’s interface is the combination of its input requirement set and its output set. Thus, decision interfaces can be defined as in Definition 6.

Definition 6. The interface $I F _ { D }$ of a decision D is a tuple $( d i r s _ { D } , O _ { D } )$ where dirs is the input requirement set and $O _ { D }$ the output set of D.

In DMN, decisions are constrained to have no side-effects so they comply with the principles of a service. As such each decision, with its associated interface, can be seen as a decision service. Consequently only the information available in a decision’s interface should be used in the process. Each decision in a DRD has its own output set and these sets should be disjoint. The outputs of subdecisions are identified as intermediate results. An output O is an intermediate result of decision D if and only if $O \notin \mathrm { ~ } O _ { D }$ and there exists a subdecision D<sup></sup> of D for which $O \in O _ { D ^ { \prime } }$

Executing a decision in DMN is referred to as invoking the decision. Using the definition of a decision’s interface it becomes possible to define when a decision can be invoked. Generally a decision can only be made if all required inputs are available. This is especially important when decisions are invoked in a process. Definition 7 determines the invocability of a decision.

Definition 7. A decision D is invocable from a set of data elements S if there exists an $s \in d i r s _ { D }$ such that $s \subseteq S .$ Given at least the values of all data elements in one of the sets in dirs the output of D can be determined

If a decision is invocable, so are its subdecisions, as stated in Theorem 1:

Theorem 1. If a decision D is invocable from a set of data objects S, then so are all of its subdecisions.

Proof for Theorem 1. Assume D<sup></sup> is a subdecision of D. Since there is a path from D<sup></sup> to D in $D R G _ { D }$ , there is also a path from each of the input requirements of D<sup></sup> to D. Thus, $d i r s _ { D ^ { \prime } } \subseteq d i r s _ { D } \subseteq S .$

We have formalised relevant constructs in the decision model. However, in order to discuss model integration, the decision model must be correlated with the process model. We formalise that connection in what follows.

## 4.2. The key to integration: decision activities and intermediate results

In this subsection, we propose a typology for different activities used for making decisions in processes. By doing so, we will link the decision model to the process model requiring the decisions. Decisions do not surface solely as the driver of control flow. Rather, they both encompass the routing of cases, i.e., because of decision outcomes that steer towards a certain activity tailored towards supporting its output, and the changes in the data layer of the process as well. For a consistent integration, distinguishing between decision making activities and intermediate results is of paramount importance, especially in the case of separation of concerns, where the decision model is externalised and holistically integrated with the process model. This categorisation is imperative for the identification of types of activities that are representatives of the decision model in the process model:

Definition 8. The input and output data variables of process activities in A are defined as follows:

$I : A \to V ,$ function assigning activities that deliver input for a variable,

$O : A  V ,$ function assigning activities that deliver output for a variable.

This enables the construction of the following activity types:

1. Operational activities ((no) inputs, no outputs): do not have any influence on the process’ decision dimension and only act as a performer of an action that is tied to that specific place in the control flow. They might serve as the end of a decision. They are provided with the decision inputs needed, which are not used further in the process, $A _ { o } = \{ a \in A \mid O ( a ) = \emptyset , \}$

2. Administrative activities (no inputs, outputs): they introduce decision inputs into the process, $A _ { a } = \{ a \in A \mid I ( a ) =$ ${ \mathfrak { g } } \wedge O ( a ) \not = { \mathfrak { g } } \}$

3. Decision activities (inputs, outputs): serve a decision purpose by transforming inputs into an outcome, $A _ { d } = \{ a \in A \mid I ( \nu )$ = ${ \mathfrak { g } } \wedge O ( \nu ) \neq { \mathfrak { g } } \}$

It holds that $A _ { a } \cup A _ { o } \cup A _ { d } = A .$ Typically, the decision points that are used for decision mining in processes are of the decision activity type, but tailored towards deciding which activity should be performed next based on the event labels, instead of encompassing the process in its entirety.

We can now make the connection with decisions and process models:

Definition 9. A decision in a business process can be defined as follows:

A decision in a process model, $d ^ { a } \in D _ { d m }$ is a tuple $( { \cal I } _ { d _ { a } } , { \cal O } _ { d _ { a } } , { \cal L } _ { d _ { a } } )$ where $: \subseteq A _ { d } , O _ { d _ { a } } \subseteq O ( a ) , I _ { d _ { a } } \subseteq I ( a )$ and $L _ { d _ { a } } \subseteq L .$

Now that we have defined the connection between decision activities in the process and the decision in the decision model, we can also define process-decision model consistency. Given a decision model, the process model should ensure that the decisions it invokes are invocable at that point in time, and that the decision results can only be used by the process if they have been invoked explicitly by said process. Hence, keeping in mind the previous definitions, we can define consistency for a process-decision model:

Definition 10. A process model is consistent with a decision model if and only if the following two conditions hold:

1 No intermediate results of non-invoked subdecisions are used.

2 Each (sub)decision invoked in the process, must be guaranteed to be invocable at that stage of the process.

## 5. Integration scenarios and inconsistencies

In this section we shortly describe possible integration scenarios and subsequently extrapolate inconsistencies that might occur in those scenarios.

## 5.1. Integration scenarios

Outlines of possible process-decision integration scenarios are provided by [5,28]. We refer to those papers for a full description of possible integration scenarios. Two extreme scenarios occur when there is only one model and hence no need for integration: a scenario describing a simple process without decisions, and a scenario with decisions where no actual process is needed. A third scenario with only one model is possible: both decisions and processes are present, but they are intertwined within the same model, as decisions are hard-coded within the process. This scenario clearly breaches the separation of concerns paradigm. A fourth scenario treats decisions as local concerns, as part of the decision logic pertaining to XOR-gates within the process is separately encapsulated in a decision model.

A more challenging scenario exists when, instead of dealing with local decisions, interrelated decisions span over multiple activities of the process. These decisions will influence the process in multiple ways, not only in terms of control flow at gateways. They will shape the flow of the process, the outcome of the process and the process modelling itself, as will be illustrated in the coming sections. The current scenario establishes long-distance dependencies between activities, data, control flow, and decisions in the process model, enabling a decision model to span over multiple activities instead of being contained to a single decision point in the process. Data management to liaise the data generated by activities that feed into decisions will be paramount for the integration of such process and decision models.

## 5.2. List of inconsistencies

In this subsection, possible inconsistencies that might arise between the process model and the decision model are described, as the goal is to identify potential inconsistencies and subsequently to alter the process to restore consistency. Furthermore, we formally define the (in)consistencies based on the formal definitions from the previous sections. All the inconsistencies are also directly linked with the relevant decisions and properties, which all heavily rely on the integration definition, i.e., Definition 10.

Inconsistency 1 (I1) - exclusion of decision outcomes: Not all outcomes from the decisions are included in the process model. Decisions can (re)direct the flow of the process. In an integrated process-decision model, all outcomes of the decision should be represented in the control flow if that decision redirects the process. Modelling all possible decision outcomes in the process is vital for a correct conclusion of the process.

Formally, if a decision D with an output set $O _ { D }$ in the decision model DM leads to a change in control flow in the process, then all elements of $O _ { D }$ should be present in the control flow resulting from the decision activity $A _ { D }$ which links D from DM to the process, i.e., in the state space of the process, the occurrences of $o \in O _ { D }$ lie between the occurrences of A and the accepting states. This is an outcome of Definitions 9 and 10.

Inconsistency 2 (I2) - inclusion of decision logic in the process: An inappropriate way to model parts of the decision logic is to embed decision logic in gateways. In cases where a process contains decision logic, the process is incapable of accommodating to changes in the underlying decision model. When changes occur, the process itself needs to be adapted. This occurs when the separation of concerns is not adopted strictly and thus the decision logic is not separated and encapsulated in an independent decision model. Hence, I2 does not allow for evolution of both models disjointedly.

More precisely, the decision logic L of a decision D should not be part of the process. Rather, L belongs to a decision $D \in D _ { d m } ,$ where $D _ { d m }$ is the finite non-empty set of decision nodes belonging to the DRD. Hence, the L is encapsulated in the decision model DM. The process can invoke D through its interface $I F _ { D }$ , which was defined as a tuple $( d i r s _ { D } , O _ { D } )$ . Through $I F _ { D } ,$ the process provides the input requirement set dirs needed for the enactment of $D ,$ and again through the interface, the decision model returns the output set of $D ,$ i.e. $O _ { D } .$ . Hence, the process accesses the decision model through an interface and is agnostic of the underlying decision logic. This is an outcome of Definitions 5 and 6.

Inconsistency $\textbf { 3 } ( \pmb { I 3 } )$ - exclusion of intermediate results: Inconsistencies arise when subdecisions are not modelled in the process, despite the fact that the process uses the outcome of those subdecisions. Therefore, certain parts of the flow could be disturbed and render the process inconsistent. Hence, a process model that is consistent with the decision model should ensure that all the subdecisions that contain an intermediate result which is relevant for the process execution are explicitly invoked. Explicitly, if the process uses the intermediate result $O _ { D ^ { \prime } }$ of a subdecision $D ^ { \prime }$ of higher level decision D, then D<sup></sup> must be represented by a decision activity $A _ { D ^ { \prime } }$ in the process. As such the process can invoke D<sup></sup> through the subdecision’s interface $I F _ { D ^ { \prime } }$ by providing the necessary input requirements from $d i r s _ { D ^ { \prime } }$ , after which $I F _ { D ^ { \prime } }$ will provide $O _ { D ^ { \prime } }$ to the process. This is an outcome of Definitions 6 and 10.

Inconsistency 4 (I4) - inclusion of process-unrelated subdecisions: Opposite to I3, more decisions than necessary can be included in the process. This occurs when decisions which do not contain relevant intermediate results for the process are modelled within the process. In this case the process becomes unclear and overly complex. Along with that, by modelling every subdecision in the process, the decision enactment or execution steps become fixed. This contradicts the declarative nature of decisions and reduces the flexibility provided by the decision model.

Specifically, if a subdecision D<sup></sup> with an output set $O _ { D ^ { \prime } }$  in the decision model DM does not lead to a change in control flow in the process, and if the process does not use intermediate result $O _ { D ^ { \prime } }$ of $D ^ { \prime } ,$ , then no decision activity $A _ { D ^ { \prime } }$ representing subdecision D<sup></sup> should be modelled in the process. This is an outcome of Definitions 7 and 9 .

Inconsistency 5 (I5) - unsound ordering of decision hierarchy: This occurs when the order of decision activities in the process model is contradictory to the hierarchy of decisions in the decision model. Consequently, the process cannot function correctly, as decisions are forced to enact without the prerequisite enactment of necessary subdecisions. This order of decisions and subdecisions introduces a partial order as shown in Property 1.

Hence, for two decisions $D _ { 1 }$ and $D _ { 2 }$ we say $D _ { 2 } \leq D _ { 1 }$ if and only if there is a directed path from $D _ { 2 }$ to $D _ { 1 }$ , i.e. $D _ { 2 }$ is a subdecision of $D _ { 1 }$ . Since decisions are declarative, this partial order does not dictate an execution order, but rather a requirement order. Using this order induced by Property 1 and the result from Theorem 1 we know that if a decision D is invoked in the process any decision D<sup></sup> for which $D ^ { \prime } \leq D$ will be invocable when placed directly in front of D.

Inconsistency 6 (I6) - exclusion of subdecisions affecting control flow: Depending on the outcome of certain subdecisions the control flow of the process may be diverted to include additional activities, to generate exceptions or even to lead to process termination. Excluding these subdecisions that have an influence on the control flow of the process leads to process-decision inconsistency. This inconsistency is closely related to I3: while I3 focuses on the exclusion of generated data by certain subdecisions, this inconsistency focuses on the change of control flow.

Explicitly, if a subdecision $D ^ { \prime }$ with a decision output set $O _ { D ^ { \prime } }$ in the decision model DM leads to a change in control flow in the process, then $D ^ { \prime }$ must be represented by a decision activity $A _ { D ^ { \prime } }$ in the process. Additionally, all elements of $O _ { D ^ { \prime } }$ should be reflected in the control flow following $A _ { D ^ { \prime } }$ which links the subdecision $D ^ { \prime }$ from the decision model DM to the process. This is an outcome of Definitions 7 and 9 .

Inconsistency ${ } ^ { 7 } ( I 7 )$ - absence of input data: Decision activities require prerequisites to function correctly. These prerequisites can be the outcome of certain subdecisions, as illustrated in I3, but also take the form of for instance user-generated input data. The inconsistency in this case occurs when the required input data is not available in a process when a certain decision task needs to be executed.

Formally, if the process contains a decision activity $A _ { D }$ referring to a decision D in the decision model DM, then the process must make sure that $d i r s _ { D } ,$ , i.e. the required input set for the decision $D ,$ is available within the process at the time decision activity $A _ { D }$ is executed. Only then can the process invoke decision D through its interface $I F _ { D } .$ . This is an outcome of Definitions 5 and 10.

## 6. Principles for consistent integration

In this section we provide a set of principles for integrated process and decision modelling. The principles are derived based on the integration scenarios and the formalisation from the previous sections. The principles state what should be included in a process model and what should be excluded from a process model which is linked to a corresponding decision model. Five Principles for integrated Process and Decision Modelling (5PDM) are derived to support consistency between the two models:

P1. Model all necessary decision output flows. If after enacting the decision, no output flow is dedicated to the decision outcome, the process will prove to be inconsistent. Namely, if a decision outcome that is not modelled in the control flow of the process occurs after the decision enactment, then the process cannot proceed properly.

P2. Do not include decision logic in the process model. Otherwise, maintainability, flexibility and scalability of the process might be impaired. Rather, the underlying decision logic should be externalised, encapsulated in the decision model and invoked as a service by the process.

P3. Model all subdecisions whose intermediate results are used by or are relevant for the process as decision activities in the process (P3.1). Subdecisions can only be invoked explicitly if they are represented in the process model. Using intermediate results of subdecisions that are not represented in the process leads to data inconsistency between the process and decision model. If a certain subdecision directly impacts the process control flow, the decision should be explicitly represented in the process model by a corresponding decision activity (P3.2). The decision might steer the control flow of the process towards additional activities, exception handling or even process termination. Excluding such decisions from the process leads to inconsistency. However, do not include more decision activities than necessary. Only the top-level decision and subdecisions relevant for the process enactment in terms of control flow, intermediate results and data management should be represented in the process itself. All other process-irrelevant subdecisions should not be modelled explicitly in the process (P3.3). Furthermore, modelling all subdecisions violates the declarative nature of decision modelling and reduces the flexibility provided by the decision model.

P4. Place all relevant decision activities in the correct order within the process. This is paramount for the correct enactment of the process and the underlying decisions, since intermediate results of subdecisions are often needed later in the process to enact higher level decisions. Modelling the subdecision before the higher level decision in the process is therefore vital for a correct management of intermediate results and data and hence for a proper decision and process enactment. Disregarding the decision hierarchy results in an inconsistent process-decision model.

P5. Model all data objects and intermediate results necessary for a correct process and decision enactment. The decision model depicts the hierarchy of decisions and hence the inputs and intermediate results that are necessary for enacting the decisions that are relevant for the process. If not all required data are represented in the process model, the decision activities requiring that data will not be executed properly and ensuring a sound process enactment becomes a dificulty. Thus, the process must facilitate a correct data management to be able to invoke a decision through its interface.

A short overview of the 5PDM principles is provided in Table 1.

## 7. How to integrate decision and process models

In this section, we will address the inconsistencies in the running example of Fig. 2 and rework it according to the 5PDM.

We have also developed a second example, however, due to page constraints that example is not incorporated in this paper. Rather, the example is available online in Section 3 of a technical report of our home institution [35].

## 7.1. Inclusion of all decision outcomes in the control flow

A first concern with the process model provided in Fig. 2 is that not all possible outcomes of the Accept Customer decision activity are represented in the control flow of the process model. The XOR-split that follows the Accept Customer decision activity offers flows for cases where the score is greater than 2 or smaller than 2. However, for a score equal to 2 there is no corresponding path in the process model. This situation corresponds to I1.

To remedy this inconsistency, P1 will be used. the process model should include a flow that supports the decision outcome of a score equalling 2. A solution is presented in Fig. 3, where an additional flow exits the XOR-gate and guides the indecisive cases with score equal to 2 towards the executive meeting where the customer acceptance will be resolved.

<table><tr><td>Table 15PDM.</td></tr><tr><td>Principles for integrated process-decision modelling (5PDM)</td></tr><tr><td>P1: Include all necessary decision outcomes in the process control flow</td></tr><tr><td>P2: Exclude decision logic and cascading XOR-splits from the process</td></tr><tr><td>P3: Include only subdecisions that directly influence the process</td></tr><tr><td>P3.1: Include subdecisions whose results are used in the process</td></tr><tr><td>P3.2: Include subdecisions that affect the process control flow</td></tr><tr><td>P3.3: Exclude subdecisions that are or irrelevant to the process</td></tr><tr><td>P4: Include decision hierarchy in decision activity modelling</td></tr><tr><td>P5: Include input data and intermediate results for decision enactment</td></tr></table>

## 7.2. Exclusion of decision logic from the process model

Fig. 3 includes all possible decision outcomes at the XOR decision point after Accept Customer. However, part of the decision logic is included in the process model, as the business rule that determines the outcome of decision activity Accept Customer has been hardcoded in the control flow of the XOR decision point. If the resulting score is smaller than 2, the customer will be rejected; if the score is greater than 2, the customer will eventually be accepted; and if the score equals 2, the executive meeting will address the customer acceptance issue. Suppose that along the way, this business rule for customer acceptance changes and that a score higher than 4 leads to customer acceptance; lower than 4 to customer rejection; and equal to 4 to the executive meeting. This business rule can be easily changed in the decision model. However, once the rule is changed, the process model does not longer consistently comply with the decision model. Hence, in this case, changes in the process model are necessary as well to achieve consistency. This corresponds with I2 and should be remedied by P2. Better is not to include decision logic in the process model and to simply model the outcome of the decision, as done in Fig. 4. Instead of hard-coding the scores in the control flow, only the decision outcome of accept, pending, reject is modelled in the control flow. The actual decision logic is encapsulated in the decision model, improving the agility and maintainability of the process model.

Fig. 3 contains different constructs containing decision logic. After a customer gets accepted, the XOR-gateway following the acceptance resembles a decision tree, where a distinction is made between low risk, medium risk and high risk customers. These are outcomes of the subdecision Risk Level in the decision model in Fig. 1. They all lead to similar activities of drawing up a contract. Hence, there is no need to model outcomes of a subdecision in the control flow, as this is another instance of including decision or data flows in the process model. The outcome of the Risk Level subdecision is determined in the decision model. Since the top-level decision Customer Acceptance is invoked by decision activity Accept Customer, the subdecision Risk Level is also implicitly invoked and there is no need to additionally model that part of the decision in the control flow. This is again a typical instance of I2, as control flows are often misused to represent decision logic.

This issue is treated according to P2 in Fig. 4, where the redundant gateway is excluded from the process model.

## 7.3. Inclusion of subdecisions directly influencing the process

I3 focuses on the use of intermediate decision results in the process model. In Fig. 4 the Draw up contract activity prepares a contract for an accepted customer based on the customer’s Risk assessment file, an intermediate result of the Risk Level subdecision in the decision model in Fig. 1. However, the process model in Fig. 4 does not recognise this intermediate result. Hence, drawing up the contract will not be possible since the Risk assessment file is missing. In order to include this file in the process model, the subdecision Risk Level that produces it should be modelled as a decision activity in the process. Fig. 5 includes the necessary subdecision and intermediate result in accordance with P3.1.

Additionally, in Fig. 4 the process remains the same regardless the validity of the identity verification executed by activity Check Identification Documents. In order to make the decision more reliable, the process could decide to only proceed when the identity is valid. The decision model in Fig. 1 provides a subdecision Customer Identity Verification. Instead of using the generic activity Check Identification Documents as in Fig. 4, it is preferential to use a decision activity referring to the subdecision Customer Identity Verification in the decision model. Depending on the outcome of this subdecision, i.e. whether the identity documents are valid or not, the control flow of the process can be diverted to include additional activities to ensure that a valid identity is provided before the process can continue. This is achieved in Fig. 5 by replacing the generic activity Check Identification Documents by the decision activity Verify Identity. If the documents are deemed valid, the process can continue; if deemed invalid, an additional activity is introduced that requests valid documentation. In order to remedy I6, subdecisions that have an influence on the control flow of the process, must be modelled as decision activities in the process according to P3.2.

![](/api/attachments/VWR5J8JV/fulltext/images/c3ff1af0d1506a79523fc8508d2afc521421c53f7c276ea405e73cceb3970514.jpg)  
Fig. 3. Iteration 1.

Fig. 4 includes decision activities that do not produce relevant intermediate results for the process at hand and that do not influence the control flow of the process. More precisely, Check Financial Position and Perform Background Check decision activities are represented in the process model. If the decision activity does not refer to the top-level decision or does not provide an intermediate result that is used in the process, or does not influence the control flow of the process, it is not necessary to model that decision activity. Thus, Fig. 4 contains I4. The obsolete decision activities can be excluded from the process model, as they can eventually be invoked by another higher level decision that is represented in the process model.

Fig. 5 provides a process model adhering to P3.3. Furthermore, representing all the decisions from the decision model in the process model opposes the declarative nature of the decision model, since by modelling all possible decision activities in the process, the decision execution is hard-coded in the process as well. This may lead to unnecessary delays in the process, e.g. the parallel gateway in Fig. 4 forces the process to stop until both branches are joined before the process can continue further, while in reality this may not be ideal. In Fig. 5, no such issues are present. Thus, Fig. 5 conforms to P3.1, P3.2 and P3.3, hence conforming to P3 and only containing relevant subdecisions that influence the process in terms of data, intermediate results, and control flow.

![](/api/attachments/VWR5J8JV/fulltext/images/e55d79cc819983a644970d0939cdae461a670097378301a22742838ff8fab2d3.jpg)  
Fig. 4. Iteration 2.

![](/api/attachments/VWR5J8JV/fulltext/images/e5b13b70fc33ebbc738b44178746be4ff61d2ca6bab2b7d8f28c8e9bb25120b8.jpg)  
Fig. 5. Iteration 3.

## 7.4. Inclusion of decision requirement hierarchy

A consistent process model should respect the decision requirement hierarchy provided by the decision model. Fig. 5 violates this condition, as the Determine Risk Level subdecision activity is located after the top-level decision activity Accept Customer. The decision Customer Acceptance requires the outcome of the subdecision Risk Level, and this hierarchy should be respected by the order of the decision activities in the process model. Decision activity Accept Customer will require an outcome of decision activity Determine Risk Level before the former can be executed successfully. This corresponds to I5.

To restore the decision requirement order in the process model one incorporates P4 and simply switches the two decision activities. Fig. 6 provides a model that solves this inconsistency.

## 7.5. Inclusion of relevant data and advanced data management

In Section 4.2 we defined decision activities as activities that have an input and an output, with a logical connection between the two.

Fig. 6 does not respect these definitions as it violates I7.

In Fig. 6 three decision activities are present, yet none of them has the required inputs. Only decision activity Determine Risk Level shows an output in the form of a Risk Assessment File, while other decision activities don’t exhibit any output data object. Hence, Fig. 6 shows poor data management and decisions cannot be enacted without the proper data input. Decision activity Verify Identity is linked to the subdecision Customer Identity Verification in the decision model in Fig. 1. The decision model reveals that the Customer ID is needed as input for this subdecision and the process model in Fig. 6 does not provide this indispensable data management.

Fig. 7 remedies the data management issues for all decision activities in the process model and links them to the relevant constructs in the decision model, hence conforming to P5. The activity classification is key to solving this problem. The decision model in Fig. 1 requires input data, namely Customer ID, Financial Statements, Financial Information and Public Records. As explained in Section 4.2, input data is produced by administrative activities. Those activities have no input, but do produce output. In the process in Fig. 7, the input data needed for a sound enactment are produced by administrative activities Collect Documents, Request Valid Identification and Look Up Information. The relevant data objects are then linked to the (sub)decision activities that exploit them as input data, e.g. decision activity Verify Identity uses Customer ID, produced by Collect Documents or Request Valid Identification. Each decision activity also produces an output data object, as previously specified in the definition for decision activities.

![](/api/attachments/VWR5J8JV/fulltext/images/808fce070e48b54aa84ae9ead3793058f6a0b78918a24ed9b107987ef28a2e40.jpg)  
Fig. 6. Iteration 4.

![](/api/attachments/VWR5J8JV/fulltext/images/914035a08fea25c8f09f17124b247199178e74cdbe992750aea61e73bc0c7c60.jpg)  
Fig. 7. Iteration 5.

The intermediate results of subdecision activities such as Verify Identity and Determine Risk Level are used in higher level decision activities as input, in accordance to the decision model. The intermediate result of decision activity Verify Identity, Identity Verification, is used in decision activity Determine Risk Level, together with the other input data required to enact the subdecision Risk Level in the decision model. Likewise, the intermediate result of decision activity Determine Risk Level, Risk Assessment File, is adopted as input for the decision activity Accept Customer, which corresponds with the top level decision Customer Acceptance in the decision model. The outcome of the top level decision is then used to determine whether or not to accept the customer and to draw up a contract if the customer gets accepted. A final activity classification from Section 4.2 refers to operational activities, i.e. activities that might have an input, but that produce no decision output. In Fig. 7 Draw Up Rejection Notification, Draw Up Contract and Discuss In Executive Meeting are representatives of the operational activity classification.

## 8. Resolving inconsistencies

This section deals with resolving inconsistencies and adhering to the principles of integrated modelling in a systematic way. In [36] soundness is defined to achieve P1 for isolated decision points. P1 and P2 are rather straightforward: make sure that every decision outcome can be handled by the process flow and avoid hard-coding decision logic in processes. Principle P3.2 is the complement of P1, as P1 suggests that when a decision activity that impacts the control flow is modelled, all its outcomes should be taken into account by the control flow. On the other hand, P3.2 determines that if a decision impacts the control flow of the process, it should be explicitly modelled as a decision activity in the process.

However, P3.1, P3.3, P4 and P5 require additional attention. Using the formal basis from the previous sections, we defined process-decision model consistency by two conditions in Definition 10:

1. No intermediate results of non-invoked subdecisions are used.

2. Each (sub)decision invoked in the process, must be guaranteed to be invocable at that stage of the process.

The first condition in Definition 10 refers mainly to P3.1 and P3.3, while the second condition acknowledges P4 and P5. In the following subsections we will address each of these necessary conditions.

## 8.1. Resolving the use of intermediate results

Violations against the first condition for consistency of Definition 10 can be resolved in the following steps:

1. Identify the subdecisions producing intermediate results that are used in the process, both in terms of data objects and control flow.

2. Add these subdecisions to the process model in the form of decision activities in the correct hierarchical order.

3. Do not include the remaining subdecisions into the process.

Note that this solution incorporates P3.1, P3.3 and even P4. In the running example of the Belgian Accounting firm case in Section 7, we identified that the Risk Level decision produces a Risk Assessment form as intermediate result and that said result is needed later on in the process. After identifying a subdecision with its relevant intermediate result, we incorporated the subdecision in the process under the Determine Risk Level decision activity and consequently we also took the decision hierarchy into account by placing the Determine Risk Level decision activity before the decision activity Accept Customer that represents the top level decision and that requires the outcome of the subdecision Risk Level.

The topological order derived from Fig. 1 induces that Customer Identity Verification≤ Risk Level and that Risk Level≤ Customer Acceptance according to Property 1. Thus, these decisions can be represented in the process model by their respective decision activities as long as they respect the topological order provided in the DRD. The first model adhering to all three steps with regard to resolving intermediate results in Section 7 is the one in Fig. 6. Here, the intermediate result of the relevant subdecision is identified and the corresponding decision activity is incorporated in the process, while respecting the topological order of the DRD and while excluding process-irrelevant subdecision activities.

## 8.2. Resolving invocability inconsistencies

The second condition provided in Definition 10 revolves around invocability of (sub)decisions. In order to invoke a certain decision in the process through a decision activity, all relevant data needed for invoking that decision and its subdecisions must be available. Additionally, if subdecisions of the decision that is invoked are modelled within the process by means of decision activities, the intermediate results of the subdecisions must be readily available as well. Note that this condition mainly refers to P4 and P5 i e the decision requirement hierarchy will ensure the availability of intermediate results (P4) and P5 additionally assures the presence of other indispensable input data. Hence, violations against the second condition for consistency of Definition 10 can be resolved in three simple steps:

1. Apply the topological hierarchy of decisions from the decision model to the order of modelled decision activities in the process.

2. Ensure that all input data present in the decision model is present in the process model as well, either as external data or as internal process data.

3. For every decision activity in the process make sure that all input data and intermediate results of it’s subdecision activities in the process are linked to the decision activity as input data objects.

Consider Fig. 7 and decision activity Determine Risk Level which represents the decision Risk Level from the decision model in Fig. 1. According to the decision model, the Risk Level decision requires intermediate results from its subdecisions . In order to enact Financial Position Check the Financial Statements and Financial Information input data is needed. In Fig. 7, this data is linked to the decision activity as it was generated in the process earlier on by two administrative activities, Collect Documents and Look Up Information. To enact the second subdecision, Background Check, the Public Records input data is necessary as well. This too is provided by an administrative activity of the process and linked to the decision activity Risk Level. Finally, the intermediate result of the Customer Identity Verification subdecision of Background Check is required as well. This intermediate result was produced earlier by the process, since the Verify Identity decision activity was invoked with the necessary Customer ID input provided by an administrative activity. This intermediate result, i.e. Identity Verification, is linked as an input data object to decision activity Determine Risk Level. Hence, Determine Risk Level has all input data and/or intermediate results necessary to invoke the Risk Level decision and the process can proceed. Thus, ensuring that all necessary input data and intermediate results for a decision are available before the decision is invoked, resolves the invocability inconsistency.

## 9. Conclusion and future work

This work provides insights and principles for integrated process and decision modelling. While most previous works approach the problem in a straightforward way, i.e. only considering decision points and containing decisions to one specific place in the process, we analyse decisions holistically as they can span over multiple activities and even over the entire process. A DMN formalisation and classification of process activities is provided to connect decisions to processes. Next, based on the formalisation, inconsistencies are revealed. To remedy these inconsistencies, Five Principles for Integrated Process and Decision Modelling (5PDM) were derived. The usefulness of 5PDM is illustrated through a case from a Belgian Accounting firm. Additionally, a systematic stepwise approach towards consistent integration of processes and decisions was contributed. This approach relies on a sound management of intermediate results of decisions and on correctly matching the information requirements of decisions to process data.

In future endeavours we will investigate how the decision model can further aid in refactoring the process model. Additionally, decision making across distributed processes [37] in cooperative information systems is of particular interest for Internet of Things (IoT) application areas [2].

## Appendix A. Supplementary data

Supplementary data to this article can be found online at https:/ doi.org/10.1016/j.dss.2017.12.008.

## References

[1] OMG, Decision Model and Notation 1.1, 2016.

[2] F.E. Horita, J.P. de Albuquerque, V. Marchezini, E.M. Mendiondo, Bridging the gap between decision-making and emerging big data sources: an application of a model-based framework to disaster management in Brazil, Decis. Support. Syst. 97 (2017) 12–22

[3] J.M. Perez-Alvarez, M.T. Gomez-Lopez, L. Parody, R.M. Gasca, Process instance query language to include process performance indicators in DMN, 20th International Enterprise Distributed Object Computing Workshop (EDOCW), IEEE. 2016, pp. 1–8.

[4] F. Hasic, J. De Smedt, J. Vanthienen, Towards assessing the theoretical complex-´ ity of the decision model and notation (DMN), Enterprise, Business-Process and Information Systems Modeling, CEUR. 2017, pp. 64–71.

[5] F. Hasic, L. Devadder, M. Dochez, J. Hanot, J. De Smedt, J. Vanthienen, Chal-´ lenges in refactoring processes to include decision modelling, Business Process Management Workshops Lecture Notes in Computer Science Springer. 2017

[6] I.T.P. Vanderfeesten, H.A. Reijers, W.M.P. van der Aalst, Product based workflow support: dynamic workflow execution, CAiSE, Lecture Notes in Computer Science vol. 5074, Springer. 2008, pp. 571–574.

[7] J. Vanthienen, F. Caron, J. De Smedt, Business rules, decisions and processes: five reflections upon living apart together, SIGBPS Workshop on Business Processes and Services, 2013. pp. 76–81.

[8] T. Biard, A. Le Mauff, M. Bigand, J.-P. Bourey, Separation of decision modeling from business process modeling using new “Decision Model and Notation"(DMN) for automating operational decision-making, Working Conference on Virtual Enterprises, Springer. 2015, pp. 489–496.

[9] C. Combi, B. Oliboni, A. Zardiniy, F. Zerbato, Seamless design of decisionintensive care pathways, IEEE International Conference on Healthcare Informatics (ICHI), IEEE. 2016, pp. 35–45.

[10] R. Ghlala, Z.K. Aouina, L.B. Said, BPMN decision footprint: towards decision harmony along BI process, International Conference on Information and Software Technologies, Springer. 2016, pp. 269–284.

[11] J. Gordijn, H. Akkermans, H. Van Vliet, Business modelling is not process modelling, Conceptual modeling for e-business and the web, Springer. 2000, pp. 40–51.

[12] J. Mendling, H.A. Reijers, W.M. van der Aalst, Seven process modeling guidelines (7PMG), Inf. Softw. Technol. 52 (2) (2010) 127–136.

[13] A.R. Hevner, S.T. March, J. Park, S. Ram, Design science in information systems research, MIS Q. 28 (1) (2004) 75–105.

[14] W.D. Roover, J. Vanthienen, On the relation between decision structures, tables and processes., OTM Workshops, Lecture Notes in Computer Science vol. 7046, Springer. 2011, pp. 591–598.

[15] F. Hasic, J. De Smedt, J. Vanthienen, A service-oriented architecture design´ of decision-aware information systems: decision as a service, OTM Confederated International Conferences "On the Move to Meaningful Internet Systems", Lecture Notes in Computer Science vol. 10573, Springer. 2017, pp. 353–361.

[16] F. Hasic, J. De Smedt, J. Vanthienen, Developing a modelling and mining frame-´ work for integrated processes and decisions, "On the Move to Meaningful Internet Systems". OTM 2017 Workshops, Lecture Notes in Computer Science vol. 10697, Springer. 2017,

[17] L. Rao, G. Mansingh, K.-M. Osei-Bryson, Building ontology based knowledge maps to assist business process re-engineering, Decis. Support. Syst. 52 (3) (2012) 577–589.

[18] S. Mertens, F. Gailly, G. Poels, Enhancing declarative process models with DMN decision logic Enterprise Business-Process and Information Systems Modeling, Springer. 2015, pp. 151–165.

[19] E. Serral, J. De Smedt, M. Snoeck, J. Vanthienen, Context-adaptive Petri Nets: supporting adaptation for the execution context, Expert Syst. Appl. 42 (23) (2015) 9307–9317.

[20] B. Von Halle, L. Goldberg, The Decision Model: A Business Logic Framework Linking Business and Technology, CRC Press. 2009.

[21] E. Abbasi, K. Abbasi, Business process modeling and decision model integration, Information & Communication Technologies, 2013 5th International Conference on, IEEE. 2013, pp. 1–7.

[22] B. Weber, M. Reichert, J. Mendling, H.A. Reijers, Refactoring large process model repositories, Comput. Ind. (2011) 467–486.

[23] A. Zarghami, B. Sapkota, M.Z. Eslami, M. van Sinderen, Decision as a service: separating decision-making from application process logic, EDOC, IEEE Computer Society. 2012, pp. 103–112.

[24] H. van der Aa, H. Leopold, K. Batoulis, M. Weske, H.A. Reijers, Integrated process and decision modeling for data-driven processes, International Conference on Business Process Management, Springer. 2015, pp. 405–417.

[25] F. Hasic, L. Vanwijck, J. Vanthienen, Integrating processes, cases, and deci-´ sions for knowledge-intensive process modelling, International Workshop on Practicing Open Enterprise Modeling, CEUR. 2017,

[26] L Hu. G Aghakhani E Hasić E. Serral An evaluation framework for designtime context-adaptation of process modelling languages, Practice of Enterprise Modelling (PoEM) Lecture Notes in Computer Science Springer 2017

[27] OMG, Business Process Model and Notation (BPMN) 2.0, 2011.

[28] L. Janssens, E. Bazhenova, J. De Smedt, J. Vanthienen, M. Denecker, Consistent integration of decision (DMN) and process (BPMN) models, CAiSE Forum, CEUR Workshop Proceedings vol. 1612, CEUR-WS.org. 2016, pp. 121–128.

[29] A. Bock, H. Kattenstroth, S. Overbeek, Towards a modeling method for supporting the management of organizational decision processes, Modellierung, LNI vol. 225, GI. 2014, pp. 49–64.

[30] E. Kornyshova, R. Deneckère, Decision-making ontology for information system engineering, ER, Lecture Notes in Computer Science vol. 6412, Springer. 2010, pp. 104–117.

[31] S. Goedertier, J. Vanthienen, Compliant and flexible business processes with business rules Proceedings of the CAISE Workshop on Business Process Modelling, Development, and Support BPMDS, 2006. pp. 94–103.

[32] W. Wei, M. Indulska, S. Sadiq, Guidelines for business rule modeling decisions, J. Comput. Inf. Syst. (2017) 1–11.

[33] M. Mircea, B. Ghilic-Micu, M. Stoica, An agile architecture framework that leverages the strengths of business intelligence, decision management and service orientation, Business Intelligence-Solution for Business Development, InTech. 2012, pp. 15–32.

[34] J. De Smedt, F. Hasic, J. Vanthienen, Towards a holistic discovery of decisions´ in process-aware information systems, Business Process Management, Lecture Notes in Computer Science vol. 10445, Springer. 2017, pp. 183–199.

[35] F. Hasic, J. De Smedt, J. Vanthienen, An Illustration of Five Principles for´ Integrated Process and Decision Modelling (5PDM), Tech. rep., KU Leuven. 2017,

[36] K. Batoulis, M. Weske, Soundness of decision-aware business processes, Business Process Management Forum, Springer. 2017, pp. 106–124.

[37] J. Becker, D. Pfeiffer, Solving the conflicts of distributed process modelling: towards an integrated approach., ECIS, 2008. pp. 1555–1568.

![](/api/attachments/VWR5J8JV/fulltext/images/1ab698c7c84409ecdbe60ef99ea97199682b70e2c4153282c382254558bf6d5d.jpg)

![](/api/attachments/VWR5J8JV/fulltext/images/573536dcdbdf7ea9baafe25e958e21d446cc8a77b3b2bb8533f8b644bdff521a.jpg)

![](/api/attachments/VWR5J8JV/fulltext/images/9e908b4394ea63fbab53c894a8b6785a1b9d6507d227ef69e3eb55f84ed7d2f4.jpg)  
Faruk Hasic´ received his M.Sc. degree in Business Engineering from KU Leuven and is currently performing research as a PhD candidate at the Leuven Institute for Research on Information Systems (LIRIS) in the Department of Decision Sciences and Information Management, KU Leuven. His research interests include process- and decision-aware information systems with an emphasis on the integrated modelling and mining of processes and decisions.

Johannes De Smedt obtained his PhD in Applied Economics at KU Leuven and is currently a lecturer in business analytics at the University of Edinburgh. His main research interests include flexible business process modelling and mining, and the general area of temporal item set discovery. His research has been published in leading journals such as Decision Support Systems, Expert Systems with Applications, and conferences such as Conference on Advanced Information Systems Engineering, and International Conference on Cooperative Information Systems.

Jan Vanthienen is a full professor of Information Systems in the Department of Decision Sciences and Information Management, KU Leuven. He received the PhD degree in applied economics from KU Leuven, Belgium, and has authored or co-authored numerous papers published in international journals and conference proceedings. His current research interests include modelling and mining business rules and decisions, process analytics, and information and knowledge management. Jan received an IBM Faculty Award in 2011 and the Belgian Francqui Chair 2009 at FUNDP. He is co-founder and presidentelect of the Benelux Association for Information Systems (BENAIS).
