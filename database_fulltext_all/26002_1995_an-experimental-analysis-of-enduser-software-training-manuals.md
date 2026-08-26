---
otero_id: 26002
otero_key: "ZC2JJPMP"
title: "An experimental analysis of end‐user software training manuals*"
authors: "L. Olfman; M. Mandviwalla"
year: "1995"
journal: "Information Systems Journal"
doi: "10.1111/j.1365-2575.1995.tb00087.x"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# An experimental analysis of end-user software training manuals\*

L. Olfman and M. Mandviwalla

Programs in Information Science, The Claremont Graduate School, Claremont, CA 91711, USA, and \*Computer and Information Sciences, Temple University, Philadelphia, PA 19122, USA

Abstract. This paper describes two experimental studies that examine the difference between software training manuals for new users of a groupware software package. The manuals differed in terms of their elaboration of procedural, conceptual and usage information. It was expected that manuals with rich conceptual and usage elaborations would produce the best learning outcomes. No significant differences were found in the learning outcomes of subjects with either high or low levels of previous computer experience. The elements that influence the development of instructional manuals are analysed from the perspective of our findings. The paper suggests that examining the underlying relationships between procedural, conceptual and usage information is an important topic for understanding and evaluating design guidelines for instructional manuals. Research into the methods used to communicate this information may provide insight on the usage and development of instructional manuals.

Keywords: conceptual and procedural information, end-user training, software manuals, text elaborations

## 1 INTRODUCTION

An effective software training programme should provide users with the necessary skills to employ their available applications. Three components of skill learning are concepts, procedures and usage (Charney et al., 1988). Concepts are the definitions of the subject matter; procedures describe how to apply a concept; and usage details why and when a procedure should be applied. A MOVE command can be learned by understanding that it is a procedure for transferring an object from one location to another, by learning the syntax for executing the procedure and by knowing that it is to be used when the location of the object must be changed. The amount of elaboration of this information and the form of its presentation are important issues in the design of software training programmes.

A training programme can emphasize the three skill components in varying degrees. For example, in the training manual of a spreadsheet application, the description of the MOVE command is limited to explaining how to move a number from one cell to another, or to explaining how to move both cells and numbers, or to explaining all possible variations of the command. In other words, a procedure is described and exemplified for only one specific component of its command range, several components or all components. The degree of procedural elaboration is independent of the amount of information imparted about concepts and/or usage. Similarly, the degree of conceptual and usage elaboration is independent of the other skill components. The training material may describe the procedures in detail while barely touching on the other skill components. Or it could emphasize usage while briefly defining concepts, and providing some procedural information.

Reder et al. (1986) define rich elaborations as those that provide more than basic information. They found that rich procedural elaboration increased initial learning of 'command-based' operating system software as compared with sparse elaboration. This was not the case for rich conceptual/usage elaborations. Since the conceptual and usage components of their material were not separated, the effects of rich concepts and/or usage elaborations were not examined.

The purpose of this paper is to explore the relationships among the components of skill learning in software training. We report the conduct and results of two experiments that compared different training manuals that contained varying amounts of information. The work extends the Reder et al. (1986) study by (1) separating the effects of rich procedural, conceptual and usage elaborations, (2) studying 'menu-based' software and (3) comparing the impacts on experienced versus novice software users.

Section 2 of the paper reviews the research literature on software training, focusing primarily on training manuals. This is followed by a description of each experiment, including, hypotheses, methods and results. The paper concludes with a discussion of implications for future research and practice in the domain of software training design.

## 2 PREVIOUS RESEARCH

Bostrom et al. (1988) provide a framework for studying end-user training/learning (see Fig. 1). They suggest measuring training outcomes in terms of understanding and motivation to use the software because both outcomes will directly affect later usage. A user who understands a software package but does not perceive its usefulness on the job will not use it. A person who is motivated to use a piece of software but does not understand how to use it will not use it, will require much support or will encounter problems while learning the software.

Software training consists of three key elements: the target software, the training method and the characteristics of the trainee. A software training method has several inputs, including an overview, a set of presentation materials and documentation such as training exercises. The focus of this paper is on the topic of training manuals.

Carroll and his colleagues at IBM (Carroll, 1984; Carroll et al., 1986; Black et al., 1987) designed and refined the minimal manual. This manual supports a discovery/active learning approach for users. The minimal manual focuses on main issues to keep the learner from becoming frustrated, and tries to get the learner to use the target software as soon as possible.

![](/api/attachments/ZC2JJPMP/fulltext/images/5515bb4ee3b9eb368da51f0df631f33e4d426b0dae30a88aaa296fb19682e185.jpg)  
Figure 1. A research framework for studying software training.

