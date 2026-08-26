---
otero_id: 21217
otero_key: "FTR73KGA"
title: "Metadata management: past, present and future"
authors: "Arun Sen"
year: "2004"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(02)00208-7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Metadata management: past, present and future

Arun Sen\*

Department of Information and Operations Management, Mays Business School, Texas A&M University, College Station, TX 77843, USA

Received 1 October 2002; accepted 4 December 2002

## Abstract

In the past, metadata has always been a second-class citizen in the world of databases and data warehouses. Its main purpose has been to define the data. However, the current emphasis on metadata in the data warehouse and software repository communities has elevated it to a new prominence. The organization now needs metadata for tool integration, data integration and change management. The paper presents a chronological account of this evolution—both from conceptual and management perspectives.

Repository concepts are currently being used to manage metadata for tool integration and data integration. As a final chapter in this evolution process, we point out the need of a concept called ‘‘metadata warehouse.’’ A real-life data warehouse project called TAMUS Information Portal (TIP) is used to describe the types of metadata needed in a data warehouse and the changes that the metadata go through. We propose that the metadata warehouse needs to be designed to store the metadata and manage its changes. We propose several architectures that can be used to develop a metadata warehouse. <sup>D</sup> 2003 Elsevier B.V. All rights reserved.

Keywords: Metadata; Data warehouse; Decision support; Metadata warehouse; Repositor

## 1. Introduction

Metadata is a term that has been used and misused many times in the past. Webster defines ‘‘meta’’ as a more comprehensive term needed to ‘‘describe a new and related discipline designed to deal critically with the original one.’’ Metadata consequently then describes a discipline that fosters the study of data about data.

The origin of metadata can be traced back to how we use measurement units. The purpose of a unit is to describe a property of an object. For example, the length (a physical property) of a stick (an object) is 5 ft (a measurement unit). This example uses for one object, a data item (the number 5) and two metadata items (length and a measuring unit).

In the past, the metadata has often been treated as a second-class citizen. With the advent of computers and our incessant need for data, we have introduced techniques to store data permanently on a secondary storage. These data can then be retrieved and used by application programs. File managers are used to store and retrieve data from the secondary storage. To accomplish their job, file managers use such metadata as field names and filenames. This use of metadata, along with the actual data, now has extensively been ingrained in the database management technology.

As a result, in the last 30 years, we have witnessed a tremendous growth in the use of metadata in developing information systems. The purpose of this paper is to study this field and see how it helps us in decision support. To do this, we first describe a 40-year chronological development of metadata concept (see Section 2). Several management tools were also designed to manage metadata in the last 40 years. In Section 3, we categorize these developments. We argue that the most neglected area in the metadata management is the notion of managing changes in metadata. Section 4 emphasizes the changes in metadata and describes a real-life case study where the changes are of utmost importance. To manage these changes, we propose a new management tool called metadata warehouse. Unlike other tools that focus on tool integration and data integration, this tool manages the changes in metadata for organizational decision support. We conclude the paper in Section 5.

## 2. Evolution of the metadata concept

To describe the evolution of the concept of metadata, we look at each decade starting with the 1960s.

## 2.1. The 1960s

Early work with files presumed that files were on tapes. Access was sequential and the cost of access grew in direct proportion to the size of the file. Simple indexes were used to speed up the access. However, as the indexes grew, they too became difficult to manage. Due to this reason, in the early 1960s, the idea of applying tree structures emerged as a potential solution. In the late 1960s, using the work of B  trees and B+ trees, many commercial vendors created file systems that were faster and were not sequential. For all file systems, the format of the records is first determined. The field names of the records and their data types are essentially metadata used in the file.

During this period, the use of metadata in program development has also been fairly discrete. For example, in attempting to reuse code, programming languages allow applications to include codes from their software libraries. We discuss these libraries in Section 3.

## 2.2. The 1970s

The 1970s could be called the decade that started the metadata phenomenon. With the advent of database management system (DBMS), the use of metadata increased tremendously. For example, in relational DBMS, the metadata is extensively used to define data. These metadata include relation names, attribute names, key and domain information. The collection of metadata is used to define schema and subschemas. In 1976, with the introduction of entity relationship (ER) data model and later with the advent of other semantic data models, higher level metadata were being used. As the semantic data models (like ER) did not have a supporting DBMS, a translational mechanism was deployed to translate the higher level (like ER) metadata to relational metadata.

## 2.3. The 1980s

With the success of database management systems to store and retrieve business data (which are essentially flat), efforts were made to look into non-business data types. These data types came from diverse application areas such as Computer-Aided Design/Computer-Aided Manufacturing (CAD/CAM), Computer-Aided Software Engineering (CASE), Geographic Information System (GIS), document storage and retrieval, science and medicine. The notion of data, at this time, got replaced by a term called asset. An asset is a piece of useful item that is a product or byproduct of application development process. An asset can be more tangible, like data (as before), designs and software code, or more intangible, such as knowledge and methodologies. Tangible asset can take a form of a large-grained component like framework or a complete application; it can also be a fine-grained component like subroutine, a class, or an encapsulated component. It can include patterns [6] and algorithms [6]. Examples of intangible asset can include programming knowledge, programming plans, software system architectures, project plans, design documents, user documents and other relevant knowledge sources.

Just like data, assets need to be stored on disks to be reused. Assets are, however, much more complicated than simple business data and are difficult to store and access. Several new database paradigms were proposed at this time that deal with assets and their metadata semantics. This includes Complex Object Model [3], Nested Relation Data Model [4,20] and Object-Oriented Data Model [1].

Accessing these assets was mainly done through object queries. An asset is stored as an object or a collection of objects. The queries use metadata that are usually class definitions and class hierarchies. Class definitions are very much like table definitions with some exceptions. They include attribute definitions along with method definitions for the class. Three predominant relationships used in building class hierarchies are aggregation [3], part – whole [3] and generalization [3]. Aggregation relationship dealt with relationships among classes that are related. For example, course class is related to student class and instructor class. Part–whole, on the other hand, dealt with composition. For example, vehicle class is composed of chassis class, engine class and others. Generalization (also known as ‘‘is-a’’) relationship was used to show classification among classes. For example, motor-vehicle and airplane classes are the subclasses of vehicle class. Generation relationship allows the subclasses to inherit the properties of the superclass.

As database management systems access data through indexing, the query to access an asset eventually finds all parts of the asset from the database and combines them to create the asset. However, it is sometimes difficult to store an asset as a collection of objects in a database. This is because the asset may be a package (like a code package or a document) that cannot be decomposed into objects. To help in this process, metadata was again utilized. A classification scheme, based on metadata, was proposed by Prieto-Diaz [18]. The idea of the classification scheme was to show relationships by collection, that is, to keep related classes more or less together according to the closeness of the relationship. He introduced the notion of faceted classification scheme. A facet is an arranged group of descriptors. For example, in the Unix domain, a facet could be {by action} [18]. A facet takes on terms or values. The {by action} facet can take terms like get, put, update, append, check and others.

## 2.4. The 1990s

In the 1990s, we see three separate research paradigms emerge that were responsible to move the metadata technology forward. We describe them one by one as follows.

## 2.4.1. Metadata in code reusability

The notion of code reusability in software development, started in the 1980s with Japanese software factories [13], became very important in the 1990s.

To facilitate the code reusability, research on software development environment flourished. A software development environment (SDE) is a collection of software and hardware tools, which explicitly tailored to support the production of software systems in a particular application domain [22]. A SDE uses metadata in all of its operations. The objective of the use of metadata is to support the selection of the tools used in the SDE. Many kinds of SDEs are currently in practice. These environments are classified into three major groups [22]: Programming Environments (PE), CASE and Software Engineering Environments (SEE). A PE is an environment that is principally intended to support the process of programming, testing and debugging. A CASE is an environment that supports software specification and design. It can also be used with a programming environment. A SEE is intended to support the production of large, long-lifetime software systems, the maintenance costs of which typically exceed development costs and are produced by a team rather than individual programmers. REuse Based on Object-Oriented Techniques (REBOOT) by Morel and Faget [14] is an example of Programming Environment tool that supports storage and retrieval of code components. It uses the facet-based classification scheme to create the metadata of the components. Four such facets are used: abstraction, operations, operates-on and dependencies. In systems like this, the metadata is stored in a database. If code library gets updated, corresponding entries in the database are changed.

