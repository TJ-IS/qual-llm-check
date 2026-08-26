---
otero_id: 7668
otero_key: "GH5PYJSN"
title: "Virtual fab: an enabling framework and dynamic manufacturing service provision mechanism"
authors: "Yea-Huey Su; Ruey-Shan Guo; Shi-Chung Chang"
year: "2005"
journal: "Information & Management"
doi: "10.1016/j.im.2003.12.014"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# Virtual fab: an enabling framework and dynamic manufacturing service provision mechanism

Yea-Huey Su<sup>a</sup>, Ruey-Shan Guo<sup>a,\*</sup>, Shi-Chung Chang<sup>b</sup>

<sup>a</sup>Graduate Institute of Business Administration, National Taiwan University, No. 1, Sec. 4, Roosevelt Road, Taipei 106, Taiwan <sup>b</sup>Department of Electrical Engineering, National Taiwan University., Taipei 106, Taiwan

Accepted 27 December 2003 Available online 2 April 2004

## Abstract

The concepts of a virtual fab (VF) and manufacturing service (MS) have been proposed over recent years as a way to face the fierce competition of the semiconductor industry. This paper proposes a way to build a VF with a flexible manufacturing service in a highly specialized and uncertain environment. The VF enabling framework contains manufacturing service, business process (BP), and infrastructure (IR) layers. A novel dynamic manufacturing service provision mechanism (DMSPM) was designed to compose objects flexibly among the three layers of the various manufacturing services. The skeleton of the scheme includes name mapping, business process binding, resource reservation binding, and manufacturing service management binding to allow flexible service composition. To assess the feasibility and potential of the framework and our DMSPM, an order commitment service (OCS) provided by a foundry fab was used as an example. A prototype system was designed and implemented to demonstrate that current IT, CASE tools, a fab information infrastructure, and data/information availability make DMSPM readily realizable and that it has good possibilities in VF and e-business developments. <sup>#</sup> 2004 Elsevier B.V. All rights reserved

Keywords: Manufacturing service; Virtual fab (VF); Enabling framework; Object-oriented technology; Dynamic manufacturing service provision mechanism (DMSPM); Order commitment service (OCS)

## 1. Introduction

1.1. Evolution of business model in the semiconductor industry

In the semiconductor industry, although the unit price per integrated circuit (IC) device continues to reduce, costs for building a new IC fab increase [37]. Only a few companies have the ability to build a fab with reasonable financial returns. Meanwhile, customers are demanding more and more advanced fabrication capabilities. Customers now demand a reduction in manufacturing cycle time with high yield and this has impacted the entire supply chain of the semiconductor industry. Therefore, the risk of running a fab has increased significantly due to its high capital investment and the dynamic situation. Industry has responded to high risk by attempting to use several business strategies, such as strategic alliances and a dedicated foundry fab; this has led to the evolution of a business model in the semiconductor industry.

The computer/electronics industry has changed from being vertically integrated to vertical disintegration [22]. In the semiconductor industry, vertically integrated firms (integrated device manufacturers (IDM)) like Intel, IBM, and Motorola have dominated the market across all segments of manufacturing. But since 1987, under the rapid growth of fabless designhouses (see Fig. 1), the increasing capital intensity of building a fab, and the decreasing technology life cycle in IC products and process technology, the dedicated foundry fabs have started to use a different specialized business model, as shown in Fig. 2. Compared to the specialization and division of labor in other computer-related industries, the semiconductor industry is functional—rather than component-based: thus the nature of disintegration in the semiconductor industry is that the departments of IC design, manufacturing, testing, and assembly (originally in a single IDM) have separated into several firms.

![](/api/attachments/GH5PYJSN/fulltext/images/877d66b7d462605eba76a96dc96d8c07ba7caa49093b656b90eecbacdb2c89b4.jpg)  
Fig. 1. Growth of number of fabless design-houses worldwide [24].

The foundry/fabless model [24] is the core of the vertical disintegration structure in the semiconductor industry. In this, foundry fabs focus their core competency on manufacturing capability and are able to provide services to many fabless design-houses and system companies because of their economies of scale. On the one hand, some foundry companies have tried to enhance their service by helping customers provide their own back-end activities, such as assembly and testing. On the other hand, fabless design-houses focus their core competency on product innovation and regard foundry fabs as their manufacturing partners. Design-houses, therefore, significantly reduce their capital investment and are able to concentrate their core competencies by accessing production capacity from outside efficient foundry fabs.

Under this vertical disintegration structure, foundry business has experienced a significant growth. It has been estimated that 10% of worldwide production volume was provided by foundry fabs in 1999, and this is expected to increase to more than 25% in the coming years (Fig. 3) [3]. The achievements of the foundry/fabless model have contributed to further disintegration in IC manufacturing. There is no doubt that, in future, the foundry business will take a larger share in IC supply and competition among the foundry will get fiercer [49].

## 1.2. From foundry fab to virtual fab

In spite of the great opportunities of growth, foundry fabs are facing critical challenges. On the business side, the fast growth in the number of foundry fabs leads to more competition and shrinking profit margins [16]. The industry is changing from regional to global [38]. This trend extends customers’ ‘‘choicespace’’ of suppliers. They expect on-time delivery of high-quality customized products at prices reflective of high-volume manufacturing costs plus great service. It is even more important for foundry fabs to provide services to satisfy the increased customer expectations—faster, cheaper, better, and more customized. Moreover, the rapid advancements in IT and Internet applications are dramatically changing the whole business into a service economy. In contrast to transactional manufacturing operations that are isolated or buffered from the customers, manufacturing firms must now deal with an environment in which the customers become part of the production processes. Consequently, a ‘‘manufacturing service (MS)’’ concept will arise to move activities into services. Manufacturing firms must pursue ever-greater flexibility so that they can provide more services to their customers [18].

![](/api/attachments/GH5PYJSN/fulltext/images/4679ffdda082a9391885c1840d3b80baa64338e9e4597e99e0acf2302df31cd2.jpg)  
Fig. 2. (a and b) Evolution of business model in the semiconductor industry [24].

