---
otero_id: 9012
otero_key: "ZHKPJRVS"
title: "Cross-organizational collaborative workflow mining from a multi-source log"
authors: "Qingtian Zeng; Sherry X. Sun; Hua Duan; Cong Liu; Huaiqing Wang"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.12.001"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Cross-organizational collaborative work<sup>fl</sup>ow mining from a multi-source log

Qingtian Zeng <sup>a,</sup>⁎, Sherry X. Sun <sup>b</sup>, Hua Duan <sup>a</sup>, Cong Liu <sup>a</sup>, Huaiqing Wang <sup>c</sup>

<sup>a</sup> College of Information Science and Engineering, Shandong University of Science and Technology, Qingdao 266510, China

<sup>b</sup> Department of Information Systems, City University of Hong Kong, 83 Tat Chee Avenue, Hong Kong

<sup>c</sup> Department of Financial Math and Financial Engineering, South University of Science and Technology of China, Shenzhen, China

## a r t i c l e i n f o

Article history: Received 10 May 2012 Received in revised form 19 September 2012 Accepted 2 December 2012 Available online 8 December 2012

Keywords: Cross-organizational work<sup>fl</sup>ow Collaborative work<sup>fl</sup>ow Running log Process mining Petri net Coordination pattern

## a b s t r a c t

Today's enterprise business processes become increasingly complex given that they are often executed by geographically dispersed partners or different organizations. Designing and modeling such a cross-organizational work<sup>fl</sup>ow is a complicated, time-consuming process and requires that a designer has extensive experience. Work<sup>fl</sup>ow logs captured by different cross-organizational systems provide a very valuable source of information on how business processes are executed in reality and thus can be used to derive work<sup>fl</sup>ow models through process mining. In this paper, we investigate the application of process mining for work<sup>fl</sup>ow integration based on the concept of RM\_WF\_Net, a type of Petri net extended with resource and message factors. Four coordination patterns are de<sup>fi</sup>ned for work<sup>fl</sup>ow integration. A process mining approach is presented to discover the coordination patterns between different organizations and the work<sup>fl</sup>ow models in different organizations from the running logs containing the information about resource allocation. A process integration approach is then presented to obtain the model for a cross-organizational work<sup>fl</sup>ow based on the model mined for each organization and the coordination patterns between different organizations.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

With the development of the Internet and distributed computing technologies, today's enterprise business processes become increasingly complex given that they are often executed by geographically dispersed partners or different organizations. For example, a typical multi-modal transportation business process may require the coordination of several business partners including the sender, the consignor, the carrier, the shipper, the buyer and other related partners. Designing and modeling such a cross-organizational work<sup>fl</sup>ow require a work<sup>fl</sup>ow designer to have lengthy discussions with the involved workers and managers of different organizations. Therefore, creating a work<sup>fl</sup>ow design is a complicated and time-consuming process and there are typically discrepancies between the actual work<sup>fl</sup>ow processes and the processes as perceived by the management [21].

Many enterprise information systems, such as enterprise resource planning (ERP), customer relationship management systems (CRM), and work<sup>fl</sup>ow management systems (WfMS), usually record information of the execution of business processes in their event logs [21]. Thus, process mining, also referred to as work<sup>fl</sup>ow mining, has recently been proposed to distil a structured process description from the event logs of those systems [9]. The goal of process mining is to analyze event logs so as to construct a model that best describes all the recorded instances of a work<sup>fl</sup>ow.

Recently, cross-organizational process mining has received more attention [18]. Although many papers on process mining have been published [3,5,6,20,21], it is dif<sup>fi</sup>cult to apply existing approaches directly to discover a model for a cross-organizational work<sup>fl</sup>ow. This can be attributed to the fact that the running log of a cross-organizational work<sup>fl</sup>ow is usually distributed on different servers owned by different partners or different organizations, while most existing process mining approaches assume that a single server is used to manage all the operations of a process [3,5,6,20,21].

To address this problem, a process mining based integration approach is proposed in this paper to obtain cross-organizational work<sup>fl</sup>ow models. Unlike the existing studies on process mining [3,5,6,20,21], the event logs in this study are distributed on different servers located in different organizations. The event logs contain information about resource allocation and messages exchanged, which are two important coordination mechanisms between organizations. The concept of RM\_WF\_Net is proposed to represent the mined work<sup>fl</sup>ows. An RM\_WF\_Net is a type of extended Petri net that allows representation of resource allocation and messages exchanged in work<sup>fl</sup>ows. On the basis of the RM\_WF\_Net model, four different coordination patterns are de<sup>fi</sup>ned for cross-organizational work<sup>fl</sup>ow integration. A process mining approach is presented to discover work<sup>fl</sup>ow models in different organizations from the event logs containing the information on resource allocation. To discover the coordination patterns between different organizations, a middleware has been implemented to integrate the work<sup>fl</sup>ow running logs between different organizations. Based on the logs integrated, the coordination patterns between different organizations can be obtained by using the process mining approach. According to the work<sup>fl</sup>ow models in different organizations and the coordination patterns between different organizations, a process integration approach is presented to obtain the cross-organizational work<sup>fl</sup>ow models. Our approach can help an organization to identify from its own perspective the overall work<sup>fl</sup>ow model re<sup>fl</sup>ecting how various organizations collaborate. Moreover, when the event log data of all relevant work<sup>fl</sup>ows are available, our method can help derive a complete overview of a work<sup>fl</sup>ow that crosses multiple organizational entities. In the paper, a multi-modal transportation business process is studied as an example to validate the proposed approaches. However, it is only possible to obtain the overall work<sup>fl</sup>ow model from the individual perspective of each organization involved in the multi-modal transportation business process, and to understand the collaboration between the organization's private work<sup>fl</sup>ow and other work<sup>fl</sup>ows. In many tightly coupled application cases, the approaches proposed in this paper can be used to obtain the overall model for a cross-organizational collaborative work<sup>fl</sup>ow; consequently, an example of hospital work<sup>fl</sup>ow model integration is used to demonstrate the approaches proposed in the paper.

The remainder of the paper is organized as follows. Section 2 presents a review of the related work. Section 3 gives a framework for cross-organizational work<sup>fl</sup>ow mining and integration. An example of a cross-organizational work<sup>fl</sup>ow used to validate the proposed approach in the paper is also given in Section 3. Section 4 de<sup>fi</sup>nes the RM\_WF\_Net model for a cross-organizational work<sup>fl</sup>ow and the coordination patterns for different organizations. Section 5 presents the work<sup>fl</sup>ow mining for one single organization. Section 6 presents the cross-organizational work<sup>fl</sup>ow integration using process mining. Section 7 presents an experiment evaluation for the proposed approach. Section 8 concludes the paper with our contributions and future research directions.

## 2. Related work

In this section, we compare our work with related work on process mining and process integration.

## 2.1. Process mining

Process mining has been proposed as a tool for analyzing business processes based on event logs [21]. Many papers on process mining have been published [20,21]. A survey of existing process mining approaches was provided by [20]. Most process mining methods start with event-based logs, i.e., sequences of instantaneous events. In event-based logs, it is possible to identify the start and end events to infer the duration of activities. In [1], methods were proposed for automatically deriving a formal model of a process from a log of events recording the executions of a process. However, these studies were limited to a sequential process structure. By using the same type of process logs as input, a work<sup>fl</sup>ow model based on Petri nets was derived to capture timing information such as minimal, maximal, and average time spent in different stages of a process [19]. The timing information is associated with a type of node called a “place” in the derived Petri net-based work<sup>fl</sup>ow model.

Recently, [22] demonstrated the application of process mining for the feasibility of conformance checking of service behavior, that is, comparing message logs with service behavior speci<sup>fi</sup>cations to detect and to quantify deviations. In our previous work [2], a mining approach was proposed to discover the structural and temporal model for a work<sup>fl</sup>ow from its timed running log. According to the reachability graph of the discovered Petri net model, all running schemas of a work<sup>fl</sup>ow can be generated, de<sup>fi</sup>ning the temporal constraints among activities. In [15], based on examination of the model resulting from process mining, we demonstrated how to determine the minimum time to <sup>fi</sup>nish a work<sup>fl</sup>ow and how to partition the work<sup>fl</sup>ow in order to achieve ef<sup>fi</sup>cient server usage.

Most process mining tools have focused on the control-<sup>fl</sup>ow perspective [1.19], and work<sup>fl</sup>ow systems are often built on client/server architecture with the event log recorded and collected from a centralized log database. In the centralized paradigm, the mining algorithm is applied to the centralized log database to obtain the process model directly [3,5,20,21]. In a cross-organizational business process, information of the process execution is recorded and stored by individual databases belonging to different organizations. There is no centralized log database to store all the execution information of a work<sup>fl</sup>ow; thus, it is dif<sup>fi</sup>cult to discover the model for a cross-organizational business process directly using existing process mining approaches.

## 2.2. Process integration

Business process integration and management is a critical element in enterprise business transformation [28], and business process integration is considered a crucial technique for supporting inter-organizational business interoperability [23]. Many studies have addressed process integration [7,12]. In [7], the authors analyzed the existing technologies and standards, and proposed a reference model for B2B work<sup>fl</sup>ow integration. In [12], a solution was proposed to the integration design of material <sup>fl</sup>ow management in an e-business manufacturing environment.

According to the studies addressing process integration [7,12], the approaches to integrating processes include, but are not limited to, model-driven [28], integration points based [23], contract-based [25], and work<sup>fl</sup>ow merge approaches [14]. A set of model-driven business integration and management methods, frameworks, supporting tools, and a runtime environment was developed to study the ef<sup>fi</sup>cacy of model-driven business process integration and management [28]. In [23], the business process integration points were classi<sup>fi</sup>ed and a priority evaluation method between different points was presented. Based on the concept of the integration point, typical atomic integration patterns and some composite patterns were proposed. Ref. [25] presents contracts that encapsulate commitments laid down as a set of obligations to coordinate and control the interaction between business work<sup>fl</sup>ows. A business contract speci<sup>fi</sup>cation language was introduced to formally link the speci<sup>fi</sup>cation of business object based work<sup>fl</sup>ow systems. In [14], the concept of work<sup>fl</sup>ow merge was described and methods for merging business processes were proposed. Four merge categories were addressed: sequential, parallel, conditional, and iterative, and the corresponding algorithms for performing these four operations were reported.

As models for work<sup>fl</sup>ows, Petri nets have been used for process integration [4,8,17]. In [17], a modeling approach was presented for inter-organizational work<sup>fl</sup>ows in terms of Petri nets and the techniques were given to verify the correctness of the inter-organizational work<sup>fl</sup>ows. In [8], the Petri nets extended with time and color were proposed as a formalization for managing events, in which seven basic patterns were designed to capture the modeling concepts that commonly arise in supply chains. Moreover, a complete Petri net can be built from those patterns and analyzed by using dependency graphs and simulation [8]. In [4], open Petri nets were proposed as a suitable semantic model for work<sup>fl</sup>ows spanning different enterprises.

From the studies reviewed here [8,14,17,23,25,28], a model integration for work<sup>fl</sup>ow models is one of the approaches most addressed. In this paper, we also mainly discuss the model integration for work<sup>fl</sup>ow processes. Four coordination patterns are de<sup>fi</sup>ned for cross-organizational work<sup>fl</sup>ows, including coordination with synchronized activities, coordination with messages exchanged, coordination with shared resources, and coordination with abstract procedures, which are used to integrate processes. To address this problem, a process mining based approach is introduced for cross-organizational process integration. To integrate processes, one important assumption is that there must be a model for each organization [8,14,17,23,25,28], otherwise it is impossible to integrate a process for a cross-organizational business work<sup>fl</sup>ow. To address this problem, process-mining technology is applied in this paper to obtain the work<sup>fl</sup>ow model within each organization. Thus, a process mining based approach is introduced for cross-organization process integration.

## 3. Framework for cross-organizational work<sup>fl</sup>ow integration based on process mining

In this section, a running example of a cross-organizational work<sup>fl</sup>ow used to validate the proposed approach is <sup>fi</sup>rst given, then a framework for cross-organizational work<sup>fl</sup>ow mining and integration is proposed.

## 3.1. A running example of cross-organizational workflows

With the acceleration of global economic integration and the rapid development of logistical technology, multi-modal transportation is needed to meet the requirements of supply chain integration. Use of a multi-modal transportation business management system can involve tracking the movement of goods between partners and monitoring the storage of goods at different locations. A typical scenario of a multi-modal transportation business process is presented in Fig. 1.

There are several participants in a typical multi-modal transportation business process. For example, the sender, consignor, carrier, shipper and buyer are usually involved in the main transportation process. In addition, the consignor is required to make a customs declaration before delivering the goods to the carrier, especially for overseas business. At some stage, the shipper transports the goods to a whar<sup>fi</sup>nger for long-term storage. Therefore, two other parties, the customer and the whar<sup>fi</sup>nger, are also possibly involved in the transportation process. A typical scenario for a multi-modal transportation business process includes the following steps.

1. The buyer books goods and the goods booking order is sent to the sender.

2. After receiving the goods booking order, the sender calculates the cost of the goods and generates the goods booking contract. The goods cost bill is sent to the buyer.

3. The sender and buyer sign the goods booking contract together.

4. After the contract is signed, the buyer pays according to the goods cost bill and sends the payment veri<sup>fi</sup>cation to the sender.

5. After receiving the payment from the buyer, the sender starts the transportation. The <sup>fi</sup>rst step is to apply for a shipping task from the consignor.

6. After receiving a shipping application from the sender, the consignor generates a transportation contract.

7. The sender and the consignor sign the transportation contract together.

8. After the transportation contract is signed, the consignor makes booking requests to the carrier and the shipper.

9. The carrier and the shipper accept the booking requests and return acceptance notices to the sender.

10. After the booking requests are accepted, the consignor prepares containers and a packing notice is sent to the sender to prepare the shipping goods.

11. The sender prepares the goods for transportation.

12. After the goods arrive, the consignor and sender pack the goods and make a customs declaration together. The consignor takes responsibility for three steps of the customs declaration procedure: generating a declaration form, declaration application, and decla ration acceptance.

13. The consignor forwards the goods to the carrier.

14. The carrier loads the shipping goods and generates a waybill for the consignor.

15. According to the waybill, the consignor pays the carrier.

16. After obtaining the payment, the goods are delivered by the carrier.

17. The carrier and shipper transport the goods.

18. After receiving the booking request from the consignor, the shipper tallies the goods and prepares for shipping.

19. After the shipper receives the goods, a terminal receipt is generated and sent to the consignor for payment.

20. The consignor makes the payment and returns the payment con-<sup>fi</sup>rmation to the shipper.

21. The goods are delivered by the shipper.

22. The sender is informed to pay for the shipping goods after the payment made by the consignor to the shipper.

23. The consignor generates a delivery order and sends a release form to the buyer.

24. When the goods arrive, the shipper sends an arrival notice to the buyer. The buyer picks up the goods with the release form.

![](/api/attachments/ZHKPJRVS/fulltext/images/4afb468fbcabff1be632a6dcb475759acdc5a8d9eb976730ef232ed9547fc933.jpg)  
Fig. 1. Typical scenario of a multi-modal transportation business process.

In the multi-modal transportation business process, each partner knows the tasks of their own work<sup>fl</sup>ow, and the coordination approach among different partners is prede<sup>fi</sup>ned. However, the model for the overall transportation business process is not known by any partner. In this paper, we use a process mining based integration approach to obtain the model of a cross-organizational work<sup>fl</sup>ow. The multi-modal transportation business process is used as a running example to explain the proposed approach.

## 3.2. Framework for workflow integration based on process mining

The framework for work<sup>fl</sup>ow integration using process mining technology is shown in Fig. 2 and includes the following.

• Recording running log. While a cross-organizational work<sup>fl</sup>ow system is running, the work<sup>fl</sup>ow management system of each organization can record the running log and store it in its own database. The running log includes information about the activity name, the start and end times of each activity, the required resources, the released resources, the messages exchanged, etc. If the execution of an activity does not require or release a resource, the resource information can be ignored in the running log. If no messages are exchanged with other work<sup>fl</sup>ows or the message information can be ignored, the message information is not recorded in the running log.

• Process mining from running log. From the running log collected from each organization, the process mining algorithm attempts to discover the model for its own work<sup>fl</sup>ow. Unlike the running log in most studies of process mining [3,5,6,20,21], the running log in this paper records information on the activity event and information on the resource allocation and the messages exchanged. The mining results can be represented in the formalized form of Petri nets extended with message and resource information

• Coordination pattern mining. To discover the coordination patterns between different organizations, a middle-ware has been implemented to integrate the work<sup>fl</sup>ow running logs between different organizations. From the running log integrated between two or more organizations, the process mining algorithm attempts to discover the coordination patterns among different organization work<sup>fl</sup>ows. The mining results are also represented in the formalized form of Petri nets extended with message and resource information.

• Process integration according to coordination patterns. The model mined from the running log of each organization only describes its own work<sup>fl</sup>ow. To obtain the model for the cross-organizational work<sup>fl</sup>ow, the work<sup>fl</sup>ow models discovered in each organization must be integrated. The coordination patterns de<sup>fi</sup>ned between different organizations present the integration approach. In this paper, the four coordination patterns de<sup>fi</sup>ned in Section 5 are applied for process integration. According to the coordination patterns published, the models mined from each organization are integrated to obtain the cross-organizational work<sup>fl</sup>ow model.

## 4. Petri net model and coordination patterns for cross-organizational work<sup>fl</sup>ows

In this section, a work<sup>fl</sup>ow model extending with information about message exchanged and resource shared is proposed <sup>fi</sup>rst, then four kinds of coordination patterns for cross-organizational work<sup>fl</sup>ows are de<sup>fi</sup>ned based on the model proposed.

![](/api/attachments/ZHKPJRVS/fulltext/images/38d29270da8aa9f0e621699568e811203b4ed1c7fd6166d4df43ffdfb50b91dc.jpg)  
Fig. 2. Framework for work<sup>fl</sup>ow integration based on process mining.

## 4.1. Primary — Petri net model for cross-organizational workflows

As methods of modeling and analyzing current and parallel systems, Petri nets [11] have shown their ability to deal with concurrency and con<sup>fl</sup>ict, and have been widely used to model, analyze, and verify systems [24,27]. Some of the essential terminology and notation for Petri nets are as follows [10,11,13,26].

