---
otero_id: 17891
otero_key: "GE4PPJMA"
title: "An information producing system that integrates stand-alone word-processing units and EDP resources"
authors: "Csaba J. Egyhazy; Nordyke & Associates"
year: "1980"
journal: "Information & Management"
doi: "10.1016/0378-7206(80)90028-2"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An Information Producing System that Integrates Stand-Alone Word-Processing Units and EDP Resources

Csaba J. Egyhazy

Organization of American States, 18th & F Streets, N.W., Washington, D.C.

and

Nordyke & Associates,

Suite 412, 8027 Leesburg Pike, Vienna, Virginia, USA

At the Organization of American States (OAS) the biennial budget formulation process represents a major undertaking, initiated by project proposals submitted by member countries and completed with the publication, in both English and Spanish, of the "Proposed Program-Budget of the Organization" for approval by the General Assembly.

This 3 volume document contains the description, goals and resource requirements of over 600 development projects and the entire administrative mechanism that support them. An innovative Information Producing System (IPS), that integrates standalone Word Processing (WP) units and existing EDP resources was conceived, designed and implemented to facilitate the processing, modification and analysis of budgetary data and the final publication of the formal document. This paper describes the IPS, with emphasis on its configuration, design and operational implementation.

Keywords: Information Producing System, Word Processing, Narrative and Numeric Data, Integration of WP and EDP Data Transmission, Design, Implementation

## 1. Introduction

Efforts to integrate stand-alone WP units and EDP resources are a recent phenomena, caused primarily by the increased number of user identified applications requiring the editing of formal text and the processing of corresponding numerical data. The latter, feeding EDP's master files, creates the data base to be accessed for analytical report generation purposes. This type of merger has occurred mostly in institutions that opted for distributed processing and standalone WP units. The already physically close equipment-user environment has proved conducive to a more responsive and custom tailored systems design and operation, and in turn, enhanced the possibilities of conceiving Information Producing Systems IPS) that integrate EDP and stand-alone WP units. Some of the reasons for considering such integrated IPS are to provide for:

– Narrative and numerical data editing and processing requirements;

![](/api/attachments/GE4PPJMA/fulltext/images/99a36e776b3b8f97883b5779a9bb4fedd5b12e1b178e295f5da1d6e3ff40db41.jpg)

Csaba J. Egyhazy is Director of Systems Planning and Design for Nordyke and Associates, Ltd., a newly formed management consulting firm. During 1979, Dr. Egyhazy was responsible for designing and implementing an Information Producing System for the formulation and analysis of the 1980–1981 Program Budget of the Organization of American States. Prior to this project, he was a member of the technical staff at the

Mitre Corporation in McLean, Virginia. Dr. Egyhazy studied Operations Research and Management Information Decision Systems at Case Western Reserve University. He is Hungarian by birth, was raised in Chile and is currently establishing himself in the United States.

\- Data entry through WP units, especially for remote sites with formal (upper and lower case characters) multi-language text management requirements;

\- Communications capability from WP of numerical data for the creation, at a low cost, of computerized data bases;

-- Common data bases and expanded reporting capability:

-- Electronic mail service.

This paper documents a case study that uses this novel approach for a budget formulation application at a large international organization: The Organization of American States (OAS).

## 2. Background--budget formulation at the OAS

The preparation of a biennial budget is a long and cumbersome task. It starts gaining momentum as governments, through their corresponding institutions, submit project proposals for funding considerations. The projects are of a varied nature, ranging from requests for technical assistance in planning, developing, or implementing large multi-national adult continuing education programs to small equipment acquisition requests for a rural technical school amounting to only a couple of thousand dollars.

The budget formulation methodology governing the entire process can be characterized by a programmatic one, where projects (the lowest level of budgetary detail) are defined in terms of goals and estimated resources required to meet them.

Projects proposals are formally received and evaluated at the corresponding OAS offices. Their programmatic value is assessed and their compatibility with the Organization's funding mission is determined. Those projects found acceptable for funding consideration are then transposed onto a specific form $^{1}$ which is used to edit, verify, analyze, modify and process budgetary data. Finally after considerable feedback loops, they are incorporated into a formal document, entitled the “Proposed Program Budget of the Organization”. This document consists of 3 volumes containing over 600 development projects and the entire administrative support mechanism.

## 3. Requirements analysis and design considerations

As an advocate of requirements analysis and the systems approach in conceiving Information Producing Systems, a number of interactive meetings were initiated with managers/analysts, and as a result a systems description of the entire budgetary cycle was prepared. This effort uncovered most of the informational needs of the budget formulation and the critical design considerations for the evolving IPS. Thus managers/analysts and technicians became aware of each others' conceptions and expectations of what lay ahead.

