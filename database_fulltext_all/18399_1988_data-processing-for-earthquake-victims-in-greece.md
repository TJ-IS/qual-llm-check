---
otero_id: 18399
otero_key: "4NJ82MTZ"
title: "Data processing for earthquake victims in Greece"
authors: "Alexander B. Sideridis; Dimitris A. Stamelos"
year: "1988"
journal: "Information & Management"
doi: "10.1016/0378-7206(88)90019-5"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Data Processing for Earthquake Victims in Greece

Alexander B. Sideridis

Informatics Laboratory, Agricultural University of Athens, 75 Iera Odos, 118 55 Athens, Greece

Dimitris A. Stamelos

National School of Public Administration, 2 Mitropoleos str., 10563 Athens, Greece

The fact that public administration can use computers as an administrative tool has been discussed by many authors. But nobody has previously tried to organize a data processing centre in a deserted city with a chaotic situation prevailing following a catastrophic earthquake. And the problem became more interesting because of the urgency with which a fully automated local administration, a successor of the traditional one, had to be established in order to support restoration and rehabilitation. In this paper, a successful data processing response to the needs of the Messinia prefecture services is briefly described. Emphasis is given on the steps taken to overcome the obstacles that such a situation is likely to raise.

Keywords: Local administration. Data processing in public administration, Information systems. Earthquake confrontation.

## 1. Introduction

On September 13, 1986 a severe earthquake measuring 6.2 on the Richter scale struck the city of Kalamata, capital of the Messinia prefecture, and the nearby region. The number of casualties was large and many buildings were destroyed. The damage was serious and extensive. The situation became worse as several aftershocks occurred in the next few days.

According to official figures, the size of the disaster was as follows:

\- 18 people were killed and 200 were injured.

\- 22,000 buildings were damaged. Of these, 2,500 collapsed, 12,500 were not suitable for habitation, needing major repairs, and the rest (7,000) had lighter damage and needed only minor repairs to make them fit for use.

\- 70% of the schools and 50% of the public buildings were damaged.

\- Roads, telephone communications, the drainage system, and the electricity network all had serious problems.

The wide range of the calamity found local authorities unprepared to cope effectively with the situation. In spite of their hard work, the magnitude of the devastation demanded an organization far beyond the one that existed before, and the prior organization itself had been severely affected because of all the problems in conjunction with the collapse of the local authority's building, etc. An indolent local administration, as is traditional in the area, could not cope with the situation. Furthermore, the old administration could not provide the necessary organizational acumen to provide quick restoration and rehabilitation, except for immediate relief under the existing emergency plan.

![](/api/attachments/4NJ82MTZ/fulltext/images/2326c265a13260f78a5e9a9922ca98e6ad4df1612015fc4cd72067ef6740be12.jpg)  
Alexander B. Sideridis is an Associate Professor in the Informatics Laboratory of the Agricultural University of Athens. He earned his first degree at the University of Athens and his M.Sc. and Ph.D. from Brunel University. He has been involved in many major projects for the establishment of information systems in large public organizations. His current research focuses on information systems design and implementation issues.

![](/api/attachments/4NJ82MTZ/fulltext/images/f057b476f29de0f11b781684d99f88ee074bb3b7453758a240c70fa92152d573.jpg)  
Dimitris A. Stamelos is a computer scientist currently employed in the National School of Public Administration. He earned his first degree in Mathematics and his M.Phil in Computer Science. He has been involved in many projects for the establishment of information systems in various public organizations. His current research is in Office Automation.

After the local and prefectorial authorities had performed this immediate help operation, the following problems remained:

\- How should the damages be registered, repairs estimated, and compensation provided with minimum bureaucracy?

\- How should temporary housing be allocated and what priority criteria should be used?

\- How should business activities (commercial, industrial, etc.) be rapidly restored to prevent the collapse of the local economy? Also, how should emergency stores be distributed and under what priorities and socio-economic criteria?

\- How should local public projects, formulated prior to the disaster, be reevaluated and continued, and what additional information would need to be collected for this?

