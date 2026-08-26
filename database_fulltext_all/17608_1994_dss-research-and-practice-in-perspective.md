---
otero_id: 17608
otero_key: "4TC4MPDT"
title: "DSS research and practice in perspective"
authors: "Albert A. Angehrn; Tawfik Jelassi"
year: "1994"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)90045-0"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# DSS research and practice in perspective

practice.

Albert A. Angehrn and Tawfik Jelassi

INSEAD. 77305 Fontainebleau, France

The aim of this paper is to assess the state-of-the-art in the Decision Support Systems (DSS) field from both a research and a practice perspective. Three main dimensions of DSS research and practice are addressed: 1) supporting human decision-making processes, 2) integrating DSS into the organizational context, and 3) identifying new application domains. The related analysis and discussion provides a better understanding of past developments in the DSS field and insights into future evolution patterns.

Keywords: Computer-aided decision-making; Decision support systems; DSS assessment; DSS research and

![](/api/attachments/4TC4MPDT/fulltext/images/9bbdbec075268c02c97596ed192caeec45266893c3e0c1f423a5e919ed2026e0.jpg)

Albert Angehrn, Associate Professor of Information Systems at INSEAD, holds a doctoral degree in mathematical sciences from the Swiss Federal Institute of Technology (ETH). His research focus lies on cognitive aspects of decision-making, intelligent forms of human-computer interaction, and management applications of Multimedia and Computer Supported Collaborative Work. Besides publishing in various academic journals and books, Dr. Angehrn's activities in

## 1. Introduction

The objective of this paper is to review the state-of-the-art in the Decision Support Systems (DSS) field and to indicate the main directions in which both DSS research and practice might evolve. The paper is oriented to researchers in the computer-aided decision-making area, as it highlights promising DSS research directions, stressing the link with other disciplines which are becoming more and more relevant for DSS research and to which DSS studies could contribute (a two-way link). From the point of view of practitioners interested in DSS and in Executive Information Systems (EIS), this paper provides an overview of the opportunities and pitfalls associated with the use of such systems in organizations, covering the main phases of DSS/EIS design and implementation, the relevant issues to consider when embarking on developing such a system, and some of the more promising application areas.

The paper attempts to achieve the above stated objective by presenting an abbreviated version of the DSS tutorial the authors gave at the first IFORS Specialized Conference on Decision Support Systems (Bruges, Belgium, March 26–29, 1991). This tutorial was widely attended; half of the 300 conference participants signed up for it. Attendees came from over twenty countries and had varying degrees of knowledge and/or experience with DSS. The diversity of their background and affiliation (academia and business) as well as the tutorial context provided a good opportunity to discuss several issues related to DSS research and practice. The outline of this paper, which reflects the structure used in the tutorial, is as follows. Following this introduction, section 2 provides some retrospective thoughts on DSS. Section 3 focuses on decision-making processes while section 4 centers on integrating DSS into the organizational context. Section 5 presents new application domains of DSS, namely supporting group decision-making, conflict resolution as well as cooperative/collaborative work in organizations.

![](/api/attachments/4TC4MPDT/fulltext/images/b05d10407d68986bd93639a9da317d6629d041c10cff969eaa719f798eb1d48e.jpg)

## 2. DSS in perspective

The DSS field has its roots in the work of Gorry and Scott Morton [27], who combined in their framework the three levels of managerial activity introduced by Antony [6] and the distinction between programmed and non-programmed decisions [71]. The framework of Gorry and Scott Morton played “a key role in launching the DSS movement” [46]. Starting from these early days, DSS researchers have attempted to adopt and extend methodologies and techniques developed in several research areas and to combine them into a new form of computer-based systems able to support and enhance managerial decision-making.

In theory, the set of disciplines which are potentially relevant to the design and implementation of effective DSS is very large, including research fields such as ergonomy, psychology, organizational studies, artificial intelligence and cognitive science (see Figure 1). The first influential DSS publications emphasized the multi- or inter-disciplinarity of the field, putting a strong focus on organizational issues and human factors [56,50,10]. For example, Mintzberg stated in one of his papers [55]: “What appeals to me about the orientation of the DSS literature, in general, is its sympathy with the needs of the manager and its sensitivity to the findings of descriptive research. It is refreshing to see these computer systems recognized as “support” and to encounter a part of the management science literature that puts down neither the manager nor his intuition. This provides a healthy basis on which to develop and introduce these systems into organizational decision-making. ... Maybe the DSS people with their managerial orientation, can rediscover what operations research seems to have lost."

