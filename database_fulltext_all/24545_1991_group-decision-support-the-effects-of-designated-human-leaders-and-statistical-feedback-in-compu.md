---
otero_id: 24545
otero_key: "H473NXR4"
title: "Group Decision Support: The Effects of Designated Human Leaders and Statistical Feedback in Computerized Conferences"
authors: "Starr Roxanne Hiltz; Kenneth Johnson; Murray Turoff"
year: "1991"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1991.11517922"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Group Decision Support: The Effects of Designated Human Leaders and Statistical Feedback in Computerized Conferences

Starr Roxanne Hiltz, Kenneth Johnson & Murray Turoff

To cite this article: Starr Roxanne Hiltz, Kenneth Johnson & Murray Turoff (1991) Group Decision Support: The Effects of Designated Human Leaders and Statistical Feedback in Computerized Conferences, Journal of Management Information Systems, 8:2, 81-108, DOI: 10.1080/07421222.1991.11517922

To link to this article: http://dx.doi.org/10.1080/07421222.1991.11517922

![](/api/attachments/H473NXR4/fulltext/images/924e65a7fa5d95159f85fa195510993d3778833be5105c7674996158c54293d0.jpg)

Published online: 18 Dec 2015.

![](/api/attachments/H473NXR4/fulltext/images/6fa4837b61448f263f518856da6b4d7466963fd3f288a678cc39449b6d973da7.jpg)

Submit your article to this journal ↗

![](/api/attachments/H473NXR4/fulltext/images/949b7f465af04de041516aefa4c09894a508a2d9b16dc7e20079a9b8cf40e5f4.jpg)

View related articles ↗

![](/api/attachments/H473NXR4/fulltext/images/82eed9a6173c603c04bbcef7e8f52b4df86bce2fecfa161f92a5c9d148cd0214.jpg)

Citing articles: 1 View citing articles ↗

# Group Decision Support: The Effects of Designated Human Leaders and Statistical Feedback in Computerized Conferences

STARR ROXANNE HILTZ, KENNETH JOHNSON, AND MURRAY TUROFF

STARR ROXANNE HILTZ is Professor of Computer and Information Science at the New Jersey Institute of Technology, Newark, New Jersey. She is also a member of the faculty of the Graduate School of Business, Rutgers University. She received her Ph.D. in sociology from Columbia University. For the last fifteen years, her research interests have centered on the applications and impacts of computer-mediated communication systems, including applications in education and group decision support. Her articles have appeared in Communications of the ACM, Management Science, Human Communication Research, American Journal of Sociology, and many other journals.

KENNETH JOHNSON is Professor of Psychology at Upsala College, in East Orange, New Jersey. He received his Ph.D. in psychology from the University of Arkansas. Psychological measurement and scaling are his central research interests. Among the journals in which his work has appeared are Psychnomic Science, Decision Support Systems, Management Science, and Journal of the American Society for Information Science.

MURRAY TUROFF is Professor of Computer and Information Science and School of Management at the New Jersey Institute of Technology. He received his Ph.D. in physics from Brandeis University. Previously, he was employed by the Office of Emergency Preparedness, Executive Offices of the President, and by IBM. His interests are in research and development associated with the utilization of the computer to facilitate human group communication and decision making. Among his publications are articles in Communications of the ACM, Journal of Organizational Computing, Telecommunications Policy, and IEEE Spectrum.

ABSTRACT: Twenty-four groups of five professionals and managers used computer conferences to reach agreement on the best solution to a complex ranking problem. Two software tools for structuring the conferences were employed in a two-by-two

Acknowledgments: A grant from the Division of Mathematical and Computer Sciences, NSF (MCS 78–00519), partially supported this research. Current work on group support systems is partially supported by a grant from the Division of Robotics and Intelligent Systems of the National Science Foundation. The opinions and findings are solely those of the authors and do not necessarily reflect the views of the National Science Foundation.

We are grateful to Andrew Finn, Tom Moulton, Nancy Rabke, Julian Scher, and James Whitescarver for their contributions to this project. We would also like to thank the organizations that took part in the study, and our referees for their helpful suggestions.

factorial design. Groups with “designated leadership” (DL) used software support to elect a discussion leader. Groups with “statistical feedback” (SF) were presented with tables periodically that displayed the mean rank and degree of consensus for each item. DL improved levels of consensus; in the absence of a leader, SF improved level of agreement slightly. Statistical feedback as operationalized in this experiment was detrimental to the ability of a group to achieve “collective intelligence,” defined as a group decision better than the prediscussion decision of any of its individual members. Characteristics of the individuals and groups were also associated with variations in outcomes.

KEY WORDS AND PHRASES: computer-mediated communication systems, group decision support systems.

## 1. Introduction

A GROUP DECISION SUPPORT SYSTEM (GDSS) HAS BEEN DEFINED as an interactive computer-based system that facilitates solution of problems by a group of decision makers $[10, p. 3]$ . The objective is to improve the process of group decision making by removing communication barriers, structuring or regulating the group interaction, and providing analytic tools such as decision aids for data-oriented, preference, or resource analytic tasks $[11]$ . GDSSs have also been described as “the latest advance in a long series of social technologies for groups” which include Robert’s Rules of Order, Nominal Group Technique, and the Delphi Method $[12]$ .

As several recent reviews have pointed out, there are basically two types of GDSS. Some are designed for use as an adjunct to face-to-face discussion in a “decision room,” and some are constructed to structure or support decision making in a distributed communications environment such as a computer conference $[41, 52]$ .

The majority of studies of GDSS have focused on the “decision room” environment, where groups gather at the same time and place, using computer support in combination with face-to-face discussion. Usually the room is set up with a large screen for common viewing and one or more individual terminals are used for input. For instance, Gallupe [19] experimented on groups with and without a GDSS in a decision room situation solving easy and difficult versions of a business-related task. Decision quality was found to be enhanced by the GDSS, particularly for the high-difficulty task, but confidence in the decision and satisfaction with the process were reduced. There have been well over 100 studies published of GDSS in the decision room environment [e.g., 16, 20, 21, 22, 40, 50, 63, 73, 74, 76].

Computer conferences are a form of computer-mediated communication (CMC) system designed to enable dispersed groups to communicate and work together $[26, 31, 42, 45, 55, 64]$ . They can be used synchronously (with participants dispersed in separate locations) or asynchronously (with participants reading and writing at different times, as well as from different locations).

A computerized conference, as compared to other forms of CMC, such as electronic mail, is a group discussion. Each person types comments that are catalogued by the system for all other participants to read and address.

Increasingly, it has been recognized that GDSS structures or tools can be combined with basic CMC to support decision making by groups dispersed in space and/or in time. For instance, Bui and Jarke $[3]$ and DeSanctis and Gallupe $[10]$ explicitly discuss the advantages of incorporating communications components in GDSS. In their survey of organizational uses of GDSS, Straub and Beauclair $[67]$ found that what they termed “interfaced” systems (embedded in computer conferencing or electronic mail systems) were the most prevalent, with 19 percent of their sample of Data Processing Management Association members reporting use, as compared to 10 percent for the decision room approach.

Decision support structures for CMC can be provided by software tools, by explicit statement of guidelines for interaction, and/or by a human leader or facilitator. Among the objectives of such structuring devices are message routing, message summarization, and social organization $[32, 37, 71]$ . Conferencing software usually provides structuring devices such as key words and organization of discussion items, and often includes special roles or powers for a group leader. If there are data as well as qualitative communications involved, ranging from simple yes/no votes to large tables or files of information bearing on a decision, the computer can serve as a decision support tool by analyzing, formatting, and feeding back the data to the group.

When GDSS tools and procedures are embedded in a computerized conferencing system, rather than in a decision room environment, the resulting system is a Distributed Group Support System (DGSS) [28]. Carroll [5, p. 142] points out that “While there has been some theoretical interest in the potential of computer conferencing as an effective aid to group decision making, there has been relatively little empirical investigation of the impact of this form of mediated communication.” Most published studies deal with varieties of “electronic mail”; local area networks used for transmission of discrete pieces of text, without any structuring via decision support tools or explicit guidance of the group processes by a leader [e.g., 59, 60, 62]. Clearly, there is a need for studies of the impacts of different ways of structuring computer conferences to serve as a distributed group support system.

A decade ago, we introduced the concept of “computer support for group versus individual decisions” and launched a series of three experiments to explore the process and outcome of group decision making within a computerized conferencing environment $[29, 72]$ . Selected results of the first and third experiments have appeared in the published literature $[30, 33]$ . But other than a one-page overview of some preliminary results included in the original overview article $[72]$ , the results of the second experiment were never published. There have been very few subsequent studies of distributed group support systems. Although the hardware to support such systems has improved in the interim, we believe that the results of this experiment remain relevant for the issue of the design of software tools and group processes to support distributed group decision making. For this paper, we went back to the original data for our second experiment and reanalyzed it within the framework of contemporary theoretical perspectives.

