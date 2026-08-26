---
otero_id: 17939
otero_key: "RQNJMAJS"
title: "Fundamentals of integrated dictionary/ directory systems"
authors: "Mary E.S. Loomis; Michael V. Mannino; Frank W. Allen"
year: "1981"
journal: "Information & Management"
doi: "10.1016/0378-7206(81)90047-1"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Fundamentals of Integrated Dictionary/Directory Systems

Mary E.S. Loomis $^{1}$ , Michael V. Mannino and Frank W. Allen $^{2}$

Department of Management Information Systems, The University of Arizona, Tucson, Arizona 85721, U.S.A.

One of the most potent tools available to support achievement of control over an organization's information resource is the Integrated Dictionary/Directory (D/D) System. Use of a D/D System can assist in data inventory management, cost control and improving resiliency to changing requirements. A D/D System is composed of a database (describing the information resource), retrieval and analysis capabilities, interfaces (enabling other software to access the D/D) and data management tools. Some D/D Systems are independent from other software packages; some either are dependent on or are actually embedded in other data management systems. D/D Systems provide functions to assist in interfacing the D/D to other software and loading the D/D with meta-data from other software. Use of a D/D System is a first step toward achieving control of the data resource.

Keywords: Dictionary/Directory System, Database management, information resource management

![](/api/attachments/RQNJMAJS/fulltext/images/45e69415e279e81d9fee071ae5eec83c7ed9024e874013200a68414c41eeecbf.jpg)

Frank W. Allen is an Assistant Professor of Management Information Systems at the University of Arizona and founder of Information Processing Resources, Inc., both in Tucson, Arizona, U.S.A. He previously served on the Computer Science Department faculty at the University of Mississippi from 1975 to 1977. Dr. Allen holds a B.S. degree from Louisiana State University and the M.S. and Ph.D. degrees in Computer Science from the University of Southwestern Louisiana, Lafayette, Louisiana, granted in 1975 and 1976, respectively. He has published articles in international journals and conferences in the research and applications areas of software engineering, database management, computer performance evaluation and management utilization of information systems.

![](/api/attachments/RQNJMAJS/fulltext/images/c923ab5d5b3747cce1aff168558a1124145f82074aba9dc5c14a2aacf80727a1.jpg)

Mary E.S. Loomis received a B.S. in Mathematics from Purdue University in 1969, an M.S. in Computer Science from U.C.L.A. in 1972, and a Ph.D. in Computer Science from U.C.L.A. in 1975. She has been an Assistant Professor of Management Information Systems at the University of Arizona since 1976, where she conducts research in problems of distributed database environments, database performance evaluation, and database design and teaches graduate-level courses in DBMS, distributed information systems, data structures and file organization, and business system programming methods. She has authored numerous research papers and has lectured extensively in the U.S.A. and in Europe. Dr. Loomis is a consultant to numerous organizations. She is a member of ACM, ACM SIGMOD, ACM SIGBDP, and SMIS.

![](/api/attachments/RQNJMAJS/fulltext/images/ccc39eeeef9e6fadb2f8e5e2db657c92e61f7892623c7a8683b63a6b55f0b9d5.jpg)

Michael V. Mannino received the BBA degree from The University of Cincinnati and the M.S. degree from The University of Arizona, Tucson in 1978 and 1981 respectively. He is presently working on a Ph.D. in Management Information Systems at The University of Arizona. His dissertation is in the area of heterogeneous database management. Mr. Mannino is a student member of the Association for Computing Machinery and the IEEE Computer Society.

## 1. Introduction

The concept of Information Resource Management (IRM) is that information is a vital asset of an organization; information should be invested in, controlled and valued like other resources. Management's ability to measure performance, to create bonds with the consumer, to gauge competitors' actions and to adapt to the marketplace depends on accurate timely and understandable data. Because data are expensive, they must be handled in such a way that they are correct and are available to produce needed information. Aspects of data handling include measurement, collection, transcription, validation, organization, storage, aggregation, update, retrieval and protection.

In recognition of the IRM concept and the difficulties of properly managing data, many firms have acquired data management software, such as Data Base Management Systems (DBMS), and have created data administration functions [9]. The ultimate objective of these efforts is to make the information resource resilient, flexible and adaptable to support decision-making activities. The following guidelines facilitate achieving this objective:

● Data must be represented and stored so that they are preserved for later access.

\- Data must be protected and managed so that they retain their value.

\- Data must be massaged and presented in forms that support users' decision-making styles.

The focus of this paper is the utility and structure of Dictionary/Directory (D/D) Systems. Readers who want additional background on aspects of D/D Systems that are not included here, e.g., the selection and evaluation of a D/D System, should consult [7,8,12,13,15]. A D/D System is one of the most potent tools available to support the DBMS and data administrator in achievement of these data management guidelines. Use of a D/D System can mean accomplishing a major step toward gaining control of the information resource.

## 2. D/D System Objectives

The fundamental responsibility of a D/D System is to manage meta-data, which is the name given to data that describe other data. A D/D System thus manages a description of an organization's information resource.

There are three ways that use of a D/D System can help an organization gain control over its data. (1) Inventory management. The D/D System provides an inventory of the data that comprise the resource and of the programs, transactions and screens used to access the resource. The inventory includes names, definitions, locations, storage formats, sizes and other characteristics. With this repository of information, standards for names, access, storage, security and validation can be implemented and enforced more easily. (2) Cost control. A D/D System helps to control the costs of developing and maintaining computer-based applications. A D/D System can provide an accurate and complete library of data definitions for use both in application programs and in canned program generators such as report writers and query processors. Maintenance efforts can also be facilitated through use of reports generated by the D/D System that help to predict the effects of change in one part of an information system on other parts of the system. (3) Resiliency. A D/D System improves the resiliency of the data resource to changes in the data processing environment. Achievement of data independence from the characteristics of a particular hardware and software environment allows the information resource to adapt to changing requirements [18].

At the heart of a D/D System is a database, called the D/D, that contains the actual meta-data that describe data, processes, interfaces, users and hardware. Note that the D/D does not contain actual object occurrences. For example, for the data element SOC-SEC-NO, the D/D might contain attributes such as length, type and value range, but it would not contain any actual social security number values.

As indicated by its name, a D/D functions as both a dictionary and as a directory. The dictionary use of a D/D facilitates the global use of data definitions in applications. For example, a terminal user can use a D/D to ascertain the names, meanings, headings, code descriptions and display formats of all elements within his domain. The D/D can provide descriptions of user data to a DBMS. The directory use of a D/D permits applications to access stored data without concern for their physical locations or characteristics. Applications programmers can rely on D/D System support to ensure proper access authorization, to convert nonprocedural requests into physical access calls and to return data in appropriate formats.

Originally, D/D Systems emphasized only the dictionary utility of a D/D. These D/D Systems featured extensive reporting capabilities that expedited the design, maintenance and use of applications. For example, the typical D/D System provided a listing of all programs that referenced a specified element. Thus an analyst quickly knew which programs to recompile if a format change occurred. Because of this emphasis, the term "Data Dictionary System" was applied. More recently, the integration of the D/D with other software packages has been emphasized. An integrated D/D System permits other systems directly or indirectly to access the D/D and automatically converts the meta-data of these systems into the format of the D/D System.

As distributed database systems become more prevalent, the directory role of the D/D will continue to expand. The D/D can play a significant role in the management of transactions to a distributed database. Its contents can be used to determine where data are located, to plan transaction execution strategies, to coordinate multiple-site updates and to ensure adherence to validity and security controls. In the distributed environment, the D/D itself becomes a specialized distributed database.

Six groups of users can benefit directly from use of a D/D System:

(1) Data administrators, who use the system as a major tool for inventorying the data resource, implementing standards, and designing, monitoring and restructuring databases; (2) Application personnel, such as analysts and programmers, who use the system to reduce program coding efforts, to store the designs of evolving systems and to support analysis of system changes; (3) Operations staff, who retrieve information about jobs from the D/D; (4) Data processing management, who receive high-level impact and summary reports about data usage from the D/D; (5) End-users, who obtain descriptions of their data views from the D/D; and (6) Auditors, who examine and obtain data descriptions for use in auditing software.

## 3. D/D System Components