![](/api/attachments/4TC4MPDT/fulltext/images/a6435bc631cc0ced1f767ee769e393ae74593be4fa4ade07ac3ab9163d1b083e.jpg)  
Fig. 1.

In practice, two main disciplines have almost exclusively influenced the evolution of the DSS field in a substantial way: Management Science/Operations Research (MS/OR) and Management Information Systems (MIS). In fact, as Eom [23] put it, the majority of systems labelled as DSS were, and still are today, either computer implementations of MS/OR models and techniques (e.g. optimization algorithms) or extensions of database systems, traditional MIS or Expert Systems. The strong impact that MS/OR and MIS had on the DSS field can be explained by two factors: first, the academic background of DSS researchers which has been almost exclusively either MS/OR or MIS/Computer Science; and second, the provision by both disciplines of a variety of ready-to-use methods and tools (mainly problem-solving and data management techniques) allowing the efficient “assembly” of DSS.

The resulting MS/OR- and MIS-driven evolution of the DSS field had both positive and negative consequences. A major benefit was the ability, in the early 1970s, to bridge, through DSS, these two basic disciplines which were evolving separately (and not always successfully [1]). Hence the DSS field provided a framework for integrating, in a balanced way, the best developments in both areas.

On the other hand, along with the most advanced models, tools and techniques, the DSS field also inherited from MS/OR and MIS the traditional, techno-rational approach to problem-solving and decision-making. This approach has been emphasizing quantitative analysis, rational behavior and computational efficiency (systemic, reductionistic perspective) and underestimating or neglecting qualitative and psychological factors (wholistic, socio-political perspective). In this context, the DSS movement has somewhat failed – at least in practice – to impose an alternative and unique approach to the design of systems supporting management decision-making. Such an approach would have helped the realization of the DSS pioneers' vision: supporting (and not replacing) human judgement; placing the user first, the system comes in second; incorporating managerial styles of decision-making; and focusing on the organizational fit of the system.

In order to attain its original objective, the DSS field needs to establish strong links to other disciplines than MS/OR and MIS. Failing to do so would continue making DSS as “vehicles” for implementing the latest MS/OR and MIS developments, be it problem-solving heuristics or computer science innovations (such as neural networks and advanced human-computer interaction techniques). As Bell recently put it: “Following initial succes in the real world, both fields [OR/MS and DSS] became more theoretical, perhaps more ‘academically respectable’. This path condemned OR to the doldrums for about thirty years. I very much hope that DSS does not suffer the same fate.” [9].

A clear distinction must be made between what effectively improves decision-making processes and what does not, or only marginally achieves this goal. The authors believe that there are three main issues that help better understand the unique contribution that DSS can make to both research and practice. These issues, which will be discussed in the remainder of this paper, address conceptual, methodological and application-oriented aspects of DSS. They provide guidelines for practitioners interested in developing relevant DSS for their organizations. They also help researchers identify new ways of enhancing decision-making processes through computer-based support systems. These three issues are:

1. Addressing the nature of individual and organizational decision-making processes (conceptual DSS focus);

2. Integrating into the human decision-making context the existing and evolving computer-based tools, techniques and systems (methodological DSS focus); and

3. Addressing the real organizational needs by extending decision support to business teams (application-oriented DSS focus).

## 3. Re-focussing on the nature of human decision-making processes

Decision-making has always been a main issue in the DSS field. In particular, it has been often used as a central focus to distinguish DSS from other interactive computer-based systems (e.g., Expert Systems and Office Information Systems) used in organizations $[74,45,79]$ .

