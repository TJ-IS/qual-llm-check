---
otero_id: 23498
otero_key: "MFXY8D7N"
title: "Methodological requirements for information systems development"
authors: "Sachidanandam Sakthivel"
year: "1992"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1992.20"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Methodological requirements for information systems development

SACHIDANANDAM SAKTHIVEL
Bowling Green State University, Bowling Green, Ohio, USA

A systems development methodology is a collection of procedures, tools, and techniques to develop computer based information systems. To develop better information systems, research studies have suggested several requirements for these methodologies. These requirements may not be equally important for practitioners. Identification of their importance for practitioners can guide researchers to solve practical issues in systems development. It will also be useful to evaluate and compare various methodologies. A study in which theoretical requirements were presented to practitioners for evaluation is presented and its findings described.

## Introduction

A systems development methodology (SDM) is a collection of organized methods to develop computer based information systems. A SDM helps to develop systems in stages such as requirements analysis, design, and implementation. Such a SDM provides tools and techniques to use in each stage of systems development. It also recommends procedures for planning, control, and evaluation of the development process.

To develop better information systems, many research studies have suggested requirements such as ease of use, automated tools, and quality assurance procedures. The importance of such SDM requirements is investigated for systems development professionals (henceforth called practitioners). This study will help researchers to understand the practitioners' perspective of methodological issues in systems development. Solving such issues will reduce the gap between theory and practice. Practitioners can objectively evaluate and compare various SDMs by identifying the support provided by a SDM for each of the requirements.

This study reviewed many research studies to identify important requirements for SDMs. These studies included feature analyses of SDMs and studies suggesting better systems development methods. The research methodology used in this study to investigate the importance of these requirements to practitioners is briefly discussed. Future research directions are also indicated.

## SDM requirements

Research studies suggest that a SDM should have capabilities to develop diverse systems, support various tasks during the systems development cycle, have ease of use, develop information systems within the estimated time and cost, and develop effective systems. These SDM requirements are further discussed.

## Capability to develop diverse systems

Although more than 25 SDMs are commercially available, they differ in their application and usefulness (Olle et al., 1982; Olle et al., 1983; Olle et al., 1986). Each of these SDMs may not meet the needs of system developers completely and may not be suitable for all systems development situations. For example, SDMs such as structured analysis-structured design (Yourdon and Constantine, 1975), and structured analysis design and implementation of information systems (STRADIS, 1983) widely used in developing management information systems are not suitable for developing decision support systems. It also takes a considerable amount of time and effort to learn and use a SDM well, and hence, it is not practical to adopt several SDMs within an organization. It is not uncommon to spend a month in learning a methodology and several months to start using it effectively. An organization should be able to use a versatile SDM for developing a variety of systems such as file based systems, data base systems, centralized systems, distributed systems, etc.

Organizations have systems of varying sizes and life terms. While some systems having about 100 000 lines of code may be used for many years, systems having about 1000 lines of code may only be used for a few months. The scope of these systems may vary in terms of application to one or more departments and to one or more persons in a department. In addition, these systems may be simple or complex due to interactions among system components. Since most medium and large size organizations have a variety of computer hardware and software, systems developed using a SDM should be implementable on any type of hardware or software. Furthermore, changing requirements of dynamic organizations warrant frequent changes in systems design. Therefore, a SDM should also have capabilities to develop: systems of various sizes and life terms, systems having different scope and complexity, systems implementable on a variety of hardware and software, and systems with changing requirements.

## Capability to support various tasks during systems development life cycle

Research studies suggest the life cycle approach for medium and large size system projects (Boehm et al., 1984; Guimaraes, 1985). Generally, the system development life cycle includes investigation, requirements analysis, design, implementation, and post-implementation stages. SDMs following the systems development life cycle approach should support various tasks during each of these stages. However, SDMs such as user software engineering (Wasserman, 1982) do not support the requirements analysis stage and SDMs such as structured analysis and design technique (Ross, 1985) do not cover the implementation stage.

