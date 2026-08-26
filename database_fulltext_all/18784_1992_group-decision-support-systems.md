---
otero_id: 18784
otero_key: "VVCKKWP3"
title: "Group decision support systems"
authors: "Mohamed A. Nour; David (Chi-Chung) Yen"
year: "1992"
journal: "Information & Management"
doi: "10.1016/0378-7206(92)90008-4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# Group decision support systems Towards a conceptual foundation

Mohamed A. Nour

Kent State University, Kent, OH 44242, USA

David (Chi-Chung) Yen

Miami University, Oxford, OH 45056, USA

Group decision support systems (GDSS) have been the focus of extensive research studies over the last decade. These, however, have largely been experimental in nature and dealt mainly with students in laboratory settings. Although the significance of these studies are not questioned, the findings have sometimes been conflicting. Further, the study of GDSS is currently lacking a real conceptual foundation. This paper is an attempt to contribute to the building of a foundation for the study, design, and implementation of GDSS. An integrated framework is presented; it is sufficiently comprehensive to embody the fundamental elements of the GDSS' complex environment. Within this framework, particular emphasis is given to the social and interpersonal variables and their impact on communication requirements. The implication for the design and implementation of the GDSS is discussed.

Keywords: Group decision making, Group problem-solving, Group decision support systems (GDSS), Decision support systems (DSS)

![](/api/attachments/VVCKKWP3/fulltext/images/7c1e4d081393cc3f71f7710b2d3a7a5daa3c9ef6b5b75f2f3753d4364b6eba90.jpg)

Mohamed A. Nour is currently doing his Ph.D. in Business Administration, with a concentration in MIS, at the Graduate School of Management, Kent State University, Kent, OH. He holds an M.B.A. (with MIS concentration) and a Master's degree in accountancy from Miami University, Oxford, OH. Mr. Nour graduated from the University of Khartoum, Khartoum, Sudan, with a B.S. in Business Administration with a concentration in accounting. Afterwards, he worked for a year in the Auditor General Chamber of the Republic of Sudan before joining the School of Management Studies of the University of Khartoum as a teaching assistant. His research interests include decision support systems, databases and data communications.

## 1. Introduction

In recent years, research interest has focused on computer-based decision support systems that model and assist in group problem solving. These systems, known as group decision support systems (GDSS), combine communication, computer, and decision technologies to support problem formulation and solution in meetings. A number of significant studies have appeared over the last decade $[1,12,27,29,32]$ , these have generally followed two directions.

First, a disproportionately large number of these studies have tended to focus on the practical aspect of group decision support systems (e.g. [9,19,22]), with little attention being paid to the theoretical underpinnings of GDSS. Numerous laboratory experiments (e.g. [28,36]) have been conducted to study and evaluate the actual outcomes of GDSS implementation. Although these studies vary in terms of experimental software used, the types of decisions involved, the degree of experimental rigor, and measurement sophistication, the findings suggest that GDSS can indeed improve the quality and effectiveness of group decision making.

Unfortunately, the methodology and research settings used suggest caution in interpreting their results. Moreover, some conflicting findings have emanated from these studies. For example, a number of researchers concluded that GDSS did improve the quality of the decision and the satisfaction of the group members. On the other hand, Gallupe et al. [10] and Watson et al. [33] have reported contrary results. These authors have found that GDSS offered little advantage over paper-and-pencil support for smaller decision-making groups.

![](/api/attachments/VVCKKWP3/fulltext/images/a0f94912641e2650c23c4863e2879b43cb46eb7a119aa69cca19c3a8e1b6e3fe.jpg)  
David (Chi-Chung) Yen is an Associate Professor of Management Information Systems in the Department of Decision Sciences, School of Business Administration, Miami University, Oxford, OH. His current research interests include MIS/DSS, data communications, data bases, expert systems, and systems analysis and design. His published work has appeared in Communications of the ACM, Information and Management, and Interface.

A review of research studies indicates that they suffer from some inherent limitations. Some have been reported by Jarvenpaa et al. [15] which include:

1. Focus on small groups: Some prior research generally used small groups (three to four persons), when in fact the impact of the GDSS technology is likely to be greater in larger groups.

2. Focus on students: Some existing research used students, who were generally naive users of the technology and computers, as group participants.

3. Focus on single meetings: Some previous studies used single-meeting experiments, where insufficient opportunity was offered group members to understand and learn to use the technology.

4. Mismatch between tasks and technology: Particular decision tasks may call for specific GDSSs. This fact may have been ignored by prior researchers.

5. Emphasis on “decision rooms” as a whole: Prior studies tended to study the “decision room” environment as a whole, instead of isolating and studying individual components of the decision room technology.

It appears, from the above, that practical GDSS research has been limited in scope as well as methodology. Further, this seems to have dominated the GDSS research in general.

Second, there is apparently a dearth of research in the theoretical foundations of group decision support systems and, to our knowledge, the only study which comprehensively examined it is by DeSanctis and Gallupe [7]. They examined a conceptual foundation based on an information-exchange perspective of decision making. Other theoretical studies include Bonczek et al. [3], Rathwell [24] and Steeb and Johnson [26]. Bonczek et al. presented a conceptual framework that examined the cognitive processes of human decision-makers and described its application to organizational decision making. Rathwell examined a distributed decision-making environment and identified requirements in terms of communication structures to support group planning and decision making activities. Finally, Steeb and Johnson presented a conceptual design of an interactive GDSS. Table 1 provides an overview of these two research directions.

Table 1  
Summary of previous research.

<table><tr><td>Experimental/field research Author(s)</td><td>Conceptual research Author(s)</td></tr><tr><td>Gallupe and DeSanctis (1988)</td><td>DeSanctis and Gallupe (1985)</td></tr><tr><td>Gallupe and McKeen (1990)</td><td>Jelassi, Tawfik M. (1987)</td></tr><tr><td>Jarvenpaa et al. (1988)</td><td>Liang, Ting-peng (1988)</td></tr><tr><td>Kull, David J. (1982)</td><td>Wang and Sheen (1989)</td></tr><tr><td>Nunamaker et al. (1987)</td><td></td></tr><tr><td>Steeb and Johnson (1981)</td><td></td></tr><tr><td>Straub and Beauclair (1987)</td><td></td></tr><tr><td>Straub and Beauclair (1988)</td><td></td></tr><tr><td>Sutherland and Crosslin (1989)</td><td></td></tr><tr><td>Watson et al. (1988)</td><td></td></tr><tr><td>Zigurs et al. (1988)</td><td></td></tr></table>

As Table 1 indicates, there is an imbalance in GDSS research, with emphasis on their practical aspects. The conflicting results emanating from previous studies indicate that we still do not really understand the theoretical underpinnings of GDSS, which has a complex and interdisciplinary nature.

## 2. Definition and taxonomy of GDSS

## 2.1 Definition of GDSS

A broad definition of a group decision support system (GDSS) is: any technology which can be used to enhance group decision making. Huber $[13]$ defines it in terms of functional components as a set of software, hardware, language components, and procedures that support a group of people engaged in a decision-related meeting. DeSanctis and Gallupe $[6]$ define it as an integrated computer-based system that facilitates solution of semi- and un-structured problems by a group of people that have a joint responsibility for making the decision. A National Science Foundation workgroup defined GDSS as the application of information technology to support the work of groups with a focus on improving group performance and organizational effectiveness [31]. While Huber's definition emphasizes GDSS components, DeSanctis and Gallupe focus on what the GDSS can do – a task-oriented definition. The definition by the NSF workgroup, on the other hand, emphasizes the role of the GDSS on improving group performance and organizational effectiveness.

![](/api/attachments/VVCKKWP3/fulltext/images/a6c2eb12f9aeaa095dc9af8d1ead4387ee942ced9bc26d54ff1375425cfada4b.jpg)  
Fig. 1. The evolution of GDSS (Source: Gray and Nunamaker [11]).