The objective of the series of experiments was to examine how variations in the structure of computerized conferences affect the process and outcome of group problem-solving discussions. Is it possible to create software that is more effective for group problem solving than free-form or unstructured conferences? How much of the variance in outcomes can be attributed to the basic characteristics of CMC as a medium of communication, the specific structures and tools provided, and the situational contingencies of group characteristics?

Versions of a computerized conferencing software environment were created that included programs for the formal selection of a designated group leader and for the statistical summarization and feedback of group members' opinions. They were chosen as examples of two special software components that may be useful for GDSS [10]. The groups were composed of employees from thirteen different organizations with the experiment conducted at their work locations. Because situational contingencies such as characteristics of the group and of its individual members can be expected to interact with the features of any particular GDSS used for any particular type of task [11, 27], the effects of these factors on outcomes are also examined.

## 1.1. The First Experiment

The prior experiment in this series compared the process and outcome of face-to-face (“FtF”) versus computerized conferences (“CC”) for two types of tasks $[29, 30]$ . One type was an intellectual task requiring rank ordering or priority setting. The problem used (“Lost in the Arctic”) has a correct or criterion solution that permits measurement of the quality of decision reached [see 15, and below]. The second task type used was cognitive conflict—a qualitative, value-laden human relations problem. The computer conferences in the first experiment were almost completely unstructured; that is, no special software tools were provided to guide or facilitate the group process. Interaction process was coded using Bales Interaction Process Analysis (IPA) $[1]$ , and in terms of equality of participation versus dominance by an emergent leader. Results bearing on this study include:

\- Outcomes: Quality of decision was equally good for the two modes, but there was greater agreement on decisions in FtF.

\- Process and Outcome: IPA distributions are related to the different outcomes for the two media. CC tends to produce relatively more of the types of communication that support high-quality decisions, and relatively less of the types that lead to group agreement.

\- Dominance: Lacking nonverbal cues or any suggested procedures for generating a leader, the CC groups did not develop any dominant participants for either task; this may have hampered their ability to organize their human resources to solve the problem.

\- Subjective Satisfaction: FtF was consistently rated as more satisfactory. The biggest difference was on satisfaction with ability to reach consensus.

\- Task: Differences between modes in interaction process and outcome are somewhat task-dependent.

The greater probability of consensus observed for the FtF groups seemed to be associated with the tendency for dominant persons—informal leaders—to emerge in the face-to-face discussions but not in the computerized conferences. We also noted that the computerized conferencing groups, lacking the ability to show their lists to one another, appeared to spend a good deal of time trying to communicate about similarities and differences in their rankings.

On the basis of these results, our speculations about appropriate software structures centered on how decision aids might improve consensus, quality of decision, and subjective satisfaction. Would it help if software were provided for generating a leader? And could the computer generate data displays that would allow the group easily to view the extent of agreement and disagreement on each of the items being discussed?

Widely used in small-group problem-solving research, the “Lost in the Arctic” problem selected for the second experiment represents the kind of “semistructured” task that is generally assumed to be most appropriate for DSS [43]. Involving the rank ordering of fifteen items, it is complex enough to benefit from computer support for statistical analysis.

## 1.2. The Functions of Leadership in Small Groups

Earlier experimental work on small groups generally supports the hypothesis that having a leader can increase effectiveness. For example, French [18] found that groups with leaders were less likely to split into subgroups or factions; Borgatta and Bales [2] found that a leader was necessary to direct activity and achieve task-oriented goals; and Maier and Solem [47] found that a discussion leader could improve the quality of decision by making sure that potentially valuable minority opinions are taken into account.

There is a continuing debate on whether and why leadership makes a difference in group and organizational performance [e.g., 49, 68]. Inconsistent findings from thousands of studies have “resulted in little accumulated knowledge that permits one to understand or predict the effects of leadership approaches or that provides a better understanding of how to be an effective leader” (Melcher [49, p. 94], as quoted by Fisher [17]). Stodgill [66] reviews conceptions of leadership as a focus of group processes, as the art of inducing compliance, as an effect of interaction, and as the initiation of structure. Palazzolo [51, p. 217] summarizes the findings about leadership by saying that “The simple differentiation of membership along leader–follower lines is sufficient and necessary to activate the group membership in the direction of effective goal- and task-directed behavior.”

In most face-to-face groups, differences in “latency of verbal response” [75] and in nonverbal communication aid in the spontaneous emergence of a leader or dominant member. The person who talks the most often gains dominance and controls turn-taking. Note that this mechanism is not operative in CC, where everyone can be typing simultaneously and differences in latency of verbal response are not relevant (although differences in typing speed may be). Nonverbal communication also includes eye-gaze and the related factor of spatial arrangement, which often help to give a group member a dominant position [35, 61, 65].

Thus, in face-to-face groups, dominant persons or “leaders” tend to emerge early in the process of interaction, if no designated leaders are provided. Most decision room GDSSs are used in conjunction with a designated group facilitator, moderator, or “chauffeur” who plays a leadership role $[13]$ . How much of the observed “impact” of the GDSS is due to the software, and how much to the process intervention of the facilitator, is generally confounded. There is widespread use of group leaders or facilitators as part of such methods for structuring face-to-face meetings as Nominal Group Technique and Focus Groups. In most studies of CMC in decision making, on the other hand, no facilitation or leadership role is explicitly provided. One of the factors examined in this experiment is the influence of a designated leader on decision making in a computerized conferencing environment.

## 1.3. Statistical Feedback

The use of numeric information through quantification and display of judgments and opinions is generally thought to lead to higher-quality and/or faster decisions $[9, 14, 36, 38]$ . Statistical feedback, especially when it is not anonymous, may initially highlight disagreement in the group. However, it is reasonable to speculate that the first step for reaching agreement is to see the nature of the disagreement clearly $[24]$ . Support for the use of statistical or summarized feedback of opinion-oriented data as a mechanism to aid decisions also comes from the Delphi Method $[7, 8, 46]$ .

## 2. Independent Variables and Hypotheses

THE TWO FACTORS CHOSEN TO VARY THE STRUCTURE of the problem-solving process within the computerized conferences were implemented as follows:

\- Designated leadership (DL) used a software program for election of a group leader before discussion, and instructions allocating specific functions to this leader.

\- Statistical feedback (SF) implemented a Delphi-like mechanism; groups periodically received tables of summarized data showing central tendencies and dispersion for the choices of the group members.

The implementation of a GDSS tool includes not only the specifics of how it works, but also the instructions to the group on how they are to use this tool in their decision-making process. Different implementations of the same “type” of tool may produce different results. Thus, details of our implementation precede the statement of hypotheses.

## 2.1. Designated Leadership

Cummings, Huber, and Arendt [6] used the “Lost on the Moon” task [23], which is very similar to the arctic task used in this study. “Leadership-neutral” groups were arranged with all members approximately equal distances apart (e.g., a circle of five), and “leader-structured” groups had one randomly selected person placed at the “head of the table" position. The quality of solutions achieved by neutrally structured groups was superior to that achieved by groups with spatially structured leaders. The authors speculate that this was because the group members did not participate in choosing the leader, citing a study by Shelley [57] that concluded that having a group leader has a positive effect on group performance only when the members of the group accept the individual as their leader. Group consensus was also greater in neutrally structured groups; this may also be related to the groups having leadership positions in the spatial arrangements randomly selected rather than legitimately chosen by the group. If leadership is to improve decision quality or consensus, then the Cummings, Huber, and Arendt [6] findings suggest that the leader must be selected or otherwise legitimized by the group.

We hypothesized that explicit software-supported procedures for generating an elected discussion leader would be helpful in CC:

H1: Designated leadership will improve amount of consensus.

H2: Designated leadership will improve quality of decision.

H3: Designated leadership will improve subjective satisfaction.

## 2.2. Statistical Feedback

The second experimental factor is the use of the computer to compile, analyze, and display information on the distribution of suggested solutions to the problem at different points in time. All groups entered their ranks on the computer and received a simple list of the members' rankings of items. In the “Statistical feedback” (SF) condition, a second table was generated. This listed the items in order of their mean ranking by all group members, indicated the ranking of each item by each group member, and reported two measures of the amount of agreement so that the group could follow its progress toward consensus. Written instructions explained that the measure of agreement for each item “reaches 100 percent if all members assign the same rank. It would be 0 percent if half ranked it at the top (#1) and half ranked it at the bottom.” The calculation of the measure of agreement on individual items is based upon the absolute value of dispersion of the ranks around the mean. The overall measure of agreement (Kendall’s coefficient of agreement) was explained as varying from 0.0 for maximum disagreement to 1.00 for 100 percent agreement on the total rank orders. It was hypothesized that SF could help to integrate the group’s communication by creating a composite picture of its collective decision at any point in time, and by focusing attention on items generating the most disagreement, thus suggesting a path to the solution of the problem. In these respects, SF has some potentials akin to that of a human leader; in fact, our earlier name for this condition was “computer leader.”

Other than the lack of anonymity, our SF condition has many of the characteristics of a real-time Delphi [70]. However, unlike most Delphi processes, we had only small groups and they were not composed of experts in the problem area. In evaluations of the Delphi method, the size of the group and their degree of expertise appear to influence the quality of the results. However, we hypothesized:

H4: Statistical feedback will improve amount of consensus in CC.

H5: Statistical feedback will improve quality of decision in CC.

H6: Statistical feedback will improve subjective satisfaction with CC.

H7: There will be interaction between designated leadership and statistical feedback.

H8: Designated leadership and statistical feedback will affect the process of communication as follows:

a) There will be less discussion with SF.

b) There will be less reranking with DL.

Because we lacked prior research in this area, we did not predict the precise nature of the interaction between the two structuring factors (H7). In regard to H8, group members had the option to communicate either by typing text comments, or by changing their rankings, which created numerical notifications and displays. To the extent that they spent relatively more time with words or with the ranking numbers (data), there was less time left for the alternative activity.

## 2.3. Systems Contingency Theory and Covariates

The “systems contingency” approach to understanding behavior within an organization assumes that each subsystem within a larger system can be analyzed as a unit of behavior in its own right, or as a subunit of behavior interacting with other subunits $[69]$ . In this experiment, the human–computer system is composed of an individual human who has certain skills and attitudes, and a CMC system with particular attributes. The human–computer system is nested within a particular group that develops patterns of structure and functioning. The social group will affect how the system is interpreted and used $[56]$ . Each group is in turn nested within a larger organizational context. Whether or not a GDSS structure will improve the process and outcome of group decision making is contingent not only upon the nature of the software tools, but also on the “fit” between these tools and the environment in which they are used: the environment includes characteristics of the individuals, the group, the task, the organization, and the communication medium.

Skills and characteristics of the individual and group composition will thus be expected to interact with the structure provided and affect the outcome. Our individual-level covariates include typing speed, previous computer experience, sex, and age, as well as prediscussion expertise related to the problem. Based on results of the previous experiment $[29]$ and of other studies of CMC systems [see 45], we predicted:

H9: Individual attributes of group members will also affect outcomes of the group decision-making process. Specifically:

H9.1: Typing speed and previous computer experience will be positively associated with the quality, agreement, and satisfaction outcomes.

H9.2: Age will be negatively related to outcomes.

H9.3: Women will tend to be more active in the discussions than men, and will tend to be more satisfied with the medium than men.

H9.4: If the group has a designated leader, his or her knowledge related to the task will be positively related to the group's quality of decision.

Another important source of variance is “group differences.” Groups from each organization were randomly assigned to condition, which is the standard procedure for experimentation with intact groups. However, groups at such organizations as Banker’s Trust, Kaiser Permanente, and Chemical Abstracts differed not only in terms of the average level of skills related to previous use of computer terminals, but also in the extent to which they were permanent working groups or just a collection of employees of the same organization who did not work together regularly. Therefore, we must also pay attention to “group” as a covariate for our analyses. Poole [53, 54] uses the term “adaptive structuration” to describe the process whereby group members appropriate and use or redefine a social technology such as GDSS, “with the result that a given structural feature may have very different effects in different groups.”

H10: There will be significant differences among groups in the use and effects of the DL and SF decision support tools.

## 3. Method

## 3.1. Subjects and Procedure

PARTICIPANTS BELONGED TO THIRTEEN DIFFERENT ORGANIZATIONS that requested a one-day “participatory seminar.” They defined themselves not as subjects in an experiment, but as managers and professionals using a “hands-on” session to learn about CMC and how it might be used to support their communication. The host organization paid expenses and selected the participants. Following an approximately half-hour-long face-to-face orientation in the morning, they spent one to one and a half hours learning and practicing with the CMC system and decision aids they would use. This practice included two ranking problems. The group then ate lunch together; this informal interaction period assured at least a minimal level of group cohesion before the problem-solving session.

It was necessary for experimental control to use the same equipment in all locations. Pretests indicated that it was important for participants to have hard copies of any lists and tables. When provided with prints, they frequently referred back to them and wrote on them in organizing their thoughts. Portable printing terminals were selected as the standard equipment, and were brought to all locations; all they required was a telephone and an electrical outlet. Although more sophisticated combinations of a high-baud-rate CRT and a printer would be preferable, it simply was not possible to transport and install such equipment in all locations.

All participants were alone in separate office spaces in the afternoon problemsolving session. After reading the arctic problem and entering their initial rankings, they had up to two hours to reach consensus. Some groups finished five to ten minutes early. When they completed postexperimental questionnaires, the group was reassembled face-to-face and debriefed.

The experiment was automated. All subjects proceeded through fifty-seven steps, administered by the computer. For instance, the first three steps were:

1. Problem and instructions were entered in the conference as a comment.

2. Initial individual rankings were solicited and checked to make sure that there were no duplications or omissions.

3. Initial rankings table(s) was (were) entered in the conference.

Methodological details about the use of EIES (the Electronic Information Exchange System) in conducting the experiment are described in a previous paper [34].

The discussion mode was a synchronous computerized conference, in which private messages were not allowed (all items were automatically entered in the group conference) and all items were automatically signed with the “real” name of the contributor (no pen name or anonymous entries were permitted). In addition to text communications in “conference comments,” a one-line “interrupt” message generated by the computer informed conferees whenever a member changed his or her rank order. A simple four-command subset of EIES was used for the experiment. It enabled the participants to enter comments, look at new comments of others, rerank the items, or display the discussion status of the participants (the last comment read by each group member, and whether they were online or disconnected).

The $2 \times 2$ factorial design used five subjects per group, with six groups per condition. Groups were randomly assigned to condition in blocks of four, so that groups in the same organization were assigned to different conditions. All groups were given two practice tasks, the first being a dessert selection problem. As their second task at the end of the practice session, groups in the DL condition were asked to rank order their members in terms of their ability to lead the group's discussion. On the basis of computer-weighted calculations from this single round of voting, the highest-ranked member was designated the leader. After their initial ranking for the arctic problem, groups in the DL condition were informed whom they had chosen as leader. The leader's instructions, printed in the conference for all to see, were to focus the discussion, suggest specific ranking changes to reach consensus, and summarize the progress. The control groups (No DL) had a comparable second practice task, rank ordering five candidates for president of the United States, but there was no reporting of the group's choices. (The experiment was conducted just prior to a presidential primary.)

The statistical feedback manipulation has been described above. A table of initial rankings was printed before the discussion began, and an updated table was delivered every ten minutes. For the SF condition, the subjects received a second statistical summary in addition to the text-only list.

## 3.2. Task and Decision Data

In the “Lost in the Arctic” ranking task [see 15], the group is asked to imagine that it has crashed in a remote subarctic region. Their task is to reach agreement on the relative importance to their survival of fifteen items that were salvaged, such as snowshoes and waterproof matches. It was explained that although the situation is fictional, the problem is an example of the kind of priority setting and planning for resource allocation in which management groups must frequently engage. The subjects were instructed to think of the problem in terms of reaching agreement on priorities and there were no complaints about the irrelevancy of the particular ranking problem chosen.

Three rank orders of items for the arctic problem were solicited by the computer. Each group member read the problem and individually gave an Initial answer, which was the basis for computations of Initial agreement and Initial quality of decision. At the end of the two-hour limit for the group discussion, or when the group reached agreement, each person was asked to report his or her perception of the Final Group decision and a Final Individual decision (what each thought was the best solution, after the group discussion). In addition, participants were free to rerank at any time during the discussion.

## 3.3. Measures of Decision Quality

## 3.3.1. Absolute Quality: Deviation Scores

The quality criterion is the solution offered by the experts, the Canadian Royal Mounted Police, who are trained and experienced in rescue in the subarctic. Following the procedure established in previous studies using this problem, correctness or quality of decision is measured by the sum of the absolute deviations of each of the items from the criterion solution. Thus, the Initial Deviation for each individual is the sum of the deviations of the prediscussion rankings from the criterion. The smaller the “deviation score,” the better the solution. The Group Deviation, calculated for individuals, is based on their report of the final “group decision” (N = 120). At the group level of analysis (N = 24), the Mean Group Deviation is the mean of the absolute deviations for the group decision reported by each of the five members.

## 3.3.2. Proportional Improvement

Groups and individuals varied in their prior knowledge. The differences among groups in the quality of the Initial prediscussion rankings are statistically significant. Although initial group differences are not significantly associated with experimental condition, it is desirable to compare relative improvement due to discussion, not just the absolute quality of the decisions. Proportional improvement is calculated as Initial (prediscussion) Deviation minus Group Deviation divided by Initial Deviation.

## 3.3.3. Collective Intelligence

Collective intelligence is defined as the ability of a group to arrive at a solution that is better than any of the members achieved individually. This is a very stringent measure of decision quality. Prior research indicates that “although the group is usually better than the average individual, it is seldom better than the best individual” [24, p. 319]. It is calculated by subtracting the Mean Group Deviation after discussion from the deviation score of the best group member before discussion (labeled “Least Deviation” in tables displaying results). The result shows how much better (or worse) the group did than its most knowledgeable member.

## 3.4. Measures of Agreement

Kendall's coefficient of agreement was calculated for each group's five rank orderings of fifteen items at four points:

—“Initial Agreement” among prediscussion rankings.

—“Discussion Agreement” reached at the end of the discussion itself, whether the ending occurred automatically because all rank orders agreed, or because time ran out. This is based on the last rankings provided by individuals before the end of the discussion.

—“Group Agreement”: after the end of discussion, the participants were asked to report their “perception” or “best estimate” of what the group decision was.

—“Final Individual Agreement,” based on postdiscussion rankings “according to what you, yourself, really think the proper rankings of the items should be.”

## 3.5. Measures of Subjective Satisfaction

Two of the items used to measure subjective satisfaction on the postexperimental questionnaire were drawn from the scales developed by the Communications Studies Group for the “Description and Classification of Meetings” [70]. These asked the participants to rate the medium of communication from “completely satisfactory” (1) to “completely unsatisfactory” (7) for a variety of functions. One is a “task-oriented” function (“giving and receiving information”) and one is a “social-emotional” function (“getting to know someone”). Two questions were semantic differential items rating satisfaction with the process and outcome of the group discussion: whether the feeling of the group was “Friendly” (1) or “Unfriendly” (7), and whether the group was “Productive” (1) or “Unproductive” (7).

## 3.6. Analysis

Each of the hypotheses was tested using correlation and analysis of variance. Except for variables that exist only at the group level, such as agreement and collective intelligence, there are 120 individual scores for each variable, but we must use a nested ANOVA design to account for group membership. Since the groups were nested under the experimental treatments, the group mean square was used as the appropriate error term for all analyses, unless the results of those analyses indicated that the group term could be combined with the within-groups mean square to provide a more stable error term [44]. In addition, covariates such as initial agreement, initial deviation, or individual attributes were used to examine further all significant $2 \times 2$ ANOVAs.

## 4. Results

AN OVERVIEW OF THE RESULTS IS PRESENTED in Table 1. The major findings are reviewed below.

## 4.1. Communication Process

The relationship between conference structure and differences in process can help to explain differences in outcomes. There were significantly fewer text comments made by participants when SF was present (H8). This was true when results were analyzed at the group level $F = 6.71, p = 0.02$ as well as when results were analyzed using the nested design for individuals. There were no differences in number of text comments made associated with the presence or absence of a DL or with the interaction between SF and DL.

Conversely, there were fewer rerankings of choices made when a DL was present (ANOVA for group level, N = 24, F for DL = 11.38, p = 0.01). Thus, when there is a designated discussion leader, participants rely relatively more on text discussion, whereas when there is no such leader, the participants rely more on the tables and are more likely to communicate changes in their judgment by changing their numerical rankings.

Discussion dominance was measured by the proportions of lines of text and comments (turns) contributed by each person. There was no relationship between condition and discussion dominance. For instance, only four groups had a dominant person when defined in terms of contributing over 33 percent of the lines in the discussion; one of these occurred in each condition. Designated leaders did tend to enter more material in the conference than others, but not so much more as to clearly dominate the discussion. This seems to be because there is no “turn-taking” in computer conferences; even though a DL is entering a comment, others may enter comments simultaneously without waiting to be recognized and without interrupting the leader. Thus, to the extent that the DL had a disproportionate influence on the group’s decision, it is because of greater influence accorded to his or her suggestions.

## 4.2. Quality of Decision

The various measures of quality of decision were highly interrelated, as would be expected. However, some of them are significantly related to condition when group

Key: L = Leader Selected; NL = No Leader; F = Statistical Feedback; NF = No Statistical Feedback.
\* Significant differences among conditions.

Table 1 Mean and Standard Deviation for Intervening and Dependent Variables, Overall and by Condition

<table><tr><td>VARIABLES</td><td>GRAND MEAN</td><td>S.D.</td><td>LF MEAN</td><td>S.D.</td><td>LNF MEAN</td><td>S.D.</td><td>NLF MEAN</td><td>S.D.</td><td>NLNF MEAN</td><td>S.D.</td></tr><tr><td></td><td colspan="10">A. By Individuals (N=120)</td></tr><tr><td>Number Comments *</td><td>18.6</td><td>7.1</td><td>16.2</td><td>5.6</td><td>20.2</td><td>6.3</td><td>16.5</td><td>7.0</td><td>21.5</td><td>8.0</td></tr><tr><td>Number Re-Rankings *</td><td>4.3</td><td>2.1</td><td>3.4</td><td>1.6</td><td>3.5</td><td>1.7</td><td>5.4</td><td>2.1</td><td>4.8</td><td>1.9</td></tr><tr><td>Initial Deviation</td><td>52.4</td><td>14.0</td><td>53.8</td><td>14.7</td><td>51.7</td><td>14.2</td><td>49.7</td><td>15.7</td><td>54.5</td><td>11.3</td></tr><tr><td>Group Deviation *</td><td>35.9</td><td>10.9</td><td>35.4</td><td>11.0</td><td>34.1</td><td>9.5</td><td>38.5</td><td>14.8</td><td>35.7</td><td>6.8</td></tr><tr><td>% Improvement *</td><td>.277</td><td>.256</td><td>.308</td><td>.246</td><td>.310</td><td>.218</td><td>.160</td><td>.357</td><td>.332</td><td>.120</td></tr><tr><td>Information Exchange *</td><td>2.81</td><td>1.37</td><td>2.43</td><td>1.01</td><td>3.20</td><td>1.71</td><td>3.00</td><td>1.39</td><td>2.60</td><td>1.19</td></tr><tr><td>Getting to Know *</td><td>4.32</td><td>1.62</td><td>4.73</td><td>1.57</td><td>4.50</td><td>1.66</td><td>4.17</td><td>1.60</td><td>3.90</td><td>.65</td></tr><tr><td>Friendly *</td><td>1.73</td><td>.93</td><td>1.73</td><td>.83</td><td>1.37</td><td>.56</td><td>2.03</td><td>1.22</td><td>1.77</td><td>.53</td></tr><tr><td>Productive</td><td>2.39</td><td>1.18</td><td>2.50</td><td>1.20</td><td>2.20</td><td>1.37</td><td>2.53</td><td>1.17</td><td>2.33</td><td>.50</td></tr><tr><td></td><td></td><td></td><td colspan="8">B. By Group (N=24)</td></tr><tr><td>Initial Agreement</td><td>.554</td><td>.113</td><td>.513</td><td>.047</td><td>.563</td><td>.184</td><td>.575</td><td>.073</td><td>.565</td><td>.119</td></tr><tr><td>Discussion Agreement *</td><td>.903</td><td>.106</td><td>.853</td><td>.096</td><td>.980</td><td>.027</td><td>.929</td><td>.074</td><td>.849</td><td>.147</td></tr><tr><td>Group Agreement</td><td>.974</td><td>.047</td><td>.953</td><td>.055</td><td>.998</td><td>.007</td><td>.986</td><td>.013</td><td>.959</td><td>.074</td></tr><tr><td>Final Individual</td><td>.858</td><td>.108</td><td>.863</td><td>.086</td><td>.879</td><td>.081</td><td>.859</td><td>.118</td><td>.823</td><td>.157</td></tr><tr><td>Least Deviation</td><td>36.9</td><td>8.2</td><td>35.7</td><td>4.6</td><td>36.7</td><td>7.7</td><td>31.3</td><td>5.9</td><td>44.0</td><td>10.0</td></tr><tr><td>Collective Intelligence*</td><td>1.0</td><td>10.6</td><td>.3</td><td>9.1</td><td>2.6</td><td>8.1</td><td>-7.2</td><td>12.7</td><td>8.3</td><td>7.5</td></tr></table>

composition variables are taken into account, and some are not significantly related at the group level of analysis.

Absolute quality. Using the nested ANOVA design, decisions were better with DL and without SF (see the “Group Deviation” row in Table 1). However, group was highly significant as a source of variation. When group-level data were used, there were no significant differences among conditions.

Proportional improvement (row 5). The quality of decision of groups in all conditions tended to improve noticeably. There are significant differences associated with SF, and the interaction between DL and SF, when the 120 individual scores are examined: the No Designated Leader, Statistical Feedback (NLF) condition improved much less than any of the others. None of the other differences is significant. However, the strongest, most significant differences are associated with group. Some groups were much better than others, regardless of condition. When the group mean scores are used, there are no significant differences among conditions (Table 2).

Collective intelligence. The last row in Table 1 shows that there are clearly significant differences among conditions when quality of decision is measured by this criterion. This relationship is examined further in Table 3, which shows whether the groups were able to incorporate and surpass the knowledge of their “best” member in making a collective decision, by condition. Overall, half of the groups exhibited “collective intelligence” by reaching a decision that was better than the initial (prediscussion) decision of any individual member, and only a third did not at least equal the performance of their best member.

Looked at purely in terms of a “yes/no” dichotomy, it appears that SF is detrimental to the emergence of “collective intelligence.” In both SF conditions, only two of the six groups produced a group decision better than that of their best member. In the NSF conditions, nine out of twelve groups exhibited “collective intelligence,” and only one out of twelve failed to do at least as well as its best member. There is one classic “outlier” group in the NDL SF condition that did much worse than any other group. However, this does not affect the simple count of whether or not groups were able to achieve collective intelligence.

