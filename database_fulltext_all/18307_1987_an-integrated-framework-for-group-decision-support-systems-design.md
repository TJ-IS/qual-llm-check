---
otero_id: 18307
otero_key: "UYVH9CE4"
title: "An integrated framework for group decision support systems design"
authors: "M.Tawfik Jelassi; Renée A. Beauclair"
year: "1987"
journal: "Information & Management"
doi: "10.1016/0378-7206(87)90022-x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An Integrated Framework for Group Decision Support Systems Design \*+

M. Tawfik Jelassi

Operations and Systems Management Department, Graduate School of Business, Indiana University, Bloomington, Indiana 47405, USA

and

Renée A. Beauclair

Management Department School of Business, University of Louisville, Louisville, Kentucky 40292, USA

Revised: September 1987.

Proposed approaches for the development of Group Decision Support Systems (GDSS) address behavioral and technical aspects of these systems. However, these approaches generally address only one of these aspects at a time. This paper reviews these approaches and suggests a framework for developing GDSS based on an integrated perspective. This proposed framework is comprehensive and integrative as it combines the behavioral characteristics of group decision making with the technical specifications that drive GDSS. Software design and future research issues are discussed.

Keywords: Group decision making, Group decision support systems, Behavioral issues, System development, Software design.

## 1. Introduction

The small decision-making group is an important fixture in today's organization. As more and more critical decisions are made by groups, the effects of the weaknesses and pitfalls of small group interaction also become more apparent. Because good decision making is crucial at all levels of an organization, many attempts are being made to help reduce the negative aspects of small group decision making. An example of such an attempt is the development of Group Decision Support Systems (GDSS). GDSS are technologies designed to help people make faster, more satisfying, and ultimately “better” decisions than they may be making without them. While group sizes vary

![](/api/attachments/UYVH9CE4/fulltext/images/428b0c7e94006ddbd0e94060e8df936716a68b8fc055ed82dd73aa42bcf60c86.jpg)  
and government.

Renée A. Beauclair is Assistant Professor in the Management Department, School of Business at the University of Louisville. She received her BA and MA from Louisiana State University and her Ph.D. from Indiana University. Her doctoral research addressed the effects of group decision support systems (GDSS) on small group decision making. Her current research also involves GDSS. In addition to her academic responsibilities, Dr. Beauclair serves as a consultant to business

![](/api/attachments/UYVH9CE4/fulltext/images/6356f29d1563204563d4956eb67c75ab31b47a5f2f5d98c8579dbe9c757a38f9.jpg)

M. Tawfik Jelassi is an Assistant Professor of Management Information System at Indiana University. He received a Ph.D. in Computer Applications and Information Systems from New York University, and Diplomas in Computer Science and Business Administration from the Université de Tunis and the Université de Paris-Dauphine. Dr. Jelassi has published a number of journal articles, book chapters and conference papers in the areas of Decision Support Systems,

Multiple Criteria Decision Making, and Database Applications.

across organizations and tasks, this paper will deal only with literature and issues pertinent to small decision making groups (three to twelve members). This restriction is due to the nature of the specific type of group decision support environment discussed as well as our experiential knowledge.

Unfortunately, current research in Group Decision Support Systems lacks a substantial and integrated focus. Technical design specifications for GDSS have been developed and behavioral aspects of group decision making explored. However, no generally accepted, specific criteria or guidelines that uniquely integrate the technical and behavioral aspects of GDSS in small decision-making groups have been provided. Also, the role of human behavior in the success or failure of GDSS has not been thoroughly addressed [21].

The purpose of this paper is to address the rationale for an integrated approach to GDSS design that includes behavioral and technical aspects of these systems. Section 2 of this paper provides a working definition of the GDSS concept. Section 3 surveys some of the well-known approaches to GDSS. Section 4 proposes a set of behavioral issues generated through a multi-disciplinary approach. Based on these issues, Section 5 discusses GDSS design features and the advantages of integrating the behavioral dimension when developing group decision support systems.

## 2. Definition of Group Decision Support Systems

