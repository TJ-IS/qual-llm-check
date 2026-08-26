---
otero_id: 4796
otero_key: "ZRAURE6E"
title: "Could the use of a knowledge-based system lead to implicit learning?"
authors: "Solomon Antony; Radhika Santhanam"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.08.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dss

# Could the use of a knowledge-based system lead to implicit learning?

Solomon Antony <sup>a</sup>, Radhika Santhanam <sup>b,⁎</sup>

<sup>a</sup> Murray State University, USA <sup>b</sup> University of Kentucky, USA

Received 5 August 2005; received in revised form 28 June 2006; accepted 10 August 2006 Available online 20 September 2006

## Abstract

The primary objective of a knowledge-based system (KBS) is to use stored knowledge to provide support for decision-making activities. Empirical studies identify improvements in decision processes and outcomes with the use of such knowledge-based systems. This research suggests that though a KBS is primarily developed to help users in their decision-making activities, as an unintentional consequence, it may induce them to implicitly learn more about a problem. Implicit learning occurs when a person learns unconsciously or unintentionally, without being explicitly instructed or tutored. To test these ideas, a laboratory-based experiment was conducted with a KBS that could provide support for data modeling activities. Results indicated support for implicit learning because subjects who interacted with the KBS exhibited better knowledge on data modeling concepts than those who did not interact with the KBS. Two versions of the KBS were tested, one with a restrictive interface and the other with a guidance interface, and both versions of the interface supported implicit learning. Implications for future research on the design and development of KBSs are proposed.

Keywords: Knowledge-based systems; Learning; Interface; Data modeling

## 1. Introduction

Knowledge-based systems (KBSs) are developed to improve their users' decision-making and problemsolving capabilities. A KBS is defined as a system that uses stored knowledge of a specific problem to assist and provide support for decision-making activities related to the specific problem context [22,24]. KBSs have been developed and used for a variety of applications, including database design activities, with controlled experiments showing that KBSs, as decision-aiding tools, can alter the decision outcomes, processes, and strategies of users as they engage in tasks [15,35,42]. Consequently, the primary emphasis on KBS research has focused on the role of a KBS as a decision-aiding tool and the intended consequences of improvements in users' decision processes and outcomes.

In this study, it is proposed that a KBS can play yet another role; it can be an agent of change to improve the user's knowledge. When a user interacts with a KBS and obtains help in solving a problem, the user may learn more about the problem and thus implicitly acquire knowledge. Implicit learning occurs when the user applies no deliberate or intentional effort to learn, but learning still occurs unconsciously [8,9,32]. Implicit learning differs from conscious and directed learning that might occur with knowledge repositories or with tutoring systems that are specifically developed to teach [1,3,21]. The objective of tutoring systems is to teach users how to acquire knowledge about problem areas. These systems typically test users' initial knowledge level and then teach in an approach similar to methods an instructor would use. Knowledge repositories discussed in the context of knowledge management systems store vast amounts of knowledge and allow users to consciously access this storehouse whenever it is needed.

As opposed to the above systems, it is proposed that decision support/aiding systems, such as computer-aided software engineering tools that are primarily designed to assist a decision maker, when embedded with knowledge, may induce users to learn more about problems as they interact with the system. To test these ideas, using theoretical perspectives from implicit learning and a KBS designed to support database design activities, a laboratory-based experiment was conducted.

Database design is a complex task, and many knowledge-based tools have been proposed to support this activity [7,27,42]. This study used a KBS that had embedded knowledge on data-modeling and could assist novices in completing data modeling tasks [6]. Two versions of this KBS were tested, each of which interacted differently with the user. One version had an interface that could be termed “restrictive” because it forced the user to follow a specific decision strategy in developing a data model, while the other version could be termed “guidance” because it offered suggestions to help users complete their data modeling tasks [37]. When users interacted with these versions of a KBS, the level of their learning was determined and compared with the learning of users who interacted with a control system that had no embedded knowledge on data modeling. Results suggest that KBSs may indeed induce users to implicitly acquire more knowledge.

## 2. Knowledge-based systems and implicit learning

In one of the earliest works on decision-aiding tools, Decision Support Systems (DSSs) were defined as coherent sets of computer-based technology that managers can interact with and use as aids for their decisionmaking activities [24]. This definition has spurred a tremendous amount of research in improving the functionalities of DSSs and understanding their impact on users' decision-making activities [16]. Research studies and reports from practice indicate that, indeed, the use of a DSS can lead to substantive improvements in decisionmaking outcomes and processes [36,43].

One path of inquiry in DSS research focuses on improving the functional capability of a DSS by embedding it with knowledge of the problem area. Unlike expert systems that recommend a final decision, these decisionaiding systems support the users' decision-making process. They are often referred to as KBSs or intelligent DSSs [19,22]. Decision-making is a knowledge-intensive activity in which knowledge of a particular problem area is used to understand and make choices during the decision process. Hence, including a knowledge base in a DSS can be very advantageous in that the system can interject and provide necessary knowledge at the appropriate points in the decision process [22]. For example, a KBS for supporting manufacturing planning activities may suggest a method to reduce the setup time for manufacturing as the user is developing a manufacturing plan. The KBS shows the decision maker how to reduce setup time based on expertise embedded in the knowledge base as rules [25]. KBSs are used in many diverse applications such as financial planning, manufacturing, tax planning, and equipment design; in fact, they are more useful than expert systems that attempt to totally replace the decision makers [19,35,47].