![](/api/attachments/4NJ82MTZ/fulltext/images/743a4548586563fbc98a5daaa95aabbc925e1e7d50fe808d6baf55d8c6aaa79c.jpg)  
$C_{1}=$ Value of Decision (VoD) as a function of the quantity of Information $C_{2}=$ VoD as a function of time of collecting the Information

\- How should a program be implemented to provide optimal use of any donations?

\- How should the many urgent financial and technical studies be made?

Of course, in such circumstances, a full scale computerization is an unrealistic goal for the short times that the problems dictate; its main prerequisite is time and this is not available. However, the variety of available software for microcomputers and the possibility of organizing a computer centre without extra facilities made it feasible to develop, in a fortnight, an adequate information system.

It is obvious that an objective, fully documented and automated procedure, including a powerful decision support mechanism, could deal effectively with most of these. The question was: how could one make use of today's efficient information tools and facilities in this environment? How quickly could personnel be trained? How could the system provide fast response without the luxury of normal development delays yet with low risk of failure?

\- How should existing and allocated necessities (goods and supplies) be managed?

## 2. Methodology

## Ends / Means Analysis

In a crisis environment, such as the Kalamata's, the usual Management Information System's (MIS) or Decision Support System's (DSS) development cycle [1,2,4,6] does not seem to be applicable. It cannot help people cope with their critical and urgent problems. The administration was confronted with a situation demanding drastic and comprehensive solutions in a very short time. An abbreviated timetable for analysis was required, with a very high Value of Decision (VoD). VoD increases in proportion to the quantity of available information and decreases very rapidly as time goes by. Thus it seems that some optimum quantity of information $(\mathrm{I_c})$ at a given time $(\mathrm{t_c})$ should be defined and collected (see Fig. 1) [3].

To this end, the Ministry of the Interior, responsible for the introduction of new technology to municipalities and prefectures [5], wished to provide the best possible aid. Knowing the exact situation and problems this was imposing, they decided that the only realistic way was a breakdown of the solution into smaller independent tasks. Several types of microcomputers were chosen as simple and realistic tools for implementing the applications.

At that time, IBM Hellas a major computer company in Greece, offered to donate a number of micros and some software. A committee was immediately formed; it consisted of DP experts in the Ministry and from IBM Hellas. The primary goal was defined; it consisted of selecting among the many urgent problems those that could be realistically achieved rapidly. Thus, an information system was designed to provide the following subsystems:

(1) Allocation of housing to satisfy priorities with respect to number of family members, income, state of health, etc.

(2) Co-ordination and supervision of distribution of necessities, taking into consideration the existing constraints that ensure equable operation.

(3) Project management supervision.

(4) Financial analysis.

(5) Goods provision cycles.

(6) Office Automation.

To provide these services, the hardware was:

\- 2 IBM PC XT computers with 512K RAM and 10Mb Hard Disks.

\- 6 IBM PC computers with 256K RAM. (2 with 512K RAM), and

\- 7 IBM Proprinters.

The software consisted of part of the IBM Assistant Series (Writing, Filing, Reporting and Planning).

This set of services was dictated by the donor and time pressures, with application development and staff training time limited to a fortnight. In particular, the IBM Assistant Series is a well known set of programs covering a wide variety of applications, including word processing, spreadsheet, filing, and a facility to create reports. From the beginning, this choice looked suitable. The package is not the best for all applications, but it offers advantages which outweigh this weakness. It is simple and easy to learn; it is consistent across applications and it supports the Greek language.

## Strategic Steps

The approved strategy was immediately implemented as follows:

\- Kalamata was visited and candidates were selected for training in the areas of analysis, office automation, MS-DOS, and system operations. Some of the most competent young people were selected for the execution of this project. Criteria for their being chosen were their willingness to participate in the project, their previous studies, their experience in local authority functions, and their knowledge of English.

