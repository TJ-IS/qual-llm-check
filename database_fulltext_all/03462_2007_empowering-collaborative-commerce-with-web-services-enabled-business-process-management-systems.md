---
otero_id: 3462
otero_key: "A468SMMF"
title: "Empowering collaborative commerce with Web services enabled business process management systems"
authors: "Minder Chen; Dongsong Zhang; Lina Zhou"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.05.014"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Empowering collaborative commerce with Web services enabled business process management systems

Minder Chen<sup>a,\*</sup>, Dongsong Zhang<sup>b</sup>, Lina Zhou

<sup>a</sup>MSN-5F4, School of Management, George Mason University, Fairfax, VA 22030, USA

<sup>b</sup>Department of Information Systems, University of Maryland, Baltimore County, 1000 Hilltop Circle, Baltimore, MD 21250, USA

Available online 1 July 2005

## Abstract

Collaborative commerce (C-Commerce) is a set of technologies and business practices that allows companies to build stronger relationships with their trading partners through integrating complex and cross-enterprise processes governed by business logic and rules, as well as workflows. Business Process Management (BPM) is a key element of C-Commerce solutions for complex process coordination. It provides a mechanism to support e-businesses in modeling, deploying, and managing business processes that involve various applications with greater flexibility. Traditional BPM solutions often lack the capability to integrate external applications in that they have very limited support for interoperability. In recent years, Web services have emerged as a promising enabling technology for BPM in support of C-Commerce. Web services offer effective and standard-based means to improve interoperability among different software applications over Internet protocols This paper aims to give an in-depth analysis of BPM and Web services in the context of C-Commerce. We propose an architecture for Web services enabled BPM in C-Commerce and provide technical insights into why Web services can enhance business process coordination. Finally, an implementation of a dynamic e-procurement application based on the proposed architecture is presented. With the advent of Web service standards and business process integration tools that support them, BPM systems enabled by Web services are empowering the development of more flexible and dynamic C-Commerce.

<sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Collaborative commerce; Business process management; Web services; Enterprise application integration; Interoperability

## 1. Introduction

In the 21st century, companies are undergoing a shift towards tying their competitive advantages to a <sup>b</sup>dynamic ecosystem<sup>Q</sup> of business web with trading partners such as suppliers, distributors, agents, dealers, brokers, retailers, etc. Creating a collaborative network of trading partners to reduce costs, shorten business process cycle times and streamline workflow is critical to business competitiveness and growth. A survey of 300 business leaders by Deloitte Consulting in 2002 showed that using collaborative trading networks could boost business efficiency by more than 70%. Many companies are beginning to understand the importance of e-business collaboration and benefit from it, including increasing revenue, streamlining operational capabilities, and transforming their business networks fundamentally. For example, Cigna Corp. earmarked \$300 million of its \$800 million information technology (IT) budget in 2002 to provide onestop shopping and integrated customer service [21].

Collaborative commerce (C-Commerce) is a term that describes a fundamental shift in the way companies interact with each other. It <sup>b</sup>consists of crossenterprise capabilities that leverage new technologies to allow an enterprise to more effectively manage today’s complex partner ecosystem through improved sharing of business processes, decision-making, workflow, and data with key trading partners<sup>Q</sup> [14]. It includes the use of Internet technologies to integrate a company’s core business processes with those of its customers and suppliers [30]. Collaborative commerce enables companies to improve the way they manage their cross-enterprise value chains dramatically. The successful, seamless, and flexible integration of business processes and information systems of different companies provides a substantial competitive advantage to companies. Deloitte analysts predicted that by 2005, 85% of companies will have implemented some collaborative commerce initiatives [14].

With its ubiquitous availability, standard protocols, and loosely coupled infrastructure, the Internet has been recognized as an ideal technology platform for software-based business collaboration. For example, providing customers with real-time order status during the complex order fulfillment process is what many businesses strive to offer as an important value-added service to their customers. Fulfilling an order may require integration of several internal applications as well as complicated interaction and coordination with other enterprises. Using Web services is a promising approach to facilitating real-time and more automated C-Commerce that ultimately delivers services to the customer in an optimal and efficient manner.

This paper primarily focuses on the emerging use of Web services in conjunction with business process management (BPM) to support C-Commerce. It offers an in-depth analysis of the nature of BPM and Web services from both theoretical and technical perspectives. We propose an architecture for Web services enabled BPM in C-Commerce and provide technical insights into why Web services can enhance process integration and how to deploy Web services for process management in support of C-Commerce. The rest of the paper is organized as follows. In Section 2, we introduce the concept of C-Commerce and its benefits, as well as BPM in C-Commerce. Web services standards and the impact of Web services on process management in the context of e-business are discussed in Section 3. An architecture of Web services enabled business process management system is proposed in Section 4 based on the belief that BPM software will become a key element of agile C-Commerce applications [15]. A prototype application that uses Web services to support dynamic e-procurement process, an important C-Commerce application, is presented in Section 5. Via this service-oriented architecture, the e-procurement application can get access to real-time pricing and inventory information from a dynamic set of suppliers to make a speedy purchase decision on spot. A business process management system (BPMS) has been used to support the modeling and deployment of this complex procurement process. Finally, issues and challenges for developing Web services enabled BPM for C-Commerce are discussed in Section 6.

## 2. Collaborative commerce

Integration, automation, and collaboration are the keys to improving communication between trading partners regardless of their technological sophistication and IT infrastructure [31]. Integration ensures that all electronic transactions interface seamlessly with existing internal and external applications. Automation and collaboration functions enable trading partners to send and receive information, manage each phase of a critical business process, as well as request and consume services from other partners.

Beyond simple online buying and selling activities on the Web, electronic commerce needs efficient back-end operations supported by software systems that handle the transactional and analytical processing of business data. One way to think of these software systems is in terms of collaboration [24]. Enterprise Resource Planning (ERP) systems promote collaboration between key departments and functions to run core operational business processes. Supply Chain Management (SCM) systems aim to optimize collaboration with a company’s various suppliers. Customer Relationship Management (CRM) systems seek to enhance collaboration between a company and its customers. The emergence of business-to-business (B2B) exchanges and Web services has created new ways for business partners to work together by integrating their software systems.

