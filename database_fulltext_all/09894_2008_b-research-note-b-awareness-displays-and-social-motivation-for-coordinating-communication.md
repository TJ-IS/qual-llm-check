---
otero_id: 9894
otero_key: "CM5WNGPU"
title: "<b>Research Note</b>—Awareness Displays and Social Motivation for Coordinating Communication"
authors: "Laura Dabbish; Robert Kraut"
year: "2008"
journal: "Information Systems Research"
doi: "10.1287/isre.1080.0175"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/CM5WNGPU/fulltext/images/2b096f3f233a555cc5f273056a54b27c37afc5680e110390c08cad60d2180ad7.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Research Note—Awareness Displays and Social Motivation for Coordinating Communication

Laura Dabbish, Robert Kraut,

## To cite this article:

Laura Dabbish, Robert Kraut, (2008) Research Note—Awareness Displays and Social Motivation for Coordinating Communication. Information Systems Research 19(2):221-238. http://dx.doi.org/10.1287/isre.1080.0175

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2008, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/CM5WNGPU/fulltext/images/6e91581ae940a5ffc81cb0964bad69fd67dc5141aae6894f76a03398d03ca5a1.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Research Note

# Awareness Displays and Social Motivation for Coordinating Communication

Laura Dabbish

H. John Heinz III School of Public Policy and Management, Carnegie Mellon University, 5000 Forbes Avenue, Pittsburgh, Pennsylvania 15213, dabbish@cmu.edu

Robert Kraut

Human-Computer Interaction Institute, Carnegie Mellon University, 5000 Forbes Avenue, Pittsburgh, Pennsylvania 15213, robert.kraut@cmu.edu

esearchers and designers have been building awareness displays to improve the coordination of communi Rcation between distributed co-workers since the early 1990s. Awareness displays are technology designed to provide contextual information about the activities of group members. Most researchers have assumed that these displays improve the coordination of communication regardless of the relationship between the communi cating parties. This article examines the conditions under which awareness displays improve coordination and the types of designs that most effectively support communication timing without overwhelming people with irrelevant information. Results from a pair of laboratory experiments indicate that awareness displays containing information about a remote collaborator’s workload lead to communication attempts that are less disruptive, but only when the interrupter has incentives to be concerned about the collaborator’s welfare. High-information awareness displays harmed interrupters’ task performance, while abstract displays did not. We conclude tha a display with an abstract representation of a collaborator’s workload is optimal; it leads to better timing of interruptions without overwhelming the person viewing the display.

Key words: computer-mediated communication and collaboration; virtual teams; laboratory experiments; attention; interruption; awareness

History: Vallabh Sambamurthy, Senior Editor; Laku Chidambaram, Associate Editor. This paper was received November 28, 2004, and was with the authors 1 year and 11 months for 3 revisions.

## Introduction

A substantial body of research shows that group work is much more difficult to accomplish when coworkers are physically distributed than when they are collocated (see Hinds and Bailey 2003, Powell et al. 2004 for reviews). In distributed environments, team members don’t communicate enough (Kraut et al. 1990), they don’t have enough contextual information (Cramton 2001) and their communication can be ineffective (Olson and Olson 2000). Researchers and designers have been building awareness displays with the goal of improving the connection between distributed co-workers since the early 1990s (Hudson and Smith 1996, Tang et al. 1994, Dourish and Bly 1992). Despite the intuition that awareness displays should improve coordination, we have little evidence that they actually help coordinate communication and almost no systematic research about the conditions under which they do so. The work presented here examines the utility of awareness displays for coordinating communication interactions.

Inopportune or disruptive communication attempts can occur in both distributed (Kraut et al. 1990) and colocated settings (Perlow 1999) as a result of information asymmetry (i.e., initiators of a communication not knowing recipients’ availability) and incentive incompatibility (i.e., initiators caring more about executing the communication than about the recipients’ welfare). But addressing the information asymmetry issue by providing awareness<sup>1</sup> information does not guarantee mutually beneficial communication timing. For example, Fogarty et al. (2004) found that IBM employees subverted an awareness display, treating a signal that co-workers were extremely busy as an indication that now was a good time to interrupt—valuing the information they would receive in the communication over the disruption to their co-worker’s ongoing task. We do not yet have a good understanding of the social conditions under which people will use awareness displays for opportune communication timing.

We also know little about how awareness displays should be designed to improve coordination. The design of awareness displays has been ad hoc, in many cases divorced from theories of interpersonal and organizational communication. Neither the commercial nor research examples of awareness displays (Fish et al. 1993, Dourish and Bly 1992, Tang et al. 1994, Fogarty et al. 2004) have systematically explored the design space to explicitly test the utility of design techniques to facilitate coordination while minimizing the potential for distraction.

Despite these open issues, researchers and practitioners in the fields of HCI, CSCW, and IS have recommended the use of systems that help work partners maintain awareness about what others are doing. We note that these recommendations rest on three unanswered research questions, addressed in the work presented: (1) Do awareness displays help coordinate communication interactions? (2) How should these displays be designed to best improve coordination? (3) Under what social conditions will people use these displays to coordinate communication?

In the next section we consider broadly the kinds of information people take into account when initiating a communication, and based on this analysis in the following section we focus on one type of information an awareness display could provide, some of the tradeoffs involved, and the conditions under which the information would be used for coordination purposes.

## Deciding to Communicate

Within the organizational context, workers initiate communication for many reasons. One common purpose is to seek information or advice. We focus on help-seeking communication in this paper, because it is so prevalent in organizational life and because it highlights the asymmetry in benefit and costs often experienced by the initiator and target of a communication (Perlow 1999). In a help-seeking interaction, the person who initiates needs some information and tries to communicate with someone perceived to possess the needed information. This target, however, may be working on another task, which could be disrupted by the incoming help-seeking communication (Kraut and Attewell 1997).

Let us consider the decision to communicate, from the point of view of both the initiator of the communication and the target. The initiator must weigh the importance and urgency of the communication against the effort required for initiation, and the net benefit or cost that the target may receive from the communication. Their perception of the target’s net benefit may depend upon the content of the communication (e.g., whether it pertains to a joint project), their relationship with the target, and whether their communication will disrupt some work the target is currently doing. Their perception of target availability depends in part upon the information they have about whether the target is physically and psychologically present to receive the communication. The degree to which initiators act upon evidence about cost or benefit to the target when initiating a communication is likely to depend upon their relationship with the target—whether they have interdependent goals (Van der Vegt et al. 1998), common group membership (Kane et al. 2005, Henry et al. 1999), personal friendships, or likely future interactions (Perlow 1999), among other factors.

The target of the communication goes through a similar process when deciding how to respond to an incoming communication. Because responding immediately can harm ongoing work (Gillie and Broadbent 1989, McFarlane 2002, Perlow 1999, Speier et al.

2003, Sproull 1984), targets must balance the value that they expect their response would have to the initiator and the potential value they may receive from the communication against the cost of postponing their current activities to communicate. Targets’ willingness to postpone their ongoing work and attend to incoming communication is influenced by the value of their current task, proximity of impending deadlines, and proximity to a reasonable stopping point in the task (McFarlane 2002). The interpersonal relationship between initiator and target may also influence the extent to which the target takes into account the value of the communication to the initiator.

## Awareness Display Design and Use

Given this overall model of the factors influencing initiators’ and targets’ willingness to engage in a communication, we focus specifically on initiator perception of target availability for communication. Awareness displays allow initiators to form these perceptions, especially in distributed work settings, where casual observation is not possible. We consider below the three open research questions guiding this work: (1) Could awareness displays facilitate less disruptive communication timing? (2) How can the design of these displays be optimized to do so, and what are the tradeoffs? (3) Under what conditions would initiators use awareness displays in this way?

## Communication Timing and Performance

Previous work suggests that it is possible to interrupt people at times that minimize the disruptive impact interruptions have on a target’s ongoing work (e.g., Gillie and Broadbent 1989, Speier et al. 2003). For example, programmers are more productive in debugging if they are not interrupted during periods of peak concentration (Fogarty et al. 2005), and interruptions are generally less disruptive if they occur at task and subtask boundaries (Adamczyk and Bailey 2004). Thus, it follows that if Initiators are attempting to minimize their impact on the Target they should attempt their communication at a time when the Target is free (e.g., not deeply engaged in a higher-priority task), and that doing so will lead to better performance on the Target’s primary task. The rest of our theory on initiating interaction rests on this assumption which we validate in the experiments described in this paper.

