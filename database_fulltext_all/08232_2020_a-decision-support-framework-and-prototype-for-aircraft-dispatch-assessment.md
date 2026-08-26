---
otero_id: 8232
otero_key: "UCHB4NPK"
title: "A decision support framework and prototype for aircraft dispatch assessment"
authors: "H. Koornneef; W.J.C. Verhagen; R. Curran"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2020.113338"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Journal Pre-proof

A decision support framework and prototype for aircraft dispatch assessment

Decision Support Systems

H. Koornneef, W.J.C. Verhagen, R. Curran

![](/api/attachments/UCHB4NPK/fulltext/images/4fc07c0260c21123cd0b79ba610bf284aa4a74e703a39dc4aad9d2edb0cf49b9.jpg)

PII: S0167-9236(20)30093-2

DOI: https://doi.org/10.1016/j.dss.2020.113338

Reference: DECSUP 113338

To appear in: Decision Support Systems

Received date: 11 November 2019

Revised date: 28 May 2020

Accepted date: 31 May 2020

Please cite this article as: H. Koornneef, W.J.C. Verhagen and R. Curran, A decision support framework and prototype for aircraft dispatch assessment, Decision Support Systems (2019), https://doi.org/10.1016/j.dss.2020.113338

This is a PDF file of an article that has undergone enhancements after acceptance, such as the addition of a cover page and metadata, and formatting for readability, but it is not yet the definitive version of record. This version will undergo additional copyediting, typesetting and review before it is published in its final form, but we are providing this version to give early visibility of the article. Please note that, during the production process, errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

© 2019 Published by Elsevier.

# A Decision Support Framework and Prototype for Aircraft Dispatch Assessment H. Koornneef<sup>a,1</sup>, W.J.C. Verhagen<sup>b</sup>, R. Curran<sup>a</sup>

<sup>a</sup>Delft University of Technology, Faculty of Aerospace Engineering, Kluyverweg 1, 2629HS, Delft,

The Netherlands

<sup>b</sup>RMIT University School of Engineering, Department of Aerospace Engineering and Aviation, Building 57, Level 3, 115 Queensberry St., Carlton 3053, Victoria, Australia

## CRediT author statement

Hemmo Koornneef: Conceptualization, Methodology, Software, Validation, Formal analysis, Investigation, Data Curation, Writing - Original Draft, Visualization Wim Verhagen: Writing - Review & Editing, Validation, Formal analysis, Investigation, Supervision, Project administration, Funding acquisition Richard Curran: Writing - Review & Editing, Supervision, Funding acquisition

## Abstract

When an aircraft experiences an unexpected issue during flight operations, a technician determines whether the aircraft can safely perform the next flight. This operational decision process - known as dispatch assessment - has to happen within limited available time between aircraft arrival and departure. Currently, technicians face two main problems during the assessment: lack of access to decision support information and a time-consuming process for finding relevant information in extensive maintenance manuals. These issues often lead to delays and additional costs and are indicative of three larger challenges in the decision support domain: 1) a paucity of decision support models and applications for operational processes in maintenance; 2) relatively few efforts in applying and evaluating artifacts in experimental and real-life operational settings; and 3) a lack of systematic development, application and eva complex decision processes in maintenance. This paper applies a design science research approach to address these challenges and introduces two novel artifacts: a decision support framework for real-time decision making in aircraft dispatch, and a web-based prototype tool accessible through mobile solutions. The practical framework and prototype is validated through two representative application and evaluation studies, one in an experimental setting and one in an operational environment. Results show significant time savings and strong qualitative indications towards a higher incentive to use documentation and reducing human risk factors that lead to maintenance error.

Keywords: decision support, aircraft maintenance, dispatch assessment, information retrieval, data integration, e-maintenance

## 1. Introduction

Air transport is known for being the safest mode of long-distance travel. Among the many factors that contribute to the safety of air transport, maintenance is essential to the airworthiness of the aircraft. However, maintenance also can have a significant effect on flight operations, for instance through delays; 5.8% of all flights in Europe still experience delays due to direct aircraft technical causes, resulting in an estimated €2.8 billion in additional cost every year [1]. Hence, research focusing on mitigating the operational impact of unexpected maintenance issues is vital.

In aircraft maintenance, dispatch assessment is the process of determining the best solution to resolve unexpected maintenance issues. It is performed during operations and at the apron, between the arrival and departure of the aircraft. The assessment is performed by line maintenance technicians and both the decision and subsequent maintena $\mathbf { \Psi } _ { \mathbf { \mathbf { K } } \mathbf { \mathsf { t } } } \quad \mathbf { \Psi } ^ { \mathbf { \cdots } } .$ ork need to be completed before the next scheduled departure of the aircraft to avoid delays Typically, technicians have limited access to equipment, tools and support information at the $\mathrm { a _ { \mathrm { r } } }$ ron, leading to a dispatch assessment process which is time consuming, burdensome and generating sub-optimal decisions. This can be illustrated by prior research, where it is indicated that technicians spend up to 30% of their time gathering task support information instead of performing maintenance [2]. Furthermore, though it is mandatory to use documentation $d ^ { \cdots } \mathrm { i n _ { \bar { s } } }$ maintenance execution, technicians usua lly make a continuous trade-off between safety, $\mathsf { l e } _ { \mathsf { L } } \mathsf { a } ^ { \mathsf { I } } \mathsf { \Lambda } .$ ity and efficiency [3] as the time for performing dispatch assessment and subsequent maintenance is limited (e.g., typically no more than 30 minutes for narrow-body aircraft such as the Airbus A320 and Boeing 737, routinely used in continental air transport). This has a negative effect on well-known human risk factors in aircraft maintenance (e.g., stress, pressure and complacency) that can lead to maintenance errors or even accidents [4, 5].

While these issues are specific to the dispatch assessment process in aircraft maintenance, they point towards a set of larger challenges in decision processes that have seen relatively little attention in decision support research (see also Section 2):

 Decision support for operational processes in maintenance: existing work in maintenance applications tends to focus on supporting decision-making for maintenance planning and scheduling, spanning time horizons of weeks, months or even years [6, 7].

 Application and evaluation in real-life operational maintenance environments: decision support systems are typically thoroughly evaluated, but practical case studies highlighting application and evaluation within real-life processes - especially when constraining oneself to operational maintenance - are not prevalent. Research shows that there is a lack of correlation between theoretical systems and actual system use [8, 9]. To overcome this problem, researchers in the domain stress the need for more case studies [10–14].

Digitization and automation of complex decision processes in maintenance: while the field of e-maintenance focuses on processing, integration and distribution of information [15] to support decision processes, major gaps remain, such as a lack of models and methodologies for decision making in distributed environments, understanding of human-machine interactions (critical for decision support systems, as opposed to algorithmic solutions) and a lack of evaluation metrics [16].