## 2.1. The vision of C-Commerce

The ultimate objectives of C-Commerce initiatives are to maximize return on information technology investment, increase business agility and the quality of customer service, and enhance supply chain integration. By integrating applications using latest standards and open technologies, business partners are able to coordinate complex transactions, share latest information, collaborate on product planning, communicate product design ideas, and integrate their workflows. C-Commerce can help companies gain competitive advantages by (1) connecting and automating processes with their partners, customers, and suppliers, (2) reducing processing latencies, (3) developing new capabilities that improve service levels while reducing costs, and (4) making planning, design, and operational decisions dynamically based on real-time information.

In C-Commerce, in order to enable collaborative business processes, interactions must increase among all internal and external applications involved to achieve visibility of end-to-end processes. There are different levels of integration in C-Commerce, listed from low to high in the following: (1) exchanging data via traditional means such as fax, phone, and mail; (2) using EDI or email for point-to-point data interchange; (3) utilizing private or public exchanges to share business process information; and (4) deploying Web services and process management tools to coordinate loosely coupled services into integrated interenterprise processes with real-time data sharing [30]. A research study conducted in 2002 by NerveWire found that majority of companies only operated at low or moderate integration levels in C-Commerce [30].

Technologies for C-Commerce must support interoperability because trading partners often use diverse systems. Consequently, solutions for C-Commerce must be based on standards to support loose coupling, autonomy, and flexibility on the one hand, as well as ensure trust and security on the other hand. There are a few standards and related technologies that are considered specifically suitable for C-Commerce [42], including messaging standards such as SOAP for accessing software components in a distributed environment; common document specification languages such as XML and ebXML (Electronic Business XML) for data interchange; and business process specifications such as Business Process Modeling Language (BPML) for describing workflows. In this paper, we mainly focus on the use of Web services standards and technologies in support of business process management for C-Commerce.

## 2.2. Business process management in C-Commerce— no process integration, no collaboration

Process is the essence of every enterprise. If business applications are viewed as a complex set of processes, then process management can be envisioned as the key to developing flexible, scalable applications that businesses need in today’s dynamic and collaborative market [20]. Process management is traditionally an implicit component of other technology offerings, but it is a central focus of C-Commerce. BPM has evolved from a feature of workflow and related technologies to a powerful tool for providing strategic values. The function of BPM in collaborative commerce is to <sup>b</sup>develop a common framework to guide interactions among all parties [20].<sup>Q</sup>

Efficient process management is critical to C-Commerce. A study from IBM found that 85% of all ebusiness infrastructures involve some form of evolution and integration of existing systems, and 90% of IT budget is allocated to integration, software, and staffing [22]. The key challenges for building effective and efficient inter- and intra-enterprise applications to support business processes include (1) how to extract business functions from existing applications and expose them as services, and (2) how to compose new applications to support business processes via integrating those existing business services. Current C-Commerce solutions add an infrastructure layer to the e-business application stack. They need a framework that enables e-businesses to quickly model, deploy, and manage business processes. We have identified three categories of business process integration solutions: workflow management systems, Enterprise Software Systems (ESS) and Enterprise Application Integration (EAI), and Business-to-Business (B2B) integration servers. These solutions are reviewed here to provide insights on how they may be used for C-Commerce.

## 2.2.1. Workflow management systems

In the past decade, workflow has been an important technology in support of business processes that require document routing and intensive manual activities such as approving a purchase request [37]. According to the WfMC, workflow is <sup>b</sup>the automation of a business process, in whole or part, during which documents, information or tasks are passed from one participant to another for action, according to a set of procedural rules ([47], p. 9).<sup>Q</sup> A workflow management system (WfMS) defines, creates and manages the execution of workflows through the use of software that runs on one or more workflow engines. A WfMS can interpret the process definition, interact with workflow participants, and invoke the use of IT tools and applications if required [47]. It is designed to support business processes by coordinating and controlling the flow of work and information between participants based on explicitly defined business process models. The focus of WfMS has changed from routing documents among knowledge workers to improving business processes. Such a shift requires solutions addressing interoperability issues, which have been a major concern of the workflow user community.

Several XML-based information interchange standards such as Wf-XML and XML Process Definition Language (XPDL) have been developed to support integration of workflow systems. However, the integration of inter-organizational workflow sys tems is difficult due to limitations of current workflow management systems. For example, processes within a workflow system may not support adequate interoperability. Conducting B2B e-commerce activities requires a business to dynamically integrate complex services provided by different vendors over the Internet. These services are often implemented in different programming languages and platforms; therefore, it is difficult to integrate them using traditional workflow systems. The lack of widely adopted standards by workflow vendors also limits the reach of workflow systems and makes customers reluctant to invest in workflow products [37].

## 2.2.2. ESS and EAI products

In the late 1990s, ESS (Enterprise Software Systems) such as ERP and CRM systems were adopted due to their ability to integrate data and processes in different functional departments [11,35]. ERP systems are particularly built upon specific reference data models and process models such that they are limited to supporting business processes similar to their underlying reference models [23]. Therefore, ERP systems are described as <sup>b</sup>tightly coupled<sup>Q</sup> [18]. Some ERP implementations were costly due to extensive customization efforts and they were still inadequate to support agile business processes. EAI products have emerged as an attempt to integrate various ERP and CRM systems within an enterprise. Through building adapters as well as using message-oriented middleware or hub-and-spoke architectures, EAI products have made interactions among systems relatively easier to manage [33]. However, due to the lack of standards, customization efforts using EAI software can be costly. In addition, there is no notion of business process modeling in many existing EAI products. Forrester Research reported that the average cost of integration projects in 3500 global companies was \$6.3 million and less than 35% of these integration projects were completed on time and within the budget [4].

## 2.2.3. B2B integration servers

B2B e-commerce applications drive integration of a firm’s internal processes with external trading partners’ systems. BizTalk Server [29] is an example of such products. B2B servers focus on supporting exchange of EDI or XML-based documents between business partners; therefore, they often offer features to enhance security and messaging reliability. Usually a message handling process (often referred to as message pipeline) is used to work with adapters that are responsible for receiving and sending messages.

