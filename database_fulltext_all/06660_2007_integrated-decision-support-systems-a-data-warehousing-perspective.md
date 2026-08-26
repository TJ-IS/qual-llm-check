---
otero_id: 6660
otero_key: "EAKZ2AGD"
title: "Integrated decision support systems: A data warehousing perspective"
authors: "Salvatore T. March; Alan R. Hevner"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.05.029"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dss

# Integrated decision support systems: A data warehousing perspective

Salvatore T. March <sup>a,\*</sup>, Alan R. Hevner <sup>b</sup>

<sup>a</sup>Owen Graduate School of Management, Vanderbilt University, 401 21st Avenue South, Nashville, TN 37203, United States <sup>b</sup>College of Business Administration, University of South Florida, United States

Available online 20 July 2005

## Abstract

Successfully supporting managerial decision-making is critically dependent upon the availability of integrated, high quality information organized and presented in a timely and easily understood manner. Data warehouses have emerged to meet this need. They serve as an integrated repository for internal and external data—intelligence critical to understanding and evaluating the business within its environmental context. With the addition of models, analytic tools, and user interfaces, they have the potential to provide actionable information resources—business intelligence that supports effective problem and opportunity identification, critical decision-making, and strategy formulation, implementation, and evaluation. Four themes frame our analysis: integration, implementation, intelligence, and innovation. © 2005 Elsevier R V. A11 rigb

Keywords: Data warehouse; Data warehousing architecture; Integrated decision support; Intelligence; Business intelligence

## 1. Introduction

Conceptually the idea of a data warehouse is extremely simple. As popularized by Inmon [12] and Inmon and Hackathorn [13] a data warehouse is a <sup>b</sup>subject-oriented, integrated, time-invariant, non-updatable collection of data used to support management decision-making processes and business intelligence. A data warehouse is a repository into which are placed all data relevant to the management of an organization and from which emerge the information and knowledge needed to effectively manage the organization [44]. While this is clearly a simplistic and idealistic view it allows us to begin the investigation of the foundations, key challenges, and research directions for this discipline. Importantly it highlights the purpose of a data warehouse: support for all levels of management decision-making processes through the acquisition, integration, transformation, and interpretation of internal and external data [25].

To begin, it is important to differentiate a data warehouse, the repository for integrated data, from data warehousing, the development, management, operational methods, and practices that define how these data are collected, integrated, interpreted, managed, and used. It is similarly important to distinguish intelligence from business intelligence. We use the term intelligence in its general sense of information—information acquired to aid the purposeful execution of business processes. We use the term business intelligence to refer to inferences and knowledge discovered by applying algorithmic analysis to acquired information. A data warehouse is a repository of intelligence from which business intelligence can be derived.

The goal of this presentation is to provide both researchers and practitioners a clear view of the challenges and opportunities of applying data warehousing technology to support all levels of management decision-making. We begin by reviewing information requirements for decision support via a general systems theory of management. From this foundation, sets of data warehousing functions are identified and organized into a layered data warehousing architecture. Research areas are highlighted as we discuss the design and implementation of these functions within each of the layers. Four overarching themes frame our analysis: integration, implementation, intelligence, and innovation.

Much of the recent literature on data warehousing has focused on operational concerns. There are a number of commercial tools and industry success stories describing this level of data warehousing (e.g., [4,23,44]). To effectively meet the emerging needs of modern organizations research in data warehousing must move beyond these operational and even tactical level decisions. It must address support for business strategy formulation and evaluation [17]. Despite the early research on critical success factors (CSF) and executive information systems (EIS) (e.g., [3,24,31,33,42]) and the more recent work on electronic dashboards and balanced scorecards (e.g., [1,16,19,21]), the links between data warehousing and strategic decision-making and evaluation remain under-researched. To fully explore the opportunities for research in this area, we begin our presentation with an overview of management, strategy, and the role of information in management processes.

## 2. Information requirements for management decision support

General Systems Theory (GST) provides a lens through which business organizations can be understood [5,7,34]. Fig. 1 illustrates a systems view of how a business operates. Every system has a purpose or goal that drives the strategy behind its design and organization. Economists describe a business as a production system that adds value to the environment. The overall goal of the business is to maximize its long term value [26]. It does so by transforming lower-valued resources acquired from the environment into higher-valued goods and services distributed back to the environment. The general functions of management are to: strategize, organize, lead, acquire and allocate resources, and monitor business activities to assure that the difference between the value of the outputs and the value of the inputs is maximized [20].

![](/api/attachments/EAKZ2AGD/fulltext/images/f543c360f66a32b5c1b78a5c21a66c6d45c1c81f550a5951136bcd47dc5c51a2.jpg)  
Fig. 1. A general systems theory view of a business.

Every business has input, production, and output processes that define its workflow [6,41]. The input processes acquire resources from the environment. Resources acquired from the environment include capital, labor, raw materials and other goods and services from vendors and other partners, as well as technology and environmental information. It is crucial that organizations systematically acquire the en vironmental information needed to make decisions and to evaluate the effects of those decisions. At a minimum this environmental information must in clude customer and market product preferences, vendor and partner capabilities, best practice production methodologies, and competitive analyses. Capital, labor, and raw materials are transformed by production processes into products that are distributed and serviced via the output processes [27,29]. Environmental information is combined with internal data by the information processor and transformed into information by which management can create strategies, develop standards (goals against which to measure organizational performance), make decisions, design business processes, and evaluate business performance with respect to the established standards.