A more comprehensive definition is offered by Bui and Jarke [4]. They define a GDSS as a computer-based system that aims at supporting a collective problem-solving process in which:

two or more persons are involved (i) each of whom is characterized by his or her own perceptions, attitudes, motivations, and personality; (ii) who recognize the existence of a common problem; and (iii) who attempt to reach a collective decision.

This definition is particularly relevant for our purposes.

## 2.2 GDSS and DSS: Unlikely twins?

The GDSS seems to have spun off the traditional decision support systems (DSS). On the other hand, a DSS may be regarded as a special case of GDSS, because a GDSS theoretically can support one decision-maker. Gray and Nunamaker [11] describe both views.

The first is that the “GDSS is an emerging subfield within DSS in which there has been a marked increase in activity since the mid-1980s.” They claim that GDSS emerged only recently and has evolved rapidly. Figure 1 presents their view of the evolution of GDSS.

The second view regards GDSS as broader in scope than DSS, and, in moving from a DSS to GDSS, additional requirements are introduced.

Table 2  
Comparison of GDSS and DSS.

<table><tr><td>Attributes</td><td>GDSS</td><td>DSS</td><td>Comments</td></tr><tr><td>Communication capabilities</td><td>Strong</td><td>Limited</td><td>GDSS has too strong comm. capabilities because of its multiuser nature</td></tr><tr><td>Model base</td><td>Yes</td><td>Yes</td><td>Enhanced in GDSS to provide voting, ranking, etc.</td></tr><tr><td>Reliability</td><td>Yes</td><td>Yes</td><td>More system reliability in GDSS is needed to handle group activities</td></tr><tr><td>Physical setup</td><td>Yes</td><td>Limited</td><td>Enhanced in GDSS</td></tr></table>

Source: Gray, Paul and Nunamaker [11].

These distinguishing characteristics are depicted on Table 2.

## 2.3 Taxonomy of GDSS

Gallupe and DeSanctis [9] classify GDSS into three levels, depending on their technical features and the level of support they provide the decision-making group:

1. Level-1 are basically communication media providing technical features aimed at removing communication barriers.

2. Level-2 (enhanced) provide decision modeling and group decision techniques aimed at reducing uncertainty in the group's decision process.

3. Level-3 are even more powerful and can include expert advice in selecting and arranging the rules to be applied during the decision-making process. In other words, they are more like “group” expert systems.

Obviously, level-3 GDSSs seem to hold the greatest promise. This taxonomy seems particularly relevant to us because of our contingency approach. In other words, the three levels fit different circumstances and different user needs. Although any decision-making group may need the services of the three types of GDSSs, they probably differ as to how much or how important each of these services is to their decision making performance.

![](/api/attachments/VVCKKWP3/fulltext/images/f205e4e74be2a804f920932decf21dcb2a6278c2ac3aa3537b7b249510e8001f.jpg)  
Fig. 2. Taxonomy of GDSS (Source: DeSanctis and Gallupe [7] and Jelassi and Beauclair [16]).

However, we have an important reservation about this taxonomy: these three levels are not mutually exclusive. Any GDSS should have a varying degree of these capabilities, depending on the group, decision task, situational, and other factors.

Table 3
GDSS configurations.

<table><tr><td>GDSS Type</td><td>Characteristics</td><td>Significance</td></tr><tr><td>* Computerized</td><td>* Small group</td><td>* Limited</td></tr><tr><td>* Decision Room</td><td>* Close proximity* Face-to-face</td><td>* Dispersed groups are not supported</td></tr><tr><td>* Legislative Session</td><td>* Large group* Close proximity* Face-to-face</td><td>* Limited comm. capability* Differs from first in group size only</td></tr><tr><td>* Local Area Network</td><td>* Small group* Locally dispersed</td><td>* More comm. capabilities* Lacks face-to-face interaction</td></tr><tr><td>* Wide Area Decision Network</td><td>* Small group* Remotely dispersed* Non-face-to-face</td><td>* Similar to one above* Extended comm. capab.* Lacks face-to-face interaction</td></tr><tr><td>* Computer-mediated Communication</td><td>* Larger group* Remotely dispersed* Non-face-to-face</td><td>* Enhanced comp. comm. capabilities* Maximum group support* Lacks face-to-face communication.</td></tr><tr><td>* Remote Site Teleconferencing</td><td>* Larger group* Remotely dispersed* Face-to-face</td><td>* Ideal GDSS* Maximum comm. capab.* Lack of technology support</td></tr></table>

