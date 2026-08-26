---
otero_id: 18434
otero_key: "4DVNFS4K"
title: "An assessment of CASE technology for software design"
authors: "Santosh K. Misra; Venkat Subramanian"
year: "1988"
journal: "Information & Management"
doi: "10.1016/0378-7206(88)90047-x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An Assessment of CASE Technology for Software Design

Santosh K. Misra

Department of Computer and Information Sciences, Cleveland State University, Cleveland, OH 44115, USA

Venkat Subramanian

Division of Business and Administrative Science, University of Wisconsin, Parkside, Kenosha, WI 53141, USA

A number of Computer Aided Software Engineering (CASE) tools for design and development of software systems have become available. These tools, unlike some of their predecessors, require only a microcomputer with minimal fixed disk space. Yet, these tools provide a powerful medium for development of software systems. A survey of such microcomputer based tools is presented. Three of these tools, Design/1, Excelerator, and Structured Architect are examined in some detail. A practical problem is analyzed and implemented using each of the three tools. Development experience and facilities are compared. Direction for future development of CASE is discussed with suggestions for increase in the power of this environment.

Keywords: CASE, Dataflow, Data dictionary, Structure chart, Diagram editor, Balancing.

## 1. Introduction

A number of structured methodologies exist for the design and development of software systems. Using these methodologies, the problem domain of a software system can be represented in abstract form, using tools such as data flow diagram (DFD), Warnier Diagrams [14], structure chart, etc. Typically, tools of structured system design call for partitioning of the problem domain into small functionally cohesive units (modules) and specifying all interfaces to these modules. The function of a module may be described using structured English, pseudocode, transition diagrams, or flowcharts. Experience reported by firms using these tools estimate savings of as much as 60 to 70 percent in the time required to perform an initial design [6,7].

System designs evolve through an iterative process of continual refinement and change. These involve tedious and time-consuming modifications to documentation. Hence there is an inherent tendency to resist change. This leads to a suboptimal design. Computers offer a solution to this problem, in the form of computer aided software

![](/api/attachments/4DVNFS4K/fulltext/images/ff1a2a2cf52e8cbde408fc5a8effdb4d42450954b2c198f1be89bc6c2c5f0308.jpg)

Santosh K. Misra received the DBA degree in Information Systems from Kent State University, Kent, Ohio in 1986. He is an Assistant Professor in the Department of Computer and Information Science at Cleveland State University. His research interests include Database Conversion, Computer aided software engineering environment and performance evaluation. Recent efforts have included studies of several fourth generation tools.

![](/api/attachments/4DVNFS4K/fulltext/images/e01d4610570388905cadbcb2071ce57bcb42cdaa49bffa4bcf6fd9576551f22b.jpg)

managerial levels, before joining Kent State University for his D.B.A. degree. Soon after completing his course work requirements, he served at Cleveland State University, Cleveland, Ohio for 2 years in the Computer and Information Sciences department. He is a member of ACS and DPMA.

Venkat Subramanian is Assistant Professor of MIS in the Business and Administration Division at University of Wisconsin–Parkside. He received his B.E. degree in mechanical engineering from Annamalai University in India. He is currently working on his research towards his D.B.A degree from Kent State University, Kent, Ohio. Soon after his B.E. Degree, he joined Hindustan Aeronautics Limited in India. He served the organization for 13 years in middle and senior engineering (CASE) tools. They allow the software engineer to develop the design specification interactively using computerized tools. Facilities of these CASE tools include picture generation and editing, dictionary generation, and design quality assessment. Because of the ease with which changes can be made, end user change requests can be incorporated without much effort. This is a definite advantage in terms of overall system quality.

However, the potential for conserving system development resources through the use of CASE tools is not yet fully exploited. When such tools mature, their use would become industry standard, and trends for this are already visible. This gives rise to a need for Business Schools to expose potential system analysts and designers to CASE technology. Industrial practitioners, who are not currently users of CASE technology, also need to consider their adoption since these tools provide a powerful system development environment leading to analysts' productivity improvements.

Currently a potential user of CASE technology is confronted with a multitude of tools, each claiming to be best. This paper presents a survey of CASE tools available for a personal computer. Three of these systems are examined in some detail. The paper presents a report on our experience with these tools. We believe this experience would be useful for potential academic and industrial users in integrating the use of CASE tools into their work environment.

