---
otero_id: 5936
otero_key: "U296PRKP"
title: "A metadatabase-enabled executive information system (Part A): A flexible and adaptable architecture"
authors: "Waiman Cheung; Gilbert Babin"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.01.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A metadatabase-enabled executive information system (Part A): A flexible and adaptable architecture

Waiman Cheung <sup>a,⁎</sup>, Gilbert Babin

Department of Decision Sciences and Managerial Economics, The Chinese University of Hong Kong, Shatin, Hong Kong <sup>b</sup> Service d'enseignement des technologies de l'information, HEC Montréal, 3000, chemin de la Côte-Sainte-Catherine, Montréal, Québec, Canada H3T 2A7

Received 16 November 2004; received in revised form 15 January 2006; accepted 25 January 2006 Available online 11 April 2006

## Abstract

Executive information systems (EIS) that are capable of accessing multiple data sources (both online and offline) for ondemand, ad hoc analysis are needed to support the changing needs of corporate executives. A major shortcoming of existing EISs is that their database schema and data content are predetermined, fixed, and hard-coded, which leads to predefined data analysis patterns. In this paper, we propose a new EIS architecture that takes advantage of a knowledge-based mechanism known as the Metadatabase. The architecture enables executives to discover new informational structures, such as critical successful factors and perspectives from which to analyze these factors, that are useful for the analysis of an enterprise's business performance. The novel and on-demand data analysis needs of executives are supported by the online capability of the new EIS architecture, and we argue that the new architecture has better system flexibility and adaptability compared to existing EISs. © 2006 Elsevier B.V. All rights reserved.

Keywords: Executive information systems; Systems integration; Metadatabase management system; Data warehouse; Online analytical processing

## 1. Introduction

Typical business processes involve both internal data exchanges and exchanges with external business partners, typically through the Internet or Web-based systems. A process often generates a vast amount of transaction data for internal systems, and to analyze and make good use of this information before the data become irrelevant is crucial to business success. In particular, such data will support senior executives in their decision-making processes at the tactical and strategic levels. In a dynamic business environment, the information that is needed to support such decisions changes constantly, and dedicated staff are often employed in the information systems department to prepare and customize the different reports that are requested by executives. However, producing these customized reports is time consuming, and often only a small proportion of such reports is delivered on time. Even the reports that are delivered may not be exactly what the executives want due to miscommunication or unclear specifications [2]. Therefore, it is a vital requirement to be able to deliver timely and accurate business intelligence from internal and external Webbased and non Web-based systems to executives. It follows that the tasks of integrating data from different sources and making it rapidly available to business executives are becoming increasingly important [31]. As specialized information systems that support executives,

Executive Information Systems (EIS) must tackle these issues to bring timely intelligence to executives.

According to Watson et al., “keeping abreast of executives’ changing information needs,” “combining data,” and “identifying initial information requirements” are among the main problems in EIS development [39]. Considering these problems, existing EISs still have much room for improvement. For instance, the quality of the information that is presented by an EIS is a major concern of executives, but EISs often fail to provide ondemand information to accommodate the changing needs of these executives [42]. As executive users become more computer literate, they are likely to request more sophisticated information technology support and, in many cases, take charge of the system development process [1]. Furthermore, as their ability to use computers increases, executives tend to ask for more powerful features in their EISs [22].

Contemporary EISs take advantage of a tailor-made information repository, which is known as a data warehouse, to provide information that is extracted from different sources at setup time. Data warehousing offers good availability and performance, as all of the data come from a single location. However, changes in the original data sources can only be propagated to the data warehouse periodically in a batch manner [31], and the timeliness of data is further affected when these changes involve the structural modification of data sources, as the update process often requires programming work or even structural changes in the data warehouse.

In this paper, we propose a Metadatabase-enabled EIS architecture to support on-demand, interactive, and multidimensional data analysis. Using this new architecture, data can be extracted from multiple internal and external data sources online and subsequently combined. Taking advantage of the Metadatabase (an enterprise knowledge base) [16], the new EIS can easily adapt to both data updates and schematic changes in the data sources.

The paper is organized as follows. Section 2 provides a review of the evolution of EISs, and Section 3 describes the Metadatabase approach that is at the core of the proposed EIS. In Section 4, the new architecture is presented at the conceptual level, and an evaluation of the architecture is provided in Section 5. Some conclusions are presented in Section 6.

