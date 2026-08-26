---
otero_id: 18828
otero_key: "7XW6U3P9"
title: "Human and machine roles in team product reviews"
authors: "Kenneth A Kozar; Ilze Zigurs"
year: "1992"
journal: "Information & Management"
doi: "10.1016/0378-7206(92)90039-i"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# Human and machine roles in team product reviews

# A prescription for change

Kenneth A. Kozar and Ilze Zigurs

University of Colorado, College of Business and Administration, Boulder, CO, USA

A team product review, often called a structured walk-through, is one type of small group meeting used to improve the quality of system deliverables. During all such meetings, participants assume roles; these have been discussed in the behavioral literature. Lately, new computer-based technologies for improving meetings have emerged. These technologies may help developers, but their use in support of meetings will require system developers to understand and accept new procedures and methods, and understand the roles of both the participants and technology. This paper examines the team product review process, past work on the various roles in small groups, and changes that might be needed when using computer system support. A basic premise is that an analysis of the roles of humans and machines can show how processes should change in order to use new technology to its maximum potential.

Keywords: Group decision support systems, Team technology, Team product reviews, Roles in systems development, Systems analysis and design, System quality

## 1. Introduction

Team efforts are an important component of improving system quality. Research has shown that teams find more errors in a deliverable than individual developers do when looking at their own products $[6,10,14,30,33,35]$ . To improve quality, a systems development team needs to share deliverables, ranging from logical products, such as requirements statements, to physical products, such as prototypes. This sharing facilitates com-

![](/api/attachments/7XW6U3P9/fulltext/images/b539f965631a98fbd5f03030766c7a6e37c30c52d08f4205aef8dfa5b3244e4d.jpg)

Kenneth A. Kozar is an Associate Professor of Information Systems in the College of Business at the University of Colorado in Boulder. He has been on the faculties of several universities and has considerable experience as an MIS practitioner. Dr. Kozar has published in journals including MIS Quarterly, International Journal of Man-Machine Studies, Journal of Management Information Systems, and the Journal of Product Innovation Management. He is the author of Humanized Information Systems Analysis and Design: People Building Systems for People (McGraw-Hill, 1989). In 1985, a paper he co-authored tied for second place in the SIM Juried Paper Competition, and in 1989, he and his co-authors won the SIM Paper Award Competition. He is an Associate Editor of the MIS Quarterly and on the Editorial Board of IS /Analyzer.

![](/api/attachments/7XW6U3P9/fulltext/images/0853946a56542ead3c019c905b96970c46cc74e05e630ae947438dd56d3d4308.jpg)

Ilze Zigurs is an Assistant Professor of Information Systems in the College of Business at the University of Colorado in Boulder. Dr. Zigurs' research focuses on the design and impacts of computer-based systems for enhancing the effectiveness of groups and group decisions. Her work has been published in the MIS Quarterly, Decision Support Systems, and the Journal of Management Information Systems. Dr. Zigurs was editor of the DSS-91 Transactions, and is currently

associate editor of the Newsletter for the Organizational Communication and Information Systems Division of the Academy of Management.

munication between and among system developers and users. Effective teamwork is crucial to building low maintenance and high quality systems that meet user requirements.

A team product review, hereafter simply referred to as a review, is an essential function in a quality system development process. Often called a structured walkthrough, it was one of the first structured techniques to be introduced. Prescriptive guidelines for conducting reviews are found in the literature $[16]$ . Although reviews have proved to be beneficial, they also have been difficult to implement in organizations $[28,36]$ .

One reason for the lack of acceptance of reviews is that they require changed behavior of review participants. A new set of roles must be assumed by the participants $[25]$ . Although roles have been a fruitful area of research in small group behavior, the importance of roles has been largely ignored in an information systems development context. Role ambiguity, role stress, and role overload are all phenomena that could detract from the success of reviews. It is important to understand how existing knowledge of roles can be leveraged to improve the review process.

