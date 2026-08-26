---
otero_id: 3450
otero_key: "B52S94XE"
title: "A decision model for managing software development projects"
authors: "Thang N. Nguyen"
year: "2006"
journal: "Information & Management"
doi: "10.1016/j.im.2005.01.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A decision model for managing software development projects

Thang N. Nguyen <sup>\*</sup>

California State University, Long Beach, College of Business Administration, 1250 Bellflower Blvd., Long Beach, CA 90840, USA

Received 5 November 2003; received in revised form 28 November 2004; accepted 24 February 2005 Available online 7 July 2005

## Abstract

The paper first examines some issues that hinder the effective management of, and decision-making on, quality software development process and products delivery by practitioners. It then generates a decision model for managing software development projects. The model uses four concepts: mappability, accountability, interoperability and controllability in decision-making which is assumed to be based on a set of indicators that link task status of the development process and its quality assessment to the responsible authorities. The quality of the tasks, and hence, of the deliverables is measured using four attributes: completeness, correctness, consistency and compliance. A web-based example implementation is then discussed. We thus show that the model is flexible, extensible and scalable. Implementation challenges and implications are then discussed. <sup>#</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Software development; Decision model; Software project management; Software quality; Key indicators

## 1. Introduction

There are many publications addressing many different aspects of software development project management: business, managerial, technical, legal, ethical, etc. They pertain to most types of applications: governmental, military, commercial, educational, scien tific, etc. There are also many good life cycle models, excellent management methods and techniques, e.g. risk-based [6,16,36], and powerful management tools, [46] in support of the good practices of software development. The practices include project planning [34,44,45], estimation and scheduling [11,26], software requirements [58], design [37], coding and testing [8,25,59], software metrics [18,42] and measurement [57], software quality [29], risk management [15,49] and software costs [7]. The models [35], methods and techniques [31], practices [24,39,47,55,56] and tools [48] can be very broad and generic or they can also be specific and detailed. Some group of authors and practitioners argue that planning is the key [53]. Others advocate a focus on process [30] and that the process needs be improved continuously.

One important aspect is the diverse decisionmaking methods of professionals and management teams driving the projects. Thus, organizations end up with their own (ad hoc or formal) decision model for managing software development projects.

The decision model is particularly complex for large to very large, multi-year system/software projects. A good example is the Department of Army/DARPA Joint Development of the Future Combat System (FCS) that is described on the Internet [1,13,20]. The system is network-centric via the command, control, computer, communications, intelligence, surveillance and reconnaissance [10] (C4ISR) for the direct support of a collection of 18 manned and unmanned systems called family of systems. This multi-billion-dollar project over a period of 2000–2014 involves many large and small defense contractors/suppliers [21]. Its unique software life cycle model is a combined and modified life cycle model of most known models. It is a system of systems for future combat scenarios and battlefield environments [50]. Although the project has a well-defined and well-standardized process for all the phases of the Army system development, its size and complexity are overwhelming. The system requires a sophisticated project management system for proper decisionmaking.

Whether small in-house, mid-size, large or very large projects are involved; overall, there are five problems in the use of current software development management practices.

1. Unmatched structures between software developing models and organizations driving them. Software development methods are linear, whether they use large-scale waterfall, risk-based spiral, evolutionary models or a mixture of the models. They basically still embody the traditional sequence of feasibility–requirements–design– implementation phases. On the other hand, the overall organization that manages the development effort, whether it is traditional, team-based, outsourced or integrated is still essentially hierarchical (top management, middle managementprofessionals) reflecting three layers of business: strategy, tactics and operations. These two unmatched structures obscure different granularity levels in task management, introduce conflict of authority and policy, and tolerate inappropriate decision-making.

2. Process-centric versus interprocess-centric. The focus of current software development is more on the processes supporting the development, rather than on the interfaces (i.e. interprocess) between different phases and activities in the development cycle. This results in mismatches and gap between the sending and the receiving units. Mismatches occur when the receivers get more (or less) deliverables than what they actually expect. Gaps occur when the receivers must perform further work before the deliverables can be useful. Improvement schemes for better product delivery are also process-centric. The improvements are frequently piecemeal due to constraints on implementing change. Global and continuous improvement of the entire organization process would be expensive and time-consuming [32].

3. Separation of quality and metrics modeling from process modeling. In practice, quality criteria of the products and processes supporting them, as well as metrics, are formulated at a different time than the development process modeling; therefore, consistency and practical benefits are in fact difficult to determine [3].

4. Little attention paid to the building of automated, practical, relatively simple and effective decision models. Automated models for managing software development projects exist but are generally costor time-driven. Few online decision model exists to provide complete rolled-up status of, and drilleddown details from the offending tasks or incomplete deliveries, to allow timely and effective decision-making by all parties.