A GDSS is broadly defined as an interactive, computer-based information system which is used to enhance structured, semi- and unstructured group decision-making tasks in organizations. Like individual decision support systems (IDSS), GDSS are designed to provide tools for decision-making by supporting the three basic DSS functions of data, model, and dialogue management [26]. Unlike IDSS, however, GDSS also facilitate decisions which must be made by more than one person (through the use of a communication sub-system).

![](/api/attachments/UYVH9CE4/fulltext/images/a8936218e879a1d8ac8ce30dd4bea71bf124f45dda4e96e995d03c626925723e.jpg)  
Fig. 1. Taxonomy of Group Decision Support Systems.

Based on this definition, GDSS may include:

1. face-to-face as well as non-face-to-face interactions;

2. synchronous or asynchronous sessions; in other words, interactive participation takes place at the same time (as in a teleconference system), or at different times and at the participants' convenience (by using electronic mail); and

3. close or dispersed proximity configurations (i.e. group members are either in the same room or separated geographically).

As shown in Fig. 1, this paper focuses on the face-to-face, close proximity, synchronous GDSS type commonly known as “war room” [30] or a “decision room” [6]. The decision room features computerized support in addition to traditional small group interaction (see Fig. 2).

In order to clarify the figure, think of a GDSS as a conference or meeting room with computer support. Picture the place where you have attended meetings before and add a computer terminal for each participant. Next, add a large video screen in a prominent place so that everyone is able to see it. Now put yourself and those you work with behind each of the terminals. This is what a GDSS looks like [1].

A brief review of some well-known approaches to GDSS outlines the state-of-the-art of these systems and reinforces the need for an integrated approach to GDSS development that includes behavioral as well as technical characteristics.

![](/api/attachments/UYVH9CE4/fulltext/images/130d1f7bb544b8a89a663c693dd681d82cb95c35ff84ef290b4880d2b48b5efc.jpg)  
Fig. 2. The GDSS room.

## 3. GDSS Approaches

Gray et al. [12] describe an actual GDSS implementation which is referred to as the SMU Decision Room Project. The goal of the system was to facilitate the integration of new group decision support technologies into the senior executive environment. The authors address the nature of group decision making in business, design concepts, initial research programs, and possible educational uses of decision rooms. They also develop different design criteria for specific decision making situations.

Gray [11] describes how this facility was tested through executive MBA student exercises. The exercises were not formal experiments but provided the following “initial impressions”: (1) GDSS enable the testing of numerous alternatives without staff intervention, (2) groups are able to concentrate only on promising alternatives, (3) communication is unstrained, and (4) pre-discussion training is advised for successful group interactions.

The work of Gray et al. does not present a formalized perspective as such; however, they do provide sketches of “design considerations” and enough information to discern the underlying assumptions which drive their studies. Implicit assumptions in these works include: GDSS should be suited for generation of alternatives; GDSS should help focus some groups on promising alternatives while allowing others to delete unpromising ones; and GDSS should mirror decision activities as business people have already experienced them. These studies suggest a “menu”-driven approach suited to provide flexible support.

Huber [13] deals with three system-related issues: capabilities, delivery modes, and design strategies. He maintains that the purpose of GDSS is to augment the effectiveness of decision groups through the interactive sharing of information between group members and the computer.

While Huber's work helped form a basis for future GDSS research, its tri-leveled approach is rather vague. The delivery section deals with actual types of systems acquisition (e.g. rent versus buy), and the capabilities section is a list of what applications a GDSS should provide. Design strategies are either technique- or task-driven. These three levels are almost entirely technical, and Huber assumes that GDSS will help groups make better decisions because they increase information sharing and the use of information between group members. No discussion of the causal, behavioral link between computer intervention and resulting behaviors is provided.

DeSanctis and Gallupe [6] categorize GDSS technology into four separate areas: decision room, local decision network, linked decision rooms, and remote decision networks. They distinguish between the four models in terms of proximity of participants and duration of the decision making session.

This work was one of the first to view GDSS from a comprehensive, practical perspective and answered such questions as: What do GDSS look like? How and when would we use GDSS? The answers to these questions help us get closer to a shared, accepted view of what GDSS is or can be. They serve as a first step to a more sophisticated approach for GDSS. However, they do not develop GDSS design strategies to the extent that an underlying theoretical perspective can be traced.

