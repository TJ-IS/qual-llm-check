---
otero_id: 20853
otero_key: "9ND7V8NW"
title: "Asynchronous implementation of the nominal group technique: is it effective?"
authors: "Karen L Dowling; Robert D St. Louis"
year: "2000"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(00)00073-7"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Asynchronous implementation of the nominal group technique: is it effective?

Karen L. Dowling, Robert D. St. Louis )

School of Accountancy and Information Management, College of Business, Arizona State UniÕersity, Tempe, AZ 85287-3606, USA

Accepted 3 April 2000

## Abstract

Two major organizational shifts are the movement toward teams and the movement toward nonstandard work schedules. This has simultaneously increased the need for meetings and decreased the ability to meet. One of the most successful processes for structuring meetings is the nominal group technique NGT . This paper provides evidence that computer-as-Ž . sisted asynchronous CAA implementations of the NGT are more effective than noncomputer-assisted synchronous NCASŽ . Ž . implementations of the NGT they generate more and better ideas, and do it in less time . The implication is thatŽ . organizations are wasting huge amounts of money on travel and accommodations for face-to-face meetings that could be conducted asynchronously. q 2000 Elsevier Science B.V. All rights reserved.

Keywords: Asynchronous communication; Group decision support system; Nominal group technique; Structured group technique; Synchronous communication; Restrictivenes

## 1. Introduction

The predominant work unit for organizations is the group; yet, it is becoming more and more difficult to arrange schedules that accommodate the meeting needs of everyone involved in these groups. For a number of reasons, group members increasingly are in different places throughout the day 6 .<sup>w</sup> <sup>x</sup> As an example, due to flex time, telecommuting, and a 24<sup>=</sup>7 work schedule, over half of the members of one IT group at a local manufacturing plant must attend their monthly group meetings on their day off. In today’s organizations, it would be helpful if employees could work asynchronously, i.e., if employees could work together without being together. Geographically distributed organizations, interorganizational units, and the fact that many individuals belong to multiple teams are additional factors contributing to the need for asynchronous work.

While there is certainly a need for asynchronous group support, the question remains: Can groups working asynchronously perform as well as groups working synchronously when making decisions?

Prior research has found that asynchronous groups struggle with the coordination of their communication, and, as a consequence, their task results suffer <sup>w</sup> <sup>x</sup> 17,32 . One approach for improving decision outcomes is to use structured group processes. The nominal group technique NGT is probably the most Ž . widely used structured group process. The NGT is designed to elicit ideas from all members of the group, and encourage consensus in the final decision making. Because it reduces process losses that can occur with groups, it generally improves decision outcomes. However, it also requires group members to meet at the same time and in the same place.

This research explores whether computer-assisted asynchronous CAA implementations of the NGT Ž . are as effective as noncomputer-assisted synchronous Ž . NCAS implementations of the NGT. An experiment is performed to compare the outcomes for groups that use the NGT both synchronously and asynchronously. Section 2 provides a brief review of previous research that is pertinent to asynchronous group communication. The role of structured group techniques in coordinating asynchronous communication, the system that was designed to assist groups with asynchronous communication, the hypotheses that were tested, the experiment that was designed to test the hypotheses, and the results of the experiment make up Sections 3–7, respectively. The paper concludes with a discussion of the limitations of the study and the implications of the findings for both business practices and future research.

## 2. Asynchronous group communication

Group decision making is prevalent in organizations today. When groups need to make decisions, the members usually gather at a single location, and use face-to-face discussion to reach a decision. Faceto-face communication is the most common form of communication, and, as such, is the form with which people are most comfortable. Unfortunately, it also has a long list of problems 29,36 . Asynchronous meetings — working together without being in the same place or at the same time — offer a potential solution to some of these problems. For example, it can be difficult to compose a meaningful response and still follow the conversation in face-to-face communication 18,26,36 . If a response is not made <sup>w</sup> <sup>x</sup> immediately, the opportunity may be lost as the conversation takes a new direction. Such time pressure may reduce not only an individual’s ability to contribute, but also his<sup>r</sup>her willingness to contribute to the conversation. Asynchronous communication, on the other hand, gives an individual time to consider what others have said, and to compose his or her own thoughts into more polished statements 34 .<sup>w</sup> <sup>x</sup> Also, given time, people occasionally decide that their initial thought was not pertinent to the discussion, and choose not to express it 36 .<sup>w</sup> <sup>x</sup>

Another problem with face-to-face communication is that increased group size is associated with decreased individual contributions 12 . Not only do <sup>w</sup> <sup>x</sup> most people feel more comfortable speaking in smaller groups, but there often is a time limit for meetings. From an opportunity standpoint, a group of five will have more time available for each person to speak than a group of 50. Again, because there is no time limit for individual contributions, the size of the group may not be as much of a barrier to communication for asynchronous groups 12 . Asyn- <sup>w</sup> <sup>x</sup> chronous communication allows the group size to be determined by the requirements of the task without limiting the opportunity for individuals to contribute.

Given the large number of group meetings, just the time spent coordinating and scheduling the meetings is substantial. Even more substantial are the travel and accommodation expenses associated with face-to-face meetings. Moreover, while a person is attending a face-to-face meeting, he<sup>r</sup>she is essentially unavailable to others as a resource. Asynchronous meetings have no travel or accommodation expenses, allow for much greater flexibility of scheduling, and do not make group members unavailable for other activities. Despite asynchronous communication’s potential for substantial economic benefit, it has not been studied as much as its synchronous counterpart.

Although some of the first studies of asynchronous communication did not employ formal experimental designs, they nonetheless provided valuable information. Not surprisingly, these early studies found that asynchronous groups have considerable difficulty coordinating their communication <sup>w</sup> <sup>x</sup> <sup>w x</sup> 17,32 . McCarthy et al. 22 pp. 178–179 note that Ž .

there are Athree tasks people undertake when they are communicating: synchronizing communication, maintaining structural coherence, and maintaining referents.B With asynchronous communication, all three of these tasks are problematic.

The basic problem is that asynchronous communication lacks temporal linearity. In general, understanding the full meaning of any single message requires knowing not only the messages that preceded it, but also the order of those messages. Synchronous communication contains inferential links that are carried by the proximity of the messages. Therefore, missing the most recent message s doesŽ . not prevent a listener from knowing the topic of the conversation. In asynchronous communication, on the other hand, multiple members are responding to multiple messages at multiple points in time. As a consequence, the responses to a specific message may be separated in both space and time from that message. This plethora of intervening messages can result in a conversation that is so fragmented that some members of the group have difficulty following the discussion 24 .<sup>w</sup> <sup>x</sup>

The absence of time pressure allows asynchronous groups to think about comments and compose more thoughtful responses. Unfortunately, this is not always positive. The sender of a message may become frustrated with the time lag between when a message is sent and when a response is received. Questions may even go unanswered in this dispersed environment 14,32 , which further increases frustra-<sup>w</sup> <sup>x</sup> tion and confusion 33 . Dufner et al. 14 reported<sup>w x</sup> <sup>w x</sup> that their group members felt both isolated and lost. Not knowing who is participating in the discussion reduces the social presence that, with face-to-face communication, encourages group members to attend and then participate in meetings 16 . Interestingly, <sup>w</sup> <sup>x</sup> research to this point has generally looked at groups with five or fewer members.

Clearly, asynchronous communication has the potential to reduce the cost and improve the outcomes of group meetings. A major stumbling block to the widespread use of asynchronous communication appears to be the difficulty of coordinating the messages. Structured group techniques have been used to coordinate communication in face-to-face meetings. Section 3 examines structured group techniques and their applicability to asynchronous communication.

## 3. Structured group processes

Structured group techniques were designed to overcome many of the difficulties associated with synchronous communication 33 . The reported re-<sup>w</sup> <sup>x</sup> sults on the success of using different structured group techniques have been mixed. One problem is that different groups adopt and adapt the techniques to different degrees. Merely having a structured group technique available does not ensure that it will be used appropriately. In an effort to explain the inconsistent results of structured group techniques, Wheeler and Valacich 35 tested different methods<sup>w</sup> <sup>x</sup> of enforcing appropriate use of the techniques. These methods are called appropriation mediators. They found that the more appropriate i.e., consistent with Ž the intention the use of the technique, the better the . decision outcome.

Appropriation mediators keep groups from using a structured technique in a manner that is inconsistent with its intended use. For example, in brainstorming groups, the intention of most structured techniques is to ensure full group participation. If groups twist a technique in such a manner as to prevent some members from contributing, that is an inappropriate use. Wheeler and Valacich 35 found<sup>w</sup> <sup>x</sup> that facilitation is the most influential mediator, even in situations where the facilitator plays a relatively weak role e.g., reminds the group of the technique’sŽ rules, but does not enforce the rules or help the group overcome any problems encountered in applying the rules ..