Profit maximization, the general economic goal of a business, does not occur spontaneously. Strategies must be developed and processes must be designed and managed [6,28] that enable the organization to effectively utilize its core capabilities and gain a competitive advantage. Decisions must be made that define the way in which each business process is performed and how each is evaluated. Measurable standards must be created against which the performance of each process can be compared. Data must be gathered from each process, combined with environmental information, and transformed into useful information for executive decision-making [46] and business evaluation [1,16]. Problems and opportunities can be viewed as deviations from established standards [36]. The role of the information processor is to integrate and interpret this data and transform it appropriately for management use. Hence, management decisions affect business workflow processes, standards, and the information processor. Data must be gathered, transformed into information, and compared to standards, thus enabling their evaluation and completing the management cycle.

A key question for business organizations is the role of information technology in each of these processes. Advances in information technology have redefined how organizations perform these processes and have enabled them to significantly reduce cost or improve performance through automation. Significant examples include computer-aided design (CAD) and computerintegrated manufacturing (CIM); the automated acquisition and processing of customer orders through electronic data interchange (EDI) systems; electronic marketplaces and Web services; and automated customer relationship management (CRM) systems.

Within this context decision support systems (DSS) focus on the process labeled Manage and data warehouses focus on the process labeled Information Processor. Information technology can play a significant role in each of these processes; however, there are major challenges that must be addressed. Drucker [9] describes the types of information that executives need and outlines the shortcomings of existing management philosophies and IT applications to acquire and use these data effectively. He differentiates internal information, useful for tactical level decision-making and evaluation, from external information, useful for strategic decision-making and evaluation. Each is discussed briefly below.

Drucker refers to internal information as <sup>b</sup>four sets of diagnostic tools<sup>Q</sup> that enable executives <sup>b</sup>to make informed judgments<sup>Q</sup> needed <sup>b</sup>to manage the business for wealth creation<sup>Q</sup> ([9], p. 58). The four sets of tools are: foundational information, productivity information, competence information, and resource-allocation information.

Foundational information includes traditional accounting and financial measurements such as cashflow and liquidity projections and ratios. While it is extremely common for a high-level executive to have access to such information in aggregate, it is much less common for operational level managers to predict and assess the impact of their decisions on these measures. As distributed decision-making has become more common it has become more important for this type of information to be available to these managers. At the same time it has become more important for their incentive structures to be aligned more closely with the impact of their decisions on the overall performance of the organization. A sales manager may, for example, decide to give a price discount in order to obtain a large sales order. The impact on gross sales is obviously positive. However, the impact on profit may be positive or negative depending on a number of factors such as the ability of the customer to pay in a timely manner, production capacity, inventory levels, existing or projected sales orders from other customers, competition, etc. These data must be captured and integrated into the data warehouse, transformed into an appropriate form for the sales manager and for the manager of the sales manager to use effectively, and the data must be positioned in the appropriate timeframe.

Productivity information describes the effectiveness and efficiency of organizational production processes [46] including knowledge-based and servicebased processes and the opportunity costs associated with management decisions. Drucker suggests economic value-added analysis (EVA) and benchmarking as appropriate mechanisms for measuring productivity performance [9]. These require obtaining external, often industry-based, data and interpreting it within the context of the organization to infer the impact of business decisions. Integrating such data and the resulting inferences with existing operational data and strategies as they evolve over time is both a significant challenge and a major opportunity for the data warehousing research community.

Competence information describes the core competencies that enable a business to succeed [30]. These are unique abilities that differentiate a business from its competitors and form the basis from which competitive advantage can be gained. Identifying, developing, and measuring core competencies are crucial and challenging management tasks. Drucker suggests that doing so requires an organization to carefully track business successes and failures, particularly unexpected successes and failures, and to gather information (intelligence) required to understand the causes for each. He further argues that innovation is a core competency that all business organizations need to develop. These are areas in which data warehousing technology has not been widely applied but has potential for adding significant value to a business [9]. Research is needed to address the determination, acquisition, integration, and application of information enabling the identification and use of core competencies. Decision-making at all levels of management must focus on leveraging such organizational competencies to gain competitive advantage. Adding to the research challenge is that much of this information is unstructured or at best semi-structured.

Resource-allocation information deals with the effective and efficient use of scarce organizational resources. Drucker focuses on capital and human resources recognizing that all decisions require a manager to evaluate the alternatives to which those resources may be applied and to assess the implications of the success or failure of the selected resource allocation. This implies that objectives (standards) must be developed against which the performance of that allocation can be measured. Similarly it implies that appropriate data must be gathered to enable such an evaluation. Clearly these issues present challenges for the data warehouse as capital investments are made and as human resource allocations change over time.

The final type of information Drucker identifies as necessary for wealth creation is environmental information—<sup>b</sup>information about markets, customers, and non-customers; about technology in one’s own industry and others; about world-wide finance; and about the changing world economy<sup>Q</sup> ([9], p. 61).

