---
otero_id: 202
otero_key: "VQ3M5SSH"
title: "An incident information management framework based on data integration, data mining, and multi-criteria decision making"
authors: "Yi Peng; Yong Zhang; Yu Tang; Shiming Li"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.11.025"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# An incident information management framework based on data integration, data mining, and multi-criteria decision making

Yi Peng <sup>a,</sup>⁎, Yong Zhang <sup>a</sup>, Yu Tang <sup>b</sup>, Shiming Li <sup>a</sup>

<sup>a</sup> School of Management and Economics, University of Electronic Science and Technology of China, Chengdu, PR China, 610054

<sup>b</sup> School of Computer Science and Engineering, University of Electronic Science and Technology of China, Chengdu, PR China, 610054

## a r t i c l e i n f o

Available online 25 November 2010

Keywords: Incident information management Data integration Data mining Multiple criteria decision making Decision support system

## a b s t r a c t

An effective incident information management system needs to deal with several challenges. It must support heterogeneous distributed incident data, allow decision makers (DMs) to detect anomalies and extract useful knowledge, assist DMs in evaluating the risks and selecting an appropriate alternative during an incident, and provide differentiated services to satisfy the requirements of different incident management phases. To address these challenges, this paper proposes an incident information management framework that consists of three major components. The <sup>fi</sup>rst component is a high-level data integration module in which heterogeneous data sources are integrated and presented in a uniform format. The second component is a data mining module that uses data mining methods to identify useful patterns and presents a process to provide differentiated services for pre-incident and post-incident information management. The third component is a multi-criteria decision-making (MCDM) module that utilizes MCDM methods to assess the current situation, <sup>fi</sup>nd the satisfactory solutions, and take appropriate responses in a timely manner. To validate the proposed framework, this paper conducts a case study on agrometeorological disasters that occurred in China between 1997 and 2001. The case study demonstrates that the combination of data mining and MCDM methods can provide objective and comprehensive assessments of incident risks.

© 2010 Elsevier B.V. All rights reserved

## 1. Introduction

Various types of incidents, such as the September 11 attacks, the SARS epidemic, and the 2008 Sichuan earthquake, cause huge loss of human lives and properties and highlight the need to improve our capabilities to prevent, protect against, respond to, mitigate, and recover from natural and manmade incidents [11].

Incident management activities can be divided into pre-incident and post-incident phases, which require different handling approaches since they associate with different levels of pressure, complexity, uncertainty, and response time. Pre-incident phases emphasize complete and comprehensive data analysis and decision support functions, while post-incident phases require fast and often real-time responses. Fig. 1 shows the main phases of incident management. Successful incident information management depends on a continuous, consistent, and systematic process that uni<sup>fi</sup>es preincident and post-incident phases.

Emergency situations often involve data collected by multiple organizations, saved in different formats, and resided in distributed sites. In order to be effective, an incident information management system needs to deal with several challenges. First, it must present the heterogeneous distributed incident data in a standardized format for accurate and timely data access, analysis, evaluation, and dissemination. Second, the system should help DMs explore large and complex data ef<sup>fi</sup>ciently, detect anomalies, and extract commonalities and correlations (OASIS [50]). Third, the system needs to assist DMs in evaluating the risks and selecting an appropriate solution during an incident. Fourth, the system should provide differentiated services to satisfy the requirements of different incident management phases and different types of incidents. For example, the urgency of a drought event is lower than an explosive blast threat to a school building.

Although there is much literature in the area of incident information management systems, the speci<sup>fi</sup>c challenges discussed above have not been thoroughly examined. The goal of this paper is to develop an incident information management framework that concentrates on these requirements. This conceptual framework consists of three major components: data integration, data mining, and multi-criteria decision making (MCDM). The data integration component is a set of approaches designed to act as a middleware between the underneath heterogeneous data sources and the upper intelligent analysis modules. It provides a high-importable, structuralized, and uni<sup>fi</sup>ed data interface to upper applications. The data mining component uses data mining methods to identify useful patterns and presents a process to provide differentiated services for pre-incident and post-incident information management. The MCDM component describes how MCDM methods can be applied in incident management to assess incident risks, evaluate feasible alternative solutions, and dispatch emergency resources.

![](/api/attachments/VQ3M5SSH/fulltext/images/11cca6e3ccb4e0e27f8babf1538976abd6a6879d40bd90245cf0eac5b6fb51da.jpg)  
Fig. 1. Incident management phases (Stoimenov et al. [65]). Adapted from L. Stoimenov, B. Predić, V. Mihajlović, M. Stanković: GIS Interoperability Platform for Emergency Management in Local Community Environment, Proceedings o 8th AGILE Conference on GIScience (2005), Estoril, Portugal.

To validate the proposed framework, this paper conducts a case study on agrometeorological disasters that occurred in China from 1997 through 2001. The case study demonstrates that the integration of data mining and MCDM methods can offer particular advantages for incident management. The contributions of this paper are threefold. It brings together the existing literature on incident information management and identi<sup>fi</sup>es several important requirements for incident information management systems that have not been fully investigated. The second contribution is the development of a conceptual incident information management framework that combines data integration, data mining, and MCDM methods based on those requirements. The third contribution is the use of data mining and MCDM techniques to assess the risks of natural incidents using real-life agrometeorological disaster data.

The rest of this paper is organized as follows: Section 2 reviews related works. Section 3 presents the incident information management framework, including the data integration module, the data mining module, and the MCDM module. Section 4 describes a case study that validates the incident information management framework. The last section concludes the paper.

## 2. Related works

The existing research of incident information integration, knowledge discovery and data mining, and decision support may be summarized into three areas. First is incident information system design and development. Second is the data integration technology for incident management. Third are decision support functions for incident information management, including data warehousing, data mining, and multiple criteria decision making.

## 2.1. Incident information systems

Research on incident information system focuses on system design requirements and approaches, system framework and development, and system evaluation.

Turoff et al. [66] present some functionality requirements for the design of emergency response management information systems and a conceptual design framework. Jain and McLean [32] propose a framework to facilitate application of modeling and simulation to incident management on three axes—incident, domain, and lifecycle phase. Klashner and Sabet [37] present a decision support system (DSS) design model for mission critical situations and suggest that broader and more integrated use of various theories and approaches is necessary to design DSS for complex domains. Chen et al. [14] provide a set of design principles for the development of incident information management systems that are grounded in emergency management concepts and in the insights from the <sup>fi</sup>rst responders.

Besides incident information management system design and development, other issues have also been studied in incident information management systems. Fruhling and De Vreede [21] implement the eXtreme Programming (XP) software development method in a Webbased, distributed emergency response system. Kim et al. [36] develop and validate an instrument to measure the effectiveness of emergency response management systems. The instrument can be used to assess strengths and weaknesses of existing incident management systems. Mendonça [47] investigates the roles of cognition and improvisation in extreme event decision making and generates design requirements for extreme event decision support systems.

## 2.2. Data integration technologies

The area of data integration or information integration has made great progress in the theoretical foundations and in the development of algorithms and tools [26]. However, there is limited literature that deals with data integration in the context of incident or emergency management. Llinas [43] describes the strategic approach to address information fusion issue for both natural and manmade disasters. The focuses of their approach include domain analysis, developing representative data sets, an effectiveness-oriented approach to the evaluation of the derived information fusion technology, and a strategy for assessing information fusion technique robustness. d'Agostino et al. [15] present their ongoing project of designing software tools for situation assessment and high-level information fusion after large-scale disasters. In particular, they deploy a rescue simulator to provide an environment for modeling, communication, and information integration schemes. Scott and Rogova [62] report their research in exploring data integration system design and performance for natural and manmade disasters in a synthetic task environment. Their system incorporates higher level and distributed fusion capabilities and surveillance for secondary incidents.

## 2.3. Decision support functions for incident management

A number of research works have been developed to support DMs in selecting appropriate solutions and identify abnormal situations using MCDM and data mining methods during emergencies.

Harms et al. [29] used frequent pattern and association rule mining to assess the local and global climatic conditions and identify drought risks. Papamichail and French [53] develop an intelligent DSS to support decision making in nuclear emergencies. The system can generate alternatives and assist DMs in understanding decision problems and selecting a sound alternative. They also devise a strategy to evaluate the system from three levels: technical, performance, and subjective. French and Niculae [20] point out some pitfalls of data mining methods, especially predicting models, and the way these models are used in emergency management. They suggest that a more socio-technical approach is needed to develop crisis response system and model predictions should be drawn into emergency management in a balanced way. Karasova et al. [34] applied spatial association rule mining techniques to determine existing spatial relationships between the location of incidents and speci<sup>fi</sup>c geographical objects within a certain area. Berndt et al. [7] explore the role of data warehousing in bioterrorism surveillance. They show that data warehousing and online analytic processing (OLAP) techniques can provide rapid exploration of unusual situations and guidance for follow-up investigations using Florida wild<sup>fi</sup>res data from 1996 through 2001. Asghar et al. [2] provide the <sup>fl</sup>exibility to organize and adapt a tailored DSS model according to the dynamic needs of a disaster and identify subroutines from existing DSS models developed for disaster management on the basis of needs categorization.

## 3. The incident information management framework

## 3.1. The data integration module

Decision making in emergencies is a time-critical and challenging task that requires immediate and effective response from decision makers (DMs) under pressures and uncertainties [71]. Data integration is a key technology for ef<sup>fi</sup>cient incident information collection, sharing, dissemination, exploitation, and analysis, which are crucial to assist DMs in making timely and right decisions during emergencies. However, the vast amount and high complexity of incident information make data integration a dif<sup>fi</sup>cult task [45].

