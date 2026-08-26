---
otero_id: 27004
otero_key: "S396K8G2"
title: "Computer-Aided Analysis of Office Systems*"
authors: "Benn R. Konsynski; Lynne C. Bracker"
year: "1982"
journal: "MIS Quarterly"
doi: "10.2307/248751"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Computer-Aided Analysis of Office Systems
Author(s): Benn R. Konsynski and Lynne C. Bracker
Source: MIS Quarterly, Vol. 6, No. 1 (Mar., 1982), pp. 1-17
Published by: Management Information Systems Research Center, University of Minnesota
Stable URL: http://www.jstor.org/stable/248751

Accessed: 09/05/2014 16:08

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

Computer-Aided Analysis of Office Systems\*

By: Benn R. Konsynski
Lynne C. Bracker

## Abstract

Computer-aided support in the analysis and design of office information systems is discussed. The support system described includes a language for description of office practice, analysis and database maintenance systems, and analysis report generation software. The system components are consistent with a general model of office interactions. The objects and relations unique to the office environment are supported in the terminology for description of both manual and automated office activities. Analysis support providing consistency and completeness evaluations and alternative views of the system serve the analysis activity. A case study is briefly overviewed and conclusions are drawn concerning the utility of the tools. The major utility of the tools was perceived by management and analysts to be the application as a dynamic and structured documentation with consistency evaluation.

Keywords: Office systems, computer-aided analysis, requirements specifications

ACM Categories: 3.5

## Introduction

An office is a functioning organization with a wide variety of activities and interactions. The creation of an integrated and automated office information system requires that all facets of the office be understood and accounted for. Due to the large number of unstructured activities occurring in the typical office, it is virtually impossible to automate all parts of all the processes; the automated system must be designed in a manner that enhances the processes which are basically unstructured and those that are required to be manual by their nature. All degrees of manual and automated processes must be included in the analysis as part of the system design.

This article describes the Office Information Specifier, OFFIS, and the OFFIS Analyzer which have been designed and implemented at the University of Arizona based on a general office information system model $[10]$ . A language has been implemented and an analyzer developed to facilitate the construction and maintenance of a database containing the specification. The analyzer also generates the analysis reports on demand. Both the model and the specification language are currently being expanded and refined based on experience in several applications and case examinations, including the case discussed below.

## Design of Office Information Systems

The design of an automated office system has remained a manual task; a design team communicates with users and with each other in order to create and integrate the various system modules using pencil, paper, and perhaps a design approach such as top-down, HIPO, Structured Analysis, or one of other available techniques [15]. The problems inherent in these ad hoc approaches include human errors, communication errors, interface incompatibilities, redundancy, incomplete specification, and inconsistencies. Furthermore, errors in design frequently remain undetected until implementation or testing processes are undertaken, as design verification is seldom attempted before implementation occurs. Several automated design systems are available, including ADS, GENASYS, SREM, PSL/PSA, and PLEXSYS [14, 15].

One might ask how the design process in the office differs, if any, from the general information system design process? Also, how does the tool differ from other design tools, like PSL/PSA, available for general information systems design? The design of office information systems is of course a special case of the general design process. The attempt here is to exploit the unique aspects of the office (characteristic object and relation definitions, etc.) to accelerate the definition and analysis of office activities. It is not intended that these specifications would replace the generic design activities, like PSA processing functions. Indeed, the intent is to produce complementary and supplemental specifications and analysis procedures that would directly interface with the other design tools. In this case, a direct interface with PSL/PSA has been a design objective from the beginning of the effort.

In addition to the OFFIS project, several other projects are concerned with the development of tools in support of the design process in the office. Two projects are in early stages of development, one at the University of Toronto [11] and another at MIT [7]. A more advanced effort has been in progress at Xerox [5, 6] with computer-aided support being provided for management of the Information Control Net, ICN, specification by the Quinault system [16].

## The OFFIS system

The OFFIS system is designed to facilitate an interactive and iterative analysis and design process to provide the planner/designer of the automated office with a flexible method of documenting and analyzing system features and constraints. This design process is depicted in Figure 1.

The planner/designer/analyst is defined to be the group of individuals who determine requirements and constraints that are imposed on the proposed system. This group would typically consist of management, clerical staff, and other non-technical office personnel. Each analyst specifies a portion of the system design using the OFFIS language. Statements incorrectly specified are returned as error diagnostics. The OFFIS statements are maintained with their relationships in the OFFIS database. At any time the analyst may request analysis of the database and associated analysis reports. The OFFIS analyzer software also produces diagnostics in cases of improper specification.