Inappropriate use of structured techniques may explain the lack of success that Dufner et al. 14 had<sup>w</sup> <sup>x</sup> in their attempt to incorporate structured group processes into asynchronous meetings. Subjects were provided with suggestions for structuring their meetings, but they were not required to follow the suggestions, even though the suggestions left considerable room for individual groups to conduct the meetings differently.

Ocker et al. 27 used a design task to examine the<sup>w</sup> <sup>x</sup> effects of synchronous vs. asynchronous communication on the creativity and quality of outcome for group meetings. A second experimental factor was whether the groups were given a structured process to follow. They found no significant differences in the quality of the outcomes for synchronous vs.

asynchronous groups, but did find significant differences in the creativity of the outcomes. They also found no interaction effects and no significant differences in either the quality or creativity of the outcomes for groups that used vs. groups that did not use the structured process. The authors provide two possible explanations for the ineffectiveness of the structured process: 1 the task may have had an Ž . obvious solution, so the groups did not need to use a structured process; 2 the structured process that Ž . was used may have been inappropriate for asynchronous communication.

Given that asynchronous groups struggle with coordinating their communication, and given that many structured group techniques are designed specifically to coordinate communication, it seems that asynchronous groups should benefit from using a structured technique. The results of Wheeler and Valacich 35 suggest that the structured group pro- <sup>w</sup> <sup>x</sup> cess must be appropriately used by the asynchronous group, and the results of Ocker et al. 27 suggest <sup>w</sup> <sup>x</sup> that the structured group process must be appropriate for asynchronous communication. These criteria were used to design the system that is described in Section 4.

## 4. A system for asynchronous group support

Message coordination is a major difficulty for asynchronous communication. Addressing this issue, Hiltz et al. 17 note that<sup>w</sup> <sup>x</sup> Athere are three major means of providing coordination for asynchronous groups: an explicit ‘agenda,’ or suggested process, to structure the group’s interaction; the presence of a human facilitator, leader, moderator, or ‘chauffeur’; and GDSS toolsB Ž . p. 145 . Each of these means of coordination has been studied outside the realm of asynchronous research. The findings, and how they were used to design the system described in this paper, are discussed below.

One method of improving coordination in faceto-face group meetings is to follow a structured process 26 . Many structured group processes have <sup>w</sup> <sup>x</sup> been developed, and it is critical to use a technique that is appropriate for the given task for a compre-Ž hensive review of commonly used techniques, see

Ref. 33 . To explore the question of whether asyn- <sup>w</sup> <sup>x</sup>. chronous groups can perform as well as synchronous groups, a planning task was selected. This is a common business task, and one for which the NGT was specifically developed 11 . The NGT has been<sup>w</sup> <sup>x</sup> found to increase the number of alternatives considered, improve the thoroughness with which alternatives are evaluated, and increase group commitment to the alternative that is selected 4 .<sup>w</sup> <sup>x</sup>

Another method of providing coordination for face-to-face meetings is to include a facilitator. Facilitators are an integral component of meeting success, even when groups use computerized decision support systems 3,5,7,8,15 . The term ‘facilitator’ has been<sup>w</sup> <sup>x</sup> used to refer to several distinctly different functions <sup>w</sup> <sup>x</sup> 13 . In this paper, the term refers to a person who has technical knowledge of both the structured group process and the computerized decision support system if one is used , but is not a member of the Ž . group.

Facilitators of face-to-face groups provide guidance in following a structured technique and, in that way, help synchronize the communication. Since distributed and asynchronous meeting environments require even more process structure than face-to-face meeting environments 8,17,31 , asynchronous com- <sup>w</sup> <sup>x</sup> munication should benefit from a facilitator. In fact, since facilitators affect the faithful appropriation of structured techniques, and since faithful appropriation affects the quality of decision outcomes, it seems critical to include facilitators in asynchronous meetings.

The role of the facilitator for asynchronous groups can be partially filled by semi-structured messages. Malone et al. 21 proposed the use of semi-struc-<sup>w</sup> <sup>x</sup> tured messages — also called message frames or templates — as a way to filter incoming information and structure outgoing messages. A message frame is similar to a form. For example, announcements of upcoming conferences all contain similar information: title or topic, date, place of the conference, etc. Instead of reading every field, persons receiving the information may look first at the title and then decide if they are interested in reading the rest of the message. People naturally process much information in this manner 10 . Using semi-structured messages <sup>w</sup> <sup>x</sup> allows people to save time by reading only the most relevant messages.

Malone et al. 20 briefly mentions the possibility <sup>w</sup> <sup>x</sup> of using semi-structured messages to aid group meetings, but the idea is not developed further. Using message frames with asynchronous communication provides much needed structure. More specifically, message frames:

1. Provide contextual, structural information that reduces the amount of information that the sender must include in the message;

2. Make it easier for the receiver to immediately identify the nature of the message, since the receiver knows exactly where to look for content on the standardized frames;

3. Provide inferential links between messages that, due to the non-sequential order of the messages, are otherwise difficult to construct in asynchronous communication; and

4. Define the context, or referent, of messages that otherwise might become obscure due to the time lag between messages among different group members.

Each message frame can include directions for what is expected of the group member at that time. Generally, this is information about the group process that, in a face-to-face meeting, would be provided by the facilitator, such as when that task is due, and what the next task will be including infor-Ž mation on what the member can expect to see from the other group members . This process guidance is . important in helping the group to navigate the structured group technique, and thus helps in faithful appropriation of the technique 35 .<sup>w</sup> <sup>x</sup>

Message frames provide not only process guidance, but also process restrictiveness, i.e., they can restrict the group’s selection of tools to be consistent with the intention of the structured process. Silver <sup>w</sup> <sup>x</sup> 30 discusses a similar concept in terms of individual decision support systems. The system can direct or restrict the users’ actions, further encouraging faithful appropriation of the structured technique.

One of the important functions a facilitator performs with face-to-face groups is determining when the meeting should move to the next stage of the process. With asynchronous groups, the facilitator makes this decision and implements the change by making the appropriate message frames available to the group. One of the difficulties of facilitating asynchronous meetings is being available around the clock for the duration of the meeting. The system presented here embeds some of the facilitator’s functions in the interface, which allows the facilitator to monitor the asynchronous meeting only occasionally rather than constantly.

In unstructured asynchronous environments, subjects usually are allowed to enter the discussion whenever they want, and as frequently as they want <sup>w</sup> <sup>x</sup> 17 . In that environment, subjects see the contributions made up to that point in time. Without a cutoff time for contributions, each subsequent entrant to the conversation sees a different view of the discussion. With synchronous communication, on the other hand, every member of the group has an identical view of the discussion as it proceeds. To provide identical views of the discussion for asynchronous groups, members must always be working within the same stage of the NGT. Thus, every member sees each member’s response only when a stage is completed. Between stages are facilitative pauses or breaks that allow the facilitator to combine the contributions of individuals and present the additional frames necessary for the next stage. Table 4 in Section 6 shows how the NGT was implemented for both the NCAS groups and the CAA groups.

Implementing structure through the computer interface is consistent with decision support system theory. In this context, it is important to distinguish between structuring the decision process and executing the decision process. The former focuses on the meta-decision of what process to use, while the latter focuses on selecting the best alternative for a specific decision situation. By providing users with a highly restrictive system, the designer makes the meta-decision of which decision process to use 30 . A draw-<sup>w</sup> <sup>x</sup> back to using a restrictive system is that it limits the types of tasks for which the system may be used. However, it does not limit the execution of the decision process, and therefore, the system may be used repeatedly for the same type of task.

McCarthy et al. 22 discussed using semi-struc-<sup>w</sup> <sup>x</sup> tured messages in a dispersed synchronous communication environment, but concluded it would take too much time to develop all the necessary frames. This problem can be overcome by structuring the communications. This limits the library of required message frames to only those predefined by the meeting technique. This restrictiveness should be especially good for asynchronous groups, since they need more process structure than face-to-face groups. Restricting the system also should lead to a more faithful appropriation of the system and higher levels of comfort with the system 28 .<sup>w</sup> <sup>x</sup>

Table 1  
Asynchronous communication problems and solutions