![](/api/attachments/GH5PYJSN/fulltext/images/5a70b522cc8207b4f5a1998c567a8886d66351de64d583696f94bf9390e7d8ad.jpg)  
Fig. 3. Growth of foundry business in percentage worldwide [3].

On the technology side, the development of the system-on-a-chip [20] and the increasingly expensive R&D on product innovation and process technology development require foundry fabs to build their capacity to support customers’ competitive product design and development. This transition is illustrated in Fig. 4; the first part depicts the earlier basic business model, where fabless design-houses and IDMs outsource their full or partial manufacturing functions, such as mask set generation, wafer fabrication, testing, and assembly to the foundry fabs. Along with the evolution of IT and fab automation for functions/firms integration, services such as one-stop or back-end turnkey services have gradually been included into the business model of the foundry fab. Fig. 4(b) depicts the latest servicedriven model, where foundry fabs also collaborate closely with intellectual property providers and third-party design service companies to provide customers with product design libraries and design verification services so that customers can quickly and easily ‘‘design for manufacturing’’ [7].

In order to meet the new challenges, a foundry fab has to adopt new strategies and more efficient methods. The value-added activities cannot be analyzed in the same way as the traditional manufacturing model. A service-driven business model that provides customers with manufacturing services in addition to manufacturing capability must be in-place under the new service economy. As a result, the idea of a ‘‘virtual fab (VF)’’ (in which a foundry fab provides integrated manufacturing services to its customers as if this foundry fab were the customer’s own fab) has been proposed as one of the critical needs for achieving competitiveness.

![](/api/attachments/GH5PYJSN/fulltext/images/444ef3e91e88ee5587171f1a0953f7199bed88e4db6fb22b157f443e8dab1d7d.jpg)  
(a) Manufacturing-driven foundry fab model

![](/api/attachments/GH5PYJSN/fulltext/images/d9cd9a44e4132fbefe06fd1ed580e5ab3356fe1c2325bbb01d64a553a8353370.jpg)  
(b) Service-driven virtual fab model  
Fig. 4. (a and b) Evolution of foundry business model [49].

Product Design

<table><tr><td rowspan="3">Process Design</td><td rowspan="3">New Existing</td><td>Existing</td><td>New</td></tr><tr><td>intensive</td><td>most intensive</td></tr><tr><td>minimum</td><td>medium</td></tr></table>

Fig. 5. Interactions between product and process development.

The VF must facilitate intensive interaction between the foundry fabs and their customers, including fabless design-houses, system vendors, or IDMs. Fig. 5 depicts four levels of interaction. These are at the minimum level when only existing process technologies and product designs are involved and are most intensive when new designs of product and of process technologies are being concurrently developed. To reduce the costs of interactions in searching, communications, and monitoring, a new virtually integrated approach is needed for linking a foundry fab and its partners (as if they were in a single firm) to facilitate a seamless relationship between the foundry fab and its customers.

## 1.3. Major design issues of the VF

Flexibility, speed, and transparency of manufacturing service provision are three key effects needed by a foundry fab in developing its internal VF environment. In spite of the attraction and significance of VF concepts, the definition and ways to achieve them remains either ambiguous or confusing to most practitioners. The issues discussed here are therefore:

(1) providing definitions of VF and manufacturing services,

(2) providing a VF enabling framework as a foundation for flexible and quick providing of manufacturing services,

(3) developing a dynamic manufacturing service provision mechanism (DMSPM) based on the VF enabling framework, and

(4) assessing the feasibility and merits of the designs by using an order commitment service (OCS) as a carrier.

## 2. Definition of virtual fab and manufacturing service

## 2.1. Elements of the virtual environment

Based on our study of the literature, the elements of a virtual environment are: separation, transparency, simulation, and customization.

Separation implies that a person can be independent of time and/or space within the environment; i.e., one may be involved with an activity without being physically on-site or working at the same time. Moreover, the concept can be applied to tangible and intangible entities and it is usually intended to increase performance or efficiency of the process. The application of electronic data interchange (EDI) [2] was based on the idea of separating information from the flow of goods [5]. Meanwhile, partners in the team of experts [1] who provided services to customers were organizationally separated but treated as though they belonged to a single organization.

Transparency refers to the ability to access resources without physically owning them [51]. To be more specific, an information provider must design a system so that users at different locations, on different platforms, and using different application tools, can access information without difficulty and feel as though he or she owns the information. Transparency also refers to collaboration or partnership with external organizations [13,34]. Information sharing is a key to integration of a supply chain. A knowledge network must be created for dynamic interaction and quick response to specific requests or problems [25].

Simulation involves imitating the real-world facilities or processes (the system) [29]. In an IC fabrication scenario, this can be a device, a process, or the entire factory. For example, a manufacturing firm that is contemplating building a large extension to one of its plants but is not sure if the potential gain in productivity must first justify the cost. A careful simulation study could shed light by determining the operation of the plant as it currently exists and as it would be if the plant were expanded.

Customization refers to the flexibility of the system to fit different users’ needs in a dynamic environment [21]. This has two implications. To the users, it requires special interfaces specifically designed to satisfy their needs. To the system designers, the system itself must be flexible enough to adjust its internal operations dynamically to respond to external needs. Based on needs, customers will thus be able to require different kinds of products (e.g. wafer, probed wafer, or packaged IC) and services (e.g. material to be directly delivered to the customer’s customers).

## 2.2. Various views and definition of virtual fab

Table 1 lists some existing views of VF. From the strategic management perspective, TSMC defines the virtual fab as the customer’s fab [48]. Moreover, the UMC Group has developed the Virtual Foundry Consultant to help its customers match their needs with the technology and service available [50]. To satisfy many customers, however, the physical fab must provide customized services and mixed products by dynamically changing operation and capacity configuration. Quality of service is guaranteed by advanced technology, high yield, sufficient capacity, rapid and on-time delivery, and design support service [27].

From the manufacturing engineering perspective, Stanford University perceived a VF as a simulated fab to run in parallel with or in front of the actual fab for fast processing, product, and operation development [32]. The Semiconductor Industry Association (SIA) further proposed the integration of the fabrication facility and its associated suppliers throughout all steps of semiconductor device manufacturing from product development through product shipment [45].