## 2.4.2. Metadata in asset repository

According to Bernstein [2], an asset repository (also called a repository) is a shared database of information about engineered artifacts, such as software, documents, maps and other things. In other words, a repository is a metadata manager. For example, a repository that supports software development and deployment tools could store metadata such as database descriptions, form definitions, controls, documents, interface definitions, source code, help text and others. The objective of the use of metadata in a repository context is to emphasize the selection and integration of diverse tools that support the different kinds of data.

## 2.4.3. Metadata in data warehouse

Metadata took a significant role in the 1990s due to the advent of data warehouse concept. Kimball et al. (Ref. [8], p. 22) define metadata in the context of data warehouse as ‘‘all of the information in the data warehouse environment that is not the actual data itself.’’ The metadata in the data warehouse context are basically of two kinds: back room metadata and front room metadata. The back room metadata is process related and guides the extraction, cleaning and loading processes. Examples include specifications typically related to source data, such as source schemas, old formats for archived mainframe data, ownership description of the source, automated extract tool settings and others; data staging metadata such as data cleaning specifications, slowly changing dimension policies and others; data transform logs; and DBMS system table contents. The front room metadata is more descriptive, and it helps query tools and report-writers function smoothly. Examples include join specifications, network security user privilege profiles, usage and access maps, network security usage statistics and others.

The need of asset repositories became crucial in the late 1990s as software projects increasingly were focussed on integrating and reusing codes, classes, components, patterns, frameworks and applications. The need is also fueled by the massive use of data warehouse techniques in the brick and mortar industry along with the web world to develop decision support using huge operational data.

![](/api/attachments/FTR73KGA/fulltext/images/2549d5bc9259fa0a9401a01b903445dfb02a31d9c951b4597ded3a1ea98c7f9a.jpg)  
Fig. 1. The time line for metadata management.

## 2.5. 2000 and beyond

Fig. 1 illustrates the evolution of metadata concept in a chronological order. Since the 1960s, the concept of metadata has grown quite a bit. Starting from the simple filenames, field names and field types, metadata in the 1970s described data definitions as modeled by various data models. In the 1980s, with the advent of object-oriented programming, the metadata started to include class definitions and class hierarchies (aggregation and generalization). A special kind of classification scheme called faceted classification was introduced in the 1980s for classifying assets. In the early 2000, however, a major effort in dealing with metadata is in the recognition of the need for the creation of a metadata standard. This standard was fueled by the fact that unlike the software development, a data warehouse project needs heterogeneous tool and data environments. For example, in the data warehouse world, data quality tools, data modeling tools, ETL tools and end-user tools developed by different vendors with entirely different specifications. The integration using a metadata standard allows them to communicate with each other. The data in a data warehouse can also be of various types and format. A standardization effort will also help in data integration.

## 3. Evolution of metadata management

Metadata, although started as information to describe data or an asset, now is competing to get equal attention as an asset or data it defines. With phenomenal use of metadata in software development, in database management and in data warehouse design and implementation, it is important to look into the techniques used to manage the metadata.

To properly narrate the evolution of metadata managers, we start with a set of tools that implicitly manage data with metadata. From this stage, we describe how metadata management has progressively moved away from implicit management to co-management with asset and data, and then into explicit management with repository managers.

## 3.1. Stage I. Implicit metadata management

Even before the advent of database management system, software library manager was an early attempt to discretely use metadata to reuse codes. It is designed to co-manage data and metadata. It has been so successful that it still exists today. Most programming languages allow applications to include codes from their software libraries. A software library is a collection of programs that can be reused in building larger program modules. In such a programming environment, a language compiler converts a program into an object module. The linker using underlying metadata then combines all object modules that make up a program including the object modules that are obtained from the library. Some example libraries are C++ Class Library [15], Standard C Library [16] and Microsoft’s MFC Library.

Although the joint management of metadata and data is not complicated, libraries like these are fairly static. Once a library has been developed and released to the external world, its structure and interface cannot change without great difficulty for the user base [19]. Using a library is equivalent to using a programming language. Changes in a class library are often more difficult to deal with than changes in a programming language.

## 3.2. Stage II. Co-management of metadata

With the advent of database management system, efforts were made to manage metadata more explicitly. This idea had been exploited to make the library managers more dynamic, where users need a mechanism to insert, delete, modify and retrieve the content of the library easily.

To create easy manipulation of the library, we use metadata along with the library. In this technique, metadata of codes need to be captured and used along with the actual library. The metadata of a code contain data about the code. The idea is to store the metadata in a database. If software library gets updated, corresponding entries in the database are changed.

The evidence of this approach can be seen in software maintenance literature. Leiter et al. [9] describe a software tool that entails a relational database with an interactive interface that supports queries about programs written in object-oriented languages.

Linos and Courtois [10] describe a tool set that includes tools to detect a mixture of procedural and object-oriented program information from the C++ code. Examples include files (both source and include files), data types, functions, constants, variables, parameters, classes, objects, etc. These are then used to populate a database. Different browsing tools are available to display metadata on the screen. IBM has an information retrieval tool called ReDiscovery TM based on OS/2 that can be used to create and search databases of information about virtually any kind of database or file system.

## 3.3. Stage III. Explicit metadata management

In this stage, metadata and their management come of age. Instead of being a side issue, metadata now is looked upon as glue that binds many enterprise resources such as applications, ERP activities, Internet technologies and data warehouses. The metadata management tool (also known as repository) now becomes crucial.

The first attempt in this area was the introduction of data dictionary. The data dictionary typically was very data focused. It provided a centralized repository of information about data such as meaning, relationships, origin, domain, usage and format [11,12]. The purpose of data dictionary was to assist the DBAs in planning, controlling and evaluating the collection, storage and use of data.

To allow the library to hold other items that are not software, a second mechanism, called repositories (see Section 2), was introduced. According to Bernstein [2], a repository is a shared database of information about engineered artifacts, such as software, documents, maps and other things. For example, a repository that supports software development and deployment tools could store database descriptions, form definitions, controls, documents, interface definitions, source code, help text and others.

In the late 1980s, IBM offered to build a universal repository, a repository that would store the outputs of a wide variety of CASE tools and make the stored elements available to any tool that requested them. Unfortunately, IBM’s repository was never delivered due to software industry’s shift from COBOL orientation to C/C++ orientation and also from main frame to client – server [23]. In the late 1990s, however, this idea got picked up again by other vendors who now have developed several repositories. These vendors include Microsoft (with Microsoft Repository), Unisys (with Universal Repository), Computer Associate (with Platinum Repository), ViaSoft (with Rochade Repository), Softlab (with Enabler Repository) and Oracle (with Oracle Repository).

To understand what constitutes a repository, let us describe the important features of any repository. The first feature of a repository is the types of metadata it manages. The types include database metadata, data model metadata, data movement metadata, business rules metadata, application component metadata, data access metadata and data warehouse related metadata. Other features of a repository include an information model that describes the core metadata types of the repository; a specification language that is the formal specification language for the tool; a language that supports tool interoperability across different products; a standard query language to query the metadata; and others. We provide as an example the features of Microsoft Repository Service (see Table 1). From this table, it is apparent that the repository architecture must include four layers. The top-most layer is usually the user access layer. The objectives of this layer are to provide support to browsing through the repository data in a client– server setup or in the web environment; to provide an interface with CASE tools; and to help the component-based development (CBD) tools develop and manage components.

The second layer is called common infrastructure support layer. The objective of this layer is to support common issues among assets such as integration of tools, cross-platform support, event management and others. The next lower layer is called repository engine layer. This layer is responsible to create and manage repository objects, their versions and configurations. It is designed and developed using an objectoriented paradigm. Finally, at the bottom level (called data services layer), a repository has a data server and supports insertion, deletion, modification and retrieval of the repository data. The technology effectively manages the information assets of the enterprise, provides a metaview of the developmental process across all software development tools, uses common data store for development tools and allows version control of any object.

Microsoft’s Repository 2.1 http://msdn.microsoft.com/library/default.asp?url=/library/en-us/reposit/htm/ reconthearchitectureofmicrosoftrepository.asp

