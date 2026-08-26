---
otero_id: 6550
otero_key: "HQZMCW5Z"
title: "A case study of an inter-enterprise workflow-supported supply chain management system"
authors: "Jianxun Liu; Shensheng Zhang; Jinming Hu"
year: "2005"
journal: "Information & Management"
doi: "10.1016/j.im.2004.01.010"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A case study of an inter-enterprise workflow-supported supply chain management system

Jianxun Liu<sup>a,\*</sup>, Shensheng Zhang<sup>b</sup>, Jinming Hu<sup>b</sup>

<sup>a</sup>Department of Computer Science and Engineering, Hunan University of Science and Technology, Hunan, PR China <sup>b</sup>CIT Laboratory, Department of Computer Science and Engineering, Shanghai Jiao Tong University, PR China Accepted 20 January 2004 Available online 2 June 2004

## Abstract

Doing business over the Internet is cheap and convenient. This enlarges the view of enterprises and gives them an opportunity to select their partners. To support business-to-business operations, an information system (IS) with an embedded workflow management component is needed. The inherent characteristics of such a system makes it suitable to implement cross-organization management. Nowadays, however, these system additions are not common. When developing a supply chain management (SCM) system for a large motorcycle corporation in China, we had to construct an inter-enterprise architecture using the internet. The main part of this is a workflow-supported inner supply chain system and an integrated interface. In it, the business processes are defined and executed by the supply chain management system. The independent inner systems are connected by the integrated interface into a large, global, supply chain manage system to management business processes across the independent enterprises. This paper presents the system design and implementation and discusses our experiences and lessons learned. <sup>#</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: Workflow management; Supply chain; Electronic commerce; Interoperability; Agent

## 1. Introduction

Business organizations today face a complex and competitive environment. Because of this, e-commerce is becoming more dynamic. It is now termed open E-commerce [18]. In this, different enterprises put their services and resources together so that they appear to be a traditional enterprise to their customers but are better called virtual enterprises (VE) [4]. The relationship between members is thus different from that within a traditional enterprise, because the members are independent, constituent, and dynamic and the business process is scattered over multiple enterprises and subject to frequent change. However, the agility of a company’s response to customer demand has been recognized as a critical success factor in meeting competition.

This implies that a cross-enterprise IS, is pressingly needed. It should aid in implementing interoperability among independent enterprises, smoothing the information flow between them, and deploying business processes over multiple enterprises. To satisfy and respond quickly to the requirements, many companies are now focusing on supply chain management (SCM) system in order to strengthen their ability to compete. This has therefore been recognized as an important area for IT innovation and investment [2].

Workflow is the automation of a business process. It has now been adopted as a way to implement the cross organization management needed to carry out businesses. The internet’s world-wide web has become the prime driver of contemporary electronic commerce (E-commerce). Phan [15] holds the view that the most successful new business models are probably those that can integrate IT to all activities of the enterprisewide value chain.

## 2. Supply chain management system and WfMS

## 2.1. Supply chain management

The supply chain can be regarded as a business process to construct enterprise-wide methods. It is defined in many ways. The International Center for Competitive Excellence defined it to be [3] ‘‘the integration of key business processes from end user through original suppliers that provides products, services and information that add value for customers and other stakeholders.’’ With the implementation of supply chain management, the narrow focus of managers and the adversarial relationships between logistics providers, suppliers, and customers are replaced by strategic alliances and long-term cooperative relationships. Suppliers and customers are viewed as partners instead of adversaries with the objective of ‘‘maximizing competitiveness and profitability for the company as well as for the whole supply chain network including the end-customer’’ [14]. Levary [9] suggests that the benefits of a supply chain include:

(1) minimizing the bullwhip effect,

(2) maximizing the efficiency of activities,

(3) minimizing the inventories,

(4) minimizing cycle times,

(5) achieving an acceptable level of quality.

The major success factors for a supply chain are effective management of strategic alliances, extensive data management capabilities, and advanced interorganizational IS to enable better information exchange; this provides more up-to-date information and allows for more accurate inventory responses to change in demand and appropriate inventory levels [24]. However, the participating enterprises usually are independent and distributed. The relationship between them has the following characteristics [7].

\- Goal-orientation: If an enterprise A (manufacturer) needs enterprise B to do a task (take an order to supply material), A will set up an agreement between them for that task. After that, A will not interfere with B. This means that the relation between enterprises is more dynamic and changing.

\- Privacy: An independent organization does not want to disclose details of its process models. Therefore, a service provider usually does not grant access to all internal information about the ongoing process. Equally, a service requester does not want to disclose its process models or organization database to its business partners.

\- Flexibility: A provider wants to change internal procedures without asking permission of or informing the requester, unless the change affects the commitment with the requester. The same is true for the requester.

\- Independence: Both parties want to stay independent of changes in the other, as long as the outcome is not affected.

Thus an open, standard and adaptable SCM system is needed to carry out business processes across enterprises and workflow and Internet technology are the obvious choices for its implementation.