Gallupe [9] deals, from a pragmatic perspective, with issues involved in experimental research in GDSS, specifically task, type of GDSS, and research methods (subjects, setting, measurement). His research results confirm the usefulness of GDSS; for example, decision quality was improved under certain conditions within the GDSS environment. These results enable Gallupe to make limited predictions about certain decision making environments as well as practical decisions about future GDSS design.

This work deals with the practical side of experimentation in GDSS and serves as an excellent guide to the GDSS researcher. Although we can make some predictions based on his observations, he does not, however, formally address theoretical or design-oriented issues.

In the remote decision network type, Bui and Jarke [3] propose a distributed architecture for a cooperative GDSS that uses a multiple-criteria decision model as “a vehicle to integrate approaches developed in conventional single-user DSS and in computerized conferencing systems”. In particular, they map the requirements for human-human communications via electronic media into layers of the International Standards Organization (ISO) model for communications [2]. Their work is among the first of its type to contribute a specific conceptual framework for technical design of GDSS.

Lewis and Keleman [24] present a “contingency approach” to GDSS advocating the eventual use of expert systems in GDSS development and usage. They describe GDSS generators and integrators, and the contingencies one would address when using the GDSS integrator to choose tool modules. Their paper has a practical focus and presents possible choices for software packages that can be used to build a GDSS.

The contribution of Lewis and Keleman's work lies in its creativity and the rule-based approach to GDSS development. Unfortunately, the “rules” stem mainly from situational variance and are not adequately based on theoretical behavioral contingencies. It should be noted, however, that Lewis and Keleman point out the need for more work in the theoretical domain, particularly work that would help us determine all of the variables involved in small group decision making.

As this brief review shows, no integrated design criteria have been presented which consider both the human and technical aspects of the system (see Table 1). Either technical specifications, tasks and techniques, or personal experiences of the designer have driven design strategies thus far. No guidelines grounded in adequate behavioral theory and coupled with technical design specifications have been provided which help guide the GDSS developer.

Table 1.
List of GDSS approaches.

<table><tr><td>AUTHOR</td><td>CONTRIBUTION</td></tr><tr><td>Gray, et al (1981)</td><td>Described SMU Decision Room</td></tr><tr><td>Gray (1983)</td><td>Described how SMU facility was tested</td></tr><tr><td>Huber (1984)</td><td>Provided general design strategies</td></tr><tr><td>DeSanctis &amp; Gallupe (1985)</td><td>Defined and categorized GDSS types</td></tr><tr><td>Gallupe (1986)</td><td>Presented pragmatic issues in GDSS research</td></tr><tr><td>Bui &amp; Jarke (1984)</td><td>Proposed distributed architecture for GDSS</td></tr><tr><td>Bui &amp; Jerke (1986)</td><td>Developed conceptual communication model for GDSS</td></tr><tr><td>Lewis &amp; Kelemen (1986)</td><td>Constructed contingency approach to GDSS</td></tr></table>

A GDSS, as any computer-based information system, is useless if humans reject it. The following section reviews the strengths and weaknesses of small decision making groups as viewed by the behavioral sciences. This will allow us to understand how GDSS may act as an intervention tool and a means by which the small group process may be enhanced. The subsequent sections provide system design strategies based on these characteristics, as well as organizational needs and GDSS constraints. It is hoped these strategies will help developers generate decision-aid systems which groups will use and benefit from.

## 4. Behavioral Issues in GDSS

The literature review suggests that many GDSS researchers believe a priori that a computerized environment is necessarily better than its non-computerized counterpart; yet little formal, theoretical support is provided by which to ground such beliefs. This section reviews the predicted benefits of GDSS in terms of research in small group decision making that deals with similar, though non-computer-supported situations.

While GDSS developers are trying to design systems that will help structure the group process, it is important to acknowledge briefly the characteristics that decision makers bring with them to the decision making environment [10,27]. These include:

1. individual characteristics of each group member (e.g. personality, sex, age, race, status, socioeconomic background, competence, and motivation);

