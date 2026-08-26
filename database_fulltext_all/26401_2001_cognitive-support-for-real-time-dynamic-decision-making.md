---
otero_id: 26401
otero_key: "YBKWZRG8"
title: "Cognitive Support for Real-Time Dynamic Decision Making"
authors: "F. Javier Lerch; Donald E. Harter"
year: "2001"
journal: "Information Systems Research"
doi: "10.1287/isre.12.1.63.9717"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [130.113.86.233] On: 13 March 2015, At: 07:24 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

## 6SR

## Information Systems Research

![](/api/attachments/YBKWZRG8/fulltext/images/dca41ad8ced1da8741dcddb97ce2a58a994c582f68a7cb805eb13f5304092bbf.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Cognitive Support for Real-Time Dynamic Decision Making

F. Javier Lerch, Donald E. Harter,

## To cite this article:

F. Javier Lerch, Donald E. Harter, (2001) Cognitive Support for Real-Time Dynamic Decision Making. Information Systems Research 12(1):63-82. http://dx.doi.org/10.1287/isre.12.1.63.9717

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 2001 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/YBKWZRG8/fulltext/images/0ed0232e9092666c2ea9567fe40f316adcd28fa9103b4c40a14fd37b1252778f.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Cognitive Support for Real-Time Dynamic Decision Making

F. Javier Lerch • Donald E. Harter

Center for Interactive Simulations, Graduate School of Industrial Administration, Carnegie Mellon University, Pittsburgh, Pennsylvania 15213

University of Michigan Business School, Ann Arbor, Michigan 48109 lerch@andrew.cmu.edu. • harter@umich.edu

making a series of interdependent decisions in a real-time environment. Decision strategies for real-time dynamic tasks consist of two main overlapping cognitive activities: monitoring and control. Monitoring refers to decision makers’ tracking of key system variables as they work toward arriving at a decision. Control refers to the decision maker’s generation, evaluation, and selection of alternative actions. In real-time tasks, these two activities compete for the same attentional resources. The questions that motivate the two studies presented here are: (1) can decision making be improved by increasing individuals’ attentional resources, thereby enhancing their ability to monitor the system, and (2) can decision making be improved by providing individuals with feedback and/or feedforward control support? Our findings show that some kinds of cognitive support degrade performance, rather than enhance it. These results indicate that providing support for real-time dynamic decision making may be very difficult, and that designing effective decision aids requires a detailed understanding of the underlying cognitive processes.

(Decision Support; Dynamic Decision Making; Real-Time Environments; Individual Differences)

## 1. Introduction

Recent developments in information technology have changed the balance between the relative costs of producing and consuming information. With current technologies, information is generated faster than individuals and organizations can make sense of it. As these technologies have become more powerful, organizations are able to collect detailed information about realtime events even as the events unfold. For example, UPS can track in real-time the movements of every package from pickup to delivery. This information can improve routing if decision makers can take advantage of it.

The challenge for contemporary organizations is not to collect more information, but to utilize it better. The consumption of information is limited by the attentional resources of human decision makers, especially as they perform in real-time environments where speed is essential. Thus, information technology has mitigated the relative scarcity of one resource—information—and has created scarcity in another—human attention. This reversal requires that we direct our efforts towards becoming more effective consumers, rather than producers, of information. To do this we need to understand how to enhance our ability to consume large quantities of information in complex, realtime technological environments.

This research investigates the management of attentional resources in a Real-Time Dynamic Decision Making (RTDDM) tasks. We characterize RTDDM as a stream of interdependent decisions to be made in real-time. We measure the quality of these interdependent decisions by considering the decision makers’ overall management of the system in question, rather than by the quality of their individual decisions. To make decisions in RTDDM tasks, individuals use decision strategies comprised of two overlapping cognitive activities: monitoring and control. Monitoring refers to the decision-makers’ tracking of key system variables as they work towards arriving at a particular decision. Here, an individual perceives and keeps track of relevant elements in the decision environment. Control, on the other hand, refers to the decision-makers generation, evaluation, and selection of alternative actions that can change the system. In real-time tasks, these two cognitive activities compete for the decisionmaker’s attentional resources.

In this paper, we present two laboratory studies that investigate how to help decision makers in RTDDM tasks. The first study examines how individuals with high and low working memory capacity adapt their decision strategies as they perform in a high-workload task. Working memory (WM) is defined by Baddeley (1986) as “a system for the temporary holding and manipulation of information during the performance of a range of cognitive tasks such as comprehension, learning and reasoning” (italics added). Limitations in WM have long been recognized as a major bottleneck in human information processing (Miller 1956, Broadbent 1958), Peterson and Peterson 1959). This study compares how individuals with different WM capacities allocate their attentional resources either to monitor or to control a system.

The second study examines how feedback and feedforward, two kinds of cognitive support, can help or hinder decision making in RTDDM tasks. In this study, the goal was to find how feedback and feedforward support could enhance learning by helping decision makers improve their evaluation of decision alternatives, or conversely consume too many scarce attentional resources, thus hindering learning and/or degrading performance.

The next section presents our theoretical view of attentional resource management in RTDDM tasks. Section 3 describes briefly the real-world task and the apparatus used in the two laboratory studies. Sections 4 and 5 present the two studies and their results. In the final section, we discuss the implications of our findings for the design of computer-based decision aids to support the management of limited attentional resources in real-time dynamic decision making.

## 2. Adaptation in Real-Time Dynamic Decision Making

This section presents our theoretical view of attentional resource management in RTDDM tasks. We begin with a brief explanation of the complexity of RTDDM tasks, and of the burden they place on a decision-maker’s attentional resources. To understand cognitive effort in RTDDM tasks, it is necessary to understand Working Memory (WM), and so we continue with a discussion of WM and its role in complex cognitive tasks. Since an individual’s allocation of WM to specific cognitive activities is important in RTDDM, we move on to present Endsley’s (1995) three levels of situational awareness. These levels of situational awareness permit us to distinguish among the different levels of demands made on a decision-maker’s attentional resources. Finally, we can then ask how supporting these demands through computer-based decision aids might improve individuals’ abilities to improve decision making.

## Real-Time Dynamic Decision Making

RTDDM is defined as a decision task that requires a series of interdependent decisions in a continuously changing environment. Real-time dynamic decisionmaking tasks have four key characteristics: (1) the tasks require a series of decisions; (2) the decisions are interdependent; (3) the environment changes autonomously and as a result of decisions; and (4) decisions are made in real-time (Brehmer 1990, 1992; Edwards 1962). RTDDM tasks have been studied from the perspective of control theory (Brehmer 1990, 1992; Hogarth 1986), feedback (Sterman 1989a,b, Hogarth et al. 1991), and computational frameworks (Gibson et al. 1997).

In RTDDM tasks, a decision-maker’s management of limited attentional resources plays a key role because decisions are interdependent, and because the pacing of the decisions is dictated by the environment. To complicate matters, attentional resources are utilized simultaneously as the decision maker acquires decision strategies (i.e., learns), and as that decision maker selects and refines these strategies during task execution. Because each decision changes the future decision space, and because the environment changes continuously, decision makers are forced to spend a great deal of their attentional resources monitoring the environment to determine when a decision should be made, and assessing the impact of both prior decisions (feedback control), and of potential decisions (feedforward control). Adaptation in RTDDM tasks can be portrayed as decision-makers’ learning and executing decision strategies that do not exceed the decision-makers’ available attentional resources.

RTDDM tasks can be categorized along several dimensions: clarity of goal, structure of task, task complexity, level of uncertainty, and time pressure. Tasks with clear goals and means to measure success should simplify strategy selection by an individual. Tasks with well-defined structure, such as scheduling problems, are more amenable to analytical solutions, as opposed to problems with more ambiguous criteria, such as identification of strategic marketing direction of a corporation. Complex tasks involving intricate interactions of decisions will require a better understanding of causal relationships than simple sequential tasks. The level of uncertainty of future events and consequences of current actions will limit an individual’s ability to learn causal relationships and inhibit learning. Time pressure (i.e., the reduction of time allowed to make decisions), limits the number of options considered in making a decision. Operations-oriented business issues will tend to have high clarity of goals, moderately high structure of tasks, moderate complexity due to interactions, some uncertainty of future environment, and moderate time pressure.

## Working Memory (WM)

The dominant models of WM in the sixties were based on the underlying assumption that WM consisted of a small number of fixed slots in which information could be temporarily held. Miller’s classic paper The Magical Number Seven (1956), stimulated interest in the limits of WM capacity. In 1965, Waugh and Norman developed a model of human memory that included a shortterm store (their version of WM) with a small number of fixed slots. In their model, items entered the shortterm store and got lost, either by decay over time or by being displaced by new items. To counteract the decay process, items could be maintained in the shortterm store by rehearsal.

