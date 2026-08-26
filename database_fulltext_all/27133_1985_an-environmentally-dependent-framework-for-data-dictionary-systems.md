---
otero_id: 27133
otero_key: "E7WJSAYC"
title: "An Environmentally Dependent Framework for Data Dictionary Systems"
authors: "Beverly K. Kahn"
year: "1985"
journal: "MIS Quarterly"
doi: "10.2307/248949"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
An Environmentally Dependent Framework for Data Dictionary Systems
Author(s): Beverly K. Kahn

Source: MIS Quarterly, Vol. 9, No. 3 (Sep., 1985), pp. 199-220

Published by: Management Information Systems Research Center, University of Minnesota

Stable URL: http://www.jstor.org/stable/248949

Accessed: 09/05/2014 08:19

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# An Environmentally Dependent Framework for Data Dictionary Systems

By: Beverly K. Kahn
Graduate School of Management
Boston University
Boston, Massachusetts

## Abstract

Data dictionary systems traditionally have been analyzed and compared against idealized standards that are independent of both the special requirements of the organization and the environment in which they will be used. This has resulted in the selection of data dictionary systems that appear to be the best product in terms of the features offered, but which may not be the most effective alternative for meeting the needs of the organization or supporting its data administration effort.

This article presents a new framework for analyzing data dictionary systems that encompasses environmental dependencies and organizational requirements. Also described is a structured methodology for selecting a data dictionary system based on this framework. This methodology is then applied to a bank holding company example.

Keywords: Data dictionary system, data administration, database management system, MIS
ACM Categories: H.2.4, H.2.7, H.4.0, K.6.3

## Introduction

Data administration (DA) is the establishment and enforcement of policies and procedures for managing data as a corporate resource. It involves the collection, storage, and dissemination of data as a globally administered and standardized resource. In data administration, as well as all other management functions, there are three levels of management: strategic planning, tactical planning/managerial control, and operational control [4]. Both strategic planning and tactical planning/managerial control activities of data administration rely on high quality data from operational control activities. Accordingly, the operational control activities are the foundation for planning and are the first priority of the data administration function.

A data dictionary system (DDS) is the single most important data administration tool [12] and, therefore, should be selected using a data administration perspective. A data dictionary system includes the data dictionary and a means for entering, modifying, and reporting its contents. A DDS is a mechanism for centralized control and management of information about the organization's data resource. A data dictionary is a repository of the information about the organization's data resource including the definition, structure, and use of data.

Today, an organization must select a DDS from a spectrum of commercially and internally developed products. No commercially available DDS can satisfy all of the requirements of every organization's data administration function. As a result, each organization is confronted with the task of evaluating a spectrum of products and selecting the one that comes closest to meeting its present and future needs. This selection should be given serious consideration and should be based on the requirements of the individual organization. According to Lefkovitz [21, p. 1, 2]:

"A data dictionary system is an information systems in its own right. . . . The decision to acquire and implement a data dictionary system and the selection of that system should follow the same sound principles that should be applicable to any other system. If anything, the process should be more stringent and subject to greater scrutiny, since mistakes can conceivably cause greater damage than those incurred with other application systems."

This article describes a structured methodology called the environmentally dependent framework (EDF) which improves upon the existing frameworks which do not consider the organizational and environmental aspects. Additionally, this framework identifies the fundamental characteristics of a DDS that constitute a minimum level of DDS functionality and of ease of use. In practice, EDF has been demonstrated to support and facilitate the DDS selection process.

## Existing Approaches

A recent survey by Kahn [18] showed that data dictionary systems were not being used to achieve the broad goals of data administration. No general reason for this occurrence emerged from the study. The failure of DDS's to support data administration was also identified by Nolan [25].

Contingency theory [15, 20] suggests the necessity of congruence of organizational arrangements (such as information systems) and the organization's environment. Applying this theory to data dictionary systems, a DDS that is incompatible with the organization's environment will not effectively support the organization. A DDS that does not fit its environment may be caused by the shortcomings of the DDS comparison and selection approach that was employed. Traditional approaches [3, 6, 11, 21, 22, 25] compare DDSs on a feature-by-feature basis against idealized criteria, independent of the organization's specific requirements and environment. EDF was found to be simpler to use because it structured the decision-making process. It was easier to comprehend and faster to learn because DDS features were directly related to organizational characteristics. It eliminated products from consideration earlier in the selection process and produced results that were reproducible, easy to defend, and directly related to the organization's data administration objectives.

## An Overview of the EDF

A refinement to this traditional, feature-by-feature analysis approach is to consider the organization's requirements and environment. Only the environmentally dependent framework does this, by relating the DDS to the organization's data administration and data management objectives, the organization's data management environment, and the planned uses of the DDS. Therefore, the EDF ensures that the data dictionary system selected will be compatible with the organization's requirements and environment.

This new framework also overcomes the shortcomings of earlier approaches by:

— structuring the decision-making (DDS selection) process,

— producing results that can be incorporated directly into the organization's selection process,

— providing a vehicle to determine whether the installation and use of a DDS is suitable and cost-beneficial, and

— providing a mechanism to determine how the DDS could satisfy the organization's data administration objectives.

## The Environmentally Dependent Framework

There are two types of requirements that must be considered when using the EDF. The environmentally dependent requirements consider both the operational control activities of data administration and the data management environment within the organization. This ensures that the DDS is compatible with the organization's data management environment and data administration objectives.

In addition to the environmentally dependent aspects of this framework, there are environmentally independent characteristics of a DDS called basic requirements. Basic requirements are those DDS features which constitute minimum functionality and which contribute to the ease of using the DDS. The basic requirements should be considered first in evaluating a DDS. The environmentally dependent framework developed and described herein consists of both the basic and environmentally dependent requirements.

(1) be easily maintainable, (2) provide easy to use reporting capabilities, (3) provide comprehensive definition and naming conventions, and (4) have adequate documentation.

## Basic requirements

A computerized data dictionary system provides a central repository for information about an organization's data and should be an efficient vehicle for accessing and managing that information. In order to be efficient, a DDS must

Certain features of data dictionary systems provide these key capabilities and meet the basic requirements of the framework. These are summarized in Table 1. Most, if not all, DDSs offer these features. However, the degree to which they are easy to use varies broadly. Most of the features included in Table 1 are self-explanatory. A comparison of commercial DDS's, with respect to the basic requirements, is summarized in Table 2. Those features related to nam-

## Table 1. Summary of the Basic Requirements

## Maintenance

\- Variety of methods (i.e., batch and interactive) for data entry and modification - Aids for data entry such as batch input, coding forms, and online display forms and prompts for interactive input

\- Flexible in approach to documenting systems (e.g., should be compatible with a variety of systems analysis and design techniques)

\- Simple to use

\- Flexible parameter specifications

\- Powerful and concise commands that are easy to use