<table><tr><td>Feature</td><td>Availability of the feature in the repository</td></tr><tr><td>Date repository was introduced</td><td>Repository 1.0 was introduced with Microsoft&#x27;s VB5.0 in 1997:</td></tr><tr><td>Major objectives of the repository</td><td>To provide a metaview of the development process across all development tools like VB, C++, etc.To study the impact of changes of any object.To provide a common data store for all development tools.</td></tr><tr><td>Types of metadata</td><td>Component definitions, development and deployment models, reusable software components, data warehouse descriptions, web pages, etc.</td></tr><tr><td>Information model that describes the core metadata types</td><td>Supports Meta Data Coalition&#x27;s Open Information Model (OIM). OIM is a set of metadata specifications to facilitate sharing between and reuse between tools and systems. The OIM consists of over 200 types and 100 relationships, described in UML and organized in easy-to-use and easy-to-extend subject areas.</td></tr><tr><td>Specification language</td><td>Universal Modeling Language (UML)—an object-oriented language.</td></tr><tr><td>Repository architecture</td><td>Repository Services 2.1 has four layers:Top Layer—Tools and Application Layer. This layer supports integrated tools, metadata-driven applications and other utilities and browsers.Layer III—OIM that supports shared metadata objects and structures, relationship among objects, etc.Layer II—Repository object manager responsible for life cycle management and maps objects to tables.Bottom layer—persistence service with jet database engine or SQL server.</td></tr><tr><td>Environment particulars</td><td>Windows-based system.</td></tr><tr><td>Development kit</td><td>Systems development kit (SDK) is available.</td></tr><tr><td>Metadata browsing facility including web browsing</td><td>Yes</td></tr><tr><td>Exchange metadata between multiple heterogeneous repositories</td><td>Supports XML interchange format</td></tr><tr><td>Object management service support</td><td>(a) Version Control, (b) Composite Object Service, (c) Collection Service (e.g. relationship service), etc.</td></tr><tr><td>Component-based framework support</td><td>Component Object Model (COM) based</td></tr><tr><td>Query language support</td><td>SQL</td></tr></table>

## 3.4. Stage IV. Metadata integration management

The focus of this stage is to manage the integration of diverse metadata in an application. There are two kinds of integration: tool integration and data integration. Tools typically generate toolspecific metadata. To establish communication among multiple tools, these metadata need to be integrated. Similarly, data can be of different formats and can come from different worlds. These data also need to be integrated to help decision support. Repository technology (of Stage III) that was originally created to manage metadata can be used to integrate.

The repository technology described above supports the metadata integration as long as the metadata follow a common model, like Microsoft’s Component

Object Model (COM) architecture. In the world of diverse metadata integration, such as currently being used in data warehouse [17] domain, the tools do not have a common model. This is because different tools from different vendors with different specifications (or metadata) are brought into the project. Tools can be ‘‘best-of-breed,’’ ‘‘most compatible,’’ or ‘‘most economic.’’ This is also true for data. The repositorybased metadata management is not very effective in this kind of metadata integration.

Noticing this kind of integration problem, two standardization groups, Meta Data Coalition (MDC) and Object Management Group (OMG), started to work on the metadata standard in the 1990s. They called the metadata standard a metamodel. The MDC group along with Microsoft in the late 1990s developed and adopted a metadata standard called Open

![](/api/attachments/FTR73KGA/fulltext/images/4ace942810a16300b763efb9f963320206eaaf874fa27e946af2711d01c22054.jpg)  
Fig. 2. The data warehousing process for the TIPS project with changed statistics.

Information Model (OIM). The other group, OMG, created a model called Common Data Warehouse Metamodel (CWM) [17] in early 2000. In June 2000, MDC members decided to join OMG and support one standard in metadata for integration.

## 4. Proposing metadata warehouse—the final frontier

In the earlier sections, we have seen how the concept of metadata has evolved and how tools to

.logtable tamus\_load.cbm001\_log;

.run file /spare3/logon/loaddata

drop table tamus\_load.et\_cbm001; drop table tamus\_load.wt\_cbm001 drop table tamus load.uv cbm001

drop table tamus\_load.cbm001;

CREATE SET TABLE tamus\_load.cbm001, NO FALLBACK, NO BEFORE JOURNAL, NO AFTER JOURNAL (record\_cd CHAR(01) TITLE 'record\_code', fice\_cd CHAR(06) TITLE 'fice\_code', student\_id CHAR(09) TITLE 'student\_id', gender CHAR(01) TITLE 'gender', classification CHAR(01) TITLE 'classification' date\_of\_birth CHAR(08) TITLE 'date\_of\_birth', tuition\_status CHAR(01) TITLE 'tuition\_status', residence CHAR(03) TITLE 'residence', transfer\_in\_college CHAR(06) TITLE 'transfer\_in\_college', ethnic\_origin CHAR(01) TITLE 'ethnic\_origin', semester CHAR(01) TITLE 'semester', year\_id CHAR(04) TITLE 'calendar\_year', sch\_load\_inter\_inst CHAR(02) TITLE 'sch\_load\_inter\_inst', flex\_entry CHAR(01) TITLE 'flex\_entry', remote\_campus CHAR(01) TITLE 'remote\_campus', major\_area\_cip CHAR(08) TITLE 'major\_area\_cip', doc\_funding\_cd CHAR(02) TITLE 'doc\_funding\_code', tuition\_waiver CHAR(02) TITLE 'tuition\_waiver'. sch\_undergrad\_prog CHAR(03) TITLE 'sch\_load\_undergraduate\_degree\_program', ug\_fund\_limit\_ind CHAR(01) TITLE 'undergraduate\_funding\_limitation\_indicator', last\_name CHAR(20) TITLE 'Iast\_name', first\_name CHAR(10) TITLE first\_name', mi CHAR(01) TITLE 'middle\_initial', sch\_dual\_credit CHAR(02) TITLE 'sch\_dual\_credit' teacher\_ed\_prog CHAR(02) TITLE 'teacher\_education\_program', update\_cd CHAR(01) TiTLE 'update\_code ) PRIMARY INDEX (student\_id, semester, year\_id );

.begin import mload tables tamus\_load.cbm001 worktables tamus load.wt cbm001 errortables tamus load.et cbm001 Tamus load.uv cbm001

Fig. 3. A partial load script used in TIP data warehouse.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*MDBBTEQ TO LOAD TAMUS\_LOAD.CBM001TO CBM STUDENT8/24/01SPRING 2001 LAYOUT

MOD #1(DD): updated temp DDL to include all target columns, deleted rename logic (now in separate script), added load\_date column (load effective date) \* .run file /spare3/logon/loaddata;