This research contributes to the state of the art by addressing these challenges within the context of the dispatch assessment problem. To do so, a design science research (DSR) approach has been followed to generate two main artifacts: 1) a novel decision support framework for real-time decision making in aircraft dispatch, built on basis of a formalized decision process [17]; 2) a web-based prototype tool accessible through mobile solutions, which has been developed within the Clean Sky 2 AIRMES project [1, 18]. Evaluation of these artifacts has been performed by considering two applications, allowing for quantitative and qualitative analysis of the core elements of the framework and prototype. From a practical point of view, this research addresses information retrieval and subsequent use in the dispatch assessment decision process. This enables technicians to evaluate more decision options and to make better-informed decisions faster. It is precisely on these points that the evaluation efforts have focused.

The remainder of this paper reflects these considerations. First, related work informing the current state of the art is discussed in Section 2. Subsequently, the two artifacts (i.e., the decision support framework for aircraft dispatch and the web-based prototype tool) are discussed in more detail. Evaluation of these artifacts is presented in Section 4. Finally, conclusions and recommendations for future research are given.

## 2. State of the art

In this Section, relevant research regarding decision support - from a methodological perspective and from a domain-specific perspective - is discussed. In particular, after briefly discussing general decision support systems (DSSs) aspects, decision support for maintenance is covered in detail. Finally, some major challenges are identified, supporting the statement of novelty in Section 1.

## 2.1. A general perspective on decision support systems

The rapid growth of information in terms of variety (i.e., data formats), velocity (i.e., speed of data generation, processing and use) and volume (i.e., data size in bytes) [19] presents new opportunities in DSSs research and applications, especially when combined with web-based DSSs. However, the integration of all these heterogeneous and often distributed data sources remains a exploit these unstructured or semi-structured information sources can lead to poorly informed decision making [21].

While there is an overall consensus that the use of a DSS leads to better decisions, a lack of correlation between theoretical systems and actual system use has been pointed out [8, 9]. As a remedy, case studies are called for in literature [11, 13, 14]. Case studies are a valuable asset to build theory [22]. Moreover, case studies improve collaboration between decision makers and system designers, which lead to systems that address real-world problems [23].

From a methodological perspective, design science research (DSR) is a well-established and growing approach within the DSS domain that tries to bridge the aforementioned gap between theory and practice. DSR aims to develop novel technology-based solutions to address real-world business problems, and typically results in the development of an artifact before a sc ientific contribution is made [24, 25]. Given the focus on the relevance of DSR [26], it is surprising that a significant amount of publications lack evaluation and merely describe developed artifacts without determining worth, effectiveness or usefulness [27].

## 2.2. Decision support in the maintenance domain

When considering decision support in maintenance, it is important to note that the increasing flow of information, paper-based use of documentation, reliance on legacy systems and the relatively slow digitization in many maintenance application domains [28] are issues that result in reduced system availability. There is a need in maintenance for a digital transformation that enables real-world solutions. From a methodological perspective, e-maintenance approaches have been touted for remote decision support and continue to evolve with new emerging technologies for processing, integration and distribution of information [15, 29]. However, there are still gaps in current e-maintenance research, such as a lack of validated models and methodologies for decision making in distributed environments, understanding of human-machine interactions and a lack of evaluation metrics [16].

When considering decision support applications in maintenance, the majority of recent literature focuses on condition-based maintenance policies and predictive maintenance approaches (e.g., [30–32]). A substantial body of work provides decision support for strategic maintenance planning and tactical scheduling in order to optimize system availability and minimize costs. These works usually span time horizons of days, weeks, months or even years [6, 7].

Only a few publications address operational decision support in aircraft maintenance, where issues that require (near) real-time resolution are considered. Two of the most relevant publications are by Papakostas et al. $( 2 0 1 ^ { \circ } , \mathrm { ~ a _ { \scriptscriptstyle 2 } ^ { \mathrm { ~ \circ ~ } } } ^ { \mathrm { ~ \circ ~ } }$ Dhanisetty et al. (2018), where the work of Papakostas et al. [33] addresses short-term maintenance planning within a multi-criteria decision support framework to improve aircraft operability and minimize maintenance costs. Dhanisetty et al. [34] developed an approach for multi-criteria decision making for operational maintenance decisions with time horizons of $\smash { \mathrm { ~ \bf ~ \psi ~ } _ { \mathrm { ~ L ~ } } ^ { } }$ urs or a few days at maximum. Both works make substantial assumptions regarding the type of tasks, task content and acceptable time horizons within their decision processes, which does not necessarily reflect (near) real-time operational maintenance processes where decisions need to be formed in under an hour, if not nearly instantaneously.

Synthesizing the $\hat { \cdot }$ revious discussions gives rise to the three main challenges identified in the introduction: 1) decision support applications for operational processes in maintenance are relatively rare; 2) application and evaluation of decision support systems in real- life operational maintenance environments is subject to improvement; and 3) digitization and automation of complex decision processes in maintenance is held back by a lack of validated models and associated evaluation efforts.

## 3. Methods: Dispatch assessment framework and prototype

## development

To address the challenges identified in Section 1 in the context of the dispatch assessment problem, it is necessary to better understand and formalize this problem first. This is covered in Section 3.1. This in effect is the first step in the design science approach which is applied in this research. The next step in this approach is to introduce two artifacts: 1) a novel framework for real-time decision support for the dispatch assessment problem; 2) a web-based, mobile DSS prototype to aid technicians in dispatch assessment and subsequent maintenance execution. The prototype has been initially developed after a first version of the framework had been defined; subsequent versions of both artifacts have been developed in an iterative and interdependent and evaluate the developed artifacts, which is covered in Section 4.

## 3.1. Formalizing the dispatch assessment process

During dispatch assessment the technician -being the decision maker- has a central role in the process; he/she performs the assessment and necessary (subsequent) maintenance work, and is responsible for signing off on the airworthiness of the aircraft. Usually, the technician is in close contact with the troubleshooting $\mathbf { \delta } \mathbf { \ d e _ { F } }$ artme nt (TS), which assists technicians in performing the prepares required (paper-based) documentation for maintenance execution. The maintenance control center (MCC) has the overview of the maintenance process as a whole and is responsible for operational and strategic maintenance planning. The ope rations control center (OCC) monitors and manages the daily flight operations and can provide support when a dispatch decision may lead to flight delay or operational constraints due to a deferred item<sup>2</sup>. The captain is the pilot responsible for the safe operation of the aircraft. This includes the authority to refuse a proposed (temporary) fix suggested by the technician if the captain believes it impairs safe continuation of flight operations in any way.

Figure 1: Typical stakeholders in the dispatch process.

An example of the stakeholders and their communication lines in a situation where the maintenance organization is part of the airline is provided in Figure 1. A system that shares the same information between stakeholders improves collaboration and can reduce miscommunication, independent of the organizational structure.