Another research avenue has used change agency perspectives to investigate how design attributes could influence users' decision choices during the process of arriving at a final decision. A DSS could be designed to restrict users' intermediary decision choices and lead them through a specific decision strategy, or it could suggest possible intermediary decision choices and thus persuade the user to follow a certain strategy [37,39,40]. A DSS interface designed with a restrictiveness approach limits a user to a subset of all possible intermediary decision-making options, while a system with a decisional guidance approach guides its users by advising and assisting them in choosing intermediary decision options during the process of making a decision. These design principles could also be used to develop a KBS in that the system could use the embedded knowledge to provide guidance on a topic or restrict the user from making certain choices. For example, a restrictive interface in a KBS for strategic planning may restrict the user from using multi-objective decision modeling options but allow the use of uni-objective decision programming modeling options. To achieve the same objective, a guidance interface will make available all the modeling options, multi-objective and uni-objective, but suggest to users that they use a uni-objective modeling approach. Thus, with a guidance interface, the system recommends design choices during the process of making a final decision, but does not restrict their intermediary design choices. These principles of guidance and restrictiveness have been researched with findings indicating that attention to these design principles help in building more focused and effective DSSs [26,29,30,38,41,45].

Thus, considerable research is being conducted to identify ways to enhance the functional capabilities and design attributes of a DSS/KBS [22,35]. But a lessresearched aspect also deserves attention. When users interact with the KBS and are focused on task completion, they may be implicitly learning about concepts, rules, and principles that improve their knowledge structures. By the very definition of a KBS, knowledge about the specific problem area is embedded within the system. When the user is engaged in the process of making a decision, the system intervenes and uses this embedded knowledge to provide advice and may even state it in the form of knowledge rules. For example, while a user is using a taxplanning KBS, the system may intervene and suggest that the user employ a specific taxation rule; or, based on its knowledge rules, the KBS may intervene to alert the user to an error in the procedure being applied. The user may not be specifically focused on learning or memorizing the corresponding taxation rules, but during the course of taxplan preparation, may become aware of a rule, thereby learning unconsciously and improving knowledge of taxation rules. Thus, a KBS may promote implicit learning about the problem area because it can intervene to prevent user errors and to suggest choices during the decision-making process.

Cognitive psychology literature has discussed implicit learning in various forms such as implicit memory, unconscious learning, selective versus unselective learning, and incidental versus intentional learning [12,14]. For this study, implicit learning refers to a situation in which people may learn about a complex domain without intending to do so. When asked, they may not even be able to articulate or recall what they learned. Implicit learning occurs without awareness when a person is exposed to problem exemplars, to right and wrong conditions, and negative and positive instances of problems. The user may not even have spent attentional resources for learning [8,13,14,20,34]. A KBS constantly presents the user with suggestions, warnings, and error messages. These situation-specific interventions and recommendations can be construed as problem exemplars. Furthermore, the system may alert users to errors and point to correct solutions. In these situations, users become aware of correct and incorrect solutions to problems, and these experiences could be sources of implicit learning regarding concepts and rules in the domain.

It is generally believed that people can acquire knowledge in a domain even though it is not presented in a declarative or concrete form [31]. A KBS may intervene and highlight an error but not state the correct rule/principle in a declarative form. People can make inferences from these situations and from interactions with their environment and thus develop knowledge structures about a particular domain [4]. Therefore, expectations that interactions with a decision-aiding KBS can help the user implicitly learn about the problem domain are theoretically justified.

Knowledge of software design can be embedded into Computer-Aided Software Engineering (CASE) tools, which can be referred as KBSs [23]. In this study, we examine a KBS that has embedded knowledge on data modeling. During data modeling activity, user requirements are turned into database structures. Data modeling activity is, hence, considered a complex and error-prone decision process, and KBSs can be used to support it [6,7,27,33,42]. A KBS for data modeling could intervene, suggest design choices, recognize errors in the conceptual model, advise users to correct the model, and help them develop better quality data models [6]. Based on the discussion on implicit learning, it is proposed that when users interact with such a KBS, receive advice, and observe their data modeling errors being highlighted, they may implicitly learn some rules, principles, and heuristics on data modeling. Hence, the first hypothesis is stated (in the alternate form):

H1. After interaction with a knowledge-based system for data modeling, users will exhibit improved learning on data modeling knowledge topics when compared with users who interact with a system that is not a knowledgebased system.

As stated earlier, the manner in which a KBS intervenes and provides advice to prevent the user from making erroneous choices is an interface design attribute that is of interest. A KBS could be designed with a restrictive interface that limits the users' choices or guides the user by suggesting a course of action. Experiments conducted to test the effects of the two different interfaces do not indicate a clear superiority of an interface type, but the outcome seems to depend on the specific task context [30,45]. In terms of implicit learning, it is not clear which of these systems will result in greater user learning. The restrictive system will stop the user from using erroneous operators, and the user may use these problem instances of correct choices as cues to infer the correct principles in the domain. The guidance system provides advice on the correct choice, and users may encode their knowledge from this advice. To examine whether implicit learning occurs through either one of the interfaces, these hypotheses were tested:

H1A. Users who interact with a knowledge-based system on data modeling through a restrictive interface will exhibit improved learning outcomes when compared with users who interact with a system that is not a knowledgebased system.

H1B. Users who interact with a knowledge-based system on data modeling through a guidance interface will exhibit improved learning outcomes when compared with users who interact with a system that is not a knowledge-based system.

While implicit learning could lead to greater knowledge in the domain, an interesting question is whether the increased knowledge is of a specific type. Problem-solving knowledge in any domain can be classified as declarative knowledge and procedural knowledge. Declarative knowledge (know-what) refers to the fundamental principles, definitions of concepts, and the relationships between the concepts in a domain. Procedural knowledge (know-how) refers to the knowledge of how to apply principles and concepts during problem-solving [2,12]. Implicit learning could lead to improvements in either declarative or procedural knowledge, or in both. Prior research or theory are not available to guide us to expect a learning effect for a specific type of knowledge. Nevertheless, it would be interesting to discover if subjects experienced more (or less) implicit learning of specific types of knowledge. Therefore, an exploratory question was formulated:

If implicit learning occurs due to interaction with a KBS on data modeling, does it favor a specific knowledge type?

## 3. Methods

## 3.1. Design

Because the study goals were to investigate if an implicit learning effect occurred with the use of a KBS, it was desirable to control extraneous variables that affect learning. Therefore, laboratory experimentation method with a repeated measures design was chosen as a suitable approach that provided a way to tightly control the effect of extraneous variables [11]. A test was used to evaluate initial data modeling knowledge of users before they interacted with the system (pre-treatment), and a similar test was used to determine their knowledge of data modeling after they interacted with the system (posttreatment). Differences between post-treatment and pretreatment knowledge tests indicate the amount of implicit learning, if any, that occurred due to interaction with the system. When these learning outcomes are compared across systems that the user interacted with (with a KBS or without a KBS), the results indicate whether interactions with a KBS lead to improved learning outcomes.

## 3.2. Knowledge-based system

A KBS that helps users in problem-solving activities must embed domain knowledge, and that knowledge must be accessible unobtrusively. It should help users with suggestions and prevent them from making errors. The system should provide feedback on user actions and must supplement users' memory with externalized problem-solving models [32]. CODASYS, a KBS in the domain of database design, was built with these prescriptions [6]. This system provides help to novice designers in data modeling tasks and prevents them from making errors. Two implementation versions of the KBS were used, one with a restrictive interface and the other with a guidance interface. A database design-related rule that states “If there are no key attributes then an entity cannot be defined” can be implemented in two ways. With a restrictive interface approach, the system will prevent the user from storing an entity if a key attribute is not assigned to it. A KBS using a guidance interface approach will remind the user to define the key attribute for the entity, i.e., provide guidance. Thus, the same knowledge rule was implemented in two different ways in the two versions of the system. Differences in the two interfaces are listed in Appendix B. In addition, a version that had the same look and feel of the knowledge-based system, but without any embedded knowledge, was developed. This is referred to as a non-knowledge-based system, and it served as a control system in that it did not intervene, nor provide advice, nor prevent the user from making errors. The control version could be likened to a drawing tool that can help the user create a data model, but it did not have the additional functionalities that could steer the novice designer toward better design choices and prevent errors [6].

## 3.3. Subjects

The KBS was designed to help novice database designers, so undergraduate business students enrolled in a database management course in a large U.S. public university were invited to participate. If participants had been informed before the study that this was a test on learning, the results might have been confounded, so participants were told instead that the exercise would evaluate the ease of use of a new software tool for database design. After the experiment participants were debriefed and told that their extent of learning was also calculated.

## 3.4. Dependent variable measures

The purpose of the study was to find if any improvement in data modeling knowledge can be attributed to implicit learning that might occur as a result of interaction with the system. Knowledge that is learned implicitly cannot be verbalized: people may not even know what they have learned, or even that they have acquired additional knowledge [14]. In other words, learning cannot be measured by asking subjects to write what they learned, or through other “open-ended” questions that might cue them to think that they are expected to show some new knowledge. But learning can be tapped by posing different problem-solving questions/scenarios and evaluating responses [12]. Hence, it was decided to have participants answer structured queries such as multiplechoice questions. A list of multiple-choice and fill-in-theblank questions on data modeling was created to test data modeling knowledge. Participants answered this test, shown in Appendix B, before they interacted with the system (pre-treatment) and also after they interacted with the system (post-treatment). Because they did not consult with any person or book but interacted solely with the system, any changes in their responses–i.e., their knowledge test scores–could be attributed to learning that occurred due to interaction with the system. Therefore, the difference in scores between the post-treatment (postinteraction) and pre-treatment (pre-interaction) was used to measure implicit learning. The test comprised twenty questions. Each question was scored 0 for an incorrect answer or 1 for a correct answer. For two questions (15 and 20), fractional points were awarded depending on the accuracy of answers. A grader blind to the conditions graded the tests.

## 3.5. Pilot study results

Prior to the main experiment, a pilot study was conducted with 12 volunteers equally divided between guidance and restrictive systems. An overall learning effect was revealed when the post-treatment scores were compared with pre-treatment scores (t-statistic = −2.76, $p { = } 0 . 0 0 5 7 )$ . Feedback from participants in the pilot test was used to improve the wording of questions in the knowledge test.

## 3.6. Experimental procedures

The invitation to participate in the study was extended to all undergraduate students in a database management class. Volunteers were assigned to one of four sessions (each lasting for no more than 2 h). These experimental sessions were conducted in a computer laboratory. Seating was arranged in such a way that users could not peer at others' tests or terminals. Participants received class credit. Non-participants could get credit through other assignments.

When participants arrived for their experimental session, they were welcomed and assigned to one of three possibilities: a control system, a KBS with a restrictive interface, or a KBS with a guidance interface. Participants completed a background questionnaire about their experiences with database applications, knowledge of data modeling, and demographic information. Their perception of prior knowledge on data modeling was captured on a Likert scale with anchors of 1 (very poor) and 5 (very high). They were also asked about the number of classes in which they had used database software. Next, they completed the pretreatment knowledge test (Appendix B). Then, for about 10 min, they were trained on the software and allowed to ask questions about the system. Using the KBS, they were then asked to solve a fairly complex data modeling task, shown in Appendix C. During this period they received no help: they interacted on their own with the system and developed the data model. After they completed the data modeling task, they answered the post-treatment knowledge test, which repeated the same questions asked in the pre-treatment knowledge test. While answering the questions the second time, participants could not use books, consult the system, or access their answers from the first test. They then answered a short questionnaire that contained a few open-ended questions about their perceptions of the system. These open-ended questions were not central to this study; their purpose was to gather feedback for improving the system for use in other research studies. Subjects were then thanked and dismissed.