<table><tr><td>Asynchronous communication problem</td><td>Computerized support system solution</td></tr><tr><td>Lack of clarity about subject of conversation (referent)</td><td>Message frames and structured group technique</td></tr><tr><td>Lack of inferential links between messages</td><td>Message frames</td></tr><tr><td>Time lag between messages and responses</td><td>Structured group technique</td></tr><tr><td>Lack of synchronization</td><td>Facilitator</td></tr></table>

All three means — a structured technique, a facilitator, and message frames — are incorporated into the system to support asynchronous communication that is presented in this paper. Although they are discussed as three separate concepts, in the development of the system, they are inseparable. The structured group technique and facilitation are embedded in the system through the use of message frames in the form of a graphical user interface. Table 1 summarizes the special problems associated with asynchronous communication, and shows the method by which the computerized support system described in this section overcomes each problem.

## 5. Hypotheses development

The purpose of this paper is to compare CAA implementations of the NGT with NCAS implementations of the NGT. The focus of the comparison is on performance. Objective and subjective measures are developed for each performance dimension.

Table 2 lists the objective and subjective measures that are developed for each performance dimension, and the hypotheses that are associated with each measure. This section begins by discussing the objective measures and their associated hypotheses. Next, the subjective measures and their associated hypotheses are developed. The section concludes with a discussion of why no directional assumptions can be made for any of the alternative hypotheses.

## 5.1. ObjectiÕe measures and associated hypotheses

In general, increasing the number of ideas to be considered increases the quality of decisions 27 .<sup>w</sup> <sup>x</sup> For this reason, the number of ideas generated during a brainstorming session is often considered an indicator of the effectiveness of the session. Because individuals frequently generate duplicate ideas during a brainstorming session, the number of unique ideas generated is more useful than the total number of ideas generated. If CAA implementations of the NGT are as effective as NCAS implementations of the NGT, then the number of unique ideas generated in each implementation should be the same. This leads to null Hypothesis 1.1:

Table 2  
Performance dimensions and their measures

<table><tr><td>Performance dimension</td><td>Objective measure</td><td>Subjective measure</td></tr><tr><td>Effectiveness of NGT</td><td>Number of unique ideas generated (Hypothesis 1.1)</td><td>Subjects’ satisfaction with opportunity to contribute (Hypothesis 1.2)</td></tr><tr><td>Time required to reach a decision</td><td>Time to reach decision (Hypothesis 2.1)</td><td>Subjects’ satisfaction with time to decision (Hypothesis 2.2)</td></tr><tr><td>Quality of ideas generated</td><td>Quality of ideas generated (Hypothesis 3.1)</td><td>Subjects’ satisfaction with decision quality (Hypothesis 3.2)</td></tr></table>

$\mathbf { H _ { 0 } }$ 1.1. There is no difference between the total number of unique ideas generated by NCAS implementations of the NGT and the total number of unique ideas generated by CAA implementations of the NGT.

Efficiency can be objectively measured by recording the time it takes groups to reach a decision. For face-to-face meetings, time to reach a decision is measured as the length of the meeting. For asynchronous meetings, time to reach a decision is measured as the sum of the lengths of time that each individual in the group is logged onto the computerized support system divided by the number of individuals in the group. This leads to null Hypothesis 2.1:

$\mathbf { H _ { 0 } }$ 2.1. There is no difference between the time it takes participants to reach a decision in NCAS implementations of the NGT and the time it takes participants to reach a decision in CAA implementations of the NGT.

With decisions that do not have a quantifiably correct answer, experts in the field may be identified and their judgments used as a measure of quality 8 . A panel of three judges in information technology determined the quality of the ideas generated by the groups in this study. These judges are academics and consultants in the information systems field and are knowledgeable not only of the technology, but also of the organizational issues involved in electronic mail e-mail privacy.Ž .

Each group’s outcome from the NGT was a set of four to eight ideas. In stage 3 of the NGT, as explained in Section 6.3, the facilitator tabulates the votes and reports back on the four ideas that receive the most votes. Because ties are possible, the number of ideas in the outcome set for each group varied from four to eight ideas. The outcome sets were presented in a different order to each rater in order to avoid introducing a bias due to evaluation weariness.

Each rater scored each idea based on its quality seeŽ Appendix C for the instructions that were given to the raters . The quality measure was a five-point. Likert-type scale 1Ž <sup>s</sup> low quality and 5<sup>s</sup>high quality . Since the number of ideas in the outcome . sets varied from four to eight, an average score was computed for each group. This leads to null Hypothesis 3.1:

$\mathbf { H _ { 0 } }$ 3.1. There is no difference between the quality of the ideas generated by NCAS implementations of the NGT and the quality of ideas generated by CAA implementations of the NGT.

## 5.2. SubjectiÕe measures and associated hypotheses

Participants’ perceptions of the opportunity to contribute ideas, the time required to make a decision, and the quality of the decision are important variables. When groups meet, it is important that all members feel that they are able to contribute ideas. If participants are unable or unwilling to contribute their ideas to a group discussion because of a dominant group member, too many group members, or any other reason, a lower-quality decision may result. The most common method of evaluating if there are barriers to communication is to ask participants if they feel they had an opportunity to contribute 6,32 .<sup>w</sup> <sup>x</sup>

Time also is a critical resource for businesses. In fact, a critical success factor for most organizations is saving time without sacrificing quality. If a technology does not either save time or improve quality, it will be abandoned. Self-reported measures of satisfaction with time expended and decision quality have been shown to be valid criteria for evaluation 32 .<sup>w</sup> <sup>x</sup>

To assess subjects’ satisfaction with opportunity to contribute, time to decision, and decision quality, a questionnaire was developed. The questionnaire is shown in Appendix B. Questions 2 and 5 were drawn from Smith and Vanecek 32 , and used to assess subject satisfaction with the opportunity to contribute ideas. Question 6 was drawn from Aldag and Power 1 , and used to assess subject satisfaction<sup>w</sup> <sup>x</sup> with the time required to reach a decision. Questions 1, 3 and 4 were drawn from Aldag and Power 1 , <sup>w</sup> <sup>x</sup> and used to assess subject satisfaction with the quality of the decision. The results from this questionnaire were used to test the following null hypotheses:

$\mathbf { H _ { 0 } }$ 1.2. There is no difference between the perceiÕed opportunity to contribute ideas of participants in NCAS implementations of the NGT and the perceiÕed opportunity to contribute ideas of participants in CAA implementations of the NGT.

$\mathbf { H _ { 0 } }$ 2.2. There is no difference between the satisfaction with time to decision of participants in NCAS implementations of the NGT and the satisfaction with time to decision of participants in CAA implementations of the NGT.

$\mathbf { H _ { 0 } }$ 3.2. There is no difference between the satisfaction with decision quality of participants in NCAS implementations of the NGT and the satisfaction with decision quality of participants in CAA implementations of the NGT.

## 5.3. AlternatiÕe hypotheses

Table 3 lists the major factors that can affect the performance measures developed in Sections 5.1 and 5.2. Table 3 also shows which implementation of the NGT has the higher level of that factor. CAA implementations of the NGT, for instance, provide a higher level of anonymity for subjects than NCAS implementations of the NGT.

The nature of the factors in Table 3, and the manner in which they interact, make it impossible to specify a direction for any alternative hypotheses, i.e., every alternative hypothesis must be of the form:

$\mathbf { H _ { a } }$ . There is a difference between the Õalue of the measure for participants in NCAS implementations of the NGT and the Õalue of the measure for participants in CAA implementations of the NGT.

Consider, for example, the effect of anonymity on the number of ideas generated. Complete anonymity in the CAA implementation of the NGT could cause participants to contribute more ideas because they need not worry about being judged 9 , but it also<sup>w</sup> <sup>x</sup> could cause participants to contribute fewer ideas since no one can tell if they spend very little time on the task 19 . Similarly, peer pressure could<sup>w</sup> <sup>x</sup> cause participants to contribute more ideas because everyone else is contributing ideas, but it also could cause participants to contribute fewer ideas because everyone wants to go home. It simply is not possible to specify a direction for any of the alternative hypotheses.

Performance measures and factors that affect them

<table><tr><td>Performance measures</td><td>Factors that affect performance measures</td><td>Implementation with higher level of factor</td></tr><tr><td rowspan="2">Number of unique ideas generated</td><td>Anonymity</td><td>CAA</td></tr><tr><td>Cognitive overload</td><td>NCAS</td></tr><tr><td>Opportunity to contribute</td><td>Evaluation apprehension</td><td>NCAS</td></tr><tr><td rowspan="2">Time required to reach a decision</td><td>Peer pressure</td><td>NCAS</td></tr><tr><td>Proximity of members</td><td>NCAS</td></tr><tr><td rowspan="2">Quality of ideas generated</td><td>Temporal linearity</td><td>NCAS</td></tr><tr><td>Time pressure</td><td>NCAS</td></tr></table>