## Design of Awareness Displays

To synchronize communication with a target’s availability, the Initiator needs feedback about the Target’s task and attentional state. In co-located settings, this information is often obtained by glancing into someone’s office (Fish et al. 1993). In a distributed situation, an awareness display showing the Target’s availability could provide similar information. Designers must deal with two problems in creating this kind of display: (1) interpretability and (2) attentional demand.

Communication systems for distributed work of the 1990s often showed a full video of a collaborator’s office, so that those who wanted to communicate could easily understand when others were present and what they were doing before attempting to communicate with them (Abel 1990, Fish et al. 1993, Tang et al. 1994). Because this level of detail can violate Targets’ privacy and be distracting to Initiators, followup research involved displays with a more abstracted view of co-workers’ current activities (Dourish and Bly 1992, Hudson and Smith 1996). The experiments in this article attempt to establish the relationship between information abstraction, the accuracy of the timing of the decision to communicate, and attentional demands in order to understand the tradeoffs involved in designing awareness displays.

Display Utility. Initiators need information about Targets’ availability and workload to synchronize their communication requests with periods of low workload for the Target. A display with no information about Targets’ availability would harm Targets, because Initiators would have little basis for making decisions about when to interrupt. In contrast, displays providing more information about availability should benefit Targets, because Initiators can synchronize interruptions with periods of low workload, thus minimizing impact on Targets’ performance.

Hypothesis 1. Displays showing Targets’ workload will allow Initiators to time their communication so that it arrives during periods of lower workload in Targets’ task.

However, there are limits to the amount of information that Initiators can effectively use to assess Targets’ workload. For example, studies have shown that people cannot effectively use more than two information sources when making decisions and that more sources can lead to errors because of the effort required to search and integrate the available cues (Wickens et al. 1998). However, we may be able to optimize human decision-makers: Dawes (1979) showed that simple linear models of decision-makers could outperform their own predictions based on clinical judgment and the raw data. In fact, the clinicians were useful only to the extent that they could select the appropriate features important to the decision and their direction of influence. Displays to facilitate monitoring of a co-worker for communication could optimize interruption timing by presenting an assessment of Target availability derived from a linear combination of the variables influencing availability, rather than all possible system cues (Wickens et al. 1998, Dawes 1979). This brings us to Hypothesis 2:

Hypothesis 2. Using abstracted information displays that show a simple representation of Targets’ workload, initiators should be able to assess availability and time communication so that it arrives during periods of low workload as well as or better than a full video display that shows more information about Targets’ work activities.

Attentional Demand. Studies of attention in perceptual psychology have shown that increases in the number of visual elements and movement (Pashler et al. 2001, Wickens et al. 1998) make visual stimuli more distracting or attention-grabbing. In addition, large numbers of visual elements increase the visual search time required to filter and process relevant cues (Wickens et al. 1998). One way to reduce the amount of information in a display is to present an abstraction containing only key information or a summary representing a linear combination of important situational variables (Wickens et al. 1998, Dawes 1979). This approach has the tradeoff though that these abstracted or aggregated representations, though containing less visual elements than a presentation of all possible information, may be more difficult to process because of possible difficulty interpreting their contents (Matthews et al. 2007). We must then ask the question, will an abstract display representing only partial information about a target’s availability consume less attention? If so, it would suggest the following hypothesis:

Hypothesis 3. An increase in the amount of information in an on-screen display of target status (with respect to number of elements and movement) will increase the amount of visual attention required to attend to the display and obtain information from it.

If abstract displays are sufficient for communication Initiators to make good decisions about when to interrupt (Hypothesis 2) and if increased information in the display will distract (Hypothesis 3), then rich awareness displays will cause Initiators to divide attention between the display and a primary task, potentially harming their primary task performance due to switching costs and reduced time on task (Wickens et al. 1998) without any benefit for Targets.

Hypothesis 4. An increased amount of information in an on-screen display of Target status should increase Targets’ attention to the display and in turn decrease Initiators’ primary task performance on continuous attention tasks.

Incentive to be Concerned About Targets’ Welfare Frequently, Initiators of communication and their Targets have incompatible incentives (Kraut and Attewell 1997). The information Targets can provide is often worth more than the Targets’ time to the Initiator. When Initiators have no stake in Targets’ performance, they have no motivation to delay communication attempts to be convenient for the Targets. It follows, therefore, that Initiators will use awareness displays to time their communication to be convenient to a target primarily when they are concerned about disruption to that person’s work.

Previous research suggests that if Initiators and Targets were in a group with outcome interdependence, their common social identity and common rewards could motivate Initiators to honor Targets’ time for both altruistic and self-interested reasons (Henry et al. 1999). For example, members of self-managed teams are mindful of the activities of their peers and strive for the welfare of the group as a whole, because team membership is emphasized and teams are rewarded based on the overall team performance, rather than on individual performance (Van der Vegt et al. 1998).

Hypothesis 5. Common social identity and outcome interdependence will cause Initiators to use awareness displays to time communication so it arrives during periods of low workload for the Target.

Figure 1 Awareness Display Design, Usage, and Performance Impacts  
![](/api/attachments/CM5WNGPU/fulltext/images/21165126f709faec645bccee918d9d5cd6983a4adae31b411c71f83d7b9dda06.jpg)

To test our hypotheses as stated and summarized in Figure 1, we designed and performed two controlled experiments. In both experiments a pair participated in a stylized instantiation of the help-seeking situation between two work-colleagues. The experiments varied both the amount and presentation of information Initiators had about their Targets’ workloads and whether Initiators perceived themselves and their Targets as part of a common team or as independent. Even though the tasks used in this laboratory setting were stylized and do not correspond in detail to work done in most organizational settings, they capture many features of organizational work, in which one person’s attempt to complete an assignment has implications for colleagues’ ability to complete their own work. The experimental settings and tasks allowed us to independently assess the impact of an awareness display on team collaborators’ performance by controlling the situation to manipulate only factors of interest (display presence, display design, and social identity).

## Experiment 1

## Method

Overview. In Experiment 1 two subjects played a stylized game where one (the Initiator) was dependent on the other (the Target) for important information. The Initiator tried to guess the identity of pictures as they were slowly revealed, and was allowed to ask the Target for hints by sending messages over the computer. Doing so interrupted the Target, who was engaged in a variant of McFarlane’s (2002) Jumpers game. The experiment varied the amount of information Initiators had about Targets workload and whether the Initiators perceived that they and the Targets were a team or not. The experimental design was a 3 (Awareness information) by 2 (Team manipulation) mixed design, with the Awareness information manipulated within subjects and the Team manipulated between subjects.

Task. The Initiator’s task was to quickly and correctly guess the identity of a partially obscured picture (640 426 pixels) as it was slowly uncovered (see Area D of Figure 2(a)). Small black squares (8 <sub>×</sub> 8 pixels) covering the image were gradually removed over

Figure 2 From Top to Bottom: (a) Initiator’s Screen in Experiment, (b) Target’s Screen in Experiment, (c) Awareness Display Conditions (Counterclockwise from Top Left: No Display, Abstract, Full )

![](/api/attachments/CM5WNGPU/fulltext/images/46630678d605f48d8b96d0989b73101b2cfea86c094b32fc291e900b263e3beb.jpg)  
Note. (a) Boxes A through E indicate the regions for eye tracking and were not visible to participants.

four minutes while “clues,” or random larger squares of the picture (40 <sub>×</sub> 40 pixels), were revealed and then hidden again. The game consisted of three rounds, during each of which the Initiator had to guess the identity of four different pictures.

Targets’ primary task was the Jumpers video game used by McFarlane (2002). (See left side of Figure 2(b).) Targets attempted to save jumpers as they fell from a building by catching them on a stretcher and bouncing them to the ambulance. Their score was based on the number of jumpers they saved. Their workload varied from zero to nine jumpers on screen simultaneously, with new jumpers arriving at random intervals.

