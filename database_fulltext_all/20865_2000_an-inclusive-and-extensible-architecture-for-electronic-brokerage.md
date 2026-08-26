---
otero_id: 20865
otero_key: "TWJVVWFC"
title: "An inclusive and extensible architecture for electronic brokerage"
authors: "Jenny Hands; Mikhail Bessonov; Mike Blinov; Ahmed Patel; Ron Smith"
year: "2000"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(00)00080-4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An inclusive and extensible architecture for electronic brokerage

Jenny Hands <sup>a,)</sup>, Mikhail Bessonov <sup>b</sup>, Mike Blinov <sup>b</sup>, Ahmed Patel <sup>b</sup>, Ron Smith <sup>c</sup>

Fretwell–Downing Data Systems Ltd., 113 OÕerton Road, Hillsborough, Sheffield S6 1WH UK

<sup>b</sup> Computer Networks and Distributed Systems Research Group, Department of Computer Science, UniÕersity College Dublin,

Belfield, Dublin 4, Ireland

KYROS, 55 EÕripidou and Thiesseos AÕe., Kalithea 17674 Athens, Greece

## Abstract

The output and experience of a large European project in Electronic Brokerage called AGeneric Architecture for Information AvailabilityB Ž . GAIA is presented. The paper describes a reference model and functional architecture for value-added mediation in Electronic Commerce. The customers are provided with a uniform way of accessing heterogeneous suppliers without changes in the supplier software. A way of employing distributed objects for large-scale service integration and multi-enterprise transactions is shown. The issues encountered during the implementation of the Common Brokerage Architecture CORBA -based pilot prototype and the application of the architecture in three diverse domains are presented.Ž . q 2000 Elsevier Science B.V. All rights reserved.

Keywords: Electronic brokerage; Electronic Commerce; Brokerage architecture; Supply chain; CORBA; Java; Z39.50; GAIA Project; RFC 2552

## 1. Introduction

Dictionaries define commerce as Athe buying and selling of goods and servicesB.

Electronic Commerce can be broadly seen as applying the information technology and telecommunications advances of recent years towards increasing the efficiency, effectiveness, and functionality of traditional commerce practices in the supply chain linking producers of goods and services and the eventual consumer. As such, Electronic Commerce covers a diverse range of commerce related activities including, but not limited to:

<sup>Ø</sup> processes that aid the potential customer individ-Ž ual or business , in locating the goods and ser-. vices they need and at the same time allowing suppliers to make potential customers aware of their products;

<sup>Ø</sup> processes facilitating the negotiation of a basis for the transaction that mutually benefits all parties;

<sup>Ø</sup> the processing of the agreed transaction;

<sup>Ø</sup> the management of the on-line delivery of the goods or services from the supplier to the consumer; and

<sup>Ø</sup> after sales services that ensure that the customer is satisfied with the order and delivery process and is able to use the delivered goods or services to their full extent.

The objective of this paper is to examine the role of brokerage within the context of Electronic Commerce and to present the Generic Architecture for Information Availability GAIA , an expandable ar-Ž . chitecture for the implementation of electronic brokerage systems.

## 1.1. Electronic commerce concerns

Electronic Commerce offers a foundation for many benefits for both the consumer and the supplier. The fact that DELL Computers profitably sells over \$5 M a day via their WEB site a is proof of the benefits Electronic Commerce has to offer customers and suppliers 10 . In parallel, there are also risks associ- <sup>w</sup> <sup>x</sup> ated with the introduction and spread of Electronic Commerce. Outside of the well-publicized issues, such as those in regard to credit card fraud, there is a real danger in what we will refer to as supplier overload. With the ease at which the current state of the art allows the creation of a WEB site, one can easily envision the situation where every individual or organization producing goods and services sets up its own on-line WEB store. If such an unstructured uncontrollable approach to the spread of Electronic Commerce continues, the future success and up-take of the technology and concepts is questionable. Related business models, architectures, and standards must be developed and adopted if Electronic Commerce is to fulfill its promise.

## 1.2. The need for the electronic broker

With this avalanche of on-line suppliers and information about goods and services, how is the consumer to locate, purchase, and obtain the goods and services they seek, at a fair market price, and from a supplier they can feel confident with? The introduction of the role of an on-line electronic broker into the Electronic Commerce supply chain linking consumers and suppliers presents the ideal solution to this problem. Mediation by these on-line electronic brokers joins customers and suppliers, thus, stimulating the market activities of both parties. Electronic brokerage systems have the potential of offering suppliers the capability to expand the number and type of potential customers for their products, thus, allowing small and medium size suppliers to more effectively and efficiently compete with larger suppliers in their domain.

## 1.3. The need for a supplier-independent architecture for electronic brokerage

In order for the electronic brokerage concepts to be effectively implemented, it is important that such implementations be based on relevant architectures and agreed standards. The brokerage architecture must be scaleable and be applicable to the distributed on-line nature of today’s Electronic Commerce supply chains. It must handle the diverse nature of the existing and future goods and services to be traded. At the same time, it must handle the heterogeneity of the systems deployed by the actors involved in the supply chain and the heterogeneous networks linking them. The architecture must allow implementations that are commercially feasible. It must support the ability of actors taking the role of broker to add value to the supply chain and to financially benefit from this added value. Recognizing that today, it is widely accepted that transactions are the key to constructing reliable distributed applications, it is important that the architecture support the transaction-oriented ACID properties, which are currently absent in today’s most commonly used Internet technologies 21,12 . To ensure success, the architecture<sup>w</sup> <sup>x</sup> must be generic and applicable to a diverse range of domains. And most importantly, to ensure fair competition and protect the consumer from a monopolistic environment, the architecture must be supplier-independent.

The explosion in Internet access and the advent of Electronic Commerce presents great potential for the market for electronic brokerage services. To date, most efforts towards the realization and standardization of this market have focused on infrastructural issues, such as secure on-line payment, electronic product catalogues, and digital delivery. However, if there is to be interoperability between businesses in the supply chain, permitting participation of both large and small suppliers and promoting choice and diversity, a supplier-independent architecture for brokerage meeting the above-described requirements is required. The GAIA, presented in this paper, is being developed by an international consortium of 19 organizations. The GAIA approach supports an information society in which Information Brokers offer service economies and refinements that enhance the supply chain to the advantage of producers and service providers in diverse domains.

