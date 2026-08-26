---
otero_id: 18615
otero_key: "AU4CGAND"
title: "An industry survey of emerging prototyping methodologies"
authors: "E. Reed Doke"
year: "1990"
journal: "Information & Management"
doi: "10.1016/0378-7206(90)90037-i"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# An Industry Survey of Emerging Prototyping Methodologies

E. Reed Doke

Computer Information Systems Department, College of Business Administration, Southwest Missouri State University, Springfield, Missouri 65804-0095, USA

The literature indicates that although the phased traditional systems development approach continues to be used, prototyping techniques are becoming popular. Instead of a single prototyping methodology, however, studies suggest there are several, each with its unique processes and characteristics. These developments raise important questions: which specific methodologies are being used, to what extent are they being applied, and how important are they? A mail survey of the MIS managers in Fortune 1000 firms was conducted to attempt to answer these questions. Four separate methodologies are identified and investigated. Results indicate that over 60% of the respondent organizations are prototyping; all four methodologies are very popular and seen as important to the development of information systems.

Keywords: Prototype, Prototyping Methodologies, Prototyping Methodology Taxonomy, System Design.

![](/api/attachments/AU4CGAND/fulltext/images/0abbb0f156d6e39a1d8f6b1a7a2b7f31e7eac7b57f88201479dbaf1cd9e3edfe.jpg)

E. Reed Doke is an Associate Professor in the Computer Information Systems Department at Southwest Missouri State University in Springfield, Missouri where he teaches programming, MIS and management science courses. Prior to joining the university, he was MIS Manager for a large financial institution. He received his Ph.D. in Management from the University of Arkansas and continues to serve industry as a consultant. He is a member of Decision Sciences Institute, Data Processing Management Association and the Association of Computer Educators. He has recently had articles published in the Journal of Computer Information Systems, Journal of Information Systems Management, Journal of The Academy of Marketing Science and Data Management. In addition, Professor Doke has authored several copyrighted software packages. His current research interests include software design and development issues.

## 1. Introduction

The systems development process has been criticized for years. The literature abounds with examples of development projects that are over budget, behind schedule, and fail to meet user needs and expectations. Often, the traditional system development life cycle (TLC) is blamed. One interpretation of the TLC phases is (1) preliminary study, (2) requirements definition, (3) design, (4) development, (5) implementation, and (6) post-implementation. Although research $[19,22]$ indicates the TLC is still being used in systems development, there is increasing evidence that the phased approach may not be the best way to develop systems, particularly ones with ill-defined requirements and those that represent high costs, risks, and complexity.

Although information systems prototyping techniques have been employed for many years [6], there has been an increase in popularity during the past decade. For example, it was discussed as a heuristic development methodology in 1979 [4] and was seen as a revolutionary change in the system development process as recently as 1982 [20]. Since early days, researchers and practitioners alike have been enthusiastic in their support of prototyping.

It has evolved because of factors such as the availability of new tools (personal computers and fourth generation languages), the trend toward increased user involvement in systems development, and the benefits demonstrated in early prototyping efforts.

Fundamentally, prototyping is a tool that requires user involvement in system development, particularly when defining system requirements. Instead of a single prototyping methodology, there are several, each with its own processes, characteristics, and objectives. At one extreme, prototyping involves the construction of sample screens and reports. At the other, it is an iterative heuristic development process, in which the user guides system design and development by reviewing and interacting with models of the proposed system and making suggestions for its modification and improvement. This process of review and refinement continues until an acceptable operational system results.

An engineering prototype is typically a model created to determine behavior under various conditions. Similarly, a software prototype is a model of a system, or part of a system, created to illustrate how a proposed system will work, demonstrate the developer's understanding of the user's requirements and to solicit feedback from the user. The model may or may not be implemented, depending on its completeness, sophistication and operational efficiency.

Unfortunately, an argument can be made that prototyping is used in the development of systems, whether we recognize it or not. For example, those systems constructed without benefit of a formal prototyping methodology may continue to undergo refinement and modification until an acceptable system emerges (or the user surrenders in total frustration). In other words, the initial two or three systems constructed were in fact prototypes which were finally hammered into an effective operational system.