## 2.2. Workflow management system (WfMS)

Conventionally, business processes were implemented by hard-coding business process related aspects, such as control and data flow, into the organization’s software systems. This leads, however, to inflexible systems that were hard to modify and maintain. Workflow is a technology that addresses such problems by separating and abstracting business processes from the software systems [8]. It is the automation of a business process, during which documents, information, or tasks are passed from one participant to another for action, according to a set of procedural rules [20]. A WfMS is used to define, create, and manage the execution of workflows through the use of software running on one or more workflow engine. The engines can interpret the process definition, interact with workflow participants, and, where required, invoke the use of IT tools and applications.

Workflow has now become a leading tool in modeling enterprise business rules by taking advantage of continuous advancements of IT [1]. Its inherent characteristics make it suitable to implement cross organizational management. Unfortunately, today’s workflow management systems are generally designed to support the workflow within one business unit rather than between business units. Moreover, those from different vendors have problems in cooperation [17]. Thus, a committee, the WfMC, is working on standards for workflow interoperability [21–23]. The WfMC has focused on developing a variety of interoperable scenarios that can operate at a number of levels from simple task passing to full workflow interoperability.

However, the real issue is not to connect systems but to develop fundamentally new concepts and architectures to support inter-organizational workflow. When developing a supply chain management system for a big motorcycle corporation in China, we developed an inter-enterprise workflow architecture that used the Internet. The main part of the architecture was a workflow-supported inner supply chain system and an integrated interface.

## 3. A case study

## 3.1. The background

Nanjing Jin Cheng Motorcycle Corporation Ltd. is among the top five motorcycle corporations in China. It has about 50 major suppliers. Under the support of the China Super Science and Technology Plan, 863/ CIMS, the corporation planned to carry out supply chain management. It aimed at improving business processing efficiency by integrating its business processes with those of its suppliers as well as sharing and exchanging information smoothly and quickly.

In order to carry out the cross-enterprise processes over the Internet, every independent enterprise had an inner IS. However, it was shown in the requirement analysis that there was neither an efficient integrated management system in the corporation nor in most of its suppliers [25]. Thus, we decided to develop a common integrated WSCM system so that the corporation and its suppliers could manage their inner processes. It was built on an MS SQL Server, WWW

![](/api/attachments/HQZMCW5Z/fulltext/images/0c3a91a4f39f98073c903d301bf94d40077315cf3085bf96c0dec4da3827600f.jpg)  
Fig. 1. The architecture of the supply chain management system.

Server, and browser. An independent integrated interface was also developed, this was integrated seamlessly with the WSCM system and provided information exchange between the system of the corporation and those of its suppliers. Fig. 1 illustrates the architecture of the entire SCM system, in which the manufacturer is the Nanjing Jin Cheng Motorcycle Corporation. Through the internet, the systems ofthecorporation, itscustomers and suppliers were integrated. For the suppliers that did not have inner information systems (IS), the WSCM and the integrated interface were provided. For the suppliers who had their own inner information systems, our major purpose was to provide the integrated interface and encapsulate their legacy systems (the original IS) to allow smooth and seamless communication with the integrated interface.

## 3.2. The workflow-supported inner supply chain management system

## 3.2.1. The architecture of WSCM

The architecture of WSCM is shown in Fig. 2. It consists of a set of business function agents, a workflow process definition tool (the SCM configuration tool), a lightweight workflow engine, and an independent integrated interface.

The set of business function agents deal with: out sourcing, production planning, sales, customer service, inventory, etc. Each agent is an autonomic and independent entity [11]. Each is now briefly discussed.

3.2.1.1. Outsourcing agent. This is an important component whose function is to outsource materials from suppliers according to the instruction from the product planning agent. It can actively adjust its working rhythm and processing contents according to changes in the environment. Different orders can be processed differently and automatically.

![](/api/attachments/HQZMCW5Z/fulltext/images/18c6650f222bc8f80b8ad721560e551574105f02d7b38147d4c09fae9b67f125.jpg)  
Fig. 2. A workflow supported inner supply chain management systems.

3.2.1.2. Inventory agent. This is also important as it manages the raw materials, semi-manufactured goods, and products in the warehouse. Its main functions are: managing and analyzing the movement of different materials from suppliers and sellers, balancing and optimizing multi-inventory management, tracking the material position, etc.

3.2.1.3. Sales agent. This does businesses with customers and provides a sales plan based on dynamic feedbackofthestatusofthesales.Italsoprovidesgeneral functions, such as analyzing and answering inquiries about the sales history or of customers.

3.2.1.4. Production planning agent. This can provide master production planning and cooperation in the planning process. It can also track and dynamically adjust the master production planning.

3.2.1.5. Customer service agent. This provides general functions, such as the statistics, management, indexing, and retrieving of customer information. It also provides some call-center services.