## 1.4. Related electronic brokerage projects

During the past few years several projects have been carried out in the area of electronic brokerage. These projects were either focused purely on brokerage, or else, considered it in the context of Electronic Commerce in general.

The Common Brokerage Architecture CORBAŽ . project 9 aimed to create an open architecture for <sup>w</sup> <sup>x</sup> the brokerage of distributed on-line resources. It has produced a comprehensive framework for brokerage systems. However, it has not defined any protocols and interfaces between actors, and did not address related interoperability issues. It also did not pay significant attention to possible federation between brokers.

The objective of the OSM An Open ServiceŽ Model for Global Information Brokerage and Distribution project 6 was to create a framework for the. <sup>w</sup> <sup>x</sup> Electronic Commerce in general. The OSM model is based on the CORBA architecture. Unfortunately, the OSM architecture does not go beyond the CORBA world. It requires all customers, brokers, and suppliers to support CORBA. This model does not cover existing customers and suppliers that use customary trading protocols. OSM also limits the scope of the brokerage to the discovery stage of the trading process.

The Object Framework for Electronic Requisitioning OFFER project 1 extended the OSM model of Ž . <sup>w</sup> <sup>x</sup> brokerage to cover both discovery and negotiation. However, it is still limited to the CORBA world. The OFFER project also increased the flexibility of the framework by introducing a class of exchangeable components. Unfortunately, this idea was only applied to the swapping of negotiation auction mech-Ž . anisms.

The Metabroker project 2 , in contrast to the <sup>w</sup> <sup>x</sup> OSM project, aimed to provide a framework that allows the integration of existing trading protocols and data formats. This is achieved by the introduction of an extra level of Aclient proxiesB that are responsible for the protocol implementations. However, the Metabroker project did not specify the external interfaces of brokers to facilitate inter-broker communication. It also used a proprietary Shadows environment for the design of proxies, which complicates the implementation of proxies by third parties. The scope of Metabroker is also limited to the discovery stage.

OMG established a Domain Task Force in Electronic Commerce ECDTF . This group produced a Ž . working version of the Electronic Commerce Reference Model 11 . This model is largely based on the<sup>w</sup> <sup>x</sup> results of the OSM project and inherits certain disadvantages of the OSM model. It limits the activity of the broker only to the discovery stage of the trading process and does not pay attention to the existing trading protocols. ECDTF has defined a framework for the long-term development of the facilities for an electronic market. However, only a few facilities are developed at the moment.

## 2. The GAIA project

## 2.1. Conception of the GAIA project

The GAIA project was conceived in 1996 to address the requirement of the on-line business society for a standards-based brokerage architecture, as outlined above. Around the central theme of the project, to produce an architecture for brokered information supply services, objectives were defined to establish a GAIA Standard with architecture and protocol recommendations, and a generic toolset to contribute to the development of practical, interoperable information brokers. In this way, GAIA would facilitate the location and purchase of online information, goods and services.

The GAIA consortium comprises service providers from diverse fields in IT, telecommunications and commerce, and a number of research organisations.

## 2.2. OÕerÕiew of GAIA’s work

In the remainder of this paper, we present the key results of the GAIA project with reference to their application and applicability in Electronic Commerce.

As shown in Fig. 1, the GAIA environment has been modeled from a number of perspectives, differing in their level of abstraction.

At the most abstract level, the GAIA Reference Model provides a common basis for the description and specification of brokerage systems. The GAIA Reference Model is defined in terms of the Roles, Actions, Events and Entities involved in electronic brokerage. The GAIA Functional Architecture defines the functional elements of the GAIA system, embodying the GAIA Reference Model. The Functional Architecture specifies the roles and relationships between the GAIA Services which instantiate the Actions and supporting Events of the Reference Model. Based on the functional relationships of architectural elements and their relationship to the world at the large, the GAIA Standard is specified.

The development of generic tools within the architecture has been a core activity in the project, providing key reusable services, including user access components and mechanisms to use data from existing repositories. The GAIA pilot implementation broker is built on the CORBA-distributed object architecture. The experience the GAIA project gained from building a CORBA-based Broker is described later in this paper.

Crucially important to the development and validation of the GAIA approach has been the involvement of representative bodies and user communities in trials of the GAIA service. GAIA selected three target domains in which to demonstrate various implementations of the developed GAIA compliant brokerage system: the Music industry, the Technical Components industry, and the Publishing industry. The Music Industry Trial focuses on delivering information and product in specialized genres namelyŽ dance, ambient and free improvisation to the sector’s. highly dispersed global consumer base. The Technical Components Industry Trial provides electronic brokerage services to allow engineers to select and retrieve technical information on a wide selection of die for the design of MultiChip Modules MCMsŽ . and hybrid circuits. The Publishing Industry Trial allows students, researchers and industry experts to locate, order and receive digitally a wide range of on-line material, including scientific articles from journals and agricultural information, such as agricultural statistics and customer contacts.

The span of these domains, from the structured, highly specified, standards-oriented, technical nature of the Technical Components industry to the artistic, loosely structured, multimedia nature of the Music industry, is to ensure that the GAIA architecture covers the needs of a wide array of other domains.

## 2.3. The GAIA Reference Model

Before describing the Functional Architecture, which is a key result of GAIA and the basis for deployment of brokerage services, we will briefly outline the Reference Model, which is the highest level of abstraction considered by GAIA, in order to clarify the use of terminology. The design of the GAIA Reference Model was based on the requirements captured in three diverse application domains, namely publishing, music and technical data domains. Models of the electronic marketplace suggested by other projects in the area of Electronic Commerce were also taken into consideration.

![](/api/attachments/TWJVVWFC/fulltext/images/0f729ba41226e4c45d60efae376052c86bfefaea31ae3fa680eacd3e9caad927.jpg)  
Fig. 1. GAIA standard formulation levels of abstraction.

The core concepts promoted by the GAIA project’s Reference Model are the roles of customer, broker and supplier, and the actions of search, locate, order and deliver. These generic roles and actions have been found to be a good basis to discuss and develop a working demonstrator broker infrastructure, with brokers and suppliers spread around Europe. The scope of the Reference Model has been limited to these areas of electronic brokerage and has not been formulated to address other areas of brokerage, such as workflow and pre- and post-sales support. Clearly, the brokerage system must interact with the back-of-house systems supporting such functionality.