With the stakeholders defined, the established 8-step approach proposed by Baker et al. [17] is adopted to formalize the dispatch decision process.

## Step 1: define problem

A problem statement that clearly describes the initial and desired conditions to all stakeholders is essential. In aircraft dispatch decision making the initial condition is that an aircraft endures an unexpected issue for which a solution must be found. In an ideal situation, the optimal dispatch solution does not compromise safety, is well- informed and is determined as soon as possible within the turnaround time, leaving more time to perform maintenance. Hence, the problem for an individual dispatch decision is defined as: “Making a well-informed dispatch decision currently requires too much time, leading to delays and additional costs. Dispatch decision making should be done within a fraction of the turnaround time and without compromising safety.”

## Step 2: determine requirements

The requirements describe conditions that feasible solutions must meet. In aircraft dispatch globally-used standard for flight delay is defined by the Federal Aviation Administration (FAA): a flight is considered delayed if it departs or arrives 15 minutes later than its scheduled departure or arrival time. Hence, the requirements for a dispatch solution are that 1) a dispatch solution shall not comprise the airworthiness of the aircraft; 2) a dispatch solution shall not result in departures later than 15 minutes after the scheduled time of departure; 3) all available alternatives shall be evaluated.

## Step 3: establish goals

Baker et al. define goals as follows: “Goals describe broad statements of intent and desirable programmatic values” [17]. Given this definition, the goals for individual dispatch decisions are to warrant safety by adhering to maintenance documentation procedure, and to minimize the decision time.

## Step 4: identify alternatives

When an aircraft experiences an issue, a technician will have to consult the minimum equipment list and the troubleshooting manual to identify available maintenance alternatives, for example deactivating or replacing a component. With thousands of tasks in each of these documents, identifying the maintenance alternatives for a given defect is currently a time-consuming process. Each alternative has an associated expected dispatch outcome depending on the type of maintenance task and the time required to complete the task, assuming that other conditions to perform maintenance are met (e.g., availability of licensed technicians, spare parts, support equipment).

## Step 5: develop evaluation criteria

Criteria are used to evaluate and compare the available alternatives. The main criteria for aircraft dispatch are safety, time and cost.

## Step 6: select decision-making tool

The number of tools available for operational decision making are scarce, especially in the (aircraft) maintenance domain. Information about the functionalities of these systems is often very limited to protect commercial interests. To the best of our knowledge, there is currently no off-the-shelf solution available that supports real-time operational dispatch decision making, where real-time is defined as: providing all required and up-to-date information to decide what to do now.

## Step 7: apply tool and select alternative

A technician evaluates the maintenance alternatives and associated expected dispatch outcomes, and subsequently selects the optimal alternative.

## Step 8: validate the answer

The selected dispatch solution is validated by comparing the expected outcome with the realized outcome (e.g., with respect to maintenance execution time and departure time).

The formalization of the dispatch process reveals that the problems in current dispatch decision making originate at Step 4, which ultimately leads to not always meeting the requirements and goals. To address these issues, two artifacts have been developed and are introduced in the next subsections.

## 3.2. Artifact 1: a framework for aircraft dispatch decision support

Following the DSR approach, a novel framework for a dispatch decision support system has been developed. It is visualized in Figure 2. The framework consists of the three elementary layers for a DSS (i.e., model, database and user interface [35]) and is expanded with a decision criteria layer to stress the influence of criteria on the decision outcome. The criteria layer indicates which factors influence the decision, and subsequently affects the type of data required in the database layer. The core of the framework for dispatch decision support is shaped by a 6-step model that describes the process of going from a fault or defect to a dispatch decision. The user interface layer pinpoints where in the process model the user interacts with the system. The individual framework layers are discussed in detail from top to bottom in the following sections.

Figure 2: Framework for aircraft dispatch decision support.

## 3.2.1.Criteria layer

The criteria layer is located at the top of the framework. The number one criterion in aviation is safety; the airworthiness of the aircraft should never be compromised. In the case of aircraft maintenance and dispatch assessment, safety is integrated through procedures and policies in maintenance documentation. All alternatives are considered safe as long as technicians follow the procedures described in the documentation. In aircraft dispatch there is a strong focus on on-time performance and thus time is an important criterion. Both the time required to co mplete the maintenance following from a dispatch decision as well as the time available before the next departure are relevant to evaluate alternatives. Another criterion that can be taken into account is the historical chance of success of a chosen course of action (i.e., selection of one or more maintenance action(s)). Provided that trustworthy data is available, prior attempts at resolving the same or a similar issue can be used to generate probabilities of success for future courses of action.

While not included in the current work, due to the absence or confidentiality of recorded data, the operational impact criterion could be included by considering the total costs associated with a particular maintenance action, consisting of direct costs (e.g., spare parts, labour), grounding costs (e.g., parking, towing) and disruption costs (e.g., delay, cancellation) [34]. Of these items the disruption costs are especially complex to include. Examples in literature discuss minimizing these costs through optimization models, which include costs such as passenger delay and flight cancellation costs [36, 37]. The complexity of these costs is further illustrated by the fact that a particular dispatch option can lead to additional fuel consumption, for example due to required re-routing for not being allowed to fly in icing conditions. Moreover, costs associated to a maintenance action are also affected by the aircraft’s location (e.g., in-house maintenance is usually less costly than outsourcing, airport ground and hand ing fees vary). Integration of such an optimization model could further enhance dispatch decision making. The location criterion can also provide information about the availability of required skills, spare parts and equipment.

## 3.2.2. Database layer

The database layer provides the required information to perform the steps in the process model (see next subsection) and includes the following sources:

Aircraft technical log contains the maintenance history of the aircraft, including defect/fault information. This is traditionally paper-based, but industry is gradually transitioning to a digital version. The aircraft technical log must be on board of the aircraft during flight operations.

Aircraft details contains detailed information of each individual aircraft in the fleet, such Customer Serial Number (CSN). This information is required in subsequent steps of the process, for example to import the flight schedule and to determine applicable content in maintenance manuals.

 Maintenance documentation contains maintenance documentation as provided by the manufacturer. Examples relevant for dispatch assessment include the Troubleshooting Manual (TSM), the Aircraft Maintenance Manual (AMM), the Aircraft Schematics Manual (ASM) and the Electrical Standard Practices Manual (ESPM), and the Minimum Equipment List (MEL), which describes equipment which is allowed to be inoperative as long as subsequent operational and/or maintenance conditions are met. Maintenance documentation is frequently updated and it is of utmost importance to always use the latest version during maintenance execution. A complicating factor for using this data is that documents can be provided in different digital formats (e.g., SGML/XML or PDF), each requiring different approaches for processing.

 Criteria evaluation data contains data to enable evaluation with respect to specific criteria. For example the flight schedule and data on the average time to complete a maintenance task can be used to evaluate an alternative with respect to the time criterion. The information in this database is highly dynamic and requires real-time processing. For example, it is essential to use the latest flight schedule information to calculate the time available for dispatch and subsequent maintenance.

