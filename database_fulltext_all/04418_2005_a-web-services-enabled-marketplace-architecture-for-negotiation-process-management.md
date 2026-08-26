---
otero_id: 4418
otero_key: "TERNQ5FU"
title: "A Web Services-enabled marketplace architecture for negotiation process management"
authors: "Jin Baek Kim; Arie Segev"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.04.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Web Services-enabled marketplace architecture for negotiation process management

Jin Baek Kim<sup>a,b</sup>, Arie Segev<sup>b,c,</sup>\*

<sup>a</sup> Department of Industrial Engineering and Operations Research, University of California-Berkeley, Berkeley, CA, USA <sup>b</sup> Fisher Center for IT and Marketplace Transformation, Haas School of Business, University of California-Berkeley, Berkeley, CA, USA <sup>c</sup> Haas School of Business, University of California-Berkeley, Berkeley, CA, USA

Available online 18 December 2004

## Abstract

As the eBusiness environment becomes more pervasive and dynamic, negotiations between companies are required more frequently than ever. Despite its potential value and the progress in research, the adoption of negotiation systems has been slow in practice. We believe one reason for this is insufficient consideration of process management aspects such as process design, description, and deployment. Business negotiations must be approached from the process management perspective since they take place in the context of corporate processes such as procurement or sales.

In this paper, we study system support and automation of business-to-business (B2B) negotiations from the process management perspective. We propose a Web Services-enabled marketplace architecture for negotiation process management and refine it by adding pattern-based process composition. We validate the concept by implementing the proposed architecture using BPEL4WS and evaluating it from various perspectives.

Keywords: Negotiation; Business process management; Inter-organizational business process; Marketplace; Web Services; BPEL4WS

## 1. Introduction

Negotiation is an essential business activity for establishing trade relationships and fine-tuning terms and conditions. As the business environment becomes more dynamic, negotiations between companies are required more frequently than ever. Business negotiations often involve multiple issues and multiple parties. The required amount of information processing and communication in those cases can easily exceed a single human being’s capability, especially when there are many negotiation issues and partners. Therefore, systems supporting and automating business negotiations have a great potential value. Considering the degree of automation achieved in other business process domains, the importance of managing negotiations to achieve more efficient business operations has become even higher. Since most business negotiations are in the context of corporate procurement or sales process, negotiation systems must be approached from the business process management perspective. However, most of the previous studies on negotiation systems have heavily focused on strategies and decision making, and paid little attention to realistic process management aspects.

Negotiation is a challenging business process for several reasons. First, it is an inter-organizational business process because every negotiation involves at least two companies. Inter-organizational processes have been considered as one of the most demanding business processes to manage due to many issues such as process autonomy, integrity, security, etc. [2,43]. Second, this process is interleaved with many other internal and external business processes such as procurement or sales. For example, procurement negotiation often needs coordination with various activities such as requisitioning, approval, receiving, inspection, and payment. Similarly, sales negotiation frequently requires interactions with marketing, credit management, production, inventory management, delivery, etc. In addition, negotiation involves collaborative decision making by many stakeholders within the organization such as accounting, marketing, production, shipping, and warehouse departments.

Management of such inter-organizational processes interleaved with other processes is complex. Early research on inter-organizational workflows focused mostly on the integration of small number of tightly coupled business processes [4]. These traditional approaches impose limitations when it comes to dynamic eBusiness. The Internet and the web have changed the requirements for inter-process functionality dramatically. Tying processes together at the back end did not work when multiple processes had to come together through a web interface, e.g., online banking. Time to market and agility associated with higher degree of inter-organizational business interaction demand a level of integration and flexibility way above traditional levels. We view this as one of the major issues in enabling eBusiness transformation in enterprises. Process interleaving concept was introduced by Segev [38] to describe the new requirements beyond traditional integration and workflow. Interleaving is a relative term and denotes a higher level of integration compared to a base state. Its significance is in eBusiness enablement to achieve dynamic ‘‘configurations’’ of various processes in general and customer solutions in particular (see Refs. [38,39] for a more elaborate discussion).

In this paper, we approach corporate negotiations from the process management perspective. We utilize principles from the interleaved processes framework by Segev [38] and the negotiation process framework by Kim and Segev [23], to design an architecture for the support of negotiation processes. First, we analyze negotiations from the inter-organizational business process perspective, and propose a marketplace-based architecture for the definition, execution, and control of negotiation processes. Then, we explain the benefits of using Web Services to manage these processes and show how they can be applied to implement the proposed marketplace-based architecture. Furthermore, to facilitate the generation and modification of negotiation processes, we propose a pattern-based composition of the processes. Finally, we evaluate the proposed solution from various perspectives.

## 2. Previous research on negotiation support and automation

Research on computer-assisted negotiations started in the 1980s. The so-called negotiation support systems (NSS) were software tools supporting negotiation activities such as eliciting preferences, evaluating and comparing offers based on the elicited preferences and Best Alternative to a Negotiated Agreement (BATNA), recommending strategies based on case-based negotiation studies, etc. These early studies on NSS focused on various issues including system design [20], usage of NSS in business [15], theories underlying NSS [26], effect of participant’s cognitive and socio-emotional biases [16], group decision aspects of NSS [21], and the behavior of negotiators [22].

In the Artificial Intelligence arena, fully automated negotiations using negotiation software agents (NSA) have been considered. In this approach, the intelligent software agents communicate with other agents and make decisions on behalf of the owner, according to the pre-programmed strategies with or without learning. Strategies of negotiation software agents were designed and analyzed based on game theory and heuristics. In the Santa Fe double auction programming contest [34] and Trading Agent Competition [46], the performance of various agent strategies was experimentally examined through agent competition.

Su et al. [45] developed a system that falls between full automation and simple assistance. The system automatically sends messages and makes simple decisions based on the specified constraints, while complex and final decisions are left to the user.

Despite the wide variety in approaches, studies on negotiation automation have heavily focused on decision making. The negotiation process has been informally defined mostly in natural languages. In addition, the negotiation process was given to the users ‘‘as is’’ and users were not allowed to control or specify the process. Further, the given negotiation processes were too simple to meet the required complexity in real business negotiations. Table 1 shows studies on the negotiation systems and underlying negotiation process.

Benyoucef et al. [6,7] and Bassil et al. [1] studied combined negotiations from the workflow management perspective. The combined negotiation is a negotiation in which a user engages in many negotiations at the same time. They developed a Combined Negotiation Support Systems (CNSS) that helps the user coordinate all the dependent negotiations. They illustrated the functional requirements of a CNSS and developed a prototype named CONSENSUS, using commercial WfMS—IBM’s MQSeries [7] and BEA’s WebLogic [1]. In the architecture of CONSENSUS, the users design the combined negotiation process at the design time. Then the software agents are assigned to each individual negotiation of the combined negotiation process and execute the process. IBM Zurich Research Lab is also implementing software tools for state machine based negotiation design, ontology editing, and communication, in their SilkRoad project [44].