What is the dominant model of human decision-making adopted by DSS researchers? The majority of textbooks and studies, such as Sprague & Carlson [73], Turban [76], and Bonczek, Holsapple & Whinston [11] explicitly or implicitly assume the validity and usefulness of the “intelligence-design-choice” model proposed by Simon [71]. As stated by Silver [70], Simon’s phase model pervades the DSS literature. The model is generally used both to explain the process of decision-making and to derive the characteristics of computer-based systems aimed at supporting this process. Consequently, traditional DSS, based on Sprague and Carlson’s guidelines [73], comprise a set of tools that support (1) the storage, manipulation and access of data, (2) the process of fitting this data into formal models, and (3) a set of methods and algorithms used to “solve” models in order to reach some decisions. These three types of support are provided by DSS components and respectively correspond to Simon’s decision-making phases of intelligence, design, and choice.

The authors believe that the wide adoption of Simon's model – which has provided a sound conceptual basis for developing the first generation of DSS – has become a serious obstacle for the evolution of DSS theory and practice. As will be shown in the sequel, different types of DSS could emerge from the adoption of alternative perspectives of human decision-making. Such models may result from:

1. the relaxation of the basic assumption that managerial behavior is mainly guided by deductive logics and full or bounded rationality as suggested by Simon's model [30;14];

2. shifting the focus from the choice phase – in which alternatives are evaluated and selected – to other phases of the decision-making process, such as problem structuring/framing [65], creativity and idea processing [21], post-decision analysis, feedback analysis, etc.

A first example of such an alternative model consists of considering decision-making as a learning process. As stated by Keen and Scott Morton [50]: “… learning is often not a by-product of a DSS but a valuable and primary contribution it can make”. In practice, not much of the DSS literature has adopted models of learning processes as a basis for eliciting the components and the dynamics of DSS. Such an approach, as shown by Henderson and Martinko [31] and Courbon [17], can lead to a different type of DSS whose main objective is to provide flexible environments through which learning about a decision situation can take place [2,3,80]. This objective can be conceptually extended from individual to organizational learning [7], giving rise to new forms of group and organizational DSS that address and support learning rather than problem-solving.

A second alternative approach to decision support consists of not adopting a specific model of decision-making, but focusing instead on typical decision-making biases observable in practice. Human decision-making biases have been extensively studied by psychologists [77,72]. These studies – encompassing both individual and group decision-making – can provide an alternative starting point for determining DSS characteristics and extend the application areas and the impact of these systems. For instance, Angehrn [4] describes the design of a DSS in which “Stimulus Agents” actively intervene during the different phases of the decision-making process. These agents can be thought of as a team of advisors, experts and devil’s advocates that challenge the frame selected by the decision maker. They provide different viewpoints and additional information, and offer alternative problem-solving strategies. As a result, the DSS user is prevented from structuring problems in a too narrow way, from becoming too overconfident in his or her judgment, and to eliminate or reduce the negative effects of other well-documented biases [32,33].

In summary, the adoption of alternative models of decision-making has the potential to stimulate innovation in the design of the three traditional DSS components. A better understanding of the dynamics of human-computer interaction, combined with the use of advanced input-output devices, can give rise to new forms of DSS dialog system $[43]$ . The associative models of information processing underlying today's hypertext and hypermedia systems $[60]$ can open new perspectives for users' data and information handling. Finally, the appropriate use of Artificial Intelligence techniques such as case-based reasoning $[5]$ can enhance the “conviviality” of the system and its interaction capabilities with a human decision maker $[36]$ .

## 4. Introducing DSS into organizations: Methods and tools

The importance of the DSS development process and of adopting a suitable implementation strategy is not a new issue in the field; it was recognized by authors like Keen [48,49], Rockart & DeLong [68] as one of the critical success factors in DSS. Still, the reason for many DSS/EIS failures is related to poor/inappropriate integration of these systems in their organizational context [26,47].

From a methodological viewpoint, DSS design and implementation problems are not different from those of integrating technical systems into human contexts $[57]$ . We believe that DSS researchers and practitioners could benefit from studies such as those describing the development of the XSEL expert system (see for example $[59]$ ). These studies could help better understand the importance of such factors as management commitment, organizational culture, users' participation in system design, users' training and system evolution strategy. Reaching out to research in organizational behavior and organization design $[25]$ is particularly important for DSS researchers since developing systems that address a sensitive domain such as decision-making cannot be done

Fig. 2.