Decision history this database contains the output of the DSS. This includes the selected decision, the available time before departure when the decision was made and the expected dispatch outcome. This information can then be used to compare the expected outcome knowledge-driven DSS.

## 3.2.3. Process model layer

The developed process model entails the following six steps:

## Step I. Collect defect reports

The first step is to determine if there are any reported issues with the aircraft. Each aircraft digital version of the aircraft technical log (e.g., the Electronic LogBook (ELB)) this process is automated in the prototype dispatch decision support tool.

## Step II. Collect aircraft data

The tail number is used to retrieve the aircraft manufacturer, aircraft model and Customer . The manufacturer and model of the affected aircraft are used to determine the $\operatorname { r } { } ^ { 1 } .$ vant maintenance manuals and the CSN is used to determine the applicability of the content within those manuals.

## Step III. Identify maintenance alternatives

Each troubleshooting task has a number of maintenance tasks associated to it, from which a combined list of unique maintenance tasks is generated. An additional source is the Minimum Equipment List (MEL) that provides alternatives to defer corrective maintenance for some issues. Deferral of an issue typically still requires some type of (light) maintenance action, such as deactivating a system. The combination of maintenance and deferral actions are the maintenance alternatives a technician can consider during

dispatch assessment.

## Step IV. Filter and rank maintenance alternatives

After a technician selects an issue to assess before dispatch, the available maintenance tasks are filtered on effectiveness by the CSN. Moreover, removal a nd installation tasks are combined. These are separate tasks in the manual but usually performed sequentially in an operational environment. Furthermore, data to evaluate alternatives by different criteria is imported, for example the flight schedule to calculate the time available before the next departure. The filtered tasks can then be ranked by criteria and optionally by airline preference (i.e., an airline might prefer deferral of corrective maintenance).

To further improve the alternative ranking, machine learning methods such as support vector machines or deep neural networks can be applied, once the decision history discussed in step VI contains sufficient data points (which is not the case in the applications included in this study - see Section 4). By comparing previous expected outcomes with the realized outcomes of dispatch decisions for similar issues, the accuracy of future expected outcomes can be optimized (e.g., y considering the historical success-rate of each corrective maintenance task for the current issue).

## Step V. Provide alternative-dispatch outcome overview

The system provides an overview of the available alternatives and instantly shows the expected dispatch outcome when an alternative is selected. The expected dispatch outcome

Based on feedback from industry experts five dispatch outcomes are defined, which is an dispatch outcome is a GO, where the technician cannot find or reproduce the reported issue. This situation is known as No Fault Found (NFF) and is usually closely monitored by the MCC for recurrence. Secondly, a GO-IF(P) involves an issue that does not affect safety or performance, but operator-specific restrictions may be imposed (e.g., a seat with a defective in- flight entertainment system is not sold). Thirdly, a GO-IF(O) involves an issue with a MEL item and is known as dispatch by MEL. It refers to a situation where the corrective maintenance action can be deferred, but must be executed within a prescribed repair interval. This offers operators the possibility to minimise flight disruption and plan corrective maintenance actions at a more convenient time and/or location. An issue can only be deferred if there are no conflicts with existing deferred items. Typically, deferral still requires some light maintenance task and may impose operational restrictions. The fourth outcome is a GO-IF(M) where an issue cannot be deferred because it is a safety critical item or conflicts with an already deferred item. Corrective maintenance must be performed and can be completed without conflict with respect to the criteria. The fifth and most disruptive outcome is a NO GO where the issue cannot be deferred because it is a safety critical item or conflicts with an already deferred item. Corrective maintenance must be performed and leads to not meeting one or more decision criteria. The flight is delayed an aircraft swap [39]).

## Step VI. Communicate and store decision

Once a technician determines the optimal maintenance alternative and the captain concurs, the decision needs to be disseminated amongst the stakeholders (e.g., MCC, OCC). The decision and relevant variables are stored in the database for future reference.

## 3.2.4. User interface layer

The user interface (UI) is essential for the effectiveness of the decision support system and is located at the bottom of the framework. Moreover, as the framework describes a human-in-the-loop system, each human actor, or user, in this system should be able to interact with the DSS at the right point(s) in time. From a high- level perspective, the other framework layers describe the automation of the majority of steps in the decision making process, including information retrieval, alternative generation, filtering, ranking, and decision communication. The user is involved in the following key steps:

 Defect selection: the user initiates the dispatch assessment process by selecting the defect from the aircraft technical log he/she wishes to focus on.

 Alternative selection: the user is in charge of the assessment process by selecting a preferred alternative from a ranked list of alternatives. As such, the user is able to overrule the ranking, allowing the inclusion of personal or organizational preferences and/or tacit knowledge not represented in the dispatch assessment framework to influence the decision making process. In effect, this retains the ultimate authority in the process in the hands of the human actor.

 Alternative confirmation: the user verifies the output of the dispatch assessment process

through conscious confirmation of the preferred alternative.

To allow for these actions, the UI should be intuitive and provide the flexibility for technicians to combine the information provided by the DSS with their tacit knowledge (e.g., the characteristics of a specific aircraft; while technically identical, individual aircraft have their own characteristics and behaviour).

Specific details about the UI developed for the prototype tool for dispatch assessment are described in the next section.

## 3.3. Artifact 2: Prototype