5. The management of the development effort is commonly placed at the project level with project managers/leaders selected from technical ranks [33] rather than business or higher management ranks (although the participation from units such as marketing, sales, support and services is solicited). Therefore, the predefined business goals are forgotten, shifted and not observed or tracked.

These issues hinder the effective management of, and decision-making on, quality software development process and product delivery by practitioners [40]. Furthermore, the nature, scope, size and complexity of software development projects, and resources (talent, funding, technology, etc.) are quite different [28].

## 2. A decision model for effective management of software development projects

A simplified software development project may be considered to have four phases:

(0) project definition (feasibility);

(1) requirements;

(2) design;

(3) construction (implementation).

The simplified model serves as the basis for presenting the five essential questions represented as: who is doing what, why, how, where and when. The model can be augmented to becoming risk-based, evolutionary or incremental.

The mappability between the development process and the organization driving it (what and why) is represented by the use of goal-directed indicators [38,43] (see Fig. 1). The accountability (who) includes the roles and responsibilities of all parties involved in the software development project. The interoperability (how) is based on the interprocess relations and quality assurance (how well) with basic quality concepts (correctness, completeness, consistency and compliance). The controllability at the interprocess interfaces (where) eliminates mismatches and gaps between processes. Finally, effective decision-making (when) depends on the indicators that express a severity level (Red—critical, Yellow—warning or Green—normal) associated with the completion of a task or a deliverable by a responsible party.

## 2.1. The what and the why: mapping between the linear software development process and the organization driving it

The problem of unmatched structures between linear development life cycle process and the organization suggests that there is a need to restructure the flat nature of the development process to link more easily to the structure of the organization (mappability). Fig. 1 shows one such mapping.

The development process consists of four conventional phases (left side). The organization is shown as representing four levels of management (right). The organization can be team-based. It may be economically and strategically distributed. It can be a collaborative effort between development business partners. It can take the structure of lead system integration in the acquisition of software components. The mapping is based on a set of goal-directed indicators (circle in the middle) similar to those obtained by Park et al. [43].

![](/api/attachments/B52S94XE/fulltext/images/ab71c43c935af978e6f1f3cc4af4038541ecd44c502659fa802eba688531b270.jpg)  
Fig. 1. Mapping between process and organization.

Table 1  
Excepts from project indicators

<table><tr><td>Task/Phase</td><td>Goal-directed indicator/key</td><td>Accountability</td></tr><tr><td>Phase 0: definition</td><td>Project definition in place, on time &amp; under budget (executive concern)</td><td>Executive</td></tr><tr><td>Task #1</td><td>Business case written</td><td>Project/first-line management and non-management personnel</td></tr><tr><td>Task #2</td><td>Project scope and objective defined</td><td>Project/first-line management and non-management personnel</td></tr><tr><td>Task #3</td><td>Customer Satisfaction objectives defined</td><td>Project/first-line management and non-management personnel</td></tr><tr><td>Task #4</td><td>Project costs and revenues estimated ...</td><td>Project/first-line management and non-management personnel</td></tr><tr><td>Task #5</td><td>Risk assessment complete and success factors identified ...</td><td>Project/first-line management and non-management personnel</td></tr><tr><td>Task #5</td><td>Quality objectives defined ...</td><td>Project/first-line management and non-management personnel</td></tr><tr><td>Task #6</td><td>Estimates and Schedules completed ...</td><td>Project/first-line management and non-management personnel</td></tr><tr><td>Task #7</td><td>-</td><td></td></tr><tr><td>Phase 1: requirements</td><td>Requirements and features identified and in place (executive concern)</td><td>Executive</td></tr><tr><td>Task #1</td><td>User requirements collected and complete</td><td>Project/first-line management and non-management personnel</td></tr><tr><td>Task #2</td><td>-</td><td></td></tr><tr><td>Phase 2: design</td><td>Design complete and on time (executive concern)</td><td>Executive</td></tr><tr><td>Task #1</td><td>-</td><td>Project/first-line management and non-management personnel</td></tr><tr><td>Task #2</td><td>-</td><td></td></tr><tr><td>Phase 3: construction</td><td>Builds, tests and product launch complete (executive concern)</td><td>Executive</td></tr><tr><td>Task #1</td><td>-</td><td>Project/first-line management and non-management personnel</td></tr><tr><td>Task #2</td><td>-</td><td></td></tr></table>

Each completion of a task of a phase or a deliverable of a task or phase is associated with a goal-directed indicator or key. Table 1 shows some tasks of project definition and the indicator associated with each.

Suppose that an executive is interested to know if the project definition Phase 0 is in place, on time and under budget. The indicators in this and subsequent phases in bold text in column 2 constitute the indicator set of the executive sponsoring the project.

