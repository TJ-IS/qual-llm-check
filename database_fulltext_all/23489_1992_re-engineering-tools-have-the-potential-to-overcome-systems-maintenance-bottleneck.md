---
otero_id: 23489
otero_key: "RWUY2BAM"
title: "Re-engineering tools have the potential to overcome systems maintenance bottleneck"
authors: "Robert Moreton"
year: "1992"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1992.14"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Re-engineering tools have the potential to overcome systems maintenance bottleneck

ROBERT MORETON

School of Information Systems, Birmingham Polytechnic, Birmingham, UK

The paper argues that the current generation of re-engineering tools can provide significant benefits for those organizations which have high applications maintenance overheads. The paper classifies the different types of re-engineering tools and their application potential. It is argued that these tools promise to provide a migration path towards the integrated computer-aided software environments which will emerge over the next 5–10 years. This paper follows on from work which the author has undertaken for the CSC-Index Performance Enhancement Programme (PEP). PEP is a continuous programme that is open to organizations wishing to measure and improve systems development and productivity.

## Introduction

In an earlier paper Moreton (1990) reflected that software maintenance can be an expensive and complicated business. The paper presented a process model which describes a properly controlled environment for managing system and software changes. In such an environment, it was argued, it is also possible to evaluate the benefits of using the newer methods and tools for software maintenance.

An increasing number of software tools are becoming available to support the stages of analysis and design in the maintenance process. Several recent articles (Abi, 1988; Guest, 1990; Jones, 1990a; Jones, 1990b) have highlighted the range of products available. These are aimed at speeding up the laborious activities such as code analysis which are often associated with the task of software maintenance.

Such so-called re-engineering tools have been developed from a number of different sources. Some, for instance, have been developed to supply software maintenance documentation (Glass, 1990). Others have emerged from a CASE environment in an attempt to 'rejuvenate, enhance and migrate old applications' (McNurlin, 1988).

However, as in many areas of business computing, the field of applications in re-engineering has been subject to over-eager claims by suppliers and is described in confusing new terminology. The purpose of this article is twofold: first to clarify the different types of re-engineering tools and their application potential; second, to identify the ways in which re-engineering tools can be used in the short-term to help manage existing applications and, in the longer term, to help load data from these applications into the emerging integrated computer-aided software engineering (I-CASE) development environments.

## Re-engineering tools and existing applications

In the short term, re-engineering tools will provide many organizations with a means of making great savings in two areas.

First, they can be used to reduce the effort required to maintain the existing applications portfolio, which on average, consumes at least 60% of the development department's effort (Wolfson, 1990). Second, they can be used to prolong the usefulness of some of the older applications, in which most organizations have invested many thousands of person-days.

Tools for re-engineering existing Cobol code will provide a real opportunity for many organizations to break free of the legacy of applications originally developed many years ago. In the near future tools for re-engineering applications written in the more common fourth-generation languages will also become available. In fact, it will be easier to develop these re-engineering tools because fourth-generation languages generally have fewer syntactical constructs than Cobol, and the applications developed with them are newer, which means that a re-engineering tool does not have to be designed to cater for the logical complexity that usually arises as a result of repeated enhancements and maintenance.

## Categories of re-engineering tools

Re-engineering tools can be categorized into three groups – redocumentation, restructuring and renovation, and inverse-engineering. Each requires its own procedures and different levels of skill are needed to use them. Clearly, each will have a role to play, and development departments will have to assess their needs for the various types of re-engineering facilities in the short, medium and long term. In the short to medium term, they can be used to simplify the maintenance task, to move to a new technology such as a relational database, to provide links that can integrate existing applications or databases, or to facilitate the use of more advanced architectures such as powerful workstations that use windowing techniques and are based on a client-server configuration. In the longer term, their importance will increase as their role in transferring the existing applications portfolio to an I-CASE development environment is recognized.

## Redocumentation tools

Redocumentation tools provide a means of automating the various tasks involved in documenting an application (see Figure 1). Typically, they produce process flow charts and cross-reference listings directly from the source code and data definitions. Examples are Flowtec from Maintec SA that documents Cobol programs and Abstract from Advanced System Concepts in the United States that documents RGP III code. The outputs enable developers to assess the likely impact of a change and to estimate the effort required with greater accuracy.

Redocumentation tools have been available for some time, but early versions tended to produce large quantities of printed output, which the developer had to go through manually. More recent versions provide interactive screen-based access to the documentation. Redocumentation facilities will become standard features of many other types of tool in the near future.

