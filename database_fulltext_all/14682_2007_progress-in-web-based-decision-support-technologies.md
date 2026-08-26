---
otero_id: 14682
otero_key: "DUJGDSGB"
title: "Progress in Web-based decision support technologies"
authors: "Hemant K. Bhargava; Daniel J. Power; Daewon Sun"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.07.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Progress in Web-based decision support technologies

Hemant K. Bhargava <sup>a,\*</sup>, Daniel J. Power <sup>b</sup>, Daewon Sun <sup>c</sup>

<sup>a</sup> University of California Davis, United States

<sup>b</sup> University of Northern Iowa, United States

<sup>c</sup> University of Notre Dame, United States

Available online 8 August 2005

## Abstract

World Wide Web technologies have transformed the design, development, implementation and deployment of decision support systems. This article reviews and summarizes recent technology developments, current usage of Web-based DSS, and trends in the deployment of such systems. Many firms use the Web as a medium to convey information about DSS products or to distribute DSS software. The use of Web-based computation to provide product demonstrations or to deploy DSS applications for remote access remains less common. The academic literature on Web-based DSS is largely focused on applications and implementations, and only a few articles examine architectural issues or provide design guidelines based on empirical evidence.

<sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Decision Support Systems; World Wide Web; Data-driven DSS; Model-driven DSS; Implementation

## 1. Introduction

Modern decision support systems (DSS) provide their users with a broad range of capabilities. Current DSS facilitate a wide variety of decision tasks including information gathering and analysis, model building, sensitivity analysis, collaboration, alternative evaluation, and decision implementation. Often, DSS are built and used for ad hoc analyses, but increasingly, decision support is integrated into business processes and information systems. In the past few years, the

World Wide Web (Berners-Lee et al. [11]) has facilitated, nurtured, and promoted a broad resurgence in the use of decision technologies to support decision-making tasks. The global Internet and the World Wide Web are now the primary enabling technologies for delivering computerized decision support. Due to the growing interest in the Web, there are many on-going efforts to develop and implement Web-based DSS in various areas, such as health care, private companies, government, and education.

This article surveys the progress in implementing Web-based decision support technologies by examining both academic research and industry practice. A Web-based DSS delivers decision support to a manager or business analyst using a <sup>b</sup>thin-client<sup>Q</sup> Web browser interface which may integrate client-side computation technologies such as Java applets or JavaScript.<sup>1</sup> Web-based decision support has come a long way since the discussion of the idea at the 3rd International Conference of the International Society for Decision Support Systems (ISDSS) in Hong Kong in 1995. This article chronicles major activities and developments on this topic and expands and updates Bhargava and Power’s [5] status report on DSS and Web technologies. The next section offers a brief historical overview of DSS practice and research with an emphasis on developments since the introduction of Web technologies. Following that, Section 3 explores the extent to which Web technologies can impact – and have impacted – major tasks associated with building and using DSS. The final two sections examine the <sup>b</sup>State of Practice<sup>Q</sup> and <sup>b</sup>State of Research<sup>Q</sup> associated with Web-based DSS. While we have taken a broad view of DSS developments, the paper does present a somewhat biased perspective – drawing on our own interests and efforts – and should not be viewed as an exhaustive survey, but rather as our review and status report.

## 2. Historical perspective

Decision support research began in the 1960s. Scott Morton [48] demonstrated that managers benefited from using a computer-based management decision system. According to Klein and Methlie [31], <sup>b</sup>. . .the first DSS papers were published by PhD students or professors in business schools, who had access to the first time-sharing computer system: Project MAC at the Sloan School, the Dartmouth Time Sharing Systems at the Tuck School<sup>Q</sup> and in France at HEC.

The 1970s was a period of conceptual and technology development for DSS. The focus was on supporting individual decision makers, and this focus was reinforced by the introduction of the personal computer in the 1980s. This perspective was, however, too limiting from the standpoint of real-world business decision making. In the mid-1980s, Group Decision Support Systems were developed to support communication-oriented tasks in decision making by teams. By the late 1980s, executive information systems became fashionable in companies and further broadened the scope of decision support.

In the early 1990s, a shift occurred from mainframe-based DSS to client–server DSS. In addition, several firms introduced a new kind of data-oriented decision support, via the use of online analytical processing (OLAP) tools. In 1992–93, the first enterprise data warehouses were completed. Soon after, with the privatization of the Internet and the sudden growth of the World Wide Web, many companies started to upgrade their network infrastructures. According to Powell [40], DBMS vendors <sup>b</sup>recognized that decision support was different from OLTP and started implementing real OLAP capabilities into their databases.<sup>Q</sup>

By the mid-1990s, researchers were exploring the possibilities for the next generation of DSS (cf., [8,12,26]). Several academic researchers and software developers had realized that the World Wide Web and Internet technologies created new opportunities for building and deploying decision support systems. Using the Web as a delivery mechanism for DSS forced a rethinking of what had been assumed true about implementing DSS. At the 1995 International Society for Decision Support Systems (ISDSS) conference, Bhargava and Krishnan (and co-authors) presented the first of a series of papers on DecisionNet, an electronic marketplace of Web-based decision support systems [6,7]. Several other papers (cf., [1,23,29]) presented at the conference also examined the use of the Web and Internet for decision support. These, and other papers covering the development of Web-based GDSS and Web access to data warehouses, were published in a 1997 special issue [12] of Decision Support Systems. In November 1995, Power, Bhargava, and Quek submitted the initial Decision Support Systems Research page to ISWorld. The goal was to provide a useful starting point for accessing Web-based material related to the design, development, evaluation, and implementation of Decision Support Systems. Nine months later, a DSS/WWW Workshop was held as part of the International Federation for Information Processing (IFIP) Working Group 8.3 Conference on <sup>b</sup>Implementing Systems for Supporting Management Decisions: Concepts, Methods, and Experiences<sup>Q</sup> held July 21–24, 1996 in London, UK.