without taking into account a variety of factors. These factors include not only individual information needs [67] and decision-making styles [34], but also their fit with existing cooperative [25] as well as conflicting [69] problem solving efforts, power structure [53] and organizational culture [66].

For instance, Ciborra [16] provides a set of examples on successful MIS implementations in organizations. A common characteristic in these examples is the joint design of both the organization and its information system; the ultimate goal being the enhancement of organizational efficiency through streamlining transactions exchange [78].

From a technical viewpoint, emphasis is increasingly given to tools that can facilitate and document the DSS design and implementation process as well as the system evolution which is necessary to accommodate a constantly changing environment $[58]$ . Some tools based on object-oriented techniques $[18]$ , hypertext and hypermedia technology $[13,64]$ are particularly promising given their ease of use and natural approach to collaborative information management. These tools can enhance the use of prototyping and allow a more participative involvement of end-users in all the system development phases $[37]$ . They have also the potential to facilitate requirements elicitation, cooperative documentation of system versions, collection of ideas and communication between end-users and technical support teams.

## 5. Decision support for business teams

Two major factors have led to extending the initial concept of providing computer-based decision support from the individual manager/user target to the group entity. These factors are:

1. A renewed awareness of the importance of teamwork and its impact on organizational performance. Groupwork and team collaboration, as opposed to individual efforts, represent for organizations a productive form of social interaction [54]. Moreover, team-based collaboration was recently suggested as a central dimension in the design of new organizational forms such as the “networked organization” [8].

2. Technological advances in telecommunications offered the necessary networking infrastructure, hence enabling the physical implementation of Group Decision Support Systems (GDSS). The system communication capabilities allowed GDSS to overcome the traditional barriers of time (synchronous versus asynchronous operation) and space (local versus remote interaction).

The first generation of GDSS was mainly based on the concept of “same time, same place”. (Figure 2, from [40] shows some GDSS dimensions). This configuration assumed that group members meet face-to-face in the same physical location and participate simultaneously in the different stages of the computer-supported decision-making process [61]. The pioneering work behind early GDSS (see for example [34] and [19]) provided valuable concepts for the design, implementation and evaluation of computer systems that aim at effectively supporting group decision-making processes.

Although the actual impact of the first GDSS generation remained quite limited both in its scope and in its organizational adoption and use, several studies (e.g. [12]) have confirmed the potential that this emerging technology has. For example, Nunamaker et al. [61] assessed the operational functions of a GDSS at an IBM site. They found that process and outcome effectiveness, efficiency and user satisfaction were consistently higher with GDSS use compared to no computer support. Moreover, a comparison of person-hours expended led to a 56% savings that was attributable to the GDSS use. (Additional information on the study mentioned above can be found in [29]).

![](/api/attachments/4TC4MPDT/fulltext/images/8613416af0b90ad364a949daacdc59dff20a846569db799aa81fa0b731466d7b.jpg)

Obviously, there is a need to conduct more field studies with varying settings and using “real” decision makers. Such an approach would help researchers confirm or question the laboratory findings and results gathered to date. (Some criteria for evaluating the success of group decision support can be found for example in [20]).

Another area of computer support for business teams focuses on conflict tasks; related systems are termed Negotiation Support Systems (or NSS). The underlying goal here is to help resolve conflicts of viewpoint and/or interest between members of the same group or among different groups $[42]$ . In addition to the distinct goal that each technology pursues (supporting conflict resolution as opposed to helping cooperative group decision-making), NSS differ from GDSS on other dimensions as well $[41]$ . It is obvious that the general atmosphere of GDSS sessions, as opposed to the NSS ones, can be characterized by openness, trust and information sharing among all participants.

As a consequence of the lack of the above features, each negotiating party usually wants to use its own set of data and decision models and tools. This fact requires finding a compromise solution to this pre-session “conflict” in order to determine the content of the NSS system components. Issues that need to be addressed here include: What and whose data should be used (and therefore stored in the system database)? What bargaining and negotiation techniques should be employed in order to help bring the two parties to a settlement? Consequently, what game-theoretical models should be part of the NSS model management component?