A second problem in reviews has been the lack of support mechanisms for conducting the review process. Computer-aided software engineering (CASE) tools available to systems developers to date have mainly supported individual, not group work, even though multiuser products exist. The recent emergence of computer-based technologies designed to make meetings more effective has great potential for reviews. These group-oriented technologies have been called group decision support systems $[2,13,20]$ , electronic meeting systems $[11]$ , groupware $[23]$ , and collaborative work support systems $[9]$ . We use the term “team technology” as a broad term for this class of technology. Such an integrated system utilizes hardware, software, and procedures to structure and support group communication.

The objective of this paper is to explore how reviews can be made more effective by focusing on: (1) the roles required, and (2) how team technology might help humans fill those roles. A combination of human and machine roles can create an environment for effective reviews, which in turn should lead to better information systems. "Role thinking" is suggested as a way to capitalize on new technology by examining existing roles in a given process and apportioning roles between humans and technology to create a more effective process.

## 2. Team product reviews

The use of reviews to enhance the quality of information system development has received considerable attention in the literature. More participation by designers and users improves the systems development process $[19]$ . Better communication between designers and users leads to higher system quality by tapping all available sources of expertise. Active involvement of all constituents leads to increased acceptance and ownership of the final system.

The process of conducting reviews also has been described, and typically takes place as follows:

1. The producer of the deliverable determines when to have other team members examine the product. Reviews are generally best conducted on rough drafts, rather than polished deliverables.

2. The project leader affirms that the product is ready for review.

3. The deliverable is distributed to the review team shortly before a scheduled meeting.

4. Reviewers are told to review material with the intent of giving constructive criticism and not of attempting to destroy the ego of the product producer.

5. After a short overview by the presenter, who may also be the product producer, reviewers make positive comments then point out possible deficiencies. The team decides disagreements by majority vote. Reviewers attempt to find deficiencies, not fix them.

6. Reviewers vote on the disposition of the product, to approve it with deficiencies corrected or to conduct another review. The desired result of the review is a team-owned product of improved quality.

Like any group process, however, reviews suffer from a number of weaknesses. Team members may hesitate to participate in group processes due to perceived status differences, pressures to perform, pressures to conform, power exertion by individuals, inability to stay on a topic, poor record keeping, dysfunctional conflicts, and focus on a narrow set of topics to the exclusion of others [8,21]. Reviewers often come to the review ill-prepared. Inappropriate behavior is exhibited during the review process, more often in the form of personal attacks on the product producer or presenter than comments on the deliverable. Participation during the review can be uneven, with some people speaking too much and others not enough. The moderator function can be difficult to perform, since peers often are called upon to discipline one another. There are problems with management's role in the review process as well. Managers often attempt to attend reviews out of curiosity or in an attempt to do a performance appraisal, and this has inhibited many reviews.

Such factors lead to negative attitudes toward reviews. Managers can be unsupportive because they feel left out of the process. Producers might - reject reviews because they want their work to be personal and not owned by a team. Reviewers often feel they are neither heard nor appreciated. Moderators can seem dictatorial because they are trying to develop harmony and make certain that procedures are followed. The problems are well-documented, both in the authors' experience and the literature [28,36]. The next section discusses how some of these problems might be relieved by greater attention to roles.

## 3. Roles in team product reviews

An examination of the roles required in a review offers a means of dealing with some of the above problems. Roles reveal a link between individual behavior and the social structures imposed on an individual [5]. Roles provide a means for examining and evaluating the process of social interaction that occurs in reviews.

![](/api/attachments/7XW6U3P9/fulltext/images/f24212b6bf3c03a27b2ec900e7c30eff144766f74c6d10070aa6c9b752f363fa.jpg)  
Fig. 1. Role classification scheme (adapted from Benne and Sheats, 1948).

## 3.1 Background on roles

The history of the study of roles dates back to the 1930s when sociologists and anthropologists began to write about the concept of role as a key to explaining the origins of social behavior [27,29]. Since then, researchers in sociology, psychology, social psychology, organizational psychology, and small group behavior have studied roles, and the field of role theory has emerged as a useful discipline [4].