Charney, Reder and colleagues at Carnegie Mellon University (Reder et al., 1986; Charney & Reder, 1986, 1987; Charney et al., 1988) have studied the topic of text elaborations in instructional materials. Charney and Reder (1987) provide a detailed explanation of why elaborations should facilitate initial skill learning. Analogies can assist in concept knowledge acquisition, while exemplification and situational examples can enhance learning of procedural and usage information. Reder et al. (1986) compared rich and sparse elaborations of procedural and concept plus usage information. They found that rich procedural elaborations influenced understanding, while rich concept/usage elaborations did not. Moreover, specific problem-solving exercises interspersed throughout the text were helpful for learners. It should be noted that elaborations were only successful when students had an orientation towards general learning of the software, rather than specific goal-oriented learning.

Some of the above findings are not congruent with the philosophy of the minimal manual that emphasizes non-specific exercises and sparse procedural elaborations (Carroll et al., 1986). The minimal manual introduces a fourth type of information for novice learners: error solving. A minimal manual is one that avoids rich elaborations of procedures, but focuses on guiding the novice learner in performing a task. In part, the minimal manual attempts to ensure that the learner can continue to the conclusion of a task by providing rich elaborations of error-solving information. Thus, it addresses another outcome of training besides understanding, namely motivation to use the software.

Black et al. (1987) found that organizing a manual around 'typical situations' aided learning. Olfman & Bostrom (1991) studied the issue of providing specific examples versus asking learners to bring their own examples (problems) to training. They gave a minimal manual to the trainees who brought their own problems. In the training evaluation questionnaire, these learners rated the manual significantly higher than a standard (unelaborated) manual that was used in the generic problem-solving training approach.

Many researchers, including Mayer (1981), have concluded that a conceptual model is an important component for enhancing learning. Conceptual models provide a framework on which learners can 'hang' their new knowledge. There are two types of conceptual models: abstract and analogical. Sein & Bostrom (1989) found that abstract models are effective in facilitating far transfer learning (when the problems are different from the ones covered during training). However, Sein (1988) also found that in some software packages it is difficult to design an effective abstract model: the users' knowledge must be sophisticated enough to comprehend the model. Yet, the Reder et al. (1986) study found that rich procedural elaborations influenced understanding, while rich concept/usage elaborations did not. The Reder et al. study targeted the concept elaborations at the command level of the software. Without an overall conceptual model of the software, rich conceptual elaborations of lower level structures (e.g. commands) may not be any more effective than sparse elaborations.

## 3 EXPERIMENT

## 3.1 Overview

It is not clear from the Reder et al. (1986) study that the combination of rich procedural, sparse conceptual and sparse usage information is an adequate solution. First, the study packaged some information such that the effectiveness of one or the other (concept and usage) was difficult to detect. Second, the study only looked at the understanding outcome, not at the motivational outcome. It is possible, for example, that rich usage information may lead to higher levels of motivation. Third, the study may have focused on a command level that was too low for all the types of elaborations to have any effect.

A controlled post-test only laboratory experiment was designed to examine these possibilities. There was one independent variable of interest: the type of training manual used in an initial training session.

## 3.2 Subjects

The subjects for this study were students who were entering a graduate programme in information systems at Claremont Graduate School. A total of 33 students participated in the study, of whom 31 completed one or more of the dependent measures. All students had some previous experience with computers; most had a high level of experience. On average, they self-reported using computers for more than 4 years, and for more than 11 hours per week during the previous 12 months.

## 3.3 Target software

The target software for the study was TEAMate (MMB, 1987). TEAMate is groupware; it integrates the concepts of electronic mail, electronic bulletin board and group outlines. We used the single-user DOS version of TEAMate that was running on IBM PC/ATs. We chose TEAMate because we wanted a novel software package and TEAMate was a new product in a new category of software. None of the students had previously used TEAMate, although one had seen a demonstration of it, and two others reported that they had encountered a similar product. We also wanted to use software that could be accessed later by the students; a beta-test copy of TEAMate (UNIX version) was available for student use.

## 3.4 Procedure

Before the beginning of the autumn term, new students were invited to attend an orientation session. Six sessions were scheduled with five or six students attending each session. All classes in the programme are held during evening hours, so the sessions began $1\frac{1}{2}$ -hours before the beginning of class. During the first quarter-hour, the administrative director of the programme presented introductory remarks on campus resources. In the next quarter-hour the experimenters were introduced and the students were given a brief introduction to the study and their roles in the study.

Subjects were then taken to a personal computer laboratory and were seated in front of a computer. The machines had been previously turned on with their screens turned off, and a training manual had been placed by each workstation. Out of the three types of manuals (see section 3.5 below for details), two of each type were randomly laid out at the six available machines for each session. Each manual was composed of an introductory section, a training section and a 'loose-leaf' reference sheet.