To extend our understanding of the prototyping phenomenon, we surveyed MIS Managers in Fortune 1000 companies to attempt to answer three main questions: (1) which specific prototyping methodologies exist? (2) to what extent are they being used? and (3) how important are they to system development projects?

## 2. Prototyping Methodologies

Early prototyping efforts suggest prototyping was a single methodology used to supplement the traditional system development life cycle, particularly the requirements definition and design stages. More recent work recognizes the existence of several methodologies, however there is little agreement about a taxonomy.

Table 1  
Prototyping Classification Approaches

<table><tr><td>Category</td><td>Description</td></tr><tr><td>1. Model Type</td><td>Disposable or nondisposable</td></tr><tr><td>2. Model Function</td><td>Mockups of screens and reports, which perform limited system functions, or models that evolve into operational systems.</td></tr><tr><td>3. Model Purpose</td><td>Illustrate system features, produce experimental results, or explore system features, characteristics, and options.</td></tr></table>

## 2.1. Methodologies in the Literature

Our survey suggests three primary ways of classifying prototyping techniques and models: see Table 1.

One author [13] recognizes numerous prototyping methodologies but condenses them into two: disposable and nondisposable. Nondisposable models are those that evolve into operational systems, while disposable ones are discarded when they are no longer needed.

Several researchers $[3,7,8]$ place prototyping methodologies into three categories: (1) mockup prototyping; (2) working model prototyping; and (3) evolutionary prototyping. The first simply creates examples of screens and reports. This technique has, of course, been widely used for many years. The working model methodology produces disposable models that simulate limited system functions, perhaps including interaction with a database. Evolutionary prototyping builds successive models that evolve into a finished operational system. Others also identify three prototyping methodologies: real life, simulated, and a combination of the two. Their work focuses on the similarities between engineering systems and information systems development approaches.

Another study [11] classifies prototyping methodologies into four categories: (1) mockup; (2) simulation; (3) working model; and (4) evolutionary. A distinction is made between simulated and real processing. The working model is a real but incomplete system. Simulation models are disposable, while the working model has potential application in the final operational system.

A more recent study [9] introduces the concept of pilot systems as separate from prototypes. A pilot is an incomplete system similar to a prototype, but while the prototype is disposable and focuses on user interaction and evaluation, the pilot system is more complete and may be implemented.

An architecture-based methodology has also been proposed [18]. This develops a working model based on the external characteristics and appearance of the system. The modeler works inward, adding detail as needed.

It has been suggested that different methodologies should be geared to different types of information systems. For example, mockups are more suitable for transaction processing systems, working models are appropriate for the more interactive information systems and evolutionary prototypes seems to be more useful when developing Decision Support and Expert Systems (where the requirements are not well defined).

Finally, several authors [12,17,21] feel there is only one prototyping methodology using various tools and techniques. In essence they see only two development approaches: prototyping or traditional life cycle, although they agree prototyping is an important tool.

## 2.2. Prototyping Processes

There is some agreement in the literature that prototyping is a 4 step iterative process which overlays the requirements and design phases of the TLC. This is shown in Figure 1. Whenever the prototype appears to be correct, it serves as a design base for development of the complete system. Depending on the type of system and the degree of model sophistication, the model may or may not be implemented.

Others have a somewhat different view based on engineering models $[14,15]$ . They see prototyping as a 3 step sequential process which results in at least 3 models: (1) Construct the initial prototype; (2) Construct a working model; and (3) Construct the operational system. The first step produces the initial prototype which serves to

Fig. 1: Iterative Prototyping Process.

show how the system can work. The second step produces a more detailed working model that manipulates data. The final step concludes with the operational system.

The specific prototyping process is determined, to some extent, by the particular methodology being employed. A mock-up model, for example, could be and probably is constructed with little revision. On the other hand, a heuristic approach will likely require several iterations of evaluation and refinement before the final operational system is produced.

## 2.3. A Taxonomy

These various views suggest the existence of four separate and distinct prototyping methodologies: Illustrative, Simulated, Functional, and Evolutionary. Each has its specific processes, life cycle relationships, objectives, and resulting models.

