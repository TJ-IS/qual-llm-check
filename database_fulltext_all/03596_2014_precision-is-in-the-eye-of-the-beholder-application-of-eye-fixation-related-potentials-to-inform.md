---
otero_id: 3596
otero_key: "66YKUUR5"
title: "Precision is in the Eye of the Beholder: Application of Eye Fixation-Related Potentials to Information Systems Research"
authors: "Pierre-Majorique Léger; Sylvain Sénecal; François Courtemanche; Ana Guinea; Ryad Titah; Marc Fredette; Élise Labonte-LeMoyne"
year: "2014"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00376"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Volume 15 Issue 10 Special Issue on Methods, Tools, and Measurement in NeurolS Research

10-20-2014

# Precision is in the E   ye of the Beholder: Application of E     ye Fixation- - Related Potentials to Information Systems Research

Pierre-Majorique Léger , pml@hec.ca

Sylvain Sénecal , sylvain.senecal@hec.ca

François Courtemanche , francois.courtemanche@hec.ca

Ana Ortiz de Guinea , ana.ortiz-de-guinea@hec.ca

Ryad Titah , ryad.titah@hec.ca

See next page for additional authors

Follow this and additional works at: https://aisel.aisnet.org/jais

## Recommended Citation

Léger, Pierre-Majorique; Sénecal, Sylvain; Courtemanche, François; Ortiz de Guinea, Ana; Titah, Ryad; Fredette, Marc; and Labonte-LeMoyne, Élise (2014) "Precision is in the Eye of the Beholder: Application of Eye Fixation-Related Potentials to Information Systems Research," , 15(10), . DOI: 10.17705/1jais.00376 Available at: https://aisel.aisnet.org/jais/vol15/iss10/3

This material is brought to you by the AIS Journals at AIS Electronic Library (AISeL). It has been accepted for inclusion in Journal of the Association for Information Systems by an authorized administrator of AIS Electronic Library (AISeL). For more information, please contact elibrary@aisnet.org.

Precision is in the E   ye of the Beholder: Application of E    ye Fixation-Related Potentials to Information Systems Research

Authors Pierre-Majorique Léger, Sylvain Sénecal, François Courtemanche, Ana Ortiz de Guinea, Ryad Titah, Marc Fredette, and Élise Labonte-LeMoyne

# Journal of the Asşociation for Information Systems JAIS

Special Issue

# Precision is in the Eye of the Beholder: Application of Eye Fixation-Related Potentials to Information Systems Research

Pierre-Majorique Léger HEC Montréal pml@hec.ca

Sylvain Sénecal HEC Montréal sylvain.senecal@hec.ca

Ryad Titah HEC Montréal ryad.titah@hec.ca

Marc Fredette HEC Montréal marc.fredette@hec.ca

François Courtemanche HEC Montréal francois.courtemanche@hec.ca

Élise Labonte-LeMoyne HEC Montréal elise.labonte-lemoyne@umontreal.ca

Ana Ortiz de Guinea HEC Montréal ana.ortiz-de-guinea@hec.ca

## Abstract

This paper introduces the eye-fixation related potential (EFRP) method to IS research. The EFRP method allows one to synchronize eye tracking with electroencephalographic (EEG) recording to precisely capture users neural activity at the exact time at which they start to cognitively process a stimulus (e.g., event on the screen). This complements and overcomes some of the shortcomings of the traditional event related potential (ERP) method, which can only stamp the time at which a stimulus is presented to a user. Thus, we propose a method conjecture of the superiority of EFRP over ERP for capturing the cognitive processing of a stimulus when such cognitive processing is not necessarily synchronized with the time at which the stimulus appears. We illustrate the EFRP method with an experiment in a natural IS use context in which we asked users to read an industry report while email pop-up notifications arrived on their screen. The results support our proposed hypotheses and show three distinct neural processes associated with 1) the attentional reaction to email pop-up notification, 2) the cognitive processing of the email pop-up notification, and 3) the motor planning activity involved in opening or not the email. Furthermore, further analyses of the data gathered in the experiment serve to validate our method conjecture about the superiority of the EFRP method over the ERP in natural IS use contexts. In addition to the experiment, our study discusses important IS research questions that could be pursued with the aid of EFRP, and describes a set of guidelines to help IS researchers use this method.

Keywords: Eye Fixation-Related Potential, EFRP, Event Related Potential, ERP, Electroencephalography, Eyetracking, NeuroIS, IT Use, IT impact, IS Methods.

\* Alan Hevner was the accepting senior editor. This article was submitted on 30th April 2013 and went through two revisions.

Volume 15, Special Issue, pp. 651-678, October 2014

# Precision is in the Eye of the Beholder: Application of Eye Fixation-Related Potentials to Information Systems Research

## 1. Introduction

The recent introduction of Neuroscience methods to Information Systems (IS) research holds the promise of allowing a more complete view of IS by fostering novel insights and ways of investigating IS phenomena (Dimoka, Pavlou, & Davis, 2011; Loos et al., 2010; Riedl et al., 2010). With the introduction of these methods to IS research, guidelines on how to use these tools to answer important research questions have started to emerge (e.g., fMRI use guidelines by Dimoka (2012)).

With this paper, we contribute to the development of the NeuroIS field by providing guidelines on how to use eye fixation-related potential (EFRP) with an example illustrating its relevance for investigating IS use during natural interactions with technology. Thus, this paper introduces a technique called EFRP, which allows, in single trial electroencephalographic (EEG) recordings, the use of eye fixations as natural stamps to time lock the evoked potential of recurring information technology (IT) events (Hutzler et al., 2007).

EEG records, with high temporal precision, the electrical activity of neurons in the brain’s cortex (Pizzagalli, Oakes, Davidson, 2003). However, because EEG represents a conglomeration of a large number of neural sources of activity, the action of isolating and identifying specific neuro-cognitive processes during a continuous EEG recording is difficult (Luck, 2005). Thus, in order to analyze the specific neural responses to events (e.g., the display of a picture), a technique called event-related potential (ERP) is often employed (Luck, 2005). ERP relies on presenting a stimulus to participants multiple times (up to several hundred times in order to obtain an appropriate signal to noise ratio). With high temporal precision (in milliseconds), the neural responses to “noticing” the stimulus (using EEG) are then averaged and contrasted (Luck, 2005).

The ERP method has been widely used in the fields of psychology and neuropsychology (Luck, 2005). However, although useful in those fields, this technique has two major shortcomings for its application in IS research. First, the ERP technique stamps the time at which the stimulus is “presented” to the participant (e.g., when the participant “notices” the stimulus), not the time at which the participant “processes” or “attends” to the stimulus. Second, the ERP technique cannot stamp or mark the time at which the participant no longer attends to (or discards) the stimulus. For example, in the context of IT use, users usually juggle between multiple applications at the same time (e.g., Microsoft Word, SAP, Lotus Notes, and Microsoft Outlook): one may be writing a report as pop-up windows appear notifying that emails are being received. Therefore, the traditional ERP approach does not allow studying the evoked potential of attending to (e.g., reading an email notification) and discarding natural occurring events while performing tasks with the aid of a computer.

In order to overcome this problem, we propose an eye fixation-related potential (EFRP) method to study IS use (Hutzler et al., 2007). This method can overcome the shortcomings presented above. First, this technique allows stamping the time at which the stimulus is cognitively processed by the participant, rather than the time at which the stimulus is presented to the participant, by using eye tracking (Nikolaev, Nakatani, Plomp, Jurica, & van Leeuwen, 2011). For example, researchers have used EFRP to investigate natural reading by time-locking the analysis on word fixation rather than the time at which words appear (Dimigen, Sommer, Hohlfeld, Jacobs, & Kliegl, 2011). Because the eyetracking device is synchronized with the EEG recording, it automatically stamps the time at which the participant starts to visually attend to a stimulus, hence providing a greater temporal precision to the measurement of neural activity associated with stimulus processing (Kamienkowski, Ison, Quiroga, & Sigman, 2012). Second, this method allows to timestamp the transitions between presenting an event (e.g., an email notification), attending to the event (e.g., reading the email notification), and returning to the previous computer task.

Our paper demonstrates the EFRP method in an IS use context. More specifically, after a succinct literature review, we posit a method conjecture arguing for the superiority of the EFRP method over ERP in capturing the users’ neural activity that follows from attending to a given stimulus during IS use. We illustrate this with an experiment investigating the neural reactions to the arrival and evaluation of emails during an IT task, and participants’ transitions between the IT task and the emails. That is, while participants perform a primary task with the aid of a computer, they need to decide whether to open incoming emails that appear on the screen by clicking on the email pop-up notification if they believe that the email is relevant to the task at hand. The time at which participants attend to the stimulus is stamped with the help of an eye-tracking device. Evoked potential is used to analyze brain activity associated with: a) the time at which the stimulus is presented (the ERP method) (when users notice the email notification), b) the time at which participants attend to the stimulus (the EFRP method) (when users read the email notification), and c) the time at which participants plan the action of opening or not the email (the ERP method) (when users open or close the email notification). After testing the hypothesized neural activity associated with a), b), and c), we validate our method conjecture by showing that the neural activity associated with b) cannot be found without EFRP by applying the ERP method alone.

The paper contributes to the IS literature in several ways. First and most importantly, it proposes a method that allows observing and assessing the “direct and unmediated effect” of IT on individuals cognitions (Ortiz de Guinea & Webster, 2013; Ortiz de Guinea & Markus, 2009; Silva, 2007). Note that such a link could not be directly established with traditional measurement tools such as selfreported questionnaires, where the effect of IT could only be observed via the prism of individual perceptions (Ortiz de Guinea & Markus, 2010). As such, EFRP allows one to unequivocally and precisely observe the effect of IT on neural activity, and this can then be linked to perceptions and behaviors in a natural IS use context. Second, the paper explains the methodological implications related to using EFRP in NeuroIS research and presents guidelines for the use of this technique in IS research. Finally, since a method is only useful if it can answer important questions for research, the paper discusses the IS areas and research questions that this method can contribute to answer. For instance, task interruption messages such as mobile device push notifications (i.e., reminders, incoming calls, or alerts), pop-up web advertisements, and IT interruptions are all potential IS research contexts in which the EFRP method could be used to gain a deeper understanding of the underlying cognitive phenomena at play.

The rest of the paper is organized as follows. In Section 2, we present our literature review on ERP and EFRP with a special emphasis on how the EFRP method can overcome the shortcomings of the traditional ERP method for the study of IS use as it occurs naturally. In Sections 3 and 4, we present and analyze an illustrative experiment investigating neural reactions during IS use with the use of both ERP and EFRP. In Section 5, we discuss the contributions of the EFRP method to IS research and the type of research questions the EFRP method can answer. Finally, in Section 6, we present guidelines of how to use EFRP in IS research.

## 2. Literature review

## 2.1. Event Related Potential (ERP)

Electroencephalography (EEG) unlike other more obtrusive methods (e.g., fMRI) offers NeuroIS researchers the possibility of measuring human brain activity during ecologically valid interactions with IT; that is, while users interact with an IT in a more natural setting.