## 2. CASE Systems

Appendix I presents a list of the CASE tools available for the personal computer. The list is not exhaustive since new tools are continually entering the market and existing tools are being upgraded and made available on other hardware.

A number of CASE tools also exist for use on main frames and work stations. For example, Software through Pictures from Interactive Development Environment of San Francisco runs on Sun $^{(TM)}$ and VAX $^{(TM)}$ work stations. Other such tools include The Solution (Wang VS Mini), TeamWork/SA (Apollo & Sun Workstations), and proprietary systems such as TAGS [11]. Readers interested in a more complete list of such products may consult [7].

An examination of Appendix I indicates that most of these tools focus on the structured analysis and design phases of a software life cycle. However, we believe that they will eventually mature to encompass the entire software development life cycle. For a discussion of the general capability and facility requirements for these tools the reader is referred to [9].

## 3. System Development Experience

The following three systems were used to implement a small system analysis problem:

1. Excelerator Release 1.7 [3]

2. Structured Architect Version 1.2 [12]

3. Design / I Version 3.50 [8]

Use of one problem allowed us to take a comparative view of the three systems. The implementation was done by two undergraduate and one graduate student; all were CIS majors, each had prior experience with the techniques of system analysis using Yourdon's methodology [13]. None of these students had any prior experience with CASE software.

A description of the system development problem is given in Appendix 2.

Table 1 gives a summary of the features of the three tools.

## 3.1. System Installation and Help Facilities

We installed Design/1 and Structured Architect in an ITT Extra machine, which is IBM PC compatible. This machine is equipped with a 10MB hard disk and a color monitor with standard graphics facility. The installation of these two software posed no special problems. Excelerator was installed on an IBM PC/AT with standard graphics and a mouse. None of the machines was equipped with any math coprocessors. These can enhance the speed of graphics generation.

On-line context sensitive help is available in all three systems. The help messages provided by Excelerator and Design/1 are generally short and cryptic. Structured Architect provides more meaningful help screens.

None of the three tools provide an on-line tutorial. Each system document provides a special tutorial section using a 'walkthrough' style of pre-$^{4}$ See also interfaces provided with the package: Programmer's workbench available on request.

Table 1  
Comparative Features (a).

<table><tr><td>Hardware Considerations</td><td>Excelerator</td><td>Design/I</td><td>Struct.Architec</td></tr><tr><td>Minimum RAM</td><td>640K</td><td>512K</td><td>320K</td></tr><tr><td>Recommended RAM</td><td>640K +</td><td>640K</td><td>512K</td></tr><tr><td>Hard Disk Support</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Flcppy Support</td><td>No</td><td>Yes</td><td>No</td></tr><tr><td>Mouse Based</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Keyboard Based</td><td>No</td><td>Yes</td><td>Yes</td></tr><tr><td>Disk Operating System</td><td>2.1 +</td><td>2.1 +</td><td>3.1 +</td></tr></table>

Table 1  
Comparative Features (b).

<table><tr><td>Adaptability/Portability</td><td>Excele-rator</td><td>Design/I</td><td>Struct. Archite.</td></tr><tr><td>Interfacing with Other Software</td><td>1</td><td>2</td><td>3</td></tr><tr><td>LAN Capabilities</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Micro/Mainframe Compatibility</td><td></td><td>Yes $^{4}$ </td><td>-</td></tr></table>

$^{1}$ Project management software interface.  
$^{2}$ ASCII file for input; IBM data dictionary; Cullinet data dictionary interfaces.  
$^{3}$ Provided only through ability to export information in the Encyclopedia to a standard DOS file for input to other systems.

Table 1  
Comparative Features (c).

