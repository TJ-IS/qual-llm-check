---
otero_id: 8414
otero_key: "G2J77WPZ"
title: "Reliable Web service selection in choreographed environments"
authors: "San-Yih Hwang; Chien-Hsiang Lee"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.12.017"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Reliable Web service selection in choreographed environments

San-Yih Hwang ⁎, Chien-Hsiang Lee

Department of Information Management, National Sun Yat-Sen University, Kaohsiung 80424, Taiwan

a r t i c l e i n f o

Article history: Received 1 February 2012 Received in revised form 5 December 2012 Accepted 14 December 2012 Available online 23 December 2012

Keywords: Web services choreography Composite web services Quality of services Reliability Optimization of services composition

## a b s t r a c t

Previous research into Web service selection mainly uses an orchestration model, in which a single entity is responsible for the selection and invocation of various Web services. However in many application scenarios, each Web service independently performs a selection, even though achieving the business's goals demands collective, pairwise interactions across the total set of Web services. This study instead considers the Web service selection problem in a choreographed environment, in which each Web service maintains its con<sup>fi</sup>- dentiality about its collaborators and exchanges only limited amounts of information with its partners. The goal is to maximize the likelihood of completing the entire choreography in a failure-prone environment. Several experiments show that the proposed method performs similarly to a centralized method and better than three distributed Web service selection methods that involve various degrees of information about other services.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Thanks to advances in computer and communication technologies, modern organizations engage in convenient, inexpensive interactions with partners. To achieve more effective and ef<sup>fi</sup>cient collaborations with business partners, an increasing number of organizations adopt service-oriented architecture (SOA) as the principle underlying their software development and integration. The goal is to allow quick, loose coupling of a set of software components within and across organizations, in response to dynamic changes in business environments. In accordance with industry standards for SOA, organizations encapsulate applications' functions as Web services, usually based on either SOAP (Simple Object Access Protocol) or REST (Representational State Transfer) [42]. Several XML-based languages also specify the composition of Web services into processes.

There are two general descriptions of Web service compositions: orchestration and choreography. An orchestration model focuses on a single composite Web service (which is a process), and each step in the process can be realized by invoking an internal or external Web service. The dominant Web service composition language for this orchestration model is Web Services Business Process Execution Language, or WS-BPEL. To allow for a more <sup>fl</sup>exible and dynamic execution of processes, a composite Web service also can be treated as an abstract process, in which the function of each step is speci<sup>fi</sup>ed in the design and the Web service for realizing the function is determined only at runtime. In this case, the process execution engine selects and executes the set of proper Web service operations for each process. Several studies address how to select Web service using an orchestration model. For example, an optimization goal might be to shorten the response time [18], enhance reliability [10,13], increase throughput [20], or balance multiple quality of services factors [37,39].

In a choreography model however, multiple composite Web services are executed in a distributed fashion, and no single entity is in charge of all invocations of the Web services. Typical speci<sup>fi</sup>cations of a choreography model include Web Services Choreography Description Language (WS-CDL) and Business Process Model and Notation (BPMN 2.0). However, unlike WS-BPEL, an executable process language, a choreography speci<sup>fi</sup>cation serves solely to describe interactions between business processes [17]. Most existing works that include choreography models accordingly verify the correctness of a given choreography [6,8,11], without considering how to coordinate Web service execution in a choreographed environment where there is no central entity in charge of all Web service selection tasks. We therefore extend previous work [14] by considering Web service selection in a choreographed environment.

Consider the sequence of a simpli<sup>fi</sup>ed shopping scenario in Fig. 1, which starts when a customer places an order with some vendor through an online business transaction. Then, the customer expects the vendor or shipper to provide noti<sup>fi</sup>cation (i.e. via “notifyCustomer” operation) when the products are ready. In fact, customer needs the noti<sup>fi</sup>cation but does not concern who delivers it. The customer may have several vendors to choose from, and the chosen vendor can independently determine the supplier and the shipper of the products. Without proper controls though, the selected vendor may fail to notify the customer and choose a shipper that does not do so (i.e., neither the selected vendor nor the shipper provides a “notifyCustomer” operation). However, it is unrealistic to pursue centralized control of all Web service invocations, because each participant is an independent service provider that is unlikely to give up its choice of or information about its collaborators.

![](/api/attachments/G2J77WPZ/fulltext/images/c9654735fd1ba94068f0ca212793b8dcbc735309c48101bb2a7fe740f9c65461.jpg)  
Fig. 1. Sequence diagram of a simpli<sup>fi</sup>ed shopping scenario.

The need to respect the con<sup>fi</sup>dentiality of each service provider in a choreographed environment makes the Web service selection problem especially challenging.

We therefore propose a model in which each participating Web service is associated with an abstract process and capable of dynamically performing Web service selection for each step in the process, based on information it knows and that provided by collaborators. We further develop a method for each Web service to select and invoke other Web services dynamically, based on limited information about other Web services, that maximizes the likelihood of completing the entire choreography in a failure-prone environment. In summary, we offer the following contributions to the Web service selection problem in a choreographed environment:

1. Each Web service does not have the information about all the Web services in the entire choreography. Instead, a Web service only gives a summary of the behavior of itself and other partner Web services to a focal Web service, which respects the con<sup>fi</sup>dentiality of business partners.

2. In the proposed Web service selection framework for a choreography model, each participating Web service makes its Web service selection on the basis of limited information released by its partner Web services.

3. We compare the performance of several Web service selection algorithms that use different amounts of information about other Web services.

The rest of this article is structured as follows: In Section 2, we review related work on Web service selection. We de<sup>fi</sup>ne the choreography model and the dynamic Web service selection problem in Section 3. The approach to the problem is then presented in Section 4. Finally, we offer experimental results and conclusions in Sections 5 and 6, respectively.

## 2. Literature review

Orchestration and choreography describe business processes from different perspectives. Most research into Web service selection adopts an orchestration model, with a focus on a single participant that chooses and delegates some required functions to other Web services from a pool of candidate Web services, some of which possess equivalent functionalities. The choreography model instead focuses on the entire system, in which multiple processes interact. We summarize previous research into Web service selection in the following subsections.

## 2.1. Web service selection in an orchestration model

The Web service selection problem has been studied intensively in recent years, because it constitutes a complex decision with lots of factors, which fall into two categories: functional and nonfunctional. Functional properties refer to aspects of Web service recorded in their pro<sup>fi</sup>les, including operations, inputs, outputs, preconditions, and effects. Hence, much research attempts to outline methods to discover Web service whose functions meet users' needs. This area is generally referred to as Web service discovery, and most works use either ontology or information retrieval techniques to determine functional similarities across different Web services [5.25.35]. The result of Web service discovery is a list of Web services, ranked by similarity to the user's desired function.

Nonfunctional properties, also called the quality of services (QoS), include factors related to performance and business policies, such as throughput, response time, reliability, availability, <sup>fi</sup>delity, and security. Unlike functional properties, QoS measures rarely appear in the speci<sup>fi</sup>cation of Web services. Previous research has proposed architecture models that require service providers to declare the QoS of their provided Web services, which enables their registration in the UDDI repository [16,28]. Thio and Karunasekera [33] propose a mechanism to measure QoS values and store them on a Web service directory server. Kulnarattana and Rongviriyapanish [18] instead propose a QoS model that uses uncertain attributes and a nonparametric test technique to test historical QoS information from the client side, then uses the QoS values as the Web service selection criteria. Sun et al. [32] assess subjective QoS value from pair-comparisons between candidate Web services and then combine users' preference, subjective and objective QoS values, with weights by using adapted Brown–Gibson method to derive aggregated QoS value of each candidate Web service.

Given the QoS values of each individual Web service, most recent works focus on the selection of Web services as a means to satisfy the QoS requirements of a process (i.e., composite Web service). To select Web services for optimizing QoS of the entire process, Zeng et al. [38] propose computing an optimal set of Web services for each possible execution path in the process, according to a weighted combination of QoS measures. Yu et al.'s [37] scheme optimizes the end-to-end