A D/D System can be viewed as a computer-based information system with four basic components:

\- A meta-data database (the D/D), also called a meta-base, that describes the data, processes, users, and processors of an organization;

\- Retrieval and analysis capabilities that assist a wide range of user groups in application development;

\- Functional interfaces that permit other software modules to access the D/D and that convert metadata from other software systems into the formats required by the D/D System;

\- Data management tools that help ensure the security, validity, recoverability, integrity and shared accessibility of the D/D.

## 3.1. The D/D Content

A typical D/D contains data that describe the following aspects of an organization's information resource: (1) Internal data, including data elements, logically related groups of data elements, reco files, databases and sub-sets of databases; (2) Input-Output, including user transactions, screens and reports; (3) Equipment, including computers, communications facilities and terminals; (4) Processes, including programs, modules, systems and manual procedures; (5) Users.

Some systems provide as many as 500 different attributes to describe the above-listed entities. Many of these attributes (especially those applicable to internal data and input-output) correspond to clauses found in data definition languages (DDLs) of DBMSs and in programming languages such as COBOL.

A turn-key D/D System may not meet the specific requirements of a particular organization, so an extensibility feature is often available from the vendor. This feature allows an organization to tailor its D/D structure by defining additional entities, relationships and attributes. Extensibility can be provided in two ways. In the simpler approach, the vendor supplies optional sets of objects, e.g., those required to describe a structured design methodology or a message-formatting environment. In the more dynamic approach to extensibility, the D/D System accommodates user-defined entities, relationships and attributes. User-defined entities are generally subject to constraints; for instance, a new entity may have to be special case of a pre-defined entity [15]. Clearly the second approach gives the user organization more flexibility of expression in the D/D, but results in a more complex D/D System.

Another important characteristic of a D/D is the ability for entity occurrences to exist in different states. For example, test status can be used to document evolving systems and uncompleted changes to productional systems. The file descriptions for a new program of an existing system have test status until the program is thoroughly tested. Production status occurrences; in the D/D reflect operational systems. Because the security of productional status information can be of concern, update access is usually reserved for the data administrator. Historic status reflects superseded meta-data, providing an audit trail of changes to the D/D. Version numbers may be used to allow multiple occurrences of one entity to exist in the D/D with the same status.

## 3.2. Retrieval and Analysis Capabilities

A typical D/D System includes two types of retrieval and analysis capabilities. The Report Processor function provides predefined reports, the ability to customize these reports and a user-defined reporting capability. Commonly predefined report types include: (1) Name listings such as keyword-in-context (KWIC) and keyword-out-of-context (KWOC), (2) Relationship reports, e.g., names of all the record types contained in a database, (3) Detail reports, e.g., descriptions for all elements with a common keyword, (4) Summary reports such as the compilation date, change description, number of source lines and the responsible programmer for all programs in a recent version of a subsystem, (5) Matrix reports such as type of access (input, output, input-output) to all files within a program, and (6) Graphical reports, e.g., showing the hierarchical structure of a program's logic. The vendor often provides a method to customize report formats. Sometimes the user can define new reports, commonly using the vendor's report writer. For example, users of Cullinane's Integrated Data Dictionary (IDD) [3] can define new reports using the CULPRIT report writer, which was written originally as an interface to IDMS, the DBMS on which IDD is implemented.

The Query Processor function of a D/D System allows natural-language-like (e.g., English, French, German) queries of the D/D. This query function for the D/D is analogous to the corresponding function in DBMSs for access to databases and is used for low-volume, interactive retrieval of information from the D/D.

## 3.3. Functional Interfaces

The benefits of a D/D System for controlling the information resource can be maximized if the D/D is the sole source of meta-data for the information system. A Software Interface function of a D/D System provides a formatted pathway enabling the D/D to provide meta-data to other software systems, such as compilers and DBMS DDL processors, and enabling these systems to retrieve and update information in the D/D. A software interface component might generate file descriptions for a program library; another might accept a user's identification code and then generate a copy of that user's database view from the D/D. Interface with a compiler might include generating file and record definitions that the compiler accepts via a copy statement.