Analysis of variance of the amount by which a group did better or worse than its best member indicates that the detrimental effect of SF on “collective intelligence” is significant. Various methods for adjusting for the “outlier” group did not change this conclusion. It appears that the SF tables have the effect of decreasing the influence of the more knowledgeable members, perhaps by creating pressure to reach a compromise rather than exploring the reasons underlying a “deviant” member’s opinion which may in fact be superior.

## 4.3. Factors Affecting Quality

What makes some groups much “better” than others, independent of condition? Among the group composition variables that appear to explain much of the apparent differences in quality of group performance are the quality of the leader’s own decision, if there is a leader; the quality of the “best individual’s” prediscussion score; and attributes such as age, sex, and typing ability, which are related to the process and outcome of the group’s decision-making process. The first two, in particular, are somewhat confounded with condition. The “best members” of the groups with SF tended not to be as knowledgeable as the best members of those groups without SF, before discussion.

## 4.3.1. Leader's Knowledge

Those who were relatively verbose during the practice tended to be ranked highly and selected as leaders; the correlation between the number of comments entered during the practice and DL ranking was -0.46 (p = 0.01).

Deviation from the correct decision varied greatly among leaders, from a low of 30 to a high of 76. There was absolutely no correlation (Pearson's R of 0.01) between the quality of the leader's initial prediscussion solution to the problem and the likelihood of having been selected as a leader. Looking at the group-level data, there is a high correlation between the quality of the leader's prediscussion decision, and the absolute quality of the group decision reached (Pearson's R = 0.71, p = 0.001). In terms of proportional improvement, the correlation is 0.44 (p = 0.001). Thus, for the DL condition, much of the variance in the quality of the group decision is explained by whether or not they happened to choose a leader who was knowledgeable about the problem.

Table 2 Proportional Improvement in Deviation from Criterion, by Condition (Individual Deviation – Group Deviation/Individual Deviation)

<table><tr><td>Condition</td><td>Statistical Feedback</td><td>No Feedback</td><td>All</td></tr><tr><td>Designated Leader</td><td>30.8</td><td>31.0</td><td>30.9</td></tr><tr><td>No Designated Leader</td><td>16.0</td><td>31.0</td><td>24.6</td></tr><tr><td>All</td><td>23.4</td><td>32.1</td><td>27.7</td></tr><tr><td colspan="4">ANOVA, Nested Design (N = 120): Leadership F = 2.89, p = 0.09; Feedback F = 5.57, p = 0.02; Leadership × Feedback F = 5.32, p = 0.02; Group F = 4.09, p = 0.001. ANOVA, Group Level (N = 24): Leadership F = 0.71, NS; Feedback F = 1.36, NS; Leadership × Feedback F = 1.30, NS.</td></tr></table>

Table 3 Mean “Collective Intelligence,” by Condition

<table><tr><td rowspan="2"></td><td colspan="3">ANALYSIS OF VARIANCE</td></tr><tr><td>SF</td><td>No SF</td><td>All</td></tr><tr><td>Designated Leader</td><td>.27</td><td>2.60</td><td>1.43</td></tr><tr><td>No DL</td><td>-7.20</td><td>8.33</td><td>.57</td></tr><tr><td>All</td><td>-3.47</td><td>5.47</td><td>1.00</td></tr></table>

Leadership, $F = 0.05$ , NS; Feedback, $F = 5.22$ , $p = 0.03$ ; DL $\times$ SF, $F = 2.85$ , $p = 0.11$ .

## 4.3.2. Influence of the Best Member

Initial deviation scores for the group member with the best prediscussion solution (“Least Deviation”) ranged from 24 to 44. Having a knowledgeable member was significantly related to the absolute quality of the final group decision, as would be expected (R = 0.44, p = 0.001).

However, unlike the leader's initial opinion, there is no correlation between Least Deviation and proportional improvement.

If “Least Deviation” is used as a covariate, with either absolute quality of decision or proportional improvement as the dependent variable, there are no significant differences among groups associated with condition. However, those groups in the SF conditions still appear to have noticeably smaller, though not statistically significant $p=0.20$ , proportional improvements. Thus, there is the suggestion that SF is detrimental to reaching high-quality decisions, but this effect is dependent upon how quality of decision is measured and what other variables are taken into account. It appears that SF does not provide as high a probability as NSF that the “best” member will have a disproportionate influence on the group decision.

## 4.4. Reaching Agreement

There are no significant differences among conditions in the initial levels of agreement before discussion (Table 1). The average Kendall's coefficient of 0.45 before discussion shows that the groups did have considerable “work” to do in order to reach agreement.

## 4.4.1. Group Agreement