<table><tr><td>Performance Considerations</td><td>Excele-rator</td><td>Design/I</td><td>Struct. Archite.</td></tr><tr><td>Methodology</td><td>1</td><td>2</td><td>3</td></tr><tr><td>Diagramming Standards</td><td>Fair</td><td>Fair</td><td>Fair</td></tr><tr><td>Cataloging System</td><td>No</td><td>No</td><td>Yes</td></tr><tr><td>Consistency Verification</td><td>No</td><td>No</td><td>Yes</td></tr><tr><td>Report Generation</td><td>Fair</td><td>Fair</td><td>Fair</td></tr><tr><td>Windowing</td><td>Fair</td><td>-</td><td>Poor</td></tr><tr><td>Plotters Interfacing</td><td>Limited</td><td>-</td><td>Limited</td></tr><tr><td>Printers Interfacing</td><td>Limited</td><td>Fair</td><td>Fair</td></tr><tr><td>Project Security</td><td>Good $^{4}$ </td><td>-</td><td>Fair</td></tr><tr><td>Zoom Facility</td><td>Good</td><td>-</td><td>Good</td></tr><tr><td>Explode Facility</td><td>Good</td><td>No</td><td>Good</td></tr></table>

$^{1}$ Yourdon [13], Gane & Sarson [4], Chen [1].  
$^{2}$ METHOD/1 [8] or other structured methodology.  
$^{3}$ Demarco [2].  
$^{4}$ hardware (PAL chip), the BLOCK, key diskette and passwords.

Table 1  
Comparative Features (d).

<table><tr><td colspan="4">Learning Considerations</td></tr><tr><td>Prompts and Pull Down Menus</td><td>Poor</td><td>-</td><td>Poor</td></tr><tr><td>On Line Help</td><td>Poor</td><td>Fair</td><td>Fair</td></tr><tr><td>Tutorial – On-Line Doc</td><td>No</td><td>No</td><td>No</td></tr><tr><td>Documentation</td><td>Poor</td><td>Poor</td><td> $Fair ^1$ </td></tr><tr><td>Ease of Learning</td><td>Fair</td><td>Fair</td><td>Fair</td></tr></table>

$^{1}$ Poor index facilities.

sentation. The examples in the tutorial are easy to follow and valuable to the first time user.

## 3.2. Picture Drawing and Editing Capability

Accelerator supports process-oriented graphs, such as data flow diagrams and structure charts; data-oriented graphs, such as data model and entity–relationship diagrams; miscellaneous graphs such as document and presentation graphs. The context diagram created using Excelerator for our trial project (AAR) is shown in Figure 1.

The graph creation and editing facilities in Excelerator are simple to use and provide a better human environment than the other two systems. Excelerator provides a good set of fonts, easy to use object size control methods and a set of graphics commands to manipulate the pictures. For example, moving an object in the picture is as simple as locating the cursor on the object and selecting the move option of a pull down menu. The cursor can then be moved to a new location, resulting in the translation of the object. Processes can be exploded (made more detailed) and the system keeps track of the exploded (children) processes with reference to the original one. This facility is very useful when complicated systems are modelled, requiring several levels of decomposition of a complex system component. The graphical objects are also linked to dictionary entries and updates are handled automatically. The screen display itself can be controlled through zoom operations (three magnification levels available); by this, segments of a diagram can be enlarged and viewed. This facility can also be used while printing the diagrams.

Drawing dataflows with Structured Architect involves seven simple steps:

1. select ADD DATAFLOW (Function key 6);

2. choose a starting point for the dataflow and position cursor;

![](/api/attachments/4DVNFS4K/fulltext/images/73a5f1298aedbe2206d3f09300b3a33ca8e7bb31f115225429cfbbf8a5dc653d.jpg)  
Fig. 1. Context Diagram from Excelerator.

![](/api/attachments/4DVNFS4K/fulltext/images/d6ec06e5d061b526f2bde480b8c5733fcdb4deef91467fca4d8021471dd43600.jpg)  
Fig. 2. First Level Decomposition from Structured Architect.

3. press enter to indicate origin;

4. draw dataflow by moving the cursor;

5. complete the dataflow;

6. move the cursor to the point where the data-flow name should appear on the diagram; and

7. enter dataflow name, as prompted by the system.

Facilities to move, delete and edit objects are comparable to those in Excelerator. However, unlike Excelerated, Structured Architect supports an AUTOCURVE option to draw curved dataflow arcs. Process decomposition, linking to the dictionary, is adequate and comparable to Excelerator. Figure 2 shows an example of the first level of decomposition of the AAR project using Structured Architect. This diagram was also constructed using the AUTOCURVE option. There is a one key zoom operation provided; for this the zoom level must be preset to one of the 10 levels available in the system.