Identification of a system's goals is a critical activity during the investigation stage. If, for example, a production control system has the goal of reporting the production progress, such goals should be clearly identified along with its limitations. If users have unrealistic expectations that the system will also reduce work in progress by 20%, then it may result in the system's failure. A SDM should facilitate the identification of a system's goals, scope, and limitations. In addition, an assessment of the system feasibility is important. The development of a system consumes resources such as analysts' time, programmers' time, users' time, and computer time. The investment in these system resources should provide an adequate return in benefits to justify development. For example, a sales management system costing \$100 000 to develop must provide benefits such as increased sales and reduced costs at least to offset the costs of development. Therefore, the investigation stage should provide methods to identify costs and benefits of developing a system, and to perform a feasibility analysis for the system development.

An information system serves the information needs of the operational, tactical, and strategic levels of management. The strategic level of management may need a lot of information from outside the organization and some summarized information from within the organization to make decisions that are often unstructured. For example, a vice president of an organization in pricing a new product may need information about the market forecast, competitors' prices, and the cost of making the product. In contrast, the operational level of management requires a lot of detailed information from within the organization and very little from outside the organization to make structured and routine decisions. For example, a shop floor supervisor needs to have information about the products to manufacture, the product quality, quantity, what machines to use, what operations to perform, in what sequence, etc. A SDM should adopt appropriate requirements analysis strategy to obtain such diverse information needs of various levels of management as well as the required reliability and accuracy of this information. Since the performance of a system in terms of its response time affects user productivity, error rate, and job satisfaction (Schneiderman, 1984), a SDM should also identify the performance requirements of the system.

The design stage translates the requirement specifications into a computer oriented physical system. There are two major types of design activities. One deals with various functional aspects such as the design of programs and files of the system; the other deals with controls required to make the system function without errors.

Functional design involves the program and procedure specifications for processing the data to provide the required information in an efficient manner. The major activities include the identification of the: input data items and user-machine interface, output data items and user-machine interface, data to be stored and their organization, and automated and manual processing functions. Several methods for data modelling (e.g. Chen, 1977), data structuring (e.g. Gane and Sarson, 1979), and programming (e.g. Jackson, 1975) are available for doing the functional design. A SDM should support the major activities for the functional design independent of the method used.

An information system consists of people, computer hardware, software, data, and procedures. In order to meet the goals of the system, these five elements of the information system need to be controlled. These controls include ensuring the accuracy of input data, preventing unauthorized use of hardware, software, or data, spelling out procedures clearly on who should use the system and how they should use the system, and preventing the loss of software and data. A SDM should help to identify such controls, without which the system may not function as expected.

Implementation is a complex stage involving people and a variety of activities such as training the users, acceptance testing, and breaking the system in. Training of users is essential because knowledge, skills, and attitudes of users determine the implementation success. Users steeped into the practice of an old system, unaware of the new facilities or their advantages, or sceptical about its benefits may cause failure of the system. Acceptance testing is a task performed by users to ensure that the new system works as specified before converting to it. Depending on the nature and importance of the current system, a new system may have to be introduced using one of the four strategies: direct, parallel, phased, and pilot conversion. Each strategy has its own costs and benefits and should be chosen carefully. For example, a reservation system critical to the operations of an airline company should not be changed using the direct conversion strategy because even a minor failure in this system could cause the airline operations to halt.

The post-implementation stage involves operation, review, and maintenance. Operation is the on-going process of running the system for users. A review of a system's achievements and shortcomings against its goals will help identify the deviations so as to modify and fine tune the system. For example, an on-line system with a response time requirement of 3 s may have passed the testing stage but under peak operating conditions may only provide a response time of 10 s. Such deviations will have to be identified and corrected to meet the system goals. Despite carefully articulated requirements, diligent analysis, and detailed design, systems have been found to have problems warranting maintenance. A SDM should provide guidelines for maintaining a system because maintenance done as a patch work over a period may make the system structure inefficient.

## Ease in using the system

In addition to supporting various stages of systems development, a SDM should be easy to use. A SDM with clear definitions of terms, rules, symbols, and notations enhances its correct use. The SDM documentation should be readable, complete, consistent, and accurate. The rules and procedures used for developing systems should be well defined without being rigid or contrived. In addition, the SDM should state its limitations and assumptions to prevent wrong applications of the SDM. They should also be flexible to match the system developer's style and the application system. A SDM should also be teachable with minimum efforts. The availability of commercial training reduces an organization's burden in training new recruits.

## Capability to develop systems within estimated cost and time