Many software packages use their own, built-in meta-data files. The Convert Function of a D/D System reads application programs, libraries and schemas and generates input transactions that describe the detected meta-data. These transactions are then used to load data into the D/D. This automated conversion facility alleviates some of the problems of initially loading a D/D from the variety of sources of meta-data that may exist in an organization.

Clearly inconsistencies arise if changes are made to the D/D without changing the meta-data controlled directly by other software packages and vice versa. The better the D/D System is integrated with other software packages, the better is the potential for control of the information resource.

## 3.4. Data Management Tools

The D/D System has a variety of functions for purposes of managing the D/D. These functions, like the retrieval and analysis capabilities, actually may be provided by a DBMS that manages the D/D as well as user databases. Alternatively, the D/D System may provide its own data management support for the D/D.

```matlab
(A) Keyword driven language

ADD ELEMENT Customer-Number
    PASSWORD IS "XYZA";
    COBOL-NAME CUSTNUM;
    TYPE numeric;
    LENGTH 10;
    KEY OF custrecord;
    DISPLAY-FORMAT "99-999-99999";
    USAGE packed-decimal;
    DESCRIPTION;
    Customer-Number uniquely identifies each account holder. The first two digits identify the district, the next three the local branch, and the final five digits specify the customer;

(B) Fixed-format input

+ADD % ELEMENT, Customer-Number
1001 % PSWD = 'XYZA', CNAM = CUSTNUM, TYPE = num, LNGT = 10,
1002 % DEKY = 'custrecord', DFRM = '99-999-99999', USGE = pdec;
1003 % TEXT;
Customer-Number uniquely identifies each account holder. The first two digits identify the district, the next three the local branch, and the final five digits specify the customer.
1003 % ENDT

(C) Prompted input

GIVE FUNC (FUNCTION = NAME)
⇒ ADD ELE = Customer-Number
GIVE PASSWORD
⇒ 'XYZA'
GIVE COBOL-NAME
⇒ CUSTNUM
GIVE TYPE
⇒ n umeric
GIVE LENGTH
⇒ 10
```  
Fig. 1. Examples of D/D Maintenance Interfaces.

The D/D Maintenance function interprets and processes requests to add, modify or delete contents of the D/D. The prevalent maintenance functions provide a variety of languages to enable a data administrator to specify changes to the D/D. These interfaces include: (1) keyword-driven languages, (2) fixed-format transactions, (3) interactive, prompted input, and (4) interactive, preformatted screens or menus [7]. Fig. 1 illustrates the first three types of input.

The D/D Management function performs the usual database management tasks such as security, integrity, concurrency control and internal access for the D/D. Again, many D/D Systems utilize the service of an existing DBMS to provide aspects of this function.

The Extensibility function of a D/D System enables the D/D structure to be extended by the definition of additional entities, relationships and attributes. For example, a “clone” transaction could be used to add a new type of entity that has attributes identical to an existing entity type [15]. Other types of extensions may require more elaborate specification. For example, to add a totally new type of entity, it may be necessary to: (1) create the specification for a new transaction type, (2) create a file of occurrences of the new entity and (3) create specifications for additional relationships to be included in the D/D.

The Exit Facility of a D/D System enables extension of the vendor-supplied routines for processing the D/D. For example, the user organization might code additional validation constraints to be applied prior to deletion of an occurrence of a particular entity type from the D/D, or a new security check might be coded for use upon access to an attribute. An Exit Facility is not available in all D/D Systems because of the possible harmful side-effects that its use may introduce.

## 4. Environmental Dependence

The environmental dependence characteristic of a D/D System describes its reliance on a specific hardware configuration, an operating system, a DBMS and/or a teleprocessing monitor. Clearly the environmental dependence of a particular D/D System is a major factor in determining whether or not it will function in a particular organization.

Most interesting is environmental dependence of a D/D System on a DBMS. The extent of this dependence is determined by the degree to which the D/D System relies on the DBMS for data management services and on the source of meta-data used by the DBMS for access to user databases. The DBMS can obtain meta-data from either the D/D or its own directory or schema files.

