---
otero_id: 24670
otero_key: "NXC4QGTA"
title: "Using Group Support Systems and Joint Application Development for Requirements Specification"
authors: "Yihwa Irene Liou; Minder Chen"
year: "1993"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1993.11518009"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Using Group Support Systems and Joint Application Development for Requirements Specification

Yihwa Irene Liou & Minder Chen

To cite this article: Yihwa Irene Liou & Minder Chen (1993) Using Group Support Systems and Joint Application Development for Requirements Specification, Journal of Management Information Systems, 10:3, 25-41, DOI: 10.1080/07421222.1993.11518009

To link to this article: https://doi.org/10.1080/07421222.1993.11518009

![](/api/attachments/NXC4QGTA/fulltext/images/ce683de6097ffde4b6f86f585bd909697b0cf607695af87e2888426408ccbd3c.jpg)

Published online: 15 Dec 2015.

![](/api/attachments/NXC4QGTA/fulltext/images/5c0ed8ed18dad6e56b222712e682bec930a139150f03d1933bda3071b855ba53.jpg)

Submit your article to this journal ↗

![](/api/attachments/NXC4QGTA/fulltext/images/e5c04c9260b2eb8017da7dd48a9843917b6173850d109d6104c6ec0180e4e315.jpg)

View related articles ↗

![](/api/attachments/NXC4QGTA/fulltext/images/491374b822bb27d6b12e052bdece324e9411529806a3a5f69996d5f3190f9605.jpg)

Citing articles: 15 View citing articles ↗

# Using Group Support Systems and Joint Application Development for Requirements Specification

YIHWA IRENE LIOU AND MINDER CHEN

YIHWA IRENE LIOU is Assistant Professor of MIS at the University of Baltimore. She holds a B.A. in philosophy from the National Taiwan University, an M.L.S. from the University of Southern Mississippi, and an M.S. and a Ph.D. from the University of Arizona in management information systems. Her current research interests include design, use, and the impact of group support systems, joint application design, computer-aided software engineering, business applications of expert systems, and knowledge acquisition techniques. Her published work has appeared in Journal of Management Information Systems, Journal of Organizational Computing, Journal of Information Technology Management, Information & Management, Knowledge Acquisition, Expert Systems with Applications, and Data Base. She is a member of the AAAI, ACM, IEEE, TIMS, and DSI.

MINDER CHEN received a B.S. in electrical engineering from the National Taiwan University, an M.B.A. from the National Chiao Tung University, and a Ph.D. in management information systems from the University of Arizona. He is currently Assistant Professor of MIS at George Mason University. His primary research interests are computer-aided software engineering, collaboration technologies, business reengineering, and expert systems development. He has published papers in Journal of Management Information Systems, Data Base, Journal of Organizational Computing, Expert Systems with Applications, IEEE Transactions on Knowledge and Data Engineering, Journal of Small Group Research, and IEEE Software. He is the co-guest editor of the March 1992 IEEE Software special issue on integrated CASE, and CASE minitrack coordinator of Hawaii International Conference on Systems Sciences for the last few years. He is a member of the IEEE, ACM, and TIMS.

ABSTRACT: The increasing use of integrated computer-aided software engineering (CASE) environments is shifting the bottleneck of systems development from physical design and coding to upstream activities, particularly requirements specification. This paper explores the use of group support systems (GSS) and joint application development (JAD) in the context of CASE environments to facilitate the requirements specification process. We first examine the relevance of GSS, JAD, and CASE to requirements specification. We then propose an integrated framework that is augmented by a domain-analysis methodology. Results of a pilot study that evaluated two process models using tools of a GSS, GroupSystems™, for requirements specification are discussed.

Acknowledgment: This study was partially supported by a research grant from the David D. Lattanze Center for Executive Studies in Information Systems, Loyola College in Maryland..

KEY WORDS AND PHRASES: computer-aided software engineering, group decision support systems, group support systems, joint application design, joint application development, requirements specification.

## 1. Introduction

THE EMPHASIS OF SYSTEMS DEVELOPMENT IS SHIFTING to the front end of the systems development life cycle $[12, 20]$ . One of the major reasons is that errors made in the early stages of information systems development are costly. Most errors found in the systems building process can be traced back to incorrect system requirements or misinterpretation of the correct ones. The cost of correcting erroneous requirements of a system in its operation stage is at least a hundred times greater than correcting them at the requirements definition stage $[3]$ . The advent of application generators and code generators greatly reduces the programming effort required for building information systems. The increasing use of integrated computer-aided software engineering (CASE) environments is shifting the “bottleneck” of systems development from physical design and coding to upstream activities, particularly requirements specification. Therefore, the challenge of systems development has become “building the right system by defining the right one” instead of “building the system right.”