## 4. Results

Fifty-two participants attended the sessions, and their demographic information is shown in Table 1.

As shown in Table 2, no significant differences were seen in demographic characteristics pertaining to age, years of computer experience, or pre-treatment scores on the data modeling knowledge test among subjects who used the control, the guided, or restrictive versions of the KBS. Even though pre-treatment knowledge tests did not show significant differences in the three groups, some differences were seen in the self-reported data modeling knowledge and number of classes on database software, so these two measures were later used as covariates in data analysis.

Table 1  
Demographic information

<table><tr><td colspan="2">Subject characteristics</td></tr><tr><td>Gender</td><td>43 males and 9 femalesa</td></tr><tr><td>Average age</td><td>22.3</td></tr><tr><td>Average number of years of computer experience</td><td>2.9</td></tr><tr><td>Average number of classes with hands-on computer work</td><td>4.9</td></tr><tr><td>Average number of classes that used database software</td><td>2.3</td></tr><tr><td>Average of self-reported rating of data modeling knowledge (1=very poor, 2=poor, 3=adequate, 4=high, 5=very high)</td><td>3.0</td></tr></table>

<sup>a</sup> The number of participants reflected the class composition, which was dominated by male students.

The summary statistics on the average learning outcomes in each condition are shown in Table 3. Users of the KBS, restrictive or guided, exhibited a positive learning outcome. The learning outcome was calculated in a conservative manner by considering only those questions that subjects answered in both the pre- and post-test condition. It was observed that a few subjects omitted one or two questions on the post-test but answered them on the pre-test. Similarly, a few subjects answered one or two questions in the pre-test but omitted them in the post-test. It can be argued that the former situation indicated an increase in knowledge, but it is difficult to argue logically that the latter situation indicated a learning effect. Therefore, it was decided that questions with missing answers would not be included in the calculation of changes in knowledge, i.e., as indicators of learning effect.

Analysis of covariance procedure was conducted using self-reported data modeling knowledge and number of classes that used database software as covariates. The results of the analysis of covariance procedure are shown in Table 4.

Table 2  
Differences in subjects' backgrounds

<table><tr><td rowspan="2">Characteristics</td><td colspan="3">System type</td><td rowspan="2">Significance</td></tr><tr><td>Control</td><td>Guidance</td><td>Restrictive</td></tr><tr><td>Age</td><td>21.8</td><td>23.6</td><td>21.6</td><td> $F=1.28, p=0.286$ </td></tr><tr><td>Years of computer experience</td><td>3.0</td><td>2.8</td><td>2.9</td><td> $F=1.54, p=0.224$ </td></tr><tr><td>Number of computer classes</td><td>4.8</td><td>5.3</td><td>4.6</td><td> $F=1.06, p=0.353$ </td></tr><tr><td>Number of classes that used database software</td><td>2.5</td><td>2.5</td><td>1.8</td><td> $F=2.54, p=0.089$ </td></tr><tr><td>Self-reported data modeling knowledge</td><td>2.9</td><td>2.9</td><td>3.2</td><td> $F=2.72, p=0.076$ </td></tr><tr><td>Scores on pre-treatment task</td><td>12.30</td><td>12.90</td><td>12.55</td><td> $F=0.53, p=0.590$ </td></tr></table>

Table 3  
Learning outcome

<table><tr><td>Group</td><td>Number of subjects</td><td>Pre-treatment knowledge test</td><td>Post-treatment knowledge test</td><td>Learning outcomea</td></tr><tr><td>Control</td><td>12</td><td>12.76</td><td>12.07</td><td>-0.58</td></tr><tr><td>Guidance</td><td>21</td><td>12.53</td><td>14.39</td><td>1.38</td></tr><tr><td>Restrictive</td><td>19</td><td>13.32</td><td>14.50</td><td>1.16</td></tr></table>

<sup>a</sup> The learning outcome (column 5) is calculated by considering only those questions that the subjects answered in both pre- and post-tests. The scores reported as the pre- and post-treatment scores (columns 3 and 4) are scores of each condition considering all the questions in the test.

It can be seen that prior data modeling knowledge was a significant covariate, but after these effects were removed, the groups showed significant learning differences due to the system (p b .01). Therefore, evidence supports the first hypothesis: “After interaction with a knowledge-based system on data modeling, users will exhibit improved learning outcomes when compared with users who interact with a system that is not a knowledgebased system.” (Note: the task grades–i.e., the quality of the data model–developed by the participants when they interacted with the system were graded, and these did not correlate with the learning outcome, p= 0.354.)

Based on the above significant omnibus test, it was important to follow up and identify where the differences occurred among the three conditions (control, restrictive, and guidance). Therefore, each condition was compared against the others using orthogonal contrasts analysis, and the results are shown in Table 5.

It can be seen that the learning effects of the knowledge-based system, whether with a restrictive interface or a guidance interface, are significantly different from those of the control system. Hence, support is gathered for hypothesis H1A, which states: “Users who interact with a knowledge-based system on data modeling through a restrictive interface will exhibit improved learning outcomes when compared with users who interact with a system that is not a knowledge-based system.” Likewise, for H1B, which states: “Users who interact with a knowledge-based system on data modeling through a guidance interface will exhibit improved learning outcomes when compared with users who interact with a system that is not a knowledge-based system.” But no differences in the learning effects are seen between using a guidance interface and a restrictive interface.