making. The prototype implementation (covering its technology, user interface aspects and application process will be discussed in more detail.

From a technological perspective, the prototype mobile tool for dispatch decision making is based on Node.js<sup>3</sup>. It provides a suitable platform for real-time web-based DSSs due to its fast, asynchronous processing and large number of available simultaneous connections with high throughput. Node.js supports server-side processes, which largely cover the database and process model layers described above. A client-side user interface (UI) has been developed using HTML and CSS and wrapped into an Android app. Technicians can access the prototype on desktop computers using an internet browser and on tablets using the aforementioned app. In line with the framework, a 3-step user interface is defined where the user consecutively selects the defect to assess, the appropriate maintenance task in the current situation and then confirms the task to execute.

The 6-step process model that was introduced in Section 3.2.3 is applied to elucidate the process elements of the prototype; details regarding the underlying technology and UI are further discussed and visualized as part of these elements.

## Step I. Collect defect reports

The process starts with the logging of a defect report. Once a maintenance issue is captured in a defect report and duplicated to a ground server, the prototype imports the report as a

JSON file<sup>4</sup>, which includes information such as the tail number and fault message.

## Step II. Collect aircraft data

The tail number associated to the defect report is used to collect aircraft details from the operators’ fleet information, such as the manufacturer, model and CSN. These details are used to determine the related maintenance manuals, what content in those manuals is applicable to this aircraft and to retrieve the flight schedule of the aircraft during subsequent steps in the process.

## Step III. Identify maintenance alternatives

Three maintenance manuals are implemented in the prototype and are consulted: the troubleshooting manual (TSM) to identify possible causes and solutions for the reported defect, the minimum equipment list (MEL) to identify deferral alternatives and the aircraft maintenance manual (AMM) to provide the maintenance procedures during task execution.

## Consulting the TSM

The TSM provides an overview of faults or warnings and their associated troubleshooting task(s). Subsequently, each associated TSM task provides a “Referenced Information” table listing all possible maintenance alternatives to resolve the issue.

Table 1: MEL repair interval categories

<table><tr><td>Category</td><td>Repair interval (hrs)</td></tr><tr><td>A</td><td>specified by certificate holder</td></tr><tr><td>B</td><td>72</td></tr><tr><td>C</td><td>240</td></tr><tr><td>D</td><td>2880</td></tr></table>

## Consulting the MEL

For some issues the MEL provides options to defer corrective maintenance for a specific interval specified by hours in operation, indicated by category (see Table 1). This enables the operator to schedule corrective maintenance at a more convenient time and place without interrupting the flight schedule.

## Automating alternative identification

Manual consultation of the TSM and MEL is time-consuming, especially considering that technicians do not have direct access to maintenance documentation at the apron. The prototype mobile tool resolves this issue by automating the alternative identification process, thereby saving valuable time in the turnaround process. The TSM and AMM are provided in SGML<sup>5</sup> format, whereas the MEL is provided in XML format. The manuals are processed by a custom-made parser <sup>6</sup> that is able to fully index the content of document containing information of all tags (e.g., indices, properties), which can then be used to retrieve the actual content fast and efficiently. Simultaneously, metadata (e.g., task reference, title, CSN effectiveness, ATA chapter and section, revision date) for each individual task in the manuals is stored in separate JSON files for later reference.

To determine the maintenance alternatives in the TSM, the prototype mobile tool uses the fault message to identify the associated TSM task(s). Subsequently, the content of each of these TSM tasks is checked for the referenced information table from which the individual (AMM) alternatives are extracted. For the MEL the process is based on the ATA Chapter and Section number associated with an issue. The MEL content associated to this chapter and section refers to specific AMM alternatives to defer the defect. The entire process of extracting information from the manuals as well as the maintenance alternative identification is automated in the prototype mobile tool and results in a single JSON file with all maintenance alternatives for the given issue.

## Step IV. Filter and rank maintenance alternatives

The first action in this step is to filter out alternatives that are not applicable to a specific aircraft. The prototype mobile tool automatically excludes these alternatives by checking the applicability in the task metadata JSON files.

Safety is critical in aviation and is integrated by adhering to the procedures described in maintenance manuals. The prototype mobile tool contrib utes to safety by facilitating efficient use of maintenance documentation on and off the apron. However, it is also imperative to minimize flight disruption and therefore time is the other critical criterion to evaluate maintenance alternatives.

## Available time

The time available to perform dispatch assessment and subsequent maintenance tasks is determined by the current time and the scheduled departure time of the aircraft. To have the most up-to-date calculation of the time available, the latest flight sc hedule of the aircraft is imported at this point. While the FAA defines a flight delayed if it departs 15 minutes later than scheduled, the prototype mobile tool allows the operator to manually set the “allowable delay” more or less strict than the standard 15 minutes, depending on their operational targets. Hence, the available tim $\mathbf { \Omega } _ { \mathbb { R } } \mathbf { \Omega } _ { \mathbf { \Lambda } }$ formalized as follows:

$$
T _ {a} = (T _ {s t d} - T _ {c}) + T _ {a d}\tag{1}
$$

where $T _ { _ { a } }$ is the time available, $T _ { _ { s t d } }$ <sub>td</sub> is the scheduled local time of departure, <sub>c</sub>T is the $T _ { c }$ current local time and $T _ { a d }$ is the allowable delay time.

## Required time

The time required for the dispatch assessment process is the sum of the time required to make the decision and the time required to perform the subsequent maintenance task:

$$
T _ {r} = T _ {d t} + T _ {m t t}\tag{2}
$$

where $T _ { _ r }$ is the total time required for aircraft dispatch, $T _ { _ { d t } }$ is the decision time and $T _ { _ { m t t } }$ is the maintenance task time.

The decision time is minimized by providing technicians with an automatically generated overview of the alternatives and their expected outcomes, resulting in having more time available for perform maintenance tasks. The maintenance task time for removal and installation tasks are summed up when the tasks are combined as replacement tasks. The time required to perform maintenance tasks can be obtained from the maintenance planning document (MPD), although these values ignore the stochastic nature of

maintenance work and rarely match with the operational experience of operators and maintenance, repair and overhaul organizations (MROs). To provide more realistic data for decision support, another mobile tool to record actual elapsed maintenance task times was developed by a partner in the AIRMES project. Data from this maintenance elapsed time control (METC) tool is imported in the prototype for alternative ranking. The prototype mobile tool provides an overview of the applicable alternatives which are ranked by the required time to complete them (i.e., from shortest to longest time to complete). Operators may choose to display deferral alternatives first, because these are commonly preferred in an operational setting to enable scheduling of the corrective maintenance task to a more convenient time and place. Moreover, there is a chance that an initially selected corrective maintenance tas oves to be unsuccessful due to the nature of the root cause for this particular oid this uncertainty when the aircraft is operational by deferrin Step V. Provide alternative-dispatch The prototype mo list of intenance alternatives for the currently select prototype displays the expected dispatch outcom tasks in the maintenance manuals. An example of UI visua -dispatch overview is shown in Figure 3, where the ed issues are left and detailed information of an issue is displayed The navigation bar at the bottom has the following current user, the local time and date, the home button for e documentation button to browse and search in maintenance manuals, the tail number associated with the current selected issue and a button to display information about the prototype mobile tool. When an issue is selected on the left side, the right side will display “Defect details” such as the creation date of the report and the flight phase when the issue occurred. The available “Dispatch actions” will also be shown, listing the alternatives for dispatch. Once one of these alternatives is selected the “Expected dispatch outcome” is shown to the right.

Figure 3: An example of the task-dispatch overview in the prototype decision tool.

## Step VI. Communicate and store decision

Communicating the decision to other stakeholders and storing the decision with relevant variables for later reference is currently not implemented in the prototype mobile tool.

## 4. Results: Artifact application and evaluation

To properly evaluate the developed framework and prototype, two case study applications are described. The first application focuses on the information retrieval capacity in the framework and prototype (in particular, the role of maintenance documentation towards identification of maintenance alternatives). The second application focuses on a demonstration scenario which has been tested and evaluated in a real-life operational maintenance environment.

## 4.1. Information retrieval evaluation

The goal of this first case study application is to quantitatively assess the time and quality associated with finding task-specific do umentation. Below, the experimental setup and evaluation results are discussed.

Experime ntal setup: An experiment has been set up in which a set of aircraft maintenance technicians (AMT) trainees (N = 17) have been requested to address a set of six problem cases involving the identification and retrieval of task-specific documentation, using two the experiment is a within-subject repeated measures study, with a total number (17 x 6 x 2) observations. Participants have been trained to use both modes of retriev before commencing the experiment. To avoid learning effects during the experiment, the order of the problem cases and search modes have been randomized. The trainees are in an advanced stage of their training; together with careful selection of the problem cases, it was ensured that their performance was comparable to what should be expected from experienced technicians. Six problem cases were defined: each case involved a brief description of a maintenance observation that, upon correct processing, leads to a specific and unique maintenance task as observed in the Aircraft Maintenance Manual (AMM). To keep complexity in line with what would be available in operational settings, the ATA chapter (describing a specific aircraft system) was made available as part of the case information. The technicians were asked to use two

information retrieval modes: 1) Performing a search of a PDF version of the AMM chapter, which is representative of current-day operations in line maintenance in many settings; 2) Performing a manual search using a simplified version of the prototype (where steps such as defect report processing, alternative generation and evaluation were left out of the prototype). The simplified version of the prototype uses the Best-Matching 25 (BM25) algorithm to determine the relevance of documents given a user query. The prototype returns a top 20 of results to the client. Note that this is a different setup than within the described dispatch assessment: there, much more specific information is available from the necessary for information retrieval is a conservative estimate when comparing this experiment with respect to prototype application for dispatch assessment in a real-life operational environment (see also Section 4.2). he experiment has been conducted on a laptop or desktop computer in a classroom environment, and thus the trainee technicians did not experience the human factors associated to the normal operational environment. Times were observed and recorded automatically for the prototype search method using system time recordings.

