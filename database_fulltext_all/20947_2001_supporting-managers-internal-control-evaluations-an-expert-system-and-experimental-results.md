---
otero_id: 20947
otero_key: "ZANMVVRM"
title: "Supporting managers' internal control evaluations: an expert system and experimental results"
authors: "Chuleeporn Changchit; Clyde W Holsapple; Donald L Madden"
year: "2001"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(00)00127-5"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Supporting managers’ internal control evaluations: an expert system and experimental results

Chuleeporn Changchit <sup>a</sup>, Clyde W. Holsapple <sup>b,)</sup>, Donald L. Madden <sup>c</sup>

<sup>a</sup> Management Sciences Department, UniÕersity of Iowa, Iowa City, IA, USA <sup>b</sup> School of Management, Carol M. Gatton College of Business Administration, UniÕersity of Kentucky, Lexington, KY 40506-0034, USA <sup>c</sup> School of Accountancy, UniÕersity of Kentucky, Lexington, KY, USA

Accepted 1 June 2000

## Abstract

Internal control issues are of significance to entities to assure the accuracy, reliability, and timeliness of the financial reports. Although management is responsible for maintaining an effective internal control system, the literature contains no example of a system devised to aid managers detecting internal control weaknesses. This type of system might prove to be highly beneficial. Nonetheless, it is not obvious that this system would yield positive results because managers may not be willing or feel comfortable using it. This study reports on the development of such system, plus empirical testing of its value and managers’ perceptions on its usefulness. q 2001 Elsevier Science B.V. All rights reserved.

Keywords: Expert system; Internal control; Auditing; Supporting manager

## 1. Introduction

Evaluation and design of internal control systems is of crucial importance to management. Yet, it is a subject that receives too little attention in the management literature. Managers tend not to be trained in the internal control arts, the detection of problems tends to be left to auditors, and internal controls are often viewed mainly as a means for preventing intentional irregularities. However, managers’ decisions can have internal control implications, perhaps unintentional or unrealized. Auditors do not oversee all such decisions as they are being made. Thus, it seems prudent for managers to approach decision making with the support of an internal control perspective. Here, we report on the initial study of an expert system for facilitating the transfer of internal control knowledge to practicing managers, thereby supporting their decisions from an internal control perspective.

Both accounting firms and researchers have devoted significant effort to the development of decision aids, especially expert systems, to assist auditors in making the complex audit decisions encountered in today’s business environment 7,9,15,17,27,29,31 .<sup>w</sup> <sup>x</sup> Several expert systems had been built to assist auditors in evaluating internal control systems 5,10,12,<sup>w</sup> 13,20,21,31,35 . These systems are generally devel- <sup>x</sup> oped using either professional literature for a knowledge source, or interview or protocol analysis to acquire knowledge from human experts 23,28 . Such<sup>w</sup> <sup>x</sup> systems have been successfully applied and there is no need to examine the benefits of using them to help auditors. However, there are no previously reported studies of expert systems devised to aid managers in evaluating internal control weaknesses. Because it is an organization’s management, not auditors, who bear ultimate responsibility for maintaining an effective internal control, there is a need to study the feasibility and value of equipping managers with expert systems that give internal control advice.

Nonetheless, it is not obvious that the use of such a system would yield positive results because managers typically have neither specific background in internal control concepts nor hands-on experience with expert systems. The managers may not be willing to learn the concept of the internal controls or may not feel comfortable using the expert systems. For example, a manager may provide incorrect inputs, not understand system outputs, find it difficult to work with an expert system, or resist considering the advice it gives.

The main purpose of this research effort is to address the question of whether an expert system can be devised to assist managers detect potential weaknesses of internal control systems in their organizations more efficiently and<sup>r</sup>or more effectively. A subsequent experiment is also conducted to examine its value to managers. The extent of its assistance is gauged in terms of the managers’ effectiveness, efficiency, and satisfaction in using the system to evaluate internal controls. If such a system can be shown to be both capable of development and beneficial, then we will have established that the distribution of auditors’ expertise in evaluating internal control systems to a wide number of users can be accomplished via expert system technology. The result is a new way for increasing the efficiency and effectiveness of ongoing decision-making processes concerned with internal control. Such expert systems could be developed and deployed by either an organization or its auditors.

The following section discusses the literature on expert system applications for internal control evaluations. The next section provides the theoretical basis for designing the experiment. We then outline the construction of an expert system developed for assisting managers evaluate existing internal control systems in their organizations. We describe a laboratory experiment designed to examine the usefulness of this expert system, including hypotheses to be tested, independent and response variables, construction of experimental materials, subjects and their tasks, and statistical analysis procedures. The paper closes with highlights of research findings, notes about contributions of the research, and identification of directions for future related research.

## 2. Background

Internal control is defined as a process designed to provide reasonable assurance regarding the achievement of objectives in the following categories: reliability of financial reporting, effectiveness and efficiency of operations, and compliance with applicable laws and regulation 1,2,25,32 . Maintain-<sup>w</sup> <sup>x</sup> ing an effective internal control system is crucial to any business organization. Without the ability to ensure the accuracy and reliability of accounting information, a business organization could not survive in a competitive environment 5 . The problem<sup>w</sup> <sup>x</sup> of checking internal control weaknesses is a Anondeterministic polynomialB problem 6,22 . Such prob-<sup>w</sup> <sup>x</sup> lems are often solved best by using the rules of thumb of experienced auditors. When such rules can be incorporated as reasoning knowledge in an expert system, the potential of developing an expert system to aid in solving audit problems is quite high.