The analyzer reports provide the analyst with snapshots of the proposed system design from various perspectives. The design is easily altered by changing, adding, or deleting selected OFFIS statements previously created. The new design is then analyzed. The design process using the OFFIS system is one of iteration until the desired system design has been achieved. It should be understood that there are certain random occurrences that cannot be modeled, nor can they be specified as part of the OFFIS design. Rather the system is used to describe regularly occurring events and interfaces.

The OFFIS System serves three basic functions — Documentation, Analysis, and Design. The degree to which the analyst group is able to take advantage of the facilities of the system is a function of the maturity of the system development process:

1. Documentation — At one level, OFFIS serves as a descriptive "model," documenting real or proposed office procedures and activities. Thus, the system provides a dynamic documentation of the activities and relations. As a management tool, OFFIS offers a representation for management to understand and communicate concerning the real organizational activities.

2. Analysis — The current primitive analysis facilities in OFFIS permit its use as an analysis tool in evaluation of the completeness and consistency of documented procedures. In this way, proposed changes may be evaluated and the impact of change can be assessed. Thus, OFFIS serves as a tool in evaluating “what if” questions related to assessment of the impact of alternative design decisions.

3. The long range objective parallels other research efforts that the authors are pursuing [8, 14, 15], facilitation of computer-aided support in the design and development of information systems. The description of a desired office information system becomes a "model" and requirements specification for automated or computer-aided design of the desired system. In this light, simulation and design tools are being interfaced [10] with the model database.

![](/api/attachments/S396K8G2/fulltext/images/13a6664372159515257b24c85a711076a57b11c9aef341d4d49ac7c0460bc44b.jpg)  
Figure 1. Overview of OFFIS System

## OFFIS Language

The OFFIS language was designed for use by office management and staff. The goal was to provide office personnel with a convenient method for stating information requirements as specifications in development of an automated office system. The language syntax is simple and the terminology used in composing the language statements are those familiar to office personnel. The OFFIS language provides for the specification of office reporting hierarchies, processes, flow of information, event scheduling, regularly-occurring interactions (e.g., meetings), and other forms of internal and external communications.

The OFFIS language is a non-procedural language used to define a system at various levels of requirements specification. OFFIS is compatible with other requirements specification languages, such as PSL. Direct interface with PSL/PSA is being pursued in order to extend the capabilities of the OFFIS system.

Each of the OFFIS language statements apply to one of several OFFIS object categories called sections. Each section begins with a section header, consisting of the keyword section-type and one or more user-supplied names for the section. All statements appearing after the section header provide description for the section. For example, a document may be defined to be a LETTER, FORM, or DATAFILE. Further, a customer LETTER is defined quite differently from an offer-for-employment LETTER. The OFFIS section types are listed in Table 1.

## Example language specification

Consider the following example. The office secretary schedules a meeting based on the president's and vice president's calendars. Notices are placed in the employees' mailboxes notifying them of the quarterly report meeting. A copy of the notification is filed. The secretary must also write and send meeting notices to the company accountants, who are external to the organization. They regularly attend the meetings. The quarterly report meeting is a regularly held event; it lasts about two hours each time it is held. The description of these relations is given below. The example illustrates the basic syntactic form of the statements and demonstrates the use of the language in depicting organizational reporting structure. The mail definitions are logical addresses for electronic mail communication.

JOB-TITLE president; OWNS p-mail;

JOB-TITLE v-president;
REPORTS-TO president;
OWNS vp-mail;

JOB-TITLE office-secretary;
REPORTS-TO president;
CREATES quarterly-meeting-notices;
SCHEDULES quarterly-meeting
USING p-calendar, vp-calendar;

MEETING quarterly-meeting;
HAPPENS 4 TIMES yearly;
ATTENDED BY president, v-president,
accountants;
DURATION 2 hours;

DATAFILE quarterly-meeting-file;
UPDATED BY office-secretary
USING quarterly-meeting-notice;

LETTER quarterly-meeting-notices;
HAPPENS 4 TIMES yearly;
SENT TO accountants;
ROUTED TO p-mail, vp-mail, employee-mail;

EXTERNAL-NAME accountants;

## The OFFIS Analyzer

The OFFIS analyzer processes the user-supplied OFFIS requirements definitions, analyzes the syntax and portions of the semantic relations, and iteratively builds the OFFIS database. The OFFIS Analyzer uses this database for generation of the OFFIS reports and creation of extraction files for the design models.

Table 1. OFFIS Objects and Relations