Intel, from the technology transfer perspective, proposed the ‘‘copy exactly’’ concept [35]. This requires that systems are developed in order to minimize the time required for technology transfer and to ensure product quality and yield. During the course of technology transfer, ‘‘everything which might affect the process, or how it is run’’ is copied down to the finest detail, unless it is either physically impossible to do so or there is an overwhelming competitive benefit in introducing a change. This approach introduces new processes or products into the production cycle but should not be applied during technology development, which requires creativity and innovation [4].

Having explored the elements of a virtual environment and various views of VF, we consider it from the perspective of manufacturing service. A VF is thus a manufacturing service environment (or system) that provides transparent services and simulations of a foundry fab to internal or external users, who are separated from the real entity in space and or time, with open and easy access and real-time response to user specific needs.

In the new business model, manufacturing services and partnerships are the key concepts. All four virtual aspects are captured in our VF model.

## 2.3. Manufacturing service for a virtual fab

Fig. 6 depicts the value chain and service delivery model in a service-driven manufacturing firm. Manufacturing service provision includes the delivery of both tangible and intangible products. Tangible products are real entities, such as probed wafers or packaged dies. In the traditional foundry fab model, the tangible products represent most of the value delivered to customers. In a manufacturing servicedriven VF model, however, they are the minimum requirements of customers. Additional intangible products must be created and delivered as part of the manufacturing service. Here, intangible products result from customers’ involvement in the manufacturing processes or the value-added functions from the customers’ perspective. Thus the tightly coupled, concurrent interactions between manufacturers and customers create a new manufacturing service.

Table 1 Various views of virtual fab

<table><tr><td rowspan="2"></td><td rowspan="2">Key concept</td><td colspan="4">Nature of virtuality</td></tr><tr><td>Separation</td><td>Transparency</td><td>Simulation</td><td>Customization</td></tr><tr><td rowspan="2">Strategic management</td><td>Customer&#x27;s fab</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Virtual foundry consultant</td><td></td><td>√</td><td>√</td><td>√</td></tr><tr><td rowspan="2">Manufacturing engineering</td><td>Simulated fab</td><td></td><td></td><td>√</td><td></td></tr><tr><td>Factory integration</td><td>√</td><td></td><td>√</td><td></td></tr><tr><td>Technology transfer management</td><td>Copy exactly</td><td>√</td><td></td><td>√</td><td></td></tr><tr><td>Manufacturing services</td><td>Service and partnership</td><td>√</td><td>√</td><td>√</td><td>√</td></tr></table>

![](/api/attachments/GH5PYJSN/fulltext/images/0349ffe3892c3af83cb67ae7fe7e174ca181815268bcc1ca0a7c9406d60ff72d.jpg)  
Fig. 6. Value chain and service delivery model.

Table 2  
Types of manufacturing services for a virtual fab

<table><tr><td rowspan="2">Product type</td><td colspan="2">Interaction pattern</td></tr><tr><td>Technology-driven service</td><td>Logistics-driven service</td></tr><tr><td rowspan="9">Intangible products</td><td>IP/library usage</td><td>Capacity reservation</td></tr><tr><td>Technology catalog</td><td>Due-date quote</td></tr><tr><td>Advanced technology</td><td>Order status checking</td></tr><tr><td>Qualification</td><td>On-time delivery</td></tr><tr><td>Yield data access</td><td>Exception handling</td></tr><tr><td>Failure cause analysis</td><td>Quick response</td></tr><tr><td></td><td>Turnkey service</td></tr><tr><td></td><td>Wafer acceptance test data access</td></tr><tr><td></td><td>Yield data access</td></tr><tr><td rowspan="3">Tangible products</td><td>Wafer</td><td></td></tr><tr><td>Probed wafers</td><td></td></tr><tr><td>Packaged dies</td><td></td></tr></table>

Table 2 provides several examples of manufacturing services for a VF: here we further classify intangible products into two types of service based on the interaction patterns between the VF and the customers: technology- and logistics-driven services.

## 3. The three-layered virtual fab enabling framework

To provide manufacturing services in a highly specialized and uncertain environment, the resources and business processes (BP) of a VF must be easily reconfigurable in a systematic way. Therefore, we propose a three-layered virtual fab enabling framework based on the concepts of object-oriented methodology [14] and a layered architecture [46]. Here the concept of object-oriented (OO) methodology is useful because of its flexibility, reusability, scalability, and expandability [52]. For example, SEMATECH proposed a CIM application framework based on an objectoriented model to provide a technological guideline to establish a common environment for the integration of applications and sharing of information in semiconductor manufacturing [42].

In Fig. 6, we see a value chain and service delivery model in which manufacturing services, both tangible and intangible, are delivered to customers through the configuration of business processes and manufacturing resources. Here, a business process is defined as a structured, measured set of activities designed to perform a specified output [12].

In proposing a VF enabling framework, it is natural to map the three-layered service delivery model into a three-layered framework. Fig. 7 shows the proposed three-layered framework; it contains the manufacturing service (MS) layer, business process (BP) layer, and infrastructure (IR) layer. The three layers work together in providing a manufacturing service but with different specialization. From the customers’ standpoints, the MS layer works as an interface to establish a customer’s request, while the BP and IR layers work together to implement the request. Note that the VF enabling framework itself is not a specific system; it only tells what each layer should do.

![](/api/attachments/GH5PYJSN/fulltext/images/69c4de21bafa4784a964d7e35d6d65dca02fe306e61c9e457d4941787257302b.jpg)  
Fig. 7. Three-layered VF: an enabling framework.

![](/api/attachments/GH5PYJSN/fulltext/images/c403d919311af7818e463ac7b1f2c3d7b34a6697b1bac42d7e888835c624c44b.jpg)  
Fig. 8. Cooperation of three layers for manufacturing services provision.