Central to the reference model is the GAIA broker, which acts as a locator and supplier of information or services to customers, i.e. users who seek services and information online, and likewise, a distribution mechanism for suppliers wishing to promote goods and services. The broker either supplies the information or service to the customer itself inŽ which case, it is acting in the supplier role , or else . Ž . playing a customer role itself it sources the information or service from another broker<sup>r</sup>supplier.

Inter-broker connections are very important for the scalability of the architecture. Brokers can specialise in different domains either by application or Ž geographic meaning . However, a customer does not . have to search for an appropriate broker. The nearest broker that supports inter-broker communications can accept the request and fulfil it using the service of a broker specialised in the area of request. If a new application domain or area is available, it can be covered by a new broker, which will propagate its services to all the members of the federation. Differ ent brokers can cover some areas simultaneously, which creates competition between brokers.

The function of the broker is to provide a path, whereby a customer may find and obtain a product.

If the broker knows where such a product can be found, he supplies the customer with the location information. If the broker does not know the location of a product, he requests a search on his behalf from other brokers, thus, widening the search. In order to allow a search to be carried out, the terms of the search need to be clearly defined. A description needs to be given by the customer to the broker of the product that he requires. The use of metadata is central to the functioning of the GAIA broker, both for the customer to describe the product that he requires, and for the GAIA broker to propagate the search to further brokers.

While brokerage involves various phases of business operation 13 , including awareness creation, <sup>w</sup> <sup>x</sup> etc., it is the transaction phase that is of most concern to GAIA. The AactionsB which the GAIA architecture caters for during a transaction are:

<sup>Ø</sup> search, where the customer describes the nature of the product, and the broker returns the identity of products matching this description;

<sup>Ø</sup> locate, where the customer obtains from the broker the location and terms of supply for a required item;

<sup>Ø</sup> order, where the customer requests supply of the required item from the given location; and

<sup>Ø</sup> delivery, where the broker causes the item to be sent to the customer.

Around these main actions are supporting actions, of which the most important are authentication, tariffing and connection to payment systems.

Based on these concepts, a more detailed architecture can be developed, first, in terms of functional decomposition, and then, in terms of systems architecture.

## 3. GAIA Functional Architecture

The GAIA Functional Architecture decomposes the overall functionality of the brokerage system into a number of components, and describes the roles and relationships of the components, and the manner in which they interoperate. The key elements of the GAIA functional architecture are the GAIA kernel,

Functional Unit Managers FUMs , Functional UnitsŽ . Ž . Ž . FUs , and Abstract Primitives APs . These are described in detail below.

## 3.1. FUs

The brokerage system provides a number of services to its users. These services are supported by the functions of the brokerage system. These include, for example,

<sup>Ø</sup> searching,

<sup>Ø</sup> metadata collection, and

<sup>Ø</sup> format translation.

Each of these functions can be provided by a number of different candidate technologies. However, the operations that are required to be carried out remain the same — regardless of the selected technologies, the functional requirements do not change. The required operations are described in terms of APs, which can be mapped to the protocol requests of whatever technology is selected to support the function. A mapping component, called an FU, is defined for each candidate technology, and converts calls to APs into protocol instructions. The FU acts as an interface between its particular technology and the rest of the brokerage system.

FUs are defined for each candidate technology that can be used to fulfil a particular functional need of the brokerage system. An FU accepts AP invocations, and maps them to calls to the particular technology to which it is dedicated. The results of the calls to the technology are translated into the corresponding APs and returned by the FU.

## 3.2. FUMs

As noted above, a number of different candidate technologies can be used to fulfil a particular functional requirement of the brokerage system. Depending on the details of the GAIA transaction underly- Ž ing network, Customer system capabilities, domain requirements, etc. , different technologies may be . more useful during different Transactions. As a result, each candidate technology has its own FU, which is invoked when that particular technology is required.

A number of different FUs can exist, which fulfil the same functional requirement of the brokerage system. In order to select the most appropriate FU Ž . and technology , the brokerage system needs to know which is most useful at any particular time. This is the responsibility of the FUM. Each function of the brokerage system has a single FUM, which is invoked in terms of APs by the Broker kernel. This FUM selects the most appropriate of the candidate technologies, and calls the corresponding FU. The interface between the FU and the FUM is defined in an open, platform-independent, programming-language-independent manner. It is important to notice that all the FUs subordinate to the same FUM have the same interface. This holds true even in the case of considerable differences between the technologies used to implement these FUs. This hides the internals of particular FUs from the FUM. The specification of the interface consists of the formal definition in CORBA IDL and the guidelines for the interpretation of passed parameters. This allows a third party vendor to develop a new FU, implementing, for example, some recently emerged search protocol, and incorporate it into the broker without any modification of any other component. This makes the architecture easily extensible.

## 3.3. The kernel and APs

The kernel of the brokerage system acts as a buffer between the FUMs, and as a bus for the transmission of APs between FUMs. It also acts as a repository of local information and as a shared data store for FUMs. All calls to APs are executed via the kernel, which exports all the APs imported by the various FUMs, and imports all those exported by the FUMs.

As shown in Fig. 2, communication between the GAIA kernel and FUMs, and between FUMs and FUs, is carried out in terms of APs. In a pure CORBA world, we would call them just methods of particular published interfaces. However, to allow a non-ORB-based implementation of a GAIA broker and to keep the interface general, a concept of APs was introduced. These APs correspond to a particular operation, which a FUM will carry out on behalf of the kernel, or which the FUM expects the kernel to carry out. Each FUM imports a set of APs, representing those services, which the FUM expects to receive from some other part of the system. The services, which the FUM is prepared to provide to other elements of the brokerage system, are presented in the form of exported APs. All APs are imported from, and exported to, the kernel. The kernel acts as a bus for APs. APs are also used in communication between the FUM and its FUs. The FU exports APs to the FUM.

![](/api/attachments/TWJVVWFC/fulltext/images/4fd85a57468c0df9163227f1a06a341d3ae3b13935cd00159e9282b884a25057.jpg)  
Fig. 2. Communication between FUM and FU.