Targets were given a copy of the pictures that Initiators were trying to guess, and thus became experts with access to information that Initiators needed (see right side of Figure 2(b)). Initiators and Targets were seated in separate rooms, and Initiators were able to send Targets 20 yes/no questions over the computer about the picture they were attempting to guess. The Initiators were informed that these questions took over Targets’ screens until they were answered, covering their primary task and interrupting the Targets ability to save jumpers.

This design required both Targets and Initiators to continually attend to their primary tasks in order to achieve optimal performance. Interruptions interfered with Targets’ ability to save jumpers. Distraction on the Initiator side prevented them from seeing important clues and thus interfered with their ability to identify the picture.

Participants. Thirty-six Initiator-Target pairs (72 individuals) were recruited from local universities. The participants mean age was 23 years (std. dev. <sub>=</sub> 5), and 53 percent were male.

Awareness Display. We tested Hypothesis 1 and 2, about the usefulness of awareness displays, and Hypotheses 3 and 4 regarding the attentional demand of the displays, by manipulating within subjects both the amount of information Initiators had about Targets’ workload (the number of jumpers currently on screen) and the presentation of that information. In the no-display condition, Initiators received no information about Targets’ current task. The no-display condition was used as a control for comparison purposes. In the abstract-display condition, Initiators saw icons representing the number of Jumpers on Targets’ screens. In the full-display condition, Initiators saw a 25" <sub>×</sub> 25" real-time replica of Targets’ screens, implemented as a Virtual Network Computing (VNC) (RealVNC 2002) window on their computer. Both the abstract and full-display conditions provided information about the number of jumpers on screen, the primary determinant of the Targets’ workload. However, we expected the full display to be more distracting, because it contained more visual elements and movement. Figure 2(c) shows each of the three awareness displays. Each subject saw each of the three awareness display conditions during one round of the game, with display order counter-balanced using a Latin square design.

Team Orientation. To test Hypothesis 5 that common social identity and outcomes with the Target would cause Initiators to use information displays to time their interruptions, we manipulated between subjects whether Initiators perceived themselves as part of a team with Targets or not.<sup>2</sup> In the Independent condition, participants in the Initiator role were rewarded based on their individual performance, were told they were competing with Targets for a fifty-dollar prize, and wore a jersey of a different color from the Targets’. In the Team condition, Initiators were rewarded based on the average of their performance and the Targets’ performance, were told they were on a team with the Targets competing against other teams for the fifty-dollar prize, and they and the Targets wore matching jerseys.<sup>3-</sup> <sup>4</sup>

Dependent Measures. To assess the performance benefits and costs of awareness information, we analyzed the rate and timing of Initiators’ questions, along with their effect on both players’ performance. Because the behavioral measures of question rate and timing directly relate to the research questions, but were not part of the participants’ incentive structure, they were examined to reveal the impact of the manipulations of interest. Initiators also described their strategies for timing interruptions via openended self-report questions, providing insight into the interruption decision-making process.

Analysis. A pair’s performance on an individual picture was the unit of analysis. There were 432 pictures (36 pairs <sub>×</sub> 3 display conditions <sub>×</sub> 4 pictures per display). Because each pair worked on multiple pictures, we analyzed data using a repeated measure mixed-model analysis of variance, with participant pairs as a random effect. We computed two singledegree-of-freedom contrasts to analyze the effects of the display manipulation. The information contrast compared the abstract and full-display conditions to the no-display condition, to test whether simply providing Initiators with information about Targets workload influenced performance (Table 1, “No Display vs. Display”). The presentation contrast compared the two display conditions, to test whether the type of display differentially influenced performance (Table 1, “Abstract vs. Full”).

## Results

Manipulation Check. Initiators completed a 12- item survey measure of group identity to check the effectiveness of the team manipulation (Henry et al. 1999). The inter-item reliability for the measure was satisfactory (Cronbach’s alpha <sub>=</sub> 085). Although Initiators in the Team condition identified more strongly with their partner than did Initiators in the Independent condition (Means: Team <sub>=</sub> 507, Independent <sub>=</sub> 467, SE 016); this difference was only marginally significant with (t36 <sub>=</sub> 203, p <sub>=</sub> 009), with a moderate effect size (Cohen’s d <sub>=</sub> 042) (Rosenthal and Rosnow 1991). Follow-up analysis showed that the team involvement manipulation did not influence either the Initiators’ or the Targets’ performance. This suggests that the team manipulation was not successful, so we will not further discuss the results from Experiment 1 with respect to the Team manipulation and do not test Hypothesis 5 in Experiment 1.

## Display Utility

Communication Timing. Hypothesis 1 predicted that awareness displays showing Targets’ workloads would allow Initiators to interrupt during periods of low Target workload. To test this hypothesis, we compared the number of jumpers Targets had on screen during a communication attempt in the abstract and full-display conditions compared to the no-display control condition. Initiators in the abstract and fulldisplay conditions attempted communication when Targets were under a lighter workload than did those in the no-display condition, supporting Hypothesis 1. The abstract and full-display conditions did not differ (Table 1, Row A).

Table 1 Performance Results for Experiment 1<sup>†</sup>

<table><tr><td rowspan="3">Row</td><td rowspan="3">Dependent variable</td><td rowspan="3">N</td><td colspan="3">Display condition means</td><td colspan="4">Differences among conditions</td></tr><tr><td rowspan="2">No display</td><td rowspan="2">Abstract</td><td rowspan="2">Full</td><td colspan="2">No display vs. display</td><td colspan="2">Abstract vs. full</td></tr><tr><td>F (SE)</td><td>p</td><td>F (SE)</td><td>p</td></tr><tr><td>A</td><td>Initiator interruption timing(probability of jumpers on screen during interruption)</td><td>432</td><td> $0.75^a$ </td><td> $0.43^b$ </td><td> $0.42^b$ </td><td>35.7 (0.063)</td><td>&lt;0.001</td><td>1.78 (0.072)</td><td>0.18</td></tr><tr><td>B</td><td>Initiator interruptions sent per minute</td><td>432</td><td> $1.046^a$ </td><td> $1.042^b$ </td><td> $1.036^c$ </td><td>12.5 (0.007)</td><td>&lt;0.001</td><td>8.38 (0.007)</td><td>0.004</td></tr><tr><td>C</td><td>% jumpers saved by Targets</td><td>432</td><td> $70.7^a$ </td><td> $75.4^b$ </td><td> $74.6^b$ </td><td>5.52 (0.018)</td><td>0.02</td><td>0.04 (0.02)</td><td>0.84</td></tr><tr><td>D</td><td>Accuracy of Initiators&#x27; puzzle performance</td><td>432</td><td> $0.79^a$ </td><td> $0.80^a$ </td><td> $0.78^a$ </td><td>0.06 (0.042)</td><td>0.8</td><td>0.24 (0.048)</td><td>0.62</td></tr><tr><td>E</td><td>Time for Initiators&#x27; puzzle performance</td><td>432</td><td> $110^a$ </td><td> $105^a$ </td><td> $121^b$ </td><td>0.24 (6.69)</td><td>0.62</td><td>4.06 (7.73)</td><td>0.04</td></tr></table>

<sup>†</sup> Different superscripts (a, b, c) in the same row indicate significant differences between values (p < 005).

Interruption Rate. We also looked at the number of questions Initiators sent per minute to calculate the interruption rate. As shown in Row B of Table 1, the interruption rate significantly decreased as Initiators received more information about Targets’ workload. They asked 7% fewer questions per minute in the abstract condition than in the no-display condition and 14% fewer in the full-display condition than in the abstract condition. This result suggests that by waiting for a good time to interrupt, Initiators sent fewer interruptions per unit time, as a side effect.

Targets’ Performance. Consistent with our assumptions and Hypothesis 1, the awareness displays that enabled Initiators to send questions during periods of low workload improved Targets’ performance. Targets were able to save approximately 7% more jumpers when Initiators were using the abstract or full displays than in the no-display control condition. (See the Display versus No-Display contrast in Table 1, Row C.) Consistent with Hypothesis 2, there was no significant difference between the abstract and full condition for number of jumpers on screen when a message was sent (Table 1, Row A), and no significant difference in Targets’ performance as the amount of information in the display increased from abstract to full (Table 1, Row C).

