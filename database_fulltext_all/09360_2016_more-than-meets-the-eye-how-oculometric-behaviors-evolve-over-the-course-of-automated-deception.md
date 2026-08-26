---
otero_id: 9360
otero_key: "25NCYZ4A"
title: "More Than Meets the Eye: How Oculometric Behaviors Evolve Over the Course of Automated Deception Detection Interactions"
authors: "Jeffrey G. Proudfoot; Jeffrey L. Jenkins; Judee K. Burgoon; Jay F. Nunamaker"
year: "2016"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2016.1205929"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# More Than Meets the Eye: How Oculometric Behaviors Evolve Over the Course of Automated Deception Detection Interactions

Jeffrey G. Proudfoot, Jeffrey L. Jenkins, Judee K. Burgoon & Jay F. Nunamaker Jr.

To cite this article: Jeffrey G. Proudfoot, Jeffrey L. Jenkins, Judee K. Burgoon & Jay F. Nunamaker Jr. (2016) More Than Meets the Eye: How Oculometric Behaviors Evolve Over the Course of Automated Deception Detection Interactions, Journal of Management Information Systems, 33:2, 332-360, DOI: 10.1080/07421222.2016.1205929

To link to this article: http://dx.doi.org/10.1080/07421222.2016.1205929

![](/api/attachments/25NCYZ4A/fulltext/images/0d75952ad607cf58cf03e2808ae41764e1365bd48f08090dc2f3135524254716.jpg)

Published online: 05 Oct 2016.

![](/api/attachments/25NCYZ4A/fulltext/images/671a48702d35684eacf94eab935131767378083893c14da2d09b7494f5bea57c.jpg)

Submit your article to this journal

![](/api/attachments/25NCYZ4A/fulltext/images/572c13d2e2a045ce6c4b0eea9d7937f34427951715644d69f871549cd5e339d4.jpg)

Article views: 10

![](/api/attachments/25NCYZ4A/fulltext/images/d17300a5b7691e3bb4c3163c33f6e2a045efa378359e7431628bb3045991b5a7.jpg)

View related articles

![](/api/attachments/25NCYZ4A/fulltext/images/ca185cf4dc912265f8101a6be25b83efeb6fbbbd5ec532a7432ae83bbcd64b6e.jpg)

View Crossmark data

# More Than Meets the Eye: How Oculometric Behaviors Evolve Over the Course of Automated Deception Detection Interactions

JEFFREY G. PROUDFOOT, JEFFREY L. JENKINS, JUDEE K. BURGOON, AND JAY F. NUNAMAKER, JR.

JEFFREY G. PROUDFOOT (jproudfoot@bentley.edu; corresponding author) is an assistant professor in the Information and Process Management Department at Bentley University. He completed his Ph.D. in management information systems at the University of Arizona. His research centers on information security and privacy with emphases on automated credibility assessment and insider threat detection. His work has been published or is forthcoming in the Journal of Management Information Systems, Decision Support Systems, and Computers and Security, among other journals. He has been principal investigator on or contributed to grants from the Department of Homeland Security, and the National Science Foundation, among others.

JEFFREY L. JENKINS (jeffrey\_jenkins@byu.edu) is an assistant professor of information systems in the Marriott School of Management, Brigham Young University. He received his Ph.D. in management information systems from the University of Arizona. His research focuses on human–computer interaction and behavioral information security. His work has been published in Information Systems Research, Journal of Management Information Systems, and MIS Quarterly, among others.

JUDEE K. BURGOON (jburgoon@cmi.arizona.edu) is a professor of communication, family studies, and human development at the University of Arizona, where she is director of research for the Center for the Management of Information, and site director for the Center for Identification Technology Research, a National Science Foundation Industry/ University Cooperative Research Center. She has authored or edited 14 books and monographs and over 300 articles, chapters, and reviews related to nonverbal and verbal communication, interpersonal deception, and computer-mediated communication. Her current program of research centers on developing tools and methods for automated detection of deception and has been funded by the National Science Foundation, Department of Defense, and Department of Homeland Security, among others. She has received numerous awards and has been identified as the most prolific female scholar in the field of communication in the twentieth century.

JAY F. NUNAMAKER, JR. (jnunamaker@cmi.arizona.edu) is a Regents and Soldwedel Professor of MIS, Computer Science and Communication at the University of Arizona. He is director of the Center for the Management of Information and the National Center for Border Security and Immigration. He received his Ph.D. in operations research and systems engineering from Case Institute of Technology. He obtained his professional engineer’s license in 1965. He specializes in the fields of system analysis and design, collaboration technology, and deception detection. He has been inducted into the Design Science Hall of Fame and received the LEO Award for Lifetime Achievement from the Association of Information Systems. He has published over 368 journal articles, book chapters, books, and refereed proceedings papers. He has also cofounded five spin-off companies based on his research.

ABSTRACT: Eye-tracking technology has exhibited promise for identifying deception in automated screening systems. Prior deception research using eye trackers has focused on the detection and interpretation of brief oculometric variations in response to stimuli (e.g., specific images or interview questions). However, more research is needed to understand how variations in oculometric behaviors evolve over the course of an interaction with a deception detection system. Using latent growth curve modeling, we tested hypotheses explaining how two oculometric behaviors—pupil dilation and eye-gaze fixation patterns—evolve over the course of a system interaction for three groups of participants: deceivers who see relevant stimuli (i.e., stimuli pertinent to their deception), deceivers who do not see relevant stimuli, and truth-tellers. The results indicate that the oculometric indicators of deceivers evolve differently over the course of an interaction, and that these trends are indicative of deception regardless of whether relevant stimuli are shown.

KEY WORDS AND PHRASES: automated screening systems, concealed information test (CIT), deception detection, eye tracking, latent growth curve modeling, pupil dilation, oculometrics.

Deception is a pervasive human behavior [93], often leading to adverse consequences for individuals, organizations, and society (e.g., successful phishing attacks can cost companies millions of dollars per year [115]). Detecting deception, however, is typically very difficult [8, 29]. People have limited time and cognitive resources available to make decisions [94] and, consequently, a limited ability to process information when making veracity judgments. Despite extensive training [35, 66, 108], laypeople and professionals (e.g., law enforcement personnel) are often incapable of processing enough reliable indicators to accurately and consistently detect deception. As a result, people detect deception with an average accuracy rate only slightly better than chance [8]. The need to improve deception detection, therefore, is urgent for individuals and organizations. To help address this pressing need, prevailing research has explored how information systems can be used to aid humans in identifying deception with greater accuracy and efficiency [66, 80, 102, 120].

Scholars have explored a number of information systems topics related to automated deception detection, including user interfaces, intelligent agents, sensors, data management, organizational impacts [80], structured interviewing, and noninvasive measurement [103], among others (see also [17, 29, 43, 101, 102, 119]). A common thread linking these studies is the identification of reliable deception indicators and the evaluation of sensors that can accurately measure these indicators. Eye-tracking devices are particularly useful for deception detection systems for several reasons: (1) The devices do not require direct physical contact to collect data, (2) they can be calibrated without the need for human intervention, (3) they are feasible for widespread use in a variety of environments due to advances in mobile technologies [15], (4) they can be used to covertly collect data, and (5) they support the use of interaction formats shorter in duration than traditional deception detection tests (e.g., see [68, 69]). Most critically, this research has suggested that when individuals are being deceptive about their knowledge of a prohibited activity, significant differences in oculometrics—the measurement of eye behaviors—occur compared to those unaware of the activity. For example, deceivers exhibit different eye-gaze fixation patterns [22, 92, 103, 105] and pupil dilation variations [9, 22, 105, 113] relative to truth-tellers. However, the measurement of these indicators traditionally focuses on brief phasic variations that occur in response to the presentation of a specific stimulus (e.g., an interview question or an image).

Many deception indicators, such as pupil dilation, are nonstrategic behaviors— behaviors that inadvertently leak out as a result of the cognitive changes or arousal that can occur when a person deceives [13, 20, 82, 95]. Nonstrategic behaviors associated with deception evolve throughout an interaction. For example, the propensity for a person to display nonstrategic behaviors changes with perceived suspicion and the passing of time [14]. Conversely, some behaviors, including eye-gaze fixations, are more easily controlled and can be considered strategic behaviors. Prior research supports the contention that deceivers often strategically manipulate their behavior in an effort to appear innocent and avoid detection [14, 84].

Understanding how strategic and nonstrategic oculometric indicators of deception evolve over the administration of an automated deception detection interaction has implications for improving the interpretation of eye-tracking results and thus the effectiveness of deception detection systems. However, extant research has not considered how oculometric indicators of deception systematically change over the course of an automated deception detection interaction, especially when deceivers are not presented with relevant stimuli—stimuli pertinent to the deceivers’ deception

—during an interaction. Greater understanding is needed about how oculometric behaviors evolve over the course of a system interaction to improve the accuracy of deception detection systems equipped with eye trackers.

We address this gap by exploring how eye-gaze fixations and pupil dilation change during an automated concealed information test (CIT)—a scientifically validated type of deception test [6, 21, 117]—administered using a deception detection system. We explore the following research question: How do pupil dilation and eye-gaze fixations change over the administration of an automated deception detection interaction for truth-tellers versus deceivers who see relevant or nonrelevant stimuli? In this study, we first summarize relevant literature and specify hypotheses about how pupil dilation and eye-gaze fixations evolve over the duration of an automated deception detection interaction. We then test the hypotheses using a mock crime experiment. The results indicate that eye-gaze fixations and pupil dilation evolve based on a person’s deceptive intent and exposure to relevant stimuli during an interaction. Theoretical and practical implications of these results include the following: (1) the identification of evolving oculometric patterns that may be used as new indicators of deception in automated screening systems, (2) a better understanding of how oculometrics (i.e., eye-gaze fixation patterns and pupil dilation) evolve over the duration of an automated deception detection interaction, and (3) evidence that oculometric behaviors can vary between truth-tellers and deceivers even if relevant stimuli are not shown.

## Relevant Literature and Background

The measurement of oculometric behaviors has been used to conduct research in a variety of information systems contexts and applications. For example, eye trackers have been used in decision-support systems [100], neuro information systems (NeuroIS) [33, 73], website development [24, 34, 111], online marketplaces [116], online advertising [72], and decision-making tasks [27, 70], to name a few. Within the information systems literature, eye trackers have also been used to develop automated deception detection systems. For example, eye trackers have been used in automated systems to detect deception at border crossings [30], test for concealed information [85, 101, 103], and assess familiarity with illicit objects [31]. These systems often take the form of kiosks [32, 37] that integrate multiple sensors [103]. Furthermore, just as there is an extensive set of applications for eye-tracking research, there is also a broad range of ocular features that can be evaluated, such as eye blinks [11, 42, 71], eye-gaze fixations [27, 70, 73, 116], saccades [85, 103, 109], pupil dilation [9, 64, 74], and smooth-pursuit eye movements [7].