has been measured using several performance indicators. For each information retrieval mode, the number of observations that yielded a cor ect document on the basis of the problem case description) have been enumera as a rough measure of quality. For the prototype retrieval mode, the number iterations per observation taken to find the correct outcome has been tracked: as the rototype allows to browse through a top-20 of ranked results, the user may need more than one iteration to identify the correct result within the ranked list. Finally, the average time in seconds required to find the correct document has been captured. Consolidated results of the experiment are represented in 2. The first indicator (AMTs that found correct document) shows a small difference between the PDF and prototype retrieval modes in the favour of the latter; while no definite conclusions can be drawn, this is a strong pointer that the quality of retrieval is not affected negatively by the novel way of searching using the prototype. For the majority of cases, AMTs are also able to navigate to the correct document using one attempt. Finally, the average time required to find the appropriate document is reduced substantially, corresponding to a 73% reduction <sup>7</sup>. It is worth noting that this reduction does not take into account the additional time that can be saved by having the search functionality available on-site, which would eliminate the time required to get physical access to the documentation.

Table 2: Consolidated results of the information retrieval experiment

<table><tr><td>Performance indicator</td><td>PDF</td><td>Prototype</td></tr><tr><td>AMTs that found correct document (out of 102)</td><td>89</td><td>91</td></tr><tr><td>Percentage AMTs that found correct document</td><td>87.3%</td><td>89.2%</td></tr><tr><td>Percentage AMTs requiring one iteration</td><td>—</td><td>67.6%</td></tr><tr><td>Percentage AMTs requiring two iterations</td><td>—</td><td>15.7%</td></tr><tr><td>Percentage AMTs requiring three iterations</td><td>—</td><td>5.9%</td></tr><tr><td>Average time required to find document [s]</td><td>203</td><td>55</td></tr></table>

## 4.2. Real-life dispatch assessment application and evaluation

Evaluation of the prototype was performed at the maintenance facilities of TAP Air Portugal in Lisbon. A maintenance scenario runs from reporting an unexpected issue through the electronic logbook (ELB) until completion of corrective maintenance tasks. The unexpected issue that is implemented as a case study is carefully selected, such that it: is not too easy so that technicians will rely on their previous experience when resolving the issue; is not to too complicated so that concerns a MEL-item with an option to defer. Given these requirements an issue with the wing anti-ice valve (WAIV) on an Airbus A321-211 was selected as a case study. The Airbus A321-211 has two WAIVs, one in each wing, and are part of the anti-icing system. The WAIV at the right-hand side may be inoperative with the valve either in the open or closed position, leading to different operational impacts. For example, the aircraft may not fly in forecasted icing conditions with the right-hand WAIV inoperative in the closed position. Below, the experimenta l setup and evaluation results associated with this case study application are discussed.

 Experimental setup: to evaluate the prototype in a real-life operational environment, a demonstration scenario has been set up which is simulated and evaluated 5 times,

involving a set of three maintenance technicians representing three major stakeholders (the technician, TS and MCC). In the case study the pilot reports a "WING ANTI ICE R VALVE OPEN" warning on the electronic centralised aircraft monitor (ECAM), indica ting an issue with the WAIV on the right-hand side of the aircraft. Once a defect is created in the electronic logbook (i.e., a digital version of the aircraft technical log) it is duplicated to a ground server and retrieved by the prototype. Based on the defect information the prototype automatically consults the AMM, TSM and MEL to identify the maintenance alternatives and subsequently filters and ranks them, following the steps outlined in Section 3.3. At this point the technician can initiate the dispatch assessment process. Each simulation results in a set of dispatch alternatives (usually comprising between 3 to 5 feasible options, depending on initialization conditions, which primarily relate to available time as per the flight schedule), which are subsequently ranked according to the time criterion. To illustrate this, Figure 3 shows the $\mathbf { \hat { \Pi } } ^ { \mathbf { { e } } } { } _ { \mathbf { \hat { \Pi } } ^ { \mathbf { { \Lambda } } } }$ ected dispatch outcome for a selected deferral alternative “Deactivation of the $U _ { \Sigma } ^ { \prime }$ Anti-Ice Control Valve to the OPEN Position”. The expected dispatch $\smash { 0 ^ { \gamma ^ { \prime } } \gamma _ { 1 } \gamma _ { 2 } ^ { \prime } }$ is based on the difference between the time available (equation 1) and the time required (equation 2) and is categorized in three categories:

1. GO-IF(P/O/M) with no delay expected, indicated in green; $T _ { r } \leq T _ { a }$ with $T _ { _ { a d } } = 0$

2. GO-IF(P/O/M) with an acceptable delay expected, indicated in yellow; $T _ { r } \leq T _ { a }$

3. NO GO, flight cancellation or aircraft swap, indicated in red; $T _ { r } > T _ { a }$