## 2. Evolution of EIS architecture

Executive Information Systems (EIS) are specially designed information systems that provide information from internal and external data sources. They enable executives to monitor and track the critical success factors (indicators) of their enterprise using customized presentation formats [5,13,34]. Traditionally, an EIS contains two major components (Fig. 1): a centralized database that stores the data that are extracted from various sources, and an engine for data analysis and the presentation of the results [26,29].

This architecture is easily manageable, and the centralized database allows queries and analyses to be processed quickly. However, the extraction and updating of data from different local sources into the centralized database is a more complex issue, and it is often the case that data from different sources are incompatible. In the traditional EIS architecture, these incompatibilities are manually resolved in an ad hoc manner. A further limitation to the traditional EIS architecture is that it only supports predefined and primitive data analyses, which cannot satisfy all of the analytical needs of executives, which are usually novel and multidimensional. Furthermore, the need for hard coding to resolve data incompatibility makes this architecture inadaptable, and when there is a change in a local data source, the centralized database may need to be repopulated, recompiled, or even redesigned [35– 37].

The difficulties that are associated with the use of traditional EISs have led researchers to study ways to integrate and access data from distributed, heterogeneous data sources and to analyze data in a multidimensional manner [27,38,40].

The introduction of data warehousing technology and Online Analytical Processing (OLAP) techniques has greatly improved traditional EISs [3,8,11,23–25], and has led to a new EIS architecture that is sometimes referred to as contemporary EIS architecture [12,30]. In this architecture, the centralized database is replaced by a data warehouse, and OLAP techniques are adopted for multidimensional data analysis and information presentation [14] (Fig. 2). The data warehousing technology alleviates some of the data integration problems, and requests and feedback are exchanged as messages between modules. A small program, which is known as a monitor or wrapper, is built for each data source, the major role of which is to communicate with the integrator and extract data from the source based on the pre-defined data view. Data from different local data sources are extracted, cleansed, and transformed by an integrator that is based on an integrated data schema, and are subsequently stored in the data warehouse. However, the integrated schema still has to be predetermined, and data are hard-wired to be retrieved and stored [7,28,41,44]. Most commercial data warehouse systems only deal with the propagation of data updates in a reactive and batch mode, if they deal with them at all. Schematic changes and constraint modifications in the data sources can entail a major rebuild of the existing data warehouse, and thus the integration of data from dynamic data sources raises new challenges in the maintenance and evolution of data warehouse systems [31].

![](/api/attachments/U296PRKP/fulltext/images/671a264c2df8f23aa9e3a96b85b1019f9429ab0e3e36dad0911ba6d71a1db167.jpg)  
Fig. 1. A traditional EIS architecture.

The Evolvable View Environment (EVE) project [31,43] is among the first attempts to address the dynamic data source issue. In the EVE, E-SQL is defined and used to describe the preference parameters that are to be attached to elements of a view query to update the data warehouse. If the schema of a source changes and affects the view in the data warehouse, the E-SQL description will be used to rewrite the view definition of the wrapper into a definition that is acceptable to the data warehouse. The project therefore offers a solution to the updating problem in data warehousing when the schema of the data warehouse is fixed and predetermined.

![](/api/attachments/U296PRKP/fulltext/images/e35f9ca7e4dcf7980b9afc34fe033e77c0dc27adeef85aa3c363371d8a557aea.jpg)  
Fig. 2. A contemporary EIS architecture.

Although OLAP techniques support multidimensional data analysis, these techniques operate using a predefined database schema, such as a star schema [32]. At the center of the star schema is an indicator, and branches of the star are dimensions or perspectives (age, location) that can be used to analyze the indicator. The length of a branch corresponds to the number of abstraction levels (office, district, region, country) of the dimension that is to be used for analysis. Data are stored in a proprietary multidimensional database or a relational data warehouse according to this schema. As a consequence, the type of data analysis that can be carried out is restricted.

## 2.1. Contemporary EIS issues

