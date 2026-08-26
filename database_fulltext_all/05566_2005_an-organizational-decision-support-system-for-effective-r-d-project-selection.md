---
otero_id: 5566
otero_key: "GNE8SMA2"
title: "An organizational decision support system for effective R&D project selection"
authors: "Qijia Tian; Jian Ma; Jiazhi Liang; Ron C.W. Kwok; Ou Liu"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2003.08.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# An organizational decision support system for effective R&D project selection

Qijia Tian<sup>a,b</sup>, Jian Ma<sup>a,</sup>\*, Jiazhi Liang<sup>a</sup>, Ron C.W. Kwok<sup>a</sup>, Ou Liu<sup>a</sup>

<sup>a</sup> Department of Information Systems, City University of Hong Kong, Hong Kong, PR China <sup>b</sup> Department of Computer Science, Shandong University of Science and Technology, PR China

Received 1 November 2001; accepted 1 August 2003 Available online 14 March 2004

## Abstract

Research and development (R&D) project selection is an important task for organizations with R&D project management. It is a complicated multi-stage decision-making process, which involves groups of decision makers. Current research on R&D project selection mainly focuses on mathematical decision models and their applications, but ignores the organizational aspect of the decision-making process. This paper proposes an organizational decision support system (ODSS) for R&D project selection. Object-oriented method is used to design the architecture of the ODSS. An organizational decision support system has also been developed and used to facilitate the selection of project proposals in the National Natural Science Foundation of China (NSFC). The proposed system supports the R&D project selection process at the organizational level. It provides useful information for decision-making tasks in the R&D project selection process. <sup>D</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: ODSS; ODSS architecture; ODSS application; R&D project selection

## 1. Introduction

Research and development (R&D) project selection is an organizational decision-making task commonly found in organizations like government funding agencies, universities, research institutes, and technology-intensive companies. It is a compli cated and challenging task to organizations with the following reasons: (1) it is very difficult to predict the future success and impacts of the candidate projects; (2) it is a multi-stage multi-person decision making process involving a group of decision makers (e.g. external reviewers and panel experts). Thus, it can be very hard to manage the decisionmaking process, especially when the decision makers have heterogeneous decision-making strategies [5,7,22].

In the past four decades, a number of decision models and methods (e.g. Mathematical Programming and Optimization, Decision Analysis, Economic Models, and Interactive Method) have been developed to help organizations make better decisions in R&D project selection [7,16]. However, current research findings [14,22] indicate that many of the elaborated decision models and methods are not being used, and they have limited impacts on decision makings for real-world project selection. In order to improve the usability of decision models and methods in real application, decision support systems (DSSs) have been proposed and developed, which integrate decision models and methods with computer-based supports together [5,10,13,14,24]. Although some of the proposed DSSs are useful, they use decision models and methods for specific tasks and fail to support the whole decision-making processes at the organization level. Since the R&D project selection process typically involves multiple decision makers in different organizational units, an organizational decision support system (ODSS) is more appropriate for R&D project selection tasks.

ODSS is an integrated decision support tool with focus on the organization-wide issues rather than individual, group, or departmental issues [4,6,18]. It supports organizational decision activities by integrating model base with database and user interfaces over the communication networks. ODSS is different from the traditional DSS in aspects such as goal, scope, users, technology components, and implementation methodologies [11,12].

ODSS combines computer and communication technologies to coordinate decision-making activities across functional areas and hierarchical layers [20,28]. ODSS architectures have been proposed to support distributed decision-making tasks with access controls over the organization [8,17,25]. ODSSs have been applied in the telecommunication organizations [11], the military [3], the governments [23], and other organizations [2,19,21]; however, few research can be found in ODSS for R&D project selection. This paper attempts to present the development of an ODSS for the selection of R&D projects at the National Natural Science Foundation of China (NSFC).

Section 2 of this paper describes the research background. Section 3 proposes an ODSS architecture for R&D project selection. Section 4 reports the application of the proposed ODSS in NSFC. A summary of the contribution and lessons learned can be found in the last section.

## 2. Research background