Baddeley and Hitch (1974) modified this view of WM as a fixed-slot storage structure. Their model emphasizes the dual purpose of WM, that is, the storage and processing of information. Since then, WM has been viewed as the crucial interface between memory and cognition (Baddeley 1992). WM is a system in which sensory information is integrated with prior knowledge to make sense of the world and to perform complex cognitive tasks. Given this current view, measuring WM requires tasks that manipulate both the storage and the processing of information. Modern measures of WM have been shown to be very highly correlated with processing speed and performance on a range of reasoning tasks that have traditionally been used for measuring intelligence (Kyllonen and Christal 1990). In our current research, we use a measure of dynamic WM developed by Daneman and Carpenter (1980). Several studies have shown that this measure is capable of explaining and predicting human performance in a variety of complex tasks with substantial WM demands, for example, in psychometric mentalrotation tasks (Just and Carpenter 1985), online language comprehension (Just and Carpenter 1992), and phone-based interaction (Huguenard et al. 1997).

The first step for designing decision aids to support RTDDM would be to increase the availability of WM capacity by using computer-based tools to increase external memory. External memory is defined as the information in foveal view that augments WM (Newell and Simon 1972). The rationale for augmenting external WM with computer aids is that increasing effective WM capacity would lower the costs of cognitively demanding decision strategies, thereby inducing decision makers to adopt them. The quality of cognitive support in RTDDM, however, should depend not only on the magnitude of the attentional resources but also on their allocation. Having extra WM capacity is useless if it is not spent wisely in the acquisition and execution of decision strategies.

In the last decade, researchers studying real-time decision tasks such as air traffic control, fire fighting, and command and control in military operations have developed a concept called situational awareness (Press 1986, Endsley 1987). Situational awareness is closely linked to WM (the ability to store and process information in real-time). Situational awareness is the ability to know what is going on in a real-time dynamic environment. More formally, it refers to the knowledge a person has, at any given point in time, of the state and the dynamics of a real-time system. Obviously, this knowledge must be updated as the system changes, and knowledge updating consumes a significant proportion of an individual’s WM capacity. We use this concept of situational awareness to propose a general framework for supporting RTDDM by either lowering the costs of executing decision strategies or by enhancing their benefits.

## Levels of Situational Awareness

Endsley (1995) distinguishes among three levels of situational awareness. The first of our studies examines questions raised by the first level (monitoring); the second explores issues raised by the second and third levels (control).

The first level of situational awareness is the ability to perceive the status, attributes, and dynamics of relevant elements in the environment, that is, to monitor the environment effectively. For example, automobile drivers learn, through time, decision strategies for allocating attentional resources to those cues in the road that are most important. At this level of situational awareness poor monitoring alone may result in poor performance. Providing individuals with cognitive support at this level can be achieved either by increasing attentional resources, so that monitoring is less expensive, or by changing how information is made available, so that even with existing resources less cognitive effort is required.

The second and third levels of situational awareness involve the capacity to comprehend, respectively, the current and future situations. The second level of situational awareness to comprehend the current situation as it develops is based on the synthesis of elements being perceived in the first level. A key factor in an individual’s comprehension of a real-time dynamic system is the processing of the feedback made available by that system. For example, many studies have shown that delays in performance feedback greatly degrade system understanding and performance (Brehmer 1990; Brehmer and Allard 1991; Sterman 1989a,b; Diehl and Sterman 1995). In addition to feedback timing, the granularity of the feedback is also important. Performance feedback may be provided either by an overall performance measure, or by breaking this overall measure down into the performance of subsystems. Having greater specificity of feedback allows decision makers to credit the particular decisions that improved or degraded performance. Also, proper credit assignment helps decision makers to estimate the benefits of alternative decision strategies, switch among alternative decision strategies if necessary, and improve performance. It is possible, however, that specific feedback may have a negative impact on performance, since more attentional resources are devoted to monitoring and processing the available feedback. In this case, the individual’s control of the system may be degraded because more attentional resources are spent assessing the value of prior decisions.

The third level of situational awareness is the ability to project the future status of the environment as it depends on alternative decisions. This ability has been called feedforward in the RTDDM literature. Brehmer (1990) distinguishes between feedback control and feedforward control, that is, between decision-makers’ control of the system through feedback on the one hand, and their control of the system through feedforward on the other. He defines feedback control as an individual’s selection of an action on the basis of current information about the system. Feedforward control refers to the individual’s selection of an action on the basis of predictions of the future state of the system. In our framework, both feedback control and feedforward control represent families of decision strategies. Brehmer (1990) argues that decision makers are more likely to adopt feedback control than feedforward control as a general decision strategy because the former requires less effort. He also suggests that if any feedback control strategy accomplishes the task at a reasonable level of success, decision makers may not even attempt feedforward, a more cognitively demanding strategy. We would expect decision makers to improve their performance if they could implement feedforward in addition to feedback control; for they could thereby better evaluate and select decision strategies. As with feedback, however, feedforward also consumes attentional resources, and so performance may be similarly degraded if the decision maker expends too much time and energy searching and evaluating the future decision space. This situation is exacerbated because decision spaces in dynamic decision environments usually grow in a combinatorial fashion.

A consideration of the first level of situational awareness (monitoring) led us to ask how increasing decision-makers’ attentional resources (WM) might permit them to better monitor important features of the decision situation. To address this question, we compared the quality of monitoring and performance of individuals with either low-WM or high WM capacity. In general, we expected high WM individuals to be better than low WM individuals at monitoring RTDDM environments. If this were the case, computer support for RTDDM could theoretically be provided by augmenting the decision-maker’s effective WM.

A consideration of the second and third levels of situational awareness (control) led us to ask how facilitating decision-makers’ feedback and feedforward support through decision aids could help improve their decision making. Feedback can be made more specific and more timely through the swifter collection, processing, and delivery of more information. Our question then becomes how much feedback is beneficial to decision makers as they operate in RTDDM tasks, and how often should it be delivered? Similarly, feedforward support may be provided through simulation aids that project future states of the system. (Such support, of course, reduces the decision-maker’s need to simulate future states inside his or her head.) Consequently, another question arises: Are the benefits of looking into the future greater than the cost of allocating attentional resources to search the future decision space? In our second study, we address these questions by manipulating both feedback and feedforward support. We expected that feedforward support would be valuable only if it was provided in conjunction with feedback support. In fact, we expected feedforward to be too cognitively expensive if the decision maker did not have the appropriate feedback to estimate the value of alternative future states. We estimated that in the worst-case scenario decision makers with too much feedforward control could get lost in the combinatorial decision space of RTDDM tasks.

In summary, our first experiment tested the impact of WM capacity in monitoring a real-time system (the first level of situational awareness). Because WM capacity is the ability to store and process information, we expected individuals with high WM capacity to be more effective at tracking system changes, which would indicate that cognitive support in RTDDM tasks can be achieved by designing external aids that increase external WM for monitoring the system. Our results did not support this hypothesis. Therefore, in the second experiment we manipulated feedback and feedforward support (the second and third level of situational awareness) to test the notion that the best way to improve performance and learning in RTDDM tasks is to support higher levels of situational awareness. In this second experiment we controlled for the quality of system monitoring to isolate the effect of feedback and feedforward support.

## 3. Experimental Environment

For both studies, we designed an animation tool that reproduces one mail-sorting factory of the United States Postal Service (USPS). The main goal of the factory is to sort incoming mail to meet two requirements for each mail destination: first, a prespecified depthof-sort (for example, mail sorted to the local post office level or to the mail carrier within the local post office) and, second, a dispatch time (that is, the time when the delivery truck for a particular post office leaves the sorting factory). The USPS has a network of 124 factories; we conducted a three-year study of the sorting factory with the 14th highest mail volume in the country (approximately six million pieces of mail a day). Our simulation reproduces the automation section of the factory, where automated sorting machines sort most of the mail (over 85% of the total mail volume), and we used that simulation to test the design of new decision aids in the factory (Lerch et al. 1997). For the present research we simplified the original simulation by scaling down the number of sorting machines and by reducing the mail volume accordingly, while keeping intact the structure of the task. Participants in our two laboratory studies were trained in the use of the animation tool with the real task as “cover story.” Subjects were told that their goal was to sort all incoming mail to its destination using the appropriate depth-ofsort for each mail destination, and to meet all dispatch deadlines.