The above three categories of business process management solutions have converged in recent years due to the increasing demand of adaptive, agile, dynamic, and interoperable e-businesses [39]. One of the new driving forces for this convergence is the advent of Web services. Web services have become a standard solution to wrap and expose the functionality of legacy enterprise applications such that they can be integrated with other applications inside and outside an organization. An in-depth analysis of Web services and their impact on process management in the context of C-Commerce is given in the next section.

## 3. Web services for business process management in C-Commerce

Web services are <sup>b</sup>loosely coupled software components delivered over standard Internet protocols<sup>Q</sup> [41]. Web services provide a standard-based approach to implementing distributed components by offering data and business logic services over standards such as HTTP, XML, and SOAP [44] over the Internet. There are three players in a Web services architecture: the service provider, the service consumer, and service registry. Interactions among these players include the following operations: service publishing, discovery, binding, and invocation [6,8]. A Web service provider can publish a Web service defined by WSDL (Web Services Description Language) in a service registry such as a UDDI (Universal Description, Discovery, and Integration) registry. A Web service requester (consumer) can search and retrieve service description and the access point to a WSDL file from the service registry. The WSDL file is used to generate a client-side Web service proxy that is used by the service consumer to invoke the Web service by sending a SOAP message. SOAP enables communications between two programs that can be written in different programming languages and run on different platforms. IDC predicts that by 2007, Web services will be a US\$21 billion market and 80% of enterprises will have Web services applications in production mode.

## 3.1. The role of Web services in C-Commerce

Web services provide a very promising solution for process and application integration in C-Commerce. Web services specifications consist of a set of welldefined standards enabling plug-and-play flexibility and interoperability. As a result, every e-business application can interact with applications of external trading partners or other internal cross-functional applications by exchanging XML-based messages. For example, Amazon builds a stronger business relationship with its trading partners by putting Web services into practice. The free Amazon Web service program allows sellers to integrate Amazon.com ecommerce features directly into their own Web sites.

Web services can be invoked via either static or dynamic binding [48]. If interfaces of Web services of the same type of applications can be standardized, a client proxy stub can be generated statically and Web services clients can bind with different Web service ports in the client proxy dynamically. This is the most possible scenario in supporting dynamic Web services composition in B2B integration when Web services registries are involved during process execution.

## 3.2. A model of Web services supported C-Commerce

As discussed in previous sections, Web services technology facilitates integration of applications developed in a heterogeneous and distributed environment within a firm and/or across organization boundary. A business process can expose its functionality as Web services and consume the functionality of other processes provided by trading partners via Web services.

Fig. 1 illustrates the possible usage of Web services in C-Commerce. ESS products such as ERP, SCM, and CRM software packages are critical elements of collaborative e-business systems. In the past decade, many ESS products have become Web-enabled, i.e., users can use a Web browser to get access to ESS applications. However, ESS packages are still considered as monolithic systems in that they are very difficult and costly to implement. Recently, some ESS products are becoming Web services enabled. Many of their functions are exposed as Web services such that they can be easily integrated with other applications [16]. For example, SAP provides a capability to build Web services in its development programming language, ABAP, and offers Web services execution on SAP Web Application Server [34]. Many enterprise software vendors have offered their products with Web services interfaces in order to improve their interoperability. For example, Oracle’s CRM package exposes hundreds of its functions as Web services. Its goal is to reduce system integration efforts and consulting fees that often cost two to five times more than the license fees for these software [12].

![](/api/attachments/A468SMMF/fulltext/images/e6acd4b7029a9e86f4156d6fed5f014cf05420f2749f79f793e1b0d7731c62c6.jpg)  
Fig. 1. A model of web services supported C-Commerce.

Web services play an important role in enhancing business-to-consumer (B2C) and business-to-business (B2B) integration by allowing trading partners to gain access to data or business functions in the legacy systems and enterprise software systems either via Web services wrappers of these systems directly or via a BPMS (Business Process Management System). An enterprise can provide Web services to its trading partners for delivering real-time data or embed its business services directly as part of partners’ services to their customers. Activities in business processes can also be implemented as Web services. Business process models or workflows can be constructed to orchestrate Web services to support high-level business processes. Web services orchestration refers to composing multiple loosely coupled Web services from several service providers into a flow model, a direct graph in which activities are nodes connected by control links that determine the invocation sequence of activities within a business process [25]. A BPMS depicted in Fig. 1 is required to support the use of Web services in implementing business processes or managing workflows within and across enterprises. The BPMS will use private and public UDDI service registries to store, search, and select business partners’ Web services for business process integration. An architecture of BPMS empowered by Web services will be described in detail in the next section. Early adoption of Web services in B2B links applications among well-established business partners in a static fashion. Gradually, Web services will be used to support dynamic e-business consisting of dynamically configured business networks.

In C-Commerce, in addition to building interfaces of Web services for existing applications, there must also be a standard approach to connecting individual Web services together to form high-level business processes. A new layer of new Web services standards has been developed to address Web services composition and orchestration issues. These Web services standards related to business process integration include BPEL4WS (Business Process Execution Language for Web Services) [3], WSCI (Web Service Choreography Interface) [2], and BPML [1]. They all try to define a universal description language to specify how business processes are enacted and carried out in a precise manner.

BPEL4WS is a standard that is layered on top of several XML specifications: WSDL 1.1, XML Schema 1.0, and XPath 1.0. It is a specification that enables a task to be accomplished using the combination of Web services, possibly involving more than one company. BPEL4WS combines and replaces IBM’s Web Services Flow Language (WSFL) and Microsoft’s XLANG specification. It describes executable business processes that rely on the import and export of Web services, and provides a formal standard for specifying business processes and business interaction protocols. It aims to specify mutually visible message exchange behavior of each partner involved in the protocol without revealing its internal behaviors.

## 4. A Web services enabled BPMS architecture for C-Commerce

The emergence of Web services and related standards has had, and will continue to have, dramatic impact on the implementation and maintenance of collaborative processes and applications. C-Commerce initiatives based on Web services provide flexible, scalable IT infrastructures for cost-effective strategic collaboration with trading partners.