A similar movement was happening among Information Systems practitioners as well. Organizations were exploring how to use the Internet and Web to enhance distributed decision making and make better use of computerized decision support systems. In 1996–97, corporate intranets were developed to support information exchange and knowledge management. The primary decision support tools in use included ad hoc query and reporting tools, optimization and simulation models, online analytical processing (OLAP), data mining, and data visualization (cf., [40]). Enterprise-wide DSS using database technologies were especially popular in Fortune 2000 companies and Web-based DSS was a new topic [41]. In 1998, innovative enterprise performance management and the balanced scorecard systems were introduced. Vendors promoted these tools as a new generation of executive information systems. In 1998, the concept of an extensible mark-up language (XML) for conveying additional information as part of a Web page was also formalized.

By the end of the 1990s, several software firms were working on new Web-based analytical applications. Many database management system (DBMS) vendors shifted their focus to Web-based analytical applications and business intelligence solutions. In 2000, application service providers (ASPs) began hosting some application software and technical infrastructure for decision support capabilities. DSS technology had gone full-circle and companies again had access to time-sharing decision support. Year 2000 was also the year of the portal and the beginning of discussions about the need for semantic Web capabilities to increase the <sup>b</sup>machine processing<sup>Q</sup> possibilities for Web content. Also, more sophisticated <sup>b</sup>enterprise decision and knowledge portals<sup>Q</sup> were introduced by vendors that combined information portals, knowledge management, business intelligence, and communications-driven DSS in an integrated Web environment (cf., [49]).

In about 2002, both software and hardware vendors began discussing Grid and Utility computing (cf.

[13,36,47]). The impact of these technologies on Web-based DSS remains uncertain. It seems plausible that due to these technology developments, decision support systems can utilize far larger and more complex models and much larger data sets at dramatically lower costs. Integrated development environments such as the LAMP Web development environment (which combines the LINUX operating system, Apache Web server, the MySQL database application, and PHP middleware) have also become more common as a DSS development environment. Today, the Web is the platform of choice for building DSS.

Going beyond the concept of Web-based deployment of individual DSS, Bhargava et al. [8] envisioned that a collection of such systems from multiple providers could be advertised and discovered via an electronic library, and that decision computation could be <sup>b</sup>sold<sup>Q</sup> on a pay-per-use basis in an electronic marketplace. They experimented with these ideas in the DecisionNet project and analyzed some of the non-technological challenges in commercial development of Web DSS [9]. While Web technologies have facilitated Web-based deployment of decision computing, as evidenced by the emergence of application service providers, the non-technological challenges have inhibited the large-scale commercial realization of Web-based decision technologies. The ASP concept, while heavily promoted in industry a few years ago, has witnessed only limited success. ASP firms and clients have struggled with issues such as a payment model, reliability of systems and moral hazard problems related to remote Web-based computation.

## 3. Web-based decision support

A number of frameworks or typologies have been proposed for organizing our knowledge about Decision Support Systems (cf., [44,50]). In the expanded framework (cf., [45]), the two most widely implemented approaches for delivering decision support are called data-driven and model-driven DSS. Data-driven DSS help managers organize, retrieve, and analyze large volumes of relevant data using database queries and OLAP techniques. Model-driven DSS use formal representations of decision models and provide analytical support using the tools of decision analysis, optimization, stochastic modeling, simulation, statistics, and logic modeling. The three other types of DSS have become more widespread and sophisticated because of Web technologies. Communication-driven DSS rely on electronic communication technologies to link multiple decision makers who might be separated in space or time or to link decision makers with relevant information and tools. The Web has expanded this technology. Knowledgedriven DSS can suggest or recommend actions to managers. The Web helps deliver this type of DSS to a much broader audience of decision makers. Finally, document-driven DSS integrate a variety of storage and processing technologies to provide managers document retrieval and analysis. Our primary focus in this status report and discussion is on the first two categories of Decision Support Systems: datadriven and model-driven DSS.

Web-based and Web-enabled decision support computation can be architected in various ways [4]. For instance, the entire collection of decision models, algorithms, documents, and data could reside on a single Web server and be accessed via a Web browser; or the DSS could combine components from multiple sources, perhaps <sup>b</sup>on the fly<sup>Q</sup> to deliver applicationspecific solution support. For example, the NEOS optimization service (Czyzyk et al. [16]) provides a collection of optimization algorithms that reside on the NEOS servers, which users can invoke from their own computer by specifying problem-specific information via an interactive problem submission tool.

## 3.1. Decision technologies as services

Bhargava and Krishnan [4] discussed technologies for Web-enablement of model-driven DSS, covering technologies that facilitate use of the Web for communication of decision information and computation, technologies that enable the remote and platform-independent access of DSS, and technologies that allow DSS components to be distributed over the Web. A number of other articles (cf., [15,16,38,43]) have also addressed issues associated with Web-enabling DSS. In particular, Fraternali [22] discussed technologies for developing Web-enabled data-intensive applications. Coddington et al. [14] discussed Web technologies in the context of DSS based on geographic information systems tools. Fourer and Goux [21] discussed the concept of optimization as an Internet service and reviewed various alternative ways of delivering such computation. Sridhar [51] emphasized decision support using a company intranet.

As discussed in Bhargava and Krishnan [4], Web technologies can be classified in terms of those technologies that enable (1) server-side computation, (2) client-side computation, and (3) a distributed implementation and deployment of DSS components. Server-side computation facilitates platform-independent and universal access to decision support applications. Relevant technologies include CGI, Java applications, server-side scripting languages, Active Server pages, PHP, and Java server pages. Those technologies enabling client-side computation that allow more capabilities to be embedded in the user interface include client-side scripting languages, Java applets, ActiveX controls, and browser plugins. Finally, those technologies enabling a distributed implementation and deployment of DSS components include CORBA, COM+, Java RMI, and Enterprise Java Beans. Together, these computing technologies create many possibilities for changing the way decision support systems are developed, deployed, and used. More recent technological developments relevant to DSS computation include Web services and messaging protocols such as SOAP, and several XML-related languages and applications for data interchange.

