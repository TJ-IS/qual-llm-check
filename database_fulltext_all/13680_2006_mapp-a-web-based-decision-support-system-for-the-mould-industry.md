---
otero_id: 13680
otero_key: "Z8ECZCK6"
title: "MAPP – A web-based decision support system for the mould industry"
authors: "C. Silva; L. Roque; A. Almeida"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.08.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# MAPP – A web-based decision support system for the mould industry

C. Silva <sup>a,\*</sup>, L. Roque <sup>b</sup>, A. Almeida <sup>c</sup>

<sup>a</sup> University of Coimbra, Mechanical Engineering Department, Po´lo II Pinhal de Marrocos, 3030 Coimbra, Portugal <sup>b</sup> Centre for Informatics and Systems of the University of Coimbra, Portugal <sup>c</sup> Instituto Pedro Nunes, Portugal

Received 22 December 2003; received in revised form 17 June 2005; accepted 2 August 2005 Available online 1 September 2005

## Abstract

This paper describes the MAPP, <sup>b</sup>Mould: Assistant Production Planner<sup>Q</sup>, a web-based decision support system developed for the mould industry. MAPP addresses two subsystems considered fundamental by the managers of a case study company: (1) production planning and control and (2) information and document management. The production planning methodology implemented is based on the workload control concept developed at Lancaster University, adapted to the context of the moulds industry, under a Rapid Prototyping case study. The main objectives of this paper are to present a discussion of the system functions at the service of the planning methodology, and to explain the development decisions in the socio-technical context of the case study company. We conclude with a brief overview of issues raised in lab and field testing, along with some proposals for further research.

<sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Web-based decision support system; Workload control; Mould industry; Socio-technical information systems development

## 1. Introduction

The Make To Order (MTO) industry sector is composed of a large number of companies, many of them belonging to the Small/Medium Enterprise (SME) category. Nevertheless, as pointed out in Ref. [15], until recently research in production planning methodology and tools disregarded the specific needs of MTO companies and concentrated on the more predictable Make To Stock (MTS) environment. The MTO industry can be divided in two types [1]: Repeat Business Customisers (RBC) and Versatile Manufacturing Companies (VMC). An RBC provides customized products on a continuous basis over the length of a contract. In a VMC each order is completed individually and a high variety of products is manufactured in small batches with little repetition.

The workload control (WLC) concept has been indicated as a production planning and control system appropriate to the MTO sector (see, for example Ref. [15]). A lot of research has been carried out on the

WLC concept and surveys can be found in Refs. [3] and [18].

The purpose of this paper is to present a web-based decision support system, called MAPP, comprising a production planning module based on the WLC concept, to be implemented in a VMC that produces moulds for the plastic injection industry. The main objective of this paper is to describe the decision support system in relation to the adaptation of the planning methodology and discuss some development decisions.

The paper is structured as follows. We start with a brief description of the company chosen as a case study. Section 3 explains the WLC concept implemented in the decision support system. Section 4 describes the decision support system and discusses some aspects of the methodology, architecture and tools used in its development. Finally, in Section 5 we discuss some aspects related to the MAPP implementation in our case study company.

## 2. The case study context

This case study was carried out for a company that produces moulds in aluminium to be used by the plastic injection industry as tools for pre-series production. Usually, a mould is made in iron and it is used to produce a large quantity of plastic products. The lead-time for making such a mould can be a few months. In our case study, the moulds are produced in aluminium to facilitate the production process and substantially reduce the lead-time. These moulds are less resistant than normal iron moulds and they are used to produce small quantities of pre-series products. Using aluminium allows a mould to be manufactured in a shorter lead-time, usually just 6 to 8 weeks.

Mould production is a typical case of a VMC. Each mould is a different product, made according to the client’s specification, and therefore manufacture can only begin once a firm order is placed.

When the company agrees a price and a delivery date for a mould with the client, the execution of the order can begin. The first step of mould production is designing the mould. For this, the company needs the specifications of the product that will be manufactured with the mould. The design consists of 2D/

3D representations of the mould and its main components. This stage is carried out in the design department, in this case composed of six designers. When the mould has been designed and approved by the client, its production can begin. The shop floor where the mould is produced is composed by 15 machines divided in four groups: support machines, CNC machines, electro-erosion and assembly. Most mould components are processed as follows: conventional machining in the support machines, CNC machining, electro-erosion and finally assembly. But this routing scheme is not followed by all components. Some return to the CNC machines after the electro-erosion operations, others are assembled and then go back to the CNC or electro-erosion machines to be machined together. Therefore we define the shop floor as a job shop, with asymmetric routing, where a dominant flow direction can be identified.

Due to the nature of the product, which is regarded as a prototype, this company needs to deal with a lot of incoming information. This information, arriving in the form of text, drawings, tables, and so forth, and in various file formats, is essential to a clear understanding of the final product specification. Furthermore, information keeps arriving during the production process, because of late change requests by the clients or in response to company enquiries for details about the desired product. Company managers call this incoming information – <sup>b</sup>dust<sup>Q</sup> – a suggestive name to refer to the fuzziness and fragmented nature of this information, and the difficulties in distributing it, on time, to all the people who need it for their tasks. The lack of tools to deal with this informational dust is indicated by company managers as one of their main daily problems, and one for which they have not found an effective solution.

A second group of problems encountered by the company managers were the difficulties found in establishing effective production plans. These difficulties were due to:

(1) The need to deal with several projects at the same time, competing for the same resources;

(2) The job-shop nature of the production system;

(3) The need to deal with a large number of subcontractors. Our case study company is in a region with a great tradition in mould manufacture. This has led to the establishment of a lot of small companies which specialize in providing support to the main mould manufacturers. Therefore, if excess work is generated due to an order for a new mould, our case study company can easily subcontract extra work in order to meet the proposed delivery date. The company can subcontract the execution of a complete component or just an operation or set of operations for a component. Historical data show that in some cases more than 85% of the component’s manufacture was subcontracted to local companies to solve capacity problems.

(4) The large amount of reworking needed in moulds sent to clients. When the mould leaves the company, the client uses it to produce small series. These series are used to test the quality and specifications of the finished products. Sometimes, the client needs small changes in the mould to solve product problems found during pre-series testing. These small changes, implying component re-design and modification, are handled as urgent work.

The problems referred to in this section are not exclusive to our case study company. In fact, a recent study on mould manufacturing [5] reveals that mould manufacturers are facing increasing pressure from their clients to reduce lead-times and to cope with the need to quickly introduce required changes in the product during the design or execution of the mould. A Portuguese study [10] also indicates that the problems found in our case study company are common to other mould manufacturers. In this study the author says that the competitiveness of mould making companies, dominated by SME’s, lies in the ability to provide short and reliable leadtimes, which implies: organization, technology and information systems. Therefore we believe that the DSS described here can be easily adapted to other companies in the mould industry.

To help solve the problems listed above we propose a decision support system containing two main modules: (1) production planning, implementing a workload control methodology, and (2) project related information and document management.

## 3. Production planning methodology

As previously mentioned, the WLC concept has been suggested as being appropriate for production planning in companies operating in the MTO sector. The main objective of the WLC concept can be defined as: to control the lengths of the queues at work centers on the shop floor in order to control waiting times and, consequently, overall manufacturing lead-times. To achieve the control of queue lengths, the WLC concept relies on the release decision. WLC concepts do not release jobs to the shop floor if they are likely to cause queues longer than certain predetermined norms. To control the release of jobs to the shop-floor a <sup>b</sup>pool<sup>Q</sup> of unreleased jobs is created. Once released, the progress of a job on the shop floor can be controlled by priority dispatching at each work center.

Historically, the origin of the WLC concept can be found in Ref. [17], where it is called input/output control. Since then the concept has evolved to a class of hierarchical capacity-oriented production control. The WLC concept exercises capacity control at three levels: (1) the entry level, where the long-term capacity utilization is controlled; (2) the release level, and (3) the dispatching level.

Three WLC concepts seem to attract the attention of researchers: (a) the one developed in Hanover [2,16], (b) the one developed in Eindhoven [4] and (c) the one developed in Lancaster [6,7]. For a comparison of these concepts see, for example, Ref. [11]. We decided to adapt the WLC concept developed in Lancaster to the MAPP production planning module. This concept was chosen because it is, probably, the one whose entry level has been best studied. We consider that the entry level is fundamental for our case study, because the subcontracting decisions can be made at this level. The WLC concept developed at Lancaster University, aims to control manufacturing lead-times by controlling a hierarchy of backlog lengths of work. It addresses two decision levels: a) the job entry stage, at which due dates are estimated, and b) the job release stage, when a job is released to the shop floor so that production can commence. The third level – dispatching – is not considered in the Lancaster WLC concept. It is assumed that, since its use reduces the complexity of shop-floor dispatching, it is sufficient to allow the foreman to determine the order in which the released jobs are processed based on his experience and informal ad-hoc approaches, or by using simple dispatching rules as, for example, first in first out (FIFO). This methodology is well documented in previous papers; see for example Ref. [8].

Some adaptations to the Lancaster WLC concept were required to make it suitable for our case study. Those adaptations, discussed in a previous paper [14], were made to the job entry level and the job release level.

At the job entry level, the adaptations were needed because our case study company can easily subcontract part of the work required to fulfil an order if capacity problems occur. Therefore, at the order entry level, the methodology can be used to decide which work should be subcontracted instead of using it exclusively to define due dates or to reject orders, as in the original idea of the methodology.

At the release level, the main adaptation is in the frequency of feedback information about the work centers’ load level. In the original methodology this feedback occurs when a job (in our case a mould component) is completed. In the methodology we implemented the feedback happens when each individual operation is completed. We took this option because the information system developed facilitates feedback, and the additional information helps the manager to keep track of intermediate progress.

The original methodology plans workload requirements on an aggregate weekly level. In our adaptation we decided that, due to the small lead times required, a weekly plan may provide insufficient control for the shop-floor. Therefore in our case we plan the workload requirements on a daily base, which leads us to the definition of a daily interval between releases.

## 4. MAPP: the decision support system

## 4.1. Information system development methodology

Next we will present a brief review of the development process for the reader to develop a more informed judgment about case similarity and suitability of approach. The problems we found in our case study company, described in Section 2, led us to consider developing a decision support system oriented to the integration of production planning with collaboration support, by helping users to manage project specific information (e.g., contracts, budgets, specifications, 3D models, change requests). With this decision support system we intend to help the company to achieve two goals: a) reduce lead-times, and b) increase the due date reliability, while maintaining or favouring other quality goals. To attain those objectives we intended to provide the company with both computational and methodological tools, suitable for resolving their problems, but the system should be generic enough to be easily adaptable to other companies operating in a make-to-order environment.