A possible approach to tackling the above difficulties was suggested by Jarke, Jelassi and Shakun [39]. It consists of using a neutral third-party, who is him/herself supported by the NSS, as a mediator that facilitates the process between the two negotiating parties. Each party is also supported by the NSS and has full control over its private data and computer “work space”. The human mediator must first determine a commonly agreed-upon data set. (This initial preparatory work can be performed using some database techniques [38]). This common denominator is intended to serve as a starting point but can, and usually does, evolve over time once the actual negotiation is underway.

Some recent laboratory experiments showed the positive impact of NSS on negotiation process, outcomes and negotiators' attitudes. For example, Jones and Jelassi [44] examined the impact of computer intervention during negotiation, in bargaining situations that can be characterized as integrative (“win-win” scenarios) or distributive (“win-lose” scenarios or zero-sum games). They found that in the integrative task, the bargainers achieved higher joint outcomes when presented with the computer-suggested settlements.

A more recent study [24], conducted in similar bargaining situations between a buyer and a seller negotiating the terms of a multi-issue purchase agreement, showed that NSS support helped achieve significantly higher joint outcomes for both parties and increased negotiators' satisfaction. Given the preliminary evidence provided by the above studies, one is encouraged to delve further into the area of analytical negotiation with the aid of computer support.

Whilst the above-mentioned approaches to group and negotiation support have had only a limited impact, another field, Computer Supported Cooperative Work (CSCW), has emerged in the last few years. Driven by the seminal work of Engelbart [22], by experimentation at Xerox Parc [75] and by theoretical work at MIT [51], research and applications in the CSCW field address the design and implementation of communication systems, shared workspace facilities [63], shared information facilities [52] and group support facilities in organizations [28].

As noted by Chin, Holsapple and Whinston [15], research in GDSS, NSS and computer support of distributed decision-making proceeds along the same lines as that in CSCW. Given that decision-making processes are generally interlinked with other information processing, communication and coordination activities, it is the author's belief that strengthening the links to the interdisciplinary CSCW community might give new impulses to research work as well as to applications of group decision and negotiation systems in organizations.

## 6. Conclusions

The objective of this paper (and of the tutorial on which it is based) was to present an overview of the evolution of the DSS field. It also aimed at providing both researchers and practitioners with a better understanding of current challenges and future opportunities in the field.

From the practitioners' perspective and based on the written feedback gathered from the tutorial participants, the authors believe that the success of the tutorial was mainly due to the issue-based approach followed to assess the state-of-the-art and future directions in DSS. Instead of adopting a traditional textbook structure, the fundamental concepts of DSS (scope and objectives, design and implementation, applications) have been gradually introduced by integrating them into the discussion of relevant issues. Such issues included focusing on decision-making processes, integrating DSS into the organizational context, and taking advantage of the new teamwork-oriented concepts and technologies.

From the researchers' perspective, the framework presented in this paper contributed to highlighting some of the most promising DSS research directions. It emphasized the (two-way) links with disciplines such as Decision Sciences, Organizational Behavior, and Cognitive Sciences, and extended the basic DSS concept from the single user framework to the group entity. New application domains which are still today in their infancy include Group DSS, Negotiation Support Systems, and Computer-Supported Cooperative Work. Early laboratory experiments and field studies provided encouraging results and demonstrated the organizational potential of these emerging technologies.

## References

[1] R.L. Ackoff, 1967, Management Misinformation Systems, Management Science, 14, 4, pp. 147–156.

[2] A.A. Angehrn, 1991, Modeling by Example, A Link Between Users, Models and Methods in DSS, European Journal of Operational Research, 55, pp. 293–305.

[3] A.A. Angehrn, 1991, Designing Humanized Systems for Multiple Criteria Decision Making, Human Systems Management, 10, 3, pp. 221–232.

[4] A.A. Angehrn, 1992, Stimulus Agents: An alternative Framework for Computer-aided Decision Making, in: DSS-92 Transactions, M.S. Silver (ed.), The Institute of

Management Science, Chicago, pp. 81–92. Forthcoming in Interfaces.

[5] A.A. Angehrn and S. Dutta, 1992, Integrating Case-Based Reasoning in Multi-Criteria Decision Support Systems, in: Decision Support Systems: Experiences and Expectations, T. Jelassi et al. (eds.), North-Holland, pp. 133–150.

[6] R.N. Anthony, 1965, Planning And Control Systems: A Framework for Analysis, Graduate School of Business Administration, Harvard University, Boston, MA.