## 3.2. Web technologies and decision support tasks

To understand how Web technologies can influence the development, deployment, and use of Decision Support Systems, we have examined the major tasks at various stages of using and building data- and model-driven DSS. Web technologies are making it possible to perform all of these tasks using a remote Web client. In thinking of such tasks, it is useful to recall the distinction made by Sprague [50] about application-specific DSS that consist of user interface, data, and models for a specific decision problem and DSS generators that provide tools and algorithms for building a variety of specific DSS. Application-specific DSS are far easier to build, but rarely reusable; DSS generators are far more complex to build but can be adapted to build many specific systems (cf., [10]).

Fig. 1 summarizes the relationships among 10 major tasks involved in building and using data- and model-driven DSS. For example, a user of an application-specific, model-driven DSS would have access to relevant decision models and data, and would then focus on tasks such as model execution, development of reports, or analysis. Using a corresponding DSS generator, on the other hand, would require the performance of additional tasks such as model definition and creation of a custom user interface. Building model-driven DSS often involves completing all of the tasks in the model rows as well as the tasks in the data-driven DSS rows. Similarly, using a DSS gene rator involves the tasks listed in the DSS generator column as well as those tasks for building an application-specific DSS. The 10 distinct DSS-related tasks that can be executed by users from a Web browser include model instantiation, model execution, creation of analyses and reports, data visualization, query and retrieval, data analysis, model definition, data definition, analysis definition, and user interface definition (see, e.g., [10] for more details about these tasks). From a browser, one can create decision support capabilities for other users or use predefined capabilities for a specific analysis.

<table><tr><td>Tasks for Model-driven only</td><td>Model instantiationModel executionAnalysis and reports</td><td>Model definitionAnalysis definitionUser Interface definition</td></tr><tr><td>Tasks for both Data-driven and Model-driven</td><td>Data visualizationQuery and retrievalData analysis</td><td>Data definitionAnalysis definitionUser Interface definition</td></tr><tr><td></td><td>Tasks for both Application-specific and DSS Generator</td><td>Tasks for DSS Generator Only</td></tr></table>

Fig. 1. Working with Decision Support Systems: common tasks.

## 4. Web-enabled decision support

A useful framework for thinking about ways in which decision support can exploit the Web is the twin perspectives of <sup>b</sup>Web as media<sup>Q</sup> and <sup>b</sup>Web as computer<sup>Q</sup> (Bhargava and Krishnan [4]). This section offers an informal and example-driven tour of the extent to which decision support products have applied these perspectives in <sup>b</sup>Web-enabling<sup>Q</sup> the decision support related tasks discussed in the previous section. Table 1 summarizes the state of practice in these categories. There is much opportunity for imagination and future development, but a few important beneficial uses of these capabilities stand out and the next two sections briefly review recent developments. All of the Web addresses (Uniform Resource Locators) for cited Web sites are included in the Appendix.

## 4.1. Web as media

The Web has facilitated the creation of a number of industry-wide DSS Information Portals (cf., [42,44]). For example, DSSResources.com, the OLAP Report, and DataWarehousing Online are industry-wide decision support portals that offer information about software products, vendors, methodologies, and white papers in the context of decision support technologies. Teradata University Network is a vendor supported teaching and learning resource related to data warehousing, DSS/Business Intelligence, and database classes. IBM’s COIN initiative and e-optimization. com offer similar portals for optimization. InfoHarvest and the Decision Analysis Society have created portals related to decision analysis.

Table 1  
State-of-practice for data and model-driven DSS

<table><tr><td></td><td>OLAP/Data warehousing</td><td>Data mining</td><td>Decision analysis</td><td>Multi-criteria DM</td><td>Optimization</td><td>Simulation</td></tr><tr><td>Industry portal</td><td>OLAP ReportDW OnlineDSS Resources</td><td></td><td>DAS</td><td>InfoHarvest</td><td>e-Opt.IBM OSS</td><td></td></tr><tr><td>Company/product information</td><td>Dimensional InsightHyperionTeradata</td><td>IBMTeradata</td><td>Aliah</td><td>Expert ChoiceInfo Harvest</td><td>iLogCPlex</td><td>DecisioneeringBizLand</td></tr><tr><td>Sales and downloads</td><td>Cognos</td><td></td><td>TreeageLumina</td><td></td><td>Frontline</td><td></td></tr><tr><td>Demo and trial-run</td><td>CognosDatabeaconMicrostrategy</td><td></td><td>TreeAgeHDS</td><td></td><td></td><td>BizLandDecisioneering</td></tr><tr><td>Vertical applications</td><td>Midway Airline</td><td></td><td>CowCulling</td><td>Personalogic</td><td>Grazing SystemsoptAmaze</td><td></td></tr><tr><td>Vertical app generator</td><td>Dimensional Insight</td><td></td><td>TreeageLumina</td><td></td><td></td><td></td></tr></table>

Individual firms have used Web technologies to communicate information about their decision support products and methods or allow users to conduct various tasks like ordering, payment, or Internet delivery related to purchasing DSS products. In the context of using the Web for <sup>b</sup>providing company and product information,<sup>Q</sup> there is substantial activity across all categories of Decision Support Systems.

DSS firms may also use the <sup>b</sup>Web as media<sup>Q</sup> capabilities to engage in electronic retailing, that is completing the order fulfillment and payment phases over the Web, and distributing DSS products as downloadable software. In the area of data-driven DSS, most vendors appear to make substantial use of Web technologies for disseminating company and product information, and in supporting the product sales functions. In the case of model-driven DSS, however, there is a surprising lack of activity in the area of Web-enabled sales. Few companies offer order placement and payment over the Web; fewer still allow buyers to download decision support software over the Web rather than wait for a package to arrive in the mail (this limitation may be explained by the size and complexity of the software).

## 4.2. Web as computer

