---
otero_id: 26069
otero_key: "4CZQFFDD"
title: "Analysis, design, and development model: a case study of an internet‐based system for insert and parameter selection"
authors: "Bahador Ghahramani"
year: "2004"
journal: "Information Systems Journal"
doi: "10.1111/j.1365-2575.2004.00169.x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Analysis, design, and development model: a case study of an internet-based system for insert and parameter selection

Bahador Ghahramani

College of Information Science and Technology, University of Nebraska at Omaha, Omaha, Nebraska 68182, USA, email: bghahramani@mail.unomaha.edu

Abstract. The analysis, design, and development model (ADDM) is based on the systems lifecycle process (SLCP) in which analysts begin to understand external client requirements and internal client specifications as they are designing and developing a complex system. In the ADDM, clients and system analysts (SA) continuously interact as the system is being designed, developed, tested and maintained. In the design phase, system development can be altered when it is most cost-effective. Depending on the type of environment and SA preference and expertise, various interfaces and software and hardware configurations are created during the SLCP. The SLCP ensures effective standardization and continuous quality improvements throughout development. The model follows modern information technology principles to integrate and monitor SLCP phases. A case is presented that describes an application of the ADDM. This case outlines the architecture of an e-commerce production system (ECPS). The system has a three-tier structure consisting of the client interface, Java server page (JSP) and database module. The model assists in designing economic production operations in an industrial setting by allowing a client to retrieve current production data needed for operations through the internet.

Keywords: systems design and development, systems lifecycle process, information technology, internet-based system for production, concurrent engineering integrated product development

## INTRODUCTION

The analysis, design, and development model (ADDM) is a model through which system analysts (SA) incorporate external client requirements and internal client specifications throughout the systems lifecycle process (SLCP) phases. The model is a modern approach in which the clients and SA collaborate and cooperate throughout the develop ment process. Collaboration begins at the concept phase of the SLCP when it is most cost-effective to implement change. As the new system is developed, hardware and software products are created depending on approved requirements, specifications, and SA preferences. In addition, the model ensures that all products adhere to strict IT standards, practices and guidelines. The model’s phases and their relationships are shown in Figure 1 schematic.

The objectives of the ADDM are to:

improve the method of system development to ensure that the SLCP actually takes place;

standardize the process;

use a common language to describe the phases;

create a framework in which tools are used; and

integrate the function of client–machine interface, otherwise known as human factors.

The ADDM consists of 12 primary SLCP phases: requirement and specifications, preliminary conceptual design, program planning, project planning, logical design and architecture, detailed design and production, system development, production, distribution, evaluation and modification, operational use and maintenance, operations, and retirement. In the system design and development environment, SA may modify the 12 primary phases into the seven phases shown in Figure 1. For simplicity, the seven phases of the model are further combined into the following three stages or categories (Baker, 1997):

![](/api/attachments/4CZQFFDD/fulltext/images/be4ab4ab49a7143a0df7ab3a53799951d2d1f679ef72d5b65ac06c461582eb9a.jpg)  
Figure 1. ADDM phases and framework

![](/api/attachments/4CZQFFDD/fulltext/images/163bc2c774970907adcd478675d960206784206222b6ca3ba09f64ff3ede1817.jpg)  
Figure 2. ADDM three stages and their relations with the developmental efforts.

• Definition – translates the requirements into specifications, and then drafts the concept of the architecture for the system.

• Development – takes detailed specifications of the system, designs the logical model of the system, and assembles it.

• Deployment – evaluates the system to determine if it complies with requirements and spec ifications, and meets efficiency, effectiveness, and functionality standards.

ADDM addresses various system products in terms of the seven SLCP primary phases and the following analyses: requirement analysis, function decomposition, data analysis, logic specification, design and development reports, and testing and maintenance procedures (Blanchard & Fabrycky, 1998).

In order to develop the new system efficiently, SLCP identifies system clients, hardware and software, products, services, and environment. The developed hardware and software products depend on type specifications, but they also must have the ability to interface with each other. Each product includes, in addition to a definition statement, the following information:

rationale – the product justification;

client – the internal and external clients of the system; and

analyst – the primary system developer.

This model suggests checklists for various examples of SLCP specifications to help the SA standardize their development efforts, as displayed in Figure 2. Figure 2 displays the model’s three stages and their relations with the development efforts. This analysis includes a descrip tion of the workings of the ADDM as well as the analysis of an application of the ADDM (Dargan & Hermes, 1997).

## RATIONALE

External clients and internal clients of new systems play integral roles in the SLCP because of the growing demand for system customization. For example, different systems with various capabilities are developed and tailored to meet local requirements. IT breakthroughs take SLCP to a new level with tools, such as computer-aided design, computer-aided manufacturing, computer-aided software engineering, etc. New tools enable rapid product development, flexible production lines, and mass customization. Internal organizational structure, culture and processes are static in nature, and thus much time is needed to push changes through to the next level (Dargan et al., 1997). Therefore, it is wise to observe modern trends in information technology (IT) and plan the implementation of changes well ahead of time. Ireson et al. have outlined some of the changes in SLCP that are anticipated to shape the future of IT (Ireson et al., 1995):

• Reduced dependency on system acquisition and development – physical implementations of hardware and software are no longer a problem; designing a system with the client in mind is the challenge (Fitzer, 1997).

• Greater focus of IT on system reliability and maintainability – the total cost of ownership is more important than the total cost of the system (Lyu, 1995).

• Greater cohesiveness between the different phases of the system development lifecycle and wider use of concurrent engineering (CE) – the level of integration of various stages of IT is positively correlated to the level of success of the systems (Marz & Plakosh, 2001).

• More software-intensive systems – software offers cost-effective solutions to many IT problems (Pine et al., 1993).