Details of each layer consist of objects that are abstracted based on the object-oriented approach for modeling the fab [44]. The generic principle of how the three layers cooperate to provide manufacturing services to customers is depicted in Fig. 8. Conceptually, each layer consists of two types: operator and manager objects. The operator objects carry out the provision of manufacturing services, while the manager objects perform either an administration or coordination task. The administration task involves the supervision of operator objects’ performance in order to guarantee the quality of manufacturing services within its own layer. The coordination task involves the coordination of manager objects across different layers in order to make sure that objects in the three layers work together properly. This design facilitates flexible provision of manufacturing services, where objects can be easily added or deleted to modify or compose manufacturing services without changing the framework.

## 3.1. Manufacturing service layer

The manufacturing service (MS) layer is concerned with the transformation of manufacturing services between the customers and a VF. The main tasks in this include accepting an MS request from customers, determining which objects of this layer are responsible for that request, creating new objects if no object is able to handle the request properly, mapping the external requests into internal service requirements, and passing them to the business process (BP) layer. On the other hand, the main tasks in the transformation include accepting the accomplished manufacturing service from the BP layer, and passing this managed manufacturing service to customers.

In order to accomplish the tasks, objects of the MS layer have to perform four main functions: interface, decomposition/composition, creation, and management. The interface function accepts and interprets service requests from customers and delivers manufacturing services to them. The decomposition function decomposes the requested services into business processes to be performed at the next business process layer. The composition function then integrates business processes, based on service requirements, into manufacturing services. The creation function produces new objects when necessary. Finally, the management function ensures that the manufacturing services guarantee quality. For each type of manufacturing service, the management function determines if different types of processes result in different levels of customer involvement and quality of service [33].

## 3.2. Business process layer

The BP layer gathers all the associated objects together to fulfill requirements from the MS layer. To provide flexible manufacturing services, business processes have to be reusable for different manufacturing services or other business processes can be dynamically configured.

Objects of the BP layer perform two main functions: configuration and creation. The configuration function arranges a group of objects to work together. That is, after receiving an internal service requirement from the MS layer, objects in the BP layer work as a controller to split it up into several activities that can be performed via cooperation of associated objects in the IR or BP layer. An object in the BP layer configures related objects by sending messages to them: they act as activity controllers while objects of the IR layer act as activity executors to carry out manufacturing service requests. The creation function creates new objects if none exists.

## 3.3. Infrastructure layer

The IR layer contains the resources to support the top two layers in providing manufacturing services. Objects are modeled from the concrete entities in a fab. The SEMATECH CIM application framework [43] can be utilized as a foundation of the infrastructure layer of the VF enabling framework. As a result, the IR layer consists of two parts: a physical and logical fab. A physical fab can be modeled by a logical fab through one-to-one mapping. This concept was also adopted in the MMST project [36], in which a distributed object-oriented CIM architecture was proposed.

In a VF environment, three resource components are identified as the key components of the physical fab. These include data-warehouse-server [10,19], open real-time simulation server [23,47], and the dynamic manufacturing service provision mechanism server. The data warehouse filters or summarizes data to users for decision support [39]; it must be set up in the early phase of the VF construction. An open realtime simulation server provides a real-time simulation environment where simulation resources are open to customer access.

## 4. Dynamic manufacturing service provision mechanism (DMSPM)

The control mechanism, called the dynamic manufacturing service provision mechanism (DMSPM), enables cooperation of objects with different roles among the three layers. It is utilized to break down required manufacturing services from customers and flexibly link related objects of business processes and logical/physical resources in order to fulfill the manufacturing services. To accomplish this, the concept of object binding [30] is utilized.

![](/api/attachments/GH5PYJSN/fulltext/images/bedef9d0ad9b2db7e11e5fcb47aa13d05cc7e423e06a5dbb8b538dab821cd7cb.jpg)  
Fig. 9. The concept of binding.

Fig. 9 illustrates this. Upon a well-defined OO fab model, the DMSPM utilizes binding in two phases. First, in the service creation phase, specific objects are associated with each other, according to their relationships, to fulfill a requested service. These relationships, either inter- or intra-layer objects, are planned when modeling a fab and are designed when new services are requested. Second, in the service execution phase, those associated objects are activated by messages passing among objects to deliver the requested manufacturing service. After providing the service, the associated objects are released for activation. In brief, object binding implies the concept of dynamic configuration in order to flexibly provide manufacturing services.

Using the binding model of Lazar et al. [31], Chang et al. [8] designed a dynamic binding mechanism for manufacturing service creation with guaranteed service quality. By distinguishing the salient needs between service creation and execution phases, the dynamic binding mechanism was further refined into the DMSPM. The expandability of the binding mechanism and reusability of objects can be employed to construct it. Now we shall consider a virtual fab environment built on a three-layered VF enabling framework over an object-oriented fab model [17].

![](/api/attachments/GH5PYJSN/fulltext/images/869d23183ceaa341d644d18f8b81f3314500d61c5fdaf2d2ea5e56640a8ea31c.jpg)  
Fig. 10. Manufacturing service provision skeleton.

## 4.1. Manufacturing service provision skeleton

The DMSPM exploits the OO abstraction of a fab and is service process driven. Compared with the traditional functional description model of a fab, the OO based fab model in the VF enabling framework not only indicates what should be done but also specifies who should do it by assigning tasks to objects. Moreover, our VF enabling framework separates real entities and logical entities for flexibility by distributing objects in the three layers. This organization of entities of resources, processes, and information [53] is flexible for re-configuration for different requirements.

The DMSPM can bind or configure a set of objects by modeling the entities or states in a fab into manufacturing services in a flexible way. Inputs of the DMSPM are manufacturing service requirements from customers and its outputs are the managed manufacturing services. According to the associating and activating concept of object binding, the process of providing manufacturing services in the DMSPM is broken into two sequential phases: creation and execution. As shown in Fig. 10, a skeleton of the DMSPM is extracted from the procedural commonality of the two phases. There are four steps in the skeleton: name mapping, business process binding, resource reservation binding, and manufacturing service management binding. The functions are:

![](/api/attachments/GH5PYJSN/fulltext/images/37fc71703f0ef0cf45540c1ec1e3b5346f2ba8b6661cdab0e2df6169fea4f751.jpg)  
Fig. 11. Application of DMSPM in VF: an enabling framework.

