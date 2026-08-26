---
otero_id: 8298
otero_key: "GQHDJAP4"
title: "How Is Your User Feeling? Inferring Emotion Through Human-Computer Interaction Devices1"
authors: "Martin Hibbeln; Jeffrey L. Jenkins; Christoph Schneider; Joseph S. Valacich; Markus Weinmann"
year: "2017"
journal: "MIS Quarterly"
doi: "10.25300/misq/2017/41.1.01"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# HOW IS YOUR USER FEELING? INFERRING EMOTION THROUGH HUMAN–COMPUTER INTERACTION DEVICES<sup>1</sup>

Martin Hibbeln Mercator School of Management, University of Duisburg-Essen, Lotharstrasse 65, 47057 Duisburg, GERMANY {martin.hibbeln@uni-due.de}

Jeffrey L. Jenkins Information Systems Department, Brigham Young University, 790 TNRB, Provo, UT 84602 U.S.A. {jjenkins@byu.edu}

Christoph Schneider Department of Information Systems, City University of Hong Kong, Tat Chee Avenue, Kowloon, HONG KONG {christoph.schneider@cityu.edu.hk}

Joseph S. Valacich Management Information Systems, University of Arizona, McClelland Hall Room 430CC, Tucson, AZ 85721 U.S.A. {valacich@arizona.edu}

Markus Weinmann

Information Systems Department, University of Liechtenstein, Fürst-Franz-Josef-Strasse, 9490 Vaduz, LIECHTENSTEIN {markus.weimann@uni.li}

Emotion can influence important user behaviors, including purchasing decisions, technology use, and customer loyalty. The ability to easily assess users’ emotion during live system use therefore has practical significance for the design and improvement of information systems. In this paper, we discuss using human–computer interaction input devices to infer emotion. Specifically, we utilize attentional control theory to explain how movement captured via a computer mouse (i.e., mouse cursor movements) can be a real-time indicator of negative emotion. We report three studies. In Study 1, an experiment with 65 participants from Amazon’s Mechanical Turk, we randomly manipulated negative emotion and then monitored participants’ mouse cursor movements as they completed a number-ordering task. We found that negative emotion increases the distance and reduces the speed of mouse cursor movements during the task. In Study 2, an experiment with 126 participants from a U.S. university, we randomly manipulated negative emotion and then monitored participants’ mouse cursor movements while they interacted with a mock e-commerce site. We found that mouse cursor distance and speed can be used to infer the presence of negative emotion with an overall accuracy rate of 81.7 percent. In Study 3, an observational study with 80 participants from universities in Germany and Hong Kong, we monitored mouse cursor movements while participants interacted with an online product configurator. Participants reported their level of emotion after each step in the configuration process. We found that mouse cursor distance and speed can be used to infer the level of negative emotion with an out-

Hibbeln et al./Inferring Emotion Through Human–Computer Interaction Devices

of-sample R<sup>2</sup> of 0.17. The results enable researchers to assess negative emotional reactions during live system use, examine emotional reactions with more temporal precision, conduct multimethod emotion research, and create more unobtrusive affective and adaptive systems.

Keywords: Negative emotion, attentional control theory (ACT), mouse cursor distance, mouse cursor speed, mouse tracking, human–computer interaction

## Introduction

System design can influence users’ emotions and thereby impact important user behavior. For example, human– computer interaction (HCI) research has found that a system’s aesthetic appearance and consistency (Tractinsky et al. 2006), as well as atmospheric cues, such as interactivity or vividness, may impact users’ emotions (Sheng and Joginapelly 2012). From a practitioners’ perspective, Microsoft’s Usability Guidelines explicitly acknowledge the role of interface design in evoking users’ emotions (Keeker 1997). While the relative impact of emotion on users’ assessments and behaviors is dependent on the task and the medium (Agarwal and Venkatesh 2002; Venkatesh et al. 2003; Venkatesh and Ramesh 2006), both the design of and the interaction with a system influence emotions in various contexts (Zhang 2013). Positive emotion induced through system design has been shown to influence the acceptance and use of technology (e.g., Agarwal and Karahanna 2000). In contrast, negative emotion induced through system design adversely influences ease-of-use and thereby intentions to use a system (Venkatesh and Davis 2000), technology use (Beaudry and Pinsonneault 2010), disclosure of information (Anderson and Agarwal 2011), online purchasing decisions (Huang 2003), and customer loyalty (Lin and Wang 2006). For example, online shoppers who experience negative emotion are more likely to leave (Tax and Brown 1998) and not return (Mulpuru et al. 2010) to e-commerce websites. Users who experience negative emotion are also more likely to spread negative word of mouth (Gelbrich 2010), which may hurt the profitability and success of online companies (e.g., Haywood 1989). The ability to easily assess users’ negative emotion during live system use has practical significance for the design, evaluation, and continuous improvement of information systems.

One potential methodology for inferring users’ emotions is through analyzing data collected from HCI user-input devices. Users interact with technology using various input devices, including the computer mouse, touch screens, and other devices. In addition to enabling interaction with technology, these devices are also high-fidelity sensors that gather valuable information about the user (Google 2015). For example, tracking the mouse cursor provides precise information about a person’s motor movements with millisecond and sometimes microsecond precision (Hehman et al. 2014). Likewise, mobile phones can not only capture precise motor-movement information when people touch the screen, but also position and motion information captured through the device’s accelerometer and gyroscope (Kim and Choi 2012). This information can indicate emotional and cognitive states of users (Freeman et al. 2011; Kim and Choi 2012).

In this paper, we specifically examine the efficacy of using mouse cursor movements to infer negative emotion, providing a method for unobtrusive and mass-deployable emotion assessment. For example, one can record mouse cursor movements as users interact with a website without interfering with their interaction. System designers can then identify segments of the interaction that are inducing negative emotion by analyzing these mouse cursor movements. Designers can use this information to better understand where to make system improvements. Further, if mouse cursor movements can be used to infer negative emotion, a system can automatically detect when one is likely experiencing a negative emotional reaction and intervene to alleviate the negative reaction, such as by providing users opportunities to express their concerns (Klein et al. 2002), apologetic statements (Tzeng 2004), compensation (Smith et al. 1999), or explanations (Kuo et al. 2011).

To explain how negative emotion influences mouse cursor movements, we draw on attentional control theory (ACT) (Eysenck et al. 2007). ACT explains that negative emotion decreases people’s ability to control their attention. Merging ACT with research demonstrating that attention influences mouse movements (Welsh and Elliott 2004), we explain how negative emotion influences mouse cursor movements, specifically mouse cursor distance and speed. Although past literature has empirically suggested that emotion influences mouse cursor movements (e.g., Salmeron-Majadas et al. 2014), our research provides a theoretical foundation explaining why negative emotion influences mouse cursor distance and speed.

In summary, our research is guided by two research questions:

RQ1: Does negative emotion influence mouse cursor distance and speed?

RQ2: Can the tracking and analysis of mouse cursor distance and speed be used to infer negative emotion?

In answering these questions, we contribute to research and practice in HCI. As an initial step, we hypothesize and empirically test the effects of negative emotion on mouse cursor movements. This lays the foundation for future research to examine the influence of other emotions on mouse cursor movements and the influence of emotion on the usage of other HCI user-input devices. In particular, we contribute to research by explaining why negative emotion (1) decreases the precision of users’ movements, resulting in greater movement distance, and (2) consumes cognitive resources, resulting in slower movement speed. We empirically demonstrate that mouse cursor distance and speed can be used to infer negative emotion. Thus, we respond to calls in the information systems literature to utilize psychophysiological tools that provide new methodological approaches for investigating the development and use of systems (see Dimoka et al. 2012). Further, we provide a methodology for assessing users’ negative emotions in real time, enabling both academic and practitioner research that cannot be easily conducted using traditional assessments. These opportunities in HCI research include gauging negative emotional reactions during live system use, examining emotional reactions with more temporal precision, conducting multimethod emotion research, and creating more unobtrusive affective and adaptive systems.

## Background

## Emotion and Motor Responses

Emotion is typically characterized as relatively brief experiences that are associated with the cognitive appraisal of an external stimulus or situation (Lazarus 1991), such as an appraisal of a website or online vendor (Sun and Zhang 2006). Emotion has been defined as

a mental state of readiness that arises from cognitive appraisals of events or thoughts; has a phenomenological tone; is accompanied by physiological processes; is often expressed physically (e.g., in gestures, posture, facial features); and may result in specific actions to affirm or cope with the emotion (Bagozzi et al. 1999, p. 184).

Emotion can be classified based on three independent and bipolar dimensions: pleasure, arousal, and dominance (Lang and Bradley 2007; Russell and Mehrabian 1977). Pleasure ranges from extreme unhappiness to extreme happiness. Arousal ranges from sleep to excitement, with intermediate states of drowsiness to alertness. Dominance ranges from feelings of a total lack of control to extreme feelings of influence and control (Russell and Mehrabian 1977). Our research focuses on how the pleasure dimension—specifically negative emotion—influences mouse cursor movements. We chose to focus on how this dimension of emotion influences mouse cursor movements because past research has robustly shown that negative emotions deter users’ adoption and use of e-commerce sites (e.g., Anderson and Agarwal 2011; Beaudry and Pinsonneault 2010; Deng and Poole 2010; Gelbrich 2010; Huang 2003; Mulpuru et al. 2010).

Neurological research suggests that “negative emotions have selective, direct connections to brain structures that mediate motor responses,” including movements in the arm and hand (Coelho et al. 2010, p. 135). Further research suggests that negative emotion influences motor track excitability—the electrical stimulation in the nerves that initiate movement (e.g., Tanaka et al. 2012)—and elicit motor evoked potentials, that is, electrical stimulation recorded on the muscles indicating potential movement (Coelho et al. 2010). Furthermore, negative emotion can influence motor movement reaction times, and the amount of muscle force that is produced (Coombes et al. 2008; Coombes, Tandonnet, et al. 2009; Naugle et al. 2012).

## Attentional Control Theory

We draw on attentional control theory (ACT) (Eysenck et al. 2007) to explain how negative emotion influences mouse cursor distance and speed. ACT explains that when experiencing negative emotion, people’s attention shifts from being goal-directed to being stimulus-driven, increasing awareness of distracting stimuli in the environment (e.g., stimuli causing negative emotion). In neurological terms, negative emotion suppresses the brain’s attentional inhibition and shifting functions. Attentional inhibition refers to the function of the brain that prevents stimuli unrelated to a task from capturing attention. Attentional shifting allocates attention to stimuli that are most relevant to a task. ACT further posits that processing more stimuli when experiencing negative emotion reduces the processing capacity of working memory, which decreases task performance (Eysenck et al. 2007).

ACT has been widely validated (Eysenck and Derakshan 2011). The theory was originally used to describe how anxiety influences attentional control; however, since its inception, it has been extended to explain how other negative emotional responses, including frustration, sadness, fear, and depression, decrease attentional control (Bishop et al. 2007; Sarter and Paolone 2011). ACT also has been utilized to explain the influence of emotional states on motor movement planning, and therefore has relevance for understanding mouse cursor movements. For example, based on ACT, research has explained how trait anxiety influences motor efficiency in the hand and fingers (Coombes, Higgins, et al. 2009), how physiological pressure influences visuomotor control—that is, using visual feedback to guide hand movements (Vine and Wilson 2011), and how physiological pressure influences corticospinal motor tract excitability and performance of finger movements (Tanaka et al. 2012).

## Negative Emotion and Mouse Cursor Movements

In HCI research, emotions have been primarily assessed using either self-report measures or psychophysiological tools (e.g., Sheng and Joginapelly 2012). Using these measures and tools has both advantages and shortcomings (see Dimoka et al. 2012). Whereas self-report measures are relatively easy to administer, their use is typically limited to academic research, and the responses are subject to various biases. Psychophysiological tools (such as facial electromyography) can allow assessing emotions with high temporal precision, but their application is typically limited to studies conducted in a laboratory. In contrast, mouse cursor movements can be recorded unobtrusively during live interactions with a system. Prior HCI research provides preliminary support that emotion may influence mouse cursor movements. For example, Maehr (2008) elicited emotional states through three film clips in an experiment: a neutral video, a video provoking sadness, and a video promoting happiness. After watching each video, participants answered a questionnaire about their feelings while mouse cursor movements were being logged and analyzed. The results suggest that emotional changes influence the precision, smoothness, speed, and acceleration of mouse movements. Grimes et al. (2013) manipulated arousal (high versus low) and pleasure (positive versus negative) through images from the International Affect Picture System (Lang and Bradley 2007), finding that negative emotion increased direction changes and distance, as well as decreased the speed of people’s mouse movements. Zimmerman and his colleagues (Zimmerman et al. 2006; Zimmerman et al. 2003) manipulated mood through film clips, finding that mood state was correlated with mouse cursor movements.