The Web can be conceptualized as a vast, distributing computing capability. The <sup>b</sup>Web as computer<sup>Q</sup> decision support capabilities fit in three broad categories:

digital product demonstrations, previewing a decision support product using online interactive examples, and on-line, Web-based Decision Support Systems.

The first category, product demonstrations, represents a baseline for the use of the Web’s capabilities for remote computation. Online demonstrations can be delivered as animated multimedia documents (e.g., QuickTime movies or Shockwave animation) that require or allow little user interaction. As a next step, online interactive examples allow users to interact (e.g., by setting parameter values, or choosing which command to execute next, or designing the format of a report) with the DSS tool in the context of a specific example. Both of these methods allow DSS developers to advertise their features to potential buyers and can be developed with relatively little expertise in developing Web-enabled computation.

There is substantial exploitation of these capabilities in the category of data-driven DSS. For example, MicroStrategy offers both self-running and interactive demonstrations of its business intelligence and data warehousing software. Surprisingly, however, very few vendors of model-driven DSS exploit these capabilities. Most company Web sites do not go much beyond mentioning DSS products; very few provide online demonstrations or interactive examples. Oddly enough, the few firms (notably Lumina and TreeAge, both makers of decision analysis software) that offered Web-based interactive examples a few years ago, now do not. An illustration of the Web’s potential in this regard is <sup>b</sup>Health Decision Strategies<sup>Q</sup> which offers a series of interactive examples that demonstrate its decision support tools.

The next step in the use of the <sup>b</sup>Web as computer<sup>Q</sup> capabilities is to offer application-specific DSS to users that have decision problems within the supported categories. OptAmaze.com provided paper trim optimization and transportation optimization services to paper mills. Grazing Systems Limited offered decision support services in the agricultural sector. More generally, some firms offer decision support applications under the <sup>b</sup>application service provider<sup>Q</sup> architecture, where a server firm hosts the decision support software and offers access to various client firms. The value of ASP deployment of DSS may be appreciated by considering the difficulties that user firms would have in installing, maintaining, and applying complex DSS tools on their own; Web-based and Web-enabled DSS allow such firms to use decision support tools without encountering these difficulties.

For DSS developers, the big leap forward in the use of <sup>b</sup>Web as computer<sup>Q</sup> capabilities is to develop off-the-shelf products that could generate Web-based application-specific DSS of the sort described above. Very few vendors have yet developed this expertise. Exceptions include Lumina and TreeAge. Lumina, which sells a desktop DSS generator based on influence diagram techniques (Analytica), also offers the Analytica Decision Engine that allows developers to produce Web-based DSS applications. TreeAge Software sells DATA Interactive, a version of its DSS development products that enables development of Internet-based decision tree applications. Web-HIPRE is a Web-based DSS for decision analytic problem structuring, multicriteria evaluation and prioritization. Table 1 summarizes example Websites related to the current state-of-practice. The examples are categorized by the decision technology and the Web capability provided.

## 5. Recent research in Web-based decision support

This section reviews and summarizes the state of Web-based DSS research in two areas: (a) architectures and technologies and (b) applications and implementations. A number of articles have reviewed more specific topics related to Web-based DSS. For example, Kuljis and Paul [33] reviewed Web-based simulation and Kersten and Noronba [30] reviewed Webbased negotiation support.

## 5.1. Architectures and technologies

A number of articles discuss architectural issues, frameworks, usability, and other technology topics that are generally applicable to Web-based DSS. Gregg et al. [24] developed a DSS metadata model for distributing decision support systems on the Web. They examined an end users’ ability to find appropriate resources on the Web and determine their suitability. The authors conducted an experiment and reported that a metadata model helps end users locate and understand a specific DSS capability on the Web.

Bharati and Chaudhury [3] conducted an empirical study to investigate customers’ satisfaction with a Web-based decision support system. In their conceptual model, they proposed three independent variables (system quality, information quality, and information presentation) that influenced end users’ satisfaction (dependent variable). They reported that system quality and information quality were positively correlated to end users’ satisfaction, but information presentation did not have a statistically significant impact on an end users’ satisfaction. Therefore, Bharat and Chaudhury argued that developers of a Web-based DSS should pay more attention to system quality (e.g., ease of use, convenience of access, and system reliability) and information quality (e.g., relevance, accuracy, completeness, and timeliness) than to information presentation.

Iyer et al. [28] studied model management for decision support in a computing environment where enterprise data and models are distributed. They identified knowledge layers for model management and proposed a preliminary architecture for a virtual business environment (VBE) that can support management of distributed models.

Gu¨ntzer et al. [25] proposed Structured Service Models that use a variant of structured modeling. This proposed approach can help users find information resources available as an online service within an Intranet. Since the process of computing similarity between two models creates a heavy computational burden, the authors proposed a heuristic approach and reported its performance from computational tests.

Zhang and Goddard [55] applied Software Architectures to the design of Web-based DSS. A layered software architecture was proposed to help developers design and implement a DSS in a distributed environment, and this architecture can provide a formal and hierarchical view of the DSS that helps clarify the design of a Web-based DSS. In addition, the authors presented a component-based framework, 3CoFramework, to assist the implementation of the DSS. Finally, an ongoing Web-based DSS, National Agricultural Decision Support System (NADSS), was presented to illustrate the applicability of the layered software architecture and 3CoFramework.

Mitra and Valente [35] provided an overview of Web-based optimization for model-driven decision support, discussed two paradigms (ASP and e-Services), and articulated technology issues for an e-Services model. To demonstrate and compare two general paradigms for Web-based optimization, the authors discussed <sup>b</sup>Optimization Service Provider (OSP)<sup>Q</sup> and <sup>b</sup>WEBPOT<sup>Q</sup> and demonstrated new benefits enabled by e-Service implementation. Some of these benefits include service discovery, service management, and quality management.