<table><tr><td colspan="2">OBJECTS</td><td colspan="2">ATTRIBUTES</td></tr><tr><td>JOB-TITLE</td><td>A</td><td>1</td><td>TITLES-HELD</td></tr><tr><td>GROUP</td><td>B</td><td>2</td><td>WEIGHT</td></tr><tr><td>DATAFILE</td><td>C</td><td>3</td><td>LOCATION</td></tr><tr><td>LETTER</td><td>D</td><td>4</td><td>SECURITY</td></tr><tr><td>FORM</td><td>E</td><td></td><td></td></tr><tr><td>CALENDAR</td><td>F</td><td></td><td></td></tr><tr><td>MAILBOX</td><td>G</td><td></td><td></td></tr><tr><td>EXTERNAL-NAME</td><td>H</td><td></td><td></td></tr><tr><td>MEETING</td><td>I</td><td></td><td></td></tr><tr><td>TIME-UNIT</td><td>J</td><td></td><td></td></tr><tr><td colspan="4">RELATIONS</td></tr><tr><td>ACCESSES</td><td>1</td><td>REPORTS TO</td><td>22</td></tr><tr><td>ACCESSED BY</td><td>2</td><td>REPORTED TO BY</td><td>23</td></tr><tr><td>ATTENDS</td><td>3</td><td>RECEIVE-EXTERNAL</td><td>24</td></tr><tr><td>ATTENDED BY</td><td>4</td><td>SENDS</td><td>25</td></tr><tr><td>CANCELLS</td><td>5</td><td>RECEIVED FROM</td><td>26</td></tr><tr><td>CANCELLED BY</td><td>6</td><td>SENT TO</td><td>27</td></tr><tr><td>CHANGES</td><td>7</td><td>RECEIVE-INTERNAL</td><td>28</td></tr><tr><td>CHANGED BY</td><td>8</td><td>ROUTES</td><td>29</td></tr><tr><td>USED TO CHANGE</td><td>9</td><td>ROUTED TO</td><td>30</td></tr><tr><td>CHANGED USING</td><td>10</td><td>ROUTED BY</td><td>31</td></tr><tr><td>CONSISTS</td><td>11</td><td>SCHEDULES</td><td>32</td></tr><tr><td>CREATES</td><td>12</td><td>SCHEDULED BY</td><td>33</td></tr><tr><td>CREATED BY</td><td>13</td><td>USED TO SCHEDULE</td><td>34</td></tr><tr><td>DELETES</td><td>14</td><td>SCHEDULED USING</td><td>35</td></tr><tr><td>DELETED BY</td><td>15</td><td>UPDATES</td><td>36</td></tr><tr><td>DURATION</td><td>16</td><td>UPDATED BY</td><td>37</td></tr><tr><td>HAPPENS</td><td>17</td><td>UPDATED USING</td><td>38</td></tr><tr><td>MEMBERS</td><td>18</td><td>USED TO UPDATE</td><td>39</td></tr><tr><td>OWNS</td><td>19</td><td>RESPONSE-EXPECTED</td><td>40</td></tr><tr><td>OWNED BY</td><td>20</td><td>IF</td><td>41</td></tr><tr><td>REFERS</td><td>21</td><td></td><td></td></tr></table>

The analyzer has a menu-driven command structure. There are three branch menus from the base menu: 1) Control and Analyst Assistance, 2) Model Building and Maintenance, and 3) Reports Subsystem. The first selection is used to define interaction parameters for the session such as output file specification, report document appending, etc. The model selection offers commands for building (input of OFFIS specifications) and maintaining databases. The third selection offers the generation of the basic analyzer reports.

Several software tools are used in construction and modification of the OFFIS language and analyzer. Use of these tools provides the desired specification language flexibility and compatibility necessary for interface with other information system requirements specification languages. Language and report modifications can be made with little difficulty. As a result, language specialization to special office environments can be accommodated. Thus, we are able to customize the language and interface new analysis and design procedures as they are determined useful.

## OFFIS Analyzer Reports

In order to effectively use an automated design tool, analysis and evaluation reports on the resulting design are a necessary feature. The OFFIS Analyzer produces reports which provide management with an overview of the system design describing the organization's functions, interfaces, and data flow. The reports show incompleteness and inconsistencies in the design as well as the classification of processes associated with each person. Various designs may be specified and evaluated using the reports, thus making the design process iterative while moving toward a satisfactory design.

Several of the major OFFIS Analyzer reports are described below. Table 2 offers a summary of the reports and describes the utility of the reports in each of the various models of usage — Documentation, Analysis, and Design. An example of each report is illustrated in the context of the case study discussed below, an aircraft sales and leaseback company.

Table 2. Report Summary