\- More particularly, the selection ensured that the candidates would form a coherent team with a variety of specializations in order to be able to take the initiative whenever needed. The chosen persons where all young, well educated (all had University degrees and most also post-graduate studies abroad such as M.Sc degrees). Their backgrounds were as follows: three were economists, two law graduates, two civil engineers, and two political scientists; the team was completed with a technician in electronics. They all seemed ambitious and very willing to contribute to the problems of their city, and at the time of their recruitment for this project were temporary clerks in the prefecture and municipality, suffering more or less the same from the unfriendly bureaucratic environment in these two services. This consisted primarily of senior staff complaints about their abilities, mistrust and fear of new ideas, isolation, and obstacles for initiatives.

\- The projects were selected by visiting the local authorities and picking the most important but feasible ones: i.e, within the limits of the equipment and satisfying the primary goal of being rapidly operational.

\- The selected people were trained in Athens and then sent back to implement the projects.

\- Their progress was monitored through visits and telephone contacts to detect any problem, particularly to overcome reaction against change.

This approach was intended to improve the chance of success. It was considered of paramount importance, because problems arose from the start and new ones occurred in this “ignorant” environment, suspicious of new technology and fearful of any change. Both could have been equally fatal to the operation. In order to counter them, early successes were imperative, for only with understanding and co-operation can projects of this nature succeed.

## 3. Implementation

## Systems Analysis and Personnel Training

The implementation of the project started with a team of analysts from IBM and the Ministry of the Interior visiting Kalamata in October '86 and collecting information about the organizational problems. During the visit several meetings took place with the local authorities; these led to a general understanding and agreement on the important issues for successful execution.

Selection was made of those applications that met the constraints and according to estimates could fit to the configured system. It proved fortunate that the team was able to select young graduates with experience of the local problems and, most important, very good reasons to participate in this project. During that visit, it was agreed that some difficulties in parts of the chosen applications would be cleared up by the authorities before the arrival of the group at the training centre.

The training went as scheduled; within 10 days the training and development course in Athens was completed and the applications were programmed and put on a production level. The course, a very intensive one, was considered a success as the observed results proved that:

\- Its two main objectives were satisfied: Firstly, to train those capable of operating and supervising applications on the PCs, and, secondly, to create the framework for the actual operation.

\- The trainees, most with no previous computer knowledge whatsoever, in spite of meeting some difficulties at the start of the seminar, learnt the needed skills and emerged quite confident at the end.

\- Creation of the framework of the actual information system application was a useful job, as it removed a lot of misunderstandings with regard to the possibilities and limitations of the machines and clarified the aims of each application.

\- Care was taken to face problems instantly and decisively during the seminar. Indeed, one such problem was inconsistency in some of the operations of the software package when using the Greek language. Another environment was installed in the middle of the seminar, involving both hardware and software alterations. Another problem was caused by changes necessary for some of the applications; these needed substantial commitment and overtime from all participants.

## Systems Installation

The computer applications were intended to support local government or prefecture services. Thus the equipment had to be decentralized and installed in many departments.

The systems were installed in Kalamata immediately after the training ended. Members of the DP committee supervised the installation and solved interim problems; this was anticipated and steps were taken to guarantee a smooth start up.

When the PCs had been installed, higher ranking staff, who were unaware of the potential of the machines, started making contradictory demands on the young employees in charge of the microcomputers. It took significant effort by the team to ease the consequent tensions, give explanations of delays to the officers, and yet keep the morale of the operators high.

The following weeks were critical to the fate of the project. The Ministry and IBM team had continuous contact with the operators and the situation improved rapidly once the systems proved successful. Supervisor and other staff saw the value of the machines and started to realize their potential. Only a month after the arrival of the microcomputers in Kalamata, the first three applications were operational and gave valuable information to the authorities about the allocation of temporary housing, restoration of business activities, and management of contributions and various donations. A month later two more applications were working successfully, helping in the management of existing and allocated needs and speeding the preparation of various financial and technical studies.

