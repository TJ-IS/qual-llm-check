---
otero_id: 18656
otero_key: "85YV7SJX"
title: "Bringing automated support to large groups: The Burr-Brown experience"
authors: "Alan R. Dennis; Alan R. Heminger; J.F. Nunamaker; Douglas R. Vogel"
year: "1990"
journal: "Information & Management"
doi: "10.1016/0378-7206(90)90065-p"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Bringing Automated Support to Large Groups: The Burr–Brown Experience

Alan R. Dennis, Alan R. Heminger,
J.F. Nunamaker, Jr., Douglas R. Vogel
University of Arizona, Management Information Systems Department, Tucson, AZ 85721, USA

The area of computer-assisted support for group work has significant practical implications for most areas of organizational practice. The ability to enhance the effectiveness and efficiency of group efforts while meeting with user satisfaction would be a valuable plus for nearly all organizations. However, early research into computer support for group work indicated that such systems would likely be limited in their effectiveness to groups of 3 to 5 persons. Later development showed that electronic meeting support (EMS) technology could be effectively used with groups of 8 to 16 participants. The session here demonstrates that EMS technology can be effectively implemented with a planning group of 31 participants. The company, Burr-Brown, used the EMS developed at the University of Arizona MIS Department to carry out its annual strategic planning. Measures of effectiveness, efficiency, and user satisfaction all indicated that the system provided the intended group support during the three day planning session.

Keywords: Collaborative work systems, Computer assisted meetings, CWS, Electronic meeting systems, EMS, Group decision support systems, GDSS.

![](/api/attachments/85YV7SJX/fulltext/images/cf31822c70fcaf0204ddb81a1d36594b8a01ff7c437e31f4f386d44edc4b4140.jpg)

Alan R. Dennis is a doctoral student in MIS at the University of Arizona. He received a Bachelor of Computer Science from Acadia University and an MBA from Queen's University in Kingston, Ontario, and was a winner of the AACSB National Doctoral Fellowship. Prior to entering the Arizona doctoral program, he spent three years as a faculty member of the Queen's University School of Business, and has published several conference proceedings, book chapters and journal articles (including MIS Quarterly and Data Base). His current research interests include electronic meeting systems, decision support systems, and business graphics.

## Introduction

Much of the research to date on the use of information systems to support group work has

![](/api/attachments/85YV7SJX/fulltext/images/120e626c3e4cc307a6c5795da40541275872af2222e33ab67719521d336e6686.jpg)

Douglas R. Vogel is an Assistant Professor of MIS. He has been involved with computers and computer systems in various capacities for over 20 years. He received his M.S. in Computer Science from U.C.L.A. in 1972 and his Ph.D. in MIS from the University of Minnesota in 1986 where he was also research coordinator for the MIS Research Center. His current research interests bridge the business and academic communities in addressing questions of the impact of management information systems on aspects of interpersonal communication, group decision making, and organizational productivity.

![](/api/attachments/85YV7SJX/fulltext/images/c12e2259d3662e109beb154983eccddb0c90bad27309a24eab6d3479a1b6466c.jpg)

Jay F. Nunamaker, Jr., is Head of the Department of Management Information Systems and is a Professor of Management Information Systems (MIS) and Computer Science at the University of Arizona. He received a PhD from Case Institute of Technology in systems engineering and operations research. He was an Associate Professor of Computer Science and Industrial Administration at Purdue University. Dr. Nunamaker joined the faculty at the University of Arizona in

1974 to develop the MIS program. He has authored numerous papers on group decision support systems, the automation of software construction, performance evaluation of computer systems, decision support systems for systems analysis and design, and has lectured throughout Europe, Russia, Asia, and South America. Dr. Nunamaker is Chairman of the Association for Computing Machinery (ACM) Curriculum Committee on Information Systems.

![](/api/attachments/85YV7SJX/fulltext/images/46870c4c526ca09b64efbc381c8e9c1a82c584437d798f4b6428117106ec6bac.jpg)

Alan R. Heminger is an Assistant Professor of MIS in the Decision and Information Systems Department at Indiana University. He received a Ph.D. in MIS at the University of Arizona in December, 1988, and an M.S. from the Educational Psychology Department of California State University at Hayward in 1978. His current research interests are in the area of computer aided support for group work, with particular interest in the assessment of such systems in oper-

ational environments, and the problem of hindsight bias as it affects group work. Heminger was selected as a Doctoral Fellow by the Society for Information Management (SIM) in 1987.

focused on small to medium size groups. Laboratory experiments have most often studied small groups of three to five persons [2,31,41,42,47,60, 62]. Organizational studies have typically reported uses by medium size groups of eight to 12 participants [5,19,39,58,59], although a few have studied larger groups [37,38,56]. This paper, which reports on the use of an Electronic Meeting Support (EMS) system by a large group (thirty-one participants) in a business setting, is an initial step toward answering the question for large groups. For three days in early January, 1988, 31 senior managers of Burr–Brown Corporation, an international electronics company, used the University of Arizona EMS environment to support their strategic planning meeting. This paper describes their experience.

## The GDSS / EMS Concept