QoS for various <sup>fl</sup>ow structures using a utility function derived from the QoS values, and the optimization problem is formulated as a general <sup>fl</sup>ow problem. Some studies instead concentrate on a single QoS measure. For example, Menasce [20] attempts to estimate the throughput of a composite Web service according to its constituent Web services and then use that throughput as a basis for selecting the Web service. Grassi and Patella's [10] framework recursively aggregates the reliability of a composite Web service, on the basis of those of its constituent Web services. Hwang et al. [13] also propose a PageRank-like algorithm to compute the aggregated reliability for each state of execution and measure the probability that a given state will lead to successful execution in a context in which each Web service may fail with some probability. They propose two dynamic strategies to select Web service that should lead to the successful completion of a given sequence of operations.

## 2.2. Web service selection in choreography model

In a choreography model, the interactions between involving participants are described and the message exchanges are also de<sup>fi</sup>ned. However, the synchronizability and realizability of the composition model has to be veri<sup>fi</sup>ed to assure that participant services can be composed to reach the given goal. Therefore, various previous works check the interaction conformance of a Web service to a given choreography, mostly based on model checking approach in either procedural speci<sup>fi</sup>cation [1,4,6,9,11,40] or declarative speci<sup>fi</sup>cation [22]. In [2,3], Baldoni et al. address the Web service selection problem in a choreography model by considering mismatched functional constraints between Web services. They adopted the concept of capability to describe the preconditions and effects of Web services, which describe the requirement of message exchange in choreography model. A logic-based reasoning approach is adopted for selecting a (complex) Web service for each role de<sup>fi</sup>ned in a choreography such that the capability requirements in the choreography model and constraints of each selected Web service are satis<sup>fi</sup>ed. All the above-mentioned works aim to choose a Web service that satis<sup>fi</sup>es functional requirements of a choreography. In contrast, the focus of this work is on the nonfunctional features of the choreography, speci<sup>fi</sup>- cally, its reliability.

The nonfunctional properties of service composition in choreography model are similar to those of orchestration model, yet QoS measurement and aggregation approaches are different. More speci<sup>fi</sup>cally, the QoS aggregation in choreography model has to do with the interactions between participants, whereas in orchestration model the aggregation is computed solely based on the QoS of individual services. Zhao et al. [41] employ a choreography language proposed by their previous work to model the behavior of Web services choreography. In their model, each activity, including assignment and interaction, possesses a set of QoS attributes. They propose three kinds of aggregation methods, namely minimal, maximal, and average, to aggregate QoS values of a Web service choreography under different control <sup>fl</sup>ows, such as basic, sequential, choice, and parallel. In addition, they estimate the cost for each individual role. Yang et al. [36] incorporate rate information, which represents the frequency of service requesting, into the choreography model. Then a continuous-time Markov chain model is derived to represent the Web service choreography. By means of PRISM, a stochastic analysis tool, the average execution time for the entire Web service choreography, the usage times for each role's channel, and the cost for each role can be computed. Both works focus on the QoS estimation for a choreography model, but they do not consider WS selection issue.

## 2.3. Distributed Web service composition

In choreographed environments, component services autonomously launch the interactions with their partners without the mediation of a centralized coordinator. Several works in distributed Web service composition consider the autonomy characteristic of services from different perspectives, such as access control and requirement negotiation. In particular, most works adopt agent-based approach to realize the autonomous behavior of services. Ermolayev et al. [7] propose an agent-based framework by which the requirements of a client can be ful<sup>fi</sup>lled by a service composition built through the requirement negotiation among the agents of candidate services. Maamar et al. [19] devise three types of agents, namely composite-service-agent, master-service-agent, and service-agent. The composition of services is centrally conducted by the composite-service-agent according to the given speci<sup>fi</sup>cation and the communication patterns between master-service-agents. During the execution time, the master-service-agent of a Web service decides whether a service instance will be created and joined to a composite service. The interactions between service instances are then conducted by service-agents. The access control for Web services in a distributed environment is addressed by She et al. [30], who consider information <sup>fl</sup>ow access control in a composite service. The information produced by a component service is guarded by back-checked mechanism and pass-on certi<sup>fi</sup>cation proposed by the authors.

Muller et al. [23] propose an interaction protocol by which the candidate services compatible with the request can communicate with each other to form a service composition. Their approach is further enhanced by Tong et al. [34] who propose a formal model to represent service agent and data dependency among candidate services. Based on the formal model, service agents communicate with the client and their partner agents via four types of messages that report the service availability and compatibility to the client. Once the client receives all required responses from available service agents, a service composition can be built. Huang et al. [12] apply SOA model to cyber physical systems, in which the involved services autonomously determine their work<sup>fl</sup>ows and cooperate in reaching the given goal. The extended SOA model allows distributed service governance including the grounding of services and concretization of work<sup>fl</sup>ow template. Mitra et al. [21] focus on the decentralized behavior of Web service composition in which there is an agent for each service, called choreographer, to store the input/output messages and invoke partner services or client service after deciding the target service of next invocation. To obtain the optimized execution sequence with minimum communication cost, the proposed approach constructs a global automaton which composes all possible execution sequences by collecting information from choreographers and identi<sup>fi</sup>es the execution sequence with the minimum communication cost. In fact, many of the previously proposed approaches determine the set of constituent Web services for a given goal in a centralized manner done by the client.

The above researches have done a plausible work to autonomously determine the work<sup>fl</sup>ow of service, to grant resources access, to negotiate the requirement of the goal, or to select services that consider communication cost. However, the con<sup>fi</sup>dentiality of service partnership is seldom considered. In this work, we mandate each service to autonomously select participating services with only partial information from their partner services and develop methods that promise to achieve high probability of successful completion.

## 3. The choreography model and problem de<sup>fi</sup>nition

In this section, we formally describe a choreography model and the Web service selection problem using the shopping example in Fig. 1 for illustration. In general, a choreography model, as de<sup>fi</sup>ned using WS-CDL or BPMN 2.0, describes collaboration among participating Web service roles by de<sup>fi</sup>ning their interactions and information exchanges from a global viewpoint. In this work, our goal is on Web service selection, and we focus on the interactions among Web services. Detailed information exchanged during interaction is thus not considered.

## 3.1. The choreography model

A choreography model focuses on observable interactions among processes. In accordance with current Web service technology, we de<sup>fi</sup>ne two types of interactions, or activities: operation invocations and operation receptions. The execution of a process may involve other types of activities, such as data movement and invocation of local atomic Web service operations, but for our purposes, we consider those activities internal and exclude them from our model.

## De<sup>fi</sup>nition 1. (Web service)

The Web service W refers to a <sup>fi</sup>nite state machine (FSM) that prescribes the legal executions of its activities. Formally, W is a tuple $( \Sigma , S , s _ { 0 } , \delta , F )$ , where

• $\scriptstyle \sum$ is a set of activities;

• S is a <sup>fi</sup>nite set of states;

• s is a state in S that represents the initial state of $W ;$

$\delta \colon S \times \sum  S$ is the transition function of the FSM, which is a partial function that returns the new state resulting from accepting an activity $a \in \Sigma$ when the Web service is in some given state; and

• F pS represents the set of <sup>fi</sup>nal states in which the interactions with W can be terminated.

## De<sup>fi</sup>nition 2. (Web service role)

A Web service role de<sup>fi</sup>nes a set of interaction patterns with other Web service roles and is associated with multiple Web services that possess similar functionalities and conform to the interaction patterns speci<sup>fi</sup>ed for the role.

There have been quite a few works that address the conformance of a Web service to a role [1,4,15,27], and we do not address this issue in this work. A Web service role constitutes an abstract service that can be realized by some (concrete) Web services. Fig. 1 shows a shopping choreography that involves four Web service roles: Customer, Vendor, Supplier, and Shipper.

## De<sup>fi</sup>nition 3. (Target Web Service)

A target Web service is the one to be activated by a client to start the entire choreography.

As Fig. 1 shows, the Web service that plays the role of Customer is the target Web service. The set of Web services involved in a choreography model is collectively a Web service community, and it includes a target Web service and several component Web services, each of which plays its own Web service role. However, not every pair of Web services communicate; in a business environment, each participant usually has a limited number of collaborating partners. To specify possible collaborations, we de<sup>fi</sup>ne a WS-invoking hierarchy.