The purpose of the Illustrative methodology is to produce representative screens and reports for user review. It is a non-iterative process that is used to enhance communication between the user and developer during the requirements definition and design phases. There is little or no interaction. Such techniques have been widely used for years.

While these produce models that look like system reports and screens, Simulated prototyping yields models that act as if they were parts of the desired system. This process is iterative, because the model can be refined and enhanced. It also supplements the requirements definition and design phases of the TLC and produces a disposable model. Simulated models appear to function like part of the system but simulate the interaction with a database.

Functional prototyping is comparable to Simulated prototyping; it provides models that interact with a database but represent a more complete set of system functions. These characteristics enable Functional models to replace a larger part of the design phase in the TLC. They are however, still generally seen as disposable, because they typically lack the operational efficiency and completeness of working systems.

The Evolutionary methodology is used to produce an operational system. The model or models are nondisposable and use either a sequential process producing multiple models or an iterative approach that repeatedly refines a single model. Evolutionary methods tend to replace the traditional life cycle entirely. Evolutionary techniques are more appropriate for systems whose requirements are poorly defined.

Table 2  
Prototyping Methodology Characteristics.

<table><tr><td>Methodology</td><td>Process</td><td>TLC Relationship</td><td>Use Database</td><td>Model Produced</td></tr><tr><td>1. Illustrative</td><td>sequential</td><td>supplements</td><td>no</td><td>disposable</td></tr><tr><td>2. Simulated</td><td>iterative</td><td>supplements</td><td>no</td><td>disposable</td></tr><tr><td>3. Functional</td><td>iterative</td><td>supplements</td><td>yes</td><td>disposable</td></tr><tr><td>4. Evolutionary</td><td>iterative or sequential</td><td>supplements or replaces</td><td>yes</td><td>operational</td></tr></table>

Table 2 gives a comparison of these methodologies and their characteristics.

## 3. Survey Design

The respondents in this study were corporate level MIS managers. Names and addresses of 500 MIS managers in Fortune 1000 companies were randomly selected. An equal number of service and industrial organizations were represented. Survey packages consisting of a personalized cover letter, a 1 page questionnaire, and a postage paid return envelope were mailed to each MIS manager. The survey was conducted during mid-1987.

The questionnaire was designed to determine the prototyping methodologies being employed, if any, and the perceived importance of each to system development projects. In order to orient respondents properly, the following description of prototype models was included on the questionnaire:

A prototype is a model of a system or part of a system that will be developed. Its purpose is to demonstrate system features and to improve communication between the user and developer. A prototype can be as simple as mock-ups of reports and screens or as complete as software that actually does some processing. Prototypes can be built with the intention of discarding them after they are no longer needed or they can become part of the final operational system.

In addition, instead of using specific methodology names in the questions, the following descriptive phrases for each methodology were used:

1. Illustrative:

produces only mockups of reports and screens.

2. Simulated:

simulates some system functions but does not use real data or a database, model not implemented.

3. Functional:

performs some actual system functions and uses real data and/or a database, model not implemented.

4. Evolutionary:

produces model(s) that become part of the final operational system.

In addition to prototyping related information, each firm's industry classification and the size of its system development staff were obtained. Respondents were encouraged to supply comments about their prototyping experiences and to provide their names.

## 4. Survey Results

Usable responses were obtained from 96 firms. Of these, 32% supplied names and 24% provided prototyping related comments. Appendix A summarizes these comments. While the return rate was lower than desired (19.0%), it was not unexpected, and, in fact, it is somewhat higher than similar surveys of this group [16]. In addition, the respondent profile clearly shows a broad cross section of industry categories represented. The sample is quite adequate to meet our limited objectives.

## 4.1. Respondent Profile

The firms were placed into two groups: prototypers and non-prototypers. Overall, 61.4% of the respondents indicated they employed prototype models in their system development projects. Table 3 lists the respondent firms by industry. This classification was determined by the individual responses. The categories shown are those written on the questionnaires by the respondents.

Figure 2 contrasts system development staff sizes for prototypers and nonprototypers. The development staff includes programmers, analysts and managers but excludes operational and clerical employees.

Table 3
Responses By Industry.