A triple $N { = } ( P , T ; F )$ is named as a net iff $( 1 ) { \cal P } \cap { \cal T } = \emptyset , { \cal P } \cup { \cal T } \not = \emptyset ;$ (2) $F \subseteq ( P \times T ) \cup ( T \times P ) ;$ and (3) Do $n ( F ) \cup C o d ( F ) = P \cup T .$ For all $x { \in } P \cup T ,$ the set $\mathbf { \dot { \sigma } } _ { X } = \{ y | y \in P \cup T \land ( y , x ) \in F \}$ is the pre-set of x and the set $x ^ { \bullet } =$ $\{ y | y \in P \cup T \land ( x , y ) \in F \}$ is the post-set of x. Let $N { = } ( P , T ; F )$ be a net. $N _ { 1 } { = } ( P _ { 1 } , T _ { 1 } ; F _ { 1 } )$ is a subnet of $N { = } ( P , T ; F )$ if $P _ { 1 } \subseteq P , \ T _ { 1 } \subseteq T ,$ and $F _ { 1 } =$ $( ( P _ { 1 } \times T _ { 1 } ) \cup ( T _ { 1 } \times P _ { 1 } ) ) \cap F . \mathrm { ~ A ~ }$ Petri net is a 4-tuple $\Sigma = ( P , T ; F , M _ { 0 } )$ such that $N { = } ( P , T ; F )$ is a net and $M _ { 0 } { : } P {  } Z ^ { + }$ is the initial marking of Σ where $Z ^ { + }$ is the non-negative integer set. The Petri net model used to model work<sup>fl</sup>ows is named the WF-net [16].

De<sup>fi</sup>nition 1. (Work<sup>fl</sup>ow net) A Petri net $\Sigma = ( P , T ; F , M _ { 0 } )$ is a WF-net (Work<sup>fl</sup>ow net) if and only if:

(1) There is one source place $i \in P$ such that $\because - \varnothing .$

(2) There is one sink place $o \in P$ such that $o ^ { \bullet } { = } \emptyset$

(3) Every node $x { \in } P \cup T$ is on a path from i to o.