• Greater commercial focus of IT – the commercial focus enables system managers to prepare their market plans and sales forecasts effectively to product and service demands (Carpenter & Maropoulos, 1999).

The rationale for a structured ADDM comes from practice:

• There are more complex interrelationships between architectural design and client requirements and also between architectural design and component development (Hoffer et al., 1999).

• Complex systems have more than just a single level of each process, depending on the nature of the system, the degree of maturity risk in subsystems and components, and the number of different components involved (Latino & Latino, 1999).

## THE MODEL

The ADDM is an IT system that is based on the SLCP philosophy of the continuous improvement in the quality of products against predefined characteristics. The SLCP starts with client requirements and uses them as the primary foundation for system development and architecture (Figure 3). The requirement phase defines the software, hardware, and interfaces to be developed in terms of system capabilities and constraints. These requirements include man agement and such contractual information as cost, time constraints and boundaries, and risk. These requirements originate from system clients at every phase of the SLCP. The SA then use these requirements to develop system specifications and architectures, to prepare process flows, and to plan alpha and beta testing procedures (Fox et al., 1993). SLCP has two spec ification iterations:

![](/api/attachments/4CZQFFDD/fulltext/images/a822922d2ce677c5636460185473880ddd252c7f1bdee863e9a098a3cee761b6.jpg)  
Figure 3. The ADDM architecture.

• Definition specification – establishes feasibility and the risks involved to proceed to the next phase.

• Proposal characteristic – leads to developing new components after approval of the specifications.

After establishing the system specifications, the SLCP defines how a system is developed and tested. The architectural design phase addresses key components, interfaces, contro structures, environment, and external systems. From this phase, a concrete plan of action is prepared and completed. The ADDM products and services are then developed, delivered, and installed into the clients’ environment (Igobaria, 1998).

The verification phase of the system involves assessing the SLCP deliverables and comparing them with IT best practices and standards. Standardization establishes common IT criteria, terms, principles, practices, materials, items, processes, software and hardware, parts, subassemblies, and assemblies to achieve uniformity of procured items. Standardization insures a minimum variety of items, practices, and facilitates. It also helps interchangeability of hardware and software within a system (Govil & Magrab, 1999)

## Scope of the mode

The scope of the model extends to requirements management, portioning the system into components, integrating components into a complete system, and testing the system against predefined specifications. SA recognize component development as one of the most important functions of the process. This step addresses risk management, resolution of interface agreements, and change management. On the other hand, component development is primarily concerned with production of the final system. The ADDM categorizes the SLCP into three activities that supplement the SLCP and the three production stages (Lykins, 1997):

• System acquisition – focuses on defining the Client Specification Document, and then checking the installed system against the client requirements.

• System development – implements the clients specifications by addressing the issues posed by the specifications, procuring the correct software and hardware components, and testing and bridging the components into a functional system.

• Component development – uses the specifications to develop a detailed design for each system component.

The model includes component interrelationships to develop dependencies between architectural design and client requirements, which carry information from the proposed design that then leads to the final product. The model performs risk and cost–benefit analysis to determine whether the architectural design is technically sound and feasible (Marz et al., 2001).

The ADDM is a system composed of various interdependent and interactive subsystems. This composition initiates multiple levels of SLCP efforts. The number of levels depends on the nature of the system, the degree of maturity and risk in potential subsystems and components, and the level of technology required. It is a recursive model that aligns itself with reality and encompasses a wide variety of scientific tools and IT technologies.

## System management

The system management phase of the SLCP is essential for successful completion of complex and modern systems. System management considerations and interaction issues dictate SA selection of a technology. The major problems associated with development of trustworthy sys tems, whether process or product, have more to do with the organization and management of the system complexity than with direct technological concerns. To ensure that systems are developed according to the pre-approved requirements and specifications, considerable emphasis must be placed on the front-end phases of the SLCP (McGraw & Harbinson, 1997).

The model is concerned with resolving scheduling and interfacing issues at every SLCP phase. In addition, it identifies and develops individual components prior to the actual system integration phase. This system integration module consists of two phases that mainly address the lower level components of engineering management and acquisition management.

• Engineering management – concerns the monitoring of the lower level component suppliers and preparing them for the integration and verification phase that will take place when the com ponents are delivered. Another function of the engineering management phase of the model is to handle scientific aspects, such as risks, costs, and consequences of change requests.

• Acquisition management – operates at a higher level than the engineering management level and deals entirely with client and client-related issues. The development of acceptance tests occurs during this phase.

Acquisition management managers assess the initial risk to the SLCP by implementing risk management techniques prescribed by the SA. The process of assessing and reporting risk will continue with clients at each level of development. Subsequently, the risk levels and the degree of control are established between SA and clients. Acquisition managers are also con cerned with safeguarding client interests during the development phase of client specifications and system delivery. They monitor the development and review processes, provide recom mendation and clarification to SA and clients, and prepare the operational phase. In addition, they work with SA to prepare contract specifications that are binding at each level of the SLCP (Lewis, 1994).

Most system failures are caused by organizational and management factors, not by hard ware, software, or their integrations. SLCP develops a product in response to the SA specifi. cations, not verifying the validity of the information (Bowman et al., 1991). In many cases, system failures are caused by imprecise definition of the purpose, the function, and/or the structure of a project. System management is responsible for minimizing such risks. System management and integration determine the functionality, effectiveness, and efficiency of the whole system (Gailkowsky et al., 1996).

## Model’s applications

Application of the ADDM occurs in the following phases:

• Pre-commitment phase – combines the system acquisition with the system requirements and articulates the design phase. This is a fact-gathering phase and involves pro gressive recursion. This phase requires a detailed feasibility study of the SLCP lower levels and its components. Among the activities initiated during this phase are allocating requests for each component at lower levels, obtaining proposed characteristics of these components, managing risks and comparing costs and benefits of each phase, product, and component.

