---
otero_id: 27203
otero_key: "E2US38P3"
title: "The Data Dictionary: An Evaluation from the EDP Audit Perspective"
authors: "Michael T. Vanecek; Ira Solomon; Michael V. Mannino"
year: "1983"
journal: "MIS Quarterly"
doi: "10.2307/249074"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
The Data Dictionary: An Evaluation from the EDP Audit Perspective
Author(s): Michael T. Vanecek, Ira Solomon and Michael V. Mannino
Source: MIS Quarterly, Vol. 7, No. 1 (Mar., 1983), pp. 15-27
Published by: Management Information Systems Research Center, University of Minnesota
Stable URL: http://www.jstor.org/stable/249074
Accessed: 03-02-2016 05:55 UTC

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# The Data Dictionary: An Evaluation from the EDP Audit Perspective

By: Michael T. Vanecek
Ira Solomon
Michael V. Mannino

## Abstract

The data dictionary system is a documentation source that is useful for management reviews of existing and proposed systems, EDP audits, and system development functions. Early data dictionary systems had limitations that reduced their effectiveness and contributed to their limited usage. Many of these limitations have been or are being resolved with the result that evolving data dictionary systems offer many benefits to management and EDP auditors. This article evaluates the features, potential benefits, and limitations of data dictionary systems from the perspective of the EDP auditor.

Keywords: Data dictionary, database administration, data management, database management systems, EDP auditing

ACM Categories: H.2.7, K.6.1, K.6.4

## Introduction

A data dictionary (DD) system manages a database of information system descriptors $[16]$ . Such descriptors may be concerned with programs, files, users, databases, hardware, procedures, or other systems attributes. DDs can function as a documentation source for existing systems and can provide a measure of control during the development of new systems. Hence, a DD system can be used as an audit tool in all phases of the systems development life cycle (SDLC). Usage of DD systems to achieve EDP audit objectives has, however, been less than expected. The purpose of this article, therefore, is to describe the features and limitations of DD systems and to provide an evaluation from the perspective of the EDP auditor.

The EDP auditor perspective is taken herein rather than the perspective of the external, or independent, auditor because the former is likely to make greater direct use of the capabilities of DD systems. If the results of the EDP auditor's work are relied upon, however, the external auditor can be affected indirectly by the capabilities and limitations of the DD system.

A wide assortment of DD systems are commercially available; each system has its own set of defined features and data entity relationships $[1, 5, 6, 14]$ . This discussion of DD system features and limitations is not limited to any particular DD system. Rather, a general approach is taken by discussing common features and limitations of DD systems from the EDP auditor's perspective.

First an overview of DD systems is presented. This overview is followed by a review of the perspective and role of the EDP auditor. The DD system is next evaluated from an EDP audit perspective including a description of the major sources of information (audit evidence) that can be generated using a DD system. DD system limitations and management considerations are then discussed.

## Overview of a DD System

A generalized DD system, as illustrated in Figure 1 (from [1]), is a computer information system composed of:

\- a database called the dictionary that contains data describing an organization's meta-data, i.e., the organization's data and its associated structures, processes, users, applications, and equipment,

\- retrieval and analysis capabilities designed to assist a wide range of users in developing applications,

\- report writer features providing for predefined reports, customized reports, and a user defined reporting capability,

\- extensibility capabilities designed to allow users to extend the capabilities of a DD system to meet unique user requirements,

\- data management tools that are intended to ensure the security, validity, recoverability, and integrity of the data dictionary system and its databases,

\- functional interfaces that enable other software modules to access the dictionary, and

\- translation services between the metadata and dictionary formats.

Not all of the currently available DD systems provide all of these features. Many early DD systems were designed to be document generators rather than information systems aids. However, later designs have incorporated program interfaces and many now offer a full range of automated services. The expansion of database technology has aided in the improvement of DD systems. It is the combination of the automated features of the DD system along with its informational content that makes modern DD systems so useful as an audit tool.

## The EDP Auditing Perspective