A wide variety of prototype and commercial systems has been developed for assisting auditors evaluate their clients’ internal control systems 18,26,30 .<sup>w</sup> <sup>x</sup> Representative examples of prototype systems and expert systems implemented for evaluating a client’s internal control system are shown in Table 1 <sup>w</sup> <sup>x</sup> 5,12,13,20,21,31,35 . These systems aimed at helping auditors, not an organization’s management. Some of the terms used in the systems are easy to understand by auditors, but not the novice users. These systems are generally designed to help auditors determine the extent of other tests they will perform in conducting an audit. If an auditor determines that the client’s internal controls are designed properly and are functioning as designed, he or she can reduce direct testing of account balances accordingly 19 . <sup>w</sup> <sup>x</sup>

Table 1  
Systems for internal control evaluations

<table><tr><td>Name</td><td>Developer(s)</td></tr><tr><td>APE: Audit Planning and Evidence</td><td>Denna</td></tr><tr><td>Inherent Risk Analysis</td><td>KPMG Peat Marwick</td></tr><tr><td>PLANET</td><td>Price Waterhouse</td></tr><tr><td>IRE</td><td>Dhar et al.; Peters</td></tr><tr><td>Risk Advisor</td><td>Coopers &amp; Lybrand</td></tr><tr><td>ANSWER</td><td>Arthur Young</td></tr><tr><td>CCR/36 Advisor</td><td>Ernst &amp; Young</td></tr><tr><td>CFILE</td><td>KPMG Peat Marwick</td></tr><tr><td>C&amp;L Control Risk Assessor</td><td>Coopers &amp; Lybrand</td></tr><tr><td>ICE</td><td>Kelly</td></tr><tr><td>ICES</td><td>Grudnitski &amp; Arthur Young</td></tr><tr><td>Internal Control Analyzer</td><td>Gal</td></tr><tr><td>Internal Control Expert</td><td>Deloitte &amp; Touche</td></tr><tr><td>Flow Eval</td><td>Ernst &amp; Young</td></tr><tr><td>Systematic</td><td>Price Waterhouse</td></tr><tr><td>TICOM</td><td>Bailey et al.</td></tr></table>

Noteworthy is that the professional literature makes it clear that the responsibility for adopting sound accounting policies, maintaining an adequate internal control system, and making fair representations in the financial statements rests with management rather than with the auditors 3,11 . However, the literature does not report on expert systems that can assist managers evaluate internal control systems of their companies. There are several reasons that such systems deserve to be investigated. First, establishment and supervision of internal control systems are the responsibility of management, not auditors. Second, compared to an auditor, an organization’s manager should possess more knowledge about the company and thus have greater immediate insight into the operation of its internal control systems. And third, the evaluation of internal control systems can be done more often if it is performed by the management because auditors are usually expensive and are not available upon request.

## 3. Theoretical basis

The experimental methodology and hypotheses in this dissertation research are based on two theories:

Ž . Ž . Ž . 1 Technological Acceptance Model TAM and 2 Induced Value Approach. Several hypotheses stem from the TAM. The experimental methodology incorporates the Induced Value Approach. An overview of these theories is presented in this section.

## 3.1. Technology acceptance model TAM ( )

The TAM provides a basis for explaining the determinants of computer acceptance and user behavior 14 . The model suggests that computer usage<sup>w</sup> <sup>x</sup> is determined by two criteria, which are perceived usefulness and perceived ease of use. The Aperceived usefulnessB is defined as Athe prospective users’ subjective probability that using a specific application system will increase his or her job performance within an organizational contextB. The perceived ease of use is defined as the degree to which the prospective user expects the target system to be free of effort 14 .<sup>w</sup> <sup>x</sup>

## 3.2. Induced Õalue approach

The induced value approach was used in this experiment to induce optimal behavior from participants 34 . This approach emphasizes the importance <sup>w</sup> <sup>x</sup> of a reward mechanism to overcome possible subjective tendencies and to focus on participation. It notes that if well-designed laboratory experiments could mirror actual organizations in key aspects, then laboratory experimentation could play a very useful role. The key underlying concept in the induced value approach is that a subject’s utility is an increasing function of the monetary reward. This implies that, given everything else is equal, the participants will try to maximize their reward.

## 4. The construction of an expert system for internal control evaluations

The expert system developed in this research offers advice about weaknesses found in evaluating internal control systems in the sales and collection cycle of medium-size merchandising organizations. The prospective users are managers who are not experienced experts in auditing. The knowledge incorporated into the system represents primarily the expertise of one expert auditor who is a partner in a

Table 2

major international accounting firm. The expert has more than 10 years of experience in the area of internal control evaluation and demonstrated significant interest in the research project. The tool selected for developing the expert system was an integrated artificial intelligence environment called GURU <sup>w</sup> <sup>x</sup> 8,24 . The version 3.01 of GURU was used to implement this expert system. Construction of the expert system is outlined below.

## 4.1. Knowledge acquisition

Knowledge for the expert system was acquired via a 6-month series of interviews with the expert. The expert was asked to identify all potential weaknesses that may occur in the sales and collection cycle of a medium-size merchandising organization. The result was a list of 126 internal control weaknesses. The expert was asked further to describe, in detail, the techniques and processes he used to discover each of these weaknesses in a client’s internal control system. The reasons for each decision-making heuristic were also acquired in an attempt to develop an expert system that would be able to emulate both the expert’s knowledge and his reasoning behavior.

## 4.2. Rule set specification

Knowledge acquired from the expert was represented in sets of rules. A couple of rule examples are paraphrased in Table 2.

By processing sets of such rules, the system infers a recommendation of potential internal control weaknesses. This recommendation identifies significant internal control weaknesses discovered in the situation being evaluated and indicates resulting exposures that could occur in a user’s organization.