Table 4  
Results of analysis of covariance

<table><tr><td>Source</td><td>Significance</td></tr><tr><td>Model</td><td>F=3.46, p=0.0147</td></tr><tr><td>System type</td><td>F=5.01, p=0.0107</td></tr><tr><td>Data modeling knowledge</td><td>F=3.73, p=0.0593</td></tr><tr><td>Number of classes that used database software</td><td>F=0.10, p=0.7483</td></tr></table>

Table 5  
Results of contrasts

<table><tr><td>Contrast</td><td>Significance</td></tr><tr><td>Control vs. KBS</td><td>F=8.26, p=0.0060</td></tr><tr><td>Control vs. restrictive KBS</td><td>F=4.54, p=0.0383</td></tr><tr><td>Control vs. guidance KBS</td><td>F=9.22, p=0.0039</td></tr><tr><td>Guidance vs. restrictive</td><td>F=0.76, p=0.3884</td></tr></table>

To explore whether the knowledge that was implicitly acquired exhibited a specific pattern, the 20 questions that were listed on the knowledge test were classified as testing declarative knowledge or procedural knowledge. Fifteen of the twenty questions were classified as declarative knowledge and five (questions 15, 16, 18, 19, and 20) were classified as procedural knowledge. Controlling for learner, the average learning effects for each question were calculated, revealing that the average learning effect was higher for questions labeled procedural. These results indicate that the implicit learning effect is probably stronger in procedural-knowledge questions.

## 5. Discussion

Learning can occur implicitly and explicitly, and typically a stimulus fosters this learning process. This study indicates that users' interaction with a KBS may provide such a stimulus and become a source of unintentional learning about the problem area. Unlike tutoring systems that are specifically designed to explicitly teach users, the system used in this study was a knowledge-based CASE tool whose purpose was to assist users in data modeling tasks. When users applied the tool to their task, they were not explicitly asked to pay attention or recall the content of messages and prompts from the system. Learning outcomes were measured conservatively. Yet, with both versions of the KBS, one restrictive and one guidance interface, users seemed to infer some domain-relevant rules and unconsciously improved their knowledge about data modeling. These results suggest that KBS could be a change agent, not only for improving users' decision making processes, but also for improving users' problem cognition.

Though learning through interaction was higher with the guidance interface was slightly higher than with the restrictive interface, it was not significantly higher. This non-significant difference can perhaps be explained by the fact that implicit learning is fostered when users become aware of problem exemplars. With a restrictive interface, the system intervenes and does not allow users to apply incorrect principles. For example, if a user tries to save an entity without defining a key attribute, the restrictive interface will not allow the user to save the entity, while a guidance system will advise the user to define a key attribute. In both situations, the user becomes more acutely aware of a modeling principle: a critical step in data modeling is that a key attribute must be defined. Hence, for implicit learning purposes, both restrictive and guidance interfaces may be equally useful. These results, though, must be tested several times with more complex tasks and in other contexts.

It was found that implicit learning seems to favor acquisition of procedural knowledge. Findings favoring the learning of procedural knowledge are not surprising given that users learned during problem-solving activities. Unlike declarative knowledge consisting of general facts about the domain, procedural knowledge is very skillbased. Procedural knowledge occurs in executing a skill: learning by doing [5]. In this case, users were involved in a data modeling exercise, and this hands-on activity might have made it easier to learn procedural “know-how” knowledge.

## 5.1. Limitations

The study, like any controlled experiment, has several limitations. First, student participants were used as subjects. But the goal was to focus on learning effects of novice designers and not on the ability of participants to make real-world decisions; therefore, using student subjects is acceptable. In this study, users' interaction with the KBS was limited to one task. The classification of questions into procedural and declarative types may not be precise, but this was done to explore the type of knowledge acquired by implicit learning. Finally, the study was specific to KBS for data modeling. Other contexts must be considered before generalizing about other types of KBS.

## 5.2. Implications for research and practice

To the best of our knowledge, this study is among the first to highlight the role of KBS as a stimulus for implicit learning, and therefore, it provides many avenues for future research. This research could be extended by determining whether the learning outcome is stable over time. Because student participants were used, it was not possible to conduct a delayed test. Participants could explicitly acquire information on data modeling through access to books and other materials. Therefore, the stability of these learning outcomes could not be tested. Another avenue of future research might have users interact with the KBS for an extended time, i.e., have them conduct several decision-making exercises before the learning outcome is tested. Repeated exposure to problem exemplars provide instances of correct solutions, so one can perhaps expect a stronger learning effect. Another study could test if users are able to transfer their knowledge and apply it to other data modeling situations. In this study, novices who had some knowledge of data modeling were used as subjects, but the extent of learning that can occur with more experienced users must be researched. It is possible that learning will still occur because the comparison with a control system showed that it was the use of a knowledge-based system that helped users learn. With more experienced users, perhaps the knowledge base and tasks must be more complex to observe a learning effect.