After seating, subjects were given a further brief introduction and then asked to read the introductory section of the manual. When all subjects had finished reading, they were told to turn on their screens and were given instructions on how to access TEAMate. They were then told to work through the manual, using the machine to practice, and taking care to read all materials presented. Subjects were due to attend classes after the experiment. Therefore, they may not have followed the instruction to read completely all the training materials. A post-experiment debriefing revealed that some subjects did not read the entire manual. This pattern was true across all manuals.

Subjects were asked to inform the experimenters when they had completed these tasks. After task completion, the training manual was removed and a questionnaire was given to each subject. The questionnaire contained specific questions about the software (subjects were allowed to use the reference sheet to answer these questions) and about their attitudes toward the software. Following completion of this questionnaire, subjects were given a second questionnaire to take home and return as soon as possible. The second questionnaire contained questions on previous computer experience.

## 3.5 Training manuals

Three training manual were developed. All the manuals included rich procedural elaborations (see Table 1). The rich-P manual, contained rich procedural elaborations, but sparse conceptual and usage elaborations. The rich-P-C manual included rich procedural and conceptual elaborations, but sparse usage elaborations. The rich-P-C-U manual included rich procedural, conceptual and usage elaborations.

Table 1. Training manual elaborations

<table><tr><td>Manual</td><td>Rich elaborations</td><td>Sparse elaborations</td></tr><tr><td>Rich-P</td><td>Procedural</td><td>Conceptual, usage</td></tr><tr><td>Rich-P-C</td><td>Procedural, conceptual</td><td>Usage</td></tr><tr><td>Rich-P-C-U</td><td>Procedural, conceptual, usage</td><td></td></tr></table>

The design model shown in Fig. 2 was used to create a baseline manual. The environmental factors (trainer, technology, organization and users) helped set the goals of the training. For example, our target users were familiar with computer basics (e.g. knowing the location of the 'Enter' key), so we assumed that knowledge in the manual design. The type of technology (new and different) and the organizational context (educational institution) also helped set the focus and design of the training. The design of the training materials (the manual), while keeping the above goals and environmental factors in mind, consisted in choosing the content, medium (reference manual, tutorial, on-line, video, etc.), type of interaction (listening/viewing, questioning, interacting or reading) and the style (organization, format, consistency and conventions) of the manual.

![](/api/attachments/ZC2JJPMP/fulltext/images/102d8df353f39da9bec58b7ff17b50653c7df3b3633e6f3f6805ec75cc4570f9.jpg)  
Figure 2. Training design model.

The contents consisted of an integrated mixture of conceptual, procedural and usage information. The medium was a tutorial/reference manual, interaction was through reading a printed copy and the style was consistent and very structured.

The baseline manual was tested and revised several times through usage and evaluation by other students in the spring term. The experimental manuals were constructed from the baseline manual. The experimental manuals varied the content of the material while holding the other factors constant. We chose a set of rudimentary commands and the Charney et al. (1988) guidelines as our design criteria. First, a procedural manual was developed by rewriting, editing and adding sections in the baseline manual. This formed the rich-P manual. The rich-P-C manual was constructed by adding a conceptual model (tested and developed in the baseline manual) to the rich-P manual. The rich-P-C-U manual built on the rich-P-C manual by adding additional information about usage.

The construction of the baseline manual helped us to experience at first hand the requirements of content in a 'real' manual developed for our particular environmental combination of users, technology and organization. The baseline manual also helped collect a 'pot' of tested material. This pot was then used to construct the experimental manuals.

![](/api/attachments/ZC2JJPMP/fulltext/images/0292b013ce7a179b6c1885cae779c5036510f6e261ed19644b52dc4b71586a9e.jpg)  
Figure 3. Conceptual model of TEAMate.

Each manual contained an introductory section that included three short subsections. The first subsection was a brief introduction to the study. The second subsection contained a description of the TEAMate software and the third subsection contained a description of the software interface.

The second subsection in the rich-P manual talked about TEAMate in general terms. In the rich-P-C and rich-P-C-U versions, the information in this subsection was linked to an analogical

## A. EXPAND

The EXPAND command will do two things: First it will make the highlighted topic the current (first) topic on the screen. Second, it will reveal any sub-topics one level underneath it.

In other words EXPAND enlarges a segment (one parent & its children) of the outline structure.

## A. EXPAND

The EXPAND command will do two things: First it will make the highlighted topic the current (first) topic on the screen. Second, it will reveal any sub-topics one level underneath it.

In other words EXPAND works as a zoom lens. When you first log on to TEAMate you are only seeing a distant overview of the wall, with only the top level Bulletin Boards visible. Expand will let you zoom into a particular board and its children.