Further, Sun et al. (2014) examined how mouse movements could be used to detect muscle stiffness associated with stress. They induced stress through social pressure, time pressure, repetition, and performance pressure. Their results indicated that muscle stiffness from stress influences users’ mouse movements. Salmeron-Majadas et al. (2014) monitored mouse movements as students completed math problems and then correlated 96 mouse indicators with self-reported pleasure and arousal. Finally, Weinmann et al. (2013) described the functional requirements for designing a system capable of inferring emotion through analyzing mouse movements in online stores. Table 1 summarizes how emotions may influence hand and mouse cursor movements.

We address two gaps in this research. First, much of the prior research is exploratory and observational, void of theory explaining why emotion influences mouse movements. Drawing on and extending ACT, we explain why negative emotion will influence users’ mouse cursor movements. Second, prior results are mostly based on single studies; thus, the generalizability of the observations is likely limited. Here, we conduct three independent studies utilizing different contexts and populations to cross-validate that negative emotion consistently influences mouse cursor movements. In Study 1, we examine whether negative emotion influences users’ mouse cursor movements; in Study 2, we examine whether mouse cursor movements can be used to infer the presence of negative emotion; and in Study 3, we examine whether mouse cursor movements can be used to infer the level of negative emotion that users experience. Taken together, we demonstrate that mouse cursor movements can be used to infer negative emotion in realistic e-commerce settings.

## Theory

Drawing on ACT, we hypothesize how negative emotion will decrease attentional control and thereby influence two characteristics of users’ mouse cursor movements: movement distance and speed. As ACT explains how negative emotion “impairs efficient functioning of the goal-directed attentional system” (Eysenck et al. 2007, p. 336), the scope of our hypotheses is to explain the relationship between negative emotion and movements in goal-directed tasks. Goal-directed tasks refer to activities that are motivated by goal attainment rather than the interaction itself, and the user’s reward is primarily realized by efficiently accomplishing the goal, rather than the journey of accomplishing the goal. Searching for specific information, paying a bill, or navigating through a checkout process are examples of online goal-directed tasks (Wells et al. 2005). In goal-directed tasks, mouse cursor movements are characterized by structured, efficient, linear search patterns (e.g., moving the mouse cursor from a starting point to a specific target in an effort to accomplish a goal as efficiently as possible).

<table><tr><td colspan="2">Table 1. Examples of Relevant Literature Linking Emotions to Hand and Mouse Cursor Movements</td></tr><tr><td>Key Findings</td><td>Reference</td></tr><tr><td>Negative emotion induced by pictures results in greater motor evoked potentials (neuroelectrical signals on the muscles) than emotion induced by neutral and pleasant pictures. No differences were found between pleasant and neutral pictures.</td><td>Coelho et al. 2010</td></tr><tr><td>People viewing emotional images subconsciously produce greater force in the hand compared to people viewing neutral images.</td><td>Coombes et al. 2008</td></tr><tr><td>People with high behavioral inhibition display a relative increase in unconscious force production during exposure to attack and mutilation images.</td><td>Coombes et al. 2011</td></tr><tr><td>People viewing negative-emotion inducing images display greater direction changes, distance, and slower mouse cursor speed while self-reporting their emotional state. Arousal further elevates direction changes and distance.</td><td>Grimes et al. 2013</td></tr><tr><td>Emotional changes can be inferred from mouse cursor movements, including changes in precision, smoothness, speed, and acceleration.</td><td>Maehr 2008</td></tr><tr><td>People viewing emotional images subconsciously produce greater force in the hand compared to people viewing neutral images. However, emotional images do not increase variability of force production compared to neutral images.</td><td>Naugle et al. 2012</td></tr><tr><td>Ninety-six mouse indicators are correlated with self-reported emotional valance and arousal.</td><td>Salmeron-Majadas et al. 2014</td></tr><tr><td>Stiffness resulting from stress influences mouse movements.</td><td>Sun et al. 2014</td></tr><tr><td>Stress increases the amplitude and decreases the latency of motor evoked potentials and increases the ratio of motor evoked potentials to background electromyography. From a behavioral perspective, the level of corticospinal motor tract excitability under stress is correlated with a decrease in performance of fine motor skills.</td><td>Tanaka et al. 2012</td></tr><tr><td>The amplitudes of motor evoked potentials are typically increased when viewing negatively valenced images.</td><td>van Loon et al. 2010</td></tr><tr><td>Systems should monitor mouse movement deviations to infer negative emotion.</td><td>Weinmann et al. 2013</td></tr><tr><td>Mood states are correlated with the number and duration of clicks, distance of movements, pauses, direction changes, speed, and keystroke dynamics.</td><td>Zimmermann et al. 2006 Zimmermann et al. 2003</td></tr></table>

## Negative Emotion and Mouse Cursor Distance

We propose that negative emotion will decrease the precision of users’ movements and thereby increase the distance users travel with the mouse cursor to accomplish a goal-directed task. As discussed, ACT explains that negative emotion deters the attentional shifting and inhibition functions of the brain. People are less able to focus their attention on the most relevant stimuli (i.e., the destination of the movement), and focus their attention more broadly on stimuli in the environment (Eysenck et al. 2007). As a result, distracting stimuli not related to one’s intended movement are more likely to catch one’s attention (Eysenck et al. 2007).

These distracting stimuli will influence the precision of movements because “attention and action are intimately linked” (Welsh and Elliott 2004, p. 1054). Visually processing a stimulus, consciously programing a movement response to the stimulus, and then making the movement can take several hundreds of milliseconds or longer for the brain to execute (Thorpe et al. 1996). To facilitate more efficient movements, the brain anticipatorily programs movements to stimuli that capture a user’s attention during movement. This preprograming of movements occurs in the brain automatically, subconsciously, and simultaneously in response to all stimuli that capture a person’s attention, even if only briefly (Welsh and Elliott 2004). This way, if a user does decide to move toward a stimulus, programing is already underway to facilitate a more efficient movement (Welsh and Elliott 2004).

The actual hand movement that occurs is a function of both one’s consciously intended movement and the subconscious programed movements toward other stimuli. For example, if one intends to move the mouse straight to a target, and the brain has subconsciously programed movements toward other distracting stimuli, these primed subconscious movements will influence the actual movement, and the resulting movement will deviate from one’s intended trajectory. One’s fine motor movements—movement of the fingers or hands—are especially vulnerable to these actions that are primed by negative emotion (Tanaka et al. 2012). As deviations occur, one’s mouse cursor is likely to travel a greater distance, as the movement deviates from the most direct path when experiencing negative emotion (see Figure 1). Thus, we propose our first hypothesis:

![](/api/attachments/GQHDJAP4/fulltext/images/444663c9eaebf6845bae9f836ab00946bd09becd68d89602528201393d51ab31.jpg)  
Figure 1. Example Mouse Cursor Trajectory Under the Influence of Negative Emotion

H1: Experiencing negative emotion will increase overall mouse cursor distance.

## Negative Emotion and Mouse Cursor Speed

We also propose that negative emotion will decrease the average speed of users’ mouse cursor movements in goaldirected tasks. Recall that negative emotion causes people to distribute their attention more broadly (Eysenck et al. 2007). ACT explains that this broader attentional focus reduces the processing and storage capacity of working memory. Unsworth and Spillers (2010, pp. 392-393) explain that “attention and working memory are intimately related....attention control and the scope or size of the focus of attention are important components of working memory.” Lower attentional control under conditions of negative emotion allows more stimuli to capture attention, which utilizes more working memory, leaving less for the primary task (Eysenck et al. 2007).

Decreased working memory capacity due to negative emotion has been robustly shown to influence people’s reaction time (Eysenck et al. 2007; Kannape et al. 2014). When working memory is consumed or split between multiple tasks, people must engage in “compensatory strategies” to complete their active tasks—that is, alterations in resource allocation and performance to complete tasks in suboptimal conditions (Eysenck et al. 2007, p. 340). One common compensatory strategy for lower working memory is to respond more slowly, allowing the brain a longer period of time to execute the task (Eysenck et al. 2007). From a neurological perspective, when working memory is low because several stimuli are competing for attention, the brain gives each stimulus a portion of working memory for a short period of time (much like multithreading on computers) (Pashler 1994). However, because the brain must switch cognitive resources among multiple competing stimuli, it will take longer to complete tasks and slow reaction time for tasks.

Reaction time influences mouse cursor speed. When directing the mouse cursor to a destination, the brain processes corrections to the movement trajectory based on continuous visual input to ultimately reach the destination (Meyer et al. 1988; Meyer et al. 1990). These corrective movements are dependent on hand-eye coordination reaction time (i.e., processing visual inputs and making adjustments to reach the target) (Lin et al. 2011). Slower reaction time (i.e., taking longer to process visual inputs and program adjustments) inhibits one’s ability to make corrections that will ultimately reach the target. Because the user must nonetheless reach the target, the body subconsciously compensates for slower reaction time by reducing movement speed. Doing so gives the brain more time to perceive and program needed adjustments (Meyer et al. 1988; Meyer et al. 1990). In other words, under conditions of low attentional control and thereby slower reaction times (due to experiencing negative emotion), the brain requires additional time to perceptually guide mouse cursor movements to a target, which will result in slower speed (see Figure 2). Thus, we propose our second hypothesis:

H2: Experiencing negative emotion will decrease average mouse cursor speed.

![](/api/attachments/GQHDJAP4/fulltext/images/47e304bb210f20429d6833cc5189349acce8d24d4d5b75def7c0e2afd439bd4d.jpg)  
Figure 2. Relationship Between Negative Emotion, Reaction Time, and Mouse Cursor Speed

## Methodology

We conducted three studies. Study 1 is an experiment that tested our hypotheses to answer RQ1 (Does negative emotion influence mouse cursor distance and speed?). Study 2 is an experiment to answer RQ2 (Can the tracking and analysis of mouse cursor distance and speed be used to infer negative emotion?) for a dichotomous outcome variable (whether or not participants received a negative emotion manipulation). Finally, Study 3 is an observational study that further examined RQ2 by investigating the efficacy of inferring the level of negative emotion (a continuous variable) rather than only a dichotomous outcome (as in Study 2). Table 2 summarizes the three studies, their purposes, and the key findings.

## Study 1

In Study 1, we answered RQ1 (Does negative emotion influence mouse cursor distance and speed?). We manipulated negative emotion in a single factor experimental design (negative emotion condition versus baseline condition) to examine the influence of negative emotion on mouse cursor movements.

## Procedure and Manipulation

We randomly assigned participants to either a negativeemotion or a baseline (i.e., nonnegative-emotion) condition.

After the treatment, all participants completed an identical follow-up task as we recorded and analyzed mouse cursor movements to test our hypotheses.

Negative-emotion condition: We induced negative emotion through an intelligence test designed to be unfair (Zuckerman 1955). The instructions explained that the test was timed, and the score would be computed based on how many questions participants answered correctly within the allotted time. While participants read the instructions, a timer in the upper right hand corner of the screen began to increment. Before loading the first question, a sequence of three 8-second messages stating that the question was being loaded was shown (Figure 3); during this time, the timer incremented. Finally, the system showed the question, giving participants 15 seconds to answer the question before the page automatically advanced. The question was difficult, requiring longer than 15 seconds to answer. After the page automatically advanced, the cycle repeated; that is, the system again displayed the sequence of three 8-second loading messages, while the timer incremented (see Figure 3). This was followed by the second difficult question that also took longer than 15 seconds to complete. After the second question automatically advanced, the system told participants that the time had expired. The system also gave participants feedback that they had only been given two out of three questions because they had taken too long to answer. Participants were then told that because of their slow reaction time and incorrect answers, their score indicated a lower intelligence level than that of most people who had taken the test.

<table><tr><td colspan="5">Table 2. Summary of Studies</td></tr><tr><td>Study</td><td>Methodology</td><td>Purpose</td><td>Sample</td><td>Findings</td></tr><tr><td>1</td><td>Experimentmanipulatingnegative emotion</td><td>Answer RQ1</td><td>65 AmazonMechanicalTurk Workers</td><td>Negative emotion influences mouse cursor distance and speed.</td></tr><tr><td>2</td><td>Experimentmanipulatingnegative emotion</td><td>Answer RQ2 in inferring the presence of emotion</td><td>126 U.S.Students</td><td>Mouse cursor distance and speed can infer whether participants received the negative emotion manipulation with an 81.7% accuracy rate.</td></tr><tr><td>3</td><td>Observational studyallowing emotion to vary naturally across tasks</td><td>Answer RQ2 in inferring the level of emotion.</td><td>80 German/Hong KongStudents</td><td>Mouse cursor distance and speed can infer the level of self-reported emotion with an out-of-sample  $R^2$  up to .17.</td></tr></table>