There are three basic forms of environmental dependence between a D/D System and a DBMS (Fig. 2) [7,14]. (1) The systems may be independent. The D/D System is freestanding and does not rely on any particular DBMS. The DBMS maintains its own source of meta-data; the D/D System uses none of the DBMS utilities for data management. One benefit of this approach is that one D/D System may provide data control support in a variety of environments with different DBMSs. An example independent D/D System is DATAMANAGER, from MSP, Ltd. [10]. (2) The systems may be dependent, with the D/D appearing to the DBMS as just another database. The DBMS maintains its own meta-data, separate from the D/D. The DBMS utilities provide most of the D/D

(A) Independent Approach  
![](/api/attachments/RQNJMAJS/fulltext/images/c9f1523ee5ecd1dc69c3895922f47e39847352ccd37aa00fa6fdbd529b7a18fe.jpg)

![](/api/attachments/RQNJMAJS/fulltext/images/f7035e09183d3885fe97b77f412dd2e476f2d4a2b1371767c5d679f432b130c3.jpg)

(C) Embedded Approach

![](/api/attachments/RQNJMAJS/fulltext/images/90fdf5f26eef46b629c6665a1b4e3dc3575c1d08ce17eab97d19b168555474bc.jpg)  
Fig. 2. D/D System–DBMS Relationship.

management functions, but meta-data are defined separately for the DBMS and for the D/D System. In this approach, the D/D System interfaces primarily with one DBMS and its related components, but may pass meta-data to other DBMSs that operate on the same machine. An example dependent D/D System is DATADICTIONARY, from Applied Data Research, Inc. [1]. (3) The D/D System may be embedded in the DBMS. The DBMS utilities provide the D/D management facilities and the DBMS uses the D/D to direct access to user databases. No other internal directories exist for the DBMS; the DBMS and its related components rely completely on the D/D for meta-data. For example, a query processor extracts user views from the D/D and the DBMS applies integrity constraints specified in the D/D before storing a data element. Because the D/D System is actually a component of the DBMS, it clearly can be used only with that DBMS. An example embedded D/D System is DIRECTORY, from Cincom, which is the controlling element for Total Information Systems (TIS) [2].

## 5. Interfacing the D/D to other Software

The D/D System that is integrated with other software in an information system is better able to provide effective data control than one which is not. A D/D can provide meta-data to other software either statically or dynamically.

A static interface links the D/D with another system indirectly via the extraction of files of formatted meta-data. There is no run-time connection between the D/D and the other system. For example, a data administrator might enter into the D/D System all pertinent transactions to describe a database. After reviewing the accuracy of this database description, the data administrator could activate a D/D System command, e.g., GENERATE, that would use this description to produce a file containing DDL. The DBMS's DDL Processor then would translate this generated DDL into a schema file that the DBMS later could access.

Static interfaces differ somewhat depending upon whether they interface the D/D System with user-written programs or with vendor-supplied software packages. Static interfaces for user-written programs produce file, record and database descriptions in COBOL or PL/I terms for copy into user programs. These interfaces sometimes feature edit capabilities, format options and various other functions to make the interface more flexible.

Static interfaces for software packages, e.g., DDL processors, communication monitors and query processors, produce formatted statements for those packages or create specially encoded control files for their use. For example, a software interface of UCC's D/D System, UCC TEN [17], generates message and terminal description statements from its D/D for use by IBM's Message Format Service, while Cullinane's IDD [3] creates from its D/D the control file utilized by the IDMS-DC communications monitor. The options for customizing the D/D interface with these types of software packages are more limited than are the options provided for interface with user-written programs; the packages generally have more rigid language formats and the interface statements are generally used only by the data administrator.

A dynamic interface provides software modules with direct access to a D/D, commonly via high-level interface commands that shield the software package from the physical details of the D/D. The commands activate standard D/D System functions, e.g., to select all entity occurrences that satisfy a condition. Dynamic interfaces provide greater potential for data consistency control than do static interfaces. Changes to the D/D are reflected automatically in the next execution of any software packages to which the D/D is interfaced; no intervening procedures are required as are with static interfaces. A software package can directly retrieve and update meta-data stored in the D/D. All requests by software packages for meta-data are routed through the D/D System by a dynamic interface function. Thus the security and validity checks of the D/D System are always applied. A drawback of a dynamic interface is the performance degradation that may be caused by frequent access to a large D/D.

