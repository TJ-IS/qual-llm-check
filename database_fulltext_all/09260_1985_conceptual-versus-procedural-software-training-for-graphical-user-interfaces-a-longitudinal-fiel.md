---
otero_id: 9260
otero_key: "64DX6X2W"
title: "Conceptual Versus Procedural Software Training for Graphical User Interfaces: A Longitudinal Field Experiment"
authors: "Lorne Olfman; Munir Mandviwalla"
year: "1985"
journal: "MIS Quarterly"
doi: "10.2307/249522"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Conceptual Versus Procedural Software Training for Graphical User Interfaces: A Longitudinal Field Experiment

By: Lorne Olfman
Programs in Information Science
Claremont Graduate School
Claremont, California 91711
U.S.A.
olfmanl@cgsvax.claremont.edu

Munir Mandviwalla
Computer and Information Sciences
Temple University
Philadelphia, Pennsylvania 19122
U.S.A.
mandviwm@astro.ocis.temple.edu

## Abstract

Graphical user interfaces (GUIs) are rapidly becoming ubiquitous in organizations. Most of what we know about software training comes from studies of command-line interfaces. This paper compares concept-based versus procedure-based content of training materials. Concept-based materials define the nature and associations of the objects in the interface, while procedure-based materials define how specific tasks are carried out. This comparison was done using a field experiment. Eighty-two volunteers participated in a three-week Windows training program and completed a follow-up questionnaire seven months later. The results show that the amount learned in such sessions is a function of neither concept-based nor procedure-based training. GUI training should provide both kinds of information because trainees need to learn both. In addition, trainers should be aware of an apparent early plateau in learning the Windows GUI.

Keywords: User training, user behavior, end users, direct manipulation, graphical user interface, computer literacy, longitudinal study

ISRL Categories: AI0113, FB1001, FD06, GB03, GB0404, HC0104, HD0108, IA02

## Introduction

Software trainers who design training materials for graphical user interfaces (GUIs) may not create the most effective materials if they use methods designed for command-line interfaces. GUIs are different from traditional command-line or text-based interfaces (Hutchins, et al., 1985). For example, a training program for a command-line interface like DOS might aim to teach commands such as COPY by focusing on the syntax (e.g., source file to be copied comes first, destination of the file comes second). For a GUI, like Windows, there is no equivalent syntax since copying a file can be accomplished by dragging one object to another—the source and destination are embedded in the user's physiological view of the interface.

While the improvement of end-user training is the overall goal of software training research, research to date has focused its attention on two broad areas:

1. Studies that investigate the method for presenting training material—for example, comparisons of exploratory and structured approaches (Carroll, 1990).

2. Studies that investigate the content of the training material—for example, investigation into the types of training information and comparisons of conceptual models (Sein and Bostrom, 1989).

The majority of published studies have stressed the first area of research by assuming that the key issue related to improving software training is the method of presentation. Most studies assume that the target software is an unimportant variable. One explanation for this assumption is that command-line interfaces present minimal feedback to the user during a training session. Consequently, it is safe to assume that the nature of a typical training session for command-line software is unidirectional; training materials provide information to the trainee, and the trainee uses this information to operate the software. However, GUIs are relatively rich in the amount and type of information embedded in the interface. Moreover, this information interacts with the information provided by the training materials. Therefore, although the method of presentation is important, it is equally important to consider the content of the training material in relation to the information embedded in the GUI.

With respect to the content of training materials for command-line interfaces, Reder, et al. (1986) found that procedural information—information about how to do things—was more effective than conceptual information—abstract or generalized information—because subjects seemed to require specific syntactic details to complete tasks. Such findings may not apply for GUIs because the objects in the interface already provide some procedural information. For example, procedures may be inferred from the appearance and behavior of objects and changes in the display.

This paper examines the relative value of different types of software training content for a GUI (viz., Windows) through a longitudinal field experiment. The goal of the research is twofold: (1) to improve and reduce the cost of GUI software training by pinpointing the most important information needed by a GUI user; and (2) to inform training research by investigating the interaction of information embedded in the GUI with information provided by the training materials. The following sections analyze the content of training materials and outline the reasons why they may lead to different outcomes for GUIs. They then describe the method used to carry out the field experiment. Finally, they summarize and discuss our results.

## Previous Research

Training materials can contain several types of information. These include: information about what the software is and what it can do, how to operate the software, what to do when problems occur, and how the software fits into the user's environment. When this information is successfully transferred to the user it becomes part of the user's knowledge base. The information presented during training is referred to as the "content of the training materials" or simply as "content." The term "knowledge" refers to training information that has become part of the user's knowledge base.

Two kinds of content are defined: concepts and procedures. Concepts are fact-based. They are abstractions or generalizations about the factual way in which the interface operates. They include the description of the objects in the interface and the relationships between objects. Procedures are task-based. They are specifications for carrying out specific tasks.

There are several definitions of the kinds of knowledge that are learned through training (see Table 1). Most definitions focus on variations of conceptual and procedural knowledge. Hereafter, the terms conceptual and procedural knowledge are used to encompass the range of definitions. $^{2}$

Importance of procedures. Anderson (1982) describes a model of skill acquisition that specifies how individuals obtain conceptual knowledge by observing procedures and then infer additional procedural knowledge from this conceptual knowledge base. Wright (1988) suggests that initially it is procedures that most people want to master, rather than an understanding of the system. In part, this is a motivational argument that stems from the findings that learners want to engage meaningful tasks (e.g., Carroll, 1990). Perrig and Kintsch (1985) too, suggest that procedures may be easier to recall than concepts.

Importance of concepts. Mayer (1989) presents evidence that concept models, presented at the outset of training, benefit novice learners by facilitating the extension of learned material to “far transfer problems” (i.e., problems not addressed during training). In effect, they help the user develop a more flexible mental model. The mental model can then be used to develop procedural skills (Glaser, 1990).

Table 1. Definitions of Training-Related Knowledge

<table><tr><td rowspan="2">Author(s)</td><td colspan="2">Conceptual</td><td colspan="2">Procedural</td></tr><tr><td>Term</td><td>Definition</td><td>Term</td><td>Definition</td></tr><tr><td>Anderson (1982)</td><td>Declarative</td><td>knowledge of facts</td><td>Procedural</td><td>knowledge of how to do things .</td></tr><tr><td>Kieras &amp; Polson (1985)</td><td>How-it-works</td><td>A hierarchy of concept explanations</td><td>How-to-do-it</td><td>knowledge of various tasks</td></tr><tr><td>Hiebert &amp; Lefevre (1987)</td><td>Conceptual</td><td>knowledge of relationships between pieces of information</td><td>Procedural</td><td>a formal language and rules for completing tasks</td></tr><tr><td>Charney &amp; Reder (1987)</td><td>Conceptual + Usage</td><td>knowing what procedures exist and circumstances for applying procedures</td><td>Procedural</td><td>knowing how to carry out procedures</td></tr></table>

Researchers tend to agree that some combination of concepts and procedures is needed (Glaser, 1990; Hiebert and Lefevre, 1986). It is the relative quantity and sequencing of the two kinds of content that has not been fully established. Santhanam and Sein (1993) studied sequencing of training content for a command-line interface (VMS-mail). After subjects were introduced to the software using either procedures or concepts as a metaphor, they received detailed training on procedures. There was no difference in the amount of learning during training regardless of the type of content presented at the outset of training. With respect to quantity of content, evidence from Reder, et al. (1986) indicates that procedure content should be greater than concept content for training of command-line interfaces.

While none of these issues have been examined in the GUI context, an argument can be made for emphasizing concepts over procedures for a GUI based on the work of Kitajima and Polson (1992). They describe and validate a computational model of the skilled use of a GUI. They define five kinds of knowledge for interacting with the display. Three of these knowledge types have to do with how the user interprets the display and sets goals for interacting with the system, and, thus, are not discussed further in this paper because these behaviors are dependent on individual characteristics that cannot be easily influenced by software training. The other two kinds, general and action-plan knowledge, are relevant for training. General knowledge is knowledge about objects and their attributes and functions. Action-plan knowledge represents the relations between an action and its response. According to Kitajima and Polson (1992), procedural knowledge is not stored sequences of procedures because the theoretical frameworks for human-computer interaction “assume that a sequence of user actions is not pre-planned” (p. 241). Procedural knowledge may, in fact, be derived from understanding the definition and behavior of concepts.