2. group characteristics (e.g. political orientation, leadership, complexity of the task and circumstances, size of group, and history of its members); and

3. environmental characteristics (e.g. setting, scheduling, length of a session, organizational context, and spatial arrangement).

A GDSS clearly cannot at this time resolve all of the problems created by the characteristics listed above, but it should be designed and used with these considerations in mind. It must be understood that most situational variables are not under the control of the GDSS developer. While researchers have addressed some of these variables [9], only Lewis and Keleman [24] specifically use them to devise their contingency model of GDSS. Unfortunately, as previously mentioned, their approach does not go into enough depth in terms of design strategies.

![](/api/attachments/UYVH9CE4/fulltext/images/45c87669a61de1d84435cf84195aa8dbfa7df5821466f9911dfb2d401b4a94aa.jpg)  
Fig. 3. Behavioral issues in GDSS design.

Groups can affect individuals in a destructive manner. These effects, with which the GDSS potentially can deal, include diffusion of responsibility, deindividuation, pressures toward group consensus, and problems of coordination [25,27]. We may come closer to a more formalized, theory-based rationale for GDSS development by having a better understanding of the destructive nature of small group interaction. Thus, we can develop design strategies that counter negative characteristics of group decision making while enhancing the positive ones (see Fig. 3).

Diffusion of responsibility, also known as social loafing, results when group members fail to take responsibility for their own actions. Researchers in this area maintain that the lack of a sense of uniqueness may cause people to do less work or perform below average [22], or lead to more risky or conservative decisions than might otherwise be reached by individuals acting alone [28,29].

Deindividuation is similar to diffusion of responsibility and occurs when group members lose their sense of objective self-awareness $[5,7,27]$ . Decision makers lose a sense of themselves as consequential participants and therefore run the risk of behaving in completely irrational ways. Examples of behaviors that result from deindividuation include lynch mobbing and “mass hysteria”.

Pressures toward group consensus may cause a group member to support an alternative or vote in a way that represents the perceived mood of the group, not necessarily the participant's [27]. These pressures occur when a person is not given adequate feedback as to his or her position in the group or is not allowed a free or anonymous atmosphere in which to express his or her opinion.

These issues are also addressed in the “groupthink” literature [4,8,14].

Problems of coordination arise from the nature of small group design. Group structure, the logistics of meeting in groups, group leadership, and specific problem definition all have a bearing on how the group's interaction will evolve [25]. However, in general, groups are slower than individuals as a result of these practical considerations. This slowdown is seen in longer feedback loops, meetings, and delayed reporting of results.

While these four characteristics of groups are generally considered to be destructive, it is possible to use diffusion of responsibility to our advantage during certain situations. In other words, there may be some constructive aspects of this characteristic if manipulated properly. Therefore, how can we use GDSS to enhance the constructive possibilities of diffusion of responsibility? Alternatively, how can we reduce the destructive aspects of problems of coordination, pressure toward group consensus, deindividuation, and diffusion of responsibility? A brief discussion of each of these will give us a better understanding of how theory may help drive design.

Uncontrolled diffusion of responsibility is clearly destructive in that it can lead group members to feel less responsible for their own behavior. It also may lead the entire group to make riskier or more conservative decisions than they might otherwise. However, in some situations the lack of a sense of uniqueness that leads to diffusion of responsibility could be useful. For example, high risk-taking behaviors may be appropriate to some decision environments such as brainstorming for ideas. Also, creativity could be enhanced because participants feel freer to express themselves in less conventional or normally unacceptable means.

![](/api/attachments/UYVH9CE4/fulltext/images/ad51f8b69b40d3a2ce464eb233f303b870dcd7603b09c13e865ce4a4653e92e1.jpg)  
Fig. 4. Advantages and disadvantages of behavioral issues in GDSS.

This can be an advantage in a situation that demands high creativity on the part of group members. Thus, how can GDSS, when appropriate, enhance creativity without letting things get out of hand?

Deindividuation, the lost sense of self-awareness, is often cited as the reason for hysterical “lynch mob” activities. Clearly, it probably would never be to a group’s advantage to encourage this behavioral characteristic, so how can a GDSS help us to reduce the possibilities for deindividuation across decision situations?