The development of information systems is not without its failures and many efforts do not achieve the hoped-for outcomes, for a variety of reasons. One is certainly the inability to correctly take the structure of the problem into account, combined with the architectural flexibility needed to cope with rapid change, within both the market and the organization. Other factors, like available working skills and worker autonomy, personal, organizational and social relations, the relationship with the installed IT base and the interconnections with suppliers and customers, can all play decisive roles in the outcome of Information Systems Development projects. It was with this socio-technical perspective of development that we embarked on this exercise, searching for a solution that would take into account the nature and diversity of the factors involved, as well as the relations between them, following a developmental approach based on prototyping we call Context Engineering [12].

We began with a diagnosis of the situation, and entered into a <sup>b</sup>negotiation process<sup>Q</sup> with the company to formulate what would be considered by managers an interesting objective to our intervention, in terms of estimated costs and effects. In this process we considered the challenges that were being described by company managers when they talked about production planning difficulties, namely, coping with customer interference during the production process (e.g., by being able to accommodate change requests) and effectively managing the significant amount of project information, updates and notifications, generated along the way. We arrived at a proposal that was accepted by the organization as a relevant research goal for them. It was during this diagnosis that it became apparent that a degree of autonomy at the level of the work center was critical to the performance and flexibility of the company when it had to cope with a steady flow of change requests and late definitions. We also noticed the burden that negotiating client requests and sub-contracts put on managers, that involved both commercial and production departments, and the importance these activities had in keeping the company focused on its central skills, while allowing it the flexibility to accept more orders. These were clearly important factors which partly explained how the company successfully related to its business environment, and they would have to be considered by whatever production planning method or adaptation the company might adopt. Thus, in proposing an innovative step that involved the adoption of new instruments, including planning and control practices, we considered their interaction within the socio-technical context of the established know-how, organizational values, rules, practices and tools [12]. This was done by evaluating the fitness between the proposed new tools and the existing and desired context model, and their capacity for promoting idealized changes.

As previously discussed, we envisaged a system that integrated planning with the management of ongoing project related information in this production context. We proposed to develop a collaboration infrastructure to support document management, circulating internally or shared with external actors. By exploring simple mechanisms such as email and web interfaces, we designed communication channels to share information and support interactions between the company and their external collaborators that could support or improve the communication processes we found in the company. These interactions include submission and access to: project contracts, specifications, planning and realization events, subcontract assignments and dispatching. The development of such mechanisms, combined with an architecture that allows selective access of customers and suppliers to related information involved significant effort. To enable rapid deployment of such an infrastructure and avoid the risks of diverting the research team’s attention from the main research goal that was being directed towards the implementation of an adequate production planning methodology, we decided to reuse a collaboration platform from a previous project, which already partly responded to the above-mentioned needs.

We prototyped the system incrementally by following the internal value-chain: beginning from customer relationship management, budgeting and negotiation activities, including product design phase and planning activities, and ending in production and subcontract management. We meet the company managers about every two months and have a lively discussion of the prototyped applications with the aim of validating or defining new requirements, evaluating the design and its suitability and relevance in the company’s context, while trying to strike a balance for the class of make-to-order SMEs in general. A number of lab tests were also performed with realistic cases based on company historical data, by analysing and translating previous project documentation, planning and revisions as predictable models of performance. At this stage we cannot offer evidence of the generality of this case, other than a common sense evaluation that confirms plausibility.

## 4.2. System model and architecture

The underlying collaboration platform comprehends a core set of functionalities including: authentication and access control, file/object repository, version management, group definition, personal and group mail distribution and selective object/document sharing spaces. This core set of services is then extended with a set of service applications, in this case a service developed to support the workload management methodology.

Each project is assigned to a document space where all documents regarding the corresponding mould are <sup>b</sup>stored<sup>Q</sup>. Each document space has a group assigned to it, containing all the people involved in the mould production. Therefore all those concerned with a given mould execution place and retrieve information from the same space, facilitating the communication and document dissemination process. Additionally, access administration can be delegated to project managers within the organization, thereby facilitating overall system management and end-user relations. We then worked to extend this functionality with a planning and control service application dedicated to the make-to-order context and, in particular, to the mould industry.

Through this process, the business logic evolved as two subsystems:

<sup>!</sup> Production Management: planning, monitoring and control of the mould production (shop floor, work centers, operations, projects, plans, loads, events, subcontracts);

<sup>!</sup> Collaboration: communication and document management (requests, budgets, negotiations, detailed project documents, group email, customer reporting).

One of the main aspects of the DSS we wanted to develop was that it should allow easy and frequent access to the available resources and tools, by a large number of mould production actors, from inside and outside the company. To take advantage of well known and widely disseminated technology, we adopted an architecture based on the three-tier architecture [13], and implemented it using web technologies. Web technology allows any user connected by Internet protocols (TCP/IP), with a Web browser, to access the application server, installed internally or externally to the organization. Access is controlled by a username/password pair to identify and authenticate the user profile.

The three-tier model is depicted in Fig. 1. The presentation tier is the user interface that runs on the web browser installed in the user’s computer; therefore, the user interface will look like an ordinary web page. The business tier is composed of: 1) the web server, which serves the page definitions and other interface elements to the browser; 2) the application server, which runs the application logic, manages user sessions, and interfaces to the business logic, and 3) the collection of code or class models that represents the business logic (data entities, rules, etc), which is what controls the preparation of production plans, runs simulations, monitors production registering, manages the document repository, etc. Finally, the data tier contains a common database management server, a file server and an email server.