Attentional Demand. The prior analyses showed that Initiators used both types of awareness displays to time their questions in ways that benefited Targets’ task performance, and that the abstract and full displays were equivalent in this regard. Were they also equivalent in their effects on Initiators’ task performance?

Initiator Performance. Initiators’ performance was measured by accuracy on the picture identification task and time taken, in seconds, to identify each picture. As Row E in Table 1 shows, the display conditions had no effect on Initiators’ ability to correctly identify pictures; however, the displays did influence Initiators’ speed. Initiators took 12.5% longer to guess pictures in the full-display condition than in the abstract-display condition or the no-display condition (Table 1, Row D), supporting Hypothesis 4.

Self-Reports About Interruption Timing. We obtained some qualitative data to get a better sense of the nature of awareness display use. Initiators described their strategy for deciding when to send questions to their Targets in response to an openended question asked immediately after using each type of awareness display. In the abstract-display condition, 60.8% of Initiators reported using the display to decide when to send questions to their partners.

Because the only information they received during this condition was the number of jumpers on the Targets’ screen, all of them reported asking questions when the number of jumpers was below some threshold. For example, they described rules such as “When there was only 1 person on the jumper indicator,” “When there was one jumper. [Otherwise] I tried to ask as few questions as possible and to figure out the picture on my own” or “When there were 2 or less[sic] jumpers.”

In the full display condition, 67% of Initiators reported using the display to determine when to send questions to their partners. Initiators’ strategies were more complex in the full-display condition than in the abstract-display condition. They reported taking into account more detailed information about the Targets’ task state than the number of jumpers and using more complex rules. For example, Initiators reported the following heuristics:

“    if the current position of the net was okay or had to be moved soon.”

“Whenever she had people at the apex of their bounce or if there was a break in the jumpers.”

“Tried to do it when the people were higher in the air so they had time to answer without losing a person.”

Summary. The results from the first experiment showed that providing an interrupter with information about a remote partner’s workload, in the form of an awareness display, benefited the remote partner’s performance. Increasing the realism of the workload display did not result in additional benefit for the remote partner. Initiators used the additional information available in the full display to form more complex strategies to time their interruptions. It was either these complex strategies or the greater perceptual complexities in the full display that harmed the interrupters’ own performance, without improving their partners’ performance.

## Experiment 2

## Overview

The results from Experiment 1 left several open questions that we sought to answer in Experiment 2. In Experiment 1 the team manipulation was not successful, so we could not test whether incentives influence

Initiators’ use of awareness displays to time communication (Hypothesis 5). Experiment 2 was designed to include a more compelling manipulation of team identity and joint outcomes. In addition, Experiment 1 indicated that the full information display harmed task performance for those using it (corresponding with Hypothesis 4). However, Experiment 1 included no direct measures of attention, preventing identification of the root of this performance deficit and testing of Hypothesis 3. In Experiment 2, we used eye tracking to measure the amount of attention required by the various displays. By examining the amount of time spent looking at the various awareness displays, we could test whether the full information display consumed more attention than the abstract one.

## Method

Task. Experiment 2 utilized the same laboratory task as Experiment 1, with a modified reward structure. In Experiment 2, Initiators were rewarded based on the time taken to guess the contents of each picture being revealed, and not simply correct picture identification as in Experiment 1. By rewarding Initiators on speed as well as accuracy, we highlighted the conflict they might experience between getting help quickly and waiting for a lull in Targets’ workload. We also lengthened the duration of each interruption, so that questions stayed on Targets’ screen for at least five seconds. The longer interruption allowed us to better observe the effect of Initiators’ interruption timing on Targets’ performance.<sup>5</sup>

Awareness Display. Experiment 2 used the same three within-subjects awareness display conditions used in Experiment 1 (no-display, abstract-display, and full-display). As in Experiment 1, each subject saw each of the three awareness display conditions during one round of the game; display order was counter-balanced using a Latin square design.

Team Orientation. As in Experiment 1, we manipulated between subjects whether the Initiators were independent and received individual rewards or were part of a team and received joint rewards. In the team condition, Initiators were rewarded based on the average of their score and their Targets’ score; they were told they were on a team with their Targets competing against other teams for a fifty-dollar prize, and that they and their Targets wore matching jerseys. To enhance their feelings of attachment to their partners, we showed Initiators in the team condition a photograph of their partners wearing the team jersey while sitting in front of a computer playing the Jumpers game (Walther et al. 2001) with the explanation that we wanted them to see what their partner would be doing during the study. Work on computer-mediated communication (CMC) has shown that participating in getting-acquainted activities with a virtual partner can result in almost the same level of trust development as face-to-face meeting (Zheng et al. 2002). To increase the likelihood of such a bond developing, Initiators in the team condition also participated in a structured social chat with confederates whom they believed to be their partners. They were instructed to exchange information with their partners in response to a list of get-acquainted questions such as “What is your major?” “What did you do last weekend?” “What is your favorite restaurant in this city?” For each question they first sent the question to their partners, received a response, were asked the question by their partners, and then provided their own answers. Confederates acting as their partner responded by sending back randomly selected answers recorded from the chat logs of naive participants answering the same series of questions.

In the independent condition, participants in the Initiator role were rewarded based on their individual performance, were told they were competing against all other Initiators for a fifty-dollar prize, and were told they wore a jersey of a different color than the Targets’. To avoid any experimenter effects that would confound the differences between the Team and Independent Initiators, participants in the Independent condition were shown a picture of a person who had completed the experiment in the past and told this was to illustrate their partner’s task setup. They also answered the same questions used in the team condition social chat via a static webbased form.<sup>6</sup>

Analysis. Players’ performance during an individual picture puzzle was the unit of analysis, except where noted. We recorded participants’ actions on 396 puzzles (33 pairs  3 display conditions  4 picture puzzles per display). Again, we used a repeated measure mixed-model analysis of variance to analyze the data in order to handle the nonindependence of observations. To examine the consequence of awareness displays, we again calculated one-degreeof-freedom planned contrasts to compare the condition with no display to the conditions where a display was visible (abstract and full-display conditions) (Table 2, “No Display vs. Display”), and to contrast the abstract-display condition with the full-display condition (Table 2, “Abstract vs. Full”).

Measuring Attentional Demand. We calibrated a visor-mounted ISCAN ETL-500 gaze tracking system to record the number and duration of Initiators’ gaze fixations in various regions of their computer screen (see Figure 2(a)), with a fixation threshold of 50 msec (Jacob and Karn 2003). In particular, we were interested in the amount of time they spent looking at their puzzle (region D) versus the awareness display (region B). The eye-tracking measures recorded were proportion of fixations and mean of fixation duration. Proportion of fixations is the number of visual fixations on a particular display element of interest relative to total number of fixations. Because people fixate more often on display elements they consider important, this measure is generally treated as a measure of visual importance of an element (Jacob and Karn 2003). Mean fixation duration is the average length of a visual fixation on an area of interest. The measure is generally treated as an indication of a participant’s difficulty extracting or interpreting information from an interface (Jacob and Karn 2003).

Eye-gaze data were collected from the Initiators for an entire round (4 pictures), so the unit of analysis for the eye-tracking data is one round in the game (with 3 rounds each session). Due to calibration problems, we excluded gaze data from fourteen participants. Thus the results with respect to visual attention come from 19 out of the 33 Initiators in Experiment 2. The number of rounds analyzed was 57 (19 pairs<sub>×</sub> 3 display conditions <sub>=</sub> 57). We used a repeated measure mixed-model analysis of variance to analyze the eyetracking data, with participant treated as a random effect to control for the nonindependence of rounds nested within pairs.

## Results

Manipulation Check. Initiators in Experiment 2 completed a 12-item survey measure of group identity to check the effectiveness of the team manipulation (Henry et al. 1999). The inter-item reliability for the measure was satisfactory (Cronbach’s alpha <sub>=</sub> 082). Initiators in the Team condition identified more strongly with their partners than did Initiators in the Independent condition (Means: Team <sub>=</sub> 424, Independent <sub>=</sub> 375, SE <sub>=</sub> 016, with t30 <sub>=</sub> 223, p < 005). Results show that the social identity manipulation was substantially stronger in Experiment 2 than in Experiment 1, with a 26% increase in effect size (Cohen’s d <sub>=</sub> 053) (Rosenthal and Rosnow 1991).