High costs and slippage of development schedules are often associated with systems development. A SDM should contribute to productivity by minimizing the development cost and by producing the system in time. Better project management, verification procedures, and automated development tools can improve the productivity (Boehm, 1987). While most SDMs provide some methods for project management, they lack verification and automated tools.

Systems development follows a series of complex activities. Project management involves planning the sequence of these activities, estimating the type and amount of resources required for each activity as well as their duration, finding these resources, and scheduling and monitoring them to complete the project within the estimated time and cost. Since projects vary in size and complexity, and skills and tools required to develop systems are changing rapidly due to advances in hardware and software technology, time and resources estimated have been major problems in project management. A SDM should provide tools and techniques for systems project management.

The cost of correcting errors at a later stage of the development is higher, and therefore, verification procedures should be used to identify them early (Boehm, 1984). These procedures avoid rework and enable efficient utilization of resources. More than 30% improvement in productivity is possible by using verification procedures and by avoiding faults in the system (Boehm, 1987). Verification includes checking the completeness (all parts are present and fully developed), consistency (no conflicts among parts of the system), feasibility (meets functional and performance requirements), and correctness (input-output relations are provable) of system specifications.

Developing a system using the life cycle approach is often a time consuming and laborious process. Computer aided systems engineering (CASE) tools can have an impact on productivity (Case, 1985). CASE tools facilitate faster development of systems, better documentation, project management, and quality assurance.

## Capability to develop effective systems

Organizations often find that the developed systems are unresponsive, contain numerous errors, and fail to meet the user needs completely due to ineffective development methods. In addition to the skills of the system developers, the SDM with its tools, techniques, and procedures plays a major role in deciding the effectiveness of the system. The effectiveness of a system can be identified by the quality of the developed systems (Halloran et al, 1978; Prell and Sheng, 1984) and the user satisfaction (Ginzberg, 1981b). The quality of a system is measured by the extent to which a system performs to specifications (reliability), the extent to which it performs to expectations (relevance), and the facility it provides to identify and remove operational problems (maintainability). User satisfaction can be measured by user perceptions of system efficiency, information quality, their use of the systems, and the management of the systems.

## Summary of SDM requirements

In summary, various requirements of a SDM pertain to its capability to:

(1) Develop a variety of systems such as file-based systems and database systems (VARIETY)

(2) Develop small, medium, and large size systems (SIZE)

(3) Develop systems having short, medium or long life (LIFE)

(4) Develop systems of varying complexity (COMPLEXI)

(5) Develop systems implementable on a variety of hardware and software (ENVIRONM)

(6) Provide support to investigate the goals and feasibility of the system (INVESTIG)

(7) Provide support to identify functional and performance requirements of the system (REQUIREM)

(8) Provide support during the design; both functional and control (DESIGN)

(9) Provide support during the implementation (IMPLEMENTEN)

(10) Provide support for post-implementation activities (MAINTAIN)

(11) Have ease of use by having good SDM documentation (DOCUMENT)

(12) Have ease of leaning (TRAINING)

(13) Be flexible in its use (FLEXIBIL)

(14) Improve development productivity by good project management methods (PROJECTM)

(15) Improve development productivity using verification (VERIFICA)

(16) Improve development productivity using automated aids (AUTOMATE)

(17) Improve development productivity by documenting the system accurately (DOCQUALI)

(18) Improve development productivity by avoiding faults in systems development (FAULTS)

(19) Improve development productivity by curtailing cost overruns (COST)

(20) Improve development productivity by curtailing time overruns (TIME)

(21) Improve development productivity by generating reusable modules and code (REUSABLE)

(22) Improve development productivity by reducing post-implementation problems (POSTPROB)

(23) Develop reliable systems (RELIABIL)

(24) Develop relevant systems (RELEVANT)

(25) Develop maintainable systems (MAINTAIN)

(26) Develop modifiable systems (MODIFIAB)

(27) Develop efficient systems (EFFICIENCY)

(28) Improve the quality of information provided by the systems (QUALITY)

(29) Promote the system use (SYSUSE)

(30) Facilitate good systems management (MANAGEME)

(31) Ensure the success of the developed system (SYSSUCCES)

## Research method