Following the above steps induced negative emotion in three ways. First, we implemented a loading delay under time pressure. Loading delays have been shown to induce negative emotion (Ceaparu et al. 2004; Galletta et al. 2004); moreover, having the timer increment during loading delays in a timed test causes a feeling of being treated unfairly and negative emotion. Second, the questions were unduly difficult and impossible to process during the given time. Finally, participants were told that they achieved a poor score, even though the score was outside of their control. After the experiment, we debriefed all participants, informing them that the test did not actually assess intelligence, but that it was a task designed to induce negative emotion to examine its influence on mouse cursor movements.

Baseline condition: As in the negative emotion condition, the instructions of the baseline condition explained to participants that they would take an intelligence test. The delivery of the questions in this condition was similar to the negativeemotion condition, except that we did not implement the negative-emotion-inducing mechanisms (i.e., the test was not timed; the sequence of loading messages was not shown; the three questions could easily be answered; and, at the conclusion, the system congratulated participants for answering the questions correctly). Thus, the task was not designed to induce negative emotion.

Follow-up task: Following the manipulation and before the debriefing, all participants engaged in an identical goaldirected task, during which we recorded and analyzed mouse cursor movements. We added this follow-up task to test the influence of negative emotion (induced by the negativeemotion condition) on mouse movements. By using an identical follow-up task, we can attribute the difference in mouse cursor movements to negative emotion, and not differences in the task. The task required participants to drag six 4-digit numbers from a box on the left side of the screen to a box on the right side of the screen, and to arrange them in ascending order.

## Participants

We recruited participants for the experiment from Amazon.com’s Mechanical Turk (MTurk).<sup>2</sup> We required all participants to have an Amazon Masters certification (awarded to people who have demonstrated quality across a wide variety of tasks), and paid them US\$0.40 for a 4-minute task.<sup>3</sup> Given that our study focused on mouse cursor movements, we further captured the type of device used, and removed data points from mobile devices. This resulted in a final sample size of 65 participants. Forty-seven percent of the participants were from the U.S., 44 percent from India, and 9 percent from other locations. Table 3 presents the sample sizes and demographics of each condition.

## Measures

Using a publicly available JavaScript library (JQuery), the webpage containing the follow-up task captured the mouse cursor’s x/y position and timestamp at a millisecond precision rate while the participants completed the follow-up task. Once

<sup>2</sup>Using MTurk to recruit participants has been deemed appropriate for random sample populations (Berinsky et al. 2012). Social scientists are increasingly using MTurk as the diversity of the participant pool is larger than that of typical undergraduate college samples, and the data are as reliable as those collected using other methods (Buhrmester et al. 2011). In a U.S. context, Steelman et al. (2014) found that studies using MTurk yield similar statistical conclusions as both student and consumer panels. Further, Mason and Suri (2012) found that the behavior of MTurk respondents closely resembled that of participants in traditional laboratory experiments.

![](/api/attachments/GQHDJAP4/fulltext/images/c15f11d6b5c2c47fa92f7697b61cb9b3d9ee69950c223ab80843e9cef99d8184.jpg)

Loading the first question... Please wait

Still loading the first question... Please be patient

![](/api/attachments/GQHDJAP4/fulltext/images/00997d0e26414bf29818cb73be9f4bdd3e75977828a481d177931dd4f5bb05da.jpg)

Question loaded. Processing first question...

![](/api/attachments/GQHDJAP4/fulltext/images/dbe9c3f1272e84e8ecc684eacc08a2dbad4bebc46189317cdb58166a11490a57.jpg)  
Figure 3. Sequence of Messages Displayed in the Negative-Emotion Condition

<table><tr><td colspan="3">Table 3. Participant Demographics of Study 1</td></tr><tr><td></td><td>Baseline Condition</td><td>Negative Emotion Condition</td></tr><tr><td>Total Participants</td><td>33</td><td>32</td></tr><tr><td>Men</td><td>48%</td><td>46%</td></tr><tr><td>Average Age</td><td>34.5 (SD = 5.1)</td><td>33.8 (SD = 4.6)</td></tr></table>

<table><tr><td colspan="6">Table 4. Descriptive Statistics for Study 1</td></tr><tr><td></td><td>Mean</td><td>Median</td><td>Std. Dev.</td><td>Min</td><td>Max</td></tr><tr><td>Distance (px)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Baseline Condition</td><td>8,337</td><td>8,171</td><td>2,879</td><td>4,075</td><td>13,716</td></tr><tr><td>Negative-Emotion Condition</td><td>10,872</td><td>9,939</td><td>4,321</td><td>6,467</td><td>21,986</td></tr><tr><td>Speed (px/ms)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Baseline Condition</td><td>.18</td><td>.17</td><td>.067</td><td>.09</td><td>.38</td></tr><tr><td>Negative-Emotion Condition</td><td>.15</td><td>.14</td><td>.048</td><td>.06</td><td>.25</td></tr><tr><td>SAM Pleasure</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Baseline Condition</td><td>7.76</td><td>9</td><td>1.50</td><td>5</td><td>9</td></tr><tr><td>Negative-Emotion Condition</td><td>3.31</td><td>3</td><td>2.33</td><td>1</td><td>9</td></tr></table>

completed, the webpage calculated total distance and average cursor speed.<sup>4</sup> As a manipulation check in a post survey, we also assessed pleasure and arousal through the self-assessment

$$
d \left(a _ {i}, a _ {i + 1}\right) = \sqrt {\left(a _ {i} ^ {(s)} - a _ {i + 1} ^ {(x)}\right) ^ {2} + \left(a _ {i} ^ {(y)} - a _ {i + 1} ^ {(y)}\right) ^ {2}}
$$

$$
D = \sum_ {i = 1} ^ {n - 1} d (a _ {i}, a _ {i + 1})
$$

manikin (SAM) scale—a nine-point pictorial scale of emotion (Bradley and Lang 1994).

## Results

The manipulation check showed that the participants in the negative-emotion condition reported significantly more negative emotion than did those in the baseline condition (t(63) = 9.162, p < .001), indicating that our manipulations were successful. No significant difference was observed in arousal between the conditions $( t ( 6 3 ) = 1 . 5 2 5 , p > . 0 5 )$ We then conducted a t-test to test the hypothesized relationships between negative emotion and mouse cursor movements and found that participants in the negative-emotion condition had significantly greater cursor distance (t(63) = 2.774, p < .01, η<sup>2</sup> = .109) and slower mouse cursor speed (t(63) = 2.257, p < .05, η<sup>2</sup> = .091) than did participants in the baseline condition. Thus, our results support both hypotheses H1 and H2 (see Table 4 for the summary statistics).

## Study 2

In Study 2, we answered RQ2: Can the tracking and analysis of mouse cursor distance and speed be used to infer negative emotion? In a realistic e-commerce scenario, we manipulated negative emotion in a single factor experimental design (negative emotion condition versus baseline condition); we then specified a model to infer whether participants were in the negative emotion condition (a dichotomous outcome) based on mouse cursor distance and speed.

## Procedure and Manipulation

We asked participants to complete a goal-directed task on an e-commerce website. The website was developed for this experiment to ensure no one had previous experience with it. Before interacting with the website, a system gave participants the following instructions:

After clicking next, you will be directed to a computer store website. Your task is to navigate the website and pretend to purchase the following product:

J. Crew Abingdon Laptop Bag for a 17 inch laptop

![](/api/attachments/GQHDJAP4/fulltext/images/17acf077dda0a72c2ef336360155adf24d3850a98ef4ee841395280cacd7e170.jpg)  
Please write down these details so you remember what product to find. After clicking on purchase, you will be guided to a survey.

After clicking “next,” the system led all participants to the homepage of the website. We designed the website such that there was only one obvious link on each page that would lead the user closer to goal attainment (finding the correct laptop bag). On the first page (the home page), users had to click on the “shop laptop cases” link (the only link on the page relevant to finding laptop bags) in the left sidebar to advance to the second page. On the second page, users had to click on the “J. Crew Abingdon Laptop Bag” that accompanied the picture shown earlier to advance to the next page. On the third page, users had to select their laptop’s “screen size” and click on “submit” to advance to the fourth page. On the fourth page, users could review the product and click “purchase.” After clicking on “purchase” the task was completed and the participants were automatically redirected to a post-survey. Figure 4 shows the four webpages. While participants interacted with the webpages, mouse cursor movements were recorded and stored in a database for analysis (see Study 1).

Negative-emotion condition: We randomly assigned half of the participants to the negative-emotion condition. We manipulated download delay (i.e., webpage loading speed) and error messages to induce negative emotion (Ceaparu et al. 2004; Galletta et al. 2004). When participants clicked on a link to advance the page (from page 1 to 2, page 2 to 3, and page 3 to 4), the webpage stopped recording mouse cursor movements, dimmed the screen, disabled the links, and showed a sequence of three 8-second messages stating that the page was being loaded (see Figure 5). After the manipulation, users re-clicked on the link, which acted as an anchor for the mouse cursor so that participants (regardless of the condition) would have approximately the same starting position on the next page.

Baseline condition: The other half of participants were randomly assigned to the baseline condition. In this condition, pages were loaded without delay. The system recorded mouse cursor movements after loading each page. Hence, the scope of the mouse cursor movement analysis had the same beginning and ending points regardless of condition (and excluded the negative emotion manipulation that was unique to the negative-emotion condition).

## Participants

A total of 126 students<sup>5</sup> from a management school at a large U.S. university participated in the experiment (see Table 5). As compensation, students earned .25 percent extra credit applied to a participating management course of their choice.

<table><tr><td>Page 1<img src="/api/attachments/GQHDJAP4/fulltext/images/bae23030b8e753b901a202fd9095c5a519c6e1cb0c9db62fd140145d17d2219a.jpg"/>WELCOME to Computer StoreThis is Computer Store. One of the Web's leading destinations for computer and electronics, Computer Store is your source for laptop computers, desktop computers, tablets, and related computer products. Our ratings, rankings, and pricing help you find the top computer products and best computer deals.FEATURED productHard DrivesMonitoresLaptopsPrice: $99.00DetailsPrice: $99.00DetailsPrice: $99.00Details<img src="/api/attachments/GQHDJAP4/fulltext/images/ba321e29d5c53e84d4c6810699cac22fd51c19978874c4a213bffc0a9090d8d8.jpg"/></td><td>Page 2<img src="/api/attachments/GQHDJAP4/fulltext/images/905d32e767c09c2dc444d0b429e07313f2bf78911409d52cb7a5597218c90be1.jpg"/></td></tr><tr><td>Page 3<img src="/api/attachments/GQHDJAP4/fulltext/images/f8f653a447f647044612876cc1954267de85de8a17bd11db32deb67e0c4e0bc3.jpg"/>Select Your Laptop Size:10.1 + SubmitHaving a website isn't enough.wwwCreate free websiteHome About Us Faq Contact Us Services Products Support Technology Clients Testimonials</td><td>Page 4<img src="/api/attachments/GQHDJAP4/fulltext/images/59ec88197ea2ec02025a44d1afbb87e3b1cbbbea67f102ac42bf992face6d03c.jpg"/>J. CREW ABINGDON LAPTOP BAG<img src="/api/attachments/GQHDJAP4/fulltext/images/d408dc2263e4b282a9e84bd9ea4962c35d19a44171c88cfe468f526847e4e6b8.jpg"/>Purchase Talk with a Sales RepresentativeOverviewInspired by vintage hunting gear, with a focus on timeless fabrics and a made-to-last construction in rugged washed cotton canvas. It turns out these durable features 54 favorites of outdoorsmen everywhere 54 are also surfied to the whole lack of laptop hitting. Given that our computer is a constant companion, they're details were all for.3" handle drop.14Hz x 15W x 4D.Removable, adjustable shoulder strap fully extends to 52".Washed cotton canvas.Burnished leather trim.Brasa finish hardware.ImportHome About Us Faq Contact Us Services Products Support Technology Clients Testimonials</td></tr><tr><td>Please wait while the next page loads.</td><td>After clicking on the link to reach the next page, recording of mouse cursor movements stopped, the window was dimmed, all links were disabled, and this loading message was displayed.</td></tr><tr><td>Page still loading. Please be patient.</td><td>After eight seconds of seeing the first message, this message was shown.</td></tr><tr><td>Error loading page. Please try again.</td><td>Finally, after eight seconds of the second message, this prompt was shown. The user then was required to click on the link again (to anchor the mouse in this position). After clicking on the link the second time, the page progressed, and recording of mouse cursor movements resumed.</td></tr></table>

Figure 4. Website Designed for Study 2

Figure 5. Sequence of Messages Displayed in the Negative-Emotion Condition