• Monitoring phase – combines the acquisition management and management contro phases. It involves recursive inter-level contracting with associated reporting, encompasses notions of project and subproject, and incorporates the use of subcontractors. As part of this phase, the SA report problems and their solutions, manage projects, control subcontractors, allocate resources, schedules activities, and quality check products and services at random intervals to minimize bottlenecks and mishaps.

• Build and test phase – encompasses a set of two phases of the system: the installation and validation phases of system acquisition, and the integration and verification phases of system development. It involves recursive inter-level delivery and testing of components to form, install, and accept the required system. This phase also includes delivering products, testing components, installing hardware and software, modules and equipments, and accepting the completed system.

## Model’s capabilities

The model is capable of developing a detailed risk assessment plan for every SLCP phase that includes a comparative evaluation of the cost–benefit analysis in the early development phase. The detailed level of the risk assessment plan not only depends on the degree of measurement required by the client and SA, but also the trade-offs between performance and cost. The assessed risk is added to the estimated expense of the system to determine its expected completion cost. Expected completion cost includes development, operations, decommissioning, and contingency expenses to cover any unforeseen and potential SLCP problems. Risk management is critical, and its measurement depends on scientific tools and information technologies used in the SLCP (Ebeling, 1997).

The SLCP levels will contain product requirements in addition to management planning and budgeting for that component. The complete contract (one level higher and lower) would comprise individual product requirements, acceptance and commercial criteria, and reporting requirements to the clients. There is also continuous monitoring of the acquisition management, engineering management, and SA activities during the development phase of the SLCP against the agreed plan (Leung & Yuen, 2001).

The manual selection of the production resources and the parameters requires great skil and decision-making. The selection involves a systematic and tedious procedure adopted from the required production specifications and parameters. There are many predetermined factors, which have to be considered before initiating resource selection. Because of the complexity associated with the cross-referencing of standards and immediate response to related problems, the likelihood of erroneous selection increases. The ADDM changes the manual selection and provides the clients with an online method of identifying and selecting the best possible resources for their products.

## MODEL’S PROCESS

SA are aware of the fact that the higher the complexity of the system under development, the more multidisciplinary the design process tends to be. This demands an innovative, highly integrated process where the product manager must frequently address anticipated solutions. Furthermore, most design and development functions of the SLCP are carried out in parallel to meet time constraints. Upon completion of the structured SLCP that is customized to the needs of the system, the SA are able to realize the devel opment problems and determine client priorities (performance, cost, schedule, risk, etc.). In addition, the SA employ effectiveness criteria to make system decisions, establish and manage specifications, identify and assess alternatives so as to converge on a solution, verify and validate specifications and solution performance, maintain the integrity of the system, use an articulated and documented process, and manage against the plan (Fitzer, 1997).

The SA attempt to answer the following process-related questions before developing the SLCP blueprint and architecture, displayed in Figure 4:

• What is the process for? (the ‘why’)

• What does the process do and what is it used for? (the ‘what’)

• How does the process perform? (the ‘how’)

![](/api/attachments/4CZQFFDD/fulltext/images/2867b26476ffeca836f027d0f5da8c070e7e14be1e0d27d3076c11e5c53cd7a5.jpg)  
Figure 4. An overview of the ADDM development process.

SLCP stresses the ideas of new systems’ expediency and feasibility. The SLCP development process is a collection of interdependent activities that result in the definition, development, and deployment of hardware and software that might be incorporated into the new system. First, market needs are assessed to determine detailed product specifications. Second, the product prototype is designed, and production process specifications are established. Because of production process specifications, production process design is outlined. Third, the operation of the production process is initiated. Fourth, the system re-engineering begins (Goldman, 1998).

## SLCP DEVELOPMENT

The SLCP development concept is presented from two different perspectives: as a process-oriented notion and from a functional perspective. Process view is the management technology that controls an SLCP and results in the definition, development, and deployment of a system that is of high quality, trustworthy, and cost-effective in meeting clients’ specifications. The SA analyse the SLCP as a sum of three knowledge components (Gremba & Myers, 1997):

• Knowledge perspective – relates to future technology direction and realities.

• Knowledge principle – represents a formal problem-solving approach, and employs modern or innovative technologies.

• Knowledge practice – represents the accumulated wisdom and experience that leads to the development of standard operating policies for a well-structured system.

Each one of the above knowledge components leads to another. As an example, knowledge perspective may create the incentive for research that leads to discovery of new knowledge principles; as knowledge principles emerge and are refined, they generally become embedded in the form of knowledge practices. The three types of knowledge components interact with each other and create a natural flow of information across the SLCP phases: planning and marketing; designing, developing, testing, and maintaining; and following-up.

The sequence of knowledge types corresponds to the sequence of SLCP phases: system planning and marketing research, development, testing and maintenance, and system acquisition, manufacturing, production or procurement. Therefore, knowledge practices originate from the knowledge principle, which in turn derives from the knowledge perspective.

SLCP differentiates between component development and system development:

• Component development – is concerned with the production of the elements, which are parts of the final system.

• System development – is responsible for assembling system components, but its role is one of technical management.

In production, the SLCP focuses on three types of development concepts: job shop and batch production (small batches or single products are manufactured), mass production (high volumes of products are manufactured), and continuous production (production goes on constantly over time). With the new market developments, a need for new production systems arises that is reconfigured to satisfy changing product lines in response to market volatilities (Figure 5).

The SLCP therefore satisfies three ADDM functions: (1) system objectives; (2) system design; and (3) system development through its two primary interactive and interdependent modules (Figure 6):

• Measurement module – includes research, development, quality assurance, and assessments.

• System module – includes system technologies, system applications, and system improvements.

![](/api/attachments/4CZQFFDD/fulltext/images/d3ea7faa631849a571c6d7151d7bd400f0580d9ed87607a656ce1e38e1680a72.jpg)  
Figure 5. A functional presentation of the ADDM lifecycle process.