$$
(4) \forall p \in P, M _ {0} (p) = \left\{ \begin{array}{l l} 1 & p = i \\ 0 & \text { otherwise }. \end{array} \right.
$$

In a WF-net, the transition set T is used to represent the activities of a work<sup>fl</sup>ow, and the source place and sink place represent the start and the end of the work<sup>fl</sup>ow, respectively. To describe the collaboration information of cross-organizational work<sup>fl</sup>ows, such as shared resources, messages exchanged, synchronized activities and so on, we propose the RM\_WF\_Net, which is a WF-net model extended with resource and message information.

De<sup>fi</sup>nition 2. (RM\_WF\_Net) A Petri net $\Sigma = ( P , T ; F , M _ { 0 } )$ is an RM\_WF\_Net iff

(1) $P = P _ { L } \cup P _ { R } \cup P _ { M } , P _ { L } \cap P _ { R } = \emptyset , P _ { L } \cap P _ { M } = \emptyset .$ , and $P _ { R } \cap P _ { M } = \emptyset ;$ $P _ { R } \subseteq P$ represents the resources involved in the work<sup>fl</sup>ow; and $P _ { M } \subseteq P$ represents the messages exchanged in the work<sup>fl</sup>ow;

(2) $F { = } F _ { L } { \cup } F _ { R } { \cup } F _ { M } ,$ where

(2.1) $F _ { L } { = } ( P _ { L } { \times } T ) \cup ( T { \times } P _ { L } )$ , represents the logical structure of the model;

(2.2) $F _ { R } = ( P _ { R } \times T ) \cup ( T \times P _ { R } ) , \ \forall x , y \in T \cup P _ { R } , \ ( x , y ) \in F _ { R }$ iff $( y , x ) \in F _ { R } , \ F _ { R }$

(2.3) $\begin{array} { r } { F _ { M } = ( P _ { M } \times T ) \cup ( T \times P _ { M } ) , \forall x , y \in T \cup P _ { M } , ( x , y ) \in F _ { M } \mathrm { i f f } ( y , x ) \not \in F _ { M } . } \end{array}$

represents the message relations of the model;

(3) $\left( P _ { L } , T ; F _ { L } \right)$ is a WF-net;

$$
(4) \forall p \in P, M _ {0} (p) = \left\{ \begin{array}{l l} 1 & p \in P _ {R} \cup \{i \} \\ 0 & \text { otherwise } \end{array} \right., \text { where } i \in P _ {L} \wedge \cdot i = \varnothing .
$$

An RM\_WF\_Net is used to represent the model of a work<sup>fl</sup>ow within a single organization, where the transition set is used to represent the set of activities involved in the work<sup>fl</sup>ow. In comparison to the traditional WF\_net [16], the main difference of an RM\_WF\_Net de<sup>fi</sup>ned in De<sup>fi</sup>nition 2 is that three components are involved in the place set, $\mathrm { i } . \mathbf { e } . , P { = } P _ { L } \cup P \mathbf { - }$ ${ } _ { R } \cup { } P _ { M } .$ In De<sup>fi</sup>nition 2, the resource set $\left( P _ { R } \right)$ and the message set $\left( P _ { M } \right)$ are separated from the normal place set (P ). All of the messages are produced during the execution of a work<sup>fl</sup>ow, so each message place does not contain any token in the model before the work<sup>fl</sup>ow is executed.

The <sup>fi</sup>ring rule of an RM\_WF\_Net is the same as that of a standard Petri net. $\forall t { \in } T , \forall M { \in } R ( M _ { 0 } )$ , t is enabled under M iff $\forall p \in \cdot _ { t , M ( p ) \geq 1 }$ All other properties such as reachability, boundedness, etc., can be de-<sup>fi</sup>ned as a standard Petri net. We do not explain and de<sup>fi</sup>ne them here.

## 4.1.1. Example 1. An example of an RM\_WF\_Net

An example of an RM\_WF\_Net is shown in Fig. 3, which represents the work<sup>fl</sup>ow of the Consignor organization in a multi-modal transportation business process. The meanings for each transition and place are shown in Table 1. To distinguish the resource and message places from the normal places, they are represented by circles in double lines in the model. Speci<sup>fi</sup>cally, in this example:

(1) $T = \{ A _ { i } , 1 \leq i \leq 1 5 \}$ represents the activities.

(2) $P _ { L } = \{ p _ { i } , 0 \leq i \leq 1 5 \}$ is used to connect the relations between activities, where p and $p _ { 1 5 }$ represent the start and end of the work<sup>fl</sup>ow, respectively.

(3) $P _ { R } = \{ p _ { r 1 } \}$ presents the resources involved in the work<sup>fl</sup>ow.

(4) $P _ { M } = \{ p _ { m i } , 1 \leq i \leq 1 3 \}$ presents the messages exchanged with other work<sup>fl</sup>ows.

There are 15 activities in this model. According to the meanings for each transition and place shown in Table 1, the main steps in the consignor work<sup>fl</sup>ow are as follows.

(1) After receiving the message Application Form, the consignor work<sup>fl</sup>ow executes the <sup>fi</sup>rst activity Application Acceptance.

(2) The second activity is to Generate Contract.

(3) After the contract is generated, the work<sup>fl</sup>ow executes the activity Contract Signed where Consignor Manager is one required resource.

(4) After the contract is signed, the consignor makes a booking request and sends Request Form<sub>1</sub> and Request Form<sub>2</sub>, respectively.

(5) After receiving messages Acceptance Notice and Acceptance Notice , the consignor starts the activity Packing Preparation and sends out the message Packing Notice.

(6) The next activity is to wait for Goods Arrival.

(7) After the goods arrive, the consignor completes the activity Container Packing.

(8) The next activity is to complete the customs declaration procedure. The procedure includes three activities, namely, Generate Declaration Form, Declaration Application, and Declaration Acceptance.

(9) After the customs declaration, the consignor Forwards the goods for Loading.

(10) According to the message Issue Waybill, the consignor pays and sends out the Payment Verification .

(11) According to the message Terminal Receipt, the consignor makes the second payment and sends out the messages Payment Verification and Payment Receipt.

(12) After receiving the Payment Verificatio $n _ { 4 } ,$ the consignor implements the activity Generate Delivery Order and sends the goods Release Form.

In this section, the Petri net model is de<sup>fi</sup>ned only for a work<sup>fl</sup>ow executed in a single organization. In the next section, the coordination patterns are de<sup>fi</sup>ned. According to the coordination patterns between different organizations, the formal model for a cross-organizational work<sup>fl</sup>ow can be obtained from the model of each organization by using process integration.

## 4.2. Coordination patterns for cross-organizational workflows

We assume that the execution of each activity in a work<sup>fl</sup>ow requires a duration, and activities need to access resources during their executions. When the execution of an activity requires resources, the activity must wait for the required resources to be released if they have been occupied exclusively and locked by other activities being executed. A resource is de<sup>fi</sup>ned as any entity required by an activity for its execution, such as a document, a database table, an appliance (for example, a printer), an application, or even an actor. The resources discussed in this paper are all exclusive and reusable. That is, if a resource is accessed by an activity, it will be locked and no other activities can access it until the activity is <sup>fi</sup>nished. After the activity has been executed, the locked resources are released and other activities can access them if necessary.

Without loss of generality, we only de<sup>fi</sup>ne the work<sup>fl</sup>ow coordination patterns between two organizations. We de<sup>fi</sup>ne four kinds of patterns for cross-organizational work<sup>fl</sup>ow coordination: coordination with synchronized activities, coordination with messages exchanged, coordination with shared resources, and coordination with abstract procedures. More details about these four coordination patterns are discussed below.

![](/api/attachments/ZHKPJRVS/fulltext/images/de393bc5819a0254d6d3602e78c5f985c71896d06b2a31cbb35345cab3d3e443.jpg)  
Fig. 3. An RM\_WF\_Net.

## 4.2.1. Pattern 1: coordination with synchronized activities

In a cross-organizational work<sup>fl</sup>ow, certain steps of the work<sup>fl</sup>ow must be completed through involving two organizations simultaneously. For example, in the multi-modal transportation business process, the signing of the transportation contract must be completed by the sender and consignor together. Thus, the contract signing is a single synchronized activity for coordinating the process between the sender and consignor. The same information about the start and end times of signing the contract can be recorded.

An example of this kind of pattern is shown in Table 2. The activities $A _ { 1 }$ and A are synchronized during the execution of the work<sup>fl</sup>ow across Organization 1 and Organization 2, which means that the start and end times of synchronized activity $A _ { 1 }$ (or A ) during the running of the private work<sup>fl</sup>ow of Organization 1 are the same as those of Organization 2.

A formal de<sup>fi</sup>nition of coordination with synchronized activities is presented in De<sup>fi</sup>nition 3.

De<sup>fi</sup>nition 3. (Coordination with synchronized activities) Let $\Sigma _ { 1 } =$ $\left( P _ { 1 } , T _ { 1 } ; F _ { 1 } , M _ { 0 1 } \right)$ and $\Sigma _ { 2 } = ( P _ { 2 } , T _ { 2 } ; F _ { 2 } , M _ { 0 2 } )$ be the work<sup>fl</sup>ow models for two organizations. If

(1) $T _ { 1 } \cap T _ { 2 } \neq \emptyset ,$ and (2) $P _ { 1 } \cap P _ { 2 } = \emptyset ,$

$\Sigma _ { 1 }$ and Σ are named as coordination with synchronized activities. Let $\Sigma = ( P , T ; F , M _ { 0 } )$ be the composed model by $\Sigma _ { 1 }$ and $\Sigma _ { 2 }$ with synchronized activities. Then

(1) $P { = } P _ { 1 } \cup P _ { 2 } ;$

(2) $T { = } T _ { 1 } \cup T _ { 2 } ;$

(3) $F { = } F _ { 1 } \cup F _ { 2 } ;$

$$
M _ {0} = M _ {0 1} \cup M _ {0 2}.
$$

Meaning of each activity and place in the model shown in Fig. 3.

<table><tr><td>Transition</td><td>Meaning</td><td>Place</td><td>Meaning</td></tr><tr><td> $A_{1}$ </td><td>Application Acceptance</td><td> $p_{m1}$ </td><td>Application Form</td></tr><tr><td> $A_{2}$ </td><td>Generate Contract</td><td> $p_{m2}$ </td><td>Request Form $_{1}$ </td></tr><tr><td> $A_{3}$ </td><td>Contract Signed</td><td> $p_{m3}$ </td><td>Request Form $_{2}$ </td></tr><tr><td> $A_{4}$ </td><td>Booking Request</td><td> $p_{m4}$ </td><td>Acceptance Notice $_{1}$ </td></tr><tr><td> $A_{5}$ </td><td>Packing Preparation</td><td> $p_{m5}$ </td><td>Acceptance Notice $_{2}$ </td></tr><tr><td> $A_{6}$ </td><td>Goods Arrival</td><td> $p_{m6}$ </td><td>Packing Notice</td></tr><tr><td> $A_{7}$ </td><td>Container Packing</td><td> $p_{m7}$ </td><td>Issue Waybill</td></tr><tr><td> $A_{8}$ </td><td>Declaration Form Generation</td><td> $p_{m8}$ </td><td>Payment Verification $_{2}$ </td></tr><tr><td> $A_{9}$ </td><td>Declaration Application</td><td> $p_{m9}$ </td><td>Terminal Receipt</td></tr><tr><td> $A_{10}$ </td><td>Declaration Acceptance</td><td> $p_{m10}$ </td><td>Payment Receipt</td></tr><tr><td> $A_{11}$ </td><td>Forward</td><td> $p_{m11}$ </td><td>Payment Verification $_{3}$ </td></tr><tr><td> $A_{12}$ </td><td>Loading</td><td> $p_{m12}$ </td><td>Payment Verification $_{4}$ </td></tr><tr><td> $A_{13}$ </td><td>Payment $_{1}$ </td><td> $p_{m13}$ </td><td>Release Form</td></tr><tr><td> $A_{14}$ </td><td>Payment $_{2}$ </td><td>-</td><td>-</td></tr><tr><td> $A_{15}$ </td><td>Generate Delivery Generated</td><td> $p_{r1}$ </td><td>Consignor Manager</td></tr></table>

In this coordination pattern, there is at least one common activity between the private work<sup>fl</sup>ows of the two involved organizations. If $A _ { i } \in T _ { 1 } \cap T _ { 2 } ,$ , then $A _ { i }$ is an activity executed synchronically between $\Sigma _ { 1 }$ and $\Sigma _ { 2 }$ so that the start time and end time of $A _ { i }$ should be consistent between them.

The coordination pattern and representation.  
![](/api/attachments/ZHKPJRVS/fulltext/images/404803cd3b5236dd7b46a00ff7c116ea8eef81de8ee4d7ae914fc0465ec75903.jpg)

## 4.2.2. Pattern 2: coordination with messages exchanged

During the execution of a work<sup>fl</sup>ow, there are many cases of messages being exchanged between different partners. For example, after the buyer organization makes a payment, a message payment verification is sent to the sender, and the work<sup>fl</sup>ows are thus coordinated with exchanged message payment verification between the buyer and the sender. An example of this kind of coordination pattern is given in Table 2. In this example, $p _ { m 1 }$ and $p _ { m 2 }$ are two message places. After the execution of activity $A _ { 1 } ,$ , place $p _ { m 1 }$ obtains one token, which means that activity $A _ { 3 }$ receives the message from $A _ { 1 }$

The formal de<sup>fi</sup>nition of coordination with messages exchanged is presented below.

De<sup>fi</sup>nition 4. (Coordination with messages exchanged) Let $\Sigma _ { 1 } = ( P _ { 1 } ,$ $T _ { 1 } ; F _ { 1 } , M _ { 0 1 } )$ and $\Sigma _ { 2 } = ( P _ { 2 } , T _ { 2 } ; F _ { 2 } , M _ { 0 2 } )$ be the work<sup>fl</sup>ow models for two organizations, where $P _ { i } { = } P _ { L i } \cup P _ { R i } \cup P _ { M i } \ : ( i { = } 1 , 2 )$ . If

(1) $P _ { M 1 } \cap P _ { M 2 } \neq \emptyset ,$

(2) $P _ { L 1 } \cap P _ { L 2 } = \emptyset ,$

(3) $P _ { R 1 } \cap P _ { R 2 } = \emptyset , \mathrm { a n d }$

(4) $T _ { 1 } \cap T _ { 2 } = \emptyset ,$

$\Sigma _ { 1 }$ and $\Sigma _ { 2 }$ are named coordination with messages exchanged. Let $\Sigma = ( P , T ; F , M _ { 0 } )$ be the composed model by $\Sigma _ { 1 }$ and $\Sigma _ { 2 }$ with messages exchanged. Then

(1) $P { = } P _ { 1 } \cup P _ { 2 } ;$

(2) $T { = } T _ { 1 } \cup T _ { 2 } ;$

(3) $F { = } F _ { 1 } \cup F _ { 2 } { \mathrm { ; } }$

(4) $M _ { 0 } = M _ { 0 1 } \cup M _ { 0 2 } .$

In the coordination with message exchanged, there is at least one common message place between the work<sup>fl</sup>ows of the two organizations.

## 4.2.3. Pattern 3: coordination with shared resources

Because resources are often accessed exclusively by a private work<sup>fl</sup>ow, resource allocation is important in avoiding resource con<sup>fl</sup>ict between different organizations when more than one private work<sup>fl</sup>ow needs to access the same resource. For example, in the multi-modal transportation business process, resources such as boxcars, goods stations, and customs brokers are accessed by different private work<sup>fl</sup>ows. However, if resources such as a boxcar and a goods station are occupied by an activity in a private work<sup>fl</sup>ow, activities that require the same resource in another private work<sup>fl</sup>ow must wait until the resource is released. The resource allocation and resource-con<sup>fl</sup>ict control are important for two work<sup>fl</sup>ows coordinated with shared resources.

An example of this coordination pattern is given in Table 2, where $p _ { r 1 }$ and $p _ { r 2 }$ are two resource places. If resource $p _ { r 1 }$ is occupied by activity $A _ { 1 } , A _ { 3 }$ must wait for the $p _ { r 1 }$ to be released by $A _ { 1 }$ after its execution is completed.

The formal de<sup>fi</sup>nition for coordination with shared resources is presented below.

De<sup>fi</sup>nition 5. (Coordination with shared resources) Let $\Sigma _ { 1 } = ( P _ { 1 } , T _ { 1 } ;$ $F _ { 1 } , M _ { 0 1 } )$ and $\Sigma _ { 2 } = ( P _ { 2 } , T _ { 2 } ; F _ { 2 } , M _ { 0 2 } )$ be the work<sup>fl</sup>ow models for two organizations, where $P _ { i } = P _ { L i } \cup P _ { R i } \cup P _ { M i } \ : ( i = 1 , 2 )$ . If

(1) $P _ { R 1 } \cap P _ { R 2 } \neq \emptyset ,$

(2) $P _ { L 1 } \cap P _ { L 2 } = \emptyset ,$

(3) P<sub>M1</sub>∩P<sub>M2</sub>=∅, and

(4) $T _ { 1 } \cap T _ { 2 } = \emptyset ,$

$\Sigma _ { 1 }$ and $\Sigma _ { 2 }$ are named coordination with shared resources.

Let $\Sigma = ( P , T ; F , M _ { 0 } )$ be the composed model by $\Sigma _ { 1 }$ and $\Sigma _ { 2 }$ with shared resources. Then

(1) $P { = } P _ { 1 } \cup P _ { 2 } ;$

(2) $T { = } T _ { 1 } \cup T _ { 2 } ;$

(3) $F { = } F _ { 1 } \cup F _ { 2 } ;$

(4) $M _ { 0 } = M _ { 0 1 } \cup M _ { 0 2 } .$

In this coordination pattern, there is at least one resource shared between two organizations. $\mathrm { I f } p _ { r i } { \in } P _ { R 1 } \cap P _ { R 2 }$ , then $p _ { r i }$ is a resource shared between $\Sigma _ { 1 }$ and $\Sigma _ { 2 } .$ Because the resource is exclusively used, if $p _ { r i }$ is occupied and locked by any one activity in $\Sigma _ { 1 }$ , then any other activities requiring $p _ { r i }$ in $\Sigma _ { 2 }$ must wait for $p _ { r i }$ to be released.

## 4.2.4. Pattern 4: coordination with abstract procedures

To coordinate with other organizations, the requirements and outputs of a private work<sup>fl</sup>ow can be published with the details being packaged as a black box. In the work<sup>fl</sup>ow of the consignor shown in Fig. 3, for example, if the consignor does not want to make known the customs declaration procedure, the three activities involved – Generate Declaration Form, Declaration Application, and Declaration Acceptance – can be packaged as an abstract procedure published for the bene<sup>fi</sup>t of partners if the consignor does not want to make the customs declaration procedure known. Before giving the de<sup>fi</sup>nition of this kind of pattern, the formal de<sup>fi</sup>nition for an abstract procedure is <sup>fi</sup>rst given.

De<sup>fi</sup>nition 6. (Abstract procedure) Let $\Sigma _ { P } { = } \left( P _ { P } { , } T _ { P } { ; } F _ { P } { , } M _ { 0 P } \right)$ be a subnet of $\Sigma = ( P , T ; F , M _ { 0 } ) . \ \Sigma _ { p }$ is an abstract procedure of Σ, if

(1) there is at least one input transition $t \in T _ { P }$ such that $\cdot _ { t = \emptyset }$

$$
t \in T _ {P}
$$

$$
t ^ {\bullet} = \emptyset
$$

(3) there is no place $p { \in } P _ { L P } \left( P _ { L P } { \subseteq } P _ { P } \right)$ such that $\cdot _ { p = \emptyset }$

(4) there is no place $p { \in } P _ { L P } \left( P _ { L P } { \subseteq } P _ { P } \right)$ such that $p ^ { \bullet } = \varnothing$ , and

(5) every node $x { \in } P _ { P } \cup T _ { P }$ is on a path from one input transition to one output transition. Such nodes are named inner nodes of $\Sigma _ { P } .$

The model shown in Fig. 4 is an example of an abstract procedure of the model shown in Fig. 3, which represents a customs declaration procedure consisting of three activities, Generate Declaration Form, Declaration Application, and Declaration Acceptance.

The content of an abstract procedure $\Sigma _ { P }$ in one model $\Sigma$ can be replaced by a special transition $t _ { p } ,$ denoted by $\begin{array} { r } { \Sigma - \sum _ { P } / t _ { p } . } \end{array}$ The replacement operation is de<sup>fi</sup>ned as follows.

(1) Delete all of the inner nodes (places and transitions) and the arcs among the inner nodes of the abstract procedure.

(2) Add a new special transition (denoted by $t _ { p } )$ to represent the abstract procedure.

(3) If there is one relation arc from some of the places not deleted to some of the transitions deleted, then add one new relation arc from the place to the newly-added special transition.

(4) If there is one relation arc from some of the transitions deleted to some of the places undeleted, then add one new relation arc from the newly added special transition to the corresponding place.

To distinguish the special transition added to represent the abstract procedure, it is drawn with double lines in the model. For example, after the model shown in Fig. 4 is replaced by the special transition $A _ { 8 - 9 - 1 0 } ,$ the replacement result of the model shown in Fig. 3 is shown in $\mathrm { F i g . } 5 .$

An abstract procedure can be regarded as a normal activity by other work<sup>fl</sup>ows that are involved in the coordination. An example of the coordination pattern with abstract procedures between the work<sup>fl</sup>ows crossing two organizations is shown in Table 2. In this example, activities $A _ { 1 }$ and A in the work<sup>fl</sup>ow of Organization 1 are packaged as a special activity $A _ { 1 2 } ,$ , which is synchronized with the work<sup>fl</sup>ow of Organization 2.

The formal de<sup>fi</sup>nition for coordination with abstract procedures is given below.

De<sup>fi</sup>nition 7. (Coordination with abstract procedures) Let $\Sigma _ { 1 } = ( P _ { 1 }$ $T _ { 1 } ; F _ { 1 } , M _ { 0 1 } )$ and $\Sigma _ { 2 } = ( P _ { 2 } , T _ { 2 } ; F _ { 2 } , M _ { 0 2 } )$ be the work<sup>fl</sup>ow models for two organizations and $\Sigma _ { P } { = } \left( P _ { P } { , } T _ { P } ; F _ { P } { , } M _ { 0 P } \right)$ be an abstract procedure of $\Sigma _ { 1 }$ $\operatorname { I f } \exists t _ { p } \in T _ { 2 }$ satis<sup>fi</sup>es the following:

![](/api/attachments/ZHKPJRVS/fulltext/images/aa80d13cab047cb1789a41726fd5bb064f417430612899f24777d3e7f8e6861a.jpg)  
Fig. 4. Example of an abstract procedure.

<sub>(</sub>1) $\mathbf { \dot { \tau } } t _ { p } = \bigcup _ { t \in T _ { p } \wedge \mathbf { \dot { \tau } } t = \emptyset } \{ x | ( x , t ) { \in } F _ { 1 } \} ,$

(2) $t _ { p } ^ { \bullet } = \operatorname * { i } _ { t \in { \cal T } _ { P } \wedge t ^ { \bullet } = \emptyset } \{ x | ( t , x ) \in { \cal F } _ { 1 } \} ,$

(3) $t _ { p } \cdot R e s o u r c e R e q = \bigcup _ { t \in T _ { P } }$ t  ResourceReq;

(4) $t _ { p } \cdot R e s o u r c e R e l = \bigcup _ { t \in T _ { P } }$ t ResourceRel;

(5) t MessageRec ∪ t MessageRec; and $\forall p { \in } t _ { p }$ :MessageRec; t∈T $\dot { M _ { 0 } } ( p ) = M _ { 0 P } ( p ) ,$

(6) $\begin{array} { l } { { t _ { p } \cdot M e s s a g e S e n t = \bigcup } } \\ { { M _ { 0 } ( p ) = M _ { 0 P } ( p ) , } } \end{array}$ t MessageSent; and $\forall p { \in } t _ { p }$ MessageSent;

$\Sigma _ { 1 }$ and $\Sigma _ { 2 }$ are named coordination with abstract procedures $\Sigma _ { P } .$ Let $\Sigma = ( P , T ; F , M _ { 0 } )$ be the composed model by $\Sigma _ { 1 }$ and $\Sigma _ { 2 }$ with abstract procedures $\Sigma _ { P } ,$ and have replacement operation $\Sigma - \Sigma _ { P } / t _ { p } .$ . Then

(1) $P { = } P _ { 1 } \cup P _ { 2 } ;$

(2) $T { = } T _ { 1 } \cup T _ { 2 } ;$

(3) $F { = } F _ { 1 } \cup F _ { 2 } ;$

$$
M _ {0} = M _ {0 1} \cup M _ {0 2}. \tag {4}
$$

Four coordination patterns have been de<sup>fi</sup>ned for the situations in which two organizations are involved. Of course, in practice, more than two organizations can be integrated by using the given coordination patterns. When more than two organizations are coordinated with different patterns, they can be transformed into two coordinated organizations to be discussed. Therefore, two organizations coordinated with one pattern is the basic model of cross-organizational coordination. The notation and meanings of the four coordination patterns are listed in Table 2.

## 5. Work<sup>fl</sup>ow mining for single organization

In order to build the coordination relations between different organizations, the proposed RM\_WF\_Net model is extended with message and resource information. Thus, the task to discover the model for an inter-organization work<sup>fl</sup>ow must obtain the information about message exchanged and resource shared. While collecting the running log data, the information about message exchanged and resource shared is also collected as part contents of the running log data. Thus, the existing process discovery techniques [20,21] are not easy to directly discover the work<sup>fl</sup>ow model for an inter-organization. Following the basic idea of process mining algorithms available [20,21], this section presents a mining algorithm that can deal with the running log data extending with the information about message exchanged and resource shared.

## 5.1. Formal definitions about running log

While a work<sup>fl</sup>ow runs, the management system can record information on resource allocation, messages exchanged, and event information about each activity implemented. For example, Table 3 shows part of the running log of the work<sup>fl</sup>ow of the consignor that was presented in Fig. 3.

From the running log in Table 3, we know that the execution of the <sup>fi</sup>rst activity Application Acceptance starts after receiving the message Application Form, and does not require or release any resource. Its start and end times are 11:00 Aug 01 and 11:03 Aug 01, respectively. In the third log, the resource required and released by the activity Contract Signed is Consignor Manager. In other words, the execution of Contract Signed requires Consignor Manager as a resource and releases it after the completion of the activity. There are 15 log records in Table 3 that record the running information of one work<sup>fl</sup>ow instance of the consignor that was presented in Fig. 3.

Given that a set of activities A is executed in a work<sup>fl</sup>ow WF, we de<sup>fi</sup>ne the following concepts regarding the running log of WF.

De<sup>fi</sup>nition 8. (Event record) An event record of WF is an 8-tuples, RRecord= (Case, Activity, Time , Time , ResourceReq, ResourceRel, MessageRec, MessageSent), where:

(1) Case is the ID indicating which case the log belongs to.

(2) Activity is the name (ID) of the activity.

(3) Time is the start time of Activity.

(4) Time is the end time of Activity, and $T i m e _ { e } { \geq } T i m e _ { s }$

(5) ResourceReq represents the required resources of the activity to be implemented.

(6) ResourceRel represents the released resources after the execution of the activity.

(7) MessageRec represents the messages received before the execution of the activity.

(8) MessageSent represents the messages sent by the activity after its execution.

An event record presents the execution information of each activity in one instance of the work<sup>fl</sup>ow. An activity cannot be executed if its required resources are not prepared well or the exchanged messages are not received. In De<sup>fi</sup>nition 8:

(1) Time<sub>s</sub> records the start time of Activity. In the following discussion, it is denoted by Activity·Time directly.

(2) Time<sub>e</sub> records the end time of Activity, and is denoted by Activity·Time directly.

(3) ResourceReq presents the set of the required resources of Activity, denoted by Activity·ResourceReq. If Activity·ResourceReq=∅ or the event record does not contain any resource information, the execution of the activity does not require any resources or the resource information can be ignored.

![](/api/attachments/ZHKPJRVS/fulltext/images/043175a971ca1719620f7fd6d9687c47f75fe45ea1d1c718482fd4f9df5090f2.jpg)  
Fig. 5. Example of a replacement operation.

Table 3  
Part of the running log of the Consignor work<sup>fl</sup>ow.

<table><tr><td>Case</td><td>Activity</td><td>Start Time</td><td>End Time</td><td>ResourceReq</td><td>ResourceRel</td><td>MessageRec</td><td>MessageSent</td></tr><tr><td>1</td><td> $A_1$ </td><td>11:00 Aug 01</td><td>11:03 Aug 01</td><td>∅</td><td>∅</td><td> $\{p_{m1}\}$ </td><td>∅</td></tr><tr><td>1</td><td> $A_2$ </td><td>11:04 Aug 01</td><td>11:08 Aug 01</td><td>∅</td><td>∅</td><td>∅</td><td>∅</td></tr><tr><td>1</td><td> $A_3$ </td><td>11:30 Aug 01</td><td>11:45 Aug 01</td><td> $\{p_{r1}\}$ </td><td> $\{p_{r1}\}$ </td><td>∅</td><td>∅</td></tr><tr><td>1</td><td> $A_4$ </td><td>11:46 Aug 01</td><td>11:50 Aug 01</td><td>∅</td><td>∅</td><td>∅</td><td> $\{p_{m2},p_{m3}\}$ </td></tr><tr><td>1</td><td> $A_5$ </td><td>11:56 Aug 01</td><td>12:04 Aug 01</td><td>∅</td><td>∅</td><td> $\{p_{m4},p_{m5}\}$ </td><td> $\{p_{m6}\}$ </td></tr><tr><td>1</td><td> $A_6$ </td><td>14:24 Aug 01</td><td>14:41 Aug 01</td><td>∅</td><td>∅</td><td>∅</td><td>∅</td></tr><tr><td>1</td><td> $A_7$ </td><td>14:42 Aug 01</td><td>14:58 Aug 01</td><td>∅</td><td>∅</td><td>∅</td><td>∅</td></tr><tr><td>1</td><td> $A_8$ </td><td>14:59 Aug 01</td><td>15:04 Aug 01</td><td>∅</td><td>∅</td><td>∅</td><td>∅</td></tr><tr><td>1</td><td> $A_9$ </td><td>15:05 Aug 01</td><td>15:14 Aug 01</td><td>∅</td><td>∅</td><td>∅</td><td>∅</td></tr><tr><td>1</td><td> $A_{10}$ </td><td>15:15 Aug 01</td><td>15:32 Aug 01</td><td>∅</td><td>∅</td><td>∅</td><td>∅</td></tr><tr><td>1</td><td> $A_{11}$ </td><td>15:33 Aug 01</td><td>15:46 Aug 01</td><td>∅</td><td>∅</td><td>∅</td><td>∅</td></tr><tr><td>1</td><td> $A_{12}$ </td><td>15:47 Aug 01</td><td>16:28 Aug 01</td><td>∅</td><td>∅</td><td>∅</td><td>∅</td></tr><tr><td>1</td><td> $A_{13}$ </td><td>16:39 Aug 01</td><td>16:44 Aug 01</td><td>∅</td><td>∅</td><td> $\{p_{m7}\}$ </td><td> $\{p_{m8}\}$ </td></tr><tr><td>1</td><td> $A_{14}$ </td><td>08:55 Aug 04</td><td>09:00 Aug 04</td><td>∅</td><td>∅</td><td> $\{p_{m9}\}$ </td><td> $\{p_{m10},p_{m11}\}$ </td></tr><tr><td>1</td><td> $A_{15}$ </td><td>09:16 Aug 04</td><td>09:20 Aug 04</td><td>∅</td><td>∅</td><td> $\{p_{m12}\}$ </td><td> $\{p_{m13}\}$ </td></tr></table>

(4) ResourceRel presents the set of the released resources after the execution of Activity, denoted by Activity·ResourceRel. If Activity·ResourceRel =∅ or the event record does not contain any resource information, it means that the execution of the activity does not release any resources or the resource information can be ignored.

(5) MessageReceived presents the messages received before the execution of Activity, denoted by Activity·MessageReceived. If Activity·MessageReceived=∅ or the event record does not contain any message information, the execution of the activity does not need to receive any messages before its execution or the resource information can be ignored.

(6) MessageSent presents the messages sent by the activity after the execution of Activity, denoted by Activity·MessageSent. If Activity·MessageSent=∅ or the event record does not contain any message information, the execution of the activity does not send any messages or the message information can be ignored.

A running case of a WF is a set of event records for its one instance, denoted by RCase. If $\forall A _ { i } \in A ,$ , RCase is complete if there is one and only one event record of A in RCase. A running log of a WF is a set of running cases, denoted by RLog.

Table 3 shows the part of the running log that includes only one running case, Case , which includes 15 event records.

De<sup>fi</sup>nition 9. (Activity set) Let RLog be the running log of a work<sup>fl</sup>ow,

(1) For each $R C a s e _ { i } { \in } R L o g , A c t i v i t y S e t ( R C a s e _ { i } ) { = } \{ A _ { j } | \exists R u n L o g { \in } R C a s e _ { i } , $ such that Run $L o g { = } ( C a s e , A _ { j } ,$ Time , Time , ResourceReq, ResourceRel, MessageRec, MessageSent) $_ { | } ( 1 \leq j \leq | R C a s e _ { i } | ) \}$ is the activity set of RCase .

(2) ActivitySet RLog ∪ ActivitySet RCase is the activity RCase ∈RLog set of RLog.

For instance, in the example given in Table 3, ActivitySet(RCase )= $\{ A _ { j } , 1 \le j \le 1 5 \}$

De<sup>fi</sup>nition 10. (Pre-activities and post-activities) Let RLog be the running log of a work<sup>fl</sup>ow, $\forall A _ { i } , A _ { j } \in$ ActivitySet(RLog), $A _ { j }$ is one of the post-activities of $A _ { i }$ (or $A _ { i }$ is one of the pre-activities of $A _ { j } )$ , denoted by $A _ { i } { \prec } A _ { j } , { \mathrm { i f } } A _ { i } { \cdot } T i m e _ { e } { \le } A _ { j } { \cdot } T i m e _ { s }$ in all cases of RLog.

De<sup>fi</sup>nition 11. (Direct pre-activities and post-activities) Let RLog be the running log of a work<sup>fl</sup>ow, $\forall A _ { i } , A _ { j } \in A c t i v i t y S e t ( R L o g ) , A _ { j }$ is one of the direct post-activities of $A _ { i }$ (or $A _ { i }$ is one of the direct pre-activities of $A _ { j } ) _ { \ l }$ , denoted by $A _ { i } { \prec } A _ { j } ,$ if $A _ { i } { \preccurlyeq } A _ { j }$ and there is no any activity $A _ { k } \in$ ActivitySet(RLog) such that $A _ { i } { \preccurlyeq } A _ { k }$ and $A _ { k } { \preccurlyeq } A _ { j }$

The set of all the direct pre-activities (post-activities) of $A _ { i }$ is denoted by A ·PreASet (A ·PostASet).

De<sup>fi</sup>nition 12. (Start activity and end activity) Let RLog be the running log of a work<sup>fl</sup>ow,

(1) $S e t _ { s t a r t } ( R L o g ) = \{ A _ { i } | A _ { i } \in A c t i v i t y S e t ( R L o g ) \land A _ { i } \cdot P r e A S e t = \emptyset \}$ is

named as the start activity set of the work<sup>fl</sup>ow.

(2) $S e t _ { e n d } ( R L o g ) = \{ A _ { i } | A _ { i } \in A c t i v i t y S e t ( R L o g ) \land A _ { i } \cdot P o s t A S e t = \emptyset \}$ is named as the end activity set of the work<sup>fl</sup>ow.

For example, in Table 3, Set (RLog)={Application Acceptance}, and Set (RLog)={Delivery Order Generated}, which means the start and end activities of the work<sup>fl</sup>ow in the Consignor organization are Application Acceptance and Delivery Order Generated, respectively. The pre-activities of Application Acceptance are {Delivery Order Generated}, and Contract Generation is a directed post-activity of Application Acceptance i.e., the pre-activities of Contract Generation are {Application Acceptance}.

## 5.2. Process mining for single organization

The quality of the running log is important as it determines the result of the model mined. A running log satisfying the following conditions is referred to as a well-formed log:

(1) Each running case is complete.

(2) There are no XOR structures in WF: i.e., there are no con<sup>fl</sup>ict activities in the work<sup>fl</sup>ow. Thus, the activities in each running case are the same.

We focus on discovering a work<sup>fl</sup>ow model from its well-formed running log. To integrate the process model for the cross-organizational work<sup>fl</sup>ow, we <sup>fi</sup>rst discover the process model for each organization from its own running log stored in its internal database, and then construct the process model for the cross-organizational work<sup>fl</sup>ow according to the coordination patterns published. In this subsection, the mining algorithm used to discover the RM\_WF\_Net from the running log is <sup>fi</sup>rst introduced. The main algorithm contains two components presented in Algorithms 1 and 2, respectively. Algorithm 1 is used to calculate the duration of each activity and the structural and temporal relations between activities. Algorithm 2 is used to construct the RM\_WF\_Net that takes the results of Algorithm 1 as inputs.

First, a function, PostASet(A ,RCase), is de<sup>fi</sup>ned to calculate the direct post-activities of activity $A _ { i }$ in running case RCase.

Function 1. To calculate $A _ { i } .$ ·PostASet of activity $A _ { i }$ in the running case RCase

PostASet(A ,RCase)

Begin:

Step 1: For $k = 1$ to |RCase| do

(1.1) A<sub>k</sub>·PostASet←∅;

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
(1.2) For j=1 to |RCase| do
If  $A_{k}\cdot t_{e}\leq A_{j}\cdot t_{s}$ , then  $A_{k}\cdot PostASet\leftarrow A_{k}\cdot PostASet\cup\{A_{j}\}$ .
EndFor;
EndFor;
Step 2: For each  $A_{j}\in A_{i}\cdot PostASet$  do
For each  $A_{k}\in A_{j}\cdot PostASet$  do
 $A_{i}\cdot PostASet\leftarrow A_{i}\cdot PostASet-\{A_{k}\}$ 
EndFor;
EndFor;
Step 3: Return  $A_{i}\cdot PostASet$ .
End.
</div>

The complexity of the <sup>fi</sup>rst step in Function 1 is $\mathcal { O } ( | R C a s e | ^ { 2 } )$ . Because |A ·PostASet|≤|RCase| and $| A _ { j } \cdot P o s t A S e t | \leq | R C a s e |$ , the complexity of the second step is also $\mathcal { O } \big ( | R C a s e | ^ { 2 } \big )$ . Thus, the complexity of Function 1 is $\mathcal { O } \big ( | R C a s e | ^ { 2 } \big )$

From each running log, information on the resources required and released and the messages exchanged is obtained directly. Now, we present the <sup>fi</sup>rst algorithm to compute the relations between activities from the running log.

Algorithm 1. To calculate $A _ { i }$ ·PreASet and $A _ { i }$ ·PostASet for each activity in the running log

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
INPUT: RLog — the set of running log of a workflow
OUTPUT:  $(A_{i}, A_{i} \cdot ResourceReq, A_{i} \cdot ResourceRel, A_{i} \cdot MessageRec, A_{i} \cdot MessageSent, A_{i} \cdot PreASet, A_{i} \cdot PostASet)$  (1 ≤ i ≤ |RCase|, RCase ∈ RLog)
Step 1: For i = 1 to |RCase| do  $A_{i} \cdot PreASet \leftarrow \varnothing$ , and  $A_{i} \cdot PostASet \leftarrow \varnothing$ ;
Step 2: For i = 1 to |RCase| do
 $A_{i} \cdot PostASet \leftarrow A_{i} \cdot PostASet \cup \bigcap_{1 \leq j \leq |RLog|} PostASet(A_{i}, RCase_{j})$ ;
EndFor;
Step 3: For i = 1 to |RCase| do
(3.1) For j = 1 to |RCase| do
 $A_{i} \cdot PreASet \leftarrow A_{i} \cdot PreASet \cup \{A_{j} | A_{i} \in A_{j} \cdot PostASet\}$ ;
EndFor;
(3.2) Output  $(A_{i}, A_{i} \cdot ResourceReq, A_{i} \cdot ResourceRel, A_{i} \cdot MessageRec, A_{i} \cdot MessageSent, A_{i} \cdot PreASet, A_{i} \cdot PostASet)$ .
EndFor.
</div>

In the second step of Algorithm 1, it has been proved that the complexity of the Function PostASet is $\mathcal { O } \big ( | R C a s e | ^ { 2 } \big )$ . The complexity to com-<sup>O</sup>plete the union or the intersection operation of two sets is RCase <sup>Oð Þj j</sup>because the number of each set is at most |RCase|. The complexity of the second step is $\mathcal { O } \big ( | R L o g | * \big ( | R C a s e | ^ { 2 } + | R C a s e | \big ) \big )$ , i.e., RLog <sup>O j j  þ</sup>RCase <sup>2</sup> . The complexity of the third step is $\mathcal { O } \big ( | R C a s e | ^ { 2 } \big )$ <sup>Oðj j</sup>. Therefore, <sup>j</sup>the complexity of Algorithm 1 is $\mathcal { O } ( | R L O g | * | R C a s e | ^ { 2 } )$

<sup>Oðj jj</sup>Taking the running log shown in Table 3 as input to Algorithm 1, Table 4 shows the resource and message information, pre-activities, and post-activities of each activity.

## Algorithm 2. To discover RM\_WF\_Net from the running log

INPUT: $( A _ { i } , A _ { i }$ ·ResourceReq, A ·ResourceRel, A ·MessageRec, $A _ { i } .$ MessageSent, $A _ { i }$ ·PreASet, $A _ { i } .$ ·PostASet) (1≤i≤|RCase|, $R C a s e \in R L o g )$ OUTPUT: RM\_WF\_Net model $\Sigma = ( P , T ; F , M _ { 0 } )$ Step $1 \colon P _ { L } \gets \emptyset , P _ { R } \gets \emptyset , P _ { M } \gets \emptyset , T \gets T \cup \{ A _ { i } | 1$ ≤ i ≤ |RCase|}, $F \gets \emptyset$ $M _ { 0 } \gets \emptyset , S e t _ { s t a r t } \gets \emptyset$ , and $S e t _ { e n d } \gets \emptyset$ Step 2: For each activity $A _ { i } \in T$ (2.1) $P _ { L } \{ - P _ { L } \cup \{ p _ { i 1 } \} \cup \{ p _ { i 2 } \} $ , and $F {  } F \cup \{ ( p _ { i 1 } , A _ { i } ) , ( A _ { i } , p _ { i 2 } ) \} ;$ (2.2) $P _ { R } {  } P _ { R } { \cup } A _ { i }$ ·ResourceReq∪A ·ResourceRel, and $F {  } F \cup \{ ( p { \mathrm { , } } A _ { i } ) |$ $p { \in } A _ { i }$ ·ResourceReq} $\mathcal { S } \{ ( A _ { i } , p ) | p \in A _ { i }$ ·ResourceRel}; (2.3) P ←P ∪A ·MessageRec∪A ·MessageSent, and $F {  } F \cup \{ ( p$ $A _ { i } ) | p \in A _ { i }$ ·MessageRec} $\cup \{ ( A _ { i } , p ) | p \in A _ { i }$ ·MessageSent}; EndFor;

Table 4  
Information on each activity mined from the running log.

<table><tr><td>Activity</td><td>ResourceReq</td><td>ResourceRel</td><td>MessageRec</td><td>MessageSent</td><td>PreASet</td><td>PostASet</td></tr><tr><td> $A_1$ </td><td>∅</td><td>∅</td><td> $\{p_{m1}\}$ </td><td>∅</td><td>∅</td><td> $\{A_2\}$ </td></tr><tr><td> $A_2$ </td><td>∅</td><td>∅</td><td>∅</td><td>∅</td><td> $\{A_1\}$ </td><td> $\{A_3\}$ </td></tr><tr><td> $A_3$ </td><td> $\{p_{r1}\}$ </td><td> $\{p_{r1}\}$ </td><td>∅</td><td>∅</td><td> $\{A_2\}$ </td><td> $\{A_4\}$ </td></tr><tr><td> $A_4$ </td><td>∅</td><td>∅</td><td>∅</td><td> $\{p_{m2},p_{m3}\}$ </td><td> $\{A_3\}$ </td><td> $\{A_5\}$ </td></tr><tr><td> $A_5$ </td><td>∅</td><td>∅</td><td> $\{p_{m4},p_{m5}\}$ </td><td> $\{p_{m6}\}$ </td><td> $\{A_4\}$ </td><td> $\{A_6\}$ </td></tr><tr><td> $A_6$ </td><td>∅</td><td>∅</td><td>∅</td><td>∅</td><td> $\{A_5\}$ </td><td> $\{A_7\}$ </td></tr><tr><td> $A_7$ </td><td>∅</td><td>∅</td><td>∅</td><td>∅</td><td> $\{A_6\}$ </td><td> $\{A_8\}$ </td></tr><tr><td> $A_8$ </td><td>∅</td><td>∅</td><td>∅</td><td>∅</td><td> $\{A_7\}$ </td><td> $\{A_9\}$ </td></tr><tr><td> $A_9$ </td><td>∅</td><td>∅</td><td>∅</td><td>∅</td><td> $\{A_8\}$ </td><td> $\{A_{10}\}$ </td></tr><tr><td> $A_{10}$ </td><td>∅</td><td>∅</td><td>∅</td><td>∅</td><td> $\{A_9\}$ </td><td> $\{A_{11}\}$ </td></tr><tr><td> $A_{11}$ </td><td>∅</td><td>∅</td><td>∅</td><td>∅</td><td> $\{A_{10}\}$ </td><td> $\{A_{12}\}$ </td></tr><tr><td> $A_{12}$ </td><td>∅</td><td>∅</td><td>∅</td><td>∅</td><td> $\{A_{11}\}$ </td><td> $\{A_{13}\}$ </td></tr><tr><td> $A_{13}$ </td><td>∅</td><td>∅</td><td> $\{p_{m7}\}$ </td><td> $\{p_{m8}\}$ </td><td> $\{A_{12}\}$ </td><td> $\{A_{14}\}$ </td></tr><tr><td> $A_{14}$ </td><td>∅</td><td>∅</td><td> $\{p_{m9}\}$ </td><td> $\{p_{m10},p_{m11}\}$ </td><td> $\{A_{13}\}$ </td><td> $\{A_{15}\}$ </td></tr><tr><td> $A_{15}$ </td><td>∅</td><td>∅</td><td> $\{p_{m12}\}$ </td><td> $\{p_{m13}\}$ </td><td> $\{A_{14}\}$ </td><td>∅</td></tr></table>

Step 3: For any two A ,A ∈T (1≤i,j≤|T|), if $A _ { j } \in A _ { i }$ ·PostASet,

$$
P _ {L} \leftarrow ((P _ {L} - \{p _ {i 2}, p _ {j 1} \}) \cup \{p _ {i j} \},
$$

$$
F \leftarrow ((F - \{(A _ {i}, p _ {i 2}), (p _ {j 1}, A _ {j}) \}) \cup \{(A _ {i}, p _ {i j}), (p _ {i j}, A _ {j}) \});
$$

Step 4: $P _ { L }  P _ { L } \cup \{ p _ { s } , p _ { e } \} ; \ T  T \cup \{ t _ { s } , t _ { e } \} ; \ F  F \cup \{ ( p _ { s } , t _ { s } ) , ( p _ { e } , t _ { e } ) \} \cup \{ ( t _ { s } , t _ { e } ) \}$ $p ) | p { \in } P _ { L } - \{ p _ { s } , p _ { e } \} \wedge ^ { \bullet } p = { \emptyset } \} { \cup } \{ ( p , t _ { e } ) | p { \in } P _ { L } - \{ p _ { s } , p _ { e } \} \wedge p ^ { \bullet } = { \emptyset } \} ,$ Step 5: For each place $p { \in } P ,$ if $p = p _ { s }$ or $p { \in } P _ { R } , M _ { 0 } ( p ) \gets 1$ , otherwise $M _ { 0 } ( p ) \gets 0 ,$ , where $P { = } P _ { L } { \cup } P _ { R } { \cup } P _ { M } { . }$ Step 6: Output $\Sigma = ( P , T ; F , M _ { 0 } )$

In the second step of Algorithm 2, the complexity to complete $P _ { R } \cup A _ { i }$ ·ResourceReq $\cup A _ { i }$ ·ResourceRel is $\mathcal { D } \big ( | P _ { R } | ^ { 2 } \big )$ . Similarly, the complexity of $P _ { M } \cup A _ { i }$ <sup>O</sup>·MessageRec∪A ·MessageSent is $\mathcal { O } \big ( | P _ { M } | ^ { 2 } \big )$ . The complexity of the second step is RCase $* \left( | \bar { P _ { R } } | ^ { 2 } { + } | P _ { M } | ^ { 2 } \right) )$ . The complexity of the <sup>O j j</sup>third, fourth, and <sup>fi</sup>fth step is  $| R \ddot { C } a s \dot { e } | ^ { 2 } ) , \stackrel { \cdot } { \mathcal { O } } ( | P _ { L } | )$ and $\mathcal { O } ( | P | )$ , respectively. Therefore, the complexity of Algorithm $2 \mathrm { ~ i ~ } s \mathcal { O } ( | R C a s e | ^ { 2 } + | R C a s e | *$ $( | P _ { R } | ^ { 2 } { + } | P _ { M } | ^ { 2 } ) { + } | P | )$ .