CREATE SET TABLE TAMUS\_DATA.cbm\_student\_temp ,NO FALLBACK , NO BEFORE JOURNAL, NO AFTER JOURNAL ( Record\_cd CHAR(1) CHARACTER SET LATIN NOT CASESPECIFIC TITLE 'record\_code', Load\_date DATE FORMAT 'YYYY/MM/DD' TITLE load date' , Fice\_cd CHAR(6) CHARACTER SET LATIN NOT CASESPECIFIC TITLE 'fice\_code', Student\_id CHAR(9) CHARACTER SET LATIN NOT CASESPECIFIC TITLE 'student\_id', Gender CHAR(1) CHARACTER SET LATIN NOT CASESPECIFIC TITLE 'gender', Classification CHAR(1) CHARACTER SET LATIN NOT CASESPECIFIC TITLE 'classification', Date\_of\_birth DATE FORMAT 'YYYY/MM/DD' TITLE 'date\_of\_birth', Tuition\_status CHAR(1) CHARACTER SET LATIN NOT CASESPECIFIC TITLE 'tuition\_status', Residence CHAR(3) CHARACTER SET LATIN NOT CASESPECIFIC TITLE 'residence', Transfer\_in\_college CHAR(6) CHARACTER SET LATIN NOT CASESPECIFIC TITLE 'transfer\_in\_college', Sch\_load\_on\_campus SMALLINT TITLE 'sch\_load\_on\_campus', Sch\_load\_off\_campus SMALLINT TITLE 'sch\_load\_off\_campus', Doc\_hrs\_funded SMALLINT TITLE 'doc\_hrs\_funded', Nursing\_pgm CHAR(2) CHARACTER SET LATIN NOT CASESPECIFIC TITLE 'nursing\_program\_code', Ethnic\_origin CHAR(1) CHARACTER SET LATIN NOT CASESPECIFIC TITLE 'ethnic\_origin', Semester CHAR(1) CHARACTER SET LATIN NOT CASESPECIFIC TITLE 'semester', Year\_id SMALLINT TITLE 'year', Sch\_load\_inter\_inst SMALLINT TITLE 'sch\_load\_inter\_inst', Flex\_entry CHAR(1) CHARACTER SET LATIN NOT CASESPECIFIC TITLE 'flex\_entry', Remote\_campus CHAR(1) CHARACTER SET LATIN NOT CASESPECIFIC TITLE 'remote\_campus', Major\_area\_cip CHAR(10) CHARACTER SET LATIN NOT CASESPECIFIC TITLE 'major\_area\_cip', Doc\_funding\_cd CHAR(2) CHARACTER SET LATIN NOT CASESPECIFIC TITLE

Fig. 4. A partial transform script used in TIP data warehouse.

'doc\_funding\_code', Tuition\_waiver CHAR(2) CHARACTER SET LATIN NOT CASESPECIFIC TITLE 'tuition\_waiver', Sch\_load\_undergrad SMALLINT TITLE 'sch\_load\_undergrad', Sch\_load\_develop SMALLINT TITLE 'sch\_load\_developmental', Sch\_non\_state SMALLINT TITLE 'sch\_load\_non\_state', Sch\_develop\_non\_state SMALLINT TITLE 'sch\_load\_developmental\_non\_state', Sch\_inter\_inst\_non\_state SMALLINT TITLE 'sch\_load\_inter\_institutional\_non\_state', Sch\_state SMALLINT TITLE 'sch\_load\_state', Sch\_develop\_state SMALLINT TITLE 'sch\_load\_developmental\_state', Sch\_undergrad\_prog SMALLINT TITLE 'sch\_load\_undergraduate\_degree\_program', ug\_fund\_limit\_ind CHAR(1) CHARACTER SET LATIN NOT CASESPECIFIC TITLE 'undergraduate\_funding\_limitation\_indicator' Last\_name CHAR(20) CHARACTER SET LATIN NOT CASESPECIFIC TITLE 'last\_name', First\_name CHAR(10) CHARACTER SET LATIN NOT CASESPECIFIC TITLE 'first\_name', mi CHAR(1) CHARACTER SET LATIN NOT CASESPECIFIC TITLE 'middle\_initial', Sch\_dual\_credit SMALLINT TITLE 'sch\_dual\_credit', Teacher\_ed\_prog CHAR(2) CHARACTER SET LATIN NOT CASESPECIFIC TITLE 'teacher\_education\_program', fte\_student CHAR(3) CHARACTER SET LATIN NOT CASESPECIFIC TITLE 'fte\_student', School\_college CHAR(6) CHARACTER SET LATIN NOT CASESPECIFIC TITLE 'school\_or\_college', Remote\_teaching\_site CHAR(6) CHARACTER SET LATIN NOT CASESPECIFIC TITLE 'remote\_teaching\_site', rn\_nurse\_prg CHAR(6) CHARACTER SET LATIN NOT CASESPECIFIC TITLE 'rn\_nursing\_program', Update\_cd CHAR(1) CHARACTER SET LATIN NOT CASESPECIFIC TITLE 'update\_code') PRIMARY INDEX ( fice\_cd ,student\_id ,semester ,year\_id ); sel date ||'  ∥| time; COLLECT STATISTICS ON tamus\_load.cbm001 index ( student\_id ,semester ,year\_id );

Fig. 4 (continued ).

manage them have matured from simple library managers to techniques that help integrate tools metadata. The integration is accomplished through a repository manager, supporting a common model of metadata under a single environment; or with a diverse set of metadata that follow a metamodel, called CWM.

The study of CWM reveals that it does not only support integration of tool metadata, it also supports the integration of metadata created in a data warehouse project. The metadata in a data warehouse project are of two kinds—back-room types and front-room types. The back room metadata is process related and guides the extraction, cleaning and loading processes. Examples include specifications related to source data, such as source schemas, old formats for archived mainframe data, ownership description of the source, automated extract tool settings and others;

data staging metadata such as data cleaning specifications, slowly changing dimension policies and others; data transform logs; and DBMS system table contents. The front room metadata is more descriptive, and it helps query tools and report-writer function smoothly. Examples include join specifications, network security user privilege profiles, usage and access maps, network security usage statistics and others. It is not only important to capture all these metadata, but we also need to worry about the changes that happen to them.

Unfortunately, at the present time, no single robust tool is available that completely supports the CWM. Few vendors, like Microsoft’s Metadata Services 2000 and Teradata’s MDS, have offered extended repository-based tools. These tools support repository features but fail to cover the decision support questions on metadata changes. We propose a new management tool as the final stage of evolution of the metadata management. We call this last stage metadata warehouse. We adopt this term from the data warehouse literature to emphasize the need for creating a warehouse full of metadata only. We need this warehouse to manage different kinds of changes that happen in a regular data warehouse. These changes include organizational changes, technological changes, physical changes, process changes, end-user requirement changes and website changes [21].

The best way to demonstrate the need of a metadata warehouse is to look at a real-life data warehouse project. Once we describe the development of the data warehouse, we need to see if we can answer the following metadata questions. They include what kinds of metadata we need to store? What are the changes in this metadata? How frequent are these changes? Where do they happen most?

## 4.1. Developing an academic data warehouse

To answer the above questions, we look at a working data warehouse. With the popularity of the data warehouse in the industry, several academic institutions (like Arizona State University, University of Wisconsin at Milwaukee and Texas A&M University) are currently developing data warehouses to meet their decision support needs. In this paper, we use one such data warehouse project to develop the concept of metadata warehouse.

The goal of Texas A&M University System’s (TAMUS) Data Warehouse Project, called TAMUS Information Portal (TIP), was to develop an automated information system. This system uses decision support analysis of financial, personnel and academic data for the Board of Regents, and management of the TAMUS and its member institutions and agencies [5]. The current on-line transaction processing systems are unable to meet the growing need for management information. Before the data warehouse, the ability to perform analysis and cross-functional analysis was a manual process. In this environment, satisfying information requests were problematical for several reasons:

\- requests are often unpredictable, important and urgent, which means that key information technology resources have to be redirected, making other project work discontinuous and extending project completion dates;

\- developing answers is laborious, because custom queries or report programs have to be analyzed, designed, developed and tested;

\- answers can be inconsistent, because answers developed by different analysts—or even by the same analyst at different times—have the potential of producing results that do not agree with other or previous results.

The TAMUS, spurred by a state management control audit, embarked on a process to define its information needs and to develop a system to address those needs. The resulting data warehouse project was defined and managed by business users and supported by an NCR’s Teradata system.

The primary objective of the project was to develop an enterprise data warehouse environment to:

\- provide the ability to access historical information currently stored in existing systems;

\- provide interactive and ad hoc data exploration;

\- provide information on a secure intranet website;

\- provide access to information for ad hoc query, analysis and report writing;

\- serve as a credible source of information;

\- support the decision-making process without hindering the performance of the operational systems.

Fig. 2 describes the data warehousing process used in the TIP project. The project has been successfully completed in the beginning of 2001 and has realized some initial benefits. They are as follows:

\- integrating disparate administrative system data into a common system for all management reporting;

\- providing a ‘‘single version of the truth’’;

\- serving as a source system for data mart projects undertaken by various members;

\- providing the end-user capabilities to users as ‘‘drill down’’ analysis of electronic reports; reports that can include graphs and or tables; reports that are easily modified; reports that can be requested anytime by anyone (with appropriate security and access privileges); reports that can be automatically run when the data warehouse is updated and ‘‘pushed’’ to the users.

## 4.2. Details of metadata in the TIP warehouse

Various types of metadata are at play in TIP data warehouse. We start with data sets that are currently sourced from the Texas Higher Education Coordinating Boards. There are nine such flat files. Each file contains summarized data elements that are not related to data elements in the other files. For example, Student-Report data source (cbm001) has 34 attributes such as record code, institution code, student identification number, gender, classification and others. In the ETL process, we have Teradata Load Scripts and Transform Scripts. Figs. 3 and 4 show a partial picture of these scripts.