A person's defined role within a group – whether that group be a family unit, a task force, an organization, or a society – can come from several sources. A role may be based on subject expertise, personality traits, status, and position [4]. Where a role is based on a relatively stable characteristic like personality, it is likely to be consistent across situations. But roles may vary from one situation to the next as a function of the social interaction process [7]. Thus, roles can be affected by several interdependent sources, including organizational, social, and personal demands [18].

Katz and Kahn [24] built on the sociological study of roles with a model of the organization as a system of roles. Their theoretical model of roles accounts for the context in which social interaction takes place. The model includes not only the person who takes the role (the “focal person”) but also other people who are sources of role expectations (the “role senders”). This model makes explicit a number of potential perceptual gaps: between role expectations and role messages sent; between role messages sent and those received; and between role messages received and action taken. Thus, Katz and Kahn’s model reflects the real complexity of studying human roles in organizational contexts.

Considerable attention has been devoted to the study of roles in the specific context of small groups. An early study by Benne and Sheats [3] classified group member roles into three categories: (1) group task roles, (2) socio-emotional group building and maintenance roles, and (3) “individual” roles. Their classification, based upon observation of interacting groups, is consistent with a central theme of group research that recognizes the importance of both task-oriented and socio-emotional behaviors [7]. The individual role category consists of behavior directed toward satisfaction of a participant’s individual needs: those not relevant to group task or functioning, for example, “aggressor” or “special interest pleader." Other role classifications, often based on categories of interaction behavior, are consistent with the framework [1,7,15]. Figure 1 is an adaptation of the Benne and Sheats roles of greatest interest here, focusing specifically on group task and group building (socio-emotional) roles.

<table><tr><td>FUNCTIONS:</td><td>Presenter</td><td>Moderator</td><td>Recorder</td><td>Reviewer</td></tr><tr><td colspan="5">TASK ROLES</td></tr><tr><td>Initiator/contributor</td><td></td><td></td><td></td><td>X</td></tr><tr><td>Info/Opinion seeker</td><td>X</td><td>X</td><td></td><td>X</td></tr><tr><td>Info/Opinion giver</td><td>X</td><td>X</td><td></td><td>X</td></tr><tr><td>Elaborator</td><td>X</td><td>X</td><td></td><td>X</td></tr><tr><td>Coordinator</td><td>X</td><td>X</td><td></td><td></td></tr><tr><td>Orienter</td><td></td><td>X</td><td></td><td></td></tr><tr><td>Evaluator</td><td></td><td>X</td><td></td><td>X</td></tr><tr><td>Energizer</td><td></td><td>X</td><td></td><td></td></tr><tr><td>Proceduralist</td><td></td><td>X</td><td></td><td></td></tr><tr><td>Recorder</td><td></td><td></td><td>X</td><td></td></tr><tr><td colspan="5">GROUP BUILDING AND MAINTENANCE ROLES</td></tr><tr><td>Encourager</td><td></td><td>X</td><td></td><td>X</td></tr><tr><td>Harmonizer</td><td></td><td>X</td><td></td><td>X</td></tr><tr><td>Compromiser</td><td></td><td>X</td><td></td><td>X</td></tr><tr><td>Gatekeeper</td><td></td><td>X</td><td></td><td></td></tr><tr><td>Standard setter</td><td></td><td>X</td><td></td><td>X</td></tr><tr><td>Group observer</td><td></td><td>X</td><td></td><td></td></tr><tr><td>Follower</td><td>X</td><td>X</td><td>X</td><td>X</td></tr></table>

Fig. 2. Roles mapped to functions in a traditional team product review.

## 3.2 Applying role concepts to team product reviews

A typical review session requires that several functions be performed. A presenter, who may or may not be the product producer, introduces the deliverable and ensures that all review participants understand the product being reviewed. A moderator enforces order and timely completion of the review. The moderator also ensures that all participants are recognized, and orients the team by summarizing what has been said. A recorder, usually using a flip chart, publicly records any action that must be taken. The reviewers, usually numbering from three to five, look for errors and omissions in the deliverable. These reviewers seek information and opinion, provide information and opinion, support and encourage the producer by recognizing positive aspects of the product, and critically evaluate the product to ensure that it meets standards and will be operational in the context of the assembled system.