## Measures

The website collected and analyzed mouse cursor movements using the same embedded JavaScript library and process as described in Study 1. After clicking on the “purchase” link, the webpage redirected participants to an online survey. In the survey, participants reported their emotion using the SAM scale (Bradley and Lang 1994).

## Model Specification

To answer research question 2, we created a model to infer whether participants were in the negative-emotion condition based on their mouse cursor movements. Prior to specifying the model, we performed manipulation checks comparing the means for pleasure and arousal between the conditions. Participants in the negative-emotion condition reported significantly more negative emotion $( t ( 1 2 4 ) = 1 0 . 8 4 5 , p < . 0 0 1 )$ ) and significantly higher arousal (t(124) = 5.440, p < .05) than participants in the baseline condition, a combination indicating that the manipulation resulted in the negative emotion of frustration (characterized by both low pleasure and high arousal). Thus, our manipulation appeared to be successful.

Based on these results, we specified a simple logistic regression model to infer whether participants were in the negativeemotion condition based on their average mouse cursor distance and speed. The model is

$$
\begin{array}{c} \text { negative   emotion   treatment   (binary) } _ {i} = \\ a + \beta_ {2} \cdot \text { cursor   distance } _ {i} + \beta_ {2} \cdot \text { cursor   speed } _ {i} + \varepsilon_ {i} \end{array}
$$

where i indexes the individuals.

## Results

Table 6 presents summary statistics for distance, speed, and pleasure. The model results indicate a significantly positive coefficient for mouse cursor distance<sup>6</sup> $( \beta = . 0 8 , p < . 0 0 1 )$ consistent with H1 (indicating that greater distance is correlated with being in the negative-emotion condition). Further, consistent with H2, the coefficient of the average cursor speed<sup>7</sup> was significantly negative (β = -7.84, p < .001) (indicating that slower speed is correlated with being in the negative-emotion condition). We assessed the model using a 10-fold cross validation technique and achieved an overall accuracy rate of 81.7 percent. Thus, affirming RQ2, our results suggest that mouse cursor distance and speed can be used to infer the presence of negative emotion. The detailed accuracy rates are shown in Table 7.

## Study 3

In Study 3, we examined the efficacy of inferring the level of negative emotion (a continuous variable) as opposed to a dichotomous variable (as done in Study 2) to further answer RQ2. Study 3 was an observational study, allowing participants’ emotion to vary naturally without direct manipulation while completing goal-directed tasks. After each task, participants self-reported their level of negative emotion. We then examined the efficacy of using participants’ mouse cursor distance and speed to infer their level of self-reported negative emotion.

<sup>7</sup>Unit: px/ms.

<table><tr><td colspan="3">Table 5. Participant Demographics of Study 2</td></tr><tr><td></td><td>Baseline Condition</td><td>Negative-Emotion Condition</td></tr><tr><td>Total Participants</td><td>62</td><td>64</td></tr><tr><td>Men</td><td>60%</td><td>63%</td></tr><tr><td>Average Age</td><td>22 (SD = 6.2)</td><td>23 (SD = 5.8)</td></tr></table>

Table 6. Descriptive Statistics for Study 2

<table><tr><td></td><td>Mean</td><td>Median</td><td>Std. Dev.</td><td>Min.</td><td>Max.</td></tr><tr><td>Distance (px)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Baseline Condition</td><td>6,540</td><td>6,284</td><td>2,830</td><td>2,047</td><td>13,108</td></tr><tr><td>Negative-Emotion Condition</td><td>12,131</td><td>10,317</td><td>7,298</td><td>3,894</td><td>33,623</td></tr><tr><td>Speed (px/ms)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Baseline Condition</td><td>.173</td><td>.159</td><td>.063</td><td>.089</td><td>.403</td></tr><tr><td>Negative-Emotion Condition</td><td>.120</td><td>.115</td><td>.038</td><td>.031</td><td>.209</td></tr><tr><td>SAM Pleasure</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Baseline Condition</td><td>7.45</td><td>8</td><td>1.62</td><td>3</td><td>9</td></tr><tr><td>Negative-Emotion Condition</td><td>3.82</td><td>3</td><td>2.11</td><td>1</td><td>9</td></tr></table>

<table><tr><td colspan="7">Table 7. Detailed Model Accuracy Results for Study 2</td></tr><tr><td>Condition</td><td>True Positive Rate</td><td>False Positive Rate</td><td>Precision</td><td>Recall</td><td>F-Value</td><td>ROC Area</td></tr><tr><td>Baseline</td><td>.823</td><td>.188</td><td>.810</td><td>.823</td><td>.816</td><td>.891</td></tr><tr><td>Negative-Emotion</td><td>.813</td><td>.177</td><td>.825</td><td>.813</td><td>.819</td><td>.891</td></tr><tr><td>Weighted Average</td><td>.817</td><td>.182</td><td>.818</td><td>.817</td><td>.817</td><td>.891</td></tr></table>

## Task and Stimuli Materials

We created five goal-directed tasks to be completed on one of two different websites (see Appendix B, Figures B1 and B2). These tasks required participants to configure a laptop computer (at dell.com) or a car (at volkswagen.co.uk). We chose to use product configuration systems for three primary reasons. First, product configurators are widely used by organizations for selling complex products. Second, product configurators require the use of the mouse when used on a desktop computer. Third, product configuration typically involves multiple, sometimes complex, steps, and thus has the potential to elicit a range of emotional reactions depending on various factors, including participants’ experience with the product category or configuration system, goal commitment, and so on (Campbell and Gingrich 1980; Nadkarni and Gupta 2007). We used configurators of two products to control for potential product-familiarity effects.

We pretested and fine-tuned the tasks using the think aloud method (Jorgensen 1990; van Someren et al. 1994), and assessed participants’ emotions to verify adequate variation in emotion among people. In addition, we ensured that the tasks were comparable in terms of length and difficulty. The tasks included selecting a product model, selecting different product attributes, and completing the configuration of the product (see Appendix C).

## Procedure

After collecting demographic information, we randomly assigned participants to either the Dell or the Volkswagen configuration website, and asked each participant to complete the five different tasks using the configurator (see Appendix C).<sup>8</sup> During each task, we recorded each participant’s mouse cursor movements. After each task, we asked participants to self-report their emotional state. Given that emotion may be appraised differently if there is a time lag between experience and appraisal (Gross and Thompson 2007), we chose to assess emotional states immediately after each task. Further, measuring emotion after each task provided a within-subject design, allowing us to control for individual and task-related differences. After completing the final survey, we debriefed all participants. On average, each session lasted approximately one hour.

## Participants

We recruited 80 participants from two universities in Germany and Hong Kong. Each participant received a modest honorarium of €5/HK\$50 as compensation for their time. As each participant completed five tasks, we collected 200 observations for each configurator (for 400 total observations). Table 8 presents the participants’ demographics.

## Measures

We recorded participants’ mouse cursor movements using Mouse Recorder Pro (Version 2.0.6). This mouse monitoring software ran in the background on a computer, allowing us to capture mouse cursor movements on a real third-party website for which we did not have access to the source code (as opposed to inserting the mouse movement JavaScript code as in the previous studies). From this data, we calculated each participant’s mouse cursor distance and speed, analogous to the previous studies. Immediately after participants completed each task, we assessed emotional pleasure using the SAM scale as our dependent variable (Bradley and Lang 1994).

## Model Specification

We specified a linear fixed-effects regression model to estimate the relationship between mouse cursor distance/ speed and negative emotion using the SAM pleasure score.<sup>9</sup> The fixed-effects model accounts for the repeatedmeasurement nature of the data by allowing each participant to have his/her own intercept in the model. As such, the model accounts for unobserved between-subject heterogeneity (e.g., individual expertise, experience, etc.) in addition to observed heterogeneity (e.g., which configurator the participant interacted with). The model is

$$
\begin{array}{c} \text {emotions} _ {i t} = \alpha_ {i} + \beta_ {1} \cdot \text {cursor speed} _ {i t} \\ + \gamma^ {\prime} \cdot \text {additional mouse variables} _ {i t} + \lambda_ {t} + \varepsilon_ {i t} \end{array}
$$

where i indexes the individuals, t the task number, $\lambda _ { t }$ represents task-specific effects, and $a _ { i }$ refers to individual fixed effects.

## Results

Table 9 presents summary statistics for distance, speed, and pleasure. The model results indicate a significantly positive coefficient for mouse cursor distance<sup>10</sup> $( \beta = . 1 3 , p < . 0 0 1 )$ consistent with H1 (indicating that greater distance is correlated with lower ratings of pleasure). Further, consistent with H2, the coefficient of the average cursor speed<sup>11</sup> was significantly negative $( \beta = - 1 0 . 3 0 , \rho < . 0 1 )$ (indicating that slower speed is correlated with lower ratings of pleasure). As shown in Appendix D, Table D3, these results were highly robust with respect to alternative model specifications (i.e., fixed effects versus random effects versus pooled regression models).

To address RQ2, we analyzed the efficacy of inferring the level of negative emotion using our model. We first split the data set into training and validation data by drawing 60 random participants, providing us with 300 (60 × 5 tasks) observations in the training data set. We used the remaining 100 observations as validation data to test the predictive power for unknown participants (Sample Definition 1). In addition, we implemented an alternative definition of these data sets by using data from all participants, but only the observations of Tasks 1, 2, and 3, providing us with 240 (80 × 3) observations in the training data set, whereas the 160 observations of Tasks 4 and 5 were validation data (Sample Definition 2). This sample definition reflects a situation where the model is applied to unknown tasks instead of unknown participants. For both of these definitions, we estimated a model using cursor distance and cursor speed from the training data to infer negative emotion (i.e., the values of SAM pleasure scale) on the validation data. We evaluated the accuracy of these models with the out-of-sample R<sup>2</sup> (Campbell and Thompson 2008), which is defined as

$$
\text { Out - of - sample } R ^ {2} = 1 - \sum_ {i = 1} ^ {M} \left(y _ {i} - \hat {y} _ {i}\right) ^ {2} / \sum_ {i = 1} ^ {M} \left(y _ {i} - \bar {y} _ {\mathrm{IS}}\right) ^ {2}
$$

<table><tr><td colspan="5">Table 8. Participant Demographics of Study 3</td></tr><tr><td></td><td>Germany: Dell</td><td>Germany: Volkswagen</td><td>Hong Kong: Dell</td><td>Hong Kong: Volkswagen</td></tr><tr><td>Total Participants</td><td>20</td><td>20</td><td>20</td><td>20</td></tr><tr><td>Men</td><td>60%</td><td>55%</td><td>45%</td><td>35%</td></tr><tr><td>Average Age</td><td>26.40 (SD = 3.32)</td><td>27.65 (SD = 5.72)</td><td>22.40 (SD = 2.63)</td><td>22.60 (SD = 2.53)</td></tr></table>

<table><tr><td colspan="6">Table 9. Descriptive Statistics for Study 3</td></tr><tr><td></td><td>Mean</td><td>Median</td><td>Std. Dev.</td><td>Min.</td><td>Max.</td></tr><tr><td>Distance (px)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Panel A. Dell Configurator</td><td>12,602</td><td>11,588</td><td>7,989</td><td>276</td><td>49,205</td></tr><tr><td>Panel B. Volkswagen Configurator</td><td>12,864</td><td>11,516</td><td>7,515</td><td>1,437</td><td>40,217</td></tr><tr><td>Speed (px/ms)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Panel A. Dell Configurator</td><td>.14</td><td>.12</td><td>.06</td><td>.04</td><td>.39</td></tr><tr><td>Panel B. Volkswagen Configurator</td><td>.12</td><td>.12</td><td>.05</td><td>.02</td><td>.27</td></tr><tr><td>SAM Pleasure</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Panel A. Dell Configurator</td><td>4.33</td><td>4</td><td>2.28</td><td>1</td><td>9</td></tr><tr><td>Panel B. Volkswagen Configurator</td><td>4.31</td><td>5</td><td>2.19</td><td>1</td><td>9</td></tr></table>

<table><tr><td colspan="2">Table 10. Out-of-Sample Analyses in Study 3</td></tr><tr><td>Sample Definition 1</td><td></td></tr><tr><td>In-Sample  $R^{2}$ </td><td>.15</td></tr><tr><td>Out-of-Sample  $R^{2}$ </td><td>.17</td></tr><tr><td>Sample Definition 2</td><td></td></tr><tr><td>In-Sample  $R^{2}$ </td><td>.23</td></tr><tr><td>Out-of-Sample  $R^{2}$ </td><td>.05</td></tr></table>