Fou [17] define three stages in the development of collaborative commerce. In the first stage (Webenabled C-Commerce), a single, Web-enabled business process allows external trading partners to access to its internal data. This is a very limited form of C-Commerce. Typical applications include displaying demand for production material and showing sales forecasts to suppliers. In the second stage (Web-integrated C-Commerce), e-business companies and trading partners are integrated through a Web portal. Thus, each enterprise can communicate and integrate with many trading partners in its supply chain through an e-marketplace mechanism. In the third and the most advanced stage (Web services enabled C-Commerce), Web services serve as a core mechanism to provide seamless and cost-effective process integration. The majority of interactions among companies involves highly integrated applications via real-time data sharing and process integration through Web services. A BPM mechanism is needed to support Web services enabled C-Commerce applications.

Based on BPM literature and evaluation of several commercial products [10,15,28,39,46], we developed a generic Web services enabled BPMS architecture for C-Commerce, which is shown in Fig. 2. It incorporates useful features of workflow management systems, EAI products, process modeling tools, and B2B servers. The architecture can be used to assist the evaluation of BPM products and to guide the development of Web services enabled C-Commerce initiatives. The architectural components of the proposed Web service enabled BPMS (WS-BPMS) are discussed as follows.

## 4.1. Process modeling tool

Business process modelers and developers can use process modeling tools to create business process models or templates. By explicitly representing a business process model based on a set of graphical notations, business users and managers can be more involved in the design of business processes.

## 4.2. Process management tools

There are three process management tools to help users manage instances of business processes throughout their life cycles: (a) The tool for process operation: End users who are directly involved in a business process may use this interactive tool to initiate a new instance of a business process or to change the status of a process instance by reviewing process information presented to them. Data associated with process instances are stored in databases or as XML files. When user inputs are required, documents will be routed to appropriate users. Users can use the tool to interact with Web services exposed by a business process; (b) The tool for process monitoring: It tracks the progress and status of process instances. Alerts can be automatically generated and sent to appropriate persons or application processes when certain situations occur; and (c) The tool for process performance measuring: This tool can produce reports for key performance indicators (PKI) with statistic analysis which can be used for continuous process management and improvement.

![](/api/attachments/A468SMMF/fulltext/images/ca6443e6ad22b2c740564ec2d46932d042de93ea207865dbb95b63f4719b5b82.jpg)  
Fig. 2. An architecture for web services enabled BPMS.

## 4.3. Business process execution engine

It carries out business processes according to process models and the status of process instances maintained by the BPMS. The engine analyzes all messages received by business processes and matches each message to an appropriate business process instance (e.g., message correlation). Message IDs may be needed for identification purpose. Under certain circumstances, the execution of business processes is guided by business rules. The execution engine often requires an application server to deploy and execute compiled business process models [10,28].

## 4.4. Business rule engine

It uses a variety of rules for real-time service selection and planning. In a C-Commerce environ ment, establishing and managing business services can be extremely burdensome due to the dynamic availability of large number of similar Web services with a variety of capabilities as well as changing customer requirements. Therefore, it is essential to generate service plans and to apply service selection policies dynamically in order to develop automated approaches for Web service composition and execution. Business policies and decision rules are explicitly defined in business process models. Several recent studies have explored various approaches based on WfSM or AI planning and execution technologies [5,40]. During process execution, the engine can interpret rules associated with an activity based on current status of a process instance to determine the routing of the process instance’s workflow at runtime.

## 4.5. Messaging services

In order to support long-running transactions, it is common to deploy a messaging service infrastructure to support asynchronous conversations [27]. A consumer (e.g., a process instance) of a Web service needs to provide a service provider with an endpoint reference for a callback service. A message correlation mechanism also needs to be established in order to associate a message from a callback operation with the original process instance that makes the initial request [36]. This service is often a built-in component of a BPMS. In C-Commerce, there are semi-structured messages in product design and development processes, as well as structured messages that are typical in operational and transaction-oriented processes.

## 4.6. Web services registry

A Web services registry (either private or public) stores meta-data about Web services published by enterprise applications or trading partners. It is used for discovery of Web services by other applications that need to consume Web services. The use of a Web service registry is critical for the development of dynamic inter-enterprise collaboration, enabling Web services to be selected and bound to a process instance during process execution.

With Web services emerging to support business processes as envisioned in our architecture, the proposed BPMS has the following capabilities that are similar to the ones suggested by Smith et al. [39]:

1. Deploy system integration technologies (messaging middleware, EAI, and B2B integration servers, etc.).

2. Integrate a workflow engine with application servers and middleware to drive technical agility to support process automation.

3. Combine automated activities of processes with human-centric workflow solutions.

4. Define process models explicitly to drive system development efforts and use business process management tools based on process models to manage business processes.

5. Accelerate application development, maintenance, and reuse.

Such a standard-based and service-oriented architecture avoids point-to-point proprietary connections and provides an e-business with technical agility to become a dynamic enterprise.

## 5. A case study: building a dynamic, Web services enabled e-procurement system

In this section, we present a simplified scenario of a dynamic e-procurement application implemented with Web services. It involves an ERP system, a business rule engine, a workflow component, a service registry, and Web services provided by suppliers handling price quotation and ordering. Issues in designing and implementing a prototype of the e-procurement application are also discussed in details.

## 5.1. The scenario of a dynamic e-procurement system

A dynamic e-procurement scenario described in this section is used to illustrate the need for using Web services composition in conjunction with business process management to support C-Commerce. In order to integrate various processes to support e-procurement, the composition of Web services is orchestrated according to an explicitly defined visual process model.

This e-procurement scenario described in Fig. 3 is modeled in UML (Unified Modeling Language) sequence diagram. In this diagram, a Web service is modeled as an object (i.e., an instance of a class). An invocation of a Web service operation is modeled as a message. Each Web operation is defined by the operation’s names, parameters, and the returned data type. An iteration control construct is represented with an asterisk (\*) before an operation signature. For example, a condition such as \*[For each qualified supplier] can be added in front of an operation’s name [19].