It follows that the contemporary EIS architecture has neither the flexibility nor the adaptability that is most needed by executives. Flexibility refers to the ability to accommodate the changing data analysis needs (information in the form of new indicators, dimensions, and abstraction levels) of executives, whereas adaptability refers to the ability to adapt to any changes in content, data format, platform, and structure that occur in local data sources. Both the data warehousing technology and OLAP techniques rely on a predefined data schema, and therefore can only provide limited flexibility and adaptability without redesign, reprogramming, or repopulation.

Contemporary e-business operations not only generate rich operational data online but also require the capability to analyze these data on demand in a flexible and adaptable manner. In this paper, we propose a new EIS architecture that includes a Metadatabase management system (MDBMS). New methods and algorithms that are based on this architecture can then be developed that take advantage of the metadata that are provided by the MDBMS to support on-demand, interactive, and multidimensional data analysis [9]. The MDBMS is a well known technology for enterprise systems integration that is based on the Metadatabase Approach. Before we introduce the new EIS architecture, we first give an introduction of the Metadatabase Approach in the following section.

## 3. The Metadatabase Approach to enterprise information integration

The Metadatabase Approach is a systems integration method that manages multiple systems and achieves open system architecture while retaining local system autonomy and allowing for the evolution of the system [6,18–20,15,21]. The Metadatabase Approach defines a concurrent architecture (Fig. 3) that consists of a central knowledge base, which is called the Metadatabase, and a number of distributed systems, such as Marketing, Production, and Accounting. The Metadatabase contains a description of the different data sources and how they are integrated and semantically interrelated in the form of mapping rules between systems. Hence, the Metadatabase can be viewed as a repository of the global enterprise model. A software shell (double circle in Fig. 3) is associated with each system, including the Metadatabase, and the role of these shells is to enable interoperability among the distributed data systems.

Systems are integrated at the metadata level instead of using hard-coded data that is stored in a data warehouse. The open nature of the Metadatabase approach provides a highly adaptive environment for systems integration. In particular, changes in local systems are reflected by changes in the metadata, and thus an old system can be removed or a new system added without the modification and recompilation of the integration environment [6,21].

At the operational level, metadata are distributed from the Metadatabase into the local shells and used to customize their operations. It is possible to use a simple and generic shell structure that adapts its behavior according to the metadata that it contains [4,16,33], which means that the number or nature of the systems that are being integrated is immaterial, as long as they are properly modeled at the metadata level. When structural changes occur in local systems, these changes are applied to the central knowledge base (changes are made to the contents of the Metadatabase) and are then propagated to the local shells, which then automatically adjust their behavior to the new structure. The shells have two roles: they serve as interfaces to access local databases, which enables online ad hoc data queries to local systems online, and support the rule-based integration of local systems, which enables predefined data transfers across systems (the population of a data warehouse). The shells differ from wrappers in that their behavior is not hard coded but rule-based, the rules being the metadata that are managed by the Metadatabase.

The Metadatabase provides a detailed description of the local database systems, such as their physical location and implementation and access methods. To manage the metadata, a Metadatabase Management System (MDBMS) was developed. At the heart of the MDBMS is a Global Query System (GQS) [4,10,17,16], which supports metadata-assisted global query formulation and the execution of queries across multiple data sources. In addition to querying local data sources, the GQS is also the main interface for accessing and manipulating the metadata that are stored in the Metadatabase. Using the GQS, a user can formulate complex queries that access multiple data sources without prior knowledge of the underlying data models. The Metadatabase serves as an underlying canvas for the formulation process, and the GQS automatically identifies missing join conditions and completes the global query for the user using the Metadatabase content. Finally, the GQS uses the shells to extract data from local systems.

![](/api/attachments/U296PRKP/fulltext/images/461e1ab9bad887bab0e34356d1591beb337e22fec0e48cc1b8297033925f4478.jpg)  
Fig. 3. Concurrent architecture using the metadatabase approach

## 4. A new architecture for Executive Information Systems

The proposed EIS architecture is shown in Fig. 4. It consists of two major components: the Metadatabase Management System (MDBMS) and the Multidimensional Data Analysis System (MDAS), which includes a ROLAP/MDB Interface and a ROLAP/MDB Analyzer.