Since early 1987, the Centre of Software Maintenance at Durham University has been investigating the role of redocumentation tools in the automation of maintenance (Goodwin, 1991). One project, backed by Rank Xerox, a major hardware and software supplier, and the software-support specialists, AGS Information Services, aims to produce a system for documenting applications in a structured manner when an application is first developed, and then semi-automatically redocumenting the application when enhancements and changes are made. This will provide a marked improvement on current redocumentation tools.

Code-analysers also fall into the redocumentation category. These provide information on how well structured the code is, and assess the maintainability and testability of the code. This information can be used to estimate the cost of maintaining the applications in the future.

According to recent research carried out by IBM, 50% of the maintenance effort is spent analysing the code prior to making any changes. The logical step forward from redocumentation and code-analysis tools is therefore the interactive code-analysis tool. VIASOFT Inc has such a tool for screen-based interactive analysis of Cobol code and has promised an extension for SQL code. VIA/Insight, provides maintenance staff with a flexible means of accessing and analysing the existing code before carrying out any enhancements or maintenance. Another interactive code-analysis tool, PM/SS, from the Adpac

![](/api/attachments/RWUY2BAM/fulltext/images/0ea9306e06efaed3c36074d1dd6590f9fb88a07f50e0a8a02a957dc0c8e54f60.jpg)  
Figure 1 Redocumentation tools

![](/api/attachments/RWUY2BAM/fulltext/images/31b8d0dccd54bc5d309192743c19c0823007bfc9510e6fa0065b93549d435dd2.jpg)  
Figure 2 Restructuring and renovation tools

Corporation, has been used by Norwich Union, a leading British insurance company, to help analyse its existing applications before loading them into a data dictionary. In two pilot projects, the use of PM/SS reduced the estimated time to load application details into the dictionary by a factor of 10. Restructuring tools are used to structure and standardize the code of existing applications. Typically, they align the code to predefined standards, simplify the logic, and remove any redundant code (see Figure 2). Examples of restructuring tools are Retrofit and DataTec, from Peat Marwick Main and Co.

Renovation tools take the re-engineering of applications a stage further than straight-forward restructuring. The application is analysed and translated into a high-level design language, such as pseudo-code, that can then be changed before the application is re-created using structured and standardized code. An example of this type of tool is Recoder, from Language Technology Inc in the US.

Restructuring or renovating is obviously not appropriate for all applications – for instance, for an old, unstructured application where little maintenance has been carried out to date, or for an application that is near the end of its useful life. The use of restructuring and renovation tools can, however, bring major benefits to most organizations, particularly in helping to overcome the problems of maintaining applications that are either poorly documented or badly structured. Hartford Insurance, based in Connecticut, reports that maintenance costs have fallen by 20–50% on all the applications that have been restructured with Recoder. Maintenance staff do, however, have to spend considerable time becoming acquainted with the new code before the maintenance effort can be reduced.

## Inverse engineering tools

Inverse engineering tools start by reverse-engineering an application and its associated databases to a stage where they can then be 'forward-engineered' to create a new version of the application in a structured manner, and in a selected language (see Figure 3). They provide facilities for translating existing code and data structures into a specification of the application expressed in high-level business terms in the form of flow diagrams or a pseudo-English language. This specification can then be changed, if required, or loaded into a data dictionary before the application is recreated.

![](/api/attachments/RWUY2BAM/fulltext/images/88548e729f7cc5c847d9c5f7ee1c8bfd3af06651cc740d2716583d9719e38842.jpg)  
Figure 3 Inverse-engineering tools

Inverse engineering products have the potential to provide the greatest benefits of all the re-engineering tools. Currently, however, there are no inverse engineering products available that can reverse-engineer and forward-engineer both the code and the data, although Bachman Information Systems Inc has shown the benefits of inverse engineering in the data area. Bachman's products can inverse engineer the data structures from flat files and from hierarchical databases such as IDS, IDMS and IMS databases to create the equivalent data structures for IDMS and DB2 databases.

Bachman admits that the development of a tool to carry out the inverse engineering of data is easier than developing one to inverse engineer processes. Several complex problems have to be overcome before inverse engineering of processes will be possible:

(1) Extracting a description of the application in business terms from the complex computer code and data definitions, which in most cases do not contain all the information required to construct such a description. The task is also complicated by the great variations in coding practices.

(2) Providing a database management system that has sufficient power to hold all the results of the reverse-engineering process. Once a description in business terms has been extracted from the code, the information will need to be stored in a powerful database. To display and manipulate this information, some form of graphical tool will probably be needed to show clearly the relationships that have been constructed.