NSFC (http://www.nsfc.gov.cn) is the largest government funding agency in China with a primary aim to promote basic and applied research. Supported by the Chinese government, NSFC’s annual budget has been dramatically increased from RMB 80 million in 1986 to over RMB 1,290 million in 2000. Up to 1999, it has provided funding support for more than 51,500 projects.

There are seven scientific departments, four bureaus, one general office and three associated units in NSFC. The scientific departments are responsible for the selection and management of the projects, while the bureaus, general office and associated units are mainly responsible for policy making, administration and other related affairs.

One of the major tasks of NSFC is to select and fund R&D projects with great potential of scientific

Table 1  
Major decision tasks in R&D project selection process

<table><tr><td>No.</td><td>Decision task</td><td>Decision makers</td><td>Responsibilities</td></tr><tr><td>1</td><td>Proposal submission</td><td>1. Division as well as department managers of NSFC2. Applicants3. Research office coordinators of the applicant institutes</td><td>1. Validate the content of proposals2. Ensure the applicants and the proposal meet the application requirements</td></tr><tr><td>2</td><td>Selection of external reviewers</td><td>1. Division managers</td><td>1. Assign external reviewers to proposals2. Transfer proposals to appropriate divisions</td></tr><tr><td>3</td><td>Peer review</td><td>1. Division managers2. External reviewers</td><td>1. Evaluate proposals by external reviewers2. Validate the content of review results3. Coordinate the evaluation process by division managers</td></tr><tr><td>4</td><td>Aggregation of review results</td><td>1. Division managers</td><td>1. Aggregate the external review results2. Recommend proposals for panel evaluation</td></tr><tr><td>5</td><td>Panel evaluation</td><td>1. Department and division managers2. Panel experts</td><td>1. Make decisions for margin proposals2. Suggest a list of funded projects</td></tr><tr><td>6</td><td>Final decision</td><td>1. Top managers2. Department managers</td><td>1. Confirm the final recommendation list2. Treat exceptional cases</td></tr></table>

breakthrough or social impacts. The selection process in NSFC is carried out once a year for most of its funding programs. Every year, NSFC receives more than 34,000 project proposals. Five external reviewers are normally assigned to evaluate each proposal. The project selection process is coordinated by the top management and accomplished by the seven scientific departments as well as their divisions. The overall project selection task is assigned to departments, and then departments further assign their tasks to divisions. Division managers then invite and assign external reviewers and panel experts to evaluate the proposals. NSFC maintains a database with more than 50,000 external reviewers and 700 panel experts from 69 disciplines.

![](/api/attachments/GNE8SMA2/fulltext/images/3f77fd1d0f006686034d3385e405ec66b6799d295692f7966ac2ee13f5026273.jpg)  
Fig. 1. R&D project selection process.

Although the evaluation process is somewhat different for projects in different program categories, the basic steps for project selection are similar (see Table 1 for the major decision tasks in R&D project selection process). They include proposal submission, selection of external reviewers, peer review, aggregation of review results, panel evaluation and final decision.

It can be seen from Table 1 that the decision makers are classified into six groups according to their decision-making tasks in the R&D project selection process. These decision-making groups cooperate with each other to accomplish the overall goal of selecting the best project proposals. They perform decision tasks in a certain sequence in which the outputs of one group can be the inputs to another group. A conceptual model of the R&D project selection process at NSFC is specified as shown in Fig. 1.

In Fig. 1, groups of decision makers are represented as circles with the group numbers in them. There are two kinds of resources for a group: (1) information resource from database or decision output of another group, which is represented as rectangle in the figure; (2) the human resources such as managers of the funding agency, external reviewers and panel experts, which are represented as ellipses. So, for each circle in the figure, there are at least two input arrows, and one output arrow. The input arrows indicate the resources involved in the group, and output arrow indicates the decision result of the group. For example, in Fig. 1, the input information for group 5 is the summary of external reviewers’ evaluation and a list of funded proposals from group 4. The decision makers are department and division managers as well as panel experts. The output is the final recommendation list of the funded proposals.

R&D project selection is a typical organizational decision-making task since the decisions are made on behalf of the organization [9]. It shares the basic features of organizational decision making as identified in the literature [4,6,18]. Thus, an ODSS is ideally suitable to support this R&D project selection process.

## 3. An ODSS for R&D project selection

This section introduces an object-oriented approach to the development of ODSS and its applications in the R&D project selection.

## 3.1. Object-oriented approach to ODSS development

Object-oriented software engineering with Unified Modeling Language (UML) [1] has been used in the design and implementation of the proposed ODSS. UML is a language for specifying, constructing, and documenting the artifacts of a real-world software system. It has been widely used in the development of large-scale software systems [1].

The major steps of the methodology include the following: (1) the user’s requirements are captured by a set of diagrams called use case diagrams. A use case is a collection of possible sequences of interactions between the system under discussion and its users (or Actors), relating to a particular goal. The diagrams specify all functionalities that the system should be able to perform from the point view of Actors. (2) Based on the use cases, classes as well as their relationships in the system are identified and described in class diagrams. (3) Sequence diagrams or collaboration diagrams are developed. These diagrams refine use cases (as defined in the use case diagrams) by describing the dynamic interaction between objects (instances of classes). Slicing all the collaboration diagrams together, we get an overall picture of how each actor’s operation will be accomplished by interactions between objects. Based on which, we are able to decompose the whole system into several functionally independent subsystems, and further decompose the subsystems into software components. Results of the decomposition are described by the subsystem collaboration diagrams.

An object-oriented analysis and design has been carried out based on the requirements of NSFC. As a result, an ODSS architecture for R&D project selection is designed as shown in Fig. 2.

## 3.2. The ODSS system architecture

The overall architecture of the ODSS (see Fig. 2) falls into the browser/server system paradigm. The system at the server side consists of the following three parts:

Organizational Information Resources Management Component: it manages the overall information resources of the organization, including proposal database, user database, model base, and knowledge base.

Group Management Component: it is responsible for managing the life cycle of decision-making groups. Thus it is a gateway among decisionmaking groups and the organizational information resources. Specifically, it supports creation, main tenance, coordination, and termination of groups.

Group Environment Component: It specifies the group work environment. Groups may work through Web-based systems, emails, electronic meeting systems, text/video-based conferencing systems, and so on. The environment provides technology infrastructure for individual groups.

Decision makers are categorized as internal and external users in the application. Internal Users are usually managers of NSFC, while External Users are usually external reviewers, panel experts and research office coordinators of the organizations.

![](/api/attachments/GNE8SMA2/fulltext/images/e95b3d3b5ea2d2c48d7cedd5cf4134b0b1d549c45c49b45df2abaad6a7809cd6.jpg)  
Fig. 2. ODSS architecture for R&D project selection.

## 3.3. R&D project selection under the ODSS architecture

The support provided by the ODSS architecture covers the whole R&D project selection process. According to Table 1, the R&D project selection process can be divided into the following three phases: (1) task decomposition and group creation; (2) decision making support and coordination; and (3) information aggregation for final organizational decision results.

In the phase of task decomposition and group creation, R&D project selection can be decomposed into subtasks crossing organizational hierarchies. In NSFC, the organizational task is decomposed into six subtasks (see Table 1). Along with each task decomposition, a decision group is created to handle the subtask. The system provides on-line supports to create decision groups along with the task decomposition.

In the phase of decision-making support and coordination, members of each group have to make their own decisions. Major support functions of the ODSS for this phase are (1) to provide decision support tools for decision makings; and (2) to coordinate the decision activities of group members. For coordination purpose, the group management component allows the group controllers to maintain the group memberships and to check the progress of group members.

For organizational decision making, there is a need to have a mechanism to aggregate the decision results obtained from different groups into the final decision. In the phase of information aggregation for final organizational decision, the ODSS supports the following: (1) all the decision groups are connected so that controllers of one group may act as the controllers or ordinary members of other groups. They therefore form a decision net. (2) Group controllers at different net nodes can aggregate the decision results of its members. Decision support tools are provided for the aggregation.

## 3.4. The database, model base and knowledge base

The database, model base and knowledge base are designed in the ODSS to support the decision makings in the R&D project selection process. The static data model of the ODSS is illustrated in Fig. 3, while the decision models and knowledge rules for the ODSS are summarized in Table 2.

![](/api/attachments/GNE8SMA2/fulltext/images/039ee8dd1356e40c34a769be78ef22a2fbd487d2d6939d6daaa4cd87c8d47792.jpg)  
Fig. 3. Data model for R&D project selection.

Table 2  
Decision models and knowledge rules in the ODSS

<table><tr><td>Task level</td><td>Task name</td><td>Support components</td></tr><tr><td rowspan="4">Division</td><td>1. Proposal submission</td><td>Knowledge rules for proposal validation</td></tr><tr><td>2. Selection of external reviewers</td><td>A model integrating a fuzzy matching model and an assignment problem model</td></tr><tr><td>3. Peer review</td><td>Knowledge rules for review results validation</td></tr><tr><td>4. Aggregation of review results</td><td>Decision model for aggregation subjective and objective information</td></tr><tr><td>Department</td><td>5. Panel evaluation</td><td>Decision model for aggregate preferences with multiple formats</td></tr><tr><td>Top</td><td>6. Final decision</td><td>Knowledge rules for funded projects distribution check</td></tr></table>

The model base structure for R&D project selection is designed for selection of external reviewers, aggregation of review results, and panel evaluation.

For selection of external reviewers, two models are designed. The first one is a fuzzy matching model, and the second one is a model for assignment problems. Since not every external reviewer is qualified for reviewing a proposal, the classical model for assignment problem cannot be applied directly in this situation. We first use the fuzzy matching model to determine the matching degrees between proposals and external reviewers, and then apply the assignment model to choose the external reviewers.

The model for aggregation of review results supports the integration of the subjective information with objective information [15,29]. The subjective information refers to the external reviewers’ evaluation results, while the objective information relates to the performance of his/her projects previously funded by NSFC.

The model for panel evaluation supports aggregation of preference information in multiple formats, i.e., ordered vector, utility vector, selected subset, fuzzy selected subset, normal preference, and fuzzy preference relation [31]. It is designed for the unstructured group meeting, where each panel expert may use his/ her favorite format to express the preference. The model provides a method to aggregate these individual preferences in different formats. The model has been successfully applied to the government funding agencies for journal grading exercises [29,30], which is a key criterion to assess the performance of projects supported by NSFC.

Rule-based knowledge systems and conventional mathematical models are complementary decision support devices. Mathematical models are useful to the well-structured decision problems that often lead to optimization solutions, while rule-based knowledge systems are good at dealing with unstructured and semi-structured problems with heuristic algorithms to reach feasible solutions. Knowledge components enable a wider range of decisions and extend the capabilities of systems well beyond data-based and model-based DSS [27].

Knowledge rules for project selection at NSFC are usually implied in its guidance and policy documents. They can be abstracted to form a rule-base. The knowledge rules for R&D project selection are classified into three categories: proposal submission, peer review, and final decision [26]. The rules for proposal submission are used to help division managers to classify the proposals into invalid, incomplete, undetermined, and valid categories. If it is invalid, division managers can turn down the proposal by filling in the NSFC Proposal Evaluation Form and then send to the department manager for approval. If the proposal is incomplete, applicants will be asked to resubmit the complementary material. If it is an undetermined proposal, a further decision is expected by the department and division managers. If it is a valid proposal, external reviewers will be assigned. The rules for peer review are used in a similar way to those for proposal submission. It is designed to check if all the required and correct content are included in the review results. The problematic review results will be ticked out for special treatment. The rules for final decision are designed for top managers to decide if the funded projects meet the macro policy requirements such as the project distribution over programs, subject areas, geographic areas and so on.

The rule base plays an important role in the ODSS. It improves the efficiency of the work progression. For example, during the proposal submission period, a division manager usually has to process hundreds of proposals by reading it line by line at the screen to check if they meet the basic requirements.

## 4. Application of the ODSS for R&D project selection in NSFC

The proposed ODSS has been implemented and incorporated in the Internet-based Science Information System (ISIS: http://isis.nsfc.gov.cn). It is built on a three-tier client/server platform as shown in Fig. 4. Object-oriented software engineering method, i.e. the UML [1], has been used in the analysis, design, and implementation of the system. Thus the components of the ODSS and those of ISIS are compared as shown in Table 3.

ISIS is built on the proposed ODSS architecture. It provides a set of major decision support functions at individual, group and organizational levels. The ISIS database stores information about proposals and users. The model base and a basic set of knowledge rules have been implemented and stored on the application server. Under current implementation, ISIS provides full supports for proposal submission, assignment of external reviewers, peer review, and aggregation of review results and partial supports for panel evaluation and final decision.

At the individual level, ISIS users are classified into the system administrator (the super user of the system), top manager, department manager, division manager, organizational user, principal investigator, external reviewer, and public user. Each user is assigned to a user group with access rights to certain system functions.

Table 3  
The matrix between the components of ODSS and of ISIS

<table><tr><td>ODSS architectural components</td><td>ISIS system components</td></tr><tr><td>Organizational information resources management component</td><td>&lt;&lt;Type Library&gt;&gt; Common type library for universal resource request</td></tr><tr><td>Group management component</td><td>&lt;&lt;Sub System&gt;&gt; Subsystem for project administrators</td></tr><tr><td>Group environment components</td><td>&lt;&lt;Sub System&gt;&gt; Subsystems for decision-making groups for the tasks listed in Table 1</td></tr></table>

The ISIS decision support functions at the individual level provide supports for division managers and external reviewers who have to make individual decisions at the operational level. As shown in Table 1, most of the decision tasks for division managers are at the individual and operational levels, e.g. validation of proposals and review results, and assignment of proposals to external reviewers.

At the group level, ISIS implements a group management component. Internal users like top managers, department managers, and division managers have permissions to create their own decision-making groups. They can use the function to create a new group, maintain the group membership, coordinate the group work, and check the work progression. One manager may create different decision-making groups for different decision-making tasks.

![](/api/attachments/GNE8SMA2/fulltext/images/7aefbd9813384b03a1bda3b8c29c2d392d362cb9c8ffa4391ad83afd0d898e53.jpg)  
Fig. 4. A three-tier system platform for ODSS implementation.

At the organizational level, ISIS provides supports to the three major phases of the R&D project selection process. (1) For the phase of task decomposition and group creation, ISIS supports the task decomposition (see Table 1) in NSFC. Specific subsystems have been designed for decision groups on these tasks. Thus the controller of a group can select and manage his/her group members. (2) For the phase of decision-making support and coordination, decision models and knowledge rules for proposals submission (see Table 2) are implemented. Thus the group controllers can check and coordinate their groups’ work progression. Multiple views of the work progression are usually provided, including detailed lists, statistic tables and figures. (3) For information aggregation of final organizational decision results, the ISIS provides group controllers with ways to aggregate the information of members decision results and the decision models are also developed to facilitate this process.

Thirteen, 37 and 52 (all) divisions in NSFC participated in the exercises of project selection through ISIS in 2001, 2002 and 2003, respectively. Results of the applications are very positive, especially the success rate of electronic peer review has reached 96% in 2003. The main reasons include (1) the system provides support at the individual, group, and organizational levels over the Internet. It therefore facilitates the coordination among groups of decision makers, and shortens the cycle time of project selection. (2) It provides decision makers with useful decision aids such as decision models and business logic rules with Web interfaces. (3) It helps to simplify the workflow and improve the work efficiency of NSFC.

## 5. Contribution and lessons learned

This paper presents an ODSS framework for R&D project selection. It includes a group-based modeling method for R&D project selection, and a corresponding ODSS architecture that supports and coordinates the work of decision-making groups. The proposed ODSS architecture provides support functions for decision makers at individual, group and organizational levels to achieve the organizational goal. In addition, the group management component of the ODSS architecture is presented to handle the difficult problems of distributed group decision-making process. Object-oriented modeling methodology has been used in the analysis, design and implementation of the proposed ODSS architecture.

The proposed architecture has been implemented and incorporated into the ISIS (an Internet-based science information system for R&D project management), which has been used in the R&D project selection in NSFC. The proposed approach looks at the project selection from organizational decisionmaking perspective; it supports the whole life cycle of the R&D project selection. However, successful application of the proposed system at NSFC has not been an easy task. Some senior staff at NSFC found it difficult to enter decision opinions in Chinese on computer terminals, thus assistant devices such as Chinese write pad should be provided. At the beginning, some staff thought that the use of the system would increase their workload. Thus reward incentives should be designed and implemented so as to ensure the successful adoption of the system. The wide spread of SARS in China during April and June 2003 has encouraged division managers of NSFC and external reviewers to use ISIS for project selection tasks over the Internet.

## Acknowledgements

This research was partly supported by the National Natural Science Foundation of China and Hong Kong Research Grant Council Joint Funding Scheme (Project No. 9050137), the Competitive Earmarked Research Grant (CERG), Hong Kong SAR (Project No.9040709 and 9040825) and Strategic Research Grant of City University of Hong Kong (Project No. 7001017). Many thanks to the anonymous reviewers for their contributions to improve this manuscript.

## References

[1] G. Booch, I. Jocobson, J. Rumbaugh, The Unified Modeling Language User Guide, Addison-Wesley, Boston, 1999.

[2] M.M. Bright, et al., An ODSS for hospital-based clinical deci sion-making: conceptual design and analysis, Proceedings of HICSS-29 III, Computer Society Press, Washington, 1996, pp. 72– 81.

[3] G.M. Carter, et al., Building Organizational Decision Support Systems, Academic Press, Boston, 1992.

[4] J.F. George, The conceptualization and development of organizational decision support systems, Journal of Management In formation Systems 8 (3) (1991–1992) 109–125.

[5] F. Ghasemzadeh, N.P. Archer, Project portfolio selection through decision support, Decision Support Systems 29 (2000) 73 – 88.

[6] R.D. Hackathorn, P.G.W. Keen, Organizational strategies for personal computing in decision support systems, MIS Quarterly/September, (1981) 21 – 27.

[7] A.D. Henriksen, A.J. Traynor, A practical R&D project-selection scoring tool, IEEE Transactions on Engineering Management 46 (2) (1999) 158–170.

[8] C.W. Holsapple, A.B. Whinston, Decision Support Systems: A Knowledge-Based Approach, West Publishing, St. Paul, MN, 1996.

[9] G.P. Huber, The nature of organizational decision-making and the design of decision support systems, MIS Quarterly/June, (1981) 1 – 11.

[10] M.G. Iyigun, A decision support system for R&D project selection and resource allocation under uncertainty, Project Management Journal 24 (1) (1993) 5 – 13.

[11] Y.G. Kim, H.W. Kim, J.W. Yoon, H.S. Ryu, Building an organizational decision support system for Korea Telecom: a process redesign approach, Decision Support Systems 19 (4) (1997) 255– 269.

[12] H. Kivijarvi, A substance-theory-oriented approach to the implementation of organizational DSS, Decision Support Systems 20 (1997) 215 – 241.

[13] D.F. Kocaoglu, M.G. Iyigun, Strategic R&D project selection and resource allocation with a decision support system application, Proceedings of IEEE International Engineering Management Conference, 1994, IEEE, pp. 225 – 232.

[14] M.J. Liberatore, A.C. Stylianou, Expert support systems for new product development decision-making: a modeling framework and applications, Management Science 41 (8) (1995) 1296 – 1316.

[15] J. Ma, Z.P. Fan, L.H. Huang, A subjective and objective integrated approach to determine attribute weights, European Journal of Operational Research 112 (2) (1999) 397 – 404.

[16] J.P. Martino, Research and Development Project Selection, Wiley-Interscience Publication, New York, 1995.

[17] L.L. Miller, S. Nilakanta, Design of organizational decision support systems: the use of a data extraction schema to facilitate model-database communication, Proceedings of HICSS-24 IV, Computer Society Press, Washington, 1991, pp. 65 – 72.

[18] J. Nunamaker, et al., Organizational decision support sys-

tems, in: A. Stohr, B.R. Konsynski (Eds.), Information Systems and Decision Processes, IEEE Computer Society Press, Los Alamitos, Calif., 1992, pp. 137 – 166.

[19] A. Perira, Modeling an organizational decision support system to improve retailers’ decisions, Proceedings of HICSS-28 III, Computer Society Press, Washington, (1995) 933 – 940.

[20] A.S. Philippakis, G.I. Green, An architecture for organizationwide decision-support systems, Proceedings of the Ninth International Conference on Information Systems, Minneapolis, Minnesota, (1988) 257– 263.

[21] R. Santhanam, T. Guimaraes, J.F. George, An empirical investigation of ODSS impact on individuals and organizations, Decision Support Systems 30 (1) (2000) 51 – 72.

[22] R.L. Schmidt, J.R. Freeland, Recent progress in modeling R&D project-selection processes, IEEE Transactions on Engineering Management 39 (2) (1992) 189–201.

[23] T.K. Sen, J.M. Laurence, T.J. Hess, An organizational decision support system for managing the DOE hazardous waste cleanup program, Decision Support Systems 29 (1) (2000) 89–109.

[24] T.J. Stewart, A multi-criteria decision support system for R&D project selection, Journal of Operational Research Society 42 (1) (1991) 17 – 26.

[25] E.B. Swanson, R.W. Zmud, ODSS concepts and architecture, in: A. Stohr, B.R. Konsynski (Eds.), Information Systems and Decision Processes, IEEE Computer Society Press, Los Alamitos, Calif., 1992, pp. 138– 141.

[26] Q.J. Tian, J. Ma, O. Liu, A hybrid knowledge and model system for R&D project selection, Expert Systems with Applications 23 (3) (2002) 265–271.

[27] E. Turban, J.E. Aronson, Decision Support Systems and Intelligent Systems, Prentice Hall, Upper Saddle River, New York, 1998.

[28] R.T. Watson, A design for an infrastructure to support organizational decision-making, Proceedings of HICSS-23 III, Computer Society Press, Washington, (1990) 111 – 119.

[29] D. Zhou, J. Ma, E. Turban, Journal quality assessment: an integrated subjective and objective approach, IEEE Transactions on Engineering Management 48 (4) (2001) 479–490.

[30] D. Zhou, J. Ma, E. Turban, N. Bolloju, A fuzzy set approach for evaluating grades of journals, Journal of Fuzzy Sets and Systems 131 (2002) 63 – 74.

[31] D.N. Zhou, Fuzzy Group Decision Support System Approach to Group Decision Making under Multi-Criteria, PhD Dissertation, City University of Hong Kong, 2000.

![](/api/attachments/GNE8SMA2/fulltext/images/12e9ab1a2cfb05f421df18f26e35eecd0a80aeee488e946ca67d94a053c505a8.jpg)  
Qijia Tian is currently pursuing his Ph.D. degree in the Department of Information Systems, City University of Hong Kong. His current research interests include organizational decision support systems, agentbased coordination in organizational decision-making and object-oriented model management.

![](/api/attachments/GNE8SMA2/fulltext/images/dbd57617dca57b05e21a3b3a9dea76de5f283260b884ec77ee08c7e921bf6891.jpg)

Jian Ma is an Associate Professor in the Department of Information Systems, City University of Hong Kong. He received his Doctor of Engineering degree in Computer Science from Asia Institute of Technology in 1991. He was a Lecturer in the School of Computer Science and Engineering at the University of New South Wales, Australia, before joining City University in 1993. Dr. Ma’s research areas include Web-based decision support systems, and object-ori-

![](/api/attachments/GNE8SMA2/fulltext/images/6307338e51ccea99d3b8a043149f6e31fdd0a35b5c4b679051ba40c58818f3bd.jpg)  
Ou Liu is currently pursuing his Ph.D. degree in the Department of Information Systems, City University of Hong Kong. His current research interests include organizational decision support systems and model management.

ented methods for information system development. His past research has been published in IEEE Transactions on Engineering Management, IEEE Transactions on Education, IEEE Transactions on Systems, Man and Cybernetics, Decision Support Systems and European Journal of Operational Research.

Jiazhi Liang is currently pursuing his M.Phil. degree in the Department of Information Systems, City University of Hong Kong. His current research interests include component-based information system development and electronic document management.

![](/api/attachments/GNE8SMA2/fulltext/images/03112f5ba930a387656f8b0c7559bd61a3027c9eb42ea93eec5ae4781663e6ab.jpg)

Ron Chi-Wai Kwok is an Assistant Professor in the Department of Information Systems, City University of Hong Kong. He received his Ph.D. in Information Systems from City University of Hong Kong. He was an Assistant Professor at the School of Management, the State University of New York at Binghamton before joining City University in 2002. His current research interests include group support system (GSS), technology-based learning,

leadership, IS outsourcing and electronic commerce. He has papers published in Journal of Association for Information Systems, Journal of Management Information Systems, Communications of ACM, IEEE Transactions on Systems, Man, and Cybernetics, Decision Support Systems, European Journal of Information Systems, Information and Management, Group Decision and Negotiation, International Journal of Information Management and Computers and Education.