EDP auditing encompasses the traditional external auditing concerns of asset safeguarding and data integrity together with the issue of whether or not the organization is effectively and efficiently accomplishing its goals. Since EDP auditing is broader in scope than is external auditing, the EDP auditor has a multifaceted role $[11]$ . For example, the EDP auditor is typically concerned with security, application development, application systems controls, data integrity, systems software, SDLC management, general EDP operational procedures and controls, systems maintenance procedures and controls, systems acquisition, information resource management, and management of the information systems audit. Given this broad scope of interest, the EDP auditor needs to have knowledge of accounting and traditional auditing methodologies, computer technology, information systems theory, management science tools, and behavioral and social considerations.

The EDP auditor's area of expertise and interest often coincides with that of other information systems professionals. For example, the EDP auditor participates in new system development projects and in the monitoring of existing EDP systems and their operation. These systems are designed, developed, and maintained by systems analysts and programmers, and are used by individuals possessing varying levels of expertise. The focus of the EDP auditor, however, typically is different from that of systems analysts, programmers, and users. The EDP auditor is especially concerned with systems internal control and auditability taken from the viewpoint of an objective observer. Consequently, the EDP auditor typically has the task of reviewing the controls and procedures associated with an organization's information assets.

Included in the reviews of the control and management aspects of an organization's information systems resources are reviews of application system controls, data integrity, and all phases of the SDLC process. Each of these reviews utilize similar sources of information. For example, one of the EDP audit tasks associated with reviews of application system controls and data integrity is an inspection of the system to identify the flow of data and controls. Also, one of the tasks associated with the review of the SDLC process is an examination of an organization's development process relative to its adequacy and compliance with specific standards. User manuals, procedure manuals, policy manuals, program documentation, record and file layouts, flow charts, organizational standards, and industrial standards are all potential information sources. Much of this variety of control, data integrity, and SDLC review information is contained in the data dictionary. Hence, the DD system can be used to facilitate the EDP audit process.

![](/api/attachments/E2US38P3/fulltext/images/2e2ec9cc44f38f10318747562c94e95751c3b79a5b08508da8bf04e28029d309.jpg)  
Figure 1. Data Dictionary Systems Functions

The role of EDP auditors typically requires them to face stringent time and cost constraints in seeking to accomplish their objectives. New systems are typically being installed and old systems are in a continual state of change. Rapidly changing technology is also creating increasing demands on EDP auditors. Accordingly, most EDP auditors could benefit from productivity increasing tools such as the data dictionary.

A DD system can also be an extremely useful EDP resource management tool $[8]$ . It is one of the major tools available to the data administrator $[12]$ . For example, DD systems can be used to organize and define the data items and their relationships, the storage organization and access characteristics, and user oriented information. The DD serves to enhance the effectiveness and efficiency of the EDP operation by providing an orderly method for managing the definition and description of an organization's data.

## Evaluating the DD from the EDP Audit Perspective

A modern and properly managed DD system provides the EDP auditor with three major sources of information (audit evidence). The DD system can serve as a documentation source for (1) automated controls, (2) manual controls, and (3) source code control violations. Each of these information sources is examined in detail in the following subsections.

## Automated controls

System documentation is an important source of audit evidence in reviews of application controls, data integrity, and the SDLC process. Given appropriate information, an understanding of the system can be gained by performing a type-level audit. In a type-level audit the EDP auditor identifies the flow and effect of each transaction type along with the controls that are designed to ensure the correct processing of the transaction. Consider, for example, a transaction that processes customer payments. The type-level audit reveals that the payment transaction debits a cash account, credits a subsidiary accounts receivable ledger, and updates the customer's record with the payment. The payment transaction is subject to controls such as edit checks applied by the database management system, a check of authorized users of the transaction, and control procedures that govern the opening of the mail and batching of payments.

The extensive documentation capabilities of a DD system facilitate a type-level audit. In particular, the DD system provides a cross reference between the different types of documentation. For example, the auditor can ascertain directly from the dictionary the names of authorized users of a transaction, the data fields that a transaction updates, and the edit checks applied to the fields of the accounting database. Developing EDP audit methodologies, such as defined in Security Audit and Field Evaluation for Computer Facilities and Information (SAFE) [9], require the data dictionary to contain at least type-level information about the data elements.

Most DD systems feature several retrieval methods such as predefined reports, high level query languages, and report writing languages so that an EDP auditor can obtain the documentation in the desired format and quantity. DD systems also provide numerous integrity controls that help ensure the quality of the documentation. Most DD systems utilize proven integrity techniques such as edit checks, recovery procedures, shared access control, and security checks. Thus, the DD system provides a fully managed database of documentation.