The heterogeneities of incident information can be divided into several aspects: system, architecture, platform, data type, timing, and language. Speci<sup>fi</sup>cally, it includes system heterogeneity such as mainframe, minicomputer, workstation, PC, and embedded system; architectural heterogeneity such as 32-bit and 64-bit architecture; platform heterogeneity such as Intel/Window, Sparc/Solaris, and Intel/Linux; data type heterogeneity such as multimedia data, spatial data, text, and optical/magnetic/infrared/thermal signals; timing heterogeneity such as continuous data, busty data, real-time data, and non-real-time data; language variety such as English, Chinese, French, German, and Dutch.

The heterogeneity and variety of incident data sources present a challenge to the construction of higher level modules, such as the intelligent analysis and decision support modules, in the incident information management system. The incident data are demanded to be delivered in a standardized formation for rapid processing and fast intelligent support. In order to meet the requirements of incident information management, multiple data sources need to be imported to the incident information management system's data interface in a simple and direct way. Therefore, a data integration module that resides between the underneath heterogeneous data sources and the upper intelligent analysis modules is required to work as a middleware to perform the tasks as data modeling, integration, formation preprocessing, and to provide a high-importable, structuralized, ef<sup>fi</sup>cient, and uni<sup>fi</sup>ed data interface to upper applications. This data integration module not only handles existing data source heterogeneity but provides high scalability that preserves connection port and growing space for future new data sources and formats as well.

The data integration module proposed here includes the following services:

• support the underneath multi-source data layer;

• contain the algorithms for heterogeneous data's modeling, fusion, and <sup>fi</sup>ltering;

• provide a uni<sup>fi</sup>ed data integration interface to upper application modules;

• provide high scalability and importability.

The architecture of the data integration module for the incident information management (IIM) system is shown in Fig. 2.

A distributed middleware approach can be deployed to implement the heterogeneous data integration module, in which the middleware layer is located under the upper data mining and decision support modules and atop the underneath heterogeneous data sources. It works as a data adaptor between the two layers. Such a middleware approach may bring the following bene<sup>fi</sup>ts:

## • Cross-platform importability

The data integration module can support various computing platforms such as Windows/VC++, Solaris/J2EE, and Linux/Eclipse.

## • High scalability

This allows the addition of new data sources and formats to the system without reengineering, which is a big advantage for system expansion.

![](/api/attachments/VQ3M5SSH/fulltext/images/ba048030b29b23e2dab94ec12e26b14c93b60e2d61a326ac928a09a9dc8b5251.jpg)  
Fig. 2. Architecture of the data integration module.

## • Design reuse

The middleware approach realizes the decoupling between the upper service modules and the underneath heterogeneous data sources, which allows adding or removing data sources without impacting the upper applications and saves the cost caused by application reengineering.

The heterogeneous data integration module (see Fig. 3) has three components, namely the Distributed Heterogeneous Data Interface, the XML-based Integrated Processor, and the Uni<sup>fi</sup>ed Data Interface (UDI). The Distributed Heterogeneous Data Interface is designed as a distributed process and can receive and convert heterogeneous data through wired or wireless connections. The XML-based Integrated Processor provides the functions of modeling, integration, and fusion to various types of data sources based on data fusion algorithms. UDI offers a standardized and easy-to-use programming interface to the upper data mining and decision support modules to allow needed data conversion and exchange.

## 3.2. The data mining module

Emergency management personnel are often overwhelmed with large amounts of information and need to make time-sensitive decisions [37]. The objective of the data mining module in incident information management framework is to help DMs understand characteristics of emergencies and predict future events by analyzing available incident information using a collection of data mining functions. The data integration module provides fundamental supports for data mining and other decision support applications. The uni<sup>fi</sup>ed data interface of the integration module supplies not only a well-structured programming interface to the data mining module but also a differentiated service mechanism to service requests with various levels of time delays.

![](/api/attachments/VQ3M5SSH/fulltext/images/8e18a4db5a7629b6ba2e2ac1f54ec0f2796acfac25a8494e3af3ab9502f72561.jpg)  
Fig. 3. Components of the data integration module.

When applying data mining methods to emergency management, it is important to keep in mind that technical models provide only one input to the decision-making process. Other components, especially tacit knowledge about social impacts of emergencies, should be taken into consideration in emergency management process [20].

The dif<sup>fi</sup>culties and challenges of prediction are essentially determined by available time and resources [10]. In incident information management, timeliness is especially critical in prediction and pattern recognition because delays can reduce the usefulness of effective interventions and alternative courses of action [7]. Different phases of the incident management have different levels of time pressure. Preincident phases, including prevention and protection, emphasize complete and comprehensive data analysis, while post-incident phases, including response and mitigation activities, require fast and often real-time prediction and decision support. Therefore, the proposed data mining module is designed to handle incident preparedness and real-time response activities with dissimilar emphases and separate functions.

## 3.2.1. Data mining in incident preparedness

Incident preparedness activities include planning, organizing, training, equipping, exercising, evaluating, and taking corrective action [48]. Since preparations can facilitate ef<sup>fi</sup>cient and effective crisis response, mitigation, and recovery, it is an important topic in incident management literature [54,67]. Information collected during pre-event preparation is enormous and covers a wide variety of data sources (e.g., local departments, census bureau, utility companies) and data types (e.g., street maps, building design records, evacuation plans) [32]. Utilizing the uni<sup>fi</sup>ed data interface provided by the data integration module, data mining module is able to analyze heterogeneous incident information and provide predictions on incident potential.

Data mining uses methods, algorithms, and techniques from a variety of disciplines to extract useful knowledge from large amounts of data in order to support decision making [55]. Data mining methods can be used across the lifecycle of incident management. They can help DMs understand the features and impact of an incident, design the emergency response plans and training programs, analyze vulnerability, and predict the probabilities of emergencies.

Data mining functionalities can be broadly divided into class characterization and discrimination, mining frequent patterns and association rules, classi<sup>fi</sup>cation and prediction, and cluster analysis [28]. All these functions can be applied to pre-incident preparation. The basic ideas of each function and its role in incident management are described below.

3.2.1.1. Class characterization and discrimination. Class characterization summarizes the general features of a target class of data through basic statistical measures and data warehousing operations [28]. Data discrimination uses similar methods to compare the features of a target class and a contracting class (or a set of contracting classes).

Incidents can be considered as target classes of interest. Domain knowledge of a certain type of incident that describes the events, their properties, and relationships between them is valuable in guiding characterization. On the other hand, class characterization, which is based on analysis of disparate and distributed data sources, can enhance existing domain knowledge of incidents. For instance, class characterization techniques can be used to describe general features of a <sup>fi</sup>re situation (e.g., its agents (<sup>fl</sup>ame, heat, and sparks) and secondary threats (<sup>fl</sup>ammable material, explosive material, gas storage, petrol station) [50]) by analyzing a large collection of <sup>fi</sup>re incidents. A complete summarization of characteristics of incidents supports effective incident planning and training.

Since incidents involve various data types, they need different characterization techniques. For numeric data, data features are described by their central tendency and dispersion using measures like mean, median, mode, quartiles, interquartile range (IQR), and variance. For complex data types (such as text, multimedia, image and spatial), data are normally stored in object-relational or object-oriented database systems. Researchers have developed many techniques to handle generalization of complex data types (see, for example, Han and Kamber [28]; Silberschatz et al. [63]).

With the development of data warehouse and online analytic processing (OLAP) techniques, more advanced data browsing, generalization, and characterization can be conducted automatically. For instance, Rivest et al. [56] described a spatial OLAP approach to explore large datasets based on prede<sup>fi</sup>ned spatial, temporal, and categorical hierarchies. The study of integrating data warehouse technology with emergency information systems has been an important topic in incident management [7]. The underlying multidimensional data model of data warehouse allows a comprehensive understanding about the nature of the incident, its consequences, and the in<sup>fl</sup>uence on populations and environment at various levels. For example, when analyzing hospital emergency room admission patterns, data aggregation numbers resulting from hospitals near tourist destinations and urban areas can be signi<sup>fi</sup>cantly different. Data warehouse that collects information from individual hospitals and allows data browsing at <sup>fi</sup>ne-grained levels help researchers avoid making wrong conclusions [7]. Other techniques such as real-time data warehousing can provide instant information and support timely detection of hazardous events [1].

3.2.1.2. Mining frequent patterns and association rules. Frequent pattern analysis and association rule mining aim at extracting regularities, correlations, and dependencies from databases. Frequent pattern refers to a pattern, which can be a set of items, subsequences, and substructures, that appears frequently in a database [28]. Frequent pattern mining reveals intrinsic and important properties of datasets and is the foundation for association rule mining. Association rules are interesting and unexpected association relationships among attributes that satisfy minimum support and con<sup>fi</sup>dence in a database.

Incidents typically involve a series of events that share associations with each other or have inherent regularities. Extracting the associations and dependencies hidden behind these events can be used to predict the happening of an incident and guide planning and training activities in incident preparedness. Few research works have been conducted to apply frequent pattern mining and association rule mining techniques to incident management (e.g., Karasova et al. [34]).