<table><tr><td>Current Reports</td><td>Description</td><td>Analysis &amp; Documentation</td><td>Design Utility</td></tr><tr><td>Completeness</td><td>Assess completeness of description</td><td>Assurance of a purposive definition</td><td>Determines the resolution of flow relations</td></tr><tr><td>Item Tracking</td><td>Trails information flow through system</td><td>Assurance of the conformance with actual flows</td><td>Assists in process organization</td></tr><tr><td>Meetings</td><td>Meeting and role assignments</td><td>Presents role responsibilities</td><td></td></tr><tr><td>Organizational hierarchy</td><td>Displays reporting hierarchy</td><td>With Item Tracking assists in separation exposure</td><td>Control definition and evaluation</td></tr><tr><td>Systems Interaction</td><td>Weighted evaluation of task distribution</td><td>Evaluate proper job and temporal distribution</td><td>Quantitative evaluation of functional task distribution</td></tr></table>

## The Completeness Report

The completeness report (Figure 2) is used to determine whether all data items (letters, forms, calendars, datafiles, mailboxes) have definitions specifying creation. The report also identifies all data items which are created but never used. For every data item created, there should be at least one entity that accesses it. Duplication of effort or possible control conflicts can be detected as the report shows that a data item is created by more than one job-title. This situation may be acceptable in some cases; however, the designer is alerted when the situation arises so that unnecessary duplication can be avoided. Data items which are created but never used and vice-versa result in \*\*\*\*\* being printed. There may be data items which have neither creator nor user. In this case two sets of \*\*\*\*\* are printed. These symbols identify errors of incomplete design specification and should be corrected by the analyst.

## Data Item Tracking Report

The Data Item Tracking Report (Figure 3) provides a detailed description of a data item traveling through the office system. All sections are scanned and all references to a particular data item are listed. Inconsistencies are noted with appropriate diagnostics. For example, LETTER A may be routed from MANAGER A to MANAGER B; however, MANAGER B has not been defined. A diagnostic message would result. All data items must be created by a CREATED BY clause. The report can be used to obtain information about all data items or about all data items requested. This report is helpful in tracking data items which are passed from one person to another in an organization.

## Meetings Report

As meetings play an important role in scheduling office activities, a Meetings Report (Figure 4) outlining meetings and their attendees is generated. The report identifies responsibilities of attendance and is used in the analysis of stated responsibilities. Management has found this frame of reporting of considerable use in specification and evaluation of job definitions and responsibilities.

## COMPLETENESS REPORT

DATA ITEM: ACCOUNTS-PAYABLE
CREATED BY: BOOKKEEPER
ACCESSED BY: OFFICE-MANAGERS

DATA ITEM. PILOT-FLIGHT-REPORTS
CREATED BY: PILOT
ACCESSED BY: PILOT
DISPATCHER

DATA ITEM: INVOICE-LOG

CREATED BY: EXECUTIVE-SECRETARY

ACCESSED BY: PRESIDENT

GENL-OFFICE-MGR

EXECUTIVE-SECRETARY

BOOKKEEPER

Figure 2. Sample Completeness Report

DATA ITEM: DISPATCHERS-MAILBOX
CREATED BY: EXECUTIVE-SECRETARY
UPDATED BY: DISPATCHER
ACCESSED BY: OWNER-ONLY
DELETED BY: DISPATCHER
USED TO SCHEDULE OR UPDATE: ----
OWNED BY: DISPATCHER
ROUTED BY: ----
SENT TO: ----
RECEIVED BY: ----

Figure 3. Data Item Tracking Report

## MEETINGS REPORT

MEETING NAME

OFFICE-MANAGERS-MEETING

WEEKLY-OFFICE-STAFF-MEETING

ATTENDEES

OFFICE-MANAGERS

GENL-OFFICE-MGR

EXECUTIVE-SECRETARY

BOOKKEEPER

DISPATCHER

Figure 4. Sample Meetings Report

## Organizational Hierarchy Report

A sample Organizational Hierarchy Report is shown in Figure 5. Using the REPORTS TO and the REPORTED-TO BY clauses the reporting scheme is shown in a chart form. If a job-title is found for which no supervision has been defined, a reporting box containing \*\*\*\*\* is constructed to show a possible omission. Errors found as a result of the hierarchy consistency and completeness checks are also shown with \*\*\*\*\* displayed in the appropriate chart box; each is accompanied by an error message. Consistency and completeness checks performed include simple control evaluation rules, such as:

1. A person cannot report to someone who eventually reports back to himself.

2. One job-title or group name cannot report to more than one job-title or group. In other words, a person may not have multiple direct managers.