![](/api/attachments/ZC2JJPMP/fulltext/images/8a29cf41d644c27ef694acd67d62bd77f0fc4e7c2aabbe8abe66e00443d13c2a.jpg)

4(b): Rich-P-C and Rich-P-C-U Overview

Figure 4. Example of overview.

conceptual model, including figures, that represented TEAMate as a set of physical bulletin boards (see Fig. 3).

The training section of the manuals contained six subsections; each described a TEAMate command. Within each subsection there were five headings. The overview contained information about the command. The rich-P overview was a summary statement about the com-

## PROCEDURE

The following steps are required:

\- Select the topic you wish to expand

\- Press E to invoke the EXPAND command

To select a topic use the cursor keys to position the highlight (reverse video) over it. A + sign follows expandable topics. The + shows that these topics have more subtopics under them.

Invoking EXPAND on a topic which is already the current (first) topic on the screen, will incrementally increase the outline view by one level.

The EXPAND command is only applicable on topic. It is available in the main menu screen.

## EXAMPLE

From the list of topics in the screen image below, you want to find out the subtopics of Practice Topics.

![](/api/attachments/ZC2JJPMP/fulltext/images/13852393357f9e20520944bd950c9216239a6a7f2be5ce9ba373726b62447f17.jpg)

Find Display Add Workarea Mail Topic Create Users Options Print Quit Expand Shrink Restore

NEW USER #8 (0)

• Welcome to TEAMate #7 (2) +
Practice Topics #8 (0) +

The + sign at its end confirms the existence of more levels underneath. Move the highlight from NEW USER down to Practice Topics (use the down arrow key). Press E to invoke the EXPAND command. Practice Topics will become the current (first) topic on the screen. Its sub-topics are now visible (screen image below).

Find Display Add Workarea Mail Topic Create Users Options Print Quit Expand Shrink Restore

Practice Topics #8 (0)

The McDonald case #29 (0) +

The Sabatini case #34 (0) +

## EXERCISE

Find the Topic Suggested revisions in contract and make it the first topic on the screen (Hint: look further under The McDonald case).

Figure 5. Example of procedure, example and exercise.

![](/api/attachments/ZC2JJPMP/fulltext/images/f2d9ed8a111e7e97724224a111a86f3587dfd89c80c52b8cbad869117b7549e7.jpg)

USAGE

Use this command to get a more detailed view of the outline

6(a): Rich-P and Rich-P-C Usage

USAGE

Use this command as a navigating tool to get a more detailed view of the outline. Press E successively to reveal all the sub-topics under a topic. To view the entire outline structure, highlight the topmost topic, and then continually press E.

6(b): Rich-P-C-U Usage

Figure 6. Example of usage.

mand (see Fig. 4a); the rich-P-C and rich-P-C-U overviews contained more elaborate statements, and a link to the conceptual model (see Fig. 4b). The procedure described how to use the command. The procedure was the same for all manuals, along with the example and the hands-on exercise (see Fig. 5). The usage section was a brief statement in the rich-P and rich-P-C versions (see Fig. 6a), but was more specific and detailed in the rich-P-C-U version (see Fig. 6b).

## 3.6 Dependent measures

## 3.6.1 Quiz

To measure subjects' understanding of the TEAMate software, we used written questions. (Pilot studies showed that hands-on exercises could not be completed in the time allotted for the experiment.) The questions were scored out of a maximum of 10 points and partial credit was given for some answers. In order to ask a range of questions, but enable the subjects to complete the questionnaire, we used three sets of questions. An analysis of variance (ANOVA) on the question sets showed no difference in scores ( $F_{1,29}=1.98$ , $P=0.158$ ), although one set of questions did generate somewhat higher scores than the other two sets. Scores are reported as percentages.

## 3.6.2 Motivational scores

Subjects were questioned on perceived usefulness, ease of use, attitude towards using and intention to use the software. The questions were scored on a seven-point Likert scale (perceived usefulness and ease of use, four items each) and a seven-point semantic differential scale (attitude, four items; and intention, two items), and were developed and refined by Davis

. n

(1989). They were highly reliable. Since all constructs contained multiple items on seven-point scales, these were averaged in order to report standardized scores.

## 3.6.3 Audit files

TEAMate can be set up to capture an audit trail of its usage. Although this file does not give a complete keystroke log, it captures a large amount of information about the interactive session. TEAMate adds one line to the audit file for each command issued and for each navigational keystroke. As such, the more the software is used, the larger the audit file. We expected that trainees with rich usage information would use the software more than those in the other two conditions. We report here the size of the audit files in terms of kilobytes of disk storage.

## 3.7 Data analysis

Data were analysed using the ANOVA procedure in SPSS $^{x}$ (SPSS, 1988). In all cases, the results of one-way ANOVAs are reported in terms of F-and P-values.