To summarize, these studies discuss metadata, model management, and usability for Web-based DSS. In addition, Mitra and Valente demonstrated that Web-based DSS can effectively incorporate optimization models and tools. These efforts to address the fundamental issues in Web-based computation are essential cornerstones for practical use of Web-based decision support. Past research indicates that (a) Web users need detailed information about DSS to organize and understand the available content, (b) systems should be designed to include constructs and artifacts that support delivery of high-quality information, and (c) new approaches for model management are needed that facilitate storage, search, retrieval, matching, and composition from a library of decision models. Research advances in these areas will be critical to the development of general guidelines and capabilities for building effective Web-based DSS.

## 5.2. Applications and implementations

Many researchers and vendors have reported Webbased DSS case studies and the development of prototype applications. Kohli et al. [32] reported a case study of a Web-based DSS for hospital management called Physician Profiling System (PPS). PPS is a Customer Relationship Management (CRM) system for physician relationship management. The authors demonstrated the development of PPS and presented a cost–benefit analysis of the project. According to their high-level analysis that excluded intangible benefits, they found that breakeven for the project occurred in about 2 months.

Ngai and Wat [37] developed and implemented a Web-based DSS that used a model based on fuzzy set theory to perform risk analysis for e-commerce development. The prototype helped project managers identify, analyze, and prioritize risk involved in an ecommerce development. In their prototype, the Web browser served as the user interface component and all models and databases were hosted at the server.

Dong et al. [20] developed a Web-based DSS framework for portfolio selection. They used Online Analytical Processing (OLAP) and a Parallel Virtual Machine (PVM) to improve the overall performance of their prototype Web-based Portfolio Selection System (WPSS). Because the Web browser is the user interface component and the server contains all the models and databases, the prototype enables multiple computers to handle a large-scale decision support problem efficiently.

Sundarraj [53] identified key issues in managing service contracts and developed a prototype that can support a manager’s planning process. The most important benefit of the prototype is standardization of the management of service contracts because the Web-based system enables many managers to access and use a single system.

Ray [46] reported a case study that demonstrates the implementation of Web-based decision support technologies. He discussed a specific application developed for the Delaware Department of Transportation (DelDOT). The system utilized network optimization tools and a Spatial Decision Support System to improve the management of oversize/overweight vehicles’ movement. Ray reported that the implementation immediately generated some benefits including reduced permit handling time and increased customer satisfaction.

Liou et al. [34] discussed the development and implementation of a Web-based Group DSS, Team-Spirit. To evaluate the functionality of the system, the authors conducted a series of experimental studies and presented preliminary results of the system’s performance. In addition, the authors presented some important factors for the success of a GDSS’s development and implementation.

Delen et al. [18] developed a Web-based DSS, called Movie Forecast Guru, to help decision makers in the movie industry. To forecast box office receipts, the proposed system adopts an information fusion meta-model that uses the output of a Neural Network, Decision Trees, Ordinal Logistic Regression, and Discriminant analysis. Their exploratory assessment of the system indicated that the users were satisfied with its usability in terms of Information Quality, System Quality, and Usefulness (cf, [17,19]).

There are many additional case studies related to deploying Web-based decision support systems. For example, Sugumaran and Meyer [52] report the development of a Spatial DSS prototype for the City of Columbia, Missouri. The system is a model-driven, Web-based DSS that supports a user’s decision making related to watersheds based on certain environmental criteria; Barton [2] reports a \$3 million project to create a Student Data Mart (SDM) that uses data warehouse technology to improve integration of data and provide higher quality data; Walton [54] reported that E Team deployed their software over the Web immediately following the 9/11 attack for emergency operations support in New York City. The software enabled users to enter their needs into E Team’s ASP servers; Pontz and Power [39] discussed a Web-based, knowledge-driven DSS built for the Pennsylvania Department of Labor and Industry. Insightful staff [27] described a Web-based drug discovery visualization system that can provide centralized data, improve productivity, and provide desktop analysis.

## 6. Conclusions

The practice of building Decision Support Systems can benefit in many ways from the increased availability and growing sophistication of Web technologies. These technologies provide platform-independent, remote, and distributed computation and the exchange of complex multimedia information. System maintenance is simplified and centralized, letting end users focus on problem analysis and decision making.

While there is significant promise in the idea of Web-based Decision Support Systems, there are also some important challenges that must be overcome. We need to resolve technological, economic, and social and behavioral challenges to realize the benefits the Web can provide as a platform for building Decision Support Systems.

## 6.1. Technological challenges

The technologies and protocols underlying Web computation create major challenges. First, the basic Web architectural model was designed for random jumps in hyperspace, hence the Web does not provide for persistent connections or persistence of state. This design is quite unlike the typical interaction found in traditional decision support applications. DSS generally require repeated interactions with a model and the exchange of large amounts of data spread across multiple interactions. Therefore, DSS developers must find ways around these limitations by setting cookies or embedding models or data within a Web page or by using a Java applet. Second, most of the implementations, if not all, use the Web browser to deliver a user interface and one or more servers execute queries to databases and execute models. This approach must confront limitations of the Web browser as a user interface, statelessness of the HTTP protocol, round-trip network delays when users interact with DSS inputs and output representations, and the <sup>b</sup>pull<sup>Q</sup> nature (i.e., a request is needed) in traditional client–server Web-based computation. Further research is needed to determine guidelines for the use of alternative technologies for Web-based computation and to understand what technologies may be most effective for different aspects of Web-based decision support.

## 6.2. Economic challenges

To offer decision support as a service, providers must experiment with new payment models. Few providers have found ways to sell information goods, such as news, community information, and music for profit, and the same challenge holds true for decision support services. Bhargava et al. [9] discuss some of the challenges in engaging in electronic commerce for decision support services. Only a few firms offering decision computation applications have well-defined revenue models. optAmaze.- com used a subscription-based model for its trim optimization service, charging differential prices based on the number of machines optimized. Another example is salesforce.com that provides Web-based Customer Relationship Management (CRM) tools. Salesforce.com enables subscribers to enter their sales data using an Internet browser and share the data and analysis with other authorized users. Although the application can support up to 5 users at a fixed price per year, large-scale implementations using a pricing scheme based upon the number of users are also available. This type of pricing scheme seems attractive for Web-based DSS because the burden upon servers and other resources is often dependent on the number of users.