A serious cause of business failure is the common assumption that conditions–taxes, social legislation, market preferences, distribution channels, intellectual property rights, and many others–must be what we think they are or what we think they should be. An adequate information system has to include information that makes executives question that assumption. It must lead them to ask the right questions, not just feed them the information they expect. That presupposes first that executives know what information they need. It demands further that they obtain that information on a regular basis. It finally requires that they systematically integrate the information into their decision-making.

The wide range of critical information requirements for business decision-making and their diverse sources, both internal and external to the organization, present a clear challenge to the development of data warehouses and the decision support systems that utilize them [45]. Wetherbe recognizes that executive information requirements are different from operational requirements and chides IS professionals for their lack of adequate methodology to determine executive information needs. Simply capturing terabytes of transaction data and loading it into a data warehouse–a common data warehouse development method–is simply not sufficient. He proposes a methodology that addresses what he claims are four fundamental mistakes that developers typically make when attempting to determine executive information needs. <sup>b</sup>These mistakes are viewing systems as functional instead of cross-functional, interviewing managers individually instead of jointly, asking the wrong questions during the interview, and not allowing trial-and-error in the detail design process<sup>Q</sup> ([46], p. 53).

Recognizing the cross-functional and more recent cross-organizational nature of executive information requirements demands significant integration efforts and presents organizational as well as technical challenges. Disciplined approaches, such as Joint Appli cation Design (JAD), to bring stakeholders together can be used to deal with this challenge. But more telling are the questions and content discussed at such joint meetings. Wetherbe contends that simply asking, <sup>b</sup>What information do you want?<sup>Q</sup> is counter-productive. Questions must address problems, solutions, decisions, critical success factors, ends (goals, performance measures), and means (alternatives). Not unlike the information needs discussed above, these questions cause managers to focus on business performance, how to measure and evaluate business suc cess, and how to improve business effectiveness. Data warehousing becomes an enabling technology.

Summarizing the above discussion, a key role of the data warehouse is to provide compelling business intelligence to the decision-maker facilitating an understanding of business problems, opportunities, and performance. It must incorporate internal and external knowledge acquired over time and adapt it to current business conditions. Turning to the psychology literature, one approach to this task is to provide a facility for developing events, critical incidents, and exceptions into a narrative or <sup>b</sup>story<sup>Q</sup> that taps into the human sense-making capability [11,32,40]. How to develop data warehouses that convey such a story to managers is a fundamental research challenge.

In his classic article on the development of decision support systems, Sprague differentiates three DSS subsystems, the data subsystem, the model subsystem, and the user interface subsystem [37].

The data subsystem corresponds to the data warehouse and the model subsystem corresponds to analytic (e.g., Online Analytical Processing (OLAP)), knowledge discovery, and data mining tools [14] each having an interface subsystem enabling them to communicate with the decision-maker. He argues that a DSS should support all phases of the management decision-making process citing Simon’s intelligence-design-choice model as an exemplar [35]. Specifically, intelligence refers to the process of searching the environment for conditions calling for decisions. Design refers to the process of inventing, developing, and analyzing possible courses of action. Choice refers to the process of selecting a particular course of action from those available. Implementation and evaluation processes typically follow choice [10].

The intelligence phase is of specific significance to data warehouse development. Webster’s dictionary defines intelligence as <sup>b</sup>(n.) inborn quickness of understanding and adaptability to relatively new situations; information.<sup>Q</sup> Webster’s Revised Unabridged Dictionary adds, <sup>b</sup>the ability to comprehend; to understand and profit from experience.<sup>Q</sup> We argue that understanding, adaptability, and profiting from experience are three important components of intelligence that need to be designed into data warehouses. Data warehouses must be understandable, adaptable, and include experience-based organizational knowledge. They must provide information that enables managers to identify situations requiring action and to understand the situation and its causes. They must enable a manager to locate and apply relevant organizational (experience-based) knowledge and to predict and measure the impact of a decision over time. These are significant challenges for the data warehousing research community.

## 3. Data warehousing architecture

With an understanding of the business information to be captured and integrated, we now turn our attention to the challenges of implementing an effective data warehouse. Without entering the debate about the merits of the top-down <sup>b</sup>corporate information factory<sup>Q</sup> [12] versus the bottom-up <sup>b</sup>business data mart architecture<sup>Q</sup> [18] approaches to developing a data warehouse, we present a layered architecture for understanding the functionality required to successfully implement data warehousing technology, independent of the manner in which the data warehouse is developed. Fig. 2 illustrates our data warehousing layered architecture.

In a layered architecture, each layer is dependent on the services in lower layers. However, each higher layer is independent of the design decisions made in the lower layers. The kernel Content Management layer addresses data capture, instance-level data integration, and data quality, particularly consistency and timeliness. It defines what data are available in the data warehouse. The Integration and Design layer addresses warehouse design and metadata management. It includes semantic and conceptual level integration, logical and physical design, and performance issues. The Use layer addresses information dissemination including the application of analytical, knowledge discovery, and data mining tools, privacy and security, and user training and support. The Evolution layer addresses change management concerns as the data warehouse responds to changing business needs. The following sections discuss the responsibilities and research challenges found in the four data warehouse architecture layers.