A first time user of Structured Architect may find a few problems in drawing diagrams. Adjusting the display scale to a value so that the diagrams are legibly displayed is tricky. The font sizes for the names on the data flow diagrams are not controlled. Other problems encountered, while editing our DFDs, included difficulty with oversized diagrams extending beyond one screen and correcting misspelled object names.

Design/1 normally supports “straight line” flows, with an option for “curved lines” supported only on high resolution graphic displays. The image editor of Design/1 can be used to enter text, draw lines, create symbols and manipulate lines or blocks of text. Design/1 provides a zoom mode if Warnier Orr [14] data structured design is used.

All systems except Structured Architect support a reasonable sized graphics primitive library. We, however, did not find any method to create customized graphics primitives.

## 3.3. Data Dictionary Definition

The project dictionary (XLD) of Excelerator is fully integrated with other system components. For example, if the DFD is modified by adding/deleting processes or flows, the changes would automatically be reflected in the dictionary. This facility is useful for completeness and consistency verification of the system specification. The XLD is organized by entity types, making extraction of information by entity fairly easy.

Excelerator automatically tracks over 80 relationship types, including relationships among processes and their exploded sub-processes, data structures and their components, etc. When changes are introduced through any of the system facilities such as reports, DFDs, and flows, corresponding changes are made globally by the system. This facility is of great value in ensuring system description consistency.

The Diagram Editor and the Encyclopedia (data dictionary) of Structured Architect are fully integrated. The encyclopedia continuously keeps track of all the “parts” and “instructions” for the system. Therefore, information entered through the Diagram Editor is available for viewing and editing through the encyclopedia menus and vice versa. In addition, as a diagram is drawn and described, the encyclopedia collects, sorts, and catalogs all picture related information, which can then be independently viewed and edited. When a DFD is constructed and its objects are named, the object names are automatically collected and cataloged by Structured Architect. Also, as changes are introduced to these diagrams, the encyclopedia is updated without introducing redundancy. This facility makes the encyclopedia one of the most powerful component. Figure 3 shows a partial extract of the dictionary listing produced by Structured Architect for our trial AAR project.

The data dictionary capabilities of Design/1 include automatic generation of system object lists and complete cross-referencing with 'Contains' and 'Where-used' reporting. Obsolete object items can be identified through cross-reference listing. Therefore, even though the data dictionary updating capabilities are unlike the other two systems, the dictionary can be easily used for ensuring completeness of object descriptions.

## 3.4. Diagram Balancing and Quality Verification

Diagram balancing refers to matching of the flows in a parent process with the flows shown in the children processes. Since the children processes are a more detailed view of the parent process, any mismatch in data flows is deduced to be an error.

Agent-Update-Confirmation dataflow
Agent-Update-Request dataflow
AllStateReport dataflow
CalculatedCostPerAgent data element
CalculatedEquipmentSupplCost data element
CalculatedStateLaborCost data element
CalculatedSupportAdministrativ data element
CalculatedTotalCost data element
Command data element
ConfirmationText data element
Date dataflow
EmployeeName data element
EquipmentSupplyType data element
ExpenseCost data element
ExpenseTable dataflow
LineText dataflow
NumberOfAgents data element
NumberOfAgentsAdded data element
NumberOfAgentsDeleted data element
Overhead dataflow
OverheadScreenName dataflow
OverheadScreenTable data store
Productname data element
ProductTable data store
ProductType data element
Project data store
Project-Allocation-Reports dataflow
ProjectCode data element
ProjectHoursPerDay dataflow
ProjectIndirectLabor dataflow
Projectlabor dataflow
ProjectLine dataflow
QuarterConstant data element
QuarterValue data element
SortdTimeAllocRecord dataflow
State-Reports dataflow
StateConstant data element
StateDetailLine dataflow
StateDisplayname data element
StateSpecificColumnHeading data element
StateSpecificTitleLines dataflow
StateSpecReport dataflow
StateTable data store
TimeAllocation data store
TimeChargedInHours dataflow
Timesheet dataflow
TimesheetLine dataflow
TotalAgents data element
TotalConstant data element
TotalCost data element
TotalCostPerAgent data element
TotalDirectLaborCost data element