## 3.8 Results and discussion

No significant differences were found in the data analyses. The results are summarized in Table 2. Some directional and near-significant differences were found. Though the differences were not significant, rich-P trainees had the highest perceived ease of use and the smallest audit trail files. These directional differences were opposite to what was expected. Our expectation was that rich conceptual and usage information would add to trainees' knowledge and motivation. However, the findings also suggest that rich-P manuals may not have the inherent advantages over rich-P-C and rich-P-C-U manuals that were predicted by Reder et al. (1986). For example, the scores for the rich-P and rich-P-C manuals are not far apart. This may indicate that, although the additional material in the rich-P-C manual did not show an advantage in the score, the extra cognitive load of reading the conceptual material did not confuse or negatively affect the trainees. Another explanation for the lack of differences might have been that the rich-P-C and rich P-C-U trainees did not read the additional information provided to them. Recall that some trainees did not read the details of the manual, although this behaviour was reported by some subjects from each group.

Table 2. Results of statistical tests for experiment 1

<table><tr><td></td><td></td><td>Rich-P</td><td>Rich-P-C</td><td colspan="2">Rich-P-C-U</td><td>Overall</td><td>ANOVA</td></tr><tr><td rowspan="2">Quiz score (%)</td><td rowspan="2">11*</td><td rowspan="2">67.1†</td><td rowspan="2">10</td><td rowspan="2">66.8</td><td>10</td><td rowspan="2">31</td><td rowspan="2"> $F_{2.26}=0.71$  $P=0.498$ </td></tr><tr><td>56.2</td></tr><tr><td rowspan="2">Usefulness</td><td rowspan="2">10</td><td rowspan="2">3.9</td><td rowspan="2">10</td><td rowspan="2">2.8</td><td>8</td><td rowspan="2">28</td><td rowspan="2"> $F_{2.25}=1.61$  $P=0.219$ </td></tr><tr><td>3.8</td></tr><tr><td rowspan="2">Ease of use</td><td rowspan="2">10</td><td rowspan="2">5.0</td><td rowspan="2">10</td><td rowspan="2">4.1</td><td>8</td><td rowspan="2">28</td><td rowspan="2"> $F_{2.25}=1.96$  $P=0.162$ </td></tr><tr><td>4.3</td></tr><tr><td rowspan="2">Attitude</td><td rowspan="2">10</td><td rowspan="2">3.7</td><td rowspan="2">10</td><td rowspan="2">3.9</td><td>8</td><td rowspan="2">28</td><td rowspan="2"> $F_{2.25}=0.18$  $P=0.833$ </td></tr><tr><td>4.0</td></tr><tr><td rowspan="2">Intention to use</td><td rowspan="2">10</td><td rowspan="2">3.5</td><td rowspan="2">10</td><td rowspan="2">3.1</td><td>8</td><td rowspan="2">28</td><td rowspan="2"> $F_{2.25}=0.19$  $P=0.832$ </td></tr><tr><td>3.3</td></tr><tr><td rowspan="2">Audit file size (kB)</td><td rowspan="2">6</td><td rowspan="2">10 204</td><td rowspan="2">10</td><td rowspan="2">12 600</td><td>7</td><td rowspan="2">23</td><td rowspan="2"> $F_{2.21}=0.39$  $P=0.685$ </td></tr><tr><td>12 563</td></tr></table>

† Mean.

The audit trails show that the trainees did work through the examples and exercises. Some trainees carried the examples further, and explored the software in more detail than others. As indicated by the size of the audit files, the exploration was not a function of the type of manual. A detailed analysis of keystrokes and screens viewed does not reveal any particular set of behaviours that differentiated explorations among the different groups.

## 4 EXPERIMENT 2

## 4.1 Overview

Most software is built with some overall conceptual idea, and this often gets translated into the interface. For example, part of the Lotus 1-2-3 (and other spreadsheet software) interface is based on a paper spreadsheet model. Learners that can discern this underlying philosophy may do very well even with no conceptual information. A subject might have done well with a rich procedural and rich conceptual model not because the model was of any help but because the subject, from interaction with the software, had 'figured out' how to use it. Similarly, a subject might have done well with a rich procedural only model not because procedural information is sufficient, but because the subject managed to 'figure out' the software by interacting with it.

One plausible explanation for why some users can 'figure out' the conceptual model in a new software package may be derived from their high level of experience in using computers. Subjects in experiment 1 were very experienced with computers. Experiment 2 explores the influence of rich conceptual information on novice users' understanding.

## 4.2 Subjects