Initial systems developed to assist groups to work together were called Group Decision Support Systems (GDSS) partly as an extension of the concept of Decision Support Systems (DSS), which were developed in the single user environment. A GDSS has been defined as an integrated computer-based system to facilitate the solution of an unstructured or semi-structured task by a group that has joint responsibility for performing it $[12]$ . However, while the initial focus of the use of IS technology to support groups was on decision making, it has become clear that the technology can also assist groups in a wide range of collaborative work tasks, not just decision making $[9,13,28]$ . For example, the University of Arizona system has been used for idea generation, topic discussion, information sharing, knowledge elicitation and consensus building, as well as for decision making. Thus, we find the label of Electronic Meeting Support (EMS) to be much more descriptive of the use of these systems. Therefore, we will use the term EMS throughout this paper.

Most references to EMS or GDSS usually use the terms to mean the software systems used to enhance communication between group members. However, we believe that a five component model of the EMS environment is more appropriate, as it more fully captures the range of features found to be necessary to support collaborative group work [9]. These components are: the facility, hardware, software, procedures, and facilitation of the group work process.

## Previous Research

Much previous EMS research has focused on its use by small groups of three to five students in laboratory experiments. This was largely built on the results of previous non-EMS group studies which suggest that the most effective group size is small. A review of non-EMS supported group research by Shaw, in 1981 [47], suggested that as the size of the group increases, group effectiveness increases until some optimum group size is reached. Based on past research, this optimum group size is three [31,32] or five [17,18,47,50]. Once size rises above this, effectiveness decreases, as there is less opportunity for group members to participate; a few participants dominating the process can largely preclude others' participation. If two people dominate a meeting of five, three are kept from participating. If the same two dominate a meeting of 20, 18 people are not heard. Thus, it is not surprising that members of larger groups experience less satisfaction with the work process than do members of small groups [12,30,34].

While authors from non-EMS fields have suggested that effective group size is limited, research within the field has proceeded with small, medium, and large groups as the focus of inquiry $[15,58,59,60]$ . Still, most previously reported research has used small groups (3–6 group members) or medium-sized groups (7–16 group members) $[10]$ , probably because few EMSs capable of supporting large groups (17 or more participants) presently exist.