3.2.1.3. Classification and prediction. Classi<sup>fi</sup>cation methods predict a discrete class label of data, while prediction methods model continuousvalued functions. Classi<sup>fi</sup>cation is also known as supervised learning since it requires the number of classes to be de<sup>fi</sup>ned in advance and needs a set of training data with prede<sup>fi</sup>ned class labels. It is a two-step process: the <sup>fi</sup>rst step is to build classi<sup>fi</sup>ers based on training data that has known class labels; the second step uses the established classi<sup>fi</sup>ers to predict class labels of unknown data [28]. Classi<sup>fi</sup>cation and prediction are widely used data mining functions and have various applications in areas like credit approval, bank loan amount determination, medical diagnosis, and insurance fraud detection.

Both classi<sup>fi</sup>cation and prediction functions are useful in incident management. For example, the development of an effective network intrusion surveillance system requires solutions to distinguish operational mistakes caused by system users and intentional intrusions initiated by attackers. In a water contamination by hazardous chemicals situation, prediction models can be used to predict the spreading of chemicals with time [50].

There is a substantial amount of research focusing on the application of classi<sup>fi</sup>cation and prediction techniques to incident management. Kou et al. [40] designed mathematical programming models for multi-class network intrusion detection and achieved satisfactory classi<sup>fi</sup>cation accuracy and low false alarm rate. Boechler [8] applied the Classi<sup>fi</sup>cation and Regression Trees (CART) approach to help emergency response personnel design the evacuation strategies and plans when a toxic compound is released into an inhabited environment.

3.2.1.4. Cluster analysis. A cluster is a collection of data records that are similar to one another within the same cluster and dissimilar to records in other clusters. Cluster analysis groups data into clusters based on some criterion functions. According to the underlying clustering concept, clustering methods can be classi<sup>fi</sup>ed into different categories, such as partitioning, hierarchical, density-based, gridbased, and model-based [28].

Unlike classi<sup>fi</sup>cation, clustering is an unsupervised learning method because it does not require training data and may not state the number of clusters in advance. Clustering algorithms automatically group data records by recognizing their characteristics. Since training data with known class labels are not available in many reallife applications, clustering has broad applications and is an important topic in several disciplines, such as pattern recognition, statistics, machine learning, biology, and marketing. Recently, it has been a highly popular topic in data mining research due to its ability to handle large amounts of data [6,39].

A major challenge in incident information management is how to ef<sup>fi</sup>ciently process and analyze the huge amounts of relevant information to allow timely and well-informed decisions. As a data mining method that is cable of automatically extracting patterns from large databases, cluster analysis is a very useful tool to identify underlying structures of incidents. Current active themes of cluster analysis in data mining, including the scalability of clustering algorithms and the effectiveness of clustering methods to analyze complex data types [28], are of great bene<sup>fi</sup>t to incident information processing. For instance, geographic clustering approaches and tools [24] can help group spatio-temporal data, which are a common data type in incident databases. There have been a few studies that apply clustering methods in incident or emergency management. For instance, Janeja et al. [33] employed density-based clustering algorithms to group alarms received from different sensors in order to generate meaningful alerts for disaster management.

## 3.2.2. Real-time data mining with differentiated service mechanism

Incident management system should provide timely detection of hazardous events to help decision makers take appropriate response activities to avoid or mitigate serious negative consequences of incidents. According to the types of incidents, the requirements for early detection and timely response are different. For example, the urgency of drought events is much lower than an explosive blast threat to a school building. Therefore, a mechanism supporting differentiated data mining services should be built into incident management system. Recently, researchers have developed concepts and methods for realtime data warehousing and data mining. For instance, real-time data warehousing can provide instant information and support timely detection of hazardous events [1]. Data mining algorithms have been designed to produce real-time network intrusion detection with minimum computational cost and reliable accuracy [40,42]. These studies form solid technical foundations for real-time detection of anomalies, trends, and patterns during emergencies.

In this paper, a two-step process is designed to support real-time data mining with differentiated services in the incident informaiton management framework (Fig. 4). The <sup>fi</sup>rst step establishes a differentiated response mechanism. An incident is prioritized based on its urgency and impact. The prioritization can be established using the guidelines provided by the national incident management system (NIMS). For example, life-threatening situations have the highest priority, followed by threat to property, high damage potential, environmental impact, economic impact, and other criteria [48]. The resource availability and the expected effort in resolving a crisis should also be taken into consideration. To support differentiated data mining services, incident priority is quanti<sup>fi</sup>ed by assigning numeric priority codes. Incoming incidents can then be prioritized using their priority codes. In the second step, the appropriate data mining functions and algorithms are invoked based on their priority codes. Incidents with higher priorities will be allocated more effort and resources. The selection of data mining functions, the determination of parameters for models, and the interpretation of data mining results require a solid background and training in the data mining and related <sup>fi</sup>elds [50]. Thus it is important and necessary to establish a uni<sup>fi</sup>ed data interface and graphic user interface (GUI) to facilitate the data mining process and decision making.

![](/api/attachments/VQ3M5SSH/fulltext/images/6bdc9bf2aa73a1af3c5d2ed22ed0e7b1801887c9314267d113ecdd36a1f04585.jpg)  
Fig. 4. Data mining with differentiated service mechanism

Another advantage of introducing a differentiated service mechanism into the incident information management system is to allow an automatic transition between daily incident preparedness and emergency response phase. When there is no high priority events coming into the incident information management system, it operates under a normal mode; when high priority incident appears, the system enters an emergency mode and invokes real-time data mining functions to provide different services.

## 3.3. The MCDM module

During the past 40 years, Multi-Criteria Decision Making (MCDM) has made remarkable progress and developed into a mature discipline. In general, multiple criteria problems can be divided into two categories: multiple criteria discrete alternative problems and multiple criteria optimization problems [68]. There are three major differences between the two types of multiple criteria problems. The <sup>fi</sup>rst difference is the size of alternatives. Multiple criteria discrete alternative problems deal with modestly sized choices on the basis of two or more criteria (e.g., location selection for a new factory), while multiple criteria optimization problems usually concern a large number of or in<sup>fi</sup>nitely many alternatives (e.g., portfolio selection). The second difference is that discrete alternative problems are more likely to be modeled with uncertain values for the criteria than optimization problems. The third difference is the role of value function in the problem. Discrete alternative problems normally explicitly represent a decision maker's utility or value function and multiple criteria optimization problems usually do not use the value function or use decision maker's preferences implicitly in the decision-making process [68].

Many approaches have been developed to solve the two types of problems [17]. For multiple criteria discrete alternative problems, major approaches include multiattribute utility theory (MAUT) [35], analytic hierarchy process (AHP) [58], elimination and choice expressing the reality (ELECTRE) methods [57], data envelopment analysis (DEA) [13], preference ranking organization method for enrichment of evaluations (PROMETHEE) [9], technique for order preference by similarity to ideal solution (TOPSIS) [31], and compromise ranking method (VIKOR) [52]. For multiple criteria optimization problems, major approaches include goal programming [12,41]), vector optimization algorithms [18,22,72], interactive procedures [5,23,38,73], and evolutionary multiobjective optimization [19,30,60,64].

Incident management involves both types of problems and can bene<sup>fi</sup>t from existing MCDM methods and tools. In incident management, it is an important task to assist users in choosing the most appropriate solution from a set of feasible alternatives on the basis of two or more criteria under time pressure, stress, and uncertainty. This type of problems can utilize methods such as AHP, DEA, and TOPSIS to prioritize the alternatives. For instance, MCDM methods can be used to support the preparedness of evacuation plans. Through the GUI and collaborative tools, incident response personnel can input emergency related information to the MCDM module, which can help decision makers select appropriate evacuation plans according to the inputs information, such as geographic information, affected personnel, potential evacuation routes, and potential evacuation strategies (e.g., shelter or evacuation following the release of toxic compounds).

Resources, such as personnel, equipment, supplies, or facilities, need to be dispatched rapidly and smoothly during emergencies. As the size and complexity of incidents grow, the dif<sup>fi</sup>culties in resource allocation and distribution increase. MCDM methods can be used to model the incident resource management procedures, prioritize resource needs, and coordinate resource allocation and distribution [48].

Recently, researchers and practitioners have made efforts to apply MCDM and MAUT methods to incident management. For example, the Open Advanced System for dISaster end emergency management (OASIS) project, funded by the European Commission with the priority “improving risk management”, designed a multi-criteria decision analysis module to allow users to formulate and obtain optimal solutions, evaluate dependencies of each variant of the possible solutions, incorporate expert knowledge and historical data, and assist DMs in making rational choices from several feasible strategies [50]. Barbarosoğlu et al. [3] developed a hierarchical multicriteria methodology for helicopter logistics planning in disaster relief operations. The models proposed in their work address the crew assignment, routing, and transportation issues and aid authorities to respond quickly and ef<sup>fi</sup>ciently during the initial response phase.

Another example of applying MCDM in incident management is Papamichail and French's work [53] on designing an intelligent decision support system for nuclear emergencies. In the early phases of a nuclear emergency, expert systems can be used to automatically generate alternatives to mitigate the damage of the radiation accident. They proposed to use MCDM methods to evaluate and rank the feasible alternatives according to the consequences of each solution and the preferences of the DMs. After determining the main objective of DMs, which is the return to normal living conditions [4], and subcriteria (including population number, individual dose, collective dose, and cost), the feasible strategies generated by expert systems are ranked using MAUT. The DMs can then select the most appropriate strategy ef<sup>fi</sup>ciently.

An important issue in designing a MCDM module for an incident information management system is the development of a practical and interactive graphic user interface. The interface should allow DMs who may have no knowledge of the MCDM theories to effectively interact with the MCDM model and make the best decisions during emergencies.

## 3.4. The incident information management framework

This study develops a conceptual framework for incident information integration, mining, and decision support. The aforementioned data integration module, data mining module, and MCDM module are the main components of this framework. Fig. 5 captures the high-level structure of the framework.