Evaluation $\mathbf { r e } \cdot \mathbf { u l } . \mathfrak { s } \colon \mathrm { B } _ { \mathcal { I } }$ automating the dispatch alternative identification and evaluation, and by bringing decision support to the technician on the platform, the decision time can be significantly reduced. All technicians participating in the simulation and evaluation were observed and interviewed. As the simulation happened within a real-life operational environment, there was insufficient possibility to 1) capture an accurate baseline for current-day processes) and 2) capture a large enough sample of measurements for meaningful statistical analysis of results. From a qualitative perspective, observations and interviews indicated that the prototype mobile tool can reduce the decision time up to 98% (i.e., from an average of 15 minutes per dispatch assessment process to 15 seconds). Note that a major part of this can be assigned towards the automated information retrieval from documentation (in line with the previously described experimental application), but this has to be extended to cover additional savings from integration of the end-to-end dispatch assessment process. Given the small number of runs, a precise distribution of savings could not be established. Qualitative benefits include the potential to consider and compare more dispatch alternatives, sharing of a consistent source of information between stakeholders, and improved availability of maintenance documentation.

## 5. Conclusions and recommendations

This paper introduced a novel framework and prototype providing real-time decision support for aircraft dispatch assessment. By following the design science research approach, these artifacts are directly linked to addressing a real-world problem, making a contribution relevant to both research and industry.

The introduced artifacts address several of the issues identified in literature by 1) providing decision support for a specific operational process in maintenance; 2) applying and evaluating the prototype through two case studies in experimental and real-life operational settings; and 3) providing web-based integration of multiple (semi-structured) data sources for real-time and on-site decision support for a complex decision process, including automated dispatch alternative identification and ranking. Quantitative evaluation shows that information retrieval time is reduced by over 70%, while the end-to-end dispatch assessment can - through automation of many of its steps, while keeping the human in the loop for essential decision making - indicatively reduce total process time by over 90%. Moreover, having instant access to relevant support documentation provides technicians with more incentive to use documentation during maintenance execution, thereby potentially reducing human risk factors that lead to maintenance error. Although the proposed framework is tailored to aircraft dispatch decision support, it may contribute in addressing similar challenges in other complex maintenance environments. To see how this could be achieved, it is worthwhile to consider replacing the aircraft-specific entries in the framework presented in Figure 2 with other complex assets, where similarities exist in recording defects, retrieving information from substantial, complex documentation, and using criteria such as safety, time, operational impact (cost), and/or location to inform subsequent decision making. There are several application domains where advances in digitalization combine with comparable timescales, pressures and constraints as acting in aviation, leading to similar operational decision-making issues. Examples include offshore assets [40], the nuclear industry [41], and healthcare applications [42]. For such applications, the framework can be maintained, but implementation will naturally require substitution of the application-specific reporting, documentation and decision processes.