One of the most striking outcomes of this exercise was the realization that the data base to be generated was very heterogeneous, composed of a large number of projects, many with special formatting requirements and different narrative-to-numerical data volume ratios. In addition, the data base had to contain complete project formulation outputs in Spanish and provide access capability to computerized report generation. This necessitated the design of a WP centered data base with numerical data transmitted to EDP for the creation of a Budget Formulation Master File (BMF) for computerized report generation. Furthermore, as users evaluated the features of the IPS implemented for the previous budget formulation, antagonism to traditional eighty column data entry forms was revealed. Any attempt to use such a data entry mechanism seemed doomed to failure. In order to overcome this expressed bias and appease an initial negative reaction, it became apparent that the data collection form had to be designed so as to resemble the desired output as closely as possible but still serve as a data entry form easily understood by the WP operators. This posed a technical hurdle for EDP that was successfully overcome by developing a transmission software module.

The budgetary cycle description initiated an interest among managers in linking the budget formulation data base with the independent ongoing financial execution reporting system in order to improve the program-budget execution monitoring functions. A specific design consideration resulting from this expressed need was the expansion of record codes to include, in addition to the project identifier, both the numerical identifier of the goal and the expenditure requested. This would allow programmatic and bud-

![](/api/attachments/GE4PPJMA/fulltext/images/acc490eeff0eadb343410fdca1bade5485552b6332b1b07e4f2466c67b504995.jpg)  
Fig. 1. Integrated WP and EDP hardware configuration.

getary changes in the future single budget formulation – execution data base and subsequently be reflected in the formal project progress report. Among the operational requirements, managers and analysts stressed the need for fast turn-around for WP generated copies of formulated projects and EDP's error and analysis reports. The urgency was due to pressure exerted by program managers, the primary recipients of the services of the IPS. Thus emphasis was placed on developing a number of procedures, rules, and measures to ensure an efficient interaction between the components of the IPS, namely people, hardware and software.

After analysing the in-house feasible hardware configurations and corresponding design options, it was concluded that by integrating stand-alone WP units and EDP's hardware and software resources, these requirements could be met. The decision to select the hardware/software configuration of the IPS described by fig. 1, was based on cost-effectiveness considerations.

## 4. Hardware configurations

Influenced by the fact that:

1. top management at the OAS was, during the project planning phase, involved in an all out effort to utilized the capabilities of word processing, and

2. the nature of the budget formulation data,

the selected hardware configuration included two local WP (MICOM) units for data entry and storage for both the narrative and numerical parts of formulated projects. The third, a dedicated WP unit separated this numerical part and prepared it for direct transmission, through internal phone lines, to EDP's Datapoint. Once received, the data was formatted, edited, and verified, and if every line item within a project proved correct, single data records were created for each project line item; these were the source data for the Budget Formulation Master File (BFMF).

## 5. Software design and development

The software development activities consisted of two basic tasks. The first was the design and development of the MICOM-Datapoint communications interface module and a number of data editing and verification routines. The second task involved the design and development of applications software to satisfy management and budget analysts information reporting requirements.

The MICOM-Datapoint communications interface software was the most challenging of all. It involved a number of data transmission tests conducted for the purposes of ensuring that all the possible characters to be transmitted (some unique to the Spanish language) were correctly interpreted by the receiving end. By means of a software module, called a "formatter", it then initiated the checks of project identifying codes, goal and line item numbering, possible WP operator induced keying errors, and proper logical positioning of every data element.

The data editing and verifying routines were developed next. Their purpose was to ensure that the data received satisfied a number of identified criteria which included range checks against standard costing tables and correct length and content of data. Finally, an “update” module checked relational characteristics among data fields. If all the line items corresponding to a project satisfied all the above checks, computer records were created to make up the Budget Formulation Master File (BFMF).

The second major task was the design and development of applications software to satisfy identified reporting requirements. They included a number of periodic and exception reports for the analysis of the budget. Personnel allocation per program, listings of country projects, classifications by object of expenditures and category of activity were among the most popular. A menu containing a total of 15 different reports were developed for budget analysis purposes. In addition, a number of summary type reports showing aggregated budgetary figures were prepared for management. They were used in monitoring the evolution of the budget formulation, specifically in correlating, at different intervals of time, the existing demand for financial resources with preestablished fundings ceilings per program.

## 6. Implementation of the IPS

The initial responsibility of coordinating both the design and the implementation of the IPS was given to a team composed of an analyst from EDP, the WP units supervisor and the Program Budget systems analyst. This project management framework was especially effective in planning and designing the IPS but proved inadequate for its implementation. A number of rules and procedures were developed to ensure the proper functioning and coordination of the components of the IPS during the implementation phase. These were contained within the following documents:

\- The project formulation manual (RM), containing guidelines and standard costing tables for budget formulation, in addition to instructions to complete the carefully designed data entry form for the IPS. This input form closely resembled the format of the project budget formulation ready for publication;

\- A guide for the manual editing and verification of budgetary data (REV) for projects formulated in the data entry forms;