<sup>þ þj</sup>Taking the output of Algorithm 1 in Table 4 as the input to Algorithm 2, the model discovered is an RM\_WF\_Net, which is shown in Fig. 3.

5.2.1. Example 2. Mining the workflow models for the Buyer organization, Sender organization, Shipper organization and Carrier organization process

In the multi-modal transportation business process, there are <sup>fi</sup>ve organizations involved in the work<sup>fl</sup>ow: the Buyer organization, Sender organization, Consignor organization, Shipper organization, and Carrier organization. The work<sup>fl</sup>ow model for the Consignor organization shown in Fig. 3, has been obtained by using process mining technology. Next, the mining algorithm is applied to discover the work<sup>fl</sup>ow models for the other four organizations. Table 5 presents the work<sup>fl</sup>ow running log in one case of the other four organizations collected from the database within their own organizations. Table 6 shows the meanings of the symbols for the transitions and places in Table 5.

Taking the running log of the Sender organization process, the format of which is similar to that shown in Table $5 ,$ as input to Algorithm 1, the mined results on the resource and message information, pre-activities, and post-activities of each activity in the work<sup>fl</sup>ow of the Sender organization are shown in Table 7. Taking the data in Table 7 as input to Algorithm 2, the RM\_WF\_Net model for the work<sup>fl</sup>ow of the Sender organization can be discovered, as shown in Fig. 6.

Similarly, taking the running log with a format similar to that shown in Table 5 as input, the mined results on the resource and message information, pre-activities, and post-activities of each activity in the work<sup>fl</sup>ow of the Buyer organization, Carrier organization, and Shipper organization are shown in Table 7. The models mined for the Buyer work<sup>fl</sup>ow, Carrier work<sup>fl</sup>ow, and Shipper work<sup>fl</sup>ows are shown in Figs. 7, 8, and 9, respectively.

Table 5  
Part of the running log of the multi-modal transportation business process in one case.

<table><tr><td>Organization</td><td>Activity</td><td>Start time</td><td>End time</td><td>ResourceReq</td><td>ResourceRel</td><td>MessageRec</td><td>MessageSent</td></tr><tr><td rowspan="4">Buyer</td><td> $A_{16}$ </td><td>08:00 Aug 01</td><td>08:23 Aug 01</td><td>∅</td><td>∅</td><td>∅</td><td> $\{p_{m14}\}$ </td></tr><tr><td> $A_{17}$ </td><td>10:30 Aug 01</td><td>10:45 Aug 01</td><td> $\{p_{r3}\}$ </td><td> $\{p_{r3}\}$ </td><td>∅</td><td>∅</td></tr><tr><td> $A_{18}$ </td><td>10:46 Aug 01</td><td>10:50 Aug 01</td><td>∅</td><td>∅</td><td> $\{p_{m15}\}$ </td><td> $\{p_{m16}\}$ </td></tr><tr><td> $A_{19}$ </td><td>10:38 Aug 06</td><td>11:20 Aug 06</td><td>∅</td><td>∅</td><td> $\{p_{m13},p_{m17}\}$ </td><td>∅</td></tr><tr><td rowspan="10">Sender</td><td> $A_{20}$ </td><td>08:24 Aug 01</td><td>08:30 Aug 01</td><td>∅</td><td>∅</td><td> $\{p_{m14}\}$ </td><td>∅</td></tr><tr><td> $A_{21}$ </td><td>08:31 Aug 01</td><td>09:10 Aug 01</td><td>∅</td><td>∅</td><td>∅</td><td> $\{p_{m15}\}$ </td></tr><tr><td> $A_{17}$ </td><td>10:30 Aug 01</td><td>10:45 Aug 01</td><td> $\{p_{r2}\}$ </td><td> $\{p_{r2}\}$ </td><td>∅</td><td>∅</td></tr><tr><td> $A_{22}$ </td><td>10:51 Aug 01</td><td>10:59 Aug 01</td><td>∅</td><td>∅</td><td> $\{p_{m16}\}$ </td><td> $\{p_{m1}\}$ </td></tr><tr><td> $A_{3}$ </td><td>11:30 Aug 01</td><td>11:45 Aug 01</td><td> $\{p_{r2}\}$ </td><td> $\{p_{r2}\}$ </td><td>∅</td><td>∅</td></tr><tr><td> $A_{23}$ </td><td>12:05 Aug 01</td><td>14:23 Aug 01</td><td>∅</td><td>∅</td><td> $\{p_{m6}\}$ </td><td>∅</td></tr><tr><td> $A_{6}$ </td><td>14:24 Aug 01</td><td>14:41 Aug 01</td><td>∅</td><td>∅</td><td>∅</td><td>∅</td></tr><tr><td> $A_{7}$ </td><td>14:42 Aug 01</td><td>14:58 Aug 01</td><td>∅</td><td>∅</td><td>∅</td><td>∅</td></tr><tr><td> $A_{8-9-10}$ </td><td>14:59 Aug 01</td><td>15:32 Aug 01</td><td>∅</td><td>∅</td><td>∅</td><td>∅</td></tr><tr><td> $A_{24}$ </td><td>09:01 Aug 04</td><td>09:15 Aug 04</td><td>∅</td><td>∅</td><td> $\{p_{m10}\}$ </td><td> $\{p_{m12}\}$ </td></tr><tr><td rowspan="7">Shipper</td><td> $A_{28}$ </td><td>11:51 Aug 01</td><td>11:54 Aug 01</td><td>∅</td><td>∅</td><td> $\{p_{m3}\}$ </td><td> $\{p_{m5}\}$ </td></tr><tr><td> $A_{29}$ </td><td>13:40 Aug 03</td><td>14:03 Aug 03</td><td>∅</td><td>∅</td><td>∅</td><td>∅</td></tr><tr><td> $A_{30}$ </td><td>23:10 Aug 03</td><td>23:30 Aug 03</td><td>∅</td><td>∅</td><td>∅</td><td>∅</td></tr><tr><td> $A_{31}$ </td><td>08:03 Aug 04</td><td>08:46 Aug 04</td><td>∅</td><td>∅</td><td>∅</td><td>∅</td></tr><tr><td> $A_{32}$ </td><td>08:47 Aug 04</td><td>08:54 Aug 04</td><td>∅</td><td>∅</td><td>∅</td><td> $\{p_{m9}\}$ </td></tr><tr><td> $A_{33}$ </td><td>09:01 Aug 04</td><td>10:33 Aug 06</td><td>∅</td><td>∅</td><td> $\{p_{m11}\}$ </td><td>∅</td></tr><tr><td> $A_{34}$ </td><td>10:34 Aug 06</td><td>10:37 Aug 06</td><td>∅</td><td>∅</td><td>∅</td><td> $\{p_{m17}\}$ </td></tr><tr><td rowspan="5">Carrier</td><td> $A_{25}$ </td><td>11:51 Aug 01</td><td>11:55 Aug 01</td><td>∅</td><td>∅</td><td> $\{p_{m2}\}$ </td><td> $\{p_{m4}\}$ </td></tr><tr><td> $A_{12}$ </td><td>08:35 Aug 01</td><td>10:41 Aug 01</td><td>∅</td><td>∅</td><td>∅</td><td>∅</td></tr><tr><td> $A_{26}$ </td><td>16:29 Aug 01</td><td>16:38 Aug 01</td><td>∅</td><td>∅</td><td>∅</td><td> $\{p_{m7}\}$ </td></tr><tr><td> $A_{27}$ </td><td>16:45 Aug 01</td><td>08:02 Aug 04</td><td>∅</td><td>∅</td><td> $\{p_{m8}\}$ </td><td>∅</td></tr><tr><td> $A_{31}$ </td><td>08:03 Aug 04</td><td>08:46 Aug 04</td><td>∅</td><td>∅</td><td>∅</td><td>∅</td></tr></table>