## 3.1. Content management

Managing the content of a data warehouse is a daunting task. Locating and acquiring the data needed to produce the types of information described above are significant challenges. Integrating the acquired information may be even more challenging. Modern organizations use a wide variety of distributed information systems to conduct their day-to-day business. These operational systems draw data from a variety of databases that operate on different hardware platforms, use different operating systems and DBMSs, and have different database structures with varying structural, conceptual, and instance level semantics.

Existing practice successfully addresses many of the hardware, operating system, DBMS, and structural heterogeneities associated with such systems. However, major challenges remain for data warehouse content management. These include identifying and accessing the appropriate data sources, coordinating data capture from them in an appropriate timeframe, assuring adequate data quality, and integrating instance level data.

A data warehouse serves as a repository for data extracted from diverse operational information systems and acquired from external sources. The extract, transform, and load (ETL) functions in a data warehouse are considered the most time-consuming and expensive portion of the development lifecycle [38]. These processes are concerned with the extraction of data from legacy systems and external sources, the transformation and pre-processing necessary to produce useful, integrated data, and the transportation of the data into the actual data warehouse structures. Often operational systems are not designed to be integrated and data extracts must be performed manually or on a schedule determined by the operational systems. Furthermore acquired data from external sources is rarely in a form conducive to integration.

![](/api/attachments/EAKZ2AGD/fulltext/images/eda3b1f08c1768e1b32ba1ab2330420263c0178289fca897d96153a01763ad93.jpg)  
Fig. 2. Data warehousing layered architecture.

As a result even data extracted from internal systems may not be consistently represented in the data warehouse. Data extracted from an inventory system, for example, may not be synchronized with data extracted from order processing or purchasing systems or specialized systems handling <sup>b</sup>internal transfers.<sup>Q</sup> Reports produced from the data warehouse may be inconsistent and unusable, particularly for real-time decision-making situations. Coordination mechanisms must be established. However, the pace of business, particularly Web-based applications, may demand operational systems be available <sup>b</sup>24 - 7<sup>Q</sup> making extracts and synchronization major problems.

Data quality is a major concern for many operational systems as well as for data warehouses [15,43]. Validation of accuracy, timeliness, completeness, and consistency remain major problems for many organizations even in internal information systems where users are trained and managed by the organization. These problems are multiplied in information systems that are exposed to customers, vendors, and other partners. The result can be a disaster for a data warehouse that depends on such systems for its content. Mechanisms for protecting a data warehouse from poor quality data are crucial. At the same time rejecting data from an operational system due to quality concerns can exacerbate the data synchronization problems discussed above, particularly when the organization is using the data warehouse to integrate diverse information systems. Methods for monitoring and cleansing data during ETL have been shown to be successful [2]; however, more attention to data quality issues in data warehouses is needed.

Instance level data integration has been studied extensively in the context of heterogeneous databases;

however, its solution remains elusive. Organizations routinely have multiple entries in operational databases for the same entity in the world. Reasons for this are varied, including data entry errors or limitations of existing software (e.g., disallowing multiple locations for a single customer may cause the organization to maintain a customer record for each location). While this problem is prevalent in internal information systems, the emergence of inter-organizational and Web-based systems and the trend toward mergers and acquisitions magnify its importance.

Content management consists of the fundamental and time-consuming activities essential to the development of an effective data warehouse. Attention to detail at this kernel layer provides a basis for the confident use of designer and user functions at subsequent data warehouse layers.

## 3.2. Integration and design

Given that the data from varied sources have been loaded into the data warehouse, the next set of challenges is the determination, representation, and conceptual integration of the data that are relevant to the managerial decision-making in an organization. Methodologies for these tasks are in their infancy. Current data and dimensional modeling (e.g., star schemas) approaches for data warehouses [18] focus almost exclusively on data extracted from current or proposed operations.

Certainly it is valuable to identify dimensions along which managers can <sup>b</sup>slice, dice, roll-up, and drill-down<sup>Q</sup> on facts acquired from operational systems. However, such an analysis fails to provide an adequate foundation for management decision-mak ing or strategy formulation and evaluation [28]. Methodologies are needed that focus on the intelligence phase of decision-making in which managers scan the environment for problems and opportunities [35]. These cannot be limited to the operational level of an organization nor can they be limited to activities that are internal to the business. They must include strategy and goals both within the organization and within its competitive environment. They must trace strategy to tactical plans and operational implementation defining key performance indicators at each level. They must be integrative yet flexible, identifying and reconciling heterogeneities among data definitions and concepts used in all levels of management concern.

Furthermore, semantic heterogeneities and instance level integration continue to pose enormous challenges. Briefly stated, a semantic heterogeneity exists when data is defined differently by different users. Differences can be as simple as naming conventions or units of measures which can be easily addressed using conversion tables. Frequently they are much more complex involving different criteria for capturing data and different meanings ascribed to captured data. For example, the use of varied and incompatible geographical units (e.g., zip codes, census tracks, political boundaries—townships, counties, states, nations) to group data creates major problems when that data must be compared and integrated. Such differences must be resolved if data from incompatible systems are to be stored in a common data warehouse. The challenge is to integrate data from diverse information systems in the face of organizational or economic constraints that require those systems to remain autonomous, i.e., retain their differences. Important research challenges that must be addressed include: schema integration, schema evolution, and query processing in such a heterogeneous environment [22].