EEG is a tool available to neuroscientists to measure brain activity in the cerebral cortex (Pizzagalli et al., 2003). More specifically, using electrodes placed on the scalp, EEG measures, with a very high temporal precision, the summation of synchronous postsynaptic potentials. In order to be able to record an electrical signal at the scalp level, a large number of neurons must fire at the same time and they must be spatially aligned for the dipoles to summate. Because electricity travels almost at the speed of light, The general assumption of this methodology is that there is only a microscopic delay (below the millisecond level) between the brain activity and what is being recording by the electrode (Luck, 2005).

However, because EEG represents the summation of a large amount of neural sources of activity, the action of isolating and identifying specific neurocognitive processes during a continuous recording is difficult (Luck, 2005). To circumvent this problem, researchers in neuroscience use a technique called event related potential (ERP). An ERP is a patterned voltage fluctuation in the EEG signal that represents a cognitive process in response to a discrete event. To derive the ERP, voltage fluctuations must be locked to a precise temporal marker associated with the event. ERPs have low voltage amplitude compared to the rest of the EEG signals and other sources of noise such as muscle movement and cardiac activity. As such, they are difficult to observe if the background EEG activity is not filtered out. To improve identification of ERPs, multiple trials are needed to average responses and filter out noise. In other words, ERP relies on the presentation of a stimulus (event) to participants on multiple occasions. The basic assumption is that if a predictable brain activity happens on every trial, it will elicit an observable pattern of fluctuations in the average EEG signal. The cognitive response to every trial generates a detectable invariant neural signature time locked to the event. Assuming that, given a sufficient number of trials, the background EEG signal is independent from this process and is randomly distributed, the signal-to-noise ratio will increase and the unsystematic noise will be filtered out (see Figure 1).

![](/api/attachments/66YKUUR5/fulltext/images/ed900d3c15ef44ffcc6f684eb83db299204f6efcf1aaeba527a06d285efad761.jpg)

The ERP approach works well only if the investigated phenomenon is phase-locked with the stimulus. Thus, ERP performs well when both the event and associated neural activity are synchronized (e.g., presenting an email notification and noticing this notification). However, if the neural activity associated with the specific information processing of the stimulus (e.g., reading an email notification) is not in phase with the stimulus presentation (e.g., appearance of an email notification) (i.e., if “eventrelated oscillations […] are not strongly synchronized with the moment of stimulus delivery”), they will be cancelled out by the average, and will virtually disappear (Kolev & Yordanova, 1997, p. 229). The same signal cancelation will occur if the time stamp of the stimulus is not imported with high temporal precision in the EEG data at the time the stimulus is presented (due to integration issues). In such a case, the neural activity that is elicited by the stimulus is averaged out because the marker is incorrectly time-locked (Luck, 2005).

## Figure 1. The Event Related Potential (ERP) technique<sup>1</sup>

An ERP approach permits one to investigate how users react to notifications because the event (e.g., an email pop-up notification) is synchronized with their cognitive response (e.g., noticing the notification). However, all users would probably not process its content (e.g., reading the subject of the email) at the exact same time. While some users would process its content immediately, some would process it at a later time, and finally others would probably not process it at all. As such, an

ERP approach would not allow one to investigate the neural activity involved in the email pop-up notification content processing because it would not be synchronized with the appearance of the event<sup>2</sup>. Therefore, the ERP approach is only suitable to address IS research questions where the event and the neural activity under investigation are in phase. If the presentation of the event and the processing of the stimuli during a natural IT task do not take place at the same time, the traditional ERP technique will fail to elicit the evoked potential of the cognitive process, which limits its usefulness in investigating many IS phenomena. That is, ERP can capture the neural activity associated with noticing an event, but not the neural activity associated with attending/processing to the event when such attending/processing is not necessarily synchronized with event presentation. For reasons of simplicity, throughout the paper, we refer to the neural activity following noticing the occurrence of an event as “stimulus reaction”, and to the neural activity following the attending to such event as “stimulus processing.”

## 2.2. Eye Fixation Related Potential (EFRP)

Eye fixation related potential (EFRP) is a method that combines eye-tracking and traditional ERP in order to observe event processing in response to eye fixation. In contrast to ERP, which time locks the brain activity to stimulus presentation, EFRP time locks the brain activity to eye fixation. That is, when people focus on the stimulus.

Fixation is important for humans to thoroughly encode visual information: “the longer an object is fixated the more likely it is to be encoded” (Nikolaev et al., 2011, p. 1598). Thus, successful encoding requires attention. Moore (2006) suggests that selective attention and eye movement involve overlapping neural mechanisms. Therefore, one useful alternative to the traditional ERP method is to analyze the electrical brain activity recordings segmented relative to eye fixations (Nikolaev et al., 2011). This requires a precise integration of eye tracking and EEG data in order to conduct valid and reliable EFRP analyses. First, the precise occurrence of prolonged eye fixations in the areas of interest must be identified. Then, these fixation markers must be inserted in the EEG data at the exact time the fixations occurred. Such integration requires a specific architecture that we describe in Section 6 Table 1 summarizes the differences between the ERP and EFRP methods.

<table><tr><td colspan="4">Table 1. Main Differences Between ERP and EFRP Methods</td></tr><tr><td colspan="2">Characteristics</td><td>ERP</td><td>EFRP</td></tr><tr><td>1.</td><td>Stimuli</td><td>Exogenous stimuli</td><td>Endogenous and exogenous stimuli</td></tr><tr><td>2.</td><td>Marker for EEG analysis</td><td>At the time of stimulus presentation</td><td>At the time of a prolonged eye-fixation in the area of interest</td></tr><tr><td>3.</td><td>Software, device, and integration</td><td>Integration between the stimulus presentation software and EEG systems</td><td>Integration between the eye-tracking device and EEG systems</td></tr></table>

The main advantage of EFRP over traditional ERP is the possibility to investigate cognitive mechanisms in a more natural setting. For example, Dimigen et al. (2011) used an EFRP method to investigate word predictability during a natural reading episode. Using a traditional ERP approach, this type of research would have involved a word-by-word stimuli presentation where participants constantly fixate the center of the screen in order to time lock the presentation of the stimulus with specific word evoked potential. In contrast, by using EFRP, participants were allowed to freely move their eyes over the text (as it occurs in a natural reading context) and evoked potentials were time locked over fixations on specific words. Kamienkowki et al. (2012) also used EFRP to replicate a standard experimental protocol (e.g., oddball paradigm) in a less restrictive manner, and were able to distinguish between target and distractor components while participants freely explored visual stimuli. Though EFRP has mainly been used in psycholinguistic studies (Baccino, 2011; Sereno & Rayner,

2003) where it has been shown to be as reliable as traditional ERP (Hutzler et al., 2007), it has recently started to be used in other fields. For example, in a recent study, Takeda et al. (2012) used EFRP to assess drivers’ attentional workload. Another study by Rämä and Baccino (2010) explored the use of EFRP during object identification.

We contend that the EFRP method provides a greater temporal precision for measuring neural reactions involved in event processing in natural IS settings. As such, it opens the possibility of investigating repetitive events occurring in natural interactions with an IT artifact. We therefore advance the following general method conjecture:

In a multiple stimuli context such as IS use, the EFRP method is more precise than the ERP method in capturing a users’ neural activity associated with stimulus processing when such processing does not necessarily occur at the same time as stimulus presentation.

Validating our general conjecture first requires testing three formal hypotheses related to the user’s 1) reaction to the presentation of a stimulus, 2) processing of the stimulus, and 3) behavioral planning response to a stimulus. These hypotheses are explained in Section 3. Furthermore, after developing the three hypotheses, we revisit and provide more precision to our conjecture about EFRP vs. ERP as it applies to the specific context of the study. Finally, we complement the test of these three hypotheses with a general validation of our main method conjecture as described in Section 4.

## 3. Demonstration of the EFRP Method Through an Illustrative Experiment

We designed and conducted an experiment to illustrate the use of the EFRP method in an IS context. The experiment depicts participants’ neural reactions at three different times while using an IS to perform a task: 1) when receiving an email notification, 2) while attending to the email notification, and 3) while deciding whether to open the email or not. During the experiment, participants received email notifications while performing a primary task with the aid of a computer. On receiving the email notification, they had to decide whether to open (or close) the email by clicking on the email pop-up notification if they believed that the email was (or was not) relevant to the task at hand.

In Section 3.1, we advance three formal hypotheses that provide a specific context to our main method conjecture. Specifically, our hypotheses concern the three times at which the EEG signal was contrasted: 1) the time at which the stimulus was presented (i.e., email pop-up notification event), or stimulus onset (T1, ERP method); 2) the time at which participants fixated the stimulus in order to process it, or fixation onset (T2, EFRP method); and 3) the time at which participants clicked on the email notification to open or not the actual email, or response onset (T3, ERP method). In Section 3.2, we then apply our method conjecture to the illustrative study’s context and posit (and demonstrate) that the cognitive processing detected at T2 with the EFRP method cannot be found by only applying the ERP method alone.

## 3.1 Hypotheses Development

## 3.1.1. Stimulus Reaction: Bottom-up Attentional Process

Attention is a critical cognitive process that guides our perception and actions on a daily basis (Posner, 2012). Attention is the “the act of restricting mental activity to consideration of only a small subset of the stimuli in the environment or a limited range of potential mental contents” (Parasuraman & Rizzo, 2008, p. 389). Past research has shown that attention control can either be driven by topdown (i.e., directed by executive attention) or bottom-up cognitive processes (i.e., exogenous or stimulus driven) (Posner & Petersen, 1990). In an IS context, a user looking for (or at) a system feature from a given list would entail a top-down attentional control process because sequential processing is required to consider available options, while a user receiving an error message from a system would entail a bottom-up attentional control process because the attention of the user is drawn to this unexpected stimulus. These two systems involve different distributed neural networks.

Top-down attention involves the frontal cortex and basal ganglia regions, while bottom-up attention activates the parietal and temporal regions of the cortex (Buschman & Miller, 2007).

Given its ability to covertly monitor cognitive processing with very high temporal precision, the ERP technique has been widely used to study attention (Luck, 2005). As numerous studies have demonstrated, the presentation of an unpredictable but recognizable stimulus generates a bottom-up attentional process characterized by an ERP with a specific positive pattern in a time window of 300 to 800 milliseconds (ms) after the presentation of the stimulus onset (Duncan et al., 2009). The amplitude and latency of this peak, referred to as a P300 component, varies with task conditions, individual differences such as age, and stimulus modality (Polich, 2007). The P300 component increases in magnitude from the frontal to parietal electrode sites (Bledowski et al., 2004), which is congruent with studies showing that the parietal cortex is involved in the orientation of attention toward a stimulus (Corbetta, Kincade, Ollinger, McAvoy, & Shulman, 2000). The P300 component voltage fluctuation has been found to be associated with a bottom-up attentional process (Hopfinger & Park, 2012). As such, we propose:

H1: At stimulus onset (i.e., pop-up notification) (T1), a bottom-up attentional process (i.e., P300 component) is observed.

## 3.1.2. Stimulus Processing: Processing of a Text Stimulus (Language Processing)