[7] C. Argyris and D.A. Schon, 1978, Organizational Learning: A Theory of Action Perspective, Addison Wesley, Reading, MA.

[8] C.A. Bartlett and S. Ghoshal, 1989, Managing across Borders, The Transnational Solution, Harvard Business Press.

[9] P.C. Bell, 1992, Decision Support Systems: Past, Present and Prospects, Journal of Decision Systems, 1, 2-3, pp. 127–137.

[10] J.L. Bennett, (ed) 1983, Building Decision Support Systems, Addison Wesley, Reading, MA.

[11] R.H. Bonczek, C.W. Holsapple and A.B. Whinston, 1981, Foundations of Decision Support Systems, Academic Press, New York.

[12] T. Bui, T.R. Sivasankaran, Y. Fijol, and M.A. Woodbury, 1987, Identifying Organizational Opportunities for GDSS Use: Some Experimental Evidence, Decision Support Systems: The International Journal, 3, pp. 68–75.

[13] V. Bush, 1945, As we may think, Atlantic Monthly, 176, 101–108.

[14] P. Checkland, 1985, From Optimizing To Learning: A Development of System Thinking for the 1990's, Journal of the Operational Research Society, 36, 9.

[15] C. Chin, C.W. Holsapple and A.B. Whinston, 1991, Computer Support In Distributed Decision Environments, in: Environments For Supporting Decision Processes, H.G. Sol and J. Vecsenyi (eds.), Elsevier, Amsterdam, The Netherlands, pp. 335–356.

[16] C.U. Ciborra, 1987, Reframing The Role Of Computers In Organizations: The Transaction Cost Approach, Office Technology and People, 3, pp. 17–38.

[17] J.C. Courbon, 1984, Transparency of Data, Information and Models in Decision Support Systems, in: Operational Research 1984, J.P. Brans (ed.), Elsevier Science Publishers.

[18] B. Cox, 1986, Object-oriented Programming: An Evolutionary Approach, Addison Wesley, Reading, MA.

[19] G. DeSanctis and R.B. Gallupe, 1987, A Foundation for the Study of Group Decision Support Systems, Management Science, 33, 5, pp. 589–609.

[20] C. Eden, 1992, A Framework for Thinking about Group Decision Support Systems, Group Decision and Negotiation, 1, pp. 199–218.

[21] J.J. Elam and M. Mead, 1990, Can Software Influence Creativity? Information Systems Research, 1, 1, pp. 1–22.

[22] D.C. Engelbart, 1963, A Conceptual Framework For The Augmentation Of Man's Intellect, in: Vistas in Information Handling, P.W. Howerton and D.C. Weeks (eds.). 1, Spartan Books, Washington, DC, pp. 1–29.

[23] H.B. Eom and S.M. Lee, 1990, A Survey of Decision Support System Applications (1971-April 1988), Interfaces, 20, 3, pp. 65–79.

[24] A. Foroughi, T. Jelassi and W.C. Perkins, 1992, An Empirical Study of an Interactive, Session-oriented Computerized Negotiation Support System, INSEAD Working Paper Series.

[25] J.R. Galbraith, 1977, Organization Design, Addison Wesley, Reading MA.

[26] M.J. Ginzberg and G. Ariav, 1986, Methodologies for DSS Analysis And Design: A Contingency Approach To Their Application, in: Proceedings of the 7th International Conference on Information Systems, San Diego, CA., pp. 46–56.

[27] A. Gorry and S. Morton, 1971, A Framework For Management Information Systems, Sloan Management Review, 13, 1, pp. 55–70.

[28] I. Greif, (ed.) 1988, Computer-supported Cooperative Work: A Book of Readings, Morgan Kaufmann, San Mateo, CA.

[29] R.B. Grohowski, C. McGoff, D.R. Vogel, W.B. Martz, and J.F. Nunamaker, Jr., 1990, Implementation of Electronic Meeting Systems at IBM, MIS Quarterly, 14, 4, pp. 369–383.

[30] A. Hatchuel and H. Molet, 1986, Rational Modeling in Understanding and Aiding Human Decision Making: About two Case Studies, European Journal of Operational Research, 24, pp. 178–186.