Clearly the data warehouse must go beyond its current role as a repository of historical data describing the operations and transactions in which the organization has engaged. It must include data describing partners and partnerships, policies and rules of the business, competitors and markets, goals and standards, opportunities and problems, successes and failures, and alternatives and predicted futures. Such data are often unstructured or semi-structured. Methodologies and representational formalisms for this level of analysis are sorely lacking.

## 3.3. Use

Organizations use data warehousing to support strategic and mission-critical applications. Data deposited into the data warehouse must be transformed into information and knowledge and appropriately disseminated to decision-makers within the organization and to critical partners in various capacities within the organizational value chain. Crucial problems that must be addressed in this area are: the modes of dissemination of information to the end user; the development, selection, and implementation of appropriate models, analytic tools, and data mining tools; the privacy and security of data; system performance; and adequate levels of training and support.

The human–computer interface is of paramount importance in the data warehouse environment and the primary determinant of success from the end-user perspective. In order to support analysis and reporting tasks, the data warehouse must have high quality data and make these data accessible through intuitive interface technologies. Data warehouse browsing tools provide star-schema query-like access through a flexible menu-based interface, with pull-down menus representing important dimensions. These types of tools are easy to use and support some ad-hoc exploration, but are usually controlled through an administrative layer that determines the data available to endusers. In developing a flexible interface, there is a tradeoff between the ability to express ad-hoc queries and the ease-of-use that results from pre-defined constructs implemented by data warehouse designers and administrators. Of course, SQL can provide an ad-hoc query facility, but its use requires some care in the data warehouse environment where the combination of very large tables and ill-formed user queries can produce some truly awful performance and potentially erroneous results. Casual users may not have sufficient understanding of SQL or of the database schema to effectively use such an interface. Typically, only trained power users (e.g., DBAs, application developers) are permitted to write SQL queries on a data warehouse.

There are a number of commercially available analytic tools and data mining tools applied in data warehousing. Online Analytical Processing (OLAP) tools support multidimensional views of the data warehouse. OLAP <sup>b</sup>cubes<sup>Q</sup> are frequently extracted from the data warehouse and made available to managers for specific decision-making situations. Using tools such as ORA-CLE Discoverer, Cognos PowerPlay, MicroStrategy, Business Objects, or even pivot tables in Excel spreadsheets managers can <sup>b</sup>slice, dice, drill-down, and rollup<sup>Q</sup> instance-level data along pre-defined dimensions. These can be extremely useful for identifying and exploring the causes of problem situations. For example, drilling down on sales for a specific product that has not met its sales goals can help a manager identify which customers or regions are underperforming with respect to that product. However, they are not very effective for generating solution alternatives once the problem is identified nor are they effective in <sup>b</sup>discovering<sup>Q</sup> relationships within the data that can be used for strategy formulation or implementation.

Data mining and other <sup>b</sup>knowledge discovery in database<sup>Q</sup> (KDD) tools, on the other hand, are specifically designed to identify relationships and <sup>b</sup>rules<sup>Q</sup> within the data warehouse [14]. Unfortunately the identified relationships and rules may or may not be useful to management. Often such tools require users to specify the type of relationship or rule sought. For example, a data mining tool could be used to identify products that are frequently purchased at the same time or products whose purchase is dependent on other previously purchased products. Enabling managers and power users to indiscriminately search the data warehouse looking for relationships or rules can raise serious privacy and security concerns, particularly when using Web-based tools.

Analytic tools and data mining tools have become quite powerful; however, they may be too complex and sophisticated for the average information consumer. Managers who are comfortable with paper-based reports may find the transition to data warehouse tools to be uncomfortable and counterproductive. Keys to effective data warehouse use are identifying the right tools for the different types of data warehouse users and providing adequate training and support once those tools have been selected. For a manager whose primary concern is monitoring sales levels over time by product and sales region a simple Excel spreadsheet automatically connected to an OLAP cube may be sufficient. For a manager attempting to identify new marketing strategies and pricing schemes more sophisticated tools are required.

Furthermore, the value of the available tools is dependent upon matching the data characteristics to the managerial need. Early data warehouse applications assumed that currency was not a required characteristic for managerial decision-making. Hence data warehouses were often <sup>b</sup>refreshed<sup>Q</sup> from operational databases on a weekly or monthly basis. Given the accelerated pace of business, <sup>b</sup>active<sup>Q</sup> or <sup>b</sup>flash<sup>Q</sup> data warehouses are becoming more prevalent. Such data warehouses are updated virtually in parallel with operational databases. This can lead to integrity and consistency problems because data are in a constant state of flux. Analytical results can vary literally from one moment to another.