An important neuroscience stream of research applied to psycholinguistics investigates how the brain processes and produces language and communication (Ahlsén, 2006). In this stream of research, neuroanatomical studies have shown that: a) the inferior frontal gyrus in the left hemisphere—known as Broca’s area (BA 44 and 45)—is associated with language production, and b) the left superior temporal gyrus—known as Wernicke's area (BA 22)—is associated with understanding language (Gazzaniga, 2004). More recent studies have further shown that Broca’s area is also involved in language comprehension in the context of complex or ambiguous sentences (Grewe et al., 2005; Skipper, Goldin-Meadow, Nusbaum, & Small, 2007).

In order to demonstrate the presence of a language-specific cortical activity, the N400 component, which is a negative waveform peak voltage fluctuation of the EEG signal, is considered to be among the most reliable indicators of such activity based on studies related to word recognition and semantic processing. Several studies have shown that the N400 component wave peaks in the 200–600 ms interval for visually presented material (Kutas & Federmeier, 2011). This negative variation in potential is detected in the centro-parietal sites (near Pz) with small right laterality and is observed when a word is identified at the point of semantic access (Luck, 2005). For example, a N400 component is observed in the case of semantically mismatching words in a sentence (Kutas & Federmeier, 2011). Several studies have also shown that the N400 amplitude is associated with levels of difficulty in retrieving the meaning of stimuli such as words or pictures and sounds (e.g., Thornhill & Van Petten, 2012).

To summarize, numerous studies have demonstrated that the N400 component is a clear indicator of language-specific cortical activity and shows how various cognitive processes such as perception, attention, memory, and language are jointly involved in one’s ability to comprehend meaning (Kutas & Federmeier, 2011). As such, we propose:

## H2: At fixation onset (i.e., while attending to the email notification) (T2), a language cognitive process (i.e., N400 component) is observed.

## 3.1.3. Stimulus Behavioral Response: Motor Planning Process

Several regions of the brain are involved in motor (or movement) planning. The premotor area (PMA) controls the core muscle movement while the supplementary motor cortex (SMA) is involved in planning the movement before it occurs (Gazzaniga, 2004), and the posterior parietal cortex coordinates movement based on visual information (Gazzaniga, 2004). Movement results from conscious or unconscious decisions. In the case of a conscious decision such as opening an email, the neural pathways from prefrontal areas project signals via the basal ganglia (which acts as an inhibitory filter for inappropriate action) to the thalamus, which relays this information to the PMA and

SMA (Gazzaniga, 2004). Performance of the movement then involves the primary motor cortex and the cerebellum, which ensure the precise timing and duration of the action.

Readiness potential (RP), also known as Bereitschaftspotential (BP), measures the neural activity associated with planning voluntary motor movement. This activity is referred to as the movementrelated cortical potentials (MRCP), and can be measured with EEG from the motor cortex and the supplementary motor cortex (Hallett, 1994). MRCP is a type of ERP that measures the voltage difference associated with the neuronal activities related to preparing a movement. However, compared to a traditional ERP where the evoked potential is time locked on stimulus presentation, the analysis is response-locked to the actual physical movement of the participant (e.g., performing a mouse click). Two components can be measured in MRCP (Deecke, 1990): the first component occurs from 500 to 1200 ms before the response, and the second component occurs in the 500 ms prior to the onset of the response. Past research (e.g., Deecke, 1990) has demonstrated that the first component can be measured in the supplementary motor cortex, while the second component originates from the primary motor cortex (Brodmann area 4). For a finger movement in a computer interaction context, previous research has shown that the neural activity can be detected between 100 and 230 ms prior to action (Blankertz, Curio, & Muller, 2002). As such, we propose:

H3:Before response onset (i.e., while deciding whether to open or not the email) (T3), a motor planning process (i.e., BP component) is observed.

## 3.2. Application of the Method Conjecture Regarding EFRP vs. ERP

In Section 2, when summarizing the ERP and EFRP methods, we argue that the EFRP method is more precise than the ERP method in capturing a users’ neural activity associated with stimulus processing when such processing does not necessarily occur at the same time as stimulus presentation. After having developed the hypotheses relevant to our illustrative study, we now provide more accuracy about how this method conjecture applies to the study at hand. Our literature review suggests that ERP is an appropriate method for capturing users’ bottom-up attentional reaction to the presentation of an email pop-up notification (H1), and users’ motor planning cognitive response just before closing the email pop-up or opening the email (H3). That is, the ERP method is appropriate when a neural response (e.g., noticing and motor planning) is synchronized with a discrete event (e.g., appearance of email pop-up notification and opening/closing the email pop up notification), as it is the case for H1 and H3.

However, it is unlikely that users will read (or process) the content of the pop-up notification at the same time (e.g., read the subject of the email pop-up notification). That is, some users would decide to read the notification right away, while others would choose to read it at a later time, and others would probably not read it at all and just ignore it. This means that the reading of the email pop-up notification (stimulus) “does not occur” at the same time as the stimulus is presented on the screen for every individual. Thus, to time lock the time at which each individual processes (or reads) each email notification pop-up, the EFRP method is needed. As such, with the EFRP method, a marker is inserted in the EEG data at the exact time at which each a user fixates, for each email, their eyes to the email pop-up notification window for a certain time (see Section 3.3.5 for specific information about this) and thus reads or processes it. Thus, the EFRP method is appropriate when users’ neural processes (e.g., a language cognitive process indicated by an N400 component) are not synchronized with the time at which the stimulus appears (e.g., email pop-up notification), which is the case for H2. As a result, we posit the following conjecture regarding the superiority of the EFRP method over the ERP one as it applies to the study at hand:

Method conjecture about EFRP vs. ERP: In a multiple stimuli context such as IT use, the EFRP method is more precise than the ERP method in capturing a users’ neural activity associated with stimulus processing when such processing does not necessarily occur at the same time as stimulus presentation. More specifically, without employing the EFRP method / with the aid of the ERP method alone, the N400 component associated with the language cognitive process of a text stimulus is unlikely to be detected.

## 3.2.1. Experimental Task

During the experiment, we asked participants to imagine that they had to prepare for a meeting in which they would have to report on a specific business-related topic. This preparation involved reading an industry report on a computer. Participants were also told that they would receive emails that would either contain relevant or irrelevant task-related information. As not all emails were relevant to the task, we asked participants to only open and read what they felt would be relevant emails, and close the rest. As Figure 2 shows, the experiment involved three sub tasks. First, participants had to read an industry report (9952 words). Second, participants needed to decide whether incoming emails were relevant based on incoming email pop-up notifications’ content. Finally, participants had to open the pop-up notification and read the emails that they considered to be relevant and discard the ones they considered irrelevant (i.e., close the pop-up notification).

![](/api/attachments/66YKUUR5/fulltext/images/4efe43405c7ce4beb7ac9f0c44568954eee78205464591243fb8f8675ce86d96.jpg)  
1- Reading task

![](/api/attachments/66YKUUR5/fulltext/images/0203a7dd03ad6e98f9bd2dee8bb9f148ca420942a7d1fa215a100f539f0c3458.jpg)  
2 - Pop-up notification

![](/api/attachments/66YKUUR5/fulltext/images/00ffb0c71355120c49d79f1642a2a7f0aa1796eb431a3581be246b9c93426b16.jpg)  
3 - Email

## Figure 2. Experimental Tasks

## 3.2.2. Experimental Stimuli

To ensure proper control over the experimental task, we specifically developed a java-based application. In this application, the text for the task was presented on the left side of the screen (Figure 2). We coded pop-up notifications to appear in the center of the screen in order to minimize the ocular artefacts generated by the movement of the eye from the text to the email notification. We set notifications to pop-up randomly between 40 seconds and 60 seconds after the preceding email was closed or discarded. The email notification included information about the sender, the object of the email, and a choice to open or close the email (two buttons labeled “open” and “close”; Figure 2). Note that there were no auditory signals accompanying the notification of emails.

If the participant chose to open the email, the industry report was greyed out and the full content of the email was displayed on the top right side of the screen (Figure 2). When the participant was finished reading the email, closing the email window would make the industry report readable again. If the participant chose not to open the email, they could close the pop up notification by clicking on the “close” button and the notification disappeared. If the notification was left unattended, we programmed it to disappear after 15 seconds. We designed this specific setup to avoid leaving emails opened and therefore stopping the experiment task. It also ensured similar task durations between participants.

We developed twenty fictitious emails (i.e., emails specifically created for this project) for the task; twelve emails (60%) were relevant to the primary task. Email titles were truncated when displayed in order to fit in the pop-up window (see Figure 2). Therefore, a constant number of 38 characters were displayed each time to participants. We programmed the experimental task to last 30 minutes.

## 3.2.3. Participants

We recruited twenty-four healthy university students (9 female, 15 male) from a university panel; each received a small financial compensation for their participation (\$20 Amazon Gift Card). Their age ranged from 19 to 40 (mean: 26 years old; SD: 7 years). We recruited only participants with no neurological and psychiatric diagnoses for this study using a pre-screened self-reported questionnaire. All had normal or corrected-to-normal vision. No participant had laser eye surgery. Finally, we obtained informed consent from each participant.

During the experiment, we explicitly told participants were to minimize movements in order to reduce artefacts in the neurophysiological recordings. We also instructed participants not to put their hand on their face during the experiment to ensure an optimal eye-tracking recording. We recorded a total of 480 email notifications. We discarded fifty-three emails for analyses because they were never opened/closed, which left a total 427 valid notifications for analysis.

## 3.2.4. Eletroencephalographic (EEG) and Eye-Tracking Recordings

We measured EEG with 32-electrode array geodesic sensor net using Netstation acquisition software and EGI amplifiers (Electrical Geodesics, Inc). We chose the vertex (recording site Cz) as the reference electrode for recording. We kept impedance below 50 kΩ with a sampling rate of 256 Hz. We monitored vertical and horizontal eye movements with a subset of the 32 electrodes.

We used a Tobii X-60 (Tobii Technology AB) eye tracker to record subjects’ eye movement patterns at 60Hz during the experiment. We performed calibration of the eyetracking software for all participants using five points located in the center and in the four corners of the screen. We checked fixation accuracy prior to the experiment by asking participants to fixate different points. We repeated the calibration procedure until we achieved sufficient accuracy. We used the Tobii implementation of the I-VT fixation filter algorithm (Salvucci & Goldberg, 2000) to extract fixations from the eye-tracking data (minimum fixation duration = 60 ms). We used the following parameters for fixation merging: the maximum angle between fixations was set at 0.5 degrees, while the maximum time between fixations was set at 75 ms. We created an area of interest (AOI) to capture users’ gaze on the email pop-up notifications. The pop-up AOI was defined 1cm larger than the actual pop-up surface (on each of four sides) in order to account for the eye-tracking device accuracy. Following Tobii Technology (2011), a good accuracy for an average subject is around 0.8°. Because the eyes of the subjects were at a distance of about 60 cm from the monitor, the tracking accuracy on screen was 0.8 cm.

We used the Noldus Observer XT (Noldus Information Technology) to synchronize the EEG and eyetracking data. The Noldus Syncbox started the co-registration of EEG and gaze data by sending a transistor-transistor logic (TTL) signal to the EGI amplifier and a keystroke signal to the Tobii Studio v 3.2. The same signals were sent during the experiment every 60 seconds to correct clock drifting between systems.