When the ERP system of ACME Inc. (a fictitious firm) receives a new order from a customer, it checks the warehouse inventory and realizes that the product ordered has to be replenished. It sends a purchase request to the Dynamic Purchase Process (DPP) via a reliable messaging mechanism. The purchase request contains the product ID and quantity requested. The DPP picks up the request from the message queue and creates a new purchase process instance.

![](/api/attachments/A468SMMF/fulltext/images/176ea9847e365c4d595caababf9579a51877bb60c94de3d8d588eebb59f8116a.jpg)  
Fig. 3. A UML sequence diagram for the use case scenario of e-procurement process integration.

The DDP is responsible for carrying out a sequence of activities and for coordinating activities performed by other applications as described in the following:

1. Finds out all qualified suppliers from a Web services registry. The interface to the registry is implemented in Web services. A query is sent to the registry via a Web service (i.e., QualifiedSuppliers) and a list of WSDL references provided by qualified suppliers who have implemented the Price-Quote Web service is returned.

2. Calls the PriceQuote Web service operation of each qualified supplier via asynchronous communication to get a quotation and possible product delivery date. The product ID and quantity to be ordered are specified in the service call.

3. The process will wait for a certain period of time (e.g., 24 h) for suppliers to send their quotations back. Each quotation message is sent back via a call-back function containing a unique RFQ<sup>\_</sup>ID which can be used to associate a quotation with a purchase process instance (i.e., message correlation).

4. All quotations will be sent to a Select Suppliers module that uses a set of predefined business rules to evaluate these offers in real-time and recommend which supplier has the best offer. The evaluation and recommendation are conducted based on the offered prices, delivery dates, supplier ratings, as well as priorities specified in the original purchase request. After receiving offers from multiple qualified suppliers, an overall fitness score will be calculated for each offer. Finally, the offer with the highest overall score will be selected and the user can proceed to place an order. Since the rules for selecting suppliers may change over time, they are specified declaratively and interpreted by the rule engine at run-time so that business analysts can easily update those rules without redeploying the application.

5. The purchase recommendation from the Select Suppliers module needs to be routed to appropriate purchasing personnel based on the product category, the amount and urgency of the purchase, and so on. The routing is done by an authorization workflow system that provides a purchase authorization form used by the designated purchasing personnel to make the final purchase authorization.

6. Once the recommended purchase order is approved, it is sent to the selected supplier via the TakeOrder Web service provided by the supplier. Once the order is received by the supplier and confirmed, it will be sent to the ERP system via a Web service as a response to the purchase request.

## 5.2. The implementation of the prototype

We used the beta version of Microsoft BizTalk Server 2004 to implement the process modeling and execution portion of the e-procurement prototype. This new version of BizTalk was chosen because it supports B2B and EAI integration and provides visual tools for process modeling and data mapping. The process model of the dynamic purchase process, depicted in Fig. 4, was created using the business process design tool in the BizTalk called Orchestration Designer. Interactions between a process and other external processes are defined by specifying send and receive activities for message exchange via ports specified at <sup>b</sup>Port Surface<sup>Q</sup>. A received message may activate a new business process instance or trigger a sequence of activities of an ongoing business process instance. A dynamic port binding feature should be selected while creating a Web port to consume a Web service. It allows the URL of a Web service to be assigned dynamically, an important feature for the dynamic selection of a supplier at run-time.

![](/api/attachments/A468SMMF/fulltext/images/0c31694f35bbdcf674a499128813da541461e13717d082966ee5188f61c94e96.jpg)  
Fig. 4. A visual model built in BizTalk for the purchase process.

When an implemented business process receives a message, it passes the message through a receive pipeline that decrypts, decodes, and disassembles the message, and transforms it into a format that BizTalk understands. Then, the message engine deposits the message and its metadata (context properties) into a MessageBox database. Message structures are defined in XML schema and transformation between messages is defined using the BizTalk’s Mapper tool.

Table 1 summarizes major business process design activities, the corresponding tools available in Biz-Talk, and the design artifacts (deliverables) produced from these activities.

One of the attractive features of Web services oriented architectures is the use of a service registry to support publishing, discovery, and dynamic binding of Web services. UDDI is a standard for implementing service registries. The public UDDI is too generic to be useful for the e-procurement application because currently there is no mechanism in UDDI to store product–supply relationships. Therefore, in this prototype system, a private Web services registry was implemented in a relational database to store product and supplier information, as well as Web services WSDL files of all participating suppliers. The registry played a key role in enabling the dynamic nature of the procurement process. The service discovery was performed through common SQL queries. A set of Web operations (i.e., methods of Web services) has been implemented to (1) allow other applications to interact with the registry, such as querying qualified suppliers for a product and retrieving WSDL references that suppliers have implemented, (2) send a request for price quotations and (3) place a purchase order. This registry and suppliers’ Web services were implemented using Visual Studio.NET. The Web services containing PriceQuote and TakeOrder operations were also implemented under .Net Framework. A Windows Server 2003 using IIS and .Net Framework SDK was used as an application server to support the deployment of Web services.

Operations of Web services that were developed to provide interfaces to the e-procurement Web service registry include the following:

1. GetSupplierWSDL (SupplierID, WebOperation): The WebOperations were a predefined set of operations implemented by all suppliers in the registry. For example, <sup>b</sup>PriceQuote<sup>Q</sup> operation allows a consumer to send a price quote request for a product and receive a quotation from a supplier. <sup>b</sup>TakeOrder<sup>Q</sup> is the operation allowing a consumer to order a product from a supplier via a Web service interface.

2. SetSupplierWSDL (SupplierID, WebOperation, WSDL): This method was used to add or update the WSDL entry of a supplier’s Web operation.

3. QualifiedSupplier (ProductID): An array of supplierIDs will be returned based on the ProductID.

Buyers and sellers in a supply chain need to work together to define a set of standard Web services operations with the same operation signatures (i.e., operation names, same number of parameters, and same data type for each parameter) and related message (document) standards to reduce unnecessary message transformation operations. This standardization effort is critical to the success of developing a dynamic and flexible e-procurement system, and resources and time should be allocated to ensure that all suppliers are informed of and have agreed to such standards.

Major business process design activities and tools support in BizTalk