Although the models shown in Figs. 3, 6, 7, 8, and 9 can partly represent the contents of the business process within the Consignor, Sender, Buyer, Carrier and Shipper organizations respectively, they do not know the coordination patterns of other organizations. For example, in the model of the Shipper organization shown in Fig. 9, p<sub>m3</sub>, p<sub>m5</sub>, p<sub>m9</sub>, p<sub>m11</sub>, and $p _ { m 1 7 }$ represent the messages it exchanges with other organizations. However, the speci<sup>fi</sup>c organizations the messages are sent to and received from are unknown. Such information is contained in the coordination patterns. In the following subsection, the mining algorithm for the coordination patterns is presented.

Meanings of transitions and places in Table 5.  
Table 6

<table><tr><td>Transition</td><td>Meaning</td><td>Place</td><td>Meaning</td></tr><tr><td> $A_{3}$ </td><td>Contract  $Signed_{2}$ </td><td> $p_{m1}$ </td><td>Application Form</td></tr><tr><td> $A_{6}$ </td><td>Goods Arrival</td><td> $p_{m2}$ </td><td>Request  $Form_{1}$ </td></tr><tr><td> $A_{7}$ </td><td>Container Packing</td><td> $p_{m3}$ </td><td>Request  $Form_{2}$ </td></tr><tr><td> $A_{8-9-10}$ </td><td>Customs Declaration</td><td> $p_{m4}$ </td><td> $Acceptance\ Notice_{1}$ </td></tr><tr><td> $A_{12}$ </td><td>Loading</td><td> $p_{m5}$ </td><td> $Acceptance\ Notice_{2}$ </td></tr><tr><td> $A_{16}$ </td><td>Goods Booking</td><td> $p_{m6}$ </td><td>Packing Notice</td></tr><tr><td> $A_{17}$ </td><td>Contract  $Signed_{1}$ </td><td> $p_{m7}$ </td><td>Waybill Issued</td></tr><tr><td> $A_{18}$ </td><td> $Payment_{1}$ </td><td> $p_{m8}$ </td><td>Payment  $Verification_{2}$ </td></tr><tr><td> $A_{19}$ </td><td>Goods Release</td><td> $p_{m9}$ </td><td>Terminal Receipt</td></tr><tr><td> $A_{20}$ </td><td>Cost Calculation</td><td> $p_{m10}$ </td><td>Payment Receipt</td></tr><tr><td> $A_{21}$ </td><td>Contract Generated</td><td> $p_{m11}$ </td><td> $Payment\ Verification_{3}$ </td></tr><tr><td> $A_{22}$ </td><td>Shipping Application</td><td> $p_{m12}$ </td><td> $Payment\ Verification_{4}$ </td></tr><tr><td> $A_{23}$ </td><td>Goods Preparation</td><td> $p_{m13}$ </td><td>Release Form</td></tr><tr><td> $A_{24}$ </td><td>Payment</td><td> $p_{m14}$ </td><td>Booking Order</td></tr><tr><td> $A_{25}$ </td><td>Booking  $Accepted_{1}$ </td><td> $p_{m15}$ </td><td>Cost Bill</td></tr><tr><td> $A_{26}$ </td><td>Generating Issue Waybill</td><td> $p_{m16}$ </td><td> $Payment\ Verification_{1}$ </td></tr><tr><td> $A_{27}$ </td><td>Container Delivery</td><td> $p_{m17}$ </td><td>Arrival Notice</td></tr><tr><td> $A_{28}$ </td><td>Booking  $Accepted_{2}$ </td><td>-</td><td>-</td></tr><tr><td> $A_{29}$ </td><td>Shipper Inventory</td><td> $p_{r2}$ </td><td>Sender Manager</td></tr><tr><td> $A_{30}$ </td><td>Cargoboat Entrance</td><td> $p_{r3}$ </td><td>Buyer Manager</td></tr><tr><td> $A_{31}$ </td><td>Transit</td><td></td><td></td></tr><tr><td> $A_{32}$ </td><td>General Terminal Receipt</td><td></td><td></td></tr><tr><td> $A_{33}$ </td><td>Delivery</td><td></td><td></td></tr><tr><td> $A_{34}$ </td><td>Goods  $Arrival_{2}$ </td><td></td><td></td></tr></table>

## 6. Process mining for cross-organizational work<sup>fl</sup>ow integration

This section presents the approach to the cross-organizational work<sup>fl</sup>ow integration by using process mining technology. The framework is proposed <sup>fi</sup>rst for process integration based on process mining. After the formal de<sup>fi</sup>nition for the running log is given, the mining algorithm for the work<sup>fl</sup>ow within an organization is proposed. Finally, the integration for the cross-organizational work<sup>fl</sup>ow is obtained.

## 6.1. Coordination patterns mining from integrated running log

In order to discover the coordination pattern between two organizations, a middleware has been implemented to integrate the work<sup>fl</sup>ow running logs between different organizations. To protect the database, the middleware can only access the historical databases after being authorized by the different organizations. It extracts the coordinated running records from the historical database of each organization, which are used to mine the coordination patterns. The running records are extracted from the database if one of the following conditions is satis<sup>fi</sup>ed,

(1) $A _ { i } { \cdot } T i m e _ { s } { = } A _ { j } { \cdot } T i m e _ { s }$ and $A _ { i } { \cdot } T i m e _ { e } { = } A _ { j }$ ·Time<sub>e</sub>;

(2) A<sub>i</sub>·ResourceReq∩A<sub>j</sub>·ResourceReq $\neq \emptyset ;$ or $A _ { i } \cdot$ ·ResourceRel∩A<sub>j</sub>· $R e s o u r c e R e l \neq \emptyset ;$

(3) A ·MessageSent $\neg A _ { j }$ ·MessageRec $\neq \emptyset ;$

(4) $A _ { i } \cdot T i m e _ { s } = A _ { j 1 } \cdot T i m e _ { s } , A _ { i } \cdot T i m e _ { e } = A _ { j k } \cdot T i m e _ { e } , A _ { i }$ ResourceReq $\bigcup _ { 1 \leq l \leq k } A _ { j i }$ <sup>¼ -</sup>ResourceReq; ${ } , A _ { i }$ <sup>- ¼</sup>ResourceRel $\mathbf { \Sigma } = \bigcup _ { 1 \leq l \leq k } A _ { j i }$ <sup>-</sup> ResourceRel; $A _ { i } \cdot M e s s a g e S e n t = \bigcup _ { 1 \leq l \leq k } A _ { j i }$ MessageSent; andA $M e s s a g e R e c = \bigcup _ { 1 \leq l \leq k } A _ { j i } \cdot M e s s a g e R e c ;$

where $A _ { i }$ and $A _ { j } \left( A _ { j 1 } \cdots A _ { j k } \right)$ represents different activities in the running records from two different organizations.

Part of the data integration of the running logs between the Consignor and the Sender work<sup>fl</sup>ows is shown in Table 8 as an example.

The work<sup>fl</sup>ow running log integrated from two organizations is used to mine the coordination patterns between these two organizations. The mining algorithm for the coordination patterns is shown in

Table 7  
Activity information mined from the running log in Table 5.

<table><tr><td>Organization</td><td>Activity</td><td>ResourceReq</td><td>ResourceRel</td><td>MessageRec</td><td>MessageSent</td><td>PreASet</td><td>PostASet</td></tr><tr><td rowspan="4">Buyer</td><td> $A_{16}$ </td><td>∅</td><td>∅</td><td>∅</td><td> $\{p_{m14}\}$ </td><td>∅</td><td> $\{A_{17}\}$ </td></tr><tr><td> $A_{17}$ </td><td> $\{p_{r2}\}$ </td><td> $\{p_{r2}\}$ </td><td>∅</td><td>∅</td><td> $\{A_{16}\}$ </td><td> $\{A_{18}\}$ </td></tr><tr><td> $A_{18}$ </td><td>∅</td><td>∅</td><td> $\{p_{m15}\}$ </td><td> $\{p_{m16}\}$ </td><td> $\{A_{17}\}$ </td><td> $\{A_{19}\}$ </td></tr><tr><td> $A_{19}$ </td><td>∅</td><td>∅</td><td> $\{p_{m13},p_{m17}\}$ </td><td>∅</td><td> $\{A_{18}\}$ </td><td>∅</td></tr><tr><td rowspan="10">Sender</td><td> $A_{20}$ </td><td>∅</td><td>∅</td><td> $\{p_{m14}\}$ </td><td>∅</td><td>∅</td><td> $\{A_{21}\}$ </td></tr><tr><td> $A_{21}$ </td><td>∅</td><td>∅</td><td>∅</td><td> $\{p_{m15}\}$ </td><td> $\{A_{20}\}$ </td><td> $\{A_{17}\}$ </td></tr><tr><td> $A_{17}$ </td><td> $\{p_{r2}\}$ </td><td> $\{p_{r2}\}$ </td><td>∅</td><td>∅</td><td> $\{A_{21}\}$ </td><td> $\{A_{22}\}$ </td></tr><tr><td> $A_{22}$ </td><td>∅</td><td>∅</td><td> $\{p_{m16}\}$ </td><td> $\{p_{m1}\}$ </td><td> $\{A_{17}\}$ </td><td> $\{A_{3}\}$ </td></tr><tr><td> $A_{3}$ </td><td> $\{p_{r2}\}$ </td><td> $\{p_{r2}\}$ </td><td>∅</td><td>∅</td><td> $\{A_{22}\}$ </td><td> $\{A_{23}\}$ </td></tr><tr><td> $A_{23}$ </td><td>∅</td><td>∅</td><td> $\{p_{m6}\}$ </td><td>∅</td><td> $\{A_{3}\}$ </td><td> $\{A_{6}\}$ </td></tr><tr><td> $A_{6}$ </td><td>∅</td><td>∅</td><td>∅</td><td>∅</td><td> $\{A_{23}\}$ </td><td> $\{A_{7}\}$ </td></tr><tr><td> $A_{7}$ </td><td>∅</td><td>∅</td><td>∅</td><td>∅</td><td> $\{A_{6}\}$ </td><td> $\{A_{8-9-10}\}$ </td></tr><tr><td> $A_{8-9-10}$ </td><td>∅</td><td>∅</td><td>∅</td><td>∅</td><td> $\{A_{7}\}$ </td><td> $\{A_{24}\}$ </td></tr><tr><td> $A_{24}$ </td><td>∅</td><td>∅</td><td> $\{p_{m10}\}$ </td><td> $\{p_{m12}\}$ </td><td> $\{A_{8-9-10}\}$ </td><td>∅</td></tr><tr><td rowspan="7">Shipper</td><td> $A_{28}$ </td><td>∅</td><td>∅</td><td> $\{p_{m3}\}$ </td><td> $\{p_{m5}\}$ </td><td>∅</td><td> $\{A_{29}\}$ </td></tr><tr><td> $A_{29}$ </td><td>∅</td><td>∅</td><td>∅</td><td>∅</td><td> $\{A_{28}\}$ </td><td> $\{A_{30}\}$ </td></tr><tr><td> $A_{30}$ </td><td>∅</td><td>∅</td><td>∅</td><td>∅</td><td> $\{A_{29}\}$ </td><td> $\{A_{31}\}$ </td></tr><tr><td> $A_{31}$ </td><td>∅</td><td>∅</td><td>∅</td><td>∅</td><td> $\{A_{30}\}$ </td><td> $\{A_{32}\}$ </td></tr><tr><td> $A_{32}$ </td><td>∅</td><td>∅</td><td>∅</td><td> $\{p_{m9}\}$ </td><td> $\{A_{31}\}$ </td><td> $\{A_{33}\}$ </td></tr><tr><td> $A_{33}$ </td><td>∅</td><td>∅</td><td> $\{p_{m11}\}$ </td><td>∅</td><td> $\{A_{32}\}$ </td><td> $\{A_{34}\}$ </td></tr><tr><td> $A_{34}$ </td><td>∅</td><td>∅</td><td>∅</td><td> $\{p_{m17}\}$ </td><td> $\{A_{33}\}$ </td><td>∅</td></tr><tr><td rowspan="5">Carrier</td><td> $A_{25}$ </td><td>∅</td><td>∅</td><td> $\{p_{m2}\}$ </td><td> $\{p_{m4}\}$ </td><td>∅</td><td> $\{A_{12}\}$ </td></tr><tr><td> $A_{12}$ </td><td>∅</td><td>∅</td><td>∅</td><td>∅</td><td> $\{A_{25}\}$ </td><td> $\{A_{26}\}$ </td></tr><tr><td> $A_{26}$ </td><td>∅</td><td>∅</td><td>∅</td><td> $\{p_{m7}\}$ </td><td> $\{A_{12}\}$ </td><td> $\{A_{27}\}$ </td></tr><tr><td> $A_{27}$ </td><td>∅</td><td>∅</td><td> $\{p_{m8}\}$ </td><td>∅</td><td> $\{A_{26}\}$ </td><td> $\{A_{31}\}$ </td></tr><tr><td> $A_{31}$ </td><td>∅</td><td>∅</td><td>∅</td><td>∅</td><td> $\{A_{27}\}$ </td><td>∅</td></tr></table>

![](/api/attachments/ZHKPJRVS/fulltext/images/6d9ac635d863b155ec5e97b7bc58758b28ec5fa52c5b7630a24863e634f7b508.jpg)  
Fig. 6. The RM\_WF\_Net of the Sender process.

![](/api/attachments/ZHKPJRVS/fulltext/images/ca045e62036a76a9c7b9daf0b3341addeca20dccbef20d109d1cdc2b63cd6e5b.jpg)  
Fig. 8. The RM\_WF\_Net of the Carrier process.  
Fig. 7. The RM\_WF\_Net of the Buyer process.

Algorithm 3. Before presenting the mining algorithm, a core function used in the mining algorithm is <sup>fi</sup>rst given.

Function 2. To extend a transition $t _ { i }$ in a RM \_WF \_Net Σ=(P,T;F,M ), where $P { = } P _ { L } { \cup } P _ { R } { \cup } P _ { M } { . }$

Step 2: $P _ { R } {  } P _ { R } \cup t _ { i }$ ·ResourceReq∪t ·ResourceRel, and $F {  } F \cup \{ ( p , t _ { i } ) |$ p∈t ·ResourceReq}∪{(t ,p)|p∈t ·ResourceRel};