The focus of this research is further exploration of pupil dilation, and eye-gaze fixation patterns specifically. Our feature selection was based on the robustness and promising nature of prior pupil dilation and eye-gaze fixation findings within the context of deception detection research [10, 64, 74, 85, 103, 105]. Pupil dilation is influenced by cognitive changes that occur when a person deceives [13,22], including vigilance, increased memory recall, familiarity, and the emotional responses associated with deception. For instance, pupil dilation is positively associated with memory retrieval [5, 46, 54, 63] and anxiety [95], two frequent correlates of deception.

Pupil dilation variations have also long been linked to the fight-or-flight response [20]: a reaction triggered in the sympathetic nervous system in response to a threatening stimulus (in this context, a system conducting a veracity assessment). In addition, pupil dilation is associated with novelty [54, 77] and the orienting response [9], both of which result from seeing a relevant (i.e., personally significant) stimulus among other, nonrelevant stimuli [19, 47, 81, 97]. Researchers have therefore successfully used pupil dilation to detect deception [10, 64, 74, 82] even when the deceiver tries to avoid detection [105]. Furthermore, research evaluating pupil dilation within the context of polygraph examinations found it to be a significant predictor of deception (and reported the correlation of pupil dilation with deception to be comparable to electrodermal activity) [113]. Importantly, this nonstrategic behavior is not static during an interaction; instead, the behavior changes with the passing of time and the level of suspicion people perceive to be directed at them [14].

Additionally, the interpretation of eye-gaze fixations has long been researched for a variety of applications, including the recognition of familiarity [2, 39, 52, 89]) and deception [3, 22, 40, 112]. For example, Cook et al. [22] evaluated the use of reading fixation patterns to identify deception in a screening context and reported that deceivers exhibited shorter periods of fixating on, reading, and rereading deceptive statements relative to truth-tellers. In other work, Schwedes and Wentura [92] conducted a CIT-based study in which deceptive participants were found to fixate longer on familiar faces even though the participants had been directed to conceal their knowledge of these faces.

In a different approach, Derrick et al. [32] tested the feasibility of using manipulated photos to identify deception. In this study, participants constructed a mock improvised explosive device (IED) and then attempted to conceal this fact during an automated screening interview. During the automated screening, all participants were shown an altered image of the IED. The results indicated that the participants who constructed the IED fixated longer on the altered portion of the image than the participants in the control group. Conversely, other studies have shown that participants try to divert their eye gaze from relevant stimuli and often focus on the center of the screen to reduce suspicion [37, 85, 103]. As deceivers engaged in veracity assessments have a propensity to avoid detection through the use of strategic behaviors [58, 59, 60, 61] (as often occurs during polygraph interviews), this oculometric avoidance tactic is of particular interest to, and has consequences for, the present research.

Despite these contributions, researchers have not examined how pupil dilation and eye-gaze fixation patterns evolve during an automated deception detection interaction. To address this gap, we explore how pupil dilation and eye-gaze fixation patterns evolved during an automated CIT-based deception detection interaction. The CIT is a recognition-based criminal-interviewing test designed to identify deception by presenting a combination of crime-relevant stimuli (also called target items) and nonrelevant stimuli (also called nontarget items) to an interviewee. In a traditional CIT, one relevant stimulus is randomly presented within a group of four to six nonrelevant stimuli; this grouping is referred to as a foil. An increase in response variation (e.g., electrodermal activity) when an interviewee is presented with a relevant stimulus, compared to nonrelevant stimuli in the same foil, may indicate recognition of the relevant stimulus and, therefore, deception [69, 75]. Interviewers typically present multiple foils during the course of a CIT. If a person repeatedly exhibits a higher response variation to relevant stimuli compared to nonrelevant stimuli over multiple foils, then these results provide greater confidence that the individual is being deceptive.

Prior research has effectively optimized the CIT to an eye-tracking context by presenting stimuli simultaneously, as opposed to serially [85, 102, 103, 105]. In this format, four stimuli are presented at the same time on a screen, one in each quadrant of a slide (refer to the methodology section to view example slides). This format permits the evaluation of unique eye-tracking indicators in automated deception detection interactions, including the measurement of eye-gaze dwell times on each of the four images, eye-gaze fixation patterns as a person views each of the images (sometimes repeatedly), attempts to avoid looking at one or more of the images, and variations in pupil dilation as each of the four images is viewed. Measurement of each of these indicators would not be possible if only a single stimulus is presented at a time, as is done in traditional CITs [102, 103, 105].

## Theory and Hypotheses

In this section, we hypothesize how pupil dilation and eye-gaze fixation patterns will initially compare across three groups: (1) deceivers who see relevant stimuli, (2) deceivers who do not see relevant stimuli, and (3) truth-tellers (i.e., the control group). We then hypothesize how these oculometric behaviors will evolve over the course of an automated deception detection interaction. First, we predict that deceivers will initially have greater pupil dilation than truth-tellers at the beginning of the interaction. Being subjected to any form of veracity assessment can be threatening; it insinuates that the screener holds the subject in suspicion, regardless of his or her truthfulness or deceptive intent. Actual or perceived suspicion leads people to (1) increase strategic behaviors to enhance their credibility and (2) attempt to decrease nonstrategic behaviors indicative of arousal, cognitive difficulty, or fear [14, 90, 91, 114].

Although all people are likely to experience some degree of anxiety when their veracity is called into question, we posit that deceivers will initially experience greater anxiety than truth-tellers based on the conditioned-response theory and conflict theory (see [13]). Conditioned-response theory explains that deceivers may experience higher arousal when screened for deception because this arousal is a cue conditioned to a past traumatic/dishonest experience (e.g., being screened primes a potentially unpleasant memory of an illicit act). Whereas deceivers are susceptible to this conditioned arousal (because they actually committed the illicit act in question), truth-tellers are not, ceteris paribus. Alternatively, conflict theory suggests that deceivers whose truthfulness is called into question will experience a higher level of arousal due to conflicting internal tendencies to deceive and tell the truth. Again, ceteris paribus, truth-tellers will not experience this same anxiety because they do not have the need to deceive. These anxiety by-products have been described as “a generally elevated level of arousal in the guilty” [74, p. 175]. This increased anxiety increases pupil dilation [95]. When anxiety increases, the pupil dilates to facilitate a greater state of alertness. When pupil dilation increases, it allows the eye to be more attentive to threatening stimuli and other information in the surrounding environment. Therefore, we predict that increased anxiety due to the state of being deceptive will be reflected in a person’s pupil dilation, as measured by an eye tracker. In summary:

Hypothesis 1: Pupil dilation will initially be greater for deceivers than for truth-tellers.

Consistent with the traditional CIT format, automated deception detection interactions are structured with multiple foils, with several stimuli in each foil.

A side effect of this procedure is repetition priming: a phenomenon in which previous exposures to a stimulus positively influence the processing efficiency of subsequent exposures [28, 44, 110]. The stimulus-model comparator theory [96, 97, 98] explains that when people see successive stimuli (e.g., multiple foils in a CIT), they generate a mental model of these stimuli. As people continue to see more stimuli, they rely less on processing the actual stimuli and more on the mental model. This allows people to process stimuli more effectively because they are able to rely on mental models regarding the format, content, and timing of stimuli, rather than on fully processing each stimulus from scratch. By products of repetition priming are decreased visual attention to stimuli and decreased pupil dilation over time [57].

Although pupil dilation for all participants is therefore likely to decrease over subsequent foils in a CIT, we posit that deceivers who do not see relevant stimuli will experience a greater decrease in pupil dilation than (a) deceivers who see relevant stimuli and (b) truth-tellers. The stimulus-model comparator theory argues that people will continue to rely heavily on their existing mental models of stimuli, unless an orienting response occurs [4]. An orienting response occurs when a stimulus is perceived as novel—or otherwise does not match the pattern or mental model of the previous stimuli. In the context of deception detection, an orienting response in a CIT occurs when someone sees a novel relevant stimulus (a stimulus he or she recognizes) in a series of nonrelevant stimuli [69, 75]. Therefore, pupil dilation for deceivers who see nonrelevant stimuli will decrease more rapidly compared to deceivers who see relevant stimuli, because deceivers who see relevant stimuli in a series of nonrelevant stimuli will experience orienting responses that counter the repetition priming effect.

Likewise, we posit that pupil dilation for deceivers who do not see relevant stimuli will decrease more rapidly than the pupil dilation for truth-tellers. Because neither group experiences an orienting response, the stimulus-model comparator theory predicts that pupil dilation for both groups will progress toward a point of saturation: a point at which behavioral responses (e.g., pupil dilation) are minimized and reliance on a mental model is maximized [96, 97, 98]. However, as previously discussed (see H1), pupil dilation for deceivers is initially larger than the pupil dilation for truth-tellers. Therefore, pupil dilation for deceivers who do not see relevant stimuli will decrease more rapidly to reach a point of saturation than pupil dilation for truth-tellers. In summary:

Hypothesis 2. Pupil dilation will decrease more rapidly over subsequent CIT foils for deceivers who do not see relevant stimuli than for (a) deceivers who do see relevant stimuli and (b) truth-tellers.

The defensive-response theory [19, 88] explains that people respond to threats by engaging in defensive behaviors to escape, combat, or otherwise alleviate the threat [48]. As identified in previous literature, one type of defensive behavior that occurs in an automated, visually based CIT is eye-gaze fixation on the center of the screen [37, 85, 102]. Automated, visually based CITs identify deception by monitoring how interviewees visually engage with stimuli presented on the screen (e.g., deceivers’ attention is often drawn toward relevant stimuli). If interviewees know that the system is monitoring their eye-gaze fixation patterns, they will often gaze at the center of the screen to avoid suspicion. People perceive the center of the screen as a “safety” point, as the center is equidistant from the visual stimuli presented in each quadrant of the screen. In other words, deceivers often view the center of the screen as an optimal point of avoidance [103].