where $\overline { { y } } _ { \mathrm { I S } }$ is the average emotion in the training data, $\hat { y } _ { i }$ is the inferred emotion in the validation data, and $y _ { i }$ is the assessed emotion of the validation data. The out-of-sample $R ^ { 2 }$ measures the reduction of the mean-square prediction error relative to the average emotion in the in-sample data. If this statistic is greater than $0 ,$ the model performs better than the in-sample average, and a value of 1 corresponds to a perfect accuracy in inferring negative emotion. Table 10 presents the results of the in-sample and out-of-sample $R ^ { 2 }$ . We found outof-sample $R ^ { 2 }$ values between .17 (unknown participants) and .05 (unknown tasks) depending on the definition of the training and validation data. These results show not only that information on cursor distance and speed can explain a relevant share of the variation of emotion in the training data set, but also that mouse cursor data can infer the level of negative emotion.

## Discussion

We introduced a ubiquitous noninvasive method to assess negative emotion: mouse cursor movements. The results of three studies support that negative emotion influences mouse cursor distance and speed (Study 1) and that these mouse characteristics can be used to infer the presence (Study 2) and level (Study 3) of negative emotion. The findings have implications for several research disciplines, including studying the usability of systems in users’ natural environments with finegrained temporal precision; designing affective computing systems capable of perceiving and responding to human emotion; and studying how to improve e-commerce interactions through adapting to users’ emotional states (e.g., website morphing). Below, we further elaborate on the theoretical and practical implications.

## Implications for Research

We contribute to research by theoretically explaining and empirically validating how negative emotion influences mouse cursor movements in goal-directed tasks. First, we extend attentional control theory (ACT) to explain how negative emotion influences mouse cursor distance. ACT explains that negative emotion decreases attentional control (Eysenck et al. 2007), which can cause users to distribute their attention more broadly, rather than primarily focusing on the task at hand. We extend ACT by explaining how this broader distribution of attention will result in deviations from one’s intended mouse cursor movement trajectory, resulting in increased distance as the cursor travels less directly to its intended destination.

Second, we extend ACT by explaining how decreased attentional control will also influence mouse cursor speed. ACT explains that reduced attentional control decreases one’s available working memory and therefore slows reaction times (Eysenck et al. 2007). We extend ACT by explaining how slower reaction time will result in slower mouse cursor speed. Namely, users subconsciously compensate for slower reaction times by slowing movements to allow the brain more time to program needed movement adjustments (Meyer et al. 1990).

These theoretical extensions have potential to extend and contribute to several research disciplines. Some studies, most exploratory in nature, have begun investigating the influence of emotion on mouse cursor movements (e.g., Grimes et al. 2013; Maehr 2008; Salmeron-Majadas et al. 2014; Sun et al. 2014; Zimmermann et al. 2006; Zimmermann et al. 2003). We contribute to this research by theoretically explaining and deriving hypotheses of why negative emotion will influence mouse cursor distance and speed. Further, our research validates that negative emotions influence distance and speed in three different studies, with differing contexts and populations. Thus, our research contributes to the literature by suggesting that distance and speed are robust indicators of emotion in different scenarios.

Second, we respond to calls for utilizing psychophysiological tools that provide new methodological approaches for investigating the development and use of systems (see Dimoka et al. 2012). Namely, our research provides a methodology to aid HCI and usability researchers in assessing negative emotional responses in users’ natural settings. Mouse cursor data can be collected without any additional user action and even unbeknownst to users (via JavaScript embedded in websites). Mouse cursor tracking, therefore, has potential to provide an unobtrusive indicator of emotion in users’ natural settings with fine-grained temporal precision. Further, our research provides a validated method for multimethod research. Mouse cursor tracking is particularly appropriate for a concurrent mixed-method research design—gathering qualitative and quantitative data during the same stage (Venkatesh et al. 2013, Venkatesh et al. 2016)—as mouse cursor movements can be captured as people naturally interact with a computer without interfering with other research data collection activities.

Third, we extend affective computer literature by introducing mouse cursor tracking as a way to assess negative emotion. Affective computing is a research discipline that studies the development of systems and devices that can recognize, interpret, process, and simulate human affect (Picard 2000). Researchers have examined technologies to recognize emotion such as analyzing vocalics and speech (Breazeal and Aryananda 2002), facial expressions (Caridakis et al. 2006), and blood volume pressure (Picard 2000), to name a few. Specialized hardware is typically needed to assess users emotions (for a list of projects, see Tao and Tan 2005). Our research suggests that affective computing researchers could also consider utilizing mouse cursor tracking to infer emotion. Mouse cursor tracking offers several benefits as it does not require attaching sensors to a person’s body, nor does it require the monitoring of the user’s private environment (e.g., using cameras or microphones that record the environment away from the computer).

Fourth, our research sets the foundation for future HCI research to explore (1) how other emotions influence mouse cursor movements and (2) how emotions influence the use of other devices. Although our study was limited to the use of the computer mouse, the theories utilized in this paper apply to motor movements in general, and thus may apply to other devices including touch screens, sketch pads, in-air sensors (e.g., the Microsoft Kinect®), accelerometers, and gyroscopes. Further, some of these devices provide more sophisticated data than mouse-cursor tracking (e.g., z-location, touch pressure, motion data, etc.), and thus may provide more indepth information about emotions. We suggest future research in each of these areas to better understand how emotion influences the use of HCI computer input devices.

Fifth, we provide a methodology for emotion assessment that enables design science research that cannot be easily conducted using traditional assessments. Design science “addresses research through the building and evaluation of artifacts” (Hevner et al. 2004, p. 79). Assessing users’ reactions (e.g., emotion) to artifacts is one type of evaluation. In some situations, however, assessing emotional responses to artifacts using traditional measures can be difficult without biasing the result. For example, when testing a system with live users—a stage of design science research (Nunamaker and Briggs 2011)—it is sometimes not ideal to interrupt the user interaction with a questionnaire. Doing so may annoy the user or yield an ineffective response rate. Likewise, in live interactions, it is often not feasible to attach psychophysiological devices (e.g., facial electromyography electrodes) to the user to observe the emotions as they occur. While such techniques yield valuable information in many situations, they may be invasive and decrease ecological validity in others. Mouse-cursor movement, however, can be monitored noninvasively (and even unbeknownst to users) to infer emotional changes. As such, our research enables researchers to assess emotional reactions during live system use with fine temporal precision. Further, in the many scenarios where traditional measures are appropriate, our research can be used to conduct multimethod emotion research to help validate the results.

Finally, we contribute to e-commerce research, particularly on website morphing (Hauser et al. 2009). Website morphing is a stream of research that suggests that changing a website to meet a user’s specific needs will increase purchase intentions (Hauser et al. 2014; Hauser et al. 2009). Typically, researchers present a pre-survey to participants to assess their preferences, and then morph a website to align it with user preference. A limitation of this approach, however, is that it is not always possible to have all users complete the presurvey. Thus, complementary methodologies are needed to dynamically detect user needs as a basis for morphing websites. Our research helps address this need and thereby can facilitate further research in this area. As one example, our research could help identify users who potentially have computer anxiety (a negative emotion) and morph the website to help alleviate that anxiety—with anxiety being a major deterrent of system use (Beaudry and Pinsonneault 2010).

Our studies are not without limitations. First, they only examined mousing indicators of negative emotion in goaldirected tasks. We have not tested the generalizability of our results in experiential tasks—that is, tasks that are rather unstructured and are primarily motivated by the interaction, not the outcome (Wells et al. 2005). Second, we only explored the influence of negative emotion on two mouse movement statistics: distance and speed. However, other statistics may also indicate negative emotion. Third, we examined the relationships between mouse cursor movements and negative emotion using a relatively narrow age range of participants (mean age between 22 and 34.5 years). Finally, we did not specifically explore how other dimensions of emotion—positive valence, various levels of arousal, and dominance—influence mouse cursor movements.

## Implications for Practice

Analyzing mouse cursor movements to detect negative emotion has several practical implications. First, practitioners can use our methodology for mass-deployable usability testing to examine how different design choices influence users’ negative emotions. For example, using the methodology described in Study 2 or 3, system designers could randomly present users with different versions of a similarly structured webpage (known as A/B testing). Through monitoring mouse cursor movements, system designers could then evaluate if one version of a webpage results in statistically different speed and distance, which may indicate that one version induced relatively greater negative emotion. Based on this analysis, system designers can choose among competing design choices to improve the user experience.

Further, JavaScript can continuously monitor mouse cursor movements over a user’s entire interaction with a website, allowing managers to identify real-life “failure points” in the interaction—that is, specific interaction points that cause a user to leave a site. For example, a website can record the timing of an abnormal increase in distance or decrease in speed for a given webpage. Trends of increased distance and decreased speed across individuals could be identified, possibly indicating that a system component induced a negative reaction. By identifying the time and location of a possible negative emotional reaction, system designers can identify areas in a webpage that may likely need to be redesigned.

Our methodology also helps build a foundation for proactively responding to customers’ negative reactions during website use in real time. Once a negative emotional reaction has been identified through our methodology, a website can take actions to better meet a user’s needs. For instance, an ecommerce site can provide an opportunity for users to express their concerns after experiencing a negative emotional reaction to help “undo some of the negative feeling it [the system] causes” (Klein et al. 2002, p. 119). Providing slightly apologetic statements is also an effective means of responding to negative emotions (Tzeng 2004). Offering compensation (e.g., additional time on a subscription) can mitigate negative encounters (Smith et al. 1999). Further, an explanation or offer for assistance may be an appropriate response to system failures (Kuo et al. 2011). By alleviating negative emotion through these interventions, e-commerce sites can prevent users from prematurely leaving a website before purchasing, spreading negative word of mouth, not disclosing information, or avoiding the site in the future. Ultimately, detecting and responding to negative emotions may be an effective mechanism for improving the profitability of e-commerce companies.

## Conclusion

Detecting negative emotion is important for the design and continual improvement of websites. Drawing on attentional control theory, we explained how negative emotion may influence mouse cursor distance and speed. In three experiments, we demonstrated that both greater cursor distance and slower average cursor speed can indicate negative emotion and that these characteristics can infer negative emotional reactions. Our findings suggest that the analysis of mouse cursor movements may enable researchers to assess negative emotional reactions during live system use, examine emotional reactions with more temporal precision, conduct multimethod emotion research, and provide researchers and system designers with an easy to deploy, but powerful, tool to infer users’ negative emotion to create more unobtrusive affective and adaptive systems.

## Acknowledgments

The work described in this paper was substantially supported by research grants from City University of Hong Kong (Projects No. 7002626 and 7004123) and the Research Grants Council of the Hong Kong Special Administrative Region (Project No. CityU149512). We would like to thank Professors Susanne Robra-Bissantz and David Woisetschläger for valuable comments on initial versions of this manuscript. Further, we would like to thank Munkhsarnai Baatar, Robert Lodahl, and Mathias Reisch for helping with the data collection.

## References

Agarwal, R., and Karahanna, E. 2000. “Time Flies When You’re Having Fun: Cognitive Absorption and Beliefs about Information Technology Usage,” MIS Quarterly (24:4), pp. 665-694.

Agarwal, R., and Venkatesh, V. 2002. “Assessing a Firm’s Web Presence: A Heuristic Evaluation Procedure for the Measurement of Usability,” Information Systems Research (13:2), pp. 168-186.

Anderson, C. L., and Agarwal, R. 2011. “The Digitization of Healthcare: Boundary Risks, Emotion, and Consumer Willingness to Disclose Personal Health Information,” Information Systems Research (22:3), pp. 469-490.

Bagozzi, R. P., Gopinath, M., and Nyer, P. U. 1999. “The Role of Emotions in Marketing,” Journal of the Academy of Marketing Science (27:2), pp. 184-206.

Beaudry, A., and Pinsonneault, A. 2010. “The Other Side of Acceptance: Studying the Direct and Indirect Effects of Emotions on Information Technology Use,” MIS Quarterly (34:4), pp. 689-710.

Berinsky, A. J., Huber, G. A., and Lenz, G. S. 2012. “Evaluating Online Labor Markets for Experimental Research: Amazon.com’s Mechanical Turk,” Political Analysis (20:3), pp. 351-368.

Bishop, S. J., Jenkins, R., and Lawrence, A. D. 2007. “Neural Processing of Fearful Faces: Effects of Anxiety are Gated by Perceptual Capacity Limitations,” Cerebral Cortex (17:7), pp. 1595-1603.

Bradley, M. M., and Lang, P. J. 1994. “Measuring Emotion: The Self-Assessment Manikin and the Semantic Differential,” Journal of Behavior Therapy and Experimental Psychiatry (25:1), pp. 49-59.

Breazeal, C., and Aryananda, L. 2002. “Recognition of Affective Communicative Intent in Robot-Directed Speech,” Autonomous Robots (12:1), pp. 83-104.