Step 3: $P _ { M } \{ - P _ { M } \cup t _ { i } .$ MessageRec∪t ·MessageSent, and $F {  } F \cup \{ ( p ,$ t )|p ∈ t ·MessageRec}∪{(t ,p)|p ∈ t ·MessageSent};

![](/api/attachments/ZHKPJRVS/fulltext/images/f411af3d5b360076a592197c3d53983998b34bb0e1b9ce875dd3285e0256e723.jpg)

$$
P _ {R}, M _ {0} (p) \leftarrow 1;
$$

Step 5: Return $\Sigma = ( P , T ; F , M _ { 0 } )$

![](/api/attachments/ZHKPJRVS/fulltext/images/65d61ff8570973c8daf301c64613f8fe225a98af5bcdcb7d755127b07b2d290e.jpg)  
Fig. 9. The RM\_WF\_Net of the Shipper process.

Table 8  
Part of the data integrated between the running logs of the Consignor and the Sender work<sup>fl</sup>ow.

<table><tr><td>Organization</td><td>Activity</td><td>Start time</td><td>End time</td><td>ResourceReq</td><td>ResourceRel</td><td>MessageRec</td><td>MessageSent</td></tr><tr><td rowspan="7">Sender</td><td> $A_{22}$ </td><td>10:51 Aug 01</td><td>10:59 Aug 01</td><td>∅</td><td>∅</td><td> $\{p_{m16}\}$ </td><td> $\{p_{m1}\}$ </td></tr><tr><td> $A_3$ </td><td>11:30 Aug 01</td><td>11:45 Aug 01</td><td> $\{p_{r2}\}$ </td><td> $\{p_{r2}\}$ </td><td>∅</td><td>∅</td></tr><tr><td> $A_{23}$ </td><td>12:05 Aug 01</td><td>14:23 Aug 01</td><td>∅</td><td>∅</td><td> $\{p_{m6}\}$ </td><td>∅</td></tr><tr><td> $A_6$ </td><td>14:24 Aug 01</td><td>14:41 Aug 01</td><td>∅</td><td>∅</td><td>∅</td><td>∅</td></tr><tr><td> $A_7$ </td><td>14:42 Aug 01</td><td>14:58 Aug 01</td><td>∅</td><td>∅</td><td>∅</td><td>∅</td></tr><tr><td> $A_{8-9-10}$ </td><td>14:59 Aug 01</td><td>15:32 Aug 01</td><td>∅</td><td>∅</td><td>∅</td><td>∅</td></tr><tr><td> $A_{24}$ </td><td>09:01 Aug 04</td><td>09:15 Aug 04</td><td>∅</td><td>∅</td><td> $\{p_{m10}\}$ </td><td> $\{p_{m12}\}$ </td></tr><tr><td rowspan="10">Consignor</td><td> $A_1$ </td><td>11:00 Aug 01</td><td>11:03 Aug 01</td><td>∅</td><td>∅</td><td> $\{p_{m1}\}$ </td><td>∅</td></tr><tr><td> $A_3$ </td><td>11:30 Aug 01</td><td>11:45 Aug 01</td><td> $\{p_{r1}\}$ </td><td> $\{p_{r1}\}$ </td><td>∅</td><td>∅</td></tr><tr><td> $A_5$ </td><td>11:56 Aug 01</td><td>12:04 Aug 01</td><td>∅</td><td>∅</td><td> $\{p_{m4},p_{m5}\}$ </td><td> $\{p_{m6}\}$ </td></tr><tr><td> $A_6$ </td><td>14:24 Aug 01</td><td>14:41 Aug 01</td><td>∅</td><td>∅</td><td>∅</td><td>∅</td></tr><tr><td> $A_7$ </td><td>14:42 Aug 01</td><td>14:58 Aug 01</td><td>∅</td><td>∅</td><td>∅</td><td>∅</td></tr><tr><td> $A_8$ </td><td>14:59 Aug 01</td><td>15:04 Aug 01</td><td>∅</td><td>∅</td><td>∅</td><td>∅</td></tr><tr><td> $A_9$ </td><td>15:05 Aug 01</td><td>15:14 Aug 01</td><td>∅</td><td>∅</td><td>∅</td><td>∅</td></tr><tr><td> $A_{10}$ </td><td>15:15 Aug 01</td><td>15:32 Aug 01</td><td>∅</td><td>∅</td><td>∅</td><td>∅</td></tr><tr><td> $A_{14}$ </td><td>08:55 Aug 04</td><td>09:00 Aug 04</td><td>∅</td><td>∅</td><td> $\{p_{m9}\}$ </td><td> $\{p_{m10},p_{m11}\}$ </td></tr><tr><td> $A_{15}$ </td><td>09:16 Aug 04</td><td>09:20 Aug 04</td><td>∅</td><td>∅</td><td> $\{p_{m12}\}$ </td><td> $\{p_{m13}\}$ </td></tr></table>

In Function 2, the complexity of the second step and the third step is $\mathcal { O } ( | P _ { R } | ^ { 2 } )$ and $\mathcal { O } ( | P _ { M } | ^ { 2 } ) ,$ , respectively. Therefore, the complexity of <sup>O</sup>Function 2 is $\mathcal { O } \big ( | P _ { R } | ^ { 2 } { + } \big | \dot { P _ { M } } \big | ^ { 2 } \big )$

## Algorithm 3. To discover the coordination patterns from the integrated running log

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
INPUT: the integrated running log,  $RLog_{1}$  and  $RLog_{2}$ 

OUTPUT: the coordination patterns  $\Sigma_{1}=(P_{1},T_{1};F_{1},M_{01})$  and  $\Sigma_{2}=(P_{2},T_{2};F_{2},M_{02})$ 

Step 1:  $P_{L1}\leftarrow\varnothing$ ,  $P_{R1}\leftarrow\varnothing$ ,  $P_{M1}\leftarrow\varnothing$ ,  $T_{1}\leftarrow\varnothing$ ,  $F_{1}\leftarrow\varnothing$ ,  $M_{01}\leftarrow\varnothing$ ; and  $P_{L2}\leftarrow\varnothing$ ,  $P_{R2}\leftarrow\varnothing$ ,  $P_{M2}\leftarrow\varnothing$ ,  $T_{2}\leftarrow\varnothing$ ,  $F_{2}\leftarrow\varnothing$ ,  $M_{02}\leftarrow\varnothing$ .

Step 2: For i=1 to  $|RCase_{1}|$  Do

For j=1 to  $|RCase_{2}|$  Do

If  $A_{i}\cdot Time_{s}=A_{j}\cdot Time_{s}$  and  $A_{i}\cdot Time_{e}=A_{j}\cdot Time_{e}$ :

(2.1.1)  $A_{j}\leftarrow A_{i}$ ;

(2.1.2)  $\Sigma_{1}\leftarrow\Sigma_{1}\cup Extension(\Sigma_{1},A_{i})$ , and  $\Sigma_{2}\leftarrow\Sigma_{2}\cup Extension(\Sigma_{2},A_{j})$ ;

Endlf;

If  $A_{i}\cdot ResourceReq\cap A_{j}\cdot ResourceReq\neq\varnothing$ :

(1.1)  $\Sigma_{1}\leftarrow\Sigma_{1}\cup Extension(\Sigma_{1},A_{i})$ , and

(1.2)  $\Sigma_{2}\leftarrow\Sigma_{2}\cup Extension(\Sigma_{2},A_{j})$ ;

Endlf;

If  $A_{i}\cdot MessageSent\cap A_{j}\cdot MessageRec\neq\varnothing$ :

(1.1)  $\Sigma_{1}\leftarrow\Sigma_{1}\cup Extension(\Sigma_{1},A_{i})$ ;

(1.2)  $\Sigma_{2}\leftarrow\Sigma_{2}\cup Extension(\Sigma_{2},A_{j})$ ;

Endlf;

If  $A_{i}\cdot Time_{s}=A_{j}\cdot Time_{s}$  and  $\exists k,j\leq k\leq|RCase_{2}|$  such that:

 $A_{i}\cdot Time_{e}=A_{k}\cdot Time_{e}$ ,

 $A_{j}\cdot ResourceReq=\bigcup_{1\leq l\leq k}A_{l}\cdot ResourceReq$ ,
</div>

$A _ { i } . R e s o u r c e R e l = \bigcup _ { 1 \leq l \leq k } A _ { l } .$ ResourceRel;  
A MessageSent ∪ A MessageSent; and  
$A _ { i } \cdot M e s s a g e R e c = \bigcup _ { 1 \leq l \leq k } ^ { ^ { \cdot } = ^ { \cdot } = ^ { n } } A _ { l }$ MessageRec :  
(1.1) $\Sigma _ { 1 }  \Sigma _ { 1 }$ ∪Extension $\textstyle ( \sum _ { 1 } , A _ { j } ) ;$  
(1.2) For $l = 1$ to k Do

$$
\Sigma_ {2} \leftarrow \Sigma_ {2} \cup \text { Extension } (\Sigma_ {2}, A _ {l});
$$

$$
\begin{array}{l} \text {   Step   3:   Output   } \Sigma_ {1} = (P _ {L 1} \cup P _ {R 1} \cup P _ {M 1}, T _ {1}; F _ {1}, M _ {0 1}) \text {   and   } \Sigma_ {2} = (P _ {L 1} \cup P _ {R 1} \cup \\ P _ {M 1}, T _ {2}; F _ {2}, M _ {0 2}). \end{array}
$$

The complexity of Algorithm 3 is mainly determined by the second step, which is RCase RCase max $\{ | R C a s e _ { 1 } | , | R C a s e _ { 1 } | \} *$ $( | P _ { R } | ^ { 2 } { + } | P _ { M } | ^ { 2 } ) )$ , where $P _ { R } = P _ { R 1 } \cup P _ { R 2 }$ and $P _ { M } = P _ { M 1 } \cup P _ { M 2 } .$ <sup>þ Þ</sup>By using the data shown in Table 8 as the input of Algorithm 3, the coordination pattern mined between the Sender organization and the Consignor organization is shown in Fig. 10.

From Fig. 10, we can see that the coordination patterns between these two organization work<sup>fl</sup>ows are as follows:

(1) The synchronized activities are {Contract Signed , Goods Arrival, Container Packing}, which are represented by transitions $A _ { 3 } , A _ { 6 } ,$ and $A _ { 7 }$ respectively in the models of the Sender and Consignor work<sup>fl</sup>ows.

(2) The messages exchanged between the Sender and Consignor work<sup>fl</sup>ows are {Application Form, Packing Notice, Payment Receipt, PaymentVerification }, which are represented by message places p<sub>m1</sub>, p<sub>m6</sub>, p<sub>m10</sub>, and $p _ { m 1 2 }$ respectively in their work<sup>fl</sup>ow models.

![](/api/attachments/ZHKPJRVS/fulltext/images/dd2a2d9c0ef90a2414f03b21f39fd9924e876255d1242cd13691f1ad564d2ae4.jpg)  
Fig. 10. The coordination pattern mined between Sender organization and the Consignor organization.

(3) The Sender and Consignor are coordinated with one abstract procedure, which is Customs Declaration represented by $A _ { 8 - 9 - 1 0 } .$ . To the Sender organization, the details of the Customs Declaration procedure are unknown. In fact, the Customs Declaration procedure contains three activities, which are {Declaration Form Generation, Declaration Application, Declaration Acceptance}, represented by

$A _ { 8 } , A _ { 9 } \mathrm { a n d } A _ { 1 0 }$ respectively in the model of the Consignor work<sup>fl</sup>ow.

The running logs of other organizations can be also integrated in order to mine their coordination patterns. Part of the data integrated between the running logs of two different organization work<sup>fl</sup>ows is shown in Table 9

By using the data shown in Table 9 as input to Algorithm 3, the coordination patterns mined between two different organizations are presented in Table 10.

The coordination pattern mined between the Carrier organization and the Shipper organization is simple. There is only one synchronized activity for these two organizations, so the coordination pattern mined is not presented here. There is only one message exchanged between the Buyer and the Consignor organization, and between the Buyer and the Shipper organization; thus, the simple coordination pattern mined is also not presented here.

From Table 10, we can see that the coordination patterns between different organizations are as follows:

(1) the coordination pattern mined between the Buyer organization and the Sender organization:

(1.1) The synchronized activity is Contract Signed , which is represented by the transition $A _ { 1 7 }$ in the models of the Buyer and Sender work<sup>fl</sup>ows; and

(1.2) The messages exchanged between the Buyer and Sender work<sup>fl</sup>ows are {Booking Order, Cost Bill, Payment Verification $_ 1 \} ,$ , which are represented by the message places $p _ { m 1 4 } , p _ { m 1 5 } ,$ and $p _ { m 1 6 }$ respectively in their individual work<sup>fl</sup>ow models.

(2) the coordination pattern mined between the Consignor organization and the Shipper organization includes four messages exchanged between them, which are {Request Form , Acceptance Notic $^ { 2 } 2 ,$ Terminal Receipt, Payment Verificatio $\boldsymbol { \imath } _ { 3 } \}$ , represented by the message places p , p , p , and $p _ { m 1 1 }$ respectively in their work<sup>fl</sup>ow models.

(3) the coordination pattern mined between the Consignor organization and the Carrier organization:

(3.1) The synchronized activity is Loading, which is represented by the transition $A _ { 1 2 }$ in the models of the Consignor and Carrier work<sup>fl</sup>ows; and

(3.2) The messages exchanged between the Consignor and Carrier work<sup>fl</sup>ows are {Request Form , Acceptance Notice , Waybill Issued, Payment Veri<sup>fi</sup>cation }, which are represented by the message places $p _ { m 2 } ,$ p<sub>m4</sub>, $p _ { m 7 }$ , and $p _ { m 8 }$ respectively in their work<sup>fl</sup>ow models.

To sum up, Table 11 presents the coordination patterns mined among <sup>fi</sup>ve organizations.

## 6.2. Cross-organizational workflow integration

According to the RM\_WF\_Net model for each organization mined from its own running log and the coordination patterns mined from the integrated running log, the union of the model and the coordination patterns is the integrated model for the cross-organization work<sup>fl</sup>ow. The integration algorithm is presented in Algorithm 4.

Assume that there are n models to be integrated and the model obtained is $\Sigma = ( P , T ; F , M _ { 0 } )$

Let

(1) $\Sigma _ { i } { = } \left( P _ { i } , T _ { i } ; F _ { i } , M _ { 0 i } \right) \left( 1 { \leq } i { \leq } n \right)$ be the work<sup>fl</sup>ow model for one organization, where $P _ { i } { = } P _ { L i } { \cup } P _ { R i } { \cup } P _ { M i }$

(2) $\Sigma _ { i } { = } \left( P _ { i } { , } T _ { i } { ; } F _ { i } { , } M _ { 0 i } \right)$ and $\begin{array} { r l } { \Sigma _ { j } = ( P _ { j } , T _ { j } ; F _ { j } , M _ { 0 j } ) } & { { } ( 1 \leq i , j \leq n ) } \end{array}$ be the work<sup>fl</sup>ow models for two organizations. $\Sigma _ { i j } = ( P _ { i j } , T _ { i j } ; F _ { i j } , M _ { 0 i j } )$ be the coordination patterns between $\Sigma _ { i }$ and $\Sigma _ { j } ,$ where $P _ { i j } { = } P _ { L i j } \cup$ $P _ { R i j } \cup P _ { M i j } .$

Algorithm 4. To integrate the models and the coordination patterns INPUT: $\Sigma _ { i } = ( P _ { i } , T _ { i } ; F _ { i } , M _ { 0 i } ) , ( 1 \leq i \leq n )$ , and $\Sigma _ { i j } = ( P _ { i j } , T _ { i j } ; F _ { i j } , M _ { 0 i j } )$ (1 ≤ i, $j \leq n )$ ;

Table 9  
Part of the data integrated between the running logs of two different organization work<sup>fl</sup>ows.

<table><tr><td>Organization</td><td>Activity</td><td>Start time</td><td>End time</td><td>ResourceReq</td><td>ResourceRel</td><td>MessageRec</td><td>MessageSent</td></tr><tr><td rowspan="3">Buyer</td><td> $A_{16}$ </td><td>08:00 Aug 01</td><td>08:23 Aug 01</td><td>∅</td><td>∅</td><td>∅</td><td> $\{p_{m14}\}$ </td></tr><tr><td> $A_{17}$ </td><td>10:30 Aug 01</td><td>10:45 Aug 01</td><td> $\{p_{r3}\}$ </td><td> $\{p_{r3}\}$ </td><td>∅</td><td>∅</td></tr><tr><td> $A_{18}$ </td><td>10:46 Aug 01</td><td>10:50 Aug 01</td><td>∅</td><td>∅</td><td> $\{p_{m15}\}$ </td><td> $\{p_{m16}\}$ </td></tr><tr><td rowspan="5">Sender</td><td> $A_{20}$ </td><td>08:24 Aug 01</td><td>08:30 Aug 01</td><td>∅</td><td>∅</td><td> $\{p_{m14}\}$ </td><td>∅</td></tr><tr><td> $A_{21}$ </td><td>08:31 Aug 01</td><td>09:10 Aug 01</td><td>∅</td><td>∅</td><td>∅</td><td> $\{p_{m15}\}$ </td></tr><tr><td> $A_{17}$ </td><td>10:30 Aug 01</td><td>10:45 Aug 01</td><td> $\{p_{r2}\}$ </td><td> $\{p_{r2}\}$ </td><td>∅</td><td>∅</td></tr><tr><td> $A_{22}$ </td><td>10:51 Aug 01</td><td>10:59 Aug 01</td><td>∅</td><td>∅</td><td> $\{p_{m16}\}$ </td><td> $\{p_{m1}\}$ </td></tr><tr><td> $A_{3}$ </td><td>11:30 Aug 01</td><td>11:45 Aug 01</td><td> $\{p_{r2}\}$ </td><td> $\{p_{r2}\}$ </td><td>∅</td><td>∅</td></tr><tr><td rowspan="3">Consignor</td><td> $A_{4}$ </td><td>11:46 Aug 01</td><td>11:50 Aug 01</td><td>∅</td><td>∅</td><td>∅</td><td> $\{p_{m2},p_{m3}\}$ </td></tr><tr><td> $A_{5}$ </td><td>11:56 Aug 01</td><td>12:04 Aug 01</td><td>∅</td><td>∅</td><td> $\{p_{m4},p_{m5}\}$ </td><td> $\{p_{m6}\}$ </td></tr><tr><td> $A_{14}$ </td><td>08:55 Aug 04</td><td>09:00 Aug 04</td><td>∅</td><td>∅</td><td> $\{p_{m9}\}$ </td><td> $\{p_{m10},p_{m11}\}$ </td></tr><tr><td rowspan="3">Shipper</td><td> $A_{28}$ </td><td>11:51 Aug 01</td><td>11:54 Aug 01</td><td>∅</td><td>∅</td><td> $\{p_{m3}\}$ </td><td> $\{p_{m5}\}$ </td></tr><tr><td> $A_{32}$ </td><td>08:47 Aug 04</td><td>08:54 Aug 04</td><td>∅</td><td>∅</td><td>∅</td><td> $\{p_{m9}\}$ </td></tr><tr><td> $A_{33}$ </td><td>09:01 Aug 04</td><td>10:33 Aug 06</td><td>∅</td><td>∅</td><td> $\{p_{m11}\}$ </td><td>∅</td></tr><tr><td rowspan="4">Consignor</td><td> $A_{4}$ </td><td>11:46 Aug 01</td><td>11:50 Aug 01</td><td>∅</td><td>∅</td><td>∅</td><td> $\{p_{m2},p_{m3}\}$ </td></tr><tr><td> $A_{5}$ </td><td>11:56 Aug 01</td><td>12:04 Aug 01</td><td>∅</td><td>∅</td><td> $\{p _{m4},p_{m5}\}$ </td><td> $\{p_{m6}\}$ </td></tr><tr><td> $A_{12}$ </td><td>15:47 Aug 01</td><td>16:28 Aug 01</td><td>∅</td><td>∅</td><td>∅</td><td>∅</td></tr><tr><td> $A_{13}$ </td><td>16:39 Aug 01</td><td>16:44 Aug 01</td><td>∅</td><td>∅</td><td> $\{p_{m7}\}$ </td><td> $\{p_{m8}\}$ </td></tr><tr><td rowspan="3">Carrier</td><td> $A_{25}$ </td><td>11:51 Aug 01</td><td>11:55 Aug 01</td><td>∅</td><td>∅</td><td> $\{p_{m2}\}$ </td><td> $\{p_{m4}\}$ </td></tr><tr><td> $A_{12}$ </td><td>08:35 Aug 01</td><td>10:41 Aug 01</td><td>∅</td><td>∅</td><td>∅</td><td>∅</td></tr><tr><td> $A_{26}$ </td><td>16:29 Aug 01</td><td>16:38 Aug 01</td><td>∅</td><td>∅</td><td>∅</td><td> $\{p_{m7}\}$ </td></tr><tr><td>Carrier</td><td> $A_{31}$ </td><td>08:03 Aug 04</td><td>08:46 Aug 04</td><td>∅</td><td>∅</td><td>∅</td><td>∅</td></tr><tr><td>Shipper</td><td> $A_{31}$ </td><td>08:03 Aug 04</td><td>08:46 Aug 04</td><td>∅</td><td>∅</td><td>∅</td><td>∅</td></tr><tr><td>Buyer</td><td> $A_{19}$ </td><td>10:38 Aug 06</td><td>11:20 Aug 06</td><td>∅</td><td>∅</td><td> $\{p_{m13},p_{m17}\}$ </td><td>∅</td></tr><tr><td>Consignor</td><td> $A_{15}$ </td><td>09:16 Aug 04</td><td>09:20 Aug 04</td><td>∅</td><td>∅</td><td> $\{p_{m12}\}$ </td><td> $\{p_{m13}\}$ </td></tr><tr><td>Buyer</td><td> $A_{19}$ </td><td>10:38 Aug 06</td><td>11:20 Aug 06</td><td>∅</td><td>∅</td><td> $\{p_{m13},p_{m17}\}$ </td><td>∅</td></tr><tr><td>Shipper</td><td> $A_{34}$ </td><td>10:34 Aug 06</td><td>10:37 Aug 06</td><td>∅</td><td>∅</td><td>∅</td><td> $\{p_{m17}\}$ </td></tr></table>