Focusing one’s gaze on the center of the screen requires high attentional control. Attentional control refers to individuals’ ability to choose what they pay attention to and what they ignore [23]. Attentional control theory explains that attentional control is influenced by anxiety [23]. As people experience anxiety, their attention shifts from being goal-directed to being stimulus-directed as they search for threatening stimuli in the environment [23]. This results in a greater “distribution of attentional resources toward threat-related stimuli at the expense of attention allocated to the task” [62, p. 254]. As discussed in H1, although all people are likely to experience some anxiety during a CIT, deceivers may initially experience greater anxiety than truth-tellers. As a result of greater anxiety, deceivers will also have less attentional control [23]. The defensive-response theory explains that this anxiety, and the attendant decrease in attentional control, will be most salient at the onset of the threatening interaction—a period known as the initial defensive reflex [19, 88]. Thus, we predict that deceivers will experience lower attentional control at the onset of a CIT compared to truth-tellers. This lower attentional control will manifest in deceivers’ inability to perform defensive behaviors that require focused attention, such as focusing their initial gaze on the center of the screen. In summary, we hypothesize:

Hypothesis 3: Eye-gaze dwell time on the center of the screen will initially be less for deceivers than for truth-tellers.

Although a CIT may be threatening for all interviewees to some degree regardless of deception, we predict that the CIT will be more threatening over the duration of the test for people who see relevant stimuli than (a) for people who do not see relevant stimuli and (b) for truth-tellers. Perceived threat is a function of the perceived severity of the threat and perceived susceptibility to it [65]. The threat of being classified as deceptive may have similar severity for people regardless of whether they are deceptive or see relevant stimuli, insofar as they would all face the same consequence. However, deceivers who see relevant stimuli may perceive themselves to be more susceptible to the threat than either truth-tellers or deceivers who do not see relevant stimuli. Deceivers who see relevant stimuli may perceive that the system is more likely to classify them as deceptive because it has information pertinent to their deception, whereas deceivers who do not see relevant stimuli may perceive that the system lacks sufficient information to classify them as deceptive. Further, as truthtellers have nothing to conceal, their perceived susceptibility to being classified as deceptive may be lower, and thus, the perceived threat may also be lower.

The defensive-response theory explains that an increase in perceived threat will also increase the use of defensive behaviors [19, 88]. Therefore, a greater perceived threat of seeing relevant stimuli may motivate deceivers to more vigorously engage in defensive behaviors, resulting in a more rapid increase in eye-gaze dwell time on the center of the screen. Truth-tellers and deceivers who do not see relevant stimuli, however, may not exhibit as rapid an increase in defensive behaviors (or may even decrease defensive behaviors over time) because the perceived threat of being classified as deceptive is lower. In summary, we hypothesize:

Hypothesis 4: Eye-gaze dwell time on the center of the screen will increase more rapidly over subsequent CIT foils for deceivers who see relevant stimuli than for (a) truth-tellers and (b) deceivers who do not see relevant stimuli.

## Methodology

We conducted a mock crime experiment to test our hypotheses. Mock crime experiments are widely used in deception research [16, 18, 30, 41, 83]. The experimental task used for this research was patterned after a mock smuggling scenario used in a number of prior studies that investigated the development of deception detection systems [80, 103, 104, 105]. Participants were randomly assigned to one of two deceptive (smuggler) conditions or a truthful (nonsmuggler) condition (i.e., the control group). All participants then passed through a security checkpoint that required the completion of an automated deception detection interview used to identify smugglers. Deceivers completed a CIT-based interaction and were presented with either relevant stimuli or nonrelevant stimuli. Using an eye tracker, we monitored pupil dilation and eye-gaze dwell time on the center of the screen and explored how each participant’s oculometric behavior evolved over the course of the automated deception detection interaction.

## Participants

Undergraduate students (N = 114) were recruited from a large public U.S. university to participate in this experiment. The majority of participants (98 percent) were college juniors and seniors. The average age of all participants was 21.2 years. More than half (57 percent) of the participants were male, and the majority (70 percent) were U.S. citizens. The remainder of the sample was composed of a diverse range of ethnic backgrounds, including Hispanic (12 percent), Asian (10 percent), American Indian (1 percent), Pacific Islander (1 percent), and Other (7 percent). The majority (88 percent) of the sample was composed of native English speakers. All participants reported having no prior experience in law enforcement, criminal investigations, or deception detection interviews. Only one participant reported hearing information about the experiment before participating; data for this participant were not included in the analysis. Each participant engaged in five CIT foils resulting in 570 responses (114 × 5).

## Experimental Task

Participants arrived at the experiment location and were randomly assigned to one of three conditions: (1) deceivers who would see relevant stimuli (38 participants), (2) deceivers who would not see relevant stimuli (43 participants), or (3) truth-tellers in the control group (33 participants). People willing to participate reviewed and signed consent forms informing them that they would complete an automated interaction designed to detect deception. Each participant was paid \$20 to participate in the experiment and was instructed that he or she would receive an additional \$20 if the system did not classify him or her as being deceptive (thus introducing a higher-stakes element to the deception). Consent forms for the two deceptive conditions informed participants that they would pack sensitive materials in a bag and conceal this fact during the automated screening. After completing the consent forms, participants received additional instructions in line with their condition. The instructions differed for participants assigned to the deceptive conditions and the control group, as described in the following two sections.

## Instructions for Deceptive Conditions

Deceptive participants were guided to a room in which they were given a written set of instructions and left alone to review the instructions. The instructions directed the participants to pack a bag with benign items (e.g., clothes, books, a camera case) located on a table. The instructions also informed participants that they were involved with a well-known criminal enterprise operating in the area. They were then instructed to open a box (also located on the table) and use the instruction sheet and components found inside (e.g., a piece of metal pipe, a circuit board with a digital clock, a 9V battery, and a trigger mechanism) to construct a fake improvised explosive device (IED; refer to Figure 1 for an image of the IED). Next, participants had to pack the IED inside the bag and deliver it to one of three criminal associates waiting nearby (the participants were not aware that the criminal associates were fictitious). To be able to deliver the IED to one of these individuals, the participants were instructed to memorize each criminal’s face by completing an exercise in which they listed several facial features that they would later use to identify each of the three recipients. Each task was designed to ensure that the participants would remember the three faces, the IED, and the name of the criminal enterprise because the system would use this information as relevant stimuli in the subsequent automated deception test.

![](/api/attachments/25NCYZ4A/fulltext/images/f4cd51a569f5f18c98b3b4faaa60814e355890c31deb35bc6f2e0701651a8536.jpg)  
Figure 1. IED Constructed and Packed by Participants in the Deceptive Conditions

## Control Group Instructions

Participants in the control group (i.e., the truth-tellers) were also guided to a room in which they were given a written set of instructions and left alone to review the instructions. The instructions directed the participants to pack a bag with benign items located on a table; however, the participants did not pack any illicit items in the bag (i.e., they did not open the box and construct the IED) and did not have any knowledge of the three criminal associates or the name of the criminal organization.

## Automated Deception Detection Interview

Upon packing the bag, all participants were directed to the system that conducted the automated deception test. Participants were asked to place the bag on the floor and stand in front of the system. The system was composed of a desktop tower and a retractable arm with a monitor and sensors. An EyeTech<sup>TM</sup> Digital Systems VT2 eye tracking device was mounted directly underneath the monitor; data were captured and recorded at a rate of 30 Hz using the QuickCAPTURE<sup>TM</sup> software platform. By moving the retractable arm, the height of the monitor and the eye tracker was adjusted to each participant’s height. Next, the participants completed an automated task to calibrate the eye tracker. The system presented nine yellow circles in various locations on the screen and recorded eye movements while the participants viewed each circle.

When the calibration phase was complete, an embodied conversational agent (in this case, an avatar representing a human) appeared on the computer screen to explain to the participants that the system would be conducting an interview to identify whether they had any illicit items. The agent further explained the format of the automated deception test. After this preliminary interaction was completed, the automated deception test commenced. During this phase, each participant viewed five CIT foils composed of five slides in each foil (i.e., twenty-five slides in total). Each slide included four images located in one of the four quadrants on the slide, in accordance with a format used in previous literature (see [103,105]).

Before each slide was presented, a prerendered animated video of the embodied conversational agent asked each participant whether he or she was familiar with any of the following images. Each slide was then displayed for 7,500 milliseconds (ms). This duration was chosen because it represents the average duration time used to display images in visually based CITs (as reported in prior research [89, 92, 105]). Consistent with the best practices in eye-tracking research (e.g., [92, 103]), a fixation cross was displayed in the center of the screen for 500 ms to standardize participants’ eye-gaze origin before each slide was presented. While each slide was displayed, the eye tracker recorded pupil dilation and eye-gaze dwell time on the center of the screen. Eye-gaze dwell time on the center of the screen was calculated by summing how long participants viewed the neutral space located in the middle of the four images on each slide. Pupil diameter was calculated by taking the average pupil diameter of the eyes while the participants viewed each slide. Participants were expected to answer by saying “yes” or “no” out loud when asked about their familiarity with each set of images.

For participants in the deceptive condition who were shown relevant stimuli, some of the slides contained pictures relevant to the criminal organization, the IED, or the individuals to whom the participants were instructed to deliver the IED. Slides containing relevant stimuli appeared randomly in different locations within each foil, and relevant stimuli appeared randomly in different locations on each slide to mitigate any location-based effects. Relevant stimuli were chosen to have visual characteristics similar to those of nonrelevant stimuli (e.g., size, brightness, and contrast) in order to ensure that significant differences in oculometric behaviors were attributable to the manipulations and not to the features inherent in the images. All images were pilot tested before the full experiment as a means of removing images that triggered anomalous oculometric behaviors. Analysis of eye-tracking data in this pilot test confirmed that the selected images did not inherently cause significant changes in pupil dilation or eye-gaze dwell time on the center of the screen. Figure 2 and Figure 3 show examples of the slides that contained faces and illicit items, respectively.

## Debriefing

When the interaction was complete, the experiment facilitator informed participants in the deceptive conditions that they would not be delivering the IED to the fictitious criminal associates. The facilitator then conducted a manipulation check to ensure that the participants who had been instructed to learn the relevant stimuli before the screening could still recall the stimuli. This check was accomplished by displaying images to the participants using a tablet computer and requesting that they vocally identify the relevant stimuli. When the manipulation check was complete, the participants completed a survey. The survey was designed to collect information about each participant’s general perceptions of the interview, emotional responses during the interview, perceived performance, and the use of countermeasures. The control group participants completed the same survey after they finished the automated interview but did not complete the manipulation check.

![](/api/attachments/25NCYZ4A/fulltext/images/b7b32f3f9e6eaf5255979a791e413e36679e1b5bc72c0e3f47a97f12d251c647.jpg)  
Figure 2. An Example Slide Containing Facial Images: The Top-Right Image Was Used As One of the Three Criminal Associates