[31] J.C. Henderson and M.J. Martinko, 1981, Cognitive Learning Theory and the Design of Decision Support Systems, in: DSS-81, Proceedings of The First International Conference on Decision Support Systems, Atlanta, GA., pp. 45–50.

[32] R.M. Hogarth, 1980, Judgment and Choice: The Psychology of Decision, John Whiley, New York.

[33] R.M. Hogarth and S. Makridakis, 1981, Forecasting and planning: An evaluation, Management Science, 27, 2, pp. 115–138.

[34] G.P. Huber, 1983, Cognitive Style As A Basis For MIS And DSS Design: Much Ado About Nothing?, Management Science, 29, 5, pp. 567–579.

[35] G. Huber, 1987, Issues in the Design of GDSS, MIS Quarterly, 7, pp. 195–204.

[36] I. Illich, 1973, Tools for Conviviality, Perennial Library, Harper & Row, New York.

[37] B. Ives and M.H. Olson, 1984, User involvement and MIS success: a review of research, Management Science, 30, 5, pp. 586–603.

[38] M. Jarke and T. Jelassi, 1986, View Integration in Negotiation Support Systems, in: Transactions of the Sixth International Conference on Decision Support Systems, Washington D.C., pp. 180–188.

[39] M. Jarke, T. Jelassi, and M.F. Shakun, 1987, MEDIATOR: Towards a Negotiation Support System, European Journal of Operational Research, 31, 3, pp. 314–334.

[40] T. Jelassi and R.A. Beauclair, 1987, An Integrated Framework for Group Decision Support Systems Design, Information and Management, 13, 3, pp. 143–153.

[41] T. Jelassi and A. Foroughi, 1989, Negotiation Support Systems: An Overview of Design Issues and Existing Software, Decision Support Systems: The International Journal, 5, 2, pp. 167–181.

[42] T. Jelassi and B. Jones, 1988, Getting to YES with NSS: How Computers Can Support Negotiations, in: Organiza-

tional Decision Support Systems, R.M. Lee, A.M. McCosh and P. Migliarese (eds.), North-Holland, pp. 75–85.

[43] C.V. Jones, 1991, User Interface Development and Decision Support Systems, paper presented at the NATO-ASI Conference on Recent Development in DSS, Il Ciocco, Italy.

[44] B. Jones and T. Jelassi, 1990, The Effects of Computer Intervention and Task Structure on Bargaining Outcome, Theory and Decision, 28, pp. 335–377.

[45] P.G.W. Keen, 1987, MIS Research: Current State, Trends And Needs, in: Information Systems Education: Recommendations and implementation, A. Buckingham et al. (eds.), Cambridge University Press, pp. 1–13.

[46] P.G.W. Keen, 1987, DSS: The Next Decade, Decision Support Systems: The International Journal, 3, 3, pp. 253–265.

[47] P.G.W. Keen, 1980, Adaptive Design For Decision Support Systems, Data Base, 12, 1-2, pp. 15–25.

[48] P.G.W. Keen, 1981a, Information Systems And Organizational Change, Communications of the ACM, 24, 1, pp. 24–33.

[49] P.G.W. Keen, 1981b, Value Analysis: Justifying Decision Support Systems, MIS Quarterly 5, 1, pp. 1–15.

[50] P.G.W. Keen and M.S. Scott Morton, 1978, Decision Support Systems: An Organizational Perspective, Addison Wesley, Reading, MA.

[51] T.W. Malone, 1988, What is Coordination Theory?, paper presented at the National Science Foundation Coordination Theory Workshop, MIT, Cambridge, MA.

[52] T.W. Malone, K.R. Grant, F.A. Turbak, S.A. Brobst and M.D. Cohen, 1987, Intelligent Information Sharing Systems, Communications of the ACM, 30, 5, pp. 390–402.

[53] M.L. Markus, 1983, Power, Politics and MIS Implementation, Communications of the ACM, 26, 6, pp. 430–444.

[54] J.E. McGrath, 1984, Groups: Interaction and Performance, Prentice-Hall.