Many people are involved in developing a complicated software project because no one possesses all the knowledge required. Domain-specific knowledge about an application and its environment as well as technical knowledge about systems development have to be incorporated into a cohesive framework to create a good software requirements specification (SRS) [1]. The elicitation of requirements is a collaborative effort among managers, users, and system analysts. One of the major factors that causes misunderstandings in the systems development process is the complexity of the communication and decision making among members of a project team [5], and communication breakdowns are most likely to occur when requirements are elicited from a heterogeneous group.

Traditionally, the requirements specification process is conducted by systems analysts through a series of one-on-one interviews with users and/or managers. However, difficulties in conducting serial interviews with users/managers individually to identify system requirements include: (1) it is a lengthy and time-consuming process; (2) users and managers may have conflicting definitions and perceptions of a system's problems and objectives. These conflicts must be resolved by individual members through several iterations of follow-up interviews. Sometimes, as when one person misinterprets another's statements and assumes that they are in agreement, a conflict may not even be recognized to exist. (3) The integration of users' views into a coherent set of system requirements is particularly difficult because of the diversity of users' backgrounds and differing usage of terminology.

Since the development of information systems has long been recognized as a joint effort among systems developers, users, and managers, the need to support collaborative activities during the application development process is evident. Though CASE tools have been used in various stages during the systems development life cycle to improve software productivity, there is no direct support in most CASE tools for direct interactions among project team members. However, group support systems (GSS), an emerging technology designed to facilitate human interactions, may be used separately or in combination with joint application development (JAD), a facilitated systems development methodology, to support collaboration among project team members in the applications development process. The purpose of this article is to explore ways to integrate GSS and JAD with CASE tools to improve the effectiveness of requirements specification. Next, we discuss enabling technologies for requirements specification.

## 2. Enabling Technologies for Requirements Specification

SEVERAL TECHNOLOGIES ARE AVAILABLE FOR SUPPORTING THE REQUIREMENTS specification process. CASE tools designed to support the system development life cycle include analysis, design, code generation, and documentation. JAD may be considered as a facilitation method for supporting systems development meetings. GSS address the need for an electronic meeting environment that provides support for collaboration in the systems development process. The current status of these technologies and their relevance to requirements specification are discussed in this section.

## 2.1. Computer-Aided Software Engineering

Upper CASE tools are designed to support systems planning, analysis and logical design $[10]$ . They are used in the application of various structured techniques including data modeling using entity relationship diagrams, process modeling using data flow diagrams, and structured design using structure charts. Each structured technique supports the modeling of only one or two aspects of a system, however. Structured texts, structured graphics, and matrices are the representation formats used in most CASE products to present the specification of a target system. Structured graphics are used extensively to support the graphic notations employed by structured techniques while structured texts are very useful in listing detailed information about a system. Matrices can be used very effectively to show binary relationships between two types of entities used in information systems planning. Additional functions provided by several CASE tools are requirements traceability, consistency and completeness checking, and project repository. It is assumed by CASE vendors that systems analysts are able to elicit requirements from users in informal formats and then to translate and specify those requirements using the formal specification languages supported by CASE tools.

Most existing CASE environments, however, do not explicitly provide a mechanism to facilitate software project meetings $[10]$ . They do provide version and configuration control mechanisms via check-in and check-out procedures that allow several systems developers working on the same project to share information stored in a repository. However, these mechanisms are only used by systems developers and are designed to prevent them from directly interacting with each other. Support for requirements elicitation (particularly in a group meeting) is a critical functionality missing from existing CASE research and products [9]. Davy [13, p. 15] stated that “current implementations of CASE tool technology encourage an individual approach to work, even if they provide multi-user capability. However, analysts improve the quality of their work by discussing and reviewing it with colleagues. CASE tools are useful, but they are no substitute for interactive group discussion. Until more responsive interfaces are available we will only be able to make limited use of them.”

There is increasing use of JAD-like facilitated meetings for building systems using CASE tools. JAD workshops provide an interactive group discussion mechanism for project team members to define system requirements. Increasingly, CASE tools are used directly during JAD sessions at the back end to document the information generated during these sessions. The essentials of JAD are explained in the next section.

## 2.2. Joint Application Development (JAD)

While the need to support collaborative requirements elicitation exists, there are very few systems development methodologies that directly support group interactions in face-to-face meetings. Joint application development (JAD), also known as joint application design, a group-oriented analysis and design methodology originally developed by IBM in 1977, is an exception $[2, 6, 34]$ . This methodology features an intensive structured workshop where participating end users are assisted by information systems personnel and guided by an experienced session leader. The leader has previously interviewed managers and users to define the scope and objectives of the project and determine who should be participants of a JAD workshop.