![](/api/attachments/25NCYZ4A/fulltext/images/43b89e2d7aaaa93bda0a9d6e0fa94856f1db8f82d267901f3826a0e93a01ea1e.jpg)  
Figure 3. An Example Slide Containing Illicit Items: The Bottom-Left Image Was the Target Item for the IED That Deceptive Participants Concealed in the Bag

## Analysis

We tested our hypotheses using latent growth curve modeling of the oculometric data collected with the automated deception detection system. Latent growth curve modeling is a longitudinal analysis technique that estimates the intercept and slope (change) of data over time [78]. In our analysis, latent growth curve modeling estimated the intercept and slope of the line that fit the observed values of pupil dilation and eye-gaze dwell time on the center of the screen over time (i.e., from foil 1 to foil 5, sequentially). The intercept indicated the value of the dependent variable at the onset of the test. The slope indicated whether the dependent variable increased or decreased over time, as well as the magnitude of this change. We then explored how each condition and control variable influenced the intercept and the slope separately. As the hypotheses are specifically about the intercept and slope of pupil dilation and eye-gaze dwell time on the center of the screen for each condition, latent growth curve modeling was deemed appropriate.

We developed separate latent growth curve models for pupil dilation and eye-gaze dwell time on the center of the screen. In each model, we included categorical dummy variables, which included a binary 1 for group membership or a binary 0 for nonmembership, to represent the conditions. We specified a relationship between each categorical variable and the slope and intercept. Because there were three groups, there were two categorical variables. For example, we included a categorical variable for (a) deceivers who saw relevant stimuli and (b) deceivers who did not see relevant stimuli. The control group was implicitly represented when both of the other categorical variables were 0 (indicating nonmembership). This third condition, (c) truth-tellers, is thus referred to as the baseline or reference group. If the categorical dummy variables for conditions (a) and (b) significantly predict the intercept or slope, then this indicates that the condition’s intercept or slope is significantly different from the intercept or slope of the baseline group. To test the hypotheses, we changed the condition that would serve as the baseline group. In addition, we accounted for control variables, including age, sex, years of education, and ethnicity. The general structural model used for each growth curve is shown in Figure 4.

We analyzed the models using the lavaan R package (version 0.5–20). We used the output of the analysis from the lavaan R package as input for the simsem R package (version 0.5–11) to conduct a power analysis and calculated additional fit indices using a Monte Carlo approach. The pupil dilation model $( \chi ^ { 2 } = 1 8 . 4 4 5 , \mathrm { d f } = 1 6 , p > . 0 5 )$ and the eye-gaze dwell time model $( \chi ^ { 2 } = 2 5 . 8 5 6 , \ : \mathrm { d f } = 1 6 , p > . 0 5 )$ demonstrated adequate fit; the root mean square error of approximation (RMSEA) was less than .05 for both models. In addition, the pupil dilation model (β = .886) and the eye-gaze dwell time model $( \beta = . 8 6 6 )$ exhibited adequate power. Finally, we analyzed the latent growth curve models with quadratic terms. For both models, the model fit was worse based on the chi-square statistics for the quadratic terms model than it was for the linear model: 66.088 for the pupil dilation quadratic model and 45.756 for the eyegaze dwell time model. Thus, we retained the linear model.

![](/api/attachments/25NCYZ4A/fulltext/images/abbdfe258e04a9fafc6e6eb99e589ba1ba91af9b5c068f37f01565dc11400171.jpg)  
Figure 4. The General Structural Model Used for Latent Growth Curve Modeling

## Models for Pupil Dilation

To analyze H1 and H2, we specified a latent growth curve model for pupil dilation with each foil as the dependent variable. First, we analyzed the model with all control variables in addition to the conditions’ dummy variables. We specified a relationship between each variable and the intercept and slope. We included sex as a binary dummy variable (1 for male, 0 for female), age as a continuous variable, and years of education as a continuous variable (the number of years of college education the participant had completed), and we created a binary dummy variable for each nationality except that of the United States, which was used as the reference group. This resulted in five ethnicity-specific dummy variables: Hispanic, Asian, American Indian, Pacific Islander, and Other. Sex statistically significantly predicted the intercept of pupil dilation $( \beta = - 0 . 3 2 2 , z = - 2 . 5 6 6 , p < . 0 1 )$ , and years of education statistically significantly predicted the slope $( \beta = 0 . 0 2 0 , z = 2 . 1 6 0 , p < . 0 5 )$

We removed the statistically nonsignificant control variables and analyzed the model again. The model thus predicted the intercept and slope using binary dummy variables for the nonrelevant stimuli and relevant stimuli conditions, a continuous variable for years of education, and a binary variable for sex. The control group, for whom the nonrelevant stimuli and the relevant stimuli conditions were 0, was the reference group. The trend lines of pupil dilation for each condition are graphed in Figure 5, and the results of this new model are shown in Table 1. The results support H1: There was a statistically significant difference in pupil dilation at the onset of the interaction between truth-tellers and deceivers who either did not see relevant stimuli $( \beta = 0 . 5 8 7 , z = 3 . 8 5 8 , p < . 0 0 1 )$ or did see relevant stimuli $( \beta = 0 . 6 2 3 , z = 4 . 8 2 7 , p <$ .001).

![](/api/attachments/25NCYZ4A/fulltext/images/a08ff44ed0cdac7a4cf114ca83891adcc4e643ff0906cf0bc7908019ecc2f411.jpg)  
Figure 5. Pupil Dilation Growth Curves for Each Group

Table 1. Pupil Dilation Model with the Control Group as the Reference Group

<table><tr><td>Group</td><td>Estimate</td><td>Std. error</td><td>z-value</td><td>P (&gt; |z|)</td></tr><tr><td colspan="5">Intercept</td></tr><tr><td>Nonrelevant stimuli</td><td>0.587</td><td>0.152</td><td>3.858</td><td>0.000</td></tr><tr><td>Relevant stimuli</td><td>0.623</td><td>0.129</td><td>4.827</td><td>0.000</td></tr><tr><td>Years of education</td><td>0.131</td><td>0.148</td><td>0.887</td><td>0.375</td></tr><tr><td>Sex</td><td>-0.344</td><td>0.131</td><td>-2.625</td><td>0.009</td></tr><tr><td colspan="5">Slope</td></tr><tr><td>Nonrelevant stimuli</td><td>-0.054</td><td>0.011</td><td>-5.089</td><td>0.000</td></tr><tr><td>Relevant stimuli</td><td>-0.022</td><td>0.011</td><td>-2.120</td><td>0.034</td></tr><tr><td>Years of education</td><td>0.015</td><td>0.010</td><td>1.575</td><td>0.115</td></tr><tr><td>Sex</td><td>0.018</td><td>0.010</td><td>1.752</td><td>0.080</td></tr><tr><td>Intercept</td><td>2.496</td><td>1.308</td><td>1.908</td><td>0.056</td></tr><tr><td>Slope</td><td>-0.270</td><td>0.079</td><td>-3.407</td><td>0.001</td></tr></table>

To test H2a and H2b, we changed the reference group in the analysis from the control group to the nonrelevant stimuli condition (we included a binary dummy variable for the relevant stimuli condition and the control group but not for the nonrelevant stimuli condition). The results are shown in Table 2 and support both hypotheses: Pupil dilation decreased more rapidly over subsequent CIT foils for deceivers who did not see relevant stimuli than for truth-tellers $( \beta = 0 . 0 5 4 , z =$ 4.991, $p \ < \ . 0 0 1 )$ and deceivers who did see relevant stimuli $( \beta \ : = \ : 0 . 0 3 2 , \ : z \ : =$ $2 . 7 8 2 , p < . 0 1 )$

Table 2. Pupil Dilation Model with the Nonrelevant Stimuli Condition as the Reference Group

<table><tr><td>Group</td><td>Estimate</td><td>Std. error</td><td>z-value</td><td>P(&gt;|z|)</td></tr><tr><td colspan="5">Intercept</td></tr><tr><td>Relevant stimuli</td><td>0.036</td><td>0.153</td><td>0.237</td><td>0.812</td></tr><tr><td>Control</td><td>-0.587</td><td>0.155</td><td>-3.775</td><td>0.000</td></tr><tr><td>Years of education</td><td>0.131</td><td>0.159</td><td>0.822</td><td>0.411</td></tr><tr><td>Sex</td><td>-0.344</td><td>0.136</td><td>-2.524</td><td>0.012</td></tr><tr><td colspan="5">Slope</td></tr><tr><td>Relevant stimuli</td><td>0.032</td><td>0.012</td><td>2.782</td><td>0.005</td></tr><tr><td>Control</td><td>0.054</td><td>0.011</td><td>4.991</td><td>0.000</td></tr><tr><td>Years of education</td><td>0.018</td><td>0.011</td><td>1.565</td><td>0.118</td></tr><tr><td>Sex</td><td>0.015</td><td>0.010</td><td>1.554</td><td>0.120</td></tr><tr><td>Intercept</td><td>4.844</td><td>1.447</td><td>3.347</td><td>0.001</td></tr><tr><td>Slope</td><td>-0.488</td><td>0.097</td><td>-5.044</td><td>0.000</td></tr></table>

## Models for Eye-gaze Dwell Time on the Center of the Screen

To analyze H3 and H4, we specified the same latent growth curve model as before, except that eye-gaze dwell time on the center of the screen for each foil was used as the dependent variable. First, similar to the previous analysis, we analyzed the model with all control variables in addition to the conditions’ dummy variables. However, none of the control variables statistically significantly influenced the intercept or slope. We therefore removed the control variables and analyzed the model again. The model thus contained binary dummy variables for the nonrelevant stimuli condition and the relevant stimuli condition predicting the intercept and slope. The control group was the reference group, in which the nonrelevant stimuli and relevant stimuli conditions were 0. The trend lines of eye-gaze dwell time on the center of the screen for each condition are graphed in Figure 6, and the results of this new model are shown in Table 3. The results do not support H3: There was no statistically significant difference in initial eye-gaze dwell time on the center of the screen between truth-tellers and deceivers who either did not see relevant stimuli $( \beta = 0 . 0 1 0 , z = 0 . 2 4 5 , p > . 0 5 )$ or did see relevant stimuli $( \beta = - 0 . 0 1 1 , z = - 0 . 2 7 2 , p > . 0 5 )$