To identify the relative importance of the 31 requirements, one needs to compare each with every other requirement. Such a method of comparison is tedious and may lead to arbitrary ranking. To simplify this comparison process, this research logically organized the requirements in the form of a hierarchy as shown in Figure 1 and used analytic hierarchy process (AHP) (Saaty, 1980) to analyse them. The numbers given in this figure are discussed in the Appendix.

In the hierarchy of Figure 1, the leaves (the lowest level) contain the 31 requirements which are grouped into one or more levels. The highest level of the hierarchy contains versatility, functionality, productivity, and effectiveness requirements. Here, versatility refers to the capability of a SDM to develop diverse systems. Functionality refers to the capability of a SDM to support various tasks during systems development life cycle and the ease with which it can be used. Productivity concerns the methods in a SDM to develop systems within the estimated cost and time. Effectiveness concerns the capability of a SDM to develop systems of the required quality.

A questionnaire was designed to rank the importance of these SDM requirements. Four hundred practitioners in the Association for Systems Management were requested to complete the questionnaire and 54 of them responded (constituting a response rate of 13.5%). Considering the complexity of the questionnaire, the amount of time required for filling it, and the unsolicited nature of the mailing, the response rate was good. Of these, 27 responses could not be used due to incomplete information in various parts of the responses. The remaining responses were statistically sufficient to show that practitioners prefer some requirements more than the other requirements, there is a common rank for these requirements, and there is a moderate agreement among the practitioners regarding the relative importance of various requirements for a SDM. The statistical analysis is described in the Appendix.

## Study findings

AHP analysis of the survey data showed that practitioners ranked the capability of a SDM to develop systems of required quality (effectiveness) as the most important, followed by its capability to support various tasks during the systems development cycle and the ease with which it can be used (functionality). The capability to develop diverse systems (versatility) was ranked next, and the capability to develop systems within the estimated time and cost (productivity) was ranked last. The analysis also showed how the practitioners ranked the importance of

![](/api/attachments/MFXY8D7N/fulltext/images/682bfa31d22c0442340a9198fc93293c44e7d8293a1593b564c5402c09b80139.jpg)

AUTOMATE — Automated aids for systems development
COMPLEXI — Ability to develop systems of varying complexity and nature
COST — Curtailing cost overruns
DESIGN — Design and coding stage
DOCQUALI — Quality of systems documentation
DOCUMENT — Good SDM documentation
EASEOFUS — Ease in using the SDM
EFFECTIV — Effectiveness of SDM
EFFICIEN — Efficiency of developed systems
ENVIRONM — Ability to develop systems for different computing environment
FAULTS — Avoiding and correcting faults in the system
FLEXIBIL — Flexibility in using the SDM
FUNCTION — Functionality of SDM
IMPLEMENTEN — Implementation stage
INVESTIG — Investigation stage
LIFE — Ability to develop different life systems
LIFECYCL — Support for life cycle stages
MAINTAIN — Maintainability of developed systems
MAINTENA — Maintenance stage
MANAGEME — Management of developed systems
MODIFIAB — Modifiability of developed systems

Figure 1 Hierarchy of SDM requirements and their relative importance

POSTPROB — Reducing post implementation problems
PROCONTR — Contribution to productivity
PRODUCTI — Productivity of SDM
PROJECTM — Project management procedures
PROPROCE — Productivity procedures available
QUALITY — Information quality of developed systems
RELELVAN — Relevance of developed systems
RELIABIL — Reliability of developed systems
REQUIREM — Requirement stage
REUSEABLE — Generating reusable space and code
SIZE — Ability to develop varied size systems
SYSQUALI — Quality of systems developed
SYSSUCCE — Success of systems developed
SYSUSE — Use of developed systems
TIME — Curtailing time overruns
TRAINING — Training in using the SDM
USERSATI — User satisfaction
VARIETY — Ability to develop a variety of systems
VERIFICA — Verification procedures
VERSATIL — Versatility of SDM

Table 1 Relative importance of a group of requirements over other groups

<table><tr><td>Group of requirements</td><td>Number of times more important</td><td>Other group of requirements</td></tr><tr><td>Effectiveness</td><td>1.81</td><td>Productivity</td></tr><tr><td>Effectiveness</td><td>1.30</td><td>Versatility</td></tr><tr><td>Effectiveness</td><td>1.20</td><td>Functionality</td></tr><tr><td>Functionality</td><td>1.51</td><td>Productivity</td></tr><tr><td>Functionality</td><td>1.09</td><td>Versatility</td></tr><tr><td>Versatility</td><td>1.39</td><td>Productivity</td></tr></table>