For the purposes of this study, therefore, we propose that emphasizing concepts over procedures in GUI training should lead to better learning of the target software since the key to procedural knowledge is conceptual knowledge.

However, this effect is unlikely to be influential by the end of a single short training session. Charney and Reder (1986) hypothesize that the knowledge gained from learning a software package is most likely to be clearly visible after a delay as opposed to right after the training session. They found, for example, that learning a command-line interface occurred after a two-day delay between the training and the testing.

Moreover, the same kind of delayed effect may take place when learning a GUI. The theoretical basis for this argument can be found in research on memory and recency effects (see, for instance, Schwartz and Reisberg, 1991). Short-term recall tends to favor the most recent information presented. However, recall of information over a longer term depends on the strength of the neural connections underlying the information. This means that in a test taken immediately after a training session, learners should be able to access their memory for information presented during the training session regardless of the kind of content emphasis. However, over time, in line with Kitajima and Polson's (1992) view, procedural information will not yet have been converted into stored procedural knowledge.

Therefore, for the purposes of this study, we propose that an emphasis of concepts over procedures will not show learning differences at the end of an initial single training session; however, over time, the postulated differences between the approaches will appear.

A goal of this study is to find ways to improve and reduce the cost of GUI training. An important factor in this context is the effectiveness of training materials. When training materials are effective and there are no other obstacles, the learning gained from training should lead to higher use of the software on the job. Previous research has looked at the connection between facilitating conditions in the environment (such as the availability of technical support, training, and access to computing resources) and increased usage (Thompson, et al., 1991), but the evidence regarding the importance of facilitating conditions is mixed. Thompson, et al. (1991) found a small negative relationship between facilitating conditions operationalized as availability of technical support to usage. However, they question their results and those of other studies because they believe that facilitating conditions should have been operationalized with additional measures such as ease of purchasing upgrades or accessibility of resources. Another potential measure that can be part of the overall facilitation construct is the effectiveness of software training. The ultimate test of learning is not how well a learner does on a test or whether the training is available, but whether the gained knowledge leads to real world use. Since utilization per se is not the focus of this study, our measurement efforts are limited to our main goal—testing the effectiveness of our manipulations. We propose that emphasizing concepts over procedures in GUI training will be more effective in terms of increasing learning. It should be recognized though that usage is not simply explainable by training effects (Olfman and Bostrom, 1991).

Nevertheless, it is logically consistent to propose that an emphasis of concepts over procedures for GUI trainees will lead to higher usage after training.

## Method

## Research Design

In order to test the above propositions, we designed a field experiment to compare the impacts of emphasizing either concepts or procedures during a multi-week training program. A field experiment was selected because we wanted to assess these training approaches using subjects who would have to transfer their learning to their job situation. Clearly, a study that is longitudinal and uses subjects who are engaged in real world working environments is difficult to control. However, we felt that these design characteristics would allow us to fully test our propositions. Moreover, the results of such a study would have good external validity and generalizability.

The longitudinal design served two purposes. First, we wanted to ensure that delayed learning effects would be captured. Second, we wanted to provide trainees with time between the sessions to practice what they learned on the job.

A number of control variables were used to increase internal validity. These variables were selected in accordance with the research framework developed by Bostrom, et al., (1988; 1990). The framework identifies the key variables in software training, as well as the interactions between these variables. It isolates three groups of variables that are inputs to the training process: the software to be learned (target software), the training environment (materials, methods, and support), and the trainee (individual differences). These inputs directly affect the development of the trainee's mental model of the target software, leading to two separate (but possibly related) outcomes. One outcome is understanding, and the other is motivation to use the software.

Our experiment focuses on how different training environments (i.e., concept-based versus procedure-based approaches) influence understanding of the target software (i.e., Windows; an operating environment with a graphical user interface), while controlling for individual differences of the trainees.

The research design is shown in Figure 1. $^{3}$ The O's in Figure 1 represent the questionnaires and tests used to measure control and dependent variables. The X's represent one training method and the Y's the other. The subscripts indicate the $ith$ observation or training session, respectively.

<table><tr><td>Before</td><td colspan="3">Week 1</td><td colspan="3">Week 2</td><td>Week 3</td><td colspan="2">Week 4</td><td>After</td></tr><tr><td> $O_{1}$ </td><td> $O_{2}$ </td><td> $X_{1}$ </td><td> $O_{3}$ </td><td> $O_{4}$ </td><td> $X_{2}$ </td><td> $O_{5}$ </td><td> $X_{3}$ </td><td> $X_{4}$ </td><td> $O_{6}$ </td><td> $O_{7}$ </td></tr><tr><td> $O_{1}$ </td><td> $O_{2}$ </td><td> $Y_{1}$ </td><td> $O_{3}$ </td><td> $O_{4}$ </td><td> $Y_{2}$ </td><td> $O_{5}$ </td><td> $Y_{3}$ </td><td> $Y_{4}$ </td><td> $O_{6}$ </td><td> $O_{7}$ </td></tr><tr><td colspan="11">where  $O_{i}$  = questionnaires and tests at different points in time $X_{i}$  = concept-based training sessions $Y_{i}$  = procedure-based training sessions</td></tr></table>

Figure 1. Research Design

## Hypotheses

total scores that the trainees obtained on the various tests (for a definition of each test see the "Dependent Measures" section below). Specific directional outcomes for subtotal scores were not hypothesized, but post hoc analyses were planned to gain additional information about the nature of any differences that might occur between the two training methods.

Research hypotheses (except H5, which is based on a post-training questionnaire) were based on

The study was conducted in three segments. Before training, subjects were recruited and completed a background questionnaire. Then, four one-hour sessions were offered over a three-week period, with trainees experiencing one of the two training approaches throughout. A follow-up survey was conducted seven months after training was completed. Details of the instruments and the procedures involved in collecting data for the study are outlined in the following sections.

Proposition 1. Concept-based and procedure-based approaches are equivalent right after a training session for a GUI.

H1: The mean scores on the post-test given in week 1 ( $O_{3}$ ) will be equal for trainees who received either concept-based ( $X_{1}$ ) or procedure-based ( $Y_{1}$ ) training when controlling for the scores on the pretest given in week 1 ( $O_{2}$ ).

H2: The mean scores on the post-test given at the end of the training session in week 2 ( $O_{5}$ ) will be equal for trainees who received either concept-based ( $X_{2}$ ) or procedure-based ( $Y_{2}$ ) training when controlling for the scores on the pretest given in week 2 ( $O_{4}$ ). $^{4}$

Proposition 2. Concept-based training will produce more effective learning over time when compared with procedure-based training for a GUI.

H3: The mean scores on the pretest given in week 2 (O $_{4}$ ) will be higher for trainees who received concept-based training in week 1 (X $_{1}$ ) than for trainees who received procedure-based training in week 1 (Y $_{1}$ )

when controlling for scores on the post-test completed in week 1 ( $O_{3}$ ).

H4: The mean scores on the integrative test given during the training session in week 4 ( $O_{6}$ ) will be higher for trainees who received concept-based training throughout than for trainees who received procedure-based training throughout when controlling for scores on the pretest completed in week 1 ( $O_{2}$ ).

Proposition 3. Concept-based training will lead to higher usage on the job compared to procedure-based training.

H5: More trainees who received concept-based training than who received procedure-based training will report using the software after training ( $O_{7}$ ).

## Subjects

A total of 82 university employees attended at least one of the four training sessions. The 22 men and 60 women, which included faculty and staff, were all volunteers. Seventy-seven attended the first week of sessions, 68 the second week, 50 the third week, and 42 the fourth week.

## Variables and measures

## Control Variables and Measures

