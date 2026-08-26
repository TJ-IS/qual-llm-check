---
otero_id: 17960
otero_key: "S5QDB29X"
title: "Opportunity determination for office information systems"
authors: "Federico Barbic; Gianmario Motta"
year: "1989"
journal: "Information & Management"
doi: "10.1016/0378-7206(81)90068-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Opportunity Determination for Office Information Systems

Federico Barbic

Dipartimento di Elettronica, Politecnico di Milano, Milano, with a grant from Applied Research Group, Milano; currently: Booz, Allen & Hamilton Italia Ltd, Piazza Adigrat 4, 20133 Milano, Italy

Gianmario Motta

Telos Management, Via della Moscova 12, 20121 Milano, Italy

Identifying information technology opportunities is crucial for an effective information strategy. Office information systems, that integrate a variety of information handling methods, require a specific approach. However, current opportunity determination techniques mainly address the narrower spectrum of data processing applications. On the other hand, information requirements analysis techniques specifically aimed at the office environment do not significantly support opportunity determination. This paper proposes a method of determining organizational requirements of office information systems and integrating them into the information requirements. Organizations are considered as a network of interchange that associates agents, organizational products and information processes. Organizational requirements arise from an assessment of change in products and interaction. Information requirements are identified and prioritized according to their potential contribution to improve the value and cost of products and interaction.

Keywords: Office information systems, Office systems methodologies, Information systems planning, Systems analysis.

1. Opportunity Determination and Office Information Systems

We term office information systems (OIS) the information technology applications that support office activities. Given the variety of activities, they deal with both structured and non-structured information, such as transaction data, text, and image. OIS are regarded as a conceptual and technological extension of the traditional information systems (IS), such as airline reservation systems, which address interdepartmental flows of structured information and are based on shared databases. See Figure 1.

We term opportunity determination (OD) the process through which an organization identifies the potential applications of information technology. Because of its objective, OD precedes the design stage of IS and OIS, and defines the information strategy. This should be consistent with the company's business and organizational strategy. Therefore, OD should rank potential applications according to their contribution to the critical success factors of the business [28,29,30] especially when information technology is a competitive factor [2,26,27].

![](/api/attachments/S5QDB29X/fulltext/images/133ee46978470b3a870b422259adfa9bea4785f017941f9121f12f59909dca2a.jpg)

Federico Barbic is a Booz, Allen & Hamilton management consultant in the Information Technology area since 1987. Before joining BAH, he was at Politecnico di Milano and at IBM Almaden Research Center, San Jose, doing research in the office and database systems sectors.

Federico Barbic received a doctorate degree in Electronic Engineering in 1982 from Politecnico di Milano. Italy and is member of ACM and the IEEE Computer Society.

![](/api/attachments/S5QDB29X/fulltext/images/6a6f4b90371f29fe012ef4d9f6f60ad27295eaddd33043a49e20f720f086af45.jpg)

Gianmario Motta joined Telos in 1983 and is currently manager of the Management Information Systems Consulting Area. Also, he teaches information systems at the MIP, the master degree of Politecnico of Milano, Italy. Before joining Telos, he worked as manager and project leader with Systems & Management, an Italian independent software house. Gianmario Motta received a doctorate degree in Philosophy in 1972 by Università Statale di Milano, Italy and is member of the IFIP Working Group 8.2.

![](/api/attachments/S5QDB29X/fulltext/images/f7f05e87f5dfd038e15734af854e9c60d55696fc175499d85ec404337fe3cde2.jpg)  
Fig. 1. Spectrum of information processes in organizations.

Therefore an effective and complete OD approach should:

1. model the organization activities in terms useful to elicit information processing requirements;

2. consider the whole spectrum of information processing methods and technologies;

3. prioritize potential applications;

4. monitor the OD process.

## 2. Techniques for Opportunity Determination: A Review

Several techniques can be used for OD. On one hand is feasibility techniques sketch out an overall map of potential information systems (IS). On the other hand, some analysis techniques for IS and OIS provide a model that interrelates organizational activities and information processes; they support an OD process at a lower level. Finally, organizational analysis methodologies focus on the organizational functions or agents using information; they help to identify the opportunities for IS and OIS.

## 2.1. Information Systems Feasibility Techniques

These techniques identify and segment an organization's potential IS, and provide a direct or indirect approach to prioritize IS projects (i.e. opportunities). Mainly developed during the late Sixties, early Seventies and Eighties, they work at a very high level, where each elementary segment of an IS may correspond to hundreds of programs, and they are typically used in IS planning. An anthology sample of early IS feasibility techniques is provided by [11]; a framework of the is planning can be found in [3] and [35].