\- Help facility

## Reporting

• Variety of standard reports

\- Ease in generating standard reports (in both batch and online modes)

\- Standard reports should be clear in purpose and suitable for system or application documentation (preferably in an 8½ by 11 format)

\- Query reporting capabilities for ad hoc reports

\- Reports useful to a broad spectrum of individuals (end user to technical users)

## Definition and Naming Conventions

\- Robust set of allowable characters and sufficient maximum length of object names

\- Range of object types

\- Flexible and comprehensive format of object definitions

\- Aliases

• Definition of organization—specific object characteristics

## Documentation

\- Comprehensive set of documentation manuals including management overview, user training as well as installation and operational problem solving

\- Easy to use and reference

\- Adequate use of examples

\- Useful and understandable to a broad spectrum of individuals

\- Adequate training, including interactive aids

\- Augmented and complemented by good vendor support and training ing and definition conventions require a more detailed explanation.

Table 2. Summary of Basic Requirements for Commercial Data Dictionary Systems

<table><tr><td colspan="9">Maintenance</td></tr><tr><td colspan="5">DATA ENTRY TECHNIQUE</td><td>DB/DC</td><td>DC/4</td><td>Data Manager</td><td>IDD</td></tr><tr><td>Batch only</td><td>Batch and On-line</td><td>Batch and Online improved</td><td>●</td><td></td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td colspan="3">COPYING FACILITY TO EXPEDITE DATA ENTRY</td><td>●</td><td></td><td>●</td><td>○</td><td>●</td><td>○</td></tr><tr><td colspan="9">LINKS BETWEEN ENTITIES:</td></tr><tr><td>Implicitly defined using defaults</td><td>●</td><td>Must be explicitly stated</td><td>●</td><td></td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td colspan="9">EASE OF BUILDING DSS:</td></tr><tr><td>Flexible</td><td>● Very Flexible</td><td>●</td><td>Must define entity before referencing</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td colspan="3">COMMANDS: ADD, DELETE AND CHANGE</td><td>●</td><td></td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td colspan="9">TEXT UPDATE METHOD:</td></tr><tr><td>Complete re-entry of text</td><td>●</td><td>Based on sequence numbers</td><td>●</td><td></td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td colspan="9">Reporting</td></tr><tr><td>Wide spectrum of standard reports</td><td>●</td><td></td><td></td><td></td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>Simple mechanism for specifying amount of report detail</td><td>●</td><td>Plus 81⁄2&quot;x11&quot; option</td><td>●</td><td></td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>One general report command</td><td>●</td><td>Many report commands</td><td>●</td><td></td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>Scan and query facility</td><td>●</td><td>Plus scan text</td><td>●</td><td></td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td colspan="9">Definition and Naming Conventions</td></tr><tr><td>Maximum Name Length Vary 8-29 characters</td><td>● Maximum Name Length 30-32</td><td>● Maximum Name Length ≥ 32 or extra qualifiers</td><td>●</td><td></td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>Alias/Synonym Facility</td><td>●</td><td></td><td></td><td></td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>Duplicate names not allowed in one version</td><td>●</td><td>Duplicate names with occurrence numbers</td><td>●</td><td></td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>Restrictive free-form text</td><td>●</td><td>Very flexible free-form text</td><td>●</td><td></td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td colspan="9">Documentation</td></tr><tr><td>Less</td><td>●</td><td>Comprehensive</td><td>●</td><td></td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>Poor Examples</td><td>●</td><td>Good Examples</td><td>●</td><td></td><td>●</td><td>●</td><td>●</td><td>●</td></tr></table>

Naming conventions are rules that govern how data names are assigned to objects (also called entities) in the dictionary. There should be flexibility in the allowable combination of characters used for data names. Restrictions such as a maximum number of characters permitted in each data name, specific prefix or suffix requirements, and uniqueness requirements may limit the effectiveness of the DDS as a repository for the description of an organization's information. The names assigned to objects in the dictionary should be user-oriented and suggest the object's semantics.

The data dictionary usually covers more than one functional area or department of an organization. Historically, each area had its own names for objects and wanted to use those names in the dictionary. The same object should be able to have more than one name. However, across the dictionary one name among the synonyms should be identifiable as the primary name, with the remaining names serving as aliases. Additionally, the same name may be used for semantically different objects. Duplicate names (homonyms) should be managed in a similar manner as synonyms.

Definition conventions form the rules that define the general format of objects, the types of objects that can be described, and the kinds of information that can be stated for each object type. The format for an object definition should be flexible and easily understood by the end user. Using the object types and associated syntax users should be able to describe application systems, application system structures, application system components, data structures, interrelationships between data and systems components, and the interrelationships between objects and the organization. Additionally, an organization should be able to define its own object characteristics (i.e., keywords, attributes) to supplement those provided by the DDS.

## Environmentally dependent requirements

The DDS characteristics that are dependent on the organization's environment form the second part of the EDF framework and are called environmentally dependent requirements. These requirements have two dimensions: (1) the operational control activities of data administration, and (2) the DBMS state. The four operational control activities of data administration provide a linkage between the DDS and the activities it supports. The DBMS state provides a linkage between the DDS and the DBMS environment under which it will be operating.

## Operational Control Activities of Data Administration

A DDS facilitates control of the maintenance and documentation of the system by supporting the maintenance activities of the system development documentation, and by supplying features for easily maintaining the dictionary. This activity is an elaboration of two aspects of the basic requirements — ease in reporting and adequacy in documentation.

Activities related to the enforcement of systems and programming standards are based on the promotion of three types of standards: dictionary definition standards, data standards, and program and system standards. Each of these standards includes: naming conventions, minimum definitional requirements of each dictionary object type, uniqueness rules, and system development rules. These standards are used to define dictionary object type descriptions which, in turn, can be used to generate portions of programs, systems, and data definitions. This process promotes standardization in data, programs, and systems and depends upon high quality control of dictionary input and modification. This is an extension of the basic requirement for comprehensive definition and naming conventions.

A DDS controls the integrity and security of an organization's data by simplifying this activity and by maintaining secure and sound descriptions of the organization's data. Dictionary integrity is provided by input quality control, definition standards, and facilities for checking compliance with standards.

Data administration is facilitated through sound system analysis and design activities. The DDS can be used as a source for centralized and consistent information by the systems analyst and designer. The DDS may include or interface with analysis and design tools, especially normalization aids.

Table 3. DDS Packages Classified by DBMS State