Buhrmester, M., Kwang, T., and Gosling, S. D. 2011. “Amazon’s Mechanical Turk: A New Source of Inexpensive, Yet High-Quality, Data?,” Perspectives on Psychological Science (6:1), pp. 3-5.

Campbell, D. I., and Gingrich, K. 1980. “The Interactive Effects of Task Complexity and Participation on Task Performance: A Field Experiment,” Organizational Behavior and Human Decision Processes (38:2), pp. 162-180.

Campbell, J. Y., and Thompson, S. B. 2008. “Predicting Excess Stock Returns Out of Sample: Can Anything Beat the Historical Average?,” Review of Financial Studies (21:4), pp. 1509-1531.

Caridakis, G., Malatesta, L., Kessous, L., Amir, N., Raouzaiou, A., and Karpouzis, K. 2006. “Modeling Naturalistic Affective States Via Facial and Vocal Expressions Recognition,” in Proceedings of the International Conference on Multimodal Interfaces, Banff, Alberta, Canada.

Ceaparu, I., Lazar, J., Bessiere, K., Robinson, J., and Shneiderman, B. 2004. “Determining Causes and Severity of End-User Frustration,” International Journal of Human–Computer Interaction (17:3), pp. 333-356.

Coelho, C. M., Lipp, O. V., Marinovic, W., Wallis, G., and Riek, S. 2010. “Increased Corticospinal Excitability Induced by Unpleasant Visual Stimuli,” Neuroscience Letters (481:3), pp. 135-138.

Compeau, D., Marcolin, B., Kelley, H., and Higgins, C. 2012. “Research Commentary—Generalizability of Information Systems Research Using Student Subjects—A Reflection on Our Practices and Recommendations for Future Research,” Information Systems Research (23:4), pp. 1093-1109.

Coombes, S. A., Gamble, K. M., Cauraugh, J. H., and Janelle, C. M. 2008. “Emotional States Alter Force Control During a Feedback Occluded Motor Task,” Emotion (8:1), pp. 104-113.

Coombes, S. A., Higgins, T., Gamble, K. M., Cauraugh, J. H., and Janelle, C. M. 2009. “Attentional Control Theory: Anxiety, Emotion, and Motor Planning,” Journal of Anxiety Disorders (23:8), pp. 1072-1079.

Coombes, S. A., Naugle, K. M., Barnes, R. T., Cauraugh, J. H., and Janelle, C. M. 2011. “Emotional Reactivity and Force Control: The Influence of Behavioral Inhibition,” Human Movement Science (30:6), pp. 1052-1061.

Coombes, S. A., Tandonnet, C., Fujiyama, H., Janelle, C.M., Cauraugh, J. H., and Summers, J. J. 2009. “Emotion and Motor Preparation: A Transcranial Magnetic Stimulation Study of Corticospinal Motor Tract Excitability,” Cognitive, Affective, & Behavioral Neuroscience (9:4), pp. 380-388.

Deng, L., and Poole, M. S. 2010. “Affect in Web Interfaces: A Study of the Impacts of Web Page Visual Complexity and Order,” MIS Quarterly (34:4), pp. 711-730.

Dimoka, A., Banker, R. D., Benbasat, I., Davis, F. D., Dennis, A. R., Gefen, D., Gupta, A., Ischebeck, A., Kenning, P. H., Pavlou, P.

A., Muller-Putz, G., Riedl, R., vom Brocke, J., and Weber, B. 2012. “On the Use of Neurophysiological Tools in IS Research: Developing a Research Agenda for NeuroIS,” MIS Quarterly (36:3), pp. 679-702.

Eysenck, M. W., and Derakshan, N. 2011. “New Perspectives in Attentional Control Theory,” Personality and Individual Differences (50:7), pp. 955-960.

Eysenck, M. W., Derakshan, N., Santos, R., and Calvo, M. G. 2007. “Anxiety and Cognitive Performance: Attentional Control Theory,” Emotion (7:2), pp. 336-353.

Freeman, J. B., Dale, R., and Farmer, T. A. 2011. “Hand in Motion Reveals Mind in Motion,” Frontiers in Psychology (2:59), pp. 1-6.

Galletta, D. F., Henry, R., McCoy, S., and Polak, P. 2004. “Web Site Delays: How Tolerant are Users?,” Journal of the Association for Information Systems (5:1), Article 1.

Gelbrich, K. 2010. “Anger, Frustration, and Helplessness After Service Failure: Coping Strategies and Effective Informational Support,” Journal of the Academy of Marketing Science (38:5), pp. 567-585.