![](/api/attachments/4CZQFFDD/fulltext/images/2ff107b3dd499b72c7745f54d90aea58c7d577dc3abb07432f54b4683dc65aa0.jpg)  
Figure 6. The SLCP continuous quality improvement process.

## TECHNOLOGIES USED

The SLCP uses the most modern and advanced technologies to develop systems. The mode places emphasis upon development of more advanced and sophisticated forms of system development using the concepts of concurrent engineering (CE) and other related technologies, such as integrated product development (IPD). CE is used to enhance the systematic completion of the SLCP phases and to integrate various development phases. The basic tasks in CE concentrate on a controlled environment reaching the following objectives (Lewis, 1994):

high quality in terms of system performances, suitability, and reliability in a large variety of operational environments;

• short deployment time. for new product and service design. and for delivery and maintenance of existing product designs; and

minimum lifecycle cost.

CE is one of the techniques designed for rapid development of products, often accomplish ing different lifecycle process phases at the same time. CE enables rapid development of costeffective functional systems that accommodate client requirements. Especially important for CE are co-ordination and management of developmental efforts, which require a great deal of careful planning at the organizational level. Three elements are critical for CE (Malaiya & Sri mani, 1990):

Correct understanding of client requirements and preferences. Efforts should take place to research client requirements and to transform them into set of specifications. This task requires extensive marketing skills.

• Translation of specifications into products and production processes.

Constant improvement of products and systems. Review and redesign are the follow-up activities SA may perform beyond the point of system’s final delivery.

IPD is a more modern application of the CE that was used to improve the SLCP. Similar to CE, the IPD is also a system management philosophy and approach that uses functional and cross-functional work teams to develop an efficient and effective SLCP for the ultimate deployment of products that satisfy client requirements through concurrent application and integration of all related lifecycle activities. The SLCP uses IPD philosophy to initiate and enforce the following 12 mission statements throughout its system development efforts (Sage, 1992):

Client satisfaction

• Integration engineering

Result oriented

Teamwork and communications

Process re-engineering

Client empowerment

Strategic planning and marketing

System managemen

Concurrent engineering

Methods, tools, and techniques

Organizational culture and leadership

Continuous quality improvement

The major impact of CE and IPD is their use in the decision-making process. These technologies help SA make the necessary decisions at the appropriate time and enhance their efforts to optimize their resources in order to achieve the following three interdependent objectives: management objectives, process objectives, and product objectives diagrammed in Figure 6. Figure 6 is a functional presentation of the SLCP to:

integrate individuals, organizations, and technologies into a set of multifunctional and net worked product development teams;

increase the quality and timeliness of decisions through centrally controlled decentralized and networked operations; and

completely satisfy clients through quality products and services.

Successful use of CE and IPD depends on the balance between four components of the SLCP: organizational culture and leadership. communications infrastructure of the organization, recognition of client needs and requirements, and product and process development (Stalling, 1999).

## MEASUREMENTS

Different types of measurements are attributed to systems with different levels of process maturity. Inactive and reactive cases relate to low process maturity organizations while proactive and interactive cases relate to systems with high maturity level. With a wider adoption of proactive and interactive cases, the need for reactive and inactive measurement becomes less urgent as most of the system problems are solved through the interactive and proactive measurements (Gailkowsky et al., 1996).

SLCP forms a functional point of view that encompasses the art and science of system development. In order to appropriately practise ADDM, there is a need for a systematic measurement that can be selected from one of the following four categories (Tai et al., 1996):

• Inactive measurement – denotes an organization that does not use metrics or that does not measure at all, except perhaps in an intuitive and qualitative manner.

• Reactive measurement – denotes an organization that performs an outcome assessment after it has detected a problem or failure, that diagnoses the cause of the problem and, often, that eliminates the symptoms which have caused the problem (Ebeling, 1997). It is performed in response to an existing problem.

• Interactive measurement – denotes an organization that measures an evolving product as it moves through the various phases of the lifecycle process in order to detect problems as soon as they occur. It is used for formal purposes to determine whether a product has defects or problems with the intention to correct them as soon as they appear.

• Proactive measurement – predicts the potential for errors and minimizes their occurrences in order to minimize the likelihood of the failure. It is designed to foresee the problems or errors in a particular phase of the lifecycle process.

## Measurement algorithms

The ADDM measures a system’s development process as a function of its total performance cost during the developmental stages. This measurement is also closely associated with system failures and their impact on clients (Ehrlich et al. 1990). Developmental measurement therefore depends on cost of reducing and eliminating hardware and software failures throughout the continuous lifecycle quality improvement phases. The model then measures the cost of reducing and eliminating hardware and software failures as an assessment of system performance (Franklin, 1993). It assumes $C _ { i } ( t )$ to be the cost of fixing failures of component i during time t.

$$
C _ {i} (t) = c _ {u} (t) + c _ {c} (t) \cdot c _ {u} (t) + c _ {e} (t)\tag{1}
$$

where

c (t) ∫ cost to the users at time t

c (t) ∫ cost to the clients at time t

c (t) ∫ cost to eliminate a failure at time t

To determine $C _ { i } ( t )$ , the ADDM computes $c _ { c } ( t )$ by simplifying Equation 1 that is positively cor related with the performance rates of component i at time t.

$$
c _ {c} (t) = \frac {d c}{d t} = \left(\frac {d c}{d m}\right) \cdot \left(\frac {d m}{d r}\right) \cdot \left(\frac {d r}{d t}\right)
$$

or

$$
c _ {c} (t) = f _ {i} (t) \cdot m _ {i} (t) \cdot r _ {i} (t)\tag{2}
$$

where

f (t) ∫ cost of failures in component i during time t

m (t) ∫ cost of errors caused by failures during time t