The <sup>fi</sup>rst level of the framework is the heterogeneous data integration module. This module has two interfaces: distributed heterogeneous data interface and uni<sup>fi</sup>ed data interface. The distributed heterogeneous data interface resides between the underneath heterogeneous data sources and differentiated response mechanism. It works as a middleware to perform the tasks as data modeling, integration, and formation preprocessing. The uni<sup>fi</sup>ed data interface prioritizes incoming emergencies using numeric priority codes and provides a high-scalable, structuralized, and uni<sup>fi</sup>ed data interface to upper applications.

The second level combines data mining and MCDM modules to perform decision support functions. Data mining summarizes the characteristics of different types of incidents, reports situation and status of current incidents, and predicts potential incidents and the probable course of events. Through the uni<sup>fi</sup>ed data interface, the appropriate data mining functions and algorithms are invoked to provide differentiated services to different incidents according to their priority codes. MCDM and MAUT functions help DMs choose the most appropriate solution from a set of feasible alternatives and take appropriate responses in a timely and ef<sup>fi</sup>cient manner.

The third level is a graphic user interface and collaboration tools. The collaboration tools and GUI play a crucial role in incident decision making because they facilitate DMs to utilize and interact with the data mining and MCDM functions without knowledge of the underlying technical details and mathematical theories.

## 4. Case study

To validate the proposed framework, this paper conducted a case study that has chosen 5 years of agrometeorological disasters that occurred in China from 1997 through 2001. Since the data are not distributed and have only numeric data type, functions of the data integration module in the framework are not explored and the focus is on the data mining and MCDM modules. This section presents how data mining and MCDM methods can be combined to provide a comprehensive evaluation of the impact of natural disasters on the agriculture production.

## 4.1. The evaluation process

Agrometeorological disasters, such as droughts, <sup>fl</sup>oods, snowstorms, and sandstorms, cause severe losses in China each year. The <sup>fi</sup>ve datasets used in the case study were collected from the Scienti<sup>fi</sup>c Database of Chinese Academy of Sciences [61]. They describe crop damage of 31 provinces in China caused by drought, <sup>fl</sup>ood, hailstorm, and frost between 1997 and 2001 using two indexes, areas covered and areas affected. Areas covered index refers to areas that have experienced a 10% or more crop loss caused by a natural disaster, while areas affected index measures areas that have experienced at least a 30% crop loss caused by a natural disaster. According to the de<sup>fi</sup>nitions, areas covered index describes the overall crop damage of a speci<sup>fi</sup>c area and areas affected index depicts the signi<sup>fi</sup>cant crop reduction caused by a natural disaster.

This paper uses these datasets to demonstrate that the combination of data mining and MCDM methods can be used to evaluate and rank disaster affected areas objectively and assist governments in disaster preparation and resource allocation. Fig. 6 summarizes the three major stages of the evaluation process: data preparation, data mining, and MCDM. Each stage is described in detail in the following sections.

## 4.2. Data preparation

The <sup>fi</sup>ve datasets used in the case study have the same structure, and each collects eight attributes to represent crop damage in 31 Chinese provinces caused by four kinds of agrometeorological disasters. Table 1 extracts a part of the 1997 dataset for illustration purpose. Since attributes are of equal importance in the case study, the <sup>fi</sup>rst step of data preparation is normalization. Each attribute was normalized to a range of 0 to 1 to prevent attributes with larger values from outweighing attributes with smaller values in the evaluation process [28]. A portion of the normalized 1997 dataset is presented in Table 2.

![](/api/attachments/VQ3M5SSH/fulltext/images/2a5fe6a136b4dc80b66efd2b1572772acc1195039e2f1ccf8aaff28f36b8798b.jpg)  
Fig. 5. Incident information management framework.

![](/api/attachments/VQ3M5SSH/fulltext/images/8bdb20fd6d104c9f1eb269e99a30b8b8688370e7dbb16afe5cbb8c820e250875.jpg)  
Fig. 6. The evaluation process of the case study.

The aim of the case study is to provide a comprehensive ranking of the 31 provinces according to the seriousness of agricultural production reduction in each province using data mining and MCDM methods. Since most MCDM methods do not take the time dimension into the ranking process, it is necessary to reduce the 3-dimensional time-series data into the traditional 2-dimensional data. Thus the second step of data preparation applies the time-ordered weighted averaging (TOWA) operator proposed by Guo et al. [25] to transform the normalized <sup>fi</sup>ve datasets into a single table. The TOWA operator is a variation of Yager's ordered weighted averaging (OWA) operator (1988). Assume that there are i rows and j columns in a table within the time interval $[ t _ { 1 } , t _ { k } ] ( k = 1 , 2 , . . . , p ) .$ . In our example, i represents provinces $( i = 1 , 2 , . . . , 3 1 ) , j$ represents attributes $( j = 1 , 2 , . . . , 8 )$ , and k represents years $( k = 1 , 2 , . . . , 5 )$ . Let $x _ { i j } ( t _ { k } )$ and w represent the original attribute value and time-weighted vector, respectively. Then a 3-dimensional value $x _ { i j } ( t _ { k } )$ can be transformed into a 2-dimensional value $x _ { i j }$ using the TOWA formula [25]:

Table 1  
A part of the agrometeorological disaster dataset (1997).

<table><tr><td rowspan="2">Province</td><td colspan="4">Percentage of areas covered to total areas</td><td colspan="4">Percentage of areas affected to total areas</td></tr><tr><td>Drought</td><td>Flood</td><td>Hailstorm</td><td>Frost</td><td>Drought</td><td>Flood</td><td>Hailstorm</td><td>Frost</td></tr><tr><td>Beijing</td><td>34.312</td><td>0.872</td><td>6.397</td><td>0.000</td><td>24.716</td><td>0.872</td><td>2.908</td><td>0.000</td></tr><tr><td>Tianjin</td><td>38.303</td><td>0.000</td><td>1.647</td><td>0.000</td><td>18.534</td><td>0.000</td><td>1.442</td><td>0.000</td></tr><tr><td>Hebei</td><td>42.131</td><td>4.097</td><td>2.717</td><td>0.000</td><td>28.809</td><td>2.179</td><td>1.424</td><td>0.000</td></tr><tr><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Ningxia</td><td>22.541</td><td>0.867</td><td>0.552</td><td>1.576</td><td>7.093</td><td>0.552</td><td>0.236</td><td>0.000</td></tr><tr><td>Xinjiang</td><td>8.104</td><td>0.627</td><td>3.563</td><td>7.853</td><td>4.692</td><td>0.477</td><td>1.781</td><td>1.455</td></tr></table>

Table 2  
A part of the normalized agrometeorological disaster dataset (1997).

<table><tr><td rowspan="2">Province</td><td colspan="4">Percentage of areas covered to total areas</td><td colspan="4">Percentage of areas affected to total areas</td></tr><tr><td>Drought</td><td>Flood</td><td>Hailstorm</td><td>Frost</td><td>Drought</td><td>Flood</td><td>Hailstorm</td><td>Frost</td></tr><tr><td>Beijing</td><td>0.5714</td><td>0.0226</td><td>0.6030</td><td>0.0000</td><td>0.7752</td><td>0.0487</td><td>0.3079</td><td>0.0000</td></tr><tr><td>Tianjin</td><td>0.6379</td><td>0.0000</td><td>0.1553</td><td>0.0000</td><td>0.5813</td><td>0.0000</td><td>0.1526</td><td>0.0000</td></tr><tr><td>Hebei</td><td>0.7016</td><td>0.1063</td><td>0.2561</td><td>0.0000</td><td>0.9036</td><td>0.1217</td><td>0.1508</td><td>0.0000</td></tr><tr><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Ningxia</td><td>0.3754</td><td>0.0225</td><td>0.0520</td><td>0.0742</td><td>0.2225</td><td>0.0308</td><td>0.0250</td><td>0.0000</td></tr><tr><td>Xinjiang</td><td>0.1350</td><td>0.0163</td><td>0.3358</td><td>0.3698</td><td>0.1472</td><td>0.0266</td><td>0.1886</td><td>0.0996</td></tr></table>

$$
x _ {i j} = \sum_ {k = 1} ^ {p} w _ {k} x _ {i j} (t _ {k}), (k = 1, 2, \dots , p)\tag{1}
$$

$$
\text { where } w = (w _ {1}, w _ {2},..., w _ {p}) ^ {\mathrm{T}}, w _ {k} \in [ 0, 1 ], \sum_ {k = 1} ^ {p} w _ {k} = 1.
$$

Formula (1) indicates that the determination of the time-weighted vector $w _ { k }$ is the key to a reliable transformation. By introducing the concepts of entropy and orness function α, the weighted vector can be calculated [69]:

$$
\begin{array}{l} \max \left[ - \sum_ {k = 1} ^ {p} w _ {k} \ln w _ {k} \right] \\ \text { s.t. } \alpha = \frac {1}{p - 1} \sum_ {k = 1} ^ {p} w _ {k} (p - k) \end{array}\tag{2}
$$