Pressure toward group consensus is often cited as contributing to the condition known as “groupthink” – the group loses sight of itself as a part of its environment and fails to take into account disconfirming or outside information [14]. There is also pressure from within the group to gain consensus and restrict opinions that are not in agreement with the group’s. This is a situation that we want to avoid since it may lead to risky decisions. The group may fail to generate numerous alternatives, and may suffer from an overall lack of creativity. What can we provide through computerized support that would help groups reduce unwarranted pressure toward group consensus and possible “groupthink”?

The last category is the problems of coordination that arise from the means by which small groups interact. The logistics of arranging meetings, the structure (or lack) of leadership, and definition of the group's problem all constitute problems of coordination, as do some of the situational variables mentioned above. Logistical and technical problems, slow feedback and potential for inaccuracies in intricate manual procedures such as voting/ranking, as well as poorly supported working conditions can lead to the frustration of group participants. How can we help groups coordinate these aspects of group decision-making?

Fig. 4 provides a summary of the advantages and disadvantages of behavioral issues in GDSS as discussed in this section. With these issues in mind, how can we design GDSS to better serve the small group decision making environment?

## 5. GDSS Design Issues

In this section, an attempt is made to answer the behavioral questions raised above. Related

GDSS design issues are addressed from a technical perspective. Our goals are twofold: through GDSS interventions, (1) reduce the negative impact, and (2) enhance the positive effect that diffusion of responsibility, problems of coordination, pressures toward consensus, and deindividuation have on group decision making.

As mentioned earlier, diffusion of responsibility (or social loafing) can have a positive contribution to the decision-making capability of the group in situations where risk may be taken (e.g. case of entrepreneurial organizations). GDSS can enhance this constructive feature by supporting anonymity in the system. This may lead to greater freedom and creativity at the decision maker level since she/he can use the system and remain anonymous.

On the other hand, in situations where diffusion of responsibility has a destructive impact on group decision making (e.g. crisis intervention), GDSS should reduce the lack of sense of uniqueness among decision makers, by not supporting anonymity in the system. This can be implemented by associating the decision maker's name with his/her inputs. For example, in voting, ranking, or brainstorming applications, the GDSS displays on the public screen, or on each workstation terminal, group member's input(s) and identity. This may lead to a greater sense of responsibility and careful thought among decision makers before stating opinions or suggesting ideas to the group.

A third design approach can be defined as a combination of the two strategies described above. Rather than supporting (or not supporting) anonymity all the way in the system, the third approach reduces the disadvantages of diffusion of responsibility in two steps:

Step 1. Display graphically on the public screen the overall results of the group. This step enforces anonymity and provides each member with feedback on the group's opinion. At this stage, the decision maker whose input significantly differs from the average; in other words, the outlier, can either change his/her opinion to join the group's (i.e. to be part of the cloud of points) or stick with his/her current attitude. If this latter case happens, Step 2 is performed. Note that Step 1 is rather a computerization of the DELPHI technique.

Step 2. Display, in a tabular form, each member's input(s) and name as well as the variance and mean values. In this step, anonymity is obviously not supported by the system and therefore may help to generate discussions among group members. In particular, the “outlier” can either change his/her input(s) or explain his/her opinion to the group.

Notice that the two-step approach outlined above encourages or forces the group, to some extent, to reach a consensus which may or may not increase personal responsibility among decision makers. What circumstances make this desirable is a research issue that needs to be investigated.

Deindividuation, or the loss of the sense of objective self-awareness, can be reduced through GDSS intervention. For example, the act of keying data into the system helps reinforce the decision-maker's self awareness. He/she has to think prior to entering data, answering the system's questions, or selecting an option from a menu screen during an interaction (e.g. brainstorming, voting, ranking, or negotiation). Unlike a verbal interaction, in which oral communication flows rather naturally, participants at this stage must transfer their thoughts through a physical medium, thus creating one more step at which he or she must reflect on the situation and his or her role in it.