## 3.4. Elements of the GAIA Functional Architecture: description of FUMs

The core activities of the brokerage system include:

<sup>Ø</sup> searching for and identifying information Products that fit a user description,

<sup>Ø</sup> sourcing information Products the identification of which is known,

<sup>Ø</sup> allowing users to order Products,

<sup>Ø</sup> delivering information in file format,

<sup>Ø</sup> delivering information as a continuous media stream,

<sup>Ø</sup> monitoring use of the system and charging for it,

<sup>Ø</sup> enforcing the security policy of its particular security domain,

<sup>Ø</sup> collection of information about what is available Ž . metadata collection ,

<sup>Ø</sup> providing a user interface to the brokerage services and alerting users as to the availability of information, using e-mail, mobile terminals, etc.,

<sup>Ø</sup> interacting with external directory services, and

<sup>Ø</sup> allowing the user to provide feedback on a particular Action or transaction.

This is illustrated in terms of FUMs in Fig. 3. Table 1 contains a brief description of every FUM specified by the GAIA Functional Architecture.

![](/api/attachments/TWJVVWFC/fulltext/images/4bddf5ee009b264a54a9d56fb171beac5d88937668754f6d670bb47ad9da7c09.jpg)  
Fig. 3. GAIA Functional architecture FUMs.

Table 1  
FUM responsibilities summary

<table><tr><td>FUM</td><td>Responsibilities</td></tr><tr><td>Search</td><td>Accepts requests to carry out a search for Products that fit a particular user description. It returns lists of identifiers of Products that fit the description.</td></tr><tr><td>Locate</td><td>Accepts Product identifiers, and discovers where they may be obtained. It returns lists of Suppliers and locations for the Product.</td></tr><tr><td>Order</td><td>Manages negotiations between a Customer and a Supplier, in order that agreement may be reached on the terms of availability of a particular Product or group of Products. Following the negotiation phase, the order FUM accepts purchase commitments from the Customer and forwards them to the Supplier. It returns a notification of the status of the order Action.</td></tr><tr><td>Item delivery</td><td>Manages the delivery of file-structured items to the Customer.</td></tr><tr><td>Stream delivery</td><td>Manages the delivery of real-time multi-media data streams to and from the Customer.</td></tr><tr><td>Payment</td><td>Provides a mechanism for payment from one actor to another.</td></tr><tr><td>Authentication</td><td>Provides a mechanism which allows a user to prove his identity to the brokerage system.</td></tr><tr><td>Metadata collection</td><td>Supports the collection of Product descriptions and where they are available.</td></tr><tr><td>Customer</td><td>Provides an interface for the user to allow him to interact with the brokerage system. It also alerts him when a Customer-specified event occurs.</td></tr><tr><td>Directory services</td><td>Provides an interface between an external directory service and the brokerage system.</td></tr></table>

In the event that a GAIA broker is a distributed entity, with different FUs and FUMs running on different platforms to the kernel, inter-module communication uses the CORBA model. The internal operations of the broker the APs imported and Ž exported by the FUMs are encoded using the Inter-. net Inter-ORB Protocol IIOP 5 inter-ORB proto- Ž . <sup>w</sup> <sup>x</sup> col, along with any data or other variables required for the operation, and then transported among the FUMs. The pilot implementation developed by the GAIA project supports this distributed model.

## 4. Choice of brokerage protocols

## 4.1. The GAIA Standard

As previously discussed, the architecture of the GAIA brokerage system is designed so that a number of different technologies can be used to fulfil any particular functional requirement of the system and, furthermore, the GAIA Broker can interoperate with non-GAIA systems, where compatible technologies have been implemented. However, in order to promote interoperability, GAIA also specifies a AGAIA StandardB, in which one technology is selected for each FUM.

The criteria for selection reflected the over-riding need to specify a workable standard, with the best chance of producing brokerage systems that are interoperable with other information navigation systems. Key selection criteria include the following:

<sup>Ø</sup> popularity and acceptance,

<sup>Ø</sup> standards status,

<sup>Ø</sup> functionality, and

<sup>Ø</sup> feasibility of integration with other information navigation systems.

The functionality of a GAIA broker is rather diverse, and different interactions in the GAIA system present varying requirements to the underpinning technologies. For the purpose of selection of appropriate protocols, the operations of a brokerage system can be broken into the following three categories:

<sup>Ø</sup> interactions with the customer,

<sup>Ø</sup> interactions with other brokers, and

<sup>Ø</sup> interactions with suppliers.

The first and last of these occur at the two ends of a supply chain, while inter-broker operations take place at other points in the chain. As shown in Fig. 4, the supply chain may take a number of different forms:

<sup>Ø</sup> A minimal chain, where the customer and the broker are the ends of the chain, and there are no intervening links. In this case, the broker plays the role of supplier to the customer.

![](/api/attachments/TWJVVWFC/fulltext/images/193868800fa837411835d788c7402c0a6b378581ced63f90c4bf1bfb84005863.jpg)  
Fig. 4. Supply chains.

<sup>Ø</sup> A three-piece chain, where the broker deals with the customer and the supplier, but not with any other broker.

<sup>Ø</sup> A longer chain, with one or more inter-broker operations.

## 4.2. Minimal profile

As specified by the GAIA reference model, a GAIA transaction is composed of a number of actions, such as search, order and delivery. Each transaction is initiated by the customer, who makes a request to the broker. In the event that the broker is able to fulfil the request, the transaction involves no other actors. In this simple case, the GAIA transaction involves the customer and the broker, and the only protocol which needs to be standardised is that between the customer and the broker. This is done in a trivial way using the HTTP protocol 19 . The<sup>w</sup> <sup>x</sup> AGAIA standardB refers to such arrangement as a Aminimal profileB.

## 4.3. Basic profile

In the event that the broker is not able to fulfil a request, the action may be propagated on to other brokers, with the original broker playing the customer role. The supply chain is, thus, made up of a single customer, one or more suppliers, and one or more brokers. While some of the existing protocols enable chained operations e.g. Z39.50 , none ofŽ . them is suitable for all stages of the trading process. To solve this problem, the GAIA project has introduced an external broker interface defined in terms of CORBA and is called the GAIA Customer interface. This interface enables access to all actions comprising the trading process and provides operations for transaction management. The support of this interface is required in the so-called GAIA Basic profile. This profile is defined primarily to facilitate inter-broker communications. If a broker does not support the Basic profile, it can take part in chained operations using customary protocols, however, the functionality of such operations will be limited. It should be noted that all properties of transaction Ž . ACID can be fully supported only if they are supported by protocols involved in this transaction. That is why the GAIA Standard strongly encourages actors to support the GAIA Basic profile.