To analyze roles in reviews, a mapping was created between each function in a review and role categories (see Figure 2). First, Benne and Sheats [3] task and group building roles were examined to find which were most relevant to the review process. Individual roles were eliminated from consideration, because they focus on behaviors that promote individual rather than group goals. The adapted role scheme was used to examine what roles were filled by each function during a review, with the analysis based on prescriptive literature [28,36] and the authors' experience.

## 4. Leveraging roles with team technology

Each function within a review needs a complex set of roles, the most complex functions being the moderator and the reviewer. Many roles must be filled by the same person, creating considerable potential for both role overload and role conflict.

A role analysis approach reveals the “stress points” in a review. For example, two of the moderator’s roles are energizer and proceduralist. An energizer may want to be creative and do away with structure, while a proceduralist may need to impose structure to keep the group on track.

Team technology has considerable potential not only for making some of the roles required within these functions easier to fill, but for transferring some roles from humans to the machine, thus alleviating role overload.

## 4.1 Background on team technology

The general concept of team technology has been implemented in a number of different ways. DeSanctis and Gallupe's general framework [13] includes centralized decision rooms for both small and large groups, dispersed local area decision networks, and computer-mediated conferences. Kraemer and King's [26] review includes electronic boardrooms, teleconferencing facilities, group networks, information centers, decision conference centers, and collaboration laboratories. Here, the “team technology” label means any computer and communications system that is specifically designed to support team interaction and group work.

Hardware for team technology might include:

\- a dedicated meeting room, transportable technology set up for specific meetings, or remote workstations;

\- a terminal/input device for each participant;

\- networked terminals;

\- a facilitator-controlled terminal that can collect input from all terminals;

\- a large screen projector or windows/split screens if remote; and

\- video and audio links for remote sites.

Software for team technology might support:

\- idea generation through electronic brainstorming;

\- idea evaluation through voting, rating, ranking, etc.; and

\- procedural control through automated agendas.

Laboratory studies have found that groups that used team technology experience increased satisfaction $[22,34]$ and produce higher quality decisions $[17,34]$ than nonsupported groups. Field studies have found high satisfaction and efficiency for team technology-supported groups $[12,31]$ . Results are by no means consistent, however, as reviews of the literature show $[11,32]$ . But the base of experience with team technology is growing, and there is a need for more in-depth understanding of the role that technology plays in meetings and how groups perceive it.

Team technology has most often been used in decision-oriented meetings: strategic planning, problem analysis, and alternatives evaluation. It has not yet been widely applied to the review process, and the study of roles within technology-supported meetings has only recently begun $[37]$ . There is potential synergy from bringing these ideas together.

## 4.2 Human and machine roles in team product reviews

We suggest three ways in which team technology could enhance the review process from a role perspective: (1) by replacing roles filled by humans, (2) by assisting humans in their roles, thus making them easier to fill, and (3) by creating and assuming new roles not previously possible that contribute to a team's effectiveness and/or efficiency. The discussion that follows refers to different team technology features, some of which are available in existing systems, while others are ideas about future designs. Thus we are not focusing on a specific implementation of team technology.

Team technology can replace a human as the recorder – the role of making a record of group deliberations and serving as the group's memory. Corrections or other action points could be recorded quickly and distributed via the system. The group's “memory” could be enhanced considerably when stored in the system.

A role with which the technology could assist is proceduralist – the role of performing routine tasks to expedite group movement. The system could be programmed with an option of having the software control the agenda and prevent the group from moving on to a new topic until resolution had been reached on the current topic. This would make the moderator function easier to perform, since the software and not the human would keep the team focused.

The system could enlarge the role of proceduralist by linking the review process with other activities in the development life cycle. Project management could be facilitated by the use of team technology, as milestones and completion times could be inputs to a project management system. Project management also could be available on-line as a reference during the review process if questions on deadlines or subsystem interfaces arose.