## 4.3. Technological options

The architecture and technology chosen to develop MAPP, presented in the previous section, has advantages and disadvantages, at both the stage of software development and that of software use. System architecture, while more complex than monolithic applications, enables the separate implementation of interface, business logic, such as planning and documental functions, and data management. This separation of concerns along different layers (or tiers) provided as web enables applications facilitates distribution without requiring individual software installations for each user, a web browser is all that is needed to access the applications. It also enables management of MAPP users based on profiles. Furthermore, the number of access points and profiles can also easily be configured to share information with customers and subcontractors without other expensive Electronic Data Interchange (EDI) systems. This is particularly important given the small dimension of the supplier companies, which can be reluctant to acquire such systems.

![](/api/attachments/Z8ECZCK6/fulltext/images/f090f2b7ed35c28839efecffb0006f004ac8177572d580fdfea70f349ab57d95.jpg)  
Fig. 1. The three-tier model and system architecture.

The alternative to the architecture we propose could be an application installed locally in every computer. In this case the user interface might be designed to resemble the interfaces found in wellknown commercial computer programs, while in our option the interface looks like a web page. From the point of view of usability the main difference between these options is the dominant way the user <sup>b</sup>communicates<sup>Q</sup> with the system. With a web-based application, interaction tends to resemble a dialogue, which assumes prior knowledge of the system’s working model. A direct manipulation interface, where the user could use a mouse to point, select, drag, or otherwise virtually manipulate visual representations of the data and operations represented in the system (e.g. components, operations, plans, work centers) would be preferable for exploratory use, enabling easier experimentation and a faster learning curve. This was a compromise made for faster software prototyping and leveraging of available technical skills. We intend to proceed by developing a direct manipulation interface when we have stabilized the knowledge of current support services and functionalities, using Java applets. While retaining the possibility of being centrally distributed and running on the same browser platform this technology enables the programming of more specialized interaction models, which usually takes more time and effort. These new interfaces could be made to reuse the same business logic already developed, roughly substituting the presentation tier in the architecture described earlier.

We used Apache and Tomcat as the Web Server and Application Server, currently readily available as open source project software at www.apache.org. The Business Logic, presentation and interaction control, were implemented as Java Server Pages and the Business Abstraction was implemented using Java Classes. JNDI – Java Naming Directory Interface is used for resource discovery and management and JDBC – Java Database Connectivity is used for independent vendor interaction with Database Management Server. JavaMail is the Internet e-mail application interface. An Internet World-Wide-Web browser is used to access the web server via the HTTP protocol. On the browser side we use the Scaleable Vector Graphics (SVG) plug-in for drawing workload graphics, plans, etc. This technological setup, while suitable for our case study, may need to be tuned for performance in a high demand situation (e.g., over 100 users).

## 4.4. Data model

Another important aspect of the system is the data model that is used to support the production management methodology. Fig. 2 shows simplified aspects of the data model used in the implementation, in particular the main data entities and attributes, along with chief relationships.

A request introduces the negotiated delivery dates that will drive the planning activity. A request goes through a series of phases (e.g. design, production) which, due to domain restrictions, may have to be kept independent and thus may be subject to independent plans. A request is satisfied by an aggregation of components, made of standard accessories and special purpose built components. A plan has components that correspond to the project components to be produced, whatever their nature (drawings, parts, etc). Every non-standard component will have its own earliest and latest release date (ERD and LRD), that enables the execution of the set of tasks (operations) required for that component, respecting operation dependency, and that will vary in the operation type parameters for each operation on each work center.

Before being considered valid, plans must undergo a simulation process to check if that plan can be performed for that delivery date (DD) under current system workload. This process reports simulation errors that must be solved with a set of available strategies: re-routing operations to alternative work centers, considering extra capacity, subcontracting operations or component executions, renegotiating the DD.

When validated a plan may be made active, which means it will enter the execution pool and become available for releasing, dispatching, monitoring and control. Work releasing is done at the component level and execution reporting is done at the operation level, generating event and execution registers. When subcontracting, specific tasks may be automatically or manually grouped under work packages for management simplicity, and associated with an open contract.

![](/api/attachments/Z8ECZCK6/fulltext/images/2bc1afbae64b2e0a6d090f3f979b67d4fd3f5d807eca00f13b14da291a69ae87.jpg)  
Fig. 2. Aspects of the underlying data model.

## 4.5. MAPP modules

In this section we present the various modules composing MAPP. We will refer to how each module provides decision support at: (1) the customer enquiry stage – Section 4.5.2; (2) at the order entry stage – Sections 4.5.3 and 4.5.4; (3) at the order release stage – Section 4.5.5 and (4) at the shop floor level – Section 4.5.5.

## 4.5.1. Parameterization

Before productive usage the system must be parameterized both with company specific information and the required WLC control parameters. The company specific information includes the user accounts, the work centers – each machine is considered a work center – and types of operation they can process, their normal daily/weekly capacity, expected mean queue lengths, and human resources allocation. Special capacity arrangements may also be set up. The

WLC control parameters set up at this stage includes the maximum total, planned and released, backlog lengths (MaxTWL, MaxPWL and MaxRWL), for the work centers and the shop-floor as a whole, and the expected pool delay.