Fig. 3. Partial Dictionary Listing from Structured Architect.

Accelerator provides four options to examine graph validity:

1. Verification report which examines the structure of a DFD for free-standing objects and illegal connections.

2. Analysis report which lists the inputs and outputs of processes and data stores on a data flow diagram.

3. Level balancing which checks the consistency of data flows between two levels of a data flow diagram.

4. Graph explosion report which starts at one graph of any type and traces the explosion paths of the objects and connections on the graph.

The first three options help find omissions, redundancies, and inconsistencies in a graph. The fourth details the explosion paths associated with any graph. Validation of structured specifications in any system development is greatly aided by such facilities, making this a desirable feature.

<table><tr><td>Structured Architect</td><td>homecomp</td><td>04-12-1938</td><td>01:29:54</td></tr><tr><td colspan="4">Balance a process with its diagram (system wide)</td></tr><tr><td colspan="4">The parent process &quot;ProjectManagement&quot; has been compared with its diagram. The following problems have been detected:</td></tr><tr><td colspan="4">The following dataflows are inputs to the parent process but not its diagram:</td></tr><tr><td colspan="4">Agent-Update-Confirmation</td></tr><tr><td colspan="4">The following children of inputs to the parent process do not appear on its diagram:</td></tr><tr><td colspan="4">ConfirmationTextStateDisplaynameProductnameNumberOfAgents</td></tr><tr><td colspan="4">The following dataflows are outputs to the parent process but not its diagram:</td></tr><tr><td colspan="4">Agent-Update-Request</td></tr><tr><td colspan="4">The following children of outputs to the parent process do not appear on its diagram:</td></tr><tr><td colspan="4">ProjectCodeProductTypeNumberOfAgentsAddedNumberOfAgentsDeleted</td></tr><tr><td colspan="4">The following dataflows are inputs to the diagram but not the parent process:</td></tr><tr><td colspan="4">Command</td></tr><tr><td colspan="4">The following dataflows are outputs from the diagram but not the parent process:</td></tr><tr><td colspan="4">*** None ***</td></tr></table>

Fig. 4. Sample Unbalanced Report from Structured Architect.

Structured Architect provides the ability to analyze the set of dataflow diagrams in a number of different ways. For example, it is possible to test whether the children processes are in balance with their parent process. Other analysis capabilities include examination of data dictionary for missing descriptions for data structures and elements, primitive processes without structured English, etc. Even though the analysis feature of Structured Architect is not as extensive as that of Excelerator, it is adequate for routine use. Two examples of analysis results are shown in Figures 4 and 5. Figure 4 shows a sample unbalanced report and Figure 5 shows a sample listing of data elements with some missing description.

Design/1 does not have a built-in mechanism to check for balancing. This system failed to detect unbalanced diagrams when such errors were deliberately introduced in order to study the system's behavior.

## 3.5. Form Generation Facilities and Templates

Most system analysis projects involve extensive documentation of processes and definitions of data items. Management of documentation is therefore an important criteria in the selection of CASE products. The best example of document management was seen for Design/1. In this system, document templates can be created in a customized

Structured Architect homecomp 04-12-1988 01:32:03
Elements without codes, values/ranges, or data class
CalculatedCostPerAgent missing code
CalculatedEquipmentSupplCost missing code
CalculatedStateLaborCost missing code
CalculatedSupportAdministrativ missing code
CalculatedTotalCost missing code
Command missing code
ConfirmationText missing code, value/range
EmployeeName missing code, value/range
EquipmentSupplyType missing code, value/range
ExpenseCost missing code
NumberOfAgents missing code
NumberOfAgentsAdded missing code
NumberOfAgentsDeleted missing code
Productname missing value/range
ProductType missing value/range
ProjectCode missing code, value/range
QuarterConstant missing code, value/range
QuarterValue missing code, value/range
StateConstant missing code, value/range
StateDisplayname missing code, value/range
StateSpecificColumnHeading missing code, value/range
TotalAgents missing code, data class
TotalConstant missing code, value/range
TotalCost missing code
TotalCostPerAgent missing code, data class
TotalDirectLaborCost missing code, value/range
TotalSupportAdministrativeCost missing code, data class
UnitCost missing code

Total data elements missing code, value/range or data class: 28