## 3.3.5. Timing of Events

Figures 3 and 4 present the timing of the three events that were contrasted in the analysis. <sup>T</sup>Event 1 is the time at which the email notification was presented on the screen for email number i; this time is referred to as the time of stimuli onset in ERP studies.

<sup>T</sup> Event is the time of the first prolonged eye fixation on the email notification for email number i; this time is referred to as the time of fixation onset in EFRP studies. Note that some subjects would react to the pop-up display with a quick gaze without engaging in reading. These eye fixations on the pop-up AOI were not considered as T2 events. This problem is analogous to the Midas Touch (Jacob, 1991) in gaze interaction, where a short and unintentional gaze on an interface element (i.e., a button) is considered to be a deliberate action of the user. The most common solution is to use a dwell time approach. However, as Surakka, Illi, and Isokoski (2003) mention, the length of the optimal dwell time depends on the task and the subject. For example, Isokoski (2000) used 150ms for gazebased text inputs (eye typing) and Miniotas (2000) used 250ms for a pointing task. The dwell should therefore be selected according to the complexity of the task (Stampe & Reingold, 1995). We used a minimal time threshold of 400ms on the pop-up AOI for the recording of T2 events. This threshold is consistent with the psycholinguistic literature, which considers this duration as the minimum time for semantic access (Kutas & Federmeier, 2011).

Finally, <sup>T</sup> <sup>3</sup> Event is the time at which the participant performs the action to open or close the email notification for email number i; this time is referred to as the time of response onset in ERP studies.

# Required parameters are missing or incorrect.

## Figure 4. Order of Events

## 3.2.6. Data Processing

We used Brain Vision Software (Brain Products) for the EEG analysis. We followed Nikolaev et al.’s (2011) and Dimigen et al.’s (2011) recommendations for EEG data processing and EFRP analysis. We used an infinite impulse response Butterworth filter on the EEG signal with a bandpass of 1-15Hz (24 dB/oct) (Duncan et al., 2009). We chose restrictive filters in order to optimize the signal-to-noise ratios because the setting used in this experiment introduced more noise than traditional ERP experiments; these filter settings remain consistent with Duncan et al.’s (2009) recommendations. We applied an independent component analysis (ICA) to attenuate the movement of eye blinks and saccades in the EEG data (Jung et al., 2000). The ICA used a selection of 200 seconds of training data located at 1000s into the recording. Previous research has shown that ICA is unlikely to selectively alter the shape of the EEG signals (Jung et al., 2000). We referenced all channels according to the common average reference. We used an automatic artifact rejection to exclude epochs with voltage differences over 50 μV between two neighboring sampling points and a difference over 200 μV in a 200ms interval. We also excluded amplitudes that exceeded +200 or −200 μV and the lowest allowed activity in a 100ms interval was 0.5 μV (Nikolaev et al., 2011). Finally, we reduced the EEG data to segments of 1000ms.

## 4. Results

In this section, we first test the study’s hypotheses. That is, we test whether we observe a bottom-up attentional process (H1), a language cognitive process (H2), and a motor planning process (H3). Second, we validate our main method conjecture regarding the superiority of the EFRP method versus the ERP one for capturing the processing of a stimulus in natural IS use contexts. Note that, to test the hypotheses and the results that follow, we applied to our statistical test the Holm-Bonferroni correction (Holm, 1979) to counteract the concerns associated with multiple tests (i.e., the possibility of committing a Type I error).

## 4.1. Testing H1 : Stimuli Onset (T1)

Hypothesis 1 advances that, at stimulus onset (T1), a bottom-up attentional process (i.e., P300 component) is observed. Following Nikolaev et al. (2011) and Duncan et al. (2009), we used the interval of 300-800ms following the appearance of the pop-up email notification for analysis.

![](/api/attachments/66YKUUR5/fulltext/images/1c063efd58cc16ea18eecd32c41d2070316a80d376a3ffe4861ab8664ebcdd53.jpg)

![](/api/attachments/66YKUUR5/fulltext/images/b7b036bfbbfa454f9bce97373834c45e86c41f93c8781af0872895d4a1ebb0d7.jpg)  
Figure 5. ERP at Stimuli Onset (T1) Revealing a P300 (Weighted Grand Average ERP)

As expected, the mean amplitude of Pz after T1 was significantly positive over the considered time interval (mean=1.803µV/ms; T=8.402; p=0.000; see Figure 5). We also observe that the mean amplitude at Pz was significantly higher than all of the other 31 nodes (t statistics ranged from 2.946 to 9.019 with corresponding p-values between 0.007 and 0.000). As such, our results clearly show a P300 component at stimulus onset (T1), which indicates the presence of a bottom-up attentional process, which supports Hypothesis 1.

## 4.2. Testing H2 : Fixation Onset (T2)

Hypothesis 2 advances that, at fixation onset (T2), a language cognitive process (i.e., N400 component) is observed. Based on the N400 literature (Duncan et al., 2009), we studied the reaction to the fixation onset (T2) over the time interval of 200-600ms and used it to test the hypothesis.

![](/api/attachments/66YKUUR5/fulltext/images/26fd7d7b53d84e73f5869a1e73a0fad1fd0de20d0d29043366f51311fddafc77.jpg)

![](/api/attachments/66YKUUR5/fulltext/images/24a6a77c061cca80b5f7b368bb23161c890ed1b6ec7d3cde67c422fa552751e8.jpg)

## Figure 6. EFRP at Fixation Onset (T2) Revealing a N400 (Weighted Grand Average ERP)

As expected, after T2, the mean amplitude of Pz was significantly negative over the considered time interval (mean=-2.160µV/ms; t=-4.740; p<0.000), which indicates the presence of a N400 component at fixation onset, which supports Hypothesis 2 (see Figure 6). We also observed that the mean amplitude at Pz was significantly lower than all of the 8 surrounding nodes $\mathsf C _ { 3 } , \mathsf C _ { 2 } , \mathsf C _ { 4 } , \mathsf P _ { 3 } , \mathsf P _ { 4 } , \mathsf O _ { 1 } , \mathsf O _ { 2 }$ and $\mathsf { O } _ { 2 }$ (t statistics ranged from -3.230 to -6.46with corresponding p-values between 0.002 and 0.000).

As for the positive mean amplitudes in the left frontal lobe, the mean amplitudes at $\mathsf { F } _ { 3 }$ and $\mathsf { F } _ { 7 }$ were both significantly positive $( \mathsf { F } _ { 3 } ;$ mean=0.894µV/ms with t=2.03 and p=0.027; $\mathsf { F } _ { 7 } ;$ mean=1.786µV/ms with t=3.89 and p=0.000) and were also both significantly higher than the mean amplitudes of $\dot { \mathsf { F } } _ { 4 }$ and $\mathsf { F } _ { 8 }$ respectively in the right frontal lobe $( \mathsf { F } _ { 3 }$ vs $\mathsf { F } _ { 4 } \colon \mathsf { t } = 2 . 6 2$ and p=0.017; $\mathsf { F } _ { 7 }$ vs $\mathsf { F } _ { 8 : }$ t=1.993 and p=0.008). As such, our results provide additional support for Hypothesis 2 by showing that language-related areas of the brain are involved in this time interval.

## 4.3. Testing H3 : Response Onset (T3)

Hypothesis 3 advances that, before response onset (T3), a motor planning process (i.e., BP component) is observed. In order to test Hypothesis 3, we studied the response onset over the time interval of 100-230ms before the respondent clicked on the email notification pop-up to open the email or close the pop-up (Blankertz et al., 2002).

As expected, our results show that the mean amplitudes of $\mathsf { F } _ { Z } , \mathsf { F C } _ { Z } ,$ and $\mathtt { C z }$ before T3 were significantly negative over the considered time interval (respectively, mean= -0.687, -0.832, and - 0.520µV/ms; t=-4.472, -4.507, and -2.416; p=0.000, 0.000, and 0.012; see Figure 7). As such, our results reveal a BP component at response onset indicating the presence of a motor planning process, which supports Hypothesis 3.

![](/api/attachments/66YKUUR5/fulltext/images/16b2e89ef66598643992783afe527885f370e7aa311f539a700046a1dd51e038.jpg)

![](/api/attachments/66YKUUR5/fulltext/images/a255732df7a7afc6acdaea5d85ce23378aa68a6eeccc4c632e87015ef4eac30d.jpg)  
Figure 7. ERP at Response Onset (T3) Revealing a BP (Weighted Grand Average ERP)

## 4.4. Validation of the Method Conjecture: Evidence Supporting the Superiority of EFRP over ERP for Capturing the Cognitive Processing of a Stimulus During IS Use

Finally, to validate our method conjecture that the EFRP method is superior to the ERP one in capturing a users’ neural activity associated with stimulus processing when such processing does not necessarily occur at the same time as stimulus presentation, we performed several analyses to show the: 1) differences in neural reactions between the stimuli onset (T1) and the fixation onset (T2), 2) differences in neural reactions between the fixation onset (T2) and the response onset (T3), and 3) results drawn from the fixation onset (T2, using the EFRP method) could not have been drawn by solely using the traditional ERP method (T1 and T3).

4.4.1. Distinguishing the Stimulus (T1) and the Fixation Onsets (T2)  
![](/api/attachments/66YKUUR5/fulltext/images/52230b3efe882eebe582d01ac0dd71ff094dfa23ecc034c6e17f389def8bb272.jpg)

![](/api/attachments/66YKUUR5/fulltext/images/8d242a1eb9eb5ebf7cc9933cc06fd7102a382effb8289a06c607f53e9cbd2989.jpg)  
Figure 8. Brain Activity Comparison After T1 and T2

Over the time interval of 300-800ms after the onsets (left-panel of Figure 8), a P300 was characterized by a positive mean amplitude at Pz. When we compared T1 and T2 over this time interval, the mean amplitude of PZ was significantly higher at T1 (t=6.660; p<0.000).

Over the time interval of 200-600ms after the onsets (right-panel of Figure 8), our N400 was characterized by a negative mean amplitude at Pz and a positive mean amplitude at $\mathsf { F } _ { 3 }$ and $\mathsf { F } _ { 7 } .$ When we compared T2 and T1 over this time interval, the mean amplitudes of $\mathsf { P } _ { Z }$ and $\mathsf { F } _ { 7 }$ at T2 were respectively significantly smaller $( \mathsf { t } = - 5 . 6 5 0 ; ~ \mathsf { p } < 0 . 0 0 0 )$ and significantly higher (t=3.163; p=0.002). However, the difference was not statistically significant at $\mathsf { F } _ { 3 } \left( \mathsf { t } = - 0 . 5 0 4 ; \mathsf { p } = 0 . 6 8 8 \right)$

## 4.4.2. Distinguishing the Fixation (T2) and Response Onsets (T3)