where $w _ { k } \in [ 0 , \ 1 ] , \ \sum _ { k = 1 } ^ { p } \ w _ { k } = 1 , \ k = 1 , \ 2 , \ . . . , p .$ The orness function indicates the degree to which the aggregation operator values a time interval. It can take a value between 0 and 1 to re<sup>fl</sup>ect the attitude of a decision maker [59]. An $\alpha = 0$ implies that weights vector w becomes $( 0 , 0 , . . . , 1 )$ and the element with the latest time value gets the largest weight. $\Lambda \cap \alpha = 1$ implies that OWA vector w becomes $( 1 , 0 , . . . , 0 )$ and the element with the earliest time value gets the largest weight. And an $\alpha { = } 0 . 5$ implies that data elements of different years have the same importance. After discussion with domain experts, we assigned a value of 0.1 to αto indicate that data from the most recent years have more importance than those from earlier years. Using formula (2), the weights vector w can be determined: $w = ( 0 . 0 0 5 1 , 0 . 0 1 7 6 , 0 . 0 6 0 1 ,$ $0 . 2 0 6 5 , 0 . 7 1 0 7 ) ^ { \mathrm { T } } . w _ { 1 } , w _ { 2 } , w _ { 3 } , w _ { 4 } ,$ and w are weights assigned to the year 1997, 1998, 1999, 2000, and 2001, respectively. Table 3 shows a portion of the aggregated data. This table is the initialized decision matrix for the following data mining and MCDM stages.

## 4.3. Data mining analysis: clustering

The 31 provinces in the agrometeorological disaster data are the alternatives that MCDM methods need to prioritize. Because 31 alternatives are too many to handle by many MCMD ranking methods, a data mining function – cluster analysis – is used to reduce the number of alternatives <sup>fi</sup>rst. Suppose there are n alternatives. Cluster analysis <sup>fi</sup>rst groups n alternatives into k clusters. Normally, k≪ fififinp .

One alternative from each cluster is then selected to represent that cluster during the ranking process.

Cluster analysis refers to group data records into clusters based on some criterion functions. Cluster can be de<sup>fi</sup>ned as a collection of data records that are similar to one another within the same cluster and dissimilar to the records in other clusters[28]. K-means clustering [44] was chosen in the case study to construct a partition of the original 31 provinces into k clusters that optimizes the partitioning criterion. The choice of <sup>fi</sup>ve as the number of clusters was determined based on the rule of thumb set by Mardia et al. [46] and the opinions of domain experts. It was implemented using the SimpleKMeans algorithm provided by Weka 3.6, a free data mining software package [27]. For each of the <sup>fi</sup>ve generated clusters, the province that has the shortest Euclidean distance to the mean of the cluster was selected to represent the cluster.

## 4.4. MCDM analysis: TOPSIS

Technique for order preference by similarity to ideal solution (TOPSIS) was initially developed by Hwang and Yoon [31] to rank alternatives over multiple criteria. TOPSIS <sup>fi</sup>nds the best alternatives by minimizing the distance to the ideal solution and maximizing the distance to the nadir or negative-ideal solution [49]. All alternative solutions can be ranked according to their closeness to the ideal solution. Since its <sup>fi</sup>rst introduction, a number of extensions and variations of TOPSIS have been developed over the years. The following TOPSIS procedure adopted from Opricovic and Tzeng [51], and Olson [49] was implemented using Matlab in the case study:

Step 1: calculate the normalized decision matrix. The normalized value $r _ { i j }$ is calculated as:

$$
r _ {i j} = x _ {i j} \Bigg / \sqrt {\sum_ {j = 1} ^ {J}} x _ {i j} ^ {2}, j = 1, \dots , J; i = 1, \dots , n.
$$

where J and n denote the number of alternatives and the number of criteria, respectively. For alternative $A _ { j } ,$ , the performance measure of the ith criterion $C _ { i }$ is represented by $x _ { i j } .$

Step 2: develop a set of weights w for each criterion and calculate the weighted normalized decision matrix. The weighted normalized value $\nu _ { i j }$ is calculated as:

$$
v _ {i j} = w _ {i} x _ {i j},   j = 1, \dots , J;   i = 1, \dots , n.
$$

where $w _ { i }$ is the weight of the ith criterion, and $\sum { _ i ^ { n } } { _ { = 1 } { w _ { i } } { = 1 } }$

Step 3: <sup>fi</sup>nd the ideal alternative solution $S ^ { + }$ , which is calculated as:

$$
S ^ {+} = \left\{v _ {1} ^ {+},..., v _ {n} ^ {+} \right\} = \left\{\left(\max _ {j} v _ {i j} | i \in I ^ {\prime}\right), \left(\min _ {j} v _ {i j} | i \in I ^ {\prime \prime}\right) \right\}
$$