With the well-known Business Systems Planning, BSP, OD essentially consists of identifying the organization's business processes, data classes, and functions, and defining their mutual relationships [17]. Organization's functions are organization's units, such as departments, offices, and plants. Data classes are aggregates of information about a given entity, such as "Product Information" or "Supplier Information". Business processes are a set of activities that typically cross multiple department lines, such as "Materials Procurement" and "Manufacturing Planning". The relationships between functions, processes, and data are shown by matrixes. For example, the relationship of processes to data classes is shown by a matrix where one axis lists the data classes while the other indicates the processes. An appropriate notation shows whether a given data is input, output, or both to a given process. With this approach, overall information needs of a given process can easily be identified and verified. IS boundaries are eventually defined on the process data matrix by outlining the data classes that refer to a given set of processes. Finally, IS projects are prioritized by appropriately scoring their expected economic return, impact, and the current condition of existing IS. Hence, OD consistency depends on how accurately processes and data classes are identified.

Business Information Characterization Technique, BISC, has the same target as BSP, but the concept of “business process” is replaced by the concept of “order” [18]. “Order” is there used in a very broad sense – it is anything that requires a response. An order can take many forms, informal and formal, and it can concern things, spaces or skills. An organization is conceived as a system that responds to orders coming from the environment. The key of BISC is the method used to classify orders and to associate information needs, based on the Business Information Analysis and Integration Technique, BIAIT [6]. The analyst raises a predefined set of questions for each ordered entity and categorizes (within a predefined framework) the way customers order and organization responds. An appropriate set of “information handling disciplines”, that control the order-response process, is associated with each category. The relationships of ordered entities to information handling disciplines is shown in a matrix, that lists entities on one axis and disciplines on the other axis. Similar tables show the relationships occurring between disciplines, data, and organizational functions. The BISC final output is similar to BSP, but its approach appears more sophisticated and mechanistic.

Both BSP and BISC are conceptually complete OD techniques for IS but not for OIS. Unstructured information and intradepartmental flows, which are typical OIS elements, are disregarded, nor BSP or BISC can be extended accordingly.

## 2.2. Analysis Techniques

Information requirements collection and analysis techniques provide an OD technique, as much as they derive information requirements from a representation of the organization's activities. The graphical representation is their main difference from feasibility techniques, such as those based on matrices. A variety of such techniques has been developed in the last decade. A comprehensive review of IS techniques is provided by [5,7,10,22, 23], while proposals more specifically aimed at the office environment are discussed in [1,4].

## 2.2.1. IS Analysis Techniques

Information Systems and Analysis of Change, ISAC [19,20], covers the whole spectrum of IS projects from preliminary problem analysis to implementation. In ISAC, the organization's activities are represented by directed graphs that show both physical and information flows and allow a fairly consistent description of information requirements. ISAC devotes to OD a specific project phase, called Analysis of Change. First, the current situation is studied in order to find out problems and to relate them to a high-level activity graph of the organizational system under study. The representation can be as detailed as needed by an appropriate top-down decomposition. Project objectives are defined. A set of possible alternative solutions is identified, described, and tested against the previously identified problems and objectives. Thus, the feasibility of implied organizational change is assessed.

In the Structured Analysis and Design Technique, SADT [31], organizational activities are described by directed graphs, called Actigrams. Actigrams represent the sequence of activities in a given system and show data, mechanisms, and controls associated with each activity. The desired detail level is obtained by top-down decomposition. Though the representation of generic flows is very easy, information requirements development is less controlled than in ISAC.

ISAC, SADT, and allied techniques provide a well-founded graphical representation of organizational activities; they associate organizational activities and information processes. However, because of their procedural orientation, they disregard the organizational units. This is a crucial aspect of OIS. Organizations are systems of interconnected units, where each one can perform a variety of activities. An OIS should support the whole spectrum of activities of a unit, not only a segment. In the airline business, the agent's OIS should support not only reservations and ticketing, but also his internal administration and document processing.

## 2.2.2. OIS Analysis Techniques

Most OIS proposals provide a formal description of office elements and procedures, and some also guide the identification of bottlenecks and sub-optimal situations.

Office Talk-D [14] is an example of an experimental distributed OIS that integrates a desk-top emulator called Office Talk-ZERO [13] and a formalism for office procedure specification and simulation based on Information Control Nets. Office Talk-D has been implemented at XEROX PARC as an active system: operational control of office work is supported by the dynamic comparison of actual procedure status with the expected status indicated by the model. Quantitative simulations and estimates of the impacts of change in office procedures are enabled by an interactive editing and simulation facility, called Quinault [21]. Since Office Talk-D gives the major emphasis to the representation of an operational view of the office, the organizational dimension is not captured and no guidelines are provided to identify critical areas.