While the activities associated with the fixation onset (T2) and the response onset (T3) are measured over time intervals of different lengths, it is possible to compare their mean amplitudes as the unit of measurement is in µV/ms. When we compared this mean amplitude to the mean amplitude observed in the time interval of 230-100ms before T3, the mean amplitude of $\mathsf { P } _ { Z }$ at T2 was significantly smaller (t=-3.372; p=0.001). In addition, the mean amplitudes of $\dot { \mathsf { F } } _ { 3 }$ and $\mathsf { F } _ { 7 }$ in the left frontal lobe at T2 were significantly higher (t=3.123 and 3.801; p=0.003 and 0.001).

## 4.4.3. Attempt to Find the N400 Component with ERP Method from Stimulus (T1) and Response (T3) Onsets

The histograms shown in Figures 9 and 10 indicate a lot of variability between T1 (email notification pop-up appearance) and T2 (email notification pop-up processing) and even more variability between T2 and T3 (the motor planning involved in either opening the email or closing the notification pop-up). As such, between the appearance of the email notification pop-up and the decision, it is unlikely, without eye tracking, to estimate when a subject starts to read the email notification pop-up (T2).

![](/api/attachments/66YKUUR5/fulltext/images/6ba2370d99ee8f21af3f8c0ad20592fd1a58a764c2191c15245880a8e2f8b59e.jpg)  
Figure 9. Distribution of the Time between Stimulus (T1) and Fixation (T2) Onsets

![](/api/attachments/66YKUUR5/fulltext/images/632b74cbc44d00635672db76eb7511ddbe124b5724742424fd739a47ad45e11c.jpg)

## Figure 10. Distribution of the Time between Fixation (T2) and Response (T3) Onsets

Furthermore, using the median observed from the histograms, we attempted to retrieve the N400 component from T1 and T3 (See Figure 11). We calculated the three topo plots on each side of Figure 11 from three 200ms intervals around the median. We observe that none of these 6 images are comparable to the N400 potential observed (the topo plot in the middle of Figure 11). This demonstrates that, without the eye tracking, even if we had perfect knowledge (which is unlikely) of the median time between T3 and T1 and the median between T2 and T3, it would have been very unlikely to retrieve the N400 component using T1 and T3, which are the only capturable events with a traditional ERP.

From T1 without eye-tracker

![](/api/attachments/66YKUUR5/fulltext/images/5e56b9c5e388d54b915a8812d96e5a96a247b6a5b12e6a8952767473c718ab92.jpg)  
From T2 with eye-tracker

![](/api/attachments/66YKUUR5/fulltext/images/841129ecb963aa6e262f28ef7682c1a8464715373d73bef56d95ae84212ac402.jpg)

![](/api/attachments/66YKUUR5/fulltext/images/5da42b962eefa63333e32d43a30c4a0aaf43a1688d7fc35d25862a803613f06a.jpg)

![](/api/attachments/66YKUUR5/fulltext/images/3a9c92ecdf5b30995de6d5ae1e18003c9fa341ae4a9af124decf9944e1c03977.jpg)

![](/api/attachments/66YKUUR5/fulltext/images/cc1c7835ca31ae6d9c11a54549771b29686097de6914c4461a5b9f7cf9814f10.jpg)

![](/api/attachments/66YKUUR5/fulltext/images/14651f3ceb8bb59dcc81729c22ec913fdea04e0184f73ff673db97823357351f.jpg)

![](/api/attachments/66YKUUR5/fulltext/images/50529eed5c40f8594c61c58dc6643f96fba95a61cebb0dcb04f3acd9969088d9.jpg)  
Figure 11. Attempt to Find the N400 Component from T1 and T3

To more formally establish the impossibility of retrieving the N400 component from T1 or T3, we calculated a large number of mean amplitudes over the time intervals (x+200ms, x+600ms) where x could theoretically be any time points between T1 and T3. If it was possible to retrieve an N400 without the EFRP, we would thus be able to find a time point x0 where the mean amplitude over the (x +200ms, x +600ms) would at the same time be:

1) significantly negative at $\mathsf { P } z ;$

2) significantly greater at $\mathsf { F } _ { 3 }$ than $\mathsf { F } _ { 4 } ;$

3) significantly greater at $\mathsf { F } _ { 7 }$ than $\mathsf { F } _ { 8 } .$

Recall that, using the EFRP, we were able to find three significant p-values for these tests (respectively 0.000, 0.027 and 0.008). Table 2 shows the p-values obtained by testing for the existence of a N400 component for every 100ms increments starting from T1 and moving forward. Likewise, Table 3 shows the p-values obtained by testing for the existence of a N400 component for every 100ms increments starting from T3 and moving backward. Just like we did when the testing of the hypotheses, we applied to our statistical test the Holm-Bonfferoni correction (Holm, 1979) in order to mitigate concerns associated with multiple tests. In both tables, all significant values after applying the Holm-Bonferroni correction are indicated in bold font. As the tables show, we were not able to obtain significant results for the tests of the three amplitudes at the same time. In Table 2, only the 3 smallest p-values are significant for one of the three tested amplitudes, while in Table 3 there are no significant p-values. In fact, even without the Holm-Bonferroni correction, we were never able to find a time interval where all three tests had a p-value smaller than 5 percent at the same time.

<table><tr><td></td><td>Amplitude at Pz&gt;0</td><td>Amplitude at F3&gt;F4</td><td>Amplitude at F7&gt;F8</td></tr><tr><td>With eye tracker (EFRP)</td><td></td><td></td><td></td></tr><tr><td>T2+(200ms,600ms)</td><td>0.000</td><td>0.017</td><td>0.008</td></tr><tr><td>Without eye tracker (ERP)</td><td></td><td></td><td></td></tr><tr><td>T1+(200ms,600ms)</td><td>1.000</td><td>0.160</td><td>0.324</td></tr><tr><td>T1+(300ms,700ms)</td><td>1.000</td><td>0.608</td><td>0.542</td></tr><tr><td>T1+(400ms,800ms)</td><td>1.000</td><td>0.903</td><td>0.940</td></tr><tr><td>T1+(500ms,900ms)</td><td>1.000</td><td>0.981</td><td>0.999</td></tr><tr><td>T1+(600ms,1000ms)</td><td>0.621</td><td>0.969</td><td>0.999</td></tr><tr><td>T1+(700ms,1100ms)</td><td>0.881</td><td>0.277</td><td>0.761</td></tr><tr><td>T1+(800ms,1200ms)</td><td>0.000</td><td>0.095</td><td>0.752</td></tr><tr><td>T1+(900ms,1300ms)</td><td>0.000</td><td>0.057</td><td>0.173</td></tr><tr><td>T1+(1000ms,1400ms)</td><td>0.000</td><td>0.101</td><td>0.154</td></tr><tr><td>T1+(1100ms,1500ms)</td><td>0.083</td><td>0.168</td><td>0.187</td></tr><tr><td>T1+(1200ms,1600ms)</td><td>0.759</td><td>0.142</td><td>0.319</td></tr><tr><td>T1+(1300ms,1700ms)</td><td>0.993</td><td>0.222</td><td>0.585</td></tr><tr><td>T1+(1400ms,1800ms)</td><td>0.999</td><td>0.258</td><td>0.838</td></tr><tr><td>T1+(1500ms,1900ms)</td><td>0.991</td><td>0.269</td><td>0.861</td></tr><tr><td>T1+(1600ms,2000ms)</td><td>0.951</td><td>0.294</td><td>0.860</td></tr><tr><td>T1+(1700ms,2100ms)</td><td>0.851</td><td>0.112</td><td>0.778</td></tr><tr><td>T1+(1800ms,2200ms)</td><td>0.913</td><td>0.054</td><td>0.545</td></tr><tr><td>T1+(1900ms,2300ms)</td><td>0.952</td><td>0.126</td><td>0.543</td></tr><tr><td>T1+(2000ms,2400ms)</td><td>0.849</td><td>0.225</td><td>0.388</td></tr><tr><td colspan="4">Table 3. P-Values to Retrieve the N400 from T3</td></tr><tr><td></td><td>Amplitude at Pz&lt;0</td><td>Amplitude at F3&gt;F4</td><td>Amplitude at F7&gt;F8</td></tr><tr><td>With eye tracker (EFRP)</td><td></td><td></td><td></td></tr><tr><td>T2+(200ms,600ms)</td><td>0.000</td><td>0.017</td><td>0.0076</td></tr><tr><td>Without eye tracker (ERP)</td><td></td><td></td><td></td></tr><tr><td>T3-(400ms,0ms)</td><td>0.079</td><td>0.191</td><td>0.514</td></tr><tr><td>T3-(500ms,100ms)</td><td>0.629</td><td>0.477</td><td>0.057</td></tr><tr><td>T3-(600ms,200ms)</td><td>0.987</td><td>0.913</td><td>0.073</td></tr><tr><td>T3-(700ms,300ms)</td><td>0.985</td><td>0.899</td><td>0.374</td></tr><tr><td>T3-(800ms,400ms)</td><td>0.719</td><td>0.778</td><td>0.526</td></tr><tr><td>T3-(900ms,500ms)</td><td>0.806</td><td>0.547</td><td>0.451</td></tr><tr><td>T3-(1000ms,600ms)</td><td>0.675</td><td>0.252</td><td>0.210</td></tr><tr><td>T3-(1100ms,700ms)</td><td>0.750</td><td>0.088</td><td>0.033</td></tr><tr><td>T3-(1200ms,800ms)</td><td>0.843</td><td>0.011</td><td>0.071</td></tr><tr><td>T3-(1300ms,900ms)</td><td>0.638</td><td>0.003</td><td>0.255</td></tr><tr><td>T3-(1400ms,1000ms)</td><td>0.303</td><td>0.027</td><td>0.780</td></tr><tr><td>T3-(1500ms,1100ms)</td><td>0.293</td><td>0.364</td><td>0.925</td></tr><tr><td>T3-(1600ms,1200ms)</td><td>0.205</td><td>0.850</td><td>0.794</td></tr><tr><td>T3-(1700ms,1300ms)</td><td>0.156</td><td>0.991</td><td>0.758</td></tr><tr><td>T3-(1800ms,1400ms)</td><td>0.283</td><td>0.989</td><td>0.581</td></tr><tr><td>T3-(1900ms,1500ms)</td><td>0.311</td><td>0.995</td><td>0.574</td></tr><tr><td>T3-(2000ms,1600ms)</td><td>0.632</td><td>0.948</td><td>0.860</td></tr><tr><td>T3-(2100ms,1700ms)</td><td>0.787</td><td>0.641</td><td>0.798</td></tr><tr><td>T3-(2200ms,1800ms)</td><td>0.951</td><td>0.301</td><td>0.586</td></tr><tr><td>T3-(2300ms,1900ms)</td><td>0.966</td><td>0.062</td><td>0.214</td></tr><tr><td>T3-(2400ms,2000ms)</td><td>0.893</td><td>0.045</td><td>0.023</td></tr><tr><td>T3-(2500ms,2100ms)</td><td>0.547</td><td>0.093</td><td>0.053</td></tr><tr><td>T3-(2600ms,2200ms)</td><td>0.059</td><td>0.131</td><td>0.130</td></tr><tr><td>T3-(2700ms,2300ms)</td><td>0.040</td><td>0.137</td><td>0.198</td></tr><tr><td>T3-(2800ms,2400ms)</td><td>0.083</td><td>0.421</td><td>0.660</td></tr></table>