one group of requirements more than the importance of the remaining groups (see Table 1).

Intuitively, one would expect the effectiveness of a SDM to be its most important requirement because the system quality and user satisfaction are major goals of any systems development. Practitioners responsible for developing and maintaining a system are the ones to make suitable modifications when it does not possess the expected quality. This modification process is not only time consuming but also expensive. The fact that organizations have been spending about 40% to 70% of their MIS resources on maintenance activities (Helms and Weiss, 1985) is an indication of the current systems quality and user satisfaction in the industry. Since the general quality of the systems in most organizations is not high and other features of a SDM are only the means to develop good systems, practitioners may have considered effectiveness as the most important requirement of a SDM.

Within the effectiveness group, user satisfaction is considered to be the most important feature followed by system quality, and system success. This agrees well with many research studies that stress the user satisfaction as the goal of systems development (Bailey and Pearson, 1983; Ives et al, 1983) and even use it as a surrogate measure for system quality (Ginzberg 1981a; Prell and Sheng, 1984).

Information systems vary in their sizes with many of them large or medium sized (Jenkins et al, 1984; Mahmood, 1987). They are also complex due to interactions among various components of the system (Belardo and Pazer, 1985). A convenient and feasible method of developing such systems is to follow the systems development life cycle approach which provides for managing the development process in several stages. Such an approach breaks a large and complex system into smaller systems and helps to develop these systems at a reduced level of complexity. It also helps to develop these systems addressing a small number of problems at each stage rather than addressing all of the problems at once. A SDM following the life cycle approach must then support various tasks during each stage of systems development. In addition, the ease of using the SDM procedures is also necessary to realize these objectives. Since these tasks are helpful in developing effective systems, practitioners may have preferred the functionality requirement as the second most important requirement. Within the functionality group, practitioners prefer to have methods to support all stages of development than the ease of using these methods.

It is intriguing to see productivity ranked next to versatility because many research studies have reported a slippage in development schedules, cost overruns, and a large backlog of systems projects (Boehm, 1987; Daly, 1988). Very few research studies have addressed the issue of a SDMs capability to develop a variety of systems (Wasserman et al, 1983). Obviously, practitioners and researchers do not have the same view on the importance of these two requirements.

Several SDMs such as the Jackson system of development (Jackson, 1975) are inadequate to develop a variety of systems. Many SDMs such as STRADIS (1983) address the issue of developing file based as well as database systems but not the issue of developing information systems with data communication facilities. Although the concepts of decentralized and distributed computer systems are well developed, they have not been integrated into any SDM to facilitate the analysis and design of distributed computer information systems. In addition, many organizations are experimenting with expert systems to exploit their potential in solving knowledge intensive problems. The analysis for expert systems needs methods such as protocol analysis which are different from those used in most SDMs. No SDM has evolved or been formalized to include development of such systems. Since only a few SDMs such as user software engineering (Wasserman, 1982) explicitly address the issue of versatility, practitioners may be using a non-versatile SDM to develop a variety of systems. Practitioners facing problems in using current SDMs to develop a variety of systems may view the importance of versatility more than that of productivity. Within the versatility group, the facility to develop systems such as data base systems and distributed computer systems is more important than the facility to develop systems of various sizes.

Within the productivity group, methods such as avoiding faults, curtailing cost, and curtailing time overrun are considered to be more important than methods such as verification.

## Conclusions

This study identified the relative importance of SDM requirements for practitioners. It showed that researchers and practitioners do not have the same priorities for some of these requirements. New systems development methods which address the SDM requirements in the order indicated may gain better acceptance among practitioners. Research projects that purport to produce such new methods will narrow the gap between theory and practice. The relative importance of SDM requirements identified in this study can be used as multiple criteria for evaluating various available SDMs. By identifying the support provided by a SDM for each criterion, one can make a comparative analysis of many SDMs.

## References

Bailey, J.E. and Pearson, S.W. (1983) Development of a tool for measuring and analyzing user satisfaction. Management Science, 29, 530–545.