## 4.5.2. Commercial management and price definition

In the original methodology the total backlog length is controlled at the customer enquiry stage to avoid the company bidding for an unfeasible mix of workloads and due dates. At that stage the workload of unconfirmed jobs multiplied by the company strike rate is added to the aggregate workload of confirmed jobs to calculate the total backlog length. The comparison of this total backlog length with the chosen limits allows the decision maker to quote reliable due dates or to adjust capacity to meet the customer required due date. In our case study, we decide to ignore this part of the original methodology due to: (1) in our case, the strike rate is very low, less than 5% of customer enquiries become a firm order and (2) if an excess of workload is generated by the incoming orders our company can subcontract this excess of work and perform only the more critical operations.

Despite this, to help in managing client relations, MAPP was designed to provide mechanisms to support the answer to customers’ enquiries. Providing this support was essential because of the large number of enquiries the company must answer. MAPP is ready to display historical information, e.g. about past enquiries and their answers, to the same customer or to similar requests. The reaction of the client, that is, acceptance or rejection of the company’s proposal, appears in relation to the various prices/due dates proposed in the past. This information helps the user define an aggregate proposal, supporting operational, raw material and subcontract costs, and avoiding detailed costing procedures, which cannot be used at this stage because a detailed design of the required mould does not yet exist.

Since the commercial department will have access to the real time workload levels, we expect some improvements in defining the due date at this stage.

## 4.5.3. Bill of materials and routing/process definition

When an order is accepted, the first step is to define a draft project. This draft is used by the production planner to compile the Bill of Materials (BOM) for the mould, specifying the components, the production routing with required operations and estimated processing times.

To setup a BOM for the mould, the manager uses the interface presented in Fig. 3. The first step consists in introducing, for each mould component, the following information: component code, designation, if it will be produced in the company or subcontracted, the quantity required and it parents components. This information is presented to the user in the form of a BOM <sup>b</sup>tree view<sup>Q</sup> like the one presented in the upper part of Fig. 3. When a component is selected in the tree the required operations appear in the middle table.

The information regarding the operations required to produce a given component is inserted in the same screen, see the lower part of Fig. 3. Here, for each operation, the user defines its code, category, type, if it will be performed inside the company or subcontracted, the work center where it will be processed and the expected processing time. The user also indicates if the operation completion date is to be calculated by MAPP or set manually to reserve capacity within a certain time frame. Finally the user indicates the dependencies between the operations in the production route for this component.

The setup of a BOM, operations dependencies and routing is time consuming because of the large number of mould components. MAPP helps to reduce the time needed to define a BOM and routing definition by enabling the user to retrieve, reuse and adapt parts of trees for mould components previously developed for other projects. Parts of BOMs in the database can be combined by <sup>b</sup>copy/pasting<sup>Q</sup> structural sub-trees, to build up at least part of the BOM tree for the new mould.

To help the planner to define component routing and to allow him to know current company workload, the system produces graphic displays of the different backlog lengths of work considered by the production planning methodology, as shown in Fig. 7.

## 4.5.4. Impact simulation and conflict resolution

The user responsible for drawing up the plans can simulate them to preview the problems that would result if that plan was introduced into the production system with the current system workload. The specification of production operations, dependencies and processing time, as described in the previous section, along with the values of mean queue lengths defined when the system is parameterized, will allow backward scheduling, identifying the components’ earliest and latest release and operations completion dates (ERD, LRD, OCD).

The OCD of the last operation of a component depends on its position in the BOM tree. If the component belongs to level 0 of the BOM tree, the OCD of its last operation will be set equal to the mould due date minus the time required to test the mould. If the component belongs to level 1 or higher of the BOM tree, the OCD of its last operation will be set equal to the first LRD of its parents’ components.

Knowing the OCD of the last operation of a component we can calculate the OCDs of its other operations. Each operation in the processing of a component is dependent on the completion of the previous operation in the component routing. This means that operation t cannot be started as long as operation t  1 is not completed. Each operation will require an amount of time on a given work center. This time for a given operation t of a component j can be denoted by Lt, j, given by Lt, j = queue time + setup time + processing time. Therefore the OCD of an operation is calculated using Eq. (1).

![](/api/attachments/Z8ECZCK6/fulltext/images/a4d5d9516eb24618fc90f77a43990eaa367946b09f92271496ef52bcfe3f95df.jpg)  
Fig. 3. The mould Bill of Materials, operations, routes and dependencies.

$$
\mathrm{OCD} t - 1, j = \mathrm{OCD} t, j - \mathrm{Lt}, j\tag{1}
$$

The OCD of the first operation on a component minus the time required to process it, $L 1 , j ,$ will result in the latest release date for that component, see Eq.

(2). This instant represents the latest date to release the component to the shop-floor.

$$
\mathrm{LRD} j = \mathrm{OCD1}, j - \mathrm{L1}, j\tag{2}
$$

Considering the pool delay (PD), representing the waiting time of a job in the pool, we can obtain the earliest release date for the component, using Eq. (3). The ERD of a component represent the date when this component will enter the pool, thus becoming available for release.

$$
\mathrm{ERD} j = \mathrm{LRD} j - \mathrm{PD}\tag{3}
$$