A more practical and generic taxonomy rests on the combinations of dimensions representing the size of the group, geographical, and “visual” proximity. These variables are dichotomized so their combinations will result in eight possibilities. These are depicted in Figure 2.

This paper posits that the design of GDSS ought to be robust and flexible enough not only to cover all practical possibilities but also to anticipate the potential future uses of the technology. Table 3 presents a description of the different GDSS configurations [e.g., 16].

Electronic Meeting Systems (EMS) purport to combine the capabilities provided in different dedicated GDSSs, such as those in Table 3. While these GDSSs represent independent systems, our conceptual model would include their combined capabilities as inputs in designing EMS.

## 3. A conceptual model of GDSS design

The effective functioning of group decision support systems depends largely upon their appropriate design and use by the decision-making group. The appropriate design of GDSS is, in turn, a function of our understanding of the technology, its conceptual foundations, and its appropriate uses. The study of DSS must be based upon a conceptual framework of decision making. However, the study of GDSS draws upon seemingly unrelated disciplines, including computer science, psychology, sociology, and linguistics.

## 3.1 Nature of group decision making

As a person moves from being a solitary decision maker to a participant in a group decision making process, complications occur. In fact, the nature of the decision-making process radically changes, since he or she now must interact with the other group members, all participating simultaneously and, perhaps, equally in the process. The following are some of the group-induced changes:

1. The individual's behavior pattern will change, being affected by interpersonal interactions.

2. The decision-making process itself will change, reflecting the nature of group processes, perceptions, motivations, and participation.

3. The communications requirements will increase, reflecting the need for communication between group members, the system and each member, and the system and the group as a whole.

Other significant issues also come into play when dealing with the group, as opposed to individual decision-making.

Task: In a group decision-making environment, the task tends to be more complex, difficult and critical in terms of its consequences and impact on the organization. Planning and other strategic decisions, for example, have substantial bearing on the organization's well-being.

In delegating the decision task to a group, a question arises: is the objective to diffuse responsibility for the decision and place it equally on the shoulders of all members. However, it might not be desirable to diffuse the responsibility for some decisions. In fact, the business as well as the political environments generally discourage diffusion. A division manager in Ford Motors, for example, is held solely responsible for the performance of the division, since he or she is given the authority to effect such performance. This is true notwithstanding the fact that there may be many group meetings in a year to tackle the critical issues in managing their division.

The tendency is to assign unique responsibilities to each individual in order to motivate them to perform the best they can.

Equal Participation: The literature seems to suggest that members in a decision-making group participate equally, and that this is always desirable. We argue against this. Indeed, some members may have the authority to override (veto) the consensus of the group. Of course, such an act may have a negative effect on the members' satisfaction and affect any future cooperation; however, it could be a valid outcome due to the final decision of the chief executive. No one would expect, for example, the CEO of a Fortune 500 company to have equal participation in a meeting with his vice presidents.

## As Kiesler et al. [17] clearly indicate:

…equal participation, objectivity, and efficiency sometimes interfere with important group outcomes. To be effective, rather than encouraging equal participation, group members may need to organize themselves by discovering sources of information, deciding who can be depended on, distributing work to those people, and protecting their autonomy.

This view recognizes the fact that some group members may have more knowledge, competence, and experience than others in dealing with the problem. We argue for “equity” of participation, with some individuals being allowed to have more say because of their authority, expertise, and knowledge.

Furthermore, consensus has not been shown to be correlated with the quality and accuracy of the decision $[25]$ , which is the overriding concern in getting the task done. Thus, if the decision at hand is crucial and critical to the survival of the organization, the question of consensus loses significance.