## 4.3. Testing

Once a prototype of the expert system had been developed, the expert was asked to test the expertise captured in the rule sets in order to ensure the validity of the system. Validation of the system is often considered the cornerstone of expert system evaluation 4 . It is the process of analyzing the <sup>w</sup> <sup>x</sup> knowledge and decision-making capabilities of the expert system 30 . Test cases were developed and <sup>w</sup> <sup>x</sup> used to examine whether the expert system did offer sufficiently good and timely advice compared to the human expert.

The test cases were generated from the manipulation of several cues for detecting the potential weaknesses in an internal control system over the sales and collection cycle. These cues were obtained from a review of auditing texts, accounting texts, and input from accounting professors and experienced auditors. To prevent any bias in designing the case studies, the expert who participated in developing the prototype expert system was not allowed to participate in generating case studies.

<table><tr><td>Rules</td><td>Remarks</td></tr><tr><td>R1PERFORM ASK1.If the function of receiving cash or cheque and the function of recording cash or cheque are performed by the same person, perform ADVICE1.</td><td>(1) ASK1 asks a user to enter the name of the person(s) who receives cash or cheque and the name of the person(s) who records cash or cheque.(2) ADVICE1 presents the recommendation of an internal.(3) Control weakness found in the organization and the reason why it is considered a weakness.</td></tr><tr><td>R2PERFORM ASK2.If the function of receiving cash or cheque and the function of recording cash or cheque are performed by persons who have a family relationship, perform ASK3.If such relationship is considered critical under the internal control concept, perform ADVICE2.</td><td>(1) ASK2 asks a user if the person(s) who receives cash or cheque and the person(s) who records cash or cheque have a family relationship.(2) ASK3 asks a user to enter the relationship of the person(s) who receives cash or cheque and the person(s) who records cash or cheque.(3) ADVICE2 presents the recommendation of an internal control weakness found in the organization and the reason why it is considered a weakness.</td></tr></table>

The expert was asked to evaluate each test case and detect its potential internal control weaknesses. Reasons for each potential weakness were also requested. Then, the prototype expert system was used to detect the potential weaknesses and offer reasons of such weaknesses as well. The results were then compared. It turned out that the expert and expert system identified similar weaknesses for each of the test cases. Where there were discrepancies, the expert reconsidered his responses and agreed that the expert system’s responses were indeed correct. Interestingly, this illustrates that an expert system can sometimes be useful even to an expert e.g., toŽ double check the expert’s reasoning ..

## 5. Examining the usefulness of the expert system

After constructing a system with the intent to use it to assist managers detect the potential weaknesses in an internal control system, an experiment was conducted to examine its utility.

## 5.1. Research model

The research model used to guide this research is illustrated in Fig. 1. Two decision aid treatments were used as values of the independent variable:

internal control evaluation with no decision aid vs. internal control evaluation with support of the expert system. Three response variables were measured as follows.

## 5.1.1. Accuracy score

Accuracy of decision-making is examined as a measure of the system’s effectiveness $[ 1 6 , 3 3 ]$ . Each weakness has a certain number of points associated with it, reflecting its importance. Some weaknesses have more points i.e., more importance than other Ž . weaknesses.

In arriving at an accuracy score, all points related to correctly identified weaknesses are added. In order to prevent the subjects from trying to detect weaknesses by guessing, they were informed at the beginning of the experiment that one-third of all points for inaccurately identified weaknesses will be subtracted as the penalty for guessing. Non-response for a potential weakness results in neither addition nor subtraction.

## 5.1.2. Time per accuracy score

The time used to make correct decisions i.e.,Ž time per accuracy score was examined as a measure. of the system’s efficiency. The time per accuracy score was computed as follows:

Time Used to Perform Task

Accuracy Score

Table 3 illustrates how to calculate the Time per Accuracy Score.

## 5.1.3. Participant satisfaction with the expert system

A post-experiment questionnaire was used to measure the participant satisfaction with the expert system. Seven-point Likert scales were used in the questionnaire. It is important to note that subjects received no feedback concerning their accuracy or speed prior to completing the questionnaire. The following questions were asked to measure satisfaction:

![](/api/attachments/ZANMVVRM/fulltext/images/2a29e6b3f7c5c49325173fcbda96e0eb3a4836f7f71f888cbe057f11a636364f.jpg)  
Fig. 1. Research model.

Table 3  
Calculation of time per accuracy score

<table><tr><td>Examples</td><td>Calculation of time per accuracy score</td></tr><tr><td>1</td><td>Mr. A correctly detects five weaknesses and incorrectly identifies five weaknesses.The time used to do the case is 40 min.Assuming that each weakness has three points associated with it, the accuracy score is  $10 = ((5 \times 3) - (5 \times 3)/3)$ .The time per accuracy score is  $4 = (40/10)$  min per accuracy score.</td></tr><tr><td>2</td><td>Mr. B detects four correct weaknesses, three incorrect weaknesses, and three non-responses.The time used to do the case is 40 min.Assuming that each weakness has three points associated with it, the accuracy score is  $9 = ((4 \times 3) - (3 \times 3)/3)$ .The time per accuracy score is  $4.4 = (40/9)$  min per accuracy score.</td></tr></table>

v On a scale of 1 very difficult to 7 very easy , Ž . Ž . how difficult was it to use the expert system?

v On a scale of 1 strongly disagree to 7 strongly Ž . Ž agree , do you agree that using the expert sys-. tem helps improve the accuracy of your answers to the case study?

v On a scale of 1 strongly disagree to 7 stronglyŽ . Ž agree , do you agree that using the expert sys-. tem helps reduce the time you used to answer the case study?