The ERDs and LRDs of all components for the new mould, and the OCDs of all operations required to obtain them, along with the workload imposed by components belonging to moulds previously accepted by the company, are used to calculate: (1) the total backlog length, (2) the planned backlog length, (3) the capacity required to maintain those backlog lengths bellow pre-specified maximum limits and (4) the capacity required to process all operations by their OCDs. The details on how those parameters are calculated can be found in Ref. [7].

The system reports the capacity problems which would occur along with suggestions for possible solutions to solve them. This report is illustrated in Fig. 4. The upper part of this screen indicates a list of components, from the mould now being planned, that will cause capacity problems. For each of those components the report indicates: (1) a description of the problem (violation of backlog length limits or impossibility to process it by its OCD), (2) the date in which the problem is expected to occur and (3) the work center were it will occur.

Next, the screen presents proposed solutions to choose for the detected capacity problems. Implemented solution strategies include: a temporary increase in work center capacity (overtime), prioritization measures, internal or external re-routing (subcontracting) specific operations or components and, as a last resort, changing the delivery date.

Manually fixing operation completion dates is another way of redistributing workload along the calendar but it is not as easily supported. Those alternatives are presented to the user who decides what is appropriate in each case. If desired, subcontracting can be kept to a minimum by exhausting the other possibilities before resorting to outside services.

Some laboratory tests have been conducted on MAPP that allowed us to understand the usefulness of the different solution strategies implemented. We found that our case study production planner prefers to solve capacity problems internally. This means that, whenever capacity problems are detected, the first choice of the production planner is to try to find an alternative internal routing for the component. If this option fails, the planner usually tries to assign some overtime, which is limited to 2 or 3 h per day and must be agreed with the machine operators. The capacity problems often cannot be solved internally and the planner decides to subcontract part of the required work. During the tests we observed that the planner usually subcontracts a complete component rather than a specific operation on a component. It should be noted that, during the tests, the planner never used the possibility of changing the delivery date or rejecting the order. This situation is probably specific to our case study where, as we said earlier, it is very easy to subcontract excess work.

![](/api/attachments/Z8ECZCK6/fulltext/images/52f088dabd1f0475b72ddf247e0e11f50bd99d2d54ea0b368b83ac727dfcaf54.jpg)  
Fig. 4. Plan simulation report with proposed solutions for detected workload problems.

## 4.5.5. Monitoring and control

For internal and external production control, MAPP helps to monitor the execution of a mould by identifying its components’ location and the operations being executed. To achieve this it provides decision support at the job release stage and at the job dispatching stage.

4.5.5.1. The job release stage. The production manager uses the interface shown in Fig. 5 to manage daily component release to the shop-floor. This interface is composed by two tables.

The first table presents a list of all components, to be produced by the company, waiting to enter the pool. This means that this list contains all components that are planed for which the ERD has not yet been attained.

The second table presents all the components waiting in the pool for release to the shop floor. In this table the jobs are sorted in order of shortest slack, the difference between the LRD and the current date. For each component in the pool, MAPP identifies the mould where it will be required, its code, designation, required quantity, its parent component, the earliest and latest release dates and the corresponding slack for current date. The production planner decides which component is to be released by checking the box presented in the last column of the table. MAPP can simulate the effect of releasing all the selected components, calculating and showing the resulting released backlog length. If the maximum released backlog length is violated at any work center, the system informs the user to choose a different mix of components to be released. This interactive procedure goes on until a desired and allowable mix of released components is achieved.

Subcontracts are dealt with in a similar manner, treating contractor’s shop-floors as extensions of the company, associating operations or components in work packages that are dispatched in time to begin processing at their destinations.

4.5.5.2. The job dispatching stage. As we previously referred, the production planning methodology adopted reduces the complexity of shop-floor dispatching. Therefore it was decided to let each operator to locally choose the processing order of the operations on the components released to his work center, as long as the OCD is satisfied. To help the operator in this decision, MAPP provides for each work center a set of information regarding the operations to be made there. See example for one component in Fig. 6. This information consists of a list of all components with operations to be executed at the work center. Each component is represented by a bar where the dark grey part represents the operation to be made in the work center and the light grey part represents other operations to be made at other work centers. For the operations to be made at the work center MAPP presents: the operation code; the component code; the type of operation to be performed; the expected processing time and the required OCD.

![](/api/attachments/Z8ECZCK6/fulltext/images/7db89b56fb75392770a9c5d8ae5df5f95259d634ab488042c27d32585b4fa0dc.jpg)  
Fig. 5. Component release interface.

This form can be printed or used online to enable the registering of the work performed per day in each operation. At the end of each day, the operator marks the operations completed and the backlog lengths are updated.

Afterwards, the analysis of execution registers will provide a better estimation of production and subcontracting costs, to support commercial budgeting for similar project components. Analysis of subcontract registers allows historical indexes to be produced for subcontractor availability, performance, quality of service and confidence. These can be used to guide the management of future relations, from choosing the <sup>b</sup>right<sup>Q</sup> subcontractor, to take operational measures like advance notification of work package release, to include security or legal protection for fulfillment dates.

## 4.5.6. Reporting for clients

Clients may have access to the current state of their orders in the system. This information can either be reported directly from the registering of production events or it can be given by the production manager, who can provide filtered or aggregated digests for client to access. Current trends in companies’ relations point to greater process transparency, which could, eventually, mean an end of <sup>b</sup>hide-andseek<sup>Q</sup> games, as they may be responsible for bigger planning accidents. In the prototyping sector, process transparency is also a requisite for dealing with later project inputs or revisions.