The trend toward real-time data warehousing for both tactical and strategic decision-making has led to interest in the concept of Business Activity Monitoring (BAM) [39]. When faced with a critical business decision, the manager must quickly assemble and analyze the situation with full views of both the organizational internal and external contexts. This requires access to current as well as historical information on objectives, past performance, external forces, internal resources, potential events, and timerelated issues. The manager will also need to be able to communicate and coordinate with others within and outside the organization. Finally, a decision will be made to take action or to delegate the decision-making authority. Fully deployed BAM systems assume that these capabilities are available to managers throughout the business organization.

In reality, tactical decision support systems and BAM solutions will require innovative research and development before they reach an adequate level of maturity for widespread deployment. Research issues pertinent to real-time data warehousing include integration of operational information with historical information, handling events and alerts as real-time data, scalability to growing numbers of users, realtime performance of analytic engines, and building active applets and alert mechanisms into user interfaces (e.g., electronic dashboards) [8]. The role of an effective data warehouse is central to the future of real-time tactical and strategic decision-making.

## 3.4. Evolution

The key challenge in this layer is that the data warehouse must be <sup>b</sup>designed for change<sup>Q</sup> from the beginning. As business organizations evolve, their information systems and their data warehouses must evolve with them. New data definitions, new instances, and new tools must be accommodated. Version control becomes crucial. Depending on the data warehouse definition even simple analyses can become problematic in the face of evolving business characteristics. How, for example, can management interpret historical sales comparisons if sales districts are reorganized or customers are transferred from one salesperson to another? How are historical product sales to be analyzed when, due to a merger or acquisition, product lines have been redefined? There is very little theory or guidance available for data warehouse managers to make decisions on how to deal with such changes. Change management in data warehouses is an area ripe for research.

Research challenges in data warehousing for integrated decision support

<table><tr><td>Architecture layer</td><td>Research challenges</td></tr><tr><td>Content management</td><td>Data selectionData captureExtraction, transformation, and loading (ETL)Instance-level data integrationData quality</td></tr><tr><td>Integration and design</td><td>Conceptual data integration from heterogenous systemsData warehouse schema designMeta-model managementBusiness intelligence scanningSupply chain integration</td></tr><tr><td>Use</td><td>Data dissemination modesAnalytical models and toolsData mining models and toolsEnd-user training and supportReal-time updating of active data warehousesReal-time tactical and strategic decision-makingBusiness activity monitoring</td></tr><tr><td>Evolution</td><td>Design for changeChange management and version control</td></tr></table>

## 3.5. Data warehouse research challenges

In this discussion we have presented a layered architecture of data warehousing foundations. Each of the four layers–Content Management, Integration and Design, Use, and Evolution–presents significant value to organizations and challenges for researchers and practitioners as summarized in Table 1. The data warehouse architecture enables the capture and integration of data into the data warehouse and the transformation of that data into useful information and knowledge disseminated appropriately to decisionmakers within the organization.

## 4. Data warehouse themes in decision support

Throughout this paper, as we have studied the effective use of data warehouses for managerial decisionmaking, four overarching objectives have emerged. They are integration, implementation, intelligence, and innovation. As concluding remarks, we briefly expand on the importance of each of these themes to the successful use of decision support systems in business organizations. Fig. 3 guides the discussion.

## 4.1. Integration

The essence of the data warehousing concept is the integration of data from disparate sources into one coherent repository of information. Achieving a satisfactory level of integration across both internal and external data is the first and, perhaps, the foremost challenge facing a data warehouse designer. Integration is also at the heart of decision-making tools supported by a data warehouse. The ability to draw business intelligence from the data warehouse to make tactical or strategic decisions is dependent upon a full integration of all raw data, current and historical, that may have impact upon that decision. The inability to integrate a critical data source may mean that a decision is being made without awareness of all relevant data and the decision-maker may not even realize that such missing data exists. Research on integration issues has been discussed in all layers of the data warehouse architecture. Effective integration decisions can only be made by those thoroughly familiar with the domain ontologies both internal and external to the business system.

![](/api/attachments/EAKZ2AGD/fulltext/images/bd56896fdf0703b85edeaa7f572a567e622876c165f9299ea80198c267f7f94b.jpg)  
Fig. 3. Themes for data warehouse support of management decision-making.

## 4.2. Implementation

Implementation involves the hard work of designing, building, and evaluating the infrastructure of the data warehouse and the decision support systems to which it interfaces. As shown in Fig. 3, results from integration decisions will provide important requirements for the implementation activities. Research and practitioner challenges abound in the areas of physical and logical data warehouse design, model management systems, analytic tools, user interfaces, distributed decision-making via networks or the Internet, and decision dissemination policies. Critical issues of data quality, information security, individual privacy, resource availability, system performance, and compliance with organizational standards must be resolved often via difficult tradeoffs.

## 4.3. Intelligence

Intelligence is rooted in acquiring the appropriate data (environmental scanning). Business intelligence is rooted in interpreting that data with respect to a business task (contextualization). Once the data ac quisition and integration systems are implemented, the procedures for effectively using the resultant information to derive business intelligence must be put into place. Such procedures must be aligned with existing business processes in the organization. For example, newly derived business intelligence on supply chain processes (e.g., altered product mixes, new distribution channels) must be able to immediately and effectively impact these processes. The ability to generate business intelligence can be assisted by computational methods such as data mining, genetic algorithms, neural networks, and case-based reason ing [25]. Active research projects are currently exploring the application of these methods to derive business intelligence from information in data warehouses. Another key area of research is the development of more effective human–computer interfaces to support management decision-making activities. The best business intelligence is only effective if it can be viewed, interpreted, and verified by a human with the authority to act on it.