The problem of introducing information technology in the office environment was developed by the MIT Office Automation Group. Office Analysis Methodology, OAM [32], together with Office Specification Language, osL [16], provides a coherent framework for oIS development, covering the phases of analysis, design, and formal specification of operational office aspects, with the objective of improving the efficiency of business processes. OAM offers a set of guidelines on how to conduct the interviews of requirements collection, and OSL supports formal requirements specification. However, it is not clear the way the dimensions of organizational units, activities, and information are mutually related, nor the way an applications portfolio is segmented and prioritized.

The problem of assessing the feasibility of a specific OIS has since been addressed in MOBILE-Burotique [12], which presents a classification of the instruments for observation, collection, and analysis of information technology requirements in the office. A great emphasis is paid to the methodological steps of Intelligence (statement of objectives and limits of the study) and Diagnosis (collection of significant indicators to identify opportunities). Unfortunately, no formal model is defined and no criteria are offered to select the most appropriate analysis instruments in the different cases.

A final example of an on-going research project is TODOS (TOOLS for Design of Office systems) [24] which has the objective of developing an integrated environment to support OIS design within the EEC ESPRIT framework. The feasibility of the introduction of IT in the organization and a sort of OD are studied first. Functional and architectural requirements are then formally specified and interpreted to generate a rapid prototype of the future system, which is verified and checked by the users. In TODOS, OD plays an important role, because it identifies the areas in which further analysis is useful.

Generally, only the most recent OIS proposals assign a primary role to OD, but, even when OD is present, no models based on relevant theory appear.

## 2.3. Organization-oriented Techniques

Organizational analysis is a key for OD as much as it identifies the organizational strategy to be served by information technology applications. With the advent of office automation technology, a lot of organizational approaches to OD have been revived. They can be categorized in various classes [34], each one based on a different representation of the organizational system.

With organizational communication approaches, the organization is viewed as a communication system. The objective of office systems is to improve communications, resulting in time saving, increased cooperation, better access to information, more control. The analysis consists of defining the communication network within the organization.

Functional approaches stress the impact of information technology on the functions performed by offices. According to this view, communications oriented approaches confuse the means (i.e. communications) with the ends (i.e. functions). Thus, the analysis is aimed at the procedural aspects.

In information resource management approaches, information is viewed (like money, people and facilities) as a resource that can be better managed through information technology. The analysis consists of quantifying the value of the information.

With decision support systems approaches, the design and measurement of office systems entail supporting the judgement of managers and other decision-makers. The analysis consists of studying the effects of systems on the performance of complex, unstructured, or semistructured activities.

Finally, in quality of life approaches, the analysis considers the potential impact of systems on the nature of work, the worker's motivation, and the design of jobs and organizations. The related intervention strategy is called “sociotechnical”, and it can be used in OD, as well in the design and implementation of any work system.

Zero Base Budgeting, ZBB, an efficiency-driven functional approach, is aimed at the realm of support staffs, which are typically large customers of information. Each individual office is considered a unit that associates labour and other resources to a given set of activities $[9,25]$ . The analyst identifies costs and benefits of each meaningful package of activities and gives each package a service level, say from zero to four. The purpose is to eliminate undesirable activities and associated costs through a value analysis of service levels. Since information technology can improve both quality and efficiency of office activities, ZBB can offer a starting point to prioritize computer projects.

## 3. Opportunity Determination for Office Information Systems

## 3.1. Objectives

IS feasibility, OIS and IS analysis technique either fail to capture the whole spectrum of information processes, or do not associate the three dimensions of organizational units, organizational activities, and information processes, or, finally, do not focus the link between technology innovation and organizational change. On the other hand, organizationoriented techniques provide models and methods to understand the need and impact of change but they should be integrated with an analysis of information technology applications.

In our opinion, a first point of an effective OD approach is a general view of the role of the information technology. As recent theory has stressed, organizations are interaction systems. Organizational units interact with other units, both inside and outside the organization's boundaries. A crucial mission of the information technology should be to reduce the costs and improve the quality of interaction [8,33]. In broad terms, our objective is an approach that:

\- associates the three dimensions of organizational units, organizational activities and information processes;

\- considers all types of information requirements, whether they imply structured or non-structured information;

\- interrelates the three dimensions of OD: the agents who operate in the organization, the activities that the organization performs, and the information processes and technologies used;

\- allows to select and prioritize the information processes that support areas critical for organizational performance;

• significantly supports the analysis of change;

\- fosters a participative approach, since experienced users are the primary source of organizational know-how and success.

## 3.2. The Conceptual Model

The organization is considered to be a network of interacting agents. The interaction consists of the products that agents make and interchange. A product can be a material or transitory output. To each product are associated a set of information handling processes.

## 3.2.1. The Interaction Network

An interaction network is defined as the set of relationships that associate a given domain of products to a given domain of agents and external counterparts. External counterparts are the external entities the organization interacts with, such as customers, suppliers, banks and government.