## (1) The creation phase:

\- Name mapping: This automatically translates an external manufacturing service request into a specification expressed in internally recognizable terms and thus it creates an internal service requirement.

\- Business processes binding: This associates business process objects through its internal service requirement and thereby generates workflow, which consists of sequences of activities with various resource requirements.

\- Resource reservation binding: This associates required resource objects to workflow. It reserves and schedules the necessary resources and thereby creates a fab service plan via functions such as resource registration, production planning, and scheduling.

\- Manufacturing service management binding: This associates managerial activities and resources to the fab service plan to become a managed service plan.

(2) The execution phase:

\- Business processes binding: This activates individual BPs and carries out the control of workflow according to the service plan.

\- Resource reservation binding: This activates resource usage in accordance with the BP requirements.

![](/api/attachments/GH5PYJSN/fulltext/images/4ad1d31a9925595e582e61bb0596af93291300ec31dc510448562a95de9eca93.jpg)  
Fig. 12. Order commitment service workflow.

\- Manufacturing service management binding: This activates the managerial activities in each layer and thereby generates a managed manufacturing service to the customer.

## 4.2. Application of DMSPM in VF enabling framework

Fig. 11 illustrates how the DMSPM is applied in a VF enabling framework, i.e., how the skeleton steps bind objects of individual layers into a manufacturing service. In this figure, arrows represent the direction of interaction while the associated numbers represent the procedural sequence of the DMSPM. For example, a customer requests manufacturing service via the interface object in the MS layer. After name mapping, the DMSPM further binds objects in the BP layer accordingly to generate workflow for the manufacturing service. The DMSPM then binds resources in the IR layer to each BP object, etc.

Note that the DMSPM may provide flexible reconfiguration of manufacturing services in the VF enabling framework in two ways. First, an object can be easily modified, added into or deleted from a fab model, and changes of a fab or customer requirements can then be captured in a service plan without changing the DMSPM. In other words, it can easily respond to changes. Second, as an object is bound for activation only when needed, it allows both binding by multiple services at different times and binding based on the actual progress of a service.

Commercial object-relational DBMS products [55] are available to store all the objects of fab models, together with their relationship and behavior, in a database. The binding actions or dynamic linkage can be implemented via object-oriented programming and the corresponding CASE tool [40]. Moreover, the techniques of run-anywhere web and one-to-one tool [6,54] are well developed for manufacturing service interface. The bill of material processor [28], customized interpreter, standardized data exchange, and name translator [15] are used to fulfill name mapping. An in-house developed or commercial scheduling/ planning tool can be used to perform the resource reservation binding. For example, a commercial ERP system [26] could be used to perform production planning or scheduling to calculate resource quantity and time to be reserved for quality of service. Finally, the project management [11] function is included in the manufacturing service to monitor service, quality, cost, and time to fulfill manufacturing services management binding and then to complete the DMSPM.

![](/api/attachments/GH5PYJSN/fulltext/images/65f431425db59e4806b485984f21984af667003a895545ac9f473c5bdf056e46.jpg)  
Fig. 13. Relationships among objects for OCS provision.

## 5. Applying DMSPM to order commitment service

To explain the ideas and to assess the practicality of the DMSPM, we use a simplified order commitment service (OCS) as an example.

## 5.1. Three-layered model of an OCS

The OCS aims at quick and accurate commitment of delivery once customers place their orders. Fig. 12 shows an abstract workflow, which is extracted from the practices of two leading foundry service providers, TSMC and UMC, and it is called the available-topromise service. As shown in Fig. 12, after receiving customers’ orders, the sales department sets a priority to each order in conjunction with the production planning (PP) department. Based on the priority and quantity requirements of an order, PP makes a wafer-out-plan for the order by calculating its capacity requirements, checking residual capacity of fabs under the ongoing production schedule, allocating the available capacity, and scheduling resource reservation and the due date. The workflow finally confirms the due date with individual customers to complete the OCS procedures. A good OCS must quickly provide customers with credible and short cycle-timed delivery schedules and transparent business processes.

To apply a DMSPM skeleton to OCS under the VF enabling framework, we first model its workflow into an object-oriented model. The class diagram of UML [41] is utilized to model the static design view of the OCS in our VF enabling framework. Fig. 13 indicates this three-layered, object-oriented abstraction of OCS workflow. Both real entities and logical entities of

![](/api/attachments/GH5PYJSN/fulltext/images/70f9bd09d9a04f139bd4e1849907c5fa8d11431b714a69cc7a71ae2069868ea5.jpg)  
Fig. 14. Sequences diagram of DMSPM in OCS provision.

Fig. 12 are modeled as objects in Fig. 13. For example, the sales-staff object is abstracted from real entities of a fab while the wafer-out-plan-BP object models a sub-flow of OCS workflow which is a logical entity.

![](/api/attachments/GH5PYJSN/fulltext/images/49bc49c95347b0955cbf7430fad24db02e3e5b07ddad94eded3698b9e012d90f.jpg)  
Fig. 15. Name mapping for OCS.

The relationships among objects are also shown. In order to reduce visual complexity, all UML-defined relationships are simplified into two types of straight line: a solid one indicates the existence of a relationship between two intra-layer objects, while a dashed one a relationship between two inter-layer objects. For instance, the OCS–BP object associates other BP objects in the same layer, such as the wafer-out-plan-BP, which in turn associates other objects such as the capacityallocation in the BP layer and the resource objects in the infrastructure layer, such as the PP-staff, the planningtool-server, and the data-warehouse-server objects.

![](/api/attachments/GH5PYJSN/fulltext/images/f9c8cfbc2d5ba176481338c571b42daf5b59e7d89446f92913f8efb41d9f147a.jpg)  
Fig. 16. Business process binding for OCS.

## 5.2. Applying DMSPM skeleton to OCS