Moreover, participation can be forced by entering, at the beginning of the session, the number of participants. Whenever an interaction between the GDSS and decision makers takes place (e.g. input requests), the system will not start processing results until all group members have entered their response, vote, rank, or opinion. This control can be implemented by using a count variable, initialized to zero before each input request, and incremented by one whenever a data entry, performed at the workstation level, is received through the local area network. These deindividuation-related GDSS interventions enhance group member's sense of self as a consequential participant.

Also, a good response time (i.e. of the order of few seconds) of the system would keep discussions among decision makers “on track” and live. However, if the GDSS supports anonymity, this may enhance the negative impact that deindividuation has on group decision making.

Pressures toward group consensus may cause decision makers to feel pressured to support an alternative or a vote in a way that represents the perceived mood of the group. This may lead to groupthink, risky decisions, and a failure to consider/generate numerous alternatives. Consequently, the group may make a decision for which individual decision makers do not want to take responsibility or that does not represent the true feelings of the members.

GDSS intervention can reduce the negative effects of pressures toward group consensus. For example, by supporting anonymity in using the system, the GDSS can significantly minimize peer pressure. Also, the use of a public screen to display group inputs allows each decision maker to know the results at any stage of the session. If these results are shown in an aggregated form (e.g. averages, variances, cross-impact analysis), each member can see the general direction of the group. If detailed results (e.g. individual votes/rankings, suggested items, generated alternatives) are provided, each decision maker is informed on exactly what everyone in the group is up to. Moreover, accurate results and a quick response time can present the group mood as it actually exists. This may be quite different from the mood as perceived by each participant. By introducing the “true” group mood we can reduce errors in judgment based on erroneous individual perceptions.

Problems of coordination between decision makers arise from the nature of small group interactions; e.g. structure, leadership, and problem definition. These problems can cause frustration among group members and may lead them in a “wrong” direction. Moreover, poorly defined decision problems can result from the lack of coordination between participants. Other factors such as overcrowding, poor working conditions, as well as slowness and inaccuracy of manual processes (due to the computing of averages/variances by hand or using a calculator) have a destructive impact on group decision making.

To alleviate the problems mentioned above, GDSS can be used to impose some structure on the decision process. For example, one GDSS called “FACILITATOR” [23] starts by asking each group member to enter first his/her set of goals (or objectives), then the list of situational constraints (or limitations), followed by the set of obstacles to the goals, and finally the suggested alternatives. Having a defined structure of the decision process improves the degree of accuracy and the response time of the system. Certain software applications such as voting, rating, brainstorming, as well as computerized nominal group techniques can help groups formulate problems clearly through a predefined structure of the decision process.

This discussion of GDSS design issues is a positive step toward a behaviorally-driven design of group decision support systems. As we have shown, design strategies can be specific to certain group behaviors (e.g. diffusion of responsibility) as well as general to computer-based decision support systems (e.g. communication and information sharing, consistency, and coherence). It is also important to consider the situational variables that a group brings to the decision making environment (e.g. task complexity, group size, and political climate) when designing tools for group use [17].

What other issues must be considered in GDSS design? In addition to the specifications already discussed, the system should be technically proficient and deliver the services for which it was designed (i.e. support group decision making). It also should be coherent, consistent, complete, fast, and able to support communication, information sharing, as well as democratic control. A discussion of each of these general issues follows.

GDSS should be able to verify the validity of decision maker's inputs when they correspond to factual data already-available in the system. This can be done by performing through a database management system (DBMS), for example, syntactic and semantic checks and enforcing pre-defined integrity constraints [17,20]. Validated inputs constitute the users' views of the decision problem at hand. These views are then integrated and serve as a basis for reaching a group solution. Techniques borrowed from relational database theory could assist in the view integration task – for more details see [15]. View integration should be performed whenever a pooled mode of group decision making is precluded by the existence of strongly defended, elaborate individual positions, as typical in many not fully cooperative GDSS situations.

System outputs should also be coherent. The response to each user request should be provided in a recognizable and consistent form within the same session as well as over longer periods of time and spanning different sessions. Also, the user interface should be consistent in generating screen contents for text display, data entry/update, or menu choice. In other words, the form and format of the menus should be the same across applications and iterations – for more details see [18]. Coherence and consistency on these levels will allow groups to make better decisions in that the feedback received will be in a representative and understandable form.