## 3.2 A conceptual framework

A systematic and logical framework can help to focus attention on the complex variables that bear upon the effective design and use of GDSS. Figure 3 presents a framework for analyzing these variables.

There are four fundamental elements in this model: (1) the decision making body (as individuals or group), (2) the decision task, (3) the organizational fit, and (4) the GDSS. We see the relationships between these elements as inherently intricate, complicated further by exogenous factors that are also critical to effective design and functioning of the GDSS.

![](/api/attachments/VVCKKWP3/fulltext/images/40a65437d5fdfbb4c1b9988374cf9f3652b109769e31fba353fa20f76ecea5d5.jpg)  
Fig. 3. Conceptual model of GDSS.

![](/api/attachments/VVCKKWP3/fulltext/images/a831737f7952fac14b01723e8260da31827764f61ff097b7440d9ff46e73db4d.jpg)  
Fig. 4. Impact of group and individual factors on communication requirements.

## 3.2.1 The decision making group

Figure 4 shows three interrelated elements: (1) personal factors, (2) group factors, and (3) the group decision-making process. Personal factors are those of each member in the group. They include competence, expertise, knowledge, and psychological factors, such as perceptions, motivation, preferences, and attitudes.

Group factors include its structure, size, leadership style, roles, norms, etc. Individual and group factors directly influence both the group decision process and its communication requirements, which, in turn, affect the design of the GDSS. There are three types of group problem solving: (1) the interacting group technique, (2) the nominal group technique, and (3) Delphi techniques. Deindividuation, group pressure for consensus and diffusion of responsibility are alternative factors to be considered.

## 3.2.2 The decision task

Figure 5 shows the decision task as influenced by management and the decision-making group. Management factors represent the demands of top management on the nature and the requirements of the task. Top management, for example, may determine the type, nature, and level of the task. The decision can be strategic or operational, depending on circumstances, induced partly by the environment and partly by management objectives and goals. It also can be planning, crisis management, routine decision making, etc. On the other hand, group preferences, politics, etc, may also influence the task.

The cumulative impact of these factors is reflected in the requirements, which can include criteria for completion, goals, and time limits, i.e. what, how, and when to finish.

## 3.2.3 Organizational fit

Figure 6 describes the nature of the environment in which the organization operates, its management, and situational factors. Environmental factors include: degree of uncertainty, rate of change, complexity, hostility, etc. Top management's style, philosophy, needs, and demands all have a bearing on how problems are solved, who should solve them, and to whom decision tasks may be entrusted. Situational factors are attributes of the organization at the time of the decision making and may include factors that triggered the decision task. There may be a crisis situation (e.g. takeover attempts), “turn around”, merger, etc. Situational factors impact not only the decision requirements, but also the group’s preferences and latitude in choosing between alternatives.

![](/api/attachments/VVCKKWP3/fulltext/images/8925db4c4767dd86af95828734685539472e04f5164b0c2ce1c76788ea959ec6.jpg)  
Fig. 5. Impact of management and group factors on nature of task.

![](/api/attachments/VVCKKWP3/fulltext/images/4e55a06515e2b1e3cf5f8febeb8ae2c4b1a3c9a28552be407b7086519d44ff71.jpg)  
Fig. 6. Impact of organizational factors.

The combination of these three factors determine what we term organizational fit: the convergence of the needs of the organization and its GDSS.

## 3.2.4 The GDSS

As previously discussed, the GDSS should be the product of the influence of three factors: (1) decision requirements, (2) communications requirements, and (3) organizational fit. These three are, themselves, a function of the other variables.

GDSS technology can actually change the decision making process, for example the speed of consensus or quality of the decision. Thus, the relationship between the decision task, including any constraints, and the GDSS is critical to its design.

On the other hand, level-1 GDSSs are intended to improve the process of group decision-making by eliminating communication barriers between the group members. The GDSS technology can therefore affect the pattern of interpersonal communication and this will ultimately influence the decision quality and other outcomes. Our model assumes that the relationships between communication requirements and the ultimate GDSS is also critical in its design.