## 4.4. Extension modules

The extension modules in the GAIA standard specify the profiles to be used for various brokerage functions see Table 2 , thereby admitting supplier Ž . systems which do not adhere to the GAIA Basic profile to the wider GAIA Standard. Example protocols are Z39.50 for discovery, ISO ILL for ordering, and FTP 16 for item delivery. More extensions can<sup>w</sup> <sup>x</sup> be easily added whenever necessary.

Table 2  
GAIA extension modules

<table><tr><td>Extension module</td><td>Protocols supported</td></tr><tr><td>Item delivery</td><td>FTP, Internet e-mail/MIME, GEDI</td></tr><tr><td>Stream delivery</td><td>MPEG/RTP</td></tr><tr><td>Security</td><td>PKIX/GSS, SSL, Java AccessControl System</td></tr><tr><td>Payment</td><td>SET</td></tr><tr><td>Discovery</td><td>Z39.50</td></tr><tr><td>Order</td><td>ISO ILL</td></tr><tr><td>Customer</td><td>Z39.50, ISO ILL, e-mail</td></tr></table>

Search and Locate actions involve the customer finding a resource or product with the assistance of the broker. By default, specification of the actions takes place via HTTP 7 , with the customer using a <sup>w</sup> <sup>x</sup> WWW interface to the GAIA broker, and the results of the discovery are returned to the customer via the WWW interface. However, if specified, results may also be returned via e-mail, using the SMTP with MIME extensions. It should be noted that searches are particularly likely to be initiated on a GAIA broker by entities which conform only to the Z39.50 protocol in the GAIA Standard. These may be chained using Z39.50 to other non-conformant entities.

Order involves the customer asking that a resource or product be delivered to him by the broker or the supplier. Once again, this takes place via a WWW interface, and the order is transported to the broker via HTTP. If the order needs to be propagated, and the basic profile is supported, the order is ‘translated’ to APs, encoded with IIOP, which are used for inter-broker communication. At the supplier end of the chain, ISO ILL may be used for ordering from libraries. This is depicted in Fig. 5.

The DeliÕery action may either be carried out using a direct supplier–customer delivery where theŽ broker has only worked as a referral agency, or is itself the supplier , or via a supply chain of multiple . linked deliveries. As shown in Fig. 6, a delivery to the customer may make use of a number of different protocols, including FTP 16 , e-mail <sup>w</sup> <sup>x</sup> <sup>r</sup>MIME <sup>w</sup> <sup>x</sup> <sup>w x</sup> 14,15,17 , and MPEG<sup>r</sup>RTP 7,18 in case of con- Ž tinuous media delivery ..

A Broker can choose an appropriate set of Extension Modules to conform to according to the functionality it wishes to achieve. There is one extension module for each of the functional areas, which are not covered by the Basic and Minimal Profiles, and one extension module for each of the existing areas Ž . Customer, Discovery and Order to allow the use of protocols other than IIOP. The extension modules specified and the protocols they are based upon are summarized in Table 1.

![](/api/attachments/TWJVVWFC/fulltext/images/691f5079c0e869e0ff29d899c15c7ceba7e83a87b763660ed444a70149ca2a29.jpg)  
Fig. 5. Search, Locate and Order action supply chains.

![](/api/attachments/TWJVVWFC/fulltext/images/125cc6af0a01f96ebaf7b93bb2e13a7ed36a4dae8b4b93b04111d476640dd248.jpg)  
Fig. 6. Delivery action supply chain.

## 5. Building a CORBA-based brokerage system

As noted earlier, the internal interfaces of the GAIA Functional Architecture were defined in CORBA IDL. This proved to be an excellent choice for a number of reasons. Subsequently, the decision was made to also use CORBA as an integration mechanism for the pilot development of the GAIA Broker. This decision was also venerated by experience, although initially, there were a number of difficulties.

GAIA made the decision to use IDL for the specification of functional interfaces for the following reasons:

<sup>Ø</sup> it is widely accepted as a standard;

<sup>Ø</sup> it is rigorously defined, independent of platform;

<sup>Ø</sup> it is easy for systems designers and programmers to learn;

<sup>Ø</sup> it is readable by technical staff with no CORBA training; and

<sup>Ø</sup> it is supported by tools such as AidldocB <sup>w</sup> <sup>x</sup> 13 which can produce documentation useful in a collaborative environment.

By May 1997, an initial set of IDL interfaces for the FUMs described above had been produced. In July 1997, the Consolidated Design for the GAIA Broker 4 was published, which detailed the IDL<sup>w</sup> <sup>x</sup> interface of the Broker Kernel, and rationalised the interfaces of the FUMs.

There were some debate as to whether these CORBA-compliant interfaces should lead to a

CORBA-based implementation of the GAIA Broker, i.e. with functional integration occurring around an ORB. The alternative was to use lower level protocols to integrate, with higher-level communication provided by a combination of proprietary middleware and GAIA’s own solutions. Note that Mi- Ž crosoft’s equivalent to CORBA, i.e. DCOM, was not in the running, because it does not support yet cross-platform interoperability..

The early experiments with ORBs were promising but problematic. A key issue was interoperability between different ORBs: prior to CORBA v2.0, no standard for interoperability was defined. Version 2.0 specifies General Inter-ORB Protocol GIOPŽ . and IIOP 4 , the latter instantiating the former over<sup>w</sup> <sup>x</sup> the Internet Protocol IP . The first v2.0-compliant Ž . ORBs appeared soon after GAIA started work, but interoperability was far from assured.

By December 1997, interoperability via IIOP was established. Systems integration of the basic framework was 4 weeks behind schedule and some AworkaroundsB were in place to handle some environment problems, e.g. concerning bugs in naming services and IIOP incompatibilities. However, with commercial requirements now mandating the use of a mixed Solaris<sup>r</sup>NT platform for a distributed Broker architecture, the use of ORBs was felt to have been beneficial. The implementation deployed to demonstrator sites for the GAIA trials makes use of the following interoperating components:

<sup>Ø</sup> Broker Kernel, built with Orbix from IONA ,Ž . running on Solaris or NT;

<sup>Ø</sup> assorted FUMs built with Orbix, running on Solaris or NT;

<sup>Ø</sup> Directory Services FUM built with OmniBroker Ž . a shareware ORB , running on NT; and

<sup>Ø</sup> Customer FUM interface built with VisiBroker Ž . from Visigenic , running on Solaris.

Other ORBs that GAIA worked with include ILU, a very early CORBA implementation from Xerox PARC laboratories, and OmniOrb, another shareware ORB. Of the ORBs tried, only Orbix and VisiBroker gave full v2.0 compatibility, with support for multithreading and for dynamic service activation. Omni-Broker was entirely satisfactory apart from lack of multi-threading, which made it suitable for a singlythreaded systems component, such as the Directory Services FUM, but not for the Broker or for the Search, Order or Directory FUMs. Dynamic service activation was considered important for efficiency, rapid start-up response time, and to support service fulfillment by agents.

Overall, the experience of ORB implementation was a good one. All components of the Functional Architecture were implemented with less AcompromiseB than the project expected. The Kernel and FUMs were built from scratch based on their IDL definitions, and largely coded in C<sup>qq</sup>. The FUs were, at least, partly based on existing code, with a

CORBA wrapper around them to offer the FUM<sup>r</sup>FU interface.

In the Spring of 1998, the User Interface architecture took shape. A layer of Java classes was built to offer this interface to diverse clients, and two structurally different User Interfaces were produced upon it. The Apure JavaB interface comprises Java applets or applications, resident or downloaded on the client machine, which call the Broker via IIOP. The Adynamic htmlB interface uses a proprietary webserver API to link a site-configurable front end to the Java classes resident on the webserver. GAIA usedŽ Netscape’s LiveConnect protocol to do this; another choice would have been Microsoft’s ISAPI protocol.. In addition, a non-Java User Interface was constructed, which provided access for non-GAIA clients running the Z39.50 search and retrieve protocol 23 : <sup>w</sup> <sup>x</sup> this interface, evidently, could not support the full range of Broker functions.

As shown in Fig. 7, three User Interface architectures were developed for the GAIA demonstrator.

The Apure JavaB interface is highlighted, as the choice which most readily supports the deployment of brokerage client software in a heterogeneous environment and is the solution being used in the GAIA Technical Components Domain demonstrator. At the time of writing, binding to Java from ORBs is much better supported than binding to C<sup>qq</sup>, Java being amenable to the provision of simpler arrangements for memory allocation, etc.

![](/api/attachments/TWJVVWFC/fulltext/images/860dfb0f01fe12fafbc9248ac75bee9fc919307b11a48051b467673ff656e55c.jpg)  
Fig. 7. User Interface architectures trialled with the CORBA-based GAIA Broker.

Fig. 8 concludes the discussion on the GAIA projects experience in developing and implementing a CORBA-based brokerage system by presenting an example of the search action as implemented within the Technical Components Domain demonstrator.

The simplified operation and implementation of each of the shown modules can be summarized as follows.

Ž . A Customer — the GAIA Technical Components Domain Client application is loaded on the customer’s Windows-based PC. This application has been written in Java and, in addition to user interface functions, it also includes Interaction Agent functionality 8 to assist the user in the operation of the <sup>w</sup> <sup>x</sup> system. After being authorized by the system, the customer performs a search operation by entering his<sup>r</sup>her search criteria and submitting the request.

Ž . B Customer FU — the GAIA Technical Components Domain Customer FU has been developed with VisiBroker from Visigenic and with Java. Call

Back target mechanisms are initiated and used to track the progress of the issued search request.

Ž . Ž . C Kernel with associated FUMs — the kernel and associated FUMs have been developed in C<sup>qq</sup> in conjunction with the Orbix CORBA environment from IONA. The kernel maintains a session for each active GAIA transaction. When the kernel receives the search request for the transaction, it will move the session to the search state and pass the request to the Search FUM. In the demonstrator, there is only one Search FU implemented so the request is passed to the Z39.50 Search FU. The kernel transaction mechanisms developed for the GAIA user trials were not based on any complex ACID transaction control process. Future commercial GAIA-based brokerage systems would need to internally include such properties using mechanisms such as those provided by the CORBA Transaction Service 12 . This will be <sup>w</sup> <sup>x</sup> particularity important for Broker kernels, which offer all of the brokerage actions described in the reference model.

Ž . D Search FU — the Search FU uses Z39.50 technology to formulate the search request. It was developed using existing software with an IDL

![](/api/attachments/TWJVVWFC/fulltext/images/67831517ed9f5fa9ae0ae322ba65473d0b3ed2c73c1c862a57d97c56c7e75d7d.jpg)  
Fig. 8. Technical components domain demonstrator.

CORBA wrapper. The FU will take the search request from the FUM and convert it into Z39.50 format.

Ž . E Supplier Database — the actual technical components supplier data is stored in a ZEBRA database. ZEBRA is a Z39.50 server developed by Index Data IS, a partner in the GAIA consortium. The ZEBRA server processes the search request and returns details of the result set to the Customer via the above-described modules.

To sum up the ORB experiences of GAIA, it is noted that cross-platform and cross-ORB interoperability is a reality and that the CORBA approach offers flexibility welcome in the provisioning of services in a distributed environment. While CORBA is at present an immature technology, it can be expected to evolve in the near future and constitute a key enabler technology for Electronic Commerce <sup>w</sup> <sup>x</sup> 22 . Other object-based approaches, such as DCOM, may also become applicable.

GAIA intends to promote its CORBA-based specifications and toolkits. Two areas where CORBA implementations may provide significant advantages are:

<sup>Ø</sup> the Z39.50 search and retrieve protocol, and <sup>Ø</sup> Directory Services.

The advantages of CORBA implementations, as specified by GAIA, are that service creators need not grapple with low-level encoding and transport mechanisms, and can use a much more standardised approach to systems integration based on business-level objects.

## 6. GAIA’s impact on the supply chain