r (t) ∫ cost of instructions to remedy failures during time t

Accordingly, $c _ { u } ( t )$ part of Equation 1 is both a function of the failures caused by software and hardware and the probability of their occurrences at time t.

$$
c _ {c} (t) = f _ {i} (t) \cdot p _ {i} (t)\tag{3}
$$

where

p (t) ∫ probability of component i failures at time t.

To determine the total cost of fixing component i failures during time t, or $C _ { i } ( t )$ , the model sim plifies Equation 1 by inputting the results of Equations 2 and 3.

$$
C _ {i} (t) = [ f _ {i} (t) \cdot p _ {i} (t) ] \cdot [ f _ {i} (t) \cdot m _ {i} (t) \cdot r _ {i} (t) ]\tag{4}
$$

or

$$
C _ {i} (t) = [ f _ {i} (t) ] ^ {2} \cdot [ p _ {i} (t) \cdot m _ {i} (t) \cdot r _ {i} (t) ]\tag{5}
$$

It is therefore possible to measure the reliability of a system’s development phases by measuring total cost of its performance from its concept to its delivery period T for its n components

$$
C _ {i} (T) = \sum_ {i = 1} ^ {n} \left\{\left[ f _ {i} (t) \right] ^ {2} \cdot \left[ p _ {i} (t) \cdot m _ {i} (t) \cdot r _ {i} (t) \right] \right\} \quad i = 1, 2, 3, \dots , n \text {   and   } t = 1, 2, 3 \dots , T\tag{6}
$$

## THE CASE

This case outlines the architecture of an e-commerce production system (ECPS) using the ADDM. In analysing this case, an attempt was made to address the areas that are technology specific and that were not included in the previous parts of the analysis. In addition, because of space limitations, the areas that are clearly mapped with the ADDM phases are not addressed here.

The system has a phase structure including end user, Java server page (JSP), and a database module (refer to Introduction). A client can retrieve production data needed for a sequence of operations remotely through the internet, and the system assists in economic operations in various size companies (Alexander $\&$ Tate, 1999). The ECPS is divided into three categories: client interface module, server side programs developed in common gateway interface (CGI) and a database module containing two databases (primary and scientific) storing production information.

The case is also based on the SLCP and presents the development of an ECPS for production operations. If a production operation requires the use of an efficient and cost-effective process, the computer-aided process planning (CAPP) system activates ECPS through the internet to receive the most appropriate resources and parameters for the required operations (Huizing, 2000). Moreover, ECPS assists remote clients, especially small- and medium-sized companies without advanced technologies, in the selection process of their production resources and parameters. With the assistance of the system, a company that lacks highly qualified SA can still effectively design and select the optimal production resources and parameters for their production operations (Lee et al., 1999).

In addition, ECPS technology provides production tools that develop products with improved accuracy and economies. Economy depends largely on proper selection of the resources and parameters that are required to successfully complete a sequence of operations and to develop a product. In turn, the volume of production also influences the selection process. The previously described algorithms (Equations 1–6) are used to measure and evaluate the feasibility and utility of each of the production operations (Bedworth & Bailey, 1987).

## Case’s background

Production is a systematic approach that re-engineers the form of raw resources and materials to develop products of specific requirements (Carpenter et al., 1999). The e-commerce production permits the flow of information through lifecycle development phases of the process. As the result of e-commerce applications, there is a significant increase in the use of internet combining operations, mechanizing processes, and integrating lifecycle development phases, thus reducing production process time and expenses. E-commerce applications therefore have become significantly more complex, remote, and mechanized. To meet the requirements of clients and SA specifications, the ECPS consolidates all aspects of production operations.

Recent advances in IT have also enhanced development of internet-based production systems capable of aiding clients in selection of resources and parameters online (Mark, 2000). The production environment is perhaps changing more rapidly now than the 19th Century Industrial Revolution. The ECPS helps its clients to successfully compete in the market with: (1) shorter duration between order and delivery; (2) smaller intervals between product conceptualization and realization; (3) greater product customization; (4) higher product quality and performance; and (5) lower production costs (Sage, 1992).

To improve the efficiency of product realization, the system effectively offers production support. The rapid expansion of high-performance internet networks allows product developers, using ECPS, to electronically integrate their activities, to take advantage of emerging markets, and to develop new products (Van Vilet & van Luttervelt. 1999)

During the CAPP phase and in conjunction with the internet network system, the SA employ agile production in performing production and operation research. If a product requires a sequence of operations during process planning, ECPS activates the CAPP through the internet to provide the most cost-effective resources and parameters employing the measurement algorithms (McGinity, 1999).

## Case’s technology

With the development of the ADDM, resource and operation research has shifted towards the remote control of the production processes. Modern advances in ADDM technology, production systems, IT, and highly reliable communication systems are creating an environment of collaborative design. These advances are enabling distributed procedures in CE design, remote operation of production processes, and operation of distributed production systems to become more feasible. In addition. recent advances in IT have created an ideal environment for experimentation in the development of internet-based production systems capable of aiding the online selection of materials and resources (van Vilet et al., 1999).

Research in this area focuses on achieving rapid response to client requirements, security of proprietary information, and high product variety that are proving to be important factors for ensuring success in the market place. Network and IT have opened up other domains for build ing future computer-aided design (CAD) and computer-aided manufacturing (CAM) or CAD/ CAM technologies and for improving the ECPS to become more global, network-centric, and spatially distributed. ECPS-layered production is also a new concept that is used for the efficient application of CE design. The ECPS also uses a web-based and user-friendly virtua design and fabrication system to maximize its efforts (Stallings, 1999).

## Case’s system