## 6. The experiment

To compare the performance of NCAS groups with the performance of CAA groups, a laboratory experiment was performed. This section describes that experiment. First, the task that was assigned to the groups is described. Next, the subjects that were assigned to the groups are described. A discussion of the treatment that was given to each group concludes the section.

## 6.1. The task

To maximize generalizability, it is necessary to use a common organizational task. The planning task is common in most businesses. This task involves the solicitation of input from several different people on an identified problem. In an overall view of decision making, this task falls after problem identification but before consensus or implementation 23 . Within<sup>w</sup> <sup>x</sup> McGrath’s group task circumflex, this task spans two quadrants: generate the brainstorming portion and Ž . choose the selection of a subset of ideas .Ž .

For this experiment, a case was developed around the topic of e-mail privacy. The full text of the case is in Appendix A. Subjects were asked to assume that they worked for a company that was trying to develop a policy on e-mail privacy. After receiving some background information, subjects were asked to submit ideas to be included in this organizational policy. The topic of e-mail privacy was chosen for its relevance to managers in the work force as well as students in a business school. This should help foster high motivation and interest on the part of the subjects.

## 6.2. The subjects

The subjects for this experiment were 154 first year MBA students, and 15 first year MSIM Master Ž of Science in Information Management students. In. total, there were 55 females and 114 males. Demographic questionnaires revealed that the subjects, on average, had over 2 years of part-time work experience and over 6.5 years of full-time work experience. This subject population approximates the education and experience level of persons who might be asked to make a similar decision in an organization. The subjects were drawn from four different MBA classes and one MSIM class. Everyone in a given class was assigned to the same meeting environment: either a NCAS environment or a CAA environment. The CAA environment had three classes and 91 subjects 36 females and 55 males assigned to it.Ž . The NCAS environment had two classes and 78 subjects 19 females and 59 males assigned to it.Ž .

Group size has been shown to have a significant impact on the extent of process losses experienced during meetings 29,36 . One way to avoid process <sup>w</sup> <sup>x</sup> losses is to limit groups to five members 25 . How-<sup>w</sup> <sup>x</sup> ever, business groups are most often composed of seven or more members 2 . Therefore, group size <sup>w</sup> <sup>x</sup> for this research was set at a minimum of seven and a maximum of 10 members. The individuals within a given class were randomly assigned to groups. This resulted in 11 groups for the CAA environment, and 10 groups for the NCAS environment.

## 6.3. The treatments

There are two treatments for this experiment. The first is the NCAS, or face-to-face, meeting environment. This is the traditional, and still predominant, form of business meeting in which the group members come together in the same place at the same time and do not use a computer-supported communication system. For this reason, the face-to-face environment typically serves as the benchmark for performance when testing a system to aid asynchronous groups. The face-to-face meetings were directed by facilitators who used the NGT. As mentioned in Section 4, the NGT was selected because of its prevalence in practice, and its established efficiency in assisting groups with planning tasks 4 .<sup>w</sup> <sup>x</sup>

The second treatment is the CAA meeting environment. In this environment, subjects communicate over time and space using a computerized support system. The system developed for this research allows subjects to participate in the meeting when and where they choose. The NGT is implemented in the system using a meeting facilitator together with message frames in the graphical user interface. The facilitator provides assistance by compiling the sub-

Table 4 Stages in the NGT

mitted ideas, advancing the system through the different stages, and answering any questions the users have about the process or the technology. Table 4 summarizes how each stage of the NGT was implemented for the two treatments.

The NCAS treatment used five facilitators to conduct the meetings for its 10 groups. The facilitators were instructed on how to implement the NGT, and given a script to ensure consistency of tone, and content for each meeting. Each session began with a brief introduction of the NGT and the case. The subjects were then asked to fill out a brief demographic survey. When the survey was complete, the begin-time for the meeting was recorded, and the subjects were given a copy of the case and asked to read it. Appendix A contains a copy of the case.

After all of the subjects had read the case, the facilitator directed the subjects to begin silent idea generation. The nominal question and the stages of the NGT were displayed on large sheets of paper. When everyone was through writing ideas, the facilitator directed the group to the recording phase. During this phase, the facilitator went around the room in order, asking each subject for one idea and recording it on a flip chart. This process was repeated until no more ideas were forthcoming. At each iteration, subjects were allowed to pass if they had no new idea to contribute. During stage 1, discussion and speaking out of turn were not allowed.

When the group finished submitting ideas, the facilitator moved to the discussion stage. During this stage, the group was allowed to discuss any ideas that seemed ambiguous, eliminate or combine any redundant ideas, and add any additional ideas that were generated. Any group member could suggest that an idea was redundant and should be deleted, but if even one other group member disagreed, the idea was not deleted. A similar process was followed when considering rewordings and combinations. This process was continued until the group was satisfied that the ideas were unique and comprehensive. This completed stage 2a in Table 4.

As soon as the group was satisfied with its reworked list of ideas, the facilitator began the voting stage. Subjects were given five separate cards one Ž vote per card . When the votes were collected, the. end-time for the meeting was recorded. As soon as the votes were counted, the results were displayed. This completed stage 3 in Table 4. Subjects were then given the post-experiment questionnaire shown in Appendix B. Upon completion of the questionnaire, questions about the research were answered and the subjects were thanked for their participation. During each session, the time was noted for each stage, as well as how many ideas each individual submitted.

<table><tr><td>NGT stage</td><td>Group 1: NCAS</td><td>Group 2: CAA</td></tr><tr><td>(1) Idea generation</td><td>Silent idea generation. Round robin public recording of ideas. Facilitator acts as scribe.</td><td>Individual idea generation. Lists given to facilitator who collates ideas into one list.</td></tr><tr><td>(2a) Discussion</td><td>Discussion of any ambiguous ideas, deletion or combination of redundant ideas, and addition of new ideas. Decisions determined by majority. Facilitator acts as scribe and parliamentarian.</td><td>Each member looks at other members&#x27; ideas, suggests combinations, asks for clarification, and adds new ideas. Facilitator collates lists and makes any changes recommended by majority.</td></tr><tr><td>(2b) Discussion (continued)</td><td></td><td>Each member invited to respond to questions from previous stage. Facilitator makes any changes recommended by majority.</td></tr><tr><td>(3) Voting</td><td>Members silently vote for five ideas from list. Facilitator tabulates votes and displays results.</td><td>Each member votes for five ideas from revised list of ideas. Facilitator tabulates votes and records results on disks.</td></tr></table>

It was possible to use only five facilitators because the NCAS implementations were conducted in two sessions of five groups each, and the two sessions were conducted approximately 1 week apart. The NCAS subjects were drawn from two different classes: one evening MBA class groups 1–5 , and Ž . one day MBA class groups 6–10 . Students in the Ž . day and evening MBA programs have little or no contact with each other, making collusion between the two sessions very unlikely. Furthermore, subjects were asked not to discuss the case with anyone outside their session and had no incentive to collude, since there was no right or wrong answer to the experiment and all of the subjects had the required knowledge to actively participate in the experiment.

The CAA treatment used the same facilitator to conduct all 11 meetings. The facilitator met face-toface with the subjects in each group, and verbally introduced the NGT and the e-mail privacy issue. The subjects were not given a paper copy of the case, but were given a disk containing the computerized support system, the text of the case, and a schedule of deadline dates for the different stages of the NGT. Subjects were asked not to discuss the case with anyone else for purposes of research integrity.

The first time subjects used the computerized support system, they were presented with two screens containing the demographic survey questions. After the survey was completed, they were shown a brief introduction to the NGT, and then shown the text of the case. Prior to this point, time was not recorded as time logged onto the computerized support system. After the case was read or at least scanned , subjectsŽ . were able to begin recording ideas. The subjects had 2 days to record ideas and return the disk to the facilitator. This was the subjects’ first 2-day opportunity to suggest new ideas. The facilitator had 1 day to collate the ideas into a single list, and prepare new disks containing the collated list for the subjects. This completed stage 1 in Table 4.

When subjects accessed the disks from stage 1, the computerized support system displayed the group’s combined list of ideas, invited clarifications, combinations, or deletions of ideas, and asked subjects if they wished to add any additional ideas. The subjects had 2 days to request clarification of ideas, rework ideas suggest combinations or deletions ,Ž . add new ideas, and return the disk to the facilitator. This was the subjects’ second 2-day opportunity to suggest new ideas. The facilitator had 1 day to record all requests for clarification, and make any combinations, or deletions that were recommended by a majority of the members in a group. Suggested additions were automatically included on the reworked list. This completed stage 2a in Table 4.