## 4.5.7. Workloads graphics

MAPP can be used to monitor the current company workload, giving a graphic display of the different backlog lengths considered by the production planning methodology. Fig. 7 shows an example of the representation of the planned backlog length for a given work center. For each day in the planning horizon, X axis, the planned backlog length (in days) is presented. The dark grey part of the columns represents the workload imposed by components belonging to moulds which have already been planned. The light grey part of the columns represents the workload imposed by a mould for which a production plan is being elaborated.

The information given by the graphic display of the different backlog lengths can be useful at various stages. During the enquiry stage this information can be used to help in the definition of reliable due dates. During the planning stage it can be used to choose appropriate routing for the mould components, e.g., seeking for a load balance between the different work centers. At the release stage they can be used to select an appropriate mix of components to be released. Furthermore, those graphics allow the user to recognize if starvation is expected in one or more work centers.

![](/api/attachments/Z8ECZCK6/fulltext/images/d0dc80eb4f6a9257981bcf5ca3b56f63245a482b9d58848b52dee8e141790031.jpg)  
Fig. 6. Execution register for a given work center.

![](/api/attachments/Z8ECZCK6/fulltext/images/566fe77f20030fdb4bb3dea75ba0b92eabfd82f86925f1e65cd370dd5af99858.jpg)  
Fig. 7. Planned backlog length for a given work center.

## 5. MAPP implementation

Implementing MAPP, and consequently the WLC concept, in this case study raised some new problems to which solutions were required. The main problems we found during this process were: (1) the practitioners’ apparent lack of knowledge about WLC, (2) the definition of work centers and (3) the definition of initial load limits for the work centers to bootstrap the use of the system.

## 5.1. Practitioner lack of knowledge about the WLC concept

During the implementation process we found that in this company the managers had no knowledge about the WLC concept. Unlike other production planning and control concepts, such as MRP or JIT, WLC does not seem to be widely known among practitioners. Therefore, when implementing a production planning methodology based on WLC, an effort must be made, at the outset, to explain its basic principles to the managers responsible for the implementation. Avoiding this problem in the future seems to require that the WLC be better disseminated among the practitioners, e.g., as part of formal academic training.

## 5.2. Definition of work centers

In relation to the definition of work centers, our first choice was to define a work center as a group of similar machines. For example, the four electro-erosion machines, each working 8 h per day, were considered a single work center with a capacity of 32 h per day. During the implementation tests we found that this option could lead to errors in calculating the time required to process the machines’ workload, because the jobs could not be split. Supposing that there was only one job in the job-shop, requiring 16 h processing in an electro-erosion machine, if we consider a single electro-erosion work center with 32 h of capacity per day, the time required to process the workload imposed by this job will be 0.5 day. In fact, since the job cannot be split, it will be processed in a single machine over two days. To avoid calculation errors of this kind we decided to consider each single machine as a work center. This problem will not exist if the jobs can be split among a set of machines comprising a work center, or if the planning horizon is divided in large time buckets rather than small ones, as in our case study. Note that in our case it was easy to consider each machine as a work center, due to the small number of machines that compose the job-shop. In job-shops with a large number of machines, this option can lead to unwanted complexity, imposing a heavy cognitive load on the manager using the production planning system, and possibly increasing the risk of human error while using the methodology.

## 5.3. Definition of load limits

The determination of norm values or mean queue lengths, required to set up MAPP was probably the biggest difficulty found during the implementation process. In fact, the determination of norm values is a difficult decision and, as stated in Ref. [9], it has not yet been crystallised. Our first option was to define identical norm values (maximum total, planned and release backlog length) and mean queue lengths for all the work centers, relating them to the desired manufacturing lead time as proposed in [6]. The choice of the preferred manufacturing lead time was discussed with company managers. Nevertheless, we found that our option led to a divergence between the calculated and the real workload for the work centers. The workload calculated for the support and CNC machines was usually less than the real workload in those machines. On the other hand the workload calculated for the assembly machines was larger than their real workload. This fact was due to the presence of a dominant flow in the job-shop. Therefore, the norm values and queue lengths were set by a trial and error procedure. This procedure is still in operation, and no conclusions about the best set of norm values and queue lengths have yet been obtained. This trial and error procedure is not the best for defining norm values since it consumes a large amount of time, which is usually not available when implementing a decision support system in a company which expects quick results. Therefore, the definition of a procedure to define accurate norm values is a subject requiring further research.

## 6. Conclusions

This paper describes MAPP, a web-based decision support system for the mould industry. MAPP is composed of two main modules (1) production planning, and (2) information and document management. The production planning methodology implemented in MAPP is an adaptation of the workload control concept developed at Lancaster University.

The case study company selected to implement MAPP designs and produces moulds for the plastic injection industry, operates in a make-to-order (MTO) environment, and can be classified as a versatile manufacturing company (VMC), since each product is individually made. MAPP was tested in laboratory using historical data from our case study company. The feedback from company managers about the tests is encouraging. MAPP seems to respond to the company needs in terms of production planning and information management.

We are now beginning field testing MAPP in the actual industrial environment. The system is being used in the company, but previous planning instruments are kept as a backup strategy while the system is being field tested. Besides providing a certain amount of confidence, these backup plans make it possible to compare the production plans provided by MAPP with those obtained by the production planner, using previous planning instruments, like MSProjectR. We expect that this industrial implementation of MAPP will lead to the achievement of company goals, and validate the applicability of the generic methodology developed at Lancaster University to the mould industry.