## 6.1. Customer impact

The heterogeneous nature of a GAIA compliant broker will ensure that the prospective customer will be able to use their current computer environment and telecommunications infrastructure to access the services of a GAIA compliant broker. Accessing a GAIA compliant broker, as opposed to other current on-line retail points of presence, will ensure that customers can locate, order and receive delivery of a wide range of products and services from suppliers in a global non-monopolistic environment. The ability of a GAIA compliant broker to add value to the process of a customer obtaining goods and services will optimize the ability of customers to select the right product, at the right price, and at the right time.

## 6.2. Supplier impact

As with the customer, the heterogeneous nature of a GAIA compliant broker will ensure that a supplier wishing to promote, sell and deliver their product or service via a GAIA compliant broker will not have to invest in a new infrastructure. Establishing a commercial relationship with a GAIA compliant broker will allow the supplier to access a larger global potential customer base. Better deals are available via the broker for financial and distribution services than could be negotiated directly with today’s service providers. Additionally, the new technologies offered by a GAIA compliant broker allow new functionality to be implemented to aid the supplier. For example, a GAIA broker operating in the office automation domain could use push distribution functionality to automatically distribute, on a try and buy basis, new upgrades to a suppliers word processing application to all customers who have purchased the product via the broker.

## 6.3. Broker impact

The adoption of the concepts of the GAIA brokerage environment will create business opportunities for entry into new brokerage markets. The value-added capabilities of the architecture ensure that the perspective broker has the potential to financially prosper from their operation. The generic nature of the architecture allows the broker easily to move into an environment supporting multiple domains. The distributed heterogeneous nature of the architecture will allow the broker to establish business relationships with other GAIA compliant brokers allowing chained brokerage transactions.

The question arises as to how the AfairnessB of the broker can be controlled and guaranteed. Electronic brokerage systems cannot do more in this area than that which is available in a traditional marketplace: in general, life is not fair and the buyer must always be aware. Broker reputation will be key. In some domains, impartiality can be the broker’s added value, while in other domains, the added value could be presenting results in a desired biased way thus,Ž not fair . In all cases, and as in non-electronic mar-. ketplaces, it is the forging of business relationships between supplier and broker, and the marketing of products and services to the customer, which dictates availability and visibility in the supply chain. Thus, the brokerage business is driven not by fairness but by opportunity.

## 6.4. DeÕeloper<sup>r</sup>implementers

The documentation and toolkits developed as part of the GAIA project will allow implementers of GAIA compliant brokers to easily design and implement GAIA compliant brokers in many diverse domains.

## 7. Conclusion

The GAIA project ended successfully in January 1999. The project culminated with the successful running of GAIA compliant brokerage user trials in three diverse domains, thereby validating the feasibility of the brokerage architecture and concepts presented in this paper. The trials were accompanied with an evaluation phase where customers, suppliers and brokers completed on-line or paper-based questionnaires one per domain demonstrator that ad-Ž . dressed various aspects of their experiences and views on the system. The evaluation criteria focused on usability, efficiency, functionality and the benefits of the service. The results of this assessment process are fully detailed in the final GAIA project deliverable 3 . Key findings from the trials showed that:<sup>w</sup> <sup>x</sup>

<sup>Ø</sup> A broker must supply domain-specific added value to ensure commercial viability. Test users were willing to pay for this added value if its value was readily apparent. For example, in the scientific publishing domain test, users were willing to pay a premium for the instant on-line or FAX delivery of desired articles.

<sup>Ø</sup> Added value services that test users, identified as particularly beneficial, were the broker’s ability to provide products from multiple suppliers and the broker’s ability to offer the service 24 h<sup>r</sup>day.

The final achievement of the project was the introduction of RFC 2552 20 , which presents the<sup>w</sup> <sup>x</sup> GAIA generic architecture for information brokerage.

Uptake of the GAIA approach since completion of the project trials has been encouraging. Most notably, the Publishing Trial in Denmark has spawned a successful, commercial brokerage service. There have been other exploitations of the project, including reuse of subsystems by project partners Ž . including Search, Payment, and Directory Services , and follow-up research proposals e.g. for access to Ž Online Learning , but it is the ongoing international . brokerage service for journal articles which best highlights the principles of GAIA. The commercial service is run by the Technical Knowledge Center and Library of Denmark DTV , and now offers Ž . comprehensive coverage of articles from five major suppliers. There are 12 million records in the broker database at the time of writing, and seven user gateways serving sectors of the scientific and academic community; expansion is ongoing in both respects. The service illustrates well the supply chain benefits of brokerage in that DTV have been able to negotiate bulk discount prices on the basis of advantages offered to the supplier, thus, better serving the customer, and providing a business opportunity for the broker.

In summary, the adoption of the GAIA supplierindependent generic electronic brokerage concepts, architecture and standards presented in this paper will allow consumers and suppliers to better capitalize from the supply chain benefits which Electronic Commerce has to offer.

## Acknowledgements

This work is partly funded through the European Commission’s ACTS Programme.

## References

<sup>w</sup> <sup>x</sup> 1 M. Bichler, C. Beam, A. Segev, OFFER — a broker-centered object framework for electronic requisitioning, in: W. Lamersdorf, M. Merz Eds. , Trends in Distributed SystemsŽ .

for Electronic Commerce TrEC ’98 ,1998, p. 1402, Springer Ž . Lecture Notes in Computer Science.

2 S.J. Caughey, D.B. Ingham, P. Watson, 1998. Metabroker: A Generic Broker for Electronic Commerce. Technical Report 635, pp. 1–13, Department of Computing Science, University of Newcastle upon Tyne, March. See also http:² <sup>rr</sup> w3objects.ncl.ac.uk<sup>r</sup>pubs<sup>r</sup>mbgbec<sup>r</sup>TR635<sup>r</sup>:.

<sup>w</sup> <sup>x</sup> 3 H. Dormann, GAIA Deliverable D0202, GAIA Service and Standard Assessment,1998

<sup>w</sup> <sup>x</sup> 4 GAIA Project Deliverable D0902 to be updated as D0903 inŽ December, 98 ..

<sup>w</sup> <sup>x</sup> 5 http:<sup>rr</sup>www.omg.org.