The animation tool was built using SIMAN IV (version 1.2) and CINEMA (version 1.2). The tool automatically recorded all keystrokes. The user interface was built using Microsoft’s Fortran (version 5.0) and Microsoft’s C (version 5.1) programming languages. The programs operated under IBM’s OS/2 (version 1.21). The simulation tool ran on two different monitors: One monitor was dedicated to information presentation; the other was for user interaction. The information monitor had five information screens. Participants could look at the information only one screen at a time, and they could switch among information screens by using hot keys. The user interaction monitor allowed the participants to implement their decisions using a menu-driven interface.

## Nature of the Task

The task selected is similar to operational business problems when measured on the five dimensions: goal clarity, task structure, task complexity, level of uncertainty, and time pressure. This task has well-defined goals and task structure, similar to industrial production and scheduling problems. The task also has moderate level of complexity, with decisions having second- and third-order effects on the system. The level of uncertainty is representative of classical production problems, where current production requirements are known, but future requirements are unknown. Finally, there are moderate to high levels of time pressure. Individuals are required to quickly make decisions; delays in decision making can reduce system performance. This task is similar to production and operations problems in industry and should be a good predictor of performance in similar venues.

The main job of the participants—in both real world and simulation—was to assign mail to sorting machines. Figure 1 shows the sequence of sorting activities for a small set of mail destinations (we will refer to mail destinations as mail types in this paper). For example, to sort all E1 mail on time, mail types C1 and D1 need to be sorted first. More specifically, in order to sort mail destined for a specific mail carrier (E1), it is necessary to sort it first by city (C1) and then by zip code within the city (D1). (There are other mail types that generate Mail Type C1; these are not shown in Figure 1.) To meet dispatch deadlines participants needed to assign mail to a limited number of sorting machines, taking into account the interdependencies of mail flow. The simulation provides an environment in which both exogenous events (for example, mail arrives from other sorting factories), and endogenous events (for instance, assigning mail type C1 to a sorting machine makes this machine unavailable, and generates mail type D1) change the status of the system.

![](/api/attachments/YBKWZRG8/fulltext/images/67cf9f58fa281d764f72ea6c151f0e04846a7d4a021d594c7ab52801062104f6.jpg)

## Monitoring

To make appropriate mail assignment decisions, participants had to monitor mail volumes for different mail types, dispatch deadlines, interdependencies among mail flows, and the availability of sorting machines (our participants were in charge of managing five sorting machines).

The simulation provided five information screens. The main information screen depicted the layout of the five sorting machines. This screen showed the status of each machine, the mail type being sorted in each machine, and the volume of mail being processed by each machine. There were three possible status indicators for each sorting machine: busy, idle, and sweep. The “sweep” status indicated a setup stage; this indicator appeared for ten minutes after a given machine finished sorting a mail type. No mail could be sorted by a machine while it was in sweep. Participants could, however, assign new mail to the machine any time during the sweep stage; the simulation would then automatically start sorting mail after the ten-minute sweep time expired, changing the machine indicator to “busy.” If no mail was assigned during sweeping, the machine indicator would turn to “idle” when the sweep period was over. These indicators were color coded (red for busy, green for idle, and yellow for sweep). The other four information screens provided data about the status of mail volume for groups of mail types (there were 23 mail types in total to be processed in the 5 sorting machines).

The animation tool had three different operating modes: BROWSE, ON, and OFF. In the BROWSE and ON modes, the participants were able to search for data by switching among the five information screens—one at a time—using the information monitor. In the BROWSE mode, the simulated time was frozen while the decision maker searched for information. In the ON mode, the animation tool simulated endogenous events (the machines sorting mail) and exogenous events (mail arriving from other sorting factories) as simulated time progressed. Finally, in the OFF mode, the participants assigned mail to the sorting machines with the user interaction monitor’s menudriven interface. When assigning mail to the machines (OFF mode), the information screens were not available in the information monitor. Therefore, the apparatus forced participants to indicate overtly when they were searching for information, as they had to change the simulation mode to either ON or BROWSE.

The rationale for the three modes is as follows: First, we wanted to be able to compare performance between high and low WM groups in both a BROWSE and no-BROWSE condition. Given the difference in performance when participants were permitted to freeze the world, would performance degrade equally between the high and low WM groups when browsing was not allowed, and when pressure to monitor the system efficiently was therefore increased? Second, we wanted to avoid penalizing participants who were slow in using the menu system for implementing their decisions. By having the OFF mode, which did not permit participants to search for information while they implemented their decisions, we were able to do so. Figure 2 summarizes the functions of the three simulation modes.

## Performance Measure

We adopted only one performance measure—missed trays. Participants were asked to sort 1,008 trays of mail to different mail destinations, each destination with a different dispatch time. Overall performance was measured by the number of trays that were not sorted before the specific deadlines. To verify that the task was feasible, the researchers ran the problem given to the participants and were able to complete it successfully, that is, to sort all trays in time. (Of course, we were aware of the timing and nature of all exogenous events, such as the timing and volume of mail arrivals from other sorting factories).

## Process Variables

We collected three process variables: machine utilization rates, number of full and split assignments, and time spent in browsing mode (the last measure only for participants in the browsing condition of the first study). Machine utilization rates were calculated by dividing the total number of minutes the five machines were either sorting mail (busy status) or being swept (sweep status) by the total number of minutes that machines were available (5 machines - 8 hours - 60 minutes/hour). Utilization rates provide a basic measure of the quality of monitoring—how good the participants were in not letting the machines go idle. Everything else held constant, it is easier to meet dispatch deadlines when utilization rates are high.

Figure 2 Description of the Simulation Modes for Study #1

<table><tr><td>Capability</td><td>ON Mode</td><td>OFF Mode</td><td>BROWS E Mode</td></tr><tr><td>Able to search the information screens</td><td>Yes</td><td>No</td><td>Yes</td></tr><tr><td>Able to implement assignment decisions</td><td>No</td><td>Yes</td><td>No</td></tr><tr><td>Simulated time running (e.g., machines sorting mail)</td><td>Yes</td><td>No</td><td>No</td></tr></table>

Figure 3 Description of the Simulation Modes for Study #2

<table><tr><td>Capability</td><td>ON Mode</td><td>OFF Mode</td><td>FEEDFORWARD Mode</td></tr><tr><td>Able to search the information screens</td><td>Yes</td><td>No</td><td>Yes</td></tr><tr><td>Able to implement assignment decisions</td><td>No</td><td>Yes</td><td>No</td></tr><tr><td>Simulated time running (e.g., machines sorting mail)</td><td>Yes</td><td>No</td><td>Yes (What-if)</td></tr></table>

A second process variable focused on the number of different types of decisions made. Usually participants in our study (and supervisors in the USPS) assigned all the existing mail for a given destination (e.g., mail for E1) to a single machine. We call these decisions full assignments. However, sometimes in order to meet a tight deadline, decision makers needed to split a given mail type onto two or more machines (e.g., to assign E1 to several machines to meet the 8:00 p.m. deadline). We refer to these decisions as split assignments. Splitting mail increases the number of sweeps, or setup times, which reduces the availability of machines for processing other types of mail (e.g., other mail destinations such as E2). It is important to notice that an increased number of splits does not affect utilization rates, since the numerator for calculating utilization rates was calculated adding sorting time to sweeping time. We expected that, everything else held constant, the higher the number of split assignments, the higher would be the number of missed trays.

The third process measure was the time that each participant spent in the browsing mode. Recall that in this mode, the user of the simulation could freeze the simulation time while inspecting the five information screens. This provided more time and data to those participants (in the first study) who were assigned to this condition.

## Default Feedback

None of the participants, except for those assigned to the feedback condition in the second study, received any explicit feedback. Participants got a sense of how well they did while running the simulation by observing missed deadlines, but only if they remembered to do so. This is the same feedback that USPS supervisors received when performing the real-world task. In the second study we manipulated feedback by providing specific feedback about missed deadlines for each mail type as described in §5.

## Feedforward

In the second study, half of the participants were provided with an option to examine the effect of decisions by a feedforward simulation. Participants paused the simulation, then activated a feedforward simulation that allowed for a what-if analysis. In feedforward mode participants could experiment with alternative decisions and examine the effect of those decisions. At any time the participant could stop the feedforward simulation and return to the time at which the normal simulation was paused. Participants in the feedforward condition averaged 66 minutes per experiment, while individuals in the no-feedforward condition averaged 62 minutes.

## 4. First Study: Working Memory

## Experimental Design