The use of ADDM technology, the presence of the internet, and the availability of the world wide web (WWW) offer a new and rich environment for information interchange and for access to computer programs that run in a client/server mode. With the unification of text, graphics, video, sound, and interactive applications, the WWW provides the means for client integration with software programs and other server information (Alexander et al., 1999). Through a web interface, remote clients on the internet can access a software application, provide any nec essary input, and view and download the results. This has initiated the research on development of new systems for production of finished goods to reduce the cost and time from initia design to customer-ready products (Sun & Martin, 1999).

For a variety of products, the ECPS remotely integrates CAD, CAPP, and CAM software through the internet, and the system loads them onto its distributed servers. A client first designs the product on the CAD system, and then calls the CAPP system, which may be avail able on a different server, for process planning and route sheet preparation. Group technology, a collection of parts that are similar either in geometric shape or in processing steps, is called during the CAD and CAPP processes. Finally, the files generated by CAD and CAPP systems are transferred to the CAM system where the actual production takes place through the loca computer numerical control (CNC) monitoring and control centre (Higgins & Langrana, 1999).

## Case’s database module

The ECPS database module consists of two databases: the primary database and the scientific database. These two databases are developed in a Window NT operating environment. With the use of these two databases, SA are able to minimize the time-consuming new product design period, planning period, and even the research period. The primary database contains information about commonly used work and production materials with their properties, static and dynamic performances of various resources needed for the CAPP. The scientific database has standard models for computing parameters for engineering analysis and design, production tools and other critical factors (Goldman, 1998). The scientific database for resource information is created using Microsoft Access. This database is accessible to SA through the internet and is used for production applications. The scientific database also uses the measurement algorithms to perform feasibility studies, cost and benefit analysis, monitor expenses, and compute total cost of each operation.

ECPS bridges to companies of all sizes, but in their resource selection and a set of parameters, they remotely assist system clients in major corporations. With direct control of the system, a company that lacks highly qualified SA is capable of easily designing and selecting the best resources and parameters for production operations (Huizing, 2000).

## Case’s architecture

The ECPS is developed in a client/server environment and is based on ADDM technology. The system is also developed as a CAPP module for the internet-based network system. As more modern and advanced production tools are adopted, production operations become more complex and costly. This technology evolution directly affects producer profit margin. ECPS focuses on obtaining precise data and maintaining the competitive advantage for companies using the system. The system is fundamentally divided into three architectural modules: client interface, server side programs, and databases (Hardekoph et al., 2001).

The client interface, which is in the form of a web page, is developed in HTML. The web pages are either dynamic or static. Dynamic web pages are developed as outputs of the CGI programs and are designed to guide the clients in selection of various production resources. The clients are also able to access various online forms through the web pages. These forms provide clients with images and visual representation of the resources. The web pages also allow clients to transfer their resource selections and completed forms to the primary database, which are in the server side CGI programs. The information received from the CGI programs are also in HTML and accessible to the clients on the browsers (McGraw et al., 1997).

The ECPS input forms use the supplied values to run the CGI programs that are on the web server. The CGI programs on the server side are developed using Visual Basic that helps the conversion of the client input to a Structured Query Language (SQL) format query and retrieve the required information from the primary database. The information received from the primary database is embedded into an HTML page and is transmitted to the client interface. The server side programs bridge the clients and the primary database. The CGI programs on the server end support the input forms and establish access to the scientific database. Each CGI program receives input from the form and processes the form using Visual Basic. A CGI script also con nects a client to the database engine that sends SQL and that accepts data returned from the engine (Leung et al., 2001). Figure 7 shows the concept of the client and server database technology and architecture used to develop the ECPS.

![](/api/attachments/4CZQFFDD/fulltext/images/67dcc89478f3fcef1b5d64b3959362ba99febe9de20475b8558dd8a219561feb.jpg)  
Figure 7. The ECPS database module architecture.

## Case’s structure

The ECPS for production operations is a system that when activated runs the CGI programs that are on the web server. The client interface consists of online forms that are embedded in the web pages that act as a bridge transmitting the required inputs to run the CGI programs that in turn provides the output of the programs on the web pages. Figure 8 is a block diagram showing the structure of the ECPS database module architecture and relationships between the primary database and the scientific database. As Figure 8 shows, the primary database and the scientific database are bridged with each other for easy access and navigation from one level to another, or from one page to another.

The remote clients access the ECPS for production resources and information using avail able web browsers, such as Netscape or Internet Explorer. The web browsers offer features, such as Java, to enhance the ECPS multimedia interface capability.

![](/api/attachments/4CZQFFDD/fulltext/images/75110918f5c42db963f687035ed842f1af5653dd2a936071f06500b58123cba4.jpg)  
Figure 8. The ECPS database module architecture and relationships.

To activate the ECPS, initially the clients are able to activate a sequence of two modules: (1) resource identification and selection: and (2) form completion and submission. The first web page of the system menu includes two buttons that directs clients to the two operations. The purpose of the first module is to provide clients useful information on identification and selection of resources and then query the primary database based on these selections. Because the first module contains a significant amount of resource information, they are further categorized into: (1) type of resources; (2) type codes and specifications; (3) operations required; and (4) query forms to complete. The basic architecture of the primary database and the scientific database are shown in Figure 8. In Figure 8 the actual flow of logic is in the direction of the arrows. The resources selected by the clients are sent as hidden fields from one page to another. The information in the hidden fields is collected by the CGI programs and is used for developing SQL queries to be sent to the primary database (Mark, 2000).

The second module uses the CGI programs to store the selected information and query the database to determine the resources that match clients’ specifications. If the system is not able to identify an exact match, the clients are provided alternate resources so that they can make the best possible selection. With each selection, to further guide clients, the system provides recommendations as to how proceed to the next step and to complete the query forms. Figures 9 and 10 represent the ECPS primary and scientific databases and samples of their tables.