The subjects for the follow-up study were business students enrolled in an introductory computer tools course at California State Polytechnic University, Pomona. A total of 31 students participated in the study. Most students were receiving their first exposure to computers during the course. The study took place near the end of the academic quarter. On average, subjects self-reported using computers for less than $1\frac{1}{2}$ years, and for about 5 hours per week during the past year. The usage means for this group are significantly different from the group of subjects in experiment 1 ( $F_{1,56}=78.126; P=0.00$ ).

## 4.3 Target software

As in experiment 1, the target software was the single-user DOS version of TEAMate. The machines were IBM PS/2 model 50s. None of the subjects had previously used TEAMate or a similar product. They did not have access to the software outside the study.

## 4.4 Procedure and training manuals

Near the end of the spring quarter, students were offered extra credit for participating in an experimental session in a large computer laboratory. Two sessions were conducted, with 16 students in one and 15 in the other.

Prior to the students' arrival, machines were turned on, screens were turned off and a training manual was placed by each workstation. Two types of manuals were used in each session: the rich-P and rich-P-C manuals described in experiment 1. Once the students were seated, the experimental procedure was the same as described in experiment 1, except that the previous computer experience questionnaire was administered at the end of the session. Unlike subjects in the previous experiment, the vast majority of the subjects in this experiment did read the manuals because they were not under a time deadline.

## 4.5 Dependent measures and data analysis

The quiz consisted of four written questions taken from the set of questions used in experiment 1. No measure of motivation was taken since the subjects would not be able to use the software after training. Audit files were collected; however, we did not expect to find a difference since there was no difference in usage elaborations between the two manuals. Data were analysed using the ANOVA procedure of SPSS $^{x}$ .

## 4.6 Results and discussion

No significant differences were found by the data analyses. The results are summarized in Table 3, and generally confirm the findings of experiment 1 in terms of understanding outcomes. Scores in experiment 1 were significantly higher ( $F_{1,61}=10.62; P=0.002$ ), showing that more experienced computer users understood more than less experienced computer users. However, rich conceptual information did not show a significant difference in the amount of learning in either experiment. As in experiment 1, the audit files did not reveal any different behaviour patterns between the two groups, although there were differences in the amount of exploration undertaken by different individuals.

One of the quiz questions in this experiment was designed to determine the subjects' understanding of the underlying conceptual model of the software. The question asked subjects to describe a particular feature of TEAMate in their own words. Those who used the rich-P-C manual had significantly higher scores on this question ( $F_{1, 29}=4.34; P=0.045$ ). This evidence suggests that the rich conceptual information in the rich-P-C manual resulted in an additional kind of learning, namely a better understanding of the underlying conceptual model of the software, as compared with those reading the rich-P manual. Since both versions of the training manual led to the same level of understanding, this result also provides some evidence that the combination of rich procedural and conceptual information may be better than a training manual with only rich procedural elaborations.

Table 3. Results of statistical tests for experiment 2

<table><tr><td></td><td></td><td>Rich-P</td><td>Rich-P-C</td><td>Overall</td><td>ANOVA</td></tr><tr><td rowspan="2">Quiz score (%)</td><td>14*</td><td>17</td><td>31</td><td colspan="2"> $F_{1.29}=0.79$ P=0.381</td></tr><tr><td></td><td>47.4†</td><td>39.5</td><td colspan="2">43.8</td></tr><tr><td rowspan="2">Audit file size (kB)</td><td>14</td><td>17</td><td>31</td><td colspan="2"> $F_{1.29}=0.59$ P=0.496</td></tr><tr><td></td><td>12 393</td><td>11 547</td><td colspan="2">11 929</td></tr></table>

• n.  
+ Mean.

## 5 IMPLICATIONS AND FUTURE RESEARCH

This study raises several issues related to the design of training materials. Some of the issues were identified as intervening variables in the experimental studies, while others introduce important implications for future research. These issues are outlined in the following points.

## 5.1 The relationship of initial training development of long-term understanding is still not clear

The cost savings of excluding rich conceptual information from an initial training session may not justify the benefits of better long-term understanding of the software. Researchers tend to focus on immediate outcomes of training. Only a few studies have tried to follow up on trainees' knowledge and/or usage over an extended period. How the initial impact of training affects long-term usage and the formation of mental models are questions that still need to be answered. That this study was not able to show that rich usage information benefited trainees in our first experiment should not imply that this information will be ineffective in the long run. It is very possible that the impacts of rich conceptual and usage information cannot be determined without follow-up analysis of trainees who are using the software. A natural extension of this research is to perform this kind of analysis.

## 5.2 Modular design of manuals may not be possible

Designing the baseline manual followed by the experimental manuals raised questions about whether rich conceptual elaborations can be added to rich procedural elaborations modularly. Our experience suggests that a good implementation of a rich conceptual elaboration may require changing the procedural elaborations. The procedural, conceptual and usage elaborations may not be separable elements and a modular approach may result in a lower quality product than an integrated approach. An important area of future research will be to attempt to identify and define the relationships (if any) and the constraints resulting from the relationships among conceptual, usage and procedural elaborations.