## Display Utility

Communication Timing. Hypothesis 1 predicted that awareness displays showing Targets’ workload would allow Initiators to interrupt during periods of low workload. To test this hypothesis, we compared the number of jumpers Targets had on screen during a communication attempt<sup>7</sup> in the abstract and fulldisplay conditions compared to the no-display control condition. Consistent with Hypothesis 1 and 2, and the results from Experiment 1, when Initiators had awareness displays (either abstract or full), they were more likely to pose their questions during periods when the Target had fewer jumpers to manage (Table 2, Row A). However, as also shown in Table 2,

<table><tr><td rowspan="2">Row</td><td rowspan="2">Dependent variable</td><td rowspan="2">N</td><td colspan="3">Team</td><td colspan="3">No team</td><td colspan="2">Differences among display conditions</td><td>Team</td><td colspan="2">Display × team interactions</td></tr><tr><td>No display Mean (SE)</td><td>Abstract Mean (SE)</td><td>Full Mean (SE)</td><td>No display Mean (SE)</td><td>Abstract Mean (SE)</td><td>Full Mean (SE)</td><td>No display vs. display F (SE)</td><td>Abstract vs. full F (SE)</td><td>Team vs. no team F (SE)</td><td>No display vs. display F (SE)</td><td>Abstract vs. full F (SE)</td></tr><tr><td>A</td><td>Initiator interruption timing (number of jumpers on screen during interruption)</td><td>1,480</td><td> $1.95^a$ (0.089)</td><td> $1.60^b$ (0.093)</td><td> $1.69^b$ (0.096)</td><td> $1.98^a$ (0.081)</td><td> $1.93^a$ (0.085)</td><td> $2.02^a$ (0.089)</td><td> $4.50^*$ (0.074)</td><td>0.97(0.089)</td><td> $9.71^{**}$ (0.074)</td><td> $7.79^{**}$ (0.110)</td><td>0.43(0.132)</td></tr><tr><td>B</td><td>Initiator interruptions sent per minute</td><td>390</td><td> $1.64^a$ (0.174)</td><td> $1.53^a$ (0.174)</td><td> $1.36^a$ (0.174)</td><td> $2.05^b$ (0.183)</td><td> $2.04^b$ (0.180)</td><td> $1.80^b$ (0.179)</td><td>2.42(0.108)</td><td>2.88(0.210)</td><td> $4.67^*$ (0.144)</td><td>1.86(0.144)</td><td>0.96(0.168)</td></tr><tr><td>C</td><td>% jumpers saved by Targets</td><td>390</td><td> $53.2^a$ (2.79)</td><td> $59.2^b$ (2.78)</td><td> $63.3^b$ (2.79)</td><td> $50.3^a$ (2.92)</td><td> $53.2^a$ (2.87)</td><td> $54.4^a$ (2.86)</td><td> $11.03^{***}$ (1.75)</td><td>1.76(1.99)</td><td>3.31(3.28)</td><td> $11.32^{***}$ (2.40)</td><td>2.18(2.76)</td></tr><tr><td>D</td><td>Accuracy of Initiators&#x27; puzzle performance</td><td>390</td><td> $54.0\%^a$ (6.29)</td><td> $50.5\%^a$ (6.25)</td><td> $58.2\%^a$ (6.26)</td><td> $43.1\%^a$ (6.65)</td><td> $50.8\%^a$ (6.49)</td><td> $56.4\%^a$ (6.44)</td><td>1.01(5.36)</td><td>1.19(6.11)</td><td>0.54(5.61)</td><td>0.002(7.39)</td><td>0.83(8.51)</td></tr><tr><td>E</td><td>Time for Initiators&#x27; puzzle performance</td><td>390</td><td> $149^a$ (10.6)</td><td> $160^a$ (10.5)</td><td> $141^a$ (10.5)</td><td> $165^a$ (11.2)</td><td> $156^a$ (10.9)</td><td> $143^a$ (10.8)</td><td>0.70(8.72)</td><td>2.57(9.94)</td><td>0.18(9.88)</td><td>0.006(12.0)</td><td>1.83(13.8)</td></tr></table>

†  
Table 2 Performance Results for Experiment 2 †

Row A and in Figure 3(a), the effects of the awareness displays depended upon the team manipulation. The awareness displays caused Initiators to communicate during periods of low workload only in the team condition, but not in the individual condition.

Interruption Rate. Initiators asked fewer questions per minute of Targets in the team condition than in the individual condition (Table 2, Row B). However, unlike Experiment 1, Initiators asked approximately the same number of questions per minute when they had information about Targets’ workload (in the abstract and full-display conditions) as when they did not (no-display condition).

Target Performance. Consistent with Hypothesis 1, Targets’ performance improved significantly when Initiators received information about Targets’ workload and used that information (see Table 2, Row C). They were able to save approximately 10% more jumpers in the abstract and full-display conditions than in the no-display condition, also supporting Hypothesis 2. Targets saved 11% more jumpers in the Team condition than in the Independent condition.

These main effects of the display and team manipulations must be qualified by the significant displayby-team interaction shown in Figure 3(b). Consistent with Hypothesis 5, the awareness displays improved Targets’ performance only when Initiators believed that they were operating as a team with their Targets (Table 2, Row C, last column). Because only Initiators were exposed to the Team manipulation and all Targets believed they were working as a team with their partners, the influence of the Team manipulation on Targets’ performance must have been mediated by the changes in Initiators’ communication rate and timing.

Attentional Demand—Gaze. Overall, from our eyetracking data we found more glances were directed to the display area of the screen when a display was present, and more attention was paid to the display area of the screen with the full display versus the abstracted one. There were no main effects for team, or team-by-display interactions, so we do not report the gaze results for the team manipulation.

Proportion of Fixations. Consistent with Hypothesis 3, Initiators in the full-display condition increased their attention to the awareness display compared to Initiators in the abstract-display condition (Area B in dition, they were not using the display to time their communications.

Figure 3 (a) Experiment 2—Jumpers on Screen When Interruption Occurred by Display Condition, (b) Experiment 2—Percent Jumpers Saved by Target by Display Condition  
![](/api/attachments/CM5WNGPU/fulltext/images/a5657ea8791a88a901635edbd7a19b11f386d25618a77fb4a3ea858a3fcd5f0c.jpg)

![](/api/attachments/CM5WNGPU/fulltext/images/d036ed948b7d74809d5ae2cbf9cfac3477380e9602d38a6b15bba43ebb59aa98.jpg)  
Figure 2(a); see also Table 3, Row A). The increased proportion of fixations on the full display indicates its prominence on screen and its level of visual attention demand. Correspondingly, Initiators in the full-display condition dropped their attention to the primary task—guessing the identity of the revealing picture. They fixated significantly less on their primary task area (Area D in Figure 2(a); Table 3, Row B). This result suggests that the full information awareness display distracted Initiators from their primary task even though, in the independent con-

Table 3 Eye-Tracking for Experiment 2<sup>†</sup>