The logical and physical diagrams also form a source of metadata. In TIPs, these diagrams were created in Erwin Development tool and can be reproduced in XML. Fig. 5 shows a partial XML description of the physical ERD. The TIP data warehouse runs on Teradata DBMS that provides another set of metadata called target data table metadata (see Fig. 6 for a sample DDL). The view also is a source of metadata (see Fig. 7 for a sample user view DDL). Finally, the end-user application uses Business Object end-user tool. A sample metadata, called Business Object Universe, is also shown in Fig. 8.

## 4.3. Changes in the TIP metadata

As business needs or conditions change over time, a data warehouse must be responsive, continuously evaluating effectiveness of the changes. Change management spans all components of a data warehouse and thus plays a vital role in the ongoing development and overall success of a data warehouse. To manage the data warehouse, it is necessary to balance two conflicting environment goals: maximizing the use of the data warehouse asset while consistently achieving user expectations by continuously monitoring the effect of business changes.

To study the need for a metadata warehouse, we focus on the academic data of TIP. Changes happen in two ways: push and pull. In the push-oriented changes, changes happen at the data source level. Changes from these sources can occur each reporting period, typically a semester, and are the primary reason the academic subject area of the TIP is the most volatile. Because this data source is outside the control of TAMUS, changes are pushed to the TIP with limited opportunity for feedback and thus are implemented after the fact.

On the other hand, in pull-oriented changes, the changes are actually at the end-user level. Any changes in the end-user requirements will pull the changes in the different metadata in TIP data warehouse.

A sample of these changes is shown in Fig. 9. These changes can happen at any level of the schema (a metadata). For example, the changes can happen at the domain level, at the attribute level, or at the entityrelationship level. Therefore, having a change management tool will greatly improve the identification of the effect of the changes and aid in automation of implementing the changes throughout the process.

4.4. Why do we need a metadata warehouse for the TIP project?

Just as the data warehouse project was initiated in response to business decision support, so also the development of a metadata warehouse must also be driven by business needs. Some of these business needs related to the changes in TIP metadata are described below:

Tracking the life cycle for each data element. The ability to provide life cycle information for each data element—from data source to end-user representation, such as source field name, ETL processing, target table definition and representation to end-user (including transformations and derived columns).

\- Analyzing the effect of changes in TIP. This changed information can be used to analyze the impact of a change. Knowing the source field name aids in the analysis of the effect of a change to the TIP whenever changes to the source system occur. In addition, knowing the ETL processing can help determine the impact of changing a source field. We provide two examples to describe the effects of changes:

 Change of a two-character field to a fourcharacter field, as was the case with the ‘‘year’’ attribute in the cbm001 data source in September 1999, only affected the load elements of the TIP (load scripts, staging tables and transform <?xml version="1.0" ?> <ERwin4 FileVersion="4002"> <Model id="{A0DB7B80-A128-11D5-8E31-00D0590E52FE}+00000000" ModelType="3" TargetServer="190" DBMSVersion="2" DBMSMinorVersion="0"> <ModelProps> <Name>TIP metadata</Name> <Type RO="Y">3</Type> <File\_Name RO="Y">C:\My Documents\DW Project\TIP\_metadata.xml</File\_Name> <Page\_Grid>1</Page\_Grid> <File\_Format RO="Y">3228</File\_Format> <Entity\_Width>0</Entity\_Width> <Entity\_Height>0</Entity\_Height> <Layout\_Grid>1</Layout\_Grid> <Layout\_Grid\_X>15</Layout\_Grid\_X> <Layout\_Grid\_Y>15</Layout\_Grid\_Y> <Font Height>16</Font Height> <Font\_Width>5</Font\_Width> <Unique\_Names>3</Unique\_Names> <Target\_Server RO="Y">190</Target\_Server> <Default\_Datatype>CHAR(1)</Default\_Datatype> <Non\_Key\_Null>0</Non\_Key\_Null> <Repos>50</Repos> <DBMS Version RO="Y">2</DBMS Version> <Logical\_Notation>0</Logical\_Notation> <Display Split Rel Names>false</Display Split Rel Names> <DBMS\_Minor\_Version RO="Y">0</DBMS\_Minor\_Version> <USEDUMP>0</USEDUMP> <Old\_Repos>50</Old\_Repos> <Max\_View\_Expr\_Display\_Len>20</Max\_View\_Expr\_Display\_Len> <Physical\_Notation>0</Physical\_Notation> <Index\_Name\_Macro>X%KeyType%TableName</Index\_Name\_Macro> <Max\_Def\_Display\_Len>40</Max\_Def\_Display\_Len> <Table Name Macro>%EntityName()</Table Name Macro> <Current Tool>true</Current Tool> <MM\_Preview>true</MM\_Preview> <Saved From Previous Version>false</Saved From Previous Version> <Model\_Background\_Color>16777215</Model\_Background\_Color> </ModelProps> <Entity\_Groups> <Entity id="{A0DB8AD1-A128-11D5-8E31-00D0590E52FE}+000000AF" Name="SUMMARY TRANSACTION"> <EntityProps> <Name>SUMMARY TRANSACTION</Name>

Fig. 5. A partial XML description of physical ERD in TIP data warehouse.

scripts) as the target table column was already defined as an integer data type.

 Deletion of ‘‘Nursing Program Acceptance’’ data element in the cbm001 data source caused two major changes. It affected the load scripts and the transform scripts. However, the target table schema and view definition remain unchanged because the historical values need to be maintained. This change is then classified as having an average impact.

![](/api/attachments/FTR73KGA/fulltext/images/a231133312ac9dba5f393e855b732bc5f2b4ec46e5bc3bbf154f23079e789402.jpg)  
Fig. 6. A partial target table DDL in TIP data warehouse.

\- Merging of current data with historical data. As source data elements slowly change over time, there is a need to merge the changing data definitions with the existing historical data definitions in a meaningful way for the user. This merge should include strategies for handling null values because new attributes will not have values in the historical data. For example, the ‘‘Appointment 0.1%—Salary’’ data element in the cbm008 data source was deleted and replaced with other salary data elements at a completely different level, that is, instead of relating salary to the faculty appointment, salary became related to the funding source (e.g. State Appropriations, Auxiliary Enterprises, Restricted, etc.). In this case, because there was no basis for comparing the existing historical salary data with the new salary definition, columns containing the new data were added in addition to retain the existing salary columns to facilitate historical comparisons.

\- Identifying and archiving obsolete data elements. Some data elements become obsolete and do not provide any business value after a given period of time. These elements need to be identified and archived to historical tables. The archived obsolete elements can then be used for comparative historical trend analysis. For example, the ‘‘Nursing Program Acceptance’’ data element in the cbm001 data source is no longer being used in analysis and is eligible for archival.

![](/api/attachments/FTR73KGA/fulltext/images/c0a44dcede8caea633c5ec0efd5dd679e59d8b0d70720380f81ebf07d3721d63.jpg)  
Fig. 7. A partial user view DDL in TIP data warehouse.

\- Identifying required data elements to be used in analysis of new data sources. As new data sources are incorporated into the TIP, the data warehouse needs to have some ability to analyze gaps between the required data elements and the data elements provided by the new data source. The gaps can occur at the source (new data source) or target (TIP). Identification of the gaps can be used to drive changes to meet necessary business requirements. This is especially true for other areas of the TIP, where there are foreign key relationships and required attributes, such as the account data in the financial subject area. Incorporating additional data sources into the existing data model has uncovered gaps in both the new data sources, that is, data elements that are not stored in the source systems, as well as gaps in the TIP, that is, data elements not originally modeled.

## 4.5. Metadata warehouse architecture

Using Inmon’s data warehouse definition [7], we define a metadata warehouse as a subject-oriented, integrated, time-variant and somewhat volatile collection of metadata in support of change management process. Like repository, a metadata warehouse stores the warehouse metadata in a database, needs to have a common information model and provides version control. However, unlike repositories, the main focus of a metadata warehouse is to manage changes that continuously happen in the metadata. Typically, these changes in the metadata ripple throughout the entire metadata base.