A JAD workshop usually lasts for three to five days and consists of many sessions. It is usually initiated by an executive sponsor who is the owner of the system project and who also is responsible for resolving major conflicts, if any, during a JAD session. Typically, JAD session leaders use overhead projectors to present information collected during the JAD preparation phase and use flip charts and magnetic cards to capture informal requirements generated by the group. Scribes translate and document the requirements captured in the session, using standardized forms. Many organizations recently have started using prototyping tools or CASE tools to support JAD workshops $[4, 6, 24]$ .

The success of a JAD workshop relies mainly on the skills of the session leader in managing processes, applying structured techniques to facilitate the group's deriving requirements, and handling the group's dynamics. Documents generated from the workshop include screen and report formats, definitions of entities and data elements, a description of work flows, and specification of systems functions. JAD not only provides an environment for more thorough recall of key requirements but also encompasses perspectives from different functional areas and from users and managers [33].

In summary, the essentials of JAD are (1) a focused workshop facilitated by JAD leaders and scribes, (2) users' participation and management's commitment, (3) the development of shared requirements and design specifications, (4) application of structured procedures and methods, and (5) an accelerated approach to meeting a specific time frame. Moreover, JAD provides the following benefits: (1) reduced time and cost in requirements elicitation, (2) improved communication among project team members, (3) provision of appropriate channels to resolve conflicts and build consensus, and (4) improved quality of workshop outcomes, such as flow charts, screen designs, and systems specifications.

There are some problems with the traditional JAD, however. First, all JAD participants may not be equally involved. Only the comments of the most vocal may be captured. Second, analysts are limited in their ability to judge group consensus in real time. Third, the products of the workshop have to be compiled and documented manually which can be very time-consuming. These problems would largely be resolved by using GSS during facilitated JAD sessions. First, participation would be encouraged and enhanced with the anonymity feature of GSS, at the same time the communication bandwidth is expanded by adding an electronic communication channel to the verbal communication channel. Second, evaluation tools such as rating and voting can be used to assess group consensus in a timely fashion. Third, the discussions and deliverables of the workshop can be captured by GSS. Compilation and documentation become unnecessary.

## 2.3. Group Support Systems (GSS)

Group support systems (GSS) are integrated computer and communication systems that support group work. Other common terms referring to the same concept include, but are not limited to, groupware, group decision support systems, and collaboration technology. GSS facilitate communications, coordination, and decision making by structuring the processes and contents of teamwork. The goals of a GSS are to reduce the process loss associated with disorganized activity, member dominance, social pressure, inhibition of expression, and other difficulties commonly encountered in groups and, at the same time, to increase the efficiency and quality of the end results $[14, 28, 31]$ . Research findings on the impacts of GSS on groups have shown that the use of a GSS increases task-oriented communication $[16, 31]$ , the quality of decisions, and group members' satisfaction and confidence $[15]$ .

There is an increasing trend toward using computer and communication systems to support such group techniques as brainstorming. Recent developments in CSCW and GDSS are rooted in earlier efforts to support collaborative work in software development $[14, 18]$ . GSS have been proven useful in such tasks as idea generation $[25, 26]$ , business planning $[15]$ , crisis management $[27]$ , and knowledge acquisition $[22, 23]$ . GSS technologies make group meetings more productive by supporting rapid access to information and message exchanges, by providing better group memory management and feedback, and by facilitating more structured group interaction processes $[29]$ . Groups supported by GSS technologies are able to use more complex group modeling tools to create and explore a wider range of alternatives $[17]$ . In addition, using a GSS often increases participation, reduces meeting time, and improves the quality of meeting results, especially when large groups are involved in complicated tasks [14, 15].

Examples of commercialized GSS include Ventana's GroupSystems V $^{TM}$ , Lotus Notes $^{TM}$ , and VisionQuest $^{TM}$ . GroupSystems V $^{TM}$ provides a set of tools to facilitate electronic meetings, same time/place or different time/place. These tools include Electronic Brainstorming, Idea Organization, Voting, Group Matrix, GroupOutliner, Team Graphic, and GroupWriter [19]. Lotus Notes $^{TM}$ is a group communication product that allows people to create, assemble, organize, distribute, and access shared information. Notes $^{TM}$ is appropriate for the development of document-oriented and mail-enabled applications, such as customer tracking and group discussion [30]. VisionQuest $^{TM}$ provides tools organized under an executable agenda to facilitate face-to-face as well as dispersed group meetings [32]. These tools include Brainwriting, Comment Cards, Rating, Ranking, and Scoring. Most GSS are designed to provide collaboration support to business teams in communication, coordination, planning, decision making, project management, and document preparation. In addition, they have been used to elicit requirements from project team members and acquire knowledge from experts [22].

## 3. Using GSS to Support JAD and CASE