ill-suited to studying the evoked potential of neural activity associated with processing naturally occurring stimuli during IS use when such activity does not necessarily take place at the same time as the stimuli occur.

This paper contributes to the literature in several ways. First, the EFRP allows one to investigate IT “direct and unmediated effects” on users’ cognitive processing during IS use. This is critical because most IS research has regarded the IT artifact as a black box (Dimoka et al., 2011). That is, most IS research has rarely investigated the direct effects of the IT artifact on users’ cognitive processing; instead, it has replaced the IT artifact by mental representations of it through the study of perceptions (e.g., usefulness) (Ortiz de Guinea & Markus, 2009; Silva, 2007). Thus, users’ neural cognitive processing identified through the EFRP method can serve as a mediator between the characteristics (and events) of an IT during use and users’ perceptions of that IT. Second, the EFRP method is more accurate than the ERP method in capturing the N400 component, which allows one to precisely measure users’ cognitive processes unobtrusively at the time at which they occur. With the EFRP method, users naturally use a given IT and their cognitive processes are automatically time locked with their eye movement and thus with the parts of the application they cognitively process at that time, with no need to interrupt their natural use and interaction with the IT. Finally, the EFRP method allows one to measure users’ automatic cognitive processes that might occur outside individuals awareness (Dimoka et al., 2012; Ortiz de Guinea & Markus, 2009; Ortiz de Guinea & Webster, 2013). In fact, one consequence of the almost exclusive focus on users’ perceptions of the IT artifact is that such approach can only capture conscious reactions, which individuals can report via self-reported measures, which thus omits potential unconscious and automatic cognitive reactions to technology as they naturally occur (Ortiz de Guinea, Titah, Léger, 2014).

All in all, this study’s main contribution is that it illustrates the superiority of the EFRP method over the ERP method for directly measuring users’ neural activity (either automatic or conscious) when processing events occurring in the IT artifact during IS use.

## 5.1. Implications for IS Research

The above contributions are important for the IS field because the strengths of the EFRP method allow one to investigate important research questions associated with the experience of IS use in a natural context. The type of research questions associated with IS use that the EFRP method can help answer have two main characteristics. First, the EFRP method can be applied to questions that require a fixation event on a spatial element of the screen (e.g., an event, a graphical representation, a functionality in an interface) on which the analyses need to be time locked with users’ processing of the event. Second, the EFRP is also particularly well suited to help answer research questions that require the study of users’ evoked potential once they start processing in a multi-stimuli context either an endogenous event, such as the natural use of a new functionality, or an exogenous event, such as reacting to warnings.

With these two characteristics in mind, we can pose several interesting and important research questions for the IS field that can be studied with the aid of the EFRP method. First, the EFRP method enables the study of users’ neural cognitive processes as they transition from one application to another in a multitasking use environment. Nowadays, a user usually has many different applications open at a given time: a text processing software to write a report, an email application to receive and send important information, a browser to search for information, a pdf reader to read through different documents, etc. (González & Mark, 2004). However, most IS use research focuses on studying factors leading to the use of one single application, rather than focusing on the neural activity that occurs as users utilize multiple applications at the same time. Thus, an important research question would be to study the neural activity that is involved in transitioning from one application to the next when prompted by a notification or an event, which would serve to identify the cognitive costs associated with such transitions and how these costs can be minimized by interface design (vom Brocke, Riedl, & Léger, 2013).

Second, the EFRP method allows one to study the neural activity associated with using new features either in the same software or in a new one. Traditionally, the IS literature has implied that a user adopting a novel feature entails a conscious cognitive effort (Jasperson, Carter, & Zmud, 2005).

However, some researchers have recently noted the capability for humans to unconsciously and automatically generalize from a behavior learned in one situation to a new one (Ortiz de Guinea & Markus, 2010). The idea is that automatic behaviors do not need to follow the same exact old patterns but that they can differ from previous learned action sequences (Bargh & Ferguson, 2000; Wood, Quinn, & Kashy, 2002). Thus, for example, studies could focus on using the EFRP method to time lock the neural activity involved in inputting, deleting, or saving in one application, and compare it with the same actions in a new application environment. Furthermore, the EFRP method could be used to time lock and compare the neural activity involved in the use of well-known features in an application with the use of other features that have never been used before (and thus are novel). As a result, the EFRP method can answer the important question of whether users can automatically and unconsciously generalize from one known application context to a relatively unknown one and whether the neural activities associated with using a known application are different from those associated with a new one.

Third, the EFRP method can be used to identify the neural activity associated with the experience of IT discrepant events (events that entail a difficulty with the IT being used) (Ortiz de Guinea & Webster, 2013). This is important because research has shown that discrepant IT events can break automatic use patterns by altering users’ cognitive, emotional, and behavioral processes, which, in turn, influence performance in a given task (Ortiz de Guinea & Webster, 2013). Similarly, research has shown that person-technology misfits cause significant stress and strain, which is detrimental to individual well-being and performance (Ayyagari, Grover, & Purvis, 2011). In such contexts, EFRP would allow one to observe (i.e., time-locking) the specific episodes overwhelming or impeding individual behaviors, or a contrario the specific manifestations of individual adaptation or coping strategies (Beaudry & Pinsonneault, 2005) during such episodes.

Finally, the EFRP method could benefit e-commerce research because it would allow one to precisely unravel and observe the instantaneous and direct effect of several IT manifestations on individuals decisions or actions such as display advertising (Lee & Ahn, 2012) or interface characteristics (Djamasbi, Siegel, Skorinko, & Tullis, 2011; Hassanein & Head, 2005). It could also help explain the specific triggers (i.e., at the time they are processed) of individual emotional experience and their consequences during, for example, the interactions with interfaces, avatars, or recommendation agents (e.g., Benbasat, Dimoka, Pavlou, & Qiu, 2010; Benlian, Titah, & Hess, 2012; Qiu & Benbasat, 2009; Senecal & Nantel, 2004), the interaction while learning a software application (Léger, Davis, Cronan, & Perret, 2014a), or during text and video interactions with other human counterparts such as in virtual team (Martins, Gilson, & Maynard, 2004) and business process collaboration settings (Léger, Riedl, & vom Brocke, 2014b)<sup>3</sup> .

While the above discussion presents several advantages of the EFRP method, we also need to acknowledge the method’s limits. Most importantly, EFRP’s principal limitation is related to the difficulty of obtaining a good signal-to-noise ratio. While this limitation could be reduced by having multiple repetition of an event (as it is the case in traditional ERP experiments), obtaining a same repetitive event in natural IT use contexts remains a challenging task. Additionally, while this study demonstrates the use of EFRP in the context of a stimulus fostering a bottom-up attentional process, future research is needed to test this method in contexts investigating the distinction between language processing and top-down executive attentional processes and with other IS related stimuli such as shape and color (i.e., icons in an interface or online advertisement).

Another potential limitation of this study is that it did not assess the comparative advantage of the EFRP method in a nomological network (i.e., the advantage of precisely capturing the individual attentional, cognitive processing, and decisional episodes during IS use). While our study was mainly methodological, we believe that future research may usefully integrate performance measures to further demonstrate how a better understanding of individual behavior and performance requires the capture of the distinct and unmediated moments at which an individual reacts to an IT event, processes it, and returns to its main task.

## 6. Guidelines for Conducting an EFRP Study

EFRP opens the door for several new and potentially original research avenues. As it is the case with all research methods, and particularly with neuroscience methods, several important technical elements need to be taken into account in order to ensure a valid execution of the method.

As Table 4 summarizes, the “first step” in EFRP recording consists, prior to the experiment, to ensure that the experimental setup does not introduce electrical noise in the EEG data. Because eye trackers are high energy consumers, particular precautions need to be taken in order to avoid direct or indirect (e.g., via a conductive material) contact with the participant. Specifically, the eye tracker needs to be placed on a nonconductive desk and at a minimum distance of approximately 30 cm from the mouse and keyboard wires that the subjects will be using.

<table><tr><td colspan="2">Steps</td><td>Guidelines</td></tr><tr><td>1.</td><td>Eye tracker isolation</td><td>Ensure that the eye tracker does not introduce 50Hz or 60Hz electrical noise in the EEG recording.</td></tr><tr><td>2.</td><td>Eye tracker calibration</td><td>Fix a minimum calibration precision threshold and recalibrate all participants until the required threshold is obtained.</td></tr><tr><td>3.</td><td>Area of interest (AOI) definition</td><td>Create the area of interest (AOI) and allow larger AOIs according to the calibration precision threshold.</td></tr><tr><td>4.</td><td>“Visit” threshold definition</td><td>Set the “visit” threshold, i.e., the minimum time spent on an AOI that could be accounted for as a valid EFRP.</td></tr><tr><td>5.</td><td>Fixation overlaps rejection</td><td>Reject fixations occurring within stimulus onset P300 window and those significantly overlapping the preceding ERP window.</td></tr><tr><td>6A.</td><td>Direct synchronization of recordings</td><td>Set the eye tracker to send live markers to the EEG system.</td></tr><tr><td rowspan="4">6B.</td><td rowspan="4">Indirect synchronization of recordings</td><td>Set the eye tracker and EEG systems to start asynchronously.</td></tr><tr><td>Set a synch device to send synchronous signals to the eye-tracker and EEG systems.</td></tr><tr><td>Parse the eye-tracker export file to extract fixation information.</td></tr><tr><td>Import parsed files in the EEG system after timestamp correction.</td></tr><tr><td>7.</td><td>Removal of ocular artifacts</td><td>Use a method that is not too restrictive and that will not affect the quality of the signal during the time window of interest.</td></tr></table>

the fixations on the stimulus are recorded sooner than desired. As such, a trade-off between participant rejection rate (small calibration threshold) and EFRP quality needs to be set.

Furthermore, because eye movements can be unintentional (Graf & Krueger, 1989) or partly controlled for by oculomotor automated routines (Engbert, Longtin, & Kliegl, 2002), they may trigger unintended AOI fixations. This phenomenon is known as the Midas Touch (Jacob & Karn, 2003), and needs to be controlled for at “step four” by defining the minimum summation of fixation durations on the AOI stimulus, also called visits, that are required to consider a relevant EFRP. The first fixation of these visits is then used to compute the actual EFRP. For example, in our experiment, we only considered visits that had a minimum duration of 400ms as valid EFRP.

The “fifth step” consists in excluding trials for which the neuronal components overlap. Such overlaps can occur in two situations:

1) when the participant looks at the stimulus almost immediately after its onset, and

2) when the experimental design involves a stimuli presentation that is too fast.

In the first situation, the N400 component related to stimuli processing is distorted by the related preceding P300, which is related to the stimuli onset. In our experiment, this situation only occurred in 2.5 percent of the events, which we excluded from our analyses. In the second situation, a temporal overlap usually occurs between successive fixations due to rapid stimuli presentation. If the overlap is too significant, the fixations need to be discarded (Dimigen et al., 2011).