3. Those lower in the reporting hierarchy must also have lower security levels. Security level is assumed to vary directly with a person's position in the company. Those at the same levels, however, may have different security levels.

![](/api/attachments/S396K8G2/fulltext/images/dcfe4ed3837d63994311b26ed6b8200feaab6c07d6248799616723152ffbd353.jpg)  
Figure 5. Organizational Hierarchy Matrix

A language for specification of consistency rules is used to modify and extend the rule set. In this way, certain policy rules, unique to the organization, can be enforced.

## Systems Interaction Report

The Systems Interaction report (Figure 6) presents each job-title and group occurrence along with the total number of individual system interactions or tasks that the person must perform. The tasks are defined to be the verbs to create, update, schedule, access, receive, route, and send data items. This report is helpful in determining whether there are company positions with an inordinately heavy or light workload or significant system interaction. When the organization has one or more positions whose duties are temporally imbalanced, serious bottlenecks can occur. It is recognized that the number of tasks assigned may not necessarily correlate directly with the difficulty of the job, as some tasks are more time-consuming than others. The numbers can, however, be an indication that job responsibilities should be examined in more detail. The Systems Interaction report allows management to evaluate positions and responsibilities. A weighting scheme is being devised to “score” workloads on defined positions and evaluate temporal distributions.

The capability has been added through a RELATIVE-IMPORTANCE statement to assign a weighting scheme to each data item. The WEIGHT field in the report reflects the total number of occurrences of each data item and its assigned value of importance. The resulting weight can be used as an indication that items with extraordinarily high values should be examined in more detail.

The authors are pursuing the extension of activity analysis to the evaluation of internal control. The scoring and weighting schemes are being adjusted to facilitate the quantification of the evaluation of internal control exposure potential. One can also see that the Organizational Hierarchy report offers insight into authorization evaluation and assessment of collusion potential.

## A Case Study

The OFFIS system was used in the design of an office information system for an aircraft sales and lease-back company. The major functions of the organization are sales and service of aircraft, flight instruction, rental of aircraft for charter flights, and management of aircraft for the owners. The company consists of the president, sixteen office personnel, and pilots, and maintenance personnel. There are over 500 regular flying customers and fifty-six aircraft that generate revenue for the plane owners and the company. The total number of revenue transactions per month is approximately 2500. The major justifications for automating the office processes were to speed the billing and improve the management reporting functions for improved decision making and to reduce human errors in the well-structured aspects of the system.

Figure 6. Systems Interaction Report

<table><tr><td colspan="3">SYSTEMS INTERACTION REPORT</td></tr><tr><td>JOB TITLE</td><td># INTERACTIONS</td><td>WEIGHTED AVERAGE</td></tr><tr><td>BOOKKEEPER</td><td>16</td><td>3.60</td></tr><tr><td>DISPATCHER</td><td>3</td><td>3.50</td></tr><tr><td>EXECUTIVE-SECRETARY</td><td>40</td><td>3.17</td></tr><tr><td>GENL-OFFICE-MGR</td><td>18</td><td>3.11</td></tr><tr><td>OFFICE-MANAGERS</td><td>15</td><td>3.26</td></tr><tr><td>PILOT</td><td>1</td><td>3.50</td></tr><tr><td>PRESIDENT</td><td>17</td><td>3.27</td></tr><tr><td>RECEPTIONIST</td><td>1</td><td>2.00</td></tr></table>

Each office worker was asked to specify tasks and interfaces with others, both internal and external to the organization. Due to management concern for minimization of the impact of change, the initial design requirements were specified in a manner which closely resembled the existing manual system. This approach facilitated a documentation and thorough analysis of existing procedures. The initial specification contained inconsistencies and redundancies and was incomplete in many aspects. The final, acceptable design was quite different from the original design in documents, volumes, and information flows, and differed from the manual operations in these aspects.

Following use of the OFFIS language and analyzer, several observations were made by the analysts and the managers:

1. It was clear that no one, including the office manager, knew the entire organization's data flow. As expected, most individuals understood their individual tasks very well but did not understand how information used or generated by these tasks was later utilized by others. Many tasks were performed with little or no understanding of the reasons for their performance. The use of the OFFIS reports as a communication mechanism was perceived as a secondary benefit by management.

2. Many inconsistencies were detected. For example, at various times, three different persons computed the pilots' pay. Each of these individuals specified a different pilot-pay algorithm.

3. Several reports were generated and were never accessed; there were also reports required with no single entity responsible for their generation or distribution.

4. A major discovery for management was the poor temporal distribution of scheduled activities. For example, there was an abundance of time-consuming tasks that the executive secretary had to perform at the end of each month. These included the customer and aircraft owner billing as well as production of management reports for aircraft and pilot utilization.