The roles of information/opinion seeker and information/opinion giver could be assisted by gathering electronic input from the review team. Opinions could be entered at individual keyboards quickly and anonymously. Since all input would be captured by the system, no ideas would be lost. The moderator would have quick access to opinions on any question by electronically polling each reviewer. The review team also could be linked to other automated storage of system documentation or company information. Data dictionary entries or graphics of systems diagrams from CASE tools could be displayed for the group. Links to organizational data that otherwise might not be part of the system documentation also could be established. The meeting would cease to be isolated from other parts of the company, because links would be established from the meeting room to other automated data stored by the company. The recorder role, when taken over by the system, becomes an information-giver role as well.

Team technology could assist the harmonizer role, which mediates differences between members to assure group harmony. During a review, it is easy for reviewers to become attackers and for the presenter to become defensive. Team technology could help by screening the language, thus relieving the moderator from some duties of assuring group harmony. Templates or prompts could be used to input comments electronically, such as “I don’t understand ——,” where the reviewer fills in the blank. This would promote the use of non-threatening language. Comments could be screened for inappropriate phrases, such as criticisms beginning with a “You …,” which could be considered to be blaming statements. The system could provide displays of questions like “Presenter, do you feel defensive?” or “How does the group feel about the process right now?” The system could also do periodic “togetherness checks” where individuals type in how they feel about the mood of the review at a given point. There would be less need for disciplining comments by the moderator since most suggestions would be made electronically and the software could temper responses.

A new role that would be created and assumed by the system is the clearinghouse role. This is a combination of information/opinion seeker, information/opinion giver, and coordinator – a combination that humans are rarely able to accomplish comprehensively and fairly. Participants using team technology could “talk electronically” at the same time via simultaneous keyboard or touch screen input. Electronic talk allows participants to clear their minds of items that need to become part of the later agenda. This means that “I forgot what I was going to say” should be less common. Once ideas are input to the system, participants can concentrate on the immediate task.

Another new role for team technology might be called the protectionist – a role that protects individuals from personal criticism about their comments. Several features of team technology make this role possible. When reviewers enter ideas about possible errors in the deliverable as presented and those ideas are displayed on the public screen, the focus of attention is removed from the person who entered the idea and is centered instead on the idea itself, thus diluting personal criticism. Anonymity of input to the system also provides a protectionist role, since the source of keyed comments is not revealed. Groups of non-peers or managers could participate in reviews without undesirable consequences. The open environment provided by anonymous input may be more conducive to expressing ideas and opinions without regard to the negative effects of rank and status influence.

## 4.3 Changed roles lead to changed procedures

A significant implication of the discussion of human and machine roles is that the potential for technological support in reviews can be reached only if participants are willing to change procedures. The technology could aid in achieving change. For example, the moderator could ask reviewers to acknowledge appropriate review behavior by displaying behavior guidelines on each terminal and waiting for each reviewer to read and accept them. Guidelines and review objectives could also be displayed on the public screen; this would unify and focus the group. The same information would continue to be available at each private terminal as a reference at any time during the meeting. The moderator could focus the group on the issues by asking for pros and cons of an idea and comments on the consequences of a positive or negative vote. Actual representation of alternatives, such as a data flow diagram, could be displayed on split screens to determine the results of different approaches, and votes could be taken on alternatives (for instance, “Do you feel we should have the representation on the right or the left?”).

Checklists can be reviewed to ensure items are not overlooked. For an activity such as requirements definition, prompts might be initiated from the checklist with questions such as “Have you considered the cost reductions of employee overtime?” or “Could there be lawsuits as a result of this business tactic?” Further prompts could be included about business or system objectives, with questions such as “When? How Many? In what area?” These lists could be built as a result of past reviews. The prompting procedure could be implemented in a similar way to an on-line help function in a typical software package. In essence, an “expert moderator system” could be built to relieve the human moderator.

Other aspects of the review process could be changed via team technology. Admission to the review might be contingent on having prepared several cogent comments on the product to be reviewed or answers to some set questions about the type of deliverable being presented. This would address the problem of ill-prepared attendees.

Team technology could also change the tone and nature of reviews. The process is likely to become more structured and undesirable features of human roles could be tempered. The technology could be used to play a policing role so that humans could focus on building group cohesiveness. Such a procedure compares to having robots do dirty, dangerous, and boring work.