Historically, DD systems have documented only the implementation phases of the SDLC (see Figure 2). Hence, the dictionary contained only a description of the system in terms of files, programs, databases, jobs, and other data processing entities. However, DD systems have expanded to cover the business analysis and design phases. Many packages can now describe a system from a non-implementation viewpoint, i.e., in terms of processes, data flows,

Evolving documentation

![](/api/attachments/E2US38P3/fulltext/images/2931efbc0121ed8e9ce71ae3b9a859232f57be2b54081cbd3104c1c175ab041a.jpg)  
Figure 2. System Development Life Cycle

validation criteria, source document definitions, report formats, authorization requirements, and conceptual entities. For example, Proform, Inc. has been expanding their use of DD systems. They are using ADR's Datadictionary, and its integrated interface to their database control systems, as an automated documentation system to provide accurate and up-to-date documentation reports. Proform, Inc., through the addition of descriptions of system documentation, distribution reports, and job/program relationships, is finding the Datadictionary to be an important control and documentation tool [7].

The State University of New York at Albany has also found the DD system to be a useful tool in the SDLC process. Their motivation was a need to improve and control the documentation process. Semprevivo [13] discusses how their dictionary/directory concept developed into a development tool for installing an online transactional system by a staff relatively inexperienced with online systems. They have since used their DD system to develop two other major systems. The DD system is an integral part of their design process and is used throughout the design and implementation phases. They found the use of a DD system provided an improvement in the quality and speed of the systems development process, reduced system maintenance requirements, and improved control.

The EDP auditor benefits from modern DD systems in at least two ways. First, the efficacy of controls can be identified early in the SDLC. Since it is generally less expensive to insert controls early in the SDLC, early participation of the EDP auditor can be useful in reducing the costs associated with designing and installing system controls. Second, the DD system encourages the active involvement of the EDP auditor in the design phase. The DD system provides a common basis for communication among all parties involved in the system design phase. In addition, the EDP auditor can use the control specifications contained in the dictionary as a major source of information on which to base sign-off of the design phase.

One example of EDP auditor use of the DD system during the SDLC is provided by Clark and Butler [4]. They describe Texaco's EDP auditor involvement and use of a data dictionary during the SDLC. A Quality Review Board is formed consisting of user, management, data processing, and EDP audit representatives. This group reviews the EDP project at the completion of the analysis phase, the design phase, and the integrated system development phase. At each review, the Quality Review Board examines the ongoing documentation stored within the DATAMANAGER dictionary. Reliance on the dictionary is achieved because Texaco uses the DATAMANAGER dictionary for all phases of the SDLC.

The DD system can also assist EDP auditors in the use of generalized audit software and in the audit of program changes. For example, the EDP auditor may wish to use generalized audit software to sample records from production files. These packages require information about file characteristics such as record length, record type, blocking factor, file size, and record layout. The auditor can obtain the data descriptors from the DD system reports and then encode them in the format required by the audit package.

If the DD system and the audit package are integrated, the data descriptors, in the appropriate format, can be entered directly to the audit package (see Figure 3). The audit package sends a request directly to the DD system which returns the appropriate values. Thus, the auditor is relieved entirely from encoding the file characteristics. However, in either case, integrated or not, the DD system would provide the EDP auditor with accurate and complete data descriptors that would otherwise be difficult to obtain.

![](/api/attachments/E2US38P3/fulltext/images/5861dc36d1fefa644fdb254fe7158d62418b368eb6c73007b19dbfa6ab16d2fe.jpg)  
Figure 3. Integrated DD System and Audit Package

## Manual controls

The EDP auditor is also concerned with manual internal controls. For example, segregation of duties between programmers and computer operators, physical control in the computer room or tape library, or access control over tapes or disk packs are all manual controls. It is not uncommon for the EDP auditor to use procedure and policy manuals, as well as control flow charts, to document manual controls.

DD systems can be useful for maintaining the documentation associated with manual internal controls. Appropriate information concerning the internal control system, such as task assignment or asset control responsibilities, can be maintained within the DD system. The EDP auditor can then use the DD system to evaluate apparent strengths and weaknesses of the internal control system, e.g., separation of duties or unauthorized release of assets. The DD system then becomes an automated internal control evaluation system. For example, the TICOM II System is one such automated internal control evaluation system [2]. The internal control system is documented through the use of an Internal Control Description Language (ICDL) containing four major entity types:

1. Object — an item managed by the accounting system such as a form or check;

2. Repository — a source, destination, or temporary storage for an object such as file drawer;

3. Operation — a procedure involving actions such as review, transfer, wait, and assign; and

4. Task — the assignment of an operation to a person.

The TICOM II system manages all the pertinent relationships among these entity types and allows ad hoc query of the documented controls.

The standard TICOM II system may not meet all documentation needs. If this is the case, the EDP auditor can develop a customized TICOM II system by using the DD system extensibility feature. This feature permits the EDP auditor or system user to add new types of entities, relationships, and attributes to the dictionary structure. Most current DD systems have an extensibility capability although they vary widely in their characteristics. For example, some DD systems force a new entity type to be based on an existing type, e.g., a new entity type “Operation” would have to be based on an original entity type “Program.” The Operation entity type then assumes the attributes of the Program entity type. New attributes also can be defined which pertain only to the Operation entity type. In contrast, some DD systems provide unrestricted extensibility. In such systems, any new types of entities, relationships, and attributes can be defined without being based on existing types. For example, Ross [12] describes the construction of a procedures data dictionary using the extensibility feature of a DD system. He discusses the motivation, solution, and benefits of using a DD system for this purpose.

## Automated and manual controls

Considering both automated and manual controls, the advantages accruing to the EDP audit staff through the use of a DD system to document internal controls are threefold. First, the EDP audit staff can use all the features of the dictionary system. The EDP auditor simply defines the documentation database and the DD system provides the method to insert into, retrieve from, and manage the documentation database. Second, the EDP auditor's documentation database becomes a part of the evolving corporate dictionary. As a result, the EDP auditor may be able to identify new relationships between the different types of documentation (e.g., the links between manual and automated procedures). Third, many DD systems provide a run-time interface so that authorized programs can access the dictionary via call statements. This feature might be utilized by writing a program that would analyze the strengths and weaknesses of the documented controls. Some advanced programming might be required for this task, but the capability is available for those cases where it can be cost/benefit justified.

## Source code controls

The review of source program change controls, and the compliance testing of those controls, is especially critical because of the potential for irregularities to be introduced through unauthorized source program modifications. Hence, the EDP auditor must be able to ascertain that only authorized changes are being made to the system and that controls are in place that prevent unauthorized changes. Without source change controls a computer programmer could, for example, violate the asset protection objectives by inserting special routines in critical programs. A routine might be inserted that truncates all paycheck amounts and deposits the remainder in the programmer's own account. Without adequate EDP audit procedures, these types of irregularities are likely to go undetected. Application development systems using integrated dictionaries can be very useful in establishing source change controls.

A DD system that is combined with a precompiler or library manager creates an integrated development system that can provide added assurance against unauthorized program change. Both the EDP auditor and data administrator can verify that the dictionary account of a program is accurate, i.e., a program is allowed access to the predesignated data descriptors and only authorized programmers can precompile the program. For example, in Figure 4, before the compilation begins, the precompiler checks with the dictionary to make sure that the programmer is authorized to access the source program. Then, during translation, the precompiler enforces the restrictions in the dictionary such as not allowing a payroll program to copy a description of the accounting database. In addition, the precompiler produces an audit trail in the dictionary. Details such as the date compiled, number of lines, number of compiles, modules copied, and data descriptions copied are noted in the dictionary and, therefore, are available for EDP auditor review.

![](/api/attachments/E2US38P3/fulltext/images/ba590ac254a703b4237616a0176b026030c50d2487602c47fc029ae49611a064.jpg)  
Figure 4. Integrated DD System and Precompiler

Another concern of the EDP auditor is that production programs, databases, jobs, and transactions behave in the prescribed manner. One way to control these is by safeguarding the source code. The EDP auditor needs assurances that the production object program resulted from the source code that is in the production library. The authors have already illustrated how a properly interfaced dictionary system, precompiler, and library manager provide stringent controls over source code. In concert, these tools provide an audit trail of changes and prevent the copying of unauthorized data and module descriptors.