Similarly, a project manager is interested in monitoring the completion of tasks in each phase looks at the indicators of all seven tasks of the Phase 0.

Some of the tasks/activities may be further decomposed and assigned to a particular first-line manager or subsequently given to non-management professionals such as the business analyst or developer. Thus, the mappability results in a structure of tightly coupled indicators. The indicators correspond to the tasks and deliverables of the four phases, as well as to the different levels of decision-making management of the organization.

## 2.2. The who: accountability

Essential elements for effective strategic, tactical and operational planning consist of accurate scope of work with a well-defined mission, objectives, strategies and tactics [2]. But if accountability is not enforced, no appropriate and timely decisions by the responsible party can be reached.

The mapping scheme implies accountability. For example, responsibility for one or several tasks (e.g. #1, . . ., #7) are assigned to a non-management professional, while the group of the seven tasks is owned by a first-line manager. The complete set is owned by an executive. The complete set must encompass all aspects of the development and delivery cycle.

## 2.3. The how: interoperability

Common practices in software development have historically placed the emphasis on process and its sub-processes for task and change management, and considered project-level management as dominant. They, therefore play down the continuing influence of higher-level management. These understate the importance of operational interfaces between processes and inadvertently make the development effort to a technical rather than a business issue; thus, many business decisions are made by technical practitioners.

![](/api/attachments/B52S94XE/fulltext/images/1035e7b42b82fa5713d5e096a70ff44c816bbde3e6bd57f7d690565d6eaca0f9.jpg)  
Fig. 2. Process and interprocess.

By shifting the emphasis from process to interprocess for interoperability (see Fig. 2) and elevating the management of deliverables, process, resources and their environment beyond and above the project management level, the organization can manage the development and delivery from an overall view encompassing business, marketing, sales, customer satisfaction views and both technical and support views.

Interoperability occurs at the interface between two organizational units: one is the sender while the other is the receiver. Thus, interoperability at all levels of granularity in an organization yields a way of detecting mismatches and gaps. The sender may give a deliverable in a format that does not match the expectation of the receiver or the receiver may receive an item that requires more unexpected work before it can be further processed. Both mismatches and gaps require rework or extra work. To eliminate mismatches and gaps the interfaces act as the control point for delivery validation and acceptance (based on the exit and entry criteria, expressed as indicators). Two examples follow.

During the project life, if any date of the planned schedule is slipped, the project is not on time. If any of the project items turns out to actually cost more than estimated, the project is cost overrun. For example:

 If the task is later than 2 weeks, and/or the cost is more than US\$ 20,000, then the project is on Red status (critical). Reasons may be documented.

 If either it is less than 2 weeks late or the cost is less than US\$ 20,000, then the status is Yellow (warning) otherwise.

 The status is Green (normal).

Table 2 shows an example of the deliverable dates between two people responsible at the interface. Exit criteria are verified by the sender and deliverables validated by the receiver based on entry criteria. Signoff may be required at this interface.

 If the difference between planned delivery date and actual delivery date (or between actual delivery date and actual receiving date) is above a certain time (e.g. 1 week), a Red indicator is flagged. Reason for lateness may be documented.

 If it is less than 1 week but not on or before the date, it is flagged as Yellow.

 If the dates are the same or the sending date is earlier, then the delivery is on time (Green).

## 2.4. The where: controllability at the interface (interprocess) to ensure quality assurance

The issue of separating quality from the process modeling leads to the need for a single, integrated point of departure from which process, deliverables, resources and environment are examined to support controllability. The indicators then allow metrics to be defined, and are measurable.

A taxonomy of quality attributes discussed in Barbacci et al. [5], can be combined with ANSI quality standards [4] and guidelines published by various quality assurance/quality control groups and organizations. These offer a set of basic measurements: completeness, correctness, consistency and compliance $\textstyle ( \mathbf { C } ^ { 3 } \mathbf { C } )$ . Quality metrics are associated with every indicator, whether at the non-management personnel level or higher level. The model is therefore qualityassured based on $\mathrm { C } ^ { 3 } \mathrm { C }$

Table 2  
Example of deliverables status (interoperability)

<table><tr><td>Sending authority (name)</td><td></td><td>Receiving authority (name)</td><td></td></tr><tr><td>Planned delivery date</td><td>12/15/2004</td><td>Planned receiving date</td><td>12/15/2004</td></tr><tr><td>Actual delivery date</td><td>12/17/2004</td><td>Actual receiving date</td><td>12/17/2004</td></tr><tr><td>Exit criteria met</td><td>☒ yes, ☐ no</td><td>Entry criteria met</td><td>☒ yes, ☐ no</td></tr><tr><td>Reason for lateness</td><td>Personnel in emergency</td><td>Reason for lateness</td><td>Caused by sender</td></tr><tr><td>Status</td><td>Yellow</td><td>Status</td><td>Yellow</td></tr></table>

Throughout the development model and delivery process, primary control is placed at the interface between two phases. Control within each process or sub-process is the responsibility of the owner; thus, controllability at the interface allows decision-making to be easily exercised.

Both interoperability and controllability are performed at the inter-process level and are scalable. This in turn allows a direct linkage between process and quality attributes of deliverables at all levels.

## 2.5. The when: effective decision-making

To aid in decision-making at any phase, the status is reported by its set of indicators. The lower indicators roll up to support the next higher level of indicators for decision-making. Information gathering during the process is readily available so that decisions makers can apply different decision schemes, based on their functions and the situations under consideration.

Generally, every organization unit and every level of management are involved in the decision-making process, within its own scope of responsibility, level of authority and roles, which can be primary or supporting. A decision scheme using the indicators, described by Rouse in Hopple [27] and diversity of decision styles [19] can be readily applied: thus (1) situation assessment can be used in conjunction with the set of indicator statuses and (2) planning and commitment, and execution and monitoring can be incorporated in deliverables reporting.

## 3. A web-based example implementation of the decision model

For proof of concept, without loss of generality, we discuss only the basic phases and basic key indicators of a simplified project. In this implementation, we use the four-phase process of software development: (1)

project definition ( feasibility), (2) requirements, (3) design and (4) implementation (see Fig. 3). The development can use any life cycle model. For simplicity, we assume that the organization consists only of three layers of decision-making: the nonmanagement personnel (professionals), the projectrelated manager (business) at the mid-layer and the executive sponsoring the project, corresponding, respectively, to the operational, tactical and strategic levels. The implementation consists of a set of indicators, each of which measures the completion or performance of a task within a phase. Each level of control is represented by one screen, which is linkable to others. Project documents, artifacts, codes, etc., are presented as Word documents or other files. We show the information flow for decision-making via two main capabilities of the decision model: drill-down details and roll-up status.

## 3.1. Drill-down details

For a given project, e.g. Online Project Tracking (selected from the drop-down list of the top left as indicated by the arrow in Fig. 3A), the sponsoring executive can examine the project’s overall status by pressing the show status button (see the arrow below the first). The status pane at the bottom shows that the project is at the completion of Phase 0 and its status is Red.

The executive can drill down to obtain details by clicking the gray button on the right (indicated by the arrow near the button) to obtain the Phase 0 window (Fig. 3B). The executive then presses the show status button of Phase 0. The result is shown with the work item, which causes the Red status as indicated by the checked radio button. The cell containing the item is highlighted in Red.

The executive can obtain the document or artifact that causes the alert by pressing the Link button (arrow at the bottom of Fig. 3B). The next window shows a word document of the project (Fig. 3C). The Project Plan is missing in the report (documented as to be submitted) hence the Red status. The Project Plan item is the offending item.

Since the project is in Red status (NO GO) it is interpreted as a ‘‘stopper’’. The executive, at his/her discretion and within his/her scope of responsibility, may choose to override it to allow the development effort to continue to the next phase by changing the Red to a Yellow in his/her window.

![](/api/attachments/B52S94XE/fulltext/images/1ff4c9eeffbe92e1277d1685f42cdeaea389d81c0e91343c52de4f6231b01ff5.jpg)  
Fig. 3. (A) Executive window, (B) Phase 0 window and (C) project document.

![](/api/attachments/B52S94XE/fulltext/images/e9bd1afd69adb0f26265dfbe4d194d2332852bd961b9d24634e42a2e421eb01b.jpg)  
Fig. 4. Overriding action.

By changing the radio button on the right side of the Executive Summary window, the executive is presented with a dialog (see Fig. 4) in which his/her justification for status change is permanently recorded: it is not deletable in the application data store. The change of status and the justification are automatically sent to all parties via e-mail.

## 3.2. Roll-up status

The responsibility of a non-management professional is to produce software development documents and artefacts, e.g. the Distance Learning Report in Fig. 5A. The artifacts include any type of documents or any deliverables, e.g. software code. The report is checked by other professionals, review board or immediately higher management team as dictated by the process.

The evaluation rule for example is: if the section corresponding to an indicator text is well prepared and well written, then the indicator is marked Green. If missing, it will be Red. Some incomplete description will result in a Yellow indicator. The distance learning project report shows that the project has successfully completed Phase 0. Phase 1 (Fig. 5C) however has two Yellow’s. The statuses of Phases 0 and 1 are automatically rolled-up to the executive level, showing Phase 0 is Green and Phase 1 is Yellow (Fig. 5D). Thus, the overall project status is marked as a Yellow.

The rule for automatically rolling up the indicators is: Green of a phase requires that all its work items are Green; Yellow of any work item without any Red items will result in a Yellow phase indicator; otherwise the phase is Red, if any work item is Red.

Within his/her scope of responsibility, the managers may override the status but must document reasons for doing so. Notifications of overriding actions are sent to all related parties and upper management. Again, the top level of management has the ability of overriding any status indicator, giving reasons.

The example application is basically designed to implement the four concepts discussed in Section 2: mappability (what and why), accountability (who), interoperability (how) and controllability (where) for decision-making (when) at all levels of management with C<sup>3</sup>C. The URL for this example implementation is: http://www.csulb.edu/-tnnguyen/DM/. Demo scenario and instructions are available from a hotspot in the entry page. The set of Figs. 3–5 constitutes the minimum collection of windows/ screens that sufficiently illustrates the major capabilities in the case the above website is no longer available.

## 4. Discussions–implementation challenges

Central to the design and implementation of the model is the identification, definition and organization of indicators linking tasks and decision makers. This is the most time-consuming effort. It involves the participation of all key personnel. Once it is complete, the set of indicators can be changed to fit any new requirements.

From a standpoint of its implementation, there is a need for a database server. A semi-freeform Text Editor should also be provided. The upload and operations such as insert, delete or update for the indicator texts must be provided. Since the indicators are displayed in the web pages, HTML and/or XML style sheets can be used for the creation and maintenance of the work item panes in the appropriate windows. Any type of documents, artifacts and/or libraries must be supported. The web-based decision model must be implementable in a client/server environment in one enterprise and/or cross-enterprises. The model is extendable and scalable to handle any organizational structures and any software development life cycles (to be discussed in Section 5).

<table><tr><td>Project Report
Project Name: Distance Learning
Developer: T Nguyen</td></tr><tr><td>1. Business case
There are many web sites offering distance learning Most of them, if not
all, operate on a stabilizers service organization much as a separate,
independent institution. There is a need for integrating various distance
learning from different institutions so that the most suitable curriculum
can be available for prospective students. This allows the students to
choose different courses from different distance learning institutions to
serve the students&#x27; unique educational needs</td></tr><tr><td>2. Purpose
• Establish an integrated network of distance learning</td></tr><tr><td>3. Overview
This is a web-based distance learning application that takes advantage of
e-business integration technology. The application allows students to lab
their curriculum from different distance learning institutions that will best
suit their needs.</td></tr><tr><td>4. Scope
• Use service-oriented architecture with asynchronous
communications products for e-business integration among two
institution servers for illustration of concepts</td></tr><tr><td>5. Benefits and values
• Flexibility of tailoring course works for students
• Collaboration among distance learning institutions
• Maximize available program offerings</td></tr><tr><td>6. Project plans, estimation, schedule and deliverables (initial plan)
• (attached)</td></tr><tr><td>7. Choice of life cycle model
• Evolutionary prototyping model is selected</td></tr><tr><td>8. Risk identification and risk analysis
• E-business integration products: Probability=0.7, estimated
loss=4 weeks</td></tr></table>

![](/api/attachments/B52S94XE/fulltext/images/05998f638956fa2cfac23606246235dd0dc3c1c6ac49bd9946c6980c7525e544.jpg)  
(A)  
(B)

![](/api/attachments/B52S94XE/fulltext/images/bd9462be7b6a0434c8a877968195c913cc36261ffd140a84f132152a0ae37fc2.jpg)  
(C)

![](/api/attachments/B52S94XE/fulltext/images/ef1298e2f3e4efc050ea8b3ae339a6da1010385d324e0189dd36ffbb3996b38c.jpg)  
(D)  
Fig. 5. (A) Project report, (B) Phase 0 indicators-status, (C) Phase 1 indicators-status, (D) project status.

A more complete list of capabilities for the decision model is summarized below (some of these are not yet however implemented).

 Customized view for different responsible authority. A user, depending upon his/her position in the organization is presented with a view of only projects she/he is responsible for. For example, an executive will see all projects that s/he is sponsoring. A project manager will see only his/her own project. The technical manager or technical leader oversees the development of his/her project. The professionals are responsible for their document and artifact. The higher the position in the organization, the broader and the coarser the associated view.

 On-line submission of documents, reports or artifacts with a complete editing capability. These can be conceptualization documents such as requirements definitions, design specifications, review reports, etc., and/or implementation libraries such as source codes which can be linked to for display and/or examination.

 On-line approval and control of process by virtual meetings. Physical meetings for managing the projects can be minimized as the online application allows timely reporting and action to be taken.

 Access and action control by appropriate management level. Security and authentication can be added.

 Automatic roll-up status and drill-down details. This was shown in details in the previous section.

 Monitoring of deliverables, quality assurance and quality control implementation. The use of completeness, correctness, consistency and compliance at any management and technical levels help identify errors and defects in solution planning, estimation, sizing, scheduling in all phases of development cycle from conceptualization to realization as well as monitoring of deliverables.

 Policy-driven capability. Since policy exists everywhere in an enterprise, policy needs be incorporated into the indicator texts and their metrics.

![](/api/attachments/B52S94XE/fulltext/images/88b8a747853fe1352a5bfa2aa24c5078c496ee5e2a1e5cf8e0235a5b7043a0bb.jpg)  
Fig. 6. Extensible concepts.

 Status override function with required (undeletable) justification. As discussed in the previous section, this also allows the avoidance of conflict of authority.

 Reports on outstanding items (status, schedules, issues, actions). These reports can be automatically published with and without notifications to all personnel parties involved. They can be generated and separated by project, owners and other types of grouping.

## 5. Implications and conclusions

## 5.1. Flexibility, extensibility and scalability of the model to address cost and other dimensions

The decision model is task/activity and timeoriented. It can be extended to cover cost and other dimensions, e.g. resource dimension (see Fig. 6).

Production of a software product consumes activities, and thus resources, which must be allocated. The status of the activity completion at each milestone (or mini-milestones) of the software development phases such as feasibility, requirements, etc., can also be expressed by indicators. They can be related to task/ schedule, cost, etc. Again, they are goal-directed. The resources consumed in each activity are reported by the people carrying out the activities (e.g. time cards, travel expenses, etc.). Thus, the set of all indicators covering all dimensions of the project become meaningful for decision-making.

The model can be extended to cover a set of dimensions as illustrated in an extended and scalable decision model of Fig. 7. The 3-D rectangular box in the middle of Fig. 7 represents the scope and dimensions (not necessary orthogonal) of cost, time and resources. The software development effort is now represented by the diagonal, thicker line, from an initial inception (at the origin) to the other end indicating the completion of the software product.

The left hand side shows the activities of software development mapped to the stages of an activity-based costing (ABC) scheme [12,23,41,51,52], similar to those of Fichman and Kemerer [17]. This mapping involves the determination of cost elements and cost drivers in the ABC stage 1, and the determination of cost objects in its stage 2 [54]. The performance of each cost object is indicated by a set of relevant indicators, which are user-defined (e.g. by accounting professionals) and again goal-directed.

The indicators express the status of the relevant performance of each and every ABC activity in terms of indicator status, again using a Red, Yellow and Green measure whose criteria may be a threshold, a range of values or otherwise. Again, the status is automatically rolled up to the highest executive sponsoring, championing and/or responsible for the intended products (or services). Thus, the organization and decision makers are mappable to this activitybased costing scheme.

With more dimensions added, the decision model becomes a hypercube. Each dimension is an independent variable that is mapped to a task/activity structure to which the decision makers within the organization is also mapped.

## 5.2. Shortfalls

One may expect that the structure of the indicators is very much similar to that of the enterprise organization and the task organization to which it is mapped. While it is capable of providing the intended information and capabilities, it hides critical path information. The model is event-driven and aggregate event-driven. It is difficult to depict a global view of the critical path, which is also crucial to the decision makers. Thus, it has to be used in conjunction with other tools that will show the critical path.

![](/api/attachments/B52S94XE/fulltext/images/ceed1027b791a293cce4ef204f4e3f84a5ceecff72c9a872e920d675cf37387e.jpg)  
Fig. 7. Activity-based extension model for managing software development projects.

## 6. Conclusions

The decision model described here offers the software development organization a quality-assured, decision-assisted management scheme with high practicality, simplicity and flexibility through the use of a collection of goal-directed indicators. They have a direct relationship to metrics and quality of process, deliverables, resources supporting them and their environment. The organization may make use of any existing measurement techniques and metrics associated with them, and any decision-making schemes. The metrics serve as keys to severity level for each indicator.

The model works well with any software process frameworks (e.g. CMMI [9]) or processes, simple or complex, traditional or e-business-driven and software/system development from simple (in-house) to complex such as Homeland Security [14,22] or FCS. Furthermore, by focusing on accountability and interprocess activities, greater control and decision-making are possible at different levels of granularity while allowing quality and risk management, and continuous process improvement globally or locally.

## Acknowledgements

The author wishes to express his special thanks to Professor E. Sibley for the extensive reviewing and editing, and the anonymous reviewers for their extremely valuable comments. Thanks also go to Quoc Sung DucAm for his proofreading the final version of the article.

## References

[1] Army Transformation Roadmap, http://www.army.mil/ 2003TransformationRoadmap, 2003.

[2] R.L. Ackoff, Strategy, Systems Practice 3(4), 1990, pp. 521– 524.

[3] Adept, Stage Gate Product Development Redesign for Speed, Efficiency and Strategic Impact, http://www.adept-plm.com/ Stage-gate\_Redesign.htm, 2003.

[4] American National Standard, Quality Systems—Model for Quality Assurance in Design, Development, Production, Installation and Servicing, American Society for Quality Con trol, ANSI/ASQC Q9001, 1994.

[5] M. Barbacci, M.H. Klein, T.A. Longstaff, C.B. Weinstock. Quality Attributes, Technical Report, CMU/SEI-95-TR-021, 1995.

[6] B.W. Boehm, Software risk management: principles and practices, IEEE Software 8(1), 1991, pp. 32–41.

[7] B.W. Boehm, Software Economics, Prentice Hall, 1981.

[8] R. Chillarese, Software Testing Best Practices, IBM Research, TR RC 21457, http://www.chillarege.com/authwork/Testing-BestPractice.pdf, 1999.

[9] M.B. Chrissis, M. Conrad, S. Shrum, CMMI: Guidelines for Process Integration and Product Improvement, Addison-Wesley, 2003.

[10] C4ISR Architecture Framework V2, http://www.afcea.org/ education/courses/archfwk2.pdf, 1997.

[11] S. Chulani, B. Boehm, C. Abts, Software Development Cost Estimation Approaches, Annals of Software Engineering, 2000.

[12] J. Chutchian-Ferranti, Activity-Based Costing. Computerworld, August, 1999.

[13] DoD, DoD Architecture Framework, vol. 1, http://www.defenselink.mil/nii/doc/DoDAF\_v1\_Volume\_I.pdf, 2003.

[14] W.F. Dawson, Homeland Security Information Sharing Architecture, http://www.dtic.mil/ndia/2003interop/Lunch.pdf, 2003.

[15] R. Fairley, Risk management for software projects, IEEE Software 11(3), 1994, pp. 57–67.

[16] P.H. Feiler, R. Smeaton, Managing Development of Very Large Systems: Implications for Integrated Environment Architecture, Technical Report, CMU/SEI-88-TR-11, 1988.

[17] R.G. Fichman, C.F. Kemerer, Activity-Based Management of Component-Based Software Development, online, accessed on November, 2003.

[18] W.A. Florac, A.D. Carleton, Measuring the Software Process: Statistical Process Control for Software Process Improvement, Allison-Wesley, 1999.

[19] T.L. Fox, J.W. Spence, An examination of the decision styles of project managers: evidence of significant diversity, Information & Management 36(December (6)), 1999, pp. 313–320.

[20] Future Combat System, http://www.globalsecurity.org/military/systems/ground/fcs.htm.

[21] GAO, Defense Acquisitions The Army’s Future Combat Systems’ Features, Risks and Alternatives, GAO-04-635T, 2004.

[22] GAO Homeland Security, Information Sharing Responsibilities, Challenges and Key Management Issues, GAO-03-715T, 2003.

[23] A. Gunasekaran, H.B. Marri, Y.Y. Yusuf, Application of activity-based costing: some case experiences, Managerial Auditing Journal 14(6), 1999, pp. 286–293.

[24] H.W. Gunther, WAS Development Best Practices for Performance and Scalability, http://www-3.ibm.com/software/webservers/appserv/ws\_bestpractices.pdf, 2000.

[25] B. Hailpern, P. Santhanam, Software Debugging, Testing and Verification, IBM System Journal 41(February (1)), 2002, pp. 4–12.

[26] M. Hamblen, Keeping IT Projects on Tract, Computer world, online, http://www.computerworld.com/printthis/ 2002/0,4814, 67690,00.html, 2002.

[27] G.W. Hopple, Decision aiding dangers: the law of the hammer and other maxims, IEEE Transactions on Systems, Man, and Cybernetics SMC-16(November/December (6)), 1986, pp. 948–963.

[28] J.J. Jiang, G. Klein, H.-G. Hwang, J. Huang, S.-Y. Hung, An Exploration of the relationship between software development process maturity and project performance, Information & Management 41(3), 2004, pp. 279–288.

[29] L.R. Levine, B.J. Pries-Heje, B. Ramesh, S. Salughter, Discovery Colloquium: Quality Software Development at Internet Speed, online, CMU/SEI-2002-TR-020 ADA406781. http:// www.sei.cmu.edu/publications/documents/02.reports/ 02tr020.html, 2002.

[30] J. Lubelczyk, A. Parra, Managing the software development process, in: N. Manset, C. Veillet, D. Crabtree (Eds.), ASP Conference Series on Astronomical Data Analysis Software and Systems IX, vol. 216, 2000, p. 3.

[31] M. Mawdesley, A Hierarchical Approach to the Management of Construction Project Risk, http://www.civeng.nottingham.ac.uk/s%26c/peterdawson.html, 1992.

[32] D.R. McAndrew, Establishing a Software Measurement Process, CMU/SEI-93-TR-16 ESC TR, 1993, pp. 93–193.

[33] J. McCarthy, Dynamics of Software Development, Microsoft Press, 1995.

[34] S. McConnell, Rapid Development, Microsoft Press, 1996.

[35] S. McConnell, The Art, Science and Engineering of Software Development, IEEE Software—Best Practices, January/February, 1998.

[36] J.R. Meredith, Project Management: A Managerial Approach, fifth ed., John Wiley & Sons, 2003.

[37] Microsoft, Software Development Models Overview, http:// www.microsoft.com/resources/sharedsource/Articles/SoftwareDevelopmentModelsOverview.mspx, 2003.

[38] R. Moore, D. Ace, The phase-gate development process takes to the web, in: Proceedings of the Fifth European Project Management Conference, PMI Europe 2002, Cannes France, June, 2002.

[39] U. Nikula, Reason to Invest in RE and Key Problems in the Task, http://www.cs.joensuu.fi/pages/saja/tSoft/dokumentit/ BaREJustification20021015.pdf, 2002.

[40] T.N. Nguyen, A quality-assured hierarchical model for solutions development management, Proceeding of IEEE Systems, Man and Cybernetics, Tokyo, Japan, 1999.

[41] G. Ooi, C. Soh, Developing an activity-based costing approach for system development and implementation, in: Database for Advances in Information Systems, 2003.

[42] J.S. Osmundson, J.B. Micahel, M.J. Machniak, M.A. Grossman, Quality management metrics for software development, Information & Management 40(8), 2003, pp. 799–812.

[43] R.E. Park, W.B. Goethert, W.A. Florac, Goal-Driven Software Measurement, CMU/SEI-96-HB-002, 1996.

[44] R.S. Pressman. Software Engineering Resources, http:// www.rspa.com/spi/, 2003.

[45] Primavera, Six Dimensions of Enterprise Project Management, http://www.primavera.com/aboutus/sd01.html, 2003.

[46] S. Purba, B. Shah, How to Manage a Successful Software Project: with Microsoft Project 2000, second ed., John Wiley & Sons, 2000.

[47] L.H. Putnam, W. Meyers, Build in Quality, http:// www.qsm.com/quality1.pdf, 2001.

[48] Rational Software, http://www.rational.com/media/whitepapers/rup\_bestpractices.pdf, 2001.

[49] Software Risk Management Bibliography, http://www.ida.- liu.se/labs/aslab/people/joaka/risk\_bib.html.

[50] SoSCOE, http://www.army.mil/fcs/factfiles/network-soscoe.html, 2002.

[51] N. Roztocki, Introduction to Activity-Based Costing, University of Pittsburg, 2003 in: http://www.pitt.edu/-roztocki/ abc/abctutor/index.htm.

[52] N. Roztocki, S. Schultz, Adoption and Implementation of Activity-Based Costing: A Web-Based Survey, online, accessed October 12, 2003.

[53] R. Srinivasan, Planning is the Key in Software Development, IT People evolve, http://www.expressitpeople.com/20020218/ management4.shtml, 2002.

[54] J. Trussel, L.N. Bitner, Strategic Cost Management: an activity-based management approach, Management Decision 36(7), 1998, pp. 441–447.

[55] StartWright, Project Management Tools, http://www.start wright.com/project1.htm, 2002.

[56] State Services Commission and The Treasury, Guidelines for Managing and Monitoring Major IT Projects, http:// www.ssc.govt.nz/ITguidelines, 2001.

[57] K.R.J. White, Measuring and Managing Success, IT Project Metrics, Expert Series, 2003.

[58] K.E. Wiegers, Software Requirements, Microsoft Press, 1999.

[59] C.E. Williams, Software testing and the UML, in: Proceedings of the International Symposium on Software Reliability Engineering, Boca Raton, November, 1999.

![](/api/attachments/B52S94XE/fulltext/images/ce02fb8433d6c5205c03b7e2c55fb97d9b640592eeef8c2529355071abe35cf8.jpg)  
Thang N. Nguyen teaches undergraduate and graduate information systems courses at California State University Long Beach, College of Business Administration. He has earned a BS in electrical engineering from Laval University, an MS in information and computer science from Georgia Institute of Technology and a PhD in information technology and engineering from George Mason Univer-

sity. He has served Candle Corporation, IBM Corporation, Litton Computer Services and other firms in various capacities in software development, IT management and education/training. His research interests include intelligent robotics, intelligent and autonomous software, symbolic–numeric integration, biological computing, ebusiness application integration and business–IT integration.