(3) Establishing a consistent means of describing applications. Currently, there are several means available (data-flow diagrams, problem-statement languages, object-oriented representations), but each has its limitations. Standards on how to manipulate such information on a screen will need to be created.

In the medium term, inverse engineering tools will become available to process both the processes and the data. These will need the assistance of an expert but will be very effective for loading details of existing applications written in third- and fourth-generation languages into an I-CASE data dictionary. The leaders in developing products in this field are Bachman and Language Technology Inc.

Research undertaken by the CSC-Index Performance Enhancement Programme, suggests that over the next few years, inverse engineering tools will evolve to the stage where they can analyse about 80% of the existing code; the remaining 20% will require human intervention. These tools, as Carlyle (1989) notes, will probably use some form of knowledge base – a database that contains information and rules – to help extract a description of the application in business terms. When a new problem is encountered, the user will add new rules to the knowledge base, enabling the tool to resolve a similar problem automatically when it occurs again.

## Re-engineering tools and future applications

As Duncan (1989) argues significant benefits will accrue if maintenance can be treated as ‘extended development’. In the longer term, this will be the result of using re-engineering tools which will change the way in which applications are developed and maintained. The life cycle of the traditional development environment, will be extended to include re-engineering, as shown in Figure 4. Many of the existing core applications will be transferred to the I-CASE environment, with the aid of re-engineering tools, by analysing the applications, restructuring them, and reverse-engineering them.

Before any decision is made to load the details of an existing application into the I-CASE data dictionary, code-analysis tools should be used to determine the condition of the application. The analysis will serve as a basis for estimating the effort to load the application into the dictionary, and for assessing whether it is worthwhile.

Once the size of the task is known, and the coding and data-naming conventions have been defined and standardized, restructuring and renovating tools can be used to structure the code to ensure that it is easier to understand. Standardizing the data, however, may be more difficult and very time-consuming as it will probably need to conform with existing data in the data dictionary or other applications.

Reverse-engineering tools can then be used to extract a description (in business terms) of the application from the code and data structures. This description will be transferred to the I-CASE development environment to forward-engineer the application.

Clearly, this will not be an easy process and will require considerable human intervention. However, it will permit existing applications to be transferred to the I-CASE development environment in a semi-automated and cost-effective manner, and will reduce the high proportion of development effort spent on maintenance.

## Conclusion

Advances in maintenance support tools have lagged behind advances in development tools. With the emergence of the current range of re-engineering products the situation is set to change in the immediate future. The current generation of re-engineering tools will provide significant benefits for those organizations with high applications maintenance overheads. At the same time, they promise to provide a migration path towards the I-CASE development environments which will emerge in the medium to long term. With the assistance of re-engineering tools, the task of defining the data models for all the various (and often fragmented) databases associated with an organization's existing core applications will become viable.

![](/api/attachments/RWUY2BAM/fulltext/images/de01cab310054f1eb2c749598e5ffc02f2c47e6cc559823e00918540546d44ab.jpg)  
Figure 4 The new applications life-cycle

McNurlin, B. (1988) Improving large application development. IS Analyser, March.

Moreton, R. (1990) A process model for software maintenance. Journal of Information Technology, May.

Wolfson, T. (1990) Shifting into reverse gear. Informatics, August.

## References

Abi, R. (1988) Software maintenance: tools and techniques. System Development, August.

Carlyle, R.E. (1989) Fighting corporate amnesia. Datamation, 1 February.

Duncan, M. (1989) The development seduction. System Development, December.

Glass, R.L. (1990) Help! My software maintenance is out of control. Computerworld, 1 December.

Goodwin, C. (1991) Tools to carve new tracks for the future. Computing, 28 February.

Guest, G. (1990) Breaking the code. Computing, 5 April.

Jones, K. (1990a) Speedy engineering from back to front. Computer Weekly, 4 October.

Jones, R. (1990b) Turning back to the future. Computing, 2 August.

## Biographical notes

Robert Moreton is Associate Head of School of Computing and Information Technology in the Faculty of Computing and Information Studies at Wolverhampton Polytechnic. He is also an associate consultant with CSC-Index. His particular interest is in methods and management approaches for systems development. A common theme of his work has been tracking and evaluating developments in information technology and forecasting the potential impact of these developments.

Address for correspondence: Robert Moreton, School of Computing and Information Technology, Wolverhampton Polytechnic, Wulfrun Street, Wolverhampton WV11SB.