From a theoretical perspective, research could proceed on the two dimensions of DSS research that were investigated in this study: the knowledge base and the interface. We used a KBS, and not a generic DSS, because it was felt that it was the problem-specific knowledge base that facilitated the advice giving (guidance) or constraints (restrictive) at appropriate points in the decision process. These appropriately timed interventions could make users aware of problem exemplars and cause them to learn implicitly. Further, the system was designed based on an understanding of how users execute the data modeling process and what errors they typically make, so that interventions were tuned to the specific decision context [6]. Spreadsheets and other non-knowledge-based DSS tools tend to be general purpose systems and do not provide a high level of problem-specific knowledge. Repeated use of these systems, however, could potentially facilitate implicit learning. For example, in a model-based DSS, users can see a list of modeling methods, or see the results of sensitivity analysis, and can become more aware of various modeling techniques and benefits. But the issue of whether a significant level of learning can occur with these DSS tools must be investigated systematically. In information systems research, the relationship between DSS use and decision performance has been substantially researched, but the relationship between DSS use and user learning has received far less attention. This study suggests that research must be conducted to identify even more benefits of using DSS/KBS than improvements in decision outcomes alone.

The interface is another dimension where more theoretically grounded research can be conducted. The notion of decisional guidance and restrictiveness was introduced as a design variable that could influence user choices and their decision processes, within which a range of design attributes could be tested [37]. In this study, an interface providing guidance was compared with a restrictive interface, and the interface with guidance did not make a significant difference in the extent of learning. But future research could investigate whether more directed guidance that clearly tells the user how to develop a data model may provide a stronger learning effect. In training research, less restrictive systems are said to foster more exploratory learning, while more restrictive systems foster more structured learning. But these are fairly explicit types of learning. Therefore, future research can investigate and contrast the extent of learning with the different interfaces and the different types of learning (explicit versus implicit). Second, this study did not examine user perceptions of ease-of-use of the system, but prior studies on data modeling have shown that novice users seem to prefer the restrictive system [6]. Research findings indicate some conflicting findings in user preferences for the two interface types [38,46]. Therefore, the issue of performance effects of these different interfaces versus the preferences of users must be investigated more closely. Also, the specific nature of the task must be considered in this analysis because users perhaps think that they know more about display formats and less about data modeling. They may thus prefer more restrictions in data modeling tasks but more choices in display tasks. The study results provide many research directions to pursue at the interface or knowledge level dimensions, or both.

The study has several implications for practice as well. If knowledge-based systems can become a source for learning, then they could be designed to consider more carefully their roles as agents for learning. CASE tools have been investigated and are perceived as providing many benefits to organizations [11,18,23,44]. Their advantages with embedded knowledge and their impact on user learning provide useful information for trainers and developers. Based on these results, CASE tool developers could consider making a learning tool by embedding at least some knowledge that can intervene to prevent users' errors and suggest design solutions.

This is an initial exploratory study, but it has provided some information to build upon and research further. When expert systems were introduced, considerable interest arose in investigating how their decision choices and explanation facilities could become learning stimuli for novice users [17,28]. Unfortunately, interest in this inquiry died, partly because of the need to specifically design and develop expert systems to function as learning tools. This research has shown that special systems need not be designed: KBSs designed for problem solving could incidentally induce unconscious learning. Understanding the role of decision-aiding tools in promoting learning activities in an organization is critical and beneficial [10]. Hence, it is hoped that findings from this study foster more research to fully exploit the potential benefits of knowledge-embedded tools and carefully constructed interfaces.

## Acknowledgements

We thank the reviewers who provided many positive comments to improve the quality of this manuscript.

Appendix A. Some differences among the responses from the two Interfaces

<table><tr><td>The user</td><td>The guidance interface</td><td>The restrictive interface</td></tr><tr><td>Enters the name of a new entity</td><td>Reminds the user to model at least two attributes for an entity, but the user can use that entity in a relationship without assigning attributes to it</td><td>Does not remind the user to assign two attributes, but entities without two attributes cannot be used in relationships</td></tr><tr><td>Saves an entity without specifying its key attribute</td><td>Reminds the user to define key attribute</td><td>Will not save the entity until a key attribute has been defined</td></tr><tr><td>Specifies the key attribute for an entity</td><td>Reminds the user to verify uniqueness of the key attribute</td><td>Asks the user whether the key attribute is unique or not; user answers Yes or No</td></tr><tr><td>Tries to select a non-free entity for a relationship</td><td>Advises the user against use of a non-free entity, but does not prevent user from using it</td><td>Blocks the use of non-free entities by not displaying that entity</td></tr><tr><td>Is using any window within the application</td><td>Allows all controls to be accessed</td><td>Does not allow access to all controls, but only a specific set of controls is enabled at any time, including menu options</td></tr><tr><td>Tries to delete a relationship</td><td>Allows the deletion of any relationship and will free up relevant entities so that they can be used later for more relationships</td><td>Allows deletion of only the most recently modeled relationship</td></tr></table>

Appendix A (<sub>continued</sub>)

<table><tr><td>The user</td><td>The guidance interface</td><td>The restrictive interface</td></tr><tr><td>Tries to modify a relationship</td><td>Allows the user to modify any relationship</td><td>Allows modification of only the most recently modeled relationship</td></tr><tr><td>Attempts to use a sub-set of or super-set of or same set of entities in two relationships</td><td>Advises the user about derived relationship; but does not prevent user from doing so</td><td>Once a relationship has been declared, the same entities cannot participate in another relationship. User will be unable to select them.</td></tr></table>

## Appendix B. Knowledge Test Questions

Note: For the following questions circle the answer that seems closest to the right answer. Write brief explanations wherever required.

Assume you are modeling an entity called “Automobile”. Which of the following items can be an attribute of that entity? If an item cannot be an attribute, specify your reason as to why.

1. Color 2. Red 3. Year 4. Past owners 5. Odometer reading 6. 1992 7. Mustang 8. Make 9. Current owner

10. Can an attribute belong to more than one entity? (a) yes (b) no (c) sometimes, because

11. How many key attributes can an entity have? (a) none necessary (b) at least one (c) at most one (d) exactly one (e) can be any number