## 3.3. Implications for the GDSS design

It seems that there are three important issues of importance in GDSS design.

First, unlike a DSS, a GDSS design is constrained by at least two important considerations: (1) it must be more powerful and robust to deal with group decisions, which are generally more critical; (2) it has to be flexible enough to provide the needed group communication support and foster productive group decision-making.

Second, its design is a function of numerous and complex variables. These, by their nature, have varying degrees of influence from one organization to another. The contingency approach appears to be at odds with most of the literature. Experimental studies in GDSS implementation rarely describe the significance and differential impact of using a particular GDSS software in their experimental settings. One of the possible reasons for this may be that few places can afford more than a single environment with one set of software. However, some places like University of Arizona have several, and report on it. In any case, there has to be a fit between not only the GDSS and the decision task, but also the GDSS and the decision-making group, and the GDSS and the needs of the organization.

Third, the task to be supported by the GDSS should not be viewed as a specific or one-time task, but rather as a description of one of the tasks faced by the organization and its decision-making group. Otherwise the GDSS would be extremely limited and dependent on that specific task.

To be successful, the design of a GDSS should be viewed from a wider perspective that includes the factors examined in our conceptual model.

## 4. Implementation issues

## 4.1. Design and implementation

Implementation implies putting the GDSS to work with a particular decision-making group. It is important to note the interdependent nature of the design and implementation of the GDSS. Some implementation issues and problems may actually have to be dealt with even before the GDSS development starts in house or outside.

## 4.2 Planning for implementation

Four important issues have to be considered as part of planning for the GDSS acquisition and implementation [8]:

1. Identifying the decision to be made.

2. Identifying the decision-making group.

3. Outlining the deficiencies in the present process.

4. Determining the desired improvement in decision outcomes.

The first issue to consider is the decision task, which should not be viewed too narrowly. Likewise, the group to be supported need not necessarily be a specific group, rather it should be an institution that participants can join or leave. In other words, the GDSS should be ready to serve any group of people in the organization.

An important consideration also is the expected benefit from the GDSS: improvement in the decision making process. The investment in GDSS, being high, has to be justified and a cost/benefit analysis may be needed.

## 4.3 Managing change

Organizations are natural foes of change. On the other hand, computer information systems are, by their very nature, vehicles of change. There is therefore always a potential for conflict during the implementation of a computer-based information system.

It seems to be generally assumed that every member in a decision-making group would like, or at least not object to, GDSS support. Although that may be true sometimes, it remains to be shown that it always is. The nature of the decision-making group is as varied as the decisions. Moreover, members are not always given a choice.

Table 4
Current GDSS in operation.

<table><tr><td>GDSS</td><td>Organization</td><td>Capabilities</td></tr><tr><td>SAMM</td><td>University of Minnesota</td><td>System allows individual members to decide what is shown on public screen. This system was designed primarily to support small group meetings.</td></tr><tr><td>Claremont</td><td>Claremont</td><td>Touchscreens used for participant&#x27;s input.Majority of typing done by chauffeur. Chauffeur guides meeting through “choice-making” software.</td></tr><tr><td>COLAB</td><td>Xerox Parc</td><td>Various tools (ala PLEXSYS) guide participants toward group consensus. These tools are being tested here to observe their effects on group meetings.</td></tr><tr><td>NICK</td><td>MCC</td><td>Only basic GDSS capabilities available.Primarily used as a testing ground for level - 1 of GDSS satisfaction among participants.</td></tr><tr><td>Capture Lab</td><td>EDS Corp.</td><td>Very basic configuration consisting of electronic blackboard and participant input terminals. Created mainly to study human behavior in meetings.</td></tr></table>

Sources: Nunamaker [21].

## 4.4 Make or buy

Every GDSS should ideally be unique in its design to fit the particular needs and circumstances of an organization, but this has a very important implication: should it be developed in-house or outside?

From Table 4, there are really no commercial off-the-shelf GDSS's, and if there were, would they meet the requirements of the organization? Moreover, the organization may not be able to develop an in-house GDSS. Risk is involved in either choice — develop in-house or buy from a vendor — but a careful consideration of the organization, its environment, and the need for the technology might help decide this.