When subjects accessed the disks from stage 2a, the computerized support system automatically displayed the group’s reworked list, and the members’ requests for clarification. The system further requested that individuals respond to the requests for clarification by other members. The subjects again had 2 days to respond to requests for clarification, suggest further combinations or deletions of ideas already on the list, or add new ideas to the list. This was the subjects’ third 2-day opportunity to suggest new ideas. The facilitator had 1 day to make any combinations, or deletions that were recommended by a majority of a team’s members. In both stages 2a and 2b, any participant could suggest the deletion or combination of an idea, but an idea was not actually deleted or combined unless a majority of the participants suggested that the idea be deleted or combined. Suggested additions, on the other hand, were automatically included on the reworked list. This completed stage 2b of Table 4.

When subjects accessed the disks from stage 2b, the computerized system automatically displayed the group’s reworked list, and asked the members to vote for the five ideas they considered to be the most important. The subjects had 2 days to vote and return the disks to the facilitator. After this point, time was not recorded as time logged onto the computerized support system. The facilitator had 1 day to count the votes, prepare disks with the tabulated results, and return the disks to the subjects. This completed stage 3 in Table 4.

After viewing the results, the subjects were asked to complete the post-experiment questionnaire that appears in Appendix B, and return the disks to the facilitator. When the disks were returned, the facilitator met face-to-face with the subjects and briefly discussed the research, answered questions, and thanked the subjects.

Within all stages of the CAA meeting environment, it was possible for subjects to exit the system and return to it at a later time. The system recorded the date and beginning and ending times whenever a subject entered the system without the subject’sŽ knowledge . Subjects were able to access the system. at home or at school, where several computer laboratories were available 24 hours a day. The computerized support system began each stage with a brief explanation of what was expected of the subject, and closed each stage with information about the next stage as well as a reminder of the schedule.

At approximately 2-day intervals, the subjects returned the disks to class where the facilitator collected them. Originally, the intention was that subjects would send and receive the files for this research via an e-mail package. Three issues prevented this: 1 at the time of the research, no e-mailŽ . package was available from the university which allowed easy attachment of files to e-mail messages; Ž . 2 a substantial number of the subjects did not have access to the university computer system from home; and 3 many of the subjects did not routinely useŽ . e-mail. It is important to note that disk swapping, instead of file transfers, did not create a disruption to the implementation of the adapted NGT. When subjects returned the disks, there was no discussion of the task. Moreover, anonymity was maintained throughout the experiment to encourage subjects to contribute ideas, and to reinforce group ownership, rather than individual ownership, of ideas and comments.

For the CAA groups, all treatments were administered during the same time period. Several steps were taken to ensure that there was no collusion between experimental subjects in the CAA groups: Ž . 1 the subjects were asked not to talk to each other; Ž . 2 the CAA subjects were not told who was in which group; and 3 care was taken to be sure the Ž . subjects did not have any incentive to collude. The fact that there was no right or wrong answer for this experiment, and the fact that all of the subjects had the required knowledge to actively participate in the experiment, both imply that subjects had little or no incentive to collude. Moreover, informal discussions with subjects revealed no collusion, and no knowledge of attempts to identify other group members.

Because half of the NCAS groups did not participate in the experiment until after the CAA groups had finished submitting ideas, collusion could have occurred between the CAA groups and these NCAS groups. However, any collusion that could have occurred would have biased the results against the CAA groups, and thus make our results even stronger than reported. Two other sources of possible bias are: 1 evening MBA students participated in theŽ . NCAS groups but not in the CAA groups; 2 MSIMŽ . students participated in the CAA groups, but not in the NCAS groups. A check on the number of ideas generated showed that the NCAS evening MBA students generated more ideas than the NCAS day MBA students an average of 21.2 vs. an average of Ž 11.8 , and that the CAA day MBA students gener-. ated more ideas than the CAA day MSIM students Ž . an average of 31.2 vs. an average of 29.5 . Here again, any biases that could have occurred would have been against the CAA groups, and thus make our results even stronger than reported.

## 7. Results

To test the six null hypotheses developed in Section 5, the first step is to perform a multivariate analysis of variance MANOVA . The six dependentŽ . variables are: number of unique ideas generated, time required to reach a decision, quality of unique ideas generated, satisfaction with opportunity to contribute, satisfaction with time to decision, and satisfaction with decision quality. There is only one factor, and it is a fixed factor with only two values: member of NCAS group, or member of CAA group. Because there are only two groups, the MANOVA reduces to Hotelling’s multivariate t-test.

The value of the F-statistic for the MANOVA is 7.21, with 6 df for the numerator and 14 df for the denominator. This gives a p-value of 0.001159. Clearly, there is a difference between the NCAS groups and the CAA groups with respect to one or more of the six dependent variables that were measured. When the null hypothesis is rejected in a MANOVA, univariate ANOVAs typically are performed on each dependent variable. Because there are only two groups, an ANOVA is equivalent to a t-test for the difference between the means for the two groups. Table 5 shows the results of the six t-tests, as well as an additional test on the total number of ideas generated. The reason for this additional test is explained below. Table 5 also contains 95% confidence limits for the differences between the means.

In Table 5, the row labeled Atotal number of ideas generatedB is the number of ideas that were on the list of ideas that was voted upon in stage 3 of the NGT. It is not the sum of the number of ideas generated by each individual, but rather the total number of ideas on the combined list that was generated by the group. Eleven groups used the CAA implementation of the NGT, and 10 groups used the NCAS implementation of the NGT. Thus, 21 values were generated for this variable.

In the CAA implementations, an idea was not actually deleted or combined unless a majority of the participants suggested that the idea be deleted or combined. Two obvious problems exist with this approach. First, if 50% of the participants suggests deleting idea A in favor of idea B, and the other 50% suggests deleting idea B in favor of idea A, then

100% of the participants feels ideas A and B are redundant, but neither idea gets eliminated. Second, it seems unlikely that a majority of the participants ever would suggest the same deletion or combination of an idea.

Even though the participants had two opportunities to delete<sup>r</sup>combine ideas in the CAA implementations as opposed to only one in the NCAS imple-Ž mentations , the above problems make it likely that. the CAA implementations contain more redundant ideas than the NCAS implementations. Note also that no provision was made in the CAA implementations for rewording ideas. There were two reasons for this: Ž . 1 participants in the CAA implementations had more time to formulate their ideas, and hence, there should be less need for rewording; and 2 it seemsŽ . impossible that a majority of the participants would suggest the same rewording for an idea. Since rewording may have clarified redundancies, the inability to reword ideas may have further contributed to the presence of redundant ideas in the CAA implementations.

To eliminate this problem, we asked an independent panel of three persons to identify redundant ideas in the final solution sets for both the CAA and the NCAS implementations. First, each member of the panel independently evaluated each solution set, and identified groups of redundant ideas. The three members then met as a group to decide which ideas should be eliminated from the sets due to redundancy. If at least two members of the panel agreed that an idea was redundant, it was eliminated. The panel eliminated a sizeable number of redundant ideas from both the CAA and the NCAS solution sets. In Table 5, the row labeled Anumber of unique ideas generatedB is the number of ideas identified as unique by this panel.

Table 5  
Two-tailed t-tests for null Hypotheses 1.1–3.2 all calculations are based on unequal error variancesŽ .

<table><tr><td>Variable</td><td>Mean for CAA groups</td><td>Mean for NCAS groups</td><td>t-value</td><td>p-value</td><td>Lower and upper 95% confidence limits for the difference in means</td></tr><tr><td>Total number of ideas generated</td><td>30.91</td><td>16.50</td><td>3.77</td><td>0.001</td><td>6.40 to 22.42</td></tr><tr><td>Number of unique ideas generated</td><td>23.91</td><td>15.60</td><td>2.87</td><td>0.010</td><td>2.30 to 14.31</td></tr><tr><td>Time to reach decision</td><td>46.99</td><td>59.00</td><td>-2.37</td><td>0.030</td><td>-22.69 to -1.34</td></tr><tr><td>Quality of unique ideas generated</td><td>3.84</td><td>3.33</td><td>2.46</td><td>0.023</td><td>0.08 to 0.94</td></tr><tr><td>Satisfaction with opportunity to contribute</td><td>2.29</td><td>2.14</td><td>0.96</td><td>0.352</td><td>-0.18 to 0.49</td></tr><tr><td>Satisfaction with time to reach decision</td><td>3.89</td><td>3.74</td><td>0.31</td><td>0.759</td><td>-0.87 to 1.17</td></tr><tr><td>Satisfaction with decision quality</td><td>3.59</td><td>3.59</td><td>-0.01</td><td>0.990</td><td>-0.65 to 0.64</td></tr></table>