## 3. Web Services-enabled marketplace architecture

Research on business process management suggests that marketplace-based architecture is a good solution for managing inter-organizational processes such as negotiation processes because marketplacebased links between companies are more efficient than point-to-point links between every buyer and every supplier [2,54]. Emerging Web Services and Web Services-based process definition standards provide mechanisms for formally defining negotiation processes that can be clearly understood and quickly deployed in a platform-independent manner. In this section, first we review and evaluate Web Services and Web Services-based process management technologies in the context of negotiation process. Then, we identify the requirements of a marketplace system for managing negotiation processes and propose a

Negotiation processes used in negotiation system research

<table><tr><td>Platforms</td><td>Underlying negotiation process</td></tr><tr><td>Kersten and Noronha (INSS) [22]</td><td>A buyer and a seller exchange offers alternating their turns (two negotiation issues).</td></tr><tr><td>Smith (ContractNet) [41]</td><td>RFQ+ sealed bidding (negotiation agents are collaborative).</td></tr><tr><td>Sandohlm (TRACONET) [34]</td><td>RFQ+ sealed bidding (negotiation agents are non-collaborative and self-interested).</td></tr><tr><td>Maes et al. (KASBAH) [29]</td><td>A buyer agent sends an offer to a seller agent. Then the seller agent says “yes” or “no”.</td></tr><tr><td>Sandohlm and Lesser [36]</td><td>RFQ+ sealed bidding (commitment can be withdrawn after paying some penalty).</td></tr><tr><td>Rosenschein and Zlotkin (Monotonic Concession Protocol) [33]</td><td>Each party makes offer alternately. Each offer must be “better” than the previous offers to the other party.</td></tr><tr><td>McFadzean and Tesfatsion (TNG) [30]</td><td>Buyer agents send offers to the sellers. A seller picks a buyer among many offers from the buyers.</td></tr><tr><td>Tsvetovatyy et al. (MAGMA) [47]</td><td>A supplier posts an advertisement and the buyer sends an offer to the supplier.</td></tr><tr><td>Esmahi et al. (MIAMAP) [14]</td><td>Negotiation between a buyer and a seller is mediated by a third party.</td></tr><tr><td>Lee et al. (Time-bounded Protocol) [25]</td><td>Tasks are announced first and sellers submit bids on the tasks with a time bound. Buyer can reject or award the bid with a time bound.</td></tr><tr><td>Dasgupta et al. (MAgNET) [13]</td><td>A buyer agent contacts the supplier agents one-by-one asking for the price quote. The supplier agent provided the best quote is selected.</td></tr><tr><td>Rachlevsky-Reich et al. (GEM) [32]</td><td>Buyer and seller submit the quotes. The broker executes orders and announces the quotes and settled prices.</td></tr></table>

Web Services-enabled marketplace architecture that satisfies those requirements. Finally, we check the feasibility of the concept by implementing a negotiation process conforming to the architecture.

## 3.1. Web Services technology for negotiation process management

Web Services are distributed application components that provide services through open standard based interfaces, Web Service Definition Language (WSDL). A Web Service has a platform-independently interpretable meta-information about the interface, as well as platform-independently accessible interfaces built based on widely accepted lower-level standards such as SOAP, XML, and HTTP. It has been pointed out that one of the key missing features of WSDL is the mechanism for coordinating multiple Web Services [9,26]. For example, the current WSDL standard can be used only for state-less interactions such as request– response of price quote and availability [24]. Thus, complementary Web Services standards have been proposed for choreographing Web Services to create Web Services-based processes. For example, Web Service Choreography Interface (WSCI), approved by W3C, can describe message flows between Web Services [51]. Business Process Management Language (BPML), proposed by the Business Process Management Initiative (BPMI), is augmented by Web Services coordination functionality [10].

Although currently there is no dominating standard for describing processes through choreography of Web Services, the consensus is that Business Process Execution Language for Web Services (BPEL4WS), supported by industry leaders such as IBM, Microsoft, BEA Systems, SAP, and Siebel, acquired the momentum to become the Web Services-based process definition standard [24]. BPEL4WS was proposed in 2002, based on two earlier workflow description languages, WSFL and XLANG. BPEL4WS supports design and implementation of Web Services-based processes by providing mechanisms to preserve the state of Web Services by properly correlating messages exchanged between Web Services. Also, it supports Long-Running (Business) Transactions (LRTs) by providing a mechanism for flexible control of the reversal operation. This is achieved by providing the ability to define fault handling and compensation [9].

BPEL4WS is layered on top of the lower level Web Services standards such as WSDL, SOAP, and XML. Several BPEL4WS authoring tools are available. For example, IBM distributes a BPEL4WS authoring tool, BPWS4J, and Collaxa [12] offers a BPEL4WS authoring tool and execution engine. Many workflow software companies including market leaders such as IBM, BEA Systems, and Microsoft announced that the next version of their business process engines will support BPEL4WS.

Since negotiations are inter-organizational business processes, they must be clearly understood in the context of heterogeneous systems. Also, the implemented processes must have interoperable interfaces because a negotiation process often requires interactions with many internal and external systems. By using BPEL4WS, a negotiation process can be clearly defined and the defined process can be platformindependently understood and deployed. Furthermore, since the activities in the BPEL4WS process are Web Services, the negotiation processes deployed on the BPEL4WS engines will have Web Service interfaces that are based on open standards. Since BPEL4WS is a new standard still under development, the expressive power of BPEL4WS is limited. According to Wohed et al. [53], it supports 11 out of 18 commonly required workflow patterns. However, its expressive power is richer than any other Web Services-based process standard [48].

Workflow management system architectures are classified into production-oriented, message-based, and document-centric [43]. Considering that message routing between negotiation partners is the primary task, the architecture of negotiation process management systems falls into the message-based architecture category. BPEL4WS focuses on correlated exchanges of messages among Web Services. So, BPEL4WS is an ideal technology for negotiation process management systems from the general system architecture perspective.

## 3.2. Web Services-enabled marketplace architecture for negotiation process management

Recently emerging approaches emphasize transformation of supply chains into open marketplaces and composition of loosely coupled services [4]. Marketbased inter-organizational process management has been examined and validated by several studies. Ludwig and Whittingham [28] proposed a solution for setting and managing inter-organizational workflows through contracts on the controlled way to access workflow systems. Hull and Su [19] proposed an inter-organizational process coordination system, which has an interface integrating information transfer, status checking, and workflow instance history query.