An interaction network can be specified at different levels of detail. At the highest level, one will consider only one agent, the whole organization, and aggregations of external counterparts (i.e. the set of customers); the products will be equally aggregated into broad families. At a lower level, one will detail agents by breaking the whole organization into organizational units, such as offices or departments, and decompose product aggregations into individual products. At the lowest level, one will focus on the interaction among individuals (agents) within a single office. In our model, we address two levels of detail. The first one, called general interaction network, considers the interaction among organizational atomic units, and the second one, called detailed interaction network, analyzes the interactions among the agents inside a given atomic organizational unit.

Both general and detailed interaction networks play a role in determining opportunities. The detailed network indicates the way products are made, thus providing the necessary information to assess alternative approaches to product fabrication. The general network, by mapping the overall net of interchange, makes it possible to outline the priority areas. Identified through some external technique, such as critical success factors, priority areas can deal with a subset of relations among organizational units and their external counterparts, a subset of products, or a meaningful intersection of both. Furthermore, one can assess the perceived value of products received by destinees, and eventually eliminate, add to or modify them.

3.2.1.1. General Interaction Network An example of a general interaction network is represented by the double entry table of Fig. 2, where one axis lists products and the other axis indicates organizational agents and external counterparts. The example is at a first level of decomposition. Products are summarized by very broad product classes, such as “receivables” and “manufactured products”.

![](/api/attachments/S5QDB29X/fulltext/images/8a2beecd71362b5daaa3c86b8bf5f851b2bf447e22cae0f7602533d4f9de5e93.jpg)

Fig. 2. An example of a general interaction grid.  
![](/api/attachments/S5QDB29X/fulltext/images/c654886733d5f838475e5e96dd30b3e759116b92f63f1271d99bf53268cbcce5.jpg)  
Fig. 3. An example of a detailed interaction grid of the general accounting office (inside the accounting department).

![](/api/attachments/S5QDB29X/fulltext/images/e12d6053f1c97cdbb0bc07e744b775508de1ee2a56b7374688132a8f46da8cea.jpg)  
Fig. 4. An example of a detailed labour allocation grid of the accounting office.

The grid shows the interchange of products among organizational agents and their external counterparts. Appropriate labels indicate the relationships. A “D” indicates that a given agent or external counterpart receives a given product, thus identifying a recipient relationship. In turn, an “M” indicates that a given agent or external counterpart generates a given product, thus identifying a producer. Also, each product has one or more contributors, that are agents and external counterparts providing the raw material to make the product. The corresponding relationship is indicated by a “C”. Finally, each product can have one or more requester, that is the agent or external counterpart that needs the product. This is indicated by an “R”.

The general network includes both physical and non-physical products. The products originating from a plant consist of physical objects (e.g. pumps) while the products from the president are non-physical (e.g. written or verbal commands). Since our target is offices, we will concentrate on non-physical products originating from or destined to offices.

The lowest level of decomposition of an interaction network will consider atomic products and atomic organizational units. An atomic unit is one that can be decomposed only into specific individuals. Generally, it consists of a group of people coordinated by a head, such as a foreman or supervisor.

3.2.1.2. Detailed Interaction Network The detailed interaction network specifies the interactions inside a given atomic organizational unit. Here, agents are individuals or aggregations of individuals, such as “buyer” and “secretary”. In this case, the interaction is illustrated by a double entry grid, which associates the agents to the products of the considered atomic units.

Fig. 3 shows the detailed interaction network for an accounting office, and, by means of a linear responsibility chart, it specifies the contribution of agents to products (execution, support, coordination, and being informed). By reading the grid vertically, one sees the role of a given agent on the unit products. Conversely, the horizontal perspective shows the involvement of agents in a given product.

In turn, Fig. 4 shows the labour effort of each agent for each product. The labour effort is an essential input to weigh the cost of office products, as far as they are labour intensive.

## 3.2.2. Office Products

An office product is an entity that:

\- is an output of an activity made in an office, or
- has at least one recipient external to the producing office.

3.2.2.1. Description of Office Products Office products are described by a limited set of attributes on their format, time frequency, and standardization. Office products are of different format: document, communication, action, or physical object. An accounting statement or a memo are typical examples of a document. On the other hand, assistance and coordination are forms of communication, since they involve interaction among people. A product can consist also of service actions, as in car repairing. Finally, a product can be a physical object, such a finished good of a plant, but it is seldom found in offices.

Time frequency specifies the time frame. Products can be released on request or periodically. Realtime order processing, where products are made every time a product (service) request enters, is an example of the first. Periodical reports, plans, and budgets are examples of the latter. Here, products are triggered by the calendar. Sometimes, the same product can be produced both on-request and periodically.