Table 11  
Table 10  
The coordination pattern mined between two different organizations.

<table><tr><td>Organizations</td><td></td></tr><tr><td>The Buyer and Sender organizations</td><td></td></tr><tr><td>The Consignor and Shipper organizations</td><td><img src="/api/attachments/ZHKPJRVS/fulltext/images/96e797cbd68e445b01a57acf7906e7b5433ecd2ff22ee9fdefc3bff57242607d.jpg"/></td></tr><tr><td>The Consignor and Carrier organizations</td><td></td></tr></table>

The coordination pattern mined between organizations.

<table><tr><td>Organization</td><td>Buyer</td><td>Sender</td><td>Consignor</td><td>Shipper</td><td>Carrier</td></tr><tr><td>Buyer</td><td></td><td>The messages exchanged  $\{p_{m14}, p_{m15}, p_{m16}\}$ ; the synchronized activities  $\{A_{17}\}$ </td><td>The messages exchanged  $\{p_{m13}\}$ </td><td>The messages exchanged  $\{p_{m17}\}$ </td><td></td></tr><tr><td>Sender</td><td>The messages exchanged  $\{p_{m14}, p_{m15}, p_{m16}\}$ ; the synchronized activities  $\{A_{17}\}$ </td><td></td><td>The messages exchanged  $\{p_{m1}, p_{m6}, p_{m10}, p_{m12}\}$ ; the synchronized activities  $\{A_{3}, A_{6}, A_{7}\}$ ; the abstract procedure  $\{A_{8-9-10}\}$ </td><td></td><td></td></tr><tr><td>Consignor</td><td>The messages exchanged  $\{p_{m13}\}$ </td><td>The messages exchanged  $\{p_{m1}, p_{m6}, p_{m10}, p_{m12}\}$ ; the synchronized activities  $\{A_{3}, A_{6}, A_{7}\}$ ; the abstract procedure  $\{A_{8-9-10}\}$ </td><td></td><td>The messages exchanged  $\{p_{m3}, p_{m5}, p_{m9}, p_{m11}\}$ </td><td>The messages exchanged  $\{p_{m2}, p_{m4}, p_{m7}, p_{m8}\}$ ; the synchronized activities  $\{A_{12}\}$ </td></tr><tr><td>Shipper</td><td>The messages exchanged  $\{p_{m17}\}$ </td><td></td><td>The messages exchanged  $\{p_{m3}, p_{m5}, p_{m9}, p_{m11}\}$ </td><td></td><td>The synchronized activities  $\{A_{31}\}$ </td></tr><tr><td>Carrier</td><td></td><td></td><td>The messages exchanged  $\{p_{m2}, p_{m4}, p_{m7}, p_{m8}\}$ ; the synchronized activities  $\{A_{12}\}$ </td><td>The synchronized activities  $\{A_{31}\}$ </td><td></td></tr></table>

![](/api/attachments/ZHKPJRVS/fulltext/images/5b59591333505520174b44867ebde356469c32d3b4a9b074045d3caa194a90eb.jpg)  
Fig. 11. The integrated work<sup>fl</sup>ow model of the Consignor organization and the Sender organization.

OUTPUT: $\Sigma = ( P , T ; F , M _ { 0 } )$

Step 1: For i=1 to n:

For j = 1 to n (i ≠ j):

If there is $\Sigma _ { i j }$ such that $P _ { i j } \neq \emptyset , T _ { i j } \neq \emptyset , F _ { i j } \neq \emptyset ,$ or $M _ { 0 i j } \neq \emptyset ,$ then

$$
P _ {L i} \leftarrow P _ {L i} \cup P _ {L i j}, P _ {R i} \leftarrow P _ {R i} \cup P _ {R i j},
$$

$$
P _ {M i} \leftarrow P _ {M i} \cup P _ {M i j},
$$

$P _ { L i } \cup P _ { R i } \cup P _ { M i }$ and $P _ { i j } { = } P _ { L i j } { \cup } P _ { R i j } { \cup } P _ { M i j } ;$

(1.2) $T _ { i } \gets T _ { i } \cup T _ { i j } { \mathrm { : } }$

(1.3) $F _ { i } {  } F _ { i } \cup F _ { i j } ; \mathrm { a n d }$

(1.4) $M _ { 0 i } {  } M _ { 0 i } \cup M _ { 0 i j } .$

EndIf.

EndFor

(1.1) $P _ { L }  P _ { L } \cup P _ { L i } , P _ { R }  P _ { R } \cup P _ { R i } ,$ and $P _ { M } {  } P _ { M } \cup P _ { M i } ;$

(1.2) $T \gets T \cup T _ { i } ;$

(1.3) $F {  } F \cup F _ { i } ; \mathrm { a n d }$

(1.4) $M _ { 0 } \gets M _ { 0 i } \cup M _ { 0 i } .$

EndFor.

Step 2: $P _ { L } \gets P _ { L } \cup \{ i , o \} ; \ T \gets T \cup \{ t _ { s t a r t } , t _ { e n d } \} ; \ F \gets F \cup \{ ( i , t _ { s t a r t } ) , ( t _ { e n d } , o ) \} ;$

and $M _ { 0 } ( i )  1 .$

Step 3: For i=1 to n:

$$
P _ {i} =
$$

(3.1) $\scriptstyle { F  F \cup \{ ( t _ { s t a r t } , p _ { s i } ) , ( p _ { e i } , t _ { e n d } ) \} } ;$

(3.2) $M _ { 0 i } ( p _ { s i } ) \gets 0 ;$

EndFor.

Step 4: Output $\Sigma = ( P _ { L } \cup P _ { R } \cup P _ { M } , T ; F , M _ { 0 } ) .$

The complexity of Algorithm 4 is mainly determined by the <sup>fi</sup>rst step, which is $\mathcal { O } ( n ^ { 2 } * ( | P | ^ { 2 } + | T | ^ { 2 } { + } | F | ) )$ , where $P { = } P _ { L } { \cup } P _ { R } { \cup } P _ { M } .$

<sup>O  þ þ j</sup>In the application case, we take the Consignor work<sup>fl</sup>ow as an example to show its integrated model with the coordination patterns with other organizations. According to Table 11, the Consignor is coordinated with other four organizations. The model of Consignor integrated with the coordination pattern with the Sender is shown in Fig. 11. In Fig. 11, although the models of Consignor and Sender are integrated, each organization only knows its running model and the coordination pattern with another; that is, the model of each organization is not open to others. This integration approach ensures that each organization knows its running model and the coordination pattern with others, and can protect its own model safely.

![](/api/attachments/ZHKPJRVS/fulltext/images/8edca6799e7821e11c08c16c70d66b814dc8f85977b662255f0c4c20c350f70e.jpg)  
Fig. 12. The integrated work<sup>fl</sup>ow model of the Consignor organization and the Carrier organization.

![](/api/attachments/ZHKPJRVS/fulltext/images/37ca0b3e2dfa8805d7305b979355b7c3e8a4ad44dde0a92435cdc3195d32c7fe.jpg)  
Fig. 13. The integrated work<sup>fl</sup>ow model of the Consignor organization and the Shipper organization.

![](/api/attachments/ZHKPJRVS/fulltext/images/7b9e0da8dfcd35fe656046b77a2157e81bb8e065f4bba10371eaffbb26c7a57c.jpg)  
Fig. 14. The integrated model for the multi-modal transportation process.

From Fig. 11, the organizations with which the messages such as p<sub>m2</sub>, p<sub>m3</sub>, p<sub>m4</sub>, p<sub>m5</sub>, p<sub>m7</sub>, p<sub>m8</sub>, p<sub>m9</sub>, p<sub>m11</sub>, p<sub>m13</sub> are exchanged are not identi<sup>fi</sup>ed. It is necessary to integrate the model of the Consignor with the coordination patterns with other organizations. The integration results of the model of the Consignor with the coordination patterns with the Carrier organization and with the Shipper organization are shown in Figs. 12 and 13, respectively. Because there is only one message exchanged between the Buyer and the Consignor organization, the integration result of the model of the Consignor with the coordination patterns with the Buyer organization is not presented here.

Fig. 14 shows the integration result of the model of the Consignor with the coordination patterns with the Buyer, Sender, Carrier and Shipper. The shaded part in Fig. 14 represents the work<sup>fl</sup>ow contents known by the Consignor organization, which includes the process model of its own business and all coordination patterns with other organizations. Although Fig. 14 presents a whole model for the multi-modal transportation process shown in Fig. 1, by using the approach we propose for each organization, to obtain the overall work<sup>fl</sup>ow model from its own perspective and understand the collaboration between its private work<sup>fl</sup>ow and other work<sup>fl</sup>ows. Such a cross-organizational

![](/api/attachments/ZHKPJRVS/fulltext/images/eecd61b90c384a62a151fc547653fea5fe5f8b713526f1c58d16128098227b7e.jpg)  
Fig. 15. The process model of the hospital work<sup>fl</sup>ow created by using Bonita.

```xml
- <steps>
- <step>
    <Activity>A6</Activity>
    <StartTime>08:55 Oct 08</StartTime>
    <EndTime>09:03 Oct 08</EndTime>
    <ResourceReq />
    <ResourceRel />
    <MessageRec>Pm2</MessageRec>
    <MessageSent>Pm3</MessageSent>
    </step>
- <step>
    <Activity>A8</Activity>
    <StartTime>09:09 Oct 08</StartTime>
    <EndTime>09:23 Oct 08</EndTime>
    <ResourceReq />
    <ResourceRel />
    <MessageRec>Pm4</MessageRec>
    <MessageSent>Pm5</MessageSent>
    </step>
- <step>
    <Activity>A11</Activity>
    <StartTime>09:41 Oct 08</StartTime>
    <EndTime>09:46 Oct 08</EndTime>
    <ResourceReq />
    <ResourceRel />
    <MessageRec>Pm6</MessageRec>
    <MessageSent />
    </step>
+ <step>
+ <step>
+ <step>
+ <step>
+ <step>
</steps>
```  
Fig. 16. Part of the work<sup>fl</sup>ow running log of the X-ray Department.

work<sup>fl</sup>ow model integration approach can ensure that each organization obtains its own business model in order to coordinate with other organizations, and can protect its private model safely which is not open to others.

## 7. Experiment evaluation

By using the example of the multi-modal transportation process integration, we can see that the mining and integration approaches from a multi-source log can discover the work<sup>fl</sup>ow model for each organization, the coordination patterns between different organizations and can integrate the model for a cross-organizational collaborative work<sup>fl</sup>ow. However, for each organization, it is only possible to view the overall work<sup>fl</sup>ow model from its own perspective and to understand the collaboration between its private work<sup>fl</sup>ow and other work<sup>fl</sup>ows. In many tightly coupled application cases, the approaches proposed can be used to obtain the overall model for a cross-organizational collaborative work<sup>fl</sup>ow. The overall model obtained for a cross-organizational tightly coupled collaborative work<sup>fl</sup>ow is very important and useful; for example, to solve business con<sup>fl</sup>icts or improve working ef<sup>fi</sup>ciency.

In this section, another example of a collaborative work<sup>fl</sup>ow across different departments in a hospital is used to verify the proposed approach. In this hospital, there are six departments involved in a business work<sup>fl</sup>ow, which are Receptionist Department, Surgical Department, X-ray Department, Charge Office, Cardiovascular Department, and Pharmacy. In order to obtain the running log of the work<sup>fl</sup>ow related to the business of each department, we use Bonita Open Solution, an open source tool provided by BonitaSoft (www.bonitasoft.com), to simulate the hospital work<sup>fl</sup>ow. The work<sup>fl</sup>ow created by using Bonita is shown in Fig. 15.

Bonita can be used for modeling and simulation of a crossorganization collaborative work<sup>fl</sup>ow. After proper con<sup>fi</sup>guration, the work<sup>fl</sup>ow created can run by Bonita. During the running of a work<sup>fl</sup>ow, its running log can be recorded and collected. To verify the mining algorithms proposed in the paper, based on Bonita Open Solution, we have a further development to integrate Bonita with the proposed mining algorithms. Next, six experiments are given to evaluate the approach for process mining and work<sup>fl</sup>ow integration.

## 7.1. Evaluation for process mining

By running the model created by using Bonita shown in Fig. 15, a hospital work<sup>fl</sup>ow system can be obtained. Each department involved in the work<sup>fl</sup>ow can login the system with its role assigned.

For example, the user of the X-ray Department can implement the activities assigned and the system can record the running log. After further development of the Bonita Open Solution, the running log can be transferred into the data in XML format. Part of the work<sup>fl</sup>ow running log of the X-ray Department is shown in Fig. 16.

By using the running log such as shown in Fig. 16 as inputs, the <sup>fi</sup>rst two experiments, Experimen $t _ { 1 }$ and Experimen $t _ { 2 } ,$ are used to evaluate the process mining approach. Through these two experiments, we demonstrate that the proposed process mining algorithms are capable of obtaining different models from different running log data. In these two experiments, Algorithm 1 is applied to the collected data set to obtain the pre-activities and post-activities of each activity, and Algorithm 2 discovers the RM\_WF\_Net model for the hospital work<sup>fl</sup>ow.

Experiment : We collected the running information for 20 work<sup>fl</sup>ow cases completed by the user of the X-ray Department as the data set for this experiment, which are shown in Table 12. To save space, the XML data are given by using a table format. Taking this data set as input to Algorithm 1, the information about each activity can be obtained, such as the pre-activities, post-activities, messages exchanged and resources released or required. Due to space limitations, the information mined about each activity in the work<sup>fl</sup>ow is not presented. Taking the output of Algorithm 1 as input to Algorithm 2, the RM\_WF\_Net model discovered for the work<sup>fl</sup>ow of the X-ray Department is shown in Table 13.

Part of the running log of two different work<sup>fl</sup>ows in the X-ray Department.

<table><tr><td>Experiment</td><td>Activity</td><td>Start time</td><td>End time</td><td>ResourceReq</td><td>ResourceRel</td><td>MessageRec</td><td>MessageSent</td></tr><tr><td rowspan="7"> $Experiment_1$ </td><td> $A_6$ </td><td>08:55 Oct 08</td><td>09:03 Oct 08</td><td>∅</td><td>∅</td><td> $\{p_{m2}\}$ </td><td> $\{p_{m3}\}$ </td></tr><tr><td> $A_8$ </td><td>09:09 Oct 08</td><td>09:23 Oct 08</td><td>∅</td><td>∅</td><td> $\{p_{m4}\}$ </td><td> $\{p_{m5}\}$ </td></tr><tr><td> $A_{11}$ </td><td>09:41 Oct 08</td><td>09:46 Oct 08</td><td>∅</td><td>∅</td><td> $\{p_{m6}\}$ </td><td>∅</td></tr><tr><td> $A_{12}$ </td><td>09:46 Oct 08</td><td>10:11 Oct 08</td><td>∅</td><td>∅</td><td>∅</td><td>∅</td></tr><tr><td> $A_{13}$ </td><td>10:11 Oct 08</td><td>10:19 Oct 08</td><td>∅</td><td>∅</td><td>∅</td><td>∅</td></tr><tr><td> $A_{14}$ </td><td>10:19 Oct 08</td><td>10:33 Oct 08</td><td>∅</td><td>∅</td><td>∅</td><td>∅</td></tr><tr><td> $A_{19}$ </td><td>10:33 Oct 08</td><td>10:37 Oct 08</td><td>∅</td><td>∅</td><td>∅</td><td> $\{p_{m7}\}$ </td></tr><tr><td rowspan="5"> $Experiment_2$ </td><td> $A_6$ </td><td>08:55 Oct 08</td><td>09:03 Oct 08</td><td>∅</td><td>∅</td><td>∅</td><td> $\{p_{m3}\}$ </td></tr><tr><td> $A_8$ </td><td>09:09 Oct 08</td><td>09:23 Oct 08</td><td>∅</td><td>∅</td><td> $\{p_{m4}\}$ </td><td>∅</td></tr><tr><td> $A_{11}$ </td><td>09:41 Oct 08</td><td>09:46 Oct 08</td><td>∅</td><td>∅</td><td> $\{p_{m6}\}$ </td><td>∅</td></tr><tr><td> $A_{12}$ </td><td>09:46 Oct 08</td><td>10:11 Oct 08</td><td>∅</td><td>∅</td><td>∅</td><td>∅</td></tr><tr><td> $A_{19}$ </td><td>10:11 Oct 08</td><td>10:15 Oct 08</td><td>∅</td><td>∅</td><td>∅</td><td> $\{p_{m7}\}$ </td></tr></table>

Table 13  
The work<sup>fl</sup>ow model mined for X-ray Department.  
![](/api/attachments/ZHKPJRVS/fulltext/images/f5b0750e3415361f85ebc84f83a6e00e105f5658e67ddf5e4d7d1c9afe738012.jpg)

Experiment : To generate a different set of data, we changed the work<sup>fl</sup>ow model of the X-ray Department shown in Fig. 15 and collected its running information for 20 work<sup>fl</sup>ow cases again, which are also shown in Table 12. We can see that the running data collected two times for Experiment<sub>1</sub> and Experiment<sub>2</sub> are different. The number of activities and the message information of some activities are changed. Taking this data set as the input for Algorithm 1, and the computing results as the input for Algorithm 2, the RM\_WF\_Net model discovered for the work<sup>fl</sup>ow of the X-ray Department is shown in Table 13.

From Table 13, we can see that the models discovered through Experiment and Experiment are different. Not only is the logic structure of the model different, but also the messages exchanged of activities are different. Experiment and Experiment have demonstrated that the process mining algorithms can identify the structure changes from the running logs.