<table><tr><td rowspan="2">Industry</td><td colspan="2">Prototypers</td><td colspan="2">Non-prototypers</td><td rowspan="2">Total</td><td rowspan="2">%a</td></tr><tr><td>Number</td><td>%</td><td>Number</td><td>%</td></tr><tr><td>Bank/Finance</td><td>6</td><td>6.26</td><td>2</td><td>2.08</td><td>8</td><td>8.34</td></tr><tr><td>Communications</td><td>1</td><td>1.04</td><td>2</td><td>2.08</td><td>3</td><td>3.12</td></tr><tr><td>Construction</td><td>1</td><td>1.04</td><td>2</td><td>2.08</td><td>3</td><td>3.12</td></tr><tr><td>Hotel/Casino</td><td>2</td><td>2.08</td><td>0</td><td>0</td><td>2</td><td>2.08</td></tr><tr><td>Insurance</td><td>2</td><td>2.08</td><td>1</td><td>1.04</td><td>3</td><td>3.12</td></tr><tr><td>Manufacturing</td><td>26</td><td>27.09</td><td>11</td><td>11.47</td><td>37</td><td>38.56</td></tr><tr><td>Oil</td><td>0</td><td>0</td><td>1</td><td>1.04</td><td>1</td><td>1.04</td></tr><tr><td>Retail</td><td>5</td><td>5.21</td><td>1</td><td>1.04</td><td>6</td><td>6.25</td></tr><tr><td>Service</td><td>1</td><td>1.04</td><td>2</td><td>2.08</td><td>3</td><td>3.12</td></tr><tr><td>Transportation</td><td>2</td><td>2.08</td><td>3</td><td>3.12</td><td>5</td><td>5.20</td></tr><tr><td>Utilities</td><td>6</td><td>6.25</td><td>1</td><td>1.04</td><td>7</td><td>7.29</td></tr><tr><td>Warehouse</td><td>1</td><td>1.04</td><td>0</td><td>0</td><td>1</td><td>1.04</td></tr><tr><td>Wholesale</td><td>0</td><td>0</td><td>3</td><td>3.12</td><td>3</td><td>3.12</td></tr><tr><td>None indicated</td><td>6</td><td>6.25</td><td>8</td><td>8.33</td><td>14</td><td>14.58</td></tr><tr><td>Totals</td><td>59</td><td>61.46</td><td>37</td><td>38.54</td><td>96</td><td></td></tr></table>

a) Does not total 100% because of rounding.

## 4.2. Methodology Popularity

The prototyping firms were asked several questions to determine the specific prototyping methodologies being used. Figure 3 summarizes the popularity of each methodology and Figure 4 shows the percent of system development projects using each methodology.

![](/api/attachments/AU4CGAND/fulltext/images/b1dd12f2866b727c2e1926540f03c884cd27c5bdb5e29634c8c13e65410f85d5.jpg)  
Fig. 2. System Development Staff Size (Mean Number, Standard Deviation: Prototypers 324, Non-Prototypers 191).

![](/api/attachments/AU4CGAND/fulltext/images/955d03db0e377bfe2170d5c5137fc28f2fa0e6722141e1150defa77781780ab9.jpg)  
Fig. 3. Methodology Popularity (Percent of Prototypers Using Each Methodology).  
TYPE OF METHODOLOGY

TYPE OF METHODOLOGY  
![](/api/attachments/AU4CGAND/fulltext/images/e655ed9bfdb607f73d65c83a10f6d5cfb1b0dd46e8174ec31f79e504e5a667ad.jpg)  
Fig. 4. Methodology Utilization (Percent of Development Projects Using Each Methodology).

![](/api/attachments/AU4CGAND/fulltext/images/7b8d4aef2daac140df7ebeadb8d3283ff6f0da5c6222b03fb29162f77c8a01ba.jpg)  
Fig. 5. Methodology Importance (To System Development Projects).

## 4.3. Methodology Importance

In addition, questions were included to determine the perceived importance of the various methodologies to system development projects. Figure 5 shows the overall perceived importance of the four methodologies.

## 5. Discussion and Summary

This study focused on determining the popularity and perceived importance of four prototyping methodologies. The results show all four are both widely used and important to system development projects.