Metadata that are contained in the Metadatabase are used to facilitate on-demand multidimensional data analysis. As the Metadatabase approach is adaptive, an existing data warehouse can be incorporated and managed as one of the local data sources by consolidating the data warehouse schema into the global enterprise model. The schema information, including synonyms and constraints, is then populated into the Metadatabase as metadata. Furthermore, rules to populate the data warehouse from other local systems can also be stored as metadata in the Metadatabase for distribution to the local shells of the data sources concerned. In this fashion, changes in the local systems can easily be reflected in the data warehouse, and this same integration approach is used to incorporate any new data source into the Metadatabase.

![](/api/attachments/U296PRKP/fulltext/images/7ee9b7cdf16fb38cb39c3e826befff32c3430924f9449dd5fe007aeab8d8b668.jpg)  
Fig. 4. A new EIS architecture using the metadatabase approach.

The use of the MDBMS simplifies the development of the MDAS, and indeed, the MDAS makes extensive use of the GQS facilities that are provided by the MDBMS. The metadata-based formulation of the GQS reduces the need for the user to have a detailed understanding of the enterprise data model. Another advantage is that the GQS and the local shells provide unified and transparent access to local data sources.

## 4.1. Metadatabase Management System (MDBMS)

The MDBMS has two roles in the proposed architecture. First, it provides transparent access to data from both local systems and the data warehouse. The built-in global query optimization mechanisms of the GQS guarantee that the required data is retrieved from the smallest number of local systems, which means that if the data warehouse contains all of the required data, then no other local system need be accessed.

Second, the MDBMS provides the metadata that are needed for multidimensional data analysis. At the interface level, metadata can be used in a browsing facility for analysis formulation, and at the processing level can be used with various algorithms and methods to generate queries to local systems. These queries are then sent to and processed by local shells.

## 4.2. Multidimensional Data Analysis System (MDAS)

The new features of the architecture, including online analysis formulation and the processing and result presentation for on-demand OLAP, are grouped into two sub-systems: the ROLAP/MDB Interface and the ROLAP/MDB Analyzer. The ROLAP/MDB Interface provides the necessary interface for executives to formulate their requests and for the results of an analysis to be presented. The actual data processing and analysis are carried out within the ROLAP/MDB Analyzer. Both sub-systems rely on the metadata that are provided by the MDBMS. In this paper, we describe the functionalities of these sub-systems, and the methods, algorithms, and associated modules are further developed in [9].

## 4.2.1. ROLAP/MDB Interface

This sub-system manages all of the interactions between the user and the MDAS. First, it enables the selection of indicators from the data that are available in the different data sources that are described in the MDBMS. It then assists the user in the selection of the dimensions that are to be used for a specific analysis. This selection process makes use of the metadata that are available, and suggests only “meaningful” dimensions to the user. To determine the dimensions that are meaningful, the ROLAP/MDB Interface uses the business rules that are implied by the data schema. Second, the sub-system offers multidimensional data analysis functionalities for the performance of the actual data analysis, such as drill-down/roll-up, slice/dice, and rotate operations.

## 4.2.2. ROLAP/MDB Analyzer

The ROLAP/MDB Analyzer is constructed around the notion of the Multidimensional Analysis Unit (MAU). A MAU is a database view that contains an indicator and all of the potential dimensions that can be used to examine that indicator (see [9] for a detailed description of a MAU). Once an indicator has been chosen, an algorithm can be developed to automatically determine its associated MAU based on the enterprise global model that is stored in the Metadatabase. The resulting MAU is actually a database sub-schema, and can be saved locally within the ROLAP/MDB Analyzer for future use.

Once a MAU has been constructed, a global query can then be generated automatically using the GQS. The generated global query can then be decomposed into local queries that are distributed to the local shells of the corresponding data sources. The retrieved data for the MAU view can be further materialized by saving it in a local relational database within the MDAS.

## 5. Evaluation of the new EIS architecture

In this section, we evaluate the new EIS architecture and compare it to the contemporary EIS architecture. In particular, we look at the advancements and new features that the new architecture provides with respect to systems integration and on-demand data analysis capabilities. In addition, we assess the trade-offs in the proposed architecture.

## 5.1. Improvements on the existing EIS architectures