We argue that the following four functional groups are the key requirements of a marketplace system for negotiation process management: shared ontology and message formats, process definition, execution/ control of the process, and interoperable system interfaces. Each requirement is discussed in detail next.

## 3.2.1. Shared ontology and message formats

Since negotiation partners may have different business practices, there is always a possibility of confusion in the meaning of the term. For example, the meaning of the ‘‘product’’ and ‘‘delivery’’ may be widely different depending whether the company belongs to the manufacturing or service sector. The term ‘‘price’’ may mean the total price, unit price, before tax price, after tax price, or other depending on business convention. The marketplace needs to supply a glossary of common definition of the terms to reduce the cost caused by the confusion.

Based on the shared understanding of the terms, the marketplace can provide negotiation message formats and templates. The message template may contain common negotiation variables such as unit price, quantity, delivery date, freight mode, payment terms, deposit requirement, return policy, insurance premium, warranty, maintenance terms, etc.

## 3.2.2. Negotiation process definition

The first step of the system-supported negotiation is to establish shared understanding of the rules of the negotiation (i.e. negotiation process). Thus, the negotiation process must be clearly defined and easily interpreted. However, defining negotiation processes from scratch takes time and efforts and checking the correctness of the defined process (e.g. deadlock-free)

requires expertise. The marketplace is in the best position to define negotiation processes because it can accumulate know-how in designing negotiation processes while supporting various transactions. The negotiation processes defined and given by the marketplace have also a clear advantage in accessibility and reusability.

## 3.2.3. Negotiation process execution and control

Once the negotiation partners agree on the negotiation process, an instance of the negotiation process needs to be instantiated, controlled, and monitored. The marketplace can execute and control the negotiation process by invoking and scheduling activities according to the process definition. It can also enforce the commitment of negotiation partners by providing a non-repudiation mechanism. The marketplace is also in the best position to execute and control negotiation processes because it can provide a neutral third-party’s perspective.

## 3.2.4. Interoperable system interfaces

Since buyers and sellers with heterogeneous systems need to interact with the marketplace, platform-independent system interfaces are a critical requirement.

Fig. 1 visually describes the proposed architecture of the Web Services-enabled marketplace that satisfies the key requirements. As stated in the previous section, since Web Services-based process management technology solves interoperability problems related to process definition and execution, we propose to use them for implementing the marketplace system for negotiation process management. Following the proposed architecture, the Web Servicesenabled marketplace is an inter-organizational process management system that mediates negotiation partners’ systems through Web Services. The marketplace has a repository of executable negotiation process defined in BPEL4WS and runs the Web Services-based process execution engine that enacts and controls the negotiation process. In addition, the proposed marketplace architecture contains the repository of shared ontology, message formats and templates. Buyer’s and seller’s internal workflow systems can either directly interact with the marketplace through Web Services or indirectly interact with the marketplace through Web Services-enabled negotiation software agents. Consequently, the users in both the buyer and seller sides may choose a level of automation ranging from completely manual control (i.e. participate in every step of the negotiation) through their internal workflow systems, to fully delegated negotiation authority to negotiation software agents. In most cases, we anticipate a level in between the two . , or choose the level in-between by properly coordinating the workflow system and software agent.

![](/api/attachments/TERNQ5FU/fulltext/images/c197d882b20306e93555daf62aa720c0ebac655422718bbadfad89ad3c2bea36.jpg)  
Fig. 1. Conceptual architecture for Web Services-enabled marketplace for negotiation process management.

## 3.3. Implementation of the proposed architecture using WSDL and BPEL4WS

In this section, we demonstrate a Web Servicesbased implementation of the proposed marketplace architecture. As a base case, we consider a negotiation process that is based on a Request-for-Quote (RFQ) business practice. In this scenario, we assume the negotiation starts from receiving a RFQ from the buyer. Then, the seller and buyer exchange offers in alternating turns until reaching an agreement. Following Benyoucef and Keller [2], we describe the negotiation process using the state chart diagram shown in Fig. 2; this diagram type has advantages over other visual modeling methods in its clarity and ease of mapping to the execution level. Fig. 3 shows the structure of the BPEL4WS implementation using the Collaxa style flow diagram [12]. Each circle in the diagram corresponds to a Web Service interface for receiving and sending messages. In order to implement it, we use ‘‘while’’ and ‘‘switch’’ constructs in BPEL4WS. Arbitrary cycles of activities are not allowed in the current BPEL4WS standard, not all the possible conversation-based negotiation processes are implementable in BPEL4WS [24]. However, as pointed out by Wohed et al. [53], it is possible to model classes of structured conversations in BPEL4WS. Alternating-offer negotiation is one of the structured conversations which can be implemented by the current version of BPEL4WS.

Offer exchange activities are modeled as asynchronous communication. It often takes time to evaluate an offer, to make a decision on the received offer, and to create and send a counter-offer. Therefore, it is reasonable to adopt asynchronous communication mode for exchanges of the decision intensive messages. For the activities that can be easily automated, synchronous communication mode is more appropriate for expediting the process. When negotiation messages are binding, acknowledgement may be automatically sent as soon as the accept message is received. So, we implemented accept-and-acknowledgement activity in synchronous communication.

![](/api/attachments/TERNQ5FU/fulltext/images/29cac89ecc8fe24d6c239bf91d1ba0336c0f064e142f81fb56117b04b7c499b4.jpg)  
Fig. 2. State chart description of the RFQ-based alternating offer negotiation process.

Listing 1 and Listing 2 show the WSDL and BPEL4WS implementation of the negotiation process described in Figs. 2 and 3. Due to the limited space, only the skeletons of WSDL and BPEL4WS are presented. WSDL description of a Web Service consists of two parts of definitions: service interface and service implementation definitions. Service interface provides logical information on the interface. Service implementation definition describes physical information of a particular Web Service instance such as network address of service endpoint, protocols, security requirements and other attributes. Four elements are required for WSDL service interface definition: Types, Messages, PortTypes, and Binding. Types specifies the data type of the elements in the message. Messages defines packages exchanged within a single message transfer. PortTypes groups messages to abstract operations. The circles in Fig. 3 correspond to the PortTypes level. Binding maps the

PortTypes elements into concrete communication protocols [42].