Fig. 14 illustrates the overall flow of the DMSPM— howitcomposesanOCSontheVFenablingframework. Objects of each layer have one of two roles: operator or manager. In Fig. 13, the shadowed objects are manager objects while the others are operator objects. For conciseness, without sacrificing the key concepts we aggregate objects in each layer into a generic manager object and a generic operator object to illustrate the application of DMSPM to OCS. All specific objects in Fig. 13 have to inherit from either the generic operator object or the generic manager object. By utilizing the sequence diagram of UML, Fig. 14 indicates the DMSPM step sequences of creation and execution phases for OCS provision.

Examples of OCS provision steps are as follows:

1. Name mapping: Consider as an example, an OCS provision process in a foundry company XYZ with five fabs. A customer NTU places an order at 11:00 a.m. on day-1 requesting 235 wafers of DRAM in 0.25 technology with a due date of day-40. Fig. 15 indicates the name mapping for OCS in the MS layer.

![](/api/attachments/GH5PYJSN/fulltext/images/f425c51bf7c3c7d9f7d1d58f2129895b47247d086383169df84e53bbff30a997.jpg)  
Fig. 17. Resource reservation binding for OCS.

2. Business process binding: Objects in the MS layer and the BP layer both conduct business process binding. As shown in Fig. 16, in the MS layer, after checking the technological feasibility from tables, the OCS–MS object assigns this order to Fab 1 of foundry company XYZ and out-sources backend processing to company G. The OCS–MS object then links objects in the BP layer by sending a message with parameter ‘‘Fab $1 ^ { \circ }$ to the OCS–BP object and a message with parameter ‘‘company $\mathbf { G } ^ { \ast }$ to the backend-outsourcing-BP object.

In the BP layer, a major task of the OCS–BP is to generate the workflow for service fulfillment. By utilizing a UML activity diagram, the OCS workflow is first modeled as a sequence of activities and saved within the OCS–BP object. After receiving messages from the OCS–MS object in the MS layer, the OCS–BP object invokes each activity to bind its associated objects, such as the sub-business processes or rules.

![](/api/attachments/GH5PYJSN/fulltext/images/523d0299f19b841f4f34bb264a42a7d61de1c6eb4e7574f2ac7eb4bb26fdd058.jpg)  
Fig. 18. Manufacturing service management binding for OCS and outputs of DMSPM.

3. Resource reservation binding: As shown in Fig. 17, once the workflow in the business process layer is complete, the associated resources in the infrastructure layer must be scheduled and reserved to satisfy a fab service plan. The fab service plan, consisting of the planning results of the equipment resources along with the staff and tool resources, will then be completed.

4. Manufacturing service management binding: Fig. 18 illustrates the steps of the manufacturing service management binding. The manager objects in each layer are first linked to their associated operator objects and then to their adjacent-layered manager objects for necessary coordination or negotiation between layers.

Fig. 19 further illustrates a specific example of manufacturing service management binding in the BP layer. In the creation phase, after receiving messages from the OCS–BP object, the BPmanager object adds the management activities in order to ensure on-time delivery in each decomposed process stage. Management activities and performance metrics, such as each stage’s lead or delivery time, are bound into the fab service plan. In the execution phase, this BP-manager object monitors these performance metrics and sends a message to the MS-manager or servermanager object if coordination between layers is required.

Finally, the outputs of the managed OCS include the dates (committed due date and planned wafer start date) and the internal waferout-plans (production and resource reservation plan). The OCS date is delivered to customers via the external interface and the internal waferout-plan is delivered to the fab’s production-plan department via the internal interface. Whether the wafer-out-plan is or is not delivered to customers depends on the business policy of individual fabs. The user interface can work as an information filter to implement this business policy.

![](/api/attachments/GH5PYJSN/fulltext/images/4b1c6837f22ad9a0c6f0af9198b0af4139d0672d47b3a3fbc55ff8d7c35d8893.jpg)  
Fig. 19. A specific example of manufacturing service management binding for OCS: management binding of the BP-manager object.

![](/api/attachments/GH5PYJSN/fulltext/images/4556325ab30faf96f3fe84288faefae058d8b0cf0f69cd133f205206e5dac178.jpg)  
Fig. 20. Prototype system of DMSPM in OCS.

## 5.3. Prototype of DMSPM in OCS

To realize the DMSPM in the OCS application, a prototype system was designed and implemented [9]. Fig. 20 depicts the system architecture which was composed of a browser client, a web server, the DMSPM server, and the VF database. Rational ROSE was used as our CASE tool for both OO modeling of OCS in terms of UML and Cþþ code skeleton generation. The DMSPM server was coded in Cþþ. The DMSPM server implemented the common steps of the DMSPM skeleton for the creation and execution phases for OCS provision. Although the manager objects were Cþþ codes in the prototype, they could be human decision-makers in a real application.

In our prototype development, it was found that input data and/or information to the DMSPM were mostly available from the IS of the fab and its company. Most business process documents were available in the company, passing ISO 9000 verification, but they may have to be computerized in the actual implementation. The inputs to OCS included order quantity, product type, technology, and expected due date. while the outputs included the committed due date and waferout-plan. Our experiment demonstrated both the ideas and the potential of the DMSPM for use in virtual fab and e-business developments.

## 6. Conclusions

Fast growth of the foundry business, fierce global competition, and advancements in the use of IT have recently made VF one of the critical ways of achieving competitiveness in the semiconductor industry. One exiting definition makes a foundry fab the equivalent of the customers’ own fab: this leads to a serviceoriented business model with emphasis on excellent manufacturing service. Such a flexible service in a highly specialized and uncertain environment becomes a driving force for the development of a VF.

This paper, identified the critical demands for a VF and manufacturing service under a service-driven business model. Based on the demands, it further defined the VF, together with the manufacturing service, and proposed a VF enabling framework. Our prototype implementation of DMSPM in the OCS application demonstrated the following cases:

(1) The ideas are feasible under current fab practice.

(2) The VF enabling framework and DMSPM should have potential for application in the e-business of foundry fabs; i.e., in an industry where economies of scale and swift change of service are demanded.

## Acknowledgements