RESEARCH RESULTS INDICATING POSITIVE OUTCOMES of using GSS for systems development activities have made it appear that an ideal approach would be to employ the JAD methodology with appropriate GSS tools to support requirements elicitation. Therefore, equal participation may be achieved, group consensus may be assessed in real time, and semiformal specifications may be generated in group meetings and recorded electronically [21]. Moreover, results from requirements elicitation sessions can be exported and transformed into specific formats supported by existing CASE tools to speed up the systems development process.

## 3.1. A Framework

The trend toward user involvement in systems development, particularly in requirements analysis and specification, has been accelerated by the advent of CASE tools and the use of prototyping in systems building. Requirements elicitation calls for intensive interactions among system developers and users in face-to-face meetings in the software development process [11]. Systems developers are better able to work closely with users in defining system requirements when it is possible to show them CASE tools-generated graphical models that represent the system's functionality and structures.

Traditional serial requirements elicitation techniques such as interviews, questionnaires, and observations are appropriate only for eliciting individual views and requirements of a system from users. It is very difficult to apply these techniques to a large-scale project due to miscommunications among project members and the amount of time required by the conflict resolution process. Group techniques can be used to facilitate the requirements elicitation from groups, however. Structured Brainstorming

Systems [20] which has been implemented in GroupSystems™ [28], is one example of the use of such techniques.

An ideal approach may be to employ GSS in JAD sessions to accelerate the requirements elicitation. Figure 1 depicts an overview of the integration of GSS and JAD into a CASE environment. Systems specifications, screen designs, and flow charts generated during the GSS-supported JAD sessions can then be used as inputs to CASE tools for formal systems specifications, code generation, and documentation.

Many GSS applications have consistently fallen short of expectations, and conflicting reports of the usefulness of GSS to facilitate various group activities call attention to the importance of adopting a methodological approach to using GSS $[29]$ . The success of GSS may depend on the nature of the application domains in which they are introduced and the methodologies employed in using them. The existence of a methodology for guiding the use of GSS possibly could have prevented earlier possible misuse and abuse of GSS. Based on our experiences in using GSS in knowledge elicitation, systems analysis and design, and business planning, we have developed a domain analysis methodology (DAM), which is independent of any specific GSS, to support requirement elicitation using GSS, JAD, and CASE tools.

## 3.2. A Domain Analysis Methodology

A methodology consists of a predetermined set of tasks grouped into stages and supported by various techniques, methods, and tools (figure 2). The domain analysis methodology (DAM) is composed of a set of methods and tools to assist users in analyzing the domain and to match appropriate group support tools to the processes of various group activities. In essence, this methodology is designed to make it possible to examine the problem faced by a group in such a way that GSS can be used appropriately to facilitate group meetings. DAM has been developed by incorporating knowledge engineering and software engineering principles and techniques to support the group process of information systems analysis and design. Requirements elicitation can be viewed as knowledge acquisition activities in which participants contribute individual understandings of the application domain of an information system. A requirements engineer should be designated to manage the requirements elicitation process using DAM. The six stages are described below.

1. Scope the project. The primary tasks involve defining project scope and identifying stakeholders. DAM is user-driven. The identification of systems problems is the first step. In addition, stakeholders (i.e., individuals, organization units, and outside entities) who have stakes and different aspects of problem domain should be identified. Requirements engineers should work with several key persons and experts in the domain to define the scope of the project and to determine schedule and allocate resources. The results of this stage should be: a well-defined project scope, a list of stakeholders, a preliminary description of the problem domain, and a temporary project schedule and resources allocation plan.

2. Determine requirements specification process. The procedure for defining the requirements specification process involves: (1) identifying the requirements to be acquired and their sources and (2) selecting specification methods for representing requirements. Requirements engineers should use the concepts, languages, and terminologies from the application domain as much as possible to specify the requirements. The outputs of this stage should include a defined requirements specification process and selected methods to represent specifications.

![](/api/attachments/NXC4QGTA/fulltext/images/76da97067e5c91249e015c4a33edea739ac658ef1f6d5786009249e5f088fb0d.jpg)  
Figure 1. A Framework for Integrating JAD, CASE, and GSS

3. Design a group process model to elicit requirements. A group process model designed at this stage would elicit requirements from various users and experts. Group tasks should be determined and sequenced. The interactions among project team members and the underlying group requirements elicitation process should be determined. Group communications and interactions should be encouraged so that group synergy and consensus can emerge in the group requirements elicitation process. A sequence of group sessions should be designed to elicit and synthesize requirements acquired from each participant. Selection of participants and definition of capacity in which each of them will serve at each session should be defined at this point. The desired patterns of interactions should be specified, including the specific structures of the messages to be used by participants in information exchange, the mechanism for sharing information about the system specified, conflict resolution strategies, the timing and constraints of interaction, and the media to be used for communication.