Google. 2015. “Compatibility Definition Android 6.0,” Google Inc. (https://static.googleusercontent.com/media/source.android. com/en//compatibility/android-cdd.pdf).

Grimes, M., Jenkins, J. L., and Valacich, J. 2013. “Exploring the Effect of Arousal and Valence on Mouse Interaction,” in Proceedings of the 34<sup>th</sup> International Conference on Information Systems, Milan, Italy.

Gross, J. J., and Thompson, R. A. 2007. “Emotion Regulation: Conceptual Foundations,” in Handbook of Emotion Regulation, J. J. Gross (ed.), New York: Guilford Press, pp. 3-24.

Hauser, J. R., Liberali, G., and Urban, G. L. 2014. “Website Morphing 2.0: Switching Costs, Partial Exposure, Random Exit, and When to Morph,” Management Science (60:6), pp. 1594-1616.

Hauser, J. R., Urban, G. L., Liberali, G., and Braun, M. 2009. “Website Morphing,” Marketing Science (28:2), pp. 202-223.

Haywood, K. M. 1989. “Managing Word of Mouth Communications,” Journal of Services Marketing (3:2), pp. 55-67.

Hehman, E., Stolier, R. M., and Freeman, J. B. 2014. “Advanced Mouse-Tracking Analytic Techniques for Enhancing Psychological Science,” Psychological Science (20:10), pp. 1183-1188.

Hevner, A., March, S. T., Park, J., and Ram, S. 2004. “Design Science in Information Systems Research,” MIS Quarterly (28:1), pp. 75-105.

Huang, M.-H. 2003. “Modeling Virtual Exploratory and Shopping Dynamics: An Environmental Psychology Approach,” Information & Management (41:1), pp. 39-47.

Jorgensen, A. H. 1990. “Thinking-Aloud in User Interface Design—A Method Promoting Cognitive Ergonomics,” Ergonomics (33:4), Apr, pp. 501-507.

Kannape, O. A., Barré, A., Aminian, K., and Blanke, O. 2014. “Cognitive Loading Affects Motor Awareness and Movement Kinematics but Not Locomotor Trajectories During Goal-Directed Walking in a Virtual Reality Environment,” PloS One (9:1), pp. 1-11.

Keeker, K. 1997. “Improving Web Site Usability and Appeal” (https://msdn.microsoft.com/en-us/library/c889361(v= office.12).aspx).

Kim, H.-J., and Choi, Y. S. 2012. “Exploring Emotional Preference for Smartphone Applications,” in Proceedings of the Consumer Communications and Networking Conference, IEEE, Las Vegas, NV, pp. 245-249.

Klein, J., Moon, Y., and Picard, R. W. 2002. “This Computer Responds to User Frustration: Theory, Design, and Results,” Interacting with Computers (14:2), pp. 119-140.

Kuo, Y. F., Yen, S. T., and Chen, L. H. 2011. “Online Auction Service Failures in Taiwan: Typologies and Recovery Strategies,” Electronic Commerce Research and Applications (10:2), pp. 183-193.

Lang, P. J., and Bradley, M. M. 2007. “The International Affective Picture System (IAPS) in the Study of Emotion and Attention,” in Handbook of Emotion Elicitation and Assessment, J. A. Coan and J. J. B. Allen (eds.), New York: Oxford University Press, pp. 29-46.

Lazarus, R. S. 1991. “Progress on a Cognitive Motivational Relational Theory of Emotion,” American Psychologist (46:8), pp. 819-834.

Lin, H.-H., and Wang, Y.-S. 2006. “An Examination of the Determinants of Customer Loyalty in Mobile Commerce Contexts,” Information & Management (43:3), pp. 271-282.

Lin, J.-F., Drury, C. G., Chou, C.-M., Lin, Y.-D., and Lin, Y.-Q. 2011. “Measuring Corrective Reaction Time with the Intermittent Illumination Model,” in Human–Computer Interaction: Design and Development Approaches, J. A. Jacko (ed.), New York: Springer, pp. 397-405.

Maehr, W. 2008. eMotion: Estimation of User’s Emotional State by Mouse Motions, Saarbrücken, Germany: VDM Verlag.

Mason, W., and Suri, S. 2012. “Conducting Behavioral Research on Amazon’s Mechanical Turk,” Behavior Research Methods (44:1), pp. 1-23.

Meyer, D. E., Abrams, R. A., Kornblum, S., Wright, C. E., and Smith, J. E. K. 1988. “Optimality in Human Motor Performance: Ideal Control of Rapid Aimed Movements,” Psychological Review (95:3), pp. 340-370.

Meyer, D. E., Smith, J. E. K., Kornblum, S., Abrams, R. A., and Wright, C. E. 1990. “Speed-Accuracy Tradeoffs in Rapid Aimed Movements: Toward a Theory of Rapid Voluntary Action,” in Attention and Performance XIV, M. Jeannerod (ed.), Hillsdale, NJ: Lawrence Erlbaum Associates, pp. 173-226.

Mulpuru, S., Hult, P., Freeman Evans, P., Sehgal, V., and McGowan, B. 2010. “US Online Retail Forecast, 2009 to 2014,” Forrester Research, Cambridge, MA.

Nadkarni, S., and Gupta, R. 2007. “A Task-Based Model of Perceived Website Complexity,” MIS Quarterly (31:2), pp. 501-524.

Naugle, K. M., Coombes, S. A., Cauraugh, J. H., and Janelle, C. M. 2012. “Influence of Emotion on the Control of Low-Level Force Production,” Research Quarterly for Exercise and Sport (83:2), pp. 353-358.

Nunamaker Jr., J. F., and Briggs, R. O. 2011. “Toward a Broader Vision for Information Systems,” ACM Transactions on Management Information Systems (2:4), pp. 1-12.

Pashler, H. 1994. “Dual-Task Interference in Simple Tasks: Data and Theory,” Psychological Bulletin (116:2), pp. 220-244.

Pew Research Center. 2014. “Internet Users in 2014,” Pew Research Center, Washington, DC (http://www.pewinternet.org/ data-trend/internet-use/latest-stats/; accessed July 7, 2014).

Picard, R. W. 2000. Affective Computing, Cambridge, MA: MIT Press.

Russell, J. A., and Mehrabian, A. 1977. “Evidence for a Three-Factor Theory of Emotions,” Journal of Research in Personality (11:3), pp. 273-294.

Salmeron-Majadas, S., Santos, O. C., and Boticario, J. G. 2014. “An Evaluation of Mouse and Keyboard Interaction Indicators Towards Non-Intrusive and Low Cost Affective Modeling in an Educational Context,” Procedia Computer Science (35), pp. 691-700.

Sarter, M., and Paolone, G. 2011. “Deficits in Attentional Control: Cholinergic Mechanisms and Circuitry-Based Treatment Approaches,” Behavioral Neuroscience (125:6), pp. 825-835.

Sheng, H., and Joginapelly, T. 2012. “Effects of Web Atmospheric Cues on Users’ Emotional Responses in E-Commerce,” AIS Transactions on Human–Computer Interaction (4:1), pp. 1-24.

Smith, A. K., Bolton, R. N., and Wagner, J. 1999. “A Model of Customer Satisfaction with Service Encounters Involving Failure and Recovery,” Journal of Marketing Research (36:3), pp. 356-372.

Steelman, Z. R., Hammer, B. I., and Limayem, M. 2014. “Data Collection in the Digital Age: Innovative Alternatives to Student Samples,” MIS Quarterly (38:2), pp. 355-378.

Sun, D., Paredes, P., and Canny, J. 2014. “MouStress: Detecting Stress from Mouse Motion,” in Proceedings of the SICGCHI Conference on Human Factors in Computing Systems, New York: ACM, pp. 61-70.

Sun, H., and Zhang, P. 2006. “The Role of Affect in IS Research: A Critical Survey and a Research Model,” in Human–Computer Interaction and Management Information Systems Foundations, P. Zhang, D. Galletta, and V. Zwass (eds.), New York: M. E. Sharpe, pp. 294-330.

Tanaka, Y., Funase, K., Sekiya, H., and Murayama, T. 2012. “Modulation of Corticospinal Motor Tract Excitability During a Fine Finger Movement under Psychological Pressure: A TMS Study,” International Journal of Sport and Health Science (10:1), pp. 39-49.

Tao, J., and Tan, T. 2005. “Affective Computing: A Review,” in Affective Computing and Intelligent Interaction, J. Tao, T. Tan, and R. W. Picard (eds.), New York: Springer, pp. 981-995.

Tax, S. S., and Brown, S. W. 1998. “Recovering and Learning from Service Failure,” Sloan Management Review (40:1), pp. 75-88.

Tractinsky, N., Cokhavi, A., Kirschenbaum, M., and Sharfi, T. 2006. “Evaluating the Consistency of Immediate Aesthetic Perceptions of Web Pages,” International Journal of Human– Computer Studies (64:11), pp. 1071-1083.

Thorpe, S., Fize, D., and Marlot, C. 1996. “Speed of Processing in the Human Visual System,” Nature (381:6582), pp. 520-522.

Tzeng, J.-Y. 2004. “Toward a More Civilized Design: Studying the Effects of Computers that Apologize,” International Journal of Human–Computer Studies (61:3), pp. 319-345.

Unsworth, N., and Spillers, G. J. 2010. “Working Memory Capacity: Attention Control, Secondary Memory, or Both? A Direct Test of the Dual-Component Model,” Journal of Memory and Language (62:4), pp. 392-406.

van Loon, A. M., van den Wildenberg, W. P., van Stegeren, A. H., Ridderinkhof, K. R., and Hajcak, G. 2010. “Emotional Stimuli Modulate Readiness for Action: A Transcranial Magnetic Stimulation Study,” Cognitive, Affective, & Behavioral Neuroscience (10:2), pp. 174-181.

van Someren, M. W., Barnard, Y. F., and Sandberg, J. A. 1994. The Think Aloud Method: A Practical Guide to Modelling Cognitive Processes, London: Academic Press.

Venkatesh, V., Brown, S. A., and Bala, H. 2013 “Bridging the Qualitative-Quantitative Divide: Guidelines for Conducting Mixed Methods Research in Information Systems,” MIS Quarterly (37:1), pp. 21-54.

Venkatesh, V., Brown, S. A., and Wati, Y. 2016. “Guidelines for Conducting Mixed Methods Research: An Extension and Illustration,” Journal of the Association for Information Systems (17:7), Article 2, pp. 435-494.

Venkatesh, V., and Davis, F. D. 2000. “A Theoretical Extension of the Technology Acceptance Model: Four Longitudinal Field Studies,” Management Science (46:23), pp. 186-204.

Venkatesh, V., Morris, M. G., Davis, G. B., and Davis, F. D. 2003. “User Acceptance of Information Technology: Toward a Unified View,” MIS Quarterly (27:3), 425-478.

Venkatesh, V., and Ramesh, V. 2006. “Web and Wireless Site Usability: Understanding Differences and Modeling Use,” MIS Quarterly (30:1), pp. 181-206.

Venkatesh, V., Ramesh, V., and Massey, A. P. 2003. “Understanding Usability in Mobile Commerce,” Communications of the ACM (46:12), pp. 53-56.

Vine, S. J., and Wilson, M. R. 2011. “The Influence of Quiet Eye Training and Pressure on Attention and Visuo-Motor Control,” Acta Psychologica (136:3), pp. 340-346.

Weinmann, M., Schneider, C., and Robra-Bissantz, S. 2013. “MOUSEREC—Monitoring Online Users’ Emotions by Recording and Evaluating Cursor Movements,” paper presented at the X Conference of the Italian Chapter of AIS: Empowering Society Through Digital Innovations, Milan, Italy.

Wells, J. D., Palmer, J. W., and Fuerst, W. L. 2005. “Designing Consumer Interfaces for Experiential Tasks: An Empirical Investigation,” European Journal of Information Systems (14:3), pp. 273-287.

Welsh, T. N., and Elliott, D. 2004. “Movement Trajectories in the Presence of a Distracting Stimulus: Evidence for a Response Activation Model of Selective Reaching,” The Quarterly Journal of Experimental Psychology Section A (57:6), pp. 1031-1057.

Zhang, P. 2013. “The Affective Response Model: A Theoretical Framework of Affective Concepts and Their Relationships in the ICT Context,” MIS Quarterly (37:1), pp. 247-274.

Zimmermann, P., Gomez, P., Danuser, B., and Schär, S. 2006. “Extending Usability: Putting Affect into the User-Experience,” in User eXperience Towards a Unified View: The 2<sup>nd</sup> COST294- MAUSE International Open Workshop, October 14, NordiCHI’06, Oslo, Norway, pp. 27-32.

Zimmermann, P., Guttormsen, S., Danuser, B., and Gomez, P. 2003. “Affective Computing—A Rationale for Measuring Mood with Mouse and Keyboard,” International Journal of Occupational Safety and Ergonomics (9:4), pp. 539-551.

Zuckerman, M. 1955. “The Effect of Frustration on the Perception of Neutral and Aggressive Words,” Journal of Personality (23:4), pp. 407-422.

## About the Authors

Martin T. Hibbeln is an assistant professor of Finance at the Mercator School of Management, University of Duisburg-Essen, Germany. He graduated with a Ph.D. in Finance from the University of Braunschweig, Germany. His research interests include financial risk management, empirical banking, and individual decision making. His research has been published in various journals, including Journal of Risk and Insurance and Journal of Banking & Finance, and conference proceedings such as the International Conference on Information Systems and the European Conference on Information Systems.

Jeffrey L. Jenkins is an assistant professor of Information Systems at the Marriott School of Management, Brigham Young University. He graduated with a Ph.D. in Management Information Systems from the University of Arizona. His active research includes human-computer interaction and behavioral information security. In a human–computer interaction context, Jeffrey’s research examines how to infer human states using computer input devices such as the computer mouse, keyboard, or touchscreen. His research has been published in various journals and conference proceedings, including Journal of Management Information Systems, Proceedings of the ACM Conference on Human Factors in Computing Systems (CHI), Computers in Human Behavior, and others. Prior to earning his Ph.D., Jeffrey was a software engineer in both the public and private sectors.

Christoph Schneider is an assistant professor in the Department of Information Systems at City University of Hong Kong. He earned a Ph.D. in Information Systems at Washington State University and previously held a visiting faculty appointment at Boise State University. His primary research interests include human–computer interaction, electronic commerce, and computer-mediated collaboration. His research has appeared in peer reviewed journals such as Information Systems Research, MIS Quarterly, and Management Science; further, he has presented his research at various international conferences, including the International Conference on Information Systems, Americas Conference on Information Systems, European Conference on Information Systems, and the Hawaii International Conference on System Sciences. He is a coauthor of the leading textbook Information Systems Today. Christoph serves as a senior editor for Information Systems Journal and as a member of the international steering committee for the International Conference on Information Systems Development.

Joseph (Joe) Valacich is an Eller Professor in the Eller College of Management at the University of Arizona and is a Fellow of the Association for Information Systems (2009). His primary research interests include human–computer interaction, deception detection, cyber security, technology-mediated collaboration, individual and group decision making, mobile and emerging technologies, and ebusiness. He has published more than 200 scholarly articles in numerous prestigious journals and conferences. In 2011 he received the best paper award from AIS Transactions on Human–Computer Interaction; in 2009 he received the best paper award from MIS Quarterly, and is currently ranked as one of MIS Quarterly’s “prolific authors.” Over his career, he has earned numerous awards for outstanding research, teaching, and service. He is also a coauthor of several leading textbooks.

Markus Weinmann is an assistant professor in the Department of Information Systems at the University of Liechtenstein. He earned a Ph.D. in Business Information Systems at the University of Braunschweig, Germany. His primary research interests include human– computer interaction, electronic commerce, applied behavioral economics, and individual decision making. In particular, his research examines how user interface design influences individual decision making. Markus presented his research at various international conferences, including the International Conference on Information Systems, the Americas Conference on Information Systems, and the European Conference on Information Systems.

# HOW IS YOUR USER FEELING? INFERRING EMOTION THROUGH HUMAN–COMPUTER INTERACTION DEVICES

Martin Hibbeln Mercator School of Management, University of Duisburg-Essen, Lotharstrasse 65, 47057 Duisburg, GERMANY {martin.hibbeln@uni-due.de}

Jeffrey L. Jenkins Information Systems Department, Brigham Young University, 790 TNRB, Provo, UT 84602 U.S.A. {jjenkins@byu.edu}

Christoph Schneider Department of Information Systems, City University of Hong Kong, Tat Chee Avenue, Kowloon, HONG KONG {christoph.schneider@cityu.edu.hk}

Joseph S. Valacich Management Information Systems, University of Arizona, McClelland Hall Room 430CC, Tucson, AZ 85721 U.S.A. {valacich@arizona.edu}

Information Systems Department, University of Liechtenstein, Fürst-Franz-Josef-Strasse, 9490 Vaduz, LIECHTENSTEIN {markus.weimann@uni.li}

## Appendix A

## Supplemental Page-Level Analysis for Study 2

We conducted an ANOVA to test the hypothesized relationships between negative emotion and mouse cursor movements across the different pages of the website in Study 2. Because no manipulation was made prior to the first page of the website, the mousing behavior should hypothetically be the same between condition groups on this page. However, because we manipulated frustration before users interacted with pages 2, 3, and 4, according to our hypotheses, the mousing behavior should be different on these pages. We present the results in Table A1. As expected, since the manipulation did not precede page 1, both mouse cursor distance and speed were not significantly different between the two conditions. However, as the negative emotion manipulation did precede pages 2, 3, and 4, participants in the negative-emotion treatment group exhibited greater distance and slower speed than did participants in the control group.

<table><tr><td rowspan="2" colspan="2">Manipulation</td><td>Page 1</td><td>Page 2</td><td>Page 3</td><td>Page 4</td></tr><tr><td>None</td><td>Frustration manipulated before interaction</td><td>Frustration manipulated before interaction</td><td>Frustration manipulated before interaction</td></tr><tr><td rowspan="2">Group 1: Baseline</td><td>Distance (px)</td><td>M = 15,315.742SD = 9,246.630</td><td>M = 6,033.361SD = 2,827.731</td><td>M = 5,212.737SD = 3,563.427</td><td>M = 8,374.849SD = 4,483.745</td></tr><tr><td>Speed (px/ms)</td><td>M = .167SD = .076</td><td>M = .161SD = .072</td><td>M = .109SD = .059</td><td>M = .248SD = .132</td></tr><tr><td rowspan="2">Group 2: Negative-Emotion</td><td>Distance (px)</td><td>M = 15,918.603SD = 9,038.885</td><td>M = 10,673.614SD = 9,468.696</td><td>M = 12,163.959SD = 14,607.910</td><td>M = 13,472.933SD = 9,294.143</td></tr><tr><td>Speed (px/ms)</td><td>M = .168SD = .070</td><td>M = .116SD = .053</td><td>M = .076SD = .040</td><td>M = .167SD = .075</td></tr><tr><td colspan="2">Distance F-Test</td><td>F(1,124) = .137p &gt; .05</td><td>F(1,124) = 13.703p &lt; .001</td><td>F(1,124) = 13.271p &lt; .001</td><td>F(1,124) = 15.220p &lt; .001</td></tr><tr><td colspan="2">Speed F-Test</td><td>F(1,124) = .940p &gt; .05</td><td>F(1,124) = 16.393p &lt; .001</td><td>F(1,124) = 13.203p &lt; .001</td><td>F(1,124) = 17.981p &lt; .001</td></tr></table>

## Appendix B

## Supplementary Material for Study 3: Website Screenshots (Examples)

![](/api/attachments/GQHDJAP4/fulltext/images/ded18fc9b2ff608b21877c31f900c8dc2eeb904670ab5a6aa6c80aa9f3d3f84d.jpg)  
Figure B1. Laptop Configurator (http://www/dell.com)

![](/api/attachments/GQHDJAP4/fulltext/images/c5fda0f4ea5a999bd4d4535aaf05fde613235c7200f44c937a1078daf7c1ad5d.jpg)  
Figure B2. Vehicle Configurator (http://volkswagen.co.uk)

## Appendix C

## Supplementary Material for Study 3: List of Tasks

## Dell (Website: http://www.dell.com)

Task 1 (Maximum allotted time: 3 min): You want to buy a new laptop computer and you already know the specifications which should be included: The display size should be 15–16 inches, it should run Microsoft Windows 7, the weight should be 5–7 lbs., the processor should be an Intel Core i5 and the price should be between US\$500 and US\$800. Use the configurator to discover which models come into consideration.

Task 2 (3 min): Choose one of the models. You love to chat with your friends, and that’s why you want to have a webcam included. Scan the models’ specifications to see whether there is a webcam included or not. It should have at least 1 megapixel. You think the i5 processor is too slow so you have decided to choose an Intel Core i7 with at least 1.7 GHz, instead of the i5. Please check whether this processor is available for your model or not. In case it is available, please select it.

Task 3 (2 min): Now you would like to have security software for your new laptop. Choose one and add it to your shopping cart.

Task 4 (2 min): You decide to invest in a 3-year customer care service. Search and add one of the service plans.

Task 5 (2 min): Finish your configuration. Ensure that you haven’t made any mistakes during the configuration process and fix any mistakes you may have made.

## Volkswagen (Website: http://volkswagen.co.uk)

Task 1 (3 min): You want to buy a new car but you are not really sure about the specifications. Your dream car should have at least 150 PS. It’s important for you that your car is efficient and environmentally friendly. That’s why the fuel consumption should be at least 60 miles/gallon (MPG) and the CO2 emissions at most 110g/km. The price should be in a range from £20,000 to £30,000. Use the configurator to discover which models come into consideration.

Task 2 (3 min): Choose one of the models. There are different variations of the cars. Please choose a car with at least 150 PS. Moreover, you want to have a car with 5 doors.

Task 3 (2 min): After you have chosen the engine, you would like to have 17 inch tires. The color of your car should be “Reflex Silver Metallic.” The interior upholstery (the seats) can be in a color you like best.

Task 4 (2 min): You love your iPod and it’s time to choose some additional extras. You would like to hear your music in your car as well. Please search for an iPod interface and add it.

Task 5 (2 min): Finish your configuration. Now it’s time to have a look at the financing of the car. Try to figure out your monthly rate if you finance your car for 36 months.

## Appendix D

# Supplementary Material for Study 3: Additional Statistical Analyses and Robustness Checks

## Model Specification

As discussed in the “Model Specification” section of Study 3, our main specification is a fixed-effects regression model of emotions on a set of mouse cursor movement data:

$$
\begin{array}{c} \text {emotions} _ {i t} = \alpha_ {i} + \beta_ {1} \cdot \text {cursor distance} _ {i t} + \beta_ {2} \cdot \text {cursor speed} _ {i t} \\ + \gamma^ {\prime} \cdot \text {additional mouse variables} _ {i t} + \lambda_ {t} + \varepsilon_ {i t} \end{array}\tag{1}
$$

where i indexes the individuals, t the task number, $\lambda _ { t }$ represents task-specific effects, and additional mouse $\nu a r i a b l e s _ { i t }$ contains left clicks, middle/right clicks, and scrolls.

However, if the unobserved differences across individuals are random,<sup>1</sup> estimates from the random effects model are not only consistent but also more efficient than fixed-effects estimates (Wooldridge 2010). Thus, our second specification is a random effects model:

$$
\begin{array}{c} \text {emotions} _ {i t} = \alpha_ {i} + \beta_ {1} \cdot \text {cursor distance} _ {i t} + \beta_ {2} \cdot \text {cursor speed} _ {i t} \\ + \gamma^ {\prime} \cdot \text {additional mouse variables} _ {i t} + \delta^ {\prime} \cdot \text {control variables} _ {i} + \lambda_ {t} + \varepsilon_ {i t} \end{array}\tag{2}
$$

where $a _ { i }$ and $\varepsilon _ { i t }$ are assumed to be independently and identically distributed, and $a _ { i }$ has expectation α and variance $\sigma _ { a } ^ { 2 } .$ In this specification, we additionally consider the control variables age, gender, and country, as well as configurator and configurator experience.

For comparison of the results, we also apply a pooled regression model of the following form:

$$
\begin{array}{c} \text {emotions} _ {i t} = \alpha + \beta_ {1} \cdot \text {cursor distance} _ {i t} + \beta_ {2} \cdot \text {cursor speed} _ {i t} \\ + \gamma^ {\prime} \cdot \text {additional mouse variables} _ {i t} + \delta^ {\prime} \cdot \text {control variables} _ {i} + \lambda_ {t} + \varepsilon_ {i t} \end{array}\tag{3}
$$

Given our use of two very different product configuration systems, there may be differences in the means of the mouse variables between the two configuration systems. Such differences could be a result of differences in website design (for example, in contrast to Volkswagen’s site, Dell’s product configurator required vertical scrolling) and are not necessarily related to different emotions. Thus, in order to account for different slopes of the mouse variables across configurators, we analyze additional specifications for the fixed-effects, random-effects, and pooled-regression model, adding interactions terms between the assigned configurator and the different mouse variables.

## Results

Table D1 presents a summary of the descriptive statistics of the variables captured in the study, and Table D2 presents the regression results using the pleasure scale of SAM. Models 1–2 of Table D2 are estimates based on fixed-effects specification (see equation 1), while model 3–4 and 5–6 refer to the random-effects specification (see equation 2) and the pooled regressions<sup>2</sup> (see equation 3), respectively. Consistent with our hypotheses, the coefficient of cursor distance was significantly positive across all models $( p < . 0 0 1 )$ . Moreover, the coefficient of the average cursor speed was significantly negative. This result was very robust to the model specification with at least p < .05 across all models. This provides evidence that greater cursor distance and lower cursor speed indicate negative emotion.

<sup>1</sup>An effect is said to be random if the study contains only a random sample of possible conditions (Field and Field 2013, p. 862). For example, the variable “product configurator” could be considered as random, as we could have used other systems or even more than two configuration systems.

Summing up the results, we found that the variation of the coefficients of interest was rather low across the models; the coefficients for cursor distance were between .126 and .132, and the respective coefficients for cursor speed varied between -10.30 and -8.08 for the models without interaction effects and between .140 and .155 for the models with interaction effects. This suggests that the results were highly robust to different model specifications.

<table><tr><td colspan="7">Table D1. Study Variable Descriptive Statistics</td></tr><tr><td colspan="7">Panel A. Dell Configurator</td></tr><tr><td></td><td>Obs.</td><td>Mean</td><td>Median</td><td>Std. Dev.</td><td>Min.</td><td>Max.</td></tr><tr><td>Independent Variables</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Distance (px)</td><td>200</td><td>12,602</td><td>11,588</td><td>7,989</td><td>276</td><td>49,205</td></tr><tr><td>Speed (px/ms)</td><td>200</td><td>.137</td><td>.12</td><td>.06</td><td>.04</td><td>.39</td></tr><tr><td>Left clicks</td><td>200</td><td>10.94</td><td>9</td><td>7.33</td><td>0</td><td>48</td></tr><tr><td>Middle/right clicks</td><td>200</td><td>.08</td><td>0</td><td>.46</td><td>0</td><td>5</td></tr><tr><td>Scrolls</td><td>200</td><td>46.21</td><td>30</td><td>48.85</td><td>0</td><td>251</td></tr><tr><td>Dependent Variable</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SAM Pleasure</td><td>200</td><td>4.33</td><td>4</td><td>2.28</td><td>1</td><td>9</td></tr><tr><td colspan="7">Panel B. Volkswagen Configurator</td></tr><tr><td></td><td>Obs.</td><td>Mean</td><td>Median</td><td>Std. Dev.</td><td>Min.</td><td>Max.</td></tr><tr><td>Independent Variables</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Distance (px)</td><td>200</td><td>12,864</td><td>11,516</td><td>7,515</td><td>1,437</td><td>40,217</td></tr><tr><td>Speed (px/ms)</td><td>200</td><td>.12</td><td>.12</td><td>.05</td><td>.02</td><td>.27</td></tr><tr><td>Left clicks</td><td>200</td><td>17.49</td><td>14</td><td>13.00</td><td>0</td><td>79</td></tr><tr><td>Middle/right clicks</td><td>200</td><td>.02</td><td>0</td><td>.14</td><td>0</td><td>1</td></tr><tr><td>Scrolls</td><td>200</td><td>5.86</td><td>0</td><td>13.37</td><td>0</td><td>108</td></tr><tr><td>Dependent Variable</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SAM Pleasure</td><td>200</td><td>4.31</td><td>5</td><td>2.19</td><td>1</td><td>9</td></tr></table>

Table D2. Regression Results Using the Pleasure Scale of SAM

<table><tr><td></td><td colspan="2">Fixed-Effects Model</td><td colspan="2">Random-Effects Model</td><td colspan="2">Pooled-Regression Model</td></tr><tr><td></td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td></tr><tr><td>Distance (px in &#x27;000)</td><td>.132***(.031)</td><td>.140***(.039)</td><td>.130***(.025)</td><td>.149***(.030)</td><td>.126***(.023)</td><td>.155***(.026)</td></tr><tr><td>Speed (px/ms)</td><td>-10.300**(3.649)</td><td>-9.029*(4.312)</td><td>-9.185***(2.658)</td><td>-9.468***(2.811)</td><td>-8.076***(2.301)</td><td>-9.949***(2.528)</td></tr><tr><td>Left clicks</td><td>-.009(.011)</td><td>-.011(.022)</td><td>-.013(.011)</td><td>-.023(.018)</td><td>-.019(.012)</td><td>-.036†(.019)</td></tr><tr><td>Middle/right clicks</td><td>.327(.241)</td><td>.257(.242)</td><td>.358(.235)</td><td>.233(.211)</td><td>.410(.281)</td><td>.231(.210)</td></tr><tr><td>Scrolls</td><td>.002(.004)</td><td>-.002(.004)</td><td>.003(.004)</td><td>-.001(.004)</td><td>.005(.004)</td><td>-.000(.004)</td></tr><tr><td>Configurator × Distance</td><td></td><td>-.016(.054)</td><td></td><td>-.042(.046)</td><td></td><td>-.074(.045)</td></tr><tr><td>Configurator × Speed</td><td></td><td>-2.567(6.478)</td><td></td><td>1.049(5.506)</td><td></td><td>5.593(5.582)</td></tr><tr><td>Configurator × Left clicks</td><td></td><td>.010(.026)</td><td></td><td>.020(.024)</td><td></td><td>.031(.025)</td></tr><tr><td>Configurator × Middle/right clicks</td><td></td><td>.654(1.042)</td><td></td><td>1.199(.930)</td><td></td><td>1.883*(.908)</td></tr><tr><td>Configurator × Scrolls</td><td></td><td>.035***(.009)</td><td></td><td>.037***(.008)</td><td></td><td>.040***(.008)</td></tr><tr><td>Internet usage</td><td></td><td></td><td>-.011(.007)</td><td>-.011(.007)</td><td>-.011(.007)</td><td>-.011(.007)</td></tr><tr><td>Configurator experience</td><td></td><td></td><td>.195(.356)</td><td>.221(.356)</td><td>.196(.350)</td><td>.240(.344)</td></tr><tr><td>Configurator = Volkswagen</td><td></td><td></td><td>-.063(.304)</td><td>-.354(.618)</td><td>.075(.305)</td><td>-.598(.686)</td></tr><tr><td>Country = Germany</td><td></td><td></td><td>.159(.374)</td><td>.146(.372)</td><td>.155(.374)</td><td>.155(.367)</td></tr><tr><td>Gender = Men</td><td></td><td></td><td>-.226(.323)</td><td>-.188(.320)</td><td>-.243(.318)</td><td>-.210(.316)</td></tr><tr><td>Age</td><td></td><td></td><td>.079†(.045)</td><td>.083†(.045)</td><td>.081†(.046)</td><td>.081†(.044)</td></tr><tr><td>Intercept</td><td>3.594***(.330)</td><td>3.510***(.321)</td><td>1.881†(1.043)</td><td>1.878†(1.128)</td><td>1.708(1.094)</td><td>2.021†(1.133)</td></tr><tr><td>Task dummies</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td></tr><tr><td>Individual effects</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>NO</td><td>NO</td></tr><tr><td>Observations</td><td>400</td><td>400</td><td>400</td><td>400</td><td>400</td><td>400</td></tr><tr><td> $R^2$ </td><td>.192a</td><td>.221a</td><td>.202</td><td>.229</td><td>.205</td><td>.234</td></tr><tr><td>Adj.  $R^2$ </td><td>.174a</td><td>.192a</td><td>.171</td><td>.189</td><td>.173</td><td>.194</td></tr></table>

Notes: <sup>†</sup>p < .1, \*p < .05, \*\*p < .01, \*\*\*p < .001. Standard errors clustered by individuals are in parentheses. <sup>a</sup>The R²/adj. R² for the fixed-effects regressions are within-R², excluding the individual effects. The R²/adj. R² including the individual effects are .532/.400 (Model 1) and .549/.411 (Model 2).

## References

Chow, G. 1960. “Tests of Equality Between Sets of Coefficients in Two Linear Regressions,” Econometrica (28:3), pp. 591-605. Field, A. J. M., and Field, Z. 2013. Discovering Stastistics Using R, London: SAGE Publications. Wooldridge, J. M. 2010. Econometric Analysis of Cross Section and Panel Data (2<sup>nd</sup> ed.), Cambridge, MA: MIT Press.