The work presented in this paper came from the help of many people and organizations. Firstly, this research was supported in part by the National Science Council of Taiwan under grants NSC-86-2622-E-002-025R, NSC872622-E022-011, NSC89-2212-E-002-040, NSC-89-2218-E-002-009, and NSC89-2213-E002-119. The authors deeply thank all practitioners in the semiconductor industry of Taiwan, who gave us many valuable suggestions with practical experiences via in-depth interview in the past few years. The authors would also like to thank the students in Department of Electrical Engineering at National Taiwan University, Steven Yuan-Wei Li, Tsung-Lian Chou, and Yi-Chang Lai, for their participation in the early stage of this research.

## References

[1] M. Athans, The expert team of experts approach to command-and-control (C2) organizations, IEEE Control Systems Magazine, September 1982, pp. 30–38.

[2] S. Banerjee, D.Y. Golhar, Electronic data interchange: characteristics of users and nonusers, Information & Management 26, 1994, pp. 65–74.

[3] S. Billat, Outlook for foundries and semiconductor equipment industry, in: Keynote Speech in the Seventh International Symposium on Semiconductor Manufacturing, Santa Clara, CA, USA, 11–13 October 1999.

[4] J. Bisgrove, et al., Integrated test facility: automation testing to support Intel manufacturing output, in: Proceedings of the Sixth International Symposium on Semiconductor Manufacturing, San Francisco, USA, 6–8 October 1997, pp. D17–D21.

[5] S.P. Brandey, J.A. Hausman, R.L. Nolan, Globalization, Technology, and Competition, Harvard Business School Press, Boston, 1993.

[6] BroadVision Inc., Broadvision at-a-glance, 2000, available at URL: http://www.broadvision.com.

[7] D.E. Carter, B.S. Baker, Concurrent Engineering: The Product Development Environment for the 1990s, Addison-Wesley, New York, 1992.

[8] S.C. Chang, T.L. Chou, R.S. Guo, Y.H. Su, L.L. Lu, I.C. Lai, A dynamic binding model for service creation in virtual fab, in: Proceedings of the 1998 Semiconductor Manufacturing Technology Workshop, Hsinchu Taiwan, 16–17 June 1998, pp. 131–138.

[9] S.C. Chang, R.S. Guo, Y.H. Su, I.C. Lai, Realizing dynamic manufacturing service provisioning mechanism in order commitment service, in: Proceedings of the Ninth International Symposium on Semiconductor Manufacturing, Tokyo Japan, 26–28 September 2000, pp. 25–28.

[10] D.N. Chorafas, Manufacturing Database and Computer Integrated Systems, CRC Press, Boca Raton, FL, 1993.

[11] K.B. Clark, S.C. Wheelwright, Managing New Product and Process Development, The Free Press, New York, 1993.

[12] T.H. Davenport, Process Innovation: Reengineering Work through Information Technology, Harvard Business School Press, Boston, 1993.

[13] W.H. Davidow, M.S. Malone, The Virtual Corporation: Structuring and Revitalizing the Corporation for the 21st Century, HarperCollins Publisher, London, 1993.

[14] B. Eckel, Thinking in Java, second ed., Prentice-Hall, NJ, 2000.

[15] M.A. Emmelhainz, Electronic Data Interchange: A Total Management Guide, second ed., Van Nostrand Reinhold, New York, 1993.

[16] ERSO/ITRI, What you wish to know about Taiwan semiconductor industry, 1999, Available at URL: http://www.tsia. org.tw/ICIndustry1999.htm.

[17] ESPRIT/AMICE, CIMOSA: Open System Architecture for CIM, Springer-Verlag, Berlin, 1993.

[18] J.A. Fitzsimmons, M.J. Fitzsimmons, Service Management: Operations, Strategy, and Information Technology, second ed., McGraw-Hill, New York, 1998.

[19] S.T. Gelman, W.D. Peck, Bringing business information to AT&T network systems through a data warehouse, AT&T Technical Journal March–April (1996) 68–78.

[20] L. Geppert, The100-million-transistor IC, IEEE Spectrum 36 (7), 1999, pp. 22–24.

[21] J.H. Gilmore, B.J. Pine II, The four faces of mass customization, Harvard Business Review January–February (1997) 91–101.

[22] A.S. Grove, Only the Paranoid Survive: How to Exploit the Crisis Points That Challenge Every Company, Currency Doubleday, New York, 1996.

[23] C. Hilton, Manufacturing operations system design and analysis, Intel Technology Journal, 1998, Available at URL: http://www.intel.com.

[24] Industrial Technology Information Services (ITIS) of Taiwan, The Trends of IC Industry, ITIS, Taipei, 1997.

[25] S.L. Jarvenpaa, L. Sirkka, The global network organization of the future: Information management opportunities and challenges, Journal of Management Information Systems 10 (4), 1994, pp. 25–57.

[26] G. Keller, SAP R/3 Process Modeling, Addison-Wesley, New York, 1998.

[27] E. Korczynski, ERSO’s children grow up, Solid State Technology, February 1997, pp. s14–s15, s23–s24.

[28] L.J. Krajewski, L.P. Ritzman, Operations Management: Strategy and Analysis, Addison-Wesley, New York, 1996.

[29] A.M. Law, W.D. Kelton, Simulation Modeling and Analysis, McGraw-Hill, New York, 1991.

[30] A.A. Lazar, S.K. Bhonsle, K.S. Lim, A binding architecture for multimedia networks, Journal of Parallel and Distributed Computing 30 (2), 1995, pp. 204–216.

[31] A.A. Lazar, K.S. Lim, F. Marconcini, ‘‘Realizing a foundation for programmability of ATM networks with the binding architecture, IEEE Journal on Selected Areas in Communications 14 (7), 1996, pp. 1214–1227.

[32] P. Losleben, Status Report on a Major Research Thrust in the Center for Integrated Systems, The Stanford Semiconductor Manufacturing Research Program, Stanford University, February 1992.

[33] C.H. Lovelock, Services Marketing, third ed., Prentice-Hall, London, 1996.

[34] J. Magertta, The power of virtual integration: an interview with Dell Computer’s Michael Dell, Harvard Business Review March–April (1998) 73–84.

[35] C.J. McDonald, The evolution of Intel’s Copy EXACTLY!: Technology transfer method, Intel Technology Journal (1998), Available at URL: http://www.intel.com.