Of course, a product can be more or less standard. Invoices are so similar that you can hardly distinguish among different ones. Communications are so different that one wonders whether they can be classified at all. The degree of standardization indicates to what extent the format of an instance of a given product remains unchanged in respect to the previous ones. The greater the standardization, the easier its automation.

By associating frequency and labour, one can compute the unit cost of each product instance, and evaluate (labour) efficiency. Typically, unit costs are calculated by dividing the yearly workdays applied to a given product (such as receivables entries) by the yearly volume (say, number of receivables entries).

## 3.2.2.2. Functional Classification of Office Products

In real world, office products number in the hundreds. Thus, a top-down definition, that allows different detail levels of products, is needed. Furthermore, defining a product involves some degree of personal judgement. The products of the accounting office “Annual Profit & Loss” and “Monthly Profit & Loss” may be grouped in one larger product or split into smaller products, depending on the level of detail needed. Therefore, some kind of general classification is necessary. We here propose a classification based on the concept of organizational function (OF).

In broad terms, an OF indicates a family of jobs. Depending on the level of detail, an OF can embrace a variable range of jobs. Let us consider an automotive corporation. There will be general OFs, such as Engineering, Manufacturing, Sales and Administrative staffs. These OFs can be split into smaller segments. Sales will be broken down into Sales Planning, Marketing, Order Processing, and Sales Line. Such segments can be further subdivided until the desired level of detail has been attained. From this process, one obtains a tree-like classification of OFs, the root being the organization itself and the leaves the individual jobs.

By using the OF classification, products can be grouped into classes homogenous in content, specialization, and, quite often, in mix of information processing. So, the classification will make it possible to segment the interaction network according to the OFs. We assume that each product belongs to one and only one OF.

## 3.2.3. Products and Information Processes

To each office product multiple information processes can be associated. It is evident that a classification is a key to opportunity determination. We think an appropriate taxonomy should take into account nature, time and space characteristics.

From the nature viewpoint, information processes can be categorized into four classes, depending on the flow they support (local or interdepartmental) and their information object (structured or nonstructured information). Corporate information systems, such as management control reporting and customer orders processing systems, are typical examples of interdepartmental and structured information processes, while the use of personal computer on our desk is a case of local, non-structured information process.

From the time viewpoint, we distinguish between interactive processing, that occurs as products are being made, and periodical batch processing, that is triggered by a calendar deadline and often occurs off-line.

From the space viewpoint, information processes can address local data, like the drafts on our desktop, or remote data, like the organization's databases or public data banks.

The core of opportunity determination is defining the information processes that are associated to each product, in either the current or future situation. Information grids show the association between products and information processes. Appropriate signs indicate whether a certain information processing application exists or is recommended for a given product.

## 3.3. Steps of the OD process

Fig. 5 associates the major steps of the proposed OD approach to the major actors - user management, office supervisors, external counterparts, study team, information analysts, and information systems department. The whole process is conceived as a participative, structured organizational development process, that starts with the definition of the scope, duration, and cost of the OD study, and ends with an action plan. Fig. 6 shows the major outputs and techniques associated with each step. General and detailed interaction grids are first designed in steps 4 and 5, where they describe the current organization's condition, and, again, in step 7, where they are used to represent alternative organizational scenarios.

## 3.3.1. Problems Gathering

The first step involves consideration of current problems. Problems are the issues that management perceive as facing the organization, as for example “high cost of administrative transactions” or “poor response to customer’s requests”. Taking stock of problems helps to focus on the appropriate organizational units and products and in identifying the stakeholders.