Based on the foregoing research model, the experiment was designed to allow testing of the hypotheses presented in Table 4.

Hypothesis H1 was tested to examine if use of the expert system can help improve the accuracy of a participant in detecting internal control weaknesses. Hypothesis H2 was tested to examine if the use of the expert system can help reduce the time used by a participant in accurately detecting the internal control weaknesses. Hypotheses H3a, H3b, and H3c are based on the Technology Acceptance Model TAMŽ . <sup>w</sup> <sup>x</sup> 14 . The TAM suggests that a computer system’s usage is determined by the behavioral intention to use such a system, which is jointly determined by the attitudes toward using the system and the perceived usefulness of the system. Therefore, these hypotheses were tested to assess the attitude of the participants in using the expert system.

## 5.2. Preparing for the experiment

Aside from the expert system itself, the experiment required the preparation of several additional items that were to be used by subjects in performing the experimental task: a list of internal control weaknesses, three internal control case studies, and a questionnaire.

Table 4

<table><tr><td colspan="2">Table 4Hypotheses</td></tr><tr><td>Hypotheses</td><td>Descriptions</td></tr><tr><td>H1</td><td>With the expert system, participants can detect potential weaknesses of an internal control system more accurately than without the expert system.</td></tr><tr><td>H2</td><td>With the expert system, participants can accurately detect potential weaknesses of an internal control system more quickly than without the expert system.</td></tr><tr><td>H3a</td><td>Participants perceive that it is not difficult to use the expert system.</td></tr><tr><td>H3b</td><td>Participants agree that using the expert system helps improve the accuracy of their answers to the case study.</td></tr><tr><td>H3c</td><td>Participants agree that using the expert system helps reduce the time they used to answer the case study.</td></tr></table>

A list of internal control weaknesses was developed from a review of auditing texts, accounting texts, and input from accounting professors and experienced auditors. Two experienced auditors and two accounting professors were asked to evaluate each weakness and assign a score to each weakness in this list using a scale of 0 to 10 based on the degree of importance of each weakness 0—the least Ž important, 10—very important . The average of the . scores for each weakness i.e., divided by four wasŽ . assigned as its importance. As described previously, importance scores for the weaknesses are used in assessing participants’ performances in internal control weakness recognition.

Three case studies A, B, and C were generatedŽ . from the manipulation of several cues for detecting the potential weaknesses in internal control systems. As with the test cases, these cues were obtained from a review of auditing texts, accounting texts, and input from accounting professors and experienced auditors. In each case, the scenario dealt with the adequacy of internal control over a company’s sales and collection cycle. These case studies also included the background information about the company and a partial organization chart that applies to each scenario. Each case study contained 10 potential weaknesses in an internal control system. Three experienced auditors and three managers were asked to pilot test these case studies to ensure their similarity with respect to the degree of difficulty in detecting the potential internal control weaknesses. Revisions to these case studies were made based on the feedback they provided.

Questionnaires were developed to gather data about participants’ perceptions of their experiences in using the expert system, as well as their demographics. These questionnaires were pretested to ensure their clarity.

## 5.3. Conducting the experiment

Because the main purpose of this study is to investigate whether an expert system can be devised to assist managers detect potential weaknesses of internal control systems in their organizations more efficiently and<sup>r</sup>or more effectively, the subjects were managers in client firms of three national accounting firms. Three lists of potential subjects were obtained from three international accounting firms. Then, one hundred and forty subjects were randomly selected from those lists. To gain subjects’ cooperation, the invitation letter explained clearly the importance of the study and assured confidentiality. All subjects were also told that they would receive a summary of this study.

The experiment was conducted in a conference room and laboratory room of a college, providing an isolated and controlled environment for the study. There were 50 participants in the experimental group Ž . 50% participation rate and 15 in the control group Ž . 37.5% participation rate . These participants served as internal control decision makers. No participants had either specific background in internal control concepts or prior hands-on experience with an expert system. Table 5 shows the industries represented by the participants.

Participants had up to 15 years of experience with their organizations, with the average being 6.5 years. The percentage of their management duties ranged from 10 to 90 with an average of 48. The number of employees in their organizations ranged from 3 to 32,000 with an average of 814. Table 6 indicates the diversity of the participants’ roles.

Table 5  
Organizations’ industries

<table><tr><td>Industries</td><td>No. of subjects in experimental group</td><td>No. of subjects in control group</td></tr><tr><td>Consultant</td><td>11</td><td>1</td></tr><tr><td>Legal</td><td>8</td><td></td></tr><tr><td>Manufacturing</td><td>7</td><td>1</td></tr><tr><td>Government</td><td>3</td><td>8</td></tr><tr><td>Insurance</td><td>3</td><td></td></tr><tr><td>Banking</td><td>2</td><td></td></tr><tr><td>Construction</td><td>2</td><td></td></tr><tr><td>Distribution</td><td>2</td><td></td></tr><tr><td>Mining</td><td>2</td><td></td></tr><tr><td>Transportation</td><td>2</td><td></td></tr><tr><td>Education</td><td>1</td><td>2</td></tr><tr><td>Finance</td><td>1</td><td>2</td></tr><tr><td>Others</td><td>6</td><td>1</td></tr><tr><td>Total</td><td>50</td><td>15</td></tr></table>

Participants’ titles  
Table 6