This study was a 2 - 2 - 3 factorial with two betweensubjects factors and three repeated trials. The two between-subjects factors were WM group and browsing condition. We selected two groups of participants, one with low dynamic WM span, and the other with high dynamic WM span as classified by Just and Carpenter (1992). There were two browsing conditions. In the first condition participants could run the simulation using only the ON and OFF modes. Therefore, participants could not freeze the simulation and search for information. In the second condition participants had all three modes: ON, OFF and BROWSE. Obviously, participants in the second condition had more time, and looked at more information than those participants in the no-browsing condition. Each participant ran the simulation three times, once on each of three consecutive days.

## Hypotheses

We expected high WM participants to perform better than low WM participants because they had greater storage and processing capabilities. We expected that high WM participants would be able to execute more complex, cognitively taxing decision strategies than low WM participants. We also expected that this storage and processing advantage would be manifested more strongly in the no-browsing condition because the added time pressure would increase the value of having additional cognitive capacity.

Hypothesis 1. We expected an interaction effect between WM group and browsing condition for missed trays.

Hypothesis 1a. Specifically, we expected High WM participants would have fewer missed trays than low WM participants in the no-browsing condition.

We also expected high WM participants to be better at monitoring the system, especially in the nobrowsing condition. A simple measure of monitoring quality in our task was the percentage of utilization of the sorting machines. Decision makers need to be aware when machines will be available, monitor this availability while making decisions, and then switch the simulation to the OFF mode to implement their decisions. Thus,

Hypothesis 2. We expected an interaction effect between WM group and browsing condition for machine utilization rates.

Hypothesis 2a. Specifically, we expected High WM participants would have higher machine utilization rates than low WM participants in the no-browsing condition.

## Participants

Seventy students were recruited from local universities and paid \$10.00 to participate in a separate study investigating the impact of WM capacity on phone-based interaction performance (Huguenard et al. 1997). All participants were administered the reading span test on an individual basis, using the guidelines given in Daneman and Carpenter (1980). The test requires the subject to read aloud a set of unrelated sentences and then recall the final word from each sentence. Subjects begin with five sets of two sentences, followed by five sets of three sentences, and so on until a potential maximum of five sets of six sentences is reached. The largest set size for which the subject successfully recalls all of the final words for at least three out of five sets is defined as the subject’s reading span. If the subject successfully recalls only two of the five sets, then he or she is assigned a reading span halfway between the current set size and the next lower one. Typical reading span scores range from 2.0 to 6.0, with increments of 0.5.

Each span test took approximately ten minutes to complete. Participants were categorized by their dynamic WM capacity into three groups: low-span (26 participants with scores of 2.0 or 2.5), medium-span (26 participants with scores of 3.0 or 3.5), and high-span (18 participants with scores of 4.0, 4.5, 5.0, 5.5, or 6.0). As an extra experimental control, we report error-free performance in the phone-based interaction tasks: 56% for low-span, 63% for medium-span, and 72% for highspan.

We selected 16 participants at random from the lowand high-span groups (8 from the low-span and 8 from the high-span), and asked them to participate in the current study. We refer to the 8 low-span participants as low WM, and to the 8 high-span as high WM. Participants were paid \$30.00.

## Training

All sixteen participants were trained individually in a one-hour session. They were told to assume the role of a supervisor in a sorting factory of the USPS. They were told about the goals of the task and shown how to operate the simulation. The participants ran the simulation for three hours of simulated time and were encouraged to ask questions. Participants in the browsing condition were trained to use the BROWSE mode, while participants in the no-browsing condition were not told about it.

## Procedure

After the training session participants were asked to run the simulation for three consecutive days. Each experimental session took approximately one hour (68 minutes on average in the browsing condition, and 53 minutes on average in the no-browsing condition). On average, the participants made 43.4 assignment decisions (full plus split assignments) in each experimental session.

All three experimental sessions had the same exogenous events—the same mail volume for all mail types, and the same arrival times. During the pilot studies we asked the participants about the similarities and differences of the simulation in each of the three days. Their response was that the three days were similar, but not identical. This is because endogenous events (i.e., mail assignment decisions) change the simulation even when the exogenous events are identical, making it difficult to discern that the situation was the same.

Participants had to sort 1,008 trays of mail in eight simulated hours using five sorting machines. The theoretical sorting capacity of the five machines, without setup times (i.e., sweeps), is 1,200 trays of mail. As a yardstick for performance, we ran the simulation making random assignments, maintaining a perfect machine-utilization rate (that is, never having idle machines). We call this rule the zero intelligence scheduler. The results for 30 replications of random assignments were a mean of 207.5 missed trays with a standard deviation of 22.6.

To collect verbal protocols, we ran two participants in each of the four experimental conditions for a fourth trial (these participants were paid an additional \$10). At the start of this trial, participants were told that verbal protocols would be collected, and were trained in the think-aloud method using two traditional training tasks (Ericsson and Simon 1993). We used these verbal protocols as additional data for interpreting performance.

## Results

Here we divide the presentation of the empirical analysis into performance and process variables.

Performance. Table 1 shows the statistical results for missed trays. The two between-subjects factors (WM group and browsing condition) were significant, as was their interaction (supporting H1). There was no significant effect for trial (i.e., no learning effect), and no significant interaction of trial and the two betweensubject factors. Since there was no trial effect, we averaged missed trays for the four experimental groups across trials. Surprisingly, the significant interaction between WM group and browsing condition was driven by the poor performance of high WM participants in the no-browsing condition. High and low WM participants had a similar number of missed trays in the browsing condition (69.2 versus 69.7), but high WM participants had an extremely poor performance in the no-browsing condition (212.3), while low WM participants had only a slight increase (77.8) in the number of missed trays (contrary to the prediction in H1a). Analysis of the process variables explains this surprising result. To preview high WM participants spent their additional attentional resources searching in the combinatorial decision space of the task, failing to perform the simplest form of system monitoring (not letting the sorting machines go idle).

Process Variables. To see how best to explain the differences in numbers of missed trays among experimental groups, we first ran a regression analysis of missed trays on machine utilization rates, and on type of assignments (full and split). The regression was highly significant (Adjusted $\mathrm { R } ^ { 2 } \ = \ 0 . 9 2 ,$ F (3,44)  176.15, p  .0001). Table 2 shows the estimates for the parameters of this regression. The number of missed trays was estimated to increase by 7.9 for every percentage point of utilization lost and by 2.7 trays for each additional split assignment. Full assignments were not significant.

We then calculated the theoretical number of missed trays generated by a percentage point of lost machine utilization, and for each additional split assignment. Here, we wanted to find the number of trays that could be run using one percent of machine capacity, and the number of trays lost by having an extra sweep. The two theoretical numbers are 12 trays per percentage point of lost utilization rate, and 5 trays for each additional split. The coefficients of the regression represent 65.8% and 54% of the theoretical numbers respectively. These results suggest that differences in the number of missed trays among experimental groups may be explained by inspecting utilization rates and the number of split assignments among the four experimental groups.

We ran a MANOVA analysis for utilization rates. There were significant differences in the utilization rates of the four experimental groups, from a low of 81.5% for high WM participants in the no-browsing condition to 97.2% for low WM participants in the browsing condition. These results among the four groups for machine utilization mirror the performance results (missed trays); high WM participants in the nobrowsing condition had the worst machine-utilization

<table><tr><td>Low WM/Browsing</td><td>Low WM/No Browsing</td></tr><tr><td>High WM/Browsing</td><td>High WM/No Browsing</td></tr></table>

Table 1 MANOVA Results for Study #1