5. Management found that it was not as difficult as expected to specify the information requirements, in an abstract form, for the less-structured decision making processes.

While none of these observations is a surprise to the experienced analyst, each of these surfaced as important benefits that management realized from the effort.

Following several design iterations using the OFFIS language and analyzer, the system was organized and the inconsistencies were resolved; redundant and unused information was eliminated; many of the purely clerical duties were eliminated, to be handled by programs; the end-of-month billing tasks were distributed over both time and personnel in order to alleviate the previous billing work backlog. In the final design, the job of office manager was dissolved and those duties were incorporated in the dispatcher's tasks. The resultant system was implemented using the OFFIS design specifications and is presently operational.

OFFIS was being tested for feasibility in the design of office systems supporting both well-structured processing and the relatively unstructured decision making processing. No time comparisons were made for design using OFFIS versus design utilizing one of the well-known manual approaches. Comparison studies are the topic of a current research effort. We found that the language could facilitate description of each transaction, interaction, and process that occurred in the test organization. The study group was somewhat surprised to find the language to be easier to use than expected. Many of the personnel were untrained in the area of data processing.

Space prohibits presentation of the entire design specification in the OFFIS language. For purposes of illustration of the language constructs, a representative portion of the case study is presented in Appendix A. Sample reports generated on the test case at various stages in the iterative design process are presented in Figures 2 through Figure 6.

## Observations

Use of the OFFIS system in the design of an office information system for the above organization provided many recommendations concerning the structure and features of the OFFIS system. This feedback is being used to refine and extend the language and analyzer. First, office personnel were enthusiastic in their participation in the design of a computer based office system. They felt they were contributing information that would ultimately be used to facilitate their own particular tasks. The language proved to be easier to learn and use than initially expected; however, additional time was required to teach office personnel to communicate their requirements using the OFFIS language constructs. The reports provided a method for interpretation of information flow and office interactions. Use of the reports facilitated evaluation of various alternatives in design and stimulated discussion on alternative designs.

The office information system in the aircraft organization was implemented over the period of one year. During this time, several changes in personnel and policy took place. A sensitivity analysis was accomplished by periodic presentation of the reports to office personnel to determine whether the system design features remained current. Changes were incorporated into the design and related programs. The resulting system evolved over time, and the implementation reflected a dynamic design rather than the full implementation of the initial design revisions specified during the previous year. The use of the OFFIS system and the approach taken facilitated the dynamic growth of the office system, and at the same time served to document that evolution.

One limitation detected in the OFFIS system was the manner in which conditionals were handled. Presently, conditional operations are specified as comment entries and are not reflected in the

OFFIS reports beyond the display of those entries. This is now perceived as a weakness in the language, and is presently being addressed. Other extensions under consideration include specification at the item level for all data sections and the production of a CODASYL-type database schema.

Several observations regarding the use of the OFFIS system might be noted at this point.

1. Cooperation and optimism of personnel in using a design tool was based on interest in the process and a feeling of job enhancement. The authors recognize that this will not always be the case.

2. The added time requirement to teach personnel the design language constructs must be acceptable to the organization. This generally took several hours over several days.

3. The managers and office workers enjoyed the ability to evaluate the current and future designs using the analyzer reports. This recognition of the system as a dynamic documentation was the major reason for acceptance.

4. Sensitivity analysis to provide automated analysis of the impact of incorporating changes following the original design specification was considered by management to be a major advantage.

5. The need for incorporation of conditional events and operations into reports is being pursued in current revisions, as it is essential to the overall evaluation of workloads and information flows.

6. The need for data description at the item level became evident with use of the system. In the authors' initial efforts, they attempted to avoid the explosion factors involving use of detailed item-level specifications. The analysis at the item level proved unavoidable.

7. Possibility for automatic generation of database schema is being pursued in the current effort, as is the interface with a data dictionary system.

One might ask the question, “Does OFFIS offer answers that differ from those we would acquire from the manual approaches?” It is not clear that OFFIS does offer different, or better answers. It was, however, felt that more alternatives were considered and that the continuing nature of the system use as a dynamic documentation illustrated the major advantages of the tool. The tool offers a means of dealing with the volume and complexity associated with the analysis of office information systems.

## Conclusions

A review of recent literature will show that office automation has as many definitions as the number of cases to which it is applied. The premise upon which OFFIS was developed is that the businessman should have a method for formal specification of the office operations in order to more intelligently design, select, and implement the automated system that most closely meets the organization's needs. The successful application of the prototype language and analyzer in the authors' case study has offered encouraging results in the ability to meet these goals.