<table><tr><td>Universe Name</td><td>Class Name</td><td>Object Name</td><td>SELECT Clause</td><td>FROM Clause</td></tr><tr><td>CBM_Reports</td><td>CBM_Class</td><td>Class Row Count</td><td>count(TAMUS_BASE.CBM_CLASS.fice_cd)</td><td>TAMUS_BASE.CBM_CLASS</td></tr><tr><td>CBM_Reports</td><td>CBM_Class</td><td>Record Cd</td><td>TAMUS_BASE.CBM_CLASS.record_cd</td><td>TAMUS_BASE.CBM_CLASS</td></tr><tr><td>CBM_Reports</td><td>CBM_Class</td><td>Fice Cd</td><td>TAMUS_BASE.CBM_CLASS.fice_cd</td><td>TAMUS_BASE.CBM_CLASS</td></tr><tr><td>CBM_Reports</td><td>CBM_Class</td><td>Subject Prefix</td><td>TAMUS_BASE.CBM_CLASS.subject_prefix</td><td>TAMUS_BASE.CBM_CLASS</td></tr><tr><td>CBM_Reports</td><td>CBM_Class</td><td>Course Nbr</td><td>TAMUS_BASE.CBM_CLASS.course_nb</td><td>TAMUS_BASE.CBM_CLASS</td></tr><tr><td>CBM_Reports</td><td>CBM_Class</td><td>Section Nbr</td><td>TAMUS_BASE.CBM_CLASS.section_nbr</td><td>TAMUS_BASE.CBM_CLASS</td></tr><tr><td>CBM_Reports</td><td>CBM_Class</td><td>Type Instr</td><td>TAMUS_BASE.CBM_CLASS.type_instr</td><td>TAMUS_BASE.CBM_CLASS</td></tr><tr><td>CBM_Reports</td><td>CBM_Class</td><td>Sch</td><td>TAMUS_BASE.CBM_CLASS.sch</td><td>TAMUS_BASE.CBM_CLASS</td></tr><tr><td>CBM_Reports</td><td>CBM_Class</td><td>Loc Cd</td><td>TAMUS_BASE.CBM_CLASS.loc_cd</td><td>TAMUS_BASE.CBM_CLASS</td></tr><tr><td>CBM_Reports</td><td>CBM_Class</td><td>Off Campus Loc</td><td>TAMUS_BASE.CBM_CLASS.off_camps_usc_loc</td><td>TAMUS_BASE.CBM_CLASS</td></tr><tr><td>CBM_Reports</td><td>CBM_Class</td><td>Composite Class Cd</td><td>TAMUS_BASE.CBM_CLASS.composite_class_cd</td><td>TAMUS_BASE.CBM_CLASS</td></tr><tr><td>CBM_Reports</td><td>CBM_Class</td><td>Tenure</td><td>TAMUS_BASE.CBM_CLASS.tenure</td><td>TAMUS_BASE.CBM_CLASS</td></tr><tr><td>CBM_Reports</td><td>CBM_Class</td><td>Off Campus Cd</td><td>TAMUS_BASE.CBM_CLASS.off_camps_usc_cd</td><td>TAMUS_BASE.CBM_CLASS</td></tr><tr><td>CBM_Reports</td><td>CBM_Class</td><td>Instructor Cd</td><td>TAMUS_BASE.CBM_CLASS.instructor_cd</td><td>TAMUS_BASE.CBM_CLASS</td></tr><tr><td>CBM_Reports</td><td>CBM_Class</td><td>Resp Factor</td><td>TAMUS_BASE.CBM_CLASS.resp_factor</td><td>TAMUS_BASE.CBM_CLASS</td></tr><tr><td>CBM_Reports</td><td>CBM_Class</td><td>Enrl Lower</td><td>TAMUS_BASE.CBM_CLASS.enrl_lowe</td><td>TAMUS_BASE.CBM_CLASS</td></tr><tr><td>CBM_Reports</td><td>CBM_Class</td><td>Enrl Upper</td><td>TAMUS_BASE.CBM_CLASS.enrl_uppe</td><td>TAMUS_BASE.CBM_CLASS</td></tr><tr><td>CBM_Reports</td><td>CBM_Class</td><td>Enrl Master</td><td>TAMUS_BASE.CBM_CLASS.enrl_master</td><td>TAMUS_BASE.CBM_CLASS</td></tr><tr><td>CBM_Reports</td><td>CBM_Class</td><td>Enrl Doctoral</td><td>TAMUS_BASE.CBM_CLASS.enrl_doctoral</td><td>TAMUS_BASE.CBM_CLASS</td></tr><tr><td>CBM_Reports</td><td>CBM_Class</td><td>Enrl Prof</td><td>TAMUS_BASE.CBM_CLASS.enrl_prof</td><td>TAMUS_BASE.CBM_CLASS</td></tr><tr><td>CBM_Reports</td><td>CBM_Class</td><td>Semester</td><td>TAMUS_BASE.CBM_CLASS.semester_id</td><td>TAMUS_BASE.CBM_CLASS</td></tr><tr><td>CBM_Reports</td><td>CBM_Class</td><td>Year Id</td><td>TAMUS_BASE.CBM_CLASS.year_id</td><td>TAMUS_BASE.CBM_CLASS</td></tr><tr><td>CBM_Reports</td><td>CBM_Class</td><td>Acad Year</td><td>TAMUS_BASE.CBM_CLASS.acad_year</td><td>TAMUS_BASE.CBM_CLASS</td></tr><tr><td>CBM_Reports</td><td>CBM_Class</td><td>Enrl Ug</td><td>TAMUS_BASE.CBM_CLASS.enrl_ug</td><td>TAMUS_BASE.CBM_CLASS</td></tr><tr><td>CBM_Reports</td><td>CBM_Class</td><td>Enrl Develop</td><td>TAMUS_BASE.CBM_CLASS.enrl_deve_lon</td><td>TAMUS_BASE.CBM_CLASS</td></tr></table>

Fig. 8. A partial business object universe in TIP data warehouse.

From the earlier case study, we observe two things. First, the size of the metadata used by the data warehouse is not small. In fact, currently in the TIP project, the academic part of the data warehouse is 331 MB, while its metadata is about 1

MB. This is very typical in all data warehouses. Second, the metadata in the TIP project can grow as it goes through a lot of changes. This kind of volatility is somewhat uncharacteristic of a regular data warehouse. These changes are important and need to be managed. This section discusses three possible architectures of a metadata warehouse. The first type uses existing data warehouse techniques, the second type extends the repository technique and the third type combines these two. We now describe these architectures with their advantages and disadvantages.