To test H4a and H4b, we changed the reference group in the analysis from the control group to the relevant stimuli condition (we included a binary dummy variable for the nonrelevant stimuli condition and the control group, but not the relevant stimuli condition). The results are shown in Table 4 and support our hypotheses: Eye-gaze dwell time on the center of the screen increased more rapidly over subsequent CIT foils for deceivers who saw relevant stimuli than for truthtellers $( \beta = - 0 . 0 3 7 , z = - 6 . 7 9 1 , p < . 0 0 1 )$ and deceivers who did not see relevant stimuli $( \beta = - 0 . 0 2 7 , z = - 3 . 0 4 8 , p < . 0 1 )$

![](/api/attachments/25NCYZ4A/fulltext/images/421ac8fdaf9391b9483e26181e4632c9d549d5eb3845781f44a68cd4dd454166.jpg)  
Figure 6. Eye-gaze Dwell Time Growth Curves for Each Group

Table 3. Eye-gaze Dwell Time on the Center of the Screen with the Control Group as the Reference Group

<table><tr><td>Condition</td><td>Estimate</td><td>Std. error</td><td>z-value</td><td>P(&gt;|z|)</td></tr><tr><td colspan="5">Intercept</td></tr><tr><td>Nonrelevant stimuli</td><td>0.010</td><td>0.042</td><td>0.245</td><td>0.806</td></tr><tr><td>Relevant stimuli</td><td>-0.011</td><td>0.040</td><td>-0.272</td><td>0.786</td></tr><tr><td colspan="5">Slope</td></tr><tr><td>Nonrelevant stimuli</td><td>0.010</td><td>0.008</td><td>1.181</td><td>0.238</td></tr><tr><td>Relevant stimuli</td><td>0.037</td><td>0.005</td><td>6.682</td><td>0.000</td></tr><tr><td>Intercept</td><td>0.088</td><td>0.093</td><td>0.949</td><td>0.343</td></tr><tr><td>Slope</td><td>-0.035</td><td>0.014</td><td>-2.558</td><td>0.011</td></tr></table>

Table 4. Eye-gaze Dwell Time on the Center of the Screen with the Relevant Stimuli Condition as the Reference Group

<table><tr><td>Group</td><td>Estimate</td><td>Std. error</td><td>z-value</td><td>P(&gt;|z|)</td></tr><tr><td colspan="5">Intercept</td></tr><tr><td>Nonrelevant stimuli</td><td>0.021</td><td>0.041</td><td>0.510</td><td>0.610</td></tr><tr><td>Control</td><td>0.011</td><td>0.038</td><td>0.281</td><td>0.778</td></tr><tr><td colspan="5">Slope</td></tr><tr><td>Nonrelevant stimuli</td><td>-0.027</td><td>0.009</td><td>-3.048</td><td>0.002</td></tr><tr><td>Control</td><td>-0.037</td><td>0.005</td><td>-6.791</td><td>0.000</td></tr><tr><td>Intercept</td><td>0.045</td><td>0.088</td><td>0.514</td><td>0.607</td></tr><tr><td>Slope</td><td>0.111</td><td>0.014</td><td>7.791</td><td>0.000</td></tr></table>

## Supplemental Analysis: Prediction

As a supplemental analysis, we calculated the intercepts and slopes of pupil dilation and eye-gaze dwell time on the center of the screen for each participant and then used them in a classification model to predict membership in the three groups: (1) deceivers who saw relevant stimuli, (2) deceivers who did not see relevant stimuli, and (3) truth-tellers. This supplemental analysis represents a high-level perspective on whether the intercepts and slopes of these oculometric features have utility in classifying deception. However, this analysis does not claim to be either an optimal model or an exhaustive approach. Future research should combine these findings with other types of deception indicators to explore the ideal times and combinations of features that can be used to predict deception.

We specified a multinomial logistic regression model in the Weka software package (version 3.6.10). In this model, the dependent variables were the three groups: (1) deceivers who saw relevant stimuli, (2) deceivers who did not see relevant stimuli, and (3) truth-tellers. The predictors were participants’ intercepts and slopes of pupil dilation and eye-gaze dwell time on the center of the screen, resulting in a total of four predictors. The model accuracy in predicting membership in the three groups was assessed using tenfold cross validation. The sensitivity of the model was 73.9 percent, and the detailed accuracy rates are shown in Table 5.

## Discussion

This research was conducted to address the following question: How do pupil dilation and eye-gaze fixations change over the administration of an automated deception detection interaction for truth-tellers versus deceivers who see relevant or nonrelevant stimuli? To explore this research question, we specified hypotheses and utilized a mock crime experiment to test whether pupil dilation and eye-gaze dwell time on the center of the screen evolved over the administration of an automated deception detection interaction for three groups: (1) deceivers who saw relevant stimuli, (2) deceivers who did not see relevant stimuli, and (3) truth-tellers. The results of the hypothesis tests are summarized in Table 6, and a discussion of these results is presented in the following sections.

## Implications for Research

Our findings have several implications for research investigating oculometric indicators of deception and the development of automated deception detection systems. First, we demonstrated how eye-tracking deception indicators evolve over the course of an automated deception detection interaction. Researchers [14] have previously suggested that oculometric behaviors evolve over the course of a deceptive interaction. However, previous research has largely left this proposition untested, often treating pupil dilation and eye-gaze fixation patterns the same over the course of interactions designed to detect deception. In contrast, we addressed this gap by examining how variations in pupil dilation and eye-gaze fixation patterns fluctuate during the course of an automated deception detection interaction. Overall, our results indicate that future research exploring the development of deception detection systems should account for these fluctuations.

Table 5. Detailed Accuracy Rates for the Prediction Model

<table><tr><td>Condition</td><td>True positive rate</td><td>False positive rate</td><td>Precision</td><td>Recall</td><td>F-measure</td><td>ROC area (AUC)</td></tr><tr><td>Truth-tellers (control)</td><td>0.763</td><td>0.143</td><td>0.725</td><td>0.763</td><td>0.744</td><td>0.881</td></tr><tr><td>Relevant stimuli</td><td>0.846</td><td>0.092</td><td>0.825</td><td>0.846</td><td>0.835</td><td>0.946</td></tr><tr><td>Nonrelevant stimuli</td><td>0.605</td><td>0.156</td><td>0.657</td><td>0.605</td><td>0.63</td><td>0.786</td></tr><tr><td>Weighted average</td><td>0.739</td><td>0.13</td><td>0.736</td><td>0.739</td><td>0.737</td><td>0.872</td></tr></table>

Notes: ROC = receiver operating characteristic

Table 6. Summary of Results

<table><tr><td>No.</td><td>Hypothesis</td><td>Supported</td></tr><tr><td>H1</td><td>Pupil dilation will initially be greater for deceivers than for truth-tellers.</td><td>Yes</td></tr><tr><td>H2a</td><td>Pupil dilation will decrease more rapidly over subsequent CIT foils for deceivers who do not see relevant stimuli than for deceivers who do see relevant stimuli.</td><td>Yes</td></tr><tr><td>H2b</td><td>Pupil dilation will decrease more rapidly over subsequent CIT foils for deceivers who do not see relevant stimuli than for truth-tellers.</td><td>Yes</td></tr><tr><td>H3</td><td>Eye-gaze dwell time on the center of the screen will initially be less for deceivers than for truth-tellers.</td><td>No</td></tr><tr><td>H4a</td><td>Eye-gaze dwell time on the center of the screen will increase more rapidly over subsequent CIT foils for deceivers who see relevant stimuli than for truth-tellers.</td><td>Yes</td></tr><tr><td>H4b</td><td>Eye-gaze dwell time on the center of the screen will increase more rapidly over subsequent CIT foils for deceivers who see relevant stimuli than for deceivers who do not see relevant stimuli.</td><td>Yes</td></tr></table>

Further, we provided a theoretical basis explaining why eye-tracking-based deception indicators evolve over the course of an automated deception detection interaction. To do this, we drew on several theories that help explain how eye-tracking behaviors evolve for truth-tellers, deceivers who see relevant stimuli, and deceivers who do not see relevant stimuli. Based on conditioned-response theory and conflict theory, we explained how pupil dilation is initially greater for deceivers than truthtellers. Drawing simultaneously on repetition priming and the stimulus-model comparator theory allows us to also explain that pupil dilation decreases more quickly for deceivers who do not see relevant stimuli than for the other groups. Finally, based on the perceived threat and defensive-response theories, we explained that deceivers who see relevant stimuli will gaze longer at the center of the screen over time in response to an increasing threat than either the control group or the other deceptive condition. Together, these theories provide a more complete perspective of how oculometrics evolve during this type of interaction for truth-tellers and deceivers than a single theory alone could predict. In our results, we found that these novel indicators predicted which experimental group the participants belonged to with a sensitivity of 73.9 percent.

In addition, our research identified challenges and opportunities associated with using eye-gaze dwell time on the center of the screen as an indicator of deception. Specifically, in our study, the intercept of eye-gaze dwell time on the center of the screen was not significantly different between any of the participant groups—deceptive or truthful. On a more general scale, these results may indicate that identifying deception by simply measuring the presence or absence of strategic behaviors (e.g., countermeasures) to avoid detection may be challenging [84, 104, 105]. We attribute this result to the fact that truth-tellers and deceivers alike want to avoid suspicion and may, therefore, employ strategic behaviors [84]. However, we found that deceivers who saw relevant stimuli increased their use of strategic behaviors more rapidly (i.e., eye-gaze dwell time on the center of the screen) than either truth-tellers or deceivers not exposed to relevant stimuli. Thus, our research suggests that although the initial presence or absence of strategic behaviors may not prove fruitful in detecting deception, an increased rate in the use of strategic behaviors during an interaction over time may at least indicate suspicion.

Finally, some implications of this study are more far-reaching than the confines of automated deception detection systems. A wealth of information systems research has focused on the initial adoption and continued use of information systems (e.g., [25, 26]). This research has been conducted based on the perspective that these systems are used to facilitate individuals and organizations in completing some form of objective [12, 86, 106, 107] or to improve organizational effectiveness [1, 99]. More recent information systems research has sought to understand automatic information technology use [50] and how users’ implicit and explicit cognitive beliefs [51] drive continued system use. As technology continues to become more pervasive, new forms of human–computer interactions are taking place, including interactions in which the goals of the user and the system conflict. For example, using a system that is designed to detect deceptive behavior may conflict with the user’s desire to avoid detection. Future research is needed to better understand these scenarios and define what constitutes an effective, useful human-computer interaction. As design science research in the information systems domain [49, 50, 55] continues to investigate deception detection systems [38, 80, 102, 103, 104], it is paramount for researchers to investigate how users perceive such interactions and to identify the positive and negative effects that may occur as these types of interactions take place.