Experiment : Taking the running log of the work<sup>fl</sup>ow of each department in the hospital, the format of which is similar to that shown in Fig. 16, as input to Algorithm 1, and taking the computing results of Algorithm 1 as input to Algorithm 2, the RM\_WF\_Net models for the work<sup>fl</sup>ows of other departments can be discovered, as shown in Table 14, which include the work<sup>fl</sup>ow models for Receptionist Department, Surgical Department, Charge Office, Cardiovascular Department, and Pharmacy.

The meanings of the transition and place in the models are shown in Table 15. For example, the activities in the work<sup>fl</sup>ow of the Receptionist Department are Register, Interaction and Triage, respectively. A message about Patient Information is sent out after the completion of activity Triage.

The model mined for each department.  
![](/api/attachments/ZHKPJRVS/fulltext/images/88c42161cb060bd03febb346df3057508a0b52b1dbbff76f4fdcdd080ef38064.jpg)

Table 15  
Meanings of symbols in Tables 12, 13, and 14.

<table><tr><td>Symbol</td><td>Meaning</td></tr><tr><td> $A_1$ </td><td>Register</td></tr><tr><td> $A_2$ </td><td>Interaction</td></tr><tr><td> $A_3$ </td><td>Triage</td></tr><tr><td> $A_4$ </td><td>Admissions</td></tr><tr><td> $A_5$ </td><td>Reservation Application</td></tr><tr><td> $A_6$ </td><td>Reservation</td></tr><tr><td> $A_7$ </td><td>Imaging Planning</td></tr><tr><td> $A_8$ </td><td>Imaging Register</td></tr><tr><td> $A_9$ </td><td>Payment  $Notice_1$ </td></tr><tr><td> $A_{10}$ </td><td> $Payment_1$ </td></tr><tr><td> $A_{11}$ </td><td>Imaging Stating</td></tr><tr><td> $A_{12}$ </td><td>Machine Operation</td></tr><tr><td> $A_{13}$ </td><td>Image Processing</td></tr><tr><td> $A_{14}$ </td><td>Backup</td></tr><tr><td> $A_{19}$ </td><td>Report</td></tr><tr><td> $A_{20}$ </td><td>Diagnosis</td></tr><tr><td> $A_{21}$ </td><td>Consultation Application</td></tr><tr><td> $A_{22}$ </td><td>Consultation Plan</td></tr><tr><td> $A_{23}$ </td><td>Consultation</td></tr><tr><td> $A_{24}$ </td><td>Prescription Processing</td></tr><tr><td> $A_{25}$ </td><td>Consultation Summary</td></tr><tr><td> $A_{26}$ </td><td>Accounting</td></tr><tr><td> $A_{27}$ </td><td> $Payment\ Notice_2$ </td></tr><tr><td> $A_{28}$ </td><td> $Payment_2$ </td></tr><tr><td> $A_{29}$ </td><td>Medicine Taking</td></tr><tr><td> $A_{30}$ </td><td>Medicine Packing</td></tr><tr><td> $p_{m1}$ </td><td>Patient Information</td></tr><tr><td> $p_{m2}$ </td><td>Reservation Form</td></tr><tr><td> $p_{m3}$ </td><td>Acceptance Notice</td></tr><tr><td> $p_{m4}$ </td><td>Photo Form</td></tr><tr><td> $p_{m5}$ </td><td> $Cost\ Bill_1$ </td></tr><tr><td> $p_{m6}$ </td><td> $Payment\ Verification_1$ </td></tr><tr><td> $p_{m7}$ </td><td>Report Result</td></tr><tr><td> $p_{m8}$ </td><td>Consultation Form</td></tr><tr><td> $p_{m9}$ </td><td>Prescription</td></tr><tr><td> $p_{m10}$ </td><td> $Cost\ Bill_2$ </td></tr><tr><td> $p_{m11}$ </td><td>Payment Verification</td></tr></table>

## 7.2. Evaluation for coordination pattern mining

In order to evaluate the coordination pattern mining between two different departments, Experiment is given.

Experiment<sub>4</sub>: Any two departments of Receptionist Department, Surgical Department, X-ray Department, Charge Office, Cardiovascular Department, and Pharmacy, their running log data can be integrated. Taking the integrated data about the running log as input to Algorithm 3, the coordination patterns mined between two different departments are presented in detail in Table 16.

There are two kinds of coordination patterns among the departments:

(1) Coordination with synchronized activities. For example, we can see that the coordination pattern between Surgical Department and Cardiovascular Department includes two synchronized activities, Consultation and Prescription Processing, and one message exchanged which is Consultation Form.

(2) Coordination with messages exchanged. For example, the messages exchanged between X-ray Department and Surgical Department include Reservation Form, Acceptance Notice, Photo Form and Report Result.

## 7.3. Evaluation for process integration

Experiment : The last experiment is used to evaluate process integration. According to the RM\_WF\_Net model for the work<sup>fl</sup>ow of each department shown in Table 14 and the coordination patterns between two different departments in Table 16, Algorithm 4 can be used to integrate the model for the whole work<sup>fl</sup>ow. The integration result is shown in Fig. 17.

According to the integrated model shown in Fig. 17 and the meaning of each symbol shown in Table 15, the details of the process model of the hospital work<sup>fl</sup>ow are shown in Fig. 18.

Comparing the models shown in Fig. 18 with the work<sup>fl</sup>ow created by using Bonita in Fig. 15, we can see that the two models are exactly the same. It indicates that the mining and integration approach proposed in the paper can discover the right model.

In contrast to the example about the multi-modal transportation business process, obtaining an overall model for a tightly coupled collaborative cross-organizational work<sup>fl</sup>ow is very important and useful in mastering the overall business. For example, to obtain the overall model as shown in Fig. 17 for a hospital collaborative work<sup>fl</sup>ow, the hospital manager can clearly grasp the business content in the hospital. By using such an overall model, the hospital manager can solve business con<sup>fl</sup>icts and improve working ef<sup>fi</sup>ciency. The scheduling of medical devices can be planned among different departments, for instance, without con<sup>fl</sup>icts according to the overall model mined. Therefore, in a tightly coupled collaborative cross-organizational work<sup>fl</sup>ow, it is not only possible to understand the collaboration between any organization's private work<sup>fl</sup>ow and other work<sup>fl</sup>ows but also to have the overall model for the cross-organizational work<sup>fl</sup>ow.

Table 16  
The coordination patterns mined between departments.  
![](/api/attachments/ZHKPJRVS/fulltext/images/1fbb22bbc7201ee9e5b7fadf8b37c0de45ceedb7d95a7022686e783ccbb0dc25.jpg)

![](/api/attachments/ZHKPJRVS/fulltext/images/fd68b587a68ea4f7e7e71c65f2c52555bbd6195dbc31155516ded01cb5dc5ac6.jpg)  
Fig. 17. The integrated model for the hospital work<sup>fl</sup>ow

## 8. Conclusion

A complex work<sup>fl</sup>ow is usually executed across several organizations, and it is not easy to obtain the overall model for a cross-organizational work<sup>fl</sup>ow. However, the running log of the work<sup>fl</sup>ow systems contains much information about their activities and the relations between activities. We present an approach to applying process mining to discover the model for a cross-organizational work<sup>fl</sup>ow from the distributed running log collected from different servers located in different organizations. Because the running log contains information about resource allocation, an RM\_WF\_Net model is proposed to represent the work<sup>fl</sup>ow discovered. In contrast to the traditional considerations of process mining, the objective is not to discover the RM\_WF\_Net model. We pay more attention to model integration for a cross-organizational work<sup>fl</sup>ow based on the models mined. This paper makes two main contributions.

• A process mining approach to discovering the coordination patterns between different organizations and the work<sup>fl</sup>ow model of each organization for a cross-organizational work<sup>fl</sup>ow from the distributed running log that contains information about resource allocation. The mining result is represented in the formalized form of an RM\_WF\_Net, which can be used to process integration for the cross-organizational work<sup>fl</sup>ow.

• A process integration approach for a cross-organizational work<sup>fl</sup>ow according to the coordination patterns and the RM\_WF\_Net of each organization.

Although the work<sup>fl</sup>ow mining approach for one single organization cannot address some special structures such as choices or invisible tasks, there are few application limitations for the approach proposed.

![](/api/attachments/ZHKPJRVS/fulltext/images/0d7f06ac63c2c0200595c24437e63ec4e3560d238ef77c58a995643bf1b8b143.jpg)  
Fig. 18. The process model of the hospital work<sup>fl</sup>ow.

Theoretically, the proposed approach can be useful if the work<sup>fl</sup>ow model for one single organization is without special structures and the coordination relations between different organizations can be expressed by the given four kinds of patterns, i.e., coordination with synchronized activities, coordination with messages exchanged, coordination with shared resources, and coordination with abstract procedures. By experiments, we <sup>fi</sup>nd that all kinds of cross-organization work<sup>fl</sup>ows can be discovered and integrated by the approach proposed if they can be created and simulated by Bonita.

In this paper, we assume that the running log of the work<sup>fl</sup>ow used for process mining does not have data noise. However, noisy data may occur when, for instance, the wrong activity is implemented such as one of another activity's pre-activities or post-activities. Obviously, the model mined from the noisy data cannot re<sup>fl</sup>ect the true structure and behavior of the work<sup>fl</sup>ow. In a cross-organizational work<sup>fl</sup>ow system, the running log may contain more noisy data, and in future work we will focus on a detection approach for noise in the running log. Meanwhile, resource allocation among different partners within a cross-organizational work<sup>fl</sup>ow is important for avoiding resource con<sup>fl</sup>icts. An integration approach using process mining is presented in this paper to obtain the model for a cross-organizational work<sup>fl</sup>ow. How to apply the model, integrated to verify and check resource con<sup>fl</sup>icts within a cross-organizational work<sup>fl</sup>ow, will also be addressed in our future work.

## Acknowledgment

This paper is supported partly by the NSFC (61170079 and 61202152); the Sci. and Tech. Development Fund of Shandong Province of China (2010GSF10811); the Specialized Research Fund for the Doctoral Program of Higher Education of China (20103718110007) and the Special Fund for Fast Sharing of Science Paper in Net Era by CSTD (2012107), the Sci. and Tech. Development Fund of Qingdao (10-3-3-32-nsh), the Strategic Research Grant sponsored by the City University of Hong Kong (project no: 7002628); and the Natural Science Foundation for Distinguished Young Scholars of Shandong and SDUST (JQ200816 and 2010KYJQ101).

## References

[1] R. Agrawal, D. Gunopulos, F. Leymann, Mining process models from work<sup>fl</sup>ow logs, in: EDBT '98: Proceedings of the 6th International Conference on Extending Database Technology, Springer-Verlag, London, UK, 1998, pp. 469–483.

[2] H. Duan, Q. Zeng, H. Wang, S.X. Sun, D. Xu, Classi<sup>fi</sup>cation and evaluation of timed running schemas for work<sup>fl</sup>ow based on process mining, Journal of Systems and Software 82 (3) (2009) 400–410.

[3] G. Greco, A. Guzzo, G. Manco, Mining and reasoning on work<sup>fl</sup>ows, IEEE Transactions on Knowledge and Data Engineering 17 (4) (2005) 519–534, (senior Member-Domenico Sacca).

[4] R. Heckel, Open Petri nets as semantic model for work<sup>fl</sup>ow integration, in: Hartmut Ehrig, Wolfgang Reisig, Grzegorz Rozenberg, Herbert Weber (Eds.), Petri Net Technology for Communication-Based Systems — Volume 2472 of Lecture Notes in Computer Science, Nov. 2003, pp. 281–294.

[5] S.-Y. Hwang, W.-S. Yang, On the discovery of process models from their instances, Decision Support Systems 34 (1) (2002) 41–57.

[6] S.-Y. Hwang, C.-P. Wei, W.-S. Yang, Discovery of temporal patterns from process instances, Computers in Industry 53 (3) (2004) 345–364.

[7] J.-Y. Jung, H. Kim, S.-H. Kang, Standards-based approaches to b2b work<sup>fl</sup>ow integration, Computers and Industrial Engineering 51 (2) (2006) 321–334.

[8] R. Liu, A. Kumar, W.M.P. van der Aalst, A formal modeling approach for supply chain event management, Decision Support Systems 43 (3) (2007) 761–778.

[9] L. Maruster, J.C. Wortmann, A.J.M.M. Weijters, W.M.P. van der Aalst, Discovering distributed processes in supply chains, in: H. Jagdev, J.C. Wortmann, H.J. Pels (Eds.), APMS. Vol. 257 of IFIP Conference Proceedings, Kluwer, 2002, pp. 219–230

[10] T. Murata, Petri nets: properties, analysis and applications, Proceedings of the JEEE (Apr. 1989).541-580

[11] C.A. Petri, Kommunikation mit automaten, in: Technical Report RADC-TR-65–377 1.1-Suppl, 1. English Translation Griffiss Air Force Base New York 1966.

[12] R.G. Qiu, Y. Tang, Q. Xu, Integration design of material <sup>fl</sup>ow management in an e-business manufacturing environment. Decision Support Systems 42 (2) (2006) 1104-1115.

[13] W. Reisig, Petri Nets: An Introduction, Springer-Verlag New York, Inc., New York NY, USA, 1985.

[14] S. Sun, A. Kumar, J. Yen, Merging work<sup>fl</sup>ows: a new perspective on connecting business processes, Decision Support Systems 42 (2) (2006) 844–858.

[15] S.X. Sun, Q. Zeng, H. Wang, Process-mining-based work<sup>fl</sup>ow model fragmentation for distributed execution, IEEE Transactions on Systems, Man, and Cybernetics, Part A 41 (2) (2011) 294–310.

[16] W.M.P. van der Aalst, The application of Petri nets to work<sup>fl</sup>ow management, The Journal of Circuits, Systems and Computers 8 (1) (1998) 21–66.

[17] W.M.P. van der Aalst, Loosely coupled interorganizational work<sup>fl</sup>ows: modeling and analyzing work<sup>fl</sup>ows crossing organizational boundaries, Information Management 37 (2) (2000) 67–75.

[18] W.M.P. van der Aalst, Con<sup>fi</sup>gurable services in the cloud: supporting variability while enabling cross-organizational process mining, in: Proceedings of the 2010 International Conference on On the Move to Meaningful Internet Systems — Volume Part I. OTM'10, Springer-Verlag, Berlin, Heidelberg, 2010, pp. 8–25.

[19] W.M.P. van der Aalst, B.F. van Dongen, Discovering work<sup>fl</sup>ow performance models from timed logs, in: EDCIS '02: Proceedings of the First International Conference on Engineering and Deployment of Cooperative Information Systems, Springer-Verlag, London, UK, 2002, pp. 45–63.

[20] W.M.P. van der Aalst, B.F. van Dongena, J. Herbst, L. Marustera, G. Schimm, A.J.M.M. Weijters, Work<sup>fl</sup>ow mining: a survey of issues and approaches, Data and Knowledge Engineering 47 (2) (Nov. 2003) 237–267.

[21] W.M.P. van der Aalst, T. Weijters, L. Maruster, Work<sup>fl</sup>ow mining: discovering process models from event logs, IEEE Transactions on Knowledge and Data Engineering 16 (9) (2004) 1128–1142.

[22] W.M.P. van der Aalst, M. Dumas, C. Ouyang, A. Rozinat, E. Verbeek, Conformance checking of service behavior, ACM Transactions on Internet Technology 8 (May 2008) 13:1–13:30.

[23] Z.J. Wang, X.F. Xu, Business process integration point classi<sup>fi</sup>cation and the priority evaluation method, International Journal of Business Information Systems 4 (2) (2009) 210–232.

[24] H. Wang, Q. Zeng, Modeling and analysis for work<sup>fl</sup>ow constrained by resources and nondetermined time: an approach based on Petri nets, IEEE Transactions on Systems, Man, and Cybernetics, Part A 38 (4) (2008) 802–817.

[25] H. Weigand, W.-J. van den Heuvel, Cross-organizational work<sup>fl</sup>ow integration using contracts, Decision Support Systems 33 (3) (2002) 247–265.

[26] Q. Zeng, Two symmetrical decomposition methods for structure-complex Petri nets and their applications, in: SNPD '07: Proceedings of the Eighth ACIS International Conference on Software Engineering, Arti<sup>fi</sup>cial Intelligence, Networking, and Parallel/Distributed Computing (SNPD 2007), IEEE Computer Society, Washington, DC, USA, 2007, pp. 1101–1106.

[27] Q. Zeng, H. Wang, D. Xu, H. Duan, Y. Han, Con<sup>fl</sup>ict detection and resolution for work<sup>fl</sup>ows constrained by resources and non-determined durations, Journal of Systems and Software 81 (9) (2008) 1491–1504

[28] J. Zhu, Z. Tian, T. Li, W. Sun, S. Ye, W. Ding, C.C. Wang, G. Wu, L. Weng, S. Huang, B. Liu, D. Chou, Model-driven business process integration and management: a case study with the bank sinopac regional service platform, IBM Journal of Research and Development 48 (5/6) (2004) 649–669.

Qingtian Zeng is a professor at the College of Information Science and Engineering, Shandong University of Science and Technology, and was a visiting professor at the Department of Information Systems at City University of Hong Kong in 2008. He obtained his Ph.D. in computer software and theory from the Institute of Computing Technology at the Chinese Academy of Sciences in 2005. His research interests are in the areas of Petri nets. Process Mining, Ontology, Knowledge Acquisition and Management. He can be reached at qtzeng@sdust.edu.cn or qtzeng@163.com.

Sherry Sun received the M.S. and Ph.D. degrees in Management Information Systems from the Eller College of Management, the University of Arizona, Tucson, Arizona, USA. She is currently an assistant professor at the Department of Information Systems, City University of Hong Kong. Her research focuses on the development of work<sup>fl</sup>ow technology and its applications in electronic commerce, knowledge management, and organizational process automation. Before joining the City University of Hong Kong, she worked as a database developer in the Arti<sup>fi</sup>cial Intelligence Lab at the University of Arizona and a database administrator in the Arizona Cancer Center. She can be reached at sherry.sun@cityu.edu.hk

Hua Duan is an associate professor at the College of Information Science and Engineering, Shandong University of Science and Technology. She obtained her Ph.D. in applied mathematics from Shanghai Jiaotong University in 2008. Her research interests are in the areas of Petri nets, Process Mining, and Machine Learning. She can be reached at hduan@sdust.edu.cn.

Cong Liu is a master student at the College of Information Science and Engineering, Shandong University of Science and Technology. His research interests are in the areas of Petri nets, Process Mining, Ontology, and Work<sup>fl</sup>ow Management. He can be reached at 15066802144@163.com

Huaiqing Wang is a professor at the Department of Financial Math and Financial Engineering at South University of Science and Technology of China. He specializes in research and development of business intelligence systems, intelligent agents and their applications (such as multi-agent supported <sup>fi</sup>nancial information systems, virtual learning systems knowledge management systems and conceptual modeling). He received his Ph D, in computer science from the University of Manchester in 1987. He can be reached at wang hq@sustc educn.