The DD system source code management approach can be very effective, but it is not always available and does not always provide for detective-like checks of production source code. Not all DD systems interface with a precompiler and library system. There are many languages that do not have precompilers. For example, except for catalogued procedures, a precompiler is not generally available for IBM Job Control language. And, of course, there are no precompilers generally available for assembly language programs. Also, sometimes the precompilers are not used because they add another layer of overhead, i.e., precompiling and compiling the source code.

Even if the integrated set of tools is available and working, the EDP auditor may still want some type of technique to be able to spot check the production source code. Manual spot checks are laborious and error-prone, and are normally not very useful. On the other hand, the DD system can provide a computer aided method for verifying production source code.

For example, the EDP audit group of the Republic National Bank of Dallas recognized this opportunity and developed several audit software packages around their DATAMANAGER dictionary system [3]. One audit routine compares any production source program, database description, and file description with the standards in the dictionary. It notes any differences between the two, such as different compilation dates, line counts, and data item descriptors. Another audit program compares listings of job control statements with the standards in the dictionary. This routine detects unauthorized programs, utilities, job steps, and files in the job. It lists any discrepancies about device types, access methods, record lengths, and block sizes. All exceptions noted by the audit routines are investigated by the EDP audit staff. Each of these audit programs utilized the CALL interfaces provided by DATAMANAGER dictionary system [10].

Figure 5 shows the data flow of a general source code checker. The checker is used to determine if the source code adheres to installation standards. The Syntax Profile describes the standards associated with the language, e.g., keywords, margins, and end of line delimiters. Any structured language can be described by a Syntax Profile. The Control Profile contains the standards pertaining to the programs, e.g., naming rules, indentation requirements, and structured programming rules. In addition, items such as file descriptions, modules called by each program, subschema definitions, and programmers authorized access to each program could also be included. The dictionary contains definitions of the resources applicable to a particular source code, e.g., complete descriptions of files, databases, attributes, and so on. The Source Code Checker processes the source code against the standards and notes violations of these standards in a report. Although not yet commercially available, MSP, Ltd. is expected to announce shortly a tool called Control Manager which is similar to this hypothetical Source Code Checker [15].

## DD System Limitations and Management Considerations

Although a DD system can be a powerful audit tool, it is not without limitations. One aspect that should not be overlooked is that the DD system is itself a valuable and critical asset whose validity and integrity must be safeguarded. Appropriate backup and recovery controls should be provided for the data dictionary. In addition, access to the entire DD system provides access into the entire organization's data processing resources. The capabilities that make DD systems so powerful also offer a potential for abuse. Consequently, user and application program access controls are needed to prevent misuse of and unauthorized access to the DD system. Further, it is expected that data administrators, and to a certain extent EDP auditors, typically will have complete access to the entire data dictionary. This, plus the nature of the positions, can result in significant system control being concentrated at a single point in the organization. Adequate compensating controls, usually administrative in nature, will be a necessary consideration in the management of DD systems.

![](/api/attachments/E2US38P3/fulltext/images/dafdf419258f99749499d9a0b3e4345cee4940e84af74a71fa9447edc63ea070.jpg)  
Figure 5. Overview of a Source Code Checker

DD systems can be difficult to manage. A major source commitment is required to implement an effective DD system. The acquisition of a dictionary system requires the establishment of a data administration group and charter. The charter should outline standards about the use of the dictionary system. The data administration group should have high visibility in the organization, usually independent of system development groups. The deployment of both the charter and the new data management group may cause friction within the organization. Even after the data administration group and charter are installed, determining what the dictionary contents should be may be very difficult. Many organizations just document new systems or selectively document old systems. It can take an organization several years before the dictionary system is fully used.

Another limitation associated with many DD systems is the lack of an overall methodology. Ideally, the DD system should be the single repository of an organization's meta-data. Thus, the DD system should support the entire SDLC process. Most DD systems provide some support for differing methodologies in the form of extensibility and user defined reporting. More comprehensive support, however, is presently uncommon. For example, it would be very useful if DD systems could interface with interactive graphics packages. Then diagrams such as data flow diagrams and structure charts could be rapidly produced.