## 6.3. Social and behavioral challenges

Decision support applications have historically been designed for industrial and organizational users, who are typically repeat users with a professional interest in using the application. The Web enables the development of DSS for casual, infrequent users, including consumers, but it is not clear that the cognitive and user interfaces that work for professional users will work as well for them. It remains to be seen, also, whether business DSS users are willing to cede control of internal corporate data and models and host their DSS with an application service provider.

Addressing these challenges may require DSS researchers to move their focus beyond traditional DSS implementation issues. More controlled laboratory studies seem warranted that focus on adoption, utilization and performance. Researchers need to learn more about increasing the satisfaction of non-managerial DSS users, such as business customers and suppliers. The Web has caused us to rethink our assumptions about supporting decision making, but we need to empirically test some of the new assumptions that have been adopted. For example, we assume that hyperlinks facilitate use of a DSS and that Web decision technologies require little training because everyone is familiar with the Web interface. We need to determine if these and other related assumptions are correct.

While modern communication technologies have made Web-based decision support computation feasible, the same technologies have made integration of business computing applications a pressing need. Stand-alone decision support systems are becoming much less useful; their data inflows and outflows need to be integrated into the overall organizational computing architecture. Integration is a major challenge in the context of Web-based decision computation, especially if the computation servers are external to the organization. Lack of such integration can be a significant inhibitor to adoption of the decision support technologies, Web-based or otherwise.

Appendix A. Web addresses of cited Websites

<table><tr><td>Site name</td><td>Uniform Resource Locator</td></tr><tr><td>Aliah</td><td>http://www.decisioncoaches.com/home.html</td></tr><tr><td>BizLand</td><td>http://www.bizland.com/bizland/index.bml</td></tr><tr><td>Cognos</td><td>http://www.cognos.com</td></tr><tr><td>Cow Culling</td><td>http://ag.arizona.edu/AREC/cull/culling.html</td></tr><tr><td>Databeacon</td><td>http://www.storydata.com</td></tr><tr><td>DataWarehousing Online</td><td>http://www.datawarehousingonline.com</td></tr><tr><td>Decision Analysis Society (DAS)</td><td>http://faculty.fuqua.duke.edu/daweb/</td></tr><tr><td>Decisioneering</td><td>http://www.decisioneering.com/</td></tr><tr><td>Dimensional Insight</td><td>http://www dimensionalinsight.com/</td></tr><tr><td>DSSResources.com</td><td>http://www.DSSResources.com</td></tr><tr><td>e-optimization.com</td><td>http://www.e-optimization.com/</td></tr><tr><td>Expert Choice</td><td>http://www.expertchoice.com/</td></tr><tr><td>Frontline Systems</td><td>http://solver.com/</td></tr><tr><td>Grazing Systems</td><td>http://www.grazingsystems.co.nz/model.cfm</td></tr><tr><td>Health Decision Strategies (HDS)</td><td>http://www.healthstrategy.com/objectiv.htm</td></tr><tr><td>Hyperion</td><td>http://www.hyperion.com/</td></tr><tr><td>IBM OSS COIN</td><td>http://oss.software.ibm.com/developerworks/opensource/coin</td></tr><tr><td>iLog</td><td>http://www.iloc.com/</td></tr><tr><td>InfoHarvest</td><td>http://www.infoharvest.com/ihroot/index.asp</td></tr><tr><td>Lumina</td><td>http://www.lumina.com/adedemo/index.htm</td></tr><tr><td>MicroStrategy</td><td>http://www.microstrategy.com</td></tr><tr><td>Personalogic</td><td>http://personalogic.com</td></tr><tr><td>Salesforce.com</td><td>http://salesforce.com</td></tr><tr><td>Teradata</td><td>http://teradata.com</td></tr><tr><td>Teradata University Network</td><td>http://www.teradatauniversitynetwork.com</td></tr><tr><td>The OLAP Report</td><td>http://www.olapreport.com/index.htm</td></tr><tr><td>TreeAge</td><td>http://www.treeage.com/</td></tr><tr><td>Web-HIPRE</td><td>http://www.hipre.hut.fi/WebHipre/</td></tr></table>

## References

[1] S. Ba, Kalakota, A.B. Whinston, Executable documents DSS, Proceedings of 3rd International Conference on DSS, Hong Kong, 22–23 June, 1995.

[2] P. Barton, The George Washington University Data-Driven Decision Support Project, URL DSSResources.COM (2003).

[3] P. Bharati, A. Chaudhury, An empirical investigation of decision-making satisfaction in Web-based decision support systems, Decision Support Systems 37 (2) (2004) 187–197.

[4] H.K. Bhargava, R. Krishnan, The World Wide Web: opportunities for operations research and management science, INFORMS Journal on Computing 10 (1998 (Fall)) 359–383.

[5] H.K. Bhargava, D.J. Power, Decision support systems and Web technologies: a status report, Proceedings of the 2001 Americas Conference on Information Systems, Boston, MA, August 3–5, 2001.

[6] H.K. Bhargava, A. King, D. McQuay, DecisionNet: an architecture for modeling and decision support over the World Wide Web, Proceedings of 3rd International Conference on DSS, Hong Kong, 22–23 June, 1995.

[7] H.K. Bhargava, R. Krishnan, D. Kaplan, On generalized access to a WWW-based network of decision support services, Proceedings of 3rd International Conference on DSS, Hong Kong, 22–23 June, 1995.

[8] H.K. Bhargava, R. Krishnan, R. Mu¨ller, Decision support on demand: emerging electronic markets for decision technologies, Decision Support Systems 19 (1997) 193– 214.