12. How many non-key attributes must an entity have? (a) none necessary (b) at least one (c) at most one (d) exactly one (e) can be any number

13. What is the link between the key attribute and a non-key attribute? (a) The key attribute must depend directly on the non-key attribute. (b) The non-key attribute must depend directly on the key attribute. (c) The key attribute may depend indirectly on the non-key attribute. (d) The non-key attribute may depend indirectly on the key attribute.

14. How many entities may participate in a relationship? (a) two only (b) one or two only (c) one, two or three only (d) any number other than zero

15. How would you decide whether X is going to be an entity or not? (a) Check whether there can be instances of that entity. (b) Check if there is a unique number or id for that entity. (c) Check if there are attributes that seem to describe it. (d) Other reason: specify

16. Consider the Course entity with 4 attributes. Course(CourseNo, Title, InstructorID, Instructor-Name) You find that there is partial dependency between InstructorName and CourseNo. Which of the following will be an appropriate action to take? (a) Leave the attributes as they are. (b) Remove the InstructorName and InstructorID and model them as separate entity. (c) Similar to solution as in (b), but remove only instructor attribute. (d) I don't know. (e) Other: specify

17. Can there be two entities with the same exact name? (a) yes (b) no

18. When there is a one–many relationship and a many–many relationship to be modeled, which relationship would you model first? (a) one–many (b) many–many (c) do not know which one.

## Appendix C. Task Completed Through the System

Super Systems Inc.

The people at Super Systems Inc. (SSI) are in the business of developing software for large companies. They have a number of projects underway. Each project has a unique name and is for a specific company. SSI may have many projects from the same company. Each project has a deadline before which it has to be completed. They wish to keep track of the company details such as company name, contact person, and contact phone number. On each project a number of skilled programmers are employed. Each project may involve work on different platforms such as Vax, AS/400, Mac etc. A programmer may work on many platforms, but for a given project, a programmer works only one platform. Information about each platform such as name, operating system, date of last upgrade, and name of manufacturer are to be stored in the database. It is necessary to store programmer information such as name and wage rate also. Each programmer has many language skills like C, C+, SmallTalk, etc. SSI wishes to code each language skill (with a unique code) and some description. Develop the Entity Relationship model for this case. Make any assumptions necessary.

## References

[1] M. Alavi, D. Leidner, Knowledge management systems: issues, challenges, and benefits, Communications of the Association for Information Systems 1 (7) (1999) 1–36.

[2] J.R. Anderson, A theory of the origins of human knowledge, Artificial Intelligence 40 (1) (1989) 313–351.

[3] J.R. Anderson, C.F. Bole, B.J. Reiser, Intelligent tutoring systems, Science 22 (8) (1985) 456–462.

[4] J.R. Anderson, J.M. Finchman, Acquisition of skills from examples, Journal of Experimental Psychology. Learning, Memory and Cognition 20 (6) (1994) 1322–1340.

[5] J.R. Anderson, C. Lebiere, Learning, in: J.R. Anderson, C. Lebiere (Eds.), Atomic Components of Thought, Lea Publishing, New York, 1998.

[6] S.R. Antony, D. Batra, CODASYS: a consulting tool for novice database designers, Database. Advances in Information Systems 33 (3) (2002) 54–69.

[7] C. Batini, S. Ceri, S.B. Navathe, Conceptual Database Design: An Entity-Relationship Approach, Benjamin Cummings, Red wood City, California, 1992.

[8] D.C. Berry, D.E. BroadBent, On the relationship between task performance and associated verbalizable knowledge, Quarterly Journal of Experimental Psychology 36 (A) (1984) 209–231.

[9] D.C. Berry, Z. Dienes, Implicit Learning: Theoretical and Empirical Issues, Lawrence Erlbaum Associates, East Sussex, UK, 1993.

[10] G.D. Bhatt, J. Zaveri, The enabling role of decision support systems in organizational learning, Decision Support Systems 32 (3) (2002) 297–309.

[11] G.M. Breakwell, S. Hammond, C. Fife-Shaw, Research Methods in Psychology, Sage Publications, London, 1993.

[12] J.E.H. Bright, A.M. Burton, Ringing in the changes: where abstraction occurs in implicit learning, European Journal of Cognitive Psychology 10 (2) (1998) 113–130.

[13] T. Curran, S.W. Keel, Attentional and non-attentional forms of sequence learning, Journal of Experimental Psychology. Learning, Memory and Cognition 19 (1) (1993) 189–202.

[14] R.P. DeShon, R.A. Alexander, Goal setting effects on implicit and explicit learning of complex tasks, Organizational Behavior and Human Decision Processes 65 (1) (1996) 18–36.

[15] J.S. Dhaliwal, I. Benbasat, The use and effects of knowledge-based system explanations: theoretical foundations and a framework for empirical evaluation, Information Systems Research 7 (3) (1996) 342–362.

[16] J. Elam, G. Huber, M. Hurt, An examination of the DSS literature (1975–1985) in decision support systems, in: E.R. McLean, H.G. Sol (Eds.), A Decade in Perspective, Proceedings of the IFIP Conference, Elsevier Science Publishers, New York, 1996.

[17] J. Fedorowicz, E. Oz, P.D. Berger, A learning curve analysis of expert system use, Decision Sciences 23 (4) (1992) 797–818.

[18] P.N. Finlay, A.C. Mitchell, Perceptions on the benefits from introduction of CASE: an empirical study, MIS Quarterly 18 (4) (1994) 353–370.

[19] M. Goul, J.C. Henderson, F.M. Tonge, The emergence of artificial intelligence as a reference discipline for decision support research, Decision Sciences 23 (6) (1992) 1263–1274.