<table><tr><td></td><td>USER MGMT</td><td>OFFICE SUP.</td><td>EXTERNAL COUNT.</td><td>IS DPT</td><td>STUDY TEAM</td></tr><tr><td>1. PROBLEMS GATHERING</td><td>P</td><td>[P]</td><td>-</td><td>[P]</td><td>E</td></tr><tr><td>2. GENERAL INTERACTION DEFINITION</td><td>[P]</td><td>P</td><td>P</td><td>-</td><td>E</td></tr><tr><td>3. DETAILED INTERACTION DEFINITION</td><td>I</td><td>P</td><td>-</td><td>-</td><td>E</td></tr><tr><td>4. PRODUCT EVALUATION</td><td>[P]</td><td>P</td><td>P</td><td>-</td><td>E</td></tr><tr><td>5. PRODUCT CHANGES</td><td>D</td><td>P</td><td>[P]</td><td>P</td><td>E</td></tr><tr><td>6. ORGANIZATIONAL CHANGES</td><td>I</td><td>P</td><td>-</td><td>[P]</td><td>E</td></tr><tr><td>7. ACTION PLANNING</td><td>D</td><td>P</td><td>[P]</td><td>P</td><td>E</td></tr><tr><td rowspan="5">LEGENDA</td><td>D</td><td colspan="4">= decides</td></tr><tr><td>E</td><td colspan="4">= executes, does the job</td></tr><tr><td>P</td><td colspan="4">= partecipates</td></tr><tr><td>I</td><td colspan="4">= is informed</td></tr><tr><td>[ ]APPROACH</td><td colspan="4">= by exception, as neededOUTPUT</td></tr><tr><td>1. PROBLEMS GATHERING</td><td>Interview management</td><td colspan="4">Preliminary hot list</td></tr><tr><td>2. GENERAL INTERACTION DEFINITION</td><td>Structured interviews</td><td colspan="4">General interaction gridsInformation grids</td></tr><tr><td>3. DETAILED INTERACTION DEFINITION</td><td>Structured interviews</td><td colspan="4">Detailed interaction grids</td></tr><tr><td>4. PRODUCT EVALUATION</td><td>Interviews of recipients</td><td colspan="4">Product scoring</td></tr><tr><td>5. PRODUCT CHANGES</td><td>Various, contingent</td><td colspan="4">Interaction segmentationInfo. technology applicationsProduct priority list</td></tr><tr><td>6. ORGANIZATIONAL CHANGES</td><td>Panels, interviews</td><td colspan="4">General interaction changesDetailed interaction changesInteraction changes feasibility</td></tr><tr><td>7. ACTION PLANNING</td><td>Project segmentation</td><td colspan="4">Project plan</td></tr></table>

Fig. 5. Roles and steps of the proposed approach for OD.

Fig. 6. Steps, inputs, and outputs of the proposed approach for OD.

The study team will develop:

(a) a statement of problems

(b) a problem grid, which associates problems with the concerned organizational units and external counterparts

(c) a preliminary general interaction grid

(d) the objectives of the OD study:

\- interaction areas to be addressed (i.e. priority product families)

\- expected result areas (cost reduction and/or product improvement).

## 3.3.2. General Interaction Definition

The general interaction is defined in a top-down process. The study team and the office supervisors examine the products of each office. Office products are identified and their characteristics described. During the interviews, the current information processes are specified, and, based on supervisor's experience and analyst's knowledge off available technology, potential changes are proposed. At the end, a general interaction and a general information grid are obtained and an appropriate functional classification of products is prepared.

## 3.3.3. Detailed Interaction Definition

Sometimes, it is necessary to further detail the interaction. In such cases, the internal work organization is represented by a detailed interaction grid, that associates individual agents and individual products. Related information is collected when interviewing the office supervisor.

## 3.3.4. Product Evaluation

The value of products is estimated by their recipients. Their evaluation is crucial when products are discretionary (e.g. internal consulting) or destined to the public.

Recipients are asked to score the quality of the products against the expected (or desired) quality. Quality attributes include timeliness, completeness, correctness, usability and overall adequacy. Recipients are also requested to list products they do not receive but consider necessary to improve the quality or cost of their output. The final outcome is a statement of quality evaluation.

Typically, this shows to what extent unnecessary products are being produced and necessary products are not, and what amount of resources results misdirected.

## 3.3.5. Analysis of Change of Products

The input of the analysis of change is a list of products, that shows:

\- products to be eliminated because they are deemed unnecessary

\- products to be modified

\- products to be introduced ex novo.

The list is backed by an estimate of the implied change of:

\- labour cost

• information technology

\- organizational design (procedures, policies, and structure).

Products are sorted according to their priorities. A first criterion is the priority that management has given. A second one is the contribution that each set of product changes can give to attaining the critical success factors of the whole company and of the functional areas.

The study team presents this analysis to the sponsor management. Priorities and product changes are refined and an operative work hypothesis is worked out.

## 3.3.6. Analysis of Organizational Change

The expected portfolio of products implies a variety of changes. The objective is to identify which changes are necessary in the interaction network and other relevant organizational aspects.

As a first task, the project team generates some alternative general interactions, that result from product changes. The software tool supports this step by duplication of the current interaction network and by specification of required change; computer reports display the changes in labour effort and information technology support. Forecasted changes are eventually assessed by interviewing the prospective recipients of the new or modified products.

As a second task, the project team assesses the impact of change of the products and the general interaction within the detailed interaction of the affected atomic organizational units, thus determining the effects on jobs, skills, and work organization.

## 3.3.7. Action Planning

Once the hypothesis of change has been worked out and approved by management, project will be planned. The plan will integrate both information technology and organizational projects.

## 3.4. The software Tool

Our OD method is supported by a prototype software tool, that stores and manipulates data on general and detailed interaction networks, products, and information grids [15].

## 3.4.1. The Data Model

The data model reflects the conceptual model and is described by an Entity/Relationship formalism. All entity types contain a “scenario” key and, therefore, different scenarios can co-exist and be compared. See Fig. 7.