<table><tr><td>metadata_type</td><td>Metadata_name</td><td>change_type</td><td>change_location</td><td>affected_location</td><td>change_name</td><td>change_date</td><td>old_value</td><td>new_value</td></tr><tr><td>Data Source</td><td>cbm001</td><td>M</td><td>attribute</td><td>Load Scripts</td><td>Date of Birth</td><td>9/1/99</td><td>char(8)</td><td>char(6)</td></tr><tr><td>Data Source</td><td>cbm001</td><td>D</td><td>attribute</td><td>Load Scripts</td><td>Nursing Program Acceptance</td><td>9/1/99</td><td>char(2)</td><td>NULL</td></tr><tr><td>Data Source</td><td>cbm001</td><td>D</td><td>attribute</td><td>Load Scripts</td><td>SCH-Undergraduate Excess Load</td><td>9/1/99</td><td>char(2)</td><td>NULL</td></tr><tr><td>Data Source</td><td>cbm001</td><td>D</td><td>attribute</td><td>Load Scripts</td><td>SCH-Developmental Excess Load</td><td>9/1/99</td><td>char(2)</td><td>NULL</td></tr><tr><td>Data Source</td><td>cbm001</td><td>A</td><td>attribute</td><td></td><td>SCH-Collegiate Not State Funded</td><td>9/1/99</td><td></td><td></td></tr><tr><td>Data Source</td><td>cbm001</td><td>A</td><td>attribute</td><td></td><td>SCH-Developmental Not State Funded</td><td>9/1/99</td><td></td><td></td></tr><tr><td>Data Source</td><td>cbm001</td><td>A</td><td>attribute</td><td></td><td>SCH-Inter-Institutional Not State Funded</td><td>9/1/99</td><td></td><td></td></tr><tr><td>Data Source</td><td>cbm001</td><td>A</td><td>attribute</td><td></td><td>SCH-Collegiate State Funded</td><td>9/1/99</td><td></td><td></td></tr><tr><td>Data Source</td><td>cbm001</td><td>A</td><td>attribute</td><td></td><td>SCH-Developmental State Funded</td><td>9/1/99</td><td></td><td></td></tr><tr><td>Data Source</td><td>cbm001</td><td>A</td><td>attribute</td><td></td><td>SCH-Undergraduate Degree Program</td><td>9/1/99</td><td></td><td></td></tr><tr><td>Data Source</td><td>cbm001</td><td>A</td><td>attribute</td><td></td><td>Student Affected by UG Funding Limit</td><td>9/1/99</td><td></td><td></td></tr><tr><td>Data Source</td><td>cbm001</td><td>A</td><td>attribute</td><td></td><td>Last Name</td><td>9/1/99</td><td></td><td></td></tr><tr><td>Data Source</td><td>cbm001</td><td>A</td><td>attribute</td><td></td><td>First Name</td><td>9/1/99</td><td></td><td></td></tr><tr><td>Data Source</td><td>cbm001</td><td>A</td><td>attribute</td><td></td><td>Middle Name Initial</td><td>9/1/99</td><td></td><td></td></tr><tr><td>Data Source</td><td>cbm001</td><td>A</td><td>attribute</td><td></td><td>SCH-Dual Credit</td><td>9/1/00</td><td></td><td></td></tr><tr><td>Data Source</td><td>cbm001</td><td>A</td><td>attribute</td><td></td><td>Teacher Education Program</td><td>9/1/00</td><td></td><td></td></tr><tr><td>Data Source</td><td>cbm001</td><td>M</td><td>attribute</td><td>Load Scripts</td><td>Unused</td><td>9/1/00</td><td>char(6)</td><td>char(11)</td></tr><tr><td>Data Source</td><td>cbm001h</td><td>M</td><td>attribute</td><td>Load Scripts</td><td>Date of Birth</td><td>1/1/00</td><td>char(6)</td><td>char(8)</td></tr><tr><td>Data Source</td><td>cbm001h</td><td>M</td><td>attribute</td><td>Load Scripts</td><td>Doctoral Hours Funded</td><td>1/1/00</td><td>char(2)</td><td>unused</td></tr><tr><td>Data Source</td><td>cbm001h</td><td>M</td><td>attribute</td><td>Load Scripts</td><td>Doctoral Funding Code</td><td>1/1/00</td><td>char(2)</td><td>unused</td></tr><tr><td>Data Source</td><td>cbm001h</td><td>M</td><td>attribute</td><td>Load Scripts</td><td>SCH-Developmental Not State Funded</td><td>1/1/00</td><td>char(2)</td><td>unused</td></tr><tr><td>Data Source</td><td>cbm001h</td><td>M</td><td>attribute</td><td>Load Scripts</td><td>SCH-Developmental State Funded</td><td>1/1/00</td><td>char(2)</td><td>unused</td></tr><tr><td>Data Source</td><td>cbm001h</td><td>A</td><td>attribute</td><td></td><td>FTE Student</td><td>1/1/00</td><td></td><td></td></tr><tr><td>Data Source</td><td>cbm001h</td><td>A</td><td>attribute</td><td></td><td>School or College</td><td>1/1/00</td><td></td><td></td></tr><tr><td>Data Source</td><td>cbm001h</td><td>A</td><td>attribute</td><td></td><td>Remote Teaching Site</td><td>1/1/00</td><td></td><td></td></tr><tr><td>Data Source</td><td>cbm001h</td><td>A</td><td>attribute</td><td></td><td>RN Nursing Program</td><td>1/1/00</td><td></td><td></td></tr><tr><td>Data Source</td><td>cbm001h</td><td>M</td><td>attribute</td><td>Load Scripts</td><td>Unused</td><td>1/1/00</td><td>char(1)</td><td>char(9)</td></tr><tr><td>Data Source</td><td>cbm004</td><td>M</td><td>attribute</td><td>Load Scripts</td><td>Other Higher Education Site</td><td>9/1/99</td><td>char(9)</td><td>char(6)</td></tr><tr><td>Data Source</td><td>cbm004</td><td>A</td><td>attribute</td><td></td><td>Enrollment - Lower Level Affected by UG Limit</td><td>9/1/99</td><td></td><td></td></tr><tr><td>Data Source</td><td>cbm004</td><td>A</td><td>attribute</td><td></td><td>Enrollment - Upper Level Affected by UG Limit</td><td>9/1/99</td><td></td><td></td></tr><tr><td>Data Source</td><td>cbm004</td><td>A</td><td>attribute</td><td></td><td>Instruction Mode</td><td>9/1/99</td><td></td><td></td></tr><tr><td>Data Source</td><td>cbm004</td><td>A</td><td>attribute</td><td></td><td>Inter-institutional Identifier</td><td>9/1/99</td><td></td><td></td></tr><tr><td>Data Source</td><td>cbm004</td><td>A</td><td>attribute</td><td></td><td>Unused</td><td>9/1/99</td><td></td><td></td></tr><tr><td>Data Source</td><td>cbm005</td><td>M</td><td>attribute</td><td>Load Scripts</td><td>Year</td><td>9/1/99</td><td>char(2)</td><td>char(4)</td></tr><tr><td>Data Source</td><td>cbm005</td><td>A</td><td>attribute</td><td></td><td>Enrollment - Students whose Undergraduate SCH Exceed State Funding Limit</td><td>9/1/99</td><td></td><td></td></tr></table>

Legend: A — Addition; D - Deletion; M — Modification  
Fig. 9. A partial list of changes in TIP data warehouse metadata.

## 4.5.1. Type 1 approach (using data warehouse architecture)

Like in a regular data warehouse, the metadata are gathered from various metadata sources. The metadata sources include descriptions of traditional data sources, load scripts, logical and physical data models, staging table definitions and data warehouse table definitions, view definitions and definitions used in end-user applications. The metadata come in different formats and are extracted from these sources by using some specialized extract, transfer and load (ETL) tool. They are then temporarily stored in an area called Metadata Staging area. It is actually the construction site of the metadata warehouse. Flat files or relations are typically used in the metadata staging area. After the extraction is done, metadata sets need to be cleaned, standardized, duplicates removed, integrated and transformed by using the ETL tool. Once we are satisfied with the quality of the metadata, we again use ETL tool to load the metadata warehouse (see Fig. 10). Currently, not much is available in metadata ETL tools domain.

The metadata warehouse needs to be located in a metadata warehouse server. A metadata warehouse server uses a relational database management system (like NCR’s Teradata, IBM’s DB2, Microsoft’s SQL Server or Oracle’s Oracle 9i). The logical and physical models for the metadata warehouse must support the metadata descriptions and their changes. The models are translated to three NF relations before storing them in a DBMS. The models can be designed from scratch or can use some generic template. These relations are used with specialized query-processing capabilities that support decision support activities, indexing capabilities and reside on very fast processors. The metadata warehouse typically spans the entire enterprise. We feel managing version control can become a serious problem in this kind of metadata warehouse.

Finally, a metadata warehouse provides end-user facilities for various types of metadata access and reporting. These tools need to allow decision support queries with respect to change management, provide mechanisms to manage metadata changes and finally, to allow the metadata to be evaluated. The end-user tools for the metadata warehouse are also not well developed. Most vendors like NCR and others provide simplistic browsing facilities through the metadata.

![](/api/attachments/FTR73KGA/fulltext/images/b077137453f7757a898762901d52b0265be093702b8910e1afab1866254b7ab2.jpg)  
Fig. 10. The metadata warehouse architecture (Type 1 approach).

## 4.5.2. Type 2 approach (using repository-based architecture)