![](/api/attachments/4CZQFFDD/fulltext/images/283ee2c6174460975c5a8b96fe72162ca21cdd54ecd4e7cc72d788462d7f9c44.jpg)  
Figure 9. Sample of the ECPS primary database tables.

## SUMMARY

The ADDM model helps SA to design and develop a production resource identification system using the SLCP continuous quality improvements to satisfy clients’ requirements. The rationale behind the ADDM is the growing demand for IT systems that are customized, user-friendly, and cost-effective. The ADDM also maintains continuous quality improvements throughout its SLCP developmental phases. Scope of the model focuses on requirement management, partitioning the system into components, integrating components into a complete system, and testing the system against pre-defined client specifications.

The system management of the ADDM ensures the clients that system development process encompasses continuous quality improvement principles and follows clients’ specifications. Applications of the model broadly cover the pre-commitment phase, monitoring phase, and build and test phase. The model’s process attempts to answer the ‘why’, the ‘what’, and the ‘how’ of the model. One important technology used in the model is the SLCP that is addressed throughout the analysis and the case. The SLCP primarily uses two new technologies: CE and IPD to effectively develop systems. The CE and IPD enable the ADDM to adhere to the continuous quality improvement philosophy of work. The model uses various measurement tools to assess various development phases and components. One of the measurement tools is an algorithm that assesses performance by measuring the total development cost of a component, module, or phase.

![](/api/attachments/4CZQFFDD/fulltext/images/bec3f2418e469f969793486321607ce6ad89742a9f67a250f6f8fd4cfc2aaa33.jpg)  
Figure 10. Sample of the ECPS scientific database tables

In the second part of the analysis, the ADDM technology is used to develop an internet-based system for selecting production resources. The ECPS is a part of the research work performed in the area of agile production, and is used during the CAPP phase of a production process. ECPS is a user-friendly interface with graphics or general guidance explaining the meaning of all input parameters for a client’s consideration. It provides the recommendations for resource and parameters selections when the client defines the resources and parameters. It also provides other choices so that the client can draw on to meet the actual requirement. The ECPS refers to a standard database and hence the systematic manual procedure is utilized with the computer programs developed to do the same work.

The ECPS is accessed through the internet, so small-scale companies can log on to the system and get a more reliable source for their resource selection. This makes the maintenance of software easy by eliminating the need to port the program to different platforms and distribute newer versions (Lee et al.. 1999)

## ACKNOWLEDGEMENTS

The author greatly appreciates his colleagues at the University of Nebraska at Omaha for their encouragements and support. This case and project would not have been possible without generous grants from the NJK Holding Corporation’s grants. The author wishes to express his appreciation to Dr Mark Pauley, Professors Theresa Stanton and Mary Levesque, and graduate students Louis Weitkam and Linfeng Cao for their editing and manuscript preparation. In addition, his sincere gratitude is given to Systems Engineers in the AT&T-Laboratories, Lucent Bell Laboratories and IBM Watson Research Center for their support and recommendations.

## REFERENCES

Alexander, J.E. & Tate, M.A. (1999) Web Wisdom: How to Evaluate and Create Information Quality on the Web. Lawrence Erlbaum Associates, Mahwah, NJ.

Baker, L. (1997) Lessons learned applying model-driven system design. Proceedings of the Seventh Annual INCOSE Symposium, 751–756.

Bedworth, D.D. & Bailey, J.E. (1987) Integrated Production Control Systems. John Willey & Sons, Inc., New York, NY.

Blanchard, B.S. & Fabrycky, W.J. (1998) Systems Engineering and Analysis. Prentice Hall, Inc., Upper Saddle River, NJ.

Bowman, W.C., Archinoff, G.H., Raina, V.M., Tremaine, D.R. & Leveson, N.G. (1991) An Application of Fault Tree Analysis to Safety. Assessment and Management, Apostolakis, G.E. (ed). Elsevier Publishing Company, Amsterdam, the Netherlands.

Carpenter, L.D. & Maropoulos, P.G. (1999) A process planning decision support system for milling operations. Proceedings of ASME Detc99/DFM, 1999 ASME Design Engineering Technical Conferences, Las Vegas, Nevada.

Dargan, P.A. & Hermes, M.A. (1997) Challenges in design ing open systems. Proceedings of the Seventh Annual INCOSE Symposium. 799–806.

Ebeling, C.E. (1997) Reliability and Maintainability Engineering. McGraw-Hill Companies, Inc., New York, NY.

Ehrlich, W.K. & Stampfel & Wu, J.R. (1990) Application of software reliability modeling to product quality and test process. Proceedings of the Twelfth International Con ference on Software Engineering, IEEE. CS Press, Los Alamitos, California.

Fitzer, M.M. (1997) Managing from afar: performance and rewards in a telecommunicating environment. Compen sation and Benefits Review. 29. 65–73

Fox, C., Levitin, A. & Redman, T. (1993) The notion of data and its quality dimensions. Information Processing and Management, 30, 9–19.

Franklin, P.H. (1993) Software-reliability prediction in a multiple-processor environment. Proceedings of the Reliability and Maintainability Symposium, Atlanta, Georgia.

Gailkowsky, C., Sivazlian, B.D. & Chaovalitwongse, P. (1996) Optimal redundancies for reliability and availabil ity of series systems. Microelectron and Reliability Jour nal, 36, 1537–1546.

Goldman, J.E. (1998) Applied Data Communication: A Business-Oriented Approach. John Wiley and Son, Inc., New York, NY

Govil, M.K. & Magrab, E.B. (1999) Designing for time-tomarket: predicting the effects of product design on production rate. Proceedings of ASME Detc99/DFM, ASME Design Engineering Technical Conferences, Las Vegas, Nevada.

Gremba, J. & Myers, C. (1997) The IDEAL model: a practical guide for improvement. Carnegie Mellon Software. Engineering Institute ‘Bridge’, Issue 3.