<table><tr><td colspan="4">Missed Trays Between-Subjects</td></tr><tr><td>Source</td><td>D.F.</td><td>F-value</td><td>p-value</td></tr><tr><td>Browsing</td><td>1,12</td><td>9.52</td><td>0.009**</td></tr><tr><td>WM</td><td>1,12</td><td>7.48</td><td>0.018*</td></tr><tr><td>Browsing * WM</td><td>1,12</td><td>7.61</td><td>0.017*</td></tr><tr><td colspan="4">Missed Trays Within-Subjects</td></tr><tr><td>Trial</td><td>2,11</td><td>3.02</td><td>0.090</td></tr><tr><td>Trial * Browsing</td><td>2,11</td><td>2.74</td><td>0.108</td></tr><tr><td>Trial * WM</td><td>2,11</td><td>2.05</td><td>0.175</td></tr><tr><td>Trial * Browsing * WM</td><td>2,11</td><td>2.14</td><td>0.164</td></tr><tr><td colspan="4">Utilization Between-Subjects</td></tr><tr><td>Browsing</td><td>1,12</td><td>15.16</td><td>0.002**</td></tr><tr><td>WM</td><td>1,12</td><td>5.68</td><td>0.035*</td></tr><tr><td>Browsing * WM</td><td>1,12</td><td>4.92</td><td>0.047*</td></tr><tr><td colspan="4">Utilization Within-Subjects</td></tr><tr><td>Trial</td><td> $T_0^2$ </td><td>1.039</td><td>0.020*</td></tr><tr><td>Trial * Browsing</td><td> $T_0^2$ </td><td>0.859</td><td>0.033*</td></tr><tr><td>Trial * WM</td><td> $T_0^2$ </td><td>0.946</td><td>0.026*</td></tr><tr><td>Trial * Browsing * WM</td><td> $T_0^2$ </td><td>0.696</td><td>0.055</td></tr><tr><td colspan="4">Split Assignments Between-Subjects</td></tr><tr><td>Browsing</td><td>1,12</td><td>0.03</td><td>0.859</td></tr><tr><td>WM</td><td>1,12</td><td>1.61</td><td>0.229</td></tr><tr><td>Browsing * WM</td><td>1,12</td><td>2.32</td><td>0.153</td></tr><tr><td colspan="4">Split Assignments Within-Subjects</td></tr><tr><td>Trial</td><td> $T_0^2$ </td><td>1.184</td><td>0.014*</td></tr><tr><td>Trial * Browsing</td><td> $T_0^2$ </td><td>0.492</td><td>0.107</td></tr><tr><td>Trial * WM</td><td> $T_0^2$ </td><td>0.094</td><td>0.610</td></tr><tr><td>Trial * Browsing * WM</td><td> $T_0^2$ </td><td>0.062</td><td>0.719</td></tr></table>

\*p  0.05 \*\*p  0.01 \*\*\*p  0.001

rate (contrary to the prediction of H2a). Consequently, performance results in missed trays are partially explained by the machine-utilization results. Statistically, the two between-subjects factors and their interaction were significant as shown in Table 1. There was also a significant trial effect. In addition, there were significant interaction effects between trial and the two between-subjects, but there was no significant triple interaction at the nominal value of alpha  0.05. The trial effect and the two interactions can be explained by inspecting Figure 4. In both conditions (browsing and no-browsing) low WM participants increased their utilization rates across trials. On the other hand, the utilization of high WM participants in the browsing condition remained flat, while utilization rates had an up-and-down pattern for high WM participants in the no-browsing condition. Machine-utilization rates for high WM participants in the no-browsing condition are significantly lower than the utilization rates in the other three conditions.

Table 2 Regression of Missed Trays on Utilization and Splits in Study #1

<table><tr><td>Variable</td><td>D.F.</td><td>Estimate</td><td>t-value</td><td>p-value</td></tr><tr><td>Utilization</td><td>1</td><td>-7.91</td><td>-16.54</td><td>0.0001***</td></tr><tr><td>Splits</td><td>1</td><td>2.73</td><td>6.35</td><td>0.0001***</td></tr><tr><td>Full</td><td>1</td><td>0.016</td><td>0.023</td><td>0.9817</td></tr></table>

\*p  0.05 \*\*p  0.01 \*\*\*p  0.001

![](/api/attachments/YBKWZRG8/fulltext/images/bc5f432307c2232aca86bc4b0d2ccc40eae449e81babb16f58edc16f542c30e6.jpg)

Examining the number of split assignments also helps explain the unexpected performance results. High WM participants had few split assignments in the browsing condition (7.8), but the number of splits increased in the no-browsing condition (18.8). Low WM participants showed little variation between browsing (13.0) and no-browsing (12.0). Statistically, there were no main effects for the WM group and browsing condition. Although there seems to be an interaction effect between WM group and browsing condition, it is not significant because of a high variance within high WM participants in the no-browsing condition. There was a significant trial effect. Participants increased their number of splits across trials—1st trial: 11.37; 2nd trial: 11.31; 3rd trial: 16.13. There were no significant interaction effects for Trial with the other factors and no significant triple interaction.

The third process variable, browsing time, also sheds light on the difference in performance between high and low WM participants. We compared the time spent browsing by low and high WM participants in the browsing condition. Low WM participants spent 9.2 minutes in the BROWSE mode, while high WM participants spent 18.2 minutes. This difference was highly significant (p  .001). These results support our explanation that high WM participants are more inclined to search extensively in the decision space.

To confirm that we were interpreting the differences in machine-utilization rates, number of split assignments, and browsing time correctly, we examined the verbal protocols. We transcribed the eight verbal protocols recorded from two participants in each experimental condition. We did not need a rigorous analysis because a cursory inspection of the protocols supported our interpretation of the numerical results. High WM participants explored more of the decision space by considering many more alternatives than low WM participants, both in the browsing and the nobrowsing conditions. In the browsing condition, high WM participants had the time to evaluate many more alternatives because they could freeze the simulation and search for information (consequently, they spent more time browsing). In the no-browsing condition, high WM participants also evaluated many more alternatives than low WM participants, but time pressures in this task environment were greater. Consequently, high WM participants often simply failed to monitor the sorting machines, letting them go idle (this showed in their lower machine-utilization rates). High WM participants also considered implementing more split assignments throughout the simulated time in both conditions. In the browsing condition they actually implemented very few of these decisions after carefully evaluating the implications of doing so. However, in the no-browsing condition they did not have the time for further evaluation, and therefore, they actually implemented more split assignments.

## Discussion

The results of the first study are rather surprising. The high WM participants in the no-browsing condition exhibited performance only equivalent to our zero intelligence scheduler. This scheduler makes random assignments while monitoring the sorting machines perfectly (never letting them go idle). In many prior studies dynamic WM capacity has been shown to be highly correlated with superior performance in a variety of tasks and is believed to be an important source for explaining intelligence scores (Kyllonen and Christal 1990). In this case, however, it appears that while having higher WM capacity does lead to exploring the decision space more carefully, it also leads to forgetting to monitor the environment effectively.

All the process data (i.e., utilization rates, type of assignments, and browsing time) suggest that high WM participants spent their superior storage and processing capacity searching the decision space. However, the size of the decision space in our task gets very large after a few moves. High WM participants in the no-browsing condition seemed to get lost searching for better assignment decisions, neglecting the simple monitoring of the sorting machines. There are many anecdotes of decision makers in real-time dynamic environments having similar experiences. In the human factors literature, these anecdotes are usually referred to as losing situational awareness (Endsley 1995).

Furthermore, many real-time decision makers in real-world tasks believe that what is important in these environments is a capacity to “keep it simple” and “just do it” (e.g., a Nike decision strategy). For example, in a recent newspaper article, a reporter interviewed air-traffic controllers in the Newark airport (considered the most difficult and stressful air-traffic space in the country). A veteran air-traffic controller made the following observations about a specific decision being discussed: “Now that’s crisp vectoring! Make a plan, make it work, but don’t think about the plan. Real educated people, somebody with real smarts, can’t do this because they’re always pondering. I don’t have time for that.” (Frey 1996, p. 47). It seems our high WM participants in the no-browsing condition spent a great deal of time pondering complex decision alternatives (e.g., split assignments), and forgot to keep it simple (e.g., monitor the sorting machines).

Because having more raw capacity for monitoring the system (the first level of situational awareness) did not improve performance, the second experiment manipulated feedback and feedforward support in an attempt to improve the second and third level of situational awareness. Our rationale was that in relatively complex systems, decision makers need more than just effective system monitoring; they need to learn how to control the system through feedback and feedforward support.

## 5. Second Study: Feedback and Feedforward

## Experimental Design

The second study was a 2 - 2 - 3 factorial with two between-subjects factors and three repeated measures. The two between-subjects factors were feedback and feedforward. Feedback participants received explicit and immediate detailed outcome feedback on the number of missed trays by mail type, while nofeedback participants did not receive any explicit feedback (as in the first study). Feedforward participants were given a what-if tool to look into the future, make decisions (if desired), and test different decision strategies. The no-feedforward participants had no what-if capability. To partially control for the effect of working memory, participants had either low or medium WM capacity. No participants were selected who had high WM span.

Each participant ran the simulation on four consecutive days. During Day 4 all participants used the no feedback/no feedforward condition. For Days 2–4 (three experimental trials), participants were assigned to one of the four (2 - 2) experimental conditions. All participants used the simulation without the BROWSE mode (e.g., as in a real-time task).

For this study we asked the participants to monitor the sorting machines very carefully. We wanted to isolate the effects of feedback and feedforward without confounding them with monitoring. We expected that all participants would have very high machine utilization rates. Consequently, we expected performance differences to be explained solely by differences in the decisions made by the four experimental groups.

## Hypotheses