## 4.5 Pilot study

To make matters easier, a pilot study could be done to assess the viability of a GDSS for an organization. This should help resolve two issues. One is economic feasibility with two factors: whether the GDSS would result in a net benefit to the organization and whether the organization can afford it.

The pilot study is an experiment in GDSS without committing large resources but allowing the organization to assess the consequences of the investment decision.

## 4.6 Technology push

A final issue has to do with the rate of technological development in GDSS. For a GDSS to be a long-term investment, important technological trends have to be anticipated and considered. Otherwise, the GDSS may soon be obsolete.

## 5. Conclusion and research directions

We have presented a conceptual framework for the design of group decision support systems (GDSS) and identified the critical issues in its design and implementation: considered GDSS from an integrated perspective and highlighted not only various crucial variables but also the interrelationships between them.

We conclude that the study of GDSS ought to start from a conceptual perspective, and that its design ought to follow a contingency approach. The effective design and functioning of a GDSS is found to depend on many variables. The most effective and robust GDSSs, therefore, are those that are designed upon a solid understanding of these variables and tailored to the specific needs of an organization.

GDSS research is too focused, with a bias towards experimental and empirical studies. Its technology is still young and much research is needed before we can understand the best way to design and use it.

In particular, research is needed to explore the nature of the group decision-making process and how to minimize its input (process loss) and maximize its output (process gain). Also, the relevancy of computerized support needs to be further substantiated.

GDSS research is heavily interdisciplinary in nature, involving various fields, not the least of which is sociology, psychology, and social psychology. Group decision-making dynamics and processes are entrenched deeply in these fields. Interpersonal communications, in the GDSS context, is not well understood.

## References

[1] Applegate, L.M., et al. “Knowledge Management in Organizational Planning”, Journal of Management Information Systems, Spring 1987, pp. 20–28.

[2] Austin, N. "A Management Support Environment". ICL Technical Journal, Vol. 5, No. 2, 1986.

[3] Bonczek, R.H., Holsapple, C.W. and Whinston, A.B. "Computer-Based Support of Organizational Decision Making", Decision Sciences, 1979, pp. 268–280.

[4] Bui, T. and Jarke, M. "Communication Requirements for Group Decision Support Systems", Journal of Management Information Systems, Spring 1986, pp. 8–19.

[5] DeGeus, A.P. “Planning as Learning”, Harvard Business Review, Vol. 66, No. 2, March–April 1988.

[6] DeSanctis, G. and Gallupe, R.B. "Group Decision Support Systems: A New Frontier", DataBase, Winter 1985.

[7] DeSanctis, G. and Gallupe, R.B. "A Foundation for the Study of Group Decision Support Systems", Management Science, May 1987, 589–609.

[8] Evans, G.E. and Riha, J.R. "Assessing DSS Effectiveness Using Evaluation Research Methods", Information & Management, 1989, pp. 197–206.

[9] Gallupe, R.B. and DeSanctis, G. “Computer-Based Support for Group Problem-Finding: An Experimental Investigation”, MIS Quarterly, June 1988, pp. 277–296.

[10] Gallupe, R.B. and McKeen, J.D. “Enhancing Computer-Mediated Communication: An Experimental Investigation into the Use of a Group Decision Support System for Face-to-Face Versus Remote Meetings”, Information & Management, Vol. 18, 1990, pp. 1–13.

[11] Gray, P. and Nunamaker, J.F. "Group Decision Support Systems", In: Decision Support Systems: Putting Theory into Practice, Prentice Hall, Englewood Cliffs, NJ, 1989).

[12] Harrison, E.F. The Managerial Decision-Making Process, 3rd edition, Houghton Mifflin, Boston, MA, 1987).

[13] Huber, G.P. “Issues in the Design of Group Decision Support Systems”, MIS Quarterly, 1984, pp. 195–204.

[14] Jacques, E. A General Theory of Bureaucracy, Heinemann Educational Books, Oxford, 1976.