<table><tr><td rowspan="2">Row</td><td rowspan="2">Dependent variable</td><td rowspan="2">Element of interest</td><td colspan="3">Team</td><td colspan="3">Non-team</td><td colspan="3">Statistics</td></tr><tr><td>None</td><td>Abstract</td><td>Full</td><td>None</td><td>Abstract</td><td>Full</td><td>Abstract vs. full F(1,33)</td><td>Team vs. no team</td><td>Display × team interaction</td></tr><tr><td>A</td><td>Proportion of fixations (percent)</td><td>Awareness display</td><td> $17.0^a$ (1.61)</td><td> $17.0^a$ (1.61)</td><td> $17.8^a$ (1.61)</td><td> $16.0^a$ (1.89)</td><td> $16.2^a$ (1.89)</td><td> $21.2^b$ (1.89)</td><td>5.91*(1.25)</td><td>0.067(2.02)</td><td>1.9936(1.65)</td></tr><tr><td>B</td><td></td><td>Primary task</td><td> $66.8^a$ (2.72)</td><td> $67.7^a$ (2.72)</td><td> $67.8^a$ (2.72)</td><td> $65.2^a$ (3.19)</td><td> $66.4^a$ (3.19)</td><td> $60.1^b$ (3.19)</td><td>4.29*(1.49)</td><td>0.85(3.82)</td><td>2.854(1.9643)</td></tr><tr><td>C</td><td>Mean fixation duration (msec)</td><td>Awareness display</td><td> $301^a$ (0.1433)</td><td> $288^a$ (0.1433)</td><td> $324^a$ (0.143)</td><td> $332^a$ (0.168)</td><td> $275^a$ (0.168)</td><td> $343^a$ (0.168)</td><td>1.85(0.125)</td><td>0.049(0.1671)</td><td>0.1806(0.140)</td></tr><tr><td>D</td><td></td><td>Primary task</td><td> $306^a$ (0.149)</td><td> $298^a$ (0.149)</td><td> $376^b$ (0.149)</td><td> $335^a$ (0.175)</td><td> $276^a$ (0.175)</td><td> $390^b$ (0.175)</td><td>4.77*(0.133)</td><td>0.0099(0.171)</td><td>0.2114(0.115)</td></tr></table>