We expected an interaction effect between feedback and feedforward groups. We expected that participants with only feedforward would get lost in the decision space, as did the high WM participants in the no-browsing condition in the first study, but we expected participants with both feedback and feedforward support to have the best performance through time. Thus,

Hypothesis 3. We expected an interaction effect between feedback and feedforward groups for missed trays.

Hypothesis 3a. Specifically, we expected feedforward participants with no explicit feedback to have the highest number of missed trays (worst performance).

Hypothesis 3b. Specifically, we expected that the feedback and feedforward group would have lower numbers of missed trays than feedforward participants who received no explicit feedback.

## Participants

Twenty-four participants were recruited from local universities and paid \$50 to participate in the four-day study. All participants were administered the reading span test (Daneman and Carpenter 1980). Reading span scores ranged from 2.0 to 3.5. As mentioned above, to partially control for WM, no high WM participants were included in the second study.

## Training

All twenty-four participants were trained individually in a one-hour session similar to the first study. They were told to assume the role of a supervisor in a sorting factory in the USPS, told about the goals of the task, and shown how to operate the simulation. The participants ran the simulation for three hours of simulated time and were encouraged to ask questions. Training for all participants was conducted using the simulation in the no feedback/no feedforward condition.

The only difference in participant training between the first and second study was that in the second study, we instructed the participants to avoid letting the machines go idle. We showed them how to monitor the status of the machines and assign mail while the machines were in sweep status. We encouraged them to monitor the machines carefully.

## Procedure

After the training session, all participants were asked to run the baseline simulation with the no-feedback and no-feedforward version. Before running the baseline simulation, participants were reminded to monitor the sorting machines, and to avoid having the machines go idle. Based on their scores from this baseline trial and the WM scores, participants were assigned to one of the four experimental conditions for Days 2–4 (Trials 1–3). The assignment of participants ensured that the average of WM scores and the average performance in the baseline trial were equivalent for the four experimental groups. Each experimental session took approximately one hour (66 minutes on average in the feedforward condition, and 62 minutes on average in the no-feedforward condition). On average, the participants made 45.6 assignment decisions (full plus split assignments) in each experimental session.

Feedback participants used a simulation that provided very specific feedback per mail type. After each dispatch deadline passed, the simulation would show the number of missed trays for the corresponding mail type, and a running total of all missed trays up to that time. At the beginning of the second day (Trial 1), participants assigned to the feedback condition were trained on how to monitor the explicit feedback made available by the simulation.

The no-feedback participants were given no feedback (as in the first study). They could observe, while running the simulation, the number of trays they missed for each mail type, but this was difficult. If they wanted to do this, they had to monitor when the dispatch time for each mail type was the same as the simulated time, then find the number of trays for that mail type not sorted in time in the appropriate information screen, check whether that mail type was being sorted in the sorting machine information screen, find the number of trays of that mail in the sorting machines (if any), and finally, add the two numbers.

Feedforward participants were able to save the system status at any given time, look into the future, and return to the saved state when desired. When looking into the future, the decision maker was able to continue making decisions (i.e., assigning mail to machines) if desired. Therefore, the decision maker using this feedforward capability could predict the impact of alternative decisions, and/or predict future events with perfect accuracy. Participants assigned to the feedforward condition were trained on how to use this whatif capability. Participants assigned to the feedback and feedforward condition were trained both on how to monitor the feedback, and how to use the feedforward capability in the simulation. Participants then ran their assigned experimental condition for three consecutive days.

All experimental groups encountered the same set of exogenous events: same mail volumes, mail arrivals, and dispatch deadlines. As in the first study, participants had to sort 1,008 trays of mail in 8 simulated hours, using five sorting machines.

## Results

We first present the results of utilization rates as an experimental control. Recall that we expected no significant differences in utilization rates among groups if all participants were able to follow the instructions given to them during training.

Experimental Control: Machine Utilization Rates. The average utilization was 99% across experimental groups and trials. There were neither significant main effects nor interactions among the three factors. Therefore, performance differences among the four experimental groups cannot be explained by the quality of monitoring. They can only be explained by the nature of the decisions made (that is, by the quality of system control).

Performance. Table 3 shows the MANOVA analysis for missed trays for all four trials: the baseline trial and the three experimental trials. There was a strong trial effect. Table 4 shows the analysis of betweensubjects factors for each trial. The table shows that there was an interaction effect between feedback and feedforward in the last trial. It also shows that this effect was nonexistent in the baseline and first experimental trials, significant at the nominal value of alpha  0.08 in the second experimental trial, and finally, significant at the nominal value of alpha  0.01 in the third experimental trial (partially supporting H3).

Table 3 MANOVA Results for Study #2

<table><tr><td colspan="4">Missed Trays Between-Subjects</td></tr><tr><td>Source</td><td>D.F.</td><td>F-value</td><td>p-value</td></tr><tr><td>Feedback (FB)</td><td>1,20</td><td>1.44</td><td>0.244</td></tr><tr><td>Feedforward (FF)</td><td>1,20</td><td>1.56</td><td>0.226</td></tr><tr><td>FB * FF</td><td>1,20</td><td>3.03</td><td>0.097</td></tr><tr><td colspan="4">Missed Trays Within-Subjects</td></tr><tr><td>Trial</td><td>3,18</td><td>9.49</td><td>0.0006***</td></tr><tr><td>Trial * FB</td><td>3,18</td><td>0.47</td><td>0.708</td></tr><tr><td>Trial * FF</td><td>3,18</td><td>3.22</td><td>0.048*</td></tr><tr><td>Trial * FB * FF</td><td>3,18</td><td>1.26</td><td>0.319</td></tr><tr><td colspan="4">Chain-3 Missed Trays Between-Subjects</td></tr><tr><td>Feedback (FB)</td><td>1,20</td><td>1.03</td><td>0.321</td></tr><tr><td>Feedforward (FF)</td><td>1,20</td><td>0.04</td><td>0.849</td></tr><tr><td>FB * FF</td><td>1,20</td><td>6.43</td><td>0.019*</td></tr><tr><td colspan="4">Chain-3 Missed Trays Within-Subjects</td></tr><tr><td>Trial</td><td>2,19</td><td>7.27</td><td>0.0045**</td></tr><tr><td>Trial * FB</td><td>2,19</td><td>3.82</td><td>0.040*</td></tr><tr><td>Trial * FF</td><td>2,19</td><td>4.94</td><td>0.018*</td></tr><tr><td>Trial * FB * FF</td><td>2,19</td><td>0.99</td><td>0.386</td></tr></table>

\*p  0.05 \*\*p  0.01 \*\*\*p  0.001

Table 4 Between-Subjects Factors Across Trials in Study #2

<table><tr><td>Trial</td><td>Source</td><td>D.F.</td><td>F-value</td><td>p-value</td></tr><tr><td rowspan="3">Baseline</td><td>Feedback (FB)</td><td>1,20</td><td>0.00</td><td>0.971</td></tr><tr><td>Feedforward (FF)</td><td>1,20</td><td>0.16</td><td>0.695</td></tr><tr><td>FB * FF</td><td>1,20</td><td>0.00</td><td>0.949</td></tr><tr><td rowspan="3">1st trial</td><td>Feedback (FB)</td><td>1,20</td><td>1.12</td><td>0.302</td></tr><tr><td>Feedforward (FF)</td><td>1,20</td><td>2.90</td><td>0.104</td></tr><tr><td>FB * FF</td><td>1,20</td><td>1.59</td><td>0.222</td></tr><tr><td rowspan="3">2nd trial</td><td>Feedback (FB)</td><td>1,20</td><td>2.26</td><td>0.148</td></tr><tr><td>Feedforward (FF)</td><td>1,20</td><td>0.05</td><td>0.831</td></tr><tr><td>FB * FF</td><td>1,20</td><td>3.56</td><td>0.074</td></tr><tr><td rowspan="3">3rd trial</td><td>Feedback (FB)</td><td>1,20</td><td>1.51</td><td>0.233</td></tr><tr><td>Feedforward (FF)</td><td>1,20</td><td>2.14</td><td>0.159</td></tr><tr><td>FB * FF</td><td>1,20</td><td>8.23</td><td>0.009**</td></tr></table>

\*p  0.05 \*\*p  0.01 \*\*\*p  0.001  
Information Systems Research Vol. 12, No. 1, March 2001

The best way to understand this interaction is to graph the number of missed trays for the two feedforward groups. Figure 5 shows both groups had a performance of around 90 trays missed on the baseline day. On the second day (1st trial), the group with feedforward but no feedback did considerably worse (around 135 missed trays) than during the baseline day. In contrast, the group with feedforward and feedback had a slight improvement. On the last two days, the participants with feedback and feedforward improved their performance substantially. On the other hand, the group with feedforward but without feedback was only able to get back to the performance achieved on the baseline day (these results support H3a and H3b). These results clearly show that having only feedforward support degraded performance and inhibited learning (at least in early trials). Having both feedback and feedforward support however, improved learning.