## De<sup>fi</sup>nition 4. (WS-invoking hierarchy)

A WS-invoking hierarchy of a Web service community is a partial order of involved Web services. One Web service $W _ { j }$ is able to be invoked by another Web service $W _ { i }$ if $W _ { j }$ can be instantiated by W to perform some function that is desired by $W _ { i } .$

In this WS-invoking hierarchy, we assume that each Web service can well interact with its partner Web services, i.e., they are compatible. In other words, the correctness of the interactions between Web services in choreography model has been veri<sup>fi</sup>ed and incompatible relationships between Web services have been eliminated from WS-invoking hierarchy. Readers interested in Web service compatibility may refer to [1,4,6,8,35] for details.

## De<sup>fi</sup>nition 5. (Choreography model)

A choreography model is a three-tuple (C, R, I), in which C is a Web service community; R is a set of Web service roles, each played by some Web services in C; and I is the WS-invoking hierarchy of C.

Based on the shopping scenario in Fig. 1, we identify an example Web service community and its WS-invoking hierarchy in Figs. 2 and 3, respectively. Note that we add two more roles in our example, namely SupplierBackend and ShipperBackend, that are upstreams of Supplier and Shipper respectively. A target Web service (W1) plays the role of Customer, three Web services (W2, W3, and W4) play the role of Vendor, four Web services (W5–W8) serve as Suppliers, two Web services (W9 and W10) play SupplierBackend role, four Web services (W11–W14) are Shippers, and two Web services (W15 and W16) play ShipperBackend role. As shown, the Web services that play the same role may provide slightly different activities. We use the pre<sup>fi</sup>xes ! and ? to denote the invocation and reception of operations, respectively. Thus x.?orderRequest indicates the reception of operation orderRequest, invoked by a partner Web service identi<sup>fi</sup>ed by x.

Furthermore, we distinguish two types of operation invocations (receptions): free and bounded. A free operation invocation, bx>.!o, indicates that several Web services might be used to execute operation o, and the selected Web service is identi<sup>fi</sup>ed by x. A bounded operation invocation, denoted x.!o, instead requires a speci<sup>fi</sup>c Web service identi<sup>fi</sup>ed by x, to execute o. Similarly, a free operation reception, denotedby>.?o, means that it can be invoked by several Web services and the actual invoker is identi<sup>fi</sup>ed by y. Finally, the bounded operation reception, denoted $y . ? 0 ,$ , indicates that the Web service identi<sup>fi</sup>ed by y receives o. For example, consider W2 in Fig. 2; W2 will be instantiated when W1 invokes it using orderRequest operation. Its <sup>fi</sup>rst activitybx>.? orderRequest is a free operation reception, and x will be bounded to W1 at runtime. The next two activities of W2, namelyby>.! initiateSupplier and bz > .!initiateShipper, are free operation invocations; and the last activity x.!notifyCustomer is a bounded operation invocation on a Web service identi<sup>fi</sup>ed by x, i.e., the target Web service (W1) in our example. Thus, the free operation reception bx > .?orderRequest in W2 is matched to the free operation invocationbx>.!orderRequest in W1, and the bounded operation invocation x.!notifyCustomer of W2 is matched to the free operation receptionby>.?notifyCustomer of W1 because W1 does not specify who will deliver the noti<sup>fi</sup>cation. A bounded operation invocation usually refers to some ancestor of the identi<sup>fi</sup>ed Web service in the WS-invoking hierarchy and serves as the callback function of an asynchronous invocation. We use the notation ancestor(x, l) to denote the ancestor of x in the lth generation in Fig. 2. For example, in W10 of Fig. 2, there is an activity, ancestor(u,1).!notifyVendor, which is intended for the parent of u (i.e., the vendor). In practice, the <sup>fi</sup>rst free operation reception of each Web service corresponds to the WS-BPEL's receiving activity in which the CreateInstance attribute equals ‘Yes’. In other words, it creates a new Web service instance.

When the target Web service in a choreography model initiates, the problem of how to select a Web service incrementally to execute each subsequent free operation invocation constitutes the dynamic Web service selection problem. This problem is complicated by the con<sup>fi</sup>dentiality requirement of each participating Web service. Speci<sup>fi</sup>cally, no single entity keeps all information about the entire choreography model, and the con<sup>fi</sup>dentiality requirement of each Web service mandates that each Web service is aware of only information about its partner Web services (i.e., its parent and child Web services in the WS-invoking hierarchy) and cannot pass on the detailed partner information to others.

A Web service may malfunction or become unavailable at runtime, and the network in which Web services operate is failure prone. Invoking a Web service does not always succeed, so another partner Web service that plays the same Web service role might be chosen instead. We refer to the problem of choosing Web service at runtime as the dynamic Web service selection problem, formally de<sup>fi</sup>ned as follows:

## De<sup>fi</sup>nition 6. (Dynamic Web service selection problem)

Consider a choreography model (C, R, I), in which C contains a target Web service $W _ { t }$ and a set of component Web services $\{ W _ { 1 }$

![](/api/attachments/G2J77WPZ/fulltext/images/3a41936949b16ed893d1596178f61e2f623e4e4a0163b4854c74de32aafcb330.jpg)  
Fig. 2. Example Web service community.

$W _ { 2 } , . . . , W _ { n } \}$ . When some Web services in C are partially executed and a free operation invocation request $< _ { - } >$ .!o in $W _ { t }$ or $W _ { i }$ for some role r in R arrives, how does $W _ { t }$ or W <sup>fi</sup>nd a partner Web service $W _ { j } ,$ as speci<sup>fi</sup>ed in I, that plays the role r and contains the matching free operation reception $< _ { - } > . ? 0 ,$ such that this instantiation improves the promise of successful completion of the entire choreography, given that each Web service interaction involves a chance of failure?

## 4. Our approach

## 4.1. The framework