<table><tr><td>Package</td><td>Vendor</td><td>Programming Language Interface*</td><td>DBMS Interface*</td></tr><tr><td colspan="4">States (1) No DBMS or (2) One DBMS</td></tr><tr><td>DB/DC Data Data Dictionary [13, 16, 17]</td><td>IBM</td><td>COBOL, PL/1</td><td>IMS (DL/1)</td></tr><tr><td>Integrated Data Dictionary (IDD) [7, 8, 9, 10]</td><td>Cullinet</td><td>COBOL</td><td>IDMS</td></tr><tr><td>UCC TEN [27, 29]</td><td>University Computing Company</td><td>COBOL, PL/1</td><td>IMS</td></tr><tr><td colspan="4">State (2) One DBMS</td></tr><tr><td>Data Control System [22]</td><td>Cincom System, Incorporated</td><td>COBOL, BAL, FOR-TRAN, PASCAL, PL/1</td><td>TOTAL</td></tr><tr><td>Extended Data Dictionary (EDD) [22]</td><td>Intel Systems Corporation</td><td>COBOL</td><td>System 2000</td></tr><tr><td colspan="4">State (1) No DBMS, (2) One DBMS, or (3) More Than One DBMS</td></tr><tr><td>Data Catalogue 2 [26, 27]</td><td>Synergetics Corporation</td><td>COBOL, PL/1, BAL</td><td>IMS (DL/1), TOTAL, ADABAS, IDMS</td></tr><tr><td>Data Dictionary [2]</td><td>Applied Data Research, Inc.</td><td>COBOL, PL/1, BAL, DATAREPORTER</td><td>DATACOM/DB, TOTAL, IMS (DL/1)</td></tr><tr><td>Data Manager [22, 23]</td><td>MSP, Inc.</td><td>COBOL, PL/1, BAL</td><td>IMS (DL/1), IDMS, ADABAS, TOTAL, System 2000/80, MARK IV</td></tr><tr><td>Lexicon** [5]</td><td>Arthur Anderson &amp; Company</td><td>COBOL, PL/1, BAL</td><td>IMS, TOTAL, IDMS, System 2000</td></tr><tr><td colspan="4">Notes</td></tr><tr><td colspan="4">* Bridge facility exists in at least one direction. ** Not supported by Arthur Anderson after January 1983.</td></tr></table>

## Database Management System State

There are three database management system states possible in this framework: (1) no DBMS in use by the organization, (2) a single DBMS in use, or (3) more than one DBMS in use. Two surveys conducted by Kahn [18, 19] determined that the no DBMS state is the least common and the other two states are equally likely to occur. In most organizations the DBMS was acquired prior to the selection of the DDS. Those organizations without a DBMS planned to acquire the packages together or acquire a DDS first. Commercial DDS products classified according to the DBMS state(s) supported are listed in Table 3.

In the no DBMS state the DDS is used to document non-DBMS applications and systems. Increasingly, organizations acquire a DDS in the hope that better information about the data resource will solve their current problems and postpone, perhaps indefinitely, the acquisition of a DBMS.

In the single DBMS state the organization has only one DBMS or currently does not have a DBMS but has made the decision to acquire a specific DBMS. The DDS is used to document both non-DBMS and DBMS-based application systems and to facilitate the use of the DBMS. In this state, the organization does not intend to acquire additional database management systems or to convert to a different DBMS.

In the multiple DBMS state the organization has or plans to have more than one DBMS. This state may also be appropriate for an organization currently without a DBMS but planning to acquire a DBMS selected from a spectrum of DBMS alternatives. If the DDS supports various DBMS alternatives then it will be usable prior to and after the acquisition of the DBMS. The DDS is used to document both non-DBMS and DBMS-based application systems.

## Integration of DBMS states and DA activities

The environmentally dependent requirements are those DDS features necessary to support the major data administration activities. These requirements depend on the DBMS state. DDS features can be organized in a matrix with the dimensions of data administration activity (column) and DBMS state (row). The required DDS features for each data administration activity in the three DBMS states are summarized in Tables 4A-D. (Each table corresponds to a column of the matrix.) This section describes how the individual DDS features support specific data administration activities according to DBMS state. All features described are available on at least one commercial DDS.

## Maintenance and Documentation

In order to provide more efficient system maintenance under all three DBMS states, it is important to have the reporting features listed in Table 4A. These reporting features are available in most DDS products. Through flexible and easy-to-use report formats, the DDS should provide improvements in the quality and generation of system and application documentation.