Figure 5 shows the performance of all four groups in the four trials (baseline trial and three experimental trials). Performance was similar for groups with or without feedback. The performance of participants without feedback was similar to the performance of low WM participants in the no-browsing condition in the first study for the first three trials (baseline trial and first two experimental trials). However, there seems to be an improvement in the last trial (participants in the first study only ran three trials, while participants in the second study ran four trials). Recall that there was no learning effect in the first study. It seems that one more trial was necessary for learning to occur for participants with neither feedback nor feedforward support.

Figure 5 Means of Missed Trays for All Groups in Study #2 Missed Trays in Study #2  
![](/api/attachments/YBKWZRG8/fulltext/images/2b8cfddd404ea038fa5130c1775bb78bf93c1adfacc4090a421628b68353b912.jpg)

Figure 6 shows the standard deviations of performance. As seen before, performance improves through the fourth trial. However, the variability of performance also decreased from earlier trials to the final trial. The statistically significant result in Trial 4 is partially due to improved performance and partially due to reduced variability between subjects. Although this reduction in variation is interesting from a perspective of consistency between subjects, it does not alter the interpretation of the learning effect in Trial 4.

The best performance was achieved by two groups. Surprisingly, these are the participants with no feedback and no feedforward (50.8 missed trays, standard deviation 16.5), and those with both feedback and feedforward (52.8 missed trays, standard deviation 10.9); this explains the interaction effect between feedback and feedforward in the last trial. In this trial, having feedback and feedforward did not make a difference when compared to the no-feedback and nofeedforward condition, while having either feedback only or feedforward only degraded performance.

Figure 6 Standard Deviations of Missed Trays for All Groups in Study #2 Standard Deviations in Study #2  
![](/api/attachments/YBKWZRG8/fulltext/images/cb44a70ced5ab77a0326d998815ddc1fbc7f7e5ff050bc37ef70dfd7ca2999c8.jpg)

There are two caveats to this interpretation. First, participants with feedback and feedforward seemed to improve faster (in the second experimental trial) than participants with no feedback and no feedforward (Figure 5). Second, the feedback and feedforward participants had to learn how to use the feedback and feedforward support in the first experimental trial, while participants with no feedback and no feedforward had to learn nothing in this trial. It is possible that the improvements for the feedback and feedforward group could have been even faster had they been trained how to use feedback and feedforward in the baseline trial.

Number of Split Assignments. The question now is how to explain performance differences, and in particular, how to explain the interaction effect between feedback and feedforward where the groups with either no support (no feedback and no feedforward) or all support (feedback and feedforward) had the best performance in the last trial. We analyzed the number of split assignments among the four groups. There were no significant factors. Therefore, we decided to perform further analysis. We examined performance results (missed trays) by mail type to explain performance differences among experimental groups.

Performance: Causal Chains. Although, the data indicate that learning occurs under certain experimental conditions, data do not explain why that learning occurs or which task factors affect learning. By exploring one possible explanation of complexity, i.e., causal chains, it is possible to further explain this pattern of learning.

Causal chains are defined as the number of interdependent decisions required to accomplish a goal. In the USPS sorting factory the goal is to sort as much mail as possible before the dispatch deadline. Figure 1 shows the steps required to sort a mail type to its final destination. The sorting steps C1–D1–E1 are the events required to sort the first set of mail to its destination. Because three decisions are required in sequence, we say that the length of its causal chain is three. Similarly, the sequence C3–D3 has a causal chain of length two, and C5 has a causal chain of length one. By looking at performance differences for missed trays with different lengths of causal chains, we hoped to gain insights into performance differences among the experimental groups.

We classified the missed trays for all participants into missed trays for mail type Chain-1, Chain-2, and Chain-3. We hypothesized that feedback and feedforward might have a differential impact on mail types with different chain sequence. More specifically, feedforward combined with feedback may be especially effective for reducing the number of missed trays for mail types with long sorting sequences because having feedback and feedforward allows the decision maker to look into the future and assess the impact of alternative decisions. We present the results for Chain-1 and Chain-2 combined (Chains 1–2) because participants missed few trays for these two mail types; then we present the results for Chain-3 mail types.

Only the feedforward main effect was significant for Chains-1–2. Participants with no feedforward had 12.3 missed trays, while participants with feedforward performed worse by having 22.5 missed trays. Feedforward does not seem to help in making decisions with a short-term horizon; in fact, it degraded performance for this type of decision. No other significant effects were found.

The largest difference in learning rates was evident in the chains of length three (Chain-3). Although all subjects in the baseline case missed an average of 60 trays categorized as Chain-3 mail type, the introduction of feedforward had a dramatic effect on the performance of feedforward participants. The number of missed trays of Chain-3 mail type dropped across trials for the feedback and feedforward group (Figure 7). In contrast, the missed trays increased significantly in Trial 1 for the feedforward and no-feedback group. The feedforward and no-feedback group returned to 60 missed trays after the final trial, while the feedback and feedforward group continued to reduce missed trays to approximately half of the baseline performance. Table 3 shows the MANOVA results for Chain-3 missed trays. There was a significant interaction between feedback and feedforward $\mathrm { ( p ~  ~ { ~ = ~ } ~ } . 0 1 9 )$ . The interactions of trial and feedback $~ ( \mathrm { p } ~ = ~ . 0 4 0 )$ and trial and feedforward $( \mathsf { p } \ = \ . 0 1 8 )$ were also significant. Learning, measured by the trial effect, was very significant $( \mathrm { p } = . 0 0 4 5 )$ . The overriding conclusion is that chains of length three involve significant associated learning and explain the difference in learning rates among the experimental groups.

![](/api/attachments/YBKWZRG8/fulltext/images/7647476f73060ceeed0a1ad6b861966ce99dd5df5253eef5eb539144a8c1d8b3.jpg)

## Discussion

We predicted earlier (H3) that we expected an interaction effect between feedback and feedforward. This interaction effect was manifested as follows. In the absence of feedforward, the addition of feedback had no effect on performance. However, when a feedforward tool was made available to the participants those without feedback performed substantially worse than their baseline performance, but those with feedback accelerated their learning. It appears that participants who were given both the feedforward tool as well as feedback were able to look into the future and assess alternative strategies. Those with feedforward but no feedback were able to look into the future, but without feedback they were not able to assess the effectiveness of alternative strategies. This was especially true for decisions of mail type Chain-3. One possible explanation for this phenomenon is that the lack of feedback not only prevents comparison of alternative strategies, but also leads to confusion, inhibiting learning in more complex aspects of the task (Chain-3 mail types).

We examined this issue of learning complex aspects of the task by comparing learning rates for mail types with different levels of complexity (Chain-1 having the lowest level of complexity, Chain-3 having the highest). Although all subjects had similar learning on tasks with causal chains of length one or two, those participants with both feedforward and feedback showed dramatic learning on the Chain-3 tasks. In contrast, the performance for participants with feedforward but no feedback showed significant degradation on Chain-3 tasks. It appears that feedforward provides a valuable tool to evaluate complex task features when used in conjunction with feedback. In the absence of feedback, feedforward simply becomes an ineffective tool of exploration having a negative effect on simple tasks (Chain-1 and Chain-2), and resulting in no learning for complex tasks (Chain-3).

## 6. General Discussion

The results of the two studies indicate that providing cognitive support for real-time dynamic decision making is very difficult. Three radical experimental manipulations failed to improve performance or to speed up learning. In the first study, individuals with high storage and cognitive processing capacity failed to perform better than individuals with lower capacity, and were unable to improve their performance. In the second study, providing either feedback or feedforward support was ineffective. Detailed performance feedback did not improve learning. Worse, a decision aid that supported feedforward control actually degraded performance and inhibited learning. Finally, individuals who received both feedback and feedforward had, at best, slightly faster learning rates than individuals with no explicit performance feedback and no feedforward computer support. All these results were surprising.

Why is it so difficult to support real-time dynamic decision making? We identify at least three reasons. First, the problem space of dynamic decision tasks is usually very large due to the interdependency of decisions. Even when individual decisions have only few options, the decision space grows exponentially because of this interdependency. For example, air-traffic controllers have few options for changing the route of an individual plane, but each routing change affects other routing changes. Second, real-time tasks by definition exert time pressure on the decision maker. Therefore, it is difficult to process all the available information. Decision makers need to filter information and pay attention to only a few important cues in the environment. Third, online human storage and processing capacity is very small. WM is a hard constraint in human information-processing capacity, and WM is faulty when overloaded; it loses information easily, and fails to perform cognitive operations correctly. For all these reasons it is difficult to design effective computer support because decision aids need to provide more benefits than the cost incurred in processing the additional information generated by the decision aid.