The advantage of using repository-based architecture is to make use of some of its salient features such as version control (to manage changes), inherent information model to design the metadata warehouse model, cross-platform support (i.e. the integration of tool metadata), event management and others. The architecture (see Fig. 11) is very similar to Fig. 9, but uses repository engine as the main tool. The metadata sources use the specialized ETL-like tools to bring the metadata into the staging or holding area. The staging area is very much like we see in a warehouse. It again uses temporary storage and does not use any repository infrastructure. The metadata warehouse is designed using an information model and then implemented on top of the repository tables. The end-user tools in this case use standard repository tools to provide the repository-styled decision support capabilities.

## 4.5.3. Type 3 approach (using integrated architecture)

Both techniques described above have their advantages and disadvantages. We propose here an integration framework that takes the best of both worlds. We capture the ETL tools, the concept of data staging and some end-user tools ideas from Type 1 architecture. We then connect these with the benefits of Type 2 architecture to get the use of repository engine, version control mechanism and integration framework for tool metadata that is inherent in the repository world. The

![](/api/attachments/FTR73KGA/fulltext/images/5765e35de65ae77b46d33787735305f1016d5d5ca1da0dfa97a75c8adcc1a4c3.jpg)  
Fig. 11. The metadata warehouse architecture (Type 2 approach).

![](/api/attachments/FTR73KGA/fulltext/images/923dcced1900cbf3f91037b1a18516e8f2a797596de74ee6b718c9467e8033ca.jpg)  
Fig. 12. The metadata warehouse integrated architecture (Type 3 approach).

emphasis on CWM can be achieved through the repository technology also. The result of this kind of integration can be seen in Fig. 12.

## 5. Conclusion and future research

While TIP Data Warehouse is a specific data warehouse, the need for metadata warehouse is universal. We see its need in the web data warehouses also. In fact, the changes are much more prevalent in the web world than in the regular data warehouse world [21]. The current research provides a window to show how metadata has come of age and now demands its own warehouse. Several conclusions and future research can be drawn from the Metadata Warehouse Proposal for the TIP project.

First, the major challenge in the metadata warehouse is to develop a design methodology that can capture the metadata scattered in the data warehouse projects and put them in the metadata warehouse. It is unclear at this time how that can be done. Will the design methodology follow any data warehouse design technique or will it be a new one?

Second, the design and development of ETL tools for the metadata warehouse need to be done. It is somewhat unusual to make use of the current ETL tools for the metadata. We feel that the metadata is quite different from regular data and needs to be treated differently.

Third, the end-user tools need to be developed for the metadata warehouse. As one can see in Fig. 12, end-users activities for a metadata warehouse span from version control (a repository activity) to change management decision support (a warehouse-type activity). We may need to drill down or drill up the data for end-users very much like we do in a regular data warehouse. Current repository-based tools (see Fig. 11) do not have these choices.

Fourth, it is obvious that the Type 3 architecture is the best of both worlds. Unfortunately, none of the current data warehouse and repository vendors implement this architecture.

Fifth, as indicated before, the metadata warehouse becomes a big problem in a web world. The reason is the incessant changes that happen in the website, starting the site structure changes, page content changes to the click-record log format changes and others. To manage all these changes, metadata warehouse seems to be the answer.

Finally, the question of integrating the metadata warehouse with the existing data warehouse is very important. As the metadata warehouse is a new phenomenon, we need to figure out how to incorporate it with the existing data warehouse. Will the metadata warehouse be kept apart from the data warehouse, or will it be integrated with it?

## Acknowledgements

The research was partially funded by a grant from Teradata, a division of NCR. The author acknowledges the help of Debbie Doran from the Texas A&M University System, and David Riegel and Mary Gros from Teradata.

## References

[1] F. Banchilhon, C. Delobel, P. Kanellakis, Building an Object-Oriented Database System, Morgan Kaufmann Publishers, San Mateo, CA, 1992.

[2] P.A. Bernstein, Repositories and object-oriented databases, SIGMOD Record 27 (1) (1998 March) 88– 96.

[3] C.J. Date, An Introduction to Database Systems, Addison-Wesley Publishing, New York, 1995.

[4] A. Deshpande, D. Van Gucht, An implementation for nested relational databases, Tech Report Number 234, Department of Computer Science, Indiana University, February 1988.

[5] D. Doran, TIP management change repository, An Internal Report, Texas A&M University System, 2001.

[6] E. Gamma, R. Helm, R. Johnson, J. Vlissides, Design Patterns: Elements of Object-Oriented Software, Addison-Wesley Publishing, New York, 1995.

[7] W.H. Inmon, Building Data Warehouse, Wiley, New York, 1992 and 1996.

[8] R. Kimball, L. Reeves, M. Ross, W. Thronthwaite, The Data Warehouse Lifecycle Toolkit, Wiley, New York, 1998.

[9] M. Leiter, S. Meyer, S.P. Reiss, Support for maintaining object-oriented programs, Transactions on Software Engineering 18 (12) (1992) 1045 – 1052.

[10] P.K. Linos, V. Courtois, A toolset for maintaining hybrid C++ programs, Software Maintenance Research and Practice 8 (1996) 389 – 419.

[11] D. Marco, Building and Managing Meta Data Repository: A Full Life Cycle Guide, Wiley, New York, 2000.

[12] D. Marco, Meta data repositories: where we’ve been and where we’re going, DM Review, February 2002. http:// www.dmreview.com/master.cfm?NavID=198&EdID=4612.

[13] Y. Matsumoto, A software factory: an overall approach to software production, in: P. Freedman (Ed.), Software Reusability, Computer Society Press, Los Alamitos, CA, 1987, pp. 155 – 178. http://www.computer.org/cspress/.

[14] J.-M. Morel, J. Faget, The REBOOT environment, Proceedings of Advances in Software Reuse, Lucca, Italy, March 24 – 26, IEEE Computer Society Press, Los Alamitos, CA, 1993, pp. 80–88.

[15] M. Pace, Evaluation and Comparison of C+ Class Libraries, http://www.desy.de/user/projects/C++/Projects.html.

[16] P.J. Plauger, The Standard C Library, Prentice-Hall, Englewood Cliffs, NJ, 1992.

[17] J. Poole, D. Change, D. Tolbert, D. Mellor, Common Warehouse Metamodel, Wiley, New York, 2002.

[18] R. Prieto-Diaz, A software classification scheme, PhD Thesis, University of California, Irvine, 1985.

[19] D. Reed, Tools for software reuse, Object Magazine (1995 February) 63 – 67.

[20] H.-J. Schek, M.H. Scholl, The relational model with relationvalued attributes, Information Systems 11 (4) (1986).

[21] A. Sen, Metadata warehousing: a methodological support to data warehouse change management, Working Paper, Texas A&M University, 2002.

[22] I. Sommerville, Software Engineering, Addison-Wesley Publishing, New York, 1992.

[23] K. Watterson, More than databases, repositories should hold the Corporate IS Jewels. Why don’t they? Byte Magazine, (1998 May) 1 – 9.

![](/api/attachments/FTR73KGA/fulltext/images/19d7e14659352c89767720e43cfe51309976c61c1cd88571651f422d2849be71.jpg)

Arun Sen is a full professor and Mays Fellow in the Department of Information and Operations Management in Texas A&M University. Before joining the Texas A&M University in 1986, he was an assistant and a tenured associate professor in the Department of Management Science, University of South Carolina. He holds an MTech in Electronics (from Calcutta University, India in 1971), an MS in Computer Science (from Penn State University in

1976) and a PhD in Information Systems (from Penn State University in 1979).

He has published 42 research papers in many journals such as MIS Quarterly, Information Systems Research, IEEE Transactions on Systems, Man and Cybernetics, IEEE Transactions on Software Engineering, IEEE Transactions on Engineering Management, Decision Sciences, Communications of the ACM, Information Systems, Computers and OR, Omega, European Journal of Operations Research, Decision Support Systems, Journal of MIS, Information and Management and others. His research interests include decision support systems, database management, repository management and software reuse, case-based reasoning, technical and behavioral aspects of data warehouse and E-Commerce.

He was an associate editor of Journal of Database Management. He was a special issue editor for Decision Support Systems, Communications of the ACM, Database and Expert Systems with Application. He was the chair of INFORMS College on Information Systems, a program chair for the 1996 Workshop on Information Technology and Systems (WITS) Conference and a track chair (Decision Support Systems and AI track) for the 1996 National DSI Conference.