## 5. A prescription for change

To reap the full benefits of team technology in reviews, the process that is used should be understood, analyzed, and revised where appropriate. A central thesis of this paper has been that a valuable means of examining processes is to examine the roles that must be filled in a successful small group activity.

A weakness of past methods that have been used to build information systems is that changes have been made incrementally. Developers have often used technology merely to automate existing procedures without examining their effectiveness and without considering new procedures made possible by automation. Order processing is one example of this problem. Order processing evolved slowly: from manual order taking and manual processing, to manual order taking and automated batch processing, to automated on-line order taking by order taking personnel, and finally to automated on-line order entry by customers. Some intermediate steps in this evolution were necessary due to technology constraints, but other steps might have been the result of thinking too small. One way to enlarge thinking is by an examination by developers of the roles filled by internal personnel, technology, and the customer. The automation of order processing might have evolved much more quickly than it did, but failure to examine roles and determine “who would do what?” was as big a factor in slowing the transition as was the capability of underlying technology.

The prescription suggested here is to examine existing roles filled by all parties involved in a process, and then to reassign roles among existing and new role players. One new player in most organizational processes is information technology. Such “role thinking” may alleviate many of the problems of assimilating new technologies.

## 6. Conclusion

The roles required during a review process bear investigation. This paper examined the many roles that need to be filled and how team technology can assist. Empirical research can follow to answer the questions raised here. For example, can team technology lessen role conflict and role overload for moderators and reviewers? Does technological assistance result in enhanced participant satisfaction? Are the expected impacts on effectiveness measurable? Does the system facilitate larger groups of reviewers, or can there be fewer reviewers, because the system does the prompting? Should reviewer performance be scored by the system and future reviewers chosen on performance scores? These are areas where empirical research can make a contribution.

The technology for enhancing review processes is available today. The use of role analysis is an attempt to merge the review process with a technological environment for enhancing group work. The hope is that we can avoid the misuse of technology that often occurs when we automate without first examining the effects of automation. This paper is an attempt to evaluate the processes and roles needed to use team technology in reviews, with an overall goal of enhancing the process and outcomes of reviews, ultimately resulting in higher quality information systems.

Acknowledgements: This research was partially funded by the IBM Corporation under Agreement #U1906. An earlier version of this paper appeared in the Proceedings of the 1989 Conference on Organization and Information Systems, Bled, Yugoslavia, September, 1989.

## References

[1] Bales, R.F. Interaction Process Analysis: A Method for the Study of Small Groups. Reading, MA.: Addison-Wesley, 1950.

[2] Beauclair, R.A. and Straub, D. Utilizing GDSS technology: Final report on a recent empirical study. Information & Management, 18(5), May 1990, 213–220.

[3] Benne, K.D. and Sheats, P. Functional roles of group members. Journal of Social Issues, 4(2), 1948, 41–49.

[4] Biddle, B.J. and Thomas, E.J. Role Theory: Concepts and Research. New York: John Wiley & Sons, Inc., 1966.

[5] Biddle, B.J. Role Theory: Expectations, Identifies, and Behaviors. New York: Academic Press, 1979.

[6] Boehm, B. Developing small-scale application software products: Some experimental results. Proceedings of IFIP 8th World Computer Conference, October, 1980, 321–326.

[7] Bormann, E.G. Discussion and Group Methods: Theory and Practice. Second edition. New York, N.Y.: Harper & Row, 1975.

[8] Bostrom, R.P. Successful application of communication techniques to improve the systems development process. Indiana University, IRMIS Working Paper, 1987.

[9] Bostrom, R.P. and Anson, R.G. A case for collaborative work support systems in a meeting environment. Information Executive, 1(1), Fall, 1988.

[10] Crossman, T.D. Some experiences in the use of inspection teams in applications development. Proceedings of Share. Inc. Applications Development Symposium, October, 1979, 163–168.

[11] Dennis, A.R., George, J.F., Jessup, L.M., Nunamaker, Jr., J.F., and Vogel, D. Information technology to support meetings. MIS Quarterly, 12(4), December 1988, 591–624.