<sup>w</sup> <sup>x</sup> 6 InfoWin ACTS Project 1998. Information Brokerage. Deutsche Telekom Berkom, Berlin.

<sup>w</sup> <sup>x</sup> 7 ISO<sup>r</sup>IEC IS 13818 Information technology — Coding of moving pictures and associated audio information, 1996, Geneva.

<sup>w</sup> <sup>x</sup> 8 D. Koutsabasis, D. Spyrou, Facilitating User–System Interaction: The GAIA Interaction Agent, HICSS, Hawaii, 1999, January.

<sup>w</sup> <sup>x</sup>9 M.J. Martin, J.E. Dobson, M.R. Strens, 1998. An Architectural Approach to Brokerage in Network Based Commerce. Department of Computing Science, University of Newcastle, Technical Report 642.

<sup>w</sup> <sup>x</sup> 10 Moules, The Middleman Always Knocks Twice, Information Strategy<sup>r</sup>Economist Group, 1998, April.

<sup>w</sup> <sup>x</sup> 11 OMG<sup>r</sup>CommerceNet 1997. Joint Electronic Commerce Whitepaper. OMG Domain Technical Committee, Monreal, See also http: ² : <sup>rr</sup>www.osm.net<sup>r</sup>upload<sup>r</sup>97-06-09.pdf .

<sup>w</sup> <sup>x</sup> 12 OMG Transaction Service: v1.1 Service Description, Nov. 1997.

<sup>w</sup> <sup>x</sup> 13 Ed.S. Plagemann, J. Hands, An enterprise model for brokerage,Guideline 3 from ACTS SIA Chain, 1997.

<sup>w</sup> <sup>x</sup> 14 RFC821, Simple Mail Transfer Protocol, J. Postel, August, 1992.

<sup>w</sup> <sup>x</sup> 15 RFC822, Standard for the format of ARPA Internet text messages, D. Crocker, August 1982.

16 RFC 959 File Transfer Protocol, October, 1985.

17 RFC1521, Multipurpose Internet Mail Extensions Part One: Mechanisms for Specifying and Describing the format of Internet Message Bodies, N. Borenstein, N. Freed, September, 1993.

<sup>w</sup> <sup>x</sup> 18 RFC 1889, RTP: A Transport Protocol for Real-Time Applications, January, 1996.

<sup>w</sup> <sup>x</sup> 19 RFC 2068<sup>r</sup>2069, HTTP v1.1, T. Berners-Lee et al. , Jan- Ž . uary, 1997.

<sup>w</sup> <sup>x</sup> 20 RFC 2552, Architecture for the Information Brokerage in the ACTS Project GAIA, M. Blinov, M. Bessonov, C. Clissmann, August, 1999.

<sup>w</sup> <sup>x</sup> 21 M. Smith, A transaction service formulated on an ODP compliant engineering platform,IFIP<sup>r</sup>ICCC Proceedings, Trondheim, Norway, June, 1966.

<sup>w</sup> <sup>x</sup> 22 Watson, Distributed Object Technology, a Key enabler for E-Commerce, TREC, Hamburg, Germany, 1998, June.

<sup>w</sup> <sup>x</sup> 23 Z39.50 Protocol Specification, The Z39.50 Maintenance Agency, http:<sup>rr</sup>lcweb.loc.gov<sup>r</sup>z3950<sup>r</sup>agency<sup>r</sup>, 1992 Library of Congress, Washington.

Jenny Hands graduated with a first class Mathematics degree and gained a PhD in Engineering Mathematics. Between 1984 and 1992, she worked as a Software consultant for PAFEC, responsible for 3D CAD developments. She joined Fretwell–Downing in 1992 to lead the GUI development and subsequently, became project leader for Open Distributed Processing applications. Between 1996 and 1999, she was Project Manager of GAIA, an EU Framework Programme collaboration involving 19 partners and some of Europe’s finest distributed systems practitioners. Currently, she is Project Manager responsible for developing FD’s integrated on-line learning and education business systems for Ufi as part of a Logica-led consortium contract for a UK-wide ICT infrastructure. This is a key initiative in the UK governement’s strategy to create a lifelong learning society, and one which expounds the principles of brokerage in the education domain.

Mikhail Bessonov received his MSc Degree in Mathematics from St.-Petersburg State University, Russia, in 1993. He is currently a postgraduate student in the Department of Computer Science at University College Dublin. His research interests include distributed information retrieval and computer networks. As a member of project technical team, he took part in the design and development of library information systems, distributed WEB search engine and streaming audio software. His current research concentrates on the use of Directory services in large-scale distributed search systems.

Mikhail Blinov is currently a full-time PhD researcher in the Department of Computer Science , UCD. He received his MSc degree from St. Petersburg State University in 1993. Prior to joining UCD, he carried out design and implementation of the multiprotocol network router for Open Systems in Russia. His research interests include stream delivery, distributed applications, network management and information brokerage.

Ahmed Patel received his MSc and PhD in Computer Science from Trinity College of Dublin in 1977 and 1984, respectively. From 1978–82, he was responsible for developing the Irish Universities Data Network, and from 1982–85, he developed the EuroKom computer conferencing and electronic mail service used by R&D projects in Europe. At University College Dublin, he is a lecturer in Computer Science and head of the Computer Networks and Distributed Systems Research Group. He is also Centre Director of Teltec Ireland, a national R&D Centre of Excellence in Telecommunications within the Department of Computer Science. He is involved in various multi-national R&D projects in ESPRIT, RACE<sup>r</sup>ACTS, INFOSEC, AIM, TELEMATICS, COST and the Irish National Telecommunications programmes. His main research interests include network management, security, protocols, performance evaluation, intelligent networks, CSCW and open distributed processing systems. He has published many technical papers and co-authored two books on computer network security and one book on group communications. He is a member of the Editorial Advisory Board of the Computer Communications and Collaborative Computing Journals.

Ron Smith received his MSc Electrical Engineering from the State University of New York at Buffalo in 1979. He has worked in international technical and management positions at Hewlett-Packard and WANG Computers. He is currently a senior consultant at KYROS in Athens, Greece. In this role, he has been involved in a number of European Research projects including GAIA, RENAISSANCE and GESTALT. His main areas of interest are Electronic Commerce, computer telephony integration and networking.