The independence and autonomy of an agent is very important to the software reconfiguration. However, it can do nothing if it does not cooperate with other agents. Ontology is the knowledge expressing concepts and criterions in a given domain. We applied ontology to describe the environment of agent execution. A set of agents can thus cooperate to complete a complex task in a specified domain.

A general graphical workflow modeling tool was provided. Its main interface and one ontology definition interface are shown in Figs. 3 and 4. Using the tool, we can define ontology, roles, persons, activities, enterprise policy rules, business processes, etc. If implemented in a different enterprise, the system can be reconfigured without modifying any code by editing and adjusting the ontology and policy rules according to the requirements of that enterprise. This allows fast SCM reconfiguration.

A lightweight workflow engine was constructed on MS SQL Server 6.5 and some COM components were written in visual basic or visual Cþþ. All the workflow related data were stored in the RDBMS, including: activities, roles, people, resources, business processes, ontology, etc. The reason we call this a lightweight workflow engine is that it only has the elementary workflow functions, such as scheduling, monitoring, etc. It is not as strong as needed in a workflow engine for commercial workflow management systems.

The enterprise business data were also stored in the MS SQL Server 6.5 database, which can be accessed by the lightweight workflow engine, integrated interface, and the business function agents.

## 3.2.2. The implementation of the light weight workflow engine

The workflow enactment software interprets the process definition and controls the instantiation of processes, sequencing of activities, adding work items to user work lists and invoking application tools. It is done through one or more co-operating workflow management engines, which manage the execution of individual instances of the various processes. In our system, it was set up as a centralized system with a single workflow engine responsible for managing all process instance executions.

![](/api/attachments/HQZMCW5Z/fulltext/images/b0e527025dbf80281d8ef8e3cd938d80ca77b5e9a5df7d7cc59bc4db8284e60a.jpg)  
Fig. 3. The main interface of the graphical workflow definition tool.

Event-condition-action (ECA) rules have been advocated by database practitioners as a powerful mechanism to transform passive data repositories into active ones. The rules make the data repositories react to internal or external events and trigger a chain of activities that include notifying users and applications or performing database updates [5]. An ECA rule has the following form

Rule (rule\_name)

ON event\_name

WITH condition\_exepression

DO actionSet

EndRule

![](/api/attachments/HQZMCW5Z/fulltext/images/959002e4889069f6d9ada9f80a4002ec11a0e936d3f2549d240aeda9862c1761.jpg)  
Fig. 4. Ontology defining interface.

![](/api/attachments/HQZMCW5Z/fulltext/images/b9eb9cb56a67dd52725be28c0a37a962b91b9dd7276c6feeabcae7694d488d9b.jpg)  
Fig. 5. Architecture of workflow engine.

Thus, when a simple or composite event occurs, if the condition expression holds a set of actions or operations are executed.

An ECA rule-based system can support ad-hoc, adaptive, flexible, and dynamic workflows that are modifiable at run-time. This allows the system designer to modify workflows as and when the requirements change. The ECA rules are often applied to control the execution sequence of activities in workflow engines. In our system, we also use ECA rules as the internal control logic for activities. Fig. 5 shows the architecture of the workflow engine, which consists of a set of management modules and data models. The management modules consist of a workflow instance management module (WIMM), a model interpreter (MI), an event management module (EMM), an activity state management module (ASMM), a data management module (DMM), etc.

The workflow model involves the process definition stored in the database. This will be instantiated by the WIMM under certain conditions. The process instance (workflow instance) model, workflow control data, and relevant data are also stored and kept by the MS SQL Server. Fig. 6 shows the relationships between them; the process instance, activity information, routing rule, activity role, activity person, and activity resource tables constitute the workflow instance data model. The control data is stored both in the event history table and in the tables of workflow instance data model (e.g. state of process instance and activity instances are stored in the process instance and activity information table separately). The workflow relevant data is stored in an independent table. In these, ProcessID identifies the process definition (workflow model) and CaseID distinguishes the process instances, which are instantiated from the same process definition. The ECA rules stored in the routing rule table are used to control the execution sequence of activities in a process instance. All the events are stored in the event history table. For brevity, we only give out the important fields of the tables.

The MI is the core of the workflow engine. It will be launched whenever a timer event, triggered by the internal clock, occurs. In our system, the timer was set to 2 min, i.e. the MI runs every 2 min. The EMM, ASMM, WIMM, and DMM are all COM components which provide functions to be called by the MI or external applications. For example, the built-in function, ST(act<sub>i</sub>), provided by the WIMM will finish the following tasks:

(1) it generates a Start(act<sub>i</sub>) event and stores it into the event history table;

(2) it generates a work item for a certain user; and

(3) it changes the state of act<sub>i</sub> into Ready.

The MI works as follows.

![](/api/attachments/HQZMCW5Z/fulltext/images/eedbe22b35b0377cc23066131d2a6202989157a21a15554c4a3d39349f4eb8cf.jpg)  
Fig. 6. Workflow instance, control and relevant data model.

Step 1. The MI monitors the event history table, when there are new events taking place, either inside or outside the engine, by calling functions provided by the EMM.