## 4.4. Innovation

As noted earlier, innovation must be a core competency of any organization if it is to survive and thrive [9] in the current business environment. Business intelligence, used effectively, will lead to innovations in business products, services, and processes. Such innovations must align with the corporate vision and strategies to be successful. Innovations will lead to organizational changes and the need to manage these changes. A critical component of change management will be the evolution of the data warehouse to capture the results of the changes and to support on-going future cycles of improved management decision support systems.

## Acknowledgements

We would like to thank the participants in the AIS SIGDSS Pre-ICIS Workshop, Research Directions on Decision Support, held on December 14, 2003 in Seattle, Washington at which an early version of this paper was presented. We would also like to thank Hugh J. Watson (University of Georgia) for his constructive critique of this work. Thanks are also due to Steve Alter, Karen (Dowling) Corral, and Michael Goul for their support and encouragement in this project and for their efforts in organizing this special issue.

## References

[1] R.D. Banker, H. Chang, S.N. Janakiraman, C.A. Konstans, A balanced scorecard analysis of performance metrics, European Journal of Operational Research 154 (2) (2004 (April)).

[2] D. Berndt, A. Hevner, J. Studnicki, The CATCH data warehouse: support for community health care decision making, Decision Support Systems 35 (2003 (June)).

[3] A.C. Boynton, R.W. Zmud, An assessment of critical success factors, Sloan Management Review 25 (4) (1984 (Summer)).

[4] G.G. Bustamente, K. Sorenson, Decision support at land’s end—an evolution, IBM Systems Journal 33 (2) (1994 (June)).

[5] P. Checkland, Systems Thinking, Systems Practice, John Wiley & Sons, New York, 1999.

[6] T. Davenport, Process Innovation: Reengineering Work through Information Technology, Harvard Business School Press, Cambridge, MA, 1992.

[7] G. Davis, M. Olson, Management Information Systems: Conceptual Foundations, Structure and Development, second ed., McGraw-Hill, Boston, MA, 1985.

[8] H. Dresner, B. Hostmann, and B. Gassman, B., Predicts 2004: Business Intelligence Technology Directions, Commentary Note COM-21-6252, Gartner, Inc. (Dec. 2003).

[9] P.F. Drucker, The information executives truly need, Harvard Business Review 73 (1) (1995 (JanuaryFebruary)) 54 – 62.

[10] G.A. Forgionne, M. Mora-Tavarez, F. Cervantes-Pe´rez, R. Kohli, Development of integrated decision-making support systems: a practical approach, Proceedings AMCIS 2000 (Long Beach, CA) 2003 (Aug.7).

[11] J.P. Gee, The narrativization of experience in the oral style, Journal of Education 167 (1985)2002.

[12] W.H. Inmon, Building the Data Warehouse, 3rd ed., Wiley, New York, 2002.

[13] W.H. Inmon, R.D. Hackathorn, Using the Data Warehouse, Wiley, New York, 1994.

[14] J. Jackson, Data mining: a conceptual overview, Communica tions of the AIS 8 (2002)2000.

[15] M. Jarke, M. Lenzerini, Y. Vassiliou, P. Vassiliadis, P. Vassiliadis (Eds.), Fundamentals of Data Warehouses, Springer-Verlag, Berlin, 2000.

[16] R.S. Kaplan, D.P. Norton, The Strategy-Focused Organization: How Balanced Scorecard Companies Thrive in the New Business Environment, Harvard Business School Press, Cambridge, MA, 2000.

[17] K. Kendall, The significance of information systems research on emerging technologies: seven information technologies that promise to improve managerial effectiveness, Decision Sciences 28 (4) (1997 (December))2002.

[18] R. Kimball, M. Ross, The Data Warehouse Toolkit: The Complete Guide to Dimensional Modeling, Second edition, Wiley, New York, 2002.

[19] A.S. Maiga, F. Jacobs, Balanced scorecard, activity-based costing and company performance: an empirical analysis, Journal of Managerial Issues 15 (3) (2003 (Fall))1994.

[20] S. Maital, Executive Economics: Ten Essential Tools for Managers, The Free Press, New York, 1994.

[21] M.A. Malina, F.H. Selto, Communicating and controlling strategy: an empirical study of the effectiveness of the balanced scorecard, Journal of Management Accounting Research 13 (2001).

[22] S.T. March, A.R. Hevner, S. Ram, Research commentary: an agenda for information technology research in heterogeneous and distributed environments, Information Systems Research 11 (4) (2000 (Dec.)).

[23] MicroStrategy, Inc., MicroStrategy 7i Sales Analysis Module Reference Guide (Version 7.2.3), 2003, available at http://www. teradatastudentnetwork.com/ (downloaded April 1, 2004)