Belardo, S. and Pazer, H.L. (1985) Scope/complexity: a framework for the classification and analysis of information-decision systems. Journal of MIS, II, 55–72.

Boehm, B.W. (1984) Validating and verifying software requirements and design specifications. IEEE Software, 1, 75–88.

Boehm, B.W., Gray, T.E. and Seewaldt, T. (1984) Prototyping versus specifying: a multi project experiment. IEEE Transactions on Software Engineering, SE-10, 290–302.

Boehm, B.W. (1987) Improving software productivity. Computer, 20, 43–57.

Case, Jr. A.F. (1985) Computer aided software engineering (CASE): technology for improving software productivity. Data Base, 17, 35–43.

Chen, P. (1977) The entity-relationship approach to logical data base design, in The Q.E.D. Monograph Series on Data Base Management (Information Sciences, Wellesley).

Daly, E.B. (1988) Management of software development. IEEE Transactions on Software Engineering, SE-14, 229–242.

Gane, C. and Sarson, T. (1979) Structured Systems Analysis: Tools and Techniques (Prentice-Hall, New York).

Ginzberg, M.J. (1981a) Early diagnosis of MIS implementation failure: promising results and unaccounted questions. Management Science, 27, 459–478.

Ginzberg, M.J. (1981b) Key recurrent issues in the MIS implementation process. MIS Quarterly, 10, 47–59.

Guimaraes, T. (1985) A study of application program development techniques. Communications of the ACM, 28, 494–499.

Halloran, D., Manchester, S., Moriarty, J., Riley, R., Rohrman, J. and Skramstad, T. (1978) Systems development quality control. MIS Quarterly, 2, 1–13.

Helms, G.L. and Weiss, I.R. (1985) Application software maintenance: can it be controlled? Data Base, 17, 16–18.

Ives, B., Olson, M.H. and Baroudi, J.J. (1983) The measurement of user information satisfaction. Communications of the ACM, 26, 785–793.

Jackson, M.A. (1975) Principles of Program Design (Academic, New York).

Jenkins, A.M., Naumann, J.D. and Wetherbe, J.C. (1984)

Empirical investigation of systems development practices and results. Information & Management, 9, 73–82.

Mahmood, M.A. (1987) Systems development methods - a comparative investigation. MIS Quarterly, 11, 293-311.

Olle, T.W., Sol, H.G. and Verrijn-Stuart, A.A. (1982) Information Systems Design Methodologies: A Comparative Review (North-Holland, New York).

Olle, T.W., Sol, H.G. and Tully, C.J. (1983) Information Systems Design Methodologies: A Feature Analysis (North-Holland, New York).

Olle, T.W., Sol, H.G. and Verrijn-Stuart, A.A. (1986) Information Systems Design Methodologies: Improving the Practice (North-Holland, New York).

Prell, E.M. and Sheng, A.P. (1984) Building quality and productivity into a large software system, IEEE Software, 1, 47–54.

Ross, D.T. (1985) Applications and extensions of SADT. Computer, 18, 25–34.

Saaty, T.L. (1980) The Analytic Hierarchy Process (McGraw Hill, New York).

Schneiderman, B. (1984) Response time and display rate in human performance with computers. Computing Surveys, 16, 265–285.

STRADIS (1983) McAuto. Surrey, UK.

Wasserman, A.I. (1982) The user software engineering methodology: an overview, in Information Systems Design Methodologies: A Comparative Review Olle, T.W., Sol, H.G. and Verrijn-Stuart, A.A. (eds) (North-Holland, New York) pp. 591–628.

Wasserman, A.I., Freeman, P. and Porcella, M. (1983) Characteristics of software development methodologies, in Information Systems Design Methodologies: A Feature Analysis Olle, T.W., Sol, H.G. and Tully, C.J. (eds) (North-Holland, New York) pp. 37–62.

Yourdon, E. and Constantine, L.L. (1975) Structured Design (Yourdon, New York).

## Appendix

This research used analytic hierarchy process (AHP) to identify the relative importance of the 31 SDM requirements shown in Figure 1. Practitioners rated the importance of these requirements in a questionnaire supplied to them. The practitioners who participated in the study were from a variety of organizations as given.