## Acknowledgment

This research was supported in part by the Portuguese Foundation for Science and Technology (FCT) under the contract POCTI/EME/38516/2001.

## References

[1] G.M. Amaro, L.C. Hendry, B.G. Kingsman, Competitive advantage, customization and a new taxonomy for non make-to-stock companies, International Journal of Operations and Production Management 19 (4) (1999 Apr.).

[2] W. Bechte, Theory and practice of load-oriented manufacturing control, International Journal of Production Research 26 (1988 Mar.).

[3] D. Bergamashi, R. Cigolini, M. Perona, A. Portioli, Order review and release strategies in a job-shop environment – a

review and a classification, International Journal of Production Research 35 (1997 Feb.).

[4] J.W.M. Bertrand, The use of workload information to control job lateness in controlled and uncontrolled release production systems, Journal of Operations Management 3 (1983 Feb.).

[5] A. Christman, J. Natsmith, Mold Machining Today, Modern Machine Shop Online, Gardner Publications, Cincinnati, 2001 (May).

[6] L.C. Hendry, A Decision Support System to Manage Delivery and Manufacturing Lead Times in Make-to-Order Companies, PhD Thesis (University of Lancaster, 1989).

[7] B.G. Kingsman, Modelling input–output workload control for dynamic capacity planning in production planning systems, International Journal of Production Economics 68 (2000 Oct.).

[8] B.G. Kingsman, I.P. Tatsiopoulos, L.C. Hendry, A structural methodology for managing manufacturing lead times in maketo-order companies, European Journal of Operational Research 40 (1989 Feb.).

[9] M. Land, G. Gaalman, Workload control concepts in job shops: a critical assessment, International Journal of Production Economics 46–47 (1996 Dec.).

[10] H. Neto, O Prazo dos Moldes: Respostas para uma Concorreˆncia Activa, O Molde, vol. 50, 2001 (Sep.).

[11] B. Oosterman, M. Land, G. Gaalman, The influence of shop characteristics on workload control, International Journal of Production Economics 68 (2000 Oct.).

[12] L. Roque, A. Almeida, A.D. Figueiredo, Context engineering: an IS development research agenda, Proceedings of the 13th ECIS – European Conference on Information Systems, Turku, Finland, 2004.

[13] D. Sadoski, S. Comella-Dorda, Three Tier Software Architectures [online], available WWW<sup>b</sup>URL: http://www.sei.cmu. edu/str/descriptions/threetier.html<sup>N</sup> (2000).

[14] C. Silva, J.M. Magalha˜es, Production planning in a make-toorder environment: the case of a mould manufacturer, Proceedings of the 1st EUROMA/POMS Joint Conference, vol. II, 2003, Como lake.

[15] M. Stevenson, L.C. Hendry, B.G. Kingsman, A review of new and established production planning and control (ppc) methods and their applicability to make to order (MTO) companies, Proceedings of the 1st EUROMA/POMS Joint Conference, vol. II, 2003, (Como lake).

[16] H.P. Wiendhal, Load Oriented Manufacturing Control, Springer-Verlag, Heidelberg, Berlin, 1995.

[17] O. Wight, Input/output control: a real handle on lead time, Production and Inventory Management 11 (1970 Mar.).

[18] J.D. Wisner, A review of the order release policy research, International Journal of Operations and Production Management 15 (1995 Jun.).

![](/api/attachments/Z8ECZCK6/fulltext/images/1eeebe2ce4adb6bc18273ed02d898b1b7cf62524c5d7ee98860c390929b78491.jpg)

Cristovao Silva was born in 1968 in France. He studied Mechanical Engineering at the University of Coimbra, where he graduated in 1992. He received his M.Sc. and Ph.D. from University of Coimbra, in 1995 and 2000, respectively, both in the area of Industrial Management. He is presently an auxiliary professor of the Mechanical Engineering Department of the University of Coimbra. His research focuses on

workload control concept, and production planning in the process industry.

![](/api/attachments/Z8ECZCK6/fulltext/images/36c7723c7e028ec91236ced4754be907465bce4f1c1d34e2212aa2c7aeac6eec.jpg)

Licı´nio Roque was born in 1968 in Portugal. He studied Informatics Engineering at the University of Coimbra, where he graduated in 1993. He is presently professor at the Department for Informatics and Engineering of the University of Coimbra and a researcher at Laboratory of Informatics and Systems, a business unit of the Instituto Pedro Nunes association for innovation and technology transfer. His research focuses on socio-technical methodologies for

Information Systems Development (ISD) with a special interest in networked application contexts with fast change requirements.

![](/api/attachments/Z8ECZCK6/fulltext/images/69441beb72379114e9404bde40c250235bfb84e7e7407ee099f6f37e5b03c7e1.jpg)

Ana Sofia Almeida was born in 1970 in Portugal. She studied Informatics Engineering at the University of Coimbra, where she graduated in 1993. She is presently executive director, researcher and project leader at Laboratory of Informatics and Systems, a business unit of the Instituto Pedro Nunes association for innovation and technology transfer. Her research focuses on Information Systems Development (ISD) methodology and the valuation of the organisational transfor-

mation that occurs within ISD processes. Her background training has been on human–computer interaction (HCI) and user-centred design of collaboration systems, socio-technical methodologies for ISD and the valuation of innovation.