Traditional and contemporary EIS architectures access data from local systems by first determining the indicators and dimensions, and then duplicating them into a centralized database or a data warehouse. This predetermination leads to a fixed and rigid database schema and causes potential redundancies and inconsistencies in the data. This makes systems management a serious burden. We show that the new EIS architecture greatly improves the adaptability and flexibility of EISs, and significantly relieves the burden of systems management.

## 5.1.1. Adaptability

Adaptability is the ability of an EIS to cope with changes in local systems. In increasing order of complexity, these include changes in content (new data that are added to a local system), data format (type, field name, etc.), platform (operating system or DBMS), and structure (adding/removing fields, tables, or local systems). Adaptability can be measured by determining the effort that is required to modify the EIS design and structure to cope with these changes. The less effort that is required, the more adaptable the EIS. Here, we project the effort that is required by analyzing the type of manual activities that would be needed to adjust the EIS. Again, in order of increasing complexity, these activities include population, which involves the loading of new data or metadata into a data repository; compilation, which involves running a schema DDL script or compiling a program source code; programming, which includes syntactic changes such as modifying or writing a DDL or a program source code; and design, which involves logical changes such as modifying or creating a schema or algorithm.

Table 1 shows the manual activities that are required to keep the different EIS architectures abreast of changes in the local systems. We first evaluate the contemporary

Adaptability of EIS architectures

<table><tr><td rowspan="2">Manual activities</td><td colspan="4">Local system changes</td></tr><tr><td>Content</td><td>Data format</td><td>Platform</td><td>Structural</td></tr><tr><td>Population</td><td> $C^a$ </td><td>C/E/M</td><td>M</td><td>C/E/M</td></tr><tr><td>Compilation</td><td></td><td>C</td><td>C/E</td><td>C</td></tr><tr><td>Programming</td><td></td><td>C</td><td>C/E</td><td>C</td></tr><tr><td>Design</td><td></td><td></td><td></td><td>C</td></tr></table>

C: contemporary EIS architecture; E: Evolvable View Environment; M: Metadatabase-enabled EIS  
Automated in a data warehouse with wrappers and monitors.

EIS architecture, which normally includes a data warehouse with a star schema and OLAP facilities. A change in the data content in a local system normally should not require any manual activity, as periodical updates can be carried out automatically for data warehouses with wrappers. Changes in data format, however, require the system administrator to change the star schema (programming and compilation) and repopulate the warehouse. In some cases, it may be that the wrappers will also need to be reprogrammed. Platform changes require programming for the wrappers, which in turn will lead to compilation, and structural changes may require the redesign of the star schema and wrappers. Any redesign will require a sequence of programming, compilation, and population. Clearly, the number of manual activities that are required with the contemporary EIS architecture is large, and the architecture is therefore not very adaptable.

The Evolvable View Environment (EVE) [31,43] resolves most of the shortcomings of the contemporary EIS architecture by automating the tasks that must be carried out to adjust the EIS, and as such is highly adaptable. This automation uses local data source descriptions, which must be modified when changes in the data format or structure occur. Only when there is a platform change do the wrappers need to be reprogrammed and compiled.

Because the new EIS incorporates the Metadatabase approach, it inherits its system integration characteristics. Changes in local database systems are dynamically reflected in transactional changes in the metadata that are stored in the Metadatabase. For example, a change in a data field format is reflected as a field update in a record in the relevant metatable, whereas adding or dropping a local system involves the addition or dropping of records in several metatables. The same can be said of platform changes. No other changes are required in the new EIS, which releases system designers from having to modify and update the centralized database or data warehouse to keep the information in the EIS up to date.

As can be seen in Table 1, the new EIS architecture achieves a higher level of adaptability than EVE, which in turn is much more adaptable than the contemporary EIS architecture.

## 5.1.2. Flexibility

Recall that we defined flexibility as the ability of an EIS to satisfy the changing data analysis requirements of executives. In increasing order of complexity, these requirement changes include the addition of a level of abstraction, the addition of a dimension, and the selection of a new indicator. We measure flexibility in the same way as we measure adaptability, that is, by determining the effort that is required to modify the EIS to cope with the new requirements. The less the effort that is required, the more flexible the system.