[20] K.J. Holyoak, B.A. Spellman, Thinking, Annual Review of Psychology 44 (2) (1993) 265–315.

[21] C.W. Holsapple, Handbook on Knowledge Management, Springer-Verlag, New York, 2003.

[22] C.W. Holsapple, A.B. Whinston, Decision Support Systems: A Knowledge-Based Approach, West Publishing, St. Paul, MN, 1996.

[23] D. Jankowski, How can CASE help? A look at the feasibility of structured analysis with CASE, Database for Advances in Information Systems 28 (4) (1997) 33–47.

[24] P.G.W. Keen, M.S. Scott-Morton, Decision Support Systems: An Organizational Perspective, Addison-Wesley, Reading, MA, 1978.

[25] S. Kim, B. Arinze, A knowledge-based decision support system for set-up reduction, Decision Sciences 23 (6) (1992) 1389–1407.

[26] M. Limayen, G. DeSanctis, Providing decisional guidance for multi-criteria decision-making in groups, Information Systems Research 11 (4) (2000) 386–401.

[27] A.W. Lo, J. Choobineh, Knowledge-based systems as database design tools: a comparative study, Journal of Database Management 10 (3) (1999) 26–40.

[28] K. Moffitt, An analysis of pedagogical effects of expert system use in the classroom, Decision Sciences 25 (3) (1994) 445–457.

[29] A.R. Montazemi, F. Wang, S.M.K. Nainar, C.K. Bart, On the effectiveness of decision guidance, Decision Support Systems 18 (2) (1996) 181–198.

[30] M. Parikh, B. Fazlollahi, S. Verma, The effectiveness of decisional guidance: an empirical evaluation, Decision Sciences 32 (2) (2001) 303–331.

[31] A.M. Paul, Learning but not trying, Psychology Today 30 (5) (1997) 14.

[32] P.V. Prabhu, G.V. Prabhu, Human error and user interface design, in: M. Helander, T.K. Landauer, P. Prabhu (Eds.), Handbook of Human–Computer Interaction, Elsevier Sciences, New York, 1997.

[33] S. Purao, APSARA: a tool to automate system design via intelligent pattern retrieval and synthesis, Database 29 (4) (1999) 45–47.

[34] A.S. Reber, Implicit Learning and Tacit Knowledge: An Essay in the Cognitive Unconscious, Oxford University Press, Oxford, 1993.

[35] R. Santhanam, J. Elam, A survey of knowledge-based systems research in decision sciences (1980–1995), Journal of Operational Research 49 (5) (1998) 445–457.

[36] R. Sharada, S.H. Barr, J.C. McDonald, Decision support system effectiveness: a review and empirical test, Management Science 34 (1) (1998) 139–149.

[37] M.S. Silver, Decision support systems: directed and non-directed change, Information Systems Research 1 (1) (1990) 47–70.

[38] M.S. Silver, Decisional guidance: broadening the scope in human– computer interaction, in: D. Galletta, P. Zhang (Eds.), Human– Computer Interaction and Management Information Systems, Ad-

vances in Management Information Systems, vol. 4, M.E. Sharpe, Armonk, NY, 2006.

[39] M.S. Silver, Decisional guidance for computer-based decision support, MIS Quarterly 15 (1) (1991) 105–122.

[40] M.S. Silver, Systems that Support Decision Makers: Description and Analysis, John Wiley, Chichester, England, 1991.

[41] D.T. Singh, Incorporating cognitive aids into decision support systems: the case of the strategy execution progress, Decision Support Systems 24 (2) (1998) 145–163.

[42] V.C. Storey, R.C. Goldstein, Knowledge-based approaches to database design, MIS Quarterly 17 (1) (1993) 25–46.

[43] P. Todd, I. Benbasat, An experimental investigation of the impact of computer-based decision aids on decision-making strategies, Information Systems Research 2 (2) (1991) 87–115.

[44] I. Vessey, S.L. Jarvenpaa, Evaluation of vendor products: case tools as methodology companions, Communications of the ACM 35 (4) (1992) 90–105.

[45] B.C. Wheeler, J.S. Valacich, Facilitation, GSS, and training as sources of process restrictiveness and guidance for structured group decision-making: an empirical assessment, Information Systems Research 7 (4) (1996) 429–450.

[46] E.V. Wilson, I. Zigurs, Decisional guidance and end-user display choices, Information and Organization 9 (1) (1999) 49–75.

[47] M.K. Wong, J.A. Monaco, Expert system applications in business: a preview and analysis of the literature (1977–1993), Information and Management 29 (1) (1995) 141–152.

Dr. Solomon Antony is an Assistant Professor at Murray State University. His publications have appeared in Data Base, International Journal of Human Computer Studies, European Journal of Information Systems, Decision Support Systems and others. His research interests are in problem solving, data modeling, and knowledge-based systems.

Dr. Radhika Santhanam is a Gatton Endowed Research Professor of Information Systems at the University of Kentucky. Her research focus is on understanding human–computer interaction issues as it relates to the design and use of information systems. Her research findings have been published in variety of journals, including MIS Quarterly, Information Systems Research, Journal of Management Information Systems, Decision Support Systems, International Journal of Human– Computer Studies, Information and Organization, Information Technology and Management, Computers and Operations Research, and European Journal of Operational Research, among others. Some of her research projects have been funded by external agencies. She currently serves on the editorial board of MIS Quarterly and Decision Support Systems. She served as the track chair for the International Conference on Information Systems–2004, and the program co-chair for Informs Conference on Information Systems–2003, and the Americas Conference on Information Systems–2005.