A facility by which an object can exist in the dictionary in both test and production versions is very valuable in minimizing the loss of data integrity. Most DDS products support at least two versions. Multiple definitions by different users could also result during system development and could be best documented in multiple test versions (provided by IBM's DB/DC and DataManager). The DDS should automatically log and update information about maintenance activities on the dictionary contents. Maintenance information is maintained and reported by IDD, but this is not a common DDS feature.

In all three DBMS states, bridge facilities aid in system maintenance. Maintenance is assisted primarily by bridges from the DDS to the application programs which generate program data definitions and other code from the dictionary contents. Dictionary population is simplified and expedited by bridges from application programs to the DDS, which generate dictionary input from application programs. Bridges in both directions are included in most DDS products.

Under the single and multiple DBMS environments, bridge facilities with the DBMS' provide a pathway between the dictionary and the data descriptions of the DBMS. Maintenance is facilitated by bridges from the DDS to the DBMS while dictionary population and documentation of DBMS applications are simplified and expedited by bridges from the DBMS to the DDS. All DDSs studied provided a bridge from DDS to the DBMS but some (DataManager and Data Catalogue 2) do not provide a bridge in the other direction.

Application maintenance is expedited by an active data dictionary in the single and multiple DBMS states. Many maintenance tasks are eliminated, thus reducing labor requirements. In an active DDS, the data definitions used by the DBMS are bound at run time so that the most current definitions are used. Additionally, new data definition language (internal or external)

<table><tr><td>No DBMS Environment</td></tr><tr><td>REPORTING</td></tr><tr><td>1. Search and query using keyword</td></tr><tr><td>2. Output format appealing to a broad spectrum of users</td></tr><tr><td>3. Wide variety of reports</td></tr><tr><td>4. Output suitable for system and application documentation</td></tr><tr><td>5. Latest maintenance information included and is easy to access</td></tr><tr><td>6. Interactive display for inquiry and update</td></tr><tr><td>7. Report analyzing the impact of a change</td></tr><tr><td>MAINTENANCE</td></tr><tr><td>1. Production and test versions of the dictionary</td></tr><tr><td>2. Multiple test versions</td></tr><tr><td>3. Active versus passive DDS</td></tr><tr><td>4. Automatic logging of dictionary changes</td></tr><tr><td>5. Simple and comprehensive procedures for making dictionary changes</td></tr><tr><td>BRIDGE FACILITIES</td></tr><tr><td>1. Facilities to generate program data definition (and other code) from the dictionary</td></tr><tr><td>2. Facilities to generate DDS from program data definitions</td></tr><tr><td>Single DBMS Environment</td></tr><tr><td>REPORTING</td></tr><tr><td>Same as no DBMS environment</td></tr><tr><td>EASE OF MAINTENANCE</td></tr><tr><td>Same as no DBMS environment</td></tr><tr><td>BRIDGE FACILITIES</td></tr><tr><td>Same as no DBMS environment</td></tr><tr><td>DBMS INTERFACE</td></tr><tr><td>1. Facilities to generate DDS input from DBMS data definitions and applications</td></tr><tr><td>2. Facilities to generate DBMS data definition language from DDS</td></tr><tr><td>3. Conformity in structural relationships between database, files and DDS</td></tr><tr><td>Multiple DBMS Environment</td></tr><tr><td>REPORTING</td></tr><tr><td>Same as no DBMS environment</td></tr><tr><td>EASE OF MAINTENANCE</td></tr><tr><td>Same as single DBMS environment</td></tr><tr><td>BRIDGE FACILITIES</td></tr><tr><td>Same as no DBMS environment</td></tr><tr><td>DBMS INTERFACE</td></tr><tr><td>1. Same as single DBMS environment plus</td></tr><tr><td>2. Simultaneous interface with a number of different DBMSs</td></tr></table>

Table 4A. DDS Features To Control Systems Maintenance and Documentation

Table 4B. DDS Features To Enforce Systems and Programming Standards

<table><tr><td>No DBMS Environment</td></tr><tr><td>USER INTERFACE</td></tr><tr><td>1. Dictionary facility or user-program to perform automatic validity checks of DDS input</td></tr><tr><td>2. Automatic generation of DDS input from program data description sections</td></tr><tr><td>3. Automatic generation of COBOL data division and PL/1 declaration from DDS</td></tr><tr><td>4. Extendable dictionary contents</td></tr><tr><td>5. Easy to write installation-specific suggested reports: DDS input validation, dictionary completeness, evaluation of standards compliance, determination of dictionary inconsistency</td></tr><tr><td>SECURITY FEATURES</td></tr><tr><td>1. Comprehensive and easy to use security for DDS access and dictionary access and modification</td></tr><tr><td>2. Test and production versions of the dictionary</td></tr><tr><td>Single DBMS Environment</td></tr><tr><td>USER INTERFACE</td></tr><tr><td>Same as no DBMS environment</td></tr><tr><td>SECURITY FEATURES</td></tr><tr><td>1. Same as no DBMS environment plus</td></tr><tr><td>2. Security features applicable to DBMS interfaces</td></tr><tr><td>DBMS INTERFACE</td></tr><tr><td>1. Facilities to generate DDS input from DBMS data definitions and applications</td></tr><tr><td>2. Facilities to generate DBMS data definition language (internal or external form) from DDS</td></tr><tr><td>3. Conformity in structural relationships between database, files and DDS</td></tr><tr><td>4. Enforcement of standards in bridge facilities</td></tr><tr><td>Multiple DBMS Environment</td></tr><tr><td>USER INTERFACE</td></tr><tr><td>Same as no DBMS environment</td></tr><tr><td>SECURITY FEATURES</td></tr><tr><td>Same as single DBMS environment</td></tr><tr><td>DBMS INTERFACE</td></tr><tr><td>1. Same as single DBMS environment plus</td></tr><tr><td>2. Simultaneous interface with a number of different DBMSs</td></tr></table>

does not have to be generated for each set of DDS and/or data changes. Some DBMSs (IDMS, System 2000/80) require an active DDS for their operation. On the other hand, a passive DDS (IBM's DB/DC, DataManager, Data Catalogue 2) requires that the data definition language be modified or produced by the DDS and then encoded into the DBMS' internal form prior to running the applications effected by the changes.

## Systems and Programming Standards

Under all DBMS states, validation of DDS input is required to enforce systems and programming standards. Validation of DDS input with respect to user-defined standards is provided by UCC-10. Many DDSs provide a user program interface facility which can be used to automatically validate DDS input with respect to organization-specific standards and dictionary contents.

Table 4C. DDS Features To Enforce Integrity and Control Security of Corporate Data

<table><tr><td>No DBMS Environment</td></tr><tr><td>USER INTERFACE</td></tr><tr><td>1. Dictionary facility and/or user-program interface to perform automatic validity checks and DDS input</td></tr><tr><td>2. Automatic generation of DDS input from portions of application programs</td></tr><tr><td>3. Automatic generation of portions of application program (e.g., COBOL data division) from dictionary</td></tr><tr><td>4. Integrity constraints and security requirements precisely and robustly defined in the dictionary</td></tr><tr><td>5. An active versus passive DDS</td></tr><tr><td>SECURITY FEATURES</td></tr><tr><td>1. Test and production versions of the dictionary</td></tr><tr><td>2. Multiple test versions</td></tr><tr><td>3. Comprehensive and easy-to-use security system for access to DDS and dictionary</td></tr><tr><td>4. User-profile-based security system</td></tr><tr><td>5. Security designation based on action performed and portion of dictionary</td></tr><tr><td>—wide range of action alternatives</td></tr><tr><td>—large spectrum of granularity for specifying dictionary portion ranging from dictionary version to a specific object in a version</td></tr><tr><td>Single DBMS Environment</td></tr><tr><td>USER INTERFACE</td></tr><tr><td>Same as no DBMS environment</td></tr><tr><td>SECURITY FEATURES</td></tr><tr><td>1. Same as single DBMS environment plus</td></tr><tr><td>2. Security features applicable to all DBMS interfaces</td></tr><tr><td>Multiple DBMS Environment</td></tr><tr><td>USER INTERFACE</td></tr><tr><td>Same as no DBMS environment</td></tr><tr><td>SECURITY FEATURES</td></tr><tr><td>Same as single DBMS environment</td></tr></table>

Enforcement of standards is enhanced in all DBMS states by the DDS bridge facility to application programs. This facility produces high quality data definitions to be included in programs. In the single and multiple DBMS states, a similar bridge facility to the DBMS promotes the production of high quality and standardized DBMS data descriptions (in external or internal form).

Standardization is also enhanced by bridge facilities from DBMS to DDS. This bridge facilitates the documentation of existing DBMS applications in the DDS and promotes consistency between existing and new systems. Most DDSs provide this facility. This consistency is important when the existing systems were developed using a standardized and controlled approach. However, if this was not the case, standardization between new and existing systems may not be desirable. Some DDSs (e.g., DataManager) operate on the principle that most existing DBMS applications are poorly conceived, inconsistent, and not standardized and that the DDS input produced automatically from these applications would be worthless.

Since users tend to analyze automatically-generated input with less rigor than manually produced input, manual creation of DDS input for existing DBMS applications will result in a higher quality dictionary and in better control of programming and documentation standards.

Extendability features help in enforcing standards in all DBMS states. Extendability facilities include extending the types of information recorded in the dictionary and the generation of organization-specific reports. The type of information stored in the dictionary can be extended in two ways: the addition on new statements to describe an existing object type, and the addition of new object types with their corresponding description. The second type, content extendability, encompasses the first. Elaborate extendability features are provided by DB/DC Data Dictionary and DataManager.

When additional (non-standard) information is in the dictionary, but is not accessed and presented by standard reports, it is necessary to write special reports. If the installation-written reports are difficult and extremely time-consuming to program, require detailed understanding of the dictionary's internal structure, or very costly to develop and maintain, most data administrators will balk at extending the dictionary contents. Therefore, an extendability facility for dictionary contents is essentially worthless without a good host language interface or query language to provide easy implementation of these special reports. For example, in the DB/DC Data Dictionary three special reports (INSTALL, GUIDE and FORMAT) exist to report on extended dictionary contents. Additionally, entity-specific reports (an option of the Report command) are available for default contents.

## Integrity and Security

Under all DBMS states it is important that input transactions are automatically screened for their validity in order to protect the integrity of information contained in the dictionary. This validity check should consider organizational standards and evaluate consistency with current dictionary contents. Validation functions can be provided by the same features used to enforce systems and programming standards. An established communication bridge between the validation mechanism and an automatic generation of dictionary input can also ensure the uniformity of the dictionary contents.

To provide protection for the information stored in the DDS, an efficient and flexible dictionary security system is required. The loss of data integrity can be minimized by the existence of multiple versions of the dictionary.

In most installations, different users need different levels of access — read, update, add (and any combination) — to different parts of the dictionary. Dictionaries can be stratified by version and by object; that is, a given user may have access to a discrete list of objects in the dictionary, to all objects in a specific version (i.e., test or production), to specific objects in a specific version, or to any combination of these alternatives. This stratification is commonly accomplished through a user profile security system that restricts or allows access to the dictionary depending on a combination of the type of action and data involved and how this combination matches with the security level of the user. DDSs differ in the level of security designations provided. Additionally, DDSs differ in the types of actions allowed. Types of actions should include: read only, add only, read and add only, and read, add, modify and delete.

The greater the precision and level of detail of the security system the better. This precision must be tempered by usability and amount of effort required for setting up the dictionary's security.

Most DDSs have a privileged security level that sets up the dictionary security scheme for all other dictionary users. This privileged level may have access to special dictionary features and reports.

An active DDS provides automatic data integrity validation since definitions are bound at run time. Validation with a passive DDS is based on the data definition generated from the data dictionary.

## Systems Analysis and Design

In any DBMS state, the DDS can be used as an information source for existing data descriptions and other system-related information by the systems analyst, designer, or other pertinent individuals. The DDS aids in system development by providing easy access to up-to-date information, as well as providing a wide variety of essential reports that facilitate analysis. A DDS is an effective tool for communication of information between end users and analysts or designers. DDS reports with graphical output especially enhance communication with users.

Table 4D. DDS Features To Aid in Systems Analysis and Design

<table><tr><td>No DBMS Environment</td></tr><tr><td>REPORTING</td></tr><tr><td>1. Search and query using keyword</td></tr><tr><td>2. Output formats appealing to broad spectrum of users</td></tr><tr><td>3. Wide variety of reports that are easy to generate</td></tr><tr><td>4. Inquiry does not require DDS or DBMS technical expertise</td></tr><tr><td>5. Reporting of a hierarchical structure of application system</td></tr><tr><td>6. Interactive display for inquiry and update</td></tr><tr><td>7. Output suitable for documentation</td></tr><tr><td>AID IN DEVELOPMENT</td></tr><tr><td>1. Test and production versions of the dictionary</td></tr><tr><td>2. Flexibility in the order in which DDS entities and their relationships are defined in the dictionary</td></tr><tr><td>3. Ability to reference previously defined DDS entities in another entity description</td></tr><tr><td>4. Extendable dictionary contents</td></tr><tr><td>5. Reporting facilities to support extendability</td></tr><tr><td>Single DBMS Environment</td></tr><tr><td>REPORTING</td></tr><tr><td>Same as no DBMS environment</td></tr><tr><td>AID IN DEVELOPMENT</td></tr><tr><td>1. Same as no DBMS environment plus</td></tr><tr><td>2. Interface with or include automated database design techniques such as computerized normalization, identification of keys, data clustering, and formation of data structures</td></tr><tr><td>Multiple DBMS Environment</td></tr><tr><td>REPORTING</td></tr><tr><td>Same as no DBMS environment</td></tr><tr><td>AID IN DEVELOPMENT</td></tr><tr><td>Same as single DBMS environment</td></tr></table>

To support an organization's systems development methodology a DDS should be flexible. The contents of the dictionary should be able to be developed in a flexible and modular manner. The dictionary should be able to contain partial object definitions, partial relationships between objects, and duplicate dictionary structures.

Extendability features and corresponding host language interface facilities will enhance the ability of a DDS to support systems analysis and design. For example, an organization using data flow diagrams as a system analysis technique could easily document these diagrams if the primitives — interfaces, inputs, outputs, data flows, and data stores — were defined as object types in the DDS. (This is provided by DataManager.) A DDS can aid the database design process by including automated design techniques as either DDS reports or interfaces with automated tools. DataManager interfaces with an interactive tool for enterprise modeling and logical database design (called DesignManager) and with other MSP products for aiding system development (ProjectManager, SourceManager and TestManager). IDD interfaces with Cullinet's Application Development System.

## Selection of a DDS

To use this framework as the basis of an improved DDS evaluation and selection process, six steps must be performed.

1. Identify and prioritize the data administration activities which can be best supported by the DDS.

2. Determine the DBMS state under which the DDS will operate.

3. Select the alternative DDSs to be evaluated.

4. Evaluate the DDS alternatives on terms of the basic requirements.

5. Evaluate the DDS alternatives in terms of the environmentally dependent requirements.

6. Select the most appropriate DDS.

Prior to the evaluation and selection process, an evaluation team must be formed and resources must be allocated to perform this process.

Step 1 — Identify and Prioritize. The data administrator should identify and prioritize the operational control requirements of data administration that are to be supported by the DDS. These requirements can be classified into the following four major activities:

1. control of systems maintenance and documentation,

2. enforcement of systems and programming standards,

3. control of the integrity and security of an organization's data, and

4. assistance in systems analysis and design.

Most organizations will have requirements in all the major activities. The relative importance of these requirements will not be uniform across the four major activities and, therefore, the priority of these activities can be determined through analysis. The priorities assigned need not be a strict ranking and can be qualitative. The resulting priority assignments can range from each activity having a different priority to all having the same one.

Step 2 — Determine the DBMS State. The organization should be analyzed to determine its current and future plans for employing a DBMS. The organization must determine the DBMS state under which it is, or soon will be operating. All organizations will fit into one of the three DBMS states.

Step 3 — Selection of DDS Alternatives. There are numerous commercial DDSs available to an organization. Internal development of a DDS should be chosen only when the organization is certain that no available DDS will satisfy their present and future requirements. Most probably this can only be determined after an evaluation of the many available commercial DDSs The DDSs being evaluated should be compatible with the organization's hardware/software environment and within its budget.

Step 4 — Evaluate the Basic Requirements. The basic requirements should be evaluated first. A DDS that does not satisfy the basic requirements is one that is not easy to use and should not be selected. After the DDSs are evaluated with respect to the basic requirements, the results should be analyzed and unsatisfactory DDSs removed from further consideration. This analysis can best be summarized in a table with the following information: DDS name, DDS vendor, percentage of basic requirements satisfied, percentage of basic requirement not satisfied, basic requirement not satisfied, and extra features.

Step 5 — Evaluate the Environmentally Dependent Requirements. All DDSs that satisfy the basic requirements should then be evaluated and analyzed with respect to the environmentally dependent requirements. A table grouping the features of the DDSs with respect to their ability to support each data administration activity is the easiest vehicle for comparison and evaluation. To facilitate analysis, features should be grouped in functional areas such as reporting, data entry, DBMS interface, etc.

Step 6 — Determine the Most Appropriate DDS. The results from steps 4 and 5 form the basis of selecting a DDS. Before commencing the selection process, one must verify that the assumptions made and the environmental characteristics determined are still correct. Additionally, the validity of the priorities assigned to each operational control activity of data administration, the organization's DBMS(s), and DBMS state must be verified.

When a large number of DDSs are being evaluated a numerical scoring method, such as Plagman [25], is best used. This technique reduces the data being analyzed to a manageable level. The assignment of weights to features is difficult, and often subjective, as is the scoring of the specific DSS feature. In applying the EDF framework, first the basic requirements and then the environmentally dependent requirements should be evaluated. Last, a composite score should be calculated.

When a few (usually three or less) DDSs are being evaluated, a relative evaluation of each feature is used (like Table 2). As with scoring, first the basic requirements and then the environmentally-dependent requirements should be evaluated.

## Case Example

A large New England bank holding company was facing a potential merger and needed an inventory of information systems. No centralized inventory of systems or computerized data existed. The company faced a very costly, time consuming, and labor-intensive activity.

At the same time the holding company's data processing management stated the desire to adopt a “database philosophy” where data was viewed as an integrated, managed, and shared corporate resource. Given this attitude the company's data processing staff advocated a data dictionary system to facilitate the transition to a database environment and to meet the continuing requirements for various system inventories. Both data processing management and company management concurred and agreed to commit the necessary resources.

The environmentally dependent framework guided the DDS selection process. First, the company set its priorities for data administration activities. The control of systems maintenance and documentation and the enforcement of systems and programming standards were deemed “very important.” Ranked “important” was the control of the integrity and security of an organization’s data. In the future, assistance in systems analysis and design will be “important.”

Most of the company's information systems were not DBMS-based. Most programs were written in COBOL. FOCUS was used by end users on extracted files. Procurement of a DBMS seemed likely in the future but no specific commercial products had been considered. Nevertheless, the company was classified as being in the multiple DBMS state in order for the DDS to be useful both before and after the DBMS acquisition. Two DDSs that supported multiple DBMSs were evaluated by the company — DataManager and Data Catalogue 2.

A comparison of the two DDSs with respect to the basic requirements is shown in Table 5. The basic requirements evaluation determined that DataManager was slightly better than Data Catalogue 2. Given that the difference was not significant, the company's evaluation continued with the environmentally dependent requirements.

A comparison of DataManager and Data Catalogue 2 with respect to the four environmentally dependent requirements is shown in Table 6. In the area of controlling systems maintenance and documentation (Table 6A), DataManager had two features superior to Catalogue 2: (1) DataManager had multiple test versions, and (2) it interfaced with a greater number of DBMS. In enforcing systems and programming standards (Table 6B), Data Catalogue 2 was superior in the enforcement of standards in DDS input through its Standards Violators Report. The two are equivalent in all other features. In the other two requirement areas, DataManager was as good or more robust than Data Catalogue 2.

Based on information contained in Tables 5 and 6, DataManager was selected to be the company's data dictionary system. The bank is awaiting software and documentation for DataManager.

## 212 MIS Quarterly/September 1985

Table 5. Evaluation of Basic Requirements

<table><tr><td>DDS FEATURES</td><td colspan="2">DATA DICTIONARY SYSTEMS</td></tr><tr><td>Maintenance</td><td>Data Catalogue 2</td><td>Datamanager</td></tr><tr><td>DATA ENTRY METHODS</td><td>Data entry accomplished via free-form or online or batch, tutorial, prompt for online, free form option under prompted online entry and tailored fixed form batch entry</td><td>Data entry via either batch or online</td></tr><tr><td>COPY FACILITY</td><td>—</td><td>Data entry facilitated by ability to copy structure and/or parts of the data definition</td></tr><tr><td>LINKS BETWEEN OBJECTS</td><td>Links between different objects are set up automatically between object types using default relationships</td><td>Links between different objects must be stated explicitly</td></tr><tr><td>DDS BUILD-UP</td><td>When relating one object to the other, names must already exist in the DDS</td><td>Flexible build-up of DDS database, top-down or bottom-up, by automatic generation of dummy objects</td></tr><tr><td>UPDATE COMMANDS</td><td>Uses add, change, delete types of update commands</td><td>Uses add, change, delete type of update commands</td></tr><tr><td>TEXT UPDATE</td><td>Update of description ‘text’ utilizes sequence number</td><td>Update of ‘comments’ utilizes sequence number</td></tr><tr><td>Reporting</td><td></td><td></td></tr><tr><td rowspan="8">STANDARD REPORTS</td><td>Seven types of standard reports:</td><td>Four types of standard reports:</td></tr><tr><td>1. catalogue report</td><td>1. glossary report</td></tr><tr><td>2. hierarchy report</td><td>2. list report</td></tr><tr><td>3. usage report</td><td>3. print report</td></tr><tr><td>4. relational report</td><td>4. detail report</td></tr><tr><td>5. index report</td><td></td></tr><tr><td>6. name-analysis report</td><td></td></tr><tr><td>7. indented page number index report</td><td></td></tr><tr><td>REPORT OPTIONS</td><td>Standard options used to specify report sequence and format, limited entries/details to be included, all reports can be produced in an 81⁄2" by 11" format</td><td>Standard options used to specify report format and level of detail; all reports can be produced in an 81⁄2" by 11" format</td></tr><tr><td>REPORT COMMANDS</td><td>Uses a number of single report commands</td><td>Uses a number of simple and similarly structured report commands</td></tr><tr><td>SCAN FACILITY</td><td>Has query reports and search facilities</td><td>Has query reports and search facilities</td></tr><tr><td colspan="3">Naming and Definition Conventions</td></tr><tr><td>OBJECT NAMING</td><td>Each object name can be up to 30 characters long; each name can be made up of any combination of characters, with no embedded blanks</td><td>Each object name can be up to 30 characters long; there are specific characters allowed in addition to the alphabets and numerals</td></tr><tr><td>ALIAS FACILITY</td><td>Alias can be used to relate synonyms</td><td>Alias can be used to relate synonyms</td></tr><tr><td>DUPLICATE NAME</td><td>Duplicate names not allowed</td><td>Duplicate names allowed only if specified for different object types or versions</td></tr><tr><td>TEXT FORMAT</td><td>Free-form description of text; up to 9999 lines each of 67 characters long</td><td>Free-form description of text; up to 32,767 lines, each of 256 characters</td></tr><tr><td colspan="3">Documentation</td></tr><tr><td>MANUALS</td><td>Comprehensive manual with slight confusion in definition of terminology in spots</td><td>Comprehensive manual with inadequate uses of examples</td></tr></table>

Table 6A. Systems Maintenance and Documentation

<table><tr><td>DDS Feature</td><td>DATA CATALOGUE 2</td><td>DATAMANAGER</td></tr><tr><td colspan="3">Reporting</td></tr><tr><td>Scan Facilities</td><td>Keyword scan report available, using COUNT, LIST and SHOW commands</td><td>Keyword scan report available, using GLOSSARY, LIST WHAT and WHICH commands</td></tr><tr><td>Maintenance Information</td><td>Latest maintenance date not automatically maintained or reported</td><td>Latest maintenance date not automatically maintained or reported</td></tr><tr><td>Online Query</td><td>Tutorial-prompted mode of data entry available</td><td>Interact display for inquiry and update available</td></tr><tr><td>Report Format</td><td>Reports can be produced in 81⁄2&quot; by 11&quot; format</td><td>Reports can be produced in 81⁄2&quot; x 11&quot; format</td></tr><tr><td colspan="3">Ease of Use</td></tr><tr><td>Dictionary Version</td><td>Can maintain one production version and only one test version of the dictionary</td><td>Can maintain both production and multiple test versions of the dictionary</td></tr><tr><td>Program Data Definition Generation</td><td>Can generate data definitions for COBOL, BAL, and PL/1</td><td>Can generate data definitions for COBOL, BAL, and PL/1</td></tr><tr><td>DDS Input Generation</td><td>Can generate dictionary input from COBOL, BAL and PL/1 programs</td><td>Can generate dictionary input from COBOL and PL/1 programs</td></tr><tr><td colspan="3">DBMS Interface</td></tr><tr><td>Conformability</td><td>Conformable to IMS, TOTAL, ADABAS and IDMS</td><td>Conformable to IMS, TOTAL, ADABAS, IDMS and System 2000/80</td></tr><tr><td>DDS Data Definition Generation</td><td>Can generate control blocks for IMS, TOTAL, ADABAS, and IDMS</td><td>Can generate control blocks for IMS, TOTAL, ADABAS, IDMS and System 2000/80</td></tr><tr><td>DBMS Support</td><td>Supports multiple DBMSs and can report on specific entities and their respective DBMSs</td><td>Supports multiple DBMSs and can report on specific entities and their respective DBMSs</td></tr><tr><td>Active vs Passive</td><td>Passive</td><td>Passive</td></tr></table>

Table 6B. Systems and Programming Standards

<table><tr><td>DDS Feature</td><td>DATA CATALOGUE 2</td><td>DATAMANAGER</td></tr><tr><td colspan="3">User Interface</td></tr><tr><td>DDS Input Validation</td><td>No built-in automated DDS input validator</td><td>No built-in automated DDS input validator</td></tr><tr><td>Interface for Input Validation</td><td>Feasible to incorporate user-written validators of DDS input for conforming to standards, and for consistency with dictionary contents via program interface</td><td>Feasible to incorporate user-validator of DDS input for conforming to standards only</td></tr><tr><td>Standards Violators Report</td><td>Available Index of StandardsViolators Report</td><td>—</td></tr><tr><td colspan="3">Program Interface</td></tr><tr><td>DDS Input Generation</td><td>Source analyzer available to scan data definition of programs and create DDS input</td><td>Source analyzer available to scan data definition of programs and create DDS input</td></tr><tr><td>Program Data Definition Generation</td><td>Can generate data definition entries for programs from DDS source</td><td>Can generate data definition entries for programs from DDS source</td></tr><tr><td colspan="3">DBMS Interface</td></tr><tr><td colspan="3">Same as Systems Maintenance and Documentation (see Table 6A)</td></tr></table>

Table 6C. Integrity and Security of Corporate Data

<table><tr><td>DDS Feature</td><td>DATA CATALOGUE 2</td><td>DATAMANAGER</td></tr><tr><td colspan="3">Security Features</td></tr><tr><td>Dictionary Access</td><td>Establishment of user access profiles required</td><td>Establishment of user access profiles required</td></tr><tr><td>Lowest Security Level</td><td>Lowest security level of dictionary access is by specific object</td><td>Lowest security of dictionary access is by specific object</td></tr><tr><td>Security Action Levels</td><td>Security action levels are: —read only —update —delete</td><td>Security access levels are: —access —alter —remove</td></tr><tr><td>Security for Information Deletion</td><td>Additional security for deletion of objects and relationships</td><td>Additional security for deletion of objects</td></tr><tr><td>Version Security</td><td>Can apply security control to specific version of dictionary</td><td>Can apply security control to specific version of dictionary</td></tr><tr><td>Test Versions</td><td>Only one test version of dictionary available</td><td>Availability of multiple test versions of dictionary</td></tr><tr><td colspan="3">User Interface</td></tr><tr><td colspan="3">Same as systems and programming standards (Table 6B)</td></tr><tr><td colspan="3">Program Interface</td></tr><tr><td colspan="3">Same as systems and programming standards (Table 6B)</td></tr><tr><td colspan="3">DBMS Interface</td></tr><tr><td colspan="3">Same as Maintenance and Documentation (Table 6A)</td></tr></table>

Table 6D. Systems Analysis and Design

<table><tr><td>DDS Feature</td><td>DATA CATALOGUE 2</td><td>DATAMANAGER</td></tr><tr><td colspan="3">Reporting</td></tr><tr><td>Standard Reports</td><td>Seven type of standard reports1. catalogue report2. hierarchy report3. usage report4. relational report5. index report6. name-analysis report7. indented page number index report</td><td>Four types of standard reports:1. glossary report2. list report3. print report4. detail report</td></tr><tr><td>Query and Search Facilities</td><td>Has query reports and search facilities</td><td>Has query reports and search facilities</td></tr><tr><td colspan="3">Ease of Use</td></tr><tr><td>Building DDS</td><td>When relating one entity to the other, names must already exist in the DDS</td><td>Flexible build-up of dictionary database, top-down or bottom-up, by automatic generation of dummy entities</td></tr><tr><td>Copying Facilities</td><td>—</td><td>Ability to copy structure and/or parts of data definition</td></tr><tr><td>Versions</td><td>Can maintain one production version and only one test version of the dictionary</td><td>Can maintain production and multiple test versions of the dictionary</td></tr><tr><td>Program Data Definition Generation</td><td>Can generate data definitions for COBOL, BAL and PL/1</td><td>Can generate data definitions for COBOL, BAL and PL/1</td></tr><tr><td>DDS Input Generation from Programs</td><td>Can generate dictionary input from COBOL, BAL and PL/1 programs</td><td>Can generate dictionary input from COBOL and PL/1 programs</td></tr><tr><td colspan="3">DBMS Interface</td></tr><tr><td>DBMS Interface(s)</td><td>Supports multiple DBMSs and can report on specific entities and their respective DBMSs</td><td>Supports multiple DBMSs and can report on their specific entities and their respective DBMSs</td></tr><tr><td colspan="3">Tool Interface</td></tr><tr><td></td><td>Data Designer</td><td>ControlManager, DesignManager, SourceManager, TestManager, ProjectManager</td></tr></table>

## Conclusion

The data dictionary system is the most crucial ingredient for a successful data administration effort. The environmentally dependent framework for selecting a DDS avoids the shortcomings of traditional approaches and still ensures that the organization's data administration objectives are satisfied. The organization that employs the environmentally dependent framework can be sure that its DDS will be responsive to its specific requirements and environment. In addition, the framework eliminates infeasible products from further consideration, thus simplifying the decision-making process.

## References

[1] Applied Data Research, Inc. Datacom/DD, Data Dictionary & Directory System, System Reference Manual, Order No. DD4G-SR-10, Dallas, Texas, September 1979.

[2] Applied Data Research. Datacom/DD, Data Dictionary and Directory System, Concepts & Facilities, Order No. DHIG-00-00, Dallas, Texas.

[3] Allen, F.W., Loomis, M.E. and Mannino, M.V. “The Integrated Data Dictionary/Directory System,” Computing Surveys, June 1982, Volume 14, Number 2, pp. 246-286.

[4] Anthony, R. Planning and Control Systems: A Framework for Analysis, Graduate School of Business Administration, Harvard University, Cambridge, Massachusetts, 1965.

[5] Arthur Anderson & Company, Lexicon, Automation Concept for Business Information Systems, General Description Manual, (4th Ed.), Chicago, Illinois, 1977.

[6] Canning, R.G. “The Data Dictionary/Directory Function,” EDP Analyzer, Volume 12, Number 11, November 1974.

[7] Cullinane Corporation, Integrated Data Dictionary, User's Guide, Revision 0, (Release 1.2), Westwood, Massachusetts, September 1978.

[8] Cullinane Corporation, Integrated Data Dictionary, DDDL Reference Guide, (Beta Release 2.0), Westwood, Massachusetts, 1979.

[9] Cullinane Corporation, IDD Classroom Aids, (Release 1.2) Westwood, Massachusetts, May 1979.

[10] Cullinane Corporation, Integrated Data Dictionary, User's Guide, (Release 2.0), Westwood, Massachusetts, 1980.

[11] Curtice, R. and Diekaman E. “A Survey of Data Dictionaries,” Datamation, March 1981, Volume 27, Number 3, pp. 135-158.

[12] Date, C.J. An Introduction to Database Systems (3rd Ed.) Addison-Wesley Publishing Company, Reading, Massachusetts, 1981.

[13] Fehder, P.L. “The IBM DB/DC Data Dictionary, A Brief Overview — With Special Emphasis on the Extensibility and Program Access Facilities,” IBM General Products Division, White Plains, New York, 1980.

[14] Gane, C.P. and Sarson, T. Structured Systems Analysis: Tools and Techniques, Prentice-Hall, Inc., Inglewood Cliffs, New Jersey, 1979.

[15] Hopwood, A.G. “Towards an Organizational Perspective for the Study of Accounting and Information Systems,” Accounting, Organization and Society, Volume 3, Number 1, pp. 3-13, 1978.

[16] IBM. DB/DC Data Dictionary Administration and Customization Guide, Document Composition Facility, (1st Ed.), Order No. SH20-9174-0, White Plains, New York, July 1979.

[17] IBM. DB/DC Data Dictionary Applications Guide, IBM Document Composition Facility, (1st Ed.), Order No. SH20-9173-0, White Plains, New York, July 1979.

[18] Kahn, B.K. “Some Realities of Data Administration,” Communications of the ACM, Volume 26, Number 10, October 1983, pp. 794-799.

[19] Kahn, B.K. and Garceau, L.R. “A Developmental Model of the Database Administration Function,” Journal of MIS, Volume 1, Number 4, Spring 1985, pp. 87-101.

[20] Lawrence, P. and Lorsch J. Organization and Environment — Managing Differentiation and Integration, Harvard University, Cambridge, Massachusetts, 1967.

[21] Lefkovitz, H.C. Data Dictionary Systems, Q.E.D. Information Sciences, Inc., Wellesley, Massachusetts, 1977.

[22] Lefkovitz, H.C., Sibley, E.H. and Lefkovitz, S.L. Information Resource/Data Dictionary

Systems, Q.E.D. Information Sciences, Inc., Wellesley, Massachusetts, 1983.

[23] Management Systems Programming Limited. DataManager User's Guide, Lexington, Massachusetts, February 1980.

[24] Management Systems and Programming Limited. DataManager Basic Training Workbook, Lexington Massachusetts, December 1979.

[25] Nolan, R.L. Managing the Data Resource Management Function, (2nd Ed.), West Publishing Company, St. Paul, Minnesota, 1982.

[26] Plagman, B.K. “Criteria for the Selection of Data Dictionary/Directory Systems,” Auerbach Publication 22-04-01, Auerbach Publishers Inc., New York, New York, 1977.

[27] Synergetics Corporation. Data Catalogue 2 System, Data Administrator's Handbook, Bedford, Massachusetts, 1977.

[28] Synergetics Corporation. Data Catalogue 2, Bedford, Massachusetts, July 1981.

[29] University Computing Company. UCC Ten Data Dictionary/Manager Technical Information Guide, Dallas, Texas, 1977.

[30] University Computing Company. UCC Ten Data Dictionary/Manager, Concepts and Facilities, Dallas, Texas, 1979.

## About the Author

Dr. Beverly K. Kahn is an Assistant Professor of Management Information Systems at the School of Management of Boston University. She received her Ph.D. in Industrial and Operations Engineering from the University of Michigan. Dr. Kahn's current research focuses on the practice and effectiveness of data administration. She is a frequent contributor at conferences, member of advisory panels, and consultant on information resource management, database design, and requirements analysis. Her methodologies for requirements analysis and database design are used by several major corporations and government agencies.