[24] M.C. Munro, B.R. Wheeler, Planning, critical success factors, and management information requirements, MIS Quarterly 4 (4) (1980 (Dec.)).

[25] S. Negash, Business intelligence, Communications of the AIS 13 (2004)2000.

[26] M. Parkin, Microeconomics, fifth edition, Addison-Wesley, Reading, MA, 2000.

[27] M.E. Porter, Competitive Advantage: Creating and Sustaining Competitive Performance, The Free Press, New York, 1985.

[28] M.E. Porter, What is strategy? Harvard Business Review 74 (6) (1996 (Nov.–Dec.)) 61 – 78.

[29] M.E. Porter, V.E. Millar, How information gives you competitive advantage, Harvard Business Review (1985 (Jul.–Aug.)).

[30] C.K. Prahalad, G. Hamel, The core competence of the corporation, Harvard Business Review (1990 (May–June)).

[31] R.K. Rainer Jr., H.J. Watson, The keys to executive information system success, Journal of Management Information Systems 12 (2) (1995 (Fall))1986.

[32] J.A. Robinson, L. Hawpe, Narrative thinking as a heuristic process, in: T.R. Sarbin (Ed.), Narrative Psychology: The Storied Nature of Human Conduct, Prager Publishers, New York, NY, 1986.

[33] J.F. Rockart, A.D. Crescenzi, Engaging top management in information technology, Sloan Management Review 25 (4) (1984 (Summer))1990.

[34] P.M. Senge, The Fifth Discipline: The Art and Practice of the Learning Organization, Doubleday, New York, 1990.

[35] H.A. Simon, The New Science of Management Decision, Harper and Row, New York, 1960.

[36] H.A. Simon, The Sciences of the Artificial, 3rd edition, MIT Press, Cambridge, MA, 1996.

[37] R.A. Sprague, A framework for the development of decision support systems, MIS Quarterly 4 (4) (1980 (Dec.)).

[38] J. Srivastava, P. Chen, Warehouse creation—a potential roadblock to data warehousing, IEEE Transactions on Knowledge and Data Engineering 11 (1) (1999 (Jan.))1983.

[39] TIBCO, Business Activity Monitoring: The Evolution of Managerial Vision and Agility, White Paper, TIBCO, Inc. (Jan. 2004) available at: http://www.tibco.com/resources/mk/ businesfactor<sup>\_</sup>event<sup>\_</sup>driven<sup>\_</sup>performance<sup>\_</sup>mgmt.pdf (downloaded April 1, 2004).

[40] E. Tulving, Elements of Episodic Memory, Oxford University Press, New York, NY, 1983.

[41] W. vanderAalst, K. vanHee, Workflow Management: Models, Methods, and Systems, MIT Press, Cambridge, MA, 2004.

[42] L. Volonino, H.J. Watson, The strategic business objectives method for guiding executive information systems development, Journal of Management Information Systems 7 (3) (1990–1991 (Winter)).

[43] Y. Wand, R.Y. Wang, Anchoring data quality dimensions in ontological foundations, Communications of the ACM 39 (11) (1996 (Nov.)).

[44] H.J. Watson, Developments in data warehousing, Communications of the AIS 8 (2001).

[45] H.J. Watson, B.H. Wixom, J.D. Buonamici, J.R. Revak, Sherwin-Williams’ data mart strategy: creating intelligence across the supply chain, Communications of the AIS 5 (2001).

[46] J.C. Wetherbe, Executive information requirements: getting it right, MIS Quarterly 15 (1) (1991 (Mar.)).

![](/api/attachments/EAKZ2AGD/fulltext/images/a3d0c5bc859385c39d4a93ea44338f9d21acfcf1a978e909dd9c8acca148da43.jpg)

Salvatore T. March: Salvatore T. March is the David K. Wilson Professor of Management at the Owen Graduate School of Management, Vanderbilt University. He received a BS in Industrial Engineering and MS and PhD degrees in Operations Research from Cornell University. His research interests are in information system development, distributed database design, information economics, and electronic commerce. His research has appeared in

journals such as Communications of the ACM, Decision Support Systems, IEEE Transactions on Knowledge and Data Engineering, Information Systems Research, and MIS Quarterly. He served as the Editor\_in\_Chief of ACM Computing Surveys and as an Associate Editor for MIS Quarterly. He is currently a Senior Editor for Information Systems Research and an associate editor for Decision Sciences Journal.

![](/api/attachments/EAKZ2AGD/fulltext/images/e1dcbd25a1341b746dfa8518baa95090db673013dffa2b106e94234fbc535d2f.jpg)

Alan R. Hevner: Alan R. Hevner is an Eminent Scholar and Professor in the College of Business Administration at the University of South Florida. He holds the Salomon Brothers/Hidden River Corporate Park Chair of Distributed Technology. His areas of research interest include information systems development, software engineering, distributed database systems, and healthcare information systems. He has published numerous research papers on these topics and

has consulted for several Fortune 500 companies. Dr. Hevner received a PhD in Computer Science from Purdue University. He has held faculty positions at the University of Maryland at College Park and the University of Minnesota. Dr. Hevner is a member of ACM, IEEE, AIS, and INFORMS.