Fig. 5. Data Elements with Missing Descriptions from Structured Architect.

manner which then can be used repetitively to create instances of dictionary entries.

The Report Design option of Excelerator allows creation of forms. Sample reports, complete with titles, headers, labels, and icons can be generated using a graphics-mode form-generation facility. System generated reports, such as those discussed in balancing can also be customized through the Report Writer Format option.

Report Design Aid (REA) is a facility of Design/1 which assists in the creation and maintenance of report layouts. The reporting facilities allow creation and printing of reports in four ways:

1. Index reporting facility, which produces 'Contains', 'Where-used' and 'Implied Documents' Reports.

2. Inventory Reporting facility, that allows the user to create a report listing existing documents for a particular 'Form ID'.

3. Element Glossary facility, which produces a report of all elements.

4. Cross Check Reporting facility, which compares documents according to their cross-references, and locates similar documents that might be combined.

A number of system generated reports are possible through the analysis option of the Structured Architect. Facilities for customizing such reports are not available.

The ability to create and maintain Electronic Design Documentation is the foundation on which all other Design/1 functions are based. All Electronic Design Documentation is stored in a Design Data Base. Control over the contents of this database is possible through creation and maintenance of documents. The format of the database is controlled by creating and maintaining forms. The database also contains system generated indexes and cross-references that are automatically maintained. In our opinion, Design/1 has the best reporting features among the systems examined.

## 3.6. External Interfaces

Excelerator has an XLD interface that supports controlled data sharing in a multi-user environment. External interfacing outside Excelerator is possible only through the creation of standard DOS files.

Structured Architect provides an "Integrator" option for the multi-user environment. The System Architect-Integrator allows many analysts to work on different structured Architect encyclopedias while ensuring the consistency of the central project database. Structured Architect makes it possible to export the information in the Encyclopedia to a standard DOS file where it can, in turn, be used as input to other software. Structured Architect can also be interfaced with the PSL/PSA product on a main-frame.

Design/1 provides a variety of interfaces. The Programmer's Workbench interface, uploads screen characteristic to a mainframe computer for use with the modular Programmer's Workbench. The IBM Data Dictionary Interface supports uploading and downloading of element and segment definitions to the IBM DB/DC Data Dictionary on the mainframe. The ASCII File Input Facility allows transfer of files into Design/1 from other microcomputer software and from mainframe files. The Print to Disk facility allows documents or forms to be transferred to other microcomputer software or to a mainframe. The Cullinet Data Dictionary Interface supports uploading of data elements, record layouts, screen layouts, and screen and report definitions to the Cullinet IDD (Integrated Data Dictionary) on the mainframe. The range of available interfaces for Design/1 is the most extensive of the three systems examined by us.

We have not tested any of the available external interfaces.

## 3.7. Project Security

The BLOCK security device that plugs directly into the parallel port of a computer, PAL chips, and Key-diskette are some of the project security measures provided with Excelerator. The XL Data dictionary actions are governed by the access privilege assigned to each Excelerator user. To a lesser extent, they are also governed by the lock status of particular entities, as locked entities are protected from modification by other users.

Structured Architect also provides BLOCK security, as in the case of Excelerator. However, we used an educational version of Structured Architect for our project and no security measures exist for this.

Design/1 security is available only through a networking environment.

## 3.8. Networking

We did not test the systems in any networking environment. However, according to the manufacturers of Excelerator, this product has been tested on the following LAN hardware/software combinations:

1. IBM PC LAN program ver. 1.10 with the IBM PC Network Adapter.

2. 3COM Etherseries ver. 2.4 software with a 3COM Etherlink board.

3. Banyan Vines ver. 1.31 with a 3COM Ether-Link board.

Design/1 claims support of 3COM EtherSeries and Novell Netware and Advanced Netware.

## 3.9. Documentation

Excelerator comes with fairly organized documentation. The absence of a centralized index in the User Guide is a glaring omission.

The Structured Architect documentation is extensive but the first time user has a problem finding the right information in the documentation. The index is, however, inadequate.

The Design/I software documentation contains all the needed information, but is rather poorly presented.

## 4. Conclusions 2nd Future Directions