where $I ^ { ' }$ is associated with bene<sup>fi</sup>t criteria and $I ^ { \prime \prime }$ is associated with cost criteria.

Table 3  
A part of the aggregated agrometeorological disaster dataset (1997-2001).

<table><tr><td rowspan="2">Province</td><td colspan="4">Percentage of areas covered to total areas</td><td colspan="4">Percentage of areas affected to total areas</td></tr><tr><td>Drought</td><td>Flood</td><td>Hailstorm</td><td>Frost</td><td>Drought</td><td>Flood</td><td>Hailstorm</td><td>Frost</td></tr><tr><td>Beijing</td><td>27.73103</td><td>1.138956</td><td>6.000233</td><td>0</td><td>16.68639</td><td>0.301861</td><td>2.996074</td><td>0</td></tr><tr><td>Tianjin</td><td>38.86606</td><td>0.912994</td><td>3.55208</td><td>0</td><td>22.81563</td><td>0.87675</td><td>1.722817</td><td>0</td></tr><tr><td>Hebei</td><td>35.07154</td><td>1.036337</td><td>5.09922</td><td>1.561851</td><td>24.67341</td><td>0.593996</td><td>2.177363</td><td>0.320701</td></tr><tr><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Ningxia</td><td>23.42854</td><td>1.462185</td><td>4.637721</td><td>1.177774</td><td>15.12409</td><td>0.786791</td><td>2.782866</td><td>0.586255</td></tr><tr><td>Xinjiang</td><td>9.634757</td><td>1.113136</td><td>8.700334</td><td>5.134067</td><td>7.172522</td><td>0.699518</td><td>3.42156</td><td>1.864255</td></tr></table>

Weights of criteria.

<table><tr><td rowspan="2"></td><td colspan="4">Percentage of areas covered to total areas</td><td colspan="4">Percentage of areas affected to total areas</td></tr><tr><td>Drought</td><td>Flood</td><td>Drought</td><td>Flood</td><td>Drought</td><td>Flood</td><td>Drought</td><td>Flood</td></tr><tr><td>Grey relational coefficient</td><td>0.87240</td><td>0.60196</td><td>0.53564</td><td>0.54358</td><td>2.61721</td><td>1.80587</td><td>1.60691</td><td>1.63074</td></tr><tr><td>Weight</td><td>0.08541</td><td>0.05893</td><td>0.05244</td><td>0.05322</td><td>0.25623</td><td>0.17680</td><td>0.15732</td><td>0.15965</td></tr></table>

Step 4: <sup>fi</sup>nd the negative-ideal alternative solution $S ^ { - }$ , which is calculated as:

$$
S ^ {-} = \{v _ {1} ^ {-},..., v _ {n} ^ {-} \} = \left\{\left(\min _ {j} v _ {i j} \Big | i \in I ^ {\prime}\right), \left(\max _ {j} v _ {i j} \Big | i \in I ^ {\prime \prime}\right) \right\}
$$

Step 5: calculate the separation measures, using the n-dimensional Euclidean distance. The separation of each alternative from the ideal solution is calculated as:

$$
D _ {j} ^ {+} = \sqrt {\sum_ {i = 1} ^ {n} \left(v _ {i j} - v _ {i} ^ {+}\right) ^ {2}}, j = 1, \dots , J.
$$

The separation of each alternative from the negative-ideal solution is calculated as:

$$
D _ {j} ^ {-} = \sqrt {\sum_ {i = 1} ^ {n} \left(v _ {i j} - v _ {i} ^ {-}\right) ^ {2}}, j = 1, \dots , J.
$$

Step 6: calculate a rati $\textmu _ { j } ^ { - + }$ that measures the relative closeness to the ideal solution and is calculated as:

$$
R _ {j} ^ {+} = D _ {j} ^ {-} \Big / \left(D _ {j} ^ {+} + D _ {j} ^ {-}\right), j = 1, \dots , J.
$$

Step 7: rank alternatives by maximizing the ratio in Step 6.

Weights w for each criterion are determined by grey relational analysis (GRA) in this study. GRA is a part of grey theory, which has been proposed to handle imprecise and incomplete information in grey systems [16]. GRA is used to decide the weights of areas covered by drought, <sup>fl</sup>ood, hailstorm, and frost. The calculated weights are then used to determine the weights of areas affected criteria. Since areas affected criteria are de<sup>fi</sup>ned as areas that have experienced at least a 30% crop loss, which are at least 3 times larger than areas covered criteria, their weights are 3 times the corresponding areas covered criterion. Speci<sup>fi</sup>cally, weights are calculated as [70]:

Step 1: calculate the grey relational coef<sup>fi</sup>cient:

$$
\gamma \left(x _ {0 j}, x _ {i j}\right) = \frac {\triangle_ {m i n} + \zeta \triangle_ {m a x}}{\triangle_ {i j} + \zeta \triangle_ {m a x}}, \mathrm{i} = 1, 2, \dots , \mathrm{n}; j = 1, \dots , J.
$$

where i is the number of attributes, j is the number of alternatives, and $\zeta$ is the distinguishing coef<sup>fi</sup>cient, ζ∈[0, 1]. The distinguishing coef<sup>fi</sup>cient is used to expand or compress the range of the grey relational coef<sup>fi</sup>cient and it is de<sup>fi</sup>ned as 0.5 in this case study. $x _ { O j }$ is the reference sequence and de<sup>fi</sup>ned as $( x _ { 0 1 } , x _ { 0 1 } , . . . , x _ { 0 J } ) = ( 1 , 1 , . . . , 1 ) . \gamma ( x _ { 0 j } ,$ $x _ { i j } )$ is the grey relational coef<sup>fi</sup>cient between x and $x _ { i j } ,$ and

$$
\begin{array}{l} \triangle_ {i j} = \left| x _ {0 j} - x _ {i j} \right|, \\ \triangle_ {m i n} = \operatorname{Min} \Bigl \{\triangle_ {i j}, i = 1, 2, \dots , n; j = 1, 2, \dots J \Bigr \}, \\ \triangle_ {m a x} = \operatorname{Max} \Bigl \{\triangle_ {i j}, i = 1, 2, \dots , n; j = 1, 2, \dots J \Bigr \} \end{array}
$$

Step 2: calculate the grey relational grade.

$$
r _ {i} = \frac {1}{J} \sum_ {j = 1} ^ {J} \gamma \big (x _ {0 j}, x _ {i j}), \mathrm{i} = 1, 2,..., \mathrm{n}; j = 1,..., J.
$$

Step 3: calculate the weights for each criterion of areas covered by drought, <sup>fl</sup>ood, hailstorm, and frost.

$$
w _ {i} = r _ {i} \Big / \sum_ {i = 1} ^ {n} r _ {i}, \mathrm{i} = 1, 2, 3, 4.
$$

Step 4: calculate the weights for each criterion of areas affected by drought, <sup>fl</sup>ood, hailstorm, and frost by multiplying the corresponding w<sub>i</sub> by 3.

Table 4 summarizes grey relational coef<sup>fi</sup>cients and the weights for each criterion.

The results of k-means clustering and TOPSIS are summarized in Table 5. The leftmost column indicates that there are total <sup>fi</sup>ve clusters. The members column shows the constituent provinces of each cluster. The representative province selected from each cluster is speci<sup>fi</sup>ed in the third column. The ratio $R _ { j } ^ { + }$ calculated using the TOPSIS procedure, which measures the relative closeness of each cluster to the ideal solution, is listed in the fourth column. If the ratio is larger, the ranking of the corresponding cluster will be higher. The TOPSIS ranking of clusters is shown in the rightmost column.

Results of cluster analysis and TOPSIS

<table><tr><td>Cluster</td><td>Members/Provinces</td><td>Representative</td><td> $R_{j}^{+}$ </td><td>Rank</td></tr><tr><td>1</td><td>Tianjin, Hebei, Shānxi, Neimenggu, Liaoning, Jilin, Heilongjiang, Anhui, Henan, Qinghai</td><td>Neimenggu</td><td>0.503466</td><td>3</td></tr><tr><td>2</td><td>Hubei, Hunan, Chongqing</td><td>Hubei</td><td>0.67499</td><td>1</td></tr><tr><td>3</td><td>Shanghai, Zhejiang, Guangdong, Guangxi, Hainan</td><td>Guangxi</td><td>0.419775</td><td>4</td></tr><tr><td>4</td><td>Fujian, Jiangxi, Sichuan, Guizhou, Yunnan, Xizang</td><td>Guizhou</td><td>0.223901</td><td>5</td></tr><tr><td>5</td><td>Beijing, Jiangsu, Shandong, Shǎnxi, Gansu, Ningxia, Xinjiang</td><td>Gansu</td><td>0.504637</td><td>2</td></tr></table>

Table 6 Ranking results comparison.

<table><tr><td rowspan="2">Province</td><td colspan="2">Areas affected/areas covered</td><td colspan="2">Areas covered/total areas</td><td colspan="2">TOPSIS</td><td colspan="2">Areas affected/areas covered</td><td colspan="2">Areas covered/total areas</td><td>TOPSIS</td></tr><tr><td>%</td><td>Rank</td><td>%</td><td>Rank</td><td>Rank</td><td>Province</td><td>%</td><td>Rank</td><td>%</td><td>Rank</td><td>Rank</td></tr><tr><td>Chongqing</td><td>50.9772</td><td>28</td><td>96.65413</td><td>1</td><td>1</td><td>Neimenggu</td><td>67.1343</td><td>4</td><td>43.21087</td><td>13</td><td>3</td></tr><tr><td>Hubei</td><td>67.0374</td><td>5</td><td>59.59628</td><td>3</td><td>1</td><td>Hebei</td><td>64.9138</td><td>6</td><td>42.77418</td><td>15</td><td>3</td></tr><tr><td>Hunan</td><td>58.8409</td><td>14</td><td>43.67051</td><td>10</td><td>1</td><td>Henan</td><td>60.7631</td><td>10</td><td>40.32286</td><td>16</td><td>3</td></tr><tr><td>Shandong</td><td>61.5879</td><td>9</td><td>46.1776</td><td>8</td><td>2</td><td>Heilongjiang</td><td>57.9938</td><td>16</td><td>33.03947</td><td>20</td><td>3</td></tr><tr><td>Shǎnxi</td><td>57.5735</td><td>17</td><td>45.60818</td><td>9</td><td>2</td><td>Hainan</td><td>55.1787</td><td>20</td><td>34.90782</td><td>17</td><td>4</td></tr><tr><td>Gansu</td><td>54.1147</td><td>21</td><td>43.52572</td><td>11</td><td>2</td><td>Guangdong</td><td>53.0843</td><td>23</td><td>31.57532</td><td>21</td><td>4</td></tr><tr><td>Beijing</td><td>57.3996</td><td>18</td><td>34.84955</td><td>18</td><td>2</td><td>Guangxi</td><td>60.4081</td><td>11</td><td>29.36654</td><td>23</td><td>4</td></tr><tr><td>Jiangsu</td><td>56.6457</td><td>19</td><td>34.82825</td><td>19</td><td>2</td><td>Zhejiang</td><td>52.5938</td><td>26</td><td>23.5013</td><td>27</td><td>4</td></tr><tr><td>Ningxia</td><td>62.7894</td><td>7</td><td>30.70582</td><td>22</td><td>2</td><td>Shanghai</td><td>47.8264</td><td>31</td><td>6.242621</td><td>31</td><td>4</td></tr><tr><td>Xinjiang</td><td>53.4704</td><td>22</td><td>24.59108</td><td>26</td><td>2</td><td>Sichuan</td><td>50.7395</td><td>29</td><td>42.90129</td><td>14</td><td>5</td></tr><tr><td>Liaoning</td><td>60.2319</td><td>13</td><td>61.67563</td><td>2</td><td>3</td><td>Jiangxi</td><td>67.6159</td><td>3</td><td>28.35271</td><td>24</td><td>5</td></tr><tr><td>Shānxi</td><td>69.8863</td><td>2</td><td>55.41644</td><td>4</td><td>3</td><td>Fujian</td><td>60.3819</td><td>12</td><td>24.89994</td><td>25</td><td>5</td></tr><tr><td>Jilin</td><td>76.0611</td><td>1</td><td>51.2113</td><td>5</td><td>3</td><td>Guizhou</td><td>50.5449</td><td>30</td><td>21.7011</td><td>28</td><td>5</td></tr><tr><td>Anhui</td><td>61.7801</td><td>8</td><td>50.14103</td><td>6</td><td>3</td><td>Yunnan</td><td>53.0766</td><td>24</td><td>17.38561</td><td>29</td><td>5</td></tr><tr><td>Qinghai</td><td>51.5156</td><td>27</td><td>49.23756</td><td>7</td><td>3</td><td>Xizang</td><td>52.8679</td><td>25</td><td>10.16864</td><td>30</td><td>5</td></tr><tr><td>Tianjin</td><td>58.6534</td><td>15</td><td>43.33114</td><td>12</td><td>3</td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

## 4.5. Results comparison and discussion

The ranking of TOPSIS is compared with two traditionally used rankings by the agricultural department. The results are summarized in Table 6. The two traditional rankings use the percentage of areas affected to areas covered and the percentage of areas covered to total areas, respectively. Because the <sup>fi</sup>rst ranking uses only the seriousness of crop reduction to evaluate the risk of agrometeorological disasters, the ranking result may convey misleading information to a decision maker. For example, although Chongqing and Jiangxi have similar total areas of crops suffering production losses during the period of 1997 to 2001 (7055 thousand hectares vs. 7145 thousand hectares), their rankings are quite different (the 28th vs. the 3rd). The second ranking measures the overall affected areas during agrometeorological disasters without considering the seriousness of disasters, which is an important factor to be considered during disaster preparation and resource allocation.

Comparing with these two rankings, the combination of data mining and MCDM methods provides a comprehensive assessment of the impact of natural disasters on the agriculture production. Cluster analysis groups provinces into clusters based on the analysis of all the attributes. The impact of each type of disaster on a province is analyzed to ensure that provinces within a cluster experiencing a similar overall pattern. The TOPSIS procedure uses GRA to assign different weights to the four kinds of disasters to re<sup>fl</sup>ect their impacts on the agricultural production objectively.

## 5. Conclusions

Incident information management requires immediate and effective response from DMs under pressures and uncertainties. Technological developments in areas such as data collection, storage, computation, and pattern recognition have enabled more effective incident information collection, processing, and exploration. One of the fundamental problems in incident information management is how to integrate and analyze heterogeneous incident data and provide intelligent decision support to DMs. This study proposes a conceptual framework for incident information management to support information integration, intelligent data analysis, and multi-criteria decision making. It develops a three-level framework for incident information management, including heterogeneous data integration, data mining and MCDM, and collaboration tools. Data integration level provides a distributed heterogeneous data interface that integrates various data sources and a uni<sup>fi</sup>ed data interface that facilitates differentiated services to upper application modules. Data mining and MCDM level supports in-Departmenth data analysis, helps DMs choose the most appropriate solution from a set of feasible alternatives, and takes appropriate incident response operations in a timely and ef<sup>fi</sup>cient manner. The third level has a graphic user interface and collaboration tools to facilitate DMs to utilize and interact with the data mining and MCDM functions without knowledge of the underlying technical details and mathematical theories.

To validate the proposed framework, a case study that utilizes data mining and MCDM methods to evaluate the risk of agrometeorological disasters using Chinese agrometeorological disasters data from years 1997 to 2001 is reported. The case study applies the TOWA operator, cluster analysis, grey relational analysis, and TOPSIS procedure to rank 31 provinces according to the impact of four kinds of agrometeorological disasters on their agriculture production. The results illustrate that the combination of data mining and MCDM methods can provide objective and comprehensive assessments of incident risks. Due to the limitation of the datasets used in the case study, the data integration module discussed in the framework is not explored.

The future research on the incident information management framework includes two major directions. The <sup>fi</sup>rst direction is to instantiate the data integration module proposed by developing data fusion algorithms and collecting or simulating incident data sources that re<sup>fl</sup>ect the heterogeneity and variety features discussed in the framework. The second direction is to implement the differentiated response mechanism and realize an automatic transition between daily incident preparedness and emergency response in an incident informaiton management system.

## Acknowledgments

This research has been supported by grants from the National Natural Science Foundation of China under grant nos. 70901011, 70921061.

## References

[1] L. Agosta, K. Gile, Real-time data warehousing: the hype and the reality, White Paper Forrester Research Inc, December 2004

[2] S. Asghar, D. Alahakoon, L. Churilov, Categorization of disaster decision support needs for the development of an integrated model for Dmdss, International Journal of Information Technology & Decision Making 7 (1) (2008) 115–145

[3] G. Barbarosoğlu, L. Özdamar, A. Cevik, An interactive approach for hierarchical analysis of helicopter logistics in disaster relief operations, European Journal of Operational Research 140 (2002) 118–133.

[4] J. Bartzis, J. Ehrhardt, S. French, J. Lochard, M. Morrey, K.N. Papamichail, K. Sinkko, A. Sohier, RODOS: decision support for nuclear emergencies, in: S.H. Zanakis, G. Doukidis, C. Zopounidis (Eds.), Recent Developments and Applications in Decision Making, Kluwer Academic Publishers, Dordrecht, The Netherlands, 2000, pp. 379–394.

[5] R. Benayoun, J. De Montgol<sup>fi</sup>er, J. Tergny, O. Larichev, Linear Programming with Multiple Objective Functions: Step Method (STEM), Math, Programming 1 (1971) 366–375.

[6] P. Berkhin, Survey of Clustering Data Mining Techniques, Technical report, Accure Software, San Jose, CA, 2002.

[7] B.J. Berndt, J.W. Fisher, J.G. Craighead, A.R. Hevner, S. Luther, J. Studnicki, The role of data warehousing in bioterrorism surveillance, Decision Support Systems 43 (4) (2007) 1383–1403.

[8] M. Boechler, Creating a Balanced Response: An Application of Data Mining to Determine when to Shelter or Evacuate, Federal Emergency Management Agency, Miscellaneous reports, 2001.

[9] J.P. Brans, B. Mareschal, P.H. Vincke, PROMETHEE—a new family of outranking methods in multicriteria analysis, in: J.P. Brans (Ed.), Operations Research '84, North-Holland, Amsterdam, 1984, pp. 477–490.

[10] J. Brynielsson, Using AI and games for decision support in command and control, Decision Support Systems 43 (4) (2007) 1454–1463.

[11] W.N. Carter, Disaster Management: A Disaster Manager's Handbook, Asian Development Bank, Manila, 1991.

[12] A. Charnes, W.W. Cooper, Management Models and Industrial Applications of Linear Programming, John Wiley, New York, 1961.

[13] A. Charnes, W.W. Cooper, E. Rhodes, Measuring the ef<sup>fi</sup>ciency of decision making units, European Journal of Operational Research 2 (6) (1978) 429–444.

[14] R. Chen, R. Sharman, H. Rao, S.J. Upadhyaya, Design principles for critical incident response systems, Information Systems and E-Business Management 5 (3) (2007) 201–227.

[15] F. d'Agostino, A. Farinelli, G. Grisetti, L. Iocchi, D. Nardi, Monitoring and Information Fusion for Search and Rescue Operations in Large-scale Disasters, Proceedings of the Fifth International Conference on Information Fusion, 2002, pp. 672–679.

[16] J. Deng, Control problems of grey systems, Systems and Control Letters 1 (1982) 288–294.

[17] J.S. Dyer, P.C. Fisburn, R.E. Steuer, J. Wallenius, S. Zionts, Multiple criteria decision making, multiattribute utility theory: the next ten years, Management Science 38 (5) (1992) 645–654.

[18] J.P. Evans, R.E. Steuer, Generating ef<sup>fi</sup>cient extreme points in linear multiple objective programming: two algorithms and computing experience, in: J.L. Cochrane, M. Zeleny (Eds.), Multiple Criteria Decision Making, University of South Carolina Press, Columbia, SC, 1973, pp. 349–365.

[19] C.M. Fonseca, P.J. Fleming, Genetic algorithms for multiobjective optimization: formulation, discussion, and generalization, Proceeding of Fifth International Conference on Genetic Algorithms, Morgan Kaufmann, San Mateo, CA, 1993, pp. 416–423.

[20] S. French, C. Niculae, Believe in the model: mishandle the emergency, Journal of Homeland Security and Emergency Management 2 (1) (2005) 1–18.

[21] A. Fruhling, G.-J. De Vreede, Field experiences with eXtreme programming: developing an emergency response system, Journal of Management Information Systems 22:4 (2006) 39–68.

[22] A.M. Geoffrion, Proper ef<sup>fi</sup>ciency and the theory of vector maximization, Journal of Mathematical Analysis and Applications 22 (1968) 618-630.

[23] A.M. Geoffrion, J.S. Dyer, A. Feinberg, An interactive approach for multicriterion optimization, with an application to the operation of an academic department, Management Science 19 (1972) 357–368.

[24] D. Guo, M. Gahegan, A.M. MacEachren, B. Zhou, Multivariate analysis and geovisualisation with an integrated geographic knowledge discovery approach, Cartography and Geographic Information Science 32 (2) (2005) 113–132.

[25] Y.J. Guo, Y. Yao, P. Yi, Method and application of dynamic comprehensive evaluation. Systems Engineering-Theory & Practice 27 (10) (2007) 154-158

[26] L.M. Haas, Beauty and the Beast: The Theory and Practice of Information Integration, 12th International Conference on Database Theory, Schwentick and Suciu (Ed.), Lecture Notes in Computer Science, Vol. 4353, Springer-Verlag, Barcelona, Spain, January 2007, pp. 28-43.

[27] M. Hall, E. Frank, G. Holmes, B. Pfahringer, P. Reutemann, I.H. Witten, The WEKA Data Mining Software: an update, SIGKDD Explorations 11 (1) (2009) 10–18.

[28] J. Han, M. Kamber, Data Mining: Concepts and Techniques, 2nd editionMorgan Kaufmann Publishers, San Francisco, CA, USA, 2006

[29] S.K. Harms, J.S. Deogun, J. Saquer, T. Tadesse, Discovering Representative Episodal Association Rules from Event Sequences Using Frequent Closed Episode Sets and Event Constraints, Proceedings of the 2001 IEEE International Conference on Data Mining, 2001, pp. 603–6068, November 29-December 02, San Jose, California, USA.

[30] J. Horn, N. Nafploitis, D. Goldberg, A niched Pareto genetic algorithm for multiobjective optimization, Proceeding of First IEEE Conf. Evolutionary Comput, IEEE Service Center, Piscataway, NJ, 1994, pp. 82–87.

[31] C.L. Hwang, K. Yoon, Multiple Attribute Decision Making Methods and Applications, Springer, Berlin Heidelberg, 1981.

[32] S. Jain, C.R. McLean, An integrating framework for modeling and simulation for incident management, Journal of Homeland Security and Emergency Management 3 (1) (2006).

[33] V.P. Janeja, V. Atluri, A. Gomaa, N. Adam, C. Bornhoevd, T. Lin, DM-AMS: employing data mining techniques for alert management, Proceedings of the 2005 national conference on Digital government research table of contents, 2005, pp. 103–111, Digital Government Society of North America, Atlanta, Georgia, USA.

[34] V. Karasova, J.M. Krisp, K. Virrantaus, Application of Spatial Association Rules for Improvement of a Risk Model for Fire and Rescue Services, Proceedings of the 10th Scandinavian Research Conference on Geographical Information Science, 2005, pp. 183–193, The Department of Planning and Environment, KTH, SE-10044, Stockholm, Sweden.

[35] R. Keeney, H. Raiffa, Decisions with Multiple Objectives: Preferences and Value Tradeoffs, Wiley, New York, 1976.

[36] J.K. Kim, R. Sharman, H.R. Rao, S. Upadhyaya, Ef<sup>fi</sup>ciency of critical incident management systems: Instrument development and validation, Decision Support Systems 44 (1) (2007) 235–250.

[37] R. Klashner, S. Sabet, A DSS Design Model for complex problems: lessons from mission critical infrastructure, Decision Support Systems 43 (3) (2007) 990–1013.

[38] P. Korhonen, J. Laakso, A visual interactive method for solving the multiple criteria problem, European Journal of Operational Research 24 (1986) 211-2S1.

[39] G. Kou, C. Lou, Multiple factor hierarchical clustering algorithm for large scale web page and search engine Clickstream data, Annals of Operations Research (2010), doi:10.1007/s10479-010-0704-3.

[40] G. Kou, Y. Peng, Y. Shi, Z. Chen, Multiple criteria mathematical programming for multi-class classi<sup>fi</sup>cation and application in network intrusion detection, Information Sciences 179 (Issue 4) (February 1 2009) 371–381.

[41] S.M. Lee, Goal Programming for Decision Analysis, Auerbach, Philadelphia, 1972.

[42] W. Lee, S.J. Stolfo, P.K. Chan, E. Eskin, F. Wei, M. Miller, S. Hershkop, J. Zhang, Real time data mining-based intrusion detection, Proceedings of the DARPA Information Survivability Conference & Exposition II, 2001, pp. 89–100, IEEE Computer Society, Anaheim, CA, USA.

[43] J. Llinas, Information Fusion for Natural and Man-Made Disasters, Proceedings of the Fifth International Conference on Information Fusion, 2002, pp. 570–576.

[44] S.P. Lloyd, Least squares quantization in PCM, IEEE Transactions on Information Theory 28 (2) (1982) 129–137.

[45] B. Ludascher, K. Lin, S. Bowers, E. Jaeger-frank, B. Brodaric, C. Baru, Managing scienti<sup>fi</sup>c data: from data integration to scienti<sup>fi</sup>c work<sup>fl</sup>ows, geoinformatics: data to knowledge, The Geological Society of America (GSA) Today, Special Issue on Geoinformatics, , 2006.

[46] K. Mardia, J.T. Kent, J.M. Bibby, Multivariate Analysis (Probability and Mathematical Statistics), Academic Press, 1979.

[47] D. Mendonça, Decision support for improvisation in response to extreme events: learning from the response to the 2001 World Trade Center attack, Decision Support Systems 43 (3) (2007) 952–967.

[48] National Incident Management System (NIMS), United States, Federal Emergency Management Agency, http://www.fema.gov/emergency/nims/2008.

[49] D.L. Olson, Comparison of weights in TOPSIS models, Mathematical and Computer Modelling 40 (7–8) (2004) 721–727.

[50] Open Advanced System for dISaster end emergency management (OASIS), Decision support activities research report, OASIS FP6 Consortium, http://www. oasis-fp6.org/2008.

[51] S. Opricovic, G.H. Tzeng, Compromise solution by MCDM methods: a comparative analysis of VIKOR and TOPSIS, European Journal of Operational Research 156 (2004) 445–455.

[52] Y. Ouyang, H. Shieh, J. Leu, G. Tzeng, A Vikor-based multiple criteria decision method for improving information security risk, International Journal Of Information Technology & Decision Making 8 (2) (2009) 267–287.

[53] K.N. Papamichail, S. French, Design and evaluation of an intelligent decision support system for nuclear emergencies, Decision Support Systems 41 (1) (2005) 84–111.

[54] C.M. Pearson, I.I. Mitroff, From crisis prone to crisis prepared: a framework for crisis management, Academy of Management Executive 7 (1) (1993) 48–59.

[55] Y. Peng, G. Kou, Y. Shi, Z. Chen, A Descriptive framework for the <sup>fi</sup>eld of data mining and knowledge discovery, International Journal of Information Technology and Decision Making 7 (4) (2008) 639–682.

[56] S. Rivest, Y. Bédard, M.-J. Proulx, M. Nadeau, F. Hubert, J. Pastor, SOLAP technology: merging business intelligence with geospatial technology for interactive spatio-temporal exploration and analysis of data, ISPRS Journal of Photogrammetry and Remote Sensing 60 (2005) 17–33.

[57] B. Roy, How outranking relation helps multiple criteria decision making, in: J.L. Cochrane, M. Zeleny (Eds.), Multiple Criteria Decision Making, University of South Carolina Press, Columbia, SC, 1973, pp. 179–201.

[58] T.L. Saaty, The Analytic Hierarchy Process, McGraw-Hill, New York, 1980.

[59] R. Sadiq, S. Tesfamariam, Probability density functions based weights for ordered weighted averaging (OWA) operators: an example of water quality indices, European Journal of Operational Research 182 (3) (2007) 1350–1368.

[60] J.D. Schaffer, Some experiments in machine learning using vector evaluated genetic algorithms. Ph.D. thesis, Vanderbilt University, Nashville, TN, 1984.

[61] Scienti<sup>fi</sup>c Database Chinese Academy of Sciences, 2010, Available online at: http:// www1.csdb.cn/.

[62] P.D. Scott, G.L. Rogova, Crisis Management in a Data Fusion Synthetic Task Environment, Proceedings of 7th Int'l Conf. Information Fusion, 2004, pp. 330–337, International Society of Information Fusion Stockholm Sweden

[63] A. Silberschatz, H.F. Korth, S. Sudarshan, Database system concepts, <sup>fi</sup>fth edition, McGraw-Hill Education, Columbus, OH, USA, 2005.

[64] N. Srinivas, K. Deb, Multiobjective optimization using nondominated sorting in genetic algorithms, Evolutionary Computation J. 2 (1994) 221–248.

[65] L. Stoimenov, B. Predić, V. Mihajlović, M. Stanković, GIS Interoperability Platform for Emergency Management in Local Community Environment, Proceedings of 8<sup>th</sup> AGILE Conference on GIScience, Estoril, Portugal, 2005.

[66] M. Turoff, M. Chumer, B. Walle, X. Yao, The Design Of A Dynamic Emergency Response Management Information System (DERMIS), The Journal of Information Technology Theory and Application 5 (4) (2004) 1–35.

[67] P.J. van Baalen, P.C. van Fenema, Instantiating global crisis networks: the case of SARS, Decision Support Systems (2009), doi:10.1016/j.dss.2009.05.005.

[68] J. Wallenius, J.S. Dyer, P.C. Fisburn, R.E. Steuer, S. Zionts, K. Deb, Multiple criteria decision making, multiattribute utility theory: recent accomplishments and what lies ahead, Management Science 54 (7) (2008) 1336–1349.

[69] R.R. Yager, On ordered weight averaging aggregation operators in multi-criteria decision making, IEEE Trans on Systems, Man, and Cybernetics 18 (1) (1988) 183–190.

[70] Kuo Yi, T. Yang, G. Huang, The use of grey relational analysis in solving multiple attribute decision-making problems, Computers & Industrial Engineering 55 (Issue 1) (August 2008) 80–93.

[71] S.W. Yoon, J.D. Velasquez, B.K. Partridge, S.Y. Nof, Transportation security decision support system for emergency response: a training prototype, Decision Suppor Systems 46 (1) (2008) 139–148.

[72] P.L. Yu, M. Zeleny, The set of all nondominated solutions in the linear cases and a multicriteria simplex method, Journal of Mathematical Analysis and Applications 49 (1975) 430–468.

[73] S. Zionts, J. Wallenius, An interactive programming method for solving the multiple criteria problem, Management Science 22 (1976) 652–663.

Yi Peng (pengyicd@gmail.com) is an Associate Professor at School of Management and Economics, University of Electronic Science and Technology of China. Previously, she worked as Senior Analyst for West Corporation, USA. Dr. Peng received her Ph.D. in Information Technology from the College of Information Science & Technology, University of Nebraska at Omaha, and got her Master's degree at the Department of Info. Science & Quality Assurance, University of Nebraska at Omaha, and Bachelor of Science degree at the Department of Management Information Systems, Sichuan University, China, respectively. Dr. Peng's research interests cover knowledge discover in database and data mining, multi-criteria decision making, data mining methods and modeling, knowledge discovery in real-life applications. She published more than forty papers in various peer-reviewed journals and conferences. She is the Workshop Chair of the 20th International Conference on Multiple Criteria Decision Making (2009), guest editor of Annals of Operations Research's special issue on Multiple Criteria Decision Making on Operations Research. Dr. Peng's work has been published or accepted in Decision Support Systems, Information Sciences, Annals of Operations Research, International Journal of Information Technology and Decision Making, Optimization Methods and Software, and various book series/conference proceedings.

Yong Zhang (vx300@163.com) is a graduate student at School of Management and Economics, University of Electronic Science and Technology of China. He received his Bachelor of Science degree at the Department of Management Science and E-Commerce, University of Electronic Science and Technology of China. His research interests include emergency management, multi-criteria decision making, data mining methods and modeling.

Yu Tang (yutang@uestc.edu.cn) is a Professor at School of Computer Science and Engineering, University of Electronic Science and Technology of China. Previously, he worked as Lead Engineer for Raytheon Company, USA. Dr. Tang received his Ph.D. in Computer Science, The George Washington University, USA, and got his Master's degree at the Department of Computer Science, Bowie State University, USA, respectively. Dr. Tang's current research interests are service computing modeling and software systems, cloud storage and computing, sensor network and real-time routing algorithm, Intelligent Decision Support Systems.

Shiming Li (lism@uestc.edu.cn) is a Professor at the School of Management and Economics, University of Electronic Science and Technology of China. Dr. Li received his Ph.D. in Southwestern University of Finance and Economics, China. He has published more than 100 papers and 8 books in strategy management, organization behavior, business management and technology management.