\- A proofreading guide (RPR) for WP generated outputs.

In addition to the above, other procedures covering almost every major operational activity were prepared. Those specifically developed for the operations of the WP units included:

\- Reception and recording of projects (PRR);

\- Entry and storage of projects (PES);

\- Procedures for data transmission (PT);

\- Correction, modification, update and back-up of projects' data (PCUB).

Among the procedures developed to facilitate the involvement of Budget Analysts were:

\- Correction of computer detected errors (PCE);

\- Modification of project data (PM);

\- Control of totals, based on project total funding requests.

Finally, procedures for the use and dissemination

RM = project formulation manual

![](/api/attachments/GE4PPJMA/fulltext/images/99ff2f44ff81972069bcc5205c565f1a68acce30ba1ed17f7686626403dd3c34.jpg)

REV = guide for manual edition and validation of project's budgetary data

RPR = guide for proofreading WP outputs

PRR = procedures for recording the reception of projects

PES = procedures for entering and storing projects

PT = procedures for project's budgetary data transmission

PCUB= procedures for correcting, updating, and backup

PCE = procedures for correcting computer detected errors

PM = procedures for modifying project's budgetary data

PDR = procedures for the distribution of reports

Fig. 2. Procedures governing the IPS implementation process.

of EDP generated reports (PDR) were prepared. Figure 2 shows the utilization of the above procedures in various stages of the IPS implementation process. Among the problems faced during implementation, the one caused by the high volume of error corrections and data modifications was the most critical. The efficiency of the WP centered data entry function proved to follow the curve of diminishing returns as the excessively high workload kept operators under continuous stress, with a resulting loss in work productivity and quality. Furthermore the conscious disruption in the free flow of information on technical problems and unannounced procedural changes caused additional unwarranted operational slow downs. Fortunately, these problems were overcome and the procedures proved, in the final analysis, effective in controlling and coordinating the IPS implementation process.

## 7. Conclusions and recommendations

In retrospect, the IPS described in this paper satisfied most of the budget formulation word and data processing requirements. After overcoming some operational data entry bottlenecks caused by outstanding errors and updates and an unexpectedly high volume of last minute project proposals that had to be processed, the main goal of the IPS was reached: the timely publication of the "Proposed Program-Budget of the Organization 80 - 81" containing the description and budgetary formulation of the administration and over 600 development projects in member countries. The document was printed almost entirely from WP generated outputs. A direct interface to photo typesetting equipment will decrease the cost and expedite this operation and is thus recommended as an IPS upgrading option.

Some practical and simple lessons were learned from having designed and implemented an IPS that integrates stand-alone WP units and EDP resources:

\- The procedures developed to coordinate the implementation of the IPS provided, indirectly, a systematic and effective operational framework to a previously unstructured and haphazard process.

\- WP units performed satisfactorily as a data entry medium. Future consideration should be given to direct entry, by means of an interconnection, to include OCR input if proved feasible and economical.

\- WP operators training and workload assignments are important enough activities to warrant management attention.

\- Technical considerations for determining the feasibility of an interface between WP and EDP hardware/software are not trivial. They involve, among others, the analysis of the profiles for both ends of the data transmission components, compatibility and/or recognition of characters by the sending and receiving ends (specifically relevant if a foreign language is employed), and communications software development.

When this paper was being written the General Assembly of the OAS was in session, discussing (among other things) the bie-nial budget for the organization. Their main source of reference was one of the tangible benefits from the IPS described here, namely the document entitled "Proposed Program-Budget for the Organization 80 - 81". The outcome of the final budgetary decisions at this meeting will produce (if any modifications are approved) an update of the data bases and subsequent preparation of the operating financial accounts. This entails the creation of computerized accounts with appropriate allotment levels. The second phase of the budgetary cycle has thus begun. This phase (know as budget or financial execution) is presently being monitored by a computerized accounting system, the basis of a quarterly progress report of limited value to users. After reviewing the design and features of the accounting system, it became clear that if continuity and integrity of the budgetary cycle was to be achieved, a more encompassing financial execution IPS had to be conceived. This effort would have to include, among other tasks, the:

\- Identification of financial and programmatic informational needs susceptible to automation;

\- Recording of personnel time distribution, preferably in machine readable form;

\- Design of an IPS compatible in its configuration, data base structure, and organization with the formulation of the IPS;

\- Identification of human-machine interface issues and problems, followed by proposals for education and training programs to deal with them;

\- Development of administrative and operational procedures to facilitate the coordination of people, hardware and software into an effective IPS.

Although the sheer magnitude of the work required to carry out the above tasks would discourage most, maintaining the present budget/financial execution system is inadequate. It would hinder any attempt at determining what is the single most sought after piece of information, namely the actual monetary rate of return (calculated by dividing the total expenditures incurred in projects in that country by the total contribution of the country) of each member of the OAS.