Manufacturing 6
Transportation, communications and utilities 2
Finance, real estate and insurance 5
Services 12
Government 2
Total 27

The participants included systems analysts, MIS managers, MIS directors, and vice-presidents of MIS.

A break down of participants according to their designations is given.

<table><tr><td>Systems analyst/Senior systems analyst</td><td>11</td></tr><tr><td>MIS manager</td><td>9</td></tr><tr><td>MIS director</td><td>4</td></tr><tr><td>Vice president/MIS</td><td>3</td></tr><tr><td>Total</td><td>27</td></tr></table>

These participants had a considerable amount of training and experience in systems development. The average of the annual MIS budget of the participants' organizations and the number of employees in their MIS department are given as

<table><tr><td>Average annual budget of the MIS department</td><td>$22.8 million</td></tr><tr><td>Average number of employees in the MIS department</td><td>179</td></tr><tr><td>Average systems development experience of participants</td><td>13.7 years</td></tr><tr><td>Average systems development training of participants</td><td>27.2 weeks</td></tr></table>

To identify the relative importance of the SDM requirements for each participant, a software product called expert choice $^{1}$ was used. This software product employs AHP computational algorithms to identify priorities. If practitioners prefer some requirements more than other requirements, then each participant will have a rank for these. If all participants prefer certain requirements, then a statistical analysis of participants' ranking should confirm it. A two way ANOVA can show whether the participants prefer some requirements more than other requirements. The null hypothesis for this analysis is

$H_{0}$ : The importance of each requirement is equally likely.

The alternate hypothesis is

$H_{a}$ : At least one requirement will be preferred to any other requirement.

The two way ANOVA produced the following results:

<table><tr><td>Source</td><td>DF</td><td>Sum of squares</td></tr><tr><td>Model</td><td>56</td><td>0.18948005</td></tr><tr><td>Error</td><td>780</td><td>0.51122724</td></tr><tr><td>Corrected total</td><td>836</td><td>0.70070729</td></tr><tr><td>Mean square</td><td>F-value</td><td>PR&gt;F</td></tr><tr><td>0.00338357</td><td>5.16</td><td>0.0001</td></tr><tr><td>0.00065542</td><td></td><td></td></tr></table>

Since the F-statistic for this analysis is 5.16, the null hypothesis is rejected at an alpha level of 0.0001. Therefore, practitioners prefer some requirements more

than other requirements and there is a common rank for these requirements.

Each of the participants may have their rank of the 31 requirements. To ascertain the agreement in rankings among the participants, a statistic W called Kendall's coefficient of concordance $^{2}$ can be calculated. If there is a perfect agreement in the rankings for all participants, requirement 1 receives the same rank for all participants, requirement 2 receives the same rank for all participants, and so on, the resulting value of W will be 1. If there is a perfect disagreement among rankings, the value of W will be 0. The analysis produced the following results: Kendall's coefficient of concordance is 0.4962 and PR > F is 0.0001. The value of W and its statistical significance at an alpha level of 0.0001 indicates that there is a moderate agreement among the participants regarding the relative importance of various requirements for a SDM.

The AHP software gives the relative importance of each requirement as a proportion of the sum of importance of all requirements. For example, the importance for the capability of a SDM to improve the productivity by project management is 0.032 and the sum of importance for all requirements is 1. Since geometric mean is appropriate to find the central value of such proportions, the geometric means of the importance of the 31 requirements for the twenty seven participants were calculated. The numbers in the parentheses in Figure 1 represent the geometric means of the relative importance of SDM requirements for all participants.

## Biographical notes

Dr Sakthivel is an Assistant Professor of MIS at Bowling Green State University, USA. He completed his PhD in August 1989 from Syracuse University, USA. His research interests are in systems analysis and software engineering. He has published in the Journal of MIS, Journal of Information Technology, Journal of Systems Management, Management Accounting, and in several national conference proceedings.

Address for correspondence: Sachidanandam Sakthivel, Accounting and MIS, Bowling Green State University, Bowling Green, OH 43403, USA.

$^{1}$ Expert Choice $^{\circledR}$ Reference Manual, (1990) Expert Choice, Pittsburgh. $^{2}$ Wallis, W.A. (1939) The Correlation Ratio for Ranked Data. Journal of American Statistical Association, 34, 533–538.