[12] Dennis, A.R., Vogel, D., Nunamaker, J., and Heminger, A. Bringing automated support to large groups: The Burr-Brown experience. Information & Management, 18(3), March 1990, 111–121.

[13] DeSanctis, G. and Gallupe, R.B. A foundation for group decision support systems design. Management Science, 33(5), 1987, 589–609.

[14] Fagan, M. Design and code inspections to reduce errors in program development. IBM Systems Journal, 15(3), July, 1976, 182–211.

[15] Fisher, B.A. Decision emergence: Phases in group decision making. Speech Monographs, 37, 1970, 53–66.

[16] Freedman, D.D. and Weinberg, G.M. Handbook of Walkthroughs. Inspections, and Technical Reviews. Boston: Little, Brown and Company, Inc., 1982.

[17] Gallupe, R.B., DeSanctis, G. and Dickson, G.W. Computer-based support for group problem-finding: An experimental investigation. MIS Quarterly, 12(2), June 1988, 277–298.

[18] Graen, G. Role-making processes within complex organizations. In Dunnette, M.D. (ed.) Handbook of Industrial and Organizational Psychology. Chicago: Rand McNally College Publishing Company, 1976, 1201–1245.

[19] Henderson, J. Cooperative behavior in information systems planning and design. Center for Information Systems Research, Sloan School of Management, MIT, CISR Working Paper #164, 1987.

[20] Huber, G.P. Issues in the design of group decision support systems. MIS Quarterly, 8(3), 1984, 195–204.

[21] Janis, I.L. Victims of Groupthink. Houghton Mifflin, Boston, MA, 1972.

[22] Jessup, L., Tansik, D.A., and Laase, T.D. Group problem solving in an automated environment: The effects of anonymity and proximity on group process and outcome with a group decision support system. Proceedings of the

1988 Annual Meeting of the Academy of Management, August 1988, 237–241.

[23] Johansen, R. Groupware: Computer Support for Business Teams. New York: The Free Press, 1988.

[24] Katz, D. and Kahn, R.L. The Social Psychology of Organizations. Second Edition. New York: John Wiley and Sons, 1978.

[25] Kozar, K.A. and Zigurs, I. Team product reviews using teamwork systems. Proceedings of the 1989 Conference on Organization and Information Systems, Bled, Yugoslavia, September, 1989.

[26] Kraemer, K.L. and King, J.L. Computer-based systems for cooperative work and group decision making. ACM Computing Surveys, 20(2), June 1988, 115–146.

[27] Linton, R. The Study of Man. New York: Appleton-Century, 1936.

[28] Lippard, M.S. Structured methods: the impossible dream? Computerworld, Dec. 1, 1980, InDepth Section, 1–15.

[29] Mead, G.H. Mind. Self and Society. Chicago: University of Chicago Press, 1934.

[30] Myers, G. A controlled experiment in program testing and code walkthroughs-inspections. Communications of the ACM, September, 1978, 760–768.

[31] Nunamaker, Jr., J.F., Vogel, D., Heminger, A., and Martz, B. Group support systems in practice: Experience at IBM. Proceedings of the Twenty-Second Annual Hawaii International Conference on System Sciences, 1989, 378–386.

[32] Pinsonneault, A. and Kraemer, K.L. The impact of technological support on groups: An assessment of the empirical research. Decision Support Systems, 5, 1989, 197–216.

[33] Schneiderman, B. Group processes in programming. Datamation, January, 1980, 138–140.

[34] Steeb, R. and Johnston, S.C. A computer-based interactive system for group decisionmaking. IEEE Transactions on Systems, Man, and Cybernetics, SMC-11(8), August 1981, 544–552.

[35] Thayer, T.A., Lipow, M., and Nelson, E.C. Software Reliability: A Study of Large Project Reality. New York: North-Holland Press, 1978.

[36] Yourdon, E. Structured Walkthroughs. Fourth Edition. Englewood Cliffs, NJ: Prentice-Hall, Inc., 1989.

[37] Zigurs, I. and Kozar, K.A. A proposal to IBM for a program of research on teamwork concepts using the IBM decision support center, February 1990.