The conflicts between the general and company specific definitions of the terms and message formats can be managed by using the name space. In Listing 2, the terms and formats of the messages are imported from a fictitious negotiation ontology service called negotiaitonOntology.org, with the associated prefix for the namespace ‘‘sns’’. Using the name spaces the industry standard ontology and message formats can be identified, imported, and reused. The negotiation service offers seven port types, called receiveRFQPT, sendSellerOfferPT, receiveSellerResponsePT, sendBuyerOfferPT, receiveBuyerResponsePT, getAckFromSellerPT, and getAckFromBuyerPT, with appropriate operations for accepting the data from the seller and the buyer. These portTypes are properly combined into two partner link types, one for the seller called sellerMarketLT and one for the buyer called buyerMarketLT.

![](/api/attachments/TERNQ5FU/fulltext/images/0aa152a2477514d0a0ad2b25795be8f33ef32a048ba5427e6f90572ec1167b19.jpg)  
Fig. 3. Flow diagram for BPEL4WS implementation of a RFQ-based simple negotiation process described in Fig. 2.

On receiving the RFQ, a negotiation process instance is created. A negotiation is uniquely identified by a negotiationID. So, the seller and buyer need to provide this information (i.e. negotiationID) in their messages. We used Boolean expressions on the value of acceptanceFlag element in the messages for implementing the stopping criteria of the while-loop. The asynchronous communications are implemented using invoke and call-back operations. Since the marketplace deals with many buyers and sellers, each pair of buyer–seller needs to give their endpoint references, which are used by the marketplace so that the negotiation service can respond properly. As stated earlier, acknowledgement activity adopts synchronous communication mode and it is implemented using the synchronous invocation method.

The stopping criteria used in the base case scenario is that either the buyer or seller accepts an offer. We used Boolean expression on the acceptance in the ‘while’ condition and ‘switch’ cases. BPEL4WS uses four types of expressions: Boolean-valued expressions (transition conditions, join conditions, while condition, and switch cases), deadline-valued expressions (‘‘until’’ attribute of onAlarm and wait), duration-valued expressions (‘‘for’’ attribute of onAlarm and wait), and general expressions (assignment) [9]. Thus, we can consider implementing other stopping criteria such as time and number of round in BPEL4WS.

From the perspective of proposed architecture, combined negotiation mentioned in Section 2 is a set of dependent negotiation instances. It can be implemented either at the internal workflow system level or at the marketplace level. In the first case, only the party performing the combined negotiation knows that negotiation instances are in the combined negotiation context, and the other parties do not know their negotiations are sub-negotiations of the combined negotiation. CNSS model considered by Benyouceff et al. [6,7] is applicable in this case. In other words, the plan for coordinating dependent negotiation instances can be considered through the internal workflow system in design-time, and the negotiation instances are executed with some tactics through software agents in run-time. In the second case where combined negotiations are considered at the marketplace level, all parties know about the combined negotiation and how it is structured because the negotiation process defined in the market is common information that is available to the negotiation partners.

## 4. Design, generation, and modification of negotiation processes

A business negotiation process is often ad hoc in nature because the relationships between negotiation partners are dynamic and the most appropriate negotiation process is dependent on the specific case. Stohr and Zhao [43] identified five issues in managing ad hoc workflows: (1) ease of generating new processes, (2) flexibility, (3) understandability, (4) information sharing, and (5) processes for decision support and collaboration. The proposed Web Services-enabled marketplace architecture is a nice solution to understandability and information sharing issues and intentionally leaves internal decision and collaboration processes to the negotiation partner side. However, the generation of new negotiation processes and their modification are not well supported. It is often the case that at least minor changes to the given negotiation process are desirable in order to accommodate company- or casespecific issues. For example, rather than a plain sealed-bid auction, a buyer may want to use a twostage sealed-bid auction mechanism when there are many candidate suppliers: the first sealed-bid auction for screening the suppliers and the second one to select a supplier. Furthermore, to increase competition, the buyer may wish to announce the bids received in the first stage. To meet the buyer’s needs in this case, the buyer must be allowed to change the typical one-stage sealed-bid negotiation process.

To summarize, because of the ad hoc nature of the negotiation process, it is important to provide negotiation partners with a tool for generating and modifying negotiation processes. For this, we propose a pattern-based process model where negotiation processes are composed by the configuration of the patterns of each process attribute. Research on negotiation frameworks [8,17,23,44] is a good starting point for analyzing attributes and patterns of negotiation processes since those frameworks studied domain-independent comprehensive and integrated guidelines for modeling negotiations and developing negotiation systems. Table 2 shows the attributes of the negotiation process and possible patterns of each attribute we identified [23]. Using the attributes, the previously mentioned two-stage sealed bid can be composed by selecting a pattern in each negotiation process attribute as follows:

– Initiation: buyer initiated

– Number of parties: multi-party (BUYER:SEL-LER = ONE:MANY)

Purpose: selection (a single supplier)

– Stages: multi-stage (two stages)

– Offer exchange rule: one-sided offer (seller-sided offer)

– Commitment: binding in both stages.

Fig. 4 shows the user interface of the prototype pattern-based negotiation process composition tool. The tool allows buyers, sellers, and market operators to generate the negotiation process based on the selection of the pattern in each process attribute. Once the patterns are selected, BPEL4WS code can be generated, edited, and validated. Because the marketplace runs the BPEL4WS engine, the generated BPEL4WS code for the negotiation process can be quickly deployed. It has constraintbased feasibility checking function for determining if the selected combination of patterns yields a meaningful negotiation process. The tool is also a gateway to register the user defined negotiation process to the process repository of the marketplace system.

Table 2  
Attributes and patterns of negotiation processes

<table><tr><td>Attributes</td><td colspan="2">Patterns</td></tr><tr><td>Initiation</td><td>Buyer initiated Seller initiated</td><td></td></tr><tr><td>Number of Parties</td><td>Bilateral Multi-parties</td><td>BUYER:SELLER one:many many:one many:many Inter-mediated</td></tr><tr><td>Purpose</td><td>Selection Coordination Hybrid</td><td></td></tr><tr><td>Stages</td><td>Single stage Multi-stage</td><td>Offer Exchange Rules Alternating offer One-sided offer Arbitrary</td></tr><tr><td rowspan="2">Commitment</td><td>Binding Non-binding Penalty</td><td>Penalty Calculation Scheme Time based Commitment amount based Etc.</td></tr><tr><td>Contingent</td><td>Contingency condition Offers from other parties Time External events Etc.</td></tr><tr><td>Information sharing with other negotiation processes</td><td>Transparent Non-transparent Partly transparent</td><td>Information Revelation Rule Profile-based Offer-based Etc.</td></tr></table>

The negotiation through the current B2B marketplaces has been severely restricted. Most of the negotiation processes supported by the marketplace (e.g. various types of auction) have been limited in complexity and flexibility. The negotiation through general communication channels provides the maximum flexibility in process but the minimum codified information on the process and exchanged data. Most of the operating B2B marketplaces support negotiations in the following way [17,50].