The general interaction network is represented by the entity types Organization, Atomic-organizationunit (i.e. office), External-Counterparts, and Products. The relationship between entity types deserve some discussion. Atomic organizational units are related to Organization through the Part-of relationship. Atomic organizational units may play an active role on Products (e.g. to make, contribute to, or receive a product) or a passive role (e.g. to receive a product). These aspects are captured by the Impacts/is-affected-by relationship. The same relationship applies also to External Counterparts, that may supply Products (e.g. vendors) or receive them (e.g. clients).

The detailed interaction network is described by the Agent entity type and Works-for and Has-role relationships. The Agent entity type may represent either individuals or groups of persons. The Hasrole relationship specifies the involvement of a given agent in the life cycle product (e.g. coordinates or executes), while Work-for indicates the correspondence of each agent with a particular atomic organizational unit.

The information grid is described by the information-process entity type and the Requires relationship. The information-process entity describes the general attributes of the information processes, and it plays the role of a glossary, which can be tailored to the specific organization. The Requires relationship specifies whether a given information process should be used to make a given product. An attribute of the Requires relationship specifies whether the information process is actually supported by a computer application.

![](/api/attachments/S5QDB29X/fulltext/images/f94d5052e1b57ecf35c4575bd38559e96a1bc69f65186c5ebc675c34d79b0c23.jpg)  
Fig. 7. Entity relationship diagram of an interaction grid.

Finally, the tree of organizational functions is represented by the Function entity type. The structure of organizational function is represented as a complex attribute of the Function entity type. Function and Product entity types are associated by the Belongs relationship: i.e. each product belongs to one and only one Function.

## 3.4.2. The Processing Functions

Data specification, data manipulation, and reporting are performed through a hierarchical menu interface. The software supports a series of integrity checks to maintain the correctness of the database. For instance, it is necessary to declare an atomic organizational unit before associating a given product to it. On the other hand, a flexible analysis process is allowed. For example, it is not necessary to specify the detailed interaction grid of all the products, but only of those that the analyst chooses.

The results of the analysis are summarized in a set of reports that show the interrelations among agents, products, and information processes. Based on a selection of specific intersection of functions (products) and atomic organizational units, it is possible to produce:

\- general interaction grids

• detailed interaction grids

• information grids (actual and expected).

Other reports will compare scenarios (current versus alternative A, alternative A versus alternative B, etc.) by highlighting variations, such as additional or more intensive information processes, reduced labour effort, and different number of interactions for a given organizational function. These comparison reports are intended to assist the change analysis, by providing a what-if support to managers and users.

## 4. Conclusion

A method to determina opportunities for office information systems has been presented. The method links organization strategy and information technology. The analysis concentrates on the interaction among organizational units and between organizational units and external counterparts. Mutual exchange of goods, communications and services is assumed as the very core of the organization. The mission of information technology consists in improving the intrinsic quality of products to be exchanged, the quality of exchange or, alternatively, in decreasing the costs of production and exchange. The method integrates concepts of information analysis and organizational analysis.

Both method and model are kept reasonably easy for practical use. Two major extensions are envisioned, one concerns the integration between opportunity determination and system design, and the other deals with the enhancement of the support tool.

Opportunity determination (OD) is the very first step of a project life cycle. The challenge is to connect the OD method to subsequent phases of logical and conceptual design of office information system. This entails a conceptual interface from OD to design techniques and a software interface as well from the the OD database to the design database. These are future steps in our research.

## Acknowledgements

The authors would like to thank Alberto Fabbri for the implementation effort provided and for useful discussions to clarify some aspects of the method.

## References

[1] F. Barbic, S. Ceri, P. Mostacci, G. Bracchi, Modeling and integrating procedures in office information systems design. Information Systems, vol. 10, n. 2, 1985, 149–168.

[2] R.I. Benjamin, J.F. Rockart, M.S. Scott Morton, J. Wyman, Information technology: a strategic opportunity, CISR working paper # 108, Massachusetts Institute of Technology, Cambridge, MA, 1983.

[3] B. Bowmann, G.B. Davis, J.C. Wetherbe, Modeling for MIS, Datamation, July 1981.

[4] G. Bracchi, B. Pernici, The design requirements of office systems, ACM Transactions on Office Information Systems, vol. 2, N. 2, April 1984, pp. 151–170.

[5] I. Brandt, A comparative study of information systems design methodologies, in: T.W. Olle, H.G. Sol, C.J. Tully (editors), Information systems design methodologies: a feature analysis, North-Holland, Amsterdam, 1983.

[6] W.M. Carlson, Business information analysis and integration technique, Data Base, Vol. 10, N. 4, Spring 1979.