[9] H.K. Bhargava, R. Krishnan, R. Mu¨ller, Electronic commerce in decision technologies: a business cycle analysis, International Journal of Electronic Commerce 1 (1997) 109–127.

[10] H.K. Bhargava, C.L. Herrick, S. Sridhar, Beyond spreadsheets: software for building decision support systems, IEEE Computer 32 (1999 (March)) 31 – 39.

[11] T. Berners-Lee, R. Cailliau, A. Luotonen, H.F. Nielsen, A. Secret, The World Wide Web, Communications of the ACM 37 (8) (1994) 76–82.

[12] T.X. Bui, Decision support in the future tense, Decision Support Systems 19 (3) (1997 (March)) 149 – 150.

[13] K. Chang, A. Dasari, H. Madduri, A. Mendoza, J. Mims, Design of an enablement process for on demand applications, IBM Systems Journal 43 (2004) 190–203.

[14] P.D. Coddington, K.A. Hawick, H.A. James, Web-based access to distributed high-performance geographic information systems for decision support, Proceedings of the 32nd Hawaii International Conference on System Sciences, January 1999.

[15] M. Cohen, C.B. Kelly, A.L. Medaglia, Decision support with Web-enabled software, Interfaces 31 (2001) 109 – 129.

[16] J. Czyzyk, J. Owen, S.J. Wright, Optimization on the Internet, OR/MS Today 24 (1997) 48– 51.

[17] F.D. Davis, Perceived usefulness, perceived ease of use, and user acceptance of information technology, MIS Quarterly 13 (3) (1989) 319– 340.

[18] D. Delen, R. Sharda, P. Kumar, Movie forecast guru: a Webbased DSS for hollywood managers, Decision Support Systems 43 (2007) 1151– 1170 (this issue), doi:10.1016/ j.dss.2005.07.005.

[19] W.H. DeLone, E.R. McLean, Information systems success: the quest for the dependent variable, Information Systems Research 3 (1) (1992) 60– 95.

[20] J. Dong, H.S. Du, S. Wang, K. Chen, X. Deng, A framework of Web-based decision support systems for portfolio selection with OLAP and PVM, Decision Support Systems 3 (2004) 367– 376.

[21] R. Fourer, J. Goux, Optimization as an Internet resource, Interfaces 31 (2001) 130– 150.

[22] P. Fraternali, Tools and approaches for developing data-intensive Web applications: a survey, ACM Computing Survey 31 (1999) 227– 263.

[23] M. Goul, A. Philippakis, M. Kiang, D. Fernandes, B. Otondo, Towards a client/server open-DSS protocol suite for automating DSS deployment on the World Wide Web, Proceedings of 3rd International Conference on DSS, Hong Kong, 22–23 June, 1995.

[24] D.G. Gregg, M. Goul, A. Philippakis, Distributing decision support systems on the WWW: the verification of a DSS metadata model, Decision Support Systems 32 (2002) 233– 245.

[25] U. Gu¨ ntzer, R. Mu¨ ller, S. Mu¨ ller, R.D. Schimkat, Retrieval for decision support resources by structured models, Decision Support Systems 43 (2007) 1117–1132 (this issue), doi:10.1016/j.dss.2005.07.004.

[26] C. Holsapple, A. Whinston, Exploring the next generation of decision support, Decision Support Systems 14 (3) (1995 (July)) 185– 186.

[27] Insightful Staff, Merck Deploys Web-Based Drug Discovery Visualization System, URL DSSResources.COM (February 2002).

[28] B. Iyer, G. Shankaranarayanan, M.L. Lenard, Model management decision environment: a Web service prototype for spreadsheet models, Decision Support Systems 40 (2) (2005 (August)) 283 – 304.

[29] M.A. Jeusfeld, T.X. Bui, Decision support components on the Internet, Proceedings of 3rd International Conference on DSS, Hong Kong, 22–23 June, 1995.

[30] G.E. Kersten, S.J. Noronba, WWW-based negotiation support design, implementation, and use, Decision Support Systems 25 (2) (1999 (March)) 135– 154.

[31] M. Klein, L.B. Methlie, Knowledge-Based Decision Support Systems with Applications in Business, John Wiley & Sons, Chichester, 1995.

[32] R. Kohli, F. Piontek, T. Ellington, T. VanOsdol, M. Shepard, G. Brazel, Managing customer relationships through E-business decision support applications: a case of hospital–physician collaboration, Decision Support Systems 32 (2001) 171– 187.

[33] J. Kuljis, R.J. Paul, An appraisal of Web-based simulation: whether we wander? Simulation Practice and Theory 9 (2001) 37– 54.

[34] Y. Liou, M. Chen, C.W. Wang, Y.W. Fan, Y.P.J. Chi, Team-Spirit: design, implementation, and evaluation of a Web-based group Decision Support System, Decision Support Systems 43 (2007) 1186–1202 (this issue), doi:10.1016/j.dss.2005.07.008.

[35] G. Mitra, P. Valente, The evolution of Web-based optimisation from ASP to e-services, Decision Support Systems 43 (2007) 1096– 1116 (this issue), doi:10.1016/j.dss.2005.07.003.

[36] V.K. Naik, A. Mohindra, D.F. Bantz, An architecture for the coordination of system management services, IBM Systems Journal 43 (2004) 78– 96.

[37] E.W.T. Ngai, F.K.T. Wat, Fuzzy decision support system for risk analysis in e-commerce development, Decision Support Systems 40 (2) (2005 (August)) 235 – 255.

[38] D. O’Leary, Internet-based information and retrieval systems, Decision Support Systems 27 (3) (1999 (December)) 319–327.

[39] C. Pontz, D.J. Power, Building an Expert Assistance System for Examiners (EASE) at the Pennsylvania Department of Labor and Industry, URL DSSResources.COM (2002).

[40] R. Powell, DM Review: a 10 Year Journey, DM Review, URL http://www.dmreview.com (2001 (February)).