Recommendations for future work include two topics. Firstly, Step VI in the process model of the framework should be implemented by storing the decision variables of completed dispatch assessments. This information is valuable because 1) it can be used to evaluate the expected implement machine learning methods in Step IV of the process model to improve the evaluation and ranking of alternatives, potentially providing more effective decision support. Secondly, the database containing the criteria evaluation data can be expanded with additional sources (e.g., formal multi-criteria decision making (MCDM) methods.

## Acknowledgements

This project has received funding from the Clean Sky 2 Joint Undertaking under the European Unions Horizon 2020 research and innovation programme under grant agreement No 681858, AIRMES project. For information, see the project websites: / and http://www.airmes-project.eu

## References

[1] L-UP, Airmes project website, (Accessed: 2019-09-11) (2019). URL http://www.airmes-project.eu/

[2] European Commission, Tatem - results in brief, (Accessed: 2019-09-16) (2012). URL https://cordis.europa.eu/project/rcn/72822/brief/en

[3] H. Zafiharimalala, D. Robin, A. Tricot, Why aircraft maintenance technicians sometimes do not use their maintenance documents: Towards a new qualitative perspective, The International Journal of Aviation Psychology 24 (3) (2014) 190–209.

[4] Y.-H. Chang, Y.-C. Wang, Significant human risk factors in aircraft maintenance

technicians, Safety science 48 (1) (2010) 54–62.

[5] L. F. Santos, R. Melicio, Stress, pressure and fatigue on aircraft maintenance personal, International Review of Aerospace Engineering 12 (1) (2019) 35–45.

[6] A. Ahmadi, S. Gupta, R. Karim, U. Kumar, Selection of maintenance strategy for aircraft systems using multi-criteria decision making methodologies, International Journal of Reliability, Quality and Safety Engineering 17 (03) (2010) 223–243.

[7] Q. Deng, B. F. Santos, R. Curran, A practical dynamic programming based methodology for aircraft maintenance check scheduling optimization, European Journal of Operational Research.

[8] S. H. Chan, Q. Song, S. Sarker, R. D. Plumlee, Decision support system (DSS) use and decision performance: DSS motivation and its antecedents, Information & Management 54 (7) (2017) 934–947.

[9] A. Rastegari, M. Mobin, Maintenance decision making, supported by computerized maintenance management system, in: 2016 Annual Reliability and Maintainability Symposium (RAMS), IEEE, 2016, pp

[10] D. Arnott, G. Pervan, A critical analysis of decision support systems research, Journal of information technology 20 (2) (2005) 67–87.

[11] D. Arnott, G. Pervan, Eight key issues for the decision support systems discipline, Decision Support Systems 44 (3) (2008) 657–672.

[12] D. J. Power, S. B. Eom, Decision support systems discipline: Achievements and needs, 15 (1) (2006) 9–21.

[13] D. J. Power, Computerized Decision Support Case Study Research: Concepts and Suggestions, Springer International Publishing, 2016, Ch. 1, pp. 1–13. doi:10.1007/978-3-319-43916-7\_1.

[14] D. J. Power, C. Heavin, P. Keenan, Decision systems redux, Journal of Decision Systems (2019) 1–18 doi:10.1080/12460125.2019.1631683.

[15] A. Muller, A. C. Marquez, B. Iung, On the concept of e-maintenance: Review and current research, Reliability Engineering & System Safety 93 (8) (2008) 1165–1187.

[16] M. G. S. Aboelmaged, E-maintenance research: a multifaceted perspective, Journal of Manufacturing Technology Management 26 (5) (2015) 606–631.

[17] D. Baker, D. Bridges, R. Hunter, G. Johnson, J. Krupa, J. Murphy, K. Sorenson,

Guidebook to decision-making methods, Tech. Rep. WSRC-IM-2002-00002, Department of Energy, USA (2001).

[18] Clean Sky Joint Undertaking, Clean Sky website, (Accessed: 2019-09-11) (2019). URL https://www.cleansky.eu/

[19] D. J. Power, Data science: supporting decision- making, Journal of Decision systems 25 (4) (2016) 345–356.

[20] H. K. Bhargava, D. J. Power, D. Sun, Progress in web-based decision support technologies, Decision Support Systems 43 (4) (2007) 1083–1095.

[21] R. Rao, From unstructured data to actionable intelligence, IT Professional 5 (6) (2003) 29–35. doi:10.1109/MITP.2003.1254966.

[22] A. L. Cavaye, Case study research: a multi-faceted research approach for is, Information systems journal 6 (3) (1996) 227–242.

[23] D. J. Power, F. Burstein, R. Sharda, Reflections on the Past and Future of Decision Support Systems: Perspective of Eleven Pioneers, Springer, New York, NY, 2011, Ch. 2, pp.

[24] A. Hevner, S. T. March, J. Park, S. Ram, Design science in information systems research, MIS quarterly 28 (1) (2004) 75–105.

[25] R. Baskerville, A. Baiyere, S. Gregor, A. Hevner, M. Rossi, Design science research contributions: finding a balance between artifact and theory, Journal of the Association for Information Systems 19 (5) (2018) 3.

[26] D. Arnott, G. Pervan, A critical analysis of decision support systems research revisited:

[27] D. Arnott, G. Pervan, Design science in decision support systems research: An assessment using the hevner, march, park, and ram guidelines, Journal of the Association for Information Systems 13 (11) (2012) 1.

[28] J. Groenenboom, Big data; the race is on, but what is the end goal?, presented at the 14th Maintenance Cost Conference, Atlanta (2018). URL https://www.iata.org/whatwedo/workgroups/Documents/MCC-2018 -ATL/Day1/1100-1130-mro-forecast-market-trend-icf.pdf

[29] O. Candell, R. Karim, P. Söderholm, E-maintenance: Information logistics for maintenance support, Robotics and Computer-Integrated Manufacturing 25 (6) (2009)

937–944.

[30] L. Lin, B. Luo, S. Zhong, Development and application of maintenance decision-making support system for aircraft fleet, Advances in Engineering Software 114 (2017) 192–207.

[31] L. R. Rodrigues, J. P. Gomes, F. A. Ferri, I. P. Medeiros, R. K. Galvao, C. L. N. Júnior, Use of phm information and system architecture for optimized aircraft maintenance planning, IEEE Systems Journal 9 (4) (2014) 1197–1207.

[32] C.-H. Lee, H.-S. Shin, A. Tsourdos, Z. Skaf, New application of data analysis using aircraft fault record data, Journal of Aerospace Information Systems 15 (5) (2018) 297–306.

[33] N. Papakostas, P. Papachatzakis, V. Xanthakis, D. Mourtzis, G. Chryssolouris, An approach to operational aircraft maintenance planning, Decision Support Systems 48 (4) (2010) 604–612.

[34] V. S. V. Dhanisetty, W. J. C. Verh making for operational maintenanc es, Transport Management 68 (2018) 152–164.

[35] R. H. Sprague Jr, A framework for the development of decision support systems, MIS quarterly (1980) 1–26.

[36] B. F. Santos, M. M. Wormer, T. A. Achola, R. Curran, Airline delay management problem with airport capacity constraints and priority decisions, Journal of Air Transport Management 63 (2017) 34–44. doi:10.1016/j.jairtraman.2017.05.003.

[37] J. Vink, B. Santos, W. Verhagen, I. Medeiros, R. Filho, Dynamic aircraft recovery problem - an op support framework, Computers & Operations Research 117 016/j.cor.2020.104892.

[38] K. Tiassou, K. Kanoun, M. Kaâniche, C. Seguin, C. Papadopoulos, Online model adaptation for aircraft operational reliability assessment, in: 6th International Congress, Embedded Real Time Software and Systems (ERTS2 2012), Toulouse, France, 2012, pp. 1–11.

[39] H.-W. M. Vos, B. F. Santos, T. Omondi, Aircraft schedule recovery problem–a dynamic modeling framework for daily operations, Transportation Research Procedia 10 (2015) 931–940.

[40] X. Yang, S. Haugen, Risk information for operational decision-making in the offshore oil and gas industry, Safety Science 86 (2016) 98–109. doi:110.1016/j.ssci.2016.02.022.

[41] X. Ding, Z. Li, M. She, Effects of information acquisition method on diagnostic task performance using digitalized interfaces, in: Advances in Human Error, Reliability, Resilience, and Performance, Springer International Publishing, 2018, pp. 300–309. doi:1110.1007/978-3-319-60645-3\_30.

[42] S. P. Bhavnani, J. Narula, P. P. Sengupta, Mobile technology and the digitization of healthcare, European Heart Journal 37 (18) (2016) 1428–1438. doi:110.1093/eurheartj/ehv770.

## Biographical notes

## Hemmo Koornneef

Hemmo Koornneef is currently a PhD candidate at Delft University of Technology, section Air Transport and Operations, where his research focuses on optimizing aircraft maintenance processes on an operational level. His work entails the development a prototype web-based mobile tool for real-time decision support during aircraft dispatch, focusing on data integration and user experience.

## Wim J.C. Verhagen

Wim J.C. Verhagen is senior lecturer at RMIT University, and formerly an Assistant Professor of Maintenance Operations in the Air Transport and Operations Section at Delft University of Technology. His research focuses on aircraft maintenance operations, with specific attention to development of knowledge-based maintenance systems, predictive algorithms and optimisation execution and support.

## Richard Curran

Richard Curran is Full Professor at Delft University of Technology and head of the Air Transport and Operations section. Among various editorial positions he is also the Editor in Chief of the Journal of Aerospace Operations and General Chair and founder of the Air Transport and Operations Symposium (ATOS).

## Highlights

 Introduces a framework for real-time aircraft dispatch decision support.

 Automates maintenance alternative identification, filtering and ranking.

 A web-based, mobile prototype evaluated in an operational environment .

 Reduced dispatch decision time up to 98% compared to current process.

![](/api/attachments/UCHB4NPK/fulltext/images/fd950e271e09f1114d6479a5b0fb8390632b9e3a20b4df8c387c4078566d7b70.jpg)  
Figure 1

![](/api/attachments/UCHB4NPK/fulltext/images/6a1985cddb1f8d695e3f3a8e85836e056c8866c1efa2bf459b21c2d2573b7954.jpg)  
Figure 2

Fault: WING A.ICE R VALVE OPEN FIN: N/A

PRF

30-11

Modified:

roe

![](/api/attachments/UCHB4NPK/fulltext/images/96284d53914799189f5b678fed05030e406bfbd7dd139f2243de06c1b440f33c.jpg)

Deactivation of the Wing Anti-Ice Control Valve to the CLOSED position MEL Action

Deactivation of the RH Wing Anti-Ice Control Valve to the OPEN position MEL Action

Replacement of the Zone Controller

Replacement of the Wing Anti-Ice Control Valve Fix success ratio: 62%