Preliminary Questionnaire: The purpose of the preliminary questionnaire was to provide a check of the equivalency of treatment groups on a number of individual difference measures that have been found to affect the outcomes of software training (as per Cook and Campbell's (1979) recommendations). There were four general categories of questionnaire items, as shown in Table 2. The measures were developed by the authors following question formats similar to those used in previous training studies (e.g., Webster and Martocchio, 1992). The preliminary questionnaire is denoted as O $_{1}$ in Figure 1.

Trainer: The research design called for a single, independent trainer who could cover all sessions over a four-week period. After attempts to find a single trainer were unsuccessful, two trainers were hired. Both trainers were male doctoral students and have experience as trainers and teachers of software products. Each taught an equal number of sessions of both types of training approaches. No previous software training research has addressed the impact of the trainer specifically, nor was this the intent of our research. With the two trainers, the design was a fully crossed 2 (type of training) by 2 (trainer) experiment. Since we were not interested in trainer effects, trainer was treated as a control variable.

Target Software: $^{5}$ For this study, we chose Microsoft Windows 3.0 (Microsoft Corporation, 1990), which is a graphical operating environment that runs on IBM-compatible personal computers. This software had just been released and was considered a major innovation for DOS-based personal computers.

## Dependent Measures

The dependent measures included scores on tests that established the trainees' knowledge of Windows and associated applications, and whether the software was used on the job. One measure was developed to acquire preliminary information from the trainee, three measures were designed to test the materials covered in different parts of the longitudinal design, and one measure was developed to acquire follow-up information regarding usage. The preliminary questionnaire has already been described; the remainder of this section describes the other measures.

General Test (O₂, O₃, O₄): The general test included 34 questions with five possible answers: Definitely True, Probably True, No Idea, Probably False, and Definitely False. Rather than giving a straight “true/false” test, we felt that ongoing learning could be more clearly assessed by using a modified version that enabled the trainees to include a measure of confidence in their answers (without asking a separate question about their confidence of each answer). The questions were drawn from three general subject domains and included both recall (i.e., questions about features of the interface: 14 items) and applied items (i.e., questions about interaction with the interface: 20 items). The subject areas were: starting and ending applications, using one application, and using multiple applications. Appendix A shows examples of items from each of the subject domains.

Table 2. Self-Report Preliminary Questionnaire Measures

<table><tr><td>General Category</td><td>Items</td></tr><tr><td>Use of Computers</td><td>Use for input, word processing, otherAccess to hardware and software</td></tr><tr><td>Knowledge of Computers</td><td>Knowledge of the Macintosh, word processing, DOS, Windows, typing, and mousePrevious training and courses</td></tr><tr><td>Attitude to Using Computers</td><td>Reason for attending, general attitude</td></tr><tr><td>Learning Style</td><td>Preferred learning style for software</td></tr></table>

Applications Test (O $_{5}$ ): The applications test contained 34 questions, most of which were directly adapted from the general test but were stated in a specific application-oriented context. While the general test included generic questions about the Windows interface, the applications test contained specific questions about Windows applications (e.g., Paintbrush). $^{6}$ Table 3 shows an item from the general test and its counterpart on the applications test. Note that in this case one form was given as “true,” the other as “false.” This was not always the case, because the truth or falsity of the questions in all tests depended on a random selection process. These questions were also ordered differently than on the general test so as to minimize the potential effects of guessing. Four questions on the applications test were completely different than on the general test so that it contained some new information that had not been tested previously. These dealt with conceptual aspects of the Windows interface. The subject areas for the applications test were: Windows, Write, and Paintbrush.

Integrative Test (O $_{6}$ ): The integrative test contained 14 questions in the same format as the other two tests. Eight of the questions were from previous tests, four were similar to previous questions, and two new questions were added. This test also contained items for evaluating the trainer and the design of the training sessions, intentions of future use, and a summary of outside sources used to learn Windows during the training period. Measures of the trainees' attitudes toward the trainers, the training sessions, and their intention to use the software in the future served as manipulation checks. $^{7}$

Follow-up Questionnaire (O $_{7}$ ): This questionnaire asked whether the trainee had used Windows since the training ended. For those who had not used Windows, there were questions to determine their reason(s), plus a question to determine if these people thought they would attend another training session. For those who had used Windows, there were questions on general usage, the impacts of training on that usage, and whether they would attend additional training.

## Independent Variable

The independent variable is the type of training materials as differentiated by their content. The two content variations used for this study, concept-based and procedure-based, are described in this section. The training materials were designed using an instructional design hierarchical decomposition approach. The target software (i.e., the GUI) determined the material for each condition. The overall design also included choices for the style, medium, and interaction of the training materials (see Appendix B). These components were maintained throughout both training treatments.

Table 3. Examples of Test Items

<table><tr><td>Test</td><td>Item</td><td>Answer</td></tr><tr><td>General</td><td>You select the Cancel button to complete a dialog box</td><td>False—you select the OK button</td></tr><tr><td>Applications</td><td>You select the OK button to complete the Image Attributes dialog box in Paintbrush</td><td>True</td></tr></table>

Concept-Based Content: Concept-based training emphasizes computer semantics by focusing on the high to medium-level objects and their actions (e.g., what is a window). It encompasses a set of instructions to describe and define the components (objects) and possible actions on these components of an interface. Examples of the concept-based approach include: defining the attributes of a window (e.g., it has a menu, scroll bars, etc.), defining the attributes of an icon, and defining the mouse actions used to access these attributes.

To implement the concept-based training approach, we focused on the objects of the software. The objects were decomposed into a hierarchy, and then each object was introduced in turn (see Figure 2). For example, in order to introduce Windows, the components of the Windows interface were decomposed into the desktop, the application, and the document. Information was provided about the desktop first. The objects at the top of the desktop hierarchy are the mouse pointer, the window, and the icon. After introducing a particular level of the hierarchy, we proceeded down the left-most branch. We provided a description of the object and showed how it behaved.

Procedure-Based Content: Procedure-based training aims to show, by example, the connection of high-level task objects (e.g., memo) and actions (e.g., writing a memo) to the required corresponding low-level computer objects (e.g., document/file) and syntax (e.g., select file save). It encompasses a set of instructions to accomplish mini-tasks. Examples of the procedurebased approach include: starting and using an application to do a task, and cutting and pasting between two applications concurrently to share information.

![](/api/attachments/64DX6X2W/fulltext/images/b6f13a622ce22944c1f9fb3d5f80fa88f3fe88ff550522307fe5fbe52cdc4537.jpg)  
Figure 2. Example Structure of Concept-Based Training Material

To implement the procedure-based training approach, we focused on the actions that create useful behaviors with the software. The first step was the development of a set of actions that would accomplish a particular task. Simple tasks were built into more complex tasks (see Figure 3). For example, in the introductory session, trainees were first shown how to enter Windows. Then they were shown how to start the Clock application, how to minimize and maximize it, and how to close it. Each “goal” was phrased as a general activity and then as a specific instance of that activity.

We provided as much equivalent information as possible across the two conditions. For example, in both approaches, the minimize and maximize buttons were addressed early on. In concept-based training, these were introduced as standard objects of the window. In procedure-based training, these were introduced through actions showing how the Clock application could be viewed as an icon or in a window. In both conditions, both concepts and procedures are covered, but the difference is that each condition emphasized only one of the content areas.

## Procedure

## Prior to Training Sessions

Approximately 350 announcements were sent to faculty and administrative employees of a western college in the United States. The memo offered free Windows training over a four-week period during the late spring. One hundred forty-three people responded to the announcement.

The respondents were sent a package of materials including the preliminary questionnaire and a form to indicate preferred training times and dates. Ninety-two people returned the questionnaire ( $O_{1}$ on Figure 1) and form. These people were then scheduled to attend sessions to be held during three one-hour time slots on one of four days for four consecutive weeks. Thus, 12 sessions were scheduled with either seven or eight people slotted into each session.

## Training Sessions

The researchers designed the training scripts with one concept-based script and one procedure-based script for each week. The script for the first week and the general test were pretested prior to the study with three trainees who were representative of the subjects in this study. The purposes of the pretest were to assess the timing of the training script and the readability of the tests. Both were found to be acceptable. No further pretests were done since the general format of the training scripts and the test blanks were maintained across sessions (even though the content varied).

Each trainer repeated one script three times on one day, and the other script three times on the next day. Trainer #1 started with the procedure-based script, while trainer #2 started with the concept-based script. The general format of sessions for each of the four weeks is summarized in Appendix C. Trainees were given a detailed written agenda for each session.

![](/api/attachments/64DX6X2W/fulltext/images/ed90f468a4692a59e07bdb470f784c5fd437e5323544e12e6a3713d12c233c7f.jpg)  
Figure 3. Example of Procedure-Based Training Material

Sessions were held in a room that has a network of 386 work stations, although these were run in stand alone configuration for the training. There are four work stations on each side of a V-shaped table. At the bottom of the V is a workstation; the monitor image projects to a front screen. The trainer sat at this station and explained the material while demonstrating it on the front screen. Trainees sat in front of a workstation and could use it at any time to practice.

Session 1 (X₁ and Y₁): Session 1 began with a brief introduction by one of the researchers. The introduction explained the dual purpose of the training sessions: to introduce the trainees to Windows and to conduct research on software training. This dual purpose entailed asking the trainees to complete multiple tests across the sessions. The trainees were told that the tests would provide feedback to them as well as to the researchers. The introductory speech also provided a transfer of control from the researcher (who had been the contact for setting up the training sessions) to the trainer.

At this point, the trainees completed a pretest on the general material planned for the first session ( $O_{2}$ ). This was followed by a brief introduction to Windows by the trainer that explained its broad features and advantages for end users. Next, the trainer presented either the procedure-based or concept-based training materials. At the end of the session, trainees completed the post-test for the general material covered in this session ( $O_{3}$ ).

Session 2 ( $X_{2}$ and $Y_{2}$ ): This session was planned so that the trainees would retake the test from the first session ( $O_{4}$ ). $^{8}$ Then, trainees were given the results of their answers to the two tests they completed during the previous week.

The demonstration portion of session 2 dealt with Windows applications, including Write and Paintbrush. Then, the trainees were given hands-on exercises to practice Write and Paintbrush. The trainer walked around and gave help when needed. A second test was completed ( $O_{5}$ ) at the end of this session. This test was designed to test the trainees' knowledge of Windows applications. Finally, questions concerning the test were answered by the trainer.

Session 3 ( $X_{3}$ and $Y_{3}$ ): The trainer modeled three applications, and after each presentation, gave the trainees time to complete an exercise using the application. A final exercise was given to the trainees, but it was not collected as a dependent measure in the study. As the study progressed through the first two weeks, we determined that the trainees were finding the two times per session testing to be tiring. The design of the experiment was modified to provide the trainees with at least one session in which they did not have to complete written tests.

Session 4 ( $X_{4}$ and $Y_{4}$ ): The trainer introduced some new material through modeling. Then another test was completed ( $O_{6}$ ). The purpose of this observation was to test the integrative material presented in the session and to test each trainee's accumulated knowledge across the entire training period. The remaining time in this session was used for practice and to copy demonstration Windows applications.

## Follow-Up

Follow-up questionnaires were sent to the 82 trainees who attended at least one session ( $O_{7}$ ). The questionnaires aimed to determine who was using Windows about seven months after training sessions ended.

## Data analysis

Question items on the general, applications, and integrative tests were scored as 0, .5, or 1. If an item was true and the subject selected “Definitely True,” a score of 1 was awarded; if “Probably True” was selected, a score of .5 was awarded. Otherwise, a score of 0 was given. The same, but reversed system, was used for coding items that were false. Individual items were summed into six groupings: starting/ending applications, one application, multiple applications, recall, applied, and grand total. Each grouping was analyzed using Analysis of Covariance. $^{9}$ In all analyses, $\alpha$ was set at .10. To calculate the power of statistical tests, we used Cohen's (1977) methods. We also calculated 90 percent confidence intervals.

## Results

## Description of Subjects

The subjects who participated in the study were generally computer literate. More than half had some previous software training or course work related to computing. This justified the training focus on Windows rather than on computer basics. While the majority signed up for training “to find out what Windows was all about,” many did not have access to Windows on their computers. The design suffered in this regard because not everyone could practice what they learned. $^{10}$ The trainees reported a mix of learning styles, with the majority favoring instruction-based rather than exploration-based approaches to training. $^{11}$ We expected that the trainees would prefer the instruction-based approach since they volunteered to attend this kind of training.

## Results of statistical tests

Table 4 shows a summary of the means of the test results. A summary of the results of hypothesis tests is given in Table 5, which also provides a shortened statement of each hypothesis. Although the overall results found differences in total scores between the two treatment groups, these differences were due to existing knowledge and not a function of the treatments. Tests for H1 through H4 were powerful enough to detect large effects. The test for H5 did not have adequate power to detect large effects (see Appendix D for a detailed analysis of statistical power for this study). To provide further insight, the remainder of this section examines our control variables and the statistical tests of each session in detail.

## Control Variables

One-way ANCOVAs were run with preferred learning style, access to computing facilities, and previous knowledge and experience as independent variables $(\mathrm{O}_{1})$ , and the first test score $(\mathrm{O}_{2})$ as a covariate. There were no main effects, indicating that the groups were not different in terms of potentially confounding individual difference variables. Each questionnaire item was run separately since grouping of similar items (as per Table 2) did not produce inter-item reliability above .80 (Cronbach's alpha). Where trainer was a factor, the trainer main effect was not significant, nor were there significant interaction effects between method and trainer. The trainees who attended the fourth session rated the trainers equally. While there was a large dropout rate, this was not attributed to the quality of the trainers. The drop rate was not different between the two training approaches or trainers. $^{12}$

## Week 1

Table 6 shows the means for the test results. The table is categorized by training content and subject area. There were no significant main or interaction effects for type of training or trainer when scores at the end of the session ( $O_{3}$ ) were covaried with scores at the beginning of the session ( $O_{2}$ ). Thus, H1 is accepted. Since power was high, we feel confident in concluding that there were no differences between approaches in terms of amount learned after the first training session.

## Week 2

In nine of 12 sessions during week 2 the general test was completed as planned at the start of the training session (O $_{4}$ ). Because of an administrative error, trainees in trainer #2's conceptbased sessions completed the tests in the wrong sequence. This meant that trainer #2's concept-based trainees completed the applications test at the beginning (instead of the end) of the session. A comparison of scores from the sessions where the general test was completed first versus those where it was completed last showed no significant differences in scores, although the end-of-session scores were slightly lower. Therefore, the means reported in Table 6 include all subjects. ANCOVA results, however, do not differ whether the ending group is included or excluded. In the complete case, the ANCOVA was a 2 by 2 design since trainer can be included (it was a 1 by 2 design in the incomplete case). In either case, the scores at the end of week 1 were used as the covariate. Results of the tests indicate that there were no differences, so we cannot accept H3. Since power was high, we can conclude, contrary to our hypothesis, that there were no differences at the beginning of the second training session (see Appendix D).

Table 4. Summary of Test Scores

<table><tr><td rowspan="2">Test</td><td rowspan="2">Description</td><td colspan="3">Concept-Based</td><td colspan="3">Procedure-Based</td></tr><tr><td>Mean</td><td>Std.Dev.</td><td>N</td><td>Mean</td><td>Std.Dev.</td><td>N</td></tr><tr><td> $O_{2}$ </td><td>start of week 1</td><td>7.35</td><td>5.66</td><td>40</td><td>6.20</td><td>4.45</td><td>37</td></tr><tr><td> $O_{3}$ </td><td>end of week 1</td><td>15.66</td><td>5.28</td><td>40</td><td>14.80</td><td>4.18</td><td>37</td></tr><tr><td> $O_{3}$ </td><td>adjusted for  $O_{2}$ </td><td>15.22</td><td></td><td></td><td>15.24</td><td></td><td></td></tr><tr><td> $O_{4}$ </td><td>start of week 2</td><td>14.95</td><td>5.39</td><td>31</td><td>12.79</td><td>5.27</td><td>33</td></tr><tr><td> $O_{4}$ </td><td>adjusted for  $O_{3}$ </td><td>14.44</td><td></td><td></td><td>13.30</td><td></td><td></td></tr><tr><td> $O_{5}$ </td><td>end of week 2</td><td>13.89</td><td>4.23</td><td>18</td><td>10.90</td><td>4.89</td><td>35</td></tr><tr><td> $O_{5}$ </td><td>adjusted for  $O_{4}$ </td><td>13.05</td><td></td><td></td><td>11.74</td><td></td><td></td></tr><tr><td> $O_{6}$ </td><td>start of week 4</td><td>7.16</td><td>2.22</td><td>22</td><td>8.00</td><td>2.47</td><td>19</td></tr><tr><td> $O_{2}$ </td><td>this sample only</td><td>7.61</td><td>5.48</td><td></td><td>7.55</td><td>4.39</td><td></td></tr><tr><td> $O_{6}$ </td><td>adjusted for  $O_{2}$ </td><td>7.16</td><td></td><td></td><td>8.00</td><td></td><td></td></tr></table>

Because of the administrative error, the applications test was completed at the end of nine (rather than 12) sessions. Table 7 shows the means for the test results. Since the material covered in week 2 was different, the domain areas of Table 7 are different from Table 6. A 1 by 2 design ANCOVA was run using the general test items from Start Week 2 as the covariate. There were no main effects. Thus, H2 is accepted. Since the power of the test was high, the hypothesis of no differences at the end of the second training session can be accepted with confidence (see Appendix D).

## Week 4

There were no differences in total score on the integrative test ( $O_{6}$ ) when controlling for the total score on the first test ( $O_{2}$ ). Thus, H4 is rejected. Table 8 shows the means for the integrative test. The covariate was not significant in this analysis. An additional analysis was performed using the applications test score ( $O_{5}$ ) as the covariate. In this case, the covariate was significant. There were no differences between the training approaches in terms of attitudes toward the trainers and the training sessions. Since power was high, we can conclude with confidence, contrary to our hypothesis, that there were no differences between the concept-based and procedure-based groups in terms of amount learned at the end of the last training session (see Appendix D).

## Follow-Up

Seventy trainees returned the follow-up questionnaire. Of that group, 16 of 33 concept-based and 16 of 37 procedure-based trainees reported using Windows since the training. A chi-square test of goodness of fit showed no difference between the two approaches in terms of later use of the software. Thus, H5 is not accepted. Since power was low, the no-difference finding cannot be accepted with confidence (see Appendix D).

Table 5. Results of Hypotheses Tests

<table><tr><td>Hypothesis</td><td>Result</td><td>Dependent Variable</td><td> $Variables Tested^{13}$ </td><td>Statistics</td><td>p-value</td></tr><tr><td rowspan="2">H1: The mean scores on the post-test given in week 1 will be equal for trainees who received either concept-based or procedure-based training.</td><td rowspan="2">Accept</td><td rowspan="2"> $O_3$ </td><td>Covariate ( $O_2$ )</td><td> $F_{1,72}=145.0$ </td><td>.000</td></tr><tr><td>Training Approach</td><td> $F_{1,72}=0.0$ </td><td>.975</td></tr><tr><td rowspan="2">H2: The mean scores on the post-test given at the end of the training session in week 2 will be equal for trainees who received either concept-based or procedure-based training.</td><td rowspan="2">Accept</td><td rowspan="2"> $O_5$ </td><td>Covariate ( $O_4$ )</td><td> $F_{1,59}=89.7$ </td><td>.000</td></tr><tr><td>Training Approach</td><td> $F_{1,59}=1.5$ </td><td>.220</td></tr><tr><td rowspan="2">H3: The mean scores on the pretest given in week 2 will be higher for trainees who received concept-based training in week 1 than for trainees who received procedure-based training in week 1.</td><td rowspan="2">Reject</td><td rowspan="2"> $O_4$ </td><td>Covariate ( $O_3$ )</td><td> $F_{1,50}=25.4$ </td><td>.000</td></tr><tr><td>Training Approach</td><td> $F_{1,50}=1.3$ </td><td>.266</td></tr><tr><td rowspan="2">H4: The mean scores on the final test given during the training session in week 4 will be higher for trainees who received concept-based training throughout than for trainees who received procedure-based training throughout.</td><td rowspan="2">Reject</td><td rowspan="2"> $O_6$ </td><td>Covariate ( $O_2$ )</td><td> $F_{1,36}=1.84$ </td><td>.183</td></tr><tr><td>Training Approach</td><td> $F_{1,36}=0.71$ </td><td>.405</td></tr><tr><td>H5: More trainees who received concept-based training than who received procedure-based training will report using the software after training.</td><td>Reject</td><td> $O_7$ </td><td>Training Approach</td><td> $\chi^2_{1,70}=0.09$ </td><td>.753</td></tr></table>

## Discussion

## Amount learned

Most people came into the Windows training with very little knowledge about the software. Scores on the pretest averaged near 20 percent. After about 45 minutes of training, these scores more than doubled. We believe the first training session was successful across both approaches. The fact that most of the trainees returned for session 2 further confirms this conclusion. Although subjects learned the material readily in the first session, the learning, as measured at the end of the session, was equivalent across both approaches. This confirms our first hypothesis that the effects of concept-based and procedure-based treatments will be equivalent in the short run for a GUI (H1). A similar effect was observed in the next session where there was no difference in amount learned at the end of the session in relation to the material covered in the session (H2). At the end of a training session, the material is still fresh, and learners are able to recall their recent exposure to the software and the training materials regardless of approach used. Moreover, the intent of the approaches was to present equivalent information but in different ways. Thus, our expectation that no difference in learning between approaches would take place at the end of week 2 was confirmed.

We hypothesized that differences in the two treatments would surface over time where the concept-based learners would be able to access their integrated knowledge of the definition and behavior of related objects to derive the needed procedural knowledge. Procedure-based learners, having learned specific steps, would be at a disadvantage since these are not likely stored. Weak evidence based on supplementary analyses for week 2 indicates that concept-based learners may have retained more of certain kinds of knowledge (e.g., about multiple applications) than procedure-based learners. However, total test scores showed no difference (H3). By the end of the fourth training session, there was clearly no difference between groups (H4). In addition, the explanatory power of the very first pretest scores ( $O_{2}$ ) was no longer significant. There are several potential explanations of these results, which are explored next.

Table 6. Mean Scores for General Tests ( $O_{2}$ , $O_{3}$ , $O_{4}$ )

<table><tr><td colspan="2"></td><td>Starting and Ending (max = 9)</td><td>One Application (max = 18)</td><td>Multiple Applications (max = 7)</td><td>Total (max = 34)</td></tr><tr><td rowspan="3">Concept-Based</td><td> $O_{2}$  (n = 40)</td><td>1.74</td><td>3.96</td><td>1.65</td><td>7.35</td></tr><tr><td> $O_{3}$  (n = 40)</td><td>3.70</td><td>8.64</td><td>3.33</td><td>15.66</td></tr><tr><td> $O_{4}$  (n = 35)</td><td>4.19</td><td>8.53</td><td>3.39</td><td>16.11</td></tr><tr><td rowspan="3">Procedure-Based</td><td> $O_{2}$  (n = 33)</td><td>1.77</td><td>3.11</td><td>1.32</td><td>6.20</td></tr><tr><td> $O_{3}$  (n = 33)</td><td>3.88</td><td>7.46</td><td>3.46</td><td>14.80</td></tr><tr><td> $O_{4}$  (n = 33)</td><td>3.42</td><td>6.70</td><td>2.67</td><td>12.79</td></tr></table>

Table 7. Mean Scores for Applications Test ( $O_{6}$ )

<table><tr><td></td><td>Windows (max = 10)</td><td>Write (max = 10)</td><td>Paintbrush (max = 14)</td><td>Total (max = 34)</td></tr><tr><td>Concept-Based (n = 18)</td><td>4.86</td><td>4.61</td><td>6.39</td><td>15.86</td></tr><tr><td>Procedure-Based (n = 35)</td><td>4.04</td><td>3.54</td><td>4.86</td><td>12.44</td></tr></table>

Table 8. Mean Scores for Integrative Test ( $O_{6}$ )

<table><tr><td></td><td>Windows Concepts (max = 6)</td><td>One Application (max = 5)</td><td>Multiple Applications (max = 3)</td><td>Total (max = 14)</td></tr><tr><td>Concept-Based (n = 22)</td><td>3.23</td><td>2.07</td><td>1.86</td><td>7.16</td></tr><tr><td>Procedure-Based (n = 19)</td><td>3.21</td><td>2.47</td><td>2.32</td><td>8.00</td></tr></table>

One reason that trainees receiving the two types of training information did not differ overall may be that learners try to fill in the gaps in their knowledge. Both trainers observed that people not receiving one kind of information wanted the other kind. They both stated that they found it difficult, at times, to follow the script without supplementing it. This observation also fits with the results of the study. The tests were designed to test overall knowledge of Windows. To do well on these tests, the trainees had to know both conceptual and procedural aspects of the software. It is likely that those trainees who attended all four sessions had learned basic information about Windows and had filled in gaps themselves as needed.

The trainees may have been able to fill in the gaps in their knowledge by inferring conceptual information from procedural knowledge and vice versa (viz., Glaser, 1990). The ability of learners to infer new information from information presented on the screen is greatly enhanced in a GUI as opposed to a command-line interface. The GUI screen is full of suggestive pictures and diagrams. In addition, in a GUI, the distinction between conceptual and procedural information is sometimes artificial. For example, if you know that items in a file list are objects then you know you can drag them to another location. If you know that you can drag something, then you know that it is an object. Even if you are not told about these relationships, the process of operating the interface may create this knowledge. In a command-line interface like DOS, the distinctions between concept and procedure are more clear cut. When you type "COPY A:\*.\* B:", you do not necessarily have to know that the copy command requires a source and a target, or what the symbols A, B, and \* mean.

Our study was different from previous efforts in that it was longitudinal, the domain was a GUI, and the presentation of the training material was interactive. The longitudinal nature of the study meant that learners were exposed to a larger and more comprehensive quantity of training material in more than one session. This exposure may have helped surface the need to learn both conceptual and procedural information. The GUI attribute meant that the learners were provided with some conceptual and procedural information through the interface. The interactive format of the training meant that learners may have felt that they could look to the trainer or other trainees for more information. This may explain the difficulty our trainers had in following the script of each session.

## Later use

There was no difference in the number of people who used Windows after training regardless of the approach used to train them (H5). This is consistent with the findings of Olfman and Bostrom (1991), who reported that about half of the trainees that took a full day of free training for Lotus 1-2-3 used the software later. The same most common reasons for not using the software were stated in both studies: non-users did not have the available resources. It seems that many people will take free software training out of curiosity even when they may not have the available resources.

One explanation for finding no differences in usage patterns may be that trainees who experimented with Windows between sessions would be most likely to continue using it after training. If so, then our data would show that those who experimented between training sessions were the same as those who reported using Windows later on. Yet, a smaller proportion of experimenters (40 percent) said they used the software after training than those who did not experiment (59 percent), although this proportional difference was not significant (z = 1.23, p = .11, power = .34). $^{14}$ Since there is not strong power to detect that there is no difference in number of users across the two methods, it is still plausible to consider that concept-based training may motivate more trainees to use Windows. Another test of this hypothesis, using only trainees who have available resources prior to training, should be conducted.

## Implications for Practice and Future research

## GUI training design

There seems to be a tacit understanding in the software industry that GUIs will require less training and support than command-line interfaces (Schindler, 1991). However, we believe that these interfaces are not a panacea. The decline in learning and the rise in dropout rate after the first training session in our study indicate that there can be obstacles to realizing the training and other potential advantages of graphical user interfaces. This issue is important for organizations that are moving to GUI environments and need to train large numbers of employees. To explore these issues we re-examined our results to look for potential explanations.

One obvious explanation for the no-difference findings is that the training sessions were poorly designed. However, the data indicates that at least the first session was successful, as measured by an average 124 percent increase in scores on the general test. Although the remainder of the sessions were not as successful, the format of all the sessions was similar.

Our trainers observed that the trainees had difficulty completing exercises in session 3, which dealt with learning multiple-applications Windows tasks. Many trainees appeared to struggle with this integrative exercise. Some could not even get started. This observation is interesting because the exercise in session 3 was based on integrating previously covered material and is unlikely to have resulted because the exercise was theoretically too difficult. Certainly, it was practically too difficult. In addition, overall learning in week 2 seems to have increased relatively less than it did the first week.

One explanation is that while the trainees were able to understand some of the concepts and procedures we taught, they were unable to learn enough to carry them forward. Corporate trainers indicate that there appears to be a steep learning curve for Windows after a simple understanding has been achieved (see Schindler, 1991). A research study is needed to examine if there is a threshold to learning a GUI, whether this threshold needs to be passed in the first GUI training session, and if there is some specific method or approach that facilitates the passing of this threshold. The existence of a threshold amount of learning may be linked to the sophistication of the Windows interface. People are required to do much more in Windows than they were used to doing in a command-line operating system (e.g., DOS). Windows allows users to utilize and share data among multiple applications. To successfully learn these extra features, trainees need to work at a higher level of sophistication.

Another explanation is that our trainees lost their initial momentum after their learning during the first session. One reason might be that they were not motivated to continue to learn. A follow-up with some of the subjects indicated that people who did drop out were curious about what they might learn in the training, and that by the end of the first session or early on into the second session, they had satisfied their curiosity and basic literacy requirements about the nature of the Windows software

## Training content

Software trainees appear to organize their mental models in a conceptual, procedural, or mixed-mode form (Santhanam and Sein, 1993; Sein and Bostrom, 1990). Given that trainees organize their mental models in different ways, it is possible that they would benefit differentially from concept-based or procedure-based training; with one approach or the other facilitating a particular type of model formation. Our study did not measure the kinds of mental models formed. A study should be done to learn whether people who form a certain type of mental model can be best facilitated with training materials of appropriate content. For example, it may be that people who form conceptual mental models are hindered if they receive procedure-based training. Such a study must include a measure of a person's mental model formation process. While Sein and colleagues have done some initial work in this area with respect to command-line interfaces, additional instrument development will be needed to extend this measurement for GUIs.

## Conclusion

There are limitations to the findings of this paper. Internal validity threats were not completely ruled out because of the low power of the test of H5 (after training usage). It is clear that many other factors contribute to usage besides training. The mix-up of questionnaires for one session in week 2 and the loss of trainees during each week of the study were tested and shown to not directly affect results, but cannot be completely ruled out as threats. Construct validity threats include the measures of learning, since our tests tapped only one kind of learning; the training sessions, since they were not completely concept-based or procedure-based; and the fact that Windows is only one kind of graphical user interface. External validity is not assured because we did not randomly sample our subjects from the general population, even though we did find that subjects fit the general profile of working adult learners.

This study demonstrates that the design of training content for graphical user interfaces as it relates to the emphasis of concepts over procedures (or vice versa) may not impact learning and later use of the target software. The main explanation for the lack of differences may be the need for trainees to learn both kinds of information. Moreover, if there is an advantage to be gained by matching training to individuals' mental models, then this approach could enhance learning. In either case, GUIs seem to call for a different training approach than command-line interfaces.

## Acknowledgements

We wish to thank the Fletcher-Jones foundation for financial support; Melissa Thomas-Schmit, Charles Elledge, and Justus Schlichting for assistance with administration and training; Dale Berger for advice on data analysis; and the associate editor, the reviewers, as well as, Bob Bostrom, Kieran Mathieson, John Satzinger, and Jane Webster for helpful comments on earlier versions of the paper.

## References

Anderson, J.R. "Acquisition of Cognitive Skill," Psychological Review (89:4), July 1982, pp. 369-406.

Baker, B.O., Hardyck, C.F., and Petrinovich, L.F. "Weak Measurements vs. Strong Statistics: An Empirical Critique of S. S. Stevens' Proscriptions on Statistics," Educational and Psychological Measurement (26:2), Summer 1966, pp. 291-309.

Baroudi, J.J. and Orlikowski, W.J. "The Problem of Statistical Power in MIS Research," MIS Quarterly (13:1), March 1989, pp. 87-106.

Bikson, T.K. and Gutek, B.A. "Training in Automated Offices: An Empirical Study of Design and Methods," in Training for Tomorrow, J.I. Rijnsdorp and Tj. Plomp (eds.), Elsevier Science Publishers, B.V., Amsterdam, 1984, pp. 129-143.

Bostrom, R.P., Olfman L., and Sein, M.K. "End-User Computing: A Research Framework for Investigating the Training/Learning Process," in Human Factors in Management Information Systems, J.M. Carey (ed.), Ablex Publishing Corporation, Norwood, NJ, 1988, pp. 221-250.

Bostrom, R.P., Olfman, L., and Sein, M.K. "The Importance of Learning Style in End-User Training," MIS Quarterly (14:1), March 1990, pp. 101-119.

Carroll, J.M. The Nürnberg Funnel: Designing Minimalist Instruction for Practical Computer Skill, MIT Press, Cambridge, MA, 1990.

Charney, D.H. and Reder, L.M. "Designing Interactive Tutorials for Computer Users," Human-Computer Interaction (2:4), 1986, pp. 297-317.

Charney, D.H. and Reder, L.M. "Initial Skill Learning: An Analysis of How Elaborations Facilitate the Three Components," in Model-

ing Cognition, P. Morris (ed.), John Wiley & Sons Ltd., Chichester, England, 1987, pp. 135-165.

Charney, D., Reder, L., and Kusbit, G. W. "Goal Setting and Procedure Selection in Acquiring Computer Skills: A Comparison of Tutorials, Problem Solving, and Learner Exploration," Cognition and Instruction (7:4), 1990, pp. 323-342.

Cohen, J. Statistical Power Analysis for the Behavioral Sciences (rev. ed.), Academic Press, New York, 1977.

Collins, A. "Cognitive Apprenticeship and Instruction Technology," in Educational Values and Cognitive Instruction: Implications for Reform, L. Idol and B.F. Jones (eds.), Lawrence Erlbaum Associates, Inc., Hillsdale, NJ, 1991, pp. 121-138.

Cook, T.D. and Campbell, D.T. Quasi-Experimentation: Design & Analysis Issues for Field Settings, Houghton Mifflin Company, Boston, MA, 1979.

Czaja, S.J., Hammond, K., Blaskovich, J.J., and Swede, H. “Learning to Use a Word-Processing System as a Function of Training Strategy,” Behaviour and Information Technology (5:3), July-September 1986, pp. 203-216.

Davis, S. and Bostrom, R.P. "Training End Users to Compute: An Experimental Investigation of the Roles of the Computer Interface and Training Methods," MIS Quarterly (17:1), March 1993, pp. 61-85.

Foley, J. "The Structure of Interactive Command Languages," in Methodology of Interaction: Seillac II, R.A. Geudj et al. (eds.), North-Holland, Amsterdam, 1980, pp. 227-234.

Gist, M.E., Schwoerer, C., and Rosen, B. "Effects of Alternative Training Methods on Self-Efficacy and Performance in Computer Software Training," Journal of Applied Psychology (74:6), December 1989, pp. 884-891.

Glaser, R. "The Reemergence of Learning Theory within Instructional Research," American Psychologist (45:1), January 1990, pp. 29-39.

Gould, J.D. and Lewis, C. "Designing for Usability: Key Principles and What Designers Think," Communications of the ACM (28:3), March 1985, pp. 300-311.

Green, G.I. and Hughes, C.T. "Effects of Decision Support Systems Training and Cognitive

Style on Decision Process Attributes," Journal of MIS (3:2), Fall 1986, pp. 83-93.

Hiebert, J. and Lefevre, P. "Conceptual and Procedural Knowledge in Mathematics: An Introductory Analysis," in Conceptual and Procedural Knowledge: The Case of Mathematics, J. Hiebert (ed.), Lawrence Erlbaum Associates, Publishers, Hillsdale, NJ, 1986, pp. 1-27.

Hutchins, E.L., Hollan, J.D., and Norman, D.A. "Direct Manipulation Interfaces," Human-Computer Interaction (1:4), 1985, pp. 311-338.

Jagodzinski, A.P. "A Theoretical Basis for the Representation of On-Line Computer Systems to Naive Users," International Journal of Man-Machine Studies (18:3), March 1983, pp. 215-252.

Kalen, T. and Allwood, C.M. "A Survey of the Training of Computer Users in Swedish Companies," Behaviour and Information Technology (10:1), January-February 1991, pp. 81-90.

Kieras, D. and Polson, P.G. "An Approach to the Formal Analysis of User Complexity," International Journal of Man-Machine Studies (22:4), April 1985, pp. 365-394.

Kitajima, M. and Polson, P.G. "A Computational Model of Skilled Use of a Graphical User Interface," in CHI '92 Conference Proceedings, P. Bauersfield, J. Bennett, and G. Lynch (eds.), Association for Computing Machinery, New York, 1992, pp. 241-249.

Mayer, R.E. "Models for Understanding," Review of Educational Research (59:1), Spring 1989, pp. 43-64.

Microsoft Corporation, Microsoft Windows 3.0 User's Guide, 1990.

Nelson, R.R. and Cheney, P. "Training End Users: An Exploratory Study," MIS Quarterly (11:4), December 1987, pp. 547-559.

Olfman, L. and Bostrom, R.P. "End-User Software Training: An Experimental Comparison of Methods to Enhance Motivation," Journal of Information Systems (1:4), October 1991, pp. 249-266.

Perrig, W. and Kintsch, W. "Propositional and Situational Representations of Text," Journal of Memory and Language (24:5), October 1985, pp. 503-518.

Reder, L.M., Charney, D.H., and Morgan, K.I. "The Role of Elaborations in Learning a Skill from an Instructional Text," Memory and

Cognition (14:1), January 1986, pp. 64-78.

Santhanam, R. and Sein, M.K. "Improving End User Proficiency: Effects of Conceptual Training and Nature of Interaction," Information Systems Research, forthcoming.

Schindler, P. "Learning Windows in a Corporate Environment," Windows Magazine (2:10), November 1991, pp. 95-97.

Schwartz, B. and Reisberg, D. Learning and Memory, W.W. Norton and Company, New York, 1991.

Sein, M.K. and Bostrom, R.P. "Individual Differences and Conceptual Models in Training Novice Users," Human-Computer Interaction (4:3), 1989, pp. 197-229.

Sein, M.K. and Bostrom, R.P. "An Experimental Investigation of the Role and Nature of Mental Models in the Learning of Desktop Systems," in Desktop Information Technology, K.M. Kaiser and H.J. Oppelland (eds.), North-Holland, Amsterdam, 1990, pp. 253-276.

Sommer, D. and Patton, C. "Learning Needs a Human Touch—Classroom Instruction Eases PC Training," InfoWorld (10:17), April 25, 1988, p. 38.

SPSS. SPSS Reference Guide, SPSS Inc., Chicago, IL 1990.

Thompson, R.L., Higgins, C.A., and Howell, J.M. "Personal Computing: Toward a Conceptual Model of Utilization," MIS Quarterly (15:1), March 1991, pp. 125-143.

Webster, J. and Martocchio, J.J. "Microcomputer Playfulness: Development of a Measure with Workplace Implications," MIS Quarterly (16:2), June 1992, pp. 201-226.

Wright, P. "Issues of Content and Presentation in Document Design," in Handbook of Human-Computer Interaction, M. Helander (ed.), Elsevier Science Publishers, B.V., Amsterdam, 1988, pp. 629-652.

## About the Authors

Lorne Olfman is associate professor of information science in the Programs in Information Science at Claremont Graduate School. He holds a Ph.D. in management information systems from Indiana University. His research has been published in MIS Quarterly, International Journal of Human Computer Studies (formerly IJMMS),

Information Systems Journal (formerly JIS), Decision Support Systems, INFOR, and Data Base. Professor Olfman has also published many book chapters and conference papers. His current research focuses on end-user training, group support systems, and organizational memory. He is program chair for the 1995 Conference on Computer Personnel Research.

Munir Mandviwalla is assistant professor of information science in the Computer and Information Sciences Division at Temple University. He hold a Ph.D. in management information systems from the Claremont Graduate School Programs in Information Science. His current research focuses on groupware, design, and end-user training.

Appendix A
Examples of General Questionnaire Items

<table><tr><td>Domain</td><td>Item</td><td>Answer</td></tr><tr><td colspan="3">Starting and Ending Applications</td></tr><tr><td>RECALL</td><td>Program Manager is an application that allows you to manage other applications.</td><td>True</td></tr><tr><td>APPLIED</td><td>Clicking on a program icon in Program Manager starts an application.</td><td>False</td></tr><tr><td colspan="3">Using One Application</td></tr><tr><td>RECALL</td><td>You cannot size a dialog box by dragging its corners/borders.</td><td>False</td></tr><tr><td>APPLIED</td><td>A maximized window cannot be dragged by its title bar.</td><td>True</td></tr><tr><td colspan="3">Using Multiple Applications</td></tr><tr><td>RECALL</td><td>A window can overlap other windows on the desktop.</td><td>True</td></tr><tr><td>APPLIED</td><td>Two applications must be in equally sized windows for them to share information.</td><td>False</td></tr></table>

## Appendix B

## Common Design Components for Training Sessions

## 1. Media

Media are technologies that deliver training objectives. Media include: manuals and audio, video, computer-based, and “live” presentations. There is little evidence singling out the most effective software training media. There are perceived benefits from using all the forms mentioned above depending on the design of other aspects of the training materials. Wright (1988) compares paper versus computer-based delivery of documentation and finds that both have advantages. Collins (1991) describes how computer-based training materials benefit learning by providing an environment similar to that of an apprenticeship. We chose to use live presenters in this study. This is the most popular (Kalen and Allwood, 1991; Nelson and Cheney, 1987) and effective (Bikson and Gutek, 1984; Czaja, et al., 1986) method of training in organizations.

## 2. Interaction

Interaction is the form in which the trainee associates with the media. Computer-aided instruction has a predefined two-way interaction with the trainee, whereas video tapes have a one-way interaction with the trainee and live instructors have a two-way open interaction with the trainee. Live instructors can tell whether a person is understanding materials and can react accordingly (Sommer and Patton, 1988). Research by Gist, et al. (1989) concludes that the process of behavior modeling (demonstrating the software by directly showing its effects) is a more effective method than tutorial instruction (telling the trainee what the software will do). Hands-on interaction with the computer during training is also important from both an understanding and a motivational perspective (Green and Hughes, 1986).

Trainees were given their own workstation for hands-on practice. The instructors used a behavior modeling approach by providing demonstrations with an overhead video projector. The process was designed to follow a “here is something you should know, now try it” rule.

## 3. Style

Style describes the form of the content. It includes the order of presentation within and between objectives, the ordering of examples and exercises within the materials, and the format and conventions of presentation. Davis and Bostrom (1993) describe two general styles of software training: exploration-based and instruction-based. They define training styles (they use the term “approaches”) in terms of process and structural features. Exploration-based training is characterized by induction, trial and error, higher learner control, incomplete learning materials, and a features focus. Instruction-based training is characterized by deduction, programmed process, lower learner control, complete learning materials, and a features focus. These methods can vary in the exploration or instruction orientation of each component. The classification indicates that exploration-based and instruction-based training are on a continuum and do not have an orthogonal relationship. Although there is some positive evidence for the advantage of exploration-based training (Carrol, 1990), mixed results have been reported (Charney, et al., 1990).

We implemented an instruction-based style for the initial training session because we assumed that learners will not have the domain experience (Charney, et al., 1990) needed to fully take advantage of the exploration-based style. However, we progressively made the training more exploration-based through modifications to the traditional systematic instruction-based style. For software such as Windows (or any multitasking operating system), the task domain is partly related to computer concepts and partly to desktop concepts. Windows allows users to perform new kinds of tasks that neither novice nor experienced users are capable of performing. Windows users need to understand the function and operation of a mouse (how to click, double click, drag, and drop), icons, hotspots, control panels, title bars, windows and so on before they can begin to use the software meaningfully. Domain experience may not apply. Thus, it is possible to expect instruction-based training to be preferable initially for the Windows application, while exploration-based training is preferable later when the trainee has acquired an understanding of the basic computer concepts in the software.

# Appendix C Format of Training Sessions

<table><tr><td>Session</td><td>Agenda</td></tr><tr><td>1</td><td>Introduction to Windows 3.0Overview (researcher—5 minutes)General test (4-5 minutes)Introduction to Windows 3.0 (Trainer—5 minutes)Basics of using Windows 3.0 (Trainer—40 minutes)General test (4-5 minutes)</td></tr><tr><td>2</td><td>Windows AccessoriesGeneral (or applications) test (5 minutes)Hand back previous week&#x27;s test (10 minutes)Demonstration of accessories (trainer—10 minutes)Play and question time (30 minutes)Applications (or general) test (5 minutes)Review test (5 minutes)</td></tr><tr><td>3</td><td>Windows ToolsPresentation of File Manager (Trainer—10 minutes)Exercise using File Manager (10 minutes)Presentation of Program Manager (Trainer—10 minutes)Exercise using Program Manager (10 minutes)Presentation of IconDraw (Trainer—5 minutes)Exercise using IconDraw (5 minutes)Final exercise (10 minutes)</td></tr><tr><td>4</td><td>Advanced Topics and ApplicationsBrief presentation on control panel (Trainer—10 minutes)Brief presentation on task list (Trainer—2 minutes)Final test (10 minutes)Play with applications and copy diskettes</td></tr></table>

## Appendix D

## Statistical Power and Confidence Intervals

Power indicates the probability of detecting an effect if it exists. Cohen (1977) specifies the effect size index (d) for a t-test as the number of standard deviations between the means of interest. He indicates that small, medium, and large effect size d values are .2, .5, and .8, respectively, meaning that a large effect size, for example, would indicate a difference between the means of interest of .8 standard deviations.

We first calculated the effect sizes for the test for H1 through H4 by multiplying .2, .5, and .8 by the overall sample standard deviation. We then determined the power of each test to detail these effects, and also the effect size required for power of .80 (an accepted standard criterion for “high” power—see Baroudi and Orlikowski (1989)). Table D1 provides a summary of these analyses. For H5, the data analysis was done using a chi-square test. The power of the test in this sample was .11. Forty-eight percent of concept-based trainees used Windows after training as compared to 43 percent of procedure-based trainees, a difference of 5 percent. For power of .80, a difference of 29 percent would be required. Since effect size does not apply for chi-square tests, we can only speculate on the ability of this study to detect an effect for H5. We believe that a difference of 29 percent is too large to expect, so that it is likely that the current test could not allow us to conclude that there is no difference in adoption rates between the two training approaches.

Table D1. Analysis of Statistical Power

<table><tr><td rowspan="2">Test</td><td rowspan="2">Actual Mean  $Diff.^{15}$ </td><td rowspan="2">Standard Deviation (σ)</td><td colspan="2">Small Effect Size</td><td colspan="2">Medium Effect Size</td><td colspan="2">Large Effect Size</td><td colspan="2">For Power = .80</td></tr><tr><td>Mean Diff. = .2σ</td><td>Power</td><td>Mean Diff. = .5σ</td><td>Power</td><td>Mean Diff. = .8σ</td><td>Power</td><td>Effect size Index (d)</td><td>Est. Mean Diff.</td></tr><tr><td>H1</td><td>-0.02</td><td>4.77</td><td>0.95</td><td>.22</td><td>2.38</td><td>.70</td><td>3.82</td><td>.97</td><td>.58</td><td>2.75</td></tr><tr><td>H2</td><td>1.14</td><td>5.20</td><td>1.10</td><td>.21</td><td>2.60</td><td>.63</td><td>4.40</td><td>.96</td><td>.63</td><td>2.30</td></tr><tr><td>H3</td><td>1.31</td><td>4.56</td><td>0.91</td><td>.17</td><td>2.28</td><td>.52</td><td>3.65</td><td>.86</td><td>.73</td><td>3.35</td></tr><tr><td>H4</td><td>-0.84</td><td>2.31</td><td>0.46</td><td>.15</td><td>1.16</td><td>.46</td><td>1.85</td><td>.80</td><td>.79</td><td>1.85</td></tr></table>

We calculated 90 percent confidence intervals for the mean differences of H1 through H4. A 90 percent confidence interval indicates a 90 percent chance that the interval has captured the true population difference. Thus, an interval that does not overlap zero would indicate a significant difference. Table D2 summarizes the 90 percent confidence intervals for H1 through H4. Note that all confidence intervals overlap zero. Note also that we used adjusted means and actual, rather than adjusted, standard deviations for calculating confidence intervals because SPSS (1990) does not calculate adjusted standard deviations for covariance analysis. This may give a slight bias in confidence interval estimations. However, a sensitivity analysis showed that fluctuations in the standard deviations would make almost no change to the estimates provided here.

Table D2. 90 Percent Confidence Intervals

<table><tr><td rowspan="2">Test</td><td colspan="3">Mean Difference: Concept-Based Training Minus Procedure-Based Training</td></tr><tr><td>Adjusted</td><td>Lower Bound</td><td>Upper Bound</td></tr><tr><td>H1</td><td>-0.02</td><td>-1.82</td><td>1.78</td></tr><tr><td>H2</td><td>1.14</td><td>-1.09</td><td>3.37</td></tr><tr><td>H3</td><td>1.31</td><td>-0.86</td><td>3.48</td></tr><tr><td>H4</td><td>-0.84</td><td>-2.08</td><td>0.40</td></tr></table>