<table><tr><td>Title</td><td>No. of subjects in experimental group</td><td>No. of subjects in control group</td></tr><tr><td>Finance and Accounting Manager</td><td>8</td><td>1</td></tr><tr><td>General Manager</td><td>6</td><td>1</td></tr><tr><td>Supervisor</td><td>6</td><td>4</td></tr><tr><td>Director</td><td>4</td><td>1</td></tr><tr><td>Senior Analyst</td><td>4</td><td></td></tr><tr><td>Assistant Manager</td><td>3</td><td>3</td></tr><tr><td>Vice President</td><td>2</td><td></td></tr><tr><td>Tax Manager</td><td>2</td><td></td></tr><tr><td>Administrative Manager</td><td>2</td><td>4</td></tr><tr><td>Legal Manager</td><td>2</td><td></td></tr><tr><td>Chief Accountant</td><td>2</td><td></td></tr><tr><td>Engineer</td><td>2</td><td></td></tr><tr><td>System Analyst</td><td>2</td><td></td></tr><tr><td>Lawyer</td><td>2</td><td></td></tr><tr><td>Marketing Manager</td><td>1</td><td>1</td></tr><tr><td>Operating Manager</td><td>1</td><td></td></tr><tr><td>Joint Venture Manager</td><td>1</td><td></td></tr><tr><td>Total</td><td>50</td><td>15</td></tr></table>

## 5.4. Experimental task

The experiment consisted of three sessions. Prior to the experiment, the three case studies were randomly assigned to the sessions, yielding the result of Case A being assigned to Session I, Case B to Session III, and Case C to Session II. In each session, participants were asked to play the role of a manager trying to detect the potential weaknesses of the internal control system described in a case study. The maximum time allowed for each session was two hours. In Session I, participants performed the case study Case A without any decision aid. Be- Ž . cause no participant has any specific background in internal control concepts, a list of possible 126 internal control weaknesses was provided in this session. The time taken to make a decision about which weakness existed was measured and the accuracy score was calculated. In Sessions II and III, participants performed the second and third case studies Ž . Case C and Case B, respectively with the expert system for each session; the time taken to make a decision was measured and the accuracy score was calculated. At the end of each of Sessions II and III, the questionnaire was given to measure participant satisfaction with the use of the expert system.

In order to assess whether changes either betterŽ or worse in participants’ performances were due to. use of the expert system or due to learning through the practice of three consecutive cases, fifteen participants served as a control group. These participants performed the same session cases as the experimental group, but without any exposure to the expert system.

A performance-based reward mechanism is crucial for laboratory experiments because it creates a more realistic environment and gives subjects incentives to perform 34 . A performance-based reward<sup>w</sup> <sup>x</sup> system was used here to induce optimal participant behavior and reduce problems due to guessing. Participants were told that their performances across the series of cases would be used to calculate two scores: an accuracy score and a time per accuracy score. They were informed that prizes would be given to those participants attaining the highest accuracy scores and to those attaining the best time per accuracy scores.

## 6. Experimental findings

Because subjects were randomly assigned to each group, two ANOVA were performed on the first session to ensure the homogeneity of subjects on internal control knowledge between the experimental group and the control group. The ANOVA were performed to test for differences in Accuracy Score and Time per Accuracy Score between the groups. At an alpha level of 0.05, no significant difference was found between the groups.

In order to test the hypotheses, we compared the performances of participants in Session I with their performances in Session III. There were two major reasons why the performances in Session III were used instead of Session II. First, because no participants have a hand-on experience in using the expert system, the accuracy scores in Session II might not reflect their actual competency. These scores might be reduced due to unfamiliarity with using the expert system. Second, the time measured in Session II could not be considered as the actual decision time because part of it might be considered as being used to learn about interacting with the expert system. Therefore, we felt that it was most appropriate to compare Session I vs. Session III. A t-test was employed to test whether sample means were distinct for the hypotheses H1, H2, H3a, H3b, and H3c. Table 7 illustrates the operationalization of these hypotheses to be tested.

T<sub>a</sub>bl<sub>e</sub> 7  
O<sub>pera</sub>ti<sub>ona</sub>li<sub>za</sub>ti<sub>on</sub> <sub>o</sub>f h<sub>ypo</sub>th<sub>eses</sub>

<table><tr><td>Ha</td><td>Descriptions</td><td>Operationalization of Hypotheses</td></tr><tr><td>H1</td><td>With the expert system, participants can detect potential weaknesses of an internal control system more accurately than without the expert system.</td><td> $H1_0: \mu_I \geq \mu_{III}; H1_a: \mu_I < \mu_{III}.$  $\mu_I = \text{the mean of accuracy scores in Session I}.$  $\mu_{III} = \text{the mean of accuracy scores in Session III}.$ We predicted that, on the average, participants could better detect potential weaknesses of an internal control system with the expert system than without the expert system. This prediction could be confirmed if the null hypothesis was statistically rejected.</td></tr><tr><td>H2</td><td>With the expert system, participants can accurately detect potential eaknesses of an internal control system more quickly than without the expert system.</td><td> $H2_0: \mu_I \leq \mu_{III}; H2_a: \mu_I > \mu_{III}.$  $\mu_I = \text{the mean of time per accuracy scores in Session I}.$  $\mu_{III} = \text{the mean of time per accuracy scores in Session III}.$ We predicted that, on the average, participants can accurately detect potential weaknesses of an internal control system more quickly with the expert system than without the expert system. This prediction could be confirmed if the null hypothesis was statistically rejected.</td></tr><tr><td>H3a</td><td>Participants perceive that it is not difficult to use the expert system.</td><td> $H3a_0: \mu_{III} \leq 4; H3a_a: \mu_{III} > 4.$  $\mu_{III} = \text{the mean of responses in Session III to the question “On a scale of 1 (very difficult) to 7 (very easy), how difficult was it to use the expert system?”}$  $4 = \text{a neutral response to the question}.$ We predicted that, on the average, participants would not experience difficulty in using the expert system. This prediction could be confirmed if the null hypothesis was statistically rejected.</td></tr><tr><td>H3b</td><td>Participants agree that using the expert system helps improve the accuracy of their answers to the case study.</td><td> $H3b_0: \mu_{III} \leq 4; H3b_a: \mu_{III} > 4.$  $\mu_{III} = \text{the mean of responses in Session III to the question “On a scale of 1 (strongly agree), do you agree that using the expert system helps improve the accuracy of your answers to the case study?”}$  $4 = \text{a neutral response to the question}.$ We predicted that, on the average, participants would be satisfied that using the expert system helps improve the accuracy of their answers to the case study. This prediction could be confirmed if the null hypothesis was statistically rejected.</td></tr><tr><td>H3c</td><td>Participants agree that using the expert system helps reduce the time they used to answer the case study.</td><td> $H3c_0: \mu_{III} \leq 4; H3c_a: \mu_{III} > 4.$  $\mu_{III} = \text{the mean of responses in Session III to the question “On a scale of 1 (strongly agree), do you agree that using the expert system helps reduce the time you used to answer the case study?”}$  $4 = \text{a neutral response to the question}.$ We predicted that, on the average, participants would be satisfied that using the expert system using the expert system helps reduce the time they use to answer the case study. This prediction could be confirmed if the null hypothesis was statistically rejected.</td></tr></table>