[36] J. McGehee, J. Hebley, J. Mahaffey, The MMST computerintegrated manufacturing system framework, IEEE Transactions on Semiconductor Manufacturing 7 (2), 1994, pp. 107–115.

[37] E.S. Meieran, 21st century semiconductor manufacturing capabilities, Intel Technology Journal (1998), Available at URL: http://www.intel.com.

[38] M. Melliar-Smith, The globalization of the semiconductor industry, in: SEMI Technology Symposium Keynote Address & Slides, 2 December 1998, Available at URL: http://www. sematech.org.

[39] Oracle Corporation, Data warehousing: turning data into decisions, White Paper, CW Custom Publications, 1995, Available at URL: http://www.oracle.com.

[40] T. Quatrani, Visual Modeling with Rational Rose and UML, Addison-Wesley, New York, 1998.

[41] J. Rumbaugh, I. Jacobson, G. Booch, The Unified Modeling Language Reference Manual, Addison-Wesley, New York, 1999.

[42] SEMATECH, Computer Integrated Manufacturing (CIM) Framework Specification, Version 2.0, Technology Transfer #93061697JA-ENG., SEMATECH, Austin, 1998.

[43] SEMATECH, CIM Framework Architecture Guide 1.0, Technology Transfer #97103379A-ENG., SEMATECH, Austin, 1997.

[44] SEMATECH, Object-Based Equipment Model Proof of Concept, Technology Transfer #98113588A-TR, SEMATECH, Austin, 1998, Available at URL: http://www.sematech.org.

[45] Semiconductor Industry Association (SIA), The National Technology Roadmap For Semiconductor, San Jose: SIA, 1994.

[46] A.S. Tanenbaum, Computer Network, third ed., Prentice-Hall, London, 1996.

[47] M. Thompson, Simulation based scheduling, IIE Solutions, May 1996, pp. 30–34.

[48] F.C. Tseng, TSMC’s semiconductor strategy, in: Proceedings of the Seventh International Symposium on Semiconductor Manufacturing, Tokyo Japan, 7–9 October 1998, pp. 5–7.

[49] F.C. Tseng, Semiconductor industry evolution for 21st century, in: Proceedings of the Symposium on VLSI Circuits Digest of Technical Papers, IEEE, 1999, pp. 1–4.

[50] UMC, UMC Group Foundry Service Guide, 1999, Available at URL: http://www.umc.com.

[51] D.M. Upton, A. McAfee, The real virtual factory, Harvard Business Review July–August (1996) 123–133.

[52] P. Vitharana, H. Jain, Research issues in testing business components, Information & Management 37, 2000, pp. 297– 309.

[53] S. Wang, Modeling information architecture for the organization, Information & Management 32, 1997, pp. 303–315.

[54] J.D. Wells, W.L. Fuerst, J. Choobineh, Managing information technology (IT) for one-to-one customer interaction, Information & Management 35, 1999, pp. 53–62.

[55] N. Yuhanna, Oracle8i Database Administration, Manning Publications Company, December 1999.

![](/api/attachments/GH5PYJSN/fulltext/images/3c4fd66f70c8bec2a8da0d066f08be70e09524a3c9272ae873244aaa09cd297d.jpg)

Yea-Huey Su is an assistant professor in the Department of Information Management at National Central University, Taiwan. She received the PhD degree in management of technology from National Taiwan University, Taiwan in 2003, and the BS degree in management science and the MS degree in information management from National Chiao Tung University, Taiwan, in 1990 and 1992,

respectively. From 1993 to 1995, she was an associate planning engineer at Institute of Information Industry, where she worked in the area of system analysis, implementation, and promotion for the Primary Health Information System. Her research interests include technology innovation, technology transfer, and business model.

![](/api/attachments/GH5PYJSN/fulltext/images/2813a068b460984fb2e23401a95c1fa49c93fc5ae36257c7fae8e8aa5e1592d4.jpg)

Ruey-Shan Guo received his PhD degree in mechanical engineering with a major in manufacturing and a minor in solid state physics from Massachusetts Institute of Technology in 1991. From 1991 to 1995, he was a research engineer at National Semiconductor, Santa Clara, CA, USA, where he worked in the areas of process control, factory operations, and computerintegrated manufacturing. He also ob-

tained his MBA degree from San Jose State University in 1994. Since 1995, he has been with National Taiwan University. He is currently professor in both Graduate Institute of Business Administration and Graduate Institute of Industrial Engineering. During his current position, he has been a principal investigator or co-PI to many industry and institution funded projects (such as TSMC, National Science Council, and Industrial Technology Research Institute in Taiwan, and Semiconductor Research Corp. in USA) in the areas of advanced process control, yield improvement, computer-integrated manufacturing, and foundry supply chain management. He has published more than 70 journal and conference papers in these areas. Dr. Guo is an IEEE member and is currently the associate editor of IEEE Transactions on Semiconductor Manufacturing. He also serves in the Editorial Board of Journal of the Chinese Institute of Industrial Engineers.

![](/api/attachments/GH5PYJSN/fulltext/images/83cbe4ea62b1097f57cf4f8cfd31b428201d7bfa703c6fe1dac4b08f3ffc72fd.jpg)

Shi-Chung Chang received the BSEE degree from National Taiwan University, Taiwan in 1979, and the MS and PhD degrees in electrical and systems engineering from the University of Connecticut, Storrs, in 1983 and 1986, respectively. From 1979 to 1981, he served as an ensign in the Chinese Navy, Taiwan. He worked as a technical in-tern at the Pacific Gas and Electric Company, San Francisco, CA, in

the summer of 1985. During 1987, he was a member of the Technical Staff, Decision Systems Section, ALPHATECH, Inc., Burlington, MA. He has been with the Electrical Engineering Department of National Taiwan University since 1988 and was promoted to professor in 1994. His research interests include control and management of complex systems, high speed networks, optimization theory and algorithms, and distributed decision-making. He has been a principal investigator and consultant to many industry and government funded projects in the above areas, and has published more than 100 technical papers. Dr. Chang is a member of Eta Kappa Nu and phi Kappa Phi.