## 5.3 Learning style may have a bearing on the kinds of elaborations that learners require

The development of the training manual/user's guide for the TEAMate personal computer software package showed that there were two typical approaches taken by users who tested the manual. One group of users liked and wanted summary material, while another group preferred elaborations and did not mention the need for summaries. These differences appear to map to either a heuristic (unstructured) or an analytical (structured) learning style. One would expect heuristic learners to like short summary information since they tend to learn by experimenting. On the other hand, analytical learners would prefer to be taken through the material as part of a structured session. These behaviours might also account for the fact that different subjects spent more time exploring the software than others. Recall that the differences in the size of audit files were not related to the type of manual used.

When we add the dimension of type of user into the discussion, then in the context of our study an important question is whether the elaborations match the processing style of the user. Recent research by Bostrom et al. (1990) argues that individual differences must be considered in the design and conduct of end-user training. Given our findings from the users who tested the initial design of the training manual, and the findings noted above, we did consider including learning style as a variable in these research studies. However, while there are some measures of learning style available (for example, see Pask, 1976), none provides an efficient and effective method of measurement. More research is needed to measure and match individual processing styles with training manuals.

## 5.4 Conceptual information is not limited to elaborations

Our experience in designing manuals suggests that conceptual information can be imparted not just through text elaborations in a manual, but also through the sequencing of tasks in the manual, the interface of the software, the context of training sessions and the task at hand. In our study the software interface and the design of the manual could have imparted rich conceptual information, making the rich text-based conceptual elaborations redundant. This explanation may reconcile the results of our study (rich text-based conceptual information does not have significant effects on initial understanding) with research that proposes that conceptual models aid learners in building a mental model for future learning. Text (including figures) might not be the only method that designers can use to impart conceptual information.

Recent work by Rosson et al. (1990) on minimal manual design employed several methods that were used to introduce conceptual information. These included the sequencing and choice of the task, the design of the instructional programme, an introductory conceptual section in the manual and the design of the tools they employed. However, some of these methods were used implicitly and were introduced into the design not as 'conceptual' information but as improvements to the training. An important goal for future research is to map out and identify all the possible types of methods that can be used to communicate conceptual, procedural and usage information. It will be useful for researchers to develop contingency theories that can identify useful combinations of these methods along with their advantages and disadvantages.

## 5.5 New forms of technology will change the way training materials are designed

It is not likely that conceptual, procedural and usage information will be imparted only by using paper-based forms. Carroll and Aaronson (1988) demonstrate the viability of on-line training materials. Procedures can be imparted through video clips rather than through text-based descriptions. Concepts can be explained through a variety of methods (as noted above) including multimedia presentations. Usage can also be demonstrated through specific video clips as well. In addition, changes in the computer interface may require researchers to re-examine the structure and breakdown of training content. For example, graphical user interfaces (GUIs) integrate a rich, comprehensive and complex conceptual model into the interface itself. Moreover, procedural information for a GUI is not as straightforward as it is for command-line interfaces where syntax can be easily specified. The new media types described above may be more appropriate for GUI training. Traditional linear text-based documentation that leads users through a series of procedures or tries to highlight concepts may not be able to depict accurately and simply the basic complexity of such interfaces. An alternative to such documentation may be sophisticated hypertext-based on-line help with audiovisual cues that enable trainees to quickly learn and find the information they need.

## 6 CONCLUSION

This paper describes two experiments that examined the effect of different types of elaborations in instructional manuals on learning. The work builds upon earlier research on developing guidelines for the design of training manuals. The different elaborations were based on two levels (rich versus sparse) of conceptual, usage and procedural information. We found only weak to no support for our expectation that rich conceptual and usage information would positively affect understanding and motivation to use the target software.

Future research is needed to determine if elaborations are not the only method of imparting conceptual information, if it may be possible to separate completely one type of skill learning information from another, whether the effect of learning style is important and whether long-term outcomes might be different from short-term results. These questions need to be addressed before we can draw generalized conclusions about the contents of training manuals that are designed for short initial training sessions for novice learners of a specific software package.

## 7 ACKNOWLEDGEMENTS

We wish to thank Bob Baskerville and Roger Morrell of MMB Development Corporation for allowing us to use TEAMate for these experiments; John Setzinger (University of Georgia) and Chris Bell for providing assistance during the experiments; and the editors and reviewers for their helpful comments on an earlier version of the paper.

## REFERENCES