4. Select and configure a GSS and CASE to support the process model. A set of group techniques and group support tools to facilitate appropriate group interactions in the process model is defined in this stage. CASE tools should also be chosen and configured to support the selected specification methods and the group activities. A domain-specific group process model that consists of a sequence of group activities supported by a set of group support tools to facilitate the acquisition of requirements should now exist. Information used by and generated from tools can also be specified. Other preparations for the JAD sessions should be made at this stage.

![](/api/attachments/NXC4QGTA/fulltext/images/52d5f246fa08bad3d10fe89d22723825799339782e96eee949f38512a8d90492.jpg)  
Figure 2. Six Stages of Domain Analysis Methodology

5. Facilitate GSS-supported JAD sessions. The next stage in DAM would be to conduct group sessions based on the specified group process model. The appropriately configured GSS would be used to facilitate group interactions, to capture semi-structured requirements from nontechnical users and managers. Group dynamics in the process should be monitored so that unexpected individual and group responses can be managed promptly.

6. Conclude JAD sessions. To conclude JAD sessions, the semiformal requirements acquired from the requirements specification sessions should be converted into formal user and engineering requirements specifications, using modeling techniques supported by existing CASE tools. Use of either the existing import/export facilities in GSS and CASE or customized software bridges should make the conversion process much easier. Because information captured in CASE tools can be represented in various formats and analyzed for completeness and consistency, the results could be fed back to the participants for the refinement of the requirements. The finalized specifications should then be evaluated by the requirements engineers, signed off by the participants, and stored in the CASE repository for use by other downstream activities in the systems development life cycle.

DAM has been used to customize GSS to support crisis planning [27], group knowledge acquisition for an expert system [22, 23], and organizational modeling [8]. It has been proven to be useful. In DAM, GSS are used to support requirements elicitation in facilitated group sessions for systems analysis and design. The methodology can improve the effectiveness of traditional JAD sessions, particularly in information strategy planning, business area analysis, and conceptual systems design.

The session results can be easily converted into CASE Data Interchange Format (CDIF) [7] or proprietary formats for specific CASE tools in order to import the session results directly into CASE tools. Therefore, the nature of the scribe's job in GSS-supported sessions is changing from recording information to operating CASE tools and GSS tools. JAD facilitators always have been in short supply because they need to have skills in many different disciplines. With the support of GSS, the cognitive burden of JAD facilitators to manage group dynamics is reduced. Facilitators need less knowledge about requirements specification processes or methods because the methods are embedded in the reusable GSS-supported group requirements specification process models. Less skillful and inexperienced JAD facilitators will be able to run GSS-supported JAD sessions successfully.

## 4. An Assessment of the Integrated Approach: A Pilot Study

TWO ASPECTS OF THE INTEGRATED APPROACH WERE EVALUATED in a pilot study. One pertains to the sequencing of steps proposed in the DAM and the other pertains to the process models used to conduct requirements elicitation meetings.

## 4.1. Research Design

The primary objectives of the study reported here were (1) to validate steps and actions specified in the domain analysis methodology in a real project, and (2) to assess comparative task effectiveness, satisfaction with the meeting process, satisfaction with the GSS, and group cohesiveness of two process models utilizing various group tools. The independent variable studied was the use of different tools in the process model. The generic process included four major steps: (1) generating and identifying system functionalities, (2) prioritizing functionalities, (3) verbally discussing the prioritized list to gain group consensus, and (4) expanding detail description and specifications on a few selected important functionalities (figure 3). Two specific process models were employed. Groups assigned to process model A used the Electronic Brainstorming tool while groups assigned to process model B utilized the Idea Organization tool for step 1. Both groups used the same tools: Voting and the GroupOutliner, for steps 2 and 4, respectively.

The dependent variables included task effectiveness, satisfaction with the meeting process, satisfaction with the GSS, and group cohesiveness. Task effectiveness was measured by the quality, manner, content, and outcome of the discussion. Satisfaction with the meeting process was measured by participants' perceptions of its efficiency, coordination, satisfaction, and effectiveness. Satisfaction with the GSS was measured by participants' feelings about using GroupSystems™ during the meeting. Group cohesiveness was measured by how well members of the group felt they had worked together. Both pre- and postmeeting questionnaires were collected from participants. Times to complete the requirements specification session appeared to be very similar; groups assigned to process model A averaged 75 minutes while groups assigned to process model B averaged 70 minutes.

## 4.2. Subjects

Twenty-eight students from a graduate-level AI/expert systems class participated in this study in the spring semester of 1992 at the University of Baltimore. They were randomly assigned to seven groups of which three were assigned to process model A and four were assigned to process model B. Each participant played a dual role in this project: as a potential user of the system and as a system developer.

## 4.3. Task