Table 5 shows that, on average, the CAA groups generated more unique ideas than the NCAS groups. Even if the lower limit of the 95% confidence interval is used, the CAA groups generated nearly 15% Ž . 2.30<sup>r</sup>15.60 more ideas than the NCAS groups. If the mean difference is used, the CAA groups generated over 53% 8.31Ž . <sup>r</sup>15.60 more ideas.

The CAA groups also generated these ideas in less time than the NCAS groups. The difference in average time required to reach a decision was 12.01 min. This represents a 20% 12.01Ž . <sup>r</sup>59.00 reduction in the time required to reach a decision. If the lower limit for the 95% confidence interval is used, there still is a 2% 1.34Ž . <sup>r</sup>59.00 reduction in the time required to make a decision. Moreover, as explained in Section 6.3, only time spent during stages 1, 2, and 3 of the NGT was counted. The difference would have been much more striking if either travel time to and from meetings, or time spent arranging the meetings, were considered. On the other hand, there also was no way to capture the amount of work time, if any, that the subjects in the CAA environment spent thinking about the task when they were not using the system. This may result in an understatement of the time required to reach a decision for the CAA groups.

Table 5 further shows that the quality of the unique ideas generated is higher for the CAA groups. As explained in Section 5.1, the measure of quality was a five-point Likert-type scale 1Ž <sup>s</sup> low quality and 5<sup>s</sup>high quality . The average difference in. quality was 0.51. This difference is more difficult to interpret than the difference in the number of ideas generated or the difference in the time that was required to reach a solution. For this particular set of 21 observations, seven of the top eight outcome sets in terms of quality were from the CAA groups, i.e., 87.5% 7Ž . Ž . <sup>%</sup>8 of the top 38% 8<sup>%</sup>21 of the outcome sets was from the CAA groups.

Of course, the top eight outcome sets were deliberately picked to maximize the percent that would be from the CAA groups. It also is true that seven of the top 11 outcome sets in terms of quality were from the CAA group. A more realistic picture can be obtained by assuming that values of the quality measure for both populations are normally distributed, and that the sample means and sample standard deviations are equal to their respective population parameters. For these data, the average difference in quality of 0.51 is equal to 1.10 times the standard deviation of the values of the quality measure for the 10 NCAS groups. Given these assumptions, 50% of the values of the quality measure for the CAA groups will be greater than the mean of 3.84 that is reported in Table 5. However, only 13.5% of the values of the quality measure for the NCAS groups will be greater than 3.84, since 3.84 equals the mean 3.33 plus 1.10 standard deviations.Ž . Thus, 79% 50Ž Ž .. ŽŽ<sup>%</sup> 50<sup>q</sup>13.5 of the top 32% 50<sup>q</sup> 13.5. . <sup>%</sup> 2 of the outcome sets in terms of quality should come from the CAA groups. If the lower limit of the confidence interval for the difference is used, the result is that 53% of the top 47% of the outcome sets in terms of quality should come from the CAA groups.

Taken together, rows two through four in Table 5 indicate that, when compared to NCAS groups, CAA groups generate more and better ideas, and do it in less time. If this result can be obtained with no decrease in satisfaction on the part of the participants, then this is strong evidence that CAA implementations of the NGT are more effective that NCAA implementations of the NGT, at least for this task type and this computerized support system.

The last three rows in Table 5 show that Hypotheses 1.2, 2.2 and 3.2 cannot be rejected. There is no statistically significant difference in satisfaction with respect to the opportunity to contribute, the time required to reach a decision, or the decision quality. Although the sample sizes are small, resulting in relatively low power for the t-tests, the sample means are so similar that there is no reason to suspect that participants in the NCAS groups were more satisfied than participants in the CAA groups.

## 8. Limitations and future research

The results from this experiment strongly indicate that CAA implementations of the NGT are more effective than NCAS implementations of the NGT. The CAA groups generated more ideas and better ideas, and did it in less time than the NCAS groups. However, this study does have several limitations. This section discusses the severity of those limitations, and suggests areas for future research.

## 8.1. Limitations

Strictly speaking, the results presented in this paper hold only for the NGT, a task of determining an e-mail privacy policy, the computerized support system that was developed by the authors, group sizes of 7–10 individuals, and masters students who meet on campus. However, there are reasons to believe the results are generalizable beyond these conditions. The severity of each of these limitations is discussed below.

## 8.1.1. NGT

Both environments used facilitators and the NGT. The NGT is the most widely used structured group process, partly because it is easy to implement, and partly because it can be used in a variety of problem situations. Limiting the results of this research to situations where it is appropriate to use the NGT still allows for a wide range of problem situations.

## 8.1.2. E-mail priÕacy task

The planning task is common in most businesses. This task involves the solicitation of input from several different people on an identified problem for which there is no known solution. The e-mail privacy task used in this research is typical of this type of task. Examples of additional planning tasks to which the results of this paper are generalizable include: identifying the core steps in a business process; determining the priorities for a committee, department, or organization; developing a software adoption policy; or formulating a work life balance policy. These types of task are very pervasive in business settings.

## 8.1.3. Computerized support system

The computerized support system used in this research had a very basic user interface. Moreover, there are a limited number of ways to design a system to support asynchronous implementation of the NGT. Thus, results similar to what was obtained in this research should be obtainable from any computerized support system that has an acceptable user interface which supports faithful appropriation of the NGT.

All of these systems will have a common problem, however. Namely, there is no way to capture the amount of work time, if any, that the subjects may spend thinking about the task when not using the system. This may cause the recorded time spent on the task to be understated. On the other hand, time spent on the task in the NCAS implementations is understated considerably by not including any time for travel or interruption having to stop what Ž you are doing, go to the meeting, and then restarting what you were doing . While both treatments did not . fully capture time, it is clear that a full and accurate time reporting would increase the NCAS times to a greater extent than the CAA times, and therefore, the results reported here understate the benefits of CAA implementations.

It also is true that participants in our CAA implementations had a longer period of time in which to contribute ideas than participants in our NCAS implementations. Nevertheless, we do not feel that this biased our results in any way. This is one of the advantages of CAA implementations, and we simply measured that advantage. It could, however, affect the generalizability of our results. If a CAA implementation of the NGT allows only one opportunity or only 1 day to provide input, the results may not be the same as we observed.

## 8.1.4. Group sizes of 7–10 indiÕiduals

Process losses quickly increase as face-to-face group size increases beyond five members 25,29,36 . <sup>w</sup> <sup>x</sup> Group size for this research was set at a minimum of seven and a maximum of 10 members, because business groups almost always have seven or more members 2 . Group size would be expected to have <sup>w</sup> <sup>x</sup> a greater impact on NCAS groups than on CAA groups. Thus, one would speculate that the differences found in this study would be larger for group sizes greater than 10, and smaller for group sizes less than seven.

## 8.1.5. Masters students who meet on campus

The subjects used for this experiment met every day for classes, and were enrolled in programs that are designed to encourage and facilitate group meetings. Hence, meeting as a group posed no hardship for them. If the subjects had been dispersed over great distances, they may have found the time to decision in the asynchronous treatment even more satisfactory. This is supported by comments from the subjects in the pilot study who were not in a lock-step program. In unstructured comments after the pilot study, these participants mentioned how much they enjoyed meeting asynchronously.

The use of students can introduce biases. However, these were not undergraduate students. They were all masters level business students, composed of both females and males 55 females, 114 males ,Ž . had over 2 years of part-time work experience onŽ average , and had over 6.5 years of full-time work. experience on average . Thus, they may be slightlyŽ . younger and slightly better educated than persons likely to use the NGT in businesses, but they are not too dissimilar. Being younger and better educated may have increased their willingness to use the CAA NGT, and may have increased their satisfaction with using it. Being students may also have made it easier for them to find the time required to use the CAA NGT. However, full-time lock-step students carry 18 semester hours, and are extremely busy. Thus, any biases introduced by using students should be quite small.

## 8.2. Future research

The limitations identified above point out the need for future research in at least three areas: task types, group sizes, and facilitation types. The difficulties asynchronous groups have in coordinating their communication may amplify the criticality of the task<sup>r</sup>process fit. Additional task types beyondŽ the planning task with appropriate processes be- . Ž yond the NGT need to be studied. Where syn-. chronous groups can adapt a process, asynchronous groups may be unable to handle the additional burden of adapting the process as well as performing the task. The system developed for use in this study was specifically designed to relieve participants of the burden of coordinating communication. The use of the NGT structured the meeting and the use of message frames structured the input of the participants.