Step 2. If some new events occur, it will call the function provided by the WIMM to substitute the logic value, True for the corresponding events in event fields of the routing rule table and mark these events as having been used in the event history table.

Step 3. Then it determines whether the ECA rules, which have just been substituted, hold or not. When an ECA rule holds, i.e. both the ON and WITH field are computable and have the logic value True the action set in the DO field will be executed. Some of the actions may be built-in functions that generate and store events in the event history table or change the state of the process or activity instance, while others may be those that modify workflow relevant data and call external applications to have some work done outside the engine.

## 3.3. The implementation of the integrated interface

The integrated interface has the same structure both in the Jin Cheng corporation and its suppliers. Fig. 7 illustrates the integrated interfaces in the corporation and one of its suppliers. It consists of a web server, a message handling agent, a set of software components, etc. The web server is the portal to the outside world, through this, outside enterprises or customers can call the services provided by the inner information system (WSCM).

![](/api/attachments/HQZMCW5Z/fulltext/images/9a20066671fd59d029ecb8888d7975d05ac94e6d69e9c1b29b1d9aa5e38ccdbd.jpg)  
Fig. 7. The integrated interfaces and the information exchange between enterprises.

Table 1  
Part of the agreement between the manufacturer and its suppliers

<table><tr><td>ID</td><td>Service name</td><td>Service entry point</td><td>Service parameter</td><td>Role</td><td>Security requirement</td><td>Audit</td><td>Version</td><td>Response requirement</td></tr><tr><td>1</td><td>OrderCreation-Request</td><td>http://.../OrderCreation.asp</td><td>Order document</td><td>Purchaser</td><td>Encrypted and signed</td><td>Yes</td><td>1.0</td><td>Yes</td></tr><tr><td>2</td><td>OrderCancel</td><td>http://.../OrderCancel.asp</td><td>OrderId</td><td>Purchaser</td><td>Encrypted and signed</td><td>Yes</td><td>1.0</td><td>Yes</td></tr><tr><td>3</td><td>CatalogSearch</td><td>http://.../CatalogSearch.asp</td><td>Cataloglist</td><td>Everyone</td><td></td><td>No</td><td>1.0</td><td>Yes</td></tr><tr><td>n</td><td>Notification-payment</td><td>http://.../NotifyPayment.asp</td><td>OrderId, fee</td><td>Accountant</td><td>Encrypted and signed</td><td>No</td><td>1.0</td><td>No</td></tr></table>

Outside applications access ASP pages directly and they call special COM components to access the database directly or to communicate with the inner IS. The message handler agent is middleware, responsible for message transformation and message transfer between the cooperating enterprises. For example, the inner information system first sends a service request to the message handler agent. This then transforms the service request into a standard message format based on XML according to the agreement between the two enterprises. Finally, the message handler agent sends the transformed message to the service provider. The agent has to be able to store the transformed message, if the service provider is inaccessible. And if the service provider is accessible, the stored message will be sent out immediately. In our system, the service provider to the message handler agent was the web server, so the message handler agent had to use HTTP to transfer messages. For reason of safety and security, both enterprises set up a firewall.

The agreement between enterprises consisted of the ontology mapping between cooperating enterprises, the authorization and authentication information, etc. [6,13]. Table 1 shows a part of the agreement between the manufacturer and its suppliers. The security requirement field specified whether the data exchanged needed to be encrypted, signed, or not. The participant with the capacity to call this service is specified in the role field.

The exchanged messages are encoded in XML, because it is a simple, structured, extensible, and widely accepted meta-language that is easily readable, both by human and by machine [16]. Fig. 8 gives part of the exchanged messages (order creation request) between enterprises.

Through this integrated interface, both synchronous and asynchronous communication can be carried out. As shown by the dotted lines in Fig. 7, synchronous communication is achieved through the direct response from the web server (e.g. catalog searching on the web). Asynchronous communication is carried out through the message handler agent (e.g. the manufacturer requests a service provided by the supplier through the web server, then the supplier inner IS completes this service and a message containing the result is sent back to the requester by the message handler agent). The requester must include its callback URL in the request message so that the return message can be sent back correctly.

The application of a web server in the integrated interface makes it possible for the exchanged messages to be transferred between the browser in one enterprise and the web server in the integrated interface of another enterprise. This makes the information exchange between enterprises both flexible and convenient.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE "OrderCreateRequest.dtd">
    <MessageContent>
    <Sale HasCustomer="True" HasItems="True" HasPayment="False" HasShipping="True" HasSummary="True" HasSignature="False">
    <Customer PKId="0" Alias=""" Password=""" CustomerName=""" Email=""" Address=""" Country=""" PhoneNumber=""" Fax=""" LastSale=""" TotalSaleYTD="0.00" />
    <Shipping Address=""" ChkAddress=""" />
    <Summary SubTotal="0.00" Tax="0.00" Shipping="0.00" Total="0.00" />
    <ShoppingCart>
    <Item ItemId="0" Title=""" OriginalUnitPrice="0.00" PromotionUnitPrice="0.00" Qty="0"/>
    ...
    </ShoppingCart>
    <SendSignature>...</SendSignature>
    </Sale>