The issue of structure and flexibility in group work is also important. The addition of structure to group processes has been shown to increase the success of group meetings $[8,20]$ . However, groups also need flexibility. While several models of group work have been proposed (eg., Simon's three stage model of intelligence, design and choice $[49]$ ), groups do not always follow such an orderly and straightforward process $[41,42,43]$ . Groups normally follow very circuitous routes to arrive at an outcome. An effective EMS must, therefore, balance the desire for increased structure, with the need for flexibility.

If we examine the user view of effectiveness, efficiency and satisfaction with EMS from previous studies, we see a somewhat conflicting picture. While both small and medium-sized groups have shown high effectiveness (ie., higher quality group meeting outcomes), with EMS use $[15,38,51,59,62]$ , the questions of efficiency and satisfaction have shown mixed results. Efficiency can be considered as the amount of participation per member in the group task per unit time. It is generally accepted that the use of EMS increases group member participation $[9]$ . The time required to complete tasks using an EMS, relative to a manual system, seems to increase with small groups and low to medium complexity tasks $[15,27,51]$ . On the other hand, it seems to decrease time relative to manual methods for medium-sized groups with more complex tasks $[37,58]$ .

User satisfaction is a key issue for EMS research. If the use of EMS to support group work does not increase the participants' satisfaction with the group process, it will be difficult to convince practitioners to adopt it. Research results are contradictory. While two studies with small groups in experimental settings have shown that EMS use decreases satisfaction $[15,60]$ , studies in operational environments have shown that EMS use produces high satisfaction $[27,37,38,48,51,59]$ . These differences may be due, in part, to the differences in the EMS employed in the different settings.

## Questions of Interest

Because there has been little reported research of the use of EMS by large groups, there is a need for baseline data as a starting point for future research. A review of previous research suggests five questions of particular interest which will be explored here:

1. Can an EMS successfully support planning by a large group?

2. Can an EMS provide both structure and flexibility to the planning group in meeting its goals?

3. Can an EMS-supported process be considered efficient, measured by high group work output per input of time?

4. Can an EMS-supported process be effective?

5. Can an EMS-supported process be satisfying to the participants?

## The EMS Environment

The EMS environment developed at the University of Arizona includes the facility, hardware, software, procedures, and facilitation [see 10 for details].

## The Facility

The EMS facility is a second generation facility of the MIS Department at the University of Arizona. It is located on campus, in the Business and Public Administration Building. It consists of the main meeting room, a control room and a small conference room. The rooms have been heavily sound and air conditioned to provide a quiet, comfortable environment for the participants with sufficient cooling for the equipment. The main room has two rows of workstations, with 24 PS/2 computers, arranged in concentric arcs on tiered flooring to provide excellent sight lines for each participant. Behind the second tier of workstations is a row of gallery seats. Up to 48 people can be accommodated in the two tiers and another 12 can be accommodated in gallery seating at the rear of the room. The facilitator's station at the front of the room has two computers of its own and the ability to control all the technology in the room. Other equipment available in the room includes: rear-projection screens, white boards, a copy stand (with multiple inputs), and sound equipment; all aimed to provide a broad support of non-intrusive technology for the support of group work.

The atmosphere of the room is comfortable and professional. There is a large amount of technological support available, but the room is designed to mask the details of the technology and to promote interaction through a seating arrangement which allows good lines of sight and good acoustics for all participants.

## Hardware

The system uses an IBM token ring network connecting the following hardware:

\- 24 IBM PS/2 Model 50s, located in participant workstations.

\- 1 PS/2 Model 60 and 1 PS/2 Model 80 in the facilitator's station.

\- A PS/2 Model 80 in the control room which serves as a file server for the system.

## Software

The planning tools are an integrated set of tools that were developed to run on a networked system of IBM PC compatible micro-computers. While the tools can stand alone, each was designed to work as a part of a unified system: receiving inputs from other tools, providing outputs to other tools, or both. The major tools that were used by this planning group were Electronic Brainstorming (EBS), Issue Identification and Analysis (IA), Topic Commenter (TC), File Reader, and the voting module (VOTE).

Electronic Brainstorming (EBS) allows participants to share comments anonymously on a specific question. Each participant works simultaneously, sharing information on the same question, but without interacting directly. The ideas generated with this tool become the input to the Issue Analyzer (IA) This facilitates the analysis and organization of the ideas generated. The VOTE module allows a variety of voting options; it is often used in conjunction with IA to aid the participants in developing a rank ordering of key issues. Discussion of topics is facilitated through the use of the Topic Commenter (TC) tool. This allows interactive simultaneous input by all participants on the issues raised. File Reader is used to make both outside files and those created during the group's process available to each of the participants. Using it, each participant can individually call up any of the files available on the system.

## Procedures

Because the tools are flexible in their application and because they can be strung together in a variety of ways, the system has the ability to meet the needs of many different groups. The procedures, which are tailored to each group's needs in a pre-planning session, map the intended process to the use of the computer tools. A typical model for group work mapped to the Arizona EMS is shown in Figure 1.

![](/api/attachments/85YV7SJX/fulltext/images/66385df48bb399d7247600a9c5014aedbbd8a638b972d22be518fc3a1fbf3e5f.jpg)  
Fig. 1. A Collaborative Work Model.

## Facilitation

The facilitation provided for this session consisted of a facilitator, an assistant facilitator and three assistants. The assistants helped the participants to use the various hardware and software features of the room and, as needed, provided clerical support by making copies of the various documents generated in the sessions.

The facilitator's role is that of implementing the plan for the sessions, keeping the participants on track, assessing the need for modifications to the plan and other such duties. This role serves a number of important functions. First, it provides a focal person who is responsible for the implementation of the plan for the session. Second, it provides a relatively neutral leader for the meeting – one whose role was that of monitoring the process, rather than pressing for a particular goal – thereby enabling the CEO to participate in the planning session.

## Background of the Organization

Burr–Brown, the company profiled in this study, is a publicly held corporation which manufactures and sells parts to other electronics manufacturers. It has approximately 1500 employees and \$150 million in annual sales. Besides the CEO, Jim Burns, participants in the session included senior managers of functional, product, and geographic divisions. The company, which has its headquarters in Tucson, is forward looking, with a reputation for making use of developing technologies to enhance its competitive position.

Upon learning of our work in EMS development, Jim Burns decided to use the system for Burr–Brown's annual strategic planning meeting. This meeting is a regular part of their organizational process. In past years, it had been carried out at off-site locations using manual methods. The company paid to use our facilities for this planning session, as they had for facilities used in manual sessions in previous years.

The participants were all senior managers at the division manager level and above. Thirty-one members of the organization participated over a three day period. Almost 50% of the participants had very little prior planning experience (they had participated in one to five prior planning sessions). The remaining 50% ranged from moderate experience (6–11 sessions) to a great deal of experience (50 sessions).

Additional members of the organization provided logistical support and/or observed the process. The Chairman of the Board was among these.

## Chronology

Three pre-planning meetings were held with representatives of the company. Through these, company goals for the sessions were refined and plans were developed. Although one pre-planning session usually suffices to prepare for an automated session, Jim Burns was not able to be present at the first two and it was not until he took part that the pre-planning details were settled.

Prior to the planning meeting, each division prepared brief one-year and five-year proposed plans. These provided general and specific divisional objectives supported by projected budgets. They were distributed to participants in advance of the session, and provided a framework from which to begin work.

The three days were divided between long term strategic planning (day one), short range action planning (day two) and a wrap-up of the two processes (day three). The planning needs of each of the organization's eleven divisions were addressed in these areas. Both automated and face to face discussions were used to maximize the effectiveness of the process. The full chronology of events is presented in Appendix A.

On the first morning, Electronic Brainstorming (EBS) was used to generate ideas about expected corporate performance in the coming years. The comments from this session were then organized and sorted using Issue Analyzer (IA). This information formed the basis from which each of the divisional plans was to be considered. Through the rest of day one, each of the divisional 5-year plans was examined using the Topic Commenter (TC) tool.

Day two was used to consider each of the divisions again – this time in light of a one-year action plan. TC was again used for this task. Late in the afternoon, EBS and IA were used to generate and organize ideas on how to accomplish the next year's overall corporate objectives.

Day three began with a continuation of the process of identifying ways to accomplish the next year's goals. The VOTE module was used to rank order the generated ideas three times – first by overall benefit to the firm, second by time (short-term versus long-term) and third, feasibility. The top five issues from the benefit ranking were then entered into TC for further group discussion. After lunch on the third day, the participants were divided by the CEO into four work groups, with each examining the developed issues from one of the following considerations: gross margin improvement, spending control and overall perspective.

At the end of this process, each work group presented its findings to the entire group. Finally, an overview of what had been accomplished was presented by the CEO.

## Data Collection

Data were collected from the session in a number of ways. First, the EMS provides data regarding the number of comments generated, the distribution of comments, etc. In addition, the participants were given a post-session questionnaire in which they were asked to assess the process (See Appendix B for the questionnaire). Finally, there was a follow-up interview with the CEO and two senior managers three months after the planning session.

The first item of the post-session questionnaire asked for the planning experience of each of the participants. Items 2 through 14 were presented as statements in which the respondents were asked to indicate their agreement with a statement by entering a number on a Likert scale showing level of agreement; “1” indicated strong disagreement and “5” indicated strong agreement.

## Results

We now address the results in terms of the research questions.

Question 1: Can an EMS successfully support planning by a large group?

The company did successfully use the EMS from beginning to end for their group planning session. At the conclusion of the process, 22 of the 26 participants responding to a post-session questionnaire indicated that they believed that the automated process was better than a manual one. The other four expressed no preference.

Question 2: Can an EMS provide both structure and flexibility to the planning group in meeting its goals?

The agenda was defined during pre-meeting sessions. During the planning meeting itself, the pre-set agenda was supported by the system. The use of the tools was successfully implemented. At the same time, several changes were made in the agenda, as the process of planning identified new areas to be explored. These changes were easy to introduce, due to the common data and file formats among the software tools.

Question 3: Can an EMS-supported process be considered efficient, measured by high group-work output per input of time?

The following testimonial was obtained from a Group Vice-President at the three-month follow-up.

"The process allowed us to do in three days what would have taken months to do. In addition, if we had done it manually, we could not have brought more than 9 or 10 people into the process...and there would have been less interaction."

An additional comment from the CEO indicates the perceived efficiency of the system.

"[The EMS-supported process]... lets so many participate. The comments were much more open than we could get with a manual session. If that had been a manual process, only two or three out of the group would have spoken up... The primary difference is that with the manual system used in the past, only 8–10 people could participate."

![](/api/attachments/85YV7SJX/fulltext/images/a79b0b9a071bda6a6f11244412f46816f76b244c401352dcdbda154d7d9cf0bb.jpg)  
Fig. 2. Pattern of Comments over Time.

During each session, the comments made by the participants were recorded. A detailed recording of a 59 minute EBS session on Day two, which tracked the pattern of comments over time and the number of comments made by each participant, showed that a total of 404 separate comments were made.

Figure 2 shows the pattern of comments over time. The thick line shows the total number of comments entered by all users (left axis), while the thin line shows the number of comments per minute (right axis). Over the entire 59 minute session, the rate averaged 5.8 comments per minute, but during the first 10 minutes of the session, comments were entered at about twice the rate. After the first ten minutes, the rate dropped to approximately 7 comments per minute (one comment per workstation about every 3.5 minutes) and gradually decreased to 4 comments per minute over the remaining time. This pattern is consistent with other observed group sessions.

We hypothesize that initial comments are entered faster because participants enter the session with a pool of previously developed ideas. Once initial comments are entered (after the first 10 minutes), the rate of entry decreases. In addition, as the session progresses, participants spend more time reading and absorbing comments of others and generating new ideas before responding. The sharp increase in the rate of comments at the end of the session may be due to the last-minute pressure to make final comments.

![](/api/attachments/85YV7SJX/fulltext/images/ca455a7a9ce18b4707fc50627fb8836bba9590bd9edd551732d999a66097e0a4.jpg)  
Fig. 3. Number of Comments per Workstation.

The number of comments entered at each workstation ranged from 4 to 27, with a mean of 15.9 (median of 16), thus all group members participated. The number of comments per workstation was highly variable, with a standard deviation of 6.5. Figure 3 shows the number of comments per workstation.

Questions 7 through 10 of the post-session questionnaire asked the participants to assess their own involvement in and responsibility for the groups outcome (Figure 4). The participants reported that they believed their own involvement to be important and that they had confidence in the results. However, when asked to express their assessment of the efficiency of the automated system (question 12), 11 found it to be efficient, 9 found it inefficient and 6 were neutral.

<table><tr><td rowspan="2">Question</td><td colspan="3">Strongly Disagree</td><td colspan="2">Strongly Agree</td></tr><tr><td colspan="5">&lt;----&gt;</td></tr><tr><td>2. EMS better than manual system</td><td>0</td><td>0</td><td>4</td><td>7</td><td>15</td></tr><tr><td>3. EMS helps generate ideas</td><td>1</td><td>0</td><td>1</td><td>9</td><td>15</td></tr><tr><td>4. EMS helps identify key issues</td><td>1</td><td>1</td><td>4</td><td>13</td><td>7</td></tr><tr><td>5. EMS helps group achieve goals</td><td>3</td><td>3</td><td>10</td><td>8</td><td>2</td></tr><tr><td>6. Facilitator is important</td><td>0</td><td>1</td><td>5</td><td>15</td><td>5</td></tr><tr><td>7. I Felt responsibility</td><td>2</td><td>6</td><td>6</td><td>11</td><td>1</td></tr><tr><td>8. Outcome reflects my inputs</td><td>0</td><td>2</td><td>6</td><td>15</td><td>3</td></tr><tr><td>9. Confident of correct outcome</td><td>0</td><td>3</td><td>6</td><td>14</td><td>3</td></tr><tr><td>10. Committed to outcome</td><td>1</td><td>2</td><td>5</td><td>13</td><td>5</td></tr><tr><td>11. Satisfied with EMS process</td><td>1</td><td>3</td><td>9</td><td>7</td><td>6</td></tr><tr><td>12. Group&#x27;s process was efficient</td><td>3</td><td>6</td><td>6</td><td>9</td><td>2</td></tr><tr><td>13. Group&#x27;s process was fair</td><td>2</td><td>2</td><td>8</td><td>10</td><td>4</td></tr><tr><td>14. Group&#x27;s process was satisfying</td><td>5</td><td>3</td><td>2</td><td>8</td><td>8</td></tr></table>

Fig. 4. Distribution of Responses to the Post-Session Questionnaire.

Question 4: Can an EMS-supported process be effective?

To determine the effectiveness of the process, data were collected on the participants' assessment of the system at two points in time. The first was on the last day of the session. Their responses are summarized in Figure 4, questions 2–5. In general, the participants reported that they found the process to be effective.

During a follow-up interview, the CEO and two senior managers were asked to assess the effectiveness of the automated system after three months had elapsed. They cited two key dimensions of effectiveness. First, “The anonymity allowed people to ask questions that would not have been asked if names were tagged to the questions” – Jim Burns, CEO, and the comments and suggestions generated by these questions are now being applied. Secondly, as suggested by Ackoff [1], one of the benefits of the planning process is simply the act of planning. The managers learned from it. Again, according to Burns:

"A lot more people are on board with an understanding of what went on. Thus, there is a stronger sense of understanding and agreement among the employees. A lot of education happened that previously hasn't happened during one of these things... People walked in with narrow perceptions of the company and walked out with a CEO's perception. This is the view that is sought in strategic planning, but is usually not achieved."

Perhaps most important, after the corporation has had the opportunity to begin acting on the plans, it views the EMS as effective and valuable. Again, in the words of Burns:

"We would be interested in using it again next year for our strategic planning. I am also interested in using it to work on specific, broad technical problems where we want to bring in managers, supervisors and machine operators to pool their ideas on the subject."

Question 5: Can an EMS-supported process be satisfying to the participants?

This was most clearly summed up on the first day of the session by a Divisional General Manager who said, “This is fun!”. In addition, the post-session questionnaire, answered by participants midway through the last day, supports the belief that the participants prefer an automated system (Figure 5). All participants either were neutral to (4), or in agreement with (22) the statement that an EMS-supported process is better than the manual process.

Responses to questions 3 through 5 demonstrate the participants' assessment of the system's ability to aid the group (Figure 4). The strongest support is for the belief that the EMS aids the group in generating ideas. There is strong support for the assessment that the automated system aids the group in identifying key ideas. Finally, the group mildly supported the belief that the system aided them in achieving their group goals. The fact that the questionnaire was completed prior to the end of the last day could have affected this response.

Responses to question 6 (Figure 6) indicate strong support for the role of the facilitator. This may be particularly important for future development of EMS, because some experimental research has not included a facilitator [e.g., 15]. Thus, while the group concluded that the automated process is clearly better than the manual process, they recognized the value of a facilitator for this type of meeting.

Questions 11 through 14 explore participant satisfaction with the EMS as well as exploring its efficiency, fairness, and group satisfaction (Figure

![](/api/attachments/85YV7SJX/fulltext/images/c69e95f470340d3569d999a9b2211eb198aeabef7613c534f4738a70467650d8.jpg)  
Strongly Disagree <----> Strongly Agree  
Fig. 5. Responses to Question 2 “The computer-aided process is better than the manual process”.

![](/api/attachments/85YV7SJX/fulltext/images/4e82e85588a7abc743ec26e04a31e498e1573e965b17503db07fd303bb8fe046.jpg)  
Fig. 6. Responses to Question 6 “The role of the facilitator is important to group planning”.

4). While opinions on efficiency were divided, the group did demonstrate satisfaction with the computer-aided process and felt that it was fair and satisfying.

## Conclusion

Previous research on the use of EMS has shown that it can, in many cases, increase the meeting effectiveness, meeting efficiency and participant satisfaction in small and medium-sized groups. This study demonstrates that the use of EMS can also be successful for large groups. The answers to all five of the questions posed in this study suggests that EMS has potential for improving the work of large groups. Specifically, the EMS assessed in this study has been shown to successfully support a large planning group, providing both structure and flexibility. It was shown to be both effective and efficient, as well as satisfying to its users. However, a study of a single use of the system cannot be considered to provide conclusive evidence for the answers to any of these questions. Further research is clearly warranted.

## Future Research

After using this system for its planning meeting, Burr–Brown expressed interest in using the system the following year for its strategic planning. That, in fact, has been done, with a similar group, a similar agenda and similar outcomes. Plans are now being made to use the system for a third year, which will provide the opportunity for a longitudinal look at the use of such a system. In addition, other large group research is underway to learn more about the effects of EMS support for such groups. Further work needs to be done to learn more about the optimal group size for this type of system.

<table><tr><td colspan="2">How to accomplish the 1988 objectives using Electronic Brainstorming (EBS) a</td></tr><tr><td>3:23</td><td>EBS Introduction by facilitator</td></tr><tr><td>3:27</td><td>Begin EBS</td></tr><tr><td>4:26</td><td>Break</td></tr><tr><td>4:40</td><td>Introduction to Issue Identification (part of IA)</td></tr><tr><td>4:47</td><td>Begin Issue Identification</td></tr><tr><td>5:25</td><td>End</td></tr></table>

## Acknowledgement

This research was partially supported by the American Assembly of Collegiate Schools of Business, the IBM Management Of Information Systems program, and the Social Sciences and Humanities Research Council of Canada.

## Appendix A: Chronology of Planning Sessions

Wednesday, January 7, 1988

8:30 Introduction by company CEO

8:45 Introduction to the automated system by facilitator

8:53 EBS Starts – Question re expected performance of the company

Issue Analysis by assistant facilitator

10:02 File Reader of Issue Analysis

10:15 CEO comments on comments generated in EBS session

Critique of 5-year Division plans using Topic Commenter (TC)
10:25 Introduction to session and tool
10:30 Begin discussion of Division 1
10:50 Group reads comments
11:09 Enter final comments
11:13 Begin discussion of Division 2
11:30 Group reads comments
11:45 Enter final comments
11:52 Lunch
1:00 Begin discussion of Division 3
1:19 Group reads comments
1:24 Enter final comments
1:31 Begin discussion of Division 4
1:58 Group reads comments
2:10 Enter final comments
2:14 Break
2:32 Begin discussion of Division 5
2:51 Group reads comments
3:03 Enter final comments
3:10 Short break
3:14 Begin discussion of Division 6
3:28 Group reads comments
3:44 Enter final comments
3:50 Short break
3:54 Begin discussion of Division 7
4:10 Group reads comments
4:23 Enter final comments
4:26 Short break
4:30 Begin discussion of Division 8
4:43 Group reads comments
4:50 Enter final comments/break
5:03 Begin discussion of Division 9

5:16 Group reads comments

5:28 Enter final comments

Thursday, January 8, 1988

Division plans for 1988

8:30 CÉO - Objectives

8:40 Introduction to Division 10 plans by participant

Production levels supported by Lotus, copy stand

9:10 Begin discussion of Division 11

9:31 Group reads comments

9:48 Enter final comments

9:50 Break

1:39 Begin discussion of Division 1

1:55 Group reads comments

2:00 Enter final comments

2:30 Begin discussion of Division 2

2:59 Group reads comments

3:11 Enter final comments

3:14 Break

Friday, January 9, 1988

How to accomplish the 1988 objectives (Continued)
8:32 CEO Agenda presentation
8:36 Issue Consolidation (part of IA)
9:25 First Vote – Benefits
9:35 Break
9:54 Discussion of voting results
10:05 Second Vote – Time order
10:17 Discussion of voting results
10:24 Third Vote – Feasibility
10:34 Discussion of voting results
10:39 Break
10:53 Questionnaire – participant assessment of process
10:58 Specific actions to meet top 7 issues (Topic Commenter)
11:34 Short Break
11:39 File reader to read actions
12:00 Lunch
1:05 Plan for Afternoon – CEO
1:15 Break into 4 groups to discuss assigned topics and prepare presentation to large group

Lotus support for one group
Otherwise no computer support
2:17 Groups begin entering action plans into system,
3:00 File reader of plans

CEO discusses plans - using front and local screens  
3:15 Gross Margin-1 team  
3:52 Gross Margin-2 team  
4:04 Spending Control team  
4:22 Overview team  
4:37 Session End

## Appendix B: Burr-Brown Planning Session

Results of Participant Post-Session Assessment

Questions 2 through 14 asked the participants to rate their agreement with a series of statements. Below are the statements and the number of responses in each category. Although 31 people took part in the three day planning session, only 26 were present at the time that the participant survey was presented to them for completion.

<table><tr><td colspan="5">Strongly Disagree ←</td><td rowspan="2">Strongly → Agree</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td colspan="6">2. The computer-aided process is better than the manual process.</td></tr><tr><td>0</td><td>0</td><td>4</td><td>7</td><td>15</td><td></td></tr><tr><td colspan="6">3. The computer-aided process helps the group generate ideas.</td></tr><tr><td>1</td><td>0</td><td>1</td><td>9</td><td>15</td><td></td></tr><tr><td colspan="6">4. The computer-aided process helps the group identify key ideas.</td></tr><tr><td>1</td><td>1</td><td>4</td><td>13</td><td>7</td><td></td></tr><tr><td colspan="6">5. The computer-aided process helps the group achieve its goals.</td></tr><tr><td>3</td><td>3</td><td>10</td><td>8</td><td>2</td><td></td></tr><tr><td colspan="6">6. The role of the facilitator is important to group planning.</td></tr><tr><td>0</td><td>1</td><td>5</td><td>15</td><td>5</td><td></td></tr><tr><td colspan="6">7. I felt personally responsible for the group&#x27;s decision.</td></tr><tr><td>2</td><td>6</td><td>6</td><td>11</td><td>1</td><td></td></tr><tr><td colspan="6">8. The outcome of the planning session reflects my inputs.</td></tr><tr><td>0</td><td>2</td><td>6</td><td>15</td><td>3</td><td></td></tr><tr><td colspan="6">9. I am confident that the outcome of the session is correct.</td></tr><tr><td>0</td><td>3</td><td>6</td><td>14</td><td>3</td><td></td></tr><tr><td colspan="6">10. I feel committed to the group&#x27;s decision.</td></tr><tr><td>1</td><td>2</td><td>5</td><td>13</td><td>5</td><td></td></tr><tr><td colspan="6">11. I am satisfied with the computer-aided planning process.</td></tr><tr><td>1</td><td>3</td><td>9</td><td>7</td><td>6</td><td></td></tr><tr><td colspan="6">12. The group&#x27;s problem-solving process was efficient.</td></tr><tr><td>3</td><td>6</td><td>6</td><td>9</td><td>2</td><td></td></tr><tr><td colspan="6">13. The group&#x27;s problem-solving process was fair.</td></tr><tr><td>2</td><td>2</td><td>8</td><td>10</td><td>4</td><td></td></tr><tr><td colspan="6">14. The group&#x27;s problem-solving process was satisfying.</td></tr><tr><td>5</td><td>3</td><td>2</td><td>8</td><td>8</td><td></td></tr></table>

## References

[1] R.L. Ackoff, Creating the Corporate Future, New York, John Wiley and Sons, 1981.

[2] R.F. Bales, and E.F. Borgatta, "Size of Group as a Factor in the Interaction Profile" in Hare, A.P., Borgatta, E.F. and Bales, R.F. (eds), Small Groups: Studies in Social Interaction, New York, Knopf, 1965, pp. 495–512.

[3] I. Benbasat, "An Analysis of Research Methodologies",

The Information Systems Research Challenge, F.W. McFarlan (Editor), Cambridge: Harvard Business School Press, 1984.

[4] I. Benbasat, D.K. Goldstein, and M. Mead, “The Case Research Strategy in Studies of Information Systems”, MIS Quarterly, 11,3, September 1987, pp. 369–386.

[5] X.T. Bui, and M. Jarke, “A DSS for Cooperative Multiple Criteria Group Decision Making”, Proceedings, 5th ICIS, 1984, pp. 101–113.

[6] G.B. Davis, and M.H. Olson, Management Information Systems Conceptual Foundations, Structure, and Development, second edition, McGraw-Hill, 1985.

[7] R. Davis, “Expert Systems: Where Are We and Where Do We Go From Here”, A.I. Memo No. 665, Massachusetts Institute of Technology, June 1982.

[8] A.L. Delbecq, and A.H. Van de Ven, “A Group Process Model for Problem Identification and Program Planning”, The Journal of Applied Behavioral Science, 7:4, 1971, pp. 446–492.

[9] A.R. Dennis, J.F. George, J.F. Nunamaker Jr. and D.R. Vogel "Automated Support for Group Work", in Morell, J.A. and Fleischer, M. (eds.) Advances in the Implementation and Impact of Computer Systems, forthcoming, 1988.

[10] A.R. Dennis, J.F. George, L.M. Jessup, J.F. Nunamaker, Jr., and D.R. Vogel, “Information Technology to support Electronic Meetings”, MIS Quarterly, Vol 12(4), 1988, pp. 591–628.

[11] G. DeSanctis, and G.W. Dickson, “GDSS Software: A Shell System in Support of a Program of Research”, Proceedings of HICCS Conference, 1987.

[12] G. DeSanctis, and R.B. Gallupe, “Group Decision Support Systems: A New Frontier”, Data Base, 16:2, Winter 1985, pp.3–9.

[13] G. DeSanctis, and R.B. Gallupe, “A Foundation for the Study of Group Decision Support Systems”, Management Science, 33:5, May 1987, pp.589–609.

[14] G.L. DeSanctis, and M.S. Poole, “Group Decision Making and Group Decision Support Systems: A Three Year Plan for the GDSS Research Project”, MIS Research Center Working Paper WP-88-02, University of Minnesota, September 1987.

[15] R.B. Gallupe, G. DeSanctis, and G.W. Dickson, “Computer-Based Support for Problem Finding: An Experimental Investigation”, MIS Quarterly, 12:2, June 1988, pp. 277–296.

[16] G. Goldhaber, Organizational Communication, Debuque Iowa: William C. Brown, 1974.

[17] J.R. Hackman, and N. Vidmar, “Effects of Size and Task Type on Group Performance and Member Reactions”, Sociometry, 1970, 33:1, pp. 37–54.

[18] A.P. Hare, "Group Size", American Behavioral Scientist, 24:5, 1981, pp. 695–708.

[19] A.R. Heminger, “Assessment of a Group Decision Support system in a Field Setting”, unpublished doctoral dissertation, the University of Arizona, 1988.

[20] R.Y. Hirokawa, and R.A. Pace, “A Descriptive Investigation of the Possible Communication Based Reasons for Effective and Ineffective Group Decision Making”, Communication Monographs, 50, 1983, pp. 363–379.

[21] G.P. Huber, “Group Decision Support Systems as Aids in the Use of Structured Group Management Techniques”, DSS-82, pp. 96–108.

[22] G.P. Huber, “Issues in the Design of Group Decision Support Systems”, MIS Quarterly, Sept 1984, pp..195–204.

[23] G.P. Huber, and R.R. McDaniel, “The Decision Making Paradigm of Organizational Design”, Management Science, 32:5, May 1986, pp. 572–589.

[24] B. Ives, and M. Olson, “Manager or Technician? The Nature of the Information Systems Manager’s Job”, MIS Quarterly, 5:4, December 1981, pp. 49–62.

[25] P. Karon, “PCs Enter the Conference Room”, PC Week, November 17, 1987, pp. 51, 60.

[26] P.W. Keen, and M. Scott Morton, Decision Support Systems: An Organization Perspective, Reading, Ma, Addison-Wesley, 1978.

[27] S. Kiesler, J. Siegal, and T.W. McGuire, “Social Psychological Aspects of Computer Mediated Communication”, American Psychologist, October 1984, pp. 1123–1134.

[28] K.L. Kraemer, and J.L. King, “Computer-Based Systems for Cooperative Work” Computing Surveys, Vol 20(2), 1988 pp. 115–146.

[29] D.J. Kull, "Group Decision: Can Computers Help?", Computer Decisions, May 1982, pp. 70+.

[30] F.L. Lewis, “Facilitator: A Micro Computer Decision Support Systems for Small Groups”, Unpublished Doctoral Dissertation, University of Louisville, 1982.

[31] T.M. Mills, “Power Relationships in Three Person Groups”, American Sociological Review, 18, 1953, pp.351–357.

[32] T.M. Mills, “Developmental Processes in Three Person Groups”, Human Relations, 9, 1956, pp. 343–354.

[33] H. Mintzberg, The Nature of Managerial Work, Harper and Row, New York, 1973.

[34] R.K. Mosvick, “Communication Practices of Managers and Technical Professionals in Four Large-Scale High Technology Industries”, Presented at the National Convention of the Speech Communication Association, 1982.

[35] R.K. Mosvick, “Communication Practices of Managers and Technical Professionals in High Technology Industries: An Update”, Macalester College, St. Paul, Minnesota, Manuscript.

[36] R.K. Mosvick, and R.B. Nelson, We've Got to Start Meeting Like This, Scott Foresman and Co., New York, 1987.

[37] J.F. Nunamaker Jr., L.M. Applegate and B.R. Konsynski, "Computer-Aided Deliberation Model Management and Group Decision Support", Operations Research, 1988, p. 826–848.

[38] J.F. Nunamaker Jr., L.M. Applegate, and B.R. Konsynski, "Facilitating Group Creativity with GDSS", Journal of Management Information Systems, 3:4, Spring 1987, pp. 5–19.

[39] J.F. Nunamaker, Jr., D.R. Vogel, A.R. Heminger, B. Martz, R. Grohowski and C. McGoff, "Experience at IBM with Group Support Systems", Decision Support Systems 5:2, 1989, pp. 183–196.

[40] R.R. Panko, “Office Work”, Off. Technol. People, Vol. 2, 1964, pp. 205–238.

[41] M.S. Poole, “Decision Development in Small Groups: A Study of Multiple Sequences in Decision Making”, Communication Monographs, 50:3, 1983, pp. 206–232.

[42] M.S. Poole, “Decision Development in Small Groups, III:

A Multiple Sequence Model of Group Decision Making", Communication Monographs, 50:4, 1983, pp. 321–341.

[43] M.S. Poole, D.R. Siebold, and R.D. McPhee, “Group Decision-Making as a Structural Process”, Quarterly Journal of Speech, 71, 1985, pp. 74–102.

[44] P.L. Rice, “Making Meetings Count”, Business Horizons, December 1973.

[45] R.E. Rice, The New Media: Communication Research and Technology, Beverly Hills, Sage Publications, 1984.

[46] L.S. Richman, “Software Catches the Team Spirit”, Fortune, June 8, 1987.

[47] M. Shaw, Group Dynamics: The Psychology of Small Group Behavior, third edition, New York, McGraw Hill, 1981.

[48] J. Siegel, V. Dubrovsky, S. Kiesler, and T. McGuire, "Group Processes in Computer Mediated Communication", Organizational Behavior and Human Decision Process, Vol. 37, 1986, pp. 157–187.

[49] H.A. Simon, The New Science of Management Decision, New York, Harper, 1960.

[50] P.E. Slater, “Contrasting Correlates of Group Size”, Sociometry, 1958, 21, pp. 129–139.

[51] R. Steeb, and S.C. Johnston, "A Computer-Based Interactive System for Group Decision Making", IEEE Transactions on Systems, Man, and Cybernetics, Vol. SMC-11, #8, August 1981, pp. 544–552.

[52] M. Stefik, G. Foster, D.G. Bobrow, K. Khan, S. Lanning, and L. Suchman, “Beyond the Chalkboard: Computer Support for Collaboration and Problem Solving in Meetings”, Communications of the ACM, 30:1, January 1987, pp. 33–47.

[53] S.L. Tubbs, A Systems Approach to Small Group Interaction, Reading MA.: Addison Wesley 1984.

[54] M. Turoff, and S.R. Hiltz, "Computer Support for Group Versus Individual Decisions", IEEE Transactions on Communications, 30:1, January 1982, pp. 82-91.

[55] A.H. Van de Ven, An Applied Experimental Text of Alternative Decision Making Process, Kent Ohio: Center for Business and Economic Research Press (Kent State University).

[56] J.N. Warfield, “Organizational Systems Learning”, General Systems, 27, 1982, pp 5–74.

[57] D.R. Vogel, “The Impact of “Messy” Data on Group Decision Making”, Proceedings of HICSS, 1988.

[58] D.R. Vogel, B. Martz, and J.F. Nunamaker Jr., "Automated Support for Groups: Implications for the Management of Information Systems", University of Arizona Working Paper, 1987.

[59] D.R. Vogel, J.F. Nunamaker Jr., L.M. Applegate, and B.R. Konsynski, "Group Decision Support Systems: Determinants of Success", DSS-87, pp. 118–128.

[60] R. Watson, G. DeSanctis, and M.S. Poole, “Using a GDSS to Facilitate Group Consensus: Some Intended and Unintended Consequences”, Proceeding of 8th ICIS, 1987, pp. 339–402.

[61] R.K. Yin, Case Study Research: Design and Methods, revised edition, Sage: Newbury Park, CA, 1989.

[62] I. Zigurs, “A Study of Influence in Computer Mediated Communication”, MIS Quarterly, Vol 12(4) 1988, pp 625–644.