OFFIS is currently being tested for feasibility in the design of office systems supporting both well-structured processing and the relatively unstructured decision making processing. Time comparison studies are the topic of a current research effort using OFFIS versus design utilizing well-known manual approaches. The authors have found that the language can facilitate description of transactions, interactions, and processes occurring in an organization. Furthermore, the authors have found the language to be easy to use by persons untrained in the area of data processing.

The development of the OFFIS system to support the office automation process has led to additional research efforts. A related effort is being pursued in evaluation of the use of similar software in the computer-aided evaluation of internal control. Further, a behavioral research project is pursuing the evaluation of the use of tools like OFFIS in facilitating communication among and between the analysts and the users. Finally, another effort is pursuing the use of graphics in specification, and its use as the direct interface with the OFFIS system.

In order to facilitate friendly interface with the analyst, the authors have developed a color graphics interface for entry and display of objects and relations. A library of icons is available to the analyst. The system allows the analyst to make graphic specifications, which are translated into internal relations in the database. The analyst's functions utilize this database in generation of reports. The control screen with menu options and a sample diagram are presented in Figure 7.

In addition to extension of analysis functions in the OFFIS analyzer, the authors are constructing interfaces with simulation analysis functions. One level of simulation evaluates office activities according to a model of job role/station activities (e.g., manager type A with an executive workstation or clerk type D with a communicating word processing workstation). In addition to the information on role and station, information on expected activity session times, projections of activity information demands, and inter-activity transition probabilities is provided. The simulation will generate traffic demands for another simulation in evaluation of local area network performance. The local area network simulation examines polling ring access architectures. The model is being extended to accommodate representation of CSMA/CD access in addition to the present capabilities.

![](/api/attachments/S396K8G2/fulltext/images/4a0850ae810f2eae6271ce0f6050486ac20666033e4cb58683b3278a40c1f598.jpg)  
DESIGN WORK AREA

![](/api/attachments/S396K8G2/fulltext/images/02e976fcfd80d993b7b54e19ab57b2720c1763305a669f908af922a80591e46d.jpg)  
Figure 7. Sample Graphics

## Appendix

JOB-TITLE president;
SYNONYMS ARE pres;
DESCRIPTION;
Responsible for setting company policy. Does hiring and firing.
OWNS presidents-mailbox, flightronics-mailbox;
REPORTED-TO BY general-office-manager;
SENDS promo-letters TO prospective-customers;
Accesses fuel-credit-log, flight-store-log,
Aircraft-log, invoice-log, charter-log,
customer-monthly-bill;
SECURITY IS level 15;

CALENDAR weeks-events-calendar;
HAPPENS weekly;
ROUTED TO presidents-mailbox;
genl-office-mgrs-mailbox, dispatchers-mailbox,
executive-secretary-mailbox, bookkeepers-mailbox;
CREATED BY office-managers;
UPDATED BY office-managers;
DELETED BY executive-secretary FOR office-managers;

MAILBOX genl-office-mgrs-mailbox;
OWNED BY genl-office-mgr;
RECEIVE-INTERNAL payroll, general-ledger,
telephone-messages;
CREATED BY executive-secretary
ACCESSED BY owner-only;

MAILBOX flightronics-mailbox;
ACCESSED BY executive-secretary, president
genl-office-mgr;
CREATED BY executive-secretary;
DELETED BY president;
RECEIVE-EXTERNAL company-bills, advertisements,
customer-communications

FORM customer-monthly-bill;
HAPPENS 300 TIMES monthly;
CREATED BY executive-secretary;
DELETED BY executive-secretary;
UPDATED BY executive-secretary; USING payment-log, invoice-log;
ACCESSED BY executive-secretary, president,
genl-office-mgr;
LAYOUT;
date    8 integer
customer #    4 integer
customer name & address    40 character
item description    20 character
debit amount    XXXX.XX
credit amount    XXXX.XX
new balance    XXXX.XX

Debit and Credit fields may be repeated up to 20 times;

LETTER promo-letters;
HAPPENS 1 TIMES monthly;
CREATED BY president;
SENT TO prospective-customers, customers;

MEETING weekly-office-staff-meeting;
HAPPENS 1 TIMES weekly;
SCHEDULED BY genl-office-mgr;
CANCELLED BY genl-office-mgr, president;
ATTENDED BY genl-office-mgr, executive-secretary,
bookkeeper, dispatcher;

## Bibliography

[1] Bracker, L. and Konsynski, B.R. "A Model of the Automated Office," MIS Technical Report, Department of Management Information Systems, University of Arizona, Tucson, Arizona, 1979.