## 5.1. Prototyping Activity

It is quite impressive that over 61% of the firms participating in this survey reported using prototype models. This is a much higher figure than has been reported in previous research. For example, a 1981 study of the Fortune 1000 group, reported only 33% of the survey respondents had used prototype models while 16% were planning to use prototyping in the future. Of course, the changing definition of prototyping models plus the fact that the respondents were not necessarily the same could account for some of the variation, nonetheless, there has been a dramatic increase in the use of prototyping techniques. The 1981 survey defined prototyping as an incomplete system. This study following the literature, described prototype models more broadly, ranging from screen and report mock-ups to functioning software.

This survey went to relatively large firms, the Fortune 1000 group. Intuitively, less prototyping would be expected in smaller organizations with fewer resources. In fact, results here suggest larger firms are more apt to apply prototyping tools to system development projects. The mean system development staff size was 269 for prototypers and only 125 for non-prototypers. The larger organizations would be expected to have more resources which would enable them to acquire the tools necessary to apply prototyping techniques.

In terms of popularity, it is not surprising that Illustrative models are being used by the majority of the prototyping firms (77%) and they are being used in 39.7% of the software development projects. What is somewhat surprising is the relative popularity of the other methodologies. They are being employed by over 60% of the firms in over 24% of their projects. Plainly, all four methodologies are being widely used in those organizations that prototype. In fact, Evolutionary models are used by 71% of these firms in 31% of their projects.

## 5.2. Prototyping Importance

Although the overall importance of prototyping to system development projects was anticipated, the very high rating given the Evolutionary methodology is somewhat startling. This methodology produces operational models. The high importance, 5.3 on a 7 point scale, coupled with strong popularity, 71% of the prototypers use this methodology in 31% of their projects, strongly suggests the Evolutionary methodology is having a significant impact on system development projects.

Simulated models, on the other hand were ranked as least important, 3.9, and were used in only 24.2% of the system development projects. Apparently the use of real data makes the Functional methodology more valuable.

## 5.3. Summary

Four unique prototyping methodologies have emerged since the early 1970's: (1) Illustrative; (2) Simulated; (3) Functional; and (4) Evolutionary. Each has been described in terms of its processes, its impact on the traditional life cycle, and the type of model produced. The first three methodologies produce disposable models to support the requirements definition and the design phases of the TLC. The Evolutionary methodology tends to replace the traditional life cycle by producing prototype models that become operational systems. The results of this study indicate that prototyping has become an important and popular tool, and that each of the methodologies are being widely used.

This survey intentionally dealt with the relatively large firms. Obviously, it is important to study prototyping in smaller organizations. In addition, a larger sample is required to draw more precise conclusions.

The software development process continues to undergo change as new tools and methodologies evolve in a very dynamic environment. In addition to answering questions about the usage and importance of prototyping methodologies, this research has raised additional important questions:

1. When should the various methodologies be used?

2. What is the impact of the methodologies on the traditional life cycle?

3. Is it appropriate to employ multiple methodologies concurrently?

4. As tools such as 4GLs become more popular and operationally efficient, what is the expected impact on the prototyping methodologies?

## Appendix A

## Summary of Respondent Prototyping Comments

Comments Made by Firms not currently using prototyping:

1. We are currently considering prototyping tools for installation this year.

2. We are evaluating types of tools we should be using to develop systems.

3. We are interested in prototyping techniques and are looking at how we might introduce that process into our design methodology.

4. We will use prototyping more extensively in the future.

5. We recognize the need for prototyping.

6. We do some data modeling but no prototyping, although they would compliment each other.

Comments Made by Firms using prototyping:

1. Prototyping is the KEY to our success.

2. The prototype can often evolve into the final system which saves development time.

3. We are using prototyping primarily on a large single project. Thus far, our experiences are encouraging, though by no means conclusive.

4. We have been using prototyping techniques for the past 2 years. As new projects are initiated, the technique is incorporated where possible.

5. We have found prototyping to provide important benefits.

6. Most of what we call prototyping is really trial and error using COBOL... not very efficient.

7. We do not follow a formal methodology but have used the concept for years.