From the applications planned, they are now all working, with the exception of the one related to the re-evaluation and management of local public projects. In spite of many efforts to make it function, the effort was eventually aborted, because of the strong opposition from another government department that considered itself solely responsible for this team project. The informal undermining actions were successful in this case.

Nevertheless the operation as a whole was a big success. This is obvious by the events in the following few months. Senior officers, who in the past were unwilling to trust the young people and offer them more responsible tasks and also seemed sceptical at the start of the project, were impressed with the potential of these new services when they saw the first results. Their reservations gave place to a rapidly increasing set of expectations and demands. So, when they were asked for an expansion of the system, they instantly agreed! Six more personal computers with hard disks were bought, as well as more sophisticated software (DBase III Plus, Lotus 1-2-3). The team immediately started learning these packages and then used them to meet the new and more complex demands. Such behaviour of the senior staff seems more impressive when it is compared to their earlier observed reservation to sign for inexpensive consumables, like paper and diskettes. Naturally, they moved forward and changed the status of the members of the team, offering them permanency!

Meanwhile, employees from other departments who were suspicious of the dangers of this project (from fear of swift penetration by their junior colleagues), reacted positively when they appreciated the relief and reduction in their workload due to the new technology.

It is obvious that a new situation occurred. Latest reports show that much pressure is being put on the team as more and more managerial projects (from preparation of management reports to common office work) involving bulky data is being requested, but without an increase in the size of the team. However this is a different story, irrelevant to the study, but included as one more sign of the project's overwhelming acceptance and success.

Now in the Ministry of the Interior, a study is underway to exploit computer networking; this is expected to require implementation of new applications as soon as possible.

## 4. Conclusions

We have shown that it is possible to respond rapidly to an emergency by automating the relief process, in spite of substantial lack of experience in modern technology. Taking advantage of the facilities and efficiency of the new information tools is undoubtedly valuable. The experience gained from such projects provides the “how” to accomplish such a task.

Such methodology, with the determination to react after a disaster, may result in the formulation of readiness plans that will provide relief effectively and accelerate the rate of progress to higher levels. In order to achieve this, it is very important to exploit any experience and update the emergency plans to allow instant action. But the contribution and co-operation of the populace will be reduced if there are delays.

A relevant emerging question is: How can something be prepared now to face a similar disaster in the future? It must be obvious from what has been described that the nature of such cases varies substantially from everyday ones. One big difference is in the temporary change in the behavior of the affected people. It is difficult to prepare in advance a team of DP experts, because they will be considered outsiders and alien to the idiosyncrasies of the locals. To repeat the same experiment may work, but it will take time, and this is more than valuable. Is it possible to keep this team, which has both the experience and the knowledge, together and ready to act, with suitable provisions for additional training? This concept is now being considered. Of course the motivation of the team will be different from that which led to the success, and such a difference may prove the most crucial factor in the repetition of this success.

## Acknowledgement

The work described in this paper is based on a project made by the authors at the request of the Greek Ministry of the Interior.

## References

[i] B. Bowman, G. Davis and J. Wetherbe, "Three Stage Model of MIS Planning", Information Management, V6/1, February 1983, pp. 11--25.

[2] E. Mumford, R. Hirchheim, G. Fitzgerald, A. Wood-Harper, "Research Methods in Information Systems", Amsterdam: North-Holland, 1985.

[3] S.D. Ostergaard, “Design of Public Information Systems: I. Principles and Implications” in Computers in Public Administration, Pergammon Press, N.Y., 1976.

[4] V. Saber, Modelling of the Office Procedural Activities", IFIP Conference Proceedings, Budapest, 1987, pp. 156–166.

[5] A.B. Sideridis, "Informatics and Municipalities: The Greek Approach", Report TR1/1986, Ministry of the Interior, Athens, Greece, 1986.

[6] F. Van Assche, P. Layzell, M. Anderson, "RUBRIC: A Rule-Based Approach to the Development of Information Systems", Eurinfo '88 Conference Proceedings, Athens, 1988, pp. 371–378.