[2] Bracker, L.C. and Konsynski, B.R. "The OFFIS System — A Tool in Automated Office Design," Proceedings of 1981 Office Automation Conference Digest, AFIPS Press, Houston, Texas, pp. 417-419.

[3] Cook, C. "Streamlining Office Procedures — An Analysis Using the Information Control Net Model," Proceedings of the National Computer Conference 1980, AFIPS Press, Anaheim, California, pp. 555-565.

[4] Couger, D. "Evolution of Business System Analysis Techniques," Computing Surveys, September 1973, reprinted in Couger and Knapp, System Analysis Techniques, Wiley, 1974.

[5] Ellis, C. “Information Control Nets: A Mathematical Model of Office Information Flow,” ACM Conference on Simulation, Modeling and Measurement of Computer Systems, August 1979.

[6] Ellis, C. and Nutt, G. "Office Information Systems and Computer Science," Computing Surveys, Volume 12, Number 1, March 1980, pp. 27-60.

[7] Hammer, M. and Kunin, J. "Design Principles of an Office Specification Language," Proceedings of the National Computer Conference, Anaheim, California, 1980, pp. 541-547.

[8] Konsynski, B.R. "A Model of Computer-Aided Definition and Analysis of Information System Requirements," Ph.D. Dissertation, Purdue University, West Lafayette, Indiana, 1976.

[9] Konsynski, B.R. and Bracker, L.C. "Office Automation — A Model for Design," Proceedings, Computer Networking Symposium, National Bureau of Standards, Gaithersburg, Maryland, December 1980.

[10] Konsynski, B. "Data Base Driven System Design," in Systems Analysis and Design: A Foundation for the 80s, W. Cotterman, ed., North Holland, New York, New York, 1981.

[11] Ladd, I. and Tsichritzis, D. "An Office Form Flow Model," Proceedings of the National Computer Conference, Anaheim, California, 1980, pp. 533-539.

[12] Naffah, N. Integrated Office Systems — Burotics, IFIP TC-6 Workshop Proceedings, North Holland, New York, New York, 1980.

[13] Ness, D. "Office Automation Project: Office Automation Today and Tomorrow," Working Paper 77-07-02, Department of Decision Sciences, Wharton School, University of Pennsylvania, Philadelphia, Pennsylvania, July 1977.

[14] Nunamaker, J. and Konsynski, B. "From Problem Statement to Automatic Code Generation," in Systemeering 75, M. Lundeberg and J. Bubenko, eds., Studentliteratur, Lund, Sweden, 1975.

[15] Nunamaker, J. and Konsynski, B. "Formal and Automated Techniques in Systems Analysis and Design," Systems Analysis and Design: A Foundation for the 80s, W.

Cotterman, ed., North Holland, New York, New York, 1981.

[16] Nutt, G. and Ricci, P. "Quinault: An Office Modeling System," IEEE Computer, May 1981, pp. 41-57.

[17] Swanson, E.B. "The Two Faces of Organizational Information," Information Systems Working Paper 2-78, Graduate School of Management, University of California, Los Angeles, California, 1978.

[18] Teichroew, D., Macasovic, P., Hershey, E.A., and Yamamoto, Y. "Application of the Entity-Relationship Approach to Information Processing Systems Modeling," Entity-Relationship Approach to Systems Analysis and Design, P. Chen, ed., North Holland Publishing Co., New York, New York, 1980, pp. 15-38.

[19] Zisman, M.D. "Representation, Specification, and Automation of Office Procedures," Working Paper 77-09-04, Department of Decision Sciences, Wharton School, University of Pennsylvania, Philadelphia, Pennsylvania, September, 1977.

## About the Authors

Benn R. Konsynski received a Ph.D. degree in Computer Science from Purdue University in West Lafayette, Indiana in 1976. He is currently an Assistant Professor in the Management Information Systems Department at the University of Arizona, in Tucson, Arizona. He has worked extensively on the development of computer aids in systems requirements specifications and analysis, and in automation of software design and cogeneration. He has published articles in Communications ACM, IEEE Transactions on Communications, and Database.

Lynn C. Bracker received a B.S. degree in Mathematics from Auburn University, in Auburn, Alabama, an M.S. degree in Computer Science from Purdue University, in West Lafayette, Indiana, and a Ph.D. degree in MIS from the University of Arizona, in Tucson, Arizona. Her work experience includes position in the U.S. Army, Redstone Arsenal, IBM Corporation, Bell Laboratories, and Hughes Aircraft. At present she is a member of the computing staff at Hughes Aircraft, in Tucson, Arizona.