This research used commonly observed group sizes. Process losses quickly increase as face-to-face group size increases. Working asynchronously, however, may substantially increase the upper bound of effective group size. The upper limit of effective group size for CAA meetings needs to be explored, and compared with the upper limit of effective group size for computer-assisted and NCAS meetings.

The effect of the facilitation provided also needs to be explored. Clearly, the type of facilitation provided can affect the number of ideas generated, the time to reach a decision, and the quality of the decision, as well as participants’ satisfaction with opportunity to contribute, time to reach a decision, and decision quality. There is an enormous difference between the type of facilitation that occurs in a computerized decision room and the type of facilitation that occurs in a normal meeting room with flip charts. Because task type, group size, and facilitation type all interact, this will require a large number of carefully designed experiments.

## 9. Conclusions and implications

This paper provides strong evidence that, for planning type tasks, CAA implementations of the NGT are more effective than NCAS implementations of the NGT. They generate more and better ideas, and do it in less time. The paper also shows that the facilitator for asynchronous group meetings does not need to be available 24 hours a day to achieve a successful outcome. By incorporating some of the functions of the facilitator into the computerized support system, the facilitator’s role is reduced to a practical size.

These results have important managerial implications. If meeting participants do not have to come together at the same time and place, and are spending more time than is necessary in meetings, then organizations currently are wasting substantial economic resources in the form of travel expenditures and time spent arranging, traveling to, and participating in meetings. Today, groups or teams are more and more frequently composed of people from widely dispersed locations. Even when groups are composed of persons from the same office, one or more members may be away on business at the time a decision needs to be made, or the members may work different schedules. Reducing the cost of meetings is thus becoming more and more important. Group members, using a system such as the one described in this paper, can work on tasks when it best fits their individual schedule, without coming together at the same time and place, and without a loss of decision quality.

## Appendix A. Sun Phones case

## A.1. E-mail: public or priÕate?

E-mail is a pervasive form of business communication. Obviously, not all e-mail messages are work-related, but many personal messages are sent from work. Surveys have found that e-mail users believe that their messages are private and subject to the same privacy protection as the U.S. mail. Not only is this not true, but in lawsuits charging violation of privacy, the courts have consistently ruled in favor of employers who monitor e-mail or other communication. What some users do not realize is that in making back-up files of data on the network, e-mail messages are also recorded and saved. Even if the user deletes the messages promptly, these back-up files often remain in archives for weeks or months.

E-mail is so convenient and easy to use that sometimes people use it in place of face-to-face communication. For example, a co-worker might send a joke that he or she recently heard over e-mail to someone in the company rather than walking to that person’s office, especially if the sender thinks the joke might give offense if overheard. Unfortunately, what the sender may not realize is that it is also extremely easy for the receiver to distribute, even inadvertently, that message to many others.

Some companies have addressed this problem by setting up electronic bulletin boards for employees to post jokes and social messages, with the clear understanding that either the bulletin board will be controlled by a person who will delete any possibly offensive messages, or that the bulletin board is closely monitored and anyone submitting a potentially offensive message will be disciplined. In this way, the company acknowledges that informal communication between employees can be beneficial to company cohesiveness and employee morale while reminding users that their messages may be read by a wide audience.

Employers have several legitimate reasons for reading e-mail messages. An employer might want to determine the percentage of complaints about their product received by e-mail. In a service industry, an employer might check to see that employees are responding politely and accurately to customer messages. The files of a hospitalized employee might be read when co-workers have to fill in for the absent employee.

After reading disparaging remarks about herself in their e-mail files, a supervisor of Nissan threatened two employees with dismissal. The employees filed a grievance against the supervisor charging that their privacy had been violated. The employees were fired. When they brought a lawsuit against the company, the court dismissed the case on the basis that the company owned the computer system and therefore had the right to read any messages on it.

At Epson America, an employee was fired after objecting to a supervisor printing out and reading employee messages sent from the internal e-mail system to an external communications service. This case was also dismissed on the grounds that the company has the right to read the messages because it provides the system. The case is currently under appeal.

Where the courts have ruled in favor of employee privacy with regard to employer monitoring, it has been because of what the employer did with the information. For example, in Arkansas, the courts ruled for an employee when her employers informed her husband of her extramarital affair. The employers discovered the relationship while monitoring for evidence of theft. The courts ruled that while it was acceptable to monitor for business purposes, the employers had no right to give information so obtained to a third party the husband .Ž .

Without legislation directly addressing the issue of e-mail communication, there will continue to be time-consuming and expensive lawsuits. The best way for businesses to defend against costly lawsuits is to establish a corporate policy regarding e-mail Ž . and other forms of communication privacy and inform their employees of the policy. The courts take into account expectations based on corporate practices or policies. So a company can develop a policy, which is consistent with their corporate culture, and expect that it will provide protection from litigation.

Developing an e-mail policy is not simple because a delicate balance must be found between the needs of the organization and the privacy rights of individuals. A policy that is too restrictive will result in the employees feeling that Big Brother is watching and that the company does not trust them. An overly restrictive policy can even discourage the use of e-mail.

You work for Sun Phones, a manufacturer of cellular phones headquartered in Phoenix. Sun Phones has over 4000 employees at multiple sites in the southwest. The company has recently decided to develop an e-mail policy that will be distributed to all the employees as a safeguard against possible litigation. While the company feels e-mail is an efficient, low-cost method of communication, and that it would be counterproductive to discourage its proper use, it also wants to retain the right to read e-mail. Therefore, Sun Phones wants to implement a policy which informs employees under what circumstances the company might read employee e-mail messages.

Assignment: Sun Phones needs a list of circumstances which might lead to the company reading e-mail. Your group has been given that task. Your first step is to generate as many ideas as possible on the following question: Under what circumstances might Sun Phones read their employees’ e-mail?

## Appendix B. Participant post-experiment survey

For each of the following questions, please circle the number which most closely reflects your attitude.

My group's solution was a good one. Agree Disagree 1-----2----3-----4-----5-----6-----7

2. My opportunities to contribute to the discussion were Complete Incomplete 1-----2-----3-----4-----5-----6-----7

3. I'm not sure our solution was appropriate. Agree Disagree 1-----2----3-----4-----5-----6----7

4. I'm not confident about our solution. Agree Disagree 1-----2----3-----4-----5----6----7

5. My freedom to participate was Constrained Free 1-----2-----3-----4----5-----6----7

6. It took too much time to reach our decision. Agree Disagree 1-----2-----3-----4-----5-----6-----7

## Appendix C. Instructions for raters

Each of the 21 groups in the experiment generated a set of recommendations related to the question AUnder what circumstances might Sun Phones want or need to read employees’ e-mail messages?B ŽSee attached case, AE-mail: public or private?B, for further information. To evaluate each group’s perfor-. mance, I ask that you rate the quality of EACH idea using the following scale. Quality is defined beneath the scale.

Rating Scale

<table><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>low</td><td></td><td></td><td></td><td>high</td></tr><tr><td>quality</td><td></td><td></td><td></td><td>quality</td></tr></table>

Definition of quality: Consistent with and related to the nominal question AUnder what circumstances might Sun Phones want or need to read employees’ e-mail messages?B Does the idea acknowledge the company’s legal right to read e-mail messages, balanced with the company’s wish to respect their employees’ privacy? Does the idea apply to a business environment? Would it be possible for a company to implement this idea technically or with respect to personnel or other resources? Does it make sense to apply this suggestion?

## References

<sup>w</sup> <sup>x</sup> 1 R.J. Aldag, D.J. Power, An empirical assessment of computer-assisted decision analysis, Decision Sciences 17 1986 Ž . 572–588.

<sup>w</sup> <sup>x</sup> 2 R. Anson, Effects of computer support and facilitator support on group processes and outcomes: an experimental assessment, PhD Dissertation, Indiana University, 1990.

<sup>w</sup> <sup>x</sup> 3 R. Anson, R. Bostrom, B. Wynne, An experiment assessing group support system and facilitator effects on meeting outcomes, Management Science 41 1995 189–208.Ž .

<sup>w</sup> <sup>x</sup> 4 J.M. Bartunek, J.K. Murnighan, The nominal group technique: expanding the basic procedure and underlying assumptions, Group and Organization Studies 9 1984 417–Ž . 432.