Generating a complete set of decision alternatives often requires the availability of a variety of data sources. The data gathering process may involve using private/public and internal/external data sets, as well as accessing local data bases (usually stored on a personal computer) or remote ones (available on mini- or mainframe systems). Data completeness, like coherence, speed, and accuracy, plays an important role in group performance. The attributes outlined above are instrumental in helping groups make decisions of higher quality than those they might make in a non-computerized environment because they provide instant, accurate, and substantive feedback to decision makers. These attributes also specifically deal with problems of coordination.

A GDSS should be fast (in terms of response time) for the individual as well as the group. By providing quick results, the GDSS is better able to facilitate the group process. Instant feedback helps reduce confusion on issues, boredom, and enhances confidence in the system. Social loafing will be less of a problem if each individual is constantly reminded of his or her role as participant in the group through communication with the machine. Also, pressures toward consensus will be reduced as each participant is constantly aware of how he or she stands within the group.

Pre-existing, democratic control structures should be established to reduce the influence of powerful or dysfunctional personalities. These control structures can be developed through software by establishing: (1) voting procedures based on one-person-one-vote; (2) negotiation software that enhances the equality of participants [16]; and (3) brainstorming outlets that allow equal time to all group members.

The system should provide communication and information sharing as much as possible and when desirable. This should be accomplished through local as well as public display, and allow for brainstorming in addition to data and model sharing. This feature would allow participants to generate ideas freely and without prejudice, and have a shared model that can serve as a basis for discussion.

## 6. Conclusion

As stated earlier, GDSS design must take into consideration behavioral as well as technical issues in order to develop useful and effective systems. A technically proficient system is useless if people are unwilling to interact with it; yet current thoughts on the design and implementation of GDSS do not propose an adequately integrated framework for the development of these systems.

This paper reviewed relevant research in order to point out weaknesses in current GDSS design. A series of behavioral issues were addressed, and a list of design criteria based on the behavioral and technical aspects of GDSS was presented. The integration of the behavioral with the technical was stressed throughout.

Future research in GDSS should bear these issues in mind. First of all, GDSS technology is expensive. Organizations stand to invest a lot of money into a GDSS which, if poorly designed, could lead to worse interactions and poorer quality decisions than those made before its implementation. Second, persons involved in sessions using a GDSS are more likely to be making decisions of great consequence to the organization. A poorly designed and conceived GDSS might aggravate a difficult situation or provide insufficient/incoherent data that could lead a group to make a “wrong” decision. Last, given the state of the study of small group dynamics and recent DSS technological advances, tools are becoming available to create useful and effective GDSS. Our task, then, is the integration of the two.

## References

[1] R.A. Beauclair (1987): An Experimental Study of the Effects of GDSS Process Support Applications on Small Group Decision Making. Unpublished Ph.D. dissertation, Indiana University.

[2] X.T. Bui and M. Jarke (1986): Communication Requirements for Group Decision Support Systems. Journal of MIS, Vol. 2, No. 4, pp. 8–20.

[3] X.T. Bui and M. Jarke (1984): A DSS for Cooperative Multiple Criteria Group Decision Making. Proceedings of the Fifth International Conference on Information Systems, pp. 101–113.

[4] J.A. Cartwright (1978): A Laboratory Investigation of Groupthink. Communication Monographs, Vol. 45, pp. 229–246.

[5] E. Diener (1980): Deindividuation: The Absence of Self-Awareness and Self-Regulation in Group Members. In P.B. Paulus (ed.), Psychology of Group Influence. Hillsdale, NJ: Erlbaum.

[6] G. DeSanctis and R.B. Gallupe (1985): Group Decision Support Systems: A New Frontier. Database, Vol. 16, pp. 3–10.

[7] L. Festinger, A. Pepitone, and T. Newcomb (1952): Some Consequences of Deindividuation in a Group. Journal of Abnormal and Social Psychology, Vol. 47, pp. 382–389.