(1) The marketplace, founded by a major buyer or a third party, supports a set of simple negotiation processes such as auctions and bidding.

(2) The buyers and suppliers in the marketplace advertise their requests or products/services, and select a negotiation process (e.g. auction, sealedbidding)

(3) The buyers and suppliers find negotiation partners.

(4) Negotiation partners make an agreement on the negotiation process.

(5) When the negotiation partners cannot find the appropriate negotiation process in the given set of negotiation processes, they may decide to negotiate through the communication channel provided by the marketplace or through other channels such as email, fax, phone, meetings, etc. In this case, there is no formal description and agreement of the negotiation process.

(6) Negotiation partners perform the negotiation until reaching an agreement or breaking off the negotiation.

The proposed architecture with the component based process composition tool allows users to generate a flexible negotiation processes which can be clearly understood as follows.

(1) The marketplace offers a set of negotiation processes, say $P { = } \{ P _ { 1 } , . . . . P _ { n } \}$ , in BPEL4WS and a set of process attributes $\boldsymbol { \mathit { I I } } { = } \{ \boldsymbol { \mathit { I I } } _ { 1 } , . . . , \boldsymbol { \mathit { I I } } _ { m } \}$ The attribute $\boldsymbol { \varPi _ { j } }$ contains patterns $\pi _ { k }$ (i.e. $\varPi _ { j } { = } \{ \pi _ { 1 } , . . . , \pi _ { p } \} $ . Each process $P _ { i }$ is a combination of the patters for the attributes (i.e. $P _ { i } { = } \{ \pi _ { 1 } , . . . . , \pi _ { m } \}$ where $\pi _ { j } { \in } { I I _ { j } } )$

(2) The marketplace provides component based negotiation process composition tool. Using the tool, users can easily generate a new process $P _ { k }$ in BPEL4WS by selecting patterns for negotiation process attributes $\cal { I I } = \{ I I _ { 1 } , . . . . , I I _ { m } \}$ , modifying the attributes in the ready-made process, or editing a BPEL4WS code.

(3) The buyers and suppliers in the marketplace advertise their requests or products/services. The party can start with a negotiation process which may be either one of the given negotiation processes $P _ { i }$ or a new negotiation process $P _ { k }$ created by the process composition tool.

![](/api/attachments/TERNQ5FU/fulltext/images/52a56e1e3b30098abd7cba80d65ee2187ff96e60aa17299fdef5570f7bf8edf6.jpg)  
Fig. 4. User interface for pattern-based negotiation process configuration based on the process attributes and patterns in Table 2

(4) Buyers and suppliers find negotiation partners.

(5) The buyer’s and seller’s system can clearly understand the negotiation process. Depending on the situation, the negotiation process selected at the beginning may need to be changed while setting up the negotiation. The process composition tool enables easy modification of the process. Negotiation partners agree on the negotiation process.

(6) The marketplace instantiates and controls the negotiation process and provides negotiation partners with Web Service interfaces for sending and receiving messages.

(7) Negotiation partners perform the negotiation through the marketplace with the aid of Web Services-enabled internal workflow systems or negotiation software agents.

## 5. Evaluation of the proposed architecture

In this section, we evaluate the proposed architecture from various perspectives suggested in the workflow literature. Sheth et al. [40] envisioned three types for marketplace-based inter-organizational business process management: process portal, process vortex, and dynamic trading process. A process portal manages inter-organizational processes on a one-to-one basis, while interactions between buyers and sellers occur through a third party in the process vortex. Dynamic trading process constructs workflow processes dynamically on a per customer basis considering unique company-specific attributes. Among these three types, the proposed architecture can be considered as a dynamic trading process since pattern-based negotiation process composition allows generation of the customized negotiation processes accommodating company specific issues.

Since negotiation systems need to interact with heterogeneous internal and external processes and systems, interoperability is a critical issue. The Workflow Management Coalition (WfMC) recommended the evaluation of interoperability based on the interoperability mode and interoperability level.

Three types of interoperability modes were suggested: chained process, nested process, and parallel

synchronized. In the chained process mode, the process instance being enacted on workflow engine A triggers the creation and enactment of a subprocess instance on workflow engine B. In the nested process mode, the process instance enacted on a workflow engine causes the creation and enactment of a sub-process instance on another engine. Then it waits for the termination of the sub-process before carrying on with its own enactment. In the parallel synchronized mode, two workflow engines enact process instances simultaneously and a rendezvous has been specified. The first workflow engine achieved the rendezvous point waits for the other to do the same. Once both process instances achieved the respective rendezvous points, there is some interchange between the workflow engines. The proposed architecture is close to the nested process mode since the negotiation process instance which is running on the marketplace triggers internal decision making process of negotiation partners and waits for the response from them.

As for the level of interoperability, WfMC suggested eight levels. Level 1 through Level 5 indicates the increasing degree of interoperability ranging from no interoperability to the common API set. Level 6 means shared definition format and Level 7 is protocol compatibility. The highest level of interoperability, Level 8, requires common look and feel utilities. Web Service interface provides the interoperability up to Level 5. The proposed marketplace architecture achieves Level 6 and Level 7 by providing shared ontology/message formats and BPEL4WS based clear inter-organizational process definition. The highest level of interoperability, common look and feel utilities, needs modification of buyer or seller side systems or negotiation partner’s internal systems, which is out of the scope of this paper.

Table 3  
Evaluation of the proposed architecture from various perspectives

<table><tr><td>Criteria</td><td>Types</td><td>The proposed architecture</td></tr><tr><td rowspan="3">Marketplace architecture for inter-organizational process management (Sheth et al. [40])</td><td>Process portal</td><td>Dynamic trading process</td></tr><tr><td>Process vortex</td><td></td></tr><tr><td>Dynamic trading process</td><td></td></tr><tr><td rowspan="3">WfMC Mode of interoperability [52]</td><td>Chained process</td><td>Nested process</td></tr><tr><td>Nested process</td><td></td></tr><tr><td>Parallel synchronized</td><td></td></tr><tr><td>WfMC Level of interoperability [52]</td><td>Level 1-Level 8</td><td>Level 7: Protocol compatibility</td></tr><tr><td rowspan="4">Zhao&#x27;s workflow interoperability framework [54]</td><td>Connectivity</td><td>Open standard based (Web Services-based) interoperable interface</td></tr><tr><td>Expressivity</td><td>Limited by the expressive power of BPEL4WS and other Web Services-based process definition standards. Current BPEL4WS standard (ver 1.1) supports 11 workflow patterns among 18 patterns suggested by van der Aalst et al. [49,53]</td></tr><tr><td>Visibility</td><td>Process status information is available. Information related to internal decision making is hidden intentionally for preserving information privacy</td></tr><tr><td>Flexibility</td><td>Flexible processes that can be easily modified through pattern-based process composition</td></tr><tr><td rowspan="5">Issues in the ad hoc WfMS (Stohr and Zhao [43])</td><td>Ease of generating new process</td><td>Easy process generation through attributes- and pattern-based process composition</td></tr><tr><td>Understandability</td><td>Platform-independent understandability</td></tr><tr><td>Flexibility</td><td>Flexible because of pattern-based process configuration</td></tr><tr><td>Information sharing</td><td>Only offers and counter-offers are revealed</td></tr><tr><td>Protocols for decision support and collaboration</td><td>Decision support and process management are separated</td></tr></table>

Zhao [55] proposed a workflow interoperability description framework consists of four dimensions: connectivity, expressivity, visibility, and flexibility. Connectivity means the method and stability of connection between the business partners. Among the illustrated connection types (hardwired connection, contract-based access, negotiated access, spontaneous access), the proposed architecture corresponds to the negotiated access type because the negotiation process needs to be agreed upon by negotiation partners each time they perform the negotiation. Expressivity means the ability to functionally communicate with other systems. Since the proposed architecture adopts BPEL4WS, the expressive power of the proposed architecture will grow as BPEL4WS is developed and elaborated. Visibility indicates levels of viewable data and process. Visibility is intentionally restricted to the information on the definition and execution of the shared part of the inter-organizational process (i.e. negotiation process). The data and information on the internal process of the negotiation partners are limited because information privacy is critical in negotiations. Flexibility is the ability to change process specifications. The pattern-based process composition allows easy creation of flexible processes. However, since the negotiation process becomes a contract after negotiation partners agree on it, user control of the process during run-time is naturally constrained.

Table 3 summarizes the evaluation presented in this section.

## 6. Conclusion

In this paper, we proposed a Web Servicesenabled marketplace architecture for negotiation process management. The marketplace based architecture is a solution to the problems in managing negotiation processes, whose nature is inter-organizational, ad hoc, and dynamic. The marketplace conforming to the architecture provides the repository of clearly defined and quickly deployable negotiation processes clearly defined based on open standard, as well as the shared ontology and message formats. We also proposed the pattern-based negotiation process composition tool for easy generation of flexible negotiation processes and their modification to alleviate problems in managing ad hoc business processes such as negotiations. The biggest advantage of the Web Services-enabled marketplace is the increased size of the pool of potential negotiation partners. Through the Web Services interfaces, heterogeneous systems of trading partners can dynamically link with each other through the marketplace. Furthermore, multiple marketplaces can be connected with each other to create a bigger aggregated marketplace.

To our knowledge, this paper is the first to present a marketplace architecture that integrates negotiation systems, business process management, and Web Services technologies. Although there have been various approaches in negotiation system research, little attention has been paid to process management aspects. We believe that the first step towards automating complex business negotiations is to resolve issues in process management. This is necessary because the automation of strategic decision making is possible only after the negotiation processes are clearly understood and can be executed in a platform-independent way.

## 7. Uncited references

[37]

## Acknowledgements

This research was partly supported by the Intel Corporations and the State of California NGI Program under contract #CEMC/NGI 000104.

## Appendix A. Listings

## A.1. Listing 1

```xml
BPEL4WS for negotiation process described in Fig. 3

<process name="negotiationService"
targetNamespace="http://marketplace.com"
xmlns:ns="http://marketplacecom/wSDL/negotiationService"
...
>
<partnersLinks>
<partnerLink name="seller" partnerLinkType="ns:sellerMarketLT" myRole="negotiationService" partnerRole="seller"/>
<partnerLink name="buyer" partnerLinkType="ns:buyerMarketLT" myRole="negotiationService" partnerRole="buyer"/>
</partners>

<!-- definition of variables and correlation sets omitted due to limited space -->
<!-- structure of the business process -->
<sequence>
<receive partner="buyer" portType = "ns:receiveRFQPT" createInstance="yes"...> . . . </receive>
<invoke name="sendRFQWithBuyerInformation" partner="seller" portType="ns:sendSellerOfferPT" . ../>
<receive name="receiveQuote" partner="seller" portType="ns:receiveSellerResponsePT" . ../>
<invoke name="sendQuoteToBuyer" partner="buyer" portType="ns:sendBuyerOfferPT" . ../>
<receive name="receiveBuyerResponseToQuote" partner="buyer" portType="ns:receiveBuyerResponsePT" . ../>
<switch>
<case condition = "bpws:getVariableProperty('buyerMessage','ns:acceptFlagFromBuyer') = true">
<invoke name="getAckFromSeller" partner="seller" portType="ns:getAckFromSellerPT" . ../>
</case>
<otherwise>
<while condition="bpws:getVariableProperty('buyerMessage','ns:acceptFlagFromBuyer') = false and
bpws:getVariableProperty('sellerMessage','ns:acceptFlagFromSeller') = false " >
<invoke name="sendOfferToSeller" partner="seller" portType="ns:sendSellerOfferPT" . ../>
<receive name="receiveSellerResponseToOffer" partner="seller" portType="ns:receiveSellerResponsePT" . ../>
<switch>
<case condition = "bpws:getVariableProperty('sellerMessage','ns:acceptFlagFromSeller') = true">
<invoke name="getAckFromBuyer" partner="buyer" portType="ns:getAckFromBuyerPT" . ../>
</case>
<otherwise>
<invoke name="sendOfferToBuyer" partner="buyer" portType="ns:sendBuyerOfferPT" . ../>
<receive name="receiveBuyerResponseToOffer" partner="buyer" portType="ns:receiveBuyerResponsePT" . ../>
<switch>
<case condition = "bpws:getVariableProperty('buyerMessage','ns:acceptFlagFromBuyer') = true">
<invoke name="getAckFromSeller" partner="seller" portType="ns:getAckFromSellerPT" . ../>
</case>
</switch>
</otherwise>
</switch>
</while>
</otherwise>
</switch>
</sequence>
</process>
```

## A.2. Listing 2

WSDL for the BPEL4WS description of negotiation process in Listing 1.

```xml
<definitions
targetNamespace="http://marketplace.com/wsdl/negotiationService"
xmlns:tns="http://marketplace.com/wsdl/negotiationService"
xmlns:sns="http://negotiationOntoloty.org/xsd/message"
...>
<import namespace="http://negotiaitonOntology.org/xsd/messages"
location="http://negotiationOntoloty.org/xsd/messages.xsd"/>
<!-- Message for communication with the seller -->
<message name = "sellerOfferMessage">
<!-- use the common ontology and message format for the offer message -->
<part name="sellerOffer" type="sns:sellerOffer"/>
<message name = "sellerAnswerMessage"> ... </message>
<!-- Message for communication with the buyer -->
<message name = "RFQMessage"> ... </message>
<message name = "buyerOfferMessage"> ... </message>
<message name = "buyerAnswerMessage"> ... </message>
<portType name="receiveRFQPT">... </portType>
<portType name="sendSellerOfferPT">... </portType>
<portType name="receiveSellerResponsePT">... </portType>
<portType name="sendBuyerOfferPT">... </portType>
<portType name="receiveBuyerResponsePT">... </portType>
<portType name="getAckFromSellerPT">... </portType>
<portType name="getAckFromBuyerPT">... </portType>
<!-- Context type used for locating negotiation process via negotiatoin Id -->
<bpws:property name="negotiationId" type="xsd:string"/>
<bpws:propertyAlias propertyName="tns:negotiaitonId"
messageType="tns:sellerOfferMessage" part="negotiationId"/>
<bpws:propertyAlias propertyName="tns:negotiaitonId"
messageType="tns:buyerOfferMessage" part="negotiationId"/>
...
<!-- Partner link type for buyer/negotiationService -->
<plink:partnerLinkType name="tns:buyerMarketLT">
    <plink:role name="negotiationService">
    <plink:portType name="tns:receiveBuyerResponsePT"/>
    </plink:role>
    <plink:role name="buyer">
    <plink:portType name="tns:sendBuyerOfferPT"/>
    </plink:role>
</plink:partnerLinkType>
<!-- Partner link type for seller/negotiationService -->
<plink:partnerLinkType name="tns:sellerMarketLT">
    <plink:role name="negotiationService">
    <plink:portType name="tns:receiveSellerResponsePT"/>
    </plink:role>
    <plink:role name="seller">
    <plink:portType name="tns:sendSellerOfferPT"/>
    </plink:role>
</plink:partnerLinkType>
</definitions>
```

## References

[1] S. Bassil, M. Benyoucef, R. Keller, P. Kropf, Addressing dynamism in e-Negotiations by workflow management systems, Proceedings of the 13th International Workshop on Database and Expert Systems Applications (DEXA2002), Aix-en-Provence, France, (2002 September).

[2] A. Basu, A. Kumar, Research commentary: workflow management issues in e-business, Information Systems Research 13 (1) (2002) 1 – 14.

[3] C. Beam, A. Segev, Automated negotiations: a survey of the state of the art, Wirtschaftsinformatik 39 (3) (1997 June) 263 – 268 (Friedr. Vieweg and Sohn Verlagsgesellschaft).

[4] B. Benatallah, M. Dumas, M.-C. Fauvet, F. Rabhi, in: F.A. Rabhi, S. Gorlatch (Eds.), Towards Patterns of Web Services Composition, Patterns and Skeletons for Parallel and Distrib uted Computing, 2002.

[5] M. Benyoucef, R. Keller, An evaluation of formalisms for negotiations in e-commerce, Proceedings of the Workshop on Distributed Communities on the Web, (2000) 45 – 54, Quebec City, QC, Canada.

[6] M. Benyoucef, H. Alj, M. Vezeau, R. Keller, Combined negotiation in e-commerce: concepts and architecture, Electronic Commerce Research 1 (2001) 277 – 299.

[7] M. Benyoucef, S. Bassil, R. Keller, Workflow modeling of combined negotiations in e-Commerce, Proceedings of the 24th International Conference on Electronic Commerce Research (ICER-4), (2001) 348 – 359.

[8] M. Bichler, G. Kersten, S. Strecker, Towards a structured design of electronic negotiations, Group Decision and Negotiation 12 (4) (2003) 311– 335.

[9] BPEL4WS, http://www.106.ibm.com/developerworks/ webservices/library/ws-bpel/.

[10] Business Process Modeling Language, http://www.bpmi.org bpml.esp.

[11] D. Chiu, C. Cheung, P. Hung, Developing e-negotiation process support by Web Services, The First International Conference on Web Services, Las Vegas, (2003) 97 – 103.

[12] Collaxa, http://www.collaxa.com.

[13] P. Dasgupta, N. Narasimhan, L. Moser, P. Melliar-Smith, MAgNET: mobile agents for networked electronic trading, IEEE Transactions on Knowledge and Data Engineering 11 (4) (1999 July – Aug.) 509 – 525 IEEE.

[14] L. Esmahi, J. Bernard, P. Dini, MIAMAP: a virtual marketplace for intelligent agents, in: Proceedings of the 33rd Annual Hawaii International Conference on System Sciences, vol. 2, 2000.

[15] A. Foroghi, A survey of the user of computer support for negotiation, Journal of Applied Business Research, (1995 Spring) 121– 134.

[16] A. Foroughi, M. Jelassi, NSS solutions to major negotiation stumbling blocks, Proceedings of Hawaiian Conference on System Sciences, Hawaii, 1990.

[17] FreeMarkets, http://www.freemarkets.com.

[18] C. Holsapple, H. Lai, A. Whinston, A formal basis for negotiation support system research, Group Decision and Negotiation 7 (1998) 203– 227.

[19] R. Hull, J. Su, The vortex approach to integration and coordination of workflows, Workshop on Cross-organizational Workflow Management and Coordination, 1999.

[20] M. Jelassi, A. Foroughi, Negotiation support systems: an overview of design issues and existing softwares, Decision Support Systems 5 (2) (1989) 167 – 181.

[21] N. Karacapilidis, C. Pappis, A framework for group decision support systems: combining AI tools and OR techniques, European Journal of Operations Research 103.

[22] G. Kersten, S. Noronha, WWW-based negotiation support: design, implementation, and use, Decision Support Systems, Newport Beach 25 (2) (1999 March) 135 – 154 (Elsevier).

[23] J. Kim, A. Segev, A framework for dynamic ebusiness negotiation processes, IEEE Conference on e-Commerce, Newport Beach, (2003 June) 84 – 91.

[24] J. Kim, A. Segev, A. Patankar, M. Cho, Web Services and BPELWS for Dynamic eBusiness Negotiation Processes, Proceedings of the International Conference on Web Services, Las Vegas, (2003 June) 111 –117.

[25] K. Lee, Y. Chang, J. Lee, Time-bound negotiation framework for electronic commerce agents, Decision Support Systems 28 (2000) 319– 331.

[26] F. Leymann, D. Roller, M.-T. Schmidt, Web Services and business process management, IBM Systems Journal 41 (2) (2002) 198– 211 (Special issue on new developments in Web services and e-Commerce).

[27] L. Lim, I. Benbasat, A theoretical perspective of Negotiation Support Systems, Journal of Management Information Systems 9 (3) (1993) 27– 44.

[28] H. Ludwig, K. Whittingham, Virtual enterprise coordinator: agreement-driven gateways for cross-organizational workflow management, International Joint Conference on Work Activities Coordination and Collaboration, San Francisco, (1999) 22–25.

[29] P. Maes, A. Chavez, Kasbah: an agent marketplace for buying and selling goods, Conference on Practical Applications of Intelligent Agents and Multi-Agent Technology, 1996 April.

[30] D. McFadzean, L. Tesfatsion, An agent-based computational model for evolution of trade networks, Iowa State University, Ames, IA, http://www.econ.iastate.edu/tesfatsi.

[31] A. Patankar, A. Segev, Inter-organizational business process management using Web Services: a case study and research issues, Proceedings of the International Conference on Web Services, Las Vegas, 2003 June.

[32] B. Rachlevsky-Reich, I. Ben-Shaul, N.T. Chan, A.W. Lo, T. Poggio, GEM: a global electronic market system, Information Systems 24 (6) (1999 Sept) 495– 518 (Elsevier).

[33] J. Rosenschein, G. Zlotkin, Rules of Encounter, MIT Press, 1994.

[34] J. Rust, J. Miller, R. Palmer, Behavior of trading automata in a computerized double auction market, in: J. Rust, D. Friedman (Eds.), The Double Auction Market: Institutions, Theories, and Evidence, Addision Wesley, Reading, MA, 1993, pp. 153– 196.

[35] T. Sandholm, An Implementation of the Contract Net Protocol Based on Marginal Cost Calculations, vol. AAAI-93, 1993.

[36] T. Sandholm, V. Lesser, Issues in automated negotiation and

electronic commerce: extending the contract net framework, . First International Conference on Multi-agent Systems, San Francisco, CA, 1995.

[37] T. Schal, Workflow management systems for process organizations, Lecture Notes in Computer Science, Springer, 1991.

[38] A. Segev, A Framework for Design Centric Content Management, Working Paper 02-WP-49, Fisher Center for Information Technology and Marketplace Transformation (CITM), Haas School of Business, University of California, Berkeley, 2002.

[39] A. Segev, From Mass Customization to ePersonalization. Working Paper 02-WP-50, Fisher Center for Information Technology and Marketplace Transformation (CITM), Haas School of Business, University of California, Berkeley, 2002.

[40] A. Sheth, W. van der Aalst, I. Arpinar, Process driving the networked economy, IEEE Concurrency 7 (3) (1999) 18 – 31.

[41] R. Smith, The contract net protocol: high-level communication and control in a distributed problem solver, Readings in distributed artificial intelligence, Morgan Kauffmann Publishing, 1988, pp. 357 – 366.

[42] M. Stal, Web Services: beyond component-based computing, Communications of the ACM 45 (10).

[43] E. Stohr, J.L. Zhao, Workflow automation: overview and research issues, Information Systems Frontiers 3 (3) (2001 September).

[44] M. Stro¨bel, C. Weinhardt, The Montreal taxonomy for electronic negotiations, Group Decision and Negotiation 12 (2003) 143– 164.

[45] S. Su, C. Huang, J. Hammer, Y. Huang, H. Li, L. Wang, Y. Liu, C. Pluempitiwiriyawej, M. Lee, H. Lam, An internetbased negotiation server for e-commerce, The VLDB Journal 10 (2001) 72–90.

[46] Trading Agent Competition, http://auction2.eecs.umich.edu.

[47] M. Tsvetovatyy, M. Gini, B. Mobasher, Z. Wieckowski, MAGMA: an agent based virtual market for electronic commerce, Applied Artificial Intelligence, vol. 6, special issue on Intelligent Agents, 1997 September.

[48] W. van der Aalst. Workflow Patterns. http://tmitwww.tm.tue.nl/ research/patterns (2003).

[49] W. van der Aalst, K. van Hee, Workflow Management: Models, Methods, and Systems, The MIT Press, 2002.

[50] VerticalNet, http://www.verticalnet.com.

[51] Web Service Choreography Interface (WSCI) 1.0, http:// www.w3.org/TR/2002/NOTE-wsci-20020808.

[52] WfMC (Workflow Management Coalition), http://www. wfmc.org.

[53] P. Wohed, W. van der Aalst, M. Dumas, A. ter Hofstede, Pattern Based Analysis of BPEL4WS, Technical Report

FIT-TR-2002-04, Queensland University of Technology, Australia, 2002.

[54] XPath, http://www.w3.org/TR/xpath.html.

[55] J.L. Zhao, Interoperability requirements for cooperative workflows in electronic commerce, Proceedings of the 2nd International Conference on Telecom. and Electronic Commerce (ICTEC99), Nashville, TN, 1999.

![](/api/attachments/TERNQ5FU/fulltext/images/2e0bd91f05b7fee065c18bc955d8a4b4841d8e027b79cc216e04e49b1a513a83.jpg)

Jin Baek Kim received a BSc in Electrical Engineering from Seoul National University and a MS in Industrial Engineering and Operations Research from University of California, Berkeley. He is currently completing his PhD in Industrial Engineering and Operations Research at University of California, Berkeley. He has worked for the Fisher Center for Information Technology and Marketplace Transformation, Haas School of Business

as a researcher and system engineer, since 2000. His research interests are in the fields of e-Business and supply chain management, especially auction, negotiation, and collaboration support systems.

![](/api/attachments/TERNQ5FU/fulltext/images/bf5b6b752835c1d9835c30a578ccd8abc7ed837b5dffa20585b2c5f5eeaf091c.jpg)

Arie Segev is a Professor of Business and Director of the Fisher Center for information Technology and Marketplace Transformation at the Haas School of Business, University of California, Berkeley. His research has been focused on Enabling eBusiness Transformation, including eBusiness process transformation, Mass Customization and Personalization, eNegotiations and eCollaboration, Sense-and-Respond Context-Dependent Process Architecture

Design, and Information Management and Quality. Professor Segev has led research projects involving the above topics in various domains including Supply Chains, Customer Interaction, B2B Procurement, and Electronics and Architectural Design Environments. He has published over 120 papers on technology and management issues and been the recipient of major government and industry grants. He holds Bsc and Msc in Industrial Engineering and Management from the Technion-Israel Institute of Technology, and an MS in Operations Research and a PhD in Computers and Information Systems from the University of Rochester. Further information about Professor Segev’s research can be found at http://haas.berkeley.edu/citm.