Black, J.B., Carroll, J.M. & Mcguigan, S.M. (1987) What kind of minimal instruction manual is most effective. CHI + GI Conference Proceedings., Carroll, J.M. and Tanner, P.P. (eds), 159–162. ACM Press, New York.

Bostrom, R.P., Olfman, L. & Sein, M.K. (1988). End-user computing: a research framework for investigating the training/learning process. In: Human Factors in Management Information Systems: The Design and Implementation of Successful Information Systems, Carey J. (ed.). 221–250. Publishing Corporation, Norwood, NJ.

Bostrom, R.P., Olfman, L. & Sein, M.K. (1990). The importance of learning style in end-user training. MIS Quarterly, 14 (1), 101–119.

Carroll, J.M. (1984) Minimalist training. Datamation, 30(18), 125–136.

Carroll, J.M., & Aaronson, A.P. (1988). Learning by doing with simulated intelligent help. Communications of the ACM, 30, 1064–1079.

Carroll, J.M., Smith-Kerker, P.L. Ford, J.R. & Mazur, S.A. (1985) The minimal manual, Research Report RC 11637 (no. 52295). IBM, Yorktown, NY.

Chamey, D.H. & Reder, L.M. (1986). Designing interactive tutorials for computer users. Human-Computer Interaction, 2, 297-317.

Charney, D.H. & Reder, L.M. (1987). Initial skill learning: an analysis of how elaborations facilitate the three components. In: Modelling Cognition, Morris, P. (ed.), 135–165. John Wiley, Chichester.

Charney, D.H., Reder, L.M. & Wells, G.W. (1988). Studies of elaboration in instructional texts. In: Effective Documentation: What We have Learned From Research, Doheny-Farina (ed.). MIT press, Boston.

Davis, F.D. (1989). Perceived usefulness, perceived ease of use, and end user acceptance of information technology. MIS Quarterly, 13, 318–339.

Mayer, R.E. (1981) The psychology of how novices learn computer programming. Computing Surveys, 13, 121–141.

MMB (1987) TEAMate Reference. MMB Development Corporation, Rolling Hills Estates, CA.

Olfman, L., & Bostrom, R.P. (1991) End-user software training: an experimental comparison of methods to enhance motivation. Journal of Information Systems, 1, 249–266.

Olfman, L., & Mandviwalla, M. (1990). An experimental comparison of end-user software training manuals. In: Proceedings of the IFIP WG 8.2 Working Conference on Desktop Information Technology and Organizational Worklife in the 1990s, Kaiser, K.M., & Oppelland, H.J. (eds), 227–236. Elsevier Science Publishers B.V. (North-Holland), Amsterdam.

Pask, G. (1976). Conversion Theory. Elsevier, Amsterdam.
Reder, L.M., Charmey, D.H. & Morgan, K.I. (1986) The role of elaborations in learning a skill from an instructional text. Memory and Cognition, 14, 64–78.

Rosson, M.B., Carroll, J.M. & Bellamy, R.K.E. (1990) Smalltalk scaffolding: a case study of minimalist instruction. CHI '90 Conference Proceedings, Chew, J.C. & Whiteside, J. (eds), 423–429. ACM Press, New York.

Sein, M.K. (1988) Conceptual models in training novice users of electronic mail: effectiveness of abstract vs. analogical models and influence of individual differences. Unpublished doctoral dissertation, Indiana University.

Sein, M.K. & Bostrom, R.P. (1989) Individual differences and conceptual models in training novice users. Human-Computer Interaction, 4, 197–229.

SPSS (1988) User's Guide. SPSS, Chicago.

## Biographies

Lorne Offman is Associate Professor of Information Science at Claremont Graduate School. His research interests are in three areas: end-user training, group support systems, and organizational memory. Lorne has previously

## L Olfman & M Mandviwalla

published in Information Systems Journal, as well as in MIS Quarterly, Journal of MIS, Decision Support Systems Journal, International Journal of Human-Computer Studies, and the ACM Transactions on Computer-Human Interaction. Lorne is program chair of the 1995 ACM Special Interest Group on Computer Personnel Research conference and chair of the 1996 conference. He has been a mini-track coordinator for many years at the Hawaii International Conference on System Sciences. He is co-editor of a special issue of Communications of the ACM on end-user training. Lorne's current research projects include experimental studies of software training methods and organizational memory technologies.

Munir Mandviwalla is Assistant Professor in Computer and Information Sciences at Temple University. His research interests include the requirements of groupware, collaborative work, cooperative learning, and software training. Munir's work has been published in ACM Transactions on Computer-Human Interaction, MIS Quarterly, and several international conferences. Munir is currently working on a project to apply mobile computing and wireless technologies as cooperative learning tools. Other recent projects include use of the World Wide Web as an instructional medium, investigating groupware interoperability, and applying a systems analysis perspective to groupware design.