High levels were reached in all conditions, as indicated by the mean of 0.97 shown in Table 1. Only three of the twenty-four groups did not reach at least 94 percent agreement (Kendall's of 0.950 or higher), and ten of the twenty-four reached 100 percent agreement. The levels of agreement in all conditions are so high that the differences that do occur are not statistically significant. However, there are some interesting qualitative differences. Either DL or SF alone was helpful in reaching very high levels of group agreement; for instance, in the DL NSF condition, five of the six groups reached 100 percent agreement. The condition with both DL and SF was the worst; none of these groups reached 100 percent agreement.

These results vary from those of our first experiment, where computerized conferencing groups did not reach such high levels of agreement on a group decision, and none was able to reach 100 percent agreement on the arctic problem. The differences may be attributable to any of five factors:

1. The groups were allowed two hours to reach agreement on the arctic problem, instead of the ninety minutes allowed in the first experiment.

2. All groups received practice ranking problems during a training period of over an hour, as compared to about a half an hour training and no practice problem in the first experiment.

3. All groups did have the text-only tables and notification of ranking changes as they were made, so that they did not have to change their ranks separately and communicate these changes to one another. In our first experiment, tables of ranks were made available only at the beginning of the discussion.

4. These were more nearly “real” groups; they were familiar with one another as members of the same organization. Thus, it can be expected that they would find it easier to work together and reach agreement than did the groups of strangers used in our first experiment.

5. The subjects had more previous computer experience than did those in our first experiment. This variable is related to ability to reach consensus.

## 4.4.2. Final Individual Agreement

Final Individual Agreement was also not significantly related to condition. It was lowest, on the average, for groups with neither DL nor SF, but only by about five points on the Kendall scale.

## 4.4.3. Discussion Agreement

In the analysis of variance for the last rankings by the subjects during the discussion, we do obtain some statistically significant differences (Table 1). This significant difference in Discussion Agreement is examined further in Table 4. Either DL alone, or SF alone, aids consensus. In combination, however, they cancel each other out and are no better than a structure without either aid.

## 4.4.4. Variables Related to Agreement

As would be expected, there was some relationship between degree of initial agreement and degree of agreement on the final group decision $R = 0.46, p = 0.03$ . However, using Initial Kendall's as a covariate did not change any of the relationships examined.

Those groups with the highest levels of agreement had a slight tendency to reach better decisions, but the correlation between the Final Kendall's coefficient for group decision and final deviation (from criterion) scores is only $-0.07$ , and not statistically significant (see the appendix). On the other hand, the correlation between Final Individual Agreement and quality of the final individual rankings is much stronger ( $R = 0.46$ , $p = 0.01$ ). The difference in these two relationships suggests that “real” agreement is positively related to good decisions, but that compromise in “real” opinions in order to reach group consensus also compromises quality.

## 4.5. Subjective Satisfaction

Generally, conditions did not vary significantly in terms of the subjective satisfaction of participants (Table 1), and the relationships that do occur do not form a clear pattern. For the function “giving and receiving information,” there is an interaction between DL and SF. The DL SF condition received the highest rating (mean = 2.4), while DL NSF received the poorest (mean = 3.2).

Table 4 Discussion Agreement, by Condition (Mean Kendall's Coefficient of Agreement)

<table><tr><td rowspan="2"></td><td colspan="3">ANALYSIS OF VARIANCE</td></tr><tr><td>SF</td><td>No SF</td><td>All</td></tr><tr><td>DL</td><td>.853</td><td>.980</td><td>.917</td></tr><tr><td>No DL</td><td>.929</td><td>.849</td><td>.889</td></tr><tr><td>All</td><td>.891</td><td>.914</td><td>.903</td></tr></table>

Leadership, F = 0.35, NS; Feedback, F = 0.50, NS; DL × SF, F = 6.92, p = 0.02.  
The feeling of the group was perceived as more friendly when there was a designated leader and when there was no statistical feedback. On the other hand, for “getting to know someone,” the NDL conditions were rated significantly more highly than the DL conditions.

## 4.6. Individual Attributes

Older participants tended to have initial solutions of poorer quality, to improve less, and to be less satisfied with the medium in any form (see the appendix). Ability to reach agreement was also negatively correlated with average age of the group (e.g., -0.42 for final individual consensus, p = 0.04).

There was a strong correlation between both typing ability $(R = 0.42, p = 0.01)$ and previous experience with computers $(R = 0.62, p = 0.01)$ , and the ability of the group to reach consensus. Those with more computer-related skills also tended to be more satisfied with the medium.

Women entered more comments than men, and tended to improve their decision more, from an initially poorer start. They also tended to be more satisfied with the medium of communication, particularly for “getting to know someone.”

## 5. Summary and Conclusion

FOR ALL CONDITIONS IN THIS STUDY, synchronous computer conferences were structured with a decision support tool to support an intellective task that required the group to reach agreement about the relative importance (rank order) of a number of alternatives. Participants could easily rank order the items at any time by using a special command. Other participants were informed whenever any group member changed his or her rank ordering, and every ten minutes, a summary table of the raw data was printed showing the current rank orders of group members. The proportional improvement of the average “group” decision compared to the average for the five members before discussion was 28 percent, and groups reached high levels of agreement in all conditions.

The presence or absence of two types of group support was varied. Groups with designated leaders (DL) used the rank-ordering tool to select a discussion leader before receiving their task. Groups with statistical feedback (SF) were provided a second table that showed mean rankings for each item and measures of agreement. Focusing on the “strong” quality criterion of “collective intelligence” (a group decision that is better than the decision made by the most knowledgeable member acting individually), there are statistically significant differences among conditions. Those groups with SF were less likely to attain collective intelligence. Our analyses suggest that the SF condition, particularly in the absence of a DL, encourages participants to change their decisions in order to conform more closely to the group average, and lessens the influence of the most knowledgeable member.

The results of tests of the hypotheses about expected differences in outcomes were as follows:

H1: Designated leadership did tend to improve quality of decision, but the differences were statistically significant at the group level of analysis only for the “collective intelligence” measure.

H2: DL tended to improve level of agreement, but the differences were not significant.

H3: DL did not improve subjective satisfaction.

H4: Statistical feedback tended to be detrimental to quality of decision, rather than improving it. The difference was statistically significant for the “collective intelligence” measure.

H5: SF did not significantly improve group agreement.

H6: SF did not affect subjective satisfaction.

H7: There was a statistically significant interaction between the DL and the SF conditions. When both were present, agreement was worse than when only one was present. SF without DL tended to decrease quality of decision.

H8: SF was associated with fewer text comments and more rerankings of items by participants.

H9: Individual attributes such as the leader's knowledgeability about the problem, typing speed, previous computer experience, sex, and age were associated with differences in quality of decision, ability to reach agreement, and subjective satisfaction.

H10: There were significant differences among groups in the effects of the DL and SF structures.

Some group leaders were knowledgeable and others were not. Groups also varied markedly in the extent to which they started out with one or more knowledgeable members, and to which they were composed of members with characteristics related to greater improvement in quality of decision. For instance, groups with more women did better. The situational contingency of group composition was a strong determinant of decision outcomes. This is one reason why some of the results are significant at the individual level, but not at the group level. A second reason is the difference in sample size (120 individuals versus 24 groups). With hindsight, we should have used more than 120 subjects and 24 groups, in order to have a better chance for software differences to overcome variations among groups.

The fact that this was a field experiment, carried out with groups of managers and professionals within actual organizations, is perhaps both its greatest strength and its greatest weakness. Because we used groups of employees in existing organizations, who participated in their office settings rather than coming to a laboratory as “subjects,” we may feel more confident about generalizing our findings, but we had less control over the experiment. The groups are not similar, and constitute a stronger source of variance than our experimental manipulations of conference structure. If we had used random assignment to experimentally constitute groups in a laboratory setting, we might have found more statistically significant differences.

Taking into account the various measures of quality of decision and covariates examined, the primary determinants of the quality of the group decision include the quality of the best member's prediscussion solution; the quality of the leader's solution, if there is a leader; and attributes such as sex and age. These findings reinforce the necessity of using a “contingency” model in predicting the effects of any particular GDDS, as also advocated by DeSanctis and Gallupe [11]. However, there is also a fairly consistent tendency for the presence of statistical feedback to be detrimental to a high-quality group decision. The feedback tables appear to decrease the influence of the “best” member, by creating pressure to compromise.

The statistical feedback table, as implemented in this experiment, seems to have led to “groupthink” [39], a process in which a strong concurrence-seeking tendency suppresses critical inquiry and the group reaches agreement before critically evaluating all points of view. A more recent experiment [4] using a task similar to the one we used (“Lost at Sea”) supports the hypothesis that high-quality decisions result from a process of vigorous critical discussion, with high levels of expression of disagreement as well as agreement.

We would not use the same version of feedback again under the same circumstances: small groups, not composed of experts on the topic of the decision. At the very least, we would like to combine the feedback with a process intervention designed to discourage premature compromise on the group's average decision. On the other hand, feedback of organized raw data does seem to be a positive influence on consensus that is not detrimental to quality.

The nature of interaction between the two aids was entirely unexpected. Although we had not formally predicted this, we had thought, “the more, the better”: having both aids would produce a disproportionate increase in ability to reach agreement. On the contrary, as implemented in this experiment, the existence of a designated leader and the provision of statistical feedback appeared to conflict with each other. We observed groups in which members pointed out that a course of action suggested by the leader contradicted the implications of the summarized data. The SF table may have functioned as a surrogate leader in terms of suggesting a solution. Perhaps the human leader should have been specially instructed in how to use the SF data to guide suggested courses of action. We suspect that the process we observed in some of our experimental groups, whereby the human leader ignored or misunderstood the computer displays and thereby generated arguments in the group, may also occur in the “real world” of DSS and MIS, and is worthy of further investigation.

In addition to the confounding of individual attributes with experimental condition, three other limitations of this experiment should be noted: the specific task, the “old-fashioned” equipment, and the use of a single synchronous computer conferencing session. It has been previously observed that the effects of computerized conferences on the process and outcome of group decision making are somewhat task-dependent $[19, 30]$ . There is a need for further studies of GDSS/conferencing technologies with other specific “intellective” tasks $[48]$ and with other task types in the future.

The participants used a line-oriented CMC system on printing terminals. However, current pilot studies on a state-of-the-art system (a full-screen EIES 2 at 9600 baud) indicate that participants behave much the same way as they did with the older equipment [28]. The main limitations on the speed and ease of information exchange are human typing and reading speed and the lack of nonverbal cues, not the speed of transmission provided by the equipment.

This experiment was conducted with synchronous conferencing within a very limited time period. There is a need for experiments that more closely match the “natural” mode of CC, where asynchronous participation is spread out over time.

For this study, with group size of only five, designated leadership was more effective than statistical feedback. For very large groups (twenty or more), some form of statistical feedback (analysis and display of data related to the group decision) might prove more valuable than it did in this experiment. In a follow-on experiment, we plan to vary group size and test this speculation about the interaction of group size and statistical feedback.

The results also confirm the point of view that good decision support structures should ensure the exploration of disagreements, and quantification or statistical feedback on “average” opinions should not be allowed to prevent this desirable process. In addition, the design of GDSS, whether synchronous or asynchronous, has to be based on a clear understanding of what is needed to support human facilitation or leadership roles. Therefore, there is a need for further research that examines the effect of different ways of structuring the leadership function, which is not confounded with software aids for other aspects of decision support.

We also conclude that some groups are simply much better candidates than others for using computerized conferences for discussion and decision making. Groups composed of participants with some previous experience using computers and groups with cooperative rather than competitive social histories are recommended. On the basis of the superior performance of the subjects in this experiment as compared to those in the first experiment, we would also stress the apparent importance of adequately training participants and giving them a chance to practice with this medium before asking them to use it to solve a difficult problem, and of allowing adequate time to complete the task, which is likely to be a longer elapsed “clock time” than would be necessary for a face-to-face meeting.

Finally, we strongly concur with the assertion by DeSanctis and Gallupe [11] that iterative programs of research on GDSS are essential if we are to succeed in making available computer-based tools that will improve the outcomes of group decision making. The efficacy of specific tools and procedures must be examined not only alone, but in combination. Because outcomes are dependent upon the interaction of the specific tools with contextual contingencies of characteristics of the task, the communication medium, and the group, it is essential that experiments build upon one another, if a cumulative and useful body of knowledge about group decision support systems is to emerge.

## REFERENCES

1. Bales, R.F. Interaction Process Analysis: A Method for the Study of Small Groups. Reading, MA: Addison-Wesley, 1950.

2. Borgatta, E.F., and Bales, R.F. Some findings relevant to the great man theory of leadership. American Sociological Review, 19 (1954), 755–759.

3. Bui, Tung, and Jarke, M. Communications requirements for group decision support systems. Journal of Management Information Systems, 2, 4 (Spring 1986), 8–20.

4. Callaway, M.R.; Marriot, R.G.; and Esser, J.K. Effects of dominance on group decision making: toward a stress-reduction explanation of groupthink. Journal of Personality and Social Psychology, 49, 4 (1985), 949–952.

5. Carroll, B. The effectiveness of structured decision support in computer conferences. Proceedings, Third Guelph Symposium on Computer-Mediated Communication, Guelph, Canada, May 15–17, 1990, 142–153.

6. Cummings, L.L.; Huber, G.P.; and Arendt, E. Effects of size and spacial arrangements on group decision making. Academy of Management Journal, 17, 4 (1974), 460–475.

7. Dalkey, N.C. The Delphi Method: An Experimental Study of Group Opinion. Santa Monica, CA: Rand Corp. (RM-5888-PR), 1969.

8. Dalkey, N.C.; Brown, B.; and Cochran, S. The Delphi Method, IV: Effect of Percentile Feedback and Feed-in of Relevant Facts. Santa Monica, CA: Rand Corp., (RM-6118-PR), 1970.

9. Delbecq, A.L.; Van de Ven, A.H.; and Gustafson, D.H. Group Techniques for Program Planning: A Guide to Nominal Group and Delphi Processes. Glenview, IL: Scott-Foresman, 1975.

10. DeSanctis, Gerardine, and Gallupe, B. Group decision support systems: a new frontier. Data Base, Special Interest Group on Business Data Processing of the Association for Computing Machinery, 16, 2 (Winter 1985), 3–10.

11. DeSanctis, G., and Gallupe, B. A foundation for group decision support systems design. Management Science, 33, 5 (May 1987), 589–609.

12. DeSanctis, G.L., and Poole, M.S. Group decision making and group decision support systems. Working paper MISRC-WP-88-02, Management Information Systems Research Center, University of Minnesota, Minneapolis, 1987.

13. Dickson, G.W.; Lee, J.E.; Robinson, L.; and Heath, R. Observations on GDSS interactions: chauffeured, facilitated, and user-driven systems. In R. Banning and D. King, eds., Proceedings of the Twenty Second Annual Hawaii Conference on System Sciences, vol. 3. Washington, DC: IEEE, 1989, 337–343.

14. Dickson, G.W.; Senn, J.A.; and Chervany, N.L. Research in management information systems: the Minnesota experiments. Management Science, 23, 9 (1977), 913–923.

15. Eady, P.M., and Lafferty, J.C. The subarctic survival situation. Plymouth, MI: Experimental Learning Methods, 1969.

16. Ellis, C.A.; Rein, G.L.; and Jarvenpaa, S.L. Nick experimentation: selected results concerning effectiveness of meeting support technology. Journal of Management Information Systems, 6, 3 (Winter 1989–90), 7–24.

17. Fisher, B.A. Leadership: when does the difference make a difference? In R.Y. Hirokawa and M.S. Poole, eds., Communication and Group Decision Making. Beverly Hills, CA: Sage, 1986, 197–215.

18. French, J.R.P., Jr. The disruption and cohesion of groups. Journal of Abnormal and Social Psychology, 36 (1941), 361–377.

19. Gallupe, R.B. Experimental research into group decision support systems: practical issues and problems. Proceedings of the Nineteenth Annual Hawaii Conference on System Sciences. IEEE Computer Society, 1986, 515–523.

20. Gallupe, R.B.; DeSanctis, G.; and Dickson, G.W. The impact of computer-based support on the process and outcomes of group decision making. Proceedings of the Seventh International Conference on Information Systems, San Diego, December 1986.

21. Gallupe, R.B.; DeSanctis, G.; and Dickson, G.W. Computer-based support for group problem finding: an experimental investigation. MIS Quarterly, 12, 2 (June 1988), 277–296.

22. Gray, P., et al. The SMU decision room project. Transactions of the First International Conference on Decision Support Systems, Atlanta, 1981, 122–129.

23. Hall, J. Decisions, decisions, decisions. Psychology Today, 5, 6 (1971), 51–54, 86–88.

24. Hare, A.P. Handbook of Small Group Research, 2d ed. New York: Free Press, 1976.

25. Harvey, J. Abilene Paradox and Other Mediations in Management. Lexington, MA: Lexington Books, 1988.

26. Hiltz, S.R. Online Communities: A Case Study of the Office of the Future, Norwood, NJ: Ablex, 1984.

27. Hiltz, S.R. Productivity enhancement from computer-mediated communications: a systems contingency approach. Communications of the ACM (December 1988), 1438–1454.

28. Hiltz, S.R.; Dufner, D.; Holmes, M.; and Poole, M.S. Distributed group support systems: social dynamics and design dilemmas. Paper presented at the Conference on Organizational Information Systems and Coordination, Austin, Texas, November 1989. Journal of Organizational Computing, 1, 2 (1991), 135–159.

29. Hiltz, S.R.; Johnson, K.; Aronovitch, C.; and Turoff, M. Face to Face vs. Computerized Conferences: A Controlled Experiment. Newark, NJ: Computerized Conferencing and Communications Center, NJIT, Research Report No. 12, 1980.

30. Hiltz, S.R.; Johnson, K.; and Turoff, M. Experiments in group decision making, 1: Communications process and outcome in face-to-face vs. computerized conferences. Human Communication Research, 13, 2 (1986), 225–252.

31. Hiltz, S.R., and Turoff, M. The Network Nation: Human Communication Via Computer. Reading, MA: Addison-Wesley, 1978.

32. Hiltz, S.R., and Turoff, M. Structuring computer-mediated communication to avoid information overload. Communications of the ACM, 28, 7 (July 1985), 680–689.

33. Hiltz, S.R.; Turoff, M.; and Johnson, K. Experiments in group decision making, 3: disinhibition, deindividuation, and group process in pen name and real name computer conferences. Decision Support Systems, 5 (1989), 217–232.

34. Hiltz, S.R.; Turoff, M.; Johnson, K.; and Aronovitch, C. Using a computerized conferencing system as a laboratory tool. SIGSOC Bulletin, 13, 4 (1982), 5–9.

35. Hovells, L.T., and Becker, S.W. Seating arrangements and leadership emergence. Journal of Abnormal and Social Psychology, 64 (1962), 148–150.

36. Huber, G.P. Group decision support systems as aids in the use of structured group management techniques. DSS-82 Conference Proceedings (1982), 96–108.

37. Huber, G.P. Organizational information systems: determinants of their performance and behavior. Management Science, 28, 2 (1982), 138–153.

38. Huber, G.P. Issues in the design of group decision support systems. MIS Quarterly, 8, 3 (1984), 195–204.

39. Janis, I.L. Victims of Groupthink. Boston: Houghton Mifflin, 1972.

40. Jarvenpaa, S.L.; Rao, V.S.; and Huber, G.P. Computer support for meetings of groups working on unstructured problems: a field experiment. MIS Quarterly, 12, 4 (December 1988).

41. Johansen, R. Groupware: Computer Support for Business Teams. New York: Free Press, 1988.

42. Johansen, R.; Vallee, J.; and Spangler, K. Electronic Meetings: Technical Alternatives and Social Choices, Reading, MA: Addison-Wesley, 1979.

43. Keen, P.G.W., and Scott-Morton, M.S. Decision Support Systems: An Organizational Perspective. Reading, MA: Addison-Wesley, 1978.

44. Keppel, G. Design and Analysis: A Researcher's Handbook, 2d ed. Englewood Cliffs, NJ, Prentice-Hall, 1982.

45. Kerr, E.B., and Hiltz, S.R. Computer-Mediated Communication Systems: Status and Evaluation. New York: Academic Press, 1982.

46. Linstone, H.A., and Turoff, M. The Delphi Method: Techniques and Applications. Reading, MA: Addison-Wesley, 1975.

47. Maier N.R.F., and Solem, A.R. The contribution of a discussion leader to the quality of group thinking: the effective use of minority opinions. Human Relations, 5 (1952), 277–288.

48. McGrath, J.E. Groups: Interaction and Performance. Englewood Cliffs, NJ: Prentice-Hall, 1984.

eds., Leadership: The Cutting Edge. Carbondale, IL: Southern Illinois University Press, 1977, 94–108.

50. Nunamaker, J.F.; Applegate, L.M.; and Konsynski, B.R. Facilitating group creativity: experience with a group decision support system. Proceedings of the Twentieth Annual Hawaii Conference on System Sciences, 1 (1987), 422–430.

51. Palazzolo, C.S. Small Groups: An Introduction. New York: D. Van Nostrand Co., 1981.

52. Pinsonneault, A., and Kramer, K.L. The impact of technological support on groups: an assessment of the empirical research. Decision Support Systems, 5 (1989), 197–216.

53. Poole, M.S. Structural paradigms and the study of group communications. In M. Mander, ed., Communications in Transition: Issues and Debates in Communication Research. New York: Praeger, 1983, 186–205.

54. Poole, M.S.; Siebold, D.R.; and McPhee, R.D. A structural theory of group decision-making. Quarterly Journal of Speech, 71 (1987), 74–102.

56. Robertson, D.D. Social determinants of information systems use. Journal of Management Information Systems, 5, 4 (1989), 55–71.

57. Shelley, H.P. Status, consensus, leadership, and satisfaction with the group. Journal of Social Psychology, 51 (1960), 157–164.

58. Short, J.; Williams, E.; and Christie, B. The Social Psychology of Telecommunications. London: Wiley, 1976.

59. Siegel, J.; Dubrovsky, V.; Kiesler, S.; and McGuire, T.W. Group processes in computer-mediated communication. Organizational Behavior and Human Decision Processes, 37 (1986), 157–187.

60. Smith, J., and Vanacek, M.T. A nonsimultaneous computer conference as a component of group decision support systems. Proceedings, Hawaii International Conference on System Sciences, vol. 3 (1989), 370–377.

61. Sommer, R. Personal Space: The Behavioral Basis of Design. Englewood Cliffs, NJ: Prentice-Hall, 1969.

62. Sproull, L., and Kiesler, S. Reducing social context cues: electronic mail in organizational communication. Management Science, 32, 11 (1986), 1492–1512.

63. Steeb, R., and Johnston, S.C. A computer-based interactive system for group decision making. IEEE Transactions on Systems, Man, and Cybernetics, SMC-11, 8 (August 1981), 544–552.

64. Steinfield, C.W. Computer-mediated communication systems. In M. Williams, ed., Annual Review of Information Sciences and Technology, vol. 21. White Plains, NY: Knowledge Industry Publications, 1986, 167–202.

65. Steinzor, B. The spacial factor in face-to-face groups. Journal of Abnormal and Social Psychology, 45 (1950), 552–555.

66. Stogdill, R.M. Handbook of Leadership. New York: Free Press, 1974.

67. Straub, D.W., Jr., and Beauclair, R.A. Current and future users of group decision support systems. Journal of Management Information Systems, 5, 1 (Summer 1988), 101–116.

68. Thomas, A.B. Does leadership make a difference to organizational performance? Administrative Science Quarterly, 33 (1988), 388–400.

69. Tosi, H.L., and Clay, H.W. Organizational Behavior and Management: A Contingency Approach. Chicago: St. Clair Press, 1974.

70. Turoff, M. Computerized conferencing and real time delphis: unique communication forms. Proceedings, 2nd International Conference on Computer Communications. IEEE Computer Society, 1974, 135–142.

71. Turoff, M. Computer-mediated communications requirements for group support. Journal of Organizational Computing, 1, 1 (1991).

72. Turoff, M., and Hiltz, S.R. Computer support for group vs. individual decisions. IEEE Transactions on Communications, COM-30, 1 (January 1982), 82–40.

73. Vogel, D.R.; Nunamaker, J.F.; Martz, W.B.; Grohowski, R.; and McGoff, C. Electronic meeting system experience at IBM. Journal of Management Information Systems, 6, 3 (Winter 1989–90), 25–43.

74. Watson, R.; DeSanctis, G.; and Poole, M.S. Using a GDSS to facilitate group consensus: some intended and unintended consequences. MIS Quarterly, 12, 3 (September 1988), 463–478.

75. Willard, D., and Strodtbeck, F.R. Latency of verbal response and participation in small groups. Sociometry, 35, 1 (1972), 161–175.

76. Zigurs, I.; Poole, M.S.; and DeSanctis, G.L. A study of influence in computer-mediated group decision making. MIS Quarterly, 12, 4 (December 1988), 233–241.

Appendix 1 Correlation Matrix of the Variables (N = 120 Individuals)

<table><tr><td>1.</td><td>Designated Leader</td><td>1</td><td>0</td><td>-.02</td><td>.11</td><td>.16</td><td>-.04</td><td>-.07</td><td> $-.39^*$ </td><td>.03</td><td>-.11</td><td>-.11</td><td>.12</td><td>.01</td><td> $.18^*$ </td><td> $-.19^*$ </td><td>-.04</td></tr><tr><td>2.</td><td>Statistical Feedback</td><td></td><td>1</td><td>.13</td><td> $-.21^*$ </td><td>-.13</td><td>-.13</td><td> $-.32^*$ </td><td>.06</td><td>-.05</td><td>.10</td><td>0</td><td>-.17</td><td>-.07</td><td>.08</td><td>.17</td><td>.11</td></tr><tr><td>3.</td><td>Age</td><td></td><td></td><td>1</td><td> $-.18^*$ </td><td> $-.19^*$ </td><td>-.16</td><td>-.15</td><td>-.08</td><td>-.16</td><td>.03</td><td>.09</td><td>-.15</td><td>.01</td><td> $.24^*$ </td><td>.05</td><td> $.22^*$ </td></tr><tr><td>4.</td><td>Sex</td><td></td><td></td><td></td><td>1</td><td> $.29^*$ </td><td>.09</td><td> $.21^*$ </td><td>-.05</td><td> $.20^*$ </td><td>-.02</td><td>-.08</td><td> $.19^*$ </td><td>.03</td><td>-.23</td><td>.05</td><td>-.17</td></tr><tr><td>5.</td><td>Typing</td><td></td><td></td><td></td><td></td><td>1</td><td> $.30^*$ </td><td>.03</td><td>-.01</td><td>.11</td><td>-.08</td><td>-.08</td><td>.16</td><td>0</td><td>-.20</td><td>0</td><td>.12</td></tr><tr><td>6.</td><td>Computer Competence</td><td></td><td></td><td></td><td></td><td></td><td>1</td><td> $.24^*$ </td><td> $.22^*$ </td><td>-.06</td><td>.07</td><td>-.02</td><td>-.09</td><td>-.10</td><td>-.07</td><td> $-.24^*$ </td><td>-.17</td></tr><tr><td>7.</td><td>% Comments</td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>-.01</td><td>.12</td><td> $.20^*$ </td><td>.07</td><td>-.03</td><td>-.03</td><td> $-.21^*$ </td><td>-.17</td><td>-.09</td></tr><tr><td>8.</td><td>% Re-Ranks</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>-.14</td><td>-.02</td><td>-.06</td><td>-.07</td><td>-.15</td><td>-.15</td><td>-.16</td><td>-.11</td></tr><tr><td>9.</td><td>Initial Group Deviation</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td> $.29^*$ </td><td> $.32^*$ </td><td> $.55^*$ </td><td>.13</td><td> $.32^*$ </td><td>.08</td><td>0</td></tr><tr><td>10.</td><td>Final Group Deviation</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td> $.67^*$ </td><td> $-.60^*$ </td><td>.06</td><td> $-.26^*$ </td><td>.07</td><td>.15</td></tr><tr><td>11.</td><td>Final Individual Deviation</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td> $-.29^*$ </td><td>-.02</td><td> $-.25^*$ </td><td>.05</td><td>.12</td></tr><tr><td>12.</td><td>% Improvement</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>.03</td><td>.01</td><td>.02</td><td>-.11</td></tr><tr><td>13.</td><td>Information Exchange</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>.16</td><td> $.18^*$ </td><td> $.32^*$ </td></tr><tr><td>14.</td><td>Get to Know</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>.07</td><td> $.28^*$ </td></tr><tr><td>15.</td><td>Friendly</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td> $.49^*$ </td></tr><tr><td>16.</td><td>Productive</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td></tr></table>

Appendix 2 Group Level Variables (N = 24 Groups)

<table><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td></tr><tr><td>1. Designated Leader</td><td>1</td><td>2</td><td>-.14</td><td>.13</td><td>.02</td><td>.13</td><td>-.11</td><td></td><td>-.09</td><td>.17</td><td>.04</td></tr><tr><td>2. Statistical Feedback</td><td></td><td>1</td><td>-.09</td><td>.11</td><td>-.10</td><td>.04</td><td>.10</td><td>.39</td><td> $-.42^{\circ}$ </td><td>-.24</td><td> $-.43^{\circ}$ </td></tr><tr><td>3. Initial Agreement</td><td></td><td></td><td>1</td><td>.28</td><td> $.46^{**}$ </td><td>.31</td><td>-.06</td><td>-.04</td><td>-.02</td><td>-.16</td><td>.05</td></tr><tr><td>4. Discussion Agreement</td><td></td><td></td><td></td><td>1</td><td> $.75^{**}$ </td><td> $.62^{**}$ </td><td> $-.37^{\circ}$ </td><td> $-.55^{\circ}$ </td><td>-.29</td><td>.25</td><td>.15</td></tr><tr><td>5. Group Agreement</td><td></td><td></td><td></td><td></td><td>1</td><td> $.58^{**}$ </td><td>-.07</td><td>-.32</td><td>-.10</td><td>-.01</td><td>.01</td></tr><tr><td>6. Individual Agreement</td><td></td><td></td><td></td><td></td><td></td><td>1</td><td> $-.46^{**}$ </td><td>.14</td><td>-.13</td><td> $.42^{\circ}$ </td><td> $.37^{\circ}$ </td></tr><tr><td>7. Group Deviation</td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td> $.74^{**}$ </td><td> $.41^{\circ}$ </td><td> $-.85^{**}$ </td><td> $-.70^{\circ}$ </td></tr><tr><td>8. Leader Deviation (N=12)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>.47</td><td> $-.45^{\circ}$ </td><td> $-.57^{\circ}$ </td></tr><tr><td>9. Least Deviation</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>.05</td><td> $.36^{\circ}$ </td></tr><tr><td>10. % Improvement</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td> $.90^{**}$ </td></tr><tr><td>11. Collective Intelligence</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td></tr></table>