In addition, SDLC control points and inter-phase mapping should be built into the DD system. Control points help ensure the completeness, consistency, and accuracy of the system specification at each step in the SDLC, e.g., checking that a data flow diagram is balanced and that all data items have an input source and output destination. Inter-phase mapping allows the specifications defined in a prior phase to be easily incorporated into the next phase; e.g., the conceptual data elements defined in the business analysis phase should be incorporated into the design phase.

The dictionary system also should be flexible because a single methodology is not likely to be appropriate for all circumstances. It is desirable to be able to incorporate the best techniques from several different methodologies. Although most existing DD systems do not provide this level of support, many are making strong advances in that direction. The audit implications are that all controls are not going to be documented in the dictionary as early as might be desired (i.e., before the physical design phase of the SDLC).

Another limitation, as described earlier, is the lack of support for control documentation. The most that the DD system can provide is an unrestricted extensibility feature. The EDP auditor is still forced to devise the control documentation model, its associated documentation analysis, and the required reports. Again, comprehensive support would be very useful. The DD system should provide a generalized prepackaged model including interfaces to interactive graphics, a documentation model, and predefined reports. No such packages are yet available.

Many DD systems can be difficult to use. The user often must learn a complicated query language. Secondary users of the dictionary system, such as systems analysts and EDP auditors, may not be willing to accept the burden of laborious query languages. For this reason, many dictionary vendors are in the process of providing simpler and less time-consuming user interfaces. Large DD systems can also cause significant performance bottlenecks. Some DD systems do not provide adequate response times in a high concurrent usage environment. Sometimes the bottleneck is the fault of the supporting computer system and sometimes it is the fault of the DD system.

Another problem stems from the existence of multiple dictionaries. An organization may use several different dictionaries because of the limitations of their DD systems or because of political influences which require a separate dictionary for each project. DD vendors do not support multiple dictionaries so that concurrency and consistency is left to the using organization. Of course, this increased redundancy may cause a reduction in the effectiveness of the overall corporate information resource management plan.

A similar problem is the existence in an organization of DD systems from different vendors. Different vendor DD systems may be acquired because of product features, vendor pressures, and political influences within the organization. The problem can be compounded if each one of the DD systems is implemented with multiple dictionaries. Multiple vendor DD systems will require the EDP auditor to know which dictionary to access and how each DD system works. The EDP auditor will need to learn the syntax, and query language characteristics for each of the different DD systems. In addition, some assurance that information contained in the multiple dictionaries is consistent, is necessary. In this instance, the EDP auditor is faced with inconsistencies due to vendor differences as well as redundancies due to multiple dictionaries.

## Conclusions

The DD system manages a documentation database and, therefore, has the potential to be a very useful EDP audit tool. The EDP auditor can browse through this database to perform type-level audits and to obtain data descriptors for generalized audit software packages. The extensibility capabilities of the DD system can be used to customize the package to the user's unique needs. In addition, the interfacing of dictionary systems with precompilers and library managers has the potential for improving productivity during reviews of source code changes and integrity. Finally, audit programs that check source code for compliance with the standards in the dictionary provide for an automated verification of production source code.

The benefits of DD systems are not without their costs and limitations. For example, some existing DD systems: (1) fail to provide needed features (interactive graphics interfaces, documentation models, etc.), (2) are difficult to properly manage, (3) lack an overall SDLC methodology, (4) lack documentation control support and source code checkers, and (5) require complicated extensions by the EDP audit staff. In addition, the EDP auditor may need to keep track of which dictionary is used by each system. Finally, unless it is responsive and easy to use, some EDP auditors may be reluctant to use a DD system.

Despite such limitations, the authors are optimistic about the future of DD systems. Future DD systems are expected to provide improved control documentation and source code control features for the EDP auditor's use. The authors also expect that the interfaces and performance of dictionary systems will be upgraded. In the next few years, most major DD systems will become fully integrated into the SDLC (see Semprivivo for an example of how the DD system can be integrated into the SDLC [13]). Consequently, it will be possible to document controls early in the SDLC process.

Organizations will improve in their ability to manage and exploit the capabilities of DD systems as more experience is gained in their use. At the same time, as Kreitzer [8] points out, DD systems are a key to effective information resource management. Likewise, as discussed herein, DD systems have the potential to be one of the most valuable and useful tools available to the EDP auditor.

## References

[1] Allen, F., Loomis, M., and Mannino, M. "The Integrated Dictionary/Directory System," ACM Computing Surveys, Volume 14, Number 2, June 1982, pp. 245-286.