[7] S. Ceri, Requirements collection and analysis for information systems design, in: H.J. Kugler (editor) 10th IFIP world computer congress, Dublin, September 1986.

[8] C. Ciborra, Reframing the role of computers in organizations: the transactions cost approach, Sixth international conference on information systems. Indianapolis, December 16–18, 1985.

[9] L.M. Cheek, Zero-base budgeting comes of age, AMACOM, New York 1977.

[10] M.A. Colter, A comparative analysis of systems analysis techniques, MIS Quarterly, Vol. 8, N. 1, March, 1984.

[11] J.D. Couger, M.A. Colter, R.W. Knapp, Advanced system development / feasibility techniques, John Wiley & Sons, New York, NY, 1982.

[12] P. Dumas, G. du Roure, C. Zanetti, D. Conrath, J. Mairet, MOBILE-Burotique: Prospects for the future, Office Information Systems, Naffah, N. (ed.) North-Holland, Amsterdam, 1982, pp. 471–480.

[13] C. Ellis, G. Nutt, Office information systems and computer science, ACM Comput. Surv., 12, 1, March 1980, pp. 27–60.

[14] C. Ellis, M. Bernal, OFFICETALK-D: An experimental office information system, Proc. ACM SIGO A Conference on Office Systems, Philadelphia, June 1982, pp. 131–140.

[15] A. Fabbri, Un metodo di analisi delle opportunità per i sistemi informativi di ufficio assistito da elaboratore, Dipartimento di Elettronica, Politecnico di Milano, Milano 1987.

[16] M. Hammer, W. Howe, V. Kruskal, I. Wladawsky, A very high level programming language for data processing applications, Communications of the ACM, vol. 20, n. 11, Nov. 1977, pp. 832–840.

[17] Business Systems Planning, IBM, GE 20-0257-1, 1975; see also Business systems planning: planning for distributed information systems, IBM, GE 20-0655-1.

[18] D.V. Kerner, Business information characterization study, Data Base, Vol. 10, N. 4, Spring, 1979.

[19] M. Lundberg, G. Goldkuhl, A. Nilsson, Information systems development: a systematic approach, Prentice Hall, Englewood Cliffs, New Jersey, 1981.

[20] M. Lundberg, The ISAC approach to specification of information systems and its application to the organization of the IFIP conference, in: T.W. Olle, H.G. Sol, A.A. Verrijn-Stuart (editors), Information systems design methodologies: a comparative review, North-Holland, Amsterdam, 1982.

[21] G. Nutt, P.A. Ricci, Quinault: an office modeling system, IEEE Computer Transactions, vol. 14, n. 5, pp. 41–57, 1981.

[22] T.W. Olle, H.G. Sol, A.A. Verrijn-Stuart (editors), Information systems design methodologies: a comparative review, North-Holland, Amsterdam, 1982.

[23] T.W. Olle, H.G. Sol, C.J. Tully (editors), Information systems design methodologies: a feature analysis, North-Holland, Amsterdam, 1983.

[24] B. Pernici, W. Vogel, An integrated approach to OIS development in ESPRIT '86: Results and Achievements, North-Holland, Amsterdam, 1987, pp. 835–844.

[25] P.A. Phyrr, Zero base budgeting, Harvard Business Review, vol. 48, n. 6, 1970.

[26] M.E. Porter, V.E. Millar, How information gives you competitive advantage. Harvard Business Review, vol. 63, n. 4, pp. 149–161, 1985.

[27] M.E. Porter, Competitive advantage, Free Press, New York, NY, 1985.

[28] N. Rackoff, C. Wiseman, W.A. Ullrich, Information systems for competitive advantage: implementation of a planning process, MIS Quarterly, November–December 1985.

[29] J. Rockart, Chief executive define their own data needs, Harvard Business Review, Vol. 57, N. 2, March–April, 1979.

[30] J. Rockart, C. Bullen, A primer on critical success factors, Center for Information Systems Research, CISR Working Paper # 69, Massachusetts Institute of Technology, Cambridge, Ma, 1981.

[31] D.T. Ross, Structured analysis (SA): a language for communicating ideas, IEEE Transactions on Software Engineering, Vol. SE-3, January, pp. 16–34, 1977.

[32] M. Sirbu, S. Schoichet, J. Kunin, M. Hammer, and J. Sutherland, "OAM: An Office Analysis Methodology", Behaviour and Information Technology, Vol. 3, N. 1, January, pp. 25–39, 1984.

[33] P.A. Strassmann, Information payoff: the transformation of work in electronic age, Free Press, New York, 1985.

[34] D. Tapscott, Office automation: a user-driven method, Plenum Press, New York, 1982.

[35] J.C. Wetherbe, “Strategic planning for MIS”, in: Systems analysis and design, 2nd edition, West Publishing Co., 1984.