The “sixth step” concerns the synchronization of the multiple data sources. The challenge of synchronization arises from the opportunity to measure concurrently several modalities, such as eye tracking and EEG used in this research, and other measures available to NeuroIS researchers, such as physiological and behavioral measures (e.g., electrocardiographs and facial expressions). Equipment manufacturers strongly recommend using only one computer per measurement tool to guaranty their specified precision level. Therefore, when multiple computers are employed, synchronization between recording computers is a crucial and necessary step. This synchronization can either be done during the experiment (step 6A) or after its completion (step 6B). For researchers using step 6A, it implies that eye gaze markers are sent live to the EEG system. It also implies that complex pre-configuration of the eye tracker to process live the fixation data using the parameters related to this EFRP method. A more practical approach is to use indirect synchronization (step 6B), but further manipulation is required to ensure proper data consistency. Specifically, because both systems do not start at the exact same time, EEG and eye-tracking data files will have different relative start times. This delay needs to be accounted for and can be measured by using a third device that will send, during the recording, a synchronous signal to both systems. As we describe in Section 3, we used the Noldus Syncbox to send TTL signals to the EEG amplifier and the eye-tracker. These markers are then used to realign the signals and thus ensure proper synchronization after each recording. Then, the eye-tracking log files need to be parsed in order to apply a timestamp correction. This correction uses the delay measured at the previous step between both recording devices. In our experiment, we achieved this step by using an application we developed ourselves (Léger et al., 2013). This application also parsed the eye-tracking log file to only extract the relevant fixations (step four), which avoided importing unnecessary events in the EEG software.

Finally, because eye movements create ocular artefacts (blinks and lateral movements) that distort the EEG data, an artefact removal process needs to be performed prior to data analysis (“step seven”). The most widely used methods for ocular artefact removal are independent component analysis (ICA) (Vigário, 1997) and electrooculography (EOG) (Gratton. Coles, & Donchin,, 1983). ICA, which was used in this study (see the data processing section), consists of a computational separation of signal sources in order to manually remove eye movement artifact components before reconstructing the signal. ICA is done in combination with manual inspection. Manual inspection of the ICA needs to be done by an expert and has been shown to be a very effective method to preserve the integrity of the cognitive components (Mennes, Wouters, Vanrumste, Lagae, & Stiers, 2010). Note that artefact removal has to be flexible enough to avoid discarding most or all EEG data during stimulus fixations as ocular artefacts are intrinsically inevitable in an EFRP experiment.

## 7. Conclusion

In this paper, we present the EFRP method and illustrated its application in an IS use context and its superiority over the employment of ERP alone. The original and distinctive characteristic of this technique is that it allows, by using eye-tracking in conjunction with EEG, to stamp the exact time at which an individual processes a particular stimulus (stimulus processing), rather than the time at which the stimulus is presented to this individual (stimulus reaction). This methodological capability is significant because it allows one to capture the direct and unmediated effect of IT on three distinct neural activities: individual attention, processing, and action at the precise moment an IT-related event or manifestation occurs. The EFRP method is also important because it allows one to investigate the cognitive reactions of users in natural IS use contexts; that is, during actual IS use. Finally, this method also complements other traditional ones (i.e., self-reported) since it allows one to assess users’ automatic and unconscious neural activity. As such, it provides a more complete understanding of users’ cognitions at the time of IS use. We hope that our illustration of the EFRP method and the guidelines for using it will be useful to IS researchers willing to investigate relevant research questions with the aid of NeuroIS tools.

## Acknowledgments

We are indebted to the participants of the 2013 Gmundem Retreat on NeuroIS (Austria) for their insightful comments on previous versions of this manuscript. This research was partially funded by a grant from the Social Sciences and Humanities Research Council of Canada (SSHRC) to Sylvain Sénecal, Pierre-Majorique Léger, Ana Ortiz de Guinea, and Ryad Titah; by a grant from Natural Sciences and Engineering Research Council of Canada to Pierre-Majorique Léger; by a grant from the Fonds Québécois pour la Recherche sur la Société et la Culture (FQRSC) to Ana Ortiz de Guinea; and by a grant from the Fonds Québécois pour la Recherche sur la Société et la Culture (FQRSC) to Ryad Titah; by a grant from the Fonds de recherche Nature et Technologies (FQRNT) to François Courtemanche.

## References

Ahlsén, E. (2006). Introduction to neurolinguistics. Amsterdam, The Netherlands: John Benjamins Publishing Company.

Ayyagari, R., Grover, V., & Purvis, R. (2011). Technostress: Technological antecedents and implications. MIS Quarterly, 35(4), 831-858.

Baccino, T. (2011). Eye movements and concurrent ERP’s: EFRPs investigations in reading. In S. Liversedge, Ian D. Gilchrist, & S. Everling (Eds.), Oxford handbook of eye movements (pp. 857-870). Oxford: Oxford University Press.

Bargh, J. A., and Ferguson, M. J. (2000). Beyond behaviorism: On the automaticity of higher mental processes. Psychological bulletin, 126(6), 925-945.

Beaudry, A., & Pinsonneault, A. (2005). Understanding user responses to information technology: A coping model of user adaptation. MIS Quarterly, 29(3), 493-524.

Benbasat, I., Dimoka, A., Pavlou, P. A, & Qiu, L. (2010). Incorporating social presence in the design of the anthropomorphic interface of recommendation agents: Insights from an fMRI study. Proceedings of the 31st International Conference on Information Systems, 1–22.

Benlian, A., Titah, R., & Hess, T. (2012). Differential effects of provider and user recommendations in e-commerce transactions: An experimental study. Journal of Management Information Systems, 29(1), 237-272.

Blankertz, B., Curio, G., & Muller, K.-R. (2002). Classifying single trial EEG: Towards brain computer interfacing. Advances in Neural Information Processing Systems, 157–164.

Bledowski, C., Prvulovic, D., Hoechstetter, K., Scherg, M., Wibral, M., Goebel, R., & Linden, D. E. J. (2004). Localizing P300 generators in visual target and distractor processing: A combined event-related potential and functional magnetic resonance imaging study. The Journal of Neuroscience, 24(42), 9353-9360.

Buschman, T. J., & Miller, E. K. (2007). Top-down versus bottom-up control of attention in the prefrontal and posterior parietal cortices. Science, 315(5820), 1860-1862.

Corbetta, M., Kincade, J. M., Ollinger, J. M., McAvoy, M. P., & Shulman, G. L. (2000). Voluntary orienting is dissociated from target detection in human posterior parietal cortex. Nature Neuroscience, 3(3), 292-297.

Deecke, L. (1990). Electrophysiological correlates of movement initiation. Revue Neurologique, 146(10), 612-619.

Dimigen, O., Sommer, W., Hohlfeld, A., Jacobs, A. M., & Kliegl, R. (2011). Coregistration of eye movements and EEG in natural reading: Analyses and review. Journal of Experimental Psychology: General, 140(4), 552-572.

Dimoka, A. (2012). How to conduct a functional magnetic resonance (FMRI) study in social science research. MIS Quarterly, 36(3), 811-840.

Dimoka, A., Pavlou, P. A., & Davis, F. D. (2011). Research commentary—NeuroIS: The potential of cognitive neuroscience for information systems research. Information Systems Research, 22(4), 687-702.

Djamasbi, S., Siegel, M., Skorinko, J., & Tullis, T. (2011). Online viewing and aesthetic preferences of generation Y and baby boomers: Testing user website experience through eye tracking. International Journal of Electronic Commerce, 15(4), 121-157.

Duncan, C. C., Barry, R. J., Connolly, J. F., Fischer, C., Michie, P. T., Näätänen, R., & Van Petten, C. (2009). Event-related potentials in clinical research: Guidelines for eliciting, recording, and quantifying mismatch negativity, P300, and N400. Clinical Neurophysiology, 120(11), 1883-1908.

Engbert, R., Longtin, A., & Kliegl, R. (2002). A dynamical model of saccade generation in reading based on spatially distributed lexical processing. Vision Research, 42(5), 621-636.

Gazzaniga, M. S. (2004). The cognitive neurosciences. Cambridge, MA : MIT Press.

González, V. M., & Mark, G. (2004). Constant, constant, multi-tasking craziness: Managing multiple working spheres. Proceedings of the SIGCHI conference on Human factors in computing systems, 113-120.

Graf, W., & Krueger, H. (1989). Ergonomic evaluation of user-interfaces by means of eye-movement data. Proceedings of the third international conference on human-computer interaction, 659-665.

Gratton, G., Coles, M. G. H., & Donchin, E. (1983). A new method for off-line removal of ocular artifact. Electroencephalography and Clinical Neurophysiology, 55(4), 468-484.

Grewe, T., Bornkessel, I., Zysset, S., Wiese, R., von Cramon, D. Y., & Schlesewsky, M. (2005). The emergence of the unmarked: A new perspective on the languag-specific function of Broca's area. Human Brain Mapping, 26(3), 178-190.

Hallett, M. (1994). Movement-related cortical potentials. Electromyography and Clinical Neurophysiology, 34(1), 5.

Hassanein, K., & Head, M. (2005). The impact of infusing social presence in the web interface: An investigation across different products. International Journal of Electronic Commerce, 10(2), 31-55.

Holcomb, P. J., & Neville, H. J. (1991). Natural speech processing: An analysis using event-related brain potentials. Psychobiology, 19(4), 286-300.

Holm, S. (1979). A simple sequentially rejective multiple test procedure. Scandinavian Journal of Statistics, 6(2), 65–70.

Hopfinger, J. B., & Park, E. L. (2012). Involuntary attention. In G. R. Mangun (Ed.), The neuroscience of attention (pp. 30-35). New York, NY: Oxford University Press.

Hutzler, F., Braun, M., Võ, M. L. H., Engl, V., Hofmann, M., Dambacher, M., & Jacobs, A. M. (2007). Welcome to the real world: Validating fixation-related brain potentials for ecologically valid settings. Brain Research, 1172(0), 124-129.

Isokoski, P. (2000). Text input methods for eye trackers using off-screen targets. Paper presented at the Proceedings of the 2000 Symposium on Eye Tracking Research & Applications, Palm Beach Gardens, Florida, USA.

Jacob, R. J. K. (1991). The use of eye movements in human-computer interaction techniques: What you look at is what you get. ACM Transactions on Information Systems, 9(2), 152-169.

Jacob, R. J. K., & Karn, K. S. (2003). Eye tracking in human-computer interaction and usability research: Ready to deliver the promises. Mind, 2(3), 573-605.

Jasperson, J. S., Carter, P. E., & Zmud, R.W. (2005). A comprehensive conceptualization of postadoptive behaviors associated with information technology enabled work systems. MIS Quarterly, 29(3), 525-557.

Jung, T. P., Makeig, S., Westerfield, M., Townsend, J., Courchesne, E., & Sejnowski, T. J. (2000). Removal of eye activity artifacts from visual event-related potentials in normal and clinical subjects. Clinical Neurophysiology, 111(10), 1745-1758.

Kamienkowski, J. E., Ison, M.J., Quiroga, R. Q., & Sigman, M. (2012). Fixation-related potentials in visual search: A combined EEG and eye tracking study. Journal of Vision, 12(7), 1-20.