<table><tr><td>Business process design activities</td><td>BizTalk tools</td><td>Design artifacts</td></tr><tr><td>Specify messages to be received or sent by the process</td><td>BizTalk Schema Editor</td><td>Message schema, specified in XML Schema [45], that defines the structure of documents or messages</td></tr><tr><td>Specify transformation logic (mappings) between messages</td><td>BizTalk Mapper</td><td>Schema maps stored as eXtensible Stylesheet Transformation (XSLT) files [43]</td></tr><tr><td>Specify process models</td><td>BizTalk Orchestration Designer</td><td>Business process model (orchestration)</td></tr><tr><td>Define Partners, PortType, and MessageLink</td><td>Partner Wizard PortType Configuration Wizard</td><td>Define the interfaces with other processes in term of: Who are they? How to bind with service interfaces of partners? What will be sent or received?</td></tr></table>

## 6. The adoption of Web services-enabled BPMS for C-Commerce in organizations

As Michael Dell put it, <sup>b</sup>We need to treat both suppliers and customers like partners and collaborators—together looking for ways to improve efficiency and value across the entire spectrum of the value chain, not just in our respective businesses.<sup>Q</sup> (Dell and Fredman [13])

The change of mindset from competition to collaboration is one of the major challenges for realizing C-Commerce. Recognizing the strategic importance of C-Commerce by the top management is critical for adopting WS-enabled BPMS. The costs and benefits of implementing Web services and deploying WS-BPMS affect organizations’ adoption decision. These are discussed in this section.

In general, Web services bring several distinct benefits to C-Commerce. First, they are much easier for developers to use than EDI and other traditional programming interfaces. Second, since Web services are developed based on a set of standards, they provide strong and cost-effective support for interoperability among heterogeneous systems. Third, the real gains may come from innovative C-Commerce applications developed and integrated using Web services. Those applications often provide better integration of internal business processes, offer better services to customers, and build strong links with suppliers. The end result is the creation of a distributed and dynamic electronic value chain that streamlines business processes within and across enterprises.

Web services enabled C-Commerce helps business trading partners to collaborate on product design, development, and production. Therefore, using Web services will reduce transaction costs, minimize unnecessary delays in companies’ business activities, as well as establish more integrated supply chains with collaborative planning, forecasting, and replenishment capability [17]. The wide adoption and ease of implementation of Web services will extend the reach and range of BPMS products from internal applications to trading partners’ systems.

Web services are an enabler to unleash the power of BPM technology by providing lowering integration costs, accelerating the time to market through shorter implementation cycles, and increasing the ability to adapt to the changing environment (e.g., through dynamic binding of processes) [32]. The use of WS-BPMS for C-Commerce not only enables developers to implement, test, modify, and re-implement processes faster and more cost-effectively, but also gets end users more involved in the design process to ensure alignment of information systems with business processes to increase the agility of enterprises [38]. Additional benefits obtained by applying WS-BPMS to C-Commerce include:

<sup>!</sup> Explicit process modeling helps business users and analysts capture and articulate business processes that may involve disparate applications. It allows business people to get involved in the design as well as management of business processes.

<sup>!</sup> Changes in C-Commerce rules and procedures can be quickly reflected in the process models. The execution of business processes based on process models ensures that information systems reflect the configuration of supply chains dynamically.

<sup>!</sup> WS-BPMS products support the integration of not only processes and data, but also people, to offer sufficient flexibility in managing business processes. They address the increasing need of integrating traditional human-centric workflows with automated applications.

There are several factors potentially affecting the cost of implementing and deploying WS-BPMS solutions for C-Commerce, thus influencing the adoption decision of an organization:

1. Modeling cost: There is cost associated with creating models for the current business processes and redesigning those processes when necessary. Since those process models will be used to generate executable code, they have to be defined at a very detailed level.

2. Web services development cost: Developers need to implement Web services wrappers for existing legacy systems to work with WS-BPMS or to build new Web services. Adding Web services wrappers without changing the internal code of legacy systems costs much less than replacing entire legacy systems.

3. Cost for purchasing WS-BPMS software: The cost of BPMS software products that have direct support for Web services integration is less than that of ESS products. For example, BizTalk 2004 Enterprise Edition is priced at \$24,999 per processor. The average initial software investment for an Oracle E-Business Suite deployment was \$1.7 million, with a median investment of \$550,000.

4. Cost for deploying IT infrastructures for Web services: The cost for deploying IT infrastructures for Web services should be considered separately from the cost of acquiring WS-BPMS products. IT infrastructures for Web services deployment require application servers such as WebSphere, or Windows Server 2003 that may have already been widely used in many organizations. Therefore, the cost for deploying Web services many not be a major factor [8].

5. Cost in developing C-Commerce standards: Working with trading partners to specify mutually agreed data interchange standards and application-level Web services operation standards are costs that need to be taken into consideration.

In summary, the cost should not be a major inhibitor for WS-BPMS adoption. There are some other issues related to the use of WS-BPMS for C-Commerce. Security is still a major concern in organizations’ decision about using WS-BPMS. The greater the reach of a business process, the more challenging it is because more efforts are required to ensure security and consistency in message structures and Web services interfaces [38]. Specific security standards for Web services are still lacking, which may complicate the implementation effort involving many trading partners. The lack of trust among trading partners may also prohibit them from giving others permissions to access their internal business data via Web services.

The implementation of WS-enabled BPMS to support C-Commerce can be done incrementally both from an architecture viewpoint and from an investment cost viewpoint. The incremental approach makes it easier for managers to commit resources to WS-BPMS. The advent of process management standards for Web services and the emergence of products in support of these standards will accelerate the adoption of Web services enabled business process management.

## 7. Conclusion

Collaborative commerce is beyond transactionbased B2C e-Commerce. Successful C-Commerce requires buyers and suppliers to engage in joint product development, demand forecasting, e-procurement, and other business processes. Common e-business standards such as XML and Web services are required to enable cross-enterprise information sharing and process integration.

In this paper, we have discussed the importance of business process management in C-Commerce and propose a Web services enabled BPMS architecture for C-Commerce. It is designed to provide a highlevel business process context for integrating applications both inside and outside enterprise boundaries in support of dynamic and agile business processes. However, the agility envisioned in new business process management environments does not come just because of the availability of new technologies. A proper development methodology is required to embrace the process- and service-oriented composition of business processes through Web services.