## 6. Converting to a D/D System

A typical organization that acquires a D/D System has hundreds or thousands of programs, reports and files to manage. Converting to a D/D System and loading the D/D with the meta-data to describe the information resource can be a formidable task if approached in a brute-force way by coding maintenance transactions to capture all the meta-data. Many D/D Systems provide convert functions that scan source programs, database descriptions and teleprocessing environment descriptions and automatically produce many of these transactions, thus sparing the data administrator many hours of manual effort. Actually, the data administrator must scrutinize these generated transactions for redundant and non-standard entries. For example, if the naming conventions used in source programs were previously uncontrolled, then the data administrator will find it necessary to change naming details in many of the generated transactions in order to impose standardization before loading the D/D.

Like the software interfaces provided to extract meta-data from a D/D, the convert functions are offered to load a D/D from both user-written programs and canned packages. For example, a D/D System may furnish conversion facilities for several programming languages (e.g., COBOL, PL/I, assembler), as well as for the DDL Processor and report writer of a given DBMS.

The input file to a convert function can be a source program or a library file. If the input is a source program, then the convert function can capture information about data usage by the program (e.g., the way a file is opened). If the input is a library file, then only the data descriptions that actually reside in the library file can be converted to the D/D format. Options for a convert function may include the ability to change names, to select lines to scan, to select types of transactions to create and to override generation of some types of meta-data [10,15].

Source program analysis for input of meta-data to the D/D involves intra-program and inter-program usage of data. Intra-program analysis detects the types of reference (e.g., input only, update) to data elements. Inter-program analysis scans code for adherence to standards and discloses inconsistencies in the names, formats and descriptions (e.g., initial values) of the data definitions used in several programs and the corresponding definitions in the D/D. Both types of analysis could be used to make the D/D in part self-generating; however the convert functions of commercial D/D Systems rarely examine procedure parts of source programs and therefore today perform only limited intra- and inter-program analysis.

## 7. Cautions

Over the last five years, D/D Systems have evolved into a tremendous tool for systems development. However, the effective use of a D/D System depends on a strong data administration commitment. Typically, a data administration group needs several years of experience before being able to use a D/D System effectively. The data administration group must have the support of top management in the form of a corporate charter, as well as high visibility in the organization. This support is difficult to obtain in many organizations. Application of a D/D System is facilitated when standards are already fully in place, e.g., standards pertaining to names, change control, program logic, and system design.

Even with a strong organizational commitment, an organization faces difficulties because of the limitations of commercially available D/D Systems. The command languages of most D/D Systems are not suitable interfaces for most users. Many organizations are clamoring for interfaces that a naive user can easily grasp. Organizations also are requesting more support from D/D Systems for system development methodologies [5]. Few D/D Systems today provide the reports, consistency checks and graphics capability required by the commonly used methodologies for systems design and development.

A related problem is created by the lack of support for an independent view of the information resource. Most D/D Systems support one or more DBMSs, communication monitors and programming languages, but do not support an enterprise model and the concept of an independent logical view. An enterprise model is a corporate-wide view of the business functions and information required to conduct those functions. The logical view describes the detailed application requirements, independent of any software products such as DBMSs or communication monitors [11]. The D/D System should facilitate the validation of an enterprise model against an organisation's logical data and application views.

An organization that is converting to a D/D System must face the difficult question of how extensively the D/D will pervade the data processing environment. Rather than retrofitting the D/D to include all applications areas, most organizations choose to apply their D/D Systems only to new application areas, letting the older systems run their courses to eventual replacement before entering the D/D. Other organizations tackle the job of converting all systems to D/D System support, thus providing better integration of the entire information resource. The tradeoff to be considered is the cost of retrofitting the D/D to old systems versus the problems of inconsistency and lack of control that may arise if the old systems are not converted.

A final problem is the control of multiple D/Ds. Ideally the D/D should be the single repository for describing the information resource, but many organizations operate with multiple D/Ds due to the inadequate performance of a single D/D and for political reasons. Few if any D/D Systems manage the access to and control of multiple D/Ds. Some firms have an even greater problem because of multiple