8. We will use prototyping more in the future.

9. All of our systems have mockups of input and output.

10. When developing systems for management, the prototype is almost always the beginning.

11. We use prototyping in virtually all of our systems development work and have found the technique to reduce implementation risks and to reduce overall implementation time frame.

## References

[1] “Working Conference on Prototyping,” Information & Management, Vol. 7, No. 3, June 1984, pp. 149–156.

[2] Alavi, M. "An Assessment of the Prototyping Approach to Information Systems Development," Communications of the ACM, Vol. 27, No. 6, pp. 556–562.

[3] Adamski, L. "The Prototyping Process," Systems International, Vol. 13, No. 6, 1985, pp. 91–92.

[4] Berrisford, T.R. and Wetherbe, J.C. "Heuristic Development: A Redesign of Systems Design," MIS Quarterly, Vol. 3, No. 1, 1979, pp. 11–19.

[5] Boar, B.H. “Application Prototyping: A Life Cycle Perspective,” Journal of Systems Management, Vol. 37, No. 2, 1986, pp. 25–31.

[6] Canning, R.G., “That Maintenance Iceburg,” EDP Analyzer, No. 10, 1972.

[7] Cerveny, R.P., Garity, E.J. and Sanders, G.L. "The Application of Prototyping to Systems Development: A Rationale and Model," Journal of Management Information Systems, Vol. 3, No. 2, 1986, pp. 52–62.

[8] Harrison, R. "Prototyping and the Systems Development Life Cycle," Journal of Systems Management, Vol. 36, No. 8, 1985, pp. 22-25.

[9] Janson, M.A. "Applying a Pilot System and Prototyping

Approach to Systems Development and Implementation," Information & Management, Vol. 10, No. 4, 1986, pp. 209–216.

[10] Janson, M.A. and Smith, L.D. “Prototyping for Systems Development: A Critical Appraisal,” MIS Quarterly, Vol. 9, No. 4, 1985, pp. 305–316.

[11] Johnson, J.R. “A Prototypical Success Story,” Datamation, Vol. 29, No. 11, 1983, pp. 251–256.

[12] Kauber, P.G. "Prototyping: Not a Method but a Philosophy," Journal of Systems Management, Vol. 36, No. 9, 1985, pp. 28-33.

[13] Klingler, D.E. “Rapid Prototyping Revisited,” Datamation, Vol. 32, No. 20, 1986, pp. 131–132.

[14] Kraushaar, J. and Shirland, L. "Prototyping Information Systems on Microcomputers: A Design Philosophy For Engineering Management," Engineering Management International, Vol. 3, No. 2, 1985, pp. 73–84.

[15] Kraushaar, J. and Shirland, L. "A Prototyping Method for Application Development by End Users and Information Systems Specialists," MIS Quarterly, Vol. 9, No. 3, 1985, pp. 189–197.

[16] Langle, G.B., Leitheiser, R.L. and Naumann, J.D. "A Survey of Applications Systems Prototyping In Industry," Information and Management, Vol. 7, No. 5, 1984, pp. 273–284.

[17] Mahmood, M.A. “System Development Methods – A Comparative Investigation,” MIS Quarterly, Vol. 11, No. 3, 1987, pp. 293–311.

[18] Mason, R.E.A. and Carey, T.T. "Prototyping Interactive Information Systems," Communications of the ACM, Vol. 26, No. 5, 1983, pp. 347-354.

[19] McKeen, J.D. “Successful Development Strategies for Business Application Systems,” MIS Quarterly, Vol. 7, No. 3, 1983. pp. 47–65.

[20] Naumann, J.D. and Jenkins, A.M. “Prototyping: The New Paradigm for Systems Development,” MIS Quarterly, Vol. 6, No. 3, 1982, pp. 29–42.

[21] Whitten, J.L., Bentley, L.D. and Ho, T.I.M. Systems Analysis & Design Methods, Times Mirror/Mosby College Publishing Company, St. Louis, 1986.

[22] Willis, G.W. “Empirical Study of the System Development Life Cycle,” Proceedings of the Southwest Decision Sciences Institute Meeting, Houston, Texas, March 12–13, 1987.