The task was to identify functionalities of an expert student advising system. This was part of a group project assigned to the class to design and develop a prototype system using an expert system shell. Participants were given three weeks to accomplish the whole project. The requirements specification session for each group was scheduled to last two hours, and an additional meeting could be scheduled if necessary. No groups scheduled another group session.

![](/api/attachments/NXC4QGTA/fulltext/images/5dbca8cd2dadc795cd21bbabbc24725b541e7707486844a03033b695f153ddb5.jpg)  
Figure 3. Generic Process Model and Supporting Tools Used in the Study

## 4.4. Software

GroupSystems™ was used in the requirements specification sessions. Tools employed in the meetings included Electronic Brainstorming (EBS) (an idea generation tool), Idea Organization (an idea generation and consolidation tool), Voting (an evaluation tool), and GroupOutliner (a tool that uses a hierarchical topic tree to allow parallel discussion on multiple topics). Descriptions of the GroupSystems™ tools could be found in [14, 28]. The GSS laboratory was equipped with nine PC workstations in a U-shaped configuration, a projection system and a large public screen, and a high-speed laser printer.

## 4.5. Procedures

All 28 students were required to fill out a pretest questionnaire that collected demographic data and background information. Each group selected a specific time slot for holding its requirements specification meeting. The same facilitator provided facilitation for all seven groups.

In the beginning of each requirements elicitation meeting the facilitator welcomed the group and provided them with a brief introduction to the purpose of the meeting, described how a GSS works, and discussed what outcomes were expected. Then the facilitator paused for a minute or two to answer questions. During the idea generation phase, a question, “What functionalities do you think the expert student advising system should have?” was posted. “A” groups brainstormed on this question using EBS and then the facilitator assisted the group to consolidate ideas by activating the keyword feature to identify a list of functionalities. "B" groups followed the nominal group technique and used the Idea Organization tool to generate a private list of functionalities and then as a group went though a round-robin discussion submitting one idea at a time to come up with a recommended list of functionalities for further evaluation.

Both groups then moved on to prioritize the list of functionalities using the Voting tool according to the following instruction: "Rank the list of functionalities based on its importance to you as a user (student)." The voting results were then discussed and another iteration of discussion and voting could have taken place. However, no groups went through another round of discussion and voting. Once the prioritized list was generated and group consensus achieved, the GroupOutliner tool was used to elicit additional ideas with regard to each functionality.

The layout of the GroupOutliner tool is similar to a sideways tree diagram with the root being the expert student advising system, the first-level nodes being functionalities, and the second-level nodes of each functionality being input, process, and output derived from the functionality. The input node corresponded to “what information should be collected?” The process node identified the reasoning process and “what expertise is required?” The output node mainly provided answers to “what outcome is expected?—i.e., what does the system present to you?” Each member of the group filled out a posttest questionnaire after the requirements elicitation meeting. Before the group left the GSS laboratory, a copy of the meeting output was handed to each member. Upon completion of the whole project, each student was asked to fill out another survey indicating how well the group worked together.

## 4.6. Results

Demographic data about the subjects are summarized below. All 28 participants, 14 male and 14 female, were graduate students (24 in the M.S. in MIS program and 4 in the M.B.A. program). Their age distribution was as follows: 1 older than 50, 1 between 40 and 49, 9 between 30 and 39, and 17 between 20 and 29. Among them, 8 held full-time positions and 3 worked part-time. Seven others had work experience but were not currently employed. The average years of work experience among those with work experience was 3.6 years. Fourteen had work experience related to the development of information systems and 12 were involved in IS projects as systems analysts/designer, programmer, or project manager. Eleven had experience with a GSS and only one had experience with developing a rule-based expert system.

Differences between the two groups were insignificant in terms of task effectiveness, satisfaction with the meeting process, satisfaction with the GSS, and group cohesiveness, and both groups expressed positive feelings about their experience and recognized benefits of this approach (see Table 1). Both process models appeared to be effective in helping to complete the assigned task within a reasonable amount of time. It appeared that task effectiveness and satisfaction with the meeting process and group cohesiveness were highly correlated. Satisfaction with the meeting process was highly correlated with satisfaction with the GSS and group cohesiveness. Task effectiveness and satisfaction with the GSS also had a positive correlation (see Table 2).

Table 1 Descriptive Statistics of Dependent Variables

<table><tr><td rowspan="2">Dependent variables</td><td colspan="2">Process model A</td><td colspan="2">Process model B</td></tr><tr><td>Mean</td><td>Standard Dev.</td><td>Mean</td><td>Standard Dev.</td></tr><tr><td>Task effectiveness</td><td>5.35</td><td>0.55</td><td>5.39</td><td>0.66</td></tr><tr><td>Satisfaction with meeting process</td><td>5.47</td><td>0.47</td><td>5.2</td><td>0.64</td></tr><tr><td>Satisfaction with GSS</td><td>5.26</td><td>0.7</td><td>5.08</td><td>0.85</td></tr><tr><td>Group cohesiveness</td><td>4.93</td><td>0.44</td><td>4.9</td><td>0.18</td></tr></table>