[8] M.L. Flowers (1977): A Laboratory Test of some Implications of Janis's Groupthink Hypothesis. Journal of Personality and Social Psychology, Vol. 5, pp. 888–896.

[9] R.B. Gallupe (1986): Experimental Research into Group Decision Support Systems: Practical Issues and Problems. Proceedings of the Nineteenth Hawaii International Conference on System Sciences.

[10] D.S. Gouran (1982): Making Decisions in Groups: Choices and Consequences. Glenview, IL: Scott-Foresman.

[11] P. Gray (1983): Initial Observations from the Decision Room Project. Proceedings of the Third International Conference on Decision Support Systems, Austin, TX, pp. 135–138.

[12] P. Gray, N.W. Berry, J.S. Aronoksky, O. Helmer, G.R. Kane, and T.E. Perkins (1981): The SMU Decision Room Project. Proceedings of the First International Conference on Decision Support Systems.

[13] G. Huber (1984): Issues in the Design of Group Decision Support Systems. MIS Quarterly, Vol. 8, pp. 195–204.

[14] I.L. Janis (1981): Groupthink (2nd ed.). Boston: Houghton-Mifflin Company.

[15] M. Jarke and M.T. Jelassi (1986): View Integration in Negotiation Support Systems. Transactions of the Sixth International Conference on Decision Support Systems, Washington, D.C., April 21–24.

[16] M. Jarke, M.T. Jelassi, and M.F. Shakun (1987): MEDIATOR: Towards a Negotiation Support System. European Journal of Operational Research, Vol. 31, No 3.

[17] M.T. Jelassi (1985): An Extended Relational Database for Generalized Multiple Criteria Decision Support Systems. Ph.D. Dissertation, Department of Computer Applications and Information Systems, New York University.

[18] M.T. Jelassi and X.T. Bui (1987): Prise de Décision dans l'Organisation: Quand les SIAD Peuvent-Ils Aider? European Journal Interfaces (forthcoming).

[19] M.T. Jelassi, M. Jarke, and A. Checroun (1985): A Database Approach for Multiple-Criteria Decision Support Systems. In G. Fundel and J. Spronk (eds.), Multiple-Criteria Decision Methods and Applications. Berlin: Springer-Verlag, pp. 227–244.

[20] M.T. Jelassi, M. Jarke, and E.A. Stohr (1985): Designing a Generalized Multiple-Criteria Decision Support System. Journal of Management Information Systems, Vol. 1, No. 4, pp. 24–43.

[21] K.L. Kraemer and J.L. King (1983): Computer Supported Conference Rooms: Final Report of a State-of-the-Art Study. Unpublished working paper, University of California at Davis.

[22] B. Latane, K. Williams, and S. Harkins (1979): Many Hands Make Light the Work: The Causes and Consequences of Social Loafing. Journal of Personality and Social Psychology, Vol. 37, pp. 822–832.

[23] L.F. Lewis (1986): Facilitator: A Decision Support System for Groups. User's Guide.

[24] L.F. Lewis, and K.S. Keleman (1986): A Contingency Approach to GDSS Design Using Expert Systems. Unpublished working paper, Western Washington University.

[25] M.E. Shaw (1981): Group Dynamics: The Psychology of Small Group Behavior (3rd ed.). New York: McGraw-Hill.

[26] R.H. Sprague and E.D. Carlson (1982): Building Effective Decision Support Systems. Englewood Cliffs, NJ: Prentice-Hall.

[27] W.S. Swap (1984): Destructive Effects of Groups on Individuals. In W.S. Swap, et. al. (eds.), Group Decision Making. Beverly Hills: Sage Publications.

[28] M.A. Wallach, N. Kogan, and D. Bem (1962): Group Influence on Individual Risk Taking. Journal of Abnormal and Social Psychology, Vol. 68, pp. 263–274.

[29] M.A. Wallach, N. Kogan, and D. Bem (1964): Diffusion of Responsibility and Level of Risk Taking in Groups. Journal of Abnormal and Social Psychology, Vol. 68, pp. 263–274.

[30] R.W. Widener (1981): Corporate Briefing Rooms and Management Communication Centers in Decision Making. National Symposium on Office Automation, DPMA.