Kolev, V., & Yordanova, J. (1997). Analysis of phase-locking is informative for studying event-related EEG activity. Biological Cybernetics, 76(3), 229-235.

Kutas, M., & Federmeier, K. D. (2011). Thirty years and counting: Finding meaning in the N400 component of the event-related brain potential (ERP). Annual Review of Psychology, 62(1), 621-647.

Lee, J. W., & Ahn, J. H. (2012). Attention to banner ads and their effectiveness: An eye-tracking approach. International Journal of Electronic Commerce, 17(1), 119-138.

Léger, P.-M., Sénécal, S., Courtemanche, F., Ortiz de Guinea, A., Titah, R., Fredette, M., & Labonte-Lemoyne, E. (2013). Eye fixation related potential method and system. Provisional patent application, US 61/903,000.

Loos, P., Riedl, R., Müller-Putz, G., vom Brocke, J., Davis, F., Banker, R., & Léger, P.-M. (2010). NeuroIS: Neuroscientific approaches in the investigation and development of information systems. Business & Information Systems Engineering, 2(6), 395-401.

Léger, P.-M., Davis, F., Cronan, P., & Perret, J. (2014a) Neurophysiological correlates of cognitive absorption in an enactive training context, computers in human behavior, 34, 273-283.

Léger, P.-M., Riedl, R., & vom Brocke, J. (2014b). Emotions and ERP information sourcing: The moderating role of expertise. Industrial Management & Data System, 114(3), 456-471.

Luck, S. (2005). An introduction to the event-related potential technique. Cambridge, MA: MIT Press.

Martins, L. L., Gilson, L. L., & Maynard, M. T. (2004). Virtual teams: What do we know and where do we go from here? Journal of Management, 30(6), 805-835.

Mennes, M., Wouters, H., Vanrumste, B., Lagae, L., & Stiers, P. (2010). Validation of ICA as a tool to remove eye movement artifacts from EEG/ERP. Psychophysiology, 47(6), 1142-1150.

Miniotas, D. (2000). Application of Fitts’ law to eye gaze interaction. Paper presented at the Proceedings of CHI 2000, The Hague, The Netherlands.

Moore, T. (2006). The neurobiology of visual attention: Finding sources. Current opinion in neurobiology, 16(2), 159-165.

Nikolaev, A. R., Nakatani, C., Plomp, G., Jurica, P., & van Leeuwen, C. (2011). Eye fixation-related potentials in free viewing identify encoding failures in change detection. NeuroImage, 56(3), 1598-1607.

Ortiz de Guinea, A., & Markus, M L. (2009). Why break the habit of a lifetime? Rethinking the roles of intention, habit, and emotion in continuing information technology use. MIS Quarterly, 33(3), 433-444.

Ortiz de Guinea, A., & Markus, M. L. (2010). Applying evolutionary psychology to the study of postadoption information technolgoy use: Reinforcement, extension, or revolution? In N. Kock (Ed.), Evolutionary psychology and information systems research: A new aprpoach to studying the effects of modern technologies on human behavior (pp. 61-83). New York, NY: Springer.

Ortiz de Guinea, A., Titah, R., & Léger, P.-M. (2014). Explicit and implicit antecedents of users’ information systems behavioral beliefs: A neuropsychological investigation. Journal of Management Information Systems, 30(4), 179-210.

Ortiz de Guinea, A., & Webster, J. (2013). An investigation of information systems use patterns: Technological events as triggers, the effects of time, and consequences for performance. MIS Quarterly, 37(4), 1165-1188.

Parasuraman, R., & Rizzo, M. (2008). Neuroergonomics: The brain at work: New York, NY: Oxford University Press.

Pizzagalli, D. A., Oakes, T. R., & Davidson, R. J. (2003). Coupling of theta activity and glucose metabolism in the human rostral anterior cingulate cortex: An EEG/PET study of normal and depressed subjects. Psychophysiology, 40(6), 939-949.

Polich, J. (2007). Updating P300: An integrative theory of P3a and P3b. Clinical neurophysiology: Official Journal of the International Federation of Clinical Neurophysiology, 118(10), 1-41.

Posner, M. I. (2012). Attention in a social world. New York, NY: Oxford University Press.

Posner, M. I., & Petersen, S.E. (1990). The attention system of the human brain. Annual Reviews in Neuroscience, 13(1), 25-42.

Qiu, L., & Benbasat, I. (2009). Evaluating anthropomorphic product recommendation agents: A social relationship perspective to designing information systems. Journal of Management Information Systems, 25(4), 145-182.

Rämä, P. I. A., & Baccino, T. (2010). Eye fixation–related potentials (EFRPs) during object identification. Visual Neuroscience, 27(5-6), 187-192.

Riedl, R., Banker, R. D., Benbasat, I., Davis, F. D., Dennis, A. R., Dimoka, A., Gefen, D., Gupta, A., Ischebeck, A., Kenning, P., Pavlou, P. A., Müller-Putz, G., Straub, D. W., vom Brocke, J., & Weber, B. (2010). On the foundations of NeuroIS: Reflections on the Gmunden Retreat 2009. Communications of the Association for Information Systems, 27(15).

Salvucci, D. D., & Goldberg, J. H. (2000). Identifying fixations and saccades in eye-tracking protocols. Proceedings of the 2000 Symposium on Eye tracking Research & Applications, 71-68.

Senecal, S., & Nantel, J. (2004). The influence of online product recommendations on consumers’ online choices. Journal of Retailing, 80(2), 159-169.

Sereno, S. C., & Rayner, K. (2003). Measuring word recognition in reading: eye movements and event-related potentials. Trends in cognitive sciences, 7(11), 489-493.

Silva, L. (2007). Post-positivist review of technology acceptance model. Journal of the Association for Information Systems, 8(4), 255-266.

Skipper, J. L, Goldin-Meadow, S., Nusbaum, H. C., & Small, S. L. (2007). Speech-associated gestures, Broca’s area, and the human mirror system. Brain and language, 101(3), 260-277.

Stampe, D. M., & Reingold, E. M. (1995). Selection by looking: A novel computer interface and its application to psychological research. In J. M. Findlay, R. Walker, & R. W. Kentridge (Eds.), Eye movement research: Mechanisms, processes and applications (pp. 467-478). Amsterdam: Elsevier Science Publishers.

Surakka, V., Illi, M., & Isokoski, P. (2003). Voluntary eye movements in human–computer interaction. In J Hyona, R. Radach, & H. Deubel (Eds.), The mind’s eye: Cognitive and applied aspects of eye movement research (pp. 73-491). Amsterdam: Elsevier Science.

Takeda, Y., Yoshitsugu, N., Itoh, K., & Kanamori, N. (2012). Assessment of attentional workload while driving by eye-fixation-related potentials. Kansei Engineering International Journal, 11, 121-126.

Thornhill, D. E, & Van Petten, C. (2012). Lexical versus conceptual anticipation during sentence processing: Frontal positivity and N400 ERP components. International Journal of Psychophysiology, 83(3), 382-392.

Tobii Technology (2011). Accuracy and precision test method for remote eye trackers (Test Specification Version 2.1.1). Retrieved from http://www.tobii.com/Global/Analysis/Training/Metrics/ Tobii\_Test\_Specifications\_Accuracy\_and\_PrecisionTestMethod\_version%202\_1\_1\_.pdf Tobii. Test, Specifications. Accuracy, and PrecisionTestMethod version%202, 1 1pdf

Vigário, R.N. (1997). Extraction of ocular artefacts from EEG using independent component analysis. Electroencephalography and clinical neurophysiology, 103(3), 395-404.

vom Brocke, J., Riedl, R., & Léger, P.-M. (2013). Application strategies for neuroscience in information systems design science research. Journal of Computer Information Systems, 53(3), 1-13.

Wood, W., Quinn, J. M., & Kashy, D. A. (2002). Habits in everyday life: Thought, emotion, and action. Journal of personality and social psychology, 83(6), 1281-1297.

## About the Authors

Pierre-Majorique LÉGER is a Full Professor of Information Systems at HEC Montréal. He holds a PhD in industrial engineering from École Polytechnique de Montréal and has done post-doctoral studies in information technologies at HEC Montréal and NYU Stern. He is also Invited professor at Henry B. Tippie College of Business (University of Iowa) and Tuck School of Business (Dartmouth University). He is the director of the ERPsim Lab and co-director of Tech3Lab. He is the principal inventor of ERPsim, a simulation game to teach ERP concepts, which is now used in more than 180 universities worldwide and many Fortune 1000 organisations. He has published articles in the Journal of the Association for Information Systems, Journal of Management of Information Systems, Information & Management, Technovation, Computers in Human Behaviour, and many others.

Sylvain SÉNÉCAL is Full Professor of Marketing, RBC Financial Group Chair of E-Commerce, and Co-director of the Tech3Lab at HEC Montreal. He holds a PhD in Marketing from HEC Montreal. His research focuses on Online Consumer Behavior, Electronic Commerce, And Consumer Neuroscience. His work has been published in journals such as Journal of Retailing, Information & Management, and International Journal of Electronic Commerce. Prior to his academic career, he held marketing positions at Arcelor Mittal.

François COURTEMANCHE is a postdoctoral researcher at the Tech3lab at HEC Montréal. He holds a PhD in computer science from the University of Montréal and a MSc in computer science from the University of Sherbrooke. He is a member of the Executive Committee and the operation manager of the Tech3Lab. He works in human-computer interactions. His main research focuses on physiological computing, eye tracking, and machine learning. His work has been published in journals such as Interacting with Computers and Applied Artificial Intelligence.

Ana ORTIZ DE GUINEA is an Associate Professor of Information Systems at HEC Montréal. She holds a PhD in Information Systems from Queen’s University, a MSc from the University of Lethbridge, and a degree in Computer Science and Engineering from the Universidad de Deusto. Prior to returning to academia, she worked as an Information Systems consultant. Her previous research has been published in many scientific journals, including Computers in Human Behavior, Information & Management, Journal of Management Information Systems, and MIS Quarterly.

Ryad TITAH is an Associate Professor of Information Systems at HEC Montréal. His main research interests are in information technology acceptance, use and impact in both public and private organizations. His work has been published in journals such as Computers in Human Behavior, Information Systems Research, Information Technology and People, International Journal of Electronic Government Research, Journal of Management Information Systems, and MIS Quarterly. He currently serves as a Senior Editor at Organization Studies and an Associate Editor at the European Journal of Information Systems.

Marc FREDETTE is an Associate Professor in Management Sciences at HEC Montréal. He holds a PhD in Statistics from the University of Waterloo. He is a member of the Executive Committee of the Tech3Lab and he is in charge of the Consultation Center in Statistics at HEC Montréal. He is also an Associate Editor for Statistical Modelling. He has published articles in journals such as Biometrika, Technometrics, Computational Statistics & Data Analysis, the Canadian Medical Association Journal, and Accident Analysis and Prevention.

Élise LABONTÉ-LEMOYNE is a postdoctoral researcher at HEC Montréal. She holds a PhD in Exercise Science from the University of Montreal and specializes in electroencephalography. Her previous research has been published in Trials and in the Journal of Clinical and Experimental Neuropsychology.