Ratings are on a scale of 1-7 where 7 refers to positive expression and 1 means negative feeling.

Table 2 Pearson Correlation Coefficients

<table><tr><td></td><td>Task effectiveness</td><td>Satisfaction with meeting process</td><td>Satisfaction with GSS</td><td>Group cohesiveness</td></tr><tr><td>Task effectiveness</td><td>1.0</td><td>0.9161</td><td>0.7412</td><td>0.9515</td></tr><tr><td>Satisfaction with meeting process</td><td>0.9161</td><td>1.0</td><td>0.9231</td><td>0.9362</td></tr><tr><td>Satisfaction with GSS</td><td>0.7412</td><td>0.9231</td><td>1.0</td><td>0.8485</td></tr><tr><td>Group cohesiveness</td><td>0.9515</td><td>0.9362</td><td>0.8485</td><td>1.0</td></tr><tr><td colspan="5">*p&lt;0.05.</td></tr></table>

## 4.7. Observations

The use of the DAM assisted in the development of process models undertaken in this study. It appeared that it was most useful at the conceptual level to define scope, establish process models, and configure a GSS. In this study, an expert system shell instead of a traditional CASE tool was used in the system development process. The output generated in the requirements specification meeting provided a well-established foundation for the groups to move on, which saved a lot of time at the beginning of the systems development process. The groups not only identified important functionalities of the system, but also generated additional detailed design and implementation information.

Interviews with some group members revealed that the GSS-supported requirements elicitation meeting contributed to the success of design and implementation of the application. Several indicated that it would have taken them at least five times as much effort without the GSS sessions. A GSS such as GroupSystems™ allows users and managers to engage actively in the systems development process. They can jointly define, discuss, evaluate, and refine the systems specifications using the GSS. The systems analysts can then transform informal specifications into formal and graphical ones using CASE tools. The analysis function in CASE tools can be applied to the formal specifications to identify inconsistency and incompleteness. The requirements elicitation process described in this section can be generalized and then customized for many other application domains such as new products development and the development of new social programs.

## 5. Conclusions

MANY MAJOR INFORMATION SYSTEMS FAILURES HAVE BEEN CAUSED by inappropriate involvement of users and managers, resulting in incomplete or inconsistent requirements. Therefore, there is a growing interest in involving users in the systems development process, particularly in the planning and analysis phases where conceptual data and process models of an application or an enterprisewide information system are defined. Businesses are also interested in understanding their business processes and reengineering these processes in order to achieve dramatic quality improvement. Business engineering requires full participation of managers and reengineered business process models are the foundations of information systems developed to support them. We have proposed a framework to integrate GSS, JAD, and CASE to support requirements specification. Such an approach can reduce the need for a highly skillful JAD session leader, a kind of specialist who is always in short supply. The framework would also increase users' participation and satisfaction in the process.

Results of a pilot study have been presented. Further analysis and follow-up studies are underway to validate the effectiveness of the proposed approach and using empirical results to refine our framework. We are also planning to build software bridges based on CASE Data Interchange Format standards to integrate groupware products and CASE products.

The contribution of this research is twofold. One benefit pertains to our understanding of activities and processes in requirements specification, how they may be facilitated by a GSS, how they may be structured to achieve the most effectiveness and efficiency, what process models may be employed, what features of a GSS are most useful, and how GSS and JAD are integrated into the domain analysis methodology. The other pertains to the use of GSS for requirements specification in practice and thus to the improvement of applications development productivity by making requirements specification more efficient and effective.

## REFERENCES

1. ANSI/IEEE Std 830–1984. IEEE Guide to Software Requirements Specifications. New York: Institute of Electrical and Electronics Engineers, 1984.

2. August, J.H. Joint Application Design: The Group Session Approach to System Design. Englewood Cliffs, NJ: Prentice-Hall, 1991.

3. Boehm, B.W. Software engineering. IEEE Transactions on Computer (December 1976), 225–240.

4. Brennan, P.F. CASE tools in a JAD workshop. CASE Trend, 2, 2 (1990), 5–6, 8.

5. Brooks, F.P. The Mythical Man-Month: Essays on Software Engineering. Reading, MA: Addison-Wesley, 1975.

6. Carmel, E.; Whitaker, R.D.; and George, J.F. PD and joint application design: a transatlantic comparison. Communications of the ACM, 36, 4 (June 1993), 40–48.

7. CDIF—Standardized CASE Interchange Meta-Model. EIA Interim Standard, EIA/IS-82. Washington, DC: Electronics Industries Association, July 1991.