<sup>w</sup> <sup>x</sup> 5 R.P. Bostrom, R. Anson, V.K. Clawson, Group facilitation and group support systems, in: L.M. Jessup, J.S. Valacich Ž . Eds. , Group Support Systems: New Perspectives, Macmillan, New York, 1993, pp. 146–168.

<sup>w</sup> <sup>x</sup> 6 K. Burke, L. Chidambaram, Developmental differences between distributed and face-to-face groups in electronically supported meeting environments: an exploratory investigation, Group Decision and Negotiation 4 1995 213–233.Ž .

<sup>w</sup> <sup>x</sup> 7 K. Cass, T.J. Heintz, K.M. Kaiser, Using a voice-synchronous GDSS in dispersed locations: a preliminary analysis of participant satisfaction, Proceedings of the 24th Annual Hawaii International Conference on Systems Sciences 3 Ž .1991 554–563.

<sup>w</sup> <sup>x</sup> 8 L. Chidambaram, B. Jones, Impact of communication medium and computer support on group perceptions and performance: a comparison of face-to-face and dispersed meetings, Management Information Systems Quarterly 17 1993 465–491.Ž .

<sup>w</sup> <sup>x</sup> 9 T. Connolly, L.M. Jessup, J.S. Valacich, Effects of anonymity and evaluative tone on idea generation in computer-mediated groups, Management Science 36 1990 689–703.Ž .

<sup>w</sup> <sup>x</sup> 10 R.L. Daft, R.H. Lengel, L.K. Trevino, Message equivocality, media selection, and manager performance: implications for information systems, Management Information Systems Quarterly 11 1987 355–366.Ž .

<sup>w</sup> <sup>x</sup> 11 A.L. Delbecq, A.H. Van de Ven, D.H. Gustafson, Group Techniques for Program Planning: A Guide to Nominal Group and Delphi Processes, Scott, Foresman and Co., Glenview, IL, 1975.

<sup>w</sup> <sup>x</sup> 12 A.R. Dennis, J.S. Valacich, Computer brainstorms: more heads are better than one, Journal of Applied Psychology 78 Ž .1993 531–537.

<sup>w</sup> <sup>x</sup> 13 G.W. Dickson, J.L. Partridge, L.H. Robinson, Exploring modes of facilitator support for GDSS technology, Management Information Systems Quarterly 17 1993 173–194.Ž .

<sup>w</sup> <sup>x</sup> 14 D. Dufner, S.R. Hiltz, K. Johnson, R. Czech, Distributed group support: the effects of voting tools on group percep-

tions of media richness, Group Decision and Negotiation 4 Ž . 1995 235–250.

<sup>w</sup> <sup>x</sup> 15 R. Grohowski, C. McGoff, D. Vogel, B. Martz, J. Nunamaker, Implementing electronic meeting systems at IBM: lessons learned and success factors, Management Information Systems Quarterly 14 1990 369–382.Ž .

16 S.C. Hayne, R. Rice, P. Licker, Social cues and anonymous group interaction using group support systems, Proceedings of the 27th Annual Hawaii International Conference on Systems Sciences 4 1994 73–81.Ž .

<sup>w</sup> <sup>x</sup> 17 S.R. Hiltz, D. Dufner, M. Holmes, S. Poole, Distributed group support systems: social dynamics and design dilemmas, Journal of Organizational Computing 2 1991 135–159.Ž .

<sup>w</sup> <sup>x</sup> 18 S.L. Jarvenpaa, V.S. Rao, G.P. Huber, Computer support for meetings of groups working on unstructured problems: a field experiment, Management Information Systems Quarterly 12 1988 645–666.Ž .

<sup>w</sup> <sup>x</sup> 19 F.J. Lim, I. Benbasat, A communication-based framework for group interfaces in computer-supported collaboration, Proceedings of the 24th Annual Hawaii International Conference on Systems Sciences 3 1991 610–620.Ž .

<sup>w</sup> <sup>x</sup> 20 T.W. Malone, K.R. Grant, K.-Y. Lai, R. Rao, D. Rosenblitt, Semi-structured messages are surprisingly useful for computer-supported coordination, in: I. Greif Ed. , Computer- Ž . Supported Cooperative Work: A Book of Readings, Morgan Kaufmann, San Mateo, CA, 1988, pp. 311–331.

<sup>w</sup> <sup>x</sup> 21 T.W. Malone, K.R. Grant, F.A. Turbak, S.A. Brobst, M.D. Cohen, Intelligent information-sharing systems, Communications of the ACM 30 1987 390–402.Ž .

<sup>w</sup> <sup>x</sup> 22 J.C. McCarthy, V.C. Miles, A.F. Monk, M.D. Harrison, A.J. Dix, P.C. Wright, Text-based on-line conferencing: a conceptual and empirical analysis using a minimal prototype, Human–Computer Interaction 8 1993 147–183.Ž .

<sup>w</sup> <sup>x</sup> 23 J.E. McGrath, Groups: Interaction and Performance, Prentice-Hall, Englewood Cliffs, NJ, 1984.

<sup>w</sup> <sup>x</sup> 24 J.E. McGrath, A.B. Hollingshead, Putting the group back in group support systems: some theoretical issues about dynamic processes in groups with technological enhancements, in: L.M. Jessup, J.S. Valacich Eds. , Group Support Sys-Ž . tems: New Perspectives, Macmillan, New York, 1993, pp. 78–96.

<sup>w</sup> <sup>x</sup> 25 R.K. Mosvick, R.B. Nelson, We’ve Got to Start Meeting Like This! A Guide to Successful Business Meeting Management, Scott, Foresman and Co., Glenview, IL, 1987.

<sup>w</sup> <sup>x</sup> 26 J.F. Nunamaker, A.R. Dennis, J.S. Valacich, D.R. Vogel, J.F. George, Electronic meeting systems to support group work, Communications of the ACM 34 1991 40–61.Ž .

<sup>w</sup> <sup>x</sup> 27 R. Ocker, S.R. Hiltz, M. Turoff, J. Fjermestad, The effects of distributed group support and process structuring on software requirements development teams: results on creativity and quality, Journal of Management Information Systems 12 Ž . 1995–6 127–153.

<sup>w</sup> <sup>x</sup> 28 M.S. Poole, G. DeSanctis, Understanding the use of group decision support systems: the theory of adaptive structuration, in: J. Fulk, C. Steinfield Eds. , Organizations and Ž . Communications Technology, Sage, Newbury Park, CA, 1990, pp. 173–193.

29 M.E. Shaw, Group Dynamics: The Psychology of Small Group Behavior, 3rd edn., McGraw-Hill, New York, 1981.

<sup>w</sup> <sup>x</sup> 30 M.S. Silver, Decision support systems: directed and nondirected change, Information Systems Research 1 1990 47–Ž . 70.

<sup>w</sup> <sup>x</sup> 31 H. Smith, J. Onions, S. Benford Eds. , Distributed GroupŽ . Communication: The AMIGO Information Model, Ellis Horwood, Chichester, England, 1989.

<sup>w</sup> <sup>x</sup> 32 J.Y. Smith, M.T. Vanecek, Dispersed group decision making using nonsimultaneous computer conferencing: a report of research, Journal of Management Information Systems 7 Ž . 1990 71–92.

<sup>w</sup> <sup>x</sup> 33 A.B. VanGundy, Techniques of Structured Problem Solving, 2nd edn., Van Nostrand-Reinhold, New York, 1988.

<sup>w</sup> <sup>x</sup>34 J.B. Walther, J.K. Burgoon, Relational communication in computer-mediated interaction, Human Communication Research 19 1992 50–88.Ž .

<sup>w</sup> <sup>x</sup> 35 B.C. Wheeler, J.S. Valacich, Facilitation, GSS, and training as sources of process restrictiveness and guidance for structured group decision making: an empirical assessment, Information Systems Research 7 1996 429–450.Ž .

<sup>w</sup> <sup>x</sup> 36 A. Zander, Making Groups Effective, Jossey-Bass, San Francisco, CA, 1982.

## Biographies

Karen Dowling is an Assistant Professor of Computer Information Systems in the College of Business at Arizona State University. She received a BA in English from the University of Michigan and an MS and PhD in Computer Information Systems from Arizona State University. Her teaching and research interests are in the areas of databases, group support systems, and decision support systems.

Robert St. Louis is an Associate Professor of Computer Information Systems in the College of Business at Arizona State University. He received an AB in Economics in 1966 from Rockhurst College, an MS in Economics in 1968 from Purdue University, and a PhD in Economics in 1972 from Purdue University. His research and teaching interests are in the areas of databases, data mining, and decision support systems.