</MessageContent>
```  
Fig. 8. Part content of the order creation request message.

![](/api/attachments/HQZMCW5Z/fulltext/images/a3fa6756f0f9ea7144a67dd8e55d8daeb87da262623b68e57efc818d0291ccec.jpg)  
Fig. 9. The state chart representation of an inter-enterprise business process.

## 3.4. An example of inter-enterprise business processes

Fig. 9 illustrates inter-enterprise business processes occurring in the supply chain: how the manufacturer, Jin Cheng Motorcycle Corporation, does business with one of its suppliers. S and E are dummy activities that represent the start and end of the process, respectively. The arrowed edge represents the execution direction. The labels, Ri, I ¼ 1, 2, 3, . . ., on the arrowed edge label the corresponding ECA rules which are used to control the route of activities. Tables 2 and 3 show the ECA rules marked in the figure for the manufacturer and the supplier separately. This process proceeds as follows.

1. After the sales department accepts an order from a customer, a ‘‘charge’’ activity is initiated to wait for payment from the customer.

2. When the payment covering the total cost of the order is received (e.g. the electronic bank informs the financial agent of e-payment from the customer), the ‘‘query inventory’’ activity is activated to check that the inventory level is enough to satisfy the order.

(a) If it is, the inventory agent adjusts the inventory level and the ‘‘deliver goods’’ activity is initiated.

(b) If not, the ‘‘manufacture plan’’ activity is activated to compute if there is enough material to produce goods for the order according to the associated bill of materials (BOM) and the inventory levels.

(i) When there is enough material, a manufacturing plan is made by the product plan agent. Then the ‘‘manufacture’’ activity is activated.

(ii) If there is not enough material, a list of materials shortage is generated and sent to the outsourcing agent, and an ‘‘outsource’’ activity is initiated, as shown. After the materials purchased from the supplier come, the ‘‘manufacture’’ activity is activated.

Table 2  
Routing ECA rules in the manufacturer

<table><tr><td>R1</td><td>ON End(Sales)DO ST(Charge)</td><td>R2</td><td>ON End(Sales) AND End(Charge)WITH Order.Payment &gt;= Order.TotalPriceDO ST(QueryInventory)</td></tr><tr><td>R3</td><td>ON End(QueryInventory)WITH IsGoodsEnoughDO ST(DeliverGoods)</td><td>R4</td><td>ON End(QueryInventory)WITH Not IsGoodsEnoughDo ST(ManufacturePlan)</td></tr><tr><td>R5</td><td>ON End(ManufacturePlan)WITH IsMaterialsEnoughDo ST(Manufacture)</td><td>R6</td><td>ON End(ManufacturePlan)WITH Not IsMaterialsEnoughDo ST(Outsource)</td></tr><tr><td>R7</td><td>ON End(Outsource)WITH ArrivedMaterialsDO ST(Manufacture)</td><td>R8</td><td>ON End(Manufacture)DO ST(DeliverGoods)</td></tr><tr><td>R9</td><td>ON Start(Outsource)DO ST(OutsourcePlan)</td><td>R10</td><td>ON End(MakeOutsourcePlan)DO ST(SendOrder)</td></tr><tr><td>R11</td><td>ON End(Purchase)WITH OrderAcceptedDO Payment(Order)</td><td>R12</td><td>ON End(Payment) AND Arrived(Materials)DO ST(CheckMaterial)</td></tr><tr><td>R13</td><td>ON End(CheckMaterial)WITH Not NoProblemDO ST(Exception)</td><td>R14</td><td>ON End(CheckMaterial)WITH NoProblemDO EndProcess()</td></tr></table>

ST(),EndProcess() are built-in functions of the workflow engine, which denote the action of starting an activity and terminating the process, respectively.

3. When the products for the order have been produced, the ‘‘deliver goods’’ activity is initiated to ship goods to the customer.

4. After the goods are delivered to the customer, the whole process is completed.

Outsourcing is a sub-process which consists of cooperation with its supplier systems. It has the following steps

(1) making outsourcing plan;

(2) send an order to the supplier;

(3) when the supplier receives the order, the auditor will check it. If acceptable, the supplier will send an order acceptance message back to the manufacturer and tell its financial department to arrange for payment;

(4) when the outsourcing agent of the manufacturer receives the order acceptance message, it will pay for the order and initiate the ‘‘check material’ activity to wait for the goods;

(5) as long as the supplier receives the payment, the order will be processed;

(6) after the order is finished, the goods will be delivered;

Table 3  
Routing ECA rules in the supplier

<table><tr><td>R1</td><td>ON Receiver(Order)DO InitProcess(Order);ST(Audit)</td><td>R2</td><td>ON End(Audit)DO ST(SendAcceptance)</td></tr><tr><td>R3</td><td>ON End(SendAcceptance)DO ST(Charge)</td><td>R4</td><td>ON End(Charge)WITH Order.Payment $\geq$ (Order.TotalPrice/2)DO ST(QueryInventory)</td></tr></table>

ST(),InitProcess() are built-in functions of the workflow engine, which denote the action of starting an activity and initiating a process, respectively.

![](/api/attachments/HQZMCW5Z/fulltext/images/61d6ecd95e92fae0a1e7a8d64b0597cef96c5c7c233f0da661d766b645476eb0.jpg)  
Fig. 10. The adjusted outsourcing business process.

(7) the goods will be checked. If it is ok, then the outsourcing sub-process is completed, otherwise an exception will occur.

This is a typical business process between enterprises and the flow is controlled by the ECA rules in Tables 2 and 3. With the support of our system, it is convenient to adjust the business process according to different requirements. For example, because Jin Cheng has a high reputation with its long-term suppliers, some can deliver goods first and then charge for them, rather than delivering after payment. Thus the outsourcing sub-process must be adjusted. Fig. 10 shows this modified process (for brevity, only the outsourcing sub-process is given). It can be easily adjusted by modifying some of the ECA rules and no code needs to be modified. Table 4 shows the modifications of the corresponding ECA rules both for the manufacturer and the supplier. For the manufacturer, rules R11, R12, and R14 are modified, while for the supplier it is rules R3 and R4.

## 3.5. Advantages of the system

The relationship principles are supported as follows

\- Goal orientation: The inter-enterprise workflow model is based on a nested sub-processes model. In this, the originating process instance starts a subprocess in a workflow enactment service and waits for a return message during its execution. The originating process chooses the sub-process according to its goal, requiring only the sub-process to fulfill this goal and return results.

\- Privacy: There is an agreement between the enterprises that represents the service constraint information. If an enterprise requests services beyond the agreement, the partners can ignore them.

Table 4 Modified ECA rules in the manufacturer and in the supplier

<table><tr><td colspan="4">Modified ECA rules in the manufacturer and in the supplier</td></tr><tr><td colspan="4">Modified ECA rules in the manufacturer</td></tr><tr><td rowspan="3">R11</td><td>ON End(SendOrder)</td><td>R12</td><td>ON End(CheckMaterial)</td></tr><tr><td>DO ST(CheckMaterial)</td><td></td><td>WITH NoProblem</td></tr><tr><td></td><td></td><td>DO ST(Payment)</td></tr><tr><td rowspan="2">R14</td><td>ON End(Payment)</td><td></td><td></td></tr><tr><td>DO EndProcess()</td><td></td><td></td></tr><tr><td colspan="4">Modified ECA rules in the supplier</td></tr><tr><td rowspan="2">R3</td><td>ON End(SendAcceptance)</td><td>R4</td><td>ON End(DeliverGoods)</td></tr><tr><td>DO ST(QueryInventory)</td><td></td><td>DO ST(Charge)</td></tr></table>

Through this agreement, we can create a firewall between the enterprises, that makes only authorized users able to access authorized data. Therefore, it protects the privacy of both enterprises.

\- Flexibility: During to the separation of the organization model from the process model in the workflow, re-engineering of the business processes within an organization is convenient. The use of standard interfaces to connect enterprises can diminish any change effects between cooperating partners. Also it is easy to adjust the business process by changing the enterprise policy rules. Therefore, the system is flexible.

\- Independence: The implementation of goal orientation, privacy, and flexibility has shown that the system is independent. For instance, the processes in one organization will not be affected by internal changes to the process in the other.

## 4. Success and lessons

## 4.1. Success

SCM system is an enabling technology for virtual enterprises. The implementation of a system in the corporation has provided an example for improving cooperation between enterprises and for changing the manufacturing mode. It also promotes full-scale management and enhances the economical efficiency and effectiveness of the corporation. The benefits are as follows.

\- The Implementation of the system enhanced the corporation’s ability to respond rapidly to the everchanging market. With the system, order data and service information of the suppliers and distributors can be returned to the corporation within a day. Different departments within the corporation can share statistical data and some of the original information can be searched over the net in real time level. With such accurate data, the corporation can make more precise outsourcing and manufacture plans.

\- It enhanced the stability and operability of the manufacturing plan. For example, the rate of shortage of raw materials has been decreased by 10%. It also allows the planner to determine a lack of resources. These results have increased the corporation income by about US\$ 800,000 per year.

\- The inventory can be kept at a very low level. Due to the accurate and timely information, the manufacturer can reasonably and effectively control the inventory level using inventory control theory and methods. The inventory level of raw materials, parts, semi-manufactured goods, and finished goods has been diminished by about 25%.

\- The average life-cycle of products in the warehouse has been lowered by about 15% and that of parts and semi-manufactured goods has been lowered by about 10%.

\- The information flow in the supply chain has been speeded significantly. Moreover, the effort to maintain the information flow, has been significantly reduced.

\- The use of working capital in the enterprise has been improved. Outsourcing occupied about US\$ 250 million per year, of which the capital used in material storage was about 10%. Thus the material storage spending was decreased by about US\$ 2.5 million.

There have also been indirect results. For example, the implementation of the system has standardized the relationship between upstream enterprises and downstream enterprises. Five unified goals has been reached in this corporation, resulting in consolidation of: (1) quality control standards; (2) development and manufacturing plan; (3) knowledge property protection methods; (4) competing strategies; and (5) product price policies. It also improved the cooperation between different teams and promoted a unified enterprise culture. Lastly, the rapid response to market requirements gained from the system has increased the influence of the corporation’ products as seen by normal consumers and made the corporation better know in the country.

## 4.2. Lessons learned

Some key success factors were achieved by efforts of some units. However, some lessons can be concluded as follows.

\- Support from the National Super Science and Technology Plan 863/CIMS and local government. The 863/CIMS plan paid most of the cost of the development and implementation of the system. The local government also paid some cost.

\- Strong support from top management. On the one hand, the general manager gave necessary resources to develop and test the new system, on the other hand, the general manager gave the project team strong power to deploy the system. Sometimes, he participated in meetings to solve management problems and kept the system implementation going smoothly and efficiently.

\- Good cooperation and negotiation with suppliers and retailers: The distributors were mostly controlled by the enterprise. Thus, it was easy to implement the system. However, the suppliers and retailers were independent. They had their own goals, management methods, and systems. For example, some suppliers did not want to use the system, because they did not want to spend money on a new IS. The enterprise helped those suppliers and if they still did not want to use the system, a method such as changing suppliers was implemented. Free-of-charge customer training was an aid to the success of the system.

\- The use of open and standard hardware and soft ware systems as well as standard e-business specifications. This made the interface easier to integrate: the most difficult work was in integrating the legacy systems of Jin Chen and its suppliers.

\- Finally, the system should be flexible, so that it can be adapted to different suppliers’ requirements.

## 5. Conclusion

SCM focuses on implementation of interoperability between independent enterprises and deployment of business processes over multiple enterprises. Here, a SCM system supported by inter-enterprise workflow architecture was discussed. This architecture of the system consisted of a workflow-supported inner supply chain system and an integrated interface. The inner workflow-supported supply chain management system was used to define and control the execution of business processes within the enterprise. Through the integrated interface, the whole supply chain system across several independent enterprises was implemented and the information exchange was fulfilled.

There are, however, several problems with our current system.

1. Integration is based on database sharing by encapsulation; thus some integrity and safety features are not well kept and the inner system becomes tightly-coupled. This may lead to conflicts between sub-systems. Nevertheless, the idea of enterprises application integration (EDI) in BizTalk may provide a way to solve such problems [12].

2. Different suppliers have different ontologies, and mapping between them is not easy [19]. This means that a word-for-word mapping is not available in ontology translation.

3. Rapid change of business process, and the dynamic, uncertain and error-prone work environment require the addition of an adaptive workflow system [10].

## Acknowledgements

The authors thank the Chairman of the Editorial Board and the anonymous referees for their helpful comments on the earlier version of this paper, which has improved the quality of the paper. This work was supported by China Super Science and Technology Plan 863/CIMS under the grant No: 2001AA415310, 2002AA411420, Hunan provincial plan for Manufacture Information Engineering under the grand No.: Hnmie-A-051, and Hunan Provincial NSFC under the grant No: 03JJY6024.

## References

[1] G. Avigdor, M. Danilo, Inter-Enterprise Workflow Management Systems, in: Proceedings of the 10th International Workshop on Database and Expert Systems Applications, 1999, pp. 623–627.

[2] J. Bowersox, J. Calantone, Logistics paradigms: the impact of information technology, Journal of Business Logistics 16 (1), 1995, pp. 65–68.

[3] S. Changchien, H.Y. Shen, Supply chain reengineering using a core process analysis matrix and object-oriented simulation, Information and Management 39 (5), 2002, pp. 345–358.

[4] G. Dimitrios, S. Hans, C. Andrzej et al., Managing process and service fusion in virtual enterprises, Information System 24 (6), 1999, pp. 429–456.

[5] A. Goh, Y.-K. Koh, D.S. Domazet, ECA rule-based support for workflows, Artificial Intelligence in Engineering 15, 2001, pp. 37–46.

[6] W. Hans, W.J. van den Heuvel, Cross-organizational workflow integration using contracts, Decision Support Systems 33, 2002, pp. 247–265.

[7] L. Heiko, W. Keith, Virtual enterprise coordinator—agreement-driven gateways for cross-organizational workflow management, in Proceedings of the international joint conference on Work activities coordination and collaboration, 1999, pp. 29–38.

[8] M. Kradolfer, A Workflow Metamodel Supporting Dynamic, Reuse-based Model Evolution, Ph.D. Thesis, Department of Information Technology, University of Zurich, Switzerland, 2000, May, 2000. http://www.ifi.unizh.ch/ifiadmin/staff/ro frei/Dissertationen/Jahr\_2000/thesis\_kradolfer.pdf, 2000.

[9] R. Levary, Better supply chains through information technology, Industrial Management 42 (3), 2000, pp. 24–30.

[10] K. Mark, D. Chrysanthos, B. Abraham, Introduction to the Special Issue on Adaptive Workflow Systems, Computer Supported Cooperative Work. No. 9, 2000, 265–267.

[11] W. Michael, N.R. Jennings, Intelligent agents: theory and practice, The knowledge Engineering Review 10 (2), 1995, pp. 115–152.

[12] Microsoft Corporation, Legacy File Integration Using Microsoft BizTalk Server 2000 White Paper, http://www.microsoft.com/biztalk/techinfo/development/2000/wp\_legacyFileIntegration.doc, 2000.

[13] A. Mike, A. Rob, Workflow Interoperability-Enabling E-Commerce, http://www.wfmc.org/standards/docs, 1999.

[14] K. Patterson, C. Grimm, T. Corsi, Adopting new technologies for supply chain management, Transportation Research Part E: Logistics and Transportation Review 39 (2), 2003, pp. 95–121.

[15] D. Phan, E-business development for competitive advantages: a case study, Information and Management 40 (6), 2003, pp. 581–590.

[16] J. Robert, M. Jay, M. Bart, An XML framework for agentbased E-commerce, Communications of the ACM 42 (3), 1999, pp. 106–114.

[17] W.M.P. Van der Aalst, Process-oriented architectures for electronic commerce and interorganizational workflow, Information Systems 24 (8), 1999, pp. 639–671.

[18] W.M.P. Van der Aalst, Loosely coupled interorganizational workflows: modeling and analyzing workflows crossing organizational boundaries, Information and Management 37, 2000, pp. 67–75.

[19] Y.L. Wang, S.S. Zhang, Software reconfiguration through ontology mapping, Chinese Journal of Computers 24 (70), 2001, pp. 776–783 (in Chinese).

[20] WfMC, Workflow Management Coalition. Workflow Refer ence Model. http://www.wfmc.org/standards/docs, Jan 1995.

[21] WfMC, Workflow Management Coalition. Workflow Standard—Interoperability: Abstract Specification. http://www. wfmc.org/standards/docs, 1996.

[22] WfMC, Workflow Management Coalition. Workflow Standard—Interoperability: Wf-XML Binding http://www.wfmc. org/standards/docs, 2000a.

[23] WfMC, Workflow Management Coalition. Workflow Standard—Interoperability: Internet e-mail MIME Binding http:// www.wfmc.org/standards/docs, 7 January 2000b.

[24] M. Whipple, R. Frankel, Strategic alliance success factors, The Journal of Supply Chain Management 36 (3), 2000, pp. 21–28.

[25] 863/CIMS, Agile Supply Chain Management System for Virtual Enterprises based on Re-configurable Technologies, Technical Report, Deptartment of Computer Science and Engineering, Shanghai Jiao Tong University, 2000, (in Chinese).

![](/api/attachments/HQZMCW5Z/fulltext/images/bd33536447402e64aa3ffb298adc816638e0b48872d360649058397e29d457b8.jpg)

Jianxun Liu was born in 1970, received his MS and PhD degree in computer science from Central South University of Technology in 1997 and Shanghai Jiao Tong University in 2003, respectively. He is now an associate professor and a vice dean of school of computer science and engineering, Hunan University of Science and Technology. His current interests include electronic commerce, workflow

management systems, agent and XML. He has published about 20 academic papers in technical journals, books, international journal and conference proceedings.

![](/api/attachments/HQZMCW5Z/fulltext/images/e89300c365f2855b9e929753a2052090ca23542aff065f2ef4de7db26ff887c1.jpg)

Shensheng Zhang is a professor in Computer Integrated Technology (CIT) Lab, Department of Computer Science and Engineering, Shanghai Jiao Tong University, PR China. He received a PhD degree in mechanical engineering from Stanford in 1988. His research interests are workflow, concurrent engineering, and agile supply chain. He has been in charge of many projects sup-

ported by High Technology Research and Development Program.

![](/api/attachments/HQZMCW5Z/fulltext/images/f1dcfb9f1292434403afa7a2e9da9fa01349e73df05b1e5503c3caf59b48793b.jpg)

Jinming Hu is a senior software architect at Kingdee Software Co. Ltd., one of biggest ERP vendors in China. He is also a part-time researcher at CIT Lab, Shanghai Jiao Tong University, China. He worked as a post-doctoral researcher at University of Twente, The Netherlands in 2001 and 2002. His research interests are in workflow management system, concurrent engineering and software en-

gineering. He received an MS in automatic control from Hunan Univeristy and a PhD in computer science from Shanghai Jiao Tong University. His email address is http://www.hujinmin@ yahoo.com.cn.