## Implications For Practice

Our research presents several practical implications. First, we identified evolving variations in oculometric behaviors that may indicate deception in an automated deception detection interview. For example, in our experiments, we found that deceivers initially have greater pupil dilation than truth-tellers (H1), that deceivers who do not see relevant stimuli have a steeper decline in pupil dilation than either deceivers who see relevant stimuli (H2a) or truth-tellers (H2b), and that deceivers who see relevant stimuli gaze at the center of the screen longer over time relative to either truth-tellers (H4a) or deceivers who do not see relevant stimuli (H4b). Effective deception detection systems should be designed to measure these and other novel deception indicators [101], insofar as doing so will result in more accurate predictions and make it more difficult for people to use countermeasures to mitigate the effectiveness of these types of systems [84, 104, 105]. As our preliminary prediction model based solely on these novel deception indicators (occurring over time) yielded overall sensitivity of 73.9 percent, the features identified in this research can be incorporated into deception detection systems that already leverage other types of indicators to improve their overall robustness and accuracy.

Another practical implication of our findings is the discovery that there may be ideal times for assessing deception during a system interaction. For example, we found that pupil dilation naturally decreases over the administration of an automated deception detection interaction. Decreasing pupil dilation may indicate habituation and decreasing vigilance; thus, the beginning of an interaction may be the best time to identify deception indicators. Conversely, the results suggest that system users may still be adjusting to the novelty of the interview process at the beginning of the interaction. Consequently, the latter half of the interaction may be the best time to identify deception indicators that deviate from the baseline. Although we showed that these trends can be valuable for predicting deception, future research should explore these changes within the context of developing optimal classification algorithms.

Finally, our research suggests the potential for a new form of deception detection test: targetless CITs. The traditional CIT requires the presentation of crime-relevant information (i.e., relevant stimuli that have meaning only for deceivers) in order to trigger orienting and defensive responses. However, with the proliferation of media outlets that report details of criminal events in real time, finding a valid relevant stimulus that has meaning only for a deceiver is difficult (assuming enough detail is known about the illicit act in the first place to identify relevant stimuli). For instance, Japan, China, and Israel are some of the only countries in which the CIT is used [36, 56, 118], in part because their media outlets do not disseminate details of active criminal cases to the public [76]. Our research suggests that there are behavioral differences between deceivers and truth-tellers that do not require the use of relevant stimuli. For example, we found that pupil dilation decreases more rapidly throughout the CIT for deceivers who do not see relevant stimuli than for truth-tellers (H2b); and pupil dilation was overall greater for deceivers who did not see relevant stimuli than for truth-tellers (H1). The identification of these differences, and others that may be illuminated in future research, can be used to construct a modified CIT in which the identification or inclusion of relevant stimuli is unnecessary.

## Limitations and Future Research

As with all research, the limitations associated with this work must be considered. First, the vast majority of deception research is limited by the use of sanctioned deception and its consequent lack of realism and generalizability [79]. However, researchers have shown that these studies are generalizable to real-world deception [6, 67, 83, 117]. Furthermore, it could be argued that statistically significant differences associated with deceptive behaviors in a lab would only be exacerbated in real-life contexts in which higher stakes are involved. Accordingly, we deem the use of a mock crime methodology to be consistent with best practices in deception research and consider this methodological approach generalizable to real-world deception. However, we recognize that a gap exists between laboratory and realworld deception and that future research should seek to minimize this gap as much as possible by confirming the laboratory results in the field.

Second, it is possible that eye tracking in a real-world environment could be riddled with inaccuracies or missing data points due to varying light conditions or uncooperative interviewees, both of which can be controlled far more readily in a laboratory setting [105]. Such considerations apply not only to eye tracking but also to any sensor considered for use in field applications (e.g., high levels of ambient noise could reduce the richness, and thus the value, of vocalic measurements). Future deception research should evaluate the robustness of eye tracking (and other sensors) in real-world interviewing applications in which there is reduced operational control.

A final limitation of this research is the reduced set of eye features selected for analysis and discussion. A variety of ocular features can be measured with eyetracking devices, including eye blinks [11, 42, 71], eye-gaze fixations [27, 70, 73, 116], saccades [85, 103, 109], pupil dilation [9, 64, 74], and smooth-pursuit eye movements [7]. Although many of these features have been explored within the context of deception, eye-gaze fixations and pupil dilation have received tremendous interest. As the purpose of this study was to expand the scope of analysis from the typical phasic-response analysis used in the majority of deception studies to a review of how deception indicators change over time, eye-gaze fixations and pupil dilation were selected due to their prominence in the literature. Future research should consider the implications of this work not only for the remaining ocular features outside the scope of this study but also for additional deception indicators that can be measured using different types of sensors (e.g., vocalics [45, 53, 87] and rigidity [102]), insofar as analysis of the evolving variations in these indicators may yield deception detection systems that are more robust and reliable.

## Conclusion

This research explored how pupil dilation and eye-gaze fixation patterns evolve over the course of an automated deception detection interaction. Hypotheses were theoretically developed to explain how oculometric behaviors evolve over the course of an automated deception detection interaction administered to three groups: (1) deceivers who see relevant stimuli, (2) deceivers who do not see relevant stimuli, and (3) truthtellers. We tested these hypotheses in a realistic mock crime experiment in which ground truth was known. The results indicate that oculometric behaviors do evolve over time. Furthermore, these trends can differentiate truth-tellers from deceivers, even in the absence of relevant stimuli. A classification model using participants’ intercepts and slopes of pupil dilation and eye-gaze dwell time on the center of the screen as predictors yielded an aggregate true positive rate of 73.9 percent and an aggregate false positive rate of 13 percent. The theoretical and practical implications of these results include the following: (1) the identification of evolving oculometric patterns that may be used as new indicators of deception in automated screening systems, (2) a better understanding of how oculometrics (i.e., eye-gaze fixation patterns and pupil dilation) evolve over the duration of an automated deception detection interaction, and (3) evidence that oculometric behaviors can vary between truth-tellers and deceivers even if relevant stimuli are not shown. The findings of this work can be used to further inform theoretically driven and practically motivated efforts to develop information systems capable of accurately distinguishing between truth and deception.