[41] D.J. Power, Web-based Decision Support Systems, DSstar, The On-Line Executive Journal for Data-Intensive Decision Support 2 (1998).

[42] D.J. Power, Finding DSS Resources on the World-Wide Web, Journal of Decision Systems 7 (1998) 7 – 20.

[43] D.J. Power, Web-based and model-driven decision support systems: concepts and issues, Proceedings of the Americas Conference on Information Systems (AMCIS 2000), Long Beach, California, 10–13 August 2000.

[44] D.J. Power, Decision Support Systems: Concepts and Resources for Managers, Greenwood/Quorum Books, Westport, CT, 2002.

[45] D.J. Power, Specifying an expanded framework for classifying and describing Decision Support Systems, Communications of the Association for Information Systems 13 (13) (2004) 158–166.

[46] J.J. Ray, A Web-based spatial Decision Support System optimizes routes for oversize/overweight vehicles in Delaware, Decision Support Systems 43 (2007) 1171–1185 (this issue), doi:10.1016/j.dss.2005.07.007.

[47] J.W. Ross, G. Westerman, Preparing for utility computing: the role of IT architecture and relationship management, IBM Systems Journal 43 (2004) 5 –19.

[48] M.S. Scott Morton, Management decision systems; computerbased support for decision making, Graduate School of Business Administration, Harvard University, 1971.

[49] J.P. Shim, M. Warkentin, J.F. Courtney, D.J. Power, R. Sharda, C. Carlsson, Past, present, and future of decision support technology, Decision Support Systems, Special Issue, DSS: Directions for the Next Decade 33 (2) (2002) 111 –126.

[50] R. Sprague, A framework for the development of Decision Support Systems, MIS Quarterly 2 (1980) 1– 26.

[51] S. Sridhar, Decision support using the intranet, Decision Sup port Systems 23 (1) (1998 (May)) 19–28.

[52] R. Sugumaran, J. Meyer, Building a Web-Based Spatial Deci sion Support System (WEBSDSS) for Environmental Planning and Management, URL DSSResources.COM (2003).

[53] R.P. Sundarraj, A Web-based AHP approach to standardize the process of managing service-contracts, Decision Support Systems 3 (2004) 343– 365.

[54] M.S. Walton, Rebuilding an Emergency Operations Center for NYC following 9/11, URL DSSResources.COM (2003).

[55] S. Zhang, S. Goddard, A software architecture and framework for Web-based distributed decision systems, Decision Support Systems 43 (2007) 1133– 1150 (this issue), doi:10.1016/ j.dss.2005.06.001.

Dr. Hemant K. Bhargava joined the Graduate School of Management at the University of California, Davis, as a Professor of Information Systems and Management in Summer 2003. Prior to this, he was a Professor at Penn State University’s Smeal College of Business Administration, after starting his academic career at the Naval Postgraduate School in Monterey. Dr. Bhargava’s work has appeared in several scientific journals including INFORMS Journal on Computing, Journal of Management Information Systems, IEEE Computer, Decision Support Systems, and Interfaces. His research on DecisionNet won Best Paper Awards at leading Information Systems conferences. Dr. Bhargava was awarded the Menneken Prize for Excellence in Research at the Naval Postgraduate School in 1998.

![](/api/attachments/DUJGDSGB/fulltext/images/5e0838b2446a42f0ccdeb71f0121b4e381926184704030323dbee14be8c856be.jpg)

Daniel J. Power is a Professor of Information Systems and Management at the College of Business Administration at the University of Northern Iowa, Cedar Falls, Iowa and the editor of DSSResources.- COM, the Web-based knowledge repository about computerized systems that support decision making, and the editor of DSS News, a biweekly e-newsletter. Dan writes the column <sup>b</sup>Ask Dan!<sup>Q</sup> in DSS News.

Since 1982, Professor Power has published more than 40 articles, book chapters and proceedings papers. His articles have appeared in leading journals including Decision Sciences, Decision Support Systems, Journal of Decision Systems, and MIS Quarterly. He is also co-author of a book titled Strategic Management Skills and he has authored two books on Decision Support Systems. His DSS Concepts book (2002) is a broad ranging handbook on the fundamentals of building decision support systems. His DSS FAQ(2005) organizes important Ask Dan! Questions (with answers) published in DSS News from 2000 through 2004. Professor Power was founding Chair of the Association for Information Systems Special Interest Group on Decision Support, Knowledge and Data Management Systems (SIG DSS). In 1982, Professor Power received a PhD in Business Administration from the University of Wisconsin–Madison. He was on the faculty at the University of Maryland–College Park from 1982 to 1989. Power served as the Head of the Management Department at the University of Northern Iowa (UNI) until January 1996. He then served as Acting Dean of the UNI College of Business Administration until July 31, 1996. In Summer 2003, he was a Visiting Faculty Research Fellow with the U.S. Air Force Research Lab Information Directorate (AFRL/IF). Dr. Power is a pioneer developer of computerized decision aiding and support systems. During 1975–77, he developed a computerized system called DECAID, DECision AID. In 1981–83, he reprogrammed and expanded the system for the Apple II PC. In 1986–87, he designed a set of decision aiding tools for the Management Decision Assistant package from Southwestern Publishing.

![](/api/attachments/DUJGDSGB/fulltext/images/6dedbaeb411eecb545d338dc7c86e5e4413e963871e0b4de5730d94de82638d3.jpg)

Daewon Sun is an Assistant Professor of Management Information Systems in the Mendoza College of Business at University of Notre Dame. He holds a PhD in Management Science and Information Systems from the Pennsylvania State University, an MBA from Bowling Green State University, and Bachelor of Business Administration from Korea University, Seoul, Korea. His primary research interests are in Economics of

Information Systems, including Pricing Strategies and Resource Management, Contingency Pricing Strategies for Internet Networking, Decision Support techniques, and Pricing Strategies for Online Retailers. He has published papers in Decision Support Systems, INFORMS Journal on Computing, and Naval Research Logistics.