8. Chen, M.; Liou, Y.I.; and Weber, E.S. Developing intelligent organizations: a context-based approach to individual and organizational effectiveness. Organizational Computing, 2, 2 (1992), 181–202.

9. Chen, M., and Nunamaker, J.F., Jr. The architecture and design of a collaborative environment for systems definition. Data Base, 22, 1/2 (1991), 22–29.

10. Chen, M.; Nunamaker, J.F., Jr.; and Weber, E.S. Computer-aided software engineering: present status and future directions. Data Base, 20, 1 (1989), 9–13.

11. Cook, P., et al. Project Nick: meeting argumentation and analysis. ACM Transactions on Office Information Systems, 5, 2 (1987), 132–146.

12. Couger, J.D. Evolution of system development techniques. In J.D. Couger, M.A. Colter, and R.W. Knapp (eds.), Advanced System Development/Feasibility Techniques. New York: Wiley, 1983, 6–13.

13. Davy, C. Using CASE to control a large data analysis project. In K. Spurr and P. Layzell (eds.), CASE on Trial. New York: Wiley, 1990, 7–16.

14. Dennis, A.R.; George, J.F.; Jessup, L.M.; Nunamaker, J.F., Jr.; and Vogel, D.R. Information technology to support electronic meetings. MIS Quarterly, 12, 4 (1988), 591–624.

15. Dennis, A.R.; Heminger, A.R.; Nunamaker, J.F., Jr.; and Vogel, D.R. Bringing automated support to large groups: the Burr-Brown experience. Information and Management, 18, 3 (1990), 111–121.

16. Gallupe, R.B.; DeSanctis, G.; and Dickson, G. Computer-based support for group problem finding: an experimental investigation. MIS Quarterly, 12, 2 (1988), 277–296.

17. Gray, P. Managing the emerging information technologies: the case of group technologies. In P. Gray, W.R. King, E.R. McLean, and Watson, H.J. (eds.), The Management of Information Systems. Orlando, FL: Dryden Press, 1989, 123–155.

18. Greif, I. Domain-specific coordination support. In I. Greif (ed.), Computer-Supported Cooperative Work: A Book of Readings. San Mateo, CA: Morgan Kaufmann, 1988, 251–252.

19. GroupSystems V $^{TM}$ marketing material, Tucson, AZ, Ventana Co., 1993.

Couger, M.A. Colter, and R.W. Knapp (eds.), Advanced System Development/Feasibility Techniques. New York: Wiley, 1983, 399–423.

21. Liou, Y.I. Collaborative knowledge acquisition. Expert Systems with Applications, 5, 1 (1992), 1–13.

22. Liou, Y.I., and Nunamaker, J.F., Jr. An investigation into knowledge acquisition using a GDSS. Information & Management, 24 (1993), 121–132.

23. Liou, Y.I.; Weber, E.S.; and Nunamaker, J.F., Jr. A methodology for knowledge acquisition in a group decision support systems environment. Knowledge Acquisition, 2 (1990), 129–144.

24. Martin, J. Rapid Systems Development. New York: Macmillan, 1991.

25. Nunamaker, J.F., Jr.; Applegate, L.M.; and Konsynski, B.R. Facilitating group creativity with GDSS. Journal of Management Information Systems, 3, 4 (1987), 5–19.

26. Nunamaker, J.F., Jr.; Applegate, L.M.; and Konsynski, B.R. Computer aided deliberation: model management and group decision support. Journal of Operation Research, 36 (1988), 826–848.

27. Nunamaker, J.F.; Weber, E.S.; and Chen, M. Organizational crisis management systems: planning for intelligent action. Journal of Management Information Systems, 5, 4 (1989), 7–32.

28. Nunamaker, J.F.; Dennis, A.R.; Valacich, J.S.; Vogel, D.R.; and George, J.F. Electronic meeting systems to support group work. Communications of the ACM, 34, 7 (1991), 40–61.

29. Pinsonnault, A., and Kraemer, K. L. The impacts of technological support on groups: an assessment of the empirical research. Decision Support Systems, 5, 2 (1989), 197–216.

30. A Quick Tour of Lotus Notes. Lotus Notes Release 3. Cambridge, MA: Lotus Corp., 1993.

31. Turoff, M., and Hiltz, S.R. Computer support for group versus individual decisions. IEEE Transactions on Communications, 30 (January 1982), 82–91.

32. VisionQuest™ marketing material. Collaboration Technologies Corporation, Austin, Texas, 1993.

33. Wetherbe, J.C. Executive information requirements: getting it right. MIS Quarterly, 15, 1 (March 1991), 51–65.

34. Wood, J., and Silver, D. Joint Application Design: How to Design Quality Systems in 40% Less Time. New York: Wiley, 1989.