BPM is an approach that bridges a missing link between business process reengineering and ITenablers for reengineering processes [7,38]. It is beneficial for C-Commerce to use BPM technologies. With that being said, the current research and development efforts towards Web services enabled C-Commerce are still at the early stage. A further step is to incorporate organization structures, business objectives, and process performance indicators into existing business process models [9]. Then, we can use visual business process models to deliver contextual information to users and managers so that they can easily access operational systems and performance data by navigating graphical business models [7].

There are many issues and challenges in dynamic Web service composition that need to be further addressed, including how to perform efficient and effective service discovery, how to generate machine understandable service descriptions (semantic annotations of Web services), how to automatically capture relations among services (e.g., interface matching), how to find an optimal composition among alternatives through quality metrics, and so on. For example, service discovery is one of the most fundamental and critical steps in dynamic Web service composition. Discovering the right service in an open system, however, is much more difficult than a matter of simply looking up a directory for several reasons. First, a trustworthy service registry might not exist. Second, there is a scalability problem—a service registry has to keep up with an ever-increasing number of services. Third, current service discovery is keywordbased, which encounters similar problems in keyword-based information retrieval. Therefore, semantics/ontology-supported Web service representation and modeling (e.g., DAML-S/OWL-S) are desired [26]. Built on top of OWL (Web Ontology Language), OWL-S supplies Web service providers with a core set of markup language constructs for describing properties and capabilities of their Web services in an unambiguous, computer-interpretable form. OWL-S markup of Web services can facilitate the automation of Web service tasks including automated Web service discovery, execution, interoperation, composition and execution monitoring.

With the advent of more comprehensive Web services standards in support of process execution, software vendors are developing new WS-enabled BPMS products integrating functions of workflow systems and B2B servers. WS-enabled BPM will become a key technology to support dynamic inter-enterprise business processes, realizing the ultimate goal of C-Commerce. Further empirical research to study the implementation issues and impacts of WS-BPMS on C-Commerce is warranted.

## References

[1] A. Arkin. Business process modeling language, BPMI.ORG. November 13, 2002.