[15] Jarvenpaa, S.L., Rao, V.S. and Huber, G.P. “Computer Support for Meetings of Groups Working on Unstructured Problems: a Field Experiment”, MIS Quarterly, December 1988, pp. 645–665.

[16] Jelassi, M.T. and Beauclair, R.A. "An Integrated Framework for Group Decision Support Systems Design", Information & Management, 1987, pp. 143–153.

[17] Kiesler, S., Siegal, J. and McGuire, T.W. "Social Psycho-

logical Aspects of Computer-Mediated Communication", American Psychologist, October 1984, pp. 1123–1134.

[18] Knight, K., ed., Participation in Systems Development, GP Publishing, Pontiac, MI, 1989.

[19] Kull, D. “Group Decision Support Systems: Can Computers Help?”, Computer Decisions, May 1982, pp. 70–72, 74, 76, 81–82, 84 and 160.

[20] Liang, T.P. “Model Management for Group Decision Support”, MIS Quarterly, December 1988, pp. 667–680.

[21] Nunamaker, J.F. "GDSS: Present and Future", IEEE, November 1989, pp. 6–16.

[22] Nunamaker, J.F., Applegate, L.M. and Konsynski, B.R. "Facilitating Group Creativity: Experience with a Group Decision Support System", Journal of Management Information Systems, Spring 1987, pp. 5–19.

[23] Phillips, L. "People-Centered Group Decision Support", In: Doukidis, G.I., Land, F. and Miller, G., eds., Knowledge-Based Management Support Systems, Ellis Horwood, Chichester, 1989.

[24] Rathwell, M.A. “Information Systems Support for Group Planning and Decision-making Activities”, MIS Quarterly, September 1985, pp. 255–271.

[25] Rice, R.E. “Computer-Mediated Communication and Organizational Innovation”, Journal of Communication, Vol. 37, No. 4, Autumn 1987, pp. 65–85.

[26] Steeb, R. and Johnson, S.C. "A Computer-Based Interactive System for Group Decision-making", IEEE Transactions on Systems, Man, and Cybernetics, Vol. SMC11, No. 8, August 1981, pp. 544–551.

[27] Stefik, M., et al., “Beyond the Chalkboard: Computer Support for Collaboration and Problem Solving in Meetings”, Communications of the ACM, January 1987, pp. 32–47.

[28] Straub, D. and Beauclair, R. “A New Dimension to Decision Support: Organizational Planning Made Easy with GDSS”, Data Management, July 1987, pp. 11, 12 and 20.

[29] Straub, D.W. and Beauclair, R.A. “Current and Future Uses of Group Decision Support System Technology: Report on a Recent Empirical Study”, Journal of Management Information Systems. Summer 1988, pp. 101–116.

[30] Sutherland, D. and Crosslin, R. “Group Decision Support Systems: Factors in a Software Implementation”, Information & Management, Vol. 16, 1989, pp. 93–103.

[31] Vogel, D. and Nunamaker, J. "Group Decision Support System Impact: Multi-Methodological Exploration", Information & Management, Vol. 18, 1990, pp. 15–28.

[32] Wang, H.F. and Sheen, S.Y. "Group Decision Support with MOLP Applications", IEEE Transactions on Systems, Man, and Cybernetics, January–February 1989, pp. 143–152.

[33] Watson, R.T., DeSanctis, G. and Poole, M.S. “Using a GDSS to Facilitate Group Consensus: Some Intended and Unintended Consequences”, MIS Quarterly, September 1988, pp. 463–477.

[34] Zander, A. Making Groups Effective, Jossey-Bass, San Francisco, CA, 1982.

[35] Zangemeister, C. “Nutzwertanalyse”, in: Freelink, H., ed., The Economics of Informatics, North Holland, Amsterdam, 1976.

[36] Zigurs, I., Poole, M.S. and DeSanctis, G.L. “A Study of Influence in Computer-Mediated Group Decision Making”, MIS Quarterly, December 1988, pp. 625–644.