[55] H. Mintzberg, 1982, Commentary on the Huber, Kunseuther and Schoemaker, and Chestnut and Jacoby papers, in: Decision Making: An interdisciplinary Inquiry, Ungson and Braunstein (eds.), Kent Publishers, pp. 280–287.

[56] M.S. Scott Morton, 1971, Management Support Systems, Computer-based Support for Decision Making, Harvard University, Boston.

[57] E. Mumford, 1979, Computer Systems In Work Design: The ETHICS method, Associated Business Press.

[58] E. Mumford, 1991, Decision Making And The Organisational Environment: Today's Problems And Tomorrow's Needs, in: Environment For Supporting Decision Processes, H.G. Sol and J. Vecsenyi (eds.), Elsevier, North Holland, pp. 1–11.

[59] E. Mumford and B. MacDonald, 1989, XSEL's progress: The Continuing Journey Of An Expert System, John Wiley, New York.

[60] B.J. Murdock, 1982, A Theory For The Storage And Retrieval Of Item And Associative Information, Psychological Review, 89, pp. 609–626.

[61] J.F. Nunamaker Jr., D. Vogel and B. Konsynski, 1989, Interaction of Task and Technology to Support Large Groups, Decision Support Systems: The International Journal, 5, 2, pp. 139–152.

[62] F. Nunamaker Jr., D. Vogel, A. Heminger, B. Martz, R. Grohowski and C. McGoff, 1989, Experiences at IBM with Group Support Systems: A Field Study, Decision Support Systems: The International Journal, 5, 2, pp. 183–196.

[63] M.H. Olson, 1989, Technological Support for Work Group Collaboration, Lawrence Erlbaum Associates, Hillsdale, N.J.

[64] T. Oren, 1987, The Architecture Of Hypertext, in: Proceedings of Hypertext '87 Chapel Hill.

[65] J.W. Payne, M.L. Braunstein and J.S. Carroll, 1978, Exploring Predecisional Behavior: An Alternative Approach To Decision Research, Organisational Behavior and Human Performance, 22, pp. 1744.

[66] L. Phillips, 1992, Gaining Corporate Commitment To Change, in Executive Information Systems and Decision Support, C. Holtham (ed.), Chapman & Hall, pp. 79–96.

[67] J.F. Rockart, 1979, Chief Executives Define Their Own Data Needs. Harvard Business Review 57, 2, pp. 81–93.

[68] J.F. Rockart and D.W. DeLong, 1988, Executive Support Systems: The Emergence Of Top Management Computer Use, Dow Jones-Irwin, Homewood, IL.

[69] T.C. Schelling, 1980, The Strategy of Conflict, Harvard University Press, Cambridge, MA.

[70] M.S. Silver, 1991, Systems That Support Decision Makers: Description And Analysis, John Whiley, New York.

[71] H. Simon, 1960, The New Science Of Management Decision, Harper & Row, New York.

[72] P. Slovic, B. Fischhoff and S. Lichtenstein, 1977, Behavioral Decision Theory, Annual Review of Psychology, 28, pp. 1–39.

[73] R.H. Sprague and E. Carlson, 1982, Building Effective Decision Support Systems, Prentice Hall.

[74] C.B. Stabell, 1983, A Decision-Oriented Approach To Building Decision Support Systems, in: Building Decision Support Systems, J.L. Bennett (ed.), Addison Wesley, pp. 221–260.

[75] M. Stefik, G. Foster, D.G. Bobrow, K. Kahn, S. Lanning and L. Suchman, 1987, Beyond the Chalkboard, Communications of the ACM, 30, 1, pp 32–47.

[76] E. Turban, 1988, Decision Support and Expert Systems. Macmillan, New York.

[77] A. Tversky and D. Kahneman, 1974, Judgment Under Uncertainty: Heuristics and biases, Science, 185, pp. 1124–1131.

[78] O.E. Williamson, 1981, The Economics Of Organization: The Transaction Costs Approach, American Journal of Sociology, 87, 3, pp. 548–577.

[79] W. Zachary, 1986, A Cognitively Based Functional Taxonomy Of Decision Support Techniques. Human-Computer Interaction, 2, pp. 25–63.

[80] M. Zeleny, 1989, Cognitive Equilibrium: A New Paradigm Of Decision Making? Human Systems Management, 8, pp. 185–188.