[2] Bailey, A., Gerlach, J., McAfee, R., and Whinster, A. "Internal Accounting Controls in the Office of the Future," Computer, Volume 14, Number 5, May 1981, IEEE, pp. 59-72.

[3] Baker, H. "Data Dictionary as a Tool for Auditability and Control," in Proceedings of North American DATAMANAGER User Group Conferences, May 1979, Washington, D.C.

[4] Clark, W. and Butler, C. "DATAMANAGER Within the Development Life Cycle at Texaco, Inc.," in Proceedings of North

American DATAMANAGER Users Group Conference, October 1981, Denver, Colorado, pp. 30.1-30.34.

[5] Curtice, R. and Dieckman, E. "A Survey of Data Dictionaries," Datamation, Volume 27, Number 3, March 1981, pp. 135-158.

[6] Ewers, Jack E. "How to Evaluate a Data Dictionary," Computerworld, March 9, 1981, pp. In Depth/1-12.

[7] “Fiberglass Maker Sets Up Eight Systems in Two Years With Data Dictionary's Aid,” Computerworld, June 28, 1982, pp. SR 24.

[8] Kreitzer, Lawrence W. "Data Dictionaries — The Heart of IRM," Infosystems, Volume 28, Number 2, February 1981, pp. 64-66.

[9] Krause, L. SAFE — Security Audit and Field Evaluations for Computer Facilities and Information, AMACOM, New York, New York, 1980.

[10] MSP, Ltd. DATAMANAGER User's Guide, MSP Technical Documentation, London, England, 1980.

[11] Rittenberg, L. and Davis, G. "The Roles of Internal and External Auditors in Auditing EDP Systems," The Journal of Accountancy, Volume 148, Number 12, December 1977, pp. 51-58.

[12] Ross, R. Data Dictionaries and Data Administration, AMACOM, New York, New York, 1981.

[13] Semprevivo, P. “Incorporating Data Dictionary/Directory and Team Approaches Into the Systems Development Process,” MIS Quarterly, Volume 4, Number 3, September 1980, pp. 1-15.

[14] Snyders, J. "Data Dictionary: The Manager in DBMS," Computer Decisions, Volume 13, Number 11, October 1981, pp. 36-46.

[15] Stenton, D. “Datamanager/Control Manager Interface,” in Proceedings of North American DATAMANAGER Users Group Conference, October 1981, Denver, Colorado.

[16] "The British Computer Society Data Dictionary Systems Working Party Report," DATA BASE, Volume 9, Number 2, Fall 1977.

## About the Authors

Dr. Michael T. Vanecek is an Associate Professor of Business Computer Information Systems at North Texas State University. He has a Ph.D. in Accounting and Information Systems from the University of Texas at Austin, an M.B.A. from the University of Houston, and an M.E.E. and B.S.E.E. from North Carolina State University. Dr. Vanecek teaches courses in business computer information systems, EDP auditing, and accounting. His research interests include distributed systems, software and taxes, information resource management, and EDP auditing. He has had several articles published in computer information systems and accounting journals. He is a member of SIM, EDPAA, ACM, AAA, DPMA, AIDS, and IEEE. Dr. Vanecek has over twenty years experience in the computer industry and is an active consultant for both industrial and governmental organizations. He holds the P.E., C.D.P., and C.I.S.A. certifications.

Dr. Ira Solomon is Assistant Professor of Accounting at the University of Arizona. Dr. Solomon received his Ph.D. from the University of Texas at Austin and was previously a member of the audit staff of Peat, Marwick, Mitchell & Co. Dr. Solomon has published articles in the Journal of Accounting, Organizations and Society, and Organizational Behavior and Human Performance, as Performance, and Organizations and Society, as well as elsewhere. He is a member of the American Institute of Certified Public Accountants and the American Institute of Decision Sciences. He was a member of the 1982-83 Auditing Standards Committee of the American Accounting Association. He holds the C.P.A. certification.

Mr. Michael V. Mannino is a doctoral candidate at the University of Arizona, Tucson, Arizona. His research interests include database design, data dictionary systems, and heterogeneous database management systems. He is presently working on a dissertation that is concerned with the design of global schemes for heterogeneous database management systems.