## 7. Results and discussion

The major findings for the experimental group are summarized in Table 8, which shows means and t-test results pertaining to the hypotheses. All hypotheses are supported at a 0.01 level of significance. Results for the control group are shown in Table 9 for comparison. Means for Session II are also shown in both tables. Although they are not used in testing the hypotheses, their values are consistent with our expectation that the potential benefits of the expert system would not be fully realized upon the subjects’ first exposure to it.

Regarding hypothesis H1, Session I vs. Session III results show that with the expert system, participants could detect internal control weaknesses significantly more accurately than without the expert system $( \mu _ { \mathrm { I } } = 4 . 5 7 5$ vs. $\mu _ { \mathrm { I I I } } = 2 7 . 4 7 3 )$ . The corresponding lack of an increase in the accuracy score for the control group $( \ l ( \mu _ { \mathrm { I } } = 8 . 5 8 4$ vs. $\mu _ { \mathrm { I I I } } = 3 . 5 9 0 )$ strongly suggests that the increase in the mean accuracy score for the experimental group was not the result of learning that may have accrued from having the participants perform three consecutive cases. The t-test confirms that there was a significant difference in participants’ accuracy in detecting an internal control weakness when they performed the task with the expert system in Session III vs. without the Ž <sup>22</sup> expert system in Session I p-value<sup>s</sup>1.219e ..

Concerning hypothesis H2, Session I vs. Session III results show that with the expert system, participants could accurately detect internal control weaknesses significantly more quickly than without the expert system. The mean of times divided by the mean of accuracy scores for the Session I is 25.598, while the mean of times divided by the mean of accuracy scores for the session III is 3.924. The lack of a comparable decline in mean of time per mean of accuracy scores in the control group $( \mu _ { \mathrm { I } } = 1 3 . 7 4 7$ vs. $\mu _ { \mathrm { I I I } } = 1 6 . 9 6 2 )$ strongly suggests that the improvement in mean of time per mean of accuracy score for the experimental group was not the result of learning effects due to having the participants perform three consecutive cases.

Table 8  
Summary of findings in the experimental group

<table><tr><td rowspan="2">Experimental group (49 participants)a</td><td>Session I</td><td>Session II</td><td>Session III</td><td rowspan="2">Ho</td><td rowspan="2">p-Value Session I vs. Session III</td></tr><tr><td>Participants perform case A with a list of internal control weaknesses</td><td>Participants perform case C with the expert system</td><td>Participants perform case B with the expert system</td></tr><tr><td>Mean of accuracy score (the range is -20 to 38)</td><td>4.575</td><td>15.459</td><td>27.473</td><td>H1</td><td> $1.21e^{-22} * *$ </td></tr><tr><td>Mean of time</td><td>117.102</td><td>120</td><td>107.816</td><td>n/a</td><td></td></tr><tr><td>Mean of time per; mean of accuracy score</td><td>25.598</td><td>7.762</td><td>3.924</td><td>H2</td><td> $2.182e^{-09b, * *}$ </td></tr><tr><td>Mean of participants&#x27; attitude on the difficulties of using the expert system (1—very difficult, 7—very easy)</td><td></td><td>4.74</td><td>5.04</td><td>H3a</td><td> $5.109e^{-07} * *$ </td></tr><tr><td>Mean of participants&#x27; agreement that using expert system can help improve their accuracy accuracy (1—strongly disagree, 7—strong agree)</td><td></td><td>5.38</td><td>5.36</td><td>H3b</td><td> $4.647e^{-10} * *$ </td></tr><tr><td>Mean of participants&#x27; agreement that using the expert system can help reduce their decision time (1—strongly disagree, 7—strong agree)</td><td></td><td>5.36</td><td>5.44</td><td>H3c</td><td> $9.925e^{-10} * *$ </td></tr></table>

Table 9  
Summary of findings in the control group

<table><tr><td rowspan="2">Control group (15 participants)</td><td>Session I</td><td>Session II</td><td>Session III</td><td rowspan="2">Ho</td><td rowspan="2">p-Value Session I vs. Session III</td></tr><tr><td>Participants perform case A with a list internal control weaknesses</td><td>Participants perform case C without the expert system</td><td>Participants perform case B without the expert system</td></tr><tr><td>Mean of accuracy score</td><td>8.584</td><td>5.153</td><td>.950</td><td>H1</td><td>0.052</td></tr><tr><td>Mean of time</td><td>118</td><td>77</td><td>67</td><td>n/a</td><td></td></tr><tr><td>Mean of timer per; mean of accuracy score</td><td>13.747</td><td>14.942</td><td>16.962</td><td>H2</td><td>0.993</td></tr></table>

Because some participants obtained a 0 accuracy score, a t-test cannot be run directly to test if there was a significant difference in the mean of time per accuracy score between the sessions i.e., the timeŽ cannot be divided by zero . In order to solve this. problem, a positive theoretical minimum score 20Ž . was added to each participant’s accuracy score. The result is referred to as an adjusted time per accuracy score. The result of conducting a t-test using these adjusted time per accuracy scores confirms that there was a significant difference in the time that participants used to accurately detect internal control weaknesses with expert system support vs. without the expert system $\left( { p \mathrm { - v a l u e } } = 2 . 1 8 2 \mathrm { e } ^ { - 0 9 } \right)$ .

Regarding hypotheses H3a, H3b, and H3c, the participants’ answers to the post-experiment questions reveal satisfaction with using the expert system. The results show their attitudes toward the using of the expert system as follows:

v It is not difficult to use the expert system $( \mu _ { \mathrm { I I I } }$ $= 4 . 8 9 , \ p \mathrm { - v a l u e } = 5 . 1 0 9 \mathrm { e } ^ { - 0 9 } )$ .

v They agree that using the expert system helps improve the accuracy of their answer to the case study $( \mu _ { \mathrm { I I I } } = 5 . 3 7 , \ p \mathrm { - v a l u e = 4 . 6 4 7 e ^ { - 1 0 } } )$

v They agree that using the expert system helps reduce the time they used to answer the case study $( \mu _ { \mathrm { I I I } } = 5 . 4 0 , \ p \mathrm { - v a l u e } = 9 . 9 2 5 \mathrm { e } ^ { - 1 0 } )$ .

Recall that these perceptions are not influenced by any knowledge of actual performance in any of the experimental sessions.

## 8. Conclusions, limitations, and directions of future research

This research is just the initial investigation of the use of an expert system to assist managers who are not auditing experts in detecting potential internal control weaknesses. The primary finding of this study is that it is feasible to build such an expert system. The managers participated in this study have demonstrated a high interest in using the system. Installing this kind of system might let organizations save time and money by allowing weaknesses in internal control systems to be detected and solved more quickly. This type of system could help in maintaining an effective internal control system, thus providing more reliable accounting data and more safeguarding of assets. Such a system can also be beneficial for auditing firms by facilitating more reliable internal control in client firms, thereby reducing planned detection risk i.e., less work and time .Ž .

The scope of this research study may limit the generalizability of the results in several respects. First, this research concentrates only on the evaluation of controls commonly found in sales and collection cycle. Second, it investigates internal control systems commonly found in the merchandising industry. It is not expected to handle novel uncom-Ž monly different accounting systems. Third, the.

knowledge of the expert system developed for this study is based primarily on one auditor who is a partner of an international accounting firm. The resulting system closely represents his reasoning about internal control evaluation. Thus, the system’s knowledge may be firm-specific or expert-specific. These limitations point to directions in which the research presented here can be extended by future investigations.

The future research might try to investigate the results of using the expert systems over a long period of time e.g., conducting additional sessions 1 weekŽ or month after the first three sessions . Another. research avenue might investigate the use of such an expert system as a training tool, instead of as the direct decision aids presented in this paper. Researchers might try to incorporate additional transaction cycles, industries, or other auditing functions into the expert system. They might attempt to develop additional expert systems by acquiring the expertise from an internal auditor instead of the external auditor. They might try to acquire the expertise from multiple auditors and then conduct experiments similar to the one reported here. Finally, researchers might investigate the feasibility of integrating this kind of expert system with the company’s databases.

## References

<sup>w</sup> <sup>x</sup> 1 American Institute of Certified Public Accountants. Codification of Statements on Auditing Standards, American Institute of Certified Public Accountants, New York, 1994.

<sup>w</sup> <sup>x</sup> 2 American Institute of Certified Public Accountants, Codification of Statements on Auditing Standards, American Institute of Certified Public Accountants, New York, 1996.

<sup>w</sup> <sup>x</sup> 3 A.A. Arens, J.K. Loebbecke, Auditing: An Integrated Approach, 6th edn., Prentice-Hall, Englewood Cliffs, NJ, 1994.

4 B. Back, Validating an expert system for financial statement planning, J. Manage. Inf. Sys. 10 3 1994 157–177.Ž . Ž .

<sup>w</sup> <sup>x</sup> 5 A.D. Bailey Jr., G.L. Duke, J. Gerlach, C. Ko, R. Meservy, A.B. Whinston, TICOM and the analysis of internal controls, Account. Rev. 60 2 1985 186–211.Ž . Ž .

<sup>w</sup> <sup>x</sup> 6 A.D. Baily, R.P. McAfee, A.B. Whinston, An application of complexity theory to the analysis of internal control systems, Auditing: J. Pract. Theory 1 1 1981 38–52.Ž . Ž .

<sup>w</sup> <sup>x</sup> 7 A.A. Baldwin-Morgan, The Impact of Expert Systems on Auditing Firms: An Investigation Using the Delphi Tech-

nique and a Case Study Approach, PhD dissertation, Virginia Polytechnic Institute and State University, 1991.

<sup>w</sup> <sup>x</sup> 8 R.H. Bonczek, C.W. Holsapple, A.B. Whinston, Foundations of Decision Support Systems, Academic Press, New York, 1981.

<sup>w</sup> <sup>x</sup> 9 J.E. Boritz, The effect of information presentation structures on audit planning and review judgments, Contemp. Account. Res. 8 1 1985 193–218.Ž . Ž .

<sup>w</sup> <sup>x</sup> 10 C.E. Brown, M.E. Phillips, Expert systems for internal auditing, Intern. Auditor 48 8 1991 23–28.Ž . Ž .

<sup>w</sup> <sup>x</sup> 11 Committee of Sponsoring Organizations of Treadway Commission, Internal Control Integrated Framework, American Institute of CPA, New York, 1992.

<sup>w</sup> <sup>x</sup> 12 B.K. Cummings, N.G. Apostolou, Expert systems in auditing: an emerging technology, Intern. Auditing 3 2 1987Ž . Ž . 3–10.

<sup>w</sup> <sup>x</sup> 13 W. Cummings, J. Lauer, R. Baker, Expert systems in internal auditing, Intern. Auditing 4 1 1988 49–64.Ž . Ž .

<sup>w</sup> <sup>x</sup> 14 F.D. Davis, R.D. Bagozzi, P.R. Warshaw, User acceptance of computer technology: a comparison of two theoretical models, Manage. Sci. 35 8 1989 982–1003.Ž . Ž .

<sup>w</sup> <sup>x</sup> 15 J. Durkin, Expert systems: a view of the field, IEEE Expert 11 2 1996 56–63.Ž . Ž .

<sup>w</sup> <sup>x</sup> 16 M.M. Eining, P.B. Dorr, The impact of expert system usage on experiential learning in an auditing setting, J. Inf. Syst. 5 Ž . Ž .1 1991 1–16.

<sup>w</sup> <sup>x</sup> 17 C.L. Foltin, L. Garceau, Beyond expert systems: neural networks in accounting, Natl. Public Account. 41 1 1996 Ž . Ž . 26–30.

<sup>w</sup> <sup>x</sup> 18 C.L. Foltin, M.L. Smith, Accounting expert systems, CPA J. 64 11 1994 46–53.Ž . Ž .

<sup>w</sup> <sup>x</sup> 19 V.M. Gadh, R. Krishnan, J.M. Peters, Modeling internal control and their evaluation, Auditing: J. Pract. Theory 12 Ž . 1993 113–129, Supplement.

<sup>w</sup> <sup>x</sup> 20 G.F. Gal, Using Auditor Knowledge to Formulate Data Model Constraints: An Expert System for Internal Control Evaluation, PhD dissertation, Michigan State University, 1985.

<sup>w</sup> <sup>x</sup> 21 L.E. Graham, J. Damens, G.V. Ness, Developing risk advisor <sup>SM</sup> : an expert system for risk identification, Auditing: J. Pract. Theory 10 1 1991 69–96.Ž . Ž .

<sup>w</sup> <sup>x</sup> 22 J.V. Hansen, W.F. Messier Jr., A preliminary investigation of EDP-XPERT, Auditing: J. Pract. Theory 6 1 1986 109–Ž . Ž . 123.

<sup>w</sup> <sup>x</sup> 23 C.W. Holsapple, V.S. Raj, An exploratory study of two KA methods, Expert Syst. 11 2 1994 77–88.Ž . Ž .

<sup>w</sup> <sup>x</sup> 24 C.W. Holsapple, A.B. Whinston, Business Expert Systems, Irwin, Homewood, IL, 1987.

<sup>w</sup> <sup>x</sup>25 International Standard on Auditing, Risk Assessment and Internal Control, International Federation of Accountants, New York, NY, 1991.

<sup>w</sup> <sup>x</sup> 26 E.G. Jancura, Expert systems: an important new technology for accountants, Woman CPA 52 2 1990 25–28.Ž . Ž .

<sup>w</sup> <sup>x</sup> 27 S.R. McDuffie, D. Oden, E.P. Porter, Tax expert systems and future development, CPA J. 64 1 1994 73–75.Ž . Ž .

<sup>w</sup> <sup>x</sup> 28 R.D. Meservy, A.D. Bailey Jr., P.E. Johnson, Internal Control Evaluation: a computational model of the review process, Auditing: J. Pract. Theory 6 3 1986 44–74.Ž . Ž .

<sup>w</sup> <sup>x</sup> 29 W.F. Messier, J.V. Hansen, Artificial Intelligence in Accounting and Auditing, Marcus Wiener, New York, 1989.

<sup>w</sup> <sup>x</sup> 30 D.E. O’Leary, Methods of validating expert systems, Interfaces 18 6 1988 72–79.Ž . Ž .

<sup>w</sup> <sup>x</sup> 31 D.E. O’Leary, P.R. Watkins, Review of expert systems in auditing, Expert Syst. Rev. Business Account. 9 2 1989Ž . Ž . 3–22.

<sup>w</sup> <sup>x</sup> 32 R. Sharda, S.H. Barr, J.C. McDonnell, Decision support system effectiveness: a review and an empirical test, Manage. Sci. 34 2 1988 139.Ž . Ž .

<sup>w</sup> <sup>x</sup> 33 V.L. Smith, Microeconomic systems as experimental science, Am. Econ. Rev. 72 5 1982 923–955.Ž . Ž .

<sup>w</sup> <sup>x</sup> 34 A.S. Vinze, V. Karan, U.S. Murthy, A generalizable knowledge-based framework for audit planning expert systems, J. Inf. Syst. 1991 78–91 Fall 1991 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 35 R. Weber, Information Systems Control and Audit, Prentice-Hall, Upper Saddle River, NJ, 1999.