<sup>†</sup>Different superscripts a b c	 in the same row indicate significant differences between values (p < 005	. $^ { * } p < 0 . 0 5 ; ^ { * * } p < 0 . 0 1 ; ^ { * * * } p < 0 . 0 0 1 .$

Table 4 Summary of Support for Stated Hypotheses Across Experiment 1 and 2

<table><tr><td>Hypothesis</td><td>Supported in Experiment 1?</td><td>Supported in Experiment 2?</td></tr><tr><td colspan="3">Awareness display design</td></tr><tr><td>Hypothesis 1: Displays showing a Target&#x27;s workload will allow Initiators to time their communication so that it arrives during periods of lower workload in the Target&#x27;s task.</td><td>Yes</td><td>Yes</td></tr><tr><td>Hypothesis 2: Abstracted information displays showing a simple representation of a target&#x27;s workload should allow initiators to assess availability and time communication so that it arrives during periods of lower workload equally as well as or better than a full video display that shows more information about a Target&#x27;s work activities.</td><td>Yes</td><td>Yes</td></tr><tr><td>Hypothesis 3: An increase in the amount of information in an on-screen display of Target status (with respect to number of elements and movement) will increase the amount of visual attention required to attend to the display and obtain information from it.</td><td>Not tested</td><td>Yes</td></tr><tr><td>Hypothesis 4: An increase in the amount of information in an on-screen display of Target status should result in decreased primary task performance of the Initiator on continuous attention tasks.</td><td>Yes</td><td>No</td></tr><tr><td colspan="3">Incentive</td></tr><tr><td>Hypothesis 5: Common social identity and outcome interdependence will cause Initiators to use awareness displays to time communication so it arrives during periods of low workload for the Target.</td><td>Not tested</td><td>Yes</td></tr></table>

Mean Fixation Duration. The average fixation duration, or how long each glance lasted on average, in the display area was about 10% longer for the full condition than for the other two conditions (Table 3, Row C), but this difference was not significant. Initiators had fixations in the primary task area (Area D in Figure 2(a)) that were 36% longer when they were using the full display than in the abstract one (see

Table 3, Row D). These data show that dealing with the informationally rich full display, whether or not it was being used for communication timing, seems to have increased participants’ cognitive load, making the primary task more challenging.

Initiator Performance. Initiators’ performance was measured by the accuracy in their identification of the picture puzzles and the time, in seconds, it took them to identify each picture. There were neither main effects (see Table 2, Rows D and E) nor interactions of the awareness display condition and team manipulation on the Initiators’ accuracy or speed at identifying pictures. In contrast to Experiment 1, Initiators performance in Experiment 2 was not influenced by the presence of the full information display, and thus Hypothesis 4 was not supported.

Summary. Experiment 2 showed that Initiators in the Team condition used the workload displays to time their interruptions more accurately (when their partners were less busy), while Initiators in the Independent condition did not do so to the same extent. This difference in interruption behavior resulted in a significant performance benefit for Targets only during the Team condition. The eye-tracking data showed that the full information display consumed substantially more attention than the abstract information display for Initiators in the Independent condition and increased Initiator cognitive load in both Team and Independent conditions.

## Discussion

The studies presented here sought to address three open research questions: (1) Can awareness displays with information about a co-worker’s activities help coordinate communication? (2) How should they best be designed to do so? (3) Under what social conditions will people use them in this fashion? Table 4 summarizes the empirical results of the studies presented and support for the hypotheses aimed at addressing the three questions above. We found that under conditions of shared rewards and common identity, awareness displays showing a communication target’s workload were beneficial for reducing the disruption associated with interruption. In both Experiment 1 and 2 the targets of interruptions performed better when the Initiators had information about the Targets’ workload and, in Experiment 2, when the Initiators had social incentives to use that information. Our results from both Experiment 1 and 2 also show that a display with abstract representations of potential communication targets’ activity is as useful for coordinating communication as a display showing everything that partners were doing. In addition, we found that the full display, showing everything that the potential target was doing, was distracting to those initiating communication. In Experiment 1, the full display negatively affected Initiators’ performance compared to the abstract one, and in Experiment 2, it consumed substantially more visual attention, was more cognitively demanding, and reduced the amount of attention the initiators paid to their primary task.

These results have practical implications for the way information technology can be used to coordinate communication, especially in distributed-work settings. The conclusions we can draw from the results go beyond the design of awareness display technology. We have learned something about the granularity of information required for communication timing online. Researchers examining interruptions in field settings have highlighted the detailed way in which people draw inferences from the rich behavior they observe in face-to-face settings (e.g., Kraut et al. 1990). For example, Heath and colleagues, examining the interactions in a London dealing room, suggested that individuals require extremely detailed information about their coworkers’ activities to coordinate interaction appropriately and avoid disruption (Heath et al. 1995). Our research suggests that you don’t need this fine-grained level of detail to strategically time communication; an abstract representation of individuals’ work status may be sufficient.

Our results also tell us something about how the social context surrounding an interaction affects conscientiousness when interrupting. Perlow’s fieldwork on interruption in a software engineering firm (1999) showed that engineers interrupted each other with little regard for their coworkers’ current status, disrupting each other so much that the group missed production deadlines. However, these engineers had little incentive to interrupt conscientiously because they were rewarded based on their individual performance. The research presented here, in contrast, shows that common incentives and identity promoted individuals to pay attention to their partners’ work state before interrupting them. This result could be applied to many work settings where interruption is endemic, by better aligning incentives with decisions to communication. The principle of incentive alignment applies across many types of information system—e.g., failure to use knowledge management systems, failure of ERP systems, etc. Considering the incentive structure surrounding system use allows one to predict when collaboration technology will be successful (Grudin 1994). Organizations can align incentives among actors with potentially conflicting goals through structural changes (e.g., basing compensation on team performance; see Barua et al. 1995, DeMatteo et al. 1998). Alternatively, they can attach incentives directly to the communication behavior, as some firms have done for adding useful information to knowledge management systems (Davenport and Prusak 2000) or has been proposed for pricing of electronic communication (Kraut et al. 2002).

## Implications for the Design of

## Communication Systems

Results from both of our experiments suggest that showing information about others’ task state can help coordinate communication between co-workers. In addition, our results show that “abstract” displays presenting only decision-relevant information about co-workers’ current states were as useful for timing interruptions as displays presenting richer information about co-workers’ current states. Before applying these ideas to real-world awareness displays, we must answer four questions not directly addressed in our empirical research: (1) How can a system gather data about the relevant aspects of a work task to use as the basis of an awareness display? (2) How can a system present the multidimensional data that might be relevant to the decision to communicate with another in ways that minimize distraction? (3) How can a system influence users’ incentives to take communication partners’ welfare into account before attempting a communication? Finally, (4) In what situations will these display be useful (i.e., to what settings do these empirical results generalize?)

Our results illuminate a response to recent critiques of the disconnect between Information Systems research and practice (e.g., Benbasat and Zmud 2003, Orlikowski and Iacono 2001), by showing a way to use empirical research to drive the design of important information technology, as opposed to solely documenting its organizational impact. What is missing from this research program is the fourth stage, translating the abstract design principles we developed and tested into actual information system applications to be deployed and evaluated in real-world settings.

We suggest here how our ideas might be applied. We acknowledge, however, that we present only a sketch of an application. Substantial research, engineering, and iterative design and testing is needed before this sketch is a reality.

Collecting Relevant Information. Although our research showed that providing a display showing a pattern’s availability and busyness can improve the coordination of communication, we could easily assess workload to drive that display only because we controlled the task. This technique cannot apply to the real world. People announce their availability with varying amounts of explicitness: by making their calendars public (Palen and Grudin 2003), by varying the openness of their doors (Fish et al. 1993) or by setting the away indicators on an instant messaging application. These kinds of techniques that rely upon potential communication targets to announce their availability often fail because of forgetfulness and self-interest (Cadiz et al. 2002).

Recent research on automated sensing of availability shows that inexpensive and easily deployable sensors coupled with machine learning techniques can do a reasonable job of assessing an individual’s availability in the workplace (Fogarty et al. 2005, Begole et al. 2003, Horvitz et al. 2003). For example, instantmessenger programs use lack of keyboard activity to set “away” messages, and simple sensors already available on a laptop computer can be combined to assess whether managers or research programmers are interruptible, with over 82% accuracy (Fogarty et al. 2005).

Displaying Relevant Information. An important technology design question is how to distill rich, multidimensional information about an individual’s current activity into a format that is easy to process visually and mentally. In our experiment this was trivial because Targets’ task was one-dimensional with respect to availability, so that workload equated to a directly measurable aspect of their task, the number of jumpers on their screens. If awareness displays needed to signal only potential communication targets’ busyness, the machine learning techniques previously mentioned could map many sources of data onto this single dimension (Horvitz et al. 2003). However, if other aspects of the situation are relevant to the interruption—e.g. whether the target is engaged in a social interaction versus a task—then a single display of busyness or availability would be insufficient. A future research avenue then is investigating how people make use of these one-dimensional assessments of availability in a field setting.

Motivation to Interrupt Sensitively. The results from Experiment 2 show that communication initiators timed their interruptions sensitively only in the team condition, when they were motivated by a shared team identity. A team identity is only one way to motivate people to interrupt at appropriate times. Friendship, reciprocity, joint history, or anticipation of future interaction may all build relationships among people that motivate them to interrupt sensitively.

With interactions among strangers (e.g., the proverbial insurance salesman calling at dinner), one might induce a similar motivation by pricing interruptions. For example, it could become more costly to interrupt people the busier they are (Horvitz et al. 2003). Pricing should regulate the timing of interruptions without revealing information that would compromise targets’ privacy. Previous studies have shown that pricing communications can successfully encourage more selective email communication (Kraut et al. 2002). Perhaps this concept can also be applied to more synchronous forms of communication.

Generalizability. The research described here used a highly stylized task to simulate advice seeking and the kind of interruptive behavior described by Perlow (1999). These results may directly apply to continuous visual attention tasks, and the logic of the analysis may apply more broadly, even if the details of the tasks and displays we used do not.

Awareness displays to coordinate communication may be especially useful for tasks requiring tight coupling between co-workers in a dynamic environment. For example, air traffic controllers, remote surgery team members, and military command-and-control crews must maintain awareness of their colleagues’ activities on a minute-by-minute basis to coordinate communication with them and inform their own actions. Our results indicate that in these settings, where there exists a feeling of common social identity with a team, the use of awareness displays with abstractions representing colleagues’ workloads could enable individuals to make informed decisions when timing their communications, minimizing potential disruption and attention required while maximizing the ability to obtain timely information.

However, because our study was conducted in the laboratory using a stylized task, our results can be generalized only with limitations. In particular, even though the participants played a game in which they were saving the lives of animated characters, in this setting the consequences for mistakes and poor performance were not as serious as in some real-world settings, e.g., air-traffic control. Risk associated with a task may affect attention and communication in a way unanticipated in our experiments. In addition, the interruptions in our studies did not vary in terms of associated task importance, but there is no guarantee that these results would be the same if deadlines and importance associated with interruptions did vary. Finally, we chose to vary only interdependence between the initiator and the target using social identity and reward structure. Many other aspects of the relationship between initiators and targets could affect communication behavior. Future work must examine these other factors, such as power, interaction history, status, role-based norms, reciprocity, liking, etc., and whether they influence communication behavior in the same way that interdependence did in our study.

Implications for the Information Systems Research Although we conducted this research to examine ways to coordinate workplace communication, this paradigm has broader implications for conducting information systems research. In part, it represents one response to recent critiques of the relationship of information systems research to practice and the call for information systems research to focus more directly on technological artifact (Benbasat and Zmud 2003, Orlikowski and Iacono 2001). The dominant theories in information systems are descriptive rather than prescriptive, and therefore do not provide explicit guidance for managers and information systems developers. Consider the Technology Adoption Model (TAM), one of the most highly cited theories in the information systems field (Davis et al. 1989, Venkatesh et al. 2003). While the Technology Adoption Model identifies utility, ease of use, and local norms as predictors of technology adoption within an organization, it does not delineate features of technology that make it either useful or easy to use. Research that focuses on the context of information systems research, including fragmented institutionalism (Lamb and Kling 2003), adaptive structuration theory (DeSanctis and Poole 1994), or research that takes a practice lens perspective, is useful for retrospectively explaining why a technology was successful or not (Orlikowski 1992) or was used in unexpected ways. But it provides little practical guidance in either designing or managing the use of information technology in organizations. The approach we adopt here, like the contextual approaches just reviewed, acknowledges potential conflict among organizational actors but goes beyond this observation to integrate conflict between actors into the design of technology.

The theory we used and developed in this research was directed in the service of designing information systems interventions to deal with problems of communication-based interruption. Our approach consists of three steps. First, we mined research and theory in organizational behavior, especially on management communication and on distributed teams, to better understand the trade-offs between communication and interruption that these systems must support. Second, this task analysis caused us to focus on two components of a system to manage these trade-offs— information about co-workers’ task environments and incentives that would cause co-workers to care about each other’s welfare. Third, we conducted two behavioral experiments, which showed that at a conceptual level the features of an information display showing a co-worker’s workload, which we identified, combined with appropriate incentives, indeed does improve communication coordination without overwhelming users of the display.

## Acknowledgments

The authors thank the senior editor, associate editor, and three anonymous reviewers for their exceptionally helpful reviews; Daniel McFarlane for his insightful comments and the use of his Jumpers game task; and the National Defense Science and Engineering Graduate Fellowship program and the National Science Foundation (grant IIS-0325351) for funding this work.

## References

Abel, M. J. 1990. Experiences in an exploratory distributed organization. C. Egido, ed. Intellectual Teamwork: Social and Technological Foundations of Group Work. Lawrence Erlbaum Associates, Hillsdale, NJ, 489–510.

Adamczyk, P. D., B. P. Bailey. 2004. If not now when?: The effects of interruption at different moments within task execution. Proc. Conf. Human Factors Comput. Systems CHI 2004, ACM Press, New York, 271–278.

Barua, A., C. H. S. Lee, A. B. Whinston. 1995. Incentives and com puting systems for team-based organizations. Organ. Sci. 6(4) 487–504.

Begole, B., J. Tang, R. Hill. 2003. Rhythm modeling, visualizations, and applications. Proc. Annual Sympos. User Inter. Software Tech. UIST 2003, ACM Press, New York, 11–20.

Benbasat, B., R. Zmud. 2003. The identity crisis within the IS discipline: Defining and communicating the discipline’s core properties. MIS Quart. 27(2) 183–194.

Cadiz, J. J., G. Venolia, G. Jancke, A. Gupta. 2002. Designing and deploying an information awareness interface. Proc. Conf. Comput. Supp. Coop. Work CSCW 2002, ACM Press, New York, 314–323.

Cramton, C. 2001. The mutual knowledge problem and its consequences for distributed collaboration. Organ. Sci. 12(3) 346–371.

Davenport, T. H., L. Prusak. 2000. Knowledge management projects in practice. Working Knowledge. Harvard Business School Press, Cambridge, MA, 144-161.

Davis, F. D., R. P. Bagozzi, P. R. Warshaw. 1989. User acceptance of computer technology: A comparison of two theoretical models. Management Sci. 35(8) 982–1003.

Dawes, R. 1979. The robust beauty of improper linear models in decision making. Amer. Psych. 34 571–582.

DeMatteo, J. S., L. T. Eby, E. Sundstrom. 1998. Team-based rewards: Current empirical evidence and directions for future research. B. M. Staw, L. L. Cummings, eds. Research in Organizational Behavior: An Annual Series of Analytical Essays and Critical Reviews, Vol. 20. JAI Press, Greenwich, CT, 141–183.

DeSanctis, G., M. S. Poole. 1994. Capturing the complexity in advanced technology use: Adaptive structuration theory. Organ. Sci. 5(2) 121–147.

Dourish, P., S. Bly. 1992. Portholes: Supporting awareness in a distributed work group. Proc. Conf. Human Factors Comput. Systems CHI 1992, ACM Press, New York, 541–547.

Endsley, M. R. 1995. Toward a theory of situation awareness in dynamic systems. Human Factors 37(1) 32–64.

Fish, R. S., R. E. Kraut, R. W. Root, R. Rice. 1993. Evaluating video as a technology for informal communication. Comm. ACM 36(1) 48–61.

Fogarty, J., J. Lai, J. Christensen. 2004. Presence versus availability: The design and evaluation of a context-aware communication client. Internat. J. Human-Comput. Stud. 61(3) 299–317.

Fogarty, J., A. Ko, H. H. Aung, E. Golden, K. Tang, S. Hudson. 2005. Examining task engagement in sensor-based statistical models of human interruptibility. Proc. Conf. Human Factors Comput. Systems CHI 2005, ACM Press, New York, 331–340.

Gillie, T., D. Broadbent. 1989. What makes interruptions disruptive? A study of length, similarity, and complexity. Psych. Res. 50(4) 243–250.

Grudin, J. 1994. Groupware and social dynamics: Eight challenges for developers. Comm. ACM 37(1) 92–105.

Heath, C., M. Jirotka, P. Luff, J. Hindmarsh. 1995. Unpacking collaboration: The interactional organization of trading in a city dealing room. Comput. Supp. Coop. Work 3(2) 147–165.

Henry, K. B., H. Arrow, B. Carini. 1999. A tripartite model of group identification: Theory and measurement. Small Group Res. 30(5) 558–581.

Hinds, P., D. Bailey. 2003. Out of sight, out of sync: Understanding conflict in distributed teams. Organ. Sci. 14(6) 615–632.

Horvitz, E., C. Kadie, T. Paek, D. Hovel. 2003. Models of attention in computing and communication: From principles to applications. Comm. ACM 46(3) 52–59.

Hudson, S., I. Smith. 1996. Techniques for addressing fundamental privacy and disruption tradeoffs in awareness support. Proc. Conf. Human Factors Comput. Systems CHI 1996, ACM Press, New York, 248–257.

Jacob, R. J. K., K. S. Karn. 2003. Eye tracking in human-computer interaction and usability research. J. Hyona, R. Radach, H. Deubel, eds. The Mind’s Eye: Cognitive and Applied Aspects of Eye Movement Research. Elsevier Science, Amsterdam, 573–605.

Jang, C., C. Steinfield, B. Pfaff. 2002. Virtual team awareness and groupware support: An evaluation of the TeamSCOPE system. Internat. J. Human-Comput. Stud. 56(1) 109–126.

Kane, A. A., L. Argote, J. Levine. 2005. Knowledge transfer between groups via personnel rotation: Effects of social identity and knowledge quality. Organ. Behav. Human Decision Processes 96(1) 56–71.

Kraut, R. E., P. Attewell. 1997. Media use in a global corporation: Electronic mail and organizational knowledge. S. Kiesler, ed. Culture of the Internet. Lawrence Erlbaum, Mahwah, NJ, 323–342.

Kraut, R. E., R. Fish, R. Root, B. Chalfonte. 1990. Informal communication in organizations: Form, function, and technology. S. Oskamp, S. Spacapan, eds. Human Reactions to Technology: Claremont Symposium on Applied Social Psychology. Sage Publications, Beverly Hills, CA, 145–199.

Kraut, R. E., J. Morris, R. Telang, D. Filer, M. Cronin, S. Sunder. 2002. Markets for attention: Will postage for email help? Proc. Conf. Comput. Supp. Coop. Work CSCW 2002, ACM Press, New York, 206–215.

Lamb, R., R. Kling. 2003. Reconceptualizing users as social actors in information systems research. MIS Quart. 27(2) 197–235.

Matthews, T., T. Rattenbury, S. Carter. 2007. Defining, designing, and evaluating peripheral displays: An analysis using activity theory. Human-Comput. Inter. 22(1) 221–261.

McFarlane, D. 2002. Comparison of four primary methods for coordinating the interruption of people in human-computer interaction. Human-Comput. Inter. 17(1) 63–139.

Olson, G. M., J. S. Olson. 2000. Distance matters. Human-Comput. Inter. 15(2) 139–178.

Orlikowski, W. 1992. Learning from notes: Organizational issues in groupware implementation. Proc. Conf. Comput. Supp. Coop. Work CSCW 1992, ACM Press, New York, 362–369.

Orlikowski, W. J., C. S. Iacono. 2001. Research commentary: Desperately seeking the “it” in it research—A call to theorizing the it artifact. Inform. Systems Res. 12(2) 121–134.

Palen, L., J. Grudin. 2003. Discretionary adoption of group support software: Lessons from calendar applications. Implementing Collaboration Technologies in Industry Case Examples and Lessons Learned. Springer-Verlag, London, 159–179.

Pashler, H., J. Johnston, E. Ruthruff. 2001. Attention and performance. Annual Rev. Psych. 52 629–651.

Perlow, L. A. 1999. The time famine: Toward a sociology of work time. Admin. Sci. Quart. 44(1) 57–81.

Powell, A., G. Piccoli, B. Ives. 2004. Virtual teams: A review of current literature and directions for future research. Database for Adv. Inform. Systems 35(1) 6–36.

Real VNC. 2002. http://www.realvnc.com/what.html.

Rosenthal, R., R. L. Rosnow. 1991. Essentials of Behavioral Research: Methods and Data Analysis, 2nd ed. McGraw-Hill, New York.

Speier, C., I. Vessey, J. S. Valacich. 2003. The effects of interruptions, task complexity, and information presentation on computersupported decision-making performance. Decision Sci. 34(4) 771–797.

Sproull, L. 1984. The nature of managerial attention. L. Sproull, J. Larkey, eds. Advances in Information Processing in Organizations. JAI Press, Greenwich, CT, 9–27.

Tang, J. C., E. A. Isaacs, M. Rua. 1994. Supporting distributed groups with a montage of lightweight interactions. Proc. Conf. Comput. Supp. Coop. Work CSCW 1994, ACM Press, New York, 23–34.

Van der Vegt, G., B. Emans, E. Van de Bliert. 1998. Motivating effects of task and outcome interdependence in work teams. Group Organ. Management 23(2) 124–143.

Venkatesh, V., M. G. Morris, G. B. Davis, F. D. Davis. 2003. User acceptance of information technology: Toward a unified view. MIS Quart. 27(3) 425–478.

Walther, J. B., C. Slovacek, L. C. Tidwell. 2001. Is a picture worth a thousand words? Photographic images in long term and short term virtual teams. Comm. Res. 28(1) 105–134.

Wickens, C. D., S. E. Gordon, Y. Liu. 1998. An Introduction to Human Factors Engineering. Addison-Wesley, New York.

Zheng, J., E. Veinott, N. Bos, J. S. Olson, G. Olson. 2002. Trust without touch: Jumpstarting long-distance trust with initial social activities. Proc. Conf. Human Factors Comput. Systems CHI 2002, ACM Press, New York, 141–146.