We have examined three leading CASE tools in detail. Each of the tools was used for a small system analysis project using students who did not have any prior experience with such products. Our experience indicates that it is not too difficult to use them particularly if tutorials are first followed and understood.

The tools examined in this study come with varying capabilities. For example, if document design is a major consideration, Design/1 would be considered clearly superior among the three tools examined. However, on the whole, Excelerator provides the most integrated environment.

Structured Architect, on the other hand, is a reasonably decent tools but with limited diagram editing facilities. None of the tools support options such as windowing and cut/paste operations for pictures which can make diagram development and editing much easier. The word processing facilities for specification development are also limited.

The limitations of current batch of CASE tools are to be expected since these are first generation products in a PC environment. With maturity, these products are likely to improve providing an analyst with a powerful medium for software development.

System analysis and design is a creative process and is highly influenced by the abilities of the individuals engaged in the process. For an assessment of CASE tool influenced productivity, one must account for variations in these individual abilities as also the cost of an adequate full range test. An idea of testing cost can be judged from the experience of a team of analysts who had to spend about two (2) man-years effort in a period of eight (8) weeks to measure and evaluate six (6) such tools [10]. These perhaps explain why productivity improvements with CASE tools have not been well documented. However, from our experience, we are convinced that productivity improvements are possible. For example, while working with Structured Architect in a related project, one of the individuals made a wrong definition of the explosion process. This necessitated creation of a very detailed diagram for a second time. A rough examination of the time used for creating the first diagram and then the second shows that the creation time would have decreased from 14 hours to about 4.5 hours. This individual used Structured Architect for the first time, as in the case of the participants of the AAR project. This time saving, therefore, is not only due to a learning effect, but also due to the speed with which reasonably complex diagrams can be constructed.

The CASE tools would not provide a good technological environment unless they assisted in quality assurances of the system specifications. Features like automatic cataloging and balancing satisfy these requirements and automatically ensure completeness of the specification. The semantic quality of the specifications is, however, not enforced by any CASE tool and may have to wait developments in Artificial Intelligence technology.

We believe that CASE tools will gain in popularity as they mature. It is therefore required that we prepare for this technology. Future research can examine several features not yet available. For example, automatic code generation from pseudocode descriptions of processes are not yet available for PC based CASE tools even though such capability exist for a few of the main frame based tools such as TAGS. Other areas needing research and development include the capability of CASE tools to provide integrated life cycle support and integration with knowledge-bases for design quality enhancement.

## References

[1] Chen, P.P., The Entity-Relationship Model - Toward a Unifying View of Data. ACM Transactions on Database Systems, Vol. 1, No. 1, March 1976.

[2] DeMarco, T., Structured Analysis and System Specification. Prentice-Hall, 1979.

[3] Excelerator Reference Guide, Tutorial, User Guide. Index Technology Corporation, Cambridge, MA 02142.

[4] Gane, C. & Sarson, T., Structured Systems Analysis: Tools and Techniques. McDonnel Douglas Professional Service Company, St. Louis, Missouri 63166.

[5] Jackson, M.A., System Development. Prentice-Hall, 1983.

[6] Leavitt, D., Scratching the surface of CASE potential. Software News, Vol 7, No. 2, Feb 87 (50–52).

[7] Knight, R., CASE paybacks perceived if not exactly measured. Software News, Vol 7, No. 2, Feb 87 (56–64).

[8] Method/1 Design/1. Arthur Anderson & Co., 33 West Monroe Rd., Chicago, IL 60602.

[9] Misra, S. & Kovijanic, A.. Computer aided productivity tools in teaching system analysis and design. The Journal of Computer Information Systems, Summer, 1988 (12–15).

[10] Sibley, E.H., Private Communication with reference to unpublished work done by him.

[11] Sievert, G.E. & Terrence, A.M., Specification-Based Software Engineering with TAGS. Computer, April 1985, pgs. 56–65.

[12] Structured Architect Users Guide. Meta Systems Ltd., 315 E. Eisenhower Pkway., Ann Arbor, MI 48104.

[13] Yourdon, E. & Constantine, L., Structured Design: Fundamentals of a Discipline of Computer Program and System Design. Prentice-Hall, Englewood Cliffs, New Jersey, 1979.

[14] Warnier, J.D., Logical Construction of Systems. Van Nostrand Reichold, 1981.