Contemporary EISs rely on Relational Online Analytical Processing (ROLAP) techniques, which require a predefined database schema for he performance of data analysis. A major shortcoming is that this approach results in predetermined and fixed analytical patterns, and also means that changes that involve a new indicator or a new dimension (a new analytical pattern) require the recompilation of the database schema and the repopulation of the data warehouse (Table 2). Furthermore, these new requirements may force the redesign of the star schema and the re-programming of the wrappers when the required data come from new data sources. Therefore, the level of flexibility of the contemporary EIS architecture is limited. The EVE suffers from the same limitations as the contemporary EIS architecture, as it only aims at resolving the adaptability problem, and thus its level of flexibility is equivalent to that of the contemporary EIS architecture.

The Metadatabase of the new EIS architecture contains metadata about the local systems. A Multidimensional Analysis Unit (MAU) is dynamically determined for a given indicator based on these metadata. A new analysis requirement from an executive will simply trigger the determination of a MAU, which is carried out automatically. The MAU can be stored for future reuse, as it only changes when a change occurs in the structure of a local data source. Furthermore, data can be retrieved directly from local systems for the first time when a MAU is used or to reflect any data updates that have occurred in the local data sources. Therefore, the new EIS architecture provides much more flexible data analysis, as it is not restricted to any predetermined pattern.

Flexibility of the contemporary EIS architecture

<table><tr><td rowspan="2">Manual activities</td><td colspan="3">Requirement changes</td></tr><tr><td>Abstraction level</td><td>Dimension</td><td>Indicator</td></tr><tr><td>Population</td><td>C/E/M</td><td>C/E/M</td><td>C/E/M</td></tr><tr><td>Compilation</td><td>C/E</td><td>C/E</td><td>C/E</td></tr><tr><td>Programming</td><td> $C^a/E^a$ </td><td> $C^a/E^a$ </td><td>C/E</td></tr><tr><td>Design</td><td> $C^a/E^a$ </td><td> $C^a/E^a$ </td><td> $C^a/E^a$ </td></tr></table>

C: contemporary EIS architecture; E: Evolvable View Environment; M: Metadatabase-enabled EIS.  
Activities that are required when a new data source is involved.

## 5.2. Features of the New EIS architecture

The new EIS architecture incorporates features that are not commonly found in contemporary EISs, such as the ability to access local data sources online and to allow on-demand multidimensional data analysis.

## 5.2.1. Accessing online data sources

The centralized databases of the existing EISs provide only off-line, historical data, and online production data are not available for analysis. Thus, the information that is delivered to executives may be outdated and comparisons with current status may not be possible.

The new EIS architecture integrates and manages heterogeneous local database systems at the metadata level. Instead of duplicating local data into a centralized database or a data warehouse, the new EIS utilizes the Global Query Facility of the MDBMS to directly retrieve data from local systems whenever necessary. The global query is generated based on an existing MAU schema, and thus online production data can be made available to generate up-to-date information for multidimensional data analysis.

## 5.2.2. Facilitating ad hoc data analysis

By using metadata, potential indicators and their dimensions and abstraction levels (analytical patterns or a MAU) can be determined online during an analysis. Hence, the ad hoc analytical needs of executives, which are usually unstructured and novel, can now be entertained. Through a step-by-step process of multidimensional data analysis, the new EIS helps executives to explore business data models to gain information that they may not initially have thought of seeking.

This feature may be used as an exploratory tool for identifying critical success factors. Once their business value has been demonstrated, these new critical success factors may be incorporated into the data warehouse for subsequent use. Specifically, the MAU that is generated specifies the star schema for the new indicator, and may be used directly in the data warehouse.

## 5.3. Shortcomings of the New EIS architecture

A drawback to this new architecture is the seeming trade-off between performance and adaptability and flexibility. However, with existing EISs, extra processing time is also inevitable to reflect changes in a data source, and typically analysts and programmers are called upon to recompile or redesign the data warehouse to support new requests. A further drawback is that because local data sources can be accessed online, data extraction may interfere with local operations. However, the actual trade-off is between “can” and “cannot.” Existing EISs cannot support data analysis that uses a new indicator without reprogramming or redesigning the centralized database or data warehouse. In [9], we propose mechanisms to overcome this shortcoming, such as storing the local data that are extracted for analysis in the EIS to avoid having to repeatedly access the local systems.

## 6. Conclusion