D/D Systems. Firms acquire multiple D/D Systems due to vendor pressures (e.g., the D/D System is included with the DBMS), for political reasons and to take advantage of product features. Peaceful co-existence of multiple D/D Systems is a not easily achieved goal in these heterogeneous environments.

## 8. Conclusions

The demand and supply of D/D Systems today are indicative of their growing significance in IRM. The fifteen largest D/D System vendors have installed approximately two-thousand systems, primarily in large organizations. Many other organizations utilize D/D Systems that were developed in-house; many even use manual systems. The potential demand for commercial D/D Systems seems vast because many of these home-grown systems are rudimentary in comparison to the commercially available D/D Systems. Many vendors have entered the D/D System market in the last few years and several additional D/D System offerings are planned. Today's D/D Systems are used primarily in fairly large configurations; tomorrow's also will invade the small computer market.

Integrated D/D Systems thus have important roles in controlling both centralized and distributed information resources. The benefits of a D/D System include increased control over the data, reduced cost and time requirements for application development and enhanced independence of meta-data across computing environments.

In the near future, development in eight related areas seems likely. (1) Vendors will release distributed DBMSs that are connected to their D/D Systems. Independent vendors will upgrade their D/D Systems to interface statically with other vendors' DDBMSs. (2) D/D Systems will support the prevalent systems development methodologies via graphics and enhanced reporting and control features. (3) Improved interfaces will be developed to accommodate naive users. (4) D/D Systems will evolve to support an enterprise model and DBMS-independent view of the information resource. (5) Design aids and performance evaluation software will interface with D/D Systems. (6) Standards for D/D Systems will emerge by 1984.

(7) D/D Systems will have the ability to manage multiple D/Ds. (8) Vendors will develop D/D Systems for use on small computers D/D System functions will migrate into operating systems of some of the small machines.

D/D Systems will play increasingly important roles in IRM. Use of a D/D System is a necessary first step toward achieving control of the data resource.

## References

[1] Applied Data Research, Inc. DATADICTIONARY User Reference Manual, 1979.

[2] Cincom Systems, Inc. TIS: A Technical Overview, 1980.

[3] Cullinane Corp. IDD User's Guide, 1978.

[4] R. Curtice and E. Dieckman, A survey of data dictionaries, Datamation, Vol. 27, 3, 1981, pp. 135–158.

[5] R. Curtice, Data Dictionaries: an assessment of current practice and problems, Proc. 7th Intl. Conf. on Very Large Data Bases, Cannes, France, 1981.

[6] DDSWP The British Computer Society Data Dictionary Systems Working Party Report, Data Base, Vol. 9, 2, 1977, ACM SIGBDP and SIGMOD Record, Vol. 9, 4, 1977.

[7] H. Lefkovits, Data Dictionary Systems, QED Information Sciences, 1977.

[8] J. Lomax, Data Dictionaries, National Computing Centre, Manchester, England, 1977.

[9] J. Lyon, The Database Administrator, John Wiley and Sons, 1976.

[10] MSP, Ltd. DATAMANAGER User's Guide, MSP Technical Documentation, 1980.

[11] H. Patel, How to upgrade a DBMS, Datamation, Sept. 1981, pp. 127–132.

[12] B. Plagman, Data dictionary/directory system: a tool for data administration and control, Auerbach Series on DBMS, Vol. 22-01-02, 1977.

[13] B. Plagman and Moss, C. Alternative architectures for active data dictionary/directory systems, Auerbach Series on DBMS, 22-04-02, 1978.

[14] E.H. Sibley, et al. The software configuration management database, Proc. Nat'l. Computer Conf., 1981, pp. 249--255.

[15] Synergetics Corp. DATA CATALOGUE 2 System Standard Facilities Manual, 1980.

[16] P. Uhrowczik, Data dictionary/directories, IBM Syst. J. Vol. 12, 4, 1973, pp. 332–350.

[17] University Computing Company, UCC TEN Concepts and Facilities, 1979.

[18] Wilson, T. (ed.) ANSI/X3/SPARC Database Systems Study Group - Standing Paper 1, Version 1.1, 1980.