[2] A. Arkin, et al., Web Service Choreography Interface 1.0 Specification, 2004 (http://dev2dev.bea.com/techtrack/wsci.jsp).

[3] BPMI.ORG, BPML|BPEL4WS: A Convergence Path Towards a Standard BPM Stack. (2002).

[4] CapeClear, EAI and Web Services Lowering the Total Cost of Integration, 2002 (Dec.) (http://www.capeclear.com/products whitepapers/eai<sup>\_</sup>ws<sup>\_</sup>whitepaper.pdf).

[5] F. Casati, M. Shan, Dynamic and Adaptive Composition of E-Services, 2001.

[6] M. Champion, et al., Web Services Architecture, W3C, 2002 (http://www.w3.org/TR/2002/WD-ws-arch-20021114).

[7] M. Chen, A model-driven approach to accessing managerial information: the development of a repository-based executive information system, Journal of MIS 11 (4) (1995) 33– 63.

[8] M. Chen, Factors affecting the adoption and diffusion of XML and Web services standards for e-business systems, International Journal of Human-Computer Studies 58 (3) (2003) 259– 279.

[9] M. Chen, J.F. Nunamaker, E.S. Weber, The use of integrated organization and information systems models in building and delivering business application systems, IEEE Transactions on Knowledge and Data Engineering 1 (3) (1989) 406– 409.

[10] Collaxa, On BPEL4WS 1.1, 2003 (http://www.collaxa.com/ product.bpel11.html).

[11] T.H. Davenport, Putting the enterprise into the enterprise system, Harvard Business Review (1998 (July–August)) 121–131.

[12] T.H. Davenport, Mission Critical—Realizing the Promise of Enterprise Systems, Harvard Business School Press, Boston, MA, 2000.

[13] M. Dell, C. Fredman, Direct from Dell: Strategies That Revolutionized an Industry, Harper Business, New York, NY, 1999.

[14] Deloitte, Directions in Collaborative Commerce: Managing the Extended Enterprise, 2002 (http://www.dc.com/Insights/ research/cross<sup>\_</sup>ind/collaborative<sup>\_</sup>commerce.asp).

[15] DelphiGroup, Bpm2002 Market Milestone Report. Delphi Group White Paper, Boston, MA, 2002.

[16] P. Fletcher, M. Waterhouse, Web Services Business Strategies and Architectures, Expert Press, Chicago, IL, 2002

[17] J. Fou, Web services and collaborative commerce: collaborate or die, Web Services Architect, 2001.

[18] T.F. Gattiker, D.L. Goodhue, Understanding the local-level costs and benefits of ERP through organizational information processing theory, Information and Management 41 (4) (2004) 431– 443.

[19] M. Granville, Conditional Logic in Sequence Diagrams, 2001 (http://www-106.ibm.com/developerworks/java/library/ j-jmod0605/).

[20] M. Harris, Defining: collaborative commerce, EAI Journal (2002 (March)) 41– 42.

[21] J. Herman, Making Collaborative Commerce Happen, 2002 (http://www.bcr.com/bcrmag/2002/10/p18.asp).

[22] IBM, The Executive E-Business Infrastructure Guide, 2001.

[23] G. Keller, S. Meinhardt, SAP R/3 Analyzer: Business Process Reengineering Based on the R/3 Reference Model, SAP North America, Philadelphia, PA, 1994.

[24] S. Kownslar, Collaborative commerce, Ubiquity-ACM 3 (33) (2002) 1.

[25] F. Leymann, D. Roller, M.-T. Schmidt, Web services and business process management, IBM Systems Journal 41 (2) (2002) 198–211.

[26] S.A. McIlraith, T.C. Son, H. Zeng, Semantic web services, IEEE Intelligent Systems 16 (2) (2001) 46– 53.

[27] Microsoft, Application Architecture For .Net: Designing Applications and Services, Microsoft Press, 2003.

[28] Microsoft, BizTalk 2004 Beta, 2003 (http://www.microsoft. com/biztalk/beta/).

[29] Microsoft, Microsoft BizTalk Server Product Overview, 2003 (http://www.microsoft.com/biztalk/evaluation/overview/ biztalkserver.asp).

[30] NerveWire, Collaborative Commerce: Compelling Benefits, Significant Obstacles, 2002 (http://www.nervewire.com/ about/press<sup>\_</sup>archive/collab<sup>\_</sup>comm<sup>\_</sup>survey.htm).

[31] S. Rabin, Collaborative Commerce: Automating and Integrating Trading Partner Relationships, 2001 (http://ecmgt.com/ Nov2001/feature.article.htm).

[32] H. Reed, Managing the reach and range of your business processes, Web Services Journal 3 (7) (2003) (July) (http:// webservices.sys-con.com/read/39804.htm).

[33] G. Samtani, D. Sadhwani, Enterprise application integration (EAI) and web services, in: P. Fletcher, M. Waterhouse (Eds.), Web Services Business Strategies and Architectures, Expert Press, Ltd., Birmingham, UK, 2002, pp. 39– 54.

[34] SAP, Sap Unveils Enterprise Services Architecture as the New Blueprint for Adaptive Business Solutions, http:// www.mysap.com/solutions/netweaver/newsevents/index.asp? pressid=2003.

[35] S. Shang, P.B. Seddon, Assessing and managing the benefits of enterprise systems: the business manager’s perspective, Information Systems Journal 12 (4) (2002) 271– 299.

[36] D. Sherman, BPEL: make your services flow, Web Services Journal (2003) 16– 21.

[37] A.P. Sheth, W.V.D. Aalst, I.B. Arpinar, Processes driving the networked economy, IEEE Concurrency 7 (1999) 18–31.

[38] H. Smith, P. Fingar, Twentieth-first century business architecture: the future is here, Web Services Journal (2003 (July)) 10–14.

[39] H. Smith, et al., The emergence of business process management, CSC’s Research Services (2002).

[40] B. Srivastava, J. Koehler, Web service composition—current solutions and open problems, 3rd International Conference on Automated Planning and Scheduling (ICAPS’03) Workshop on Planning for Web Services, Trento, Italy, 2003.

[41] Stencil Group, Defining Web Services, 2001 (http://www. stencilgroup.com/ideas<sup>\_</sup>scope<sup>\_</sup>200106wsdefined.pdf).

[42] V. Tschammer, Collaborative Commerce—Trends and Technology Potentials, First DEEDS Policy Group meeting, Brussels, May 14–15, 2001 (http://www.deeds-ist.org/Downloaddocs/ Technology-DEEDS-Paper.pdf).

[43] W3C, XSL transformations (XSLT) specification, W3C Working Draft, 1999 (http://www.w3.org/TR/xslt).

[44] W3C, Simple Object Access Protocol (SOAP) 1.1 W3c Note, 2000 (http://www.w3.org/TR/SOAP/).

[45] W3C, XML schema Part 0: primer, W3C Recommendation, 2001 (http://www.w3.org/TR/xmlschema-0/).

[46] webMethods, webMethods 6 Integration Workshop: Participant Guide, webMethods, Inc., Fairfax, VA, 2003.

[47] WfMC, Workflow management coalition terminology and glossary. Workflow Management Coalition WFMC-TC-1011, 1999 (Feb.).

[48] D. Zhang, Web services composition for process management in E-Business, Journal of Computer Information Systems XLV (2) (2005) 83– 91.

![](/api/attachments/A468SMMF/fulltext/images/8a36a444425dc53ec0cdc19cd987511ab0cfa2f447d74ee7aeb43de8f0ae7760.jpg)

Minder Chen is an Associate Professor of Management Information Systems and Decision Science in the School of Management at George Mason University and was the Director of Technology Program (an Executive Master Program in Information Technology Management). He received a B.S. in Electrical Engineering from National Taiwan University in 1979, an M.B.A. from National Chiao Tung University in 1983, and a Ph.D. in Management Infor-

mation Systems from the University of Arizona in 1988. His primary research interests are Web services, electronic commerce, knowledge management, business reengineering and change management, computer-aided software engineering, collaboration technologies and virtual teams, and object-oriented systems development methodology. He has published papers in International Journal of E-Business, Journal of Management Information Systems, Database, Journal of Organizational Computing, Expert Systems with Applications, IEEE Transactions on Knowledge and Data Engineering, International Journal of Human Computer Studies, Journal of Electronic Commerce Research, Journal of Computer Information Systems, IEEE Transactions on Systems, Man, and Cybernetics, Journal of Small Group Research, and IEEE Software. He is the program co-chair of the Third Workshop of E-Business, Dec. 2003 and the invited speaker on <sup>b</sup>XML Web Services and E-Business<sup>Q</sup> at a pre-conference session of ICIS 2002 in Spain, sponsored by Microsoft.

![](/api/attachments/A468SMMF/fulltext/images/b4b9dd30588bac4e7a9592b333562fab05c225ba2093039961b3734523301e21.jpg)

Dongsong Zhang is an assistant professor in the Department of Information Systems at University of Maryland, Baltimore County. He received his Ph.D. in Management Information Systems from the University of Arizona. His research interests include Web-based learning, mobile computing, computer-mediated communication, and data mining. His work has been published in Communications of the ACM, IEEE Transactions on Multimedia, IEEE Transac-

tions on Systems, Man, and Cybernetics, Communications of the AIS, Journal of the American Society for Information Science and Technology, among others.

![](/api/attachments/A468SMMF/fulltext/images/e88cc830ea6c4fba49a263acd3277475fa833e821abca664fe8679838c1c4fcd.jpg)

Lina Zhou is an assistant professor in the Department of Information Systems at University of Maryland, Baltimore County. She received her Ph.D. in Computer Science from Peking University. Her research interests center around text mining, deception detection, ontology learning, and Semantic Web. Her work has appeared in Journal of Management Information Systems, Communications of the ACM, IEEE Transactions on Professional Communica-

tion, IEEE Transactions on Systems, Man, and Cybernetics, Group-Decision and Negotiation, among others.