A Web service in a choreographed environment can play two roles: service consumer and service provider. Each Web service is a service provider when it accepts the instantiation from another Web service through some free operation reception. It may subsequently play the role of service consumer by choosing and initiating other Web services through free operation invocations during its execution. From the perspective of a single Web service, its partner Web services may be either service providers or service consumers. A Web service must acquire information about the behavior of its partners (and partners' partners) to make a good choice for its free operation invocations. However, a Web service cannot reveal detailed behavioral information about its partners to others. In Fig. 3 for example, detailed information about the supplier and shipper partners of a given vendor should not be disclosed to its customer.

![](/api/attachments/G2J77WPZ/fulltext/images/04535c4d30ba8b0ce79168aeb592ea9587a0a131637d11ff69c03245fcdcd495.jpg)  
Fig. 3. Example WS-invoking hierarchy.

Therefore, we propose that each Web service provides a summary of the activities performed by it and its ancestors (descendants) in the WS-invoking hierarchy to each of its service providers (consumers). Every Web service provides one view, which we refer to as view , for its service consumer, and it offers several $\begin{array} { r } { \boldsymbol { v } i e \boldsymbol { w } _ { \mathrm { p } } \boldsymbol { s } , } \end{array}$ one for each role of its service providers. The view of a Web service W summarizes the behavior of W and its descendants in the WS-invoking hierarchy, intended solely for the service consumers of W to facilitate better selection decision. Speci<sup>fi</sup>cally, view of W can be regarded as a FSM of activities to be matched to W's service consumers, as de<sup>fi</sup>ned in the WS-invoking hierarchy. For example, consider W3 in Fig. 2, and assume that it has only one supplier (W7) and one shipper (W13) as its partners. The view of W3 in this case contains only two sequential activities, ?orderRequest (from W3) and !notifyCustomer (from W13), to be matched to its service consumer (i.e., W1). In contrast, the view of W for a given Web service role r summarizes the behavior of W and W's ancestors in the WS-invoking hierarchy for the service providers of role r. The Web service roles may differ in their provided activities, so the view s of a given Web service may differ for different Web service roles. In our previous example, the $v i e w _ { \mathrm { p } }$ of W3 for its supplier has only one activity, ! initiateSupplier, whereas that for the shipper contains two activities, ! initiateShipper and ?notifyCustomer, because W3 and its ancestor (i.e., W1) collectively provide them, as required by the shipper's role.

When the view and $v i e w _ { \mathsf { p } }$ of all Web services have been formulated, a Web service can combine its own activities and those in the view s of its service providers and vie $ { v _ { \mathrm { p } } } S$ of its service consumers to form its view of the choreography, called a local composition. When a Web service must choose and invoke some Web service for a free operation invocation, it consults its local composition. Each invoked Web service may subsequently choose Web service for its free operation invocations by reviewing its own local composition. We discuss how to generate view and $v i e w _ { \mathrm { p } }$ for each Web service and construct local compositions in the following sections.

## 4.2. Generating view and view for each Web service

The view s of Web services in the community are constructed in a bottom-up manner. For leaf nodes in the WS-invoking hierarchy (i.e., those that do not instantiate other Web services), the view s are equivalent to their own FSMs. In addition, the target Web service, or the root in the WS-invoking hierarchy, does not need to provide view because it has no service consumers. The $v i e w _ { \mathrm { c } }$ of a Web service that is an intermediate node in the WS-invoking hierarchy can be constructed by taking as input the view of its children in the WS-invoking hierarchy, as well its own FSM. For example, view of W2 in Fig. 3 is a function of its own FSM and the view s of its service providers (W6, W11, W12, and W14). To combine a set of FSMs into a new FSM, we adopt the well-known Petri net as the intermediacy, because it offers the capability to model concurrent behavior in distributed systems. Speci<sup>fi</sup>- cally, each input FSM is <sup>fi</sup>rst converted into a Petri net, and the component Petri nets then are combined by synchronizing the corresponding operation invocations/receptions. Finally, the FSM of the resultant Petri net forms the basis of view . Each transition in $v i e w _ { \mathrm { c } }$ is then associated with a probability value that indicates the chance of a successful transition. The transition probabilities in view can help determine the transition probabilities for a local composition. We illustrate each step using the example in Figs. 2 and 3.

## 4.2.1. Creating view for a Web service

The <sup>fi</sup>rst step converts each involved FSM into a corresponding Petri net by treating states of the FSM as places on the Petri net and assigning a token in place of the initial state. Consider W2 in Figs. 2 and 3. To build its view , we combine its own FSM and the view s of W6, W11, W12, and W14. Note that the view of W11 is the same as its own FSM, because it does not instantiate other Web services. The view of W6 contains only one activity (?initiateSupplier), because its other activity (!upstreamSupplier) matches its child's (W9) activity (?upstreamSupplier). The view s of W12, and W14 can be constructed similarly. Fig. 4 shows the corresponding Petri net of each involved FSM.

In the second step, we combine these Petri nets into a global Petri net by merging the transitions with the corresponding operation invocations/ receptions. Speci<sup>fi</sup>cally, two transitions marked by !t, ?t—where !t and ?t are the (free or bounded) invocation and reception of the same operation, respectively—can be merged into a single transition whose input place set is the union of the input place sets of !t and ?t. The output place set instead is the union of the output place sets of !t and ?t. Fig. 5 shows the global Petri net obtained by combining the Petri nets in Fig. 4, in which the combined transitions are pre<sup>fi</sup>xed by ≡.

The third step is transforming the global Petri net into the corresponding FSM. It has been shown that a Petri net has an equivalent FSM [26], and we follow the same approach. Speci<sup>fi</sup>cally, each possible marking in the global Petri net is treated as a state in the corresponding FSM, and the transformation between markings in the global Petri net form the transitions in the FSM [26]. In addition, the start state of the FSM is the initial marking of the global Petri net, and its <sup>fi</sup>nal states correspond to those in which there is a token in the <sup>fi</sup>nal state of focal Web service (i.e., W2 in this example) and all other tokens are located in either the initial or the <sup>fi</sup>nal states of its child Web services. The corresponding FSM of the global Petri net in Fig. 5, called the gross FSM, is depicted in Fig. 6.

The gross FSM describes all possible interactions between the focal Web services and its descendant Web services to realize its functionality. For example, the rightmost path of Fig. 6 represents one possible execution sequence that could ful<sup>fi</sup>ll the functionality of W2, in which the following activities are executed sequentially: receiving orderRequest, invoking initiateSupplier (of W6), invoking initiateShipper (of W14), and invoking notifyCustomer, where initiateSupplier and initiateShipper are matched activities (i.e., transitions pre<sup>fi</sup>xed by ≡) that invoke two partner Web services, W6 and W14, respectively, by W2. These two activities are irrelevant to the service consumer of W2 and therefore should not appear in view<sub>c</sub> of W2. Furthermore, Web service variables pre<sup>fi</sup>xed a bounded operation may have to be adjusted. For instance, in Fig. 5, variable x of W2 identi<sup>fi</sup>es its invoker. Because W2 further invokes W12.? initiateShipper, the variable z of W12 is bound to W2. Thus, ancestor(z,1) of W12 refers to W2's invoker, which is x. Therefore, ancestor(z,1) of W12 can be replaced by x in Fig. 5.

In the following, we reduce the gross FSM to view by removing matched activities. Moreover, the probabilities of the transitions retained in view have to be given by considering the eliminated matched activities. Take the rightmost execution path (bx>−w2.?orderRequest, w2– w6.≡initiateSupplier, w2–w14.≡initiateShipper, w2-x.!notifyCustomer) in Fig. 6 as an example. After eliminating matched activities, only two activities, ?orderRequest and !notifyCustomer, remain in view . The probability of ?orderRequest in view , however, must re<sup>fl</sup>ect the chance of successfully completing ?orderRequest and the two (invisible) matched activities. The way to assign probabilities to transitions of remaining activities is described below.

We de<sup>fi</sup>ne the probability of a transition with a (nonmatched) activity o in view as the probability that o and the subsequent matched activities in the corresponding gross FSM are completed successfully before reaching a nonmatched activity or <sup>fi</sup>nal state. For example, the transition probability of ?orderRequest in view is the chance of successfully executing ?orderRequest and the subsequent matched activities before encountering any nonmatched activity (i.e., reaching states a, b, or c in the gross FSM of Fig. 6). To compute the transition probability for an activity in a view , we extract the succeeding matched activities and the related states from the gross FSM to form a time homogeneous

![](/api/attachments/G2J77WPZ/fulltext/images/a6e3789226d4259262271406f7d9abe6406cedf48498fda883da12aa3bed3181.jpg)  
Fig. 4. Corresponding Petri nets for FSM of W2 and view s of its children (W6, W11, W12, and W14).

![](/api/attachments/G2J77WPZ/fulltext/images/363089955f196dcc03201f8d30c033bfb32346b1e896f25ec29176a01726c1ac.jpg)  
Fig. 5. Global Petri net that combines the local Petri nets in Fig. 4.

Markov chain, in which the destination state of the given (nonmatched) activity in the gross FSM represents the initial state and the two additional states, the success and the failure states, represent the <sup>fi</sup>nal states. The probability of successfully executing subsequent matched activities is equivalent to the stationary probability of the success state in the derived Markov chain [13].

Fig. 7 shows the derived Markov chain for ?orderRequest extracted from the gross FSM in Fig. 6. The initial state of the Markov chain corresponds to the state that marks the completion of ?orderRequest. The success state, marked by Success, indicates the successful completion of the succeeding matched activities. Thus in the Markov chain, each of the states a, b, and c has one outgoing edge with probability 1 to the success state. In addition, the failure state, marked by Failure, indicates any failures that happened during the execution of the matched activities. Therefore, two edges, represented as dotted-line in Fig. 7, are added to represent the occurrence of failure by connecting the states 1 and 2 to failure state to represent the failed execution of initiateSupplier and initiateShipper respectively. The square brackets are the transition probabilities, which indicate the probabilities that the corresponding operation invocations/ receptions are chosen and successfully completed. The successful execution probability of a matched activity (≡o) is represented by the corresponding view . In our example, we assume that the probability of successful invocation of an operation to be 0.8. Thus in Fig. 7, the initial state has one outgoing transition, and its successful execution probability is 0.8, as obtained from the view of W6. Next, there are three outgoing transitions from state 2, and they have equal chances of being executed. As a result, the probability of the transition from state 2 to

Failure state is equivalent to the probability that all three initiateShipper operations fail, which is $( 1 - 0 . 8 ) ^ { 3 } = 0 . 0 0 8 \cong 0 . 0 1$ . The probability of transition from state 2 to each of the states a, b, and c is thus $( 1 - 0 . 0 1 ) / 3 =$ 0.33. In addition, the probabilities of transitions from the states a, b, and c to Success state are assigned to 1 to represent successful termination. Finally, there is a loop edge for each of success and failure states with transition probability being 1 to comply with the requirement of Markov chain: the sum of probabilities of all transitions incident from each state must be 1.We then apply power method to computing stationary probability of the Success state in the Markov chain [24]. The stationary probability of the Success state in Fig. 7 is 0.792, and it can be treated as the probability of successfully completing succeeding matched activities after ?orderRequest of W2. We then determine the transition probability of an activity in view as the product of its operation reliability (α) and the stationary probability of Success state in its associated Markov chain. For example, assuming $\begin{array} { r } { \alpha = 0 . 8 , } \end{array}$ , the probability of a transition with ?orderRequest in view of W2 is $0 . 8 \times 0 . 7 9 2 { \cong } 0 . 6 3 4$

The structure of view can be derived easily from a gross FSM by replacing each transition with some matched activity $\mathsf { b y } \varepsilon \left( \mathrm { n u l l } \right)$ . We can simplify the resultant view by eliminating ε, that is, converting the FSM to a regular expression and applying the following established rules [29]:

$$
\chi \cdot \varepsilon = \varepsilon \cdot \chi = \chi .\tag{1}
$$

$$
\varepsilon^ {*} = \varepsilon .\tag{2}
$$

$$
(\chi + \varepsilon) ^ {*} = \chi^ {*}.\tag{3}
$$

![](/api/attachments/G2J77WPZ/fulltext/images/934ae704072a71cc0c0c3f2f93fc62d70f3e0223a5b815ab399ca1b1bec180e3.jpg)  
Fig. 6. The gross FSM corresponding to the global Petri net in Fig. 5.

In Fig. 8 we reveal the view derived from the gross FSM in Fig. 6, in which only nonmatched activities in Fig. 6 are preserved and their probabilities are computed using the approach described above.

However, this view contains the identi<sup>fi</sup>ers of Web services, which compromises con<sup>fi</sup>dentiality of business partners. By eliminating Web services identi<sup>fi</sup>ers, this view could become nondeterministic in that there could be more than one transition with the same activity starting from a given state. There are four transitions incident from state 1 with the same activity x.!notifyCustomer in Fig. 8, for example. It is desirable to convert the nondeterministic view into a deterministic one, which we do by combining the transitions with the same activity into a single transition [31]. To determine the probability of a combined transition in vie $W _ { \mathrm { { C } } } ,$ we perform the following two sequential steps. First, transitions from the same Web service are combined. Because these transitions result from different execution paths in the focus Web service, the probability of the combined transition is the average of their respective probabilities. Second, we merge the transitions from different Web services into one transition. These transitions are regarded as alternatives for executing the same activity, and thus the probability of the merged transition is the probability that at least one transition succeeds.

![](/api/attachments/G2J77WPZ/fulltext/images/4a584dbcdb49c22400c0580c6ef0de535f333789b43cc8aaf779d7a45baeceaf.jpg)  
Fig. 7. The Markov chain for non-matched activity ?orderRequest from Fig. 6.

```txt
GenViewC(w0, P) : viewc
    // w0 is the focal Web service
    // P = (w1, w2, ..., wk) is the viewc of w0's partners
{
    for (i=0, i<=k, i++) convert wi into Petri Net ti;
    Convert t0∪t1∪t2∪ ...∪tk into a global Petri Net G;
    Convert G into a FSM F;
    for each nonmatched activity a in F {
    Compute the transition probability of a;
    }
    Eliminate matched activities in F to produce V;
    Convert V into a deterministic FSM V'
    for each combined transition t in V' {
    Compute the probability of t;
    }
    Return V';
}
```

![](/api/attachments/G2J77WPZ/fulltext/images/1e70da7d1a57c7c3527f29b437c4eee79113bd0a30d0b39e6008d3fe7442d345.jpg)  
Fig. 8. The non-deterministic FSM converted from Fig. 6 after removing matched activities, where the operation reliability α is 0.8 except W12.!notifyCustomer whose reliability is 0.7.

Formally, to combine n transitions $t _ { 1 } , t _ { 2 } , . . . , t _ { n }$ , with the same activity a, we use the following equation to compute the probability of the combined transition t, denoted Pr(t).

$$
\operatorname * {P r} (t) = \left\{ \begin{array}{l l} \frac {\sum_ {i = 1} ^ {n} \operatorname* {P r} (t _ {i})}{n} & \text { if } W S (t _ {1}) = \dots = W S (t _ {n}) \dots (4 - 1) \\ 1 - \prod_ {i = 1} ^ {n} (1 - \operatorname * {P r} (t _ {i})) & \text { otherwise } \dots \dots (4 - 2) \end{array} \right.
$$

For example, in Fig. 8, there are four transitions incident from node 1 with the same activity x.!notifyCustomer. We <sup>fi</sup>rst, combine the three transitions that belong to W2 by applying formula (4-1) to aggregate their probabilities: $( 0 . 8 + 0 . 8 + 0 . 8 ) / 3 = 0 . 8 .$ Second, assuming that the probability of successfully invoking W12.!notifyCustomer is 0.7, we can apply formula (4-2) to compute the <sup>fi</sup>nal probability: $1 - ( 1 - 0 . 8 ) \times ( 1 - 0 . 7 ) = 0 . 9 4$ . The <sup>fi</sup>nal view of W2 is shown in Fig. 9. Note that the names of Web services participating in transitions of view do not appear in the <sup>fi</sup>nal vie $ { N _ { \mathrm { c } } } ,$ which indicates respect for con-<sup>fi</sup>dentiality. The process of creating view of a Web service is outlined in Fig. 10.

## 4.2.2. Creating view for each Web service role of service provider

The view s of a Web service are constructed in a top-down manner. $v _ { \mathrm { p } } S$ Therefore, the $v i e w _ { \mathrm { p } }$ of the target Web service is the same as its own FSM. The Web services that are leaf nodes in the WS-invoking hierarchy do not have vie $ { \boldsymbol { v } } _ { \mathrm { p } }  { \boldsymbol { S } } ,$ because they do not need service providers. The view of a Web service that is an intermediate node in the WS-invoking hierarchy can be constructed, with the input of the view s of its service consumers and its own FSM. For example, the vie $v _ { \mathrm { p } } s$ of W2 are functions of its own FSM and the vie $v _ { \mathsf { p } } S$ of the target Web service. We apply the same approach we used for constructing view to generate vie $N _ { \mathrm { p } }$ without computing transition probabilities. No transition probabilities are needed because the $v i e w _ { \mathrm { p } }$ of a Web service is intended for its service providers, who are only concerned with their descendents in the WS-invoking hierarchy when they make Web service selections. The combined FSM thus can be tailored to each role r of the service providers, considering only activities permitted in r, which results in the $v i e w _ { \mathrm { p } }$ for role r. Fig. 11 shows the vie $w _ { \mathrm { p } }$ of the two Web service roles that W2's service providers may play, namely, Supplier and Shipper.

![](/api/attachments/G2J77WPZ/fulltext/images/3d53470420c49910b1a5e9af9f1229634d8d48d738dd5250c22e203f1cc31c63.jpg)  
Fig. 9. The <sup>fi</sup>nal view<sub>c</sub> of W2.

## 4.3. Building local compositions

The local composition of each Web service serves as its local view on the entire choreography, in which interactions may involve ancestors/ descendants in the WS-invoking hierarchy. The construction of the local composition uses its own FSM, the view s of its service consumers, and the view s of its service producers. An algorithm for building the composition of a set of FSMs has been proposed in prior research [13]. This composition is also an FSM in which each state, or con<sup>fi</sup>guration, combines states in the input FSMs. In other words, the local composition represents all possible delegations that lead to successful termination, characterized by a <sup>fi</sup>nal con<sup>fi</sup>guration, such that all states of the involving Web services must be initial or <sup>fi</sup>nal. In addition, each transition that does not involve a given Web service W (i.e., represents a match between two activities of an ancestor and a descendant of W in the WS-invoking hierarchy) is replaced by $\varepsilon ,$ because it is irrelevant to the Web service selection by W. In our example, the local composition for

Fig. 10. The pseudo code of creating view for a Web service $w _ { 0 } .$

![](/api/attachments/G2J77WPZ/fulltext/images/837e85f62efcdde32463acee4e6a03d8bc1e728e97e7f14ef43a6a95aa635782.jpg)  
Fig. 11. The view<sub>p</sub>s of the two Web service roles of W2.

W2 can be built by combining the view of the target Web service (W1), the FSM of W2, and the view s of W5, W6, W11, W12, and W14, some of which are shown in Fig. 12. The resultant composition is in Fig. 13. Each transition in the local composition involves some activity by W2. Note that activities by W5 and W12 are not involved in any transitions of W2's local composition, so they will not be considered in W2's Web service selection, because choosing either of them would not lead to a <sup>fi</sup>nal con<sup>fi</sup>guration.

Each transition in the composition is then assigned a probability. If a transition is a match of two activities from the focal Web service and some view , its probability simply equals the operation reliability (denoted α). However, a transition obtained by matching two activities from the focal Web service and some view retains the same probability of the corresponding activity in view . In our example, the involved view are from W6, W11, and W14. The transition probability of W2–W6.initateSupplier is 0.64, equal to the transition probability of ?initiateSupplier in W6's view . For the next operation, initiateShipper, two alternatives are from W11 and W14, and the two corresponding transitions have probabilities equal to the product of the transition probabilities in the associated view s and the selection probabilities, initially set to 1/2 and then adjusted according to the algorithm proposed in [13]. Finally, the aggregate reliability of each con<sup>fi</sup>guration, which represents the probability of reaching some <sup>fi</sup>nal con<sup>fi</sup>guration, is computed. In Fig. 13, the aggregate reliability of each con<sup>fi</sup>guration is enclosed in a square bracket next to it. For details regarding the computation of aggregated reliabilities, see [13].

At runtime, each Web service, assuming it has been instantiated, consults its local composition to decide which Web service to invoke for each free operation invocation. Speci<sup>fi</sup>cally, when an incoming free operation invocation arrives, given a particular con<sup>fi</sup>guration, we sort the candidate Web services according to the non-increasing order of the products of their transition probabilities and the aggregated reliabilities of the destination con<sup>fi</sup>gurations. These Web service operations, tried one at time in order, eventually reveal which can be executed successfully. For example, in Fig. 13, after completing the initiateSupplier operation (i.e., the current con<sup>fi</sup>guration is (1, 2, 0, 1f, 0, 0, 0)), there are two alternatives for initiateShipper, W11 and W14. W11 will be selected and invoked <sup>fi</sup>rst because the value of the product of its transition probability and the aggregated reliability of its destination con<sup>fi</sup>guration (i.e., 0.8×0.8) is higher. If this invocation of initiateSupplier fails, W14 will be chosen and invoked.

## 5. Performance evaluation

We refer to our proposed method as the view-based method, because each component Web service in the choreography model provides views of its ancestors and descendants in the WS-invoking hierarchy to collaborating partners. In addition, we evaluate four other methods as benchmarks: centralized, view-based propagation-free, view-based reliability-free, and random methods.

• Centralized method: This method assumes the existence of a centralized entity that holds all information about the entire Web service community. When a Web service needs to decide which Web service to invoke for a free operation invocation, it resorts to this entity for a recommendation. The centralized entity maintains a global composition for all involved Web services using the approach proposed by [13]. The centralized method suffers from single point failure and compromises con<sup>fi</sup>dentiality, though it can make the best choice. It serves as the reference point for comparison.

• View-based propagation-free method: This simpli<sup>fi</sup>ed version of the proposed view-based method allows each Web service to consider only its parents and children in constructing its local composition. Activities by a Web service's grandchildren in the WS-invoking hierarchy do not get considered for matching. Take W1 in Fig. 2 as an example: It may <sup>fi</sup>nd W3 undesirable for !orderRequest because it does not provide the callback invocation (!notifyCustomer) needed by W1. However, W3 is not really a bad choice, because one of its service providers, W13, provides !notifyCustomer. Comparing this method with the view-based method reveals the effect of propagating information about activities (and transition probabilities) beyond a Web service's partners.

• View-based reliability-free method: Although similar to view-based method, this approach eliminates the complicated computation of the transition probabilities of view . The view of each Web service thus has no probability values associated with its transitions. When it comes to building a local composition, each outgoing transition is assumed to have an equal chance of being invoked.

![](/api/attachments/G2J77WPZ/fulltext/images/043e3e8c2c5e9919da20893e28bec5a267affe8f24015e2e8bfdbe8f77c40816.jpg)  
Fig. 12. Partial input for the local composition of W2 in Fig. 11.

![](/api/attachments/G2J77WPZ/fulltext/images/a4fa0239eacbdf005a6337c88deace045362d1eed6d44855418c66e0bbf49841.jpg)  
Fig. 13. Local composition of W2.

• Random method: This most naïve approach randomly chooses a Web service that provides the corresponding free operation reception for a given free operation invocation.

## 5.1. Experimental design

We implement the shopping scenario described above and adopt the Web service community and WS-invoking hierarchy in Figs. 2 and 3 respectively for our experiments. In addition, we add W5 as an extra partner of W2 to shed light on the performance differences among the various methods. The performance metric we consider is success rate, which measures the ratio of target Web service executions whose activities are successfully delegated and executed. A selection method with a higher success rate means that, if this method is adopted, the execution of the target Web service is more likely to <sup>fi</sup>nish successfully.

![](/api/attachments/G2J77WPZ/fulltext/images/f862bbe3f673b49630cb88605e478e1138683f8a1178221d12e80c9f10fb83eb.jpg)  
Fig. 14. Success rates of the <sup>fi</sup>ve methods for the simpli<sup>fi</sup>ed shopping scenario.

For each of the methods we investigate, we execute 10,000 instances of the target Web service. Each operation invocation is assumed to have a <sup>fi</sup>xed probability α that it will succeed, which we refer to as operation reliability. We repeat each experiment 100 times and report the average success rate. A one-way analysis of variance (ANOVA) with post-hoc analysis serves to test the signi<sup>fi</sup>cance of the performance differences between methods.

## 5.2. Success rates of five methods

The success rates of the <sup>fi</sup>ve methods, with α varying from 0.5 to 0.99, appear in Fig. 14. As we expected, the centralized method achieves the highest success rate across all operation reliabilities; our proposed view-based method attains comparable performance. Both methods are consistently better than the view-based propagation-free, viewbased reliability-free, and random methods.

The centralized method performs the best because the global composition is maintained by a single entity that possesses all detailed information about all Web services. Our view-based method achieves similar performance, because each Web service possesses a good summary of the behavior of its ancestors and descendants in the WS-invoking hierarchy. Their performance difference, though slight, is still signi<sup>fi</sup>cant according to the ANOVA analysis. The main source of this difference is the preference for orderRequest: The view-based method prefers W2 to W4, whereas the centralized method favors W4, as we summarize in

Priority sequence of Web service for !orderRequest of W1.

<table><tr><td>Method</td><td>Priority sequence</td></tr><tr><td>Centralized</td><td>W3, W4, W2</td></tr><tr><td>View-based</td><td>W3, W2, W4</td></tr><tr><td>View-based propagation-free</td><td>W2</td></tr><tr><td>View-based reliability-free</td><td>Equal priority for W2, W3, and W4</td></tr></table>

Table 2  
Priority sequences of Web service for !initiateSupplier of W2, W3, and W4.

<table><tr><td rowspan="2">Method</td><td colspan="3">Priority sequence</td></tr><tr><td>W2</td><td>W3</td><td>W4</td></tr><tr><td>Centralized</td><td>W6</td><td>W7,W6</td><td>W5,W8</td></tr><tr><td>View-based</td><td>W6</td><td>W7,W6</td><td>W5,W8</td></tr><tr><td>View-based propagation-free</td><td>W6</td><td>N/A</td><td>N/A</td></tr><tr><td>View-based reliability-free</td><td>W6</td><td>Equal priority for W6 and W7</td><td>Equal priority for W5 and W8</td></tr></table>

Table 1. This outcome occurs because ?orderRequest on the view of W2 represents a higher transition probability, because it accumulates the transition probabilities of ?initiateSupplier from both W5 and W6. However, W5 cannot be used in reality, because the target Web service does not match the !notifyVendor operation of W5, as we show in Table 2. Should W5 be excluded from the partner set of W2, the view-based method would perform as well as the centralized method. This observation demonstrates the potential limitation of our view-based method and explains its slightly inferior performance compared with a centralized method.

In the view-based propagation-free method, each Web service is aware of only its partner Web services. A lack of information beyond partner Web services harms performance compared with the proposed view-based method. In our experimental scenario, with the view-based propagation-free method, the target Web service must always delegate orderRequest to W2 and disallow the delegation to W3 and W4, as shown in Table 1, because W3 and W4 rely on their descendants to invoke notifyCustomer. This restriction increases the probability of failure because the failure of W2.orderRequest results in the failure of the entire execution. Even if W2 is invoked successfully, according to Table 2, only W6 can be chosen for !initiateSupplier, whereas both W3 and W4 have two candidates for !initiateSupplier. This result signi<sup>fi</sup>es the importance of propagating information across Web services. The view-based reliability-free method achieves better performance than the view-based propagation-free method because it assigns equal probabilities to choosing W2, W3, and W4 for ?orderRequest, in that it lacks transition probabilities (shown in Table 1).

## 5.3. Success rates of five methods in a nontransitive scenario

The view-based method incorporates the propagation of information about activities and comprehensive transition probability compu tations, which contribute to higher success rates in our experimental choreography with transitive callbacks (e.g., notifyCustomer between W13 and W1). However, in a choreography without transitive callbacks, perhaps its performance would match that of the view-based propagation-free method. To test this conjecture, we conducted another experiment with a revised choreography model in which operation callback activities, such as !notifyCustomer and !notifyVendor, are provided only by immediate descendant Web services. Speci<sup>fi</sup>cally, to the Web service community in Fig. 2, we

![](/api/attachments/G2J77WPZ/fulltext/images/b6169bfd1a7f5d6cf8484e4a6a1cf61c6a2219ae3397f8555e0a391694a880c1.jpg)  
Fig. 15. Success rates of the <sup>fi</sup>ve methods for the nontransitive scenario.

Table 3  
Priority sequence of Web service for !orderRequest of W1.

<table><tr><td>Method</td><td>Priority sequence</td></tr><tr><td>Centralized</td><td>W4, W2</td></tr><tr><td>View-based</td><td>W4, W2</td></tr><tr><td>View-based propagation-free</td><td>W2, W4</td></tr><tr><td>View-based reliability-free</td><td>Equal priority for W2 and W4</td></tr></table>

<sup></sup> drop W3 and add !notifyCustomer activity to W4; and,

<sup></sup> remove !upstreamSupplier activity of W8 and !recordInfoToDB activities of W12 and W14.

For this new choreography model, we provide the success rates of the <sup>fi</sup>ve methods in Fig. 15. The centralized and view-based methods still top the list, and their success rates exhibit no differences in the ANOVA test. However, to our surprise, the view-based propagation-free method still performs worse than the view-based method, though its performance is closer compared with the result in the <sup>fi</sup>rst experiment.

As we show in Table 3, both the centralized and view-based methods result in the same priority sequence (i.e., W4 followed by W2) for orderRequest. In contrast, the view-based propagation-free method prefers W2 to W4, because W2 has a shorter activity sequence. However, W4 is actually a better choice, because it offers two !initiateSupplier candidates (see Table 4)—a trait unknown to W1 without propagation. Moreover, its performance is slightly worse than that of the view-based reliability-free method, which has a better chance of choosing W4 (Table 3). Thus, the comprehensive reliability information computed by the view-based method contributes to a better success rate, even in a choreographed environment that has no transitive callbacks.

## 6. Conclusions

In this work, we have de<sup>fi</sup>ned a choreography model and proposed the view-based method for a Web service to select partner Web service in a choreographed environment, in which respect for con<sup>fi</sup>dentiality demands that each Web service is aware of only the behavior of its partners. In our view-based method, a Web service summarizes the behavior of its descendant Web services in the WS-invoking hierarchy and thus forms a view for its service consumers. It also summarizes the behavior of its ancestor Web services in the WS-invoking hierarchy for each of its service providers, or view . Any given Web service then can use the view s provided by its service providers and the view s given by its service consumers to construct a local composition. We use a measure of aggregated reliability to guide the selection and instantiation of partner Web services [13]. The experimental results show that our proposed method performs nearly as well as the centralized method yet respects con<sup>fi</sup>dentiality of Web service partners.

We plan to apply our proposed method to some real application that involves dynamic operation invocation, using WS-BPEL, in further research to justify the practical value of our approach. Other research might address some limitations of our study, such as that we assume all Web services in the Web service community conform to the choreograph speci<sup>fi</sup>cation, usually expressed in WS-CDL or BPMN 2.0 in practice. If this assumption does not hold, some Web services should be excluded before any subsequent Web service selection.

Priority sequence of Web service for !initiateSupplier of W2 and W4.

<table><tr><td rowspan="2">Method</td><td colspan="2">Priority sequence</td></tr><tr><td>W2</td><td>W4</td></tr><tr><td>Centralized</td><td>W6</td><td>W5,W8</td></tr><tr><td>View-based</td><td>W6</td><td>W5,W8</td></tr><tr><td>View-based propagation-free</td><td>W6</td><td>W5,W8</td></tr><tr><td>View-based reliability-free</td><td>W6</td><td>Equal priority for W5 and W8</td></tr></table>

## Acknowledgments

This work has been supported in part by the National Science Council in Taiwan, under grant no NSC99-2752-H-110-005.

## References

[1] M. Baldoni, C. Baroglio, A. Martelli, V. Patti, A Priori Conformance Veri<sup>fi</sup>cation for Guaranteeing Interoperability in Open Environments, in: 4th International Con ference on Service-Oriented Computing (ICSOC 2006), 2006, pp. 339–351.

[2] M. Baldoni, C. Baroglio, A. Martelli, V. Patti, Reasoning on choreographies and capability requirements, International Journal of Business Process Integration and Management 2 (4) (2007) 247–261.

[3] M. Baldoni, C. Baroglio, A. Martelli, V. Patti, C. Schifanella, Service Selection by Choreography-Driven Matching, in: T. Gschwind, C. Pautasso (Eds.), Emerging Web Services Technology, 2008, pp. 5–22.

[4] M. Baldoni, C. Baroglio, A.K. Chopra, N. Desai, V. Patti, M.P. Singh, Choice, Interoperability, and Conformance in Interaction Protocols and Service Choreographies, in: 8th International Conference on Autonomous Agents and Multiagent Systems, 2009, pp. 843–850.

[5] U. Bellur, R. Kulkarni, Improved Matchmaking Algorithm for Semantic Web Services Based on Bipartite Gaph Matching, in: 2007 IEEE International Conference on Web Services (ICWS 2007), 2007, pp. 86–93.

[6] T. Bultan, X. Fu, J. Su, Analyzing Conversations: Realizability, Synchronizability, and Veri<sup>fi</sup>cation, in: L. Baresi, E. Nitto (Eds.), Test and Analysis of Web Services, 2007, pp. 57–85.

[7] V. Ermolayev, N. Keberle, Towards a framework for agent-enabled semantic Web service composition, International Journal of Web Services Research 1 (3) (2004) 63–87.

[8] H. Foster, S. Uchitel, J. Magee, J. Kramer, Compatibility Veri<sup>fi</sup>cation for Web Service Choreography, in: 2004 IEEE International Conference on Web Services (ICWS 2004), 2004, pp. 738–741.

[9] H. Foster, S. Uchitel, J. Magee, J. Kramer, Model-Based Analysis of Obligations in Web Service Choreography in: 2oo6 Advanced International Conference on Telecommunication and International Conference on Internet and Web Applications and Services 2006.

[10] V. Grassi, S. Patella, Reliability prediction for service-oriented computing environments, IEEE Internet Computing 10 (3) (2006) 43–49.

[11] N. Guermouche, C. Godart, Timed Model Checking Based Approach for Web Services Analysis, in: 2009 IEEE International Conference on Web Services (ICWS 2009), 2009, pp. 213–221.

[12] J. Huang, Y.S. Zhang, I.L. Yen, J.T. Carson, M.F. Siok, F. Bastani, Y.J. Zhao, J. Dong, Real-Time Service-Oriented Distributed Governance, in: 2010 6th World Congress on Services (SERVICES-1, 2010, pp. 479–484.

[13] S.Y. Hwang, E.P. Lim, C.H. Lee, C.H. Chen, Dynamic Web service selection for reliable Web service composition, IEEE Transactions on Services Computing 1 (2) (2008) 104–116.

[14] S.Y. Hwang, W.P. Liao, C.H. Lee, Web Services Selection in Support of Reliable Web Service Choreography, in: 2010 IEEE International Conference on Web Services (ICWS 2010), 2010, pp. 115–122.

[15] S.Y. Hwang, W.F. Hsieh, C.H. Lee, Verifying Web Services in a Choreography Environment, in: 2011 IEEE International Conference on Service Oriented Computing and Applications (SOCA 2011), 2011.

[16] S. Jiang, F. Aagesen, An Approach to Integrated Semantic Service Discovery, in: Autonomic Networking, 2006, pp. 159–171.

[17] N. Kavantzas, D. Burdett, G. Ritzinger, T. Fletcher, Y. Lafon, Web Services Choreography Description Language Version 1.0, http://www.w3.org/TR/2004/WD-ws-cdl-10-20041217/2004

[18] L. Kulnarattana, S. Rongviriyapanish, A Client Perceived QoS Model for Web Services Selection, in: 6th International Conference on Electrical Engineering/Electronics, Computer, Telecommunications and Information Technology (ECTI-CON 2009), 2009, pp. 731–734.

[19] Z. Maamar, S.K. Mostefaoui, H. Yahyaoui, Toward an agent-based and context-oriented approach for Web services composition, IEEE Transactions on Knowledge and Data Engineering 17 (5) (2005) 686–697.

[20] D.A. Menasce, QoS issues in Web services, IEEE Internet Computing 6 (6) (2002) 72–75.

[21] S. Mitra, R. Kumar, S. Basu, Optimum Decentralized Choreography for Web Services Composition, in: 2008 IEEE International Conference on Services Computing (SCC 2008), 2008, pp. 395–402.

[22] M. Montali, M. Pesic, W.M.P. van der Aalst, F. Chesani, P. Mello, S. Storari, Declarative Speci<sup>fi</sup>cation and Veri<sup>fi</sup>cation of Service Choreographies, ACM Transactions on the Web 4 (1) (2009), (Article 3:1-62)

[23] I. Muller, R. Kowalczyk, P. Braun, Towards Agent-Based Coalition Formation for Service Composition, in: The IEEE/WIC/ACM International Conference on Intelli gent Agent Technology (IAT 2006), 2006, pp. 73–80.

[24] G. Nakos, D. Joyner, Linear Algebra with Applications, Brooks/Cole Pub. Co, 1998

[25] M. Paolucci, T. Kawamura, T. Payne, K. Sycara, Semantic Matching of Web Services Capabilities, in: 1st International Semantic Web Conference (ISWC 2002), 2002, pp. 333–347.

[26] J.L. Peterson, Petri Net Theory and the Modeling of Systems, Prentice Hall PTR Upper Saddle River, NJ, USA, 1981.

[27] S. Rajamani, J. Rehof, Conformance Checking for Models of Asynchronous Message Passing Software, in: 14th International Conference on Computer Aided Veri<sup>fi</sup>cation (CAV 2002), 2002, pp. 299–323.

[28] S. Ran, A model for Web services discovery with QoS, SIGecom Exchanges 4 (1) (2003) 1–10.

[29] E. Rich, Manipulating and Simplifying Regular Expressions, in: Automata, computability and complexity: theory and applications, 2008, pp. 149–151.

[30] W. She, I.L. Yen, B. Thuraisingham, E. Bertino, The SCIFC Model for Information Flow Control in Web Service Composition, in: 2009 IEEE International Conference on Web Services (ICWS 2009), 2009, pp. 1–8.

[31] M. Sipser, Introduction to the Theory of Computation, PWS Pub. Co, 1996.

[32] Y. Sun, S. He, J.Y. Leu, Syndicating Web services: a QoS and user-driven approach Decision Support Systems 43 (1) (2007) 243–255.

[33] N. Thio, S. Karunasekera, Automatic Measurement of a QoS Metric for Web Service Recommendation, in: 2005 Australian Software Engineering Conference (ASWEC 2005), 2005, pp. 202–211.

[34] H. Tong, J. Cao, S.S. Zhang, M.L. Li, A distributed algorithm for Web service composition based on service agent model, IEEE Transactions on Parallel and Distributed Systems 22 (12) (2011) 2008–2021.

[35] C. Wu, E. Chang, A. Aitken, An Empirical Approach for Semantic Web Services Discovery, in: 19th Australian Conference on Software Engineering (ASWEC 2008), 2008, pp. 412–421.

[36] H.L. Yang, L. Zhou, K. He, C. Deng, X.P. Zhao, Z.Y. Qiu, A Probabilistic QoS Model-Checking for Dynamic Routing Protocol, in: 2010 10th International Con ference on Quality Software (ICSQ 2010), 2010, pp. 441–448.

[37] T. Yu, Y. Zhang, K.J. Lin, Ef<sup>fi</sup>cient algorithms for Web services selection with end-to-end QoS constraints, ACM Transactions on the Web 1 (1) (2007) 1–25.

[38] L. Zeng, B. Benatallah, M. Dumas, J. Kalagnanam, Q.Z. Sheng, Quality Driven Web Services Composition, in: 12th International Conference on World Wide Web (WWW 2003), 2003, pp. 411–421.

[39] L. Zeng, B. Benatallah, A.H.H. Ngu, M. Dumas, J. Kalagnanam, H. Chang, QoS-aware middleware for Web services composition, IEEE Transactions on Software Engi neering 30 (5) (2004).311-327

[40] X. Zhao, H. Yang, Z. Qui, X. Zhao, H. Yang, Z. Qui, Towards the Formal Model and Veri<sup>fi</sup>cation of Web Services Choreography Description Language, in: 3rd International Workshop on Web Services and Formal Methods (WSFM'06, 2006.

[41] X. Zhao, C. Cai, H. Yang, Z. Qiu, X. Zhao, C. Cai, H. Yang, Z. Qiu, A QoS View of Web Service Choreography, in: 2007 IEEE International Conference on e-Business Engineering (ICEBE 2007), 2007, pp. 607–611.

[42] M. zur Muehlen, J.V. Nickerson, K.D. Swenson, Developing web services choreography standards—the case of REST vs. SOAP, Decision Support Systems 40 (1) (2005) 9–29.

![](/api/attachments/G2J77WPZ/fulltext/images/748bf4ee622461911e94780f6d394b28af53d33af0b1cf7e6dbb1bc81bd27fde.jpg)  
San-Yih Hwang received the BS and MS degrees from National Taiwan University, Taiwan, and the PhD degree from the University of Minnesota, Minneapolis in 1994, all in computer science. He joined the Department of Information Management at National Sun Yat-sen University, Taiwan, in 1995 and is presently a professor and department chair. His current research interests include services computing, work<sup>fl</sup>ow management, and recommendations

![](/api/attachments/G2J77WPZ/fulltext/images/6d49af7b1fa8461c7c7d7ee5e62ac15a5299a8877697b113622e163cce27731b.jpg)

Chien-Hsiang Lee received the PhD degree from National Sun Yat-Sen University, Taiwan in 2012. He received the BS degree in Management Science and the MS degree in Information Management from National Chiao Tung University Taiwan in 1988 and 1991 respectively. He is currently a postdoctoral researcher at the Department of Information Management at National Sun Yat-sen University. His current research interests include Web services, service-oriented architecture, and service science.