Hardekoph, B., Kwiat, K. & Upadhyaya, S. (2001) Secure and Fault-Tolerance Voting in Distributed Systems. Air Force Research Laboratory, Wright Paterson Airforce Base, OH.

Higgins, K.B. & Langrana, N.A. (1999) Web-based, userfriendly design and virtual fabrication for lavered manufacturing. Proceedings of ASME Detc99/DFM, 1999 ASME Design Engineering Technical Conferences, Las Vegas, Nevada.

Hoffer, J., George, J. & Valacich, J. (1999) Modern System Analysis and Design. Addison-Wesley, Boston, MA.

Huizing, E. (2000) The content and design of web sites: an empirical study. Information and Management, 37, 123– 134.

Igobaria, M. (1998) Special section: managing virtua workplaces and teleworking with information technol ogy. Journal of Management Information Systems, 14, 5–86.

Ireson, W.G., Coombs, C.F. & Moss, R.Y. (1995) Handbook of Reliability Engineering and Management. McGraw-Hill Companies, Inc., New York, NY.

Latino, R.J. & Latino, K.C. (1999) Root Cause Analysis Improving Performance for Bottom Line Results. CRC Press, Boca Raton, FL.

Lee, J.Y., Kim, H. & Han, S.B. (1999) Web-enabled feature-based modeling in a distributed design environ ment. Proceedings of ASME Detc99/DFM, 1999 ASME Design Engineering Technical Conferences, Las Vegas, Nevada.

Leung, H.N. & Yuen, T.C. (2001) A process framework for small projects. Software Process: Improvement and Practice, 6, 67–83.

Lewis, E.E. (1994) Introduction to Reliability Engineering. John Wiley & Sons, Inc., New York, NY.

Lykins, H. (1997) A framework for research into modeldriven system design. Proceedings of the Seventh Annual INCOSE Symposium, 765–772.

Lyu, M.R., ed. (1995) Software Reliability Engineering. IEEE Computer Society Press, New York, NY.

Malaiva. Y.K. & Srimani. P.K. (1990) Software Reliability Models: Theoretical Developments, Evaluation and Appli cations. IEEE Computer Society Press, New York, NY.

Mark, C.T. (2000) Machining systems: revolution, not evo lution. Manufacturing Engineering, February.

Marz, T.F. & Plakosh, D. (2001) Real-Time Systems: Engineering Lessons Learned from Independent Technica Assessments. Carnegie Mellon Software Engineering Institute, Pittsburg, PA.

McGinity, M. (1999) Staying connected: flying wireless, with a net: mobile internet providers prepare for takeoff. Communications of the ACM, 42, 19–20.

McGraw, K. & Harbinson, K. (1997) User-Centered Requirements. Lawrence Erlbaum Associates, Mathwah, NJ.

Pine, B.J.I.I., Victor, B. & Boynton, A.C. (1993) Making mass customization work. Harvard Business Review 71, 108–119.

Sage, A.P. (1992) Systems engineering and information technology: catalysts for total quality in industry and education. IEEE Transactions on Systems, Man, and Cybernetics, 22, 833–864.

Stallings, W. (1999) Cryptography and Network Security, Principles and Practice. Prentice Hall, Upper Saddle River, NJ.

Sun, J. & Martin, H. (1999) Building an integrated large scale step database for virtual enterprises. Proceedings of ASME Detc99/DFM, 1999 ASME Design Engineering Technical Conferences, Las Vegas, Nevada.

Tai, A.T., Meyer, J.F. & Avizienis, A. (1996) Software Performability: From Concepts to Applications. Kluwer Academic Publishers, New York, NY.

Van Vilet, J.W. & van Luttervelt, C.A. (1999) State-of-the art report on design for manufacturing. Proceedings O ASME Detc99/DFM, 1999 ASME Design Engineering Technical Conferences, Las Vegas, Nevada.

## Biographies

Dr Bahador Ghahramani is an Associate Professor in the Department of Information Systems and Quantitative Analysis at the University of Nebraska at Omaha (UNO). Prior to joining academiahe was a Distinguished Member of Technical Staff (DMTS) at AT&T-Bell Laboratories. His work experience includes positions in academia, industry and consulting. He has extensive R&D experience in Advanced Systems Design and Development, Telecommunication Systems, Advanced Managemen Information Systems, Advanced Business Applications Programming. Obiect Oriented Programming Environments, Expert Systems and Decision Support Systems, Database Management. Design of Human Machine Systems, Business Data Communications, Information Technology, Business Systems Analysis and Design, and Business Data Structure.

Dr Ghahramani has presented and published numerous papers and has been an active participant and officer in several national and international organizations and honour societies, He holds seven patents: 'Eve Depth Testing Apparatus’, ‘A Method for Measuring the Usability of a System’, ‘A Method for Measuring the Usability of a System and for Task Analysis and Re-engineering’, ‘Electronic Depth Perception Testing Systems Apparatus for Conducting Depth Perception Tests’, ‘Emergency Marking System, Marking Device, Components Therefore and Methods of Making the Same’, ‘Computer System for Performing Eye Depth Perception Test’, and ‘Multipurpose Hazard Field Marker and Components Therefore'. In addition, he has applied for and maintains copyrights on five AT&T global system designs.

Dr Ghahramani received a PhD in Industrial Engi neering from Louisiana Technological University with a minor in Information Systems; an MBA in Information Systems from Louisiana State University; an MS in Industrial Engineering from Texas Technological University; an MS in Applied Mathematics and Computer Sci ence from Southern University; and a BS in Industria Engineering and Management from Oklahoma State University. Dr Ghahramani is the recipient of the University of Nebraska at Omaha Alumni Excellence in Teach ing Award for the College of Information Science and Technology, General Motor’s Outstanding Teaching Award, and the University of Missouri at Rolla Outstand ing Teaching Award.