Funding: This research was supported by the U.S. Department of Homeland Security, through the National Center for Border Security and Immigration (Grant #2008-ST-061-BS0002), and the Center for Identification Technology Research (CITeR), a National Science Foundation (NSF) Industry/University Cooperative Research Center (I/UCRC) (Project #12F-13W-12). Acknowledgments: Any opinions, findings, and conclusions or recommendations herein are those of the authors and do not necessarily reflect views of the U.S. Department of Homeland Security or the Center for Identification Technology Research. We acknowledge contributions made by Nathan W. Twyman and Aaron C. Elkins in facilitating the data collection, as well as support provided by a number of researchers affiliated with the Center for the Management of Information (CMI).

## REFERENCES

1. Adamson, I., and Shine, J. Extending the new technology acceptance model to measure the end user information system satisfaction in a mandatory environment: A bank’s treasury. Technology Analysis and Strategic Management, 15, 4 (2003), 441–455.

2. Althoff, R.R., and Cohen, N.J. Eye-movement-based memory effect: A reprocessing effect in face perception. Journal of Experimental Psychology: Learning, Memory, and Cognition, 25, 4 (1999), 997–1010.

3. Baker, L.; Stern, J.A.; and Goldstein, R. The Gaze Control System and the Detection of Deception. Final Report. St. Louis: Washington University, Department of Psychology, 1992.

4. Barry, R.J. Habituation of the orienting reflex and the development of preliminary process theory. Neurobiology of Learning and Memory, 92, (2009), 235–242.

5. Beatty, J., and Kahneman, D. Pupillary changes in two memory tasks. Psychonomic Science, 5, 10 (1966), 371–372.

6. Ben-Shakhar, G., and Elaad, E. The validity of psychophysiological detection of information with the guilty knowledge test: A meta-analytic review. Journal of Applied Psychology, 88, 1 (2003), 131–151.

7. Beutter, B.R., and Stone, L.S. Human motion perception and smooth eye movements show similar directional biases for elongated apertures. Vision Research, 38, 9 (1998), 1273–1286.

8. Bond, C.F., and DePaulo, B.M. Accuracy of deception judgments. Personality and Social Psychology Review, 10, 3 (2006), 214–234.

9. Bradley, M.M.; Miccoli, L.; Escrig, M.A.; and Lang, P.J. The pupil as a measure of emotional arousal and autonomic activation. Psychophysiology, 45, 4 (2008), 602–607.

10. Bradley, M.T., and Janisse, M.P. Accuracy demonstrations, threat, and the detection of deception: Cardiovascular, electrodermal, and pupillary measures. Psychophysiology, 18, 3 (1981), 307–315.

11. ten Brinke, L., and Porter, S. Cry me a river: Identifying the behavioral consequences of extremely high-stakes interpersonal deception. Law and Human Behavior, 36, 6 (2012), 469–477.

12. Brown, S.A.; Venkatesh, V.; and Goyal, S. Expectation confirmation in technology use. Information Systems Research, 23, 2 (2012), 474–487.

13. Buller, D.B., and Burgoon, J.K. Deception: Strategic and nonstrategic communication. In J.A. Daly and J.M. Wiemann (eds.), Strategic Interpersonal Communication. Hillsdale, NJ: Erlbaum, 1994, pp. 191–223.

14. Buller, D.B., and Burgoon, J.K. Interpersonal deception theory. Communication Theory, 6, 3 (1996), 203–242.

15. Bulling, A., and Gellersen, H. Toward mobile eye-based human-computer interaction. Pervasive Computing, IEEE, 9, 4 (2010), 8–12.

16. Burgoon, J.K.; Blair, J.P.; and Strom, R.E. Cognitive biases and nonverbal cue availability in detecting deception. Human Communication Research, 34, 4 (2008), 572–599.

17. Burgoon, J.K.; Derrick, D.C.; Elkins, A.C. et al. Potential noncontact tools for rapid credibility assessment from physiological and behavioral cues. In the 42nd Annual IEEE International Carnahan Conference on Security Technology, Prague, October 13–16, 2008, pp. 150–157.

18. Burgoon, J.K., Proudfoot, J.G., Wilson, D., and Schuetzler, R. Hidden patterns of nonverbal behavior associated with truth and deception. Journal of Nonverbal Behavior, 38, 3 (2014), 325–254.

19. Campbell, B.A.; Wood, G.; and McBride, T. Origins of orienting and defensive responses: An evolutionary perspective. In P.J. Lang, R.F. Simons and M. Balaban (eds.), Attention and Orienting: Sensory and Motivational Processes. Malwah, NJ: Erlbaum, 1997, pp. 41–67.

20. Cannon, W.B. The emergency function of the adrenal medulla in pain and the major emotions. American Journal of Physiology-Legacy Content, 33, 2 (1914), 356–372.

21. Carmel, D.; Dayan, E.; Naveh, A.; Raveh, O.; and Ben-Shakhar, G. Estimating the validity of the guilty knowledge test from simulated experiments. Journal of Experimental Psychology-Applied, 9, 4 (2003), 261–269.

22. Cook, A.E.; Hacker, D.J.; Webb, A.K. et al. Lyin’ eyes: Ocular-motor measures of reading reveal deception. Journal of Experimental Psychology: Applied, 18, 3 (2012), 301–313.

23. Coombes, S.A.; Higgins, T.; Gamble, K.M.; Cauraugh, J.H.; and Janelle, C.M. Attentional control theory: Anxiety, emotion, and motor planning. Journal of Anxiety Disorders, 23, 8 (2009), 1072–1079.

24. Cyr, D.; Head, M.; Larios, H.; and Pan, B. Exploring human images in website design: A multi-method approach. MIS Quarterly, 33, 3 (2009), 539–566.

25. Davis, F. Perceived usefulness, perceived ease of use, and user acceptance of information technology. MIS Quarterly, 13, 3 (1989), 319–340.

26. Davis, F.D.; Bagozzi, R.P.; and Warshaw, P.R. Extrinsic and intrinsic motivation to use computers in the workplace. Journal of Applied Social Psychology, 22, 14 (1992), 1111–1132.

27. Day, R. Examining the validity of the Needleman-Wunsch algorithm in identifying decision strategy with eye-movement data. Decision Support Systems, 49, 4 (2010), 396–403.

28. Demb, J.B.; Desmond, J.E.; Wagner, A.D.; Vaidya, C.J.; Glover, G.H.; and Gabrieli, J.D. E. Semantic encoding and retrieval in the left inferior prefrontal cortex: A functional MRI study of task difficulty and process specificity. Journal of Neuroscience, 15, 9 (1995), 5870–5878.

29. DePaulo, B.M.; Lindsay, J.J.; Malone, B.E.; Muhlenbruck, L.; Charlton, K.; and Cooper, H. Cues to deception. Psychological Bulletin, 129, 1 (2003), 74–118.

30. Derrick, D.C.; Elkins, A.C.; Burgoon, J.K.; Nunamaker, J.F., Jr.; and Zeng, D. Border security credibility assessments via heterogeneous sensor fusion. IEEE Intelligent Systems, 25, 3 (2010), 41–49.

31. Derrick, D.C.; Jenkins, J.L.; and Nunamaker, J.F., Jr. Design principles for special purpose, embodied, conversational intelligence with environmental sensors (SPECIES). AIS Transactions on Human-Computer Interaction, 3, 2 (2011), 62–81.

32. Derrick, D.C.; Moffit, K.; and Nunamaker, J.F., Jr. Eye gaze behavior as a guilty knowledge test: Initial exploration for use in automated, kiosk-based screening. In Forty-Fourth Annual Hawaii International Conference on System Sciences. Kauai. Piscataway, NJ: Printing House, 2011, pp. 5–10.

33. Dimoka, A.; Banker, R.D.; Benbasat, I. et al. On the use of neurophysiological tools in IS research: Developing a research agenda for NeuroIS. MIS Quarterly, 36, 3 (2012), 679–702.

34. Djamasbi, S.; Siegel, M.; Skorinko, J.; and Tullis, T. Online viewing and aesthetic preferences of Generation Y and the baby boom generation: Testing user web site experience through eye tracking. International Journal of Electronic Commerce, 15, 4 (2011), 121–158.

35. Ekman, P., and O’Sullivan, M. Who can catch a liar? American Psychologist, 46, 9 (1991), 913–920.

36. Elaad, E. Detection of guilty knowledge in real-life criminal investigations. Journal of Applied Psychology, 75, 5 (1990), 521–529.

37. Elkins, A.C.; Derrick, D.C.; and Gariup, M. The voice and eye gaze behavior of an imposter: Automated interviewing and detection for rapid screening at the border. In Workshop on Computational Approaches to Deception Detection: Association for Computational Linguistics. Association for Computational Linguistics, Avignon, France, April 23–27, 2012, pp. 49–54.

38. Elkins, A.C.; Dunbar, N.E.; Adame, B.; and Nunamaker, J.F., Jr. Are users threatened by credibility assessment systems? Journal of Management Information Systems, 28, 4 (2013), 249–261.

39. Ellis, H.D.; Shepherd, J.W.; and Davies, G.M. Identification of familiar and unfamiliar faces from internal and external features. Perception, 8 (1979), 431–439.

40. Ellson, D.G.; Davis, R.C.; Saltzman, I.J.; and Burke, C.J. A Report of Research on Detection of Deception: Technical Report Prepared for Office of Naval Research. Bloomington: Indiana University, 1952.

41. Farwell, L.A., and Donchin, E. The truth will out: Interrogative polygraphy (lie detection) with event-related brain potentials. Psychophysiology, 28, 5 (1991), 531–547.

42. Fukuda, K. Eye blinks: New indices for the detection of deception. International Journal of Psychophysiology, 40, 3 (2001), 239–245.

43. Fuller, C.M.; Biros, D.P.; and Wilson, R.L. Decision support for determining veracity via linguistic-based cues. Decision Support Systems, 46, 3 (2009), 695–703.

44. Gabrieli, J.D.E.; Desmond, J.E.; Demb, J.B. et al. Functional magnetic resonance imaging of semantic memory processes in the frontal lobes. Psychological Science, 7 (1996), 278–283.

45. Gamer, M.; Rill, H.G.; Vossel, G.; and Gödert, H.W. Psychophysiological and vocal measures in the detection of guilty knowledge. International Journal of Psychophysiology, 60, 1 (2006), 76–87.

46. Gardner, R.M.; Beltramo, J.S.; and Krinsky, R. Pupillary changes during encoding, storing, and retrieval of information. Perceptual and Motor Skills, 41, 3 (1975), 951–955.

47. Gati, I., and Ben-Shakhar, G. Novelty and significance in orientation and habituation : A feature-matching approach. Journal of Experimental Psychology-General, 119, 3 (1990), 251–263.

48. Gray, J.A. The Psychology of Fear and Stress. 2nd ed. Cambridge: Cambridge University Press, 1988.

49. Gregor, S., and Hevner, A.R. Positioning and presenting design science research for maximum impact. MIS Quarterly, 37, 2 (2013), 337–355.

50. de Guinea, A.O., and Markus, L. Why break the habit of a lifetime? Rethinking the roles of intention, habit, and emotion in continuing information technology use. MIS Quarterly, 33, 3 (2009), 433–444.

51. de Guinea, A.O.; Titah, R.; and Leger, P.M. Explicit and implicit antecedents of users’ behavioral beliefs in information systems: A neuropscyhological investigation. Journal of Management Information Systems, 30, 4 (2014), 179–209.

52. Hannula, D.E.; Althoff, R.R.; Warren, D.E.; Riggs, L.; Ryan, J.D.; and Cohen, N.J. Worth a glance: Using eye movements to investigate the cognitive neuroscience of memory. Frontiers in Human Neuroscience, 4, 166 (2010), 1–16.

53. Harnsberger, J.D.; Hollien, H.; Martin, C.A.; and Hollien, K.A. Stress and deception in speech: Evaluating layered voice analysis. Journal of Forensic Sciences, 54, 3 (2009), 642–650.

54. Heaver, B. Psychophysiological indices of recognition memory. Dissertation at the University of Sussex, 2012.

55. Hevner, A.R.; March, S.T.; Park, J.; and Ram, S. Design science in information systems research. MIS Quarterly, 28, 1 (2004), 75–105.

56. Hira, S., and Furumitsu, I. Polygraphic examinations in Japan: Application of the guilty knowledge test in forensic investigations. International Journal of Police Science and Management, 4 (2002), 16–27.

57. Hock, H.; Daniels, L.; and Nichols, D. The effect of spatial attention on pupil dynamics. Journal of Vision, 10, 7 (2010), 87.

58. Honts, C.R.; Amato, S.L.; and Gordon, A.K. Effects of spontaneous countermeasures used against the comparison question test. Polygraph, 30, 1 (2001), 1–9.

59. Honts, C.R.; Devitt, M.K.; Winbush, M.; and Kircher, J.C. Mental and physical countermeasures reduce the accuracy of the concealed knowledge test. Psychophysiology, 33, 1 (1996), 84–92.

60. Honts, C.R.; Hodes, R.L.; and Raskin, D.C. Effects of physical countermeasures on the physiological detection of deception. Journal of Applied Psychology, 70, 1 (1985), 177–187.

61. Honts, C.R., and Kircher, J.C. Mental and physical countermeasures reduce the accuracy of polygraph tests. Journal of Applied Psychology, 79, 2 (1994), 252–259.

62. Hwang, M.Y.; Hong, J.C.; Cheng, H.Y.; Peng, Y.C.; and Wu, N.C. Gender differences in cognitive load and competition anxiety affect 6th grade students’ attitude toward playing and intention to play at a sequential or synchronous game. Computers and Education, 60, 1 (2013), 254–263.

63. Janisse, M.P. Pupillometry: The Psychology of the Pupillary Response. Washington, DC: Hemisphere, 1977.

64. Janisse, M.P., and Bradley, M.T. Deception, information and the pupillary response. Perceptual and Motor Skills, 50, 3 (1980), 748–750.

65. Janz, N.K., and Becker, M.H. The health belief model: A decade later. Health Education and Behavior, 11, 1 (1984), 1–47.

66. Jensen, M.L.; Lowry, P.B.; and Jenkins, J.L. Effects of automated and participative decision support in computer-aided credibility assessment. Journal of Management Information Systems, 28, 1 (2011), 203–236.

67. Kircher, J.C., and Raskin, D.C. Human versus computerized evaluations of polygraph data in a laboratory setting. Journal of Applied Psychology, 73, 2 (1988), 291–302.

68. Kleiner, M. Handbook of Polygraph Testing. London: Academic Press, 2002.

69. Krapohl, D.J.; McCloughlan, J.B.; and Senter, S.M. How to use the concealed information test. Polygraph, 35, 3 (2009), 34–49.

70. Kuo, F.; Hsu, C.; and Day, R. An exploratory study of cognitive effort involved in decision under framing: An application of the eye-tracking technology. Decision Support Systems, 48, 1 (2009), 81–91.

71. Leal, S., and Vrij, A. The occurrence of eye blinks during a guilty knowledge test. Crime and Law, 16, 4 (2010), 349–357.

72. Lee, J., and Ahn, J. Attention to banner ads and their effectiveness: An eye-tracking approach. International Journal of Electronic Commerce, 17, 1 (2012), 119–137.

73. Leger, P.M.; Senecal, S.; Courtemanche, F. et al. Precision is in the eye of the beholder: Application of eye fixation-related potentials to information systems research. Journal of the Association for Information Systems, 15, 10 (2014), 651–678.

74. Lubow, R.E., and Fein, O. Pupillary size in response to a visual guilty knowledge test: New technique for the detection of deception. Journal of Experimental Psychology-Applied, 2, 2 (1996), 164–177.

75. Lykken, D.T., and Venables, P.H. Direct measurement of skin conductance: A proposal for standardization. Psychophysiology, 8, 5 (1971), 656–672.

76. Matsuda, I.; Nittono, H.; and Allen, J.J.B. The current and future status of the concealed information test for field use. Frontiers in Psychology, 3 (2012), 1–11.

77. Maw, N.N., and Pomplun, M. Studying human face recognition with the gaze-contingent window technique. In Proceedings of the Twenty-Sixth Annual Meeting of the Cognitive Science Society. Chicago, IL, August 4–7, 2004, pp. 927–932.

78. McArdle, J.J., and Nesselroade, J.R. Growth curve analysis in contemporary psychological research. In J. Schinka and W. Velicer (eds.), Comprehensive Handbook on Psychology: Research Methods in Psychology. New York: Wiley, 2003, pp. 447–480.

79. Miller, G.R., and Stiff, J.B. Deceptive Communication. Newbury Park, CA: Sage, 1993.

80. Nunamaker, J.F., Jr.; Derrick, D.C.; Elkins, A.C.; Burgoon, J.K.; and Patton, M.W. Embodied conversational agent-based kiosk for automated interviewing. Journal of Management Information Systems, 28, 1 (2011), 17–48.

81. O’Gorman, J.G. The orienting reflex: Novelty or significance? Psychophysiology, 16, (1979), 253–262.

82. Pak, J., and Zhou, L. Eye movements as deception indicators in online video chatting. In Proceedings of the Americas Conference on Information Systems. Detroit, MI, August 4–8, 2011.

83. Pollina, D.A.; Dollins, A.B.; Senter, S.M.; Krapohl, D.J.; and Ryan, A.H. Comparisons of polygraph data obtained from individuals involved in mock crimes and actual criminal investigations. Journal of Applied Psychology, 89, 6 (2004), 1099–1105.

84. Proudfoot, J.G.; Boyle, R.J.; and Schuetzler, R. Man vs. machine: Investigating the effects of adversarial system use on end-user behavior in automated deception detection interviews. Decision Support Systems, 85 (2016), 23–33.

85. Proudfoot, J.G.; Twyman, N.W.; and Burgoon, J.K. Eye tracking and the CIT: Utilizing oculometric cues to identify familiarity with wanted persons. In Forty-Sixth Annual Hawaii International Conference on System Sciences. Maui, January 7–10, 2013, pp. 75–84.

86. Rauniar, R.; Rawski, G.; Yang, J.; and Johnson, B. Technology acceptance model (TAM) and social media usage: An empirical study on Facebook. Journal of Enterprise Information Management, 27, 1 (2014), 6–30.

87. Rockwell, P.; Buller, D.B.; and Burgoon, J.K. Measurement of deceptive voices: Comparing acoustic and perceptual data. Applied Psycholinguistics, 18, 4 (1997), 471–484.

88. Roelofs, K.; Hagenaars, M.A.; and Stins, J. Facing freeze: Social threat induces bodily freeze in humans. Psychological Science, 21, 11 (2010), 1575–1581.

89. Ryan, J.D.; Hannula, D.E.; and Cohen, N.J. The obligatory effects of memory on eye movements. Memory, 15, 5 (2007), 508–525.

90. Saxe, L., and Ben-Shakhar, G. Admissibility of polygraph tests: The application of scientific standards post-Daubert. Psychology, Public Policy, and Law, 5, 1 (1999), 203–223.

91. Saxe, L.; Dougherty, D.; and Cross, T. The validity of polygraph testing: Scientific analysis and public controversy. American Psychologist, 40, 3 (1985), 355.

92. Schwedes, C., and Wentura, D. The revealing glance: Eye gaze behavior to concealed information. Memory and Cognition, 40, 4 (2012), 642–651.

93. Serota, K.B.; Levine, T.R.; and Boster, F.J. The prevalence of lying in America: Three studies of reported deception. Human Communication Research, 36, 1 (2010), 2–25.

94. Simon, H.A. Rational choice and the structure of the environment. Psychological Review, 63, 2 (1956), 129–138.

95. Simpson, H.M., and Molloy, F.M. Effects of audience anxiety on pupil size. Psychophysiology, 8, 4 (1971), 491–496.

96. Sokolov, E.N. Neuronal models and the orienting influence. In M.A. Brazier (ed.), The Central Nervous System and Behavior. New York: Macy Foundation, 1960, pp. 187–276.

97. Sokolov, E.N. Higher nervous functions: Orienting reflex. Annual Review of Physiology, 25, 1 (1963), 545–580.

98. Sokolov, E.N. Perception and the Conditioned Reflex. New York: Macmillan, 1963.

99. Sorebo, O., and Eikebrokk, T.R. Explaining IS continuance in environments where usage is mandatory. Computers in Human Behavior, 24, 5 (2008), 2357–2371.

100. Todd, P., and Benbasat, I. Process tracing methods in decision support systems research: Exploring the black box. MIS Quarterly, 11, 4 (1987), 493–514.

101. Twyman, N.W.; Burgoon, J.K.; Elkins, A.C.; and Proudfoot, J.G. Alternative cues in concealed information testing. In Forty-Sixth Annual Hawaii International Conference on System Sciences. Maui, January 7–10, 2013, pp. 51–59.

102. Twyman, N.W.; Elkins, A.C.; Burgoon, J.K.; and Nunamaker, J.F., Jr. A rigidity detection system for automated credibility assessment. Journal of Management Information Systems, 31, 1 (2014), 173–201.

103. Twyman, N.W.; Lowry, P.B.; Burgoon, J.K.; and Nunamaker, J.F., Jr. Autonomous scientifically controlled screening systems for detecting information purposefully concealed by individuals. Journal of Management Information Systems, 31, 3 (2014), 106–137.

104. Twyman, N.W.; Proudfoot, J.G.; Schuetzler, R.; Elkins, A.C.; and Derrick, D.C. Robustness of multiple indicators in automated screening systems for deception detection. Journal of Management Information Systems, 32, 4 (2015), 215–245.

105. Twyman, N.W.; Schuetzler, R.; Proudfoot, J.G.; and Elkins, A.C. A systems approach to countermeasures in credibility assessment interviews. In International Conference on Information Systems. Milan, December 15–18, 2013.

106. Venkatesh, V.; Morris, M.G.; Davis, G.B.; and Davis, F.D. User acceptance of information technology. MIS Quarterly, 27, 3 (2003), 425–478.

107. Venkatesh, V.; Thong, J.Y.L.; and Xu, X. Consumer acceptance and use of information technology: Extending the unified theory of acceptance and use of technology. MIS Quarterly, 36, 1 (2012), 157–178.

108. Vrij, A. Why professionals fail to catch liars and how they can improve. Legal and Criminological Psychology, 9 (2004), 159–181.

109. Vrij, A.; Oliveira, J.; Hammond, A.; and Ehrlichman, H. Saccadic eye movement rate as a cue to deceit. Journal of Applied Research in Memory and Cognition, 4, 1 (2015), 15–19.

110. Wagner, A.D.; Desmond, J.E.; Demb, J.B.; and Gabrieli, J.D.E. Semantic repetition priming for verbal and pictorial knowledge: A functional MRI study of left interior prefrontal cortex. Journal of Cognitive Neuroscience, 9, 6 (1997), 714–726.

111. Wang, Q.; Yang, S.; Liu, M.; Cao, Z.; and Ma, Q. An eye-tracking study of website complexity from cognitive load perspective. Decision Support Systems, 62 (2014), 1–10.

112. Webb, A.K.; Hacker, D.J.; Osher, D. et al. Eye movements and pupil size reveal deception in computer administered questionnaires. In D.D. Schmorrow, I.V. Estabrooke, and M. Grootjen (eds.), Foundations of Augmented Cognition. Neuroergonomics and Operational Neuroscience. Berlin: Springer, 2009, pp. 553–562.

113. Webb, A.K.; Honts, C.R.; Kircher, J.C.; Bernhardt, P.; and Cook, A.E. Effectiveness of pupil diameter in a probable-lie comparison question test for deception. Legal and Criminological Psychology, 14 (2009), 279–292.

114. Wolpe, P.R.; Foster, K.R.; and Langleben, D.D. Emerging neurotechnologies for liedetection: Promises and perils. American Journal of Bioethics, 5, 2 (2005), 39–49.

115. Wright, R., and Marett, K. The influence of experiential and dispositional factors in phishing: An empirical investigation of the deceived. Journal of Management Information Systems, 27, 1 (2010), 273–303.

116. Ye, Q.; Cheng, Z.; and Fang, B. Learning from other buyers: The effect of purchase history records in online marketplaces. Decision Support Systems, 56 (2013), 502–512.

117. Yokoi, Y.; Okazaki, Y.; Kiriu, M.; Kuramochi, T.; and Ohama, T. The validity of the guilty knowledge test used in field cases. Japanese Journal of Criminal Psychology, 39, 1 (2001), 15–27.

118. Zhang, X. The evolution of polygraph testing in the People’s Republic of China. Polygraph, 40, 3 (2011), 181–193.

119. Zhou, L.; Burgoon, J.K.; Nunamaker, J.F., Jr.; and Twitchell, D. Automating linguistics-based cues for detecting deception in text-based asynchronous computer-mediated communications. Group Decision and Negotiation, 13, 1 (2004), 81–106.

120. Zhou, L.; Burgoon, J.K.; Twitchell, D.P.; Qin, T.; and Nunamaker, J.F., Jr. A comparison of classification methods for predicting deception in computer-mediated communication. Journal of Management Information Systems, 20, 4 (2004), 139–165.