The results of the first study are still puzzling: Why didn’t high WM individuals simply reduce the allocation of cognitive resources dedicated to exploring the problem space? Isn’t it always better to have more cognitive resources? Perhaps not. Many tasks in the real world are designed for individuals with average WM capacity (average WM capacity is represented by low and medium WM span in the dynamic WM test used in our studies). For example, we are taught addition and subtraction in school with external aids and methods, such as paper and pencil and carrying the digits, which make good use of our attentional resources: They do not overload our WM, and they help us pace ourselves through the task. Such external aids and methods were developed through trial and error over long periods of time. Many new tasks embedded in information technology have not evolved adequately to fit well with human attentional capabilities. Consequently, many computer-based tasks overload people, or fail to pace them adequately. Having more WM capacity can only help if it is used to filter and process information effectively, and to explore the decision space efficiently. This can only be done if the decision maker can acquire and execute decision strategies that exploit the nature of the task.

Another unexpected finding was that performance feedback did not speed up learning. This is surprising because a myriad of studies have shown that detailed and timely feedback is a major factor in improving decision making (Balzer et al., 1992). One explanation for this failure is that in dynamic environments the existence of interdependent decisions increases the difficulty of assigning credit to particular decisions, even with very specific feedback. In our task, participants made around 45 decisions per session. Knowing which set of decisions made a difference from session to session is difficult; therefore, performance feedback should not be expected to be of immediate help in RTDDM. Besides their credit assignment problem, decision makers in real-time environments spend time processing the feedback, which in turn lowers the share of attentional resources for processing other task information. In summary, although we do expect performance feedback to be a major factor influencing learning in RTDDM, we need a better understanding of how feedback attributes (specificity, timing, etc.) help or hinder the acquisition and execution of decision strategies.

It is clear from the second study that feedforward support too can be harmful in RTDDM tasks. In our study participants with feedforward could freeze the world, project the status of the system into the future with perfect accuracy, and use this information to make decisions in the present. The results clearly indicate that this support, by itself, degraded performance. Our explanation for this result is similar to the explanation of why high WM individuals performed poorly in the first study: Participants allocated too many of their scare attentional resources to exploring the combinatorial decision space, got lost in the decision space, and therefore made worse decisions than those participants without the feedforward facility. On the other hand, slightly faster learning was observed when feedforward was provided in conjunction with detailed feedback. In conclusion, the design of feedforward support requires a good understanding of its benefits and costs because it affects decision strategies. Even in ideal conditions such as those in the second study (where participants could freeze the world and look into the future), feedforward can overload decision makers and prevent them from adopting adequate decision strategies.

## Acknowledgments

The research was supported by grants from the Air Force Office of Scientific Research (F49620-97-1-0368) and the United States Postal Service (104230-91-H-3819). The authors would like to acknowledge the comments from the associate editor and three anonymous reviewers. They would also like to thank Steven Vargo for writing the simulation for the experimental apparatus.

## References

Baddeley, A. D. 1992. Working memory: The interface between memory and cognition. J. of Cogn. Neuroscience 4 (3) 281–288.

——, G. J. Hitch. 1974. Working memory. G. H. Bower ed. The Psychology of Learning and Motivation. 8. Academic Press, New York.

Balzer, W. K., L. M. Sulsky, L. B. Hammer, K. E. Sumner. 1992. Task information, cognitive information, or functional validity information: Which components of cognitive feedback affect performance? Organ. Behavior and Human Decision Proc. 53 35–54.

Brehmer, B. 1990. Strategies in real-time, dynamic decision making. R. M. Hogarth, ed. Insights in Decision Making. University of Chicago Press, Chicago, IL, 262–279.

——. 1992. Dynamic decision making: Human control of complex systems. Acta Psychologica 81 211–241.

—, R. Allard. 1991. Real-time dynamic decision making: The effects of task complexity and feedback delays. J. Rasmussen, B. Brehmer, J. Leplat, eds. Distributed Decision Making: Cognitive Models for Cooperative Work. Wiley, Chichester, U.K.

Broadbent, D. E. 1958. Perception and Communication. Pergamon Press, London, U.K.

Daneman, M., P. A. Carpenter. 1980. Individual differences in working memory and reading. J. Verbal Learn. and Verbal Behavior 19 450–466.

Davis, F. D., J. E. Kottemann. 1995. Determinants of decision rule use in a production planning task. Organ. Behavior and Human Decision Proc. 63 145–157.

Diehl, E., J. D. Sterman. 1995. Effects of feedback complexity on dynamic decision making. Organ. Behavior and Human Decision Proc. 62 (2) 198–215.

Edwards, W. 1962. Dynamic decision theory and probabilistic information processing. Human Factors 4 59–73.

Endsley, M. R. 1987. SAGAT: A methodology for the measurement of situation awareness (NOR DOC 87–83). Northrop Corp. Hawthorne, CA.

——. 1995. Toward a theory of situation awareness in dynamic systems. Human Factors 37 (1) 32–64.

Ericsson, K. A., H. A. Simon. 1993. Protocol Analysis (Revised Edition). MIT Press, Cambridge, MA.

Frey, D. 1996. Something’s got to give. New York Times Sunday Magazine (March 24) 43–55.

Gibson, F. P., M. Fichman, D. C. Plaut. 1997. Learning in dynamic decision tasks: Computational model and empirical evidence. Organ. Behavior and Human Decision Proc. 71(1) 1–35.

Hogarth, R. M. 1986. Generalization in decision research: The role of

formal models. IEEE Trans. on Systems, Man, and Cybernetics 16 439–449.

—, R. M. McKenzie, B. J. Gibbs, M. A. Marquis. 1991. Learning from feedback: Exactingness and incentives. J. of Experiment. Psych. Learning, Memory, and Cognition 17(4) 734–752.

Huguenard, B. R., F. J. Lerch, B. W. Junker, R. J. Patz, R. E. Kass. 1997. Working memory failure in phone-based interaction. ACM Trans. on Comput. Human Interaction. 4 67–102.

Just, M. A., P. A. Carpenter. 1985. Cognitive coordinate systems: Accounts of mental rotation and individual differences in spatial ability. Psych. Rev. 92 (2) 137–171.

—, ——. 1992. A capacity theory of comprehension: Individual differences in working memory. Psych. Rev. 99(1) 122–149.

Kerstholt, J. H. 1995. Decision making in a dynamic situation: The effect of false alarms and time pressure. J. of Behavioral Decision Making. 8 181–200.

Kyllonen, P. C., R. E. Christal. 1990. Reasoning ability is (little more than) working-memory capacity?! Intelligence 14 389–433.

Lerch, F. J., D. J. Ballou, D. E. Harter. 1997. Using simulation-based experiments for software requirements engineering. Ann. Software Engr. 9 1–22.

Miller, G. A. 1956. The magical number seven plus or minus two:

Some limits on our capacity for processing information. Psych. Rev. 63 81–97.

Newell, A., H. A. Simon. 1972. Human Problem Solving. Prentice-Hall Englewood Cliffs, NJ.

Payne, J. W., J. R. Bettman, E. J. Johnson. 1993. The Adaptive Decision Maker. Cambridge Univ. Press, New York.

Peterson, L. R., M. J. Peterson. 1959. Short-term retention of individ ual verbal items. J. of Experiment. Psych. 58 193–198.

Press, M. 1986. Situation awareness: Let’s get serious about the cluebird. Unpublished Manuscript.

Sterman, D. 1989a. Misperceptions of feedback in dynamic decision making. Organ. Behavior and Human Decision Proc. 43 301–335.

——. 1989b. Modeling managerial behavior: Misperceptions of feedback in a dynamic decision making experiment. Management Sci. 35 321–339.

Todd, P., I. Benbasat. 1994. The influence of decision aids on choice strategies: An experimental analysis of the role of cognitive effort. Organ. Behavior and Human Decision Proc. 60 36–74.

Tversky, A. 1972. Elimination by aspects: A theory of choice. Psych. Rev. 79 281–299.

Waugh, N. C., D. A. Norman. 1965. Primary memory. Psych. Rev. 72 89–104.

Izak Benbasat, Senior Editor. This paper was received on August 25, 1997, and has been with the authors 18 months for 2 revisions.