In this paper, we propose a new Executive Information System (EIS) architecture that includes a systems integration mechanism, the Metadatabase approach, to enable on-demand OLAP from heterogeneous systems and databases. The novel and ad hoc needs of executives for business intelligence are supported with the help of metadata, and this new architecture enhances the adaptability of EISs and provides flexibility in data analysis. Online production data from local systems are made available for analysis and the exploration of critical success factors.

With the characteristics that are inherited from the Metadatabase approach, the new EIS architecture is able to integrate local systems at the metadata level, which means that neither standards nor changes are imposed on the local systems. Data can be retrieved online from the local systems, and changes in these systems that range from changes in data types to the addition or removal of a local system are simply reflected by changes in the Metadatabase. The proposed architecture comes with a potential compromise on performance at the local system level, but offers features that are otherwise unavailable.

Designing this architecture is just the starting point. Available data warehousing solutions would be greatly improved by using the proposed architecture, and methods and tools can be developed to take advantage of the combined presence of the Metadatabase and a data warehouse to overcome the shortcomings of the new architecture. We show how these methods and tools can be implemented in [9], and also point to possible research areas to further improve the architecture.

## References

[1] A.K. Aggarwal, Trends in end user computing: a professional's perspective, Journal of End User Computing 6 (3) (1994).

[2] J. Ang, T.S.H. Teo, Management issues in data warehousing: insights from the housing and development board, Decision Support Systems 29 (2000).

[3] Arbor Software White Paper, Relational OLAP: Expectations and Reality, www.arborsoft.com/papers/rolapTOC.html (1996).

[4] G. Babin, Adaptiveness in Information Systems Integration, Rensselaer Polytechnic Institute, Aug 1993.

[5] J. Bird, Executive Information Systems Management Handbook, NCC Blackwell, 1991.

[6] M. Bouziane, Metadata Modeling and Management, Rensselaer Polytechnic Institute, 1991.

[7] S.S. Chawathe, A. Rajaraman, H. Garcia-Molina, J. Widom, Change detection in hierarchically structured information, Proceedings of the ACM SIGMOD Conference, Montreal, Canada, Jun 1996.

[8] M. Chen, A model-driven approach to accessing managerial information: the development of a repository-based executive information system, Journal of Management Information Systems 11 (4) (Spring 1995).

[9] W. Cheung, G. Babin, A metadatabase enabled executive information system (Part B): methods for dynamic multidimensional data analysis, Decision Support Systems 42 (2006) 1599–1612. doi:10.1016/j.dss.2006.01.008 (this issue).

[10] W. Cheung, C. Hsu, The model-assisted global query system for multiple databases in distributed enterprises, ACM Transactions on Information Systems 14 (4) (Oct 1996).

[11] E.F. Codd, S.B. Codd, C.T. Salley, Providing OLAP (Online Analytical Processing) to user-analyst, An IT Mandate, E.F. Codd and Associates, 1996.

[12] P. Fernandez, D. Schnedier, The ins and outs (and everything in between) of data warehousing, SIGMOD Conference, 1996.

[13] D. Friend, Executive information systems: successes and failures, insights and misconceptions, Journal of Information Systems Management 3 (4) (Fall 1986).

[14] J. Hammer, H. Garcia-Molina, J. Widom, W. Labio, Y. Zhuge, The Stanford data warehousing project, IEEE Data Engineering Bulletin 18 (2) (Jun 1995).

[15] C. Hsu, The metadatabase project at Rensselaer, ACM SIGMOD Record 20 (4) (1991).

[16] C. Hsu, Enterprise Integration and Modeling: The Metadatabase Approach, Kluwer Academic Publishers, 1996.

[17] C. Hsu, G. Babin, A rule-oriented concurrent architecture to effect adaptiveness for integrated manufacturing enterprises, Proceedings of the International Conference on Industrial Engineering and Production Management, Brussels, Belgium, 1993.

[18] C. Hsu, A. Perry, M. Bouziane, W. Cheung, TSER: a data modeling system using the two-stage-entity-relationship approach, Proceedings of the 6th International Conference on Entity-Relationship Approach, New York, NY, 1987.

[19] C. Hsu, M. Bouziane, W. Cheung, J. Nogus, L. Rattner, L. Yee, A metadata system for information modeling and integration, Proceedings of the 1990 International Conference on Systems Integration, IEEE Computer Society, April 1990.

[20] C. Hsu, M. Bouziane, L. Rattner, L. Yee, Information resources management in heterogeneous distributed environments: a metadatabase approach, IEEE Transactions on Software Engineering 17 (6) (1991).

[21] C. Hsu, G. Babin, M. Bouziane, W. Cheung, L. Rattner, L. Yee, Metadatabase modeling for enterprise information integration, Journal of Systems Integration 2 (1) (1992).

[22] S.H. Hung, Expert versus novice use of the executive support systems: an empirical study, Information and Management 40 (2003).

[23] W.H. Inmon, R.D. Hackathorn, Using the Data Warehouse, John Wiley and Sons, 1994.

[24] W.H. Inmon, J.D. Welch, K. Glassey, Managing the Data Warehouse, John Wiley and Sons, 1997.

[25] W.H. Inmon, J. Zachman, K. Geiger, Data Stores, Data Warehousing, and the Zachman Framework, McGraw-Hill, 1997.

[26] J.W. Jones, J.R. McLeod, The structure of executive information systems: an exploratory analysis, Decision Sciences 17 (2) (Spring 1986).

[27] Kenan System Corporation, An Introduction To Multidimensional Database Technology, www.kenan.com/acumate/acu\_- home.htm (1995).

[28] W.J. Labio, H. Garcia-Molina, Efficient snapshot differential algorithms for data warehousing, Proceedings of VLDB Conference, Mumbai, India, Sept. 1996.

[29] I. Millet, C.H. Mawhinney, Executive information systems: a critical perspective, Information and Management 23 (2) (Aug 1992).

[30] OLAP Council White Paper, OLAP Technology, www.olapcouncil.org/whtpap.html (1995).

[31] E.A. Rundensteiner, A. Koeller, X. Zhang, Maintaining data warehouses over changing information sources, Communications of the ACM 43 (6) (June 2000).

[32] K. Sahin, Multidimensional database technology and data warehousing, Relational Database Journal 4 (6) (1995).

[33] Y. Tao, Differential control on distributed database updates using concurrent rulebase shells, Rensselaer Polytechnic Institute, 1997.

[34] L. Volonino, H.J. Watson, S. Robinson, Using EIS to respond to dynamic business conditions, Decision Support Systems 14 (2) (Jun 1995).

[35] M.T. Warmouth, D. Yen, A detailed analysis of executive information systems, International Journal of Information Management 12 (3) (Sept. 1992).

[36] H.J. Watson, M.N. Frolick, Executive information systems: determining information requirements, Information Systems Management 9 (2) (Spring 1992).

[37] H.J. Watson, M.N. Frolick, Determining information requirements for an EIS, MIS Quarterly 17 (3) (Sept. 1993).

[38] H.J. Watson, R.K. Rainer, G. Houdeshel, Executive information systems: emergence, development, impact, John Wiley and Sons, Inc., 1992

[39] H.J. Watson, R. Watson, S. Singh, D. Holmes, Development practices for executives information systems: findings of a field study, Decision Support Systems 14 (1995).

[40] J. Widom, Research problems in data warehousing, Proceedings of the 4th International Conference on Information and Knowledge Management (CIKM), Nov 1995.

[41] J.L. Wiener, H. Gupta, W.J. Labio, Y. Zhuge, H. Garcia-Molina, J. Widom, A system prototype for warehouse view maintenance, Proceedings of the ACM Workshop on Materialized Views: Techniques and Applications, Montreal, Canada, Jun 7, 1996.

[42] X.M. Xu, B. Lehaney, S. Clarke, Y. Duan, Some UK and USA comparisons of executive information systems in practice and theory, Journal of End User Computing 15 (1) (March 2003).

[43] X. Zhang, E.A. Rundensteiner, The SDCC framework for integrating existing algorithms for diverse data warehouse maintenance tasks, Proceedings of the International Database Engineering and Application Symposium, Montreal, Canada, Aug 1999.

[44] Y. Zhuge, H. Garcia-Molina, J.L. Wiener, The strobe algorithms for multi-source warehouse consistency, The 4th Conference on Parallel and Distributed Information Systems, Miami Beach, FL, Dec 1996.
